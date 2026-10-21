---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek AI Studio Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 15
source_pdf: "eeacbdd56b18b059_Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek AI Studio Product Introduction 20260831.pd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/OpenTrek/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20OpenTrek%20OpenTrek%20AI%20Studio%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek AI Studio Product Introduction 20260831

## Table of Contents

- 1 AI Studio
  - 1.1 Features
  - 1.2 Benefits
  - 1.3 Common scenarios
  - 1.4 Functions and features

## 1 AI Studio

AI Studio is a full-stack AI PaaS service platform for Apsara Stack. The platform provides AI developers with an AI engineering platform that includes dataset management, model development, model training, and model management.

### 1.1 Features

In terms of the functional architecture, AI Studio is divided into four layers: resources, model development and training, model service, and operation.
1. **AI resource layer:** You can use computing resources in the form of bare metal and EGS.
You can use multiple types of local computing resources, such as Haoguang and Ascend, to meet the requirements of different computing power scenarios.
2. **Model development and training layer:** provides three model training methods: visual
modeling, notebook modeling, and task modeling. It supports data sets of different storage types such as OSS Object Storage Service and CPFS file systems. It also supports mainstream model training frameworks such as TensorFlow, PyTorch, DeepSpeed, and Megatron. Comprehensive model training capabilities, such as integrated model development, training monitoring, training results recording, and deployment of trained models, are provided for standalone and distributed training scenarios.
3. **Model service layer:** supports online model service and batch inference, real-time
monitoring of model service performance, and resource scaling configurations to ensure the stability of external services in a timely manner.
4. **AI operation:** You can Resource Management resources and training tasks at different
levels and control metering and quotas to meet your requirements in intelligent computing operation scenarios.

### 1.2 Benefits

This topic describes the benefits of AI Studio.

**One cloud with multiple computing power**

Built on the AI computing power infrastructure provided by Apsara Stack, AI Studio allows users to select the appropriate computing power type for their specific scenarios. It supports multiple mainstream domestic GPU chips to meet various requirements for model training, inference, and other scenarios in government and enterprise environments.

**Systematic model training capabilities for the entire process**

AI Studio delivers integrated capabilities for the entire model training process through both single-machine and distributed training scenarios. These capabilities include model development, training monitoring, training result recording, and model listing.

**High availability**

Control services and model inference are designed with high availability. When a node of an online service or control service fails, other nodes automatically continue to provide services, ensuring uninterrupted operation.

**Open and efficient**

Models trained on the AI Studio platform or provided by users can be imported into the model marketplace through AI Studio, enabling users to efficiently manage and share models.

### 1.3 Common scenarios

AI Studio products can be applied to scenarios such as model development, model training, and model online services.

**Model Development**

Algorithm engineers or algorithm scientists can use Notebook modeling to develop models in the Notebook editor.

**Model Training**

Users can create task modeling tasks to perform standalone and distributed training on TensorFlow and PyTorch framework models. AI Studio can also monitor the resource usage and status during the training process to ensure the stability of the training process.

**Model Evaluation**

AI Studio supports issue evaluation tasks. After you associate an evaluation dataset with an evaluation task and set the relevant runtime environment, you can create an evaluation task. Model evaluation can be run at regular intervals.

**Elastic Algorithm Service (EAS)**

Deploy the model and provide the model API calling service.

### 1.4 Functions and features

This topic describes the functions and features of AI Studio.

**Functions and features of Apsara Uni-manager Operations**

**Console**

| Feature |   | Description |
|---|---|---|
| Overview |   | The system collects and displays the resource usage of task modeling, online services, and datasets in AI Studio, allowing you to intuitively and accurately understand the system status. |
|   | Data annotation | Navigate from the AI Studio console to the Bailian exclusive large model console for Data Annotation > Task Management. Important You must purchase the Bailian exclusive edition data annotation product. Otherwise, the data annotation menu item does not appear. |

| Data mana geme nt |   |   |
|---|---|---|
|   | Datasets | The system provides centralized data management. You can upload processed training or evaluation data to datasets and directly associate the datasets with model modeling and model evaluation. The system supports viewing, uploading, deleting, and sharing datasets. Note Uploading datasets requires data transmission to OSS, CPFS, or APFS. |
|   | Data processing | Navigate from the AI Studio console to the Bailian exclusive large model console for Data Processing > data processing tasks. Important You must purchase the Bailian exclusive edition data processing product. Otherwise, the data processing menu item does not appear. |
|   | Visual modeling | The system includes more than 100 built-in AI workflow components that cover scenarios such as product recommendation, financial risk control, and advertisement prediction. The system supports large-scale distributed training and stream-batch integrated workflow orchestration. The specific features are as follows: Create, view, modify, clone, run, and stop workflows. View workflow tasks and set execution cycles. Roll back versions and diagnose tasks. Create workflows by using preset templates or custom templates. Use the built-in algorithm library. Monitor instances, including CPU, memory, GPU, and network metrics. This feature depends on Prometheus and CMS. Deploy models to online services. Create custom components and custom templates. |

