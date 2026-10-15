---
title: "BI 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 220
source_pdf: "06_开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/quickbi/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# BI 开发指南

Quick BI 色

## 批量更新工作空间成员的角色

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| UserIds | Strin g | Query | 是 | 136516262323****,1244 98444445**** | 用户ID。此处为Quick BI的 UserID，而非阿里云的 UID。 支持批量传参，用户ID之间用半角逗号（,）隔开。 |
| RoleId | Long | Query | 是 | 25 | 用户在工作空间内的角色 ID。取值范围： 25：空间管理员 26：开发者 27：分析者 30：阅览者 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7AAB95D7-2E11- 4FE2-94BC- 858E4FC0C976 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功，存在部分成员修改成功，部分修改失败的情况，失败的原因参考返回结果中的FailureDetail false：请求失败，不会持久化任何数据 |
| Result | Struct |  | 返回接口执行结果。 |
| -Failure | Integer |  |  |
| -FailureDetail | Map |  |  |
| -Total | Integer |  |  |
| -Success | Integer |  |  |

Quick BI 色

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateWorkspaceUsersRole &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserIds=136516262323****,124498444445**** &RoleId=25
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7AAB95D7-2E11-4FE2-94BC-858E4FC0C976",
 "Success":true,
 "Result":{
  "FailureDetail":"",
  "Total":"",
  "Failure":"",
  "Success":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010008 | Workspace.Type.Error | The type of group workspace is invalid. |
| 400 | AE0150010013 | User.Not.WorkspaceAdmin | Only administrators of the group workspace can perform this operation. |
| 400 | AE0150010014 | Remove.AdminRoleOf.Workspa ceOwner | The owner of the group workspace must be assigned the administrator role. |
| 400 | AE0150010004 | User.NotIn.Workspace | The user is not a member of the group workspace. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |

| Quick BI |  |  | 开发指南·批量更新工作空间成员的角色 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 修改工作空间成员角色

修改工作空间下指定成员的角色。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| UserId | Strin g | Query | 是 | f5698bedeb384b1986af ccd9e434**** | Quick BI用户ID。 |
| RoleId | Long | Query | 是 | 25 | 空间成员角色ID。 25：管理员 26：开发者 27：分析者 30：阅览者 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateWorkspaceUserRole &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserId=f5698bedeb384b1986afccd9e434**** &RoleId=25
```

&公共请求参数正常返回示例 Quick BI `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010008 | Workspace.Type.Error | The type of group workspace is invalid. |
| 400 | AE0150010013 | User.Not.WorkspaceAdmin | Only administrators of the group workspace can perform this operation. |
| 400 | AE0150010004 | User.NotIn.Workspace | The user is not a member of the group workspace. |
| 400 | AE0150010014 | Remove.AdminRoleOf.Workspa ceOwner | The owner of the group workspace must be assigned the administrator role. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 | AE0150010003 | User.AlreadyIn.Role | The user is already assigned this role. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

| 开发指南·修改工 | 作空间成员角色 |  | Quick B |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 更新组织成员标签值

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 待修改标签值的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |
| TagId | Strin g | Query | 是 | pop 001 _ | 待修改的标签ID。 |
| TagValue | Strin g | Query | 是 | 产品总监 | 待修改的标签值。 如果需要清除该标签，则设置标签值为 （$NULL$）。 多值请用英文逗号分割。 格式校验，最大长度： 3000字符 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 46e5374665ba4b6 79ee22e2a29270 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回修改用户标签的结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例 Quick BI

```
http(s)://[Endpoint]/?Action=UpdateUserTagValue &UserId=fe67f61a35a94b7da1a34ba174a7**** &TagId=pop_001
```

`&TagValue=`产品总监 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"46e5374665ba4b679ee22e2a29270",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100023 | UserTag.NotIn.CurrentOrganiz ation | The user tag is not in the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

Quick BI

## 更新组织成员标签元信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TagId | Strin g | Query | 是 | e82f6c6c0333431bad02 25b2f85e**** | 指定的TagID。 格式检查：最大长度64 个字符。 |
| TagName | Strin g | Query | 是 | 职位 | 标签名称。 格式检查：最大长度50 个字符。 只允许输入中英文数字和/\|符号。 |
| TagDescri ption | Strin g | Query | 否 | 部门内的工作职位 | 标签描述。 格式检查：最大长度255 个字符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口是否执行成功。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUserTagMeta &TagId=e82f6c6c0333431bad0225b2f85e****
```

`&TagName=`职位 &公共请求参数 Quick BI 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100023 | UserTag.NotIn.CurrentOrganiz ation | The user tag is not in the current organization. |
| 400 | AE0150100025 | TagName.Repeat | The tag name is duplicated. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 更新用户组信息

更新组织下指定用户组的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 是 | f5eeb52e-d9c2-4a8b- 80e3-47ab55c2**** | 用户组ID。 |
| UserGrou pName | Strin g | Query | 否 | pop0001 | 用户组名称。 格式校验：最大长度255 特殊格式校验：中英文数字 \ / \| () ] [ _ |
| UserGrou pDescripti on | Strin g | Query | 否 | 描述信息 | 用户组描述。 格式校验：最大长度255 特殊格式校验：中英文数字 \ / \| () ] [ _ |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4AEF8C5C-D5D2- 55D3-BB2F- 9D3AA1B6F4FA | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口是否执行成功。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUserGroup &UserGroupId=f5eeb52e-d9c2-4a8b-80e3-47ab55c2****
```

&公共请求参数正常返回示例 Quick BI `JSON` 格式

```json
{
 "RequestId":"4AEF8C5C-D5D2-55D3-BB2F-9D3AA1B6F4FA",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 | AE0150020301 | UserGroup.Remove.RootNode | The root user group cannot be deleted. |
| 400 | AE0150020302 | UserGroup.Remove.WithChildr en | This user group contains a child user group and cannot be deleted. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 更新组织成员信息

更新组织下指定成员的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 待更新的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |
| AdminUse r | Boole an | Query | 是 | true | 是否是组织管理员。取值范围： true：是 false：否 |
| AuthAdmi nUser | Boole an | Query | 是 | true | 是否是权限管理员。取值范围： true：是 false：否 |
| UserType | Integ er | Query | 是 | 1 | 组织成员的角色类型。取值范围： 1 ：开发者 2 ：访问者 3 ：分析师 |
| NickName | Strin g | Query | 是 | 小张 | 昵称。 格式检查：最大长度50 个字符。 特殊格式校验：中英文数字 \ / \| () ] [ _ |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUser &UserId=fe67f61a35a94b7da1a34ba174a7**** &AdminUser=true &AuthAdminUser=true &UserType=1
```

`&NickName=`小张 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0150100010 | NickName.AlreadyIn.Organizati on | The alias already exists. |
| 400 | AE0150100006 | Fobbiden.Action | The organization owner must have the administrator role. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0520010021 | Organization.Developers.Reac hedTheUpperLimit | The developers of the organization have reached the upper limit:%s |

| Quick BI |  |  | 开发指南·更新组织成员信息 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010023 | Organization.Viewers.Reached TheUpperLimit | The visitors of the organization have reached the upper limit:%s. |
| 400 | AE0520010022 | Organization.Analysts.Reached TheUpperLimit | The analysts of the organization have reached the upper limit:%s. |
| 400 | AE0520010013 | Instance.Over.MaxLicense | You have reached the maximum number of users that can be added. Please upgrade the configurations or remove some users first. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

Quick BI

## 更新嵌入ticket票据数量

对用于免登嵌入报表的指定的ticket进行更新票据数量操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ticket | Strin g | Query | 是 | 040e6f79d33444838*** 83c7206c070 | 三方嵌入的票据值，即URL 中的accessTicket值。 |
| TicketNu m | Integ er | Query | 是 | 1 | 票据数。 取值范围：1~99998， 建议值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 是否更新成功。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTicketNum &Ticket=040e6f79d33444838***83c7206c070 &TicketNum=1
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0130010022 | Authorize3rdTicket.BindedWor ks.Mismatch | The report bound by the ticket mismatches the actual report. |
| 400 | AE0130010024 | Authorize3rdTicket.Expired | Ticket [%s] has expired. |
| 400 | AE0130010027 | Authorize3rdTicket.HasNo.Logi nToken | The request [%s] has no token. |
| 400 | AE0130010023 | Authorize3rdTicket.NotExist | Ticket %s does not exist. |
| 400 | AE0130010025 | Authorize3rdTicket.Num.Excee d | The number of tickets %s is invalid. |
| 400 | AE0130010026 | Authorize3rdTicket.Num.HasN oLeft | There is no ticket number left, please generate new ticket. |
| 400 | AE0510200000 | NoPermissionTo.Operate.Objec t | You are not authorized to operate the objects. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |

Quick BI 态

## 更新数据集行列权限开关状态

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 7c7223ae-****- 3c744528014b | 数据集ID。 |
| RuleType | Strin g | Query | 是 | ROW LEVEL _ | 数据集行列权限类型。取值范围： ROW LEVEL：行级权限 _ COLUMN LEVEL：列级 _ 权限 |
| IsOpen | Integ er | Query | 是 | 1 | 更新行列权限开关状态。取值范围： 1：打开 0：关闭 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDataLevelPermissionStatus &CubeId=7c7223ae-****-3c744528014b &RuleType=ROW_LEVEL &IsOpen=1
```

&公共请求参数 Quick BI 态正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 设置行级权限白名单

设置指定行级权限的白名单列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WhiteList Model | Strin g | Query | 是 | {"ruleType":"ROW LEVE _ L","usersModel": {"userGroups": ["26edcb76-****- bdbab78267cb","187e6 dd5-1611-4cf7-a034- 1a93bd5fecf9"],"users": ["4334***358","Huang** *3fa822"]},"cubeId":"7c 7223ae- ****44528014b"} | { "ruleType": "ROW LEVEL", // 行级权 _ 限类型 "usersModel": { "userGroups": [ "0d5fb19b-***- 1248fc27ca51", // 用户组 ID "3d2c23d4-***- f6390f325c2d" ], "users": [ "4334***358", // Quick BI用户的UserID "Huang***3fa822" ] }, "cubeId": "7c7223ae- 31d1-4d2f-b11f- 3c744528014b" } |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例 Quick BI

```json
http(s)://[Endpoint]/?Action=SetDataLevelPermissionWhiteList &WhiteListModel={"ruleType":"ROW_LEVEL","usersModel":{"userGroups":["26edcb76-****-bdba b78267cb","187e6dd5-1611-4cf7-a034-1a93bd5fecf9"],"users": ["4334***358","Huang***3fa822"]},"cubeId":"7c7223ae-****44528014b"}
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 置信息

## 设置单条数据集行列权限配置信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RuleModel | Strin g | Query | 是 | { "cubeId": "aa574353- 41cf-****-8d0d- 455176c101fa", "hitTakeEffect": 1, "isOpen": 1, "permissionMode": "COMPLEX", "ruleContentModel": { "ruleContent": { "pathId": [ "264b7a970b" ] }, "ruleContentJson": " {\"pathId\": [\"264b7a970b\"]}", "ruleContentType": "COLUMN FORBID" _ }, "ruleId": "3971fa8e- f7e0-****-b6e3- 5b3167dd7247", "ruleLevelType": "COLUMN LEVEL", _ "ruleName": "规则名称", "ruleTargetScope": "ALL" | { "rule": "a5bb24da-- a891683e14da", // 行列权限规则的ID,当传入时为修改行级权限规则,否则新增 "cubeId": "7c7223ae- -3c744528014b", // 数据集ID "ruleName": "测试行级权限", // 行级权限规则的名称 "ruleLevelType": "ROW LEVEL", // 行级权 _ 限类型：ROW LEVEL：行 _ 级权限,COLUMN LEVEL： _ 列级权限 "ruleTargetScope": "ALL", // 行级权限规则针对的人群：1：所有人,2：指定人 "hitTakeEffect": 1, //命中后规则生效还是不生效（针对列级权限）：1：生效 （默认生效）,0：不生效 "ruleUsersModel": { "userGroups": [ "9bd2c6440ac542589f1 6bf12ca8178dd", // 用户组人群的用户组ID "0d5fb19b- -1248fc27ca51", "3d2c23d4-- f6390f325c2d" ], "users": [ "43342 3784358", // 用户人群的 UserID "Huang2e3fa822" ] }, "ruleContentModel": { "ruleContentType": "ROW FIELD", // 行列权 _ 限的规则类型 "ruleContentJson": " {"conditionNode": {"caption":"周期","isMeasure":false, |

Quick BI 置信息

| 参数名称 | 类型 | 位置 | 是否必选 | } 示例 | "pathId":"7d3b 说明 bc6","relationOperato |
|---|---|---|---|---|---|
|  |  |  |  |  | r":"not- null","name":"7d3b bc6","value":{"value": [""],"valueType":"ENUM" }}}", // 规则的JSON字符串 "ruleOriginConfigJson": " {"operator":"and","oper ands":[{"labelName":"周期","isValid":true,"uniqu eId":"5","fieldId":"7d3b* **bc6","error":false,"fiel dType":"string","default Value": {"selectType":"condition ","value": {"conditionOp":"not- null","conditionValue":"" },"valueType":"ENUM"} }],"isRelation":true}" // 前端模板要是用的JSON结果 （行级权限专用） } } |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |

Quick BI 置信息

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Result | String | { "cubeId": "aa574353-41cf- ****-8d0d- 455176c101fa", "hitTakeEffect": 1, "isOpen": 1, "permissionMode": "COMPLEX", "ruleContentModel ": { "ruleContent": { "pathId": [ "264b7a970b" ] }, "ruleContentJson": "{\"pathId\": [\"264b7a970b\"]}" , "ruleContentType": "COLUMN FORBID" _ }, "ruleId": "3971fa8e-f7e0- ****-b6e3- 5b3167dd7247", "ruleLevelType": "COLUMN LEVEL", _ "ruleName": "规则名称", "ruleTargetScope": "ALL" } | 保存成功的行列权限信息。 |

**示例**

请求示例 Quick BI 置信息

```json
http(s)://[Endpoint]/?Action=SetDataLevelPermissionRuleConfig &RuleModel={
    "cubeId": "aa574353-41cf-****-8d0d-455176c101fa",
    "hitTakeEffect": 1,
    "isOpen": 1,
    "permissionMode": "COMPLEX",
    "ruleContentModel": {
        "ruleContent": {
            "pathId": [
                "264b7a970b"
```

]

```json
        },
        "ruleContentJson": "{\"pathId\":[\"264b7a970b\"]}",
        "ruleContentType": "COLUMN_FORBID"
    },
    "ruleId": "3971fa8e-f7e0-****-b6e3-5b3167dd7247",
    "ruleLevelType": "COLUMN_LEVEL",
```

`"ruleName": "`规则名称`",`

```json
    "ruleTargetScope": "ALL"
}
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":"{    \"cubeId\": \"aa574353-41cf-****-8d0d-455176c101fa\",
\"hitTakeEffect\": 1, \"isOpen\": 1, \"permissionMode\": \"COMPLEX\", \"ruleContentModel\": { \"ruleContent\": { \"pathId\": [ \"264b7a970b\" ] }, \"ruleContentJson\": \"{\\\"pathId\\\":[\\\ "264b7a970b\\\"]}\", \"ruleContentType\": \"COLUMN_FORBID\" }, \"ruleId\": \"3971fa8e-f7e0-****-b6e3-5b3167dd7247\", \"ruleLevelType\": \"COLUMN_LEVEL\", \" ruleName\": \"规则名称\", \"ruleTargetScope\": \"ALL\"}" }
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030031 | CubePermission.ColumnlevelFi eld.Repeat | There are duplicate field configurations. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |

| 开发指南·设置单置信息 | 条数据集行列权限配 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 设置行列权限额外配置

设置行列权限的额外配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 7c7223ae-******- 3c744528014b | 数据集ID。 |
| RuleType | Strin g | Query | 是 | ROW LEVEL _ | 数据集行列权限类型。取值范围： ROW LEVEL：行级权限 _ COLUMN LEVEL：列级 _ 权限 |
| MissHitPol icy | Strin g | Query | 是 | NONE | 未命中规则时的策略： NONE：无权限 ALL：拥有所有权限 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | B70E1FBD-E533- 52F2-A7A1- E02B92F78DDF | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetDataLevelPermissionExtraConfig &CubeId=7c7223ae-******-3c744528014b &RuleType=ROW_LEVEL &MissHitPolicy=NONE
```

