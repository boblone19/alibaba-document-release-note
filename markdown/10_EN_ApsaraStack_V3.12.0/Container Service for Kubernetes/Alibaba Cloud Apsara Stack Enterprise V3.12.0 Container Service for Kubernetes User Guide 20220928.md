---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 179
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Container%20Service%20for%20Kubernetes%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Container Service for Kubernetes User Guide 20220928

## Table of Contents

- 1 What is Container Service?
- 2 Planning and preparation
- 3 Quick start
  - 3.1 Flowchart
  - 3.2 Log on to the Container Service console
  - 3.3 Log on to the Container Registry console
  - 3.4 Create a Kubernetes cluster
  - 3.5 Create an application from an orchestration template
- 4 Kubernetes clusters
  - 4.1 Authorizations
    - 4.1.1 Assign RBAC permissions to a RAM user
  - 4.2 Clusters
    - 4.2.1 Create a Kubernetes cluster
    - 4.2.2 View cluster logs
    - 4.2.3 Connect to a cluster through kubectl
    - 4.2.4 Connect to a master node by using SSH
    - 4.2.5 Expand a cluster
    - 4.2.6 Renew a certificate
    - 4.2.7 Delete a cluster
    - 4.2.8 View cluster overview
  - 4.3 Nodes
    - 4.3.1 Add an existing node
    - 4.3.2 View nodes
    - 4.3.3 Manage node labels
    - 4.3.4 Set node schedulability
    - 4.3.5 Remove a node
    - 4.3.6 View node resource usage
    - 4.3.7 Upgrade the NVIDIA driver on a GPU node
    - 4.3.8 Create a Kubernetes cluster for GPU computing
    - 4.3.9 Use labels to schedule pods to GPU nodes
    - 4.3.10 Manually upgrade the kernel of a GPU node in a cluster
  - 4.4 Storage
    - 4.4.1 Overview
    - 4.4.2 Use Apsara Stack disks
    - 4.4.3 Use NAS volumes
    - 4.4.4 Use OSS volumes
    - 4.4.5 Create a PVC
    - 4.4.6 Use a PVC
  - 4.5 Network management
    - 4.5.1 Set access control for pods
    - 4.5.2 Set bandwidth limits for pods
  - 4.6 Namespaces
    - 4.6.1 Create a namespace
    - 4.6.2 Set resource quotas and limits
    - 4.6.3 Edit a namespace
    - 4.6.4 Delete a namespace
  - 4.7 Applications
    - 4.7.1 Create an application from an image
    - 4.7.2 Create an application from an orchestration template
    - 4.7.3 Create an application through Kubernetes Dashboard
    - 4.7.4 Use commands to manage applications
    - 4.7.5 Create a service
    - 4.7.6 Scale a service
    - 4.7.7 View a service
    - 4.7.8 Update a service
    - 4.7.9 Delete a service
    - 4.7.10 Create a trigger on an application
    - 4.7.11 View pods
    - 4.7.12 Simplify Kubernetes application deployment by using Helm
    - 4.7.13 Schedule pods to nodes
  - 4.8 SLB and Ingress
    - 4.8.1 Overview
    - 4.8.2 Access a service through SLB
    - 4.8.3 Configure ingress monitoring
    - 4.8.4 Ingress support
    - 4.8.5 Ingress configurations
    - 4.8.6 Create an Ingress in the console
    - 4.8.7 Update an ingress
    - 4.8.8 Delete an ingress
  - 4.9 Config maps and secrets
    - 4.9.1 Create a ConfigMap
    - 4.9.2 Use a ConfigMap in a Pod
    - 4.9.3 Update a ConfigMap
    - 4.9.4 Delete a ConfigMap
    - 4.9.5 Create a secret
    - 4.9.6 Edit a secret
    - 4.9.7 Delete a secret
  - 4.10 Templates
    - 4.10.1 Create an orchestration template
    - 4.10.2 Update an orchestration template
    - 4.10.3 Save an orchestration template as a new one
    - 4.10.4 Download an orchestration template
    - 4.10.5 Delete an orchestration template
  - 4.11 Images
    - 4.11.1 Create an image repository
    - 4.11.2 Create a namespace
    - 4.11.3 Synchronize an image
    - 4.11.4 Sign and verify an image
    - 4.11.5 Synchronize images between instances
  - 4.12 Create a batch release
  - 4.13 Use Log Service to collect Kubernetes logs

e?

## 1 What is Container Service?

Container Service provides high-performance, scalable, and enterprise-class management service for Kubernetes containerized applications throughout the application lifecycle. Container Service simplifies the deployment and scaling operations on Kubernetes clusters. Integrated with services such as virtualization, storage, network, and security, Container Service aims to provide the optimal cloud environment for Kubernetes containerized applications. Alibaba Cloud is a Kubernetes Certified Service Provider (KCSP). As one of the first services to participate in the Certified Kubernetes Conformance Program, Container Service provides you with professional support and services. n

## 2 Planning and preparation

Before you start using Container Service, you need to create cloud resources such as VPC networks, VSwitches, disks, and OSS buckets based on your application requirements. Before you create a Kubernetes cluster, make the following preparations: Creat e a VPC net work (optional) To create a cluster in an existing VPC network, you must create the VPC network and VSwitches in advance. Creat e a volume (optional) To create a stateful application with network storage, you must create disks or OSS buckets in advance.

## 3 Quick start

### 3.1 Flowchart

You can take the following steps to use Container Service. The flowchart is as follows: St ep 1: Aut horize t he def ault role Authorize the Container Service default role to perform operations on the resources under the target organization. St ep 2: Log on t o t he Cont ainer Service console Log on to the Container Service console. For more information, see Log on to the Container Service console. St ep 3: Creat e a clust er Set the network environment and the number of nodes, and configure node details. St ep 4: Deploy an applicat ion by using an image or orchest rat ion t emplat e You can use an existing image or orchestration template, or create a new image or orchestration template. To create an application that consists of services based on different images, use an orchestration template. St ep 5: Manage t he applicat ion lif ecycle

### 3.2 Log on to the Container Service console

console You can perform the following steps to log on to the Container Service console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Cont ainer Service f or
Kubernet es.
5. Select the target organization and region.
6. Click ACK to go to the Container Service console.

### 3.3 Log on to the Container Registry console

console You can perform the following steps to log on to the Container Registry console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > ACK-CR.
5. Select the target organization and region.
6. Click CR to go to the Container Registry console.

### 3.4 Create a Kubernetes cluster

To create a Kubernetes cluster, you need to set a series of parameters. For more information, see . Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. On the Clusters page, click Creat e
Kubernet es Clust er in the upper-right corner.
3. Configure basic parameters.
Cluster parameters

| Parameter | Description |
|---|---|
| Clust er Name | The name of the cluster. The name must be 1 to 63 characters in length and can contain digits, Chinese characters, letters, and hyphens (-). Not e The cluster name must be unique under one account. |
| Region | The region where the cluster is deployed. |
| Zone | The zone where the cluster belongs. |

| Parameter | Description |
|---|---|
| VPC | You can select a VPC network from the drop- down list. If the VPC network that you select already has a NAT gateway, Container Service will use this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear the Conf igure SNAT f or VPC check box. Not e In this case, you need to manually create a NAT gateway or configure SNAT rules to enable Internet access to the VPC network. Otherwise, cluster creation will fail. |
| Node T ype | Currently, only pay-as-you-go nodes are supported. |
| Mast er Conf igurat ion | Select the instance types and system disk type. Instance Type: You can select multiple instance types. For more information, see the Instance t ypes chapter of ECS User Guide. System Disk: SSD and ultra disks are supported. Quantity: You can add three master nodes. |
| Worker Inst ance | You can choose to create instances or add existing instances. |
| Worker Conf igurat ion | If you choose Creat e Inst ance, you need to set the following parameters: Instance Type: You can select multiple instance types. For more information, see the Instance t ypes chapter of ECS User Guide. Quantity: Set the number of worker nodes. System Disk: SSD and ultra disks are supported. Attach Data Disk: SSD, ultra, and basic disks are supported. |
| Docker Version and Kubernet es Version | Supported Docker and Kubernetes versions are displayed. Select based on your needs. |

| Parameter | Description |
|---|---|
| Password | Set the node logon password. Not e The password must be 8 to 30 characters in length and contain three of the following four types of characters: uppercase letters, lowercase letters, digits, and special characters. |
| Conf irm Password | Enter the logon password again. |
| Net work Plug-in | Flannel and Terway are supported. Flannel is enabled by default. |
| Pod CIDR Block and Service CIDR (Optional) | For more information, see the Network planning chapter of VPC User Guide. Not e These options are available when you select an exist ing VPC network. |
| Conf igure SNAT | Optional. If you clear this check box, you need to create a NAT gateway or configure SNAT rules to enable Internet access to the VPC network. |
| Public SLB | If you select this check box, a public SLB instance is created and the 6443 port used by the API server is enabled on master nodes. You can use kubeconfig to connect to the cluster through the Internet. Not e If you clear the Expose API Server wit h Public SLB check box, you cannot access the cluster API server through the Internet. |
| SSH logon | If you select this check box, you can use SSH to access the cluster. If you clear this check box, you cannot use SSH or kubectl to access the cluster. |
| Log Service | If you enable Log Service, select an existing project or create a new one. The Log Service plug-in is automatically installed in the cluster. |
| Delet e Prot ect ion | If you select this check box, the cluster cannot be deleted through the console or API operations. |

| Parameter | Description |
|---|---|
| RDS Whit elist | Add the IP addresses of nodes to the RDS whitelist. |
| Node Prot ect ion | This check box is selected by default to prevent nodes from being deleted through the console or APIs. |
| Labels | Attach labels to the nodes. |
| Advanced Opt ions | Pods on Each Node: The maximum number of pods that can run on a single node. Cluster Domain: Default is cluster.local. Custom domains are supported. Cluster CA: Set whether to enable custom cluster CA. |

4. Click Creat e Clust er in the upper-right corner.
5. On the Conf irm page, click OK to start the deployment.
Result You can find the newly created cluster on the Clust ers page.

### 3.5 Create an application from an orchestration template

orchestration template Container Service provides orchestration templates that you can use to create applications quickly. You can also modify the templates based on YAML syntax to customize applications. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Context The following example demonstrates how to create an NGINX application consisting of a deployment and a service. The service is associated with a pod created by the deployment. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployment s page
appears.
3. In the upper-right corner, click Creat e f rom T emplat e.
4. Set the parameters and click Creat e.
Clust er: Select the cluster where the resource objects are to be deployed. Namespace: Select the namespace to which the resource objects belong. The default namespace is default. Except for underlying computing resources such as nodes and PVs, most resources are scoped to namespaces. Sample T emplat e: Container Service provides YAML templates of various resource types to help you deploy resource objects quickly. You can also create a custom template based on YAML syntax to describe the resource that you want to define. Add Deployment : This feature allows you to quickly define a YAML template. Use Exist ing T emplat e: You can import an existing template to the configuration page. Based on an orchestration template provided by Container Service, the following sample template creates a deployment of an NGINX application. Not e Container Service supports YAML syntax. You can use the `---` symbol to separate multiple resource objects. This enables you to create multiple resource objects in a single template.

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
   type: LoadBalancer        ## This example changes the service type from NodePort to
LoadBalancer.
```

5. Click Creat e. A message appears indicating the deployment status.
In the left-side navigation pane, choose Ingresses and Load Balancing > Services to view the newly created service.
6. On Kubernetes Dashboard, verify that a my-service1 service is running and its external endpoint is
displayed. Click the address in the Ext ernal Endpoint column.
7. You can visit the NGINX welcome page in the browser.
What's next You can also choose Ingresses and Load Balancing > Services in the left-side navigation pane to view the NGINX service.

## 4 Kubernetes clusters

### 4.1 Authorizations

#### 4.1.1 Assign RBAC permissions to a RAM user

This topic describes how to assign role-based access control (RBAC) permissions to Resource Access Management (RAM) users. By default, RBAC policies are enabled for Kubernetes 1.6 and later versions. RBAC policies are important for you to improve the management of clusters. You can use RBAC policies to specify the types of operations that are allowed for specific users based on their roles in an organization. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Aut horizat ions to go to the Authorizations
page.
3. Choose Select RAM User > RAM Users, select the required RAM user, and then click Modif y
Permissions. Not e Before you authorize a RAM user, make sure that the RAM user has been granted the RBAC administrator permissions or the cluster-admin role for the specified cluster.
4. On the Conf igure Role-Based Access Cont rol (RBAC) wizard page, click the plus sign (+) to add
permissions on one or all clusters and namespaces, select a predefined role in the Permission field, or click the minus sign (-) for a target role to delete the role, and then click Next St ep. Not e You can add permissions of a predefined role and one or more custom roles on a specified cluster or namespace. The following table defines the permissions of predefined roles on one or all clusters and namespaces. Roles and permissions

| Role | RBAC-based permission on one or all clusters |
|---|---|
| Administrator | Granted the read and write permissions on resources in all namespaces. |
| O&M Engineer | Granted the read and write permissions on resources in all namespaces and the read-only permissions on nodes, persistent volumes (PVs), namespaces, and quotas. |
| Developer | Granted the read and write permissions on resources in one or all namespaces. |
| Restricted User | Granted the read-only permissions on resources in one or all namespaces. |

| Role | RBAC-based permission on one or all clusters |
|---|---|
| Custom | Different cluster roles have different permissions. Before you authorize a RAM user, make sure that you are aware of all resource access permissions of the selected cluster roles. This avoids unnecessary permissions granted to the RAM user. |

After the authorization, you can use the specified RAM user to log on to the Container Service console and manage the service. For more information, see Log on to the Container Service console. Custom permissions Container Service supports predefined roles to grant different permissions. These predefined roles include: administrator, O&M engineer, developer, and restricted user. These predefined roles meet most of your requirements when you manage the service in the console. If you want to customize permissions on clusters, you can use custom roles. Container Service provides multiple custom roles. Not e The cluster-admin role has permissions of a super administrator of clusters and has permissions on all resources. You can log on to the master node of the specified cluster and run the following command to view the details of custom permissions.

```bash
 # kubectl get clusterrole
# kubectl get clusterrole
NAME AGE admin 13d alibaba-log-controller 13d alicloud-disk-controller-runner 13d cluster-admin 13d cs:admin 13d edit 13d flannel 13d kube-state-metrics 22h node-exporter 22h prometheus-k8s 22h prometheus-operator 22h system:aggregate-to-admin 13d .... system:volume-scheduler 13d view 13d
```

In this example, the cluster-admin role is used. On the command line, run the following command to view the permission details:

```bash
 # kubectl get clusterrole cluster-admin -o yaml
