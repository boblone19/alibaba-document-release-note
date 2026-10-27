---
title: "Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack"
product_version: "V3.18.6"
doc_version: "20260703"
pdf_pages: 158
source_pdf: "openshift.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

## Table of Contents

- 1 Introduction of Red Hat Openshift Container
- 2 Introduction of Alibaba Cloud Apsara Stack
  - 2.1 Overview of Alibaba Cloud Apsara Stack
  - 2.2 Cloud Products on Apsara Stack
- 3 Architecture and Planning
  - 3.1 Installation approaches
  - 3.2 Agent-based installer workflow
  - 3.3 Feasibility analysis of deploying Openshift Cloud
  - 3.4 Resource Planning
- 4 Preparing Cluster on Apsara Stack
  - 4.1 Creating and configuring resources on Apsara Stack
  - 4.2 Disconnected Environments Preparation
- 5 Installation using agent-based installer
- 6 Optional Steps
  - 6.1 Log into Openshift cluster via CLI
  - 6.2 Log into Openshift web console
  - 6.3 Monitor cluster
  - 6.4 Manage cluster
- 7 OpenShift updates
  - 7.1 Introduction to OpenShift updates
  - 7.2 How cluster updates work
  - 7.3 Understanding update channels and releases
  - 7.4 Understanding OpenShift Container Platform update
  - 7.5 Preparing to update a cluster
  - 7.6 Performing a cluster update
  - 7.7 Troubleshooting a cluster update
- 8 Summary
- 9 Frequently Asked Questions (FAQs)
  - 9.1 Support
  - 9.2 does volumes in Apsara Stack supports increasing disk
  - 9.3 why do we need to perform a deta clone in Section

**Red Hat OpenShift**

**Container Platform 4.18 on**

**Alibaba Cloud Apsara Stack**

**Product version：OpenShift 4.18**

**Apsara Stack 3.18.6**

**Document version：20260703**

Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Legal disclaimer**

of this legal disclaimer before you read or use this document. If you have read or used this 1. You shall download and obtain this document from the Alibaba Cloud website or other Alibaba Cloud-authorized channels, and use this document for your own legal information of Alibaba Cloud. You shall strictly abide by the confidentiality obligations. No part of this document shall be disclosed or provided to any third party for use without the prior written consent of Alibaba Cloud. 2. No part of this document shall be excerpted, translated, reproduced, transmitted, or disseminated by any organization, company or individual in any form or by any means without the prior written consent of Alibaba Cloud. 3. The content of this document may be changed because of product version upgrade, adjustment, or other reasons. Alibaba Cloud reserves the right to modify the content of this document without notice and an updated version of this document will be released through Alibaba Cloud-authorized channels from time to time. You should pay attention to the version changes of this document as they occur and download and obtain the most up-to-date version of this document from Alibaba Cloudauthorized channels. 4. This document serves only as a reference guide for your use of Alibaba Cloud products and services. Alibaba Cloud provides this document based on the "status quo", "being defective", and "existing functions" of its products and services. Alibaba Cloud makes every effort to provide relevant operational guidance based on existing technologies. However, Alibaba Cloud hereby makes a clear statement that it in no way guarantees the accuracy, integrity, applicability, and reliability of the content of this document, either explicitly or implicitly. Alibaba Cloud shall not take legal responsibility for any errors or lost profits incurred by any organization, company, or individual arising from download, use, or trust in this document. Alibaba Cloud shall not, under any circumstances, take responsibility for any indirect, consequential, punitive, contingent, special, or punitive damages, including lost profits arising from the use or trust in this document (even if Alibaba Cloud has been notified of the possibility of such a loss). 5. Alibaba Cloud products and services may be used in combination with third-party software, hardware, or services that are procured, deployed, and maintained by you or other third parties, including but not limited to Red Hat OpenShift. Alibaba Cloud and such third-party vendors separately offer support to their respective customers. Each vendor is solely responsible for the delivery, deployment, operation, maintenance, and support of its own products and services within its established scope. Alibaba Cloud makes no representation, warranty, or guarantee regarding the compatibility, interoperability, or performance of Alibaba Cloud products and services when used Page 2 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack with any third-party software, hardware, or services. Alibaba Cloud shall not be liable for any issues, errors, or damages arising from or related to the use of third-party software, hardware, or services, including but not limited to Red Hat OpenShift, or from the integration or combination of such third-party offerings with Alibaba Cloud products and services. You acknowledge that using Alibaba Cloud products and services with unsupported or uncertified third-party components may introduce risks to your environment and that you are solely responsible for assessing and managing such risks. 6. By law, all the contents in Alibaba Cloud documents, including but not limited to pictures, architecture design, page layout, and text description, are intellectual property of Alibaba Cloud and/or its affiliates. This intellectual property includes, but is not limited to, trademark rights, patent rights, copyrights, and trade secrets. No part of this document shall be used, modified, reproduced, publicly transmitted, changed, disseminated, distributed, or published without the prior written consent of Alibaba Cloud and/or its affiliates. The names owned by Alibaba Cloud shall not be used, published, or reproduced for marketing, advertising, promotion, or other purposes without the prior written consent of Alibaba Cloud. The names owned by Alibaba Cloud include, but are not limited to, "Alibaba Cloud", "Aliyun", "HiChina", and other brands of Alibaba Cloud and/or its affiliates, which appear separately or in combination, as well as the auxiliary signs and patterns of the preceding brands, or anything similar to the company names, trade names, trademarks, product or service names, domain names, patterns, logos, marks, signs, or special descriptions that third parties identify as Alibaba Cloud and/or its affiliates. 7. Please directly contact Alibaba Cloud for any errors of this document. Page 3 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Content Legal disclaimer .......................................................................................................................................................................... 2 Introduction of Red Hat Openshift Container Platform ....................................................................................... 6 Introduction of Alibaba Cloud Apsara Stack ........................................................................................................... 7 2.1 Overview of Alibaba Cloud Apsara Stack .......................................................................................................... 7 2.2 Cloud Products on Apsara Stack .......................................................................................................................... 8 Architecture and Planning.............................................................................................................................................. 9 3.1 Installation approaches .................................................................................................................................... 9 3.2 Agent-based installer workflow .................................................................................................................. 10 3.3 Feasibility analysis of deploying Openshift Cloud Platform on Apsara Stack .............................. 11 3.3.1 Cluster resources .................................................................................................................................... 11 3.3.2 Network resources ................................................................................................................................. 12 3.4 Resource Planning ........................................................................................................................................... 13 Preparing Cluster on Apsara Stack ............................................................................................................................ 15 4.1 Creating and configuring resources on Apsara Stack ................................................................................. 15 4.1.1 Create VPC ................................................................................................................................................ 15 4.1.2 Create vSwitch ......................................................................................................................................... 17 4.1.3 Create and configure security group ............................................................................................... 19 4.1.4 Configure DNS ........................................................................................................................................ 21 4.1.5 Create ECS instances ............................................................................................................................. 23 4.1.6 Configure SLB instance ......................................................................................................................... 26 4.1.7 Configure OSS bucket ........................................................................................................................... 29 4.2 Disconnected Environments Preparation ................................................................................................. 31 4.2.1 About disconnected environments .................................................................................................. 32 4.2.2 About disconnected installation mirroring .................................................................................... 33 Installation using agent-based installer .................................................................................................................. 48 5.1.1 Downloading the Agent-based Installer ........................................................................................ 49 5.1.2 Verifying the supported architecture for an Agent-based installation ................................ 49 5.1.3 Creating the preferred configuration inputs ................................................................................. 50 5.1.4 Creating and boot the agent image ................................................................................................ 50 5.1.5 Verifying that the current installation host can pull release images ..................................... 55 5.1.6 Tracking and verifying installation progress .................................................................................. 56 Optional Steps .................................................................................................................................................................. 64 6.1 Log into Openshift cluster via CLI ............................................................................................................... 64 6.2 Log into Openshift web console ................................................................................................................. 65 6.3 Monitor cluster .................................................................................................................................................. 65 6.4 Manage cluster ................................................................................................................................................. 67 OpenShift updates .......................................................................................................................................................... 68 7.1 Introduction to OpenShift updates ............................................................................................................ 68 7.1.1 Cluster update overview ...................................................................................................................... 68 7.1.2 Common questions about update availability .............................................................................. 69 7.1.3 About the OpenShift Update Service .............................................................................................. 70 7.1.4 Understanding cluster Operator condition types ........................................................................ 71 7.1.5 Understanding cluster version condition types ............................................................................ 72 7.1.6 Common terms ....................................................................................................................................... 73 7.2 How cluster updates work ............................................................................................................................. 74 7.2.1 The ClusterVersion object .................................................................................................................... 74 Page 4 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack 7.2.2 Evaluation of update availability ........................................................................................................ 77 7.2.3 Release images ........................................................................................................................................ 77 7.2.4 Update process workflow .................................................................................................................... 78 7.2.5 Understanding how manifests are applied during an update ................................................ 79 7.2.6 Understanding how the Machine Config Operator updates nodes...................................... 81 7.3 Understanding update channels and releases ....................................................................................... 83 7.3.1 Overview of update channels ............................................................................................................. 83 7.3.2 Update channels ..................................................................................................................................... 84 7.3.3 Restricted network clusters ................................................................................................................. 85 7.3.4 Update recommendations in the channel ..................................................................................... 85 7.3.5 Update recommendations and Conditional Updates ................................................................ 85 7.3.6 What to consider when choosing an update channel ............................................................... 86 7.3.7 Considerations for switching between channels.......................................................................... 87 7.4 Understanding OpenShift Container Platform update duration ...................................................... 87 7.4.1 Factors affecting update duration .................................................................................................... 87 7.4.2 Cluster update phases .......................................................................................................................... 88 7.4.3 How to estimate cluster update time .............................................................................................. 91 7.4.4 Red Hat Enterprise Linux (RHEL) compute nodes ....................................................................... 91 7.5 Preparing to update a cluster ...................................................................................................................... 92 7.5.1 Preparing to update to OpenShift Container Platform 4.18 .................................................... 92 7.5.2 Preflight validation for Kernel Module Management (KMM) Modules ................................ 95 7.5.3 Preparing to update from OpenShift Container Platform 4.18 to a newer version ......... 97 7.6 Performing a cluster update .......................................................................................................................101 7.6.1 Updating a cluster using the CLI .....................................................................................................101 7.6.2 Updating a cluster using the web console ...................................................................................109 7.6.3 Performing a Control Plane Only update .....................................................................................115 7.6.4 Performing a canary rollout update ...............................................................................................119 7.6.5 Updating a cluster in a disconnected environment ..................................................................129 7.7 Troubleshooting a cluster update ............................................................................................................154 7.7.1 Gathering data about your cluster update ..................................................................................154 Summary ..........................................................................................................................................................................157 Frequently Asked Questions (FAQs) .......................................................................................................................157 9.1 Support ..............................................................................................................................................................157 9.2 does volumes in Apsara Stack supports increasing disk performance for control planes? ..158 9.3 why do we need to perform a deta clone in Section 4.1.5? ............................................................158 Page 5 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

## 1 Introduction of Red Hat Openshift Container

**Platform**

OpenShift Container Platform is a platform for developing and running containerized applications. It is designed to allow applications and the data centers that support them to expand from just a few machines and applications to thousands of machines that serve millions of clients. With its foundation in Kubernetes, OpenShift Container Platform incorporates the same technology that serves as the engine for massive telecommunications, streaming video, gaming, banking, and other applications. Its implementation in open Red Hat technologies lets you extend your containerized applications beyond a single cloud to on-premise and multi-cloud environments. Page 6 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack OpenShift Container Platform provides enterprise-ready enhancements to Kubernetes, including the following enhancements: ●Integrated Red Hat technology. Major components in OpenShift Container Platform come from Red Hat Enterprise Linux (RHEL) and related Red Hat technologies. OpenShift Container Platform benefits from the intense testing and certification initiatives for Red Hat’s enterprise quality software. ●Open source development model. Development is completed in the open, and the source code is available from public software repositories. This open collaboration fosters rapid innovation and development. Although Kubernetes excels at managing your applications, it does not specify or manage platform-level requirements or deployment processes. Powerful and flexible platform management tools and processes are important benefits that OpenShift Container Platform 4.18 offers.

## 2 Introduction of Alibaba Cloud Apsara Stack

### 2.1 Overview of Alibaba Cloud Apsara Stack

Alibaba Cloud Apsara Stack is an open, unified, and trusted cloud solution that is tailored for enterprise customers. Apsara Stack is developed based on the same distributed architecture as Alibaba Cloud. Apsara Stack allows enterprises to deploy public cloud services in onpremises environments and implement auto scaling of services with a few clicks based on public cloud resources. Apsara Stack provides stable, secure, all-in-one, lightweight, and easy-to-integrate capabilities that allow enterprises of different business scales to adapt to various business scenarios. Both Apsara Stack and Alibaba Cloud public cloud are based on Apsara Distributed Operating System. Apsara Distributed Operating System provides underlying services such as storage, computing, and scheduling for upper-layer services. Apsara Distributed Operating System is a hyper-scale universal operating system developed by Alibaba Cloud. Apsara Distributed Operating System connects millions of servers around the world to act as a supercomputer and provides computing capabilities such as online public services. The computing capabilities provided by Apsara Distributed Operating System are powerful, universal, and accessible to everyone. Page 7 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 2.2 Cloud Products on Apsara Stack

| Cloud Product | Description |
|---|---|
| ASCM (Apsara Uni- Manager, unified cloud management platform) | Apsara Uni-manager provides various operations management features, such as resource management, user management, permission management, operations center, and security center. |
| ECS (Elastic Compute Service) | ECS is a computing service that provides scalable processing capabilities. You can create ECS instances, scale cloud disks, or batch release ECS instances at any time based on your business requirements. You can also import customized images for ECS instances. |
| EBS (Elastic Block Storage) | EBS provides block-level random storage that features low latency and provides high performance, durability, and reliability for ECS instances. EBS devices use the triplicate distributed storage mechanism to ensure data durability for ECS instances. You can create, release, and resize EBS devices based on your business requirements. |
| VPC (Virtual Private Cloud) | A VPC provides network services for resources in the cloud. Different VPCs are logically isolated from each other. You have full control over your VPC. For example, you can specify CIDR blocks, and configure route tables and gateways for your VPC. In your VPCs, you can use Alibaba Cloud resources, such as ECS instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances. VPC also provides built-in NAT gateway features. |

Page 8 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| SLB (Server Load Balancer) | SLB is an Alibaba Cloud service that distributes inbound network traffic across multiple backend servers. The backend servers are ECS instances, and traffic is routed to these servers based on forwarding rules. SLB extends the service capability of applications and enhances their availability. |
|---|---|
| Apsara Stack DNS (Domain Name System) | Apsara Stack DNS provides the Domain Name System (DNS) resolution and global server load balancing (GSLB) services for virtual private clouds (VPCs), networks of self-managed data centers, and classic networks. |
| OSS (Object Storage Service) | OSS is a storage service designed to store large amounts of unstructured data such as images, audio, and videos on the Internet. |

Find more details on homepage of Alibaba Cloud Apsara Stack: https://www.alibabacloud.com/en/product/apsarastack/download?tags=V3.18.6,ProductIntroduction

## 3 Architecture and Planning

This chapter describes the architecture and planning of a typical Red Hat Openshift cluster with 3 control-plane nodes and 3 compute nodes.

### 3.1 Installation approaches

The OpenShift Container Platform installation program offers four methods for deploying a cluster which are detailed in the following list: ●**Interactive**: You can deploy a cluster with the web-based Assisted Installer. This is an ideal approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform, it provides smart defaults, and it performs pre-flight validations before installing the cluster. It also provides a RESTful API for automation and advanced configuration scenarios. ●**Local Agent-based**: You can deploy a cluster locally with the Agent-based Installer for disconnected environments or restricted networks. It provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface. This approach is ideal for disconnected environments. ●**Automated**: You can deploy a cluster on installer-provisioned infrastructure. The installation program uses each cluster host’s baseboard management Page 9 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack controller (BMC) for provisioning. You can deploy clusters in connected or disconnected environments. ●**Full control**: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments. In this case Agent-based installation method is used. With the Agent-based installation method provides the flexibility to boot your Apsara Stack ECSs in any way that you choose. It combines the ease of use of the Assisted Installation service with the ability to run offline, including in air-gapped environments. Agent-based installation is a subcommand of the OpenShift Container Platform installer. It generates a bootable ISO image containing all of the information required to deploy an OpenShift Container Platform cluster, with an available release image.

### 3.2 Agent-based installer workflow

One of the control plane hosts runs the Assisted Service at the start of the boot process and eventually becomes the bootstrap host. This node is called the **rendezvous host** (node 0). The Assisted Service ensures that all the hosts meet the requirements and triggers an OpenShift Container Platform cluster deployment. All the nodes have the Red Hat Enterprise Linux CoreOS (RHCOS) image written to the disk. The non-bootstrap nodes reboot and initiate a cluster deployment. Once the nodes are rebooted, the rendezvous host reboots and joins the cluster. The bootstrapping is complete and the cluster is deployed. Page 10 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack This documentation shows an example of deploying a three-node Openshift Container Platform cluster.

### 3.3 Feasibility analysis of deploying Openshift Cloud

**Platform on Apsara Stack**

**Cluster resources**

**3.3.1**

| Requirement of Openshift Cloud Platform | Capabilities of Apsara Stack |
|---|---|
| ➔ CPU architecture | ★ Apsara Stack supports multiple CPU |
| ➔ required flavor to host RHCOS | architecture, such as 64-bit x86, 64-bit |
| ➔ mounting ISO image | ARM. |

Page 11 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

|   | ★ Aspara Stack provides multiple ECS |
|---|---|
|   | specifications. In this case a typical |
|   | specification of 8c16G will be used. |
|   | ★ Apsara Stack supports to mount ISO |
|   | images to ECS instances （while it's |
|   | more recommended to use template |
|   | such as .qcow2 or .vhd） |

**Network resources**

**3.3.2**

**DHCP**

**3.3.2.1**

| Requirement of Openshift Cloud Platform | Capabilities of Apsara Stack |
|---|---|
| ➔ You must specify the value for the | ★ Apsara Stack provides built-in DHCP |
| rendezvousIP | service in VPC network for tenants, with |
|   | default gateway, DNS server information |
|   | and a rendezvousIP. |

**Static networking**

**3.3.2.2**

| Requirement of Openshift Cloud Platform | Capabilities of Apsara Stack |
|---|---|
| ➔ If a value is not specified for the | ★ rendezvousIP can be specified when |
| rendezvousIP field, one address will be | creating ECS instances. |
| chosen from the static IP addresses | ★ MAC address is generated and assigned |
| specified in the networkConfig fields. | automatically. |
| ➔ The MAC address of an interface on the | ★ DNS/Next hop addresses are delivered |
| host, used to determine which host to | by DHCP automatically in Apsara Stack. |
| apply the configuration to. |   |
| ➔ The static IP address of the target host. |   |
| ➔ The static IP address’s subnet prefix for |   |
| the target bare metal host. |   |
| ➔ The DNS server for the target host. |   |
| ➔ Next hop address for the node traffic. |   |
| This must be in the same subnet as the IP |   |
| address set for the specified interface. |   |

**DNS**

**3.3.2.3**

| Requirement of Openshift Cloud Platform | Capabilities of Apsara Stack |
|---|---|
| ➔ Reverse DNS resolution required for | ★ Apsara Stack provides built-in DNS service |
| the Kubernetes API, the control plane | for tenants, supporting reverse DNS, |
| machines and the compute machines. | A/AAAA/CNAME and PTR records. |

Page 12 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| ➔ DNS A/AAAA or CNAME records, and |   |
|---|---|
| PTR records are required. |   |

**Load balancing**

**3.3.2.4**

| Requirement of Openshift Cloud Platform | Capabilities of Apsara Stack |
|---|---|
| ➔ Layer 4 load balancing for API load | ★ Apsara Stack provides built-in SLB |
| balancer and application ingress load | service for tenants, supporting both |
| balancer. | Layer 4 and Layer 7 load balancing with |
| ➔ A stateless load balancing algorithm | multiple algorithm (including stateless |
|   | load balancing) |

### 3.4 Resource Planning

| Apsara Stack Cloud | Qty. of | Resource Information | Role in Openshift |
|---|---|---|---|
| Resource | resource |   | Cloud Platform |
| VPC | 1 | provides DHCP, static network for ECS instances | DHCP, static networking |
| DNS | -- | provides reverse resolution, A/AAAA/CNAME/PTR records | DNS |
| SLB | 1 | provides load balancing for cluster | Load balancer |
| ECS | 7 | provides 3 ECS instance as control plane, 3 as worker nodes and 1 as installation node. | Cluster |

**Diagram of cluster**

**ECS instances**

Page 13 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

|   |   | Specification |
|---|---|---|
| Name | IP address |   |
|   |   | (vCPU/Memory/Storage) |
| installer | 192.168.33.58 | 4C/8G/200G |
| master0 | 192.168.33.60 | 8C/16G/200G |
| master1 | 192.168.33.61 | 8C/16G/200G |
| master2 | 192.168.33.62 | 8C/16G/200G |
| worker0 | 192.168.33.70 | 8C/16G/200G |
| worker1 | 192.168.33.71 | 8C/16G/200G |
| worker2 | 192.168.33.72 | 8C/16G/200G |
| worker3 | 192.168.33.73 | 8C/16G/200G |

**DNS records**

| Record | Value | Type |
|---|---|---|
| api.ocptest.apsara | 192.168.33.80 | A |
| api-int.ocptest.apsara | 192.168.33.80 | A |
| *.apps.ocptest.apsara | 192.168.33.80 | A |
| master0.ocptest.apsara | 192.168.33.60 | A |
| master1.ocptest.apsara | 192.168.33.61 | A |
| master2.ocptest.apsara | 192.168.33.62 | A |
| worker0.ocptest.apsara | 192.168.33.70 | A |
| worker1.ocptest.apsara | 192.168.33.71 | A |
| worker2.ocptest.apsara | 192.168.33.72 | A |
| worker3.ocptest.apsara | 192.168.33.73 | A |
| etcd-0.ocptest.apsara | 192.168.33.60 | A |
| etcd-1.ocptest.apsara | 192.168.33.61 | A |
| etcd-2.ocptest.apsara | 192.168.33.62 | A |
| 80.33.168.192.in-addr.arpa. | api.ocptest.apsara. api-int.ocptest.apsara. | PTR |
| 69.33.168.192.in-addr.arpa. | bootstrap.ocptest.apsara. | PTR |
| 60.33.168.192.in-addr.arpa. | master0.ocptest.apsara. | PTR |
| 61.33.168.192.in-addr.arpa. | master1.ocptest.apsara. | PTR |
| 62.33.168.192.in-addr.arpa. | master2.ocptest.apsara. | PTR |
| 70.33.168.192.in-addr.arpa. | worker0.ocptest.apsara. | PTR |
| 71.33.168.192.in-addr.arpa. | worker1.ocptest.apsara. | PTR |
| 72.33.168.192.in-addr.arpa. | worker2.ocptest.apsara. | PTR |
| 73.33.168.192.in-addr.arpa. | worker3.ocptest.apsara. | PTR |

**SLB listeners**

| port | back-end server | description |
|---|---|---|
| 6443 | control plane (You must configure the /readyz endpoint for the API server health check probe.) | Kubernetes API server |

Page 14 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| 22623 | control plane | Machine config server |
|---|---|---|
| 443 | The machines that run the Ingress Controller pods, compute, or worker, by default. | HTTPS traffic |
| 80 | The machines that run the Ingress Controller pods, compute, or worker, by default. | HTTP traffic |

## 4 Preparing Cluster on Apsara Stack

### 4.1 Creating and configuring resources on Apsara Stack

Prerequisites: ●A workstation with internet browser and access to the Internet ●Access to Apsara Stack ASCM ●Access to Red Hat Portal ●username with full access to VPC/SLB/DNS/ECS/OSS. ○VPC ○SLB ○DNS ○ECS ○OSS

**Create VPC**

**4.1.1**

Navigate to "Virtual Private Cloud" console after log into ASCM. Page 15 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Click on button "Create VPC" and fill the fields as per table below. Page 16 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Create vSwitch**

**4.1.2**

After VPC is created, create vSwitch as below. Page 17 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Page 18 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Create and configure security group**

**4.1.3**

In this case, a security group will be applied on ECS instances, including control plane nodes, compute nodes and installer node. To create the security group, navigate to "Security Groups" section under "Elastic Compute Service" page, and click on button "Create Security Group". Page 19 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Configure policies in security group as below to allow external traffic towards specified ports. Page 20 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Configure DNS**

**4.1.4**

DNS service is used for internal domain name resolving and hostname delivering. To configure DNS entries as planned, navigate to "Alibaba Cloud DNS" in top menu. Page 21 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Click on button "Add Domain Name" under "Private Domain Name for VPC" section. Configure entries as planned in Chapter 3.4.2.3 Page 22 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Create ECS instances**

**4.1.5**

To create ECS instance for installer, master nodes and worker nodes according to planned resources in Chapter 3.5 Resource Planning, navigate to "ECS instances" under section of "Elastic Compute Service" and click "Create Instance". Page 23 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Page 24 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Mirror: For now we can just use a random image, and in later steps we will replace the image with a custom image spcifically for master and worker nodes. Configure system disk type as "Premium Performance Disk" and set capacity to 200GB: For network part, select the VPC and VSwitch created in Chapter 4.1.1 and 4.1.2. Specify IP address for ECS instances according to Chapter 3.5. Page 25 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Select security group created in Chapter 4.1.3: In this case, master nodes and worker nodes are using same instance type, so it's possible to create these instances in one time: After all this configured and submitted, ECS instances will be created:

**Configure SLB instance**

**4.1.6**

To create SLB instance, navigate to "Server Load Balancer(SLB)" page: Page 26 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Click "Create SLB" button under "Instance Management" section: Configure name and specification of SLB instance. For test scenario, using "Small I" specification with 3000 CPS and 1000 QPS is enough. For "Instance Type", select "Intranet". For "Network Type", select "VPC", then select VPC created in Chapter 4.1.1 and VSwitch created in Chapter 4.1.2. Specify service IP planned in Chapter 3.5. Page 27 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Submit the configuration and SLB instance is created: Click the instance ID, and navigate to "Add Listener": Page 28 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Configure Listeners as planned in Chapter 3.5:

**Configure OSS bucket**

**4.1.7**

OSS bucket will be used for importing ECS image. Navigate to "Object Storage Service": Page 29 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Click on button "Create Bucket" in section of "Buckets": Create bucket as below: Page 30 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack To upload files into the bucket:

### 4.2 Disconnected Environments Preparation

This chapter provides information about install preparation of OpenShift Container Platform clusters in environments without internet access. Page 31 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**About disconnected environments**

**4.2.1**

A disconnected environment is an environment that does not have full access to the internet. Apsara Stack, as a private cloud solution, was more focused on disconnected requirements in the local data center of customers. OpenShift Container Platform is designed to perform many automatic functions that depend on an internet connection, such as retrieving release images from a registry or retrieving update paths and recommendations for the cluster. Without a direct internet connection, you must perform additional setup and configuration for your cluster to maintain full functionality in the disconnected environment.

**Glossary of disconnected environment terms**

**4.2.1.1**

Although it is used throughout the OpenShift Container Platform documentation, disconnected environment is a broad term that can refer to environments with various levels of internet connectivity. Other terms are sometimes used to refer to a specific level of internet connectivity, and these environments might require additional unique configurations. The following table describes the different terms used to refer to environments without a full internet connection:

| Term | Description |
|---|---|
| Air-gapped network | An environment or network that is completely isolated from an external network. This isolation depends on a physical separation, or an "air gap", between machines on the internal network and any other part of an external network. Air-gapped environments are often used in industries with strict security or regulatory requirements. |
| Disconnected environment | An environment or network that has some level of isolation from an external network. This isolation could be enabled by physical or logical separation between machines on the internal network and an external network. Regardless of the level of isolation from the external network, a cluster in a disconnected environment does not have access to public services hosted by Red Hat and requires additional setup to maintain full cluster functionality. |
| Restricted Network | An environment or network with limited connection to an external network. A physical connection may exist between machines on the internal network and an external network, but network traffic is limited by additional configurations, such as with firewalls and proxies. |

Page 32 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Preferred methods for working with disconnected environments**

**4.2.1.2**

You can choose between multiple options for most aspects of managing a cluster in a disconnected environment. For example, when mirroring images you can choose between using the oc-mirror OpenShift CLI (oc) plugin or using the oc adm command. However, some options provide a simpler and more convenient user experience for disconnected environments, and are the preferred method over their alternatives. Unless your organizational needs require you to choose another option, use the following methods for mirroring images, installing your cluster, and updating your cluster: Mirror your images using the oc-mirror plugin v2. Install your cluster using the Agent-based Installer. Update your cluster using a local OpenShift Update Service instance.

**About disconnected installation mirroring**

**4.2.2**

As a cluster administrator, you can use a mirror registry to ensure that your clusters only use container images that satisfy your organizational controls on external content.

**Mirror registries for installing clusters in disconnected environments**

**4.2.2.1**

You must mirror required container images into a disconnected environment before you can install and provision a cluster there. To mirror those container images, you must have a mirror registry. Consider the following options for creating and using a mirror registry: If you already have a container image registry, such as Red Hat Quay, you can use it as your mirror registry. If you do not already have a registry, you must create one. After you establish your registry, you need mirroring tools. To mirror your OpenShift Container Platform image repository to the mirror registry in your disconnected environment, you can use the oc-mirror OpenShift CLI (oc) plugin. The oc-mirror plugin is a single tool that mirrors all required OpenShift Container Platform content and other images to your mirror registry. The oc-mirror plugin is the preferred method for mirroring. Alternately, you can use the oc adm command to mirror just release and catalog images for OpenShift Container Platform.

**Creating a mirror registry with mirror registry for Red Hat OpenShift**

**4.2.2.2**

If you already have a container image registry, such as Red Hat Quay, you can skip this section and go straight to Mirroring the OpenShift Container Platform image repository.
**Important**: The mirror registry for Red Hat OpenShift is not intended to be a substitute for
a production deployment of Red Hat Quay.

**4.2.2.2.1Prerequisites**

