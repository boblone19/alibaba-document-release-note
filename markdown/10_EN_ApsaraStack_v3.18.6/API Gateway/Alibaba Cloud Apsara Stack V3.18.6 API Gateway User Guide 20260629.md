---
title: "API Gateway User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 196
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 API Gateway User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/API%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20API%20Gateway%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# API Gateway User Guide 20260629

## Product introduction

### What is API Gateway

API Gateway is a stable, reliable, and scalable platform for service integration, API hosting, and service publication. It lets you quickly integrate new and legacy business systems and expose their services as standard APIs. API Gateway helps you manage APIs of any scale and improves development and collaboration efficiency. You can also use the microservice gateway to securely publish and share your mature business services. API Gateway provides the following features: Service integration: Connect to services using a registry for service discovery or by specifying a fixed address. API management: Manage the full lifecycle of your service APIs, including creation, editing, maintenance, testing, and unpublishing. Gateway routing: Configure gateway routes to expose services to client applications. Plugin management: Use various system plugins for features such as redirection, request header modification, retries, and parameter-based routing. Traffic shaping: Control traffic by limiting the number of incoming requests to protect your services from traffic spikes. Gateway logs: You can use the log explorer to query request logs. Each log entry shows the call time, request method, request URI, source IP, return code, duration, and request and response data. Authentication and authorization: Authenticate clients and authorize their access to APIs. Supported client authentication methods include Basic and JWT.

## Log on to the API Gateway

**console**

This topic describes how to log on to the API Gateway console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

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
**Gateway** to open the **API Gateway 2.0** console.

## Log on to the O&M console

**of ASR for Geo-disaster**

**Recovery**

This topic describes how to log on to the O&M console of ASR for Geo-disaster Recovery.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Disaster Recovery Management > ASR for Geo-disaster Recovery**.

## Getting started

### Use routes to access EDAS

**applications**

This topic describes how to call gateways. API Gateway exposes backend microservices for external calls. The backend microservices are developed with Spring Cloud and registered by using Nacos.

**Note**

Data resources on this platform are isolated by instances. Note that an instance is an abstract concept and does not refer to a specific node. An instance can have a single node or multiple nodes. In this example, an instance with a single node is used.

**Prerequisites**

The edas-demo application that contains an access path is created in the Enterprise Distributed Application Service (EDAS) console. An imported cluster resides in the same virtual private cloud (VPC) as the edas-demo application. For more information, see Import a cluster.

**Create a gateway instance**

1. Log in to the API Gateway console and create a gateway instance.
On the Gateway instance page, click **Create an instance** to access the Create API Gateway Instance page. Select a region, configure the basic and network settings, and click
**Submit**. After the instance is created, you can view the instance on the Instance List page.

**Note**

For more information about the parameter settings, see Create an instance. The following figure shows an example of creating an instance based on the EDAS deployment architecture. The selected cluster in **EDAS Configuration** must be in the same VPC as the edas-demo application in the Prerequisites section.
2. Log in to the EDAS console and configure a Server Load Balancer (SLB) instance for the
application. On the Application Details page, click **Add** next to **Server Load Balancer (Private)** in the
**Application Settings** section. When you configure the TCP protocol, set both **SLB Port**
and **Container Port** to 80, and then click **OK**.

**Create a service source**

In this example, creating a service source is optional. Go to the instance created in Create a gateway instance. Choose **Service > Source Management**, and click **Create Source**. Specify **Source Type**, **Source Name**, and **Address of Registration Centre**, and click
**Confirm**. You can view the created sources in the source list.

**Note**

For more information about the parameter settings, see Create a source.

**Create a service**

Go to the instance created in Create a gateway instance. Choose **Service > Service List**, and click **Create Service**. Specify the required parameters, and click **Submission**. You can view the created service in the service list.

**Note**

For more information about the parameter settings, see Create a service. The following example shows how to create a service named edas-demo-service. In **Node**, set **Host name/IP** and **Port** to the IP address and port number of the edas-demo application specified in Prerequisites.

**Create a route**

After you register a service on the platform, you need to expose the service through a gateway. In this case, you need to create a route for the service on the gateway. Users can visit Gateway address+Route path+Interface path to access the service. Go to the instance created in Create a gateway instance. Choose **Open Services > Route**
**Management**, and click **Create Route**. Specify **Route Name**, **Route Path**, and **Backend**
**Services**, specify the route match conditions, and click **Confirm**. You can view the created
route in the route list. The route supports exact match, placeholder match, and regular expression match.

**Note**

For more information about the parameter settings, see Create a route. In the following figure, a route named edas-demo-route is created. **Route Path** is set to `/demo/**` (regular expression match). The route is associated with the backend service edas-demo-service that has been created in Create a service. **Route Intercepting Series** must be enabled and set to 1. Leave other parameters as default. You can use `http://Gateway IP:PORT/ demo /echo/hello` to access the `/echo/hello` interface of the edas-demo-service. In the preceding example, exact route match can also be used. Specifically, **Route Path** is set to `/demo/echo/{str}` .

**Test the connectivity**

Use SLB to call the gateway. Example: `curl http://Gateway IP address: PORT/ demo`

```
/echo/hello .
```

Use API debugging for quick access. Click **Debugging** in the **Operation** column of the route created in the Create a route step, specify `/demo /echo/hello` as the access path, and click **Send**. The call is successful.

**Note**

API debugging is only used for testing. The connectivity of the actual gateway is subject to SLB calls.

### Use routes to access

**applications in an ACK cluster**

This topic describes how to access applications in a Container Service for Kubernetes (ACK) cluster by using routes in API Gateway.

**Prerequisites**

A Kubernetes cluster is created in the ACK console. For more information, see **Container**
**Service for Kubernetes User Guide > Create an ACK cluster**.

**Procedure**

**Step 1: Import a cluster**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, click **Import K8s Cluster**.
4. In the **Import to K8s cluster** panel, specify the parameters as shown in the following
figure and click **Determine**.

**Note**

For more information about the parameter settings, see Import a cluster.

**Step 2: Create a gateway instance**

1. In the left-side navigation pane, choose **API Gateway > Instance List**.
2. Click **Create an instance**.
3. Configure the parameters as shown in the following figure and click **Submit**.
**Kubernetes Cluster**: Select the imported cluster.

**Note**

For more information about the parameter settings, see Gateway instance (Kubernetes deployment architecture).

**Step 3: Obtain the IP address and port number**

Run the following command to obtain the IP address and port number of the service for external access in the `higress-system` namespace of the Kubernetes cluster:

```bash
kubectl get svc -n higress-system
```

**Step 4: Create a service**

1. In the left-side navigation pane, choose **Service Management > Service List**.
2. On the **Service List** page, click **Create Service**.
3. Configure the parameters as shown in the following figure and click **Submission**.
Enter the IP address and port number obtained in the previous step in **Host name/IP** and
**Port**, respectively.

**Note**

For more information about the parameter settings, see Create a service.

**Step 5: Create a route**

1. In the left-side navigation pane, choose **Open Services > Routing Management**.
2. On the **Route Management** page, click **Create Route**.
3. Configure the parameters as shown in the following figure and click **Confirm**.
Specify the service you created in the previous step as **Backend Services**.

**Note**

For more information about the parameter settings, see Create a route.

**Step 6: Verify the results**

1. On the **Route Management** page, find the new route and click **Debugging** in the
**Operation** column. The **API debugging** page is displayed.
2. Configure the parameters as shown in the following figure and click **Send**.

**Note**

For more information, see API debugging. t

## Instance management

### Instance list

#### Configure security group rules

If API Gateway and a backend service are in the same Virtual Private Cloud (VPC), they can communicate. However, because they are usually in different security groups, you must configure security group rules to grant API Gateway the required access permissions.

**Background information**

A security group is a virtual firewall that controls the inbound and outbound traffic of Elastic Compute Service (ECS) instances and elastic network interfaces (ENIs). This feature enhances the security of ECS instances. Security groups provide stateful inspection and packet filtering. You can use security group attributes and rules to create security domains in the cloud. For more information, see the **Elastic Compute Service User Guide > Security Group**
**Overview** topic.
API Gateway supports two deployment architectures: EDAS deployment and custom deployment. In an EDAS deployment architecture, API Gateway instances must be associated with a Container Service for Kubernetes (ACK) cluster. The gateway instance uses the VPC, vSwitch, and security group of the node pool in the ACK cluster. In a custom deployment architecture, API Gateway instances are deployed in the tenant's ACK cluster or EDAS environment. You must ensure that the security groups allow access between the nodes where the instances are deployed and the backend services. The nodes for API Gateway and the backend service are typically in different security groups. You must grant API Gateway access permissions for the required port range in the security group of the backend service. t

**Procedure**

1. Obtain the CIDR block of the node where the gateway instance is located.
i. Log on to the Container Service for Kubernetes console. In the navigation pane on the left, choose **Clusters**. ii. On the **Cluster List** page, click the name of the target cluster. Then, in the navigation pane on the left, choose **Node Management > Node Pools**. Click the name of the node pool. iii. On the **Node Pool** page, find the **Node vSwitch** ID in the **Node Configurations** section.
2. Obtain the CIDR block of the vSwitch.
i. Log on to the Virtual Private Cloud (VPC) console. In the navigation pane on the left, choose **vSwitches**. ii. On the **vSwitches** page, find the vSwitch that you obtained in Step 1 and click its ID. t iii. On the **Basic Information** tab, the value of **IPv4 CIDR Block** is the CIDR block of the vSwitch.
3. Obtain the security group of the node where the target service is located.
Upstream services associated with API Gateway are typically deployed in containers or on ECS instances. Obtain the security group ID as follows:

**Container deployment**

i. Log on to the Container Service for Kubernetes console. In the navigation pane on the left, choose **Clusters**. ii. On the **Cluster List** page, click the name of the target cluster. Then, in the navigation pane on the left, choose **Node Management > Node Pools**. Click the name of the node pool. iii. On the **Node Pool** page, find the **Security Group** ID in the **Node Pool Information** section.

**ECS deployment**

i. Log on to the Elastic Compute Service (ECS) console. ii. In the navigation pane on the left, choose **Instances & Images > Instances**. Click the ID of the ECS instance where the target service is deployed.

| Parameter | Description | Example |
|---|---|---|
| Port Range | Enter the port range for the security group rule. | 1/65535 |
| Priority | Enter the priority of the security group rule. | 1 |
| Authorization Type | Select IPv4 CIDR Block Access. | IPv4 CIDR Block Access |
| Authorization Object | Enter the CIDR block of the gateway instance's node from Step 1. | 172.16.0.2/24 |

t iii. On the **Instance Details** page, click the **Security Groups** tab to obtain the security group ID.
4. Add a security group rule.
i. Log on to the ECS console. ii. In the navigation pane on the left, choose **Network & Security > Security Groups**. Click the ID of the security group that you obtained in Step 3 for the node where the target service is located. iii. Click the **Security Group Rules** tab. In the **Inbound** section, click **Add Security Group**
**Rule**. Configure the following parameters and then click **OK**.

**FAQ**

**The security group rule is added, but the service is still**

**inaccessible. Why?**

Troubleshoot the issue as follows:
1. First, confirm that your target service is deployed on the correct node.
For example, the service might be deployed on Node A, but the security group rule is added for Node B.
2. Check if the target node is associated with multiple security groups.
If so, add the rule to each security group.

| Parameter | Description |
|---|---|
| Instance Name | The name must be 2 to 80 characters in length. It must start with a letter or a Chinese character. It can contain digits, periods (.), underscores ( ), and hyphens (-). _ |

t

**The security group is authorized, and the gateway could access**

**the service before. Why has it suddenly stopped working?**

Troubleshoot the issue as follows:
1. First, confirm that the service itself is running properly.
You can use the `curl` command from another node in the same security group to check the service connectivity.
2. Confirm whether the port exposed by your published service has changed.
For example, the port was 8080, and you authorized only port 8080 in the security group rule. If you later change the port to 8081, you must update the port in the security group rule. To avoid this issue, you can specify a wider port range, such as 1-65535, when you configure the security group rule.

#### Gateway instances (EDAS deployment

**architecture)**

**Prerequisites**

Your organization has enabled **Cloud Resource Access Authorization**.

**Create an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Click **Create Instance**.
4. Enter the configuration information and click **Submit** to create the gateway instance.

| Number Of Instance Nodes | The number of nodes for the instance. Valid values: 1 to 100. |
|---|---|
| Instance Type | The instance types provided by the platform. |
| Gateway Type | Select API Gateway. |
| Deployment Architecture | Select EDAS. |
| EDAS Configuration | You can add multiple configurations. The selected cluster must be in the same VPC as the backend service. The values in the Microservices Namespace, Cluster, and Kubernetes Namespace drop-down lists are sourced from existing data in Enterprise Distributed Application Service (EDAS). Prepare them in advance as needed. |

t
5. You can view the new gateway instance on the instance list page.

**Note**

**Instance status transitions:**

Starting: The status of an instance immediately after it is created. Running: An instance enters the Running state after it starts and reports its information to the control plane. Abnormal: If the instance fails to report within the timeout period, the status changes to Abnormal. The overview page displays basic information, a gateway overview, and endpoint information for the instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the navigation pane on the left, select **Overview**. The page includes the **Basic**
**Information** and **Endpoints** tabs.
On the **Basic Information** tab:
**Gateway Overview**: Displays the **Total Routes**, **Number of Consumers**, **Total**
**Services**, and **Total Policies**.
t
**Basic Information**: Displays the **Instance ID**, **Instance Name**, **Status**, **Deployment**
**Architecture**, **Namespace**, **Creation Time**, **Modification Time**, **Engine Type**,
**Engine Version**, and **EDAS Configuration**. Click **View** next to **EDAS Configuration**
to view the applications associated with the instance. On the **Endpoints** tab, you can view the endpoint information, including **Type**, **Network**
**Type**, **Service Name**, **External IPs**, **Ports**, and **ClusterIP**.

**Modify an instance name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. In the instance list, find the target instance. Then, click
in the **Actions** column and select **Edit**.
4. Modify the **Instance Name** and click **Submit**.

**Unregister an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. In the instance list, find the target instance. Then, click the
icon in the **Actions** column and select **Unregister** or **Force Unregister**.
4. In the **Notice** dialog box, click **OK**.

**Scale an instance**

You can scale an instance horizontally by changing the number of instance nodes or vertically by changing the instance type. This operation is performed in the EDAS console.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. In the instance list, find the target instance and click **EDAS Configuration** in the **External**
**Access** column.
4. In the **EDAS Application Management** dialog box, click the application ID to open the
EDAS console.
5. In the EDAS console, find the target application by its ID and then scale the instance. For
more information, see the **Scale Applications** section in **Enterprise Distributed**
**Application Service EDAS User Guide**.

#### Gateway instance (Kubernetes

**deployment architecture)**

This topic describes how to create and manage an API Gateway instance in a Kubernetes deployment architecture.

**Prerequisites**

**Cloud Resource Access Authorization** is enabled for the current organization.

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the API Gateway instance belongs. Important After you create the instance, you cannot change the organization for the instance. |
| Resource Set | Select the resource set for the gateway instance. You can select the default resource set or an existing one. Note You can use resource sets to categorize and manage the resources of your Alibaba Cloud account. This way, you can manage permissions, deploy resources, and monitor resources by group, without needing to handle individual resources separately. Important After you create the instance, you cannot change the resource set for the instance. |

t A Kubernetes cluster is imported. For more information, see Import a cluster.

**Create an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the page that appears, click **Create an instance**.
4. Configure the parameters described in the following table and click **Submit**.

| Region | Select the region to which the API Gateway instance belongs. Important After you create the instance, you cannot change the region for the instance. |
|---|---|
| Instance Name | The name must be 2 to 80 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. |
| Number of Instance Nodes | The number of nodes in the instance. Valid values: 1 to 100. |
| Specification | The instance type provided by API Gateway. |
| Gateway Type | Select API Gateway. |
| Deployment Architecture | Select K8s. |
| Kubernetes Cluster | Select an imported Kubernetes cluster to deploy the API Gateway instance. |
| Simple Log Service | If you select Use Simple Log Service, Simple Log Service (SLS) is activated and log shipping is enabled to help you analyze logs and visualize data on dashboards. |
| Monitoring Plugin | If you select Prometheus Monitoring, the API Gateway instances are monitored on Prometheus. |

t
5. Click **OK**. The API Gateway instance is listed on the Gateway instance page.

**Note**

**Instance status transitions:**

**Starting**: After an instance is created, its initial state is Starting.
**In operation**: After the instance starts up and reports its status, the control
plane receives the information and changes the instance state to In operation.
**Abnormal**: If the instance fails to report its status within the expected timeout
period, its state transitions to Abnormal. On the Overview page, you can view the basic information, gateway overview, and endpoint information about the instance.
1. Log in to the API Gateway console.
t
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Overview** to view the instance overview, including
**Basic information** and **Access Point**.
**Basic information** tab:
**Gateway Overview**: displays **Total routes**, **Number of consumers**, **Total number**
**of services**, and **Total Policies** of the gateway instance.
**Basic information**: displays **Instance ID**, **Instance name**, **Status**, **Deployment**
**Architecture**, **Cluster**, **Namespace**, **Creation Time**, **Modified**, and **Engine Type** of
the gateway instance.
**Access Point** tab: displays the access point information about the instance, including
**Type**, **Network Type**, **ServiceName**, **External IPs**, **Ports**, and **ClusterIP**.

**Change the name of an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the Gateway instance page, find the instance that you want to manage, click the
icon in the **Operation** column, and then select **Edit**.
4. On the page that appears, modify the **Instance name** parameter and click **Submission**.

**Deregister an instance**

**Important**

After an instance is deregistered, the instance and its data are deleted. Proceed with caution.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the Gateway instance page, find the instance that you want to manage, click the
icon in the **Operation** column, and then select **Unregister** or **Force Unregister**.
4. In the **Alert** message, click **OK**.

**Stop an instance**

If you no longer need to run a gateway instance, you can stop the instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the Gateway instance page, find the instance that you want to manage, click the
icon in the **Operation** column, and then select **Shutdown**.
4. In the message that appears, click **OK**. In the instance list, the **Instance Status** column for
the instance changes to **Shutdown**.

**Restart an instance**

If you need to continue using a gateway instance, you can restart it.

| Parameter | Description |
|---|---|
| Instance Name | The name must be 2 to 80 characters in length. It must start with a letter or a Chinese character. It can contain digits, periods (.), underscores ( ), and hyphens (-). _ |
| Number Of Instance Nodes | The number of nodes for the instance. The value can be from 1 to 100. |
| Instance Type | The instance types provided by the platform. |

t
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the Gateway instance page, find the instance that you want to manage, click the
icon in the **Operation** column, and then select **Restart**.
4. In the message that appears, click **OK**. In the instance list, the value in the **Instance**
**Status** column for the instance changes to **Running**.

#### Gateway instances (custom

**deployment architecture)**

**Prerequisites**

Your organization must have **Cloud Resource Access Authorization** enabled.

**Create an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Click **Create Instance**.
4. Enter the configuration information and click **Submit** to create the gateway instance.

| Gateway Type | Select API Gateway. |
|---|---|
| Deployment Architecture | Select Custom. |

t
5. In the instance list, you can find the created gateway instance, which has a status of **To be**
**Deployed**.

**Note**

**Instance status transitions:**

**Pending Deployment**: The instance is waiting to be deployed.
**Running**: After the instance starts, it reports its status to the control plane,
which then changes the instance state to Running.
**Abnormal**: If the instance status report times out, the state changes to
Abnormal.
6. On the **Gateway Instance** page, click the
icon in the **Actions** column of the target instance and select **View** to see the deployment details for the instance (cluster or ECS).
7. Deploy the instance.
For a cluster deployment, you need a Kubernetes cluster with network access to the console service. On a node in this cluster, create two files named service.yaml and deployment.yaml. Copy the content from the **Cluster Deployment** tab that you viewed in the previous step into these files. Then, run the following commands:

```bash
kubectl apply -f deployment.yaml kubectl apply -f service.yaml
```

For an ECS deployment, you need an ECS instance with network access to the console service. You must configure the environment variables for JDK 8. Then, copy the commands from the **ECS Deployment** tab that you viewed in the previous step and run them.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the navigation pane on the left, click **Overview**. You can view the **Basic Information**
and **Endpoints** of the instance. On the **Basic Information** tab, you can view the following information:
**Gateway Overview**: This section displays the **Number Of Consumers**, **Total**
**Routes**, **Total Services**, and **Total Policies** for the gateway instance.
**Basic Information**: This section displays the **Instance ID**, **Instance Name**, **Status**,
**Deployment Architecture**, **Namespace**, **Creation Time**, **Modification Time**,
**Engine Version**, and **Engine Type** of the gateway instance.
t
**Custom Deployment Information**: This section displays the **Deployment**, **Service**,
**Get JAR Package**, and **Deployment Command** information for the gateway instance.
On the **Endpoints** tab, you can view the **Type**, **Network Type**, **ServiceName**, **External**
**IPs**, **Ports**, and **ClusterIP** for the endpoints.

**Modify an instance name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Find the target instance, click the
icon in the **Actions** column, and select **Edit**.
4. Modify the **Instance Name** and click **Submit**.

**Unregister an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Find the target instance, click the
icon in the **Actions** column, and select **Unregister**.
4. In the **Notice** dialog box, click **OK**.

**Note**

This operation only deletes the instance data from the database. It does not delete the running instance. You must manually delete the instance from Kubernetes or ECS.
5. Delete the instance.
For a Kubernetes deployment, run the following commands to delete the instance.

```bash
kubectl delete deployment cop-broker-{Instance ID} kubectl delete service cop-broker-{Instance ID}
```

For an ECS deployment, run the following commands to find and kill the instance process to delete the instance.

```
ps -ef | grep cop-broker kill -9 {Process ID}
```

**Force unregister an instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Find the target instance, click the
icon in the **Actions** column, and select **Force**
**Logoff**.
4. In the **Notice** dialog box, click **OK**.

**Note**

This operation deletes the instance record and its data from the database. t

### Shared instances

On the Shared Instance List, you can view and manage all available shared API Gateway instances in the current organization.

**Background information**

A shared instance is an API Gateway instance that is pre-created and pre-configured by the system or an administrator. It can be shared by multiple organization units, such as departments and project teams. The superior organization can view the resources of the subordinate organization. Resources are isolated among subordinate organizations. In most cases, shared instances are deployed in public networks and support HA, high performance, and access control among multiple tenants. Shared instances are maintained by the platform. You do not need to create or maintain the underlying infrastructure. On the Overview page, you can view the basic information, gateway overview, and endpoint of the shared instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Overview** to view the overview of the instance on the
**Basic information** and **Access Point** tabs.
**Basic information** tab:
**Gateway Overview**: displays the number of **routes**, **consumers**, **services**, and
**policies** of the gateway.
**Basic information**: displays the **instance ID**, **instance name**, **status**, **deployment**
**architecture**, **namespace**, **creation time**, **modification time**, and **engine type** of
the gateway.
**Access Point** tab: displays the endpoint information about the instance in the **Type**,
**Network Type**, **ServiceName**, **External IPs**, **Ports**, and **ClusterIP** columns.

**Rename a shared instance**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. Find the shared instance that you want to rename, click the
icon in the **Operation** column, and then select **Edit**.
4. Modify the **instance name** and click **Submission**.

**Deregister a shared instance**

**Important**

After a shared instance is deregistered, the instance and its data are deleted. Proceed with caution.
1. Log in to the API Gateway console.
t
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. Find the shared instance that you want to deregister, click the
icon in the **Operation** column, and then select **Write-off** or **Force Logoff**.
4. In the **Alert** message, click **Determine**.

**Stop a shared instance**

If you do not need to run a shared instance, you can stop the shared instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. Find the shared instance that you want to stop, click the
icon in the **Operation** column, and then select **Shutdown**.
4. In the message that appears, click **Determine**. In the instance list, the status in the
**Instance Status** column changes to **Shutdown**.

**Restart a shared instance**

If you need to continue using a shared instance, you can restart the shared instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. Find the shared instance that you want to restart, click the
icon in the **Operation** column, and then select **Restart**.
4. In the message that appears, click **Determine**. In the instance list, the status in the
**Instance Status** column changes to **In operation**.

### Import management

API Gateway supports smooth migration of API definitions, group configurations, and authorization rules from the original API Gateway 1.0 to shared API Gateway instances. This reduces upgrade costs and ensures business continuity.

**Import data**

**Important**

Plug-in data import from API Gateway 1.0 is not supported. Otherwise, existing resource data is overwritten.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Import Management**.
5. On the **Data Import Management** page, click **Import data**.
6. In the **Import data** dialog box, specify the following parameters, and click **Start**
**importing**.

| Parameter | Description |
|---|---|
| Gateway instance ID | The destination gateway instance to which you want to import data. The default value is the current instance. You cannot modify the value. |
| Region ID | The ID of the region where the gateway is created. You cannot modify the value. |
| AccessKey ID/AccessKey Secret | Enter the AccessKey pair of the specified user. If this parameter is left empty, the AccessKey pair of the system is used to query resource data by default. |
| Download link | If the standardized data package has been exported before, you can set the parameter to a URL, and the system will import data from the URL. Note The HTTP and HTTPS protocols are supported. |
| Import content | Valid values: Certificate Domain name Grouping API Application |
| Enable group header | If the parameter is enabled, the request header x-apig-group-id:{groupId} is added as a routing condition when requests are forwarded. |
| Designated group | Enter group IDs. Separate multiple groups with commas (,). Note If this parameter is left empty, all groups are imported. Otherwise, the data is filtered by specified group IDs. |

