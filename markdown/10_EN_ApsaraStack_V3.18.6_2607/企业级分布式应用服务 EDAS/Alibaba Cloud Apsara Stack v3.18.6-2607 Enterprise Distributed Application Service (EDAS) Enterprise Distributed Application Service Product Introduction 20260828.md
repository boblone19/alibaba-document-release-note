---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise Distributed Application Service Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 16
source_pdf: "ec4038f81da270a0_Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%20EDAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Enterprise%20Distributed%20Application%20Service%20%28EDAS%29%20Enterprise%20Distributed%20Application%20Service%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise Distributed Application Service Product Introduction 20260828

## Table of Contents

- 1 Enterprise distributed application service (EDAS)
- 2 Product details
- 3 Product value
- 4 Features
- 5 Scenarios
- 6 Limits
- 7 Key concepts

rprise distributed application serv ice (EDAS)

## 1 Enterprise distributed application service (EDAS)

**application service (EDAS)**

Enterprise Distributed Application Service (EDAS) is a cloud-native Platform as a Service (PaaS) offering for application hosting and microservice management. It provides full-stack solutions for application development, deployment, monitoring, and operations and maintenance (O&M). EDAS also supports microservice runtime environments, such as Spring Cloud and Apache Dubbo (Dubbo), to help you easily migrate your applications to the cloud. uct details

## 2 Product details

Enterprise Distributed Application Service (EDAS) is a core product in Alibaba's distributed service architecture. It provides a wide range of features, such as application hosting, full application lifecycle management, and operations and maintenance (O&M) control.

**Application hosting**

Application hosting allows developers to host applications with a service provider (SP) instead of on their own servers. After you develop an application, you can host it on EDAS.

| Feature | Description |
|---|---|
| Multiple underlying server options | EDAS supports ECS instances, Container Service for Kubernetes, and self- managed Kubernetes clusters. |
| Multiple deployment methods | EDAS supports deployments using the console, API, command-line interface (CLI), and SDKs. It also supports automated application deployment using the Cloud Toolkit plugin. |
| Multiple deployment formats | Supports deployment using WAR packages, JAR packages, and images. |
| Elastic scaling | Elastic scaling handles traffic bursts by automatically scaling out applications to a suitable level. After the traffic surge, it scales the applications back in to save resource costs. |

**Application lifecycle management**

EDAS provides full lifecycle management for applications. This includes deployment, start, stop, scale-out, scale-in, rollback, and deletion. You can easily manage thousands of application instances.

**Application development**

EDAS supports hosting applications developed using native Spring Cloud, native Dubbo, or HSF. You can host applications developed using the Spring Cloud framework on EDAS by adding dependencies and making minor configuration changes. This eliminates the need to set up Eureka or Consul, which saves on deployment and O&M costs. You also gain access to enterprise-grade EDAS capabilities, such as application hosting, service administration, monitoring and alerts, and application diagnostics. You can host applications developed using the Dubbo framework on EDAS by adding dependencies and making minor configuration changes. This eliminates the need to set up ZooKeeper or Redis, which saves on deployment and O&M costs. You also gain access to enterprise-grade EDAS capabilities, such as application hosting, service administration, monitoring and alerts, and application diagnostics. uct details High-Speed Service Framework (HSF) is a distributed Remote Procedure Call (RPC) service framework widely used within Alibaba. It connects different business systems and decouples the implementation dependencies between them. HSF also standardizes how services are published and invoked in distributed applications. This helps you develop distributed applications quickly and easily. HSF provides common functional modules and hides the complex technical details of the distributed domain.

**Microservice administration**

EDAS provides complete microservice administration capabilities for microservice applications built using various frameworks. These capabilities include service search, trace query, outlier ejection, and service authentication. Service search: View the Dubbo, Spring Cloud, and HSF services of an application within a specific region and namespace. Trace query: Set query conditions to accurately identify services with poor or abnormal performance. Outlier ejection: In a microservices model, if an application instance of an SP becomes abnormal, the consumer may be unaware. This can affect normal service invocation, which impacts the consumer's service performance or even its availability. The outlier ejection feature detects the availability of application instances and makes dynamic adjustments to ensure successful service invocations. This improves business stability and service quality. Service authentication: If a microservice application has security requirements and should not be invoked by all other applications, you can authenticate the applications that invoke it. Only applications that match the authentication rules are allowed to invoke the service. Elastic scaling: This feature detects the status of each instance within an application and then dynamically scales the application out or in based on that status. This improves application availability while ensuring service quality. Throttling and degradation: Throttling and degradation are used to prevent slow system responses or crashes caused by excessive pressure on core backend services. This is typically used in high-traffic scenarios, such as flash sales, panic buying, sales promotions, and anti-brushing. Health check: Health checks periodically inspect containers and applications and report the results to the console. This helps you understand the overall running status of your applications in a cluster environment and assists with troubleshooting and problem-solving. Full-link traffic shaping: This feature enables a smooth transition between old and new versions of an application.

