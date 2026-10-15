---
title: "Container Service for Kubernetes Distributed Cloud Container Platform ACK One User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 22
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Container Service for Kubernetes Distributed Cloud Container Platform ACK One User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%88%86%E5%B8%83%E5%BC%8F%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1ACK%20One/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Service%20for%20Kubernetes%20Distributed%20Cloud%20Container%20Platform%20ACK%20One%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# Container Service for Kubernetes Distributed Cloud Container Platform ACK One User Guide 20260629

Container Service for Kubernetes Distributed Cloud Container Platf ACK One?

## What is ACK One?

Distributed Cloud Container Platform for Kubernetes (ACK One) is an enterprise-class cloudnative platform provided by Alibaba Cloud. This platform can be used in hybrid cloud, multicluster, distributed computing, and disaster recovery scenarios. You can use ACK One to connect and manage Kubernetes clusters deployed on top of any infrastructure or in any regions. ACK One also provides APIs that are compatible with open source versions to help you manage and maintain computing, networks, storage, security, monitoring, logs, jobs, applications, and traffic. Container Service for Kubernetes Distributed Cloud Container Platf

## Log in to the ACK One

**console**

This topic describes how to log in to the ACK One console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. Container Service for Kubernetes Distributed Cloud Container Platf

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
5. In the top navigation bar, choose **Products > Computing > Container Service >**
**Distributed Cloud Container Platform ACK One** to go to the **ACK One** console.

| RBAC role | Permission |
|---|---|
| admin (administrator) | Provides read and write permissions on cluster-wide resources and resources in all namespaces. |
| dev (developer) | Provides read and write permissions on resources in the specified namespace. |

Container Service for Kubernetes Distributed Cloud Container Platf

## Authorization management

### Authorization overview

To use the features provided by Distributed Cloud Container Platform for Kubernetes (ACK One), you need to grant Role-Based Access Control (RBAC) permissions to the service account. This topic describes RBAC permissions and how to grant required permissions to the service account. By default, the account that creates a Fleet instance has RBAC permissions, and no additional authorization is required. A RAM role must be granted RBAC permissions before the RAM role can manage Kubernetes resources in ACK One clusters. System policies can be attached to RAM users to grant only the operation permissions on ACK One cluster resources. If you want to perform operations on Kubernetes resources (such as creating multi-cluster applications and obtaining multi-cluster application information) in a specific cluster by assuming a RAM role, you must grant RBAC permissions to the RAM role to perform operations on the specified ACK One cluster and namespace. ACK One provides the following predefined roles:

**RBAC permissions on multi-cluster Fleet instances**

For more information about the resources controlled by RBAC permissions and how to grant permissions, see Grant RBAC permissions to a RAM role.

### Attach system policies to a

**RAM role**

If you need to use the features of ACK One by assuming a RAM role, you must grant the role the permissions to perform operations, such as creating Fleet instances and associating clusters, on ACK One. ACK One provides default system policies to control global read and write permissions. This topic describes how to attach a system policy to a RAM role.

**Usage notes**

You need to grant permissions to a RAM role by using an administrator account. You cannot grant permissions by using a RAM user.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

| RBAC role | RBAC permission |
|---|---|
| admin (administrator) | Provides read and write permissions on cluster-wide resources and resources in all namespaces. |
| dev (developer) | Provides read and write permissions on resources in the specified namespace. |

Container Service for Kubernetes Distributed Cloud Container Platf
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions > Role Permissions**.
4. On the Role Permissions page, click **Create Custom Role** to go to the **Create Role** page.
5. In the **Basic Configurations** step, configure the parameters and click **Next**. For more
information about how to configure the parameters, see **Manage custom roles** in **Apsara**
**Uni-manager Management Console User Guide**.
6. In the **Management Permissions** step, select the management permissions that you
want to grant to the role and click **Next**.
7. In the **Application Permissions** step, select **Cluster Authorization** in the Distributed
Cloud Container Platform section that you want to grant to the role and click **Next**.
8. In the **Menu Permissions** step, select the menu items that you want to authorize the role
to access and click **Next** or **Create**. For more information, see **Manage custom roles** in
**Apsara Uni-manager Management Console User Guide** .
9. Return to the **Role Permissions** page. Find the created role and click **Authorize** in the
**Actions** column. Select the users or user groups that you want to authorize and click **OK**.

