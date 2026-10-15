---
title: "OpenTrek AI Studio Product Introduction 20260630"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 OpenTrek AI Studio Product Introduction 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/AI%20Studio/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek%20AI%20Studio%20Product%20Introduction%2020260630.pdf"
converter: line-classifier (PyMuPDF)
---

# OpenTrek AI Studio Product Introduction 20260630

## AI Studio

AI Studio is a full-stack AI PaaS service platform for Apsara Stack. The platform provides AI developers with an AI engineering platform that includes dataset management, model development, model training, and model management.

### Features

In terms of the functional architecture, AI Studio is divided into four layers: resources, model development and training, model service, and operation.
1. **AI resource layer:** You can use computing resources in the form of bare metal and EGS.
You can use multiple types of local computing resources, such as Haoguang and Ascend, to meet the requirements of different computing power scenarios.
2. **Model development and training layer:** provides three model training methods: visual
modeling, notebook modeling, and task modeling. It supports data sets of different storage types such as OSS Object Storage Service and CPFS file systems. It also supports mainstream model training frameworks such as TensorFlow, PyTorch, DeepSpeed, and Megatron. Comprehensive model training capabilities, such as integrated model development, training monitoring, training results recording, and deployment of trained models, are provided for standalone and distributed training scenarios.
3. **Model service layer:** supports online model service and batch inference, real-time
monitoring of model service performance, and resource scaling configurations to ensure the stability of external services in a timely manner.
4. **AI operation:** You can Resource Management resources and training tasks at different
levels and control metering and quotas to meet your requirements in intelligent computing operation scenarios.

### Benefits

This topic describes the benefits of AI Studio.

**One cloud with multiple computing power**

Built on the AI computing power infrastructure provided by Apsara Stack, AI Studio allows users to select the appropriate computing power type for their specific scenarios. It supports multiple mainstream domestic GPU chips to meet various requirements for model training, inference, and other scenarios in government and enterprise environments.

**Systematic model training capabilities for the entire process**

AI Studio delivers integrated capabilities for the entire model training process through both single-machine and distributed training scenarios. These capabilities include model development, training monitoring, training result recording, and model listing.

**High availability**

Control services and model inference are designed with high availability. When a node of an online service or control service fails, other nodes automatically continue to provide services, ensuring uninterrupted operation.

**Open and efficient**

Models trained on the AI Studio platform or provided by users can be imported into the model marketplace through AI Studio, enabling users to efficiently manage and share models.

### Common scenarios

| Module |  | Description |
|---|---|---|
| Overview |  | Displays the statistics on task modeling, online services, and datasets in AI Studio. This allows you to intuitively and accurately understand the status of AI Studio. |
| Data Manag ement | Data Labeling | Supports manual annotation and automatic annotation. Supports annotation of image and text data. You can view and export annotation task results. Supports annotation task distribution for collaborative annotation and approval. Supports data processing algorithms. Note Only classification algorithms for structured data are provided. Unstructured data is not supported. |

AI Studio products can be applied to scenarios such as model development, model training, and model online services.

**Model Development**

Algorithm engineers or algorithm scientists can use Notebook modeling to develop models in the Notebook editor.

**Model Training**

Users can create task modeling tasks to perform standalone and distributed training on TensorFlow and PyTorch framework models. AI Studio can also monitor the resource usage and status during the training process to ensure the stability of the training process.

**Model Evaluation**

AI Studio supports issue evaluation tasks. After you associate an evaluation dataset with an evaluation task and set the relevant runtime environment, you can create an evaluation task. Model evaluation can be run at regular intervals.

**Elastic Algorithm Service (EAS)**

Deploy the model and provide the model API calling service.

### Functions and features

This topic describes the features of AI Studio.

|  | Dataset | Allows you to manage data in a centralized manner. You can upload processed training or evaluation data to a dataset and select the dataset during modeling or model evaluation. You can also view, upload, delete, and share datasets. Note To upload data to a dataset, make sure that the data is transferred to Object Storage Service (OSS) or Cloud Parallel File Storage (CPFS). |
|---|---|---|
|  | Data Generation | Allows you to increase the data volume of a dataset by using data generation if the data in the dataset is insufficient. |
|  | Visualized Modeling | Provides hundreds of AI algorithms that can be applied to various scenarios, such as product recommendation, financial risk control, or advertising prediction. Large-scale distributed training and workflow orchestration for streaming and batch processing are also supported. The following features are provided: Allows you to create, view, modify, clone, and run workflows. Allows you to view workflow tasks. Allows you to create a workflow by using a preset template or a custom template. Provides built-in algorithm libraries. Supports instance monitoring, including the instance CPU, memory, GPU, and network monitoring. This feature depends on Prometheus and CloudMonitor. Allows you to deploy models as online services. |

| Model Trainin g |  |  |
|---|---|---|
|  | Notebook Modeling | Provides an online interactive development environment. Notebook eliminates the need for users to prepare the development environment and helps users easily manage datasets, code, and models. The following features are provided: Allows you to create Notebook modeling instances. Allows you to adjust resource quotas for instances. Allows you to export instances as images. Allows you to change instance configurations. Allows you to view, stop, and start instances. Allows you to view instance events. Supports Visual Studio Code and JupyterLab editors. |
|  |  | Note The same instance supports two types of editors. You can view the same file directory in two development environments. Supports SSH remote connections. Supports multi-person collaborative development. Supports instance monitoring, including the instance CPU, memory, GPU, and network monitoring. This feature depends on Prometheus and CloudMonitor. Allows you to save models. |