●An OpenShift Container Platform subscription. Page 33 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Red Hat Enterprise Linux (RHEL) 8 and 9 with Podman 3.4.2 or later and OpenSSL installed. If you are using Podman 5.7 or later, see "Configuring rootless Podman networking". ●Fully qualified domain name for the Red Hat Quay service, which must resolve through a DNS server. ●Key-based SSH connectivity on the target host. SSH keys are automatically generated for local installs. For remote hosts, you must generate your own SSH keys. ●2 or more vCPUs. ●8 GB of RAM. ●About 12 GB for OpenShift Container Platform 4.18 release images, or about 358 GB for OpenShift Container Platform 4.18 release images and OpenShift Container Platform 4.18 Red Hat Operator images.
**Important**:
Up to 1 TB per stream or more is suggested. These requirements are based on local testing results with only release images and Operator images. Storage requirements can vary based on your organization’s needs. You might require more space, for example, when you mirror multiple z-streams. You can use standard Red Hat Quay functionality or the proper API callout to remove unnecessary images and free up space.

**4.2.2.2.2Mirror registry for Red Hat OpenShift introduction**

For disconnected deployments of OpenShift Container Platform, a container registry is required to carry out the installation of the clusters. To run a production-grade registry service on such a cluster, you must create a separate registry deployment to install the first cluster. The mirror registry for Red Hat OpenShift addresses this need and is included in every OpenShift Container Platform subscription. It is available for download on the OpenShift console **Downloads** page. The mirror registry for Red Hat OpenShift allows users to install a small-scale version of Red Hat Quay and its required components by using the mirror-registry command-line interface (CLI) tool. The mirror registry for Red Hat OpenShift is deployed automatically with pre-configured local storage and a local database. It also includes auto-generated user credentials and access permissions with a single set of inputs and no additional configuration choices to get started. The mirror registry for Red Hat OpenShift provides a pre-determined network configuration and reports deployed component credentials and access URLs upon success. A limited set of optional configuration inputs such as fully qualified domain name (FQDN) services, superuser name and password, and custom TLS certificates are also provided. This provides users with a container registry so that they can easily create an offline mirror of all OpenShift Container Platform release content when running OpenShift Container Platform in restricted network environments. Use of the mirror registry for Red Hat OpenShift is optional if another container registry is already available in the install environment. Page 34 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**4.2.2.2.2.1Mirror registry for Red Hat OpenShift limitations**

The following limitations apply to the mirror registry for Red Hat OpenShift: ●The mirror registry for Red Hat OpenShift is not a highly-available registry and only local file system storage is supported. It is not intended to replace Red Hat Quay or the internal image registry for OpenShift Container Platform. ●The mirror registry for Red Hat OpenShift is not intended to be a substitute for a production deployment of Red Hat Quay. ●The mirror registry for Red Hat OpenShift is only supported for hosting images that are required to install a disconnected OpenShift Container Platform cluster, such as Release images or Red Hat Operator images. It uses local storage on your Red Hat Enterprise Linux (RHEL) machine, and storage supported by RHEL is supported by the mirror registry for Red Hat OpenShift.
**Note**: Because the mirror registry for Red Hat OpenShift uses local storage, you should
remain aware of the storage usage consumed when mirroring images and use Red Hat Quay’s garbage collection feature to mitigate potential issues. For more information about this feature, see "Red Hat Quay garbage collection". ●Support for Red Hat product images that are pushed to the mirror registry for Red Hat OpenShift for bootstrapping purposes are covered by valid subscriptions for each respective product. A list of exceptions to further enable the bootstrap experience can be found on the Self-managed Red Hat OpenShift sizing and subscription guide. ●Content built by customers should not be hosted by the mirror registry for Red Hat OpenShift. ●Using the mirror registry for Red Hat OpenShift with more than one cluster is discouraged because multiple clusters can create a single point of failure when updating your cluster fleet. Instead, use the mirror registry for Red Hat OpenShift to install a cluster that can host a production-grade, highly-available registry such as Red Hat Quay, which can serve OpenShift Container Platform content to other clusters.

**4.2.2.2.3Configuring rootless Podman networking**

To restore rootless Podman networking when the default pasta stack fails on OpenShift Container Platform mirror or install hosts, you can set the default rootless network back to

| slirp4netns | in the | /etc/containers/containers.conf |   |
|---|---|---|---|
| ~/.config/containers/container.conf |   |   | file. |

You might need to configure rootless Podman networking after upgrading to RHEL 9.5 or Podman 5.0. In these versions, the default networking stack changed from slirp4netnsto pasta. As a result, systems that previously operated without a default route might no longer be able to establish network connectivity and could display the following error: Error: pasta failed with exit code 1: External interface not usable

**4.2.2.2.3.1Prerequisites**

●You have updated to RHEL 9.5 or Podman 5.0. Page 35 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**4.2.2.2.3.2Procedure**

1.Use your preferred IDE to modify the /etc/containers/containers.confor

| ~/.config/containers/container.conffile. a. To modify the /etc/containers/containers.conffile, enter the following command: |   |   |
|---|---|---|
| $ nano /etc/containers/containers.conf |   |   |
| b. To modify the | ~/.config/containers/container.conf | file, enter the following |

command:

| $ nano ~/.config/containers/container.conf |   |   |
|---|---|---|
| 2. Add, or update, the | config | [network] section as in the following example: |
| # ... |   |   |
| [network] |   |   |
| default rootless network cmd = "slirp4netns" _ _ _ |   |   |
| # ... |   |   |

3.Restart the Podman system as the rootless user by entering the following command. Note that all containers must be stopped and restarted for the change to take effect. $ podman system migrate

**4.2.2.2.4Mirroring on a local host with mirror registry for Red Hat OpenShift**

This procedure explains how to install the mirror registry for Red Hat OpenShift on a local host by using the mirror-registry installer tool. By doing so, users can create a local host registry running on port 443 for the purpose of storing a mirror of OpenShift Container Platform images.

| ng the | mirror-registry |   |
|---|---|---|
| $HOME/quay-install |   | d |

**Note**: Installing the mirror registry for Red Hat OpenShift using the mirror-registry CLI tool
makes several changes to your machine. After installation, a $HOME/quay-install directory is created, which has installation files, local storage, and the configuration bundle. Trusted SSH keys are generated in case the deployment target is the local host, and systemd files on the host machine are set up to ensure that container runtimes are persistent. Additionally, an initial user named init is created with an automatically generated password. All access credentials are printed at the end of the install routine.

**4.2.2.2.4.1Procedure**

1.Download the mirror-registry.tar.gz package for the latest version of the mirror registry for Red Hat OpenShift found on the OpenShift console Downloads page. 2.Install the mirror registry for Red Hat OpenShift on your local host with your current user account by using the mirror-registry tool. For a full list of available flags, see "mirror registry for Red Hat OpenShift flags". $ ./mirror-registry install \ --quayHostname <host_example_com> \ --quayRoot <example_directory_name> 3.Use the username and password generated during installation to log in to the registry by running the following command: $ podman login -u init \ -p <password> \ Page 36 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| <host example com>:8443> \ _ _ |   |   |
|---|---|---|
| --tls-verify=false |   |   |
| You can avoid running | --tls-verify=false | by configuring your system to trust the generated |

rootCA certificates. See "Securing Red Hat Quay" and "Configuring the system to trust the certificate authority" for more information.
**Note**: You can also log in by accessing the UI at https://<host.example.com>:8443 after
installation. 4.You can mirror OpenShift Container Platform images after logging in. Depending on your needs, see either the "Mirroring the OpenShift Container Platform image repository" or the "Mirroring Operator catalogs for use with disconnected clusters" sections of this document.
**Note**: If there are issues with images stored by the mirror registry for Red Hat
OpenShift due to storage layer problems, you can re-mirror the OpenShift Container Platform images, or reinstall mirror registry on more stable storage.

**Mirroring images for a disconnected installation by using the oc-**

**4.2.2.3**

**mirror plugin v2**

You can run your cluster in a disconnected environment if you install the cluster from a mirrored set of OpenShift Container Platform container images in a private registry. This registry must be running whenever your cluster is running. You can use oc-mirror plugin v2 to mirror images to a mirror registry in your fully or partially disconnected environments. To download the required images from the official Red Hat registries, you must run oc-mirror plugin v2 from a system with internet connectivity.

**4.2.2.3.1About oc-mirror plugin v2**

The oc-mirror OpenShift CLI (oc) plugin is a single tool that mirrors all required OpenShift Container Platform content and other images to your mirror registry. To use the new version of oc-mirror, add the --v2 flag to the oc-mirror plugin v2 command line. oc-mirror plugin v2 has the following features: ●Provides a centralized method to mirror OpenShift Container Platform releases, Operators, helm charts, and other images. ●Verifies that the complete image set specified in the image set configuration file is mirrored to the mirrored registry, regardless of whether the images were previously mirrored or not. ●Uses a cache system instead of metadata, which prevents the need to start the mirroring process over in the case of a failure for a single step of the process. ●Maintains minimal archive sizes by incorporating only new images into the archive. ●Generates mirroring archives with content selected by mirroring date. ●Can generate ImageDigestMirrorSet (IDMS) and ImageTagMirrorSet (ITMS) resources, which cover the full image set, instead of an ImageContentSourcePolicy (ICSP) Page 37 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack resource, which only covered incremental changes to the image set for each mirroring operation with v1. ●Does not perform automatic pruning. v2 now uses a Delete feature, which grants users more control over deleting images. ●Introduces support for registries.conf files. This change facilitates mirroring to multiple enclaves while using the same cache.

**4.2.2.3.1.1High level workflow**

The following steps outline the high-level workflow on how to use the oc-mirror plugin v2 to mirror images to a mirror registry: 1.Create an image set configuration file. 2.Mirror the image set to the target mirror registry by using one of the following workflows: 3.Mirror an image set directly to the target mirror registry (mirror to mirror). 4.Mirror an image set to disk (mirror to disk), transfer the tar file to the target environment, then mirror the image set to the target mirror registry (disk to mirror). 5.Configure your cluster to use the resources generated by the oc-mirror plugin v2. 6.Repeat these steps to update your target mirror registry as necessary.

**4.2.2.3.1.2oc-mirror plugin v2 compatibility and support**

The oc-mirror plugin v2 is supported for OpenShift Container Platform.
**Note**: On aarch64, ppc64le, and s390x architectures the oc-mirror plugin v2 is supported
only for OpenShift Container Platform 4.14 and later. Use the latest available version of the oc-mirror plugin v2 regardless of which versions of OpenShift Container Platform you need to mirror.

**4.2.2.3.2Prerequisites**

●You must have a container image registry that supports Docker V2-2 in the location that hosts the OpenShift Container Platform cluster, such as Red Hat Quay.
**Note**:
●If you use Red Hat Quay, use version 3.6 or later with the oc-mirror plugin. See Deploying the Red Hat Quay Operator on OpenShift Container Platform (Red Hat Quay documentation). If you need additional assistance selecting and installing a registry, contact your sales representative or Red Hat Support. ●If you do not have an existing solution for a container image registry, OpenShift Container Platform subscribers receive a mirror registry for Red Hat OpenShift. This mirror registry is included with your subscription and serves as a small-scale container registry. You can use this registry to mirror the necessary container images of OpenShift Container Platform for disconnected installations. ●Every machine in the provisioned clusters must have access to the mirror registry. If the registry is unreachable, tasks like installation, updating, or routine operations Page 38 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack such as workload relocation, might fail. Mirror registries must be operated in a highly available manner, ensuring their availability aligns with the production availability of your OpenShift Container Platform clusters.

**4.2.2.3.3Preparing your mirror hosts**

To use the oc-mirror plugin v2 for image mirroring, you must install the plugin and create a file with credentials for container images, enabling you to mirror from Red Hat to your mirror.

**4.2.2.3.3.1Installing the oc-mirror OpenShift CLI plugin**

Install the oc-mirror OpenShift CLI plugin to manage image sets in disconnected environments.

**Prerequisites**

●You have installed the OpenShift CLI (oc). If you are mirroring image sets in a fully disconnected environment, ensure the following: ○You have installed the oc-mirror plugin on the host that has internet access. ○The host in the disconnected environment has access to the target mirror registry. ●You have set the umask parameter to 0022 on the operating system that uses ocmirror. ●You have installed the correct binary for the RHEL version that you are using.

**Procedure**

1.Download the oc-mirror CLI plugin: ○Navigate to the Downloads page of the Red Hat Hybrid Cloud Console. ○In the **OpenShift disconnected installation tools** section, select the **OS**
**type** and **Architecture type** of the **OpenShift Client (oc) mirror plugin** from the
dropdown menus. ○Click **Download** to save the file. 2.Extract the archive by running the following command: $ tar xvzf oc-mirror.tar.gz 3.If necessary, update the plugin file to be executable by running the following command: $ chmod +x oc-mirror
**Note**: Do not rename the oc-mirror file.
4.Install the oc-mirror CLI plugin by placing the file in your PATH, for example /usr/local/bin, by running the following command: $ sudo mv oc-mirror /usr/local/bin/.

**Verification**

●Verify that the oc-mirror plugin v2 is successfully installed by running the following command: $ oc-mirror --v2 --help Page 39 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**4.2.2.3.3.2Configuring credentials that allow images to be mirrored**

Create a container image registry credentials file so that you can mirror images from Red Hat to your mirror. Complete the following steps on the installation host.
**Warning**: Do not use this image registry credentials file as the pull secret when you install
a cluster. If you provide this file when you install cluster, all of the machines in the cluster will have write access to your mirror registry.

**Prerequisites**

●You configured a mirror registry to use in your disconnected environment. ●You identified an image repository location on your mirror registry to mirror images into. ●You provisioned a mirror registry account that allows images to be uploaded to that image repository. ●You have write access to the mirror registry.

**Procedure**

1.Download your registry.redhat.io pull secret from Red Hat OpenShift Cluster Manager. 2.Make a copy of your pull secret in JSON format by running the following command: $ cat ./pull-secret | jq . > <path>/<pull_secret_file_in_json> Specify the path to the directory to store the pull secret in and a name for the JSON file that you create.

**Example pull secret**

| { |   |   |
|---|---|---|
| "auths": { |   |   |
| "cloud.openshift.com": { |   |   |
| "auth": "b3BlbnNo...", |   |   |
| "email": "you@example.com" |   |   |
| }, |   |   |
| "quay.io": { |   |   |
| "auth": "b3BlbnNo...", |   |   |
| "email": "you@example.com" |   |   |
| }, |   |   |
| "registry.connect.redhat.com": { |   |   |
| "auth": "NTE3Njg5Nj...", |   |   |
| "email": "you@example.com" |   |   |
| }, |   |   |
| "registry.redhat.io": { |   |   |
| "auth": "NTE3Njg5Nj...", |   |   |
| "email": "you@example.com" |   |   |
| } |   |   |
| } |   |   |
| } |   |   |
| 1. If the | $XDG RUNTIME DIR/containers _ _ | directory does not exist, create one by entering |

the following command:

| $ mkdir -p $XDG RUNTIME DIR/containers _ _ |   |   |
|---|---|---|
| 2. Save the pull secret file as | $XDG RUNTIME DIR/containers/auth.json _ _ | . |

Page 40 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack 3.Generate the base64-encoded user name and password or token for your mirror registry by running the following command:

| $ echo -n '<user name>:<password>' \| base64 -w0 _ |   |   |   |   |
|---|---|---|---|---|
| For | <user name> _ | and | <password> | , specify the user name and password that you |

configured for your registry.

**Example output**

BGVtbYk3ZHAtqXs= 4.Edit the JSON file and add a section that describes your registry to it:

| "auths": { |   |   |
|---|---|---|
| "<mirror registry>": { _ |   |   |
| "auth": "<credentials>", |   |   |
| "email": "you@example.com" |   |   |
| } |   |   |
| }, |   |   |
| ● For the | <mirror registry> _ | value, specify the registry domain name, and optionally the |

port, that your mirror registry uses to serve content. For

| e, | registry.example.com |   |
|---|---|---|
| <credentials> |   | value, sp |

example, registry.example.com or registry.example.com:8443. ●For the <credentials> value, specify the base64-encoded user name and password for the mirror registry.

**Example modified pull secret**

{ "auths": { "registry.example.com": { "auth": "BGVtbYk3ZHAtqXs=", "email": "you@example.com" }, "cloud.openshift.com": { "auth": "b3BlbnNo...", "email": "you@example.com" }, "quay.io": { "auth": "b3BlbnNo...", "email": "you@example.com" }, "registry.connect.redhat.com": { "auth": "NTE3Njg5Nj...", "email": "you@example.com" }, "registry.redhat.io": { "auth": "NTE3Njg5Nj...", "email": "you@example.com" } } } Page 41 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**4.2.2.3.4Mirroring an image set to a mirror registry**

Mirroring an image set to a mirror registry ensures that the required images are available in a secure and controlled environment, facilitating smoother deployments, updates, and maintenance tasks.

**4.2.2.3.4.1Creating the image set configuration**

Before you can use the oc-mirror plugin v2 to mirror images, you must create an image set configuration file. This image set configuration file defines which OpenShift Container Platform releases, Operators, and other images to mirror, along with other configuration settings for the oc-mirror plugin v2.

**Prerequisites**

●You have created a container image registry credentials file. For instructions, see Configuring credentials that allow images to be mirrored.

**Procedure**

●Create an ImageSetConfiguration YAML file and modify it to include your required images.

| Example | ImageSetConfiguration | YAML file |
|---|---|---|
| kind: ImageSetConfiguration |   |   |
| apiVersion: mirror.openshift.io/v2alpha1 |   |   |
| mirror: |   |   |
| platform: |   |   |
| channels: |   |   |
| - name: stable-4.18 |   |   |
| minVersion: 4.18.2 |   |   |
| maxVersion: 4.18.2 |   |   |
| graph: true |   |   |
| operators: |   |   |
| - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.18 |   |   |
| packages: |   |   |
| - name: aws-load-balancer-operator |   |   |
| - name: 3scale-operator |   |   |
| - name: node-observability-operator |   |   |
| additionalImages: |   |   |
| - name: registry.redhat.io/ubi8/ubi:latest |   |   |
| - name: |   |   |
| registry.redhat.io/ubi9/ubi@sha256:20f695d2a91352d4eaa25107535126727b5945bff38ed36a3e59590f4 |   |   |
| 95046f0 |   |   |

1.Set the channel to retrieve OpenShift Container Platform images from. 2.Add graph: true to build and push the graph-data image to the mirror registry. The graph-data image is required to create OpenShift Update Service (OSUS). The graph:

| true | fie |
|---|---|
| The | oc |

true field also generates the UpdateService custom resource manifest. The oc command-line interface (CLI) can use the UpdateService custom resource manifest to create OSUS. For more information, see About the OpenShift Update Service. Page 42 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack 3.Set the Operator catalog to retrieve the OpenShift Container Platform images from. 4.Specify only certain Operator packages to include in the image set. Remove this field to retrieve all packages in the catalog. 5.Specify any additional images to include in image set.
**Note**: In oc-mirror plugin v2, you must use explicit registry hostnames for all images listed
under additionalImages. Otherwise, images are mirrored to incorrect target paths.

**4.2.2.3.4.2Comparison of oc-mirror workflows**

Use the following table to compare the supported use cases for the mirror-to-disk (m2d), disk-to-mirror (d2m), and mirror-to-mirror (m2m) workflows.

| Use Case | Mirror To Disk (m2d) and Disk To Mirror (d2m) | Mirror To Mirror (m2m) |
|---|---|---|
| The target registry exists in an environment with no internet access and no external access. | ✓ |   |
| The target registry exists in an environment with no internet access but is accessible from another machine. For example, the target registry resides in a bastion host. |   | ✓ |
| You must move content to the disconnected environment by using a physical method, such as USB devices. | ✓ |   |
| The workflow moves content directly to the target registry without generating an intermediate tar file. |   | ✓ |
| The workflow uses an internal cache to resume after failures but requires additional disk space. | ✓ |   |
| The workflow does not use a cache, restarts from the beginning after a failure, and requires no additional disk space. |   | ✓ |

**4.2.2.3.4.3Mirroring an image set in a partially disconnected environment**

You can mirror image sets to a registry using the oc-mirror plugin v2 in environments with restricted internet access.

**Prerequisites**

●You have access to the internet and the mirror registry in the environment where you are running the oc-mirror plugin v2.

**Procedure**

●Mirror the images from the specified image set configuration to a specified registry by running the following command: $ oc-mirror -c <image_set_configuration> --workspace file://<file_path> docker://<mirror_registry_url> --v2 where:
**<image_set_configuration>** : Specifies the name of the image set configuration file.
Page 43 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
**<file_path>** : Specifies the directory where cluster resources will be generated in.
**<mirror_registry_url>** : Specifies the URL or address of the mirror registry where the
images are stored and from which they need to be deleted.

**Verification**

1.Navigate to the working-dir/cluster-resources directory that was generated in the <file_path> directory. 2.Verify that the YAML files are present for the ImageDigestMirrorSet, ImageTagMirrorSet, and CatalogSource resources.

**Next steps**

●Configure your cluster to use the resources generated by oc-mirror plugin v2.

**4.2.2.3.4.4Mirroring an image set in a fully disconnected environment**

You can mirror image sets in a fully disconnected environment where the OpenShift Container Platform cluster cannot access the public internet. The following high-level workflow describes the mirroring process: 1.**Mirror to disk**: Mirror the image set to an archive. 2.**Disk transfer**: Manually transfer the archive to the network of the disconnected mirror registry. 3.**Disk to mirror**: Mirror the image set from the archive to the target disconnected registry.

**Mirroring from mirror to disk**

You can use the oc-mirror plugin v2 to generate an image set and save the content to disk. Afterwards, you can transfer the generated image set to the disconnected environment and mirror it to the target registry. oc-mirror plugin v2 retrieves the container images from the source specified in the image set configuration file and packs them into a tar archive in a local directory.

**Procedure**

●Mirror the images from the specified image set configuration to the disk by running the following command: $ oc-mirror -c <image_set_configuration> file://<file_path> --v2 where:
**<image_set_configuration>** : Specifies the name of the image set configuration file.
**<file_path>** : Specifies the directory where the archives containing the image sets will be
generated in.

**Verification**

1.Navigate to the <file_path> directory that was generated. 2.Verify that the archive files have been generated.

**Next steps**

●Mirroring from disk to mirror

**Mirroring from disk to mirror**

You can use the oc-mirror plugin v2 to mirror image sets from a disk to a target mirror registry. Page 44 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack The oc-mirror plugin v2 retrieves container images from a local disk and transfers them to the specified mirror registry.

**Procedure**

1.Transfer the disk containing mirrored image sets to the environment that contains the target mirror registry. 2.Process the image set file on the disk and mirror the contents to a target mirror registry by running the following command: $ oc-mirror -c <image_set_configuration> --from file://<file_path> docker://<mirror_registry_url> --v2 where:
**<image_set_configuration>** : Specifies the name of the image set configuration file.
**<file_path>** : Specifies the directory on the disk containing the archives. This folder will
also contain cluster resources generated for you apply to the cluster, for example the ImageDigestMirrorSet (IDMS) or ImageTagMirrorSet (ITMS) resources.
**<mirror_registry_url>** : Specifies the URL or address of the mirror registry where the
images are stored.

**Verification**

| cluster-resources |   |   |
|---|---|---|
|   | <file path> _ | dire |

1.Navigate to the cluster-resources directory within the working-dir directory that was 2.Verify that the YAML files are present for the ImageDigestMirrorSet, ImageTagMirrorSet, and CatalogSource resources.

**Next steps**

●Starting your cluster installation or configure your cluster to use the resources generated by oc-mirror plugin v2.

**4.2.2.3.5About custom resources generated by oc-mirror plugin v2**

The oc-mirror plugin v2 automatically generates the following custom resources:

**ImageDigestMirrorSet (IDMS)**

Handles registry mirror rules when using image digest pull specifications. Generated if at least one image of the image set is mirrored by digest.

**ImageTagMirrorSet (ITMS)**

Handles registry mirror rules when using image tag pull specifications. Generated if at least one image from the image set is mirrored by tag.

**CatalogSource**

Retrieves information about the available Operators in the mirror registry. Used by Operator Lifecycle Manager (OLM) Classic.

**ClusterCatalog**

Retrieves information about the available cluster extensions (which includes Operators) in the mirror registry. Used by OLM v1.

**UpdateService**

Provides update graph data to the disconnected environment. Used by the OpenShift Update Service. Page 45 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**4.2.2.3.5.1Restrictions on modifying resources that are generated by the oc-mirror**

**plugin**

When using resources that are generated by the oc-mirror plugin v2 to configure your cluster, you must not change certain fields. Modifying these fields can cause errors and is not supported. The following table lists the resources and their fields that must remain unchanged:

| Resource |   |   |   |   |   | Fields that must not be changed |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CatalogSource |   |   |   |   |   | apiVersion | , | kind | , | spec.image |   |   |   |   |   |
| ClusterCatalog |   |   |   |   |   | apiVersion | , | kind | , | spec.source.image.ref |   |   |   |   |   |
| ImageDigestMirrorSet |   |   |   |   |   | apiVersion | , | kind | , | spec.imageDigestMirrors |   |   |   |   |   |
| ImageTagMirrorSet |   |   |   |   |   | apiVersion | , | kind | , | spec.imageTagMirrors |   |   |   |   |   |
| Signature | ConfigMap |   |   |   |   | apiVersion | , | kind | , | metadata.namespace, |   | binaryData |   |   |   |
| UpdateService |   |   |   |   |   | apiVersion | , | kind | , | spec.graphDataImage |   | , spec.releases |   |   |   |

For more information about these resources, see the OpenShift API documentation for CatalogSource, ImageDigestMirrorSet, and ImageTagMirrorSet.

**4.2.2.3.6Verifying your selected images for mirroring**

You can use oc-mirror plugin v2 to perform a test run (dry run) that does not actually mirror any images. This enables you to review the list of images that would be mirrored. You can also use a dry run to catch any errors with your image set configuration early. When running a dry run on a mirror-to-disk workflow, the oc-mirror plugin v2 checks if all the images within the image set are available in its cache. Any missing images are listed in

| missing.txt |   | f |
|---|---|---|
| h | missing.txt |   |

the missing.txt file. When a dry run is performed before mirroring, both missing.txt and mapping.txt files contain the same list of images.

**4.2.2.3.6.1Performing a dry run for oc-mirror plugin v2**

Verify your image set configuration by performing a dry run without mirroring any images. This ensures your setup is correct and prevents unintended changes.

**Procedure**

●To perform a test run, run the oc mirror command and append the --dry-

|   | run | argument to the command: |
|---|---|---|
| $ oc-mirror -c <image set config yaml> file://<oc mirror workspace path> --dry-run --v2 _ _ _ _ _ _ |   |   |

where:

| <image set config yaml> _ _ _ |   | : Sp |
|---|---|---|
| <oc mirror workspace path> _ _ _ |   |   |
| <mirror registry url> _ _ | : Insert t |   |

<image_set_config_yaml>: Specifies the image set configuration file that you created. <oc_mirror_workspace_path> : Insert the address of the workspace path. <mirror_registry_url> : Insert the URL or address of the remote container registry from which images will be mirrored or deleted.

**Example output**

[INFO] : :wave: Hello, welcome to oc-mirror [INFO] : :gear: setting up the environment for you... [INFO] : :twisted_rightwards_arrows: workflow mode: mirrorToDisk [INFO] : :sleuth_or_spy: going to discover the necessary images... Page 46 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack [INFO] : :mag: collecting release images... [INFO] : :mag: collecting operator images... [INFO] : :mag: collecting additional images... [WARN] : :warning: 54/54 images necessary for mirroring are not available in the cache. [WARN] : List of missing images in : CLID-19/working-dir/dry-run/missing.txt. please re-run the mirror to disk process [INFO] : :page_facing_up: list of all images for mirroring in : CLID-19/working-dir/dryrun/mapping.txt [INFO] : mirror time : 9.641091076s [INFO] : :wave: Goodbye, thank you for using oc-mirror

**Verification**

1.Navigate to the workspace directory that was generated:

| $ cd <oc mirror workspace path> _ _ _ |   |   |   |   |
|---|---|---|---|---|
| 2. Review the | mapping.txt | and | missing.txt | files that were generated. These files contain a |

list of all images that would be mirrored.

**4.2.2.3.6.2Troubleshooting oc-mirror plugin v2 errors**

oc-mirror plugin v2 now logs all image mirroring errors in a separate file, making it easier to track and diagnose failures.

**Important**

●When errors occur while mirroring release or release component images, they are critical. This stops the mirroring process immediately. ●Errors with mirroring Operators, Operator-related images, or additional images do not stop the mirroring process. Mirroring continues, and oc-mirror plugin v2 saves a file under the working-dir/logs directory describing which Operator failed to mirror. When an image fails to mirror, and that image is mirrored as part of one or more Operator bundles, oc-mirror plugin v2 notifies the user which Operators are incomplete, providing clarity on the Operator bundles affected by the error.

**Procedure**

1.Check for server-related issues:

**Example error**

| [ERROR] : [Worker] error mirroring image localhost:55000/openshift/graph-image:latest error: copying |   |   |   |   |
|---|---|---|---|---|
| image 1/4 from manifest list: trying to reuse blob |   |   |   |   |
| sha256:edab65b863aead24e3ed77cea194b6562143049a9307cd48f86b542db9eecb6e at destination: |   |   |   |   |
| pinging container registry localhost:5000: Get "https://localhost:5000/v2/": http: server gave HTTP |   |   |   |   |
| response to HTTPS client |   |   |   |   |
| a. Open the | mirroring error date time.log _ _ _ | file in the | working-dir/logs | folder located in |

the oc-mirror plugin v2 output directory. b.Look for error messages that typically indicate server-side issues, such as HTTP 500 errors, expired tokens, or timeouts. c. Retry the mirroring process or contact support if the issue persists. 2.Check for incomplete mirroring of Operators: Page 47 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Example error**

