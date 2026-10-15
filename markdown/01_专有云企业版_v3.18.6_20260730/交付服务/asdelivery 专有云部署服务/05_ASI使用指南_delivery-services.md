---
title: "专有云部署服务 ASI使用指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 49
source_pdf: "05_ASI使用指南_delivery-services.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asdelivery/zh/delivery-services.pdf"
converter: line-classifier (PyMuPDF)
---

# 专有云部署服务 ASI使用指南

## 登录ASI平台

**操作步骤**

1. 登录ASI平台。
i. 打开浏览器（推荐使用Chrome浏览器）。 ii. 在浏览器中配置好浏览器代理后，在地址栏输入ASI的访问地址，然后按下**回车**键，进入ASI平台的鉴权页面。

**说明**

ASI需要通过ops1的管理网卡（一般为eth0）IP地址访问，默认端口为8848，其地址格式为： IP:8848，例如，10.201.*.*:8848。 iii. 输入登录用户名和密码，单击**账号登录**，进入**ASI-****混合云可视化交付变更平台**页面。

**说明**

登录用户名和密码请联系阿里云技术支持通过获取。 在您首次登录ASI平台后，系统会默认保存登录用户名和密码，后续登录时，该界面不会再出现。但是您一旦清理了浏览器缓存，那么再次登录时，仍需要输入登录用户名和密码。
2. 选择部署形态和版本。
i. 在**ASI-****混合云可视化交付变更平台**页面，选择**我要交付** > **单机房交付**。 ii. 在**我要交付**-**单机房交付**页面，单击**企业版**-**融合****PAAS(****适用****v3.14****及以后的版本**)下的版本（例如，v3.16）。

**重要**

专有云形态和版本选定后即进入部署交付页面，形态和版本不可更改，请务必根据实际环境的云形态进行选择。 如果形态和版本选择错误，请先进入当前部署交付页面，然后在右上角选择**系统工具** >
**ASI****系统清理**，清理当前ASI状态等数据。清理完成后，返回导航页面可重新选择专有云形
态和版本。

## 配置首页信息

### 上传ASI数据包

ASI部署完成后，您需要将朱雀终态文件（ASI数据包ASI_DATA.tar.gz）上传到ops1节点，以便部署脚本调用。

**前提条件**

已获取ASI数据包（ `ASI_DATA.tar.gz` ），具体请参见专有云版本部署指南中的下载朱雀终态文件章节。

**背景信息**

| 前ASI数据包（ | ASI DATA.tar.gz _ |  |
|---|---|---|
| producting-planning.json |  |  |
|  |  | ）， |

| 传 | ASI DATA.tar.gz _ |
|---|---|
| tianji imports _ _ |  |

| u disk _ |  |
|---|---|
|  | 目录 |

**操作步骤**

1. 登录ASI平台后，进入**首页**页面。
2. 在**首页**的**请选择终态文件**区域，单击**上传****ASI_DATA**。
3. 在弹出的**上传****ASI_DATA****数据**对话框中，单击**上传文件**。
4. 在弹出的对话框中，选择从朱雀下载的目标ASI数据包（ `ASI_DATA.tar.gz` ），然后单击**打开**即可。

### 配置基础信息

在部署专有云云产品前，需要在ops1机器上配置服务器带外用户名和密码、设置ops1的系统时间并选择交付场景配置模式。

**前提条件**

已从客户或服务器厂商处获取了服务器的带外用户名和密码。

**背景信息**

在开始交付前，您必须完成装机信息配置，并且需要保证配置正确无误。

**重要**

如果发现装机信息配置错误，请在IDC_CHECK前重新配置，否则后续部署会出错。

**操作步骤**

1. 登录ASI平台后，进入**首页**页面。
2. 在**首页**的**基础配置**区域填写装机信息，包括：**带外用户名**、**带外密码**、**OPS1****系统时间**。
交付场景配置说明如下表所示。

| 安装方式 | 说明 | 适用场景 |
|---|---|---|
| 常规安装（手动提交终态） | 该模式下IDC-CHECK会对服务器进行硬件和配置检测；并且在飞天基础运维平台底座和PaaS底座部署完成后需要手动提交终态，之后才会继续部署飞天基础运维平台云产品和 PaaS云产品。 | 企业版敏捷版全量场景 |
| 常规安装（自动提交终态） | 该模式下IDC CHECK会对服务器进 _ 行硬件和配置检测，并且在飞天基础运维平台底座和PaaS底座部署完成后会自动提交终态，不需要人工干预。 | 敏捷版基础场景 |
| 快速安装（装机忽略硬件检查及自动提交终态） | 该模式下IDC CHECK不会对服务器 _ 进行硬件和配置检测，并且在飞天基础运维平台底座和PaaS底座部署完成后会自动提交终态，不需要人工干预。 | 非标服务器场景 |

3. 单击**保存基础配置**。

### 开始交付

您可以在部署交付首页概览项目信息，确认项目信息配置无误后，即可开始交付。

**操作步骤**

1. 在部署交付**首页**，确认**基础配置**信息无误后，单击右下角**开始交付**。
2. 在弹出的**温馨提示**对话框中，确认部署形态、朱雀终态文件、服务器带外用户名和密码、ops1系统时间
和交付模式是否正确。确认相关信息完全无误后，单击**确定**即可开始交付。

**重要**

请确保服务器带外用户名和密码正确，如果错误，服务器会装机失败。如果需要修改，请先与服务器厂商或项目客户确认，然后再通过现场交付工具进行修改。

## 部署准备

### 前提条件及准备流程

在部署底座和云产品前，需要满足一定的前提条件。本文介绍需要满足的具体的前提条件和整体部署准备流程。

**前提条件**

已配置了OPS1的带外用户名和密码、OPS1系统时间及交付场景配置。 安装包拷贝前，请确保存放云产品安装包和HTTPS证书等数据的移动硬盘已挂载到OPS1机器的/mnt目录下。如果挂载点不在/mnt目录下，则需要在页面拷贝配置中进行订正。 网络初始化前，请确保已导入 `_tianji_imports` 终态到/apsarapangu/disk3/u_disk目录。 如果客户要求某些PaaS云产品使用自有资源（VIP和数据库），则已从客户处获取相应的资源信息。

**说明**

当客户要求某些PaaS云产品使用自有资源时，正常情况下在朱雀规划时已进行了相关配置。如果朱雀规划后需要修改或者朱雀规划时未进行相关配置，您均可在此处进行配置。

**准备流程**

