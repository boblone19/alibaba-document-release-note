---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 222
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Container%20Service%20for%20Kubernetes%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Container Service for Kubernetes User Guide 20220928

## Table of Contents

- 1 Container Service support for Kubernetes 1.18
- 2 What is Container Service?
- 3 ACK@Edge overview
- 4 Planning and preparation
- 5 Quick start
  - 5.1 Procedure
  - 5.2 Log on to the Container Service console
  - 5.3 Create a Kubernetes cluster
  - 5.4 Create an application from an orchestration template
- 6 Kubernetes clusters
  - 6.1 Authorizations
    - 6.1.1 Assign RBAC roles to a RAM user
  - 6.2 Clusters
    - 6.2.1 Create a Kubernetes cluster
    - 6.2.2 Create an edge Kubernetes cluster
    - 6.2.3 View log files of a cluster
    - 6.2.4 Connect to a cluster through kubectl
    - 6.2.5 Connect to a master node by using SSH
    - 6.2.6 Expand a cluster
    - 6.2.7 Renew a certificate
    - 6.2.8 Delete a Kubernetes cluster
    - 6.2.9 View cluster overview
  - 6.3 Nodes
    - 6.3.1 Add existing nodes to a Kubernetes cluster
    - 6.3.2 Add nodes to an edge Kubernetes cluster
    - 6.3.3 View nodes
    - 6.3.4 Manage node labels
    - 6.3.5 Set node schedulability
    - 6.3.6 Remove a node
    - 6.3.7 View node resource usage
    - 6.3.8 Upgrade the NVIDIA driver on a GPU node
    - 6.3.9 GPU scheduling for Kubernetes clusters with GPU-accelerated nodes
    - 6.3.10 Use labels to schedule pods to GPU-accelerated nodes
    - 6.3.11 Manually upgrade the kernel of a GPU node in a cluster
    - 6.3.12 Node pools
      - 6.3.12.1 Create a node pool
      - 6.3.12.2 Scale out a node pool
      - 6.3.12.3 Schedule an application pod to a specific node pool
  - 6.4 Storage
    - 6.4.1 Overview
    - 6.4.2 Mount disk volumes
    - 6.4.3 Mount NAS volumes
    - 6.4.4 Mount OSS volumes
    - 6.4.5 Create a PVC
    - 6.4.6 Use PVCs
  - 6.5 Network management
    - 6.5.1 Set access control for pods
    - 6.5.2 Set bandwidth limits for pods
    - 6.5.3 Work with Terway
  - 6.6 Namespaces
    - 6.6.1 Create a namespace
    - 6.6.2 Set resource quotas and limits
    - 6.6.3 Modify a namespace
    - 6.6.4 Delete a namespace
  - 6.7 Applications
    - 6.7.1 Create an application from an image
    - 6.7.2 Create an application from an orchestration template
    - 6.7.3 Use commands to manage applications
    - 6.7.4 Create a Service
    - 6.7.5 View a Service
    - 6.7.6 Update a Service
    - 6.7.7 Delete a Service
    - 6.7.8 Use a trigger to redeploy an application
    - 6.7.9 View pods
    - 6.7.10 Manage pods
    - 6.7.11 Schedule pods to specific nodes
    - 6.7.12 Simplify application deployment by using Helm
  - 6.8 SLB and Ingress
    - 6.8.1 Overview
    - 6.8.2 Use SLB to access Services
    - 6.8.3 Configure Ingress monitoring
    - 6.8.4 Ingress support
    - 6.8.5 Ingress configurations
    - 6.8.6 Create an Ingress in the console
    - 6.8.7 Update an Ingress
    - 6.8.8 Delete an Ingress
  - 6.9 Config maps and secrets
    - 6.9.1 Create a ConfigMap
    - 6.9.2 Use a ConfigMap in a pod
    - 6.9.3 Update a ConfigMap
    - 6.9.4 Delete a ConfigMap
    - 6.9.5 Create a Secret
    - 6.9.6 Modify a Secret
    - 6.9.7 Delete a Secret
  - 6.10 Templates
    - 6.10.1 Create an orchestration template
    - 6.10.2 Update an orchestration template
    - 6.10.3 Save an orchestration template as a new one
    - 6.10.4 Download an orchestration template
    - 6.10.5 Delete an orchestration template
  - 6.11 Auto scaling
    - 6.11.1 Auto scaling of nodes
    - 6.11.2 Horizontal pod autoscaling
  - 6.12 Sandboxed-containers
    - 6.12.1 Overview
    - 6.12.2 Create a Kubernetes cluster that runs sandboxed containers
    - 6.12.3 Expand a Container Service cluster that runs sandboxed containers
    - 6.12.4 Create an application that runs in sandboxed containers
    - 6.12.5 Configure a Kubernetes cluster that runs both sandboxed and Docker containers
    - 6.12.6 How do I select between Docker and Sandboxed-Container?
    - 6.12.7 Benefits of Sandboxed-Container
    - 6.12.8 Differences between runC and runV
    - 6.12.9 Compatibility notes
  - 6.13 Use the Kubernetes event center
  - 6.14 Use Log Service to collect log data from containers

t for Kubernetes 1.18

## 1 Container Service support for Kubernetes 1.18

Kubernetes 1.18 Container Service strictly conforms to the terms of the Certified Kubernetes Conformance Program. This topic describes the changes that Container Service has made to support Kubernetes 1.18. Version upgrades Container Servcie has upgraded and optimized all of its components to support Kubernetes 1.18.8.

| Key component | Version | Description |
|---|---|---|
| Kubernetes | 1.18.8 | Some frequently used API versions are deprecated in Kubernetes 1.18. Before you upgrade a Kubernetes cluster, we recommend that you upgrade the deprecated API versions that are listed in this topic. |
| Docker | 19.03.5 (containerd 1.2.10) | No. |
| etcd | 3.4.3 | No. |
| CoreDNS | 1.6.7 | No. |

Version details Resource changes and deprecat ion The following APIs are deprecated in Kubernetes 1.18: The APIs apps/v1beta1 and apps/v1beta2 of all the resources are replaced by apps/v1. The API extensions/v1beta1 of DaemonSets, Deployments, and ReplicaSets is replaced by apps/v1. The API extensions/v1beta1 of Networkpolicies resources is replaced by net working.k8s.io/v1. The API extensions/v1beta1 of pod security policies is replaced by policy/v1bet a1. The label that specifies the regions of a node is changed to topology.kubernetes.io/region. The label that specifies the zone of a node is changed to topology.kubernetes.io/zone. We recommend that you update the related configurations for your workloads. Feat ure upgrades Server-side Apply Beta 2 is introduced. You can view the relationships between the configuration items of a resource in the metadata.managedFields field of the resource. The Node Local DNS Cache feature is released to improve the DNS availability and performance of your cluster. The Volume Snapshot feature is in public preview and supports operations such as data volume backup, recovery, and scheduled backup. Container Service upgrades for Kubernetes 1.18.8 t for Kubernetes 1.18 In Kubernetes 1.18.8, Container Service enables the following feature in the kubelet configuration file: Users who use raw data volumes can upgrade clusters without the need to drain the nodes. e?

## 2 What is Container Service?

Container Service provides high-performance, scalable, and enterprise-class management service for Kubernetes containerized applications throughout the application lifecycle. Container Service simplifies the deployment and scaling operations on Kubernetes clusters. Integrated with services such as virtualization, storage, network, and security, Container Service aims to provide the optimal cloud environment for Kubernetes containerized applications. Alibaba Cloud is a Kubernetes Certified Service Provider (KCSP). As one of the first services to participate in the Certified Kubernetes Conformance Program, Container Service provides you with professional support and services.

## 3 ACK@Edge overview

ACK@Edge is released for commercial use. ACK@Edge is a cloud-managed solution that is provided by Container Service to coordinate cloud and edge computing. This topic describes the background and features of edge Kubernetes clusters. Overview With the rapid growth of smart devices connected to the Internet and the advent of 5G and IoT, computing and storage services provided by traditional cloud computing platforms can no longer satisfy the needs of edge devices for time-efficient computing, larger storage capacity, and enhanced computing capacity. Edge Kubernetes clusters are intended for bringing cloud computing to edges (clients). Edge Kubernetes clusters can be created, managed, and maintained in the Container Service console. This is the trend of cloud computing. An edge Kubernetes cluster is a standard, secure, and highly-available Kubernetes cluster deployed in the cloud. This type of cluster is integrated with features of Alibaba Cloud, such as virtualization, storage, networking, and security. This simplifies the management and maintenance of clusters and allows you to focus on your business development. ACK@Edge provides the following features: Allows you to build a cloud-native infrastructure for edge computing with a few clicks. Allows you to quickly connect edge computing resources to the cloud. These resources include IoT gateway devices, terminals, Content Delivery Network (CDN) resources, and data centers. Applies to diverse scenarios, such as edge intelligence, intelligent buildings, intelligent factories, audio and video live streaming, online education, and CDN. Edge Kubernetes clusters support features such as node autonomy, cell-based management, and native APIs for the management and maintenance of resources at the edge side. To use these features, you do not need to rewrite the logic of your services. This provides a native and centralized method for application lifecycle management and resource scheduling in edge computing scenarios. Features Edge Kubernetes clusters provide the following features to support lifecycle management for containerized applications and resources in edge computing scenarios: Allows you to create highly available edge Kubernetes clusters with a few clicks and provides lifecycle management on edge Kubernetes clusters, such as scaling cloud nodes, adding edge nodes to clusters, upgrading, logging, and monitoring. You can perform the preceding operations in the Container Service console. Supports access to various heterogeneous resources, such as data centers and IoT devices. Hybrid scheduling of heterogeneous resources is also supported. Supports node autonomy and network autonomy to ensure the reliability of edge nodes and services in edge computing scenarios where the network connection is weak. Supports reverse tunneling for management and maintenance of edge nodes. n

## 4 Planning and preparation

Before you start using Container Service, you need to create cloud resources such as VPC networks, VSwitches, disks, and OSS buckets based on your application requirements. Before you create a Kubernetes cluster, make the following preparations: Creat e a VPC net work (optional) To create a cluster in an existing VPC network, you must create the VPC network and VSwitches in advance. Creat e a volume (optional) To create a stateful application with network storage, you must create disks or OSS buckets in advance.

## 5 Quick start

### 5.1 Procedure

You can perform the following steps to use the Container Service service. The following diagram shows the procedure to use the Container Service service. St ep 1: Aut horize t he def ault role Authorize the default role of Container Service to perform operations on the resources that belong to the specified organization. St ep 2: Log on t o t he Cont ainer Service console Log on to the Container Service console. For more information, see Log on to the Container Service console. St ep 3: Creat e an Cont ainer Service clust er Set the network environment and the number of nodes, and configure node details. St ep 4: Deploy an applicat ion by using an image or orchest rat ion t emplat e You can use an existing image or orchestration template, or create a new image or orchestration template. To create an application that consists of services based on different images, use an orchestration template. St ep 5: Manage t he applicat ion lif ecycle

### 5.2 Log on to the Container Service console

console You can perform the following steps to log on to the Container Service console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Cont ainer Service f or
Kubernet es.
5. Select the required organization and region.
6. Click ACK to go to the Container Service console.

### 5.3 Create a Kubernetes cluster

This topic describes how to create a Kubernetes cluster in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers. On the Clusters page that appears, click Creat e
Kubernet es Clust er in the upper-right corner.
3. On the Creat e Kubernet es Clust er page, set the parameters.

| Parameter | Description |
|---|---|
| Cluster Name | Enter a name for the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). Not e The cluster name must be unique among clusters that belong to the same Alibaba Cloud account. |
| Region | Select the region where you want to deploy the cluster. |

| Parameter | Description |
|---|---|
| VPC | You can select a virtual private cloud (VPC) from the drop-down list. If the specified VPC is already associated with a NAT gateway, the cluster uses this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear Conf igure SNAT f or VPC. Not e If you disable the system to automatically create a NAT gateway and want the VPC to access the Internet, you must manually associate the VPC with a NAT gateway or create Source Network Address Translation (SNAT) rules for the VPC. |
| VSwitch | Select one or more vSwitches for the cluster. You can select up to three vSwitches that are deployed in different zones. |
| Kubernetes Version | Select a Kubernetes version. |
| Container Runtime | You can select Docker or Sandboxed-Container. |
| Billing Method | Only pay-as-you-go nodes are supported. |
| Master Configurations | Set the Instance Type and System Disk parameters: Master Node Quantity: You can add up to three master nodes. Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. |
| Worker Instance | You can select Creat e Inst ance or Add Exist ing Inst ance. |

| Parameter | Description |
|---|---|
| Worker Configurations | If Worker Inst ance is set to Creat e Inst ance, set the following parameters: Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. Selected Types: The selected instance types are displayed. Quantity: Set the number of worker nodes. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. Mount Data Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Encrypt Disk to encrypt disks. You can select Enable Backup to back up disk data. |
| Operating System | The CentOS and Aliyun Linux operating systems are supported. |
| Password | Set a password that is used to log on to the nodes. Not e The password must be 8 to 30 characters in length, and must contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. |
| Confirm Password | Enter the password again. |
| Network Plug-in | Flannel and Terway are supported. By default, Flannel is selected. |

| Parameter | Description |
|---|---|
| Pod CIDR Block and Service CIDR | These parameters are optional. For more information, see Network planning in VPC User Gui de. Not e These parameters are available only when you select an existing VPC. |
| Configure SNAT | This parameter is optional. If you clear Configure SNAT for VPC, you must create a NAT gateway or configure SNAT rules for the VPC. |
| Access to the Internet | Specify whether to expose the API server with an elastic IP address (EIP). The Kubernetes API server provides multiple HTTP-based RESTful APIs that can be used to create, delete, modify, query, and watch resource objects such as pods and Services. If you select this check box, an EIP is created and associated with an internal-facing Server Load Balancer (SLB) instance. Port 6443 used by the API server is exposed on the master nodes. You can connect to and manage the cluster by using kubeconfig over the Internet. If you clear this check box, no EIP is created. You can connect to and manage the cluster only by using kubeconfig within the VPC. |
| Ingress | Specify whether to Inst all Ingress Cont rollers. By default, Inst all Ingress Cont rollers is selected. |
| Log Service | If you enable Log Service, you can select an existing project or create a project. If you select Enable Log Service, the Log Service plug-in is automatically installed in the cluster. If you select Creat e Ingress Dashboard, Ingress access logs are collected and displayed on dashboards. |
| Volume Plug-in | By default, CSI is selected. |
| Deletion Protection | This check box prevents you from accidentally deleting the cluster in the console or by calling API operations. |

| Parameter | Description |
|---|---|
| RDS Whitelist | Add the IP addresses of the nodes to the whitelist of the ApsaraDB RDS instance that is allowed to access the Kubernetes cluster. Not e To enable an ApsaraDB RDS instance to access the Kubernetes cluster, you must deploy the ApsaraDB RDS instance in the same VPC as the Kubernetes cluster. |
| Node Protection | This check box is selected by default to prevent you from accidentally deleting the nodes in the console or by calling API operations. |
| Label | Add labels to the cluster. |

4. Complete the advanced settings of the cluster.

| Parameter | Description |
|---|---|
| IP Addresses per Node | The number of IP addresses that are assigned to a node. |
| Custom Image | You can select a custom image. After you select a custom image, all nodes in the cluster are deployed by using this image. |
| Kube-proxy Mode | ipt ables and IPVS are supported. iptables is a tested and stable kube-proxy mode. It uses iptables rules to conduct service discovery and load balancing. The performance of this mode is limited by the size of the Kubernetes cluster. This mode is suitable for Kubernetes clusters that manage a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux Virtual Server (LVS) to conduct service discovery and load balancing. This mode is suitable for Kubernetes clusters that manage a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. |
| Custom Node Name | Specify whether to use a custom node name. |
| Node Port Range | Specify the value of Node Port Range. |
| Taints | Add taints to all worker nodes in the Kubernetes cluster. |

| Cont | ainer Service for Kubernetes | User Guide·Quick star | t |
|---|---|---|---|

| Parameter | Description |
|---|---|
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |
| Cluster Domain | The default domain name of the cluster is cluster.local. You can specify a custom domain name. |
| Cluster CA | Specify whether to enable the cluster CA certificate. |
| User Data | Customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run scripts during instance startup. Import user data as normal data to an ECS instance for future reference. |

5. Click Creat e Clust er in the upper-right corner of the page.
6. On the Conf irm page, after all check items are verified, select the terms of service and disclaimer
and click OK to start the deployment. Result After the cluster is created, you can find the cluster on the Clust ers page in the Container Service console.

### 5.4 Create an application from an orchestration template

orchestration template Container Service provides orchestration templates that you can use to create applications. You can also modify the templates based on YAML syntax to customize applications. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Context This topic describes how to use an orchestration template to create an NGINX application that consists of a Deployment and a Service. The Deployment provisions pods for the application and the Service manages access to the pods at the backend. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom YAML in the upper-right
corner.
6. Configure the template and click Creat e.
Sample T emplat e: Container Service provides YAML templates of various resource types to help you quickly deploy resource objects. You can also create a custom template based on YAML syntax to describe the resource that you want to define. Add Deployment : This feature allows you to quickly define a YAML template. Use Exist ing T emplat e: You can import an existing template to the configuration page. Based on an orchestration template provided by Container Service, the following sample template is used to create a Deployment of an NGINX application. Not e Container Service supports YAML syntax. You can use the `---` symbol to separate multiple resource objects. This allows you to create multiple resource objects in a single template.

```
apiVersion: apps/v1beta2 # for versions before 1.8.0 use apps/v1beta1 kind: Deployment metadata:
    name: nginx-deployment
    labels:
      app: nginx
spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:1.7.9 # replace it with your exactly <image_name:tags>
          ports:
          - containerPort: 80
--apiVersion: v1 # for versions before 1.8.0 use apps/v1beta1 kind: Service metadata:
   name: my-service1        #TODO: to specify your service name
   labels:
     app: nginx
spec:
   selector:
     app: nginx             #TODO: change label selector to match your backend pod
   ports:
   - protocol: TCP
     name: http
     port: 30080            #TODO: choose an unique port on each node to avoid port con
flict
     targetPort: 80
   type: LoadBalancer        ##In this example, the type is changed from Nodeport to Lo
adBalancer.
```

7. Click Creat e. A message that indicates the deployment status appears.
After the application is created, choose Services and Ingresses > Services in the left-side navigation pane. On the Services page, you can find that a Service named my-service1 is created for the application. The external endpoint of the Service is also displayed on the page. Click the endpoint in the Ext ernal Endpoint column.
8. You can visit the NGINX welcome page in the browser.

## 6 Kubernetes clusters

### 6.1 Authorizations

#### 6.1.1 Assign RBAC roles to a RAM user

This topic describes how to assign role-based access control (RBAC) roles to Resource Access Management (RAM) users. By default, RBAC is enabled for Kubernetes 1.6 and later. RBAC is important for you to manage clusters. You can use RBAC to specify the types of operations that are allowed for specific users based on their roles in an organization. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Aut horizat ions.
3. On the RAM Users tab, select the RAM user to which you want to grant permissions and click
Modif y Permissions. Not e If you log on to the Container Service console as a RAM user, make sure that the RAM user is assigned the predefined RBAC administrator role or the cluster-admin role.
4. On the Conf igure Role-Based Access Cont rol (RBAC) wizard page, click Add Permissions to
add cluster-scoped or namespace-scoped permissions and select a predefined or custom RBAC role in the Permission column. You can also click the minus sign (-) to delete permissions. After you add the permissions, click Next St ep. Not e For each RAM user, you can assign only one predefined RBAC role but one or more custom RBAC roles to manage the same cluster or namespace. The following table describes the permissions that the predefined and custom RBAC roles have on clusters and namespaces. Roles and permissions

| Role | RBAC permissions on cluster resources |
|---|---|
| Administrator | Read and write permissions on resources in all namespaces. |
| O&M Engineer | Read and write permissions on resources in all namespaces and read-only permissions on nodes, persistent volumes (PVs), namespaces, and service quotas within a cluster. |
| Developer | Read and write permissions on resources in a specified namespace or all namespaces. |
| Restricted User | Read-only permissions on resources in a specified namespace or all namespaces. |

| Role | RBAC permissions on cluster resources |
|---|---|
| Custom | The cluster role that you select for a custom role determines what permissions the custom role has. Before you select a cluster role, make sure that you are aware of the permissions that the cluster role has in case the RAM user is granted excessive permissions. |

After the authorization is complete, you can use the account of the specified RAM user to log on to the Container Service console. For more information, see Log on to the Container Service console. Predefined and custom RBAC roles Container Service provides the following predefined RBAC roles: administrator, O&M engineer, developer, and restricted user. You can use these roles to regulate Container Service access control in most scenarios. In addition, you can use custom roles to customize permissions on clusters. Container Service provides a set of custom RBAC roles. Not e The cluster-admin role is similar to a super administrator. By default, the cluster-admin role has the permissions to manage all resources within a cluster. You can log on to a master node of a cluster and run the following command to view the custom RBAC roles that are assigned to the current account:

```bash
 # kubectl get clusterrole
```

```bash
# kubectl get clusterrole
NAME AGE admin 13d alibaba-log-controller 13d alicloud-disk-controller-runner 13d cluster-admin 13d cs:admin 13d edit 13d flannel 13d kube-state-metrics 22h node-exporter 22h prometheus-k8s 22h prometheus-operator 22h system:aggregate-to-admin 13d .... system:volume-scheduler 13d view 13d
```

Run the following command to view the details of a role, for example, the cluster-admin role:

```bash
 # kubectl get clusterrole cluster-admin -o yaml
```

Not ice After a RAM user is assigned the cluster-admin role, the RAM user has the same permissions as the Alibaba Cloud account to which the RAM user belongs. The RAM user has full control over all resources within the cluster. Proceed with caution.

```bash
# kubectl get clusterrole cluster-admin  -o yaml
apiVersion: rbac.authorization.k8s.io/v1 kind: ClusterRole metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  creationTimestamp: 2018-10-12T08:31:15Z
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: cluster-admin
  resourceVersion: "57"
  selfLink: /apis/rbac.authorization.k8s.io/v1/clusterroles/cluster-admin
  uid: 2f29f9c5-cdf9-11e8-84bf-00163e0b2f97
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'
```

### 6.2 Clusters

#### 6.2.1 Create a Kubernetes cluster

This topic describes how to create a Kubernetes cluster in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers. On the Clusters page, click Creat e Kubernet es
Clust er in the upper-right corner.
3. On the Creat e Kubernet es Clust er page, set the parameters.

| Parameter | Description |
|---|---|
| Cluster Name | Enter a name for the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). Not e The names of the clusters that belong to the same Alibaba Cloud account must be unique. |
| Region | Select the region where you want to deploy the cluster. |
| VPC | You can select a virtual private cloud (VPC) from the drop-down list. If the specified VPC is already associated with a NAT gateway, the cluster uses the associated NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear Conf igure SNAT f or VPC. Not e If you disable the system to automatically create a NAT gateway and want the VPC to access the Internet, you must manually associate the VPC with a NAT gateway or create Source Network Address Translation (SNAT) rules for the VPC. |
| VSwitch | Select one or more vSwitches for the cluster. You can select at most three vSwitches that are deployed in different zones. |
| Kubernetes Version | Select a Kubernetes version. |

| ainer Service for Kubernetes | User Guide·Kubernetes cluster |
|---|---|

| Parameter | Description |
|---|---|
| Container Runtime | You can select Docker or Sandboxed-Container. |
| Billing Method | Only pay-as-you-go nodes are supported. |
| Master Configurations | Set the Instance Type and System Disk parameters: Master Node Quantity: You can add at most three master nodes. Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. |
| Worker Instance | You can select Creat e Inst ance or Add Exist ing Inst ance. |
| Worker Configurations | If Worker Inst ance is set to Creat e Inst ance, set the following parameters: Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. Selected Types: The selected instance types are displayed. Quantity: Set the number of worker nodes. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. Mount Data Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Encrypt Disk to encrypt disks. You can select Enable Backup to back up disk data. |
| Operating System | The CentOS and Aliyun Linux operating systems are supported. |

| Guide·Kubernetes clusters | Container Service for Kubernete |
|---|---|

| Parameter | Description |
|---|---|
| Password | Set a password that is used to log on to the nodes. Not e The password must be 8 to 30 characters in length, and must contain at least three of the following types of character: uppercase letters, lowercase letters, digits, and special characters. |
| Confirm Password | Enter the password again. |
| Network Plug-in | Flannel and Terway are supported. By default, Flannel is selected. |
| Pod CIDR Block and Service CIDR | These parameters are optional. For more information, see Network planning in VPC User Gui de. Not e These parameters are available only when you select an existing VPC. |
| Configure SNAT | This parameter is optional. If you clear Configure SNAT for VPC, you must create a NAT gateway or configure SNAT rules for the VPC. |
| Access to the Internet | Specify whether to expose the API server with an elastic IP address (EIP). The Kubernetes API server provides multiple HTTP-based RESTful APIs that can be used to create, delete, modify, query, and watch resource objects such as pods and Services. If you select this check box, an EIP is created and attached to an internal-facing Server Load Balancer (SLB) instance. Port 6443 used by the API server is exposed on the master nodes. You can connect to and manage the cluster by using kubeconfig over the Internet. If you clear this check box, no EIP is created. You can connect to and manage the cluster only by using kubeconfig from within the VPC. |
| Ingress | Specify whether to Inst all Ingress Cont rollers. By default, Inst all Ingress Cont rollers is selected. |

| Parameter | Description |
|---|---|
| Log Service | If you enable Log Service, you can select an existing project or create a project. If you select Enable Log Service, the Log Service plug-in is automatically installed in the cluster. If you select Creat e Ingress Dashboard, the Ingress access log is collected and displayed on dashboards. |
| Volume Plug-in | By default, CSI is selected. |
| Deletion Protection | This check box prevents you from accidentally deleting the cluster in the console or by calling API operations. |
| RDS Whitelist | Add the IP addresses of the nodes to the whitelist of the ApsaraDB RDS instance that is allowed to access the Kubernetes cluster. Not e To enable an ApsaraDB RDS instance to access the Kubernetes cluster, you must deploy the ApsaraDB RDS instance in the same VPC as the Kubernetes cluster. |
| Node Protection | This check box is selected by default to prevent you from accidentally deleting the nodes in the console or by calling API operations. |
| Label | Add labels to the cluster. |

4. Complete the advanced settings of the cluster.

| Parameter | Description |
|---|---|
| IP Addresses per Node | The number of IP addresses that are assigned to a node. |
| Custom Image | You can select a custom image. After you select a custom image, all nodes in the cluster are deployed by using this image. |

| Parameter | Description |
|---|---|
| Kube-proxy Mode | ipt ables and IPVS are supported. iptables is a tested and stable kube-proxy mode. It uses iptables rules to conduct service discovery and load balancing. The performance of this mode is limited by the size of the Kubernetes cluster. This mode is suitable for Kubernetes clusters that manage a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux Virtual Server (LVS) to conduct service discovery and load balancing. This mode is suitable for Kubernetes clusters that manage a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. |
| Custom Node Name | Specify whether to use a custom node name. |
| Node Port Range | Specify the value of Node Port Range. |
| Taints | Add taints to all worker nodes in the Kubernetes cluster. |
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |
| Cluster Domain | The default domain name of the cluster is cluster.local. You can specify a custom domain name. |
| Cluster CA | Specify whether to enable the cluster CA certificate. |
| User Data | You can customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run scripts during instance startup. Import user data as normal data to an ECS instance for future reference. |

5. Click Creat e Clust er in the upper-right corner of the page.
6. On the Conf irm page, after all check items are verified, select the terms of service and disclaimer
and click OK to start the deployment. Result After the cluster is created, you can view the created cluster on the Clust ers page in the Container Service console.

#### 6.2.2 Create an edge Kubernetes cluster

Edge Kubernetes clusters are intended for bringing cloud computing to edges (clients). Edge Kubernetes clusters can be created, managed, and maintained in the Container Service console. Container Service is a platform built on top of the edge computing infrastructure. It is also integrated with cloud computing and edge computing. This topic describes how to create an edge Kubernetes cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers. On the Clusters page that appears, click Creat e
Kubernet es Clust er in the upper-right corner.
3. On the Create Cluster page, click the Managed Edge Kubernet es tab and set the cluster
parameters.

| Parameter | Description |
|---|---|
| Cluster Name | Enter a name for the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). Not e The cluster name must be unique among clusters that belong to the same Alibaba Cloud account. |
| Region | Select the region where you want to deploy the cluster. |

| Parameter | Description |
|---|---|
| VPC | You can select a virtual private cloud (VPC) from the drop-down list. If the specified VPC is already associated with a NAT gateway, the cluster uses this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear Conf igure SNAT f or VPC. Not e If you disable the system to automatically create a NAT gateway and want the VPC to access the Internet, you must manually associate the VPC with a NAT gateway or create Source Network Address Translation (SNAT) rules for the VPC. |
| VSwitch | Select one or more vSwitches for the cluster. You can select up to three vSwitches that are deployed in different zones. |
| Kubernetes Version | Select a Kubernetes version. |
| Master Configurations | Set the Instance Type and System Disk parameters: Master Node Quantity: You can add up to three master nodes. Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. |
| Worker Instance | You can select Creat e Inst ance or Add Exist ing Inst ance. |

| Parameter | Description |
|---|---|
| Worker Configurations | If Worker Inst ance is set to Creat e Inst ance, set the following parameters: Instance Type: You can select one or more instance types. For more information, see the In stance types chapter of ECS User Guide. Selected Types: The selected instance types are displayed. Quantity: Set the number of worker nodes. By default, worker nodes are not required in edge Kubernetes clusters. Therefore, the value of this parameter is set to 0. System Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Enable Backup to back up disk data. Mount Data Disk: SSD Disk and Ult ra Disk are supported. Not e You can select Encrypt Disk to encrypt disks. You can select Enable Backup to back up disk data. |
| Operating System | The CentOS and Aliyun Linux operating systems are supported. |
| Network Plug-in | Edge Kubernetes clusters support only Flannel. You do not need to set this parameter. |
| Password | Set a password that is used to log on to the nodes. Not e The password must be 8 to 30 characters in length, and must contain at least three of the following types of character: uppercase letters, lowercase letters, digits, and special characters. |
| Confirm Password | Enter the password again. |

| Parameter | Description |
|---|---|
| Pod CIDR Block and Service CIDR | These parameters are optional. For more information, see Network planning in VPC User Gui de. Not e These parameters are available only when you select an existing VPC. |
| Configure SNAT | This parameter is optional. If you clear Configure SNAT for VPC, you must create a NAT gateway or configure SNAT rules for the VPC. Not e For edge Kubernetes clusters, we recommend that you select Configure SNAT for VPC. |
| Access to the Internet | Specify whether to expose the API server with an elastic IP address (EIP). The Kubernetes API server provides multiple HTTP-based RESTful APIs that can be used to create, delete, modify, query, and watch resource objects such as pods and Services. Not e We recommend that you expose the API server with an EIP. If you select this check box, an EIP is created and associated with an internal-facing Server Load Balancer (SLB) instance. Port 6443 used by the API server is exposed on the master nodes. You can connect to and manage the cluster by using kubeconfig over the Internet. If you clear this check box, no EIP is created. You can connect to and manage the cluster only by using kubeconfig within the VPC. |

| Parameter | Description |
|---|---|
| SSH Logon | To enable Secure Shell (SSH) logon, you must first select Expose API Server with EIP. If you select Use SSH to Access the Cluster from the Internet, you can access the cluster through SSH. If you clear Use SSH to Access the Cluster from the Internet, you cannot access the cluster through SSH or kubectl. If you want to access an Elastic Compute Service (ECS) instance in the cluster through SSH, you must manually bind an elastic IP address (EIP) to the ECS instance and configure security group rules to open SSH port 22. |
| Log Service | If you enable Log Service, you can select an existing project or create a project. If you select Enable Log Service, the Log Service plug-in is automatically installed in the cluster. If you select Creat e Ingress Dashboard, Ingress access logs are collected and displayed on dashboards. |
| Deletion Protection | If you select this check box, the cluster cannot be deleted in the console or by calling API operations. |
| Node Protection | This check box is selected by default to prevent nodes from being accidentally deleted in the console or by calling API operations. |

4. Complete advanced settings of the cluster.