error mirroring image docker://registry.redhat.io/3scale-amp2/zyncrhel9@sha256:8bb6b31e108d67476cc62622f20ff8db34efae5d58014de9502336fcc479d86d (Operator bundles: [3scale-operator.v0.11.12] - Operators: [3scale-operator]) error: initializing source docker://localhost:55000/3scale-amp2/zyncrhel9:8bb6b31e108d67476cc62622f20ff8db34efae5d58014de9502336fcc479d86d: reading manifest 8bb6b31e108d67476cc62622f20ff8db34efae5d58014de9502336fcc479d86d in localhost:55000/3scaleamp2/zync-rhel9: manifest unknown error mirroring image docker://registry.redhat.io/3scale-amp2/3scale-rhel7-operatormetadata@sha256:de0a70d1263a6a596d28bf376158056631afd0b6159865008a7263a8e9bf0c7d error: skipping operator bundle docker://registry.redhat.io/3scale-amp2/3scale-rhel7-operatormetadata@sha256:de0a70d1263a6a596d28bf376158056631afd0b6159865008a7263a8e9bf0c7d because one of its related images failed to mirror error mirroring image docker://registry.redhat.io/3scale-amp2/systemrhel7@sha256:fe77272021867cc6b6d5d0c9bd06c99d4024ad53f1ab94ec0ab69d0fda74588e (Operator bundles: [3scale-operator.v0.11.12] - Operators: [3scale-operator]) error: initializing source docker://localhost:55000/3scale-amp2/systemrhel7:fe77272021867cc6b6d5d0c9bd06c99d4024ad53f1ab94ec0ab69d0fda74588e: reading manifest fe77272021867cc6b6d5d0c9bd06c99d4024ad53f1ab94ec0ab69d0fda74588e in localhost:55000/3scaleamp2/system-rhel7: manifest unknown a.Check for warnings in the console or log file indicating which Operators are incomplete. If an Operator is flagged as incomplete, the image related to that Operator likely failed to mirror. b.Manually mirror the missing image or retry the mirroring process. 3.Check for errors related to generated cluster resources. Even if some images fail to mirror, oc-mirror v2 will still generate cluster resources such as IDMS.yaml and ITMS.yaml files for the successfully mirrored images. a.Check the output directory for the generated files. b.If these files are missing for specific images, ensure that no critical errors occurred for those images during the mirroring process.
**Note**:
●if you meet the download disconnection, you can try HTTP/1.1 degradation parameter anti-disconnection by using GODEBUG=http2client=0 in front of the oc-mirror command. ●For more details or no mentioned about the disconnected environments preparation, your can reference the Red Hat official documentation here.

## 5 Installation using agent-based installer

The following procedures deploy a 6 nodes OpenShift Container Platform in online environment. You can use these procedures as a basis and modify according to your requirements. Page 48 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Downloading the Agent-based Installer**

**5.1.1**

Use this procedure to download the Agent-based Installer and the CLI needed for your installation.

**Procedure**

**5.1.1.1**

1.Log in to the Red Hat Hybrid Cloud Console using your login credentials. 2.Navigate to Datacenter. 3.Click **Run Agent-based Installer locally**. 4.Select the operating system and architecture for the **OpenShift Installer** and
**Command line interface**.
5.Click **Download Installer** to download and extract the install program. 6.Download or copy the pull secret by clicking on **Download pull secret** or **Copy pull**
**secret**.
7.Click **Download command-line tools** and place the openshift-install binary in a directory that is on your PATH.

**Verifying the supported architecture for an Agent-based**

**5.1.2**

**installation**

Before installing an OpenShift Container Platform cluster using the Agent-based Installer, you can verify the supported architecture on which you can install the cluster. This procedure is optional.

**Prerequisites**

**5.1.2.1**

●You installed the OpenShift CLI (oc). ●You have downloaded the installation program.

**Procedure**

**5.1.2.2**

1.Log in to the OpenShift CLI (oc). 2.Check your release payload by running the following command: $ ./openshift-install 4.18.0 built from commit abc123def456 release image quay.io/openshift-release-dev/ocprelease@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0 release architecture amd64 If you are using the release image with the multi payload, the release architecture displayed in the output of this command is the default architecture. 3.To check the architecture of the payload, run the following command: Page 49 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| $ oc adm release info <release image> -o jsonpath="{ .metadata.metadata}" _ |   |   |   |
|---|---|---|---|
| {"release.openshift.io architecture":"multi"} |   |   |   |
| Replace | <release image> _ | with the release image. For example: | quay.io/openshift-release- |
| dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0 |   |   |   |

If you are using the release image with the multi payload, you can install the cluster on

| amd64 | , | s390x |
|---|---|---|

install the cluster only on the release architecture displayed in the output of the openshiftinstall version command.

**5.1.3**

**Creating the preferred configuration inputs**

Use this procedure to create the preferred configuration inputs used to create the agent image. Configuring the install-config.yaml and agent-config.yaml files is the preferred method for using the Agent-based Installer.

**Procedure**

**5.1.3.1**

| 1. Install the | nmstate | dependency by running the following command: |   |
|---|---|---|---|
| $ sudo dnf install /usr/bin/nmstatectl -y |   |   |   |
| 2. Place the | openshift-install |   | binary in a directory that is on your PATH. |

3.Create a directory to store the install configuration by running the following command:

| $ mkdir ~/<directory name> _ |   |   |   |   |
|---|---|---|---|---|
| 4. Copy the | install-config.yaml | and | agent-config.yaml | files to the directory. |

**5.1.4**

**Creating and boot the agent image**

Use this procedure to boot the agent image on your machines.

**Procedure**

**5.1.4.1**

1.Create the agent image by running the following command: $ openshift-install --dir <install_directory> agent create image Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a

| lt | /etc/multipath.conf |   |   | configuration |
|---|---|---|---|---|
| agent.x86 64.iso _ |   | , | agent.aarch64.iso |   |

The agent.x86_64.iso, agent.aarch64.iso, or agent.s390x.iso image will be created. 2.Converting the ISO to qcow2 file. ECS on Apsara Stack doesn't support ISO booting, so we have to convert the image into a qcow2 file. $ qemu-img convert -f raw -O qcow2 agent.x86_64.iso agent.x86_64.qcow2 3.Upload this qcow2 to Alibaba OSS storage and import it as a ECS image. Page 50 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Import the image to "ECS images": Check imported image: Page 51 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack 4.boot the agent image on your machines. In Chapter 4.1.5, ECS instances for master and worker nodes are created with random images. Now they need to be replaced with the new imported images. Make sure the master nodes and worker nodes are shutdown. Navigate to "ECS instances" page and find menu as below: Page 52 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack In "New Configuration", select "Custom image" and select the imported image: Page 53 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Submit the configuration and start the ECS instances. Now they will boot up using the CoreOS image. Page 54 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**5.1.5**

**Verifying that the current installation host can pull release images**

After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images. If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the Additional checks section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds. If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations. If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed.

**Procedure**

**5.1.5.1**

1.Wait for the agent console application to check whether or not the configured release image can be pulled from a registry. 2.If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation. You can still choose to view or change network configuration settings even if the connectivity checks have passed. Page 55 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation. 3.If the agent console application checks have failed, which is indicated by a red icon beside the Release image URL pull check, use the following steps to reconfigure the host’s network settings: a.Read the Check Errors section of the TUI. This section displays error messages specific to the failed checks. b.Select Configure network to launch the NetworkManager TUI. c. Select Edit a connection and select the connection you want to reconfigure. d.Edit the configuration and select OK to save your changes. e.Select Back to return to the main screen of the NetworkManager TUI. f. Select Activate a Connection. g.Select the reconfigured network to deactivate it. h.Select the reconfigured network again to reactivate it. i. Select Back and then select Quit to return to the agent console application. j. Wait at least five seconds for the continuous network checks to restart using the new network configuration. k.If the Release image URL pull check succeeds and displays a green icon beside the URL, select Quit to exit the agent console application and continue with the installation.

**5.1.6**

**Tracking and verifying installation progress**

Use the following procedure to track installation progress and to verify a successful installation. Page 56 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Prerequisites**

**5.1.6.1**

You have configured a DNS record for the Kubernetes API server.

**Procedure**

**5.1.6.2**

1.Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command:

| $ ./openshift-install --dir <install directory> agent wait-for bootstrap-complete \ _ |   |   |
|---|---|---|
| --log-level=info |   |   |
| ................................................................... |   |   |
| ................................................................... |   |   |
| INFO Bootstrap configMap status is complete |   |   |
| INFO cluster bootstrap is complete |   |   |
| For | <install directory> _ | , specify the path to the directory where the agent ISO was |

generated. To view different installation details, specify warn, debug, or error instead of info. The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines. 2.Monitor the progress of the installation operation and perform necessary manual operations. The ECS system disk was booted by an agent image and the cluster node system was located on a data disk. But the ECS virtual machine currently does not support pointing the boot disk to the data disk. We need to perform some manual operations during the node restart to enable the system on the data disk to be bootable. A relatively convenient approach is to quickly clone the data disk to the system disk ( same size ) before the system restarts and the disk is not mounted. This will enable the ECS to still boot using the system disk, but the system will now be a ready RHCOS system. As a result, this node also achieved the automatic restart without the need for manual intervention during the Day2 operation. When the node restarts, you can press 'E' in the TUI interface to enter the GRUB configuration. If you accidentally miss the guiding interface as shown in the following picture, you can click the square icon in the upper left corner and select CTRL+ALT+DELETE to restart the node. Page 57 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Once you press 'E' in the TUI interface to enter the GRUB configuration, you can add rd.break=pre-mount to the boot configuration as shown in the following screenshot. Page 58 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Page 59 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Press F10 or Ctrl-x to initiate the system. The startup process will be interrupted before the disks are mounted. Page 60 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Execute the following command to clone vdb to vda, and then clean vdb. You don't have to write the command by hand. You can use the button on the upper right corner to copy and paste the command and then execute it. dd if=/dev/vdb of=/dev/vda bs=$((512 * 32)) count=$((16777182 / 32 + 1)) status=progress wipefs -a /dev/vdb Page 61 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Page 62 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Finally, enter the reboot command, and the node will restart and boot using the RHCOS on the system disk. 3.To track the progress and verify successful installation, run the following command: $ openshift-install --dir <install_directory> agent wait-for install-complete ................................................................... ................................................................... INFO Cluster is installed INFO Install complete! INFO To access the cluster as the system:admin user when using 'oc', run INFO export KUBECONFIG=/home/core/installer/auth/kubeconfig INFO Access the OpenShift web-console here: https://console-openshift-console.apps.snocluster.test.example.com For <install_directory> directory, specify the path to the directory where the agent ISO was generated. Page 63 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

## 6 Optional Steps

### 6.1 Log into Openshift cluster via CLI

To log into the OpenShift cluster via CLI, locate the OCPHelper instance. This instance is pre-installed with the command line terminal and login configuration, allowing direct access to the cluster using oc. The cluster kubeconfig is configured as an environment variable. Operations can be performed as the system:admin user. Execute the oc get co command to verify the cluster operators and the oc get nodes command to check the cluster nodes. Page 64 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 6.2 Log into Openshift web console

You can access the OpenShift web console through the Bastionhost's browser. Navigate to https://console-openshift-console.apps.ocptest.apsara and enter the username and password to log in. You will then see the OpenShift console Overview page and can manage the cluster through the web console.

### 6.3 Monitor cluster

You can view the overall cluster monitoring information through the dashboards in Observe, including usage statistics for resources such as CPU, memory, and network. Page 65 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Navigate to Metrics and perform queries to view the relevant metrics of the current cluster. Navigate to Alerting to view alerts and configure alerting rules as needed. To ensure timely alert notifications, navigate to Cluster Settings and configure alert receivers including PagerDuty, Webhook, Email, and Slack. Page 66 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 6.4 Manage cluster

Navigate to Cluster Settings to view and manage the cluster operators and configuration. Navigate to User Management to access and manage users, groups, service accounts, and role bindings. Navigate to Workloads to access and manage pods, deployments and other workload resources. Page 67 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

## 7 OpenShift updates

### 7.1 Introduction to OpenShift updates

With OpenShift Container Platform 4, you can update an OpenShift Container Platform cluster with a single operation by using the web console or the OpenShift CLI (oc). Platform administrators can view new update options either by going to **Administration** → **Cluster Settings** in the web console or by looking at the output of the oc adm upgrade command.

**Cluster update overview**

**7.1.1**

OpenShift Container Platform updates involve several services, Operators, and processes working in tandem to change the cluster to the desired version. Red Hat hosts a public OpenShift Update Service (OSUS), which serves a graph of update possibilities based on the OpenShift Container Platform release images in the official registry. The graph contains update information for any public release. OpenShift Container Platform clusters are configured to connect to the OSUS by default, and the OSUS responds to clusters with information about known update targets. An update begins when either a cluster administrator or an automatic update controller edits the custom resource (CR) of the Cluster Version Operator (CVO) with a new version. To reconcile the cluster with the newly specified version, the CVO retrieves the target release image from an image registry and begins to apply changes to the cluster.
**Note** : Operators previously installed through Operator Lifecycle Manager (OLM) follow a
different process for updates. See Updating installed Operators for more information. The target release image contains manifest files for all cluster components that form a specific OCP version. When updating the cluster to a new version, the CVO applies manifests in separate stages called Runlevels. Most, but not all, manifests support one of the cluster Operators. As the CVO applies a manifest to a cluster Operator, the Operator might perform update tasks to reconcile itself with its new specified version. Page 68 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack The CVO monitors the state of each applied resource and the states reported by all cluster Operators. The CVO only proceeds with the update when all manifests and cluster Operators in the active Runlevel reach a stable condition. After the CVO updates the entire control plane through this process, the Machine Config Operator (MCO) updates the operating system and configuration of every node in the cluster.

**Common questions about update availability**

**7.1.2**

There are several factors that affect if and when an update is made available to an OpenShift Container Platform cluster. The following list provides common questions regarding the availability of an update:

**What are the differences between each of the update channels?**

| candidate |   | channe |
|---|---|---|
| on the | candidate |   |

●A new release is initially added to the candidate channel. the fast channel, an errata is published, and the release is now fully supported.

|   | stable |
|---|---|
| stable |   |

●After a delay, a release on the fast channel is finally promoted to the stable channel. This delay represents the only difference between the fast and stable channels.
**Note**: For the latest z-stream releases, this delay may generally be a week or two.
However, the delay for initial updates to the latest minor version may take much longer, generally 45-90 days. ●Releases promoted to the stable channel are simultaneously promoted to the eus channel. The primary purpose of the eus channel is to serve as a convenience for clusters performing a Control Plane Only update.

**Is a release on the stable channel safer or more supported than a release on**

**the fast channel?**

●If a regression is identified for a release on a fast channel, it will be resolved and managed to the same extent as if that regression was identified for a release on the stable channel.

| stable | cha |
|---|---|
| n the | fast |

●The only difference between releases on the fast and stable channels is that a release only appears on the stable channel after it has been on the fast channel for some time, which provides more time for new update risks to be discovered. ●A release that is available on the fast channel always becomes available on the stable channel after this delay.

**What does it mean if an update has known issues?**

●Red Hat continuously evaluates data from multiple sources to determine whether updates from one version to another have any declared issues. Identified issues are typically documented in the version’s release notes. Even if the update path has known issues, customers are still supported if they perform the update. ●Red Hat does not block users from updating to a certain version. Red Hat may declare conditional update risks, which may or may not apply to a particular cluster. ○Declared risks provide cluster administrators more context about a supported update. Cluster administrators can still accept the risk and update to that particular target version. Page 69 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**What if I see that an update to a particular release is no longer recommended?**

●If Red Hat removes update recommendations from any supported release due to a regression, a superseding update recommendation will be provided to a future version that corrects the regression. There may be a delay while the defect is corrected, tested, and promoted to your selected channel.

**How long until the next z-stream release is made available on the fast and stable**

**channels?**

●While the specific cadence can vary based on a number of factors, new z-stream releases for the latest minor version are typically made available about every week. Older minor versions, which have become more stable over time, may take much longer for new z-stream releases to be made available.
**Important**: These are only estimates based on past data about z-stream releases. Red Hat
reserves the right to change the release frequency as needed. Any number of issues could cause irregularities and delays in this release cadence. ●Once a z-stream release is published, it also appears in the fast channel for that minor version. After a delay, the z-stream release may then appear in that minor version’s stable channel.

**About the OpenShift Update Service**

**7.1.3**

The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform, including Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the vertices of component Operators and the edges that connect them. The edges in the graph show which versions you can safely update to. The vertices are update payloads that specify the intended state of the managed cluster components. The Cluster Version Operator (CVO) in your cluster checks with the OpenShift Update Service to see the valid updates and update paths based on current component versions and information in the graph. When you request an update, the CVO uses the corresponding release image to update your cluster. The release artifacts are hosted in Quay as container images. To allow the OpenShift Update Service to provide only compatible updates, a release verification pipeline drives automation. Each release artifact is verified for compatibility with supported cloud platforms and system architectures, as well as other component packages. After the pipeline confirms the suitability of a release, the OpenShift Update Service notifies you that it is available. The OpenShift Update Service (OSUS) supports a single-stream release model, where only one release version is active and supported at any given time. When a new release is deployed, it fully replaces the previous release. The updated release provides support for upgrades from all OpenShift Container Platform versions starting after 4.8 up to the new release version.
**Important** : The OpenShift Update Service displays all recommended updates for your
current cluster. If an update path is not recommended by the OpenShift Update Service, it Page 70 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack might be because of a known issue related to the update path, such as incompatibility or availability. Two controllers run during continuous update mode. The first controller continuously updates the payload manifests, applies the manifests to the cluster, and outputs the controlled rollout status of the Operators to indicate whether they are available, upgrading, or failed. The second controller polls the OpenShift Update Service to determine if updates are available.
**Important** : Only updating to a newer version is supported. Reverting or rolling back your
cluster to a previous version is not supported. If your update fails, contact Red Hat support. During the update process, the Machine Config Operator (MCO) applies the new configuration to your cluster machines. The MCO cordons the number of nodes specified by the maxUnavailable field on the machine configuration pool and marks them unavailable. By default, this value is set to 1. The MCO updates the affected nodes alphabetically by zone, based on the topology.kubernetes.io/zone label. If a zone has more than one node, the oldest nodes are updated first. For nodes that do not use zones, such as in bare metal deployments, the nodes are updated by age, with the oldest nodes updated first. The MCO updates the number of nodes as specified by the maxUnavailable field on the machine configuration pool at a time. The MCO then applies the new configuration and reboots the machine.
**Warning** : The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool. If you use Red Hat Enterprise Linux (RHEL) machines as workers, the MCO does not update the kubelet because you must update the OpenShift API on the machines first. With the specification for the new version applied to the old kubelet, the RHEL machine cannot return to the Ready state. You cannot complete the update until the machines are available. However, the maximum number of unavailable nodes is set to ensure that normal cluster operations can continue with that number of machines out of service. The OpenShift Update Service is composed of an Operator and one or more application instances.

**Understanding cluster Operator condition types**

**7.1.4**

The status of cluster Operators includes their condition type, which informs you of the current state of your Operator’s health. The following definitions cover a list of some common ClusterOperator condition types. Operators that have additional condition types and use Operator-specific language have been omitted. The Cluster Version Operator (CVO) is responsible for collecting the status conditions from cluster Operators so that cluster administrators can better understand the state of the OpenShift Container Platform cluster. Page 71 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Available: The condition type Available indicates that an Operator is functional and available in the cluster. If the status is False, at least one part of the operand is nonfunctional and the condition requires an administrator to intervene. ●Progressing: The condition type Progressing indicates that an Operator is actively rolling out new code, propagating configuration changes, or otherwise moving from one steady state to another. Operators do not report the condition type Progressing as True when they are reconciling a previous known state. If the observed cluster state has changed and the Operator is reacting to it, then the status reports back as True, since it is moving from one steady state to another. ●Degraded: The condition type Degraded indicates that an Operator has a current state that does not match its required state over a period of time. The period of time can vary by component, but a Degraded status represents persistent observation of an Operator’s condition. As a result, an Operator does not fluctuate in and out of the Degraded state. There might be a different condition type if the transition from one state to another does not persist over a long enough period to report Degraded. An Operator does not report Degraded during the course of a normal update. An Operator may report Degraded in response to a persistent infrastructure failure that requires eventual administrator intervention.
**Note**: This condition type is only an indication that something may need investigation and
adjustment. As long as the Operator is available, the Degraded condition does not cause user workload failure or application downtime. ●Upgradeable: The condition type Upgradeable indicates whether the Operator is safe to update based on the current cluster state. The message field contains a humanreadable description of what the administrator needs to do for the cluster to successfully update. The CVO allows updates when this condition is True, Unknown or missing. When the Upgradeable status is False, only minor updates are impacted, and the CVO prevents the cluster from performing impacted updates unless forced.

**Understanding cluster version condition types**

**7.1.5**

The Cluster Version Operator (CVO) monitors cluster Operators and other components, and is responsible for collecting the status of both the cluster version and its Operators. This status includes the condition type, which informs you of the health and current state of the OpenShift Container Platform cluster. In addition to Available, Progressing, and Upgradeable, there are condition types that affect cluster versions and Operators. ●Failing: The cluster version condition type Failing indicates that a cluster cannot reach its desired state, is unhealthy, and requires an administrator to intervene. Page 72 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Invalid: The cluster version condition type Invalid indicates that the cluster version has an error that prevents the server from taking action. The CVO only reconciles the current state as long as this condition is set. ●RetrievedUpdates: The cluster version condition type RetrievedUpdates indicates whether or not available updates have been retrieved from the upstream update

| val, | False | if the u |
|---|---|---|
| availableUpdates |   |   |

server. The condition is Unknown before retrieval, False if the updates either recently failed or could not be retrieved, or True if the availableUpdates field is both recent and accurate. ●ReleaseAccepted: The cluster version condition type ReleaseAccepted with a True status indicates that the requested release payload was successfully loaded without failure during image verification and precondition checking. ●ImplicitlyEnabledCapabilities: The cluster version condition type ImplicitlyEnabledCapabilities with a True status indicates that there are enabled capabilities that the user is not currently requesting through spec.capabilities. The CVO does not support disabling capabilities if any associated resources were previously managed by the CVO.

**Common terms**

**7.1.6**

Some terms are commonly used in the context of OpenShift Container Platform updates, which might be useful to learn.

**Control plane**

The control plane, which is composed of control plane machines, manages the OpenShift Container Platform cluster. The control plane machines manage workloads on the compute machines, which are also known as worker machines.

**Cluster Version Operator**

The Cluster Version Operator (CVO) starts the update process for the cluster. It checks with OSUS based on the current cluster version and retrieves the graph which contains available or possible update paths.

**Machine Config Operator**

The Machine Config Operator (MCO) is a cluster-level Operator that manages the operating system and machine configurations. Through the MCO, platform administrators can configure and update systemd, CRI-O and Kubelet, the kernel, NetworkManager, and other system features on the worker nodes.

**OpenShift Update Service**

The OpenShift Update Service (OSUS) provides over-the-air updates to OpenShift Container Platform, including to Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the vertices of component Operators and the edges that connect them.

**Channels**

Channels declare an update strategy tied to minor versions of OpenShift Container Platform. The OSUS uses this configured strategy to recommend update edges consistent with that strategy. Page 73 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Recommended update edge**

A recommended update edge is a recommended update between OpenShift Container Platform releases. Whether a given update is recommended can depend on the cluster’s configured channel, current version, known bugs, and other information. OSUS communicates the recommended edges to the CVO, which runs in every cluster.

### 7.2 How cluster updates work

The Cluster Version Operator (CVO) is the primary component that orchestrates the OpenShift Container Platform update process. During standard cluster operation, the CVO compares manifests of cluster Operators to in-cluster resources and reconciles discrepancies between the actual state of these resources and their desired state. The following sections describe each major aspect of the OpenShift Container Platform (OCP) update process in detail. For a general overview of how updates work, see the Introduction to OpenShift updates.

**The ClusterVersion object**

**7.2.1**

One of the resources that the Cluster Version Operator (CVO) monitors is the ClusterVersion resource. Administrators and OpenShift Container Platform components can communicate or interact with the CVO through the ClusterVersion object. The desired CVO state is declared through the ClusterVersion object and the current CVO state is reflected in the object’s status.
**Note** : Do not directly modify the ClusterVersion object. Instead, use interfaces such as
the oc CLI or the web console to declare your update target. The CVO continually reconciles the cluster with the target state declared in the spec property of the ClusterVersion resource. When the desired release differs from the actual release, that reconciliation updates the cluster.

**Update availability data**

**7.2.1.1**

The ClusterVersion resource also contains information about updates that are available to the cluster. This includes updates that are available, but not recommended due to a known risk that applies to the cluster. These updates are known as conditional updates. To learn how the CVO maintains this information about available updates in the ClusterVersion resource, see the "Evaluation of update availability" section. You can inspect all available updates with the following command:

| $ oc adm upgrade --include-not-recommended |   |   |
|---|---|---|
| Note: The additional | --include-not-recommended | parameter includes updates that are |

available with known issues that apply to the cluster.

**Example output**

Page 74 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Cluster version is 4.13.40 Upstream is unset, so the cluster will use an appropriate default. Channel: stable-4.14 (available channels: candidate-4.13, candidate-4.14, eus-4.14, fast-4.13, fast-4.14, stable-4.13, stable-4.14) Recommended updates: VERSION IMAGE 4.14.27 quay.io/openshift-release-dev/ocprelease@sha256:4d30b359aa6600a89ed49ce6a9a5fdab54092bcb821a25480fdfbc47e66af9ec 4.14.26 quay.io/openshift-release-dev/ocprelease@sha256:4fe7d4ccf4d967a309f83118f1a380a656a733d7fcee1dbaf4d51752a6372890 4.14.25 quay.io/openshift-release-dev/ocprelease@sha256:a0ef946ef8ae75aef726af1d9bbaad278559ad8cab2c1ed1088928a0087990b6 4.14.24 quay.io/openshift-release-dev/ocprelease@sha256:0a34eac4b834e67f1bca94493c237e307be2c0eae7b8956d4d8ef1c0c462c7b0 4.14.23 quay.io/openshift-release-dev/ocprelease@sha256:f8465817382128ec7c0bc676174bad0fb43204c353e49c146ddd83a5b3d58d92 4.13.42 quay.io/openshift-release-dev/ocprelease@sha256:dcf5c3ad7384f8bee3c275da8f886b0bc9aea7611d166d695d0cf0fff40a0b55 4.13.41 quay.io/openshift-release-dev/ocprelease@sha256:dbb8aa0cf53dc5ac663514e259ad2768d8c82fd1fe7181a4cfb484e3ffdbd3ba Updates with known issues: Version: 4.14.22 Image: quay.io/openshift-release-dev/ocprelease@sha256:7093fa606debe63820671cc92a1384e14d0b70058d4b4719d666571e1fc62190 Reason: MultipleReasons Message: Exposure to AzureRegistryImageMigrationUserProvisioned is unknown due to an evaluation failure: client-side throttling: only 18.061µs has elapsed since the last match call completed for this cluster condition backend; this cached cluster condition request has been queued for later execution In Azure clusters with the user-provisioned registry storage, the in-cluster image registry component may struggle to complete the cluster update. https://issues.redhat.com/browse/IR-468 Incoming HTTP requests to services exposed by Routes may fail while routers reload their configuration, especially when made with Apache HTTPClient versions before 5.0. The problem is more likely to occur in clusters with higher number of Routes and corresponding endpoints. https://issues.redhat.com/browse/NE-1689 Version: 4.14.21 Image: quay.io/openshift-release-dev/ocprelease@sha256:6e3fba19a1453e61f8846c6b0ad3abf41436a3550092cbfd364ad4ce194582b7 Reason: MultipleReasons Message: Exposure to AzureRegistryImageMigrationUserProvisioned is unknown due to an evaluation failure: client-side throttling: only 33.991µs has elapsed since the last match call completed for this cluster condition backend; this cached cluster condition request has been queued for later execution In Azure clusters with the user-provisioned registry storage, the in-cluster image registry component Page 75 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| may struggle to complete the cluster update. https://issues.redhat.com/browse/IR-468 |   |   |   |   |
|---|---|---|---|---|
| Incoming HTTP requests to services exposed by Routes may fail while routers reload their |   |   |   |   |
| configuration, especially when made with Apache HTTPClient versions before 5.0. The problem is more |   |   |   |   |
| likely to occur in clusters with higher number of Routes and corresponding endpoints. |   |   |   |   |
| https://issues.redhat.com/browse/NE-1689 |   |   |   |   |
| The | oc adm upgrade | command queries the | ClusterVersion | resource for information about |

available updates and presents it in a human-readable format. One way to directly inspect the underlying availability data created by the CVO is by

| querying the | ClusterVersion | resource with the following command: |
|---|---|---|
| $ oc get clusterversion version -o json \| jq '.status.availableUpdates' |   |   |

**Example output**

[ { "channels": [ "candidate-4.11", "candidate-4.12", "fast-4.11", "fast-4.12" ], "image": "quay.io/openshift-release-dev/ocprelease@sha256:400267c7f4e61c6bfa0a59571467e8bd85c9188e442cbd820cc8263809be3775", "url": "https://access.redhat.com/errata/RHBA-2023:3213", "version": "4.11.41" }, ... ] A similar command can be used to check conditional updates: $ oc get clusterversion version -o json | jq '.status.conditionalUpdates'

**Example output**

[ { "conditions": [ { "lastTransitionTime": "2023-05-30T16:28:59Z", "message": "The 4.11.36 release only resolves an installation issue https://issues.redhat.com//browse/OCPBUGS-11663 , which does not affect already running clusters. 4.11.36 does not include fixes delivered in recent 4.11.z releases and therefore upgrading from these versions would cause fixed bugs to reappear. Red Hat does not recommend upgrading clusters to 4.11.36 version for this reason. https://access.redhat.com/solutions/7007136", "reason": "PatchesOlderRelease", "status": "False", "type": "Recommended" } ], "release": { "channels": [...], "image": "quay.io/openshift-release-dev/ocp- Page 76 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack release@sha256:8c04176b771a62abd801fcda3e952633566c8b5ff177b93592e8e8d2d1f8471d", "url": "https://access.redhat.com/errata/RHBA-2023:1733", "version": "4.11.36" }, "risks": [...] }, ... ]

**Evaluation of update availability**

**7.2.2**

The Cluster Version Operator (CVO) periodically queries the OpenShift Update Service (OSUS) for the most recent data about update possibilities. This data is based on the cluster’s subscribed channel. The CVO then saves information about update recommendations into either the availableUpdates or conditionalUpdates field of its ClusterVersion resource. The CVO periodically checks the conditional updates for update risks. These risks are conveyed through the data served by the OSUS, which contains information for each version about known issues that might affect a cluster updated to that version. Most risks are limited to clusters with specific characteristics, such as clusters with a certain size or clusters that are deployed in a particular cloud platform. The CVO continuously evaluates its cluster characteristics against the conditional risk information for each conditional update. If the CVO finds that the cluster matches the criteria, the CVO stores this information in the conditionalUpdates field of its ClusterVersion resource. If the CVO finds that the cluster does not match the risks of an update, or that there are no risks associated with the update, it stores the target version in the availableUpdates field of its ClusterVersion resource. The user interface, either the web console or the OpenShift CLI (oc), presents this information in sectioned headings to the administrator. Each known issue associated with the update path contains a link to further resources about the risk so that the administrator can make an informed decision about the update.

**Release images**

**7.2.3**

