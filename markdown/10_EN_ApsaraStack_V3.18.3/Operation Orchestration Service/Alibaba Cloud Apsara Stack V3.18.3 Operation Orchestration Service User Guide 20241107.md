---
title: "Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service User Guide 20241107"
product_version: "V3.18.3"
doc_version: "20241107"
pdf_pages: 13
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service User Guide 20241107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E8%BF%90%E7%BB%B4%E7%BC%96%E6%8E%92OSS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Operation%20Orchestration%20Service%20User%20Guide%2020241107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service User Guide 20241107

## Table of Contents

- 1 Public templates
- 2 Custom templates
  - 2.1 Template syntax
    - 2.1.1 Template structure
    - 2.1.2 Overview
    - 2.1.3 Output
- 3 Manage task executions

## 1 Public templates

CloudOps Orchestration Service (OOS) provides a variety of templates that are suitable for different scenarios. The following table describes the templates and scenarios supported by OOS.

| Template category | Template name | Description |
|---|---|---|
| Instance management | ACS-ECS-ModifyInstanceSpec | Modifies the instance type of a pay-as-you-go Elastic Compute Service (ECS) instance. |
|   | ACS-ECS-BulkyStopInstances | Stops multiple ECS instances at a time. |
|   | ACS-ECS-BulkyResizeDisk | Increases the space of multiple disks at a time. |
|   | ACS-ECS-BulkyRebootInstances | Restarts multiple ECS instances at a time. |
|   | ACS-ECS-BulkyDeleteInstances | Deletes multiple pay-as-you-go ECS instances at a time. |
|   | ACS-ECS-BulkyStartInstances | Starts multiple ECS instances at a time. |
| Command running | ACS-ECS-BulkyRunCommand | Runs commands on multiple ECS instances at a time. |
| Image management | ACS-ECS-DeleteImage | Deletes an ECS image. |
|   | ACS-ECS-CreateImage | Creates an ECS image. |
| Data backup | ACS-ECS-BulkyCreateSnapshot | Creates multiple snapshots at a time. |
| Security audit | ACS-RDS- ReleaseInstancePublicConnection | Releases the public IP address of an ApsaraDB RDS instance. |
|   | ACS-RDS-BulkyModifySQLCollectorPolicy | Enables the SQL Explorer and Audit feature for an ApsaraDB RDS instance. |
| > Document Version: 2 | 0241107 |   |

| User Guide·Public temp |   |   |
|---|---|---|
|   | ACS-RDS- BulkyModifySecurityIpsByInstanceIPArray | Removes 0.0.0.0/0 from the IP address whitelist of an ApsaraDB RDS instance. |
| Scheduled operation | ACS-ECS-ScheduleToStopInstances | Stops an ECS instance at the specified point in time. |
|   | ACS-ECS-ScheduleToRebootInstances | Restarts an ECS instance at the specified point in time. |
|   | ACS-ECS- ScheduleToStartAndStopInstances | Starts and then stops an ECS instance at the specified points in time. |
|   | ACS-ECS-ScheduleToStartInstances | Starts an ECS instance at the specified point in time. |
|   | ACS-ECS- ScheduleToStopAndStartInstances | Stops and then starts an ECS instance at the specified points in time. |
|   | ACS-ECS-ScheduleToExecuteTemplate | Executes a template at the specified point in time. |
| Auto scaling management | ACS-ESS- CreateImageAndUpdateScalingConfigurati on | Creates an ECS image and updates the image ID in the scaling configurations. |
|   | ACS-ESS- UpdateScalingConfigurationImage | Runs commands to update an existing ECS image, creates an ECS image, and then updates the image ID in the scaling configurations. |
| Cross-region replication | ACS-ECS-BulkyCloneInstances | Clones multiple ECS instances at a time. |
| Other | ACS-ECS-UpdateImage | Updates an image |

After you find the template that you want to use on the Public Template page, you can click
**Create Execution** to execute the template. For more information, see the **Manage task**
**executions** topic.

