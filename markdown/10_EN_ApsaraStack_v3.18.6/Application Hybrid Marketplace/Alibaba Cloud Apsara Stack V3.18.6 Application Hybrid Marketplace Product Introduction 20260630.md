---
title: "Application Hybrid Marketplace Product Introduction 20260630"
product_version: "V3.18.6"
pdf_pages: 8
source_pdf: "fe484276466e009c_Alibaba Cloud Apsara Stack V3.18.6 Application Hybrid Marketplace Product Introduction 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%B7%B7%E5%90%88%E4%BA%91%E5%BA%94%E7%94%A8%E4%B8%AD%E5%BF%83AHM/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Application%20Hybrid%20Marketplace%20Product%20Introduction%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Application Hybrid Marketplace Product Introduction 20260630

## Table of Contents

- 1 Hybrid cloud application center
  - 1.1 Product details
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Functions and features

## 1 Hybrid cloud application center

**center**

The Hybrid Cloud Application Center (Application Hybrid Marketplace, AHM) is the third product development and delivery pipeline alongside the Apsara Stack infrastructure Tianji and PaaS platform. It primarily supports the deployment of third-party ISV or Alibaba Cloud internal SaaS applications in Apsara Stack scenarios. AHM uses cloud platform tenant-side resources for application delivery, with the goal of expanding the Apsara Stack product ecosystem.

### 1.1 Product details

Application Center provides customers with convenient and fast application delivery and deployment methods.

**Application management**

Application Center supports adding and updating cloud product applications in the application marketplace by importing cloud product packages in standard formats. Applications in the application marketplace support multiple version selections, allowing users to choose specific versions to build application deployment environments. Trial experiences support environment delivery with minimized resource requirements to meet user trial needs. Additionally, you can add and update applications through OpenAPI operations.

**Environment management**

Deployment activation: Supports completing resource configuration requirements and environment deployment for various application components with standard environment requirements and standard resources. Variable management: Supports defining global variables that take effect across the environment and cluster variables that take effect for specific clusters. Supports generating keys for internal database calls in the deployment environment. Container resource monitoring: Supports monitoring resource data changes based on Application Operations and Management Platform (AOP) and Prometheus, displaying container resource usage. Deployment offline: Supports taking deployed application instances offline to release resources.

**Task management**

Supports viewing application deployment task status and execution progress. When execution failures occur during task execution, you can manually retry or skip related steps.

**Image repository management**

Supports creating Docker image repositories for clusters, providing different image services for different clusters. When deploying applications, the system reads the image repository configuration to obtain the image source.

### 1.2 Benefits

Application Center integrates various services and resources into a complete solution through standard protocols and Infrastructure as Code (IaC) orchestration engines, enabling one-click deployment of this complete solution to customer Apsara Stack environments.

**Access standards**

The universal application package format, simple and unified access standards, and whitescreen baseline orchestration interface enable partners to quickly become familiar with and use the system. The system provides a protocol format that combines multiple services and resource definitions into a cohesive whole. It also offers open extension capabilities that can incorporate Apsara Stack resource capabilities into its format descriptions, supplemented by corresponding implementations, to complete the delivery of the entire environment.

**Third-party ecosystem**

A complete third-party ecosystem allows ISV service providers to build application versions through the delivery console. After testing acceptance and complete delivery verification, relevant sales mechanisms are established to achieve lifecycle management of product applications. We strive to create a simplified operations management system that enables customers and suppliers to complete basic O&M management on the Application Center platform.

**One-click delivery**

With the one-click product deployment mechanism, users can complete the delivery of the product environment with just one button when they need to try or formally purchase applications.

**Simplified O&M**

Application Center integrates infrastructure monitoring capabilities and supports automated O&M through custom policies. We are committed to creating a simplified operations management system that enables customers and service providers to quickly complete basic O&M actions on the Application Center platform.

### 1.3 Scenarios

Apsara Stack has been deployed in numerous enterprises. Enterprise customers increasingly want to make better use of this cloud platform and hope to introduce more high-quality cloud products (such as Alibaba Cloud and third-party ISV SaaS products) to meet more of their business requirements. Application Center supports the sales and deployment of Alibaba Cloud or third-party ISV applications in Apsara Stack scenarios, meeting customers' diverse product application needs in the Apsara Stack environment. Application Center is mainly used in the following scenarios: Third-party ISV suppliers join the Apsara Stack platform to publish various cloud products and applications Decoupling of base version dependencies, enabling rapid deployment of iterative Alibaba Cloud internal products and applications Cloud products and applications that need to be deployed on the tenant side to utilize comprehensive Apsara Stack product capabilities

### 1.4 Functions and features

This topic describes the features of Hybrid Cloud Application Center.

**Application management**

| Feature | Description |
|---|---|

| Application overview | You can view the status of applications, the statistics of resources used for application deployment (by CPU, memory, and disk), the distribution of resources for application deployment, and the alert status of resources (including critical, important, and medium) in real time. This allows you to quickly locate issues and optimize application resource management. |
|---|---|
| Application integration | Hybrid Cloud Application Center adopts the Open Application Model (OAM) standard specification to integrate and package various services and resources into a complete solution. You can deploy this complete solution in your Apsara Stack environment with a few clicks. |
| Application store | The application store displays the information of all published applications by application category, including the service provider information, overall description, core highlights, feature introduction, product qualification, specifications, price, contact information, and delivery and after-sales support. |
| Application import | You can add or update cloud service applications in the application store by importing cloud service packages in a standard format. |
| Application deployment | The applications in the application store support multiple versions. You can select a specific version to deploy. You can use the trial feature to test application deployment with the minimal resources required by an application. The resource configuration and environment deployment for each application component can be completed using standard resources based on the standard environment requirements. |
| Openness | You can create and update applications by calling API operations. |

**My applications**

| Feature | Description |
|---|---|
| Application instance deployment | After an application is deployed, you can view all the instances that have been purchased and instances that are in trial use. The instance information includes the list of cloud service instances on which the instance depends and detailed deployment logs. You can also view and delete the official application instances that have been deployed. |
| Application configuration | You can modify the parameters of a deployed application in the console. |
| Application instance deletion | You can delete an application instance that is no longer in use. After you delete an instance, all resources used by the instance are released and the application data is automatically deleted. |
| Container resource monitoring | You can monitor resource changes and container resource usage by using Sunfire and Prometheus for applications deployed based on containers. |

| Application deployment task management | You can view the status and execution progress of an application deployment task. If a task fails during execution, you can manually retry or skip the related steps. |
|---|---|

**Plug-in center**

| Feature | Description |
|---|---|
| Plug-in store | You can import independent Service Provider Interfaces (SPIs) abstracted from external system features as plug-ins. This way, applications can call external capabilities by using the SPIs. This implements external capability pluggability. You can import ZIP packages of OAM applications and JAR packages of remote applications as plug-ins. |
| My plug-ins | The system displays the basic information, plug-in information, and endpoints of deployed plug-ins. You can update, uninstall, disable, enable, and restart plug-ins. |
| Shortcuts | You can use shortcuts for deployed plug-ins to quickly go to the plug-in management platform. |

**System management**

| Feature | Description |
|---|---|
| Image repository management | You can create Docker image repositories for clusters to provide different image services for different clusters. When you deploy an application, the system reads the configurations of the image repository to obtain images. |
| Variable management | You can define global variables and cluster variables that take effect for specific clusters. You can generate keys for internal database calls in the deployment environment. |