在部署交付首页，需要确认项目的基础配置信息都正确。单击下一步进入部署准备环节。进入部署准备环节，您需要根据页面向导进行部署准备相关的操作，包括安装包拷贝、网络初始化、密评配置（仅用于国密密评配置（仅用于国密场景）：加密机IP地址分配，生成双向证书并加载双向证书。 制作https证书：支持生成阿里云自签证书目录。如果客户使用阿里云自签工具签发证书，建议您通过此方式生成。 PaaS产品配置变更：配置部分PaaS云产品的自定义参数，以及自定义PaaS云产品后端使用的资源。

### 安装包拷贝

**背景信息**

安装包拷贝过程中，会先解压再拷贝。拷贝时会将docker image、tianji_ops服务的安装包直接拷贝到指定的目录。安装包拷贝大约需要4小时（具体时间与安装包大小相关），在此期间您可同步进行网络初始化操作。

**说明**

安装包拷贝前，请确保移动硬盘已挂载到ops1机器的/mnt目录下。如果之前已完成安装包拷贝，则可

**操作步骤**

1. 安装包拷贝前检查。
i. 检查移动硬盘是否已挂载到/mnt目录下。 如果挂载的是其他目录，建议您重新挂载到/mnt，您可以通过**更多** > **编辑拷贝配置**修改 `package_dir` 的挂载目录。配置样例如下所示： ii. 检查/mnt目录下的云产品安装包，该安装包需要指定到具体的压缩包文件，如果是文件夹，则需要指定到具体的文件夹。 拷贝开始时，ASI将自动查找并拷贝/mnt下7z格式的压缩包。
2. 完成以上检查后，单击**安装包拷贝**，拷贝安装包到指定目录。

**说明**

3. 安装包拷贝期间或安装包拷贝完成后，单击**下一步**，进入**网络初始化**页面。

### 网络初始化

**背景信息**

网络初始化将在ops1上启动一个netdev_proxy服务（DHCP Server），交换机重置时，会请求下发交换机配置。

**操作步骤**

1. 单击**网络初始化**，开始网络初始化。

**说明**

理想情况下，网络初始化大约需要半小时。如网络初始化持续1小时仍未成功，则检测程序将退出， 请您联系网络架构师检查交换机的连线、配置等是否正确。
2. **可选：**如果网络初始化失败，您可单击**更多** > **抓包工具**进行抓包分析。
3. 网络初始化完成后，单击**安装包拷贝**，查看安装包拷贝是否完成。
4. 确认网络初始化成功并且安装包拷贝完成后，单击**下一步**。
如果系统部署了国密产品，则会进入**密评配置**页面。

### 3.4. （可选）密评配置

如果系统部署了国密产品，则需要进行密评配置相关操作。

**操作步骤**

1. 在**部署准备**页面的**密评配置**阶段，单击**ip&****域名配置**，等待ip&域名配置分配完成。
分配后可正常查看VSM IP和归属HSM IP，如下示例： 该步骤的IP分配规则与产品规划和加密机连线中的IP分配规则一致，请确认分配结果是否与产品规划和加密机连线中的规则一致，如果不一致，则需要调整HSM和VSM IP配置。
2. 单击**签发****vsm****证书**。
3. 单击**批量下载****VSM****证书**，该操作会备份VSM双向认证证书，如果出现步骤5中VSM自动初始化失败时，
可提供该下载包给加密机厂商，由加密机厂商分析并修复初始化失败问题。
4. 手工检查VSM网络连通性。
从ops1 telnet VSM IP的8443端口，正常连接后进入下一步。
5. 单击**VSM****自动初始化**，在弹出的对话框中单击**VSM****初始化**。
等待初始化完成，大约需要5分钟。
6. VSM初始化完成后，单击**VSM****可用性检测**。

**说明**

v3.18.1版本无需执行**生成****tianji****加密配置**，直接进入下一步。 当VSM可用性均为正常时，继续下执行一步。 当存在检测失败的VSM，需联系加密机厂商或提工单到加密服务产品进行排查。

### 制作HTTPS证书

#### HTTPS证书制作流程

专有云环境支持直接使用阿里云ASI工具签发的证书，也支持客户自签或自购证书。本文介绍HTTPS证书的制作流程。 专有云HTTPS证书制作需要依赖ASI工具，制作流程如下图所示。 目前HTTPS证书使用场景说明如下： 客户无自签或自购证书需求直接使用ASI签发的证书。 客户有自签或自购证书需求如果客户有自签或自购证书需求，则ASI签发证书后，您需要提供泛域名列表给客户，以便客户根据列表

#### 阿里云ASI工具签发证书

ASI支持以可视化的操作一键生成证书目录，当前仅支持生成阿里云自签证书目录。如果客户使用阿里云自签工具签发证书，建议您通过此方式生成。

**前提条件**

朱雀规划已完成，并且已获取朱雀终态文件（ASI_DATA.tar.gz）。 ASI部署准备流程，已完成密评配置实例化。 朱雀规划已完成，并且已获取朱雀终态文件（ASI_DATA.tar.gz）。

**背景信息**

在ASI上制作证书时，ASI会自动在OPS1节点的/https_certificate/目录下生成HTTPS证书目录， 即/https_certificate/target/证书签发时间，例如/https_certificate/target/20210421191200。同时 ASI还会拷贝HTTPS证书到/apsarapangu/disk3/certificate4bootstrap目录下，以备云产品部署时后台脚本调用。

**重要**

HTTPS证书目录生成后，您需要下载证书提供给客户，以作为备份。客户使用时可通过以下命令进行解压：

```
openssl des3 -d -k password -salt -in xxx.tar.gz | tar xzf -
```

其中，password需要替换成实际的压缩密码（字母和数字组合），xxx.tar.gz需要替换成实际的压缩包名称。

**操作步骤**

1. 进入证书签发页面。
i. 登录ASI混合云可视化交付平台。 ASI平台需要通过OPS1的管理网卡（一般为eth0）的IP地址访问，默认端口为8848，其地址格式为： IP:8848，例如，10.201.*.*:8848。 ii. 在ASI导航页面，选择**我要交付** > **单机房交付**。 iii. 在**我要交付**-**单机房交付**页面中，选择需要部署的专有云形态和版本（此处选择**企业版** **> v3.16**）。
2. 在**制作****https****证书**配置向导页，单击**签发证书**。
3. 在弹出的**自签证书法律风险提示**对话框中，请客户仔细阅读法律风险提示并签字。

**重要**

在单击**确定**前，请务必保证客户已仔细阅读了法律风险提示，并且同意签字。
4. 客户签字后，单击**确定**，开始签发证书。
证书签发完成后，页面会弹出提示信息。
5. 在弹出的**提示信息**对话框中，单击**确认**，下载签发的HTTPS证书。

**说明**

如果此处单击了取消，则后续可在**HTTPS****证书制作**页面下方，单击**下载证书**。
6. 在弹出的**证书加密**对话框中，设置证书压缩密码。