A release image is the delivery mechanism for a specific OpenShift Container Platform (OCP) version. It contains the release metadata, a Cluster Version Operator (CVO) binary matching the release version, every manifest needed to deploy individual cluster Operators, and a list of SHA digest-versioned references to all container images that make up this version. You can extract a specific release image by running the following command: $ oc adm release extract <release image>

**Example command**

$ oc adm release extract quay.io/openshift-release-dev/ocp-release:4.12.6-x86_64

**Example output**

Page 77 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Extracted release payload from digest sha256:800d1e39d145664975a3bb7cbc6e674fbf78e3c45b5dde9ff2c5a11a8690c87b created at 2023- 03-01T12:46:29Z After the release image is extracted, you can inspect its contents by running the following command: $ ls

**Example output**

0000_03_authorization-openshift_01_rolebindingrestriction.crd.yaml 0000_03_config-operator_01_proxy.crd.yaml 0000_03_marketplace-operator_01_operatorhub.crd.yaml 0000_03_marketplace-operator_02_operatorhub.cr.yaml 0000_03_quota-openshift_01_clusterresourcequota.crd.yaml ... 0000_90_service-ca-operator_02_prometheusrolebinding.yaml 0000_90_service-ca-operator_03_servicemonitor.yaml 0000_99_machine-api-operator_00_tombstones.yaml image-references release-metadata In this example output, the following contents can be seen:

| 0000 03 quota-openshift 01 clusterresourcequota.crd.yaml _ _ _ _ |   |   |   |
|---|---|---|---|
| the | ClusterResourceQuota |   |   |
| 0000 90 service-ca-operator 02 prometheusrolebinding.yaml _ _ _ _ |   |   |   |
| the | PrometheusRoleBinding | resource for the | service-ca-operator |

Runlevel 90. ●image-references is the list of SHA digest-versioned references to all required images.

**Update process workflow**

**7.2.4**

When you initiate a cluster update, the Cluster Version Operator (CVO) begins a specific sequence of events to orchestrate the update. The following steps represent a detailed workflow of the OpenShift Container Platform update process: 1.The target version is stored in the spec.desiredUpdate.version field of the ClusterVersion resource, which may be managed through the web console or the CLI. 2.The CVO detects that the desiredUpdate field in the ClusterVersion resource differs from the current cluster version. Using graph data from the OpenShift Update Service, the CVO resolves the desired cluster version to a pull spec for the release image. 3.The CVO validates the integrity and authenticity of the release image. Red Hat publishes cryptographically-signed statements about published release images at predefined locations by using image SHA digests as unique and immutable release image identifiers. The CVO utilizes a list of built-in public keys to validate the presence and signatures of the statement matching the checked release image. 4.The CVO creates a job named version-$version-$hash in the openshift-clusterversion namespace. This job uses containers that are executing the release image, so Page 78 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack the cluster downloads the image through the container runtime. The job then extracts the manifests and metadata from the release image to a shared volume that is accessible to the CVO. 5.The CVO validates the extracted manifests and metadata. 6.The CVO checks some preconditions to ensure that no problematic condition is detected in the cluster. Certain conditions can prevent updates from proceeding. These conditions are either determined by the CVO itself, or reported by individual cluster Operators that detect some details about the cluster that the Operator considers problematic for the update. 7.The CVO records the accepted release in status.desired and creates a status.history entry about the new update. 8.The CVO begins reconciling the manifests from the release image. Cluster Operators are updated in separate stages called Runlevels, and the CVO ensures that all Operators in a Runlevel finish updating before it proceeds to the next level. 9.Manifests for the CVO itself are applied early in the process. When the CVO deployment is applied, the current CVO pod stops, and a CVO pod that uses the new version starts. The new CVO proceeds to reconcile the remaining manifests. 10.The update proceeds until the entire control plane is updated to the new version. Individual cluster Operators might perform update tasks on their domain of the cluster, and while they do so, they report their state through the Progressing=True condition. 11.The Machine Config Operator (MCO) manifests are applied towards the end of the process. The updated MCO then begins updating the system configuration and operating system of every node. Each node might be drained, updated, and rebooted before it starts to accept workloads again. The cluster reports as updated after the control plane update is finished, usually before all nodes are updated. After the update, the CVO maintains all cluster resources to match the state delivered in the release image.

**Understanding how manifests are applied during an update**

**7.2.5**

Some manifests supplied in a release image must be applied in a certain order because of the dependencies between them. For example, the CustomResourceDefinition resource must be created before the matching custom resources. Additionally, there is a logical order in which the individual cluster Operators must be updated to minimize disruption in the cluster. The Cluster Version Operator (CVO) implements this logical order through the concept of Runlevels. These dependencies are encoded in the filenames of the manifests in the release image: 0000_<runlevel>_<component>_<manifest-name>.yaml For example: 0000_03_config-operator_01_proxy.crd.yaml The CVO internally builds a dependency graph for the manifests, where the CVO obeys the following rules: Page 79 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●During an update, manifests at a lower Runlevel are applied before those at a higher Runlevel. ●Within one Runlevel, manifests for different components can be applied in parallel. ●Within one Runlevel, manifests for a single component are applied in lexicographic order. The CVO then applies manifests following the generated dependency graph.
**Note** : For some resource types, the CVO monitors the resource after its manifest is
applied, and considers it to be successfully updated only after the resource reaches a stable state. Achieving this state can take some time. This is especially true for ClusterOperator resources, while the CVO waits for a cluster Operator to update itself and then update its ClusterOperator status. The CVO waits until all cluster Operators in the Runlevel meet the following conditions before it proceeds to the next Runlevel: ●The cluster Operators have an Available=True condition. ●The cluster Operators have a Degraded=False condition. ●The cluster Operators declare they have achieved the desired version in their ClusterOperator resource. Some actions can take significant time to finish. The CVO waits for the actions to complete in order to ensure the subsequent Runlevels can proceed safely. Initially reconciling the new release’s manifests is expected to take 60 to 120 minutes in total; see **Understanding**
**OpenShift Container Platform update duration** for more information about factors that
influence update duration. Page 80 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack In the previous example diagram, the CVO is waiting until all work is completed at Runlevel
20. The CVO has applied all manifests to the Operators in the Runlevel, but
the cccc performs some actions after its new version was deployed. The kube-apiserveroperator ClusterOperator declares this progress through the Progressing=True condition and by not declaring the new version as reconciled in its status.versions. The CVO waits until the ClusterOperator reports an acceptable status, and then it will start reconciling manifests at Runlevel 25.

**Understanding how the Machine Config Operator updates nodes**

**7.2.6**

The Machine Config Operator (MCO) applies a new machine configuration to each control plane node and compute node. During the machine configuration update, control plane nodes and compute nodes are organized into their own machine config pools, where the pools of machines are updated in parallel. Page 81 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack The .spec.maxUnavailable parameter, which has a default value of 1, determines how many nodes in a machine config pool can simultaneously undergo the update process.
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool. When the machine configuration update process begins, the MCO checks the amount of currently unavailable nodes in a pool. If there are fewer unavailable nodes than the value of .spec.maxUnavailable, the MCO initiates the following sequence of actions on available nodes in the pool: 1.Cordon and drain the node
**Note**: When a node is cordoned, workloads cannot be scheduled to it.
2.Update the system configuration and operating system (OS) of the node 3.Reboot the node 4.Uncordon the node A node undergoing this process is unavailable until it is uncordoned and workloads can be scheduled to it again. The MCO begins updating nodes until the number of unavailable nodes is equal to the value of .spec.maxUnavailable. As a node completes its update and becomes available, the number of unavailable nodes in the machine config pool is once again fewer than .spec.maxUnavailable. If there are remaining nodes that need to be updated, the MCO initiates the update process on a node until the .spec.maxUnavailable limit is once again reached. This process repeats until each control plane node and compute node has been updated. The following example workflow describes how this process might occur in a machine config pool with 5 nodes, where .spec.maxUnavailable is 3 and all nodes are initially available: 1.The MCO cordons nodes 1, 2, and 3, and begins to drain them. 2.Node 2 finishes draining, reboots, and becomes available again. The MCO cordons node 4 and begins draining it. 3.Node 1 finishes draining, reboots, and becomes available again. The MCO cordons node 5 and begins draining it. 4.Node 3 finishes draining, reboots, and becomes available again. 5.Node 5 finishes draining, reboots, and becomes available again. 6.Node 4 finishes draining, reboots, and becomes available again. Because the update process for each node is independent of other nodes, some nodes in the example above finish their update out of the order in which they were cordoned by the MCO. You can check the status of the machine configuration update by running the following command: $ oc get mcp

**Example output**

NAME CONFIG UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE Page 82 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack master rendered-master-acd1358917e9f98cbdb599aea622d78b True False False 3 3 3 0 22h worker rendered-worker-1d871ac76e1951d32b2fe92369879826 False True False 2 1 1 0 22h

### 7.3 Understanding update channels and releases

Update channels are the mechanism by which users declare the OpenShift Container Platform minor version they intend to update their clusters to. They also allow users to choose the timing and level of support their updates will have through the fast, stable, candidate, and eus channel options. The Cluster Version Operator uses an update graph based on the channel declaration, along with other conditional information, to provide a list of recommended and conditional updates available to the cluster.

**Overview of update channels**

**7.3.1**

Update channels correspond to a minor version of OpenShift Container Platform. The version number in the channel represents the target minor version that the cluster will eventually be updated to, even if it is higher than the cluster’s current minor version. For instance, OpenShift Container Platform 4.10 update channels provide the following recommendations: ●Updates within 4.10. ●Updates within 4.9. ●Updates from 4.9 to 4.10, allowing all 4.9 clusters to eventually update to 4.10, even if they do not immediately meet the minimum z-stream version requirements. ●eus-4.10 only: updates within 4.8. ●eus-4.10 only: updates from 4.8 to 4.9 to 4.10, allowing all 4.8 clusters to eventually update to 4.10. 4.10 update channels do not recommend updates to 4.11 or later releases. This strategy ensures that administrators must explicitly decide to update to the next minor version of OpenShift Container Platform. Update channels control only release selection and do not impact the version of the cluster that you install. The openshift-install binary file for a specific version of OpenShift Container Platform always installs that version. OpenShift Container Platform 4.18 offers the following update channels: ●stable-4.18 ●eus-4.y (only offered for EUS versions and meant to facilitate updates between EUS versions)

| fast-4.18 |   |
|---|---|
| candidate-4.18 |   |

Page 83 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack If you do not want the Cluster Version Operator to fetch available updates from the update recommendation service, you can use the oc adm upgrade channel command in the OpenShift CLI to configure an empty channel. This configuration can be helpful if, for example, a cluster has restricted network access and there is no local, reachable update recommendation service.
**Warning**: Red Hat recommends updating only to versions suggested by OpenShift
Update Service. For a minor version update, versions must be contiguous. Red Hat does not test updates to noncontiguous versions and cannot guarantee compatibility with earlier versions.

**Update channels**

**7.3.2**

OpenShift Container Platform offers several update channels for you to choose from, depending on your desired update strategy.

**fast-4.18 channel**

**7.3.2.1**

The fast-4.18 channel is updated with new versions of OpenShift Container Platform 4.18 as soon as Red Hat declares the version as a general availability (GA) release. As such, these releases are fully supported and purposed to be used in production environments.

**stable-4.18 channel**

**7.3.2.2**

While the fast-4.18 channel contains releases as soon as their errata are published, releases are added to the stable-4.18 channel after a delay. During this delay, data is collected from multiple sources and analyzed for indications of product regressions. Once a significant number of data points have been collected, these releases are added to the stable channel.
**Note**: Since the time required to obtain a significant number of data points varies based
on many factors, Service LeveL Objective (SLO) is not offered for the delay duration between fast and stable channels. For more information, please see "Choosing the correct channel for your cluster" Newly installed clusters default to using stable channels.

**eus-4.y channel**

**7.3.2.3**

In addition to the stable channel, all even-numbered minor versions of OpenShift Container Platform offer Extended Update Support (EUS). Releases promoted to the stable channel are also simultaneously promoted to the EUS channels. The primary purpose of the EUS channels is to serve as a convenience for clusters performing a Control Plane Only update.
**Note**: Both standard and non-EUS subscribers can access all EUS repositories and
necessary RPMs (rhel-*-eus-rpms) to be able to support critical purposes such as debugging and building drivers. Page 84 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**candidate-4.18 channel**

**7.3.2.4**

The candidate-4.18 channel offers unsupported early access to releases as soon as they are built. Releases present only in candidate channels may not contain the full feature set of eventual GA releases or features may be removed prior to GA. Additionally, these releases have not been subject to full Red Hat Quality Assurance and may not offer update paths to later GA releases. Given these caveats, the candidate channel is only suitable for testing purposes where destroying and recreating a cluster is acceptable.

**Restricted network clusters**

**7.3.3**

If you manage the container images for your OpenShift Container Platform clusters yourself, you must consult the Red Hat errata that is associated with product releases and note any comments that impact updates. During an update, the user interface might warn you about switching between these versions, so you must ensure that you selected an appropriate version before you bypass those warnings.

**Update recommendations in the channel**

**7.3.4**

OpenShift Container Platform maintains an update recommendation service that knows your installed OpenShift Container Platform version and the path to take within the channel to get you to the next release. Update paths are also limited to versions relevant to your currently selected channel and its promotion characteristics. You can imagine seeing the following releases in your channel: ●4.18.0 ●4.18.1 ●4.18.3 ●4.18.4 The service recommends only updates that have been tested and have no known serious regressions. For example, if your cluster is on 4.18.1 and OpenShift Container Platform suggests 4.18.4, then it is recommended to update from 4.18.1 to 4.18.4.
**Important**: Do not rely on consecutive patch numbers. In this example, 4.18.2 is not and
never was available in the channel, therefore updates to 4.18.2 are not recommended or supported.

**Update recommendations and Conditional Updates**

**7.3.5**

Red Hat monitors newly released versions and update paths associated with those versions before and after they are added to supported channels. If Red Hat removes update recommendations from any supported release, a superseding update recommendation will be provided to a future version that corrects the regression. Page 85 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack There may however be a delay while the defect is corrected, tested, and promoted to your selected channel. Beginning in OpenShift Container Platform 4.10, when update risks are confirmed, they are declared as Conditional Update risks for the relevant updates. Each known risk may apply to all clusters or only clusters matching certain conditions. Some examples include having the Platform set to None or the CNI provider set to OpenShiftSDN. The Cluster Version Operator (CVO) continually evaluates known risks against the current cluster state. If no risks match, the update is recommended. If the risk matches, those update paths are labeled as updates with known issues, and a reference link to the known issues is provided. The reference link helps the cluster admin decide if they want to accept the risk and continue to update their cluster. When Red Hat chooses to declare Conditional Update risks, that action is taken in all relevant channels simultaneously. Declaration of a Conditional Update risk may happen either before or after the update has been promoted to supported channels.

**What to consider when choosing an update channel**

**7.3.6**

Choosing the appropriate update channel for your cluster involves two decisions. First, select the minor version you want for your cluster update. Selecting a channel which matches your current version ensures that you only apply z-stream updates and do not receive feature updates. Selecting an available channel which has a version greater than your current version will ensure that after one or more updates your cluster will have updated to that version. Your cluster will only be offered channels which match its current version, the next version, or the next EUS version.
**Note**: Due to the complexity involved in planning updates between versions many minors
apart, channels that assist in planning updates beyond a single Control Plane Only update are not offered. Second, you should choose your desired rollout strategy. You may choose to update as soon as Red Hat declares a release GA by selecting from fast channels or you may want to wait for Red Hat to promote releases to the stable channel. Update recommendations offered in the fast-4.18 and stable-4.18 are both fully supported and benefit equally from ongoing data analysis. The promotion delay before promoting a release to the stable channel represents the only difference between the two channels. Updates to the latest zstreams are generally promoted to the stable channel within a week or two, however the delay when initially rolling out updates to the latest minor is much longer, generally 45-90 days. Please consider the promotion delay when choosing your desired channel, as waiting for promotion to the stable channel may affect your scheduling plans. Additionally, there are several factors which may lead an organization to move clusters to the fast channel either permanently or temporarily including the following: ●The desire to apply a specific fix known to affect your environment without delay. ●Application of CVE fixes without delay. CVE fixes may introduce regressions, so promotion delays still apply to z-streams with CVE fixes. Page 86 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Internal testing processes. If it takes your organization several weeks to qualify releases it is best test concurrently with our promotion process rather than waiting. This also assures that any telemetry signal provided to Red Hat is a factored into our rollout, so issues relevant to you can be fixed faster.

**Considerations for switching between channels**

**7.3.7**

You can switch your cluster’s update channel through the web console or the CLI, in order to access different update recommendations for your cluster. You can switch the channel from the CLI by running the following command: $ oc adm upgrade channel <channel> The web console will display an alert if you switch to a channel that does not include the current release. The web console does not recommend any updates while on a channel without the current release. You can return to the original channel at any point, however. Changing your channel might impact the supportability of your cluster. The following conditions might apply: ●Your cluster is still supported if you change from the stable-4.18 channel to the fast- 4.18 channel. ●You can switch to the candidate-4.18 channel at any time, but some releases for this channel might be unsupported. ●You can switch from the candidate-4.18 channel to the fast-4.18 channel if your current release is a general availability release.

| stable-4.18 |   | chann |
|---|---|---|
| ted to | stable-4.18 |   |

●You can always switch from the fast-4.18 channel to the stable-4.18 channel. There is a possible delay of up to a day for the release to be promoted to stable-4.18 if the current release was recently promoted.

### 7.4 Understanding OpenShift Container Platform update

**duration**

OpenShift Container Platform update duration varies based on the deployment topology. You can understand the factors that affect update duration and use them to estimate how long the cluster update takes in your environment.

**Factors affecting update duration**

**7.4.1**

The duration of OpenShift Container Platform updates vary for several reasons. The following factors can affect your cluster update duration: ●The reboot of compute nodes to the new machine configuration by Machine Config Operator (MCO) ○The value of MaxUnavailable in the machine config pool
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools
in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool. Page 87 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ○The minimum number or percentages of replicas set in pod disruption budget (PDB) ●The number of nodes in the cluster ●The health of the cluster nodes

**Cluster update phases**

**7.4.2**

OpenShift Container Platform updates are done in multiple phases. The cluster update happens in the following two phases: ●Cluster Version Operator (CVO) target update payload deployment ●Machine Config Operator (MCO) node updates

**Cluster Version Operator target update payload deployment**

**7.4.2.1**

In the first phase of the update, the Cluster Version Operator (CVO) retrieves the target update release image and applies to the cluster. All components which run as pods are updated during this phase, whereas the host components are updated by the Machine Config Operator (MCO). This process might take 60 to 120 minutes.
**Note**: The CVO phase of the update does not restart the nodes.

**Machine Config Operator node updates**

**7.4.2.2**

In the second phase of the update, the Machine Config Operator (MCO) applies a new machine configuration to each control plane and compute node. During this process, the MCO performs the following sequential actions on each node of the cluster: 1.Cordon and drain all the nodes 2.Update the operating system (OS) 3.Reboot the nodes 4.Uncordon all nodes and schedule workloads on the node
**Note**: When a node is cordoned, workloads cannot be scheduled to it.
The time to complete this process depends on several factors including the node and infrastructure configuration. This process might take 5 or more minutes to complete per node. In addition to MCO, you should consider the impact of the following parameters: ●The control plane node update duration is predictable and oftentimes shorter than compute nodes, because the control plane workloads are tuned for graceful updates and quick drains. ●You can update the compute nodes in parallel by setting the maxUnavailable field to greater than 1 in the Machine Config Pool (MCP). The MCO cordons the number of

| maxUnavailable |   | a |
|---|---|---|
| f | maxUnavailable |   |
|   | maxUnavailable |   |

nodes specified in maxUnavailable and marks them unavailable for update. ●When you increase maxUnavailable on the MCP, it can help the pool to update more quickly. However, if maxUnavailable is set too high, and several nodes are cordoned Page 88 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack simultaneously, the pod disruption budget (PDB) guarded workloads could fail to drain because a schedulable node cannot be found to run the replicas. If you increase maxUnavailable for the MCP, ensure that you still have sufficient schedulable nodes to allow PDB guarded workloads to drain. ●Before you begin the update, you must ensure that all the nodes are available. Any unavailable nodes can significantly impact the update duration because the node unavailability affects the maxUnavailable and pod disruption budgets. To check the status of nodes from the terminal, run the following command: $ oc get node

**Example Output**

| NAME STATUS ROLES AGE |   |   |   |   |
|---|---|---|---|---|
| VERSION |   |   |   |   |
| ip-10-0-137-31.us-east-2.compute.internal Ready,SchedulingDisabled worker 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| ip-10-0-151-208.us-east-2.compute.internal Ready master 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| ip-10-0-176-138.us-east-2.compute.internal Ready master 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| ip-10-0-183-194.us-east-2.compute.internal Ready worker 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| ip-10-0-204-102.us-east-2.compute.internal Ready master 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| ip-10-0-207-224.us-east-2.compute.internal Ready worker 12d |   |   |   |   |
| v1.23.5+3afdacb |   |   |   |   |
| If the status of the node is | NotReady | or | SchedulingDisabled | , then the node is not available |

and this impacts the update duration. You can also check the status of nodes from the **Administrator** perspective in the web console by expanding **Compute → Nodes**.

**Example update duration of cluster Operators**

**7.4.2.3**

You can review an example of the update duration for cluster Operators to better understand the factors that affect the duration of the update. Page 89 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack The previous diagram shows an example of the time that cluster Operators might take to update to their new versions. The example is based on a three-node AWS OVN cluster, which has a healthy compute MachineConfigPool and no workloads that take long to drain, updating from 4.13 to 4.14.
**Note**:
●The specific update duration of a cluster and its Operators can vary based on several cluster characteristics, such as the target version, the amount of nodes, and the types of workloads scheduled to the nodes. ●Some Operators, such as the Cluster Version Operator, update themselves in a short amount of time. These Operators have either been omitted from the diagram or are included in the broader group of Operators labeled "Other Operators in parallel". Each cluster Operator has characteristics that affect the time it takes to update itself. For instance, the Kube API Server Operator in this example took more than eleven minutes to update because kube-apiserver provides graceful termination support, meaning that existing, in-flight requests are allowed to complete gracefully. This might result in a longer shutdown of the kube-apiserver. In the case of this Operator, update speed is sacrificed to help prevent and limit disruptions to cluster functionality during an update. Another characteristic that affects the update duration of an Operator is whether the Operator utilizes DaemonSets. The Network and DNS Operators utilize full-cluster DaemonSets, which can take time to roll out their version changes, and this is one of several reasons why these Operators might take longer to update themselves. Additionally, the update duration for some Operators is heavily dependent on characteristics of the cluster itself. For example, the Machine Config Operator update applies machine configuration changes to each node in the cluster. A cluster with many Page 90 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack nodes has a longer update duration for the Machine Config Operator compared to a cluster with fewer nodes.
**Note**: Each cluster Operator is assigned a stage during which it can be updated. Operators
within the same stage can update simultaneously, and Operators in a given stage cannot begin updating until all previous stages have been completed. For more information, see "Understanding how manifests are applied during an update".

**How to estimate cluster update time**

**7.4.3**

