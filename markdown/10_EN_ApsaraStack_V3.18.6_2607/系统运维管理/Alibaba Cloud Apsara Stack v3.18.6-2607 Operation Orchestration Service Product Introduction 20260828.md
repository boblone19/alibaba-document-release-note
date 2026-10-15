---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 8
source_pdf: "066e3a0f26c3e9b1_Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Product Introduction 2026082"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E7%B3%BB%E7%BB%9F%E8%BF%90%E7%BB%B4%E7%AE%A1%E7%90%86/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Operation%20Orchestration%20Service%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Product Introduction 20260828

## Table of Contents

- 1 Product details
- 2 Benefits
- 3 Use cases
- 4 Features

ails

## 1 Product details

A template defines tasks, their execution order, inputs, and outputs. Running the template automates these tasks. OOS integrates with multiple cloud products, such as ECS, RDS, SLB, and VPC.

**Templates**

OOS uses templates to define operation orchestration tasks. Templates support both YAML and JSON formats and come in two types: public templates and custom templates.

**Execution**

OOS supports multiple execution modes, including automatic execution and step-by-step execution. Automatic execution: We recommend first running the template in a test environment to understand its operations and verify the results before deploying it to a production environment. Step-by-step execution: Use this debugging mode to closely examine how each task in the template runs.

## 2 Benefits

This topic describes the key benefits of OOS.

**Standardized automated O&M**

OOS helps you standardize O&M procedures by defining them as reusable templates. These templates can be run automatically, which significantly improves operational efficiency, enhances security, and reduces manual errors.

**Visual execution tracking**

OOS provides complete visibility into execution processes and results. You can: View execution details, input parameters, and output results for each task. Visualize task execution workflows and error-handling paths to quickly locate and resolve issues.

**Fully managed automation**

OOS provides a fully managed and serverless automation engine. Executions run without consuming your computing resources, such as ECS instances. This model supports the automated O&M needs of businesses of all sizes, from startups to large enterprises. This fully automated approach eliminates manual supervision, so you can focus on business growth.

**Efficient batch task management**

In traditional scenarios, managing batch tasks is significantly more complex than managing a single task. OOS simplifies large-scale operations by providing real-time progress tracking, runtime status statistics, and rapid error detection, which improves overall O&M efficiency.

**Comprehensive authentication and auditing**

OOS integrates with RAM to provide fine-grained permission control. All actions, including operations within OOS and tasks that interact with other cloud services, support both authentication and auditing. This ensures that every operation is secure and fully traceable.

**Rapid template creation**

The OOS template builder makes it easy to create templates without starting from scratch. OOS offers built-in integrations with popular cloud services to simplify template creation, reduce scripting complexity, and improve your overall O&M efficiency. For common O&M scenarios, you can use a public template. Simply copy and modify an existing template to meet your specific requirements.

**Operations as Code**

OOS lets you manage operational tasks as code by defining them in templates that follow standard code lifecycle practices. After a template is created, reviewed, and synchronized with a production account, subsequent O&M tasks are run exclusively from standard templates. This practice ensures that your operations are secure, standardized, and auditable, which helps you implement Operations as Code best practices.

## 3 Use cases

Operation Orchestration Service (OOS) supports a variety of common operational scenarios. It enables standardized operations and lets you create custom templates for your specific business needs. This topic describes common use cases for OOS.

**Batch operations**

You can run the same operational command on multiple targets, such as ECS instances. This is ideal for large-scale, standardized tasks that help ensure business continuity and system health. For example, to check the remaining disk space on multiple ECS instances at once, first select the target instances by using methods such as name matching, grouping by tags, or grouping by resource groups. Then, use a Cloud Assistant command to perform the disk check and view all results in one place.

**Update images**

OOS automates image updates to keep your ECS instance environments secure and compliant, letting you install security patches, upgrade component dependencies, and more. The process starts with a source image, applies updates step-by-step, and creates a new image for testing and production. This approach provides version control and traceability for your images, which helps prevent environment drift caused by manual changes.

**Approval operations**

For high-risk or sensitive tasks, you can introduce a manual approval step to ensure an operation is necessary and compliant. By adding an approval action ( `ACS::Approve` ) to a template, OOS pauses the operation and waits for human approval before execution. This helps prevent accidental changes and unnecessary resource usage. This is useful for scenarios such as: Changes to a production environment, such as restarting a database or modifying configurations. Releasing or deleting resources. Executing batch commands that require sensitive permissions. OOS helps you prevent operational errors and meet your organization's IT governance and audit requirements.

**Scheduled tasks**

You can schedule recurring operational tasks to run automatically. This reduces manual effort and helps maintain a stable environment. For example, in a testing scenario, you might need to automatically clear files in an OSS object storage bucket at midnight every day to ensure each test starts in a clean environment. You can create a template that runs daily to keep your test environment pristine and prevent previous test data from affecting new results.

## 4 Features

This topic describes the features of CloudOps Orchestration Service (OOS).

| Feature | Description |
|---|---|
| Scheduled O&M | OOS allows you to execute O&M tasks at the specified points in time. For example, you can create a template and execute it at 00:00 every day to delete Object Storage Service (OSS) files that are generated by tests within an account on the previous day. This produces a new and clean test environment every day to prevent subsequent test results from being affected. |
| Public templates | OOS provides templates for multiple scenarios, such as instance management, command execution, image management, data backup, security audit, scheduled execution, auto scaling management, and cross-region replication. |
| Custom templates | You can use custom templates to meet your O&M requirements. |
| Manage executions | You can manage the entire lifecycle of task executions created by using templates. You can view the execution status, cancel the execution, delete the execution, and obtain detailed execution logs and output information. This ensures the transparency and accuracy of task execution to better meet automated O&M requirements. |