```

Not ice After a RAM user is granted the permissions of cluster-admin, for the specified cluster, the RAM user has the same permissions as your Alibaba Cloud account and has all permissions on all resources in the cluster. Proceed with caution.

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

### 4.2 Clusters

#### 4.2.1 Create a Kubernetes cluster

To create a Kubernetes cluster, you need to set a series of parameters. For more information, see . Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. On the Clusters page, click Creat e
Kubernet es Clust er in the upper-right corner.
3. Configure basic parameters.
Cluster parameters

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Clust er Name | The name of the cluster. The name must be 1 to 63 characters in length and can contain digits, Chinese characters, letters, and hyphens (-). Not e The cluster name must be unique under one account. |
| Region | The region where the cluster is deployed. |
| Zone | The zone where the cluster belongs. |
| VPC | You can select a VPC network from the drop- down list. If the VPC network that you select already has a NAT gateway, Container Service will use this NAT gateway. Otherwise, the system automatically creates a NAT gateway. If you do not want the system to create a NAT gateway, clear the Conf igure SNAT f or VPC check box. Not e In this case, you need to manually create a NAT gateway or configure SNAT rules to enable Internet access to the VPC network. Otherwise, cluster creation will fail. |
| Node T ype | Currently, only pay-as-you-go nodes are supported. |
| Mast er Conf igurat ion | Select the instance types and system disk type. Instance Type: You can select multiple instance types. For more information, see the Instance t ypes chapter of ECS User Guide. System Disk: SSD and ultra disks are supported. Quantity: You can add three master nodes. |
| Worker Inst ance | You can choose to create instances or add existing instances. |

| Parameter | Description |
|---|---|
| Worker Conf igurat ion | If you choose Creat e Inst ance, you need to set the following parameters: Instance Type: You can select multiple instance types. For more information, see the Instance t ypes chapter of ECS User Guide. Quantity: Set the number of worker nodes. System Disk: SSD and ultra disks are supported. Attach Data Disk: SSD, ultra, and basic disks are supported. |
| Docker Version and Kubernet es Version | Supported Docker and Kubernetes versions are displayed. Select based on your needs. |
| Password | Set the node logon password. Not e The password must be 8 to 30 characters in length and contain three of the following four types of characters: uppercase letters, lowercase letters, digits, and special characters. |
| Conf irm Password | Enter the logon password again. |
| Net work Plug-in | Flannel and Terway are supported. Flannel is enabled by default. |
| Pod CIDR Block and Service CIDR (Optional) | For more information, see the Network planning chapter of VPC User Guide. Not e These options are available when you select an exist ing VPC network. |
| Conf igure SNAT | Optional. If you clear this check box, you need to create a NAT gateway or configure SNAT rules to enable Internet access to the VPC network. |
| Public SLB | If you select this check box, a public SLB instance is created and the 6443 port used by the API server is enabled on master nodes. You can use kubeconfig to connect to the cluster through the Internet. Not e If you clear the Expose API Server wit h Public SLB check box, you cannot access the cluster API server through the Internet. |

| Parameter | Description |
|---|---|
| SSH logon | If you select this check box, you can use SSH to access the cluster. If you clear this check box, you cannot use SSH or kubectl to access the cluster. |
| Log Service | If you enable Log Service, select an existing project or create a new one. The Log Service plug-in is automatically installed in the cluster. |
| Delet e Prot ect ion | If you select this check box, the cluster cannot be deleted through the console or API operations. |
| RDS Whit elist | Add the IP addresses of nodes to the RDS whitelist. |
| Node Prot ect ion | This check box is selected by default to prevent nodes from being deleted through the console or APIs. |
| Labels | Attach labels to the nodes. |
| Advanced Opt ions | Pods on Each Node: The maximum number of pods that can run on a single node. Cluster Domain: Default is cluster.local. Custom domains are supported. Cluster CA: Set whether to enable custom cluster CA. |

4. Click Creat e Clust er in the upper-right corner.
5. On the Conf irm page, click OK to start the deployment.
Result You can find the newly created cluster on the Clust ers page.

#### 4.2.2 View cluster logs

You can view operation logs through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers. The Clusters page appears.
3. Find the target cluster and click View Logs in the Actions column.
You can view operations performed on the cluster.

#### 4.2.3 Connect to a cluster through kubectl

You can use the Kubernetes command line tool, kubectl, to connect to a Kubernetes cluster from a local computer. Procedure
1. Download the latest kubectl client from the Kubernetes change log page.
2. Install and set up the kubectl client.
For more information, see Install and set up kubectl.
3. Configure the cluster credentials.
You can use the `scp` command to securely copy the master node configuration file from the `/` `etc/kubernetes/kube.conf` directory of the master VM and paste it to the $HOME/.kube/config directory of the local computer, where the `kubectl` credentials are expected to be stored.

```
mkdir $HOME/.kube scp root@<master-public-ip>:/etc/kubernetes/kube.conf $HOME/.kube/config
```

You can find `master-public-ip` on the cluster details page. i. Log on to the Container Service console. ii. In the left-side navigation pane, click Clust ers. The Clusters page appears. iii. Find the target cluster and click Manage in the Actions column. In the Clust er Inf ormat ion section, you can find the master node IP address.

#### 4.2.4 Connect to a master node by using SSH

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

#### 4.2.5 Expand a cluster

You can adjust the number of worker nodes in a cluster based on business needs in the console. Context Currently, you cannot adjust the number of master nodes in a cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Select the target cluster and click Expand in the Actions column.
4. On the Expand page, specify the number of worker nodes.
In this example, increase the number of worker nodes from zero to two.
5. Configure worker nodes.
Inst ance T ype: You can select multiple instance types.
6. Configure node logon settings.
Password: Set the logon password. Conf irm Password: Enter the logon password again.
7. Click Submit .
What's next In the left-side navigation pane, choose Clust ers > Nodes. On the Nodes page, verify that the number of worker nodes is now changed to two.

#### 4.2.6 Renew a certificate

This topic describes how to renew a Kubernetes certificate in the console. Prerequisites You have created a Kubernetes cluster and its certificate is about to expire. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clust ers page appears.
3. Select the target cluster and click Updat e Cert if icat e. The Updat e Cert if icat e page appears.
Not e The Updat e Cert if icat e button will be displayed two months before your cluster certificate expires.
4. Click Updat e and the Conf irm page appears.
5. Click Conf irm.
Result On the Updat e Cert if icat e page, the following message appears: T he cert if icat e has been updat ed. On the Clust ers page, the Updat e Cert if icat e button has disappeared.

#### 4.2.7 Delete a cluster

You can delete clusters in the Container Service console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Find the target cluster and choose More > Delet e in the Actions column.
What's next Resource Orchestration Service (ROS) has no permission to delete resources that were manually added under ROS-created resources. For example, if you manually add a VSwitch under a ROS-created VPC instance, ROS cannot delete the VPC instance and therefore the cluster cannot be deleted. Container Service allows you to force delete clusters. If your first attempt to delete a cluster fails, you can forcibly delete the cluster and ROS stack. However, you still need to manually release the resources that were manually added in the first place. An error message appears when an attempt to delete a cluster fails. Select the cluster that you failed to delete and choose More > Delet e in the Actions column. In the dialog box that appears, you can view the resources that were manually added. Select the Force Delet e check box and click OK to delete the cluster and ROS resource stack.

#### 4.2.8 View cluster overview

The Container Service console provides a cluster overview page. This page displays the information such as application status, component status, and resource monitoring status. This allows you to check the health status of your cluster at your convenience. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Overview. The Overview page appears.
3. Select the target cluster and namespace. You can view the application status, component status,
and resource monitoring charts. Applicat ion St at us: displays the statuses of the deployments, pods, and replica sets that are running in the cluster. Green sections indicate a normal state and yellow sections indicate an exception state. Node St at us: displays the statuses of the nodes in the cluster. Component St at us: Components are deployed in the kube-system namespace. Core components are used, such as the scheduler, controller-manager, and etcd. Event s: displays events such as warnings and errors. If no events are displayed, the cluster is running in the normal state. Monit oring: displays CPU and memory monitoring charts. CPU usage is measured in cores or millicores and accurate to three decimal places. A millicore is one thousandth of a core. Memory usage is measured in GiB and accurate to three decimal places. For more information, see Meaning of CPU and Meaning of memory.

### 4.3 Nodes

#### 4.3.1 Add an existing node

You can add an existing ECS instance to a cluster. Currently, you can only add worker nodes to clusters. Prerequisites You have created a Kubernetes cluster. For more information, see Log on to the Container Service console. You have created an ECS instance. Ensure that the region, zone, department, project, security group, VPC network, and operating system settings of the ECS instance are the same as those of the cluster. Context By default, a cluster can contain up to 50 nodes. To add more nodes to a cluster, submit a ticket. The ECS instance must be in the same region and VPC network as the cluster. The ECS instance must belong to the same account as the cluster. The ECS instance must be running the CentOS operating system. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster and click Add Exist ing Node in the upper-right corner.
4. On the page that appears, you can manually add existing ECS instances to the cluster.
To manually add an ECS instance, you need to obtain the installation command and log on to the ECS instance to run the command. You can only add one ECS instance at a time. i. Select the ECS instance that you want to add and click Next St ep. You can add only one ECS instance at a time. ii. Confirm the instance information and click Next St ep. iii. Copy the command. iv. Click Complet e. v. Go to the ASCM console. In the top navigation bar, choose Product s > Elast ic Comput e Service. On the Inst ances page, select the department and region of the cluster, and then find the target ECS instance. vi. Click the instance name to go to the Instance Details tab. Click Connect t o VNC. In the dialog box that appears, enter the VNC password and then click OK. After you log on to the instance, paste the copied command and click OK to execute the script. vii. When the script execution succeeds, the ECS instance is added to the cluster. You can go to the Clusters page and click the cluster ID to view nodes in the cluster. Check whether the ECS instance has been added to the cluster.

#### 4.3.2 View nodes

You can view the nodes in a cluster through commands, the console, or the Kubernetes Dashboard. Through commands Not e To view the nodes in a cluster through commands, you need to Connect to a Kubernetes cluster through kubectl. Use kubectl to connect to a cluster and run the following command to view the nodes in the cluster.

```bash
kubectl get nodes
```

A sample out put is as f ollows:

```bash
$ kubectl get nodes
    NAME                      STATUS    AGE       VERSION
    iz2ze2n6ep53tch701yh9zz   Ready     19m       v1.6.1-2+ed9e3d33a07093
    iz2zeafr762wibijx39e5az   Ready     7m        v1.6.1-2+ed9e3d33a07093
    iz2zeafr762wibijx39e5bz   Ready     7m        v1.6.1-2+ed9e3d33a07093
    iz2zef4dnn9nos8elyr32kz   Ready     14m       v1.6.1-2+ed9e3d33a07093
    iz2zeitvvo8enoreufstkmz   Ready     11m       v1.6.1-2+ed9e3d33a07093
```

Through the Container Service console
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster to view the nodes in the cluster.
Through the Kubernetes Dashboard
1. Log on to the Container Service console.
2. In the left-side navigation pane, click Clust ers to go to the Clusters page.
3. Select the target cluster and click Dashboard in the Actions column to go to the Kubernetes
Dashboard.
4. In the left-side navigation pane, click Nodes. On the page that appears, you can view all nodes in
the cluster.

#### 4.3.3 Manage node labels

You can manage node labels through the console. You can add a label to multiple nodes at the same time, filter nodes by label, and remove labels. For more information about how to use labels to schedule nodes, see Set node scheduling. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Add a label to multiple nodes
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster and click Manage Labels in the upper-right corner.
4. Select multiple nodes and then click Add Label.
5. In the dialog box that appears, enter the label name and value, and then click OK.
On the Manage Labels page, the selected nodes now have the same label. Remove a label
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster and click Manage Labels in the upper-right corner.
4. Select a node and click the cross sign at the end of a label, for example, `group:worker` .
Click Conf irm to remove the label.

#### 4.3.4 Set node schedulability

Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster and select one or more nodes. Click Set t o Unschedulable.
4. In the dialog box that appears, you can set the specified nodes to either of the following statues:
Set t o Unschedulable: Pods will not be scheduled to this node when you deploy new applications. Set t o Unschedulable and Drain: Pods will not be scheduled to this node when you deploy new applications. Pods on this node will be evicted, except for the pods that are managed by DaemonSets. In this example, Set t o Unschedulable is selected. Click OK. The node status is now changed to Unschedulable. What's next Pods will not be scheduled to the node when you deploy new applications.

#### 4.3.5 Remove a node

To restart or release an ECS node in a cluster, you must remove the node from the cluster first. This topic describes how to remove a node. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You can use kubectl to connect to the Kubernetes cluster. For more information, see Connect to a Kubernetes cluster through kubectl. Context When you remove a node, pods running on the node will be migrated to other nodes, which may cause service interruptions. We recommend that you remove nodes during off-peak hours. Unexpected errors may occur when you remove a node. We recommend that you back up your data in advance. The node that you choose to remove will be set to the unschedulable state. You can only remove worker nodes. Procedure
1. Run the following command to migrate the pods on the target node to other nodes.
Not e Make sure that the other nodes have sufficient resources.

```bash
kubectl drain node-name
```

Not e node-name must be in the format of your-region-name.node-id. your-region-name represents the region where your cluster is deployed. node-id represents the ID of the ECS instance where the target node is deployed. For example, cn-hanghzou.i-xxx.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
3. Select the target cluster. Find the target node and choose More > Remove in the Actions column.
The Remove Node page appears. Not e To remove multiple nodes at the same time, select nodes on the Nodes page and click Bat ch Remove.
4. (Optional)To release the ECS instance where the target node is deployed, select the Release ECS
Inst ance check box. Not e This option only releases pay-as-you-go ECS instances. Subscription ECS instances will be automatically released after the subscription expires. If you do not select the Release ECS Inst ance check box, you will continue to be billed for the ECS instance where the target node is deployed.
5. Click OK to remove the node.

#### 4.3.6 View node resource usage

You can view the resource usage of the nodes in a cluster through the console. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes to go to the Nodes page.
You can view the request and usage rate of CPU and memory on each node. CPU request rate = sum (The amount of CPU requested by all pods on the node) / Total CPU of the node CPU usage rate = sum (The amount of CPU used by all pods on the node) / Total CPU of the node Memory request rate = (The amount of memory requested by all pods on the node) / Total memory of the node Memory usage rate = sum (The amount of memory used by all pods on the node) / Total memory of the node Not e You can adjust the workload of a node based on resource usage. For more information, see Set node scheduling. When the request or usage rate of a node reaches 100%, pods will not be scheduled to the node.

#### 4.3.7 Upgrade the NVIDIA driver on a GPU node

This topic describes how to upgrade the NVIDIA driver on a GPU node when workloads are deployed on the node and when no workload is deployed on the node. Upgrade the NVIDIA driver on a GPU node where workloads are deployed
1. Connect to a Kubernetes cluster through kubectl.
2. Run the following command to set the target node to unschedulable.

```bash
kubectl cordon node-name
```

Not e Currently, you can only upgrade the NVIDIA driver on worker nodes. node-name must be in the format of your-region-name.node-id. your-region-name represents the region where your cluster is deployed. node-id represents the ID of the ECS instance where the target node is deployed. You can run the following command to query node-name.

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
Not e If your driver version is 384.111, perform the following steps. If your driver version is not 384.111, download the corresponding driver from the official NVIDIA website first.

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

#### 4.3.8 Create a Kubernetes cluster for GPU computing

computing This topic describes how to create a Kubernetes cluster for GPU computing. Prerequisites The Container Service for Kubernetes, Resource Orchestration Service (ROS), and Resource Access Management (RAM) services are activated. Not e Container Service for Kubernetes uses ROS to deploy applications in Kubernetes clusters. Before you create a Kubernetes cluster, you must activate ROS. Context Starting from version 1.8, Kubernetes adds support for the following hardware acceleration devices by using device plug-ins: NVIDIA GPUs, InfiniBand devices, and field-programmable gate arrays (FPGAs). GPU solutions developed by the community will be phased out in version 1.10, and removed from the master code in version 1.11. Container Service for Kubernetes enables you to use a GPU-accelerated Kubernetes cluster to run compute-intensive tasks such as machine learning and image processing. You can deploy applications and achieve auto scaling without the need to install NVIDIA drivers or Compute Unified Device Architecture (CUDA) in advance. You must complete the following operations in the Container Service console to create a Kubernetes cluster: Create Elastic Compute Service (ECS) instances, configure a public key to enable SSH logon from master nodes to other nodes, and configure the Kubernetes cluster by using cloud-init. Create a security group that allows access to the Virtual Private Cloud (VPC) network over Internet Control Message Protocol (ICMP). Create a VPC network and a VSwitch and create SNAT rules for the VSwitch if you do not specify an existing VPC network. Create VPC routing rules. Create a NAT gateway and an elastic IP address. Create a RAM user and grant it permissions to query, create, and delete ECS instances and permissions to add and delete cloud disks. The RAM user is also granted all permissions on Server Load Balancer (SLB), Cloud Monitor, VPC, Log Service, and Network Attached Storage (NAS). The Kubernetes cluster dynamically creates SLB instances, cloud disks, and VPC routing rules based on your settings. Create an internal SLB instance and open port 6443. Create a public SLB instance and open ports 6443, 8443, and 22. If you choose to enable SSH logon when you create the cluster, port 22 is enabled. Otherwise, port 22 is not enabled. Limits Kubernetes clusters support only VPC networks. By default, each account has specific quotas on the amount of cloud resources that can be created. You cannot create clusters if the quota limit is exceeded. Make sure that you have sufficient quotas before you create a cluster. To request a quota increase, submit a ticket. You can create up to five clusters across all regions for an account. A cluster can contain up to 40 nodes. To create more clusters or nodes, submit a ticket. Not e In a Kubernetes cluster, you can create up to 48 route entries per VPC. This means that a cluster can contain up to 48 nodes. To increase the number of nodes, submit a ticket to increase the number of route entries first. You can create up to 100 security groups for each account. You can create up to 60 pay-as-you-go SLB instances for each account. You can create up to 20 elastic IP addresses for each account. ECS instances have the following limit: Only CentOS is supported. Create a GN5 Kubernetes cluster GN5 Kubernetes clusters support only Kubernetes 1.12.6-aliyun.1. Kubernetes 1.11.5 is not supported.
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clust ers page appears.
3. In the upper-right corner of the page, click Creat e Kubernet es Clust er. The Creat e Kubernet es
Clust er page appears. You are redirected to the Dedicat ed Kubernet es tab by default. Not e To create a cluster for GPU computing, select ECS instance types with GPU capabilities to create worker nodes. For more information about other parameters, see Create a Kubernetes cluster.
4. Configure worker nodes. In this example, worker nodes are used to run GPU tasks and the gn5i-c4gi1
instance type is seleted. i. If you choose to create worker instances, you must set Instance Type and Quantity. Three worker nodes with GPU capabilities are created in this example. Not e We recommend that you use SSD disks. ii. If you choose to add existing instances, you must create GPU-accelerated instances in the target region in advance.
5. Set the other parameters and click Creat e Clust er to start the deployment.
After the cluster is created, choose Clust ers > Nodes to go to the Nodes page. Select the target cluster. Find one of the created nodes and choose More > Det ails to view the GPU-based devices attached to the node. Create a GPU experimental environment to run TensorFLow Jupyter is a standard tool that is used by data scientists to create the experimental environment to run TensorFlow. The following example shows how to deploy a Jupyter application.
1. In the left-side navigation pane, choose Applicat ions > Deployment s to go to the
Deployment s page.
2. In the upper-right corner of the page, click Creat e f rom T emplat e.
3. Select the target cluster and namespace. Select a sample template, or set Sample Template to
Custom and customize the template in the Template field. Then, you can click Creat e. In this example, a Jupyter application template is implemented. The template includes a deployment and a service.

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
            nvidia.com/gpu: 1                      #Specifies the number of NVIDIA GPUs
that are called by the application.
        ports:
        - containerPort: 8888
          hostPort: 8888
        env:
          - name: PASSWORD                         #Specifies the password used to acce
ss the Jupyter instance. You can modify the password as required.
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
  type: LoadBalancer                           #Creates an SLB service to ensure that t
he Jupyter instance is accessible over the Internet.
```

4. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. Select the
target cluster and namespace. Find the tf-notebook service and check its external endpoint.
5. To connect to the Jupyter instance in a browser, enter `http://EXTERNAL-IP` in the address bar
and enter the password specified in the template.
6. You can run the following program to verify that the Jupyter instance has access to GPU-based
devices. The program lists all devices that can be used by TensorFlow:

