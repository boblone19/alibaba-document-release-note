---
title: "运维编排 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 29
source_pdf: "08_运维指南_o-m-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/oos/zh/o-m-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 运维编排 运维指南

运维编排

## 入门概述

本快速入门指引您快速创建一个运维编排模板，并执行模板。 本快速入门包含以下操作：
1. 新建模版
以一个简单的示例模版为例，介绍如何新建模板，详情请参见新建模板。

## 2. 创建执行

选择新建的模版创建执行任务并启动执行，详情请参见创建执行。 运维编排

## 新建模板

本示例中，创建一个简单的示例模板，输入为ECS实例的某个特定状态（比如Running或者Stopped），输出为此账号下处于该特定状态的ECS实例的ID列表。该模板会执行DescribeInstances的OpenAPI，并自动翻页进行查询。如果此账号下符合该特定状态的ECS实例数量小于1000，则将全部列出，否则，列出前 1000个。

**操作步骤**

1. 登录专有云运维编排管理控制台。
2. 选择自定义任务模板，单击**创建模板**。
3. 在基本信息区域，配置模板参数。
4. 输入**模板名称**，本示例中为DescribeInstances。
运维编排
5. 在**模板详情**区域，选择**YAML**格式，并输入以下示例模板。您可以修改此模板，增加多个Task，调用
任意的OpenAPI。

```
---
 Description: DescribeInstances
 FormatVersion: OOS-2019-06-01
 Parameters:
     Status:
         Description: Running or Stopped
         Type: String
 Tasks:
   - Name: describeInstances
     Action: ACS::ExecuteAPI
     Properties:
         Service: ECS
         API: DescribeInstances
         Parameters:
             Status: "{{ Status }}"
     Outputs:
         InstanceIds:
             Type: List
             ValueSelector: .Instances.Instance[].InstanceId
 Outputs:
     InstanceIds:
         Type: List
         Value: "{{ describeInstances.InstanceIds }}"
```

6. 单击**创建模板**。
运维编排

## 创建执行

创建模板后，您需要为该模板创建执行并启动执行。

**操作步骤**

1. 登录**运维编排管理控制台**。
2. 在**我的模板**页面，选择模板**创建执行**。
3. 在**创建执行**页面，设置**基本信息**。
本示例中，选择**执行模式**为**自动执行**。参数解释如下：

| 参数 | 描述 |
|---|---|
| 执行模式 | 自动执行：确认创建后，将自动执行。 单步执行：确认创建后，需要手动开启执行。 |
| 失败暂停 | 若为循环任务，当子任务执行有失败时，执行会暂停，等待您调整并决定是否继续执行。 |
| 模板类别 | 公共模板：平台提供的常用场景的模板。 自定义模板：根据自身需求您创建的模板。 |
| 模板选择 | 选择您新建的模板。 |

4. 单击**下一步：设置参数**，输入需要设置的参数。本示例的模板中有参数**Status**，设置该参数的值为
**Stopped**。
5. 单击**下一步：确认创建**。
6. 单击**创建执行**。
运维编排
7. 返回**执行管理**页面，查看提交的执行。
如果选择了**自动执行**，则自动开始执行。执行完毕后，**执行状态**显示**成功**。 如果选择了**单步执行**或**高风险操作需要二次确认**，则需要手动开始执行。
8. 单击**执行****ID**或**详情**页面，查看执行状态。
运维编排

## 批量释放ECS实例

运维编排服务OOS为批量释放实例的场景提供了公共模板。只需输入需要被释放的实例ID，就可以达到释放所有实例的操作，避免手动操作单独释放实例。本文介绍批量删除按量付费实例的操作及批量删除实例的背后逻辑。

**前提条件**

确保需被释放的实例类型属于**按量计费**。

**操作步骤**