| Parameter | Description |
|---|---|
| IP Addresses per Node | The number of IP addresses that is assigned to a node. We recommend that you use the default value. |
| Custom Image | You can select a custom image. After you select a custom image, all nodes in the cluster are deployed by using this image. |

| Parameter | Description |
|---|---|
| Kube-proxy Mode | ipt ables and IPVS are supported. iptables is a tested and stable kube-proxy mode. It uses iptables rules to conduct service discovery and load balancing. The performance of this mode is limited by the size of the Kubernetes cluster. This mode is suitable for Kubernetes clusters that manage a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux Virtual Server (LVS) to conduct service discovery and load balancing. This mode is suitable for Kubernetes clusters that manage a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. |
| Node Port Range | Specify the value of Node Port Range. |
| Taints | Add taints to all of the worker nodes in the cluster. We recommend that you do not add additional taints in case the system components cannot be deployed in the edge Kubernetes cluster. |
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |
| Cluster Domain | The default domain name of the cluster is cluster.local. You can specify a custom domain name. |
| Cluster CA | Specify whether to enable the cluster CA certificate. |
| User Data | Customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run scripts during instance startup. Import user data as normal data to an ECS instance for future reference. |

5. Click Creat e Clust er in the upper-right corner of the page.
6. On the Conf irm page, after all check items are verified, select the terms of service and disclaimer
and click OK to start the deployment. Result After the cluster is created, you can find the cluster on the Clust ers page in the Container Service console.

#### 6.2.3 View log files of a cluster

You can view the operation log of a cluster in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. Find the cluster that you want to manage and click View Logs in the Actions column.
You can view operations performed on the cluster.

#### 6.2.4 Connect to a cluster through kubectl

You can use the Kubernetes command line tool, kubectl, to connect to a Kubernetes cluster from a local computer. Procedure
1. Download the latest kubectl client from the Kubernetes change log page.
2. Install and set up the kubectl client.
For more information, see Install and set up kubectl.
3. Configure the cluster credentials.

| You can use the | scp | com |
|---|---|---|
| etc/kubernetes/kube.conf |   |   |

You can use the `scp` command to securely copy the master node configuration file from the `/` `etc/kubernetes/kube.conf` directory of the master VM and paste it to the $HOME/.kube/config directory of the local computer, where the `kubectl` credentials are expected to be stored.

```
mkdir $HOME/.kube scp root@<master-public-ip>:/etc/kubernetes/kube.conf $HOME/.kube/config
```

You can find `master-public-ip` on the cluster details page. i. Log on to the Container Service console. ii. In the left-side navigation pane, click Clust ers. The Clusters page appears. iii. Find the target cluster and click Manage in the Actions column. In the Clust er Inf ormat ion section, you can find the master node IP address.

#### 6.2.5 Connect to a master node by using SSH

You can access a master node in a cluster by using a Secure Shell (SSH) client. Prerequisites A Kubernetes cluster is created and Use SSH t o Access t he Clust er f rom t he Int ernet is selected for the cluster. For more information, see Create a Kubernetes cluster. The SSH client can connect to the network where the cluster is deployed. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers to go to the Clusters page. Find the
cluster that you want to manage, and click Manage in the Actions column for the cluster.
3. The Basic Information page appears. In the Cluster Information section, you can find the IP address
that is displayed in the Mast er Node IP Address f or SSH Logon field.
4. Use SSH to connect to the cluster from an SSH client that has access to the cluster network.
If you have a leased line that connects to the cluster network over the Internet, you can use tools such as PuTTY to create an SSH connection. If you have an Elastic Compute Service (ECS) instance that is connected to the Virtual Private Cloud (VPC) network of the cluster, run the following command to create an SSH connection:

```
ssh root@ssh_ip #ssh_ip specifies the IP address of the maste r node for SSH connection.
```

#### 6.2.6 Expand a cluster

This topic describes how to scale out the worker nodes of a Kubernetes cluster in the Container Service console. Context You cannot scale out the master nodes of a Kubernetes cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to expand and choose More > Expand in
the Act ions column.
4. On the Node Pools page, select the node pool that you want to scale out and click Scale Out in
the Act ions column.
5. Go to the Expand page and set the required parameters.
In this example, the number of worker nodes in the cluster is increased from three to five. The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Nodes to Add | Specify the number of nodes to be added to the cluster. |
| Region | By default, the region where the cluster is deployed is displayed. |
| Container Runtime | By default, the container runtime of the cluster is displayed. |

| User | Guide·Kubernetes clusters | Container Service for Kubernete | s |
|---|---|---|---|

| Parameter | Description |
|---|---|
| VPC | By default, the virtual private cloud (VPC) of the cluster is displayed. |
| VSwitch | Select one or more vSwitches for the cluster. You can select at most three vSwitches that are deployed in different zones. |
| Instance Type | You can select one or more instance types. For more information, see the Instance types topic of ECS User Guide. |
| Selected Types | The selected instance types. |
| System Disk | Standard SSDs, enhanced SSDs (ESSDs), and ultra disks are supported. |
| Mount Data Disk | Standard SSDs, ESSDs, and ultra disks are supported. |
| Operating System | The operating system of the cluster. |
| Password | Password: Enter the password that is used to log on to the nodes. Conf irm Password: Enter the password again. |
| ECS Label | You can add labels to the ECS instances. |
| Node Label | Add labels to nodes. |
| Taints | Add taints to the worker nodes in the cluster. |
| Custom Image | You can select a custom image. After you select a custom image, all nodes in the cluster are deployed by using this image. |
| RDS Whitelist | Set the Relational Database Service (RDS) whitelist. Add the IP addresses of the nodes in the cluster to the RDS whitelist. |
| User Data | Customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used in the following ways: Run scripts during instance startup. Import user data as normal data to an ECS instance for future reference. |

6. Click Submit .
What's next After the cluster is expanded, choose Nodes > Nodes in the left-side navigation pane. On the Nodes page, you can find that the number of worker nodes is increased from 3 to 5.

#### 6.2.7 Renew a certificate

This topic describes how to renew a Kubernetes cluster certificate in the console. Prerequisites A Kubernetes cluster is created and the cluster certificate is about to expire. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. Select the cluster for which you want to renew the certificate and click Updat e Cert if icat e. The
Updat e Cert if icat e message appears. Not e The Updat e Cert if icat e button will be displayed two months before your cluster certificate expires.
4. Click Updat e and the Conf irm page appears.
5. Click OK.
Result On the Updat e Cert if icat e page, the following message appears: T he cert if icat e has been updat ed. On the Clust ers page, the Updat e Cert if icat e button disappears.

#### 6.2.8 Delete a Kubernetes cluster

This topic describes how to delete a Kubernetes cluster in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to delete and choose More > Delet e in the
Act ions column.
4. In the Delet e Clust er dialog box that appears, select the resources that you want to retain, select
I underst and t he above inf ormat ion and want t o delet e t he specif ied clust er, and then click OK. What's next Resource Orchestration Service (ROS) does not have permissions to delete resources that are manually added to resource created by ROS. For example, if you manually add a vSwitch to a virtual private cloud (VPC) created by ROS, ROS cannot delete the VPC and therefore the cluster cannot be deleted. Container Service allows you to forcibly delete clusters. If your first attempt to delete a cluster fails, you can forcibly delete the cluster and ROS resource stack. However, you still need to manually release the resources that are manually added. An error message appears when an attempt to delete a cluster fails. Select the cluster that you failed to delete and choose More > Delet e in the Actions column. In the dialog box that appears, you can view the resources that are manually added. Select the Force Delet e check box and click OK to delete the cluster and ROS resource stack.

#### 6.2.9 View cluster overview

The Container Service console provides a cluster overview page. This page displays the information such as application status, component status, and resource monitoring status. This allows you to check the health status of your cluster at your convenience. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Overview. The Overview page appears.
3. Select the target cluster and namespace. You can view the application status, component status,
and resource monitoring charts. Applicat ion St at us: displays the statuses of the deployments, pods, and replica sets that are running in the cluster. Green sections indicate a normal state and yellow sections indicate an exception state. Node St at us: displays the statuses of the nodes in the cluster. Component St at us: Components are deployed in the kube-system namespace. Core components are used, such as the scheduler, controller-manager, and etcd. Event s: displays events such as warnings and errors. If no events are displayed, the cluster is running in the normal state. Monit oring: displays CPU and memory monitoring charts. CPU usage is measured in cores or millicores and accurate to three decimal places. A millicore is one thousandth of a core. Memory usage is measured in GiB and accurate to three decimal places. For more information, see Meaning of CPU and Meaning of memory.

### 6.3 Nodes

#### 6.3.1 Add existing nodes to a Kubernetes cluster

Container Service allows you to add an existing Elastic Compute Service (ECS) instance to a Kubernetes cluster. You can add only worker nodes to clusters. Prerequisites A Kubernetes cluster is created. For more information, see Log on to the Container Service console. An ECS instance is created. Make sure that the region, zone, organization, project, security group, virtual private cloud (VPC), and operating system settings of the ECS instance are the same as those of the cluster. Context By default, a cluster can contain at most 50 nodes. To increase the quota, submit a ticket. The ECS instance that you add must be in the same region and VPC as the cluster. The ECS instance must belong to the same Apsara Stack tenant account as the cluster. The ECS instance must be running the CentOS operating system. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. In the upper-right corner of the page, click Add Exist ing Node.
6. On the page that appears, you can manually add existing ECS instances to the cluster.
To manually add an ECS instance, you must obtain the installation command and log on to the ECS instance to run the command. You can add only one ECS instance at a time. i. Select Manual, find and select the ECS instance that you want to add, and then click Next St ep. You can add only one ECS instance at a time. ii. Confirm the instance information and click Next St ep. iii. On the Complete wizard page, copy the command. iv. Click Done. v. Go to the Apsara Uni-manager Management Console. In the top navigation bar, choose Product s > Elast ic Comput e Service. On the Inst ances page, select the organization and region of the cluster, and then find the ECS instance that you want to add to the cluster. vi. Click the instance name to go to the Instance Details tab. Click Connect t o VNC. In the dialog box that appears, enter the VNC password and then click OK. After you log on to the instance, paste the copied command and click OK to run the script. vii. After the script is executed, the ECS instance is added to the cluster. You can go to the Clusters page and click the cluster ID to view nodes in the cluster. Check whether the ECS instance has been added to the cluster.

#### 6.3.2 Add nodes to an edge Kubernetes cluster

You can add worker nodes to an edge Kubernetes cluster in the Container Service console. However, you must make sure that the added nodes can communicate with the Kubernetes API server of the cluster. This topic describes how to add nodes to an edge Kubernetes cluster. Prerequisites Context By default, a cluster can contain at most 50 nodes. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, click the name of the cluster that you want to manage.
4. In the left-side navigation pane of the cluster details page, choose Nodes > Nodes. On the page
that appears, click Add Exist ing Node in the upper-right corner.
5. On the Select Exist ing ECS Inst ance wizard page, click Next St ep.
You can only manually add nodes to edge Kubernetes clusters.
6. On the Specif y Inst ance Inf ormat ion wizard page, set the parameters and click Next St ep.

| Parameter | Description | Default |
|---|---|---|
| flannelIface | The name of the network interface controller (NIC) that is used by the Flannel plug-in. | The name of the NIC that is specified in the default route entry of the node. |
| enableIptables | Specifies whether to enable iptables. | false |
| quiet | Specifies whether to answer all questions with yes when you add nodes. | false |
| manageRuntime | Specifies whether to use edgeadm to install and manage the runtime. | false |
| nodeNameOverride | The name of the node. | "". This is the default value. This value specifies that the hostname is used as the node name. "*". This value specifies that a random string that contains six characters is used as the node name. "*."*.XXX". This value specifies that a random string that is followed by a suffix is used as the node name. The random string contains six characters. |
| allowedClusterAddons | The list of add-ons to be installed. By default, this parameter is empty. This indicates that no add-on is installed. For a standard edge node, set this parameter to ["kube- proxy","flannel","coredns"]. | [] |
| gpuVersion | Specifies whether the node to be added is a GPU-accelerated node. By default, this parameter is empty. Supported GPU models are Nvidia Tesla T4, _ _ Nvidia Tesla P4, and _ _ Nvidia Tesla P100. _ _ | "". This is the default value. This value specifies that the node to be added is not a GPU- accelerated node. |

| Parameter | Description | Default |
|---|---|---|
| inDedicatedNetwork | Specifies whether an Express Connect circuit is used to connect to the managed edge Kubernetes cluster. | false |
| labels | Specifies the labels to be added to the node. | {} |
| annotations | Specifies the annotations to be added to the node. | {} |
| nodeIface | This parameter specifies the following information: Specifies the node IP address that kubelet retrieves from the specified network interface. If you do not specify this parameter, kubelet attempts to retrieve the node IP address in the following order: Searches /etc/hosts for the node whose name is the same as the specified hostname. Finds the IP address of the network interface that is specified in the default route entry of the node. Specifies the name of the NIC that is used by the Flannel plug-in. In this case, this parameter is equivalent to the flannellface parameter. This parameter will soon replace the flannellface parameter. | "" |

7. On the Complet e wizard page, copy the script to the node that you want to add to the edge
Kubernetes cluster and click Done.
8. Log on to the edge node and execute the script. This way, the node is added to the edge
Kubernetes cluster.

#### 6.3.3 View nodes

You can view nodes of a Kubernetes cluster by using the Container Service console, kubectl, or Kubernetes Dashboard. View nodes by using kubectl Not e To view the nodes in a cluster by using kubectl, you must Connect to a Kubernetes cluster through kubectl. Connect to a cluster by using kubectl and run the following command to view the nodes in the cluster:

```bash
kubectl get nodes
```

Sample out put :

```bash
$ kubectl get nodes
    NAME                      STATUS    AGE       VERSION
    iz2ze2n6ep53tch701yh9zz   Ready     19m       v1.6.1-2+ed9e3d33a07093
    iz2zeafr762wibijx39e5az   Ready     7m        v1.6.1-2+ed9e3d33a07093
    iz2zeafr762wibijx39e5bz   Ready     7m        v1.6.1-2+ed9e3d33a07093
    iz2zef4dnn9nos8elyr32kz   Ready     14m       v1.6.1-2+ed9e3d33a07093
    iz2zeitvvo8enoreufstkmz   Ready     11m       v1.6.1-2+ed9e3d33a07093
```

View nodes by using the Container Service console
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes to view the nodes in
the cluster.

#### 6.3.4 Manage node labels

You can manage node labels in the Container Service console. You can add a label to multiple nodes at a time, filter nodes by label, and delete labels. You can use labels to schedule nodes. For more information, see Set node scheduling. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Add a label to multiple nodes at a time
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. On the Nodes page, click Manage Labels and T aint s in the upper-right corner.
6. Select multiple nodes and click Add Label.
7. In the dialog box that appears, enter the name and value of the label and click OK.
On the Labels tab, you can find that the selected nodes have the same label. Delete a label
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. On the Nodes page, click Manage Labels and T aint s in the upper-right corner.
6. Select a node, find the label that you want to delete, and then click the
icon. In the message that appears, click Conf irm. After the label is deleted, it is removed from the Labels column.

#### 6.3.5 Set node schedulability

You can mark a node as schedulable or unschedulable in the Container Service console. This allows you to optimize the distribution of the loads on each node. This topic describes how to set node schedulability. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. On the Nodes page, select the node that you want to manage and click Drain/Set t o
Unschedulable in the Actions column.
6. In the dialog box that appears, you can change the status of the node.
If you select Set t o Unschedulable, pods will not be scheduled to this node when you deploy new applications. If you select Set t o Unschedulable and Drain, pods will not be scheduled to this node when you deploy new applications. Pods on this node will be evicted, except for the pods that are managed by DaemonSets. In this example, Set t o Unschedulable is selected. Click OK. The status of the node is changed to Unschedulable. What's next Pods will not be scheduled to the node when you deploy new applications.

#### 6.3.6 Remove a node

To restart or release an Elastic Compute Service (ECS) node in a cluster, you must first remove the node from the cluster. This topic describes how to remove a node. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. You can connect to the Kubernetes cluster by using kubectl. For more information, see Connect to a Kubernetes cluster through kubectl. Context When you remove a node, pods that run on the node are migrated to other nodes. This may cause service interruption. We recommend that you remove nodes during off-peak hours. Unknown errors may occur when you remove nodes. Before you remove nodes, we recommend that you back up data on these nodes. Nodes remain in the unschedulable state when they are being removed. You can remove only worker nodes. You cannot remove master nodes. Procedure
1. Run the following command to migrate the pods on the node that you want to remove to other
nodes. Not e Make sure that the other nodes have sufficient resources for these pods.

```bash
kubectl drain node-name
```

Not e node-name must be in the format of your-region-name.node-id. your-region-name specifies the region where the cluster that you want to manage is deployed. node-id specifies the ID of the ECS instance where the node to be removed is deployed. Example: cn-hanghzou.i-xxx.
2. Log on to the Container Service console.
3. In the left-side navigation pane, click Clust ers.
4. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
5. In the left-side navigation pane of the details page, choose Nodes > Node.
6. Find the node that you want to remove and choose More > Remove in the Act ions column.
Not e To remove multiple nodes at a time, select the nodes that you want to remove on the Nodes page and click Bat ch Remove.
7. (Optional)Set parameters in the Remove Node dialog box.
Select Drain t he Node to migrate the pods on the node to other nodes. If you select this option, make sure that the other nodes have sufficient resources for these pods. Select Release ECS Inst ance to release the ECS instance where the node is deployed. Not e Select this option to release only pay-as-you-go ECS instances. Subscription ECS instances are automatically released after the subscription expires. If you do not select Release ECS Inst ance, you are still billed for the ECS instance where the node is deployed.
8. In the Remove Node message, click OK.

#### 6.3.7 View node resource usage

You can view the resource usage of the nodes in a cluster in the Container Service console. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. On the Nodes page, find the node that you want to manage and choose More > Det ails in the
Act ions column. You can view the request rate and usage rate of CPU and memory resources on each node. CPU request rate = sum (The amount of CPU resources requested by all pods on the node) / Total CPU resources of the node CPU usage rate = sum (The amount of CPU resources used by all pods on the node) / Total CPU resources of the node Memory request rate = (The amount of memory resources requested by all pods on the node) / Total memory resources of the node Memory usage rate = sum (The amount of memory resources used by all pods on the node) / Total memory resources of the node Not e You can adjust the workload of a node based on the resource usage. For more information, see Set node scheduling. When the request or usage rate of a node reaches 100%, pods are not scheduled to the node.

#### 6.3.8 Upgrade the NVIDIA driver on a GPU node

This topic describes how to upgrade the NVIDIA driver on a GPU node when workloads are deployed on the node and when no workload is deployed on the node. Upgrade the NVIDIA driver on a GPU node where workloads are deployed
1. Connect to a Kubernetes cluster through kubectl.
2. Run the following command to set the target node to unschedulable.

```bash
kubectl cordon node-name
```

Currently, you can only upgrade the NVIDIA driver on worker nodes. node-name must be in the format of your-region-name.node-id. your-region-name represents the region where your cluster is deployed. node-id represents the ID of the ECS instance where the target node is deployed. You can run the following command to query node-name.

```bash
kubectl get node
```

3. Run the following command to migrate pods from the target node to other nodes:

```bash
kubectl drain node-name --grace-period=120 --ignore-daemonsets=true
```

4. Run the following command to log on to the target node:

```
ssh root@xxx.xxx.x.xx
```

5. Run the following command to check the current NVIDIA driver version:

```
nvidia-smi
```

6. Run the following commands to uninstall the existing driver:
If your driver version is 384.111, perform the following steps. If your driver version is not 384.111, download the corresponding driver from the official NVIDIA website first.

```bash
cd /tmp curl -O https://cn.download.nvidia.cn/tesla/384.111/NVIDIA-Linux-x86_64-384.111.run chmod u+x NVIDIA-Linux-x86_64-384.111.run . /NVIDIA-Linux-x86_64-384.111.run --uninstall -a -s -q
```

7. Run the following command to restart the target node:

```
reboot
```

8. Download the driver that you want to use from the official NVIDIA website. In this example, version
410.79 is used.
9. Run the following command to install the downloaded driver under the directory where it was
saved:

```
sh . /NVIDIA-Linux-x86_64-410.79.run -a -s -q
```

10. Run the following commands to configure the driver:

```
nvidia-smi -pm 1 || true nvidia-smi -acp 0 || true
```

11. Run the following commands to update device-plugin:

```
mv /etc/kubernetes/manifests/nvidia-device-plugin.yml / mv /nvidia-device-plugin.yml /etc/kubernetes/manifests/
```

12. Log on to a master node and run the following command to set the target node to schedulable:

```bash
kubectl uncordon node-name
```

Result Run the following command on a master node to check the NVIDIA driver version on the target node. The driver version is now 410.79. Not e Replace node-name with the target node name.

```bash
kubectl exec -n kube-system -t nvidia-device-plugin-node-name nvidia-smi
```

Upgrade the NVIDIA driver on a GPU node where no workload is deployed
1. Run the following command to log on to the target node:

```
ssh root@xxx.xxx.x.xx
```

2. Run the following command to check the current NVIDIA driver version:

```
nvidia-smi
```

3. Run the following commands to uninstall the existing driver:
Not e If your driver version is 384.111, perform the following steps. If your driver version is not 384.111, download the corresponding driver from the official NVIDIA website first.

```bash
cd /tmp curl -O https://cn.download.nvidia.cn/tesla/384.111/NVIDIA-Linux-x86_64-384.111.run
```

```
chmod u+x NVIDIA-Linux-x86_64-384.111.run . /NVIDIA-Linux-x86_64-384.111.run --uninstall -a -s -q
```

4. Run the following command to restart the target node.

```
reboot
```

5. Download the driver that you want to use from the official NVIDIA website. In this example, version
410.79 is used.
6. Run the following command to install the downloaded driver under the directory where it was
saved:

```
sh . /NVIDIA-Linux-x86_64-410.79.run -a -s -q
```

7. Run the following commands to configure the driver:

```
nvidia-smi -pm 1 || true nvidia-smi -acp 0 || true
```

Result Run the following command on a master node to check the NVIDIA driver version on the target node. The driver version is now 410.79. Not e Replace node-name with the target node name.

```bash
kubectl exec -n kube-system -t nvidia-device-plugin-node-name nvidia-smi
```

#### 6.3.9 GPU scheduling for Kubernetes clusters with GPU-accelerated nodes

with GPU-accelerated nodes This topic describes GPU scheduling for Kubernetes clusters with GPU-accelerated nodes. Prerequisites Container Service, Resource Orchestration Service (ROS), and Resource Access Management (RAM) are activated. Not e Container Service uses ROS to deploy applications in Kubernetes clusters. To create a Kubernetes cluster, you must first activate ROS. Context Starting from version 1.8, Kubernetes adds support for the following hardware acceleration devices by using device plug-ins: NVIDIA GPUs, InfiniBand devices, and field-programmable gate arrays (FPGAs). GPU solutions developed by the community will be phased out in version 1.10, and removed from the master code in version 1.11. Container Service enables you to use a Kubernetes cluster with GPU-accelerated nodes to run compute-intensive tasks such as machine learning and image processing. You can deploy applications and achieve auto scaling without the need to install NVIDIA drivers or Compute Unified Device Architecture (CUDA) in advance. The system performs the following operations when a Kubernetes cluster is created: Creates Elastic Compute Service (ECS) instances, configures a public key to enable Secure Shell (SSH) logon from master nodes to other nodes, and then configures the Kubernetes cluster through CloudInit. Creates a security group that allows access to the virtual private cloud (VPC) over Internet Control Message Protocol (ICMP). If you do not specify an existing VPC, the system creates a VPC and a vSwitch and creates SNAT entries for the vSwitch. Adds route entries to the VPC. Creates a NAT gateway and an elastic IP address (EIP). Creates a RAM user and grants it permissions to query, create, and delete ECS instances, and permissions to add and delete disks. The RAM user is also granted full permissions on Server Load Balancer (SLB) instances, CloudMonitor, VPC, Log Service, and Apsara File Storage NAS (NAS). The system also creates an AccessKey pair for the RAM user. The system automatically creates SLB instances, disks, and VPC route entries based on your configuration. Creates an internal-facing SLB instance and opens port 6443. Creates an Internet-facing SLB instance and open ports 6443, 8443, and 22. If you enable SSH logon when you create the cluster, port 22 is open. Otherwise, port 22 is not open. Limits Kubernetes clusters support only VPCs. By default, you can create only a limited amount of cloud resources with each account. You cannot create clusters if the quota on clusters is reached. Make sure that you have sufficient quota before you create a cluster. To request a quota increase, submit a ticket. By default, you can create at most five clusters across all regions with each account. Each cluster can contain at most 40 nodes. To increase the quota of clusters or nodes, submit a ticket. Not e In a Kubernetes cluster, you can create at most 48 route entries for each VPC. This means that a cluster can contain at most 48 nodes. To increase the quota of nodes, submit a ticket to increase the quota of route entries first. By default, you can create at most 100 security groups with each account. By default, you can create at most 60 pay-as-you-go SLB instances with each account. By default, you can create at most 20 EIPs with each account. Limits on ECS instances: Only CentOS is supported. Create a GN5 Kubernetes cluster GN5 Kubernetes clusters support only Kubernetes 1.12.6-aliyun.1. Kubernetes 1.11.5 is not supported.
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. In the upper-right corner of the Clust ers page, click Creat e Kubernet es Clust er.
On the cluster configuration page, set the parameters. Not e To create a cluster with GPU-accelerated nodes, select GPU-accelerated ECS instance types as worker nodes. For more information about other parameters, see Create a Kubernetes cluster.
4. Configure worker nodes. In this example, worker nodes are used to run GPU computing tasks and
the gn5i-c4gi1 instance type is selected. i. If you choose to create worker instances, you must set Instance Type and Quantity. In this example, three GPU-accelerated worker nodes are created. Not e We recommend that you use standard SSDs. ii. If you choose to add existing instances, you must create GPU-accelerated ECS instances in the region where you want to create the cluster in advance.
5. Specify the other parameters and click Creat e Clust er to start the deployment.
After the cluster is created, choose Clust ers > Nodes to go to the Nodes page. Select a worker nodes that was configured for the cluster and choose More > Det ails in the Actions column to view the GPU devices that are attached to the node. Create a GPU experimental environment to run TensorFlow Jupyter is a standard tool that is used by data scientists to create an experimental environment to run TensorFlow. The following example shows how to deploy a Jupyter application.
1. Log on to the Container Service console. In the left-side navigation pane, choose Applicat ions >
Deployment s to go to the Deployment s page.
2. In the upper-right corner of the page, click Creat e f rom T emplat e.
3. Select the required cluster and namespace. Select a sample template, or set Sample Template to
Custom and customize the template in the Template field. Then, click Creat e to create the application. In this example, the template uses a Deployment and a Service to create a Jupyter application.

```bash
---
# Define the tensorflow deployment
apiVersion: apps/v1 kind: Deployment metadata:
  name: tf-notebook
  labels:
    app: tf-notebook
spec:
  replicas: 1
  selector: # define how the deployment finds the pods it manages
    matchLabels:
      app: tf-notebook
  template: # define the pods specifications
    metadata:
      labels:
        app: tf-notebook
    spec:
      containers:
      - name: tf-notebook
        image: tensorflow/tensorflow:1.4.1-gpu-py3
        resources:
          limits:
            nvidia.com/gpu: 1                      #The number of NVIDIA GPUs that are
requested by the application.
        ports:
        - containerPort: 8888
          hostPort: 8888
        env:
          - name: PASSWORD                         #The password that is used to access
the Jupyter application. You can modify the password as required.
            value: mypassw0rd
# Define the tensorflow service
--apiVersion: v1 kind: Service metadata:
  name: tf-notebook
spec:
  ports:
  - port: 80
    targetPort: 8888
    name: jupyter
  selector:
    app: tf-notebook
  type: LoadBalancer                           #An SLB instance is used to route intern
al traffic and perform load balancing.
```

4. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. Select the
required cluster and namespace, find the tf-notebook Service, and then check its external endpoint.
5. To connect to the Jupyter application, enter `http://EXTERNAL-IP` into the address bar of your
browser and enter the password specified in the template.
6. You can run the following program to verify that the Jupyter application is allowed to use GPU
resources. The program lists all devices that can be used by TensorFlow:

```python
from tensorflow.python.client import device_lib def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]
print(get_available_devices())
```

#### 6.3.10 Use labels to schedule pods to GPU-accelerated nodes

accelerated nodes To use Kubernetes clusters for GPU computing, you must schedule pods to GPU-accelerated nodes. Container Service allows you to schedule pods to specific GPU-accelerated nodes by adding labels to the GPU-accelerated nodes. Context When Kubernetes deploys nodes with NVIDIA GPUs, the attributes of these GPUs are discovered and exposed as node labels. These labels have the following benefits: You can use the labels to filter GPU-accelerated nodes. The labels can be used as conditions to schedule pods. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
In this example, the Kubernetes cluster contains three master nodes, among which two are equipped with GPUs. Record the node IP addresses.
5. On the Nodes page, select the node that is equipped with GPUs and choose More > Det ails in the
Actions column to view the labels that are added to the node. You can also log on to a master node and run the following command to view the labels of GPUaccelerated nodes:

```bash
# kubectl get nodes
NAME STATUS ROLES AGE VERSION cn-beijing.i-2ze2dy2h9w97v65u**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1
# Compare these nodes with the nodes displayed in the console to identify GPU-accelerat
ed nodes. cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1 cn-beijing.i-2ze9xylyn11vop7g**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2zed5sw8snjniq6m**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2zej9s0zijykp9pw**** Ready <none> 2d v1.12.6-aliyun.1
```

Select a GPU-accelerated node and run the following command to query the labels of the node:

```bash
# kubectl describe node cn-beijing.i-2ze8o1a45qdv5q8a****
Name: cn-beijing.i-2ze8o1a45qdv5q8a7luz Roles: <none> Labels: aliyun.accelerator/nvidia_count=1 #Note
                    aliyun.accelerator/nvidia_mem=12209MiB
                    aliyun.accelerator/nvidia_name=Tesla-M40
                    beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/instance-type=ecs.gn4-c4g1.xlarge
                    beta.kubernetes.io/os=linux
                    failure-domain.beta.kubernetes.io/region=cn-beijing
                    failure-domain.beta.kubernetes.io/zone=cn-beijing-a
                    kubernetes.io/hostname=cn-beijing.i-2ze8o1a45qdv5q8a****
 ......
```

In this example, the following labels are added to the GPU-accelerated node.

| key | value |
|---|---|
| aliyun.accelerator/nvidia count _ | The number of GPU cores. |
| aliyun.accelerator/nvidia mem _ | The size of the GPU memory. Unit: MiB. |
| aliyun.accelerator/nvidia name _ | The name of the NVIDIA GPU. |

GPU-accelerated nodes of the same type have the same GPU name. You can use this label to locate GPU-accelerated nodes.

```bash
# kubectl get no -l aliyun.accelerator/nvidia_name=Tesla-M40
NAME STATUS ROLES AGE VERSION cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1 cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1
```

6. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
7. On the Deployment s page, select the namespace and click Creat e f rom T emplat e in the upper-
right corner.
8. Create a Deployment for a TensorFlow job. The Deployment is used to schedule pods to a GPU-
accelerated node.
9. You can also exclude an application from GPU-accelerated nodes. The following example shows
how to schedule a pod based on node affinity for an NGINX application. For more information, see the section that describes node affinity in Create an application from an image. The following YAML template is used as an example:

```
apiVersion: v1 kind: Pod metadata:
  name: not-in-gpu-node
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: aliyun.accelerator/nvidia_name
            operator: DoesNotExist
  containers:
  - name: not-in-gpu-node
    image: nginx
```

Result In the left-side navigation pane of the details page, choose Workloads > Pods. On the Pods page, select the namespace to view pods created in the namespace. On the Pods page, you can find that the pods in the preceding examples are scheduled to the desired nodes. This means that labels can be used to schedule pods to GPU-accelerated nodes.

#### 6.3.11 Manually upgrade the kernel of a GPU node in a cluster

node in a cluster This topic describes how to manually upgrade the kernel of a GPU node in a cluster. Context The current kernel version is earlier than `3.10.0-957.21.3` . Procedure
1. Connect to a Kubernetes cluster through kubectl.
2. Run the following command to set the target GPU node to unschedulable. This example uses node
cn-beijing.i-2ze19qyi8votgjz12345 as the target node.

