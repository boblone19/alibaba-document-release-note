---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 26
source_pdf: "ffaac6cd8d8b6e45_Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Operations and Maintenance "
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20ACK/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Container%20Service%20for%20Kubernetes%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Before you start
- 2 Architecture
  - 2.1 System architecture
  - 2.2 Architecture
  - 2.3 Deployment architecture
  - 2.4 Server roles
- 3 ACK cluster O&M
- 4 Component O&M
  - 4.1 Components
- 5 GUI-based changes
  - 5.1 Kubernetes version baselines
  - 5.2 Troopers configurations
- 6 Log management
- 7 Operation audit
- 8 etcd O&M
  - 8.1 etcd backup

## 1 Before you start

Container Service for Kubernetes (ACK) provides container services. You may encounter service interruptions if you perform improper operations on applications in your ACK clusters. This topic describes the usage notes of ACK clusters and instructions on high-risk operations. This helps you learn the risks that may arise when you use ACK clusters.

**Usage notes**

**Data plane components**

Data plane components are system components that run on your Elastic Compute Service (ECS) instances. Data plane components include CoreDNS, Ingresses, kube-proxy, Terway, and the kubelet. You and the ACK team must collaborate to ensure the stability of data plane components that run on your ECS instances. When you use data plane components, we recommend that you take note of the following items: Modifying the component configuration may cause the component to malfunction. Exercise caution when you modify the component configuration. For more information, see
**Container Service for Kubernetes User Guide** > **Components** > **Manage**
**components**.
Do not use the APIs of Infrastructure as a Service (IaaS) services to modify the environment of data plane components. For example, do not use the ECS API to change the status of the ECS instances on which data plane components run, or modify the security groups or network settings of the worker nodes. Do not use the Server Load Balancer (SLB) API to modify the configurations of the SLB instances that are used by your cluster. Improper changes to the IaaS resources may cause the components to malfunction. Several data plane components may have the same bugs or vulnerabilities as the corresponding open source versions. Update your components at the earliest opportunity in case the bugs or vulnerabilities affect your business.

**Cluster updates**

Use the cluster update feature that is provided by ACK to update the Kubernetes version of ACK clusters. If you use other methods to update the Kubernetes version of your ACK clusters, stability or compatibility issues may occur in the ACK clusters. For more information, see
**Container Service for Kubernetes User Guide** > **Kubernetes clusters** > **Clusters** >
**Update the Kubernetes version of a cluster** .
ACK provides the following features to update clusters: Version updates for ACS clusters. Release notes for new Kubernetes versions. The release notes describe new Kubernetes versions and compare new versions with earlier versions. Notifications for potential risks due to resource changes. This feature can inform you of the risks that may arise due to resource changes caused by version updates. We recommend that you follow these suggestions when you use the cluster update feature: Read the release notes of the new Kubernetes versions, confirm the status of the cluster and workloads based on the update risks that are reported by ACK, and evaluate the impacts of the risks. For more information, see **Container Service for Kubernetes User**
**Guide** > **Announcements** and **Container Service for Kubernetes User Guide** >
**Kubernetes clusters** > **Clusters** > **Update the Kubernetes version of a cluster** .
You cannot roll back cluster updates. Before you update a cluster, prepare for the update and make a backup plan.

**Kubernetes configurations**

Do not change key Kubernetes configurations. For example, do not change the following directories or modify the paths, links, and content of the files in the directories: /var/lib/kubelet /var/lib/docker /etc/kubernetes /etc/kubeadm /var/lib/containerd Do not use annotations that are reserved by Kubernetes in YAML templates. Otherwise, resource unavailability, application failures, and exceptions may occur. Labels prefixed with

| kubernetes.io/ |   | or | k8s.io/ | are reserved for key comp |
|---|---|---|---|---|
| the annotation |   |   |   |   |

**App catalog**

The application marketplace of ACK provides the app catalog feature to help you install applications that are developed based on open source versions. Open source applications may have potential risks. Proceed with caution.