|   | Notebook modeling | Notebook is an online interactive development environment that eliminates the need to prepare a development environment and helps you manage datasets, code, and models. The Notebook modeling features are as follows: Create Notebook modeling instances. Assign resource groups to instances. Export instances to images. Modify instance configurations. View, stop, and start instances. View instance events. Use VS Code and JupyterLab editors. Note A single instance supports both editors, and you can view the same file directory in both development environments. Connect remotely over SSH. Enable collaborative development among multiple users. Monitor instances, including CPU, memory, GPU, and network metrics. This feature depends on Prometheus and CMS. Save models. Set a username and password to protect the Notebook instances that you create. Enable SSH access and assign a classic SLB instance to the Notebook instance. |
|---|---|---|
| Model traini ng |   |   |

|   | Task modeling | Create custom modeling tasks for single-host or distributed training, and manage the task lifecycle by monitoring or deleting tasks. Use suite-based modeling to create modeling tasks with one click by configuring the input, output, and parameters of a suite. Create, view, modify, clone, delete, start, and pause training tasks. Assign resource groups to tasks. View task events and node events. Save models. Enable automatic fault tolerance to restart instances when training tasks fail. Run health checks to test the compute resources and network performance of assigned instances before formal training, and restart instances that have performance bottlenecks. Monitor tasks, including CPU, memory, GPU, and network metrics of instances. This feature depends on Prometheus and CMS. View task logs. Configure multiple OSS mount paths. Resume training from a checkpoint. You can select a checkpoint to resume a training task for recovery within seconds. Note The checkpoint-based training resumption feature depends on CPFS. Adjust task priorities by viewing the current task modeling task list in a resource group and manually changing the priority. Integrate TensorBoard code for visual analysis of task execution. |
|---|---|---|
|   | Model fine-tuning | The system provides fine-tuning and reinforcement learning capabilities to meet your requirements for domain-specific fine-tuning and reinforcement learning based on large models. Create fine-tuning tasks by using custom configurations or suite configurations. View, edit, stop, start, and delete fine-tuning tasks. Integrate TensorBoard for model fine-tuning and training. |

| Model servic es | Online services | Online services expose model APIs after you deploy models, which facilitates AI application development and usage. Deploy, stop, and start online services. Use custom deployment, A-Speed high-performance deployment, and inference suite deployment. View service details. Scale resources in and out. Enable auto scaling. Upload a README document. You can upload a documentation file for the online service. Only PDF files are supported. Monitor services, including CPU, memory, GPU, and network metrics of instances. This feature depends on Prometheus and CMS. Perform inference on EGS resources. This feature depends on ACK and EGS. Configure multiple OSS mount paths. When the third-party storage path switch is turned on, the system validates the file path values in third-party storage. When the third-party high-speed network switch is turned on, you can build a third-party network solution. However, the platform does not guarantee availability or functionality. Configure throttling policies based on service QPS, TPM, and concurrency. Canary groups: Provide a unified access entry point for multiple online services and enable smooth service rollout and rollback through traffic splitting. One-click stress testing: Create stress testing tasks to benchmark the performance of inference services. |
|---|---|---|
|   | Batch inference | Batch inference tasks run inference on large volumes of data and generate inference result files. Create, start, and pause batch inference tasks. Schedule batch inference tasks. When the third-party storage path switch is turned on, the system validates the file path values in third-party storage. |

| Model mana geme nt | Model gallery | The model gallery connects to external third-party model marketplaces to provide timely access to the latest models in the industry. You can directly fine-tune, evaluate, and deploy these models to provide model services. The model gallery includes system models, custom models, Qwen exclusive models, and MaaS marketplace models. AI Studio comes with preset open-source models from the DeepSeek, Qwen, Llama, and ChatGLM series. You can deploy system models and test them through conversations. For custom models, you can import, view, test, edit, and delete models. Note To upload a model, you must transfer the model to OSS. For Qwen exclusive models, you can import, view, deploy, and enable or disable models. The system downloads MaaS marketplace models from third-party MaaS marketplaces. You can deploy and test downloaded models immediately. |
|---|---|---|
|   | Model workshop | Model quantization: The system supports multiple floating-point quantization strategies. Select an appropriate quantization method based on available compute resources. The resulting quantized model significantly reduces GPU memory usage and accelerates inference. Save successfully quantized models to the model repository. Delete model quantization tasks. Model conversion: Model conversion enables bidirectional conversion between the Megatron format commonly used for large model training and the HuggingFace and ModelScope formats commonly used for large model inference. Save converted models to the model repository. Delete model conversion tasks. |