```python
from tensorflow.python.client import device_lib def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]
print(get_available_devices())
```

#### 4.3.9 Use labels to schedule pods to GPU nodes

To use Kubernetes clusters for GPU computing, you need to schedule pods to GPU nodes. To make the scheduling more flexible and efficient, you can add labels to GPU nodes. Context When Kubernetes deploys nodes with NVIDIA GPUs, the attributes of these GPUs will be discovered and exposed as node labels, which have the following benefits: You can quickly filter GPU nodes by label. You can use labels as scheduling conditions when you deploy pods. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes. The Nodes page appears.
Not e This example selects a cluster with three worker nodes, among which two are equipped with GPUs. Note the node IP addresses.
3. Select a GPU node and choose More > Det ails in the Actions column to go to Kubernetes
Dashboard. You can view the labels attached to the node. You can also log on to a master node and run the following command to view the labels on GPU nodes:

```bash
# kubectl get nodes
NAME STATUS ROLES AGE VERSION cn-beijing.i-2ze2dy2h9w97v65u**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1
# Compare these nodes with the nodes displayed in the console to identify GPU nodes.
cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1 cn-beijing.i-2ze9xylyn11vop7g**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2zed5sw8snjniq6m**** Ready master 2d v1.12.6-aliyun.1 cn-beijing.i-2zej9s0zijykp9pw**** Ready <none> 2d v1.12.6-aliyun.1
```

Select a GPU node and run the following command to query its labels:

```bash
# kubectl describe node cn-beijing.i-2ze8o1a45qdv5q8a****
Name: cn-beijing.i-2ze8o1a45qdv5q8a7luz Roles: <none> Labels: aliyun.accelerator/nvidia_count=1 # This f ield is important.
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

In this example, the GPU node is attached with the following three labels:

| key | value |
|---|---|
| aliyun.accelerator/nvidia count _ | The number of GPU cores. |
| aliyun.accelerator/nvidia mem _ | The size of the GPU memory in MiB. |
| aliyun.accelerator/nvidia name _ | The name of the NVIDIA graphics card. |

GPU nodes of the same type have the same graphics card name. You can use this label to filter nodes.

```bash
# kubectl get no -l aliyun.accelerator/nvidia_name=Tesla-M40
NAME STATUS ROLES AGE VERSION cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1 cn-beijing.i-2ze8o1a45qdv5q8a**** Ready <none> 2d v1.12.6-aliyun.1
```

4. Go to the homepage of the Container Service console. In the left-side navigation pane, choose
Applicat ions > Deployment s. On the page that appears, click Creat e f rom T emplat e in the upper-right corner. i. Create a TensorFlow deployment and schedule it to a GPU node. This example uses the following YAML template:

```bash
---
# Define the tensorflow deployment
apiVersion: apps/v1 kind: Deployment metadata:
  name: tf-notebook
  labels:
    app: tf-notebook
spec:
  replicas: 1
  selector: # define how the deployment finds the pods it mangages
    matchLabels:
      app: tf-notebook
  template: # define the pods specifications
    metadata:
      labels:
        app: tf-notebook
    spec:
      nodeSelector:                                                  # This field i
s important.
        aliyun.accelerator/nvidia_name: Tesla-M40
      containers:
      - name: tf-notebook
        image: tensorflow/tensorflow:1.4.1-gpu-py3
        resources:
          limits:
            nvidia.com/gpu: 1                                        # This field i
s important.
        ports:
        - containerPort: 8888
          hostPort: 8888
        env:
          - name: PASSWORD
            value: mypassw0rdv
```

ii. You can also avoid deploying an application to a GPU node. The following example deploys an NGINX pod and schedules the pod based on node affinity. For more information, see the part about node affinity in Create an application from an image. This example uses the following YAML template:

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

5. In the left-side navigation pane, choose Applicat ions > Pods. On the page that appears, select
the target cluster and namespace. Result On the Pods page, the two pods from preceding examples have been scheduled to the target nodes. You can use labels to schedule pods to specific GPU nodes with ease.

#### 4.3.10 Manually upgrade the kernel of a GPU node in a cluster

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
Not e This step uninstalls the version 384.111 driver. If your driver version is not 384.111, you need to download a driver from the official NVIDIA website and replace `384.111` with your actual version number. i. Log on to the target GPU node and run the `nvidia-smi` command to query the driver version.

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

### 4.4 Storage

#### 4.4.1 Overview

In the Container Service console, you can create volumes of other Apsara Stack services, enabling you to create stateful applications and use Apsara Stack disks and OSS to implement persistent storage. Both static and dynamic volumes are supported. The following table shows how static and dynamic volumes are supported.

| Apsara Stack storage | Static volume | Dynamic volume |
|---|---|---|
| Apsara Stack disk | You can use a static disk volume through either of the following methods: Use a volume directly Use a volume through a PV and PVC | Supported |
| Apsara Stack NAS | You can use a static NAS volume through either of the following methods: Use a volume through the FlexVolume plug-in Use a volume directly Use a volume through a PV or PVC Use a volume through the Kubernetes NFS driver | Supported |
| Apsara Stack OSS | You can use a static OSS volume through either of the following methods: Use a volume directly Use a volume through a PV or PVC | Not supported |

#### 4.4.2 Use Apsara Stack disks

You can use Apsara Stack disks to create volumes. You can use volumes created from Apsara Stack disks in Kubernetes clusters. Apsara Stack disks can be attached to Kubernetes clusters as the following volume types: Statically provisioned volumes You can use the statically provisioned volumes in either of the following ways: Use a disk as a volume. Create a persistent volume (PV) or a persistent volume claim (PVC). Dynamically provisioned volumes Considerat ions A disk is a non-shared storage device that can only be attached to a single pod at a time. To use a disk as a volume, you must have created the disk and obtained its disk ID. The disk must meet the following capacity requirements: A basic disk must have a minimum capacity of 5 GiB. An ultra disk must have a minimum capacity of 20 GiB. An SSD disk must have a minimum capacity of 20 GiB. volumeId: the ID of the attached disk. The value must be the same as volumeName and PV Name. The node and the disk to be attached must be in the same zone. Only pay-as-you-go disks can be attached to nodes. If you change the billing method of an Elastic Compute Service (ECS) instance in the cluster from pay-as-you-go to subscription, you cannot change the billing method of its disks to subscription. Otherwise, the disks cannot be attached to the cluster. Statically provisioned volumes You can use disks as volumes or by creating PVs and PVCs. Prerequisit es A disk is created in the ECS console. Use a disk as a volume Use the following disk-deploy.yaml file to create a pod.

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

Use a disk t o creat e a PV and a PVC i. Use a disk t o creat e a PV You can create a PV in the console or by using a YAML file. Creat e a PV by using a YAML f ile Use the following `disk-pv.yaml` file to create a PV. Not e The PV name must be the same as the disk ID.

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

Creat e a PV in t he console a. Log on to the Container Service console. b. In the left-side navigation pane, choose Clust ers > Persist ent Volumes to go to the PVs and PVCs page. c. On the Persist ent Volumes tab, select the target cluster and click Creat e in the upperright corner. d. Set the parameters in the Create PV dialog box. PV parameters

| Parameter | Description |
|---|---|
| PV T ype | In this example, Cloud Disk is selected. |
| Volume Plug-in | Flexvolume and CSI are supported. |
| Access Mode | By default, ReadWriteOnce is used. |
| Disk ID | Select a disk that is in the same region and zone as your cluster. |
| File Syst em T ype | Select the file system of the disk. Supported file systems include ext4, ext3, xfs, and vfat. Default value: ext4. |
| Label | Add labels to the PV. |

e. Click Creat e. ii. Creat e a PVC Use the following `disk-pvc.yaml` file to create a PVC:

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

iii. Creat e a pod Use the following disk-pod.yaml file to create a pod.

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

Dynamically provisioned volumes To use a dynamically provisioned volume, you must manually create a StorageClass, and use storageClassName to specify the disk type in a PVC.
1. Creat e a St orageClass

```
kind: StorageClass apiVersion: storage.k8s.io/v1beta1 metadata:
  name: alicloud-disk-common-hangzhou-b
provisioner: alicloud/disk parameters:
  type: cloud_ssd
  regionid: cn-hangzhou
  zoneid: cn-hangzhou-b