**High-risk operation**

The following high-risk operations may adversely affect your business when you work with ACK. Read and understand the impacts of the following high-risk operations before you perform these operations:

**High-risk operations on clusters**

| Category | High-risk operation | Impact | How to recover |
|---|---|---|---|
| API Server | Delete the SLB instance that is used to expose the API server. | You cannot manage the cluster. | Unrecoverable. You must create a new cluster. |
|   | Modify the security group of nodes. | The nodes may become unavailable. | Add the master nodes to the original security groups again. The security groups are created when you create the cluster. For more information, see ECS User Guide > Security groups > Add an instance to a security group. |
|   | Remove nodes. | The nodes become unavailable. | Unrecoverable. |
|   | Reinstall the node OS. | Components are uninstalled from nodes. | Remove the worker nodes and then add the nodes to the cluster again. |

| Worker nodes |   |   |   |
|---|---|---|---|
|   | Update component versions. | The nodes may become unavailable. | Roll back to the original component versions. |
|   | Change the IP addresses of nodes. | The nodes become unavailable. | Change the IP addresses of the nodes to the original IP addresses. |
|   | Modify the parameters of key components, such as kubelet, docker, and containerd. | The nodes may become unavailable. | Refer to the ACK official documentation and configure the component parameters. |
|   | Modify node OS configurations. | The nodes may become unavailable. | Restore the configurations, or remove the worker nodes and then purchase new nodes. |
| Master nodes in ACK dedicated clusters | Modify the security group of master nodes. | The master nodes may become unavailable. | Add the master nodes to the original security groups again. The security groups are created when you create the cluster. For more information, see ECS User Guide > Security groups > Add an instance to a security group. |
|   | Remove master nodes. | The master nodes become unavailable. | Unrecoverable. |
|   | Reinstall the node OS. | Components are uninstalled from master nodes. | Unrecoverable. |
|   | Update master nodes or the etcd component. | The cluster may become unavailable. | Roll back to the original version. |
|   | Delete or format the directories that store business-critical data on nodes, for example, /etc/kubernetes. | The master nodes become unavailable. | Unrecoverable. |
|   | Change the IP addresses of master nodes. | The master nodes become unavailable. | Change the IP addresses of the master nodes to the original IP addresses. |

|   | Modify the parameters of key components, such as etcd, kube-apiserver, and docker. | The master nodes may become unavailable. | Refer to the ACK official documentation and configure the component parameters. |
|---|---|---|---|
|   | Replace the certificates of master nodes or the etcd. | The cluster may become unavailable. | Unrecoverable. |
|   | Increase or decrease the number of master nodes. | The cluster may become unavailable. | Unrecoverable. |
| Other services | Use Resource Access Management (RAM) to modify permissions. | You may fail to create specific resources, such as SLB instances. | Restore the permissions. |

**High-risk operations on node pools**

| High-risk operation | Impact | How to recover |
|---|---|---|
| Delete scaling groups. | Node pool exceptions occur. | Unrecoverable. You must create new node pools. |
| Use kubectl to remove nodes from a node pool. | The number of nodes in the node pool that is displayed in the ACK console is different from the actual number. | Remove the nodes by using the ACK console or by calling the ACK API. For more information, see Container Service for Kubernetes User Guide > Kubernetes clusters > Node management > Nodes > Remove a node. |
| Manually release ECS instances. | Incorrect information may be displayed on the node pool details page. | Unrecoverable. Remove the nodes by using the ACK console or by calling the ACK API. For more information, see Container Service for Kubernetes User Guide > Kubernetes clusters > Node management > Nodes > Remove a node. |
| Manually scale in or scale out a node pool that has auto scaling enabled. | The auto scaling component automatically adjusts the number of nodes in the node pool after you manually scale in or scale out the node pool. | Unrecoverable. You do not need to manually scale a node pool that has auto scaling enabled. |