**重要**

证书会采用DES3进行加密，密码不支持特殊字符，只支持数字和字母。设置密码后，请务必牢记。
7. 密码设置完成后，单击**确定**即可自动下载证书（certs_target.tar.gz）到本地。
结束本次操作后，您可在**签发证书**区域查看HTTPS证书目录，并且可以通过**下载根证书**再次下载证书，示例如下图所示。
8. 证书下载后，提供给客户进行备份保存。
9. 确保证书下载成功且备份后，单击**下一步**，进入**PAAS****产品配置变更**页面。

#### 提供泛域名列表给客户

客户有自签或自购证书需求时，ASI生成证书后，您需要提供泛域名列表给客户，以便客户根据此表自签或自购证书。

**前提条件**

已在ASI上完成证书签发。

**背景信息**

ASI工具签发证书后，在ops1节点上会生成所有产品的泛域名列表，即 `/https_certificate/target/<`证书签发时间`>/tianji/certificate_excel.xls` 文件。

**操作步骤**

1. 登录ops1节点。
2. 进入 `certificate_excel.xls` 文件所在目录。

```
cd /https_certificate/target/<证书签发时间>/tianji/
```

其中， <证书签发时间> 是以ASI生成证书时间命名的文件夹，请根据实际替换。
3. 从ops1节点复制 `certificate_excel.xls` 文件到本地电脑。

```
scp root@<ops1_ip>:./certificate_excel.xls <local_path>
```

其中： `<ops1_ip>` ：实际ops1节点的IP地址。 `<local_path>` ：复制 `certificate_excel.xls` 到本地的路径，自定义即可。
4. 提供 `certificate_excel.xls` 文件给客户。
以上是 `certificate_excel.xls` 文件的一个示例，具体客户项目请以实际为准。ASI签发证书是以服务 （Service）为单位进行签发的，实际客户可以按服务自签或购买证书，也可以按产品进行自签或购买证书。 在 `certificate_excel.xls` 表格中，第一列为产品，第二列为服务，自签或购买证书说明如下： 按服务签发：此情况下，每个服务签发一个证书。客户按表格每行签发一个证书即可。 按产品签发：此情况下，每个产品签发一个证书。客户需要把表格产品名称相同的域名全部合并，然后签发一个证书即可。 例如，本例中 `tianji` 产品有三个服务，合并这三行所有的域名，签发一个证书即可。

**重要**

对于包含多个域名的证书，即使只自签或购买其中的一个域名，也需要重新签发所有域名。例如， `tianji` 产品下的 `paas-seed` 服务。 如果不同服务的域名重复，则只需要自签或购买一个证书即可。例如，本例中 `tianji` 产品下的两个 `tianji` 服务的域名重复，则这两个服务只签发一个证书即可。

#### 客户自签或自购证书

专有云部署时，部分客户存在使用自有CA系统签发证书或自购证书的需求。本文介绍如何协助客户使用自有CA系统签发证书或向权威CA机构购买证书。

**前提条件**

客户已从部署交付人员处获取泛域名列表，即ops1节点上的/https_certificate/target/证书签发时间/tianji/certificate_excel.xls文件。

**背景信息**

如果客户自有CA系统或要求自购证书，则您首先需要通过ASI工具生成证书目录，然后将泛域名列表 （certificate_excel.xls）提供给客户，由客户根据泛域名列表自签证书或购买证书。客户自签或购买证书后，您需要对证书进行验证。

**说明**

向权威CA购买证书需要一定的费用，购买证书前，建议客户先确定开放到公网的产品及泛域名。 证书绑定域名列表不区分阿里云CA和客户CA，要求是目标版本证书绑定域名列表要全面，原则是以现场证书绑定域名为基准，融合目标版本产品声明域名列表，进而形成最终版本证书。 当证书绑定域名列表与当前访问域名不匹配时，客户端会判定为证书异常。浏览器常见异常如下：

```
NET::ERR_CERT_COMMON_NAME_INVALID
```

证书中，域名支持多域名，每个域名安装默认泛化处理，以便减少证书中域名数量。技术上，单张SSL证书可支持500以上个泛域名，但有些客户CA会限制泛域名字节长度，例如单张证书仅支持长度为800字符以下的泛域名列表。

| ：绑定 | *.aliyun.com |  |
|---|---|---|
| p2.p1.aliyun.com |  |  |
|  |  | 。 |

| p1.aliyun.com |  | ，但 |
|---|---|---|
| 加 |  |  |

**客户自签和自购证书**

专有云环境对证书格式具有严格的要求，具体请参见证书格式要求。客户自签或购买证书有以下两种方式： 提供ASI工具生成的泛域名列表certificate_excel.xls给客户，由客户根据文件中的泛域名到自有CA系统中签发证书，或向权威CA机构购买证书。此方式下，客户需要签发一套PEM（公钥）和KEY（私钥）证书。 根据自签证书私钥导出证书请求文件，然后提供证书请求文件及certificate_excel.xls文件给客户 （/https_certificate/target/证书签发时间/tianji/certificate_excel.xls），以便其签发新PEM证书。 此方式下，客户只需要签发PEM证书（公钥），然后配合阿里自签的KEY证书（私钥）一起使用。证书请求文件的导出命令如下： `openssl req -new -key <`阿里自签私钥名称`>.key -out request.csr`

**证书格式要求**

专有云环境只支持PEM格式的HTTPS证书。 Root CA 证书格式必须符合如下要求：

```
以 -----BEGIN CERTIFICATE----- 开头，以 -----END CERTIFICATE----- 结尾。
```

每行64个字符，最后一行长度可以不足64个字符。 证书内容不能包含空格。 中级机构颁发的证书证书链格式必须符合如下要求： 服务器证书放第一位，中级证书放第二位，中间不能有空行。 证书内容不能包含空格。 证书之间不能有空行，并且每行64字节。更多信息，请参见RFC1421。 符合证书的格式要求。一般情况下，中级机构在颁发证书时会有对应说明，证书要符合证书机构的格式要求。 中级机构颁发的证书链示例如下：

```
-----BEGIN CERTIFICATE-----
```

`***`服务器证书`***`

```
-----END CERTIFICATE----- -----BEGIN CERTIFICATE-----
```

`***`中间证书`***`

```
-----END CERTIFICATE----- -----BEGIN CERTIFICATE-----
```

`***`根证书`***`

```
-----END CERTIFICATE-----
```

服务器证书公钥当前公钥支持RSA 2048算法，文件名以.pem结尾，包含完整的证书链。公钥内容示例如下： `-----BEGIN CERTIFICATE-----`服务器证书公钥内容