```

Parameters provisioner: Set the value to alicloud/disk, which means that the Alibaba Cloud Provisioner plugin is used to create the StorageClass. type: the type of the disk. Valid values: cloud_efficiency, cloud_ssd, and available. If you set this parameter to available, the system will try to create a disk in the following order: ultra disk, SSD disk, and basic disk. The system will stop trying until a disk is created. regionid: the region of the disk. zoneid: the zone of the disk.
2. Creat e a service

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

Def ault opt ions By default, Kubernetes clusters support the following types of StorageClasses: alicloud-disk-efficiency: ultra disk. alicloud-disk-ssd: SSD disk. alicloud-disk-available: This option ensures high availability. The system tries to create an ultra disk first. If no ultra disk is available in the specified zone, the system tries to create an SSD disk.
3. Creat e a mult i-inst ance St at ef ulSet by using a disk
We recommend that you use the volumeClaimTemplates parameter. This allows the system to dynamically create multiple PVCs and PVs. PVCs are associated with PVs and pods.

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

#### 4.4.3 Use NAS volumes

This topic describes how to use Network Attached Storage (NAS) file systems in Kubernetes clusters. NAS file systems can be mounted to Kubernetes clusters as the following volume types: Statically provisioned NAS volumes You can use statically provisioned NAS volumes in the following ways: Use the FlexVolume plug-in Use a NAS file system as a volume Use a NAS file system to create a persistent volume (PV) and a persistent volume claim (PVC) Use the Network File System (NFS) driver of Kubernetes. Dynamically provisioned NAS volumes Prerequisites A NAS file system is created in the NAS console and a mount target is added. The mount target is used to mount the file system to the Kubernetes cluster. The NAS file system and the Kubernetes cluster are deployed in the same Virtual Private Cloud (VPC) network. Statically provisioned NAS volumes You can use the FlexVolume plug-in provided by Alibaba Cloud or the NFS driver provided by Kubernetes to manage NAS file systems. Use t he FlexVolume plug-in The FlexVolume plug-in allows you to use a NAS file system as a volume. You can also use a NAS file system to create a PV and a PVC. Not e NAS is a shared storage system that provides storage services for multiple pods at the same time. server: the mount target of the NAS volume. path: the mounted directory in the NAS file system. You can specify a subdirectory as a volume. If no subdirectory exists, the system automatically creates and mounts a subdirectory. vers: the version of the NFS mounting protocol. Version 4.0 is supported. mode: the access permissions on the mounted directory. If the root directory of the NAS file system is specified as the mounted directory, you cannot modify the access permissions. If the NAS file system stores a large amount of data, the mounting process may take a long time or fail. Therefore, we recommend that you do not set the mode parameter. Use a NAS f ile syst em as a volume Use the following `nas-deploy.yaml` file to create a pod.

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

Use a NAS f ile syst em t o creat e a PV and a PVC St ep 1: Creat e a PV You can use a YAML file or the Container Service console to create a PV. Create a PV by using a YAML file Use the following `nas-pv.yaml` file to create a PV.

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

Create a PV in the console i. Log on to the Container Service console. ii. In the left-side navigation pane, choose Clust ers > Persist ent Volumes. The PVs and PVCs page appears. iii. On the Persist ent Volumes tab, select the target cluster and click Creat e in the upper-right corner. iv. In the Create PV dialog box, set the following parameters: PV T ype: In this example, NAS is selected. Volume Name: the name of the PV. The name must be unique in the cluster. In this example, pv-nas is specified. Volume Plug-in: In this example, Flexvolume is selected. Capacit y: the capacity of the PV. The capacity of the PV cannot exceed that of the NAS file system. Access Mode: The default mode is ReadWriteMany. Mount T arget Domain Name: Enter the address of the mount target that is used to mount the NAS file system to the cluster. Subdirect ory: Enter a subdirectory in the NAS file system. The subdirectory must start with a forward slash (/). If this parameter is set, the specified subdirectory is mounted as the PV. If the specified subdirectory does not exist, the system automatically creates this subdirectory. This parameter is optional. By default, the root directory of the NAS file system is mounted. Permissions: Set the access permissions on the mounted directory, for example, 755, 644, or 777. The permissions can be set only when a subdirectory is mounted as the PV. This parameter is optional. By default, the original permissions are used. chmod (Change Mode): In this example, Non-recursive is selected. Version: The version of the NFS mounting protocol. Version 3 and 4.0 are supported. We recommend that you use the default version 3. Label: Add labels for the PV. v. Click Creat e. St ep 2: Creat e a PVC Use the following nas-pvc.yaml file to create a PVC.

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

St ep 3: Creat e a pod Use the following nas-pod.yaml file to create a pod.

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

Use t he NFS driver St ep 1: Creat e a NAS f ile syst em Log on to the NAS console. For more information, see the Create a file systemchapter ofNAS User Guide. Not e The NAS file system and the Kubernetes cluster must be deployed in the same region. In this example, the following mount target is used: `055f84ad83-ixxxx.cn-`

```
hangzhou.nas.aliyuncs.com .
```

St ep 2: Creat e a PV You can use a YAML template or the Container Service console to create a PV. Creat e a PV by using a YAML t emplat e Use the nas-pv.yaml file to create a PV. Run the following command to create a PV from the NAS file system:

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

Creat e a PV in t he console For more information, see Use a NAS file system to create a PV and a PVC. St ep 3: Creat e a PVC Create a PVC and associate the PVC with the PV that is created in Step 2.

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

St ep 4: Creat e a Pod Create an application to use the PV.

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

The NAS file system is now mounted to the application that runs in the pod. Dynamically provisioned NAS volumes If you want to use dynamically provisioned NAS volumes, install a driver plug-in and configure a NAS mount target. Inst all t he plug-in

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

Use a dynamically provisioned NAS volume

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

#### 4.4.4 Use OSS volumes

You can use OSS buckets to create PVs in Kubernetes clusters. You can use OSS volumes in the following ways: Directly as volumes Through PVs and PVCs Prerequisites You have created a bucket in the OSS console. Background Currently, you can only use static OSS volumes. OSS is a shared storage system that can provide storage services to multiple pods at the same time. bucket: Only buckets can be mounted to a Kubernetes cluster. The subdirectories or files in a bucket cannot be mounted to a Kubernetes cluster. url: The OSS endpoint, namely, the domain that is used to mount an OSS bucket to a cluster. akId: Your AccessKey ID. akSecret: Your AccessKey secret. otherOpts: The custom parameters for mounting an OSS bucket, in the format of `-o *** -o ***` . Not e To use OSS volumes, you must create a secret with your AccessKey information when you deploy the flexvolume service. Use static OSS volumes Use an OSS bucket as a volume Use the following oss-deploy.yaml file to create a pod.

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

Use an OSS bucket t o creat e a PV and a PVC i. Creat e a PV You can create a PV through the console or by using a YAML file. Creat e a PV by using a YAML f ile Use the following oss-pv.yaml file to create a PV.

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

Creat e a PV t hrough t he console a. Log on to the Container Service console. b. In the left-side navigation pane, choose Clust ers > Persist ent Volumes. The PVs and PVCs page appears. c. On the Persist ent Volumes tab, select the target cluster and click Creat e in the upperright corner. d. In the Create PV dialog box, set the following parameters. Create a PV through the console

| Parameter | Description |
|---|---|
| PV T ype | In this example, select OSS. |
| Volume Name | The name of the PV. The name must be unique in the cluster. In this example, enter pv-oss. |
| Volume Plugin-in | Supports Flexvolume and CSI. |
| Capacit y | The capacity of the PV. |
| Access Mode | Default is ReadWriteMany. |
| AccessKey ID and AccessKey Secret | The AccessKey pair is required to access OSS buckets. To obtain your AccessKey pair, go to the ASCM console, choose Ent erprise > Organizat ions, click at the right of the target organization, and click AccessKey. |

| Parameter | Description |   |   |
|---|---|---|---|
| Opt ional Paramet ers | Enter custom parameters in the format of -o *** -o *** . |   |   |
| Bucket ID | The name of the OSS bucket that you want to use. Click Select Bucket . In the dialog box that appears, choose the target bucket and click Select . |   |   |
| Endpoint | We recommend that you choose Int ernal Endpoint . |   |   |
| Label | Add labels to the PV. |   |   |

e. Click Creat e. ii. Creat e a PVC Use the following oss-pvc.yaml file to create a PVC.

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

iii. Creat e a pod Use the following oss-pod.yaml file to create a pod.

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

Use dynamic OSS volumes Currently, dynamic OSS volumes are not supported.

#### 4.4.5 Create a PVC

Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created a PV. This example uses a PV created from a disk. For more information, see Use Apsara Stack disks. By default, PVCs are associated with PVs that have the alicloud-pvname label. PVs created through the Container Service console all have this label. If a PV does not have this label, you need to add the label before you can associate it with a PVC. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Persist ent Volume Claims. The PVs
and PVCs page appears.
3. On the Persist ent Volume Claims tab, select the target cluster and namespace, and click Creat e
in the upper-right corner.
4. In the Create PVC dialog box, set the parameters, and click Creat e.
Source: Select an existing PV or use a storage class. PVC T ype: The same as the types of PVs. Three types, cloud disk, NAS, and OSS, are supported. Name: The name of the PVC. Allocat ion Mode: Currently, only existing volumes are supported. Exist ing Volumes: Select PVs of the same type as the PVC. Capacit y: The claimed usage, which cannot be larger than the total capacity of associated PVs. Not e If your cluster has a PV that is not used, but you cannot find it in the Select PV dialog box, the reason may be that the PV does not have the alicloud-pvname label. If you cannot find available PVs, you can choose Clust ers > Persist ent Volumes in the left-side navigation pane. Find the PV that you want to use and click Manage Labels in the Actions column. You can attach a label to the PV and set the label name to alicloud-pvname and the value to the PV name. By default, the disk ID is used as the PV name if the PV is created from a disk.
5. On the Persistent Volume Claims page, the newly created PVC is now displayed.

#### 4.4.6 Use a PVC

You can use persistent volume claims (PVCs) in your applications. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created a PVC. This example uses a PVC named pvc-disk. For more information, see Create PVCs. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployment s page
appears. In the upper-right corner, click Creat e f rom Image.
3. On the Basic Information page, specify the application name, cluster, namespace, number of
replicas, type, labels, and annotations. Then click Next .
4. On the Container page, select the image. Then, specify the type of cloud volume. Currently, cloud
disks, NAS, and OSS are supported. In this example, select the pvc-disk PVC and click Next .
5. Configure the test-nginx application, and then click Creat e.
6. After the application is created, choose Applicat ions > Pods in the left-side navigation pane.
Select the pod to which the application belongs, and click View Det ails.
7. On the pod details page, click the Volumes tab. Verify that the pod is now associated with the
pvc-disk PVC.

### 4.5 Network management

#### 4.5.1 Set access control for pods

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

#### 4.5.2 Set bandwidth limits for pods

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

### 4.6 Namespaces

#### 4.6.1 Create a namespace

You can create a namespace in the console. Prerequisites You have created a Kubernetes cluster. Context In a Kubernetes cluster, you can use namespaces to create multiple virtual spaces. When a large number of users share a cluster, you can use namespaces to divide different workspaces and allocate cluster resources to different tasks. Furthermore, you can use resource quotas to allocate resources to each namespace. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Namespaces. The Namespaces page appears.
3. Select the target cluster and click Creat e in the upper-right corner.
4. In the dialog box that appears, set the parameters.
Create a namespace

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Name | Enter a name for the namespace. In this example, enter test. The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). It must start and end with a letter or digit. |
| Label | Label: Add one or more labels to the namespace. Labels are used to add marks to namespaces. For example, you can use a label to mark the namespace as one used in the test environment. Enter a variable key and value. Then click Add on the right to add a label. |

5. Click OK.
6. The newly created namespace is now displayed on the Namespaces page.

#### 4.6.2 Set resource quotas and limits

You can set resource quotas and limits for a namespace in the console. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created the sample namespace t est . For more information, see Create a namespace. You can connect to a master node of the cluster. For more information, see Connect to a Kubernetes cluster through kubectl. Context By default, a running pod uses the CPU and memory resources of a node without limit. This means that any pod can use the computing resources of a cluster without restraints. Therefore, pods of a namespace may deplete the cluster resources. Namespaces can be used as virtual clusters to serve multiple purposes and meet different needs. We recommend that you set resource quotas for all namespaces. For a namespace, you can set quotas on resources such as CPU, memory, and pod quantity. For more information, see Resource Quotas. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Namespaces. On the Namespaces page,
select the target cluster. Find the target namespace and click Resource Quot as and Limit s in the Actions column.
3. In the dialog box that appears, set resource quotas and default resource limits.
Not e After you set CPU and memory quotas for a namespace, you must specify CPU and memory limits when you create a pod. Alternatively, you can set the default resource limits for the namespace. For more information, see Resource Quotas. i. Set resource quotas for the namespace. ii. You can set resource limits and resource requests for containers in the namespace. This enables you to control the amount of resources consumed by containers. For more information, see https://kubernetes.io//memory-default-namespace/.
4. After you set resource quotas and limits, connect to a master node of the cluster and run the
following commands to query the resource configurations of the namespace.

```bash
# kubectl get limitrange,ResourceQuota -n test
NAME AGE limitrange/limits 8m NAME AGE resourcequota/quota 8m
# kubectl describe limitrange/limits resourcequota/quota -n test
Name: limits Namespace: test Type Resource Min Max Default Request Default Limit Max Limit/Request Ratio ---- -------- --- --- --------------- ------------- ----------------------- Container cpu - - 100m 500m - Container memory - - 256Mi 512Mi - Name: quota Namespace: test Resource Used Hard -------- ---- ---configmaps 0 100 limits.cpu 0 2 limits.memory 0 4Gi persistentvolumeclaims 0 50 pods 0 50 requests.storage 0 1Ti secrets 1 10 services 0 20 services.loadbalancers 0 5
```

#### 4.6.3 Edit a namespace

You can edit an existing namespace. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created the sample namespace t est . For more information, see Create a namespace. Context When you edit a namespace, you can add, delete, or modify namespace labels based on needs. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Namespaces. The Namespaces page appears.
3. Select the target cluster. Find the namespace that you want to edit and click Edit in the Actions
column.
4. In the dialog box that appears, select a label and click Edit to modify its key and value. This
example changes a label to `env:test-V2` . Then click Save.
5. Click OK. Go to the Namespaces page and check the newly edited namespace label.

#### 4.6.4 Delete a namespace

You can delete namespaces that are no longer in use. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created the sample namespace t est . For more information, see Create a namespace. Context Not e When you delete a namespace, all resource objects under the namespace will be deleted. Exercise caution when you perform this operation. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Namespaces. The Namespaces page appears.
3. Select the target cluster. Find the namespace that you want to delete and click Delet e in the
Actions column.
4. In the dialog box that appears, click Conf irm.
5. The namespace is now deleted from the Namespaces page. Resource objects under the
namespace are also deleted.

### 4.7 Applications

#### 4.7.1 Create an application from an image

You can use an image to create an NGINX application that is accessible over the Internet. Prerequisites A Kubernetes cluster is created. For more information, see Create a Kubernetes cluster. Your Kubernetes cluster is accessible over the Internet. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s to go to the Deployments
page. Then, click Creat e f rom Image in the upper-right corner of the page.
3. In the dialog box that appears, set the parameters, including Name, Clust er, Namespace,
Replicas, and T ype, and select Synchronize T imezone. Click Next . If you do not set the Namespace parameter, the default namespace is used.
4. Configure containers.
Not e You can configure multiple containers for the pods of the application. i. Configure general settings. Container general settings

| Parameter | Description |
|---|---|
| Image Name | You can click Select Image, and in the dialog box that appears, select the required image and click OK. In this example, NGINX is selected. You can also enter a private registry URL to specify the image. The registry URL follows this format: domainname/namespace/imagename . |
| Image Version | You can click Select Image Version to select the required version. If you do not specify the image version, the latest version is used. |
| Always Pull Images | To improve efficiency, Container Service caches images. During the deployment, if the version of the specified image is the same as that of a cached image, Container Service will reuse the cached image instead of pulling the image again. Therefore, when you update the application code, if you do not change the image version for reasons such as to support the upper-layer workloads, the previously cached image will be used. When this check box is selected, Container Service will always pull the image from the repository to deploy the application. This ensures that the latest image and code are used. |
| Set Image Pull Secret | Click Set Image Pull Secret to set the secret. The secret is required if you need to access a private repository. |
| Resource Limit | The upper limits of CPU and memory resources that are available to this application. This prevents the application from occupying excessive resources. The unit of CPU resources is Core. The unit of memory is MiB. |
| Required Resources | The amount of CPU and memory resources that are reserved for this application. These resources are exclusive to the container. This prevents the application from being unavailable if other services or processes share the resources. |
| Cont ainer St art Paramet er | Select st din to enable standard inputs for the container. Select t t y to assign a virtual terminal that is used to send signals to the container. We recommend that you select both check boxes. This allows you to associate the terminal (tty) with the standard inputs (stdin) of the container. For example, an interactive program can be used to obtain standard inputs from users and then display the inputs on the terminal. |
| Init Cont ainer | When this check box is selected, the system creates an Init Container that contains useful tools. For more information, see . |

ii. (Optional)Set environment variables. You can use key-value pairs to set environment variables for pods. Environment variables are used to apply pod configurations to containers. For more information, see Pod variable. iii. (Optional)Configure health check settings. Health check settings include liveness and readiness probes. Liveness probes determine when to restart the container. Readiness probes determine whether the container is ready to start accepting traffic. For more information about health checks, see .

| Request type | Description |
|---|---|

| Request type | Description |
|---|---|
| HT T P request | Sends an HTTP GET request to the container. Supported parameters include: Protocol: HTTP or HTTPS. Path: the requested path on the server. Port: the port opened in the container. The port number must range from 1 to 65535. HTTP Header: The custom headers in the HTTP request. Duplicate headers are allowed. Key-value pairs are supported. Initial Delay (s): the init ialDelaySeconds field, which specifies the period between when the container is started and when the system performs the first probe. Unit: seconds. Default value: 3. Period (s): the periodSeconds field, which specifies the intervals between two adjacent probes. Unit: seconds. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field, which specifies the period after which a probe times out. Unit: seconds. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of consecutive successes that must occur for a probe to be considered successful after having failed. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of consecutive failures that must occur for a probe to be considered failed after having succeeded. Default value: 3. Minimum value: 1. |

| Request type | Description |
|---|---|
| T CP connect ion | Sends a TCP socket to the container. The kubelet will attempt to open the socket on the specified port. If the connection can be established, the container is considered healthy. Otherwise, it is considered unhealthy. Supported parameters include: Port: the port opened in the container. The port number must range from 1 to 65535. Initial Delay (s): the init ialDelaySeconds field, which specifies the period between when the container is started and when the system performs the first probe. Unit: seconds. Default value: 15. Period (s): the periodSeconds field, which specifies the intervals between two adjacent probes. Unit: seconds. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field, which specifies the period after which a probe times out. Unit: seconds. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of consecutive successes that must occur for a probe to be considered successful after having failed. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of consecutive failures that must occur for a probe to be considered failed after having succeeded. Default value: 3. Minimum value: 1. |
| Command line | Runs a probe command in the container to check its health status. Supported parameters include: Command: the probe command that is used to check the health status of the container. Initial Delay (s): the init ialDelaySeconds field, which specifies the period between when the container is started and when the system performs the first probe. Unit: seconds. Default value: 15. Period (s): the periodSeconds field, which specifies the intervals between two adjacent probes. Unit: seconds. Default value: 10. Minimum value: 1. Timeout (s): the t imeout Seconds field, which specifies the period after which a probe times out. Unit: seconds. Default value: 1. Minimum value: 1. Healthy Threshold: the minimum number of consecutive successes that must occur for a probe to be considered successful after having failed. Default value: 1. Minimum value: 1. For liveness probes, this parameter must be set to 1. Unhealthy Threshold: the minimum number of consecutive failures that must occur for a probe to be considered failed after having succeeded. Default value: 3. Minimum value: 1. |

iv. Configure lifecycle events. You can set the following parameters to configure the lifecycle of the container in the Start, Post Start, and Pre Stop fields. For more information, visit https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/. St art : the pre-start command and parameter. Post St art : the post-start command. Pre St op: the pre-stop command. v. (Optional)Configure volumes. Local storage and cloud storage are supported. Local St orage: supports hostPaths, ConfigMaps, secrets, and temporary directories, and mounts a mount source to the specified path in the container. For more information, see Volumes. Cloud St orage: supports three types of persistent volumes (PVs): cloud disks, Network Attached Storage (NAS), and Object Storage Service (OSS). In this example, a PV is created from a cloud disk, and the PV is mounted to the /tmp path in the container. Data generated in this path is stored in the cloud disk. vi. (Optional)Configure Log Service. You can configure collection methods and custom tags. Not e Make sure that the Log Service agent is installed in the cluster. Log collection parameters include: Logst ore: the Logstore that is used to store log data in Log Service. Log Pat h in Cont ainer: You can set this parameter to stdout or a log path. st dout : collects standard outputs of the container. Log Pat h: collects logs in the specified path of the container. In this example, logs in the following path are collected: /var/log/nginx. Wildcards are supported. You can also set custom tags, which will be collected and output along with logs. Custom tags simplify statistical analysis of log data.
5. Set other parameters based on your needs and click Next .
6. Configure advanced settings, including the access control settings.
You can configure the method to access pods and click Creat e to create the application. In this example, a service of the Cluster IP type and an Ingress are created to enable Internet access to the NGINX application. Not e You can configure access control settings based on your needs: Internal applications: For applications that run inside the cluster, you can create a service of the Cluster IP or Node Port type to enable internal communication to fit your needs. External applications: For applications that need to be accessed over the Internet, you can configure access control settings by using one of the following methods: Create a service of the Server Load Balancer (SLB) type and enable access to your application over the Internet by using the SLB instance. Create a service of the Cluster IP or Node Port type, create an Ingress, and then enable access to your application over the Internet by using the Ingress. For more information, see . i. To create a service, click Creat e in the Service section. In the dialog box that appears, configure the service and click Creat e.

| Parameter | Description |
|---|---|
| Name | Enter a name for the service. Default value: applicationname-svc . |

| Parameter | Description |
|---|---|
| T ype | Select one of the following types: Cluster IP: enables access to the service through an internal IP address of the cluster. If you select this type, the service is only accessible within the cluster. Node Port: enables access to the service through the IP address and static port on each node. The NodePort field specifies the static port. A NodePort service can be used to route requests to a Cluster IP service. The system automatically creates the Cluster IP service. You can access a Node Port service from outside the cluster by requesting <NodeIP>:<NodePort> . Server Load Balancer: enables access to the service by using an SLB instance over the Internet or an internal network. The SLB instance can route requests to Node Port and Cluster IP services. |
| Port Mapping | Set a service port and a container port. If the T ype parameter is set to Node Port, you must set a node port to avoid port conflicts. TCP and UDP protocols are supported. |
| Annot at ions | Add annotations to the service. SLB parameters are supported. For more information, see Access services by using SLB. |
| Label | Add labels to the service. |

ii. To create an Ingress, click Creat e in the Ingress section. In the dialog box that appears, configure Ingress rules and click Creat e. For more information about Ingress configuration, see Ingress configurations. When you create an application from an image, you can create an Ingress for only one service. In this example, a virtual host name is used as the test domain. You must add the following entry to the hosts file to map the domain to the IP address of the Ingress. In actual scenarios, use a domain that has obtained an ICP number.

```
101.37.224.146 foo.bar.com #The IP address of the Ingress.
```

iii. You can find the newly created service and Ingress in the Access Control section. You can click Updat e or Delet e to make changes.
7. Click Creat e.
8. After the application is created, a message appears to display the resource objects included in the
application. You can click View Det ails to view application details. The nginx-deployment page is displayed by default.
9. In the left-side navigation pane, choose Ingresses and Load Balancing > Ingresses. The
following rule is displayed on the Ingresses page.
10. Enter the test domain in the address bar of your browser and press the Enter key. The NGINX
welcome page appears.

#### 4.7.2 Create an application from an orchestration template

orchestration template Container Service provides orchestration templates that you can use to create applications quickly. You can also modify the templates based on YAML syntax to customize applications. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Context The following example demonstrates how to create an NGINX application consisting of a deployment and a service. The service is associated with a pod created by the deployment. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployment s page
appears.
3. In the upper-right corner, click Creat e f rom T emplat e.
4. Set the parameters and click Creat e.
Clust er: Select the cluster where the resource objects are to be deployed. Namespace: Select the namespace to which the resource objects belong. The default namespace is default. Except for underlying computing resources such as nodes and PVs, most resources are scoped to namespaces. Sample T emplat e: Container Service provides YAML templates of various resource types to help you deploy resource objects quickly. You can also create a custom template based on YAML syntax to describe the resource that you want to define. Add Deployment : This feature allows you to quickly define a YAML template. Use Exist ing T emplat e: You can import an existing template to the configuration page. Based on an orchestration template provided by Container Service, the following sample template creates a deployment of an NGINX application. Not e Container Service supports YAML syntax. You can use the `---` symbol to separate multiple resource objects. This enables you to create multiple resource objects in a single template.

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
   type: LoadBalancer        ## This example changes the service type from NodePort to
LoadBalancer.
```

5. Click Creat e. A message appears indicating the deployment status.
In the left-side navigation pane, choose Ingresses and Load Balancing > Services to view the newly created service.
6. On Kubernetes Dashboard, verify that a my-service1 service is running and its external endpoint is
displayed. Click the address in the Ext ernal Endpoint column.
7. You can visit the NGINX welcome page in the browser.
What's next You can also choose Ingresses and Load Balancing > Services in the left-side navigation pane to view the NGINX service.

#### 4.7.3 Create an application through Kubernetes Dashboard

Dashboard You can create an application through Kubernetes Dashboard. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Find the target cluster and click Dashboard in the Actions column to go to Kubernetes Dashboard.
4. On the Overview page, click CREAT E in the upper-right corner.
5. In the dialog box that appears, configure the application.
You can use one of the following methods to create the application. CREAT E FROM T EXT INPUT : Directly enter an orchestration template in YAML or JSON format to create the application. A sample template in YAML format is provided as follows: CREAT E FROM FILE: Import a YAML or JSON configuration file to create the application. CREAT E AN APP: Set parameters to create the application. Application parameters

| Parameter | Description |
|---|---|
| App name | The name of the application. In this example, enter nginx . |
| Cont ainer image | The URL of the image. In this example, a Docker NGINX image is used. |
| Number of pods | The number of pods that constitute the application. |
| Service | Valid values: Ext ernal and Int ernal. Ext ernal: Create a service that is accessible from outside the cluster. Int ernal: Create a service that is accessible within the cluster. |
| Advanced opt ions | Click SHOW ADVANCED OPT IONS to set labels and environment variables. The following setting distributes traffic to three pods based on load balancing. |

