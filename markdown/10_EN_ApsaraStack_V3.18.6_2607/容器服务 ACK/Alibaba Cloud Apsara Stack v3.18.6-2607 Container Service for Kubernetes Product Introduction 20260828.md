---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 24
source_pdf: "8230979dea1bc058_Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Product Introduction 202608"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20ACK/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Container%20Service%20for%20Kubernetes%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Product Introduction 20260828

## Table of Contents

- 1 What is Container Service?
- 2 Features
- 3 Benefits
- 4 Architecture
- 5 Functions and features
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

nd features

## 5 Functions and features

Alibaba Cloud Container Service for Kubernetes (ACK) is a high-performance and scalable container management service. It provides robust Kubernetes cluster management capabilities and delivers a one-stop container cluster management solution that covers cluster management, O&M, high availability, and container images. The service helps you manage the entire lifecycle of Kubernetes containerized applications in the cloud quickly and efficiently. This topic describes the specific features in detail.

**Cluster management**

| Feature | Description |
|---|---|
| Master node management | The system supports high availability with three or five nodes and enables OS rotation and replacement for master nodes. It enables deletion protection for the SLB instance associated with an API Server by default and allows access to the API Server over both the public and private networks. |
| Namespace management | The system manages the lifecycle of namespaces and allows you to configure resource quotas and default resource limits. |
| Authorization management | The system supports a combination of RBAC and RAM permissions. The available permission types include administrator, O&M engineer, developer, and restricted user. You can revoke kubeconfig permissions and grant different types of permissions to RAM users based on the cluster or namespace scope. The system also supports login through ASCM STS role assumption. |
| Cluster management | For cluster creation and mixed deployment, the system supports simultaneous deployment of ECS instances with x86 and ARM architectures, use of ECS instances with the same chip instruction set within a cluster, custom service domain names, and network configuration. It also continuously releases Kubernetes versions compatible with newly released community versions.. The system supports one-click upgrades of Kubernetes versions. The system allows you to add tags to clusters. |
| License management | The system supports metering and control of licenses. |
| Registered clusters | You can create registered clusters and manage on-premises Kubernetes clusters to achieve unified management of multiple clusters and improve O&M flexibility. |

**Node pool management**

| Feature | Description |
|---|---|

nd features

| Operating system support | The system supports multiple operating systems, including Alibaba Cloud Linux 3, Anolis OS, UOS, and Kylin V10. |
|---|---|
| Node configuration | You can create GPU worker nodes and ECS bare metal instances, and deploy worker nodes across zones. You can place nodes in specific deployment sets. You can customize data, node names, and images. The system supports DDH instances. |
| Network and security | You can bind public IP addresses to worker nodes, enable deletion protection for ECS nodes, and select existing security groups. The system also provides data disk encryption to ensure security and data protection. |
| Monitoring and plug-in support | You can deploy the CloudMonitor plug-in on node pools to monitor resource usage and performance in real time. |
| Node pool lifecycle management | You can scale out existing nodes or add new nodes automatically or manually. The system supports auto scaling of nodes, node removal, node label and taint management, and node maintenance. |

**Container network**

| Feature | Description |
|---|---|
| Terway container network | The system supports Terway container network 2.0 and provides network configuration in IPVLAN and extended Berkeley Packet Filter (eBPF) mode, which enables IPv6 dual-stack capabilities and Trunking ENI features. |
| Network policy and management | You can define network policies and configure CIDR blocks for Services and Pods to achieve more flexible network management. |
| SLB and DNS support | You can enable deletion protection when you create an SLB instance. The system provides local DNS caching to improve domain name resolution efficiency. |
| Flannel mode | The system provides VPC Flannel mode to meet the requirements of various network scenarios. |

**Network management**

nd features