Historical update duration of similar clusters provides you the best estimate for the future cluster updates. If you do not have historical data, you can calculate an estimate of the update duration. You can use the following convention to estimate your cluster update time: Cluster update time = CVO target update payload deployment time + (# node update iterations x MCO node update time) A node update iteration consists of one or more nodes updated in parallel. The control plane nodes are always updated in parallel with the compute nodes. In addition, one or more compute nodes can be updated in parallel based on the maxUnavailable value.
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool. For example, to estimate the update time, consider an OpenShift Container Platform cluster with three control plane nodes and six compute nodes, where each host takes about 5 minutes to reboot.
**Note**: The time it takes to reboot a particular node varies significantly. In cloud instances,
the reboot might take about 1 to 2 minutes, whereas in physical bare metal hosts the reboot might take more than 15 minutes. In a scenario where you set maxUnavailable to 1 for both the control plane and compute nodes Machine Config Pool (MCP), then all the six compute nodes will update one after another in each iteration:

| Cluster update time = 60 + (6 x 5) = 90 minutes |   |   |   |   |
|---|---|---|---|---|
| In a scenario where you set | maxUnavailable | to | 2 | for the compute node MCP, then two |

compute nodes will update in parallel in each iteration. Therefore it takes total three iterations to update all the nodes. Cluster update time = 60 + (3 x 5) = 75 minutes
**Important**: The default setting for maxUnavailable is 1 for all the MCPs in OpenShift
Container Platform. It is recommended that you do not change the maxUnavailable in the control plane MCP.

**Red Hat Enterprise Linux (RHEL) compute nodes**

**7.4.4**

Red Hat Enterprise Linux (RHEL) compute nodes require an additional usage of openshiftansible to update node binary components. The actual time spent updating RHEL compute Page 91 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack nodes should not be significantly different from Red Hat Enterprise Linux CoreOS (RHCOS) compute nodes.

### 7.5 Preparing to update a cluster

**Preparing to update to OpenShift Container Platform 4.18**

**7.5.1**

Learn more about administrative tasks that cluster admins must perform to successfully initialize an update, as well as optional guidelines for ensuring a successful update.

**Kubernetes API removals**

**7.5.1.1**

There are no Kubernetes API removals in OpenShift Container Platform 4.18.

**Assessing the risk of conditional updates**

**7.5.1.2**

A conditional update is an update target that is available but not recommended due to a known risk that applies to your cluster. The Cluster Version Operator (CVO) periodically queries the OpenShift Update Service (OSUS) for the most recent data about update recommendations, and some potential update targets might have risks associated with them. The CVO evaluates the conditional risks, and if the risks are not applicable to the cluster, then the target version is available as a recommended update path for the cluster. If the risk is determined to be applicable, or if for some reason CVO cannot evaluate the risk, then the update target is available to the cluster as a conditional update. When you encounter a conditional update while you are trying to update to a target version, you must assess the risk of updating your cluster to that version. Generally, if you do not have a specific need to update to that target version, it is best to wait for a recommended update path from Red Hat. However, if you have a strong reason to update to that version, for example, if you need to fix an important CVE, then the benefit of fixing the CVE might outweigh the risk of the update being problematic for your cluster. You can complete the following tasks to determine whether you agree with the Red Hat assessment of the update risk: ●Complete extensive testing in a non-production environment to the extent that you are comfortable completing the update in your production environment. ●Follow the links provided in the conditional update description, investigate the bug, and determine if it is likely to cause issues for your cluster. If you need help understanding the risk, contact Red Hat Support.

**etcd backups before cluster updates**

**7.5.1.3**

etcd backups record the state of your cluster and all of its resource objects. You can use backups to attempt restoring the state of a cluster in disaster scenarios where you cannot recover a cluster in its currently dysfunctional state. Page 92 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack In the context of updates, you can attempt an etcd restoration of the cluster if an update introduced catastrophic conditions that cannot be fixed without reverting to the previous cluster version. etcd restorations might be destructive and destabilizing to a running cluster, use them only as a last resort.
**Warning**: Due to their high consequences, etcd restorations are not intended to be used
as a rollback solution. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support. There are several factors that affect the viability of an etcd restoration. For more information, see "Backing up etcd data" and "Restoring to a previous cluster state".

**Best practices for cluster updates**

**7.5.1.4**

OpenShift Container Platform provides a robust update experience that minimizes workload disruptions during an update. Updates will not begin unless the cluster is in an upgradeable state at the time of the update request. This design enforces some key conditions before initiating an update, but there are a number of actions you can take to increase your chances of a successful cluster update.

**7.5.1.4.1Choose versions recommended by the OpenShift Update Service**

The OpenShift Update Service (OSUS) provides update recommendations based on cluster characteristics such as the cluster’s subscribed channel. The Cluster Version Operator saves these recommendations as either recommended or conditional updates. While it is possible to attempt an update to a version that is not recommended by OSUS, following a recommended update path protects users from encountering known issues or unintended consequences on the cluster. Choose only update targets that are recommended by OSUS to ensure a successful update.

**7.5.1.4.2Address all critical alerts on the cluster**

Critical alerts must always be addressed as soon as possible, but it is especially important to address these alerts and resolve any problems before initiating a cluster update. Failing to address critical alerts before beginning an update can cause problematic conditions for the cluster. In the **Administrator** perspective of the web console, navigate to **Observe → Alerting** to find critical alerts.

**7.5.1.4.3Ensure that the cluster is in an Upgradable state**

When one or more Operators have not reported their Upgradeable condition as True for more than an hour, the ClusterNotUpgradeable warning alert is triggered in the cluster. In most cases this alert does not block patch updates, but you cannot perform a minor version update until you resolve this alert and all Operators report Upgradeable as True. Page 93 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.5.1.4.3.1SDN support removal**

OpenShift SDN network plugin was deprecated in versions 4.15 and 4.16. Starting with OpenShift Container Platform 4.17, the SDN network plugin is no longer supported and the content has been removed from the documentation. If your OpenShift Container Platform cluster is still using the OpenShift SDN CNI, see Migrating from the OpenShift SDN network plugin.
**Important**: It is not possible to update a cluster to OpenShift Container Platform 4.17 and
later if it is using the OpenShift SDN network plugin. You must migrate to the OVN- Kubernetes plugin before upgrading to OpenShift Container Platform 4.17 and later.

**7.5.1.4.4Ensure that enough spare nodes are available**

A cluster should not be running with little to no spare node capacity, especially when initiating a cluster update. Nodes that are not running and available may limit a cluster’s ability to perform an update with minimal disruption to cluster workloads. Depending on the configured value of the cluster’s maxUnavailable spec, the cluster might not be able to apply machine configuration changes to nodes if there is an unavailable node. Additionally, if compute nodes do not have enough spare capacity, workloads might not be able to temporarily shift to another node while the first node is taken offline for an update. Make sure that you have enough available nodes in each worker pool, as well as enough spare capacity on your compute nodes, to increase the chance of successful node updates.
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool.

**7.5.1.4.5Ensure that the cluster’s PodDisruptionBudget is properly configured**

You can use the PodDisruptionBudget object to define the minimum number or percentage of pod replicas that must be available at any given time. This configuration protects workloads from disruptions during maintenance tasks such as cluster updates. However, it is possible to configure the PodDisruptionBudget for a given topology in a way that prevents nodes from being drained and updated during a cluster update. When planning a cluster update, check the configuration of the PodDisruptionBudget object for the following factors: ●For highly available workloads, make sure there are replicas that can be temporarily taken offline without being prohibited by the PodDisruptionBudget. ●For workloads that are not highly available, make sure they are either not protected by a PodDisruptionBudget or have some alternative mechanism for draining these workloads eventually, such as periodic restart or guaranteed eventual termination. Page 94 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Preflight validation for Kernel Module Management (KMM)**

**7.5.2**

**Modules**

Before performing an upgrade on the cluster with applied KMM modules, you must verify that kernel modules installed using KMM are able to be installed on the nodes after the cluster upgrade and possible kernel upgrade. Preflight attempts to validate

| y | Module |   |
|---|---|---|
| Module |   | t |

every Module loaded in the cluster, in parallel. Preflight does not wait for validation of one Module to complete before starting validation of another Module.

**Validation kickoff**

**7.5.2.1**

Preflight validation is triggered by creating a PreflightValidationOCP resource in the cluster. This spec contains two fields:

**releaseImage**

Mandatory field that provides the name of the release image for the OpenShift Container Platform version the cluster is upgraded to.

| pushBuiltImage |   |   |
|---|---|---|
| If | true | , then the i |

If true, then the images created during the Build and Sign validation are pushed to their repositories. This field is false by default.

**Validation lifecycle**

**7.5.2.2**

Preflight validation attempts to validate every module loaded in the cluster. Preflight stops running validation on a Module resource after the validation is successful. If module validation fails, you can change the module definitions and Preflight tries to validate the module again in the next loop. If you want to run Preflight validation for an additional kernel, then you should create another PreflightValidationOCP resource for that kernel. After all the modules have been validated, it is recommended to delete the PreflightValidationOCP resource.

**Validation status**

**7.5.2.3**

A PreflightValidationOCP resource reports the status and progress of each module in the cluster that it attempts or has attempted to validate in its .status.modules list. Elements of that list contain the following fields:

**lastTransitionTime**

The last time the Module resource status transitioned from one status to another. This should be when the underlying status has changed. If that is not known, then using the time when the API field changed is acceptable.

**name**

The name of the Module resource.namespaceThe namespace of the Module resource.

**statusReason**

Verbal explanation regarding the status.

**verificationStage**

Page 95 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Describes the validation stage being executed:

| ● ● ● | image: |
|---|---|
|   | build |
|   | sign: |
| verificationStatus |   |

●image: Image existence verification The status of the Module verification:

| true: | Veri : Ver r: Err |
|---|---|
| false |   |
| erro |   |
| unknown |   |

●false: Verification failed ●error: Error during the verification process ●unknown: Verification has not started

**Preflight validation stages per Module**

**7.5.2.4**

Preflight runs the following validations on every KMM Module present in the cluster: 1.Image validation stage 2.Build validation stage 3.Sign validation stage

**7.5.2.4.1Image validation stage**

Image validation is always the first stage of the preflight validation to be executed. If image validation is successful, no other validations are run on that specific module. Image validation consists of two stages: 1.Image existence and accessibility. The code tries to access the image defined for the upgraded kernel in the module and get its manifests. 2.Verify the presence of the kernel module defined in the Module in the correct path for future modprobe execution. If this validation is successful, it probably means that the kernel module was compiled with the correct Linux headers. The correct path is <dirname>/lib/modules/<upgraded_kernel>/.

**7.5.2.4.2Build validation stage**

Build validation is executed only when image validation has failed and there is a build section in the Module that is relevant for the upgraded kernel. Build validation attempts to run the build job and validate that it finishes successfully.

| Note: You must specify the kernel version when running |   |   |   | depmod | , as shown here: |
|---|---|---|---|---|---|
| $ RUN depmod -b /opt ${KERNEL VERSION} _ |   |   |   |   |   |
| If the | PushBuiltImage | flag is defined in the | PreflightValidationOCP |   | custom resource (CR), it |

also tries to push the resulting image into its repository. The resulting image name is taken from the definition of the containerImage field of the Module CR.

| e | sign | section is |
|---|---|---|
| containerImage |   |   |

**Note**: If the sign section is defined for the upgraded kernel, then the resulting image will
not be the containerImage field of the Module CR, but a temporary image name, because the resulting image should be the product of Sign flow. Page 96 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.5.2.4.3Sign validation stage**

Sign validation is executed only when image validation has failed. There is a sign section in the Module resource that is relevant for the upgrade kernel, and build validation finishes successfully in case there was a build section in the Module relevant for the upgraded kernel. Sign validation attempts to run the sign job and validate that it finishes successfully. If the PushBuiltImage flag is defined in the PreflightValidationOCP CR, sign validation also tries to push the resulting image to its registry. The resulting image is always the image

| Module | . The inp |
|---|---|
| UnsignedImage |   |

the Build stage, or an image defined in the UnsignedImage field.

| put image is the build sec o be available for the sign | build |   | sec |
|---|---|---|---|
|   |   | sign |   |
| PreflightValidationOCP |   |   | CR |

**Note**: If a build section exists, the sign section input image is the build section’s output
image. Therefore, in order for the input image to be available for the sign section, the PushBuiltImage flag must be defined in the PreflightValidationOCP CR.

**Example PreflightValidationOCP resource**

**7.5.2.5**

This section shows an example of the PreflightValidationOCP resource in the YAML format. The example verifies all of the currently present modules against the upcoming kernel version included in the OpenShift Container Platform release 4.11.18, which the following release image points to:

| quay.io/openshift-release-dev/ocp- |   |   |   |   |
|---|---|---|---|---|
| release@sha256:22e149142517dfccb47be828f012659b1ccf71d26620e6f62468c264a7ce7863 |   |   |   |   |
| Because | .spec.pushBuiltImage | is set to | true | , KMM pushes the resulting images of |

Build/Sign in to the defined repositories. apiVersion: kmm.sigs.x-k8s.io/v1beta2 kind: PreflightValidationOCP metadata: name: preflight spec: releaseImage: quay.io/openshift-release-dev/ocprelease@sha256:22e149142517dfccb47be828f012659b1ccf71d26620e6f62468c264a7ce7863 pushBuiltImage: true

**Preparing to update from OpenShift Container Platform 4.18 to**

**7.5.3**

**a newer version**

Before you update from OpenShift Container Platform 4.18 to a newer version, learn about some of the specific concerns around Red Hat Enterprise Linux (RHEL) compute machines and Gateway API networking resources.

**Migrating workloads off of package-based RHEL worker nodes**

**7.5.3.1**

With the introduction of OpenShift Container Platform 4.19, package-based RHEL worker nodes are no longer supported. If you try to update your cluster while those nodes are up and running, the update will fail. Page 97 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack You can reschedule pods running on RHEL compute nodes to run on your RHCOS nodes instead by using node selectors. For example, the following Node object has a label for its operating system information, in this case RHCOS:

| Sample | Node | object with RHCOS label |
|---|---|---|
| kind: Node |   |   |
| apiVersion: v1 |   |   |
| metadata: |   |   |
| name: ip-10-0-131-14.ec2.internal |   |   |
| selfLink: /api/v1/nodes/ip-10-0-131-14.ec2.internal |   |   |
| uid: 7bc2580a-8b8e-11e9-8e01-021ab4174c74 |   |   |
| resourceVersion: '478704' |   |   |
| creationTimestamp: '2019-06-10T14:46:08Z' |   |   |
| labels: |   |   |
| kubernetes.io/os: linux |   |   |
| failure-domain.beta.kubernetes.io/zone: us-east-1a |   |   |
| node.openshift.io/os version: '4.18' _ |   |   |
| node-role.kubernetes.io/worker: '' |   |   |
| failure-domain.beta.kubernetes.io/region: us-east-1 |   |   |
| node.openshift.io/os id: rhcos _ |   |   |
| beta.kubernetes.io/instance-type: m4.large |   |   |
| kubernetes.io/hostname: ip-10-0-131-14 |   |   |
| beta.kubernetes.io/arch: amd64 |   |   |
| #... |   |   |

1.The label identifying the operating system that runs on the node, to match the pod node selector. Any pods that you want to schedule to new RHCOS nodes must contain a matching label in its nodeSelector field. The following procedure describes how to add the label.

**Procedure**

1.Deschedule the RHEL node currently running your existing pods by entering the following command:

| $ oc adm cordon <rhel-node> |   |   |
|---|---|---|
| 2. Add an | rhcos | node selector to a pod: |

●To add the node selector to existing and future pods, add the node selector to the controller object for the pods by entering the following command:

| Example | Deployment | object with |   | rhcos | label |   |
|---|---|---|---|---|---|---|
| $ oc patch dc <my-app> -p |   |   |   |   |   |   |
| '{"spec":{"template":{"spec":{"nodeSelector":{"node.openshift.io/os id":"rhcos"}}}}}' _ |   |   |   |   |   |   |
| Any existing pods under your |   |   | Deployment |   |   | controlling object will be re-created on your |

RHCOS nodes. ●To add the node selector to a specific, new pod, add the selector to the Pod object directly:

| Example | Pod | object with | rhcos | label |
|---|---|---|---|---|
| apiVersion: v1 |   |   |   |   |
| kind: Pod |   |   |   |   |
| metadata: |   |   |   |   |

Page 98 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack name: <my-app>
#...
spec: nodeSelector: node.openshift.io/os_id: rhcos
#...
The new pod will be created on RHCOS nodes, assuming the pod also has a controlling object.

**Identifying and removing RHEL worker nodes**

**7.5.3.2**

With the introduction of OpenShift Container Platform 4.19, package-based RHEL worker nodes are no longer supported. The following procedure describes how to identify RHEL nodes for cluster removal on bare-metal installations. You must complete the following steps to successfully update your cluster.

**Procedure**

1.Identify nodes in your cluster that are running RHEL by entering the following command: $ oc get -l node.openshift.io/os_id=rhel

**Example output**

NAME STATUS ROLES AGE VERSION rhel-node1.example.com Ready worker 7h v1.31.7 rhel-node2.example.com Ready worker 7h v1.31.7 rhel-node3.example.com Ready worker 7h v1.31.7 2.Continue with the node removal process. RHEL nodes are not managed by the Machine API and have no compute machine sets associated with them. You must unschedule and drain the node before you manually delete it from the cluster. For more information on this process, see How to remove a worker node from Red Hat OpenShift Container Platform 4 UPI.

**Provisioning new RHCOS worker nodes**

**7.5.3.3**

If you need additional compute nodes for your workloads, you can provision new ones either before or after you update your cluster. For more information, see the following machine management documentation: ●Manually scaling a compute machine set ●Applying autoscaling to an OpenShift Container Platform cluster ●Adding compute machines to clusters with user-provisioned infrastructure manually For installer-provisioned infrastructure installations, automatic scaling adds RHCOS nodes by default. For user-provisioned infrastructure installations on bare metal platforms, you can manually add RHCOS compute nodes to your cluster. Page 99 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Preparing for Gateway API management succession by the Ingress**

**7.5.3.4**

**Operator**

Starting in OpenShift Container Platform 4.19, the Ingress Operator manages the lifecycle of any Gateway API custom resource definitions (CRDs). Updating from a version before 4.19 of OpenShift Container Platform where this management was not present requires you to replace or remove any Gateway API CRDs that already exist in the cluster so that they conform to the specific OpenShift Container Platform specification required by the Ingress Operator. OpenShift Container Platform version 4.19 requires Gateway API Standard version 1.2.0 CRDs.
**Warning**: Updating or deleting Gateway API resources can result in downtime and loss of
service or data. Be sure you understand how this will affect your cluster before performing the steps in this procedure. If necessary, back up any Gateway API objects in YAML format in order to restore it later.

**Prerequisites**

●You have installed the OpenShift CLI (oc). ●You have access to an OpenShift Container Platform account with cluster administrator access. ●Optional: You have backed up any necessary Gateway API objects.

**Procedure**

1.List all the Gateway API CRDs that you need to remove by running the following command: $ oc get crd | grep "gateway.networking"

**Example output**

gatewayclasses.gateway.networking.k8s.io gateways.gateway.networking.k8s.io grpcroutes.gateway.networking.k8s.io httproutes.gateway.networking.k8s.io referencegrants.gateway.networking.k8s.io 2.Delete the Gateway API CRDs from the previous step by running the following command: $ oc delete crd gatewayclasses.networking.k8s.io && \ oc delete crd gateways.networking.k8s.io && \ oc delete crd grpcroutes.gateway.networking.k8s.io && \ oc delete crd httproutes.gateway.networking.k8s.io && \ oc delete crd referencesgrants.gateway.networking.k8s.io
**Important**: Any controller that was previously managing the lifecycle of the Gateway API
CRDs will fail to operate properly. Attempting to force its use in conjunction with the Ingress Operator to manage Gateway API CRDs might prevent the cluster update from succeeding. 3.Get the supported Gateway API CRDs by running the following command: $ oc apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.0/standardinstall.yaml Page 100 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 7.6 Performing a cluster update

**Updating a cluster using the CLI**

**7.6.1**

You can perform minor version and patch updates on an OpenShift Container Platform cluster by using the OpenShift CLI (oc).

**About updating single node OpenShift Container Platform**

**7.6.1.1**

You can update a single-node OpenShift Container Platform cluster by using either the console or CLI. However, note the following limitations: ●The prerequisite to pause the MachineHealthCheck resources is not required because there is no other node to perform the health check. ●Restoring a single-node OpenShift Container Platform cluster using an etcd backup is not officially supported. However, it is good practice to perform the etcd backup in case your update fails. If your control plane is healthy, you might be able to restore your cluster to a previous state by using the backup. ●Updating a single-node OpenShift Container Platform cluster requires downtime and can include an automatic reboot. The amount of downtime depends on the update payload, as described in the following scenarios: ○If the update payload contains an operating system update, which requires a reboot, the downtime is significant and impacts cluster management and user workloads. ○If the update contains machine configuration changes that do not require a reboot, the downtime is less, and the impact on the cluster management and user workloads is lessened. In this case, the node draining step is skipped with singlenode OpenShift Container Platform because there is no other node in the cluster to reschedule the workloads to. ○If the update payload does not contain an operating system update or machine configuration changes, a short API outage occurs and resolves quickly.
**Important**: There are conditions, such as bugs in an updated package, that can cause the
single node to not restart after a reboot. In this case, the update does not rollback automatically.

**Prerequisites for a cluster update**

**7.6.1.2**

You must satisfy the following prerequisites before updating a cluster using the CLI. ●Have access to the cluster as a user with admin privileges. See "Using RBAC to define and apply permissions" for more information. ●Have a recent etcd backup in case your update fails and you must restore your cluster to a previous state. Page 101 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Have a recent Container Storage Interface (CSI) volume snapshot in case you need to restore persistent volumes due to a pod failure. ●Your RHEL7 workers are replaced with RHEL8 or RHCOS workers. Red Hat does not support in-place RHEL7 to RHEL8 updates for RHEL workers; those hosts must be replaced with a clean operating system install. ●You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" for more information on how to check compatibility and, if necessary, update the installed Operators. ●Ensure that all machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy. ●If your cluster uses manually maintained credentials, update the cloud provider resources for the new release. For more information, including how to determine if this is a requirement for your cluster, see "Preparing to update a cluster with manually maintained credentials". ●Ensure that you address all Upgradeable=False conditions so the cluster allows an update to the next minor version. An alert displays at the top of the **Cluster**
**Settings** page when you have one or more cluster Operators that cannot be updated.
You can still update to the next available patch update for the minor release you are currently on. ●If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If minAvailable is set to 1 in PodDisruptionBudget, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the PodDisruptionBudget field can prevent the node drain.
**Important**:
●When an update is failing to complete, the Cluster Version Operator (CVO) reports the status of any blocking components while attempting to reconcile the update. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support. ●Using the unsupportedConfigOverrides section to modify the configuration of an Operator is unsupported and might block cluster updates. You must remove this setting before you can update your cluster.

**Pausing a MachineHealthCheck resource**

**7.6.1.3**

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the MachineHealthCheck resources might identify such nodes as unhealthy Page 102 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack and reboot them. To avoid rebooting worker nodes, you must pause all

| MachineHealthCheck |   |   | resource |   |
|---|---|---|---|---|
| e: Some MachineHealthCheck r MachineHealthCheck resourc |   | MachineHealthCheck |   |   |
|   | MachineHealthCheck |   |   | resourc |

**Note**: Some MachineHealthCheck resources might not need to be paused. If
your MachineHealthCheck resource relies on unrecoverable conditions, pausing that MHC is unnecessary.

**Prerequisites**

●You installed the OpenShift CLI (oc).

**Procedure**

1.List all of the available MachineHealthCheck resources that you want to pause by running the following command:

| $ oc get machinehealthcheck -n openshift-machine-api |   |   |
|---|---|---|
| 2. For each | MachineHealthCheck | resource, pause the machine health check by running |

the following command:

| $ oc -n openshift-machine-api annotate mhc <mhc name> cluster.x-k8s.io/paused="" _ |   |   |
|---|---|---|
| The annotated | MachineHealthCheck | resource resembles the following YAML file: |
| apiVersion: machine.openshift.io/v1beta1 |   |   |
| kind: MachineHealthCheck |   |   |
| metadata: |   |   |
| name: example |   |   |
| namespace: openshift-machine-api |   |   |
| annotations: |   |   |
| cluster.x-k8s.io/paused: "" |   |   |
| spec: |   |   |
| selector: |   |   |
| matchLabels: |   |   |
| role: worker |   |   |
| unhealthyConditions: |   |   |
| - type: "Ready" |   |   |
| status: "Unknown" |   |   |
| timeout: "300s" |   |   |
| - type: "Ready" |   |   |
| status: "False" |   |   |
| timeout: "300s" |   |   |
| maxUnhealthy: "40%" |   |   |
| status: |   |   |
| currentHealthy: 5 |   |   |
| expectedMachines: 5 |   |   |

**Important**: Resume the machine health checks after updating the cluster. To resume the
check, remove the pause annotation from the MachineHealthCheck resource by running the following command: $ oc -n openshift-machine-api annotate mhc <mhc-name> cluster.x-k8s.io/paused-

**Updating a cluster by using the CLI**

**7.6.1.4**

You can use the OpenShift CLI (oc) to review and request cluster updates. Page 103 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack You can find information about available OpenShift Container Platform advisories and updates in the errata section of the Customer Portal.

**Prerequisites**

●You installed the OpenShift CLI (oc) that matches the version for your updated version. ●You are logged in to the cluster as user with cluster-admin privileges. ●You have paused all MachineHealthCheck resources.

**Procedure**

1.View the available updates and note the version number of the update that you want to apply by running the following command: $ oc adm upgrade

**Example output**

Cluster version is 4.13.10 Upstream is unset, so the cluster will use an appropriate default. Channel: stable-4.13 (available channels: candidate-4.13, candidate-4.14, fast-4.13, stable-4.13) Recommended updates: VERSION IMAGE 4.13.14 quay.io/openshift-release-dev/ocprelease@sha256:406fcc160c097f61080412afcfa7fd65284ac8741ac7ad5b480e304aba73674b 4.13.13 quay.io/openshift-release-dev/ocprelease@sha256:d62495768e335c79a215ba56771ff5ae97e3cbb2bf49ed8fb3f6cefabcdc0f17 4.13.12 quay.io/openshift-release-dev/ocprelease@sha256:73946971c03b43a0dc6f7b0946b26a177c2f3c9d37105441315b4e3359373a55 4.13.11 quay.io/openshift-release-dev/ocprelease@sha256:e1c2377fdae1d063aaddc753b99acf25972b6997ab9a0b7e80cfef627b9ef3dd
**Note**:
●If there are no recommended updates, updates that have known issues might still be available. See Updating along a conditional update path for more information. ●For details and information on how to perform a Control Plane Only update, see "Performing a Control Plane Only update". 2.Based on your organization requirements, set the appropriate update channel by running the following command. For example, you can set your channel to stable- 4.13 or fast-4.13. For more information about channels, see "Understanding update channels and releases". $ oc adm upgrade channel <channel>

**Example command**

$ oc adm upgrade channel stable-4.18
**Important**: For production clusters, you must subscribe to a stable-*, eus-*, or fast-
* channel.
**Note**:
When you are ready to move to the next minor version, choose the channel that corresponds to that minor version. The sooner you declare the update channel, the more effectively the cluster can recommend update paths to your target version. The cluster might take some time to evaluate all the possible updates that are available and offer the best update recommendations to choose from. Update Page 104 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack recommendations can change over time, as they are based on what update options are available at the time. If you cannot see an update path to your target minor version, keep updating your cluster to the latest patch release for your current version until the next minor version is available in the path. 3.Apply an update: ●To update to the latest version, run the following command: $ oc adm upgrade --to-latest=true ●To update to a specific version, run the following command:

| $ oc adm upgrade --to=<version> |   |
|---|---|
| Replace | <version> |
| adm upgrade recommend |   |

**Important**: When using the oc adm upgrade --help command, there is a listed option for
the --force flag. This is heavily discouraged, because using the --force option bypasses cluster-side guards, including release verification and precondition checks. Using the -force flag does not guarantee a successful update. Bypassing guards puts the cluster at risk. 4.Review the status of the Cluster Version Operator by running the following command: $ oc adm upgrade 5.After the update completes, confirm that the cluster version has updated to the new version by running the following command: $ oc adm upgrade

**Example output**

Cluster version is <version> Upstream is unset, so the cluster will use an appropriate default. Channel: stable-<version> (available channels: candidate-<version>, eus-<version>, fast-<version>, stable-<version>) No updates available. You may force an update to a specific release image, but doing so might not be supported and might result in downtime or data loss. 6.If you are updating your cluster to the next minor version, such as version X.y to X.(y+1), confirm that your nodes are updated before deploying workloads that rely on a new feature. Run the following command: $ oc get nodes

**Example output**

NAME STATUS ROLES AGE VERSION ip-10-0-168-251.ec2.internal Ready master 82m v1.31.3 ip-10-0-170-223.ec2.internal Ready master 82m v1.31.3 ip-10-0-179-95.ec2.internal Ready worker 70m v1.31.3 ip-10-0-182-134.ec2.internal Ready worker 70m v1.31.3 ip-10-0-211-16.ec2.internal Ready master 82m v1.31.3 ip-10-0-250-100.ec2.internal Ready worker 69m v1.31.3 Page 105 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Finding recommended update paths with oc adm upgrade**

**7.6.1.5**

**recommend (Technology Preview)**

When updating your cluster, the oc adm upgrade command returns a list of the next available versions. You can use the oc adm upgrade recommend command to narrow down your suggestions and recommend a new target release before you launch your update. The oc adm upgrade recommend command is read-only and cannot alter the state of your cluster.
**Important**:
The oc adm upgrade recommend command is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see Technology Preview Features Support Scope.
**Note**: Your cluster does not need to be a Technology Preview-enabled cluster in order for
you to use the oc adm upgrade recommend command.

**Procedure**

1.Set the OC_ENABLE_CMD_UPGRADE_RECOMMEND environment variable to true by running the following command: $ export OC_ENABLE_CMD_UPGRADE_RECOMMEND=true 2.Run one of the following commands: ●To list the recommended versions for your update, run the oc adm upgrade

|   | recommend | command: |
|---|---|---|
| $ oc adm upgrade recommend |   |   |

**Example output**

Upstream is unset, so the cluster will use an appropriate default. Channel: stable-4.13 (available channels: candidate-4.12, candidate-4.13, eus-4.12, eus-4.14, fast-4.12, fast-4.13, stable-4.12, stable-4.13) Updates to 4.13: Version: 4.13.50 Image: quay.io/openshift-release-dev/ocprelease@sha256:6afb11e1cac46fd26476ca134072937115256b9c6360f7a1cd1812992c065f02 Reason: AdminAckRequired Message: Kubernetes 1.26 and therefore OpenShift 4.13 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/6958394 for details and instructions. Version: 4.13.49 Image: quay.io/openshift-release-dev/ocp- Page 106 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack release@sha256:ab6f574665395d809511db9dc57764358278538eaae248c6d199208b3c30ab7d Reason: AdminAckRequired Message: Kubernetes 1.26 and therefore OpenShift 4.13 remove several APIs which require admin consideration. Please see the knowledge article https://access.redhat.com/articles/6958394 for details and instructions. Updates to 4.12: VERSION ISSUES 4.12.64 no known issues 4.12.63 no known issues And 43 older 4.12 updates you can see with '--show-outdated-releases' or '--version VERSION'. ●To determine whether a specific version is recommended for your update, run the oc adm upgrade recommend --version command: $ oc adm upgrade recommend --version 4.12.51

**Example output**

Upstream is unset, so the cluster will use an appropriate default. Channel: stable-4.13 (available channels: candidate-4.12, candidate-4.13, eus-4.12, eus-4.14, fast-4.12, fast-4.13, stable-4.12, stable-4.13) Update to 4.12.51 Recommended=False: Image: quay.io/openshift-release-dev/ocprelease@sha256:158ced797e49f6caf7862acccef58484be63b642fdd2f66e6416295fa7958ab0 Release URL: https://access.redhat.com/errata/RHSA-2024:1052 Reason: MultipleReasons Message: An unintended reversion to the default kubelet nodeStatusReportFrequency can cause significant load on the control plane. https://issues.redhat.com/browse/MCO-1094 After rebooting into kernel-4.18.0-372.88.1.el8_6 or later, kernel nodes experience high load average and io_wait times. The nodes might fail to start or stop pods and probes may fail. Workload and host processes may become unresponsive and workload may be disrupted. https://issues.redhat.com/browse/COS-2705

**Gathering cluster update status using oc adm upgrade status**

**7.6.1.6**

**(Technology Preview)**

When updating your cluster, the oc adm upgrade command returns returns limited

| the | oc adm upgrade |   |
|---|---|---|
| oc adm upgrade |   | com |

information about the status of your update. You can use the oc adm upgrade status command to decouple status information from the oc adm upgrade command and return specific information regarding a cluster update, including the status of the control plane and worker node updates. The oc adm upgrade status command is read-only and does not alter any state in your cluster.
**Important**:
The oc adm upgrade status command is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not Page 107 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see Technology Preview Features Support Scope. The oc adm upgrade status command can be used for clusters from version 4.12 up to the latest supported release.
**Note**: Your cluster does not need to be a Technology Preview-enabled cluster in order for
you to use the oc adm upgrade status command.

**Procedure**

1.Set the OC_ENABLE_CMD_UPGRADE_STATUS environment variable to true by running the following command:

| $ export OC ENABLE CMD UPGRADE STATUS=true _ _ _ _ |   |   |
|---|---|---|
| 2. Run the | oc adm upgrade status | command: |
| $ oc adm upgrade status |   |   |

**Example output for an update progressing successfully**

= Control Plane = Assessment: Progressing Target Version: 4.17.1 (from 4.17.0) Updating: machine-config Completion: 97% (32 operators updated, 1 updating, 0 waiting) Duration: 54m (Est. Time Remaining: <10m) Operator Status: 32 Healthy, 1 Unavailable Control Plane Nodes NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-53-40.us-east-2.compute.internal Progressing Draining 4.17.0 +10m ip-10-0-30-217.us-east-2.compute.internal Outdated Pending 4.17.0 ? ip-10-0-92-180.us-east-2.compute.internal Outdated Pending 4.17.0 ? = Worker Upgrade = WORKER POOL ASSESSMENT COMPLETION STATUS worker Progressing 0% (0/2) 1 Available, 1 Progressing, 1 Draining infra Progressing 50% (1/2) 1 Available, 1 Progressing, 1 Draining Worker Pool Nodes: Worker NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-4-159.us-east-2.compute.internal Progressing Draining 4.17.0 +10m ip-10-0-99-40.us-east-2.compute.internal Outdated Pending 4.17.0 ? Worker Pool Nodes: infra NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-4-159-infra.us-east-2.compute.internal Progressing Draining 4.17.0 +10m Page 108 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ip-10-0-20-162.us-east-2.compute.internal Completed Updated 4.17.1 - = Update Health = SINCE LEVEL IMPACT MESSAGE 54m4s Info None Update is proceeding well

**Updating along a conditional update path**

**7.6.1.7**

You can update along a recommended conditional update path using the web console or the OpenShift CLI (oc). When a conditional update is not recommended for your cluster, you can update along a conditional update path using the OpenShift CLI (oc) 4.10 or later.

**Procedure**

1.To view the description of the update when it is not recommended because a risk might apply, run the following command: $ oc adm upgrade --include-not-recommended 2.If the cluster administrator evaluates the potential known risks and decides it is acceptable for the current cluster, then the administrator can waive the safety guards and proceed the update by running the following command:

| $ oc adm upgrade --allow-not-recommended --to <version> <.> |   |   |
|---|---|---|
| <.> | <version> | is the update version that you obtained from the output of the previous |

command, which is supported but also has known issues or risks.

**Changing the update server by using the CLI**

**7.6.1.8**

You can change the update server your cluster uses to retrieve information about update paths. Changing the update server is optional. If you have an OpenShift Update Service (OSUS) installed and configured locally, you must set the URL for the server as the upstream to use the local server during updates. The default value for upstream is https://api.openshift.com/api/upgrades_info/v1/graph.

**Procedure**

●Change the upstream parameter value in the cluster version by running the following command:

| $ oc patch clusterversion/version --patch '{"spec":{"upstream":"<update server url>"}}' --type=merge _ _ |   |   |
|---|---|---|
| Replace | <update server url> _ _ | with the URL for the update server. |

**Example output**

clusterversion.config.openshift.io/version patched

**Updating a cluster using the web console**

**7.6.2**

You can perform minor version and patch updates on an OpenShift Container Platform cluster by using the web console.
**Note**: Use the web console or oc adm upgrade channel <channel> to change the update
channel. You can follow the steps in Updating a cluster using the CLI to complete the update after you change to a 4.18 channel. Page 109 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Before updating the OpenShift Container Platform cluster**

**7.6.2.1**

Before updating your cluster, you must consider several factors in order to improve the chances of performing a successful update. Consider the following information: ●Whether you have recently backed up etcd. ●In PodDisruptionBudget, if minAvailable is set to 1, the nodes are drained to apply pending machine configs that might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the PodDisruptionBudget field can prevent the node drain. ●You might need to update the cloud provider resources for the new release if your cluster uses manually maintained credentials. ●You must review administrator acknowledgement requests, take any recommended actions, and provide the acknowledgement when you are ready. ●You can perform a partial update by updating the worker or custom pool nodes to accommodate the time it takes to update. You can pause and resume within the progress bar of each pool.
**Important**:
●When an update is failing to complete, the Cluster Version Operator (CVO) reports the status of any blocking components while attempting to reconcile the update. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support. ●Using the unsupportedConfigOverrides section to modify the configuration of an Operator is unsupported and might block cluster updates. You must remove this setting before you can update your cluster.

**Changing the update server by using the web console**

**7.6.2.2**

You can change the update server your cluster uses to retrieve information about update paths. Changing the update server is optional. If you have an OpenShift Update Service (OSUS) installed and configured locally, you must set the URL for the server as the upstream to use the local server during updates.

**Prerequisites**

●You have access to the cluster with cluster-admin privileges. ●You have access to the OpenShift Container Platform web console.

**Procedure**

1.On the web console, navigate to **Administration** → **Cluster Settings** and click **version**. 2.Click the **YAML** tab and then edit the upstream parameter value:

**Example YAML snippet**

... spec: clusterID: db93436d-7b05-42cc-b856-43e11ad2d31a Page 110 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack upstream: '<update_server_url>' ... Replace <update_server_url> with the URL for the update server. The default upstream value is https://api.openshift.com/api/upgrades_info/v1/graph. 3.Click **Save**.

**Pausing a MachineHealthCheck resource by using the web console**

**7.6.2.3**

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the machine health check might identify such nodes as unhealthy and reboot them. To avoid rebooting such nodes, pause all the MachineHealthCheck resources before updating the cluster.

**Prerequisites**

●You have access to the cluster with cluster-admin privileges. ●You have access to the OpenShift Container Platform web console.

**Procedure**

1.On the web console, navigate to **Compute** → **MachineHealthChecks**.

| each | MachineHealthCheck |   | resource, pause the m annotation to the res |
|---|---|---|---|
| cluster.x-k8s.io/paused="" |   |   |   |
| otation to the |   | machine-api-termination-handler |   |

steps: a.Click the Options menu with **3-dot** logo next to the machine-api-terminationhandler and click **Edit annotations**. b.In the **Edit annotations** dialog, click **Add more**. c. In the **Key** and **Value** fields, add cluster.x-k8s.io/paused and "" values, respectively, and click **Save**.

**Updating a cluster by using the web console**

**7.6.2.4**

If updates are available, you can update your cluster from the web console. You can find information about available OpenShift Container Platform advisories and updates in the errata section of the Customer Portal.

**Prerequisites**

●Have access to the web console as a user with cluster-admin privileges. ●You have access to the OpenShift Container Platform web console. ●Pause all MachineHealthCheck resources. ●You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default OperatorHub catalogs switch from the current minor version to the next during a cluster update. ●Your machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy. Page 111 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Your RHEL7 workers are replaced with RHEL8 or RHCOS workers. Red Hat does not support in-place RHEL7 to RHEL8 updates for RHEL workers; those hosts must be replaced with a clean operating system install.

**Procedure**

1.From the web console, click **Administration** → **Cluster Settings** and review the contents of the **Details** tab. 2.For production clusters, ensure that the **Channel** is set to the correct channel for the version that you want to update to, such as stable-4.18.
**Important**: For production clusters, you must subscribe to a stable-*, eus-* or fast-
* channel.
**Note**:
When you are ready to move to the next minor version, choose the channel that corresponds to that minor version. The sooner you declare the update channel, the more effectively the cluster can recommend update paths to your target version. The cluster might take some time to evaluate all the possible updates that are available and offer the best update recommendations to choose from. Update recommendations can change over time, as they are based on what update options are available at the time. If you cannot see an update path to your target minor version, keep updating your cluster to the latest patch release for your current version until the next minor version is available in the path. If the **Update status** is not **Updates available**, you cannot update your cluster.
**Select channel** indicates the cluster version that your cluster is running or is updating to.
3.Select a version to update to, and click **Save**. The Input channel **Update status** changes to **Update to <product-version> in progress**, and you can review the progress of the cluster update by watching the progress bars for the Operators and nodes.
**Note**: If you are updating your cluster to the next minor version, for example from version
4.10 to 4.11, confirm that your nodes are updated before deploying workloads that rely on a new feature. Any pools with worker nodes that are not yet updated are displayed on the **Cluster Settings** page. 4.After the update completes and the Cluster Version Operator refreshes the available updates, check if more updates are available in your current channel. ●If updates are available, continue to perform updates in the current channel until you can no longer update. ●If no updates are available, change the **Channel** to the stable-*, eus-* or fast-
* channel for the next minor version, and update to the version that you want in that
channel. You might need to perform several intermediate updates until you reach the version that you want. Page 112 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Viewing conditional updates in the web console**

**7.6.2.5**

You can view and assess the risks associated with particular updates with conditional updates.

**Prerequisites**

●You have access to the cluster with cluster-admin privileges. ●You have access to the OpenShift Container Platform web console. ●Pause all MachineHealthCheck resources. ●You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default OperatorHub catalogs switch from the current minor version to the next during a cluster update. ●Your machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing an advanced update strategy, such as a canary rollout, an EUS update, or a control-plane update.

**Procedure**

1.From the web console, click **Administration** → **Cluster settings** page and review the contents of the **Details** tab. 2.You can enable the Include versions with known issues feature in the **Select new**
**version** dropdown of the **Update cluster** modal to populate the dropdown list with
conditional updates.
**Note**: If a version with known issues is selected, more information is provided with
potential risks that are associated with the version. 3.Review the notification detailing the potential risks to updating.

**Performing a canary rollout update**

**7.6.2.6**

In some specific use cases, you might want a more controlled update process where you do not want specific nodes updated concurrently with the rest of the cluster. These use cases include, but are not limited to the following situations: ●You have mission-critical applications that you do not want unavailable during the update. You can slowly test the applications on your nodes in small batches after the update. ●You have a small maintenance window that does not allow the time for all nodes to be updated, or you have multiple maintenance windows. The rolling update process is not a typical update workflow. With larger clusters, it can be a time-consuming process that requires you execute multiple commands. This complexity can result in errors that can affect the entire cluster. It is recommended that you carefully consider whether your organization wants to use a rolling update and carefully plan the implementation of the process before you start. The rolling update process described in this topic involves: ●Creating one or more custom machine config pools (MCPs). Page 113 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Labeling each node that you do not want to update immediately to move those nodes to the custom MCPs. ●Pausing those custom MCPs, which prevents updates to those nodes. ●Performing the cluster update. ●Unpausing one custom MCP, which triggers the update on those nodes. ●Testing the applications on those nodes to make sure the applications work as expected on those newly-updated nodes. ●Optionally removing the custom labels from the remaining nodes in small batches and testing the applications on those nodes.
**Note**: Pausing an MCP should be done with careful consideration and for short periods of
time only. If you want to use the canary rollout update process, see "Performing a canary rollout update".

**About updating single node OpenShift Container Platform**

**7.6.2.7**

You can update a single-node OpenShift Container Platform cluster by using either the console or CLI. However, note the following limitations: ●The prerequisite to pause the MachineHealthCheck resources is not required because there is no other node to perform the health check. ●Restoring a single-node OpenShift Container Platform cluster using an etcd backup is not officially supported. However, it is good practice to perform the etcd backup in case your update fails. If your control plane is healthy, you might be able to restore your cluster to a previous state by using the backup. ●Updating a single-node OpenShift Container Platform cluster requires downtime and can include an automatic reboot. The amount of downtime depends on the update payload, as described in the following scenarios: ○If the update payload contains an operating system update, which requires a reboot, the downtime is significant and impacts cluster management and user workloads. ○If the update contains machine configuration changes that do not require a reboot, the downtime is less, and the impact on the cluster management and user workloads is lessened. In this case, the node draining step is skipped with singlenode OpenShift Container Platform because there is no other node in the cluster to reschedule the workloads to. ○If the update payload does not contain an operating system update or machine configuration changes, a short API outage occurs and resolves quickly.
**Important**: There are conditions, such as bugs in an updated package, that can cause the
single node to not restart after a reboot. In this case, the update does not rollback automatically. Page 114 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Performing a Control Plane Only update**

**7.6.3**

Due to fundamental Kubernetes design, all OpenShift Container Platform updates between minor versions must be serialized. You must update from OpenShift Container Platform <4.y> to <4.y+1>, and then to <4.y+2>. You cannot update from OpenShift Container Platform <4.y> to <4.y+2> directly. However, administrators who want to update between two even-numbered minor versions can do so incurring only a single reboot of noncontrol plane hosts.
**Important**: This update was previously known as an **EUS-to-EUS** update and is now
referred to as a **Control Plane Only** update. These updates are only viable between **even-**
**numbered minor versions** of OpenShift Container Platform.
There are several caveats to consider when attempting a Control Plane Only update. ●Control Plane Only updates are only offered after updates between all versions involved have been made available in stable channels. ●If you encounter issues during or after updating to the odd-numbered minor version but before updating to the next even-numbered version, then remediation of those issues may require that non-control plane hosts complete the update to the oddnumbered version before moving forward. ●You can do a partial update by updating the worker or custom pool nodes to accommodate the time it takes for maintenance. ●Until the machine config pools are unpaused and the update is complete, some features and bugs fixes in <4.y+1> and <4.y+2> of OpenShift Container Platform are not available. ●All the clusters might update using EUS channels for a conventional update without pools paused, but only clusters with non control-plane MachineConfigPools objects can do Control Plane Only updates with pools paused.

**Performing a Control Plane Only update**

**7.6.3.1**

The following procedure pauses all non-master machine config pools and performs updates from OpenShift Container Platform <4.y> to <4.y+1> to <4.y+2>, then unpauses the machine config pools. Following this procedure reduces the total update duration and the number of times worker nodes are restarted.

**Prerequisites**

●Review the release notes for OpenShift Container Platform <4.y+1> and <4.y+2>. ●Review the release notes and product lifecycles for any layered products and Operator Lifecycle Manager (OLM) Operators. Some products and OLM Operators might require updates either before or during a Control Plane Only update. ●Ensure that you are familiar with version-specific prerequisites, such as the removal of deprecated APIs, that are required before updating from OpenShift Container Platform <4.y+1> to <4.y+2>. ●If your cluster uses in-tree vSphere volumes, update vSphere to version 7.0u3L+ or 8.0u2+. Page 115 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.6.3.1.1Control Plane Only update using the web console**

**Prerequisites**

●Verify that machine config pools are unpaused. ●Have access to the web console as a user with admin privileges.

**Procedure**

1.Using the Administrator perspective on the web console, update any Operator Lifecycle Manager (OLM) Operators to the versions that are compatible with your intended updated version. You can find more information on how to perform this action in "Updating installed Operators". 2.Verify that all machine config pools display a status of Up to date and that no machine config pool displays a status of UPDATING. To view the status of all machine config pools, click **Compute** → **MachineConfigPools** and review the contents of the **Update**
**status** column.
**Note**: If your machine config pools have an Updating status, please wait for this status to
change to Up to date. This process could take several minutes. 3.Set your channel to eus-<4.y+2>. To set your channel, click **Administration** → **Cluster Settings** → **Channel**. You can edit your channel by clicking on the current hyperlinked channel. 4.Pause all worker machine pools except for the master pool. You can perform this action on the **MachineConfigPools** tab under the **Compute** page. Select the vertical ellipses next to the machine config pool you’d like to pause and click **Pause updates**. 5.Update to version <4.y+1> and complete up to the **Save** step. You can find more information on how to perform these actions in "Updating a cluster by using the web console"; 6.Ensure that the <4.y+1> updates are complete by viewing the **Last completed**
**version** of your cluster. You can find this information on the **Cluster Settings** page
under the **Details** tab. 7.If necessary, update your OLM Operators by using the Administrator perspective on the web console. You can find more information on how to perform these actions in "Updating installed Operators". 8.Update to version <4.y+2> and complete up to the **Save** step. You can find more information on how to perform these actions in "Updating a cluster by using the web console". 9.Ensure that the <4.y+2> update is complete by viewing the **Last completed**
**version** of your cluster. You can find this information on the **Cluster Settings** page
under the **Details** tab. 10.Unpause all previously paused machine config pools. You can perform this action on the **MachineConfigPools** tab under the **Compute** page. Select the vertical ellipses next to the machine config pool you’d like to unpause and click **Unpause updates**. Page 116 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
**Important**: If pools are paused, the cluster is not permitted to upgrade to any future minor
versions, and some maintenance tasks are inhibited. This puts the cluster at risk for future degradation. 11.Verify that your previously paused pools are updated and that your cluster has completed the update to version <4.y+2>. You can verify that your pools have updated on the **MachineConfigPools** tab under the **Compute** page by confirming that the **Update status** has a value of **Up to date**.
**Important**: When you update a cluster that contains Red Hat Enterprise Linux (RHEL)
compute machines, those machines temporarily become unavailable during the update process. You must run the upgrade playbook against each RHEL machine as it enters the NotReady state for the cluster to finish updating. You can verify that your cluster has completed the update by viewing the **Last completed**
**version** of your cluster. You can find this information on the **Cluster Settings** page under
the **Details** tab.

**7.6.3.1.2Control Plane Only update using the CLI**

**Prerequisites**

●Verify that machine config pools are unpaused. ●Update the OpenShift CLI (oc) to the target version before each update.
**Important**: It is highly discouraged to skip this prerequisite. If the OpenShift CLI (oc) is not
updated to the target version before your update, unexpected issues may occur.

**Procedure**

1.Using the Administrator perspective on the web console, update any Operator Lifecycle Manager (OLM) Operators to the versions that are compatible with your intended updated version. You can find more information on how to perform this action in "Updating installed Operators". 2.Verify that all machine config pools display a status of UPDATED and that no machine config pool displays a status of UPDATING. To view the status of all machine config pools, run the following command: $ oc get mcp

**Example output**

NAME CONFIG UPDATED UPDATING master rendered-master-ecbb9582781c1091e1c9f19d50cf836c True False worker rendered-worker-00a3f0c68ae94e747193156b491553d5 True False 3.Your current version is <4.y>, and your intended version to update is <4.y+2>.

| Change to the | eus-<4.y+2> | channel by running the following command: |   |   |
|---|---|---|---|---|
| $ oc adm upgrade channel eus-<4.y+2> |   |   |   |   |
| Note: If you receive an error message indicating that |   |   | eus-<4.y+2> | is not one of the |

available channels, this indicates that Red Hat is still rolling out EUS version updates. This rollout process generally takes 45-90 days starting at the GA date. 4.Pause all worker machine pools except for the master pool by running the following command: $ oc patch mcp/worker --type merge --patch '{"spec":{"paused":true}}' Page 117 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
**Note**: You cannot pause the master pool.
5.Update to the latest version by running the following command: $ oc adm upgrade --to-latest

**Example output**

Updating to latest version <4.y+1.z> 6.Review the cluster version to ensure that the updates are complete by running the following command: $ oc adm upgrade

**Example output**

Cluster version is <4.y+1.z> ... 7.Update to version <4.y+2> by running the following command: $ oc adm upgrade --to-latest 8.Retrieve the cluster version to ensure that the <4.y+2> updates are complete by running the following command: $ oc adm upgrade

**Example output**

Cluster version is <4.y+2.z> ... 9.To update your worker nodes to <4.y+2>, unpause all previously paused machine config pools by running the following command: $ oc patch mcp/worker --type merge --patch '{"spec":{"paused":false}}'
**Important**: If pools are not unpaused, the cluster is not permitted to update to any future
minor versions, and some maintenance tasks are inhibited. This puts the cluster at risk for future degradation. 10.Verify that your previously paused pools are updated and that the update to version <4.y+2> is complete by running the following command: $ oc get mcp
**Important**: When you update a cluster that contains Red Hat Enterprise Linux (RHEL)
compute machines, those machines temporarily become unavailable during the update process. You must run the upgrade playbook against each RHEL machine as it enters the NotReady state for the cluster to finish updating.

**Example output**

NAME CONFIG UPDATED UPDATING master rendered-master-52da4d2760807cb2b96a3402179a9a4c True False worker rendered-worker-4756f60eccae96fb9dcb4c392c69d497 True False

**7.6.3.1.3Control Plane Only updates for layered products and Operators installed**

**through Operator Lifecycle Manager**

In addition to the Control Plane Only update steps mentioned for the web console and CLI, there are additional steps to consider when performing Control Plane Only updates for clusters with the following: ●Layered products ●Operators installed through Operator Lifecycle Manager (OLM) Page 118 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**What is a layered product?**

Layered products refer to products that are made of multiple underlying products that are intended to be used together and cannot be broken into individual subscriptions. For examples of layered OpenShift Container Platform products, see Layered Offering On OpenShift. As you perform a Control Plane Only update for the clusters of layered products and those of Operators that have been installed through OLM, you must complete the following: 1.You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default OperatorHub catalogs switch from the current minor version to the next during a cluster update. 2.Confirm the cluster version compatibility between the current and intended Operator versions. You can verify which versions your OLM Operators are compatible with by using the Red Hat OpenShift Container Platform Operator Update Information Checker. As an example, here are the steps to perform a Control Plane Only update from <4.y> to <4.y+2> for 'OpenShift Data Foundation'. This can be done through the CLI or web console. For information about how to update clusters through your desired interface, see Control Plane Only update using the web console.

**Example workflow**

1.Pause the worker machine pools. 2.Update OpenShift <4.y> → OpenShift <4.y+1>. 3.Update ODF <4.y> → ODF <4.y+1>. 4.Update OpenShift <4.y+1> → OpenShift <4.y+2>. 5.Update to ODF <4.y+2>. 6.Unpause the worker machine pools.
**Note**: The update to ODF <4.y+2> can happen before or after worker machine pools have
been unpaused.

**Performing a canary rollout update**

**7.6.4**

For a more controlled rollout of worker node updates, you can use a canary update. A canary update is an update strategy where worker node updates are performed in discrete, sequential stages instead of updating all worker nodes at the same time. This strategy can be useful in the following scenarios: ●You want a more controlled rollout of worker node updates to ensure that missioncritical applications stay available during the entire update, even if the update process causes your applications to fail. ●You want to update a small subset of worker nodes, evaluate cluster and workload health over a period of time, and then update the remaining nodes. ●You want to fit worker node updates, which often require a host reboot, into smaller defined maintenance windows when it is not possible to take a large maintenance window to update the entire cluster at one time. Page 119 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack In these scenarios, you can create multiple custom machine config pools (MCPs) to prevent certain worker nodes from updating when you update the cluster. After the rest of the cluster is updated, you can update those worker nodes in batches at appropriate times.

**Example Canary update strategy**

**7.6.4.1**

To better understand how the canary rollout strategy works, it is useful to consider an example of an update using the strategy. The following example describes a canary update strategy where you have a cluster with 100 nodes with 10% excess capacity, you have maintenance windows that must not exceed 4 hours, and you know that it takes no longer than 8 minutes to drain and reboot a worker node.
**Note**: The previous values are an example only. The time it takes to drain a node might
vary depending on factors such as workloads.

**7.6.4.1.1Definition of custom machine config pools**

In order to organize the worker node updates into separate stages, you can begin by defining the following machine config pools: ●**workerpool-canary** with 10 nodes ●**workerpool-A** with 30 nodes ●**workerpool-B** with 30 nodes ●**workerpool-C** with 30 nodes

**7.6.4.1.2Update of the canary worker pool**

During your first maintenance window, you pause the machine config pools (MCPs) for **workerpool-A**, **workerpool-B**, and **workerpool-C**, and then initiate the cluster update. This updates components that run on top of OpenShift Container Platform and the 10 nodes that are part of the unpaused **workerpool-canary** MCP. The other three MCPs are not updated because they were paused.

**7.6.4.1.3Whether or not to proceed with the remaining worker pool updates**

If for some reason you determine that your cluster or workload health was negatively affected by the **workerpool-canary** update, you then cordon and drain all nodes in that pool while still maintaining sufficient capacity until you have diagnosed and resolved the problem. When everything is working as expected, you evaluate the cluster and workload health before deciding to unpause, and thus update, **workerpool-A**, **workerpool-B**, and **workerpool-C** in succession during each additional maintenance window. Managing worker node updates using custom machine config pools (MCPs) provides flexibility, however it can be a time-consuming process that requires you execute multiple commands. This complexity can result in errors that might affect the entire cluster. It is recommended that you carefully consider your organizational needs and carefully plan the implementation of the process before you start. Page 120 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
**Important**:
Pausing a machine config pool prevents the Machine Config Operator from applying any configuration changes on the associated nodes. Pausing an MCP also prevents any automatically rotated certificates from being pushed to the associated nodes, including the automatic CA rotation of the kube-apiserver-to-kubelet-signer CA certificate. If the MCP is paused when the kube-apiserver-to-kubelet-signer CA certificate expires and the MCO attempts to automatically renew the certificate, the MCO cannot push the newly rotated certificates to those nodes. This causes failure in multiple oc commands, including oc debug, oc logs, oc exec, and oc attach. You receive alerts in the Alerting UI of the OpenShift Container Platform web console if an MCP is paused when the certificates are rotated. Pausing an MCP should be done with careful consideration about the kube-apiserverto-kubelet-signer CA certificate expiration and for short periods of time only.
**Note**: It is not recommended to update the MCPs to different OpenShift Container
Platform versions. For example, do not update one MCP from 4.y.10 to 4.y.11 and another to 4.y.12. This scenario has not been tested and might result in an undefined cluster state.

**About the canary rollout update process and MCPs**

**7.6.4.2**

In OpenShift Container Platform, nodes are not considered individually. Instead, they are grouped into machine config pools (MCPs). By default, nodes in an OpenShift Container Platform cluster are grouped into two MCPs: one for the control plane nodes and one for the worker nodes. An OpenShift Container Platform update affects all MCPs concurrently. During the update, the Machine Config Operator (MCO) drains and cordons all nodes

| the specified | maxUnavailable |   |   |   |
|---|---|---|---|---|
| maxUnavailable |   | is set to | 1. | D |

deschedules all pods on the node and marks the node as unschedulable. After the node is drained, the Machine Config Daemon applies a new machine configuration, which can include updating the operating system (OS). Updating the OS requires the host to reboot.

**7.6.4.2.1Using custom machine config pools**

To prevent specific nodes from being updated, you can create custom MCPs. Because the MCO does not update nodes within paused MCPs, you can pause the MCPs containing nodes that you do not want to update before initiating a cluster update. Using one or more custom MCPs can give you more control over the sequence in which you update your worker nodes. For example, after you update the nodes in the first MCP, you can verify the application compatibility and then update the rest of the nodes gradually to the new version. Page 121 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool.
**Note**: To ensure the stability of the control plane, creating a custom MCP from the control
plane nodes is not supported. The Machine Config Operator (MCO) ignores any custom MCP created for the control plane nodes.

**7.6.4.2.2Considerations when using custom machine config pools**

Give careful consideration to the number of MCPs that you create and the number of nodes in each MCP, based on your workload deployment topology. For example, if you must fit updates into specific maintenance windows, you must know how many nodes OpenShift Container Platform can update within a given window. This number is dependent on your unique cluster and workload characteristics. You must also consider how much extra capacity is available in your cluster to determine the number of custom MCPs and the amount of nodes within each MCP. In a case where your applications fail to work as expected on newly updated nodes, you can cordon and drain those nodes in the pool, which moves the application pods to other nodes. However, you must determine whether the available nodes in the remaining MCPs can provide sufficient quality-of-service (QoS) for your applications.
**Note**: You can use this update process with all documented OpenShift Container Platform
update processes. However, the process does not work with Red Hat Enterprise Linux (RHEL) machines, which are updated using Ansible playbooks.

**About performing a canary rollout update**

**7.6.4.3**

The process of a canary update can be understood as several high-level steps. The following steps outline the high-level workflow of the process: 1.Create custom machine config pools (MCP) based on the worker pool.
**Note**: You can change the maxUnavailable setting in an MCP to specify the percentage or
the number of machines that can be updating at any given time. The default is 1.
**Warning**: The default setting for maxUnavailable is 1 for all the machine config pools in
OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to 3 for the control plane pool. 2.Add a node selector to the custom MCPs. For each node that you do not want to update simultaneously with the rest of the cluster, add a matching label to the nodes. This label associates the node to the MCP.
**Important**: Do not remove the default worker label from the nodes. The nodes must have
a role label to function properly in the cluster. 3.Pause the MCPs you do not want to update as part of the update process. 4.Perform the cluster update. The update process updates the MCPs that are not paused, including the control plane nodes. 5.Test your applications on the updated nodes to ensure they are working as expected. Page 122 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack 6.Unpause one of the remaining MCPs, wait for the nodes in that pool to finish updating, and test the applications on those nodes. Repeat this process until all worker nodes are updated. 7.Optional: Remove the custom label from updated nodes and delete the custom MCPs.

**Creating machine config pools to perform a canary rollout update**

**7.6.4.4**

To perform a canary rollout update, you must first create one or more custom machine config pools (MCP).

**Procedure**

1.List the worker nodes in your cluster by running the following command: $ oc get -l 'node-role.kubernetes.io/master!=' -o 'jsonpath={range .items[*]}{.metadata.name}{"\n"}{end}' nodes

**Example output**

ci-ln-pwnll6b-f76d1-s8t9n-worker-a-s75z4 ci-ln-pwnll6b-f76d1-s8t9n-worker-b-dglj2 ci-ln-pwnll6b-f76d1-s8t9n-worker-c-lldbm 2.For each node that you want to delay, add a custom label to the node by running the following command: $ oc label node <node_name> node-role.kubernetes.io/<custom_label>= For example: $ oc label node ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz node-role.kubernetes.io/workerpoolcanary=

**Example output**

node/ci-ln-gtrwm8t-f76d1-spbl7-worker-a-xk76k labeled 3.Create the new MCP: a.Create an MCP YAML file: apiVersion: machineconfiguration.openshift.io/v1 kind: MachineConfigPool metadata: name: workerpool-canary spec: machineConfigSelector: matchExpressions:
  - {
key: machineconfiguration.openshift.io/role, operator: In, values: [worker,workerpool-canary] } nodeSelector: matchLabels: node-role.kubernetes.io/workerpool-canary: "" where:

**metadata.name**

Specifies a name for the MCP.

**spec.machineConfigSelector.matchExpressions.values**

Page 123 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| Specifies the | worker | and custom MCP name. |
|---|---|---|
| spec.nodeSelectormatchLabels.node-role.kubernetes.io/workerpool-canary |   |   |

Specifies the custom label you added to the nodes that you want in this pool.

| b. Create the | MachineConfigPool | object by running the following command: |
|---|---|---|
| $ oc create -f <file name> _ |   |   |

**Example output**

machineconfigpool.machineconfiguration.openshift.io/workerpool-canary created 4.View the list of MCPs in the cluster and their current state by running the following command: $ oc get machineconfigpool

**Example output**

| NAME CONFIG |   |   |
|---|---|---|
| UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT |   |   |
| UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE |   |   |
| master rendered-master-b0bb90c4921860f2a5d8a2f8137c1867 True |   |   |
| False False 3 3 3 0 |   |   |
| 97m |   |   |
| workerpool-canary rendered-workerpool-canary-87ba3dec1ad78cb6aecebf7fbb476a36 True |   |   |
| False False 1 1 1 0 |   |   |
| 2m42s |   |   |
| worker rendered-worker-87ba3dec1ad78cb6aecebf7fbb476a36 True |   |   |
| False False 2 2 2 0 |   |   |
| 97m |   |   |
| The new machine config pool, | workerpool-canary | , is created and the number of nodes to |

which you added the custom label are shown in the machine counts. The worker MCP machine counts are reduced by the same number. It can take several minutes to update the machine counts. In this example, one node was moved from the worker MCP to the workerpool-canary MCP.

**Managing machine configuration inheritance for a worker pool**

**7.6.4.5**

**canary**

You can configure a machine config pool (MCP) canary to inherit any MachineConfig assigned to an existing MCP. This configuration is useful when you want to use an MCP canary to test as you update nodes one at a time for an existing MCP.

**Prerequisites**

●You have created one or more MCPs.

**Procedure**

1.Create a secondary MCP as described in the following two steps: a.Save the following configuration file as machineConfigPool.yaml.

| Example | machineConfigPool | YAML |
|---|---|---|
| apiVersion: machineconfiguration.openshift.io/v1 |   |   |
| kind: MachineConfigPool |   |   |
| metadata: |   |   |
| name: worker-perf |   |   |

Page 124 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack spec: machineConfigSelector: matchExpressions:
  - {
key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker-perf] } nodeSelector: matchLabels: node-role.kubernetes.io/worker-perf: ""
# ...
b.Create the new machine config pool by running the following command: $ oc create -f machineConfigPool.yaml

