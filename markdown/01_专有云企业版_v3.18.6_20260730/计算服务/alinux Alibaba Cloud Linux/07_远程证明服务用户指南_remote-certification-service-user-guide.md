---
title: "Cloud Linux 远程证明服务用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 32
source_pdf: "07_远程证明服务用户指南_remote-certification-service-user-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/alinux/zh/remote-certification-service-user-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# Cloud Linux 远程证明服务用户指南

## 快速入门

### 什么是远程证明服务

本文介绍远程证明服务的产品概述、核心能力与价值以及技术架构。

**产品概述**

远程证明服务（Remote Attestation Service）是一种基于可信计算技术的高安全性服务，旨在为分布式系统、云计算环境、物联网设备等场景提供环境可信性验证与数据完整性证明能力。通过密码学技术与硬件级安全模块（如TPM/TEE），该服务可实时验证远程设备、虚拟机或容器的运行状态是否可信，确保其未被篡改或攻击，从而为业务建立“零信任”环境下的安全信任基础。

**核心能力与价值**

**核心功能**

**环境可信性验证**

实时检测远程设备/服务的硬件、固件、操作系统及关键应用的完整性，确保运行环境未被恶意篡改。验证范围：启动链（Boot Chain）、系统配置、关键进程、安全策略等。

**动态身份认证**

基于环境可信状态生成动态身份凭证，替代传统静态密钥，防止身份盗用或仿冒攻击。

**数据完整性证明**

为关键数据或代码生成密码学证明报告，供第三方验证其来源与完整性，适用于合规审计、跨平台协作等场景。

**威胁实时告警**

检测到异常环境（如未授权修改、恶意软件注入）时，可触发告警等操作。

**自动化合规审计**

生成标准化证明报告，满足GDPR、等保2.0、ISO 27001等法规对系统可信性的要求。

**白屏化管理**

提供白屏化的远程证明服务管理，包含trustee实例、可信策略、验证结果展示与管理。

**客户价值**

**增强信任**：为业务合作伙伴、监管机构提供可验证的信任凭证，降低合作门槛。
**风险防控**：主动识别并隔离被篡改的节点，避免数据泄露或服务中断。
**降本增效**：自动化证明流程减少人工审计成本，加速业务上云与跨平台协作。

**技术架构**

**客户端代理**：轻量级代理程序，部署于待验证设备/服务中，采集环境数据并生成证明证据。
**证明服务端**：基于TEE（可信执行环境）或TPM（可信平台模块）签发密码学证明报告。
**审计**&**认证结果**：自动化生成审计日志，并进行远程证明结果展示。

### 远程证明策略说明

本文阐述了远程证明策略的相关说明。 远程证明策略，其本质上是一段用户可定制的代码，用于控制证据内容和参考值比对的具体要求。

**输入内容**

根据OPA策略引擎要求，输入有两类：input和data，在远程证明策略验证中，分别为如下内容： input：解析后的远程证明证据内容，即Attestation Result Token中

```
的 submods.cpu0.ear.veraison.annotated-evidence 值。
```

data：参考值Map。

**输出内容**

包含四个维度（硬件、可执行程序、配置以及文件系统）评估结果的信任向量： “configuration”：描述系统配置的可信度，例如kernel cmdline等。 “executables”：描述系统可执行程序的可信度，例如shim、grub、kernel等。 “file_system”：描述文件系统的可信度，例如rootfs、自定义度量文件等。 “hardware”：描述硬件的可信度，例如TDX、TPM、CSV等硬件属性等。 信任向量的值用IETF RATS式标准中的AR4SI draft来表示评估结果： 0~32：可信，对应 `valid` 。 33~96：警告，对应 `warning` 。 97~127：禁用，对应 `contraindicated` 。

**执行逻辑**

首先，将四个维度信任向量初始值设置为 97~127（禁用），然后分成四个模块来分别判定其可信程度，判定方法如下： 若kernel cmdline度量值等于参考值，则将 `configuration` 设置为0~32（可信）。 若shim、grub、kernel、initrd的度量值等于参考值，则将 `executables` 设置为0~32（可信）。 若AAEL中记录的文件度量值等于参考值，则将 `file_system` 设置为0~32（可信）。 若关注的硬件特定字段的值（例如安全版本号、闭源固件度量值等）等于参考值，则将 `hardware` 设置为0~32（可信）。 如果不关注其中某个维度，例如没有关注的硬件特定字段值（因为Trustee在远程证明策略验证之前已经对硬件证据进行了一轮默认签名和证书验证），也可以直接将某个维度默认设置成0~32（可信）或 33~96（警告）。

**示例**

下面是从default策略中截取的一段TDX机器的验证策略：