### Grant RBAC permissions to a

**RAM role**

System policies can be attached to RAM users to grant only the operation permissions on Distributed Cloud Container Platform for Kubernetes (ACK One) cluster resources. The operation permissions include creating and viewing instances. If you want to perform operations on Kubernetes resources in a specific cluster by assuming a RAM role, you must grant Role-Based Access Control (RBAC) permissions to the RAM role to perform operations on the specified ACK One cluster and namespace. This topic describes how to grant RBAC permissions to a RAM role.

**Usage notes**

You must use an administrator account or a RAM user that has the **cluster authorization** permission to grant permissions to the specified RAM role. For more information, see Attach a system permission policy to a RAM role.

**RBAC permissions supported by ACK One**

**RBAC permissions on multi-cluster Fleet instances**

**View cluster and namespace resources**

Fleet instance-scoped resources

| Kind | apiVersion |
|---|---|
| Namespace | v1 |
| Managedcluster | cluster.open-cluster-management.io |
| MseIngressConfig | mse.alibabacloud.com/v1alpha1 |
| IngressClass | networking.k8s.io/v1 |

| Kind | apiVersion |
|---|---|
| Deployment | apps/v1 |
| Service | v1 |
| Ingress | networking.k8s.io/v1 |
| ConfigMap | v1 |
| Secret | v1 |
| StatefulSet | apps/v1 |
| PersistentVolumeClaim | v1 |
| ServiceExport | multicluster.x-k8s.io/v1alpha1 |
| ServiceImport | multicluster.x-k8s.io/v1alpha1 |
| HorizontalPodAutoscaler | autoscaling/v1 |
| Application ApplicationSet Appproject | argoproj.io |

Container Service for Kubernetes Distributed Cloud Container Platf Namespace-scoped resources

| Workflow | argoproj.io |
|---|---|
| Application | core.oam.dev |

| Kind | apiVersion |
|---|---|
| Application | argoproj.io |

Container Service for Kubernetes Distributed Cloud Container Platf Application resources in the argocd namespace

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Authorization Management**.
3. On the **Authorization Management** page, select a Fleet instance from the **Fleet** drop-
down list.
4. Find the RAM user that you want to authorize in the list and click **Authorization**
**Management** in the **Action** column.
5. In the dialog box that appears, specify **RAM Role Authorization** and click **OK**.

**Note**

You can select **Operations Administrator** or **Developer** for **RAM Role**
**Authorization**.
You can click **Revoke Authorization** in the **Action** column to revoke the authorization. Distributed Cloud Container Platf Container Service for Kubernetes

## Fleets

### Manage Fleet instances

#### Fleet management overview

Due to the wide adoption of Kubernetes, enterprises may want to run and manage multiple Kubernetes clusters. This brings challenges such as how to manage multiple clusters, how to use a unified external ingress to access the clusters, and how to schedule resources for the clusters. The Fleet instances of Distributed Cloud Container Platform for Kubernetes (ACK One) are managed by Container Service for Kubernetes (ACK). You can use the Fleet instances to manage Kubernetes clusters that are deployed in different environments in a centralized manner. Fleet instances create a consistent experience for enterprises that want to manage cloud-native applications.

**Core concepts**