| Change the upper or lower limit of instances that a scaling group can contain. | Scaling errors may occur. | For a node pool that has auto scaling disabled, the default upper limit of instances for the scaling group is 2,000, and the default lower limit of instances is 0. For a node pool that has auto scaling enabled, make sure that the upper and lower limits of instances for the scaling group are the same as the upper and lower limits of instances for the node pool. |
|---|---|---|
| Add existing nodes to a cluster without backing up the data on the nodes. | The data on the nodes is lost after the nodes are added to the cluster. | Unrecoverable. If you want to add existing nodes in Manual mode, you must first back up the data on the nodes. If you want to add existing nodes in Auto mode, you must first back up the data on the system disks because the system disks will be replaced when the nodes are added to the cluster. |

**High-risk operations on networks and load balancing**

| High-risk operation | Impact | How to recover |
|---|---|---|
| Specify the following kernel setting: net.ipv4.ip forward=0 . _ | Network connectivity issues occurred. | Replace the setting with the following content: net.ipv4.ip forward=1 . _ |

| Specify the following kernel parameter settings: net.ipv4.conf.all.rp fil _ ter = 1\|2 | Network connectivity issues occurred. |   | Replace the settings with the following content: net.ipv4.conf.all.rp fil _ ter = 0 |   |
|---|---|---|---|---|
| net.ipv4.conf. [ethX].rp filter = 1\|2 _ Note ethX specifies the network interface controllers whose names start with eth . |   |   |   |   |
|   |   | connectivity issues d. |   |   |
|   |   |   | net.ipv4.conf. [ethX].rp filter = 0 _ |   |
| Specify the following kernel parameter setting: net.ipv4.tcp tw reuse = _ _ 1 . | Pods fail to pass health checks. |   | Replace the setting with the following content: net.ipv4.tcp tw reuse = _ _ 0 . |   |
| Specify the following kernel setting: net.ipv4.tcp tw recycle = _ _ 1 . | Network address translation errors occur. |   | Replace the setting with the following content: net.ipv4.tcp tw recycle = _ _ 0 . |   |
| Specify the following kernel setting: net.ipv4.ip local port ran _ _ _ ge . | Network connectivity issues occasionally occur. |   | Replace the setting with the following content: net.ipv4.ip local port ran _ _ _ ge="32768 60999" . |   |
| Install firewall software, for example, Firewalld or ufw. | The container network becomes inaccessible. |   | Uninstall the firewall software and restart the nodes. |   |
| The security group of a node does not open UDP port 53 for the pod CIDR block. | DNS resolutions cannot be performed as normal in the cluster. |   | Refer to the ECS official documentation and modify the security group configuration to open UDP port 53 for the pod CIDR block. |   |
| Modify or delete the tags that ACK added to SLB instances. | The SLB instances cannot work as normal. |   | Restore the tags. |   |
| Modify the configurations of the SLB instances that are managed by ACK, including the configurations of the instances, listeners, and vServer groups. | The SLB instances cannot work as normal. |   | Restore the SLB configurations. |   |

| net.ipv4.conf.all.rp fil _ |   |
|---|---|

|   | [ethX].rp filter = 1\|2 _ |   |
|---|---|---|

| net.ipv4.conf.all.rp fil _ |   |
|---|---|

|   | [ethX].rp filter = 0 _ |   |
|---|---|---|

|   | net.ipv4.tcp tw reuse = _ _ |
|---|---|
| 1 |   |

|   |   | net.ipv4.tcp tw reuse = _ _ |
|---|---|---|
|   | 0 |   |

|   | net.ipv4.tcp tw recycle = _ _ |   |
|---|---|---|
| 1 |   |   |

|   |   | net.ipv4.tcp tw recycle = _ _ |   |
|---|---|---|---|
|   | 0 |   |   |

| net.ipv4.ip local port ran _ _ _ | o |
|---|---|