**Example output**

machineconfigpool.machineconfiguration.openshift.io/worker-perf created 2.Add some machines to the secondary MCP. The following example labels the worker

| nodes | worker-a |   | , | worker-b | , and |   | worker-c | to the MCP |   | worker-perf | : |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $ oc label node worker-a node-role.kubernetes.io/worker-perf='' |   |   |   |   |   |   |   |   |   |   |   |
| $ oc label node worker-b node-role.kubernetes.io/worker-perf='' |   |   |   |   |   |   |   |   |   |   |   |
| $ oc label node worker-c node-role.kubernetes.io/worker-perf='' |   |   |   |   |   |   |   |   |   |   |   |
| 3. Create a new |   | MachineConfig |   |   |   | for the MCP |   |   | worker-perf | as described in the following |   |

two steps:

| a. Save the following MachineConfig example as a file called new-machineconfig.yaml: Example MachineConfig YAML |   |   |
|---|---|---|
| apiVersion: machineconfiguration.openshift.io/v1 |   |   |
| kind: MachineConfig |   |   |
| metadata: |   |   |
| labels: |   |   |
| machineconfiguration.openshift.io/role: worker-perf |   |   |
| name: 06-kdump-enable-worker-perf |   |   |
| spec: |   |   |
| config: |   |   |
| ignition: |   |   |
| version: 3.2.0 |   |   |
| systemd: |   |   |
| units: |   |   |
| - enabled: true |   |   |
| name: kdump.service |   |   |
| kernelArguments: |   |   |
| - crashkernel=512M |   |   |
| # ... |   |   |
| b. Apply the | MachineConfig | by running the following command: |
| $ oc create -f new-machineconfig.yaml |   |   |

4.Create the new canary MCP and add machines from the MCP you created in the previous steps. The following example creates an MCP called worker-perf-canary, and adds machines from the worker-perf MCP that you previosuly created. Page 125 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| a. Label the canary worker node | worker-a |   | by running the following command: |   |
|---|---|---|---|---|
| $ oc label node worker-a node-role.kubernetes.io/worker-perf-canary='' |   |   |   |   |
| b. Remove the canary worker node |   | worker-a |   | from the original MCP by running the |

following command: $ oc label node worker-a node-role.kubernetes.io/worker-perfc. Save the following file as machineConfigPool-Canary.yaml.

**Example machineConfigPool-Canary.yaml file**