&公共请求参数 Quick BI 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"B70E1FBD-E533-52F2-A7A1-E02B92F78DDF",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 添加作品收藏

添加用户的收藏数据作品。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 121344444790**** | 收藏作品的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |
| WorksId | Strin g | Query | 是 | d23e84a1-82a0-4292- bfdb-521306c3**** | 收藏作品的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SaveFavorites &UserId=121344444790**** &WorksId=d23e84a1-82a0-4292-bfdb-521306c3****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0550010012 | Workspace.Status.Error | This group workspace has been disabled or deleted. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 自定义审批流回调接口

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Applicatio nId | Strin g | Query | 是 | c5ea0db8-****-****- 9081-04bc0df4c6a3 | 审批流的ID。 |
| HandleRe ason | Strin g | Query | 是 | 你不是A部门分析师。 | 审批理由。 |
| Status | Integ er | Query | 是 | 1 | 审批结果： 1：通过 2：拒绝 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ResultCallback &ApplicationId=c5ea0db8-****-****-9081-04bc0df4c6a3
```

`&HandleReason=`你不是A部门分析师。

```
&Status=1
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0510200019 | Application.Object.NotExist | The object you are operating does not exist or has been deleted. |
| 400 | AE0580800021 | Application.RecordClosed | The closed application record cannot be operated. |
| 400 | AE0580800013 | Application.NotExist | The application is not exists. |

Quick BI

## 查询工作空间下的成员列表

查询指定工作空间下的成员列表信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| Keyword | Strin g | Query | 否 | 分析 | 工作空间成员用户名的关键字。 |
| PageNum | Integ er | Query | 否 | 1 | 工作空间成员列表的当前页码： 起始值：1 默认值：1 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时的每页行数： 默认值：10 最大值：1000 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回成员列表的分页结果，成员的详细信息列表存放在返回参数Data中。 |
| -Data | Array |  |  |
| --Email | String |  |  |
| --UserId | String |  |  |
| --AccountId | String |  |  |
| --NickName | String |  |  |

| 开发指南·查询工作空 | 间下的成员列表 |  | Quick B |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Phone | String |  |  |
| -- AccountName | String |  |  |
| --Role | Struct |  |  |
| ---RoleCode | String |  |  |
| ---RoleName | String |  |  |
| ---RoleId | Long |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryWorkspaceUserList &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Email":"",
   "AccountId":"",
   "UserId":"",
   "Phone":"",
   "NickName":"",
   "--Role":{
    "RoleName":"",
    "RoleCode":"",
    "RoleId":""
   },
   "AccountName":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

| 开发指南·查询工 | 作空间下的成员列表 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

Quick BI

## 查询工作空间下的所有作品

查询组织下某个工作空间下的所有作品，可指定作品类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 89713491-cb4f-4579- b889-e82c35f1**** | 工作空间ID。 |
| WorksTyp e | Strin g | Query | 否 | PAGE | 作品类型。取值范围： DATAPRODUCT：数据门户 PAGE：仪表板 FULLPAGE：全屏仪表板 REPORT：电子表格 |
| Status | Integ er | Query | 否 | 0 | 作品状态。取值范围： 0：未发布 1：已发布 2：已修改未发布 3：已下线 |
| ThirdPartA uthFlag | Integ er | Query | 否 | 0 | 第三方嵌入状态。取值范围： 0：暂未开通嵌入 1：已开通嵌入 |
| PageNum | Integ er | Query | 否 | 1 | 页码。 默认值1。 |
| PageSize | Integ er | Query | 否 | 10 | 每页行数。 默认值10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回组织工作空间下所有符合请求条件的作品列表。 |
| -Data | Array |  |  |
| --Status | Integer |  |  |
| --GmtModify | String |  |  |
| --Auth3rdFlag | Integer |  |  |
| --WorksId | String |  |  |
| --WorkType | String |  |  |
| --OwnerName | String |  |  |
| -- WorkspaceNa me | String |  |  |
| --OwnerId | String |  |  |
| --ModifyName | String |  |  |
| --WorkspaceId | String |  |  |
| --SecurityLevel | String |  |  |
| --Description | String |  |  |
| --WorkName | String |  |  |
| --GmtCreate | String |  |  |
| --Directory | Struct |  |  |
| ---PathId | String |  |  |
| ---PathName | String |  |  |
| ---Name | String |  |  |
| ---Id | String |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |

| Quick BI |  |  | 开发指南·查询工作空间下的所有作品 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryWorksByWorkspace &WorkspaceId=89713491-cb4f-4579-b889-e82c35f1****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Status":"",
   "OwnerName":"",
   "Description":"",
   "--Directory":{
    "PathId":"",
    "PathName":"",
    "Id":"",
    "Name":""
   },
   "WorkType":"",
   "ModifyName":"",
   "WorkspaceId":"",
   "Auth3rdFlag":"",
   "GmtCreate":"",
   "OwnerId":"",
   "GmtModify":"",
   "SecurityLevel":"",
   "WorkName":"",
   "WorkspaceName":"",
   "WorksId":""
  }
 }
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询组织下的所有作品

查询整个组织下的所有作品，可指定作品类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksTyp e | Strin g | Query | 否 | PAGE | 查询作品的类型，填空为查询所有类型。取值范围： DATAPRODUCT：数据门户 PAGE：仪表板 FULLPAGE：全屏仪表板 REPORT：电子表格 dashboardOfflineQuer y：自助取数 |
| Status | Integ er | Query | 否 | 0 | 查询作品的状态。取值范围： 0：未发布 1：已发布 2：已修改未发布 3：已下线 |
| ThirdPartA uthFlag | Integ er | Query | 否 | 1 | 第三方嵌入状态。取值范围： 0：暂未开通嵌入 1：已开通嵌入 |
| PageNum | Integ er | Query | 否 | 1 | 页码。 默认值1。 |
| PageSize | Integ er | Query | 否 | 10 | 每页行数。 默认值10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回组织下所有符合请求条件的作品列表。 |
| -Data | Array |  |  |
| --Status | Integer |  |  |
| --Auth3rdFlag | Integer |  |  |
| --GmtModify | String |  |  |
| --WorksId | String |  |  |
| --WorkType | String |  |  |
| --OwnerName | String |  |  |
| -- WorkspaceNa me | String |  |  |
| --OwnerId | String |  |  |
| --ModifyName | String |  |  |
| --WorkspaceId | String |  |  |
| --SecurityLevel | String |  |  |
| --Description | String |  |  |
| --WorkName | String |  |  |
| --GmtCreate | String |  |  |
| --Directory | Struct |  |  |
| ---PathId | String |  |  |
| ---PathName | String |  |  |
| ---Name | String |  |  |
| ---Id | String |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |

| Quick BI |  |  | 开发指南·查询组织下的所有作品 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryWorksByOrganization
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Status":"",
   "OwnerName":"",
   "Description":"",
   "--Directory":{
    "PathId":"",
    "PathName":"",
    "Id":"",
    "Name":""
   },
   "WorkType":"",
   "ModifyName":"",
   "WorkspaceId":"",
   "Auth3rdFlag":"",
   "GmtCreate":"",
   "OwnerId":"",
   "GmtModify":"",
   "SecurityLevel":"",
   "WorkName":"",
   "WorkspaceName":"",
   "WorksId":""
  }
 }
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0510000005 | Parameter.Validation.Failed | Parameter validation failed. |

Quick BI

## 查询数据作品的血缘信息

获取数据作品的血缘关系，包括各组件引用的数据集以及查询字段信息。目前仅支持的数据作品包含仪表板、电子表格、自助取数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | abcd**** | 数据作品的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 作品血缘信息列表。 |
| -QueryParams | Array |  | 查询参数引用列的列表。 |
| --Uid | String |  |  |
| --PathId | String |  |  |
| --Caption | String |  |  |
| --DataType | String |  |  |
| --IsMeasure | Boolean |  |  |
| --AreaId | String |  |  |
| --AreaName | String |  |  |
| -ComponentId | String | 0696083a-ca72- 4d89-8e7a- c017910e0*** | 组件ID。 |
| - ComponentNa me | String | 线图 | 组件名称。 |

| 开发指南·查询数据作 | 品的血缘信息 |  | Quick B |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ComponentTy pe | Integer | 3 | 组件类型。 |
| - ComponentTy peName | String | LINE | 组件类型名称。 |
| -DatasetId | String | dc78a4ed-880d- 452e-b017- 90cfc10c83e5 com _ pany sales record _ _ | 数据集ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryWorksBloodRelationship &WorksId=abcd****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "ComponentType":3,
  "ComponentTypeName":"LINE",
  "ComponentName":"线图",
  "ComponentId":"0696083a-ca72-4d89-8e7a-c017910e0***",
  "-QueryParams":{
   "PathId":"",
   "AreaName":"",
   "Uid":"",
   "IsMeasure":"",
   "AreaId":"",
   "DataType":"",
   "Caption":""
  },
  "DatasetId":"dc78a4ed-880d-452e-b017-90cfc10c83e5_company_sales_record"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Invalid.Works.Empty | works not exist,the report has been deleted!reportId:%s |

| Quick BI |  |  | 开发指南·查询数据作品的血缘信息 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0581060004 | Invalid.WorksId.Not.Publish | works %s is not published yet |
| 400 | AE0150100012 | Invalid.Workspace | workspace not in organization |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询数据作品信息

查询指定数据作品信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | abcd**** | 报表ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 作品详情信息。 |
| -WorksId | String |  |  |
| -WorkType | String |  |  |
| -WorkName | String |  |  |
| -WorkspaceId | String |  |  |
| - WorkspaceNa me | String |  |  |
| -SecurityLevel | String |  |  |
| -Auth3rdFlag | Integer |  |  |
| -Description | String |  |  |
| -OwnerId | String |  |  |
| -OwnerName | String |  |  |
| -ModifyName | String |  |  |
| -GmtCreate | String |  |  |

| Quick BI |  |  | 开发指南·查询数据作品信息 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -GmtModify | String |  |  |
| -Status | Integer |  |  |
| -Directory | Struct |  |  |
| --Id | String |  |  |
| --Name | String |  |  |
| --PathId | String |  |  |
| --PathName | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryWorks &WorksId=abcd****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "Status":"",
  "OwnerName":"",
  "Description":"",
  "WorkType":"",
  "ModifyName":"",
  "WorkspaceId":"",
  "Auth3rdFlag":"",
  "GmtCreate":"",
  "OwnerId":"",
  "GmtModify":"",
  "WorkName":"",
  "SecurityLevel":"",
  "WorkspaceName":"",
  "-Directory":{
   "PathId":"",
   "Id":"",
   "PathName":"",
   "Name":""
  },
  "WorksId":""
 }
}
```

Quick BI

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0110130007 | Invalid.Works.Empty | works not exist! |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0510130015 | Resource.NotBelongTo.Current Organization | The resource does not belong to the current organization. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询组织成员标签值列表

查询特定用户标签值列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 返回用户标签及标签值列表的请求结果。 |
| -TagValue | String | 主管 | 标签的值。 |
| -TagName | String | 职位 | 标签名称。 |
| -TagId | String | pop 001 _ | 标签 ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserTagValueList &UserId=fe67f61a35a94b7da1a34ba174a7****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TagName":"职位",
  "TagId":"pop_001",
  "TagValue":"主管"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100023 | UserTag.NotIn.CurrentOrganiz ation | The user tag is not in the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

Quick BI 表

## 查询组织成员标签元信息列表

查询组织内成员标签元信息列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 返回组织内的用户标签列表。 |
| -TagName | String | 职位 | 标签名称。 |
| - TagDescriptio n | String | 用于区分部分职位 | 标签描述。 |
| -TagId | String | pop 001 _ | 标签 ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserTagMetaList
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TagName":"职位",
```

`"TagDescription":"`用于区分部分职位`",`

```json
  "TagId":"pop_001"
 }
}
```

**错误码**

Quick BI 表

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询工作空间成员的角色

获取指定工作空间下的成员角色信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | f5698bedeb384b1986af ccd9e434**** | Quick BI用户ID。 |
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 成员的角色信息。 |
| -RoleCode | String |  |  |
| -RoleName | String |  |  |
| -RoleId | Long |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserRoleInfoInWorkspace &UserId=f5698bedeb384b1986afccd9e434**** &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "RoleName":"",
  "RoleCode":"",
  "RoleId":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 | AE0150010004 | User.NotIn.Workspace | The user is not a member of the group workspace. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询组织成员列表信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Keyword | Strin g | Query | 否 | 测试用户 | 组织成员用户名或昵称的关键字。 |
| PageNum | Integ er | Query | 否 | 1 | 组织成员列表的当前页码： 起始值：1 默认值：1 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时的每页行数： 默认值：10 最大值：1000 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回用户列表的分页结果，组织成员的详细信息列表存放在返回参数Data中。 |
| -Data | Array |  |  |
| --UserType | Integer |  |  |
| --Email | String |  |  |
| --UserId | String |  |  |
| -- AuthAdminUse r | Boolean |  |  |
| --AccountId | String |  |  |

|  | 开发指南·查询组织成 | 员列表信息 |  | Quick B | I |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --NickName | String |  |  |
| --AdminUser | Boolean |  |  |
| --Phone | String |  |  |
| -- AccountName | String |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserList
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Email":"",
   "AccountId":"",
   "UserId":"",
   "Phone":"",
   "AdminUser":"",
   "NickName":"",
   "UserType":"",
   "AuthAdminUser":"",
   "AccountName":""
  }
 }
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 根据用户ID查询用户信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 用户ID。此处的UserID为 Quick BI的UserID，而非阿里云的UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回的组织用户信息。 |
| -UserType | Integer |  |  |
| -Email | String |  |  |
| -UserId | String |  |  |
| - AuthAdminUse r | Boolean |  |  |
| -AccountId | String |  |  |
| -NickName | String |  |  |
| -AdminUser | Boolean |  |  |
| -Phone | String |  |  |
| -AccountName | String |  |  |

**示例**

请求示例 Quick BI