**Fleet instance**: Fleet instances are designed based on open source projects Argo CD and
Open Cluster Management. Fleet instances support traffic control, provide multi-cluster application distribution, and allow developers to call the same Kubernetes API to schedule and distribute workloads, applications, and configuration files. Fleet instances are maintenance-free because they are managed by ACK. You can focus on application development.
**Associated cluster**: You can associate ACK clusters that belong to the same account with a
Fleet instance. Then, you can use the Fleet instance to distribute applications and workloads to the associated clusters. You can associate a Fleet instance with clusters that are not deployed in the region where the Fleet instance resides.
**Fleet instance administrator**: Fleet instance administrators are the creators of Fleet
instances. Fleet instance administrators can create namespaces, set the priorities of Jobs, and configure resource quotas for accounts that are assigned the developer role.
**Developer**: Accounts that are assigned the developer role can only submit Jobs or publish
applications in specific namespaces.

**Scenarios**

Container Service for Kubernetes Distributed Cloud Container Platf Unified Control Plane

**ACK One Fleet**

Multi-cluster Resource Distribution Distribution Open Cluster Management Apsara Data Stack Center Deployment/Svc Deployment/Svc Multi-cluster Svc Multi-cluster Svc Job Job ACK Cluster K8s Cluster The Fleet management feature of ACK One is ideal for the following scenarios: The control plane is built based on Kubernetes control planes and provides Kubernetes APIs. You can connect external Kubernetes clusters to a multi-cluster Fleet instance based on a registered cluster. Multi-cluster application distribution: The managed open source Argo CD is used for multicluster application distribution.

#### Network design for Fleet management

You can use the Fleet management feature to manage multiple clusters that are associated with a Fleet instance across regions. To enable the Fleet management feature, you must specify the region, virtual private cloud (VPC), and vSwitch information for the Fleet instance. This topic describes the architecture that is used to connect the network of a Fleet instance to the network of the associated clusters. This topic also describes how to specify a proper region, VPC, and vSwitch for a Fleet instance.

**Network architecture**

The following figure shows the network architecture that is used by Distributed Cloud Container Platform for Kubernetes (ACK One) for Fleet management. ACK Cluster 1 and ACK Cluster 2 are deployed in VPC 1 in Region 1. ACK Cluster 3 is deployed in VPC 2 in Region 2. The system administrator can access the endpoint of the API server of the Fleet instance to manage the associated clusters.

| Admin | istrator |  |  |  | Region 2 VPC 1 VP 1 API Server SLB Applications ACK Cluster 3 VPC Interconnection 2 |  |  |
|---|---|---|---|---|---|---|---|
| Region 1 API Server SLB ACK One Fleet Instance 1 1 API Server SLB API Server SLB Applications Applications ACK Cluster 1 ACK Cluster 2 2 2 |  |  |  |  |  | Region 2 VP API Server SLB Applications ACK Cluster 3 rconnection 2 |  |
|  |  |  |  |  | 1 VPC Inte |  |  |
|  |  | Applications |  |  |  |  |  |
|  |  |  |  | uster 2 2 |  |  |  |

|  | API Server SLB |  |  |
|---|---|---|---|
| Applications |  |  |  |

Distributed Cloud Container Platf Container Service for Kubernetes The connections marked by Circled Number 1 in the following figure indicate that the VPC of the Fleet instance can access the endpoints of the API servers of the associated clusters. The connections marked by Circled Number 2 in the following figure indicate that the VPCs of the associated clusters can access the endpoint of the API server of the Fleet instance.

**How to select a region**

A Fleet instance serves as an ingress to the clusters that are associated with the Fleet instance. We recommend that you select a region that is close to most of the associated clusters. In the preceding figure, two associated clusters are deployed in Region 1 and one associated cluster is deployed in Region 2. In this scenario, you can deploy the Fleet instance in Region 1.

**Important**

You can create more than one Fleet instance for multi-cluster management based on various factors, such as the business type, nearest region, test environment, and production environment. Each associated cluster can be managed by only one Fleet instance.

**How to select a VPC**