```bash
kubectl cordon cn-beijing.i-2ze19qyi8votgjz12345 node/cn-beijing.i-2ze19qyi8votgjz12345 already cordoned
```

3. Run the following command to drain the target GPU node:

```bash
# kubectl drain cn-beijing.i-2ze19qyi8votgjz12345 --grace-period=120 --ignore-daemonset
s=true node/cn-beijing.i-2ze19qyi8votgjz12345 cordoned WARNING: Ignoring DaemonSet-managed pods: flexvolume-9scb4, kube-flannel-ds-r2qmh, kube -proxy-worker-l62sf, logtail-ds-f9vbg pod/nginx-ingress-controller-78d847fb96-5fkkw evicted
```

4. Uninstall the existing nvidia-driver.
This step uninstalls the version 384.111 driver. If your driver version is not 384.111, you need to download a driver from the official NVIDIA website and replace `384.111` with your actual version number. i. Log on to the target GPU node and run the `nvidia-smi` command to query the driver version.

```bash
# nvidia-smi -a | grep 'Driver Version'
Driver Version : 384.111
```

ii. Run the following commands to download the driver installation package:

```bash
cd /tmp/ curl -O https://cn.download.nvidia.cn/tesla/384.111/NVIDIA-Linux-x86_64-384.111.run
```

Not e The installation package is required to uninstall the driver. iii. Run the following commands to uninstall the existing nvidia-driver:

```
chmod u+x NVIDIA-Linux-x86_64-384.111.run . /NVIDIA-Linux-x86_64-384.111.run --uninstall -a -s -q
```

5. Run the following commands to upgrade kernel:

```bash
yum clean all && yum makecache yum update kernel -y
```

6. Run the following command to restart the GPU node:

```
reboot
```

7. Log on to the GPU node and run the following command to install the kernel-devel package.

```bash
yum install -y kernel-devel-$(uname -r)
```

8. Run the following commands to download the required driver and install it on the target node. In
this example, version 410.79 is used.

```bash
cd /tmp/ curl -O https://cn.download.nvidia.cn/tesla/410.79/NVIDIA-Linux-x86_64-410.79.run chmod u+x NVIDIA-Linux-x86_64-410.79.run sh . /NVIDIA-Linux-x86_64-410.79.run -a -s -q
# warm up GPU
nvidia-smi -pm 1 || true nvidia-smi -acp 0 || true nvidia-smi --auto-boost-default=0 || true nvidia-smi --auto-boost-permission=0 || true nvidia-modprobe -u -c=0 -m || true
```

9. Check the /etc/rc.d/rc.local file and check whether the following configurations are included. If
not, add the following content.

```
nvidia-smi -pm 1 || true nvidia-smi -acp 0 || true nvidia-smi --auto-boost-default=0 || true nvidia-smi --auto-boost-permission=0 || true nvidia-modprobe -u -c=0 -m || true
```

10. Run the following commands to restart kubelet and Docker.

```
service kubelet stop service docker restart service kubelet start
```

11. Run the following command to set the GPU node to schedulable:

```bash
# kubectl uncordon cn-beijing.i-2ze19qyi8votgjz12345
node/cn-beijing.i-2ze19qyi8votgjz12345 already uncordoned
```

12. Run the following command on the nvidia-device-plugin container to check the driver version:

```bash
kubectl exec -n kube-system -t nvidia-device-plugin-cn-beijing.i-2ze19qyi8votgjz12345 n vidia-smi Thu Jan 17 00:33:27 2019 +-----------------------------------------------------------------------------+
| NVIDIA-SMI 410.79       Driver Version: 410.79       CUDA Version: N/A      |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  On   | 00000000:00:09.0 Off |                    0 |
| N/A   27C    P0    28W / 250W |      0MiB / 16280MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

#### 6.3.12 Node pools

##### 6.3.12.1 Create a node pool

You can use a node pool to manage multiple nodes in a Kubernetes cluster as a group. For example, you can centrally manage the labels and taints of the nodes in a node pool. This topic describes how to create a node pool in the Container Service console. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. The Kubernetes cluster must run Kubernetes 1.9 or later. Not ice By default, a cluster can contain at most 100 nodes. Before you add an existing Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC), make sure that an elastic IP address (EIP) is associated with the ECS instance, or a NAT gateway is created for the VPC. In addition, make sure that the ECS instance can access the Internet. Otherwise, you cannot add the ECS instance. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Node Pools.
5. On the Node Pools page, click Creat e Node Pool.
6. In the Creat e Node Pool dialog box, set the parameters.
For more information about the parameters, see Create a Kubernetes cluster. The following list describes some of the parameters: Name: the name of the node pool. Quantity: the initial number of nodes in the node pool. If you do not want to add nodes to the node pool, set this parameter to 0. ECS Label: the labels of the ECS instances. Node Label: the labels of nodes in the node pool. Custom Resource Group: the resource group to which the nodes of the node pool belong. Custom Security Group: the custom security group of the ECS instance.
7. Click Conf irm Order.
On the Node Pools page, check the St at us column of the managed node pool. If the node pool is in the Init ializing state, it indicates that the node pool is being created. After the node pool is created, the st at e of the node pool changes to Act ive. What's next After the node pool is created, find the node pool on the Node Pools page and click Det ails in the Act ions column to view details of the node pool.

##### 6.3.12.2 Scale out a node pool

You can use a node pool to manage multiple nodes in a Kubernetes cluster as a group. For example, you can centrally manage the labels and taints of the nodes in a node pool. This topic describes how to scale out a node pool in the Container Service console. Prerequisites A node pool is created. For more information, see Create a node pool. The Kubernetes cluster must run Kubernetes 1.9 or later. Not ice By default, a cluster can contain at most 100 nodes. Before you add an existing Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC), make sure that an elastic IP address (EIP) is associated with the ECS instance, or a NAT gateway is created for the VPC. In addition, make sure that the ECS instance can access the Internet. Otherwise, you cannot add the ECS instance. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Node Pools.
5. On the Node Pools page, select the node pool that you want to manage and click Scale Out in
the Act ions column.
6. In the dialog box that appears, set the number of nodes that you want to add to the node pool.
7. (Optional)In the dialog box that appears, click Modif y Node Pool Set t ings to modify the node
pool. For more information, see Expand a Container Service cluster. The following list describes some of the parameters: ECS Label: You can add labels to the ECS instances in the node pool. Node Label: You can add labels to the nodes in the node pool. Taints: You can add one or more taints to the specified nodes. Not e If you select Synchronize Node Labels and T aint s, the specified labels and taints are synchronized to the existing and newly added nodes. CloudMonitor Agent: You can install the CloudMonitor agent on the nodes and view monitoring information about the nodes in the CloudMonitor console.
8. Click Submit .
On the Node Pools page, the st at us of the node pool is Scaling. This indicates that the scaleout event is in progress. After the scale-out event is completed, the st at us of the node pool changes to Act ive. What's next Click Det ails in the Actions column for the node pool. On the Nodes tab, you can check the nodes that are added to the node pool.

##### 6.3.12.3 Schedule an application pod to a specific node pool

pool Label is an important concept of Kubernetes. Services, Deployments, and pods are associated with each other by labels. You can configure pod scheduling policies based on node labels. This allows you to schedule pods to nodes that have specific labels. This topic describes how to schedule an application pod to a specific node pool. Procedure
1. Add a label to the nodes in a node pool.
Container Service allows you to manage a group of cluster nodes by using a node pool. For example, you can centrally manage the labels and taints of the nodes in a node pool. For more information about how to create a node pool, see Create a node pool. i. Log on to the Container Service console. ii. In the left-side navigation pane, click Clust ers. iii. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. iv. In the left-side navigation pane of the details page, choose Nodes > Node Pools. v. In the upper-right corner of the Node Pools page, click Creat e Node Pool. vi. In the Create Node Pool dialog box, click Show Advanced Opt ions and click on the right of Node Label to add labels to nodes. In this example, the pod: nginx label is added. You can also click Scale Out on the right side of a node pool to update or add labels for the nodes. If automatic scaling is enabled for a node pool, click Modif y on the right side of the node pool to update or add labels for the nodes.
2. Configure a scheduling policy for an application pod.
After the preceding step is completed, the pod: nginx label is added to the nodes in the node pool. You can set the nodeSelector or nodeAffinity field in pod configurations to ensure that an application pod is scheduled to nodes with matching labels in a node pool. Perform the following steps: Set nodeSelector. nodeSelector is a field in the spec section of pod configurations. Add the pod: nginx label to nodeSelector. Sample template:

```
apiVersion: apps/v1 kind: Deployment metadata:
  name: nginx-deployment-basic
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      nodeSelector:
        pod: nginx      # After you add the label in this field, the application pod
can run only on nodes with this label in the node pool.
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

Set nodeAffinity. You can also use nodeAffinity to schedule an application pod based on your requirements. nodeAffinity supports the following scheduling policies:

```
- requiredDuringSchedulingIgnoredDuringExecution
```

If this policy is used, a pod can be scheduled only to a node that meets the match rules. If no node meets the match rules, the system retries until a node that meets the rules is found. IgnoreDuringExecution indicates that if the label of the node where the pod is deployed changes and no longer meets the match rules, the pod continues to run on the node.

```
- requiredDuringSchedulingRequiredDuringExecution
```

If this policy is used, the pod can be scheduled only to a node that meets the match rules. If no node meets the rules, the system retries until a node that meets the rules is found. RequiredDuringExecution indicates that if the label of the node where the pod is deployed changes and no longer meets the match rules, the system redeploys the pod to another node that meets the rules.

```
- preferredDuringSchedulingIgnoredDuringExecution
```

If this policy is used, the pod is preferably scheduled to a node that meets the match rules. If no node meets the rules, the system ignores the rules.

```
- preferredDuringSchedulingRequiredDuringExecution
```

If this policy is used, the pod is preferably scheduled to a node that meets the match rules. If no node meets the rules, the system ignores the rules. RequiredDuringExecution indicates that if the label of a node where the pod is deployed changes and still meets the match rules, the system reschedules the pod to a node that meets the match rules. In the following example, the requiredDuringSchedulingIgnoredDuringExecution policy is used to ensure that the application pod always runs on a node in a specific node pool.

```
apiVersion: apps/v1 kind: Deployment metadata:
  name: nginx-with-affinity
  labels:
    app: nginx-with-affinity
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-with-affinity
  template:
    metadata:
      labels:
        app: nginx-with-affinity
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: pod
                operator: In      # This policy ensures that the application pod can
run only on a node that has the pod: nginx label.
                values:
                - nginx
      containers:
      - name: nginx-with-affinity
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

Result In the preceding example, all application pods are scheduled to the xxx.xxx.0.74 node. This node has the pod: nignx label.

### 6.4 Storage

#### 6.4.1 Overview

In the Container Service console, you can create volumes of other Apsara Stack services, enabling you to create stateful applications and use Apsara Stack disks and OSS to implement persistent storage. Both static and dynamic volumes are supported. The following table shows how static and dynamic volumes are supported.

| Apsara Stack storage | Static volume | Dynamic volume |
|---|---|---|
| Apsara Stack disk | You can use a static disk volume through either of the following methods: Use a volume directly Use a volume through a PV and PVC | Supported |
| Apsara Stack NAS | You can use a static NAS volume through either of the following methods: Use a volume through the FlexVolume plug-in Use a volume directly Use a volume through a PV or PVC Use a volume through the Kubernetes NFS driver | Supported |
| Apsara Stack OSS | You can use a static OSS volume through either of the following methods: Use a volume directly Use a volume through a PV or PVC | Not supported |

#### 6.4.2 Mount disk volumes

You can mount disks as volumes. Container Service allows you to mount disks as persistent volumes (PVs) in Kubernetes clusters. Disks can be mounted to Kubernetes clusters as the following volume types: Statically provisioned disk volumes You can use statically provisioned disk volumes in the following ways: Mount disks as volumes Mount disk volumes by creating a PV and a persistent volume claim (PVC) Dynamically provisioned disk volumes Usage not es You can mount a disk only to one pod. Before you mount a disk to a pod, you must create the disk and obtain its disk ID. The disk must meet the following capacity requirements: If the disk is a basic disk, it must be at least 5 GiB in size. If the disk is an ultra disk, it must be at least 20 GiB in size. If the disk is a standard SSD, it must be at least 20 GiB in size. volumeId: the ID of the disk that you want to mount. The value must be the same as those of volumeName and PV Name. A disk can be mounted only to a node that is deployed in the same zone as the disk. Only pay-as-you-go disks can be mounted. If you change the billing method of an Elastic Compute Service (ECS) instance in the cluster from pay-as-you-go to subscription, you cannot change the billing method of its disks to subscription. Otherwise, the disks cannot be mounted to the cluster. Statically provisioned disk volumes You can mount disks as volumes or by creating PVs and PVCs. Prerequisit es A disk is created in the ECS console. Mount a disk as a volume Use the following disk-deploy.yaml file to create a pod:

```
apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: nginx-disk-deploy
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx-flexvolume-disk
        image: nginx
        volumeMounts:
          - name: "d-bp1j17ifxfasvts3tf40"
            mountPath: "/data"
      volumes:
        - name: "d-bp1j17ifxfasvts3tf40"
          flexVolume:
            driver: "alicloud/disk"
            fsType: "ext4"
            options:
              volumeId: "d-bp1j17ifxfasvts3tf40"
```

Mount disk volumes by creat ing a PV and a PVC i. Creat e a PV of t he disk t ype You can create a PV of the disk type in the Container Service console or by using a YAML file. Creat e a PV by using a YAML f ile Use the following `disk-pv.yaml` file to create a PV: Not e The PV name must be the same as the disk ID.

```
apiVersion: v1 kind: PersistentVolume metadata:
  name: d-bp1j17ifxfasvts3tf40
  labels:
    failure-domain.beta.kubernetes.io/zone: cn-hangzhou-b
    failure-domain.beta.kubernetes.io/region: cn-hangzhou
spec:
  capacity:
    storage: 20Gi
  storageClassName: disk
  accessModes:
    - ReadWriteOnce
  flexVolume:
    driver: "alicloud/disk"
    fsType: "ext4"
    options:
      volumeId: "d-bp1j17ifxfasvts3tf40"
```

Creat e a PV in t he console a. Log on to the Container Service console. b. In the left-side navigation pane, click Clust ers. c. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. d. In the left-side navigation pane of the details page, choose Volumes > Persist ent Volumes. e. On the Persist ent Volumes page, click Creat e in the upper-right corner. f. In the Create PV dialog box, set the parameters. PV parameters

| Parameter | Description |
|---|---|
| PV T ype | In this example, Cloud Disk is selected. |
| Volume Plug-in | Displays the supported storage drivers. |
| Access Mode | By default, ReadWriteOnce is selected. |
| Disk ID | Select a disk that is in the same region and zone as your cluster. |
| File Syst em T ype | Select the file system of the disk. Supported file systems are ext4, ext3, xfs, and vfat. Default value: ext4. |
| Label | Add labels to the PV. |

g. Click Creat e. ii. Creat e a PVC Use the following `disk-pvc.yaml` file to create a PVC:

```
kind: PersistentVolumeClaim apiVersion: v1 metadata:
  name: pvc-disk
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: disk
  resources:
    requests:
      storage: 20Gi
```

iii. Creat e a pod Use the following disk-pod.yaml file to create a pod:

```
apiVersion: v1 kind: Pod metadata:
  name: "flexvolume-alicloud-example"
spec:
  containers:
    - name: "nginx"
      image: "nginx"
      volumeMounts:
        - name: pvc-disk
          mountPath: "/data"
  volumes:
  - name: pvc-disk
    persistentVolumeClaim:
      claimName: pvc-disk
```

Dynamically provisioned disk volumes To mount a disk as a dynamically provisioned volume, you must create a StorageClass of the disk type and specify the StorageClass in the storageClassName field of the PVC.
1. Creat e a St orageClass

```
kind: StorageClass apiVersion: storage.k8s.io/v1beta1 metadata:
  name: alicloud-disk-common-hangzhou-b
provisioner: alicloud/disk parameters:
  type: cloud_ssd
  regionid: cn-hangzhou
  zoneid: cn-hangzhou-b
```

Required parameters: provisioner: Set this parameter to alicloud/disk. This indicates that the Provisioner plug-in is used to create the StorageClass. type: Specify the disk type. Valid values: cloud, cloud_efficiency, cloud_ssd, and available. If you set this parameter to available, the system attempts to create a disk in the following order: ultra disk, standard SSD, and basic disk. The system stops trying until a disk is created. regionid: Specify the region of the disk. zoneid: Specify the zone of the disk.
2. Creat e a PVC

```
kind: PersistentVolumeClaim apiVersion: v1 metadata:
  name: disk-common
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: alicloud-disk-common-hangzhou-b
  resources:
    requests:
      storage: 20Gi
--kind: Pod apiVersion: v1 metadata:
  name: disk-pod-common
spec:
  containers:
  - name: disk-pod
    image: nginx
    volumeMounts:
      - name: disk-pvc
        mountPath: "/mnt"
  restartPolicy: "Never"
  volumes:
    - name: disk-pvc
      persistentVolumeClaim:
        claimName: disk-common
```

Def ault opt ions By default, Kubernetes clusters support the following types of StorageClass: alicloud-disk-common: basic disk. alicloud-disk-efficiency: ultra disk. alicloud-disk-ssd: standard SSD. alicloud-disk-available: This option ensures high availability. The system attempts to create an ultra disk first. If no ultra disk is available in the specified zone, the system attempts to create a standard SSD. If no standard SSD is available, the system attempts to create a basic disk.
3. Creat e a mult i-inst ance St at ef ulSet by using a disk
We recommend that you use the volumeClaimTemplates parameter. This parameter allows the system to dynamically create PVCs and PVs. PVCs are associated with corresponding PVs.

```
apiVersion: v1 kind: Service metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
--apiVersion: apps/v1beta2 kind: StatefulSet metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: disk-common
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: disk-common
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "alicloud-disk-common"
      resources:
        requests:
          storage: 10Gi
```

#### 6.4.3 Mount NAS volumes

Container Service allows you to mount Apsara File Storage NAS (NAS) file systems as persistent volumes (PVs) in Container Service clusters. NAS file systems can be mounted to Kubernetes clusters as the following volume types: Statically provisioned NAS volumes You can statically provision NAS volumes in the following ways: Use the FlexVolume plug-in Directly mount NAS file systems as volumes Mount NAS file systems by creating a PV and a persistent volume claim (PVC) Use the Network File System (NFS) driver Dynamically provisioned NAS volumes Prerequisites A NAS file system is created in the NAS console and a mount target is added. The mount target is used to mount the NAS file system to the Kubernetes cluster. The NAS file system and your cluster are deployed in the same virtual private cloud (VPC). Statically provisioned NAS volumes You can use the FlexVolume plug-in provided by Alibaba Cloud or the NFS driver provided by Kubernetes to mount NAS file systems. Use t he FlexVolume plug-in You can use the FlexVolume plug-in to directly mount a NAS file system as a volume. You can also mount a NAS file system by creating a PV and a PVC. Not e NAS is a shared storage service. You can mount a NAS file system to multiple pods. server: the mount target of the NAS volume. path: the directory to which the NAS volume is mount. You can specify a subdirectory. If the specified subdirectory does not exist, the system automatically creates the subdirectory. vers: the version of the NFS protocol. Version 4.0 is supported. mode: the access permissions on the directory of the NAS file system. If the root directory of the NAS file system is specified, you cannot modify the access permissions. If the NAS file system stores a large amount of data, the mounting operation may be time-consuming or even fail. Therefore, we recommend that you do not set the mode parameter. Mount a NAS f ile syst em as a volume Use the following `nas-deploy.yaml` file to create a pod:

```
apiVersion: v1 kind: Pod metadata:
  name: "flexvolume-nas-example"
spec:
  containers:
    - name: "nginx"
      image: "nginx"
      volumeMounts:
        - name: "nas1"
          mountPath: "/data"
  volumes:
    - name: "nas1"
      flexVolume:
        driver: "alicloud/nas"
        options:
          server: "0cd8b4a576-grs79.cn-hangzhou.nas.aliyuncs.com"
          path: "/k8s"
          vers: "4.0"
```

Mount a NAS f ile syst em by creat ing a PV and a PVC St ep 1: Creat e a PV You can create a PV in the Container Service console or by using a YAML file. Create a PV by using a YAML file. Use the following `nas-pv.yaml` file to create a PV:

```
apiVersion: v1 kind: PersistentVolume metadata:
  name: pv-nas
spec:
  capacity:
    storage: 5Gi
  storageClassName: nas
  accessModes:
    - ReadWriteMany
  flexVolume:
    driver: "alicloud/nas"
    options:
      server: "0cd8b4a576-uih75.cn-hangzhou.nas.aliyuncs.com"
      path: "/k8s"
      vers: "4.0"
```

Create a PV in the console i. Log on to the Container Service console. ii. In the left-side navigation pane, click Clust ers. iii. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. iv. In the left-side navigation pane of the details page, choose Volumes > Persist ent Volumes. v. On the Persist ent Volumes page, click Creat e in the upper-right corner. vi. In the Create PV dialog box, set the parameters.

| Parameter | Description |
|---|---|
| PV T ype | Select NAS. |
| Volume Name | Enter a name for the PV. The name must be unique in the cluster. |
| Volume Plug-in | By default, CSI is selected. |
| Capacit y | Specify the capacity of the PV. The capacity of the PV cannot exceed the capacity of the disk. |
| Access Mode | By default, ReadWriteMany is selected. |
| Mount T arget Domain Name | The domain name of the mount target that is used to mount the NAS file system to the cluster. |
| Subdirect ory | Enter a subdirectory in the NAS file system. The subdirectory must start with a forward slash (/). If you set this parameter, the PV is mounted to the specified subdirectory. If the specified subdirectory does not exist, the system automatically creates the subdirectory in the NAS file system. If you do not set this parameter, the PV is mounted to the root directory of the NAS file system. |
| Version | The version of the NFS protocol. Version 3 and 4.0 are supported. By default, version 3 is used. We recommend that you use version 3. |
| Label | Add labels to the PV. |

vii. Click Creat e. St ep 2: Creat e a PVC Use the following nas-pvc.yaml file to create a PVC:

```
kind: PersistentVolumeClaim apiVersion: v1 metadata:
  name: pvc-nas
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: nas
  resources:
    requests:
      storage: 5Gi
```

St ep 3: Creat e a pod Use the following nas-pod.yaml file to create a pod:

```
apiVersion: v1 kind: Pod metadata:
  name: "flexvolume-nas-example"
spec:
  containers:
    - name: "nginx"
      image: "nginx"
      volumeMounts:
          - name: pvc-nas
            mountPath: "/data"
  volumes:
  - name: pvc-nas
    persistentVolumeClaim:
        claimName: pvc-nas
```

Use t he NFS driver St ep 1: Creat e a NAS f ile syst em Log on to the NAS console. For more information about how to log on to the NAS console, see the Create a NAS file system chapter of the NAS User Guide. Not e The NAS file system that you want to create and the Kubernetes cluster must be deployed in the same region. In this example, the following mount target is used: `055f84ad83-ixxxx.cn-`

```
hangzhou.nas.aliyuncs.com .
```

St ep 2: Creat e a PV You can create a PV in the console or by using a YAML file. Creat e a PV by using a YAML t emplat e Use the following nas-pv.yaml file to create a PV. Run the following command to create a PV that uses the NAS file system:

```
root@master # cat << EOF |kubectl apply -f apiVersion: v1 kind: PersistentVolume metadata:
   name: nas
spec:
   capacity:
     storage: 8Gi
   accessModes:
     - ReadWriteMany
   persistentVolumeReclaimPolicy: Retain
   nfs:
     path: /
     server: 055f84ad83-ixxxx.cn-hangzhou.nas.aliyuncs.com
EOF
```

Creat e a PV by using t he console For more information, see Mount a NAS file system by creating a PV and a PVC. St ep 3: Creat e a PVC Create a PVC and associate the PVC with the PV that is created in Step 2.

```
root@master # cat << EOF | kubectl apply -f apiVersion: v1 kind: PersistentVolumeClaim metadata:
     name: nasclaim
spec:
     accessModes:
       - ReadWriteMany
     resources:
       requests:
         storage: 8Gi
EOF
```

St ep 4: Creat e a pod Create an application to use the PV.

```
root@master # cat << EOF |kubectl apply -f apiVersion: v1 kind: Pod metadata:
     name: mypod
spec:
     containers:
       - name: myfrontend
         image: registry.aliyuncs.com/spacexnice/netdia:latest
         volumeMounts:
         - mountPath: "/var/www/html"
           name: mypd
     volumes:
       - name: mypd
         persistentVolumeClaim:
           claimName: nasclaim
EOF
```

The NAS file system is mounted to the application that runs in the pod. Dynamically provisioned NAS volumes If you want to dynamically provision NAS volumes, you must install a driver plug-in and configure a NAS mount target. Inst all t he plug-in

```
apiVersion: storage.k8s.io/v1 kind: StorageClass metadata:
  name: alicloud-nas
provisioner: alicloud/nas --apiVersion: v1 kind: ServiceAccount metadata:
  name: alicloud-nas-controller
  namespace: kube-system
--kind: ClusterRoleBinding apiVersion: rbac.authorization.k8s.io/v1beta1 metadata:
  name: run-alicloud-nas-controller
subjects:
  - kind: ServiceAccount
    name: alicloud-nas-controller
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: alicloud-disk-controller-runner
  apiGroup: rbac.authorization.k8s.io
--kind: Deployment apiVersion: extensions/v1beta1
```

```
metadata:
  name: alicloud-nas-controller
  namespace: kube-system
spec:
  replicas: 1
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: alicloud-nas-controller
    spec:
      tolerations:
      - effect: NoSchedule
        operator: Exists
        key: node-role.kubernetes.io/master
      - effect: NoSchedule
        operator: Exists
        key: node.cloudprovider.kubernetes.io/uninitialized
      nodeSelector:
         node-role.kubernetes.io/master: ""
      serviceAccount: alicloud-nas-controller
      containers:
        - name: alicloud-nas-controller
          image: registry.cn-hangzhou.aliyuncs.com/acs/alicloud-nas-controller:v1.8.4
          volumeMounts:
          - mountPath: /persistentvolumes
            name: nfs-client-root
          env:
            - name: PROVISIONER_NAME
              value: alicloud/nas
            - name: NFS_SERVER
              value: 0cd8b4a576-mmi32.cn-hangzhou.nas.aliyuncs.com
            - name: NFS_PATH
              value: /
      volumes:
        - name: nfs-client-root
          nfs:
            server: 0cd8b4a576-mmi32.cn-hangzhou.nas.aliyuncs.com
            path: /
```

Dynamically provision a NAS volume

```
apiVersion: apps/v1beta1 kind: StatefulSet metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 2
  volumeClaimTemplates:
  - metadata:
      name: html
    spec:
      accessModes:
        - ReadWriteOnce
      storageClassName: alicloud-nas
      resources:
        requests:
          storage: 2Gi
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        volumeMounts:
        - mountPath: "/usr/share/nginx/html/"
          name: html
```

#### 6.4.4 Mount OSS volumes

You can mount Object Storage Service (OSS) buckets as volumes in Kubernetes clusters. You can mount OSS buckets in the following ways: Mount an OSS bucket as a volume. Mount an OSS bucket by creating a PV and a PVC. Prerequisites To mount an OSS bucket as a statically provisioned volume, you must create an OSS bucket in the OSS console. Background OSS buckets can be mounted only as statically provisioned volumes. An OSS bucket can be shared by multiple pods. bucket: Only buckets can be mounted to a Kubernetes cluster. The subdirectories or files in a bucket cannot be mounted to a Kubernetes cluster. url: specifies the endpoint of the OSS bucket. The endpoint is the domain name that is used to mount the OSS bucket to the Kubernetes cluster. akId: specifies your AccessKey ID. akSecret: specifies your AccessKey secret. otherOpts: the custom parameters that are used to mount the OSS bucket. The parameters must be in the following format: `-o *** -o ***` . Not e To mount an OSS bucket as a volume, you must create a Secret with your AccessKey pair when you deploy the flexvolume Service. Mount an OSS bucket as a statically provisioned volume Mount an OSS bucket as a volume Use the following oss-deploy.yaml file to create a pod:

```
apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: nginx-oss-deploy
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx-flexvolume-oss
        image: nginx
        volumeMounts:
          - name: "oss1"
            mountPath: "/data"
      volumes:
        - name: "oss1"
          flexVolume:
            driver: "alicloud/oss"
            options:
              bucket: "docker"
              url: "oss-cn-hangzhou.aliyuncs.com"
              akId: ***
              akSecret: ***
              otherOpts: "-o max_stat_cache_size=0 -o allow_other"
```

Creat e a st at ic PV and a PVC i. Creat e a PV You can create a persistent volume (PV) in the Container Service console or by using a YAML file. Creat e a PV by using a YAML f ile Use the following oss-pv.yaml file to create a PV:

```
apiVersion: v1 kind: PersistentVolume metadata:
  name: pv-oss
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany
  storageClassName: oss
  flexVolume:
    driver: "alicloud/oss"
    options:
      bucket: "docker"
      url: "oss-cn-hangzhou.aliyuncs.com"
      akId: ***
      akSecret: ***
      otherOpts: "-o max_stat_cache_size=0 -o allow_other"
```

Creat e a PV in t he Cont ainer Service console a. Log on to the Container Service console. b. In the left-side navigation pane, click Clust ers. c. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. d. In the left-side navigation pane of the details page, choose Volumes > Persist ent Volumes. e. On the Persist ent Volumes page, click Creat e in the upper-right corner. f. In the Create PV dialog box, set the parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| PV T ype | In this example, OSS is selected. |   |   |
| Name | Enter a name for the PV. The name must be unique in the cluster. In this example, pv-oss is used. |   |   |
| Volume Plug-in | By default, CSI is selected. |   |   |
| Capacit y | Specify the capacity of the PV. |   |   |
| Access Mode | By default, ReadWriteMany is selected. |   |   |
| AccessKey ID and AccessKey Secret | The AccessKey pair that is required to access OSS buckets. To obtain your AccessKey pair, go to the Apsara Uni-manager Management Console, choose Ent erprise > Organizat ions, click on the right side of the organization. Then, click AccessKey and copy the AccessKey pair. |   |   |
| Opt ional Paramet ers | Enter custom parameters in the format of -o *** -o *** . |   |   |
| Bucket ID | Enter the name of the OSS bucket that you want to mount. Click Select Bucket . In the dialog box that appears, select the OSS bucket that you want to mount and click Select . |   |   |
| Endpoint | Int ernal Endpoint is recommended. |   |   |
| Label | Add labels to the PV. |   |   |

g. Click Creat e. ii. Creat e a PVC Use the following oss-pvc.yaml file to create a persistent volume claim (PVC):

```
kind: PersistentVolumeClaim apiVersion: v1 metadata:
  name: pvc-oss
spec:
  storageClassName: oss
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
```

iii. Creat e a pod Use the following oss-pod.yaml file to create a pod:

```
apiVersion: v1 kind: Pod metadata:
  name: "flexvolume-oss-example"
spec:
  containers:
    - name: "nginx"
      image: "nginx"
      volumeMounts:
          - name: pvc-oss
            mountPath: "/data"
  volumes:
  - name: pvc-oss
    persistentVolumeClaim:
        claimName: pvc-oss