```
http(s)://[Endpoint]/?Action=QueryUserInfoByUserId &UserId=fe67f61a35a94b7da1a34ba174a7****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "Email":"",
  "AccountId":"",
  "UserId":"",
  "Phone":"",
  "AdminUser":"",
  "NickName":"",
  "UserType":"",
  "AuthAdminUser":"",
  "AccountName":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

Quick BI

## 根据账号查询用户信息

根据阿里云ID或阿里云账户名查询用户信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Account | Strin g | Query | 是 | 1386587****@163.com | 输入待查询的阿里云账号名或阿里云ID。 当输入账号名时： 如果组织用户是主账号 （例如 main account），则 _ 查询账号格式为主账号。即，要输入的主账号main account。 _ 如果组织用户是子账号 （例如 z***@test.ona liyun.com），则查询账号格式为子账号的头部，即，要输入的子账号为zhangsan。 当输入阿里云ID时： 输入完整的账号UID， 即可查询到对应的账号信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回的组织用户信息。 |
| -UserType | Integer |  |  |
| -Email | String |  |  |
| -UserId | String |  |  |

| Quick BI |  |  | 开发指南·根据账号查询用户信息 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - AuthAdminUse r | Boolean |  |  |
| -AccountId | String |  |  |
| -NickName | String |  |  |
| -AdminUser | Boolean |  |  |
| -Phone | String |  |  |
| -AccountName | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserInfoByAccount &Account=1386587****@163.com
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "Email":"",
  "AccountId":"",
  "UserId":"",
  "Phone":"",
  "AdminUser":"",
  "NickName":"",
  "UserType":"",
  "AuthAdminUser":"",
  "AccountName":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |
| 400 |  | Internal.System.Error | An internal system error occurred. |

| 开发指南·根据账 | 号查询用户信息 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

Quick BI

## 查询用户组成员列表

获取用户组下的成员列表信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 是 | 2fe4fbd8-588f-489a- b3e1-e92c7af0**** | 用户组ID。 |
| Keyword | Strin g | Query | 否 | 小刘 | 用户组成员用户名或昵称的关键字。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 48C930FF-DFCF- 5986-902B- E24C202E2443 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 用户组成员列表的请求结果。 |
| - ParentUserGro upName | String | 财务组 | 所属用户组名称。 |
| -IsUserGroup | Boolean | true | 是否为用户组。取值范围： true：用户组 false：用户 |
| -Name | String | 小刘的测试用户组 | 用户组名称或用户组成员昵称 。 |
| - ParentUserGro upId | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0**** | 所属用户组ID。 |
| -Id | String | 3d2c23d4-2b41- 4af8-a1f5- f6390f32**** | 用户组ID或用户组成员ID。 |

**示例**

Quick BI 请求示例

```
http(s)://[Endpoint]/?Action=QueryUserGroupMember &UserGroupId=2fe4fbd8-588f-489a-b3e1-e92c7af0****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"48C930FF-DFCF-5986-902B-E24C202E2443",
 "Success":true,
 "Result":{
  "ParentUserGroupName":"财务组",
  "ParentUserGroupId":"2fe4fbd8-588f-489a-b3e1-e92c7af0****",
  "IsUserGroup":true,
  "Id":"3d2c23d4-2b41-4af8-a1f5-f6390f32****",
```

`"Name":"`小刘的测试用户组"

```
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 列表

## 查询父用户组下的子用户组列表

获取指定父用户组下的子用户组信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ParentUse rGroupId | Strin g | Query | 是 | 3d2c23d4-2b41-4af8- a1f5-f6390f32**** | 父用户组ID。 当输入父用户组ID时，可以获取该ID下的子用户组信息。 当输入-1时，可以获取根目录下的子用户组信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 72B19D61-B37A- 5C7A-9389- 0856CD7935B3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 子用户组信息。 |
| -IdentifiedPath | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0****/3d2c 23d4-2b41-4af8- a1f5- f6390f32****/f5eeb 52e-d9c2-4a8b- 80e3- 47ab55c2**** | 子用户组的目录层级。 |
| -ModifiedTime | String | 2020-11-16 15:49:08 | 子用户组最新修改时间。 |
| -CreateUser | String | 136516262323**** | 子用户组创建者。此处为Quick BI的UserID，而非阿里云的UID。 |
| -CreateTime | String | 2020-10-30 10:03:09 | 子用户组创建时间。 |

Quick BI 列表

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -UserGroupId | String | f5eeb52e-d9c2- 4a8b-80e3- 47ab55c2**** | 子用户组ID。 |
| - UserGroupNa me | String | popapi测试分组 | 子用户组名称。 |
| -ModifyUser | String | 136516262323**** | 子用户组修改者。此处为Quick BI的UserID，而非阿里云的UID。 |
| - ParentUserGro upId | String | 3d2c23d4-2b41- 4af8-a1f5- f6390f32**** | 父用户组ID。 |
| - UserGroupDes cription | String | 用来测试的用户组 | 子用户组备注。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryUserGroupListByParentId &ParentUserGroupId=3d2c23d4-2b41-4af8-a1f5-f6390f32****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"72B19D61-B37A-5C7A-9389-0856CD7935B3",
 "Success":true,
 "Result":{
  "ParentUserGroupId":"3d2c23d4-2b41-4af8-a1f5-f6390f32****",
  "ModifyUser":"136516262323****",
  "ModifiedTime":"2020-11-16 15:49:08",
  "IdentifiedPath":"2fe4fbd8-588f-489a-b3e1-e92c7af0****/3d2c23d4-2b41-4af8-a1f5-f6390f
32****/f5eeb52e-d9c2-4a8b-80e3-47ab55c2****",
  "CreateTime":"2020-10-30 10:03:09",
  "UserGroupId":"f5eeb52e-d9c2-4a8b-80e3-47ab55c2****",
  "UserGroupName":"popapi测试分组",
  "CreateUser":"136516262323****",
```

`"UserGroupDescription":"`用来测试的用户组"

```
 }
}
```

**错误码**

Quick BI 列表

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020305 | UserGroup.NotIn.Organization | The user group is not in the current organization. |
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询嵌入报表ticket详情

获取免登嵌入报表的指定ticket的详情信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ticket | Strin g | Query | 是 | a27a9aec-****-****- bd40-1a21ea41d7c5 | 票据值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 生成的票据详情。 |
| -AccessTicket | String |  |  |
| - OrganizationId | String |  |  |
| -UserId | String |  |  |
| - UsedTicketNu m | Integer |  |  |
| - MaxTicketNum | Integer |  |  |
| -RegisterTime | String |  |  |
| -InvalidTime | String |  |  |
| -WorksId | String |  |  |
| -CmptId | String |  |  |
| -GlobalParam | String |  |  |
| - WatermarkPar am | String |  |  |

Quick BI

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryTicketInfo &Ticket=a27a9aec-****-****-bd40-1a21ea41d7c5
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "UsedTicketNum":"",
  "CmptId":"",
  "MaxTicketNum":"",
  "RegisterTime":"",
  "AccessTicket":"",
  "WatermarkParam":"",
  "UserId":"",
  "OrganizationId":"",
  "InvalidTime":"",
  "WorksId":"",
  "GlobalParam":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0130010022 | Authorize3rdTicket.BindedWor ks.Mismatch | The report bound by the ticket mismatches the actual report. |
| 400 | AE0130010024 | Authorize3rdTicket.Expired | Ticket [%s] has expired. |
| 400 | AE0130010027 | Authorize3rdTicket.HasNo.Logi nToken | The request [%s] has no token. |
| 400 | AE0130010023 | Authorize3rdTicket.NotExist | Ticket %s does not exist. |
| 400 | AE0130010025 | Authorize3rdTicket.Num.Excee d | The number of tickets %s is invalid. |
| 400 | AE0130010026 | Authorize3rdTicket.Num.HasN oLeft | There is no ticket number left, please generate new ticket. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |

Quick BI

## 查询授权给用户的作品列表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 46e53****5ba4b679ee2 2e2a2927**** | 用户ID。此处的用户ID为 Quick BI的UserID，而非阿里云的UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 返回授权给用户的作品列表。 |
| -Status | Integer | 1 | 报表的发布状态。取值范围： 0：未发布 1：已发布 2：已修改未发布 3：已下线 |
| - ThirdPartAuthF lag | Integer | 0 | 第三方嵌入状态。取值范围： 0：未开通嵌入 1：已开通嵌入 |
| -WorksId | String | 97f7f4c1-543a- 4069-8e8d- a56cfcd6**** | 报表ID。 |
| -CreateTime | String | 1530078690000 | 创建时间的毫秒级时间戳。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -WorkType | String | DATAFORM | 作品类型。取值范围： DATAPRODUCT：数据门户 PAGE：仪表板 FULLPAGE：全屏仪表板 REPORT：电子表格 dashboardOfflineQuery：自助取数 |
| -OwnerName | String | w****@aliyun.com | 作品所有者的阿里云账户名。 |
| - WorkspaceNa me | String | 专业版回归 | 报表所在工作空间的名称。 |
| -OwnerId | String | 74f5527216d14e9 892245320ebf2*** * | 作品所有者在Quickbi 的UserID。 |
| -ModifyName | String | 13855265****@16 3.com | 修改者的阿里云账户名。 |
| -WorkspaceId | String | c5f86ad2-ef53- 4c51-8720- 162ecfdb**** | 报表所在工作空间的ID。 |
| -SecurityLevel | String | 0 | 作品协同授权的安全策略。取值： 0：私密 12：授权指定成员 1或11：授权所有空间成员若您使用旧版权限，则返回值为1。 若您使用新版权限，则返回值为11。 |
| -Description | String | 测试报表的描述 | 作品备注。 |
| -WorkName | String | 测试报表 | 报表名称。 |
| -ModifyTime | String | 1530078690000 | 修改时间的毫秒级时间戳。 |
| -Directory | Struct |  | 作品所在的目录信息。 |
| --PathId | String |  |  |
| --PathName | String |  |  |
| --Name | String |  |  |
| --Id | String |  |  |

Quick BI

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QuerySharesToUserList &UserId=46e53****5ba4b679ee22e2a2927****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":{
  "Status":1,
  "ModifyTime":"1530078690000",
  "OwnerName":"w****@aliyun.com",
```

`"Description":"`测试报表的描述`",`

```json
  "WorkType":"DATAFORM",
  "ModifyName":"13855265****@163.com",
  "CreateTime":"1530078690000",
  "WorkspaceId":"c5f86ad2-ef53-4c51-8720-162ecfdb****",
  "ThirdPartAuthFlag":0,
  "OwnerId":"74f5527216d14e9892245320ebf2****",
  "SecurityLevel":"0",
```

`"WorkName":"`测试报表`",` `"WorkspaceName":"`专业版回归`",`

```json
  "-Directory":{
   "PathId":"",
   "PathName":"",
   "Id":"",
   "Name":""
  },
  "WorksId":"97f7f4c1-543a-4069-8e8d-a56cfcd6****"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| Quick BI |  |  | 开发指南·查询授权给用户的作品列表 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询作品的分享记录

查询作品被分享给哪些对象的列表，只返回仍然在有效期限内的分享配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ReportId | Strin g | Query | 是 | 6b407e50-e774-406b- 9956-da2425c2**** | 作品ID。这里的作品包括数据门户、仪表板、电子表格、自助取数、即席分析、 数据填报、数据大屏。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 返回作品被分享给的对象列表。 |
| -ShareId | String | 0ab9659e-29cf- 47d7-a364- 3a91553b**** | 分享配置ID。 |
| -ShareToId | String | 95296e95-ca89- 4c7d-8af9- dedf0ad0**** | 分享目标的ID，可能是在Quick BI的用户ID，可能是用户组ID。 当ShareToType=2（所有组织内的成员）的时候，ShareToId为组织ID。 |
| -AuthPoint | Integer | 3 | 分享权限。取值范围： 1：仅查看 3：查看和导出 |
| -ExpireDate | Long | 1640102400000 | 授权有效时间的毫秒级时间戳。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ShareToType | Integer | 0 | 分享类型。取值范围： 0：用户 1：用户组 2：组织 3：空间 |
| -ReportId | String | 6b407e50-e774- 406b-9956- da2425c2**** | 作品ID。 |
| -ShareToName | String | 小张 | 分享对象的名称。 |
| -ShareType | String | product | 被分享作品的类型。取值范围： product：数据门户 dashboard：仪表板 worksheet：电子表格 dashboardOfflineQuery：自助取数 ANALYSIS：即席分析 DATAFORM：数据填报 SCREEN：数据大屏 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryShareList &ReportId=6b407e50-e774-406b-9956-da2425c2****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":{
  "ShareId":"0ab9659e-29cf-47d7-a364-3a91553b****",
  "ShareToId":"95296e95-ca89-4c7d-8af9-dedf0ad0****",
  "ExpireDate":1640102400000,
  "ShareToType":0,
  "AuthPoint":3,
  "ShareToName":"小张",
  "ReportId":"6b407e50-e774-406b-9956-da2425c2****",
  "ShareType":"product"
 }
}
```

Quick BI

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 表

## 查询用户有权查看的作品列表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | Quick BI用户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 用户有权限查看的作品列表。 |
| -Status | Integer | 1 | 报表状态。取值范围： 0：未发布 1：已发布 2：已修改未发布 3：已下线 |
| - ThirdPartAuthF lag | Integer | 1 | 第三方嵌入状态。取值范围： 0：暂未开通嵌入 1：已开通嵌入 |
| -WorksId | String | 03366b16-69ce- 43c8-b782- 56c2f6ec**** | 作品ID。 |
| -CreateTime | String | 1611023338000 | 创建时间的毫秒级时间戳。 |

Quick BI 表

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -WorkType | String | PAGE | 作品类型。取值范围： DATAPRODUCT：数据门户 PAGE：仪表板 FULLPAGE：全屏仪表板 REPORT：电子表格 |
| -OwnerName | String | 张三 | 所有者的阿里云账户名。 |
| - WorkspaceNa me | String | 测试工作空间 | 作品所属工作空间名称。 |
| -OwnerId | String | 46e5374665ba4b6 79ee22e2a2927*** * | 作品所有者的Quick BI的UserID。 |
| -ModifyName | String | 李四 | 修改者的阿里云账户名。 |
| -WorkspaceId | String | 89713491-cb4f- 4579-b889- e82c35f1**** | 作品所属工作空间ID。 |
| -SecurityLevel | String | 0 | 作品协同授权的安全策略。取值： 0：私密 12：授权指定成员 1或11：授权所有空间成员若您使用旧版权限，则返回值为1。 若您使用新版权限，则返回值为11。 |
| -Description | String | 备注 | 作品备注。 |
| -WorkName | String | 公司地区表 | 作品名称。 |
| -ModifyTime | String | 1611023338000 | 修改时间的毫秒级时间戳。 |
| -Directory | Struct |  | 作品所处的目录结构。 |
| --PathId | String |  |  |
| --PathName | String |  |  |
| --Name | String |  |  |
| --Id | String |  |  |

Quick BI 表

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryReadableResourcesListByUserId &UserId=de4bc5f9429141cc8091cdd1c15b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "Status":1,
  "ModifyTime":"1611023338000",
  "OwnerName":"张三",
  "Description":"备注",
  "WorkType":"PAGE",
  "ModifyName":"李四",
  "CreateTime":"1611023338000",
  "WorkspaceId":"89713491-cb4f-4579-b889-e82c35f1****",
  "ThirdPartAuthFlag":1,
  "OwnerId":"46e5374665ba4b679ee22e2a2927****",
  "SecurityLevel":"0",
```

`"WorkName":"`公司地区表`",` `"WorkspaceName":"`测试工作空间`",`

