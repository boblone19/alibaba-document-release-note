---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Data Center as a service Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 41
source_pdf: "14b39c2b809c096e_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Data Center as a service Operations and Mainten"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%A3%B8%E6%9C%BA%E7%AE%A1%E7%90%86%20BMS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Stack%20Data%20Center%20as%20a%20service%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Data Center as a service Operations and Maintenance Guide 20260828

## Table of Contents

- 1 What is BMS?
- 2 Getting started
  - 2.1 Work with the BMS Operations Console
  - 2.2 Log in to the BMS Operations Console
- 3 Instance management
  - 3.1 Register an instance
  - 3.2 Batch register instances
  - 3.3 Re-register an instance
  - 3.4 View instance details
  - 3.5 Release an instance
  - 3.6 Restart an instance
  - 3.7 Stop an instance
  - 3.8 Start an instance
  - 3.9 Delete an instance
  - 3.10 Query operation logs
  - 3.11 Modify the properties of an ECS bare metal instance
  - 3.12 Modify the hostname of an instance
  - 3.13 Reset the password of an instance
  - 3.14 Change the gateway port of an ECS bare metal instance
  - 3.15 Log in to the out-of-band console
- 4 Monitoring and alerting
  - 4.1 Instance monitoring
    - 4.1.1 View the monitoring information about bare metal instances
  - 4.2 Alerts of ECS bare metal instances
    - 4.2.1 Query the alerts of ECS bare metal instances
    - 4.2.2 View pending alerts
    - 4.2.3 View handled alerts
    - 4.2.4 Handle alerts
  - 4.3 Alerts of managed instances
    - 4.3.1 Query the alerts of managed instances
    - 4.3.2 View pending alerts
    - 4.3.3 View handled alerts
    - 4.3.4 Handle alerts
- 5 Basic settings
  - 5.1 Image management
    - 5.1.1 Upload a custom image
    - 5.1.2 View custom image details
    - 5.1.3 Delete a custom image
    - 5.1.4 View the details of a public image
    - 5.1.5 Image status management
    - 5.1.6 Export an image
  - 5.2 Network management
  - 5.3 Model management
    - 5.3.1 Add a model
    - 5.3.2 Modify a model
    - 5.3.3 View the details of a model
    - 5.3.4 Delete a model
  - 5.4 GPU settings
    - 5.4.1 Add a GPU
    - 5.4.2 Modify a GPU
    - 5.4.3 Query GPUs
    - 5.4.4 Delete a GPU

## 1 What is BMS?

Bare Metal Service (BMS) is a cloud service that flexibly provides physical servers for tenants on demand through a cloud platform. It is typically used to supply compute resources to services such as core databases, key application systems, and high-performance computing. BMS is deployed in the Apsara Uni-manager Operations Console and allows you to manage physical machines as nodes in a fine-grained manner. For example, you can add or remove physical machines, power on or off physical machines, and deploy systems. After servers are installed and provisioned, you can deploy multiple bare metal devices at a time on an intuitive user interface (UI). Then, you can create high-performance bare metal instances by using these bare metal devices and install different operating systems, including AliOS and CentOS for x86, to meet diverse business requirements. In addition, BMS allows you to manage the full lifecycle of bare metal instances in a fine-grained manner, from instance creation to instance release.

**Characteristics and benefits**

**Full lifecycle management and maintenance**

BMS allows you to manage the full lifecycle of bare metal instances, covering instance registration, release, deletion, and re-registration. You can perform fine-grained O&M operations, such as starting or stopping instances, forcibly restarting instances, configuring instance properties, changing hostnames, reseting passwords, and logging in to out-of-band consoles. BMS minimizes user errors and simplifies O&M by enabling centralized management.

**Multi-dimensional monitoring and alerting**

BMS monitors key metrics related to CPU, memory, disk, and network resources in real time to help plan capacity. The alerts of bare metal instances and managed instances are centrally displayed. You can handle alerts based on alert levels in a closed-loop manner. BMS also associates and analyzes multi-dimensional data to quickly locate the root causes of issues and improve system stability.

**Standardized and flexible configuration**

BMS supports the standardized management of image, network, model, and GPU resources. You can manage basic configurations to improve the efficiency of cross-team collaboration, dynamically expand business, and maximize the utilization of compute resources.

**Features**

**Instance management**

The instance management feature allows you to manage and maintain the lifecycle of physical machines, covering instance registration, release, deletion, and re-registration. You can remotely start or stop instances or forcibly restart instances in BMS. This way, the status of instances can be controlled in real time. In addition, BMS provides fine-grained O&M features that allow you to modify instance properties, change hostnames, reset passwords, and log in to out-of-band consoles. It architects a sophisticated solution to bare metal instance O&M.

**Monitoring and alerting**

The monitoring and alerting feature centrally monitors registered physical machines and allows you to manage alerts. This feature consists of the following core modules: Instance monitoring Monitors the performance metrics of key resources such as CPU, memory, disk, and network, and displays resource utilization in real time to facilitate capacity planning. Bare metal instance alerts Centrally displays the alerts of bare metal instances and allows you to handle alerts based on alert levels. You can trace historical alerts and manage alerts in a closed-loop manner. Managed instance alerts Centrally displays the alerts of managed instances and allows you to handle alerts based on alert levels. You can trace historical alerts and manage alerts in a closed-loop manner. The system uses the monitoring and alerting feature to display the faults of resources of different types in a panoramic view. In combination with the alert level mechanism, the monitoring and alerting feature helps you quickly locate the root causes of issues and efficiently handle alerts. This improves the availability of bare metal instances and the efficiency of O&M.

**Basic settings**

