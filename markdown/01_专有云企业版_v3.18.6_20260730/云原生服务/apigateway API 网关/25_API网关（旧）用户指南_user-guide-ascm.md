---
title: "网关 API网关（旧）用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 88
source_pdf: "25_API网关（旧）用户指南_user-guide-ascm.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apigateway/zh/user-guide-ascm.pdf"
converter: line-classifier (PyMuPDF)
---

# 网关 API网关（旧）用户指南

## 产品概述

API网关为您提供完整的API托管服务，辅助您将能力、服务、数据以API的形式开放给合作伙伴提供防攻击、防重放、请求加密、身份认证、权限管理、流量控制等多重手段保证API安全，降低API开放风险。 API网关将能力的复用率最大化，企业间能够互相借力，企业发展能够专注自身业务，实现共赢。 图 1. API网关界说明

## API网关产品责任边界说明

本文档明确了专有云场景下API网关产品的责任边界，明确了API网关产品的免责范围。 API 网关产研团队仅对按照官方提供的产品文档与运维手册进行规范操作的结果负责，下面是API网关产研团队的免责范围： （2）因用户后端服务异常、应答超时、无法连接、网络不可达等原因导致的API调用失败； （3）因网络传输问题导致的API调用失败； （5）客户的应用程序受到黑客攻击而导致被API网关限制的请求； （6）客户端版本过低(不支持SNI)导致HTTPS连接建立失败的请求； （7）用户的域名证书没有及时更新或者更新了错误域名证书导致失败的请求； （8）用户的域名未备案导致失败的请求； （9）因请求数超出API网关规定配额，引起的调用失败； （10）客户未正确配置客户端超时时间导致的失败的请求； （11）任何阿里云所属设备以外的网络、设备故障或配置调整引起的调用失败； （12）用户的应用程序或数据信息受到黑客攻击而引起的调用失败； （13）用户维护不当或保密不当致使数据、口令、密码等丢失或泄漏所引起的调用失败； （14）用户的疏忽或由用户授权的操作所引起的调用失败； （15）客户未遵循阿里云产品使用文档或使用建议引起的调用失败； （16）用户任何非标准化部署的服务引起的调用失败； （17）专有云运维缺失引起的调用失败； （18）不可抗力以及意外事件引起的调用失败； （19）其他非阿里云原因所引起的调用失败； （20）客户端发出的HTTP请求或者后端服务返回的HTTP应答不符合HTTP规范导致的失败请求。 API网关产研团队有责任和义务在任何情况下协助用户尽快恢复业务。

## 登录API网关控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。
1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 单击**账号登录**。
4. 在页面顶部的菜单栏中，选择**产品** > **应用服务** **> API****网关**。

## 快速入门

### 创建后端服务为HTTP的API

本文将快速引导您如何在API网关中，发布后端服务为HTTP类型的API，并如何使用”阿里云APP”认证中的 AppKey和AppSecret进行调用。您需要依次完成以下步骤：**创建分组**->**定义****API**->**创建应用和****API****授权**-

#### 创建分组

1. **创建分组**。点击**开放****API >** **分组管理**，在分组管理页面，点击**创建分组**；在新的页面，选择**组织**，**资源**
集，**地域**，实例默认选择“Shared Instance(Classic Network)”，输入分组名称testAppkeyGroup， 点击**提交**
2. **查看分组信息**。回到**分组管理**页面，点击**刷新**，能看到刚刚创建的分组，点击名称可以进入到详情页，进
行绑定域名、修改基本信息等动作。API分组会自动创建二级域名，此二级域名可作为专有云内调用该分组下的所有API的域名使用，在本示例中使用此域名进行测试。
1. **定义****API****基本信息**。本环节是定义了API的基本信息，包括 API 分组、 API 名称、安全认证方式、 API 类
型、和描述等。选择刚刚创建的分组testAppkeyGroup，写入对应配置，主要选择阿里云APP认证，禁止AppCode认证。
2. **定义****API****请求**。本环节是定义client端(如浏览器、手机APP或其他的业务系统)如何请求您的API，需要确
定的内容包括请求类型、协议、请求Path、HTTP Method、入参请求模式、和入参定义。在本例中，请求path中配置”/web/cloudapi”，并且分别配置了一个path参数，query参数和header参数。
3. **定义****API****后端服务信息**。本环节是定于API网关收到client端的请求后，进行何种参数映射、处理，以及连
接哪个后端地址。本例中的后端服务类型选择HTTP(s)服务，此后端服务可以填写任何能与API网关网络能通的地址，其他的后端服务类型可以参考其他帮助文档。按照页面要求完成后端地址、请求Path信息。
4. **定义返回结果**。本环节用于API帮助文档的自助生成，帮助API使用者更好理解。可以设置返回
ContentType、返回结果示例和失败返回结果示例。本例中不涉及到这部分，因此可以点击**保存**按钮
5. **发布****API**。您对API进行过任何的配置，都需要发布到对应的环境(API网关内置了三个环境：”线上”、”预
发”、”测试”)中才能够生效。本例中，点击发布，按照控制台页面的提示，把此API发布到”线上”环境。

**创建应用和API授权**

应用（APP）是您调用API服务时的身份。在本例中的步骤1中，认证方式选择的是”阿里云APP认证”，因此在API发布后，还需要创建APP，并将APP和API的对应关系建立好，才能够正常访问。
1. **创建应用**。在**调用****API >** **应用管理**页面先创建一个APP，然后进入APP详情页面，如下图所示。可以看到
阿里云APP下有两种认证方式，AppKey和AppCode。AppKey方式有一组AppKey和AppSecret，您可以理解为账号密码，调用API的时候需要将AppKey做参数传入，AppSecret用于签名计算，网关会校验这对密钥对您进行身份认证。
2. 对**API****进行授权**。在**API****管理**页面，找刚创建好的API，在操作项中，点击**授权**，出现如下的弹出框。注
意环境需要选择已经进行了发布的环境，如本例中的”线上”。直接点击**搜索**，会搜出刚创建的应用，点击+**添加**；然后点击**确定**，提示授权成功，即成功授权；

**调试API**

API网关提供了在线调试的功能，因此一般建议在API网关上完成API配置之后，可以先通过此功能确认API是否配置成功，然后再通过client端进行调用。 在**调用****API >** **应用管理**页面，点击前面步骤中授权的应用，进入应用详情页，选择**已授权的****API**，在对应 API右侧的操作下，点击**调试****API**进入如下页面。如果您定义了API的入参，在调试API页面中也可以输出不同的参数查看API的执行情况。 只有API已经发布到某环境，且将该环境的API已经授权给APP后，在**已授权的****API**中才会显示。 通过上述步骤，您已经创建API、创建APP、建立了授权关系，调试API完成，并将API发布到线上环境，本阶段将会模拟如何通过调用API网关提供的SDK，来在您的业务系统中调用发布好的API。 在**调用****API >** **已授权****API**的**SDK**页面，您可以下载此应用授权的API的SDK。通过点击对应的语言，直接下载SDK包。里面包含了API对应的文档和API的sdk。具体使用方法可参考里面对应的readme文档目前只支持线上环境的API的sdk。

## 调用 API

### 管理应用

#### 创建应用

应用（APP）是您调用API服务时的身份。您可以拥有多个APP，可以根据您的业务需求分别被授权不同的 API。API的授权对象是APP而不是用户账号。您可以在API网关控制台完成对APP的创建、修改、删除、查看详情、密钥管理、查看已授权等管理操作。 每个APP有一组**Key**和**Secret**，您可以理解为账号密码，您调用API的时候需要将**AppKey**做参数传入，**AppSecret**用于签名计算，网关会校验这对密钥对您进行身份认证。调用API需要这个APP具备调用该API的权限，这个授权和鉴权也是面向APP的。 您可以在API网关控制台**应用管理**页面创建您的APP。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**调用****API >** **应用管理**。
3. 单击页面右上角的**创建****APP**。
应用名称必须全局唯一，支持汉字、英文字母、数字、英文格式的下划线，且必须以字母或汉字开始，4~26个字符。 创建成功后，系统会为APP分配一对**AppKey**和**AppSecret**。您需要使用**AppSecret**完成签名计算， 您请求时需要携带签名信息，网关会通过签名信息对您做身份验证。 在**应用管理**页面，单击应用名称进入详情，就能看见**AppKey**和**AppSecret**信息，如果密钥丢失还可以操作重置。

#### 查看应用详情

您可以查看已经创建的应用的详细信息。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**调用****API >** **应用管理**。
3. 单击要查看的应用的名称。
您可以查看应用的基本信息，**APPKey**和**已授权的****API**

#### 编辑应用

您可以编辑已经创建的应用。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**调用****API >** **应用管理**。
3. 选择需要修改的应用并单击操作图标中的**修改**选项。
4. 修改应用信息并单击**确定**。

#### 删除应用

您可以删除已经创建的应用。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**调用****API >** **应用管理**。
3. 选择需要删除的应用并单击**删除**。
4. 在弹出的对话框中单击**确定**。

### 查看已创建的 API

您可以通过控制台查看已经创建的API。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。

### 授权

授权，是指授予APP调用某个API的权限。您的APP需要获得API的授权才能调用该API。 您需要向API服务商提供您的应用ID (AppID)，使API服务商能够搜索到您的APP，并完成授权。完成授权后您可以在控制台看到该APP被授权的 API。 由提供方操作授权的API会出现在应用详情的**已授权** **API**子页面。 提供方授权时就已经将API授权给准确的APP 了，所以您不需要也没有权限来操作授权。

### 加密签名

您调用API时，需要拼接签名字符串，并将签名计算后的字符串放在请求的Header传入，网关会通过对称计算签名来验证请求者的身份。 在请求的Header需要传入一个计算后的签名字符串。 您需要将入参信息按照请求签名说明文档组织成为String to sign，再用SDK样例中的算法计算签名。计算结果就是上面提到的计算后的签名字符串。 HTTP和HTTPS 请求，都需要加入请求签名。 请求签名String to sign 的组织方法请参见请求签名说明文档，您只需要在SDK样例中，将AppKey、 AppSecret换成您自己的真实密钥值，再根据实际API文档按照签名文档组织String to sign，您就可以成功发起请求了。

### 请求签名说明文档

**域名**

每个API服务都属于一个API分组，每个API分组有不同的域名。域名是由服务端绑定的独立域名，API网关通过域名来寻址定位API分组。 域名的格式为www.[独立域名].com/[Path]?[HTTPMethod]。 API网关通过域名定位到一个唯一的分组，通过Path+HTTPMethod 确定该分组下唯一的API。 您购买后在控制台**已购买** **API**可以获得API文档说明，若无购买行为，则可以联系API提供者操作授权， 授权后您就可以在控制台应用详情页面的**已授权的** **API**获得API文档说明。

**系统级 Header**

【必选】X-Ca-Key：AppKey。 【必选】X-Ca-Signature：签名字符串。 【可选】X-Ca-Timestamp：API调用者传递时间戳，值为当前时间的毫秒数，也就是从1970年1月1日起至今的时间转换为毫秒，时间戳有效时间为15分钟。 【可选】X-Ca-Nonce：API 调用者生成的UUID，结合时间戳防重放。 【可选】Content-MD5 当请求Body非Form表单时，可以计算Body的MD5值传递给云网关进行Body MD5校验。 【可选】X-Ca-Stage请求API所属Stage，目前仅支持TEST 、PRE和RELEASE，默认RELEASE，若您调用的API不在线上环境，请一定要指定该参数的值，否则会报URL错误。

**签名校验**

组织参与签名计算的字符串

```
String stringToSign= HTTPMethod + "\n" +
```

Accept + "\n" + //建议显示设置 `Accept Header`。当 `Accept` 为空时，部分 `Http` 客户端会给 `Accept` 设置默认值为 `*/*`，导致签名校验失败。

```
Content-MD5 + "\n" Content-Type + "\n" + Date + "\n" + Headers + Url
```

HTTPMethod为全大写，如POST。 Accept、Content-MD5、Content-Type、Date 如果为空也需要添加换行符 \n ，Headers如果为空不需要添加 \n 。 Content-MD5 Content-MD5是指Body的MD5值，只有当Body非Form表单时才计算MD5，计算方式为：

```
String content-MD5 = Base64.encodeBase64(MD5(bodyStream.getbytes("UTF-8")));
```

bodyStream为字节数组。 Headers Headers是指参与Headers签名计算的Header 的 Key、Value拼接的字符串，建议对X-Ca 开头以及自定义Header计算签名。

**重要**

如下参数不参与Headers 签名计算：X-Ca-Signature、X-Ca-Signature-Headers、Accept、 Content-MD5、Content-Type、Date。 Headers组织方法： 先对参与Headers 签名计算的Header的Key按照字典排序后使用如下方式拼接，如果某个Header的 Value为空，则使用 HeaderKey + “:” + “\n” 参与签名，需要保留Key和英文冒号。

```
String headers = HeaderKey1 + ":" + HeaderValue1 + "\n"\+ HeaderKey2 + ":" + HeaderValue2 + "\n"\+ ... HeaderKeyN + ":" + HeaderValueN + "\n"
```

将Headers签名中Header的Key使用英文逗号分割放到Request的Header中，Key为：X-Ca-Signature- Headers。 Url Url指**Path + Query + Body**中**Form**参数，组织方法：对**Query+Form**参数按照字典对**Key**进行排序后按照如下方法拼接，如果**Query**或**Form**参数为空，则 `Url = Path` ，不需要添加？，如果某个参数的**Value**为空只保留**Key**参与签名，等号不需要再加入签名。

```
String url = Path + "?" + Key1 + "=" + Value1 + "&" + Key2 + "=" + Value2 + ... "&" + KeyN + "=" + ValueN
```

**重要**

这里**Query**或**Form**参数的**Value**可能有多个，多个的时候只取第一个Value参与签名计算。

**计算签名**

```
Mac hmacSha256 = Mac.getInstance("HmacSHA256"); byte[] keyBytes = secret.getBytes("UTF-8"); hmacSha256.init(new SecretKeySpec(keyBytes, 0, keyBytes.length, "HmacSHA256")); String sign = new String(Base64.encodeBase64(Sha256.doFinal(stringToSign.getBytes("UTF- 8")),"UTF-8"));
```

`secret` 为APP的密钥。

**传递签名**

将计算的签名结果放到Request 的Header 中，Key为 X-Ca-Signature。

**签名错误排查方法**

当签名校验失败时，API网关会将服务端的StringToSign放到HTTP Response的Header中返回到客户端，Key为：X-Ca-Error-Message，只需要将本地计算的StringToSign 与服务端返回的StringToSign进行对比即可找到问题。 如果服务端与客户端的StringToSign一致请检查用于签名计算的密钥是否正确。 因为HTTP Header中无法表示换行，因此StringToSign中的换行符都被过滤掉了，对比时请忽略换行符。