```
MIID5DCCAkygAwIBAgISUJxFpsAciWjROsFDtitgFe9EMA0GCSqGSIb3DQEBCwUA ... NykGHEMiTh1Boul+Ra2PLLfZZb59SqTf9K/L6Q+QJbSErp/UrsMJiQ== -----END CERTIFICATE-----
```

`-----BEGIN CERTIFICATE-----`中间证书公钥内容

```
MIIEkzCCAnugAwIBAgITAMF7E51oKSFCQToaNQAx8Wx/YDANBgkqhkiG9w0BAQsF ... HkPGQtDUNQ72CYk7vTKwbatzz0ADr+o= -----END CERTIFICATE-----
```

`-----BEGIN CERTIFICATE-----` 根证书公钥内容

```
MIIFDzCCAvegAwIBAgISJaUSWQlD/nIlU2XxAzwQ+ZGvMA0GCSqGSIb3DQEBCwUA ... n8Uf -----END CERTIFICATE-----
```

服务器私钥私钥是加密的，内容以 `-----BEGIN PRIVATE KEY-----` 开头，以 `-----END PRIVATE KEY-----` 结尾，文件名以.pem结尾。私钥内容示例如下：

```
-----BEGIN PRIVATE KEY----- MIIG/wIBADANBgkqhkiG9w0BAQEFAASCBukwggblAgEAAoIBgQC8vS1a3jCQobqa ... VcPSWt+KE1GOFavNfblyp49gHg== -----END PRIVATE KEY-----
```

#### 上传和验证客户证书

客户自签或自购证书后，您需要上传这些证书到ops1的相应目录下，替换原ASI签发的对应产品的证书，然后还需要验证客户证书是否符合要求。

**前提条件**

已获取客户自签或自购的证书。 已获取babaSSL工具安装包（issue-cert-tool-20200408.tar.gz）。

**背景信息**

ASI签发证书是按服务进行签发的，实际客户自签或购买时，可按服务进行签发也可按产品进行签发，并且对于域名重复的服务，只需要签发一份证书即可。无论客户以哪种方式签发证书，您在上传客户证书时都必须按照ASI生成的原始证书目录上传，具体说明如下： 按产品签发：客户按产品签发证书时，如果产品下有多个服务，则每个服务均需要复制出一份证书，证书名称和存储目录需要与原ASI签发的相同。 按服务签发：客户按服务签发证书时，证书签发单位与ASI相同，直接上传证书到相应产品目录下即可。 证书存储位置： `/https_certificate/target/<`证书签发时间`>/tianji/certificate4bootstrap/<`产品名称`>/<`服务名称`>/<`证书文件>

**重要**

如果不同服务的域名重复，并且客户只签发了一个证书，则每个服务均需要复制出一份证书，证书名称和存储目录需要与原ASI签发的相同。

**操作步骤**

1. 登录ops1节点。
2. 安装babaSSL。
i. 解压 `issue-cert-tool-20200408.tar.gz` 工具包。 从解压的 `./cert/ext/certificates/issue-cert-tool` 目录下获取babaSSL的安装包。babaSSL 安装包包含以下三个版本： babassl-8.0.3-1874062.alios5.x86_64.rpm babassl-8.0.3-1874062.alios6.x86_64.rpm babassl-8.0.3-1874062.alios7.x86_64.rpm

**说明**

其中，安装包名称中的alios*是指适用的AliOS操作系统版本，现场安装时需要根据实际选择安装包。 ii. 执行以下命令安装babaSSL。

```bash
sudo rpm -ivh babassl-8.0.3-1874062.alios5.x86_64.rpm
```

| 中，命令中的 | alios5 | 为当前机器的操 |
|---|---|---|
| /usr/local/babassl/bin/openssl |  |  |

3. 备份ASI生成的证书。
ASI生成的证书所在目录： `/https_certificate/target/<`证书签发时间 `>/tianji/certificate4bootstrap/<`产品名称`>/<`服务名称`>/<`证书文件>
4. 对于客户提供证书的产品，删除ASI生成的证书。
5. 上传客户证书。
i. 按照ASI生成的证书名称，重命名客户证书文件。 ii. 通过FTP工具或执行以下命令，上传客户证书目录到ops1。

```
scp <local_file> root@<ops1_ip>:/https_certificate/target/<证书签发时间
```

`>/tianji/certificate4bootstrap/<`产品名称`>/<`服务名称>
6. 验证客户证书。
执行以命查询书域名然后中的域名进行对 i. 执行以下命令，查询证书域名，然后与 `certificate_excel.xls` 中的域名进行对比。

```
dns=`/usr/local/babassl/bin/openssl x509 -in <pub_full_name> -noout -text |grep DNS
```

:` 其中， `<pub_full_name>` 为公钥证书名称。返回结果需要与 `certificate_excel.xls` 中相应产品的域名一致。如果域名不一致，则说明客户证书有问题，请与客户沟通。 ii. 执行以下命令，检验证书公私钥是否匹配。
# 输出证书的公钥信息

```
/usr/local/babassl/bin/openssl x509 -pubkey -noout -in <pub_full_name> > pub_cert.t
```

`mp` 其中， `<pub_full_name>` 为公钥证书名称。
# 提取私钥中的公钥信息

```
/usr/local/babassl/bin/openssl <enc_type> -pubout -in <pri_full_name> > pri_cert.tm
```

p 其中， `<enc_type>` 为证书使用的算法类型，支持国际算法证书（RSA）和国密算法证书（EC）两种； `<pri_full_name>` 为私钥证书名称。证书算法类型的确认方法：打开证书私钥文件，开头有 RSA字样的为RSA，无RSA字样的为EC。
#比对以上两个文件中的公钥信息是否一致

```
diff -eq pub_cert.tmp pri_cert.tmp
```

命令 `diff` 返回结果为0，表示两个文件中的公钥信息一致（即证书公私钥匹配）；否则表示证书公私钥不匹配。 如果证书公私钥不匹配，则说明客户证书有问题，请与客户沟通。
7. 验证下一个证书，直到所有客户证书均验证完毕。

#### 验证客户自签或自购证书

客户存在自签或自购证书后，您需要验证客户提供的证书是否符合要求。本文介绍客户如何验证客户的证书。

**前提条件**

已获取客户自签或自购的证书。 已获取证书验证工具包（issue-cert-tool-20200408.tar.gz）。

**背景信息**