6. Click DEPLOY to deploy the pods and service.
You can also click SHOW ADVANCED OPT IONS to configure other parameters. What's next After you click DEPLOY, you can click the left-side navigation pane to view the service or pods that constitute the application. In the left-side navigation pane, click Pods. The icon on the left side of each pod indicates the status of the pod. indicates that the pod is being deployed. indicates that the pod has been successfully deployed. indicates that an error occurred while deploying the pod.

#### 4.7.4 Use commands to manage applications

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

#### 4.7.5 Create a service

You can create a service for your application through the Container Service console. The service provides access to the application. A Kubernetes service, generally known as microservice, is an abstraction which defines a logical set of pods and a policy by which to access the pods. A label selector usually determines whether the set of pods can be accessed by the service. Each pod has its own IP address. Pods are created and deleted dynamically and quickly. Using pods to provide services externally is therefore not a highly available solution. The service abstraction enables the decoupling between the frontend and the backend. The frontend does not need to be aware of how the backend is implemented, which leads to a loosely coupled microservices based architecture. For more information, see Kubernetes service. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Step 1: Create a deployment
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. In the upper-right corner,
click Creat e f rom T emplat e.
3. Select the target cluster and namespace. Set the Sample Template field to Custom and enter the
following code in the Template field. Then click Creat e. In this example, the template of an NGINX deployment is used.

```
apiVersion: apps/v1beta2 # for versions before 1.8.0 use apps/v1beta1 kind: Deployment metadata:
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
       containers:
       - name: nginx
         image: nginx:1.7.9                # replace it with your exactly <image_name:t
ags>
         ports:
         - containerPort: 80               ##expose this port in the service
```

4. Click Kubernet es Dashboard to view the status of the deployment.
Step 2: Create a service
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. The Services
page appears.
3. Select the target cluster and namespace. Then click Creat e in the upper-right corner.
4. In the Create Service dialog box that appears, set the following parameters.
Name: The name of the service. In this example, enter nginx-svc. T ype: The type of the service, namely, how to expose the service. Cluster IP: Exposes the service through an internal IP address in the cluster. When this option is selected, the service is only accessible within the cluster. This is the default service type. Node Port: Exposes the service through the IP address and static port (NodePort) of each node. A NodePort service can route requests to a Cluster IP service, which is automatically created by the system. You can access a Node Port service from outside the cluster by requesting `<NodeIP>:<NodePort>` . Server Load Balancer: Exposes the service through an SLB instance, which supports Internet access or internal access. An SLB service can route requests to Node Port and Cluster IP services. Backend: The backend object that you want to associate with the service. In this example, select nginx-deployment-basic created from the previous step. If you do not specify a deployment, no Endpoint object will be created. You can manually bind the service to an Endpoint object. For more information, see services-without-selectors. Port Mapping: Set the service port and container port. The container port must be the same as the one exposed by the backend pod. Annot at ions: Add one or more annotations to the service to configure SLB parameters. For example, set the name to `service.beta.kubernetes.io` and value to `20` . This means that the maximum bandwidth of the service is 20 Mbit/s. For more information, see Access services by using SLB. Label: Add labels to the service.
5. Click Creat e. Service nginx-svc is displayed on the Services page.
6. You can view basic information about the service. You can also access its external endpoint
through a browser. You have created a service and associated it with a backend deployment. You can now visit the NGINX welcome page.

#### 4.7.6 Scale a service

After an application is created, you can scale in or scale out the service based on your needs. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Find the target cluster and click Dashboard in the Actions column to go to Kubernetes Dashboard.
4. In the left-side navigation pane, click Deployment s.
5. Find the target application, click the More icon on the right, and choose Scale.
6. In the dialog box that appears, change the Desired number of pods to 2. Then, click OK.
This action adds a new pod and increases the number of replicas to two. What's next The icon on the left side of each Kubernetes object indicates the status of the object. indicates that the object is being deployed. indicates that the object has been successfully deployed. After a deployment is complete, you can click the deployment name to view details of the running web services. You can view the replica sets included in the deployment, and the CPU and memory usage of these replica sets. You can also click to view container logs. Not e If no resources are displayed, wait a few minutes and then refresh the page.

#### 4.7.7 View a service

You can view details about a service through the Container Service console. Context If an external service is configured when you create an application, Kubernetes Dashboard creates the external service and preconfigures the SLB instance to direct traffic to containers in the cluster. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. The Services
page appears.
3. Select the target cluster and namespace. Find the target service and click Det ails in the Actions
column.
4. (Optional)You can also go to Kubernetes Dashboard. In the left-side navigation pane, click
Services to view all services.

#### 4.7.8 Update a service

You can update a service through the Container Service console. Update a service through the Services page
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. The Services
page appears.
3. Select the target cluster and namespace. Find the target service and click Updat e in the Actions
column. In this example, the target service is nginx-svc.
4. In the dialog box that appears, modify the configurations based on your needs and click Updat e.
5. Find the service on the Services page and click Det ails in the Actions column to view configuration
changes. In this example, the label of the service is updated. Update a service through Kubernetes Dashboard
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers. The Clusters page appears.
3. Find the target cluster and click Dashboard in the Actions column.
4. On Kubernetes Dashboard, select the target namespace and click Services in the left-side
navigation pane.
5. Find the target service, click the More icon on the right, and choose View/edit YAML.
6. In the dialog box that appears, modify the configurations. For example, change nodePort to `3100`
`0` . Then click UPDAT E.

#### 4.7.9 Delete a service

Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created a service. For more information, see Create Servcies. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Services. The Services
page appears.
3. Select the target cluster and namespace. Find the target service and click Delet e in the Actions
column. In this example, the target service is nginx-svc.
4. In the dialog box that appears, click Conf irm. The target service is deleted and disappears from
the Services page.

#### 4.7.10 Create a trigger on an application

Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. You have created an application based on which the trigger is created and tested. In this example, an NGINX application is created. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. On the Deployment s
page that appears, select the target cluster and namespace. Then find the NGINX application and click Det ails in the Actions column.
3. On the application details page that appears, click Creat e T rigger in the Trigger section.
4. In the dialog box that appears, set Action to Redeploy and click OK.
Not e Currently, you can only create a trigger to redeploy the application. After the trigger is created, a trigger link address is displayed in the Trigger section on the Deployment nginx page.
5. Copy the link and open it in your browser. A message appears, displaying information such as the
request ID.
6. Go to the Deployment nginx page. A new pod is displayed on the Pods tab.
After the new pod is successfully deployed, the old pod will be automatically deleted. What's next You can call triggers through GET or POST requests from a third-party system. For example, you can run curl commands to call triggers. To call the redeploy trigger, run the following command:

```bash
 curl https://cs.console.aliyun.com/hook/trigger?token=xxxxxxx
```

#### 4.7.11 View pods

You can view pods through the console. View pods on the Pods page
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Pods. The Pods page appears.
3. Select the target cluster and namespace. Find the target pod and click View Det ails.
Not e You can update or delete pods on the Pods page. We recommend that you use deployments to manage pods if they were created by deployments.
4. On the pod details page, you can view detailed information about the pod.
View pods through Kubernetes Dashboard
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Find the target cluster and click Dashboard in the Actions column. The Kubernetes Dashboard
page appears.
4. In the left-side navigation pane, click Pods to view pods of the cluster.
You can also click Services in the left-side navigation pane and then click a service name to view pods of the service.
5. The icon at the left side of each pod indicates the status of the pod.
indicates that the pod is being deployed. indicates that the pod has been successfully deployed.
6. Select a pod and click its name to view pod details, including the CPU and memory usage.
7. Select a pod and click
at the right to view logs.
8. You can also click the More icon and click Delet e to delete the pod.

#### 4.7.12 Simplify Kubernetes application deployment by using Helm

deployment by using Helm This topic introduces the basic concepts and components of Helm and describes how to use Helm to deploy the sample applications WordPress and Spark in a Container Service for Kubernetes cluster. Prerequisites A Kubernetes cluster is created in the Container Service console. For more information, see Create a Kubernetes cluster. Tiller is automatically deployed to the cluster when the Kubernetes cluster is created. The Helm command-line interface (CLI) is automatically installed on each master node. You must configure the Helm CLI to point to the Alibaba Cloud chart repository. The supported Kubernetes version is used. Only Kubernetes 1.8.4 and later versions are supported. For Kubernetes 1.8.1, you can upgrade the cluster to the required version. To upgrade the cluster, log on to the Container Service console, go to the Clusters page, find the cluster, and then choose More > Upgrade Clust er in the Actions column for the cluster. Context When you run and manage applications with Kubernetes, you can use Helm as the package manager to simplify application distribution and deployment. The Helm project enables consist software packaging and supports version control. In the Container Service console, the App Catalog feature integrates the Helm binaries and supports the Alibaba Cloud chart repository. This allows you to easily deploy applications by using the Helm CLI or in the Container Service console. Overview Helm is an open source tool that is created by Deis. It can be used to simplify the deployment and management of Kubernetes applications. Helm works as a Kubernetes package manager and allows you to discover, share, and run applications that are created in Kubernetes. When you use Helm, you must understand the following basic concepts: Chart: a packaging format used by Helm. Each chart contains the images, dependencies, and resource definitions that are required for running an application. A chart may contain service definitions in a Kubernetes cluster. You can use a chart in a similar way as you use a Homebrew formula, the dpkg packages manager of the Advanced Package Tool (APT) package management system, or the Red Hat Package Manager (RPM) package for Yellowdog Updater, Modified (YUM). Release: an instance of a chart that runs in a Kubernetes cluster. A chart can be installed many times into the same cluster. After a chart is installed, a new release is created. For example, you can install a MySQL chart. If you want to run two databases in your cluster, you can install the MySQL chart twice. Each installation generates a release with a release name. Repository: the location where charts are stored and released. Helm components Helm works in a client-server architecture and consists of the following components: The Helm CLI is the Helm client that runs on your on-premises computer or on the master nodes of a Kubernetes cluster. Tiller is the server-side component and runs on a Kubernetes cluster. Tiller manages the lifecycles of Kubernetes applications. A repository is used to store charts. The Helm client can access the index file and packaged charts in a chart repository over HTTP. Deploy an application in the Container Service console
2. In the left-side navigation pane, choose Market place > App Cat alog to go to the App Catalog
page.
3. Click a chart, for example, WordPress, to go to the page that shows the details of the chart.
4. In the Deploy section on the right of the page, enter the basic information for the deployment.
Clust er: Select the cluster to which you want to deploy the application. Namespace: Select a namespace for the application. By default, this parameter is set to default. Release Name: Enter a release name for the application.
5. Click the Paramet ers tab to set the parameters.
In this example, a dynamically provisioned volume is associated with a persistent volume claim (PVC). For more information, see Use Apsara Stack disks. Not e Before the association, you must create a persistent volume (PV) as the dynamic volume. The capacity of the PV cannot be less than the value defined by the PVC.
6. After you set the parameters, click Creat e to deploy the application. After the application is
deployed, you are navigated to the release page of the application.
7. In the left-side navigation pane, choose Ingresses and Load Balancing > Services, select the
target cluster and namespace, and then find the required service from the list of services. In the External Endpoint column for the service, you can see the external HTTP and HTTPS endpoints.
8. Click either of the endpoints to go to the WordPress application where you can publish blog posts.
Deploy an application by using the Helm CLI After the Helm CLI is automatically installed on the master node of the Kubernetes cluster and points to the required repository, you can log on to the master node by using SSH. This allows you to deploy applications by using the Helm CLI. For more information, see Connect to a master node through SSH. You can also install and configure the Helm CLI and kubectl on your on-premises computer. In this example, on your on-premises computer, the Helm CLI and kubectl are installed and configured and the WordPress and Spark applications are deployed.
1. Install and configure the Helm CLI and kubectl.
i. Install and configure kubectl on your on-premises computer. For more information, see Connect to a Kubernetes cluster through kubectl. To view the information of the target Kubernetes cluster, on the command line, enter `kubect`

```
l cluster-info .
```

ii. Install Helm on your on-premises computer. For more information, see Install Helm.
2. Deploy the WordPress application.
To deploy a WordPress blog website by using Helm, perform the following steps: i. On the command line, run the following command:

```
helm install --name wordpress-test stable/wordpress
```

Not e Container Service for Kubernetes allows you to use block storage or disks as dynamically provisioned volumes. Before you deploy the WordPress application, you must create dynamically provisioned volumes based on disks. The following example shows the output:

```
NAME: wordpress-test LAST DEPLOYED: Mon Nov 20 19:01:55 2017 NAMESPACE: default STATUS: DEPLOYED ...
```

ii. On the command line, run the following commands to view the release and service of WordPress.

```bash
helm list kubectl get svc
```

iii. On the command line, run the following command to view the pod that is associated with the WordPress application. The pod may take a few minutes to change to the running state.

```bash
kubectl get pod
```

iv. On the command line, run the following command to obtain the endpoint of the WordPress application.

```
echo http://$(kubectl get svc wordpress-test-wordpress -o jsonpath='{.status.loadBa lancer.ingress[0].ip}')
```

You can enter the preceding endpoint in your browser to access the WordPress application. You can also follow the chart instructions described in the console and run the following commands to obtain the administrator account and password of the WordPress application:

```
echo Username: user echo Password: $(kubectl get secret --namespace default wordpress-test-wordpress -o jsonpath="{.data.wordpress-password}" | base64 --decode)
```

v. On the command line, run the following command to delete the WordPress application:

```
helm delete --purge wordpress-test
```

Use a third-party chart repository You can use the default Alibaba Cloud chart repository. You can also use a third-party chart repository if the third-party chart repository is accessible. On the command line, run the following command to add a third-party chart repository:

```
helm repo add Repository name Repository URL helm repo update
```

For more information about Helm commands, see Helm documentation. References The Kubernetes community has experienced rapid technological developments based on Helm. These developments have allowed software providers, such as Bitnami, to offer high-quality charts. For more information about available charts, visit `https://kubeapps.com/` .

#### 4.7.13 Schedule pods to nodes

You can add labels to nodes and then configure `nodeSelector` to schedule pods to specific nodes. For more information about how nodeSelector works, see nodeselector. To meet business needs, you may need to deploy a management service on a master node, or deploy certain services on nodes with SSD storage. You can use the following method to schedule pods to specific nodes based on needs. Prerequisites You have created a Kubernetes cluster. For more information, see Create a Kubernetes cluster. Step 1: Add a label to a node
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Nodes. The Nodes page appears.
3. Select the target cluster and click Manage Labels in the upper-right corner.
4. Select one or more nodes and then click Add Label. In this example, select a worker node.
5. In the dialog box that appears, enter the label name and value, and then click OK.
On the Manage Labels page, you can find the `group:worker` label next to the selected node. You can also use the following command to add a label to a node: `kubectl label nodes <node-name>`

```xml
<label-key>=<label-value> .
```

Step 2: Schedule a pod to the node
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployment s page
appears.
3. In the upper-right corner, click Creat e f rom T emplat e.
4. Configure the template to create a pod and schedule it to the node from step 1. Then, click
Creat e. Clust er: Select the cluster where the pod is deployed. Namespace: Select the namespace where the pod belongs. In this example, select the default namespace. Sample T emplat e: In this example, select Custom. Enter the following template content:

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
     group: worker  ##This value must be the same as the label of the node from step 1.
 status: {}
```

5. Click Creat e. A message appears indicating the deployment status. After the pod is created, click
Kubernet es Dashboard to check the status of hello-pod.

### 4.8 SLB and Ingress

#### 4.8.1 Overview

Container Service allows you to flexibly manage load balancing and customize load balancing policies for Kubernetes clusters. Kubernetes clusters provide you with a variety of methods to access containerized applications. They also allow you to use SLB or Ingress to access internal services and implement load balancing.

#### 4.8.2 Access a service through SLB

You can access a service through Server Load Balancer (SLB). Use the CLI
1. Create an NGINX application by using the CLI.

```
root@master # kubectl run nginx --image=registry.aliyuncs.com/acs/netdia:latest
       root@master # kubectl get po
       NAME                                   READY     STATUS    RESTARTS   AGE
       nginx-2721357637-dvwq3                 1/1       Running   1          6s
```

2. Create a service of the Server Load Balancer type for the NGINX application. Set `type=LoadBalance`

| r to expose the NGINX application to the Internet. |   |
|---|---|
|   | root@master # kubectl expose deployment nginx --port=80 --target-port=80 --type=LoadBal ancer root@master # kubectl get svc NAME CLUSTER-IP EXTERNAL-IP PORT(S) AGE nginx 172.19.XX.XX 101.37.XX.XX 80:31891/TCP 4s |

3. Visit `http://101.37.XX.XX` in a browser to access the NGINX application.
Use the Kubernetes Dashboard
1. Create an `nginx-svc.yml` file with the following code on a local computer.

```
apiVersion: v1 kind: Service metadata:
  labels:
    run: nginx
  name: http-svc
  namespace: default
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    run: nginx
  type: LoadBalancer
```