### API调用示例

您可以直接用API网关控制台为您提供的多语言调用示例来测试调用，可以自行编辑HTTP(S) 请求来调用 API。

**第一部分：请求**

**请求地址**

请求的域名内网调用默认是分组的二级域名，可以在**开放****API >** **分组管理**，进入分组详情，查看分组二级域名。如果该分组绑定了独立域名，则可以使用独立域名发起访问。

```
http://e710888d3ccb4638a723ff8d03837095-cn-qingdao.aliapi.com/demo/post
```

**请求方法**

```
POST
```

**请求体**

```
FormParam1=FormParamValue1&FormParam2=FormParamValue2 //HTTP Request Body
```

**请求头部**

```
Host: e710888d3ccb4638a723ff8d03837095-cn-qingdao.aliapi.com Date: Mon, 22 Aug 2016 11:21:04 GMT User-Agent: Apache-HttpClient/4.1.2 (java 1.6) Content-Type: application/x-www-form-urlencoded; charset=UTF-8
```

`//`请求体类型，请根据实际请求体内容设置。

```
Accept: application/json
```

`//`请求响应体类型，部分 `API` 可以根据指定的响应类型来返回对应数据格式，建议手动指定此请求头，如果不设置， 部分 `HTTP` 客户端会设置默认值 `*/*`，导致签名错误。

```
X-Ca-Request-Mode: debug
```

`//`是否开启 `Debug` 模式，大小写不敏感，不设置默认关闭，一般 `API` 调试阶段可以打开此设置。

```
X-Ca-Version: 1
```

`// API`版本号，目前所有 `API` 仅支持版本号『1』，可以不设置此请求头，默认版本号为『1』。

```
X-Ca-Signature-Headers: X-Ca-Request-Mode,X-Ca-Version,X-Ca-Stage,X-Ca-Key,X-Ca-Timesta
```

`mp` `//`参与签名的自定义请求头，服务端将根据此配置读取请求头进行签名，此处设置不包含 `Content-Type`、`Accept` 、`Content-MD5`、`Date` 请求头，这些请求头已经包含在了基础的签名结构中，详情参照请求签名说明文档。

```
X-Ca-Stage: RELEASE
```

`//`请求 `API`的`Stage`，目前支持 `TEST`、`PRE`、`RELEASE` 三个 `Stage`，大小写不敏感，`API` 提供者可以选择发布到哪个 `Stage`，只有发布到指定 `Stage` 后 `API` 才可以调用，否则会提示 `API` 找不到或 `Invalid Url`。

```
X-Ca-Key: 60022326
```

`//`请求的 `AppKey`，请到 `API` 网关控制台生成，只有获得`API`授权后才可以调用。

```
X-Ca-Timestamp: 1471864864235
```

`//`请求的时间戳，值为当前时间的毫秒数，也就是从`1970`年1月1日起至今的时间转换为毫秒，时间戳有效时间为`15`分钟。

```
X-Ca-Nonce:b931bc77-645a-4299-b24b-f3669be577ac
```

`//`请求唯一标识，`15`分钟内 `AppKey+API+Nonce` 不能重复，与时间戳结合使用才能起到防重放作用。

```
X-Ca-Signature: FJleSrCYPGCU7dMlLTG+UD3Bc5Elh3TV3CWHtSKh1Ys=
```

`//`请求签名。

```
CustomHeader: CustomHeaderValue
```

`//`自定义请求头，此处仅作为示例，实际请求中根据 `API`定义可以设置多个自定义请求头。

**第二部分：响应**

**状态码**

`//`响应状态码，大于等于`200`小于`300`表示成功；大于等于`400`小于`500`为客户端错误；大于`500`为服务端错误。

**响应头**

```
X-Ca-Request-Id: 7AD052CB-EE8B-4DFD-BBAF-EFB340E0A5AF
```

`//`请求唯一 `ID`，请求一旦进入 `API` 网关应用后，`API` 网关就会生成请求 `ID` 并通过响应头返回给客户端，建议客户端与后端服务都记录此请求 `ID`，可用于问题排查与跟踪。

```
X-Ca-Error-Message: Invalid Url
```

`// API`网关返回的错误消息，当请求出现错误时 `API` 网关会通过响应头将错误消息返回给客户端。

```
X-Ca-Debug-Info: {"ServiceLatency":0,"TotalLatency":2}
```

`//`当打开 `Debug` 模式后会返回 `Debug` 信息，此信息后期可能会有变更，仅用做联调阶段参考。 您调用API时，无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名信息。详细加密签名的计

## 开放 API

### 管理分组

#### 创建分组

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 单击页面右上角的**创建分组**。
4. 在页面上选择对应的**组织**，**资源集**和**地域**。然后填写分组的**分组名称**和**描述**信息，完成后单击**确定**。
分组名称必须唯一，支持汉字、英文字母、数字、英文格式的下划线，必须以英文字母或汉字开头，4~50个字符。

#### 域名管理

专有云内可以直接使用分组二级域名调用API，您也可以绑定自己的域名到分组上，这样就可以用您的域名访问该分组的API。

**背景信息**

如果要直接用您的域名调用API，不仅要在分组上进行域名的绑定操作，还需要在您的域名管理的地方添加 DNS解析，解析到分组二级域名上或者分组二级域名对应的IP上。

**绑定独立域名**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 选择需要绑定域名的分组，单击右侧的**操作**列中的**绑定域名**。
4. 在弹出的确认对话框中，填写**域名**信息，并单击**绑定**。

**删除域名**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 在**分组列表**中，单击所需的分组，进入**分组详情**页面。
4. 在分组的**独立域名**里，单击**删除域名**按钮。
5. 在弹出的确认对话框中，单击**确定**。

#### 证书管理

独立域名如果要支持HTTPS，还需要上传SSL证书。

**背景信息**

一个API接口要支持HTTPS调用，除了域名需要支持HTTPS外，API定义中的请求基础定义>网络协议需要勾选HTTPS。

**上传证书**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 在**分组列表**中，单击所需的分组，进入**分组详情**页面。
4. 在分组的**独立域名**里，单击**SSL****证书**列的+**添加**。
5. 在弹出的**创建证书**对话框中，填写**证书名称**，**证书内容**，**私钥**，然后单击**确定**。

**编辑证书**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 在**分组列表**中，单击所需的分组，进入**分组详情**页面。
4. 在分组的**独立域名**里，单击**SSL****证书**列的**编辑**。
5. 在弹出的**创建证书**对话框中，填写**证书名称**，**证书内容**，**私钥**，然后单击**确定**。

**删除证书**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 在**分组列表**中，单击所需的分组，进入**分组详情**页面。
4. 在分组的**独立域名**里，单击**操作**列的**删除证书**。
5. 在弹出的确认对话框中，单击**确定**。

#### 删除分组

您可以删除已经创建的分组。

**操作步骤**

## 1. 登录API网关控制台

2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 选择需要删除的分组，单击右侧操作列中的**删除**。
4. 在弹出的确认对话框中单击**确认**。
删除分组前需要先删除分组下的API。

**说明**

#### 环境管理

关于环境需要理解两个概念，环境和环境变量。
**环境**是API分组上的一个配置，每个分组有若干个环境。 API录入后，未经发布时，就只是API定义。发布
到某个环境后才是能够对外提供服务的API 。
**环境变量**是在环境上用户可创建可管理的一种变量，该配置是固定于环境上的。如在线上环境创建变量，
变量名为 `Path` ，变量值为 `/stage/release` 。 在API定义中的Backend Service Address位置，写作 #Path# ，即配置为变量标识，变量名为 `Path` 。 那么将该API发布到线上环境时，该API在线上环境的运行定义，Path处的 #Path# ，会取值

```
为 /stage/release 。
```

而将该API发布到其他环境时，若环境上没有环境变量 #Path# ，则无法取值，那么API就无法调用。 使用环境变量可以解决后端服务需要区分环境的问题，通过不同的环境上配置不同的服务地址和Path，来调用不同的后端服务，同时API的定义配置又是一套。使用时需要注意以下几点： 变量名严格区分大小写。 如果在API定义中设置了变量，那么一定要在要发布的环境上配置变量名和变量值，否则变量无赋值， API将无法正常调用。

**创建环境变量**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 选择所需的分组，单击右侧操作列的**环境管理**。
4. 单击**新增变量**，填写变量名和变量值，并单击**新增**。
请给线上，预发，测试环境分别加上相同的环境变量，值可以不同。待API发布到对应环

**重要**

境后，会自动将变量值进行替换。

**删除环境变量**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API >** **分组管理**。
3. 选择所需的分组，单击右侧操作列的**环境管理**。
4. 选择所需的运行环境和需要删除的变量，单击右侧操作列中的**删除**。
5. 在弹出的确认对话框中，单击**确定**。

### 创建API

#### 概述

创建API，即在API网关录入API的定义。您需要定义API的基本信息、服务信息、请求信息、返回信息。 网关支持您配置对入参的预校验规则，让网关成为您后端服务的第一道关卡。 网关支持您配置前端和后端的全映射，即参数混排。如您可以让您的用户在**Query**传入参数，但是您后端从**Header**里接收，等等。以满足您需要将服务包装变形输出。 网关支持您配置常量参数、系统参数，这些参数对您的用户不可见，但是网关可以在中转时将常量参数、 系统参数加入请求中，传递至后端服务，满足您后端的一些业务需求。比如您需要网关每次向您发送请求都带有一个keyword **aligateway**，您就可以把**aligateway**配置为常量参数，并指定接收的位置。

#### 创建API

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 单击页面右上角的**创建****API**
4. 填写API的基本信息并单击**下一步**。

| 参数 | 描述 |
|---|---|
| 分组 | 分组是API的管理单元，创建API之前您需要先创建分组，选择分组即选择Region。 |
| API名称 | 所创建的API的名称。 |

| 安全认证方式 | API请求的认证方式，目前支持阿里云APP和无认证两种认证方式。 阿里云APP：认证方式即要求请求者调用该 API 时能够通过对APP的身份认证。 无认证：认证方式即任何人知晓该 API 的请求定义后，均可发起请求，网关不对其做身份验证，均会转发至您后端服务。 |
|---|---|
| 签名算法 | 参与签名的算法 HmacSHA256 HmacSHA1和HmacSHA256：表示同时支持这2种签名算法 |
| 描述 | 填写API的相关描述。 |

5. 定义API请求。定义用户如何请求您的API ，包括请求类型、网络协议、请求Path、HTTP Method、入
参请求模式。

| 参数 | 描述 |
|---|---|
| 请求类型 | 请求类型： 有4种类型可选， 目前只支持普通请求。 普通请求：普通的HTTP(S)协议请求。 |
| 网络协议 | API调用支持HTTP,HTTPS,WEBSOCKET协议 |
| 请求Path | Path指相对于服务host，API的请求路径。请求Path可以与后端服务实际Path不同， 您可以随意撰写合法的有明确语义的Path给用户使用。您可以在请求Path中配置动态参数，即要求用户在Path中传入参数，同时您的后端又可以不在Path中接收，可以映射为在Query、Header等位置接收。 |
| HTTP Method | 可选择PUT、GET、POST、PATCH、DELETE、HEAD。 |
| 入参请求模式 | 可选入参映射和入参透传。 入参映射（过滤未知参数）表示Query，Path 和 Body Form位置的参数需要配置前后端映射，网关只会透传给后端配置过的参数，其他参数会被过滤掉。 入参映射（透传未知参数）表示Query，Path 和 Body Form位置的参数需要配置前后端映射，网关除配置的请求参数外，不对其他位置的请求参数进行映射与校验，用户参数会透明传递给后端入参透传表示不需要在入参定义处配置Query，Body Form参数（PATH参数仍需要配置）。客户端传给网关的参数都会被网关透传给后端。 |

6. 配置入参定义。
定义您API的请求入参，即配置用户需要在什么位置传入什么参数。可选位置有Head、Query、Body、 Path（Parameter Path），尤其当您在Path中配置了动态参数，那么在入参配置时需要对动态参数做配置说明。支持的参数类型有String、Integer、Boolean。 需要注意所有参数的名称会校验是否唯一。 您可以使用左侧的快捷键快速调整参数顺序。 您可以使用操作图标下的**删除**选项，删除不需要的参数。
7. 设置参数校验规则。
您可以单击操作图标中的**编辑更多**配置校验规则。如String的长度，Number的枚举等等。网关会参照校验规则对请求做初步校验，如果入参不合法，则不会到达您的后端服务，大大的降低了后端服务的压力。
8. 设置后端服务信息并单击**下一步**。
这部分主要是定义一些参数的前后端映射，具体描述的是您后端真实服务的API配置。用户请求到达网关后，网关会根据您的后端配置映射为对应实际后端服务的请求形式，去请求您的后端。包括后端服务地址、后端Path、后端超时时间、参数映射、常量参数、系统参数。 您所有录入的参数，包括Path中的动态参数、Headers参数、Query参数、Body参数

**说明**

（非二进制）、常量参数、系统参数，参数名称保证全局唯一。即如果您同时在Headers和Query里各有一个名为name的参数，是不允许的。 i. 设置后端基础定义。

| 参数 | 描述 |
|---|---|
| 后端服务类型 | HTTP(s): 默认类型，后端是HTTP或者HTTPS协议的服务接入，当网关和后端服务网络能直接连通时使用。 VPC: 当后端服务在某个VPC内时使用。 Mock: 用于模拟最初预定的返回结果 |
| VPCID | 当后端类型为VPC时，此处需要填写后端服务所在的VPCID |
| 后端服务地址 | 后端服务的host。 后端服务为HTTP(s): 可以是一个域名，也可以是 http(s)://host:port 的形式。 后端服务为VPC：此处需要用 http://ip:port 形式填写，不支持填写域名。 |
| 后端请求 Path | Path是您的API服务在您后端服务器上的请求路径，实际请求路径。若您后端Path 需要接收动态参数，那么需要声明该参数是调用者从哪个位置哪个参数传入的，即声明映射关系。 |
| HTTP Method | 可选择PUT、GET、POST、PATCH、DELETE、HEAD。 |
| 后端超时 | 指API请求到达网关后，网关去调API后端服务的响应时间。由网关请求后端开始到网关收到后端返回结果。该值不能超过30秒。超过该值网关会放弃请求后端服务， 并给用户返回相应的错误信息。 |

ii. 配置后端服务参数。 网关支持参数在前端、后端的全映射，包括名称映射和位置映射。位置映射包括Path、Header、 Query、Body的混排映射。也就是说，您可以将您的后端服务通过映射完成包装成更规范、更专业的 API形态。这部分就是在声明前后端API映射关系的。 前后端参数名称不能重复。