apiVersion: machineconfiguration.openshift.io/v1 kind: MachineConfigPool metadata: name: worker-perf-canary spec: machineConfigSelector: matchExpressions:
  - {
key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker-perf,worker-perf-canary] } nodeSelector: matchLabels: node-role.kubernetes.io/worker-perf-canary: "" where:

**spec.machineConfigSelector.matchExpressions.values**

Specifies a value you can use to configure members of an additional MachineConfig. This example includes worker-perf-canary as an additional value. This is an optional value. d.Create the new worker-perf-canary by running the following command: $ oc create -f machineConfigPool-Canary.yaml

**Example output**

| machineconfigpool.machineconfiguration.openshift.io/worker-perf-canary created |   |   |   |   |
|---|---|---|---|---|
| 5. Check if the | MachineConfig | is inherited in | worker-perf-canary | . |

a.Verify that no MCP is degraded by running the following command: $ oc get mcp

**Example output**

NAME CONFIG UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE master rendered-master-2bf1379b39e22bae858ea1a3ff54b2ac True False False 3 3 3 0 5d16h worker rendered-worker-b9576d51e030413cfab12eb5b9841f34 True False False 0 0 0 0 5d16h worker-perf rendered-worker-perf-b98a1f62485fa702c4329d17d9364f6a True False False 2 2 2 0 56m worker-perf-canary rendered-worker-perf-canary-b98a1f62485fa702c4329d17d9364f6a True Page 126 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| False False 1 1 1 0 |   |   |   |   |
|---|---|---|---|---|
| 44m |   |   |   |   |
| b. Verify that the machines are inherited from | worker-perf | into | worker-perf-canary | . |
| $ oc get nodes |   |   |   |   |

**Example output**

| NAME STATUS ROLES AGE VERSION |   |   |   |   |
|---|---|---|---|---|
| ... |   |   |   |   |
| worker-a Ready worker,worker-perf-canary 5d15h v1.27.13+e709aa5 |   |   |   |   |
| worker-b Ready worker,worker-perf 5d15h v1.27.13+e709aa5 |   |   |   |   |
| worker-c Ready worker,worker-perf 5d15h v1.27.13+e709aa5 |   |   |   |   |
| c. Verify that | kdump | service is enabled on | worker-a | by running the following command: |
| $ systemctl status kdump.service |   |   |   |   |

**Example output**

| NAME STATUS ROLES AGE VERSION |   |   |   |
|---|---|---|---|
| ... |   |   |   |
| kdump.service - Crash recovery kernel arming |   |   |   |
| Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; preset: disabled) |   |   |   |
| Active: active (exited) since Tue 2024-09-03 12:44:43 UTC; 10s ago |   |   |   |
| Process: 4151139 ExecStart=/usr/bin/kdumpctl start (code=exited, status=0/SUCCESS) |   |   |   |
| Main PID: 4151139 (code=exited, status=0/SUCCESS) |   |   |   |
| d. Verify that the MCP has updated the |   | crashkernel | by running the following command: |
| $ cat /proc/cmdline |   |   |   |
| The output should include the updated | crashekernel |   | value, for example: |

**Example output**

| crashkernel=512M |   |   |
|---|---|---|
| 6. Optional: If you are satisfied with the upgrade, you can return worker-a to worker- perf. a. Return worker-a to worker-perf by running the following command: |   |   |
| $ oc label node worker-a node-role.kubernetes.io/worker-perf='' |   |   |
| b. Remove | worker-a | from the canary MCP by running the following command: |
| $ oc label node worker-a node-role.kubernetes.io/worker-perf-canary- |   |   |

**Pausing the machine config pools**

**7.6.4.6**

After you create your custom machine config pools (MCPs), you then pause those MCPs. Pausing an MCP prevents the Machine Config Operator (MCO) from updating the nodes associated with that MCP.

**Procedure**

●Patch the MCP that you want paused by running the following command: $ oc patch mcp/<mcp_name> --patch '{"spec":{"paused":true}}' --type=merge For example: $ oc patch mcp/workerpool-canary --patch '{"spec":{"paused":true}}' --type=merge

**Example output**

machineconfigpool.machineconfiguration.openshift.io/workerpool-canary patched Page 127 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**Performing the cluster update**

**7.6.4.7**

After the machine config pools (MCP) enter a ready state, you can perform the cluster update.

**Procedure**

●See one of the following update methods, as appropriate for your cluster: ○"Updating a cluster using the web console" ○"Updating a cluster using the CLI"

**Unpausing the machine config pools**

**7.6.4.8**

After the OpenShift Container Platform update is complete, unpause your custom machine config pools (MCP) one at a time. Unpausing an MCP allows the Machine Config Operator (MCO) to update the nodes associated with that MCP.

**Procedure**

1.Patch the MCP that you want to unpause: $ oc patch mcp/<mcp_name> --patch '{"spec":{"paused":false}}' --type=merge For example: $ oc patch mcp/workerpool-canary --patch '{"spec":{"paused":false}}' --type=merge

**Example output**

machineconfigpool.machineconfiguration.openshift.io/workerpool-canary patched 2.Optional: Check the progress of the update by using one of the following options: a.Check the progress from the web console by clicking **Administration → Cluster**
**settings**.
b.Check the progress by running the following command: $ oc get machineconfigpools 3.Test your applications on the updated nodes to ensure that they are working as expected. 4.Repeat this process for any other paused MCPs, one at a time.
**Note**: In case of a failure, such as your applications not working on the updated nodes, you
can cordon and drain the nodes in the pool, which moves the application pods to other nodes to help maintain the quality-of-service for the applications. This first MCP should be no larger than the excess capacity.

**Moving a node to the original machine config pool**

**7.6.4.9**

After you update and verify applications on nodes in a custom machine config pool (MCP), move the nodes back to their original MCP by removing the custom label that you added to the nodes.
**Important**: A node must have a role to be properly functioning in the cluster.

**Procedure**

1.For each node in a custom MCP, remove the custom label from the node by running the following command: $ oc label node <node_name> node-role.kubernetes.io/<custom_label>- Page 128 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack For example: $ oc label node ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz node-role.kubernetes.io/workerpoolcanary-

**Example output**

node/ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz labeled The Machine Config Operator moves the nodes back to the original MCP and reconciles the node to the MCP configuration. 2.To ensure that node has been removed from the custom MCP, view the list of MCPs in the cluster and their current state by running the following command: $ oc get mcp

**Example output**

NAME CONFIG UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE master rendered-master-1203f157d053fd987c7cbd91e3fbc0ed True False False 3 3 3 0 61m workerpool-canary rendered-mcp-noupdate-5ad4791166c468f3a35cd16e734c9028 True False False 0 0 0 0 21m worker rendered-worker-5ad4791166c468f3a35cd16e734c9028 True False False 3 3 3 0 61m When the node is removed from the custom MCP and moved back to the original MCP, it can take several minutes to update the machine counts. In this example, one node was moved from the removed workerpool-canary MCP to the worker MCP. 3.Optional: Delete the custom MCP by running the following command: $ oc delete mcp <mcp_name>

**Updating a cluster in a disconnected environment**

**7.6.5**

You can update a cluster in an environment without access to the internet by taking additional steps to prepare your environment.

**About cluster updates in a disconnected environment**

**7.6.5.1**

A disconnected environment is one in which your cluster nodes cannot access the internet or where you want to manage update recommendations and release images locally for policy or performance purposes. This section covers mirroring OpenShift Container Platform images, managing an OpenShift Update Service, and performing cluster updates in a disconnected environment.

**7.6.5.1.1Mirroring OpenShift Container Platform images**

To update your cluster in a disconnected environment, your cluster environment must have access to a mirror registry that has the necessary images and resources for your targeted Page 129 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack update. A single container image registry is sufficient to host mirrored images for several clusters in the disconnected network. The following page has instructions for mirroring images onto a repository in your disconnected cluster: Mirroring OpenShift Container Platform images

**7.6.5.1.1.1Performing a cluster update in a disconnected environment**

You can use one of the following procedures to update a disconnected OpenShift Container Platform cluster: Updating a cluster in a disconnected environment using the OpenShift Update Service Updating a cluster in a disconnected environment without the OpenShift Update Service

**7.6.5.1.1.2Uninstalling the OpenShift Update Service from a cluster**

You can use the following procedure to uninstall a local copy of the OpenShift Update Service (OSUS) from your cluster: Uninstalling the OpenShift Update Service from a cluster

**7.6.5.1.2Mirroring OpenShift Container Platform images**

You must mirror container images onto a mirror registry before you can update a cluster in a disconnected environment. You can also use this procedure in connected environments to ensure your clusters run only approved container images that have satisfied your organizational controls for external content.
**Note**: Your mirror registry must be running at all times while the cluster is running.
The following steps outline the high-level workflow on how to mirror images to a mirror registry: 1.Install the OpenShift CLI (oc) on all devices being used to retrieve and push release images. 2.Download the registry pull secret and add it to your cluster. 3.Use the oc-mirror OpenShift CLI () plugin: a.Install the oc-mirror plugin on all devices being used to retrieve and push release images. b.Create an image set configuration file for the plugin to use when determining which release images to mirror. You can edit this configuration file later to change which release images that the plugin mirrors. c. Mirror your targeted release images directly to a mirror registry, or to removable media and then to a mirror registry. d.Configure your cluster to use the resources generated by the oc-mirror plugin. e.Repeat these steps as needed to update your mirror registry. Compared to using the oc adm release mirror command, the oc-mirror plugin has the following advantages: ●It can mirror content other than container images. ●After mirroring images for the first time, it is easier to update images in the registry. Page 130 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●The oc-mirror plugin provides an automated way to mirror the release payload from Quay, and also builds the latest graph data image for the OpenShift Update Service running in the disconnected environment.

**7.6.5.1.2.1Mirroring resources using the oc-mirror plugin**

You can use the oc-mirror OpenShift CLI (oc) plugin to mirror images to a mirror registry in your fully or partially disconnected environments. You must run oc-mirror from a system with internet connectivity to download the required images from the official Red Hat registries. See Mirroring images for a disconnected installation by using the oc-mirror plugin v2 for additional details.

**7.6.5.1.3Updating a cluster in a disconnected environment using the OpenShift Update**

**Service**

To get an update experience similar to connected clusters, you can use the following procedures to install and configure the OpenShift Update Service (OSUS) in a disconnected environment. The following steps outline the high-level workflow on how to update a cluster in a disconnected environment using OSUS: 1.Configure access to a secured registry. 2.Update the global cluster pull secret to access your mirror registry. 3.Install the OSUS Operator. 4.Create a graph data container image for the OpenShift Update Service. 5.Install the OSUS application and configure your clusters to use the OpenShift Update Service in your environment. 6.Perform a supported update procedure from the documentation as you would with a connected cluster.

**7.6.5.1.3.1Using the OpenShift Update Service in a disconnected environment**

The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform clusters. Red Hat publicly hosts the OpenShift Update Service, and clusters in a connected environment can connect to the service through public APIs to retrieve update recommendations. However, clusters in a disconnected environment cannot access these public APIs to retrieve update information. To have a similar update experience in a disconnected environment, you can install and configure the OpenShift Update Service so that it is available within the disconnected environment. A single OSUS instance is capable of serving recommendations to thousands of clusters. OSUS can be scaled horizontally to cater to more clusters by changing the replica value. So for most disconnected use cases, one OSUS instance is enough. For example, Red Hat hosts just one OSUS instance for the entire fleet of connected clusters. Page 131 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack If you want to keep update recommendations separate in different environments, you can run one OSUS instance for each environment. For example, in a case where you have separate test and stage environments, you might not want a cluster in a stage environment to receive update recommendations to version A if that version has not been tested in the test environment yet. The following sections describe how to install an OSUS instance and configure it to provide update recommendations to a cluster.

**7.6.5.1.3.2Prerequisites**

●You must have the oc command-line interface (CLI) tool installed. ●You must provision a container image registry in your environment with the container images for your update, as described in Mirroring OpenShift Container Platform images.

**7.6.5.1.3.3Configuring access to a secured registry for the OpenShift Update Service**

If the release images are contained in a registry whose HTTPS X.509 certificate is signed by a custom certificate authority, complete the steps in Configuring additional trust stores for image registry access along with following changes for the update service. The OpenShift Update Service Operator needs the config map key name updateserviceregistry in the registry CA cert. Image registry CA config map example for the update service apiVersion: v1 kind: ConfigMap metadata: name: my-registry-ca data: updateservice-registry: | -----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----registry-with-port.example.com..5000: | -----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- 1.The OpenShift Update Service Operator requires the config map key name updateservice-registry in the registry CA cert. 2.If the registry has the port, such as registry-with-port.example.com:5000, : should be replaced with ...

**7.6.5.1.3.4Updating the global cluster pull secret**

To add new registries or change authentication for your OpenShift Container Platform cluster, you can update the global pull secret by replacing it or appending new credentials. Page 132 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Use the oc set data secret/pull-secret command to apply the updated pull secret to all nodes in your cluster. Use this procedure when you need a separate registry to store images than the registry used during installation.

**Prerequisites**

●You have access to the cluster as a user with the cluster-admin role.

**Procedure**

1.Optional: To append a new pull secret to the existing pull secret: a.Download the pull secret by entering the following command: $ oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > <pull_secret_location> where:

**<pull_secret_location>**

Specifies the path to the pull secret file. b.Add the new pull secret by entering the following command: $ oc registry login --registry="<registry>" \ --auth-basic="<username>:<password>" \ --to=<pull_secret_location> where:

**<registry>**

Specifies the new registry. You can include many repositories within the same registry, for

| example: | --registry="<registry/my-namespace/my-repository> |   |
|---|---|---|
| <username>:<password> |   |   |

Specifies the credentials of the new registry.

**<pull_secret_location>**

Specifies the path to the pull secret file. 2.Update the global pull secret for your cluster by entering the following command. Note that this update rolls out to all nodes, which can take some time depending on the size of your cluster. $ oc set data secret/pull-secret -n openshift-config \ --from-file=.dockerconfigjson=<pull_secret_location> where:

**<pull_secret_location>**

Specifies the path to the new pull secret file.

**7.6.5.1.3.5Installing the OpenShift Update Service Operator**

To install the OpenShift Update Service, you must first install the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI.
**Note**: For clusters that are installed in disconnected environments, also known as
disconnected clusters, Operator Lifecycle Manager by default cannot access the Red Hatprovided OperatorHub sources hosted on remote registries because those remote sources require full internet connectivity. For more information, see Using Operator Lifecycle Manager in disconnected environments. Page 133 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Installing the OpenShift Update Service Operator by using the web console 1.**You can use the web console to install the OpenShift Update Service Operator.**

**Procedure**

a.In the web console, click **Operators** → **OperatorHub**.
**Note**: Enter Update Service into the Filter by keyword… field to find the Operator faster.
b.Choose **OpenShift Update Service** from the list of available Operators, and click **Install**. i. Select an **Update channel**. ii. Select a **Version**. iii.Select **A specific namespace on the cluster** under **Installation Mode**. iv.Select a namespace for Installed Namespace or accept the recommended namespace openshift-update-service. v.Select an **Update approval** strategy: ■The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. ■The **Manual** strategy requires a cluster administrator to approve the Operator update. vi.Click Install. c. Go to **Operators** → **Installed Operators** and verify that the OpenShift Update Service Operator is installed. d.Ensure that **OpenShift Update Service** is listed in the correct namespace with a **Status** of **Succeeded**. 2.**Installing the OpenShift Update Service Operator by using the CLI** You can use the OpenShift CLI (oc) to install the OpenShift Update Service Operator.

**Procedure**

a.Create a 命名空间 for the OpenShift Update Service Operator:

| i. Create a Namespace object YAML file, for example, update-service- namespace.yaml, for the OpenShift Update Service Operator: |   |   |
|---|---|---|
| apiVersion: v1 |   |   |
| kind: Namespace |   |   |
| metadata: |   |   |
| name: openshift-update-service |   |   |
| annotations: |   |   |
| openshift.io/node-selector: "" |   |   |
| labels: |   |   |
| openshift.io/cluster-monitoring: "true" |   |   |
| Set the | openshift.io/cluster-monitoring | label to enable Operator-recommended cluster |

monitoring on this namespace. ii. Create the namespace: $ oc create -f <filename>.yaml For example: $ oc create -f update-service-namespace.yaml b.Install the OpenShift Update Service Operator by creating the following objects: Page 134 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

| i. Create an OperatorGroup object YAML file, for example, update-service- operator-group.yaml: |   |   |
|---|---|---|
| apiVersion: operators.coreos.com/v1 |   |   |
| kind: OperatorGroup |   |   |
| metadata: |   |   |
| name: update-service-operator-group |   |   |
| namespace: openshift-update-service |   |   |
| spec: |   |   |
| targetNamespaces: |   |   |
| - openshift-update-service |   |   |
| ii. Create an | OperatorGroup | object: |
| $ oc -n openshift-update-service create -f <filename>.yaml |   |   |

For example: $ oc -n openshift-update-service create -f update-service-operator-group.yaml iii.Create a Subscription object YAML file, for example, update-servicesubscription.yaml:

**Example Subscription**

apiVersion: operators.coreos.com/v1alpha1 kind: Subscription metadata: name: update-service-subscription namespace: openshift-update-service spec: channel: v1 installPlanApproval: "Automatic" source: "redhat-operators" sourceNamespace: "openshift-marketplace" name: "cincinnati-operator" Specify the name of the catalog source that provides the Operator. For clusters that do not use a custom Operator Lifecycle Manager (OLM), specify redhat-operators. If your OpenShift Container Platform cluster is installed in a disconnected environment, specify the name of the CatalogSource object created when you configured Operator Lifecycle Manager (OLM).

| iv. Create the | Subscription | object: |
|---|---|---|
| $ oc create -f <filename>.yaml |   |   |

For example: $ oc -n openshift-update-service create -f update-service-subscription.yaml The OpenShift Update Service Operator is installed to the openshift-updateservice namespace and targets the openshift-update-service namespace. c. Verify the Operator installation: $ oc -n openshift-update-service get clusterserviceversions

**Example output**

NAME DISPLAY VERSION REPLACES PHASE update-service-operator.v4.6.0 OpenShift Update Service 4.6.0 Succeeded ... Page 135 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack If the OpenShift Update Service Operator is listed, the installation was successful. The version number might be different than shown.

**7.6.5.1.3.6Creating the OpenShift Update Service graph data container image**

The OpenShift Update Service requires a graph data container image, from which the OpenShift Update Service retrieves information about channel membership and blocked update edges. Graph data is typically fetched directly from the update graph data repository. In environments where an internet connection is unavailable, loading this information from an init container is another way to make the graph data available to the OpenShift Update Service. The role of the init container is to provide a local copy of the graph data, and during pod initialization, the init container copies the data to a volume that is accessible by the service.
**Note**: The oc-mirror OpenShift CLI (oc) plugin creates this graph data container image in
addition to mirroring release images. If you used the oc-mirror plugin to mirror your release images, you can skip this procedure.

**Procedure**

| 1. Create a Dockerfile, for example, | ./Dockerfile | , containing the following: |
|---|---|---|
| FROM registry.access.redhat.com/ubi9/ubi:latest |   |   |
| RUN curl -L -o cincinnati-graph-data.tar.gz https://api.openshift.com/api/upgrades info/graph-data _ |   |   |
| RUN mkdir -p /var/lib/cincinnati-graph-data && tar xvzf cincinnati-graph-data.tar.gz -C |   |   |
| /var/lib/cincinnati-graph-data/ --no-overwrite-dir --no-same-owner |   |   |
| CMD ["/bin/bash", "-c" ,"exec cp -rp /var/lib/cincinnati-graph-data/* /var/lib/cincinnati/graph-data"] |   |   |

2.Use the docker file created in the above step to build a graph data container image,

| for example, | registry.example.com/openshift/graph-data:latest | : |
|---|---|---|
| $ podman build -f ./Dockerfile -t registry.example.com/openshift/graph-data:latest |   |   |

3.Push the graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service, for

| example, | registry.example.com/openshift/graph-data:latest | : |
|---|---|---|
| $ podman push registry.example.com/openshift/graph-data:latest |   |   |

**Note**: To push a graph data image to a registry in a disconnected environment, copy the
graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service. Run oc image mirror --help for available options.

**7.6.5.1.3.7Creating an OpenShift Update Service application**

You can create an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI. 1.**Creating an OpenShift Update Service application by using the web console** You can use the OpenShift Container Platform web console to create an OpenShift Update Service application by using the OpenShift Update Service Operator.

**Prerequisites**

Page 136 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●The OpenShift Update Service Operator has been installed. ●The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service. ●The current release and update target releases have been mirrored to a registry in the disconnected environment.

**Procedure**

a.In the web console, click **Operators** → **Installed Operators**. b.Choose **OpenShift Update Service** from the list of installed Operators. c. Click the **Update Service** tab. d.Click **Create UpdateService**. e.Enter a name in the **Name** field, for example, service. f. Enter the local pullspec in the **Graph Data Image** field to the graph data container image created in "Creating the OpenShift Update Service graph data container image", for example, registry.example.com/openshift/graph-data:latest. g.In the **Releases** field, enter the registry and repository created to contain the release images in "Mirroring the OpenShift Container Platform image repository", for example, registry.example.com/ocp4/openshift4-release-images. h.Enter 2 in the **Replicas** field. i. Click **Create** to create the OpenShift Update Service application. j. Verify the OpenShift Update Service application: ○From the **UpdateServices** list in the **Update Service** tab, click the Update Service application just created. ○Click the **Resources** tab. ○Verify each application resource has a status of **Created**. 2.**Creating an OpenShift Update Service application by using the CLI** You can use the OpenShift CLI (oc) to create an OpenShift Update Service application.

**Prerequisites**

●The OpenShift Update Service Operator has been installed. ●The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service. ●The current release and update target releases have been mirrored to a registry in the disconnected environment.

**Procedure**

a.Configure the OpenShift Update Service target namespace, for

| example, | openshift-update-service |   | : |   |
|---|---|---|---|---|
| $ NAMESPACE=openshift-update-service |   |   |   |   |
| The namespace must match the |   | targetNamespaces |   | value from the operator group. |

b.Configure the name of the OpenShift Update Service application, for

| example, | service | : |
|---|---|---|
| $ NAME=service |   |   |

c. Configure the registry and repository for the release images as configured in "Mirroring the OpenShift Container Platform image repository", for example, registry.example.com/ocp4/openshift4-release-images: Page 137 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack $ RELEASE_IMAGES=registry.example.com/ocp4/openshift4-release-images d.Set the local pullspec for the graph data image to the graph data container image created in "Creating the OpenShift Update Service graph data container image",

| for example, | registry.example.com/openshift/graph-data:latest | : |
|---|---|---|
| $ GRAPH DATA IMAGE=registry.example.com/openshift/graph-data:latest _ _ |   |   |

e.Create an OpenShift Update Service application object: $ oc -n "${NAMESPACE}" create -f - <<EOF apiVersion: updateservice.operator.openshift.io/v1 kind: UpdateService metadata: name: ${NAME} spec: replicas: 2 releases: ${RELEASE_IMAGES} graphDataImage: ${GRAPH_DATA_IMAGE} EOF f. Verify the OpenShift Update Service application: i. Use the following command to obtain a policy engine route: $ while sleep 1; do POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")"; SCHEME="${POLICY_ENGINE_GRAPH_URI%%:*}"; if test "${SCHEME}" = http -o "${SCHEME}" = https; then break; fi; done You might need to poll until the command succeeds. ii. Retrieve a graph from the policy engine. Be sure to specify a valid version for channel. For example, if running in OpenShift Container Platform 4.18, use stable-4.18: $ while sleep 10; do HTTP_CODE="$(curl --header Accept:application/json --output /dev/stderr -write-out "%{http_code}" "${POLICY_ENGINE_GRAPH_URI}?channel=stable-4.6")"; if test "${HTTP_CODE}" -eq 200; then break; fi; echo "${HTTP_CODE}"; done This polls until the graph request succeeds; however, the resulting graph might be empty depending on which release images you have mirrored.
**Note**: The policy engine route name must not be more than 63 characters based on RFC-

| 1123. If you see ReconcileCompleted reason CreateRouteFailed caused by |   | ReconcileCompleted |   | status as |   | false | with the |
|---|---|---|---|---|---|---|---|
|   | CreateRouteFailed |   | caused by | host must conform to DNS 1123 naming convention |   |   |   |
| and must be no more than 63 characters |   |   |   |   | , try creating the Update Service with a shorter |   |   |

name.

**7.6.5.1.3.8Configuring the Cluster Version Operator (CVO)**

After the OpenShift Update Service Operator has been installed and the OpenShift Update Service application has been created, the Cluster Version Operator (CVO) can be updated to pull graph data from the OpenShift Update Service installed in your environment.

**Prerequisites**

●The OpenShift Update Service Operator has been installed. Page 138 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service. ●The current release and update target releases have been mirrored to a registry in the disconnected environment. ●The OpenShift Update Service application has been created.

**Procedure**

1.Set the OpenShift Update Service target namespace, for example, openshift-update-

|   | service | : |   |   |
|---|---|---|---|---|
| $ NAMESPACE=openshift-update-service |   |   |   |   |
| 2. Set the name of the OpenShift Update Service application, for example, |   |   | service | : |
| $ NAME=service |   |   |   |   |

3.Obtain the policy engine route: $ POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")" 4.Set the patch for the pull graph data: $ PATCH="{\"spec\":{\"upstream\":\"${POLICY_ENGINE_GRAPH_URI}\"}}" 5.Patch the CVO to use the OpenShift Update Service in your environment: $ oc patch clusterversion version -p $PATCH --type merge

**7.6.5.1.3.9Next steps**

Before updating your cluster, confirm that the following conditions are met: ●The Cluster Version Operator (CVO) is configured to use your installed OpenShift Update Service application. ●The release image signature config map for the new release is applied to your cluster.
**Note**: The Cluster Version Operator (CVO) uses release image signatures to ensure that
release images have not been modified, by verifying that the release image signatures match the expected result. ●The current release and update target release images are mirrored to a registry in the disconnected environment. ●A recent graph data container image has been mirrored to your registry. ●A recent version of the OpenShift Update Service Operator is installed.
**Note**: If you have not recently installed or updated the OpenShift Update Service Operator,
there might be a more recent version available. See Using Operator Lifecycle Manager in disconnected environments for more information about how to update your OLM catalog in a disconnected environment. After you configure your cluster to use the installed OpenShift Update Service and local mirror registry, you can use any of the following update methods: Updating a cluster using the web console Updating a cluster using the CLI Performing a Control Plane Only update Performing a canary rollout update Page 139 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.6.5.1.4Updating a cluster in a disconnected environment without the OpenShift**

**Update Service**

Use the following procedures to update a cluster in a disconnected environment without access to the OpenShift Update Service.

**7.6.5.1.4.1Prerequisites**

●You must have the oc command-line interface (CLI) tool installed. ●You must provision a local container image registry with the container images for your update, as described in Mirroring OpenShift Container Platform images.

| o the cluster as a user with | admin | privileges. See |
|---|---|---|

define and apply permissions. ●You must have a recent etcd backup in case your update fails and you must restore your cluster to a previous state. ●You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default OperatorHub catalogs switch from the current minor version to the next during a cluster update. See Updating installed Operators for more information on how to check compatibility and, if necessary, update the installed Operators. ●You must ensure that all machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy. ●If your cluster uses manually maintained credentials, update the cloud provider resources for the new release. For more information, including how to determine if this is a requirement for your cluster, see Preparing to update a cluster with manually maintained credentials. ●If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If minAvailable is set to 1 in PodDisruptionBudget, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the PodDisruptionBudget field can prevent the node drain.
**Note**: If you run an Operator or you have configured any application with the pod
disruption budget, you might experience an interruption during the update process. If minAvailable is set to 1 in PodDisruptionBudget, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the PodDisruptionBudget field can prevent the node drain.

**7.6.5.1.4.2Pausing a MachineHealthCheck resource**

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the MachineHealthCheck resources might identify such nodes as unhealthy Page 140 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack and reboot them. To avoid rebooting worker nodes, you must pause all the MachineHealthCheck resources before updating the cluster.
**Note**: Some MachineHealthCheck resources might not need to be paused. If
your MachineHealthCheck resource relies on unrecoverable conditions, pausing that MHC is unnecessary.

**Prerequisites**

●You installed the OpenShift CLI (oc).

**Procedure**

1.List all of the available MachineHealthCheck resources that you want to pause by running the following command:

| $ oc get machinehealthcheck -n openshift-machine-api |   |   |
|---|---|---|
| 2. For each | MachineHealthCheck | resource, pause the machine health check by running |

the following command:

| $ oc -n openshift-machine-api annotate mhc <mhc name> cluster.x-k8s.io/paused="" _ |   |   |
|---|---|---|
| The annotated | MachineHealthCheck | resource resembles the following YAML file: |
| apiVersion: machine.openshift.io/v1beta1 |   |   |
| kind: MachineHealthCheck |   |   |
| metadata: |   |   |
| name: example |   |   |
| namespace: openshift-machine-api |   |   |
| annotations: |   |   |
| cluster.x-k8s.io/paused: "" |   |   |
| spec: |   |   |
| selector: |   |   |
| matchLabels: |   |   |
| role: worker |   |   |
| unhealthyConditions: |   |   |
| - type: "Ready" |   |   |
| status: "Unknown" |   |   |
| timeout: "300s" |   |   |
| - type: "Ready" |   |   |
| status: "False" |   |   |
| timeout: "300s" |   |   |
| maxUnhealthy: "40%" |   |   |
| status: |   |   |
| currentHealthy: 5 |   |   |
| expectedMachines: 5 |   |   |

**Important**:
Resume the machine health checks after updating the cluster. To resume the check, remove the pause annotation from the MachineHealthCheck resource by running the following command: $ oc -n openshift-machine-api annotate mhc <mhc-name> cluster.x-k8s.io/paused- Page 141 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.6.5.1.4.3Retrieving a release image digest**

In order to update a cluster in a disconnected environment using the oc adm upgrade command with the --to-image option, you must reference the sha256 digest that corresponds to your targeted release image.

**Procedure**

1.Run the following command on a device that is connected to the internet: $ oc adm release info -o 'jsonpath={.digest}{"\n"}' quay.io/openshift-release-dev/ocprelease:${OCP_RELEASE_VERSION}-${ARCHITECTURE} For {OCP_RELEASE_VERSION}, specify the version of OpenShift Container Platform to which you want to update, such as 4.10.16.