## 2 Custom templates

### 2.1 Template syntax

#### 2.1.1 Template structure

The content of a template is a piece of UTF-8 text in the JSON or YAML format. The template defines the version, parameters, tasks, sequence, inputs, and outputs. You can use the template to define the required O&M operations.

**Syntax**

YAML format

```
--- FormatVersion: OOS-2019-06-01 # Required. The version of the template. Example: OOS-201 9-06-01. Description: "" # Optional. The description of the template, such as the features or us age of the template. Parameters: # Optional. The parameters to be set for executing the template. For more i nformation, see the relevant documentation. RamRole: # Optional. The role that Operation Orchestration Service (OOS) assumes to cal l the API operations of each cloud product. Default value: OOSServiceRole. Tasks: # Required. The tasks to be executed. As the most important component of a templ ate, the Tasks parameter defines the details of O&M operations. Each task in the templa te corresponds to an action. By default, multiple tasks are executed one by one. If a t ask is a loop task, concurrent child execution may occur within the task. For more info rmation, see the relevant documentation. Outputs: # Optional. The template outputs, such as resource attributes. You can obtain the outputs through the API or the OOS console. For more information, see the relevant documentation.
```

JSON format (For more information, see the parameter description for the YAML format.) `{`

```json
  "FormatVersion": "OOS-2019-06-01",
  "Description": "",
  "Parameters": {},
  "RamRole": "",
  "Tasks": [],
  "Outputs": {}
```

`}`

#### 2.1.2 Overview

When creating and executing a template, you can use parameters to improve the flexibility and reusability of the template.

**Definition**

You can define a parameter in the Parameters field of the template, including the parameter name, description, type, default value, and verification rules.

**Syntax**

YAML format

```
Parameters:
  Parameter-name-1: # The name of the parameter. The name can contain lowercase letters
, uppercase letters, digits, underscores (_), and hyphens (-). Spaces are not allowed. We recommend that you use the lower camel case for a name. Example: instanceId.
    Type: String # Optional. The type of the parameter. Valid values: List, Number, Str
ing, Boolean, and Json. Default value: String.
    Description: description # Optional. The description of the parameter, such as the
features of the parameter.
    Default: default-value # Optional. The default value of the parameter.
    AllowedValues: # Optional. The list of the valid values for the parameter.
      - value1
      - value2
    AllowedPattern: regular-expression # Optional. The regular expression that must be
matched with the parameter value. This attribute is valid only when the parameter value is a string.
    MinLength: 1 # Optional. The minimum length of the parameter value. This attribute
is valid only when the parameter value is a string.
    MaxLength: 10 # Optional. The maximum length of the parameter value. This attribute
is valid only when the parameter value is a string.
```

JSON format (For more information, see the parameter description for the YAML format.) `{`

```json
  "Parameters": {
    "parameter-name-1": {
      "Type": "String",
      "Description": "description",
      "Default": "default-value",
      "AllowedValues": [
        "value1",
        "value2"
```

`],`

```json
      "AllowedPattern": "regular-expression",
      "MinLength": 1,
      "MaxLength": 10
```

`}` `}` `}`

**Reference**

You can reference the parameters defined above as attributes in the Tasks field. The following is the syntax for referencing parameters:

```
"some text {{ parameter_name }} some text {{parameter_name_2}} ..."
```

For example: When the YAML format is used, referenced parameters must be enclosed in the double quotation marks ("").

```
"{parameter-name}" # Reference a parameter itself. "this is the {parameter-name}" # Reference a parameter in a fixed string. "hello {{ parameter-last-name }} {{ parameter-first-name }}" # Reference multiple param eters in a fixed string.
```

**Pseudo parameters**

OOS provides pseudo parameters for obtaining the execution information. You can reference these parameters without the need to define them. The following table describes the supported pseudo parameters. If you need more pseudo parameters, submit a ticket and describe your scenarios. We will give you feedback and support as soon as possible.