**说明**

iii. 配置常量参数。 比如您需要网关每次请求您后端时都带有标记apigateway，您可以直接将标记配置为常量参数。常量参数对您的用户不可见，请求达到网关后，网关会自动在指定位置加上该参数再去请求您的后端。 iv. 配置系统参数。 API网关的系统参数，这些参数默认不会传递给您，但是如果您需要获取，您可以在API里配置接收位置和名称。具体内容如下表：

| 参数名称 | 参数含义 |
|---|---|
| CaClientIp | 发送请求的客户端IP。 |
| CaDomain | 发送请求的域名。 |
| CaRequestHandleTim e | 请求时间（格林威治时间）。 |
| CaAppId | 请求的APP的ID。 |
| CaRequestId | 每次请求的唯一标识：RequestId。 |
| CaApiName | API名称。 |
| CaHttpSchema | 用户调用API使用的协议，HTTP或者HTTPS。 |
| CaProxy | 代理（AliCloudApiGateway）。 |

9. 定义返回结果并单击**创建**。
您可以设置返回contentType、返回结果示例、失败返回结果示例和错误码定义。目前返回结果在 API 网关是不做解析的，API 网关直接转发给 API 的请求者。

#### 安全认证

API网关支持的安全认证方式为阿里云APP和无认证。 阿里云APP：API提供者需要将API授权给某个APP，API调用者访问API时需要带上AppKey和加密签名 （具体签名方法参考加密签名），否则网关会校验不通过。 无认证：只要API发布后，无需授权即可被调用。请求API时无需传AppKey和加密签名。

#### 网络协议

控制台暂时不支持HTTPS的域名配置，所以通过控制台配置的HTTPS暂时无效。如果确实需要HTTPS，可以暂时通过API网关的OpenAPI去配置。 可以在API页签找到相应API，在**API****定义** > **编辑** > **请求基础定义**中进行修改。 API可选的协议包括： HTTP：允许HTTP访问。 HTTPS：允许HTTPS访问。 WEBSOCKET：允许WEBSOCKET访问。

#### BODY配置

当HTTP Method选择POST/PUT/PATCH等方式时，可以配置BODY。此时有2种方式设置。以下2种方式配置互斥。 FORM表单形式的BODY配置：在入参定义中增加一条，参数位置选择BODY。该位置配置的BODY只能用于FORM形式传输非FORM表单的BODY配置：如果要传输的BODY为JSON，XML，需要勾选“ 非Form表单数据，比如 JSON字符串、文件二进制数据等”。Body大小不要超过8M。

#### Mock 您的 API

在项目开发过程中，往往是多个合作方一同开发，多个合作方相互依赖，而这种依赖在项目过程中会造成相互制约，理解误差也会影响开发进度，甚至影响项目的工期。所以在开发过程中，一般都会使用Mock来模拟最初预定的返回结果，来降低理解偏差，从而提升开发效率。 API网关也支持Mock模式的简单配置。

**配置 Mock**

单击左侧导航栏的**开放****API > API****列表**，单击API所对应的操作下的**管理**，进入API详情页面，单击页面右上角的**编辑**按钮，进入API编辑页面。 在**API** **编辑页面** > **后端基础定义**，来配置Mock。
1. **后端服务类型**选择**Mock**
2. 填写Mock返回结果。
Mock返回的body内容，可以填写您真实的返回结果。目前支持是Json、XMl、文本等格式作为Mock返回结果。如

```json
  {
 "result": {
```

`"title": " API` 网关 `Mock` 测试`",`

```
 }
 }
```

保存后Mock设置成功，请根据实际需要**发布**到测试或线上环境进行测试。
3. 设置**HTTP Status Code**，需要按照Http status code标准填写。一般成功填写200
4. 设置**Mock Header**，可根据需要添加Mock返回的header

#### 返回ContentType

该值仅用于API文档生成，不会修改后端的真实返回值。所以后端服务需要自己返回Content-Type这个 header。

### API 管理

#### 查看和编辑 API 定义

您可以查看API定义并根据需要进行编辑。 当您需要编辑某个API的定义时，如果该API已经发布，对定义的修改不会对线上产生影

**说明**

响，定义修改后需要再次发布才能把修改后的定义同步到线上环境。
1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 选择需要查看的API
点击操作列下的**管理**。您可以看到当前所选API的定义信息。 按照您的需要进行编辑，单击**编辑**按钮。 编辑API定义的流程和创建API定义一致，详细信息参见创建API。如果您想放弃编辑，可以点击页面顶部的返回图标。

#### 发布 API

API创建完成后，发布到某环境，通过二级域名或者独立域名访问时，需要在请求的Header指定要请求的环境。 当您要发布某个API时，如果该API在测试或者线上已经有版本在运行，您的此次发布将覆盖原来环境的 API定义，15秒内自动生效。但是历史版本及定义会有记录，您可以快速回滚。 您可以将测试或者线上的某个API下线，下线之后，与插件的绑定或者与APP的授权关系依然存在，再次上线时会自动生效。如果要解除关系，需要专门去做授权关系和插件的解绑操作。

**步骤 1 发布**

API网关支持对测试/线上的API做版本管理，您可以发布API、下线API还可以切换版本，切换版本是实时生效。
1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 单击要发布的API右侧的操作图标，选择**发布**。
4. 选择要发布的环境，填写变更备注后，单击**确定**。

**步骤 2 测试**

为了模拟真实的用户请求，您可以自己创建一个APP，操作您的API给这个APP授权。 然后按照真实的请求场景，写代码或者基于网关提供的SDK样例请求API。 您可以将API发布到测试或者线上环境，在绑定独立域名之前，可以直接访问二级域名来进行测试调用。请求时注意指定环境（通过增加header X-Ca-Stage: TEST/PRE/RELEASE 访问各个环境），若不指定则默认为访问线上。

#### 授权

您需要通过授权来建立API和APP的权限关系。您将API发布到线上环境后，需要给客户的APP授权，客户才能用该APP进行调用。您有权对此类授权操作建立或者解除某个API与某个APP的授权关系， API网关会对权限关系进行验证。

**说明**

您可以将一个或者多个API授权给一个或者多个APP 。 如果一个API在测试和线上均有发布，但是只将测试的API授权给某APP，那该APP只能调用测试环境。 您可以通过客户提供给您的AppID来定位APP 。 当您需要解除某个API下某个APP的授权时，您可以查看API的授权列表，在列表页进行解除。 应用（APP）代表请求者的身份。当您的客户或者您自己测试调用API时，都需要创建APP作为请求者的身份，然后由您操作给APP授权。 授权是区分环境的，同一个API、同一个APP，在两个环境需要分别授权，避免因为授权的

**说明**

环境和请求的环境不一致，导致报错。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 选择要授权的API ，单击右侧的操作图标，选择**授权**，页面会弹出API授权窗口。
4. 选择要授权的环境，和要授权的应用。
左侧为**我的应用**，此时直接点击**搜索**，会自动加载本账号下的APP 如果要给其他账号下APP授权，需要选择**应用****ID**,然后在文本框中输入对应的应用ID，再点击**搜索**进行查询。
5. 勾选要授权的应用，单击中间的向右添加的图标，添加到待授权应用列表中。
6. 单击**确定**按钮，完成授权。
7. 授权完成后，可以进入API管理页面，通过左侧的菜单**授权信息**进行查看。

#### 解除授权

您可以解除某个API下某个APP的授权。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 单击要解除授权的API，进入API定义详情页面，然后进入**授权信息**子页面
4. 勾选待解除的应用项，单击左下方的**解除授权**按钮。
5. 在弹出的确认对话框中，单击**确定**。

#### 下线 API

您可以下线已经发布的API定义。 您可以将测试或者线上的某个API下线，下线之后，与策略、密钥、 APP的绑定或者授权关系依然存在，再次上线时会自动生效。如果要解除关系，需要专门操作删除（参见解除授权）。
1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 选择需要下线的API，单击右侧操作列中的**下线**。
4. 在弹出的确认对话框中，选择要下线的环境，单击**确定**。

#### 查看发布历史

您可以查看您每个API的发布历史记录，包括每次发布的版本号、说明、环境、时间和具体定义内容。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 选择需要查看的API，单击右侧操作列中的**管理**。进入API详情页面
4. 单击左侧导航栏中的**发布历史**。可以看到该API的发布历史。
5. 单击右侧的**查看**，就可以看到该版本API定义的详情。

#### 切换发布版本

查看发布历史时，您可以选定某个版本然后操作切换到此版本，该操作会使该版本直接在指定环境中替换之前的版本，实时生效。

**操作步骤**

1. 登录API网关控制台。
2. 单击左侧导航栏的**开放****API > API****列表**。
3. 选择需要查看的API，并单击右侧的**管理**。进入API详情页面。
4. 单击左侧导航栏中的**发布历史**。
5. 选择需要的版本并单击右侧的**切换至此版本**。
6. 在弹出的确认对话框中，填写备注并单击**切换**。

### 插件管理

#### 参数与条件表达式的使用

在访问控制,流量控制 ,后端路由，错误码映射插件中，支持用户从当前的请求、应答或系统上下文中获取参数，并使用自定义的条件表达式对参数进行判断，本文描述参数的定义方法与条件表达式的书写方法。

**1、参数的定义**

1. 定义方式
在使用条件表达式前，需要先在parameters字段中将所有需要在条件表达式中需要使用的参数进行显式定义，参考下面的例子：

```
--parameters:
  method: "Method"
  appId: "System:CaAppId"
  action: "Query:action"
  userId: "Token:UserId"
```

`parameters` 字段类型是字符串类型的键值对，key和 value的定义规范为

| 的规则为 | [a-zA-Z ][a-zA-Z0-9]+ _ |  |
|---|---|---|
| {location}:{name} |  | 的方式进行定 |

考如下的例子:

| location |  |
|---|---|
| name | 表示 |

2. 参数的支持位置
在使用条件表达式前，我们需要先定义参与条件表达式计算的参数，目前API网关支持在插件中直接使用如下位置的参数

| 位置名称 | 适用范围 | 说明 |  |  |
|---|---|---|---|---|
| Method | 请求 | HTTP请求方法 (大写)，如: GET, POST … |  |  |
| Path | 请求 | HTTP完整请求路径, 如: /path/t o/query |  |  |
|  |  |  | /path/t |  |
| StatusCode | 应答 | 后端的HTTP应答码，如:200,400 |  |  |

|  | o/query |
|---|---|

| 户指南（旧）·开放 API |  | API 网关 |
|---|---|---|

| 位置名称 | 适用范围 | 说明 |  |  |
|---|---|---|---|---|
| ErrorCode | 应答 | 错误代码表 |  |  |
| Header | 请求/应答 | 使用 Header:{Name} 获取名字为 {Name} 的HTTP头的第一个值 |  |  |
| Query | 请求 | 使用 Query:{Name} 获取 QueryString中名字为 {Name} 的第一个值 |  |  |
| Form | 请求 | 使用 Form:{Name} 获取Form 中名字为 {Name} 的第一个值 |  |  |
| Host | 请求 | 使用 Host:{Name} 获取匹配到的泛域名模板参数 |  |  |
| Parameter | 请求 | 使用 Parameter:{Name} 获取用户API自定义参数中名字为Name 的第一个值 |  |  |
| BodyJsonField | 应答 | 使用 BodyJson:{JPath} 以 JSONPath方式获取请求/应答包体中的JSON字段值 |  |  |
| System | 请求/应答 | 使用 System:{Name} 获取名字为 {Name} 的系统参数值 |  |  |
| Token | 请求/应答 | 当处于jwt授权场景时，使用 Tok en:{Name} 获取token中名字为 {Name} 的值 |  |  |
|  |  |  | Tok |  |

|  | Header:{Name} |
|---|---|
| {Name} |  |

|  | System:{Name} |
|---|---|
| {Name} |  |

|  | en:{Name} |
|---|---|

取值规则说明

| 流量控制 |  | , | 后端路由 |  |  | ， | 错误码映射 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | Path |  |  |  |  |  |  |  |
| Method | , |  |  | , |  |  |  | , | Query |

| System , | Tok |
|---|---|

`en`

| 插件错误码映射置: StatusCode | 错误码映射 |  | 发生在应答阶段，插件仅支持适用范围为应答 , ErrorCode , Header , BodyJsonField |  |
|---|---|---|---|---|
|  |  |  |  | BodyJsonField |
| Method |  | Path |  |  |

`Header` 位置的参数，当用于请求阶段的插件时，读取来自客户端请求中的Header; 当用于应答阶段的插件时，读取来自后端应答中的Header `Parameter` 位置的参数，仅用于请求阶段的插件，查找API定义中同名的参数，使用参数名而非后端参数名查找，当参数不存在时返回为null `Path` 返回为完整的请求路径，如果需要Path位置的参数，请使用 `Parameter` 位置的参数 `BodyJsonField` 位置的参数，目前仅支持在错误码映射中使用，使用 `JSONPath` 方式读取应答 json包体的值，参考下面的JSONPath使用说明 `Token` 当配置了 `JWT`授权,使用 `Token:{CliamName}` 可以读取在插件定义的值，参考对应插件的文档
3. JSONPath使用说明
用于 `BodyJsonField` 位置，目前仅用于错误码映射插件，用于从后端返回的 `json` 包体中提取字段，关于JSONPath的详细规范说明

| code:"BodyJsonField:$.result code" _ |  |  |
|---|---|---|
| ，可以解析到 | code:ok |  |

```json
{ "result_code": "ok", "message": ... }
```

4. 系统参数列表

| 参数名称 | 参数含义 | 取值 |
|---|---|---|
| CaClientIp | 请求来源客户端IP | 如: 37.78.3.3 |
| CaDomain | 请求的完整域名(Host头) | 如: api.foo.com |
| CaAppId | 请求的 APP 的 ID | 如: 49382332 |
| CaAppKey | 请求的 APP 的 Key | 如: 12983883923 |
| CaRequestId | 网关生成的唯一请求Id | 如: CCE4DEE6-26EF-46CB- B5EB-327A9FE20ED1 |
| CaApiName | API 名称 | 如: TestAPI |
| CaHttpSchema | 客户端调用协议 | 取值范围: http, https, ws |
| CaClientUa | 客户端的UserAgent头 | 透传客户端上传的值 |
| CaStage | API网关环境 | 取值：TEST, PRE, RELEASE |

**2、条件表达式**

条件表达式可在插件或其他场景中使用，用于在需要的场景中执行灵活的条件判断
1. 基本语法
条件表达式与SQL表达式类似，比如: $A > 100 and '$B = 'B'

