---
title: "Container Service for Kubernetes Product Introduction 20251202"
product_version: "V3.18.6"
pdf_pages: 23
source_pdf: "39fd1960e423baba_Alibaba Cloud Apsara Stack V3.18.6 Container Service for Kubernetes Product Introduction 20251202.pd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1Kubernetes%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Service%20for%20Kubernetes%20Product%20Introduction%2020251202.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Container Service for Kubernetes Product Introduction 20251202

## Table of Contents

- 1 What is Container Service?
- 2 Features
- 3 Benefits
- 4 Architecture
- 5 Features
- 6 Scenarios
- 7 Limits
- 8 Terms

tainer Service?

## 1 What is Container Service?

Container Service provides high-performance, scalable, and enterprise-class management services for Kubernetes containerized applications throughout the application lifecycle. Container Service simplifies the deployment and scale-out operations of Kubernetes clusters and is empowered by the capabilities of virtualization, storage, networking, and security provided by Alibaba Cloud. Based on these capabilities, Container Service provides an ideal runtime environment for containerized applications. Alibaba Cloud is a Kubernetes Certified Service Provider (KCSP). As one of the first services to participate in the Certified Kubernetes Conformance Program, Container Service provides enterprises with professional support and services.

## 2 Features

**Features of Container Service**

**Cluster management**

Allows you to create a dedicated Kubernetes cluster that contains GPU servers within 10 minutes in the Container Service console. Provides OS images that are optimized for containerized applications and supports Kubernetes versions and Docker versions with high stability and enhanced security. Supports multi-cluster management, cluster updates, and cluster scaling.

**Provides all-in-one container lifecycle management**

**Network**

Provides high-performance virtual private clouds (VPCs) and elastic network interfaces (ENIs) that are optimized for Alibaba Cloud, boasting 20% increased performance compared with regular network solutions. Supports access control and traffic throttling for containers.

**Storage**

Supports Alibaba Cloud disks and OSS buckets, and provides the standard FlexVolume driver. Supports dynamic volume creation and migration.

**Logs**

Provides high-performance log collection based on Log Service. Supports the integration with third-party open source logging solutions.

**Monitoring**

Supports container-level and VM-level monitoring. You can also integrate Container Service with third-party open source monitoring solutions.

**Permissions**

Supports cluster-level Resource Access Management (RAM) authorizations. Supports application-level permission configuration and management.

**Application management**

Supports canary release and blue-green releases. Supports application monitoring and scaling.

**High-availability scheduling policies that integrate upstream and downstream**

**delivery processes**

Supports service-level affinity policies and scale-out. Provides cross-zone high availability and disaster recovery. Provides API operations for cluster and application management to easily implement continuous integration and integrate with private deployment systems.

## 3 Benefits

**Overview**

**Easy to use**

You can easily create Kubernetes clusters in the Container Service console. You can easily upgrade Kubernetes clusters in the Container Service console. When you use custom Kubernetes clusters, you may need to handle clusters of different versions. Currently, each time you upgrade the clusters, you need to make major adjustments and high operation and maintenance costs are incurred. Container Service allows you to perform rolling upgrades based on images and supports full metadata backups. You can easily roll back clusters to previous versions. Allows you to easily scale Kubernetes clusters in the Container Service console. Kubernetes clusters enable you to quickly scale up or down applications to handle traffic fluctuations in a timely manner.

| Feature | Description |
|---|---|
| Network | Supports continuous network integration to optimize network performance. |
| Load balancing | Allows you to create public and internal SLB instances. If you use an Ingress to control access to your Kubernetes cluster, frequent service releases may negatively affect the performance of the Ingress and increase the error rate. Container Service allows you to create SLB instances, which provide high availability load balancing and can automatically modify network configurations to suit your business needs. This solution is adopted by a large number of users and has been proven to be a more stable and reliable alternative to Ingresses. |
| Storage | Supports Apsara Stack cloud disks, Network Attached Storage (NAS), and Block Storage, and provides FlexVolume drivers. Supports seamless integration with cloud storage services for custom Kubernetes clusters that cannot use cloud storage resources. |
| O&M | Supports integration with Apsara Stack Log Service. Supports automatic scaling. |