**Configuration management**

EDAS is integrated with Application Configuration Management (ACM). In EDAS, you can use ACM to centrally manage and push application configurations. You can also use namespaces to isolate and synchronize configurations between different environments. Configuration management features include creating and managing configurations, viewing historical versions, and querying listeners.

**Application monitoring**

After an application is hosted on EDAS, you can monitor its performance and status. Monitoring features include an overview, details, API call monitoring, logs, and alert notifications. Application monitoring: Monitor the health of an application's IaaS layer resources and services in real time. This helps you quickly discover and locate problems. You can also enable advanced monitoring with Application Real-Time Monitoring Service (ARMS). uct details Logs: You can view the runtime logs of applications deployed on an instance without logging on to the instance. When an application behaves abnormally, you can check the logs to troubleshoot the problem. Real-time logs (for applications deployed in Kubernetes clusters): When an application behaves abnormally, you can view real-time logs to troubleshoot pod-related issues. Notifications and alerts: When certain resources are overused, notifications are sent by text message or email to the designated contacts. This allows them to handle production issues promptly.

**System administration**

EDAS provides system administration features to manage and control permissions for accounts and roles. Root user and RAM user system: The root user and RAM user system lets you establish relationships between these user types on the EDAS platform. These relationships can be based on your company's organizational structure, such as departments, teams, and projects. ECS resources can also be divided based on these relationships, which makes resource allocation easier. Roles and access control: Application lifecycle management involves different roles, such as developers and O&M personnel, who perform different operations. EDAS provides a role and access control mechanism that lets you define roles for different accounts and assign the corresponding permissions. Service authentication: To ensure the stability and security of distributed services, strict authentication is performed for every service invocation. This authentication occurs at every step of the process, including service registration, service subscription, and service invocation. uct value

## 3 Product value

EDAS supports over 99% of the large-scale applications within Alibaba Group. These applications include core online services such as membership, transactions, products, stores, logistics, and reviews. EDAS offers unique advantages in stability and reliability.

**Greater reliability**

Built on core technologies developed and refined within Alibaba for nearly a decade. Supports the stable operation of core applications within Alibaba Group. Proven by multiple Double 11 Shopping Festivals. A comprehensive authentication system ensures that every service invocation is secure and reliable.

**Comprehensive features**

A complete Platform as a Service (PaaS) solution for application lifecycle management. A complete service administration solution for managing distributed services. A comprehensive application diagnostics system to easily locate the root cause of failures. Online stress testing to obtain machine performance metrics and real-time operational data. Automatic elastic scaling to handle sudden traffic peaks with ease.

**In-depth insights**

Access to in-depth business metrics and comprehensive report generation. Comprehensive, multi-dimensional monitoring for thorough troubleshooting. Link tracing for insights into every distributed call. Dependency analysis to identify every system bottleneck.

**More open**

Built on multiple open source Internet middleware products. Contributions to top-level Apache projects that have earned an excellent industry reputation. No vendor lock-in. You can easily replace components with open source software.

## 4 Features

Enterprise Distributed Application Service (EDAS) is a core product of Alibaba's distributed service architecture. It provides a wide range of features, such as application management, microservice governance, and operations and maintenance (O&M).

**Account and permission management**

| Feature | Description |
|---|---|
| User logon and authorization | Supports user logon with an account and password. Provides a guided flow for service activation and role authorization. Prompts users to renew or purchase services after logon, based on the account's renewal status. |
| Role Management | Create: Create custom enterprise roles. View: View a list of enterprise roles and their associated permission details, which are displayed as a permission tree. Edit: Edit permission assignments for existing roles. Delete: Delete enterprise roles that are no longer needed. |
| Sub-account management | View: View a list of sub-accounts in your enterprise. Manage: Manually sync RAM sub-accounts, attach users to sub- accounts, and grant RAM policies. |
| Access policy management | View and manage: Use the permission assistant to view and manage permission settings for Enterprise Distributed Application Service. |

**Application management**

| Feature | Description |
|---|---|
| Application lifecycle | Create: Create applications using a wizard. You can create applications from scratch, from a template, or from a Helm Chart. View: View a centralized list of applications. Filter and view applications by region, resource group, namespace, and other dimensions. Edit: Edit basic application information, such as the name, description, and owner. Configure: Configure detailed application settings, such as JVM parameters, Tomcat configurations, environment variables, and mounted volumes. Delete: Delete a single application or an entire application group. |