| 变量参数 q1" 的参数 |  |  |  |
|---|---|---|---|
|  |  | 变量参数 |  |
| q1" |  |  |  |
|  |  |  | 的参数 |

| 常量参数支持字符串 ， 支持以下操作符 : = , == :等于判断 <> , != : 不等于判断 > , >= , < , <= :比 like , !like :相似判 ix%' in cidr , !in cidr _ _ |  |
|---|---|
|  | !in cidr _ |

| 常量参数 | 支持 | 字符串 |
|---|---|---|

| > | , | >= , | < |
|---|---|---|---|
| like |  |  |  |

| null |  |
|---|---|
| 用 | and |

可以用小括号 `(,)` 来指定条件的优先级使用 !(,) 可以对括起来的表达式执行取反操作，如： !(1=1) 结果为false 系统内置一些函数，用于一些特殊场景的判断 `Random()` : 产生一个0-1的浮点类型参数, 用于蓝绿发布等一些需要随机的场合 `Timestamp()` : 返回以毫秒计数的Unix时间戳 `TimeOfDay()` :按GMT时区，返回当前时间到当日零点的毫秒数
2. 参数类型与判断规则
表达式中支持以下类型 `STRING` : 字符串类型，支持单引号或双引号，如： `"Hello"` , `'Hello'`

| ，如 | 1001 |  |  | , |
|---|---|---|---|---|
| true |  | , | false |  |

| 于 | 等于 |
|---|---|

`STRING` : 使用字符串顺序执行判断，例如： `'123' > '10000'` 结果为true `'A123' > 'A120'` 结果为true `'' <'a'` 结果为true `NUMBER` :使用数字大小进行判断 `123 > 1000` 结果为false `100.0 == 100` 结果为true `BOOLEAN` :布尔值的判断依据为true 大于false

| true == true |  |
|---|---|
| false == false |  |
| true > false | 结 |

| 于 | 等于 | , | 不等于 |
|---|---|---|---|
| STRING |  | NUMBER |  |

| '100' == 100.0 |  |
|---|---|
| '-100' > 0 | 结果 |

| STRING | BOOLEAN |
|---|---|

例子：

| 'True' == true | 结 |
|---|---|
| 'False' == false |  |
| 'bad' == false 结 ’bad‘ != false 结 |  |

’bad‘ != true 结果为true ’0' > false 结果为false ’0‘ <= false 结果为false

| NUMBER | BOOLEAN |
|---|---|

| 等于 | ， | 不等于 | ， | 比较 |
|---|---|---|---|---|
|  | $A != null |  |  |  |

| $A |  | 为空 |
|---|---|---|
| 符串 | '' |  |
| 比较操 |  |  |

`like` , !like 操作符，可用于字符串前缀、后缀、包含的判断，判断依据为表达式仅支持右值为 `STRING` 常量的写法，如 $Path like '/users/%'

| ’%‘ 字符可用于支持前缀、后缀、与包含判断，如 $Path like '/users/%' , $Path !like '/admin/%' $q1 like '%search' , $q1 !like '%.do' $ErrorCode like '%400%' , $ErrorCode !like '%200%' |  |  |  |
|---|---|---|---|
|  | $Path like '/users/%' |  |  |
|  | $q1 like '%search' | , $q1 !like '%.do' |  |
|  | $ErrorCode like '%400%' |  | , $ErrorCode !like '%200%' |

当左值为非 `NUMBER` 或 `BOOLEAN` 类型时，会转换为 `STRING` 格式后执行判断当左值为空值 `null` 时，结果为 `false`

| in _ | cidr |
|---|---|

表达式仅支持右值为 `STRING` 常量且符合IPV4或IPV6 CIDR格式的写法，如：

```
 $ClientIP in_cidr '10.0.0.0/8'
 $ClientIP !in_cidr '0:0:0:0:0:FFFF::/96'
```

当左值类型为 `STRING` 类型时，会作为IPv4地址后进行判断当左值类型为 `NUMBER` , `BOOLEAN` 或为空时，结果为 `false` `System:CaClientIp` 参数会返回客户端Ip地址，一般使用这种方式执行判断

**3、使用案例**

随机5%的几率为真：

```
 Random() < 0.05
```

判断当前API请求的是测试环境

```
parameters:
    stage: "System:CaStage"
$CaStage='TEST'
```

自定义参数中的UserName是Admin且来源IP在 `47.47.74.0/24`

```
parameters:
  UserName: "Token:UserName"
  ClientIp: "System:CaClientIp"
$UserName = 'Admin' and $CaClientIp in_cidr '47.47.74.0/24'
```

当前请求的用户Id是1001,1098,2011中的一个，且使用HTTPS协议请求

```
pameters:
  CaAppId: "System:CaAppId"
  HttpSchema: "System:CaHttpSchema"
$CaHttpScheme = 'HTTPS' and ($CaAppId = 1001 or $CaAppId = 1098 or $CaAppId = 2011)
```

当应答StatusCode=200,包体json包体存在result_code且不为ok时

```
parameters:
  StatusCode: "StatusCode"
  ResultCode: "BodyJsonField:$.result_code"
$StatusCode = 200 and ($ResultCode <> null and $ResultCode <> 'ok')
```

**4、使用限制**

单个插件中的参数定义个数不超过16个单个表达式的字符数不超过512个字符 BodyJsonField对请求或应答应答包体的限制为16K Bytes, 超过限制后将不会生效

#### 创建插件

##### 创建IP访问控制插件

IP访问控制可以辅助API提供者设置API访问的白名单或者黑名单。创建流程如下。

## 1. 登录API网关控制台

2. 单击**开放****API >** **插件管理**菜单
3. 点击页面右上角的**创建插件**,在新的页面上，选择**组织**，**资源集**，**地域**，然后填写**插件名称**，类型选择**IP**
**访问控制**，**脚本配置**会自动加载yaml格式的插件定义模板。修改好内容后。

| 配置 | 说明 |
|---|---|

| 配置 | 说明 |
|---|---|
| type | ALLOW：支持配置 IP 或者 APPID + IP 的白名单访问，不在白名单列表的请求将会被拒绝 IP 白名单，只允许设定的调用来源 IP 的请求被允许。 APPID + IP 的白名单，此APPID只能在设定的 IP 下访问，其他 IP 来源将被拒绝。 REFUSE：可以配置 IP 黑名单，黑名单中 IP 的访问将被 API 网关拒绝。 |

IP访问控制脚本模板

```
---
```

`type: ALLOW #` 控制模式，支持白名单模式`'ALLOW'`和黑名单模式`'REFUSE'`

```
items:
- blocks:         # IP地址段
```

    - `- 78.11.12.2 #` 使用`IP`地址方式配置
    - `- 61.3.9.0/24 #` 使用`CIDR`方式配置
`appId: 219810 # (`可选) 如果配置了`appId`则该条目仅对该`AppId`生效

```
- blocks:         # IP地址段
```

    - `- 79.11.12.2 #` 使用`IP`地址方式配置
4. 插件信息填写完成后，并单击**确定**。

##### 创建流量控制插件

流控插件可以根据用户需要设置API的访问次数，防止流量过大攻击到后端服务。可通过如下步骤创建。

## 1. 登录API网关控制台

2. 单击**开放****API >** **插件管理**。
3. 单击**创建插件**。在新的页面上先选择**组织**,**资源集**,**地域**.然后填写**插件名称**，类型选择**流量控制**，修改脚本
内容。

| 配置 | 说明 |
|---|---|
| unit | 可选SECOND, MINUTE, HOUR, DAY。表示流控的时间粒度。 |
| apiDefault | 表示该API在单位时间内最大调用次数限制。一般根据后端服务能力设置。 该值必填 |
| userDefault | 每个用户的默认流控值。该值需小于或等于API流量限制值，表示访问用户在单位时间内的最大访问次数。该值可选填 |

| 配置 | 说明 |
|---|---|
| appDefault | 每个APP的默认流控值。该值需小于或者等于用户流量限制值，表示每个 APP在单位时间内的最大访问次数。该值可选填 |
| specials | 可选填。表示特殊流控。可单独为某APP或某用户设置流控值。设置后，该 APP或用户则不走默认流控，以特殊流控配置为准。 |

脚本模板

```
--unit: SECOND # 控制区间, 取值: SECOND, MINUTE, HOUR, DAY
```

`apiDefault: 1000 #` 允许的总流量值 `userDefault: 30 # (`可选)每个用户的默认流量最大值`, 0`表示不进行限制, 不能大于总流量值 `appDefault: 30 # (`可选)每个`APP`允许的流量最大值`, 0`表示不进行限制, 不能大于总流量值 `specials: # (`可选)特殊流控, 支持`"APP"`和`"USER"`两种特殊维度
    - `- type: "APP" #` 针对不同应用`(AK)`进行的流控

```
    policies:
```

    - `- key: 10123123 # AppId, AppId`的取值请在`API`网关控制台`->`应用管理`->`应用详情处查看
`value: 10 #` 特殊流控值, 不能大于总流量值

```
    - key: 10123121  # AppId
```

`value: 10 #` 特殊流控值, 不能大于总流量值
    - `- type: "USER" #` 针对不同的阿里云账户进行的流控

```
    policies:
```

    - `- key: 123455 #` 阿里云账号`ID,` 可点击阿里云控制台左上角查看账号`ID`
`value: 100 #` 特殊流控值, 不能大于总流量值
4. 插件信息填写完成后，单击**确定**。

##### 创建后端签名插件

后端签名插件用于网关和后端服务的签名认证。是由用户自己创建的一对Key和Secret，相当于您给网关颁发了一个账号密码，网关向您后端服务请求时会将密钥计算后一起传过去，您后端获取相应的字符串做对称计算，就可以对网关做身份验证。创建流程如下。

**操作步骤**

## 1. 登录API网关控制台

2. 单击**开放****API >** **插件管理**
3. 单击**创建插件**，选择**组织**，**资源集**，**地域**，然后填写**插件名称**。类型选择**后端签名**。
根据需要选择适当的配置填写。
4. 插件信息填写完成后，单击**确定**。

##### 创建跨域资源访问插件

当一个资源从与该资源本身所在的服务器不同的域或端口请求一个资源时，资源会发起一个跨域 HTTP 请求，出于安全原因，浏览器限制从页面脚本内发起的跨域请求，将结果拦截了。此时需要用跨域插件CORS 来解决。

**操作步骤**

## 1. 登录API网关控制台

2. 单击**开放****API >** **插件管理**
3. 点击**创建插件**,选择**组织**，**资源集**，**地域**，然后填写**插件名称**。类型选择**跨域资源访问**。
跨域访问模板

```
---
```

`allowOrigins: api.foo.com,api2.foo.com #` 允许的`ORIGIN,`用逗号分隔, 默认`"*"` `allowMethods: GET,POST,PUT #` 允许的方法,用逗号分隔 `allowHeaders: X-Ca-RequestId #` 允许的请求头部,用逗号分隔 `exposeHeaders: X-RC1,X-RC2 #` 允许暴露给`XMLHttpRequest`对象的头,用逗号分隔

```
allowCredentials: true # 是否允许Cookie maxAge: 172800
```

根据需要选择适当的配置填写。
4. 插件信息填写完成后，单击**确定**。

##### 创建后端路由插件

Routing插件具备根据请求的参数取值与系统参数取值，变更后端地址、路径、参数或类型的能力。可以用于租户路由，蓝绿发布，不同环境的区分等场合。

**创建路由插件**

## 1. 登录API网关控制台

2. 点击**开放****API >** **插件管理**
3. 单击**创建插件**，选择**组织**，**资源集**，**地域**，然后填写**后端路由**。类型选择**后端路由**
4. 修改脚本内容，点击**确定**

**配置方式**

配置模板可以选择json或者yaml格式的来配置您的插件，两种格式的schema相同，可以搜索yaml to json转换工具来进行配置格式的转换，yaml格式的模板见下表

```
--routes:
```

# 针对太老的客户端, 返回不再支持的应答`, ClientVersion`是`API`中的自定义参数

```
- name: MockForOldClient
  condition: "$ClientVersion < '2.0.5'"
  backend:
    type: "MOCK"
    statusCode: 400
    mockBody: "This version is not supported!!!"
```

# 蓝绿发布场景: 将5%的请求路由给蓝绿发布后端

```
- name: BlueGreenPercent05
  condition: "Random() < 0.05"
  backend:    type: "HTTP"
    address: "https://beta-version.api.foo.com"
  constant-parameters:
  - name: x-route-blue-green
    location: header
    value: "route-blue-green"
```

配置模板的根对象为routes，包含多个route对象，每个route对象用于指定一条路由，每条路由以下几个部分组成 name: X-Ca-Routing-Name表示这个路由的名称，大小写英文字母和数字，在每个插件中保持唯一， 如果命中了这条路由，后端收到的请求会包含一个名为X-Ca-Routing-Name的HTTP请求头。 condition：路由的条件表达式，如果当前的请求符合条件表达式，则本条路由命中，Routing插件会按照插件的配置顺序从上到下进行判断，并将请求路由给命中的第一条记录，并忽略后面的记录，如果您配置了多条路由记录，请仔细检查配置的顺序与您期望的逻辑一致。 backend: 后端描述，与API网关的Swagger标准保持一致，当看到这个错误时，请检查自己的backend 配置是否完整，后端在原有API的后端上覆盖backend配置后处理，如果覆盖后的backend不完整，会提示客户端X-Ca-Error-Code: I504RB，当看到这个错误时，请检查自己的backend配置是否完整， constant-parameters: query header可以自行设置路由的常量参数，常量参数会附加在命中路由的后端请求上，用于后端的业务逻辑处理，location支持header和query

**Condition条件表达式**

基本语法 Condition表达式与SQL表达式类似，基础表达形式为$A = 'A' and '$B = 'B' 参数以$开头，可以引用在API中定义的参数(API为映射与透传方式均可)，如果您在API中定义了名为 query1的参数，则$query1可以表示当前请求中的query1参数s 支持以下常量类型: STRING: 字符串类型，支持单引号或双引号，如: “Hello” INTEGER: 整数类型，如: 1001，-1 NUMBER: 浮点数类型，如: 0.1, 100.0 BOOLEAN: 布尔类型，如: true、false 可以使用and、or来连接不同的表达式可以用小括号(，)来指定条件判断的优先级 Random()作为内置函数，可以产生一个0-1的NUMBER浮点类型参数，用于随机的判断可以使用 $CaAppId 形式来引用当前请求的系统参数，系统参数不需要API中被定义即可引用，但如果您在API中定义了重名的参数，取到的值会被自定义参数覆盖，可用于路由插件的系统参数列表如下： CaStage: 当前API请求的环境, RELEASE,PRE,TEST CaDomain：当前请求的域名 CaRequestHandleTime：请求处理的UTC时间 CaAppId：请求参数的AppId CaAppKey：请求参数的AppKey CaClientIp：客户端IP CaApiName：创建时候的API名字 CaHttpScheme：请求的协议HTTP,HTTPS,WS CaClientUa: 客户端上传的UserAgent字段如果表达式中使用了不存在的参数, 如$UnknonwParameter = 1，则表达式的判断会返回false 条件表达式样例 5%的几率为真