2. Log on to the Container Service console.
3. Select the target cluster and click Dashboard in the Actions column to go to the Kubernetes
Dashboard.
4. Click Creat e in the upper-right corner to create an application.
5. Click the CREAT E FROM FILE tab. Select file nginx-svc.yml.
6. Click UPLOAD.
This creates an `http-svc` service of the Server Load Balancer type and associates the service with the NGINX application.
7. In the left-side navigation pane, select the default namespace and click Services.
You can find the newly created service `http-svc` and its external endpoint `http://114.55.XX.X` `X:80` .
8. Enter the endpoint in a browser to access the service.
See also Server Load Balancer provides a variety of parameters that you can use to configure settings such as health check, billing method, and SLB instance type. For more information, see . Annotations You can add annotations to use the features provided by Server Load Balancer. Use an exist ing int ernal SLB inst ance You need to add two annotations as follows. Note that you must replace "yourloadbalancer-id" with your SLB instance ID.

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

Creat e an HT T PS-based service of t he Server Load Balancer t ype Create a certificate in the Apsara Stack console and copy cert-id. Then create an HTTPS-based service of the Server Load Balancer type as follows:

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
| service.beta.kubernetes.io/aliclou d-loadbalancer-protocol-port | The listening port. Separate multiple ports with commas (,). For example, https:443,http:80. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-address-type | The type of the SLB instance. Valid values: internet and intranet. | internet |
| service.beta.kubernetes.io/aliclou d-loadbalancer-slb-network-type | The network type of the SLB instance. Valid values: classic and vpc. | classic |
| service.beta.kubernetes.io/aliclou d-loadbalancer-charge-type | The billing method of the SLB instance. Valid values: paybytraffic and paybybandwidth. | paybybandwidth |
| service.beta.kubernetes.io/aliclou d-loadbalancer-id | The ID of the SLB instance. You can use loadbalancer-id to specify an existing SLB instance and its existing listeners will be overwritten. The SLB instance will not be deleted if the service is deleted. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-backend-label | The labels for specifying the nodes to be added as backend servers of the SLB instance. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-region | The region where the SLB instance is deployed. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-bandwidth | The bandwidth of the SLB instance. | 50 |
| service.beta.kubernetes.io/aliclou d-loadbalancer-cert-id | The certificate ID. You need to upload the certificate first. | “” |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check-flag | Specifies whether to enable the health check feature. Valid values: on and off. | off. This annotation is not required for TCP listeners. By default, the health check feature is enabled for TCP listeners and cannot be disabled. |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- type | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check-uri | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- connect-port | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |

| User Guide·Kubernetes clusters | Containe | r Service for Kubernete |
|---|---|---|

| Annotation | Description | Default value |
|---|---|---|
| service.beta.kubernetes.io/aliclou d-loadbalancer-healthy- threshold | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-unhealthy- threshold | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- interval | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- connect-timeout | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |
| service.beta.kubernetes.io/aliclou d-loadbalancer-health-check- timeout | For more information, see the CreateLoadBalancerTCPListener chapter of SLB Developer Guide. | - |

#### 4.8.3 Configure ingress monitoring

You can enable the default VTS module to view ingress monitoring data. Enable VTS module by using the CLI
1. Modify the ingress ConfigMap to add the following configuration item: `enable-vts-status: "tru`
`e"` .

```
root@master # kubectl edit configmap nginx-configuration -n kube-system
      configmap "nginx-configuration" edited
```

The modified ingress ConfigMap is as follows:

```json
apiVersion: v1 data:
  enable-vts-status: "true" # Enable the VTS module
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

2. Verify that the VTS module is enabled.

```
root@master # kubectl get pods --selector=app=ingress-nginx -n kube-system NAME READY STATUS RESTARTS AGE nginx-ingress-controller-79877595c8-78gq8 1/1 Running 0 1h root@master # kubectl exec -it nginx-ingress-controller-79877595c8-78gq8 -n kube-system -- cat /etc/nginx/nginx.conf | grep vhost_traffic_status_display
         vhost_traffic_status_display;
         vhost_traffic_status_display_format html;
```

3. Access the NGINX Ingress Controller from a local computer.
Not e By default, the VTS port is not enabled for security concerns. The following example uses port forwarding to access the controller.

```
root@master # kubectl port-forward nginx-ingress-controller-79877595c8-78gq8 -n kube-sy stem 18080 Forwarding from 127.0.0.1:18080 -> 18080 Handling connection for 18080
```

4. Visit `http://localhost:18080/nginx_status` to access the NGINX Ingress Controller.
Enable VTS module by using the Kubernetes Dashboard
1. Log on to the Container Service console.
2. Find the target cluster and click Dashboard in the Actions column to go to Kubernetes Dashboard.
3. In the left-side navigation pane, select the kube-system namespace and edit the nginx-
configuration ConfigMap to add the following configuration item: `enable-vts-status: "true"` . The modified ingress ConfigMap is as follows: `{`

```json
  "kind": "ConfigMap",
  "apiVersion": "v1",
  "metadata": {
    "name": "nginx-configuration",
    "namespace": "kube-system",
    "selfLink": "/api/v1/namespaces/kube-system/configmaps/nginx-configuration",
    "creationTimestamp": "2018-03-20T07:10:18Z",
    "labels": {
      "app": "ingress-nginx"
```

`},`

```json
    "annotations": {
      "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"dat
a\":{\"proxy-body-size\":\"20m\"},\"kind\":\"ConfigMap\",\"metadata\":{\"annotations\": {},\"labels\":{\"app\":\"ingress-nginx\"},\"name\":\"nginx-configuration\",\"namespace\ ":\"kube-system\"}}\n"
```

`}` `},`

```json
 "data": {
   "proxy-body-size": "20m",
   "enable-vts-status": "true"
```

`}` `}`
4. Access the NGINX Ingress Controller from a local computer.
Not e By default, the VTS port is not enabled for security concerns. The following example uses port forwarding to access the controller.

```
root@master # kubectl port-forward nginx-ingress-controller-79877595c8-78gq8 -n kube-sy stem 18080 Forwarding from 127.0.0.1:18080 -> 18080 Handling connection for 18080
```

5. Visit `http://localhost:18080/nginx_status` to access the NGINX Ingress Controller.

#### 4.8.4 Ingress support

Kubernetes clusters support ingress rules. You can define ingress rules based on your needs to implement load balancing. In Kubernetes, an ingress is a collection of routing rules that authorize external access to cluster services. You can use an ingress to enable Layer-7 load balancing. You can configure an ingress to provide Kubernetes services with externally reachable URLs, SLB instances, SSL connections, and namebased virtual hosting. Prerequisites To test a complex routing scenario, this example creates an NGINX application that consists of multiple services. You need to create an NGINX deployment and multiple services in advance. In practice, replace service names with the actual values.

```
root@master # kubectl run nginx --image=registry.cn-hangzhou.aliyuncs.com/acs/netdia:latest
    root@master # kubectl expose deploy nginx --name=http-svc --port=80 --target-port=80
    root@master # kubectl expose deploy nginx --name=http-svc1 --port=80 --target-port=80
    root@master # kubectl expose deploy nginx --name=http-svc2 --port=80 --target-port80
    root@master # kubectl expose deploy nginx --name=http-svc3 --port=80 --target-port=80
```

Simple routing Use the following commands to create a simple ingress that redirects traffic to path /svc to a http-svc service. `nginx.ingress.kubernetes.io/rewrite-target: /` indicates that traffic to /svc is redirected to the root path /, which can be recognized by the backend service.

```
root@master # cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
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
EOF root@master # kubectl get ing NAME HOSTS ADDRESS PORTS AGE simple * 101.37.192.211 80 11s
```

You can now visit `http://101.37.192.211/svc` to access the NGINX service. Simple fanout based on domains If you have multiple services exposed externally through different domains, you can use the following configuration to implement a simple fanout based on domains:

```
root@master # cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
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
EOF root@master # kubectl get ing NAME HOSTS ADDRESS PORTS AGE simple-fanout * 101.37.192.211 80 11s
```

| You can now visit | http://foo.bar.com/foo | to access ser |
|---|---|---|
| http://foo.bar.com/bar |   | http-svc2 |
| to access service | http-svc3 |   |

| Not e In a production environment, you need to point the domain to the returned address 101.37 .192.211 . In a test environment, you need to add the following mapping rules to the hosts file. 101.37.192.211 foo.bar.com 101.37.192.211 foo.example.com |   |   |
|---|---|---|
|   | 101.37 |   |

Default domain for simple routing If you have no domain address, you can use the default domain associated with the ingress to access the service. The default domain is in the following format: `*.[cluster-id].[region-` `id].alicontainer.com` . You can obtain the domain address on the cluster basic information page in the console. You can use the following configuration to expose the two services through the default domain.

```
root@master # cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
  name: shared-dns
spec:
  rules:
  - host: foo.[cluster-id].[region-id].alicontainer.com  ## Replace with the default domain
of your cluster
    http:
      paths:
      - path: /
        backend:
          serviceName: http-svc1
          servicePort: 80
  - host: bar.[cluster-id].[region-id].alicontainer.com  ## Replace with the default domain
of your cluster
    http:
      paths:
      - path: /
        backend:
          serviceName: http-svc2
          servicePort: 80
EOF root@master # kubectl get ing NAME HOSTS ADDRESS PORTS AGE shared-dns foo.[cluster-id].[region-id].alicontainer.com,bar.[cluster-id].[region-id].ali container.com 47.95.160.171 80 40m
```

| http://foo.[cluster-id].[region-id].alicontainer.com/ |   | to |
|---|---|---|
| visit | http://bar.[cluster-id].[region-id].alicontainer.com |   |

```
 http-svc2 .
```

Secure routing Container Service supports managing multiple certificates to enhance protection for your services.
1. Prepare your certificate.
If you have no certificate, use the following method to generate a test certificate. Not e The domain must be the same as the one specified in your ingress configuration.

```
root@master # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

After you run the preceding command, a certificate file tls.crt and a private key file tls.key are generated. Use the certificate and private key to create a Kubernetes secret named foo.bar. You need to reference the secret when you create the ingress.

```
root@master # kubectl create secret tls foo.bar --key tls.key --cert tls.crt
```

2. Create a secure ingress.

```
root@master # cat <<EOF | kubectl create -f apiVersion: extensions/v1beta1 kind: Ingress metadata:
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
EOF root@master # kubectl get ing NAME HOSTS ADDRESS PORTS AGE tls-fanout * 101.37.192.211 80 11s
```

3. As described in Simple f anout based on domains, you need to configure the `hosts` file or
set a domain to access the tls ingress.

| http://foo.bar.com/foo |   |
|---|---|
| access service | http-svc2 |

You can visit `http://foo.bar.com/foo` to access service `http-svc1` and visit `http://foo.bar.` You can also access the HTTPS service by using HTTP. By default, the ingress redirects HTTP traffic to the HTTPS address. Traffic to `http://foo.bar.com/foo` is automatically redirected to `https`

```
://foo.bar.com/foo .
```

Deploy an ingress in Kubernetes Dashboard
1. Create an `nginx-svc.yml` file with the following code:

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

2. Log on to the Container Service console.
3. In the left-side navigation pane, click Clusters. Find the target cluster and click Dashboard in the
Actions column to go to the Overview page.
4. Click CREAT E in the upper-right corner to create an ingress.
5. Click the CREAT E FROM FILE tab. Select file `nginx-ingress.yml` .
6. Click UPLOAD.
This creates an ingress that routes Layer-7 traffic for service `http-svc` .
7. In the left-side navigation pane, select the def ault namespace and click Ingresses.
You can view the newly created ingress and its endpoint.
8. Enter the endpoint into your browser to access the `http-svc` service.

#### 4.8.5 Ingress configurations

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

#### 4.8.6 Create an Ingress in the console

The Container Service console is integrated with the Ingress service. You can create an Ingress in the console and manage inbound traffic that is forwarded to different services to meet your business requirements. Prerequisites A Kubernetes cluster is created and an Ingress controller runs normally in the cluster. For more information, see Create a Kubernetes cluster. You can use kubectl to connect to a master node. For more information, see Connect to a Kubernetes cluster through kubectl. In this example, the image is retrieved over the Internet. You can replace the image address with the one that is accessible to your own cluster. Otherwise, you can build the image that is used in this example and push the image to a repository. To use the image, you can pull the image from the repository. Step 1: Create a deployment and a service
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployment s page
appears.
3. Click Creat e f rom T emplat e in the upper-right corner of the page.
4. Select the target cluster and namespace, select a sample template or enter a custom template,
and then click Creat e. In this example, two NGINX applications are created. One is named old-nginx and the other is named new-nginx. The following code example shows the template that is used to create old-nginx:

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

The following code example shows the template that is used to create new-nginx:

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

5. In the left-side navigation pane, choose Ingresses and Load Balancing > Services.
On the Services page, find the newly created services. Step 2: Create an Ingress
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Ingresses. The
Ingresses page appears.
3. Select the target cluster and namespace, and click Creat e in the upper-right corner of the page.
4. In the dialog box that appears, enter the Ingress name. In this example, nginx-ingress is used.
5. Configure Ingress rules.
Ingress rules are used to manage inbound access to the services in the cluster. The rules include HTTP or HTTPS rules. You can configure the following items in rules: domain name (virtual hostname), URL path, service name, port, and weight. For more information, see Ingress configurations. In this example, a rule is added to specify two services for the default domain name and virtual hostname of the cluster. Traffic routing is based on domains. Simple f anout conf igurat ions based on domains In this example, a virtual hostname is used as the test domain to provide services. Route weights are specified for both services and a canary release is configured for one of the services. In your production environment, you can use a domain name that has obtained an Internet Content Provider (ICP) number to provide services. Domain: Enter the test domain name. In this example, `foo.bar.com` is used. You must modify the hosts file to add a domain name mapping rule.

```
118.178.XX.XX foo.bar.com #The IP address of the Ingress.
```

Services: Set the path, name, port, and weight of each service. Path: Enter the URL path of each service. In this example, the default root path / is used. Name: In this example, two service names are used: old-nginx and new-nginx. Port: In this example, port 80 is opened. Weight: Set the weight for each service. The weight is a percentage value. Default value: 100. In this example, the same weight 50 is set for each service.
6. Configure TLS. Select EnableT LS to enable TLS and configure secure routing. For more
information, see Configure a secure Ingress. You can select an existing secret. a. Log on to a master node and create the tls.key and tls.crt files.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

b. Create a secret.

```bash
kubectl create secret tls foo.bar --key tls.key --cert tls.crt
```

c. On the command line, enter `kubectl get secret` and verify that the secret has been created. You can then select the foo.bar secret. You can also use the TLS private key and certificate to create a secret. a. Log on to a master node and create the tls.key and tls.crt files.

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=foo.bar.com/O=foo.bar.com"
```

b. On the command line, enter `vim tls.key` and `vim tls.crt` to obtain the private key and certificate that are generated. c. Copy the certificate to the Cert field and the private key to the Key field.
7. Configure a canary release.
Not e Currently, only Ingress controllers of 0.12.0-5 and later versions support traffic splitting. Container Service supports multiple traffic splitting methods. This allows you to select more suitable solutions for specific scenarios, such as canary releases and A/B testing, including: i. Traffic splitting based on request headers ii. Traffic splitting based on cookies iii. Traffic splitting based on query parameters After a canary release is configured, requests that match only the specified rules are routed to the new-nginx service. If the weight of new-nginx is lower than 100%, requests that match the specified rules are routed to this service based on the weight. In this example, the rule is added to specify a request header that matches the regular expression foo=^bar$ . Only requests that contain this header can access new-nginx. Services: the service to be accessed. T ype: the type of the matching rule, such as Header, Cookie, or Query. Name and Mat ch Value: custom request fields. The name and matching value comprise a keyvalue pair. Mat ching Rule: Regular expressions and exact matches are supported.
8. Configure annotations.
Click Rewrit e Annot at ion to add a rewrite annotation for the Ingress. For example, `nginx.ingre` `ss.kubernetes.io/rewrite-target: /` indicates that /path is redirected to the root path /. The root path can be recognized by the backend service. Not e In this example, no path is configured for the service. You do not need to configure rewrite annotations. Rewrite annotations allow the Ingress to forward traffic through root paths to the backend service. This avoids the error 404 that is caused by invalid paths. You can also click Add to enter annotation names and values in key-value pairs. For more information about Ingress annotations, visit https://kubernetes.github.io/ingress-nginx/userguide/nginx-configuration/annotations/.
9. Add labels.
Add labels to describe the features of the Ingress.
10. Click Creat e.
You can find the nginx-ingress Ingress on the Ingresses page.
11. Click foo.bar.com to view the NGINX welcome page.
When you click the domain name that points to new-nginx, the old-nginx service page appears. Not e By default, when you enter the route address in the browser, requests with headers that do not contain foo=^bar$ are directed to old-nginx.
12. Use SSH to log on to a master node. Run the following commands to simulate requests with
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

#### 4.8.7 Update an ingress

You can update an ingress through the console. Prerequisites You have created a Kubernetes cluster and an ingress controller is running normally in the cluster. For more information about creating clusters, see Create a Kubernetes cluster. You have created an ingress. For more information, see Create an ingress through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Ingresses. The
Ingresses page appears.
3. Select the target cluster and namespace. Find the ingress that you want to update and click
Updat e in the Actions column.
4. In the dialog box that appears, modify the parameters and click OK. This example changes `foo.ba`

```
r.com to test.bar.com .
```

What's next On the Ingresses page, you can find the updated ingress rule.

#### 4.8.8 Delete an ingress

Prerequisites You have created a Kubernetes cluster and an ingress controller is running normally in the cluster. For more information about cluster creation, see Create a Kubernetes cluster. You have created an ingress. For more information, see Create an ingress through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Ingresses and Load Balancing > Ingresses.
3. Select the target cluster and namespace. Find the ingress that you want to delete and click Delet e
in the Actions column.
4. In the dialog box that appears, click OK.

### 4.9 Config maps and secrets

#### 4.9.1 Create a ConfigMap

You can create a ConfigMap on the ConfigMaps page or by using a template. Create a ConfigMap on the ConfigMaps page
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Conf igMaps. The ConfigMaps page
appears.
3. Select the target cluster and namespace, and then click Creat e.
4. Set the parameters and click OK.
Create a ConfigMap on the ConfigMaps page

| Parameter | Description |
|---|---|
| Clust er | The ID of the selected cluster. |
| Namespace | The selected namespace. A ConfigMap is a kind of Kubernetes resource object and must be scoped into a namespace. |

| User | Guide·Kubernetes clusters | Container Service for Kubernete | s |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Conf igMap Name | Required. The name can contain lowercase letters, digits, hyphens (-), and periods (.). Other resource objects need to reference ConfigMap names to obtain configuration information. |
| Conf igMap | Enter the Name and Value, and then click Add to add the key-value pair. You can also click Edit YAML f ile, modify the parameters in the dialog box that appears, and then click OK. |

In this example, two variables named enemies and lives are created. Their values are set to aliens and 3 respectively.
5. Click OK. You can find the newly created ConfigMap on the ConfigMaps page.
You can also click Browse to upload a configuration file to create a ConfigMap. Create a ConfigMap from a template
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Deployment s. The Deployments page
appears.
3. In the upper-right corner, click Creat e f rom T emplat e.
4. On the page that appears, set the parameters and click Creat e.
Create a ConfigMap from a template

| Parameter | Description |
|---|---|
| Clust er | The cluster where the ConfigMap is created. |

| Parameter | Description |
|---|---|
| Namespace | The namespace where the ConfigMap belongs. A ConfigMap is a kind of Kubernetes resource object and must be scoped into a namespace. |
| Sample T emplat e | Container Service provides various YAML templates for different types of resources. This helps you deploy resources quickly. You can choose Custom and enter your own ConfigMap based on YAML syntax, or select the Resource-Co nfigMap template. In the sample template, the ConfigMap is named aliyun-config and contains two variable files game.properties and ui.properti es. You can modify the ConfigMap based on your needs. |
| T emplat e | Enter the template content based on YAML syntax. The template can contain multiple resource objects that are separated by --- . |
| Add Deployment | This feature allows you to quickly define a YAML template. You can click Use Exist ing T emplat e to import an existing template. |

You can find the newly created ConfigMap aliyun-config on the ConfigMaps page.

#### 4.9.2 Use a ConfigMap in a Pod

You can use a ConfigMap in a Pod in the following scenarios: Use a ConfigMap to define environment variables Use a ConfigMap to configure command line parameters Use a ConfigMap in volumes For more information, see Configure a Pod to use a ConfigMap. Limits To use a ConfigMap in a Pod, make sure that the ConfigMap and Pod are in the same cluster and namespace. Create a ConfigMap This example creates a ConfigMap named special_config, which consists of two key-value pairs:

```
 SPECIAL_LEVEL: very  and  SPECIAL_TYPE: charm .