```json
  "-Directory":{
   "PathId":"",
   "PathName":"",
   "Id":"",
   "Name":""
  },
  "WorksId":"03366b16-69ce-43c8-b782-56c2f6ec****"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| 开发指南·查询用表 | 户有权查看的作品列 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 获取组织下的工作空间列表

获取当前组织下的工作空间列表信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Keyword | Strin g | Query | 否 | 程序 | 空间名称的关键字。 |
| PageNum | Integ er | Query | 否 | 1 | 工作空间列表的当前页码： 起始值：1 默认值：1 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时的每页行数： 默认值：10 最大值：1000 |
| UserId | Strin g | Query | 否 | fe67f61a35a94b7da1a3 4ba174a7**** | 用户在Quick BI的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回工作空间列表的分页结果，工作空间的详细信息列表存放在返回参数Data中。 |
| -Data | Array |  |  |
| -- CreateUserAcc ountName | String |  |  |
| --Owner | String |  |  |
| --CreateTime | String |  |  |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- WorkspaceNa me | String |  |  |
| -- OrganizationId | String |  |  |
| --WorkspaceId | String |  |  |
| -- AllowShareOp eration | Boolean |  |  |
| --CreateUser | String |  |  |
| --ModifiedTime | String |  |  |
| -- WorkspaceDes cription | String |  |  |
| --ModifyUser | String |  |  |
| -- AllowPublishO peration | Boolean |  |  |
| -- OwnerAccount Name | String |  |  |
| -- ModifyUserAcc ountName | String |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryOrganizationWorkspaceList
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "WorkspaceDescription":"",
   "Owner":"",
   "ModifyUser":"",
   "CreateTime":"",
   "OwnerAccountName":"",
   "WorkspaceId":"",
   "CreateUser":"",
   "OrganizationId":"",
   "ModifyUserAccountName":"",
   "ModifiedTime":"",
   "AllowShareOperation":"",
   "WorkspaceName":"",
   "AllowPublishOperation":"",
   "CreateUserAccountName":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

| 开发指南·获取组 | 织下的工作空间列表 |  | Quick B |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

Quick BI

## 查询报表嵌入状态

查询某个报表是否已经开通嵌入。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 查询的作品ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 作品是否开通嵌入。取值范围： true：嵌入 false：未嵌入 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryEmbeddedStatus &WorksId=95296e95-ca89-4c7d-8af9-dedf0ad0****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0510130015 | Resource.NotBelongTo.Current Organization | The resource does not belong to the current organization. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 获取组织嵌入配置

获取组织下的嵌入配置，包括最大嵌入数和已经嵌入数等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 组织下报表的嵌入信息。 |
| - EmbeddedCou nt | Integer |  |  |
| -MaxCount | Integer |  |  |
| -Detail | Struct |  |  |
| -- DashboardOffli neQuery | Integer |  |  |
| --Report | Integer |  |  |
| --Page | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryEmbeddedInfo
```

正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "-Detail":{
   "Report":"",
   "DashboardOfflineQuery":"",
   "Page":""
  },
  "MaxCount":"",
  "EmbeddedCount":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 态

## 获取数据集行级权限开关状态

获取指定数据集的行级权限开关状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 7c7223ae-****- 3c744528014b | 数据集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | FAECEFA8-09BB- 58AB-BC58- C8ACEFE4D232 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 数据集行列权限开关详情。 |
| - IsOpenRowLev elPermission | Integer |  |  |
| -CubeId | String |  |  |
| - IsOpenColumn LevelPermissio n | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryDatasetSwitchInfo &CubeId=7c7223ae-****-3c744528014b
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI 态

```json
{
 "RequestId":"FAECEFA8-09BB-58AB-BC58-C8ACEFE4D232",
 "Success":true,
 "Result":{
  "CubeId":"",
  "IsOpenRowLevelPermission":"",
  "IsOpenColumnLevelPermission":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询工作空间数据集列表

查询指定工作空间的数据集列表，按照创建时间倒序排列。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| DirectoryI d | Strin g | Query | 否 | schemaad8aad00-9c55- 4984-a767- b4e0ec60**** | 指定目录ID。 若该字段不为空，则获取该目录下的所有数据集。 |
| WithChildr en | Boole an | Query | 否 | true | 是否递归包好子目录下的数据集。取值范围： true：返回directoryId 目录下所有递归子目录下的数据集。 false：仅返回 directoryId指定目录下的数据集，不包含子目录下的。 |
| Keyword | Strin g | Query | 否 | 测试数据集 | 数据集名称搜索关键字。 |
| PageNum | Integ er | Query | 否 | 1 | 数据集列表的当前页码： 起始值：1 默认值：1 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时的每页行数： 默认值：10 最大值：1000 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回数据集列表的分页结果，数据集列表的详细信息存放在返回参数Data中。 |
| -Data | Array |  |  |
| --RowLevel | Boolean |  |  |
| --WorkspaceId | String |  |  |
| --Description | String |  |  |
| --CreateTime | String |  |  |
| --OwnerName | String |  |  |
| -- WorkspaceNa me | String |  |  |
| --OwnerId | String |  |  |
| --ModifyTime | String |  |  |
| -- DatasetName | String |  |  |
| --DatasetId | String |  |  |
| --DataSource | Struct |  |  |
| ---DsType | String |  |  |
| ---DsName | String |  |  |
| ---DsId | String |  |  |
| --Directory | Struct |  |  |
| ---PathId | String |  |  |
| ---PathName | String |  |  |
| ---Name | String |  |  |
| ---Id | String |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |

| Quick BI |  |  | 开发指南·查询工作空间数据集列表 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -PageSize | Integer |  |  |
| -TotalNum | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryDatasetList &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "ModifyTime":"",
   "OwnerName":"",
   "--DataSource":{
    "DsName":"",
    "DsId":"",
    "DsType":""
   },
   "Description":"",
   "--Directory":{
    "PathId":"",
    "PathName":"",
    "Id":"",
    "Name":""
   },
   "OwnerId":"",
   "DatasetName":"",
   "CreateTime":"",
   "WorkspaceId":"",
   "RowLevel":"",
   "WorkspaceName":"",
   "DatasetId":""
  }
 }
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0510100038 | CubeSchema.Not.Exist | The cube schema does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询数据集简略信息

查询指定数据集的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DatasetId | Strin g | Query | 是 | a201c85c-****** | 数据集唯一ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | a4d1a221d-41za1- **** | 请求ID。 |
| Success | Boolean | true | 接口是否成功返回，取值范围： true：成功 false：失败 |
| Result | Struct |  | 数据集信息。 |
| -CubeTableList | Array |  |  |
| --TableName | String |  |  |
| --DatasourceId | String |  |  |
| --DsType | String |  |  |
| --UniqueId | String |  |  |
| --FactTable | Boolean |  |  |
| --Caption | String |  |  |
| --Customsql | Boolean |  |  |
| --Sql | String |  |  |
| -DimensionList | Array |  |  |
| --DataType | String |  |  |
| --Expression | String |  |  |
| --FactColumn | String |  |  |

| 开发指南·查询数据集 | 简略信息 |  | Quick B |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- DimensionTyp e | String |  |  |
| --Granularity | String |  |  |
| --RefUid | String |  |  |
| --Caption | String |  |  |
| --Uid | String |  |  |
| -- TableUniqueId | String |  |  |
| -MeasureList | Array |  |  |
| --DataType | String |  |  |
| --Expression | String |  |  |
| --MeasureType | String |  |  |
| --FactColumn | String |  |  |
| --Caption | String |  |  |
| -- TableUniqueId | String |  |  |
| --Uid | String |  |  |
| -GmtModify | String |  |  |
| -DsName | String |  |  |
| -DsId | String |  |  |
| -OwnerName | String |  |  |
| - WorkspaceNa me | String |  |  |
| -OwnerId | String |  |  |
| -DatasetName | String |  |  |
| -RowLevel | Boolean |  |  |
| -WorkspaceId | String |  |  |
| -CustimzeSql | Boolean |  |  |
| -GmtCreate | String |  |  |
| -DsType | String |  |  |

| Quick BI |  |  | 开发指南·查询数据集简略信息 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DatasetId | String |  |  |
| -Directory | Struct |  |  |
| --PathId | String |  |  |
| --PathName | String |  |  |
| --Name | String |  |  |
| --Id | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryDatasetInfo &DatasetId=a201c85c-******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"a4d1a221d-41za1-****",
 "Success":true,
 "Result":{
  "OwnerName":"",
  "-MeasureList":{
   "Uid":"",
   "Expression":"",
   "DataType":"",
   "MeasureType":"",
   "TableUniqueId":"",
   "Caption":"",
   "FactColumn":""
  },
  "WorkspaceId":"",
  "RowLevel":"",
  "DsId":"",
  "CustimzeSql":"",
  "-DimensionList":{
   "DimensionType":"",
   "RefUid":"",
   "Uid":"",
   "Expression":"",
   "DataType":"",
   "TableUniqueId":"",
   "Granularity":"",
   "Caption":"",
   "FactColumn":""
  },
"CbTblLit"{
```

Quick BI

```json
  "-CubeTableList":{
   "TableName":"",
   "UniqueId":"",
   "FactTable":"",
   "DatasourceId":"",
   "Customsql":"",
   "Caption":"",
   "DsType":"",
   "Sql":""
  },
  "DsType":"",
  "DatasetId":"",
  "GmtCreate":"",
  "OwnerId":"",
  "GmtModify":"",
  "DatasetName":"",
  "DsName":"",
  "WorkspaceName":"",
  "-Directory":{
   "PathId":"",
   "PathName":"",
   "Id":"",
   "Name":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510200002 | Not.WorkspaceCube.Error | You can only use the %s dataset of the current workspace. |
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |
| 400 | AE0110220001 | Decryption.Error | An error occurred while decoding. |
| 400 | AE0510260006 | Datasource.UserPermission.Err or | You do not have datasource authorization. |
| 400 | AE0510100002 | CubeMeta.ToXml.Error | An error occurred while converting the data object to the XML format. |
| 400 | AE0510260009 | Datasource.NotFound.Error | The specified data source does not exist: %s. |

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510110002 | Cube.ParseToXml.Error | An error occurred while parsing a dataset object to XML format. |
| 400 | AE0510260010 | DatasourceId.IsNull.Error | You must select a data source before selecting the table. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 查询数据集详情

查询指定数据集的详情，包括所属数据源、目录、以及数据集模型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DatasetId | Strin g | Query | 是 | 5820f58c-c734-4d8a- baf1-7979af4f**** | 数据集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

Quick BI

|  | 参数名称 | 类型 |  | 示例 | 返回JSON格式的数据集数据： 说明 { "cube": { "dimensions": [ { |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | 说明 { "cube": { "dimensions": [ { |  |
|  |  |  |  |  | "caption": "客户名称", "dataType": |  |  |
|  |  |  |  |  | "string", "dimensionType": |  |  |
|  |  |  |  | 返回JSON格式的数据 | "standard dimension", "factColumn": _ |  |  |
|  | Result | String |  | 集数据，详见左侧说 | "customer name", "uid": _ |  |  |
|  |  |  |  | 明。 | "N5820f5 customer name" }, { _ _ |  |  |
|  |  |  |  |  | "caption": "订单编号", "dataType": |  |  |
|  |  |  |  |  | "string", "dimensionType": |  |  |
|  |  |  |  |  | "standard dimension", "factColumn": _ |  |  |
|  |  |  |  |  | "order id", "uid": _ |  |  |
|  |  |  |  |  | "N5820f5 order id" }, ], _ _ |  |  |
|  |  |  |  |  | "measures": [ { "caption": "订单金 |  |  |
|  |  |  |  |  | 额", "dataType": "number", |  |  |
|  |  |  |  |  | "factColumn": "order amt", _ |  |  |
|  |  |  |  |  | "measureType": "standard measure", _ |  |  |
|  |  |  |  |  | "uid": "N5820f5 order amt" } ], _ _ |  |  |
|  |  |  |  |  | "table": { "customsql": false, |  |  |
|  |  |  |  |  | "dsId": "261b252d-c3c3-498a-a0a7- |  |  |
|  |  |  |  |  | 5d1ec6cd****", "tableName": |  |  |
|  |  |  |  |  | "company sales record copy" } }, _ _ _ |  |  |
|  |  |  |  |  | "datasetId": "5820f58c-c734-4d8a- |  |  |
|  |  |  |  |  | baf1-7979af4f****", "datasetName": |  |  |
|  |  |  |  |  | "company sales record copy12", _ _ _ |  |  |
|  |  |  |  |  | "datasource": { "dsId": "261b252d- |  |  |
|  |  |  |  |  | c3c3-498a-a0a7-5d1ec6cd****", |  |  |
|  |  |  |  |  | "dsName": "立三自用", "dsType": |  |  |
|  |  |  |  |  | "mysql" }, "directory": { "id": |  |  |
|  |  |  |  |  | "schemaad8aad00-9c55-4984-a767- |  |  |
|  |  |  |  |  | b4e0ec60****", "name": "我的数据集", |  |  |
|  |  |  |  |  | "pathId": "schemaad8aad00-9c55- |  |  |
|  |  |  |  |  | 4984-a767-b4e0ec60****", |  |  |
|  |  |  |  |  | "pathName": "我的数据集" }, |  |  |
|  |  |  |  |  | "ownerId": "13651626232****", |  |  |
|  |  |  |  |  | "ownerName": "张三", "rowLevel": |  |  |
|  |  |  |  |  | false, "workspaceId": "95296e95- |  |  |
|  |  |  |  |  | ca89-4c7d-8af9-dedf0ad0****", |  |  |
|  |  |  |  |  | "workspaceName": "测试工作空间" } |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryDatasetDetailInfo &DatasetId=5820f58c-c734-4d8a-baf1-7979af4f****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
```

`"Result":"`返回`JSON`格式的数据集数据，详见左侧说明。"

```
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510200002 | Not.WorkspaceCube.Error | You can only use the %s dataset of the current workspace. |
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |
| 400 | AE0510260010 | DatasourceId.IsNull.Error | You must select a data source before selecting the table. |
| 400 | AE0510260006 | Datasource.UserPermission.Err or | You do not have datasource authorization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 调用数据服务API

对数据服务中已创建的API进行调用。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| ApiId | Strin g | Query | 是 | f4cc43bc3*** |  | 数据服务中的API ID，请参见：数据服务。 |  |  |
| Conditions | Strin g | Query | 否 | { "area": ["华东", "华北"], "shopping date": _ "2019Q1", } |  | 数据服务的查询条件，以 Key和Value的形式传入。 map类型的字符串。其中，Key为请求参数的参数名，Value为请求参数的参数值。Key和Value必须成对出现。 说明： 请求参数的操作符设置为枚举筛选时支持 value包含多个值，此时 value值的格式是JSON形式的List。例如： area=["华东","华北","华南"] 对于日期，根据类型不同，提供不同的入参格式： 年：2019 季：2019Q1 月：201901 （携带 0） 周：2019-52 日：20190101 时：14:00:00 （分、 秒为00） 分：14:12:00 （秒为 00） 秒：14:34:34 |  |  |
|  |  |  |  |  |  |  | area=["华东","华 |  |
|  |  |  |  |  |  | 北","华南"] |  |  |
| ReturnFiel ds | Strin g | Query | 否 | ["area", "city", "price", "date"] |  | 返回参数的参数名列表，List 类型字符串。 |  |  |

**返回数据**

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 78C1AA2D-9201- 599E-A0BA- 6FC462E57A95 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回接口查询结果。 |
| -Values | Map |  |  |
| -Headers | Array |  |  |
| --Type | String |  |  |
| --DataType | String |  |  |
| --Granularity | String |  |  |
| --Label | String |  |  |
| --Column | String |  |  |
| --Aggregator | String |  |  |
| -Sql | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryDataService &ApiId=f4cc43bc3***
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"78C1AA2D-9201-599E-A0BA-6FC462E57A95",
 "Success":true,
 "Result":{
  "Values":"",
  "-Headers":{
   "Type":"",
   "Column":"",
   "Label":"",
   "DataType":"",
   "Aggregator":"",
   "Granularity":""
  },
  "Sql":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0581040002 | API.No.Permission | You are not authorized to call the data service API operation. |
| 400 | AE0581040001 | API.Not.Exist | The data service API operation does not exist. |
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0581040005 | Invalid.Parameter.Conditions | The specified Conditions is invalid. %s is not defined. |
| 400 | AE0581040004 | Invalid.Parameter.ReturnFields | The specified returnFields is invalid. %s is not defined. |
| 400 | AE0581040006 | Missing.Conditions | The specified Conditions is invalid. You must specify %s. |
| 400 | AE0581040013 | Missing.Dimension.Measure | The dimension or measure %s does not exist in Cube. |
| 400 | AE0510030023 | Rowlevel.Permission.Forbbiden | The request is denied by row level permission. The dataset is %s, %s %s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |

Quick BI 列表

## 查询用户所属的用户组信息列表

根据用户的UserID，查询该用户所属的所有用户组信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 46e5374665ba4b679ee 22e2a2927**** | 用户ID。此处为Quick BI的 UserID，而非阿里云的 UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E2440604-3059- 561A-AD68- DEDBC870EB2B | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 用户组信息。 |
| -IdentifiedPath | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0****/3d2c 23d4-2b41-4af8- a1f5- f6390f32****/f5eeb 52e-d9c2-4a8b- 80e3- 47ab55c2**** | 用户组的目录层级。 |
| - ParentUsergro upId | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0**** | 用户组ID。 |
| -ModifiedTime | String | 2021-03-15 20:36:40 | 用户组最新修改时间。 |
| -CreateUser | String | 46e5374665ba4b6 79ee22e2a2927*** * | 用户组创建者。此处为Quick BI的UserID，而非阿里云的UID。 |
| - UsergroupNam e | String | 测试用户组 | 用户组名称。 |

|  | Quick BI |  |  | 开发指南·查询用户所属的用户组信息列表 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -CreateTime | String | 2021-03-15 17:13:55 | 用户组创建时间。 |
| - UsergroupDes c | String | 备注 | 用户组备注。 |
| -UsergroupId | String | 34fd141d-4598- 4093-8c33- 8e066dcb**** | 用户组ID。 |
| -ModifyUser | String | 46e5374665ba4b6 79ee22e2a2927*** * | 用户组修改者。此处为Quick BI的UserID，而非阿里云的UID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListUserGroupsByUserId &UserId=46e5374665ba4b679ee22e2a2927****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"E2440604-3059-561A-AD68-DEDBC870EB2B",
 "Success":true,
 "Result":{
  "ModifyUser":"46e5374665ba4b679ee22e2a2927****",
  "ModifiedTime":"2021-03-15 20:36:40",
  "UsergroupDesc":"备注",
  "IdentifiedPath":"2fe4fbd8-588f-489a-b3e1-e92c7af0****/3d2c23d4-2b41-4af8-a1f5-f6390f
32****/f5eeb52e-d9c2-4a8b-80e3-47ab55c2****",
  "CreateTime":"2021-03-15 17:13:55",
  "ParentUsergroupId":"2fe4fbd8-588f-489a-b3e1-e92c7af0****",
  "CreateUser":"46e5374665ba4b679ee22e2a2927****",
```

