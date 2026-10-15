---
title: "Operation Orchestration Service Product Introduction 20250728"
product_version: "V3.18.6"
pdf_pages: 9
source_pdf: "1f455df16a320e9b_Alibaba Cloud Apsara Stack V3.18.6 Operation Orchestration Service Product Introduction 20250728.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%BF%90%E7%BB%B4%E7%BC%96%E6%8E%92%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Operation%20Orchestration%20Service%20Product%20Introduction%2020250728.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Operation Orchestration Service Product Introduction 20250728

## Table of Contents

- 1 Service details
- 2 Benefits
- 3 Scenarios
- 4 Features

ils

## 1 Service details

You can use templates to define O&M tasks, including task execution sequence, task input, and task output. Operation Orchestration Service (OOS) can automatically execute the O&M tasks after you define the tasks in the templates. OOS can be used to manage other Alibaba Cloud services, such as Elastic Compute Service (ECS), ApsaraDB RDS, Server Load Balancer (SLB), and Virtual Private Cloud (VPC).

**Template**

OOS uses templates to define the O&M operations that require orchestration. The template content is specified in the YAML or JSON format. The templates are classified into public templates and custom templates.

**Execution**

OOS supports a variety of execution modes, including automatic execution, semi-automatic execution, and manual execution. This helps you complete diverse O&M tasks. Automatic execution: We recommend that you execute a template in this mode in the test environment first. This way, you can have a better understanding of the O&M operations performed by using the template. If the test result meets the expectations, you can execute the template in this mode in the production environment. Manual execution: This execution mode is similar to debugging. If you want to know more about the execution of each task, we recommend that you use the manual execution mode.

## 2 Benefits

Operation Orchestration Service (OOS) can help enterprises better standardize, manage, and perform automated O&M operations. You can define required operations by using templates and execute the operations in the system. This improves the overall efficiency of O&M operations, enhances the security of O&M operations, and reduces manual O&M errors.

**Visualized execution processes and results**

You can view the execution process and the result of a template in the OOS console, including: The input, output, and details of each O&M task The procedure and sequence for executing tasks and redirection errors of failed tasks

**Fully managed service**

OOS provides a fully managed and serverless O&M service that enables automatic execution of O&M tasks. O&M tasks can be automatically executed without consuming your computing resources, such as Elastic Compute Service (ECS) instances. OOS can meet the O&M requirements of startups, small and medium-sized enterprises, and large enterprises. OOS minimizes the effort of enterprises in O&M and allows enterprises to focus on business growth.

**Efficiency in managing multiple O&M tasks at a time**

Managing multiple O&M tasks at a time is more complex than managing a single task. To enhance O&M efficiency, you can use OOS to manage task progress, monitor task status, and locate execution errors.

**Superior authentication and verification systems**

You can use Resource Access Management (RAM) to manage OOS. You can manage and audit permissions on OOS configurations and OOS-based O&M operations on other Alibaba Cloud services. You do not need to worry about the security of configurations and operations.

**Easy-to-use templates**

OOS provides a variety of templates that are easy to use to minimize your effort in creating templates. OOS integrates common O&M operations for popular Alibaba Cloud services and provides easy-to-use templates. This helps improve O&M efficiency. OOS provides public templates for common O&M tasks. You can select a public template and modify the template based on your business requirements.

**Operations as code**

OOS provides templates to standardize common O&M tasks. In OOS, you can manage templates by using code. After you create, review, and publish a template to the production environment, you can use the template to generate O&M tasks. This ensures the security and unification of O&M tasks and helps deliver best practices of operations as code.

**Delegated authorization**

Authorization must be appropriately delegated to O&M engineers. O&M engineers must be granted the required permissions to complete the corresponding O&M tasks. To prevent risks, they cannot be granted higher permissions than required to execute unexpected O&M tasks. OOS provides a delegated authorization solution to meet the preceding O&M requirements. When a high-privileged O&M engineer creates a template, a RAM role can be specified and granted the required permissions to use the template. The high-privileged O&M engineers can also grant a lower-privileged O&M engineer the permissions to execute the template. If the duty of executing the template is transferred to the lower-privileged O&M engineer, accidental operations that require high privileges may be reduced.

## 3 Scenarios

Common O&M scenarios of Operation Orchestration Service (OOS) include executing multiple O&M tasks at a time, updating images, managing approval requests, and managing scheduled O&M tasks. You can create custom templates based on your business requirements.

**Execute multiple O&M tasks at a time**

In some scenarios, you need to perform O&M operations on multiple targets, such as Elastic Compute Service (ECS) instances, to ensure continual business operation and growth. For example, to check the available space of hard disks in multiple ECS instances at a time, you need to perform the following operations: select the ECS instances whose hard disks you want to check, perform the hard disk check by running a Cloud Assistant command, and then view the check results in a centralized manner. OOS provides multiple methods to select instances, including name matching, tag grouping, and resource group classifying.

**Update images**

To ensure a safe runtime environment for ECS instances, you must install the latest patches or update related components. OOS allows you to update ECS instance images. You can generate a new image from a source image, and use the new image for testing and production.

**Manage approval requests**

In many scenarios, you need to manage approval requests to ensure that only expected O&M operations are performed. You can define an ACS::Approve action in a template. This action ensures that an O&M task is approved before the task is executed and that expected O&M tasks are executed without mistakes.

**Manage scheduled tasks**

Some O&M tasks must be executed as scheduled. For example, each morning, you need to delete all Object Storage Service (OSS) files generated by the previous tests to prepare a clean runtime environment for the next test. In this case, you can create a template and schedule delete operations in the morning.

## 4 Features

This topic describes the features of CloudOps Orchestration Service (OOS).

| Feature | Description |
|---|---|
| Scheduled O&M | OOS allows you to execute O&M tasks at the specified points in time. For example, you can create a template and execute it at 00:00 every day to delete Object Storage Service (OSS) files that are generated by tests within an account on the previous day. This produces a new and clean test environment every day to prevent subsequent test results from being affected. |
| Public templates | OOS provides templates for multiple scenarios, such as instance management, command execution, image management, data backup, security audit, scheduled execution, auto scaling management, and cross-region replication. |
| Custom templates | You can use custom templates to meet your O&M requirements. |
| Manage executions | You can manage the entire lifecycle of task executions created by using templates. You can view the execution status, cancel the execution, delete the execution, and obtain detailed execution logs and output information. This ensures the transparency and accuracy of task execution to better meet automated O&M requirements. |
