---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 7
source_pdf: "f4d5bc079dc42c88_Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Product Introduction 20260828"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B5%84%E6%BA%90%E7%BC%96%E6%8E%92/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Resource%20Orchestration%20Service%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Product Introduction 20260828

## Table of Contents

- 1 What is ROS?
  - 1.1 Overview
  - 1.2 Benefits
  - 1.3 Common scenarios
  - 1.4 Functions and features

Resource Orchestration Service ?

## 1 What is ROS?

Resource Orchestration Service (ROS) is a service provided by Apsara Stack to allow you to manage cloud computing resources in a simplified manner. You can author a stack template based on the template syntax that is defined in ROS. In the template, you can define the required cloud computing resources, such as Elastic Compute Service (ECS) and ApsaraDB RDS instances, and the dependencies between resources. The ROS engine automatically creates and configures all resources in a stack based on the template. This helps achieve automatic deployment and O&M. ROS helps you build infrastructures in the cloud to implement Infrastructure as Code (IaC). Compared with the calls for API operations of cloud services, ROS significantly improves the efficiency of your business.

### 1.1 Overview

ROS is a service provided by Apsara Stack to allow you to manage cloud computing resources in a simplified manner. You can use stacks and templates to achieve automatic deployment and O&M of the resources.

**Stack**

ROS manages a group of Apsara Stack resources in a centralized manner based on the logic of a stack. You can create, update, recreate, and delete Apsara Stack resources by stack.

**Template**

A template is a JSON text file that is encoded in UTF-8. Templates are used to create stacks and serve as the blueprints for infrastructures and architectures. You can define the configurations of Apsara Stack resources in a template to specify the dependencies between the resources. An ROS template is a standardized method that is used to deliver resources and applications. Independent software vendors (ISV) can use ROS templates to deliver a holistic system or solution that encompasses cloud resources and applications. This way, Apsara Stack resources can be integrated with the software systems for centralized delivery. Developers and administrators can define the required Apsara Stack resources, such as ECS and ApsaraDB RDS instances, and the dependencies between resources in a template. The ROS engine automatically creates and configures all resources in a stack based on the template. This helps achieve automatic deployment and O&M.

### 1.2 Benefits

ROS can help you model and configure your Apsara Stack resources. After you create a template in which the required resources such as ECS and ApsaraDB RDS instances are defined, ROS creates and configures the resources based on the template. This way, you can manage resources in a simplified manner.

**Improved deployment efficiency**

You can use a template in ROS to provision your entire cloud environment. As your business grows, you can use the template to deploy cloud resources in new zones. You can also use the template to deploy the development, testing, and production environments. This helps improve the deployment efficiency and reduce the risk of human errors.

**Reduced cost**

Resource Orchestration Service ? If you use a template in ROS to provision your cloud environment, ROS can automatically deploy or delete a large number of stacks based on your business requirements. ROS provides elastic cloud resources to help reduce costs.

**Compliance control**

ROS is an IaC service. You can use templates to define infrastructures. When you want to create or update a template, you can review the code. Continuous integration (CI) and continuous delivery (CD) are integrated into templates to ensure that the templates can meet the management regulations of your organization and improve the security compliance of your cloud environment.

### 1.3 Common scenarios

ROS can be used in a wide range of scenarios. You can use ROS to migrate your business to the cloud, deploy multiple resources at a time, and distribute environments based on your business requirements. ROS uses only approved templates to deploy cloud environments. This helps meet IT compliance requirements and minimize financial risks.

**Migration of business to the cloud**

Based on the best practices accumulated from Apsara Stack, ROS provides a solution to help you deploy all resources in a few steps and optimize the cloud architecture. No professional IT skills or experience in cloud architecture design are required.

**On-demand deployment of resources**

You can use a template to deploy multiple application runtime environments at a time in business scaling or DevOps scenarios.

**Business environment distribution**

In centralized IT management scenarios, ROS distributes a standardized environment across regions and accounts to meet the business requirements of each organization and team.

**Cloud environment management**

ROS uses only approved templates to deploy cloud environments. This helps meet IT compliance requirements and minimize financial risks.

### 1.4 Functions and features

ROS serves as an engine that automatically creates and configures all resources in a stack based on a template to make automatic deployment and O&M possible. ROS can help build your own infrastructure in the cloud to implement IaC. Compared with API calls of cloud services, ROS significantly improves business efficiency. This topic describes the features of ROS.

**Template**

| Feature module in the console | Description |
|---|---|

Resource Orchestration Service ?

| My Templates | You can author a stack template based on the template syntax that is defined in ROS. In the template, you can define the required cloud computing resources, such as ECS and ApsaraDB RDS instances, and configure the dependency relationships between resources. The ROS engine automatically creates and configures all resources in a stack based on a template to implement automated deployment and O&M. |
|---|---|

**Stack**

| Feature module in the console | Description |
|---|---|
| Stacks | ROS manages a collection of cloud resources in a centralized manner by using a single unit named a stack. A stack is a collection of Apsara Stack resources. You can create, delete, and clone cloud resources by using a stack. |