t

**View the details of an import task**

t
1. (Optional) On the **Data Import Management** page, you can search for an import task by
**Task ID**, **Status**, or **Current stage**.
2. In the task list, you can view **Task ID**, **Region**, **Current stage**, **Status**, **Message**,
**Creation time**, and **Update time**.
3. Click the task ID or click **Details** in the **Operation** column to view more information,
including **Basic Information**, **Statistics**, and **Detailed information**. t

**Roll back data**

If data import fails, you can cancel the task.

**Note**

The rollback operation rolls back full data in the download link.
1. In the import task list, find the task that you want to roll back and click **Rollback** in the
**Operation** column.
2. In the message that appears, click **Confirm**.

### Service publication

#### Route groups

The service provides a default group and allows you to create custom groups. This topic describes how to create and manage route groups.

**Create route a group**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing packet**.
5. In the **Routing packet** page, click **Create a routing Group**.
6. Configure the parameters and click **Submission**.

| Parameter | Description |
|---|---|
| Group Name | Enter a name for the route group. The name can be up to 128 characters in length. |
| BasePath | The path is used as the prefix of the API path when a client application calls the API. |
| Description | Enter a description for the route group. The description can be up to 50 characters in length. |
| Default domain as a routing condition | If you enable this feature, the system automatically allocates a domain name to the route group. |
| Associated Domain Name | The domain names in the drop-down list are the associated names configured on the Domain Name Management page. |

t
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing packet**.
5. On the **Routing packet** page, you can filter route groups by **Group Name** and **Group ID**.

**View route group details**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing packet**.
5. On the **Routing packet** page, find the route group that you want to view and click the
group ID or name. Then, view the information in the **Basic information** and **Associated**
**Domain Name** sections.
**Basic information**: View the **group ID**, **group name**, **default domain name**,
**BasePath**, and **description**.
**Associated Domain Name**: View and manage the domain names associated with the
route group.

| Parameter | Description |
|---|---|

t

**Note**

In the **Associate Domain Name** section, you can click **Add** to associate a domain name with the route group.

**Modify a route group**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing packet**.
5. On the **Routing packet** page, find the route group that you want to modify and click **Edit**
in the **Operation** column.
6. Modify the information about the route group and click **Submission**.

**Delete a route group**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing packet**.
5. On the **Routing packet** page, find the route group that you want to delete and click
**Delete** in the **Operation** column.
6. In the **Alert** message, click **Determine**.

#### Route management

After you create a service, you can create routes for the service in the route management module. Routes are used to receive requests from external users and then forward the requests to backend services.

**Create a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing** page, click **Create Route**.
6. Configure the following parameters and click **Determine**.

| Routing Grouping | The route group to which the route belongs. |
|---|---|
| Route Name | The name of the route, which cannot exceed 128 characters in length. |
| Routing path | The API path to which clients send requests to call the API. You can specify multiple API paths. Exact match, placeholders, and regular expressions are supported. |
| Route Intercepting Series | After this feature is enabled, the API path of a request is truncated based on the value of this parameter before the request is forwarded to the backend service. |
| Routing Priority | When multiple routes that point to the same path exist, the route with the highest priority is used. A lower value indicates a higher priority. |
| Request Method/Request Header/Request Cookie/Request Query | Specify the request methods, headers, cookies, and query strings. Only routes that match the specified rules are used to forward traffic. |
| Route | Valid values: Single Service and Multi- service. |
| Enabled Status | Specify whether to enable or disable the route. |
| Backend Services | The backend services to be associated with the route. Note To use the multi-service canary release feature, you must specify at least two backend services. |
| Associated Domain Name | The domain name to be associated with the route group. |
| Domain Name | The backend service domain name to be associated with the route. |

t

**View the details of a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click the name of the target route to go to the
**Routing details** page. On this page, you can view the basic information and other
configuration of the route. On the **Routing Details** tab, you can view the details of the route, including **Basic**
**information**, **Associated Services**, **Associated Domain Name**, and **Enabled Status**.
Click the **Policy Configuration** tab to manage the policies bound to the route. Click **Add**
**Policy** to bind a policy to the route. For more information, see Policy management.

**Note**

In the route list, you can also click **Policy Configuration** in the **Operation** column of the target route to go to the **Policy Configuration** tab. Click the **Plugin configuration** tab to add plug-ins or manage the plug-ins of the route. Add a plug-in: Click **AddPlugin**, select a plug-in, configure the corresponding parameters as requested, and then click **Determine**.

**Note**

The configuration varies depending on the plug-in that you select. The actual parameters displayed on the page prevail. If no plug-in meets the requirements, you can add custom plug-ins. For more information, see Plugin management. Enable or disable a plug-in: Click **Enable** or **Disable** in the **Operation** column of the plug-in. In the **Alert** message, click **Determine**. Modify a plug-in: Click **Edit** in the **Operation** column of the plug-in, modify the parameters, and then click **Determine**. Remove a plug-in: Click **Delete** in the **Operation** column of the plug-in. In the **Alert** message, click **Determine**. View the details of a plug-in: Click the name of the plug-in to view the details on the page that appears. Click the **Interface Center** tab to view the details of the interfaces associated with the current route. For more information, see Interface center.

**Note**

In the route list, you can also click **Interface Center** in the **Operation** column of a route to go to the **Interface Center** tab.

**Important**

Before you create a source route, you need to create a cascade link. For more information, see Cascade links.
1. Log in to the API Gateway console.
t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click **Source route generation** in the **Operation**
column of a route.
6. In the dialog box that appears, specify **Cascade link** and click **Determine**.

**Note**

After you complete the configuration, you can choose **Cascade > Source Routing** to view the generated source route. For more information, see Source routing.

**Enable or disable a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click the
icon in the **Operation** column of a route and click **Enable** or **Disable**.

**Important**

After you disable a route, all requests forwarded based on the route will fail.
6. In the **Alert** message, click **Determine**.

**Modify a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click the
icon in the **Operation** column of a route and click **Edit** to go to the **Edit route** page.
6. On the **Edit route** page, modify the parameters and click **Determine**.

**Delete a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click the
icon in the **Operation** column of a route and click **Delete**.
6. In the **Alert** message, click **OK**.

**Delete multiple routes at a time**

You can delete routes in batches.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, select the routes that you want to delete and click
**Batch Delete**.

**Note**

Make sure that the routes you select are not associated with capabilities or released APIs. Otherwise, you fail to delete the routes. A maximum of 100 routes can be deleted at a time. If you select more than 100 routes, the batch delete operation fails.
6. In the **Alert** message, click **OK**.

**Perform route debugging**

You can perform online debugging on existing routes.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, find the route that you want to debug and click
**Debugging** in the **Operation** column to open the **API model debugging** page.
6. Configure the parameters and click **Send Request**. For more information, see API
debugging.

#### Plugin management

##### Plug-in marketplace

t The **plug-in marketplace** displays all plug-ins of the current gateway instance. You can use these plug-ins to implement different features, such as request or response rewriting and filtering and parameter mapping. Plug-ins are classified into two categories: built-in plug-ins and custom plug-ins. A built-in plug-in is provided by this service for all gateway instances. You can view its applicable scenarios and use methods on the Plugin Details page. Custom plug-ins are programmed by users. If the built-in plug-ins do not meet your requirements, you can write a custom plug-in. The following section describes how to write a custom plug-in.

**View plug-in details**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Plugin**
**market**.
5. Click the name of a plug-in to view the details of the plug-in.
**Basic information**: displays the name and type of the plug-in. You can also view the
download URL of a custom plug-in.
**Plug-in description**: describes the features and use scenarios of the plug-in.
**Configuration Fields**: lists the fields that you need to configure and whether these
fields are required.
**Usage**: displays whether the plug-in is used as a global plug-in or a routing plug-in.

**Create a custom plug-in**

This service supports custom plug-ins. You can write code and package it as a custom plug-in to add it to a gateway. First, you need to follow the instructions of the custom plug-in, write the code and package it into a JAR package, and then upload the JAR package to a storage system that is accessible to the gateway instance, such as Object Storage Service (OSS). Then, you can obtain a download URL of the JAR package. For more information, see Develop custom plugins.
1. Log in to the API Gateway console.

| Parameter | Description |
|---|---|
| Plugin name | Enter a name for the plug-in. |
| Download Address | Enter a URL that is accessible to the gateway instance, which downloads the plug-in to the on-premises device and stores the plug-in in the memory. If the gateway instance cannot access the URL, the plug-in cannot take effect. |
| Plugin description | Enter a description for the plug-in. |
| Configuration Fields | The fields must be the same as those written in the custom plug- in code. Otherwise, the fields cannot take effect. |

t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Plugin**
**market**.
5. On the **Plugin market** page, click **Create a plug-in**.
6. Configure the parameters and click **Determine**.
After the plug-in is created, the plug-in is displayed on the Plugin market page. Then, you can configure the plug-in as a global plug-in or a routing plug-in.

**Modify a custom plug-in**

You can edit custom plug-ins that are not in use, including global plug-ins and routing plugins.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Plugin**
**market**.
5. On the **Plugin market** page, move the pointer over the
icon of the plug-in card and select **Edit**. You can edit the **download URL**, **description**, and **configuration fields** of the plug-in.

**Delete a custom plug-in**

You can delete custom plug-ins that are not in use, including global plug-ins and routing plugins.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.

| Parameter | Description |
|---|---|

t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Plugin**
**market**.
5. On the **Plugin market** page, move the pointer over the
icon of the plug-in card that you want to delete, select **Delete**, and then click **Determine**.

**Add a global plug-in**

After a global plug-in is added, the plug-in applies to all routes of the current gateway instance.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Plugin**
**market**.
5. On the **Plugin market** page, move the pointer over the
icon of the plug-in card and select **Add global plugins**. For more information, see Global plug-ins.

##### Global plug-ins

The Global Plugin page displays all global plug-ins in the current gateway. After a global plugin is enabled, it takes effect on all routes of the current gateway.

**Add a global plug-in**

You can add a global plug-in from the plug-in marketplace so that it will take effect on all routes of the current gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Global**
**Plugin**.
5. On the **Global Plugin** page, click **Add global plugins**.
6. In the **Add global plugins** panel, configure the parameters and click **Determine**.

**Note**

By default, a global plug-in is disabled after it is added. For more information about how to enable a global plug-in, see Modify the status of a global plug-in.

| Plugin name | Select the global plug-in that you want to add from the plug-in marketplace. |
|---|---|
| Execution Priority | Requests may be processed by multiple plug-ins when they pass through a gateway. The order in which the plug-ins process requests is determined based on the priorities of the plug-ins. A smaller number indicates a higher priority. Valid values: 1 to 10000. Default value: 1000. |
| Configuration | Specify all plug-in parameters. |

t

**View the details of a global plug-in**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Global**
**Plugin**.
5. On the **Global Plugin** page, find the plug-in that you want to view and click its name.
6. In the **Plugin Details** panel, you can view the details of the plug-in, including **Plugin**
**name**, **Plugin type**, **Plugin description**, **Status**, **Execution Priority**, **Configuration**,
**Creation time**, and **Update time**.

**Modify the status of a global plug-in**

By default, a global plug-in is disabled after it is added.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Global**
**Plugin**.
5. On the **Global Plugin** page, find the plug-in that you want to enable and click **Enable** in
the **Operation** column. After you enable the plug-in, you can click **Disable** to disable the plug-in.

**Modify the configuration of a global plug-in**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Global**
**Plugin**.
t
5. On the **Global Plugin** page, find the plug-in that you want to modify, click **Edit** in the
**Operation** column, modify the parameters, and then click **Determine**.

**Note**

You can modify only the **Execution Priority** and **Configuration** settings of the global plug-in.

**Remove a global plug-in**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Plugin Management > Global**
**Plugin**.
5. On the **Global Plugin** page, find the plug-in that you want to remove and click **Delete** in
the **Operation** column.
6. In the **Alert** message, click **Determine**. If the plug-in is enabled, after you remove the
plug-in, it no longer takes effect.

##### Develop custom plugins

This topic describes how to develop custom plugins using the custom-plugin-demo template.

**pom.xml**

The project POM file has the following requirements: Spring Boot version: 2.4.0 Java version: 1.8 Spring Cloud version: 2020.0.0 Add the `spring-cloud-starter-gateway` dependency and set its scope to `provided`. This setting prevents the dependency from being added to the JAR package. Add other dependencies as needed. Do not set their scope to `provided`. This ensures the dependencies are included in the final JAR package. The plugin uses the assembly plugin for packaging. The configuration is shown in the example below. The following code shows an example of the POM file for the template project.

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.0</version>
    <relativePath/> <!-- lookup parent from repository -->
```

`</` `t>` t

```xml
  </parent>
  <groupId>com.example</groupId>
  <artifactId>custom-plugin-demo</artifactId>
  <version>0.0.2-SNAPSHOT</version>
  <name>custom-plugin-demo</name>
  <description>custom-plugin-demo</description>
  <properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>2020.0.0</spring-cloud.version>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-gateway</artifactId>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-dependencies</artifactId>
        <version>${spring-cloud.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>3.3.0</version>
        <executions>
          <execution>
            <id>make-assembly</id>
            <phase>package</phase>
            <goals>
              <goal>single</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <descriptors>src/main/assembly/assembly.xml</descriptors>
        </configuration>
      </plugin>
</plugins>
```

t

```
    </plugins>
  </build>
</project>
```

**Code example**

The project must contain a custom plugin class. The class must meet the following requirements: The class name must follow the format xxxGatewayFilterFactory, where xxx is the name of your custom plugin. For example, in the template project, the custom plugin is named RequestTime, so the class name is RequestTimeGatewayFilterFactory.

**Important**

The plugin name must match the name that you specify when you create the plugin in the console. Otherwise, the plugin does not work. The class must inherit the `AbstractGatewayFilterFactory` class from Spring Cloud Gateway. The class must implement a configuration class for the plugin. This must be implemented as a child class. For example, the configuration class in the template project is `RequestTimeGatewayFilterFactory$Config`. The fields in the configuration class must be of the String, Integer, or Boolean type.

**Important**

The fields in the plugin configuration class must match the configuration fields that you enter in the console. Otherwise, the configuration does not work. The class must implement the `apply` method, which returns a `GatewayFilter`. Write your custom plugin logic in the `GatewayFilter.filter` method. The following code shows an example of the custom plugin class from the template project. This RequestTime plugin calculates the backend response time of a request and adds the time to the response header. The header name is specified by the `header` configuration.

```java
package com.example.customplugindemo.filter; import org.springframework.cloud.gateway.filter.GatewayFilter; import org.springframework.cloud.gateway.filter.GatewayFilterChain; import org.springframework.cloud.gateway.filter.factory.AbstractGatewayFilterFactory; import org.springframework.web.server.ServerWebExchange; import reactor.core.publisher.Mono; import java.util.Collections; import java.util.List; public class RequestTimeGatewayFilterFactory extends AbstractGatewayFilterFactory<RequestTimeGatewayFilterFactory.Config> {
    private static final String HEADER_KEY = "header";
    private static final String REQUEST_TIME_BEGIN = "requestTimeBegin";
```

t

```java
    public RequestTimeGatewayFilterFactory() {
        super(Config.class);
    }
    @Override
    public List<String> shortcutFieldOrder() {
        return Collections.singletonList(HEADER_KEY);
    }
    @Override
    public GatewayFilter apply(Config config) {
        return new GatewayFilter() {
            @Override
            public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain
chain) {
                exchange.getAttributes().put(REQUEST_TIME_BEGIN,
System.currentTimeMillis());
                return chain.filter(exchange).then(
                        Mono.fromRunnable(() -> {
                            Long startTime = exchange.getAttribute(REQUEST_TIME_BEGIN);
                            if (startTime != null) {
                                long requestTime = System.currentTimeMillis() -
startTime; exchange.getResponse().getHeaders().add(config.getHeader(), requestTime + "ms");
                            }
                        })
                );
            }
        };
    }
    public static class Config {
        private String header;
        public String getHeader() {
            return header;
        }
        public void setHeader(String header) {
            this.header = header;
        }
    }
}
```

**Packaging**

The custom plugin project uses the assembly plugin to package dependencies into the JAR file. As shown in the pom.xml file above, the assembly configuration file is located at src/main/assembly/assembly.xml. t

```xml
<assembly xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-
plugin/assembly/1.1.2 http://maven.apache.org/xsd/assembly-1.1.2.xsd">
    <id>assembly</id>
    <formats>
        <format>jar</format>
    </formats>
    <includeBaseDirectory>false</includeBaseDirectory>
    <dependencySets>
        <dependencySet>
            <unpack>true</unpack>
            <scope>runtime</scope>
        </dependencySet>
    </dependencySets>