|   |   | net.ipv4.ip local port ran _ _ _ |
|---|---|---|
|   | ge="32768 60999" |   |

| Remove the annotation service.beta.kubernetes.io |   |   | Add the annotation to the Service configuration. Note If a Service uses an existing SLB instance, you cannot modify the configuration to create an SLB instance for the Service. To use a newly created SLB instance, you must create a new Service. |   |
|---|---|---|---|---|
|   | service.beta.kubernetes.io |   |   | Note |
| /alibaba-cloud- |   |   |   |   |
| loadbalancer-id: |   | T |   |   |
| ${YOUR LB ID} _ _ |   |   |   |   |
| Delete the SLB instances that are created by ACK in the SLB console. |   | Errors may occur on the cluster network. | Delete SLB instances by deleting the Services that are associated with the SLB instances. |   |
| Manually delete the nginx- ingress-lb Service in the kube-system namespace of a cluster that has the NGINX Ingress controller installed. |   | The NGINX Ingress controller does not run as normal or may stop running. | Use the following YAML template to create a Service that has the same name: apiVersion: v1 kind: Service metadata: annotations: labels: app: nginx-ingress- lb name: nginx-ingress-lb namespace: kube-system spec: externalTrafficPolicy: Local ports: - name: http port: 80 protocol: TCP targetPort: 80 - name: https port: 443 protocol: TCP targetPort: 443 selector: app: ingress-nginx type: LoadBalancer |   |

| nginx- |   |
|---|---|

|   | ingress-lb |
|---|---|

**High-risk operations on storage**

| High-risk operation | Impact | How to recover |
|---|---|---|

| Unmount cloud disks that are mounted to pods in the ECS console. | I/O errors occur when you write data to the pods. | Restart the pods and clear residual data on the nodes. |
|---|---|---|
| Unmount disks from their mount paths on nodes. | Pod data is written to local disks. | Restart the pods. |
| Manage cloud disks on the nodes. | Pod data is written to local disks. | Unrecoverable. |
| Mount a cloud disk to multiple pods. | Pod data is written to local disks or I/O errors occur when you write data to the pods. | Mount the cloud disk only to one pod. |
| Manually delete the NAS directories that are mounted to pods. | I/O errors occur when you write data to the pods. | Restart the pods. |
| Delete the NAS file systems that are mounted to pods or delete the mount targets that are used to mount NAS file systems. | I/O hangs occur when you write data to the pods. | Restart the ECS instances. |

**High-risk operations on logs**

| High-risk operation | Impact | How to recover |
|---|---|---|
| Delete the /tmp/ccs-log- collector/pos directory on a node. | Duplicate logs are collected. | Unrecoverable. The /tmp/ccs- log-collector/pos directory contains information about the path from which logs are collected. |
| Delete the /tmp/ccs-log- collector/buffer directory on a node. | Logs are lost. | Unrecoverable. The /tmp/ccs- log-collector/buffer directory stores cached log files that need to be consumed. |

| Delete the aliyunlogconfig CustomResourceDefinition (CRD) objects. | Logs cannot be collected. | Recreate the aliyunlogconfig CRD objects that are deleted and the related resources. Logs that are generated within the period of time during which the aliyunlogconfig CRD objects do not exist cannot be collected. If you delete the aliyunlogconfig CRD objects, the related log collection tasks are also deleted. After you recreate the aliyunlogconfig CRD objects, you must also relaunch the log collection tasks. |
|---|---|---|
| Uninstall the logging component. | Logs cannot be collected. | Reinstall the logging component and manually create the aliyunlogconfig CRD objects. Logs that are generated within the period of time during which the logging component and the aliyunlogconfig CRD objects do not exist cannot be collected. If you delete the logging component, the aliyunlogconfig CRD objects and Logtail are also deleted. Logs that are generated within the period of time during which the logging component does not exist cannot be collected. |

## 2 Architecture

### 2.1 System architecture