|   | Model evaluation | The system evaluates model performance. After you associate an evaluation dataset and configure the runtime environment, you can create an evaluation task. You must define the evaluation algorithms and result output in the evaluation code. The system supports both standard and scheduled evaluation tasks. Create automatic evaluation tasks and benchmark evaluation tasks. View, edit, stop, restart, and delete evaluation tasks. View evaluation results. Compare evaluation tasks. Diagnose evaluation tasks and view diagnosis results. Monitor metrics of model evaluation tasks, such as CPU usage, CPU utilization, and memory usage. |
|---|---|---|
| AI | AI resource pools | AI resource pools provide centralized management of the physical compute resources required by the AI management platform and deliver infrastructure support for model development, training, and tuning tasks. Create, view, edit, and delete AI resource pools. Use GPU cloud servers. This feature depends on ACK and GPU cloud servers and supports A100, Hygon K100, and other GPU types. Use bare metal compute resources. This feature depends on BMCP and ACK and supports A100, Hygon K100, Ascend 910B, and APG910E. Configure classic networks. The system issues TLS certificates for the domain names or classic network addresses of resource pools to enable HTTPS access for instances in the resource pools. Configure third-party storage. Enable or disable the third-party high-speed network to support distributed training and inference tasks. Set the sharing scope of resource pools, including the current organization and its subordinate organizations, the current resource set, and the current organization. Support dual-stack IPv4 and IPv6 protocols. |
| resou rce mana geme nt |   |   |

|   | Resource groups | Resource groups allocate resources from resource pools. After you bind a resource group to a specific workspace, you can use the resource group for AI development and training within that workspace to achieve flexible and efficient resource management. Resource groups are divided into dedicated resource groups and shared resource groups. Create, edit, and delete resource groups. Adjust specifications. Share resource sets. Match images, models, and compute resource information. Add elastic scheduling policies. |
|---|---|---|
|   | Image repositories | Image repositories provide development and runtime environment images for model development and training to help you quickly build development and training tasks. Images are divided into public images and custom images. For custom images, you can upload, delete, edit, and share images. Note Image upload depends on ACR Standard Edition or Advanced Edition. Manage image versions. Use preset images. |
| AI asset mana geme nt |   |   |
|   | Code sets | Code sets centralize the custom code required for model training, which improves code configuration efficiency in model training tasks. Create, edit, and delete code sets. Configure the sharing scope of code sets. |
|   | Data accelerator | Data accelerators speed up dataset and model loading during model training and inference to improve training and inference efficiency. Create data accelerators to preheat and cache datasets and model data stored in OSS. After you create a data accelerator, you must reference it when you create Notebook modeling, task modeling, online services, model evaluation, batch inference, or model tuning jobs for the accelerator to take effect. |

|   | Training and inference suites | A training and inference suite works as a one-click deployment package that preconfigures the images, code, startup scripts, and GPU resource requirements for model execution. After you bind a suite to your model, you can select the suite during training, inference, tuning, and quantization to skip complex configuration and accelerate deployment. In task modeling, model tuning, and online service scenarios, when you select a model weight and a required suite, the system displays the suites associated with the model. |
|---|---|---|
|   | Software sources | When the Internet is accessible, the system retrieves software packages from PyPI, YUM, Debian, and Conda and caches them locally to build an offline source. The local offline source continues to serve requests for cached software packages even when the Internet is unavailable. |
| Syste m confi gurati on | Resource synchronization | Synchronize inference images from the BMCP image center of the bare metal compute platform to the public image repository of AI Studio. |
|   | User priority | User priority defines the maximum task priority that each user can assign. The value ranges from 1 to 10, where a larger value indicates a higher priority. |
|   | User API key | Create and manage API keys for users and bind them to the required online services. |

**Features of the Apsara Uni-manager Operations Console**

| Feature |   | Description |
|---|---|---|
| Resource availability check | Resource pool | Check the availability of AI resource pools and add features. |
|   | Resource group | Check the availability of resource groups and add features. |
| Toolbox | Kubectl | Use commands to query pods in a resource pool. |
|   | Chip model registration | The system includes preset supported chip models. This feature allows you to manually register additional chip models. |
|   | Feature registration | Register required features for AI Studio in advance, including the chip models, cluster types, and feature types associated with each feature. |
| 4 | > Document Version: 2026083 |   |

|   | Import assets | Import assets through the console. |
|---|---|---|
| System settings |   | Isolate the AI Studio training push task list by creator and configure a toggle for this setting. Configure third-party storage path modes, including the open path mode and the mandatory path mode. Note The involved feature modules include task modeling, Notebook modeling, online services, and batch inference. Enable or disable the third-party high-speed network to support distributed training and inference tasks. After you turn on the quantization suite toggle, the system displays quantization suites in the public suite module, the model-suite association module, and the model quantization module. |