| Image repository | Provides high availability and high concurrency. Supports accelerated image retrieval. Supports peer-to-peer image distribution. Custom image repositories may stop responding when millions of clients attempt to pull images at the same time. Container Service provides an image repository system that offers enhanced reliability and reduces O&M and upgrade costs. |
|---|---|
| Stability | Dedicated support teams guarantee the stability of containers. All Linux and Kubernetes versions must pass rigorous testing before they are available to the public. Container Service supports Docker CE and provides a Docker community to help you communicate with other Docker enthusiasts and solve problems. Best practices are provided to help you address issues, such as network interruptions, kernel incompatibilities, or Docker crashes. |
| Technical support | Allows you to quickly upgrade Kubernetes clusters to the latest version. Provides professional technical support services to help you solve the issues that may occur when you use containers. |

## 4 Architecture

Container Service is adapted and enhanced on the basis of native Kubernetes. This service simplifies cluster creation and scaling and integrates Apsara Stack virtualization, storage, network, and security capabilities, providing the optimal environment to run Kubernetesbased containerized applications in the cloud.

| Feature | Description |
|---|---|
| Dedicated Kubernetes mode | Integrated with Apsara Stack virtualization technologies, the service allows you to create dedicated Kubernetes clusters. ECS, Elastic GPU Service (EGS), and ECS Bare Metal instances can all be used as cluster nodes. Instances support a wide range of plug-ins and can be flexible configured to different specifications. |
| Alibaba Cloud Kubernetes cluster management and control service | The service provides powerful network, storage, cluster management, scaling, and application extension features. |
| Alibaba Cloud Kubernetes management service | The service supports secure images and is highly integrated with Apsara Stack Resource Access Management (RAM), and logging and monitoring services to provide a secure and compliant Kubernetes solution. |
| Convenient and efficient use | Container Service for Kubernetes provides services through the Web console, APIs, and SDKs. |

## 5 Features

Container Service for Kubernetes is a high-performance, scalable container management service with powerful Kubernetes cluster management capabilities. It provides a comprehensive container cluster management solution that includes cluster management, operations and maintenance, high availability, and container image management. It offers professional support to efficiently manage the entire lifecycle of Kubernetes containerized applications in the cloud. The specific features and detailed descriptions are as follows:

**Cluster management**

| Feature | Description |
|---|---|
| Master node management | Supports 3/5 node high availability. Supports OS rotation and replacement for master nodes. Enables deletion protection for API Server SLB by default and supports access to the API Server through both public and private networks. |
| Namespace management | Provides lifecycle management for namespaces and supports setting resource quotas and default resource limits. |
| Authorization management | Supports a combination of RBAC and RAM permissions. Permission types include the following: administrator, O&M personnel, developer, and restricted user. Allows revoking kubeconfig permissions and granting different types of permissions to sub-accounts based on cluster or namespace scope. Also supports login through ASCM STS role assumption. |
| Cluster management | For cluster creation and co-deployment capabilities, supports deploying both X86 and ARM architecture ECS instances simultaneously, using ECS instances with the same chip instruction set within a cluster, customizing service domain names and network configurations, and continuously releasing versions compatible with newly released K8s community versions. Supports one-click upgrade of K8s versions. Supports adding tags to clusters. |
| License management | Supports metering and control of licenses. |
| Cluster registration | Supports creating registered clusters and managing offline K8s clusters, allowing you to manage multiple clusters uniformly and improving the flexibility of operations management. |

**Node pool management**

| Feature | Description |
|---|---|