```
Random() < 0.05
```

当前API请求的是测试环境

```
$CaStage = 'TEST'
```

自定义参数中的UserName是Admin且来源IP是47.47.74.77

```
$UserName = 'Admin' and $CaClientIp = '47.47.74.77'
```

当前请求的用户Id是1001,1098,2011中的一个，且使用HTTPS协议请求

```
$CaHttpScheme = 'HTTPS' and ($CaAppId = 1001 or $CaAppId = 1098 or $CaAppId = 2011)
```

**Backend的定义与覆盖规则**

Backend的结构与API网关导入Swagger时的结构一致。目前支持的后端类型及配置样例如下，如果插件中不需要变更后端类型，只需要变更部分设置，则不需要填写完整的字段，仅填写需要变更的即可。 HTTP

```
--backend:
  type: HTTP
  address: "http://10.10.100.2:8000"
  path: "/users/{userId}"
  method: GET
  timeout: 7000
```

HTTP-VPC

```
--backend:
  type: HTTP-VPC
  vpcId: vpc-xxxx
  vpcInstance: 172.168.1.1
  vpcInstancePort: 80
  path: "/users/{userId}"
  method: GET
  timeout: 10000
```

MOCK

```
--backend:
  type: MOCK
  mockResult: "mock resul sample"
  mockStatusCode: 200
  mockHeaders:
    - name: server
      value: mock
    - name: proxy
      value: GW
```

**限制**

插件的文本大小限制为16384字节，超过后会报错InvalidPluginData.TooLarge 单个Routing插件的条数限制为16条，超过后会报错InvalidPluginData.TooManyRoutes 单条Condition语句的大小限制为512字节，超过后会报错InvalidPluginData.ConditionTooLong 插件更新会实时生效至所有已绑定该插件的API，插件的更新频率被限制为45秒一次，超出时会报错，InvalidPluginData.UpdateTooBusy

**典型应用场景**

配置租户路由(根据AppId分配不同的后端地址)。比如：AppId为10098,10099的用户是我的VIP用户， 我希望来自这两个用户的请求路由到独立的服务器集群去，

```
--- -routes:
```

# 当调用方的`AppId`为`10098`或`10099`时, 路由至独立的地址,
# 例子中指定了`VPC`授权名为`"slbAddressForVip"`的地址

```
- name: http1
  condition: "$CaAppId = 10098 or $CaAppId = 10099"
  backend:
    type: "HTTP"
    address: "https://test-env.foo.com"
```

Stage路由(测试/预发/生产环境变更)。我不同的环境有不同的后端地址，但我希望将所有访问测试环境的API指向我的测试服务器

```
--routes:
```

# 当访问测试环境时, 将路由转向我的公网服务器

```
- name: Vip
  condition: "$CaStage = 'TEST'"
  backend:
    type: "HTTP"
    address: "https://test-env.foo.com"
```

蓝绿发布。我准备将5%的流量指向一组beta服务器地址，进行蓝绿发布

```
--routes:
```

# 蓝绿发布场景: 将5%的请求路由给蓝绿发布后端

```
- name: BlueGreenPercent05
  condition: "Random() < 0.05"
  backend:
    type: "HTTP"
    address: "https://beta-version.api.foo.com"
```

##### 创建缓存插件

通过缓存可以将后端返回的应答缓存在API网关服务层面，有效降低后端的负荷，增加平滑度
1. .** **使用方法**
仅缓存GET方法的应答可在插件中加入如下的配置来区分不同的缓存 varyByApp: 针对不同的App区分缓存 varyByParameters: 针对不同的参数取值区分缓存,从绑定的API取同名的参数 varyByHeaders: 针对不同的请求头区分缓存，如 `Accept` , `Accept-Language` 现在用户在每个Region可以使用的缓存空间为5M(按用户区分), 使用超期释放策略, 缓存满了后不缓存后续的应答。 网关遵守后端应答中的Cache-Control头的约定来处理缓存，如果后端不返回 `Cache-Control` 头，则默认缓存，使用插件中配置的duration字段作为缓存超期时间。 最长允许的超期时间为48小时(172800秒), 超过这个时间的配置无效，被视为48小时超期网关默认不处理客户端的 `Cache-Control` 头，可以通过clientCacheControl来进行配置，mode取值为

| 中的 Cache-Control 头请求中的 Cache-Control apps 配置列表中的请求的 | Cache-Control | 头 |
|---|---|---|

| Content-Type | ， | Content-Encoding |  |
|---|---|---|---|
|  | cacheableHeaders |  |  |
| , 可使用配置中的 |  |  | 配 |

2. .** **插件配置**
可以选择json或者yaml格式的来配置您的插件，两种格式的schema相同，可以搜索yaml to json转换工具来进行配置格式的转换，yaml格式的模板见下表

```
---
```

`varyByApp: false #` 是否按照访问方的`AppId`来区分缓存内容, 默认为`false` `varyByParameters: #` 按照不同的参数取值来区分缓存内容
  - `- userId #` 参数名称，如果后端参数映射为不同的名称，这里请填写映射后的参数名称
`varyByHeaders: #` 是否按照不同的请求`Header`值来区分缓存内容
  - Accept # `Accept`表示按照不同的`Accept`头来区分缓存
`clientCacheControl: #` 允许客户端通过`Cache-Control`头来影响缓存策略, 默认`off` `mode: "app" # off:` 拒绝所有端`, all:` 允许所有端`, apps:` 允许`appId`取值在`apps`列表中的端 `apps: #` 如果`mode`配置为`app`, 则允许`AppId`在以下列表中的取值
  - `- 1992323 #` 消费者`AppId,` 注意不是`AppKey`
  - `- 1239922 #` 消费者`AppId,` 注意不是`AppKey`
`cacheableHeaders: #` 允许缓存的后端`Headers,` 默认只缓存`Content-Type`和`Content-Length`
  - `- X-Customer-Token #` 允许缓存的`Header`名称
`duration: 3600 #` 默认超期的秒数
3. .** **运行规则**
当API网关命中Cache后，返回的应答中会包含头 `X-Ca-Caching: true`
4. .** **使用限制**
插件元数据的大小限制为16380个字符超过128K的应答BODY不会被缓存每个Region的总限制为30M Bytes

##### JWT认证插件

Json Web Token(RFC7519), 是一种便捷的可用于网关进行请求认证的j鉴权方案， `API` 网关可以通过托管用户的 `Public JWK` 实现对请求进行JWT认证，并将 `claims` 作为后端参数转发给后端，已方便用户简化开发后端应用的开发。

| OpenId Connect |  | 功能 |
|---|---|---|
| 上的 |  |  |

|  | JWT认证插件 |
|---|---|
| JWT认证 |  |

支持不含 `kid` 的 `jwk` 支持配置多个 `jwk` 支持直接从 `header` 或 `query` 读取Token，不需要每个API都设置Token参数当 `JWT` 以 `Authorization bearer {token}` 方式传输时，可以通过 `parameter: Authorization` , `parameterLocation: header` 方式配置已实现正确的Token读取通过添加 `preventJtiReplay: true` 配置，可支持基于 `claim:jti` 的防重放检查通过添加 `bypassEmptyToken: true` 配置，可在Token不存在时跳过验证直接转发给后端通过添加 `ignoreExpirationCheck: true` 配置, 可忽略Token的 `exp` 超期校验

| 果你配置了 | JWT认证插件 |  |
|---|---|---|
| OpenId Connect |  |  |
|  |  | 的功能 |

1. .** **获取****JWK (Json Web Key)**

|  |  | JWT认证插件 |
|---|---|---|
|  | Json Web Key Generator |  |
| Json Web Key |  |  |

```json
{
  "kty": "RSA",
  "e": "AQAB",
  "kid": "O9fpdhrViq2zaaaBEWZITz",
  "use": "sig",
  "alg": "RS256",
  "n": "qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-9do7w9X1uKFXAnqfto4TepSNuYU2bA_-tzSLAGBsR
-BqvT6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrfSPEoNU-0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr-9 FPGy8NCoIO4MfLXzJ3mJ7xqgIZp3NIOGXz- GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXRV84tIZpFVh2lmRh0h8ImK-vI42dwlD_hOIzayL1Xno2R0T-d 5AwTSdnep7g-Fwu8-sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ" }
```

这里展示的是json格式，当使用yaml格式配置插件，需要转换* `JWT`认证插件只需要配置 `Public Key` , 请妥善保存好您的 `Private Key` ，目前JWT认证插件支持以下算法：

| 签名算法 | 支持的 alg 取值 |
|---|---|
| RSASSA-PKCS1-V1 5 with SHA-2 _ | RS256, RS384, RS512 |
| Elliptic Curve (ECDSA) with SHA-2 | ES256, ES384, ES512 |
| HMAC using SHA-2 | HS256, HS384, HS512 |

当配置HS256,HS384,HS512类型的Key时, 秘钥为Base64 UrlEncode后的值, 如遇到Invalid Signature 问题, 请检查您的Key的格式是否与生成Token的Key一致
2. .** **插件配置**
您可以选择json或者yaml格式的来配置您的插件，两种格式的schema相同，请搜索 `yaml to json` 转换工具来进行配置格式的转换，yaml格式的模板见下表。 中`---` `parameter: X-Token #` 从指定的参数中获取`JWT,` 对应`API`的参数 `parameterLocation: header # API`为映射模式时可选`, API`为透传模式下必填, 用于指定`JWT`的读取位置, 仅支持`query`,`header` `preventJtiReplay: false #` 是否开启针对`jti`的防重放检查, 默认`: false` `bypassEmptyToken: false #` 当`jwt`为空时是否允许验证通过 `ignoreExpirationCheck: false #` 是否允许忽略`exp`超期时间的检查 `claimParameters: # claims`参数转换, 网关会将`jwt claims`映射为后端参数
  - `- claimName: aud # claim`名称,支持公共和私有
`parameterName: X-Aud #` 映射后参数名称

```
  location: header           # 映射后参数位置, 支持`query,header,path,formData`
```

  - `- claimName: userId # claim`名称,支持公共和私有
`parameterName: userId #` 映射后参数名称

```
  location: query            # 映射后的参数位置, 支持`query,header,path,formData`
```

#

```bash
# `Json Web Key`的`Public Key`
jwk:
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-9do7w9X1uKFXAnqfto4TepSNuYU2bA_-tzSLAGBsR-Bq
vT6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrfSPEoNU-0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr-9FPG y8NCoIO4MfLXzJ3mJ7xqgIZp3NIOGXz- GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXRV84tIZpFVh2lmRh0h8ImK-vI42dwlD_hOIzayL1Xno2R0T-d 5AwTSdnep7g-Fwu8-sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ
```

#
# 可以支持配置多个`JWK,` 可以与`jwk`字段一起配置
# 配置多个`JWK`时`,kid`是必选的,如果`JWT`中没有提供`kid,`则校验失败

```
jwks:
```

  - `- kid: O9fpdhrViq2zaaaBEWZITz #` 在只配置一个`JWK`时`,kid`是可选的,但如果`JWT`中包含了`kid,`网关会校验k
`id`的一致性

```
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5v....
```

  - `- kid: 10fpdhrViq2zaaaBEWZITz #` 在只配置一个`JWK`时`,kid`是可选的,但如果`JWT`中包含了`kid,`网关会校验k
`id`的一致性

```
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5v...
```

|  | JWT认证插件 |  | 会使用配置的 | parameter | 与 | parameterLocation |  |
|---|---|---|---|---|---|---|---|
| : X-Token |  |  |  |  |  |  |  |

如果API上配置了与 `paramter` 配置同名的参数时， `paramterLocation` 可以忽略，否则会在调用时报错

| 如果使用Authorization头传输Token，如: Authorization bearer {token} Authorization , parameterLocation: header 方式配置，JWT插件可以正当配置了 preventJtiReplay: true 时，插件会使用 claims 中的 jti 字 |  |  | Authorization bearer {token} |
|---|---|---|---|
| Authorization |  | parameterLocation: header |  |
| 当配置了 | preventJtiReplay: true |  |  |

当配置了 `bypassEmptyToken: true` 时，当Token参数为空时，允许跳过检查，直接转发请求给后端当配置了 `ignoreExpirationCheck: true` 时，会跳过 `exp` 的超期检查，否则网关会检查Token是否已超期如果需要API网关将Token中的 `claims` 转发给后端应用，可以通过 `tokenParameters` 字段配置转发参数 `claimName` : token中claim的名字, 支持配置 `kid` `parameterName` : 转发到后端的参数名称 `location` : 转发到后端的参数位置，支持 `header` , `query` , `path` , `formData` 当配置为 `path` 时，后端path必须包含同名的参数，如 `/path/{userId}` 当配置为 `formData` 时，仅支持在参数映射且包体为 `form` 格式下才能正确映射到后端的form 中

| jwk |  | 字 |
|---|---|---|
| 含 | kid |  |
| kid |  | 的 |

3. .** **校验规则**

| paramater |  | 与 | parameterToken |
|---|---|---|---|
| 需要配置 |  |  |  |

当配置多个Key是的选择原则为优先选择与请求Token中 `kid` 一致的Key来进行签名校验不含 `kid` 的Key只能配置一个，当不存在 `kid` 与请求Token一致的情况时，使用不含 `kid` 的 Key执行签名校验如果没有配置不含 `kid` 的Key，如果请求Token中未包含 `kid` ，或通过 `kid` 未匹配到Key则报

```
错 A403JK
```

如果Token中包含了 `iat` , `nbf` , `exp` 字段，JWT插件会校验时间字段的合法性默认情况下，API网关会校验Token的 `exp` 过期时间字段，如果希望跳过 `exp` 的超期检查，需要配

```
置 ignoreExpirationCheck: true
```

如果配置了 `tokenParameters` 字段转发，当Token的 `claims` 中包含对应的字段时， `claim` 字段会转发给后端，不存在的 `claim` 不会转发
4. .** **配置案例**

**4.1. 配置单个JWK**

```
---
```

`parameter: X-Token #` 从指定的参数中获取`JWT,` 对应`API`的参数 `parameterLocation: header # API`为映射模式时可选`, API`为透传模式下必填, 用于指定`JWT`的读取位置, 仅

```
支持`query`,`header`
```

`claimParameters: # claims`参数转换, 网关会将`jwt claims`映射为后端参数
  - `- claimName: aud # claim`名称,支持公共和私有