客户自签证书后，您需要通过证书验证工具来检验公钥和私钥是否匹配，以及泛域名是否完整。HTTPS证书验证依赖环境上的openssl，社区版或OS自带的openssl版本不支持国密证书验证，所以在验证证书前您需要单独安装支持国密证书验证的openssl版本，即阿里版本babassl。 证书验证支持单一公私钥验证，也支持批量公私钥验证。批量公私钥验证的规则说明如下： 证书目录要求符合目录整体规则，即IEA目录为国际证书，SM目录为国密证书。 IEA和SM证书目录下的证书公私钥命名规则需要符合要求，公私钥命名保持一致，详细规则说明如下： 国际证书公钥后缀为PEM，私钥后缀为KEY。 国密证书签名证书公钥后缀为SIGN.PEM，私钥后缀为SIGN.KEY。 国密证书加密证书公钥后缀为ENC.PEM，私钥后缀为ENC.KEY。 客户购买或自签证书也可放置在对应目录下，但命名规则必须符合以上要求。 本功能只校验最终用户证书，不校验根证书和中间证书。

**操作步骤**

1. 安装babassl。
证书工具包解压后，您可从./cert/ext/certificates/issue-cert-tool目录下可获取babassl的rpm包。 babassl的安装方法如下：

```bash
sudo rpm -ivh babassl-8.0.3-1874062.alios5.x86_64.rpm
```

命令中的alios5可设置为alios5、alios6或alios7，根据实际情况选择即可。安装目录为/usr/local/babassl/bin/openssl。
2. 进入证书验证工具所在目录。
证书工具包解压后，证书验证工具所在目录为./cert/ext/certificates/issue-cert-tool。
3. 验证证书的公私钥。
证书公私钥验证支持单一公私钥验证，也支持批量公私钥验证，具体操作方法分别如下： 单一公私钥验证验证脚本及参数说明如下：

```xml
$sh check_cert.sh -h Usage: sh check_cert.sh [-e <certificate_enc_algorithm>] [-b <public_key>] [-i <private_key>] [-s <san_domains>] [-h <help>] Options:
  -e                    [required] Certificate encryption
algorithm.Options(rsa|ec).rsa: International Encryption Algorithm、 ec: Commercial Encryption Algorithm.
  -b                    [required] Path of public key.
  -i                    [required] Path of private key
  -s                    [required] Path of san_domains.
```

验证正常和异常的示例如下：
# --- 正常输出 `---`

```
$sh check_cert.sh -e rsa -b https_proxy.pem -i https_proxy_key.pem -s 17e_san_domains writing RSA key public key is match private key. certificates are OK $sh check_cert.sh -e ec -b sm_https_proxy_enc.pem -i sm_https_proxy_enc_key.pem -s 17e_san_domains read EC key writing EC key public key is match private key. certificates are OK
```

# --- 异常输出 `---`

```
$sh check_cert.sh -e ec -b https_proxy.pem -i https_proxy_key.pem -s 17e_san_domains read EC key unable to load Key 0:error:0608308E:digital envelope routines:EVP_PKEY_get0_EC_KEY:expecting a ec key: crypto/evp/p_lib.c:528: [ERROR]public key is not match private key. $sh check_cert.sh -e rsa -b IEA/CN___******_test_20200402210627.pem -i IEA/CN___******_test_20200402210627.key -s 17e_san_domains writing RSA key public key is match private key. [ERROR] domain: [ *.aegis.cn-***-env***-***.inter.env***.com ] not in certificate. please generate certificates again. $sh check_cert.sh -e rsa -b SM/SM_CN___******_test_20200402210629.enc.pem -i SM/SM_ CN___******_test_20200402210629.enc.key -s 17e_san_domains 0:error:0607907F:digital envelope routines:EVP_PKEY_get0_RSA:expecting an rsa key:c rypto/evp/p_lib.c:469: [ERROR]public key is not match private key.
```

批量公私钥验证批量公私钥验证脚本及参数说明如下：

```
$python check_cert.py --help usage: check_cert.py [-h] -i cert_directory -s san_domains
```

`https`证书校验工具

```
optional arguments:
  -h, --help         show this help message and exit
  -i cert_directory  [required]
```

证书文件存放目录，证书目录及命名规则：
1. `为国密证目录
2.
3. 结尾

```
  -s san_domains     [required] san_domains文件路径
```

批量公私钥验证的证书目录示例：

```
$tree 17E 17E ├── IEA │ ├── CN___inter_env17e_***_20200303170029.key │ ├── CN___inter_env17e_***_20200303170029.pem │ ├── encrypted_CN___inter_env17e_***_20200303170029.key │ ├── intermediate.key │ ├── intermediate.pem │ ├── root.key │ └── root.pem └── SM
    ├── encrypted_SM_CN___inter_env17e_***_20200303170030.enc.key
    ├── encrypted_SM_CN___inter_env17e_***_20200303170030.sign.key
    ├── SM_CN___inter_env17e_***_20200303170030.enc.key
    ├── SM_CN___inter_env17e_***_20200303170030.enc.pem
    ├── SM_CN___inter_env17e_***_20200303170030.sign.key
    ├── SM_CN___inter_env17e_***_20200303170030.sign.pem
    ├── SM_intermediate.key
    ├── SM_intermediate.pem
    ├── SM_root.key
    └── SM_root.pem