```java
package policy import rego.v1 default executables := 33 default hardware := 97 default configuration := 36 default file_system := 35 executables := 3 if {
 # Check the kernel, initrd, shim and grub measurements for any supported algorithm
 validate_boot_measurements_uefi_event_log(input.tdx.uefi_event_logs)
} hardware := 2 if {
 # Check the quote is a TDX quote signed by Intel SGX Quoting Enclave
 input.tdx.quote.header.tee_type == "81000000"
 input.tdx.quote.header.vendor_id == "939a7233f79c4ca9940a0db3957f0607"
 # Check TDX Module version and its hash. Also check OVMF code hash.
 input.tdx.quote.body.mr_seam in data.reference["tdx.mr_seam"]
 input.tdx.quote.body.tcb_svn in data.reference["tdx.tcb_svn"]
 input.tdx.quote.body.mr_td in data.reference["tdx.mr_td"]
} configuration := 2 if {
 # Check the TD has the expected attributes (e.g., debug not enabled) and features.
 input.tdx.td_attributes.debug == false
 input.tdx.quote.body.xfam in data.reference["tdx.xfam"]
 # Check kernel command line parameters have the expected value for any supported algor
ithm
 validate_kernel_cmdline(input.tdx.ccel, input.tdx.ccel.kernel_cmdline)
} file_system := 2 if {
 # Check measured files - iterate through all file measurements
 validate_aael_file_measurements(input.tdx.uefi_event_logs)
}
```

### 登录Apsara Uni-manager运营控制

**台**

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 勾选**我已阅读并同意产品服务协议、隐私协议、用户协议**。

**说明**

登录页展示的链接文字为文档标题，单击链接文字，可查看协议的详细内容。
**产品服务协议**、**隐私协议**和**用户协议**仅在已发布时才会显示。如果三种类型协议都没有发布，
则不需要执行该操作。
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

**相关操作**

**忘记密码**

1. 用户忘记登录密码时，单击密码输入框下方的**忘记密码**。
2. 在忘记密码页面，输入**账户名**、**邮箱**和验证码后，单击**确认**。

**说明**

账户名请输入当前账号的用户名，邮箱请输入注册账号的Email地址。 重置密码的链接将发至邮箱，进入链接后用户可输入新密码。

### 登录远程证明服务控制台

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **计算** > **可信隐私计算** > **远程证明服务**，进入远程证明服务控制台。

## 操作指南

### Trustee实例

本文介绍创建、删除、查看Trustee实例，以及为Trustee实例进行标签的绑定与解绑的相关操作。

**背景信息**

Trustee实例是远程证明服务中的核心概念及管理单元。它代表了一个独立部署、可进行管理和监控的远程证明服务环境。Trustee实例作为远程证明服务的逻辑载体和操作对象，除了提供服务健康状态的实时监控功能外，还集成了策略、资源、参考值和审计等全面的管理功能，为用户构建了一个安全、可靠且可审计的远程系统验证环境。

**约束限制**

针对tpm ECS可信实例，最多支持20个活跃会话数，即每个Trustee实例最多可为20个tpm ECS可信实例提供远程证明服务。 针对TDX ECS机密实例，最多支持5个活跃会话数，即每个Trustee实例最多可为5个TDX ECS机密实例提供远程证明服务。
1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**Trustee****实例**。
3. 在**Trustee****实例**页面，单击**创建****Trustee**。
4. 在**创建****Trustee**页面，设置相关参数，然后单击**提交**。

| 参数 | 说明 |
|---|---|
| 组织 | 待创建实例归属的组织。 |
| 资源集 | 待创建实例归属的资源集。 |
| 地域 | 待创建实例所属的地域。 |
| 名称 | 自定义Trustee实例的名称。 |
| 描述 | Trustee实例的描述信息。 |
| VPC | 选择Trustee实例要接入的虚拟私有云网络。 |
| VSwitch | 选择Trustee实例具体部署在哪一个子网内。 |

1. 在**Trustee****实例**页面，您可以通过实例ID、实例名称、标签或创建人快速筛选实例。同时，系统还支持
关键字的自动识别以筛选实例。页面展示实例的基本信息，包括**实例****ID/****实例名称**、**标签**、**描述**、**实例状** 态、**服务状态**、**活跃会话数**、**远程证明****URL**、**VPC**、**交换机**、**组织**/**资源集**、**创建人**以及**创建时间**。

**说明**