| Operating system | Supports multiple operating systems, including Alibaba Cloud Linux 3, Alibaba Cloud Server OS V3, Anolis, UnionTech UOS, and Kylin V10, and more. |
|---|---|
| Node configuration | Supports creating GPU worker nodes and ECS Bare Metal instances, and deploying worker nodes across availability zones. Supports placing nodes in specific deployment sets. Supports custom data, node names, and images. Supports DDH instance types. |
| Network and security | Allows binding public IP addresses to worker nodes, supports enabling deletion protection for ECS nodes and selecting existing security groups, and provides data disk encryption to ensure security and data protection. |
| Monitoring and plugin support | Supports deploying CloudMonitor plugins on node pools for real-time monitoring of resource usage and performance. |
| Node pool lifecycle management | Supports scaling out existing nodes or adding new nodes automatically or manually. Supports automatic scaling management of nodes, node removal, node label and taint management, and provides node maintenance capabilities. |

**Container network**

| Feature | Description |
|---|---|
| Terway container network | Supports Terway container network 2.0 and provides ipvlan+ebpf mode network configuration, supporting IPv6 dual-stack capabilities and Trunking ENI functionality. |
| Network policy and management | Supports defining Network Policy and configuring CIDR for Services and Pods, enabling more flexible network management. |
| SLB and DNS support | Supports enabling deletion protection when creating SLB. Features DNS local caching to improve domain name resolution efficiency. |
| Flannel mode | Provides VPC Flannel mode to meet the requirements of various network scenarios. |

**Network management**

| Feature | Description |
|---|---|
| Service management | Provides creation, viewing, updating, and deletion functions for service lifecycle management. Supports multiple access methods, including Cluster IP, Node Port, and Load Balancer. Supports viewing and updating services via scripts and creating Headless Services. |
| Ingress management | Supports accessing services through domain names and provides weight-based multi-service access control. Supports viewing and updating routing configurations via scripts, along with configuring service phased release strategies to meet different release scenarios. Supports full lifecycle management of routes, including creation, viewing, updating, and deletion. |
| Configuration management | Supports configuration management for Config Maps and Secrets, allowing you to manage configuration information and sensitive data in workloads, enhancing application security and flexibility. |

**Workload management**

| Feature | Description |
|---|---|
| Container instance management | Supports setting limits on the number of container instances per node. Supports viewing container instance events. Supports terminal access to container instances for real-time management and debugging. |
| Workload scaling | Provides HPA (Horizontal Pod Autoscaler) auto-scaling policy that can automatically adjust the number of container instances based on load. Also supports manual scaling operations to flexibly respond to resource demand changes. |
| Workload creation | Supports creating various types of workloads, including Job applications, DaemonSets, CronJobs, stateless applications (Deployments), and stateful applications (StatefulSets). Supports creating workloads from ACR Enterprise Edition images, templates, or images. Supports configuring health checks, environment variables, data disk mounting, and log collection paths to ensure workload stability and monitoring capabilities. |

| Workload lifecycle management | Allows comprehensive management of application event viewing, application version rollback, replacement upgrades, viewing, updating, and deletion operations. Also supports rolling upgrades and trigger redeployment operations for applications, providing flexibility for operations and maintenance. Supports viewing and updating applications via scripts, simplifying O&M processes. |
|---|---|
| Workload scheduling | Supports node affinity, inter-application affinity, and anti-affinity scheduling policies to optimize resource configuration and improve cluster resource utilization and application running efficiency. |

**Container storage**

| Feature | Description |
|---|---|
| Persistent volumes and volume claims | Supports snapshots and restoration of persistent volumes (PVs) and persistent volume claims (PVCs), allowing you to back up and recover data, ensuring data security and reliability. |
| Storage management | Supports viewing and updating persistent volumes and volume claims via scripts, enabling automated management and improving operational efficiency. |
| Storage class support | Supports creating various types of persistent volumes, including Elastic Block Storage, Network Attached Storage (NAS), and Object Storage Service, to meet different application requirements and scenarios. |
| Volume claim attachment | Supports creating persistent volume claims to attach persistent volumes, ensuring applications can dynamically bind storage resources as needed, improving resource utilization. |
| Storage plugin support | Supports the Container Storage Interface (CSI) storage plugin, allowing integration of various storage solutions in Kubernetes environments, thereby extending storage functionality and enhancing flexibility. |

**Cloud-native AI capabilities**