1. 登录运维编排管理控制台。
2. 在左侧导航栏，单击**公共任务模板**。
3. 在搜索框内搜索ACS-ECS-BulkyDeleteInstances（批量删除按量付费实例）模板。
4. 单击**创建执行**。
5. 配置基本信息。
根据实际情况填写**执行描述**，并选择**组织**和**资源集**，其余参数将由系统自动带入。 运维编排
6. 单击**下一步：设置参数**。
7. 设置参数。
输入公共模板参数：ACS-ECS-BulkyDeleteInstances。

| 参数项 | 说明 |
|---|---|
| 是否强制释放正在运行的实例 | 开启后将强制释放正在运行的实例。 |
| 选择实例 | 选择被处理的实例。支持手动选择实例、指定实例标签和选择全部。 |
| 任务执行的并发比率 | 支持设置以下参数： 执行模式：可选并发控制、批次控制。 并发速率：指定一个数值或者百分比来控制并发速率。 最大错误次数：指定任务在停止前的最大错误次数，可以是数值或者百分比，默认值是0，表示有1个错误时整个任务就会失败结束。若设置为100%则表示无论遇到多少错误整个执行都会成功。 |
| OOS扮演的RAM角色 | （默认设置）当前账号的已有权限：执行您使用的账号的权限动作。请确保您拥有创建自定义镜像涉及的所有ECS API调用权限。 指定RAM角色，使用该角色的权限：如果指定了RAM角色名称，OOS扮演该RAM角色执行运维任务。 |

运维编排
8. 单击**下一步：确定**。
9. 单击**创建**。
0. 在**任务执行管理**中可查看刚刚创建的执行，若创建执行成功，且执行状态处于运行中，则表示实例处于删
除中。
1. 在目标任务执行详情页，单击**高级视图** > **可视化预览**。
状态为成功时，表示实例被删除。 运维编排
2. 查询实例是否被删除。

**公共模板和背后逻辑**

**批量删除非预付费实例（ACS-ECS-BulkyDeleteInstances）**

该模板顺序执行以下任务：
1. 获取目标实例或实例上的Tags。
2. 批量删除实例。

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky delete ECS postpaid instances.
```

`zh-cn:` 批量删除`ECS`按量付费实例。

```
  name-en: ACS-ECS-BulkyDeleteInstances
```

`name-zh-cn:` 批量删除`ECS`实例

```
  categories:
    - instance_manage
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  force:
    Description:
      en: Whether to force the release of a running instance.
```

运维编排 e:

```
ete
```

`to`

```
ocete eeaseo
```

a u g

```
stace.
```

`zh-cn:` 是否强制释放正在运行的实例。

```
    Type: Boolean
    Default: false
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
```

`zh-cn:` 任务执行的并发比率。

```
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 10
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
```

`zh-cn: OOS`扮演的`RAM`角色。

```
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
```

`zh-cn:` 获取`ECS`实例。

```
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
  - Name: deleteInstance
    Action: 'ACS::ExecuteAPI'
    Description:
      en: Deletes ECS instance with the specified instance ID.
```

`zh-cn:` 通过指定实例`ID`删除实例。

```
    Properties:
      Service: ECS
      API: DeleteInstance
      Parameters:
        InstanceId: '{{ ACS::TaskLoopItem }}'
        Force: '{{ force }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
```

**批量删除预付费实例（ACS-ECS-BulkyDeletePrepaidInstances）**

该模板顺序执行以下任务：
1. 获取目标实例或实例上的Tags。
运维编排
2. 将预付费实例修改为按量付费实例。
3. 批量删除实例。

```
FormatVersion: OOS-2019-06-01 Description:
  en: >-
    Bulky delete prepaid instances.The specified ECS instances must be in
    stopped status.
```

`zh-cn:` 批量删除`ECS`预付费实例。指定的`ECS`实例必须处于已停止状态。

```
  name-en: ACS-ECS-BulkyDeletePrepaidInstances