```

You can use the following YAML template to create a ConfigMap.

```
apiVersion: v1 kind: ConfigMap metadata:
  name: special-config
  namespace: default
data:
  SPECIAL_LEVEL: very
  SPECIAL_TYPE: charm
```

You can also log on to the Container Service console and choose Conf igurat ion > Conf igMaps in the left-side navigation pane. You can then click Creat e to create a ConfigMap. Use ConfigMaps to define Pod environment variables Def ine t he value of a Conf igMap as an environment variable You can log on to the Container Service console and choose Applicat ions > Deployment s in the leftside navigation pane. Click Creat e f rom T emplat e, select and modify the Pod type template, and deploy the application. You can also go to the Kubernetes dashboard and choose Upload YAML or JSON File. The following sample template creates a Pod and defines environment variables in the Pod. valueFrom is used to reference the value of SPECIAL_LEVEL to define an environment variable.

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
          valueFrom:              ##Use valueFrom to denote that env references the value o
f a ConfigMap.
            configMapKeyRef:
              name: special-config               ##The referenced ConfigMap name.
              key: SPECIAL_LEVEL                 ##The referenced ConfigMap key.
  restartPolicy: Never
```

To define the values of multiple ConfigMaps as environment variables, you only need to add multiple env parameters in the Pod definition. Def ine t he key-value pairs of a Conf igMap as environment variables To define the key-value pairs of a ConfigMap as Pod environment variables, you can use the envFrom parameter. The keys in a ConfigMap are used as the names of the environment variables. A sample template is provided as follows:

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-2
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      envFrom:                ##Reference all the key-value pairs in the special-config Con
figMap.
      - configMapRef:
        name: special-config
  restartPolicy: Never
```

Use a ConfigMap to configure command line parameters You can use ConfigMaps to configure the commands or parameter values in a container by using the environment variable replacement syntax $(VAR_NAME). A sample template is provided as follows:

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

Run the Pod and the output is as follows:

```
very charm
```

Use a ConfigMap in volumes You can use a ConfigMap to define volumes. The following sample template specifies a ConfigMap name under volumes. This stores the key-value pair data to the mountPath path, which is /etc/config in this example. This generates configuration files that are named after the keys of the ConfigMap. The corresponding values of the ConfigMap are stored in these files.

```
apiVersion: v1 kind: Pod metadata:
  name: config-pod-4
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "ls /etc/config/" ]   ##List the names of files under thi
s directory.
      volumeMounts:
        - name: config-volume
          mountPath: /etc/config
   volumes:
     - name: config-volume
       configMap:
         name: special-config
  restartPolicy: Never
```

Run the Pod and the keys of the ConfigMap are output:

```
SPECIAL_TYPE SPECIAL_LEVEL
```

#### 4.9.3 Update a ConfigMap

You can use multiple methods to update a ConfigMap. Note If you update a ConfigMap, the applications that use this ConfigMap will be affected. Update a ConfigMap on the ConfigMaps page
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Conf igMaps to go to the ConfigMaps
page.
3. Select the target cluster and namespace, find the ConfigMap that you want to update, and then
click Edit in the Actions column for the ConfigMap.
4. In the dialog box that appears, modify the configurations, and click OK.
Update a ConfigMap by using the Kubernetes dashboard
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers to go to the Clusters page. Find the
cluster that you want to manage and click Dashboard in the Actions column for the cluster.
3. On the Overview page, choose Conf ig and St orage > Conf igMaps in the left-side navigation
pane. Select the target ConfigMap and choose
> View/edit YAML.

4. In the dialog box that appears, modify the configurations and click Updat e.

#### 4.9.4 Delete a ConfigMap

You can use multiple methods to delete a ConfigMap. Notes If you delete a ConfigMap, the applications that use this ConfigMap will be affected. Delete a ConfigMap on the ConfigMaps page
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Conf igMaps. The ConfigMaps page
appears.
3. Select the target cluster and namespace. Find the ConfigMap that you want to delete and click
Delet e in the Actions column. Delete a ConfigMap through Kubernetes Dashboard
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Clust ers > Clust ers. Find the target cluster and click
Dashboard in the Actions column.
3. On the Kubernetes Dashboard page, choose Conf ig and St orage > Conf ig Maps in the left-side
navigation pane. Find the target ConfigMap and choose t he More icon > Delet e.
4. In the dialog box that appears, click DELET E.

#### 4.9.5 Create a secret

You can create secrets for applications in the Container Service console. Prerequisites A Kubernetes cluster is created. Context We recommend that you use secrets to store sensitive information in Kubernetes clusters, such as passwords and certificates. Secrets are classified into the following types: Service Account: This type of secret is automatically created by Kubernetes and is automatically mounted to the pod directory /run/secrets/kubernetes.io/serviceaccount. You can use this type of secret to access the Kubernetes API. Opaque: This type of secret is encoded in the Base64 format and used to store sensitive information, such as passwords and certificates. You can use the Container Service console to create only Opaque secrets. Opaque data belongs to the map type. The value of this type must be encoded in the Base64 format. You can encode plain text in the Base64 format by using the console. You can also manually create secrets by using the command-line interface (CLI). For more information, see Kubernetes secrets. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Secret s. The Secrets page appears.
3. Select the target cluster and namespace. Click Creat e in the upper-right corner of the page.
4. Configure the secret and click OK.
Not e To enter secret data in plain text, select Encode Dat a Values Using Base64. Secret parameters

| Parameter | Description |
|---|---|
| Name | The name of the secret that you want to create. The name must be 1 to 253 characters in length and can only contain lowercase letters, digits, hyphens (-), and periods (.). |
| Dat a | The data stored in the secret. Click Add, and in the dialog box that appears, enter the key and value as a key-value pair. In this example, two entries are entered: username: admin and password: 1f2d1e2e67df . |

|   | username: admin |
|---|---|
| password: 1f2d1e2e67df |   |

5. You can view the newly created secret on the Secrets page.

#### 4.9.6 Edit a secret

This topic describes how to edit a secret in the Container Service console. Prerequisites You have created a Kubernetes cluster. You have created a secret. For more information, see Create a secret. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Secret s to go to the Secrets page.
3. Select the cluster and namespace. Choose the target secret and click Edit in the Actions column.
4. On the Edit Secret page, edit the secret based on your needs.
5. Click OK to save your edits.

#### 4.9.7 Delete a secret

This topic describes how to delete a secret in the Container Service console. Prerequisites You have created a Kubernetes cluster. You have created a secret. For more information, see Create a secret. Context Not e Do not delete secrets that were generated during the cluster creation process. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Conf igurat ion > Secret s to go to the Secrets page.
3. Select the cluster and namespace. Choose the target secret and click Delet e in the Actions
column.
4. In the dialog box that appears, click OK to delete the secret.

### 4.10 Templates

#### 4.10.1 Create an orchestration template

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

#### 4.10.2 Update an orchestration template

This topic describes how to edit and update an orchestration template. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Edit in the upper-right corner.
5. In the dialog box that appears, edit the name, description, and template content, and click Save.
6. Go to the T emplat es page. You can view the template that you have updated on the My
T emplat es tab.

#### 4.10.3 Save an orchestration template as a new one

one This topic describes how to save an orchestration template as a new one. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, modify the template and click Save As in the upper-right corner.
5. In the dialog box that appears, enter the template name and click OK.
6. Go to the T emplat es page. The newly saved template is displayed on the My T emplat es tab.

#### 4.10.4 Download an orchestration template

This topic describes how to download an orchestration template. Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Download in the upper-right corner to download the template
as a YAML file.

#### 4.10.5 Delete an orchestration template

Prerequisites You have created an orchestration template. For more information, see Create orchestration templates. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Market place > Orchest rat ion T emplat es. The
T emplat es page appears. You can view existing templates on the My T emplat es tab.
3. Select the target template and click Det ails.
4. On the template details page, click Delet e in the upper-right corner.
5. In the dialog box that appears, click OK.

### 4.11 Images

#### 4.11.1 Create an image repository

This topic describes how to create an image repository in the Container Registry console. Prerequisites The Container Registry service is activated and a namespace is created in the Container Registry service. Procedure
1. Log on to the Container Registry console.
2. In the left-side navigation pane, click Reposit ories to go to the Repositories page. Click Creat e
Reposit ory in the upper-right corner of the page.
3. In the dialog box that appears, set the following parameters and click Next .
Region: Use the default value. The region of the repository must be the same as that of the cluster. Namespace: Use the default value. The namespace must be the same as that of the organization that you select when you log on to the console. Reposit ory Name: The repository name must be 2 to 64 characters in length and can contain lowercase letters, digits, and special characters, including underscores (_), hyphens (-), and periods (.). It cannot start or end with a special character. Summary: Enter the repository summary. Descript ion: Enter description information. The description must be 0 to 100 characters in length. Reposit ory T ype: The repository type can be public or private.
4. Set the code source and click Creat e Reposit ory.
Not e Currently, only local repositories are supported. You can push images to an image repository by using the command-line interface (CLI).
5. Go to the Repositories page to view the newly created repository.
What's next You can click Admin in the Act ions column for the repository to go to the Det ails page and learn how to manage the repository.

#### 4.11.2 Create a namespace

This topic describes how to create a namespace in the Container Registry console. Context A namespace is a collection of repositories. We recommend that you place the repositories of a company or an organization in the same namespace. You can enter a name that corresponds to a company name, such as aliyun or alibaba. You can enter a name that corresponds to a team or organization name for the namespace, such as misaka-team. Procedure
2. In the left-side navigation pane, click Namespace. On the page that appears, click Creat e
Namespace to create a namespace. You can find the newly created namespace on the Namespace page. Not e You can turn on or turn off Aut omat ically Creat e Reposit ory to specify whether to automatically create image repositories for the namespace. You can set the repository type to Public or Privat e for the namespace. What's next You can create more image repositories for the namespace.

#### 4.11.3 Synchronize an image

Container Registry can be used to synchronize images across data centers. This allows you to retrieve images from the data center that is nearest to where your workloads are deployed. Prerequisites A namespace is created. For more information, see Create a namespace. An image repository for the namespace is created. For more information, see Create a repository. Procedure
1. Log on to the Container Registry console.
2. In the left-side navigation pane, choose Reposit ories to go to the Reposit ories page.
3. Select the target repository and click Admin in the Act ions column for the repository to go to the
Details page.
4. In the left-side navigation pane, choose T ags. Find the target tag and click Sync in the Act ions
column for the tag.
5. On the Sync page, specify the tag and target repository, and click OK.
A message appears to indicate that the synchronization request is submitted. Result In the left-side navigation pane of the target repository, click Sync to check the status of the synchronization task. You can click Det ails in the Actions column for the task to check the task status for the specified image.

#### 4.11.4 Sign and verify an image

When you manage container images, you can use content trust to verify both the integrity and the publisher of images. Image publishers can encrypt images by using digital signatures that are stored in Container Registry. We recommend that you verify the signatures to ensure that only images signed by trusted authorities are deployed. This way, you can minimize or stop attacks that may occur when you run containers. Install and configure signature tools
1. Install the aliyun client tool. For more information, see Install Alibaba Cloud CLI.
2. On the command line, run the following command to configure aliyun client:

```
./aliyun configure set \
  --profile akProfile \
  --mode AK \
  --region cn-qingdao-env17-d01 \
  --access-key-id yourAK \
  --access-key-secret yourAK
```

3. After you install and configure the GPG tool, run the following command to export the public key:

```
#Query the pubKeyId.
gpg --fingerprint
#Export the public key.
gpg --armor --output public-key.txt --export yourUser
```

Not e For Apsara Stack instances, instanceId is set to default. Sign container images
1. On the command line, run the following command to determine the image tag URL:

```
echo image://region/instanceId/namespace/repo@digest | tee imageURL.txt
#e.g.
#echo image://cn-qingdao-env17-d01/default/kritis-test/busybox2@sha256:2f122941b5850006
dbb7adda78d2ea5b382841ca6569fd174bd24c14bfff3dca > imageURL.txt
```

2. On the command line, run the following command to use GPG to sign the unique URL of the image.
By default, imageURL.txt.asc is generated.

```
gpg --armor --sign imageURL.txt
```

The imageURL.txt.asc file includes the following content:

```
-----BEGIN PGP MESSAGE----owGbwMvMwMEo63vGqaX74wXGNXVJ3CmpaYmlOSV6JRUlcZy7vmfmJqanWunr**** ....... =O2TP -----END PGP MESSAGE-----
```

3. On the command line, run the following command to create a metadata namespace:

```
./aliyun cr CreateMetadataNamespace --force --version 2018-12-01 --endpoint cr.inter.en v17e.shuguang.com --NamespaceName kritis-test-2 --Description "for test"
```

4. On the command line, run the following command to create a signature note:

```
cat <<EOF > note.json| jq
```

`{`

```json
  "name": "/namespaces/kritis-test-2/notes/image-sign",
  "LongDescription": "long",
  "ShortDescription": "short",
  "ExpirationTime": "2021-01-01T00:00:00Z",
  "Kind": "ATTESTATION",
  "Attestation": {
    "Hint": {
      "HumanReadableName": "ACR"
```

`}` `}` `}`

```
EOF
```

5. On the command line, run the following command to create an occurrence for the image signature
and save the occurrence to the metadata service:

```
cat <<EOF > occurrence.json | jq
```

`{`

```json
  "Name": "/namespaces/kritis-test-2/occurrences/randomId1",
  "NoteName": "/namespaces/kritis-test-2/notes/image-sign",
  "ResourceUri": "image://cn-qingdao-env17-d01/default/kritis-test/busybox2@sha256:2f12
2941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bff****",
  "Kind": "ATTESTATION",
  "Attestation": {
    "Signatures": [
```

`{`

```json
        "Signature": $(cat imageURL.txt.asc|jq -R --slurp),
        "PublicKeyId": "E5B5FF2AFC3A1D70FE3CE57C1D4DCC42848****"
```

`}` `]` `}` `}`

```
EOF
```

```
./aliyun cr CreateMetadataOccurrence --force --version 2018-12-01 --endpoint cr.inter.e nv17e.shuguang.com --NamespaceName kritis-test-2 --OccurrenceName randomId1 --Occurrenc e "$(cat occurrence.json)"
```

6. On the command line, run the following command to query the image signature:

```
#Retrieve a list of occurrences for a specified note. In this example, one occurrence i
s created. ./aliyun cr ListMetadataOccurrences --force --version 2018-12-01 --endpoint cr.inter.en v17e.shuguang.com --NamespaceName kritis-test-2 --NoteName image-sign --PageNo 1 --Page Size 5
#Retrieve a list of occurrences for a specified note that occurs on a resource. In this
example, one occurrence is created. ./aliyun cr ListMetadataOccurrences --force --version 2018-12-01 --endpoint cr.inter.en v17e.shuguang.com --NamespaceName kritis-test-2 --NoteName image-sign --PageNo 1 --Page Size 5 --ResourceURIs '["image://cn-qingdao-env17-d01/default/kritis-test/busybox2@sha2 56:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bfff****"]'
```

Verify an image signature The following steps describe how to install an image signature verification component and enable the verification feature on Apsara Stack.
1. Install the image signature verification component.
i. Log on to the Container Service console. ii. Go to the Clusters page, find the cluster in which you want to install the image signature verification component, and in the Actions column for the cluster, choose More > Install Kritis.
2. Configure the signature verification policy.
i. Set the following signature parameters to configure the signature verification policy:

```bash
$ export namespace=Actual value of namespace $ export noteName=Actual value of noteName $ export publicKeyData=Actual value of publicKeyData
```

namespace: the ACR namespace setting used for signing an image. noteName: the noteName setting used for signing an image. publicKeyData: the Base64-encoded GPG public key. ii. On the command line, run the following command to set AttestationAuthority: Not e The default namespace is used in the following example.

```bash
$ cat <<EOF > aa.yaml apiVersion: kritis.grafeas.io/v1beta1 kind: AttestationAuthority metadata:
  name: ${noteName}