| Feature | Description |
|---|---|
| AI component set | Supports deploying AI component sets in edge clusters, fully utilizing edge computing resources to improve the efficiency of big data processing and AI inference. |

| Hardware compatibility | Supports high-performance GPU models such as NVIDIA A100 and V100 to meet the requirements of AI and big data applications with high computational demands. |
|---|---|
| GPU resource sharing | Provides GPU share functionality, allowing multiple applications to share GPU resources, improving resource utilization and adapting to different load requirements. |
| Component support | Supports components such as Queue and Arena, providing efficient task scheduling and resource management, enhancing the operational efficiency of AI tasks. |
| Operating system compatibility | The AI component set is compatible with Alibaba Cloud Linux 3.2.10 and Anolis 8.6 ANCK versions, ensuring consistency and compatibility across different environments. |
| Cluster scheduling policy | The cluster scheduler supports various scheduling policies, including Gang scheduling and Capacity scheduling, to optimize resource allocation and task execution order. |

**Operations and monitoring**

| Feature | Description |
|---|---|
| Intelligent diagnostics | Provides diagnostic capabilities for pods within the cluster, supporting real-time monitoring and analysis of pod status, helping operations personnel quickly locate and resolve potential issues, improving cluster stability and reliability. |
| Node diagnostics | Supports diagnostic functions for nodes within the cluster, providing node status information to help you comprehensively understand node health conditions, quickly identify and troubleshoot issues, thereby ensuring high availability of the entire cluster. |
| Log management | Supports viewing container instance logs, application logs, and cluster logs, and supports centralized log management, improving the efficiency of troubleshooting and performance monitoring. |
| Log center | Provides Ingress dashboard and log center dashboard, displaying Nginx Ingress logs through dashboards to help you intuitively understand and analyze cluster log data. |
| Monitoring capabilities | Integrates Alibaba Cloud Prometheus service capabilities, supports arms-Prometheus monitoring, and implements comprehensive monitoring at the cluster, node, application, and container instance levels, helping you monitor system status in real time. |

## 6 Scenarios

**DevOps continuous delivery**

**Optimized continuous delivery pipeline**

Container Service works with Jenkins to automate the DevOps pipeline, from code submission to application deployments. The service ensures that code is only submitted for deployment after passing automated testing, and provides a better alternative to traditional delivery models that involve complex deployments and slow iterations. DevOps pipeline automation Automates the DevOps pipeline, from code updates to code builds, image builds, and application deployments. Consistent environment Allows you to deliver code and runtime environments based on the same architecture. Continuous feedback Provides immediate feedback on each integration or delivery.

**Related products and services**

ECS + Container Service

**Machine learning based on cloud-native technology**

**Enables rapid application developments with a focus on machine learning**

Container Service allows data engineers to easily develop and deploy machine learning applications in heterogeneous computing clusters. Integrated with multiple distributed storage systems, the service supports faster read and write speeds to facilitate the testing, training, and release of data models. You can focus on your core business operations instead of worrying about the deployment and maintenance process. Ecosystem support Supports mainstream deep learning frameworks, such as TensorFlow, Caffe, MXNet, and Pytorch, and offers optimized features of these frameworks. Quick start and elastic scaling Provides machine learning services for development, training, and inference. Supports the startup of training and inference tasks within seconds, and elastic scaling of GPU resources. Easy to use Allows you to easily create and manage large-scale GPU clusters and monitor core metrics, such as GPU utilization. Deep integration Seamless integration with Apsara Stack storage, logging and monitoring, and security infrastructure capabilities.

**Related products and services**

ECS/EGS/HPC + Container Service + OSS/NAS/CPFS

**Microservices architecture**

**Agile development and deployment to speed up the evolution of business models**

In the production environment, you can split your system into microservices and use Apsara Stack image repositories to store these microservice applications. Apsara Stack can schedule, orchestrate, deploy, and implement phased releases of microservice applications while you focus on feature updates. Load balancing and service discovery Forwards layer 4 and layer 7 requests and binds the requests to backend containers. Multiple scheduling and disaster recovery policies Supports different levels of affinity scheduling policies, and cross-zone high availability and disaster recovery. Microservices monitoring and auto scaling Supports microservice and container monitoring, and microservice auto scaling.