```

`name-zh-cn:` 批量删除`ECS`预付费实例

```
  categories:
    - instance_manage
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
```

`zh-cn:` 任务执行的并发比率。

```
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 10
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
```

`zh-cn: OOS`扮演的`RAM`角色。

```
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
```

`zh-cn:` 获取`ECS`实例。

```
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
  - Name: modifyInstanceChargeType
    Action: 'ACS::ExecuteAPI'
    Description:
      en: Modify the charge type for prepaid instances to postpaid.
```

运维编排 `zh-cn:` 修改预付费实例付费方式为按量付费。

```
    Properties:
      Service: ECS
      API: ModifyInstanceChargeType
      Parameters:
        InstanceIds: '{{ getInstance.instanceIds }}'
        InstanceChargeType: PostPaid
  - Name: deleteInstance
    Action: 'ACS::ECS::DeleteInstance'
    Description:
      en: Deletes the ECS instance by instance ID.
```

`zh-cn:` 通过实例`ID`删除实例。

```
    Properties:
      instanceId: '{{ ACS::TaskLoopItem }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
```

运维编排

## 自动定时重启ECS云服务器

本文介绍如何通过设置定时任务自动重启ECS来维护不同场景下的系统稳定性和安全性，帮助系统管理员简化维护流程、提升系统稳定性、优化用户体验，并增强系统的安全性与合规性。

**背景**

无论是电子商务、在线教育、游戏，还是流媒体等业务，服务器的稳定运行都是至关重要的。然而，在实际运行中，我们可能会遇到这样一些场景： 系统更新：一些操作系统或者软件的更新可能需要重启服务器才能生效。通过定时重启能够保证这些更新的正常应用。 内存泄漏：有的程序可能存在内存泄漏的问题，长时间运行后可能会消耗大量的服务器内存，影响服务器性能。通过定时重启可以释放这部分内存。 高负载运行：对于一些需要持续高负载运行的服务器，定时进行重启可以避免因长时间高负载运行带来的潜在问题。 缓存问题：有一些应用程序可能会产生大量的缓存数据，如果不定期清理可能会影响存储空间，通过定时重启服务器，可以清理这部分缓存。 安全原因：定时重启服务器，可以降低被黑客攻击的风险，因为黑客往往需要一段时间来探测和攻击系统，定时重启可以打乱他们的计划。 日志文件：一些程序会定期生成日志文件，长时间运行可能会导致日志文件过大，占用过多硬盘空间。通过定时重启，可以定期清理这些日志。 在这种情况下，我们可以使用OOS服务来创建定时任务，自动重启ECS实例。在进行设置时，我们需要注意合理设置重启的时间，评估重启对业务的影响，尽可能避免在业务高峰期进行，以免影响业务的正常运行。

**操作步骤**

1. 登录OOS控制台。
2. 在左侧导航栏找到**定时运维**，单击**创建**。
3. 定时设置选择周期性重复执行。
运维编排
4. 模板选择 ACS-ECS-BulkyRebootInstances ，然后配置参数创建执行。
运维编排

## 带审批的自动运维

本文介绍OOS的审批运维功能。

**背景信息**

在自动化运维中，某些高风险或高成本操作（如删除核心资源、启动高配实例、批量重启生产服务器等）若完全自动化，可能带来失控风险；但若退回手工操作，又会破坏自动化流程的一致性与可追溯性。在自动化流程中嵌入人工审批环节，既保留自动化的效率优势，又确保关键操作受到必要的人工监督。

**解决方案**

在运维编排服务中，当被执行模板中包括审批动作，且执行到审批动作所在任务时，OOS执行引擎会暂停执行，执行进入等待中状态，并发送一个包含通知的审批链接到管理员用户。当管理员点击审批链接后，可根据业务需求作出审批决定，同意或拒绝，同意后则OOS引擎继续执行后续任务，拒绝后引擎停止执行，执行状态转为已取消（Cancelled）。

**操作步骤**

1. 登录运维编排管理控制台。
2. 在左侧导航栏，单击**自定义任务模板**。
3. 单击**创建模板**。
4. 配置**基本信息**。

| 参数项 | 说明 |
|---|---|
| 模板名称 | 模板的名称，由字母、数字、中划线、下划线组成，最长支持128字符，且不能以ALIYUN、 ACS、ALIBABA、ALICLOUD开头。 |
| 组织 | 模板所属的组织。 |
| 资源集 | 模板所属的资源集。 |
| 版本描述 | 模板的版本描述。 |

运维编排
5. 单击**YAML**，将**附录**1**：模板（审批****ECS****实例重启）**粘贴到空白编辑栏。
6. 单击**创建模板**。
7. 在**自定义模板**中，单击目标模板**操作**列的**创建执行**。
8. 配置基本信息。
请选择组织、资源集以及执行描述。系统将自动填充其余参数。
9. 单击**下一步，设置参数**。
0. 输入以下的参数。

| 参数项 | 是否必填 | 参数说明 |
|---|---|---|
| targets | 是 | 将重启的实例范围。 |
| webHookUrl | 是 | 审批通知及链接将发送到的钉钉群助手WebHook。获取方法可参考附录2：钉钉WebHook获取。 |
| rateControl | 否 | 并发速率控制。 |
| atMobiles | 否 | 发送审批通知时，在钉钉群中@的指定的用户。 |
| atAll | 否 | 发送审批通知时，是否@钉钉群中的所有成员。 |
| OOSAssumeRole | 否 | OOS默认使用当前登录用户的权限执行动作；如果指定了RAM角色名称，OOS扮演该RAM角色执行动作。 |

运维编排
1. 单击**下一步：确定**。
2. 单击**创建**。
3. 在**任务执行管理**中可查看刚刚创建的执行，若创建执行成功，被指定的手机号的用户，在钉钉群中会被
@，且当前执行状态处于等待中，用户可以单击审批链接，根据需要作出审批决定。

**附录1：模板（审批ECS实例重启）**

模板任务逻辑： i. 捕捉所选实例信息。 ii. 下发对实例重启的审批通知及链接。 iii. 如审批通过，对所选实例进行重启。 模板内容（YAML）

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky restarts the ECS instances with Approval.
```