The basic settings feature allows you to configure core parameters for bare metal instance registration and O&M. This feature supports images, networks, models, and GPUs. The basic settings feature consists of the following modules:
**Image management** Supports full lifecycle management of custom images and public
images. You can export, enable, and disable images. You can also upload and delete custom images. Based on image management, BMS enables standardized deployment of operating systems and application environments.
**Network management** Allows you to query and view subnet information, such as the
subnet name, CIDR block, and gateway.
**Model management** Allows you to flexibly configure hardware specifications, including
model creation, parameter modification, and model deletion, to meet the requirements in diverse business scenarios and optimize resource utilization.
**GPU settings** Supports fine-grained management of heterogeneous compute units. You
can add GPU models, modify parameters, and release resources. This ensures that resources can adapt to AI or high-performance computing scenarios.

## 2 Getting started

### 2.1 Work with the BMS Operations Console

**Console**

This topic describes how to use the Bare Metal Service (BMS) Operations Console. In the BMS Operations Console, you can register bare metal instances with Apsara Stack, and perform O&M and management operations on them as an administrator. These operations include powering on or off, deleting, releasing, modifying attributes of, and resetting passwords of bare metal instances. Note that the required server installation and related network connection work must be done before you use the O&M and management service of bare metal instances. You can perform the following operations on bare metal instances: Add a model: When you register a bare metal instance, you must select a model for it. You can also add a model in the BMS Operations Console and configure related parameters, such as the model name, CPU, and memory, as prompted. Register an instance: You can log in to the BMS Operations Console as an administrator, register a bare metal instance, and specify the basic settings for it. To register a bare metal instance, you need to select the management type and instance architecture, specify the image to be installed on the instance, specify the network, and enter the instance name and description. Search for an instance: You can search for all registered bare metal instances in the resource pool. The information about each instance includes both the instance details entered by the administrator and those automatically configured by the system, such as creation time, automatically assigned IP address, running status of bare metal instance, agent status, power status, and O&M status. Release an instance: You can log in to the BMS Operations Console as an administrator and release a bare metal instance with a specified instance ID. After the instance is released, it is returned to the resource pool for reinstallation. You can apply for using it again.

### 2.2 Log in to the BMS Operations Console

**Console**

This topic describes how to log in to the Apsara Uni-manager Operations Console and then access the Bare Metal Service (BMS) Operations Console. The endpoint of the Apsara Uni-manager Operations Console is obtained. To log in to the BMS Operations Console, you must first log in to the Apsara Uni-manager Operations Console. A web browser is available. We recommend that you use Google Chrome.
1. Enter the endpoint of the Apsara Uni-manager Operations Console into the address bar of
the browser.

> **Note:** You can click the current language in the upper-right corner of the login page to switch to another language. Simplified Chinese and English are supported.

2. Enter your username and password.

> **Note:** You need to obtain the username and password that are used to log in to the Apsara Uni-manager Operations Console from the deployment engineer or administrator.
> If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account.
> If you log in to the Apsara Uni-manager Operations Console for the first time, you need to change the password for your username as prompted. To enhance security, make sure that your password meets the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

3. Click **Agree to Private Policy and Log On** to log in to the Apsara Uni-manager
Operations Console.
4. In the top navigation bar, choose **Product Operation > Computing > BMS Operations**
**Console**.

## 3 Instance management

Instance management allows you to register a single instance, batch register instances, release instances, re-register instances, and query assets for management and maintenance. Administrators can perform remote O&M operations, such as remotely starting or stopping instances and forcefully restarting instances.

### 3.1 Register an instance

This section describes how to register a bare metal instance in the Bare Metal Management O&M service based on your specific O&M requirements.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, click **Register Instance** in the upper-left corner.
4. In the **Basic Information** section of the **Register Instance** panel, select the **region and**
**AZ** as prompted.
5. In the **Instance** section, configure the instance parameters.

| Configuration Item | Description |
|---|---|
| Management Type | You can select Bare Metal Management or In-Band Management. Bare Metal Management: Uses a standard image provided by the cloud platform to initialize the BMS and start the bare metal instance. In-Band Management: Does not modify the operating system on the existing device. |
| Architecture | The CPU architecture. You can select one of the following types. x86 64 _ aarch64 |
| Device Model | Select a Add a model. |
| SN | The value must be 2 to 128 characters in length and cannot start with a special character. It can contain only periods (.), underscores ( ), hyphens _ (-), and colons (:). |
| Device Model | The value must be a combination of uppercase letters, lowercase letters, and digits, and must be less than 128 characters in length. |
| Data Center | The value must be a combination of uppercase letters, lowercase letters, and digits, and must be less than 128 characters in length. |

| Room | The value must be 2 to 128 characters in length and can contain digits, uppercase letters, lowercase letters, hyphens (-), and underscores ( ). _ Example: 1-1-1. |
|---|---|
| Rack | The value must be 3 characters in length, start with an uppercase letter, and end with a positive integer from 01 to 24. Example: F02. |
| Rack Position | The value must be a positive integer from 1 to 48. |
| Maintenance Time | Select the maintenance expiration time. |

6. In the **Image** section, configure the image parameters.

| Configuration Item | Description |
|---|---|
| Image Type | You can select a Public Image or a Custom Image. |
| Public/Custom Image | Select an image. |

> **Note:** You can configure the **Image** parameter only when you set **Management Type**to **Bare Metal Management.**

7. In the **Network** section, configure the network parameters.

| Configuration item | Description |
|---|---|
| Physical gateway | Select a physical gateway. |
| Physical gateway port | Select a physical gateway port. |
| Subnet | Select a subnet. |
| Subnet IP | Enter a subnet IP address. |
| Out-of-band information | This section is hidden by default. To configure the out-of-band information, click Expand. |

| Out-of-band IP | Enter an out-of-band IP address. |
|---|---|
| Out-of-band username | The username must be 2 to 128 characters in length and start with a letter. It can contain digits and the following special characters: ~ ! @ # $ % ^ & * () - = + \| [ { } ] ; : . _ |
| Out-of-band password | The password must be 1 to 128 characters in length. |

8. In the **Configure Password** section, configure the password information.