**Related products and services**

ECS + ApsaraDB RDS + OSS + Container Service

**Hybrid cloud architecture**

**Unified O&M of cloud resources**

You can centrally manage cloud and on-premises resources in the Container Service console. Containers hide the differences between infrastructures. This enables you to use the same images and orchestration templates to deploy applications in the cloud and on premises. Application scaling in the cloud During peak hours, Container Service can scale up applications in the cloud and forward traffic to the scaled-up resources. Disaster recovery in the cloud Business systems can be deployed on premises for service provisioning and in the cloud for disaster recovery. On-premises development and testing Applications that are developed and tested on premises can be seamlessly released to the cloud.

**Related products and services**

ECS + VPC + Express Connect

**Automatic scaling architecture**

**Traffic-based scalability**

Container Service enables businesses to auto-scale their resources based on traffic. This prevents traffic spikes from bringing down your system and eliminates idle resources during off-peak hours. Quick response Container scale-out can be triggered within seconds when traffic reaches the scale-out threshold. Auto scaling The scaling process is fully automated without human interference. Low cost Containers are automatically scaled in when traffic decreases to avoid resource waste.

**Related products and services**

ECS + CloudMonitor

## 7 Limits

| Limit | Description |
|---|---|
| Cluster | By default, you can create a maximum of 50 clusters across all regions. Each cluster can contain a maximum of 100 nodes. To increase these quotas, submit a ticket. After you create a cluster, you cannot perform the following actions: You cannot change a cluster's VPC. You cannot change the container network plugin. The storage plug-in cannot be changed. You cannot migrate applications between different namespaces. Ensure that you have purchased enough ACK licenses. If you have an insufficient number of licenses, cluster creation fails. |
| ECS instance | Cluster creation, scale-out, and auto-scaling operations are subject to the quota and inventory of underlying products, such as Elastic Compute Service (ECS). If the quota or inventory is insufficient, some nodes may fail to be created. When you create a cluster, the ECS instances must have at least 2 vCPUs and 4 GiB of memory. |

## 8 Terms

**Terms**

**Cluster**

A group of cloud resources required to run containers. A cluster connects several cloud resources, such as server nodes, Server Load Balancer instances, and virtual private clouds.

**Node**

A server, which can be a virtual machine or a physical server, that has Docker Engine installed. It is used to deploy and manage containers. The ACK agent is installed on the node and registered with a cluster. The number of nodes in a cluster can be scaled.

**Node pool**

A node pool is a logical group of nodes that share the same properties. This lets you manage and maintain the nodes in a unified way, such as performing node upgrades and using Auto Scaling. You can also use the automated O&M features of node pools to automatically fix OS CVE vulnerabilities, recover failed nodes, and upgrade kubelet and containerd versions. This helps reduce O&M costs. For more information, see **User Guide**
**> Node Pools** in Container Service for Kubernetes.

**Virtual private cloud (VPC)**

A virtual private cloud (VPC) is a private network that you create in the cloud. You have full control over your VPC, including specifying IP address ranges and configuring route tables and gateways. You can use Alibaba Cloud resources, such as Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances, in your VPC.

**Security group**

A security group is a virtual firewall that provides stateful inspection and packet filtering to create security domains in the cloud. It is a logical group that consists of instances in the same region that have the same security requirements and trust each other.

**App Catalog**

The App Catalog feature integrates Helm and provides related features and extensions, such as a graphical user interface (GUI).

**Orchestration template**

An orchestration template is used to save orchestration files in Kubernetes YAML format.

**Knative**

Knative is a serverless framework based on Kubernetes. Its goal is to establish a cloudnative, cross-platform standard for serverless orchestration.

**Kubernetes**

Kubernetes is an open source platform that is portable and extensible. It is used to manage containerized workloads and services, and it simplifies declarative configuration and automation.

**Container**

A technology for packaging an application and its runtime dependencies. Multiple containers can run on a single node.

