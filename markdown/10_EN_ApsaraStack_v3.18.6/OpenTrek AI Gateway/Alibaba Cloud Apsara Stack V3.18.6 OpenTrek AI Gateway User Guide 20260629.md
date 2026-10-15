---
title: "OpenTrek AI Gateway User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 358
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 OpenTrek AI Gateway User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/AI%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek%20AI%20Gateway%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# OpenTrek AI Gateway User Guide 20260629

OpenTrek

## Product overview

### What is AI Gateway

This topic describes the scenarios and core features of AI Gateway. By configuring AI Gateway, you can integrate administration capabilities to use large model services efficiently and securely. Artificial Intelligence (AI) plays an essential role in modern business innovation. With the rise of large language models (LLMs), the scenarios for AI applications are expanding. Various commercial and self-built models are driving business development in different fields. However, enterprises face many challenges when using AI, such as issues with integration, stability, security, and management complexity. To address these challenges, AI Gateway acts as a bridge between enterprise AI applications and LLM services. It significantly improves integration efficiency and administration for enterprises that use large model services.

**Challenges for enterprises in AI scenarios**

LLMs are widely used in enterprise AI scenarios. These scenarios include the following three typical types of calls:
**Developers directly using large model services:** Developers directly connect to the
large language model APIs of different providers to meet business needs.
**AI applications calling large model services:** Internal enterprise AI applications call
large model services to handle complex tasks.
**AI applications calling regular applications (as tools):** AI applications call the API
operations of regular applications to extend their features. In practice, enterprises often need to choose and switch between multiple models. If a model has poor stability or performance, an enterprise must be able to quickly switch to another. They also need to perform grayscale testing on new models to evaluate them. Unlike personal applications, enterprises face the following four major challenges when adopting AI technology:
**High cost of integration and switching between different large model services** :
LLM API standards and access methods vary among model providers. This makes it difficult for LLM API callers to smoothly switch between providers or use models from different providers simultaneously. OpenTrek
**Difficulty in managing users of large model services within the enterprise** : LLM
APIs are shared and scarce resources within an enterprise. Improper use by some callers can lead to issues such as rate limiting, which must be avoided. The costs of different models vary greatly. Enterprises must ensure that high-cost models are used for high-value business scenarios. However, relying on management alone makes it difficult to achieve fine-grained permission management and resource control for users. It is also difficult to apply different models and policies for different business scenarios.
**High risks to data security and compliance** : Large model services are often limited by
factors such as hardware and are typically provided as Software as a Service (SaaS). When an enterprise calls a large model service API, its internal data is at risk of exposure. Additionally, data compliance is a significant concern when calling large model services, especially open source or external ones.
**Poor stability of large model services**: Large model services are constrained by
hardware, resulting in low rate-limiting thresholds for their APIs. Their stability is also lower than that of typical API services. The response time (RT) and request success rate are often unstable. This instability affects the overall availability of AI applications.

**Example AI Gateway scenario**

An enterprise wants to build AI applications to improve operational efficiency and explore new business opportunities. The enterprise purchases large model services, such as Alibaba Cloud Model Studio and Azure OpenAI. It also deploys a self-built open source model (llama3.x) on Alibaba Cloud FC. To allow its AI applications to use these services efficiently and securely, the enterprise configures AI Gateway. This integrates administration capabilities and provides a unified access point for all AI applications. The following figure illustrates this scenario. The gateway administrator assigns a consumer identity to each AI application, authenticated by an API key. When an application sends a request to AI Gateway, the gateway automatically routes the request to Alibaba Cloud Model Studio and Azure model services based on the `model` parameter. If a model service is unavailable due to rate limiting or other reasons, the gateway automatically falls back to the self-built open source model. To ensure data security and compliance, all AI requests must pass a Content Moderation review. The gateway blocks non-compliant requests. The administrator enables rate limiting and caching to prevent an application from overwhelming a model service with too many requests. The administrator also monitors the AI API observation dashboard to check the status of model calls and make adjustments as needed.

**Core features of AI Gateway**

AI Gateway provides a complete solution for exposing and managing AI applications as APIs. This solution ensures that: OpenTrek All calls to large model services pass through AI Gateway. This approach resolves issues such as model stability, authentication, security, compliance, observability, and administration at the gateway level. All API calls exposed by AI applications pass through AI Gateway. This allows the gateway to handle requirements such as protocol access, authentication, authorization, rate limiting, and degradation. To address these challenges, AI Gateway provides the following core features:

**Unified call method**

AI Gateway can quickly integrate various large model services, including commercial and self-built models. It exposes a unified API that is compatible with OpenAI. AI Gateway supports over a dozen domestic and international large model providers, including Alibaba Cloud Model Studio and OpenAI, along with self-built large model services, such as ollama. AI Gateway provides the AI API type, which is optimized for AI scenarios. The AI API offers three ways to integrate large model services: Single model service: Specify a single large model service. You can either pass through the model name from the request or specify a fixed model name. If you specify a fixed model name, the model name in the user's request is ignored. Multiple model services (by model name): Specify one or more large model services. You can configure a model name matching rule for each service. For example, you can configure a rule that routes requests with model names matching the `gpt-*` pattern to the OpenAI large model service, and requests with names matching the `qwen-*` pattern to the Alibaba Cloud Model Studio large model service. OpenTrek Multiple model services (by proportion): Specify one or more large model services. For each service, you can specify the target model name and a traffic percentage. This pattern is ideal for the grayscale release of new models. AI Gateway integrates observability features for AI calls, including metrics, logging, and tracing. Unlike general API observation, AI observability supports token-based statistics. It also supports observation dimensions, such as API, model, and consumer. Logs for AI requests and responses are recorded for tracking and auditing purposes. Key metrics for AI observation include the following: QPS: The number of AI requests and responses per second. This is divided into QPS for AI requests, streaming responses, and non-streaming responses. Request success rate: The success rate of AI requests, which can be calculated per second, per 15 seconds, or per minute. Tokens consumed/s: The number of tokens consumed per second, divided into input tokens, output tokens, and total tokens. Average request RT: The average response time (in milliseconds) of AI requests over a specified period (such as per second, per 15 seconds, or per minute). This is divided into non-streaming RT, streaming RT (total time for a streaming response), and first-packet RT for streaming (time to the first packet of a streaming response). Cache hits: The number of cache hits and misses over a specified period. Rate limiting statistics: The number of rate-limited and normal requests over a specified period. Token statistics by model: Token consumption statistics for different models over a specified period. Token statistics by consumer: Token consumption statistics for different consumers over a specified period. Threat statistics: Threats detected by Content Moderation, with statistics broken down by dimensions, such as threat type and consumer. OpenTrek AI Gateway has three core security features: Unified API key management and rotation: You can store the API keys for large model services at the gateway level, which hides them from callers. You can also configure multiple API keys for automatic rotation. Unified authentication: You can use the built-in consumer authentication feature to grant permissions to different callers separately. This feature supports authentication methods such as JWT and API Key. You can also monitor caller activity and configure rate limiting by consumer. Content moderation: AI Gateway deeply integrates with Alibaba Cloud Content Moderation to review and protect the content of AI requests and responses. You can configure review policies and sensitive words as needed. This ensures that request content is compliant and prevents the leakage of sensitive enterprise information.

**AI call administration and acceleration**

AI Gateway provides a unified administration center for enterprise AI applications. It uses features such as rate limiting, caching, and fallback to effectively improve the success rate of model calls. These features include the following: Rate limiting by token: AI Gateway has a built-in token-based rate limiting policy. You can limit the number of tokens consumed per unit of time based on request features, such as headers. Automatic rotation of multiple API keys: AI Gateway supports configuring multiple API keys for a model service. When processing AI requests, the keys rotate automatically. This prevents an issue with a single key from affecting all requests. AI caching: AI Gateway integrates an AI cache policy. It can cache responses to repeated requests to improve response efficiency and reduce the cost of large model services. Model service fallback: AI Gateway supports falling back to a backup model when a model service is unavailable. It also supports multi-level fallback, which can effectively increase the success rate of AI requests. In summary, AI Gateway is a key tool for improving the efficiency of enterprise AI applications. It simplifies integration, unifies administration, enhances security, and accelerates response times. This makes the process of innovating with AI technology more efficient, secure, and controllable for enterprises. rt OpenTrek

## Quick Start

### Log on to the AI Gateway

**console**

This topic describes how to log on to the AI Gateway console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. OpenTrek rt

**Note**

You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button. If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

**Note**

Obtain the username and password from an operations administrator. The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**.

**Note**

For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in Apsara Uni-manager Management Console User Guide.
5. In the top menu bar, choose **Product > Middleware > Application Integration > API**
**Gateway** to navigate to the **API Gateway 2.0** console.

**Note**

AI Gateway and API Gateway share the same console. rt OpenTrek

### Use Model API to proxy AI

#### traffic

This topic describes how to use Model API to proxy AI traffic.

**Background information**

Traditional HTTP routing applies only to generic services and cannot perfectly accommodate special requirements of large language models (LLMs), such as streaming responses, protocol differences, and token statistics. Forcing its use leads to high development costs and poor stability. When you integrate with LLMs, directly use the `Model API` mode. This mode natively integrates LLM-specific capabilities and offloads complex protocol conversion and scheduling policies to the gateway layer. You can focus on business logic and build more robust and easily operable AI infrastructure.

**Prerequisites**

You have created a Kubernetes cluster in Container Service for Kubernetes.

**Procedure**

**Step 1: Import a Kubernetes cluster**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster management** page, click **Import Kubernetes cluster**.
4. In the **Import Kubernetes cluster** panel, configure the parameters shown in the following
figure and click **OK**.

**Note**

For more information about parameter configurations, see Import a cluster.
1. In the left-side navigation pane, click **AI Gateway**.
OpenTrek rt
2. On the **Gateway instances** page, click **Create instance.**
3. On the **Create API Gateway Instance** page, configure the parameters shown in the
following figure and click **Submit**.
**Kubernetes cluster**: Select the Kubernetes cluster that you just imported.

**Note**

For more information about parameter configurations, see Create a gateway instance. rt OpenTrek OpenTrek rt
1. On the **Gateway instances** page, click the ID of the gateway instance that you just
created or click **Details** in the **Actions** column to go to the **Overview** page of the instance.
2. In the left-side navigation pane, click **AI Service**.
3. On the **AI services** page, click **Create AI service**.
4. On the **Create AI Service** page, configure the parameters shown in the following figure
and click **Create**.
**Endpoint**: Enter the endpoint of the LLM that you want to use.
**API Key**: Enter the API key of the LLM that you want to use.

**Note**

For more information about parameter configurations, see Create an AI service.
1. In the left-side navigation pane, click **Model API**.
2. On the **Model APIs** page, click **Create API**.
3. In the **Select scenario** dialog box, click **Create** in the lower-right corner of Text
Generation.
4. In the **Create Model API** panel, configure the parameters shown in the following figure
and click **OK**.
**Service name**: Select the AI service that you just created.

**Note**

For more information about parameter configurations, see Create a model API. rt OpenTrek

**Step 5: Debug the Model API**

OpenTrek rt
1. In the left-side navigation pane, click **Model API**.
2. In the Model API list, click **Debug** in the **Actions** column of the Model API that you just
created.
3. In the **Debug AI model** panel, configure the parameters shown in the following figure and
click **Send Request**.
**Model**: Enter the LLM that you want to use, for example, `qwen3.6-plus` .
**Prompt**: Enter "Hello".

**Note**

For more information about parameter configurations, see Debug a model API.

### MCP management

Model Context Protocol (MCP) is an open-source protocol that standardizes how applications provide context to large language models (LLMs). It acts like a "USB-C port" for AI applications, allowing models to flexibly and securely connect to various data sources and tools. This topic describes how to create and use MCP services.

**Features**

MCP service management enables a smooth migration from RESTful APIs to MCP services. It supports access through both Server-Sent Events (SSE) and Streamable HTTP protocols. This feature also integrates a consumer-based authentication mechanism, which provides a foundation for enterprise-level API administration.

**Create an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**, and then click **Create MCP**
**Service**.
5. In the **Create MCP Service** panel, configure the parameters, and then click **Save And**
**Publish**.

| Parameter |  | Description |  |  | Example |  |  |
|---|---|---|---|---|---|---|---|
| Name |  | Enter a custom name for the MCP service. Note The name of an MCP service must be unique within the same gateway instance. |  |  | demo |  |  |
| Description |  | Enter a description for the MCP service. |  |  | Test |  |  |
| MCP Endpoint | Domain Name | The domain name used to access the MCP service. You can select multiple domain names. Note If no domain names are available, click Add Domain Name to the right of the selection box to create one. For more information, see Create a domain name. |  |  | www.aliyun.com |  |  |
|  | Path (SSE) | The path of the MCP service endpoint for SSE. The path is generated based on the service name. |  |  | /mcp- |  |  |
|  |  |  |  |  |  | /mcp- |  |
|  |  |  |  | is | servers/{your-mcp- |  |  |
|  |  |  | rated based on the ce name. |  |  |  |  |
|  |  |  |  |  | server-name}/sse |  |  |
|  | Path (Streamable HTTP) | The path of the MCP endpoint for Streamable HTTP. The path is generated based on the service name. |  |  | /mcp- |  |  |
|  |  |  |  |  |  | /mcp- |  |
|  |  |  |  |  | servers/{your-mcp- |  |  |
|  |  |  | is generated based on ervice name. | n |  |  |  |
|  |  |  |  |  | server-name} |  |  |
| Service Type |  | The type of the MCP tool service. |  |  | You can select OpenAPI, DB, or Direct Routing. |  |  |
| Backend Service |  | Specify the service to which API requests are forwarded. |  |  | test |  |  |
| Consumer Authentication |  | If you enable this feature, only authorized consumers can access the MCP service. |  |  | Enabled |  |  |

rt OpenTrek OpenTrek rt

**View MCP service details**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. (Optional) On the **MCP Management** page, you can quickly filter MCP services by **MCP**
**Service Name** or **MCP Service Type**.
6. In the service list, click the service name or **Details** in the **Actions** column. On the **MCP**
**Details** page, you can view the basic information and configuration details of the MCP
service. On the **Basic Information** tab, you can view the service's **Basic Information** and
**Endpoint Information**.
On the **Tools** tab, you can add tools to the MCP service. For more information, see Add tools to an MCP service. On the **Consumer Authentication** tab, you can set up consumer authentication and authorization for the MCP service. For more information, see Consumer authentication. The **Resources** and **Prompt** tabs are not yet supported.

**Add tools to an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**, and then click **Details** in the
**Actions** column for the target service.
5. On the **Tools** tab, click **Edit Tools** in the upper-right corner of the page.
6. MCP services currently support two methods for adding tools:
Method 1: **Based On A Swagger File** (Recommended) i. **Import Swagger To Create Or Incrementally Update MCP Tools** : Upload an OpenAPI file from your local machine or paste the API definition into the editor, and then click **Generate Now**. ii. **Update And Confirm The MCP Tool List**: You can view the generated MCP tool description file. You can then confirm and modify the information in the file. Method 2: **Custom YAML** You can manually create MCP tools using custom YAML.
7. Click **OK**. On the **Tools** tab, you can view the tool list, along with the tool names,
descriptions, and parameter information. 1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**. Click the name of the target
service or **Details** in the **Actions** column, and then click the **Consumer Authentication** tab.

| Configuration Item | Description |
|---|---|
| Enabled Status | Turns the consumer authorization switch on or off. This feature is disabled by default. |
| Authentication Method | The only supported authentication method for consumer authorization is API Key. An API key is a simple authentication method. When a client makes a request, it must add the credential to the request in a specified way. After the gateway receives the request, it verifies the validity and permissions of the API key. The server assigns a unique string to the client as an access credential. The client submits this API key in the header or as a query parameter with each request. |

rt OpenTrek
5. On the **Consumer Authentication** tab, turn on the **Enabled Status** switch for
**Configuration Information**.

**Important**

After you enable consumer authentication, the service cannot be accessed if no authorization relationship is configured.
6. In the **Consumers** area, click **Grant Authorization**, select a consumer, and click **Add**.

**Note**

If no consumers exist, you must first create one before you can grant authorization. For more information, see Create a consumer.

**Debug an MCP service with MCP Inspector**

**Note**

You can start MCP Inspector locally to debug MCP services. MCP Inspector is a debugging tool provided by the MCP community. You can use it to debug the entire flow of an MCP service.
1. Install the Node.js environment.
2. Run the following command to start MCP Inspector: `npx @modelcontextprotocol/inspector`

```
node build/index.js .
```

3. Select a transport type. Set **Transport Type** to **SSE**.
4. Enter the `URL` . You can find the URL on the right side of the MCP service details page.
5. (Optional) If consumer authentication is configured, click **Authentication** to expand the
authorization configuration, and then enter the consumer's token.
6. Click **Connect**. After a successful connection, the **List Tools** button appears in the middle
of the page. Click **List Tools** to retrieve all the tools for the MCP service. OpenTrek rt
7. (Optional) To debug a specific tool, click the tool name, enter the required parameters on
the right, and click **Run Tool** to start the tool calling test.

**Modify an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. In the service list, find the service that you want to modify and click **Edit** in its **Actions**
column.
6. In the **Edit MCP Service** panel, modify the configurations as needed, and then click **Save**
**And Publish**.

**Delete an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. In the service list, find the service that you want to delete and click **Delete** in its **Actions**
column.
6. In the **Notice** dialog box that appears, click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a custom cluster name. |
| Cluster Type | Select Self-managed Kubernetes or Container Service for Kubernetes. |
| Container Service Cluster ID | Note This parameter appears only when you select Container Service for Kubernetes for Cluster Type. Enter the ID of the Container Service cluster that you want to import. You can view the cluster ID on the Clusters page in the Container Service for Kubernetes console. |

de OpenTrek

## User Guide

### Kubernetes cluster

**management**

This topic describes how to import an external Kubernetes cluster into the AI Gateway for centralized management.

**Prerequisites**

You have created a Kubernetes cluster by following the instructions in **Container Service**
**for Kubernetes User Guide > Create a Kubernetes cluster**, or you have obtained the
kubeconfig information of a self-managed Kubernetes cluster.

**Import a cluster**

**Note**

The system currently supports only Kubernetes clusters.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, click **Import Kubernetes Cluster**.
4. In the **Import Kubernetes Cluster** panel, configure the parameters. Then, click **Test**
**Connection** to verify the configuration. Finally, click **OK**.

| Container Service Cluster Name | Note This parameter appears only when you select Container Service for Kubernetes for Cluster Type. Enter the name of the Container Service cluster that you want to import. You can view the cluster name on the Clusters page in the Container Service for Kubernetes console. |
|---|---|
| SLB Type | Select Internet or Intranet. |
| Configuration Content | Enter the corresponding kubeconfig information. |

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the gateway belongs. Important You cannot change the organization after you create the resource. |

OpenTrek de

**Cancel cluster import**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, click **Remove** in the **Actions** column of the target
cluster.
4. In the **Note** dialog box that appears, click **OK**.

### Gateway management

#### Create a gateway instance

This topic describes how to create an AI Gateway instance.

**Prerequisites**

You have imported a Kubernetes cluster. For more information, see Import a cluster.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway** page, click **Create Instance.**
4. On the **Create API Gateway Instance** page, configure the following parameters.

| Resource set | Select the resource set to which the gateway belongs. You can select the default resource group or an existing resource group. Note You can use resource sets to classify and manage resources under your Alibaba Cloud account by group. This allows you to manage permissions, deploy resources, and monitor resources at the group level without handling each resource individually. Important You cannot change the resource set after you create the resource. |
|---|---|
| Region | Select the region where the gateway resides. Important You cannot change the region after you create the resource. |
| Instance name | Specify a custom name for the gateway. We recommend that you name the instance based on the environment or environment plus business domain, such as test or order-prod. The instance name must be 2 to 128 characters in length. |
| Number of instance nodes | Specify the number of nodes for the gateway instance. |
| Specification | Select a node specification based on your actual requirements. |
| Gateway type | Select AI Gateway. |
| Deployment architecture | Select Kubernetes. Note The Kubernetes option refers to the deployment of the AI Gateway instance. The system deploys the instance by using an existing Helm artifact. |
| Kubernetes cluster | Select an imported Kubernetes cluster to deploy the AI Gateway instance. |
| Ingress class name | Enter an Ingress class name. The name can contain only letters, digits, and hyphens (-) and cannot start with a hyphen (-). |
| Namespace | Enter a namespace. The namespace can contain only letters, digits, and hyphens (-) and cannot start with a hyphen (-). |

de OpenTrek

| Log Service | If you select Use Log Service, the system activates Simple Log Service (SLS) and enables the log shipper feature for the gateway. This provides log analysis and dashboards. For more information, see View gateway log information. |
|---|---|
| Monitoring plug-in | If you select Use Prometheus Monitoring, Prometheus monitors the AI Gateway instance. For more information, see View gateway monitoring metrics. |

OpenTrek de
5. On the **Create API Gateway Instance** page, review the AI Gateway configuration details
and click **Submit**.

**Note**

It may take 1 to 5 minutes to create the gateway instance. Please wait patiently.
6. Return to the **Gateway** page. If the created gateway information is correct and the
**instance status** is **Running**, the gateway is created successfully.

#### View gateway instance details

This topic describes how to view the details of an AI Gateway instance in the AI Gateway console.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. (Optional) On the **Gateway Instances** page, you can filter for the target instance by
**Instance Name** and **Instance ID**.
4. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
5. In the navigation pane on the left, choose the **Overview** page to view the **Basic**
**Information** and Access Point of the AI Gateway instance.
On the **Basic Information** tab:
**Gateway Overview**: Displays the **Total Routes**, **Number Of Consumers**, **Total**
**Services**, **Total MCP Services**, and **Total Plugins** of the current AI Gateway
instance.
**Basic Information**: Displays the **Instance ID**, **Instance Name**, **Status**, **Deployment**
**Architecture**, **Cluster**, **Namespace**, **Creation Time**, **Modification Time**, **Engine**
**Type**, **Engine Version**, and **Container Service Cluster ID** of the current AI Gateway
instance. The Access Point tab displays the endpoint information for the instance, including **Type**,
**Network Type**, **ServiceName**, **External IPs**, **Ports**, and **ClusterIP**.

#### Modify a gateway instance

This topic describes how to modify the name of a gateway instance.

**Procedure**

de OpenTrek

**Note**

You can only modify the instance name.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instance** page, click
in the **Actions** column for the target instance, and then click **Edit**.
4. On the **Edit Instance** page, change the **Instance Name** and click **Submit**.

#### Release an AI gateway instance

If you no longer need an AI gateway, you can release the instance to shut down the cloudnative AI gateway.

**Precautions**

Releasing an instance permanently deletes it and all of its data. Exercise caution.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instances** page, in the **Actions** column for the target instance, click
, and then click Write-off or **Force Logoff** .
4. In the **Notice** dialog box, click **OK**.

#### Stop a gateway instance

This topic describes how to stop an AI gateway instance.

**Procedure**

You can stop a gateway instance if you do not need it to run temporarily.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instances** page, in the **Operations** column of the target instance, click
and then click **Stop**.
4. In the **Prompt** dialog box, click **OK**. The **Instance Status** of the instance changes to
**Stopped**.

#### Restart a gateway instance

This topic explains how to restart an AI gateway instance.

**Procedure**

You can restart a gateway instance to resume its service.
1. Log in to the AI Gateway console.
OpenTrek de
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instance** page, click
in the **Actions** column of the target instance, and then click **Restart**.
4. In the **Message** dialog box that appears, click **OK**. The **Instance Status** changes to
**Running**.

#### Scale Gateway Instances

After you create an AI Gateway, you can scale its specification, CPU, and memory.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instances** page, click
in the **Actions** column for your target instance. Then, click **Configuration Change**.
4. In the **API Gateway Instance Configuration Change** panel, select a **specification**, then
click **Submit**.

#### Upgrade an instance engine

This topic describes how to upgrade the engine of a gateway instance.

**Prerequisites**

The instance is not running the latest engine version.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway Instances** page, in the **Engine Version** column for the target instance,
click **Manual Upgrade**.

#### Configure security group rules

The AI Gateway and backend service nodes are in different security groups. You must configure security group rules to grant the AI Gateway access permissions to the backend services.

**Background information**

A security group is a virtual firewall that controls inbound and outbound traffic for Elastic Compute Service (ECS) instances and Elastic Network Interfaces (ENIs) in the security group. This improves the security of ECS instances. Security groups provide stateful inspection and packet filtering. You can use security groups and their rules to create security domains in the cloud. For more information, see the ***Elastic Compute Service User Guide* > Security**
**Group Overview** section.
Because the AI Gateway and backend service nodes are in different security groups, you must grant the AI Gateway access permissions for the required port range in the security group of the backend service. de OpenTrek The figure shows how an AI Gateway can be used to manage network access and distribute traffic for different types of services. The connections are as follows: Client devices, such as computers, on the left access the internal network through the AI Gateway. The AI Gateway forwards traffic to service-sg1 and service-sg2 based on its configuration. The pods in service-sg1 can process requests on port 8080. The ECS instances in service-sg2 can process requests on ports 80 and 9000.

**Step 1: Obtain the CIDR block of the node where the gateway**

**instance is located**

1. Log on to the Container Service for Kubernetes (ACK) console. In the navigation pane on the
left, choose **Clusters**.
2. On the **Clusters** page, click the name of the target cluster. In the navigation pane on the
left, choose **Node Management > Node Pools**. Click the name of the node pool.
3. On the **Node Pool** page, find the **Node Configurations** section and obtain the ID of the
**Nodev Switch**.
4. Log on to the Apsara Stack VPC console. In the navigation pane on the left, click
**vSwitches**.
5. On the **vSwitches** page, click the vSwitch ID that you obtained in Step 3.
6. On the **vSwitch Details** page, click the **Basic Information** tab. Obtain the value of the
IPv4 CIDR block. This is the CIDR block for the vSwitch.

**Step 2: Obtain the security group of the node where the target**

**service is located**

| Parameter | Description | Example |
|---|---|---|
| Port Range | Enter the port range for the security group authorization. | 1/65535 |
| Priority | Enter the priority of the security group rule. | 1 |
| Authorization Type | Select IPv4 CIDR Block Access. | IPv4 CIDR Block Access |
| Authorization Object | Enter the CIDR block of the node where the gateway instance is located. You obtained this in Step 1. | 172.16.0.2/24 |

OpenTrek de The upstream services associated with the AI Gateway are deployed in containers or on ECS instances. Obtain the security group ID in one of the following ways:

**The target service is deployed in ACK**

1. Log on to the Container Service for Kubernetes (ACK) console. In the navigation pane on the
left, choose **Clusters**.
2. On the **Clusters** page, click the name of the target cluster. In the navigation pane on the
left, choose **Node Management > Node Pools**. Click the name of the node pool.
3. On the **Node Pool** page, obtain the security group ID from the **Node Pool Information**
section.

**The target service is deployed on an ECS instance**

1. Log on to the Elastic Compute Service (ECS) console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. On the **ECS Instances** page, click the target ECS instance. Then, click the **Security**
**Groups** tab to obtain the security group ID.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**. Click
the ID of the security group that you obtained in Step 2.
3. Click the **Security Group Rules** tab. On the **Inbound** tab, click **Add Security Group**
**Rule**. Configure the following parameters and then click **OK**.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**. Click
the ID of the security group that you obtained in Step 2.
3. Click the **Security Group Rules** tab. Delete the security group authorization rule using one
of the following methods. Method 1: In the **Actions** column of the target security group rule, click **Delete**. de OpenTrek Method 2: In the **Actions** column of the target security group rule, click **Modify**
**Properties**. In the **Modify Properties** dialog box, remove the IP address range from the
authorization rule.

**FAQ**

**Why is the service inaccessible even after I granted**

**authorization in the security group?**

Troubleshoot the issue by following these steps:
1. First, confirm that your target service is deployed on the correct node.
The service might be deployed on Node A, but you granted authorization to the security group of Node B.
2. Check if the target node is associated with multiple security groups.
If a node is associated with multiple security groups, you must grant authorization to each of them.

**The gateway could access the service before, but now it**

**cannot, even though the security group is authorized. Why?**

Troubleshoot the issue by following these steps:
1. First, confirm that the service itself is working correctly.
Run the `curl` command from another node in the same security group to check the service connectivity.
2. Confirm whether the port exposed by the published service has changed.
For example, the port was previously 8080, and you only authorized port 8080 for the AI Gateway. If you change the port to 8081, you must adjust the security group rule to authorize the new port. To avoid this issue, you can expand the port range when you configure the security group authorization. Set the range to 1/65535.

### Model APIs

#### Create a model API

This topic describes how to create a model API.

**Background information**

The model API module allows you to configure the routing rules, protocol, associated backend services, and disaster recovery policy (such as fallback) of a model API. This way, you can centrally manage AI capabilities, enforce security control, and schedule traffic.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. On the **Model API** page, click **Create API**.

| Parameter | Description |
|---|---|
| Use case | Default value: Text generation. You cannot modify this parameter. |
| Agreement | Select a communication protocol for the API. Valid values: OpenAI compatible, Native API, and Custom HTTP. |
| Routing | Configure path mappings for API requests. You can select multiple paths. |
| API name | The unique identifier of the API. The API name must be no more than 64 characters in length, and can contain letters, digits, underscores ( ), and hyphens ( - ). _ |
| Domain name | Select one or more domain names to expose the API to HTTPS access. Note If no domain name is available, click Add domain name on the right side to create a domain name. For more information, see Create a domain name. |
| Base Path | The base path of the API. Default value: / . If you select Remove when forwarding to the backend service, the base path is automatically removed from the path of a request before the request is forwarded to the associated backend service. For example, if the base path is /api and the original request path is /api/users, the path of the request forwarded to the backend service is /users. |

OpenTrek de
6. In the **Select the use case** dialog box, click **Create** in the lower-right corner of the **Text**
**generation** card.

**Note**

Currently, only **text generation** is supported.
7. In the **Create a model API** panel, configure the following parameters and click **Confirm**.

| AI request for observation | After you turn on AI request for observation, you can view the metrics, logging, and tracing information of AI requests. Logging and tracing rely on the log shipping feature of Simple Log Service (SLS). Record request content: If you select this check box, request parameters are recorded. Record response content: If you select this check box, results returned by the model are recorded. Important When AI request for observation is turned on, the system gateway automatically records the content of all AI requests, including the request body, in access logs. Make sure that SLS is properly configured and take necessary security measures to ensure the security of log content and prevent information leakage or other risks. |
|---|---|

de OpenTrek

| Large Model Service | Select a model service. Single-model service: The API is associated with a single AI service. Service Name: Select an existing AI service. Use the specified model name: If you select Yes, the system ignores the model names carried in requests and forwards the requests to the model service specified by the Service Name parameter. Model Name: The default value is Pass- through. Multi-model service (by model name): Requests are forwarded based on the model field carried in the requests. Note Click Add to add services and specify their weights. Click Add a matching rule to add matching rules. Model Name Matching Rules: Use the Glob syntax to match model names. Service Name: Select an existing AI service. Service weight: Requests are distributed to services based on the weights of the services. Higher values indicate larger proportions. Valid values: 0 to 10000. Multi-model service (by weight): An API request can be distributed to multiple AI services and processed proportionally based on the weights of the services. Note Click Add to add AI services. Service Name: Select an existing AI service. Service weight: Requests are distributed to services based on the weights of the services. Higher values indicate larger proportions. Valid values: 0 to 10000. Use the specified model name: If you select Yes, the system ignores the model names carried in requests and forwards the requests to the model service specified by the Service Name parameter. Model Name: The default value is Pass- through. |
|---|---|

OpenTrek de

| Fallback | After you enable Fallback, when the primary service is unavailable or times out, the system automatically fails over to the secondary service. After the fallback is enabled, you need to add one or more secondary AI services for failovers. The selected services are sorted in descending order of priority. The system attempts to call the services in the order they are sorted one after one. |
|---|---|

de OpenTrek

#### Manage APIs

This topic describes how to view, edit, and delete model APIs.

**View API details**

After creating an API, you can view its details.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. (Optional) On the **Model API** page, you can quickly filter APIs by **API name**, **Scenario**
**Type**, and **Agreement**.
6. In the API list, click the API name or click **View** in the **Operation** column to go to the **Model**
**API Details** page. On this page, you can view the **basic information**, **associated**
**routes**, **consumer authentication**, **plugin configuration**, **policy configuration**, and
**usage guide** of the API.
On the **Basic Information** tab, view the **basic information**, **route distribution**
**configuration**, **observability configuration**, and **fallback configuration** of the API.
On the **Associated Routes** tab, view the route information associated with the current model API. On the **Consumer Authentication** tab, configure consumer authentication and authorization for the model API. For more information, see Consumer authentication. On the **Policy Configuration** tab, configure header modification, timeout settings, AI rate limiting, and AI content safety. For more information, see Configure model API policies. On the **Usage Guide** tab, view the **configuration information**, **parameter settings**, and **usage example** of the model API.
**Configuration Information**: Include the domain name, model name, consumer
choice, and external access address. The system allows modifying the domain name, model, and consumer.
**Parameter settings**: Include **temperature**, **top_p**, and **max_tokens**. The system
allows adjusting parameter values.
**Usage example**: View the example code for using the model API. You can click the
**Copy** button on the right to obtain the example code.

**Edit an API**

1. Log in to the AI Gateway console.

| Configuration item | Description |
|---|---|
| Enable request authentication | Turn on or off the consumer authorization switch. By default, it is turned off. |

OpenTrek de
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the API list, click **Edit** in the **Operation** column of the API that you want to modify.
6. In the panel that appears, modify the API parameters and click **Confirm**.

**Delete an API**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the API list, click **Delete** in the **Operation** column of the target API.
6. In the dialog box that appears, click **OK**.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Model API**. Click the target API name or click **View**
in the **Operation** column. Then, click the **Consumer Authentication** tab.
5. On the **Consumer Authentication** tab, click the switch next to **Enable request**
**authentication** to enable request authentication.

**Important**

After you enable consumer authentication, if no authorization relationship is configured, you cannot access the current API.

| Certification type | The authentication method for consumer authorization currently supports only API Key. API Key is a simple authentication method. When a client accesses the API, it must add credentials to the request in a specified way. The gateway verifies the validity and permissions of the API Key upon receiving the request. The server assigns a unique string as an access credential to the client. The client submits this credential through headers or query parameters in each request. |
|---|---|

| Parameter | Description |
|---|---|
| Domain name | Select the domain name bound to this route. |
| Model | Select an AI model that has been connected from the drop-down list. |
| Consumer | Select the client identity that calls this API. |

de OpenTrek
6. In the **Consumer Certification List** section, click **Authorization**, select consumers, and
then click **Confirm**.

**Note**

If no consumers exist, create one first. For more information, see Create a consumer. Then, authorize the consumer. In the **Consumer Certification List** table, click **Remove** in the **Operation** column, or select the target consumers and click **Batch remove** to revoke consumer authorization for the model API.

**Debug a model API**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the model API list, click **Debugging** in the **Operation** column of the target model API.
6. In the **AI model debugging** panel, configure the parameters and click **Send Request**.

**Note**

Click **Fill in historical parameters** to quickly reproduce the previous configuration. Click **Reset** to restore default values.

| Streaming request | Toggle to enable or disable streaming output. If you enable streaming requests, the system returns results character by character. |
|---|---|
| Prompt | Enter a user question or instruction to trigger model inference. |
| System Prompt | Enter system prompts to define the model's role and behavioral guidelines. |
| max tokens _ | Control the maximum number of tokens generated. |
| top p _ | The nucleus sampling parameter controls the diversity of generated outputs. |
| temperature | Control generation randomness. A higher value produces more random output. |

OpenTrek de
7. In the **Model return** section, view the generated result.

**Note**

By default, the system retains context across multiple calls. Click **Empty memory** to clear it.

#### Configure model API policies

This topic describes how to configure policies for model APIs, including header modification, timeout settings, AI rate limiting, and AI content safety.

**Configure header modification policy**

Before a request is forwarded to the target backend service or before the backend service's response is returned to the client, the header modification policy can modify headers in the original request.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the model API list, click the target model API name or click **View** in the **Operation**
column, then click the **Policy Configuration** tab.
6. On the **Policy Configuration** tab, click **Header modification**.
7. In the **Header modification** section, configure the relevant parameters as needed, then
click **Save configuration**.

| Parameter | Description |
|---|---|
| Enable | On: After you enable the header modification policy, the gateway controls headers in requests and responses. Off: After you disable the header modification policy, the gateway does not control headers in requests and responses. |
| Add request header | Click Add, enter the header name and value to add a new header to the request. Note If the header you add already exists, the system appends the new value to the existing value, separated by a comma (,). |
| Set the request header | Click Add, enter the header name and value to modify a specified header in the request. Note If the specified header does not exist, the system adds a new header with the provided name and value. If the specified header exists, the system overwrites its value. |
| Remove request header | Click Add, enter the header name to delete the specified header from the request. |
| Add response header | Click Add, enter the header name and value to add a new header to the response. Note If the header you add already exists, the system appends the new value to the existing value, separated by a comma (,). |

de OpenTrek

| Set the response header | Click Add, enter the header name and value to modify a specified header in the response. Note If the specified header does not exist, the system adds a new header with the provided name and value. If the specified header exists, the system overwrites its value. |
|---|---|
| Remove the response header | Click Add, enter the header name to delete the specified header from the response. |

| Parameter | Description |
|---|---|
| Enable | The switch to enable or disable the timeout policy. On: The timeout policy takes effect. Off: The timeout policy becomes invalid. |

OpenTrek de

**Configure timeout policy**

You can configure the maximum time that the gateway waits for a response from the backend service for a specified model API. If the gateway does not receive a response from the backend service within the specified time, it returns an HTTP status code 504 (Gateway Timeout) to the client.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the model API list, click the target model API name or click **View** in the **Operation**
column, then click the **Policy Configuration** tab.
6. On the **Policy Configuration** tab, click **Timeout setting**.
7. In the **Timeout setting** section, configure the relevant parameters, then click **Save**
**configuration**.

**Note**

After you configure and enable the timeout policy, verify whether the service timeout rule takes effect based on your actual business needs.

| Timeout | Set the timeout period for requests of the current model API. Unit: seconds. Note If you set this parameter to 0 or disable the timeout policy, the gateway waits indefinitely for the response. |
|---|---|

| Parameter | Description |
|---|---|
| Enable | On: After enabling, the rate limiting rules configured below take effect. Off: When not enabled, all requests are not subject to AI rate limiting limits. |

de OpenTrek

**Configure AI rate limiting**

The AI rate limiting policy is designed for large model services and high-concurrency calling scenarios. It supports a multi-dimensional dynamic control mechanism based on token consumption, request count, and concurrency. You can configure rate limiting rules across multiple dimensions including consumer identity, request header parameters, query parameters, cookies, and client IP addresses. The policy also provides API-level global rate limiting capability. This multi-dimensional rate limiting mode precisely matches the computing resource consumption characteristics of large models. It effectively prevents system overload, API abuse, and malicious calls while ensuring stable operation of core business under complex scenarios.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Model API**.
5. In the model API list, click the target model API name or click **View** in the **Operation**
column, then click the **Policy Configuration** tab.
6. On the **Policy Configuration** tab, click **AI Rate Limiting**.
7. In the **AI Rate Limiting Configuration** section, configure the relevant parameters, then
click **Save configuration**.

| Rate Limiting Rule Configuration | Set the judgment condition and rate limiting configuration. Judgment condition: Select a rate limiting dimension. The system supports five options: By consumer, By Request Header, By URL Parameter, By Cookie, By client IP. Rate Limiting Configuration: Depending on the selected judgment condition, you must fill in different matching information (such as matching rule, parameter name, matching content). See the detailed descriptions for each dimension below. Note Click Add rate-limiting configuration to set multiple rate limiting configurations for a single rule. Click Delete on the right side of a rate limiting rule to remove unnecessary rate limiting configurations. Click Add rule to configure multiple rules. The system supports up to 10 rules. Click Deletion rules to clear rules that are no longer needed. |
|---|---|
| Global Rate Limiting Configuration | Global rate limiting is a fallback policy independent of the rate limiting policies described above. It applies limits to the entire API without distinguishing specific judgment conditions. Enable method: Click Add Global Rate Limit to configure the rate limiting rule. Form fields: Rate limiting category (Token/Requests/Concurrency) → Rate limiting scope (per second/every minute/every hour/every day) → Rate limiting value + rate limiting unit. Supports adding multiple rules: You can click Add Global Rate Limit to add multiple global rate limiting rules and set different rate limiting modes for each rule. Example: The entire API allows a maximum of 10,000 Tokens consumed per minute, 100 requests per minute, and a maximum concurrency of 20. Note Global rate limiting serves as a fallback policy beyond the policies described above. It can be used simultaneously with standard rules. Both take effect cumulatively, and triggering either rule activates rate limiting. |

OpenTrek de
**By consumer**: Rate limiting based on consumer identity, suitable for multi-tenant
scenarios.

**Important**

To configure rate limiting by consumer, you must first enable Consumer authentication.

| example, | 192.168.1.1 |  |
|---|---|---|
| 0.0.0.0/0 |  |  |
|  |  | matches a |

de OpenTrek Form fields: Judgment condition (**By consumer**) → Matching rule (**Exact match**/**Prefix**
**matching**/**Regular expression matching**/**Arbitrary match**) → Matching content →
Rate limiting category → Rate limiting scope → Rate limiting value + rate limiting unit. Matching content: When you select **Arbitrary match**, no consumer information is required. Example: Any consumer is limited to 1,000 tokens per minute.
**By Request Header**: Rate limiting based on specified fields in the request header.
Form fields: Judgment condition (**By Request Header**) → Parameter name (request header name) → Matching rule (**Exact match/Prefix matching/Regular expression**
**matching/Arbitrary match**) → Matching content → Rate limiting category → Rate
limiting scope → Rate limiting value + rate limiting unit. Parameter name: Required. Enter the request header name to match. Matching content: When you select **Arbitrary match**, no input is required. Example: Limit requests where the header `x-user-level` equals `beta` to 100 tokens per minute.
**By URL Parameter**: Rate limiting based on query parameters in the request URL.
Form fields: Judgment condition (**By URL Parameter**) → Parameter name (URL parameter name) → Matching rule (**Exact match/Prefix matching/Regular**
**expression matching/Arbitrary match**) → Matching content → Rate limiting
category → Rate limiting scope → Rate limiting value + rate limiting unit. Parameter name: Required. Enter the URL parameter name to match. Matching content: When you select **Arbitrary match**, no input is required. Example: Limit requests with the URL parameter `user_id=1` to 100 Tokens per minute.
**By Cookie**: Rate limiting based on specified fields in the request Cookie.
Form fields: Judgment condition (**By Cookie**) → Parameter name (Cookie field name) → Matching rule (**Exact match/Prefix matching/Regular expression**
**matching/Arbitrary match**) → Matching content → Rate limiting category → Rate
limiting scope → Rate limiting value + rate limiting unit. Parameter name: Required. Enter the Cookie field name to match. Matching content: When you select **Arbitrary match**, no input is required. Example: Limit requests containing a target identifier in the Cookie to 100 tokens per minute.
**By client IP**: Rate limiting based on the client IP address. Supports individual IPs and IP
segments.

**Note**

When **By client IP** is selected, you do not need to select a matching rule or rate limiting scope. The system handles this automatically. Form fields: Judgment condition (**By client IP**) → IP address → Rate limiting category → Rate limiting scope → Rate limiting value + rate limiting unit. addresses. Example: Limit the maximum concurrency for each client IP address to 50.

| Matching rule | Description | Example |
|---|---|---|
| Exact match | The matching value must exactly equal the target value. | The header x-user-level exactly equals beta . |
| Prefix matching | The matching value must start with the specified prefix. | The header x-user-level starts with vip . |
| Regualr expression matching | The matching value must conform to the specified regular expression. | The header x-user-level matches `^(gold . |
| Arbitrary match | Matches all values under this dimension. No matching content is required. | Applies to any consumer. |

|  | x-user-level |
|---|---|
| vip |  |

|  | x-user-level |
|---|---|
| `^(gold |  |

| Rate limiting category | Description | Applicable conditions |
|---|---|---|
| Token | The system calculates consumption based on the number of tokens input to and output from the large language model (LLM). | All conditions. |
| Requests | The system calculates consumption based on the number of requests. | All conditions. |

OpenTrek de

**Matching rules**

The system supports the following four matching rules for judgment conditions of by consumer, request header, URL parameter, and Cookie. Priority: exact match > prefix matching > regular expression matching > arbitrary match.

**Note**

If you configure multiple rules, triggering any single rule results in blocking. Rate limiting by client IP and by model uses fixed matching methods. You do not need to manually select a matching rule.

**Rate limiting categories and rate limiting modes**

Each rate limiting rule allows you to select a rate limiting category. Different rate limiting categories correspond to different measurement methods:

| Concurrency | The system calculates consumption based on the number of requests processed simultaneously. | All conditions. |
|---|---|---|

| Rate limiting scope | Token rate limiting | Request rate limiting | Concurrency rate limiting |
|---|---|---|---|
| Per second | The maximum number of tokens allowed for consumption per second. | The maximum number of requests allowed per second. | — |
| Every minute | The maximum number of tokens allowed for consumption per minute. | The maximum number of requests allowed per minute. | — |
| Every hour | The maximum number of tokens allowed for consumption per hour. | The maximum number of requests allowed per hour. | — |
| Every day | The maximum number of tokens allowed for consumption per day. | The maximum number of requests allowed per day. | — |
| (No time window) | — | — | The maximum number of requests allowed for simultaneous processing. |

de OpenTrek Rate limiting policies support the following rate limiting scopes (time windows), paired with rate limiting units:

**Note**

Concurrency rate limiting does not require a rate limiting scope (time window). You only need to set the maximum concurrency value. The valid range for the rate limiting value is from 1 to 2,147,483,647.

**Configure AI content safety**

The AI content safety configuration performs real-time content moderation on inputs (user prompts) and outputs (model responses) of large language models. This prevents the generation or dissemination of illegal, sensitive, or inappropriate content and ensures compliance and security of AI services.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.

| Parameter | Description |
|---|---|
| Enable | On: It enables the content moderation feature. Off: After disabling, all requests skip content detection, which poses compliance risks. |
| Access address | The system automatically populates the endpoint for the detection service. No manual modification is required. |
| Check request switch | When enabled, the system performs security checks on user inputs. |
| Check the response switch | When enabled, the system performs security checks on model-generated responses. |
| Number of chunked characters in the streaming response | Content detection triggers when the preset character count is reached. For example, "100 characters" means content detection triggers every time 100 characters are generated cumulatively. Important If chunks are too small (for example, 10 characters), detection calls increase. If chunks are too large (for example, 500 characters), partial exposure of prohibited content may occur. |
| Flush wait time | Specify a timeout period. After this period elapses, the system automatically pushes one chunk. For example, "1 second" means the system detects and returns generated content after waiting for one second. |
| Illegal content response message | The message prompt returned to users when the system detects prohibited content. |
| Input Detection Service | The system automatically generates the name of the Alibaba Cloud Content Security service used to detect whether user inputs comply with regulations. |
| Output Detection Service | The system automatically generates the name of the Alibaba Cloud Content Security service used to detect whether model outputs comply with regulations. |

OpenTrek de
4. In the left-side navigation pane, click **Model API**.
5. In the model API list, click the target model API name or click **View** in the **Operation**
column, then click the **Policy Configuration** tab.
6. Click **AI Content Safety** on the **Policy Configuration** tab.
7. In the **AI Content Security Configuration** section, configure the relevant parameters,
then click **Save configuration**.

| Protection level | Sets the risk-level interception threshold for content moderation. max: Detect content but do not intercept (record only). high: Intercept high-risk content only. medium: Intercept content with medium risk or higher. low: Intercept content with low risk or higher. |
|---|---|

| Parameter | Description |
|---|---|
| Service Name | Enter a service name. |
| Large Model Provider | Select an LLM provider, such as OpenAI, Alibaba Cloud Bailian, and Bean package. Important The LLM capabilities provided by the AI service are not directly exposed by the AI gateway. Before you use the service, assess the applicability and reliability of the service and ensure that your behavior fully complies with relevant laws, regulations, and service agreements. Alibaba Cloud is not liable for any consequences arising from the violation of the above provisions. |

de OpenTrek

### AI services

#### Create an AI service

This topic describes how to create an AI service.

**Background information**

You can quickly create an AI service to quickly configure and release a third-party large language model (LLM), such as an OpenAI or Alibaba Cloud Model Studio model. This enables you to centrally manage, authenticate, and limit access to LLMs.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **AI Service**.
5. On the **AI Service** page, click **Create AI Service**.
6. On the **Create AI Service** page, configure the following parameters and click **Create**.

| Model Agreement | Select an API protocol used to communicate with the backend model. Valid values: OpenAI/V1 and Native protocol. |
|---|---|
| Service address | Enter the API address of the LLM service. |
| Service Description | Enter the description of the AI service. |
| API Key | Enter the API key used to call the LLM. You can enter multiple API keys for load balancing or disaster recovery. |
| Enable health check | After you enable health check, the system periodically checks the health of service nodes and isolates unhealthy nodes. |
| Check the agreement | Select the health check protocol. Valid values: HTTP: HTTP health checks simulate how a web browser accesses resources by sending HTTP requests to backend servers to verify their health. TCP: TCP health checks send SYN packets to backend servers to check whether the ports of the backend servers are available to receive requests. |
| Check path | The HTTP path for health check, such as /health or /ping . Note This parameter is available only when Check the agreement is set to HTTP. |
| Check the Host | The HTTP Host header for health check. Note This parameter is available only when Check the agreement is set to HTTP. |

OpenTrek de

| Expected status code | The HTTP status codes used to determine whether the backend servers are healthy. Note This parameter is available only when Check the agreement is set to HTTP. |
|---|---|
| Check interval (seconds) | The interval between two consecutive health checks. |
| Timeout (seconds) | The response timeout period. If a backend server does not return a response within the specified time period, the backend server is considered unhealthy. |
| Health threshold | If the number of times that a backend server consecutively passes health checks reaches the healthy threshold, the backend server is considered healthy. |
| Unhealthy threshold | If the number of times that a backend server consecutively fails to pass health checks reaches the unhealthy threshold, the backend server is considered unhealthy. |

de OpenTrek

#### Manage AI services

This topic describes how to view, modify, and delete AI services.

**View the details of an AI service**

After you create an AI service, you can view the details of the AI service. If a large number of services are available, you can filter or search for services to improve the efficiency.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **AI Service**.
5. Optional. On the **AI Service** page, you can specify the **Service Name** or **Large Model**
**Provider** filter condition to filter AI services.
6. In the AI service list, click the name of an AI service to go to the **AI Service Details** page.
The **Service Details** tab is displayed. In the **Basic Information** section, you can view **Service Name**, **Creation time**, and
**Service Description**.
In the **AI Service Configuration** section, you can view **Large Model Provider**, **Model**
**Agreement**, **Service address**, and **API Key**.
OpenTrek de In the **health check Configuration** section, you can view **Status**, **Check the**
**agreement**, **Timeout duration**, **Inspection interval**, **Load balancing algorithm**,
**Health threshold**, and **Unhealthy threshold**.

**Modify an AI service**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **AI Service**.
5. In the AI service list, click **Editor** in the **Operation** column of the target AI service.
6. On the **AI Editing Service** page, modify the parameters and click **Save**.

**Note**

You cannot change the name of the AI service.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **AI Service**.
5. Delete AI services.
Delete an AI service: In the AI service list, click **Delete** in the **Operation** column of the target AI service. Delete multiple AI services at a time: In the AI service list, select the target AI services and click **Batch delete** below the list.
6. In the message that appears, click **Confirm**.

### Route management

A route is the primary method by which a gateway exposes its access capabilities. This topic describes how to manage routes.

**Create a route**

**Note**

After you configure the route, the system supports both HTTP and WebSocket access.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Route management**, and then click **Create route**.
5. In the **Create route** panel, configure the parameters as prompted and click **OK**.

| Configuration item | Description |
|---|---|
| Route name | The custom name of the route. Important The route name must be globally unique. |
| Route path | Configure the path and matching method for route matching. The matching methods include prefix match, exact match, and regex match. |
| Request method | The request method to match. If you do not specify a request method, the system matches all request methods during route matching. |
| Request header | The request headers to match. Multiple headers are associated by using the AND operator. |
| Request query | The request queries to match. Multiple queries are associated by using the AND operator. |
| Backend service | The associated backend services. You can configure weights for backend services. |
| Domain name | The domain names used to access the route. You can select multiple domain names. Note The combination of a domain name and a base path is globally unique and cannot be duplicated. |

de OpenTrek

**View route details**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. (Optional) On the **Route management** page, you can filter routes based on **route name**
or **service name**.
6. In the route list, click a route name to go to the **Route details** page. On this page, you can
view information about **route details**, **plugin configuration**, **policy configuration**, and
**usage guide**.
OpenTrek de On the **Route details** tab, you can view the detailed information about the route, including **basic information**, **associated services**, and **associated domain names**. Click the **Plugin configuration** tab to manage plugins bound to the current route. Click
**Add plugin** to bind a plugin to the route. For more information, see Create a plugin.

**Note**

On the route list page, you can also click **Plugin configuration** in the **Actions** column to go directly to the **Plugin configuration** tab. Click the **Policy configuration** tab to configure policy rewriting, header modification, timeout settings, and degradation. For more information, see Policy configuration. Click the **Usage guide** tab to view the **configuration information**, **parameter**
**settings**, and **usage examples** of the route.
**Configuration information**: includes **domain name**, **model selection**, **consumer**,
and **external access address**. The system allows you to modify the **domain name**,
**model selection**, and **consumer**.
**Parameter settings**: include **temperature**, **top_p**, and **max_tokens**. The system
allows you to adjust parameter values.
**Usage examples**: View sample code for using the route. You can click the **Copy**
button on the right to obtain the sample code.

**Modify a route**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. In the route list, click **Edit** in the **Actions** column of the target route.
6. In the **Edit route** panel, modify the route information as needed and click **OK**.

**Delete a route**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. Delete a route.
Delete one route: In the route list, click **Delete** in the **Actions** column of the target route. Delete multiple routes: In the route list, select the target routes and click **Batch delete**.
6. In the **Note** dialog box that appears, click **OK**.

**Debug a route**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.

| Parameter | Description |
|---|---|
| Domain name | Select the domain name bound to this route. |
| Model | Select an AI model that has been connected from the drop-down list. |
| Consumer | Select the client identity that calls this API. |
| Streaming request | Use the toggle to enable or disable streaming output. If you enable streaming requests, the system returns results character by character. |
| Prompt | Enter a user question or instruction to trigger model inference. |
| System prompt | Enter the system prompt to define the model's role and behavior guidelines. |
| max tokens _ | Control the maximum number of tokens to generate. |
| top p _ | The nucleus sampling parameter that controls the diversity of generation. |
| temperature | Control the randomness of generation. A higher value indicates more randomness. |

de OpenTrek
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. In the route list, click **Debug** in the **Actions** column of the target route.
6. In the **AI model debugging** panel, configure the parameters and click **Send request**.

**Note**

Click **Fill in historical parameters** to quickly reproduce the previous configuration. Click **Reset** to quickly restore default values.
7. In the **Model response** section, view the generated result.
OpenTrek de

**Note**

By default, the system retains context across multiple calls. You can click **Clear**
**memory** to clear the context.

### Policy configuration

#### Configure a rewrite policy

A rewrite policy modifies the path and host domain of a request before it is forwarded to a backend service. You can use rewrite policies to meet specific business and architectural requirements. These policies give you precise control over the request path and host domain to ensure that requests are correctly routed to the appropriate service or endpoint.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. On the Routing Management page, find the route that you want to manage and click its
name to go to the **Routing Details** page.
6. On the **Routing Details** page, click the **Policy Configuration** tab.
7. On the **Policy Configuration** tab, click **Rewrite**. Click the **Enable** button. Configure **Path**
**Rewrite** and **Host Rewrite**, then click **Save**.

**Note**

For more information about configuring **Path Rewrite** and **Host Rewrite**, see Configure a rewrite policy.

**Rewrite policies**

Rewriting is primarily used to modify the path (Path) and host domain (Host) of an original request.

**Path rewrite**

For path (Path) rewriting, AI Gateway supports two rewrite patterns: exact rewrite and prefix rewrite.

**Exact rewrite**

An exact rewrite completely modifies the path of the original request.

**Example**

If the original request path is `/app/test` but the path forwarded to the backend service must be `/foo/bar` , the recommended configuration is as follows: Routing match condition: The match pattern is an exact match, and the path is

```
 /app/test .
```

de OpenTrek Rewrite: The rewrite pattern is an exact rewrite, and the path is `/foo/bar` .

**Important**

An exact rewrite requires the routing match pattern to be an exact match or a regular expression match. Exact rewrite is not supported for prefix matches.

**Prefix rewrite**

A prefix rewrite modifies the path prefix of an original request.

**Example 1**

If the original request path is `/app/test` but the path forwarded to the backend service must be `/test` , the recommended configuration is as follows: Routing match condition: The match pattern is a prefix match, and the path is `/app` . Rewrite: The rewrite pattern is a prefix rewrite, and the path is / .

**Example 2**

If the original request path is `/v1/test` but the path forwarded to the backend service must be `/v2/test` , the recommended configuration is as follows: Routing match condition: The match pattern is a prefix match, and the path is `/v1` . Rewrite: The rewrite pattern is a prefix rewrite, and the path is `/v2` .

**Important**

A prefix rewrite requires the routing match pattern to be a prefix match. Exact matches or regular expression matches do not support prefix rewrite. Because a prefix match pattern matches all requests with the specified path prefix, confirm that all these requests must be rewritten when you configure the prefix rewrite. If not, use an exact rewrite.

**Host domain rewrite**

For host domain (Host) rewriting, AI Gateway supports exact rewrite. For example, if the host of the original request is `test.com` but the host forwarded to the backend service is `dev.com` , you can set the rewrite host to `dev.com` in the rewrite policy.

#### Configure a header modification policy

A header modification policy modifies the headers of a request before it is forwarded to a backend service. The policy can also modify the headers of a response before it is returned to a client. This topic describes how to set request and response headers in AI Gateway.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.

| Parameter | Description |
|---|---|
| Enable | On: The gateway controls request and response headers. Off: The gateway does not control request and response headers. |
| Add Request Header | Click Add, enter a header name and value to add a header to the request. Note If the header already exists, the new value is appended to the existing value, separated by a comma (,). |
| Modify Request Header | Click Add, enter a header name and value to modify a specified header in the request. Note If the specified header does not exist, a new header is added with the specified name and value. If the specified header exists, its value is overwritten. |
| Delete Request Header | Click Add and enter a header name to delete a specified header from the request. |
| Add Response Header | Click Add, enter a header name and value to add a header to the response. Note If the header already exists, the new value is appended to the existing value, separated by a comma (,). |

OpenTrek de
5. On the Routing Management page, find the route that you want to manage and click its
name to go to the **Routing Details** page.
6. On the **Routing Details** page, click the **Policy Configuration** tab.
7. On the **Policy Configuration** tab, click **Header Modification**.
8. In the **Header Modification** section, configure the parameters and then click **Save**.

| Modify Response Header | Click Add, enter a header name and value to modify a specified header in the response. Note If the specified header does not exist, a new header is added with the specified name and value. If the specified header exists, its value is overwritten. |
|---|---|
| Delete Response Header | Click Add and enter a header name to delete a specified header from the response. |

de OpenTrek

**Verify the results**

For example, to add a test response header, configure the settings as shown in the following figure. Run the following command to send a test request:

```bash
curl -I http://121.196.XX.XX/demo/item/list // Gateway entry IP address
```

The response contains the header `test:demo` :

| Parameter | Description |
|---|---|
| Enable | The switch to enable the route timeout policy. Enable: The gateway route timeout policy is enabled. Disable: The gateway route timeout policy is disabled. |

OpenTrek de

```
HTTP/1.1 200 OK x-content-type-options: nosniff x-xss-protection: 1; mode=block cache-control: no-cache, no-store, max-age=0, must-revalidate pragma: no-cache expires: 0 x-frame-options: DENY content-type: application/json content-length: 86 date: Tue, 30 Nov 2021 03:03:04 GMT x-envoy-upstream-service-time: 4 test: demo server: istio-envoy
```

#### Configure a timeout policy

AI Gateway provides route-level timeout settings. You can set the maximum time that the gateway waits for a response for a specific route. If the gateway does not receive a response from the backend service within this time, the gateway returns a response with an HTTP status code of 504 Gateway Timeout to the client. This topic describes how to configure a route timeout policy for AI Gateway.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. On the Routing Management page, find the route that you want to manage and click its
name to go to the **Routing Details** page.
6. On the **Routing Details** page, click the **Policy Configuration** tab.
7. On the **Policy Configuration** tab, click **Timeout**.
8. In the **Timeout** area, configure the parameters, and then click **Save**.

**Note**

After you configure and enable the timeout policy, verify that the timeout rule takes effect.

| Timeout | The timeout period for the current route, in seconds. Note If this parameter is set to 0 or the timeout policy is disabled, the gateway waits indefinitely for a response. |
|---|---|

| Parameter | Description |
|---|---|
| Enable | A switch to enable the routing degradation policy. Enable: The gateway routing degradation policy takes effect. Disable: The gateway routing degradation policy is disabled. |
| Response Codes For Degradation | Select 4xx or 5xx. 4xx: Client errors, such as 404 and 403. 5xx: Server errors, such as 500 and 502. |

de OpenTrek

#### Configure a degradation policy

Degradation is a fault tolerance mechanism. When a backend service experiences issues, such as timeouts or error responses, the system automatically switches over to a preconfigured degradation service. This process ensures system availability and prevents a complete interruption.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Route Management**.
5. On the Routing Management page, find the route that you want to manage and click its
name to go to the **Routing Details** page.
6. On the **Routing Details** page, click the **Policy Configuration** tab.
7. On the **Policy Configuration** tab, click **Degradation**.
8. In the **Degradation** section, configure the parameters and click **Save**.

**Important**

A degradation service should be simple, stable, and respond quickly. Verify the degradation logic in a staging environment before publishing to the production environment. Degradation is used only to ensure availability and should not affect core business logic.

| Degradation Service | Select a backup service to use as the degradation target. |
|---|---|

| Configuration item | Description |
|---|---|
| Name | The custom service name. |
| Source Type | Select Nacos service discovery, DNS domain name, Fixed Address, or Kubernetes cluster. Nacos service discovery: The AI Gateway dynamically retrieves the service instance list from the Nacos registration center. DNS domain name: The AI Gateway supports using DNS resolution results as backend service addresses. Fixed Address: If the service lacks a service discovery mechanism, manually add the backend node address of the service. Kubernetes cluster: The backend service is deployed in a Kubernetes cluster and accessed through internal cluster Services. This applies to containerized applications. |

OpenTrek de

### Service management

#### Create a service

You must add an existing service to the gateway and register it as a candidate routing service so that the gateway can obtain the service endpoint. The AI Gateway supports adding services in three forms: fixed endpoint, DNS domain name, and Kubernetes cluster.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Service**.
5. On the **Service List** page, select the **Service** tab, then click **Create Service**.
6. On the **Create Service** page, configure the following parameters, then click **Submission**.

**Note**

The AI Gateway does not modify your request. When the request is forwarded to the backend domain name service, the system does not rewrite the Host header to the domain name you configured.

| Select orange | Note This parameter appears only when you select Nacos service discovery for Source Type. Select the service orange. For instructions on creating service origins, see Create an origin. |
|---|---|
| Group name | Note This parameter appears only when you select Nacos service discovery for Source Type. The service group identifier in Nacos to logically isolate services across different environments or teams. |
| Namespace ID | Note This parameter appears only when you select Nacos service discovery for Source Type. The Nacos namespace to isolate configurations and services further, commonly used in multi- tenant or multi-project scenarios. |
| Service name | Note This parameter appears only when you select Nacos service discovery for Source Type. Retrieve the registered service list from the selected Nacos instance, group, and namespace. |

de OpenTrek

| Load balancing algorithm | Note This parameter appears only when you select Nacos service discovery for Source Type. Valid values: Round robin Random Least requests Consistent hashing Least connections |
|---|---|
| Node | When you select DNS domain name for Source Type, enter Domain Name and Port. Domain Name: Configure the domain name of the service. Port: The access port for the service domain name. When you select Fixed Address for Source Type, enter Host name/IP and Port. Host name/IP: The backend node address of the service, which can be a host name or IP address. Port: The port of the backend node address for the service. |
| Service address | Note This parameter appears only when you select Kubernetes cluster for Source Type. Select the full domain name of the backend service. |
| Protocol Type | Select the protocol type for the service: HTTP or HTTPS. |

OpenTrek de

| Proxy server | Note This parameter appears when you select DNS domain name for Source Type and HTTPS for Protocol Type. Select a proxy server based on your actual requirements. If no proxy servers are available, create one by following the instructions in Proxy servers. |
|---|---|
| Enable Health Check | If you enable health checks, the system actively sends requests (such as TCP connections or HTTP GET requests) to probe whether service nodes are alive and directly determine service availability. |
| Health check protocol | HTTP: Health checks simulate browser access by sending requests to verify the health of server applications. TCP: Health checks detect whether server ports are alive by sending SYN handshake packets. |
| Health Check Path | The URI for the health check page file. We recommend checking static pages. Note This parameter appears only when you select HTTP for Health Check Protocol. |
| Health Check Domain Name (Optional) | Use only letters, numbers, hyphens (-), and periods (.). By default, no HOST field is set. Note This parameter appears only when you select HTTP for Health Check Protocol. |
| Normal status code | The HTTP status code that indicates a healthy check result. Note This parameter appears only when you select HTTP for Health Check Protocol. |

de OpenTrek

| Response timeout duration | The maximum timeout period for each health check response. Treat any timeout as unhealthy. |
|---|---|
| Interval time | The time interval between two consecutive health checks. |
| Health threshold | The number of consecutive successful health checks required for an ECS instance to transition from unhealthy to healthy. |
| Unhealthy threshold | The number of consecutive failed health checks required for an ECS instance to transition from healthy to unhealthy. |

OpenTrek de

#### Manage services

The backend node endpoints of services with fixed origin addresses in the AI Gateway may change. The gateway cannot dynamically obtain these endpoints. You must manually update the service’s backend node endpoints so the gateway can retrieve them. This topic describes how to view, edit, and delete services.

**View service details**

After you create a service, you can view it. If you have many services, use filters or search to locate services efficiently.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Services**.
5. (Optional) On the **Services** tab, filter services quickly by entering keywords in the **Service**
**Name** field.
6. In the service list, click a service name to open the **Service Details** page. You can view
information about **service details** and **plugin configurations**. On the **Service Details** tab, view detailed service information including **basic**
**information**, **node list**, and **associated routes**.
In the **Basic Information** section, view the service **name**, **origin type**, and **protocol**
**type**.
In the **Node List** section, view the primary **hostname/IP** and **port**. In the **Associated Routes** section, view the **route name** and **route path**. Click the **Plugin Configuration** tab to manage plugins bound to the current service. Click **Add Plugin** to bind a plugin to the service. For more information, see Create a plugin.

| Configuration item | Description |
|---|---|
| Origin type | You can select only Nacos. |

de OpenTrek

**Note**

On the service list page, you can also click **Plugin Configuration** in the **Actions** column to jump directly to the **Plugin Configuration** tab.

**Edit a service**

1. On the **Services** tab, click **Edit** in the **Actions** column for the service you want to modify.
2. In the **Edit Service** panel, update the service parameters and click **Submit**.

**Note**

You can edit static IP services and DNS services that you created yourself. You cannot edit other service types, such as Kubernetes services.

**Delete a service**

1. Delete a service.
Delete individually: On the **Services** tab, click **Delete** in the **Actions** column for the target service. Delete in batch: On the **Services** tab, select the target services and click **Batch Delete**.
2. In the pop-up **Note** dialog box, click **OK**.

#### Create an origin

The AI Gateway currently supports only the origin type **Nacos**. Before you introduce a service, you must first import the service origin—that is, create an origin—and provide relevant origin information. This allows the gateway to obtain instances and service information from the specified origin. You can then manage service instances under that origin.

**Prerequisites**

You have deployed a Nacos service.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Service**.
5. On the **Service** page, select the **Origin** tab.
6. On the **Origin** tab, click **Create Origin**.
7. On the **Create Origin** page, configure the following parameters and then click **OK**.

| Origin name | Customize the name based on your scenario. The name can contain up to 128 characters. |
|---|---|
| Origin description | The description of the origin. |
| Registration center address | The addresses of nodes. Separate multiple nodes with commas. Example: 127.0.0.1:8848. |
| Authentication method | Supports No authentication, Alibaba Cloud authentication, and Simple authentication. No authentication: Select No authentication if the Nacos service does not enable authentication. Alibaba Cloud authentication: Select Alibaba Cloud authentication if you purchased a public cloud Nacos service. You must also configure the AccessKey/SecretKey. Simple authentication: Select Simple authentication if the Nacos service does not enable authentication. You must also configure the Username/Password. Example: nacos/nacos. |

OpenTrek de

#### Manage origins

This topic describes how to view, modify, and delete an origin.

**View origin details**

After you add an origin to the platform, you can view its details.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Service**.
5. On the **Service** page, select the **Origin** tab.
6. On the **Origin** tab, click the name in the **Origin ID/Name** column to view the origin details.

**Modify an origin**

1. In the list, find the origin that you want to modify and click **Edit** in the **Actions** column.
2. Modify the relevant parameters and click **OK** to complete the modification.

| Configuration item | Description |
|---|---|
| Name | A custom name for the consumer. The name must be unique within the instance. |
| Description | A description of the consumer. |
| Authentication Method | The authentication method that the consumer supports. Currently, only API Key is supported. |

de OpenTrek

**Note**

The configuration of an origin may change over time. The platform provides the feature to modify origins so that you can adjust their parameters. To ensure the stability of downstream services, the system rejects edit requests if the origin has associated downstream services.

**Delete an origin**

1. On the **Origin** tab, click **Delete** in the **Actions** column for the target origin.
2. In the dialog box that appears, click **OK**.

**Note**

To ensure the stability of downstream services, the system rejects delete requests if the origin has associated downstream services.

### Consumer management

#### Create a consumer

AI Gateway uses consumers to enable authentication for routes and APIs. This topic describes how to create a consumer in the AI Gateway console.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. On the **Consumers** page, click **Create Consumer**.
6. In the **Create Consumer** panel, configure the following parameters and click **OK**.

| Token | The custom API key credential. System Generated: The system automatically generates the API key credential. Custom: Specify a custom API key credential and its source. |
|---|---|

OpenTrek de

#### View consumer details

This topic describes how to view the details of a consumer.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. On the **Consumers** page, click a consumer name to open the **Consumer Details** page.
This page displays the consumer's **Basic Configuration** and **Consumer Authorization** information. On the **Basic Configuration** tab, you can view the consumer's **Basic Information** and
**Consumer Authentication** information.
**Basic Information**: This section displays the **Consumer ID**, **Consumer Name**,
**Consumer Description**, and **Consumer Status**.
**Consumer Authentication**: This section displays the **Authentication Method** and
**Token** information.
Click the **Consumer Authorization** tab to manage authorizations for the consumer. For more information, see Authorization management.

#### Authorization management

This topic describes how to manage API consumer authorization. This ensures that only consumers whose identities and permissions are verified can access service resources.

**Authorize consumers**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. On the **Consumer** page, use one of the following methods to go to the **Consumer**
**Authorization** tab.
Method 1: Find the consumer that you want to manage and click **Authorization** in the
**Operation** column.
Method 2: Find the consumer that you want to manage and click its name. On the
**Consumer Details** page, click the **Consumer Authorization** tab.
de OpenTrek
6. On the **Consumer Authorization** tab, you can authorize the consumer to use routes,
Model Context Protocol (MCP) services, and model APIs. Route authorization: On the **Routing** tab, click **Authorization**, select one or more routes from the **Routing** drop-down list, and then click **Determine**.

**Note**

If no route is available, create one. For more information, see Route management. MCP service authorization: On the **MCP Service** tab, click **Authorization**, select one or more MCP services from the **MCP Service** drop-down list, and then click **Determine**.

**Note**

If no MCP service is available, create one. For more information, see Manage MCP services. Model API authorization: On the **Model API** tab, click **Authorization**, select one or more model APIs from the **Model API** drop-down list, and then click **Determine**.

**Note**

If no model API is available, create one. For more information, see Create a model API.

**Revoke authorization**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. On the **Consumer** page, use one of the following methods to go to the **Consumer**
**Authorization** tab:
Method 1: Find the consumer that you want to manage and click **Authorize** in the
**Operation** column.
Method 2: Find the consumer that you want to manage and click its name. On the
**Consumer Details** page, click the **Consumer Authorization** tab.
6. On the **Consumer Authorization** tab, you can revoke route, MCP service, and model API
authorization. Revoke route authorization: On the **Routing** tab, click **Delete** in the **Operation** column. In the message that appears, click **OK**. Revoke MCP service authorization: On the **MCP Service** tab, click **Delete** in the
**Operation** column. In the message that appears, click **OK**.
Revoke model API authorization: On the **Model API** tab, click **Delete** in the **Operation** column. In the message that appears, click **OK**. This topic describes how to modify a consumer configuration.

#### Modify a consumer

OpenTrek de

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. On the **Consumers** page, locate the target consumer and click **Edit** in the **Operation**
column.
6. In the **Edit Consumer** pane, edit the parameters and click **OK**.

#### Delete consumers

This topic describes how to delete AI Gateway consumers.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Consumer**.
5. Delete consumers.
To delete a single consumer: On the **Consumers** page, click **Delete** in the **Actions** column for the target consumer. To delete multiple consumers: On the **Consumers** page, select the checkboxes for the target consumers and click **Batch Delete**.
6. In the **Notice** dialog box, click **OK**.

### Manage MCP services

Model Context Protocol (MCP) is an open-source protocol that standardizes how applications provide context to large language models (LLMs). It acts like a "USB-C port" for AI applications, allowing models to flexibly and securely connect to various data sources and tools. This topic describes how to create and use MCP services.

**Features**

MCP service management enables a smooth migration from RESTful APIs to MCP services. It supports access through both Server-Sent Events (SSE) and Streamable HTTP protocols. This feature also integrates a consumer-based authentication mechanism, which provides a foundation for enterprise-level API administration.

**Create an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**, and then click **Create MCP**
**Service**.

| Parameter |  | Description |  |  | Example |  |  |
|---|---|---|---|---|---|---|---|
| Name |  | Enter a custom name for the MCP service. Note The name of an MCP service must be unique within the same gateway instance. |  |  | demo |  |  |
| Description |  | Enter a description for the MCP service. |  |  | Test |  |  |
| MCP Endpoint | Domain Name | The domain name used to access the MCP service. You can select multiple domain names. Note If no domain names are available, click Add Domain Name to the right of the selection box to create one. For more information, see Create a domain name. |  |  | www.aliyun.com |  |  |
|  | Path (SSE) | The path of the MCP service endpoint for SSE. The path is generated based on the service name. |  |  | /mcp- |  |  |
|  |  |  |  |  |  | /mcp- |  |
|  |  |  |  | is | servers/{your-mcp- |  |  |
|  |  |  | rated based on the ce name. |  |  |  |  |
|  |  |  |  |  | server-name}/sse |  |  |
|  | Path (Streamable HTTP) | The path of the MCP endpoint for Streamable HTTP. The path is generated based on the service name. |  |  | /mcp- |  |  |
|  |  |  |  |  |  | /mcp- |  |
|  |  |  |  |  | servers/{your-mcp- |  |  |
|  |  |  | is generated based on ervice name. | n |  |  |  |
|  |  |  |  |  | server-name} |  |  |
| Service Type |  | The type of the MCP tool service. |  |  | You can select OpenAPI, DB, or Direct Routing. |  |  |
| Backend Service |  | Specify the service to which API requests are forwarded. |  |  | test |  |  |

de OpenTrek
5. In the **Create MCP Service** panel, configure the parameters, and then click **Save And**
**Publish**.

| Consumer Authentication | If you enable this feature, only authorized consumers can access the MCP service. | Enabled |
|---|---|---|

OpenTrek de

**View MCP service details**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. (Optional) On the **MCP Management** page, you can quickly filter MCP services by **MCP**
**Service Name** or **MCP Service Type**.
6. In the service list, click the service name or **Details** in the **Actions** column. On the **MCP**
**Details** page, you can view the basic information and configuration details of the MCP
service. On the **Basic Information** tab, you can view the service's **Basic Information** and
**Endpoint Information**.
On the **Tools** tab, you can add tools to the MCP service. For more information, see Add tools to an MCP service. On the **Consumer Authentication** tab, you can set up consumer authentication and authorization for the MCP service. For more information, see Consumer authentication. The **Resources** and **Prompt** tabs are not yet supported.

**Add tools to an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**, and then click **Details** in the
**Actions** column for the target service.
5. On the **Tools** tab, click **Edit Tools** in the upper-right corner of the page.
6. MCP services currently support two methods for adding tools:
Method 1: **Based On A Swagger File** (Recommended) i. **Import Swagger To Create Or Incrementally Update MCP Tools** : Upload an OpenAPI file from your local machine or paste the API definition into the editor, and then click **Generate Now**. ii. **Update And Confirm The MCP Tool List**: You can view the generated MCP tool description file. You can then confirm and modify the information in the file. Method 2: **Custom YAML** You can manually create MCP tools using custom YAML.
7. Click **OK**. On the **Tools** tab, you can view the tool list, along with the tool names,
descriptions, and parameter information. 1. 2. 3.

| Configuration Item | Description |
|---|---|
| Enabled Status | Turns the consumer authorization switch on or off. This feature is disabled by default. |
| Authentication Method | The only supported authentication method for consumer authorization is API Key. An API key is a simple authentication method. When a client makes a request, it must add the credential to the request in a specified way. After the gateway receives the request, it verifies the validity and permissions of the API key. The server assigns a unique string to the client as an access credential. The client submits this API key in the header or as a query parameter with each request. |

de OpenTrek
4. In the navigation pane on the left, select **MCP Management**. Click the name of the target
service or **Details** in the **Actions** column, and then click the **Consumer Authentication** tab.
5. On the **Consumer Authentication** tab, turn on the **Enabled Status** switch for
**Configuration Information**.

**Important**

After you enable consumer authentication, the service cannot be accessed if no authorization relationship is configured.
6. In the **Consumers** area, click **Grant Authorization**, select a consumer, and click **Add**.

**Note**

If no consumers exist, you must first create one before you can grant authorization. For more information, see Create a consumer.

**Debug an MCP service with MCP Inspector**

**Note**

You can start MCP Inspector locally to debug MCP services. MCP Inspector is a debugging tool provided by the MCP community. You can use it to debug the entire flow of an MCP service.
1. Install the Node.js environment.
2. Run the following command to start MCP Inspector: `npx @modelcontextprotocol/inspector`

```
node build/index.js .
```

3. Select a transport type. Set **Transport Type** to **SSE**.
4. Enter the `URL` . You can find the URL on the right side of the MCP service details page.
5. (Optional) If consumer authentication is configured, click **Authentication** to expand the
authorization configuration, and then enter the consumer's token. OpenTrek de
6. Click **Connect**. After a successful connection, the **List Tools** button appears in the middle
of the page. Click **List Tools** to retrieve all the tools for the MCP service.
7. (Optional) To debug a specific tool, click the tool name, enter the required parameters on
the right, and click **Run Tool** to start the tool calling test.

**Modify an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. In the service list, find the service that you want to modify and click **Edit** in its **Actions**
column.
6. In the **Edit MCP Service** panel, modify the configurations as needed, and then click **Save**
**And Publish**.

**Delete an MCP service**

1. 2. 3.
4. In the navigation pane on the left, select **MCP Management**.
5. In the service list, find the service that you want to delete and click **Delete** in its **Actions**
column.
6. In the **Notice** dialog box that appears, click **OK**.

### Plugin management

#### Create a plugin

Plugin configuration allows you to apply various plugins in the AI Gateway to different domain objects and their combinations. For example, you can configure a throttling plugin on a route or a service. This provides greater flexibility for plugin configuration in the AI Gateway. The AI Gateway provides an Extension Marketplace with built-in plugins for authentication, traffic control, security protection, and other functions. It also supports adding custom plug-ins to enable flexible and personalized capability extensions for the gateway.

**Background information**

The AI Gateway contains a variety of plugins. It also includes the following four domain objects. MCP_SERVER In the AI Gateway, you can configure the same type of plugin multiple times on the same domain object or combination of domain objects. For example, you can configure multiple throttling rules for the same route.

**Supported plugin types**

de OpenTrek AI ai-load-balancer ai-history ai-json-resp model-mapper model-router oidc ext-auth opa cors waf cluster-key-rate-limit key-rate-limit OpenTrek de geo-ip Plug-ins that users add to the Extension Marketplace are for personal use only. For more information about how to add custom plug-ins, see Custom Plug-In.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. Go to the plugin creation page.

**Note**

The system provides five entry points for creating plugins, each suitable for different scenarios. You can choose any one as needed. Plugins created via the main entry point apply to the current instance. Plugins created via quick entry points apply to the current service, route, domain name, or MCP service.
**Main entry point**: Use this entry point to create a plugin for the current instance.
a. In the left-side navigation pane, select **Plugin**, then click **Create Plugin**. b. On the **Create Plugin** page, select the corresponding plugin.
**Quick entry point 1**: Use this entry point to create a plugin for a specific route or a
combination of domain objects that include this route. a. In the left-side navigation pane, click **Route**. b. On the **Route Management** page, click **Plugin Configuration** in the **Operation** column for the target route. c. On the **Plugin Configuration** tab, click **AddPlugin** to go to the **Create Plugin** page and select the corresponding plugin for creation.
**Quick entry point 2**: Use this entry point to create a plugin for a specific service or a
combination of domain objects that include this service. a. In the left-side navigation pane, click **Service**. b. On the **Service List** page, click **Plugin Configuration** in the **Operation** column for the target service.

| Parameter | Description |
|---|---|
| Scope | Select Global or Local. Global: By default, the system applies this plugin to the entire instance. Local: You must specify the domain object or combination of domain objects to which you want to bind this plugin. Note that the available domain objects vary depending on the plugin type. If you specify a combination of domain objects, the relationship between these objects is AND. For example, if this local plugin is bound to both a route and a consumer, the system executes the plugin only for requests that carry the token of the consumer and match the route. |
| Binding Type | This parameter appears only when you set Scope to Local. Select Route, Service, Domain name, or MCP SERVER. _ |

de OpenTrek c. On the **Plugin Configuration** tab, click **AddPlugin** to go to the **Create Plugin** page and select the corresponding plugin for creation.
**Quick entry point 3**: Use this entry point to create a plugin for a specific domain name
or a combination of domain objects that include this domain name. a. In the left-side navigation pane, click **Domain name**. b. On the **Domain Management** page, click **Plugin Configuration** in the **Operation** column for the target domain name. c. On the **Plugin Configuration** tab, click **AddPlugin** to go to the **Create Plugin** page and select the corresponding plugin for creation.
**Quick entry point 4**: Use this entry point to create a plugin for a specific MCP service or
a combination of domain objects that include this MCP service. a. In the left-side navigation pane, click **MCP Management**. b. On the **MCP Management** page, click the name of the target MCP service or click
**Details** in the **Operation** column.
c. Click the **Plugin Configuration** tab, then click **AddPlugin** to go to the **Create Plugin** page and select the corresponding plugin for creation.
5. After configuring the relevant information based on the selected plugin, click **OK**.

**Note**

The following procedure takes creating a CORS plugin as an example. The procedures for other plugins are similar.

| Bind Route | This parameter appears only when you set Binding Type to Route. Select the route to which you want to bind the plugin. If no routes are available, create a route. For more information, see Route management. |
|---|---|
| Bind Service | This parameter appears only when you set Binding Type to Service. Select the service to which you want to bind the plugin. If no services are available, create a custom service. For more information, see Create a service. |
| Bind Domain | This parameter appears only when you set Binding Type to Domain name. Select the domain name to which you want to bind the plugin. If no domain names are available, associate a domain name. For more information, see Create a domain name. |
| Bind MCP Server | This parameter appears only when you set Binding Type to MCP SERVER. _ Select the MCP service to which you want to bind the plugin. If no MCP services are available, create an MCP service. For more information, see Manage MCP services. |
| cors | Configure the CORS plugin. Click View Documentation or see Cross-origin resource sharing for configuration instructions. |

OpenTrek de

#### Custom Plug-In

The AI Gateway allows you to add custom plug-ins for flexible and personalized capability expansion. This topic describes how to add a custom plug-in.

**Prerequisites**

You have Create a gateway instance. You have prepared the OCI image or file URL for the custom plug-in.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, select **Plugin**, then click **Create Plugin**.
5. On the **Create Plugin** page, click **Add Custom Plug-In**.
6. In the **Add Custom Plug-In** panel, configure the following parameters, then click **Save**.

| Parameter | Description |
|---|---|
| Plug-in name | The unique identifier of the plug-in, used for code reference and log tracing. |
| Plug-in title | Enter a readable display name for front-end interface presentation. |
| Plug-in description | A detailed explanation of the plug-in’s function and purpose. |
| Image URL | Image URL: oci:// : References an OCI image. http[s]:// : References a remotely hosted Wasm file. |
| Image pull policy | Controls the update policy for the Wasm module, affecting startup speed and version consistency. Never: Never actively pulls the image; uses only locally available images. IfNotPresent: Pulls the image only if it is not present locally. Always: Forces pulling the latest image every time the pod starts. |
| Image pull secret | Authentication credentials required to access a private image repository. |
| Plug-in execution phase | Determines when the plug-in executes in the request trace: UNSPECIFIED PHASE: Inserts the plug-in at _ the end of the plug-in filter chain, before the router. AUTHN: Inserts the plug-in before the Istio authentication filter. AUTHZ: Inserts the plug-in after the Istio authentication filter and before the Istio authorization filter. STATS: Inserts the plug-in after the Istio authorization filter and before the Istio statistics filter. |

de OpenTrek

| Plug-in execution priority | Under the same phase, a higher value means earlier request processing but later response processing. |
|---|---|

OpenTrek de

**More operations**

After adding a custom plug-in, you can **modify** or **delete** it. Modify a plug-in i. Click on the plug-in card and select **Modify**. ii. In the **Edit Custom Plug-In** panel, edit the plug-in’s basic information, **configuration**
**example**, and **plug-in documentation**. Click **Save** when finished.

**Note**

**Configuration example** must use YAML format.
**Plug-in documentation** must use Markdown format.
Delete a plug-in i. Click on the plug-in card and select **Delete**. ii. In the dialog box that appears, click **OK**.

**Note**

After you delete a plug-in, objects configured with this plug-in are automatically unbound.

#### Manage plug-ins

This topic describes how to manage plug-ins.

**View plug-in details**

After you create a plug-in, you can view its details.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Plugin Management**.
5. (Optional) On the **Plug-in Management** page, you can filter plug-ins by **Plug-in ID** or
**Plug-in Type**.
6. In the plug-in list, click a plug-in ID to go to the **Plug-in Configuration Details** page. You
can view the **Basic Information** and **Plug-in Information**.
**Basic Information**: Includes the **Plug-in Type**, **Plug-in Status**, and **Applicable**
**Scope**.
**Plug-in Information**: Includes detailed information about the plug-in.

**Enable or disable a plug-in**

de OpenTrek
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Plugin Management**.
5. In the plug-in list, find the plug-in that you want to manage and click **Enable** or **Disable** in
the **Actions** column.
6. In the **Prompt** dialog box, click **OK**.

**Modify a plug-in**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Plugin Management**.
5. In the plug-in list, find the plug-in that you want to modify and click **Edit** in the **Actions**
column.
6. On the **Edit Plug-in** page, modify the configuration information and click **OK**.

**Delete a plug-in**

You can delete a plug-in when you no longer need it.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Plugin Management**.
5. In the plug-in list, find the plug-in that you want to delete and click **Delete** in the **Actions**
column.
6. In the **Prompt** dialog box, click **OK**.

#### AI

##### AI proxy

**Features**

The `AI proxy` plugin implements AI proxy features based on the OpenAI API contract. It currently supports AI service providers (SPs), such as OpenAI, Azure OpenAI, Moonshot, and Qwen.

**Important**

If the URI of the request ends with `/v1/chat/completions` , it is a text generation scenario. The plugin parses the request body using the OpenAI text generation protocol and then transforms it into the protocol of the target Large Language Model (LLM) provider.

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| provider | object | Required | - | Configures the information of the target AI service provider. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| type | string | Required | - | The name of the AI service provider. |
| apiTokens | array of string | Optional | - | The tokens used for authentication when accessing the AI service. If you configure multiple tokens, the plugin randomly selects one for each request. Some service providers support only one token. |

OpenTrek de If the URI of the request ends with `/v1/embeddings` , it is a text embedding scenario. The plugin parses the request body using the OpenAI text embedding protocol and then transforms it into the protocol of the target LLM provider.

**Runtime properties**

Plugin execution phase: `Default phase` . Plugin execution priority: `100` .

**Configuration fields**

**Basic configurations**

The configuration fields for `provider` are as follows:

|  | timeout |  | number | Optional | - | The timeout period for accessing the AI service, in milliseconds. The default value is 120000, which is 2 minutes. This configuration is currently used only for retrieving contextual information and does not affect the actual forwarding of requests to the large model. |
|---|---|---|---|---|---|---|
|  | modelMapping |  | map of string | Optional | - | The AI model mapping table. It maps the model name in the request to a model name supported by the service provider. Prefix matching is supported. For example, use "gpt-3-*" to match all models whose names start with "gpt-3-". You can use "*" as a key to configure a universal fallback mapping. If the target name for the mapping is an empty string (""), the original model name is retained. |
|  |  | modelMapping |  |  |  |  |

de OpenTrek

|  | protocol |  | string | Optional | - | The API contract that the plugin provides. The following values are supported: openai (default, uses the OpenAI API contract) and original (uses the native API contract of the target service provider). |
|---|---|---|---|---|---|---|
|  | context |  | object | Optional | - | Configures the contextual information for the AI chat. |
|  | customSettings |  | array of customSetting | Optional | - | Specifies parameters to overwrite or fill in for AI requests. |
|  |  | customSettings |  |  |  |  |
|  | failover |  | object | Optional | - | Configures the failover policy for apiTokens. When an apiToken becomes unavailable, it is removed from the list. It is added back to the list after it passes a health check. |
|  | retryOnFailure |  | object | Optional | - | Immediately retries a request if it fails. |
|  |  | retryOnFailure |  |  |  |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| fileUrl | string | Required | - | The URL of the file that stores the AI chat context. Only plain text file content is supported. |

OpenTrek de The configuration fields for `context` are as follows:

| serviceName | string | Required | - | The full name of the AI gateway backend service that corresponds to the URL. |
|---|---|---|---|---|
| servicePort | number | Required | - | The access port of the AI gateway backend service that corresponds to the URL. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| name | string | Required | - | The name of the parameter to set, such as max tokens . _ |
| value | string/int/float/bo ol | Required | - | The value of the parameter to set, such as 0. |
| mode | string | Optional | "auto" | The mode for setting the parameter. Valid values are "auto" and "raw". If set to "auto", the parameter name is automatically rewritten based on the protocol. If set to "raw", no rewriting or restriction checks are performed. |

de OpenTrek The configuration fields for `customSettings` are as follows:

| overwrite | bool | Optional | true | If set to false, the parameter is filled only when the user has not set it. Otherwise, the existing user setting for the parameter is overwritten. |
|---|---|---|---|---|

| settingName |  |
|---|---|
| max tokens _ | i |

| u set | name | to | max tokens _ |  |
|---|---|---|---|---|
|  |  |  |  | is replace |

| setting Name | openai | baidu | spark | qwen | gemini | hunyu an | claude | minim ax |
|---|---|---|---|---|---|---|---|---|
| max to _ kens | max to _ kens | max ou _ tput tok _ ens | max to _ kens | max to _ kens | maxOut putToke ns | none | max to _ kens | tokens _ to gene _ rate |
| temper ature | temper ature | temper ature | temper ature | temper ature | temper ature | Temper ature | temper ature | temper ature |
| top p _ | top p _ | top p _ | none | top p _ | topP | TopP | top p _ | top p _ |
| top k _ | none | none | top k _ | none | topK | none | top k _ | none |
| seed | seed | none | none | seed | none | none | none | none |

| parameters | subpat |
|---|---|

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de The custom setting feature replaces the corresponding field based on the `name` and `name` is not in this table, the corresponding protocol does not support the parameter, or the raw mode is not set, the configuration does not take effect. If you enable the raw mode, the custom setting directly uses the input `name` and `value` to modify the JSON content of the request without any restrictions or modifications to the parameter name. For most protocols, the custom setting modifies or fills parameters at the root path of the JSON content. For the `qwen` protocol, the AI proxy configures parameters The configuration fields for `failover` are as follows:

| enabled | bool | Optional | false | Specifies whether to enable the failover mechanism for apiTokens. |
|---|---|---|---|---|
| failureThreshold | int | Optional | 3 | The threshold of consecutive failed requests that triggers a failover, in number of times. |
| successThreshold | int | Optional | 1 | The success threshold for health checks, in number of times. |
| healthCheckInter val | int | Optional | 5000 | The interval for health checks, in milliseconds. |
| healthCheckTime out | int | Optional | 5000 | The timeout period for health checks, in milliseconds. |
| healthCheckMode l | string | Required when failover is enabled |  | The model used for health checks. |
| failoverOnStatus | array of string | Optional: | ["4.*", "5.*"] | The status codes of the original requests that require a failover. Regular expression matching is supported. |

|  |  | ["4.*", |  |
|---|---|---|---|
|  | "5.*"] |  |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

de OpenTrek The configuration fields for `retryOnFailure` are as follows:

| enabled | bool | Optional | false | Specifies whether to retry failed requests. |
|---|---|---|---|---|
| maxRetries | int | Optional | 1 | The maximum number of retries. |
| retryTimeout | int | Optional | 30000 | The timeout period for retries, in milliseconds. |
| retryOnStatus | array of string | Optional | ["4.*", "5.*"] | The status codes of the original requests that require a retry. Regular expression matching is supported. |

|  |  | ["4.*", |  |
|---|---|---|---|
|  | "5.*"] |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | openaiCustomUr l |  | string | Optional | - | The base URL based on the OpenAI protocol, for example, www.example.co m/myai/v1. |
|  |  | openaiCustomUr |  |  |  |  |
|  | l |  |  |  |  |  |
|  | responseJsonSc hema |  | object | Optional | - | Defines the JSON Schema that the OpenAI response must meet. Note that only specific models currently support this usage. |
|  |  | responseJsonSc | obj |  |  |  |
|  | hema |  |  |  |  |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de

**Provider-specific configurations**

**OpenAI**

The `type` for OpenAI is `openai` . Its specific configuration fields are as follows:

**Azure OpenAI**

The `type` for Azure OpenAI is `azure` . Its specific configuration fields are as follows:

| azureServiceUr l | string | Required | - | The URL of the Azure OpenAI service. It must include the api-version query parameter. |
|---|---|---|---|---|

|  |  | azureServiceUr |  |
|---|---|---|---|
|  | l |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | moonshotFileId |  | string | Optional | - | The ID of a file uploaded to Moonshot through the file API. Its content is used as the context for the AI chat. This field cannot be configured at the same time as the context field. |
|  |  | moonshotFileId |  |  |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | qwenEnableSear ch |  | boolean | Optional | - | Specifies whether to enable the built- in web search feature of Qwen. |
|  |  | qwenEnableSear | b |  |  |  |
|  | ch |  |  |  |  |  |

de OpenTrek

**Important**

Azure OpenAI supports only one API token.

**Moonshot**

The `type` for Moonshot is `moonshot` . Its specific configuration fields are as follows:

**Qwen**

The `type` for Qwen is `qwen` . Its specific configuration fields are as follows:

|  | qwenFileIds |  | array of string | Optional | - | The ID of a file uploaded to Dashscope through the file API. Its content is used as the context for the AI chat. This field cannot be configured at the same time as the context field. |
|---|---|---|---|---|---|---|
|  | qwenEnableComp atible |  | boolean | Optional | false | Enables the Qwen compatible mode. After you enable this mode, the compatible mode API of Qwen is called, and no modifications are made to the request or response. |
|  |  | qwenEnableComp | boole |  |  |  |
|  | atible |  |  |  |  |  |

OpenTrek de

**Baichuan AI**

The `type` for Baichuan AI is `baichuan` . It has no specific configuration fields.

**Yi**

The `type` for Yi is `yi` . It has no specific configuration fields.

**Zhipu AI**

The `type` for Zhipu AI is `zhipuai` . It has no specific configuration fields.

**DeepSeek**

The `type` for DeepSeek is `deepseek` . It has no specific configuration fields.

**Groq**

The `type` for Groq is `groq` . It has no specific configuration fields.

**Baidu ERNIE Bot**

The `type` for Baidu ERNIE Bot is `baidu` . It has no specific configuration fields.

**360 AI Brain**

The `type` for 360 AI Brain is `ai360` . It has no specific configuration fields.

**GitHub Models**

The `type` for GitHub Models is `github` . It has no specific configuration fields.

**Mistral**

|  | Name |  | Data type | Required | Default value |  | Description |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | minimaxApiType |  | string | Select one from v2 and pro. | v2 |  | v2 represents the ChatCompletion v2 API, and pro represents the ChatCompletion Pro API. |  |  |
|  |  | minimaxApiType |  |  |  |  |  |  |  |
|  | minimaxGroupId |  | string | Required when minimaxApiTyp e is pro. | - |  | When minimaxApiTyp e is set to pro, the ChatCompletion Pro API is used, and you must set the groupID. |  |  |
|  |  |  |  |  |  |  |  | minimaxApiTyp |  |
|  |  |  |  |  |  |  | e |  |  |

| minimaxApiTyp |  |
|---|---|

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | claudeVersion |  | string | Optional | - | The API version of the Claude service. The default is 2023- 06-01. |
|  |  | claudeVersion |  |  |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | ollamaServerHo st |  | string | Required | - | The host address of the Ollama server. |
|  |  | ollamaServerHo | s |  |  |  |
|  | st |  |  |  |  |  |
|  | ollamaServerPo rt |  | number | Required | - | The port number of the Ollama server. The default is 11434. |
|  |  | ollamaServerPo | n |  |  |  |
|  | rt |  |  |  |  |  |

de OpenTrek The `type` for Mistral is `mistral` . It has no specific configuration fields.

**MiniMax**

The `type` for MiniMax is `minimax` . Its specific configuration fields are as follows:

**Anthropic Claude**

The `type` for Anthropic Claude is `claude` . Its specific configuration fields are as follows:

**Ollama**

The `type` for Ollama is `ollama` . Its specific configuration fields are as follows:

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | hunyuanAuthId |  | string | Required | - | The ID used for v3 authentication in Hunyuan. |
|  | hunyuanAuthKey |  | string | Required | - | The key used for v3 authentication in Hunyuan. |
|  |  | hunyuanAuthKey |  |  |  |  |

|  |  | hunyuanAuthId |
|---|---|---|

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | cloudflareAcco untId |  | string | Required | - | Cloudflare Account ID |
|  |  | cloudflareAcco | strin |  |  |  |
|  | untId |  |  |  |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | geminiSafetySe tting |  | map of string | Optional | - | The content filtering and safety level settings for Gemini AI. For more information, see Safety settings. |
|  |  | geminiSafetySe | map |  |  |  |
|  | tting |  |  |  |  |  |

OpenTrek de

**Hunyuan**

The `type` for Hunyuan is `hunyuan` . Its specific configuration fields are as follows:

**Stepfun**

The `type` for Stepfun is `stepfun` . It has no specific configuration fields.

**Cloudflare Workers AI**

The `type` for Cloudflare Workers AI is `cloudflare` . Its specific configuration fields are as follows:

**Spark**

The `type` for Spark is `spark` . It has no specific configuration fields. For the iFLYTEK Spark Cognitive Large Model, the value of the `apiTokens` field is `APIKey:APISecret` . You must enter your APIKey and APISecret, separated by a colon ( : ).

**Gemini**

The `type` for Gemini is `gemini` . Its specific configuration fields are as follows:

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| targetLang | string | Required | - | The target language required by the DeepL translation service. |

de OpenTrek

**DeepL**

The `type` for DeepL is `deepl` . Its specific configuration fields are as follows:

**Cohere**

The `type` for Cohere is `cohere` . It has no specific configuration fields.

**Together-AI**

The `type` for Together-AI is `together-ai` . It has no specific configuration fields.

**Usage examples**

**Use the OpenAI protocol to proxy the Azure OpenAI service**

This example uses the basic Azure OpenAI service without any contextual configuration.

```
provider:
  type: azure
  apiTokens:
    - "YOUR_AZURE_OPENAI_API_TOKEN"
  azureServiceUrl:
"https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat ompletions?api-version=2024-02-15-preview",
```

**Sample request**

```json
{
  "model": "gpt-3",
  "messages": [
    {
      "role": "user",
      "content": "Hello, who are you?"
    }
```

`],`

```json
  "temperature": 0.3
}
```

**Sample response**

```json
{
  "choices": [
    {
"contentfilterreslts" {
```

OpenTrek de

```json
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      },
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "Hello! I am an AI assistant that can answer your questions and prov
ide help. How can I help you?",
        "role": "assistant"
      }
    }
```

`],`

```json
  "created": 1714807624,
  "id": "chatcmpl-abcdefg1234567890",
  "model": "gpt-35-turbo-16k",
  "object": "chat.completion",
  "prompt_filter_results": [
    {
      "prompt_index": 0,
      "content_filter_results": {
        "hate": {
          "filtered": false,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": false,
          "severity": "safe"
        },
        "sexual": {
          "filtered": false,
          "severity": "safe"
        },
        "violence": {
          "filtered": false,
          "severity": "safe"
        }
      }
    }
```

`],` de OpenTrek `],`

```json
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 40,
    "prompt_tokens": 15,
    "total_tokens": 55
  }
}
```

**Use the OpenAI protocol to proxy the Qwen service**

This example uses the Qwen service and configures model mapping from OpenAI large models to Qwen models.

```
provider:
  type: qwen
  apiTokens:
    - "YOUR_QWEN_API_TOKEN"
  modelMapping:
    'gpt-3': "qwen-turbo"
    'gpt-35-turbo': "qwen-plus"
    'gpt-4-turbo': "qwen-max"
    'gpt-4-*': "qwen-max"
    'gpt-4o': "qwen-vl-plus"
    'text-embedding-v1': 'text-embedding-v1'
    '*': "qwen-turbo"
```

**Sample AI chat request**

URL: http://your-domain/v1/chat/completions Sample request:

```json
{
  "model": "gpt-3",
  "messages": [
    {
      "role": "user",
      "content": "Hello, who are you?"
    }
```

`],`

```json
  "temperature": 0.3
}
```

Sample response: OpenTrek de

```json
{
  "id": "c2518bd3-0f46-97d1-be34-bb5777cb3108",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I am Qwen, an AI assistant developed by Alibaba Cloud. I can answer
various questions, provide information, and have conversations with users. How can I he lp you?"
      },
      "finish_reason": "stop"
    }
```

`],`

```json
  "created": 1715175072,
  "model": "qwen-turbo",
  "object": "chat.completion",
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 33,
    "total_tokens": 57
  }
}
```

**Sample multi-modal model API request (for** `qwen-vl-plus` **and** `qwen-vl-max`

**models)**

URL: http://your-domain/v1/chat/completions Sample request:

```json
{
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://dashscope.oss-cn-
beijing.aliyuncs.com/images/dog_and_girl.jpeg"
                    }
                },
                {
                    "type": "text",
                    "text": "Where is this picture from?"
                }
```

]

```
        }
```

`],`

```json
    "temperature": 0.3
}
```

de OpenTrek Sample response:

```json
{
    "id": "17c5955d-af9c-9f28-bbde-293a9c9a3515",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": [
                    {
                        "text": "This photo shows a woman and a dog on a beach. Because
I cannot obtain specific geographical location information, I cannot determine which be ach this is. However, based on the visual content, it could be a sandy coastline in a c oastal area with waves lapping the shore. Such scenes can be found in many beautiful se aside locations around the world. If you need more precise information, provide more ba ckground or detailed descriptions."
                    }
```

]

```json
            },
            "finish_reason": "stop"
        }
```

`],`

```json
    "created": 1723949230,
    "model": "qwen-vl-plus",
    "object": "chat.completion",
    "usage": {
        "prompt_tokens": 1279,
        "completion_tokens": 78
    }
}
```

**Example text embedding request**

URL: http://your-domain/v1/embeddings Sample request:

```json
{
  "model": "text-embedding-v1",
  "input": "Hello"
}
```

Example response: OpenTrek de

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -1.0437825918197632,
        5.208984375,
        3.0483806133270264,
        -1.7897135019302368,
        -2.0107421875,
        ...,
        0.8125,
        -1.1759847402572632,
        0.8174641728401184,
        1.0432943105697632,
        -0.5885213017463684
```

]

```
    }
```

`],`

```json
  "model": "text-embedding-v1",
  "usage": {
    "prompt_tokens": 1,
    "total_tokens": 1
  }
}
```

**Use Qwen with plain text contextual information**

This example uses the Qwen service and configures plain text contextual information.

```
provider:
  type: qwen
  apiTokens:
    - "YOUR_QWEN_API_TOKEN"
  modelMapping:
    "*": "qwen-turbo"
  context:
    - fileUrl: "http://file.default.svc.cluster.local/ai/context.txt",
      serviceName: "file.dns",
      servicePort: 80
```

**Sample request**

de OpenTrek

```json
{
  "model": "gpt-3",
  "messages": [
    {
      "role": "user",
      "content": "Please summarize the copy."
    }
```

`],`

```json
  "temperature": 0.3
}
```

**Sample response**

```json
{
  "id": "cmpl-77861a17681f4987ab8270dbf8001936",
  "object": "chat.completion",
  "created": 9756990,
  "model": "moonshot-v1-128k",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "This copy is about..."
      },
      "finish_reason": "stop"
    }
```

`],`

```json
  "usage": {
    "prompt_tokens": 20181,
    "completion_tokens": 439,
    "total_tokens": 20620
  }
}
```

**Use Qwen with its native file context**

This example uploads a file to Qwen in advance and uses the file content as the context for its AI service.

```
provider:
  type: qwen
  apiTokens:
    - "YOUR_QWEN_API_TOKEN"
  modelMapping:
    "*": "qwen-long" # The file context of Qwen can only be used with the qwen-long mod
```

`el`

```
  qwenFileIds:
  - "file-fe-xxx"
  - "file-fe-yyy"
```

OpenTrek de

**Sample request**

```json
{
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": "Please summarize the copy."
    }
```

`],`

```json
  "temperature": 0.3
}
```

**Sample response**

```json
{
  "output": {
    "choices": [
      {
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": "You have uploaded two files, `context.txt` and `context_2.txt`, b
oth of which seem to contain information about xxxx"
        }
      }
```

]

```json
  },
  "usage": {
    "total_tokens": 2023,
    "output_tokens": 530,
    "input_tokens": 1493
  },
  "request_id": "187e99ba-5b64-9ffe-8f69-01dafbaf6ed7"
}
```

**Use the original protocol to proxy an Alibaba Cloud Model**

**Studio agent application**

```
provider:
 type: qwen
 apiTokens:
 - "YOUR_DASHSCOPE_API_TOKEN"
 protocol: original
```

**Sample request**

de OpenTrek

```json
{
 "input": {
 "prompt": "Introduce Dubbo"
 },
 "parameters":  {},
 "debug": {}
}
```

**Sample response**

```json
{
 "output": {
 "finish_reason": "stop",
 "session_id": "677e7e8fbb874e1b84792b65042e1599",
 "text": "Apache Dubbo is a..."
 },
 "usage": {
 "models": [
 {
 "output_tokens": 449,
 "model_id": "qwen-max",
 "input_tokens": 282
 }
```

]

```json
 },
 "request_id": "b59e45e3-5af4-91df-b7c6-9d746fd3297c"
}
```

**Use the OpenAI protocol to proxy the Doubao large model**

```
provider:
 type: doubao
 apiTokens:
 - YOUR_DOUBAO_API_KEY
 modelMapping:
 '*': YOUR_DOUBAO_ENDPOINT
 timeout: 1200000
```

**Use the original protocol to proxy a Coze application**

```
provider:
 type: coze
 apiTokens:
 - YOUR_COZE_API_KEY
 protocol: original
```

**Use Moonshot with its native file context**

OpenTrek de This example uploads a file to Moonshot in advance and uses the file content as the context for its AI service.

```
provider:
 type: moonshot
 apiTokens:
 - "YOUR_MOONSHOT_API_TOKEN"
 moonshotFileId: "YOUR_MOONSHOT_FILE_ID",
 modelMapping:
 '*': "moonshot-v1-32k"
```

**Sample request**

```json
{
 "model": "gpt-4-turbo",
 "messages": [
 {
 "role": "user",
 "content": "Please summarize the content"
 }
```

`],`

```json
 "temperature": 0.3
}
```

**Sample response**

```json
{
 "id": "cmpl-e5ca873642ca4f5d8b178c1742f9a8e8",
 "object": "chat.completion",
 "created": 1872961,
 "model": "moonshot-v1-128k",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "The content is about a payment platform named 'xxxx'..."
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "usage": {
 "prompt_tokens": 11,
 "completion_tokens": 498,
 "total_tokens": 509
 }
}
```

**Use the OpenAI protocol to proxy the Groq service**

de OpenTrek

```
provider:
 type: groq
 apiTokens:
 - "YOUR_GROQ_API_TOKEN"
```

**Sample request**

```json
{
 "model": "llama3-8b-8192",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

]

```
}
```

**Sample response**

```json
{
 "id": "chatcmpl-26733989-6c52-4056-b7a9-5da791bd7102",
 "object": "chat.completion",
 "created": 1715917967,
 "model": "llama3-8b-8192",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": " Ni Hao! (That's \"hello\" in Chinese!)\n\nI am LLaMA, an AI assistant dev
eloped by Meta AI that can understand and respond to human input in a conversational ma nner. I'm not a human, but a computer program designed to simulate conversations and an swer questions to the best of my ability. I'm happy to chat with you in Chinese or help with any questions or topics you'd like to discuss! "
 },
 "logprobs": null,
 "finish_reason": "stop"
 }
```

`],`

```json
 "usage": {
 "prompt_tokens": 16,
 "prompt_time": 0.005,
 "completion_tokens": 89,
 "completion_time": 0.104,
 "total_tokens": 105,
 "total_time": 0.109
 },
 "system_fingerprint": "fp_dadc9d6142",
 "x_groq": {
 "id": "req_01hy2awmcxfpwbq56qh6svm7qz"
 }
}
```

OpenTrek de

**Use the OpenAI protocol to proxy the Claude service**

```
provider:
 type: claude
 apiTokens:
 - "YOUR_CLAUDE_API_TOKEN"
 version: "2023-06-01"
```

**Sample request**

```json
{
 "model": "claude-3-opus-20240229",
 "max_tokens": 1024,
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

]

```
}
```

**Sample response**

```json
{
 "id": "msg_01Jt3GzyjuzymnxmZERJguLK",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "Hello, I am a chat assistant developed by the artificial intelligence comp
any Anthropic. My name is Claude. I am an intelligent, friendly, and knowledgeable conv ersational system. It's a pleasure to meet you! I can chat with you on various topics, answer questions, provide suggestions, and offer help. I will do my best to give you he lpful responses. I hope we have a pleasant conversation!"
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "created": 1717385918,
 "model": "claude-3-opus-20240229",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 16,
 "completion_tokens": 126,
 "total_tokens": 142
 }
}
```

**Use the OpenAI protocol to proxy the Hunyuan service**

de OpenTrek

```
provider:
 type: "hunyuan"
 hunyuanAuthKey: "<YOUR AUTH KEY>"
 apiTokens:
 - ""
 hunyuanAuthId: "<YOUR AUTH ID>"
 timeout: 1200000
 modelMapping:
 "*": "hunyuan-lite"
```

**Sample request**

Request script:

```json
curl --location 'http://<your higress domain>/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{
 "model": "gpt-3",
 "messages": [
 {
 "role": "system",
 "content": "You are a professional developer!"
 },
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "temperature": 0.3,
 "stream": false
}'
```

**Sample response**

OpenTrek de

```json
{
 "id": "fd140c3e-0b69-4b19-849b-d354d32a6162",
 "choices": [
 {
 "index": 0,
 "delta": {
 "role": "assistant",
 "content": "Hello! I am a professional developer."
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "created": 1717493117,
 "model": "hunyuan-lite",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 15,
 "completion_tokens": 9,
 "total_tokens": 24
 }
}
```

**Use the OpenAI protocol to proxy the Baidu ERNIE Bot service**

```
provider:
 type: baidu
 apiTokens:
 - "YOUR_BAIDU_API_TOKEN"
 modelMapping:
 'gpt-3': "ERNIE-4.0"
 '*': "ERNIE-4.0"
```

**Sample request**

```json
{
 "model": "gpt-4-turbo",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "stream": false
}
```

**Sample response**

de OpenTrek

```json
{
 "id": "as-e90yfg1pk1",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "Hello, I am ERNIE Bot. I can interact with people, answer questions, assis
t with creation, and efficiently help people obtain information, knowledge, and inspira tion."
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "created": 1717251488,
 "model": "ERNIE-4.0",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 4,
 "completion_tokens": 33,
 "total_tokens": 37
 }
}
```

**Use the OpenAI protocol to proxy the MiniMax service**

```
provider:
 type: minimax
 apiTokens:
 - "YOUR_MINIMAX_API_TOKEN"
 modelMapping:
 "gpt-3": "abab6.5s-chat"
 "gpt-4": "abab6.5g-chat"
 "*": "abab6.5t-chat"
```

**Sample request**

```json
{
 "model": "gpt-3",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "stream": false
}
```

**Sample response**

OpenTrek de

```json
{
 "id": "03ac4fcfe1c6cc9c6a60f9d12046e2b4",
 "choices": [
 {
 "finish_reason": "stop",
 "index": 0,
 "message": {
 "content": "Hello, I am a large language model developed by MiniMax, named MM Intellig
ent Assistant. I can help answer questions, provide information, conduct conversations, and perform various language processing tasks. If you have any questions or need help, feel free to let me know!",
 "role": "assistant",
 "name": "MM Intelligent Assistant",
 "audio_content": ""
 }
 }
```

`],`

```json
 "created": 1734155471,
 "model": "abab6.5s-chat",
 "object": "chat.completion",
 "usage": {
 "total_tokens": 116,
 "total_characters": 0,
 "prompt_tokens": 70,
 "completion_tokens": 46
 },
 "input_sensitive": false,
 "output_sensitive": false,
 "input_sensitive_type": 0,
 "output_sensitive_type": 0,
 "output_sensitive_int": 0,
 "base_resp": {
 "status_code": 0,
 "status_msg": ""
 }
}
```

**Use the OpenAI protocol to proxy the GitHub model service**

```
provider:
 type: github
 apiTokens:
 - "YOUR_GITHUB_ACCESS_TOKEN"
 modelMapping:
 "gpt-4o": "gpt-4o"
 "gpt-4": "Phi-3.5-MoE-instruct"
 "gpt-3.5": "cohere-command-r-08-2024"
 "text-embedding-3-large": "text-embedding-3-large"
```

**Sample request**

de OpenTrek

```json
{
 "messages": [
 {
 "role": "system",
 "content": "You are a helpful assistant."
 },
 {
 "role": "user",
 "content": "What is the capital of France?"
 }
```

`],`

```json
 "stream": true,
 "temperature": 1.0,
 "top_p": 1.0,
 "max_tokens": 1000,
 "model": "gpt-4o"
}
```

**Sample response**

```json
{
 "choices": [
 {
 "finish_reason": "stop",
 "index": 0,
 "logprobs": null,
 "message": {
 "content": "The capital of France is Paris.",
 "role": "assistant"
 }
 }
```

`],`

```json
 "created": 1728131051,
 "id": "chatcmpl-AEy7PU2JImdsD1W6Jw8GigZSEnM2u",
 "model": "gpt-4o-2024-08-06",
 "object": "chat.completion",
 "system_fingerprint": "fp_67802d9a6d",
 "usage": {
 "completion_tokens": 7,
 "prompt_tokens": 24,
 "total_tokens": 31
 }
}
```

**Sample text embedding request**

```json
{
 "input": ["first phrase", "second phrase", "third phrase"],
 "model": "text-embedding-3-large"
}
```

Sample response: OpenTrek de

```json
{
 "object": "list",
 "data": [
 {
 "object": "embedding",
 "index": 0,
 "embedding": [
 -0.0012583479,
 0.0020349282,
 ...
 0.012051377,
 -0.0053306012,
 0.0060688322
```

]

```
 }
```

`],`

```json
 "model": "text-embedding-3-large",
 "usage": {
 "prompt_tokens": 6,
 "total_tokens": 6
 }
}
```

**Use the OpenAI protocol to proxy the 360 AI Brain service**

```
provider:
 type: ai360
 apiTokens:
 - "YOUR_360_API_TOKEN"
 modelMapping:
 "gpt-4o": "360gpt-turbo-responsibility-8k"
 "gpt-4": "360gpt2-pro"
 "gpt-3.5": "360gpt-turbo"
 "text-embedding-3-small": "embedding_s1_v1.2"
 "*": "360gpt-pro"
```

**Sample request**

```json
{
 "model": "gpt-4o",
 "messages": [
 {
 "role": "system",
 "content": "You are a professional developer!"
 },
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

]

```
}
```

de OpenTrek

**Sample response**

```json
{
 "choices": [
 {
 "message": {
 "role": "assistant",
 "content": "Hello, I am 360 AI Brain, a large language model. I can help answer variou
s questions, provide information, conduct conversations, and more. How can I help you?"
 },
 "finish_reason": "",
 "index": 0
 }
```

`],`

```json
 "created": 1724257207,
 "id": "5e5c94a2-d989-40b5-9965-5b971db941fe",
 "model": "360gpt-turbo",
 "object": "",
 "usage": {
 "completion_tokens": 33,
 "prompt_tokens": 24,
 "total_tokens": 57
 },
 "messages": [
 {
 "role": "system",
 "content": "You are a professional developer!"
 },
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "context": null
}
```

**Sample text embedding request**

URL: http://your-domain/v1/embeddings Sample request:

```json
{
 "input":["Hello"],
 "model":"text-embedding-3-small"
}
```

Sample response: OpenTrek de

```json
{
 "data": [
 {
 "embedding": [
 -0.011237,
 -0.015433,
 ...,
 -0.028946,
 -0.052778,
 0.003768,
 -0.007917,
 -0.042201
```

`],`

```json
 "index": 0,
 "object": ""
 }
```

`],`

```json
 "model": "embedding_s1_v1.2",
 "object": "",
 "usage": {
 "prompt_tokens": 2,
 "total_tokens": 2
 }
}
```

**Use the OpenAI protocol to proxy the Cloudflare Workers AI**

```
provider:
 type: cloudflare
 apiTokens:
 - "YOUR_WORKERS_AI_API_TOKEN"
 cloudflareAccountId: "YOUR_CLOUDFLARE_ACCOUNT_ID"
 modelMapping:
 "*": "@cf/meta/llama-3-8b-instruct"
```

**Sample request**

```json
{
 "model": "gpt-3.5",
 "max_tokens": 1024,
 "messages": [
 {
 "role": "user",
 "content": "Who are you?"
 }
```

]

```
}
```

**Sample response**

de OpenTrek

```json
{
 "id": "id-1720367803430",
 "object": "chat.completion",
 "created": 1720367803,
 "model": "@cf/meta/llama-3-8b-instruct",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "I am LLaMA, an AI assistant developed by Meta AI that can understand and r
espond to human input in a conversational manner. I'm not a human, but a computer progr am designed to simulate conversation and answer questions to the best of my knowledge. I can be used to generate text on a wide range of topics, from science and history to e ntertainment and culture.\n\nI'm a large language model, which means I've been trained on a massive dataset of text from the internet and can generate human-like responses. I can understand natural language and respond accordingly, making me suitable for tasks s uch as:\n\n* Answering questions on various topics\n* Generating text based on a given prompt\n* Translating text from one language to another\n* Summarizing long pieces of t ext\n* Creating chatbot dialogues\n\nI'm constantly learning and improving, so the more conversations I have with users like you, the better I'll become."
 },
 "logprobs": null,
 "finish_reason": "stop"
 }
```

]

```
}
```

**Use the OpenAI protocol to proxy the Spark service**

```
provider:
 type: spark
 apiTokens:
 - "APIKey:APISecret"
 modelMapping:
 "gpt-4o": "generalv3.5"
 "gpt-4": "generalv3"
 "*": "general"
```

**Sample request**

OpenTrek de

```json
{
 "model": "gpt-4o",
 "messages": [
 {
 "role": "system",
 "content": "You are a professional developer!"
 },
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "stream": false
}
```

**Sample response**

```json
{
 "id": "cha000c23c6@dx190ef0b4b96b8f2532",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "Hello! I am a professional developer skilled in programming and solving te
chnical problems. How can I help you?"
 }
 }
```

`],`

```json
 "created": 1721997415,
 "model": "generalv3.5",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 10,
 "completion_tokens": 19,
 "total_tokens": 29
 }
}
```

**Use the OpenAI protocol to proxy the Gemini service**

de OpenTrek

```json
provider:
 type: gemini
 apiTokens:
 - "YOUR_GEMINI_API_TOKEN"
 modelMapping:
 "*": "gemini-pro"
 geminiSafetySetting:
 "HARM_CATEGORY_SEXUALLY_EXPLICIT" :"BLOCK_NONE"
 "HARM_CATEGORY_HATE_SPEECH" :"BLOCK_NONE"
 "HARM_CATEGORY_HARASSMENT" :"BLOCK_NONE"
 "HARM_CATEGORY_DANGEROUS_CONTENT" :"BLOCK_NONE"
```

**Sample request**

```json
{
 "model": "gpt-3.5",
 "messages": [
 {
 "role": "user",
 "content": "Who are you?"
 }
```

`],`

```json
 "stream": false
}
```

**Sample response**

```json
{
 "id": "chatcmpl-b010867c-0d3f-40ba-95fd-4e8030551aeb",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "I am a large multi-modal model, trained by Google. I am designed to provid
e information and answer questions to the best of my abilities."
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "created": 1722756984,
 "model": "gemini-pro",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 5,
 "completion_tokens": 29,
 "total_tokens": 34
 }
}
```

**Use the OpenAI protocol to proxy the DeepL text translation**

| The model Pro . You c system can |  | model |
|---|---|---|
|  | Pro |  |
| system |  |  |

|  | Free |
|---|---|
| content |  |

OpenTrek de

```
provider:
 type: deepl
 apiTokens:
 - "YOUR_DEEPL_API_TOKEN"
 targetLang: "ZH"
```

**Sample request**

This additional context can improve the quality of the translation.

```json
{
 "model": "Free",
 "messages": [
 {
 "role": "system",
 "content": "money"
 },
 {
 "content": "sit by the bank"
 },
 {
 "content": "a bank in China"
 }
```

]

```
}
```

**Sample response**

```json
{
 "choices": [
 {
 "index": 0,
 "message": { "name": "EN", "role": "assistant", "content": "Act as a bookmaker" }
 },
 {
 "index": 1,
 "message": { "name": "EN", "role": "assistant", "content": "Bank of China" }
 }
```

`],`

```json
 "created": 1722747752,
 "model": "Free",
 "object": "chat.completion",
 "usage": {}
}
```

**Use the OpenAI protocol to proxy the Together-AI service**

de OpenTrek

```
provider:
 type: together-ai
 apiTokens:
 - "YOUR_TOGETHER_AI_API_TOKEN"
 modelMapping:
 "*": "Qwen/Qwen2.5-72B-Instruct-Turbo"
```

**Sample request**

```json
{
 "model": "Qwen/Qwen2.5-72B-Instruct-Turbo",
 "messages": [
 {
 "role": "user",
 "content": "Who are you?"
 }
```

]

```
}
```

**Sample response**

```json
{
 "id": "8f5809d54b73efac",
 "object": "chat.completion",
 "created": 1734785851,
 "model": "Qwen/Qwen2.5-72B-Instruct-Turbo",
 "prompt": [],
 "choices": [
 {
 "finish_reason": "eos",
 "seed": 12830868308626506000,
 "logprobs": null,
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "I am Qwen, a large language model created by Alibaba Cloud. I am designed
to assist users in generating various types of text, such as articles, stories, poems, and more, along with answering questions and providing information on a wide range of t opics. How can I assist you today?",
 "tool_calls": []
 }
 }
```

`],`

```json
 "usage": {
 "prompt_tokens": 33,
 "completion_tokens": 61,
 "total_tokens": 94
 }
}
```

**Complete configuration examples**

OpenTrek de

**Kubernetes example**

The following example shows a complete plugin configuration for using the OpenAI protocol to proxy the Groq service. de OpenTrek

```
apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 namespace: higress-system
spec:
 matchRules:
 - config:
 provider:
 type: groq
 apiTokens:
 - "YOUR_API_TOKEN"
 ingress:
 - groq
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/ai-proxy:1.0.0
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/backend-protocol: HTTPS
 higress.io/destination: groq.dns
 higress.io/proxy-ssl-name: api.groq.com
 higress.io/proxy-ssl-server-name: "on"
 labels:
 higress.io/resource-definer: higress
 name: groq
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - host: <YOUR-DOMAIN>
 http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /
 pathType: Prefix
--apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: default
 namespace: higress-system
spec:
 registries:
 - domain: api.groq.com
 name: groq
 port: 443
 type: dns
```

OpenTrek de
**Sample access**:

```json
curl "http://<YOUR-DOMAIN>/v1/chat/completions" -H "Content-Type: application/json" -d '{
 "model": "llama3-8b-8192",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

]

```
}'
```

**Docker-Compose example**

`docker-compose.yml` configuration file:

```bash
version: '3.7' services:
 envoy:
 image: higress-registry.cn-hangzhou.cr.aliyuncs.com/higress/envoy:1.20
 entrypoint: /usr/local/bin/envoy
 # Enable debug-level logs for easy debugging
 command: -c /etc/envoy/envoy.yaml --component-log-level wasm:debug
 networks:
 - higress-net
 ports:
 - "10000:10000"
 volumes:
 - ./envoy.yaml:/etc/envoy/envoy.yaml
 - ./plugin.wasm:/etc/envoy/plugin.wasm
networks:
 higress-net: {}
```

`envoy.yaml` configuration file:

```
admin:
 address:
 socket_address:
 protocol: TCP
 address: 0.0.0.0
 port_value: 9901
static_resources:
 listeners:
 - name: listener_0
 address:
 socket_address:
 protocol: TCP
 address: 0.0.0.0
 port_value: 10000
 filter_chains:
 - filters:
 - name: envoy.filters.network.http_connection_manager
 typedconfig:
```

de OpenTrek _

```json
 "@type":
type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConne ionManager
 scheme_header_transformation:
 scheme_to_overwrite: https
 stat_prefix: ingress_http
 # Output envoy logs to stdout
 access_log:
 - name: envoy.access_loggers.stdout
 typed_config:
 "@type": type.googleapis.com/envoy.extensions.access_loggers.stream.v3.StdoutAccessLog
 # Modify as required
 route_config:
 name: local_route
 virtual_hosts:
 - name: local_service
 domains: [ "*" ]
 routes:
 - match:
 prefix: "/"
 route:
 cluster: claude
 timeout: 300s
 http_filters:
 - name: claude
 typed_config:
 "@type": type.googleapis.com/udpa.type.v1.TypedStruct
 type_url: type.googleapis.com/envoy.extensions.filters.http.wasm.v3.Wasm
 value:
 config:
 name: claude
 vm_config:
 runtime: envoy.wasm.runtime.v8
 code:
 local:
 filename: /etc/envoy/plugin.wasm
 configuration:
 "@type": "type.googleapis.com/google.protobuf.StringValue"
 value: | # Plugin configuration
 {
 "provider": {
 "type": "claude",
 "apiTokens": [
 "YOUR_API_TOKEN"
```

]

```
 }
 }
 - name: envoy.filters.http.router
 clusters:
 - name: claude
 connect_timeout: 30s
 type: LOGICAL_DNS
 dns_lookup_family: V4_ONLY
 lb_policy: ROUND_ROBIN
```

| gin, such as | key-auth |  |
|---|---|---|
| ai-statistics |  |  |
|  |  | plugin |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de

```json
 load_assignment:
 cluster_name: claude
 endpoints:
 - lb_endpoints:
 - endpoint:
 address:
 socket_address:
 address: api.anthropic.com # API endpoint
 port_value: 443
 transport_socket:
 name: envoy.transport_sockets.tls
 typed_config:
 "@type":
type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext
 "sni": "api.anthropic.com"
```

**Sample access**:

```json
curl "http://localhost:10000/v1/chat/completions" -H "Content-Type: application/json" -d '{
 "model": "claude-3-opus-20240229",
 "max_tokens": 1024,
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

]

```
}'
```

##### AI quota

**Features**

The `ai-quota` plugin applies rate limiting to specific consumers based on an assigned quota. The plugin also supports quota management, which includes querying, refreshing, increasing, and decreasing quotas. token statistics.

**Runtime properties**

The plugin runs in the `Default phase` with an execution priority of `750` .

|  | redis key pref _ _ ix |  | string | Optional | chat quota: _ | The prefix for the quota Redis key. |
|---|---|---|---|---|---|---|
|  |  | redis key pref _ _ | s |  |  |  |
|  | ix |  |  |  |  |  |
|  | admin consumer _ |  | string | Required | - | The consumer name that is granted permission to manage quotas. |
|  |  | admin consumer _ |  |  |  |  |
|  | admin path _ |  | string | Optional | /quota | The path prefix for quota management requests. |
|  | redis |  | object | Yes | - | Redis configuration. |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| service name _ | string | Required | - | The Redis service name. This must be the full FQDN, including the service type. Examples: my- redis.dns, redis.my- ns.svc.cluster.loc al. |
| service port _ | int | No | The default value is 80 for a static service. For other service types, the default is 6379. | The service port for the Redis service. |
| username | string | No | - | The Redis username. |
| password | string | No | - | The Redis password. |
| timeout | int | No | 1000 | The Redis connection timeout in milliseconds. |

de OpenTrek The following table describes the configuration fields for `redis` . OpenTrek de

**Configuration examples**

**Limit rates based on the apikey parameter**

```
redis_key_prefix: "chat_quota:" admin_consumer: consumer3 admin_path: /quota redis:
 service_name: redis-service.default.svc.cluster.local
 service_port: 6379
 timeout: 2000
```

**Refresh a quota**

If the request URL suffix matches `admin_path`, you can update the quota. For example, assume the plugin is active on the `example.com/v1/chat/completions` route. To update the quota, run the following command:

```bash
curl https://example.com/v1/chat/completions/quota/refresh -H "Authorization: Bearer cr edential3" -d "consumer=consumer1&quota=10000"
```

The value of the `chat_quota:consumer1` key in Redis is refreshed to 10000.

**Query a quota**

To query the quota for a specific user, run the following command:

```bash
curl https://example.com/v1/chat/completions/quota?consumer=consumer1 -H "Authorization: Bearer credential3"
```

The command returns the following: {"quota": 10000, "consumer": "consumer1"}

**Increase or decrease a quota**

You can adjust a specific user's quota.

```bash
curl https://example.com/v1/chat/completions/quota/delta -d "consumer=consumer1&value=100" -H "Authorization: Bearer credential3"
```

This command increases the value of the `chat_quota:consumer1` key in Redis by 100. To decrease the quota, use a negative value.

**Configuring access for model parameter-based routing**

When routing is configured based on the `model` parameter in the request body, accessing the quota API as described previously will result in a 404 error. This happens because the quota API does not follow the OpenAI body protocol and cannot extract the `model` parameter. To hit a route that matches a specific `model` parameter, add the `x-higress-llm-model` request header. For example:

```bash
### This example shows how to refresh a quota. The same method applies to other operati
ons. curl https://example.com/v1/chat/completions/quota/refresh -H 'x-higress-llm-model: dee pseek-r1' -H "Authorization: Bearer credential3" -d "consumer=consumer1&quota=10000"
```

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|
| serviceName | string | required | - | The name of the service. |
| servicePort | string | required | - | The port of the service. |
| serviceHost | string | required | - | The domain name of the Alibaba Cloud Content Moderation endpoint. |
| accessKey | string | required | - | The Alibaba Cloud AccessKey. |
| secretKey | string | required | - | The Alibaba Cloud SecretKey. |
| checkRequest | bool | optional | false | Check whether the request content complies with policies. |
| checkResponse | bool | optional | false | Check whether the LLM response content complies with policies. When enabled, streaming responses become non- streaming. |

de OpenTrek This ensures the request hits the route that matches the `deepseek-r1` model parameter. Make sure the route's method and path matching rules also match the quota API.

##### AI Content Moderation

This topic describes how to ensure AI application content complies with legal and regulatory requirements by integrating with the input and output of the Alibaba Cloud Content Moderation LLM.

**Execution properties**

Execution phase for this plugin: `default phase` . Plugin execution priority: `300` .

**Configuration instructions**

| requestCheckServ ice |  | string |  | optional | llm query moderation _ _ |  | Specify the Alibaba Cloud Content Moderation service used to detect input content. |
|---|---|---|---|---|---|---|---|
| responseCheckSer vice |  | string |  | optional | llm response moderatio _ _ n |  | Specify the Alibaba Cloud Content Moderation service used to detect output content. |
| requestContentJs onPath |  | string |  |  | messages.@reverse.0. content |  | Specify the JSONPath to the content to be checked in the request body. |
|  |  |  |  |  |  | messages.@reverse.0. | JSONPa conten |
|  |  |  |  | optional | content |  |  |
| responseContentJ sonPath |  | string |  |  | choices.0.message.co ntent |  | Specify the JSONPath to the content to be checked in the response body. |
|  |  |  |  |  |  | choices.0.message.co | JSON cont |
|  |  |  |  | optional | ntent |  |  |
| responseStreamCo |  |  |  |  | choices.0.delta.cont |  | Specify the JSONPath to the content to be checked in the streaming response body. |
|  | responseStreamCo |  |  |  |  | choices.0.delta.cont | co |
| ntentJsonPath |  | string |  | optional | ent |  |  |
| denyCode |  | int |  | optional | 200 |  | The response status code when the content is illegal. |
| denyMessage |  | string |  | optional | For streaming or non- streaming responses in OpenAI format, the response content is the recommended reply from Alibaba Cloud Content Moderation. |  | The response content when the content is illegal. |

|  | requestCheckServ | s |
|---|---|---|
| ice |  |  |

|  | responseCheckSer | str |
|---|---|---|
| vice |  |  |

|  | requestContentJs | strin |
|---|---|---|
| onPath |  |  |

|  | responseContentJ | string |
|---|---|---|
| sonPath |  |  |

OpenTrek de

| credentialType | string | optional | access key _ Note Access the Content Moderation service directly by using the AccessKey pair. | The credential type used to access the Content Moderation service. Valid values: access key and _ oidc role arn. _ _ |
|---|---|---|---|---|
| rrsaInfoServiceN ame | string | optional | rrsa-info-server.higress- system.svc.cluster.local Note higress-system is the namespace of the instance. You must modify this value based on your actual namespace. | The domain name of the service that obtains STS RRSA information when credentialType is set to oidc role arn. _ _ |
| rrsaInfoServiceP ort | string | optional | 18080 | The port of the service that obtains STS RRSA information when credentialType is set to oidc role arn. _ _ |
| bufferLimit | string | optional | 100 | The number of characters. |
| bufferFlushTimeI nterval | string | optional | 1 | The timeout period. |

|  | rrsaInfoServiceN | s |
|---|---|---|
| ame |  |  |

|  | rrsaInfoServiceP | s |
|---|---|---|
| ort |  |  |

|  | bufferFlushTimeI | string |
|---|---|---|
| nterval |  |  |

de OpenTrek

**Configuration example - Access_Key**

**Prerequisites**

1. Because the plugin calls Alibaba Cloud Content Moderation service, you must first create a
DNS-type service. For more information, see Create a service.
2. You need a route that is configured for the LLM API. For more information, see Create a
route. OpenTrek de

**Note**

LLM API: A route whose upstream service is an LLM service is a route for the LLM API.
3. Click **Plugin configuration** in the **Actions** column of the target route to go to the
configured plugin list. Then, click **Add plugin** to go to the **Create plugin** page where you can view the list of configurable plugins.
4. Click **ai-security-guard** to go to the **Create plugin: ai-security-guard** page.
5. Configure **ai-security-guard** based on your scenario requirements.

**Check whether the input content complies with regulations**

**(access_key)**

```bash
serviceName: yundun-green-service.dns servicePort: 80 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" accessKey: "XXXXXXXXX" secretKey: "XXXXXXXXXXXXXXX" checkRequest: true
# default check service(option)
requestCheckService: "dc_llm_query_moderation"
```

**Check whether the input and output comply with regulations**

```bash
serviceName: yundun-green-service.dns servicePort: 80 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" accessKey: "XXXXXXXXX" secretKey: "XXXXXXXXXXXXXXX" checkRequest: true checkResponse: true
# default check service(option)
requestCheckService: "dc_llm_query_moderation" responseCheckService: "dc_llm_response_moderation"
```

**Specify a custom Content Moderation service**

You may need to configure different detection rules for different scenarios. You can achieve this by configuring different Content Moderation services for different domains, routes, or services. As shown in the following figure, a detection service named llm_query_moderation_01 is created. The detection rules of this service are modified based on those of llm_query_moderation. Next, perform the following configuration at the domain, route, or service level to specify the use of the rules in the custom llm_query_moderation_01 for detection. de OpenTrek

```
serviceName: yundun-green-service.dns servicePort: 80 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" accessKey: "XXXXXXXXX" secretKey: "XXXXXXXXXXXXXXX" checkRequest: true requestCheckService: llm_query_moderation_01
```

**Configure non-OpenAI protocols (for example, Alibaba Cloud**

**Model Studio App)**

```
serviceName: yundun-green-service.dns servicePort: 80 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" accessKey: "XXXXXXXXX" secretKey: "XXXXXXXXXXXXXXX" checkRequest: true checkResponse: true requestContentJsonPath: "input.prompt" responseContentJsonPath: "output.text" denyCode: 200
```

`denyMessage: "`很抱歉，我无法回答您的问题"

**Configure streaming responses**

```
---
### Cache forced flush wait time, unit: s
bufferFlushTimeInterval: 1
### Supported number of characters
bufferLimit: 1000 checkRequest: false checkResponse: true credentialType: "oidc_role_arn" rrsaInfoServiceName: "rrsa-info-server.higress-system.svc.cluster.local" rrsaInfoServicePort: 18080 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" serviceName: "yundun-green-service.dns" servicePort: 80
```

**Prerequisites**

Make sure that the ACK cluster where the target instance resides has enabled RRSA support. Make sure that you have created a RAM role corresponding to the ACK cluster OIDC provider, and the ARN of the RAM role follows the rule: ack-fluid-${ack-id}. Make sure that the namespace where the target instance resides has the label podidentity.alibabacloud.com/injection=on. If this label is not configured, run the following command to add it. Replace $target_ns with the name of the namespace where the instance resides. OpenTrek de

```bash
kubectl label namespace ${target_ns} pod-identity.alibabacloud.com/injection=on --ove rwrite
```

Create an ingress that points to the upstream service: rrsa-infoserver.${target_ns}.svc.cluster.local:18080.

```
apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
  annotations:
    higress.io/destination: rrsa-info-server.${target_ns}.svc.cluster.local:18080
    higress.io/ignore-path-case: "false"
  generation: 2
  labels:
    higress.io/resource-definer: higress
    higress.io/internal: true
  name: rrsa-info-server.internal
  resourceVersion: "26189979"
  uid: 4f5d3a02-b29d-4050-bba9-e956a49bfb67
spec:
  ingressClassName: higress
  rules:
  - host: higress-rrsa-info-server.io
    http:
      paths:
      - backend:
          resource:
            apiGroup: networking.higress.io
            kind: McpBridge
            name: default
        path: /get_json
        pathType: Prefix
```

**Scenario 1: Check whether the input content complies with**

**regulations**

**Note**

All subsequent scenarios also support access_key and rrsa. The configuration method is the same. This document does not provide examples for rrsa.

```bash
serviceName: yundun-green-service.dns servicePort: 80 serviceHost: "greenprivate-biz.cn-*****-*****-d01.inter.env38.shuguang.com" credentialType: "oidc_role_arn" rrsaInfoServiceName: "rrsa-info-server.higress-system.svc.cluster.local" rrsaInfoServicePort: 18080 checkRequest: true
# default check service(option)
requestCheckService: "dc_llm_query_moderation"
```

de OpenTrek For other scenarios, refer to the usage method of access_key described earlier. The ai-security-guard plugin provides the following monitoring metrics: `ai_sec_request_deny` : The number of requests that failed content security detection. `ai_sec_response_deny` : The number of requests that failed model response security detection.

**Tracing**

If you enable tracing, the ai-security-guard plugin adds the following attributes to the request span: `ai_sec_risklabel` : The risk type that the request matches. `ai_sec_deny_phase` : The phase in which the system detects a risk for the request. Valid values: request and response.

**Request example**

```json
curl http://localhost/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
```

`"content": "`这是一段非法内容"

```
    }
```

]

```
}'
```

The system sends the request content to Alibaba Cloud Content Moderation for detection. If the detection result indicates that the content is illegal, the gateway returns a response similar to the following:

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| attributes | []Attribute | Optional | - | The information to record in the log or span. |

OpenTrek de

```json
{
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "gpt-4o-mini",
    "system_fingerprint": "fp_44709d6fcb",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
```

`"content": "`作为一名人工智能助手，我不能提供涉及色情、暴力、政治等敏感话题的内容。如果您有其他相关问题，欢迎您提问。`",`

```json
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
```

]

```
}
```

##### AI statistics

**Introduction**

This plugin provides basic AI observability capabilities, including metrics, logs, and traces. It must be used with the ai-proxy plugin. If the ai-proxy plugin is not used, this plugin requires additional configuration to function.

**Runtime properties**

Plugin execution phase: `Default phase` Plugin execution priority: `200` . By default, the plugin provides the following basic observability values for requests that comply with the OpenAI protocol format. No special configuration is required: Metrics: Provides metrics such as input tokens, output tokens, response time (RT) for the first token in streaming requests, and total request RT. These metrics can be observed across four dimensions: gateway, routing, service, and model. Logs: Provides fields such as `input_token`, `output_token`, `model`, `llm_service_duration`, and `llm_first_token_duration`. You can also extend the observable values through configuration: Attribute configuration:

|  | Name |  | Data type | Requirements | Default value |  |  | Description |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | key |  | string | Required | - |  |  | The attribute name. |  |  |  |  |
|  | value source _ |  | string | Required | - |  |  | The source of the attribute value. Valid values are fixed value , _ request heade _ r , request body _ , response head _ er , response body _ , and response stre _ aming body . _ |  |  |  |  |
|  |  |  |  |  |  |  |  | r |  |  |  |  |
|  |  | value source _ |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | er |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | , |  |
|  |  |  |  |  |  |  |  |  |  | , and |  |  |
|  |  |  |  |  |  |  |  | aming body _ |  |  |  |  |
|  | value |  | string | Required | - |  |  | The key, value, or path for fetching the attribute value. |  |  |  |  |
|  | rule |  | string | Optional | - |  |  | The rule for extracting the attribute from a streaming response. Valid values are first , replace , and append . |  |  |  |  |
|  | apply to log _ _ |  | bool | Optional | false |  |  | Specifies whether to record the extracted information in the log. |  |  |  |  |
|  |  | apply to log _ _ |  |  |  |  |  |  |  |  |  |  |

de OpenTrek

| apply to span _ _ | bool | Optional | false | Specifies whether to record the extracted information in the Tracing Analysis span. |
|---|---|---|---|---|

|  |  | apply to span _ _ |
|---|---|---|

OpenTrek de The following list describes the valid values for `value_source` : `fixed_value` : A static value. `request_header` : The attribute value is obtained from the HTTP request header. Set `value` to the header key. `request_body` : The attribute value is obtained from the request body. Set `value` to a GJSON path. `response_header` : The attribute value is obtained from the HTTP response header. Set `value` to the header key. `response_body` : The attribute value is obtained from the response body. Set `value` to a GJSON path. `response_streaming_body` : Retrieves the attribute value from the streaming response body. Set `value` to a GJSON path. If `value_source` is `response_streaming_body` , configure `rule` to specify how to retrieve the value from the streaming body. The following list describes the valid values. `first` : Uses the value from the first valid chunk. `replace` : Uses the value from the last valid chunk. `append` : Concatenates the values from all valid chunks. This can be used to retrieve the full response content.

**Configuration examples**

To record AI statistics in the gateway access log, modify the `log_format`. Add a new field to the existing `log_format` as shown in the following example:

```
'{"ai_log":"%FILTER_STATE(wasm.ai_log:PLAIN)%"}'
```

**Empty configuration**

de OpenTrek

```bash
# counter type, cumulative value of input tokens
route_upstream_model_consumer_metric_input_token{ai_route="ai-routealiyun.internal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwen-turb o",ai_consumer="none"} 24
# counter type, cumulative value of output tokens
route_upstream_model_consumer_metric_output_token{ai_route="ai-routealiyun.internal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwen-turb o",ai_consumer="none"} 507
# counter type, cumulative total time consumed by streaming and non-streaming requests
route_upstream_model_consumer_metric_llm_service_duration{ai_route="ai-route-aliyun.int ernal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwenturbo",ai_consumer="none"} 6470
# counter type, cumulative number of streaming and non-streaming requests
route_upstream_model_consumer_metric_llm_duration_count{ai_route="ai-routealiyun.internal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwen-turb o",ai_consumer="none"} 2
# counter type, cumulative first-token latency for streaming requests
route_upstream_model_consumer_metric_llm_first_token_duration{ai_route="ai-route-aliyun .internal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwen-turbo",ai_ consumer="none"} 340
# counter type, cumulative number of streaming requests
route_upstream_model_consumer_metric_llm_stream_duration_count{ai_route="ai-route-aliyu n.internal",ai_cluster="outbound|443||llm-aliyun.internal.dns",ai_model="qwen-turbo",ai _consumer="none"} 1
```

The following examples show how to use the metrics: Average first-token latency for streaming requests:

```
irate(route_upstream_model_consumer_metric_llm_first_token_duration[2m])
```

/

```
irate(route_upstream_model_consumer_metric_llm_stream_duration_count[2m])
```

Average total time consumed by streaming and non-streaming requests:

```
irate(route_upstream_model_consumer_metric_llm_service_duration[2m])
```

/

```
irate(route_upstream_model_consumer_metric_llm_duration_count[2m])
```

**Log**

```json
{
  "ai_log":"{\"model\":\"qwen-
turbo\",\"input_token\":\"10\",\"output_token\":\"69\",\"llm_first_token_duration\":\"309 ,\"llm_service_duration\":\"1955\"}" }
```

OpenTrek de

**Tracing Analysis**

If the configuration is empty, no additional attributes are added to the span.

**Extract token usage information from non-OpenAI protocols**

When the protocol in the ai-proxy plugin is set to `original`, you can use the following configuration to specify how to extract `model`, `input_token`, and `output_token`. This example shows a configuration for Alibaba Cloud Model Studio.

```
attributes:
 - key: model
 value_source: response_body
 value: usage.models.0.model_id
 apply_to_log: true
 apply_to_span: false
 - key: input_token
 value_source: response_body
 value: usage.models.0.input_tokens
 apply_to_log: true
 apply_to_span: false
 - key: output_token
 value_source: response_body
 value: usage.models.0.output_tokens
 apply_to_log: true
 apply_to_span: false
route_upstream_model_consumer_metric_input_token{ai_route="bailian",ai_cluster="qwen",ai_ del="qwen-max"} 343 route_upstream_model_consumer_metric_output_token{ai_route="bailian",ai_cluster="qwen",ai odel="qwen-max"} 153 route_upstream_model_consumer_metric_llm_service_duration{ai_route="bailian",ai_cluster=" en",ai_model="qwen-max"} 3725 route_upstream_model_consumer_metric_llm_duration_count{ai_route="bailian",ai_cluster="qw ",ai_model="qwen-max"} 1
```

**Log**

With this configuration, the log appears as follows:

```json
{
  "ai_log": "{\"model\":\"qwen-
max\",\"input_token\":\"343\",\"output_token\":\"153\",\"llm_service_duration\":\"19110\" }
```

**Tracing Analysis**

You can see three additional attributes in the Tracing Analysis span: `model`, `input_token`, and `output_token`.

**Record the consumer with authentication and authorization**

de OpenTrek For example:

```
attributes:
  - key: consumer # Record the consumer with authentication and authorization
    value_source: request_header
    value: x-mse-consumer
    apply_to_log: true
```

**Record questions and answers**

```
attributes:
  - key: question # Record the question
    value_source: request_body
    value: messages.@reverse.0.content
    apply_to_log: true
  - key: answer   # Extract the large model's answer from a streaming response
    value_source: response_streaming_body
    value: choices.0.delta.content
    rule: append
    apply_to_log: true
  - key: answer   # Extract the large model's answer from a non-streaming response
    value_source: response_body
    value: choices.0.message.content
    apply_to_log: true
```

**Advanced**

Using data transformation in Alibaba Cloud Simple Log Service (SLS), you can extract and process AI-related fields. For example, if the raw log is:

```
ai_log:{"question":"Use python to calculate 2 to the power of 3","answer":"You can use Python's power operator `**` to calculate the power of a number. To calculate 2 to the power of 3, which is 2 multiplied by itself 2 times, you can use the following code:\n\ n```python\nresult = 2 ** 3\nprint(result)\n```\n\nRunning this code will give you the output 8, because 2 multiplied by itself twice equals 8.","model":"qwenmax","input_token":"16","output_token":"76","llm_service_duration":"5913"}
```

Use the following data transformation script to extract `question` and `answer`:

```
e_regex("ai_log", grok("%{EXTRACTJSON}")) e_set("question", json_select(v("json"), "question", default="-")) e_set("answer", json_select(v("json"), "answer", default="-"))
```

After extraction, SLS adds the `question` and `answer` fields. The following example shows the result:

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| rule name _ | string | Yes | - | The name of the rate limiting rule. A Redis key is constructed using the rule name, limit type, key name, and the key's actual value. |

OpenTrek de

```python
ai_log:{"question":"Use python to calculate 2 to the power of 3","answer":"You can use Python's power operator `**` to calculate the power of a number. To calculate 2 to the power of 3, which is 2 multiplied by itself 2 times, you can use the following code:\n\ n```python\nresult = 2 ** 3\nprint(result)\n```\n\nRunning this code will give you the output 8, because 2 multiplied by itself twice equals 8.","model":"qwenmax","input_token":"16","output_token":"76","llm_service_duration":"5913"} question:Use python to calculate 2 to the power of 3 answer:You can use Python's power operator `**` to calculate the power of a number. To calculate 2 to the power of 3, which is 2 multiplied by itself 2 times, you can use the following code: result = 2 ** 3 print(result) Running this code will give you the output 8, because 2 multiplied by itself twice equa ls 8.
```

##### AI token rate limiting

**Feature description**

The `ai-token-ratelimit` plugin limits the token rate based on a specific key. This key can be sourced from a URL parameter, an HTTP request header, the client IP address, the consumer name, or a key name in a cookie.

**Runtime properties**

Plugin execution phase: `Default phase` . Execution priority: `600` .

| rule items _ | array of object | Yes | - | Rate limiting rule items. The plugin matches items in the order they appear in `rule items`. _ After the first match, the plugin applies the rule and ignores all subsequent rules. |
|---|---|---|---|---|
| rejected code _ | int | No | 429 | The HTTP status code returned when a request is rate-limited. |
| rejected msg _ | string | No | Too many requests | The response body returned when a request is rate-limited. |
| redis | object | Yes | - | Redis-related configurations. |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| limit by header _ _ | string | No. Select one from the limit by * _ _ options. | - | Specifies the name of the HTTP request header from which to get the rate limiting key value. |
| limit by param _ _ | string | No. Select one from the limit by * _ _ options. | - | Specifies the name of the URL parameter from which to get the rate limiting key value. |
| limit by consume _ _ r | string | No. Select one from the limit by * _ _ options. | - | Rate limits based on the consumer name. No actual value needs to be added. |

de OpenTrek The configuration fields for each item in `rule_items` are described below:

| limit by cookie _ _ | string | No. Select one from the limit by * _ _ options. | - | Specifies the name of the cookie key from which to get the rate limiting key value. |
|---|---|---|---|---|
| limit by per hea _ _ _ der | string | No. Select one from the limit by * _ _ options. | - | Matches specific HTTP request headers based on a rule and calculates rate limits for each header separately. Specifies the name of the source HTTP request header for the rate limiting key. Supports regular expressions or * when configuring limit keys . _ |
| limit by per para _ _ _ m | string | No. Select one from the limit by * _ _ options. | - | Matches specific URL parameters based on a rule and calculates rate limits for each parameter separately. Specifies the name of the source URL parameter for the rate limiting key. Supports regular expressions or * when configuring limit keys . _ |

OpenTrek de

| limit by per cons _ _ _ umer | string | No. Select one from the limit by * _ _ options. | - | Matches specific consumers based on a rule and calculates rate limits for each consumer separately. Rate limits are based on the consumer name, so no actual value is needed. Supports regular expressions or * when configuring limit keys . _ |
|---|---|---|---|---|
| limit by per cook _ _ _ ie | string | No. Select one from the limit by * _ _ options | - | Matches specific cookies based on a rule and calculates rate limits for each cookie separately. Specifies the name of the source cookie key for the rate limiting key. Supports regular expressions or * when configuring limit keys . _ |

de OpenTrek

| limit by per ip _ _ _ | string | No. Select one from the limit by * _ _ options. |  | - |  |  | Matches specific IP addresses based on a rule and calculates the rate limit for each IP address separately. This parameter specifies the source of the IP address to use as the rate-limiting key. Use the format from- |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | header- |  |  |  |
|  |  |  |  |  |  |  | <header name> _ |  |  |  |
|  |  |  |  |  |  |  | x-forwarded- |  |  |  |
|  |  |  |  |  |  |  | for |  | ), or use |  |
| limit keys _ | array of object | Yes |  | - |  |  | Configures the rate limit counts after a key value is matched. |  |  |  |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de The configuration fields for each item in `limit_keys` are described below:

| key | string | Yes | - |  | The key value to match. For limit by per _ _ _ header , limit by per _ _ _ param , limit by per _ _ _ consumer , and limit by per _ _ _ cookie types, configure a regular expression (prefixed with `regexp:`) or use `*` (matches all). For example, regexp:^d.* matches all strings that start with 'd'. For limit by per _ _ _ ip , configure an IP address or an IP address range. |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | limit by per _ _ _ |  |  |  |  |
|  |  |  |  |  | header |  |  |  |  |  |
|  |  |  |  |  |  |  |  | , |  |  |
|  |  |  |  |  | param |  |  |  |  |  |
|  |  |  |  |  |  |  | , |  |  |  |
|  |  |  |  |  | consumer |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | , and |  |
|  |  |  |  |  | cookie |  |  |  |  |  |
| token per secon _ _ d | int | No. Select one from token per sec _ _ ond , token per min _ _ ute , token per hou _ _ r , or token per day _ _ . | - |  | The number of token requests allowed per second. |  |  |  |  |  |
| token per minut _ _ e | int | No. Select one from token per sec _ _ ond , token per min _ _ ute , token per hou _ _ r , or token per day _ _ . | - |  | The number of token requests allowed per minute. |  |  |  |  |  |

|  |  | limit by per _ _ _ |  |
|---|---|---|---|
|  | ip |  |  |

|  |  | token per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | token per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

de OpenTrek

| token per hour _ _ | int | No. Select one from token per sec _ _ ond , token per min _ _ ute , token per hou _ _ r , or token per day _ _ . | - | The number of token requests allowed per hour. |
|---|---|---|---|---|
| token per day _ _ | int | No. Select one from token per sec _ _ ond , token per min _ _ ute , token per hou _ _ r , or token per day _ _ . | - | The number of token requests allowed per day. |

|  |  | token per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | token per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| service name _ | string | Required | - | The Redis service name. This must be the full FQDN, including the service type. For example, `my- redis.dns` or `redis.my- ns.svc.cluster.loc al`. |
| service port _ | int | No | The default value is 80 for static services and 6379 for others. | Enter the service port for the Redis service. |
| username | string | No | - | The Redis username. |

OpenTrek de The configuration fields for each item in `redis` are described below:

| password | string | No | - | The Redis password. |
|---|---|---|---|---|
| timeout | int | No | 1000 | The Redis connection timeout in milliseconds. |

de OpenTrek

**Configuration examples**

**Differentiated rate limiting based on the apikey request**

**parameter**

```bash
rule_name: default_rule rule_items:
 - limit_by_param: apikey
 limit_keys:
 - key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 token_per_minute: 10
 - key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 token_per_hour: 100
 - limit_by_per_param: apikey
 limit_keys:
 # Regular expression that matches all strings starting with 'a'. 10 requests per secon
d for each matching apikey.
 - key: "regexp:^a.*"
 token_per_second: 10
 # Regular expression that matches all strings starting with 'b'. 100 requests per minu
te for each matching apikey.
 - key: "regexp:^b.*"
 token_per_minute: 100
 # Fallback rule that matches all requests. 1000 requests per hour for each matching ap
ikey.
 - key: "*"
 token_per_hour: 1000
redis:
 service_name: redis.static
```

**Differentiated rate limiting based on the x-ca-key request**

OpenTrek de

```bash
rule_name: default_rule rule_items:
 - limit_by_header: x-ca-key
 limit_keys:
 - key: 102234
 token_per_minute: 10
 - key: 308239
 token_per_hour: 10
 - limit_by_per_header: x-ca-key
 limit_keys:
 # Regular expression that matches all strings starting with 'a'. 10 requests per secon
d for each matching apikey.
 - key: "regexp:^a.*"
 token_per_second: 10
 # Regular expression that matches all strings starting with 'b'. 100 requests per minu
te for each matching apikey.
 - key: "regexp:^b.*"
 token_per_minute: 100
 # Fallback rule that matches all requests. 1000 requests per hour for each matching ap
ikey.
 - key: "*"
 token_per_hour: 1000
redis:
 service_name: redis.static
```

**Differentiated rate limiting based on the peer IP address from**

**the x-forwarded-for header**

```bash
rule_name: default_rule rule_items:
 - limit_by_per_ip: from-header-x-forwarded-for
 limit_keys:
 # Exact IP
 - key: 1.1.1.1
 token_per_day: 10
 # IP range. 100 requests per day for each IP in this range.
 - key: 1.1.1.0/24
 token_per_day: 100
 # Fallback rule. The default is 1000 requests per day for each IP.
 - key: 0.0.0.0/0
 token_per_day: 1000
redis:
 service_name: redis.static
```

**Differentiated rate limiting based on the consumer**

de OpenTrek

```bash
rule_name: default_rule rule_items:
 - limit_by_consumer: ''
 limit_keys:
 - key: consumer1
 token_per_second: 10
 - key: consumer2
 token_per_hour: 100
 - limit_by_per_consumer: ''
 limit_keys:
 # Regular expression that matches all strings starting with 'a'. 10 requests per secon
d for each matching consumer.
 - key: "regexp:^a.*"
 token_per_second: 10
 # Regular expression that matches all strings starting with 'b'. 100 requests per minu
te for each matching consumer.
 - key: "regexp:^b.*"
 token_per_minute: 100
 # Fallback rule that matches all requests. 1000 requests per hour for each matching co
nsumer.
 - key: "*"
 token_per_hour: 1000
redis:
 service_name: redis.static
```

**Differentiated rate limiting based on key-value pairs in a**

**cookie**

OpenTrek de

```bash
rule_name: default_rule rule_items:
 - limit_by_cookie: key1
 limit_keys:
 - key: value1
 token_per_minute: 10
 - key: value2
 token_per_hour: 100
 - limit_by_per_cookie: key1
 limit_keys:
 # Regular expression that matches all strings starting with 'a'. 10 requests per secon
d for each matching cookie value.
 - key: "regexp:^a.*"
 token_per_second: 10
 # Regular expression that matches all strings starting with 'b'. 100 requests per minu
te for each matching cookie value.
 - key: "regexp:^b.*"
 token_per_minute: 100
 # Fallback rule that matches all requests. 1000 requests per hour for each matching co
okie value.
 - key: "*"
 token_per_hour: 1000
rejected_code: 200 rejected_msg: '{"code":-1,"msg":"Too many requests"}' redis:
 service_name: redis.static
```

**Complete example**

The AI token rate limiting plugin depends on Redis to record the number of remaining tokens. Therefore, you must first deploy a Redis service. de OpenTrek

```
apiVersion: apps/v1 kind: Deployment metadata:
 name: redis
 labels:
 app: redis
spec:
 replicas: 1
 selector:
 matchLabels:
 app: redis
 template:
 metadata:
 labels:
 app: redis
 spec:
 containers:
 - name: redis
 image: redis
 ports:
 - containerPort: 6379
--apiVersion: v1 kind: Service metadata:
 name: redis
 labels:
 app: redis
spec:
 ports:
 - port: 6379
 targetPort: 6379
 selector:
 app: redis
---
```

In this example, Qwen is used as the AI service provider. You also need to set up the AI statistics plugin, because the AI token rate limiting plugin relies on it to calculate the number of tokens consumed by each request. The following configuration limits the total number of input and output tokens to 200 per minute. OpenTrek de

```bash
apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 namespace: higress-system
spec:
 matchRules:
 - config:
 provider:
 type: qwen
 apiTokens:
 - "<YOUR_API_TOKEN>"
 modelMapping:
 'gpt-3': "qwen-turbo"
 'gpt-35-turbo': "qwen-plus"
 'gpt-4-turbo': "qwen-max"
 '*': "qwen-turbo"
 ingress:
 - qwen
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/ai-proxy:1.0.0
 phase: UNSPECIFIED_PHASE
 priority: 100
--apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 name: ai-token-ratelimit
 namespace: higress-system
spec:
 defaultConfig:
 rule_name: default_limit_by_param_apikey
 rule_items:
 - limit_by_param: apikey
 limit_keys:
 - key: 123456
 token_per_minute: 200
 redis:
 # By default, to reduce pressure on the data plane, the global.onlyPushRouteCluster pa
rameter in Higress is set to true. This means Kubernetes services are not automatically discovered.
 # To use a Kubernetes service for service discovery, set the
global.onlyPushRouteCluster parameter to false.
 # This lets you set service_name directly to the Kubernetes service without creating a
n McpBridge and an Ingress route for Redis.
 # service_name: redis.default.svc.cluster.local
 service_name: redis.dns
 service_port: 6379
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/ai-token-
ratelimit:1.0.0
 phase: UNSPECIFIED_PHASE
 priority: 600
```

de OpenTrek The `service_name` configuration item for Redis in the AI token rate limiting plugin is derived from the service source configured in McpBridge. You must also configure the Qwen service endpoint in McpBridge.

```
apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: default
 namespace: higress-system
spec:
 registries:
 - domain: dashscope.aliyuncs.com
 name: qwen
 port: 443
 type: dns
 - domain: redis.default.svc.cluster.local # Kubernetes Service
 name: redis
 type: dns
 port: 6379
```

You can create two routing rules. OpenTrek de

```
apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/backend-protocol: HTTPS
 higress.io/destination: qwen.dns
 higress.io/proxy-ssl-name: dashscope.aliyuncs.com
 higress.io/proxy-ssl-server-name: "on"
 labels:
 higress.io/resource-definer: higress
 name: qwen
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - host: qwen-test.com
 http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /
 pathType: Prefix
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/destination: redis.dns
 higress.io/ignore-path-case: "false"
 labels:
 higress.io/resource-definer: higress
 name: redis
spec:
 ingressClassName: higress
 rules:
 - http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /
 pathType: Prefix
```

You can forward traffic from higress-gateway to your local machine for testing.

```bash
kubectl port-forward svc/higress-gateway -n higress-system 18000:80
```

Rate limiting is triggered as follows:

| Name | Data type | Require d | Default value | Description |
|---|---|---|---|---|
| lb policy _ | string | Required | - | The type of load balancing policy. |

de OpenTrek

```json
curl "http://localhost:18000/v1/chat/completions?apikey=123456" \ -H "Host: qwen-test.com" \ -H "Content-Type: application/json" \ -d '{
 "model": "gpt-3",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "stream": false
}' {"id":"88cfa80f-545d-93b4-8ff3-3f5245ca33ba","choices":[{"index":0,"message":{"role":"a ssistant","content":"I am Qwen, an AI assistant developed by Alibaba Cloud. I can answe r various questions, provide information, and have conversations with users. How can I help you?"},"finish_reason":"stop"}],"created":1719909825,"model":"qwenturbo","object":"chat.completion","usage": {"prompt_tokens":13,"completion_tokens":33,"total_tokens":46}} curl "http://qwen-test.com:18000/v1/chat/completions?apikey=123456" -H "Content-Type: a pplication/json" -d '{
 "model": "gpt-3",
 "messages": [
 {
 "role": "user",
 "content": "Hello, who are you?"
 }
```

`],`

```json
 "stream": false
}' Too many requests # Rate limiting successful
```

##### AI load balancing

The hot-swappable load balancing policy for Large Language Model (LLM) services reverts to the service's native policy when the plugin is shut down. The native policies include roundrobin, local least requests, random, and consistent hashing.

**Runtime properties**

The plugin runs in the `Default phase` with an execution priority of `50` .

| lb config _ | object | Required | - | The configuration for the current load balancing policy type. |
|---|---|---|---|---|

| least busy _ |  |
|---|---|
|  | . |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| serviceFQDN | string | Required | - | The FQDN of the Redis service. For example: redis.dns . |

OpenTrek de The following load balancing policies are supported: `global_least_request` : Performs global least requests load balancing using Redis. `prefix_cache` : Selects a backend node based on a prompt prefix match. If a matching node is not found, it selects a service node using the global least requests method.

**Global least requests**

**Feature description**

In a distributed environment, a gateway instance often consists of multiple nodes. Traditional load balancing policies operate locally on each node and lack a global view. The AI Gateway uses Redis to implement a global least requests load balancing algorithm. This algorithm balances the load based on the number of requests that each LLM pod is currently processing. The process for selecting a pod is as follows:

| servicePort | int | Required | - | The port of the Redis service. |
|---|---|---|---|---|
| username | string | Required | - | The Redis username. |
| password | string | Optional | Empty | The Redis password. |
| timeout | int | Optional | 3000 ms | The Redis request timeout period. |
| database | int | (Optional) | 0 | The ordinal number of the Redis database. |

de OpenTrek

**Configuration example**

```
lb_policy: global_least_request lb_config:
  serviceFQDN: redis.static
  servicePort: 6379
  username: default
  password: '123456'
```

**Prefix matching**

**Feature description**

This method selects a pod based on a prompt prefix match to reuse the Key-Value (KV) Cache. If a matching node is not found using the prefix, it selects a service node using the global least requests method. For example, the following request is routed to Pod 1:

```json
{
  "model": "qwen-turbo",
  "messages": [
    {
      "role": "user",
      "content": "hi"
    }
```

]

```
}
```

Therefore, subsequent requests with the same prefix are routed to Pod 1:

| Name | Data type | Requirements | Default value | Description |
|---|---|---|---|---|
| serviceFQDN | string | Required | - | The FQDN of the Redis service. For example: redis.dns . |
| servicePort | int | Required | - | The port of the Redis service. |
| username | string | Required | - | The Redis username. |
| password | string | Optional | Empty | The Redis password. |
| timeout | int | Optional | 3000 ms | The Redis request timeout period. |
| database | int | Optional | 0 | The ordinal number of the Redis database. |

OpenTrek de

```json
{
  "model": "qwen-turbo",
  "messages": [
    {
      "role": "user",
      "content": "hi"
    },
    {
      "role": "assistant",
      "content": "Hi! How can I assist you today? "
    },
    {
      "role": "user",
      "content": "write a short story aboud 100 words"
    }
```

]

```
}
```

| redisKeyTTL | int | Optional | 1800 ms | The TTL for the key that corresponds to the prompt prefix. |
|---|---|---|---|---|

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | criticalModels |  | []string | Optional | - | A list of critical models. |
|  |  | criticalModels |  |  |  |  |

de OpenTrek

**Configuration example**

```
lb_policy: prefix_cache lb_config:
  serviceFQDN: redis.static
  servicePort: 6379
  username: default
  password: '123456'
```

**Least Load**

**Feature description**

This policy is the wasm implementation of `gateway-api-inference-extension` .

**Configuration example**

```
lb_policy: least_busy lb_config:
  criticalModels:
  - meta-llama/Llama-2-7b-hf
  - sql-lora
```

##### AI data masking

The ai-data-masking plugin blocks and replaces sensitive words in requests and responses. This topic describes how to configure the ai-data-masking plugin.

**Features**

Blocks and replaces sensitive words in requests and responses.

| Name | Data type | Default value | Description |
|---|---|---|---|
| deny openai _ | bool | true | Blocks requests that use the OpenAI protocol. |

OpenTrek de

**Data scope**

OpenAI protocol: Processes conversational content in requests and responses. JSONPath: Processes only specified fields. Raw: Processes the entire request or response body.

**Sensitive word blocking**

If a sensitive word is detected within the specified data scope, the request is immediately blocked and a preset error message is returned. Supports a built-in system wordlist and custom sensitive words.

**Sensitive word replacement**

Replaces sensitive words in request data with masked strings before sending the data to the backend service. This ensures that sensitive data does not leave the domain. Some masked data can be restored after the backend service returns a response. Custom rules support standard regular expressions and Grok rules. Replacement strings support variable substitution.

**Runtime properties**

This plugin runs during the `Authentication phase` and has an execution priority of `991` .

**Configuration fields**

| deny jsonpath _ | string | [] | Blocks requests based on the specified JSONPath expressions. |
|---|---|---|---|
| deny raw _ | bool | false | Blocks requests based on the raw body. |
| system deny _ | bool | false | Enables the built-in blocking rules. |
| deny code _ | int | 200 | The HTTP status code to return when a request is blocked. |
| deny message _ | string | The question or answer contains sensitive words and has been blocked. | The message that the AI returns when a request is blocked. |
| deny raw message _ _ | string | {“errmsg”:“Your question or answer could not be posted because it contains a sensitive word.”} | The content to return when a non-OpenAI request is blocked. |
| deny content type _ _ | string | application/json | The Content-Type header to return when a non-OpenAI request is blocked. |
| deny words _ | array of string | [] | A list of custom sensitive words. |
| replace roles _ | array | - | Custom rules for replacing sensitive words using regular expressions. |
| replace roles.regex _ | string | - | The regular expression for the rule. Built-in Grok rules are supported. |
| replace roles.type _ | [replace, hash] | - | The replacement type. |
| replace roles.restore _ | bool | false | Specifies whether to restore the original value. |

de OpenTrek

| replace roles.value _ | string | - | The replacement value. Regular expression variables are supported. |
|---|---|---|---|

OpenTrek de

**Configuration example**

```bash
system_deny: true deny_openai: true deny_jsonpath:
  - "$.messages[*].content"
deny_raw: true deny_code: 200 deny_message: "The question or answer contains sensitive words and has been blocked." deny_raw_message: "{\"errmsg\":\"The question or answer contains sensitive words and ha s been blocked.\"}" deny_content_type: "application/json" deny_words:
  - "Custom sensitive word 1"
  - "Custom sensitive word 2"
replace_roles:
  - regex: "%{MOBILE}"
    type: "replace"
    value: "****"
    # Mobile number 1380013**** -> ****
  - regex: "%{EMAILLOCALPART}@%{HOSTNAME:domain}"
    type: "replace"
    restore: true
    value: "****@$domain"
    # Email adm**@gmail.com -> ****@gmail.com
  - regex: "%{IP}"
    type: "replace"
    restore: true
    value: "***.***.***.***"
    # IP address 192.168.0.1 -> ***.***.***.***
  - regex: "%{IDCARD}"
    type: "replace"
    value: "****"
    # ID card number 110000000000000000 -> ****
  - regex: "sk-[0-9a-zA-Z]*"
    restore: true
    type: "hash"
    # hash sk-12345 -> 9cb495455da32f41567dab1d07f1973d
    # The hashed value is sent to the large model. When the model responds, the hash is
reverted to the original value.
```

**Sensitive word replacement example**

**User request**

```
Change curl http://172.20.5.14/api/openai/v1/chat/completions -H "Authorization: sk-
```

`12345" -H "Auth: te**@gmail.com"` to use the POST method.

| curl |  |  |
|---|---|---|

| -H "Content-Type: application/json" |  |
|---|---|
| application/json . | This tells the serve |

| curl |  |  |
|---|---|---|

| -H "Content-Type: application/json" |  |
|---|---|
| application/json . | This tells the serve |

de OpenTrek

**Processed request sent to the large model**

```
Change curl http://***.***.***.***/api/openai/v1/chat/completions -H "Authorization:
```

`48a7e98a91d93896d8dac522c5853948" -H "Auth: ****@gmail.com"` to use the POST method.

**Response from the large model**

```bash
curl -X POST \
 -H "Authorization: 48a7e98a91d93896d8dac522c5853948" \
 -H "Auth: ****@gmail.com" \
 -H "Content-Type: application/json" \
 -d '{"key":"value"}' \
 http://***.***.***.***/api/openai/v1/chat/completions
```

The following modifications were made: `-X POST` sets the request method to POST. `-d '{"key":"value"}'` specifies the data to send. `'{"key":"value"}'` is a simple example of a JSON object. Replace it with the actual data you want to send. Note: Replace `"key":"value"` with your actual data. If your API accepts a different data structure or requires specific fields, adjust this part as needed.

**Processed response returned to the user**

```bash
curl -X POST \
 -H "Authorization: sk-12345" \
 -H "Auth: te**@gmail.com" \
 -H "Content-Type: application/json" \
 -d '{"key":"value"}' \
 http://172.20.5.14/api/openai/v1/chat/completions
```

The following modifications were made: `-X POST` sets the request method to POST. `-d '{"key":"value"}'` specifies the data to send. `'{"key":"value"}'` is a simple example of a JSON object. Replace it with the actual data you want to send. Note: Replace `"key":"value"` with your actual data. If your API accepts a different data structure or requires specific fields, adjust this part as needed.

**Notes**

In streaming mode, if a masked word is split across multiple chunks, the original word may not be restored.

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| llm | object | Required | - | Information about the AI service provider. |
| apis | object | Required | - | Information about the external API service provider. |

OpenTrek de In streaming mode, if a sensitive word is split across multiple chunks, a portion of the word may be returned to the user before it is detected. For a list of built-in Grok rules, see Grok Pattern Reference.

##### AI agent

The ai-agent plug-in supports flexible configurations, including custom settings for large model services, external APIs, and prompt templates. This topic describes how to configure the ai-agent plug-in.

**Features**

This is a customizable API AI agent. It supports APIs that use GET and POST HTTP methods. It also supports multi-turn conversations in both streaming and non-streaming modes. The agent flowchart is as follows:

**Runtime properties**

Execution stage: `Default Stage` . Execution priority: `200` .

**Configuration fields**

**Basic configurations**

|  | promptTemplate |  | object | Optional | - | Information about the Agent ReAct template. |
|---|---|---|---|---|---|---|
|  |  | promptTemplate |  |  |  |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | apiKey |  | string | This field is required. | - | The token used for authentication when accessing the large model service. |
|  | serviceName |  | string | Required | - | The name of the large model service. |
|  | servicePort |  | int | Required | - | The service port of the large model. |
|  | domain |  | string | This parameter is required. | - | The domain name used to access the large model service. |
|  | path |  | string | Required | - | The path used to access the large model service. |
|  | model |  | string | Required | - | The model name used to access the large model service. |
|  | maxIterations |  | int | Required | 15 | The maximum number of steps before the execution loop ends. |
|  | maxExecutionTi me |  | int | Required | 50000 | The timeout period for each request to the large model, in milliseconds. |
|  |  | maxExecutionTi | i |  |  |  |
|  | me |  |  |  |  |  |

|  |  | maxIterations |
|---|---|---|

de OpenTrek The following table describes the configuration fields for `llm` .

| maxTokens | int | Required | 1000 | The output token limit for each request to the large model. |
|---|---|---|---|---|

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| apiProvider | object | Required | - | Information about the external API service. |
| api | string | Required | - | The OpenAPI document for the tool. |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | apiKey |  | object | Optional | - | The token used for authentication when accessing the external API service. |
|  | maxExecutionTi me |  | int | Optional | 50000 | The timeout period for each API request, in milliseconds. |
|  |  | maxExecutionTi |  |  |  |  |
|  | me |  |  |  |  |  |
|  | serviceName |  | string | Required | - | The name of the external API service. |
|  | servicePort |  | int | Required. | - | The service port of the external API. |
|  | domain |  | string | Required | - | The domain name used to access the external API. |

OpenTrek de The following table describes the configuration fields for `apis` . The following table describes the configuration fields for `apiProvider` . The following table describes the configuration fields for `apiKey` .

| Name Data type Required in string Optional name string Optional value string Optional |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | Name | Data type | Required | Default value |  | Description |
|  | in | string | Optional | none |  | Specifies whether the authentication token is placed in the header or query when accessing the external API service. If the API does not require a token, set this parameter to `none`. |
|  | name | string | Optional | - |  | The name of the authentication token used when accessing the external API service. |
|  | value | string | Optional | - |  | The value of the authentication token used when accessing the external API service. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| language | string | Optional | EN | The language of the Agent ReAct template. Valid values are `CH` and `EN`. |
| chTemplate | object | Optional | - | The Chinese Agent ReAct template. |
| enTemplate | object | Optional | - | The English Agent ReAct template. |

| 67 |  |  | > Documen | t Version: 2026062 |
|---|---|---|---|---|

de OpenTrek The following table describes the configuration fields for `promptTemplate` . The following table describes the configuration fields for `chTemplate` and `enTemplate` .

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| question | string | Optional | - | The `question` part of the Agent ReAct template. |
| thought1 | string | Optional | - | The `thought1` part of the Agent ReAct template. |
| observation | string | Optional | - | The `observation` part of the Agent ReAct template. |
| thought2 | string | Optional | - | The `thought2` part of the Agent ReAct template. |

OpenTrek de

**Usage examples**

```
llm:
 apiKey: xxxxxxxxxxxxxxxxxx
 domain: dashscope.aliyuncs.com
 serviceName: dashscope.dns
 servicePort: 443
 path: /compatible-mode/v1/chat/completions
 model: qwen-max-0403
 maxIterations: 2
promptTemplate:
 language: CH
apis:
- apiProvider:
 domain: restapi.amap.com
 serviceName: geo.dns
 servicePort: 80
 apiKey:
 in: query
 name: key
 value: xxxxxxxxxxxxxxx
 api: |
 openapi: 3.1.0
 info:
 title: AMAP
 description: Get information about POIs
 version: v1.0.0
 servers:
 - url: https://restapi.amap.com
 paths:
```

de OpenTrek

```
 /v5/place/text:
 get:
 description: Get the latitude and longitude coordinates of a POI based on it
s name
 operationId: get_location_coordinate
 parameters:
 - name: keywords
 in: query
 description: The name of the POI. The name must be in Chinese.
 required: true
 schema:
 type: string
 - name: region
 in: query
 description: The region where the POI is located. The name must be in
Chinese.
 required: true
 schema:
 type: string
 deprecated: false
 /v5/place/around:
 get:
 description: Search for POIs near the given coordinates
 operationId: search_nearby_pois
 parameters:
 - name: keywords
 in: query
 description: Keywords for the target POI
 required: true
 schema:
 type: string
 - name: location
 in: query
 description: The longitude and latitude of the centroid, separated by a comm
```

a

```
 required: true
 schema:
 type: string
 deprecated: false
 components:
 schemas: {}
- apiProvider:
 domain: api.seniverse.com
 serviceName: seniverse.dns
 servicePort: 80
 apiKey:
 in: query
 name: key
 value: xxxxxxxxxxxxxxx
 api: |
 openapi: 3.1.0
 info:
 title: Seniverse Weather
 description: Get weather forecast information
```

i OpenTrek de

```
 version: v1.0.0
 servers:
 - url: https://api.seniverse.com
 paths:
 /v3/weather/now.json:
 get:
 description: Get real-time weather for a specified city
 operationId: get_weather_now
 parameters:
 - name: location
 in: query
 description: The city to query
 required: true
 schema:
 type: string
 - name: language
 in: query
 description: The language for the weather query results
 required: true
 schema:
 type: string
 default: zh-Hans
 enum:
 - zh-Hans
 - en
 - ja
 - name: unit
 in: query
 description: The unit of temperature. Can be Celsius or Fahrenheit.
 required: true
 schema:
 type: string
 default: c
 enum:
 - c
 - f
 deprecated: false
 components:
 schemas: {}
- apiProvider:
 apiKey:
 in: "header"
 name: "DeepL-Auth-Key"
 value: "73xxxxxxxxxxxxxxx:fx"
 domain: "api-free.deepl.com"
 serviceName: "deepl.dns"
 servicePort: 443
 api: |
 openapi: 3.1.0
 info:
 title: DeepL API Documentation
 description: The DeepL API provides programmatic access to DeepL’s machine t
ranslation technology.
 version: v1.0.0
servers:
```

de OpenTrek

```
 servers:
 - url: https://api-free.deepl.com/v2
 paths:
 /translate:
 post:
 summary: Request Translation
 operationId: translateText
 requestBody:
 required: true
 content:
 application/json:
 schema:
 type: object
 required:
 - text
 - target_lang
 properties:
 text:
 description: |
 Text to be translated. Only UTF-8-encoded plain text is supported. The
parameter may be specified
 up to 50 times in a single request. Translations are returned in the same or
der as they are requested.
 type: array
 maxItems: 50
 items:
 type: string
 example: Hello, World!
 target_lang:
 description: The language into which the text should be translated.
 type: string
 enum:
 - BG
 - CS
 - DA
 - DE
 - EL
 - EN-GB
 - EN-US
 - ES
 - ET
 - FI
 - FR
 - HU
 - ID
 - IT
 - JA
 - KO
 - LT
 - LV
 - NB
 - NL
 - PL
 - PT-BR
 - PT-PT
```

OpenTrek de

```
 - RO
 - RU
 - SK
 - SL
 - SV
 - TR
 - UK
 - ZH
 - ZH-HANS
 example: DE
 components:
 schemas: {}
```

This example configures three services and demonstrates tools that use both GET and POST methods. The GET tools include AMAP and Seniverse Weather. The POST tool is DeepL Translate. First, configure these three services as DNS domain names in AI Gateway and ensure that they are healthy. AMAP provides two tools: one to retrieve the coordinates of a specified location, and another to search for points of interest (POIs) near given coordinates. For more information, see https://lbs.amap.com/api/webservice/guide/api-advanced/newpoisearch. Seniverse Weather provides a tool to retrieve real-time weather for a specified city. It provides responses in Chinese, English, and Japanese, and displays temperatures in Celsius and Fahrenheit. For more information, see For more information, see the referenced document. DeepL provides a tool to translate given sentences and supports multiple languages. For more information, see https://developers.deepl.com/docs/v/zh/api-reference/translate? fallback=true. The following are test use cases. For stable results, use a consistent large model version. This example uses qwen-max-0403.

**Sample request**

```bash
curl 'http://<replace_with_gateway_public_IP>/api/openai/v1/chat/completions'
```

\

```
-H 'Accept: application/json, text/event-stream' \ -H 'Content-Type: application/json' \ --data-raw '{"model":"qwen","frequency_penalty":0,"max_tokens":800,"stream":false,"messages :[{"role":"user","content":"I want to drink coffee near Xinsheng Building in Jinan City. Can you recommend some places?"}],"presence_penalty":0,"temperature":0,"top_p":0}'
```

**Sample response**

de OpenTrek

```json
{"id":"139487e7-96a0-9b13-91b4-290fb79ac992","choices":[{"index":0,"message": {"role":"assistant","content":"Near Xinsheng Building in Jinan City, here are some coffee shops:\n1. luckin coffee (Xinsheng Building Store): Lobby of Building 2, Xinsheng Building, 1299 Xinluo Street.\n2. NOWWA COFFEE (Sanqing Qisheng Plaza Store): 60 meters southwest of the intersection of Xinluo Street and Yingxiu Road.\n3. luckin coffee (Sanqing Qisheng Plaza Store): 1267 Yingxiu Road.\n4. Cotti Coffee (Qilu Software Park Store): Ground floor of Building 4, Sanqing Qisheng Plaza, Xinluo Street.\n5. Cotti Coffee (Meilian Plaza Store): L117, Meilian Plaza, 1166 Xinluo Street, High-tech Zone.\nOther options are also available. Hope this helps!"},"finish_reason":"stop"}],"created":1723172296,"model":"qwen-max- 0403","object":"chat.completion","usage": {"prompt_tokens":886,"completion_tokens":50,"total_tokens":936}}
```

**Sample request**

```bash
curl 'http://<replace_with_gateway_public_IP>/api/openai/v1/chat/completions'
```

\

```
-H 'Accept: application/json, text/event-stream' \ -H 'Content-Type: application/json' \ --data-raw '{"model":"qwen","frequency_penalty":0,"max_tokens":800,"stream":false,"messages :[{"role":"user","content":"What is the current weather in Jinan City?"}],"pre sence_penalty":0,"temperature":0,"top_p":0}'
```

**Sample response**

```json
{"id":"ebd6ea91-8e38-9e14-9a5b-90178d2edea4","choices":[{"index":0,"message": {"role":"assistant","content":" The current weather in Jinan City is overcast, with a temperature of 31°C. This information was last updated at 15 :12 (UTC+8) on August 9, 2024."},"finish_reason":"stop"}],"created":1723187991,"model":"qwen-max- 0403","object":"chat.completion","usage": {"prompt_tokens":890,"completion_tokens":56,"total_tokens":946}}
```

**Sample request**

```bash
curl 'http://<replace_with_gateway_public_IP>/api/openai/v1/chat/completions'
```

\

```
-H 'Accept: application/json, text/event-stream' \ -H 'Content-Type: application/json' \ --data-raw '{"model":"qwen","frequency_penalty":0,"max_tokens":800,"stream":false,"messages :[{"role": "user","content": "What's the weather like in Jinan?"},{ "role": "assistant","content": "Currently, the weather in Jinan City is cloudy with a temperature of 24°C. The data was last updated at 21:50:14 on September 12, 2 024."},{"role": "user","content": "What about Beijing?"}],"presence_penalty":0,"temperature":0,"top_p":0}'
```

**Sample response**

OpenTrek de

```json
{"id":"ebd6ea91-8e38-9e14-9a5b-90178d2edea4","choices":[{"index":0,"message": {"role":"assistant","content":"Currently, the weather in Beijing is clear with a temperature of 19°C. The data was last updated at 22:17:40 on September 12, 2024."},"finish_reason":"stop"}],"created":1723187991,"model":"qwen-max- 0403","object":"chat.completion","usage": {"prompt_tokens":999,"completion_tokens":76,"total_tokens":1075}}
```

**Sample request**

```bash
curl 'http://<replace_with_gateway_public_IP>/api/openai/v1/chat/completions'
```

\

```
-H 'Accept: application/json, text/event-stream' \ -H 'Content-Type: application/json' \ --data-raw '{"model":"qwen","frequency_penalty":0,"max_tokens":800,"stream":false,"messages :[{"role":"user","content":"What is the current weather in Jinan City? Use Fahrenheit and answer in Japanese."}],"presence_penalty":0,"temperature":0,"top_p":0}'
```

**Sample response**

```json
{"id":"ebd6ea91-8e38-9e14-9a5b-90178d2edea4","choices":[{"index":0,"message": {"role":"assistant","content":"The current weather in Jinan is rainy and cloud y. The temperature is 88°F. This information was updated at 15:12 on August 9 , 2024 (Tokyo Time)."},"finish_reason":"stop"}],"created":1723187991,"model":"qwen-max- 0403","object":"chat.completion","usage": {"prompt_tokens":890,"completion_tokens":56,"total_tokens":946}}
```

**Example request**

```bash
curl 'http://<replace_with_gateway_public_IP>/api/openai/v1/chat/completions'
```

\

```
-H 'Accept: application/json, text/event-stream' \ -H 'Content-Type: application/json' \ --data-raw '{"model":"qwen","frequency_penalty":0,"max_tokens":800,"stream":false,"messages :[{"role":"user","content":"Help me translate the following sentence into German: Hail Hydra!"}],"presence_penalty":0,"temperature":0,"top_p":0}'
```

**Sample response**

```json
{"id":"65dcf12c-61ff-9e68-bffa-44fc9e6070d5","choices":[{"index":0,"message": {"role":"assistant","content":"The German translation of “Hail Hydra!” is “Hoch lebe Hydra!”."
```

##### AI RAG

This topic describes AI retrieval-augmented generation (RAG).

| Name | Data type | Require d | Defau lt value | Description |
|---|---|---|---|---|
| dashscope.apiKey | string | Required | - | The authentication token for the Qwen service. |
| dashscope.serviceFQDN | string | Required | - | The service name of Qwen. |
| dashscope.servicePort | int | Required | - | The service port for Qwen. |
| dashscope.serviceHost | string | Required | - | The domain name for accessing the Qwen service. |
| dashvector.apiKey | string | Required | - | The authentication token for the DashVector service. |

de OpenTrek You can implement RAG for large language models (LLMs) by connecting to Alibaba Cloud Vector Retrieval Service (DashVector). The process is shown in the following figure:

**Runtime properties**

Execution phase: `Default phase` . Execution priority: `400` .

| dashvector.serviceFQDN | string | Required | - | The service name of DashVector. |
|---|---|---|---|---|
| dashvector.servicePort | int | Required | - | The service port for DashVector. |
| dashvector.serviceHost | string | Required | - | The domain name for accessing the DashVector service. |
| dashvector.topk | int | Required | - | The number of vectors to retrieve from DashVector. |
| dashvector.threshold | float | Required | - | The vector distance threshold. Documents with a distance score higher than this threshold are filtered out. |
| dashvector.field | string | Required | - | The field name in DashVector where the document is stored. |

|  | dashvector.serviceFQDN |
|---|---|

|  | dashvector.servicePort |
|---|---|

|  | dashvector.serviceHost |
|---|---|

OpenTrek de

**Note**

After the plugin is enabled, when you use the Tracing Analysis feature, the document `id` retrieved by `rag` is added to the `attribute` of the `span` for troubleshooting.

**Example**

```
dashscope:
    apiKey: xxxxxxxxxxxxxxx
    serviceFQDN: dashscope
    servicePort: 443
    serviceHost: dashscope.aliyuncs.com
dashvector:
    apiKey: xxxxxxxxxxxxxxxxxxxx
    serviceFQDN: dashvector
    servicePort: 443
    serviceHost: vrs-cn-xxxxxxxxxxxxxxx.dashvector.cn-hangzhou.aliyuncs.com
    collection: xxxxxxxxxxxxxxx
    topk: 1
    threshold: 0.4
    field: raw
```

The CEC-Corpus dataset contains a corpus and annotated data from 332 news reports about breaking events. The original text from these news articles is extracted, vectorized, and added to DashVector.

| the Hainan rear-end collision happen? What was the cause? How many casualties were |  |
|---|---|

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| defaultEnable | bool | Optional | true | The plug-in is enabled by default. If you set this to false, the plug-in is enabled only when the request contains the `web search opti _ _ ons` field. |
| needReference | bool | Optional | false | Specifies whether to add references to the response. |

de OpenTrek Without processing by the RAG plug-in, the LLM returns the following result: I'm sorry. As an AI model, I cannot retrieve real-time information or updates on specific news events, including details such as the location, cause, and casualties. For specific events such as this, check the latest news reports or official announcements for accurate information. Visit major media websites, use news applications, or follow announcements from relevant government departments to obtain this information. After being processed by the RAG plug-in, the LLM returns the following result: The Hainan rear-end collision occurred at the 37 km mark of the Haiwen Expressway, in the direction from Wenchang to Haikou. The traffic police department was still investigating the cause of the accident. Therefore, the exact cause cannot be determined from the provided information. There was one fatality (the driver died at the scene) and eight injuries (including two children and six adults). All injured people were rescued and sent to the hospital for treatment.

##### AI search enhancement

The ai-search plug-in improves AI model responses by adding real-time results from search engines such as Google, Bing, Arxiv, and Elasticsearch. The plug-in automatically adds search results to the prompt template. You can also configure the plug-in to add references to the final response. This topic describes how to configure the ai-search plug-in.

**Runtime properties**

Plug-in execution phase: `Default phase` Plug-in execution priority: `460` .

**Configuration fields**

| referenceFormat | string | Optional | "**References :**\n%s" |  | The format for the reference content. This must include the `%s` placeholder. |  |  |
|---|---|---|---|---|---|---|---|
| referenceLocatio n | string | Optional | "head" |  | The location of the reference. "head" places it at the beginning of the response. "tail" places it at the end. |  |  |
| defaultLang | string | Optional | - |  | The default search language code, such as zh- CN or en-US. |  |  |
| promptTemplate | string | Optional | Built-in template |  | The prompt template. It must include the {search resul _ ts} and {question} placeholders. |  |  |
|  |  |  |  |  |  | {search resul _ |  |
|  |  |  |  |  | ts} |  |  |
| searchFrom | array of object | Required | - |  | See the search engine configurations below. Configure at least one engine. |  |  |
| searchRewrite | object | Optional | - |  | The search rewrite configuration. Use this to optimize search queries with a Large Language Model (LLM) service. |  |  |

|  |  | "**References | the refe content |
|---|---|---|---|
| onal | :**\n%s" |  |  |

OpenTrek de

**Search rewrite description**

The search rewrite feature uses a Large Language Model (LLM) service to analyze and optimize the user's original query. It can perform the following operations: Determine whether the user's question requires a search engine query. If a query is not required, the search enhancement logic is not executed. Convert the user's natural language query into a combination of keywords that is more effective for search engines.

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| llmServiceName | string | Required | - | The LLM service name. |
| llmServicePort | number | Required | - | The LLM service port. |
| llmApiKey | string | Optional | - | The API key for the LLM service. |
| llmUrl | string | Required | - | The API address for the LLM service. |
| llmModelName | string | Required | - | The LLM model name. |
| timeoutMillisecon d | number | Optional | 30000 | The API call timeout period in milliseconds. |
| maxCount | number | Optional | 3 | The maximum number of queries generated by search rewrite. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

de OpenTrek For Arxiv paper searches, automatically identify relevant paper categories and add category filters. For private knowledge base searches, break down long queries into multiple precise keyword combinations. You can enable this feature when you use the Arxiv or Elasticsearch engines. For Arxiv searches, this feature accurately identifies the paper's field and optimizes English keywords. For private knowledge base searches, this feature provides more precise keyword matching and significantly improves search results.

**Search rewrite configuration**

**General search engine configuration**

| type | string | Required | - | The engine type (google, bing, arxiv, elasticsearch, or quark). |
|---|---|---|---|---|
| serviceName | string | Required | - | The backend service name. |
| servicePort | number | Required | - | The backend service port. |
| apiKey | string | Required | - | The search engine API key or Aliyun AccessKey. |
| count | number | Optional | 10 | The number of results to return for a single search. |
| start | number | Optional | 0 | The search result offset. Results are returned starting from the (start + 1)th result. |
| timeoutMillisecon d | number | Optional | 5000 | The API call timeout period in milliseconds. |
| optionArgs | map | Optional | - | Search engine- specific parameters in key-value format. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| cx | string | Required | - | The Google Custom Search Engine ID. Use this to specify the search scope. |

OpenTrek de

**Google-specific configuration**

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| arxivCategory | string | Optional | - | The paper category to search, such as cs.AI or cs.CL. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| index | string | Required | - | The name of the Elasticsearch index to search. |
| contentField | string | Required | - | The name of the content field to query. |
| semanticTextFiel d | string | Required | - | The name of the embedding field to query. |
| linkField | string | Optional | - | The name of the result link field. This is required when needReference is configured. |
| titleField | string | Optional | - | The name of the result title field. This is required when needReference is configured. |
| username | string | Optional | - | The Elasticsearch username. |
| password | string | Optional | - | The Elasticsearch password. |

|  |  | needReference |
|---|---|---|

|  |  | needReference |
|---|---|---|

de OpenTrek

**Arxiv-specific configuration**

**Elasticsearch-specific configuration**

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| contentMode | string | Optional | "summary" | The content mode: "summary" uses the snippet. "full" uses the full text. `markdownTex t` is prioritized. If it is empty, `mainText` is used. |

OpenTrek de The Reciprocal Rank Fusion (RRF) query used in hybrid search requires Elasticsearch 8.8 or later. Currently, document vectorization relies on the Elasticsearch embedding model. This feature requires an Elasticsearch Enterprise Edition license or a 30-day trial license. For more information about installing the built-in Elasticsearch embedding model, see this document. To install a third-party embedding model, see this document. For a complete tutorial on integrating the ai-search plug-in with Elasticsearch to build a Retrieval-Augmented Generation (RAG) application, see Build a RAG Application with LangChain, Higress, and Elasticsearch.

**Quark-specific configuration**

**Configuration examples**

**Basic configuration (single search engine)**

```
needReference: true searchFrom:
- type: google
  apiKey: "your-google-api-key"
  cx: "search-engine-id"
  serviceName: "google-svc.dns"
  servicePort: 443
  count: 5
  optionArgs:
    fileType: "pdf"
```

**Arxiv search configuration**

```
searchFrom:
- type: arxiv
  serviceName: "arxiv-svc.dns"
  servicePort: 443
  arxivCategory: "cs.AI"
  count: 10
```

de OpenTrek

**Quark search configuration**

```
searchFrom:
- type: quark
  serviceName: "quark-svc.dns"
  servicePort: 443
  apiKey: "quark api key"
  contentMode: "full"  # Optional values: "summary" (default) or "full"
```

**Multiple search engine configuration**

```bash
defaultLang: "en-US"
  # Search Results:
  {search_results}
  # Please answer this question:
  {question}
searchFrom:
- type: google
  apiKey: "google-key"
  cx: "github-search-id"  # Search engine ID for searching GitHub content
  serviceName: "google-svc.dns"
  servicePort: 443
- type: google
  apiKey: "google-key"
  cx: "news-search-id"    # Search engine ID for searching Google News content
  serviceName: "google-svc.dns"
  servicePort: 443
- type: bing
  apiKey: "bing-key"
  serviceName: "bing-svc.dns"
  servicePort: 443
  optionArgs:
    answerCount: "5"
```

**Concurrent query configuration**

Search engines limit the number of results for a single query. For example, Google limits a single query to a maximum of 100 results. To retrieve more results, you can perform the following steps:
1. Set a small `count` value, such as 10.
2. Specify the result offset using the `start` parameter.
3. Send multiple concurrent query requests. Increment the `start` value of each request by
the `count` value. For example, to retrieve 30 results, you can set `count` to 10 and send three concurrent queries with `start` values of 0, 10, and 20. OpenTrek de

```
searchFrom:
- type: google
 apiKey: "your-google-api-key"
 cx: "search-engine-id"
 serviceName: "google-svc.dns"
 servicePort: 443
 start: 0
 count: 10
- type: google
 apiKey: "your-google-api-key"
 cx: "search-engine-id"
 serviceName: "google-svc.dns"
 servicePort: 443
 start: 10
 count: 10
- type: google
 apiKey: "your-google-api-key"
 cx: "search-engine-id"
 serviceName: "google-svc.dns"
 servicePort: 443
 start: 20
 count: 10
```

**Important**

High concurrency may cause rate limiting. Adjust the concurrency level as needed.

**Elasticsearch configuration (for connecting to a private**

**knowledge base)**

```bash
searchFrom:
- type: elasticsearch
  serviceName: "es-svc.static"
  index: "knowledge_base"
  contentField: "content"
  semanticTextField: "semantic_text"
  # username: "elastic"
  # password: "password"
```

**Custom reference format**

```
needReference: true referenceFormat: "### Data Source\n%s" searchFrom:
- type: bing
 apiKey: "your-bing-key"
 serviceName: "search-service.dns"
 servicePort: 8080
```

**Custom reference location**

de OpenTrek

```
needReference: true referenceLocation: "tail" # Add the reference at the end of the response, not the begi nning searchFrom:
- type: bing
  apiKey: "your-bing-key"
  serviceName: "search-service.dns"
  servicePort: 8080
```

**Search rewrite configuration**

```
searchFrom:
- type: google
  apiKey: "your-google-api-key"
  cx: "search-engine-id"
  serviceName: "google-svc.dns"
  servicePort: 443
searchRewrite:
  llmServiceName: "llm-svc.dns"
  llmServicePort: 443
  llmApiKey: "your-llm-api-key"
  llmUrl: "https://api.example.com/v1/chat/completions"
  llmModelName: "gpt-3.5-turbo"
  timeoutMillisecond: 15000
```

**On-demand plug-in configuration**

You can configure the plug-in to be enabled only when the request contains the `web_search_options` field.

```
defaultEnable: false searchFrom:
- type: google
 apiKey: "your-google-api-key"
 cx: "search-engine-id"
 serviceName: "google-svc.dns"
 servicePort: 443
```

This configuration is compatible with the OpenAI search model protocol. The plug-in is activated when the request contains the `web_search_options` field, even if the field is a null object ( `"web_search_options": {}` ).

**Search context size configuration**

You can dynamically adjust the number of search queries by adding the `search_context_size` parameter to the `web_search_options` field in the request.

```json
{
 "web_search_options": {
 "search_context_size": "medium"
 }
}
```

|  | {search results} _ |
|---|---|
| {cur date} _ |  |

| Name | Data type | Require d | Default value | Description |
|---|---|---|---|---|
| cacheKeyFrom.request Body | string | Optional | "messages.@reverse.0. content" | Extracts a string from the request body based on the GJSON PATH syntax. |
| cacheValueFrom.respo nseBody | string | Optional | "choices.0.message.con tent" | Extracts a string from the response body based on the GJSON PATH syntax. |
| cacheStreamValueFro m.responseBody | string | Optional | "choices.0.delta.content " | Extracts a string from the streaming response body based on the GJSON PATH syntax. |

OpenTrek de The `search_context_size` parameter supports the following three levels: `low` : generates one search query for simple questions. `medium` : generates three search queries. This is the default value. `high` : generates five search queries for complex questions. This setting overwrites the `maxCount` value in the configuration. This allows the client to dynamically adjust the search depth based on the complexity of the question.

**Notes**

`January 2, 2006` format. The default template includes guidelines for processing search results and formatting responses. We recommend that you use the default template. You can modify the template if you have specific requirements. Multiple search engines are queried in parallel. The total timeout period is the highest `timeoutMillisecond` value among all search engine configurations, plus the processing time. Arxiv searches do not require an API key. However, you can specify a paper category (`arxivCategory`) to narrow the search scope.

##### AI cache

This plugin caches Large Language Model (LLM) results. You can use the default configurations to cache results for the OpenAI protocol. The plugin supports both streaming and non-streaming responses.

**Runtime properties**

Plugin execution phase: `Authentication phase` Plugin execution priority: `10`

**Configuration description**

|  | cacheKeyPrefix |  | string |  | Optional | "higress-ai-cache" |  | The prefix for the Redis cache key. |
|---|---|---|---|---|---|---|---|---|
|  | cacheTTL |  | intege r |  | Optional | 0 |  | The time-to-live (TTL) for the cache in seconds. The default value is 0, which means the cache never expires. |
|  | redis.serviceName |  | string |  | Required | - |  | The Redis service name. This must be a fully qualified domain name (FQDN) that includes the service type, such as my- redis.dns or redis.my- ns.svc.cluster.local. |
|  | redis.servicePort |  | intege r |  | Optional | 6379 |  | The Redis service port. |
|  | redis.timeout |  | intege r |  | Optional | 1000 |  | The timeout period for Redis requests in milliseconds. |
|  | redis.username |  | string |  | Optional | - |  | The username to log on to Redis. |
|  | redis.password |  | string |  | Optional | - |  | The password to log on to Redis. |
|  |  |  |  |  |  | {"id":"from- |  |  |
|  |  |  |  |  |  |  | {"id":"from- |  |
|  |  |  |  |  |  | cache","choices": |  |  |
|  |  |  |  |  |  | [%s],"model":"gpt- |  | The template for the |
|  | returnResponseTempla |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 4o","object":"chat.co |  | HTTP response. Use %s |
|  |  |  | string |  | Optional |  |  | to mark the part that |
|  | te |  |  |  |  | mpletion","usage": |  | will be replaced by the |
|  |  |  |  |  |  | {"prompt tokens":0,"c _ |  | cache value. |
|  |  |  |  |  |  | ompletion tokens":0," _ |  |  |
|  |  |  |  |  |  | total tokens":0}} _ |  |  |

de OpenTrek

|  |  |  |  |  |  | data:{"id":"from- |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | data:{"id":"from- |  |  |
|  |  |  |  |  |  | cache","choices": |  |  |  |
|  |  |  |  |  |  | [{"index":0,"delta": |  |  |  |
|  |  |  |  |  |  | {"role":"assistant"," |  |  |  |
|  |  |  |  |  |  | content":"%s"},"finis |  | The template for the |  |
|  |  |  |  |  |  | h reason":"stop"}],"m _ |  | streaming HTTP |  |
|  | returnStreamResponse |  |  |  |  |  |  |  |  |
|  |  |  | string |  | Optional | odel":"gpt- |  | response. Use %s to |  |
|  | Template |  |  |  |  |  |  | mark the part that will |  |
|  |  |  |  |  |  | 4o","object":"chat.co |  |  |  |
|  |  |  |  |  |  |  |  | be replaced by the |  |
|  |  |  |  |  |  | mpletion","usage": |  | cache value. |  |
|  |  |  |  |  |  | {"prompt tokens":0,"c _ |  |  |  |
|  |  |  |  |  |  | ompletion tokens":0," _ |  |  |  |
|  |  |  |  |  |  | total tokens":0}}\n\n _ |  |  |  |
|  |  |  |  |  |  | data:[DONE]\n\n |  |  |  |

OpenTrek de

**Configuration example**

```
redis:
  serviceName: my-redis.dns
  timeout: 2000
```

**Advanced usage**

The default cache key is extracted using the GJSON PATH expression: `messages.@reverse.0.content` . This expression inverts the `messages` array and then retrieves the `content` from the first item. GJSON PATH supports conditional syntax. For example, to use the `content` of the last item where `role` is `user` as the key, use the following expression: `messages.@reverse.#`

```
(role=="user").content .
```

To combine the `content` from all items where `role` is `user` into an array for the key, use the following expression: `messages.@reverse.#(role=="user")#.content` . Pipeline syntax is also supported. For example, to retrieve the `content` of the second-tolast item where `role` is `user` as the key, use the following expression:

```
 messages.@reverse.#(role=="user")#.content|1 .
```

For more information, see the official documentation. You can test the syntax using the GJSON Playground.

##### AI intent recognition

The ai-intent plugin intelligently determines how well a user request aligns with the functions of a specific realm or agent. This improves the performance and user experience of various models. This topic describes how to configure the ai-intent plugin.

**Running properties**

Plugin execution phase: `Default phase` . Plugin execution priority: `700` .

**Configuration instructions**

This plugin has a higher priority than other plugins that use intents, such as ai-proxy. Subsequent plugins can call the proxywasm.GetProperty([]string{"intent_category"}) method to retrieve the intent subject. Based on this subject, the plugins can select different cache libraries or large language models (LLMs).

|  | Name |  | Data type | Required |  | Default value |  | Description |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | scene.categor y |  | string | Required |  | - |  | Preset scenario categories, separated by \| , such as finance\|E- |  |  |
|  |  | scene.categor |  |  |  |  |  |  |  |  |
|  | y |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | finance\|E- |  |
|  |  |  |  |  |  |  |  | commerce\|law\|AI |  |  |
|  |  |  |  |  |  |  |  | gateway |  |  |
|  | scene.prompt |  | string | Optional |  | You are an intelligent category detection assistant. Your task is to determine which preset category a user's question belongs to, based on the question and the preset categories, and then provide the corresponding category. The user's question is %s, and the preset categories are %s. Directly return a specific category. If no match is found, return 'NotFound'. |  | The prompt template for LLM requests. |  |  |

|  |  | scene.prompt |
|---|---|---|

de OpenTrek You can create a new large model route for the AI Gateway to allow this plugin to access the large model. For example, you can use /intent as the route prefix, select the model service, and enable the ai-proxy plugin for this route. You can create a new service with a fixed address, such as intent-service. The service must point to 127.0.0.1:80, which is the gateway instance and port. The ai-intent plugin internally calls this service to access the new route. The service name must correspond to the llm.proxyServiceName parameter. Alternatively, you can create a DNS-type service to allow the plugin to access other large models. If you use a service with a fixed address to call the gateway itself, add 127.0.0.1 to the gateway's access whitelist.

**Configuration fields**

|  | llm.proxyServ iceName |  | string | Required | - | The new AI Gateway service that points to the large model. Use the Fully Qualified Domain Name (FQDN) value from the AI Gateway. |
|---|---|---|---|---|---|---|
|  |  | llm.proxyServ | string |  |  |  |
|  | iceName |  |  |  |  |  |
|  | llm.proxyUrl |  | string | Required | - | The full path of the large model route request address. This can be the address of the gateway itself or the address of another large model that uses the OpenAI protocol. For example: http://127.0.0.1:80/int ent/compatible- mode/v1/chat/complet ions. |
|  | llm.proxyDoma in |  | string | Optional | Parsed from `proxyUrl`. | The domain of the model service. |
|  |  | llm.proxyDoma | s |  |  |  |
|  | in |  |  |  |  |  |
|  | llm.proxyPort |  | string | Optional | Parsed from `proxyUrl`. | The port number of the model service. |
|  |  | llm.proxyPort |  |  |  |  |
|  | llm.proxyApiK ey |  | string | Optional | - | If you use an external large model service, configure the corresponding API KEY _ for that model. |
|  |  | llm.proxyApiK | s |  |  |  |
|  | ey |  |  |  |  |  |
|  | llm.proxyMode l |  | string | Optional | qwen-long | The type of the large model. |
|  |  | llm.proxyMode |  |  |  |  |
|  | l |  |  |  |  |  |
|  | llm.proxyTime out |  | number | Optional | 10000 | The timeout period for calling the large model. Unit: ms. Default: 10000 ms. |
|  |  | llm.proxyTime | n |  |  |  |
|  | out |  |  |  |  |  |

|  |  | llm.proxyUrl |
|---|---|---|

OpenTrek de

**Configuration example**

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| identityHeader | string | Optional | "Authorization" | The request header used for identity parsing, such as Authorization or X-Mse-Consumer. |
| fillHistoryCnt | integer | Optional | 3 | The default number of conversation rounds to fill. |
| cacheKeyPrefix | string | Optional | "higress-ai- history:" | The prefix for the Redis cache key. |

de OpenTrek

```
scene:
  category: "Finance|E-commerce|Law|AI Gateway"
  prompt: "You are an intelligent category detection assistant. Your task is to determi
ne which preset category a user's question belongs to, based on the question and the pr eset categories, and then provide the corresponding category. The user's question is:'% s', and the preset categories are:'%s'. Directly return a specific category. If no matc h is found, return 'NotFound'." llm:
  proxyServiceName: "intent-service.static"
  proxyUrl: "http://127.0.0.1:80/intent/compatible-mode/v1/chat/completions"
  proxyDomain: "127.0.0.1"
  proxyPort: "80"
  proxyModel: "qwen-long"
  proxyApiKey: ""
  proxyTimeout: "10000"
```

##### AI conversation history

The ai-history plugin identifies users based on request headers. It automatically caches the conversation history for each user and fills this history into the context of subsequent conversations. You can also query your conversation history. This topic describes how to configure the ai-history plugin.

**Runtime properties**

The plugin runs during the `Default phase` with an execution priority of `650` .

**Configuration fields**

| cacheTTL | integer | Optional | 0 | The cache's time- to-live (TTL) in seconds. The default value is 0, which means the cache never expires. |
|---|---|---|---|---|
| redis.serviceNam e | string | Required | - | The Redis service name. This must be a fully qualified domain name (FQDN) that includes the service type, such as my- redis.dns or redis.my- ns.svc.cluster.loc al. |
| redis.servicePort | integer | Optional | 6379 | The Redis service port. |
| redis.timeout | integer | Optional | 1000 | The timeout period for Redis requests, in milliseconds. |
| redis.username | string | Optional | - | The username to log on to Redis. |
| redis.password | string | Optional | - | The password to log on to Redis. |

OpenTrek de

**Usage examples**

```
redis:
  serviceName: my-redis.dns
  timeout: 2000
```

**Request examples**

**Auto-fill request example:**

First-round request: de OpenTrek

```json
 curl 'http://example.com/api/openai/v1/chat/completions?fill_history_cnt=3' \
 -H 'Accept: application/json, text/event-stream' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer sk-Nzf7RtkdS4s0zFyn5575124129254d9bAf9473A5D7D06dD3'
 --data-raw '{"model":"qwen-
long","frequency_penalty":0,"max_tokens":800,"stream":false,"messages":[
 {
 "role": "user",
 "content": "Can Higress replace Nginx?"
 }
 ],"presence_penalty":0,"temperature":0.7,"top_p":0.95}'
```

After the request is filled:

**Note**

Because this is the request for the first conversation round, no history is filled. The request remains unchanged. First-round response:

```json
{
 "id": "02f4c621-820e-97d4-a905-1e3d0d8f59c6",
 "choices": [
 {
 "index": 0,
 "message": {
 "role": "assistant",
 "content": "Higress and Nginx can both function as gateways, but their design philosop
hies and application scenarios differ. Nginx is widely known as a high-performance HTTP and reverse proxy server. Higress is a cloud-native gateway that provides basic routing and forwarding capabilities. It also integrates many cloud-native features, such as ser vice mesh, observability, and security management.\n\nTherefore, if you want to deploy applications in a cloud-native environment and need advanced features for modern applic ations, such as service administration, phased releases, circuit breaking, throttling, and security authentication, Higress is an excellent alternative to Nginx. However, for simple static websites or if you only need basic reverse proxy functionality, a traditi onal Nginx configuration might be simpler and more direct."
 },
 "finish_reason": "stop"
 }
```

`],`

```json
 "created": 1724077770,
 "model": "qwen-long",
 "object": "chat.completion",
 "usage": {
 "prompt_tokens": 7316,
 "completion_tokens": 164,
 "total_tokens": 7480
 }
}
```

Second request: OpenTrek de

```json
 curl 'http://example.com/api/openai/v1/chat/completions?fill_history_cnt=3' \
 -H 'Accept: application/json, text/event-stream' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer sk-Nzf7RtkdS4s0zFyn5575124129254d9bAf9473A5D7D06dD3'
 --data-raw '{"model":"qwen-
long","frequency_penalty":0,"max_tokens":800,"stream":false,"messages":[
 {
 "role": "user",
 "content": "What about Spring Cloud Gateway?"
 }
 ],"presence_penalty":0,"temperature":0.7,"top_p":0.95}'
```

After the request is completed:

**Note**

This is a second-round request. The conversation history from the previous round is automatically populated.

```json
 curl 'http://example.com/api/openai/v1/chat/completions?fill_history_cnt=3' \
 -H 'Accept: application/json, text/event-stream' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer sk-Nzf7RtkdS4s0zFyn5575124129254d9bAf9473A5D7D06dD3'
 --data-raw '{"model":"qwen-
long","frequency_penalty":0,"max_tokens":800,"stream":false,"messages":[
 {
 "role": "user",
 "content": "Can Higress replace Nginx?"
 },
 {
 "role": "assistant",
 "content": "Higress and Nginx can both function as gateways, but their design philosop
hies and application scenarios differ. Nginx is widely known as a high-performance HTTP and reverse proxy server. Higress is a cloud-native gateway that provides basic routing and forwarding capabilities. It also integrates many cloud-native features, such as ser vice mesh, observability, and security management.\n\nTherefore, if you want to deploy applications in a cloud-native environment and need advanced features for modern applic ations, such as service administration, phased releases, circuit breaking, throttling, and security authentication, Higress is an excellent alternative to Nginx. However, for simple static websites or if you only need basic reverse proxy functionality, a traditi onal Nginx configuration might be simpler and more direct."
 },
 {
 "role": "user",
 "content": "What about Spring Cloud Gateway?"
 }
 ],"presence_penalty":0,"temperature":0.7,"top_p":0.95}'
```

For each request, include the current question and the number of conversation rounds to fill. The conversation history is then automatically filled.

**Example: Retrieving historical data**

de OpenTrek

```bash
curl 'http://example.com/api/openai/v1/chat/completions/ai-history/query?cnt=3' \
 -H 'Accept: application/json, text/event-stream' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer sk-Nzf7RtkdS4s0zFyn5575124129254d9bAf9473A5D7D06dD3'
```

Example response: [

```json
 {
 "role": "user",
 "content": "Can Higress replace Nginx?"
 },
 {
 "role": "assistant",
 "content": "Higress and Nginx can both function as gateways, but their design philosop
hies and application scenarios differ. Nginx is widely known as a high-performance HTTP and reverse proxy server. Higress is a cloud-native gateway that provides basic routing and forwarding capabilities. It also integrates many cloud-native features, such as ser vice mesh, observability, and security management.\\n\\nTherefore, if you want to deplo y applications in a cloud-native environment and need advanced features for modern appl ications, such as service administration, phased releases, circuit breaking, throttling , and security authentication, Higress is an excellent alternative to Nginx. However, f or simple static websites or if you only need basic reverse proxy functionality, a trad itional Nginx configuration might be simpler and more direct."
 },
 {
 "role": "user",
 "content": "What about Spring Cloud Gateway?"
 },
 {
 "role": "assistant",
 "content": "Compared to Spring Cloud Gateway, Higress is also an API gateway, but ther
e are some key differences between them:\\n\\n- **Design philosophy**: Spring Cloud Gat eway is primarily designed for inter-service communication and routing in a microservic es model. As part of the Spring Cloud ecosystem, it focuses more on microservice scenar ios for Java developers. As a cloud-native gateway, Higress not only focuses on inter-s ervice communication but also provides a range of cloud-native features, such as servic e mesh, observability, and security management.\\n- **Deployment method**: Spring Cloud Gateway typically runs as part of a microservice application within an application serv er. Higress is usually deployed as an independent microservice or a containerized servi ce in a Kubernetes environment, making it suitable for modern cloud-native deployment m odels.\\n- **Extensibility and integration**: Higress offers broader integration and su pport, such as deep integration with ecosystems like Istio and Kubernetes. This allows it to better adapt to complex cloud-native environments.\\n\\nTherefore, if your applic ation is built on Spring Cloud and you want a lightweight, easy-to-integrate service ga teway, Spring Cloud Gateway might be a suitable choice. However, if you are building or refactoring a cloud-native application and require more powerful routing rules, service administration, and observability features, Higress is a better option."
 },
 {
 "role": "user",
 "content": "Can Higress replace Nginx?"
 },
{
```

| Field | Type | Required | Default value | Description |
|---|---|---|---|---|
| serviceName | string | required | - | The name of the AI service or the gateway service that supports AI- Proxy. |
| serviceDomain | str | optional | - | The domain name or IP address of the AI service or the gateway service that supports AI- Proxy. |
| servicePath | str | optional | ’/v1/chat/complet ions’ | The base path of the AI service or the gateway service that supports AI- Proxy. |

OpenTrek de

```json
 {
 "role": "assistant",
 "content": "Higress and Nginx can both function as gateways, but their design philosop
hies and application scenarios differ. Nginx is widely known as a high-performance HTTP and reverse proxy server. Higress is a cloud-native gateway that provides basic routing and forwarding capabilities. It also integrates many cloud-native features, such as ser vice mesh, observability, and security management.\\n\\nTherefore, if you want to deplo y applications in a cloud-native environment and need advanced features for modern appl ications, such as service administration, phased releases, circuit breaking, throttling , and security authentication, Higress is an excellent alternative to Nginx. However, f or simple static websites or if you only need basic reverse proxy functionality, a trad itional Nginx configuration might be simpler and more direct."
 }
```

] The response contains three historical conversations. If the cnt parameter is not specified, all cached historical conversations are returned by default.

##### AI JSON formatting

The ai-json-resp plugin structures AI responses based on a default or user-configured JSON Schema to prepare them for processing by subsequent plugins. This plugin supports only non-streaming responses. This topic describes how to configure the ai-json-resp plugin.

**Runtime properties**

Plugin execution phase: `Default Phase` . Plugin execution priority: `150` .

**Configuration parameters**

| serviceUrl | string | optional | - | The URL of the AI service or the gateway service that supports AI- Proxy. The plugin automatically extracts the domain and path to fill in serviceDomain or servicePath if they are not configured. |
|---|---|---|---|---|
| servicePort | int | optional | 443 | The gateway service port. |
| serviceTimeout | int | optional | 50000 | The default request timeout period. |
| maxRetry | int | optional | 3 | The number of retries if the response cannot be correctly extracted and formatted. |
| contentPath | str | optional | ”choices.0.messa ge.content” | The gpath used to extract the response result from the Large Language Model (LLM) response. |
| jsonSchema | string (json) | optional | - | The JSON Schema used to validate the response. If this field is empty, the plugin only validates that the response is in a valid JSON format and returns it. |

de OpenTrek

| enableSwagger | bool |  | optional |  |  | false |  | Specifies whether to use the Swagger protocol for validation. |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| enableOas3 | bool |  | optional |  |  | true |  | Specifies whether to use the OpenAPI Specification (OAS) 3.0 protocol for validation. |  |  |
| enableContentDis position | bool |  | optional |  |  | true |  | Specifies whether to enable the Content- Disposition header. If enabled, the plugin adds Content- |  |  |
|  |  |  |  |  |  |  |  |  | Content- |  |
|  |  |  |  |  |  |  |  | Disposition: |  |  |
|  |  |  |  |  |  |  |  | attachment; |  |  |
|  |  |  |  |  |  |  |  | filename="respo |  |  |
|  |  |  |  |  |  |  |  | nse.json" |  |  |

OpenTrek de

**Note**

For performance reasons, the maximum supported JSON Schema depth is 6 by default. If a JSON Schema exceeds this depth, it is not used for validation. The plugin only checks if the returned response is in a valid JSON format.

**Request and response parameters**

**Request parameters**: This plugin uses the OpenAI request format. The request includes
the `model` and `messages` fields. The `model` field specifies the name of the AI model. The `messages` field is a list of conversation messages. Each message contains a `role` field and a `content` field. The `role` field specifies the role of the message sender, and the `content` field contains the message content.

```json
{
 "model": "gpt-4",
 "messages": [
 {"role": "user", "content": "give me a api doc for add the variable x to x+5"}
```

]

```
}
```

For more information about other request parameters, see the documentation for the configured AI service or gateway service.
**Response parameters**:
de OpenTrek Returns a `JSON response` that conforms to the defined JSON Schema constraints. If no JSON Schema is defined, a valid `JSON response` is returned. If an internal error occurs, an error message is returned in the following format: {

```json
"Code": 10XX, "Msg": "Error message" } .
```

**Request example**

```json
curl -X POST "http://localhost:8001/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{
  "model": "gpt-4",
  "messages": [
    {"role": "user", "content": "give me a api doc for add the variable x to x+5"}
```

]

```
}'
```

**Response examples**

**Normal response**

The system returns JSON data validated against the JSON Schema. If no JSON Schema is configured, the system returns valid JSON data that conforms to the JSON standard.

```json
{
 "apiVersion": "1.0",
 "request": {
 "endpoint": "/add_to_five",
 "method": "POST",
 "port": 8080,
 "headers": {
 "Content-Type": "application/json"
 },
 "body": {
 "x": 7
 }
 }
}
```

**Error response**

If an error occurs, the system returns a status code of `500` and the response body contains an error message in JSON format. The message includes two fields: `Code` for the error code and `Msg` for the error message.

```json
{
 "Code": 1006,
 "Msg": "retry count exceed max retry count"
}
```

**Error codes**

| Error code | Description |
|---|---|
| 1001 | The configured JSON Schema is not in a valid JSON format. |
| 1002 | The configured JSON Schema failed to compile. It is not a valid JSON Schema format, or its depth exceeds jsonSchemaMaxDepth and rejectOnDepthExceeded is set to true. |
| 1003 | Cannot extract valid JSON from the response. |
| 1004 | The response is an empty string. |
| 1005 | The response does not conform to the JSON Schema definition. |
| 1006 | The number of retries exceeds the maximum limit. |
| 1007 | Cannot get the response content. This may be caused by an upstream service configuration error or an incorrect ContentPath. |
| 1008 | serviceDomain is empty. Note that serviceDomain and serviceUrl cannot both be empty. |

OpenTrek de

**Service configuration**

This plugin requires an upstream service configuration to support the automatic retry mechanism. You can configure either an `AI service that supports the OpenAI API` or a

```
 local gateway service .
```

**AI service that supports the OpenAI API**

For example, the following is a basic configuration for Qwen:

| Name | Data type | Required | Defau lt value | Description |
|---|---|---|---|---|

de OpenTrek

```
serviceName: qwen serviceDomain: dashscope.aliyuncs.com apiKey: [Your API Key] servicePath: /compatible-mode/v1/chat/completions jsonSchema:
 title: ReasoningSchema
 type: object
 properties:
 reasoning_steps:
 type: array
 items:
 type: string
 description: The reasoning steps leading to the final conclusion.
 answer:
 type: string
 description: The final answer, taking into account the reasoning steps.
 required:
 - reasoning_steps
 - answer
 additionalProperties: false
```

**Local gateway service**

To reuse existing service configurations, this plugin also supports configuring a local gateway service. For example, if an AI-proxy service is already configured on the gateway, you can configure it directly as follows:
1. Create a service with a fixed IP address of 127.0.0.1:80, such as localservice.static.
2. Add the service configuration for localservice.static to the configuration file.

```
serviceName: localservice serviceDomain: 127.0.0.1 servicePort: 80
```

3. The plugin automatically extracts information such as the request path and headers. This
avoids duplicate configuration for the AI service.

##### AI request/response transform

The AI request/response transform plug-in uses a large language model (LLM) to modify the headers and bodies of requests and responses.

**Runtime properties**

The plug-in is executed in the `Authentication phase` with an execution priority of `410` .

**Configuration parameters**

| request.enable | bool | Required | - | Specifies whether to enable transformation in the request phase. |
|---|---|---|---|---|
| request.prompt | string | Required | - | The prompt used for transformation in the request phase. |
| response.enable | string | Required | - | Specifies whether to enable transformation in the response phase. |
| response.prompt | string | Required | - | The prompt used for transformation in the response phase. |
| provider.serviceName | string | Required | - | The service name of the DNS type. Currently, only Qwen is supported. |
| provider.domain | string | Required | - | The domain name of the LLM service. |
| provider.apiKey | string | Required | - | The API key for the Alibaba Cloud dashscope service. |

|  | provider.serviceName |
|---|---|

OpenTrek de

**Configuration example**

```
request:
    enable: false
    prompt: "If the request path starts with /httpbin, remove the /httpbin prefix. Do n
ot change anything else." response:
    enable: true
    prompt: "Modify the following HTTP response: 1. Change the content-type to applicat
ion/json. 2. Convert the body from XML to JSON. 3. Remove the content-length." provider:
    serviceName: qwen
    domain: dashscope.aliyuncs.com
    apiKey: xxxxxxxxxxxxx
```

Accessing the `/xml` endpoint of the original httpbin service returns the following result: de OpenTrek

```xml
<?xml version='1.0' encoding='us-ascii'?> <!-- A SAMPLE set of slides --> <slideshow
    title="Sample Slide Show"
    date="Date of publication"
    author="Yours Truly"
```

>

```xml
    <!-- TITLE SLIDE -->
    <slide type="all">
      <title>Wake up to WonderWidgets!</title>
    </slide>
    <!-- OVERVIEW -->
    <slide type="all">
        <title>Overview</title>
        <item>Why WonderWidgets are great</item>
        <item/>
        <item>Who buys WonderWidgets</item>
    </slide>
</slideshow>
```

With the preceding configuration, accessing the `/xml` endpoint of httpbin through the gateway returns the following result:

```json
{
  "slideshow": {
    "title": "Sample Slide Show",
    "date": "Date of publication",
    "author": "Yours Truly",
    "slides": [
      {
        "type": "all",
        "title": "Wake up to WonderWidgets!"
      },
      {
        "type": "all",
        "title": "Overview",
        "items": [
          "Why WonderWidgets are great",
          "",
          "Who buys WonderWidgets"
```

]

```
      }
```

]

```
  }
}
```

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| prepend | array of message object | Optional | - | The statements to insert before the initial input. |
| append | array of message object | Optional | - | The statements to insert after the initial input. |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| role | string | Required | - | The role. |
| content | string | Required | - | The message. |

OpenTrek de

##### AI prompt

The AI prompt plugin lets you insert prompts before and after Large Language Model (LLM) requests.

**Runtime properties**

Plugin execution stage: `Default stage` . Plugin execution priority: `450` . The following table describes the configuration of a message object. The following code provides a configuration example:

```
prepend:
- role: system
  content: "Please answer the question in English"
append:
- role: user
  content: "After answering the question, try to ask a follow-up question"
```

The following is an example of a request that uses the preceding configuration: de OpenTrek

```json
curl http://localhost/test \ -H "content-type: application/json" \ -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "Who are you?"
    }
```

]

```
}
```

After the plugin processes the request, the resulting request is:

```json
curl http://localhost/test \ -H "content-type: application/json" \ -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "Please answer the question in English"
    },
    {
      "role": "user",
      "content": "Who are you?"
    },
    {
      "role": "user",
      "content": "After answering the question, try to ask a follow-up question"
    }
```

]

```
}
```

**Add user location data to prompts using the geo-ip plugin**

To add user location data before and after LLM requests, you must enable both the geo-ip plugin and the AI prompt decorator plugin. The geo-ip plugin must have a higher execution priority than the AI prompt decorator plugin within the same request processing stage. The geo-ip plugin determines the user's location based on their IP address and then passes this information to subsequent plugins through request properties. For example, in the default stage, you can set the execution priority for the geo-ip plugin to 1000 and the execution priority for the ai-prompt-decorator plugin to 500. The following code provides a configuration example for the geo-ip plugin:

```
ipProtocal: "ipv4"
```

The following code provides a configuration example for the AI prompt decorator plugin: OpenTrek de

```
prepend:
- role: system
  content: "The user's current location is Country: ${geo-country}, Province: ${geo-pro
vince}, City: ${geo-city}" append:
- role: user
  content: "After answering the question, try to ask a follow-up question"
```

The following is an example of a request that uses the preceding configuration:

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "What is the weather like today?"
    }
```

]

```
}'
```

After the plugin processes the request, the resulting request is:

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "The user's current location is Country: China, Province: Beijing, Cit
y: Beijing"
    },
    {
      "role": "user",
      "content": "What is the weather like today?"
    },
    {
      "role": "user",
      "content": "After answering the question, try to ask a follow-up question"
    }
```

]

```
}'
```

##### AI prompt templates

You can use AI prompt templates to quickly create similar AI requests.

**Execution properties**

| Name | Data type | Required | Defau lt value | Description |
|---|---|---|---|---|
| templates | array of object | Required | - | The template settings. |

| Name | Data type | Require d | Defa ult value | Description |
|---|---|---|---|---|
| name | string | Require d | - | The name of the template. |
| template.model | string | Require d | - | The name of the model. |
| template.messages | array of object | Require d | - | The input for the large language model (LLM). |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| role | string | Required | - | The role. |
| content | string | Required | - | The message. |

de OpenTrek

**p**

**p**

The plugin executes during the `Default stage` with an execution priority of `500` . The following table describes the parameters for a template object. The following table describes the parameters for a message object.

**Example**

The following code shows an example configuration:

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| modelKey | string | Optional | model | The location of the model parameter in the request body. |

OpenTrek de

```
templates:
- name: "developer-chat"
  template:
    model: gpt-3.5-turbo
    messages:
    - role: system
      content: "You are a {{program}} expert, in {{language}} programming language."
    - role: user
      content: "Write me a {{program}} program."
```

The following code shows a sample request body that uses the preceding configuration:

```json
{
  "template": "developer-chat",
  "properties": {
    "program": "quick sort",
    "language": "python"
  }
}
```

##### Model mapping

The model-mapper plugin maps model parameters. This topic describes how to configure the model-mapper plugin.

**Configuration fields**

|  | modelMapping |  | map of string | Optional | - | The AI model mapping table. It maps the model name in a request to a model name supported by the service provider. Prefix matching is supported. For example, use "gpt-3-" to match all models whose names start with "gpt-3-". Use "*" as a key to configure a universal fallback mapping. If the target name for the mapping is an empty string "", the original model name is retained. |
|---|---|---|---|---|---|---|
|  | enableOnPathSu ffix |  | array of string | Optional | ["/v1/chat/compl etions"] | The plugin takes effect only on requests with these specific path suffixes. |
|  |  | enableOnPathSu | arra |  |  |  |
|  | ffix |  |  |  |  |  |

|  |  | modelMapping |
|---|---|---|

| qwen-max |  | . The |
|---|---|---|
| en to |  |  |

de OpenTrek

**Runtime properties**

Plugin execution phase: `Authentication phase` . Plugin execution priority: `800` .

**Effects**

Consider the following configuration:

```
modelMapping:
  'gpt-4-*': "qwen-max"
  'gpt-4o': "qwen-vl-plus"
  '*': "qwen-turbo"
```

`turbo` . For example, the original request is:

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| modelKey | string | Optional | model | The location of the model parameter in the request body. |

OpenTrek de

```json
{
    "model": "gpt-4o",
    "frequency_penalty": 0,
    "max_tokens": 800,
    "stream": false,
    "messages": [{
        "role": "user",
        "content": "What is the GitHub address of the main Higress project repository?"
    }],
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}
```

After the plugin processes the request, the original Large Language Model (LLM) request body is changed to:

```json
{
    "model": "qwen-vl-plus",
    "frequency_penalty": 0,
    "max_tokens": 800,
    "stream": false,
    "messages": [{
        "role": "user",
        "content": "What is the GitHub address of the main Higress project repository?"
    }],
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}
```

##### Model routing

The model-router plugin routes requests based on the model parameter in the Large Language Model (LLM) protocol. This topic describes how to configure the model-router plugin.

**Configuration fields**

|  | addProviderHea der |  | string | Optional | - | Parses the provider name from the model parameter and adds it to a specified request header. |
|---|---|---|---|---|---|---|
|  |  | addProviderHea | str |  |  |  |
|  | der |  |  |  |  |  |
|  | modelToHeader |  | string | Optional | - | Adds the model parameter directly to a specified request header. |
|  | enableOnPathSu ffix |  | array of string | Optional | ["/v1/chat/compl etions"] | The plugin takes effect only for requests with these specific path suffixes. |
|  |  | enableOnPathSu | arra |  |  |  |
|  | ffix |  |  |  |  |  |

|  |  | modelToHeader |
|---|---|---|

de OpenTrek

**Runtime properties**

Plugin execution phase: `Authentication phase` . Execution priority: `900` .

**How it works**

**Route based on the model parameter**

Use the following configuration:

```
modelToHeader: x-higress-llm-model
```

The plugin extracts the model parameter from the request and sets it as the value of the xhigress-llm-model request header. This header can then be used for routing. For example, the original LLM request body is:

```json
{
    "model": "qwen-long",
    "frequency_penalty": 0,
    "max_tokens": 800,
    "stream": false,
    "messages": [{
        "role": "user",
        "content": "What is the GitHub address of the main Higress project repository?"
    }],
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}
```

After the plugin processes the request, the following request header is added for route matching.

```
 x-higress-llm-model: qwen-long
```

OpenTrek de

**Extract the provider field from the model parameter for routing**

**Important**

In this pattern, you must specify the provider in the `model` parameter using a / as a separator. Use the following configuration:

```
addProviderHeader: x-higress-llm-provider
```

The plugin extracts the provider from the model parameter, if present. This provider is set as the value of the x-higress-llm-provider request header, which can be used for routing. The plugin then rewrites the model parameter to contain only the model name. For example, the original LLM request body is:

```json
{
    "model": "dashscope/qwen-long",
    "frequency_penalty": 0,
    "max_tokens": 800,
    "stream": false,
    "messages": [{
        "role": "user",
        "content": "What is the GitHub address of the main Higress project repository?"
    }],
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}
```

After the plugin processes the request, the following request header is added for route matching.

```
 x-higress-llm-provider: dashscope
```

The original LLM request body is changed to:

```json
{
    "model": "qwen-long",
    "frequency_penalty": 0,
    "max_tokens": 800,
    "stream": false,
    "messages": [{
        "role": "user",
        "content": "What is the GitHub address of the main Higress project repository?"
    }],
    "presence_penalty": 0,
    "temperature": 0.7,
    "top_p": 0.95
}
```

#### Authentication

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|
| global auth _ | bool | Optional (Instance-level configuration only) | - | This parameter can only be configured at the instance level. If set to `true`, authentication is enabled globally. If set to `false`, authentication is enabled only for the configured domain names and routes. If this parameter is not configured, authentication is enabled globally only when no domain name or route configurations exist. This ensures backward compatibility. |
| consumers | array of object | Required | - | Configures the callers of the service to authenticate requests. |

de OpenTrek

##### Key authentication

**Feature description**

The `key-auth` plugin provides authentication and authorization using API keys. It parses API keys from the URL parameters or headers of an HTTP request and verifies that the API key has permission to access the service.

**Configuration fields**

Authorization and authentication configurations cannot coexist within the same rule. For requests that pass authentication and authorization, an `X-Mse-Consumer` field is added to the request header. This field identifies the name of the caller.

| keys | array of string | Required | - | The name of the source field for the API key. It can be a URL parameter or an HTTP request header name. |
|---|---|---|---|---|
| in query _ | bool | At least one of in query and _ in header _ must be `true`. | true | If set to `true`, the gateway attempts to parse the API key from URL parameters. |
| in header _ | bool | At least one of in query and _ in header _ must be `true`. | true | If set to `true`, the gateway attempts to parse the API key from HTTP request headers. |

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|
| credential | string | Required | - | Configures the access credential for this consumer. |
| name | string | Required | - | Configures the name of this consumer. |

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|

OpenTrek de The following table describes the configuration fields for each item in `consumers` .

**Authorization configuration (optional)**

| allow | array of string | Optional (Not for instance-level configuration) | - | This parameter can only be configured on fine-grained rules, such as routes or domain names. For requests that meet the matching conditions, configure the consumers that are allowed access. This provides fine- grained access control. |
|---|---|---|---|---|

de OpenTrek

**Configuration examples**

**Configure global authentication and route-level authorization**

The following configuration enables key authentication and authorization for specific gateway routes or domain names. The value of the `credential` field must be unique. Configure the plugin at the instance level as follows:

```
global_auth: false consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

Configure the `route-a` and `route-b` routes as follows:

```
allow:
- consumer1
```

Configure the `*.example.com` and `test.com` domain names as follows: OpenTrek de

```
allow:
- consumer2
```

**Note**

In this example, `route-a` and `route-b` are the route names that you enter when you create gateway routes. When a request matches these routes, callers with the name `consumer1` are granted access. All other callers are denied access. In this example, `*.example.com` and `test.com` are used to match the domain name of the request. When a domain name matches, callers with the name `consumer2` are granted access. All other callers are denied access. Based on this configuration, the following requests are allowed:

**Assume that a request matches the route-a route and the API key is set in a URL**

**parameter.**

```bash
curl http://xxx.hello.com/test?apikey=2bda943c-ba2b-11ec-ba07-00163e1250b5
```

**The API key is set in the HTTP request header.**

```bash
curl http://xxx.hello.com/test -H 'x-api-key: 2bda943c-ba2b-11ec-ba07- 00163e1250b5'
```

After successful authentication and authorization, an `X-Mse-Consumer` field is added to the request header to identify the name of the caller. In this example, its value is `consumer1` . The following requests will be denied access:

**A 401 error is returned if the request does not include an API key.**

```bash
curl http://xxx.hello.com/test
```

**A 401 error is returned if the provided API key is unauthorized.**

```bash
curl http://xxx.hello.com/test?apikey=926d90ac-ba2e-11ec-ab68-00163e1250b5
```

**A 403 error is returned if the caller identified by the API key in the request does**

**not have access permissions.**

```bash
# consumer2 is not on the allow list of route-a
curl http://xxx.hello.com/test?apikey=c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
```

**Enable at the gateway instance level**

The following configuration enables key authentication at the gateway instance level. This requires all requests to be authenticated.

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|
| consumers | array of object | Required. | - | Configures the callers of the service to authenticate requests. |
| global auth _ | array of string | Optional. Can be configured only at the instance level. | - | Can be configured only at the instance level. If set to true, the authentication mechanism is enabled globally. If set to false, the authentication mechanism is enabled only for the configured domain names and routes. If you do not configure this parameter, authentication is enabled globally only if no domain names or routes are configured. This ensures backward compatibility. |

| 17 |  |  |  | > Document Version: 2026062 |
|---|---|---|---|---|

de OpenTrek

```
global_auth: true consumers:
- credential: 2bda943c-ba2b-11ec-ba07-00163e1250b5
 name: consumer1
- credential: c8c8e9ca-558e-4a2d-bb62-e700dcc40e35
 name: consumer2
keys:
- apikey
- x-api-key
```

##### JWT authentication

The jwt-auth plugin provides authentication and authorization based on JSON Web Tokens (JWT). It parses JWTs from the URL parameters, request headers, or cookies of an HTTP request. It also verifies that the token has the required access permissions. Unlike standard JWT authentication and authorization, the jwt-auth plugin also identifies the caller. This lets you configure different JWT credentials for different callers. This topic describes how to configure the jwt-auth plugin.

**Configuration fields**

The following table describes the fields for each subkey in `consumers` .

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|
| name | string | Required. | - | The name of the consumer. |
| jwks | string | Optional. `jwks` or `remote jwks` is _ required. | - | A JSON-formatted string specified by JSON Web Key (JWK). It is a JSON Web Key Set that consists of the public keys or symmetric keys used to verify the signature in the JWT. |
| remote jwks _ | object | Optional. Specify either `jwks` or `remote jwks`. _ | {"uri":" http://1 27.0.0. 1/keys", "servic e":"test. static"," port":"8 0","ttl": 30000," timeout ":3000} | Pulls the JWKS from a specified URI of a specified service at regular intervals. If both `jwks` and `remote jwks` are _ configured, the JWKS pulled by `remote jwks` takes _ precedence. Note The size of the JWKS returned by `remote jwks` should _ not exceed 1 MB. |
| issuer | string | Optional. | - | The issuer of the JWT. The value must be the same as the `iss` field in the payload. |
| claims | object | Optional. | - | The key-value pairs correspond to the key-value pairs in the payload. You can use this field to verify that multiple fields are consistent with the payload. For example, if you configure `aud: mobile-site`, the `aud` field in the payload must be `mobile-site`. |
| claims to he _ _ aders | array of object | Optional. | - | Extracts specified fields from the JWT payload, sets them in the specified request headers, and then forwards them to the backend. |

OpenTrek de

| from header _ s | array of object | Optional. | [{"nam e":"Aut horizati on","val ue pref _ ix":"Be arer"}] | Extracts the JWT from the specified request headers. |
|---|---|---|---|---|
| from params _ | array of string | Optional. | access _ token | Extracts the JWT from the specified URL parameters. |
| from cookies _ | array of string | Optional. | - | Extracts the JWT from the specified cookies. |
| clock skew s _ _ econds | number | Optional. | 60 | The allowed clock skew in seconds when verifying the `exp` and `iat` fields of the JWT. |
| keep token _ | bool | Optional. | true | Specifies whether to keep the JWT when forwarding the request to the backend. |

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|
| name | string | Required. | - | The request header from which to extract the JWT. |
| value prefix _ | string | Required. | - | The prefix to remove from the request header value. The remaining part is used as the JWT. |

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|

de OpenTrek

**Note**

The default values are used only when `from_headers` , `from_params` , and `from_cookies` are not configured. The following table describes the configuration fields for each item in `from_headers` . The following table describes the configuration fields for each item in `claims_to_headers` .

| claim | string | Required. | - | A specified field in the JWT payload. The value must be a string or an unsigned integer. |
|---|---|---|---|---|
| header | string | Required. | - | The request header to which the value of the field extracted from the payload is set. The request is then forwarded to the backend. |
| override | bool | Optional. | true | true: An existing request header with the same name is overwritten. false: The new header is appended. |

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|
| uri | string | Required. | - | The request URL. |
| service | string | Required. | - | Example for a Kubernetes service: `foo.default.svc.cluster.lo cal`. Example for a Nacos service: `foo.DEFAULT- GROUP.public.nacos`. For a DNS service named `test`, enter `test.dns`. For a static IP service named `test`, enter `test.static`. |
| port | bool | Required. | - | The service port. |
| timeout | bool | Optional. | 3000 | The request timeout period for the service, in milliseconds. |
| ttl | number | Optional. | 30000 | The cache duration, in milliseconds. |

OpenTrek de The following table describes the configuration fields for each item in `remote_jwks` .

**Authorization configuration (optional)**

| Name | Data type | Requirement | Defaul t value | Description |
|---|---|---|---|---|
| allow | array of string | Optional. Cannot be configured at the instance level. | - | Can be configured only on fine- grained rules such as routes or domain names. For requests that meet the matching conditions, configure the allowed consumers to implement fine-grained access control. |

de OpenTrek

**Important**

Authorization and authentication configurations cannot exist in the same rule. For requests that pass authentication and authorization, an `X-Mse-Consumer` field is added to the request header to identify the caller's name.

**Configuration examples**

**Globally configure authentication and route-level authorization**

The following configuration enables JWT Auth authentication and authorization for specific gateway routes or domain names.

**Note**

If a JWT can match multiple JWKS, the first matching consumer in the configuration order is used.

**Plugin configuration**

Configure the plugin at the instance level as follows: OpenTrek de

```json
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

**Route and domain name configuration**

Configure the plugin for the `route-a` and `route-b` routes as follows:

```
allow:
- consumer1
```

Configure the plugin for the `*.example.com` and `test.com` domain names as follows:

```
allow:
- consumer2
```

| cation, the | X-Mse-Consumer |  |
|---|---|---|
| consumer1 |  |  |
|  |  | , which identifie |

de OpenTrek

**Note**

In this example, `route-a` and `route-b` are the names of the gateway routes. If a request matches either of these routes, access is granted to callers with the `name` `consumer1` , and denied to all other callers. This example uses `*.example.com` and `test.com` to match the domain name of a request. If the domain name matches, callers with the `name` `consumer2` are allowed access, while all other callers are denied access.

**Request examples**

Based on this configuration, the following requests are allowed, assuming they match the `route-a` route. Set the JWT in a URL parameter.

```bash
curl 'http://xxx.hello.com/test? access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEy****.eyJp************.-v BSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
```

Set the JWT in an HTTP request header.

```bash
curl http://xxx.hello.com/test -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEyMyJ9.eyJpc3MiOiJhYmNkIiwic3ViIjoidGVzdC ImlhdCI6MTY2NTY2MDUyNywiZXhwIjoxODY1NjczODE5fQ.vBSV0bKeDwQcuS6eeSZN9dLTUnSnZVk8eVCXdooCQ4'
```

**Verify the result**

The following requests will be denied: If a request does not provide a JWT, an HTTP 401 status code is returned. If the caller matched by the provided JWT does not have access permissions, an HTTP 403 status code is returned.

**Enable at the gateway instance level but disable for a specific**

Configure the plugin at the instance level as follows:

|  | route-b |
|---|---|
| true |  |

OpenTrek de

```json
global_auth: true consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

Configure the plugin for the `route-b` route as follows:

```
_disable_: true
```

`route-b` in this example is the route name that you entered when you created the gateway route. Because `_disable_` is set to `true` , this plugin is disabled when a request matches this route. No JWT authentication is performed, and all users are allowed access. de OpenTrek authentication for all requests. Both `consumer1` and `consumer2` are allowed access.

**Enable at the domain name level but disable for a specific**

Configure the plugin at the instance level as follows:

```json
consumers:
- name: consumer1
  issuer: abcd
  jwks: |
    {
      "keys": [
        {
          "kty": "oct",
          "kid": "123",
          "k":
"hM0k3AbXBPpKOGg__Ql2Obcq7s60myWDpbHXzgKUQdYo7YCRp0gUqkCnbGSvZ2rGEl4YFkKqIqW7mTHdj-bcqX pNr-NOznEyMpVPOIlqG_NWVC3dydBgcsIZIdD- MR2AQceEaxriPA_VmiUCwfwL2Bhs6_i7eolXoY11EapLQtutz0BV6ZxQQ4dYUmct-- 7PLNb4BWJyQeWu0QfbIthnvhYllyl2dgeLTEJT58wzFz5HeNMNz8ohY5K0XaKAe5cepryqoXLhA-V-O1OjSG8lC NdKS09OY6O0fkyweKEtuDfien5tHHSsHXoAxYEHPFcSRL4bFPLZ0orTt1_4zpyfew",
          "alg": "HS256"
        }
```

]

```json
    }
- name: consumer2
  issuer: abc
  jwks: |
    {
      "keys": [
        {
          "kty": "RSA",
          "e": "AQAB",
          "use": "sig",
          "kid": "123",
          "alg": "RS256",
          "n":
"i0B67f1jggT9QJlZ_8QL9QQ56LfurrqDhpuu8BxtVcfxrYmaXaCtqTn7OfCuca7cGHdrJIjq99rz890NmYFZuvha LMt2iyiSb9LZJAeJmHf7ecguXS_- 4x3hvbsrgUDi9tlg7xxbqGYcrco3anmalAFxsbswtu2PAXLtTnUo6aYwZsWA6ksq4FL3anPNL5oZUgIp3HGyhhLTLdlQcC83jzxbguOim-0OEz- N4fniTYRivK7MlibHKrJfO3xa_6whBS07HW4Ydc37ZN3Rx9Ov3ZyV0idFblU519nUdqp_inXj1eEpynlxH60Ys_aT POGZh_25KXGdF_ZC_MSRw"
        }
```

]

```
    }
```

Configure the plugin for the `route-b` route as follows:

```
_disable_: true
```

You can configure the plugin for the `*.example.com` domain name as follows:

| HTTP status code | Error message | Cause |
|---|---|---|
| 401 | Jwt missing | The request header does not provide a JWT. |
| 401 | Jwt expired | The JWT has expired. |
| 401 | Jwt verification fails | JWT payload verification failed. For example, the `iss` field does not match. |
| 403 | Access Denied | No permission to access the current route. |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| consumers | array of object | This parameter is required. | - | Specifies the service callers to authenticate requests. |

OpenTrek de

```
allow:
- consumer1
- consumer2
```

In this example, `route-b` is the name that you specified for the gateway route. If a request matches this route, the plugin is disabled because `_disable_` is set to `true` . As a result, JWT authentication is not performed, and all users are allowed access. In this example, `*.example.com` is used to match the domain name of the request. When the domain name matches, access is granted to callers with the `name` `consumer1` or `consumer2` . Access is denied to all other callers. Configuration rules are matched sequentially. The first rule that is matched is executed, and no subsequent rules are processed. Route matching has a higher priority than domain name matching. This means a configuration can apply to a domain name, but be disabled for a specific route under that domain name.

**Related error codes**

##### Basic authentication

The basic-auth plugin provides authentication and authorization based on the HTTP Basic Auth standard. This topic describes how to configure the basic-auth plugin.

**Plugin type**

Authentication and authorization.

**Configuration fields**

| global auth _ | Array of strings | Optional (instance- level configuration only). | - | Can only be configured at the instance level. If set to `true`, the authentication mechanism applies globally. If set to `false`, the authentication mechanism applies only to configured domain names and routes. If not configured, the authentication mechanism applies globally only when no domain name or route configurations exist. This ensures compatibility for existing users. |
|---|---|---|---|---|

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| credential | string | Required | - | You can configure the access credential for this consumer. |
| name | string | Required. | - | The name of the consumer. |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| allow | array of string | Optional (not for instance-level configuration). | - | Can only be configured on fine- grained rules such as routes or domain names. For requests that meet the matching conditions, configure the allowed consumers to implement fine-grained access control. |

de OpenTrek The following table describes the fields for each item in `consumers` .

**Authorization configuration (optional)**

**Important**

Authorization and authentication configurations cannot be used in the same rule. If a request passes authentication and authorization, an `X-Mse-Consumer` field is added to the request header to identify the caller's name. OpenTrek de

**Configuration examples**

**Configure global authentication and route-level authorization**

The following configuration enables Basic Auth authentication and authorization for specific gateway routes or domain names.

**Note**

Use a colon (:) to separate the username and password in the credential information. The `credential` field cannot have duplicate values. Configure the plugin at the instance level as follows:

```
global_auth: false consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

Configure the plugin for the `route-a` and `route-b` routes as follows:

```
allow:
- consumer1
```

Configure the plugin for the `*.example.com` and `test.com` domain names as follows:

```
allow:
- consumer2
```

**Note**

`route-a` and `route-b` in this example are the route names that you specified when you created the gateway routes. If a request matches these routes, only callers with the `name` `consumer1` are allowed access. All other callers are denied access. `*.example.com` and `test.com` in this example are used to match the domain name of a request. If a domain name matches, only callers with the `name` `consumer2` are allowed access. All other callers are denied access. Based on this configuration, the following requests are allowed: You are prompted for a username and password.

| HTTP status code | Error message | Cause |
|---|---|---|
| 401 | Request denied by Basic Auth check. No Basic Authentication information found. | The request does not provide a credential. |

de OpenTrek

```bash
# Assume the following request matches the route-a route
# Specify using the -u parameter of curl
curl -u admin:123456 http://xxx.hello.com/test
# Or, directly specify the Authorization request header. The username and password mu
st be Base64-encoded. curl -H 'Authorization: Basic YWRtaW46MTIzNDU2' http://xxx.hello.com/test
```

**Note**

After successful authentication and authorization, an `X-Mse-Consumer` field is added to the request header. In this example, the value of this field is `consumer1` , which is the name of the caller. The following requests are denied: The request does not include a username or password. A 401 error is returned.

```bash
curl http://xxx.hello.com/test
```

The request includes an incorrect username or password. A 401 error is returned.

```bash
curl -u admin:abc http://xxx.hello.com/test
```

The caller that is authenticated by the username and password does not have access permissions. A 403 error is returned.

```bash
# consumer2 is not in the allow list for route-a
curl -u guest:abc http://xxx.hello.com/test
```

**Enable at the gateway instance level**

The following configuration enables Basic Auth authentication at the gateway instance level. All requests must be authenticated to gain access.

```
global_auth: true consumers:
- credential: 'admin:123456'
  name: consumer1
- credential: 'guest:abc'
  name: consumer2
```

**Related error codes**

| 401 | Request denied by Basic Auth check. Invalid username and/or password. | The request credential is invalid. |
|---|---|---|
| 403 | Request denied by Basic Auth check. Unauthorized consumer. | The requesting caller does not have access permissions. |

| Name | Data type | Description | Default value |
|---|---|---|---|
| cookie name _ | string | the name of the cookie that the oauth proxy _ creates. Should be changed to use a cookie prefix( Host- or __ Secure- ) if -- __ cookie-secure is set. | " oauth2 proxy" _ _ |
| cookie secret _ | string | the seed string for secure cookies (optionally base64 encoded) | - |
| cookie domains _ | string\|list | Optional cookie domains to force cookies to (e.g. .yourcompany.c om ). The longest domain matching the request’s host will be used (or the shortest cookie domain if there is no match). | - |

|  |  |  | Host- __ |  |  |
|---|---|---|---|---|---|
|  |  | Secure- __ |  |  |  |
|  |  |  |  | ) if |  |
|  | cookie-secure |  |  |  |  |

| .yourcompany.c |  |
|---|---|

| t | om |
|---|---|

OpenTrek de

##### OIDC authentication

The oidc plugin supports identity authentication using OpenID Connect (OIDC). The plugin also enhances protection against cross-site request forgery (CSRF) attacks. It supports the Logout Endpoint and Refresh Token mechanisms that are defined in the OIDC protocol. After the Wasm plugin authenticates a request using OIDC, the request carries an `Authorization` header that contains the corresponding Access Token.

**Runtime properties**

Plugin execution phase: `Authentication phase` . Plugin execution priority: `350` .

**Configuration fields**

| cookie path _ | string | an optional cookie path to force cookies to (e.g. /poc/ ) | "/" |
|---|---|---|---|
| cookie expire _ | duration | expire timeframe for cookie. If set to 0, cookie becomes a session-cookie which will expire when the browser is closed. | 168h0m0s |
| cookie refresh _ | duration | refresh the cookie after this duration; 0 to disable | - |
| cookie secure _ | bool | set secure (HTTPS only) cookie flag | true |
| cookie httponly _ | bool | set HttpOnly cookie flag | true |
| cookie samesite _ | string | set SameSite cookie attribute ( "lax" , "strict" , "none" , or "" ). | "" |
| cookie csrf per reque _ _ _ st | bool | Enable having different CSRF cookies per request, making it possible to have parallel requests. | false |
| cookie csrf expire _ _ | duration | expire timeframe for CSRF cookie. | 15m |
| client id _ | string | the OAuth Client ID. | - |
| client secret _ | string | the OAuth Client Secret. | - |
| provider | string | OAuth provider. | oidc |

|  |  | "lax" |  |
|---|---|---|---|

de OpenTrek

|  | pass authorization he _ _ ader |  |  | bool |  |  | pass OIDC IDToken to upstream via Authorization Bearer header. |  | true |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | oidc issuer url _ _ |  |  | string |  |  | the OpenID Connect issuer URL, e.g. "https://dev- |  |  |  |
|  |  |  |  |  |  |  |  | "https://dev- | - |  |
|  |  |  |  |  |  |  | o43xb1mz7ya7ach4.us. |  |  |  |
|  |  |  |  |  |  |  | auth0.com" |  |  |  |
|  | oidc verifier request t _ _ _ imeout |  |  | uint32 |  |  | OIDC verifier discovery request timeout. |  | 2000(ms) |  |
|  | scope |  |  | string |  |  | OAuth scope specification. |  | - |  |
|  | redirect url _ |  |  | string |  |  | the OAuth Redirect URL, e.g. "https://inter |  |  |  |
|  |  |  |  |  |  |  |  | "https://inter |  |  |
|  |  |  |  |  |  |  | nalapp.yourcompany.c |  |  |  |
|  |  |  |  |  |  |  |  |  | - |  |
|  |  |  |  |  |  |  | om/oauth2/callback" |  |  |  |
|  | service name _ |  |  | string |  |  | registered name of the OIDC service, e.g. auth.dns , ke ycloak.static |  | - |  |
|  | service port _ |  |  | int64 |  |  | service port of the OIDC service. |  | - |  |
|  | service host _ |  |  | string |  |  | host of the OIDC service when type is static ip. |  | - |  |
|  | match type _ |  |  | string |  |  | match type ( whitelist or bl acklist ). |  | "whitelist" |  |
|  | match list _ |  |  | rule\|list |  |  | a list of (match rule domain, _ _ match rule path, and _ _ match rule type). _ _ |  | - |  |

|  |  | auth.dns |
|---|---|---|
|  | ycloak.static |  |

| ke | - |
|---|---|

|  |  | whitelist |
|---|---|---|
|  | acklist |  |

| bl |  | "whi | telist" |
|---|---|---|---|

OpenTrek de

| match rule domain _ _ | string | match rule domain, support wildcard pattern such as *.bar.com . | - |
|---|---|---|---|
| match rule path _ _ | string | match rule path such as /headers . | - |
| match rule type _ _ | string | match rule type can be exact or pref ix or regex . | - |

|  |  | exact |  |
|---|---|---|---|
|  | ix |  |  |

| pref |  |
|---|---|

de OpenTrek

**Usage**

**Generate a cookie secret**

```python
python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
```

For more information, see Oauth2-proxy Generating a Cookie Secret.

**Whitelist and blacklist modes**

The plugin supports whitelist and blacklist modes. The whitelist mode is used by default. If the whitelist is empty, all requests require authentication. The plugin supports wildcard domain names for domain name matching, such as `*.bar.com` . The supported matching rules are `exact` , `prefix` , and `regex` .

**Whitelist mode**

```
match_type: 'whitelist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/foo'
 match_rule_type: 'prefix'
```

Requests that have a path with the prefix `/foo` under the wildcard domain name `*.bar.com` do not require authentication.

**Blacklist mode**

```
match_type: 'blacklist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/headers'
 match_rule_type: 'prefix'
```

Only requests that have a path with the prefix `/header` under the wildcard domain name `*.bar.com` require authentication.

**Log off a user**

OpenTrek de To log off a user, you can redirect the user to the `/oauth2/sign_out` endpoint. This endpoint removes only the cookie that is set by oauth2-proxy. This means that the user remains logged on to the OIDC Provider and may be automatically logged on again when the user accesses the application. Therefore, you can use the `rd` query parameter to redirect the user to the logoff page of the authentication provider. Redirect the user to an address that is similar to the following example. Note the URL encoding.

```
/oauth2/sign_out?rd=https%3A%2F%2Fmy-oidcprovider.example.com%2Fsign_out_page
```

Alternatively, you can include the redirection URL in the `X-Auth-Request-Redirect` header:

```
GET /oauth2/sign_out HTTP/1.1 X-Auth-Request-Redirect: https://my-oidc-provider.example.com/sign_out_page ...
```

The redirection URL can include the `post_logout_redirect_uri` parameter to specify the page to which the OIDC Provider redirects the user after the user logs off, such as the logoff page of the backend service. If this parameter is not included, the user is redirected to the default logoff page of the OIDC Provider. For more information, see the Auth0 and Keycloak examples below.

**Note**

If the OIDC Provider supports session management and discovery, the sign_out_page must be the `end_session_endpoint` that is obtained from the metadata.

**OIDC service with HTTPS protocol**

If the OIDC Provider uses the HTTPS protocol, see Configure the backend service protocol: HTTPS in the Higress documentation. You can use the `higress.io/backend-protocol:` `"HTTPS"` annotation to configure requests to be forwarded to the backend service using HTTPS. For more information, see the Ingress configuration in the Auth0 example.

**Configuration examples**

**Auth0 configuration example**

**Configuration procedure**

**Step 1: Configure your Auth0 account**

Log on to the Auth0 developer website. Register a test web app.

**Important**

You must configure items such as Allowed Callback URLs, Allowed Logout URLs, and Allowed Web Origins. Otherwise, the OIDC Provider considers the redirection URL or logoff URL of the user invalid.

**Step 2: Configure the service source in the AI Gateway**

Create an auth0 DNS source in the service sources of AI Gateway. de OpenTrek

**Step 3: Configure HTTPS for the OIDC service**

```
apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 name: auth0-ingress
 annotations:
 higress.io/destination: auth.dns
 higress.io/backend-protocol: "HTTPS"
 higress.io/ignore-path-case: "false"
spec:
 ingressClassName: higress
 rules:
 - host: foo.bar.com
 http:
 paths:
 - path: /
 pathType: Prefix
 backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
```

**Step 4: Configure the Wasm plugin**

```
redirect_url: 'http://foo.bar.com/oauth2/callback' oidc_issuer_url: 'https://dev-o43xb1mz7ya7ach4.us.auth0.com/' client_id: 'XXXXXXXXXXXXXXXX' client_secret: 'XXXXXXXXXXXXXXXX' scope: 'openid email offline_access' cookie_secret: 'nqav************_8DCfY=' service_name: 'auth.dns' service_port: 443 match_type: 'whitelist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/foo'
 match_rule_type: 'prefix'
```

**Important**

You must configure the service source first. This is because the Wasm plugin needs to access the configured service to obtain the openid-configuration during initialization.

**Test the results**

**Access the service page and get redirected if not logged on**

OpenTrek de

**Log on successfully and get redirected to the service page**

In the headers, you can view the _oauth2_proxy cookie for subsequent logon attempts. The Authorization header corresponds to the ID Token. The backend service uses the ID Token to obtain user information.

**Access the logoff URL and get redirected to the logoff page**

```
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdevo43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout
```

de OpenTrek

**Access the logoff URL and get redirected to a specified URI**

**with the post_logout_redirect_uri parameter**

```
http://foo.bar.com/oauth2/sign_out?rd=https%3A%2F%2Fdevo43xb1mz7ya7ach4.us.auth0.com%2Foidc%2Flogout%3Fpost_logout_redirect_uri%3Dhttp% A%2F%2Ffoo.bar.com%2Ffoo
```

**Important**

The URI for the `post_logout_redirect_uri` redirection must be configured in the Allowed URLs of the OIDC Provider to work as expected. OpenTrek de

**Keycloak configuration example**

**Configuration procedure**

**Step 1: Get started with keycloak on docker**

https://www.keycloak.org/getting-started/getting-started-docker

**Important**

You must configure items such as Valid redirect URIs, Valid post logout URIs, and Web origins. Otherwise, the OIDC Provider considers the redirection URL or logoff URL of the user invalid.

**Step 2: Configure the service source in the AI Gateway**

Create a Keycloak static address service in the service sources of AI Gateway.

**Step 3: Configure the Wasm plugin**

de OpenTrek

```
redirect_url: 'http://foo.bar.com/oauth2/callback' oidc_issuer_url: 'http://127.0.0.1:9090/realms/myrealm' client_id: 'XXXXXXXXXXXXXXXX' client_secret: 'XXXXXXXXXXXXXXXX' scope: 'openid email' cookie_secret: 'nqavJrGvRmQxWwGNptLdyUVKcBNZ2b18Guc1n_8DCfY=' service_name: 'keycloak.static' service_port: 80 service_host: '127.0.0.1:9090' match_type: 'blacklist' match_list:
 - match_rule_domain: '*.bar.com'
 match_rule_path: '/headers'
 match_rule_type: 'prefix'
```

**Test the results**

**Access the service page and get redirected if not logged on**

**Log on successfully and get redirected to the service page**

OpenTrek de

**Access the logoff URL and get redirected to the logoff page**

```
http://foo.bar.com/oauth2/sign_out? rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenidconnect%2Flogout
```

**Access the logoff URL and get redirected to a specified URI**

**with the post_logout_redirect_uri parameter**

```
http://foo.bar.com/oauth2/sign_out? rd=http%3A%2F%2F127.0.0.1:9090%2Frealms%2Fmyrealm%2Fprotocol%2Fopenidconnect%2Flogout%3Fpost_logout_redirect_uri%3Dhttp%3A%2F%2Ffoo.bar.com%2Ffoo
```

de OpenTrek

**OIDC flow**

oidc_process

**OIDC flow explained**

**User not logged on**

1. A user attempts to access the corresponding service API.

```bash
curl --url "foo.bar.com/headers"
```

2. AI Gateway redirects the user to the logon page of the OIDC Provider. The redirection
includes OIDC authentication parameters, such as client_id, response_type, and scope. AI Gateway also sets a CSRF cookie to prevent CSRF attacks.

```bash
curl --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/authorize"\
 --url-query "approval_prompt=force" \
 --url-query "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --url-query "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
 --url-query "response_type=code" \
 --url-query "scope=openid+email+offline_access" \
 --url-query "state=nT06************_hCjskrH_VupPqdcdw%3A%2Ffoo" \
 --header "Set-Cookie:
_oauth2_proxy_csrf=LPruATEDgcdmelr8zScD_ObhsbP4zSzvcgmPlcNDcJpFJ0OvhxP2hFotsUkZnYxd5KsIjzeIXGTOjf8TKcbTHbDItaQoZORXI_0id3qeY0Jt78223DPeJ1xBqa8VO0UiEOUFOR53FGxirJOdKFxaAvxDFb1Ok=|17189624 5|V1QGWyjQ4hMNOQ4Jtf17HeQJdVqHdt5d65uraFduMIU=; Path=/; Expires=Fri, 21 Jun 2024 08:06:20 GMT; HttpOnly"
```

3. The user is redirected to the logon page.
OpenTrek de
4. The user enters a username and password to log on.
5. The user is redirected back to AI Gateway with an authorization grant. The request carries
the state parameter to validate the CSRF cookie and an authorization code to exchange for a token.

```bash
curl --url "http://foo.bar.com/oauth2/callback" \
 --url-query "state=nT06xdCqn4IqemzBRV5hmO73U_hCjskrH_VupPqdcdw%3A%2Ffoo" \
 --url-query "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm"
```

6. AI Gateway validates that the encrypted state value stored in the CSRF cookie is the same
as the state value in the URL parameter.
7. You can exchange the grant for an id_token and an access_token.

```bash
curl -X POST \
 --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
 --data "grant_type=authorization_code" \
 --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --data
"client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ " \
 --data "redirect_uri=http%3A%2F%2Ffoo.bar.com%2Foauth2%2Fcallback" \
 --data "code=0bdopoS2c2lx95u7iO0OH9kY1TvaEdJHo4lB6CT2_qVFm" \
```

The response contains an id_token, an access_token, and a refresh_token for future token refreshes. de OpenTrek

```json
{
 "access_token": "eyJh************..WP_WRVM-
y3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o xrOOJIzXTgsfFVA2x15gjBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EPomFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs- 344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP- KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh BFNX6A.mgGGeeWgugfXcUcsX4T5dQ",
 "refresh_token": "GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG",
 "id_token":
"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imc1Z1ExSF9ZbTY0WUlvVkQwSVpXTCJ9 yJlbWFpbCI6IjE2MDExNTYyNjhAcXEuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJpc3MiOiJ dHRwczovL2Rldi1vNDN4YjFtejd5YTdhY2g0LnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJZYWdGcVJEOX mTklhYWM1QmFtamhzU2F0anJBbnNuWiIsImlhdCI6MTcxOTE5ODYzOCwiZXhwIjoxNzE5MjM0NjM4L JzdWIiOiJhdXRoMHw2NjVkNzFlNzRjMTMxMTc3YmU2NmU2MDciLCJzaWQiOiJjdDJVOF9ZUS16VDdF GkwRTNNeUstejc5ZGlWUWhhVSJ9.gfzXKJ0FeqzYqOUDLQHWcUG19IOLqkpLN09xTmIat0umrlGV5V SumgWH3XJmmwnhdb8AThH3Jf-7kbRJzu4rM- BbGbFTRBTzNHeUajFOFrIgld5VENQ_M_sXHkTp0psWKSr9vF24kmilCfSbvC5lBKjt878ljZ7-x teWuaUYOMUdcJb4DSv0-zjX01sonJxYamTlhji3M4TAW7VwhwqyZt8dBhVSNaRw1wUKj- M1JrBDLyx65sroZtSqVA0udIrqMHEbWYb2de7JjzlqG003HRMzwOm7OXgEd5ZVFqgmBLosgixOU5DJ A26nlqK92Sp6VqDMRvA-3ym8W_m-wJ_A",
 "scope": "openid email offline_access",
 "expires_in": 86400,
 "token_type": "Bearer"
}
```

8. AI Gateway encrypts and stores the obtained id_token, access_token, and refresh_token in
the _oauth2_proxy cookie.
9. AI Gateway redirects the user to the backend service that the user originally accessed and
sets the cookie. This cookie is used for subsequent validation of the user's logon status. At the same time, AI Gateway purges the _oauth2_proxy_csrf cookie. OpenTrek de

```
"Set-Cookie": [
 "_oauth2_proxy_csrf=; Path=/; Expires=Mon, 24 Jun 2024 02:17:39 GMT;
HttpOnly",
 "_oauth2_proxy=8zM_Pcfpp_gesKFe4SMg08o5Iv0A8WAOQOmG1-vZBbQ56UggYVC0Cu-
gFMEoxJZU5q1O5vqRlVBizlLetgVjRCksGVbttwl8tQ7h5YiyIubbbtvF1T4JzLh3QfzUUrwbB- VznOkh8qLbjAhddocecjBt4rMiDyceKXqMr4eO5TUEMx4vHtJYnTYalMeTYhGXk5MNSyrdZX9NnQnk rCjiOQM13ggwob2nYwhGWaAlgzFSWkgkdtBy2Cl_YMWZ8_gKk9rDX289- JrJyGpr5k9O9RzRhZoY2iE3Mcr8-Q37RTji1Ga22QO- XkAcSaGqY1Qo7jLdmgZTYKC5JvtdLc4rj3vcbveYxU7R3Pt2vEribQjKTh4Sqb0aA03p4cxXyZN4SU BW1NAOm4JLPUhKJy8frqC9_E0nVqPvpvnacaoQs8WkX2zp75xHoMa3SD6KZhQ5JUiPEiNkOaUsyafL ht6lLkNDhgzW3BP2czoe0DCDBLnsot0jH-qQpMZYkaGr- ZnRKI1OPl1vHls3mao5juOAW1VB2A9aughgc8SJ55IFZpMfFMdHdTDdMqPODkItX2PK44GXpHeLxkOqrzp3GHtMInpL5QIQlTuux3erm3CGntlUE7JBtN2T9LEb8XfIFu58X9_vzMun4JQlje2Thi9_taI_z1DSaTtvNNb54wJfSPwYCCl4OsH- BacVmPQhH6TTZ6gP2Qsm5TR2o1U2D9fuVkSM- OPCG9l3tILambIQwC3vofMW6X8SIFSmhJUDvN7NbwxowBiZ6Y7GJRZlAk_GKDkpsdrdIvC67QqczZF hRVnm6qigPO41APCbcO6fgTwyOhbP3RrZZKWSIqWJYhNE3_Sfkf0565H7sC7Hc8XUUjJvP3WnjKS9x7KwzWadsUjV3-Q-VNl-rXTguVNAIirYKqrMNMZGCRcJqcLnUF0V_J2lVmFyVsSlE3t0sDw2xmbkOwDptXFOjQL5Rb4esUMYdCBWFajBfvUtcZE tYhD0kb6VcbjXO3NCVW5qKh_l9C9SRCc7TG1vcRAqUQlRXHacTGWfcWsuQkCJ3Mp_oWaDxs1GRDykQ xAn5sTICovThWEU2C6o75grWaNrkj5NU- 0eHh3ryvxLmGLBOXZV9OQhtKShWmUgywSWMxOHOuZAqdAPULc8KheuGFjXYp- RnCbFYWePJmwzfQw89kSkj1KUZgMYwKEjSz62z2qc9KLczomv76ortQzvo4Hv9kaW6xVuQj5R5Oq6_ MBOqsmUMzcXpxCIOGjcdcZRBc0Fm09Uy9oV1PRqvAE4PGtfyrCaoqILBix8UIww63B07YGwzQ-h AXDysBK- Vca2x7GmGdXsNXXcTgu00bdsjtHZPDBBWGfL3g_rMAXr2vWyvK4CwNjcaPAmrlF3geHPwbIePT0hsk boX1v1bsuhzsai7rGM4r53pnb1ZEoTQDa1B- HyokFgo14XiwME0zE1ifpNzefjpkz1YY2krJlqfCydNwoKaTit4tD2yHlnxAeFF9iIrxzSKErNUFpm La7ge7V33vhEH-6k5oBTLE2Q2BrC6aAkLCcPwU9xv_SzBDQPRY0MEYv3kGF03Swo1crRbGhaifYX9NiHDsmG6r1vAnx0MAOw2Jzuz2x6SSdfBrzlcoWBlrwiZzd9kAKq75n1Uy9uzZ8SRnkBrEZyS BwEbu196VklkRE0jqwC-e3wWNNuviSOfwkVeX- 7QdOoO10yw9VK2sW52lFvIEf4chv_ta7bGfAZOWBjpktG6ZLD81SE6A88zpqG2SysSyNMp9hl-u mG-5sFsjCn_c9E8bDvwkUOUVb9bNqhBDsZgR0BNPawiOZjmyfhzmwmWfzgFzfFSV6BvOwNRi3sCOHTsWcuk9NBQ_YK8CpNkVl3WeIBSDfidimuC_QV9UWKs1GPk35ZRkM4zKtL 2JsBFWKaDy_P80TcOzcMBoP8gIBClXZ-WUqfE8s1yyc4jrqqL1_wJ24ef1O9FktsbyZiDKXw2vnqsT8-g_hCeG-unrT1ZFscf8oNdqczARHX- K4vKH2k3uIqEx1M=|1719199056|2rsgdUIClHNEpxBLlHOVRYup6e4oKensQfljtmn4B80=; P ath=/; Expires=Mon, 01 Jul 2024 03:17:36 GMT; HttpOnly"
```

]
0. AI Gateway checks whether a cookie that stores the user's token information exists and
whether the cookie has expired.
1. The request is sent to the corresponding API with the `Authorization` header, which
contains the user's access_token. de OpenTrek

```bash
curl --url "foo.bar.com/headers"
 --header "Authorization: Bearer
eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtbzQzeGIxbXo3eW 3YWNoNC51cy5hdXRoMC5jb20vIn0..WP_WRVMy3fM1sN4.fAQqtKoKZNG9Wj0OhtrMgtsjTJ2J72M2klDRd9SvUKGbiYsZNPmIl_qJUf81D3VIjD59o xrOOJIzXTgsfFVA2x15gjBlNh68N7dyhXu9237Tbplweu1jA25IZDSnjitQ3pbf7xJVIfPnWcrzl6uT8G1EPomFcl6AQprV2FoKFMCGFCgeafuttppKe1a8mpJDj7AFLPs- 344tT9mvCWmI4DuoLFh0PiqMMJBByoijRSxcSdXLPxZng84j8JVF7H6mFa-dj-icP- KLy6yvzEaRKz_uwBzQCzgYK434LIpqw_PRuN3ClEsenwRgIsNdVjvKcoAysfoZhmRy9BQaE0I7qToh BFNX6A.mgGGeeWgugfXcUcsX4T5dQ"
```

2. The backend service retrieves the user authorization information based on the
access_token and returns the corresponding HTTP response.

```json
{
 "email": "******",
 "email_verified": false,
 "iss": "https://dev-o43xb1mz7ya7ach4.us.auth0.com/",
 "aud": "YagFqRD9tfNIaac5BamjhsSatjrAnsnZ",
 "iat": 1719198638,
 "exp": 1719234638,
 "sub": "auth0|665d71e74c131177be66e607",
 "sid": "ct2U8_YQ-zT7E8i0E3MyK-z79diVQhaU"
}
```

**User token refresh**

1. A user attempts to access the corresponding service API.

```bash
curl --url "foo.bar.com/headers"
```

2. AI Gateway validates the token's time-to-live (TTL).
3. If a refresh_token is detected in the cookie, AI Gateway accesses the corresponding
interface to exchange the refresh_token for a new id_token and a new access_token.

```bash
curl -X POST \
 --url "https://dev-o43xb1mz7ya7ach4.us.auth0.com/oauth/token" \
 --data "grant_type=refresh_token" \
 --data "client_id=YagFqRD9tfNIaac5BamjhsSatjrAnsnZ" \
 --data
"client_secret=ekqv5XoZuMFtYms1NszEqRx03qct6BPvGeJUeptNG4y09PrY16BKT9IWezTrrhJ " \
 --data "refresh_token=GrZ1f2JvzjAZQzSXmyr1ScWbv8aMFBvzAXHBUSiILcDEG"
```

4. The request is sent to the corresponding API with the Authorization header, which contains
the new access_token.
5. The backend service retrieves the user authorization information based on the
access_token and returns the corresponding HTTP response.

##### HMAC authentication

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| consumers | array of object | Required | - | Configures the service callers used to authenticate requests. |
| date offset _ | number | Optional | - | The maximum allowed time offset for the client, in seconds. The client's UTC is parsed from the Date request header. This parameter helps prevent replay attacks. If you do not configure this parameter, no verification is performed. |
| global auth _ | Array of strings | Optional: This is an instance-level configuration only. | - | This parameter can only be configured at the instance level. If set to `true`, authentication is enabled globally. If set to `false`, authentication is enabled only for the configured domain names and routes. If this parameter is not configured, authentication is enabled globally only when no domain names or routes are configured. This maintains compatibility with previous user behavior. |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|

OpenTrek de The hmac-auth plugin generates unforgeable signatures for HTTP requests based on the Hash-based Message Authentication Code (HMAC) algorithm. The plugin uses these signatures to perform identity authentication and authorization. This topic describes how to configure the hmac-auth plugin.

**Plugin type**

Authentication and authorization.

**Configuration fields**

The following table describes the fields for each item in the `consumers` array.

| key | string | Required | - | Configures the access credential for the consumer. |
|---|---|---|---|---|
| secret | string | Required | - | Configures the secret used to generate the signature. |
| name | string | Required | - | Configures the name of the consumer. |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| allow | array of string | Optional configuration (non- instance-level) | - | This parameter can only be configured in fine-grained rules, such as routes or domain names. For requests that match the conditions, configure the allowed consumers to implement fine-grained access control. |

de OpenTrek

**Authorization configuration (optional)**

**Important**

Authorization and authentication configurations cannot exist in the same rule. For requests that pass both authentication and authorization, an `X-Mse-Consumer` field is added to the request header to identify the caller's name.

**Configuration examples**

**Configure global authentication and route-level authorization**

The following configuration enables HMAC authentication and authorization for specific gateway routes or domain names.

**Important**

The value of the `key` field must be unique. Configure the plugin at the instance level as follows:

```
global_auth: false consumers:
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

OpenTrek de For the `route-a` and `route-b` routes, configure the plugin as follows:

```
allow:
- consumer1
```

For the `*.example.com` and `test.com` domain names, configure the plugin as follows:

```
allow:
- consumer2
```

**Note**

The `route-a` and `route-b` specified in this example are the route names that you entered when you created the gateway routes. When a request matches these routes, callers with the `name` `consumer-1` are allowed access. Other callers are denied access. The `*.example.com` and `test.com` specified in this example are used to match the domain name of the request. When a domain name match is found, callers with the `name` `consumer-2` are allowed access. Other callers are denied access.

**Enable at the gateway instance level**

```
global_auth: true consumers:
- key: appKey-example-1
  secret: appSecret-example-1
  name: consumer-1
- key: appKey-example-2
  secret: appSecret-example-2
  name: consumer-2
```

**Signature mechanism**

**Prerequisites**

You must configure the credentials that are required to generate and verify signatures in the plugin configuration. key: Set in the `x-ca-key` request header. secret: Used to generate the request signature.

**How the client generates a signature**

**Process overview**

The client generates a signature in three steps:
1. Extract key data from the original request to obtain a string to sign.
2. Use an encryption algorithm and the configured `secret` to encrypt the string to sign and
obtain the signature.
3. Add all signature-related headers to the original HTTP request to create the final HTTP
request. de OpenTrek

**String-to-sign extraction process**

The client must extract key data from the HTTP request and combine it into a string to sign. The format of the string to sign is as follows:

```
HTTPMethod Accept Content-MD5 Content-Type Date Headers PathAndParameters
```

The seven fields above form the entire string to sign. The fields are separated by line feeds (`\n`). If the `Headers` field is empty, do not add a line feed after it. For other empty fields, you must still include the line feed. The signature calculation is case-sensitive. The extraction rule for each field is as follows: HTTPMethod: The HTTP method in uppercase, such as POST. Accept: The value of the `Accept` header in the request. This field can be empty. You must set the `Accept` header explicitly. If the `Accept` header is empty, some HTTP clients set a default value of `*/*` , which causes signature verification to fail. Content-MD5: The value of the `Content-MD5` header in the request. This field can be empty. The `Content-MD5` header is calculated only when the request has a body that is not in a form format. The following Java code shows how to calculate the `Content-MD5` value.

```
String content-MD5 = Base64.encodeBase64(MD5(bodyStream.getBytes("UTF-8")));
```

Content-Type: The value of the `Content-Type` header in the request. This field can be empty. Date: The value of the `Date` header in the request. This field can be empty if `date_offset` is not enabled. Otherwise, it is used for time offset verification. Headers: You can select specific headers to include in the signature. The rules for concatenating the header string are as follows: The keys of the headers included in the signature calculation are sorted alphabetically and then concatenated as follows:

```
HeaderKey1 + ":" + HeaderValue1 + "\n" + HeaderKey2 + ":" + HeaderValue2 + "\n" + ... HeaderKeyN + ":" + HeaderValueN + "\n"
```

If a header has an empty value, use `HeaderKey:` + `\n` for the signature. The key and the colon must be retained. A comma-separated list of all header keys included in the signature is placed in the `X-` `Ca-Signature-Headers` header. The following headers are not included in the header signature calculation: `X-Ca- Signature`, `X-Ca-Signature-Headers`, `Accept`, `Content-MD5`, `Content-Type`, and `Date`. PathAndParameters: This field contains the path and all parameters from the query and form. It is structured as follows: OpenTrek de

```
Path + "?" + Key1 + "=" + Value1 + "&" + Key2 + "=" + Value2 + ... "&" + KeyN + "=" + ValueN
```

**Note**

The key-value pairs for query and form parameters are sorted alphabetically by key and then concatenated as shown above. If there are no query or form parameters, use only the path. Do not add a `?`. If a query or form contains an array parameter (parameters with the same key but different values), use the first value for the signature calculation.

**String-to-sign extraction example**

Initial HTTP request:

```
POST /http2test/test?param1=test HTTP/1.1 host:api.aliyun.com accept:application/json; charset=utf-8 ca_version:1 content-type:application/x-www-form-urlencoded; charset=utf-8 x-ca-timestamp:1525872629832 date:Wed, 09 May 2018 13:30:29 GMT+00:00 user-agent:ALIYUN-ANDROID-DEMO x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 content-length:33 username=user_example&password=123456789
```

Correct string to sign:

```
POST application/json; charset=utf-8 application/x-www-form-urlencoded; charset=utf-8 Wed, 09 May 2018 13:30:29 GMT+00:00 x-ca-key:203753385 x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 x-ca-signature-method:HmacSHA256 x-ca-timestamp:1525872629832 /http2test/test?param1=test&password=123456789&username=user_example
```

**Signature calculation process**

After the client extracts the key data from the HTTP request and assembles the string to sign, the client must encrypt and encode the string to create the final signature. The encryption is performed as follows. `stringToSign` is the extracted string to sign, `secret` is the secret specified in the plugin configuration, and `sign` is the final generated signature. de OpenTrek

```
Mac hmacSha256 = Mac.getInstance("HmacSHA256"); byte[] secretBytes = secret.getBytes("UTF-8"); hmacSha256.init(new SecretKeySpec(secretBytes, 0, secretBytes.length, "HmacSHA256")); byte[] result = hmacSha256.doFinal(stringToSign.getBytes("UTF-8")); String sign = Base64.encodeBase64String(result);
```

The `stringToSign` is encoded into a byte array using UTF-8. The byte array is then encrypted. Finally, the encrypted array is encoded using Base64 to create the final signature.

**Process for adding the signature**

The client must include the following four headers in the HTTP request that is sent to the cloud-native API gateway for signature verification. x-ca-key: The App Key. Required. x-ca-signature-method: The signature algorithm. The value can be `HmacSHA256` or `HmacSHA1`. Optional. The default value is `HmacSHA256`. x-ca-signature-headers: A comma-separated collection of all signed header keys. Optional. x-ca-signature: The signature. Required. The following is an example of a complete HTTP request with a signature.

```
POST /http2test/test?param1=test HTTP/1.1 host:api.aliyun.com accept:application/json; charset=utf-8 ca_version:1 content-type:application/x-www-form-urlencoded; charset=utf-8 x-ca-timestamp:1525872629832 date:Wed, 09 May 2018 13:30:29 GMT+00:00 user-agent:ALIYUN-ANDROID-DEMO x-ca-nonce:c9f15cbf-f4ac-4a6c-b54d-f51abf4b5b44 x-ca-key:203753385 x-ca-signature-method:HmacSHA256 x-ca-signature-headers:x-ca-timestamp,x-ca-key,x-ca-nonce,x-ca-signature-method x-ca-signature:xfX+bZxY2yl7EB/qdoDy9v/uscw3Nnj1pgoU+Bm6xdM= content-length:33 username=user_example&password=123456789
```

**How the server verifies a signature**

**Process overview**

The server verifies the client signature in four steps:
1. Extracts key data from the received request to obtain a string to sign.
2. Reads the `key` from the received request and uses the `key` to query the corresponding

```
 secret .
```

3. Uses an encryption algorithm and the `secret` to encrypt the string to sign and obtain the
signature.
4. Reads the client signature from the received request and compares it with the server-side
signature for consistency.

**Troubleshooting signature errors**

| HTTP status code | Error message | Description |
|---|---|---|
| 400 | Invalid Signature. | The signature string in the `x-ca-signature` request header does not match the signature calculated by the server. |
| 400 | Invalid Content-MD5. | The `content-md5` request header is incorrect. |
| 400 | Invalid Date. | The time offset calculated from the `date` request header exceeds the configured `date offset`. _ |
| 401 | Invalid Key. | The `x-ca-key` is not provided in the request header, or the `x-ca-key` is invalid. |
| 401 | Empty Signature. | The `x-ca-signature` string is not provided in the request header. |
| 403 | Unauthorized Consumer. | The request caller does not have access permissions. |
| 413 | Request Body Too Large. | The request body exceeds the size limit of 32 MB. |
| 413 | Payload Too Large. | The request body exceeds the global `DownstreamConnectionBufferLimits` configuration. You can increase this value on the parameter settings page. |

OpenTrek de If gateway signature verification fails, the server-side string to sign (StringToSign) is returned to the client in the `X-Ca-Error-Message` HTTP response header. To identify the problem, compare your locally calculated StringToSign with the one returned by the server. If the server-side and client-side StringToSign values are identical, check whether the App Secret used for signature calculation is correct. Because line breaks cannot be represented in an HTTP header, the line feed characters in the StringToSign are replaced with # , as shown in the following example.

```
X-Ca-Error-Message: Server StringToSign:`GET#application/json##application/json##X-Ca- Key:200000#X-Ca-Timestamp:1589458000000#/app/v1/config/keys?keys=TEST`
```

**Related error codes**

|  | Name |  | Data type |  | Req uire d | Defau lt value | Description |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | http service _ |  | object |  | Yes | - | Configuration for the external authorization service. |  |  |
|  | match type _ |  | string |  | No |  | Valid values are whitelist and blacklist . |  |  |
|  | match list _ |  | array of MatchRule |  | No |  | A list that contains ( match rule domain , _ _ match rule path , match rule type ). _ _ _ _ |  |  |
|  | failure mode _ _ allow |  | bool |  | No | false | If set to true, client requests are accepted even if communication with the authorization service fails or the service returns an HTTP 5xx error. |  |  |
|  | failure mode _ _ |  |  |  |  |  | If both failure mode allow and _ _ failure mode allow header add are set _ _ _ _ to true, the x-envoy-auth-failure-mode- allowed: true header is added to the request if communication with the authorization service fails or the service returns an HTTP 5xx error. |  |  |
|  |  | failure mode _ _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | x-envoy-auth-failure-mode- |  |
|  | allow header ad _ _ |  |  |  |  |  |  |  |  |
|  |  |  |  | ol | No | false | allowed: true |  |  |
|  | d |  |  |  |  |  |  |  |  |
|  | status on err _ _ or |  | int |  | No | 403 | The HTTP status code returned to the client when the authorization service is inaccessible or returns a 5xx status code. The default status code is 403 . |  |  |

|  |  | http service _ |
|---|---|---|

|  |  | failure mode _ _ | boo |
|---|---|---|---|
|  | allow |  |  |

|  |  | status on err _ _ |  |
|---|---|---|---|
|  | or |  |  |

de OpenTrek

**Note**

Increase the `DownstreamConnectionBufferLimits` value with caution. A higher value for this parameter significantly increases the memory usage of the gateway.

##### External authentication

The ext-auth plugin sends authentication requests to an external authorization service to verify client request authorization. This topic describes how to configure the ext-auth plugin.

**Runtime properties**

This plugin runs during the authentication phase with an execution priority of `360` .

**Configuration fields**

The following table describes the configuration fields for each item in `http_service` .

|  |  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|---|
|  |  | endpoint mode _ |  | string | No | envoy | Valid values are envoy and forward auth _ . |
|  |  |  | endpoint mode _ |  |  |  |  |
|  |  | endpoint |  | object | Yes | - | Information about the HTTP service to which authentication requests are sent. |
|  |  | timeout |  | int | No | 1000 | The connection timeout for the ext-auth service, in milliseconds. |
|  |  | authorization _ request |  | object | No | - | Configuration for sending authentication requests. |
|  |  |  | authorization _ | object |  |  |  |
|  |  | request |  |  |  |  |  |
|  |  | authorization _ response |  | object | No | - | Configuration for processing authentication responses. |
|  |  |  | authorization _ | object |  |  |  |
|  |  | response |  |  |  |  |  |

|  |  | envoy |
|---|---|---|
|  |  | forward auth _ |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de The following table describes the configuration fields for each item in `endpoint` .

|  | service name _ |  | string | Yes |  | - |  |  | The name of the authorization service. Enter the full FQDN with the service type, such as ext- auth.dns or ext-auth.my- |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  | ext- |  |  |
|  |  |  |  |  |  |  |  |  | auth.dns |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | or |  |
|  |  |  |  |  |  |  |  |  | ns.svc.cluster. |  |  |  |  |
|  |  |  |  |  |  |  |  |  | local |  |  |  |  |
|  | service port _ |  | int | No |  | 80 |  |  | The service port of the authorization service. |  |  |  |  |
|  | service host _ |  | string | No |  | - |  |  | The Host header set when requesting the authorization service. If you leave this empty, the value is the same as the FQDN. |  |  |  |  |
|  | path prefix _ |  | string | Required if endpoint mode _ is set to envoy . |  | - |  |  | The prefix of the request path that the client uses to send requests to the authorization service. This is used when endpoint mode _ is set to envoy . |  |  |  |  |
|  | request method _ |  | string | No |  | GET |  |  | The HTTP method that the client uses to send requests to the authorization service. This is used when endpoint mode _ is set to forward auth _ . |  |  |  |  |
|  |  | request method _ |  |  |  |  |  |  |  |  |  |  |  |

|  |  | service name _ |
|---|---|---|

|  |  | service port _ |
|---|---|---|

|  |  | service host _ |
|---|---|---|

|  |  | endpoint mode _ |
|---|---|---|
| g |  |  |

|  |  | endpoint mode _ |
|---|---|---|

|  |  |  | endpoint mode _ |
|---|---|---|---|

de OpenTrek

| path | string |  |  | Required if endpoint mode _ |  | - | The request path that the client uses to send requests to the authorization service. This is used when endpoint mode _ is set to forward auth _ . |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  | endpoint mode _ |  |  |
|  |  | g |  |  |  |  |  |

|  |  |  | endpoint mode _ |
|---|---|---|---|

|  | Name | Data type | Required | Default value | Description |  |
|---|---|---|---|---|---|---|
|  | allowed header _ s | array of StringMatcher | No | - | After you set this field, the client request headers that match are added to the authorization service request. In addition to user-defined header matching rules, the Authorization HTTP header is automatically included in the authorization service request. If endpoint mode _ is set to forward auth _ , X- Forwarded-* request headers are added. |  |
|  | s |  |  |  |  |  |

|  |  |  |  | endpoint mode _ |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | , |  |

OpenTrek de The following table describes the configuration fields for each item in

```
 authorization_request .
```

|  | headers to add _ _ |  | map[string]string | No | - |  | A list of request headers to include in the authorization service request. Important Client request headers with the same name are overwritten. |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | headers to add _ _ |  |  |  |  |  |  |  |  |  |
|  | with request b _ _ ody |  | bool | No | false |  | Buffers the client request body and sends it in the authentication request. This does not take effect for GET, OPTIONS, or HEAD requests. |  |  |  |  |
|  |  | with request b _ _ | bo |  |  |  |  |  |  |  |  |
|  | ody |  |  |  |  |  |  |  |  |  |  |
|  | max request bo _ _ dy bytes _ |  | int | No | 10 MB |  | The maximum size of the client request body to hold in memory. If the client request body reaches the size set in this field, an HTTP 413 status code is returned and the authorization procedure does not start. Important This setting takes precedence over the failure m _ ode allow _ configuratio n. |  |  |  |  |
|  |  | max request bo _ _ | int |  |  |  |  |  |  |  |  |
|  | dy bytes _ |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | failure m _ |  |  |
|  |  |  |  |  |  |  |  | ode allow _ |  |  |  |

de OpenTrek

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | allowed upstre _ am headers _ |  | array of StringMatcher | No | - | Response headers from the authentication request that match are added to the original client request headers. Note that request headers with the same name are overwritten. |
|  |  | allowed upstre _ | array of |  |  |  |
|  | am headers _ |  |  |  |  |  |
|  | allowed client _ headers _ |  | array of StringMatcher | No | - | If this is not set, all response headers from the authentication request are added to the client's response headers when the request is denied. If this is set, only the matching response headers from the authentication request are added to the client's response headers when the request is denied. |
|  |  | allowed client _ | array of |  |  |  |
|  | headers _ |  |  |  |  |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| exact | string | No. Select one from exact , prefix , suffix , contains , and regex . | - | Exact match. |

|  | exact |
|---|---|
| prefix |  |
| suffix |  |

OpenTrek de The following table describes the configuration fields for each item in

```
 authorization_response .
```

The following table describes the configuration fields for the `StringMatcher` type. When you use an `array of StringMatcher` , the items are processed in the order they are defined in the array.

| prefix | string | No. Select one from exact , prefix , suffix , contains , and regex . | - | Prefix match. |
|---|---|---|---|---|
| suffix | string | No. Select one from exact , prefix , suffix , contains , and regex . | - | Suffix match. |
| contains | string | No. Select one from exact , prefix , suffix , contains , and regex . | - | It is included. |
| regex | string | No. Select one from exact , prefix , suffix , contains , and regex . | - | Regular expression match. |

|  | exact |
|---|---|
| prefix |  |
| suffix |  |

|  | exact |
|---|---|
| prefix |  |
| suffix |  |

|  | exact |
|---|---|
| prefix |  |
| suffix |  |

|  | exact |
|---|---|
| prefix |  |
| suffix |  |

|  | Name |  | Data type | Required | Default value | Description |
|---|---|---|---|---|---|---|
|  | match rule dom _ _ ain |  | string | No | - | The domain name for the matching rule. Wildcard patterns are supported, such as *.bar.com . |
|  |  | match rule dom _ _ | str |  |  |  |
|  | ain |  |  |  |  |  |
|  | match rule met _ _ hod |  | []string | No | - | The request methods to match. |
|  |  | match rule met _ _ | []s |  |  |  |
|  | hod |  |  |  |  |  |
|  | match rule pat _ _ h |  | string | No | - | The rule for matching the request path. |
|  |  | match rule pat _ _ |  |  |  |  |
|  | h |  |  |  |  |  |

de OpenTrek The following table describes the configuration fields for the MatchRule type. When you use an `array of MatchRule` , the items are processed in the order they are defined in the array.

|  | match rule typ _ _ |  | string | No | - | The type of rule for matching the request path. Valid values are exact , prefix , suffix , contains , and regex . |
|---|---|---|---|---|---|---|
|  |  | match rule typ _ _ |  |  |  |  |
|  | e |  |  |  |  |  |

| envoy |  | , the authe |
|---|---|---|
| red |  |  |

| endpoint mode _ |  | is set |
|---|---|---|
| ured |  |  |

| Header | Description |
|---|---|
| x-forwarded-proto | The scheme of the original request, such as http or https. |
| x-forwarded-method | The method of the original request, such as GET, POST, DELETE, or PATCH. |
| x-forwarded-host | The host of the original request. |
| x-forwarded-uri | The path of the original request, including path parameters, such as /v1/app?test=true . |

| such as | *.bar.com |  |  | , are sup |
|---|---|---|---|---|
| exact |  |  |  | suffix |
|  | , | prefix | , |  |

OpenTrek de

**Differences between the two endpoint_mode values**

service:

**Whitelist and blacklist modes**

You can configure a whitelist or a blacklist. By default, the plugin uses whitelist mode with an

**Whitelist mode**

| sume the | ext-auth |  |  | servi |
|---|---|---|---|---|
| ext-auth |  |  |  |  |
|  |  | , port is |  |  |

de OpenTrek

```bash
# Whitelist mode configuration. Requests that match the whitelist rules do
not require authentication. match_type: 'whitelist' match_list:
 # All requests with the domain api.example.com and a path prefix of /public
do not require authentication.
 - match_rule_domain: 'api.example.com'
   match_rule_path: '/public'
   match_rule_type: 'prefix'
 # For the image resource server images.example.com, all GET requests do not
require authentication.
 - match_rule_domain: 'images.example.com'
   match_rule_method: ["GET"]
 # For all domains, HEAD requests with an exact path match of /health-check d
o not require authentication.
 - match_rule_method: ["HEAD"]
   match_rule_path: '/health-check'
   match_rule_type: 'exact'
```

**Blacklist mode**

```bash
# Blacklist mode configuration. Requests that match the blacklist rules
require authentication. match_type: 'blacklist' match_list:
 # All requests with the domain admin.example.com and a path prefix of /sensi
tive require authentication.
 - match_rule_domain: 'admin.example.com'
   match_rule_path: '/sensitive'
   match_rule_type: 'prefix'
 # For all domains, DELETE requests with an exact path match of /user require
authentication.
 - match_rule_method: ["DELETE"]
   match_rule_path: '/user'
   match_rule_type: 'exact'
 # All POST requests with the domain legacy.example.com require
authentication.
 - match_rule_domain: 'legacy.example.com'
   match_rule_method: ["POST"]
```

**Configuration examples**

**When endpoint_mode is envoy**

**Example 1**

Configuration for the `ext-auth` plugin: OpenTrek de

```
http_service:
  endpoint_mode: envoy
  endpoint:
    service_name: ext-auth.backend.svc.cluster.local
    service_port: 8090
    path_prefix: /auth
  timeout: 1000
```

After you enable the `ext-auth` plugin, you can send the following request to the gateway:

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

**Successful request to the** `ext-auth` **service:**
The `ext-auth` service receives the following authentication request:

```
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1 Host: ext-auth.backend.svc.cluster.local Authorization: xxx Content-Length: 0
```

**Failed request to the** `ext-auth` **service:**
If the `ext-auth` service returns a 5xx response, the client receives an HTTP 403 status code and all response headers from the `ext-auth` service. If the `ext-auth` service returns the `x-auth-version: 1.0` and `x-auth-failed: true` response headers, they are forwarded to the client.

```
HTTP/1.1 403 Forbidden x-auth-version: 1.0 x-auth-failed: true date: Tue, 16 Jul 2024 00:19:41 GMT server: istio-envoy content-length: 0
```

If the `ext-auth` service is inaccessible or returns a 5xx status code, the client request is denied with the status code configured in `status_on_error` . If the `ext-auth` service returns any other HTTP status code, the client request is denied with that status code. If `allowed_client_headers` is configured, the matching response headers are added to the client's response.

**Example 2**

Configuration for the `ext-auth` plugin: de OpenTrek

```
http_service:
  authorization_request:
    allowed_headers:
    - exact: x-auth-version
    headers_to_add:
      x-envoy-header: true
  authorization_response:
    allowed_upstream_headers:
    - exact: x-user-id
    - exact: x-auth-version
  endpoint_mode: envoy
  endpoint:
    service_name: ext-auth.backend.svc.cluster.local
    service_host: my-domain.local
    service_port: 8090
    path_prefix: /auth
  timeout: 1000
```

After you enable the `ext-auth` plugin, you can send the following request to the gateway:

```bash
curl -X POST http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx"
```

The `ext-auth` service receives the following authentication request:

```
POST /auth/users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 HTTP/1.1 Host: my-domain.local Authorization: xxx X-Auth-Version: 1.0 x-envoy-header: true Content-Length: 0
```

If the response from the `ext-auth` service includes the `x-user-id` and `x-auth-version` headers, the gateway adds these two headers to the request sent to the upstream service.

**When endpoint_mode is forward_auth**

**Example 1**

Configuration for the `ext-auth` plugin:

```
http_service:
  endpoint_mode: forward_auth
  endpoint:
    service_name: ext-auth.backend.svc.cluster.local
    service_port: 8090
    path: /auth
    request_method: POST
  timeout: 1000
```

After you enable the `ext-auth` plugin, you can send the following request to the gateway: OpenTrek de

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "Host: foo.bar.com"
```

**Successful request to the** `ext-auth` **service:**
The `ext-auth` service receives the following authentication request:

```
POST /auth HTTP/1.1 Host: ext-auth.backend.svc.cluster.local Authorization: xxx X-Forwarded-Proto: HTTP X-Forwarded-Host: foo.bar.com X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 X-Forwarded-Method: GET Content-Length: 0
```

**Failed request to the** `ext-auth` **service:**
If the `ext-auth` service returns a 5xx response, the client receives an HTTP 403 status code and all response headers from the `ext-auth` service. If the `ext-auth` service returns the `x-auth-version: 1.0` and `x-auth-failed: true` response headers, they are forwarded to the client.

```
HTTP/1.1 403 Forbidden x-auth-version: 1.0 x-auth-failed: true date: Tue, 16 Jul 2024 00:19:41 GMT server: istio-envoy content-length: 0
```

If the `ext-auth` service is inaccessible or returns a 5xx status code, the client request is denied with the status code configured in `status_on_error` . If the `ext-auth` service returns any other HTTP status code, the client request is denied with that status code. If `allowed_client_headers` is configured, the matching response headers are added to the client's response.

**Example 2**

Configuration for the `ext-auth` plugin: de OpenTrek

```
http_service:
  authorization_request:
    allowed_headers:
    - exact: x-auth-version
    headers_to_add:
      x-envoy-header: true
  authorization_response:
    allowed_upstream_headers:
    - exact: x-user-id
    - exact: x-auth-version
  endpoint_mode: forward_auth
  endpoint:
    service_name: ext-auth.backend.svc.cluster.local
    service_host: my-domain.local
    service_port: 8090
    path: /auth
    request_method: POST
  timeout: 1000
```

After enabling the `ext-auth` plugin, send the following request to the gateway:

```bash
curl -i http://localhost:8082/users?apikey=9a342114-ba8a-11ec-b1bf- 00163e1250b5 -X GET -H "foo: bar" -H "Authorization: xxx" -H "X-Auth-Version: 1.0" -H "Host: foo.bar.com"
```

The `ext-auth` service receives the following authentication request:

```
POST /auth HTTP/1.1 Host: my-domain.local Authorization: xxx X-Forwarded-Proto: HTTP X-Forwarded-Host: foo.bar.com X-Forwarded-Uri: /users?apikey=9a342114-ba8a-11ec-b1bf-00163e1250b5 X-Forwarded-Method: GET X-Auth-Version: 1.0 x-envoy-header: true Content-Length: 0
```

If the response from the `ext-auth` service includes the `x-user-id` and `x-auth-version` headers, the gateway adds these headers to the upstream request.

##### OAuth2 authentication

The OAuth2 plugin issues OAuth2 access tokens based on JSON Web Tokens (JWT) that conform to the RFC9068 specification. This topic describes how to configure the OAuth2 plugin.

**Plugin type**

Authentication and authorization.

**Plugin configuration**

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| consumers | array of object | Required | - | Configures service callers to authenticate requests. |
| issuer | string | Optional | Higress - Gatewa y | Fills the issuer field in the JWT. |
| auth path _ | string | Optional | /oauth2 /token | Specifies the path suffix used to issue tokens. For route-level configurations, ensure the corresponding route is matched first. When using API management, you must create an API with the same path. |
| global crede _ ntials | bool | Optional | true | Allows access with credentials issued by any route, provided the consumer is authenticated. |
| auth header _ _ name | string | Optional | Authori zation | Specifies the request header from which to get the JWT. |
| token ttl _ | number | Optional | 7200 | The validity period of a token after it is issued. Unit: seconds. |
| clock skew s _ _ econds | number | Optional | 60 | The allowed clock skew when verifying the exp and iat fields of a JWT. Unit: seconds. |
| keep token _ | bool | Optional | true | Specifies whether to keep the JWT when forwarding the request to the backend. |

OpenTrek de

**Configuration fields**

| global auth _ | array of string | Optional. This setting applies to instance-level configurations only. | - | Can only be configured at the instance level. If set to true, the authentication mechanism is enabled globally. If set to false, the authentication mechanism is enabled only for configured domain names and routes. If not configured, the mechanism is enabled globally only when no domain name or route configurations exist. This is for compatibility with previous customer usage patterns. |
|---|---|---|---|---|

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|
| name | string | Required | - | The name of the consumer. |
| client id _ | string | Required | - | The OAuth2 client ID. |
| client secret _ | string | Required | - | The OAuth2 client secret. |

| Important If this plugin is enabled for a route, requests with a path suffix that matches auth path are not forwarded to the backend service. Instead, they are used to _ generate a token. If you disable global credentials , ensure that the plugin is not enabled on a _ route that uses an exact path match. This is because unexpected behavior may occur if a route that uses a prefix path match also exists. For requests that pass authentication and authorization, the gateway adds the X- Mse-Consumer request header, which contains the name of the consumer. |  |  |
|---|---|---|
|  | X- |  |

| Name | Data type | Required | Defaul t value | Description |
|---|---|---|---|---|

de OpenTrek The following table describes the configuration fields for each item in `consumers` .

**Authorization configuration (optional)**

| allow | array of string | Optional non- instance-level configuration | - | Can only be configured on fine- grained rules such as routes or domain names. For requests that meet the matching conditions, configure the allowed consumers to implement fine-grained access control. |
|---|---|---|---|---|

OpenTrek de

**Important**

Authentication and authorization cannot be configured in the same rule.

**Configuration examples**

**Configure authentication at the route granularity**

Apply the following plugin configuration to the `route-a` and `route-b` routes:

```
consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Although the same configuration is used, credentials issued for `route-a` cannot be used to access `route-b` , and vice versa. To share credentials across routes that use the same configuration, use the following configuration:

```
global_credentials: true consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**Configure global authentication and route-level authorization**

The following configuration enables JWT authentication and authorization for a specific gateway route or domain name. Note that if a JWT matches multiple `jwks` , the first matching `consumer` is hit based on the configuration order. Apply the following plugin configuration at the instance level:

```
global_auth: false consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

de OpenTrek Apply the following plugin configuration to `route-a` and `route-b` :

```
allow:
- consumer1
```

Apply the following plugin configuration to `*.example.com` and `test.com` :

```
allow:
- consumer2
```

**Note**

In this example, `route-a` and `route-b` are the names of the gateway routes. If a request matches these routes, callers whose `name` is `consumer1` are granted access. All other callers are denied access. In this example, `*.example.com` and `test.com` are used to match the domain name of a request. If a match is found, callers whose `name` is `consumer2` are granted access. All other callers are denied access.

**Enable at the gateway instance level**

The following configuration enables OAuth2 authentication for the entire gateway instance. All incoming requests must be authenticated.

```
global_auth: true consumers:
- name: consumer1
  client_id: 12345678-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: consumer2
  client_id: 87654321-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  client_secret: hgfedcba-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**Request examples**

**Use the Client Credentials grant type**

**Get an access token**

| HTTP status code | Error message | Cause |
|---|---|---|
| 401 | Invalid Jwt token. | The JWT is not provided in the request header, the JWT format is incorrect, or the JWT has expired. |
| 403 | Access Denied. | Permission to access the current route is denied. |

OpenTrek de

```json
# Get the token using the GET method (recommended)
curl 'http://test.com/oauth2/token?grant_type=client_credentials&client_id=12345678-xxx x-xxxx-xxxx-xxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
# Get the token using the POST method (A route with a real destination service must be
matched first. Otherwise, the gateway does not read the request body.) curl 'http://test.com/oauth2/token' -H 'content-type: application/x-www-form-urlencoded ' -d 'grant_type=client_credentials&client_id=12345678-xxxx-xxxx-xxxxxxxxxxxxxxxx&client_secret=abcdefgh-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
# Get the access_token field from the response:
{
  "token_type": "bearer",
  "access_token":
"eyJh************.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW50X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHg Hh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiOjE2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZX eSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0ODEwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9. T_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0",
  "expires_in": 7200
}
```

**Make a request with an access token**

```bash
curl 'http://test.com' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6ImFwcGxpY2F0aW9uXC9hdCtqd3QifQ.eyJhdWQiOiJkZWZhdWx0IiwiY2xpZW X2lkIjoiMTIzNDU2NzgteHh4eC14eHh4LXh4eHgteHh4eHh4eHh4eHh4IiwiZXhwIjoxNjg3OTUxNDYzLCJpYXQiO 2ODc5NDQyNjMsImlzcyI6IkhpZ3Jlc3MtR2F0ZXdheSIsImp0aSI6IjEwOTU5ZDFiLThkNjEtNGRlYy1iZWE3LTk0 EwMzc1YjYzYyIsInN1YiI6ImNvbnN1bWVyMSJ9.NkT_rG3DcV9543vBQgneVqoGfIhVeOuUBwLJJ4Wycb0'
```

**Related error codes**

##### OPA policies

The OPA plugin enforces `OPA` policies. This topic describes how to configure the OPA plugin.

**Runtime properties**

Plugin execution phase: `Authentication phase` . Plugin execution priority: `225` .

**Configuration fields**

| Field | Data type | Require d | Defaul t value | Description |
|---|---|---|---|---|
| policy | string | Required | - | The OPA policy. |
| timeout | string | Required | - | The access timeout period. |
| serviceSource | string | Required | - | k8s, Nacos, IP, route. |
| host | string | Optional | - | Service host (required if serviceSource is ip ). |
| serviceName | string | Optional | - | The service name. This parameter is required if `serviceSource` is set to one of the following values: k8s,nacos,ip . |
| servicePort | string | Optional | - | Service port (Required if `serviceSource` is k8s, nacos, or ip ). |
| namespace | string | Optional | - | The service port. This parameter is required if `serviceSource` is k8s,nacos . |

de OpenTrek

**Configuration example**

```
serviceSource: k8s serviceName: opa servicePort: 8181 namespace: higress-backend policy: example1 timeout: 5s
```

**OPA service installation reference**

**Start the OPA service**

```bash
docker run -d --name opa -p 8181:8181 openpolicyagent/opa:0.35.0 run -s
```

**Create an OPA policy**

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de

```java
curl -X PUT '127.0.0.1:8181/v1/policies/example1' \
 -H 'Content-Type: text/plain' \
 -d 'package example1
import input.request default allow = false allow {
 # HTTP method must GET
 request.method == "GET"
}'
```

**Query the policy**

```bash
curl -X POST '127.0.0.1:8181/v1/data/example1/allow' \
 -H 'Content-Type: application/json' \
 -d '{"input":{"request":{"method":"GET"}}}'
```

#### Security

##### Cross-origin resource sharing

**Description**

The `cors` plugin enables Cross-Origin Resource Sharing (CORS) by adding the required HTTP response headers.

**Configuration fields**

| allow origins _ | array of string | Optional | * | Specifies the origins that can access the resource. The format is `scheme://host:p ort`, such as http://example.co m:8081. If `allow credential _ s` is `false`, you can use `*` to allow all origins. |
|---|---|---|---|---|
| allow origin patt _ _ erns | array of string | Optional | - | Specifies the origin patterns that can access the resource. Use `*` as a wildcard for domain names or ports. For example: `http://*.example .com` matches a subdomain. `http://*.example .com: [8080,9090]` matches a subdomain and specified ports. `http://*.example .com:[*]` matches a subdomain and all ports. A standalone `*` matches all domain names and ports. |
| allow methods _ | array of string | Optional | GET, PUT, POST, DELETE, PATCH, OPTIONS | Specifies the methods allowed for cross-domain access, such as `GET` and `POST`. Use `*` to allow all methods. |

de OpenTrek

| allow headers _ | array of string | Optional | DNT,X- CustomHeader,K eep-Alive,User- Agent,X- Requested-With, If-Modified- Since,Cache- Control,Content- Type,Authorizatio n | Specifies the non-standard CORS request headers that a requester can include. Use `*` to allow any header. |
|---|---|---|---|---|
| expose headers _ | array of string | Optional | - | Specifies the non-standard CORS response headers that the server can expose. Use `*` to allow any header. |
| allow credentials _ | bool | Optional | false | Specifies whether the requester can include credentials, such as cookies, in cross-domain requests. Per the CORS specification, if this option is `true`, you cannot set `allow origins` to _ `*`. Instead, set `allow origin pat _ _ terns` to `*`. |
| max age _ | number | Optional | 86400 seconds | Specifies the maximum time in seconds that a browser can cache the CORS preflight request result. During this time, the browser reuses the previous check result. |

OpenTrek de

**Configuration examples**

**Allow all cross-domain access without credentials**

de OpenTrek

```
allow_origins:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: false max_age: 7200
```

**Allow all cross-domain access with credentials**

```
allow_origin_patterns:
 - '*'
allow_methods:
 - '*'
allow_headers:
 - '*'
expose_headers:
 - '*'
allow_credentials: true max_age: 7200
```

**Allow cross-domain access from specific subdomains with**

**specific methods, request headers, and credentials**

```
allow_origin_patterns:
 - http://*.example.com
 - http://*.example.org:[8080,9090]
allow_methods:
 - GET
 - PUT
 - POST
allow_headers:
 - Content-Type
expose_headers:
 - '*'
allow_credentials: true max_age: 7200
```

**Testing**

**Test configuration**

```
apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: mcp-cors-httpbin
```

OpenTrek de

```
 namespace: higress-system
spec:
 registries:
 - domain: httpbin.org
 name: httpbin
 port: 80
 type: dns
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/destination: httpbin.dns
 higress.io/upstream-vhost: "httpbin.org"
 higress.io/backend-protocol: HTTP
 name: ingress-cors-httpbin
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - host: httpbin.example.com
 http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: mcp-cors-httpbin
 path: /
 pathType: Prefix
--apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 name: wasm-cors-httpbin
 namespace: higress-system
spec:
 defaultConfigDisable: true
 matchRules:
 - config:
 allow_origins:
 - http://httpbin.example.net
 allow_origin_patterns:
 - http://*.example.com:[*]
 - http://*.example.org:[9090,8080]
 allow_methods:
 - GET
 - POST
 - PATCH
 allow_headers:
 - Content-Type
 expose_headers:
```

de OpenTrek

```
 - X-Custom-Header
 - X-Env-UTM
 allow_credentials: true
 max_age: 3600
 configDisable: false
 ingress:
 - ingress-cors-httpbin
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/cors:1.0.0
 imagePullPolicy: Always
```

**Test requests**

**Simple request**

```bash
curl -v -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 200 OK
> x-cors-version: 1.0.0
> access-control-allow-origin: http://httpbin2.example.org:9090
> access-control-expose-headers: X-Custom-Header,X-Env-UTM
> access-control-allow-credentials: true
```

**Preflight request**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: POST" -H "Access-Control-Reque st-Headers: Content-Type, Token" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 200 OK < x-cors-version: 1.0.0 < access-control-allow-origin: http://httpbin2.example.org:9090 < access-control-allow-methods: GET,POST,PATCH < access-control-allow-headers: Content-Type,Token,Authorization < access-control-expose-headers: X-Custom-Header,X-Env-UTM < access-control-allow-credentials: true < access-control-max-age: 3600 < date: Tue, 23 May 2023 11:41:28 GMT < server: istio-envoy < content-length: 0
```

<

```
* Connection #0 to host 127.0.0.1 left intact
* Closing connection 0
```

**Preflight request with an invalid CORS origin**

OpenTrek de

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: GET" http://127.0.0.1/anything/get\?foo\=1
 HTTP/1.1 403 Forbidden
< content-length: 70 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:27:01 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**Preflight request with an invalid CORS method**

```bash
curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H "Host: httpbin.example.com" -H "Access-Control-Request-Method: DELETE" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 403 Forbidden < content-length: 49 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:28:51 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

**Preflight request with an invalid CORS header**

```bash
 curl -v -X OPTIONS -H "Origin: http://httpbin2.example.org:9090" -H  "Host:
httpbin.example.com" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request -Headers: TokenView" http://127.0.0.1/anything/get\?foo\=1 < HTTP/1.1 403 Forbidden < content-length: 52 < content-type: text/plain < x-cors-version: 1.0.0 < date: Tue, 23 May 2023 11:31:03 GMT < server: istio-envoy
```

<

```
* Connection #0 to host 127.0.0.1 left intact
Invalid CORS request
```

##### IP restriction

| Configuration item | Type | Required | Default value |  | Description |  |  |
|---|---|---|---|---|---|---|---|
| ip source type _ _ | string | No | origin-source |  | Possible values: Peer socket IP address: origin- source . Retrieved from a header: header . |  |  |
|  |  |  |  |  |  | origin- |  |
|  |  |  |  |  | source |  |  |
| ip header name _ _ | string | No | x-forwarded-for |  | Specifies the custom header for the IP source when ip source typ _ _ e is set to header . |  |  |
| allow | array | No | [] |  | The whitelist. |  |  |
| deny | array | No | [] |  | The blacklist. |  |  |
| status | int | No | 403 |  | The HTTP status code for access denied. |  |  |
| message | string | No | Your IP address is blocked. |  | The message returned when access is denied. |  |  |

|  |  | ip source typ _ _ |  |
|---|---|---|---|
|  | e |  |  |

de OpenTrek The ip-restriction plugin restricts access to services or routes by adding IP addresses to a whitelist or a blacklist. It supports restrictions for single IP addresses, multiple IP addresses, and Classless Inter-Domain Routing (CIDR) ranges, such as 10.10.10.0/24. This topic describes how to configure the ip-restriction plugin.

**Running properties**

This plugin runs during the `Authentication phase` and has an execution priority of `210` .

```
ip_source_type: origin-source allow:
 - 10.0.0.1
 - 192.168.0.0/16
```

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| useCRS | bool | Optional | false | Specifies whether to enable the OWASP CRS. For more information, see coreruleset. |
| secRules | array of string | Optional | - | Custom WAF protection rules. For syntax rules, see the ModSecurity Chinese Manual. |

OpenTrek de

```
ip_source_type: header ip_header_name: x-real-iP deny:
 - 10.0.0.1
 - 192.169.X.X/16
```

##### WAF protection

The Web Application Firewall (WAF) plugin implements a protection rule engine based on ModSecurity. It blocks suspicious requests based on configured rules and supports the Open Web Application Security Project (OWASP) Core Rule Set (CRS) to provide basic protection for your site. This topic describes how to configure the WAF plugin.

**Running properties**

Plugin execution phase: `Authorization phase` . Plugin execution priority: `330` .

**Configuration fields**

**Configuration examples**

**Monitor mode**

```
useCRS: true secRules:
 - "SecRuleEngine DetectionOnly"
```

**Remove a specific rule**

For example, if a rule with an ID of 10 causes false positives in monitor mode, you can remove it.

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|

de OpenTrek

```
useCRS: true secRules:
 - "SecRuleRemoveById 10"
 - "SecRuleEngine On"
```

**Custom protection rules**

```
useCRS: true secRules:
 - "SecDebugLogLevel 3"
 - "SecRuleEngine On"
 - "SecAction \"id:100,phase:1,pass\""
 - "SecRule REQUEST_URI \"@streq /admin\" \"id:101,phase:1,t:lowercase,deny\""
 - "SecRule REQUEST_BODY \"@rx maliciouspayload\" \"id:102,phase:2,t:lowercase,deny\""
```

Based on this configuration, the following requests are denied:

```bash
curl http://example.com/admin curl http://example.com -d "maliciouspayload"
```

##### Request blocking

The request-block plugin blocks HTTP requests based on features such as URLs and request headers. Use this plugin to prevent specific site resources from being exposed. This topic describes how to configure the request-block plugin.

**Runtime properties**

Plugin execution phase: `Authentication phase` . Plugin execution priority: `320` .

**Configuration fields**

| block urls _ | array of string | Optional. At least one of block urls , _ block exact u _ _ rls , block regexp _ _ urls , block headers _ , or block bodies _ is required. | - | Specifies the strings to match for URLs that you want to block. |
|---|---|---|---|---|
| block exact urls _ _ | array of string | Optional. At least one of block urls , _ block exact u _ _ rls , block regexp _ _ urls , block headers _ , or block bodies _ is required. | - | Specifies the strings for an exact match of URLs that you want to block. |

|  |  | rls |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | , |  |  |
|  |  | urls |  |  |  |  |
|  |  |  |  |  | , |  |
|  | of string |  |  |  |  |  |

|  |  | rls |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | , |  |  |
|  |  | urls |  |  |  |  |
|  |  |  |  |  | , |  |
| y of string |  |  |  |  |  |  |

OpenTrek de

| block regexp url _ _ s | array of string | Optional. At least one of block urls , _ block exact u _ _ rls , block regexp _ _ urls , block headers _ , or block bodies _ is required. | - | Specifies the regular expressions to match for URLs that you want to block. |
|---|---|---|---|---|
| block headers _ | array of string | Optional. At least one of block urls , _ block exact u _ _ rls , block regexp _ _ urls , block headers _ , or block bodies _ is required. | - | Specifies the strings to match for request headers that you want to block. |
| block bodies _ | array of string | Optional. At least one of block urls , _ block exact u _ _ rls , block regexp _ _ urls , block headers _ , or block bodies _ is required. | - | Specifies the strings to match for request bodies that you want to block. |
| blocked code _ | number | Optional. | 403 | Specifies the HTTP status code to return when a request is blocked. |

|  |  | rls |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | , |  |  |
|  |  | urls |  |  |  |  |
|  |  |  |  |  | , |  |

|  |  | rls |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | , |  |  |
| y of string |  | urls |  |  |  |  |
|  |  |  |  |  | , |  |

|  |  | rls |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | , |  |  |
|  |  |  |  |  |  | - |
|  |  | urls |  |  |  |  |
|  |  |  |  |  | , |  |

de OpenTrek

| blocked message _ | string | Optional. | - | Specifies the HTTP response body to return when a request is blocked. |
|---|---|---|---|---|
| case sensitive _ | bool | Optional. | true | Specifies whether the match is case- sensitive. The default value is true. |

OpenTrek de

**Configuration examples**

**Block request URL paths**

```
block_urls:
- swagger.html
- foo=bar
case_sensitive: false
```

With this configuration, the following requests are blocked:

```bash
curl http://example.com?foo=Bar curl http://exmaple.com/Swagger.html
```

**Block request URL paths with an exact match**

```
block_exact_urls:
- /swagger.html?foo=bar
case_sensitive: false
```

With this configuration, the following request is blocked:

```bash
curl http://example.com/Swagger.html?foo=Bar
```

**Block request URL paths with a regular expression match**

```
block_exact_urls:
- .*swagger.*
case_sensitive: false
```

With this configuration, the following request is blocked:

```bash
curl http://example.com/Swagger.html?foo=Bar
```

| block headers _ | entries, the request is not |
|---|---|
| global |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| allow | array of string | Optional | - | A regular expression that matches the User-Agent request header. A request is allowed if it matches the expression. |

de OpenTrek

**Block request headers**

```
block_headers:
- example-key
- example-value
```

With this configuration, the following requests are blocked:

```bash
curl http://example.com -H 'example-key: 123' curl http://example.com -H 'my-header: example-value'
```

**Block request bodies**

```
block_bodies:
- "hello world"
case_sensitive: false
```

With this configuration, the following requests are blocked:

```bash
curl http://example.com -d 'Hello World' curl http://example.com -d 'hello world'
```

**Request body size limit**

When `block_bodies` is configured, matching applies only to request bodies smaller than 32 MB. If a request body exceeds this limit and there are no matching `block_urls` or

##### Bot detection

The bot-detect plugin detects and blocks Internet crawlers from accessing your site resources. This topic describes how to configure the bot-detect plugin.

**Runtime properties**

This plugin runs during the `Authorization phase` with an execution priority of `310` .

**Configuration fields**

| deny | array of string | Optional | - | A regular expression that matches the User-Agent request header. A request is blocked if it matches the expression. |
|---|---|---|---|---|
| blocked code _ | number | Optional | 403 | The HTTP status code to return when a request is blocked. |
| blocked message _ | string | Optional | - | The HTTP response body to return when a request is blocked. |

| allow |  | and | deny |
|---|---|---|---|

OpenTrek de default logic. You can use the `deny` field to add custom bot detection rules. The default collection of regular expressions for bot detection is as follows:

```bash
# Bots General matcher 'name/0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]
craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50}))[/ ](\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots General matcher 'name 0.0'
 (?:\/[A-Za-z0-9\.]+|) {0,5}([A-Za-z0-9 \-_\!\[\]:]{0,50}(?:[Aa]rchiver|[Ii]ndexer|[Ss]
craper|[Bb]ot|[Ss]pider|[Cc]rawl[a-z]{0,50})) (\d+)(?:\.(\d+)(?:\.(\d+)|)|)
# Bots containing spider|scrape|bot(but not CUBOT)|Crawl
 ((?:[A-z0-9]{1,50}|[A-z\-]{1,50} ?|)(?: the |)(?:[Ss][Pp][Ii][Dd][Ee][Rr]|[Ss]crape|[C
c][Rr][Aa][Ww][Ll])[A-z0-9]{0,50})(?:(?:[ /]| v)(\d+)(?:\.(\d+)|)(?:\.(\d+)|)|)
# Bots Pattern '/name-0.0'
 /((?:Ant-)?Nutch|[A-z]+[Bb]ot|[A-z]+
[Ss]pider|Axtaris|fetchurl|Isara|ShopSalad|Tailsweep)[ \-](\d+)(?:\.(\d+)(?:\.(\d+))?)?
# Bots Pattern 'name/0.0'
\b(008|Altresium|Argus|BaiduMobaider|BoardReader|DNSGroup|DataparkSearch|EDI|Goodzer|Grub NGRID|Infohelfer|LinkedInBot|LOOQ|Nutch|OgScrper|PathDefender|Peew|PostPost|Steeler|Twitt bot|VSE|WebCrunch|WebZIP|Y!J-BR[A-Z]|YahooSeeker|envolk|sproose|wminer)/(\d+)(?:\.(\d+)
|)(?:\.(\d+)|)
# More bots
 (CSimpleSpider|Cityreview Robot|CrawlDaddy|CrawlFire|Finderbots|Index crawler|Job Robo
ter|KiwiStatus Spider|Lijit Crawler|QuerySeekerSpider|ScollSpider|
```

**Configuration examples**

**Permit requests that match bot rules**

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|

de OpenTrek

```
allow:
- ".*Go-http-client.*"
```

If you do not add this configuration, requests from the default Golang network library are identified as bots and blocked.

```
deny:
- "spd-tools.*"
```

With this configuration, the following requests are blocked:

```bash
curl http://example.com -H 'User-Agent: spd-tools/1.1' curl http://exmaple.com -H 'User-Agent: spd-tools'
```

#### Traffic

##### Key-based cluster rate limiting

The cluster-key-rate-limit plugin uses Redis to implement cluster rate limiting and is suitable for scenarios that require globally consistent rate limiting across multiple AI Gateway instances. This topic describes how to configure the cluster-key-rate-limit plugin.

**Features**

The `cluster-key-rate-limit` plugin uses Redis to implement **cluster-level rate limiting** and is suitable for scenarios that require **globally consistent rate limiting** across multiple AI Gateway instances. Two throttling modes are supported:
**Global rule-level rate limiting**: Sets a global rate limit threshold for a custom rule group
based on shared `rule_name` and `global_threshold` configurations.
**Dynamic key-level rate limiting**: Groups and rate-limits requests based on a dynamic
key from the request, such as a URL parameter, request header, client IP, consumer name, or cookie field.

**Runtime properties**

Execution phase: `Default phase` . Execution priority: `20` .

**Configuration parameters**

| rule name _ | string | Yes | - |  |  | The name of the rate limiting rule. The Redis key is assembled using the rule name, throttling type, rate limiting key name, and the actual value of the rate limiting key. |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| global threshold _ | Object | No. You must specify either global thresh _ old or rule items . _ | - |  |  | Applies rate limiting to the entire custom rule group. |  |  |  |
| rule items _ | array of object | No. You must specify either global thresh _ old or rule items . _ | - |  |  | An array of rate limiting rule items. The items are matched in order. When the first matching rule item is hit, rate limiting is triggered, and subsequent rules are not executed. |  |  |  |
| show limit quota _ _ header _ | bool | No | false |  |  | Specifies whether to show the X- |  |  |  |
|  |  |  |  |  |  |  |  | X- |  |
|  |  |  |  |  |  | RateLimit- |  |  |  |
|  |  |  |  |  |  | Limit |  |  |  |
|  |  |  |  |  |  |  | X-RateLimit- |  |  |
|  |  |  |  |  |  | Remaining |  |  |  |
| rejected code _ | int | No | 429 |  |  | The HTTP status code returned when a request is rate-limited. |  |  |  |

|  |  | global thresh _ | - |
|---|---|---|---|
|  | old |  |  |

|  |  | global thresh _ | - |
|---|---|---|---|
|  | old |  |  |

OpenTrek de

| rejected msg _ | string | No | Too many requests | The response body returned when a request is rate-limited. |
|---|---|---|---|---|
| redis | object | Yes | - | Redis-related configurations. |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| query per secon _ _ d | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per second. |
| query per minut _ _ e | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per minute. |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

de OpenTrek The following table describes the fields in `global_threshold` .

| query per hour _ _ | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per hour. |
|---|---|---|---|---|
| query per day _ _ | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per day. |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| limit by header _ _ | string | No. You must specify one of the limit by * _ _ parameters. | - | The name of the HTTP request header from which to get the rate limiting key value. |
| limit by param _ _ | string | No. You must specify one of the limit by * _ _ parameters. | - | The name of the URL parameter from which to get the rate limiting key value. |

OpenTrek de The following table describes the fields in `rule_items` .

| limit by consume _ _ r | string | No. You must specify one of the limit by * _ _ parameters. | - | Rate-limits based on the consumer name. No actual value needs to be added. |
|---|---|---|---|---|
| limit by cookie _ _ | string | No. You must specify one of the limit by * _ _ parameters. | - | The name of the key in the cookie from which to get the rate limiting key value. |
| limit by per hea _ _ _ der | string | No. You must specify one of the limit by * _ _ parameters. | - | Matches specific HTTP request headers by rule and calculates rate limits for each header separately. Specify the name of the source HTTP request header for the rate limiting key value. When you configure limit keys , _ regular expressions or * are supported. |

de OpenTrek

| limit by per para _ _ _ m | string | No. You must specify one of the limit by * _ _ parameters. | - | Matches specific URL parameters by rule and calculates rate limits for each parameter separately. Specify the name of the source URL parameter for the rate limiting key value. When you configure limit keys , _ regular expressions or * are supported. |
|---|---|---|---|---|
| limit by per cons _ _ _ umer | string | No. You must specify one of the limit by * _ _ parameters. | - | Matches specific consumers by rule and calculates rate limits for each consumer separately. Rate- limits based on the consumer name. No actual value needs to be added. When you configure limit keys , _ regular expressions or * are supported. |
| limit by per cook _ _ _ ie | string | No. You must specify one of the limit by * _ _ parameters. | - | Matches specific cookies by rule and calculates rate limits for each cookie separately. Specify the name of the key in the source cookie for the rate limiting key value. When you configure limit keys , _ regular expressions or * are supported. |

OpenTrek de

| limit by per ip _ _ _ | string | No. You must specify one of the limit by * _ _ parameters. | - |  |  | Matches specific IPs by rule and calculates rate limits for each IP separately. Specify the source IP parameter for the rate limiting key value. To get the IP from a request header, use from- header- followed by the header name. Example: from- |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | from- |  |
|  |  |  |  |  |  | header-x- |  |  |
|  |  |  |  |  |  | forwarded- |  |  |
|  |  |  |  |  |  | for |  |  |
| limit keys _ | array of object | Yes | - |  |  | Configures the rate limit counts after a key value is matched. |  |  |

|  |  | from- |  |
|---|---|---|---|
|  | header- |  |  |

|  |  | from- |  |
|---|---|---|---|
|  | remote-addr |  |  |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|

de OpenTrek The following table describes the fields in `limit_keys` .

| key | string | Yes | - |  | The key value to match. For limit by per _ _ _ header , limit by per _ _ _ param , limit by per _ _ _ consumer , and limit by per _ _ _ cookie types, you can configure a regular expression (prefixed with `regexp:`) or `*` (matches all). Regular expression example: regexp:^d.* (matches all strings starting with 'd'). For limit by per _ _ _ ip , you can configure an IP address or an IP address range. |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | limit by per _ _ _ |  |  |  |  |
|  |  |  |  |  | header |  |  |  |  |  |
|  |  |  |  |  |  |  |  | , |  |  |
|  |  |  |  |  | param |  |  |  |  |  |
|  |  |  |  |  |  |  | , |  |  |  |
|  |  |  |  |  | consumer |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | , and |  |
|  |  |  |  |  | cookie |  |  |  |  |  |
| query per secon _ _ d | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - |  | The number of allowed requests per second. |  |  |  |  |  |
| query per minut _ _ e | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - |  | The number of allowed requests per minute. |  |  |  |  |  |

|  |  | limit by per _ _ _ |  |
|---|---|---|---|
|  | ip |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

OpenTrek de

| query per hour _ _ | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per hour. |
|---|---|---|---|---|
| query per day _ _ | int | No. You must specify one of query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , or query per day _ _ . | - | The number of allowed requests per day. |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , or |  |  |

| Configuration item | Type | Required | Default value | Description |
|---|---|---|---|---|
| service name _ | string | Required | - | The Redis service name. This must be the full FQDN with the service type, such as `my-redis.dns` or `redis.my- ns.svc.cluster.loc al`. |

de OpenTrek The following table describes the fields in `redis` .

| service port _ | int | No | The default value is 80 for a static service. For other service types, the default is 6379. | The service port of the Redis service. |
|---|---|---|---|---|
| username | string | No | - | The Redis username. |
| password | string | No | - | The Redis password. |
| timeout | int | No | 1000 | The Redis connection timeout period, in milliseconds. |
| database | int | No | 0 | The ID of the database to use. For example, if you set this to 1, it corresponds to SELECT 1 . |

OpenTrek de

**Configuration examples**

**Global rate limiting for a custom rule group**

```
rule_name: routeA-global-limit-rule global_threshold:
 query_per_minute: 1000 # Limit the custom rule group to 1,000 requests/minute
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Differentiated rate limiting based on the apikey request**

**parameter**

de OpenTrek

```bash
rule_name: routeA-request-param-limit-rule rule_items:
 - limit_by_param: apikey
 limit_keys:
 - key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
 query_per_minute: 10
 - key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
 query_per_hour: 100
 - limit_by_per_param: apikey
 limit_keys:
 # Match apikeys starting with 'a' using a regular expression. Limit each match to 10 r
equests/second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # Match apikeys starting with 'b' using a regular expression. Limit each match to 100
requests/minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: Wildcard match for all apikeys. Limit each to 1,000 requests/hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Differentiated rate limiting based on the x-ca-key request**

```bash
rule_name: routeA-request-header-limit-rule rule_items:
 - limit_by_header: x-ca-key
 limit_keys:
 - key: 102234
 query_per_minute: 10
 - key: 308239
 query_per_hour: 10
 - limit_by_per_header: x-ca-key
 limit_keys:
 # Match apikeys starting with 'a' using a regular expression. Limit each match to 10 r
equests/second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # Match apikeys starting with 'b' using a regular expression. Limit each match to 100
requests/minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: Wildcard match for all apikeys. Limit each to 1,000 requests/hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

OpenTrek de

**Differentiated rate limiting based on the client IP from the x-**

**forwarded-for header**

```bash
rule_name: routeA-client-ip-limit-rule rule_items:
 - limit_by_per_ip: from-header-x-forwarded-for # IP-based rate limiting based on the x
-forwarded-for header
 limit_keys:
 # Exact IP: 1.1.X.X, limited to 10 requests/day
 - key: 1.1.X.X
 query_per_day: 10
 # IP range 1.1.1.0/24: Each IP is independently limited to 100 requests/day
 - key: 1.1.1.0/24
 query_per_day: 100
 # Fallback rule: All IPs, each independently limited to 1,000 requests/day
 - key: 0.0.0.0/0
 query_per_day: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Differentiated rate limiting based on the consumer**

```bash
rule_name: routeA-consumer-limit-rule rule_items:
 - limit_by_consumer: ''
 limit_keys:
 - key: consumer1
 query_per_second: 10
 - key: consumer2
 query_per_hour: 100
 - limit_by_per_consumer: ''
 limit_keys:
 # Match consumers starting with 'a' using a regular expression. Limit each match to 10
requests/second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # Match consumers starting with 'b' using a regular expression. Limit each match to 10
0 requests/minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: Wildcard match for all consumers. Limit each to 1,000 requests/hour.
 - key: "*"
 query_per_hour: 1000
redis:
 service_name: redis.static
show_limit_quota_header: true
```

**Differentiated rate limiting based on key-value pairs in a**

**cookie**

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|
| limit by header _ _ | string | Optional. Select one from limit by head _ _ er and limit by para _ _ m . | - | The name of the HTTP request header that provides the key value for rate limiting. |

|  |  | limit by head _ _ |  |  |
|---|---|---|---|---|
| g | er |  |  |  |
|  |  |  | and |  |
|  | m |  |  |  |

de OpenTrek

```bash
rule_name: routeA-cookie-limit-rule rule_items:
 - limit_by_cookie: key1 # Rate limit based on the cookie key 'key1'
 limit_keys:
 # Static value 'value1': Limit to 10 requests/minute
 - key: value1
 query_per_minute: 10
 # Static value 'value2': Limit to 100 requests/hour
 - key: value2
 query_per_hour: 100
 - limit_by_per_cookie: key1 # Independently rate limit each value of the cookie key 'k
ey1'
 limit_keys:
 # Match values starting with 'a' using a regular expression. Limit each to 10 requests
/second.
 - key: "regexp:^a.*"
 query_per_second: 10
 # Match values starting with 'b' using a regular expression. Limit each to 100 request
s/minute.
 - key: "regexp:^b.*"
 query_per_minute: 100
 # Fallback rule: All values, each independently limited to 1,000 requests/hour.
 - key: "*"
 query_per_hour: 1000
rejected_code: 200 rejected_msg: '{"code":-1,"msg":"Too many requests"}' redis:
 service_name: redis.static
show_limit_quota_header: true
```

##### Key-based rate limiting

The key-rate-limit plugin implements rate limiting based on a specific key value, which can be obtained from a URL parameter or an HTTP request header. This topic describes how to configure the key-rate-limit plugin.

**Runtime properties**

This plugin runs in the `Default phase` with an execution priority of `10` .

**Configuration fields**

| limit by param _ _ | string | Optional. Select one from limit by head _ _ er and limit by para _ _ m . | - | The name of the URL parameter that provides the key value for rate limiting. |
|---|---|---|---|---|
| limit keys _ | array of object | Required. | - | Specifies the rate limit settings for matched key values. |

|  |  | limit by head _ _ |  |  |
|---|---|---|---|---|
| g | er |  |  |  |
|  |  |  | and |  |
|  | m |  |  |  |

| Name | Data type | Requirement | Default value | Description |
|---|---|---|---|---|
| key | string | Required. | - | The key value to match. |
| query per secon _ _ d | number | Optional. Select one from query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , and query per day _ _ . | - | The number of allowed requests per second. |
| query per minut _ _ e | number | Optional. Select one from query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , and query per day _ _ . | - | The number of allowed requests per minute. |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , and |  |  |
| ber |  |  |  |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
| ber | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , and |  |  |

OpenTrek de The following table describes the configuration fields for each item in `limit_keys` .

| query per hour _ _ | number | Optional. Select one from query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , and query per day _ _ . | - | The number of allowed requests per hour. |
|---|---|---|---|---|
| query per day _ _ | number | Optional. Select one from query per sec _ _ ond , query per min _ _ ute , query per hou _ _ r , and query per day _ _ . | - | The number of allowed requests per day. |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
| ber | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , and |  |  |

|  |  | query per sec _ _ |  |  |  |
|---|---|---|---|---|---|
|  | ond |  |  |  |  |
|  |  |  |  | , |  |
|  | ute |  |  |  |  |
|  |  |  |  | , |  |
|  | r |  |  |  |  |
|  |  |  | , and |  |  |

de OpenTrek

**Configuration examples**

**Apply different rate limits based on the apikey request**

**parameter**

```
limit_by_param: apikey limit_keys:
- key: 9a342114-ba8a-11ec-b1bf-00163e1250b5
  query_per_second: 10
- key: a6a6d7f2-ba8a-11ec-bec2-00163e1250b5
  query_per_minute: 100
```

**Apply different rate limits based on the x-ca-key request**

```
limit_by_header: x-ca-key limit_keys:
- key: 102234
  query_per_second: 10
- key: 308239
  query_per_hour: 10
```

##### Traffic tagging

|  | Field name |  | Type | Default value | Required | Description |
|---|---|---|---|---|---|---|
|  | conditionGroup s |  | array of object | - | No | Defines conditional groups for content-based tagging. For the detailed structure, see Conditional group configuration. |
|  |  | conditionGroup |  |  |  |  |
|  | s |  |  |  |  |  |
|  | weightGroups |  | array of object | - | No | Defines conditional groups for weight-based tagging. For the detailed structure, see Weight group configuration. |
|  | defaultTagKey |  | string | - | No | The default tag key. This key is used when no conditions are matched. This parameter takes effect only when defaultTagVal is also configured. |
|  | defaultTagVal |  | string | - | No | The default tag value. This value is used when no conditions are matched. This parameter takes effect only when defaultTagKey is also configured. |

|  |  | weightGroups |
|---|---|---|

|  |  | defaultTagKey |
|---|---|---|

|  |  | defaultTagVal |
|---|---|---|

OpenTrek de The traffic-tag plugin tags request traffic by adding a specific request header. Tagging can be based on the weight or content of the request. The plugin also supports complex logic to determine how traffic is tagged based on user-defined criteria. This topic describes how to configure the traffic-tag plugin.

**Runtime properties**

Plugin execution phase: `Default phase` Plugin execution priority: `400` .

**Configuration fields**

This section describes the configuration fields.

**Conditional group configuration**

| Field name | Type | Default value | Required | Description |
|---|---|---|---|---|
| headerName | string | - | Yes | The name of the HTTP header to add or modify. |
| headerValue | string | - | Yes | The value of the HTTP header. |
| logic | string | - | Yes | The logical relationship between conditions in the group. Supported values are and and or . The value must be in lowercase. |
| conditions | array of object | - | Yes | Describes the specific tagging conditions. For the detailed structure, see the conditions configuration fields described below. |

|  | Field name |  | Type | Default value | Required | Description |
|---|---|---|---|---|---|---|
|  | conditionType |  | string | - | Yes | The condition type. Supported values are header , parameter , and cookie . |

de OpenTrek The following table describes the configuration fields for each item in `conditionGroups` : The following table describes the configuration fields for each item in `conditions` :

| key | string | - | Yes | The keyword for the condition. |
|---|---|---|---|---|
| operator | string | - | Yes | The operator. Supported values are equal , not equal , _ prefix , in , not in , _ regex , and percentage . |
| value | array of string | - | Yes | The value of the condition. You can configure multiple values only when the operator is in or not in . _ |

| Field name | Type | Default value | Required | Description |
|---|---|---|---|---|
| headerName | string | - | Yes | The name of the HTTP header to add or modify. |
| headerValue | string | - | Yes | The value of the HTTP header. |
| weight | integer | - | Yes | The traffic weight percentage. |

| Operator | Description |
|---|---|

OpenTrek de

**Note**

When the operator is regex, the regular expression engine used is RE2. For more information, see the official RE2 documentation.

**Weight group configuration**

The following table describes the configuration fields for each item in `weightGroups` :

**Operator descriptions**

| equal | Exact match. The value must be exactly equal. |
|---|---|
| not equal _ | Not equal match. The condition is met if the values are not equal. |
| prefix | Prefix match. The condition is met if the specified value is a prefix of the actual value. |
| in | Inclusion match. The actual value must be in the specified list. |
| not in _ | Exclusion match. The condition is met if the actual value is not in the specified list. |
| regex | Regular expression match. Matches according to regular expression rules. |
| percentage | Percentage match. The condition is met if hash(get(key)) % 100 < value is true. |

| x-mse-tag: gray |  |  |  |  |
|---|---|---|---|---|
|  | user |  | , |  |

de OpenTrek

**Important**

The percentage operator and the weight parameter have different functions. The percentage operator evaluates each request to determine if it meets a specific percentage condition. The weight parameter statically allocates a random proportion of the total traffic.

**Configuration examples**

**Example 1: Content-based matching**

`defaultTagVal` are configured, requests that do not match these conditions are tagged with the `x-mse-tag: base` header.

|  | x- |
|---|---|
| x-mse-tag: blue |  |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

OpenTrek de

```
defaultTagKey: x-mse-tag defaultTagVal: base conditionGroups:
 - headerName: x-mse-tag
   headerValue: gray
   logic: and
   conditions:
   - conditionType: header
     key: role
     operator: in
     value:
     - user
     - viewer
     - editor
   - conditionType: parameter
     key: foo
     operator: equal
     value:
     - bar
```

**Example 2: Weight-based matching**

```bash
# The sum of weights is 100. The remaining 40% of traffic is not configured and will no
t have a header added. weightGroups:
 - headerName: x-mse-tag
   headerValue: gray
   weight: 30
 - headerName: x-mse-tag
   headerValue: blue
   weight: 30
```

##### Request validation

The request-validation plugin validates requests before they are forwarded to upstream services. This plugin uses the `JSON Schema` mechanism to validate request data, such as the body and header. This topic describes how to configure the request-validation plugin.

**Runtime properties**

Plugin execution phase: `Authentication` . Plugin execution priority: `220` .

**Configuration fields**

| header schema _ | object | Optional | - | The JSON Schema used to validate the request header. |
|---|---|---|---|---|
| body schema _ | object | Optional | - | The JSON Schema used to validate the request body. |
| rejected code _ | number | Optional | 403 | The HTTP status code returned when a request is rejected. |
| rejected msg _ | string | Optional | - | The HTTP response body returned when a request is rejected. |
| enable swagger _ | bool | Optional | false | Specifies whether to enable validation against a Swagger document. |
| enable oas3 _ | bool | Optional | false | Specifies whether to enable validation against an OAS3 document. |

de OpenTrek

**Important**

The validation rules are the same for the header and the body.

**Configuration examples**

**Enumeration (Enum) validation**

OpenTrek de

```
body_schema:
 type: object
 required:
 - enum_payload
 properties:
 enum_payload:
 type: string
 enum:
 - "enum_string_1"
 - "enum_string_2"
 default: "enum_string_1"
```

**Boolean validation**

```
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
 default: true
```

**Number or integer range validation**

```
body_schema:
 type: object
 required:
 - integer_payload
 properties:
 integer_payload:
 type: integer
 minimum: 1
 maximum: 10
```

**String length validation**

```
body_schema:
 type: object
 required:
 - string_payload
 properties:
 string_payload:
 type: string
 minLength: 1
 maxLength: 10
```

**Regular expression (Regex) validation**

de OpenTrek

```
body_schema:
 type: object
 required:
 - regex_payload
 properties:
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**Array validation**

```
body_schema:
 type: object
 required:
 - array_payload
 properties:
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
```

**Combined field validation**

OpenTrek de

```
body_schema:
 type: object
 required:
 - boolean_payload
 - array_payload
 - regex_payload
 properties:
 boolean_payload:
 type: boolean
 array_payload:
 type: array
 minItems: 1
 items:
 type: integer
 minimum: 1
 maximum: 10
 uniqueItems: true
 default: [1, 2, 3]
 regex_payload:
 type: string
 minLength: 1
 maxLength: 10
 pattern: "^[a-zA-Z0-9_]+$"
```

**Custom rejection message**

```
body_schema:
 type: object
 required:
 - boolean_payload
 properties:
 boolean_payload:
 type: boolean
rejected_code: 403 rejected_msg: "Request rejected"
```

#### Transform

##### Request/response transform

The transformer plugin can transform request and response headers, query parameters, and body parameters. You can perform various operations, such as delete, rename, update, add, append, map, and deduplicate. This topic describes how to configure the transformer plugin.

**Runtime properties**

Execution phase: `Authentication phase` . Execution priority: `410` .

**Configuration fields**

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| reqRules | string | Optional. Specify at least one of reqRules and respRules. | - | Configuration for the request converter. Specifies the transform operation type and the transform rules for request headers, query parameters, and the request body. |
| respRules | string | Optional. Specify at least one of reqRules and respRules. | - | Configuration for the response converter. Specifies the transform operation type and the transform rules for response headers and the response body. |

| Name | Data type | Requirements | Default value | Description |
|---|---|---|---|---|
| operate | string | Required. Valid values are remove , rename , replace , add , append , map , and dedupe . | - | Specifies the transform operation type. Supported types are remove, rename, replace, add, append, map, and dedupe. If multiple rules of different types exist, they are executed in this order. |
| mapSource | string | Optional. Valid values are headers , querys , and body . | - | This is valid only when `operate` is map . Specifies the mapping source. If you do not specify this field, the default is the source itself. |

de OpenTrek The following table describes the configuration fields for each item in `reqRules` and

```
 respRules .
```

| headers | array of object | Optional. |  | - |  | Specifies the transform rules for request/response headers. |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| querys | array of object | Optional. |  | - |  | Specifies the transform rules for request query parameters. |  |  |  |  |
| body | array of object | Optional. |  |  |  | Specifies the transform rules for request/response body parameters. For request body transforms, the content-type can be application/j son , application/x |  |  |  |  |
|  |  |  |  |  |  |  | application/j |  |  |  |
|  |  |  |  |  |  | son |  |  |  |  |
|  |  |  |  |  |  |  |  | , |  |  |
|  |  |  |  |  |  | -www-form- |  |  |  |  |
|  |  |  |  |  |  | urlencoded |  |  | , or |  |
|  |  |  |  | - |  |  |  |  |  |  |
|  |  |  |  |  |  | m-data |  |  |  |  |

|  |  | application/j |  |
|---|---|---|---|
|  | son |  |  |

OpenTrek de The following table describes the configuration fields for each item in `headers` , `querys` , and `body` .

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| key | string | Optional. | - | Used when operate is remove . For more information, see Transform operation types. |
| oldKey | string | Optional. | - | Used when operate is set to rename . For more information, see Transform operation types. |
| newKey | string | Optional. | - | Used when operate is rename . For more information, see Transform operation types. |
| key | string | Optional. | - | Used when operate is replace . For more information, see Transform operation types. |
| newValue | string | Optional. | - | Used when `operate` is replace . For more information, see Transform operation types. |
| key | string | Optional. | - | Used when `operate` is set to add . For more information, see Transform operation types. |

de OpenTrek

| value | string | Optional. | - | Used when operate is add . For more information, see Transform operation types. |
|---|---|---|---|---|
| key | string | Optional. | - | Used when operate is append . For more information, see Transform operation types. |
| appendValue | string | Optional. | - | Used when `operate` is append . For more information, see Transform operation types. |
| fromKey | string | Optional. | - | Used when operate is map . For more information, see Transform operation types. |
| toKey | string | Optional. | - | Used when operate is set to map . For more information, see Transform operation types. |
| key | string | Optional. | - | Used when `operate` is dedupe . For more information, see Transform operation types. |

OpenTrek de

| strategy | string | Optional. | - |  |  | Used when operate is dedupe . For more information, see Transform operation types. |  |  |
|---|---|---|---|---|---|---|---|---|
| value type _ | string | Optional. Valid values are object , boolean , number , and string . |  |  |  | When content- |  |  |
|  |  |  |  |  |  |  | content- |  |
|  |  |  |  |  |  | type: |  |  |
|  |  |  |  |  |  | application/jso |  |  |
|  |  |  | string |  |  |  |  |  |
|  |  |  |  |  |  | n |  |  |
| host pattern _ | string | Optional. | - |  |  | Specifies the matching rule for the request hostname. This field is valid when the transform operation type is replace , add , or append . |  |  |
| path pattern _ | string | Optional. | - |  |  | Specifies the matching rule for the URI of the request. This field is valid when the transform operation type is replace , add , or append . |  |  |

| obje | ct |
|---|---|
| boolean |  |
| number |  |
| string |  |

de OpenTrek Note:

| host pattern _ |  |
|---|---|
| add |  |

| Operation type | Meaning of key field | Meaning of value field | Description |
|---|---|---|---|
| remove | Target key | Not required | If the specified key exists, it is deleted. Otherwise, no operation is performed. |
| rename | Target oldKey | New key name | If the specified oldKey:value exists, its key is renamed to newKey , resulting in newKey:value . Otherwise, no operation is performed. |

OpenTrek de The `request transformer` supports transformations on request headers, query parameters, and the request body (application/json, application/x-www-form-urlencoded, and multipart/form-data). The `response transformer` supports transformations on response headers and the response body (application/json). The plugin supports bidirectional transforms. A single plugin can transform both the request and the response. The transform operations are executed in the order specified in the configuration file. For example, remove → rename → replace → add → append → map → dedupe, or dedupe → map → append → add → replace → rename → remove. When transforming headers, the `key` is case-insensitive. For `rename` and `map` operations, the `value` is also case-insensitive because it functions as a key. In contrast, for queries and body parameters, both the `key` and `value` fields are case-sensitive. `value_type` is valid only for request and response bodies with a content-type of application/json.

| Update and replace | Target key | New value | If the specified key:value exists, its value is updated to newValue , resulting in key:newValue . Otherwise, no operation is performed. |  |
|---|---|---|---|---|
| add | Key to add | Value to add | If the specified key:value does not exist, it is added. Otherwise, no operation is performed. |  |
| append | Target key | Value to append | If the specified key:value pair exists, `appendValue` is appended, resulting in key:[value..., appendValue] . Otherwise, this operation is equivalent to executing an `add` operation, which results in key:appendValue . |  |
| map | Mapping source fromKey | Mapping target toKey | If the specified fromKey:fromValue exists, its value fromValue is mapped to toKey to create toKey:fromValue , while fromKey:fromValue is retained. Note If toKey already exists, its value is overwritten. Otherwise, no operation is performed. |  |

| o append | appendValue] |
|---|---|

|  |  | fromKey:fromValue |
|---|---|---|

|  |  | fromKey:fromValue |
|---|---|---|
| ping target toKey |  |  |

de OpenTrek

| dedupe | Target key | Deduplication policy (strategy) |  |  | strategy can be one of the following: RETAIN UNIQUE : _ Retains all unique values in order. For example, k1: |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | k1: |  |  |
|  |  |  |  |  | [v1,v2,v3,v3,v2,v1 |  |  |  |  |
|  |  |  |  |  | ] | becomes |  | k1: |  |

|  |  | k1: |  |
|---|---|---|---|
|  | [v1,v2,v3] |  |  |

OpenTrek de

**Configuration examples**

**Implement routing based on body parameters**

Configuration example:

```
reqRules:
- operate: map
 headers:
 - fromKey: userId
 toKey: x-user-id
 mapSource: body
```

This rule parses the `userId` from the request body and adds it to the request header as `x-` `user-id` . This lets you implement routing based on body parameters using the AI Gateway's ability to match routes based on request headers. This configuration supports both `application/json` and `application/x-www-form-` `urlencoded` request body types.

|  | x-user- |
|---|---|
| x-user-id: |  |

|  | id |
|---|---|
| 12 |  |

de OpenTrek For example:

**For an application/json body**

```bash
curl localhost -d '{"userId":12, "userName":"johnlanni"}' -H 'contenttype:application/json'
```

The gateway recalculates the route after the plugin adds this header. This allows gateway routing rules to match this header and direct requests to a specific target service.

**application/x-www-form-urlencoded body**

```bash
curl localhost -d 'userId=12&userName=johnlanni'
```

The value of the `userId` field is extracted from the form data in `k1=v1&k2=v2` format and added to the request as the `x-user-id` header. The backend service then receives a request header such as `x-user-id: 12` . The gateway recalculates the route after the plugin adds this header. This allows gateway routing rules to match this header, directing requests to a specific target service.

**JSON path support**

You can extract fields from complex JSON based on the GJSON Path syntax. For example, with the following JSON:

```json
{
 "name": {"first": "Tom", "last": "Anderson"},
 "age":37,
 "children": ["Sara","Alex","Jack"],
 "fav.movie": "Deer Hunter",
 "friends": [
 {"first": "Dale", "last": "Murphy", "age": 44, "nets": ["ig", "fb", "tw"]},
 {"first": "Roger", "last": "Craig", "age": 68, "nets": ["fb", "tw"]},
 {"first": "Jane", "last": "Murphy", "age": 47, "nets": ["ig", "tw"]}
```

]

```
}
```

You can extract data as follows:

```
name.last "Anderson" name.first "Tom" age 37 children ["Sara","Alex","Jack"] children.0 "Sara" children.1 "Alex" friends.1 {"first": "Roger", "last": "Craig", "age": 68} friends.1.first "Roger"
```

OpenTrek de To extract the first field from the second item in friends and the last field from the JSON body, and then set them as the values of the `x-first-name` and `x-last-name` headers, use the following plugin configuration:

```
reqRules:
- operate: map
 headers:
 - fromKey: friends.1.first
 toKey: x-first-name
 - fromKey: friends.1.last
 toKey: x-last-name
 mapSource: body
reqRules:
- operate: remove
 headers:
 - key: X-remove
- operate: rename
 headers:
 - oldKey: X-not-renamed
 newKey: X-renamed
- operate: replace
 headers:
 - key: X-replace
 newValue: replaced
- operate: add
 headers:
 - key: X-add-append
 value: host-$1
 host_pattern: ^(.*)\.com$
- operate: append
 headers:
 - key: X-add-append
 appendValue: path-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: map
 headers:
 - fromKey: X-add-append
 toKey: X-map
- operate: dedupe
 headers:
 - key: X-dedupe-first
 strategy: RETAIN_FIRST
 - key: X-dedupe-last
 strategy: RETAIN_LAST
 - key: X-dedupe-unique
 strategy: RETAIN_UNIQUE
```

Send a request: de OpenTrek

```json
$ curl -v console.higress.io/get -H 'host: foo.bar.com' \ -H 'X-remove: exist' -H 'X-not-renamed:test' -H 'X-replace:not-replaced' \ -H 'X-dedupe-first:1' -H 'X-dedupe-first:2' -H 'X-dedupe-first:3' \ -H 'X-dedupe-last:a' -H 'X-dedupe-last:b' -H 'X-dedupe-last:c' \ -H 'X-dedupe-unique:1' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:3' \ -H 'X-dedupe-unique:3' -H 'X-dedupe-unique:2' -H 'X-dedupe-unique:1'
# httpbin response
{
 "args": {},
 "headers": {
 ...
 "X-Add-Append": "host-foo.bar,path-get",
 ...
 "X-Dedupe-First": "1",
 "X-Dedupe-Last": "c",
 "X-Dedupe-Unique": "1,2,3",
 ...
 "X-Map": "host-foo.bar,path-get",
 "X-Renamed": "test",
 "X-Replace": "replaced"
 },
 ...
}
```

OpenTrek de

```
reqRules:
- operate: remove
 querys:
 - key: k1
- operate: rename
 querys:
 - oldKey: k2
 newKey: k2-new
- operate: replace
 querys:
 - key: k2-new
 newValue: v2-new
- operate: add
 querys:
 - key: k3
 value: v31-$1
 path_pattern: ^.*?\/(\w+)[\?]{0,1}.*$
- operate: append
 querys:
 - key: k3
 appendValue: v32
- operate: map
 querys:
 - fromKey: k3
 toKey: k4
- operate: dedupe
 querys:
 - key: k4
 strategy: RETAIN_FIRST
```

Send a request:

```json
$ curl -v "console.higress.io/get?k1=v11&k1=v12&k2=v2"
# httpbin response
{
 "args": {
 "k2-new": "v2-new",
 "k3": [
 "v31-get",
 "v32"
```

`],`

```json
 "k4": "v31-get"
 },
 ...
 "url": "http://foo.bar.com/get?k2-new=v2-new&k3=v31-get&k3=v32&k4=v31-get"
}
```

de OpenTrek

```
reqRules:
- operate: remove
 body:
 - key: a1
- operate: rename
 body:
 - oldKey: a2
 newKey: a2-new
- operate: replace
 body:
 - key: a3
 newValue: t3-new
 value_type: string
- operate: add
 body:
 - key: a1-new
 value: t1-new
 value_type: string
- operate: append
 body:
 - key: a1-new
 appendValue: t1-$1-append
 value_type: string
 host_pattern: ^(.*)\.com$
- operate: map
 body:
 - fromKey: a1-new
 toKey: a4
- operate: dedupe
 body:
 - key: a4
 strategy: RETAIN_FIRST
```

Send a request:

**Content-Type: application/json**

OpenTrek de

```json
$ curl -v -x POST console.higress.io/post -H 'host: foo.bar.com' \ -H 'Content-Type: application/json' -d '{"a1":"t1","a2":"t2","a3":"t3"}'
# httpbin response
{
 ...
 "headers": {
 ...
 "Content-Type": "application/json",
 ...
 },
 "json": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 ...
}
```

**Content-Type: application/x-www-form-urlencoded**

```json
$ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \ -d 'a1=t1&a2=t2&a3=t3'
# httpbin response
{
 ...
 "form": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 "headers": {
 ...
 "Content-Type": "application/x-www-form-urlencoded",
 ...
 },
 ...
}
```

**Content-Type: multipart/form-data**

de OpenTrek

```json
$ curl -v -X POST console.higress.io/post -H 'host: foo.bar.com' \ -F a1=t1 -F a2=t2 -F a3=t3
# httpbin response
{
 ...
 "form": {
 "a1-new": [
 "t1-new",
 "t1-foo.bar-append"
```

`],`

```json
 "a2-new": "t2",
 "a3": "t3-new",
 "a4": "t1-new"
 },
 "headers": {
 ...
 "Content-Type": "multipart/form-data; boundary=------------------------
1118b3fab5afbc4e",
 ...
 },
 ...
}
```

This process is similar to transforming requests. This section provides notes specifically for transforming request or response bodies in JSON format.

**Nest keys using  .**

1. Typically, a . in the specified key indicates nesting, as shown below:

```json
respRules:
- operate: add
 body:
 - key: foo.bar
 value: value
$ curl -v console.higress.io/get
# httpbin response
{
 ...
 "foo": {
 "bar": "value"
 },
 ...
}
```

2. When you use \. to escape the . in a key, it treats the period as a literal character
instead of a nesting operator, as shown below: OpenTrek de

**Note**

When the string is enclosed in double quotation marks, you must use \\. to escape the period.

```bash
respRules:
- operate: add
 body:
 - key: foo\.bar
 value: value
$ curl -v console.higress.io/get
# httpbin response
{
 ...
 "foo.bar": "value",
 ...
}
```

**Access array elements using  .index**

You can access array elements using the syntax array.index, where index is the zero-based index of the element:

```json
{
 "users": [
 {
 "123": { "name": "zhangsan", "age": 18 }
 },
 {
 "456": { "name": "lisi", "age": 19 }
 }
```

]

```
}
```

1. To remove the first element from `user` :

```
reqRules:
- operate: remove
 body:
 - key: users.0
```

de OpenTrek

```json
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'
# httpbin response
{
 ...
 "json": {
 "users": [
 {
 "456": {
 "name": "lisi"
 }
 }
```

]

```
 },
 ...
}
```

2. Rename the key `123` of the first element in `users` to `msg` :

```json
reqRules:
- operate: rename
 body:
 - oldKey: users.0.123
 newKey: users.0.first
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"123":{"name":"zhangsan"}},{"456":{"name":"lisi"}}]}'
# httpbin response
{
 ...
 "json": {
 "users": [
 {
 "msg": {
 "name": "zhangsan"
 }
 },
 {
 "456": {
 "name": "lisi"
 }
 }
```

]

```
 },
 ...
}
```

**Traverse array elements using  .#**

OpenTrek de You can use `array.#` to traverse an array:

**Note**

This operation is currently supported only for replace operations. Using this syntax with other transform operations may lead to unpredictable results.

```json
{
 "users": [
 {
 "name": "zhangsan",
 "age": 18
 },
 {
 "name": "lisi",
 "age": 19
 }
```

]

```json
} reqRules:
- operate: replace
 body:
 - key: users.#.age
 newValue: 20
$ curl -v -X POST console.higress.io/post \ -H 'Content-Type: application/json' \ -d '{"users":[{"name":"zhangsan","age":18},{"name":"lisi","age":19}]}'
# httpbin response
{
 ...
 "json": {
 "users": [
 {
 "age": "20",
 "name": "zhangsan"
 },
 {
 "age": "20",
 "name": "lisi"
 }
```

]

```
 },
 ...
}
```

| Name | Data type | Required |  | Default value |  | Description |  |  |
|---|---|---|---|---|---|---|---|---|
| grayKey | string | Optional |  | - |  | The unique identifier for a user ID. It can come from a cookie or a header, such as userid . If not specified, the system uses rules[].grayT agKey and rules[].grayT agValue to filter grayscale rules. |  |  |
| graySubKey | string | Optional |  | - |  | User identity information may be exposed in JSON format. For example: userInfo:{ |  |  |
|  |  |  |  |  |  |  | userInfo:{ |  |
|  |  |  |  |  |  | userCode:"001" |  |  |
|  |  |  |  |  |  | } |  |  |
| rules | array of object | Required |  | - |  | Defines different grayscale rules for various scenarios. |  |  |

|  |  | rules[].grayT |  |  |
|---|---|---|---|---|
|  | agKey |  |  |  |
|  |  |  | and |  |

de OpenTrek

##### Frontend grayscale release

The frontend-gray plugin implements grayscale releases for frontend users. This plugin supports A/B tests. It also ensures the stability of system releases and O&M through grayscale, monitoring, and rollback policies. This topic describes how to configure the frontend-gray plugin.

**Runtime properties**

Plugin execution phase: `Authentication phase` . Plugin execution priority: `450` .

**Configuration fields**

|  | rewrite |  | object | Required | - | Rewrite configurations. These are typically used for frontend deployments on OSS or CDN. |
|---|---|---|---|---|---|---|
|  | baseDeployment |  | object | Optional | - | Configures the baseline rule. |
|  |  | baseDeployment |  |  |  |  |
|  | grayDeployment s |  | array of object | Optional | - | Configures the effective rules and versions for the grayscale release. |
|  |  | grayDeployment |  |  |  |  |
|  | s |  |  |  |  |  |

|  | Name |  | Data type | Required | Default value |  | Description |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | name |  | string | Required | - |  | The unique name of the rule. It is associated with deploy.gray[] .name to take effect. |  |  |
|  |  |  |  |  |  |  |  | deploy.gray[] |  |
|  |  |  |  |  |  |  | .name |  |  |
|  | grayKeyValue |  | array of string | Optional | - |  | A whitelist of user IDs. |  |  |
|  |  | grayKeyValue |  |  |  |  |  |  |  |
|  | grayTagKey |  | string | Optional | - |  | The key of the tag used for user categorization. It comes from a cookie. |  |  |
|  | grayTagValue |  | array of string | Optional | - |  | The value of the tag used for user categorization. It comes from a cookie. |  |  |
|  |  | grayTagValue |  |  |  |  |  |  |  |

OpenTrek de Configuration of the `rules` field: Configuration of the `rewrite` field: Both `indexRouting` (homepage rewrite) and `fileRouting` (file rewrite) are based on prefix matching. For example, the mapping `/app1` : `/mfe/app1/{version}/index.html` means that requests with the /app1 prefix are routed to the `/mfe/app1/{version}/index.html` page. The `{version}` variable represents the version number and is dynamically replaced with the value of `baseDeployment.version` or `grayDeployments[].version` at runtime.

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| host | string | Optional | - | The host address. If you use OSS, set this to the VPC internal network endpoint. |
| notFoundUri | string | Optional | - | The configuration for the 404 page. |

de OpenTrek `{version}` is a reserved placeholder. It is dynamically replaced with the frontend version number from `baseDeployment.version` or `grayDeployments[].version` during execution.

|  | indexRouting |  | map of string to string | Optional |  |  |  | Defines rewrite rules for the home page. Each key represents the routing path of the home page, and the value points to the target redirection file. For example, the key /app1 corresponds to the value /mfe/app1/{ve |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | /mfe/app1/{ve |  |
|  |  |  |  |  |  |  |  | rsion}/index.ht |  |  |
|  |  |  |  |  |  |  |  | ml |  |  |
|  |  |  |  |  |  | - |  |  |  |  |
|  |  | indexRouting |  |  |  |  |  |  |  |  |

|  |  | /mfe/app1/0.0 |  |
|---|---|---|---|
|  | .1/index.html |  |  |

OpenTrek de

| fileRouting | map of string to string | Optional | - |  | Defines rewrite rules for resource files. Each key represents the resource access path, and the value points to the target redirection file. For example, the key /app1/ corresponds to the value /mfe/app1/{ve rsion} . If the effective version is 0.0.1 and the access path is /app1/js/a.js , the request is redirected to /mfe/app1/0.0 .1/js/a.js . |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | /mfe/app1/0.0 |  |
|  |  |  |  |  | .1/js/a.js |  |  |

|  |  | /mfe/app1/{ve |  |
|---|---|---|---|
|  | rsion} |  |  |

|  |  | /app1/js/a.js |
|---|---|---|

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| version | string | Required | - | The version number of the base version. This serves as the fallback version. |

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|

de OpenTrek Configuration of the `baseDeployment` field: Configuration of the `grayDeployments` field:

|  | version |  | string | Required | - | The version number of the grayscale version. This version is used if a grayscale rule is hit. For non- CDN deployments, the x-higress- tag is added to the header. |  |  |
|---|---|---|---|---|---|---|---|---|
|  | backendVersion |  | string | Required | - | The backend grayscale version. The x- mse-tag is added to the header of XHR/Fetch requests to the backend. |  |  |
|  |  |  |  |  |  |  | x- |  |
|  |  | backendVersion |  |  |  |  |  |  |
|  | name |  | string | Required | - | The rule name. It is associated with rules[].name . |  |  |
|  | enabled |  | boolean | Required | - | Specifies whether to enable the current grayscale rule. |  |  |

|  |  | x-higress- |
|---|---|---|
|  | tag |  |

|  | mse-tag |
|---|---|

|  |  | rules[].name |
|---|---|---|

OpenTrek de

**Configuration examples**

**Basic configuration**

de OpenTrek

```
grayKey: userid rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

The unique user identifier in the cookie is `userid` . The current grayscale rule is configured for the `beta-user` tag. The `version: gray` is used when the following conditions are met: The `userid` in the cookie is `00000002` or `00000003` . The `level` in the cookie is `level3` or `level5` . Otherwise, the `version: base` is used.

**User information in JSON**

OpenTrek de

```
grayKey: appInfo graySubKey: userId rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

The `appInfo` field in the cookie contains JSON data. The `userId` field within this data is used as the unique identifier. The current grayscale rule is configured for the `beta-user` tag. The `version: gray` is used when the following conditions are met: The `userid` in the cookie is `00000002` or `00000003` . The `level` in the cookie is `level3` or `level5` . Otherwise, the `version: base` is used.

**Rewrite configuration**

**Note**

This configuration is typically used in CDN deployment scenarios. de OpenTrek

```
grayKey: userid rules:
- name: inner-user
 grayKeyValue:
 - '00000001'
 - '00000005'
- name: beta-user
 grayKeyValue:
 - '00000002'
 - '00000003'
 grayTagKey: level
 grayTagValue:
 - level3
 - level5
rewrite:
 host: frontend-gray.oss-cn-shanghai-internal.aliyuncs.com
 notFoundUri: /mfe/app1/dev/404.html
 indexRouting:
 /app1: '/mfe/app1/{version}/index.html'
 /: '/mfe/app1/{version}/index.html',
 fileRouting:
 /: '/mfe/app1/{version}'
 /app1/: '/mfe/app1/{version}'
baseDeployment:
 version: base
grayDeployments:
 - name: beta-user
 version: gray
 enabled: true
```

The `{version}` placeholder is dynamically replaced with the actual version number during runtime.

**indexRouting: Home page routing configuration**

Requests for paths such as `/app1` , `/app123` , `/app1/index.html` , `/app1/xxx` , or `/xxxx` are routed to '/mfe/app1/{version}/index.html'.

**fileRouting: File routing configuration**

The following file mappings are valid:

```
 /js/a.js  =>  /mfe/app1/v1.0.0/js/a.js
 /js/template/a.js  =>  /mfe/app1/v1.0.0/js/template/a.js
 /app1/js/a.js  =>  /mfe/app1/v1.0.0/js/a.js
 /app1/js/template/a.js  =>  /mfe/app1/v1.0.0/js/template/a.js
```

##### Custom responses

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| status code _ | number | Optional | 200 | The custom HTTP response status code. |
| headers | array of string | Optional | - | The custom HTTP response headers. Separate the key and value with an equal sign ( = ). |
| body | string | Optional | - | The custom HTTP response body. |
| enable on status _ _ | array of number | Optional | - | The original status code to match. If a match is found, a custom response is generated. If you leave this field empty, the original status code is not checked. |

OpenTrek de The custom-response plugin lets you configure custom responses, including custom HTTP response status codes, HTTP response headers, and HTTP response bodies. You can use this plugin to mock responses or to provide a custom response for a specific status code, such as when a gateway throttling policy is triggered. This topic describes how to configure the custom-response plugin.

**Runtime properties**

This plugin runs during the `Authentication phase` with an execution priority of `910` .

**Configuration fields**

**Configuration examples**

**Mock response scenario**

```
status_code: 200 headers:
- Content-Type=application/json
- Hello=World
body: "{\"hello\":\"world\"}"
```

| Parameter | Description | Default |
|---|---|---|
| gql | The GraphQL query. | Cannot be empty |
| endpoint | The GraphQL query endpoint. | /graphql |
| timeout | The query connection timeout in milliseconds. | 5000 |

de OpenTrek This configuration returns the following custom response:

```json
HTTP/1.1 200 OK Content-Type: application/json Hello: World Content-Length: 17 {"hello":"world"}
```

**Custom response when throttling is triggered**

```
enable_on_status:
- 429
status_code: 302 headers:
- Location=https://example.com
```

When gateway throttling is triggered, a `429` status code is typically returned. In this scenario, the request returns the following custom response:

```
HTTP/1.1 302 Found Location: https://example.com
```

This uses the browser's 302 redirection mechanism to redirect throttled users to another page, such as a static page on a CDN. To return a different standard response when throttling is triggered, configure the fields as shown in the mock response scenario.

##### DeGraphQL

The de-graphql plugin enables you to access a GraphQL upstream service as a traditional service by mapping URIs to GraphQL queries. This topic describes how to configure the degraphql plugin.

**Runtime properties**

Plugin execution phase: `Authentication phase` Plugin execution priority: `430` .

**Parameter settings**

| domain | The service domain name. This is used when the service source is a DNS configuration. | - |
|---|---|---|

OpenTrek de

**Plugin usage**

Sample configuration

```
apiVersion: networking.higress.io/v1 kind: McpBridge metadata:
 name: default
 namespace: higress-system
spec:
 registries:
 - domain: api.github.com
 name: github
 port: 443
 type: dns
--apiVersion: networking.k8s.io/v1 kind: Ingress metadata:
 annotations:
 higress.io/destination: github.dns
 higress.io/upstream-vhost: "api.github.com"
 higress.io/backend-protocol: HTTPS
 name: github-api
 namespace: higress-system
spec:
 ingressClassName: higress
 rules:
 - http:
 paths:
 - backend:
 resource:
 apiGroup: networking.higress.io
 kind: McpBridge
 name: default
 path: /api
 pathType: Prefix
--apiVersion: extensions.higress.io/v1alpha1 kind: WasmPlugin metadata:
 namespace: higress-system
spec:
 matchRules:
 - ingress:
 - github-api
 config:
 timeout: 5000
endpoint:/graphql
```

de OpenTrek

```
 endpoint: /graphql
 domain: api.github.com
 gql: |
 query ($owner:String! $name:String!){
 repository(owner:$owner, name:$name) {
 name
 forkCount
 description
 }
 }
 url: oci://higress-registry.cn-hangzhou.cr.aliyuncs.com/plugins/de-graphql:1.0.0
```

Test result

```json
curl "http://localhost/api?owner=alibaba&name=higress" -H "Authorization: Bearer some-t oken" {
 "data": {
 "repository": {
 "description": "Next-generation Cloud Native Gateway",
 "forkCount": 149,
 "name": "higress"
 }
 }
}
```

**Introduction to GraphQL**

**GraphQL endpoint**

A REST API has multiple endpoints. A GraphQL API has only one endpoint.

```
https://api.github.com/graphql
```

**Communicating with GraphQL**

You can use cURL or any other HTTP-compatible library to communicate with a GraphQL API. While REST uses the HTTP verb to determine the operation, GraphQL requires a JSON request body to run a query. For this reason, the POST HTTP verb is used for most operations. The only exception is an introspection query, which is a simple GET request sent to the endpoint.

**GraphQL POST request parameters**

A standard GraphQL POST request includes the following: An HTTP request header: Content-Type: application/json. A request body in JSON format. The JSON request body contains the following fields: query: The query document. This field is required. variables: The variables. This field is optional. operationName: The operation name. This field is optional, but required if the query document contains multiple operations. OpenTrek de

```json
{
 "query": "{viewer{name}}",
 "operationName": "",
 "variables": {
 "name": "value"
 }
}
```

**Basic GraphQL parameter types**

The basic parameter types are String, Int, Float, and Boolean. [Type] represents an array. For example, [Int] represents an integer array. When passing basic GraphQL parameters: Formal parameters are defined within parentheses. A type must be defined for each parameter. An exclamation mark (!) indicates that a parameter is required.

```
query ($owner : String!, $name : String!) {
 repository(owner: $owner, name: $name) {
 name
 forkCount
 description
 }
}
```

**Testing GitHub GraphQL**

You can use the cURL command to query GraphQL by sending a POST request with a valid JSON request body. The request body must contain a string named `query`.

```json
curl https://api.github.com/graphql -X POST \ -H "Authorization: bearer <PAT>" \ -d "{\"query\": \"query { viewer { login }}\"}" {
 "data": {
 "viewer": {
 "login": "2456868764"
 }
 }
}
```

| Name | Data type | Requirements | Default value | Description |
|---|---|---|---|---|

de OpenTrek

```json
curl 'https://api.github.com/graphql' -X POST \ -H 'Authorization: bearer <PAT>' \ -d '{"query":"query ($owner: String!, $name: String!) {\n repository(owner: $owner, na me: $name) {\n name\n forkCount\n description\n }\n}\n","variables": {"owner":"2456868764","name":"higress"}}' {
 "data": {
 "repository": {
 "name": "higress",
 "forkCount": 149,
 "description": "Next-generation Cloud Native Gateway"
 }
 }
}
```

**References**

https://github.com/graphql/graphql-spec https://docs.github.com/zh/graphql/guides/forming-calls-with-graphql https://github.com/altair-graphql/altair

##### Browser cache control

The cache-control plug-in adds `Expires` and `Cache-Control` headers to a response based on the file extension in the request URL. This allows browsers to cache specific files, such as `jpg` and `png` image files. This topic describes how to configure the cache-control plug-in.

**Runtime properties**

Execution phase: `Authentication` . Execution priority: `420` .

**Configuration fields**

| suffix | string | Optional. The file extensions to match, such as jpg and png . To match multiple extensions, separate them with a vertical bar ( \| ), such as png\|jpg . If you leave this field empty, all extensions are matched. | - | Specifies the file extensions of requests to match. |
|---|---|---|---|---|
| expires | string | Required. The maximum cache duration. If you enter a number, the unit is seconds. For example, to cache for one hour, enter 3600. You can also enter epoch or max. These values have the same semantics as in NGINX. | - | Specifies the maximum cache duration. |

OpenTrek de

**Configuration examples**

1. Cache files with the `jpg` , `png` , and `jpeg` extensions for one hour.

```
suffix: jpg|png|jpeg expires: 3600
```

This configuration adds the `Expires` and `Cache-Control` headers to the response for the following requests. The expiration time is set to one hour from the current time.

```bash
curl http://example.com/test.png curl http://exmaple.com/test.jpg
```

2. Cache all files until the maximum expiration time: `"Thu, 31 Dec 2037 23:55:55 GMT"` .

```
expires: max
```

#### Observability

| Name | Data type | Required | Default value | Description |
|---|---|---|---|---|
| ip protocol _ | string | No | ipv4 | Valid values: ipv4: Retrieves geolocation information only for user requests over IPv4 and passes it to subsequent plugins. Requests from IPv6 users skip this plugin and are processed by subsequent plugins. ipv6: (This feature will be available in a future version) Retrieves geolocation information only for user requests over IPv6 and passes it to subsequent plugins. Requests from IPv4 users skip this plugin and are processed by subsequent plugins. Note Currently, requests are still skipped by the plugin and processed by subsequent plugins. |
| ip source type _ _ | string | No | origin-source | Valid values: Peer socket IP: origin-source . Get from header: header . |

de OpenTrek

##### IP geolocation

The geo-ip plugin retrieves geolocation information based on a user's IP address. It then passes this information to subsequent plugins using request properties and a new request header. This topic describes how to configure the geo-ip plugin.

**Execution properties**

Execution phase: `Authentication phase` . Execution priority: `440` .

**Configuration fields**

| ip header nam _ _ e | string | No | x-forwarded-for | When ip source type is _ _ set to header , this field specifies the custom header for the source IP address. |
|---|---|---|---|---|

OpenTrek de

**Configuration example**

```
ip_protocol: ipv4 ip_source_type: header ip_header_name: X-Real-Ip
```

**How to use properties**

The geo-ip plugin calls proxywasm.SetProperty() to add the country, city, province, and ISP values to the request properties. Subsequent plugins can then retrieve this information. You can use proxywasm.GetProperty() to retrieve the geolocation data for the user's IP address in the request.

**Extend the AI prompt decorator plugin to include user**

**geolocation information**

To add user geolocation information to a Large Language Model (LLM) request, enable both the geo-ip plugin and the AI prompt decorator plugin. The execution priority of the geo-ip plugin must be higher than that of the AI prompt decorator plugin. The geo-ip plugin first determines the user's geolocation from their IP address and passes the information to subsequent plugins using request properties. For example, in the default phase, set the execution priority of the geo-ip plugin to 1000 and the AI prompt decorator plugin to 500. The following is a configuration example for the geo-ip plugin:

```
ipProtocal: "ipv4"
```

The following is a configuration example for the AI prompt decorator plugin:

```
prepend:
- role: system
 content: "The user's current geolocation is: Country: ${geo-country}, Province: ${geo-
province}, City: ${geo-city}" append:
- role: user
 content: "After answering the question, ask a follow-up question."
```

Send a request using the preceding configuration: de OpenTrek

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "user",
 "content": "What is the weather like today?"
 }
```

]

```
}'
```

After the plugin processes the request, the actual request is as follows:

```json
curl http://localhost/test \ -H "content-type: application/json" \ -H "x-forwarded-for: 87.254.XXX.XXX,4.5.X.X" \ -d '{
 "model": "gpt-3.5-turbo",
 "messages": [
 {
 "role": "system",
 "content": "The user's current geolocation is: Country: China, Province: Beijing, City
: Beijing"
 },
 {
 "role": "user",
 "content": "What is the weather like today?"
 },
 {
 "role": "user",
 "content": "After answering the question, ask a follow-up question."
 }
```

]

```
}'
```

### Certificate management

#### Create a certificate

You can use the certificate management feature to upload certificates to an AI gateway. When a user accesses the gateway over HTTPS, the gateway finds the certificate that matches the requested domain name and sends it to the user to complete the TLS handshake.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.

| Parameter | Description |
|---|---|
| Certificate Name | A custom name. The maximum length is 15 characters. |
| Certificate Type | Only Server Certificate is supported. |
| Certificate File | Enter the content of the certificate file in the text box, or click Upload Certificate to read the content from a file. |
| Certificate Key | Enter the content of the certificate key in the text box, or click Upload Key to read the content from a file. |

OpenTrek de
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate Management** page, click **Create Certificate**. Configure the
parameters, and then click **OK**.

#### Manage certificates

Certificate management includes features to update, delete, and view certificate details. These features help you manage the entire certificate lifecycle.

**View certificate details**

After you upload a certificate, you can view its details.
1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate Management** page, click the name of the target certificate to view its
details:
**Basic Information**: View the **Certificate ID**, **Serial Number**, **Certificate Name**,
**Algorithm**, **Certificate Type**, **Private Key Length**, **Issue Time**, and **Expiration Time**.
**Issuer Information**: View the **Issuer Name** and **Issuer Department**.

**Update a certificate**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate Management** page, find the target certificate and click **Update** in the
**Operation** column.
de OpenTrek
6. In the **Update Certificate** panel, enter the new certificate information and click **OK**.

**Delete a certificate**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate Management** page, find the target certificate and click **Delete** in the
**Operation** column.
6. In the **Prompt** dialog box, click **OK**.

**Access the gateway**

After you upload the certificate, you can access the gateway using the correct domain name and an incorrect one. The results are as follows:

| Parameter | Description |
|---|---|
| Domain | Enter the full domain name, such as hello.com . You can manage the protocols and certificates for this domain name independently. Routing configurations are also isolated by domain name. |

OpenTrek de A successful handshake occurs only when you access the gateway with the correct domain name because the gateway can provide the corresponding certificate.

### Domain name management

#### Create a domain name

AI Gateway lets you manage protocols, certificates, and routing configurations for multiple domain names.

**Prerequisites**

Complete the ICP filing for the domain name.

**Note**

Domain names used in mainland China must have an ICP filing with Alibaba Cloud or have their ICP filing transferred to Alibaba Cloud. ICP filing is not required for domain names used outside China.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. Click **Associate Domain**. In the **Associate Domain** pane, configure the parameters, and
then click **OK**.

| Protocol | Select the HTTP protocol or the HTTPS protocol. The supported ports for each protocol are as follows: HTTP: Port 80 is supported. HTTPS: Port 443 is supported. |
|---|---|
| Server Certificate | Note This parameter is displayed only when you set Protocol to HTTPS. Select an SSL Certificate created in Certificate Management Service. |

de OpenTrek

**Verify the results**

An accessible route is configured for the path under the current domain name. If the public DNS record for your domain name is active, you can verify access directly in a browser. If you have not configured DNS parsing for your domain name, you can use the following method to verify access. For example, if your domain name is `hello.com` , replace {Public IP} in the following command with your public IP address. Verify HTTP

```bash
curl http://hello.com --resolve "hello.com:80:{Public IP}"
```

Verify HTTPS

```bash
curl -v -k https://hello.com --resolve "hello.com:443:{Public IP}" --cacert my-cert .pem
```

#### Manage domain names

After you create a domain name, you can edit it, delete it, or view its details.

**View domain name details**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Management** page, click a domain name to open the **Domain Details**
page. You can view the domain name's **Basic Information**, **Routing Information**, and
**Plugin Configuration**.
**Basic Information**: This section displays the **Domain Name** and **Protocol**.
**Routing Information**: Click a routing or service name to view its details.
OpenTrek de Click the **Plugin Configuration** tab to manage the plugins that are bound to the domain name. Click **Add Plugin** to bind a plugin to the domain name. For more information, see Create a plugin.

**Note**

On the Domain Management page, you can also click **Plugin Configuration** in the
**Actions** column to go directly to the **Plugin Configuration** tab.

**Modify a domain name**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Management** page, find the domain name that you want to modify and
click **Edit** in the **Actions** column.
6. In the **Modify Domain Name** panel, change the protocol and certificate, and then click
**OK**.

**Delete a domain name**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Management** page, find the domain name that you want to delete and
click **Delete** in the **Actions** column.
6. In the **Prompt** dialog box, click **OK**.

### Observation and analysis

#### Model monitoring

This topic describes how to use the **model monitoring** feature in the AI Gateway console to query and analyze data.

**Background information**

Model monitoring is a core feature of Apsara Stack AI gateways used to observe and analyze large language model (LLM) service calls and assess the performance of LLM services in real time. This feature allows you to view the key metrics of model services, including the traffic trend of model requests, token usage, response latency, and success rate. It can help you ensure the stability of model services, optimize resources, and troubleshoot issues.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
de OpenTrek
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Observational > Model Monitoring**.
5. On the **Model Monitoring** page, specify **Time range**, **Query granularity**, **Instance ID**,
**API**, **Model**, **Consumer**, **Routing**, and **Service** and click **Query**.

**Note**

You can also click **Reset** to clear the filter conditions.
6. The model charts are displayed in the lower part of the page.
**PV:** the total number of requests (page views) received within the specified time period.
**UV:** the number of unique visitors, which indicates the total number of requests sent by
different clients or devices.
**Fallback Request Count**: the number of requests that trigger the fallback policy. When
the primary model is unavailable, the fallback policy is triggered to use the secondary model.
**Enter the number of tokens :** the total number of tokens used for inputting text.
**Number of output tokens:** the total number of tokens used for generating results.
**Total number of tokens:** the sum of input tokens plus output tokens, which reflect the
total computing loads.
**QPS**: the number of requests processed per second.
**Request success rate**: the ratio of successful requests to total requests.
**Token consumption rate/s**: the number of tokens consumed per second, including
input tokens and output tokens.
**Average Request RT/ms**: the average response time in milliseconds. The response
time describes the time when a request is sent to the time when the result is received.
**Cache Hit/s**: the number of cache hits per second.
**Rate-limited requests/s**: the number of requests that are denied per second due to
traffic throttling.
**Model token usage statistics** : the distribution of input/output token usage of each
model.
**Consumer token usage statistics**: the token usage of each consumer in percentage.
**Service token usage statistics**: the token usage of each backend service in
percentage.
**Error Request Statistics**: the distribution of error requests, such as requests with
invalid parameters, requests that have timed out, and requests that failed to pass authentication.
**Throttling Consumer Statistics**: the distribution of consumers whose requests are
denied due to traffic throttling and the level of traffic throttling.
**Risk Type Statistics**: model calls that are labeled as high-risk behavior, such as
sensitive content generation and unauthorized access.
**Risky Consumer Statistics**: consumers with abnormal behavior, such as those that
frequently trigger the security policy and those that initiate malicious service calls.

#### MCP monitoring

OpenTrek de This topic describes how to use the Model Context Protocol (**MCP**) feature to query and analyze data in the AI Gateway console.

**Background information**

MCP monitoring is a key feature of Apsara Stack AI Gateway. It is used to observe model service calls and system performance in real time. This feature allows you to view the key metrics of model services, such as the number of API requests, response status, response latency, and success rate. It can help you analyze the stability of model services, troubleshoot exceptions, and optimize service performance.

**Procedure**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Observational > MCP Monitoring**.
5. On the **MCP Monitoring** page, specify the **Time range**, **Query granularity**, **Instance ID**,
**Consumer**, **Service**, **MCP Server**, and **MCP Tool** filter conditions and click **Query**.

**Note**

You can also click **Reset** to clear the filter conditions.
6. The MCP charts are displayed in the lower part of the page.
**PV:** the total number of requests (page views) received within the specified time period.
**UV:** the number of unique visitors, which indicates the total number of requests sent by
different clients or devices.
**Gateway Inbound Traffic:** the amount of network traffic that flows to the system
through the AI gateway. Unit: bytes.
**Gateway outbound traffic:** the amount of network traffic that flows to the client
through the AI gateway. Unit: bytes.
**Method distribution:** the percentage of API calls made by using each HTTP method,
such as GET, POST, and PUT.
**Gateway Status Code Distribution:** the distribution of status codes returned by the
gateway, such as 200, 404, and 500.
**Backend Service Status Distribution:** the distribution of status codes returned by
backend services, such as 200, 502, and 503.
**QPS**: the number of requests processed per second.
**Request success rate**: the ratio of successful requests to total requests.
**Request RT/ms**: the average response time in milliseconds. The response time
describes the time when a request is sent to the time when the result is received.
**Request Distribution**: the distribution of requests by time, such as changes in the
number of requests received per hour or per day.

### Proxy servers

This topic describes how to create and manage proxy servers.

**Background information**

| Parameter | Description |
|---|---|
| Name | The name of the proxy server. The name must be 1 to 50 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must start with a letter. _ |
| Type | Select the protocol of the proxy server. Valid values: HTTP and HTTPS. |
| Server Address | Enter the IP address or domain name of the proxy server. Example: 127.0.0.1 or proxy.example.com . |
| Server Port | Enter the port on which the proxy server listens. Example: 8080. |
| Connection timeout duration | Specify the timeout period of connections to the proxy server, in milliseconds. |

de OpenTrek Proxy servers are used to expose AI services, such as large language models (LLMs), image recognition, and speech processing services, deployed in internal or private networks without compromising the security and controllability of the AI services. Serving as a unified ingress, this feature provides the following benefits:
**Connect internal networks to external networks** : With proxy servers, external
requests can be forwarded to internal AI services by API Gateway without the need to expose the endpoints of the backend services.
**Conduct centralized service governance**: Proxy servers provide features such as route
distribution, access authentication, traffic control, logging, and call monitoring to help you manage and observe AI services.
**Enhance security**: Proxy servers can be used together with HTTPS encryption, identity
verification, and access control to isolate risks from external networks and ensure the security of AI services and data.
**Simplify integration and O&M**: Proxy servers support HTTP and HTTPS and are
compatible with mainstream AI inference frameworks. This reduces the complexity of integration and enables fast release and consistent O&M.

**Create a proxy server**

1. Log in to the AI Gateway console.
2. In the left-side navigation pane, click **AI Gateway**.
3. On the **Gateway instance** page, find the instance that you want to manage and click its ID
or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Proxy Server**.
5. On the **Proxy Server** page, click **Create a proxy server**.
6. In the **Create a proxy server** panel, configure the following parameters and click **Save**.

**Modify a proxy server**

OpenTrek de

**Note**

You cannot modify the **name** or **type** of a proxy server.
1. On the **Proxy Server** page, click **Edit** in the **Operation** column of the target proxy server.
2. In the **Edit Proxy Server** panel, modify **Server Address**, **Server Port**, and **Connection**
**timeout duration**, and click **Save**.

**Delete a proxy server**

**Important**

Before you delete a proxy server, make sure that the proxy server is not referenced by other services.
1. On the **Proxy Server** page, click **Delete** in the **Operation** column of the target proxy
server.
2. In the message that appears, click **OK**.

### Monitoring and analysis

#### View gateway log information

AI Gateway log data integrates seamlessly with Simple Log Service (SLS). This enables centralized collection, storage, and analysis of traffic logs for AI scenarios. This topic describes how to view AI Gateway log information in **SLS**.

**Prerequisites**

An AI Gateway instance is created and **Simple Log Service** is enabled. For more information, see Create a gateway instance.

**Procedure**

1. In the top menu bar, choose **Products > Storage > Storage Data Services > Simple**
**Log Service SLS** to open the Simple Log Service console.
2. In the **Project List** section, search for the cluster ID of the gateway instance.
3. Click the log project that appears in the search results to view its details.
de OpenTrek
4. In the Logstore list on the left, click **higress-gateway**. The collected log information
appears on the right.

#### View gateway monitoring metrics

AI Gateway integrates with the monitoring service to provide complete observability for core gateway metrics. This topic describes how to view gateway monitoring metrics after you enable the monitoring service.

**Prerequisites**

You have created an AI Gateway instance and selected the **Monitoring Plugin** during creation. For more information, see Create a gateway instance.

**Procedure**

1. In the top menu bar, choose **Product > Middleware > Cloud Native Observability >**
**Prometheus Monitoring 2.0** to open the Prometheus Monitoring 2.0 console.
2. In the navigation pane on the left, click Access Management. In the **Integrated**
**Environments** list on the right, search for the environment where the gateway is located.
3. Find the environment in the search results and click the environment name to open the
**Details** page.
4. On the **Details** page, click **Self-monitoring > Targets**. Find **higress-gateway-metrics**
in the list on the right. OpenTrek de
5. Expand **higress-gateway-metrics** and click the Endpoint to open the details page.
The details page that appears displays all metrics.