| Configuration item | Description |
|---|---|
| Logon name | The default value is root, and you cannot change it. |
| Logon password | The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ()`~!@#$%^&* -+=\|{}[]:;'<>,.?/. _ |
| Confirm password | Enter the logon password again. |

> **Important:** Keep your password secure. If you forget the password, log on to the Bare Metal Management and Operation Console to Reset the password of an instance.

9. In the **Instance Name** section, set the **Instance Name**, **Hostname**, and **Instance**
**Description** as required.

| Configuration Item | Description |
|---|---|
| Instance Name | The name must be 2 to 128 characters in length and can contain uppercase letters, lowercase letters, digits, hyphens (-), and periods (.). It must start with a letter or a digit. |
| Hostname | Enter the hostname of the instance. |
| Instance Description | The description of the instance. The description can be 0 to 1,000 characters in length. |

0. After you complete the preceding parameter configuration, click **OK** to register the
instance.

### 3.2 Batch register instances

This topic describes how to register multiple instance at a time in the Bare Metal Service (BMS) Operations Console by uploading a file of the required format, such as an XLS file. A local file in the CSV, XLS, or XLSX format for batch instance registration is prepared based on the template. For more information about the template, see the Download a template, Template format, and Template parameters sections of this topic.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, click **Batch Register**.
4. In the **Batch Register** dialog box, configure the **Region** and **Zone** parameters.
5. In the Upload File section, upload the prepared file. Make sure that you have filled in the
template with the required instance information.
6. Click **OK**.

**Download a template**

On the Instances page, click Batch Register. In the **Batch Register** dialog box, click
**template** to download the template.

**Template format**

The following figure describes the template format. You can also download the template to view the format.

| I n s t a n c e T y p e | A r c h i t e c t u r e | M o d e l | S N | E q u i p m e n t M o d e l | I D C | R o o m | R a c k | R a c k U n i t N u m b e r | M a i n t e n a n c e T i m e | I m a g e T y p e | I m a g e | H S W | H S W P o r t | S u b n e t | S u b n e t I P / S e r v e r I P | B M C I P | B M C U s e r n a m e | B M C P a s s w o r d | U s e r n a m e | P a s s w o r d | I n s t a n c e N a m e | H o s t n a m e | I n s t a n c e D e s c r i p t i o n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

| b m s | x 8 6 _ 6 4 | F 5 2 | 6 6 6 6 6 6 6 6 | H S W | I D C | 1 - 1 - 1 | A 0 1 | 1 | 2 0 2 4 - 0 8 - 0 1 | p u b l i c | U b u n t u 1 8 . 0 4 . 0 | H S W - . A M T E S T | T e n - G i g a b i t E t h e r n e t 1 / 0 / 1 , T e n - G i g a b i t E t h e r n e t 2 / 0 / 1 | H S W . 1 0 G E - 1 | 1 0 . x . x . x | 1 0 . x . x . x | x x x x x | * * * * * * * * | x x x x x | * * * * * * * * | i n s t a n c e - b m s | h o s t - i n s t a n c e - b m s | d e s c - i n s t a n c e - b m s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

| Oper e·In | ation stan | s an ce m | d M ana | aint gem | enan ent | ce G | ui |   |   |   |   |   |   |   |   | Aps | ara | Stac | k Da | ta C | ente | r as | a s rvic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n o _ c l o n e | x 8 6 _ 6 4 | F 5 2 P 2 | 8 8 8 8 8 8 8 8 | H S W | I D C | 1 - 1 - 1 | A 0 2 | 2 | 2 0 2 4 - 0 8 - 0 1 |   |   | H S W - . A M T E S T | T e n - G i g a b i t E t h e r n e t 1 / 0 / 1 , T e n - G i g a b i t E t h e r n e t 2 / 0 / 1 | H S W . 1 0 G E - 1 | 1 0 . x . x . x |   |   |   | x x x x x | * * * * * * * * | I n s t a n c e - n o - c l o n e | h o s t - i n s t a n c e - n o - c l o n e | d e s c - i n s t a n c e - n o - c l o n e |
| 5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | > | Doc | ume | nt V | ersio | n: 2 | 026 | 082 |

**Template parameters**

| Parameter | Required | Description |
|---|---|---|
| Instance Type | Yes | The management type of the instance. Valid values: bms: bare metal management. no clone: in-band management. _ |
| Architecture | Yes | The CPU architecture. Valid values: x86 64 _ aarch64 sw 64 _ |
| Model | Yes | The model. |
| SN | Yes | The serial number of the instance. The value must be 2 to 128 characters in length and can contain periods (.), underscores ( ), _ hyphens (-), and colons (:). It cannot start with a special character. |
| Equipment Model | Yes | The equipment model. The value can be up to 128 characters in length and can contain letters and digits. |
| IDC | Yes | The data center. The value can be up to 128 characters in length and can contain letters and digits. |
| Room | Yes | The server room. The value must be 2 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ Example: 1-1-1. |
| Rack | Yes | The rack ID. The value must be three characters in length. It must start with an uppercase letter and end with an integer in |
|   |   | the range of 01 to 24. Example: F02. |
| Rack Unit Number | Yes | The rack unit number. The value must be a positive integer ranging from 1 to 48. |
| Maintenance Time | Yes | The end time of the warranty period. Format: yyyy-mm-dd. Example: 2024-08-01. |

| Image Type | No | This parameter is required if the Instance Type parameter is set to bms. The image type. Valid values: public: public image. customize: custom image. |
|---|---|---|
| Image | No | The image. This parameter is required if the Instance Type parameter is set to bms. |
| HSW | Yes | The host switch (HSW). |
| HSW Port | Yes | The HSW port. |
| Subnet | Yes | The subnet. |
| Subnet IP/Server IP | Yes | The IP address within the subnet. |
| BMC IP | No | The out-of-band IP address. |
| BMC Username | No | The out-of-band username. The value must be 2 to 128 characters in length. It must start with a letter and can contain digits and special characters. Supported special characters include ~ ! @ # $ % ^ & * () - = + \| [ { } ] ; : . _ |
| BMC Password | No | The password of the out-of-band username. The value must be 1 to 128 characters in length. |
| Username | Yes | The username. Set the value to root. |
| Password | Yes | The password. The value must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include () ' ~ ! @ # $ % ^ & * - + = \| {} [] : ; ' <> , . ? /. _ |
| Instance Name | Yes | The instance name. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), and hyphens (- ). The name must start with a letter or digit. |
| Hostname | Yes | The hostname. |
| Instance Description | No | The description of the instance. |

### 3.3 Re-register an instance

This topic describes how to re-register a bare metal instance in the Bare Metal Service (BMS) Operations Console to re-install the instance. A bare metal instance is registered. For more information, see Register an instance. The bare metal instance to be re-registered belongs to the resource pool. The bare metal instance is in a stable state, such as running, stopped, registration failed, or no heartbreak.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the instance that you want to re-register and click **Re-**
**register** in the Actions column.
4. In the **Re-register** panel, configure the parameters as required. For more information, see
Register an instance.
5. Click **OK**.

### 3.4 View instance details

This topic describes how to search for an instance and view its details. A bare metal instance is registered. For more information, see Register an instance.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, select a filter condition and enter a keyword in the search box to
search for the bare metal instance that meets the condition. The following filter conditions are supported: **Instance Name**, **Instance ID**, **SN**, **Subnet IP Address**, **VPC IP Address**, and **Out-of-band IP Address**.
4. View the details of the instance.
i. Method 1: Find the instance that you want to view and click **Manage** in the **Actions** column. ii. Method 2: Find the instance that you want to view and click its ID in the **Instance**
**ID/Name** column.
5. On the **Instance details** page, view the instance details in the **Basic Information** and
**Configuration Information** sections.
i. The information displayed in the Basic Information section includes **Instance ID**,
**Instance Name**, **SN**, **Region**, and **Zone**.
ii. The information displayed in the Configuration Information section includes **Model**, **IDC**,
**Equipment Model**, **CPU**, **OS**, **Network**, and **NIC**.

> **Note:** The information displayed in the BMS Operations console prevails.

### 3.5 Release an instance

Elastic Compute Service (ECS) bare metal instances on the tenant side must be released on the same side. If you fail to release ECS bare metal instances on the tenant side, you can use the Bare Metal Management Service (BMS) Operations Console to forcefully release them. This topic describes how to release an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be released belongs to a tenant. The ECS bare metal instance to be released is in the Release failed state.

**Background information**

Administrators can release ECS bare metal instances that belong to tenants and are in the Release failed state. After an ECS bare metal instance is released, it is added to the resource pool and reinstalled. After an ECS bare metal instance is released, you can apply for the instance again. Administrators do not have permissions to release ECS bare metal instances that are in the Normal state on the tenant side.

**Warning**

Instance releasing is a high-risk operation. Proceed with caution.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to release and
move the pointer over **Instance Status** in the Actions column.
4. Click **Release Instance** in the drop-down list.
5. In the message that appears, click **Release** to release the instance.

### 3.6 Restart an instance

This topic describes how to restart an instance. An Elastic Compute Service (ECS) bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be restarted belongs to a resource pool. The ECS bare metal instance is in a stable state. For example, the instance is running or stopped, failed creation, or does not have heartbeats.

**Background information**

Administrators can restart specific ECS bare metal instances. After an instance is restarted, its status changes to Restarting.

**Warning**

Instance restart is a high-risk operation. Proceed with caution.

**Method A:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to restart and
move the pointer over **Instance Status** in the Actions column.
4. Click **Restart Instance** in the drop-down list.
5. In the message that appears, click **OK**.
6. In the **Warning** message, click **OK** to restart the instance.

**Method B:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to restart and click
**Manage** in the Actions column.
4. On the Instance details page, click **Restart** in the upper-right corner.
5. In the message that appears, click **OK**.
6. In the **Warning** message, click **OK** to restart the instance.

### 3.7 Stop an instance

Administrators can stop Elastic Compute Service (ECS) bare metal instances. After an ECS bare metal instance is stopped, its status changes to No Heartbeat. This topic describes how to stop an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be stopped belongs to a resource pool. The ECS bare metal instance is in a stable state. For example, the instance is running, stopped, or failed or the instance does not have heartbeats.

**Warning**

This operation is a high-risk operation. Proceed with caution.

**Method A:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to stop and move
the pointer over **Instance Status** in the Actions column.
4. Click **Stop Instance** in the drop-down list.
5. In the message that appears, click **OK**.
6. In the **Warning** message, click **OK** to stop the instance.

**Method B:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to stop and click
**Manage** in the Actions column.
4. On the Instance details page, click **Stop** in the upper-right corner**.**
5. In the message that appears, click **OK**.
6. In the **Warning** message, click **OK** to stop the instance.

### 3.8 Start an instance

Administrators can start Elastic Compute Service (ECS) bare metal instances. After an ECS bare metal instance is started, its status changes to Normal. This topic describes how to start an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be started belongs to a resource pool. The ECS bare metal instance is stopped.

**Method A:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to start and move
the pointer over **Instance Status** in the Actions column.
4. Click **Start Instance** in the drop-down list.
5. In the message that appears, click **OK** to start the instance.

**Method B:**

1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to start and click
**Manage** in the Actions column.
4. On the Instance details page, click **Start** in the upper-right corner.
5. In the message that appears, click **OK** to start the instance.

### 3.9 Delete an instance

This topic describes how to delete an Elastic Compute Service (ECS) bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be deleted belongs to a resource pool. The ECS bare metal instance is in a stable state. For example, the instance is running or stopped, failed creation, or does not have heartbeats.

**Background information**

Administrators can delete ECS bare metal instances that belong to a resource pool. Only administrators can delete ECS bare metal instances that belong to a resource pool. Administrators cannot delete ECS bare metal instances on the tenant side.

**Warning**

This operation is a high-risk operation. Proceed with caution.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the ECS bare metal instance that you want to delete and
move the pointer over **Instance Status** in the Actions column.
4. Click **Delete Instance** in the drop-down list.
5. In the message that appears, confirm the instance information.
6. Click **Delete** to delete the instance.

### 3.10 Query operation logs

Administrators can view operation logs of specific bare metal instances based on O&M requirements. This section describes how to view the operation logs of a bare metal instance. You have registered the bare metal instance. For more information, see Register an instance.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Bare Metal Instances** page, select a filter condition and enter the corresponding
information in the search box to query bare metal instances that meet the condition. The supported filter conditions include: **Instance Name**, **Instance ID**, **SN**, **VPC IP Address**,
**BMC IP Address**, **Key Pair Name**, and **Tag**.
4. View the operation logs.
i. Method 1: In the Actions column of the target instance, click **Log.** ii. Method 2: Click the **Operation Status** of the instance, such as Completed or Error.

**Note**

Method 1allows you to view all operation logs of the instance. Method 2allows you to view only the operation logs of the last task of the instance.
5. In the **Operation Logs** dialog box, you can view the operation information of the bare
metal instance, such as the **Operation Type**, **Operation Status**, **Operation Time**, and
**Description Information**.
6. Click the "+" button before the **Operation Type** to expand the task details of the
operation, including the **Task Type**, **Subitem**, **Start Time**, **Execution Status**, and
**Description Information**.

**Other operations**

**Retry a task**

1. Click the **Operation Status** of the instance, such as Completed, Shutting Down, or Error.
2. In the Operation Logs dialog box, you can view the tasks that allow retries.
3. Click **Retry** after the **Task Type** or **Subitem**.
4. In the confirmation dialog box, click **OK**.

### 3.11 Modify the properties of an ECS bare metal instance

**ECS bare metal instance**

Administrators can modify the names and descriptions of Elastic Compute Service (ECS) bare metal instances. This topic describes how to modify the name and description of an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be modified belongs to a resource pool.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, click **Manage** in the Actions column of the desired instance.
4. On the Instance details page, click **More** in the upper-right corner**.**
5. Click **Modify Property** in the drop-down list.
6. In the **Modify Property** dialog box, follow the on-screen instructions to modify the name
and description of the instance.

### 3.12 Modify the hostname of an instance

**instance**

This topic describes how to modify the hostname of a bare metal instance. A bare metal instance is registered. For more information, see Register an instance. The bare metal instance to be modified belongs to the resource pool. The online status of the bare metal instance to be modified is Running. The power status of the bare metal instance to be modified is Boot.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the instance that you want to modify and click **Manage** in the
Actions column.
4. On the Instance details page, move the pointer over **More** in the upper-right corner**.**
5. Select **Modify host name** in the drop-down list.
6. In the **Modify host name** dialog box, modify the hostname of the instance.

### 3.13 Reset the password of an instance

**instance**

This topic describes how to reset the password of a bare metal instance. A bare metal instance is registered. For more information, see Register an instance. The bare metal instance whose password you want to reset belongs to the resource pool. The online status of the bare metal instance whose password you want to reset is Running. The power status of the bare metal instance whose password you want to reset is Boot.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, find the instance whose password you want to reset and click
**Manage** in the **Actions** column.
4. On the Instance details page, move the pointer over **More** in the upper-right corner**.**
5. Select **Reset Instance Password** in the drop-down list.
6. In the **Reset Instance Password** dialog box, enter a new password as prompted.
7. Click **OK**.

### 3.14 Change the gateway port of an ECS bare metal instance

**an ECS bare metal instance**

Administrators can change the gateways and gateway ports of Elastic Compute Service (ECS) bare metal instances. This topic describes how to change the gateway and gateway port of an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance to be modified belongs to a resource pool.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, click **Manage** in the Actions column of the desired instance.
4. On the Instance details page, click **More** in the upper-right corner**.**
5. Click **Modify CGW Port** in the drop-down list.
6. In the **Modify CGW Port** dialog box, change the physical gateway and physical gateway
port of the instance.
7. Click **OK** to complete the modification.

### 3.15 Log in to the out-of-band console

**console**

To fix machine faults in O&M scenarios, administrators are allowed to log in to the out-ofband consoles of Elastic Compute Service (ECS) bare metal instances to diagnose issues and locate the cause. This topic describes how to log in to the out-of-band console of an ECS bare metal instance. An ECS bare metal instance is registered. For more information, see Register an instance. The ECS bare metal instance already has an out-of-band IP address.
1. Log in to the BMS Operations Console.
2. In the left-side navigation pane, click **Instance Management > Instances**.
3. On the **Instances** page, click **Manage** in the Actions column of the desired instance.
4. On the Instance details page, click **More** in the upper-right corner**.**
5. Click **Out-of-band Console** in the drop-down list.
6. On the out-of-band console login page, enter the account information and click **Log In** to
log in to the out-of-band console.

## 4 Monitoring and alerting

The monitoring and alerting module provides administrators with capabilities to centrally monitor the resources of registered Elastic Compute Service (ECS) bare metal instances, and allows them to query and handle alerts generated by ECS bare metal instances in the resource pool. It also allows administrators to query and handle alerts generated by ECS bare metal instances on the tenant side.

### 4.1 Instance monitoring

The instance monitoring feature provides operation information about registered bare metal instances, such as CPU utilization, memory usage, disk read and write rates, and networkrelated metrics. This helps you comprehensively understand the resource usage.

#### 4.1.1 View the monitoring information about bare metal instances

**bare metal instances**

Administrators can centrally monitor the resource usage of registered bare metal instances, including CPU utilization, memory usage, disk load, network load, and number of online servers. This topic describes how to view the resource monitoring information about bare metal instances. A bare metal instance is registered. For more information, see Register an instance.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Instance Monitoring**.
3. On the **Bare Metal Instance Monitoring** page, view the basic metrics of bare metal
instances.

**Basic Data**

The basic information about the resource pool, including **Total CPU Cores**, **Total**
**Memory Size**, **Total Disk Capacity**, and **Disk Usage**.
**CPU Utilization**: the CPU utilization.
**Memory Usage**: the memory usage.
**Disk Read/Write Rate**: the disk read and write rates.
**System Load**: the system load.
**Network Bandwidth**: the network upload and download rates.
**TCP Connection Status**: the number of TCP connections.

### 4.2 Alerts of ECS bare metal instances

**instances**

Administrators can view and handle alerts generated by Elastic Compute Service (ECS) bare metal instances to identify potential issues promptly and ensure the stability of ECS bare metal instances.

#### 4.2.1 Query the alerts of ECS bare metal instances

**instances**

This section describes how to query the alerts of registered Elastic Compute Service (ECS) bare metal instances. An ECS bare metal instance is registered. For more information, see Register an instance.

**Background information**

You can query and view the alerts of registered ECS bare metal instances. The platform generates the following types of alerts: MemoryMonitor, OobMonitor, CPUMonitor, BoardMonitor, and PowerMonitor. The levels of MemoryMonitor, CPUMonitor, BoardMonitor, and PowerMonitor alerts are P2 (Major). The level of OobMonitor alerts is P3 (Minor).
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Bare Metal Instance**
**Alerts**.
3. On the **Bare Metal Instance Alerts** page, specify filter conditions and click **Search** to
search for alerts that meet the conditions. You can specify the following filter conditions: SN, Alert Type, Alert Level, Alerts, Instance IP Address, and Start and End Time.
4. After you find the ECS bare metal instance, you can view alerts related to the instance.

#### 4.2.2 View pending alerts

This topic describes how to view the pending alerts of Elastic Compute Service (ECS) bare metal instances. An ECS bare metal instance is registered. For more information, see Register an instance.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Bare Metal Instance**
**Alerts**.
3. On the **Bare Metal Instance Alerts** page, click the **Unprocessed** tab.
4. On the **Unprocessed** tab, you can view the pending alerts of all ECS bare metal instances.

#### 4.2.3 View handled alerts

This topic describes how to view the handled alerts of Elastic Compute Service (ECS) bare metal instances. An ECS bare metal instance is registered. For more information, see Register an instance.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Bare Metal Instance**
**Alerts**.
3. On the **Bare Metal Instance Alerts** page, click the **Processed** tab.
4. On the **Processed** tab, you can view the handled alerts of all ECS bare metal instances.

#### 4.2.4 Handle alerts

This section describes how to handle the alerts of registered Elastic Compute Service (ECS) bare metal instances. An ECS bare metal instance is registered. For more information, see Register an instance.

**Background information**

You can handle the alerts generated by registered ECS bare metal instances. You can ignore alerts or mark them as fixed based on the actual situation. The detection cycle of alerts is 30 minutes.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Bare Metal Instance**
**Alerts**.
3. On the **Bare Metal Instance Alerts** tab, click **Create an event ticket** in the Actions
column of the alert that you want to handle.
4. In the dialog box that appears, handle the alert based on the actual situation. For example,
if the alert is a false positive or the alert does not require any operations, select **Ignore**, specify **Handler** and **Closing Reason**, and then click **OK**.
5. If the O&M engineer has repaired the ECS bare metal instance based on the alert
information and submitted the feedback, you can select **Fixed**, specify **Handler** and
**Closing Reason**, and then click **OK**.

### 4.3 Alerts of managed instances

Administrators can view and handle alerts generated by managed instances on the tenant side. This allows administrators to identify potential issues promptly and ensures the stability and high availability of managed instances.

#### 4.3.1 Query the alerts of managed instances

This topic describes how to query the alerts of managed instances. A managed instance is created.

**Background information**

You can query and view the alerts of managed instances. The platform generates the following types of alerts: MemoryMonitor, OobMonitor, CPUMonitor, BoardMonitor, and PowerMonitor. The levels of MemoryMonitor, CPUMonitor, BoardMonitor, and PowerMonitor alerts are P2 (Major). The level of OobMonitor alerts is P3 (Minor).
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Managed Instance**
**Alerts**.
3. On the **Managed Instance Alerts** page, specify filter conditions and click Search to
search for alerts that meet the conditions. You can specify the following filter conditions: SN, Alert Type, Alert Level, Alerts, Instance IP Address, and Start and End Time.
4. After you find the managed instance, you can view alerts related to the instance.

#### 4.3.2 View pending alerts

This topic describes how to view the pending alerts of managed instances. A managed instance is created.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Managed Instance**
**Alerts**.
3. On the **Managed Instance Alerts** page, click the **Unprocessed** tab.
4. On the **Unprocessed** tab, you can view the pending alerts of all managed instances.

#### 4.3.3 View handled alerts

This topic describes how to view the handled alerts of managed instances. A managed instance is created.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Managed Instance**
**Alerts**.
3. On the **Managed Instance Alerts** page, click the **Processed** tab.
4. On the **Processed** tab, you can view the handled alerts of all managed instances.

#### 4.3.4 Handle alerts

This section describes how to handle the alerts of managed instances. A managed instance is created.

**Background information**

You can handle the alerts generated by managed instances. You can ignore alerts or mark them as fixed based on the actual situation by following the same procedure for handling the alerts of Elastic Compute Service (ECS) bare metal instances. The detection cycle of alerts is 30 minutes.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Monitoring & Alerting > Managed Instance**
**Alerts**.
3. On the **Managed Instance Alerts** tab, click **Create an event ticket** in the Actions
column of the alert that you want to handle.
4. In the dialog box that appears, handle the alert based on the actual situation. For example,
if the alert is a false positive or the alert does not require any operations, select **Ignore**, specify **Handler** and **Closing Reason**, and then click **OK**.
5. If the O&M engineer has repaired the managed instance based on the alert information and
submitted the feedback, you can select **Fixed**, specify **Handler** and **Closing Reason**, and then click **OK**.

## 5 Basic settings

The basic settings module aggregates important information required for registering and maintaining Elastic Compute Service (ECS) bare metal instances, including image metadata, network configuration, models and specifications, and GPU information. This module greatly simplifies the management of ECS bare metal instances and improves the efficiency and reliability of instance deployment.

### 5.1 Image management

The image management feature is used to maintain image metadata required for installing Elastic Compute Service (ECS) bare metal instances. It allows administrators to query custom images, manage custom image status, delete images, and export images, and query public images, manage public image status, and export public images. Administrators can upload custom images based on their business requirements.

#### 5.1.1 Upload a custom image

This topic describes how to upload a custom image. A local custom image file that meets the specifications is prepared.

**Background information**

You can upload custom image files in the tgz or qcow2 format based on your business requirements.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. Click **Upload Custom Image**.
4. In the Upload Custom Image panel, configure the parameters. The following table describes
the parameters.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The region to which the image belongs. |
| Zone | Yes | The zone to which the image belongs. |
| Image Name | Yes | The name of the image, which is automatically specified after the image file is uploaded. |

| System Architectu re | Yes | The CPU architecture. Valid values: x86 64 _ aarch64 sw 64 _ |
|---|---|---|
| Platform | Yes | The image type. |
| Kernel Version | No | The kernel version. |
| Template Name | No | The template name. |
| Image Descriptio n | No | The image description. |
| Image Upload | Yes | Click Select File to upload the image file. Supported image file formats: tgz and qcow2. Note The certificate of the environment to which you log in affects image uploading. Check whether the certificate is still valid. If the certificate has expired, the system prompts that the image failed to be uploaded. In this case, contact the administrator of the environment or perform the following operations to troubleshoot the issue: i. Click click here below the Select File button to trust the certificate. ii. On the warning page that appears, click Advanced and proceed to visit a new page. iii. Upload the image file again. |

5. Click **OK**.

#### 5.1.2 View custom image details

This topic describes how to query images and view image details. A custom image has been created. For more information, see Upload a custom image.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. On the **Custom Images** tab, select a filter condition and enter the corresponding
information in the search box. Supported filter conditions include **Image Name** and **Image**
**ID**.
4. Click the search icon to query images that meet the specified conditions.
5. The image list displays detailed image information, such as **Image Name/ID**, **System**
**Architecture**, **Platform**, **Kernel Version**, **Image Format**, and **Status**.

#### 5.1.3 Delete a custom image

This topic describes how to delete a custom image. A custom image is uploaded. For more information, see Upload a custom image.

> **Important:** When you delete an image, the source image file is also deleted. Proceed with caution.

1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. On the **Custom Image** tab, find the image that you want to delete and click Delete Image
in the **Actions** column.
4. In the message that appears, click **OK**.

#### 5.1.4 View the details of a public image

This topic describes how to view the details of a public image. Public images are available in the environment to which you are logged in.

**Background information**

Public images in the tgz or qcow2 format are supported in Apsara Stack. By default, the platform provides some adapted public images. If no image is displayed on the Public Image tab or the status of the public images on the tab is not "Available", contact the developer. A public image that has been disabled is not displayed on the bare metal instance registration page. To use this image, you must first enable it on the Images page. Some public images are only used to ensure compatibility with migrated products of earlier versions. You cannot export these images.

> **Note:** Public images cannot be deleted.

1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. Click the **Public Image** tab.
4. Select a filter condition and enter a keyword in the search box. Supported filter conditions
include **Image Name** and **Image ID**.
5. View the information about all the available public images in the columns, including **Image**
**Name/ID**, **System Architecture**, **Platform**, **Kernel Version**, **Image Format**, **Available**
**Status**, and **Enabling status**.

**Related operations**

Manage image status: Change the status of an image. Export an image: Export an image to your on-premises machine.

#### 5.1.5 Image status management

This section describes how to change the status of an image. You have public image resources or have created custom images. For more information, see Upload a custom image. The image whose status you want to change is not in use.

**Background information**

You can change the status of a specified image. After you disable an image, the system cannot reference the image during machine deployment. If the system already references the image, you cannot disable the image.

**Disable an image**

1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. You can disable both custom images and public images.
i. Disable a custom image. a. In the **Enabled Status** column of the destination image, click the status. b. In the drop-down menu that appears, click **Disable Image**. ii. Disable a public image. a. Click the **Public Image** tab. b. In the **Enabled Status** column of the destination image, click the status. c. In the drop-down menu that appears, click **Disable Image**.
4. In the status list, the enabled status of the image changes to **Disabled**.

**Enable an image**

1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. You can enable both custom images and public images.
i. Enable a custom image. a. In the **Enabled Status** column of the destination image, click the status. b. In the drop-down menu that appears, click **Enable Image**. ii. Enable a public image. a. Click the **Public Image** tab. b. In the **Enabled Status** column of the destination image, click the status. c. In the drop-down menu that appears, click **Enable Image**.
4. In the status list, the enabled status of the image changes to **Enabled**.

#### 5.1.6 Export an image

This topic describes how to export a public image or custom image to an on-premises machine. A public image is available or a custom image is uploaded. For more information, see Upload a custom image.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Images**.
By default, the **Custom Image** tab is displayed.
3. Export a custom image.
i. Find the custom image that you want to export and click **Export Image** in the Actions column.
4. Export a public image.
i. Click the Public Image tab. ii. Find the public image that you want to export and click **Export Image** in the Actions column.
5. Wait until the image is downloaded.

### 5.2 Network management

Administrators can query and view information about existing subnets and new subnets. This topic describes how to query the information about existing subnets and update subnet information.
1. Log in to the Bare Metal Management Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Network**.
3. On the **Network** page, select a filter condition, enter the keyword into the search box, and
click the Search icon to search for subnets that meet the filter condition. You can search subnets by **Subnet Name**.
4. On the **Network** page, click **Get Subnet** above the list to obtain or update the subnet
information.

### 5.3 Model management

The model management feature allows administrators to add, query, delete, and modify models. This way, administrators can flexibly manage models to meet diverse business requirements. This feature also helps ensure the accuracy and consistency of model information, which simplifies the management and deployment of Elastic Compute Service (ECS) bare metal instances.

#### 5.3.1 Add a model

After you add a model, you can search for the model and view its information. This topic describes how to add a model.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Models**.
3. On the **Models** page, click **Add Model** in the upper-left corner.
4. In the **Add Model** dialog box, configure the parameters.

| Parameter | Require d | Description |
|---|---|---|
| Model Name | Yes | The name of the model. |
| CPU Architecture | Yes | The CPU architecture. Valid values: x86 64 _ aarch64 sw 64 _ |
| CPU Manufacturer | Yes | The CPU manufacturer. The valid values of this parameter vary based on the value of the CPU Architecture parameter. If the CPU architecture is x86 64, you can select Intel or _ Hygon. If the CPU architecture is aarch64, you can select Kunpeng, Phytium, or Yitian. If the CPU architecture is sw 64, you can select SW. _ |
| CPU Model | Yes | The CPU model. |
| CPUs | Yes | The number of CPUs. |
| Memory | Yes | The memory capacity of the model. Unit: GB. |

| Disk Size | Yes | The disk capacity of the model. Unit: GB. |
|---|---|---|
| Disk Type | Yes | The type of the storage disk. |
| GPU Manufacturer | No | The GPU manufacturer. This parameter is required only when you need to configure GPUs. For more information about how to manage and view GPU information, see GPU settings. |
| GPU model | No | The GPU model. This parameter is required only when you need to configure GPUs. |
| GPUs | No | The number of GPUs. This parameter is required only when you need to configure GPUs. |
| NICs | Yes | The number of network interface controllers (NICs). |
| NIC Type | Yes | The NIC type. |
| Slots Occupied by the Machine | Yes | The number of standard rack units that the server occupies in the rack. |
| Manufacturer Name | Yes | The manufacturer name of the server. |
| Server Rated Power | Yes | The rated power consumption of the server under standard operating conditions. |
| Minimum CPU Security Frequency | No | The minimum operating frequency of the CPU in safe operating mode. |
| Description | No | The description of the model. |

5. Click **OK**.

#### 5.3.2 Modify a model

This topic describes how to modify the configurations of a model. A model is added. For more information, see Add a model. The model to be modified is not used to register bare metal instances.

**Background information**

You can modify all properties of a model except the model name. After a model is modified, you can search for the modified model and view the information about the model.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Models**.
3. On the **Models** page, find the model that you want to modify and click **Modify** in the
Actions column.
4. In the **Modify model** dialog box, modify the model parameters. For more information
about the parameters, see Add a model.
5. Click **OK**.

#### 5.3.3 View the details of a model

This topic describes how to search for a model and view the details of the model. A model is added. For more information, see Add a model.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Models**.
3. On the **Models** page, select a filter condition, enter a keyword in the search box, and then
click the search icon to search for models that meet the filter condition. Supported filter conditions include **Model Name**, **Disk Type**, and **Manufacturer**.
4. View the model details in the columns, including **Model Name**, **Architecture**, **CPUs**, **CPU**
**Manufacturer**, and **CPU Model**.

#### 5.3.4 Delete a model

This topic describes how to delete a model. A model is added. For more information, see Add a model. The model to be deleted is not referenced by any Elastic Compute Service (ECS) bare metal instances.

**Warning**

This operation is a high-risk operation and is irreversible. Proceed with caution.

**Note**

Administrators can delete models with the specified names. If physical machines of a model are registered, the model cannot be deleted.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > Models**.
3. On the **Models** page, find the model that you want to delete and click **Delete** in the
Actions column.
4. In the message that appears, click **OK** to delete the model.

### 5.4 GPU settings

The GPU settings feature allows administrators to add, query, modify, and delete GPUs. Administrators can use this feature to add GPU settings, efficiently search GPU settings, update existing GPU settings, and delete GPU settings in certain scenarios.

#### 5.4.1 Add a GPU

This topic describes how to add a GPU.

**Background information**

After you add a GPU, you can search for the GPU and view its information.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > GPU Settings**.
3. On the **GPU Settings** page, click **Add GPU** in the upper-left corner.
4. In the **Add GPU** dialog box, configure the parameters. The following table describes the
parameters.

| Parameter | Required | Description |
|---|---|---|
| GPU Manufacturer | Yes | The GPU manufacturer. |
| GPU Manufacturer (Chinese) | No | The Chinese name of the GPU manufacturer. |
| GPU Model | Yes | The GPU model. |
| GPU Model (Chinese) | No | The Chinese name of the GPU model. |
| GPU Memory Size | Yes | The memory size of the GPU. |
| TFLOPS | Yes | The tera floating-point operations per second (TFLOPS). |

5. Click **OK**.

#### 5.4.2 Modify a GPU

This topic describes how to modify the configurations of a GPU. A GPU is added. For more information, see Add a GPU.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > GPU Settings**.
3. On the **GPU Settings** page, find the GPU that you want to modify and click **Edit** in the
Actions column.
4. In the **Edit GPU** dialog box, modify the GPU parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| GPU Manufacturer | The GPU manufacturer. This parameter cannot be modified. |
| GPU Manufacturer (Chinese) | The Chinese name of the GPU manufacturer. |
| GPU Model | The GPU model. This parameter cannot be modified. |
| GPU Model (Chinese) | The Chinese name of the GPU model. |
| GPU Memory Size | The memory size of the GPU. |
| TFLOPS | The tera floating-point operations per second (TFLOPS). |

5. Click **OK**.

#### 5.4.3 Query GPUs

Administrators can query and view information about GPUs. This topic describes how to query GPUs. A GPU is added. For more information, see Add a GPU.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > GPU Settings**.
3. On the **GPU Settings** page, enter a GPU model into the search box to find the GPU that
meets the condition.

#### 5.4.4 Delete a GPU

Administrators can delete the specified GPUs. This topic describes how to delete a GPU. A GPU is created. For more information, see Add a GPU.

**Warning**

This operation is irreversible. Proceed with caution.
1. Log in to the Bare Metal Service (BMS) Operations Console.
2. In the left-side navigation pane, choose **Basic Settings > GPU Settings**.
3. On the **GPU Settings** page, find the GPU that you want to delete and click **Delete** in the
Actions column.
4. In the message that appears, click **OK** to delete the GPU.