```

Can I mount an OSS bucket as a dynamically provisioned volume? No. Dynamically provisioned OSS volumes are not supported.

#### 6.4.5 Create a PVC

This topic describes how to create a persistent volume claim (PVC). Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A persistent volume (PV) is created. In this example, a PV created from a disk is used. For more information, see Use Apsara Stack disks. By default, PVCs are associated with PVs that have the alicloud-pvname label. This label is added to all PVs that are created in the Container Service console. If a PV does not have this label, manually add the label to the PV before you can associate the PV with a PVC. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Volumes > Persist ent Volume
Claims.
5. In the upper-right corner of the Persist ent Volume Claims page, click Creat e.
6. In the Creat e PVC dialog box, set the parameters and click Creat e.
PVC T ype: The PVC and PV must be of the same type. You can select Cloud Disk, NAS, and OSS. Name: Enter the name of the PVC. Allocat ion Mode: Use St orageClass, Exist ing Volumes, and Creat e Volume are supported. In this example, Use St orageClass or Exist ing Volumes is selected. Exist ing St orage Class: Click Select . In the Select Storage Class dialog box, find the Storage Class that you want to use and click Select in the Actions column. This parameter is required only when you set Allocation Mode to Use St orageClass. Exist ing Volumes: Click Select PV. In the Select PV dialog box, find the PV that you want to use and click Select in the Actions column. This parameter is required only when you set Allocation Mode to Exist ing Volumes. Capacit y: Specifies the capacity used by the PVC. The value cannot be larger than the total capacity of the associated PV. Access Mode: The default value is ReadWriteOnce. This parameter is required only when you set Allocation Mode to Use St orageClass. Not e If your cluster has a PV that is not used, but you cannot find it in the Select PV dialog box, the reason may be that the PV does not have the alicloud-pvname label. If you cannot find available PVs, click Persist ent Volumes in the left-side navigation pane. On the Persistent Volumes page, find the PV that you want to use, click Manage Labels in the Actions column, and then add a label to the PV. On the Manage Labels dialog box, set the key of the label to alicloud-pvname and the value to the name of the PV. If the PV is created from a disk, the disk ID is used as the name of the PV.
7. Go to the Persistent Volume Claims page. You can find the newly created PVC in the list.

#### 6.4.6 Use PVCs

You can use persistent volume claims (PVCs) to mount volumes for applications. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A PVC is created. In this example, a PVC named pvc-disk is created to mount a disk volume. For more information, see Create PVCs. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, click Creat e f rom Image in the upper-right corner.
6. On the Basic Inf ormat ion wizard page, specify the application name, number of replicas, type,
and labels, select whether to synchronize the time zone from nodes to containers, and then click Next .
7. On the Cont ainer wizard page, select an image and configure volumes of the cloud storage type.
You can select Cloud Disk, Apsara File Storage NAS (NAS), and Object Service Storage (OSS). In this example, select the PVC named pvc-disk and click Next . For more information, see Container configurations.
8. On the Advanced wizard page, create a Service for the test-nginx application and click Creat e.
9. On the Complet e wizard page, click View Details to view detailed information about the
application. You are redirected to the details page of the test-nginx application.
10. On the Pods tab, you can find the pods to which the application belongs. Select a pod and click
View Det ails to view detailed information about the pod.
11. On the details page of the pod, click the Volumes tab. You can find that the pod is associated
with the pvc-disk PVC.

### 6.5 Network management

#### 6.5.1 Set access control for pods

This topic describes how to use network policies to control access between pods. Prerequisites You have created a Kubernetes cluster and selected the T erwaynet work plug-in. For more information, see Create a Kubernetes cluster. Context You can declare network policies to control access between pods and thus prevent applications from interfering each other. Procedure For more information about standard Kubernetes network policies, see Network policies.
1. Create a pod that runs as a server and attach `label run=nginx` to the pod. For more
information, see Create an application from an orchestration template. The sample YAML file is as follows:

```
apiVersion: v1 kind: Pod metadata:
  name: server
  labels:
    run: nginx
spec:
  containers:
    - name: nginx
      image: registry.acs.intranet.env22.com/nginx:1.8
```

2. Create a network policy. For more information, see Create an application from an orchestration
template. The sample YAML file is as follows:

```
kind: NetworkPolicy apiVersion: networking.k8s.io/v1 metadata:
  name: access-nginx
spec:
  podSelector:
    matchLabels:
      run: nginx # Apply the network policy to pods with the run=nginx label
  ingress:
  - from:
    - podSelector:
        matchLabels:
          access: "true" # Only pods with the access=true label are accessible
```

3. Use the client.yaml and client-label files to create two pods that run as clients.
One pod has the required label and the other does not. i. Create the client.yaml and client-label files with the following contents respectively.

```bash
# This pod has no label
apiVersion: v1 kind: Pod metadata:
  name: client
spec:
  containers:
    - name: busybox
      image: registry.acs.intranet.env22.com/acs/busybox
      command: ["sh", "-c", "sleep 200000"]
# This pod has the label
apiVersion: v1 kind: Pod metadata:
  name: client-label
  labels:
    access: "true"
spec:
  containers:
    - name: busybox
      image: registry.acs.intranet.env22.com/acs/busybox
      command: ["sh", "-c", "sleep 200000"]
```

ii. Run the following commands to create these pods:

```bash
kubectl apply -f client.yaml kubectl apply -f client-label.yaml
```

You can see that only the pod with the required label can access the server.

#### 6.5.2 Set bandwidth limits for pods

This topic describes how to limit the bandwidth of inbound and outbound traffic that flows through a pod. Prerequisites You have created a Kubernetes cluster and selected the T erwaynet work plug-in. For more information, see Create a Kubernetes cluster. Context Throttling pods helps prevent performance degradation of the host or other workloads when certain pods occupy excessive resources. Method You can use the `k8s.aliyun.com/ingress-bandwidth` and `k8s.aliyun.com/egress-bandwidth` annotations for pod throttling.

| k8s.aliyun.com/ingress-bandwidth |   |
|---|---|
| k8s.aliyun.com/egress-bandwidth | : |

The bandwidth limit is measured in m and k, which represent Mbit/s and Kbit/s respectively. Procedure
1. Create a pod that runs as a server in the console. For more information, see Create an application
from an orchestration template. The sample YAML file is as follows:

```
apiVersion: v1 kind: Pod metadata:
  name: server
  annotations:
    k8s.aliyun.com/ingress-bandwidth: 10m # Set the inbound bandwidth limit to 10 Mbit/
```

`s`

```
    k8s.aliyun.com/egress-bandwidth: 10m
spec:
  containers:
    - name: nginx
      image: registry.acs.intranet.env22.com/nginx:1.8
```

2. Run the kubectl exec command to connect to the pod. To verify that pod throttling is effective,
run the following commands to create a file on the pod. Assume that the IP address of the pod created in step 1 is 172.16.XX.XX.

```
cd /usr/share/nginx/html dd if=/dev/zero of=bigfile bs=1M count=1000
```

3. Use the client-deploy.yaml file to create a pod that runs as a client.
i. Create the client-deploy.yaml file with the following content:

```
apiVersion: v1 kind: Pod metadata:
  name: client
  annotations:
     k8s.aliyun.com/ingress-bandwidth: 10m # Set the inbound bandwidth limit to 10
Mbit/s
     k8s.aliyun.com/egress-bandwidth: 10m
spec:
  containers:
    - name: busybox
      image: registry.acs.intranet.env22.com/acs/netdia
      command: ["sh", "-c", "sleep 200000"]
```

ii. Run the following command to create the pod:

```bash
kubectl apply -f client-deploy.yaml
```

4. Run the following command to check whether bandwidth is limited:

```bash
kubectl exec -it client sh
```

#### 6.5.3 Work with Terway

Terway is an open source Container Network Interface (CNI) plug-in developed by Alibaba Cloud. Terway works with Virtual Private Cloud (VPC) and allows you to use standard Kubernetes network policies to regulate how containers communicate with each other. You can use Terway to enable internal communication within a Kubernetes cluster. This topic describes how to use Terway. Context Terway is a network plug-in developed by Alibaba Cloud for Container Service. Terway allows you to set up networks for pods by associating Alibaba Cloud elastic network interfaces (ENIs) with the pods. Terway also allows you to use standard Kubernetes network policies to regulate how containers communicate with each other. In addition, Terway is compatible with Calico network polices. In a cluster that has Terway installed, each pod has a separate network stack and is assigned a separate IP address. Pods on the same Elastic Compute Service (ECS) instance communicate with each other by forwarding packets inside the ECS instance. Pods on different ECS instances communicate with each other through ENIs in the VPC where the ECS instances are deployed. This improves communication efficiency because no tunneling technologies such as Virtual Extensible Local Area Network (VXLAN) are required to encapsulate packets. How Terway works Comparison between Flannel and Terway When you create a Kubernetes cluster, you can choose one of the following network plug-ins: Terway: a network plug-in developed by Alibaba Cloud for Container Service. Terway allows you to assign ENIs to containers and use standard Kubernetes network policies to regulate how containers communicate with each other. Terway also supports bandwidth throttling on individual containers. Terway uses flexible IP Address Management (IPAM) policies to allocate IP addresses to containers. This avoids IP address waste. If you do not want to use network policies, you can select Flannel as the network plug-in. Otherwise, we recommend that you select Terway. Flannel: an open source CNI plug-in, which is simple and stable. You can use Flannel with VPC of Alibaba Cloud. This allows your clusters and containers to run in high-performance and stable networks. However, Flannel provides only basic features. It does not support standard Kubernetes network policies. For more information, see Flannel.

| Item | Terway | Flannel |
|---|---|---|

| Item | Terway | Flannel |
|---|---|---|
| Performance | The IP address of each pod in a Kubernetes cluster is assigned from the CIDR block of the VPC where the cluster is deployed. Therefore, you do not need to use the Network Address Translation (NAT) service to translate IP addresses. This avoids IP address waste. In addition, each pod in the cluster can use an exclusive ENI. | Flannel works with VPC of Alibaba Cloud. The CIDR block of pods that you specify must be different from that of the VPC where the cluster is deployed. Therefore, the NAT service is required and some IP addresses may be wasted. |
| Security | Terway supports network policies. | Flannel does not support network policies. |
| IP address management | Terway allows you to assign IP addresses on demand. You do not have to assign CIDR blocks by node. This avoids IP address waste. | You can only assign CIDR blocks by node. In large-scale clusters, a great number of IP addresses may be wasted. |
| SLB | Server Load Balancer (SLB) directly forwards network traffic to pods. You can upgrade the pods without service interruption. | SLB forwards network traffic to the NodePort Service. Then, the NodePort Service routes the network traffic to pods. |

Considerations To use the Terway plug-in, we recommend that you use ECS instances of higher specifications and newer types, such as ECS instances that belong to the g5 or g6 instance family with at least eight CPU cores. For more information, see the Instance families chapter of ECS User Guide. The maximum number of pods that each node supports is based on the number of ENIs assigned to the node. Maximum number of pods supported by each shared ENI = (Number of ENIs supported by each ECS instance - 1) × Number of private IP addresses supported by each ENI Maximum number of pods supported by each exclusive ENI = Number of ENIs supported by each ECS instance -1 Step 1: Plan CIDR blocks When you create a Kubernetes cluster, you must specify a VPC, vSwitches, the CIDR block of pods, and the CIDR block of Services. If you want to install the Terway plug-in, you must first create a VPC and two vSwitches in the VPC. The two vSwitches must be created in the same zone. You can assign the following CIDR blocks for a cluster that uses Terway. VPC CIDR block: 192.168.0.0/16 vSwitch CIDR block: 192.168.0.0/19 CIDR block of pod vSwitch: 192.168.32.0/19 Service CIDR block:172.21.0.0/20 IP addresses within the CIDR block of the vSwitch are assigned to nodes. IP addresses within the CIDR block of the pod vSwitch are assigned to pods. The following example describes how to create a VPC and two vSwitches. The CIDR blocks in the preceding section are assigned in this example.
1. Log on to the VPC console.
Not e For more information, see the Log on to the VPC console chapter of VPC.
2. Create a VPC.
i. In the top navigation bar, select the region where you want to create the VPC. ii. On the VPCs page, click Creat e VPC. iii. On the Creat e VPC page, set the following parameters and click Submit .

| Paramete r | Description |
|---|---|
| Organiz at ion | Select the organization to which the VPC belongs. |
| Resourc e Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set : Only the administrator of the current resource set can use the VPC to create resources. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the shared VPC. Current Organizat ion: Only the administrator of the current organization can use create resources for the shared VPC. |
| VPC Name | Enter a name for the VPC. In this example, vpc 192 168 0 0 16 is used. _ _ _ _ _ The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter and cannot start _ with http:// or https:// . |
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. In this example, 192.168.0.0/16 is specified. Not e After a VPC is created, the IPv4 CIDR block of the VPC cannot be modified. |

| Paramete r | Description |
|---|---|
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: An IPv6 CIDR block is automatically assigned to the VPC. If you set this parameter to Assign, the system automatically creates a free IPv6 gateway for this VPC, and assigns an IPv6 CIDR block with the subnet mask /56, such as 2xx1: db8::/56. By default, IPv6 addresses can be used to communicate within only private networks. If you want to allow an instance assigned with an IPv6 address to access the Internet or be accessed by IPv6 clients over the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. For more information, see the Act ivat e IPv6 Int ernet bandwidt h section of the Manage IPv6 Int ernet bandwidt h topic of the IPv6 gateway user guide. |
| Descript ion | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with _ a letter and cannot start with http:// or https:// . |

3. Create vSwitches.
i. In the left-side navigation pane, click VSwit ches. ii. Select the region of the VPC in which you want to create a vSwitch. iii. On the VSwit ches page, click Creat e VSwit ch. iv. On the Creat e vSwit ch page, set the following parameters and click Submit . Not e Make sure that the two vSwitches are in the same zone.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone to which the vSwitch belongs. In a VPC, each vSwitch can be deployed in only one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e A cloud instance can be deployed in only one vSwitch. |

| Parameter | Description |
|---|---|
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set : Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organizat ion: Only the administrator of the current organization can create resources in the shared vSwitch. |
| VPC | Select the VPC for which you want to create the vSwitch. |
| Dedicat ed f or Out -of -cloud Physical Machines | Specify whether the vSwitch to be created is dedicated for bare-metal instances. For more information about bare-metal instances, see the VPC bare-met al inst ance f eat ures topic in BMS User Guide. |
| vSwit ch Name | Enter a name for the vSwitch. In this example, node switch 192 168 0 0 19 is _ _ _ _ _ _ used. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must _ start with a letter and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. In this example, 192.168.0.0/19 is used. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. You must check whether IPv6 is enabled for the specified VPC. If IPv6 is disabled, you cannot assign an IPv6 CIDR block to the vSwitch. If IPv6 is enabled, you can enter a decimal number ranging from 0 to 255 to define the last 8 bits of the IPv6 CIDR block of the vSwitch. For example, if the IPv6 CIDR block of the VPC is 2xx1:db8::/64, specify 255 to define the last 8 bits of the IPv6 CIDR block. In this case, the IPv6 CIDR block of the vSwitch is 2xx1:db8:ff::/64. ff is the hexadecimal value of 255. |
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). The _ name must start with a letter and cannot start with http:// or https:// . |

4. Repeat Step to create a pod vSwitch. Set the name of the pod vSwitch to
pod_swit ch_192_168_32_0_19 and IPv4 CIDR Block to 192.168.32.0/19. Step 2: Set up networks for a cluster that uses Terway To install Terway in a cluster and set up networks for the cluster, set the following parameters. A Kubernetes cluster is used as an example to show how to set up networks for a cluster that uses Terway as the network plug-in. For more information about how to create a Kubernetes cluster, see Create a Kubernetes cluster. VPC: Select the VPC created in Step 1: Plan CIDR blocks. VSwit ch: Select the vSwitch created in Step 1: Plan CIDR blocks. Net work Plug-in: Select T erway. Pod VSwit ch: Select the pod vSwitch created in Step 1: Plan CIDR blocks. Service CIDR: Use the default settings.

### 6.6 Namespaces

#### 6.6.1 Create a namespace

You can create a namespace in the Container Service console. Prerequisites A Kubernetes cluster is created. Context In a Kubernetes cluster, you can use namespaces to create multiple virtual spaces. When a large number of users share a cluster, you can use namespaces to divide different workspaces and allocate cluster resources to different tasks. You can also use resource quotas to allocate resources to each namespace. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, click Namespaces and Quot as.
5. On the Namespace page, click Creat e in the upper-right corner.
6. In the Creat e Namespace dialog box, configure the namespace.
Create a namespace

| Parameter | Description |
|---|---|
| Name | Enter a name for the namespace. In this example, test is entered. The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). It must start and end with a letter or digit. |

| Parameter | Description |
|---|---|
| Label | Label: Add one or more labels to the namespace. Labels are used to identify namespaces. For example, you can label a namespace as one used in the test environment. To add a label, enter a key and a value and click Add in the Actions column. |

7. Click OK.
You can find the namespace that you created on the Namespace page.

#### 6.6.2 Set resource quotas and limits

You can set resource quotas and limits for a namespace in the Container Service console. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A sample namespace named t est is created. For more information, see Create a namespace. You are connected to a master node of the cluster. For more information, see Connect to a Kubernetes cluster through kubectl. Context By default, a running pod uses the CPU and memory resources of a node without limit. This means that pods can compete for computing resources of a cluster. As a result, the pods in a namespace may exhaust all of the computing resources. Namespaces can be used as virtual clusters to serve multiple purposes. We recommend that you set resource quotas for namespaces. For a namespace, you can set quotas on resources such as CPU, memory, and pod quantity. For more information, see Resource Quotas. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, click Namespaces and Quot as.
5. Find the namespace that you want to manage and click Resource Quot as and Limit s in the
Act ions column.
6. In the dialog box that appears, set resource quotas and default resource limits.
Not e After you set CPU and memory quotas for a namespace, you must specify CPU and memory limits when you create a pod. You can also set the default resource limits for the namespace. For more information, see Resource Quotas. i. Set resource quotas for the namespace. ii. You can set resource limits and resource requests for containers in the namespace. This enables you to control the amount of resources consumed by the containers. For more information, see https://kubernetes.io//memory-default-namespace/.
7. After you set resource quotas and limits, connect to a master node of the cluster and run the
following commands to query the resource configurations of the namespace.

```bash
# kubectl get limitrange,ResourceQuota -n test
NAME AGE limitrange/limits 8m NAME AGE resourcequota/quota 8m
# kubectl describe limitrange/limits resourcequota/quota -n test
Name: limits Namespace: test Type Resource Min Max Default Request Default Limit Max Limit/Request Ratio ---- -------- --- --- --------------- ------------- ----------------------- Container cpu - - 100m 500m - Container memory - - 256Mi 512Mi - Name: quota Namespace: test Resource Used Hard -------- ---- ---configmaps 0 100 limits.cpu 0 2 limits.memory 0 4Gi persistentvolumeclaims 0 50 pods 0 50 requests.storage 0 1Ti secrets 1 10 services 0 20 services.loadbalancers 0 5
```

#### 6.6.3 Modify a namespace

You can modify an existing namespace. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A sample namespace named t est is created. For more information, see Create a namespace. Context When you modify a namespace, you can add, delete, or modify the labels that are added to the namespace based on your requirements. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, click Namespaces and Quot as.
5. Find the namespace that you want to modify and click Edit in the Act ions column.
6. In the Edit Namespace dialog box, find the label that you want to modify and click Edit to
modify the label. For example, you can change the key-value pair of the label to `env:test-V2` . Then, click Save.
7. Click OK.
You can find that the labels of the namespace on the Namespace page are updated.

#### 6.6.4 Delete a namespace

You can delete namespaces that are no longer in use. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A sample namespace named t est is created. For more information, see Create a namespace. Context Not e When you delete a namespace, all resource objects under the namespace are deleted. Proceed with caution. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, click Namespaces and Quot as.
5. Find the namespace that you want to delete and click Delet e in the Act ions column.
6. In the message that appears, click Conf irm.
Return to the Namespace page. You can find that the namespace is deleted. Resource objects in the namespace are also deleted.

### 6.7 Applications

#### 6.7.1 Create an application from an image

You can use an image to create an NGINX application that is accessible over the Internet. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Your Kubernetes cluster is accessible over the Internet. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom Image in the upper-right
corner.
6. On the page that appears, set the following parameters: Name, Clust er, Namespace, Replicas,
and T ype. Then, select Synchronize T imezone. Click Next . If you do not set the Namespace parameter, the default namespace is used.
7. Configure containers.
Not e You can configure a pod that contains one or more containers for the application. i. Configure basic settings. Basic settings of the container

| Parameter | Description |   |   |
|---|---|---|---|
| Image Name | You can click Select Image to select an image in the dialog box that appears and click OK. In this example, NGINX is selected. You can also specify an image in a private registry. Use the following format to specify an image in a private registry: domainname/namespac e/imagename . |   |   |
|   |   | domainname/namespac |   |
| Image Version | You can click Select Image Version to select a version. If you do not specify the image version, the latest version is used. |   |   |
| Always | Container Service caches images to improve the efficiency of application deployment. When Container Service deploys the application, if the specified image version is the same as the cached image version, the cached image is used. Therefore, when you update the application code, if you do not change the image version for reasons such as to support the upper-layer workloads, the cached image is used to deploy the application. After you select the Always option, Container Service always pulls the latest image from the repository. This ensures that the latest image and code are used to deploy the application. |   |   |
| Set Image Pull Secret | Click Set Image Pull Secret to set the image Secret. The Secret is required if you need to access a private repository. |   |   |
| Resource Limit | The upper limits of CPU and memory resources that can be used by this application. This prevents the application from occupying excessive resources. The unit of CPU resources is Core. The unit of memory is MiB. |   |   |
| Required Resources | The amount of CPU and memory resources that are reserved for this application. These resources are exclusive to the container. This prevents other services or processes from occupying the resources of the application. |   |   |
| Cont ainer St art Paramet er | st din: Pass stdin to the container. t t y: Stdin is a TTY. Typically, these two check boxes are both selected. This allows you to associate the terminal (tty) with the standard inputs (stdin) of the container. For example, an interactive program can obtain standard inputs from users and then display the inputs on the terminal. |   |   |
| Init Cont ainer | When this check box is selected, the system creates an Init Container that contains useful tools. For more information, see . |   |   |

|   | e/imagename |
|---|---|

ii. (Optional)Set environment variables. You can set environment variables in key-value pairs for pods. Environment variables are used to apply pod configurations to containers. For more information, see Pod variable. iii. (Optional)Configure the Healt h Check settings. Health check settings include liveness and readiness probes. Liveness probes determine when to restart the container. Readiness probes indicate whether the container is ready to accept network traffic. For more information about health checks, see .

| Request type | Description |
|---|---|
| HT T P | Sends an HTTP GET request to the container. Supported parameters: Protocol: HTTP or HTTPS. Path: the requested path on the server. Port: the container port that you want to open. Enter a port number from 1 to 65535. HTTP Header: the custom headers in the HTTP request. Duplicate headers are allowed. Key-value pairs are supported. Initial Delay (s): The init ialDelaySeconds field. The time (in seconds) to wait before performing the first probe after the container is started. Default value: 3. Period (s): the periodSeconds field. The intervals (in seconds) between two adjacent probes. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field. The time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |

| Request type | Description |
|---|---|
| T CP | Sends a TCP socket to the container. Kubelet attempts to open the socket on the specified port. If the connection can be established, the container is considered healthy. Otherwise, the container is considered unhealthy. You can set the following parameters: Port: the container port that you want to open. Enter a port number from 1 to 65535. Initial Delay (s): the init ialDelaySeconds field. The time (in seconds) to wait before performing the first probe after the container is started. Default value: 15. Period (s): the periodSeconds field. The intervals (in seconds) between two adjacent probes. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field. The time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |
| Command | Runs a probe command in the container to check the health status of the container. You can set the following parameters: Command: the probe command that is run to check the health status of the container. Initial Delay (s): the init ialDelaySeconds field. The time (in seconds) to wait before performing the first probe after the container is started. Default value: 5. Period (s): the periodSeconds field. The intervals (in seconds) between two adjacent probes. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field. The time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |

iv. Configure the lifecycle of the container. You can set the following parameters to configure the lifecycle of the container in the Start, Post Start, and Pre Stop fields. For more information, see https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/. St art : the pre-start command and parameter. Post St art : the post-start command. Pre St op: the pre-stop command. v. (Optional)Configure volumes. Local storage and cloud storage are supported. Local St orage: supports hostPath, ConfigMap, Secret, and emptyDir. The specified volume is mounted to a path in the container. For more information, see Volumes. Cloud St orage: supports disks, Apsara File Storage NAS (NAS) volumes, and Object Storage Service (OSS) volumes. In this example, a persistent volume (PV) is created from a disk and mounted to the /tmp path in the container. Data generated in this path is stored in the disk. vi. (Optional)Configure Log Service. You can specify log collection configurations and custom tags. Not e Make sure that the Log Service agent is installed in the cluster. You can configure the following log collection settings: Logst ore: Create a Logstore in Log Service to store the collected log data. Log Pat h in Cont ainer: Specify stdout or a path to collect log data. st dout : specifies that the stdout files are collected. T ext Logs: specifies that the log data in the specified path of the container is collected. In this example, the log data in the /var/log/nginx path is collected. Wildcard characters can be used in the path. You can also add custom tags. Tags are added to the log data of the container when the log data is collected. Log data with tags is easier to aggregate and filter.
8. After you complete the configurations of the container, click Next .
9. Configure advanced settings. Configure the Access Cont rol settings.
You can configure the method to expose pods and click Creat e. In this example, a ClusterIP Service and an Ingress are created to enable Internet access to the NGINX application. You can configure the following access control settings based on your business requirements: Internal applications: For applications that run inside the cluster, you can create a ClusterIP Service or a NodePort Service to enable internal communication. External applications: For applications that need to be accessed over the Internet, you can configure access control settings by using one of the following methods: Create a LoadBalancer Service: When you create a LoadBalancer Service, a Server Load Balancer (SLB) instance is associated with the Service and is created to expose applications to the Internet. Create a ClusterIP Service or a NordPort Service, and then create an Ingress: When you use this method, an Ingress is created to expose applications to the Internet. For more information, see . i. To create Services, click Creat e in the Access Control section. In the dialog box that appears, set the parameters, and then click Creat e.

| Parameter | Description |
|---|---|
| Name | Enter a name for the Service. Default value: applicationname-svc . |

| Parameter | Description |   |   |
|---|---|---|---|
| T ype | Select one from the following three Service types: Cluster IP: creates a ClusterIP Service. This type of Service exposes applications through an internal IP address of the cluster. If you select this type, applications can be accessed only within the cluster. Node Port: creates a NordPort Service. This type of Service exposes applications through the IP address and static port on each node. A NodePort Service can be used to route requests to a ClusterIP Service. The system automatically creates the ClusterIP Service. You can access a NodePort Service from outside the cluster by requesting <NodeIP> :<NodePort> . Server Load Balancer: creates a LoadBalancer Service. This type of Service exposes applications through an SLB instance, which supports Internet access or internal access. The SLB instance can route requests to NodePort and ClusterIP Services. |   |   |
|   |   | <NodeIP> |   |
| Port Mapping | Specify a Service port and a container port. If the T ype parameter is set to Node Port, you must specify a node port to avoid port conflicts. TCP and UDP protocols are supported. |   |   |
| Annot at ions | Add annotations to the Service. SLB parameters are supported. For more information, see Access services by using SLB. |   |   |
| Label | Add one or more labels to the Service. The labels are used to identify the Service. |   |   |

|   | :<NodePort> |
|---|---|

ii. To create Ingresses, click Creat e in the Access Control section. Configure Ingress rules in the dialog box that appears, and then click Creat e. For more information about Ingress configuration, see Ingress configurations. When you create an application from an image, you can create an Ingress for only one Service. In this example, a virtual hostname is specified as the test domain name. You must add a mapping rule to the hosts file for this domain name, as shown in the following code block. In actual scenarios, use a domain name that has obtained an Internet Content Provider (ICP) number.

```
101.37.224.146 foo.bar.com #The IP address of the Ingress.
```

iii. You can find the newly created Service and Ingress in the Access Control section. You can click Updat e or Delet e to make changes.
10. Click Creat e.
11. After the application is created, you are redirected to the Complete page, which displays the
resource objects under the application. You can click View Det ails to view application details. The nginx-deployment details page appears.
12. In the left-side navigation pane, choose Services and Ingresses > Ingresses. On the Ingresses
page, you can find the created Ingress.
13. Enter the test domain in the address bar of your browser and press Enter. The NGINX welcome
page appears.

#### 6.7.2 Create an application from an orchestration template

orchestration template Container Service provides orchestration templates that you can use to create applications. You can also modify the templates based on YAML syntax to customize applications. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Context This topic describes how to use an orchestration template to create an NGINX application that consists of a Deployment and a Service. The Deployment provisions pods for the application and the Service manages access to the pods at the backend. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom YAML in the upper-right
corner.
6. Configure the template and click Creat e.
Sample T emplat e: Container Service provides YAML templates of various resource types to help you quickly deploy resource objects. You can also create a custom template based on YAML syntax to describe the resource that you want to define. Add Deployment : This feature allows you to quickly define a YAML template. Use Exist ing T emplat e: You can import an existing template to the configuration page. Based on an orchestration template provided by Container Service, the following sample template is used to create a Deployment of an NGINX application. Not e Container Service supports YAML syntax. You can use the `---` symbol to separate multiple resource objects. This allows you to create multiple resource objects in a single template.

```
apiVersion: apps/v1beta2 # for versions before 1.8.0 use apps/v1beta1 kind: Deployment metadata:
    name: nginx-deployment
    labels:
      app: nginx
spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:1.7.9 # replace it with your exactly <image_name:tags>
          ports:
          - containerPort: 80
--apiVersion: v1 # for versions before 1.8.0 use apps/v1beta1 kind: Service metadata:
   name: my-service1        #TODO: to specify your service name
   labels:
     app: nginx
spec:
   selector:
     app: nginx             #TODO: change label selector to match your backend pod
   ports:
   - protocol: TCP
     name: http
     port: 30080            #TODO: choose an unique port on each node to avoid port con
flict
     targetPort: 80
   type: LoadBalancer        ##In this example, the type is changed from Nodeport to Lo
adBalancer.
```

7. Click Creat e. A message that indicates the deployment status appears.
After the application is created, choose Services and Ingresses > Services in the left-side navigation pane. On the Services page, you can find that a Service named my-service1 is created for the application. The external endpoint of the Service is also displayed on the page. Click the endpoint in the Ext ernal Endpoint column.
8. You can visit the NGINX welcome page in the browser.

#### 6.7.3 Use commands to manage applications

You can use commands to create applications or view application containers. Prerequisites Before you use commands on your local host, you have connected to a Kubernetes cluster through kubectl. For more information, see Connect to a Kubernetes cluster through kubectl. Run a command to create an application You can use the following command to run a simple container (an NGINX Web server in this example):

```bash
 # kubectl run -it nginx --image=registry.aliyuncs.com/spacexnice/netdia:latest
```

This command creates a service portal for this container. After you specify `--type=LoadBalancer` , an SLB route to the NGINX container is created.

```bash
# kubectl expose deployment nginx --port=80 --target-port=80 --type=LoadBalancer
```

Run a command to view container information Run the following command to list all running containers in the default namespace:

```
root@master # kubectl get pods
    NAME                                   READY     STATUS    RESTARTS   AGE
    nginx-2721357637-dvwq3                 1/1       Running   1          9h