`zh-cn:` 批量重启`ECS`实例带审批。

```
  name-en: BulkyRebootInstancesWithApproval
```

`name-zh-cn:` 批量重启`ECS`实例带审批

```
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
```

`zh-cn:` 任务执行的并发比率。

```
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 100%
webHookUrl:
```

运维编排

```
  webHookUrl:
    Description:
      en: >-
        The webHook url of dingtalk group assistant,
        e.g.https://oapi.dingtalk.com/robot/send?access_token=1234zxcvaksdq31414.
      zh-cn: >-
```

钉钉群助手的`webhook`地址，形如https://oapi.dingtalk.com/robot/send?

```
access_token=1234zxcvaksdq31414。
    Type: String
  atMobiles:
    Description:
      en: >-
        The telephone numbers of member in dingtalk group assistant @, when
        notify comes.
```

`zh-cn:` 当群助手向钉钉群中发送审批通知时，要被@的群成员注册钉钉所用手机号。

```
    Type: List
    Default:
      - '12345678901'
  atAll:
    Description:
      en: 'assistant @ all members in dingtalk group or not, when notify comes.'
```

`zh-cn:` 当群助手向钉钉群中发送审批通知时是否@所有人。

```
    Type: String
    Default: 'false'
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
```

`zh-cn: OOS`扮演的`RAM`角色。

```
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
```

`zh-cn:` 获取`ECS`实例。

```
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
      instanceNames:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceName'
  - Name: approveRestart
    Action: 'ACS::Approve'
    Properties:
      NotifyType: WebHook
      WebHook:
        URI: '{{webhookUrl}}'
        Headers:
```

运维编排