| Feature | Description |
|---|---|
| Service management | You can create, view, update, and delete services throughout their lifecycle. The system supports multiple access methods, including Cluster IP, Node Port, and Load Balancer. You can view and update services by using scripts and create headless Services. |
| Ingress management | You can access services by using domain names and control multi-service access based on weights. You can view and update Ingress configurations and canary release strategies of services by using scripts to meet the requirements of various release scenarios. You can create, view, update, and delete Ingresses throughout their lifecycle. |
| Configuration management | You can manage ConfigMaps and Secrets to handle configuration information and sensitive data in workloads, which improves application security and flexibility. |

**Workload management**

| Feature | Description |
|---|---|
| Container instance management | You can set a limit on the number of container instances per node. You can view events of container instances. You can access container instances through a terminal for real- time management and debugging. |
| Workload scaling | The system provides Horizontal Pod Autoscaler (HPA) policies to automatically adjust the number of container instances based on workloads, and also supports manual scaling to flexibly respond to changing resource demands. |

nd features

| Workload creation | You can create multiple types of workloads, including Jobs, DaemonSets, CronJobs, Deployments, and StatefulSets. You can create workloads from Container Registry Enterprise Edition images, templates, or images. You can configure health checks, environment variables, data disk mounting, and log collection paths to ensure workload stability and observability. |
|---|---|
| Workload lifecycle management | You can manage application events, roll back applications to previous versions, perform rolling updates, trigger redeployments, and view, update, or delete applications, which provides flexibility for O&M operations. You can view and update applications by using scripts to simplify O&M workflows. |
| Workload scheduling | The system supports node affinity, pod affinity, and pod anti-affinity scheduling policies to optimize resource allocation and improve cluster resource utilization and application efficiency. |

**Container storage**

| Feature | Description |
|---|---|
| Persistent volumes and persistent volume claims | You can create and restore snapshots for persistent volumes (PVs) and persistent volume claims (PVCs) to back up and restore data, which ensures data security and reliability. |
| Storage management | You can view and update PVs and PVCs by using scripts to automate management and improve operational efficiency. |
| Storage type support | You can create multiple types of PVs, including block storage, network attached storage (NAS), and object storage, to meet various application requirements and scenarios. |
| PVC mounting | You can create PVCs to mount PVs, which allows applications to dynamically bind storage resources on demand and improves resource utilization. |
| Storage plug-in support | The system supports the Container Storage Interface (CSI) plug-in, which allows you to integrate various storage solutions in Kubernetes environments to extend storage capabilities and improve flexibility. |

**Cloud-native AI capabilities**

| Feature | Description |
|---|---|

nd features

| AI suite | You can deploy AI suites in edge clusters to make full use of edge compute resources and improve the efficiency of big data processing and AI inference. |
|---|---|
| Hardware compatibility | The system supports high-performance GPU models such as NVIDIA A100 and V100 to meet the high compute resource requirements of AI and big data applications. |
| GPU resource sharing | The GPU share feature allows multiple applications to share GPU resources, which improves resource utilization and adapts to different workload requirements. |
| Component support | The system supports components such as Queue and Arena to provide efficient task scheduling and resource management, which improves the execution efficiency of AI tasks. |
| Operating system adaptation | AI suites support Alibaba Cloud Linux 3.2.10 and Anolis OS 8.6 ANCK to ensure consistency and compatibility across different environments. |
| Cluster scheduling strategies | A cluster scheduler supports multiple scheduling strategies, including Gang scheduling and Capacity scheduling, to optimize resource allocation and task execution sequences. |

**O&M monitoring**

| Feature | Description |
|---|---|
| Intelligent diagnostics | The system diagnoses pods in a cluster, monitors and analyzes pod status in real time, and helps O&M engineers quickly locate and resolve potential issues to improve cluster stability and reliability. |
| Node diagnostics | The system diagnoses nodes in a cluster and provides node status information to help you fully understand node health, quickly discover and troubleshoot faults, and ensure high availability of the entire cluster. |
| Log management | You can view container instance logs, application logs, and cluster logs. Centralized log management improves the efficiency of troubleshooting and performance monitoring. |
| Log center | The system provides an Ingress dashboard and a log center dashboard. The Nginx Ingress log dashboard helps you visually understand and analyze cluster log data. |