`"UsergroupName":"`测试用户组`",`

```json
  "UsergroupId":"34fd141d-4598-4093-8c33-8e066dcb****"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |

| 列表 |  |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 列表

## 获取首页看板被授权的作品列表

获取指定用户在首页看板中展示的被授权的作品列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | b5d8fd9348cc4327****a fb604 | 要查询用户在Quick BI中的 UserID。 |
| Keyword | Strin g | Query | 否 | 测试报表 | 作品名称的关键字。 |
| TreeType | Strin g | Query | 否 | PAGE | 查询作品的类型（填空查询所有类型）。取值范围 ： DATAPRODUCT：数据门户 PAGE：仪表板 REPORT：电子表格 |
| PageSize | Integ er | Query | 否 | 10 | 查询作品列表的行数： 默认值：10 最大值：9999 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回查询结果。 |
| -Data | Array |  |  |
| --TreeId | String |  |  |
| --Type | String |  |  |
| --Name | String |  |  |

|  | 开发指南·获取首页看列表 | 板被授权的作品 |  | Quick B | I |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --OwnerNum | String |  |  |
| --OwnerName | String |  |  |
| --GmtCreate | String |  |  |
| --GmtModified | String |  |  |
| --PublishStatus | Integer |  |  |
| --Favorite | Boolean |  |  |
| --HasViewAuth | Boolean |  |  |
| --HasEditAuth | Boolean |  |  |
| --WorkspaceId | String |  |  |
| -- WorkspaceNa me | String |  |  |
| -TotalNum | Integer |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListSharedReports &UserId=b5d8fd9348cc4327****afb604
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI 列表

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Favorite":"",
   "OwnerName":"",
   "OwnerNum":"",
   "GmtModified":"",
   "WorkspaceId":"",
   "Name":"",
   "Type":"",
   "GmtCreate":"",
   "TreeId":"",
   "WorkspaceName":"",
   "HasViewAuth":"",
   "PublishStatus":"",
   "HasEditAuth":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

Quick BI 表

## 获取首页看板常看和足迹列表

获取指定用户在首页看板中展示的常看和足迹列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | b5d8fd9348cc4327****a fb604 | 要查询的用户在Quick BI中的UserID。 |
| Keyword | Strin g | Query | 否 | 财务报表 | 作品名称的关键字。 |
| TreeType | Strin g | Query | 否 | PAGE | 查询作品的类型（填空查询所有类型）。取值范围 ： DATAPRODUCT：数据门户 PAGE：仪表板 REPORT：电子表格 |
| QueryMod e | Strin g | Query | 否 | 1 | 查询模式。取值范围： 1：按访问次数排序 2：按最近访问时间排序 |
| PageSize | Integ er | Query | 否 | 10 | 查询作品列表的行数： 默认值：10 最大值：9999 |
| OffsetDay | Integ er | Query | 否 | 10 | 查询最近多少天的数据（默认10天）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |

Quick BI 表

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Result | Struct |  | 返回查询结果。 |
| -Data | Array |  |  |
| --TreeId | String |  |  |
| --Type | String |  |  |
| --Name | String |  |  |
| --OwnerNum | String |  |  |
| --OwnerName | String |  |  |
| --GmtCreate | String |  |  |
| --GmtModified | String |  |  |
| --PublishStatus | Integer |  |  |
| --Favorite | Boolean |  |  |
| --HasViewAuth | Boolean |  |  |
| --HasEditAuth | Boolean |  |  |
| --WorkspaceId | String |  |  |
| -- WorkspaceNa me | String |  |  |
| --ViewCount | Long |  |  |
| -- LatestViewTim e | String |  |  |
| -TotalNum | Integer |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListRecentViewReports &UserId=b5d8fd9348cc4327****afb604
```

&公共请求参数正常返回示例 Quick BI 表 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Favorite":"",
   "LatestViewTime":"",
   "OwnerName":"",
   "OwnerNum":"",
   "GmtModified":"",
   "WorkspaceId":"",
   "ViewCount":"",
   "Name":"",
   "Type":"",
   "GmtCreate":"",
   "TreeId":"",
   "WorkspaceName":"",
   "HasViewAuth":"",
   "PublishStatus":"",
   "HasEditAuth":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

Quick BI

## 获取数据门户菜单列表

获取具体数据门户下的分层菜单列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataPortal Id | Strin g | Query | 是 | 0d173abb53e84c8ca749 5429163b**** | 数据门户的ID。 |
| UserId | Strin g | Query | 否 | 1234567*** | Quick BI中的用户ID。传入时列表仅展示用户有权限的菜单。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 75912036-5527- 4B7E-9265- B481D6651AC2 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Result | String | [{"children": [{"children": [{"children": [{"menuId":"54kqg oa****","menuNam e":"报表菜单","menuType":0," showOnlyWithAcce ss":true,"dependen tPermisson":false," uri":"e5da4a3f- d7f9-4262-a39e- a840043c****"}, {"menuId":"pg1n1 35****","menuNam e":"目录菜单","menuType":4," showOnlyWithAcce ss":false,"depende ntPermisson":true} ],"menuId":"23a7d 5d8-e55a-4737- b6a1- 3c585505****","m enuName":"pop三级菜单","menuType":4," showOnlyWithAcce ss":true,"dependen tPermisson":true}], "menuId":"80764f3 c-affd-45a1-aaa1- bb039d8a****","m enuName":"pop二级菜单","menuType":4," showOnlyWithAcce ss":false,"depende ntPermisson":true} ],"menuId":"277f96 8a-22ff-4ce6-83f0- a82950f4****","me nuName":"pop一级菜单","menuType":4," showOnlyWithAcce ss":false,"depende ntPermisson":true} ] | 分级门户菜单列表详情的JSON字符串。取值范围： menuType：菜单类型。 0：仪表板 1：外链 2：电子表格 4：目录文件夹 5：表单填报 6：自助取数 menuId：菜单ID uri： 菜单关联资源的ID或者URL showOnlyWithAccess：是否仅授权可见 menuName：菜单显示名称 dependentPermisson：菜单关联的报表资源是否有权限 children：子菜单 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListPortalMenus &DataPortalId=0d173abb53e84c8ca7495429163b****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"75912036-5527-4B7E-9265-B481D6651AC2",
 "Success":true,
 "Result":"[{\"children\":[{\"children\":[{\"children\":