| Name | Type | Description | Example |
|---|---|---|---|
| ACS::TemplateName | String | The name of the template that is executed. | ACS-ECS- StartInstances br or MyTemplate1 |
| ACS::ExecutionId | String | The ID of the execution. | exec- 21234455677892ac |
| ACS::Region | String | The region where the template is executed. | cn-hangzhou |
| ACS::AccountId | String | The account that is used to execute the template. | 12345678901234 |

#### 2.1.3 Output

You can configure the output parameters for a template. The output parameters can define the results you need after the O&M operations are completed. For example, you can set the output parameters to obtain the ID of an Elastic Compute Service (ECS) instance after the O&M operation for creating the ECS instance is completed.

**Syntax**

YAML format

```
Outputs:
  OutputParameterName1:# Required.The name of the output parameter. The name can contai
n lowercase letters, uppercase letters, digits, underscores (_), and hyphens (-). It ca n be up to 200 characters in length.
    Type: String # Optional. The type of the output parameter. The valid values include
the basic parameter types supported by the YAML or JSON format, such as String, Number, Boolean, List or Array, and Object. Default value: String.
    Value: "{taskName. OutputParameter1}" # Required. The value of the output parameter
. The value is usually the output of a task.
```

JSON format (For more information, see the parameter description for the YAML format.) `{`

```json
  "Outputs": {
    "OutputParameterName1": {
      "Type": "String",
      "Value": "{{ taskName.OutputParameter1 }}"
```

`}` `}` `}` ons

## 3 Manage task executions

**Procedure**

Log on to the CloudOps Orchestration Service (OOS) console. In the left-side navigation pane, click **Task Execution Management**. On the page that appears, perform the following operations based on your business requirements.

**Create an execution**

1. Click **Create**.
2. Configure the parameters in the Basic Information step, and then click Next Step:
Parameter Settings. image The following table describes the parameters.

| Parameter | Description |
|---|---|
| Execution Description | Enter a description for the execution that you want to create. |
| Template Category | Select the type of the template that you want to use. Valid values: Public Template Custom Template |
| Template | After you select a template type, select the template that you want to use from the Template drop-down list. |
| Select Version | Select a template version. This parameter is displayed only if you select Custom Template as Template Category. |
| Template Description | The description of the selected template. |
| Organization | Select an organization. Organizations are the highest-level management units in Apsara Stack. Organizations are used to logically isolate cloud resources, users, and permissions. This ensures that the data and resources of each organization can be independently and securely accessed. |
| Resource Set | Select a resource set. Resource sets are resource management units within an organization. You can group cloud resources with similar characteristics into a resource set. |

ons

| Execution Mode | Select an execution mode. Valid values: Automatic Suspend upon Failure Manual |
|---|---|

3. Configure the parameters in the Parameter Settings step. The required parameters vary
based on the template. In this example, the ACS-ECS-ModifyInstanceSpec template is selected. This template is used to change the instance type of an Elastic Compute Service (ECS) instance. i. In the Parameter Configure section, specify the instance types before and after the change in the specified format. ii. In the Select Ecs Instances section, select a region ID and the ECS instance whose instance type you want to change. iii. In the Control Options section, configure the Resource Access Management (RAM) role of OOS.
4. Click **Next Step: OK**.
5. In the OK step, click **Create**.

**View the details of an execution**

Find the execution whose details you want to view and click **Details** in the **Actions** column.

**Clone an execution**

1. Find the execution that you want to clone and click **Clone** in the **Actions** column.
2. Configure the parameters in the Basic Information and Parameter Settings steps. For more
information, see the Create an execution section of this topic.
3. Click **Next Step: OK**.
4. In the OK step, click **Create**.

**Delete an execution**

1. Find the execution that you want to delete. Click the More icon and select **Delete** in the
**Actions** column.
2. In the **delete execution** message, click **OK**.

**View child executions**

1. Find the execution whose child executions you want to view and click **Child Execution** in
the **Actions** column. A child execution is generated only when you execute an embedded template in the template. ons