This topic describes the system architecture of Container Service for Kubernetes (ACK). Container Service is adapted and enhanced based on native Kubernetes. This service simplifies cluster creation and scaling, and is integrated with Apsara Stack virtualization, storage, network, and security capabilities. This service provides the optimal environment to run Kubernetes-based containerized applications in the cloud.

| Feature | Description |
|---|---|
| Dedicated Kubernetes mode | Integrated with Apsara Stack virtualization technologies, the service allows you to create dedicated Kubernetes clusters. You can use Elastic Compute Service (ECS), Elastic GPU Service (EGS), and ECS Bare Metal instances as cluster nodes. You can deploy a wide range of plug-ins and configure various specifications for the instances. |
| Cluster management and control | The service provides powerful network, storage, cluster management, scaling, and application extension features. |
| Kubernetes management | The service supports secure images and is integrated with Apsara Stack Resource Access Management (RAM), Key Management Service (KMS), and logging and monitoring services to provide a secure and compliant Kubernetes solution. |

| Convenient and efficient use | ACK provides services through the web console, APIs, and SDK. |
|---|---|

### 2.2 Architecture

This topic describes the component architecture of Container Service for Kubernetes (ACK).

| Category | Component | Description |
|---|---|---|
| Apsara Stack Container Service console | CosConsoleAliyunCom | The console that is used to manage clusters, nodes, and applications. |
|   | Backend | Dashboard. |
| Apsara Stack Container Service controller | Troopers | Controller backend. |
|   | RC | Component installation service. |
|   | CloudAccessVpc | Reverse tunneling. |
|   | Cert | Static file service. |
|   | CertControl | Component certificate signing. |
|   | Registry | Image service. |
| > Document Version: 20260828 | 1 |   |

|   | Mirana | API server traffic forwarding. |
|---|---|---|
|   | Certificate | Certificate update. |
| ACK tools | ControlInit | Data initialization and API registration. |
|   | ServiceTest | Self-check service. |
|   | DiagnosticTool | Quick diagnostic tool. |

### 2.3 Deployment architecture

This topic describes the deployment architecture of Container Service for Kubernetes (ACK).

| Component | Deployment method |
|---|---|
| Apsara Stack Container Service console | Containerized deployment |
| Apsara Stack Container Service controller | Containerized deployment |
| Container Service tools | Containerized deployment |

### 2.4 Server roles

This topic describes the server roles of Container Service for Kubernetes (ACK).

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|

| acs | AcsControlCluste r | acs-acs control _ | ControlInit | Data initialization and API registration. |
|---|---|---|---|---|
|   |   |   | Troopers | Controller backend. |
|   |   |   | CloudAccessVpc | Reverse tunneling. |
|   |   |   | Cert | Static file service. |
|   |   |   | CertControl | Component certificate signing. |
|   |   |   | Registry | Image service. |
|   |   |   | Mirana | API server traffic forwarding. |
|   |   |   | Backend | Dashboard. |
|   |   |   | CosConsoleAliyun Com | Console. |
|   |   |   | Certificate | Certificate updates. |
|   |   |   | ServiceTest | Self-check service. |
|   |   |   | DiagnosticTool | Quick diagnostic tool. |

## 3 ACK cluster O&M

This topic described how to view the basic information about all Container Service for Kubernetes (ACK) clusters on the ACK Clusters page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, click **ACK Clusters** to go to the ACK Clusters page. You
can view the following information on the page: **Clusters**, **Nodes**, **Kubernetes Versions**,
**Operating Systems**, and brief information about all ACK clusters.
3. In the **Clusters** section, you can view information about all clusters. You can also search
for clusters by **Name**, **Status**, **Type**, and **Label**.