To use a Fleet instance to centrally manage the associated clusters, you must create network connections from the Fleet instance to the associated clusters. This way, the Fleet instance and associated clusters can access the endpoints of the API servers of each other.
1. The connections marked by Circled Number 1 in the preceding figure indicate that the VPC
of the Fleet instance can access the endpoints of the API servers of the associated clusters.
2. The connections marked by Circled Number 2 in the preceding figure indicate that the VPCs
of the associated clusters can access the endpoint of the API server of the Fleet instance.
3. If the Fleet instance and the associated clusters are deployed in different VPCs, you must
connect the VPCs to ensure that the API servers of the Fleet instance and associated clusters can access each other.

**Important**

| Parameter | Description |
|---|---|
| Fleet Name | Enter a name for the Fleet instance. Note The name must be 1 to 63 characters in length. It can contain letters, digits, underscores ( ), and hyphens (-). It must start _ with a letter or digit. |
| Organization | Select the organization to which the Fleet instance belongs. |
| Resource Set | Select the resource set to which the Fleet instance belongs. |
| Region | Select the region to which the Fleet instance belongs. |
| Virtual Private Cloud | Select a virtual private cloud (VPC) for the Fleet instance. |

Container Service for Kubernetes Distributed Cloud Container Platf Make sure that the security groups of the Fleet instance and the associated clusters accept connection requests from each other. When you specify the VPC of a Fleet instance, we recommend that you select the VPC in which most of the associated clusters reside. This way, the Fleet instance is automatically connected to the associated clusters by using VPC private connections. For example, ACK Cluster 1 and ACK Cluster 2 are deployed in VPC 1, and ACK Cluster 3 is deployed in VPC 2. In this scenario, you can deploy the Fleet instance in VPC 1.

**How to select a vSwitch**

Fleet instances do not have specific requirements on vSwitches. You can select a vSwitch based on your network design.

#### Create a Fleet instance

This topic describes how to create a Fleet instance.

**Prerequisites**

You are assigned the operations administrator or organization administrator role. If you are assigned a custom role, the custom role must be granted the permissions to access the
**Authorization Management** page. For more information, see Attach a system permission
policy to a RAM role.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. On the **Fleet List** page, click **Create**.
4. On the **Create Fleet** page, configure the following parameters and click **Submit**.

| vSwitch | Select a vSwitch for the Fleet instance. |
|---|---|
| Create and Bind EIP | Specify whether to expose the API server to external access. By default, the API server is not exposed to external access. Important If you turn on this switch, an elastic IP address (EIP) is created and associated with the internal-facing Server Load Balancer (SLB) instance of the API server. The EIP is used to expose the API server to external access. The EIP cannot be disassociated because the clusters that are associated with the Fleet instance may use the public endpoint of the Fleet instance. |
| API Server Load Balancer | Default value: Standard Type 1 (slb.s2.small). You cannot change the default setting. |

Distributed Cloud Container Platf Container Service for Kubernetes
5. Click **Submit**.
Wait a few minutes. After the status of the Fleet instance changes to **Running**, the Fleet instance is created.

#### View the details of a Fleet instance

This topic describes how to view the details of a Fleet instance.

**Procedure**

After a Fleet instance is created, you can view the basic information, connection information, logs, and associated clusters of the Fleet instance.
1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. Optional. On the **Fleet List** page, specify the **Fleet ID** parameter to search for fleets.
4. On the Fleet List page, find the Fleet instance that you want to manage and click the Fleet
instance ID or click **Details** in the **Action** column.

**Note**

On the **Fleet Information** page, click **Delete** or **Refresh** in the upper-right corner to delete the Fleet instance or refresh the fleet instance information. On the **Basic Information** tab, you can view the name, ID, status, region, creation time, API Server endpoints, and other network information of the Fleet instance.

**Note**

You can turn on or off Deletion Protection for the Fleet instance. After you turn on Deletion Protection, you cannot delete the Fleet instance. Container Service for Kubernetes Distributed Cloud Container Platf On the **Connect to Fleet** tab, you can view the content of the kubeconfig files for internal access and external access. The kubeconfig files store the configurations for connecting kubectl to the Fleet instance over the Internet and internal network. On the **Fleet Logs** tab, you can view the logs of the Fleet instance.

**Note**