```

#### 6.7.4 Create a Service

You can create a Service for your application in the Container Service console. The Service provides access to the application. In Kubernetes, a Service is an abstraction which defines a logical set of pods and a policy by which to access the pods. This pattern is also known as a microservice. A label selector determines whether the set of pods can be accessed by the Service. Each pod in Kubernetes clusters has its own IP address. However, pods are frequently created and deleted. Therefore, if you directly expose pods to external access, high availability is not ensured. Services decouple the frontend from the backend. The frontend clients do not need to be aware of which backend pods are used. This provides a loosely-decoupled microservice architecture. For more information, see Kubernetes Services. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Step 1: Create a Deployment
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom T emplat e in the upper-
right corner.
6. Select a sample template or customize a template, and click Creat e.
In this example, the template of an NGINX Deployment is used.

```
apiVersion: apps/v1 # for versions before 1.8.0 use apps/v1beta1 kind: Deployment metad ata: name: nginx-deployment-basic labels: app: nginx spec: replicas: 2 selector: matchL abels: app: nginx template: metadata: labels: app: nginx spec: # nodeSelector: # env: t est-team containers: - name: nginx image: nginx:1.7.9 # replace it with your exactly <i mage_name:tags> ports: - containerPort: 80
```

Query the state of the Deployment. Step 2: Create a Service
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Services.
5. On the Services page, select the Namespace and click Creat e in the upper-right corner.
6. On the Create Service dialog box, set the parameters.
Name: Enter a name for the Service. In this example, nginx-svc is used. T ype: Select the type of the Service. This parameter specifies how to access the Service. Valid values: Cluster IP: a ClusterIP Service. This type of Service exposes pods through an internal IP address of the cluster. If you select this option, pods can be accessed only within the cluster. This is the default value. Node Port: a NodePort Service. This type of Service exposes pods by using the IP address and a static port of each node. A NodePort Service can be used to route requests to a ClusterIP Service, which is automatically created by the system. You can access a NodePort Service from outside the cluster by sending requests to `<NodeIP>:<NodePort>` . Server Load Balancer: a LoadBalancer Service. This type of Service exposes pods by using Server Load Balancer (SLB) instances, which support Internet access or internal access. SLB instances can be used to route requests to NodePort and ClusterIP Services. Backend: the backend object that you want to associate with the Service. In this example, select nginx-deployment-basic that was created in the preceding step. If you do not associate the Service with a backend object, no Endpoint object is created. You can also manually associate the Service with an Endpoint object. For more information, see Create a Service without selectors. Port Mapping: Set the Service port and container port. The container port must be the same as the one that is exposed in the backend pod. Annot at ions: Add one or more annotations to the Service to configure SLB parameters. For example, set the name to `service.beta.kubernetes.io` and the value to `20` . This means that the maximum bandwidth of the Service is 20 Mbit/s. For more information, see Access services by using SLB. Label: Add one or more labels to the Service. The labels are used to identify the Service.
7. Click Creat e. After the nginx-svc Service is created, it appears on the Services page.
8. On the Services page, you can view basic information about the Service. You can also access its
external endpoint by using a browser.

#### 6.7.5 View a Service

You can view details about a Service in the Container Service console. Context Each pod in Kubernetes clusters has its own IP address. However, pods are frequently created and deleted. Therefore, it is not practical to directly expose pods to external access. Services decouple the frontend from the backend, which provides a loosely-coupled microservice architecture. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane, choose Services and Ingresses > Services.
5. On the Services page, select the namespace, find the Service that you want to view, and then click
Det ails in the Actions column. On the details page, you can view detailed information about the Service.

#### 6.7.6 Update a Service

You can update a Service through the Container Service console. This topic describes how to update a Service. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Services.
5. On the Services page, select the namespace, find the Service that you want to update, and then
click Updat e in the Actions column.
6. In the Updat e Service dialog box, modify the configurations and click Updat e.
7. In the Service list, find the Service that you updated and click Det ails in the Actions column to view
configuration changes. In this example, the labels of the Service are modified.

#### 6.7.7 Delete a Service

This topic describes how to delete a Service. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. A Service is created. For more information, see Create Servcies. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Services.
5. On the Services page, select the namespace, find the Service that you want to delete, and then
click Delet e in the Actions column.
6. In the message that appears, click Conf irm.

#### 6.7.8 Use a trigger to redeploy an application

You can create a trigger and use it to redeploy an application. This topic describes how to use a trigger. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. An application is created. Then, a trigger is created for the application and the application is used to test the trigger. In this example, an NGINX application is created. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Manage in the Act ions
column of the cluster.
4. In the left-side navigation pane, click Deployments. On the Deployment s page, find the NGINX
application and click Det ails in the Actions column.
5. On the details page of the application, click the T riggers tab. Then, click Creat e T rigger.
6. In the dialog box that appears, set Action to Redeploy and click Conf irm.
Not e You can create triggers only to redeploy applications. After the trigger is created, the webhook URL of the trigger appears in the Trigger Link Address column on the nginx - deployment page.
7. Copy the webhook URL, enter it into the address bar of your browser, and press Enter. A message
that indicates specific information such as the request ID appears.
8. Go to the nginx - deployment page. A new pod appears on the Pods tab.
After the new pod is deployed, the original pod is automatically deleted. What's next You can run triggers by sending GET or POST requests from an external system. For example, you can use the curl command-line tool to run triggers. To run the redeploy trigger, run the following command:

```bash
 curl https://cs.console.aliyun.com/hook/trigger?token=xxxxxxx
```

#### 6.7.9 View pods

You can view pods in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Pods.
5. In the left-side navigation pane, choose Applicat ions > Pods. The Pods page appears.
6. On the Pods page, select the namespace, find the pod that you want to view, and then click View
Det ails in the Actions column. Not e You can update or delete pods on the Pods page. We recommend that you use Deployments to manage pods if the pods are created by Deployments. On the details page of the pod, you can view detailed information about the pod.

#### 6.7.10 Manage pods

Pods are the smallest deployable units in Kubernetes. A pod runs an instance of an independent application in Kubernetes. Each pod contains one or more containers that are tightly coupled. You can modify pods, view pods, and manually scale the number of pods for an application in the Container Service console. View pods View pod det ails
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click the name or click Det ails
in the Act ions column.
4. In the left-side navigation pane of the details page, choose Workloads > Pods.
5. Find the pod that you want to view and click View Det ails in the Actions column.
You can view details of pods by using one of the following methods: Method 1: In the left-side navigation pane of the details page, choose Workloads > Deployment s. Find the application that you want to manage and click the name of the application. On the Pods tab, click the name of the pod to view details. Method 2: In the left-side navigation pane of the details page, choose Services and Ingresses
> Services. Click the name of the Service that you want to manage. On the page that appears,

find and click the name of the application that you want to manage. On the Pods tab, click the name of the pod to view details. Not e On the Pods page, you can modify and delete pods. For pods that are created by using a Deployment, we recommend that you use the Deployment to manage the pods. View pod log You can view a pod log by using the following methods: Navigate to the Pods tab, find the pod that you want to manage, and then click Logs on the right side to view the log data. Modify pod configurations
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click the name or click Det ails
in the Act ions column.
4. In the left-side navigation pane of the details page, choose Workloads > Pods.
5. On the Pods page, find the pod that you want to manage and click Edit in the Actions column.
6. In the dialog box that appears, modify the configuration of the pod and click Updat e.
Manually scale the number of pods for an application After an application is created, you can scale in or out the pods that are provisioned for the application.
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click the name or click Det ails
in the Act ions column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. Select the namespace where the Deployment is deployed, find the Deployment, and then click
Scale in the Act ions column.
6. In the dialog box that appears, set Desired Number of Pods to 4 and click OK.
Not e By default, the resources created by a Deployment are updated based on the rollingUpdate strategy. This ensures that a minimum number of pods are running during the update. You can specify the minimum number of pods that must run in Pod Template of the YAML file.

#### 6.7.11 Schedule pods to specific nodes

You can add labels to nodes and schedule pods to the nodes with specified labels. This topic describes how to schedule a pod to a node with specified labels. You can add labels to nodes and then configure `nodeSelector` to schedule pods to nodes with specified labels. For more information about how nodeSelector works, see nodeselector. To meet business requirements, you may want to deploy a controller service on a master node, or deploy services on nodes that use standard SSDs. You can use the following method to schedule pods to nodes with specified labels. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Step 1: Add a label to a node
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Nodes.
5. On the Nodes page, click Manage Labels and T aint s in the upper-right corner.
6. Select one or more nodes and then click Add Label. In this example, a worker node is selected.
7. In the dialog box that appears, enter the name and value of the label and click OK.
On the Labels tab, you can find the `group:worker` label next to the selected node. You can also run the following command to add a label to a node: `kubectl label nodes <node-name>`

```xml
<label-key>=<label-value> .
```

Step 2: Schedule a pod to the node
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom T emplat e in the upper-
right corner.
6. On the Creat e page, select a template from the Sample Template drop-down list. In this example,
a custom template is selected. Copy the following content to the custom template and click Creat e. The following template is used as an example:

```
 apiVersion: v1
 kind: Pod
 metadata:
   labels:
     name: hello-pod
   name: hello-pod
 spec:
   containers:
     - image: nginx
       imagePullPolicy: IfNotPresent
       name: hello-pod
       ports:
         - containerPort: 8080
           protocol: TCP
       resources: {}
       securityContext:
         capabilities: {}
         privileged: false
       terminationMessagePath: /dev/termination-log
   dnsPolicy: ClusterFirst
   restartPolicy: Always
   nodeSelector:
     group: worker                           ## This value must be the same as the node
label that is added in Step 1.
 status: {}
```

#### 6.7.12 Simplify application deployment by using Helm

Helm This topic introduces the basic terms and components of Helm and describes how to use Helm to deploy the sample applications WordPress and Spark in a Kubernetes cluster. Prerequisites A Kubernetes cluster is created in the Container Service console. For more information, see Create a Kubernetes cluster. Tiller is automatically deployed to the cluster when the Kubernetes cluster is created. The Helm CLI is automatically installed on each master node. An Alibaba Cloud chart repository is added to Helm. A Kubernetes version that supports Helm is used. Only Kubernetes 1.8.4 and later support Helm. If the Kubernetes version of your cluster is 1.8.1, you can upgrade the cluster on the Clusters page of the Container Service console. Context Application management is the most challenging task in Kubernetes. The Helm project provides a unified method to package software and manage software versions. You can use Helm to simplify application distribution and deployment. App Catalog is integrated with Helm in the Container Service console and provides extended features based on Helm. App Catalog also supports Alibaba Cloud chart repositories to help you accelerate application deployments. You can deploy applications in the Container Service console or by using the Helm CLI. This topic introduces the basic terms and components of Helm and describes how to use Helm to deploy the sample applications WordPress and Spark in a Kubernetes cluster. Basic terms Helm is an open source project initiated by Deis. Helm can be used to simplify the deployment and management of Kubernetes applications. Helm serves as a package manager for Kubernetes and allows you to find, share, and use applications built by Kubernetes. Before you use Helm, you must familiarize yourself with the following basic terms: Chart: a packaging format used by Helm. Each chart contains the images, dependencies, and resource definitions that are required to run an application. A chart may contain service definitions in a Kubernetes cluster. A Helm chart is similar to a Homebrew formula, an Advanced Package Tool (APT) dpkg, or a Yum rpm. Release: an instance of a chart that runs in a Kubernetes cluster. A chart can be installed multiple times into a Kubernetes cluster. After a chart is installed, a new release is created. For example, you can install a MySQL chart. If you want to run two databases in your cluster, you can install the MySQL chart twice. Each time a chart is installed, a release is created with a different name. Repository: the storage of charts. Charts are published and stored in repositories. Helm components Helm uses a client-server architecture and consists of the following components: The Helm CLI is the Helm client that runs on your on-premises machine or on the master nodes of a Kubernetes cluster. Tiller is the server-side component and runs in a Kubernetes cluster. Tiller manages the lifecycles of Kubernetes applications. A repository is used to store charts. The Helm client can access the index file and packaged charts in a chart repository over HTTP. Deploy an application in the Container Service console
2. In the left-side navigation pane, choose Market place > App Cat alog.
3. On the App Catalog page, find and click the WordPress chart to go to the details page of the
chart.
4. Click the Paramet ers tab and modify the configurations.
In this example, a dynamically provisioned disk volume is associated with a persistent volume claim (PVC). For more information, see Use Apsara Stack disks. Not e You must first provision a disk as a persistent volume (PV). The capacity of the PV cannot be less than the capacity specified in the PVC.
5. In the Deploy section, select the cluster in which you want to deploy the application and click
Creat e. After the application is deployed, you are redirected to the release page of the application.
6. In the left-side navigation pane, click Clust ers.
7. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
8. In the left-side navigation pane of the details page, choose Services and Ingresses > Services.
On the Services page, select the namespace, find the Service that is created for the application, and then check its HTTP and HTTPS external endpoints.
9. Click one of the endpoints to go to the WordPress website where you can publish blog posts.
Deploy an application by using the Helm CLI After the Helm CLI is automatically installed on the master nodes of the Kubernetes cluster and the required chart repository is added to Helm, you can log on to the master nodes by using SSH. Then, you can deploy applications by using the Helm CLI. For more information, see Connect to a master node through SSH. You can also install and configure the Helm CLI and kubectl on your on-premises machine. In this example, the Helm CLI and kubectl are installed and configured on your on-premises machine, and then an Apache Spark-based WordPress application is deployed.
1. Install and configure the Helm CLI and kubectl.
i. Install and configure kubectl on your on-premises machine. For more information, see Connect to a Kubernetes cluster through kubectl. To view the details of a Kubernetes cluster, run the `kubectl cluster-info` command. ii. Install Helm on your on-premises machine. For more information, see Install Helm.
2. Deploy the WordPress application.
In the following example, a WordPress blog website is deployed by using Helm. i. Run the following command:

```
helm install --name wordpress-test stable/wordpress
```

Not e Container Service allows you to mount disks as dynamically provisioned volumes. Before you deploy the application, you must create a disk volume. The following output is returned:

```
NAME: wordpress-testLAST DEPLOYED: Mon Nov 20 19:01:55 2017NAMESPACE: defaultSTATUS : DEPLOYED...
```

ii. Run the following command to query the release and Service created for the WordPress application:

```
helm listkubectl get svc
```

iii. Run the following command to view the pods provisioned for the WordPress application. You may need to wait until the pods change to the Running state.

```bash
kubectl get pod
```

iv. Run the following command to obtain the endpoint of the WordPress application:

```
echo http://$(kubectl get svc wordpress-test-wordpress -o jsonpath='{.status.loadBa lancer.ingress[0].ip}')
```

You can enter the preceding URL into the address bar of your browser to access the WordPress application. You can also run the following command based on the chart description to obtain the username and password of the administrator account for the WordPress application:

```
echo Username: userecho Password: $(kubectl get secret --namespace default wordpres s-test-wordpress -o jsonpath="{.data.wordpress-password}" | base64 --decode)
```

v. To delete the WordPress application, run the following command:

```
helm delete --purge wordpress-test
```

Use a third-party chart repository You can use the default Alibaba Cloud chart repository. If a third-party chart repository is accessible from your cluster, you can also use the third-party chart repository. Run the following command to add a third-party chart repository to Helm:

```
helm repo add Repository name Repository URLhelm repo update
```

For more information about Helm commands, see Helm documentation. References Helm contributes to the development of Kubernetes. A growing number of software suppliers, such as Bitnami, have provided high-quality charts. For more information about available charts, visit

```
 https://kubeapps.com/ .
```

### 6.8 SLB and Ingress

#### 6.8.1 Overview

Container Service allows you to flexibly manage load balancing and customize load balancing policies for Kubernetes clusters. Kubernetes clusters provide you with a variety of methods to access containerized applications. They also allow you to use SLB or Ingress to access internal services and implement load balancing.

#### 6.8.2 Use SLB to access Services

You can access a Service through Server Load Balancer (SLB). Use the CLI
1. Create an NGINX application by using the command-line interface (CLI).

```
root@master # kubectl run nginx --image=registry.aliyuncs.com/acs/netdia:latest
       root@master # kubectl get po
       NAME                                   READY     STATUS    RESTARTS   AGE
       nginx-2721357637-dvwq3                 1/1       Running   1          6s
```

2. Create a Service for the NGINX application and set `type=LoadBalancer` to expose the NGINX
Service to the Internet through an SLB instance.

```
root@master # kubectl expose deployment nginx --port=80 --target-port=80 --type=LoadBal ancer
       root@master # kubectl get svc
       NAME                  CLUSTER-IP      EXTERNAL-IP      PORT(S)
AGE
       nginx                 172.19.XX.XX    101.37.XX.XX     80:31891/TCP
```

`4s`
3. Copy `http://101.37.XX.XX` into the address bar of your browser and press Enter to access the
NGINX Service. SLB parameters SLB provides a variety of parameters that you can use to configure features and services such as health check, billing method, and SLB instance type. For more information, see . Annotations You can add annotations to use the load balancing features provided by SLB. Use an exist ing int ernal-f acing SLB inst ance You need to add two annotations. You must replace "yourloadbalancer-id" with your SLB instance ID.

```
apiVersion: v1 kind: Service metadata:
  annotations:
    service.beta.kubernetes.io/alicloud-loadbalancer-address-type: intranet
    service.beta.kubernetes.io/alicloud-loadbalancer-id: your-loadbalancer-id
  labels:
    run: nginx
  name: nginx
  namespace: default
spec:
  ports:
  - name: web
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    run: nginx
  sessionAffinity: None
  type: LoadBalancer
```

Save the preceding code as an slb.svc file and run the following command: `kubectl apply -f`

```
slb.svc .
```

Creat e an HT T PS-based Service of t he Loadbalancer t ype You must first create a certificate in the SLB console. Then, you can use the certificate ID (cert-id) and the following template to create a LoadBalancer Service and an HTTPS-based SLB instance.

```
apiVersion: v1 kind: Service metadata:
  annotations:
    service.beta.kubernetes.io/alicloud-loadbalancer-cert-id: your-cert-id
    service.beta.kubernetes.io/alicloud-loadbalancer-protocol-port: "https:443"
  labels:
    run: nginx
  name: nginx
  namespace: default
spec:
  ports:
  - name: web
    port: 443
    protocol: TCP
    targetPort: 443
  selector:
    run: nginx
  sessionAffinity: None
  type: LoadBalancer
```

Not e Annotations are case sensitive. SLB parameters

| Annotation | Description | Default value |
|---|---|---|
| service.beta.kubernetes.io/aliclou d-loadbalancer-protocol-port | The listening port. Separate multiple ports with commas (,). Example: https:443,http:80. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-address-type | The type of the SLB instance. Valid values: internet and intranet. | internet |
| service.beta.kubernetes.io/aliclou d-loadbalancer-slb-network-type | The network type of the SLB instance. Valid values: classic and vpc. | classic |
| service.beta.kubernetes.io/aliclou d-loadbalancer-charge-type | The billing method of the SLB instance. Valid values: paybytraffic and paybybandwidth. | paybybandwidth |
| service.beta.kubernetes.io/aliclou d-loadbalancer-id | The ID of the SLB instance. You can set the loadbalancer-id parameter to specify an existing SLB instance and its existing listeners will be overwritten. The SLB instance will not be deleted if the Service is deleted. | N/A |

| Annotation | Description | Default value |
|---|---|---|
| service.beta.kubernetes.io/aliclou d-loadbalancer-backend-label | The labels that specify the nodes to be added as backend servers of the SLB instance. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-region | The region where the SLB instance is deployed. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-bandwidth | The bandwidth of the SLB instance. | 50 |
| service.beta.kubernetes.io/aliclou d-loadbalancer-cert-id | The certificate ID. You must upload the certificate first. | "" |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check-flag | Valid values: on and off. | Default value: off. If TCP is used, do not modify this parameter. The health check feature is enabled for TCP listeners by default and cannot be disabled. |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- type | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check-uri | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- connect-port | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-healthy- threshold | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-unhealthy- threshold | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- interval | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- connect-timeout | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- timeout | For more information, see CreateLoadBalancerTCPListener in the SLB Developers Guide. | N/A |

#### 6.8.3 Configure Ingress monitoring

You can enable the virtual host traffic status (VTS) dashboard to view Ingress monitoring data. Enable the VTS dashboard by using the CLI
1. Add the following configuration item to the Ingress ConfigMap: `enable-vts-status: "true"` .

```
root@master # kubectl edit configmap nginx-configuration -n kube-system
      configmap "nginx-configuration" edited
```

The following template shows the modified Ingress ConfigMap:

```json
apiVersion: v1 data:
  enable-vts-status: "true"# Enables the VTS dashboard.
  proxy-body-size: 20m
kind: ConfigMap metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"proxy-body-size":"20m"},"kind":"ConfigMap","metadata"
:{"annotations":{},"labels":{"app":"ingress-nginx"},"name":"nginx-configuration","names pace":"kube-system"}}
  creationTimestamp: 2018-03-20T07:10:18Z
  labels:
    app: ingress-nginx
  name: nginx-configuration
  namespace: kube-system
  selfLink: /api/v1/namespaces/kube-system/configmaps/nginx-configuration
```

2. Verify that the VTS dashboard is enabled for the NGINX Ingress controller.

```
root@master # kubectl get pods --selector=app=ingress-nginx -n kube-system NAME READY STATUS RESTARTS AGE nginx-ingress-controller-79877595c8-78gq8 1/1 Running 0 1h root@master # kubectl exec -it nginx-ingress-controller-79877595c8-78gq8 -n kube-system -- cat /etc/nginx/nginx.conf | grep vhost_traffic_status_display
         vhost_traffic_status_display;
         vhost_traffic_status_display_format html;
```

3. Access the VTS dashboard from an on-premises machine.
Not e By default, the VTS port is not exposed due to security concerns. In the following example, port forwarding is used to access the VTS dashboard.

```
root@master # kubectl port-forward nginx-ingress-controller-79877595c8-78gq8 -n kube-sy stem 18080 Forwarding from 127.0.0.1:18080 -> 18080 Handling connection for 18080
```

4. Visit `http://localhost:18080/nginx_status` to access the VTS dashboard.

#### 6.8.4 Ingress support

Kubernetes clusters support Ingress rules. You can define Ingress rules based on your needs to implement load balancing. In Kubernetes clusters, an Ingress is a collection of routing rules that authorize external access to cluster Services. You can use an Ingress to enable Layer-7 load balancing. You can configure an Ingress to provide Kubernetes Services with externally reachable URLs, SLB instances, SSL connections, and name-based virtual hosting. Prerequisites To test a complex routing scenario, an NGINX application that consists of multiple Services is created in this example. You need to create a Deployment and multiple Services for the NGINX application in advance. In practice, replace Service names with the actual values.

```bash
kubectl run nginx --image=registry.cn-hangzhou.aliyuncs.com/acs/netdia:latest kubectl expose deploy nginx --name=http-svc --port=80 --target-port=80 kubectl expose deploy nginx --name=http-svc1 --port=80 --target-port=80 kubectl expose deploy nginx --name=http-svc2 --port=80 --target-port80 kubectl expose deploy nginx --name=http-svc3 --port=80 --target-port=80
```

Create a simple Ingress Run the following commands to create a simple Ingress that redirects traffic to the /svc path to a httpsvc Service. `nginx.ingress.kubernetes.io/rewrite-target: /` redirects traffic destined for the /svc path to the / path that can be recognized by the backend application.

```bash
cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: simple
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /svc
        backend:
          serviceName: http-svc
          servicePort: 80
EOF kubectl get ing NAME HOSTS ADDRESS PORTS AGE simple * 101.37.19*.*** 80 11s
```

You can visit `http://101.37.19*.***/svc` to access the NGINX application. Create a simple fanout Ingress that uses multiple domain names You can create a simple fanout Ingress to route traffic from an external IP address to multiple Services with different domain names. The following example shows the configuration of a simple fanout Ingress:

```bash
cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: simple-fanout
spec:
  rules:
  - host: foo.bar.com
    http:
      paths:
      - path: /foo
        backend:
          serviceName: http-svc1
          servicePort: 80
      - path: /bar
        backend:
          serviceName: http-svc2
          servicePort: 80
  - host: foo.example.com
    http:
      paths:
      - path: /film
        backend:
          serviceName: http-svc3
          servicePort: 80
EOF kubectl get ing NAME HOSTS ADDRESS PORTS AGE simple-fanout * 101.37.19*.*** 80 11s
```

| You can visit | http://foo.bar.com/foo |   |
|---|---|---|
| http://foo.bar.com/bar |   |   |
| to access Service |   | http-svc3 |

|   | http-svc1 |
|---|---|
| http-svc2 |   |

| Not e In a production environment, you need to point the domain name to the returned address 101.37.19*.*** . In a test environment, you need to add the following mapping rules to the hosts file. 101.37.19*.*** foo.bar.com 101.37.19*.*** foo.example.com |   |   |
|---|---|---|

Create a simple Ingress that uses the default domain name If you do not have a domain name, you can use the default domain name associated with the Ingress to access the Service. The default domain name is in the following format: `*.[cluster-id].[region-` `id].alicontainer.com` . You can find the default domain name in the basic information of the Kubernetes cluster in the Container Service console. The following example shows the configuration of a simple Ingress that allows external access to the Service through the default domain name:

```bash
cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: shared-dns
spec:
  rules:
  - host: foo.[cluster-id].[region-id].alicontainer.com  ## Replace with the default domain
name of your cluster.
    http:
      paths:
      - path: /
        backend:
          serviceName: http-svc1
          servicePort: 80
  - host: bar.[cluster-id].[region-id].alicontainer.com  ## Replace with the default domain
name of your cluster.
    http:
      paths:
      - path: /
        backend:
          serviceName: http-svc2
          servicePort: 80
EOF kubectl get ing NAME HOSTS ADDRESS PORTS AGE shared-dns foo.[cluster-id].[region-id].alicontainer.com,bar.[cluster-id].[region-id].ali container.com 47.95.16*.*** 80 40m
```

| http://foo.[cluster-id].[region-id].alicontainer.com/ |   | t |
|---|---|---|
| sit | http://bar.[cluster-id].[region-id].alicontainer.com |   |

| http- |   |   |
|---|---|---|
| e | http- |   |

`svc2` . Create an Ingress to secure data transmission Container Service allows you to use multiple types of certificates to reinforce the security of your applications.
1. Prepare your certificate.
If you do not have a certificate, perform the following steps to generate a test certificate: Not e The domain name must be the same as the one specified in your Ingress configuration.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

After you run the preceding command, a certificate file tls.crt and a private key file tls.key are generated. Use the certificate and private key to create a Kubernetes Secret named foo.bar. You need to reference the Secret when you create the Ingress.

```bash
kubectl create secret tls foo.bar --key tls.key --cert tls.crt
```

2. Create an Ingress to secure data transmission.

```bash
cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: tls-fanout
spec:
  tls:
  - hosts:
    - foo.bar.com
    secretName: foo.bar
  rules:
  - host: foo.bar.com
    http:
      paths:
      - path: /foo
        backend:
          serviceName: http-svc1
          servicePort: 80
      - path: /bar
        backend:
          serviceName: http-svc2
          servicePort: 80
EOF kubectl get ing NAME HOSTS ADDRESS PORTS AGE tls-fanout * 101.37.19*.*** 80 11s
```

3. You need to configure the `hosts` file or set a domain to access the tls Ingress, as described in
Simple f anout based on domains.

| http://foo.bar.com/foo |   | t |
|---|---|---|
| access Service | http-svc2 |   |

You can visit `http://foo.bar.com/foo` to access Service `http-svc1` and visit `http://foo.bar` You can also access the HTTPS Service by using HTTP. By default, the Ingress redirects HTTP traffic to the HTTPS address. Traffic to `http://foo.bar.com/foo` is automatically redirected to `https`

```
://foo.bar.com/foo .
```

Create an Ingress
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Ingresses.
5. On the Ingresses page, select a namespace and click Create Resources in YAML to create an
Ingress.
6. On the Creat e page, select Cust om from the Sample T emplat e drop-down list, copy the
following content to the template, and then click Creat e.

```
apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: simple
spec:
  rules:
  - http:
      paths:
      - path: /svc
        backend:
          serviceName: http-svc
          servicePort: 80
```

This way, an Ingress that routes Layer-7 traffic for Service `http-svc` is created.

#### 6.8.5 Ingress configurations

Container Service provides Ingress controller components. Integrated with Apsara Server Load Balancer, these components provide Kubernetes clusters with flexible and reliable Ingress service. An Ingress orchestration template is provided below. When you configure an Ingress through the console, you need to configure annotations and may need to create dependencies. For more information, see Create an ingress through the console, Ingress support, and Kubernetes Ingress. You can also create ConfigMaps to configure Ingresses. For more information, see https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/.

```
apiVersion: extensions/v1beta1 kind: Ingress metadata:
  annotations:
    nginx.ingress.kubernetes.io/service-match: 'new-nginx: header("foo", /^bar$/)' #Canary
release rule. In this example, the request header is used.
    Nginx. ingress. kubernetes. IO/service-weight: 'New-nginx: 50, old-nginx: 50' #The rout
e weight.
  creationTimestamp: null
  generation: 1
  name: nginx-ingress
  selfLink: /apis/extensions/v1beta1/namespaces/default/ingresses/nginx-ingress
spec:
  rules: ##The Ingress rule.
  - host: foo.bar.com
    http:
      paths:
      - backend:
          serviceName: new-nginx
          servicePort: 80
        path: /
      - backend:
          serviceName: old-nginx
          servicePort: 80
        path: /
tls: ## Enable TLS for secure routing.
  - hosts:
    - *.xxxxxx.cn-hangzhou.alicontainer.com
    - foo.bar.com
    secretName: nginx-ingress-secret     ##The Secret name.
status:
  loadBalancer: {}
```

Annotations For each Ingress, you can configure its annotations, Ingress controller, and rules, such as the route weight, canary release rule, and rewrite rules. For more information about annotations, see https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/. For example, the following rewrite annotation, `nginx.ingress.kubernetes.io/rewrite-target: /` , indicates that /path is redirected to the root path /, which can be recognized by the backend service. Rules Ingress rules are used to manage external access to the services in the cluster and can be HTTP or HTTPS rules. You can configure the following items in rules: domain name (virtual hostname), URL path, service name, and port. For each rule, you need to set the following parameters: Domain: The test domain or virtual hostname of your service, such as `foo.bar.com` . Path: The URL path of your service. Each path is associated with a backend service. Server Load Balancer only forwards traffic to the backend if the incoming request matches the domain and path. Service: Specify the service in the form of `service:port` . You also need to specify a route weight for each service. The Ingress routes traffic to the matching service based on the route weight. Name: The name of the backend service. Port: The port of the service. Weight: The route weight of the service in the service group. Not e a. The weight is a percentage value. For example, you can set two services to the same weight of 50%. b. A service group includes services that have the same domain and path defined in the Ingress configuration. If no weight is set for a service, the default value, 100, is used. Canary release Container Service supports multiple traffic splitting approaches to suit scenarios such as canary release and A/B testing. Not e Currently, only Ingress controllers of 0.12.0-5 and later versions support traffic splitting.
1. Traffic splitting based on request header
2. Traffic splitting based on cookie
3. Traffic splitting based on query parameter
After canary release is configured, only requests that match certain rules are routed to the corresponding service. If the weight of the corresponding service is lower than 100%, requests that match certain rules are routed to one of the services in the service group based on the weight. TLS You can use a Secret that contains a TLS private key and certificate to encrypt the Ingress. This ensures secure routing. The TLS Secret must contain a certificate named tls.crt and a private key named tls.key. For more information about how TLS works, see TLS. For how to create a Secret, see Configure a secure Ingress. Labels You can add labels to the Ingress.

#### 6.8.6 Create an Ingress in the console

The Container Service console is integrated with the Ingress service. You can create an Ingress in the console and manage inbound traffic that is forwarded to different Services to meet your business requirements. Prerequisites A Kubernetes cluster is created and an Ingress controller runs as normal in the cluster. For more information, see Create a Kubernetes cluster. You are connected to a master node by using kubectl. For more information, see Connect to a Kubernetes cluster through kubectl. The image address used in this example requires Internet access. You can use the image address of your own cluster to replace it. You can also build and push the image used in this example to a repository and then pull it from the repository when you use it. Step 1: Create a Deployment and a Service
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select a namespace and click Creat e f rom T emplat e in the upper-
right corner.
6. On the Creat e page, select a sample template or customize a template and click Creat e.
In this example, two NGINX applications are created: old-nginx and new-nginx. The following template is used to create the old-nginx application:

```
apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: old-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      run: old-nginx
  template:
    metadata:
      labels:
        run: old-nginx
    spec:
      containers:
      - image: registry.cn-hangzhou.aliyuncs.com/xianlu/old-nginx
        imagePullPolicy: Always
        name: old-nginx
        ports:
        - containerPort: 80
          protocol: TCP
      restartPolicy: Always
--apiVersion: v1 kind: Service metadata:
  name: old-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    run: old-nginx
  sessionAffinity: None
  type: NodePort
```

The following template is used to create the new-nginx application:

```
apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: new-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      run: new-nginx
  template:
    metadata:
      labels:
        run: new-nginx
    spec:
      containers:
      - image: registry.cn-hangzhou.aliyuncs.com/xianlu/new-nginx
        imagePullPolicy: Always
        name: new-nginx
        ports:
        - containerPort: 80
          protocol: TCP
      restartPolicy: Always
--apiVersion: v1 kind: Service metadata:
  name: new-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    run: new-nginx
  sessionAffinity: None
  type: NodePort
```