单击**活跃会话数**列的数字，弹出**服务对象**对话框，可查看**实例****ID/****名称**、**客户端****IP**以及**镜像**等信息。
2. 选择目标实例，单击目标实例ID或右侧**操作**列的**管理**，即可跳转至**实例详情**页面，查看目标实例的详细信
息。
**服务健康状态**：组件列表展示Trustee实例的**as**、**rvps**、**kbs**以及**gateway**组件的健康状态以及时
间等信息；资源列表展示**CPU**和**内存**资源的**使用量**、**限制**、**使用率**以及**水位**情况。
**服务对象**：展示Trustee实例的服务对象。包括**实例****ID/****名称**、**客户端****IP**和**镜像**等信息。
**策略管理**：展示Trustee实例所绑定的策略列表，包括**策略****ID/****策略名称**、**类型**、**策略内容**、**创建时**

**说明**

单击**策略内容**列的 ，可查看策略的具体内容和详细配置信息。 绑定策略：单击**绑定策略**，在弹出的对话框中勾选待绑定的策略，然后单击**确定**。

**说明**

解绑策略：在策略列表中，单击**操作**列的**解绑**，然后单击**确定**。
**参考值管理**：软硬件的 `key: value` 哈希值基线管理，旨在为默认认证策略提供支持。该管理机制用
于系统的运行状态下，将当前软硬件的量测值与此处设定的参考值进行比对，以判断软硬件是否存在被篡改的情况。您可在**参考值管理**页签管理和设置参考值。
**审计日志**：展示实例认证审计记录的相关信息，包括**会话****ID**、**客户端****IP**、**声明**、**状态码**、**结果**以及时
间等。

**说明**

您可以通过**会话****ID**、**客户端****IP**或**结果**快速筛选审计信息。 单击**声明**列的 ，可查看声明内容的详细信息。 单击**操作**列的**详情**，可在详情面板中查看**信任向量**和**证据详情**的详细信息。

**重要**

1. 在**Trustee****实例**页面，单击目标实例**操作**列的**删除**。
2. 在弹出的对话框中，单击**确定**。

**为单个实例绑定标签**

或上，然后单击编辑图标。

**说明**

图标表示当前实例未绑定任何标签； 图标表示当前实例已绑定标签。 ii. 在**编辑标签**对话框中，设置标签键和值，然后单击**确定**。

**说明**

单击**添加**可为实例绑定多个标签。 每个资源最多可绑定20个标签，系统标签不计入标签数量限制。 若需要对标签进行统一管理，可参考**《统一云管平台****用户指南》** > **标签管理**章节。

**批量绑定标签**

ii. 单击实例列表下方的**批量绑定标签**。 iii. 在**批量绑定标签**对话框中，单击**添加**，然后设置标签键和值，最后单击**确定**。

**说明**

单击**添加**可为实例绑定多个标签。 每个资源最多可绑定20个标签，系统标签不计入标签数量限制。 若需要对标签进行统一管理，可参考**《统一云管平台****用户指南》** > **标签管理**章节。

**为单个实例解绑标签**

上，然后单击编辑图标。 ii. 在**编辑标签**对话框中，单击标签值右侧的图标，然后单击**确定**。

**批量解绑标签**

ii. 单击实例列表下方的**批量解绑标签**。 iii. 在**批量解绑标签**对话框中，选择需要解绑的标签，然后单击**确定**。

**说明**

批量解绑是以标签键为单位进行解绑的，所以当您选择一个标签时，所有与其标签键相同的标签都会被选择。

### 策略管理

#### 证明策略管理

##### 创建证明策略

远程证明策略用于验证平台的可信度和在该平台中运行的代码的完整性。本文介绍如何创建证明策略。

**操作步骤**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**策略管理** > **证明策略管理**。
3. 在**证明策略管理**页面，单击**新增策略**。
4. 在**新增策略**对话框中，配置以下参数，然后单击**确定**。

| 参数 | 说明 |
|---|---|
| 名称 | 自定义策略名称。 |
| 策略类型 | 当前仅支持选择rego。 |
| 策略内容 | 策略的具体逻辑定义，采用所选策略类型（rego）的语法编写，用于对远程证明请求中的证据（如 TPM 测量值、系统配置、文件哈希等）进行评估，并输出判定结果（如是否可信）。更多信息可参见远程证明策略说明。 |

##### 管理证明策略

本文介绍如何查看、编辑以及删除证明策略。

**前提条件**

**操作步骤**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**策略管理** > **证明策略管理**。
4. 在证明策略列表中，您可以对策略进行以下操作：

| 操作 | 步骤 |
|---|---|
| 查看策略详情 | 在证明策略列表中，展示策略ID/策略名称、类型、策略内容、创建时间以及更新时间。 说明单击可以查看策略内容详情。 |
| 编辑策略 | i. 单击目标策略操作列的编辑。 ii. 在编辑策略对话框中，完成策略修改，然后单击确定。 |
| 删除策略 | 重要删除策略前，请确保该策略未被使用。 i. 单击目标策略操作列的删除。 ii. 单击确定。 |

### 服务对象查询

**操作步骤**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**服务对象查询**。
3. （可选）在**服务对象查询**页面，您可以通过**实例****ID**、**实例名称**、**客户端****IP**、**TrusteeID**快速筛选服务对
象。
4. 在服务对象列表，展示服务对象的**实例****ID/****名称**、**客户端****IP**、**镜像**、**实例类型**、**Trustee**以及**更新时间。**

## 常见案例

### 远程证明在ECS可信实例中的应用案例

本文介绍如何创建ECS可信实例以及在可信实例中验证远程证明和文件度量。

**创建可信实例**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**Trustee****实例**。
3. 在**Trustee****实例**页面，单击**创建****Trustee**。
4. 在**创建****Trustee**页面，设置相关参数，然后单击**提交**。

| 参数 | 说明 |
|---|---|
| 组织 | 待创建实例归属的组织。 |
| 资源集 | 待创建实例归属的资源集。 |
| 地域 | 待创建实例所属的地域。 |
| 名称 | 自定义Trustee实例的名称。 |
| 描述 | Trustee实例的描述信息。 |
| VPC | 选择Trustee实例要接入的虚拟私有云网络。 |
| VSwitch | 选择Trustee实例具体部署在哪一个子网内。 |

**步骤二：创建可信实例**

创建可信实例的步骤与创建普通实例类似，但需要注意一些特定选项。本步骤重点介绍可信实例相关的特定配置，如果您想了解其他通用配置，请参见**《云服务器** **ECS****用户指南》**中的“**创建实例**”章节。
1. 登录云服务器ECS控制台。
2. 在左侧导航栏中，选择**实例与镜像** **> ECS****实例**。
3. 在顶部菜单栏处，选择组织、资源集和地域。
4. 单击**创建实例**。
5. 在创建实例页面，配置以下参数：
i. **开启热变配**：否。 ii. **规格**：当前仅支持g7x-vtpm-k25规格族，您也可以在筛选框输入tpm搜索可信实例。 iii. **镜像**：当前仅支持**阿里云服务器操作系统** **V3 Linux 64**位**安全增强版**镜像。 iv. **VPC/VSwitch**：选择步骤一：创建Trustee实例时选择的VSwitch。

**远程证明验证**

1. 使用Workbench工具以SSH协议登录Linux实例，具体操作请参考**《云服务器** **ECS****用户指南》**中的“**使用**
**Workbench****工具以****SSH****协议登录****Linux****实例**”章节。
2. 执行测试命令，触发远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

3. 在远程证明控制台左侧导航栏，单击**Trustee****实例**。
4. 在**Trustee****实例**页面，单击可信实例对应Trustee实例操作列的**管理**，进入Trustee实例详情页。
5. 在Trustee实例详情页，单击**审计日志**页签，然后单击**声明**列下的
图标，查看首次远程证明的审计信息。 示例声明内容：

```json
{
    "customized_claims": {
        "init_data": null,
        "runtime_data": null
    },
    "evaluation-reports": [
        {
            "policy-hash":
"f5abdc02716d85a5ab28cf43500201591bbe4e5600751039462e5ec2e0ae2698d637c1f487f58bca182244 fdf3b4b1",
            "policy-id": "default"
        }
```

`],`

```json
    "exp": 1752734041,
    "iat": 1752733741,
    "iss": "CoCo-Attestation-Service",
    "jti": "QZYdPC4lEE",
    "nbf": 1752733741,
    "tcb-status": "
{\"init_data\":\"\",\"report_data\":\"0000000000000000000000000000000000000000000000000 0000000000000\",\"tpm.AA.eventlog.file.measure\":\"/etc/trustiflux/attestation-agent. toml:08979911e7776edda9dedc02e4ca2661c2286fa10c8188cb112eb7713d78d4f1\",\"tpm.kernel_cm ine\":\"grub_kernel_cmdline (hd0,gpt3)/boot/vmlinuz-5.10.134- 012.2.ali5000.pro.al8.x86_64 root=UUID=7f245c64-292b-4504-b070-f56dea9ea4a7 ro rhgb q uiet cgroup.memory=nokmem crashkernel=0M-2G:0M,2G-8G:192M,8G-376G:384M,376G-:448M spe c_rstack_overflow=off vring_force_dma_api kfence.sample_interval=100 kfence.booting_max=0-2G:0,2G-32G:2M,32G-:32M preempt=none vga=791 biosdevname=0 net.i fnames=0 console=tty0 console=ttyS0,115200n8 noibrs nvme_core.io_timeout=4294967295 n vme_core.admin_timeout=4294967295 cryptomgr.notests rcupdate.rcu_cpu_stall_timeout=300 swiotlb=any\\u0000\",\"tpm.measurement.grub.SHA1\":\"94b31eb049948918ce988e0ef1a80521db
****\",\"tpm.measurement.initrd.SHA1\":\"8635ba312053fb3377cd3423a61677642d2b****\",\"t
.measurement.kernel.SHA1\":\"f4f039c92ae8b60c544b96c4ccebf6f00bf9****\",\"tpm.measureme .kernel_cmdline.SHA1\":\"706abfc6e5500a3ff776f67e93dd330c3f6a****\",\"tpm.measurement.s m.SHA1\":\"54377e45046bd7e9d7734a9d693dc3e9e529****\",\"tpm.quote.clock_info\":\"168725 8\",\"tpm.quote.firmware_version\":\"2312323638123443766\",\"tpm.quote.signer\":\"000bc 16eeb5062d10ae88e9f144aab698adf34a47d889f0810aad0e319a0bf****\"}",
    "tee": "tpm"
}
```

6. 单击**参考值管理**页签，将上一步骤示例声明内容tcb-status中的grub、initrd、kernel等软硬件度量值字
段作为参考值填入**参考值管理**作为基线标准值。 您也可以自定义认证策略作为基线标准值。 参考值管理格式如下：

```json
{
    "tpm.measurement.grub.SHA1": [
        "94b31eb049948918ce988e0ef1a80521db3****"
```

`],`

```
    "tpm.measurement.initrd.SHA1": [
        "8635ba312053fb3377cd3423a61677642d2b****"
```

`],`

```
    "tpm.measurement.kernel.SHA1": [
        "f4f039c92ae8b60c544b96c4ccebf6f00bf9****"
```

`],`

```
    "tpm.measurement.kernel_cmdline.SHA1": [
        "706abfc6e5500a3ff776f67e93dd330c3f6a****"
```

`],`

```
    "tpm.measurement.shim.SHA1": [
        "54377e45046bd7e9d7734a9d693dc3e9e529****"
```

]

```
}
```

7. 验证远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

如果被度量的软硬件信息一致，则远程证明成功，**审计日志**页签下**结果**为**成功**。 如果被度量的软硬件发生被篡改或者完整性被破坏，则远程证明出现错误，**审计日志**页签下**结果**为失败。

**文件度量**

1. 使用Workbench工具以SSH协议登录Linux实例，具体操作请参考**《云服务器** **ECS****用户指南》**中的“**使用**
**Workbench****工具以****SSH****协议登录****Linux****实例**”章节。
2. 查看measurement_tool.service状态。

```bash
systemctl status measurement_tool.service
```

预期状态为inactive。
3. 在 `/etc/measurement_tool/config.toml` 文件中添加需要度量的文件。
4. 启动measurement_tool。

```
measurement_tool /etc/measurement_tool/config.toml
```

5. 触发远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

6. 在Trustee实例详情页，单击**审计日志**页签，然后单击**声明**列下的
图标，在声明内容中，即可查看到需要度量的文件。
7. 单击**参考值管理**页签，将上一步骤获取的文件度量填入参考值管理。
参考值管理格式如下：

```json
{
    "tpm.AA.eventlog.file./etc/trustiflux/attestation-agent.toml": [
        "08979911e7776edda9dedc02e4ca2661c2286fa10c8188cb112eb7713d78****"
```

`],`

```
    "tpm.AA.eventlog.file./root/measurement_tool-0.2.0-1.al8.x86_64.rpm": [
        "8079aae02d0685802696a156af767907398acc68496e815e365576f8b027****"
```

`],`

```
    "tpm.AA.eventlog.file./usr/local/bin/attestation-agent": [
        "d07c6de6ca7c36c87fdf7f0a16d482dd0e4349c5a973760f98cfe18a1b50****"
```

]

```
}
```

8. 文件度量。
**未修改文件度量**：直接执行 `attestation-agent-client get-token --token-type coco_as` 触发
远程证明，**审计日志**页签下**结果**为**成功**。
**模拟修改文件度量值**：
a. 修改 `/etc/trustiflux/attestation-agent.toml` 文件度量内容。 b. 启动measurement_tool，重新hash文件到eventlog中。

```
measurement_tool /etc/measurement_tool/config.toml
```

c. 触发远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

参考值不一致导致报错，并且**审计日志**页签下**结果**为**失败**。

### 远程证明在ECS TDX机密实例中的应

**用案例**

本文介绍如何创建TDX机密实例以及在TDX机密实例中验证远程证明。

**前提条件**

已完成机密ECS宿主机（intel TDX）背书凭证上传PCCS，具体操作请参考**《专有云运维平台****操作指**
**南》** > **机密****ECS****宿主机（****intel TDX****）背书凭证上传****PCCS** 。
运维侧已部署intel PCCS服务。

**创建TDX实例**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**Trustee****实例**。
3. 在**Trustee****实例**页面，单击**创建****Trustee**。
4. 在**创建****Trustee**页面，设置相关参数，然后单击**提交**。

| 参数 | 说明 |
|---|---|
| 组织 | 待创建实例归属的组织。 |
| 资源集 | 待创建实例归属的资源集。 |
| 地域 | 待创建实例所属的地域。 |
| 名称 | 自定义Trustee实例的名称。 |
| 描述 | Trustee实例的描述信息。 |
| VPC | 选择Trustee实例要接入的虚拟私有云网络。 |
| VSwitch | 选择Trustee实例具体部署在哪一个子网内。 |

**步骤二：创建TDX实例**

创建机密实例的步骤与创建普通实例类似，但需要注意一些特定选项。本步骤重点介绍机密实例相关的特定配置，如果您想了解其他通用配置，请参见**《云服务器** **ECS****用户指南》**中的“**创建实例**”章节。
1. 登录云服务器ECS控制台。
2. 在左侧导航栏中，选择**实例与镜像** **> ECS****实例**。
3. 在顶部菜单栏处，选择组织、资源集和地域。
4. 单击**创建实例**。
5. 在创建实例页面，配置以下参数：
i. **开启热变配**：否。 ii. **规格**：当前仅支持ecs.g8v-tdx-k10，ecs.g8v-tdx-k25、ecs.s8-tdx-k规格族，您也可以在筛选框输入tdx搜索TDX实例。 iii. **机密虚拟机**：选中**机密虚拟机**。 iv. **镜像**：当前仅支持**阿里云服务器操作系统** **V3 Linux 64**位**安全增强版**镜像。
6. （可选）实例创建完成后，可执行 env | grep TRUSTEE_URL 命令查看远程证明URL是否自动下发成
功，如果回显信息中无法查到TRUSTEE_URL，可执行以下命令让客户端重新获取远程证明URL：

**说明**

```bash
mkdir -p /etc/systemd/system.conf.d/ echo '[Manager]' > /etc/systemd/system.conf.d/99-trustee-env.conf echo 'DefaultEnvironment="TRUSTEE_URL=<<远程证明URL>>"' >> /etc/systemd/system.conf.d/99-trustee-env.conf systemctl set-environment TRUSTEE_URL="<<远程证明URL>>" systemctl restart attestation-agent
```

**远程证明验证**

1. 使用Workbench工具以SSH协议登录Linux实例，具体操作请参考**《云服务器** **ECS****用户指南》**中的“**使用**
**Workbench****工具以****SSH****协议登录****Linux****实例**”章节。
2. 执行测试命令，触发远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

3. 在远程证明控制台左侧导航栏，单击**Trustee****实例**。
4. 在**Trustee****实例**页面，单击机密实例对应Trustee实例操作列的**管理**，进入Trustee实例详情页。
5. 在Trustee实例详情页，单击**审计日志**页签，然后单击**声明**列下的
图标，查看首次远程证明的审计信息。 示例声明内容：

```json
{
    "customized_claims": {
        "init_data": null,
        "runtime_data": null
    },
    "evaluation-reports": [
        {
            "policy-hash":
"f5abdc02716d85a5ab28cf43500201591bbe4e5600751039462e5ec2e0ae2698d637c1f487f58bca182244 fdf3b4b1",
            "policy-id": "default"
        }
```

`],`

```json
    "exp": 1752734041,
    "iat": 1752733741,
    "iss": "CoCo-Attestation-Service",
    "jti": "QZYdPC4lEE",
    "nbf": 1752733741,
    "tcb-status": "
{\"init_data\":\"\",\"report_data\":\"0000000000000000000000000000000000000000000000000 0000000000000\",\"tpm.AA.eventlog.file.measure\":\"/etc/trustiflux/attestation-agent. toml:08979911e7776edda9dedc02e4ca2661c2286fa10c8188cb112eb7713d78d4f1\",\"tpm.kernel_cm ine\":\"grub_kernel_cmdline (hd0,gpt3)/boot/vmlinuz-5.10.134- 012.2.ali5000.pro.al8.x86_64 root=UUID=7f245c64-292b-4504-b070-f56dea9ea4a7 ro rhgb q uiet cgroup.memory=nokmem crashkernel=0M-2G:0M,2G-8G:192M,8G-376G:384M,376G-:448M spe c_rstack_overflow=off vring_force_dma_api kfence.sample_interval=100 kfence.booting_max=0-2G:0,2G-32G:2M,32G-:32M preempt=none vga=791 biosdevname=0 net.i fnames=0 console=tty0 console=ttyS0,115200n8 noibrs nvme_core.io_timeout=4294967295 n vme_core.admin_timeout=4294967295 cryptomgr.notests rcupdate.rcu_cpu_stall_timeout=300 swiotlb=any\\u0000\",\"tpm.measurement.grub.SHA1\":\"94b31eb049948918ce988e0ef1a80521db
****\",\"tpm.measurement.initrd.SHA1\":\"8635ba312053fb3377cd3423a61677642d2b****\",\"t
.measurement.kernel.SHA1\":\"f4f039c92ae8b60c544b96c4ccebf6f00bf9****\",\"tpm.measureme .kernel_cmdline.SHA1\":\"706abfc6e5500a3ff776f67e93dd330c3f6a****\",\"tpm.measurement.s m.SHA1\":\"54377e45046bd7e9d7734a9d693dc3e9e529****\",\"tpm.quote.clock_info\":\"168725 8\",\"tpm.quote.firmware_version\":\"2312323638123443766\",\"tpm.quote.signer\":\"000bc 16eeb5062d10ae88e9f144aab698adf34a47d889f0810aad0e319a0bf****\"}",
    "tee": "tdx"
}
```

6. 单击**参考值管理**页签，将上一步骤示例声明内容tcb-status中的grub、initrd、kernel等软硬件度量值字
段作为参考值填入**参考值管理**作为基线标准值。 您也可以自定义认证策略作为基线标准值。 参考值管理格式如下：

```json
{
    "tdx.measurement.grub.SHA1": [
        "94b31eb049948918ce988e0ef1a80521db3****"
```

`],`

```
    "tdx.measurement.initrd.SHA1": [
        "8635ba312053fb3377cd3423a61677642d2b****"
```

`],`

```
    "tdx.measurement.kernel.SHA1": [
        "f4f039c92ae8b60c544b96c4ccebf6f00bf9****"
```

`],`

```
    "tdx.measurement.kernel_cmdline.SHA1": [
        "706abfc6e5500a3ff776f67e93dd330c3f6a****"
```

`],`

```
    "tdx.measurement.shim.SHA1": [
        "54377e45046bd7e9d7734a9d693dc3e9e529****"
```

]

```
}
```

7. 验证远程证明。

```
attestation-agent-client get-token --token-type coco_as
```

如果被度量的软硬件信息一致，则远程证明成功，**审计日志**页签下**结果**为**成功**。 如果被度量的软硬件发生被篡改或者完整性被破坏，则远程证明出现错误，**审计日志**页签下**结果**为失败。

**已知功能限制**

TDX规格上同时支持创建普通实例和TDX机密实例。 选中**机密虚拟机**：TDX机密实例。 未选中**机密虚拟机**：普通实例。 TDX规格（包含TDX机密实例和普通实例）不支持热迁移/热变配/宕机迁移。 开启TDX特性的ECS的CPU寄存器和内存中的数据会通过CPU硬件进行加密保护，因此其性能相较普通 ECS实例存在一定损失。 大规格TDX机密实例关机较慢：
**小于等于****32 GiB**内存实例规格：若应用全部使用完内存，关机在30s内，可正常关机。然而，在连续
多次关机的情况下，可能会出现关机失败。 大规格实例：若内存使用超过32 GiB，可能会因关机慢问题而导致关机失败。 受限于TDX动态度量值（RTMR）重置/中断保护/寄存器状态恢复等设计，开启了TDX特性的ECS实例不支持内部重启（即在操作系统内部不支持执行reboot命令），但可以通过ECS管理控制台或者调用 RebootInstance重启ECS实例。 暂不支持VNC登录实例，但不影响SSH方式登录，例如可以通过Workbench或第三方客户端登录。 镜像限制： 仅支持UEFI镜像。 暂不支持Windows。 阿里云提供了支持TDX动态度量和远程证明的镜像：**阿里云服务器操作系统** **V3 Linux 64**位**机密增**
**强版**；如您使用其他UEFI镜像，请自行研发支持TDX动态度量及远程证明能力的自定义镜像。
由于Intel EMR平台TME-MK限制，共计支持128个key，即飞天企业版EMR平台上支持128个key，其中，keyID=0保留给TME-bypaas使用，keyID=1给TDX module使用，其余key均给TDVM使用，因此最多可开126个TDVM（机密实例）。 Linux guest kernel SWIOTLB buffer已知问题： 可见内存较常规实例较小，开启了TDX特性的ECS实例内部将使用特定的非加密内存（SWIOTLB）用于外设通信，该内存区域的大小默认情况下为ECS实例可用内存的6%。 大规格插入多张ENI弹性网卡可能导致ECS实例崩溃，原因为网卡多队列情况下SWIOTLB内存可能不足导致内存分配失败，您可以在控制台将对应ECS实例关机并卸载对应弹性网卡以从启动失败中恢复。 如果您的实例负载涉及大量的IO通信，则可能遭遇由SWIOTLB不足导致的性能下降。您可以使用以下命令检查此问题是否存在：

```
dmesg| grep 'swiotlb buffer is full'
```

**重要**

错误配置SWIOTLB参数可能导致您的实例启动失败，建议您在操作前创建磁盘快照，以便在任何错误情况下可以安全回滚。具体操作，请参见**《云服务器** **ECS****用户指南》**中的“**创建快照**”章节。 如您确认该问题存在，您可以尝试调大SWIOTLB大小以改善ECS的性能，具体操作如下： 将SWIOTLB的大小修改为2 GiB。

```
grubby --update-kernel=ALL --args=swiotlb=1048576
```

如果您的内核版本大于 `5.10.134-18.al8.x86_64` ，可以额外增加参数 `any` 以支持使用更大的 SWIOTLB，如：

```
grubby --update-kernel=ALL --args=swiotlb=2097152,any # 将SWIOTLB调整为4 GiB
```

**说明**

SWIOTLB参数取值的计算方法为：目标大小（以MiB为单位）* 512。更多信息，请参见The kernel's command-line parameters。

### 远程证明在ECS CSV机密实例中的应用

**案例**

本文介绍如何创建CSV机密实例以及在CSV机密实例中验证远程证明。

**前提条件**

已完成机密ECS宿主机（海光CSV3）的芯片凭证批量搜集并上传，具体操作请参考**《专有云运维平台**操
**作指南》** > **机密****ECS****宿主机（海光****CSV3****）的芯片凭证批量搜集并上传**。
运维侧已部署intel PCCS服务。

**创建CSV实例**

1. 登录远程证明服务控制台。
2. 在左侧导航栏，单击**Trustee****实例**。
3. 在**Trustee****实例**页面，单击**创建****Trustee**。
4. 在**创建****Trustee**页面，设置相关参数，然后单击**提交**。

| 参数 | 说明 |
|---|---|
| 组织 | 待创建实例归属的组织。 |
| 资源集 | 待创建实例归属的资源集。 |
| 地域 | 待创建实例所属的地域。 |
| 名称 | 自定义Trustee实例的名称。 |
| 描述 | Trustee实例的描述信息。 |
| VPC | 选择Trustee实例要接入的虚拟私有云网络。 |
| VSwitch | 选择Trustee实例具体部署在哪一个子网内。 |

**步骤二：创建CSV实例**

创建CSV 机密实例的步骤与创建普通实例类似，但需要注意一些特定选项。本步骤重点介绍机密实例相关的特定配置，如果您想了解其他通用配置，请参见**《云服务器** **ECS****用户指南》**中的“**创建实例**”章节。
1. 登录云服务器ECS控制台。
2. 在左侧导航栏中，选择**实例与镜像** **> ECS****实例**。
3. 在顶部菜单栏处，选择组织、资源集和地域。
4. 单击**创建实例**。
5. 在创建实例页面，配置以下参数：
i. **开启热变配**：否。 ii. **规格**：当前仅支持ecs.g8v-CSV-k10，ecs.g8v-CSV-k25、ecs.s8-CSV-k规格族，您也可以在筛选框输入CSV搜索CSV实例。 iii. **机密虚拟机**：选中**机密虚拟机**。 iv. **镜像**：当前仅支持**阿里云服务器操作系统** **V3 Linux 64**位**安全增强版**镜像。
6. （可选）实例创建完成后，可执行 systemctl show-environment | grep TRUSTEE_URL 命令查看远程
证明URL是否自动下发成功，如果回显信息中无法查到TRUSTEE_URL，可执行以下命令让客户端重新获取远程证明URL：

**说明**

```bash
mkdir -p /etc/systemd/system.conf.d/ echo '[Manager]' > /etc/systemd/system.conf.d/99-trustee-env.conf echo 'DefaultEnvironment="TRUSTEE_URL=<<远程证明URL>>"' >> /etc/systemd/system.conf.d/99-trustee-env.conf systemctl set-environment TRUSTEE_URL="<<远程证明URL>>" systemctl restart attestation-agent
```

**已知功能限制**

选择CSV3规格必须开启机密虚拟机选项。 CSV3规格不支持热迁移/热变配。 开启CSV特性后ECS的内存数据会通过CPU硬件进行加密保护，因此其性能相较普通ECS实例存在一定损失。 镜像限制： 仅支持UEFI镜像。 暂不支持Windows。 阿里云提供了支持CSV3动态度量和远程证明的镜像：**阿里云服务器操作系统** **V3 Linux 64**位**安全增**
**强版**；如您使用其他UEFI镜像，请自行研发支持CSV3动态度量及远程证明能力的自定义镜像。
暂不支持VNC登录实例，但不影响SSH方式登录，例如可以通过Workbench或第三方客户端登录。 Linux guest kernel SWIOTLB buffer已知问题： 可见内存较常规实例较小，开启了CSV3特性的ECS实例内部将使用特定的非加密内存（SWIOTLB）用于外设通信，该内存区域的大小默认情况下为ECS实例可用内存的6%。 大规格插入多张ENI弹性网卡可能导致ECS实例崩溃，原因为网卡多队列情况下SWIOTLB内存可能不足导致内存分配失败，您可以在控制台将对应ECS实例关机并卸载对应弹性网卡以从启动失败中恢复。 如果您的实例负载涉及大量的IO通信，则可能遭遇由SWIOTLB不足导致的性能下降。您可以使用以下命令检查此问题是否存在：

```
dmesg| grep 'swiotlb buffer is full'
```

**重要**

错误配置SWIOTLB参数可能导致您的实例启动失败，建议您在操作前创建磁盘快照，以便在任何错误情况下可以安全回滚。 如您确认该问题存在，您可以尝试调大SWIOTLB大小以改善ECS的性能，具体操作如下： 将SWIOTLB的大小修改为2 GiB。

```
grubby --update-kernel=ALL --args=swiotlb=1048576
```

如果您的内核版本大于 `5.10.134-18.al8.x86_64` ，可以额外增加参数 `any` 以支持使用更大的 SWIOTLB，如：

```
grubby --update-kernel=ALL --args=swiotlb=2097152,any # 将SWIOTLB调整为4 GiB
```

**说明**

SWIOTLB参数取值的计算方法为：目标大小（以MiB为单位）* 512。更多信息，请参见The kernel's command-line parameters。

### 企业级安全组放通远程证明请求操作方

**法**

在企业级安全组中，如果出方向流量与安全组出方向规则匹配，将按照规则指定的授权策略，允许或拒绝放行。其他任何出方向流量，将会被拒绝访问。默认场景下，远程证明客户端对服务端发起的远程证明的请求会被拦截。

**说明**

普通安全组默认放通出方向流量，无此问题。

**操作步骤**

1. 从问题实例获取远程证明URL，您可通过以下两种方式获取：
方式一：从远程证明服务获取。 c. 在**Trustee****实例**页面，找到需要放通的Trustee实例的**远程证明****URL**列的值。 方式二：从自定义参数获取。 a. 登录云服务器 ECS控制台，在左侧导航栏选择**实例与镜像** **> ECS****实例**。 b. 在**ECS****实例**页面，找到目标实例，单击**操作**列的 ，选择**修改属性**。 c. 在**自定义数据**区域获取URL的值。
2. 放通远程证明URL的IP与端口。
i. 在**ECS****实例**页面，单击ECS实例ID；在**实例详情**页面，单击**安全组**页签。 ii. 在**安全组列表**子页签，单击安全组**操作**列的**配置规则**。 iii. 在**安全组规则**页签，单击**出方向**子页签。 iv. 单击**添加安全组规则**，配置以下参数，然后单击**确定**。
**授权策略**：选择**允许**。
**授权对象**：输入从问题实例获取远程证明URL的IP。
**端口范围**：输入从问题实例获取远程证明URL的端口。