| Application deployment and release | Deploy: Deploy applications from an image, a WAR/JAR package, or by building from source code. Configure release policy: Configure release policies during deployment, such as phased release and canary release. You can also configure health checks and resource quotas. Version management: Upgrade and roll back versions of application instances. View release orders: View a list and details of release orders. Check the release history, status, logs, and pipeline view. Operate on release orders: Manually confirm or abort a phased release process. |
|---|---|
| Phased release | Create and manage: Create, view, and delete end-to-end canary release environments. Configure canary rules: Manage application groups in the canary release environment. Configure canary rules and traffic splitting policies. |
| Application details and instances | View instances: View a list of all instances (pods or ECS instances) for an application and their running status. Manage instances: Scale application instances out or in (elastic scaling). Attach SLB: Attach, detach, and modify Server Load Balancer (SLB) configurations for an application. |

**Microservice governance**

| Feature | Description |
|---|---|
| Namespace | Create/View/Delete: Perform full lifecycle management for microservice namespaces, including creating, viewing, editing, and deleting them. |
| Service registration and discovery | View services: Query and browse registered services and their details by namespace and protocol type, such as Dubbo, Spring Cloud, and Service Mesh. |
| Traffic governance | Configure routing rules: Configure tag-based service routing rules for fine-grained traffic shaping. Configure load balancing: Configure load balancing policies for microservices. Configure service timeout: Configure a unified timeout policy for microservices. Configure service retry: Configure a retry policy for microservices to increase the success rate of service invocations. |

| Resilience and fault tolerance | Configure service degradation: Configure service degradation rules (Mock) to ensure core services remain available when dependent services are abnormal. Configure fault injection: Inject faults in test environments to verify the system's fault tolerance. Configure outlier ejection: Configure automatic outlier ejection policies to improve overall service stability. |
|---|---|
| Service authentication | Configure service authentication: Configure authentication and authorization rules for microservices to secure service-to-service invocations. |
| Service Mesh (Istio) | Manage service mesh: Manage the service mesh through a visual interface. View the service topology, gateways, and more. |

**Resource management**

| Feature | Description |
|---|---|
| Cluster management | Create/Import: Create EDAS clusters or import clusters from existing cloud resources, such as ACK. View: View a list and details of different cluster types, such as ECS, Kubernetes, and self-managed Kubernetes clusters. Edit/Upgrade: Edit cluster information and upgrade Kubernetes cluster versions. Delete: Delete clusters. Migrate: Migrate host instances between different clusters. |
| ECS instance management | View: View a list of ECS instances and their details by namespace. Import/Migrate: Use a wizard to import or migrate existing ECS instances into EDAS-managed clusters. |
| Resource group management | Create/Edit/Delete: Create, edit, and delete resource groups. Attach resources: Attach or detach cloud resources, such as ECS instances, SLB instances, and clusters, to or from resource groups. |
| VPC/Network management | View and sync: View and manually sync the Virtual Private Cloud (VPC) resource list. |

**Monitoring and O&M**

| Feature | Description |
|---|---|

| Application monitoring (APM) | View call chains: View call chains with end-to-end distributed tracing. Visualize service invocation relationships and time consumption. View application overview: View an application overview with advanced application performance management (APM) features, such as application topology, interface monitoring, and exception analysis. Configure alerts: Configure alert rules, manage alert contacts, and view alert history. Integrate Prometheus: Embed the Prometheus monitoring interface for custom metric monitoring. |
|---|---|
| Log Management | View real-time logs: View real-time standard output logs and file logs from application instances. Search historical logs: Search and analyze archived application logs. Configure log collection: Configure collection rules to gather application logs into Simple Log Service. |
| Configuration management | Manage configurations: Centrally manage distributed configuration items for applications. Create, publish, roll back, and view historical versions. |
| Auto Scaling | Configure scaling rules: Configure scaling rules based on metrics such as CPU, memory, and load to automatically scale application instances. |
| Batch operations | Execute batch tasks: Execute O&M commands or scripts in batches on multiple machines. View task records: View the execution history, status, and results of batch tasks. |
| Security Center | Manage security policies: Use the application Security Center to configure and manage access control and security policies. |

**CI/CD and task scheduling**

| Feature | Description |
|---|---|
| CI/CD | Manage pipelines: Manage pipelines for continuous integration/continuous deployment (CI/CD). |
| Distributed task scheduling | Manage scheduled tasks: Create, view, and manage distributed scheduled tasks (Jobs) and workflows. |

narios

## 5 Scenarios

EDAS is an application hosting platform that is ideal for distributed architectures and for migrating digital businesses to the cloud. It is used in a wide range of scenarios.

**Microservice solutions**