7. In the left-side navigation pane of the details page, choose Services and Ingresses > Services.
After the Services are created, you can find these Services on the Services page. Step 2: Create an Ingress
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Ingresses.
5. On the Ingresses page, select a namespace and click Creat e in the upper-right corner.
6. In the dialog box that appears, enter a name for the Ingress. In this example, the Ingress is named
nginx-ingress.
7. Configure Ingress rules.
Ingress rules are used to manage external access to Services in the cluster. Ingress rules can be HTTP or HTTPS rules. You can configure the following items in rules: domain name (virtual hostname), URL path, Service name, port, and weight. For more information, see Ingress configurations. In this example, a complex rule is added to configure Services for the default domain name and virtual hostname of the cluster. Traffic is routed based on domain names. Creat e a simple f anout Ingress t hat uses mult iple domain names In this example, a virtual hostname is used as the test domain name for external access. Route weights are specified for two backend Services and canary release settings are configured for one of the Services. In your production environment, you can use a domain name that has obtained an Internet Content Provider (ICP) number for external access. Domain: Enter the test domain name. In this example, the test domain name is `foo.bar.com` . You must add the following domain name mapping to the hosts file:

```
118.178.XX.XX foo.bar.com #The IP address of the Ingress.
```

Services: Set the names, paths, port numbers, and weights of the backend Services that you want to access. Path: Enter the URL of the backend Service. In this example, the root path / is used. Name: In this example, both the old-nginx and new-nginx Services are specified. Port: In this example, port 80 is open. Weight: Set a weight for each backend Service. The weight is a percentage value. The default value is 100. In this example, the weight of each backend Service is 50. This means that the two backend Services have the same weight.
8. Configure Transport Layer Security (TLS). Select EnableT LS to enable TLS and configure a secure
Ingress. For more information, see Configure a secure Ingress. You can use an existing Secret. a. Log on to a master node. Create a file named tls.key and another file named tls.crt.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

b. Create a Secret.

```bash
kubectl create secret tls foo.bar --key tls.key --cert tls.crt
```

c. Run the `kubectl get secret` command and verify that the Secret is created. Then, you can select the newly created Secret foo.bar. You can also use the TLS private key and certificate to create a Secret. a. Log on to a master node, and then create a file named tls.key and another file named tls.crt.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

b. Run the `vim tls.key` and `vim tls.crt` commands to obtain the private key and certificate that are generated. c. Paste the certificate to the Cert field and the private key to the Key field.
9. Configure canary release settings.
Not e Only Ingress controllers of 0.12.0-5 and later versions support traffic splitting. Container Service supports multiple traffic splitting methods. This allows you to select suitable solutions for specific scenarios, such as canary releases and A/B testing: i. Traffic splitting based on request headers. ii. Traffic splitting based on cookies iii. Traffic splitting based on query parameters. After canary release settings are configured, only requests that match the specified rules are routed to the new-nginx Service. If the weight of new-nginx is lower than 100%, requests that match certain rules are routed to this Service based on the weight. In this example, the rule is added to specify a request header that matches the regular expression foo=^bar$ . Only requests with headers that match the regular expression are forwarded to new-nginx. Services: Specify the Services to be accessed. T ype: Select the type of matching rule. Valid values: Header, Cookie, and Query. Name and Mat ch Value: Specify custom request fields. Each field is a key-value pair. Mat ching Rule: Regular expressions and exact matches are supported.
10. Configure annotations.
Click Rewrit e Annot at ion and add an annotation to redirect inbound traffic for the Ingress. For example, `nginx.ingress.kubernetes.io/rewrite-target: /` specifies that /path is redirected to the root path /. The root path can be recognized by the backend Services. Not e In this example, no path is configured for the backend Services. Therefore, you do not need to configure rewrite annotations. Rewrite annotations allow the Ingress to forward traffic through root paths to the backend Services. This avoids the 404 error that is caused by invalid paths. You can also click Add to enter annotation names and values in key-value pairs. For more information about Ingress annotations, visit https://kubernetes.github.io/ingress-nginx/userguide/nginx-configuration/annotations/.
11. Add labels.
Add labels to describe the Ingress.
12. Click Creat e. You are redirected to the Ingresses page.
After the Ingress is created, you can find the nginx-ingress Ingress on the Ingresses page.
13. Click foo.bar.com to view the NGINX welcome page.
Click the domain name that points to new-nginx, the old-nginx Service page appears. By default, when you enter the domain name in the browser, request headers do not match the foo=^bar$ regular expression. Therefore, requests are directed to old-nginx.
14. Log on to a master node by using SSH. Run the following commands to simulate requests with
specific headers and check the results:

```bash
curl -H "Host: foo.bar.com" http://47.107.XX.XX old
 curl -H "Host: foo.bar.com" http://47.107.XX.XX
old
 curl -H "Host: foo.bar.com" http://47.107.XX.XX                     #Similar to a brow
ser request. old
 curl -H "Host: foo.bar.com" -H "foo: bar" http://47.107.XX.XX           #Simulate a re
quest with a specific header. The results are returned based on the weight. new
 curl -H "Host: foo.bar.com" -H "foo: bar" http://47.107.XX.XX
old
 curl -H "Host: foo.bar.com" -H "foo: bar" http://47.107.XX.XX
old
 curl -H "Host: foo.bar.com" -H "foo: bar" http://47.107.XX.XX
new
```

#### 6.8.7 Update an Ingress

You can update Ingresses in the Container Service console. Prerequisites A Kubernetes cluster is created and an Ingress controller is running as normal in the cluster. For more information, see Create a Kubernetes cluster. An Ingress is created. For more information, see Create an ingress through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Ingresses.
5. On the Ingresses page, select the namespace, find the Ingress that you want to update, and then
click Updat e in the Actions column.
6. In the dialog box that appears, modify the parameters and click Updat e. In this example, change

```
foo.bar.com to test.bar.com .
```

On the Ingresses page, you can find the changed Ingress rule.

#### 6.8.8 Delete an Ingress

This topic describes how to delete an Ingress. Prerequisites A Kubernetes cluster is created and an Ingress controller is running as normal in the cluster. For more information about how to create a cluster, see Create a Kubernetes cluster. An Ingress is created. For more information, see Create an ingress through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Services and Ingresses > Ingresses.
5. On the Ingresses page, select the namespace, find the Ingress that you want to delete, and then
click Delet e in the Actions column.
6. In the message that appears, click Conf irm.

### 6.9 Config maps and secrets

#### 6.9.1 Create a ConfigMap

In the Container Service console, you can create a ConfigMap on the ConfigMap page or by using a template. This topic describes how to create a ConfigMap. Create a ConfigMap on the ConfigMap page
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Conf igMaps.
5. On the Conf igMap page, select a namespace and click Creat e.
6. Set the parameters and click OK.
Create a ConfigMap on the ConfigMap page

| Parameter | Description |
|---|---|
| Clust ers | The ID of the cluster that you have selected. |

| Parameter | Description |
|---|---|
| Namespaces | The namespace that you have selected. A ConfigMap is a Kubernetes resource object and must be scoped to a namespace. |
| Conf igMap Name | The name of the ConfigMap. The name can contain lowercase letters, digits, hyphens (-), and periods (.). This parameter is required. Other resource objects must reference the ConfigMap name to obtain the configuration information. |
| Conf igMap | Specify Name and Value, and then click Add to add the key-value pair. You can also click Edit YAML f ile, modify the parameters in the dialog box that appears, and then click OK. |

In this example, two variables named enemies and lives are created. Their values are set to aliens and 3 separately.
7. Click OK. You can find the test-config ConfigMap on the ConfigMap page.
You can also click Browse and upload a configuration file to create a ConfigMap. Create a ConfigMap from a template
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom T emplat e in the upper-
right corner.
6. On the page that appears, set the parameters and click Creat e.
Create a ConfigMap from a template

| Parameter | Description |
|---|---|
| Sample T emplat e | Container Service provides YAML templates of various resource types to help you quickly deploy resource objects. You can select Custom from the drop-down list and configure your ConfigMap based on YAML syntax. You can also select the Re source-ConfigMap template to create a ConfigMap. In the sample template, the ConfigMap is named aliyun-config and contains two variable files: game.properties and ui.propert ies. You can modify the ConfigMap based on your needs. |
| T emplat e | Enter the template content based on YAML syntax. The template can contain multiple resource objects that are separated by --- . |
| Add Deployment | This feature allows you to quickly define a YAML template. You can click Use Exist ing T emplat e to import an existing template. |

After the deployment is completed, you can find the ConfigMap named aliyun-config on the ConfigMap page.

#### 6.9.2 Use a ConfigMap in a pod

This topic describes how to use a ConfigMap in a pod. You can use a ConfigMap in a pod in the following scenarios: Use a ConfigMap to define environment variables for a pod. Use a ConfigMap to set command line parameters. Use a ConfigMap in a volume. For more information, see Configure a pod to use a ConfigMap. Limits To use a ConfigMap in a pod, make sure that the ConfigMap and the pod are in the same cluster and namespace. Create a ConfigMap In this example, a ConfigMap named special_config is created. This ConfigMap consists of two key-value pairs: `SPECIAL_LEVEL: very` and `SPECIAL_TYPE: charm` . You can use the following YAML template to create the ConfigMap:

```
apiVersion: v1 kind: ConfigMap metadata:
  name: special-config
  namespace: default
data:
  SPECIAL_LEVEL: very
  SPECIAL_TYPE: charm
```

You can also log on to the Container Service console and choose Conf igurat ion > Conf igMaps in the left-side navigation pane. You can then click Creat e to create the ConfigMap. Use a ConfigMap to define one or multiple environment variables for a pod Use a key-value pair of a Conf igMap t o def ine one environment variable You can log on to the Container Service console. In the left-side navigation pane, click Clust ers. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. In the left-side navigation pane of the details page, choose Workloads > Deployment s. Click Creat e f rom T emplat e, select a pod template from the Sample Template drop-down list, and then start the deployment. You can use the following sample template to create a pod and defines environment variables in the pod. valueFrom is used to reference the value of SPECIAL_LEVEL to define an environment variable.

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-1
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:                             ##valueFrom is used to reference the value
of the ConfigMap to define an environment variable.
            configMapKeyRef:
              name: special-config               ##The name of the referenced ConfigMap.
              key: SPECIAL_LEVEL                 ##The key of the referenced key-value pair
```

`.`

```
  restartPolicy: Never
```

To use the values of multiple ConfigMaps to define multiple environment variables, add multiple env parameters to the pod configuration file. Use all t he key-value pairs of a Conf igMap t o def ine mult iple environment variables To define the key-value pairs of a ConfigMap as pod environment variables, you can use the envFrom parameter. The keys in a ConfigMap are used as the names of the environment variables. The following sample template is used to create a pod:

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-2
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      envFrom:                ##Reference all the key-value pairs of the sepcial-config Con
figMap.
      - configMapRef:
        name: special-config
  restartPolicy: Never
```

Use a ConfigMap to set command line parameters You can use ConfigMaps to define the commands or parameter values for a container by using the environment variable replacement syntax $(VAR_NAME). The following template is used as an example:

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-3
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "echo $(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: special-config
              key: SPECIAL_LEVEL
        - name: SPECIAL_TYPE_KEY
          valueFrom:
            configMapKeyRef:
              name: special-config
              key: SPECIAL_TYPE
  restartPolicy: Never
```

After you run the pod, the following output is returned:

```
very charm
```

Use a ConfigMap in a volume You can use a ConfigMap to define volumes. The following sample template specifies a ConfigMap name under volumes. This stores the key-value pairs of the ConfigMap to the path that you specified in the mountPath field. In this example, the path is /etc/config. This generates configuration files that are named after the keys of the ConfigMap. The corresponding values of the ConfigMap are stored in these files.

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-4
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "ls /etc/config/" ]   ##List the files under the director
```

`y.`

```
      volumeMounts:
        - name: config-volume
          mountPath: /etc/config
   volumes:
     - name: config-volume
       configMap:
         name: special-config
  restartPolicy: Never
```

After you run the pod, the following output is returned:

```
SPECIAL_TYPE SPECIAL_LEVEL
```

#### 6.9.3 Update a ConfigMap

You can use multiple methods to update a ConfigMap. Considerations If you update a ConfigMap, the applications that use the ConfigMap are affected. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Conf igMaps.
5. On the Conf igMap page, select the namespace, find the ConfigMap that you want to update, and
then click Edit in the Actions column.
6. In the dialog box that appears, modify the configurations and click OK.

#### 6.9.4 Delete a ConfigMap

You can use multiple methods to delete a ConfigMap. Considerations If you delete a ConfigMap, the applications that use this ConfigMap are affected. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Conf igMaps.
5. On the Conf igMap page, select the namespace, find the ConfigMap that you want to delete, and
then click Delet e in the Act ions column.
6. In the message that appears, click OK.

#### 6.9.5 Create a Secret

You can create Secrets for applications in the Container Service console. Prerequisites A Kubernetes cluster is created. Context We recommend that you use Secrets to store sensitive information in Kubernetes clusters, such as passwords and certificates. Secrets are classified into the following types: Service account: A service account is automatically created by Kubernetes and automatically mounted to the /run/secrets/kubernetes.io/serviceaccount directory of a pod. The service account provides an identity for the pod to interact with the API server. Opaque: This type of secret is encoded in Base64 and used to store sensitive information, such as passwords and certificates. By default, you can create only Opaque Secrets in the Container Service console. Opaque Secrets store map type data. Therefore, values must be encoded in Base64. You can create Secrets in the Container Service console with a few clicks. Plaintext is automatically encoded in Base64. You can also create Secrets by using the CLI. For more information, see Kubernetes Secrets. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Secret s.
5. On the Secret s page, select the namespace and click Creat e in the upper-right corner.
6. Configure the Secret and click OK.
Not e To enter Secret data in plaintext, select Encode Dat a Values Using Base64.

| Parameter | Description |
|---|---|
| Name | Enter a name for the Secret. The name must be 1 to 253 characters in length, and can contain only lowercase letters, digits, hyphens (-), and periods (.). |
| Namespace | Select the namespace of the Secret. |
| Type | You can select Opaque, Private Repository Logon Secret, or TLS Certificate. |
| Opaque | If you set Type to Opaque, configure the following parameters: (Optional)To enter Secret data in plaintext, select Encode Dat a Values Using Base64. Configure the Secret in key-value pairs. Click + Add. Enter the keys and values for the Secret in the Name and Value fields. |

| Parameter | Description |
|---|---|
| Private Repository Logon Secret | If you set Type to Private Repository Logon Secret, configure the following parameters: Docker Registry URL: Enter the address of the Docker registry where your Secret is stored. Username: Enter the username that is used to log on to the Docker registry. Password: Enter the password that is used to log on to the Docker registry. |
| TLS Certificate | If you set Type to TLS Certificate, configure the following parameters: Cert: Enter a TLS certificate. Key: Enter the key for the TLS certificate. |

You can view the newly created Secret on the Secrets page.

#### 6.9.6 Modify a Secret

This topic describes how to modify a Secret in the Container Service console. Prerequisites A Kubernetes cluster is created. A Secret is created. For more information, see Create a secret. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Secret s.
5. On the Secrets page, select the namespace, find the Secret that you want to modify, and then
click Edit in the Actions column.
6. In the dialog box that appears, modify the Secret and click OK.

#### 6.9.7 Delete a Secret

This topic describes how to delete a Secret in the Container Service console. Prerequisites A Kubernetes cluster is created. A Secret is created. For more information, see Create a secret. Context Do not delete Secrets that are generated when the cluster is created. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Conf igurat ions > Secret s.
5. On the Secret s page, select the namespace, find the Secret that you want to delete, and then
click Delet e in the Act ions column.
6. In the message that appears, click OK.

### 6.10 Templates

#### 6.10.1 Create an orchestration template

This topic describes how to use multiple methods to create orchestration templates through the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es and click
Creat e in the upper-right corner.
3. In the dialog box that appears, configure the template, and then click Save. This example
demonstrates how to create a Tomcat application template that contains a deployment and a service. Name: The name of the template. Descript ion: Optional. The description of the template. T emplat e: Enter the template content based on YAML syntax. The template can contain multiple resource objects that are separated by `---` .
4. After the template is created, you are redirected to the T emplat es page by default. You can find
the template on the My T emplat es tab.
5. (Optional)You can also choose Applicat ions > Deployment s in the left-side navigation pane,
and click Creat e f rom T emplat e to go to the Creat e f rom T emplat e page. You can modify a built-in template provided by Container Service and save it as a custom template. i. Select a built-in template and click Save T emplat e. ii. In the dialog box that appears, specify the name, description, and content. Click Save to save the template. Not e You can modify the built-in template based on your needs. iii. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. You can find the newly created template on the My T emplat es tab. What's next You can use the orchestration templates on the My T emplat es tab to quickly create applications.

#### 6.10.2 Update an orchestration template

This topic describes how to edit and update an orchestration template. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Edit in the upper-right corner.
5. In the dialog box that appears, edit the name, description, and template content, and click Save.
6. Go to the T emplat es page. You can view the template that you have updated on the My
T emplat es tab.

#### 6.10.3 Save an orchestration template as a new one

one This topic describes how to save an orchestration template as a new one. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, modify the template and click Save As in the upper-right corner.
5. In the dialog box that appears, enter the template name and click OK.
6. Go to the T emplat es page. The newly saved template is displayed on the My T emplat es tab.

#### 6.10.4 Download an orchestration template

This topic describes how to download an orchestration template. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Download in the upper-right corner to download the template
as a YAML file.

#### 6.10.5 Delete an orchestration template

Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Delet e in the upper-right corner.
5. In the dialog box that appears, click OK.

### 6.11 Auto scaling

#### 6.11.1 Auto scaling of nodes

Container Service provides the auto scaling component to automatically scale the number of nodes. Regular instances and GPU-accelerated instances can be automatically added to or removed from a Container Service cluster to meet your business requirements. This component supports multiple scaling modes, various instance types, and instances that are deployed across zones. This component is applicable to diverse scenarios. How it works The auto scaling model of Kubernetes is different from the traditional scaling model that is based on the resource usage threshold. Developers must understand the differences between the two scaling models before they migrate workloads from traditional data centers or other orchestration systems such as Swarm to Kubernetes. The traditional scaling model is based on resource usage. For example, if a cluster contains three nodes and the CPU utilization or memory usage of the nodes exceeds the scaling threshold, new nodes are added to the cluster. However, you must consider the following issues when you use the traditional scaling model: How do you set a proper scaling threshold and how does the system check whether the threshold is exceeded? In a Kubernetes cluster, the resource usage of hot nodes is higher than that of other nodes. If you specify the average resource usage as the scaling threshold, scaling activities may not be promptly triggered. If you specify the lowest node resource usage as the scaling threshold, the newly added nodes may not be used. This causes a waste of resources. How are the loads balanced after new nodes are added? In Kubernetes, pods are the smallest deployable units for applications. Pods are deployed on different nodes in a Kubernetes cluster. When auto scaling is triggered for a cluster or a node in the cluster, pods with high resource usage are not replicated and the resource limits of these pods are not changed. As a result, the loads cannot be balanced to newly added nodes. How do you determine whether scaling activities must be triggered and how are scaling activities performed? If scale-in activities are triggered based on resource usage, pods that request large amounts of resources but have low resource usage may be evicted. If the number of these pods is large within a Kubernetes cluster, resources may be exhausted and some pods may fail to be scheduled. How does the auto scaling model of Kubernetes fix these issues? Kubernetes provides a two-layer scaling model that decouples pod scheduling from resource scaling. In simple terms, pods are scaled based on resource usage. When pods enter the Pending state due to insufficient resources, a scale-out activity is triggered. After new nodes are added to the cluster, the pending pods are automatically scheduled to the newly added nodes. This way, the loads of the application are balanced. The following section describes the auto scaling model of Kubernetes in detail: How is a scale-out activity triggered? The cluster-autoscaler component scans for pending pods and then triggers scaling activities. When pods enter the Pending state due to insufficient resources, cluster-autoscaler simulates pod scheduling to decide the scaling group that can provide new nodes to accept the pending pods. If a scaling group meets the requirement, nodes from this scaling group are added to the cluster. In simple terms, a scaling group is treated as a node during the simulation. The instance type of the scaling group specifies the CPU, memory, and GPU resources of the node. The labels and taints of the scaling group are also applied to the node. The node is used to simulate the scheduling of the pending pods. If the pending pods can be scheduled to the node, cluster-autoscaler calculates the number of nodes that need to be added from the scaling group. How is a scale-in activity triggered? Only nodes that are added by scaling activities can be removed by cluster-autoscaler. This component cannot manage static nodes. Each node is separately evaluated to determine whether the node needs to be removed. If the resource usage of a node drops below the scale-in threshold, a scale-in activity is triggered for the node. In this case, cluster-autoscaler simulates the eviction of all workloads on the node to determine whether the node can be completely drained. clusterautoscaler does not drain the nodes that contain specific pods, such as non-DaemonSet pods in the kube-system namespace and pods that are controlled by PodDisruptionBudgets (PDBs). A node is drained before it is removed. After pods on the node are evicted to other nodes, the node can be removed. How is a scaling group selected from multiple scaling groups that meet the requirements? Different scaling groups are treated as nodes in different specifications. cluster-autoscaler selects a scaling group based on a scoring policy that is similar to a scheduling policy. Nodes are first filtered by the scheduling policy. Among the filtered nodes, the nodes that conform to policies, such as affinity settings, are selected. If no scheduling policy or affinity settings are configured, clusterautoscaler selects a scaling group based on the least-waste policy. The least-waste policy selects the scaling group that has the fewest idle resources after simulation. If a scaling group of CPUaccelerated nodes and a scaling group of GPU-accelerated nodes both meet the requirements, the scaling group of CPU-accelerated nodes is selected by default. How can the success rate of auto scaling be increased? The success rate of auto scaling depends on the following factors: Whether the scheduling policy is met After you configure a scaling group, you must be aware of the pod scheduling policies that the scaling group supports. If you are unaware of the pod scheduling policies, you can simulate a scaling activity by using the node selectors of pending pods and the labels of the scaling group. Whether resources are sufficient After the scaling simulation is complete, a scaling group is selected. However, the scaling activity fails if the specified types of Elastic Compute Service (ECS) instances in the scaling group are out of stock. To increase the success rate of auto scaling, you can select different types of instances in more than one zone. How can auto scaling be accelerated? Method 1: Perform auto scaling in swift mode. After a scaling group experiences a scale-in activity and a scale-out activity, the swift mode is enabled for the scaling group. Method 2: Use custom images that are created from the base image of Alibaba Cloud Linux 2 (formerly known as Aliyun Linux 2). This ensures that the resources of Infrastructure as a Service (IaaS) are delivered 50% faster. Considerations For each account, the default CPU quota for pay-as-you-go instances in each region is 50 vCPUs. You can add at most 48 custom route entries to each route table of a virtual private cloud (VPC). To request a quota increase, submit a ticket. The stock of ECS instances may be insufficient for auto scaling if you specify only one ECS instance type for a scaling group. We recommend that you specify multiple ECS instance types with the same specification for a scaling group. This increases the success rate of auto scaling. In swift mode, when a node is shut down and reclaimed, the node stops running and enters the NotR eady state. When a scale-out activity is triggered, the state of the node changes to Ready. If a node is shut down and reclaimed in swift mode, you are charged only for the disks. This rule does not apply to nodes that use local disks, such as the instance type of ecs.d1ne.2xlarge, for which you are also charged a computing fee. If the stock of nodes is sufficient, nodes can be launched within a short period of time. If elastic IP addresses (EIPs) are associated with pods, we recommend that you do not delete the scaling group or remove ECS instances from the scaling group in the ECS console. Otherwise, these EIPs cannot be automatically released. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clusters page, find the cluster that you want to manage and choose More > Aut o Scaling
in the Act ions column.
4. On the Conf igure Aut o Scaling page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Cluster | The name of the cluster for which you want to enable auto scaling. |
| Scale-in Threshold | For a scaling group that is managed by cluster- autoscaler, set the value to the ratio of the requested resources per node to the total resources per node. If the actual value is lower than the threshold, the node is removed from the cluster. Not e In auto scaling, a scale-out activity is automatically triggered based on node scheduling. Therefore, you need to set only scale-in parameters. |
| GPU Scale-in Threshold | The scale-in threshold for GPU-accelerated instances. If the actual value is lower than the threshold, the node is removed from the cluster. |
| Defer Scale-in For | The amount of time that the cluster must wait before the cluster scales in. The default value is 10 minutes. |
| Cooldown | The cooldown period after a scale-in activity is triggered. No scale-in activity is triggered during the cooldown period. The default value is 10 minutes. |

5. Click Creat e Scaling Group and specify the type of resource for auto scaling based on your
business requirements. Regular instances and GPU-accelerated instances are supported.
6. In the Aut o Scaling Group Conf igurat ion dialog box, set the following parameters.

| Parameter | Description |
|---|---|
| Region | The region where you want to deploy the scaling group. The scaling group and the Kubernetes cluster must be deployed in the same region. You cannot change the region after the scaling group is created. |
| VPC | The scaling group and the Kubernetes cluster must be deployed in the same VPC. |
| VSwitch | The vSwitches of the scaling group. You can specify vSwitches of different zones. The vSwitches allocate pod CIDR blocks to the scaling group. |

7. Configure worker nodes.

| Parameter | Description |
|---|---|
| Instance Type | The instance types in the scaling group. |
| Selected Types | The instance types that you select. You can select at most 10 instance types. |
| System Disk | The system disk of the scaling group. |
| Mount Data Disk | Specify whether to mount data disks to the scaling group. By default, no data disk is mounted. |
| Instances | The number of instances contained in the scaling group. Not e Existing instances in the cluster are excluded. By default, the minimum number of instances is 0. If you specify one or more instances, the system adds the instances to the scaling group. When a scale-out activity is triggered, the instances in the scaling group are added to the cluster to which the scaling group is bound. |
| Password | Use a password. Password: Enter the password that is used to log on to the nodes. Confirm Password: Enter the password again. |
| Scaling Mode | You can select St andard or Swif t . |
| RDS Whitelist | The ApsaraDB RDS instances that can be accessed by the nodes in the scaling group after a scaling activity is triggered. |

| Guide·Kubernetes clusters | Container Service for Kubernete |
|---|---|

| Parameter | Description |
|---|---|
| Label | Labels are automatically added to nodes that are added to the cluster by scale-out activities. |
| ECS Label | You can add labels to the selected ECS instances. |
| Taints | After you add taints to a node, Container Service no longer schedules pods to the node. |
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |

8. Set advanced options.

| Parameter | Description |
|---|---|
| Custom Security Group | Set a custom security group. |
| Custom Image | You can select a custom image. Then, all nodes in the Kubernetes cluster are deployed based on the image. |
| User Data | Customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run scripts during instance startup. Import user data as normal data to an ECS instance for future reference. |

9. Click OK.
Check the results In the left-side navigation pane, choose Applicat ions > Deployment s, select the kube-system namespace. You can find the cluster-autoscaler component. This indicates that the scaling group is created. FAQ Why does the auto scaling component fail to add nodes after a scale-out activity is triggered? Check whether the following situations exist: The instance types in the scaling group cannot fulfill the resource request from pods. By default, system components are installed for each node. Therefore, the requested pod resources must be less than the resource capacity of the instance type. The Resource Access Management (RAM) role does not have the permissions to manage the Kubernetes cluster. You must complete the authorization for each Kubernetes cluster that is involved in the scale-out activity. The Kubernetes cluster cannot connect to the Internet. The auto scaling component must call Alibaba Cloud API operations. Therefore, the nodes must have access to the Internet. Why does the auto scaling component fail to remove nodes after a scale-in activity is triggered? Check whether the following situations exist: The requested resource threshold of each pod is higher than the configured scale-in threshold. Pods that belong to the kube-system namespace are running on the node. A scheduling policy forces the pods to run on the current node. Therefore, the pods cannot be scheduled to other nodes. PodDisruptionBudget is set for the pods on the node and the minimum value of PodDisruptionBudget is reached. For more information about FAQ, see open source component. How does the system choose a scaling group for a scaling activity? When pods cannot be scheduled to nodes, the auto scaling component simulates the scheduling of the pods based on the configuration of scaling groups. The configuration includes labels, taints, and instance specifications. If a scaling group can simulate the scheduling of the pods, this scaling group is selected for the scale-out activity. If more than one scaling groups meet the requirements, the system selects the scaling group that has the fewest idle resources after simulation.

#### 6.11.2 Horizontal pod autoscaling

You can create an application that has Horizontal Pod Autoscaling (HPA) enabled in the Container Service console. HPA can automatically scale container resources for your application. You can also use a YAML file to describe HPA settings. Create an application that has HPA enabled in the Container Service console Container Service provided by Alibaba Cloud is integrated with HPA. You can create an application that has HPA enabled in the Container Service console. You can enable HPA when you create an application or after the application is created. Enable HPA when you creat e an applicat ion
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click the name or click Det ails
in the Act ions column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s tab, click Creat e f rom Image.
6. On the Basic Inf ormat ion wizard page, enter a name for your application, set other required
parameters, and then click Next .

| Parameter | Description |
|---|---|
| Name | Enter a name for the application. |
| Replicas | The number of pods that are provisioned for the application. Default value: 2. |
| Type | The type of the application. You can select Deployment s, St at ef ulSet s, Jobs, Cron Jobs, or DaemonSet s. |
| Label | Add a label to the application. The label is used to identify the application. |
| Annotations | Add an annotation to the application. |
| Synchronize Timezone | Specify whether to synchronize the time zone between nodes and containers. |

7. On the Cont ainer wizard page, set the container parameters, select an image, and then configure
the required computing resources. Click Next . For more information, see Configure the containers. Not e You must configure the required computing resources for the Deployment. Otherwise, you cannot enable HPA.
8. On the Advanced wizard page, find the Access Cont rol section, click Creat e on the right side of
Services, and then set the parameters. For more information, see Create an application from an image.
9. On the Advanced wizard page, select Enable for HPA and configure the scaling threshold and
related settings. Met ric: Select CPU Usage or Memory Usage. The selected resource type must be the same as the one that you have specified in the Required Resources field. Condit ion: Specify the resource usage threshold. HPA triggers scaling activities when the threshold is exceeded. Max. Replicas: Specify the maximum number of pods to which the Deployment can be scaled. Min. Replicas: Specify the minimum number of pods that must run for the Deployment.
10. In the lower-right corner of the Advanced wizard page, click Creat e. The application is created
with HPA enabled. Verif y t he result i. Click View Det ails or choose Workloads > Deployment s. On the page that appears, click the name of t he creat ed applicat ion or click Det ails in the Act ions column. Then, click the Horizont al Pod Aut oscaler tab to view information about the scaling group of the application. ii. After the application starts to run, container resources are automatically scaled based on the CPU utilization. You can also check whether HPA is enabled in the staging environment by performing a CPU stress test on the pods of the application. Verify that the pods are automatically scaled within 30 seconds. Enable HPA af t er an applicat ion is creat ed This example describes how to enable HPA for a stateless application.
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage, and click the name of the cluster
or click Det ails in the Act ions column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, click the name of the application that you want to manage.
6. Click the Pod Scaling tab and click Creat e.
7. In the Creat e dialog box, configure the HPA settings. For more information about how to set the
parameters, see HPA settings in Step 9.
8. Click OK.
Create an application that has HPA enabled by using kubectl You can also create a Horizontal Pod Autoscaler by using an orchestration template and associate the Horizontal Pod Autoscaler with the Deployment for which you want to enable HPA. Then, you can run kubect l commands to enable HPA. In the following example, HPA is enabled for an NGINX application.
1. Create a file named nginx.yml and copy the following content into the file.
The following code block is a YAML template that is used to create a Deployment:

```
apiVersion: apps/v1 kind: Deployment metadata:
  name: nginx
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9 # replace it with your exactly <image_name:tags>
        ports:
        - containerPort: 80
        resources:
          requests:                         ##To enable HPA, you must set this paramete
```

`r.`

```
            cpu: 500m
```

2. Run the following command to create an NGINX application:

```bash
kubectl create -f nginx.yml
```

3. Create a Horizontal Pod Autoscaler.
Use scaleTargetRef to associate the Horizontal Pod Autoscaler with the Deployment named nginx.

```
apiVersion: autoscaling/v2beta1 kind: HorizontalPodAutoscaler metadata:
  name: nginx-hpa
  namespace: default
spec:
  scaleTargetRef:                             ##Associate the Horizontal Pod Autoscaler
with the nginx Deployment.
    apiVersion: apps/v1
    kind: Deployment
    name: nginx
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      targetAverageUtilization: 50
```