On the **Fleet List** page, click **View Logs** in the **Action** column to go to the **Fleet**
**Logs** tab.
On the **Associate Cluster** tab, associate clusters with the Fleet instance. For more information, see Manage associated clusters.

#### Delete a Fleet instance

This topic describes how to delete a Fleet instance.

**Prerequisites**

Before you delete a Fleet instance, you must remove the clusters associated with the Fleet instance. For more information, see Disassociate clusters from a Fleet instance.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. On the Fleet List page, find the Fleet instance that you want to delete and click **Delete** in
the **Action** column.
4. In the message that appears, click **OK**.

### Manage associated clusters

#### Associate clusters with a Fleet instance

After you create a Fleet instance, you can associate clusters with the Fleet instance, and then deploy applications and workloads to the associated clusters from the Fleet instance. You can associate a Fleet instance with clusters that reside outside the region of the Fleet instance. This topic describes how to associate clusters with a Fleet instance.

**Prerequisites**

A Fleet instance is created and is in the **Running** state. For more information, see Create a Fleet instance.

**Limits**

The cluster to be associated and the Fleet instance are deployed in the same virtual private cloud (VPC). If the cluster and Fleet instance belong to different VPCs, you must establish a network connection between the cluster and the Fleet instance. You can associate or disassociate at most 10 clusters at a time.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
Distributed Cloud Container Platf Container Service for Kubernetes
3. On the Fleet List page, find the Fleet instance that you want to manage and click the Fleet
instance ID or click **Details** in the **Action** column.
4. On the **Fleet Information** page, click the **Associate Cluster** tab.
5. On the **Associate Cluster** tab, click **Associate Cluster**.
6. In the **Associate Cluster** panel, select the cluster to be associated and click **OK**.
Wait a period of time (less than 5 minutes). On the **Associate Cluster** page, if the
**Association Status** of the cluster displays **Associated successfully**, the cluster is
associated with the Fleet instance. Click **Details** in the **Actions** column to go to the **Basic**
**Information** page of the cluster.

**Note**

After the cluster is associated, you need to manually refresh the Fleet management page to view the updated list of associated clusters. The following list describes the states of an associated cluster:
**Processing**: The request for associating the cluster is submitted to the Fleet
instance.
**Associating**: The Fleet instance has received the association request and the
cluster is being associated with the Fleet instance.
**Associated successfully**: The cluster is associated with the Fleet instance.
**Failed to associate**: The system failed to associate the cluster with the Fleet
instance.

#### Disassociate clusters from a Fleet

**instance**

This topic describes how to disassociate the clusters that are associated with a Fleet instance.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. On the Fleet List page, find the Fleet instance that you want to manage and click the Fleet
instance ID or click **Details** in the **Action** column.
4. On the **Fleet Information** page, click the **Associate Cluster** tab.
5. Disassociate clusters
Disassociate a single cluster: On the **Associate Cluster** tab, find the cluster that you want to disassociate from the Fleet instance and click **Disassociate** in the **Actions** column. Disassociate multiple clusters at a time: On the **Associate Cluster** tab, select multiple associated clusters and click **Batch Disassociate** below the list.
6. In the message that appears, click **OK**.

| Parameter | Description |
|---|---|
| Name | Specify a name for the namespace. The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). It must start and end with a letter or digit. |
| Tag | You can add multiple tags to a namespace. Tags are used to identify namespaces. For example, you can tag a namespace as one that is used in the test environment. To add a tag, enter a key and a value. You can clickA dd to add more tags. |

Container Service for Kubernetes Distributed Cloud Container Platf

**Note**

Wait a period of time and refresh the **Associate Cluster** tab. If the clusters are removed from the list of associated clusters, the clusters are disassociated.

### Manage namespaces

#### Create a namespace

This topic describes how to create a namespace.

**Prerequisites**

A Fleet instance is created. For more information, see Create a Fleet instance.

**Background information**