| Column | Description |
|---|---|
| Cluster ID/Name | The ID and name of the cluster. |
| Cluster Status | The status of the cluster, such as Running or Create Failed. |
| Label | The labels that are added to the cluster. |
| Type | The type of the cluster. For example, the cluster is an ACK dedicated cluster. |
| Nodes | The number of nodes in the cluster. You can click the number in the column to go to the Node Management page and view node information in the list. On the Node Management page, click the ID of a node to view the basic information of the node. |
| Usage | The CPU utilization and memory usage of the cluster. |
| Version | The Kubernetes version of the cluster. |
| Created At | The time when the cluster was created. |

| Actions | The operations that you can perform on the cluster. For example, you can click View Logs in the Actions column to view the cluster logs. |
|---|---|

4. Find the cluster that you want to manage and click its name in the **Cluster ID/Name**
column to go to the cluster details page. The following parameters are displayed in the Cluster Information section of the Basic Information tab: **API Server Internal Endpoint**,
**Pod Network CIDR**, **Service CIDR**, **Kube-proxy Mode**, **Node IP Addresses**, and
**Network Plug-ins**.

## 4 Component O&M

### 4.1 Components

This topic describes how to view the basic information about all components on the Component List page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, choose **Component OPS > Component List**. On the
Component List page, view the information about all components in the environment.
3. On the **Component List** list, search for components by component name or component
version. Find the component that you want to manage and click its name in the **Name** column to go to the **Component Details** page.

> **Note:** You can also click **View Cluster** in the **Actions** column to view the status of the cluster that is associated with the component.

4. On the **Component Details** page, view the basic information about the component. The
following parameters are displayed: **Component Name**, **Component ID**, **Component**
**Type**, **Created At**, **Component Description**, and **Component Template**.

## 5 GUI-based changes

### 5.1 Kubernetes version baselines

This topic describes how to view the information about baselines on the **K8S version**
**baseline** page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, choose **ACK Change > Version Baseline**. On the K8S
version baseline page, view the baseline information displayed in the following columns:
**Name**, **Baseline Type**, **Version**, **Cluster Type**, **Property**, **Creation Time**, and
Operation. You can also search for baselines by name.

> **Note:** To view the YAML or JSON file of the baseline, click the file in the **Actions** column.

### 5.2 Troopers configurations

This topic describes how to view and modify the information about troopers configurations on the Troopers Configurations page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, choose **ACK Change > Troops Config**. On the Troopers
Configurations page, view the name, content, creation time, and update time of each configuration item, and the operations that you can perform on each configuration item. You can also search for configuration items by name.
3. Find the configuration item that you want to manage and click **View Configuration** in the
**Actions** column to view the configuration. You can also click **Update configuration** in the
**Actions** column to modify the configuration.

## 6 Log management

This topic describes how to query and view service logs such as troopers logs.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, click **Log Management**. On the page that appears, search
for logs, such as troopers logs, by Logstore and time range.

## 7 Operation audit

This topic describes how to view the information about operations.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, click **Operation Audit**. On the page that appears, view
the operation information in the following columns: **Change Name**, **Change Description**,
**Operation Type**, **Operation Object**, **Change Type**, **Status**, and **User**.

> **Important:** In the **Actions** column, click **View Change** to view the change in read-only mode or click **Roll Back Change** to roll back the change.

## 8 etcd O&M

### 8.1 etcd backup

This topic describes how to back up the etcd data of a Container Service for Kubernetes (ACK) cluster and view historical backup information on the ETCD Backup Records page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Product Operation > Computing > Container Operations Console**.
2. In the left-side navigation pane, click **ETCD Backup Records**. On the **ETCD Backup**
**Records** page, you can view the following information about an etcd backup record:
**cluster ID**, **bucket**, **user ID**, **ID**, **log**, **creation time**, and **status**.
3. In the upper-left corner of the page, click **Back Up**. In the Create etcd dialog box, configure
the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Access key | The AccessKey ID. |
| Access secret | The AccessKey secret. |

| Cluster ID | The ID of the cluster. |
|---|---|
| Bucket name | The name of the Object Storage Service (OSS) bucket that stores the etcd data. |