**Image**

A container image is the standard format for packaging a containerized application. It encapsulates the application and all its software dependencies. When you deploy a containerized application, you can specify an image. The image can be from Docker Hub, Alibaba Cloud Container Registry, or your private image repository.

**Image repository**

An image repository stores container images for use in Kubernetes and container-based application development.

**Control plane node**

A control plane node manages a Kubernetes cluster. It runs services such as kubeapiserver, kube-scheduler, kube-controller-manager, and etcd, and components for container networking.

**Worker node**

A worker node is a node in a Kubernetes cluster that runs workloads. It can be a virtual machine or a physical machine. A worker node is responsible for running pods and communicating with control plane nodes. Services on a worker node include the Docker runtime environment, kubelet, Kube-Proxy, and other optional components.

**Namespace**

A namespace provides virtual isolation for resources within a Kubernetes cluster.

**Pod**

A pod is the smallest and most basic unit that can be deployed in Kubernetes to run an application or a service. A pod encapsulates one or more application containers, storage resources, a unique network IP address, and policy options that control how the containers run.

**ReplicationController (RC)**

RC ensures that a specified number of Pod replicas are running in the Kubernetes cluster at any time. You can monitor running pods to ensure that a specified number of Pod replicas are running in the cluster. The specified number can be multiple or one. If the specified number is less than the specified number, RC starts running a new Pod replica. If the number is more than the specified number, RC terminates the redundant Pod replicas.

**ReplicaSet (RS)**

A ReplicaSet (RS) is an upgraded version of a ReplicationController (RC). The main difference is its support for more expressive selectors. ReplicaSets are not typically used directly but are used by Deployments to manage pod replicas.

**Workload**

A workload is an application running on Kubernetes.

**Label**

Labels are key-value pairs that are attached to resource objects. They are used to specify object attributes that are meaningful to users but have no direct meaning to the core system. Labels can be attached to an object at creation time and can be added or modified at any time. Each object can have multiple labels, but each key must be unique for that object.

**Service**

A Service is a basic operational unit in Kubernetes that acts as an abstraction for an application service. Each Service is backed by a set of pods and uses a selector to determine how to route requests to them. The Service provides a single, stable access interface.

**Ingress**

An Ingress is a set of rules that allow inbound connections to reach cluster services. An Ingress controller is responsible for fulfilling the Ingress, usually with a load balancer. It can also configure edge routers and other frontends to help handle traffic in a highly available manner.

**ConfigMap**

A ConfigMap stores configuration data as key-value pairs. This data can be fine-grained, such as individual properties, or coarse-grained, such as entire configuration files or JSON objects. You can use ConfigMaps to save configuration information and files that do not require encryption.

**Secret**

A Secret is used to store sensitive configuration information in a Kubernetes cluster, such as passwords and certificates.

**Volume**

A Kubernetes volume is similar to a Docker volume. However, a Docker volume is scoped to a single container, whereas a Kubernetes volume shares the same lifecycle as its pod. All containers in a pod share the volumes declared in that pod.

**Persistent volume (PV)**

A persistent volume (PV) is a storage resource in the cluster, just as a node is a cluster resource. A PV's lifecycle is independent of any individual pod that uses the PV. You can create different types of PVs based on different StorageClass types.

**Persistent volume claim (PVC)**

A persistent volume claim (PVC) is a request for storage resources. Similar to how a pod consumes node resources, a PVC consumes PV resources.

**StorageClass**

A StorageClass enables dynamic volume provisioning, which allows storage volumes to be created on demand.

**Auto Scaling**

Auto Scaling is a service that automatically adjusts computing resources as needed and policies. Typical use cases include applications with variable traffic, large-scale computing tasks, and deep learning training and inference that use GPUs or shared GPUs.

**Observability**

Kubernetes observability encompasses monitoring and logging. Monitoring helps developers view the operational status of the system, while logging is used for troubleshooting and diagnostics.

**Helm**

Helm is a package manager for Kubernetes. Helm uses packages called charts to organize the resources related to an application and manage them.