|  | Task Modeling | Allows you to create standalone or distributed training tasks, and manage the lifecycle of tasks such as monitoring and deletion. Allows you to create, view, delete, start, and pause training tasks. Allows you to adjust resource quotas for tasks. Allows you to view task events and node events. Allows you to save models. Supports automatic fault tolerance. If a training task fails, the instance is restarted. Supports health checks. Before a training task starts, the computing power and network performance of the instances used for training are checked, and the instances with performance bottlenecks are restarted. Supports task monitoring, including the instance CPU, memory, GPU, and network monitoring. This feature depends on Prometheus and CloudMonitor. Allows you to view task logs. Supports checkpoint-based resumable training. You can select a checkpoint to resume a training task within seconds. Note The checkpoint-based resumable training feature depends on CPFS. Allows you to adjust the priority of tasks. You can view the task list on the Task Modeling page and manually adjust the priority. Supports TensorBoard for visualized task running and analysis. |
|---|---|---|
| Model Servic e | Online | Allows you to deploy models as model API services. This facilitates the development and usage of AI applications. Allows you to deploy, stop, and start online services. Allows you to view the details of services. Allows you to scale resources. Supports scaling. Allows you to upload a README file including online service descriptions. Only a PDF file can be uploaded. |
|  | Service | Supports service monitoring, including the instance CPU, memory, GPU, and network monitoring. This feature depends on Prometheus and CloudMonitor. Supports resource inference of Elastic GPU Service. This features depends on Container Service for Kubernetes (ACK) and Elastic GPU Service. Supports distributed inference by using an AI gateway. Allows you to perform throttling on online services. |

|  | Canary Group | Provides a unified access portal for multiple online services. Traffic allocation can be used to achieve smooth service publishing and unpublishing. Allows you to create, modify, and delete canary groups. Allows you to add multiple online services to a canary group. Allows you to perform throttling on online services by using canary groups. |
|---|---|---|
|  | Batch Inference | Supports inference on multiple data entries and generates an inference result file. Allows you to create, start, and pause batch inference tasks. |
|  |  | Allows you to configure timing settings for batch inference tasks. |
| Model Manag ement | Models | Allows you to perform model self-registration and model lifecycle management. The following features are provided: Allows you to upload, modify, deploy, share, enable, and disable models. Note To upload a model, make sure that the model is transferred to OSS or CPFS. Allows you to convert the format of a model from Megatron to Hugging Face or ModelScope, or from Hugging Face or ModelScope to Megatron. Allows you to manage model versions. Allows you to upload a README file including online service descriptions. Only a PDF file can be uploaded. Supports system models, custom models, and Model as a Service (MaaS) models. |
|  | Model Tuning | Supports the following tuning methods: supervised fine-tuning (SFT), direct preference optimization (DPO), and group relative policy optimization (GRPO). You can specify the fine-tuning method and select appropriate fine-tuning data and parameters. The model performance after fine-tuning better meets your business requirements. Allows you to create model tuning tasks to optimize model training. Allows you to view, modify, stop, start, and delete tuning tasks. |
|  | Model Evaluation | Allows you to create an evaluation task after you specify the evaluation dataset and set the relevant environment. The evaluation algorithm and evaluation result path need to be set in the evaluation code. You can create general evaluation tasks and scheduled evaluation tasks. |
|  | Model Conversion | Allows you to convert the format of a foundation model from Megatron to Hugging Face or ModelScope for inference, or from Hugging Face or ModelScope to Megatron for training. |

|  | duction·AI Studi |  |
|---|---|---|
| AI Resour ce Manag ement | AI Resource Pool | Allows you to create an AI resource pool to centrally manage the physical computing power required by the AI management platform and provide underlying computing power for model development, training, and tuning tasks. Allows you to create, view, modify, and delete AI resource pools. Supports GPU-accelerated cloud computing power that depends on ACK and Elastic GPU Service, and supports GPUs such as A100 and Hygon K100. Supports bare metal computing power that depends on Bare Metal Computing Platform (BMCP) and ACK, and supports A100, Hygon K100, Ascend 910B, and APG810E. |
|  | Resource Quota | Allows you to allocate resources from a resource pool. After a resource quota is associated with a workspace, you can use the resource quota in the workspace for AI development and training. This way, you can use and manage resources in a flexible and efficient manner. Allows you to create, modify, and delete resource quotas. Allows you to adjust specifications. Supports resource set sharing. Supports image, model, and computing power matching. Supports GPU sharing. |
| Agent Develo | Dify Open Source Edition | Allows you to deploy open source Dify instances based on your habits. This provides end-to-end capabilities from model training and inference to AI agent development and debugging, and accelerates the implementation of model services tailored to customer business scenarios. |
| pment Platfor m |  |  |
| AI Asset Manag ement | Image Repository | Provides images of development and runtime environments for model development and training. This helps you quickly create development and training tasks. Allows you to upload, delete, modify, and share images. Note Image upload depends on Container Registry Standard Edition or Advanced Edition. Allows you to manage image versions. Supports preset images. |
|  | Code Build | Allows you to compile the code that is required for training and manage the code in a centralized manner by creating a code build. This improves the efficiency of code configuration in model training tasks. You can create, modify, delete, or share code builds. |
|  | Data Accelerator | Accelerates the loading of datasets and models during model training and inference. This improves the efficiency of training and inference. You can create data accelerators to prefetch and cache datasets and model data stored in OSS. |

|  | AI Studio Product Studio | Intro |
|---|---|---|
|  | Software Source | Obtains software packages such as PyPI, YUM, Debian, and Conda packages from the Internet and caches them locally to form offline stores. Local offline stores can provide services without the need for Internet connections. |
| Syste m Config uration s | Synchronize Resources | Allows you to synchronize inference images from the BMCP image center to the public image repository of AI Studio. |