Not e You must configure the requested resources for the pods of the application. Otherwise, the Horizontal Pod Autoscaler cannot be started.
4. Run the `kubectl describe hpa` name command. The following output is an example of a
warning that is returned:

```
Warning FailedGetResourceMetric 2m (x6 over 4m) horizontal-pod-autoscaler miss ing request for cpu on container nginx in pod default/nginx-deployment-basic-75675f5897 -mqzs7 Warning FailedComputeMetricsReplicas 2m (x6 over 4m) horizontal-pod-autoscaler fail ed to get cpu utilization: missing request for cpu on container nginx in pod default/ng inx-deployment-basic-75675f5
```

5. After the Horizontal Pod Autoscaler is created, run the `kubectl describe hpa` name command.
If the following output is returned, it indicates that the Horizontal Pod Autoscaler is running as expected:

```
Normal SuccessfulRescale 39s horizontal-pod-autoscaler New size: 1; reason: All metrics below target
```

If the CPU utilization of the NGINX application pod exceeds 50% as specified in the HPA settings, the Horizontal Pod Autoscaler automatically adds pods. If the CPU utilization of the NGINX application pod drops below 50%, the Horizontal Pod Autoscaler automatically removes pods.

### 6.12 Sandboxed-containers

#### 6.12.1 Overview

Sandboxed-Container is an alternative to the Docker runtime. Sandboxed-Container allows you to run applications in a sandboxed and lightweight virtual machine that has a dedicated kernel. This enhances resource isolation and improves security. Sandboxed-Container is applicable to scenarios such as untrusted application isolation, fault isolation, performance isolation, and workload isolation among multiple users. Sandboxed-Container provides higher security. Sandboxed-Container has minor impacts on application performance and offers the same user experience as Docker in terms of logging, monitoring, and elastic scaling. Architecture Features Sandboxed-Container is a container-securing runtime that is developed by Alibaba Cloud based on sandboxed and lightweight virtual machines. Compared with Sandboxed-Container V1, Sandboxed- Container V2 maintains the same isolation performance and reduces the pod overhead by 90%. It also allows you to start sandboxed containers 3 times faster and increases the maximum number of pods that can be deployed on a host by 10 times. Sandboxed-Container V2 provides the following key features: Strong isolation based on sandboxed and lightweight virtual machines. Good compatibility with runC in terms of application management. Network Attached Storage (NAS) file systems, disks, and Object Storage Service (OSS) buckets can be mounted both directly and through virtio-fs. The same user experience as runC in terms of logging, monitoring, and storage. Supports RuntimeClass (runC and runV). For more information, see RuntimeClass. Easy to use with minimum requirements on technical skills. Higher stability than Kata Containers. For more information about Kata Containers, see Kata Containers.

#### 6.12.2 Create a Kubernetes cluster that runs sandboxed containers

sandboxed containers This topic describes how to create a Kubernetes cluster that runs sandboxed containers in the Container Service console.
1. Log on to the Container Service console.
2. In the left-side navigation pane of the Container Service console, click Clust ers. On the Clusters
page that appears, click Creat e Kubernet es Clust er in the upper-right corner.
3. On the Creat e Clust er page, set basic configurations for the cluster.

| Parameter | Description |
|---|---|
| Cluster Name | Enter a name for the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). Not e The cluster name must be unique among clusters that belong to the same Alibaba Cloud account. |
| Region | Select the region where you want to deploy the Kubernetes cluster. |

| Parameter | Description |
|---|---|
| VPC | You can select a virtual private cloud (VPC) from the drop-down list. If the specified VPC is already associated with a NAT gateway, the cluster uses this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear Conf igure SNAT f or VPC. Not e If you disallow the system to automatically create a NAT gateway and want the VPC to access the Internet, you must manually associate the VPC with a NAT gateway or create Source Network Address Translation (SNAT) rules for the VPC. |
| VSwitch | Select one or more vSwitches for the cluster. You can select up to three vSwitches that are deployed in different zones. |
| Kubernetes Version | Select a Kubernetes version. |
| Container Runtime | Select a runtime for the Kubernetes cluster. |
| Billing Method | Only pay-as-you-go nodes are supported. |
| Master Configurations | Set the Instance Type and System Disk parameters: Master Node Quantity: You can add up to three master nodes. Instance Type: You can select one or more instance types. For more information, see the Instance types chapter of ECS User Gui de. System Disk: Standard SSDs and ultra disks are supported. Not e You can select Enable Backup to back up disk data. |
| Worker Instance | By default, Creat e Inst ance is selected. |

| Parameter | Description |
|---|---|
| Worker Configurations | If Worker Inst ance is set to Creat e Inst ance, set the following parameters: Instance Type: Select Elastic Compute Service (ECS) bare metal instance types. Selected Types: The selected instance types are displayed. Quantity: Set the number of worker nodes. System Disk: Standard SSDs and ultra disks are supported. Not e You can select Enable Backup to back up disk data. Mount Data Disk: Standard SSDs and ultra disks are supported. Not e You can enable disk encryption and data backup when you mount disks. The disks are used to store the root file systems of containers on the nodes. Therefore, you must mount a disk of at least 200 GiB. We recommend that you mount a disk of at least 1 TiB. |
| Password | Set a password that is used to log on to the nodes. Not e The password must be 8 to 30 characters in length, and must contain at least three of the following types of character: uppercase letters, lowercase letters, digits, and special characters. |
| Confirm Password | Enter the password again. |
| Network Plug-in | Flannel and Terway are supported. By default, Flannel is selected. |
| Pod CIDR Block and Service CIDR | These parameters are optional. For more information, see Network planning in VPC User Guide. Not e These parameters are available only when you select an existing VPC. |
| Configure SNAT | This parameter is optional. If you clear Configure SNAT for VPC, you must create a NAT gateway or configure SNAT rules for the VPC. |

| Parameter | Description |
|---|---|
| Access to the Internet | Specify whether to expose the API server with an elastic IP address (EIP). The Kubernetes API server provides multiple HTTP-based RESTful APIs that can be used to create, delete, modify, query, and watch resource objects such as pods and Services. If you select this check box, an EIP is created and attached to an internal-facing Server Load Balancer (SLB) instance. Port 6443 used by the API server is exposed on the master nodes. You can connect to and manage the cluster by using kubeconfig over the Internet. If you clear this check box, no EIP is created. You can connect to and manage the cluster only by using kubeconfig from within the VPC. |
| Ingress | Specify whether to install Ingress controllers. By default, Inst all Ingress Cont roller is selected. |
| Log Service | If you enable Log Service, you can select an existing project or create a project. If you select Enable Log Service, the Log Service plug-in is automatically installed in the cluster. If you select Creat e Ingress Dashboard, Ingress access logs are collected and displayed on dashboards. |
| Volume Plug-in | By default, CSI is selected. |
| Deletion Protection | If you select this check box, the cluster cannot be deleted in the console or by calling API operations. |
| RDS Whitelist | Add the IP addresses of the nodes to the whitelist of the ApsaraDB RDS instance that is allowed to access the Kubernetes cluster. Not e To enable an ApsaraDB RDS instance to access the Kubernetes cluster, you must deploy the ApsaraDB RDS instance in the same VPC as the Kubernetes cluster. |
| Node Protection | This check box is selected by default to prevent nodes from being deleted in the console or by calling API operations. |
| Label | Add labels to the cluster. |

4. Complete the advanced settings of the cluster.

| Parameter | Description |
|---|---|
| IP Addresses per Node | The number of IP addresses that is assigned to a node. |

| Parameter | Description |
|---|---|
| Kube-proxy Mode | iptables and IPVS are supported. iptables is a mature and stable kube-proxy mode. It uses iptables rules to conduct service discovery and load balancing. The performance of this mode is restricted by the size of the Kubernetes cluster. This mode is suitable for Kubernetes clusters that manage a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux Virtual Server (LVS) to conduct service discovery and load balancing. This mode is suitable for Kubernetes clusters that manage a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. |
| Custom Node Name | Specify whether to use a custom node name. |
| Node Port Range | Specify the node port range. |
| Taints | Add taints to all worker nodes in the Kubernetes cluster. |
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |
| Cluster Domain | The default domain name of the cluster is cluster.local. You can specify a custom domain name. |
| Cluster CA | Specify whether to enable the cluster CA certificate. |
| User Data | You can customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run user data scripts during instance startup. Import user data as common data to an ECS instance for future reference. |

5. Click Creat e Clust er in the upper-right corner of the page.
6. On the Conf irm page, click OK to start the deployment.
Result After the cluster is created, you can find the cluster on the Clust ers page in the Container Service console.

#### 6.12.3 Expand a Container Service cluster that runs sandboxed containers

runs sandboxed containers This topic describes how to scale out the worker nodes in a Container Service cluster that runs sandboxed containers in the Container Service console. Prerequisites You cannot scale out the master nodes in a Container Service cluster that runs sandboxed containers. To expand a Container Service cluster that runs sandboxed containers, you must set the parameters as required in the following table. Otherwise, the added nodes cannot run sandboxed containers.
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Expand in the Act ions
column.
4. Go to the Expand page and set the required parameters.
In this example, the number of worker nodes in the Container Service cluster is increased from three to five. The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Cluster Name | By default, the name of the Container Service cluster appears. |
| Region | The region where the Container Service cluster is deployed. |
| Container Runtime | By default, Sandboxed-Container appears. |
| VPC | You can select a virtual private cloud (VPC) from the drop-down list. If the specified VPC is already associated with a NAT gateway, the cluster uses this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear Conf igure SNAT f or VPC. Not e If you disallow the system to automatically create a NAT gateway and want the VPC to access the Internet, you must manually associate the VPC with a NAT gateway or create Source Network Address Translation (SNAT) rules for the VPC. |
| VSwitch | Select one or more vSwitches for the cluster. You can select up to three vSwitches that are deployed in different zones. |
| Billing Method | Only pay-as-you-go nodes are supported. |
| Existing Worker Nodes | The number of existing workers in the Container Service cluster. |
| Nodes to Add | Set the number of worker nodes to add. |
| Worker Nodes After Scaling | The number of worker nodes after the scaling. |

| Guide·Kubernetes clusters | Container Service for Kubernete |
|---|---|

| Parameter | Description |
|---|---|
| Instance Type | Select ECS Bare Metal Instance. |
| Selected Types | The selected instance types are displayed. |
| System Disk | Standard SSDs and ultra disks are supported. Not e You can select Enable Backup to back up disk data. |
| Mount Data Disk | Standard SSDs and ultra disks are supported. Not e You can enable disk encryption and data backup when you mount disks. The disks are used to store the root file systems of containers on the nodes. Therefore, you must mount a disk of at least 200 GiB. We recommend that you mount a disk of at least 1 TiB. |
| Password | Password: Enter the password that is used to log on to the nodes. Conf irm Password: Enter the password again. |
| RDS Whitelist | Set the Apsara RDS whitelist. Add the IP addresses of the nodes in the cluster to the RDS whitelist. |
| Label | Add labels to the cluster. |
| Taints | Add taints to all worker nodes in the Kubernetes cluster. |
| CPU Policy | Specify the CPU policy. Valid values: None: indicates that the default CPU affinity is used. This is the default policy. Static: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity. |
| User Data | You can customize the startup behaviors of ECS instances and import data to the ECS instances. The user data can be used to perform the following operations: Run user data scripts during instance startup. Import user data as common data to an ECS instance for future reference. |

5. Click Submit .
What's next After the Container Service cluster is expanded, go to the details page of the Container Service cluster. In the left-side navigation pane, choose Clust ers > Node Pools. You can find that the number of worker nodes is increased from 3 to 5.

#### 6.12.4 Create an application that runs in sandboxed containers

sandboxed containers This topic describes how to use an image to create an NGINX application that runs in sandboxed containers. The NGINX application is accessible over the Internet. Prerequisites A cluster that contains sandboxed containers is created. For more information, see Create a Kubernetes cluster that supports sandboxed containers. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Workloads > Deployment s.
5. On the Deployment s page, select the namespace and click Creat e f rom Image in the upper-right
corner.
6. On the Basic Inf ormat ion wizard page, specify the basic information of the application and click
Next . Set Cont ainer Runt ime to runv. Set the following parameters: Name, Replicas, T ype, Label, and Annot at ions. Select whether you want to enable Synchronize T imezone. The number of replicas specifies the number of pods that are provisioned for in the application. Not e Deployment s is selected in this example.
7. Configure containers.
Not e In the upper part of the Cont ainer wizard page, click Add Cont ainer to add more containers for the application. The following table describes the parameters that are required to configure the containers. General settings

| Parameter | Description |
|---|---|
| Image Name | Click Select Image. In the dialog box that appears, select an image and click OK. In this example, an NGINX image is selected. You can also enter the address of an image stored in a private registry. The image address must be in the following format: doma inname/namespace/imagename:tag . |

|   | inname/namespace/imagename:tag |
|---|---|

| Parameter | Description |
|---|---|
| Image Version | Click Select Image Version and select an image version. If you do not specify an image version, the latest image version is used. You can select the following image pulling policies: if Not Present : If the image that you want to pull is found in the region where the cluster is deployed, Container Service uses the local image. Otherwise, Container Service pulls the image from the corresponding repository. Always: Container Service pulls the image from the repository each time the application is deployed or expanded. Never: Container Service uses only images on your on-premise machine. Not e If you select Image Pull Policy, no image pulling policy is applied. To pull the image without a Secret, click Set Image Pull Secret to set a Secret for pulling images. |
| Resource Limit | You can specify an upper limit for the CPU, memory, and ephemeral storage space that the container can consume. This prevents the container from occupying an excessive amount of resources. The CPU resource is measured in milicores (one thousandth of one core). The memory resource is measured in MiB. The ephemeral storage resource is measured in GiB. |
| Required Resources | The amount of CPU and memory resources that are reserved for this application. These resources are exclusive to the container. This prevents the application from becoming unavailable if other services or processes compete for computing resources. |
| Container Start Parameter | stdin: Pass stdin to the container. tty: Stdin is a TeleTYpewriter (TTY). |
| Privileged Container | If you select Privileged Container, privileged=true is set for the container and the privilege mode is enabled. If you do not select Privileged Container, privileged=false is set for the container and the privilege mode is disabled. |
| Init Container | If you select Init Container, an init container is created. An init container provides tools to manage pods. For more information, see Init Containers. |

(Optional)Ports Configure container ports. Name: Enter a name for the port. Container Port: Enter the container port that you want to open. Enter a port number from 1 to 65535. Protocol: Select TCP or UDP. (Optional)Environments You can configure environment variables for pods in key-value pairs. Environment variables are used to apply pod configurations to containers. For more information, see Pod variables. Type: Select the type of the environment variable. You can select Cust om, Conf igMaps, Secret s, Value/ValueFrom, or ResourceFieldRef . If you select ConfigMaps or Secret as the type of the environment variable, all values in the selected ConfigMap or Secret are passed to the container environment variables. In this example, Secret is selected. Select Secret s from the Type drop-down list and select a Secret from the Value/ValueFrom drop-down list. All values in the selected Secret are passed to the environment variable. In this case, the YAML file that is used to deploy the application contains the settings that reference all data in the selected Secret. Variable Key: Specify the name of the environment variable. Value/ValueFrom: Specify the value that is referenced by the environment variable. (Optional)Health Check Health check settings include liveness and readiness probes. Liveness probes determine when to restart the container. Readiness probes determine whether the container is ready to accept network traffic. For more information about health checks, see Configure Liveness, Readiness, and Startup Probes.

| Request type | Description |
|---|---|

| Request type | Description |
|---|---|
| HTTP | Sends an HTTP GET request to the container. You can configure the following parameters: Protocol: HTTP or HTTPS. Path: the requested path on the server. Port: Enter the container port that you want to open. Enter a port number from 1 to 65535. HTTP Header: Enter the custom headers in the HTTP request. Duplicate headers are allowed. Key-value pairs are supported. Initial Delay (s): the initialDelaySeconds field in the YAML file. This field specifies the time (in seconds) that the system must wait before it can send a probe to the container after the container is started. Default value: 3. Period (s): the periodSeconds field in the YAML file. This field specifies the interval (in seconds) at which probes are performed. Default value: 10. Minimum value: 1. Timeout (s): the timeoutSeconds field in the YAML file. This field specifies the time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |

| Request type | Description |
|---|---|
| TCP | Sends a TCP socket to the container. kubelet attempts to open the socket on the specified port. If the connection can be established, the container is considered healthy. Otherwise, the container is considered unhealthy. You can set the following parameters: Port: Enter the container port that you want to open. Enter a port number from 1 to 65535. Initial Delay (s): the initialDelaySeconds field in the YAML file. This field specifies the time (in seconds) that the system must wait before it can send a probe to the container after the container is started. Default value: 15. Period (s): the periodSeconds field in the YAML file. This field specifies the time interval (in seconds) at which probes are performed. Default value: 10. Minimum value: 1. Timeout (s): the timeoutSeconds field in the YAML file. This field specifies the time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |
| Command | Runs a probe command in the container to check the health status of the container. You can set the following parameters: Command: the probe command that is run to check the health status of the container. Initial Delay (s): the initialDelaySeconds field in the YAML file. This field specifies the time (in seconds) that the system must wait before it can send a probe to the container after the container is started. Default value: 5. Period (s): the periodSeconds field in the YAML file. This field specifies the interval (in seconds) at which probes are performed. Default value: 10. Minimum value: 1. Timeout (s): the timeoutSeconds field in the YAML file. This field specifies the time (in seconds) after which a probe times out. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of times that an unhealthy container must consecutively pass health checks before it is considered healthy. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of times that a healthy container must consecutively fail health checks before it is considered unhealthy. Default value: 3. Minimum value: 1. |

Lifecycle You can set the following parameters to configure the lifecycle of the container: Start, Post Start, and Pre Stop. For more information, see Configure the lifecycle of a container. St art : Set the command and parameter that take effect before the container starts. Post St art : Set the command that takes effect after the container starts. Pre St op: Set the command that takes effect before the container stops. (Optional)Volume You can mount local volumes and persistent volume claims (PVCs) to the container. Add Local St orage: You can select HostPath, ConfigMap, Secret, and EmptyDir. The source directory or file is mounted to a path in the container. For more information, see Volumes. Add PVC: Cloud Storage is supported. In this example, a PVC named disk-ssd is mounted to the /tmp path of the container. (Optional)Log Configure Log Service. You can specify log collection configurations and add custom tags. Not ice Make sure that the Log Service agent is installed in the cluster.

| Parameter | Description |
|---|---|
| Collection Configuration | Logstore: creates a Logstore in Log Service to store collected log data. |
|   | Log Path in Container: specifies stdout or a path to collect log data stdout: specifies that the stdout files are collected. Text Logs: specifies that log data in the specified path of the container is collected. In this example, /var/log/nginx is specified as the path. Wildcard characters can be used to specify the path. |
| Custom Tag | You can also add custom tags. Custom tags are added to the log data of the container when the log data is collected. Log data with tags is easier to aggregate and filter. |

8. Configure the parameters based on your business requirements and click Next .
9. (Optional)Configure advanced settings.
Access Control You can configure the following access control settings based on your business requirements: Internal applications: For applications that run inside the cluster, you can create a ClusterIP or NodePort Service to enable internal communication. External applications: For applications that are open to the Internet, you can configure access control by using one of the following methods: Create a LoadBalancer Service and enable access to your application over the Internet by using a Server Load Balancer (SLB) instance. Create an Ingress and use the Ingress to expose your application to the Internet. For more information, see Ingress. You can also specify how the backend pods are exposed to the Internet. In this example, a ClusterIP Service and an Ingress are created to expose the NGINX application to the Internet.

| Parameter | Description |
|---|---|
| Services | Click Creat e on the right side of Services. In the Create Service dialog box, set the parameters. Select Clust er IP. |
| Ingresses | Click Creat e on the right side of Ingresses. In the Create dialog box, set the parameters. Not e When you create an application from an image, you can create an Ingress only for one Service. In this example, a virtual hostname is used as the test domain name. You must add the following entry to the hosts file to map the domain name to the IP address of the Ingress. In actual scenarios, use a domain name that has obtained an Internet Content Provider (ICP) number. 101.37.22*.*** foo.bar.com #The IP address of the Ingress. |

You can find the created Service and Ingress in the Access Cont rol section. You can click Updat e or Delet e to change the configurations. Scaling Specify whether to enable HPA to automatically scale the number of pods based on the CPU and memory usage. This enables the application to run smoothly at different load levels. Not e To enable HPA, you must configure required resources for the container. Otherwise, HPA does not take effect. Met ric: Select CPU Usage or Memory Usage. The selected resource type must be the same as the one you have specified in the Required Resources field. Condit ion: Specify the resource usage threshold. HPA triggers scaling events when the threshold is exceeded. Max. Replicas: Specify the maximum number of replicated pods to which the application can be scaled. Min. Replicas: Specify the minimum number of replicated pods that must run. Scheduling You can set the following parameters: Update Method, Node Affinity, Pod Affinity, Pod Anti Affinity, and Toleration. For more information, see Affinity and anti-affinity. Not e Node affinity and pod affinity affect pod scheduling based on node labels and pod labels. You can add node labels and pod labels that are provided by Kubernetes to configure node affinity and pod affinity. You can also add custom labels to nodes and pods, and then configure node affinity and pod affinity based on these custom labels.

| Parameter | Description |
|---|---|
| Update Method | Select Rolling Update or OnDelete. For more information, see Deployments. |
| Node Affinity | Set Node Af f init y by adding labels to worker nodes. Node Affinity supports required and preferred rules, and various operators, such as In, NotIn, Exists, DoesNotExist, Gt, and Lt. Required: Specify the rules that must be matched for pod scheduling. In the YAML file, these rules are defined by the requiredDuringSchedulingIgnoredDuringExecution field of the nodeAffinity parameter. These rules have the same effect as the NodeSelector parameter. In this example, pods can be scheduled only to nodes with the specified labels. You can create multiple required rules. However, only one of them must be met. Pref erred: Specify the rules that are not required to be matched for pod scheduling. Pods are scheduled to a node that matches the preferred rules when multiple nodes match the required rules. In the YAML file, these rules are defined by the preferredDuringSchedulingIgnoredDuringExecution field of the nodeAffinity parameter. In this example, the scheduler attempts to schedule a pod to a node that matches the preferred rules. You can also set weights for preferred rules. If multiple nodes match the rule, the node with the highest weight is preferred. You can create multiple preferred rules. However, all of them must be met before the pod can be scheduled. |
|   | Pod affinity rules specify how pods are deployed relative to other |

| Contain | er Service for Kubernetes | User Guide·Kubernetes cluster |   | s |
|---|---|---|---|---|
|   | Parameter | pods in the same topology domain. For example, you can use pod Description affinity to deploy services that communicate with each other to |   |   |
|   | Pod Affinity | the same topological domain, such as a host. This reduces the network latency between these services. Pod affinity enables you to select nodes to which pods can be scheduled based on the labels of other running pods. Pod affinity supports required and preferred rules, and the following operators: In, NotIn, Exists, and DoesNotExist . Required: Specify rules that must be matched for pod scheduling. In the YAML file, these rules are defined by the requiredDuringSchedulingIgnoredDuringExecution field of the podAffinity parameter. A node must match the required rules before pods can be scheduled to the node. Namespace: Specify the namespace to apply the required rule. Pod affinity rules are defined based on the labels that are added to pods and therefore must be scoped to a namespace. T opological Domain: Set the topologyKey. This specifies the key for the node label that the system uses to denote the topological domain. For example, if you set the parameter to kubernetes.io/hostname , topologies are determined by nodes. If you set the parameter to beta.ku bernetes.io/os , topologies are determined by the operating systems of nodes. Select or: Click Add to add pod labels. View Applicat ions: Click View Applicat ions and set the namespace and application in the dialog box that appears. You can view the pod labels on the selected application and add the labels as selectors. Required Rules: Specify labels on existing applications, the operator, and the label value. In this example, the required rule specifies that the application to be created is scheduled to a host that runs applications with the app:nginx label. Pref erred: Specify rules that are not required to be matched for pod scheduling. In the YAML file, preferred rules are defined by the preferredDuringSchedulingIgnoredDuringExecution field of the podAffinity parameter. The scheduler attempts to schedule the pod to a node that matches the preferred rules. You can set weights for preferred rules. The other parameters are the same as those of required rules. Not e Weight : Set the weight of a preferred rule to a value from 1 to 100. The scheduler calculates the weight of each node that meets the preferred rule based on an algorithm, and then schedules the pod to the node with the highest weight. |   |   |
|   |   |   | beta.ku |   |

|   | bernetes.io/os |
|---|---|

| Parameter | Description |
|---|---|
| Pod Anti Affinity | Pod anti-affinity rules specify that pods are not scheduled to topological domains where pods with matching labels are deployed. Pod anti-affinity rules apply to the following scenarios: Schedule the pods of an application to different topological domains, such as multiple hosts. This allows you to enhance the stability of the service. Grant a pod exclusive access to a node. This enables resource isolation and ensures that no other pod can share the resources of the specified node. Schedule pods of an application to different hosts if the pods may interfere with each other. Not e The parameters of pod anti-affinity rules are the same as those of pod affinity rules. You can create the rules for different scenarios. |
| Toleration | Configure toleration rules to allow pods to be scheduled to nodes with matching taints. |
| Schedule to Virtual Nodes | Specify whether to schedule pods to virtual nodes. This option is unavailable if the cluster does not contain a virtual node. |

Labels and Annotations Pod Labels: Add a label to the pod. The label is used to identify the application. Pod Annotations: Add an annotation to the pod.
10. Click Creat e.
After the application is deployed, you are redirected to the Complete wizard page. The resource objects of the application are displayed. You can find the resource objects under the application and click View Det ails to view application details.
11. In the left-side navigation pane, choose Ingresses and Load Balancing > Ingresses.
The created Ingress rule is displayed on the page. Result Enter the test domain in the address bar of your browser and press Enter. The NGINX welcome page appears.

#### 6.12.5 Configure a Kubernetes cluster that runs both sandboxed and Docker containers

both sandboxed and Docker containers Node pools support multiple types of container runtime. However, nodes in the same node pool must use the same type of container runtime. Container Service allows you to create node pools of different container runtime types for a cluster. This topic describes how to create a node pool that runs sandboxed containers and a node pool that runs Docker containers for a Kubernetes cluster. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Not ice The Kubernetes cluster must meet the following requirements: The cluster version must be 1.14.6-aliyun.1 or later. The network plug-in must be Flannel or Terway. Terway must run in One ENI for Multi-Pod mode. The volume plug-in must be CSI-Plugin 1.14.8.39-0d749258-aliyun or later. Flexvolume is not supported. The logtail-ds version must be 0.16.34.2-f6647154-aliyun or later. Considerations By default, a cluster can contain at most 100 nodes. Before you add an existing Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC), make sure that an elastic IP address (EIP) is associated with the ECS instance, or a NAT gateway is created in the VPC. In addition, the nodes that you want to add to the node pool must have access to the Internet. Otherwise, the ECS instance cannot be added. Create a node pool that runs Docker containers
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Node Pools.
5. On the Node Pools page, click Creat e Node Pool and set the parameters.
For more information, see Create a Kubernetes cluster. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | Enter a name for the node pool. |
| Container Runtime | Select Docker. This specifies that all containers in the node pool are Docker containers. |
| Quantity | Specify the initial number of nodes in the node pool. If you do not need to create nodes, set this parameter to 0. |
| Operating System | The CentOS and Aliyun Linux operating systems are supported. |

| ainer Service for Kubernetes | User Guide·Kubernetes cluster |
|---|---|

| Parameter | Description |
|---|---|
| ECS Label | You can add labels to the ECS instances. |
| Node Label | You can add labels to the nodes in the cluster. |
| Custom Resource Group | Specify the resource group of the nodes to be added to the node pool. |
| Custom Security Group | Select a custom security group. |

6. Click OK.
Create a node pool that runs sandboxed containers
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Nodes > Node Pools.
5. On the Node Pools page, click Creat e Node Pool and set the parameters.
For more information, see Create a Kubernetes cluster. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | Enter a name for the node pool. |
| Container Runtime | Select Sandboxed-Container. This specifies that all containers in the node pool are sandboxed containers. |
| Quantity | Specify the initial number of nodes in the node pool. If you do not need to create nodes, set this parameter to 0. |
| Operating System | Select an operating system. Sandboxed containers support only the Aliyun Linux operating system. |
| Mount Data Disk | You must mount a disk of at least 200 GiB. |
| ECS Label | You can add labels to the ECS instances. |
| Node Label | You can add labels to the nodes in the cluster. |
| Custom Resource Group | Specify the resource group of the nodes to be added to the node pool. |
| Custom Security Group | Select a custom security group. |

6. Click OK.
Result After you perform the preceding steps, check the states of the node pools on the Node Pools page. If the node pools are in the Act ivat e state, the node pools are created. You can connect to the Kubernetes cluster and view detailed information about the nodes in the node pools. i. On the Node Pools page, select a node pool that you have created and click its name. In the Node Pool Inf ormat ion section, find and record the Node Pool ID. ii. Connect to the Kubernetes cluster by using kubectl. For more information, see Connect to a cluster through kubectl. iii. Run the following command to query the names of the nodes in a specified node pool:

```bash
kubectl get node --show-labels | grep -E "${node pool ID}|${node pool ID}"
```

iv. Run the following command to query detailed information about a specified node:

```bash
kubectl get node -o wide | grep -E "${node name} {node name}"
```

#### 6.12.6 How do I select between Docker and Sandboxed-Container?

Sandboxed-Container? Containers and images have become the industry standards for software packaging and delivery. Kubernetes has become a standard platform for building, developing, and managing containerized cloud-native applications. An increasing number of enterprises and customers choose to deploy their applications in Container Service. Container Service supports two types of runtime: Docker and Sandboxed-Container. This topic describes the differences between these runtimes in the following aspects: implementations and limits, commonly used commands provided by Docker Engine and Containerd, and deployment architectures. This provides references for you to select between Docker and Sandboxed-Container based on your requirements. Differences between Docker and Sandboxed-Container in terms of implementations and limits

| Item | Docker | Sandboxed-Container V2 | Description |
|---|---|---|---|
| Cluster type | All types | All types | N/A |
| Node type | ECS EBM | EBM | N/A |

| ontainer Service for Kubern | etes | Use | r Guide·Kubernetes cluster |
|---|---|---|---|

| Item | Docker | Sandboxed-Container V2 | Description |
|---|---|---|---|
| Node operating system | CentOS Alibaba Cloud Linux2 | Alibaba Cloud Linux2 | You cannot deploy both Docker and Sandboxed-Container on the same node. To deploy both Docker and Sandboxed-Container in a cluster, you can create node pools of different runtime types. |
| Container engine | Docker | Containerd | N/A |
| Monitoring | Supported | Supported | N/A |
| Container log collection | Supported | Sidecar: supported. Manual configuration is required. | N/A |
| Container stdout collection | Supported | Supported | N/A |
| RuntimeClass | Not supported | Supported (runV) | N/A |
| Pod scheduling | No configuration is required. | For Kubernetes V1.14.x, you must add the following configuration to the nodeSelector field: alibabacloud.co m/sandboxed- container: Sandboxed- Container.runv For Kubernetes V1.16.x and later, no configuration is required. | N/A |
| HostNetwork | Supported | Not supported | N/A |
| exec/logs | Supported | Supported | N/A |
| Node data disk | N/A | Required. The data disk must be at least 200 GiB. | N/A |

| ser Guide·Kubernetes clust | ers | Cont | ainer Service for Kubernete |
|---|---|---|---|

| Item | Docker | Sandboxed-Container V2 | Description |
|---|---|---|---|
| Network plug-in | Flannel Terway | Flannel Terway: supports only the One ENI for Multi-Pod mode. | N/A |
| Kube-proxy mode | Iptables IPVS | Iptables IPVS | N/A |
| Volume plug-in | CSI Plugin | CSI Plugin | N/A |
| Container root file system | OverlayFS | VirtioFS | N/A |

Differences in the commonly used commands provided by Docker Engine and Containerd Docker uses Docker Engine for container lifecycle management. Sandboxed-Container uses Containerd for container lifecycle management. These tools support different commands that can be used to manage images and containers. The following table lists the commonly used commands.