nd features

| Monitoring capabilities | The system integrates Alibaba Cloud Prometheus capabilities and supports ARMS Prometheus monitoring to provide comprehensive monitoring at the cluster, node, application, and container instance levels, which helps you monitor system status in real time. |
|---|---|

**Dual-stack network**

| Feature | Description |
|---|---|
| IPv4/IPv6 dual-stack support | ACK clusters fully support native Kubernetes IPv4/IPv6 dual-stack networking. |

## 6 Scenarios

**DevOps continuous delivery**

**Optimized continuous delivery pipeline**

Container Service for Kubernetes (ACK) works with Jenkins to automate the DevOps pipeline, from code submission to application deployments. The service ensures that code is only submitted for deployment after passing automated testing, and provides a better alternative to traditional delivery models that involve complex deployments and slow iterations. DevOps pipeline automation Automates the DevOps pipeline, from code updates to code builds, image builds, and application deployments. Consistent environment Allows you to deliver code and runtime environments based on the same architecture. Continuous feedback Provides immediate feedback on each integration or delivery.

**Related products and services**

ECS + ACK

**Machine learning based on cloud-native technology**

**Enables rapid application developments with a focus on machine learning**

ACK allows data engineers to easily develop and deploy machine learning applications in heterogeneous computing clusters. Integrated with multiple distributed storage systems, the service supports faster read and write speeds to facilitate the testing, training, and release of data models. You can focus on your core business operations instead of worrying about the deployment and maintenance process. Ecosystem support Supports mainstream deep learning frameworks, such as TensorFlow, Caffe, MXNet, and Pytorch, and offers optimized features of these frameworks. Quick start and elastic scaling Supports fast model development, training, and inference based on machine learning, and supports quick startup of training tasks within seconds and elastic scaling of GPU resources. Easy to use Allows you to easily create and manage large-scale GPU clusters and monitor core metrics, such as GPU utilization. Deep integration Seamless integration with Apsara Stack storage, logging, monitoring, and security infrastructure capabilities.

**Related products and services**

ECS/EGS/HPC + ACK + OSS/NAS/CPFS

**Microservices architecture**

**Agile development and deployment to speed up business iteration**

In the production environment, you can split your system into microservices and use Apsara Stack image repositories to store these microservices applications. Apsara Stack can schedule, orchestrate, deploy, and implement phased releases of microservices applications while you focus on feature updates. Load balancing and service discovery Forwards Layer 4 and Layer 7 requests and binds the requests to backend containers. Multiple scheduling and disaster recovery policies Supports service-level affinity scheduling policies, and cross-zone high availability and disaster recovery. Microservices monitoring and auto scaling Supports microservice and container monitoring, and auto scaling of microservices.

**Related products and services**

ECS + ApsaraDB RDS + OSS + ACK

**Hybrid cloud architecture**

**Unified O&M of cloud resources**

You can centrally manage cloud and on-premises resources in the ACK console. Containers hide the differences between infrastructures. This enables you to use the same images and orchestration templates to deploy applications in the cloud and on premises. Application scaling in the cloud During peak hours, ACK can scale up applications in the cloud and forward traffic to the scaled-up resources. Disaster recovery in the cloud Business systems can be deployed on premises for service provisioning and in the cloud for disaster recovery. On-premises development and testing Applications that are developed and tested on premises can be seamlessly released to the cloud.

**Related products and services**

ECS + VPC + Express Connect

**Automatic scaling architecture**

**Traffic-based scalability**

ACK enables businesses to auto-scale their resources based on traffic. This prevents traffic spikes from bringing down your system and eliminates idle resources during off-peak hours. Quick response Container scale-out can be triggered within seconds when traffic reaches the scale-out threshold. Auto scaling The scaling process is fully automated without manual intervention. Low cost Containers are automatically scaled in when traffic decreases to avoid resource waste.

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