spec:
  noteReference: namespaces/${namespace}
  publicKeyData: ${publicKeyData}
EOF $ kubectl -n default apply -f aa.yaml
```

iii. On the command line, run the following command to set GenericAttestationPolicy: Not e The default namespace is used in the following example.

```bash
$ cat <<EOF > gap.yaml apiVersion: kritis.grafeas.io/v1beta1 kind: GenericAttestationPolicy metadata:
  name: my-gap
spec:
  attestationAuthorityNames:
  - ${noteName}
EOF $ kubectl -n default apply -f gap.yaml
```

3. Test the signature verification feature.
In the test, a signed image is used: registry.acs.example.com/kritistest/signed@sha256:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bfff****. An unsigned image is also used: registry.acs.example/kritis-test/notsign@sha256:efc961b2b3499c25753d3c9f29977f494f49125cf1191071057aa68bffa7****. If the feature functions as expected, the signature verification policy enables the signed image and disables the unsigned image for the default namespace. The following example shows how to test the feature:

```bash
#A deployment is created based on the signed image.
$ kubectl -n default run test-signed --image=registry.acs.example.com/kritis-test/signe d@sha256:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bff**** deployment.apps/test-signed created
#The unsigned image fails a deployment.
$ kubectl -n default run test-not-signed --image=registry.acs.example/kritis-test/not-s ign@sha256:efc961b2b3499c25753d3c9f29977f494f49125cf1191071057aa68bffa7**** Error from server: admission webhook "kritis-validation-hook-deployments.grafeas.io" de nied the request: image registry.acs.example/kritis-test/not-sign@sha256:efc961b2b3499c 25753d3c9f29977f494f49125cf1191071057aa68bffa7**** is not attested
```

Not e After you enable image signature verification, when you create resources, the image ID must be a digest value in the format such as @sha256:<hash>. Appendix 1: Use GPG commands to generate publicKeyData
1. On the command line, run the following command to find the local GPG key user that you want to
use: Not e The user in the following example is `abcdef@example.com` .

```bash
$ gpg --list-keys pub rsa2048 2020-01-08 [SC] [Expired on: 2022-01-07]
      7726310BC6E11E9B57B9CC08E2932E4363F3***
uid [Absolute] abcdef <abcdef@example.com> sub rsa2048 2020-01-08 [E] [Expired on: 2022-01-07]
```

2. Export the public key of this user and encode the content of the public key in the Base64 format to
generate publicKeyData.

```bash
$ gpg --armor --export <user> |base64 | tr -d '\n'
#In the example, the user is abcdef@example.com.
#Run this command to generate publicKeyData: gpg --armor --export  abcdef@example.com |
base64 | tr -d '\n'
# export publicKeyData=$(gpg --armor --export  abcdef@example.com |base64 | tr -d '\n')
```

Appendix 2: Retrieve an image digest value You can use the following method to find an image digest value. In this example, the image URL is registry.acs.example.com/kritis-test/alpine:3.11.

```bash
$ docker pull registry.acs.example.com/kritis-test/alpine:3.11 $ docker images --digests | grep registry.acs.example.com/kritis-test/alpine registry.acs.example.com/kritis-test/alpine 3.11 sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1 f23a8e742c90e6e1297bfa1bc0c45 e7d92cdc71fe 2 months ago 5.59MB
```

The output shows that the image digest value is sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45. When you create resources, the following image ID must be used: registry.acs.example.com/kritistest/alpine:sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45.

#### 4.11.5 Synchronize images between instances

You can configure synchronization rules to automatically synchronize images from a source instance to a destination instance. By default, images are automatically synchronized for instances that are deployed in different regions. Procedure
1. Log on to the Container Registry console.
2. Go to the Reposit ories page, find the repository that you want to manage, and then click Admin
in the Act ions column for the repository.
3. The Details page is displayed. In the left-side navigation pane, click Sync.
4. In the upper-right corner of the Sync page, click Creat e. In the Sync dialog box, set the T ag and
T arget parameters, specify the namespace, repository name, and tag of the target repository, and then click OK. The synchronization rule is created. Result After the synchronization rule is created, a synchronization task is automatically triggered when a new image is uploaded to the repository whose name matches the specified synchronization rule.

### 4.12 Create a batch release

Context Not e In Kubernetes clusters of the latest version, alicloud-application-controller is installed by default. This component is only available in Kubernetes 1.9.3 and later. You can upgrade your cluster through the console. Procedure
1. Log on to the Container Service console.
2. In the left-side navigation pane, choose Applicat ions > Releases. Click the Bat ch Release tab
and click Creat e Bat ch Release in the upper-right corner. Not e If the button is dimmed, it indicates that you need to upgrade your cluster first.
3. On the Batch Release Basic Information tab, set the following parameters: application name,
cluster, namespace, and release option. Click Next .
4. On the Batch Release Configuration tab, configure the pods and service, and then click Updat e to
create an application.
5. Go to the Releases page and click the Batch Release tab. You can find the newly created
application and its status is Not St art ed. Click Det ails in the Actions column.
6. On the Details tab, you can find more information about the application. Click Change
Conf igurat ion in the upper-right corner to change the application configuration.
7. On the page that appears, change the configuration and then click Updat e.
8. You are redirected to the Releases page by default. Click the Batch Release tab and you can find
the application status. After the first batch is deployed, click Det ails.
9. On the details tab, two pods are listed in the Not Started list and two pods are listed in the
Completed list. This indicates that the first batch has been released. Click Cont inue to release the second batch of pods. Click Roll Back to roll back to the previous version.
10. After the release is completed, click the Hist ory tab and you can choose to roll back to a previous
version. What's next You can create a batch release to quickly verify the functionalities of a new application version while serving all production traffic. A batch release requires less resources than a blue-green release. Currently, you can only create batch releases through the wizard. Support for YAML configuration files will be available soon.

### 4.13 Use Log Service to collect Kubernetes logs

Kubernetes logs Container Service for Kubernetes is integrated with Log Service. When you create a cluster, you can enable Log Service to collect container logs, including standard outputs and text files. Activate Log Service To activate Log Service, perform the following steps:
1. Log on to the Apsara Stack Cloud Management (ASCM) console. In the top navigation bar, choose
Product s > Log Service to go to the Log Service page.
2. Select the target organization and region.
3. Click SLS to go to the SLS console.
Create a cluster and enable Log Service To create a Kubernetes cluster, perform the following steps:
1. Log on to the Container Service console.
Not e The specified organization must be the same as the one you selected when you activate Log Service. For more information, see Activate Log Service.
2. In the left-side navigation pane, choose Clust ers > Clust ers. The Clusters page appears.
3. Click Creat e Kubernet es Clust er. For more information about the configurations, see Create a
Kubernetes cluster.
4. Select Enable Log Service to install the logging agent.
5. After you select the check box, you must specify a project to store log data. You can click Select
Project and select an existing project from the drop-down list that appears. You can also click Create Project to allow the system to automatically create a project for log management. The project is named `k8s-log-{ClusterID}` , where ClusterID is the unique identifier of the cluster.
6. After you set the parameters, click Creat e Clust er in the upper-right corner. In the dialog box that
appears, click OK to create the cluster. You can find the created cluster on the Clusters page. Install Log Service components in an existing cluster If you have already created a Kubernetes cluster and activated Log Service, you can perform the following steps to use Log Service:
1. Connect to the Kubernetes cluster by using CloudShell.
For more information, see Connect to a Kubernetes cluster through kubectl.
2. Run the script logtail-dedicated.sh to install Log Service components in the cluster.

```
#! /env/bin/bash
yaml=$(cat <<-END --apiVersion: v1 kind: ConfigMap metadata:
  name: alibaba-log-config-file
  namespace: kube-system
data:
  ilogtail_config.json: |
```

`{`

```json
      "config_server_address" : "http://logtail. $REGION.sls-pub. $INTERNET_DOMAIN",
      "data_server_address" : "http://data. $REGION.sls-pub. $INTERNET_DOMAIN",
      "data_server_list" :
```

`[` `{`

```json
              "cluster" : "$REGION",
              "endpoint" : "data. $REGION.sls-pub. $INTERNET_DOMAIN"
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
    log-endpoint: "data. $REGION.sls-pub. $INTERNET_DOMAIN"
    log-machine-group: "k8s-group-$CLUSTER_ID"
    log-config-path: "/etc/ilogtail/conf/apsara/ilogtail_config.json"
    log-ali-uid: "$ALI_UID"
    log-access-id: "" # just use blank string
logaccesskey:""#justuseblankstring
```

```
    log-access-key: "" # just use blank string
--apiVersion: extensions/v1beta1 kind: Deployment metadata:
  name: alibaba-log-controller
  namespace: kube-system
  labels:
    k8s-app: alibaba-log-controller
  annotations:
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
name:alibaba-log-configuration
```

```
                name: alibabalogconfiguration
                key: log-access-id
          - name: "ALICLOUD_ACCESS_KEY_SECRET"
            valueFrom:
              configMapKeyRef:
                name: alibaba-log-configuration
                key: log-access-key
      nodeSelector:
        beta.kubernetes.io/os: linux
--apiVersion: apiextensions.k8s.io/v1beta1 kind: CustomResourceDefinition metadata:
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
```

```
  - update
  - get
- apiGroups: [""]
  resources:
  - events
  verbs:
  - create
  - patch
  - update
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
```

```
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
```

```
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

| 3. Set <your server architecture> , <your k8s cluster region id> , _ _ _ _ _ _ <your k8s cluster id> , <k8s cluster domain suffix> , <your ali uid> _ _ _ _ _ _ _ _ e repo url> to the actual values. Then, run the following commands to set the _ _ | <your server architecture> _ _ | , | <your k8s cluster region id> _ _ _ _ |   | , |
|---|---|---|---|---|---|
|   |   |   |   | <your ali uid> _ _ |   |
| e repo url> _ _ |   |   |   |   |   |

variables for deploying the components.

```
export ARCH=<your_server_architecture> export REGION=<your_k8s_cluster_region_id> export CLUSTER_ID=<your_k8s_cluster_id> export INTERNET_DOMAIN=<k8s_cluster_domain_suffix> export IMAGE_REPO_URL=<your_image_repo_url> export ALI_UID=<your_ali_uid> bash logtail-dedicated.sh // Run the script to install the components.
```

Not e `<your_server_architecture>` : the server architecture, for example, amd64. `<your_k8s_cluster_region_id>` : the region where the cluster is deployed, for example, cn-qingdao-apsara-d01. `<your_k8s_cluster_id>` : the ID of the cluster. `<k8s_cluster_domain_suffix>` : the domain suffix of the cluster, for example, env28.internet.com. `<your_ali_uid>` : the Apsara Stack tenant account ID, for example, 1234074238634394. `<your_image_repo_url>` : the URL of the image repository, for example, registry.cnhangzhou.aliyuncs.com. Create an application and configure Log Service When you create an application in Container Service, you can configure Log Service to collect container logs. Currently, you can only use YAML templates to configure Log Service.
1. In the left-side navigation pane, choose Applicat ions > Deployment s. In the upper-right corner
of the Deployments page, click Creat e f rom T emplat e.
2. Set environment variables in the ENV field to configure log collection and custom tags. To support
the specified log collection, you must set the volumeMounts and volumes fields. YAML templates follow the Kubernetes syntax. The following example shows how to configure Log Service in a pod:

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

Specify the following configurations in sequence to fit your needs: Use environment variables to configure log collection and custom tags. All environment variables must be prefixed with `aliyun_logs_` . Log collection is configured in the following format:

```
- name: aliyun_logs_{Logstore name}
  value: {Log path}
```

In the preceding example, two environment variables are used to configure log collection. The environment variable `aliyun_logs_log-stdout` instructs the system to create a Logstore named log-stdout. The Logstore collects standard output logs from the container in the pod. Not e A Logstore name cannot contain underscores (_). You can use hyphens (-) instead. Cust om t ags are configured in the following format:

```
- name: aliyun_logs_{Tag name without underscores (_)}_tags
  value: {Tag name}={Tag value}
```

After a custom tag is set, it is automatically appended to certain log fields when the Logstore collects logs from the container. If you specify a log path to collect log data other than standard output log data, you must add the volumeMounts field. In the preceding example, the volumeMounts field is added and set to /var/log. This allows the specified Logstore to collect /var/log/*.log files.
3. After you edit the YAML template, click Creat e to submit the configurations.
Advanced configurations You can set more environment variables to apply advanced configurations to log collection. The following table provides details of these variables.

| Variable | Description | Example | Note |
|---|---|---|---|
| aliyun logs {key} _ _ | Required. The key field can contain lowercase letters, digits, and hyphens (- ), and cannot contain underscores ( ). _ If the environment variable aliyun logs {key} log _ _ _ store is not set, a Logstore named {key} is created to collect logs. To collect standard output logs of the container, set the value to stdout. You can also set the value to another Logstore path. | - name: aliyun logs cat _ _ alina stdout - name: aliyun logs acc _ _ ess-log /var/log/nginx/ access.log | By default, the simple mode is used to collect logs. To parse logs, we recommend that you use the Log Service console. The key field must be set to a unique value in the cluster. |
| aliyun logs {key} tags _ _ _ | Optional. This variable is used to add tags to log data. The value must be in the following format: {tag-key}={tag-value}. | - name: aliyun logs catal _ _ ina tags _ app=catalina | - |

| Variable | Description | Example | Note |
|---|---|---|---|
| aliyun logs {key} projec _ _ _ t | Optional. This variable specifies a project in Log Service. By default, the project that you specified when you create the cluster is used to manage related logs and resources in Log Service. | - name: aliyun logs catal _ _ ina project _ my-k8s-project | The region of the project must be the same as where your Logtail is located. |
| aliyun logs {key} logsto _ _ _ re | Optional. This variable specifies a Logstore in Log Service. By default, the Logstore is named after {key}. | - name: aliyun logs catal _ _ ina tags _ my-logstore | - |
| aliyun logs {key} shard _ _ _ | Optional. This variable specifies the number of shards in the Logstore. Valid values: 1 to 10. Default value: 2. | - name: aliyun logs catal _ _ ina shard _ 4 | - |
| aliyun logs {key} ttl _ _ _ | Optional. This variable specifies the number of days for which log data is retained. Valid values: 1 to 3650. To retain log data permanently, set the value to 3650. Default value: 90. | - name: aliyun logs catal _ _ ina ttl _ 3650 | - |
| aliyun logs {key} machi _ _ _ negroup | Optional. This variable specifies the machine group of the application. By default, the machine group is the one where your Logtail is located. | - name: aliyun logs catal _ _ ina machinegroup _ my-machine- group | - |

Scenario 1: Collect logs from multiple applications and store them in the same Logstore In this scenario, you can set the aliyun_logs_{key}_logstore variable. The following example shows how to collect standard output logs from two applications and store them in stdout-logstore. Set the following environment variables for Application 1:

```
######### Set environment variables ###########
    - name: aliyun_logs_app1-stdout
      value: stdout
    - name: aliyun_logs_app1-stdout_logstore
      value: stdout-logstore
```

Set the following environment variables for Application 2:

```
######### Set environment variables ###########
    - name: aliyun_logs_app2-stdout
      value: stdout
    - name: aliyun_logs_app2-stdout_logstore
      value: stdout-logstore
```

Scenario 2: Collect logs from different applications and store them separately in different projects In this scenario, perform the following steps: i. Create a machine group in each project and set the machine group ID in the following format: k8s-group-{cluster-id}, where {cluster-id} is the ID of the cluster. You can customize machine group names. ii. Specify the project, Logstore, and machine group in the environment variables for each application.

```
######### Set environment variables ###########
    - name: aliyun_logs_app1-stdout
      value: stdout
    - name: aliyun_logs_app1-stdout_project
      value: app1-project
    - name: aliyun_logs_app1-stdout_logstore
      value: app1-logstore
    - name: aliyun_logs_app1-stdout_machinegroup
      value: app1-machine-group
```

View log data To view log data, perform the following steps:
1. Log on to the Log Service console. For more information, see Activate Log Service.
2. Select the target project. By default, the project ID is k8s-log-{Cluster ID}.
3. In the list of Logstores, find the target Logstores and click Search in the Log Search column for
each Logstore. In this example, the Logstores are log-stdout and log-varlog.
4. On the Raw Logs tab, you can view raw logs in log-stdout and log-varlog.