```

批量公私钥验证示例：

```
python check_cert.py -i /https_cert/https-proxy/17E -s /https_cert/httpsproxy/17e_san_domains
```

# demo 输出

```
$python test.py -i /home/zi***/https_cert/https-proxy/17E -s /home/zi***/https_cert/https-proxy/17e_san_domains
```

`---------`开始扫描 `IEA https`证书`---------`

```
sh check_cert.sh -e rsa -b /home/zi***/https_cert/httpsproxy/17E/IEA/CN___inter_env17e_***_20200303170029.pem -i /home/zi***/https_cert/https-proxy/17E/IEA/CN___inter_env17e_***_20200303170029.key -s /home/zi***/https_cert/https-proxy/17e_san_domains writing RSA key public key is match private key. wildcard domain check success. certificatesareOK
```

```
certificates are OK sh check_cert.sh -e rsa -b /home/zi***/https_cert/httpsproxy/17E/IEA/encrypted_CN___inter_env17e_***_20200303170029.pem -i /home/zi***/https_cert/httpsproxy/17E/IEA/encrypted_CN___inter_env17e_***_20200303170029.key -s /home/zi***/https_cert/https-proxy/17e_san_domains the public key /home/zi***/https_cert/httpsproxy/17E/IEA/encrypted_CN___inter_env17e_***_20200303170029.pem not exist! sh check_cert.sh -e rsa -b /home/zi***/https_cert/httpsproxy/17E/IEA/CN___inter_env17e_***_20200303170029.pem -i /home/zi***/https_cert/https-proxy/17E/IEA/CN___inter_env17e_***_20200303170029.key -s /home/zi***/https_cert/https-proxy/17e_san_domains writing RSA key public key is match private key. wildcard domain check success. certificates are OK
```

`---------`扫描 `IEA https`证书完成`---------` `---------`开始扫描 `SM https`证书`---------`

```
sh check_cert.sh -e ec -b /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.sign.pem -i /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.sign.key -s /home/zi***/https_cert/https-proxy/17e_san_domains read EC key writing EC key public key is match private key. wildcard domain check success. certificates are OK sh check_cert.sh -e ec -b /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.enc.pem -i /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.enc.key -s /home/zi***/https_cert/https-proxy/17e_san_domains read EC key writing EC key public key is match private key. wildcard domain check success. certificates are OK sh check_cert.sh -e ec -b /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.sign.pem -i /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.sign.key -s /home/zi***/https_cert/https-proxy/17e_san_domains read EC key writing EC key public key is match private key. wildcard domain check success. certificates are OK sh checkcert.sh -e ec -b /home/zi***/httpscert/https-
```

_ p_ p

```
proxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.sign.pem -i /home/zi
***/https_cert/https-
proxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.sign.key -s /home/zi
***/https_cert/https-proxy/17e_san_domains
the public key /home/zi***/https_cert/httpsproxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.sign.pem not exist! sh check_cert.sh -e ec -b /home/zi***/https_cert/httpsproxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.enc.pem -i /home/zi*
**/https_cert/https-
proxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.enc.key -s /home/zi*
**/https_cert/https-proxy/17e_san_domains
the public key /home/zi***/https_cert/httpsproxy/17E/SM/encrypted_SM_CN___inter_env17e_***_20200303170030.enc.pem not exist! sh check_cert.sh -e ec -b /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.enc.pem -i /home/zi***/https_cert/httpsproxy/17E/SM/SM_CN___inter_env17e_***_20200303170030.enc.key -s /home/zi***/https_cert/https-proxy/17e_san_domains read EC key writing EC key public key is match private key. wildcard domain check success. certificates are OK
```

`---------`扫描 `SM https`证书完成`---------`

### PaaS产品配置变更

**操作步骤**

1. 在左侧导航树中选择产品集群，然后在右侧选择Chart。

**说明**

如果云产品无自定义参数，并且不需要自定义后端资源，则可直接单击右上方的**保存**，然后再单击左上方的**保存配置到终态**。
2. 配置PaaS云产品自定义参数（部署产品包含DLA时需要此配置）。
i. 在**自定义配置**页面，根据现场实际情况配置选定Chart的自定义参数。

**说明**

当前支持自定义参数的PaaS云产品包含DLA，请根据页面提示填写相应的参数。如果不支持自定义参数，则页面会提示无自定义配置。 ii. 完成上述参数配置后，单击右上方的**保存**。
3. 自定义云产品后端资源（客户要求使用自有资源时需要此配置）。
i. 在**资源规划**页面，单击相应资源**操作**列的**规划**。 云产品后端资源包括VIP（**vip**）和数据库（**db**）两种类型，通常只有数据库。 ii. 在弹出的**规划****db**或者**规划****vip**对话框中，**资源后端****(Provider)**设置为**external**，然后根据客户提供信息填写各参数。 图 1. 数据库资源示例图 2. VIP资源示例 iii. 完成上述参数配置后，单击**确认**。 iv. 单击右上方的**保存**。
4. 完成所有云产品的自定义配置后，单击左上方的**保存配置到终态**。
5. 在弹出的**信息提示**对话框中，单击**确认**。
6. PaaS云产品配置变更完成后，单击**下一步**。
7. 单击**全量部署**，进入部署实施阶段。

### 部署准备总结

部署准备阶段的所有步骤完成后，部署准备总结页面向您展示了整个部署准备阶段的整体状态以及对应的详情。

**操作步骤**

1. 部署准备阶段的所有步骤完成后，单击**下一步**，进入总结展示页面。
2. 单击对应阶段，即可查看每个阶段的详情。
3. 确认部署准备工作全部完成后，单击右下角的**全量部署**，进入部署实施阶段。

## 全量部署

### 启动部署

完成部署准备后，即可启动部署专有云环境。启动部署阶段包含9个步骤，ASI会自动部署底座和云产品到终态（自动提交终态安装方式）。本文介绍如何启动部署，以及整个部署过程中您需要重点关注的操作。

**前提条件**

部署准备已完成。

**背景信息**

启动部署包含9个步骤，各步骤间无严格的顺序关系，ASI会自动检查各服务的依赖关系，然后按合理的顺序自动进行部署，无依赖关系的步骤可并行运行。

### 启动部署

1. 在**全量部署**页面，单击**启动部署**，ASI开始自动部署专有云环境，主要包含下图中的9个步骤。
部署过程中您需要关注的事项及说明如下： 查看底座部署进度和状态部署过程中，您需要时刻关注各步骤的部署进度和状态，请参见查看部署进度。 提交云产品终态如果在开始交付时选择了手动提交终态的安装方式，您需要手动提交云产品终态，以启动云产品部署， 具体请参见提交云产品终态。 查看云产品部署进度和状态提交云产品终态后，您可在部署大盘中查看云产品的部署进度和状态，具体请参见查看部署大盘。 镜像预下载 IDC检查及装机步骤耗时较长，当Docker_host装机完成时，可以利用这个时间差，提前将产品部署的镜像下载到Docker_host机器，这样产品部署时可以节省镜像下载的时间。具体请参见镜像预下载。 处理失败步骤如果有部署失败的步骤，您需要及时处理，以免阻塞部署流程，具体请参见处理失败步骤。
2. 等待上面的9个部署步骤均完成，单击**下一步**，进入**产品部署状态**页面。

**查看部署进度**

部署需要很长时间，您需要时刻关注部署进度。**云产品部署**页面按不同粒度为您展示底座的部署进度。
1. 查看部署总体进度和单个步骤进度。
区域①：按照9个步骤整体统计当前部署进度。 区域②：统计单个步骤的部署进度。
2. 查看步骤下子步骤的部署进度。
单击某个步骤**操作**列的**步骤详情**，查看该步骤下各子步骤的部署进度。
3. 查看装机进度（仅适用于步骤2：IDC检查及装机）。
i. 在**IDC****检查及装机**步骤的**操作**列，单击**查看装机进度**。 ii. 在装机进度页面，查看各机器的装机进度和状态。 iii. 如果存在装机失败的机器，按以下方法进行处理。 a. 登录iHardware平台定位和处理故障，具体请参见登录iHardware。 b. 故障处理完成后，返回ASI的装机进度页面，单击相应机器**操作**列的**重新****clone**。

**提交云产品终态**

开始交付时，如果选择了手动提交终态的安装方式，在天基底座和PaaS底座部署完成后（步骤8的Ark服务部署到达终态），您需要手动提交云产品终态，以继续部署本次规划的天基云产品和PaaS云产品。

**操作步骤**

1. 在**启动部署**阶段，单击**提交云产品终态**。
2. 在弹出的**提交云产品终态**对话框中，单击**操作**列的**执行**。

**说明**

部署天基基础服务阶段未完成之前，提交天基侧云产品终态启动部署**操作**列的**执行**置灰。 PaaS底座部署未完成之前（Ark服务到达终态），提交paas侧云产品终态**操作**列的**执行**置灰。
3. 在提示云产品终态提交成功后，单击**确认**。

**查看部署大盘**

部署大盘在TianJi和K8s部署到终态后可使用，它从产品、集群、服务、服务角色四个维度展示了当前云产品的部署详情。
1. 在**启动部署**阶段，单击右侧的**更多**＞**查看部署大盘**。
2. 查看部署到达终态率。
在**部署大盘**页面上方，ASI统计出了本次部署的产品、集群、服务、服务角色总数量，以及当前到达终态的数量。
3. 查看集群部署状态。
在**产品状态**页签，查看集群的当前部署状态。如果需要查看服务、服务角色粒度的部署状态，单击**详情**列的**查看**。 绿色图标表示到达终态，蓝色图标表示部署中，红色图标表示部署失败。如果部署出错或阻塞，则选中相应服务或服务角色，在右侧查看诊断信息，然后根据修复建议进行处理。
4. 查看全局诊断。
单击**全局诊断**页签，查看本次部署的失败类型和对象。 全局诊断自动归类了本次部署过程中的的失败类型和对象，并提供了处理方案。当全局诊断中存在失败信息时，请按处理方案提示进行处理。
5. 跳转到Apsara Uni-manager运维控制台（原ASO）或Apsara Uni-manager运营控制台（原ASCM）
平台。 单击**部署大盘**右上方的**ASO**或**ASCM**的链接，跳转到相应平台的登录页面。 部署大盘支持跳转到专有云环境常用的运维和运营平台，包括飞天基础运维平台、Apsara Unimanager运维控制台（原ASO）、Apsara Uni-manager运营控制台（原ASCM）、PaaS运维控制台、 PaaS巡检平台。
6. 返回全部部署。
部署大盘查看完成后，单击右下角的**返回**。

**镜像预下载**

IDC检查及装机步骤耗时较长，当Docker_host装机完成时，可以利用这个时间差，提前将产品部署的镜像下载到Docker_host机器，这样产品部署时可以节省镜像下载的时间。

**重要**

**镜像预下载**功能只能在Docker_host机器装机完成后使用。如果Docker_host机器没有装机完成，单
击**镜像预下载**，系统会提示**暂时不能进行镜像预下载，请等待管控宿主机装机完成，并且机器上面的**
**tianji-dockerdaemon****服务到达终态**。
1. 在**全量部署**页面，单击**启动部署**阶段右侧的**更多**＞**镜像预下载**。
2. 如果装机完成，单击**下载**，则开始下载镜像。
下载过程中，您可以单击**查看下载状态**，查看当前下载进度。

**处理失败步骤**

在部署过程中，如果出现部署失败的步骤，您需要及时处理，以免阻塞部署流程。当前ASI支持以下故障定位手段： 通过iHardware平台定位故障。 如果IDC-CHECK或iClone装机失败，请登录iHardware平台定位和处理故障，具体请参见登录 iHardware。 通过诊断功能定位故障。 i. 步骤失败或者卡在某一进度时，单击步骤后的**诊断**。

**说明**

诊断功能只在运行中或失败的步骤中可执行，成功的步骤中不可操作。 ii. 在弹出的诊断对话框中，查看错误信息及修改建议。 通过子步骤错误信息定位故障。 i. 单击失败步骤**操作**列的**步骤详情**。 ii. 在步骤详情页面，单击失败子步骤**错误信息**列的**查看详情**。 iii. 在弹出的**状态详情**对话框中，查看当前子步骤的状态信息。 通过日志定位故障。 i. 单击失败步骤**操作**列的**查看日志**。

**重要**

如果某个步骤的查看日志不可操作，则说明该步骤无日志。 ii. 在查看日志对话框中，查看具体的失败日志，定位失败原因。 进入日志页面时，ASI会自动定位到当前步骤的日志位置。 iii. 如果需要下载日志，单击**下载完整****Log**即可。 通过产品状态列表定位故障。 i. 在**部署大盘**的**产品状态**列表中，单击部署失败的产品集群**详情**列的**查看**。 ii. 在该集群的部署诊断页面，选中部署失败的服务角色，在右侧查看失败原因和修复建议。 通过全局诊断信息定位故障。 i. 在**部署大盘**页面中，单击**全局诊断**页签。 ii. 在**全局诊断**页面，查看本次部署的失败对象、失败原因以及处理方案等信息。

**常见问题**

云产品部署完成，需要打通飞天基础运维平台集群的panguTools到pangu_master/pangu_chunkserver 的admin免密。 盘古集群能正常巡检的前提是panguTools节点到panguChunkserver/panguMaster的admin用户免密打通，如果免密未打通，则需要进行以下操作：
1. 登录ag（即PanguTools），admin用户查看/home/admin/.ssh/下文件。
查询结果显示：ag admin用户下没有id_rsa.pub，但是有私钥id_rsa。此时，可以使用当前的私钥生成公钥。
2. 执行如下命令生成公钥。

```
ssh-keygen -y -f id_rsa > id_rsa.pub
```

执行结果： 执行结果显示：ag到chunkserver机器不能免密，但是ops到各个机器是通的，我们先将生成好的公钥拷贝至ops1 tmp下，然后再从ops1上下发到机器（如果没有免密机器较多的话，这里可以使用pscp下发，如果是单台可直接操作追加）。
3. 将ag的公钥追加到机器上的 `authorized_keys` 中。
首先使用以下命令备份当前chunkserver的 `authorized_keys` 。

```
cp /home/admin/.ssh/authorized_keys /home/admin/.ssh/authorized_keys_bak
```

再执行以下命令验证ag到chunkserver是否免密。

```
cat /tmp/id_rsa.pub >> /home/admin/.ssh/authorized_keys
```

如果免密的话，会显示VM之间直接连接成功。如下图所示：

### 产品部署状态

**前提条件**

启动部署已完成。

**操作步骤**

1. **启动部署**阶段完成后，单击右下角**下一步**，进入**产品部署状态**阶段。
2. 查看部署到达终态率。
在页面上方，ASI统计出了本次部署的产品、集群、服务、服务角色总数量，以及当前到达终态的数量。
3. 查看集群部署状态。
在**产品状态**页签，查看集群的当前部署状态。如果需要查看服务、服务角色粒度的部署状态，单击**详情**列的**查看**。 绿色图标表示到达终态，蓝色图标表示部署中，红色图标表示部署失败。如果部署出错或阻塞，则选中相应服务或服务角色，在右侧查看诊断信息，然后根据修复建议进行处理。
4. 查看全局诊断。
单击**全局诊断**页签，查看本次部署的失败类型和对象。 全局诊断自动归类了本次部署过程中的失败类型和对象，并提供了处理方案。当全局诊断中存在失败信息时，请按处理方案提示进行处理。
5. 常用链接跳转。
该页面支持跳转到专有云环境常用的运维和运营平台，包括飞天基础运维平台、PaaS运维控制台、 Apsara Uni-manager运维控制台（原ASO）、Apsara Uni-manager运营控制台（原ASCM）平台和 PaaS巡检平台。
6. 待产品部署状态到达终态后，单击右下角**下一步**，进入**部署后处理**页面。

### 导入license

**操作步骤**

1. 进入**全量部署**页面的**导入****license**阶段。
2. 单击左侧**导入****license**，选择并上传目标license文件。
上传成功并导入完成后，**导入****license**按钮后会有绿色字体提示**license****数据已上传，导入****license**授
**权配置成功**；导入成功后，您可以通过下文的**授权验证**进行相关信息确认。
3. 确认文件上传无误后，单击**下一步**。

**授权验证**

License导入成功后，您可以通过如下步骤进行授权核验。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏，单击**系统配置**。
3. 在左侧导航栏，选择**授权信息**。

**说明**

授权信息页面的相关内容，在授权导入生效后会立即更新。
**授权信息**页面，包含**授权详情**、**授权规格详情**和**授权规格信息统计**三个页签。
**授权详情**页签展示了授权的基本信息，例如授权类型是试用授权还是正式授权、授权生成时间和云实例
ID等。
**授权规格详情**页签展示了客户合同配置中已购买的软件授权信息，按区域、机房进行展示。
**授权规格信息统计**页签展示了授权信息的相关统计。

### 部署后处理

产品部署状态到达终态后会进入部署后处理阶段，该阶段系统会进行tianji服务模板重定向和检查部署流程是否完成。

**前提条件**

**操作步骤**

1. 产品部署状态到达终态后，单击右下角**下一步**，进入**部署后处理**阶段。
2. 单击右上角**开始执行**，系统会进行tianji服务模板重定向和检查部署流程是否完成。
待检查完成后，可通过**执行结果**列直观查看检查结果。如果需要清理之前的执行状态，可单击**清理执行状** 态。
3. 单击**日志**列的**查看**，可查看日志详情。
4. 如果执行结果显示**失败**，可单击**操作**列的**重试**，进行再次尝试。
5. 待**执行结果**均显示**完成**后，单击右下角**下一步**，进入**部署总结**页面。

### 部署总结

**前提条件**

**操作步骤**

1. 在**部署总结**页面，查看部署概括信息以及部署时间统计信息。
2. 单击**导出**，以YML格式的文件保存部署时间统计信息到本地。
3. 确认所有产品、集群、服务、服务角色均到达终态后，单击**完成**，完成本次部署。

## 附录

### 产品规划和加密机连线

本文介绍朱雀规划中涉及的加密机配置和查询方法，以及加密机硬件的网络连线规则。

**版本包要求**

增量规划国密产品时，必须确保使用的system包中包含baseserviceall、webappall产品，以便部署阶段读取baseserviceall、webappall基线配置，生成国密证书，实际不会重新部署baseserviceall、 webappall。可使用全量包或创建一个包含baseserviceall、webappall和国密相关产品的小版本进行增量规划，如下为使用小版本增量规划国密产品的示例： system ID包含baseserviceall、webappall的示例：

**产品规划**

在朱雀规划阶段，需要包含如下产品。朱雀规划完成后，可在朱雀规划中查询加密机的机架位和IP地址规划信息。

**重要**

同一机房内两台加密机应分布在不同组的ASW下，服务器自动上架后若不满足ASW分散需求，应手工调整。

| 云产品 | 产品-英文简称 | 售卖规格 | 交付组件包 |
|---|---|---|---|
| 加密服务-管控软件 | hsm | 密钥管理服务底座版（虚拟机部署） | HsmIdcService |
| 加密服务托管密码机 | hsm | 底座版配套密码机 | HsmIdcresourceService |
| 密钥管理服务 | kms | 密钥管理服务底座版（虚拟机部署） | KmsIdcVirtualService |
| 云盾-IDAAS | idaas | IDP Standard统一身份认证平台专有云版 | idaas |

如下示意图为朱雀产品信息的样例： IDC-hsm IDC-kms IDAAS

**加密机网络规划**

每个机房需要为hsm产品分配一个/24地址段，使用平台内部私网地址。 自动化IP分配工具会将该地址段按照以下规则拆分： 将HSM Virtual地址段（/24）拆分为四个小段（/26），每个小段供一组ASW下的加密物理机和虚拟机使用，小段内第一个IP地址作为网关，第二个为物理加密机（HSM）的IP，其余的顺延作为虚拟加密机 （VSM）IP，如果加密机分为GVSM和EVSM两种类型，地址优先GVSM开始分配。 IP分配示例如下表：

| 机房 | 规划地址段 | 加密机 | IP地址段 | 网关地址 | 物理加密机IP | 虚拟加密机类型 | 虚拟加密机IP |
|---|---|---|---|---|---|---|---|
| 机房 1 | x.x.x.0/24 | 设备1 | x.x.x.0/26 | x.x.x.1/26 | x.x.x.1/26 | GVSM | x.x.x.3 |
|  |  |  |  |  |  | GVSM | x.x.x.4 |
|  |  |  |  |  |  | EVSM | x.x.x.5 |
|  |  |  |  |  |  | EVSM | x.x.x.6 |
|  |  |  |  |  |  | 其他EVSM | 依次递增 |
|  |  |  | x.x.x.32/2 6 | 预留，未来横向扩容加密机使用 |  |  |  |
|  |  | 设备2 | x.x.x.64/2 6 | x.x.x.65/2 6 | x.x.x.66/26 | GVSM | x.x.x.67 |
|  |  |  |  |  |  | GVSM | x.x.x.68 |
|  |  |  |  |  |  | EVSM | x.x.x.69 |
|  |  |  |  |  |  | EVSM | x.x.x.70 |
|  |  |  |  |  |  | 其他EVSM | 依次递增 |
|  |  |  | x.x.x.96/2 6 | 预留，未来横向扩容加密机使用 |  |  |  |