`parameterName: X-Aud #` 映射后参数名称

```
  location: header         # 映射后参数位置, 支持`query,header,path,formData`
```

  - `- claimName: userId # claim`名称,支持公共和私有
`parameterName: userId #` 映射后参数名称 `location: query #` 映射后的参数位置, 支持`query,header,path,formData` `preventJtiReplay: false #` 是否开启针对`jti`的防重放检查, 默认`: false`
#

```bash
# `Json Web Key`的`Public Key`
jwk:
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5vGsOmaorPDzHUubBmZZ4UXj-9do7w9X1uKFXAnqfto4TepSNuYU2bA_-tzSLAGBsR-Bq
vT6w9SjxakeiyQpVmexxnDw5WZwpWenUAcYrfSPEoNU-0hAQwFYgqZwJQMN8ptxkd0170PFauwACOx4Hfr-9FPG y8NCoIO4MfLXzJ3mJ7xqgIZp3NIOGXz- GIAbCf13ii7kSStpYqN3L_zzpvXUAos1FJ9IPXRV84tIZpFVh2lmRh0h8ImK-vI42dwlD_hOIzayL1Xno2R0T-d 5AwTSdnep7g-Fwu8-sj4cCRWq3bd61Zs2QOJ8iustH0vSRMYdP5oYQ
```

**4.2. 配置多个JWK**

```
--parameter: Authorization # 从Authorization头中获取Token parameterLocation: header # 从Authorization头中获取Token
```

`claimParameters: # claims`参数转换, 网关会将`jwt claims`映射为后端参数
  - `- claimName: aud # claim`名称,支持公共和私有
`parameterName: X-Aud #` 映射后参数名称

```
  location: header         # 映射后参数位置, 支持`query,header,path,formData`
```

  - `- claimName: userId # claim`名称,支持公共和私有
`parameterName: userId #` 映射后参数名称 `location: query #` 映射后的参数位置, 支持`query,header,path,formData` `preventJtiReplay: true #` 是否开启针对`jti`的防重放检查, 默认`: false`

```
jwks:
```

  - `- kid: O9fpdhrViq2zaaaBEWZITz #` 配置多个`JWK`时，需要使用不同的`kid`

```
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5v....
```

  - `- kid: 10fpdhrViq2zaaaBEWZITz #` 配置多个`JWK`时，需要使用不同的`kid`

```
  kty: RSA
  e: AQAB
  use: sig
  alg: RS256
  n: qSVxcknOm0uCq5v...
```

5. .** **相关错误码**

| Status | Code | Message | Description |
|---|---|---|---|
| 400 | I400JR | JWT required | 未找到JWT参数 |
| 403 | S403JI | Claim jti is required when preventJtiReplay:t rue | 当在 JWT授权插件中配置了防重放功能时，请求未提供有效的 jti |
| 403 | S403JU | Claim jti in JWT is used | 当在 JWT授权插件中配置了防重放功能时，请求提供的 jti 已被使用 |
| 403 | A403JT | Invalid JWT: ${Reason} | 请求中提供的 JWT 非法 |
| 400 | I400JD | JWT Deserialize Failed: ${Token} | 请求中提供的 JWT 解析失 |
| 403 | A403JK | No matching JWK, kid:${kid} not found | 请求 JWT 中的 kid 没有匹配的 JWK |
| 403 | A403JE | JWT is expired at ${Date} | 请求中提供的 JWT 已过期 |
| 400 | I400JP | Invalid JWT plugin config: ${JWT} | JWT授权插件配置错误 |

|  |  | preventJtiReplay:t | 配求 |
|---|---|---|---|
|  | rue |  |  |

|  | JWT |
|---|---|
| kid |  |
| JWK |  |

| X-Ca-Error-Code 头中获出现 A403JT 或 I400JD |  |  |  | 头中获 |
|---|---|---|---|---|
|  |  |  | I400JD |  |
| 出现 | A403JT | 或 |  |  |

6. .** **使用限制**
插件元数据的大小限制为**16380**个字符。 转发参数列表最大限制为**16**个, `claimName` 与 `parameterName` 长度不超过**32**个字符, 仅支持[A-Zaz0-9-_]。 JWK的 `alg` 支持列表为: RS256, RS384, RS512, ES256, ES384, ES512, HS256, HS384, HS512。

##### 访问控制插件

1. .** **概述**
访问控制插件可以根据请求参数或上下文，来执行条件判断，用于过滤不希望传递到后端的请求，参考参数与条件表达式的使用来了解如何定义参数和使用条件表达式。
2. .** **配置说明**
在这个例子中假设我们的API请求Path为 `/{userId}/...` , API使用JWT认证，JWT中有userId和 userType两个claim, 我们这个插件的校验条件为： 当userType=admin时，允许所有的路径。 当userType=user时，仅允许/{userId}路径一致的请求。

```
---
```

#
# 在这个例子中假设我们的`API`请求`Path`为`/{userId}/...`,
# API使用`JWT`认证，`JWT`中有`userId`和`userType`两个`claim`
# 我们这个插件的校验条件为
# - 当`userType=admin`时，允许所有的路径，
# - 当`userType=user`时，仅允许`/{userId}`路径一致的请求

```
parameters:
  userId: "Token:userId"
  userType: "Token:userType"
  pathUserId: "path:userId"
```

#
# 关于`Rules`的处理规则，依次演算条件，按照返回值为`true`或者`false`，处理`ifTrue`的逻辑或`ifFalse`
的结果
# `ALLOW`会直接判断为成功，而`DENY`则会直接返回错误代码给客户端，
# 如果没有触发`ALLOW`或`DENY`逻辑，则执行下一条

```xml
rules:
  - name: admin
    condition: "$userType = 'admin'"
    ifTrue: "ALLOW"
  - name: user
    condition: "$userId = $pathUserId"
    ifFalse: "DENY"
    statusCode: 403
    errorMessage: "Path not match ${userId} vs /${pathUserId}"
    responseHeaders:
      Content-Type: application/xml
    responseBody:
      <Reason>Path not match ${userId} vs /${pathUserId}</Reason>
```

3. .** **相关错误码**

| 错误代码 | Http状态码 | Message | 描述 |
|---|---|---|---|
| A403AC | 403 | Access Control Forbidden by ${RuleName} | 被授权控制插件阻止。 |

4. .** **使用限制**
参数定义个数不超过**16**个。 单个表达式的字符数不超过**512**个字符。 插件配置大小限制为**16380**字符的文本。 最大允许的 `rules` 条数为16条。

##### 错误码映射插件

1. .** **概述**
错误码映射插件用于将后端应答中返回的非正常请求，映射为客户端期望的错误应答的场景。
2. .** **快速开始**
请先参考下面的例子, 某后端的的返回中, HTTP应答码为200, 但错误信息包含在包体中json字段中。

```json
HTTP 200 OK Content-Type:application/json {"req_msg_id":"d02afa56394f4588832bed46614e1772","result_code":"ROLE_NOT_EXISTS"}
```

在这个场景中，客户端期望得到非200的应答，但希望通过不修改后端的方式实现

```
HTTP 404 X-Ca-Error-Message: Role Not Exists, ResultId=d02afa56394f4588832bed46614e1772 ---
```

# 参与映射的字段

```
parameters:
  statusCode: "StatusCode"
  resultCode: "BodyJsonField:$.result_code"
  resultId: "BodyJsonField:$.req_msg_id"
```

# 映射条件

```
errorCondition: "$statusCode = 200 and $resultCode <> 'OK'"
```

# 错误码字段

```
errorCode: "resultCode"
```

# 映射项

```
mappings:
  - code: "ROLE_NOT_EXISTS"
    statusCode: 404
    errorMessage: "Role Not Exists, RequestId=${resultId}"
  - code: "INVALID_PARAMETER"
    statusCode: 400
    errorMessage: "Invalid Parameter, RequestId=${resultId}"
```

# 默认映射(可选)

```
defaultMapping:
  statusCode: 500
  errorMessage: "Unknown Error, ${resultCode}, RequestId=${resultId}"
```

|  |  |  | result code _ |
|---|---|---|---|
| result code _ |  | 作为错误码字段执 |  |
| 4应答，而 |  |  |  |

3. .** **插件配置与映射规则**

**3.1. 插件配置**

错误映射插件配置使用 `json` 或 `yaml` 格式配置，各个字段的详细说明如下:

| parameters |  | (必选 |
|---|---|---|
| errorCondition |  |  |
| errorCode | (可选 |  |

| true |  | 时， |
|---|---|---|
| 中的 | code |  |

`mappings` (必选): 用于指定映射记录列表, 网关将会用符合错误代码或错误条件记录重新构造返回应答，详细字段为 `code` (可选): 唯一，设置这个字段是 `codeParameter` 字段为必选, 当错误代码与 `code` 字段一致时，执行当前映射记录 `condition` (可选): 错误条件表达式, 当表达式演算为 `true` 时，执行当前映射记录

| 映射记录 |  | 的 |
|---|---|---|
| 前 | 映射记录 |  |

| errorMessage |  |  |
|---|---|---|
|  | 头及日志的 |  |

`responseHeaders` (可选): 以Map方式配置，用于设置当前映射记录的应答头 `responseBody` (可选): 用于覆写当前映射记录的应答包体 `defaultMapping` (可选): 默认映射记录，如果 `mappings` 中的所有记录均未命中, 则使用本条记录作为应答

| statusCode |  |  |
|---|---|---|
| errorMessage |  |  |
|  | 头及日志的 |  |

| 映射记录 |  | 的 |
|---|---|---|
| 前 | 映射记录 |  |

`responseHeaders` (可选): 以Map方式配置，用于设置当前映射记录的应答头 `responseBody` (可选): 用于覆写当前映射记录的应答包体配置规则: `mappingCondition` , `mappings[].condition` 中的条件表达式使用的参数，与 `parameters` 字段中定义的字段必须对应，否则会报错，关于参数定义与条件表达式，参考参数与条件表达式的使用

| 为 | parameters |  |
|---|---|---|
| condition |  | 必 |

|  | parameters |
|---|---|
| 换, 字段取值来自 |  |
| responseHeaders |  |
| responseBody |  |
| responseHeaders |  |

`defaultMapping` 没有配置时，错误码映射不生效，透传后端应答

**3.2. 映射参数**

映射参数可通过如下的方式在 `parameters` 参数中配置为键值对，其中键作为变量名定义，值可以使用 `Location:Name` 的方式配置，表示从当前应答或系统上下文的特定位置中读取。

```
---
```

# 参与映射的字段

```
parameters:
  statusCode: "StatusCode"
  resultCode: "BodyJsonField:$.result_code"
  resultId: "BodyJsonField:$.req_msg_id"
```

错误码映射目前支持以下位置的参数。

| 位置名称 | 适用范围 | 说明 |
|---|---|---|
| StatusCode | 应答 | 后端的HTTP应答码，如: 200 , 400 |
| ErrorCode | 应答 | API网关系统错误码 |
| ErrorMessage | 应答 | API网关系统错误消息 |
| Header | 应答 | 使用 Header:{Name} 获取名字为 {Name} 的HTTP头的第一个值 |
| BodyJsonField | 应答* | 使用 BodyJsonField: {JPath} 以 JSONPath 方式获取请求/应答包体中的JSON字段值 |
| System | 应答 | 使用 System:{Name} 获取名字为 {Name} 的系统参数值 |
| Token | 应答 | 当处于 jwt , oauth2 授权场景是，使用 Token:{Name} 获取 token中名字为 {Name} 的值 |

|  |  | BodyJsonField: |
|---|---|---|
|  | {JPath} |  |

`ErrorCode` 和 `ErrorMessage` 会返回API网关的系统错误码与系统错误信息，请参考错误代码表文档。 使用 `BodyJsonField` 可以使用JSONPath来提取后端返回json的值, 但如果后端应答的包体大小超过**15360 Bytes**则这个字段将会无法提取到值，得到的是空值 `null`

**3.3. 执行规则**

i. 根据 `parameters` 中配置的参数列表，从应答及系统上下文中获取当前的参数表 i. 依据步骤1 得到的参数表，执行 `errorCondition` 中配置的条件表达式，为 `true` 则继续执行， `false` 不生效 i. 如果配置了 `errorCode` 字段, 则获取 `errorCode` 字段的值, 并寻找与 `mappings` 中 `code` 匹配的映射记录, i. 如果步骤3没有匹配到映射记录，则依次执行 `mappings` 字段配置了 `condition` 的映射记录 i. 如果步骤3或4中匹配到了映射记录，根据对应的配置构造应答，否则构造默认应答

**3.4. 系统错误的映射及日志**

API网关系统错误码出现在网关的检查、校验、流控、插件处理等场合，参考错误代码表文档，使用 `Err` `orCode` 作为映射参数，可以支持对系统错误码的映射，可用于诸如：客户端仅支持200应答，但希望将被限流的429应答映射为200应答的场景。 当出现系统错误时，位置为 `StatusCode` , `Header` , `BodyJsonField` 等来自应答的字段取值都将为 `null` ，在写条件表达式时需要注意，未出现系统错误时 `ErrorCode` 位置的取值为 `OK` 。

| 错误码映射插件 |  | 改写 |
|---|---|---|
| 志中的 | statusCode |  |

4. .** **配置示例**

**4.1. 映射包体错误码**

映射

```
---
```

# 参与映射的字段

```
parameters:
  statusCode: "StatusCode"
  resultCode: "BodyJsonField:$.result_code"
  resultId: "BodyJsonField:$.req_msg_id"
```

# 映射条件

```
errorCondition: "$statusCode = 200 and $resultCode <> 'OK'"
```

# 错误码字段

```
errorCode: "resultCode"
```

# 映射项

```
mappings:
  - code: "ROLE_NOT_EXISTS"
    statusCode: 404
    errorMessage: "Role Not Exists, RequestId=${resultId}"
  - code: "INVALID_PARAMETER"
    statusCode: 400
    errorMessage: "Invalid Parameter, RequestId=${resultId}"
```

# 默认映射(可选)

```
defaultMapping:
  statusCode: 500
  errorMessage: "Unknown Error, ${resultCode}, RequestId=${resultId}"
```

5. .** **使用限制**
参数定义个数不超过**16**个。 单个表达式的字符数不超过**512**个字符。 `BodyJsonField` 位置的字段对应答包体的限制为**16380 Bytes**, 超过后直接返回空值。

| 为 | 16380 | 字 |
|---|---|---|
| condition |  |  |

#### 绑定 API

创建插件后，您需要将其绑定到API上，才会对已绑定的API起作用。

**背景信息**

您可以将某插件绑定于多个API，插件对每一个API单独生效。API上每种插件只能绑定一个。当您绑定API 时，如果该API已经绑定了一个相同类型的插件，您的此次操作将替换之前的插件，实时生效。

## 1. 登录API网关控制台

2. 单击**插件管理**。
3. 选择所需的插件并单击右侧的操作图标，选择**绑定****API**。
4. 选择所要绑定的API所在的环境和分组。
5. 勾选要添加的API，单击中间的右移图标，将API加入待绑定列表，并单击**确定**。

#### 删除插件

您可以删除已经创建的插件。

## 1. 登录API网关控制台

2. 单击**插件管理**页签。
3. 选择所需的插件并单击右侧的操作图标，选择**删除插件**。
4. 在弹出的确认对话框中，单击**确定**。

#### 解绑插件

您可以解除API和插件的绑定关系。

## 1. 登录API网关控制台

2. 单击**插件管理**页签。
3. 选择要解绑的插件，单击右侧的操作图标，选择**查询详情**，进入API定义页面。
4. 单击对应插件右侧的操作图标，选择**解绑**。
5. 在弹出的确认对话框中，单击**确定**。

## 监控管理

### 云监控预警

API网关结合云监控产品，提供了可视化的实时监控和预警。您可以查看账号下API的调用统计信息，包括调用量、流量、后端响应时间、错误分布等多个维度、多种时间单位的数据统计结果

**查看API监控信息**

需要到云监控产品页面下，查询本账号API的调用信息
1. 点击**产品** > **监控运维** > **云监控** **CMS**
2. 在左侧菜单选择**API****网关**
3. 在监控列表中选择要监控的API，点击API右侧的**监控图表**
监控图表含义： code2xx 表示API返回的HttpStatusCode为2xx的请求次数，如：200，一般2xx表示后端请求成功。 code4xx 表示API返回的HttpStatusCode为4xx的请求次数, 如：404，一般4xx表示客户端错误。 code5xx表示API返回的HttpStatusCode为5xx的请求次数, 如：500，一般5xx表示服务端错误。 流入带宽表示API请求的流量大小流出带宽表示API响应的流量大小响应时间表示API后端服务响应时间（不包含API网关的延迟，网关延迟一般在3~5ms） 总体请求次数表示该API总的请求次数

**配置API预警**

通过在云监控页面配置API报警规则，可以实现较实时的API报警。
1. 在API网关监控列表页面，找到想配置监控的API
2. 点击API右侧的**报警规则**，进入报警规则配置页面
3. 点击**创建报警规则**，在弹出的页面中产品选择 API网关, 资源范围选择对应的API，接下来创建规则
4. 点击**添加规则描述**, 填写规则名称,指标名称,比较,阈值和报警级别后点击**确定**。
5. 选择**报警联系人组**，是从组织关系中选择。
如果要监控API的服务状态，建议监控code5xx。

**说明**

### API网关监控

API网关控制台提供了一个API调用的统计信息概览页面。除了云监控上监控API的调用信息。您还可以通过全局监控页面查看API的调用统计信息。

**重要**

：只能查看本账号自己拥有的分组和API的调用情况，不属于该账号下的资源（不是该资源的 owner），则无权查看，所以root账号也不能查看dashboard数据。

**总览监控**

1. 在API网关控制台页面，点击菜单，在实例页面，点击**全局监控**，进入当前账号的总览监控页面。
2. 通过选择不同的时间单位（页面默认30分钟），查看该时间段内，本账号下的分组或域名的调用情况。
可查看监控指标： 请求数：可查看此账号的总请求数、平均每秒总请求数、平均后端延时、平均整体延时。 流量：可查看此账号的每秒请求流量、每秒应答流量、平均请求大小、平均应答大小。 返回码：可查看此账号的返回码以及每个返回码的请求数和占比。 错误码：可查看此账号的错误码以及错误码的请求数和占比。 时延：可查看此账号某个时延范围内的请求数和占比。 另外还可以查看各分组绑定的域名，并且可根据归属部门、请求数、每秒请求数、返回码、平均后端延时对分组进行排序。

**分组监控**

在总览页点击分组名称即可进入分组监控，通过选择不同的时间单位（页面默认30分钟），查看该时间段内，此分组以及此分组下的API的调用情况。 可查看监控指标： 请求数：可查看分组的总请求数、平均每秒总请求数、平均后端延时以及平均整体延时。 流量：可查看分组的每秒请求流量、每秒应答流量、平均请求大小以及平均应答大小。 返回码：可查看分组的某个时间段的返回码以及每个返回码的请求数和占比。 错误码：可查看分组某个时间段的错误码以及错误码的请求数和占比。 时延：可查看分组某个时延范围内的请求数和占比。 另外还可以查看此分组下所有API的请求路径，并且可根据请求数、每秒请求数、返回码、时延对API进行排序。

**API监控**

在分组监控页点击API名称即可进入API监控，通过选择不同的时间单位（页面默认30分钟），查看该时间段内，此API的调用情况。 可查看监控指标： 请求数：可查看API的总请求数、平均每秒总请求数、平均后端延时以及平均整体延时。 流量：可查看API的每秒请求流量、每秒应答流量、平均请求大小以及平均应答大小。 返回码：可查看API的某个时间段的返回码以及每个返回码的请求数和占比。 错误码：可查看API某个时间段的错误码以及错误码的请求数和占比。 时延：可查看API某个时延范围内的请求数和占比。

### 配置全局监控账号

API网关提供了全局监控功能，可配置全局管理员，此管理员可以全局查看所有部门下的API调用情况。 配置全局监控，需先配置全局管理员，目前通过数据变更的方式配置。将管理员对应的一级部门的 PrimaryKey作为uid，配置到网关里面。 步骤1：获取数据库用户名及密码登录飞天基础运维平台，找到project为apigateway的集群，点击进入dashboard。在集群资源里找到 Type为db的集群，右键点击Result显示更多，即可查看数据库详情。其中db_user为数据库用户名，db_host为数据库地址，db_password为数据库密码，db_port为数据库端口，db_name为数据库名称。 步骤2：获取全局管理员对应的一级部门的PrimaryKey 登录阿里云控制台，选择企业——组织管理——选择全局管理员——获取accesskey，即可获取 PrimaryKey。 步骤3：登录数据库配置全局管理员在飞天基础运维平台登录serverRole为apigateway.ApigatewayOpenAPIForClassic的宿主机，根据步骤1与步骤2获取的信息登录数据库并配置全局管理员。相关命令如下

```
mysql -u api_gateway -hapi-gateway.mysql.minirds.intra.env66.shuguang.com -pemSJzawsl
```

`70ybhll -P 3157 #`登录数据库

```
use api_gateway; #选择api_gateway数据库 INSERT INTO `ca_stastic_config`( `gmt_create` , `gmt_modified` , `config_key` , `config _value` , `is_removed` ) VALUES(NOW(),NOW(),'AdminUidConfig','["xxx"]', 0); #配
```

置全局管理员，将`PrimaryKey`作为`uid`替换以下语句中的`xxx,`可配置多个`uid`

```
UPDATE `ca_stastic_config` SET `config_value` = '["xxx"]' WHERE `config_key` = 'AdminUi dConfig'; #更新配置
```

步骤4：使用全局管理员查看全局监控登录 API网关控制台，点击实例页面——全局监控，可以看到监控页面，选择对应的统计时间进行查看，可根据分组和调用域名进行过滤。

**注意：默认只能展示本部门一级组织下的分组的统计，只有配置的全局管理员可以查看所有部门的统计信**

**息。**

## 高级使用

### 自定义日志的业务参数

API网关提供了Hack模式，支持用户通过Hack配置方法配置，在日志中记录用户调用的请求和响应参数。

**操作步骤**

## 1. 登录API网关控制台

2. 单击左侧导航栏的**开放****API >** **分组管理**
3. 点击特定的分组名称，进入分组详情页面。
4. 单击右上角的**修改基本信息**
5. 在分组的**描述**字段里面，增加下面这一行内容。

```
logConf:reqBody=1024,reqHeaders,reqQuery,respHeaders,respBody=1024
```

**说明**

这一行一定要是单独的一行，否则配置不成功。 您也可以自己修改后面的内容，例如去掉respHeaders，这样日志中就不会记录response header的内容。 reqBody=1024这个表示request body最多在日志中存放1024个字符，超出这个长度会被截断。
6. 到日志服务查询日志页面，检查是否已经记录上对应的字段日志。

### 配置API网关的LOG日志

#### 初始化API网关的LOG默认配置

API网关默认配置了Gateway的调用日志同步到飞天基础运维平台自带的LOG上。但是账号需要登录到飞天基础运维平台日志服务控制台才能激活，激活后才可以使用。
1. 登录飞天基础运维平台，在左侧点击工具——运维工具——机器运维工具，然后在页面左侧点击跳转
2. 在跳转的页面选择**集群**，然后在**Project**下拉列表中选择apigateway。
集群运维界面
3. 找到筛选出的项目，将鼠标放在
图标上，选择**Dashboard**。
4. 在集群资源下找到Name值为apigateway-sls，Type值为accesskey这行，右键选择Result列的**显示更**
多，查看accesskey-id和accesskey-secret。
5. 使用获取的accesskey-id和accesskey-secret登录飞天基础运维平台日志服务控制台。
飞天基础运维平台地址：http://portal.${region}.sls.${internet-domain}，其中region和internetdomain可以从飞天基础运维平台中kv.conf文件中获取。 i. 单击apigateway集群的**集群配置文件**。 ii. 单击**kv.conf****文件**查看region和internet-domain信息。

**说明**

登录系统几分钟后，API网关的LOG服务自动化配置就会完成。

#### 配置网关的日志到用户的LOG

如果您不想用飞天基础运维平台侧的LOG和固定账号，您可以通过日志服务产品，自己创建一个LOG的 project，然后通过配置，将API网关日志投递到您自己的LOG上。

**背景信息**

您需要自己创建LOG project并配置logstore、机器组等。具体操作方法如下：

**1 登录API网关gateway机器终端**

1. 登录飞天基础运维平台，找到project为apigateway的集群。
2. 在dashboard页面查看**服务实例列表**，找到服务实例为apigateway一行。
3. 单击**详情**操作，进入**服务角色列表**，找到服务角色为ApigatewayLite#。
4. 单击**详情**，找到**机器信息**列表,登录gateway机器终端。

**2 配置用户区LOG日志**

1. 打开日志服务的管控页面，在跳转页面上选择**区域**和对应的**部门**，单击**SLS**按钮。
2. 单击**创建****Project**，填写相关信息，点击确认
3. 确认后，在进入的logstore列表页面，创建一个Logstore。
4. 之后进入接入数据页，在页面选择**分隔符**-**文本日志**。
5. 参考第一节的步骤在飞天基础运维平台进入以ApigatewayLite开头的SR的容器执行创建机器组页的安装
命令。看到install logtail success，则表示安装成功。
6. 确认安装完毕后，正式创建机器组，填写相关信息。机器组名称自定义，IP地址填写以ApigatewayLite
开头的SR的容器docker的IP地址（进入docker内查看），将所有容器IP加进去。
7. 配置机器组，点击确认会自动进行心跳检查，心跳检查OK后，会自动跳转下一步。
8. 进入logstail配置列表页面。数据源相关配置，按照如下内容填写，然后单击**下一步**。

| 配置 | 配置值 |
|---|---|
| 配置名称 | gateway request log _ _ |
| 日志路径 | /alidata/www/logs/java/cloudapi- gateway/logs/request user.log _ |
| 模式 | 分隔符模式 |

| 日志样例 | 2019-08-15 14:25:05\|CC7C526B-C915-44F1-93A2- F44DBBE35177\|b2909c9fa66146f19baf2bd8f4 709ab8\|integration root\|e4032f87ace14cc _ 6965cf5352a9637a6\|RELEASE\|0619f7763b004 fc3a16a41dd712ce8d7\|biz1 anonymous\|10.4 _ .21.241\|\|\|b2909c9fa66146f19baf2bd8f4709 ab8.apigateway.env4b.shuguang.com\|POST\| /biz1/anonymous\|403\|A403JT:Invalid JWT: deserialized JWT failed\|\|1453964555641148\|cn-qingdao- env4b-d01\|2019-08- 15T06:25:05Z\|614\|0\|0\|A403JT\|http\|\|\|cf80 2da1-54d0-49b8-b77c-2b20b172d90a\|\| {"X-JWT-Token":"bad jwt token"}\|a=%21111\|\|\|\|\|\|\| |
|---|---|
| 分隔符 | 竖线 |

9. 单击**下一步**，后面即可采用默认配置，一直到创建完成。
0. 配置完成后，可以到API网关控制台多调用几次API，然后在日志服务检查是否配置成功。

### 跨用户使用VPC授权

当用户后端服务在VPC内时，需要通过VPC授权的方式配置后端地址。默认情况下，后端VPC所有者必须和 API的所有者是同一个用户，从V3.8.1版本开始，API网关提供了2个内部接口，允许VPC所有者将自己的

#### VPC用户授权其他用户使用

因为涉及到跨VPC使用，考虑到安全性，需要VPC的所有者调用接口明确进行授权后，API提供者才可以使用该VPC。API网关的openAPI机器内置了Aliyun CLI 工具，用户可以通过该工具完成授权。调用方法如下：

**操作步骤**

1. 登录飞天基础运维平台，找到project为apigateway的集群。
2. 在dashboard页面查看**服务实例列表**，找到**服务实例**为**apigateway**一行。
3. 单击**详情**操作，进入**服务角色列表**，找到**服务角色**为**ApigatewayLite#**。
4. 单击**详情**，找到**机器信息**列表。
5. 随机登录该ServerRole下的一台机器，进入容器。
6. 配置CLI的调用AK。执行命令如下：
`aliyun configure --profile vpctest //`新增`AK`配置，`profile`后面的`vpc`为`profileName`，可自定义， 回车后根据提示完成`AccessKeyId` 和 `AccessSecret`配置。 `aliyun configure list //`查看`config`配置,看上面的`profile`是否已经添加。
7. 执行如下命令进行授权。

```
aliyun cloudapi AuthorizeVpc --VpcId vpc-tb5mfcwx3s4zqctzw**** --TargetUserId 1475462 14349**** --endpoint apigateway.cn-qingdao-env11-d01.inter.env11b.shuguang.com --force --profile vpctest
```

**说明**

以上命令中 endpoint需要到天基**报表** > **服务注册变量**中找apigateway服务中的 apigateway.openapi.endpoint 变量的值。profile 的值也需要根据实际情况替换。 该命令完成将Vpc（vpc-tb5mfcwx3s4zqctzw19w2）授权给1475462143497330这个用户使用。您需要根据实际需要完成参数值替换。 操作成功示例：

#### API配置

授权完成后，接下来是API所有者进行API的设置，需要特殊配置的地方是定义API后端服务部分。因为 Apsara Stack控制台不能选择他人的VPC ID，所以此处需要以特殊方式配置API后端地址。

**背景信息**

VPC ID需选择不使用VPC授权。 后端服务地址部分需要以 http(s)://{后端服务ip}.{vpcId}.gateway.vpc:{port} 的格式填写。其中{} 中内容需要根据实际情况填写。示例如下：

```
http://192.168.XX.XX.vpc-tb5mfcwx3s4zqctzw****.gateway.vpc:8080
```

## 1. 登录API网关控制台

2. 单击**API**页签。
3. 选择需要查看的API，单击右侧的操作图标。
选择**查询详情**。您可以看到当前所选API的定义信息。 选择**修改**，按照您的需要进行编辑并单击**修改**。 编辑API定义的流程和创建API定义一致，详细信息参见创建API。如果您想放弃编辑，可以点击页面顶部的返回图标。

### 使用HTTPS访问API

**背景信息**

API网关通过域名来定位到一个唯一的API分组，再通过Path+HTTPMethod确定唯一的API。网关会给每个分组分配一个二级域名，您可以直接使用该域名调用API，但是该域名默认不支持HTTPS访问，只支持 http。而且某些客户不想用分组二级域名，想用自己的域名调用API，本文将讲述以上两种的支持方法。

**分组二级域名支持HTTPS访问**

让分组二级域名支持HTTPS访问，需要在网关上配置一个专有云二级域名的泛域名证书（证书需要自己准备）。配置方法如下
1. 准备网关二级域名配置文件
修改下面这段配置，将*.wildcard.com，修改为您的泛域名(一般为 *.apigateway.${internetdomain}, ${internet-domain}这个变量在Tianji配置文件kv.conf里面可以找到)，比如您最终对外提供服务的域名为abc.alibaba.com，那么就替换成*.alibaba.com。将修改后的内容配置保存为 wildcard.conf，将证书公钥文件命名为wildcard.crt，将证书私钥文件命名为wildcard.key。

```
server {
    listen              443 http2 ssl;
    server_name         *.wildcard.com;
    limit_req           zone=perserver_req burst=100;
    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers         ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA:AES128-GCM-S
HA256:AES128-SHA256:AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:EC DHE-RSA-AES256-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-AES128-SHA256 :!aNULL:!eNULL:!RC4:!EXPORT:!DES:!3DES:!MD5:!DSS:!PKS;
    ssl_certificate     /home/admin/cai/certs/wildcard.crt;
    ssl_certificate_key /home/admin/cai/certs/wildcard.key;
    ssl_session_cache   shared:SSL:10m;
    ssl_session_timeout 10m;
    location / {
        proxy_pass http://gateway_upstream;
    }
}
```

2. 将配置文件放入指定位置
将wildcard.conf复制到apigateway.ApiGatewayLite# 对应的宿主机/alidata/sites/conf文件夹内， 将wildcard.crt、wildcard.key复制到apigateway.ApiGatewayLite#对应的宿主机/alidata/sites/certs文件夹内。
3. 生效证书
进入apigateway.ApiGatewayLite# SR的容器内：执行 `/home/admin/cai/bin/nginxctl reload`

**说明**

第2，3步，apigateway.ApiGatewayLite# SR下所有的机器都要执行。

**用自定义域名支持HTTPS访问API**

当用户需要用自己的域名访问API时，步骤如下：
1. 给分组绑定域名
i. 进入API网关控制台，点击左边菜单的分组管理，进入分组列表页面，然后点击要绑定域名的分组，进入分组详情页面。 ii. 在页面右下方看到**绑定域名**的按钮，点击按钮： iii. 在弹出的对话框中，填写您自己的域名，点击**确定**后域名绑定成功。
2. 做域名解析
为了直接通过该域名能访问到API网关，您需要在在专有云内做域名解析，将您的域名解析到网关的VIP 上。网关VIP的查找方法，ping [分组二级域名]
3. 上传域名证书
绑定好域名后，就可以使用绑定的域名以HTTP方式访问分组下的所有API了，但是如果想以HTTPS的方式访问分组下的API，需要将您的域名证书上传到刚才绑定的域名下才行。您需要准备该域名的证书，并将证书内容上传到网关上。 i. 在**分组详情**下的**独立域名**点击**手动添加证书**。 ii. 在打开的对话框中，输入**证书名称**,**证书内容**,**私钥**。

**说明**

如果证书是自签名生成的，访问的时候需要做忽略证书处理。

## 常见问题

### 如何获取错误信息

所有的 API 请求只要到达了网关，网关就会返回请求结果信息。 用户需要查看返回结果的头部，即 Header 部分。其中 X-Ca开头的均为网关返回，比较重要信息是： `//` 请求唯一`ID`，请求一旦进入`API`网关应用后，`API`网关就会生成请求`ID`并通过响应头返回给客户端，建议客户端与后端服务都记录此请求`ID`，可用于问题排查与跟踪

```
X-Ca-Request-Id: 7AD052CB-EE8B-4DFD-BBAF-EFB340E0A5AF
```

`// API`网关返回的错误消息，当请求出现错误时`API`网关会通过响应头将错误消息返回给客户端

```
X-Ca-Error-Message: Invalid Parameter Required `field1`
```

`// API`网关系统错误码，当请求出现错误被网关拦截后，由`API`网关提供的错误码`: (`经典网络实例无此头)

```
X-Ca-Error-Code: I400MP
```

|  | Header |
|---|---|
| Ca-Request-Id |  |

### 错误代码表

1. . API****网关错误码表**
当客户端收到的应答中 `X-Ca-Error-Code` 头不为空，表示应答码由API网关产生，错误码由一个6位长度的字符描述，请参考下表，而 `X-Ca-Error-Message` 表示错误的应答信息，用于描述改场景下更详细的一些错误信息。 如果 `X-Ca-Error-Code` 头为空，则表示这个Http应答码由后端服务产生，API网关透传了来自后端的错误信息。

| 错误代码 | Http状态码 | Message | 描述 |
|---|---|---|---|
| I400HD | 400 | Invalid Header `${HeaderName}` ${Reason} | HTTP请求头非法 |
| I400MH | 400 | Header `${HeaderName}` is Required | 缺少HTTP请求头 |
| I400BD | 400 | Invalid Body: ${Reason} | HTTP请求包体非法 |
| I400PA | 400 | Invalid Request Path `${Reason}` | HTTP请求路径非法 |
| I405UM | 405 | Unsupported Method `${Reason}` | 不支持的HTTP请求方法 |
| I400RU | 400 | Invalid Request Uri `${Reason}` | HTTP请求Url非法 |

| I403PT | 403 | Invalid protocol ${Protocol} unsupported | 使用了API配置中不支持的协议, 请检查API配置 |
|---|---|---|---|
| I413RL | 413 | Request body too Large | 请求包体过长 |
| I413UL | 413 | Request URL too Large | 请求URL过长 |
| I400CT | 400 | Invalid Content-Type: `${Reason}` | 非法的`Content-Type` |
| I404DO | 404 | Invalid Domain `${DomainName}` | 未知的请求域名 |
| I410GG | 410 | Group's instance invalid | 请求了非法的实例,分组可能已经不属于当前实例 |
| I400SG | 400 | Invalid Stage | 请求了未知的环境 |
| I404NF | 404 | API not found ${Reason} | 根据请求的 `Path`,`Method`在当前的环境中未找到API |
| X400PM | 400 | Invalid plugin meta ${PluginName} ${Reason} | 插件元数据非法,请工单联系客服人员 |
| X500ED | 500 | Expired api definition | API元数据定义非法,请工单联系客服人员 |
| X500AM | 500 | Invalid Api Meta, try deploy again or contact us via ticket | API元数据定义非法,请工单联系客服人员 |
| X403DG | 403 | Bad Domain or Group: ${Reason} | 分组数据非法,请工单联系客服人员 |
| B451DO | 451 | Unavailable Domain for Legal Reasons | 域名因法律法规问题被禁 |
| B451GO | 451 | Unavailable Group for Legal Reasons | 分组因法律法规问题被禁 |
| B403OD | 403 | Provider Account Overdue | API提供方欠费 |
| A400AC | 400 | Invalid AppCode ${Reason} | 当使用AppCode模式授权时,未找到AppCode |
| A400IK | 400 | Invalid AppKey | 当使用`Key/Secret`签名授权时,未找到AppKey |
| A403IS | 403 | Invalid Signature, Server StringToSign:`${String ToSign}` | 签名不匹配,请参考API网关签名文档 |
| A403EP | 403 | App authorization expired | 授权已过期 |

| A403PR | 403 | Plugin Authorization Needed | 需要插件授权 |
|---|---|---|---|
| A400MA | 400 | Need authorization, `X-Ca-Key` or `Authorization: APPCODE ...` is required | 需要使用`Key/Secret`签名授权或`AppCode`授权 |
| I400I5 | 400 | Invalid Content-MD5 ${Reason} | 不匹配的`Content- MD5` |
| I400NC | 400 | X-Ca-Nonce is required | 当设置了`使用X-Ca- Nonce防重放`选项时,必须提供`X-Ca-Nonce`头 |
| S403NU | 403 | Nonce Used | 检测到请求重放,请求的 `X-Ca-Nonce`头重复 |
| S403TE | 403 | X-Ca-Timestamp is expired | `X-Ca-Timestamp`头中提供的时间戳已过期 |
| I400MP | 400 | Parameter `${ParameterName}` is required | API中配置的必选参数未传值 |
| I400IP | 400 | Invalid parameter `${ParameterName}` ${Reason} | API中配置的参数值非法 |
| I400JR | 400 | JWT required | 未找到JWT参数 |
| S403JI | 403 | Claim `jti` is required when `preventJtiReplay:true ` | 当在`JWT授权插件`中配置了防重放功能时，请求未提供有效的`jti` |
| S403JU | 403 | Claim `jti` in JWT is used | 当在`JWT授权插件`中配置了防重放功能时，请求提供的`jti`已被使用 |
| I400JD | 400 | JWT Deserialize Failed: `${Token}` | 请求中提供的`JWT`解析失败 |
| A403JT | 403 | Invalid JWT: ${Reason} | 请求中提供的`JWT`非法 |
| A403JK | 403 | No matching JWK, `${kid}` not found | 请求`JWT`中的`kid`没有匹配的`JWK` |
| A403JE | 403 | JWT is expired at `${Date}` | 请求中提供的`JWT`已过期 |
| I400JP | 400 | Invalid JWT plugin config: ${JWT} | `JWT授权`插件配置错误 |
| A403OL | 403 | OAuth2 Login failed: ${Reason} |  |
| A403OU | 403 | OAuth2 Get User Info failed: ${Reason} |  |

| A401OT | 401 | Invalid OAuth2 Access Token |  |
|---|---|---|---|
| A401OM | 401 | OAuth2 Access Token is required |  |
| T429ID | 429 | Throttled by INNER DOMAIN Flow Control, ${Domain} is a test domain, only 1000 requests per day | 当使用默认二级域名访问时,限制1000次/天，请绑定正式域名以解除这个限制 |
| T429IN | 429 | Throttled by INSTANCE Flow Control | 触发当前实例的流控限制 |
| T429GR | 429 | Throttled by GROUP Flow Control | 触发当前分组的流控限制 |
| T429PA | 429 | Throttled by API Flow Control | 触发插件上的默认API流控 |
| T429PR | 429 | Throttled by PLUGIN Flow Control | 触发插件的特殊流控 |
| T429UP | 429 | Throttled by Usage Plan Flow Control | 触发使用计划的流控 |
| T429SR | 429 | Throttled by SERVER Flow Control |  |
| T429MR | 429 | Too Many Requests, throttle by `${Description}` |  |
| A403IP | 403 | Access denied by IP Control Policy | 被`IP访问控制插件`阻止访问 |
| A403IN | 403 | Access from internet is disabled ${Reason} | `API`或`API分组`禁止从公网访问 |
| A403VN | 403 | Access from invalid VPC is disabled | 来源VPC被阻止 |
| A403AC | 403 | Access Control Forbidden by ${RuleName} | 被`授权控制`插件阻止 |
| A403CO | 403 | Cross origin resource forbidden ${Domain} | 被CORS策略阻止访问 |
| I404CO | 404 | Cross origin resource not found ${Method} - ${Path} | 根据CORS预检请求中的 Path与Method，无法找到API定义 |
| I404CH | 404 | Content not cached, with `Cache- Control:only-if-cached` |  |
| I404NR | 404 | ${Resource} not found |  |

| I404SR | 404 | Stage route missing: ${Reason} |  |
|---|---|---|---|
| B403MO | 403 | Api Market Subscription overdue | API提供商欠费 |
| B403MQ | 403 | Api Market Subscription quota exhausted | 购买的云市场API配额已耗尽 |
| B403ME | 403 | Api Market Subscription expired | API订购关系已过期 |
| B403MI | 403 | Api Market Subscription invalid | API市场订购关系非法 |
| D504RE | 504 | Backend domain `${Domain}` resolve failed | 后端域名解析失败 |
| D504IL | 504 | Backend domain `${Domain}` resolve to illegal address `${Address}` | 后端域名解析结果非法 |
| D504CO | 504 | Backend service connect failed `${Reason}` | 后端连接失败,请检查安全组、后端服务器启动状态、或防火墙配置 |
| D504CS | 504 | Backend http ssl connect failed `${Reason}` | 后端HTTPS连接失败，请检查后端配置的协议与端口是否匹配 |
| D504TO | 504 | Backend service request timeout | 后端请求超时 |
| X504VE | 504 | Backend service vpc mapped failed | 后端VPC映射错误, 请工单联系客服人员 |
| D503BB | 503 | Backend circuit breaker busy | API被断路器阻止 |
| D503CB | 503 | Backend circuit breaker open, ${Reason} | API处于熔断/断路器开状态, 请检查后端性能 |
| I508LD | 508 | Loop Detected | 检测到环回调用 |
| I404DD | 404 | Device id ${DeviceId} not found | 当使用WebSocket双向通信调用时，DeviceId未找到 |
| A403FC | 403 | Function Compute AssumeRole failed ${RequestId}:${Reaso n} | 后端是函数计算时授权错误 |
| D502FC | 502 | Function Compute response invalid: ${Reason} | 后端是函数计算时，来自后端的应答非法 |

| X500ER | 500 | Service Internal Error | 服务器内部错误,请工单联系工作人员 |
|---|---|---|---|
| X503BZ | 503 | Service Busy | API网关服务忙,请稍后再试或工单联系工作人员 |
| X504TO | 504 | Service timeout | API网关处理超时 |

部分错误代码可能随着升级或新功能的加入而改变。