EDAS supports three major microservice frameworks: Apache Dubbo, Spring Cloud, and HSF. The built-in HSF framework is a high-performance microservice framework that has been proven during Alibaba's Double 11 Global Shopping Festival. It is developed based on best practices from various Alibaba business scenarios. You can also migrate Apache Dubbo and Spring Cloud applications to the cloud without code modifications. This migration effectively reduces O&M costs and supports advanced features, such as phased releases and traffic shaping. This lets you easily build microservice applications on the cloud.
**Quickly build applications on a mature microservice framework** : You can build
microservice applications on the cloud using HSF, Alibaba's proven microservice framework.
**Migrate Apache Dubbo and Spring Cloud to the cloud** : You can eliminate the need to
build self-managed services that microservices depend on, such as ZooKeeper, Eureka, and Consul. This greatly reduces O&M costs.
**Meet the requirements for enterprise-grade advanced features** : You can use built-
in, enterprise-grade advanced features, such as phased releases, traffic shaping, and environment isolation.

**Application hosting solutions**

EDAS eliminates the complex task of logging on to and deploying servers one by one and removes the need for cluster maintenance. You can log on to the EDAS console to quickly deploy applications using WAR packages, JAR packages, or images. EDAS provides full application lifecycle management on ECS, including releases, rollbacks, application group management, and the coexistence of multiple versions. It also integrates monitoring and logging to greatly improve the efficiency of ECS cluster management.
**Significantly reduce O&M costs**: You can eliminate O&M for Infrastructure as a Service
(IaaS) and cluster maintenance to effectively reduce labor costs.
**Full application lifecycle management**: You can visually manage the application
lifecycle and easily view the running status of your applications.

**Container hosting solutions**

EDAS supports hosting applications in containers. It seamlessly integrates with Alibaba Cloud Container Service for Kubernetes. You do not need to understand the underlying details of the container service. You can use the EDAS console to manage the full lifecycle of applications in containers, including services such as monitoring and diagnostics. This provides a low barrier to entry for adopting new container technologies and helps you maximize resource utilization.
**Seamless support for Kubernetes**: You can host Kubernetes clusters on EDAS and focus
only on application lifecycle management.
**Perfect combination of containers and microservices** : You can quickly build a
microservices model on containers based on Kubernetes.
**No need to build images**: You can directly deploy WAR and JAR packages. EDAS builds
the images and deploys them to your Kubernetes cluster. This simplifies the process and lowers the barrier to entry. ts

## 6 Limits

This topic describes the limitations of EDAS. Review them carefully before you use the service.

| Limit | Description |
|---|---|
| Application development language | EDAS currently supports only applications developed in Java. |
| Application development framework | EDAS supports runtime environments for microservices frameworks such as Spring Cloud, Apache Dubbo, and HSF. It also supports the service mesh architecture. |
| Application package size | EDAS currently supports only application packages and container images up to 500 MB. |
| Cluster environment | EDAS currently supports application deployment only in a Kubernetes cluster. In a K8s cluster, do not modify the Deployment of an application deployed by EDAS, as this can cause application instability. |
| Service registry | If you use Nacos as a service registry, ensure that the Nacos client version is 1.4.2 or later. |
| Microservice namespace | A K8s cluster can be bound to only one EDAS microservice namespace. An EDAS microservice namespace can be bound to multiple K8s clusters. |

concepts

## 7 Key concepts

This topic summarizes the core concepts of Enterprise Distributed Application Service (EDAS) to help you quickly understand them.

**Ali-Tomcat**

Ali-Tomcat is a container required for the EDAS service runtime. It integrates core features such as service publishing, subscription, and distributed tracing. You must deploy applications to this container in both development and runtime environments.

**Dubbo**

Dubbo is a distributed service framework that provides high-performance and transparent remote procedure call (RPC) solutions. As the core framework of Alibaba's service-oriented architecture (SOA) governance solution, it supports over 2,000 services with more than 3 billion calls per day and is widely used on Alibaba Group's websites.

**Cluster**

A collection of cloud resources required to run an application. An ECS instance must be added to a cluster. If you do not specify a cluster, the system adds the ECS instance to the default cluster.

**Namespace**

An isolated resource environment within a region that contains one or more clusters. Namespaces are logically isolated. A cluster must be created within a namespace. If you do not specify a namespace, the system creates the cluster in the default namespace.

**EDAS Agent**

The EDAS Agent is a daemon that runs on your ECS instances and acts as a communication bridge between the EDAS service cluster and the applications running on those instances. It handles core functions such as application management, status reporting, and information collection. It also serves as the primary communication channel between the EDAS console and your applications.

**RPC service**

The EDAS RPC service supports the Dubbo framework. A Dubbo application deployed as a WAR package can be seamlessly published and managed on the EDAS platform. This allows the application to use all the service governance and data-driven operational features that EDAS provides.

**Application Lifecycle**

An application is the basic unit of management in EDAS and typically runs on multiple machines. EDAS manages the entire application lifecycle. This includes operations such as creating, deploying, starting, rolling back, scaling in and out, stopping, and deleting an application.

**Application instance quota**

This is the maximum number of instances that a main account and its sub-accounts can deploy across all their applications.