```
          Content-Type: application/json
        Content:
          msgtype: text
          text:
            content: >-
              Notify: please approve instances restart, instance names to
              approve  are {{getInstance.instanceNames}}, sent by
              {{ACS::RegionId}} oos {{ACS::ExecutionId}}.
          at:
            atMobiles: '{{atMobiles}}'
            isAtAll: '{{atAll}}'
  - Name: rebootInstance
    Action: 'ACS::ECS::RebootInstance'
    Description:
      en: Restarts the ECS instances.
```

`zh-cn:` 重启实例。

```
    Properties:
      instanceId: '{{ ACS::TaskLoopItem }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
Outputs:
  instanceIds:
    Type: List
    Value: '{{ getInstance.instanceIds }}'
```

**附录2：钉钉WebHook获取**

1. 选择要添加群助手通知的群，单击
。 运维编排
2. 单击**智能群助手**。
3. 单击**添加机器人**。
运维编排
4. 单击**自定义**。
5. 单击**添加**。
运维编排
6. 填写**机器人名字**，本示例**安全设置**选择**自定义关键字**，并输入WebHook通知内容中所包含的词汇作为关
键字，比如本示例模板通知内容中含"Notify"，于是在该处可填写"Notify"。单击**完成**。
7. 单击**复制**，获取到WebHook地址。
运维编排

## 常见问题

本文汇总了使用OOS时的常见问题。 子账户进行操作，报错：User has no permission to do the action: (ListTemplates) 子账户进行操作，报错：User has no permission to do the action: (PassRole) 执行模板时遇到报错：Assumes role failed. Code: EntityNotExist.Role, msg: The role not exists: acs:111111:role/OOSServiceRole. 执行模板时报错：Assumes role failed. Code: NoPermission, msg: You are not authorized to do this action. You should be authorized by RAM.

**子账户进行操作，报错：User has no permission to do the action:**

**(ListTemplates)**

原因：子账户权限不够，不能执行OOS的指定API。 解决办法：以管理员或者主账户身份，登录**RAM****控制台**，对报错的子账户进行适当授权，授权范围可以是相关API，也可是所有API，下面样例 `"Action": "oos:*"` 则是对所有API授权，详情请参见**账户访问控** 制。

```json
{
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "oos:*",
          "Resource": "*"
      }
```

`],`

```json
  "Version": "1"
}
```

**子账户进行操作，报错：User has no permission to do the action:**

**(PassRole)**

原因：子账户没有PassRole权限，不能以指定的Role执行运维编排。 解决办法：以管理员或者主账户身份，在**RAM****控制台**，对子账户做适当的PassRole授权，参见**账户访问控** 制。

```json
{
  "Statement": [
      {
          "Effect": "Allow",
          "Action": "oos:*",
          "Resource": "*"
      }
```

`],`

```json
  "Version": "1"
}
```

**执行模板时遇到报错：Assumes role failed. Code:**

**EntityNotExist.Role, msg: The role not exists:**

**acs:111111:role/OOSServiceRole.**

运维编排原因：没有为OOS服务创建默认的RAM角色。 解决办法：主账户或者管理员登录**RAM****控制台**>的RAM访问控制，增加对应的RAM角色 OOSServiceRole。请参见为**OOS****服务设置****RAM****权限**。

**执行模板时报错：Assumes role failed. Code: NoPermission, msg:**

**You are not authorized to do this action. You should be**

**authorized by RAM.**

原因：对应的RAM角色没有给OOS服务配置信任策略。 解决办法：主账户或者管理员登录**RAM****控制台**的RAM访问控制，增加对应的RAM角色OOSServiceRole。 请参见为**OOS****服务设置****RAM****权限** 1.登录**RAM****控制台**，在角色中输入"OOSServiceName"进行搜索： 2.点击信任策略： 3.修改信任策略： 将信任策略修改为如下内容： 运维编排

```json
{
  "Statement": [
      {
          "Action": "sts:AssumeRole",
          "Effect": "Allow",
          "Principal": {
              "Service": [
                  "oos.aliyuncs.com"
```

]

```
          }
      }
```

`],`

```json
  "Version": "1"
}
```