</assembly>
```

After you finish developing the custom plugin, run the `mvn clean package` command to package it. The output file is in the `target` directory. The file with the `assembly` suffix is the packaged result. Upload this file as the plugin JAR package.

**Upload the JAR package**

After you package the file, upload it to an object storage system. This allows the gateway data plane to download the file using a URL. This section uses Alibaba Cloud Object Storage Service (OSS) as an example to show how to upload the plugin.
1. In the top menu bar, choose **Products > Storage > Base Storage Service > Object**
**Storage Service (OSS)** to open the **Object Storage Service** console.
2. In the navigation pane on the left, click **Bucket List**.
3. On the **Bucket List** page, click the name of your bucket.
4. Click the **Object Mannagement** tab and then click **Upload Object** . Upload the JAR
package that you generated in the previous step. t

**Note**

Set the file permission to public to obtain a permanent URL for the file. The URL must not contain special characters, such as the percent sign (%). This prevents parsing errors after the gateway downloads the JAR package.

#### Signature management

The current signature management module provides the following features:

| Parameter | Description |
|---|---|

t Request anti-tampering: If the request information used for signature calculation is modified, the original signature becomes invalid and cannot pass signature verification. Signature timeliness: The request information used for signature calculation is valid only within a certain period of time. When the request information is expired, the signature cannot pass signature verification even if the request and signature information are correct. After API request signing is enabled, a client interacts with an API gateway based on the following procedure:

**Enable API request signing**

The API request signing is route-specific. After this feature is enabled for a route, only the signatures of API requests that match the route are verified. You can enable this feature when you create or modify routes.

**Create a signature plan**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Signature Management**.
5. Click **Create Signature**.
6. Configure the following parameters and click **Determine**.

| Scheme Name | Enter a name for the signature plan, which is unique within shared instance. |
|---|---|
| Signature Algorithm | The algorithm used for request information perturbation and digest generation. Valid values: HMAC-SHA1, HMAC-SHA256, and HMAC-SM3. |

t
7. On the **Signature Management** page, you can view the signature plan that you create.

**Configure a signature plan for a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Select a route and click **Policy Configuration** in the **Operation** column.
6. Click **AddStrategy**. On the **Create Policy** page, click **Signature Policy**, specify **Name**
and **Signature Strategy**, and then click **Determine**.
7. On the Policy Configuration tab, click the ID of the signature policy to view the signature
information, including **Signature Algorithm**, **Signature Key**, and **Signature Scheme**
**Status**.

**Note**

After you configure a signature plan for a route, the signature plan can be used for API request signature calculation. You can configure multiple signature plans for a route. A client only needs to initiate requests that carry any of the specified signatures.

**Enable or disable a signature plan**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Signature Management**.
5. Select the signature plan that you want to manage and click **Enable** or **Disable** in the
Operation column.
6. In the message that appears, click **Determine**.
t

**Note**

By default, the signature plan is enabled after it is created. If the SecretKey used in a signature plan is disclosed or the signature algorithm has vulnerabilities, the signature plan is no longer secure. Attackers can forge request information and exploit the signature plan to generate a signature to launch attacks. In this case, you need to disable the signature plan in a timely manner to minimize the loss. After the signature plan is disabled, requests that carry the signature can no longer pass signature verification.

**Modify a signature plan**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Signature Management**.
5. Select the signature plan that you want to modify and click **Edit** in the Operation column.
6. In the dialog box that appears, modify **Name** and click **Determine**.

**Delete a signature plan**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Signature Management**.
5. Select the signature plan that you want to delete and click **Delete** in the Operation column.
6. In the message that appears, click **Determine**.

**Note**

You can delete a signature plan only if the signature plan is disabled or not associated with any routes.

**Disable API request signing**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Select the route for which you want to disable API request signing and click **Policy**
**Configuration** in the **Operation** column.
6. Select the target signature policy and click **Disable** in the **Operation** column. In the **Alert**
message, click **Determine**.

| Field | Signature information | Description | Example |
|---|---|---|---|
| x-csb-sig-timestamp | Timestamp | The time when the request is initiated, which is used to check the validity of the signature. Unit: milliseconds. | 1654566424356 |
| x-csb-sig-expire | Expiration time | The expiration time of the request, which is used to check the validity of the signature. Unit: milliseconds. | 60000 |
| x-csb-sig-scheme | Signature plan | The ID of the signature plan configured for the route. | 85fef190-5cfe-42c6- a50c-323e6831b916 |
| x-csb-sig-white-list | Request header whitelist | The keys of headers used for signature calculation, which are separated by semicolons (;) and sorted in ASCII ascending order. | x-csb-sig-expire;x-csb- sig-scheme;x-csb-sig- timestamp |
| x-csb-sig | Signature | The signature generated based on the request information. | UiWshZ6PNWUGIpmm Qm2gnkHkGm5UIdkC7 sx23DTDDKs= |

t

**Note**

After you disable API request signing for a route, the signatures of requests that match the route are no longer verified until you enable this feature for the route again.

**Integrate API request signing**

After you enable API request signing for a route, requests that match the route must carry the specified signature to pass signature verification. To meet this goal, you must integrate API request signing with the client that initiates requests to add the signature to requests.

**Integration logic**

The request headers must carry the following signature information. Directly specify the preceding information except the signature. Calculate the signature based on the following procedure: Request information formatting. Request information perturbation.

| Parameter | Request information | Formatting |
|---|---|---|
| HttpMethod | Request type | Convert to uppercase. |
| HeaderWhiteList | Values of request header keys used for signature calculation | Convert to lowercase and sort in lexicographical ascending order. Separate multiple values with semicolons (;). |
| header | Values of keys in HeaderWhiteList | The order in which the values are sorted must be consistent with that of the keys in HeaderWhiteList. Separate multiple values with \n. Empty values are also used for signature calculation. |
| path | Request path | - |
| query | Request parameters | Sort the request parameters in lexicographical ascending order and separate multiple KV pairs with ampersands (&). |
| body | Request body | When mediatype is application/json, use the MD5 algorithm to obtain a binary array based on the JSON string and encode the array with Base64. When mediatype is application/x-www-form- urlencoded, include it in the query. When mediatype is set to other values, this parameter is left empty. |

t Digest generation based on the perturbation result. Digest encoding by using Base64. After encoding, the signature is generated.

**Request information formatting**

The following table lists the information used for signature calculation. After you obtain the preceding information, sort the information based on the following format:

```
HttpMethod + '\n' + HeaderWhiteList +'\n' + header +'\n' + path + '\n' + query + '\n' + body
```

t Sample request:

```json
curl --location --request POST 'localhost:80/test/echo' \ --header 'User-Agent: apifox/1.0.0 (https://www.apifox.cn)' \ --header 'Content-Type: application/json' \ --data-raw '{
    "id":1,
    "msg":"test"
}'
```

After the request is signed:

```
POST x-csb-sig-expire;x-csb-sig-scheme;x-csb-sig-timestamp 60000 fwj_test 1654571140853 /test/echo ewww8tc903GK8is3nD2jTA==
```

**Perturb the formatted information and generate a digest**

To prevent attackers from directly generating the signature based on the formatted information and the digest algorithm, a SecretKey is needed to perturb the formatted information. The SecretKey is generated by the backend when you create a signature plan. You can view the SecretKey in the signature plan list or the route details page. Currently, both signature algorithms support request information perturbation and digest generation. Therefore, you only need to directly select a signature algorithm. For Java, you can use the javax.crypto.Mac class to obtain the corresponding signature class instance based on the name of the signature algorithm. For more information about how to obtain the SecretKey, signature plan name, and signature algorithm, see Configure a signature plan for a route.

**Integration example - Java**

Perform the following steps to complete integration:
1. Create a signature information object based on the request information.
2. Calculate the signature and return a signature calculation result object.
Format the request information. Obtain the signature plan. Calculate the signature.
3. Add the signature calculation result object to the request information.
The code is as follows: t

```java
public abstract class AbstractApiSigFacade<T> {
    private SigCountCmdExe sigCountCmdExe;
    protected abstract SigCountCmd convertToSigCountCmd(T req);
    protected abstract T extReq(T req,RequestExtSigDTO ext);
    public T execute(T req){
        //Convert the request information to a signature information object.
        SigCountCmd sigCountCmd = convertToSigCountCmd(t);
        //Calculate the signature and return a signature calculation result object.
        SigResDTO sigResDTO = sigCountCmdExe.execute(sigCountCmd);
        //Add the signature calculation result object to the request information.
        T extSigReq = extReq(t,sigResDTO);
        return extSigReq;
    }
}
```

**Encapsulation of information related to signature calculation,**

**enumeration, and interface design**

```java
@Data public class SigCountCmd {
    private String method;
    private String path;
    private Map<String,List<String>> header;
    private Map<String,List<String>> query;
    private SigCountBodyDTO body;
}
```

Signature calculation - request body

```java
@Data public class SigCountBodyDTO {
    private String value;
    private String mediaType;
}
```

Signature information formatting class t

```java
@Data public class SigFormatMsgCmd {
    private String method;
    private String path;
    private Map<String, List<String>> header;
    private Map<String,List<String>> query;
    private SigCountBodyDTO body;
    private String sigScheme;//The name of the signature plan.
}
```

Signature plan

```java
@Data public class SigSchemeDTO {
    private String sigAlg;
    private String secretKey;
    private String sigSchemeName;
}
```

MediaType enumeration class

```java
public class MediaTypeConstant {
    private MediaTypeConstant(){}
    public static final String APPLICATION_JSON = "application/json";
    public static final String APPLICATION_FORM_URLENCODED = "application/x-www-form-ur
lencoded"; }
```

Enumeration information related to the signature information

```java
public class SigHeaderConstants {
    private SigHeaderConstants() {
    }
    public static final String HEADER_KEY_SIGN = "x-csb-sig";
    public static final String HEADER_KEY_SIGN_TIMESTAMP = "x-csb-sig-timestamp";
    public static final String HEADER_KEY_WHITE_LIST = "x-csb-sig-white-list";
    public static final String HEADER_KEY_EXPIRE = "x-csb-sig-expire";
    public static final String HEADER_KEY_SIG_SCHEME_ID = "x-csb-sig-scheme";
    public static final String DEFAULT_HEADER_WHITE_LIST = "x-csb-sig-expire;x-csb-sig-
scheme;x-csb-sig-timestamp";
    public static final Long DEFAULT_SIG_EXPIRE = 60000L;
}
```

t Interface for querying the signature plan information

```
public interface ISigSchemeOneQryExe {
    SigSchemeDTO execute(BaseSigSchemeOneQry qry);
} public interface ISigFormatMsgCmdExe {
    SigFormatDTO execute(SigFormatMsgCmd sigFormatMsgCmd);
}
```

**Calculate the signature and return the signature calculation**

**result**

Obtain the signature plan

```
/**
 *The demo used in this example is for reference only.
```

`*/`

```java
public class SigSchemeOneQryExe implements ISigSchemeOneQryExe{
    @Override
    public SigSchemeDTO execute(BaseSigSchemeOneQry qry) {
        SigSchemeDTO sigSchemeDTO = new SigSchemeDTO();
        sigSchemeDTO.setSigSchemeName("fwj_test");
        sigSchemeDTO.setSigAlg("HmacSHA256");
        sigSchemeDTO.setSecretKey("4112e422-28dc-4918-9758-c4f510bd4638");
        return sigSchemeDTO;
    }
}
```

Calculate the signature

```java
@AllArgsConstructor public class SigCountCmdExe {
    private ISigSchemeOneQryExe sigSchemeOneQryExe;
    private ISigFormatMsgCmdExe sigFormatMsgCmdExe;
    public SigResDTO execute(SigCountCmd cmd){
        SigResDTO sigResDTO = new SigResDTO();
        //Enter the logic for obtaining sigScheme.
        BaseSigSchemeOneQry baseSigSchemeOneQry = new BaseSigSchemeOneQry();
        SigSchemeDTO sigSchemeDTO = sigSchemeOneQryExe.execute(baseSigSchemeOneQry);
        //Format the information.
        SigFormatMsgCmd sigFormatMsgCmd = new SigFormatMsgCmd();
        sigFormatMsgCmd.setMethod(cmd.getMethod());
        sigFormatMsgCmd.setPath(cmd.getPath());
```

t

```java
        sigFormatMsgCmd.setHeader(cmd.getHeader());
        sigFormatMsgCmd.setQuery(cmd.getQuery());
        sigFormatMsgCmd.setBody(cmd.getBody());
        sigFormatMsgCmd.setSigScheme(sigSchemeDTO.getSigSchemeName());
        SigFormatDTO sigFormatDTO = sigFormatMsgCmdExe.execute(sigFormatMsgCmd);
        String sig = createSign(sigSchemeDTO.getSigAlg(), sigFormatDTO.getFormatMsg(),
sigSchemeDTO.getSecretKey());
        sigResDTO.setSig(sig);
        sigResDTO.setSigScheme(sigSchemeDTO.getSigSchemeName());
        sigResDTO.setExpire(sigFormatDTO.getExpire());
        sigResDTO.setTimestamp(sigFormatDTO.getTimestamp());
        sigResDTO.setHeaderWhiteList(sigFormatDTO.getHeaderWhiteList());
        return sigResDTO;
    }
    private  String createSign(
            String signType,
            String formateMsg,
            String secretKey) {
        try {
            Mac mac = Mac.getInstance(signType);
            SecretKey key = new
SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8),signType);
            mac.init(key);
            mac.update(formateMsg.getBytes(StandardCharsets.UTF_8));
            return new String(Base64.encodeBase64(mac.doFinal()),"UTF-8");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (InvalidKeyException e) {
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return null;
    }
}
```

Format the request information

```java
public class SigFormatMsgCmdExe implements ISigFormatMsgCmdExe{
    @Override
    public SigFormatDTO execute(SigFormatMsgCmd cmd) {
        SigFormatDTO sigFormatDTO = new SigFormatDTO();
        String body = getBody(cmd);
        String headerWhiteList = getHeaderWhiteList(cmd);
        Map<String, List<String>> headers = getHeaders(cmd, headerWhiteList);
        Map<String,List<String>> query = getQuery(cmd);
        //Obtain the timestamp.
        String timestamp  =
headers.get(SigHeaderConstants.HEADERKEYSIGNTIMESTAMP).get(0);
```

t _ _ _

```java
        //Obtain the expiration time.
        String expire = headers.get(SigHeaderConstants.HEADER_KEY_EXPIRE).get(0);
        String formateMsg = formateMsg(cmd.getMethod(), headerWhiteList, headers, cmd.g
etPath(), query, body);
        sigFormatDTO.setFormatMsg(formateMsg);
        sigFormatDTO.setExpire(expire);
        sigFormatDTO.setTimestamp(timestamp);
        sigFormatDTO.setHeaderWhiteList(headerWhiteList);
        return sigFormatDTO;
    }
    public  String formateMsg(
            String method,
            String headerWhiteList,
            Map<String, List<String>> header,
            String path,
            Map<String, List<String>> query,
            String body) {
        StringBuilder sb = new StringBuilder();
        return sb.append(method.toUpperCase()).append('\n')
                .append(headerWhiteList).append('\n')
                .append(getHeaderStr(header,headerWhiteList)).append('\n')
                .append(path).append('\n')
                .append(getQueryStr(query)).append('\n')
                .append(body)
                .toString();
    }
    private Map<String, List<String>> getQuery(SigFormatMsgCmd cmd) {
        Map<String, List<String>> query = cmd.getQuery();
        SigCountBodyDTO body = cmd.getBody() == null ?  new SigCountBodyDTO() :
cmd.getBody();
        //If MediaType is urlencoded, include the body in the query.
        if(MediaTypeConstant.APPLICATION_FORM_URLENCODED.equals(body.getMediaType())){
            String[] mapStrs = body.getValue().split("&");
            for (String mapStr : mapStrs) {
                String[] map = mapStr.split("=");
                query.put(map[0], Arrays.asList(map[1]));
            }
        }
        return query;
    }
    /**
     * If MediaType is application/json, use the MD5 algorithm to obtain the digest bas
ed on the JSON string.
     * If MediaType is set to other values, return an empty value.
     * @param cmd
     * @return
```

`*/`

```java
    private String getBody(SigFormatMsgCmd cmd) {
        if (cmd.getBody() != null &&
MediaTypeConstant.APPLICATION_JSON.equals(cmd.getBody().getMediaType())) {
```

t

```
            String bodyStr = cmd.getBody().getValue();
            if(StringUtils.isNotBlank(bodyStr)){
                try {
                    MessageDigest md5 = MessageDigest.getInstance("md5");
                    return
Base64.encodeBase64String(md5.digest(bodyStr.getBytes(StandardCharsets.UTF_8)));
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                }
            }
        }
        return "";
    }
    /**
     * Obtain the values of request header keys used for signature calculation.
     * The default is x-csb-sig-expire;x-csb-sig-scheme;x-csb-sig-timestamp.
     * Separate multiple values with semicolons (;) and sort them in ASCII ascending or
der.
     * @param cmd
     * @return
```

`*/`

```java
    private String getHeaderWhiteList(SigFormatMsgCmd cmd) {
        Map<String, List<String>> headerOrigin = cmd.getHeader();
        String headerWhiteList = SigHeaderConstants.DEFAULT_HEADER_WHITE_LIST;
        if (headerOrigin != null && !headerOrigin.isEmpty()) {
            List<String> v =
headerOrigin.get(SigHeaderConstants.HEADER_KEY_WHITE_LIST);
            if (v != null && !v.isEmpty()) {
                String[] keys = v.get(0).split(";");
                TreeSet<String> treeSet = new TreeSet<>();
                treeSet.add(SigHeaderConstants.HEADER_KEY_EXPIRE);
                treeSet.add(SigHeaderConstants.HEADER_KEY_SIGN_TIMESTAMP);
                treeSet.add(SigHeaderConstants.HEADER_KEY_SIG_SCHEME_ID);
                for (String key : keys) {
                    treeSet.add(key.toLowerCase(Locale.ROOT));
                }
                headerWhiteList = treeSet.stream().collect(Collectors.joining(";"));
            }
        }
        return headerWhiteList;
    }
    /**
     * Add headers.
     * If the timestamp and expiration time are not specified, the default values are u
sed.
     * @param cmd
     * @param headerWhiteList
     * @return
```

`*/`

```java
    private Map<String, List<String>> getHeaders(SigFormatMsgCmd cmd, String
headerWhiteList) {
        Map<String, List<String>> headerOrigin = new HashMap<>(cmd.getHeader());
```

t

```
        //Add a timestamp.
        if(!headerOrigin.containsKey(SigHeaderConstants.HEADER_KEY_SIGN_TIMESTAMP)){
            String timeStamp = String.valueOf(System.currentTimeMillis());
headerOrigin.put(SigHeaderConstants.HEADER_KEY_SIGN_TIMESTAMP,Arrays.asList(timeStamp));
        }
        //Add the expiration time.
        if(!headerOrigin.containsKey(SigHeaderConstants.HEADER_KEY_EXPIRE)){
headerOrigin.put(SigHeaderConstants.HEADER_KEY_EXPIRE,Arrays.asList(String.valueOf(SigHea rConstants.DEFAULT_SIG_EXPIRE)));
        }
        //Add a signature plan.
        if (!headerOrigin.containsKey(SigHeaderConstants.HEADER_KEY_SIG_SCHEME_ID)){
headerOrigin.put(SigHeaderConstants.HEADER_KEY_SIG_SCHEME_ID,Arrays.asList(cmd.getSigSche ()));
        }
headerOrigin.put(SigHeaderConstants.HEADER_KEY_WHITE_LIST,Arrays.asList(headerWhiteList))
        return headerOrigin;
    }
    /**
     * Obtain the header values based on the request header whitelist and convert them
to a string.
     * Separate multiple values with \n.
     * Separate multiple values of the same key with commas (,).
     * @param header
     * @param headerWhiteList
     * @return
```

`*/`

```java
    private String getHeaderStr(Map<String,List<String>> header,String headerWhiteList)
{
        String[] whiteList = headerWhiteList.split(";");
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < whiteList.length-1; i++){
            List<String> value = header.get(whiteList[i]);
            String str = value == null ?  "" :
value.stream().collect(Collectors.joining(","));
            sb.append(str).append('\n');
        }
        List<String> value = header.get(whiteList[whiteList.length-1]);
        String str = value == null ?  "" :
value.stream().collect(Collectors.joining(","));
        sb.append(str);
        return sb.toString();
    }
    /**
     * Format the request parameters.
*Usetheformatofpath?k1 1&k2
```

t

```
     * Use the format of path?k1=v1&k2=v2.
     * If MediaType is urlencoded, include the body information in the request paramete
rs.
     * @param query
     * @return
```

`*/`

```java
    private String getQueryStr(Map<String, List<String>> query){
        TreeMap<String,String> queryMap = new TreeMap<>();
        query.forEach((k,v)->{
            queryMap.put(k,v.stream().collect(Collectors.joining(",")));
        });
        StringBuilder sb = new StringBuilder();
        queryMap.forEach((k,v) ->{
            sb.append("&")
                    .append(k)
                    .append("=")
                    .append(v);
        });
        return sb.length() == 0 ?  "" : sb.substring(1);
    }
}
```

**Create a signature information object based on the request**

**information and add the object to requests**

ApacheHttpClient is used in this example.

```java
public class ApacheHttpClientApiSigFacade extends AbstractApiSigFacade<HttpRequestBase> {
    public ApacheHttpClientApiSigFacade(SigCountCmdExe sigCountCmdExe) {
        super(sigCountCmdExe);
    }
    @Override
    protected SigCountCmd convertToSigCountCmd(HttpRequestBase req) {
        SigCountCmd sigCountCmd = new SigCountCmd();
        sigCountCmd.setMethod(req.getMethod());
        sigCountCmd.setPath(req.getURI().getPath());
        sigCountCmd.setQuery(getQuery(req.getURI().getQuery()));
        sigCountCmd.setHeader(getHeader(req.getAllHeaders()));
        if (req instanceof HttpEntityEnclosingRequestBase){
            sigCountCmd.setBody(getBody(((HttpEntityEnclosingRequestBase)
req).getEntity()));
        }
        return sigCountCmd;
    }
    /**
     * Obtain the request body from the request information.
     * The current version supports only application/json yu.
*@paramentit
```

t

```
     * @param entity
     * @return
```

`*/`

```java
    private SigCountBodyDTO getBody(HttpEntity entity){
        SigCountBodyDTO sigCountBodyDTO = new SigCountBodyDTO();
        if (entity == null){
            return sigCountBodyDTO;
        }
        String mediaType = entity.getContentType().getValue();
        if (MediaTypeConstant.APPLICATION_JSON.equals(mediaType) ||
MediaTypeConstant.APPLICATION_FORM_URLENCODED.equals(mediaType)){
            sigCountBodyDTO.setMediaType(mediaType);
            try (BufferedReader reader = new BufferedReader(new
InputStreamReader(entity.getContent()))){
                String body = reader.readLine()
                        .lines().collect(Collectors.joining());
                sigCountBodyDTO.setValue(body);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return sigCountBodyDTO;
    }
    /**
     * Obtain the query from the request information.
     * @param qryStr
     * @return
```

`*/`

```java
    private Map<String, List<String>> getQuery(String qryStr){
        Map<String, List<String>> query = new HashMap<>();
        if (StringUtils.isNotEmpty(qryStr)) {
            String[] kvs = qryStr.split("&");
            for (String kv : kvs) {
                String[] q = kv.split("=");
                String k = q[0];
                List<String> v = q.length > 1 ?  Arrays.asList(q[1]) :
Collections.emptyList();
                query.put(k, v);
            }
        }
        return query;
    }
    /**
     * Obtain the header information from the request information.
     * @param headers
     * @return
```

`*/`

```java
    private Map<String,List<String>> getHeader(Header[] headers){
        Map<String,List<String>> map = new HashMap<>();
        for (Header header : headers) {
            map.put(header.getName(),Arrays.asList(header.getValue()));
        }
returnmap;
```

t

```
        return map;
    }
    /**
     * Add the signature calculation result to the request information.
     * @param req
     * @param ext
     * @return
```

`*/`

```java
    @Override
    protected HttpRequestBase extReq(HttpRequestBase req, SigResDTO ext) {
        req.setHeader(SigHeaderConstants.HEADER_KEY_EXPIRE,ext.getExpire());
        req.setHeader(SigHeaderConstants.HEADER_KEY_SIGN_TIMESTAMP,ext.getTimestamp());
        req.setHeader(SigHeaderConstants.HEADER_KEY_SIG_SCHEME_ID,ext.getSigScheme());
        req.setHeader(SigHeaderConstants.HEADER_KEY_SIGN,ext.getSig());
req.setHeader(SigHeaderConstants.HEADER_KEY_WHITE_LIST,ext.getHeaderWhiteList());
        return req;
    }
}
```

**Test**

Use ApacheHttpClient to initiate a request that carries the API signature.

```java
public class ApacheHttpClientRequest {
    @Test
    public void get() throws IOException {
        //Create a policy class to query the signature plan.
        SigSchemeOneQryExe sigSchemeOneQryExe = new SigSchemeOneQryExe();
        //Create a policy class to format request information.
        SigFormatMsgCmdExe sigFormatMsgCmdExe = new SigFormatMsgCmdExe();
        //Create a policy class to calculate the signature.
        SigCountCmdExe sigCountCmdExe = new SigCountCmdExe(sigSchemeOneQryExe,
sigFormatMsgCmdExe);
        //Create a class to add the signature to the request information.
        ApacheHttpClientApiSigFacade sigFacade = new
ApacheHttpClientApiSigFacade(sigCountCmdExe);
        // /api/test/ is the prefix of the route to be tested.
        String url = "http://localhost:80/api/test/test/echo/1?msg1=hello&msg2=world";
        // Create an HttpClient instance.
        HttpClient client = HttpClientBuilder.create().build();
        // Create a GET request.
        HttpGet get = new HttpGet(url);
        // Add an appId.
        get.setHeader("appId", "92d8cda0-df79-48fe-b984-cf8e867de249");
        // Add the API signature to the request.
        get = (HttpGet) sigFacade.execute(get);
        // Execute the GET request and print the request information.
        HttpResponse response = client.execute(get);
```

t p p p g

```java
        System.out.println(response.getStatusLine());
        System.out.println(EntityUtils.toString(response.getEntity(), Charsets.UTF_8));
    }
    @Test
    public void post_json() throws IOException {
        //Create a policy class to query the signature plan.
        SigSchemeOneQryExe sigSchemeOneQryExe = new SigSchemeOneQryExe();
        //Create a policy class to format request information.
        SigFormatMsgCmdExe sigFormatMsgCmdExe = new SigFormatMsgCmdExe();
        //Create a policy class to calculate the signature.
        SigCountCmdExe sigCountCmdExe = new SigCountCmdExe(sigSchemeOneQryExe,
sigFormatMsgCmdExe);
        //Create a class to add the signature to the request information.
        ApacheHttpClientApiSigFacade sigFacade = new
ApacheHttpClientApiSigFacade(sigCountCmdExe);
        String url = "http://localhost:80/api/test/test/echo";
        // Create an HttpClient instance.
        HttpClient client = HttpClientBuilder.create().build();
        // Create a POST request.
        HttpPost post = new HttpPost(url);
        // Construct POST parameters.
        Map<String, String> params = new HashMap<>();
        params.put("id", "11");
        params.put("msg", "test");
        // Convert it to JSON and configure encoding.
        StringEntity entity = new StringEntity(JSONObject.toJSON(params).toString());
        entity.setContentType("application/json");
        entity.setContentEncoding("UTF-8");
        post.setEntity(entity);
        // Add an appId.
        post.setHeader("appId", "92d8cda0-df79-48fe-b984-cf8e867de249");
        // Add the API signature to the request.
        post = (HttpPost) sigFacade.execute(post);
        // Send the request and print the response.
        HttpResponse response = client.execute(post);
        System.out.println(response.getStatusLine());
        System.out.println(EntityUtils.toString(response.getEntity(), Charsets.UTF_8));
    }
    @Test
    public void post_urlencoded() throws IOException {
        //Create a policy class to query the signature plan.
        SigSchemeOneQryExe sigSchemeOneQryExe = new SigSchemeOneQryExe();
        //Create a policy class to format request information.
        SigFormatMsgCmdExe sigFormatMsgCmdExe = new SigFormatMsgCmdExe();
        //Create a policy class to calculate the signature.
        SigCountCmdExe sigCountCmdExe = new SigCountCmdExe(sigSchemeOneQryExe,
```

| Parameter | Description |
|---|---|

t

```java
sigFormatMsgCmdExe);
        //Create a class to add the signature to the request information.
        ApacheHttpClientApiSigFacade sigFacade = new
ApacheHttpClientApiSigFacade(sigCountCmdExe);
        String url = "http://localhost:80/api/test/test/echo/form";
        // Create an HttpClient instance.
        HttpClient client = HttpClientBuilder.create().build();
        // Create an HTTP request.
        HttpPost post = new HttpPost(url);
        // Construct POST parameters.
        List<NameValuePair> params = new ArrayList<NameValuePair>();
        params.add(new BasicNameValuePair("msg", "test"));
        params.add(new BasicNameValuePair("id", "11"));
        // Convert to urlencoded media type body.
        UrlEncodedFormEntity entity = new UrlEncodedFormEntity(params);
        post.setEntity(entity);
        // Add an appId.
        post.setHeader("appId", "92d8cda0-df79-48fe-b984-cf8e867de249");
        // Add the API signature to the request.
        post = (HttpPost) sigFacade.execute(post);
        // Send the request and print the response information.
        HttpResponse response = client.execute(post);
        System.out.println(response.getStatusLine());
        System.out.println(EntityUtils.toString(response.getEntity(), Charsets.UTF_8));
    }
}
```

### Service invocation

#### Consumers

A consumer is a client. When a service API is available to a third party, the third party can call the API as a client.

**Create a consumer**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, click **Create Consumer**.
6. Configure the parameters and click **Determine**.

| Name | Enter a name for the consumer. |
|---|---|
| Description | Enter a description for the consumer. |
| Authentication Method | Valid values: API KEY, BASIC, JWT, OAuth2.0, API gateway application, and CSB authentication. For more information, see Authentication policy. |
| Token | You can use the random value generated by the system and click Refresh to generate a new random value. |
| Consumer Grouping | Add the consumer to a consumer group as needed. |

t

**Configure an authentication method for the consumer**

When you create a consumer, you must select an authentication method. You can also
**change** the authentication method of a consumer. Procedure:
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, find the consumer that you want to modify and click **Edit** in the
**Operation** column.
6. Change the **authentication method** and configure the corresponding parameters.

**Note**

In a microservices architecture, multiple services may accept requests from external clients. In most cases, you need to process requests in the gateway and use the gateway as a check point for access from external services to internal services and authenticate access requests from external users. The following authentication methods are supported: API KEY, BASIC, JWT, OAuth2.0, API gateway application, and CSB authentication.
**JSON Web Token (JWT)** is a highly lightweight specification that ensures secure
and reliable information exchange between users and servers. During the authentication process, the client obtains a JWT. Set a minimum valid period for JWTs.
**BASIC** is a relatively simple HTTP authentication method. The client transmits the
username and password in plaintext to the server for authentication. In most cases, HTTPS is used together to ensure the security of information transmission.

**View consumer details**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, filter consumers by keywords, such as **Consumer Name**, **ID**, and
**Authentication Method**.
6. Click the ID or name of the consumer that you want to view.
On the **Basic configuration** tab, view the basic information, authentication information, and consumer group of the consumer.
**Basic information**: displays the **consumer ID**, **consumer name**, **consumer**
**description**, and **consumer status**.
**Consumer Certification**: displays the consumer authentication method and
configuration information.
**Consumer Grouping**: displays the consumer groups to which the consumer is added.
On the **Consumer Authorization** tab, manage the permissions that the consumer has on APIs. For more information, see the Manage permissions section of this topic. On the **Policy Configuration** tab, you can manage policies that are attached to the consumer. You can click **Add Strategy** to attach a policy to the consumer. For more information, see Manage policies.

**Manage permissions**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, find the consumer that you want to authorize and click
**Authorization** in the **Operation** column. On the **Consumer Authorization** tab, you can
perform the following operations:
**Authorize the consumer**: You can authorize the consumer to access certain APIs.
a. On the **Consumer Authorization** tab, click **Associated Routing**. b. In the **Associated Routing** dialog box, select one or more routes and click
**Determine**.
**Revoke permissions**: You can disallow the consumer from accessing the APIs.
a. On the **Consumer Authorization** tab, click **Stop authorization** in the **Operation** column. b. In the **Alert** message, click **Determine**. After the permissions are revoked, the status in the **Authorization Status** column changes to **Unauthorized**.

**Note**

To enable the permissions for the consumer, click **Open authorization** in the
**Operation** column.
**Disassociated a route from the consumer** : After you disassociate a route from the
consumer, the consumer no longer has permissions on the APIs. a. On the **Consumer Authorization** tab, click **Delete** in the **Operation** column. t b. In the **Alert** message, click **OK**.

**Modify a consumer**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, find the consumer that you want to modify and click **Edit** in the
**Operation** column.
6. Modify the parameters and click **Determine**.

**Delete a consumer**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, find the consumer that you want to delete and click **Delete** in the
**Operation** column.
6. In the **Alert** message, click **Determine**.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Consumer**.
5. On the **Consumer** page, select the consumers that you want to delete and click **Batch**
**Delete**.
6. In the message that appears, click **Determine**.

**Note**

You can delete at most 100 consumers at the same time. The operation fails if more than 100 consumers are specified.

#### API debugging

API debugging can be used for quick and simple online testing of gateways. This topic describes how to debug an API operation.

**Online testing**

t After you create a gateway instance and add related services and routes, you can use API debugging to perform a simple and quick online test.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > API debugging**.
5. On the **API debugging** page, enter an API operation and click **Send**.

#### Authorization audit

The authorization audit feature records all application authorization and authorization modification operations in logs for archiving. This topic describes the authorization audit feature.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Invocation > Authorized audit**.
5. On the **Authorized audit** page, you can view records of authorization operations and filter
records by **name**, **consumer ID**, and **route name**.

### Service management

#### Source management

API Gateway supports the following types of sources: **Nacos, microservices namespace,**
**Eureka**, and **database**.

| Parameter | Description |
|---|---|
| Source Type | Select NACOS. |
| Source Name | Enter a source name that does not exceed 128 characters in length based on the use scenario. |
| Source Description | Enter the description of the source. |

| Parameter | Description |
|---|---|
| Address of Registration Centre | Enter node addresses and separate them with commas (,). Example: 127.0.0.1:8848. |
| Authentication Method | Valid values: Exemption from Authentication, Alibaba Cloud authentication, and Simple Authentication. |

t Before you create a service, you need to first create a source by specifying the information of the service source. This enables API Gateway to retrieve instance and service information from the specified source and manage service instances that belong to the source.

**Create a source**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Source Management**.
5. On the Source Management page, click **Create Source**. In the **Create Source** panel,
configure the parameters.

**Note**

For more information about how to create different types of sources, see Create a Nacos source, Create a microservice space source, Create an Eureka source, and Create a database source.

**Create a Nacos source**

1. In the **Create Source** panel, configure **Basic information**.
2. In the **Create Source** panel, configure **Registration Center**.

| AccessKey/SecretKey | When Authentication Method is set to Alibaba Cloud authentication, you need to specify your AccessKey pair. For more information about how to obtain the AccessKey pair, see the AccessKey pairs of a personal account topic in Apsara Uni- manager Management Console User Guide. |
|---|---|
| User Name and Password | When Authentication Method is set to Simple Authentication, you need to specify the username and password. Example: nacos and nacos. |

| Parameter | Description |
|---|---|
| Source Type | Select Microservice space. |
| Source Name | Enter a source name that does not exceed 128 characters in length based on the use scenario. |
| Source Description | Enter the description of the source. |

| Parameter | Description |
|---|---|
| Registration Center Type | Valid values: Nacos and HSF registration center. |
| Microservice space ID | You can obtain the microservices namespace ID on the Microservice Namespaces page of the Enterprise Distributed Application Service (EDAS) console. |
| AccessKey/SecretKey | You can obtain the AccessKey pair on the Microservice Namespaces page of the Enterprise Distributed Application Service (EDAS) console. |
| Connection mode | Valid values: Address Server and Direct connection. |
| Address Server Address | When Connection mode is set to Address Server, you need to enter a node IP address. |

t
3. Click **Determine**.

**Create a microservices namespace source**

1. In the **Create Source** panel, configure **Basic information**.
2. In the **Create Source** panel, configure **Registration Center**.

| Address Server Port | When Connection mode is set to Address Server, you need to enter the node port 8080. |
|---|---|
| Address of Registration Centre | When Connection mode is set to Direct connection, view the endpoint on the Configurations page of Microservice Configurations in the EDAS console. |

| Parameter | Description |
|---|---|
| Source Type | Select Eureka. |
| Source Name | Enter a source name that does not exceed 128 characters in length based on the use scenario. |
| Source Description | Enter the description of the source. |

| Parameter | Description |
|---|---|
| Source Type | Select Database. |
| Source Name | Enter a source name that does not exceed 128 characters in length based on the use scenario. |
| Source Description | Enter the description of the source. |

t
3. Click **Determine**.

**Note**

API Gateway allows you to access microservices deployed in EDAS.

**Create an Eureka source**

1. In the **Create Source** panel, configure **Basic information**.
2. In the **Create Source** panel, configure **Registration Center**.
Set **Address of Registration Centre** to a node IP address. Make sure that the IP address is valid.
3. Click **Determine**.

**Create a database source**

1. In the **Create Source** panel, configure **Basic information**.
2. In the **Create Source** panel, configure **Registration Center**.

| Parameter | Description |
|---|---|
| Data Source Type | Valid values: MySQL and PostgreSQL. |
| JDBC connection string | Enter a Java Database Connectivity (JDBC) connection string. Example: jdbc:mariadb://192.168.xxx.xxx:3306/<database name>. _ |
| User Name | Enter the username of the database. |
| Password | Enter the password of the database. |
| Maximum number of connections | Up to 1,000 connections are supported. |
| Maximum number of idle connections | Up to 1,000 idle connections are supported. |
| Connection Idle Time (seconds) | The maximum connection idle time is 1,000 seconds. |

t
3. Click **Determine**.

**Modify a source**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Source Management**.
5. In the source list, click **Edit** in the **Operation** column of the target source.
6. Modify the parameters and click **Determine**.

**Note**

API Gateway allows you to modify the configuration of sources to meet different business requirements. To ensure the stability of the downstream services of sources, API Gateway does not allow you to modify sources that are associated with downstream services.

**View the details of a source**

After you create a source, you can view the details of the source.
1. Log in to the API Gateway console.
t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Source Management**.
5. On the **Source Management** page, you can search for sources by **source name** or
**source ID**.
6. Click the ID or name of a source in the **Source ID/name** column to view the basic
information and registry center information of the source.

**Delete a source**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Source Management**.
5. On the Source Management page, click **Delete** in the **Operation** column of the target
source. In the message that appears, click **Determine**.

**Note**

To ensure the stability of the downstream services of sources, API Gateway does not allow you to modify sources that are associated with downstream services.

**Delete multiple sources at a time**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Source Management**.
5. On the Source Management page, select the sources that you want to delete and click
**Batch Delete** below the list. In the message that appears, click **Determine**.

**Note**

If any of the selected sources is associated with downstream services, the batch delete operation fails. You can delete up to 100 sources at a time. If you select more than 100 sources, the batch delete operation fails.

#### Service list

**Create a service**

1. Log in to the API Gateway console.

| Parameter | Description |
|---|---|
| Health Check Type | The request protocol supported by health check interfaces. Valid values: HTTP/HTTPS and TCP. |
| Health check path | The path for health check interfaces. Currently, only interfaces of the GET type are supported, such as /he althCheck. |
| HTTP request health code | The HTTP status code returned by health check interfaces. The gateway asserts health status based on this status code. A successful assertion indicates that the checked service is healthy. Separate multiple status codes with commas (,). Example: 200,201. |
| Request Timeout (ms) | The request timeout of health check interfaces. If no response is returned within this timeout period, the health check is considered failed. Example value: 10,000 ms. |
| Health Node Check Interval (s) | The interval at which health checks are performed on healthy nodes. For example, a value of 10 indicates that health checks are performed on healthy nodes every 10 seconds. |
| Unhealthy node check interval (s) | The interval at which health checks are performed on unhealthy nodes. For example, a value of 5 indicates that health checks are performed on unhealthy nodes every 5 seconds. |

t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. On the **Service List** page, click **Create Service**.
6. Configure the parameters and then click **Submission**.

**Note**

For more information about the parameters in the **Basic information** section, see Protocol conversion. The **Health Check** section is displayed only when you set **Service Type** to **RPC**
**service** and **Upstream Type** to **Fixed node**, or when you set **Service Type** to
**VPC**.

| Check Threshold to Health Status | The number of consecutive times that an unhealthy node passes health checks before it is declared healthy. For example, a value of 3 indicates that an unhealthy node must pass three consecutive health checks before it is declared healthy. |
|---|---|
| Check Threshold to Unhealthy State | The number of consecutive times that a healthy node fails health checks before it is declared unhealthy. For example, a value of 3 indicates that a healthy node must fail three consecutive health checks before it is declared unhealthy. |

| Parameter | Description |
|---|---|
| Name | You do not need to specify this parameter. The service name is automatically set to the name in the corresponding source. |
| Description | The description of the service. |

t

**Note**

Service types include **Fixed node** and **Service Discovery**. Before you select the
**Service Discovery** type, you must create a service source. For more information, see
Create a source. First, you need to connect the existing microservices to the gateway and provide relevant service call information. This enables the gateway to obtain service endpoints and then manage and route traffic to the interfaces exposed by these services. Currently, services can be added in two ways: From a service registry: This method can be used if the service registry has been configured as a service source in the gateway. From a fixed endpoint: If the service that you want to add cannot be found by using the service discovery mechanism, you can manually add the backend node endpoint of the service to the gateway.

**Import a service**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. On the **Service List** page, click **Import Service**.
6. Configure the parameters and then click **Submission**.

| Upstream Type | Service Discovery is specified by default. You do not need to specify this parameter. |
|---|---|
| Load balancing algorithm | Valid values: Polling and Random. |
| Source | Select a created source from the drop-down list. For more information, see Create a source. |
| Group Name | The gateway provides a default group name. You can enter a custom group name. |
| Namespace | Enter the namespace where the service resides. |
| Service not imported | The services that exist in the source. You can select the services to be imported. |
| Imported Services | You can select services in the Service not imported section and click Import to add the services to the Imported Services section. |
| Protocol Type | Valid values: HTTP, HTTPS, and Dubbo. |

t

**Modify a service**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. On the Service List page, find the service that you want to manage and click **Edit** in the
**Operation** column.
6. Modify the parameter settings and click **Submission**.

**Note**

The service configuration may change as the upstream type is modified. Therefore, you may need to modify the service by adjusting the parameters associated with the new upstream type.

**View a service**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. On the Service List page, you can filter services by **Service Name**.

**View the details of a service**

After a service is added to the gateway, you can view the service node and its health status.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. In the service list, find the service that you want to view and click its name to go to the
**Service Details** page. You can view the basic information and other configurations of the
service. On the **Service Details** tab, you can view the service details.

**Note**

In the **Basic information** section, click **Modification** to modify the description of the service. In the **Service Node** section, click the icon in the **Flow Ratio** column to modify the traffic ratio. Nodes with a 0% traffic ratio can be undeployed, and only undeployed nodes can be deleted. On the **Strategy configuration** tab, you can manage policies that are attached to the service. You can click **AddStrategy** to attach a policy to the service. For more information, see Policy management.

**Note**

On the Service List page, you can click **Strategy configuration** in the **Operation** column to go to the **Strategy configuration** tab. On the **Associated MCP** tab, you can view the information about the MCP server associated with the service, including **MCP Server Name**, **Service Type**, **Description**, and **Creation Time**.

**Delete a service**

After a service is added to the gateway, you can delete the service.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
t
5. On the Service List page, find the service that you want to manage and click **Delete** in the
**Operation** column.

**Note**

The selected service must not be associated with a route. Otherwise, the service fails to be deleted.
6. In the message that appears, click **Determine**.

**Delete multiple services in a batch**

After services are added to the gateway, you can delete the services in a batch.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Service Management > Service List**.
5. On the Service List page, select the services that you want to delete and click **Batch**
**Delete**. In the message that appears, click **Determine**.

**Note**

The selected services must not be associated with any route. Otherwise, the services fail to be deleted. You can delete at most 100 services in a batch. The deletion fails if more than 100 services are selected.

### Cascade management

#### Source routes

This topic describes how to create and manage source routes. For more information about the cascade feature and relevant terms, see Overview.

**Create a source route**

**Use scenarios**

For example, you created a **source route** named httpbin in a source gateway. Then, a
**cascade route** named cascade-httpbin is automatically created in the cascade gateway.
Users in Network B can access backend services in Network A through the cascade route.

**Procedure**

**Important**

The following operations must be performed in the console of the source gateway.
1. Log in to the API Gateway console.

| Parameter | Description |
|---|---|
| Route Name | Enter the name of the route. |
| Routing path | Specify a route path in the same way you specify a route path for a regular route. |
| Route Intercepting Series | The number of paths to be removed from the request URI before the request is sent to downstream services. |
| Route Priority | A lower value indicates a higher route priority. |
| Request Method/Request Header/Request Cookie/Request Query | Specify the request methods, headers, cookies, and query strings. Only routes that match the specified rules are used to forward traffic. If no request method is specified, all request methods match the route. |
| Backend Services | Specify backend services in the same way you specify backend services for a regular route. For more information, see Create a service or Import a service in the Service list topic. |
| Cascade link | Select a cascade link, which is the cascade gateway to which the source route is synchronized. For more information about how to create a cascade link, see the "Create a cascade link" section in the Cascade links topic. |

t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Routing**.
5. Click **Create Source Route**, configure the parameters, and then click **Determine**.

**Considerations after you create a source route**

You can view the status of cascade route synchronization on the source route details page.
**Successfully created** indicates that the route is synchronized to the cascade gateway.
**Failed to create** indicates that the system failed to create the route. You can check the
log to locate the cause. If the synchronization failure persists, modify the target cascade gateway in the **Cascading**
**Gateway** list. Click **Test Connection** and check whether you can connect to the console of
the cascade gateway. If the connection failed, troubleshoot the failure based on the error message. If the connection is created, modify the source route and try again. If the connection is created but "Synchronization failed" is still prompted, contact the developer to troubleshoot the issue. After you confirm that both the source route and the cascade route are functioning as expected, check whether the route can be used to forward requests as expected. t

**Note**

To distinguish from regular routes, the `**API gateway_cascade:true**` header match rule is added for both the source route and cascade route. Therefore, when you initiate a request, make sure that the request carries the header so that the request can match the corresponding route.

**View the details of a source route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Routing**.
5. On the **Source Routing** page, click the name of the target source route to go to the
**Source Route Details** page and view the details and configuration of the source route.
On the **Routing Details** tab, you can view the details of the source route, including
**Basic information**, **Associated Services**, and **Cascade link**.
On the **Policy Configuration** tab, you can manage the policies that are bound to the current source route. Click **Add Policy** to bind a policy to the source route.

**Note**

In the source route list, click **Policy Configuration** in the **Operation** column of the target source route to go to the **Policy Configuration** tab. The **Create Policy** page displays the available policies and labels these policies with "Support synchronization" or "Synchronization is not supported". "Support synchronization" means that the policy will be synchronized to the cascade route after the policy is created. Synchronization is not supported" means that the policy will not be synchronized to the cascade route after the policy is created. The other policy configurations are the same as creating a policy for a regular route. On the **Plugin Configuration** tab, you can add plug-ins for the current source route and manage the plug-ins of the source route. Add a plug-in: Click **Add a routing plugin**, select a plug-in, specify **Execution**
**Priority**, and then click **Determine**.

**Note**

The plug-in configuration may vary depending on the plug-in you add. The actual parameters displayed in the console prevail. If no plug-in meets the requirements, you can add custom plug-ins. For more information, see Plugin management. Plug-ins added to a source route are not synchronized to the corresponding cascade route. This means that the plug-ins take effect only on requests that match the source route. Enable or disable a plug-in: Click **Enable** or **Disable** in the **Operation** column. In the
**Alert** message, click **Determine**.
t Modify a plug-in: Click **Edit** in the **Operation** column of the target plug-in, modify the parameters, and click **Determine**. Remove a plug-in: Click **Delete** in the **Operation** column of the target plug-in. In the
**Alert** message, click **Determine**.
View the details of a plug-in: Click the name of the plug-in. In the panel that appears, you can view the plug-in details. On the **Interface Center** tab, you can view the details of interfaces associated with the source route. For more information, see Interface center.

**Note**

In the source route list, click **Interface Center** in the **Operation** column of the target source route to go to the **Interface Center** tab.

**Perform source route debugging**

You can perform online debugging on existing source routes.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Routing**.
5. On the **Source Routing** page, find the source route that you want to debug and click
**Debugging** in the **Operation** column to open the **API model debugging** page.
6. Configure the parameters and click **Send Request**. For more information, see API
debugging.

**Modify a source route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Routing**.
5. On the **Source Routing** page, select the source route you want to modify, click the
icon in the **Operation** column, and click **Edit**.
6. In the **Edit Source Route** panel, modify the parameters and click **Determine**.

**Delete a source route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Routing**.

| Parameter | Description |
|---|---|
| Name | The name of the source consumer. |
| Description | The description of the source consumer. |
| Authentication Method | Valid values: API KEY, BASIC, and JWT. For more information, see Authentication policy. |
| Token | You can use a random value generated by the platform and click Refresh to change the random value. |
| Source Consumer Group | The group to which the source consumer belongs. |

t
5. On the **Source Routing** page, select the source route you want to delete, click the
icon in the **Operation** column, and click **Delete**.
6. In the **Alert** message, click **Determine**.

#### Source consumers

This topic describes how to create and manage source consumers. For more information about the cascade feature and relevant terms, see Overview.

**Create a source consumer**

**Use scenarios**

For example, after you create a **source consumer** named consumer in the source gateway, a **cascade consumer** named cascade-consumer is automatically created in the cascade gateway. Similarly, you can authorize a **source consumer** to use a source route. After the authorization is complete, the **cascade consumer** is automatically authorized to use the cascade route in the cascade gateway.

**Procedure**

**Important**

The following operations must be performed in the console of the source gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, click **Create Source Consumer**.
6. Configure the parameters and click **Determine**.

| Cascade link | Select a cascade link to synchronize the source consumer to the selected cascade gateway. For more information about how to create a cascade link, see the "Create a cascade link" section in the Cascade links topic. |
|---|---|

t

**Source Consumer Authentication**

When you create a source consumer, you must select an authentication method. The platform also provides the **update authentication** feature.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, find the target source consumer and click **Update**
**Certification** in the **Operation** column.
6. Select a different **authentication method** and configure the parameters.

**Note**

In a microservices architecture, multiple services will receive requests from external clients. In most cases, a gateway is needed to process these requests, which serves as a controller node between external and internal services. The gateway also needs to verify the identities of external users that send the requests. The following authentication methods are supported: API key, BASIC, JWT, OAuth2.0, API gateway application, and CBS.
**JSON Web Token** (JWT): a lightweight specification that ensures secure and
reliable information transfer between users and servers. Users need to obtain a JWT to pass identity verification. The retention period of a JWT must not exceed its validity period.
**BASIC**: a simple HTTP authentication method. A client transmits the username
and password to a server for authentication in plaintext. Typically, HTTPS is required to ensure the security of information transmission.

**View the details of a source consumer**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. Optional. On the **Source consumer** page, you can search for source consumers by **name**,
**ID**, and **authentication method**.
6. Click the ID of the target source consumer to view its details.
On the **Basic configuration** tab, you can view the basic information, authentication information, group, and cascade link of the source consumer. t
**Basic information**: You can view **Source Consumer ID**, **Source Consumer Name**,
**Source Consumer Description**, and **Source Consumer Status**.
**Source Consumer Authentication**: You can view the authentication method and
relevant configuration of the source consumer.
**Source Consumer Group**: You can view the group to which the source consumer
belongs.
**Cascade link**: You can view the cascade link of the source consumer.
On the **Source Consumer Authorization** tab, you can manage the permissions of the source consumer on certain APIs. For more information, see Manage permissions.

**Manage permissions**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, find the consumer that you want to manage and click
**Authorization** in the **Operation** column. On the **Source Consumer Authorization** tab,
you can perform the following operations:
**Grant permissions to the source consumer** : You can authorize the source consumer
to access certain APIs. a. On the **Source Consumer Authorization** tab, click **Associated Source Routing**. b. In the **Associated Source Routing** dialog box, select one or more routes and click
**Determine**.
**Suspend authorization**: You can temporarily suspend the authorization that allows the
source consumer to access certain APIs. a. On the **Source Consumer Authorization** tab, click **Stop authorization** in the
**Operation** column of the source consumer.
b. In the **Alert** message, click **Determine**. The **Authorization Status** column then changes to **Unauthorized**.

**Note**

After you stop authorization, you can click **Open Authorization** in the **Operation** column of the source consumer to allow the source consumer to access the APIs again.
**Revoke permissions**: You can revoke the permissions of the source consumer on
certain APIs. a. On the **Source Consumer Authentication** tab, click **Delete** in the **Operation** column of the source consumer. b. In the **Alert** message, click **Determine**.

**Modify a source consumer**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, find the source consumer that you want to manage, click
the icon in the **Operation** column, and then click **Edit**.
6. Modify the parameters and click **Determine**.

**Delete a source consumer**

You can delete source consumers that are no longer needed.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, find the source consumer that you want to delete, click
the icon in the **Operation** column, and then click **Delete**.
6. In the **Alert** message, click **Determine**.

**Disable a source consumer**

You can disable source consumers that are not in use.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source consumer**.
5. On the **Source consumer** page, find the source consumer that you want to disable and
click **Deactivate** in the **Operation** column.

**Note**

To use a disabled source consumer, click **Enable** in the **Operation** column of the source consumer.

#### Source signatures

This topic describes how to create and manage source signatures. For more information about the cascade feature and relevant terms, see Overview.

**Create a source signature**

**Use scenarios**

For example, after you create a **source signature** named test in the source gateway, a
**cascade signature** named cascade-test is automatically created in the cascade gateway.

| Parameter | Description |
|---|---|
| Scheme Name | Enter a name. |
| Signature Algorithm | Valid values: HMAC-SHA256, HMAC-SHA1, and HMAC-SM3. |
| Cascade link | Select a cascade link to synchronize the source signature to the selected cascade gateway. For more information about how to create a cascade link, see the "Create a cascade link" section in the Cascade links topic. |

t

**Procedure**

**Important**

The following operations must be performed in the console of the source gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Signature**.
5. Click **Create Source Signature**, configure the parameters, and then click **Determine**.

**View the details of a source signature**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Signature**.
5. On the **Source Signature** page, click the ID of the source signature that you want to view.
On the Source Signature Details page, view the **basic information** about and **cascading**
**link** of the source signature.
**Basic Information**: You can view the name, ID, algorithm, key, creation time, update
time, and scheme status of the source signature.
**Cascade Link**: You can view the name, source gateway, cascade gateway, last
synchronization time, and status of the cascade link associated with the source signature.

**Enable or disable a source signature**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column. t
4. In the left-side navigation pane, choose **Cascade Management > Source Signature**.
5. On the **Source Signature** page, find the source signature that you want to manage and
click **Disable** or **Enable** in the **Operation** column.
6. In the message that appears, click **Determine**.

**Delete a source signature plan**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Signature**.
5. On the **Source Signature** page, find the source signature that you want to delete and click
**Delete** in the **Operation** column.
6. In the message that appears, click **Determine**.

**Rename a source signature**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Source Signature**.
5. On the **Source Signature** page, find the source signature that you want to rename and
click **Edit** in the **Operation** column.
6. In the dialog box that appears, modify the name of the source signature and click
**Determine**.

#### Cascade routes

This topic describes how to manage cascade routes. For more information about the cascade feature and relevant terms, see Overview.

**Prerequisites**

A source route is created in the source gateway.

**Procedure**

**Important**

The following operations must be performed in the console of the cascade gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Cascade routing**.
t
5. Optional. On the **Cascade routing** page, you can search for cascade routes by **route ID** or
**route name**.
6. In the cascade route list, you can view the ID, name, path, associated service, and creation
time of the cascade routes. Click the ID of the cascade route that you want to manage. On the **Cascade Route**
**Details** page, you can view the **basic information**, **associated services**, **policy**
**configuration**, and **interface center** of the cascade route.
Click **Interface Center** in the **Operation** column to go to the **Interface Center** tab. On this tab, you can view the API configurations of the cascade route. Click **Debugging** in the **Operation** column to go to the **API debugging** page. For more information, see API debugging.

#### Cascade consumers

This topic describes how to view cascade consumers. For more information about the cascade feature and related terms, see Overview.

**Prerequisites**

A source consumer is created on the source gateway.

**Procedure**

**Important**

You must perform the following operations in the console of the cascade gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Cascade Consumer**.
5. Optional. On the **Cascade Consumer** page, you can search for cascade consumers by
**name** or **ID**.
6. In the cascade consumer list, you can view the ID, name, status, authentication method,
creation time, and update time of each cascade consumer. Click the ID of a cascade consumer to view the basic configuration and authorization information of the cascade consumer.

#### Cascade signatures

This topic describes how to view cascade signatures. For more information about the cascade feature and relevant terms, see Overview.

**Prerequisites**

A source signature is created in the source gateway.

**Procedure**

**Important**

t The following operations must be performed in the console of the cascade gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Cascade Management > Cascading Signature**.
5. Optional. On the **Cascading Signature** page, you can filter cascade signatures by
**signature name**.
6. In the cascade signature list, you can view the ID, name, key, algorithm, signature plan
status, and creation time of each cascade signature. You can click the ID of a cascade signature to view its details, including **Cascading Signature Name**, **Cascade signature**
**ID**, **Source Gateway ID**, **Source Signature Name**, **Source Signature ID**, **Signature**
**Algorithm**, **Signature Key**, **Creation Time**, **Update time**, and **Signature Scheme**
**Status**.

### Policy management

#### Create a policy

Policies can be attached to objects and combinations of objects. For example, you can attach a traffic throttling policy to consumers, routes, or services. This facilitates API policy configuration in API Gateway.

**Background information**

API Gateway supports a variety of policies, such as IP address blacklists and whitelists, traffic throttling policies, and mock policies. API Gateway supports the following four objects: In API Gateway, only one type of policy can be attached to the same object or combination of objects. For example, only one traffic throttling policy can be attached to the same route. This topic describes several methods of creating policies and the use scenarios of each method. You can choose a method based on your business requirements. The primary method supports all types of policies, and you can use this method based on your business requirements. By default, **Scope of action** is set to **Global**. You can switch to **Local** if your business requires. The quick methods support only certain types of policies. By default, **Scope of action** is set to **Local**.

**Primary method**

We recommend that you use this method if you want to view all policy types.

**Procedure**

| Parameter | Description |
|---|---|
| Basic information |  |
| Name | Enter a name for the policy. |
| Scope of action | Global: By default, the policy is applied to the entire instance. Local: Enter the object or combination of objects to which you want to attach the policy. The available objects vary with the policy type. If you specify a combination of objects, the relationship between these objects is AND. For example, if a local policy is attached to a combination of route and consumer, the policy is executed only when a request that carries the consumer token and matches the route. For more information about objects, see Background information. |
| Policy (policy-specific) | Each policy has unique attributes. For example, you must specify information such as the authentication method for an authentication policy and the throttling threshold type for a throttling policy. For more information about how to configure the unique attributes of each policy, see Policy types. |

t
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Routing Management**. On the Policy Configuration
tab, click **Add Strategy**.
5. On the Create Policy page, click the type of policy that you want to create.

**Note**

The primary method supports all types of policies, including **Authentication Policy**,
**Flow Control Policy**, **Timeout Policy**, **Circuit Breaker Policy**, **MOCK Policy**,
**Signature Policy**, **Cross-domain Policy**, **Caching policy**, **IP Blacklist and**
**Whitelist Policy**, **Request Tracking Policy**, **ACL Permission Control Policy**, and
**HSF Protocol Mapping Policy**.
6. Configure the parameters. The default applicable scope is **Global**.

**Parameter description**

When you create a policy, you must specify the basic information about the policy and the unique attributes of the policy.

**Quick method 1**

We recommend that you use this method if you want to create a policy for a route or a combination of objects that contain a route.

**Procedure**

t
1. In the left-side navigation pane, choose **Open Services > Routing packet**.
2. On the **Strategy** page, view all routes and click the **Policy Configuration** tab.
Method 1: Click the route ID. The **Routing Details** tab appears. Click the **Policy**
**Configuration** tab.
Method 2: Find the route and click **Configure Policy** in the **Operation**.
3. On the **Policy Configuration** tab, click **Add Strategy** to go to the **Create Policy** page.

**Note**

This method supports only the following types of policies: **Authentication Policy**,
**Flow Control Policy**, **Timeout Policy**, **Circuit Breaker Policy**, **MOCK Policy**,
**Signature Policy**, **Cross-domain Policy**, **Caching Policy**, **IP Blacklist and**
**Whitelist Policy**, **ACL Permission Control Policy**, and **HSF Protocol Mapping**
**Policy**.

**Quick method 2**

We recommend that you use this method if you want to create a policy for a service or a combination of objects that contain a service.

**Procedure**

1. In the left-side navigation pane, choose **Service Management > Service List**.
2. On the Service List page, use one of the following methods to go to the **Strategy**
**configuration** tab:
Method 1: Click the service ID or name. The **Service Details** tab appears. Click the
**Strategy configuration** tab.
Method 2: Find the service and click **Strategy configuration** in the **Operation** column.
3. On the **Strategy configuration** tab, click **Add Strategy** to go to the **Create Policy** page.

**Note**

This method supports only the following types of policies: **Authentication Policy**,
**Flow Control Policy**, **Circuit Breaker Policy**, **MOCK Policy**, **Cross-domain Policy**,
**Caching Policy**, **IP Blacklist and Blacklist Policy** , **Request Tracking Policy**, and
**ACL Permission Control Policy**.

**Quick method 3**

We recommend that you use this method if you want to create a policy for a consumer or a combination of objects that contain a consumer.

**Procedure**

1. In the left-side navigation pane, choose **Service Invocation > Consumer**.
2. Click the consumer ID or name. On the **Consumer Details** page, click the **Strategy**
**configuration** tab.
3. On the **Strategy configuration** tab, click **Add Strategy** to go to the **Create Policy** page.
t

**Note**

This method supports only the following types of policies: **Flow Control Policy**,
**Circuit Breaker Policy**, **MOCK Policy**, **Caching Policy**, and **IP Blacklist and**
**Whitelist Policy**.

#### Policy lifecycle management

This topic describes how to view the configuration of a policy, change the status of a policy, modify the configuration of a policy, and delete a policy.

**View the configuration details of a policy**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Policy Management**.
5. On the **Strategy** page, you can view the configuration of all policies. You can filter policies
by **policy type**.
6. Click the ID of a policy in the **Strategy ID/name** column to view the basic information and
policy settings of the policy.

**Change the status of a policy**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Policy Management**.
5. Find the policy that you want to manage and click **Enable/Disable** in the **Operation**
column.
6. In the message that appears, click **Determine**.

**Modify the configuration of a policy**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Policy Management**.
5. Find the policy that you want to modify and click **Edit** in the **Operation** column.
6. On the **Edit Policy** page, modify the parameters and click **Determine**.

**Delete a policy**

1. Log in to the API Gateway console.

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | For more information, see the Scope of action section in Create a policy. Supported scopes are Global and Local. If you select Local, the policy can only be attached to an Route, a Service, or a combination of both. |
| Bind Route | This parameter is displayed when you set Scope of action to Local. |
| Bind Service | This parameter is displayed when you set Scope of action to Local. |
| Authentication Method | Set this parameter to API KEY. |
| Location | Supported locations are Header and Query. |
| Name | Use the default value provided by the system. |
| Remove Authentication Parameter | If you enable this option, the gateway removes the API KEY authentication parameter from the request after authentication is complete. |

t
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Policy Management**.
5. Find the policy that you want to delete and click **Delete** in the **Operation** column.
6. In the **Alert** message, click **Determine**.

#### Policy types

##### Authentication policy

###### API KEY authentication

API Gateway authentication policies support API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway application, and CSB authentication. This topic describes the API KEY authentication policy. On the page for creating an authentication policy, set **Authentication Method** to **API KEY**. The system provides default values that you can use.

| Skip Authentication For OPTIONS Requests | If you enable this option, API KEY authentication is not performed for OPTIONS requests. |
|---|---|

t

**Configure an API KEY consumer**

Configure a corresponding API KEY consumer to set the value for the API KEY.

**Note**

The procedure for configuring an API KEY source consumer is similar to configuring an API KEY consumer.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set **Authentication Method** to **API KEY** and enter a
parameter value. You can use the default random value that is generated by the system.
3. After the consumer is created, the list of consumers is displayed. In the **Operation** column,
click **Authorization**.
4. On the **Consumer Authorization** tab, clickBind **Route**. In theBind **Route** dialog box that
appears, select a **Route** and click **OK** to attach the route. Make sure that you have created an Ingress and associated it with a backend service. For more information, see Create an Ingress. After you complete the configurations, you can perform a simple test.
1. On the **Route Management** page, find the Ingress that is associated with the consumer. In
the **Operation** column, click **Debug**.
2. On the **API Debugging** interface, enter the URI of the request, select a **Consumer**, and
click **Send**. In the **Actual Request** section, you can see that the API KEY is passed in the headers when the request is sent. t Otherwise, the call fails. The following figure shows a failed authentication.

###### BASIC authentication

API Gateway authentication policies support various authentication methods, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication. This topic describes the BASIC authentication policy.

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | See Scope of action in Create a policy. The supported scopes are Global and Local. If you select Local, only Bind route, Bind Service, and a combination of these two realm objects are supported. |
| Bind Route | This parameter is displayed when you set Scope of action to Local. |
| BindService | This parameter is displayed when you set Scope of action to Local. |
| Authentication Method | Set this parameter to BASIC. |
| Token Location | Specifies the invocation credential. You can select the default system fields, Authorization or Cookie, or specify a custom field name. Regardless of the field name, you must place the field in the request header when you initiate a call. |

t When you create an authentication policy, set **Authentication Method** to **BASIC**. The system provides default values that you can use.

**Configure a BASIC consumer**

You can configure a BASIC consumer to set request values for BASIC authentication. The platform automatically generates an invocation credential for the consumer during this process.

**Note**

Configuring a BASIC source consumer is similar to configuring a BASIC consumer.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set **Authentication Method** to **BASIC**, and then enter
the **Account** and **Password**. You can use the random value that the system automatically generates for the account.
3. After the consumer is created, you are redirected to the **Consumer List** page. In the
**Operations** column, click **Grant**.
4. On the **Consumer Authorization** tab, click Bind Route. In the Bind Route dialog box that
appears, select an **Ingress** and click **OK** to attach the Ingress. Make sure that you have created a route and associated it with a backend service. For more information, see Create a route. After you complete the configuration, you can perform a simple test. t
1. On the Ingress management page, find the Ingress that is associated with the consumer. In
the **Operations** column, click **Debug**.
2. On the API Debugging interface, enter the URI of the request, select a **Consumer**, and click
**Send**.
In the **Actual Request** section, you can see that the token is passed in `header > Authorization` when the request is sent. Otherwise, the call fails. The following figure shows a failed authentication. t

**Additional information**

**Obtain a token**

In practice, the caller can obtain a token in the following ways:
1. Copy the token that is automatically generated by the platform.

| Parameter | Description |
|---|---|

t
2. Generate a token on your own. The following code provides an example. In the code, `Key`
is the account and `Password` is the password.

```
public static String createBasic(String key, String password){
        StringBuilder str = new StringBuilder(key).append(":").append(password);
        return  EncryptUtil.encryptBASE64(str.toString());
    }
```

###### JWT authentication

API Gateway supports authentication policies with the following methods: API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway application, and CSB authentication. This topic describes the JWT authentication policy. On the Create Authentication Policy page, set **Authentication Method** to **JWT**. The remaining parameters are populated with default values.

| Name | The name of the policy. You can customize the name. |
|---|---|
| Scope of action | See Scope of action in Create a policy. The supported scopes are Global and Local. When you select Local, only Bind Route, Bind Service, and a combination of these two realm objects are supported. |
| Bind route | This parameter is displayed when you set Scope of action to Local. |
| Bind Service | This parameter is displayed when you set Scope of action to Local. |
| Authentication Method | Set this parameter to JWT. |
| Token Location | Specifies the call credential. You can select the default Authorization or Cookie field, or define a custom field name. Note that regardless of the name, the field must be placed in the request header for every call. |

| Parameter | Description |
|---|---|
| Name | The name of the consumer. You can customize the name. The name can be up to 15 characters long. |
| Description | The description of the consumer. The description can be 0 to 50 characters in length. |
| Authentication Method | Set this parameter to JWT. |
| key | You can use the random value that is automatically generated by the system. |

t

**Configure a JWT consumer**

You can configure a JWT consumer to specify request values. The platform automatically generates a credential for the consumer.

**Note**

The procedure for configuring a JWT source consumer is similar to configuring a JWT consumer.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set the **Authentication Method** to **JWT** and enter a **Key**
and a **Secret**. You can use the default system-generated random value as the secret. You can also set the **Validity Period** to long-term (365 days) or short-term.

| Key | You can use the random value that is automatically generated by the system. |
|---|---|
| Validity Period | Select Long-term or Short-term. The default long-term period is 365 days. |
| Issuer | The iss (issuer) claim of the JWT. This is the entity that issued the token. Make sure the value of the iss field in the JWT payload matches the value configured here. For example: https://example.com/auth |
| Sub | The sub (subject) claim of the JWT. This is the entity that the token is about. Make sure the value of the sub field in the JWT payload matches the value configured here. If this parameter is not set or is empty, its value defaults to the value of the Issuer parameter. For example: example-app. If this parameter is not set or is empty, its value is the same as the Issuer value. |
| JWTS | The JWT public key in JSON format. |

t
3. After the consumer is created, you are redirected to the **Consumer List**. In the **Actions**
column, click **Grant**.
4. On the **Consumer Authorization** tab, click **Associate Route**. In the **Associate Route**
dialog box, select a **Route** and click **OK** to attach the route. Before you perform this step, you must create a route and associate it with a backend service. For more information, see Create a route. After you complete the configuration, you can perform a simple test.
1. On the Route Management page, find the route associated with the consumer and click
**Debug** in the **Actions** column.
2. On the API Debugging interface, you can enter the URI of the request, select a **Consumer**,
and click **Send**. t In the **Actual Request** section, you can see the token in the Authorization field of the header. Otherwise, the call fails due to an authentication failure, as shown in the following figure. t

**Additional information**

**Obtain a token**

In a real-world scenario, the caller can obtain a token in the following ways:
1. Copy the token that is automatically generated by the platform.
2. Generate a token. The following sample code shows how to generate a token. In the code,
uniqueKey is the key registered on the platform, payload is the payload, ttlMillis is the token validity period in milliseconds (ms), and secretKey is the secret. The signature algorithm is HS256, which is the only algorithm that the platform supports.

| Configuration item | Description |
|---|---|
| Name | The name of the policy. You can customize the name. |
| Scope of action | Refer to the description of Scope of action in Create a policy. The supported scopes are Global and Local. When you select Local, onlyBind route Bind Service, and a combination of these two realm objects are supported. |

t

```
public static String createJWT(String uniqueKey, JwtPayload payload, Long ttlMillis,S tring secretKey) {
    long nowMillis = System.currentTimeMillis();
    Date now = new Date(nowMillis);
    SecretKey key = generalKey(secretKey);
    JwtBuilder builder = Jwts.builder()
        .claim("appId", uniqueKey)  // The unique key of the JWT
        .setSubject(payload.getSubject())   // The subject of the JWT, which is its o
wner. This is a JSON-formatted string that can store information such as a user ID or role ID as the unique identifier of a user.
        .setIssuer(payload.getIssuer())     // The issuer is a case-sensitive URL tha
t uses the HTTP or HTTPS scheme. The URL contains the scheme, host, and optional port number and path.
        .setIssuedAt(now)      // The time when the JWT was issued
        .signWith(SignatureAlgorithm.HS256, key); // Set the signature algorithm and
the secret key used for signing
    if (ttlMillis > 0) {
        long expMillis = nowMillis + ttlMillis;
        Date expDate = new Date(expMillis);
        builder.setExpiration(expDate); // The expiration time
    }
    return builder.compact();
}
```

For information about the related dependencies, see the following code.

```xml
<dependency>
  <groupId>io.jsonwebtoken</groupId>
  <artifactId>jjwt</artifactId>
  <version>0.7.0</version>
</dependency>
```

###### OAuth 2.0 authentication

API Gateway supports several authentication policies, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication. This topic describes the OAuth 2.0 authentication policy. On the Create Authentication Policy page, set **Authentication Method** to **OAuth2.0**. You can use the default values.

| Bind route | This parameter is displayed when you set Scope of action to Local. |
|---|---|
| BindService | This parameter is displayed when you set Scope of action to Local. |
| Authentication Method | Set this parameter to OAuth2.0. |
| Token Location | The location of the access credential. The OAuth 2.0 authentication policy currently supports only Authorization. |

| Parameter | Description |
|---|---|
| Name | The name of the consumer. You can customize the name. The name can be up to 15 characters long. |
| Description | The description of the consumer. The description can be 0 to 50 characters long. |
| Authentication Method | Set this parameter to OAuth2.0. |
| Scopes | Separate multiple scopes with commas (,), for example, email,phone. |
| Type | Supports Authorization Code. |
| Token Validity Period | The unit is seconds. |
| Refresh Token Validity Period | The unit is days. |
| Client ID | The client ID, for example, oauth2-client-test. |
| Client Secret | The client secret, for example, oauth2-client-secret. |

t

**Configure an OAuth 2.0 consumer**

You can configure an OAuth 2.0 consumer to set the request values for OAuth 2.0. The platform automatically generates an access credential for the consumer.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set **Authentication Method** to **OAuth2.0** and specify
the other parameter values.

| Redirect Uris | Separate multiple URLs with commas (,), for example, https://10.4.xx.xx/xx,https://10.5.xx.xx/xx. |
|---|---|
| PKCE | Specifies whether to enable Proof Key for Code Exchange (PKCE). For better security, enable this feature. For more information, see the OAuth 2.0 standard definition. |

t
3. After the consumer is created, you are redirected to the **Consumer List**. In the **Actions**
column, click **Grant**.
4. On the **Consumer Authorization** tab, click **Associate Ingress**. In the **Associate Ingress**
dialog box, select an **Ingress** to attach and click **OK**. Ensure that you have created a route and associated it with a backend service. For more information, see Create a route.

**Debug the configuration**

After you complete the configuration, you can perform a simple test.
1. On the **Ingress Management** page, locate the Ingress associated with the consumer and
click **Debug** in the **Actions** column.
2. On the **API Debugging** page, you can enter the request URI, select the **Consumer**, and
click **Send**. In the **Actual Request** section, you can see the token passed in the `header > Authorization` field of the request, which is required to authenticate the call.

**Additional information**

**Request an authorization code**

The first step of the authorization code grant type is to request an authorization code. Send the request directly to port 8443 of the gateway broker. This example assumes that you have configured a certificate. Use the following command to request an authorization code.

```bash
curl -k -v https://${BROKER_IP}:8443/oauth2/authorize\? client_id\=${CLIENT_ID}\&redirect_uri\=http://127.0.0.1:8080/authorized\&response_type\=c e\&scope\=${SCOPE}
```

**Note**

Port 8443 accepts only HTTPS requests. You must set a certificate for the gateway. For more information, see Certificate Management. Replace all parameters with the values from your OAuth 2.0 consumer configuration. The scope parameter must be a subset of the Scopes parameter that you set on the configuration page. Replace ${BROKER_IP}, ${CLIENT_ID}, and ${SCOPE} with their actual values. In compliance with the OAuth 2.0 specification, a successful response includes the authorization code in the Location header. The following code shows a sample response: t

```
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: CN=csb.online
*  start date: Oct 19 09:36:40 2022 GMT
*  expire date: Jan 17 09:36:40 2023 GMT
*  issuer: CN=csb.online
*  SSL certificate verify result: self signed certificate (18), continuing anyway.
> GET /oauth2/authorize?
client_id=oauth&redirect_uri=http://127.0.0.1:8080/authorized&response_type=code&scope=ph e HTTP/1.1
> Host: 47.108.xx.xx:32724
> User-Agent: curl/7.64.1
> Accept: */*
```

>

```
< HTTP/1.1 200 OK < X-Content-Type-Options: nosniff < X-XSS-Protection: 1; mode=block < Cache-Control: no-cache, no-store, max-age=0, must-revalidate < Pragma: no-cache < Expires: 0 < X-Frame-Options: DENY < Location: http://127.0.0.1:8080/authorized? code=0BEfTlh6egB2QBe2_IRQFkkzRdy37p9dpB7s0kO6vsxwZ3dZCrqDoyYOnqxWEfyIADLRpsuFbazGZxp1lLWB Ny_GzNRQOmdLaCYMB2E4oo6YHHW4L_JEaKuVnPSo8k < Content-Length: 0 < Date: Wed, 19 Apr 2023 06:46:18 GMT
```

<

```
* Connection #0 to host 47.108.XX.XX left intact
* Closing connection 0
```

**Note**

The returned code is valid for 5 minutes. After it expires, you must request a new one.

**Request a token**

Use the authorization code from the Location header in the response to construct a request for an access token. The following command shows an example. t

```bash
curl -k https://${BROKER_IP}:8443/oauth2/token -H "Authorization: Basic ${TOKEN}" -X PO ST \
  --data "grant_type=authorization_code" \
  --data "client_id=${CLIENT_ID}" \
  --data "client_secret=${CLIENT_SECRET}" \
  --data "code=${CODE}" \
  --data "redirect_uri=http://127.0.0.1:8080/authorized"
```

**Note**

The Basic value for the Authorization header is the Base64-encoded value of ClientId:ClientSecret from your OAuth 2.0 consumer configuration. In this example, the Base64-encoded value of oauth2:oauth2 is b2F1dGgyOm9hdXRoMg==. You can use an online tool such as Base64 Encode and Decode to obtain the value. Replace ${BROKER_IP}, ${CLIENT_ID}, ${CLIENT_SECRET}, ${CLIENT_SECRET}, and ${TOKEN} with their actual values. A successful request for a token returns a response similar to the following. The value of the
**access_token** field is the access credential.

**Refresh a token**

If the access_token expires, you can send a refresh_token request to obtain a new access_token.

```bash
curl -k https://${BROKER_IP}:8443/oauth2/token -H "Authorization: Basic ${TOKEN}" -X PO ST \
 --data "grant_type=refresh_token" \
 --data "client_id=${CLIENT_ID}" \
 --data "client_secret=${CLIENT_SECRET}" \
 --data "refresh_token=${REFRESH_TOKEN}"
```

**Note**

The refresh_token is included in the response from the request in the "Request a token" section. Before you send the request, replace the refresh_token and other variables enclosed in ${} with their actual values.

**PKCE feature**

**Introduction to PKCE**

t PKCE stands for Proof Key for Code Exchange. It was published in 2015 as an extension to the OAuth 2.0 core protocol. It can be used with existing grant types, such as Authorization Code + PKCE, which is a best practice. PKCE was originally created for mobile and native applications to mitigate authorization code interception attacks for public clients. The latest OAuth 2.1 specification recommends that all clients, not just public clients, use PKCE. The specification also removes the Implicit and Password grant types. Clients that previously used these grant types can now use the Authorization Code grant type with PKCE. PKCE works by having the client create a proof that it sends to the authorization server. The server uses this proof to authenticate the client and issues the access token to the legitimate client, not a malicious one.

**Use PKCE**

1. On the **Consumers** page, click **Edit** in the **Actions** column.
2. On the **Edit Consumer** page, enable PKCE.
3. Generate a verifier and a challenge
t The verifier and challenge are typically generated by a program. For this demo, you can use the manual generation feature provided by a tool website.

**Note**

Click **Generate Code Verifier** and then **Generate Code Challenge** to generate the corresponding **Code Challenge**.

**Request an authorization code**

After you enable PKCE, you must include the code challenge in the request. If you send a request for an authorization code without the code challenge, an error is returned. The following code shows an example:

```bash
curl -k -v --resolve https://${BROKER_IP}:8443/oauth2/authorize\? client_id\=${CLIENT_ID}\&redirect_uri\=http://127.0.0.1:8080/authorized\&response_type\=c e\&scope\=${SCOPE}\&code_challenge\=47DEQpj8HBSa-_TImW- 5JCeuQeRkm5NMpJWZG3hSuFU\&code_challenge_method\=S256
```

**Request a token**

After you enable PKCE, you must include the code verifier when you request a token. The authorization server issues the token only after it completes the authentication. The following code shows an example:

```bash
curl -k -v https://${BROKER_IP}:8443/oauth2/token -H "Authorization: Basic ${TOKEN}" -X POST \
 --data "grant_type=authorization_code" \
  --data "client_id=${CLIENT_ID}" \
  --data "client_secret=${CLIENT_SECRET}" \
  --data "code=${CODE}" \
  --data
"code_verifier=d1SdWUti_gh~t3AVs.K3xxTxtGdhhRQTruaVDM7xb4DnXe.NP6D5QJryCTjMQOCGi1Ls_ZF2eb A0YImwRl~WfmX5mAQbYOJ.iOEzjvt8YzS06WV.XHvu0EH8YA0VIr" \
  --data "redirect_uri=http://127.0.0.1:8080/authorized"
```

**Make a call**

Use the following request with the access token to make a service call and verify that you can access the service. Note: Replace the ${ACCESS_TOKEN} placeholder with the access token value that you obtained in the previous step. Replace the other placeholders enclosed in ${} with their corresponding values.

```bash
curl -k -H "Authorization: Bearer ${ACCESS_TOKEN}" ${BROKER_IP}:${BROKER_PORT}/httpbin/get
```

| Parameter | Description | Example |
|---|---|---|
| Name | A custom name for the policy. | test |
| Scope of action | For more information about the Scope of action, see Create a policy. The options are Global and Locall. If you select Local, you can only attach the policy to a Route, a Service, or a combination of both. | Partial |
| Bind route | This parameter is displayed when you set Scope of action to Local. | - |
| BIndService | This parameter is displayed when you set Scope of action to Local. | - |
| Authentication Method | Select Custom Authentication. | Custom authentication |
| Token Location | The invocation credential. You can use the default fields Authorization or Cookie, or specify a custom field name. The field must be placed in the request header when you make a call, regardless of the field name. | Manually enter token |

t

###### Custom authentication

API Gateway supports several authentication policy methods, such as API key, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication. This topic describes custom authentication policies. A custom authentication server can be integrated with any server that provides authentication and authorization services. This demo uses Keycloak as the third-party authentication and authorization server. After you obtain the address of the third-party authentication server, configure the custom authentication settings for the route :

| Allowed header in the authentication request | If the headers specified here are present in the client request, they are added to the authentication request. The Host, Method, Path, and Content- Length headers are added by default. | Authorization |
|---|---|---|
| Allowed header in Authentication response | If the headers specified here are present in the authentication response, they are added to the client request. If a header already exists in the client request, its value is overwritten. | - |
| Authentication Service Address | The backend service used to verify the token and permissions. | - |
| Authentication API | The path of the authentication API provided by the authentication service. The API path must be a prefix match. | /realms/myrealm/protocol/openid- connect/token/introspect |
| Timeout | The maximum time to wait for a response from the authentication service, in milliseconds. The default timeout is 10,000 ms. | 10000 |
| Connection lifetime | The duration that an idle connection can remain active before it is destroyed. | 60000 |
| Mode | Strict Mode: The gateway rejects client requests if the authentication service is unavailable. Loose Mode: The gateway allows client requests if the authentication service is unavailable. | Strict mode |
| Authentication Assertion | The key in the response body that indicates a successful verification. | ResponseBody, active |
| Assertion Field Value | The value of the assertion field that indicates a successful verification. | true |

|  |  | /realms/myrealm/protocol/openid- |
|---|---|---|
| rvice. The API path must be a prefix | connect/token/introspect |  |

t

**Obtain a token**

Obtain a token based on the type of your authentication and authorization server.

**Make a call**

Run the following command to make a service call based on the configured custom authentication rule. Replace `${ACCESS_TOKEN}` with the access token obtained in the previous step. Replace other variables enclosed in `${}` with their actual values.

| Parameter | Description |
|---|---|
| Name | The name of the policy. This is user-defined. |
| Scope of action | For more information, see the Scope of action section in Create a policy. This parameter supports Global and Local. If you selectLocal only Bind route, Bind Service, and a combination of these two realm objects are supported. |
| Bind route | This parameter is displayed when you setScope of action to Local. |
| BindService | This parameter is displayed when you set Scope of action toL ocal. |

t

```bash
curl -k -X POST \
 -H "Authorization: Basic dGVzdDpVS0l0Y2lVT25oMTFpaTJnalU3QlRnbnVRYnRrcDl6Ng==" \
 -H "Content-Type: application/x-www-form-urlencoded" \
 -H "token: ${ACCESS_TOKEN}" \
${BROKER_IP}:${BROKER_PORT}/httpbin/post
```

If the authentication is successful, the service returns the following result:

###### API Gateway application authentication

API Gateway supports authentication policies such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway application, and CSB authentication. This topic describes the API Gateway application authentication policy.

**Configure an API Gateway application authentication policy**

The API Gateway application authentication policy is compatible with the authentication method used in the original API Gateway. This policy is intended for use only when you migrate from the original API Gateway to the current gateway. On the Create Authentication Policy page, set **Authentication Method** to **API Gateway**
**Application**. The system provides the required parameter values.

| Authentication Method | Select API Gateway Application. |
|---|---|
| AppCode Authentication | You can select one of three options: Disable AppCode Authentication, Allow AppCode Authentication (Header), or Allow AppCode Authentication (Header&Query). The meanings of these options are the same as in the original API Gateway. |

| Parameter | Description |
|---|---|
| App Key | Enter the identity of the application. |
| App Secret | Enter the application key. |
| App Code | Enter the application code. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |

t To use API Gateway application authentication, you must configure the corresponding consumers and set their parameter values.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set **Authentication Method** to **API Gateway**
**Application** and enter the parameter values. You can use the default random values that
the system generates.
3. After the consumer is created, you are redirected to the consumer list. Click **Authorization**
in the **Actions** column.
4. On the **Consumer Authorization** tab, click **Associate Route**. In the **Associate Route**
dialog box, select a **Route** and click **OK** to associate the route. You must first create an ingress and associate it with a backend service. For more information, see Create an ingress.

###### CSB authentication

API Gateway authentication policies support several authentication methods, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication. This topic describes the CSB authentication policy. On the Create Authentication Policy page, set **Authentication Method** to **CSB**
**Authentication** and configure the parameters.

| Scope of action | Refer to Applicable Scope in Create a policy. The supported scopes are Global and Local. If you select Local, the policy applies only to Attach Ingress, Attach Service, and a combination of these two realm objects. |
|---|---|
| Bind route | This parameter appears when you set Applicable Scope to Specific Realm. |
| BindService | This parameter appears when you set Applicable Scope to Specific Realm. |
| Authentication Method | Set this to CSB Authentication. |

| Parameter | Description |
|---|---|
| Name | The name of the policy. This is user-defined. |
| Scope of action | See Scope of action in Create a policy. The supported scopes are Global and Local. If you select Local, a combination of Bind Route, Bind Service, Bind Consumer, and any realm objects is supported. |

t You can configure consumers to set request values for the API Gateway application.
1. On the **Consumers** page, click **Create Consumer**.
2. On the **Create Consumer** page, set **Authentication Method** to **CSB Authentication**. An
AppSecret is generated by default.
3. After the consumer is created, you are redirected to the consumer list. In the **Actions**
column, click **Grant**.
4. On the **Consumer Authorization** tab, click **Associate Ingress**. In the **Associate Ingress**
dialog box, select an **Ingress** and click **OK** to attach the Ingress. You must first create a route and associate it with a backend service. For more information, see Create a route.

##### Throttling policies

This topic describes how to configure throttling policies.

**Configure a throttling policy**

You can use throttling policies to limit the rate of requests. To create a throttling policy, specify the configuration items on the creation page. When you enable throttling for the Client IP or Remote Host properties, the gateway throttles all requests based on their source IP address or host. For other properties, such as Header, URL parameter, or Cookie, you can specify matching parameters. In this case, only requests that meet the specified conditions are throttled.

| Request Property Matching | When enabled, you can configure the following Parameter Properties: Client IP: When enabled, throttles all client IP addresses. Remote Host: When enabled, throttles all client hosts. Header: When enabled, throttles requests based on matching request header parameters. The Match Pattern can be Exact, Regex, or Substring. URL Parameter: When enabled, throttles requests based on matching URL parameters. The Match Pattern can be Exact, Regex, or Substring. Cookie: When enabled, throttles requests based on matching Cookie parameters. The Match Pattern can be Exact, Regex, or Substring. |
|---|---|
| Threshold Type | The supported types are QPS and Thread. |
| Request Count Threshold | This parameter is displayed when you set Threshold Type to QPS. It specifies the maximum number of requests allowed per unit of time. Requests that exceed this number are rejected. |
| Throttling Mode | This parameter is displayed when you set Threshold Type to QPS. The supported modes are Uniform Queuing and Fast Queuing. |
| Timeout Period | This parameter is displayed when you set Throttling Mode to Uniform Queuing. Requests are queued. If a request waits in the queue for too long, it fails. |
| Burst Traffic | This parameter is displayed when you set Throttling Mode to Fast Queuing. It specifies the maximum traffic allowed during a burst. Requests that exceed this limit are rejected. |
| Thread Count | The limit on the number of concurrent threads at any given moment. |

t

**Throttling policy examples**

The following examples show how to throttle requests by matching the Header, URL parameter, and Cookie properties.

**Throttle by request header**

You can throttle requests by matching specific fields in the HTTP request header. You can set matching rules using exact match, regular expression (regex) match, or substring match.

**Example 1: Exact match**

Match pattern: Exact match Header name: X-Forwarded-For Match string: 192.168.0.1 This throttles requests where the X-Forwarded-For request header has a value of 192.168.0.1.

**Example 2: Regex match**

t Match pattern: Regex match Header name: X-Forwarded-For Match string: ^(192.168.).* This throttles requests where the X-Forwarded-For request header starts with 192.168.

**Example 3: Substring match**

Match pattern: Substring match Header name: X-Forwarded-For Match string: 192.168 This throttles requests where the X-Forwarded-For request header contains the substring 192.168.

**Throttle by URL parameter**

You can throttle requests by matching specific URL parameters in the HTTP request. You can set matching rules using exact match, regex match, or substring match.

**Example 1: Exact match**

Match pattern: Exact match URL parameter name: user_id Match string: 123456 This throttles requests where the user_id is 123456.

**Example 2: Regex match**

To match all user IDs that start with 1, use the following settings: Match pattern: Regex match URL parameter name: user_id Match string: ^1.* This throttles all requests where the user_id starts with 1.

**Example 3: Substring match**

To match all user IDs that contain 123, use the following settings: Match pattern: Substring match URL parameter name: user_id Match string: 123 This throttles requests where the user_id contains 123.

**Throttle by Cookie parameter**

You can throttle requests by matching specific cookies in the HTTP request. You can set matching rules using exact match, regex match, or substring match.

**Example 1: Exact match**

Match pattern: Exact match Cookie name: session_id Value: 123 This throttles requests where the session_id cookie has a value of 123.

**Example 2: Regex match**

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | For more information, see Scope of action in Create a policy. Global and local scopes are supported. When you select Local, a combination of Attach Route, Attach Service, Attach Consumer, and any realm objects is supported. |
| Timeout | The timeout for connecting to the backend. The default is 20 s. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | For more information, see Scope of action in Create a policy. The scope can be Global or Local. If you select Local, a combination of Attach Route, Attach Service, Attach Consumer, and any realm objects is supported. |

t Match pattern: Regex match Cookie name: session_id Value: ^1.* This throttles requests where the value of the session_id cookie starts with 1.

**Example 3: Substring match**

Match pattern: Substring match Cookie name: session_id Value: 123 This throttles requests where the value of the session_id cookie contains the substring 123.

##### Timeout policy

On the Create Timeout Policy page, specify the parameters for the policy.

##### Circuit breaker policy

On the Create Circuit Breaker Policy page, set the parameters and create the policy.

| Fault Conditions | Backend Response Time: The response time for a request to a route. Ratio Threshold: The ratio of requests that meet the fault condition. The value must be greater than 0 and less than 1. Judgment time window:: The time window for counting successful circuit breaker assertions. Breaker Duration: The duration for which the circuit breaker remains open. Minimum Requests: The system checks for faults only after the number of requests reaches this minimum value. |
|---|---|
| Degradation Policy | Default: The platform provides a default degradation policy. Mock: If you configure Mock, you can set the Response Code, Response Header, and Response Body. When the circuit breaker is triggered, the system returns the configured mock response. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Applicable Scope | For more information, see the Applicable Scope section in Create a policy. Both global and local scopes are supported. When you select Local, you can use a combination of Attach Route, Attach Service, Attach Consumer, and any realm objects. |
| Mock Policy | You can set the Response Code, Response Header, and Response Body. When circuit breaking is triggered, the system returns a response based on the mock configuration. |

| Parameter | Description |
|---|---|

t

##### Mock policy

After you enable a mock policy, the gateway no longer sends requests to the backend. Instead, it returns mock information directly to the client. On the Create Mock Policy page, set the parameters and then create the policy.

##### Signature Scheme

**Configure a signing policy**

On the Create Signing Policy page, you can specify the configuration items to create the policy.

| Name | A custom name for the policy. |
|---|---|
| Scope of action | For more information, see the Scope of actionparameter in Create a policy. The scope can be global or realm-specific. If you select Local, you can attach the policy to a combination of Route, Services, Consumers, and any realm objects. |
| Signature Scheme | Select a signing scheme. For more information, see Signing management. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | Refer to the Scope of action section in Create a policy. Global and local scopes are supported. If you select Local, only Bind Route, Bind Service, and a combination of these two realm objects are supported. |
| Cross-domain Type | Supported types are CORS and JSONP. |
| Source | This parameter is displayed when you set Cross-domain Type to CORS. The Origin, which is the endpoint of the caller. It consists of a protocol, domain name, and port. Example: http://httpbin:80.org. |
| Request Type | This parameter is displayed when you set Cross-domain Type to CORS. Supported methods: GET, POST, PUT, DELETE, HEAD, PATCH, and OPTIONS. |
| Pass Cookie | This parameter is displayed when you set Cross-domain Type to CORS. You can select Allow or Forbid. If the source is set to all (by entering *), you cannot pass cookies. |

t

##### Cross-domain policies

Cross-domain policies allow you to dynamically configure cross-domain capabilities for connected services. This feature supports Cross-Origin Resource Sharing (CORS) and JSON with Padding (JSONP).

**Configure a cross-domain policy**

On the Create Cross-domain Policy page, specify the configuration items to create the policy.

| Expose-Headers | This parameter is displayed when you set Cross-domain Type to CORS. During cross-origin access, the getResponseHeader() method of the XMLHttpRequest object can only access basic response headers, such as Cache-Control, Content-Language, Content-Length, Content- Type, Expires, Last-Modified, and Pragma. To access other headers, configure Expose-Headers. For example, to get the x-csb-caching response header, add x-csb-caching. |
|---|---|
| Allow-Headers | This parameter is displayed when you set Cross-domain Type to CORS. Specifies the request headers that are allowed in the request. To allow all request headers, enter *. |
| Pre-Check Cache Time | This parameter is displayed when you set Cross-domain Type to CORS. The browser caches the information from a successful preflight request. Modifying this configuration does not purge the browser cache. Configure this parameter with care. |
| Callback function name | This parameter is displayed when you set Cross-domain Type to JSONP. This name corresponds to the parameter carried in the request. Note: The callback function name cannot be the same as any backend API parameter names. |

t

**Cross-domain policy examples**

**CORS cross-domain requests**

Configuration: Allow all sources. Do not allow cookies to be sent. Allow any request headers. Allow the frontend to access only the CORS response headers.

**Allow requests to carry cookies**

Scenario: Requests need to include cookies, and the frontend service has a specific endpoint. Configuration: In the source field, enter the frontend service endpoint. If you have multiple endpoints, separate them with commas (,). Select the option that allows cookies to be sent.

**Restrict allowed request headers**

Scenario: You need to restrict the request headers that the frontend can send to the backend to a specific list of allowed headers. Configuration: In the Allow-Headers field, enter the allowed request headers. If you have multiple headers, separate them with commas (,).

**Allow the frontend to get custom response headers**

Scenario: The frontend needs to access a response header that is not one of the default headers allowed by CORS (Cache-Control, Content-Language, Content-Length, Content-Type, Expires, Last-Modified, or Pragma).

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | For more information, see the Scope of action section in Create a policy. The scope can be global or local. If you selectL ocal, you can attach the policy to an Ingress, a Service, a Consumer, or any combination of these three realms. |
| Cache Policy | Configure the policy as needed. For more information, see Cache policy configuration examples. |

t Configuration: In the Expose-Headers field, add the response headers that you want to expose. If you have multiple headers, separate them with commas (,).

**Configure the preflight cache duration**

Recommendation: If you restrict request headers and the header parameters change frequently, do not set a long preflight cache duration. For complex requests, the browser sends a preflight request before the actual request. The actual request is sent only after the preflight request succeeds. After a successful preflight, the browser caches the preflight information based on the URL and request header parameters. When the same request is made again, another preflight request is not needed. Because the preflight information is cached in the browser, if you modify the CORS configuration while a preflight cache for a request already exists, the browser will not send a new preflight request until the cache expires. This means that the new Allow-Headers configuration will not take effect immediately.

**JSONP cross-domain requests**

For example, the direct request URL for a backend API is: http://test.com/hello?id=1&msg=1 To make a JSONP request, the frontend adds a callback parameter to the URL. For example, if the callback parameter is 'Callback' and its value is 'jsonp', the request URL becomes: http://test.com/hello?id=1&msg=1&callback=jsonp.

**Choose between CORS and JSONP**

Use JSONP if you only use GET AJAX requests and need to support older browsers, such as **IE**
**<= 9, Opera < 12**, or **Firefox < 3.5**. Otherwise, use CORS.

##### Cache policy

A response cache policy caches response information for specific APIs. Matching requests can then retrieve the response directly from the cache. This reduces the processing load on your service. Responses are cached based on the request method, path, headers, and query parameters. Different parameter values result in separate cached responses.

**Disable cache control**

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |

t To add a response cache for an API in Service A, the direct request URL is:

```
GET http://testA.com/hello?id=1&msg=1
```

The configuration is as follows:
**Cache Duration**: 300 seconds.
**Cache Control**: Disabled.
**Response Status Code**: 200.
**API To Cache**: Set **Method** to `GET` , **Path** to `/hello` , and QueryParams to `id,msg` .

**Enable cache control**

You can use `cache-control` to specify how the cache is used. After you enable **Cache Control**, you can add the `Cache-Control` instruction to the request header. This instruction specifies how the cache is used for the request. The following instructions are supported: no-store: Does not store the response in the cache. max-age: Specifies the maximum age of an acceptable cached response, in seconds. For example, `max-age=2` means the request only uses responses cached within the last 2 seconds. The following examples show how to use the instructions:

```bash
curl --request GET 'http://domain/cache/hello' --header 'cache-control: no-store' curl --request GET 'http://domain/cache/hello' --header 'cache-control: max-age=300'
```

##### IP blacklist and whitelist policy

You can configure blacklists and whitelists to restrict access to this route based on IP addresses. The IP blacklist and whitelist feature supports both standard IP addresses and IP addresses in Classless Inter-Domain Routing (CIDR) format. After you enter an IP address, you can set the policy to allow or deny access from that IP address.

**Note**

Deny policies have a higher priority than allow policies. API Gateway first checks if a request matches any deny rule. If a match is found, the request is denied immediately. If no deny rule matches, API Gateway checks for a match with an allow rule. If a match is found, the request is allowed. If a request does not match any configured IP blacklist or whitelist rules, it is denied. On the Create IP Blacklist and Whitelist Policy page, you can specify the parameters to create the policy.

| Scope of action | See Scope of action in Create a policy. You can select a Global or Local scope. If you select Local, you can select Attach Route, Attach Service, Attach Consumer, or any combination of these three realm objects. |
|---|---|
| IP Blacklist And Whitelist Policy | Supports IP Addresses or CIDR Blocks. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | See Scope of action in Create Policy. The scope can be global or local. If you select Local, only Attach Service is supported. |
| Pass To Downstream | Specifies whether the gateway echoes the request ID in the response header. If you enable this option, the request ID is added to the request header. Because the request is configured to be passed downstream, the response header will also include the request ID header. |
| Request Header Name | The name of the HTTP header that contains the request ID. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |

t

##### Request tracing policy

Request tracing adds a request ID to requests forwarded to a backend service. You can read this ID from the response header returned by the gateway. This requires enabling the option to pass the ID downstream. On the Create Request Tracing Policy page, you can set the parameters for the policy.

##### ACL access control policy

You can configure an Access Control List (ACL) policy to specify which consumer groups can access this route. If a consumer belongs to a group that matches a configured ACL rule, the gateway grants access. Note that deny rules have a higher priority than allow rules. On the policy creation page, complete the configuration and create the policy.

| Scope of action | For more information, see theScope of action section in Create a policy. The scope can be global or local. If you select Local, you can attach the policy only to a Route, a Service, or a combination of both realm objects. |
|---|---|
| ACL Access Control Policy | You can configure multiple rules. Set each rule to Deny or Allow. |

| Parameter | Description |
|---|---|
| Name | A custom name for the policy. |
| Scope of action | For more information, see the Scope of action section in Create a policy. Global and local scopes are supported. If you select Local, only Bind Route, Bind Service, and a combination of these two realm objects are supported. |
| HSF Method Name | The method name of the target upstream service. |
| Request Parameters | Parameter Name: The name of the parameter that corresponds to the upstream service method. Parameter Type: The type of the parameter that is defined in the upstream service method. Parameter Position: The order of the parameter in the upstream service method definition. The sequence starts from 1. |

t

##### HSF protocol mapping policy

On the HSF protocol mapping policy page, specify the configuration items to create a policy.

**Example of an HSF protocol mapping policy configuration**

1. View the HSF method definition of the backend service.

```
String sayHiAndSendMoney2(String name, Money[] moneyList);
```

2. In the **HSF Protocol Mapping Policy**, specify the following parameters:
**HSF Method Name**: sayHiAndSendMoney2
**Request Parameter** 1:
**Parameter Name**: name
**Parameter Type**: Reference data type, java.lang.String
**Parameter Position**: body
**Request Parameter** 2:

| Parameter | Description |
|---|---|
| Certificate Name | Enter the name of the certificate, which cannot exceed 15 characters in length. |
| Certificate Type | Valid values: Server Certificate and CA Certificate. |
| Certificate File | Enter the content of the certificate file into the text box, or click Upload Certificate to read content from the certificate file. |
| Certificate Key | Enter the content of the key file into the text box, or click Upload Key to read content from the key file. Note This parameter is available only when Certificate Type is set to Server Certificate. |

t
**Parameter Name**: moneyList
**Parameter Type**: Basic type, array
**Parameter Position**: body

### Certificate management

The certificate management feature allows you to upload certificates to an API gateway. After you upload certificates, when a user accesses the API gateway over HTTPS, the gateway will return the certificate corresponding to the requested domain name to the user in order to complete TLS handshake. In addition, the certificate management feature also allows you to update, delete, and view certificates in order to manage the entire lifecycle of certificates.

**Create a certificate**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate** page, click **Create Certificate**, configure the parameters, and click
**Determine**.

**View the details of a certificate**

After you upload a certificate, you can view the details of the certificate.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
t
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate** page, click the name of the target certificate to view the certificate
details.
**Basic Information**: You can view **Certificate ID**, **Serial Number**, **Certificate Name**,
**Algorithm**, **Certificate Type**, **Private Key Length**, **Issue Time**, and **Expiration Time**.
**Issuer Information**: You can view **Name of Issuer** and **Issuer Department**.

**Update a certificate**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate** page, click **Update** in the Operation column of the target certificate.
6. In the **Update Certificate** panel, modify the certificate information and click **Determine**.

**Remove a certificate**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Certificate Management**.
5. On the **Certificate** page, click **Delete** in the **Operation** column of the target certificate.
6. In the message that appears, click **Determine**.

**Access the gateway**

After you upload a certificate, use the domain name that is associated with the certificate and other domain names to access the gateway. t The result indicates that the gateway returns the corresponding certificate and the TLS handshake is complete only when you use the domain name associated with the certificate to access the gateway. =

### Domain name management

| Parameter | Description |
|---|---|
| Domain Name | Enter a domain name. |
| Agreement | Valid values: HTTPS and HTTP. |
| Server Certificate | Note This parameter is available only when Agreement is set to HTTPS. Select a server certificate. If no server certificate is available, create one. For more information, see Certificate management. |
| Enable two-way authentication | Specify whether to enable or disable two-way authentication. |
| CA Certificate | Note This parameter is available only after you enable two- way authentication. Select a CA certificate. For more information about how to create a CA certificate, see Certificate management. |
| Add request header fields to get client certificate holder (Subject) information | Note This parameter is available only after you enable two- way authentication. Select or unselect this option based on your business requirements. If you select this option, the system automatically adds custom request headers based on the CA certificate. |

t The domain name management module allows you to add different domain names and associate a route with domain names. This way, only requests sent to the associated domain names are forwarded based on the corresponding route.

**Add a domain name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Name Management** page, click **Associated Domain Name**, configure
the parameters, and click **Determine**.

| Add a Request Header Field to Get Client Certificate Issuer (Issuer) Information | Note This parameter is available only after you enable two- way authentication. Select or unselect this option based on your business requirements. If you select this option, the system automatically adds custom request headers based on the CA certificate. |
|---|---|

t

**Modify a domain name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Name Management** page, click **Edit** in the **Operation** column of the
target domain name.
6. Modify **Agreement** and click **Determine**.

**Remove a domain name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Name Management** page, click **Delete** in the **Operation** column of the
target domain name.
6. In the **Alert** message, click **Determine**.

**View the details of a domain name**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, click **Domain Name Management**.
5. On the **Domain Name Management** page, you can filter domain names by **domain**
**name**.
6. Click a domain name in the **Domain Name** column to view its details.
**Basic information**: You can view **Domain Name**, **Agreement**, **Creation time**, and
**Update time**.
**Associated Routing**: You can view routes and services associated with the domain
name and their creation time. t

**Associate a domain name with a route**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. On the **Routing Management** page, click **Create Route**. You can also click the
icon in the **Operation** column of the target route and click **Edit**.
6. On the **Create Route** or **Edit route** page, specify **Associated Domain Name** to
associate the route with a domain name.

**Access the gateway through the domain name**

After you associate a route with a domain name, the API gateway uses the route to forward requests when you access the associated domain name. The Host header of requests carries the associated domain name. If you access a different domain name, the API gateway cannot locate the corresponding route.

### Disaster recovery

**management**

#### Disaster recovery groups

Disaster recovery groups are applicable to high availability (HA) solutions and disaster recovery solutions that ensure service continuity in the event of a fault. This topic describes how to create and manage disaster recovery groups.

**Prerequisites**

The local gateway is connected to the peer gateway. For more information, see Disaster recovery gateways.

**Important**

t The following operations must be performed on the local gateway.

**Create a disaster recovery group**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Disaster Recovery > Routing Group**.
5. On the **Disaster Recovery Group** page, click **Create a disaster recovery group**.
6. On the **Create a routing Group** page, configure the parameters and click **Submission**.
For more information, see Create a disaster recovery group.

**Note**

After the disaster recovery group is created, a corresponding record is generated in the disaster recovery group list of the peer gateway. You can only view the disaster recovery group of the peer gateway. Other operations are not supported.

**What to do next**

After you create a disaster recovery group, you can view the details of the group, modify the configuration of the group, and delete the group and on the **Disaster Recovery Group** page. For more information, see Route groups.

#### Disaster recovery services

On the Disaster Recovery Services page, you can create and manage service instances that support disaster recovery capabilities to implement high availability (HA) deployment across regions. This topic describes how to create and manage disaster recovery services.

**Prerequisites**

The local gateway is connected to the peer gateway. For more information, see Disaster recovery gateways.

**Create a recovery service**

**Important**

The following operations must be performed on the local gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Disaster Recovery > Services**.
5. On the **Disaster Recovery Services** page, click **Create a disaster recovery service**.
6. On the **Create Service** page, configure the parameters and click **Determine**. For more
information, see Create a service. t

**Note**

After the disaster recovery service is created, a corresponding record is generated in the disaster recovery list of the peer gateway. You can only view the disaster recovery service of the peer gateway. Other operations are not supported.

**What to do next**

After you create a disaster recovery service, you can view the details of the service, modify the configuration of the service, and delete the service on the **Disaster Recovery Services** page. For more information, see Service list.

#### Disaster recovery routes

On the **Disaster Recovery Routing** page, you can configure a request routing rule that implements disaster recovery by scheduling traffic across regions for high availability (HA).

**Prerequisites**

The local gateway is connected to the peer gateway. For more information, see Disaster recovery gateways.

**Create a disaster recovery route**

**Important**

The following operations must be performed on the local gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Disaster Recovery > Routing**.
5. On the **Disaster Recovery Routing** page, click **Create disaster recovery routing**.
6. On the **Create Route** page, configure the parameters and click **Determine**. For more
information, see the "Create a route" section in the Route management topic.

**Note**

After the disaster recovery route is created, a corresponding record is generated in the disaster recovery list of the peer gateway. You can only view the disaster recovery route of the peer gateway. Other operations are not supported.

**What to do next**

After you create a disaster recovery route, you can view the details of the route, modify the configuration of the route, and delete the route on the **Disaster Recovery Routing** page. For more information, see Route management. t

#### Disaster recovery consumers

On the **Disaster Recovery Consumer** page, you can manage client applications (consumers) that access the disaster recovery system. This ensures that these applications can still call services in scenarios such as primary/secondary switchover and cross-region deployment.

**Prerequisites**

The local gateway is connected to the peer gateway. For more information, see Disaster recovery gateways.

**Create a disaster recovery consumer**

**Important**

The following operations must be performed on the local gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Disaster Recovery > Consumer**.
5. On the **Disaster Recovery Consumer** page, click **Create a disaster recovery**
**consumer**.
6. On the **Create a disaster recovery consumer** page, configure the parameters and click
**Determine**. For more information, see the "Create a consumer" section in the Consumers
topic.

**Note**

After the disaster recovery consumer is created, a corresponding record is generated in the disaster recovery list of the peer gateway. You can only view the disaster recovery consumer of the peer gateway. Other operations are not supported.

**What to do next**

After you create a disaster recovery consumer, you can view the details of the consumer and modify the configuration and group of the consumer on the **Disaster Recovery Consumer** page. For more information, see Consumers.

#### Disaster recovery policies

On the **Strategy Management** page, you can create and manage different types of disaster recovery policies to implement fine-grained control over traffic scheduling, failovers, and permissions.

**Prerequisites**

The local gateway is connected to the peer gateway. For more information, see Disaster recovery gateways. t

**Create a disaster recovery policy**

**Important**

The following operations must be performed on the local gateway.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Disaster Recovery > Strategy Management**.
5. On the **Strategy Management** page, click **Create Policy**.
6. On the **Create Policy** page, configure the parameters and click **Determine**. For more
information, see Create a policy.

**Note**

After the disaster recovery policy is created, a corresponding record is generated in the disaster recovery list of the peer gateway. You can only view the disaster recovery policies of the peer gateway. Other operations are not supported.

**What to do next**

After you create a disaster recovery policy, you can view the details of the policy, change the status of the policy, modify the configuration of the policy, and delete the policy on the
**Strategy Management** page. For more information, see Policy lifecycle management.

| Parameter | Description |
|---|---|
| Name | Specify a custom name for the cluster. |
| Cluster Type | Select Self-built Kubernetes or Container Service. |
| Container service cluster ID | Note This parameter is displayed only if Cluster Type is set to Container Service. Enter the ID of the cluster to be imported. You can view the cluster ID on the Clusters page in the ACK console. |
| Container Service Cluster Name | Note This parameter is displayed only if Cluster Type is set to Container Service. Enter the name of the cluster to be imported. You can view the cluster name on the Clusters page in the ACK console. |

## Kubernetes cluster

**management**

This topic describes how to import external Kubernetes clusters to API Gateway for centralized management.

**Prerequisites**

A Kubernetes cluster is created or the kubeconfig file of a self-managed Kubernetes cluster is obtained. For more information, see **Container Service for Kubernetes User Guide >**
**Create an ACK cluster**.

**Import the cluster**

**Note**

Currently, only Kubernetes clusters are supported.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, click **Import K8s Cluster**.
4. In the **Import to K8s Cluster** panel, specify the parameters, click **Test connection** to
check the configuration, and then click **OK**.

| SLB Type | Select Internet or Internal Network. |
|---|---|
| Configuration Content | Enter the kubeconfig information. |

**Cancel cluster import**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, click **Cluster Management**.
3. On the **Cluster Management** page, find the cluster that you want to remove and click
**Remove** in the **Operation** column.
4. In the **Remove this K8s cluster** message, click **OK**.
t

## Cascade management

### Overview

The cascade feature is an important capability of API Gateway. It connects the routing and services between multiple API Gateways. This connection allows users of one API Gateway to call services managed by another API Gateway.

**Background**

The cascade feature connects routing and services between two network partitions, each with its own API Gateway. This connection allows users in one partition to call services in the other partition through API Gateway. This feature is ideal for large-scale, cross-region Apsara Stack systems. Consider the following scenario: A company has two independent environments, such as two separate Apsara Stack systems. The two environments are in different network partitions, Network A and Network B. Each environment has its own API Gateway system deployed. Typically, users expose backend services in their own environment through API Gateway. These services are then called by users within the same environment. The two systems operate independently of each other. Suppose a new requirement arises where you need to publish backend services from Network A to Network B using API Gateway routing. This makes the services available for users in Network B to call, which allows for flexible communication between the two environments. The cascade feature provides a simple way to meet this requirement.

**Terms**

The preceding diagram illustrates the main concepts and workflow of the cascade feature. The basic concepts are described as follows: Source gateway: The gateway in the network where the backend service is located. For example, in the diagram, a backend service in Network A is exposed to users in Network B. In this case, the API Gateway in Network A is the source gateway. t Cascade gateway: The gateway in the network where the users who call the backend service are located. For example, in the diagram, users in Network B want to call the backend service in Network A. In this case, the API Gateway in Network B is the cascade gateway. Source gateway console: The console for the source gateway. In this console, you can create, modify, or delete entities such as routes, consumers, and signatures. These operations are then synced to the cascade gateway. The source gateway console can be considered the "operator". Cascade gateway console: The console for the cascade gateway. This console receives requests from the source gateway console to create entities, such as routes and consumers, and then creates the corresponding cascade entities. The cascade gateway console can be considered the "receiver" because it only accepts and executes commands from the source gateway console. Prerequisites: All API Gateway instances must be version 2.5.1 or later. The source gateway console must be able to access the cascade gateway console over the network. The cascade gateway must be able to access the source gateway over the network. To use the cascade feature, perform the following steps:
1. Import the cascade gateway. In the source gateway console, import the cascade gateway
and provide its basic information. After the import is complete, you can monitor the status of the cascade gateway from the source gateway console.
2. Create a cascade link. In the source gateway console, create a cascade link. A cascade link
consists of a source gateway and a cascade gateway. The source gateway must be an instance managed by the current console. The cascade gateway must be the one imported in the previous step.
3. Create a route. In the source gateway console, create a source route and specify the
cascade link. A corresponding cascade route is then automatically created in the cascade gateway. After you complete these steps, users in Network B can access services in Network A through the cascade route. If you require policies such as authentication and signing, you must perform the following additional steps:
1. Create a source consumer. In the source gateway console, create a source consumer and
specify the cascade link. A corresponding cascade consumer is then automatically created in the cascade gateway. Note: When you attach a route to the source consumer, the route must use the same cascade link.
2. Create a source signature. In the source gateway console, create a source signature and
specify the cascade link. A corresponding cascade signature is then automatically created in the cascade gateway. Note: When you create a signature policy for the source route, you can only attach a source signature that uses the same cascade link.

### Cascade gateways

This topic describes how to import, view, and delete cascade gateways. It also provides answers to frequently asked questions.

**Import a cascade gateway**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascading Gateway**.

| Parameter | Description |
|---|---|
| Gateway Type | Internal Gateway: A gateway instance managed by this console. To select this type of gateway, simply select a gateway from the drop-down list. External Gateway: A gateway instance not managed by this console. To select this type of gateway, enter the basic information. |
| Cascade Instance | This parameter appears when you set Gateway Type to Internal Gateway. Select the required instance from the drop- down list. |
| Gateway Name | This parameter appears when you set Gateway Type to External Gateway. The name of the gateway. You can customize the name. |
| Cascade Instance ID | Displayed when Gateway Type is set to External Gateway. The ID of the gateway, which is user-defined. Ensure that the ID is consistent with the instance ID of the gateway entered above. |
| OpenAPI Endpoint | This parameter appears when you set Gateway Type to External Gateway. The OpenAPI endpoint must be an address that starts with http:// and does not contain any path. The endpoint must provide direct access to the backend of the cascade gateway console. |
| Console AccessKey | This parameter appears when you set Gateway Type to External Gateway. To obtain the AccessKey, see the Apsara Uni-manager Management Console User Guide > Personal AccessKey section. |
| Console SecretKey | This parameter appears when you set Gateway Type to External Gateway. To obtain the SecretKey, see the Apsara Uni-manager Management Console User Guide > Personal AccessKey section. |

t
3. Click **Import Cascade Gateway**, enter the required parameters, and click **OK**. If the
gateway type is **External Gateway**, after you configure the parameters, you can click
**Test Connection** to verify the settings.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascading Gateway**.
3. On the **Cascade Gateways** page, you can view all imported cascade gateways. You can
filter the gateways by **Instance Name** and **Instance ID**.
4. Find the cascade gateway that you want to view and click its ID in the **Gateway ID/Name**
column to view its details.

**Delete a cascade gateway**

t
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascading Gateway**.
3. Find the cascade gateway that you want to delete and click **Delete** in the **Actions** column.
4. In the **Notice** dialog box that appears, click **OK**.

**View cascade call instructions**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascading Gateway**.
3. On the **Cascade Gateways** page, click **Cascade Call Instructions** in the upper-right
corner to view detailed instructions on cascade calls.

**FAQ**

**Connection error when importing a cascade gateway**

A **Connection Error** message indicates a network fault. Check the following items:
1. Verify that the OpenAPI endpoint is correct.
2. Verify that the network connection is established.

**OpenAPI-related error when importing a cascade gateway**

An OpenAPI-related error indicates that the AccessKey or SecretKey is incorrect. Check the following items:
1. Verify that the access credential is valid.
2. Confirm that you entered the credential correctly. For example, make sure that no
characters are missing and no extra spaces are added during a copy-and-paste operation.

### Cascade links

This topic describes how to create, view, edit, and delete cascade links.

**Create a cascade link**

You must create cascade links in the source gateway console.

| Parameter | Description |
|---|---|
| Link Name | Enter a custom name for the link. |
| Source Gateway | Select a gateway instance that is managed by the current console. |
| Source Gateway Access Address | The cascade gateway uses this endpoint to access the source gateway. |
| Cascading Gateway | Select an imported gateway. For more information, see Import cascade gateways. |

t
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascade link**.
3. Click Create a cascading link, enter the parameters, and then click **OK**.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascade link**.
3. On the **Cascade Links** page, you can view all existing cascade links. You can filter the
links by **Link Name** or **Link ID**.
4. Select the target cascade link and click its ID in the **Link ID/Name** column to view its
details.

**Edit a cascade link**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascade link**.
3. Find the cascade link that you want to edit. In the **Actions** column, click **Edit**.
4. In the **Edit Cascade Link** dialog box, edit the **Source Gateway Endpoint** and click **OK**.

**Delete a cascade link**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Cascade Management > Cascade link**.
3. Find the cascade link that you want to delete. In the **Actions** column, click **Delete**.
4. In the **Prompt** dialog box, click **OK**.

| Parameter | Description |
|---|---|
| Cloud Name | The name of the cloud center. You can customize the name for easy identification. The name must be 4 to 20 bytes in length, and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Cloud Edition | Select Enterprise Edition. |
| Cloud Managemen t | Select ASR for Geo-disaster Recovery. |

## Disaster recovery

**management**

### Disaster recovery gateways

Two API Gateway instances deployed in different regions, such as China (Hangzhou) and China (Shanghai), can be paired to form a disaster recovery group. If the primary gateway fails, the system automatically switches traffic to the secondary gateway to ensure service continuity.

**Procedure**

**Step 1: Configure cloud information**

**Note**

When you log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console from the Apsara Uni-manager Operations Console for the first time, you must configure the secondary cloud. To configure the secondary cloud, go to the Cloud Information Management page. On the Cloud Information Management page, click **Edit** in the
**Current Cloud** section. You can also find the secondary cloud in the All Clouds section
and click **Edit** in the **Actions** column. After the secondary cloud is configured, it enters the **Running** state. For more information about how to configure the parameters, see the table that describes the parameters in the "Procedure" section of this topic.
1. Log in to the ASR for Geo-disaster Recovery console from the Apsara Uni-manager
Operations Console.
2. In the left-side navigation pane, choose **General > Cloud Information Management**.
3. On the Cloud Information Management page, click **Add Cloud**. In the Add Cloud dialog box,
configure the parameters. The following table describes the parameters.

| Managemen t API Endpoint | Specify the value of Manage API Access Point of the peer cloud on the Cloud Information Management page of the ASR for Geo-disaster Recovery console. |
|---|---|
| AccessKey ID and AccessKey Secret | Enter the AccessKey ID and AccessKey secret of the operations administrator account on the peer cloud. For more information, see Obtain the AccessKey pair of a personal account. |

| Parameter | Description |
|---|---|
| Disaster Recovery Interconnection Name | The name of the disaster recovery interconnection. |
| Description | The description of the disaster recovery interconnection. |
| Regions with Disaster Recovery Interconnections Configured | The regions to be interconnected for disaster recovery. Specify at least two regions. |
| Services with Disaster Recovery Interconnections Configured | The cloud services for disaster recovery interconnection. The system automatically identifies the cloud services that support disaster recovery in the specified interconnected regions. Use the default value. |

4. Click **Verify**. After the verification is passed, click **OK**.
5. Configure cloud services.
i. On the Cloud Information Management page, find the cloud that you want to manage and click **Configuration** in the **Actions** column to go to the **Cloud Service Configuration** page. ii. In the **Disaster Recovery Services** section, click **Add Service**. iii. In the dialog box that appears, select **APIGATEWAY** from the drop-down list. The system automatically generates **API Gateway Address**. Confirm that **API Gateway Address** is correct and click **OK**. iv. For more information about the services in the **Basic Services** section, see **ASR for**

**Geo-disaster User Guide > O&M console of ASR for Geo-disaster Recovery >**

**Basic capability O&M > Manage cloud service information**.

**Step 2: Create a disaster recovery interconnection**

1. Log in to the ASR for Geo-disaster Recovery console. In the left-side navigation pane,
choose **General > Disaster Recovery Interconnection Management**.
2. On the Disaster Recovery Interconnection Management page, click **Add Disaster**
**Recovery Interconnection**. In the dialog box that appears, configure the following
parameters.
3. Click **Submit**.

**Step 3: Create a cloud instance**

**Note**

If you log in to the ASR-DR: Geo-Disaster Recovery Management Platform for the first time, you must create a cloud instance. Otherwise, you can skip this step.
1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products > Disaster Recovery and Backup >**
**Disaster Recovery > ASR-DR: Geo-Disaster Recovery Management Platform**.
3. In the left-side navigation pane, choose **System Management > Cloud Instance**
**Management**.
4. In the **Current Instance** section, click **Edit**.
5. In the dialog box that appears, specify Tenant Account AccessKey Pair and Tenant Account
AccessKey Secret, and click **Submit**. For more information about how to obtain the AccessKey pair, see Obtain the AccessKey pair of an organization.

**Note**

Enter the AccessKey ID and AccessKey secret of the organization you obtained in the Tenant Account AccessKey Pair and Tenant Account AccessKey Secret fields for the primary cloud. The Tenant Account AccessKey Pair and Tenant Account AccessKey Secret parameters need to be specified only once by the cloud instance creator.
6. In the dialog box that appears, enter the AccessKey ID and AccessKey secret of the
personal account you obtained. For more information about how to obtain the AccessKey pair, see Obtain the AccessKey pair of a personal account.

**Note**

Enter the AccessKey ID and AccessKey secret of the personal account you obtained for the primary cloud in the **User ************** and **User ****************** fields.
7. In the **All Instances** section, click **Add Instance**, select the cloud instance that you want
to add, and then click **Next**.
8. In the dialog box that appears, select options from the **Organizations** and **Resource Set**
drop-down lists, specify Tenant Account AccessKey Pair and Tenant Account AccessKey Secret, and then click **Submit**. For more information about how to obtain the AccessKey pair, see Obtain the AccessKey pair of an organization.

**Note**

Enter the AccessKey ID and AccessKey secret of the organization you obtained in the Tenant Account AccessKey Pair and Tenant Account AccessKey Secret fields for the peer cloud. The Tenant Account AccessKey Pair and Tenant Account AccessKey Secret parameters need to be specified only once by the cloud instance creator.
9. In the dialog box that appears, enter the AccessKey ID and AccessKey secret of the
personal account you obtained. For more information about how to obtain the AccessKey pair, see Obtain the AccessKey pair of a personal account.

| Parameter |  | Description |
|---|---|---|
| Disaster Recovery Relationship Name |  | A custom name for the disaster recovery relationship. The name must be 5 to 29 characters in length. |
| Description |  | A description of the disaster recovery relationship. |
|  | Cloud Instance | The cloud instance where the ASR-DR platform that you are logged on to is located. Keep the default value. |
|  | Region | The region where the ASR-DR platform that you are logged on to is located. Keep the default value. |

**Note**

Enter the AccessKey ID and AccessKey secret of the personal account you obtained for the peer cloud in the **User ************** and **User ****************** fields.
0. Click **Confirm**. Configured is displayed in the User AccessKey Pair column of the cloud
instance.

**Note**

The **User ************** and **User ****************** parameters must be configured for each user. A user can use the cloud instance only after the parameters are configured.

**Step 4: Create a disaster recovery relationship**

**Note**

If you log in to the ASR-DR: Geo-Disaster Recovery Management Platform for the first time, you must create a disaster recovery relationship. Otherwise, you can skip this step.
1. Log in to the ASR-DR: Geo-Disaster Recovery Management Platform. In the left-side
navigation pane, choose **System Management** > **Disaster Recovery Relationship**
**Management**.
2. On the **DR Relationship Management** page, click **Add DR Relationship**.

**Note**

In multiple regions within a disaster recovery relationship, only one production region exists. All regions except the production region are secondary regions.

| Current Region Configurati on |  |  |
|---|---|---|
|  | Regional Role | Select whether the current region is a production region or a secondary region. Production Region: The region where the primary data center is located in the ASR-DR system. Secondary Region: A backup site or data center that ensures business continuity and data recovery when a disaster or failure occurs in the primary production environment. Note For DR relationships other than Hybrid Disaster Recovery, configure the current region as a secondary region. |
| Disaster Recovery Region Configurati on | Cloud Instance | Select a cloud instance. In a DR relationship, a cloud instance can be added multiple times, but each instance must be in a different region. This enables cross-region DR. |
|  | Region | Select the region to which the cloud instance belongs. |
|  | Regional Role | Select Production Region or Secondary Region. This role must be different from the Regional Role of the Current Region Configuration. |

3. Click **OK**.

**Step 5: Create a protection group**

1. Log in to the ASR-DR: Geo-Disaster Recovery Management Platform. In the left-side
navigation pane, choose **DR for Business** > **Protection Groups**.
2. On the Protection Groups page, click **Create**.
3. On the **Create Protection Group** page, configure the parameters that are described in
the following table.

| Section | Parameter | Description |
|---|---|---|
| Basic Configurations Note This section displays the basic information about the disaster recovery region. | Organizations | The organization to which the protection group data belongs. |
|  | Resource Set | The resource set to which the instance for disaster recovery belongs. |
|  | Disaster Recovery Relationship | The disaster recovery relationship to which the protection group belongs. |
| Protection Group Information | Name | The name of the protection group. You can specify a custom name. The name must be 4 to 40 characters in length and can contain only letters, digits, hyphens (-), underscores ( ), and _ periods (.). |
|  | Synchronization Direction | The switchover direction. If services are provided by the instances at the primary site, select Forward. If services are provided by the instances at the secondary site, select Backward. Note The synchronization direction for the protection group changes based on the completion of switchovers and switchbacks. After switchovers are complete, Forward changes to Backward. After switchbacks are complete, Backward changes to Forward. |
|  | Protection Group Mode | Primary/Secondary: In primary/secondary mode, the primary site provides services. The secondary site replicates data from the primary site in real time, but does not provide services. When the primary site fails, services are failed over to the secondary site. Active-active: In active-active mode, both the primary and secondary sites provide services. Note You can create a protection group in active-active mode only after you purchase a corresponding license. |
| Document Version: 2026 | 0629 15 |  |

|  | Description | The description of the protection group. You can customize the description for easy identification. |
|---|---|---|

4. Click **Submit**. On the **Protection Groups** page, find the protection group that you created,
and click **Create Entity** in the Actions column.
5. Add synchronization entities as prompted. For more information, see **ASR for Geo-**

**disaster User Guide > ASR for Geo-disaster Recovery operations in the Apsara**

**Uni-manager Management Console > DR for business > Manage protection**

**groups > Add a synchronization entity > API Gateway**.
6. Click **OK**. The protection group is created.

**Step 6: View a disaster recovery group**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **Disaster Recovery > Gateway Instance**.
3. On the **Disaster Recovery Gateway Instance** page, you can view the information about
created disaster recovery groups, including **This gateway Instance ID**, **Peer Gateway**
**Instance ID**, **Disaster Recovery Gateway Name**, **Creation time**, and **Update time**.

**Obtain an AccessKey pair**

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only operations administrators or level-1 organization administrators can obtain the AccessKey pairs of organizations.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page that appears, move the pointer over the profile
picture, and click **User Information**.
3. In the **AccessKey Pair** section, you can view the AccessKey pair of your account.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page, click **Manage AccessKey Pairs**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

| Servic e type | Servic e disco very meth od | HTTP- to- Dubb o | HTTP- to- gRPC | HTTP- to- WebS ervice | HTTP- to- HTTP | HTTP- to- HTTP S | HTTP- to- HSF | HTTP- to- JDBC | HTTP/ HTTP S-to- HTTP |
|---|---|---|---|---|---|---|---|---|---|
| RPC servic e | Servic e discov ery | Suppo rted | Not suppor ted | Not suppor ted | Suppo rted | Suppo rted | Suppo rted | Not suppor ted | Not suppor ted |
|  | Fixed nodes | Suppo rted | Suppo rted | Suppo rted | Suppo rted | Suppo rted | Suppo rted | Not suppor ted | Not suppor ted |
| Datab ase | Fixed nodes | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Suppo rted | Not suppor ted |
| Virtua l Privat e Cloud (VPC) servic e | Fixed nodes | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Not suppor ted | Suppo rted |

| Parameter | Description |
|---|---|
| Name | Required. The globally unique name of the service within the scope of a gateway instance. |

## Protocol conversion

API Gateway provides the following protocol conversion capabilities. The HTTP-to-Dubbo and HTTP-to-HTTP protocol conversion supports both fixed nodes and service discovery, whereas the HTTP-to-gRPC and HTTP-to-WebService protocol conversion supports only fixed nodes.

**Create a service**

Find the API Gateway instance that you want to manage and go to the gateway details page. In the left-side navigation pane, choose **Service Management > Service List**. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to
**Dubbo** and specify other parameters to create the service.

| Description | The description of the service. |
|---|---|
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
| Upstream Type | Required. The type of the upstream service. Valid values: Fixed node and Service Discovery. |
| Node | This parameter is required when you set Upstream Type to Fixed node. Enter the host address of the backend service. |
| Source | This parameter is required when Upstream Type is set to Service Discovery. This parameter indicates the source type of the backend service. Valid values: Nacos, Eureka, and EDAS. |
| Service Name | This parameter is required when you set Upstream Type to Service Discovery. The unique identifier of the service in the registry. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values when Upstream Type is set to Service Discovery: Polling and Random. Valid values when Upstream Type is set to Fixed node: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Select Dubbo. |
| Interface Name | Required. The name of the Dubbo service interface. |
| Version Number | The version number of the Dubbo service interface. |
| Interface Grouping | The group of the Dubbo service interface. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP-to-Dubbo protocol conversion are supported only in the POST request body. The following sample code shows the required parameter format.

| Parameter | Description |
|---|---|

```json
{
  "Type of Parameter 1": Parameter 1,
  "Type of Parameter 2": Parameter 2,
  ...
  "Type of Parameter n": Parameter n,
}
```

This section demonstrates the service call of the following Dubbo API operation:

```
 String sayHello(List<People> name, String first);
```

The following example shows how to call the operation. The first parameter of the operation is a list of the java.util.List type whose element type is a custom Person class, which has a name attribute of the String type and an age attribute of the Integer type. The second parameter is of the java.lang.String type. The following figure shows how to call the operation.

**Note**

You must specify multiple parameters in the same order as those defined in the API operation.

**Create a service**

Find the API Gateway instance that you want to manage and go to the gateway details page. In the left-side navigation pane, choose **Service Management > Service List**. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to
**gRPC** and specify other parameters to create the service.

| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
|---|---|
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
| Upstream Type | Required. The type of the upstream service. Currently, HTTP-to-gRPC protocol conversion supports only the Fixed node type. |
| Node | The host address of the backend service. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values when Upstream Type is set to Fixed node: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Select gRPC. |
| Interface Name | Required. The name of the gRPC service interface. Sample format: Package name.Service name. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP-to-gRPC protocol conversion are supported only in the POST request body. The following sample code shows the required parameter format. [

```
    JSON object for Parameter 1,
    JSON object for Parameter 2,
    ...
    JSON object for Parameter n,
```

] This section demonstrates the service call of the following gRPC API operation:

```java
package hello; service HelloService{ rpc SayHello(HelloRequest) returns (HelloResponse){} } message HelloRequest{ string name = 1; }
```

The following example shows how to call this operation. This operation has only one parameter whose element type is HelloRequest, which has a name attribute of the String type. The following figure shows how to call this operation:

**Note**

You must specify multiple parameters in the same order as those defined in the API operation.

| Parameter | Description |
|---|---|

**Limits**

Currently, HTTP-to-gRPC protocol conversion in the current version supports only Javabased gRPC services. In addition, the reflection parameter query feature must be enabled for gRPC services. HTTP-to-gRPC protocol conversion in this version supports only upstream gRPC services of the fixed node type.

**Create a service**

Find the API Gateway instance that you want to manage and go to the gateway details page. In the left-side navigation pane, choose **Service Management > Service List**. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to
**WebService** and specify other parameters to create the service.

| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
|---|---|
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
| Upstream Type | Required. The type of the upstream service. Currently, HTTP-to- WebService protocol conversion supports only the Fixed node type. |
| Protocol Type | Required. The protocol type of the upstream service. Select WebService. |
| Service Description File Address | Required. The address of the WSDL description file. |
| Service Version Information | Required. Valid values: SOAP1.1 and SOAP1.2. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP-to-WebService protocol conversion can be carried only in the POST request body. The following sample code shows the required parameter format. [

```
    JSON object for Parameter 1,
    JSON object for Parameter 2,
    .....
    JSON object for Parameter n
```

] This section demonstrates the service call of the following WebService API operation:

```
 String sayHello3(Person person, String name);
```

The following example shows how to call the operation. The first parameter of this operation is an object of the custom Person class, which has a name attribute of the String type and an age attribute of the Integer type. The second parameter is of the java.lang.String type. The following figure shows how to call the operation.

**Note**

You must specify multiple parameters in the same order as those defined in the API operation.

**Limits**

Currently, HTTP-to-WebService protocol conversion in this version supports only upstream WebService services of the fixed node type. Only WebService services whose bindType is Document-Literal (Wrapper or Unwrapper) are supported. Supported parameter types include Java primitive data types, List, Set, and custom object types. Parameters of the Map type are not supported. If you use parameters of the Map type, we recommend that you convert the data type to List or another supported type.

**Create a service**

| Parameter | Description |
|---|---|
| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
| Upstream Type | Required. The type of the upstream service. Valid values: Fixed node and Service Discovery. |
| Node | This parameter is required when you set Upstream Type to Fixed node. Enter the host address of the backend service. |
| Source | This parameter is required when Upstream Type is set to Service Discovery. Enter the source type of the backend service. Valid values: Nacos, Eureka, and EDAS. |
| Service Name | This parameter is required when you set Upstream Type to Service Discovery. The unique identifier of the service in the registry. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values when Upstream Type is set to Service Discovery: Polling and Random. Valid values when Upstream Type is set to Fixed node: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Select HTTP. |

Find the API Gateway instance that you want to manage and go to the gateway details page. In the left-side navigation pane, choose **Service Management > Service List**. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to
**HTTP** and specify other parameters to create the service.

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. The gateway supports various parameter-passing methods for HTTP-to-HTTP protocol conversion. For example, parameters can be appended to the route (URL path) for GET requests and carried in the POST request body. The parameter organization follows the same conventions as standard RESTful API operations.

```
 public String c(String name);
```

| Parameter | Description |
|---|---|
| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
| Description | The description of the service. |

The following figure shows how to call the operation. The only parameter of this operation is of the java.lang.String type.

**Create a service**

Find the API Gateway instance that you want to manage and go to the gateway details page. In the left-side navigation pane, choose **Service Management > Service List**. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to
**HTTPS** and specify other parameters to create the service.

| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
|---|---|
| Upstream Type | Required. The type of the upstream service. Valid values: Fixed node and Service Discovery. |
| Node | This parameter is required when you set Upstream Type to Fixed node. Enter the host address of the backend service. |
| Source | This parameter is required when Upstream Type is set to Service Discovery. Enter the source type of the backend service. Valid values: Nacos, Eureka, and EDAS. |
| Service Name | This parameter is required when you set Upstream Type to Service Discovery. The unique identifier of the service in the registry. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values when Upstream Type is set to Service Discovery: Polling and Random. Valid values when Upstream Type is set to Fixed node: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Select HTTPS. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. The gateway supports various parameter-passing methods for HTTP-to-HTTPS protocol conversion. For example, parameters can be appended to the route (URL path) for GET requests and carried in the POST request body. The parameter organization follows the same conventions as standard RESTful API operations. In this example, the HTTPS service provided by the GET method in httpbin.org is tested. The following figure shows how to call the service.

**Create a service**

**Note**

You can select an upstream type based on whether the application is registered with a registry. HTTP-to-HSF protocol conversion features similar configurations for the upstream types of Fixed node and Service Discovery. The following section describes how to create a service when the upstream type is Service Discovery for HTTP-to-HSF protocol conversion. The operations are similar when the upstream type is Fixed node. Before you create a service, you must create a source. Find the gateway instance that you want to manage and go to the instance details page. In the left-side navigation pane, choose
**Service Management > Source Management**. On the page that appears, click **Create**
**Source**. The source of an HSF service must be the HSF registry in EDAS. Then, specify the ID
of the namespace in EDAS where the service resides.

**Note**

HSF service discovery supports only the HSF registry in EDAS. After the source is created, choose **Service Management > Service List** in the left-side navigation pane. On the Service List page, click **Create Service**. On the Create Service page, set **Protocol Type** to **HFS** and specify other parameters to create the service.

| Parameter | Description |
|---|---|
| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select RPC service. |
| Upstream Type | Required. The type of the upstream service. Valid values: Fixed node and Service Discovery. |
| Node | This parameter is required when you set Upstream Type to Fixed node. Enter the host address of the backend service. |
| Source | This parameter is required when Upstream Type is set to Service Discovery. Enter the source type of the backend service. Valid values: Nacos, Eureka, and EDAS. |
| Service Name | This parameter is required when you set Upstream Type to Service Discovery. The unique identifier of the service in the registry. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values when Upstream Type is set to Service Discovery: Polling and Random. Valid values when Upstream Type is set to Fixed node: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Select HSF. |
| Interface Name | Required. The name of the HSF service interface. |
| Version Number | The version number of the HSF service interface. |
| Interface Grouping | The group of the HSF service interface. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP-to-HSF protocol conversion can be carried only in the POST request body. The following sample code shows the required parameter format.

| Parameter | Description |
|---|---|
| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select Database. |

```json
{
  "Type of Parameter 1": Parameter 1,
  "Type of Parameter 2": Parameter 2,
  ....
  "Type of Parameter n": Parameter n,
}
```

This section demonstrates the service call of the following HSF API operation:

```
 String sayHello(List<People> name, String first);
```

The following example shows how to call the operation. The first parameter of the operation is a list of the java.util.List type whose element type is a custom Person class, which has a name attribute of the String type and an age attribute of the Integer type. The second parameter is of the java.lang.String type. The following figure shows how to call the operation.

**Note**

You must specify multiple parameters in the same order as those defined in the API operation. The following figure shows how to access a gateway pod to call the operation.

```bash
curl --request POST 'http://127.0.0.1:80/default/sayHello' -d '{"java.util.List":[{"nam e":"james","age":33}],"java.lang.String":"mike"}'
```

**Create a service**

Before you create a service, you must create a source. Find the gateway instance that you want to manage and go to the instance details page. In the left-side navigation pane, choose
**Service Management > Source Management**. On the page that appears, click **Create**
**Source**. To implement HTTP-to-JDBC protocol conversion, you must select a database source.
Currently, mainstream database types MySQL and PostgreSQL are supported. After the source is created, choose **Service Management > Service List** in the left-side navigation pane. On the Service List page, click **Create Service**. On the Create Service page, set **Service Type** to **Database** and specify other parameters to create the service.

| Source | The service source to which the backend service belongs. Valid value: Database. |
|---|---|
| Protocol Type | Required. The protocol type of the upstream service. Select JDBC. |
| Return the maximum number of records | Required. Default value: 1000. If you have other requirements, contact the product team for adjustment. |
| COUNT Total number of records scanned Protection | After this switch is turned on, you can set the maximum number of records that can be scanned each time. |
| COUNT Maximum number of records scanned | This parameter is required only when the COUNT Total number of records scanned Protection switch is turned on. |
| Timeout (s) | Required. If you set the value to 0, no timeout limit is imposed. |
| SQL Template | Required. The FROM clause and subsequent content in normal SQL statements are required. The related return value fields must be specified in the Edit SQL result parameters section below. SQL statements of the MyBatis type are supported. |
| Edit SQL condition parameters | The parameter mappings for SQL execution. |
| Edit SQL result parameters | The result mappings of the returned values for SQL execution. |

The following figure shows the expanded **Edit SQL condition parameters**:
**requireTotalCount**, **offset**, and **limit** are default parameters. You cannot modify these
default parameters, and they are optional when a service call is initiated. The values in the
**queryValues** must be specified based on the actual situation. The parameter names in the
**SQL template parameter name** column must exactly match the parameter names
enclosed in #{xx} within SQL statements. The parameter names in the **Open parameter**
**name** column are the names of the parameters that are used to initiate the request.
The following figure shows the expanded Edit SQL result parameters: **resultCode**,
**resultMsg**, **resultCount**, and count are default parameters. You cannot modify these default
parameters, and they are optional when a service call is initiated. The values in **result** must be specified based on the actual situation. The fields in the **Parameter Table Field Name** column indicate the field names of the destination table in the database. The fields in the
**Open parameter name** column indicate the field names corresponding to the returned field
values for the call request. The **__csbRecordError** field is provided for customers to record error information encountered during parameter parsing. You can click **Edit** to modify the SQL condition parameters and result parameters. You can click **Add child node** to add child items under the SQL condition parameters or result parameters. You can click **Delete** to delete SQL condition parameters or result parameters.

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP-to-JDBC protocol conversion can be carried only in the POST request body. The following sample code shows the required parameter format.

```json
{
  "Name of Parameter 1": Parameter 1,
  "Name of Parameter 2": Parameter 2,
  ....
  "Name of Parameter n": Parameter n,
}
```

Initiate a request based on the JDBC service created in the preceding section. The following sample code shows the request structure and response format.

**Note**

The offset and limit parameters are optional and can be used to implement paginated queries. If you set the requireTotalCount parameter to true, the number of all results that meet the conditions is returned. If you set the requireTotalCount parameter to false, the number of results that meet the conditions is not returned.

| Parameter | Description |
|---|---|

```json
curl --request POST 'http://127.0.0.1:80/postgresql-route' -d ' {
    "queryValues": {
        "no1": 0,
        "no2": 3
    },
    "requireTotalCount": true,
    "offset": 0,
    "limit": 10
}'
```

Returned result:

```json
{
  "count": 2,
  "result": [
    {
      "customerId": 1,
      "email": "john@example.com",
      "name": "John Smith"
    },
    {
      "customerId": 2,
      "email": "mary@example.com",
      "name": "Mary Johnson"
    }
```

`],`

```json
  "resultCode": 200,
  "resultMsg": "SUCCESS",
  "totalCount": 99995
}
```

**Limits**

Currently, only MySQL and PostgreSQL databases are supported. Currently, only query operations on databases are supported. You cannot perform add, delete, and modify operations on databases. When you create a service, SQL statements must conform to MyBatis syntax.

**Create a service**

Before you create a service, you must create a source. Find the gateway instance that you want to manage and go to the instance details page. In the left-side navigation pane, choose
**Service Management > Source Management**. On the page that appears, click **Create**
**Source**.
After the source is created, choose **Service Management > Service List** in the left-side navigation pane. On the Service List page, click **Create Service**. On the Create Service page, set **Service Type** to **VPC Service** and specify other parameters to create the service.

| Name | Required. The globally unique name of the service within the scope of a gateway instance. |
|---|---|
| Description | The description of the service. |
| Service Type | Required. The type of the backend service for which protocol conversion is required. Select VPC Service. |
| Upstream Type | Required. The type of the upstream service. Only Fixed node is supported. |
| Node | Enter the VPC ID, hostname/IP address, port number, status, and traffic ratio. |
| Load balancing algorithm | Required. The load balancing algorithm used by the gateway to call the backend service. Valid values: Weighted Polling and Weighted random. |
| Protocol Type | Required. The protocol type of the upstream service. Valid values: HTTP and HTTPS. |

**Call a service**

The process of creating a route that involves protocol conversion is identical to that of creating a regular route that does not involve protocol conversion. No separate demonstration is provided for protocol conversion scenarios. For more information, see the route creation instructions. Currently, parameters for HTTP/HTTPS-to-HTTP protocol conversion can be carried only in the POST request body. The following sample code shows the required parameter format. [

```
    JSON object for Parameter 1,
    JSON object for Parameter 2,
    .....
    JSON object for Parameter n
```

] This section demonstrates the service call of the following HTTP/HTTPS API operation:

```java
package hello; service HelloService{ http SayHello(HelloRequest) returns (HelloResponse){} } message HelloRequest{ string name = 1; }
```

This operation has only one parameter whose element type is HelloRequest, which has a name attribute of the String type. The following figure shows how to call this operation:

**Note**

You must specify multiple parameters in the same order as those defined in the API operation.

**Limits**

Only shared instances are supported.

| Parameter | Description |
|---|---|
| Interface Name | Enter an interface name that does not exceed 50 characters in length. |
| Interface Description | Enter the description for the interface. |
| Interface request method | The HTTP method of requests sent to the gateway. |
| Back-end request method | The HTTP method of requests sent by the gateway to backend services. |

## Interface center

The interface center provides descriptions of interfaces that belong to a specific route. These interfaces can generate inspection items used to inspect interfaces. The interface details are also included in the portal interface details.

**Create an interface and configure parameter mapping**

**Note**

You can add interface information in the GUI, including the path, request parameters, and returned data. A shared gateway can perform parameter verification and mapping only on requests sent by upstream services that use the Http2Http and Http2Https protocols. A shared gateway can perform only parameter verification on requests sent by upstream services that use the Http2Dubbo and Http2GRpc protocols.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. On the **Interface Center** tab, click **Create** to go to the **Create Interface** page.
7. On the **Create Interface** page, configure the following parameters and click **Publish**
**Interface**.

| Content-type | This parameter is available only when Back- end request method is set to PUT or POST. You can select Pass-through client ContentType header, Custom, or Gateway Default. |
|---|---|
| Routing path | Select a route for the interface. |
| subPath | Specify whether to enable the subPath feature. |
| Subpath | This parameter is available only when the subPath feature is enabled. Enter a subpath. The subpath must start with a forward slash (/). |
| Access Path | The concatenation of the route path and the subpath, which cannot be modified. |
| Backend Interface Path | The path of requests sent by the gateway to the backend services. |
| Mapping mode | The mapping mode of the interface. Into the transparent transmission: In this mode, the interface definition is used only for documentation. The gateway does not verify or map the interface. In-parameter mapping (filtering unknown parameters): In this mode, the gateway filters out parameters that are not defined in the interface after receiving a request. For example, if you define query parameters a and b in the interface, but the request parameters are a=1&b=2&c=3, the gateway filters out c=3. The parameters forwarded to the backend services are a=1&b=2. Incoming parameter mapping (pass through unknown parameters): This mode is the opposite of the previous mode. In this mode, the gateway does not verify, filter out, or map parameters that are not defined in the interface. Instead, the gateway directly passes the parameters to the backend services. |

| Request Parameters | Configure the parameters on the Params, Body, and Header tabs based on your business requirements. For more information, see Request parameters in this topic. |
|---|---|

**Request parameters**

You can define request parameters for the interface. The request parameters consist of four parts. Query: the parameters appended to the URL in the format of ?a=&b=. Path: the request path. Body: the request body. Header: the request header. When you define request parameters, you can specify a backend path. The request path is mapped to the backend path. You can click **Edit More** to allow the gateway to verify the parameters.

**Constant parameter**

You can exclude some fixed parameters from the requests that you send and define them as constant parameters. This way, the gateway will automatically add these constant parameters to the requests it receives. Currently, only the Query and Header parameters can be specified as constant parameters.

**Return Response**

You can define the content to be returned by backend services. This setting is used only for demonstration in documentation.
8. Specify **Release Notes** and click **Determine**.

**Import interfaces**

You can import interfaces by using Swagger URLs.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. Click **Import**, specify **routePath**, enter a Swagger URL, specify **Release Notes**, and click
**Determine**.

**Note**

After you disable **Import and Publish**, an interface release operation is not synchronized to the portal, and the interface is not displayed in the portal.

**View interfaces**

After you add an interface, you can view it in the interface list and filter interfaces by interface name.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. Find the interface in the list and click its name to view interface documentation. You can
also filter interfaces by **interface name** or **interface path**.

**Interface version management**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. Click **Edit** in the upper-right corner. On the **Edit Interface** page, modify the interface and
click **Publish Interface**.
7. Specify **Release Notes**.
8. Click the **Version Management** tab to view the versions of the interface.
9. You can select a historical version of the interface.

**Perform interface debugging**

With the interface debugging feature, you can initiate a real-time call to the interface to check the real-time status of the interface and view the details of the request and response parameters of the interface.
1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. Select an interface and click **Debugging** in the Operation column.
7. Configure the parameters and click **Send**.

**Delete an interface**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List** or **API Gateway >**
**Shared Instance List**.
3. On the **Gateway instance** page, find the instance that you want to view and click the
instance ID or click **Details** in the **Operation** column.
4. In the left-side navigation pane, choose **Open Services > Routing Management**.
5. Find the route that you want to manage and click **Interface Center** in the **Operation**
column.
6. Select the interface that you want to delete and click **Delete** in the Operation column.
7. In the **Alert** message, click **Determine**.

**Parameter mapping instance**

**Example 1: Map parameters in Query to JSON**

The URL of the request sent to the gateway is as follows:

```
 /httpbin/anything?a=hello world&b=2
```

The backend interface parameters are as follows:

```json
{
  "a": "String",
  "b": "Integer"
}
```

The following figure shows the interface configuration on the gateway. For parameters that are mapped to jsonBody, the gateway creates a virtual root node. You need to specify the names of the backend parameters in a layered structure based on the root node.

```json
{
  "obj1": {
    "item1": "String",
    "item2": "String"
  }
}
```

**Example 2: Map complex JSON objects**

The parameters received by the backend services are as follows:

```json
POST /api/createApi HTTP/1.1 Content-Type: application/json {
  "obj": {
    "item1": "String",
    "item2": "List<String>",
  },
  "str": "String",
  "array": "List<Integer>"
}
```

| Parameter | Type | Whether the parameter is mapped to a backend parameter | Required |
|---|---|---|---|
| queryStr1 | String | root.obj.item1 | Yes |
| queryArray1 | List<String> | root.obj.item2 | Yes |
| queryStr2 | String | root.str | No |
| queryArray2 | List<Integer> | root.array | No |

The request parameters received by the gateway are included in Query. The following figures show the interface configuration on the gateway. After you use postman to initiate a request, the expected result is returned.

| Parameter | Type | Required | Verification rule |
|---|---|---|---|
| queryStr | String | Yes | Only English is allowed. |
| queryInt | Int | Yes | Valid values: 0 to 100. |
| queryArray | List<String> | Yes | Maximum length: 3. |

**Example 3: Verify parameters**

The request parameters received by the gateway are included in Query. The following figures show the interface configuration in the interface center. Use postman to initiate a request.

**Invalid request 1: the String parameter is invalid**

**Invalid request 2: excessively long array**

**Invalid request 3: invalid number**

| Log name | Description |
|---|---|
| access.log | Gateway request log. This log is enabled by default and records every request. |

## Gateway logs

This topic describes how to configure log collection for a gateway, the log classifications, and provides examples and details for the major log files.

**Configure log collection**

When a gateway is deployed using EDAS, you can collect logs in Simple Log Service (SLS). The steps and parameter settings are as follows: First, find the gateway instance in the instance list and navigate to the associated EDAS application. Then, configure log collection using the application deployment settings in EDAS. Log Type: File Log (Container Log Path) Collection Path: /home/admin/cop-broker/logs/*.log After the configuration is complete, you can view the collected gateway logs by category in SLS:

**Log classifications**

The collected logs are classified as follows:

| request.log | Gateway request body and response body log. This log is disabled by default. It records the request body and response body for every request. This log is disabled by default for performance reasons. If you enable it, gateway performance degrades sharply because it unpacks all requests and responses. Note Note the difference between access.log and request.log. The access.log file records only the URI information for each request and does not read the message body. The request.log file is used to troubleshoot business issues and records the specific message body. |
|---|---|
| config.log | Gateway configuration push log. Each time a push is received from the configuration center, the configuration content is printed. This helps troubleshoot configuration push issues. |
| schedule.log | Scheduled task run log. This file is used exclusively to record scheduled task logs to prevent them from interfering with other log outputs. |
| remoting.log | Connection log. This log records the establishment and disconnection of persistent connections between the gateway and backend services. It is used to troubleshoot network issues. |
| debug.log | Gateway business log. All other business information is output to this log. |

| No. | Description | SLS field |
|---|---|---|
| 1 | Gateway access start time | startTime |
| 2 | Request ID | requestId |
| 3 | Requested service name | serviceName |
| 4 | Gateway instance ID | gwInstanceId |

**access.log**

Log example:

```
[access] 2022-11-02 17:32:14.858 [INFO ] [reactor-http-kqueue-10] accessLog - 166738153 4546||httpbin|default-cop-broker-musi-5|null|null|null|null|/httpbin/get|/get|4c7906f1- 1378-48c0-befb-6294e3a320e7|httpbin|1667381534855|httpbin.org|-1|127.0.0.1|GET|200 OK|1 667381534855|0|473|1|null|1667381534858|312|custom:custom|
```

Details:

| 5 | Consumer ID | appId |
|---|---|---|
| 6 | Consumer name | appName |
| 7 | Token for authentication | token |
| 8 | Request signature | sign |
| 9 | Full request URL | url |
| 10 | Actual request URL | realRoutePath |
| 11 | Route ID | routeId |
| 12 | Route name | routeName |
| 13 | Service invocation start time | serviceInvokeStartTime |
| 14 | Requested domain name or IP address | requestIp |
| 15 | Request data size | inputDataSize |
| 16 | Client request IP address | clientIp |
| 17 | Request method | method |
| 18 | Response code | status |
| 19 | Service invocation end time | serviceInvokeEndTime |
| 20 | Service invocation round trip time | serviceRt |
| 21 | Response data size | outputDataSize |
| 22 | Indicates whether the call was successful | isSuccess |

| 23 | Error message | errorMsg |
|---|---|---|
| 24 | Gateway access end time | endTime |
| 25 | Gateway invocation round trip time | platformRt |
| 26 | Custom log items | customLogItems |

| No. | Description | SLS field |
|---|---|---|
| 1 | Corresponds to the requestId in access.log | request id _ |
| 2 | Request body | request body _ |
| 3 | Response body | response body _ |

**request.log**

Log example:

```json
[request] 2022-11-02 17:32:14.858 [INFO ] [reactor-http-kqueue-10] requestLog - {"reque stId":"7b1fe671-7ad7-4638-9863-3f9e1c4733da", "request_body":"request_body", "response_body":"response_body"}
```

Details: To ensure performance, request.log is disabled by default. You can enable it by configuring the following environment variable.

```
env:
  PRINT_REQUEST_INFO: true
```

| Parameter | Description |
|---|---|
| Instance Name | The name of the instance. The name must be 2 to 80 characters in length and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores ( ), and hyphens (-). _ |
| Number Of Instance Nodes | The number of nodes for the instance. The value can be from 1 to 100. |
| Specification | The instance types provided by the platform. |
| Gateway Type | Select API Gateway. |
| Deployment Architecture | Select EDAS. |

## Best practices

### Zone-disaster recovery

This topic describes how to enable zone-disaster recovery when you create an API Gateway 2.0 instance. API Gateway 2.0 supports multi-cluster deployments. To enable zone-disaster recovery, you can deploy a single API Gateway 2.0 instance to multiple Kubernetes (K8s) clusters when you create the instance.

**Procedure**

1. Log in to the API Gateway console.
2. In the left-side navigation pane, choose **API Gateway > Instance List**.
3. Click **Create an instance**.
4. Enter the configuration information. Set **Deployment Architecture** to **EDAS**. In the **EDAS**
**Configuration** section, associate your existing K8s clusters. Click **Submit** to create the
gateway instance. The following table describes some of the parameters.

| EDAS Configuration | Associate your existing K8s clusters. Keep the Microservices Namespace consistent. The Kubernetes Namespace can be configured as needed. The selected clusters must be in the same VPC as the backend service. |
|---|---|
