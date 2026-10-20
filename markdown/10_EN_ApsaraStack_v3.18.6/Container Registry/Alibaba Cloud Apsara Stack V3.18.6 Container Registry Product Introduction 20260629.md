---
title: "Container Registry Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "bbdf132882a1cdf5_Alibaba Cloud Apsara Stack V3.18.6 Container Registry Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Registry%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Container Registry Product Introduction 20260629

## Table of Contents

- 1 Container Registry
  - 1.1 Product details
  - 1.2 Benefits
  - 1.3 Features
  - 1.4 Scenarios
  - 1.5 Key concepts
  - 1.6 Limitations

## 1 Container Registry

Container Registry is a platform that allows you to manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: image permission management, synchronous image distribution, and content signing. The features allow you to manage the entire lifecycle of container images. Container Registry simplifies the setup and O&M of container registry. Container Registry is integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to easily create and deliver a one-stop solution for cloud-native applications.

### 1.1 Product details

Container Registry is a platform that lets you manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: artifact management, image replication, artifact security, and deployment integration.

**Artifact management**

Secure hosting: Host container images securely within namespaces. Lifecycle management: Query artifacts and image versions, and delete artifacts and image repositories. Fine-grained permission management: Manage permissions for users, Apsara Stack Cloud Management (ASCM) departments, and resource sets. Version immutability: Configure version immutability for images and OCI artifacts.

**Image replication**

Triggers: Configure triggers to automatically initiate events when a container image is updated. Image synchronization: Manually synchronize specific image versions for disaster recovery and backup across multiple regions. The service also supports automatic synchronization after an image is pushed .

**Artifact security**

Encrypted image distribution: Distribute container images securely using the HTTPS protocol. Container image signing: Sign container images to ensure end-to-end consistency from distribution to deployment. This prevents man-in-the-middle (MITM) attacks and stops unauthorized images from being updated or run. Image security scanning: Scan container images to detect vulnerabilities.

**Deployment integration**

Secret-free pulls: When deploying on a container service platform, you can configure secret-free pulls to avoid the need to set a Secret for each pull operation. Deployment selection: When deploying on a container service platform, you can visually select image repositories and versions from ACR.

### 1.2 Benefits

Container Registry provides you with the following benefits: ease of use, security, and integrability.

**Ease of use**

Allows you to create an image repository without the need to manually build and maintain the images. Allows you to pull and push images across multiple regions in a fast and stable manner.

**Security and controllability**

Provides an all-in-one management system for image permissions. This ensures secure and convenient image sharing. Provides the image scanning feature to identify vulnerabilities in images and prompt vulnerability levels.

**Efficient distribution**

Supports large-scale image distribution in a single region and concurrent image pulls on 500 nodes. Supports cross-region image replication and cross-cloud synchronous image distribution. Supports manual and automatic image replication.

**Seamless integration with other Alibaba Cloud services**

Integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to implement continuous deployment after images are updated.

### 1.3 Features

This topic describes the core features of Container Registry and the availability of each feature in different ACR editions. These features include instance management, artifact distribution and management, container image signing and management, and integration with container platforms for passwordless pull and visual deployment. These capabilities help enterprises efficiently manage the full lifecycle of container images.

| Primary Feature | Secondary Feature | Description | ACR Standard Edition | ACR Premium Edition | ACR Multi- instance Edition |
|---|---|---|---|---|---|
| Instance Management | Create Multiple Instances | Supports creating multiple instances. By default, up to 100 instances are supported. | Not supported | Not supported | Supported |
|   | Cross- instance Image Sync | Supports synchronizing image repositories across instances. | Not supported | Not supported | Supported |

|   | Delete Instance | Supports deleting and releasing image instances. | Not supported | Not supported | Supported |
|---|---|---|---|---|---|
| Artifact Distribution | Manual Sync | Supports manually triggering sync for a specific image version to enable disaster recovery and backup across regions. | Supported | Supported | Supported |
|   | Automatic Sync | Supports automatic synchronizati on based on sync rules after an image is pushed. | Not supported | Supported | Supported |
|   | Triggers | Supports automatically triggering events when a container image is updated. | Supported | Supported | Supported |
|   | DADI Image Acceleration | Supports DADI image acceleration. | Not supported | Supported | Supported |
|   | Encrypted Image Distribution | Supports distributing container images using the HTTPS encryption protocol. | Supported | Supported | Supported |

|   | Image Signing | Supports signing container images to ensure end- to-end consistency from distribution to deployment and prevent man-in-the- middle attacks and unauthorized image updates or execution. | Supported | Supported | Not supported |
|---|---|---|---|---|---|
| Artifact Security |   |   |   |   |   |
|   | Signing Management | Supports GUI- based operations to add signatures at the instance and namespace levels. Note This feature depends on KMS and Containe r Security products and requires them to be used together. | Supported | Supported | Supported |