| Command | Docker | Containerd |   |
|---|---|---|---|
|   | docker | crictl (recommended) | ctr |
| Queries containers | docker ps | crictl ps | ctr -n k8s.io c ls |
| Queries container details | docker inspect | crictl inspect | ctr -n k8s.io c info |
| Queries container logs | docker logs | crictl logs | N/A |
| Runs a command in a container | docker exec | crictl exec | N/A |
| Mounts local standard input, output, and error streams to a running container | docker attach | crictl attach | N/A |
| Queries resource usage statistics | docker stats | crictl stats | N/A |
| Creates a container | docker create | crictl create | ctr -n k8s.io c create |
| Starts one or more containers | docker start | crictl start | ctr -n k8s.io run |
| Stops one or more containers | docker stop | crictl stop | N/A |

| ontainer Service for Kubern | etes | Use | r Guide·Kubernetes cluster |
|---|---|---|---|
| Command | Docker | Containerd |   |
|   | docker | crictl (recommended) | ctr |
| Removes one or more containers | docker rm | crictl rm | ctr -n k8s.io c del |
| Queries images | docker images | crictl images | ctr -n k8s.io i ls |
| Queries image details | docker inspect | crictl inspecti | N/A |
| Pulls an image | docker pull | crictl pull | ctr -n k8s.io i pull |
| Pushes an image | docker push | N/A | ctr -n k8s.io i push |
| Removes one or more images | docker rmi | crictl rmi | ctr -n k8s.io i rm |
| Queries pods | N/A | crictl pods | N/A |
| Queries pod details | N/A | crictl inspectp | N/A |
| Starts one or more pods | N/A | crictl runp | N/A |
| Stops one or more pods | N/A | crictl stopp | N/A |

Differences between Docker and Sandboxed-Container in terms of deployment architectures

| Runtime | Deployment architecture |
|---|---|
| Docker | kubelet -> dockerd -> containerd -> containerd-shim -> runC containers |
| Sandboxed- Container V1 | kubelet -> (CRI)containerd \-> containerd-shim -> runC containers \-> containerd-shim-kata-v2 -> runV sandboxed containers |
| Sandboxed- Container V2 | kubelet -> (CRI)containerd \-> containerd-shim -> runC containers \-> containerd-shim-rund-v2 -> runV sandboxed containers |

#### 6.12.7 Benefits of Sandboxed-Container

This topic describes the advantages and application scenarios of Sandboxed-Container and provides a comparison between Sandboxed-Container and open source Kata Containers. This allows you to learn more about the benefits of Sandboxed-Container. Context Sandboxed-Container provides an alternative to the Docker runtime environment. It supports the following features: Sandboxed-Container allows your applications to run in a sandboxed and lightweight virtual machine. This virtual machine is equipped with a dedicated kernel and provides better isolation and enhanced security. Compared with open source Kata Containers, Sandboxed-Container is optimized for storage, networking, and stability. You can use Sandboxed-Container to isolate untrusted applications and applications of different tenants for higher security. You can also use Sandboxed-Container to isolate applications with faults and applications with degraded performance. This minimizes the negative impact on your service. In addition, Sandboxed-Container offers the same user experience as Docker in terms of logging, monitoring, and elastic scaling. Benefits Compared with Docker, Sandboxed-Container has the following benefits: Strong isolation based on sandboxed and lightweight virtual machines. Compatibility with runC in terms of application management. High performance that corresponds to 90% performance of applications based on runC. The same user experience as runC in terms of logging, monitoring, and storage. Support for RuntimeClass. Easy to use with limited expertise that is required to use virtual machines. Higher stability than that provided by Kata Containers. Comparison between Sandboxed-Container and Kata Containers Sandboxed-Container outperforms Kata Containers in the following aspects.

| Item | Category | Sandboxed-Container | Kata Containers |
|---|---|---|---|
| Sandbox startup time consumption |   | About 150 ms | About 500 ms |
| Root file system |   | OverlayFS over virtio-fs. Performance: ☆☆☆☆ | OverlayFS over 9pfs. Performance: ☆☆ |
|   | HostPath | Disks are mounted to Sandboxed-Container over 9pfs. Performance: ☆☆ | Disks are mounted to Kata Containers over 9pfs. Performance: ☆☆ |

| ontainer Service for Kubern |   |   |   |
|---|---|---|---|
|   | etes User Guide·Kubernetes cluster |   |   |
| Item | Category | Sandboxed-Container | Kata Containers |
| Volume | EmptyDir | over VirtioFS | By default, the volume is mounted to Kata Containers over 9pfs. |
|   | Disk | By default, cloud disks are mounted to Sandboxed-Container over virtio-fs. Performance: ☆☆☆☆ | Cloud disks are mounted to Kata Containers over 9pfs. Performance: ☆☆ |
|   | NAS | By default, Apsara File Storage NAS (NAS) file systems are mounted to Sandboxed- Container over virtio-fs. Performance: ☆☆☆☆ | NAS file systems are mounted to Kata Containers over 9pfs. Performance: ☆ |
| Network plug-in |   | The Terway network plug-in is used. Its network performance is 20% to 30% higher than Flannel. Terway supports features such as NetworkPolicy. This allows you to define the networking policies for pods. Flannel | Flannel |
| Monitoring and alerting |   | Enhanced monitoring of disks and network conditions for pods that host Sandboxed- Container. Integrated with Cloud Monitor. This facilitates cluster monitoring and alerting. | Monitoring of disks and network conditions is unavailable for pods that host Sandboxed- Container. |
| Stability |   | ☆☆☆☆☆ | ☆☆ |

Applicable scenarios of Sandboxed-Container This section describes the applicable scenarios of Sandboxed-Container. Scenario 1: Sandboxed-Container can run untrusted code and applications in isolated containers. This is not supported by containers in runC. Security risks of runC runC isolates containers by using namespaces and control groups (cgroups). This exposes containers to security threats. All containers on a node share the host kernel. If a kernel vulnerability is exposed, malicious code may escape to the host and then infiltrate the backend network. Malicious code execution may cause privilege escalation, compromise sensitive data, and destroy system services and other applications. Attackers may also exploit application vulnerabilities to infiltrate the internal network. You can implement the following measures to reduce security risks of containers in runC. Seccomp: filters system calls. SElinux: restricts the permissions of container processes, files, and users. Capability: limits the capability of container processes. dockerd rootless mode: forbids users to use root permissions to run the Docker daemon and containers. The preceding measures can enhance the security of containers in runC and reduce attacks on the host kernel by malicious containers. However, container escapes and host kernel vulnerabilities remain unresolved. Sandboxed-Container prevents potential risks based on container isolation In a Sandboxed-Container runtime environment, applications that have potential security risks are deployed on sandboxed and lightweight virtual machines. Each of the virtual machines has a dedicated guest OS kernel. If a security vulnerability is detected on a guest OS kernel, the attack is limited to one sandbox and does not affect the host kernel or other containers. The Terway network plug-in allows you to define networking policies for pods. This enables system isolation, data isolation, and network isolation for Sandboxed-Containers. Scenario 2: Sandboxed-Container resolves common issues of runC containers, such as fault spreading, resource contention, and performance interference. Kubernetes provides easy deployment of different containers on a single node. However, cgroups are not optimized to address resource contention. Resource-intensive applications (such as CPUintensive, I/O-intensive applications) may compete for the same resources. This causes significant fluctuations in response time and increases the overall response time. Exceptions or faults on an application may spread to the hosting node and disrupt the running of the total cluster. For example, memory leaks and frequent core dumps of an application may overload the node, and exceptions on a container may trigger a host kernel bug that results in complete system failure. Sandboxed- Container addresses the issues that are common with runC containers by using dedicated guest OS kernels and hypervisors. The issues include failure spreading, resource contention, and performance interference. Scenario 3: Sandboxed-Container supports multi-tenant services. You may need to isolate the applications of an enterprise that consists of multiple business lines or departments. For example, a financial department requires high security applications. However, other non-security-sensitive applications do not have high security requirements. Containers in runC fail to eliminate the potential risks that arise in untrusted applications. In this scenario, you can implement the following counter measures: Deploy multiple independent single-tenant clusters. For example, deploy financial business and other non-security-sensitive business in different clusters. Deploy a multi-tenant cluster and separate applications of different business lines by namespaces. The resource of a node is exclusive to a single business line. This solution provides data isolation for coordination with the resource quotas and network policies to implement multi-tenant isolation. Compared with multiple single-tenant clusters, this solution focuses on fewer management planes and thus reduces management costs. However, this solution cannot avoid resource waste on nodes. This issue is caused by low resource utilization of some tenants. Sandboxed-Container allows you to isolate untrusted applications by using sandboxed virtual machines. This prevents the risks of container escapes. This also allows you to deploy different containerized applications on each node. This way, the following benefits are provided: Resource scheduling is simplified. A node is no longer exclusive to a service. This improves node resource usage and reduces resource fragments and cluster resource costs. Sandboxed containers use lightweight virtual machines to provide almost the same performance as containers in runC.

#### 6.12.8 Differences between runC and runV

This topic describes the differences between runC and Sandboxed-Container (runV) in terms of their performance and pod creation methods. This allows you to better understand and utilize the benefits of sandboxed containers. Differences between runC and runV

| Item | runC | runV |
|---|---|---|
| Container engine | Docker and Containerd | Containerd |
| Node type | Elastic Compute Service (ECS) instances and ECS Bare Metal instances | EBM |
| Container kernel | Share the host kernel | Dedicated kernel |
| Container isolation | Cgroups and namespaces | Lightweight virtual machines (VMs) |
| Rootfs Graph Driver | OverlayFS | DeviceMapper |
| RootFS I/O throttling | Cgroups | DeviceMapper Block IO Limit Not e Supported by only Sandboxed-Container V1. |
| NAS mounting | Not supported | Supported |
| Disk mounting | Not supported | Supported |
| Collection of container logs | Logtail directly collects container logs from the host. | logtail sidecar |

| Item | runC | runV |
|---|---|---|
| Pod Overhead | None | Sandboxed-Container V1: For example, if you set memory: 512 Mi for a pod overhead, it indicates that 512 MiB of memory is allocated to the pod sandbox. Pod overhead refers to the amount of resources consumed by the pod sandbox. In this case, if you set a memory limit of 512 MiB for containers in the pod, the pod will request a total memory of 1,024 MiB. Sandboxed-Container V2: The memory limit for a pod overhead is calculated based on the following formula: Memory for a pod overhead = 64 MiB + Requested memory of containers in a pod × 2%. If the result is greater than 512 MiB, the value is set to 512 Mi. If the result is smaller than 64 MiB, the value is set to 64 Mi. |

Differences in pod creation between runC and runV You can connect to clusters of Container Service by using kubectl. For more information, see Connect to a cluster through kubectl. Create a pod that uses runC i. (Optional)Use `runtimeClassName: runc` to set the container runtime to runC. Not e The preceding command is optional. runC is the default container runtime. ii. Run the following commands to create a pod that uses runC:

```
cat <<EOF | kubectl create -f apiVersion: v1 kind: Pod metadata:
  name: busybox-runc
  labels:
    app: busybox-runc
spec:
  containers:
  - name: busybox
    image: registry.cn-hangzhou.aliyuncs.com/acs/busybox:v1.29.2
    command:
    - tail
    - -f
    - /dev/null
    resources:
      limits:
        cpu: 1000m
        memory: 512Mi
      requests:
        cpu: 1000m
        memory: 512Mi
EOF
```

Create a pod that uses runV i. Use `runtimeClassName: runv` to set the container runtime to runV. ii. (Optional)Run the following command to verify that a RuntimeClass object named `runv` exists in the cluster.

```bash
kubectl get runtimeclass runv -o yaml
```

Not e A RuntimeClass object named `runv` is automatically created in a Kubernetes cluster that uses Sandboxed-Container. iii. Run the following command to create a pod that uses runV:

```
cat <<EOF | kubectl create -f apiVersion: v1 kind: Pod metadata:
  name: busybox-runv
  labels:
    app: busybox-runv
spec:
  runtimeClassName: runv
  nodeSelector:
    alibabacloud.com/container-runtime: Sandboxed-Container.runv
  containers:
  - name: busybox
    image: registry.cn-hangzhou.aliyuncs.com/acs/busybox:v1.29.2
    command:
    - tail
    - -f
    - /dev/null
    resources:
      limits:
        cpu: 1000m
        memory: 512Mi
      requests:
        cpu: 1000m
        memory: 512Mi
EOF
```

Not ice If the Kubernetes version is earlier than 1.16, add the following nodeSelector configuration:

```
nodeSelector:
    alibabacloud.com/container-runtime: Sandboxed-Container.runv
```

iv. Run the following command to query the pod that you have created: If the output is `runv` , it indicates that the pod is running in a sandbox.

```bash
kubectl get pod busybox-runv -o jsonpath={.spec.runtimeClassName}
```

v. Run the following command to log on to the pod and query its CPU and memory specifications:

```bash
kubectl exec -ti pod busybox-runv /bin/sh / # cat /proc/meminfo | head -n1 MemTotal: 1130692 kB / # cat /proc/cpuinfo | grep processor processor : 0
```

The output shows that the number of CPUs is not the same as that of the host. The total memory is the sum of pod memory and pod overhead. Be aware that the total memory is slightly smaller because the system also consumes some memory.

#### 6.12.9 Compatibility notes

This topic describes the pod fields that are supported by Sandboxed-Container. This allows you to fully use the Sandboxed-Container runtime. Context Sandboxed-Container is a new runV container runtime that provides compatibility with runC in terms of pod networking, service networking (ClusterIP and NodePort), and image management. However, Sandboxed-Container does not support all pod fields. To use Sandboxed-Container, you do not need to change your development mode or image packaging method. Supported pod fields Sandboxed-Container supports the following pod fields that are marked by ticks:

### 6.13 Use the Kubernetes event center

The event center feature allows you to log Kubernetes events, query events, and configure alerting. This topic describes how to enable and view the Kubernetes event center. Enable the Kubernetes event center Enable t he Kubernet es event cent er when a Kubernet es clust er is creat ed
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers. On the page that appears, click Creat e
Kubernet es Clust er in the upper-right corner.
3. On the Creat e Clust er page, select Inst all node-problem-det ect or and Creat e Event
Cent er in the Log Service field. For more information about other parameters, see Create a Kubernetes cluster. Then, click Creat e Clust er.
4. On the Conf irm dialog box, after all check items are verified, select the terms of service and
disclaimer and click OK to create the cluster. Enable t he Kubernet es event cent er in App Cat alog
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > App Cat alog.
3. On the App Cat alog page, find and click ack-node-problem-detector.
4. On the App Cat alog - ack-node-problem-det ect or page, click the Paramet ers tab and set

```
eventer.sinks.sls.enabled to true .
```

5. On the App Cat alog - ack-node-problem-det ect or page, click the Descript ion tab.
6. In the Deploy pane, select the cluster and click Creat e.
Access the Kubernetes event center Access t he Kubernet es event cent er in t he Cont ainer Service console
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers.
3. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions
column.
4. In the left-side navigation pane of the details page, choose Operat ions > Event Cent er.
5. Access the Kubernetes event center on the Event Center page
Not e If the Event Center page does not appear, check whether the Kubernetes event center is enabled. On the Event Cent er page, click the Event s Overview tab to go to the overview page of the Kubernetes event center. On the Event Cent er page, click the Clust er Event s Query tab to customize query conditions. On the Event Cent er page, click the Pod Event s tab to query events of pods. Access t he Kubernet es event cent er by using Log Service
1. View the cluster ID.
i. Log on to the Container Service console. ii. In the left-side navigation pane, click Clust ers. iii. On the Clust ers page, find the cluster that you want to manage and click Det ails in the Act ions column. iv. Click the Basic Inf ormat ion tab to view the cluster ID.
2. Log on to the Log Service console.
3. In the search box of the Projects section, enter and click k8s-log-<CLUSTER_ID>.
Not e Replace the CLUSTER_ID with the cluster ID that you obtained in Step .
4. In the Logstores section, choose K8s-event > Visual Dashboards > Kubernet es Event Cent er
V1.2.
5. On the Kubernet es Event Cent er V1.2 page, you can view the trends of WARNING events and
ERROR events.

### 6.14 Use Log Service to collect log data from containers

data from containers Container Service is integrated with Log Service. When you create a cluster, you can enable Log Service to collect log data from containers, including standard outputs (stdout) and text files. Activate Log Service To activate Log Service, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose
Product s > Log Service to go to the Log Service page.
2. Select the required organization and region.
3. Click SLS to go to the Log Service console.
Create a Kubernetes cluster and enable Log Service To create a Kubernetes cluster, perform the following steps:
1. Log on to the Container Service console.
Not e The specified organization must be the same as the one that you selected when you activated Log Service. For more information, see Activate Log Service.
2. In the left-side navigation pane, click Clust ers.
3. On the Clusters page, click Creat e Kubernet es Clust er. For more information, see Create a
Kubernetes cluster.
4. In the Component Configuration step, select Enable Log Service to install the Log Service
component.
5. When the Enable Log Service check box is selected, the system prompts you to create a Log Service
project. You can only select Creat e Project . After you select Create Project, the system creates a project. By default, the system names the project in the format of `k8s-log-{ClusterID}` . ClusterID indicates the unique ID of the cluster to be created.
6. Click Creat e Clust er in the upper-right corner of the page.
7. On the Conf irm Order page, after all check items are verified, select the terms of service and
disclaimer and click OK to start the deployment. On the Clusters page, you can find the created cluster. Install Log Service components in an existing Kubernetes cluster If you created a Kubernetes cluster and activated Log Service, you can perform the following steps to use Log Service:
1. Connect to the Kubernetes cluster by using CloudShell.
For more information, see Connect to a Kubernetes cluster through kubectl.
2. Run the logtail-dedicated.sh script to install Log Service components in the Kubernetes cluster.

```
#!/env/bin/bash
yaml=$(cat <<-END --apiVersion: v1 kind: ConfigMap metadata:
  name: alibaba-log-config-file
  namespace: kube-system
data:
  ilogtail_config.json: |
```

`{`

```json
      "config_server_address" : "http://logtail.$REGION.sls-pub.$INTERNET_DOMAIN",
      "data_server_address" : "http://data.$REGION.sls-pub.$INTERNET_DOMAIN",
      "data_server_list" :
```

`[` `{`

```json
              "cluster" : "$REGION",
              "endpoint" : "data.$REGION.sls-pub.$INTERNET_DOMAIN"
```

`}` `],`

```json
      "shennong_unix_socket" : false
```

`}`

```
--apiVersion: v1 kind: ConfigMap metadata:
  name: alibaba-log-configuration
  namespace: kube-system
data:
    log-project: "k8s-log-$CLUSTER_ID"
    log-endpoint: "data.$REGION.sls-pub.$INTERNET_DOMAIN"
    log-machine-group: "k8s-group-$CLUSTER_ID"
    log-config-path: "/etc/ilogtail/conf/apsara/ilogtail_config.json"
    log-ali-uid: "$ALI_UID"
    log-access-id: "" # just use blank string
    log-access-key: "" # just use blank string
--apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: alibaba-log-controller
  namespace: kube-system
  labels:
    k8s-app: alibaba-log-controller
  annotations:
```

```
    component.version: "v0.1.3"
    component.revision: "v1"
spec:
  replicas: 1
  template:
    metadata:
      labels:
        k8s-app: alibaba-log-controller
      annotations:
        scheduler.alpha.kubernetes.io/critical-pod: ''
    spec:
      serviceAccountName: alibaba-log-controller
      tolerations:
        - operator: "Exists"
      containers:
      - name: alibaba-log-controller
        image: $IMAGE_REPO_URL/acs/log-controller-$ARCH:v0.1.3.0-527ff4d-aliyun
        resources:
          limits:
            memory: 100Mi
          requests:
            cpu: 50m
            memory: 100Mi
        env:
          - name: "ALICLOUD_LOG_PROJECT"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-project
          - name: "ALICLOUD_LOG_ENDPOINT"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-endpoint
          - name: "ALICLOUD_LOG_MACHINE_GROUP"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-machine-group
          - name: "ALICLOUD_ACS_K8S_FLAG"
            value: "ture"
          - name: "ALICLOUD_ACCESS_KEY_ID"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-access-id
          - name: "ALICLOUD_ACCESS_KEY_SECRET"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-access-key
      nodeSelector:
        beta.kubernetes.io/os: linux
---
```

`iV` `i` `i` `t` `i` `k8`

```
i/1bt1
```

```
apiVersion: apiextensions.k8s.io/v1beta1 kind: CustomResourceDefinition metadata:
  name: aliyunlogconfigs.log.alibabacloud.com
spec:
  group: log.alibabacloud.com
  version: v1alpha1
  names:
    kind: AliyunLogConfig
    plural: aliyunlogconfigs
  scope: Namespaced
--apiVersion: rbac.authorization.k8s.io/v1beta1 kind: ClusterRoleBinding metadata:
  name: alibaba-log-controller
subjects:
- kind: ServiceAccount
  name: alibaba-log-controller
  namespace: kube-system
roleRef:
  kind: ClusterRole
  name: alibaba-log-controller
  apiGroup: rbac.authorization.k8s.io
--apiVersion: rbac.authorization.k8s.io/v1beta1 kind: ClusterRole metadata:
  name: alibaba-log-controller
  labels:
    k8s-app: alibaba-log-controller
rules:
- apiGroups: ["log.alibabacloud.com"]
  resources:
  - aliyunlogconfigs
  verbs:
  - update
  - get
  - watch
  - list
- apiGroups: [""]
  resources:
  - configmaps
  verbs:
  - create
  - update
  - get
- apiGroups: [""]
  resources:
  - events
  verbs:
  - create
  - patch
  - update
---
```

```
--apiVersion: v1 kind: ServiceAccount metadata:
  name: alibaba-log-controller
  namespace: kube-system
  labels:
    k8s-app: alibaba-log-controller
--apiVersion: extensions/v1beta1 kind: DaemonSet metadata:
  name: logtail-ds
  namespace: kube-system
  labels:
    k8s-app: logtail-ds
  annotations:
    component.version: "v0.16.16"
    component.revision: "v0"
spec:
  updateStrategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        k8s-app: logtail-ds
      annotations:
        scheduler.alpha.kubernetes.io/critical-pod: ''
    spec:
      tolerations:
        - operator: "Exists"
      containers:
      - name: logtail
        image: $IMAGE_REPO_URL/acs/logtail-$ARCH:v0.16.24.0-c46cd2fe-aliyun
        resources:
          limits:
            memory: 512Mi
          requests:
            cpu: 100m
            memory: 256Mi
        livenessProbe:
          exec:
            command:
            - /etc/init.d/ilogtaild
            - status
          initialDelaySeconds: 30
          periodSeconds: 30
        securityContext:
          privileged: false
        env:
          - name: "ALIYUN_LOGTAIL_CONFIG"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-config-path
```

```
ey: ogco gpat
          - name: "ALIYUN_LOGTAIL_USER_ID"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-ali-uid
          - name: "ALIYUN_LOGTAIL_USER_DEFINED_ID"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-machine-group
          - name: "ALICLOUD_LOG_DOCKER_ENV_CONFIG"
            value: "true"
          - name: "ALICLOUD_LOG_ECS_FLAG"
            value: "ture"
          - name: "ALICLOUD_LOG_DEFAULT_PROJECT"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-project
          - name: "ALICLOUD_LOG_ENDPOINT"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-endpoint
          - name: "ALICLOUD_LOG_DEFAULT_MACHINE_GROUP"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-machine-group
          - name: "ALICLOUD_LOG_ACCESS_KEY_ID"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-access-id
          - name: "ALICLOUD_LOG_ACCESS_KEY_SECRET"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-access-key
          - name: "ALIYUN_LOG_ENV_TAGS"
            value: "_node_name_|_node_ip_"
          - name: "_node_name_"
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: "_node_ip_"
            valueFrom:
              fieldRef:
                fieldPath: status.hostIP
        volumeMounts:
        - name: sock
          mountPath: /var/run/docker.sock
        - name: root
          mountPath: /logtail_host
```

```
          readOnly: true
        - name: alibaba-log-config-file-volume
          mountPath: /etc/ilogtail/conf/apsara
          readOnly: true
      terminationGracePeriodSeconds: 30
      nodeSelector:
        beta.kubernetes.io/os: linux
      volumes:
      - name: sock
        hostPath:
          path: /var/run/docker.sock
          type: Socket
      - name: root
        hostPath:
          path: /
          type: Directory
      - name: alibaba-log-config-file-volume
        configMap:
          name: alibaba-log-config-file
END
```

`)`

```bash
echo "$yaml" > logtail.yml kubectl create -f logtail.yml
```

| e | <your server architecture> _ _ |   | , | <your k8s cluster region id> _ _ _ _ |   |   | , | <your k8s cluster _ _ _ |   |
|---|---|---|---|---|---|---|---|---|---|
| <k8s cluster domain suffix> _ _ _ |   | , | <your ali uid> _ _ |   | , and | <your image repo url> _ _ _ |   |   | with |

actual values, and run the following commands. This allows you to set the environment variables and deploy the components.

```
export ARCH=<your_server_architecture> export REGION=<your_k8s_cluster_region_id> export CLUSTER_ID=<your_k8s_cluster_id> export INTERNET_DOMAIN=<k8s_cluster_domain_suffix> export IMAGE_REPO_URL=<your_image_repo_url> export ALI_UID=<your_ali_uid> bash logtail-dedicated.sh // Run the script to install the components.
```

Not e `<your_server_architecture>` : the server architecture, for example, amd64. `<your_k8s_cluster_region_id>` : the region where the Kubernetes cluster is deployed, for example, cn-qingdao-apsara-d01. `<your_k8s_cluster_id>` : the ID of the Kubernetes cluster. `<k8s_cluster_domain_suffix>` : the domain suffix of the Kubernetes cluster, for example, env28.internet.com. `<your_ali_uid>` : the ID of the Apsara Stack tenant account, for example, 1234074238634394. `<your_image_repo_url>` : the URL of the image repository, for example, registry.cnhangzhou.aliyuncs.com. Create an application and configure Log Service When you create an application in Container Service, you can configure Log Service to collect log data from containers. You can only use YAML templates to configure Log Service.
1. Log on to the Container Service console. In the left-side navigation pane, choose Applicat ions >
Deployment s. In the upper-right corner of the Deployments page, click Creat e f rom T emplat e.
2. YAML templates follow the Kubernetes syntax. You can use environment variables to add
collect ion conf igurat ions and cust om t ags. You must also configure volumeMounts and volumes. The following is an example of a pod for collecting log data:

```
apiVersion: extensions/v1beta1 kind: Deployment metadata:
  labels:
    app: logtail-test
  name: logtail-test
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: logtail-test
      name: logtail-test
    spec:
      containers:
      - name: logtail
        image: registry.acs.env28.intranet.com/acs/busybox:latest
        args:
        - ping
        - 127.0.0.1
        env:
        - name: aliyun_logs_log-stdout
          value: stdout
        - name: aliyun_logs_log-varlog
          value: /log/*.log
        - name: aliyun_logs_log_tags
          value: tag1=v1
        volumeMounts:
        - name: volumn-sls
          mountPath: /log
      volumes:
      - name: volumn-sls
        emptyDir: {}
```

Specify the following configurations in order based on your business requirements: Use environment variables to add collect ion conf igurat ions and cust om t ags. All environment variables for collection configurations must use the `aliyun_logs_` prefix. Add log collection configurations in the following format:

```
- name: aliyun_logs_{Logstore name}
  value: {Log file path}
```

In the preceding YAML template, two environment variables are added to the log collection configuration. Environment variable `aliyun_logs_log-stdout` indicates that a Logstore named log-stdout is created to store the standard outputs collected from containers. Not e The name of the Logstore cannot contain underscores (_). You can use hyphens (-) instead. Cust om t ags must be specified in the following format:

```
- name: aliyun_logs_{Tag name without underscores (_)}_tags
  value: {Tag name }={Tag value}
```

After a tag is added, the tag is automatically appended to the log files that are collected from the container. If you specify a log path to collect log files that are not standard outputs, you must configure volumeMounts. In the preceding YAML template, the mountPath field in volumeMounts is set to /var/log. This allows the Log Service component to collect /var/log/*.log files.
3. After you modify the YAML template, click Creat e to submit the configurations.
Configure advanced parameters in the env field You can specify multiple parameters in the env field to configure log collection. The following table describes the parameters.

| Parameter | Description | Example | Precaution |
|---|---|---|---|
| aliyun logs {key} _ _ | Required.{key} can contain only lowercase letters, digits, and hyphens (- ), and cannot contain underscores ( ). _ If the specified aliyun logs {key} log _ _ _ store does not exist, a Logstore named {key} is created. To collect standard outputs of container log files, set the value to stdout. You can also set the value to a path inside a container. | - name: aliyun logs cat _ _ alina stdout - name: aliyun logs acc _ _ ess-log /var/log/nginx/ access.log | By default, the Log Service component collects log files in simple mode. In this case, the collected log files are not parsed. If you want to parse the log files, we recommend that you change the collection mode in the Log Service console. The value of {key} must be unique in the cluster. |

| Parameter | Description | Example | Precaution |
|---|---|---|---|
| aliyun logs {key} tags _ _ _ | Optional. This parameter is used to add tags to log data. The value must be in the following format: {tag-key}={tag-value}. | - name: aliyun logs catal _ _ ina tags _ app=catalina | - |
| aliyun logs {key} projec _ _ _ t | Optional. This parameter specifies a project in Log Service. By default, the project that you specified when you create the cluster is used. | - name: aliyun logs catal _ _ ina project _ my-k8s-project | The region of the project must be the same as where your logtail-ds is deployed. |
| aliyun logs {key} logsto _ _ _ re | Optional. This variable specifies a Logstore in Log Service. By default, the Logstore is named after {key}. | - name: aliyun logs catal _ _ ina tags _ my-logstore | - |
| aliyun logs {key} shard _ _ _ | Optional. This variable specifies the number of shards in the Logstore. Valid values: 1 to 10. Default value: 2. | - name: aliyun logs catal _ _ ina shard _ 4 | - |
| aliyun logs {key} ttl _ _ _ | Optional. This parameter specifies the number of days for which log data is retained. Valid values: 1 to 3650. To permanently retain log data, set the value to 3650. Default value: 90. | - name: aliyun logs catal _ _ ina ttl _ 3650 | - |
| aliyun logs {key} machi _ _ _ negroup | Optional. This parameter specifies the machine group of the application. By default, the machine group is the one where your logtail-ds is deployed. | - name: aliyun logs catal _ _ ina machinegroup _ my-machine- group | - |

Scenario 1: Collect log files from multiple applications and store them in the same Logstore In this scenario, set the aliyun_logs_{key}_logstore parameter. The following example shows how to collect standard outputs from two applications and store the outputs in stdout-logstore. Configure the following environment variables for Application 1:

```
######### Configure environment variables ###########
    - name: aliyun_logs_app1-stdout
      value: stdout
    - name: aliyun_logs_app1-stdout_logstore
      value: stdout-logstore
```

Configure the following environment variables for Application 2:

```
######### Configure environment variables ###########
    - name: aliyun_logs_app2-stdout
      value: stdout
    - name: aliyun_logs_app2-stdout_logstore
      value: stdout-logstore
```

Scenario 2: Collect log files from different applications and store them in different projects In this scenario, perform the following steps: i. Create a machine group in each project and set the machine group ID in the following format: k8s-group-{cluster-id}, where {cluster-id} is the ID of the cluster. You can customize the machine group name. ii. Specify the project, Logstore, and machine group in the environment variables for each application.

```
######### Configure environment variables ###########
    - name: aliyun_logs_app1-stdout
      value: stdout
    - name: aliyun_logs_app1-stdout_project
      value: app1-project
    - name: aliyun_logs_app1-stdout_logstore
      value: app1-logstore
    - name: aliyun_logs_app1-stdout_machinegroup
      value: app1-machine-group
```

View log data Perform the following steps to view log data:
1. Log on to the Log Service console. For more information, see Activate Log Service.
2. Select the project that is associated with the Kubernetes cluster to go to the Logstores tab. By
default, the project name is in the format of k8s-log-{Kubernetes cluster ID}.
3. In the list of Logstores, find the Logstores and click Search in the Log Search column for each
Logstore. In this example, the Logstores are log-stdout and log-varlog.
4. On the Raw Logs tab, you can view raw log data in log-stdout and log-varlog.