[{\"menuId\":\"54kqgoa****\",\"menuName\":\"报表菜单 \",\"menuType\":0,\"showOnlyWithAccess\":true,\"dependentPermisson\":false,\"uri\":\"e5da 3f-d7f9-4262-a39e-a840043c****\"},{\"menuId\":\"pg1n135****\",\"menuName\":\"目录菜单\", \"menuType\":4,\"showOnlyWithAccess\":false,\"dependentPermisson\":true}],\"menuId\":\"23 d5d8-e55a-4737-b6a1-3c585505****\",\"menuName\":\"pop三级菜单 \",\"menuType\":4,\"showOnlyWithAccess\":true,\"dependentPermisson\":true}],\"menuId\":\" 764f3c-affd-45a1-aaa1-bb039d8a****\",\"menuName\":\"pop二级菜单 \",\"menuType\":4,\"showOnlyWithAccess\":false,\"dependentPermisson\":true}],\"menuId\":\ 77f968a-22ff-4ce6-83f0-a82950f4****\",\"menuName\":\"pop一级菜单 \",\"menuType\":4,\"showOnlyWithAccess\":false,\"dependentPermisson\":true}]" }
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 情

## 获取数据门户菜单的授权详情

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataPortal Id | Strin g | Query | 是 | 0d173abb53e84c8ca749 5429163b**** | 数据门户的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 门户菜单的授权详情列表。 |
| -Receivers | Array |  | 菜单所授权的对象详情。 |
| --ReceiverId | String |  |  |
| --ReceiverType | Integer |  |  |
| - ShowOnlyWith Access | Boolean | true | 是否仅授权可见。取值范围： true：仅授权可见 false：都可见 |
| -MenuId | String | 54kqgoa**** | 数据门户的叶子节点菜单ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListPortalMenuAuthorization &DataPortalId=0d173abb53e84c8ca7495429163b****
```

&公共请求参数正常返回示例 Quick BI 情 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":{
  "MenuId":"54kqgoa****",
  "-Receivers":{
   "ReceiverId":"",
   "ReceiverType":""
  },
  "ShowOnlyWithAccess":true
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 首页看板收藏列表

获取指定用户在首页看板中展示的收藏作品列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | b5d8fd9348cc4327****a fb604 | 要查询用户在Quick BI中的 UserID。 |
| Keyword | Strin g | Query | 否 | 财务报表 | 作品名称的关键字。 |
| TreeType | Strin g | Query | 否 | PAGE | 查询作品的类型（填空查询所有类型）。取值范围 ： DATAPRODUCT：数据门户 PAGE：仪表板 REPORT：电子表格 |
| PageSize | Integ er | Query | 否 | 10 | 查询作品列表的行数： 默认值：10 最大值：9999 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回查询结果。 |
| -Data | Array |  |  |
| --TreeId | String |  |  |
| --Type | String |  |  |
| --Name | String |  |  |

| Quick BI |  |  | 开发指南·首页看板收藏列表 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --OwnerNum | String |  |  |
| --OwnerName | String |  |  |
| --GmtCreate | String |  |  |
| --GmtModified | String |  |  |
| --PublishStatus | Integer |  |  |
| --Favorite | Boolean |  |  |
| --HasViewAuth | Boolean |  |  |
| --HasEditAuth | Boolean |  |  |
| --WorkspaceId | String |  |  |
| -- WorkspaceNa me | String |  |  |
| -TotalNum | Integer |  |  |
| -TotalPages | Integer |  |  |
| -PageNum | Integer |  |  |
| -PageSize | Integer |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListFavoriteReports &UserId=b5d8fd9348cc4327****afb604
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "TotalNum":"",
  "PageNum":"",
  "PageSize":"",
  "TotalPages":"",
  "-Data":{
   "Favorite":"",
   "OwnerName":"",
   "OwnerNum":"",
   "GmtModified":"",
   "WorkspaceId":"",
   "Name":"",
   "Type":"",
   "GmtCreate":"",
   "TreeId":"",
   "WorkspaceName":"",
   "HasViewAuth":"",
   "PublishStatus":"",
   "HasEditAuth":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

Quick BI 列表

## 获取数据集行列权限白名单列表

根据行列权限种类，获取数据集行列权限的白名单列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 3d5db23c-e4f2-49dd- a883-92285b48e14a | 数据集ID。 |
| RuleType | Strin g | Query | 是 | ROW LEVEL _ | 白名单所属的行列权限类型： ROW LEVEL：行级权限 _ COLUMN LEVEL：列级 _ 权限 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 指定行级权限类型的白名单列表。 |
| -CubeId | String |  |  |
| -RuleType | String |  |  |
| -UsersModel | Struct |  |  |
| --UserGroups | String |  |  |
| --Users | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataLevelPermissionWhiteList &CubeId=3d5db23c-e4f2-49dd-a883-92285b48e14a &RuleType=ROW_LEVEL
```

&公共请求参数 Quick BI 列表正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":{
  "-UsersModel":{
   "Users":"",
   "UserGroups":""
  },
  "CubeId":"",
  "RuleType":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 表

## 获取数据集行列权限配置列表

获取指定数据集的行列权限配置列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 7c7223ae-****- 3c744528014b | 数据集ID。 |
| RuleType | Strin g | Query | 是 | ROW LEVEL _ | 数据集行列权限类型。取值范围： ROW LEVEL：行级权限 _ COLUMN LEVEL：列级 _ 权限 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |

Quick BI 表

| 参数名称 | 类型 | 示例 | { 说明 "isOpen": 1, |
|---|---|---|---|
|  |  |  | "extraConfigModel": { // 额外配置信息 "ruleType": "ROW LEVEL", //行级权限类型 _ "missHitPolicy": "NONE", //命中规则策略： NONE无权限，ALL有权限 "cubeId": "7c7223ae-31d1-4d2f-b11f- 3c744528014b" //数据集ID }, "ruleType": "ROW LEVEL", //行列权限类型 _ |
| Result | String | 行列权限列表的JSON 串，详情见描述。 | "ruleModels": [ { "ruleUsersModel": { // 针对的人群 "userGroups": [ "0d5fb19b--1248fc27ca51", // 用户组 ID "4aa3f089- -85f0-0e8ac7c2dee9" ], "users": [ "HuangJia***2e3fa822", // 用户的UserID "4334***84358" ] }, "ruleContentModel": { "ruleContentType": "ROW FIELD", //行列权 _ 限类型 "ruleContentJson": "{"conditionNode": {"caption":"周期","isMeasure":false,"pathId":"7d3b073bc 6","relationOperator":"not- null","name":"7d3b073bc6","value": {"value":[""],"valueType":"ENUM"}}}", // 行列权限规则的JSON串 "ruleOriginConfigJson": " {"operator":"and","operands": [{"labelName":"周期","isValid":true,"uniqueId":"5","fieldId":"7 d3b073bc6","error":false,"fieldType":"strin g","defaultValue": {"selectType":"condition","value": {"conditionOp":"not- null","conditionValue":""},"valueType":"EN UM"}}],"isRelation":true}" }, //前端需求的固定格式JSON串 "isOpen": 1, // 行列权限配置的开关状态 1.开启 0.关闭 "hitTakeEffect": 1, // 针对列级权限，命中后规则是否生效 1生效、0不生效。 "ruleName": "测试行级权限勿删", // 行列权限 _ 规则的名称 "ruleLevelType": "ROW LEVEL", //行列权限 _ 类型 "ruleId": "a5bb24da-772f-45e8-a43c- a891683e14da", // 行列权限规则的ID "cubeId": "7c7223ae-31d1-4d2f-b11f- 3c744528014b", // 数据集ID "ruleTargetScope": "OTHERS" 规则生效范围：ALL所有人、OTHERS指定人 } ], "cubeId": "7c7223ae-31d1-4d2f-b11f- 3c744528014b" // 数据集ID } |

Quick BI 表

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListCubeDataLevelPermissionConfig &CubeId=7c7223ae-****-3c744528014b &RuleType=ROW_LEVEL
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
```

`"Result":"`行列权限列表的`JSON`串，详情见描述。"

```
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |

Quick BI 表

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 获取用户收藏作品列表

获取用户收藏的作品列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 用户ID。此处的用户ID为 Quick BI的UserID，而非阿里云的UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 162A632E-0A88- 51CF-98F8- 94FDEE82DB7D | 请求ID。 |
| Success | Boolean | true | 收藏记录的主键 ID。 |
| Result | Array |  | 用户收藏的报表列表详情。 |
| -WorkspaceId | String | 9337d121-a78f- 4c1b-a8bc- f81de117**** | 工作空间ID。 |
| -WorksType | String | dashboardOfflineQ uery | 作品类型。取值范围： DATAPRODUCT：数据门户 PAGE：仪表板 REPORT：电子表格 dataForm：数据填报 dashboardOfflineQuery：自助取数 |
| -FavoriteId | Integer | 12373 | 收藏记录的主键 ID。 |
| -WorksId | String | 95296e95-ca89- 4c7d-8af9- dedf0ad0**** | 作品的ID。 |
| -WorksName | String | 奇异博士 | 作品的名称。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - WorkspaceNa me | String | 测试工作空间 | 工作空间名称。 |
| -OwnerId | String | fe67f61a35a94b7d a1a34ba174a7**** | 作品所有者的用户ID。此处的用户ID为Quick BI 的UserID，而非阿里云的UID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListCollections &UserId=fe67f61a35a94b7da1a34ba174a7****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"162A632E-0A88-51CF-98F8-94FDEE82DB7D",
 "Success":true,
 "Result":{
  "FavoriteId":12373,
  "WorksType":"dashboardOfflineQuery",
  "OwnerId":"fe67f61a35a94b7da1a34ba174a7****",
```

`"WorksName":"`奇异博士`",`

```json
  "WorkspaceId":"9337d121-a78f-4c1b-a8bc-f81de117****",
```

`"WorkspaceName":"`测试工作空间`",`

```json
  "WorksId":"95296e95-ca89-4c7d-8af9-dedf0ad0****"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| Quick BI |  |  | 开发指南·获取用户收藏作品列表 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 批量查询用户组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pIds | Strin g | Query | 是 | 34fe-***-6dcb,84q9-****- 4a274 | 要查询的用户组ID，批量查询时用半角逗号（,）隔开。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回用户组查询结果。 |
| - FailedUserGro upIds | String |  |  |
| - UserGroupMod els | Array |  |  |
| -- IdentifiedPath | String |  |  |
| -- ParentUsergro upId | String |  |  |
| --ModifiedTime | String |  |  |
| --CreateUser | String |  |  |
| -- UsergroupNam e | String |  |  |
| --CreateTime | String |  |  |

| Quick BI |  |  | 开发指南·批量查询用户组 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- UsergroupDes c | String |  |  |
| --UsergroupId | String |  |  |
| --ModifyUser | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListByUserGroupId &UserGroupIds=34fe-***-6dcb,84q9-****-4a274
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":{
  "FailedUserGroupIds":"",
  "-UserGroupModels":{
   "ModifyUser":"",
   "ModifiedTime":"",
   "UsergroupDesc":"",
   "IdentifiedPath":"",
   "CreateTime":"",
   "ParentUsergroupId":"",
   "CreateUser":"",
   "UsergroupName":"",
   "UsergroupId":""
  }
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |

| 开发指南·批量查 | 询用户组 |  | Quick B |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 根据关键字获取用户组信息

根据用户组名称关键字搜索用户组信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Keyword | Strin g | Query | 是 | 测试用户组 | 用户组名称关键字。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D7980306-1F08- 5A88-9FE7- ECB8B9C4C0F5 | 请求 ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Array |  | 用户组信息。 |
| -IdentifiedPath | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0****/34fd 141d-4598-4093- 8c33-8e066dcb**** | 用户组的目录层级。 |
| - ParentUsergro upId | String | 2fe4fbd8-588f- 489a-b3e1- e92c7af0**** | 父用户组ID。 |
| -ModifiedTime | String | 2021-03-15 20:36:40 | 用户组最新修改时间。 |
| -CreateUser | String | 46e5374665ba4b6 79ee22e2a2927*** * | 子用户组创建者。此处为Quick BI的UserID，而非阿里云的UID。 |
| - UsergroupNam e | String | 测试用户组01 | 用户组名称。 |
| -CreateTime | String | 2021-03-15 17:13:55 | 用户组创建时间。 |
| - UsergroupDes c | String | 测试描述 | 用户组备注。 |

| 开发指南·根据关键字 | 获取用户组信息 |  | Quick B |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -UsergroupId | String | 34fd141d-4598- 4093-8c33- 8e066dcb**** | 用户组ID。 |
| -ModifyUser | String | 46e5374665ba4b6 79ee22e2a2927*** * | 用户组修改者。此处为Quick BI的UserID，而非阿里云的UID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetUserGroupInfo
```

`&Keyword=`测试用户组 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D7980306-1F08-5A88-9FE7-ECB8B9C4C0F5",
 "Success":true,
 "Result":{
  "ModifyUser":"46e5374665ba4b679ee22e2a2927****",
  "ModifiedTime":"2021-03-15 20:36:40",
```

`"UsergroupDesc":"`测试描述`",`

```json
  "IdentifiedPath":"2fe4fbd8-588f-489a-b3e1-e92c7af0****/34fd141d-4598-4093-8c33-8e066d
cb****",
  "CreateTime":"2021-03-15 17:13:55",
  "ParentUsergroupId":"2fe4fbd8-588f-489a-b3e1-e92c7af0****",
  "CreateUser":"46e5374665ba4b679ee22e2a2927****",
```

`"UsergroupName":"`测试用户组`01",`

```json
  "UsergroupId":"34fd141d-4598-4093-8c33-8e066dcb****"
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| Quick BI |  |  | 开发指南·根据关键字获取用户组信息 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除工作空间

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 391d5920-****-****- a6a4-c8177cafcfc4 | 工作空间ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Result | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Success | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteWorkspace &WorkspaceId=391d5920-****-****-a6a4-c8177cafcfc4
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

`XML` 格式 Quick BI

```xml
<RequestId>D8749D65-E80A-433C-AF1B-CE9C180FF3B4</RequestId> <Success>true</Success> <Result>true</Result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0150100005 | Not.Organization.Admin | No permission,you are not organization admin. |
| 400 | AE0150010020 | Workspace.Num.Exceed | The number of create workspace exceeds the maximum number limit %s. |
| 400 | AE0510000018 | Name.Repetition | The workspace name already exists. |
| 400 |  | Internal.System.Error | An internal system error occurred. |

Quick BI

## 删除组织成员标签元信息

删除组织成员的标签元信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TagId | Strin g | Query | 是 | pop 001 _ | 待删除的标签ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回删除标签的执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUserTagMeta &TagId=pop_001
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100023 | UserTag.NotIn.CurrentOrganiz ation | The user tag is not in the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

Quick BI

## 用户批量退出用户组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 204627493484**** | 要退出用户组的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |
| UserGrou pIds | Strin g | Query | 是 | 34fd141d-4598-4093- 8c33- 8e066dcb****,3d2c23d4 -2b41-4af8-a1f5- f6390f32**** | 要退出的用户组ID。 支持批量传参，ID之间用半角逗号（,）隔开。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | ABBAD906-3925- 5D18-B23D- 714053AB0AA2 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUserGroupMembers &UserId=204627493484**** &UserGroupIds=34fd141d-4598-4093-8c33-8e066dcb****,3d2c23d4-2b41-4af8-a1f5-f6390f32****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"ABBAD906-3925-5D18-B23D-714053AB0AA2",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020307 | Usergroup.NotBelongTo.Curren tOrganization | The usergroup %s does not belong to the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除用户组成员

删除指定用户组下的指定成员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 是 | 46e537**** | 用户组ID。 |
| UserId | Strin g | Query | 是 | 2fe4fbd8**** | Quick BI的用户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回删除用户组成员的结果。取值范围： true：删除成功 false：删除失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUserGroupMember &UserGroupId=46e537**** &UserId=2fe4fbd8****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":true
}
```

Quick BI

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除用户组

删除组织内的用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 是 | f5eeb52e-d9c2-4a8b- 80e3-47ab55c2**** | 用户组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F2775AB6-DE99- 5FA6-86A4- 72EA0A8AFEE3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUserGroup &UserGroupId=f5eeb52e-d9c2-4a8b-80e3-47ab55c2****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F2775AB6-DE99-5FA6-86A4-72EA0A8AFEE3",
 "Success":true,
 "Result":true
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 | AE0150020301 | UserGroup.Remove.RootNode | The root user group cannot be deleted. |
| 400 | AE0150020302 | UserGroup.Remove.WithChildr en | This user group contains a child user group and cannot be deleted. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除工作空间成员

删除指定工作空间的成员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| UserId | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 待删除的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUserFromWorkspace &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserId=de4bc5f9429141cc8091cdd1c15b****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010013 | User.Not.WorkspaceAdmin | Only administrators of the group workspace can perform this operation. |
| 400 | AE0150010008 | Workspace.Type.Error | The type of group workspace is invalid. |
| 400 | AE0150010009 | CanNot.Remove.WorkspaceOw ner | You cannot remove the group workspace owner from the group. |
| 400 | AE0150010004 | User.NotIn.Workspace | The user is not a member of the group workspace. |
| 400 | AE0510280006 | Cannot.TransferTo.Owner | You cannot transfer an item to its current owner. |
| 400 | AE0510200010 | Works.Transfer.Error | You are not authorized to transfer this item. |
| 400 | AE0510280001 | Transfer.TargetUser.NotExist | The new owner does not exist. Please ensure that the target user has logged on to the system. |
| 400 | AE0510280003 | PersonalWorkspace.NotSuppor t.AllTransfer | Personal workspaces cannot be transferred. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

|  | 开发指南·删除工 | 作空间成员 |  | Quick B | I |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除组织用户

删除指定组织用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | fe67f61a35a94b7da1a3 4ba174a7**** | 待删除的用户ID。此处的用户ID为Quick BI的 UserID，而非阿里云的 UID。 |
| TransferU serId | Strin g | Query | 否 | f5****afccd9e434a274 | 继承者的用户ID。如果不为空，则将删除用户在工作空间内的报表资源转移给继承者，否则转移给空间 owner。 继承者不能是组织访问者继承者在工作空间的权限不能小于删除掉的用户， 管理权限>开发权限>分享权限>查看权限继承者不在工作空间内， 会自动加入工作空间 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例 Quick BI

```
http(s)://[Endpoint]/?Action=DeleteUser &UserId=fe67f61a35a94b7da1a34ba174a7****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100007 | CannotRemove.OrganizationO wner | You cannot remove the organization owner from the organization. |
| 400 | AE0150100008 | Member.ExistInWorkspace.Erro r | You cannot remove a user who is a member of a group workspace. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010008 | Workspace.Type.Error | The type of group workspace is invalid. |
| 400 | AE0150100026 | Not.Organization.AuthAdmin | You are not a role administrator of the organization and do not have the permission to perform the operation. |
| 400 | AE0510200010 | Works.Transfer.Error | You are not authorized to transfer this item. |
| 400 | AE0150010009 | CanNot.Remove.WorkspaceOw ner | You cannot remove the group workspace owner from the group. |
| 400 | AE0150010004 | User.NotIn.Workspace | The user is not a member of the group workspace. |
| 400 | AE0510280001 | Transfer.TargetUser.NotExist | The new owner does not exist. Please ensure that the target user has logged on to the system. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 |  | Internal.System.Error | An internal system error occurred. |

| Quick BI |  |  | 开发指南·删除组织用户 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |

Quick BI

## 删除嵌入ticket

删除免登嵌入报表的指定ticket。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ticket | Strin g | Query | 是 | 040e6f79d****7d283c72 06c070 | 三方嵌入的票据值，即URL 中的accessTicket值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 是否删除成功。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTicket &Ticket=040e6f79d****7d283c7206c070
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0130010022 | Authorize3rdTicket.BindedWor ks.Mismatch | The report bound by the ticket mismatches the actual report. |
| 400 | AE0130010024 | Authorize3rdTicket.Expired | Ticket [%s] has expired. |
| 400 | AE0130010027 | Authorize3rdTicket.HasNo.Logi nToken | The request [%s] has no token. |
| 400 | AE0130010023 | Authorize3rdTicket.NotExist | Ticket %s does not exist. |
| 400 | AE0130010025 | Authorize3rdTicket.Num.Excee d | The number of tickets %s is invalid. |
| 400 | AE0130010026 | Authorize3rdTicket.Num.HasN oLeft | There is no ticket number left, please generate new ticket. |
| 400 | AE0510200000 | NoPermissionTo.Operate.Objec t | You are not authorized to operate the objects. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |

Quick BI

## 删除行列权限规则

删除单条行列权限规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 | 7c7223ae-****- 3c744528014b | 数据集ID。 |
| RuleId | Strin g | Query | 是 | a5bb24da-****- a891683e14da | 行列权限的规则ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDataLevelRuleConfig &CubeId=7c7223ae-****-3c744528014b &RuleId=a5bb24da-****-a891683e14da
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

Quick BI

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除行列规则的人群

针对单条行列权限规则删除选定的人群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DeleteUse rModel | Strin g | Query | 是 | {"ruleId":"a5bb24da-***- a891683e14da","cubeId ":"7c7223ae-***- 3c744528014b","delMod el":{"userGroups": ["0d5fb19b-***- 1248fc27ca51","3d2c23 d4-***- f6390f325c2d"],"users": ["4334***358","Huang** *3fa822"]}} | { "ruleId": "a5bb24da-***- a891683e14da", // 行列权限规则ID "cubeId": "7c7223ae- ***-3c744528014b", // 数据集ID "delModel": { "userGroups": [ "0d5fb19b-***- 1248fc27ca51", // 删除用户组人群的用户组ID "3d2c23d4-***- f6390f325c2d" ], "users": [ "4334***358", // 删除用户人群的UserID "Huang***3fa822" ] } } |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例 Quick BI

```
http(s)://[Endpoint]/?Action=DeleteDataLevelPermissionRuleUsers &DeleteUserModel= {"ruleId":"a5bb24da-***-a891683e14da","cubeId":"7c7223ae-***-3c744528 014b","delModel":{"userGroups":["0d5fb19b-***-1248fc27ca51","3d2c23d4-***f6390f325c2d"],"users":["4334***358","Huang***3fa822"]}}
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 更新嵌入ticket的失效时间

更新嵌入报表的ticket的失效时间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ticket | Strin g | Query | 是 | 040e6f79d33444838e** ***c7206c070 | 三方嵌入的票据值，即URL 中的accessTicket值。 |
| ExpireTim e | Integ er | Query | 是 | 200 | 要延期的时间。 单位分钟，取值范围 0~240（4小时）。 已过期的票据无法延期。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 是否延期成功。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DelayTicketExpireTime &Ticket=040e6f79d33444838e*****c7206c070 &ExpireTime=200
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0130010022 | Authorize3rdTicket.BindedWor ks.Mismatch | The report bound by the ticket mismatches the actual report. |
| 400 | AE0130010024 | Authorize3rdTicket.Expired | Ticket [%s] has expired. |
| 400 | AE0130010027 | Authorize3rdTicket.HasNo.Logi nToken | The request [%s] has no token. |
| 400 | AE0130010023 | Authorize3rdTicket.NotExist | Ticket %s does not exist. |
| 400 | AE0130010025 | Authorize3rdTicket.Num.Excee d | The number of tickets %s is invalid. |
| 400 | AE0130010026 | Authorize3rdTicket.Num.HasN oLeft | There is no ticket number left, please generate new ticket. |
| 400 | AE0510200000 | NoPermissionTo.Operate.Objec t | You are not authorized to operate the objects. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |

Quick BI

## 增量修改行列权限白名单

修改指定数据集行列权限的白名单。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CubeId | Strin g | Query | 是 |  | 数据集ID。 |
| RuleType | Strin g | Query | 否 |  | 行级权限类型： ROW LEVEL：行级权 _ 限， COLUMN LEVEL：列级 _ 权限 |
| OperateTy pe | Strin g | Query | 否 |  | 操作类型： 1. ADD：增加白名单 2. DELETE：删除白名单 |
| TargetTyp e | Strin g | Query | 否 |  | 修改白名单对应的类型： 1：用户 2：用户组 |
| TargetIds | Strin g | Query | 否 |  | 授权对象，同时支持多个授权对象，多个对象以英文逗号分隔。取值范围： TargetType=1（用户） 时，为用户ID。 TargetType=2（用户组）时，为用户组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 |  |
| Result | Boolean | true |  |
| Success | Boolean | true |  |

**示例**

Quick BI 请求示例

```
http(s)://Endpoint/?Action=AddDataLevelPermissionWhiteList &CubeId=7c7223ae-***-3c74452
```

`8014b &`公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

`XML` 格式

```xml
<RequestId>D8749D65-E80A-433C-AF1B-CE9C180FF3B4</RequestId> <Success>true</Success> <Result>true</Result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |

Quick BI

## 添加行列权限规则人群

针对单条行列权限规则增量添加选定的人群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AddUserM odel | Strin g | Query | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Result | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Success | Boolean | true | 接口执行结果。取值范围： true：请求成功 false：请求失败 |

**示例**

请求示例

```json
http(s)://Endpoint/?Action=AddDataLevelPermissionRuleUsers &AddUserModel= {"ruleId":"a5bb24da--a891683e14da","cubeId":"7c7223ae--3c744528014b","addModel":{"userG roups":"0d5fb19b--1248fc27ca51","3d2c23d4-f6390f325c2d","users":"4334358","Huang3fa822"}} &公共请求参数
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

`XML` 格式 Quick BI

```xml
<RequestId>D8749D65-E80A-433C-AF1B-CE9C180FF3B4</RequestId> <Success>true</Success> <Result>true</Result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510030032 | CubePermission.Columnlevel.V ersionError | You are not allowed to use the new dataLevelPermission API. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510030033 | RowLevelPermission.SwitchClo se.Error | The row level permission switch must be on. |
| 400 | AE0510030034 | RowLevelPermission.Rule.NotE xsist | The row level permission rule does not exist: %s. |
| 400 | AE0510030035 | RowLevelPermission.Rule.NotB elongToCube | The row level permission rule does not belong to the current cube. |
| 400 | AE0510100043 | Cube.NotBelongTo.CurrentOrg anization | The cube does not belong to the current organization %s. |

Quick BI

## 批量添加成员到用户组

将用户批量添加到指定的用户组中。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 46e5****37a5 | Quick BI的用户ID。 |
| UserGrou pIds | Strin g | Query | 是 | 0d5fb19b-****-****- 99da-1248fc27ca51 | 用户组ID，以英文逗号分隔。示例： aGroupId,bGroupId,cGro upIds |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 |  |
| Result | Boolean | true |  |
| Success | Boolean | true |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUserGroupMembers &UserId=46e5****37a5 &UserGroupIds=0d5fb19b-****-****-99da-1248fc27ca51
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

`XML` 格式 Quick BI

```xml
<RequestId>D8749D65-E80A-433C-AF1B-CE9C180FF3B4</RequestId> <Success>true</Success> <Result>true</Result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020003 | Invalid.User | The user does not exist and cannot be added to a user group. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000035 | Invalid.Parameter | The length of the parameter must not exceed 1000. |
| 400 | AE0110000001 | Internal.System.Error | An internal system error occurred. |
| 400 |  | Internal.System.Error | An internal system error occurred. |

Quick BI

## 新建工作空间

在当前组织下新建一个工作空间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eName | Strin g | Query | 是 | 示例工作空间 | 工作空间名称。 |
| Workspac eDesc | Strin g | Query | 否 | 存放示例的报表资源，用于演示 | 工作空间描述。 |
| UseComm ent | Boole an | Query | 否 | true | 工作空间创建数据集是否使用表备注，默认：true |
| AllowExpo rt | Boole an | Query | 否 | true | 工作空间报表是否允许导出，默认：true |
| AllowShar e | Boole an | Query | 否 | true | 工作空间报表是否允许分享，默认：true |
| AllowPubli sh | Boole an | Query | 否 | true | 工作空间报表是否允许公开，默认：true |
| AllowAuth orize3rd | Boole an | Query | 否 | true | 工作空间报表是否允许第三方嵌入，默认：true |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 |  |
| Result | String | true |  |
| Success | Boolean | true |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateWorkspace
```

`&WorkspaceName=`示例工作空间 &公共请求参数 Quick BI 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":"true"
}
```

`XML` 格式

```xml
<RequestId>D8749D65-E80A-433C-AF1B-CE9C180FF3B4</RequestId> <Success>true</Success> <Result>true</Result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0150100005 | Not.Organization.Admin | No permission,you are not organization admin. |
| 400 | AE0150010020 | Workspace.Num.Exceed | The number of create workspace exceeds the maximum number limit %s. |
| 400 | AE0510000018 | Name.Repetition | The workspace name already exists. |

| Quick BI |  |  | 开发指南·新建工作空间 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |

Quick BI

## 新建用户组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 否 | pop0001 | 用户组唯一ID。 无需传入，系统会自动生成；当用户主动传入 UserGroupId时，以用户传入的ID作为用户组 ID，用户需要自行保证该 ID在组织内唯一。 格式校验：最大长度 64，不能为-1， |
| UserGrou pName | Strin g | Query | 是 | 杭州财报 | 用户组名称。 格式校验：最大长度255 特殊格式校验：中英文数字 \ / \| () ] [ _ |
| UserGrou pDescripti on | Strin g | Query | 否 | 用户分组描述 | 用户组描述。 格式校验：最大长度255 特殊格式校验：中英文数字 \ / \| () ] [ _ |
| ParentUse rGroupId | Strin g | Query | 是 | 3d2c23d4-2b41-4af8- a1f5-f6390f32**** | 父用户组ID。可以将新建的用户组添加到该分组下： 当输入父用户组ID时，新建的用户组会添加到该ID 的用户组下。 当输入-1时，新建的用户组会添加到根目录下。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 36829379-0C38- 5BC0-830A- 92665BF77D4F | 请求 ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |

| Quick BI |  |  | 开发指南·新建用户组 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| Result | String | f5eeb52e-d9c2- 4a8b-80e3- 47ab55c2**** | 返回用户组添加成功后的ID。如果添加失败，返回空字符串“”。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateUserGroup
```

`&UserGroupName=`杭州财报

```
&ParentUserGroupId=3d2c23d4-2b41-4af8-a1f5-f6390f32****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"36829379-0C38-5BC0-830A-92665BF77D4F",
 "Success":true,
 "Result":"f5eeb52e-d9c2-4a8b-80e3-47ab55c2****"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 | AE0510000018 | Duplicate.Name.Error | The name already exists. |
| 400 | AE0150020001 | UserGroup.Parent.NotFound | The parent user group does not exist. |
| 400 | AE0150020306 | Duplicate.UserGroup.Id | Duplicated usergroupId %s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| 开发指南·新建用 | 户组 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 生成报表嵌入ticket

生成报表嵌入需要使用的ticket。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | a206f5f3-****- e9b17c835b03 | 开通嵌入的报表ID。 目前仅支持仪表板和电子表格。 |
| CmptId | Strin g | Query | 否 | 0fc6a275c7f64f17b1**** a306ce0f31 | 组件ID。为以上报表中某个组件的ID。 获取组件ID调用的接口请参见QueryWorksBloodRela tionship。 |
| TicketNu m | Integ er | Query | 否 | 1 | Ticket的票据数量，每次使用票据访问后，Ticket的票据数量减1。 默认值为1。 建议值为1。 最大值为99999。 |
| UserId | Strin g | Query | 否 | 46e537466****92704c8 | Quick BI的UserId，非您的阿里云账号ID。 您可以调用QueryUserInfoByAcco unt接口，获取UserId。 UserId样例为 fe67f61a35a94b7da1a3 4ba174a7****。 UserId和 AccountName只填一个即可，不填时默认绑定报表的Owner，访问报表时将以该用户身份访问。若您需要配置数据行级权限，请参见行级权限。 |

Quick BI

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccountN ame | Strin g | Query | 否 | 测试用户 | 用户的账号名称。 如果用户是阿里云主账号wangwu ，格式为 **[主账号]，例如 wangwu**。 如果用户是RAM账号zhangsan @aliyu n.cn**，格式为**[主账号：子账号]，例如 wangwu:zhangsa n****。 UserId和 AccountName只填一个即可，不填时默认绑定报表的Owner，访问报表时将以该用户身份访问。若您需要配置数据行级权限，请参见行级权限。 |
| AccountTy pe | Integ er | Query | 否 | 1 | 用户的账号类型。 1：阿里云账号 3：Quick BI自建账号 4：钉钉 5：RAM子账号 9：企业微信 10：飞书若AccountName不为空时，则 AccountType也不能为空。 |
| ExpireTim e | Integ er | Query | 否 | 200 | 过期时间单位：分钟默认：240 |
| Watermar kParam | Strin g | Query | 否 | 三方嵌入 | 报表的水印参数。 不得超过50个字符。 |
| GlobalPar am | Strin g | Query | 否 | [{"paramKey":"price","jo inType":"and","condition List": [{"operate":">","value": "0"}]}] | 报表过滤条件的全局参数。 JsonArray格式的字符串。 若您需要使用全局参数能力，请联系Quick BI运营负责人。 |

Quick BI

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | String | ccd3428c-****- ****-a608- 26bae29dffee | 生成ticket的值。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTicket &WorksId=a206f5f3-****-e9b17c835b03
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":"ccd3428c-****-****-a608-26bae29dffee"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DEFAULT | Internal.System.Error | An internal system error occurred. |
| 400 | AE0130010022 | Authorize3rdTicket.BindedWor ks.Mismatch | The report bound by the ticket mismatches the actual report. |
| 400 | AE0130010024 | Authorize3rdTicket.Expired | Ticket [%s] has expired. |
| 400 | AE0130010027 | Authorize3rdTicket.HasNo.Logi nToken | The request [%s] has no token. |
| 400 | AE0130010023 | Authorize3rdTicket.NotExist | Ticket %s does not exist. |
| 400 | AE0130010025 | Authorize3rdTicket.Num.Excee d | The number of tickets %s is invalid. |

| 开发指南·生成报 | 表嵌入ticket |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0130010026 | Authorize3rdTicket.Num.HasN oLeft | There is no ticket number left, please generate new ticket. |
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0130010003 | Authorize3Rd.Report.Unauthori zed | The report is not enabled for third party embedding. |
| 400 | AE0510100020 | Cube.Not.Exist | The Cube does not exist. |
| 400 | AE0510260009 | Datasource.NotFound.Error | The specified data source does not exist: %s. |
| 400 | AE0110130007 | Report.NotExist | The dashboard does not exist. |
| 400 | AE0510200025 | Organization.Workspace.Inconf ormity | The workspace does not match the organization. |
| 400 | AE0591000014 | ApiUser.Not.Exists | The specified user does not exist. |
| 400 | AE0510000035 | Parameter.Length.Exceed | Parameter length exceeds maximum limit: [%s]. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |

Quick BI 权限

## 查询用户对数据作品的查看权限

查询用户对数据作品（仪表板、电子表格等）是否有权限查看。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 作品的ID。这里的资源包括数据门户，仪表板，电子表格，自助取数。 |
| UserId | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 待检测的Quick BI用户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CheckReadable &WorksId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserId=de4bc5f9429141cc8091cdd1c15b****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI 权限

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI 式

## 修改数据门户菜单的可见方式

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataPortal Id | Strin g | Query | 是 | 0d173abb53e84c8ca749 5429163b**** | 数据门户的ID。 |
| MenuIds | Strin g | Query | 是 | 54kqgoa****,pg1n135** ** | 数据门户的叶子节点菜单 ID。 目录菜单无法进行授权操作支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为100 |
| ShowOnly WithAcces s | Boole an | Query | 是 | true | 是否仅授权可见。取值范围： true：仅授权可见 false：都可见 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Integer | 2 | 修改成功的菜单数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ChangeVisibilityModel &DataPortalId=0d173abb53e84c8ca7495429163b**** &MenuIds=54kqgoa****,pg1n135**** &ShowOnlyWithAccess=true
```

&公共请求参数 Quick BI 式正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":2
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0580800008 | AccessMenu.NotMatch.Portal | The menu does not match the BI portal. |
| 400 | AE0580800016 | FolderMenu.CanNot.Authorize | The folder type menu cannot be authorized. Menu ID: %s. |
| 400 | AE0580800015 | Menu.NotBelongTo.CurrentDat aportal | Menu %s does not belong to the current data portal %s. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 删除数据作品的分享授权

删除数据作品的一个分享授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ReportId | Strin g | Query | 是 | 6b407e50-e774-406b- 9956-da2425c2**** | 作品的ID。这里的作品包括数据门户，仪表板，电子表格，自助取数。 |
| ShareToId s | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 被分享者的ID，可能是 Quick BI的用户ID，也可能是用户组ID。 ShareToType=0（用户）时，ShareTo为用户 ID。 ShareToType=1（用户组）时，ShareTo为用户组ID。 ShareToType=2（组织）时，ShareTo为组织 ID。 |
| ShareToT ype | Integ er | Query | 是 | 0 | 删除方式。取值范围： 0：按用户删除 1：按用户组删除 2：按组织删除 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | DC4E1E63-B337- 44F8-8C22- 6F00DF67E2C3 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

Quick BI

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CancelReportShare &ReportId=6b407e50-e774-406b-9956-da2425c2**** &ShareToIds=de4bc5f9429141cc8091cdd1c15b**** &ShareToType=0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"DC4E1E63-B337-44F8-8C22-6F00DF67E2C3",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0510130015 | Resource.NotBelongTo.Current Organization | The resource does not belong to the current organization. |
| 400 | AE0150100033 | User.NotBelongTo.CurrentOrga nization | The user %s does not belong to the current organization. |
| 400 | AE0150020307 | Usergroup.NotBelongTo.Curren tOrganization | The usergroup %s does not belong to the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

|  | Quick BI |  |  | 开发指南·删除数据作品的分享授权 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 取消作品收藏

取消用户收藏的数据作品。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | 5d6ae4e7-cede-43cd- b4d3-d2fd442a9202 | 取消收藏的作品ID。 |
| UserId | Strin g | Query | 是 | 121344444790**** | 收藏用户的ID。此处的用户 ID为Quick BI的UserID， 而非阿里云的UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7c7223ae-****- 3c744528014b | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CancelCollection &WorksId=5d6ae4e7-cede-43cd-b4d3-d2fd442a9202 &UserId=121344444790****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7c7223ae-****-3c744528014b",
 "Success":true,
 "Result":true
}
```

Quick BI

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0510200017 | Favorite.NotCancel.Permission | You have not added this work to favorites. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 批量取消数据门户菜单授权

根据门户菜单ID，取消指定用户、用户组的授权记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataPortal Id | Strin g | Query | 是 | 0d173abb53e84c8ca749 5429163b**** | 数据门户的ID。 |
| MenuIds | Strin g | Query | 是 | 54kqgoa****,pg1n135** ** | 数据门户的叶子节点菜单 ID。 目录菜单无法进行授权操作支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为100 |
| UserGrou pIds | Strin g | Query | 否 | 34fd141d-4598-4093- 8c33- 8e066dcb****,3d2c23d4 -2b41-4af8-a1f5- f6390f32**** | 用户组ID列表。 支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为200 UserGroupIds和 UserIds不能同时为空 |
| UserIds | Strin g | Query | 否 | 204627493484****,1213 44444790**** | 用户ID列表。此处为Quick BI的UserID，而非阿里云的 UID。 支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为200 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Integer | 2 | 取消授权成功的菜单数。 |

Quick BI

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CancelAuthorizationMenu &DataPortalId=0d173abb53e84c8ca7495429163b**** &MenuIds=54kqgoa****,pg1n135****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":2
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0580800008 | AccessMenu.NotMatch.Portal | The menu does not match the BI portal. |
| 400 | AE0580800016 | FolderMenu.CanNot.Authorize | The folder type menu cannot be authorized. Menu ID: %s. |
| 400 | AE0580800015 | Menu.NotBelongTo.CurrentDat aportal | Menu %s does not belong to the current data portal %s. |
| 400 | AE0150100033 | User.NotBelongTo.CurrentOrga nization | The user %s does not belong to the current organization. |
| 400 | AE0150020307 | Usergroup.NotBelongTo.Curren tOrganization | The usergroup %s does not belong to the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |

| 开发指南·批量取 | 消数据门户菜单授权 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 数据门户菜单批量授权

数据门户菜单的批量授权，已经授权的会自动略过。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataPortal Id | Strin g | Query | 是 | 0d173abb53e84c8ca749 5429163b**** | 数据门户的ID。 |
| MenuIds | Strin g | Query | 是 | 54kqgoa****,pg1n135** ** | 数据门户的叶子节点菜单 ID。 目录菜单无法进行授权操作支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为100 |
| UserGrou pIds | Strin g | Query | 否 | 34fd141d-4598-4093- 8c33- 8e066dcb****,3d2c23d4 -2b41-4af8-a1f5- f6390f32**** | 用户组ID列表。 支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为200 UserGroupIds和 UserIds不能同时为空 |
| UserIds | Strin g | Query | 否 | 204627493484****,1213 44444790**** | 用户ID列表。此处为Quick BI的UserID，而非阿里云的 UID。 支持批量传参，ID之间用半角逗号（,）隔开，批量修改的最大数为200 |
| AuthPoint sValue | Integ er | Query | 否 | 3 | 授权菜单的权限。取值范围： 1：查看 3：查看+导出（默认） |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 188F0B12-00EF- 41B3-944A- FB7EF06C9F43 | 请求ID。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Integer | 2 | 授权成功的菜单数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AuthorizeMenu &DataPortalId=0d173abb53e84c8ca7495429163b**** &MenuIds=54kqgoa****,pg1n135****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"188F0B12-00EF-41B3-944A-FB7EF06C9F43",
 "Success":true,
 "Result":2
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0580800008 | AccessMenu.NotMatch.Portal | The menu does not match the BI portal. |
| 400 | AE0580800016 | FolderMenu.CanNot.Authorize | The folder type menu cannot be authorized. Menu ID: %s. |
| 400 | AE0580800015 | Menu.NotBelongTo.CurrentDat aportal | Menu %s does not belong to the current data portal %s. |
| 400 | AE0150100033 | User.NotBelongTo.CurrentOrga nization | The user %s does not belong to the current organization. |
| 400 | AE0150020307 | Usergroup.NotBelongTo.Curren tOrganization | The usergroup %s does not belong to the current organization. |

| Quick BI |  |  | 开发指南·数据门户菜单批量授权 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 批量添加成员到工作空间

批量添加工作空间成员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| UserIds | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 用户ID。此处为Quick BI的 UserID，而非阿里云的 UID。 支持批量传参，用户ID之间用半角逗号（,）隔开。 |
| RoleId | Long | Query | 是 | 25 | 角色ID。取值范围： 25：管理员 26：开发者 27：分析者 30：阅览者 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7AAB95D7-2E11- 4FE2-94BC- 858E4FC0C976 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功，存在添加部分成员成功，部分失败的情况，添加失败的原因参考返回结果中的FailureDetail false：请求失败，不会持久化任何数据 |
| Result | Struct |  | 返回接口执行结果。 |
| -Failure | Integer |  |  |
| -FailureDetail | Map |  |  |
| -Total | Integer |  |  |
| -Success | Integer |  |  |

Quick BI

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddWorkspaceUsers &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserIds=de4bc5f9429141cc8091cdd1c15b**** &RoleId=25
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"7AAB95D7-2E11-4FE2-94BC-858E4FC0C976",
 "Success":true,
 "Result":{
  "FailureDetail":"",
  "Total":"",
  "Failure":"",
  "Success":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |

|  | 开发指南·批量添 | 加成员到工作空间 |  | Quick B | I |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 添加成员到工作空间

在指定的工作空间添加成员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Workspac eId | Strin g | Query | 是 | 95296e95-ca89-4c7d- 8af9-dedf0ad0**** | 工作空间ID。 |
| UserId | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 被添加的Quick BI用户ID。 |
| RoleId | Long | Query | 是 | 25 | 角色ID。 25：管理员 26：开发者 27：分析者 30：阅览者 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUserToWorkspace &WorkspaceId=95296e95-ca89-4c7d-8af9-dedf0ad0**** &UserId=de4bc5f9429141cc8091cdd1c15b**** &RoleId=25
```

&公共请求参数正常返回示例 Quick BI `JSON` 格式

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0150010002 | User.RoleType.Valid | The role ID is invalid. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150010008 | Workspace.Type.Error | The type of group workspace is invalid. |
| 400 | AE0150010013 | User.Not.WorkspaceAdmin | Only administrators of the group workspace can perform this operation. |
| 400 | AE0591000014 | ApiUser.Not.Exists | The specified user does not exist. |
| 400 | AE0150010017 | Viewer.AddInTo.Workspace | Organization members with viewer type are not allowed to add to workspace: %s. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0150010001 | User.AlreadyIn.Workspace | This user already exists. |
| 400 | AE0150010003 | User.AlreadyIn.Role | The user is already assigned this role. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |

|  | Quick BI |  |  | 开发指南·添加成员到工作空间 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

Quick BI

## 新增组织成员标签元信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TagName | Strin g | Query | 是 | 职位 | 标签名称。格式检查： 最大长度50个字符。 只允许输入中英文数字和/\|符号。 |
| TagDescri ption | Strin g | Query | 否 | 部门内的职位 | 标签描述。格式检查：最大长度255个字符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | String | 0822a7d9-****- ****-****- f20163ab9b0d | 返回添加成功的标签ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUserTagMeta
```

`&TagName=`职位 &公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":"0822a7d9-****-****-****-f20163ab9b0d"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150100025 | TagName.Repeat | The tag name is duplicated. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 添加成员到用户组

将组织成员添加到指定的用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserGrou pId | Strin g | Query | 是 | 555c4cd**** | 用户组ID。 |
| UserIdList | Strin g | Query | 是 | 46e537a5****,3dadsu*** * | Quick BI的用户ID，可输入多个，以英文逗号（,）分隔，例如：abc,efg。最多可输入1000条。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | B6141A5A-A9EF- 5F16-BF34- EFB9C1CCE4F3 | 请求 ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回添加用户组成员的结果。取值范围： true：添加成功 false：添加失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUserGroupMember &UserGroupId=555c4cd**** &UserIdList=46e537a5****,3dadsu****
```

&公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"B6141A5A-A9EF-5F16-BF34-EFB9C1CCE4F3",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0150020003 | Invalid.User | The user does not exist and cannot be added to a user group. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0510000035 | Parameter.Length.Exceed | Parameter length exceeds maximum limit: [%s]. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 添加组织成员

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AdminUse r | Boole an | Query | 是 | true | 是否是管理员。取值范围： true：是 false：否 |
| AuthAdmi nUser | Boole an | Query | 是 | true | 是否是权限管理员。取值范围： true：是 false：否 |
| UserType | Integ er | Query | 是 | 1 | 组织成员的角色类型。取值范围： 1 ：开发者 2 ：访问者 3 ：分析师 |
| AccountN ame | Strin g | Query | 是 | xxxxxx@163.com | 阿里云账号名称。 说明：如果是子账号，格式为『主账号：子账号』。例如： master test@aliyun.c _ om:subaccount 格式检查：最大长度50 个字符。 |
| NickName | Strin g | Query | 是 | 张三 | 阿里云账号昵称。 格式检查：最大长度50 个字符。 特殊格式校验：中英文数字 \ / \| () ] [ _ |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D787E1A3-A93C- 424A-B626- C2B05DF8D885 | 请求ID。 |

|  | Quick BI |  |  | 开发指南·添加组织成员 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Struct |  | 返回新增阿里云用户的详细信息。 |
| -UserType | Integer |  |  |
| -Email | String |  |  |
| -UserId | String |  |  |
| - AuthAdminUse r | Boolean |  |  |
| -NickName | String |  |  |
| -AdminUser | Boolean |  |  |
| -Phone | String |  |  |
| -AccountName | String |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUser &AdminUser=true &AuthAdminUser=true &UserType=1 &AccountName=xxxxxx@163.com
```

`&NickName=`张三 &公共请求参数正常返回示例 `JSON` 格式 Quick BI

```json
{
 "RequestId":"D787E1A3-A93C-424A-B626-C2B05DF8D885",
 "Success":true,
 "Result":{
  "Email":"",
  "UserId":"",
  "Phone":"",
  "AdminUser":"",
  "NickName":"",
  "UserType":"",
  "AuthAdminUser":"",
  "AccountName":""
 }
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010021 | Organization.Developers.Reac hedTheUpperLimit | The developers of the organization have reached the upper limit:%s |
| 400 | AE0520010023 | Organization.Viewers.Reached TheUpperLimit | The visitors of the organization have reached the upper limit:%s. |
| 400 | AE0520010022 | Organization.Analysts.Reached TheUpperLimit | The analysts of the organization have reached the upper limit:%s. |
| 400 | AE0150100010 | NickName.AlreadyIn.Organizati on | The alias already exists. |
| 400 | AE0150100022 | User.AlreadyIn.Organization | This user is already a member of the current organization. |
| 400 | AE0150100001 | User.AlreadyIn.Organization | The user already exists. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |
| 400 | AE0520010013 | Instance.Over.MaxLicense | You have reached the maximum number of users that can be added. Please upgrade the configurations or remove some users first. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |

| Quick BI |  |  | 开发指南·添加组织成员 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0510000005 | Invalid.Parameter | An error occurred while verifying parameters. |
| 400 | AE0510000038 | Invalid.Parameter.Error | The parameter is invalid:%s. |
| 400 | AE0150100005 | Invalid.User.Admin | You are not an administrator of this organization. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |

Quick BI

## 用户退出所有用户组

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UserId | Strin g | Query | 是 | 46e5374665ba4b679ee 22e2a2927**** | 用户ID。此处为Quick BI的 UserID，而非阿里云的 UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8749D65-E80A- 433C-AF1B- CE9C180FF3B4 | 请求ID。 |
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=WithdrawAllUserGroups &UserId=46e5374665ba4b679ee22e2a2927****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"D8749D65-E80A-433C-AF1B-CE9C180FF3B4",
 "Success":true,
 "Result":true
}
```

**错误码**

Quick BI

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000015 | System.Param.empty | This error code has been discarded. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |

Quick BI

## 添加数据作品分享配置

添加数据作品的一个分享配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WorksId | Strin g | Query | 是 | 6b407e50-e774-406b- 9956-da2425c2**** | 分享作品的ID。这里的作品包括数据门户，仪表板，电子表格，自助取数。 |
| ShareToId | Strin g | Query | 是 | de4bc5f9429141cc8091 cdd1c15b**** | 被分享者的ID，可能是 Quick BI的用户ID，也可能是用户组ID。 ShareToType=0（用户）时，ShareTo为用户 ID。 ShareToType=1（用户组）时，ShareTo为用户组ID。 ShareToType=2（组织）时，ShareTo为组织 ID。 |
| ShareToT ype | Integ er | Query | 是 | 0 | 分享类型。取值范围： 0：用户 1：用户组 2：组织 |
| ExpireDat e | Long | Query | 是 | 1608202110838 | 分享的有效期限，格式为毫秒级时间戳 。 |
| AuthPoint | Integ er | Query | 是 | 3 | 授权类型。取值范围： 1：仅查看 3：查看并导出 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 05739b8e-3de0- 4204-9669- 7f04f02522b9 | 请求ID。 |

Quick BI

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。取值范围： true：请求成功 false：请求失败 |
| Result | Boolean | true | 返回接口执行结果。取值范围： true：执行成功 false：执行失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddShareReport &WorksId=6b407e50-e774-406b-9956-da2425c2**** &ShareToId=de4bc5f9429141cc8091cdd1c15b**** &ShareToType=0 &ExpireDate=1608202110838 &AuthPoint=3
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"05739b8e-3de0-4204-9669-7f04f02522b9",
 "Success":true,
 "Result":true
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510130012 | Report.NotExist.Error | This work does not exist. It may have been deleted. Work ID is %s. |
| 400 | AE0150010007 | Workspace.Not.Exist | The group workspace does not exist. |
| 400 | AE0150100012 | Workspace.NotIn.Organization | The workspace is not owned by the organization. |
| 400 | AE0510200012 | Workspace.Share.Forbidden | Content in the current group workspace cannot be shared. |
| 400 | AE0150100013 | UserInfo.Error | The personal information is invalid. |

| 开发指南·添加数 | 据作品分享配置 |  | Quick B |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AE0510200013 | Workspace.OutsideShare.Forbi dden | Content in the current group workspace cannot be shared with another organization. |
| 400 | AE0150020002 | Usergroup.Not.Exist | The user group does not exist. |
| 400 | AE0150020305 | UserGroup.NotIn.Organization | The user group is not in the current organization. |
| 400 |  | Internal.System.Error | An internal system error occurred. |
| 400 | AE0510140015 | Share.ExpireDate.Error | The expire date is illegal. |
| 400 | AE0520010008 | Instance.Expired | Your instance has expired. |
| 400 | AE0520010001 | Instance.Not.Exist | The specified instance does not exist. |
| 400 | AE0150100003 | Invalid.Organization | The specified organizational unit does not exist. |
| 400 | AE0150100004 | User.Not.In.Organization | The specified user is not in the organizational unit. |
| 400 | AE0510000031 | Invalid.Param.Error | The parameter is invalid. |
| 400 | AE0510000015 | System.Param.Empty | You must specify the %s parameter. |
| 400 | AE0580800012 | Access.Forbidden | Access forbidden. Your instance version or access key is not allowed to call the API operation. |
| 400 | AE0150100004 | Invalid.User.Organization | The user is not in your organization. |