In a Kubernetes cluster, you can use namespaces to create multiple virtual spaces. When a large number of users share a cluster, you can use namespaces to divide different workspaces and allocate cluster resources to different tasks.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Namespace**.
5. On the **Namespace** page, click **Create Namespace**.
6. In the **Create Namespace** dialog box, enter a namespace name and a tag, and click **OK**.

#### Modify the tags of a namespace

This topic describes how to modify the tags of a namespace.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
Distributed Cloud Container Platf Container Service for Kubernetes
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Namespace**.
5. On the **Namespace** page, find the namespace that you want to manage and click **Edit** in
the **Action** column.
6. In the dialog box that appears, modify, add, or delete tags, and then click **OK**.

#### Delete a namespace

This topic describes how to delete a namespace.

**Usage notes**

When you delete a namespace, all resource objects under the namespace are deleted. Proceed with caution.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Namespace**.
5. On the **Namespace** page, find the namespace that you want to manage and click **Delete**
in the **Action** column.
6. In the message that appears, click **OK**.

### Manage multi-cluster

**applications**

#### Create a multi-cluster application

This topic describes how to create a multi-cluster application.

**Background information**

Multi-cluster applications are supported. You can use an Argo CD ApplicationSet to automatically create one or more applications from one orchestration template.

**Prerequisites**

A Fleet instance is created. For more information, see Create a Fleet instance. The Fleet instance is associated with multiple clusters. For more information, see Associate clusters with a Fleet instance. A namespace is created. For more information, see Create a namespace.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Multi-Cluster Application**.

| Parameter | Description |
|---|---|
| Multi-Cluster Application Name | The name of the application. |
| Chart Name | The name of the Helm chart that defines the application template to be deployed. |
| Chart URL | The URL of a Helm chart repository (HTTP/HTTPS URL) or the URL of an OCI image repository (such as in the image repository address/namespace format for Container Registry Advanced Edition). Currently, only public image repositories are supported. |
| Version | The chart version to use. |
| Destination Cluster | The destination cluster where the application will be deployed. |
| Namespace | The namespace where the application will be deployed in the cluster. |

Container Service for Kubernetes Distributed Cloud Container Platf
5. On the **Multi-Cluster Application** page, click **Create Multi-Cluster Application**.
6. In the **Create Multi-Cluster Application** panel, configure the following parameters and
click **OK**.

#### View the information about multi-

**cluster applications**

This topic describes how to view the information about multi-cluster applications under a Fleet instance.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Multi-Cluster Application**.
5. Optional. On the **Multi-Cluster Application** page, enter a multi-cluster application name
to filter applications.
6. In the multi-cluster application list, you can view **Tag Name**, **Type**, **Deployment State**,
**Application**, **Namespace**, and **Creation Time** of multi-cluster applications.
Distributed Cloud Container Platf Container Service for Kubernetes

**Note**

Click a number in the **Application** column to view the application summary information about the multi-cluster application. Click **View YAML** in the **Action** column to view the YAML information of the multi-cluster application (ArgoCD ApplicationSet resource).

#### Modify the configuration of a multi-

**cluster application**

This topic describes how to modify the configuration of a multi-cluster application.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Multi-Cluster Application**.
5. On the **Multi-Cluster Application** page, find the application that you want to manage and
click **Edit** in the **Action** column.
6. On the **Edit Multi-Cluster Application** page, modify the configuration and click **OK**.

**Note**

You cannot modify the name of a multi-cluster application.

#### Delete a multi-cluster application

This topic describes how to delete a multi-cluster application.

**Usage notes**

After you delete a multi-cluster application, the corresponding applications deployed in the associated clusters will also be deleted.

**Procedure**

1. Log in to the ACK One console.
2. In the left-side navigation pane, click **Fleet List**.
3. In the fleet list, click the ID of the desired fleet or click **Details** in the **Actions** column.
4. In the left-side navigation pane, click **Multi-Cluster Application**.
5. On the **Multi-Cluster Application** page, find the application that you want to manage and
click **Delete** in the **Action** column.
6. In the message that appears, click **OK**.