|   | {ARCHITECTURE |   |   |   |   |
|---|---|---|---|---|---|
| x86 64 _ |   | , | aarch64 | , | s390x |

For {ARCHITECTURE}, specify the architecture of the cluster, such

**Example output**

sha256:a8bfba3b6dddd1a2fbbead7dac65fe4fb8335089e4e7cae327f3bad334add31d 2.Copy the sha256 digest for use when updating your cluster.

**7.6.5.1.4.4Updating the disconnected cluster**

Update the disconnected cluster to the OpenShift Container Platform version that you downloaded the release images for.
**Note**: If you have a local OpenShift Update Service, you can update by using the
connected web console or CLI instructions instead of this procedure.

**Prerequisites**

●You mirrored the images for the new release to your registry. ●You applied the release image signature ConfigMap for the new release to your cluster.
**Note**: The release image signature config map allows the Cluster Version Operator (CVO)
to ensure the integrity of release images by verifying that the actual image signatures match the expected signatures. ●You obtained the sha256 digest for your targeted release image. ●You installed the OpenShift CLI (oc). ●You paused all MachineHealthCheck resources.

**Procedure**

●Update the cluster: $ oc adm upgrade --allow-explicit-upgrade --to-image <defined_registry>/<defined_repository>@<digest> Where:

**<defined_registry>**

Specifies the name of the mirror registry you mirrored your images to.

**<defined_repository>**

Specifies the name of the image repository you want to use on the mirror registry.

**<digest>**

Page 142 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Specifies the sha256 digest for the targeted release image, for example, sha256:81154f5c03294534e1eaf0319bef7a601134f891689ccede5d705ef659aa8c9 2.
**Note**:
●See "Mirroring OpenShift Container Platform images" to review how your mirror registry and repository names are defined. ●If you used an ImageContentSourcePolicy or ImageDigestMirrorSet, you can use the canonical registry and repository names instead of the names you defined.

| e canonical registry name is | quay.io |   |
|---|---|---|
| openshift-release-dev/ocp-release |   | . |

●You can only configure global pull secrets for clusters that have

| ImageContentSourcePolicy |   |
|---|---|
| ImageTagMirrorSet | object. |

or ImageTagMirrorSet object. You cannot add a pull secret to a project.

**7.6.5.1.4.5Understanding image registry repository mirroring**

By setting up container registry repository mirroring, you can perform the following tasks: ●Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry. ●Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used. Repository mirroring in OpenShift Container Platform includes the following attributes: ●Image pulls are resilient to registry downtimes. ●Clusters in disconnected environments can pull images from critical locations, such as quay.io, and have registries behind a company firewall provide the requested images. ●A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried. ●The mirror information you enter is added to the /etc/containers/registries.conf file on every node in the OpenShift Container Platform cluster. ●When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node. You can set up repository mirroring in the following ways: ●At OpenShift Container Platform installation: By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment. ●After OpenShift Container Platform installation: If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects: Page 143 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ○ImageDigestMirrorSet (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. ○ImageTagMirrorSet (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails. ○ImageContentSourcePolicy (ICSP). This object allows you to pull images from a mirrored registry by using digest specifications. The ICSP CR always falls back to the source registry if the mirrors do not work.
**Important**:
Using an ImageContentSourcePolicy (ICSP) object to configure repository mirroring is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported. It will be removed in a future release and is not recommended for new deployments. If you have existing YAML files that you used to

| , you can use the | oc adm migrate |   |
|---|---|---|
| ImageDigestMirrorSet |   | YAML files. F |

create ImageContentSourcePolicy objects, you can use the oc adm migrate information, see "Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring". Each of these custom resource objects identify the following information: ●The source of the container image repository you want to mirror. ●A separate entry for each mirror repository you want to offer the content Note the following actions and how they affect node drain behavior: ●If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node. ●If you create an ITMS CR object, the MCO drains and reboots the node. ●If you delete an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node. ●If you modify an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.

> **Important:** ○When the MCO detects any of the following changes, it applies the update without draining or rebooting the node: ■Changes to the SSH key in the spec.config.passwd.users.sshAuthorizedKeys parameter of a machine config. ■Changes to the global pull secret or pull secret in the openshiftconfig namespace. ■Automatic rotation of the /etc/kubernetes/kubelet-ca.crt certificate authority (CA) by the Kubernetes API Server Operator.


| hen the MCO detects changes to the /etc/containers/registries.conf ch as editing an ImageDigestMirrorSet, ImageTagMirrorSet, ImageContentSourcePolicy object, it drains the corresponding nod | /etc/containers/registries.conf |
|---|---|
| ImageContentSourcePolicy |   |

Page 144 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack applies the changes, and uncordons the nodes. The node drain does not happen for the following changes: ■The addition of a registry with the pull-from-mirror = "digestonly" parameter set for each mirror. ■The addition of a mirror with the pull-from-mirror = "digestonly" parameter set in a registry. ■The addition of items to the unqualified-search-registries list. For new clusters, you can use IDMS, ITMS, and ICSP CRs objects as needed. However, using IDMS and ITMS is recommended. If you upgraded a cluster, any existing ICSP objects remain stable, and both IDMS and ICSP objects are supported. Workloads that use ICSP objects continue to function as expected. However, if you want to take advantage of the fallback policies introduced in the IDMS CRs, you can migrate current workloads to IDMS objects by using the oc adm migrate icsp command as shown in the **Converting ImageContentSourcePolicy (ICSP) files for**
**image registry repository mirroring** section that follows. Migrating to IDMS objects does
not require a cluster reboot.

| te: If your cluster uses an | ImageDigestMirrorSet |   |
|---|---|---|
| ImageContentSourcePolicy |   | object to configure |

global pull secrets for mirrored registries. You cannot add a pull secret to a project. 1.**Configuring image registry repository mirroring** You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry.

**Prerequisites**

●Access to the cluster as a user with the cluster-admin role.

**Procedure**

a.Configure mirrored repositories, by either: ○Setting up a mirrored repository with Red Hat Quay. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using Red Hat Quay. ■Red Hat Quay Repository Mirroring

| g a tool such as | skopeo | to copy im |
|---|---|---|

repository to the mirrored repository. For example, after installing the skopeo RPM package on a {op-system-

| base-full system}, use the | skopeo | command as shown in the following example: |
|---|---|---|
| $ skopeo copy --all \ |   |   |
| docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \ |   |   |
| docker://example.io/example/ubi-minimal |   |   |
| In this example, you have a container image registry named example.io and image repository named example. You want to copy the ubi9/ubi-minimal image from registry.access.redhat.com to example.io. After you create the mirrored |   |   |

registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository. Page 145 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack b.Create a postinstallation mirror configuration custom resource (CR), by using one of the following examples: ○Create an ImageDigestMirrorSet or ImageTagMirrorSet CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:

| apiVersion: config.openshift.io/v1 |   |   |
|---|---|---|
| kind: ImageDigestMirrorSet |   |   |
| metadata: |   |   |
| name: ubi9repo |   |   |
| spec: |   |   |
| imageDigestMirrors: |   |   |
| - mirrors: |   |   |
| - example.io/example/ubi-minimal |   |   |
| - example.com/example2/ubi-minimal |   |   |
| source: registry.access.redhat.com/ubi9/ubi-minimal |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| - mirrors: |   |   |
| - mirror.example.com/redhat |   |   |
| source: registry.example.com/redhat |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| - mirrors: |   |   |
| - mirror.example.com |   |   |
| source: registry.example.com |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| - mirrors: |   |   |
| - mirror.example.net/image |   |   |
| source: registry.example.com/example/myimage |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| - mirrors: |   |   |
| - mirror.example.net |   |   |
| source: registry.example.com/example |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| - mirrors: |   |   |
| - mirror.example.net/registry-example-com |   |   |
| source: registry.example.com |   |   |
| mirrorSourcePolicy: AllowContactingSource |   |   |
| ○ Create an | ImageContentSourcePolicy | custom resource, replacing the source |

and mirrors with your own registry and repository pairs and images: apiVersion: operator.openshift.io/v1alpha1 kind: ImageContentSourcePolicy metadata: name: mirror-ocp spec: repositoryDigestMirrors:
  - mirrors:
  - mirror.registry.com:443/ocp/release
source: quay.io/openshift-release-dev/ocp-release
  - mirrors:
Page 146 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack
  - mirror.registry.com:443/ocp/release
source: quay.io/openshift-release-dev/ocp-v4.0-art-dev where:
  - **- mirror.registry.com:443/ocp/release**
Specifies the name of the mirror image registry and repository.

**source: quay.io/openshift-release-dev/ocp-release**

Specifies the online registry and repository containing the content that is mirrored. c. Create the new object by running the following command: $ oc create -f registryrepomirror.yaml After the object is created, the Machine Config Operator (MCO) drains the nodes

| ImageTagMirrorSet | o |
|---|---|
| ImageDigestMirrorSet |   |

for ImageTagMirrorSet objects only. The MCO does not drain the nodes for ImageDigestMirrorSet and ImageContentSourcePolicy objects. d.To check that the mirrored configuration settings are applied, do the following on one of the nodes. i. List your nodes: $ oc get node

**Example output**

NAME STATUS ROLES AGE VERSION ip-10-0-137-44.ec2.internal Ready worker 7m v1.31.3 ip-10-0-138-148.ec2.internal Ready master 11m v1.31.3 ip-10-0-139-122.ec2.internal Ready master 11m v1.31.3 ip-10-0-147-35.ec2.internal Ready worker 7m v1.31.3 ip-10-0-153-12.ec2.internal Ready worker 7m v1.31.3 ip-10-0-154-10.ec2.internal Ready master 11m v1.31.3 ii. Start the debugging process to access the node: $ oc debug node/ip-10-0-147-35.ec2.internal

**Example output**

| Starting pod/ip-10-0-147-35ec2internal-debug ... |   |   |   |   |
|---|---|---|---|---|
| To use host binaries, run `chroot /host` |   |   |   |   |
| iii. Change your root directory to |   | /host | : |   |
| sh-4.2# chroot /host |   |   |   |   |
| iv. Check the | /etc/containers/registries.conf |   |   | file to make sure the changes were |

made:

| sh-4.2# cat /etc/containers/registries.conf |   |   |
|---|---|---|
| The following output represents a | registries.conf | file where postinstallation mirror |

configuration CRs are applied.

**Example output**

unqualified-search-registries = ["registry.access.redhat.com", "docker.io"] short-name-mode = "" [[registry]] prefix = "" location = "registry.access.redhat.com/ubi9/ubi-minimal" [[registry.mirror]] location = "example.io/example/ubi-minimal" Page 147 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack pull-from-mirror = "digest-only" [[registry.mirror]] location = "example.com/example/ubi-minimal" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.example.com" [[registry.mirror]] location = "mirror.example.net/registry-example-com" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.example.com/example" [[registry.mirror]] location = "mirror.example.net" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.example.com/example/myimage" [[registry.mirror]] location = "mirror.example.net/image" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.example.com" [[registry.mirror]] location = "mirror.example.com" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.example.com/redhat" [[registry.mirror]] location = "mirror.example.com/redhat" pull-from-mirror = "digest-only" [[registry]] prefix = "" location = "registry.access.redhat.com/ubi9/ubi-minimal" blocked = true Page 148 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack [[registry.mirror]] location = "example.io/example/ubi-minimal-tag" pull-from-mirror = "tag-only" where:

**[[registry]].location = "registry.access.redhat.com/ubi9/ubi-minimal"**

The repository listed in a pull spec.

**[[registry.mirror]].location = "example.io/example/ubi-minimal"**

Indicates the mirror for that repository.

**[[registry.mirror]].pull-from-mirror = "digest-only"**

Means that the image pull from the mirror is a digest reference image.

| [[registry]].blocked = true |   |
|---|---|
| Indicates that the | NeverContactSource |
| [[registry.mirror]].pull-from-mirror = "tag-only" |   |

Indicates that the image pull from the mirror is a tag reference image. v.Pull an image to the node from the source and check if it is resolved by the mirror. sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...

**Troubleshooting**

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem: ●The first working mirror is used to supply the pulled image. ●The main registry is only used if no other mirror works.

| ontext, the | Insecure | flags are |
|---|---|---|
| /etc/containers/registries.conf |   |   |

version 2 and in TOML format. 2.**Converting ImageContentSourcePolicy (ICSP) files for image registry repository**

**mirroring**

Using an ImageContentSourcePolicy (ICSP) object to configure repository mirroring is a deprecated feature. This functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments. ICSP objects are being replaced by ImageDigestMirrorSet and ImageTagMirrorSet objects to configure repository mirroring. If you have existing YAML files that you used to create ImageContentSourcePolicy objects, you can use the oc adm migrate icsp command to convert those files to an ImageDigestMirrorSet YAML file. The command updates the API to the current version, changes the kind value to ImageDigestMirrorSet, and changes spec.repositoryDigestMirrors to spec.imageDigestMirrors. The rest of the file is not changed. Because the migration does not change the registries.conf file, the cluster does not need to reboot. Page 149 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack For more information about ImageDigestMirrorSet or ImageTagMirrorSet objects, see "Configuring image registry repository mirroring" in the previous section.

**Prerequisites**

| s a user with the | cluster-admin |   |
|---|---|---|
| ImageContentSourcePolicy |   | obje |

**Procedure**

a.Use the following command to convert one or more ImageContentSourcePolicy YAML files to an ImageDigestMirrorSet YAML file: $ oc adm migrate icsp <file_name>.yaml <file_name>.yaml <file_name>.yaml --dest-dir <path_to_the_directory> where:

**<file_name>**

Specifies the name of the source ImageContentSourcePolicy YAML. You can list multiple file names.

**--dest-dir**

Optional: Specifies a directory for the output ImageDigestMirrorSet YAML. If unset, the file is written to the current directory. For example, the following command converts the icsp.yaml and icsp-2.yaml file and saves

| the new YAML files to the | idms-files | directory. |
|---|---|---|
| $ oc adm migrate icsp icsp.yaml icsp-2.yaml --dest-dir idms-files |   |   |

**Example output**

wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi8repo.5911620242173376087.yaml wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi9repo.6456931852378115011.yaml b.Create the CR object by running the following command: $ oc create -f <path_to_the_directory>/<file-name>.yaml where:

**<path_to_the_directory>**

Specifies the path to the directory, if you used the --dest-dir flag.

**<file_name>**

Specifies the name of the ImageDigestMirrorSet YAML. c. Remove the ICSP objects after the IDMS objects are rolled out.

**7.6.5.1.4.6Widening the scope of the mirror image catalog to reduce the frequency of**

**cluster node reboots**

You can scope the mirrored image catalog at the repository level or the wider registry level. A widely scoped ImageContentSourcePolicy resource reduces the number of times the nodes need to reboot in response to changes to the resource. To widen the scope of the mirror image catalog in the ImageContentSourcePolicy resource, perform the following procedure.

**Prerequisites**

●Install the OpenShift Container Platform CLI oc. ●Log in as a user with cluster-admin privileges. Page 150 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack ●Configure a mirrored image catalog for use in your disconnected cluster.

**Procedure**

1.Run the following command, specifying values for <local_registry>, <pull_spec>,

| and | <pull secret file>: _ _ |   |
|---|---|---|
| $ oc adm catalog mirror <local registry>/<pull spec> <local registry> -a <pull secret file> --icsp- _ _ _ _ _ |   |   |
| scope=registry |   |   |

where:

**<local_registry>**

is the local registry you have configured for your disconnected cluster, for example, local.registry:5000.

**<pull_spec>**

is the pull specification as configured in your disconnected registry, for example, redhat/redhat-operator-index:v4.18

**<pull_secret_file>**

is the registry.redhat.io pull secret in .json file format. You can download the pull secret from Red Hat OpenShift Cluster Manager.

| The | oc adm catalog mirror |
|---|---|
| manifests |   |

The oc adm catalog mirror command creates a /redhat-operator-indexmanifests directory and generates imageContentSourcePolicy.yaml, catalogSource.yaml, and mapping.txt files. 2.Apply the new ImageContentSourcePolicy resource to the cluster: $ oc apply -f imageContentSourcePolicy.yaml

**Verification**

| ● Verify that | oc apply | successfully applied the change to | ImageContentSourcePolicy | : |
|---|---|---|---|---|
| $ oc get ImageContentSourcePolicy -o yaml |   |   |   |   |

**Example output**

| apiVersion: v1 |   |   |
|---|---|---|
| items: |   |   |
| - apiVersion: operator.openshift.io/v1alpha1 |   |   |
| kind: ImageContentSourcePolicy |   |   |
| metadata: |   |   |
| annotations: |   |   |
| kubectl.kubernetes.io/last-applied-configuration: \| |   |   |
| {"apiVersion":"operator.openshift.io/v1alpha1","kind":"ImageContentSourcePolicy","metadata":{"annotati |   |   |
| ons":{},"name":"redhat-operator- |   |   |
| index"},"spec":{"repositoryDigestMirrors":[{"mirrors":["local.registry:5000"],"source":"registry.redhat.io"}]}} |   |   |
| ... |   |   |
| After you update the | ImageContentSourcePolicy | resource, OpenShift Container Platform |

deploys the new settings to each node and the cluster starts using the mirrored repository for requests to the source repository.

**7.6.5.1.5Uninstalling the OpenShift Update Service from a cluster**

To remove a local copy of the OpenShift Update Service (OSUS) from your cluster, you must first delete the OSUS application and then uninstall the OSUS Operator. Page 151 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.6.5.1.5.1Deleting an OpenShift Update Service application**

You can delete an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI. 1.**Deleting an OpenShift Update Service application by using the web console** You can use the OpenShift Container Platform web console to delete an OpenShift Update Service application by using the OpenShift Update Service Operator.

**Prerequisites**

●The OpenShift Update Service Operator has been installed.

**Procedur**

a.In the web console, click **Operators** → **Installed Operators**. b.Choose **OpenShift Update Service** from the list of installed Operators. c. Click the **Update Service** tab. d.From the list of installed OpenShift Update Service applications, select the application to be deleted and then click **Delete UpdateService**. e.From the **Delete UpdateService**? confirmation dialog, click **Delete** to confirm the deletion. 2.**Deleting an OpenShift Update Service application by using the CLI** You can use the OpenShift CLI (oc) to delete an OpenShift Update Service application.

**Procedure**

a.Get the OpenShift Update Service application name using the namespace the OpenShift Update Service application was created in, for example, openshift-

|   | update-service | : |
|---|---|---|
| $ oc get updateservice -n openshift-update-service |   |   |

**Example output**

| NAME AGE |   |   |
|---|---|---|
| service 6s |   |   |
| b. Delete the OpenShift Update Service application using the | NAME | value from the |

previous step and the namespace the OpenShift Update Service application was

| created in, for example, | openshift-update-service | : |
|---|---|---|
| $ oc delete updateservice service -n openshift-update-service |   |   |

**Example output**

updateservice.updateservice.operator.openshift.io "service" deleted

**7.6.5.1.5.2Uninstalling the OpenShift Update Service Operator**

You can uninstall the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI. 1.**Uninstalling the OpenShift Update Service Operator by using the web console** You can use the OpenShift Container Platform web console to uninstall the OpenShift Update Service Operator.

**Prerequisites**

●All OpenShift Update Service applications have been deleted.

**Procedure**

Page 152 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack a.In the web console, click **Operators** → **Installed Operators**. b.Select **OpenShift Update Service** from the list of installed Operators and click **Uninstall Operator**. c. From the **Uninstall Operator**? confirmation dialog, click **Uninstall** to confirm the uninstallation. 2.**Uninstalling the OpenShift Update Service Operator by using the CLI** You can use the OpenShift CLI (oc) to uninstall the OpenShift Update Service Operator.

**Prerequisites**

●All OpenShift Update Service applications have been deleted.

**Procedure**

a.Change to the project containing the OpenShift Update Service Operator, for

| example, | openshift-update-service | : |
|---|---|---|
| $ oc project openshift-update-service |   |   |

**Example output**

Now using project "openshift-update-service" on server "https://example.com:6443". b.Get the name of the OpenShift Update Service Operator operator group: $ oc get operatorgroup

**Example output**

| NAME AGE |   |   |
|---|---|---|
| openshift-update-service-fprx2 4m41s |   |   |
| c. Delete the operator group, for example, | openshift-update-service-fprx2 | : |
| $ oc delete operatorgroup openshift-update-service-fprx2 |   |   |

**Example output**

operatorgroup.operators.coreos.com "openshift-update-service-fprx2" deleted d.Get the name of the OpenShift Update Service Operator subscription: $ oc get subscription

**Example output**

NAME PACKAGE SOURCE CHANNEL update-service-operator update-service-operator updateservice-index-catalog v1 e.Using the Name value from the previous step, check the current version of the subscribed OpenShift Update Service Operator in the currentCSV field: $ oc get subscription update-service-operator -o yaml | grep " currentCSV"

**Example output**

| currentCSV: update-service-operator.v0.0.1 |   |   |
|---|---|---|
| f. Delete the subscription, for example, | update-service-operator | : |
| $ oc delete subscription update-service-operator |   |   |

**Example output**

subscription.operators.coreos.com "update-service-operator" deleted g.Delete the CSV for the OpenShift Update Service Operator using

| the | currentCSV | value from the previous step: |
|---|---|---|
| $ oc delete clusterserviceversion update-service-operator.v0.0.1 |   |   |

**Example output**

clusterserviceversion.operators.coreos.com "update-service-operator.v0.0.1" deleted Page 153 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 7.7 Troubleshooting a cluster update

**Gathering data about your cluster update**

**7.7.1**

When reaching out to Red Hat support for issues with an update, it is important to provide data for the support team to use for troubleshooting your failed cluster update.

**Gathering log data for a support case**

**7.7.1.1**

To gather data from your cluster, including log data, use the oc adm mustgather command. See Gathering data about your cluster.

**Gathering cluster update status using oc adm upgrade status**

**7.7.1.2**

**(Technology Preview)**

When updating your cluster, the oc adm upgrade command returns returns limited

| the | oc adm upgrade |   |
|---|---|---|
| oc adm upgrade |   | com |

information about the status of your update. You can use the oc adm upgrade status command to decouple status information from the oc adm upgrade command and return specific information regarding a cluster update, including the status of the control plane and worker node updates. The oc adm upgrade status command is read-only and does not alter any state in your cluster.
**Important**:
The oc adm upgrade status command is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see Technology Preview Features Support Scope.

| oc adm upgrade status | command can be used for clusters |
|---|---|

latest supported release.
**Note:** Your cluster does not need to be a Technology Preview-enabled cluster in order for
you to use the oc adm upgrade status command.

**Procedure**

1.Set the OC_ENABLE_CMD_UPGRADE_STATUS environment variable to true by running the following command:

| $ export OC ENABLE CMD UPGRADE STATUS=true _ _ _ _ |   |   |
|---|---|---|
| 2. Run the | oc adm upgrade status | command: |
| $ oc adm upgrade status |   |   |

**Example output for an update progressing successfully**

= Control Plane = Assessment: Progressing Page 154 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Target Version: 4.17.1 (from 4.17.0) Updating: machine-config Completion: 97% (32 operators updated, 1 updating, 0 waiting) Duration: 54m (Est. Time Remaining: <10m) Operator Status: 32 Healthy, 1 Unavailable Control Plane Nodes NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-53-40.us-east-2.compute.internal Progressing Draining 4.17.0 +10m ip-10-0-30-217.us-east-2.compute.internal Outdated Pending 4.17.0 ? ip-10-0-92-180.us-east-2.compute.internal Outdated Pending 4.17.0 ? = Worker Upgrade = WORKER POOL ASSESSMENT COMPLETION STATUS worker Progressing 0% (0/2) 1 Available, 1 Progressing, 1 Draining infra Progressing 50% (1/2) 1 Available, 1 Progressing, 1 Draining Worker Pool Nodes: Worker NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-4-159.us-east-2.compute.internal Progressing Draining 4.17.0 +10m ip-10-0-99-40.us-east-2.compute.internal Outdated Pending 4.17.0 ? Worker Pool Nodes: infra NAME ASSESSMENT PHASE VERSION EST MESSAGE ip-10-0-4-159-infra.us-east-2.compute.internal Progressing Draining 4.17.0 +10m ip-10-0-20-162.us-east-2.compute.internal Completed Updated 4.17.1 - = Update Health = SINCE LEVEL IMPACT MESSAGE 54m4s Info None Update is proceeding well

**Gathering ClusterVersion history**

**7.7.1.3**

The Cluster Version Operator (CVO) records updates made to a cluster, known as the ClusterVersion history. The entries can reveal correlation between changes in cluster behavior with potential triggers, although correlation does not imply causation.
**Note**: The initial, minor, and z-stream version updates are stored by the ClusterVersion
history. However, the ClusterVersion history has a size limit. If the limit is reached, the oldest z-stream updates in previous minor versions are pruned to accommodate the limit. You can view the ClusterVersion history by using the OpenShift Container Platform web console or by using the OpenShift CLI (oc). Page 155 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

**7.7.1.3.1Gathering ClusterVersion history in the OpenShift Container Platform web**

**console**

You can view the ClusterVersion history in the OpenShift Container Platform web console.

**Prerequisites**

●You have access to the cluster as a user with the cluster-admin role. ●You have access to the OpenShift Container Platform web console.

**Procedure**

●From the web console, click **Administration → Cluster Settings** and review the contents of the **Details** tab.

**7.7.1.3.2Gathering ClusterVersion history using the OpenShift CLI (oc)**

You can view the ClusterVersion history using the OpenShift CLI (oc).

**Prerequisites**

●You have access to the cluster as a user with the cluster-admin role. ●You have installed the OpenShift CLI (oc).

**Procedure**

1.View the cluster update history by entering the following command: $ oc describe clusterversions/version

**Example output**

Desired: Channels: candidate-4.13 candidate-4.14 fast-4.13 fast-4.14 stable-4.13 Image: quay.io/openshift-release-dev/ocprelease@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4 URL: https://access.redhat.com/errata/RHSA-2023:6130 Version: 4.13.19 History: Completion Time: 2023-11-07T20:26:04Z Image: quay.io/openshift-release-dev/ocprelease@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4 Started Time: 2023-11-07T19:11:36Z State: Completed Verified: true Version: 4.13.19 Completion Time: 2023-10-04T18:53:29Z Image: quay.io/openshift-release-dev/ocprelease@sha256:eac141144d2ecd6cf27d24efe9209358ba516da22becc5f0abc199d25a9cfcec Started Time: 2023-10-04T17:26:31Z State: Completed Verified: true Version: 4.13.13 Page 156 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack Completion Time: 2023-09-26T14:21:43Z Image: quay.io/openshift-release-dev/ocprelease@sha256:371328736411972e9640a9b24a07be0af16880863e1c1ab8b013f9984b4ef727 Started Time: 2023-09-26T14:02:33Z State: Completed Verified: false Version: 4.13.12 Observed Generation: 4 Version Hash: CMLl3sLq-EA= Events: <none>

## 8 Summary

In this document, we successfully deployed an OpenShift Container Platform cluster of version 4.18 on the Apsara Stack cloud computing platform using the Agent-based installer. The cluster consists of three control plane nodes and three compute nodes. An upgrade of the cluster from version 4.18 to 4.19 is also performed successfully. This deployment leveraged a suite of Apsara Stack cloud services, including ECS, OSS, SLB, DNS, and VPC. The successful implementation validates that Apsara Stack possesses the necessary infrastructure and capabilities to deploy and operate the OpenShift Container Platform effectively.

## 9 Frequently Asked Questions (FAQs)

### 9.1 Support

Customers are expected to perform the installation independently based on the provided documentation. Should any technical issues arise, they may contact Alibaba Cloud team for support: ●Online documentation: https://www.alibabacloud.com/en/product/apsara-stack/ ●Online support and tickets: https://smartservice.console.aliyun.com/service ●Manual services (optional and selected by customer) ○7*24 L1 Remote service: a dedicated support team of Alibaba Cloud for customers with 7*24 on-call coverage, to provide Q&A and trouble shooting towards technical issues. ○5*8 L2 Support: usually acted by R&D team of Alibaba Cloud to provide support on technical issues escalated by L1 Remote service. ○TAM (Technical Account Manager): acts as the primary owner responsible for customer, leading a team with O&M specialists to collaborate with customers. TAM team handle complex troubleshooting cases, and (when allowed by customer) perform and execute changes towards customer's Apsara Stack. If Apsara Stack is not part of the reported issue, customers are expected to contact Red Hat for support, as per standard support policy and SLA of Red Hat. Page 157 Red Hat OpenShift Container Platform 4.18 on Alibaba Cloud Apsara Stack

### 9.2 does volumes in Apsara Stack supports increasing disk

**performance for control planes?**

ApsaraStack supports multiple disk categories. Users can determine which disk types are supported on the cloud either before or after the deployment of ApsaraStack. The available disk categories include Premium Performance Disks, Standard Performance Disks. ●Premium Performance Disks are tailored for I/O-intensive application scenarios, delivering up to 25,000 random IOPS for ECS instances. ●Standard Performance Disks are designed for scenarios with moderate I/O workloads, providing ECS instances with up to 5,000 random IOPS. If users need to improve disk performance, there are generally two approaches: ●Increase Disk Capacity: Taking the Premium Performance Disk used in this article as an example, its IOPS is calculated using the formula: min(1800 + 30*Capacity, 25000). As shown, IOPS increases with capacity until it hits the single-disk limit of 25,000 IOPS at around 773 GB. ●Change Disk Category: This involves converting the disk type, for example, upgrading from a Standard Performance Disk to a Premium Performance Disk. With default disk performance of a 200GB disk, you may encounter etcd slow requests failures, such as below: │ OPCT-010A │ │ fail │ etcd logs: slow requests: average should be under 500ms │ <=500.00 ms │ 518.271 │ │ OPCT-010B │ │ fail │ etcd logs: slow requests: maximum should be under 1000ms │ <=1000.00 ms │ 1551.514 In this case, running etcd on a dedicated data disk is a recommended approach to improve control plane performance.

### 9.3 why do we need to perform a deta clone in Section

**4.1.5?**

As detailed in Section 4.1.5, when creating the ECS instance, we utilized a QCOW2 image converted from the original ISO file as the initialization image, rather than mounting the ISO directly. This approach is necessary because Apsara Stack supports image formats such as VHD and QCOW2 for ECS instances, but does not support direct booting from mounted ISO files. In this context, a secondary issue arose: when using QCOW2 images in ApsaraStack, the system does not support selecting a specific boot disk and is restricted to booting solely from the default system disk. To resolve this, as described in Section 4.1.5, we

| /dev/vda |   | . Thi |
|---|---|---|
| n to | /dev/vdb |   |

executed commands to clone the data from /dev/vdb to /dev/vda. This ensured that the operating system could access the data originally written to /dev/vdb upon booting from /dev/vda. Subsequently, we issued commands to wipe the original data from /dev/vdb. Page 158