| Artifact Management | Container Images | Supports immutable image versions. | Not supported | Supported | Supported |
|---|---|---|---|---|---|
|   |   | Supports secure hosting of container images organized by namespace. | Not supported | Supported | Supported |
|   |   | Supports querying image versions and deleting image repositories. | Not supported | Supported | Supported |
|   |   | Supports permission management for ASCM departments and resource sets, along with RAM user permissions. | Supported | Supported | Supported |
| Deployment Integration | Passwordless Pull | Supports passwordless pull configuration during deployment on container platforms, eliminating the need to reconfigure Secrets for every deployment. | Supported | Supported | Not supported |

|   | Deployment Selection | Supports visually selecting image repositories and versions from ACR during deployment on container platforms. | Supported | Supported | Supported |
|---|---|---|---|---|---|

### 1.4 Scenarios

Container Registry is suitable for scenarios such as continuous delivery and automatic image synchronization.

**Continuous delivery**

Container Registry is integrated with Jenkins to automate DevOps pipelines from code committing to application deployment and ensure that code is committed for deployment only after the code passes automated testing. This simplifies application deployment and accelerates application iteration. DevOps automation Container Registry can automate DevOps pipelines, from code update to code building, image building, and application deployment. Environment consistency Container Registry lets you deliver code together with the runtime environment that is built based on an immutable architecture. Continuous feedback Container Registry returns results in real time after integration or delivery.

**Automatic image synchronization**

Your containerized applications may require deployment across multiple regions. In such scenarios, you can commit a container application once for deployment to multiple regions. The image synchronization feature of Container Registry improves automated distribution efficiency, reduces manual O&M costs, and enhances disaster recovery capabilities. Multi-scenario synchronization Supports synchronization across regions. Supports both manual synchronization and automatic synchronization triggered by image updates. Scheduling optimization Optimizes the scheduling of image synchronization to increase the success rate. Security and compliance Supports data encryption to ensure the security of the synchronized images.

### 1.5 Key concepts

This topic introduces the key concepts of Alibaba Cloud Container Registry (ACR) to help you build a foundational understanding of the service.

**Container image**

A container image is a standardized delivery artifact that contains an application and all its dependencies. You can build an application into a container image with a Dockerfile, push the image to an image repository, and then pull it to start containers in your test or production environments.

**Container registry instance**

To manage private images, you first create a container registry instance and image repositories within it. After logging in to a repository, you can push new versions of a modified image or push an image built locally.

**OCI artifact**

In addition to container images, ACR supports packaging various types of data, such as Helm charts and CNAB bundles, into OCI-compliant artifacts. These artifacts follow the structure defined by the OCI artifact specification, including manifests and indexes. This provides a unified way to store, manage, and distribute different types of artifacts.

**RAM access control**

Resource Access Management (RAM) is an Alibaba Cloud service that lets you manage user identities and resource access permissions. You can create multiple RAM users under a single Alibaba Cloud account to represent employees, systems, or applications within your organization.

**RAM user**

A RAM user is an identity in RAM with a unique ID and credentials. A RAM user typically represents a person or an application. You can grant different image access permissions to different RAM users.

**Helm chart**

Helm is a package manager for Kubernetes that helps you manage charts and their running instances, known as releases. A chart is a collection of files that describe a related set of Kubernetes resources. It contains everything needed to run an application, including images, dependencies, and resource definitions. For example, a single chart can deploy a combination of WordPress and MySQL, or an etcd cluster.

**OSS**

Object Storage Service (OSS) is an Alibaba Cloud storage service that offers high scalability, security, durability, and cost-effectiveness. OSS provides a platformindependent RESTful API that lets you store and access any type of data from any application.

**OSS bucket**

An OSS bucket is a container that stores objects in OSS. All objects must reside in a bucket. A bucket has configurable properties, such as its region, access permissions, and storage class. You can create different types of buckets to meet your specific data storage needs. The Enterprise Edition of Alibaba Cloud Container Registry (ACR) uses a customizable OSS bucket to host container images.

### 1.6 Limitations

Before using Container Registry (ACR), understand its limitations.

| Limit | Value |   |   |
|---|---|---|---|
|   | Standard edition | Advanced edition | Multi-instance edition |
| Number of namespaces | 15 | 1,000 | 1,000 |
| Number of image repositories per namespace | 1,000 | 100,000 | 100,000 |
| Number of instances | / | / | 100 |
