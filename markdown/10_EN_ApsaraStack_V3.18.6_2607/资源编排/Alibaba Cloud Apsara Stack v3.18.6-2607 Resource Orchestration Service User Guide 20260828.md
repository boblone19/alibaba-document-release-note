---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 457
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B5%84%E6%BA%90%E7%BC%96%E6%8E%92/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Resource%20Orchestration%20Service%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service User Guide 20260828

## What is ROS?

Resource Orchestration Service (ROS) is a service provided by Apsara Stack to simplify the management of cloud computing resources. You can author a stack template based on the template specifications defined in ROS. In the template, you can define required cloud computing resources, such as Elastic Compute Service (ECS) and ApsaraDB RDS instances, and the dependencies between resources. The ROS engine automatically creates and configures all resources in a stack based on the template. This helps achieve automatic deployment and O&M. An ROS template is a readable, easy-to-author text file. You can directly edit a JSON template or use version control tools, such as Apache Subversion (SVN) and Git, to manage the template and infrastructure versions. You can call APIs and use SDKs to integrate the orchestration capabilities of ROS with your applications to implement Infrastructure as Code (IaC). An ROS template is a standardized method to deliver resources and applications. If you are an independent software vendor (ISV), you can use ROS templates to deliver a holistic system or solution that encompasses cloud resources and applications. This way, Apsara Stack resources can be integrated with your software systems for centralized delivery. ROS manages a collection of cloud resources in a centralized manner by using a single unit named a stack. A stack is a collection of Apsara Stack resources. You can create, delete, and recreate cloud resources by stack. sole

## Log in to the ROS console

This topic describes how to log in to the Resource Orchestration Service (ROS) console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the service domain name for the Apsara Uni-manager
Management Console and press Enter.

**Note**

You can click the current language in the upper-right corner to switch to another language.
2. Enter your username and password.
sole

**Note**

You can obtain the username and logon password from an operations administrator. If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.
3. Select **I Have Read And Agree To The Product Service Agreement, Privacy Agreement, And**
**User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement. The **Product Service Agreement**, **Privacy Agreement**, and **User Agreement** are displayed only if they have been published. If none of these agreements are published, you can skip this step.
4. Click **Account Logon** or **Authorized Logon**.

**Note**

The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".
5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of the following
scenarios:

**Note**

When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.
6. In the top navigation bar, choose **Products > Development Tools > Resource Orchestration**
**Service (ROS)**.

## Manage stacks

### Create a stack

Resource Orchestration Service (ROS) allows you to use a stack to manage a group of resources. This topic describes two methods to create a stack.

**Method 1 (recommended): Create a stack on the Stacks page**

1. Log on to the ROS console.
2. In the left-side navigation pane, click **Stack**.
3. On the **Stack** page, click **Create Stack**.
4. On the **Select Template** page, select the **Organization**, **Resource Set**, and **Region**.
5. Select a template import method, configure the template, and then click **Next**.
**Enter Template Content**: Enter a template in JSON format in the **Prepare Template** section.
**My Templates**: Select an existing template. For more information about how to create a template, see
Create a template.
6. On the **Configure Template Parameters** page, enter the stack name and parameters, and then click
**Next**.

**Note**

The required parameters vary based on the template. Follow the on-screen instructions in the console to configure the parameters. You can also click **Preview** to view the resource name, resource type, and resource properties.
7. On the **Configure Stack** page, specify whether to enable rollback on failure, set the timeout period, and
then click **Next**.
8. On the **Confirm Information** page, verify the stack information and click **Submit**.
After the stack is created, **Created** appears in the **Status** column of the stack. You can then click the stack ID to view the basic information (such as the stack name, ID, and creation time), events, resources, outputs, parameters, and template of the stack.

**Method 2: Quickly create a stack from an existing template**

If you have already created a template, you can quickly create a stack by using the following method. For more information about how to create a template, see Create a template.
1. Log on to the ROS console.
2. In the left-side navigation pane, click **My Templates**.
3. On the **My Templates** page, find the template that you want to use and click **Create Stack** in the
**Operation** column.
4. On the **Select Template** page, select the **Organization**, **Resource Set**, and **Region**, and then click
**Next**.
5. On the **Configure Template Parameters** page, enter the stack name and parameters, and then click
**Next**.
6. On the **Configure Stack** page, specify whether to enable rollback on failure, set the timeout period, and
then click **Next**.
7. On the **Confirm Information** page, verify the stack information and click **Submit**.
After the stack is created, **Created** appears in the **Status** column of the stack. You can then click the stack ID to view the basic information (such as the stack name, ID, and creation time), events, resources, outputs, parameters, and template of the stack.

### View a stack

This topic describes how to view the details of a stack in the Resource Orchestration Service (ROS) console. The details include the basic information, events, and resources.

**Prerequisites**

A stack is in the Created state. For more information, see Create a stack.

**Procedure**

1. Log on to the ROS console.
2. In the left-side navigation pane, click **Stacks**.
3. On the **Stacks** page, click the ID of the desired stack.
You can filter a desired stack by **stack name**, **stack ID**, and **tag**. On the stack details page, you can perform the following operations: Click the **Stack Information** tab to view the basic information and template content of the stack. Click the **Events** tab to view each event that occurs during the stack lifecycle. Click the **Resources** tab to view information about each resource contained in the stack. Click the **Outputs** tab to view information about the outputs specified in the template when you created the stack. Click the **Parameters** tab to view the parameters specified in the template when you created the stack, including the pseudo parameters that are provided by ROS and whose names contain the ALIYUN:: prefix. Click the **Operation Logs** tab to view the access and usage information about the stack. This helps you analyze and trace previous operations. You can find the desired operation record by using filters, including the **Operation Name**, **Operator**, and **Execution status** filters. The following table describes the supported filters.

| Filter | Description |
|---|---|
| Operator | Enter the operator. |
| Operation Name | Enter the name of the API operation that corresponds to the change operation on the stack. |
| Execution status | Select Success or Failed. |
| Operation Source IP | Enter the source IP address of the operation. |
| Operation Time | Specify the time range that you want to query. |

**(Optional)** Find the operation record and click **Operation Details** in the **Operation** column to view
data in the **Basic Information** and **API call details** sections.

### Update a stack

You can update a stack if you want to modify only the template that is used to create the stack or the stack configurations. The update operation does not change the organization, resource set, or region of your stack. This topic describes how to update a stack.

**Prerequisites**

A stack is in the **Created** state. For more information, see Create a stack.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **Stacks**.
3. On the **Stacks** page, find the stack that you want to update and click **Update** in the **Actions** column.
4. In the **Select Template** step, select a value for Specify Template Import Method. Then, click **Next**.
**Enter Template Content**: Enter the content of a JSON template in the **Prepare Template** section.
**My Templates**: Select an existing template.
5. In the **Configure Template Parameters** step, modify the parameter settings in the Set Parameter
section. Then, click **Next**.

**Note**

The parameters that you must configure vary based on the template. Follow on-screen instructions to configure the parameters.
6. In the **Configure Stack** step, set the timeout period and click **Next**.
7. In the **Confirm** step, confirm the template and stack configurations, and click **Update Stack**.

### Recreate a stack

You can recreate a stack if you want to change your template, stack configurations, and the organization, resource set, and region of the stack. This topic describes how to recreate a stack.

**Prerequisites**

A stack is in the **Created** state. For more information, see Create a stack.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **Stacks**.
3. On the **Stacks** page, find the stack that you want to recreate and click **Re-create** in the **Actions** column.
4. In the **Select Template** step, configure **Organization**, **Resource Set**, and **Region**.
5. Select a value for Specify Template Import Method. Enter the content of your template in the Prepare
Template section. Then, click **Next**.
**Enter Template Content**: Enter the content of a JSON template in the **Prepare Template** section.
**My Templates**: Select an existing template.
6. In the **Configure Template Parameters** step, modify the parameter settings in the Stacks and Set
Parameters sections. Then, click **Next**.

**Note**

The parameters that you must configure vary based on the template. Follow on-screen instructions to configure the parameters. The name must be unique in your Apsara Stack tenant account.
7. In the **Configure Stack** step, configure Rollback on Failure and Timeout Period based on your business
requirements, and click **Next**.
8. In the **Confirm** step, confirm the template and stack configurations, and click **Create Stack**.

### Delete a stack

You cannot delete a stack that is in the process of an operation such as create or update.

**Prerequisites**

A stack is created. For more information, see Create a stack.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **Stack**.
3. Deletes one or more stacks.
i. Delete a single stack: Find the stack that you want to delete and click **Delete** in the **Operation** column. ii. Delete multiple stacks at a time: Select the stacks that you want to delete and click **Batch Delete** in the lower part of the stack list.
4. In the dialog box that appears, confirm the stacks that you want to delete and select a **Deletion Method**.
**Retain Resources**: retains the resources in a stack when the stack is deleted.
**Release Resources**: releases the resources in a stack when the stack is deleted. Proceed with caution.
5. Click **Delete**.

## Manage templates

### Create a template

Resource Orchestration Service (ROS) allows you to use a JSON-formatted template to create a stack. This topic describes how to create a template.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **My Templates**.
3. On the **My Templates** page, click **Create Template**.
4. In the **Create Template** dialog box, configure the **Template Name**, **Template Description**,
**Organization**, **Resource Set**, and **Prepare Template** parameters.

| Parameter | Description |
|---|---|
| Template Name | The name must be 2 to 255 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). It must start with a letter. _ |
| Organization | Select the organization to which the template belongs. |
| Resource Set | Select the resource set to which the template belongs. |
| Sharing Scope | Select the sharing scope of the template. |
| Template Description | The description can be up to 256 characters in length. |
| Prepare Template | The template content is a JSON-formatted text file that uses UTF-8 encoding. Templates are used to create stacks and serve as the blueprint for underlying infrastructure and architectures. You can define resources and configurations and describe dependency relationships between the resources in a template. For more information about how to write a template, see Template structure. |

5. Click **OK**.

### Modify a template

You can modify the name, description, and content of a template based on your business requirements in the Resource Orchestration Service (ROS) console.

**Prerequisites**

A template is created. For more information, see Create a template.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **My Templates**.
3. Select a filter condition from the drop-down list and enter relevant information in the search box to search
for templates. The templates that meet the specified filter condition are displayed.

**Note**

You can search for a template by **Name or ID** or **Tag**. You can also click Advanced Filter and specify multiple filter conditions to narrow down the search results.
4. On the **My Templates** page, find the template that you want to modify and click **Edit** in the **Actions**
column.
5. In the **Edit Template** dialog box, modify the **Template Name**, **Template Description**, and **Prepare**
**Template** parameters as required.
6. Click **Confirm**.

### Configure sharing settings

You can share an existing template with the current resource set, current organization, or subordinate organizations based on your business requirements.

**Prerequisites**

A template is created. For more information, see Create a template.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **My Templates**.
3. On the **My Templates** page, find the template that you want to manage and click **Sharing Settings** in
the **Actions** column.
4. In the **Edit Sharing Settings** dialog box, select **Current Organization and Subordinate**
**Organizations**, **Current Resource Set**, or **Current Organization** from the **Sharing Scope** drop-down
list based on your business requirements.
5. Click Confirm.

### Delete a template

You can delete templates that you no longer need.

**Prerequisites**

A template is created. For more information, see Create a template.

**Procedure**

1. Log in to the ROS console.
2. In the left-side navigation pane, click **My Templates**.
3. On the **My Templates** page, find the template that you want to delete and click **Delete** in the **Actions**
column.
4. In the dialog box that appears, confirm the template that you want to delete and click **Delete**.

## View operation logs

This topic describes how to view operation logs to track user access and behavior, which facilitates analysis and review of historical operations.

**Procedure**

1. Log on to the Resource Orchestration Service console.
2. In the left navigation bar, click **Operation Logs**.
3. On the **Operation Logs** page, you can view the operation records of all operators within the specified
time range. You can use **Advanced Filter** to further filter the operation records by filter conditions such as **Resource**
**Type**, **IP Address**, and time range.
4. Select the record you want to view, and click **View** in the **Details** column on the right to view **General**
**Information** and **Instance Details**.

## Template syntax

### Template structure

A template is a UTF-8 encoded JSON file that is used to create stacks. Templates serve as the blueprint for underlying infrastructure and architecture. Templates define the configurations of Apsara Stack resources and dependencies between the resources.

**ROS template structure**

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Description" : "The description of the template, which is used to provide information such as use
scenarios and architecture of the template",
  "Metadata" : {
    // The template metadata that provides information such as the layout for visualizations.
```

`},`

```json
  "Parameters" : {
    // The parameters that you can specify when you create a stack.
```

`},`

```json
  "Mappings" : {
    // The mapping tables. Mapping tables are nested tables.
```

`},`

```json
  "Conditions": {
    // The conditions defined by using internal condition functions. These conditions determine when
to create associated resources.
```

`},`

```json
  "Resources" : {
    // The detailed information of resources such as configurations and dependencies.
```

`},`

```json
  "Outputs" : {
    // The outputs that are used to provide information such as resource properties. You can use the
Resource Orchestration Service (ROS) console or API to obtain the information.
```

**ROSTemplateFormatVersion**

Required. The template versions supported by ROS. Current version: 2015-09-01.

**Description**

Optional. The description of the template, which is used to provide information such as use scenarios and architecture of the template. A detailed description can help users better understand the content of the template.

**Metadata**

Optional. The metadata of the template, in the JSON format.

**Parameters**

Optional. The parameters that you can specify when you create a stack. An Elastic Compute Service (ECS) instance type is often defined as a parameter. Parameters have default values. Parameters can improve the flexibility and reusability of the template. When you create a stack, select appropriate specifications.

**Mappings**

Optional. Mappings are defined as nested mapping tables. You can use Fn::FindInMap to retrieve values corresponding to keys. You can also use parameter values as keys. For example, you can search the regionimage mapping table for desired images by region.

**Conditions**

Optional. The conditions defined by using Fn::And, Fn::Or, Fn::Not, and Fn::Equals. Multiple conditions are separated by commas (,). The system evaluates all conditions in the template before it creates or updates a stack. All resources associated with `true` conditions are created, and all resources associated with `false` conditions are ignored.

**Resources**

Optional. The detailed information of resources in the stack created based on the template. The information includes resource dependencies and configurations.

**Outputs**

Optional. The outputs that are used to provide information such as resource properties. You can use the ROS console or API to obtain the information.

### Overview

When you create a template, you can use parameters to improve its flexibility and reusability. When you use the template to create a stack, you can replace specific parameter values as needed.

**Syntax**

Each parameter consists of a parameter name and properties. The parameter name must contain only letters and digits, and must be unique within the same template. You can use the **Label** field to define a parameter alias. The following table describes the parameter properties.

| Property | Required | Description |
|---|---|---|
| Type | Yes | The data type of the parameter. Valid values: String : a string. Example: "ecs.s1.medium" . Number : an integer or a floating-point number. Example: 3.14. CommaDelimitedList : a set of strings separated by commas (,), which can be indexed by using the Fn::Select function. Example: "80, foo, bar" . Json : a string in JSON format. Examples: {"foo": "bar"} and [1, 2, 3] . Boolean : a Boolean value. Examples: true and false . ALIYUN::OOS::Parameter::Value : a common parameter stored in Operation Orchestration Service (OOS) Parameter Store. Example: my image . _ ALIYUN::OOS::SecretParameter::Value : an encrypted parameter stored in Operation Orchestration Service (OOS) Parameter Store. Example: my password . _ Note ALIYUN::OOS::Parameter::Value and ALIYUN::OOS::SecretParameter::Value do not support AllowedPattern validation. |

| "80, foo, bar" |   |
|---|---|
| Json |   |

| Default | No | The default value of a parameter. When you create a stack, if you do not specify a value for a parameter, Resource Orchestration Service (ROS) checks whether a default value is defined for the parameter in the template. If a default value is defined, ROS uses it. Otherwise, ROS returns an error. Note You can set the default value to null , which indicates that the parameter value is empty and ROS skips verification for this parameter. |
|---|---|---|
| AllowedValues | No | The list of allowed values for the parameter. |
| AllowedPattern | No | A regular expression that validates whether a user-provided string parameter matches the allowed pattern. If the user provides a non- string value, ROS returns an error. If you use the following special characters, you must escape each character by preceding it with two backslashes (\\): *.?+-$^[ ]( ){ }\|\/ Note You do not need to add escape characters before hyphens (-) that are placed at the start and end of a regular expression. Example: [a-z-]. |
| MaxLength | No | An integer that specifies the maximum number of characters allowed for a String-type parameter. |
| MinLength | No | An integer that specifies the minimum number of characters allowed for a String-type parameter. |
| MaxValue | No | A numeric value that specifies the maximum value allowed for a Number-type parameter. |
| MinValue | No | A numeric value that specifies the minimum value allowed for a Number-type parameter. |
| NoEcho | No | Specifies whether to mask the return value of a parameter when the GetStack operation is called. If you set this property to true , ROS returns the parameter value masked as asterisks (*). |
| Description | No | A string that describes the parameter. |
| ConstraintDescrip tion | No | A string that explains a constraint when the constraint is violated. |
| Label | No | The parameter alias, which supports UTF-8 characters. When you create a web form based on a template, label can be mapped to the parameter name. |

| AssociationProper ty | No | This property is used to automatically verify the validity of values of a parameter and provide a set of valid values for the parameter. |
|---|---|---|
| AssociationProper tyMetadata | No | A metadata map that specifies the constraint of AssociationProperty to filter results that meet the conditions. This property is of the Map type. |
| Confirm | No | Specifies whether the parameter requires a second input for confirmation when NoEcho is set to true . Default value: false . Note You can set Confirm to true only when it is used with a String-type parameter and NoEcho is set to true . |
| TextArea | No | Specifies whether the parameter supports line breaks. Valid values: true false (default) For example, the following code indicates that the Content parameter supports line breaks. ROSTemplateFormatVersion: '2015-09-01' Parameters: Content: Type: String TextArea: true Outputs: TestContent: Value: Ref: Content |

**Example: Create a stack for a web application**

For example, you want to create a stack for a web application. The stack contains one Server Load Balancer (SLB) instance, two Elastic Compute Service (ECS) instances, and one ApsaraDB RDS instance. If the web application is under a heavy workload, you can select an ECS instance that has advanced specifications when you create the stack. Otherwise, you can select an ECS instance that has basic specifications. The following sample code shows how to define properties for the InstanceType parameter in a template:

```
Parameters:
  InstanceType:
    Type: String
    AllowedValues:
      - ecs.t1.small
      - ecs.s1.medium
      - ecs.m1.medium
      - ecs.c1.large
    Default: ecs.t1.small
    Label: ECS instance type
    Description: Select the configuration for the ECS instance. The default value is ecs.t1.small. Va
lid values: ecs.t1.small, ecs.s1.medium, ecs.m1.medium, and ecs.c1.large.
```

In this example, you can reassign a value to **InstanceType** when you use the template to create a stack. If you do not specify a value for the parameter, the system uses the default value: `ecs.t1.small` . You can reference this parameter when you define resources:

```
Webserver:
  Type: ALIYUN::ECS::Instance
  InstanceType:
    Ref: InstanceType
```

### Resources

This topic describes the properties of each resource and dependencies between resources in a stack. A resource can be referenced by other resources and output items.

**Syntax**

Each resource consists of an ID and a description. All resource descriptions are enclosed in braces {}. Multiple resources are separated by commas (,). The following sample code shows the Resources syntax:

```json
"Resources" : {
    "Resource1 ID" : {
        "Type" : "The resource type",
        "Condition": "The condition that specifies whether to create the resource",
        "Properties" : {
            The description of the resource properties
```

`},`

```json
    "Resource2 ID" : {
        "Type" : "The resource type",
        "Condition": "The condition that specifies whether to create the resource",
        "Properties" : {
            The description of the resource properties
```

Parameter description: The resource ID must be unique within the template. You can use the resource ID to reference the resource in other parts of the template. The Type parameter specifies the type of the resource that is being declared. For example, ALIYUN::ECS::Instance indicates that the resource is an Elastic Cloud Service (ECS) instance. The Properties section provides additional options that you can specify for a resource. For example, you must specify an image ID for each ECS instance. The image ID is one of the resource properties. Examples

```json
"Resources" : {
  "ECSInstance" : {
    "Type" : "ALIYUN::ECS::Instance",
    "Properties" : {
      "ImageId" : "m-25l0r****"
```

If a resource does not need properties to be declared, omit the Properties section of that resource. Property values can be text strings, string lists, Boolean values, referenced parameters, or return values of functions. The following example shows how to declare different types of property values:

```json
"Properties" : {
    "String" : "string",
    "LiteralList" : [ "value1", "value2" ],
    "Boolean" : "true"
    "ReferenceForOneValue" :  { "Ref" : "ResourceID" } ,
    "FunctionResultWithFunctionParams" : {
        "Fn::Join" : [ "%", [ "Key=", { "Ref" : "SomeParameter" } ] ] }
```

The DeletionPolicy parameter specifies whether to retain a resource when its stack is deleted. The following sample code shows how to use the DeletionPolicy parameter to retain an ECS instance when its stack is deleted:

```json
"Resources" : {
  "ECSInstance" : {
    "Type" : "ALIYUN::ECS::Instance",
    "Properties" : {
      "ImageId" : "m-25l0r****"
```

`},`

```json
    "DeletionPolicy" : "Retain"
```

The DependsOn parameter allows you to create a specific resource after you create its dependent resource. If you specify the DependsOn parameter for a resource, the resource is created only after its dependent resource specified by the DependsOn parameter is created. In the following example, WebServer is created only after DatabaseServer is created:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "DependsOn": "DatabseServer"
```

`},`

```json
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
```

The Condition parameter specifies whether to create the resource. The resource can be created only when the Condition parameter is set to true. In the following example, WebServer is created only if the condition determined by the MaxAmount parameter is true:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters": {
    "MaxAmount": {
      "Type": "Number",
      "Default": 1
```

`},`

```json
  "Conditions": {
    "CreateWebServer": {"Fn::Not": {"Fn::Equals": [0, {"Ref": "MaxAmount"}]}}
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Condition": "CreateWebServer",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
```

`},`

```json
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
```

**Resource declaration example**

The following example shows how to declare a resource:

```json
"Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [{
            "Key": "Department1",
            "Value": "HumanResource"
        },{
            "Key": "Department2",
            "Value": "Finance"
```

`]` `},`

```json
    "ScalingConfiguration": {
      "Type": "ALIYUN::ESS::ScalingConfiguration",
      "Properties": {
        "ImageId": "ubuntu1404_64_20G_aliaegis_2015****.vhd",
        "InstanceType": "ecs.t1.small",
        "InstanceId": "i-25xhh****",
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 1,
        "InternetMaxBandwidthOut": 20,
        "SystemDisk_Category": "cloud",
        "ScalingGroupId": "bwhtvpcBcKYac9fe3vd0****",
        "SecurityGroupId": "sg-25zwc****",
        "DiskMappings": [
                "Size": 10
```

`},`

```json
                "Category": "cloud",
                "Size": 10
```

`]`

### Outputs

The Outputs section is used to define the values returned when the GetStack operation is called. For example, if you define an Elastic Compute Service (ECS) instance ID as an output item, the ECS instance ID is returned when the GetStack operation is called.

**Syntax**

Each output item consists of an ID and a description. All output descriptions are enclosed in braces {}. Multiple output items are separated by commas (,). Each output item can have multiple values in an array format. The following example shows the Outputs syntax:

```json
"Outputs" : {
  "Output1 ID" : {
    "Description": "The description of the output item",
    "Condition": "The condition that specifies whether to provide resource properties",
    "Value": "The output value expression"
```

`},`

```json
  "Output2 ID" : {
    "Description": "The description of the output item",
    "Condition": "The condition that specifies whether to provide resource properties",
    "Value" : [
      "Output value expression 1",
      "Output value expression 2",
      ...
```

`]` Output ID: the ID of the output item. Duplicate IDs are not allowed within a template. Description: optional. The description of the output item. Value: required. The value returned when the GetStack operation is called. Condition: optional. The condition that specifies whether to create a resource and provide its information. The resource is created and its information is provided only when the specified condition is `true` . In the following example, WebServer is created only if the condition determined by the MaxAmount parameter is true:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters": {
    "MaxAmount": {
      "Type": "Number",
      "Default": 1
```

`},`

```json
  "Conditions": {
    "CreateWebServer": {"Fn::Not": {"Fn::Equals": [0, {"Ref": "MaxAmount"}]}}
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Condition": "CreateWebServer",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
  "Outputs": {
    "WebServerIP": {
      "Condition": "CreateWebServer",
      "Value": {
        "Fn::GetAtt": ["WebServer", "PublicIps"]
```

**Examples**

The following example contains two output items: The InstanceId value of WebServer The PublicIp and PrivateIp values of WebServer

```json
"Outputs": {
  "InstanceId": {
    "Value" : {"Fn::GetAtt": ["WebServer", "InstanceId"]}
```

`},`

```json
  "PublicIp & PrivateIp": {
    "Value" : [
      {"Fn::GetAtt": ["WebServer", "PublicIp"]},
      {"Fn::GetAtt": ["WebServer", "PrivateIp"]}
```

`]`

### Functions

Resource Orchestration Service (ROS) provides several built-in functions to help you manage stacks. You can use built-in functions to define Resources and Outputs.

**Fn::Base64Encode**

The Fn::Base64Encode function is used to return the Base64 representation of the input string. Declaration

```
"Fn::Base64Encode": "stringToEncode"
```

Parameters `stringToEncode` : the string to be encoded in Base64. Return value The Base64 representation of the input string. Examples

```json
{"Fn::Base64Encode": "string to encode"}
```

`c3RyaW5nIHRvIGVuY29kZQ==` is returned in this example.

**Fn::Base64Decode**

The Fn::Base64Decode function is used to return a string decoded from a Base64-encoded string. Declaration

```json
{"Fn::Base64Decode": "stringToEncode"}
```

Parameters `stringToDecode` : the string decoded from the Base64-encoded string. Return value The string decoded from the Base64-encoded string. Examples

```json
{"Fn::Base64Decode": "c3RyaW5nIHRvIGVuY29kZQ=="}
```

`string to encode` is returned in this example.

**Fn::Base64**

The Fn::Base64 function returns the Base64 representation of the input string. Declaration

```
 "Fn::Base64": stringToEncode
```

Parameters valueToEncode: the string to be encoded in Base64. Return value The Base64 representation of the input string. Examples

```
 "Fn::Base64":"string to encode"
```

**Fn::FindInMap**

The Fn::FindInMap function is used to return the values based on keys in a two-level mapping that is declared in the Mappings section. Declaration

```
"Fn::FindInMap": ["MapName", "TopLevelKey", "SecondLevelKey"]
```

Parameters `MapName` : the ID of a mapping declared in the Mappings section that contains keys and values. `TopLevelKey` : the top-level key name. The value is a list of key-value pairs. `SecondLevelKey` : the second-level key name. The value is a string or a number. Return value The value that is assigned to the SecondLevelKey parameter. Examples The ImageId property must be specified when you create a WebServer instance. The Mappings section describes the ImageId mappings by region. The Parameters section describes the regions that must be specified by template users. Fn::FindInMap finds the corresponding ImageId mapping in RegionMap based on the region specified by a user, and then finds the corresponding ImageId values in the mapping. MapName can be set to a custom value, which is `RegionMap` in this example. TopLevelKey is set to the region where the stack is created, which is `{ "Ref" : "regionParam" }` in this example. SecondLevelKey is set to the required architecture, which is `32` in this example.

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
      "Description": "The region where the ECS instance is created",
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

`]` `},`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
```

`},`

```json
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
```

`},`

```json
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
            {"Ref": "regionParam"},
            "32"
```

`]` `},`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "key1",
            "Value": "value1"
```

`},`

```json
            "Key": "key2",
            "Value": "value2"
```

`]` Supported functions Fn::FindInMap Ref

**Fn::GetAtt**

The Fn::GetAtt function is used to return the value of a property from a resource in a template. Declaration

```
"Fn::GetAtt": ["resourceID", "attributeName"]
```

Parameters

| resourceID | : th |
|---|---|
| attributeName |   |

`resourceID` : the ID of the resource. `attributeName` : the name of the resource property. Return value The value of the resource property. Examples The ImageId property of MyEcsInstance is returned in this example.

```json
{"Fn::GetAtt" : ["MyEcsInstance" , "ImageID"]}
```

**Fn::Join**

The Fn::Join function is used to combine a set of values into a single value that is separated by a specified delimiter. Declaration

```json
{"Fn::Join": ["delimiter", ["string1", "string2", ... ]]}
```

Parameters `delimiter` : the value used to divide the string. The delimiter value can be left blank so that all the values are directly combined. `[ "string1", "string2", ... ]` : the list of values that are combined into a string. Return value The combined string. Examples

```json
{"Fn::Join": [ ",", ["a", "b", "c"]]}
```

`"a,b,c"` is returned in this example. Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Select**

The Fn::Select function is used to return a single data element from a list of data elements by using an index. Declaration The following example assumes that the list of data elements is an array:

```
"Fn::Select": ["index", ["value1", "value2", ... ]]
```

The following example assumes that the list of data elements is a mapping table:

```
"Fn::Select": ["index", {"key1": "value1", ... }]
```

Parameters `index` : the index of the object data element. If the list of data elements is an array, the index must be an integer ranging from 0 to N-1, where N indicates the number of elements in the array. If the list of data elements is a mapping table, the index must be a key in the mapping table. If the corresponding value of the index cannot be found, the system returns an empty string. Return value The object data element. Examples The following example assumes that the list of data elements is an array:

```json
{"Fn::Select": ["1", ["apples", "grapes", "oranges", "mangoes"]]}
```

`"grapes"` is returned in this example. The following example assumes that the list of data elements is a mapping table:

```json
{"Fn::Select": ["key1", {"key1": "grapes", "key2": "mangoes"}]}
```

`"grapes"` is returned in this example. The following example assumes that the list of data elements is a comma-delimited list:

```json
"Parameters": {
  "userParam": {
    "Type": "CommaDelimitedList",
      "Default": "10.0.100.0/24, 10.0.101.0/24, 10.0.102.0/24"
"Resources": {
  "resourceID": {
      "Properties": {
          "CidrBlock": {"Fn::Select": ["0", {"Ref": "userParam"}]}
```

Supported functions For the Fn::Select index value, you can use the Ref function. For the Fn::Select list of data elements, you can use the following functions: Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref

**Ref**

The Ref function is used to return the value of a specified parameter or resource. If the specified parameter is a resource ID, the value of the resource is returned. Otherwise, the system returns the value of the specified parameter. Declaration

```json
"Ref": "logicalName"
```

Parameters `logicalName` : the logical name of the resource or parameter that you want to reference. Return value The value of the resource or parameter. Examples The following example demonstrates how to use the Ref function to specify regionParam as the region parameter for RegionMap of WebServer:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
      "Description": "The region where the ECS instance is created",
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

`]` `},`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
```

`},`

```json
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
```

`},`

```json
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
            {"Ref": "regionParam"},
            "32"
```

`]` `},`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "tiantt",
            "Value": "ros"
```

`},`

```json
            "Key": "tiantt1",
            "Value": "ros1"
```

`]` Supported function When you use the Ref function, you cannot use other functions in it at the same time. You must specify a string value for the logical ID of a resource.

**Fn::GetAZs**

The Fn::GetAZs function is used to return a list of zones for a specified region. Declaration

```
"Fn::GetAZs": "region"
```

Parameters `region` : the ID of the region. Return value The list of zones within the specified region. Examples The following example demonstrates how to create an Elastic Compute Service (ECS) instance in the first zone of a specified region:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": "centos7u2_64_40G_cloudinit_2016****.raw",
        "InstanceType": "ecs.n1.tiny",
        "SecurityGroupId": "sg-2zedcm7ep5quses0****",
        "Password": "Ros1****",
        "AllocatePublicIP": true,
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 100,
        "InternetMaxBandwidthOut": 100,
        "SystemDiskCategory": "cloud_efficiency",
        "IoOptimized": "optimized",
        "ZoneId": {"Fn::Select": ["0", {"Fn::GetAZs": {"Ref": "ALIYUN::Region"}}]}
```

`},`

```json
  "Outputs": {
    "InstanceId": {
         "Value": {"Fn::GetAtt": ["WebServer","InstanceId"]}
```

`},`

```json
    "PublicIp": {
         "Value": {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Replace**

The Fn::Replace function is used to replace a specified substring contained in a string with a new substring. Declaration

```json
{"Fn::Replace": [{"object_key": "object_value"}, "object_string"]}
```

Parameters `object_key` : the substring to be replaced. `object_value` : the new substring to replace the previous substring. `object_string` : the string whose `object_key` is replaced. Return value The string after replacement. Examples The following example demonstrates how to replace "print" with "echo" in the specified script:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "centos_7_2_64_40G_base_2017****.vhd",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-94q49****",
        "Password": "MytestPassword****",
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-94vdv8****",
        "VpcId": "vpc-949uz****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData": {"Fn::Replace": [{"print": "echo"},
         {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "print hello > ~/1.txt\n"
         ]]}]}
```

`},`

```json
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
```

`},`

```json
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref

**Fn::Split**

The Fn::Split function is used to split a string into a list of values separated by a specified delimiter and return the list. Declaration

```
"Fn::Split": ["delim", "original_string"]
```

Parameters

| delim | : the speci |
|---|---|
| original string _ |   |

`delim` : the specified delimiter, which can be a comma (,), semicolon (;), line break (\n), or indent (\t). `original_string` : the string to be split. Return value A list of string values. Examples The following example assumes that the list of data elements is an array:

```json
{"Fn::Split": [";", "foo; bar; achoo"]}
```

`["foo", " bar", "achoo "]` is returned in this example. The following example demonstrates how to use Fn::Split to split InstanceIds:

```json
  "Parameters": {
    "InstanceIds": {
      "Type": "String",
      "Default": "instane1_id,instance2_id,instance2_id"
```

`},`

```json
  "Resources": {
    "resourceID": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Fn::Split": [
            ",",
              "Ref": "InstanceIds"
```

`]` Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Fn::Replace Fn::GetAZs Fn::If Ref

**Fn::Equals**

The Fn::Equals function is used to compare whether two values are equal. If the two values are equal, true is returned. If the two values are not equal, false is returned. Declaration

```json
{"Fn::Equals": ["value_1", "value_2"]}
```

Parameters `value` : the values to be compared. Return value true or false. Examples The following example demonstrates how to use Fn::Equals to define a condition in the Conditions section:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "EnvType": {
      "Default": "pre",
      "Type": "String"
```

`},`

```json
  "Conditions": {
    "TestEqualsCond": {
      "Fn::Equals": [
        "prod",
        {"Ref": "EnvType"}
```

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::And**

The Fn::And function is used to represent the AND operator, and must contain at least two conditions. If all the specified conditions are evaluated as true, true is returned. If any condition is evaluated as false, false is returned. Declaration

```json
{"Fn::And": ["condition", {...}]}
```

Parameters `condition` : the condition to be evaluated. Return value true or false. Examples The following example demonstrates how to use Fn::And to define a condition in the Conditions section:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
```

`},`

```json
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestAndCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::Or**

The Fn::Or function is used to represent the OR operator, and must contain at least two conditions. If any specified condition is evaluated as true, true is returned. If all the conditions are evaluated as false, false is returned. Declaration

```json
{"Fn::Or": ["condition", {...}]}
```

Parameters `condition` : the condition to be evaluated. Return value true or false. Examples The following example demonstrates how to use Fn::Or to define a condition in the Conditions section:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
```

`},`

```json
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestOrCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::Not**

The Fn::Not function is used to represent the NOT operator. If a condition is evaluated as false, true is returned. If a condition is evaluated as true, false is returned. Declaration

```json
{"Fn::Not": "condition"}
```

Parameters `condition` : the condition to be evaluated. Return value true or false. Examples The following example demonstrates how to use Fn::Not to define a condition in the Conditions section:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters":{
    "EnvType":{
      "Default":"pre",
      "Type":"String"
```

`},`

```json
  "Conditions": {
    "TestNotCond": {"Fn::Not": {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::If**

This function returns one of two possible values. If a specified condition is evaluated as true, one value is returned. If the specified condition is evaluated as false, the other value is returned. The property values of Resources and Outputs in templates support the Fn::If function. You can use the `ALIYUN::NoValue` pseudo parameter as the return value to delete the corresponding property. Declaration

```json
{"Fn::If": ["condition_name", "value_if_true", "value_if_false"]}
```

Parameters `condition_name` : the name of the condition in the Conditions section. A condition is referenced by using the condition name.

| value if true _ _ | : |
|---|---|
| value if false _ _ |   |

`value_if_true` : If the specified condition is evaluated as true, this value is returned. `value_if_false` : If the specified condition is evaluated as false, this value is returned. Examples The following example demonstrates how to determine whether to create a data disk based on input parameters:

```json
    "ROSTemplateFormatVersion":"2015-09-01",
    "Parameters":{
        "EnvType":{
            "Default":"pre",
            "Type":"String"
```

`},`

```json
    "Conditions":{
        "CreateDisk":{
            "Fn::Equals":[
                "prod",
                    "Ref":"EnvType"
```

`]` `},`

```json
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
```

```json
            "Properties":{
                "DiskMappings":{
                    "Fn::If":[
                        "CreateDisk",
```

`[`

```json
                                "Category":"cloud_efficiency",
                                "DiskName":"FirstDataDiskName",
                                "Size":40
```

`},`

```json
                                "Category":"cloud_ssd",
                                "DiskName":"SecondDataDiskName",
                                "Size":40
```

`],`

```json
                            "Ref":"ALIYUN::NoValue"
```

`]` `},`

```json
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
```

`},`

```json
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

`]` `},`

```json
        "ZoneId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "ZoneId"
```

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref

**Fn::ListMerge**

The Fn::ListMerge function is used to merge multiple lists into one list. Declaration

```json
{"Fn::ListMerge": [["list_1_item_1", "list_1_imte_2", ...], ["list_2_item_1", "list_2_imte_2", ...]
```

`]}` Parameters `["list_1_item_1", "list_1_imte_2", ...]` : the first list to merge. `["list_2_item_1", "list_2_imte_2", ...]` : the second list to merge into the first list. Examples The following example demonstrates how to attach two ECS instance groups to a Server Load Balancer (SLB) instance:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "ros",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
```

`},`

```json
    "BackendServer1": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3****",
        "MaxAmount": 1,
        "MinAmount": 1
```

`},`

```json
    "BackendServer2": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3iu****",
        "MaxAmount": 1,
        "MinAmount": 1
```

`},`

```json
    "Attachment": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "LoadBalancerId": {"Ref": "LoadBalancer"},
        "BackendServerList": { "Fn::ListMerge": [
            {"Fn::GetAtt": ["BackendServer1", "InstanceIds"]},
            {"Fn::GetAtt": ["BackendServer2", "InstanceIds"]}
```

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If

**Fn::GetJsonValue**

The Fn::GetJsonValue function is used to resolve a JSON string and obtain its key value from the first layer. Declaration

```json
{"Fn::GetJsonValue": ["key", "json_string"]}
```

Parameters

| key | : the key |
|---|---|
| json string _ |   |

`json_string` : the specified JSON string to be resolved. Examples In the following example, the WebServer instance executes UserData and returns a JSON string, and the WebServer2 instance then obtains the corresponding key value from the string.

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "Password": "Wenqiao****",
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxze****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData": {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "print hello > ~/1.txt\n",
             "Fn::GetAtt": ["WaitConHandle", "CurlCli"],
             "\n",
             "Fn::GetAtt": ["WaitConHandle", "CurlCli"],
             " -d '{\\"id\\" : \\"1\\", \\"data\\": [\\"1111\\", \\"2222\\"]}'\n"
         ]]},
         "PrivateIpAddress": "192.168.XX.XX",
         "HostName": "userdata-1
```

`},`

```json
    "WaitConHandle": {
        "Type": "ALIYUN::ROS::WaitConditionHandle"
```

`},`

```json
    "WaitCondition": {
        "Type": "ALIYUN::ROS::WaitCondition",
        "Properties": {
          "Handle": {"Ref": "WaitConHandle"},
          "Timeout": 900
```

`},`

```json
    "WebServer2": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
```

```json
        "Password": "Wenqiao****,
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData":
          {"Fn::Join": ["", [
             "#!/bin/sh\n",
             "mkdir ~/test_ros\n",
             "echo hello > ~/1.txt\n",
             "server_1_token=",
             {"Fn::GetJsonValue": ["1", { "Fn::GetAtt": ["WaitCondition", "Data"]}]},
             "\n"
         ]]},
         "PrivateIpAddress": "192.168.XX.XX",
         "HostName": "userdata-2"
```

`},` `},`

```json
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
```

`},`

```json
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If

**Fn::MergeMapToList**

The Fn::MergeMapToList function is used to merge multiple mappings into a list of mapping elements. Declaration

```json
{"Fn::MergeMapToList": [{"key_1": ["key_1_item_1", "key_1_item_2", ...]}, {"key_2":["key_2_item_1", "key_2_item_2", ...]}, ... ]}
```

Parameters `{"key_1": ["key_1_item_1", "key_1_item_2", ...]}` : the first mapping to merge. The `"key_1"` value must be a list. `"key_1"` is the key for each mapping in the list of merged mappings. The "key_1" value is `"key_1_item_1"` for the first merged mapping and `"key_1_item_2"` for the second merged mapping. All values follow the same format. The length of the final list of merged mappings is the length of the longest list `"key_x"` from all mappings being merged. If a `"key_y"` list is shorter, the last element of the list is repeated until the list is the longest.

| {"key 2": ["key 2 item 1", "key 2 item 2", ...]} _ _ _ _ _ _ _ |   | : th |
|---|---|---|
| mapping. The "key 2" value must be a list. "key 2" _ _ The "key 2" value is "key 2 item 1" for the first merge _ _ _ _ | "key 2" _ |   |

second merged mapping. All values follow the same format. Examples The following example demonstrates how to merge three mappings. The length of the list based on the key values for each mapping is the same.

```json
   "Fn::MergeMapToList": [
      {"key_1": ["kye_1_item_1", "kye_1_item_2"]},
      {"key_2": ["kye_2_item_1", "kye_2_item_2"]},
      {"key_3": ["kye_3_item_1", "kye_3_item_2"]}
```

`]` The following code shows the merged result: `[`

```json
      "key_1": "kye_1_item_1",
      "key_2": "kye_2_item_1",
      "key_3": "kye_3_item_1"
```

`},`

```json
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_2",
      "key_3": "kye_3_item_2"
```

`]` The length of the list based on the key values for each mapping varies in the following example:

```json
   "Fn::MergeMapToList": [
      {"key_1": ["kye_1_item_1", "kye_1_item_2"]},
      {"key_2": ["kye_2_item_1", "kye_2_item_2", "key_2_item_3"]},
      {"key_3": ["kye_3_item_1", "kye_3_item_2"]}
```

`]` The following code shows the merged result: `[`

```json
      "key_1": "kye_1_item_1",
      "key_2": "kye_2_item_1",
      "key_3": "kye_3_item_1"
```

`},`

```json
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_2",
      "key_3": "kye_3_item_2"
```

`},`

```json
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_3",
      "key_3": "kye_3_item_2"
```

`]` In the following template example, all instances created in WebServer are added to the vServer group of an SLB instance:

```json
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
        "WebServer": {
          "Type": "ALIYUN::ECS::InstanceGroupClone",
          "Properties": {
              "SourceInstanceId": "i-xxxxx",
               "Password": "Hello****",
               "MinAmount": 1,
               "MaxAmount": 1
```

`},`

```json
        "CreateVServerGroup": {
            "Type": "ALIYUN::SLB::VServerGroup",
            "Properties": {
                "LoadBalancerId": "lb-****",
                "VServerGroupName": "VServerGroup-****",
                "BackendServers": {
                   "Fn::MergeMapToList": [
                       {"Port": [6666, 9090, 8080]},
                       {"ServerId": {"Fn::GetAtt": ["WebServer", "InstanceIds"]}},
                       {"Weight": [20, 100]}
```

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If Fn::ListMerge Fn::GetJsonValue

**Fn::Avg**

The Fn::Avg function is used to return the average value of a set of numbers. Declaration

```json
{"Fn::Avg": [ndigits, [number1, number2, ... ]]}
```

Parameters

| ndigits | : the number of de |
|---|---|
| [ number1, number2, ... ] |   |

`ndigits` : the number of decimal places to display. This parameter value must be an integer. `[ number1, number2, ... ]` : the set of numbers for which the average value will be calculated. Each element in the group must be a number or a string that can be converted into a number. Return value The average value of the set of numbers. Examples

```json
{ "Fn::Avg": [ 1, [1, 2, 6.0] ] } { "Fn::Avg": [ 1, ['1', '2', '6.0'] ] }
```

**3.0** is returned in this example.
Supported functions Fn::GetAtt Ref

**Fn::SelectMapList**

The Fn::SelectMapList function is used to return a list of map elements. Declaration

```json
{"Fn::SelectMapList": ["key2", [{"key1": "value1-1", "key3": "value1-3"}, {"key1": "value2-1", "key 2": "value2-2"}, {"key1": "value3-1", "key2": "value3-2"}, ...] ] }
```

Parameters

| key2 | : the key to be queried in the map. |
|---|---|
| [{ "key1": "value1-1", "key3": "value1-3" }, ... ] |   |

Return value A list of key values for all maps in the map list. Examples

```
 "Fn::SelectMapList": [
   "key2",
```

`[`

```json
      {"key1": "value1-1", "key3": "value1-3"},
      {"key1": "value2-1", "key2": "value2-2"},
      {"key1": "value3-1", "key2": "value3-2"}
```

`]` `]` `["value2-2","value3-2"]` is returned in this example.

**Fn::Add**

The Fn::Add function is used to sum the values of parameters. Declaration

```json
{"Fn::Add": [{"Product": "ROS"}, {"Fn": "Add"}]}
```

Parameters The parameters must be arranged as a list. The parameters in the list can be of the Number, List, or Dictionary type. All the parameters must be of the same type. The list must contain at least two parameters. Return value If the parameter values are numbers, sum the parameter values. If the parameter values are lists, concatenate the values. If the parameter values are dictionaries, merge the values. If the two parameters have the same key, overwrite the former parameter value with the latter. Examples

```json
 "Fn::Add": [
   {"Product": "ROS"},
   {"Fn": "Add"}
```

`]` `{"Fn":"Add","Product":"ROS"}` is returned in this example.

### Mappings

The Mappings section is a key-value mapping table. When mappings are used in resource and output definitions, use Fn::FindInMap to find their values by specifying corresponding keys.

**Syntax**

A mapping consists of key-value pairs, where both the keys and values can be strings or numbers. Multiple mappings are separated by commas (,). Each mapping name must be unique. Mappings must be pure data and cannot parse functions.

**Examples**

The following example shows a correct mapping definition:

```json
"Mappings": {
    "ValidMapping": {
        "TestKey1": {"TestValu1": "value1"},
        "TestKey2": {"TestValu2": "value2"},
        1234567890: {"TestValu3": "value3"},
        "TestKey4": {"TestValu4": 1234}
```

The following example shows an incorrect mapping definition:

```json
"Mappings": {
    "InvalidMapping1": {
        "ValueList": ["foo", "bar"],
          "ValueString": "baz"
```

`},`

```json
    "InvalidMapping2": ["foo", {"bar" : "baz"}],
    "InvalidMapping3": "foobar"
```

The following example shows how to use Fn::FindInMap to find the return value:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "regionParam": {
      "Description": "The region where the ECS instance is created",
      "Type": "String",
      "AllowedValues": [
        "hangzhou",
        "beijing"
```

`]` `},`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
```

`},`

```json
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
```

`},`

```json
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
              "Ref": "regionParam"
```

`},`

```
            "32"
```

`]` `},`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "Department1",
            "Value": "HumanResource"
```

`},`

```json
            "Key": "Department2",
            "Value": "Finance"
```

`]`

### Conditions

Condition bodies are defined by Fn::And, Fn::Or, Fn::Not, and Fn::Equals operators. These operators, along with the parameters that you specify when you create or update a stack, are used to evaluate each condition. You can reference other conditions, parameters, and mappings in your condition. Conditions are used in resource and output definitions to establish dependencies. Use Fn::If or Condition in resource and output definitions to implement conditions.

**Syntax**

Each condition consists of a condition name and a condition body. The condition name is a string. The condition body starts with Fn::And, Fn::Or, Fn::Not, or Fn::Equals. You can reference other conditions in your condition. Separate multiple conditions with comma (,). Each condition name must be unique. The following functions can be used, but not as the outermost functions: "Fn::Select", "Fn::Join", "Fn::Split", "Fn::Replace","Fn::Base64Encode", "Fn::Base64Decode", "Fn::MemberListToMap","Fn::If", "Fn::ListMerge", "Fn::GetJsonValue", "Fn::MergeMapToList","Fn::SelectMapList", "Fn::Add", "Fn::Avg", "Fn::Str", "Fn::Calculate","Ref"(parameter references only), and "Fn:: FindInMap".

**Examples**

The following example shows how to define conditions:

```json
"Conditions" : {
       "DevEnv": {"Fn::Equals": ["Dev", {"Ref": "EnvType"}]},
       "UTEnv": {"Fn::Equals": ["UT", {"Ref": "EnvType"}]},
       "PREEnv": {"Fn::Not": {"Fn::Or": ["DevEnv", "UTEnv"]}},
       "ProdEnv": {"Fn::And": [{"Fn::Equals": ["Prod", {"Ref": "EnvType"}]}, "PREEnv"]}
```

The following example shows how to use conditions in a resource definition. In this example, a condition is used to determine whether to create a data disk and an Object Storage Service (OSS) bucket for an Elastic Compute Service (ECS) instance based on the EnvType value.

```json
    "ROSTemplateFormatVersion":"2015-09-01",
    "Parameters":{
        "EnvType":{
            "Default":"pre",
            "Type":"String"
```

`},`

```json
    "Conditions":{
        "CreateProdRes":{
            "Fn::Equals":[
                "prod",
                    "Ref":"EnvType"
```

`]` `},`

```json
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
            "Properties":{
                "DiskMappings":{
                    "Fn::If":[
                        "CreateProdRes",
```

`[`

```json
                                "Category":"cloud_efficiency",
                                "DiskName":"FirstDataDiskName",
                                "Size":40
```

`},`

```json
"Category":"cloudssd"
```

```json
                                Category:cloud_ssd,
                                "DiskName":"SecondDataDiskName",
                                "Size":40
```

`],`

```json
                            "Ref":"ALIYUN::NoValue"
```

`]` `},`

```json
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
```

`},`

```json
        "OssBucket": {
            "Type": "ALIYUN::OSS::Bucket",
            "Condition": "CreateProdRes",
            "Properties": {
                "AccessControl": "private",
                "BucketName": "myprodbucket"
```

`},`

```json
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

`]` `},`

```json
        "OssDomain":{
            "Condition": "CreateProdRes",
            "Value":{
                "Fn::GetAtt":[
                    "OssBucket",
                    "DomainName"
```

`]`

## Resource types

### ECS

#### ALIYUN::ECS::AutoSnapshotPolicy

ALIYUN::ECS::AutoSnapshotPolicy is used to create an automatic snapshot policy.

**Syntax**

```json
  "Type" : "ALIYUN::ECS::AutoSnapshotPolicy",
  "Properties" : {
    "TimePoints" : String,
    "RepeatWeekdays" : String,
    "RetentionDays" : Integer,
    "DiskIds" : List,
    "Tags": List,
    "AutoSnapshotPolicyName" : String,
    "ResourceGroupId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TimePoints | List | Yes | Yes | The points in time of a day at which to create automatic snapshots. | Valid values: 0 to 23. The values from 0 to 23 indicate the 24 points in time on the hour from 00:00 to 23:00. For example, 1 indicates 01:00. Unit: hours. If you need automatic snapshots to be created at several times in a day, you can specify multiple hours. You can specify up to 24 hours. You must set this property to a list. Example: [0, 1, ... 23]. Separate multiple hours with commas (,). |
| RepeatWeekd ays | List | Yes | Yes | The days of a week on which to create automatic snapshots. | Valid values: 1 to 7. The values from 1 to 7 indicate the seven days in a week from Monday to Sunday. Cycle: week. If you need automatic snapshots to be created at several times in a week, you can specify multiple days. You must set this property to a list. Example: [1, 2, ... 7]. Separate multiple days with commas (,). You can specify up to seven days. |

| RetentionDay s | Integer | Yes | Yes | The number of days for which the system retains automatic snapshots. | Default value: -1. Valid values: -1: permanently retains automatic snapshots. 1 to 65535: retains automatic snapshots based on the number of days that you specify. Unit: days. |
|---|---|---|---|---|---|
| DiskIds | List | No | Yes | The IDs of disks to which you want to apply the automatic snapshot policy. | If you need to apply the automatic snapshot policy to multiple disks, you must set this property to a list in the ["d- xxxxxxxxx", "d-yyyyyyyyy", … "d-zzzzzzzzz"] format. Separate multiple IDs with commas (,). |
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the automatic snapshot policy belongs. | None |
| Tags | List | No | Yes | The tags of the automatic snapshot policy. | You can add up to 20 tags. For more information, see Tags properties. |
| AutoSnapshot PolicyName | String | No | Yes | The name of the automatic snapshot policy. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . By default, this property is empty. |

|   | http:// |
|---|---|
| https:// |   |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with aliyun or acs: . |

| Value | String | No | No | The value of the tag. | The tag value can be up to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with aliyun or acs: . |
|---|---|---|---|---|---|

**Return value**

Fn::GetAtt AutoSnapshotPolicyId: the ID of the automatic snapshot policy.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DiskIds:
    Type: CommaDelimitedList
    AssociationProperty: ALIYUN::ECS::Disk::DiskId
    Description: The disk ID. When you want to apply the automatic snapshot policy to multiple disk
s, you can set the DiskIds to an array. The format is list of ["d-xxxxxxxxx", "d-yyyyyyyyy", ..., " d-zzzzzzzzz"] and the IDs are separated by commas (,). Resources:
  AutoSnapshotPolicy:
    Type: ALIYUN::ECS::AutoSnapshotPolicy
    Properties:
      TimePoints:
      DiskIds:
        Ref: DiskIds
      RetentionDays: 1
      RepeatWeekdays:
Outputs:
  AutoSnapshotPolicyId:
    Description: The automatic snapshot policy ID.
    Value:
      Fn::GetAtt:
        - AutoSnapshotPolicy
        - AutoSnapshotPolicyId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "DiskIds": {
      "Type": "CommaDelimitedList",
      "AssociationProperty": "ALIYUN::ECS::Disk::DiskId",
      "Description": "The disk ID. When you want to apply the automatic snapshot policy to multiple
disks, you can set the DiskIds to an array. The format is list of [\"d-xxxxxxxxx\", \"d-yyyyyyyyy\" , ..., \"d-zzzzzzzzz\"] and the IDs are separated by commas (,)."
```

`},`

```json
  "Resources": {
    "AutoSnapshotPolicy": {
      "Type": "ALIYUN::ECS::AutoSnapshotPolicy",
      "Properties": {
        "TimePoints": [
          20,
```

`],`

```json
        "DiskIds": {
          "Ref": "DiskIds"
```

`},`

```json
        "RetentionDays": 1,
        "RepeatWeekdays": [
```

`1,` `]` `},`

```json
  "Outputs": {
    "AutoSnapshotPolicyId": {
      "Description": "The automatic snapshot policy ID.",
      "Value": {
        "Fn::GetAtt": [
          "AutoSnapshotPolicy",
          "AutoSnapshotPolicyId"
```

`]` For more examples, visit AutoSnapshotPolicy.json and AutoSnapshotPolicy.yml.

#### ALIYUN::ECS::BandwidthPackage

ALIYUN::ECS::BandwidthPackage is used to create a service plan for a NAT gateway.

**Syntax**

```json
  "Type": "ALIYUN::ECS::BandwidthPackage",
  "Properties": {
    "Description": String,
    "NatGatewayId": String,
    "ZoneId": String,
    "BandwidthPackageName": String,
    "Bandwidth": Integer,
    "IpCount": Integer
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NatGatewayId | String | Yes | No | The ID of the NAT gateway to which you want to bind the service plan. | None |
| Bandwidth | Integer | Yes | No | The bandwidth. | Valid values: 5 to 5000. Unit: Mbit/s. Default value: 5. |
| IpCount | Integer | Yes | No | The number of public IP addresses assigned to the NAT gateway. | Valid values: 1 to 5. |
| Description | String | No | No | The description of the service plan. | The description must be 2 to 256 characters in length. |
| ZoneId | String | No | No | The ID of the zone where the NAT gateway resides. | None |
| BandwidthPack ageName | String | No | No | The name of the service plan. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter. |

**Response parameters**

Fn::GetAtt BandwidthPackageId: the ID of the service plan. BandwidthPackageIps: all IP addresses included in the service plan.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "BandwidthPackage": {
      "Type": "ALIYUN::ECS::BandwidthPackage",
      "Properties": {
        "BandwidthPackageName": "pkg_2",
        "Description": "my_bandwidth",
        "NatGatewayId": "ngw-h1xox****",
        "IpCount": 2,
        "Bandwidth": 5,
        "ZoneId": "cn-beijing-c"
```

`},`

```json
  "Outputs": {
    "BandwidthPackageId": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageId"]}
```

`},`

```json
    "BandwidthPackageIps": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageIps"]}
```

#### ALIYUN::ECS::Command

ALIYUN::ECS::Command is used to create a Cloud Assistant command.

**Statement**

```json
  "Type": "ALIYUN::ECS::Command",
  "Properties": {
    "Name": String,
    "WorkingDir": String,
    "CommandContent": String,
    "Timeout": Integer,
    "Type": String,
    "Description": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | True | The name of the command, which supports all character sets. The name can be up to 30 characters in length. | None |
| WorkingDir | String | Yes | True | The working directory on the ECS instance where the command will be run. | None |

| CommandContent | String | Yes | Released | The Base64-encoded content of the command. When you specify request parameters Type you must also specify this parameter. The parameter value must be Base64-encoded and cannot exceed 16 KB in size after encoding. | None |
|---|---|---|---|---|---|
| Timeout | String | No. | True | The timeout period that is specified for the command to run on ECS instances. Unit: seconds. If the command fails to run within the specified period, the command execution will time out and the process will be forcibly terminated. Default value: 3600. | None |
| Type | String | No | No | The command type. Valid values: RunBatScript: Creates a Bat script for a Windows instance. RunPowerShellScript: Create a PowerShell script to run on a Windows instance. RunShellScript: Creates a Shell script for Linux- based instances. | None |
| Description | String | Yes | True | The description of the command, which supports all character sets. The description can be up to 100 characters in length. | None |

**Response parameters**

Fn::GetAtt CommandId: the ID of the command.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "WorkingDir": {
      "Type": "String",
      "Description": "The path where command will be executed in the instance."
```

`},`

```json
    "CommandContent": {
      "Type": "String",
      "Description": "The content of command. Content requires base64 encoding. Maximum size support
16KB."
```

`},`

```json
    "Type": {
      "Type": "String",
      "Description": "The type of command."
```

`},`

```json
    "Description": {
      "Type": "String",
      "Description": "The description of command."
```

`},`

```json
    "Timeout": {
      "Type": "Number",
      "Description": "Total timeout when the command is executed in the instance. Input the time unit
as second. Default is 3600s."
```

`},`

```json
    "Name": {
      "Type": "String",
      "Description": "The name of command."
```

`},`

```json
  "Resources": {
    "Command": {
      "Type": "ALIYUN::ECS::Command",
      "Properties": {
        "WorkingDir": {
          "Ref": "WorkingDir"
```

`},`

```json
        "CommandContent": {
          "Ref": "CommandContent"
```

`},`

```json
        "Type": {
          "Ref": "Type"
```

`},`

```json
        "Description": {
          "Ref": "Description"
```

`},`

```json
        "Timeout": {
          "Ref": "Timeout"
```

`},`

```json
        "Name": {
          "Ref": "Name"
```

`},`

```json
  "Outputs": {
    "CommandId": {
      "Description": "The id of command created.",
      "Value": {
        "Fn::GetAtt": [
          "Command",
          "CommandId"
```

`]`

#### ALIYUN::ECS::CustomImage

ALIYUN::ECS::CustomImage is used to create a custom image.

**Statement**

```json
  "Type": "ALIYUN::ECS::CustomImage",
  "Properties": {
    "Description": String,
    "InstanceId": String,
    "ImageName": String,
    "ImageVersion": String,
    "SnapshotId": String,
    "Tag": List,
    "ResourceGroupId": String,
    "Platform": String,
    "DiskDeviceMapping": List,
    "Architecture": String
```

**Properties**

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the image. | The description can be up to 256 characters in length. This parameter is empty by default. It cannot start with http:// or https://. |
| InstanceId | String | Yes | Released | The ID of the ECS instance. | If this parameter is specified, an ECS instance will be used to create the custom image. |
| ImageName | String | Yes | Released | The name of the image. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ and hyphens(-). It must start with a letter but cannot start with http:// or https://. |
| ImageVersion | String | Yes | Released | The image version. | The image version must be 1 to 40 characters in length. |
| SnapshotId | String | Yes | Released | The ID of the snapshot. | If this parameter is specified, a snapshot will be used to create the custom image. If both this parameter and the InstanceId parameter are specified, this parameter will be ignored and an instance will be used to create the custom image. |
| Tags | List | Erased | Released | The tags of the image. | None |
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the custom image belongs. | None |

| Platform | String | Yes | Released | If you specify a data disk snapshot to be used to create the system disk of the custom image, you must use the Platform parameter to determine the release version of the operating system for the system disk. | None |
|---|---|---|---|---|---|
| DiskDeviceMappin g | List | Erased | Released | The mappings between images and snapshots. | None |
| Architecture | String | Yes | Released | If you specify a data disk snapshot to be used to create the system disk of the custom image, you must use the Architecture parameter to determine the architecture of the system disk. Default value: x86 64. _ | Valid values: i386 x86 64 _ |

**Tag syntax**

```json
"Tag": [
    "Key": String,
    "Value": String
```

`]`

**Tag properties**

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | Released | The tag key of the image. | The tag key cannot be a null string. The key can be up to 64 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://. |
| Value | String | Yes | Released | The tag value of the image. | The tag value can be an empty string. The value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://. |

**DiskDeviceMapping**

```json
"DiskDeviceMapping": [
    "Device": String,
    "SnapshotId": String,
    "Size": Integer,
    "DiskType": String
```

`]`

**DiskDeviceMapping properties**

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Device | String | Yes | Released | The device name of disk N in the custom image. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot that is used to create the custom image. | None |
| Size | String | Optional | Released | The size of disk N. Unit: GiB. | Valid values: 5 to 2000. The default value is the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. If the DiskDeviceMapping.N.S napshotId parameter is not specified, the default disk size is 5 GiB. The disk size must be greater than or equal to the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. |
| DiskType | String | Yes | Released | The type of disk N in the custom image. You can specify this parameter to create the system disk of the custom image from a data disk snapshot. If you do not specify this parameter, the disk type is determined by the corresponding snapshot. | Valid values: system: indicates a system disk. data: indicates a data disk. |

**Response parameters**

Fn::GetAtt ImageId: the ID of the custom image.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "MinAmount": 1,
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "ImageId": {
          "Ref": "CustomImage"
```

`},`

```json
        "IoOptimized": "optimized",
        "SystemDisk_Description": "SystemDisk.Description",
        "SystemDisk_DiskName": "SystemDisk.DiskName",
        "SystemDisk_Category": "cloud_ssd",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "Password": "Wenqiao****",
        "InstanceType": "ecs.n1.medium",
        "MaxAmount": 1
```

`},`

```json
    "CustomImage": {
      "Type": "ALIYUN::ECS::CustomImage",
      "Properties": {
        "InstanceId": "i-2zefq1f3ynnrr89q****",
        "SnapshotId": "s-2ze0ibk1pvak4mw6****",
        "ImageName": "image-test-****",
        "ImageVersion": "verison-6-1"
```

`},`

```json
  "Outputs": {
    "CustomImage": {
      "Value": {
        "Fn::GetAtt": [
          "CustomImage",
          "ImageId"
```

`]` `},`

```json
    "InstanceIds": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceIds"
```

`]`

#### ALIYUN::ECS::DedicatedHost

ALIYUN::ECS::DedicatedHost is used to create a dedicated host.

**Statement**

```json
  "Type": "ALIYUN::ECS::DedicatedHost",
  "Properties": {
    "DedicatedHostType": String,
    "DedicatedHostName": String,
    "AutoReleaseTime": String,
    "Description": String,
    "AutoPlacement": String,
    "Tags": List,
    "ActionOnMaintenance": String,
    "NetworkAttributesSlbUdpTimeout": Integer,
    "ChargeType": String,
    "ResourceGroupId": String,
    "ZoneId": String,
    "NetworkAttributesUdpTimeout": Integer,
    "Quantity": Integer
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DedicatedHos tType | String | No | No | The dedicated host type. | None |
| DedicatedHos tName | String | Yes | Released | The name of the dedicated host. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), _ and hyphens (-). Must start with an uppercase or lowercase letter, and cannot start with http:// or https:// the beginning. It can contain digits, colons (:), underscores ( ), _ and hyphens (-). |

|   | http:// |
|---|---|
| https:// |   |

| AutoReleaseT ime | String | Yes | Released | The time scheduled for the dedicated host to be automatically released. If you do not specify the AutoReleaseTime parameter, the dedicated host will not be automatically released. The minimum release time must be at least 30 minutes after the current time. The maximum release time must be at most three years from the current time. If the value of ss is not 00 , the start time is automatically rounded down to the nearest minute based on the value of mm . | None |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the dedicated host. | None |
| ZoneId | String | Yes | Released | The ID of the zone where the dedicated host resides. This parameter is empty by default. If this parameter is not specified, the system will automatically select a zone. | None |
| ChargeType | String | Yes | Released | The billing method of the dedicated host. | Valid values: PostPaid and pay-as-you-go. |
| AutoPlaceme nt | String | Yes | Released | Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify a DedicatedHostId when you create an instance on a DDH, Alibaba Cloud automatically selects a DDH from the resource pool to host the instance. | Valid values: on off Note If you do not specify this parameter, the dedicated host is added to the automatic deployment resource pool. If you do not want to add the dedicated host to the resource pool for automatic deployment, set the value to off. |

| Tags | List |   | Erased |   | Released |   | The custom tags of the instance. |   | A maximum of 20 tags are supported. The format is as follows: [{"Key": |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | [{"Key": |   |
|   |   |   |   |   |   |   |   | gs of | "tagKey", "Value": |   |   |
|   |   |   |   |   |   |   |   |   | "tagValue"},{"Key": |   |   |
|   |   |   |   |   |   |   |   |   | "tagKey2", "Value": |   |   |
|   |   |   |   |   |   |   |   |   | "tagValue2"}] |   |   |
| ActionOnMain tenance | String |   | Yes |   | Released |   | The method used to migrate the instances on the DDH when the DDH fails or needs to be repaired online. |   | Valid valus: Migrate: specifies that the instances are migrated to another physical server and restarted. Stop: specifies that all the instances on the DDH are stopped. If the DDH cannot be repaired, the instances are migrated to another physical server and restarted. The default value is "Migrate" for a dedicated host and "Stop" for a local disk. |   |   |
| NetworkAttrib utesSlbUdpTi meout | String |   | Optional |   | Released |   | The timeout period for a UDP session. |   | Valid values: 15 to 310. Unit: seconds. |   |   |
| ResourceGro upId | String |   | Yes |   | Released |   | The ID of the resource group to which the dedicated host belongs. |   | None |   |   |
| NetworkAttrib utesUdpTime out | String |   | Optional |   | Released |   | The timeout period for UDP sessions that users can access for cloud services running on the dedicated host. |   | Valid values: 15 to 310. Unit: seconds. |   |   |
| Quantity | String |   | Optional |   | Released |   | The number of DDHs that you want to create this time. |   | Valid values: 1 to 100. Default value: 1 |   |   |

**Response parameters**

Fn::GetAtt OrderId: the ID of the order. DedicatedHostIds: the list of host IDs.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AutoRenewPeriod": {
      "Type": "Number",
      "Description": "The time period of auto renew. When the parameter InstanceChargeType is
PrePaid, it will take effect.It could be 1, 2, 3, 6, 12\. Default value is 1.",
      "AllowedValues": [
```

`1,` `2,` `3,` `6,` `],`

```json
      "Default": 1
```

`},`

```json
    "Description": {
      "Type": "String",
      "Description": "The description of host."
```

`},`

```json
    "ZoneId": {
      "Type": "String",
      "Description": "The zone to create the host."
```

`},`

```json
    "DedicatedHostName": {
      "Type": "String",
      "Description": "The name of the dedicated host, [2, 128] English or Chinese characters. It must
begin with an uppercase/lowercase letter or a Chinese character, and may contain numbers, '_' or '-'. It cannot begin with http:// or https://."
```

`},`

```json
    "ChargeType": {
      "Type": "String",
      "Description": "Instance Charge type, allowed value: Prepaid and Postpaid. If specified
Prepaid, please ensure you have sufficient balance in your account. Or instance creation will be fail ure. Default value is Postpaid.",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
```

`},`

```json
    "AutoRenew": {
      "Type": "String",
      "Description": "Whether renew the fee automatically? When the parameter InstanceChargeType is P
rePaid, it will take effect. Range of value:True: automatic renewal.False: no automatic renewal. Defa ult value is False.",
      "AllowedValues": [
        "True",
        "False"
```

`],`

```json
      "Default": "False"
```

`},`

```json
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. Unit is month, it could be from 1 to 9 or 12, 24, 36, 48,
60\. Default value is 1.",
      "AllowedValues": [
```

`1,` `2,` `3,` `4,` `5,` `6,` `7,` `8,` `9,`

```
        12,
        24,
        36,
        48,
```

`],`

```json
"Default":1
```

```json
      "Default": 1
```

`},`

```json
    "DedicatedHostType": {
      "Type": "String",
      "Description": "The instance type of host."
```

`},`

```json
    "PeriodUnit": {
      "Type": "String",
      "Description": "Unit of prepaid time period, it could be Week/Month. Default value is Month.",
      "AllowedValues": [
        "Week",
        "Month"
```

`],`

```json
      "Default": "Month"
```

`},`

```json
    "AutoReleaseTime": {
      "Type": "String",
      "Description": "Auto release time for created host, Follow ISO8601 standard using UTC time. for
mat is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
```

`},`

```json
  "Resources": {
    "Host": {
      "Type": "ALIYUN::ECS::DedicatedHost",
      "Properties": {
          "Description": {
          "Ref": "Description"
```

`},`

```json
        "ZoneId": {
          "Ref": "ZoneId"
```

`},`

```json
        "DedicatedHostName": {
          "Ref": "DedicatedHostName"
```

`},`

```json
        "ChargeType": {
          "Ref": "ChargeType"
```

`},`

```json
          "DedicatedHostType": {
          "Ref": "DedicatedHostType"
```

`},`

```json
        "PeriodUnit": {
          "Ref": "PeriodUnit"
```

`},`

```json
        "AutoReleaseTime": {
          "Ref": "AutoReleaseTime"
```

`},`

```json
  "Outputs": {
    "OrderId": {
      "Description": "The order id list of created instance.",
      "Value": {
        "Fn::GetAtt": [
          "Host",
          "OrderId"
```

`]` `},`

```json
    "DedicatedHostIds": {
      "Description": "The host id list of created hosts",
      "Value": {
        "Fn::GetAtt": [
```

```
          "Host",
          "DedicatedHostIds"
```

`]`

#### ALIYUN::ECS::Disk

ALIYUN::ECS::Disk creates an ECS cloud disk.

**Syntax**

```json
  "Type": "ALIYUN::ECS::Disk",
  "Properties": {
    "StorageSetId": String,
    "Description": String,
    "Tags": List,
    "AutoSnapshotPolicyId": String,
    "Encrypted": Boolean,
    "DiskName": String,
    "DiskCategory": String,
    "ResourceGroupId": String,
    "KMSKeyId": String,
    "DeleteAutoSnapshot": Boolean,
    "SnapshotId": String,
    "StorageSetPartitionNumber": Integer,
    "PerformanceLevel": String,
    "ZoneId": String,
    "Size": Integer,
    "BurstingEnabled": Boolean,
    "ProvisionedIops": Integer,
    "MultiAttach": String,
    "InstanceId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The resource group ID of the cloud disk. | None. |
| ZoneId | String | No | No | The zone ID for creating the pay-as- you-go cloud disk. | If you do not specify InstanceId, you must specify ZoneId. You cannot specify both ZoneId and InstanceId. |

| DiskName | String | No | No | The cloud disk name. | 2 to 128 characters. Must start with a letter. Cannot start with http:// or https:// . Can contain letters, digits, periods (.), underscores ( ), _ and hyphens (-). |
|---|---|---|---|---|---|
| Description | String | No | No | The cloud disk description. | 2 to 256 characters. Cannot start with http:// or https:// . |
| InstanceId | String | No | No | The subscription instance ID to attach the subscription cloud disk to. | If InstanceId is specified, ResourceGroupId, Tags, and KMSKeyId are ignored. You cannot specify both ZoneId and InstanceId. Default: null. Creates a pay-as- you-go cloud disk in the region and zone specified by RegionId and ZoneId. |
| Tags | List | No | No | The tags. | Up to 20 tags. Tags properties. |
| DiskCategory | String | No | No | The cloud disk category. | Valid values: cloud (default): basic disk cloud efficiency: ultra disk _ cloud ssd: standard SSD _ cloud essd: Enterprise SSD _ (ESSD) |
| SnapshotId | String | No | No | The snapshot ID. | If both SnapshotId and Size are specified, SnapshotId takes precedence. The created cloud disk uses the specified snapshot size. Note Snapshots created on or before July 15, 2013 cannot create cloud disks. |

|   | http:// |
|---|---|
| https:// |   |

| PerformanceL evel | String | No | No | The ESSD performance level (PL). | Valid values: PL0: An ESSD can deliver up to 10,000 random read/write IOPS. PL1 (default): An ESSD can deliver up to 50,000 random read/write IOPS. PL2: An ESSD can deliver up to 100,000 random read/write IOPS. PL3: An ESSD can deliver up to 1,000,000 random read/write IOPS. ESSDs. |
|---|---|---|---|---|---|
| Size | Integer | No | No | The cloud disk size. | cloud: 5 to 2000. cloud efficiency: 20 to _ 32768. cloud ssd: 20 to 32768. _ cloud essd: 20 to 32768. _ Unit: GiB. Must be greater than or equal to the specified snapshot size. |
| BurstingEnabl ed | Boolean | No | No | Whether to enable burst mode. | Valid values: true false (default) |
| ProvisionedIo ps | Integer | No | No | The preconfigured IOPS. | None. |
| AutoSnapshot PolicyId | String | No | No | The automatic snapshot policy ID. | None. |
| Encrypted | Boolean | No | No | Whether to encrypt the cloud disk. | Valid values: true false (default) |
| DeleteAutoSn apshot | Boolean | No | No | Whether to delete automatic snapshots when the cloud disk is released. | Valid values: true (default) false |
| StorageSetId | String | No | No | The storage set ID. | None. |

| KMSKeyId | String | No | No | The Key Management Service (KMS) key ID for the cloud disk. | None. |
|---|---|---|---|---|---|
| StorageSetPa rtitionNumber | Integer | No | No | The number of storage set partitions. | None. |
| MultiAttach | String | No | No | Whether to enable multi- attach. | Valid values: Disabled (default): Multi- attach is disabled. Enabled: Enables multi- attach. Valid only for ESSDs. Note Multi-attach cloud disks support only pay-as-you- go billing. |

**Tags syntax**

```json
"Tags" : [
    "Value" : String,
    "Key" : String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | 1 to 128 characters. Cannot contain http:// or https:// . Cannot start with aliyun or acs: . |
| Value | String | No | No | The tag value. | Up to 128 characters. Cannot contain http:// or https:// . Cannot start with aliyun or acs: . |

|   |   | http:// |
|---|---|---|
| https:// |   |   |

|   |   | http:// |
|---|---|---|
| https:// |   |   |

**Return values**

Fn::GetAtt DiskId: the cloud disk ID. Status: the cloud disk state.

**Examples**

**YAML  format**

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  ZoneId:
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Type: String
    Label:
      en: VSwitch Availability Zone
Resources:
  DataDisk:
    Type: ALIYUN::ECS::Disk
    Properties:
      Size: 10
      ZoneId:
        Ref: ZoneId
      DiskName: DataDisk
Outputs:
  DiskId:
    Value:
      Fn::GetAtt:
        - DataDisk
        - DiskId
  Status:
    Value:
      Fn::GetAtt:
        - DataDisk
        - Status
```

**JSON  format**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Label": {
        "en": "VSwitch Availability Zone"
```

`},`

```json
  "Resources": {
    "DataDisk": {
      "Type": "ALIYUN::ECS::Disk",
      "Properties": {
        "Size": 10,
        "ZoneId": {
          "Ref": "ZoneId"
```

`},`

```json
        "DiskName": "DataDisk"
```

`},`

```json
  "Outputs": {
    "DiskId": {
      "Value": {
        "Fn::GetAtt": [
          "DataDisk",
          "DiskId"
```

`]` `},`

```json
    "Status": {
      "Value": {
        "Fn::GetAtt": [
          "DataDisk",
          "Status"
```

`]`

#### ALIYUN::ECS::DiskAttachment

ALIYUN::ECS::DiskAttachment is used to attach a disk to an ECS instance.

**Syntax**

```json
  "Type": "ALIYUN::ECS::DiskAttachment",
  "Properties": {
    "InstanceId": String,
    "Device": String,
    "DeleteWithInstance": Boolean,
    "DiskId": String,
    "DeleteAutoSnapshot": Boolean
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | Yes | No | The ID of the ECS instance to which you want to attach the disk. | None |
| DiskId | String | Yes | No | The ID of the disk. | The disk and ECS instance must reside within the same zone. |
| Device | String | No | No | The device name of the disk. | If you do not set this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| DeleteWithInsta nce | Boolean | No | No | Specifies whether to release the disk together with the instance. | Valid values: true: releases the disk when the instance is released. false: retains the disk when the instance is released. |
| DeleteAutoSnap shot | Boolean | No | No | Specifies whether to delete automatic snapshots of the disk when the disk is released. | Default value: true. Valid values: true: false |

**Response parameters**

Fn::GetAtt DiskId: the ID of the created disk. Status: the status of the created disk. Device: the device name of the created disk.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  InstanceId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Instance::InstanceId
  DiskId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Disk::DiskId
Resources:
  DiskAttachment:
    Type: ALIYUN::ECS::DiskAttachment
    Properties:
      InstanceId:
        Ref: InstanceId
      Device: /dev/xvda
      DiskId:
        Ref: DiskId
Outputs:
  Status:
    Description: The disk status now.
    Value:
      Fn::GetAtt:
        - DiskAttachment
        - Status
  Device:
    Description: The device where the volume is exposed on ecs instance.
    Value:
      Fn::GetAtt:
        - DiskAttachment
        - Device
  DiskId:
    Description: The disk id of created disk
    Value:
      Fn::GetAtt:
        - DiskAttachment
        - DiskId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceId"
```

`},`

```json
    "DiskId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Disk::DiskId"
```

`},`

```json
  "Resources": {
    "DiskAttachment": {
      "Type": "ALIYUN::ECS::DiskAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
```

`},`

```json
        "Device": "/dev/xvda",
        "DiskId": {
          "Ref": "DiskId"
```

`},`

```json
  "Outputs": {
    "Status": {
      "Description": "The disk status now.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Status"
```

`]` `},`

```json
    "Device": {
      "Description": "The device where the volume is exposed on ecs instance.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Device"
```

`]` `},`

```json
    "DiskId": {
      "Description": "The disk id of created disk",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "DiskId"
```

`]`

#### ALIYUN::ECS::ForwardEntry

ALIYUN::ECS::ForwardEntry is used to configure the Destination Network Address Translation (DNAT) table of a Network Address Translation (NAT) gateway.

**Syntax**

```json
  "Type": "ALIYUN::ECS::ForwardEntry",
  "Properties": {
    "ExternalIp": String,
    "ExternalPort": String,
    "ForwardTableId": String,
    "InternalIp": String,
    "IpProtocol": String,
    "InternalPort": String,
    "PortBreak": Boolean,
    "ForwardEntryName": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ExternalIp | String | Yes | No | The public IP address. | The value of the ExternalIp property must be an IP address that is included in the shared service plan of the NAT gateway to which the DNAT table belongs. |
| ExternalPort | String | Yes | No | The public port number. | Valid values: 1 to 65535. |
| ForwardTableId | String | Yes | No | The ID of the DNAT table. | None |
| InternalIp | String | Yes | No | The destination IP address to which you want to forward the request. | The value of the InternalIp property must be a private IP address. |
| IpProtocol | String | Yes | No | The protocol type. | Valid values: TCP UDP Any |
| InternalPort | String | Yes | No | The port number of the private network. | Valid values: 1 to 65535. |

| PortBreak | Boolean | No | No | Specifies whether to remove limits on the port range. | Default value: false. Valid values: true: removes limits on the port range. false: does not remove limits on the port range. Note If an SNAT entry and a DNAT entry use the same public IP address and you want to specify a port number that is greater than 1024, set the Portbreak property to true. |
|---|---|---|---|---|---|
| ForwardEntryNa me | String | No | No | The name of the DNAT entry. | The name must be 2 to 128 characters in length and must start with a letter. The name cannot start with http:// or https:// . |

**Return values**

Fn::GetAtt ForwardEntryId: the ID of each entry in the DNAT table.

**Examples**

`YAML` format

```
Parameters:
  ForwardTableId:
    Type: String
    Description: Create forward entry in specified forward table.
ROSTemplateFormatVersion: '2015-09-01' Outputs:
  ForwardEntryId:
    Description: The id of created forward entry.
    Value:
      Fn::GetAtt:
        - ForwardTableEntry
        - ForwardEntryId
Resources:
  ForwardTableEntry:
    Type: ALIYUN::ECS::ForwardEntry
    Properties:
      IpProtocol: TCP
      ExternalIp: 100.100.100.1
      ForwardTableId:
        Ref: ForwardTableId
      ExternalPort: '22'
      InternalPort: '22'
      InternalIp: 192.168.1.1
```

`JSON` format

```json
  "Parameters": {
    "ForwardTableId": {
      "Type": "String",
      "Description": "Create forward entry in specified forward table."
```

`},`

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Outputs": {
    "ForwardEntryId": {
      "Description": "The id of created forward entry.",
      "Value": {
        "Fn::GetAtt": [
          "ForwardTableEntry",
          "ForwardEntryId"
```

`]` `},`

```json
  "Resources": {
    "ForwardTableEntry": {
      "Type": "ALIYUN::ECS::ForwardEntry",
      "Properties": {
        "IpProtocol": "TCP",
        "ExternalIp": "100.100.100.1",
        "ForwardTableId": {
          "Ref": "ForwardTableId"
```

`},`

```json
        "ExternalPort": "22",
        "InternalPort": "22",
        "InternalIp": "192.168.1.1"
```

#### ALIYUN::ECS::Instance

ALIYUN::ECS::Instance is used to create an ECS instance.

**Statement**

```json
  "Type": "ALIYUN::ECS::Instance",
  "Properties": {
    "RamRoleName": String,
    "IoOptimized": String,
    "PrivateIpAddress": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "Description": String,
    "Tags": List,
    "HostName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "Password": String,
    "InstanceType": String,
    "SystemDiskCategory": String,
    "UserData": String,
    "SystemDiskSize": Number,
    "ZoneId": String,
    "VpcId": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String,
    "DiskMappings": List,
    "StorageSetId": String,
    "StorageSetPartitionNumber": Integer
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |

| ImageId | String | No | Yes | The ID of the image used to start the ECS instance. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | When editing a template, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (*) to represent part of an image ID. Take all Ubuntu public images provided by Alibaba Cloud as an example. You can use one of the following methods to specify the public image ID for the ECS instance: If you enter ubuntu, the system matches it with the following ID: ubuntu16 0402 64 20G aliba _ _ _ _ se 20170818.vhd _ If you enter ubuntu 14, the _ system matches it with the following ID: ubuntu 14 0405 64 20G alib _ _ _ _ _ ase 20170824.vhd _ If you enter ubuntu*14*32, the system matches it with the following ID: ubuntu 14 0405 32 40G alib _ _ _ _ _ ase 20170711.vhd _ If you enter ubuntu 16 0402 32, the _ _ _ system matches it with the following ID: ubuntu 16 0402 32 40G alib _ _ _ _ _ ase 20170711.vhd _ |
|---|---|---|---|---|---|
| InstanceType | String | No | No | The type of the ECS instance. | None |
| SecurityGroupId | String | No | No | The ID of the security group to which the created instance will belong. | None |
| Description | String | Yes | Released | The description of created instances. | The description can be up to 256 characters in length. |
| InstanceName | String | Yes | Released | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and _ hyphens (-). |

| Password | String | Yes | Released | The password used to log on to the ECS instance. | The characters in length is 8 to 30. And must contain at least one of the following character types: uppercase letters, lowercase letters, digits, and special character. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ‘ < > , . ? / - / - If you specify the Password parameter in the API request, use HTTPS to secure the API and protect your password. |
|---|---|---|---|---|---|
| HostName | String | Yes | Released | The hostname of the instance. | The password must be at least 2 characters in length. It cannot And hyphens (-) cannot start or end the hostname and cannot be used consecutively. On Windows, the hostname can be up to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot contain periods (.) and cannot be composed of only digits. On other OSs such as Linux, the hostname can contain a maximum of 30 characters, including periods (.), each segment can contain uppercase or lowercase letters, digits, and hyphens (-). |
| PrivateIpAddress | String | Yes | Released | The private IP address of an ECS instance in a VPC. The specified IP address must not be used by other instances in the VPC. | None |
| InternetMaxBand widthIn | String | Optional | Released | The maximum inbound bandwidth from the Internet. | Valid values: 1 to 100. Default value: 100. Unit: Mbit/s. |
| IoOptimized | String | Yes | Released | Specifies whether an I/O optimized instance is created. | Valid values: none (non-I/O optimized) optimized Default value: none. |
| DiskMappings | List | Erased | Released | The data disks to be attached to the instance. | A maximum of 16 disks can be attached to each instance. |

| SystemDiskCateg ory |   | String | Yes | Released |   | The type of the system disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ |   |
|---|---|---|---|---|---|---|---|---|
| SystemDiskDescri ption |   | String | Yes | Released |   | The description of the ECS instance system disk. | None |   |
| SystemDiskDiskN ame |   | String | Yes | Released |   | The name of the ECS instance system disk. | None |   |
| SystemDiskSize |   | Number | No. | True |   | The size of the system disk. Unit: GB. | Valid values: 40 to 500. If a custom image is used to create a system disk, make sure that the size of the system disk is greater than that of the custom image. |   |
| Tags |   | List | Erased | Released |   | The custom tags | A maximum of 20 tags are supported. The format is as follows: [{&ldquo;Key”:”tagKey”,”Val |   |
|   |   |   |   |   |   |   |   | [{&ldquo;Key”:”tagKey”,”Val |
|   |   |   |   |   |   | of the instance. | ue”:”tagValue”}, |   |
|   |   |   |   |   |   |   | {&ldquo;Key”:”tagKey2”,”Valu |   |
|   |   |   |   |   |   |   | e”:”tagValue2”}] |   |
| UserData |   | String | Yes | Released |   | The user data that you provide when you create ECS instances. | The user data can be up to 16KB in size. You do not need to use Base64. you must use special characters. \ Escape. |   |
| ZoneId |   | String | Yes | Released |   | The ID of the zone where the instance resides. | None |   |
| HpcClusterId |   | String | Yes | Released |   | The ID of the HPC cluster to which the ECS instance belongs. | None |   |
| VpcId |   | String | Yes | Released |   | The ID of the VPC to which the ECS instance belongs. | None |   |
| VSwitchId |   | String | Yes | Released |   | The ID of the VSwitch for the ECS instance. | None |   |

| KeyPairName | String | Yes | Released | The name of the key pair that is used to connect to created ECS instances. | For Windows-based instances, this parameter is empty by default. In the Linux, if this parameter is specified, the Password content is still set to the instance, but the Password logon method is disabled by default. The key pair is used to verify the logon. |
|---|---|---|---|---|---|
| RamRoleName | String | Yes | Released | The RAM role name of the instance. You can call the ListRoles operation to query the role name. | None |
| DeletionProtectio n | Boolean | Erased | Released | The release protection property of created instances. It specifies whether the instances can be released from the ECS console or through the DeleteInstance operation. | Valid values: True False |
| DeploymentSetId | String | Yes | True | Deployment Set ID. | None |
| StorageSetId | String | No | No | The ID of the storage set. | None. |
| StorageSetPartitio nNumber | Integer | No | No | The maximum number of partitions in the storage set. | The value must be greater than or equal to 2. |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
```

`]`

**DiskMappings properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ Default value: cloud. |
| DiskName | String | Yes | Released | The name of data disk N. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (- ). |
| Description | String | Yes | Released | The description of data disk N. | Valid values: 2 to 256. Default value: Null. |
| Device | String | Yes | Released | The device name of the data disk. | If you do not specify this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | None |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |
| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt InstanceId: the ID of the instance. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIp: The private IP address of the instance in a VPC. This parameter takes effect only when the NetworkType parameter is set to VPC. InnerIp: The private IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. PublicIp: the public IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. ZoneId: the zone ID. HostName: the hostname of the instance.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": "m-25l0rc****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [{
            "Key": "tiantt",
            "Value": "ros"
        },{
            "Key": "tiantt1",
            "Value": "ros1"
```

`]` `},`

```json
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
```

`},`

```json
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
```

#### ALIYUN::ECS::InstanceClone

ALIYUN::ECS::InstanceClone is used to clone an ECS instance.

**Statement**

```json
  "Type": "ALIYUN::ECS::InstanceClone",
  "Properties": {
    "DeletionProtection": Boolean,
    "DiskMappings": List,
    "LoadBalancerIdToAttach": String,
    "Description": String,
    "BackendServerWeight": Integer,
    "Tags": List,
    "SecurityGroupId": String,
    "RamRoleName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "SpotPriceLimit": String,
    "InstanceChargeType": String,
    "SourceInstanceId": String,
    "Period": Number,
    "SpotStrategy": String,
    "Password": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "ZoneId": String,
    "KeyPairName": String
```

**Properties**

| Parameter | Type | Require d | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroup Id | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |
| SourceInstance Id | String | No | No | The ID of the ECS instance to be cloned. | The clone operation clones the specified instance, including its instance type, image, bandwidth billing method, bandwidth limit, and network type. If the source ECS instance belongs to multiple security groups, the cloned instance is added only to the first of these security groups. |
| BackendServer Weight | String | Optional | Released | The weight of the ECS instance in the Server Load Balancer instance. | Value range:[0, 100]. Default value: 100. |
| LoadBalancerId ToAttach | String | Yes | Released | The ID of the SLB instance to which the ECS instance is to be attached. | None |
| Description | String | Yes | Released | The description of created instances. | The description can be up to 256 characters in length. |

| ImageId | String | Yes | True | The ID of the image used to start created instances. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | When editing a template, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (*) to represent part of an image ID. Take all Ubuntu public images provided by Alibaba Cloud as an example. You can use one of the following methods to specify the public image ID for the ECS instance: If you enter ubuntu, the system matches it with the following ID: ubuntu16 0402 64 20G alibase 2 _ _ _ _ _ 0170818.vhd If you enter ubuntu 14, _ the system matches it with the following ID: ubuntu 14 0405 64 20G alibase _ _ _ _ _ _ 20170824.vhd If you enter ubuntu*14*32, the system matches it with the following ID: ubuntu 14 0405 32 40G alibase _ _ _ _ _ _ 20170711.vhd If you enter ubuntu 16 0402 32, _ _ _ the system matches it with the following ID: ubuntu 16 0402 32 40G alibase _ _ _ _ _ _ 20170711.vhd |
|---|---|---|---|---|---|
| SecurityGroupI d | String | Yes | Released | The ID of the security group to which the created instance will belong. | None |
| InstanceName | String | Yes | Released | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and hyphens (-). _ |
| Password | String | Yes | Released | The password used to log on to the ECS instance. | The password must be 8 to 30 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; < > , . ? / If you specify the password parameter in the API request, use HTTPS to secure the API and protect your password. |
| DiskMappings | List | Erased | Released | The disks to be attached to created instances. | A maximum of 16 disks can be attached to each instance. |

| Tags | List | Erased | Released | The custom tags of the instance. | A maximum of 20 tags can be specified in the [{"Key":"tagKey","Value":"tagValu e" },{ "Key":"tagKey2","Value":"tagValue 2"}]. |
|---|---|---|---|---|---|
| ZoneId | String | Yes | Released | The ID of the zone where the instance resides. | None |
| InstanceCharge Type | String | Yes | Released | The billing method of the new ECS instance. | Valid values: PrePaid and PostPaid. Default value: Postpaid. If you set this parameter to Prepaid, make sure that you have sufficient balance in your account. Otherwise, the instance fails to be created. |
| Period | Number | Erased | Released | The subscription period of the new ECS instance. This parameter is required when the InstanceChargeType parameter is set to PrePaid. This parameter is ignored when the InstanceChargeType parameter is set to PostPaid. | Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. Unit: month. |
| KeyPairName | String | Yes | Released | The name of the key pair that is used to connect to created ECS instances. | For Windows-based instances, this parameter is empty by default. In the Linux, if this parameter is specified, the Password content is still set to the instance, but the Password logon method is disabled by default. The key pair is used to verify the logon. |
| RamRoleName | String | Yes | Released | The RAM role name of the instance. You can call the ListRoles operation to query the role name. | None |
| SpotPriceLimit | String | Yes | Released | The maximum hourly price of the instance. | Parameter SpotStrategy this parameter takes effect only when the value is SpotWithPriceLimit. |
| SpotStrategy | String | Yes | Released | The bidding policy for the pay-as-you-go instance. | This parameter is valid only when the InstanceChargeType parameter is set to PostPaid. Valid values: NoSpot: applies to regular pay-as- you-go instances. SpotWithPriceLimit: applies to preemptible instances with a maximum hourly price. SpotAsPriceGo: applies to pay-as- you-go instances priced at the market price at the time of purchase. Default value: NoSpot. |

| InternetMaxBa ndwidthIn | String | Optional | Released | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. | Valid values: 1 to 200. |
|---|---|---|---|---|---|
| DeletionProtect ion | Boolean | Erased | Released | Specifies whether to enable instance release protection in the console or by calling an API operation. ( DeleteInstance) Release instances. | Valid values: true and false. |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
```

`]`

**DiskMappings properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, and _ ephemeral ssd _ Default value: cloud. |
| DiskName | String | Yes | Released | Disk name. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | Yes | Released | The description of data disk N. | The description must be 2 to 256 characters in length. This parameter is empty by default. |
| Device | String | Yes | Released | The device name of the data disk. | If you do not specify this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | None |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key, which cannot be an empty string. It can be up to 64 characters in length, cannot start with acs: or aliyun, and cannot contain http:// or https://. | None |
| Value | String | Yes | Released | The tag value, which can be an empty string. It can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt InstanceId: the ID of the instance. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIp: The private IP address of the instance in a VPC. This parameter takes effect only when the NetworkType parameter is set to VPC. InnerIp: The private IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. PublicIp: the public IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. ZoneId: the zone ID. HostName: the hostname of the instance.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceClone",
      "Properties": {
        "SourceInstanceId": "i-25zsk****",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "DiskMappings": [
            {"Size": 10, "Category": "cloud"},
            {"Size": 10, "Category": "cloud", "SnapshotId": "s-25wsw****"}
```

`]` `},`

```json
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
```

`},`

```json
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
```

#### ALIYUN::ECS::InstanceGroup

ALIYUN::ECS::InstanceGroup is used to create a group of Elastic Compute Service (ECS) instances.

**Syntax**

```json
  "Type": "ALIYUN::ECS::InstanceGroup",
  "Properties": {
    "SystemDiskAutoSnapshotPolicyId": String,
    "DedicatedHostId": String,
    "LaunchTemplateName": String,
    "RamRoleName": String,
    "IoOptimized": String,
    "PrivateIpAddress": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "Description": String,
    "Tags": List,
    "HostName": String,
    "ImageId": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "EniMappings": List,
    "Password": String,
    "InstanceType": String,
    "MaxAmount": Integer,
    "AutoReleaseTime": String,
    "SystemDiskCategory": String,
    "UserData": String,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "SystemDiskSize": Number,
    "ZoneId": String,
    "VpcId": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "Ipv6AddressCount": Integer,
    "SecurityGroupId": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String,
    "Ipv6Addresses": List,
    "NetworkType": String,
    "DiskMappings": List,
    "SystemDiskPerformanceLevel": String,
    "StorageSetId": String,
    "StorageSetPartitionNumber": Integer,
    "SchedulerOptions": Map
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroup Id | String | No | Yes | The ID of the resource group to which the ECS instances belong. | None. |

| HpcClusterId | String | No | Yes | The ID of the Elastic High Performance Computing (E- HPC) cluster to which the ECS instances belong. | None. |
|---|---|---|---|---|---|
| MaxAmount | Integer | Yes | Yes | The maximum number of ECS instances that can be created at a time. | Valid values: 1 to 100. The value of MaxAmount must be greater than or equal to the value of MinAmount. |
| MinAmount | String | Yes | Yes | The minimum number of ECS instances that can be created at a time. | Valid values: 1 to 100. The value of MinAmount must be less than or equal to the value of MaxAmount. |
| Description | String | No | Yes | The description. | The description can be up to 256 characters in length. |
| InstanceType | String | Yes | Yes | The ECS instance type. | None. |
| ImageId | String | Yes | Yes | The ID of the image that is used to start the ECS instances. You can use a public image, custom image, or Alibaba Cloud Marketplace image. | To specify a public image ID, you can enter a partial image ID instead of the complete image ID. Public image IDs support fuzzy matches. Examples: If you specify Ubuntu, the system matches it with the following image ID: ubuntu 16 0402 64 _ _ _ _ 20G alibase 2017081 _ _ 8.vhd. If you specify ubuntu1432, the system matches it with the following image ID: ubuntu 14 0405 32 _ _ _ _ 40G alibase 2017071 _ _ 1.vhd. |
| SecurityGroupI d | String | No | No | The security group to which the ECS instances belong. | None. |

| InstanceName | String | No |   | No |   |   | The name of the ECS instance. |   | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). The name must be in the name prefix[begin nu _ _ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | name prefix[begin nu _ _ |   |   |
|   |   |   |   |   |   |   |   |   | mber,bits]name suffix _ |   |   |   |
| Password | String | No |   | Yes |   |   | The logon password of the ECS instances. |   | The password must be 8 to 30 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ( ) ` ~ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ( ) ` ~ |   |
|   |   |   |   |   |   |   |   |   | ! @ # $ % ^ & * - |   |   |   |
|   |   |   |   |   |   |   |   |   | + = \| { } [ ] : ; |   |   |   |
|   |   |   |   |   |   |   |   |   | ‘ < > , . ? / |   |   |   |
| HostName | String | No |   | No |   |   | The hostname. |   | The hostname must be at least two characters in length. It cannot start or end with a period (.) or hyphen (-). It cannot contain consecutive periods (.) or consecutive hyphens (-). |   |   |   |
| AutoReleaseTi me | String | No |   | No |   |   | The point in time at which the system automatically releases the ECS instances. |   | Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be within three years from the time at which the ECS instances are created. |   |   |   |
| PrivateIpAddre ss | String | No |   | No |   |   | The private IP address of an ECS instance in a virtual private cloud (VPC). |   | Other instances in the VPC must not use the specified IP address. |   |   |   |

|   |   | yyyy-MM- |   |
|---|---|---|---|
| em | ddTHH:mm:ssZ |   |   |

| DiskMappings | List | No | Yes | The data disks that you want to create for the ECS instances. | None. |
|---|---|---|---|---|---|
| InternetMaxBa ndwidthIn | Integer | No | No | The maximum inbound public bandwidth. | Unit: Mbit/s. Valid values: 1 to 100. Default value: 100. |
| IoOptimized | String | No | No | Specifies whether to create an I/O optimized ECS instance. | Valid values: none: does not create an I/O optimized ECS instance. optimized: creates an I/O optimized ECS instance. Default value: none. |
| SystemDiskCat egory | String | No | Yes | The category of the system disk. | Valid values: cloud: basic disk. cloud efficiency: ultra _ disk. cloud ssd: standard _ SSD. cloud essd: Enterprise _ SSD (ESSD). ephemeral ssd: local _ SSD. |
| SystemDiskDe scription | String | No | Yes | The description of the system disk. | None. |
| SystemDiskDis kName | String | No | Yes | The name of the system disk. | None. |
| SystemDiskSiz e | Number | No | Yes | The size of the system disk. | Valid values: 40 to 500. Unit: GB. If you use a custom image to create a system disk, make sure that the size of the system disk is larger than the size of the custom image. |

| Tags | List |   | No |   | Yes |   | The custom tags that you want to add to | You can add up to 20 tags in the following format: [{"Key":"tagKey","Va |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | [{"Key":"tagKey","Va |
|   |   |   |   |   |   |   | the ECS | lue":"tagValue"}, |   |
|   |   |   |   |   |   |   | instances. | {"Key":"tagKey2","Val |   |
|   |   |   |   |   |   |   |   | ue":"tagValue2"}] |   |
| UserData | String |   | No |   | Yes |   | The user data that you want to specify when you create the ECS instances. | The user data can be up to 16 KB in size. You do not need to convert the data into Base64- encoded strings. If the data contains special characters, you must add the escape character (\) before each special character. |   |
| ZoneId | String |   | No |   | No |   | The ID of the zone. | None. |   |
| VpcId | String |   | No |   | No |   | The ID of the VPC. | None. |   |
| VSwitchId | String |   | No |   | No |   | The ID of the vSwitch. | None. |   |
| KeyPairName | String |   | No |   | Yes |   | The name of the key pair that is used to connect to the ECS instances. | For Windows ECS instances, you can ignore KeyPairName. By default, this property is empty. If you specify KeyPairName, the value of Password is still used for ECS instances. However, password- based logons are disabled for ECS Linux instances. |   |
| RamRoleName | String |   | No |   | Yes |   | The name of the Resource Access Management (RAM) role for the ECS instances. | You can call the ListRoles operation to query the RAM role name. |   |
| DedicatedHostI d | String |   | No |   | No |   | The ID of the dedicated host. | None. |   |
| LaunchTemplat eName | String |   | No |   | Yes |   | The name of the launch template. | None. |   |

| EniMappings | List | No | Yes | The elastic network interfaces (ENIs) that you want to attach to the ECS instances. | You can attach up to one ENI to an instance. |
|---|---|---|---|---|---|
| LaunchTemplat eId | String | No | Yes | The ID of the launch template. | None. |
| LaunchTemplat eVersion | String | No | Yes | The version of the launch template. | If you do not specify a version, the default version is used. |
| NetworkType | String | No | No | The network type of the ECS instances. | Valid values: vpc classic Default value: classic. |
| DeletionProtec tion | Boolean | No | No | The release protection property of the ECS instances. This property specifies whether you can delete the ECS instances by using the ECS console or DeleteInstance operation. | Valid values: true false |
| DeploymentSe tId | String | No | Yes | The ID of the deployment set. | None. |
| StorageSetId | String | No | No | The ID of the storage set. | None. |
| StorageSetPart itionNumber | Integer | No | No | The maximum number of partitions in the storage set. | Valid values: greater than or equal to 2. |
| SchedulerOptio ns | Map | No | No | The scheduling options. | For more information, see the "SchedulerOptions property" section of this topic. |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "PerformanceLevel": String,
    "AutoSnapshotPolicyId": String
```

`]`

**DiskMappings properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | Yes | No | The size of the data disk. | Unit: GB. |
| Category | String | No | No | The category of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ cloud essd _ ephemeral ssd _ The default value for an I/O optimized instance is cloud efficiency. The _ default value for a non- I/O optimized instance is cloud. |
| DiskName | String | No | No | The name of the data disk. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | No | No | The description of the data disk. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| Device | String | No | No | The device name of the data disk that you want to attach to the ECS instance. | The system assigns a device name in alphabetical order from /dev/xvda to /dev/xvdz. |

|   | http:// |
|---|---|
| https:// |   |

| SnapshotId | String | No | No | The ID of the snapshot. | None. |
|---|---|---|---|---|---|
| Encrypted | Boolean | No | No | Specifies whether to encrypt the data disk. | Valid values: true false Default value: false. |
| KMSKeyId | String | No | No | The ID of the Key Management Service (KMS) key that you want to use for the data disk. | None. |
| AutoSnapshotP olicyId | String | No | Yes | The ID of the automatic snapshot policy. | None. |
| PerformanceLe vel | String | No | No | The performance level (PL) of the ESSD that you want to use as the data disk. | PL1 (default): An ESSD can deliver up to 50,000 random read/write IOPS. PL2: An ESSD can deliver up to 100,000 random read/write IOPS. PL3: An ESSD can deliver up to 1,000,000 random read/write IOPS. |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |

| Value | String | No | No | The value of the tag. | The value can be up to 128 characters in length and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
|---|---|---|---|---|---|

**EniMappings syntax**

```json
"EniMappings": [
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
```

`]`

**EniMappings properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupI d | String | Yes | Yes | The ID of the security group to which the ENI belongs. | The security group of the ENI and the security group of the ECS instance must reside in the same VPC. |
| VSwitchId | String | Yes | No | The ID of the vSwitch. | None. |
| Description | String | No | Yes | The description of the ENI. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| NetworkInterfa ceName | String | No | Yes | The name of the ENI. | The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

| PrimaryIpAddr ess | String | No | No | The primary private IP address of the ENI. | The primary IP address must be an idle IP address within the vSwitch CIDR block of the ENI. If you leave this property empty, an idle IP address is assigned from the CIDR block of the vSwitch at random. |
|---|---|---|---|---|---|

**SchedulerOptions syntax**

```json
"SchedulerOptions": [
    "DedicatedHostClusterId": String,
```

`]`

**SchedulerOptions property**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DedicatedHost ClusterId | String | Yes | No | The ID of the dedicated host cluster in which you want to deploy the ECS instance. The system automatically selects a dedicated host from the specified cluster to deploy the instance. |   |

**Return values**

Fn::GetAtt InstanceIds: the IDs of the ECS instances. An instance ID is a GUID that is generated by the system. PrivateIps: the private IP addresses of the ECS instances in the VPC. This property takes effect when NetworkType is set to vpc. The value is a JSON array that can contain up to 100 IP addresses separated by commas (,). Example: ["172.16.XX.XX", "172.16.XX.XX", … "172.16.XX.XX"] . InnerIps: the private IP addresses of the ECS instances in the classic network. This property takes effect when NetworkType is set to classic. The value is a JSON array that can contain up to 100 IP addresses separated by commas (,). Example: ["10.1.XX.XX", "10.1.XX.XX", … "10.1.XX.XX"] . PublicIps: the public IP addresses of the ECS instances in the classic network. This property takes effect when NetworkType is set to classic. The value is a JSON array that can contain up to 100 IP addresses separated by commas (,). Example: ["42.1.XX.XX", "42.1.XX.XX", … "42.1.XX.XX"] . HostNames: the hostnames of the ECS instances. OrderId: the order IDs of the ECS instances. ZoneIds: the IDs of the zones. RelatedOrderIds: the related order IDs of the created ECS instances.

**Example**

```json
  "ROSTemplateFormatVersion":"2015-09-01",
  "Resources":{
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId":"m-25l0r****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "MaxAmount":1,
        "MinAmount":1,
        "Tags": [{
            "Key": "tiantt",
            "Value": "ros"
        },{
            "Key": "tiantt1",
            "Value": "ros1"
```

`]` `},`

```json
  "Outputs": {
    "InstanceIds": {
         "Value":{"get_attr": ["WebServer","InstanceIds"]}
```

`},`

```json
    "PublicIps": {
         "Value":{"get_attr": ["WebServer","PublicIps"]}
```

#### ALIYUN::ECS::InstanceGroupClone

ALIYUN::ECS::InstanceGroupClone is used to clone an ECS instance group.

**Statement**

```json
  "Type": "ALIYUN::ECS::InstanceGroupClone",
  "Properties": {
    "BackendServerWeight": Integer,
    "DiskMappings": List,
    "LaunchTemplateName": String,
    "SpotPriceLimit": String,
    "ResourceGroupId": String,
    "KeyPairName": String,
    "SystemDiskDiskName": String,
    "PeriodUnit": String,
    "Description": String,
    "Tags": List,
    "ImageId": String,
    "SpotStrategy": String,
    "SourceInstanceId": String,
    "EniMappings": List,
    "Password": String,
    "MaxAmount": Integer,
    "AutoReleaseTime": String,
    "SystemDiskCategory": String,
    "LoadBalancerIdToAttach": String,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "ZoneId": String,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "DeletionProtection": Boolean,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "RamRoleName": String,
    "HpcClusterId": String,
    "SystemDiskDescription": String
```

**Properties**

| Parameter | Type | Req uir ed | Edi tab le | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Rel eas ed | The ID of the enterprise resource group to which a created instance belongs. | None |
| HpcClusterId | String | Yes | Tru e | The ID of the E-HPC cluster to which a created instance belongs. | None |
| SourceInstanceI d | String | No | No | The ID of the ECS instance to be cloned. | The clone operation clones the specified instance, including its instance type, image, bandwidth limit, and network type. If the source ECS instance belongs to multiple security groups, the cloned instance is added only to the first of these security groups. |
| MaxAmount | Integer | Ret aine d | Yes | The maximum number of ECS instances to be created. | Valid values: 1 to 100. The MaxAmount parameter must be set to a value greater than or equal to the value of the MinAmount parameter. |

| MinAmount | String | No | Yes | The minimum number of ECS instances to be created. | Valid values: 1 to 100. The MinAmount parameter must be set to a value less than or equal to the value of the MaxAmount parameter. |
|---|---|---|---|---|---|
| BackendServer Weight | String | Opti onal | Rel eas ed | The weight assigned to the ECS instance in the Server Load Balancer instance. | Valid values: 0 to 100. Default value: 100. |
| LoadBalancerIdT oAttach | String | Yes | Rel eas ed | The ID of the SLB instance to which the ECS instance is to be attached. | None |
| Description | String | Yes | Rel eas ed | The description of created instances. | The description can be up to 256 characters in length. |
| ImageId | String | Yes | Tru e | The ID of the image used to start created instances. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | You can specify a partial public image ID instead of providing the complete ID. When editing a template used to deploy an ECS instance, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (\*) to represent part of an image ID. You can use one of the following methods to specify the public image ID for the ECS instance: If you set the parameter to ubuntu, ubuntu 16 0402 64 20G alibase 20170818 _ _ _ _ _ _ .vhd. If this parameter is set to ubuntu 14, _ ubuntu 14 0405 64 20G alibase 20170824 _ _ _ _ _ _ .vhd is returned. Specify: ubuntu1432, which will eventually match: ubuntu 14 0405 32 40G alibase 20170711 _ _ _ _ _ _ .vhd Specify: ubuntu 16 0402 32, which will _ _ _ eventually match: ubuntu 16 0402 32 40G alibase 20170711 _ _ _ _ _ _ .vhd |
| SecurityGroupId | String | Yes | Rel eas ed | The ID of the security group to which created instances belong. | None |
| InstanceName | String | Yes | Rel eas ed | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and hyphens (-). _ |
| Password | String | Yes | Rel eas ed | The password used to log on to the ECS instance. | The password The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special character. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / If the Password parameter is specified, you must use HTTPS to call the operation to ensure that the Password remains confidential. |
| DiskMappings | List | Eras ed | Rel eas ed | The data disks to be attached to the instance. | A maximum of 16 disks can be attached to each instance. |

|   | Tags | List |   | Eras | Rel eas | The custom tags of | You can specify a maximum of 20 tags. The format is as follows: [{"Key":"tagKey","Value":"tagValue"}, {"Key":"tagKey2","Value":"tagValue2"}] . |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | [{"Key":"tagKey","Value":"tagValue"}, |
|   |   |   |   | ed | ed | the instance. | {"Key":"tagKey2","Value":"tagValue2"}] |   |
|   | ZoneId | String |   | Yes | Rel eas ed | The ID of the zone where the instance resides. | None |   |
|   | KeyPairName | String |   | Yes | Rel eas ed | The name of the key pair that is used to connect to the ECS instance. For Windows-based ECS instances, this parameter is ignored. Default value: empty. For Linux-based instances, the Password parameter still takes effect if this parameter is specified. However, logon by Password is disabled, and the KeyPairName value is used. | None |   |
|   | RamRoleName | String |   | Yes | Rel eas ed | The RAM role name of the instance. | You can use RAM API ListRoles you can call this operation to query the RAM role name of an instance. |   |
|   | SpotPriceLimit | String |   | Yes | Rel eas ed | The maximum hourly price of the instance. | This parameter supports up to three decimal places. Parameter SpotStrategy this parameter takes effect only when the value is SpotWithPriceLimit. |   |
|   | SystemDiskDisk Name | String |   | Yes | Tru e | The name of the system disk of created instances. | The name must be 2 to 128 characters in length Must start with an uppercase or lowercase letter, and cannot start with http:// or https:// and can contain digits, colons (:), underscores ( ), and hyphens _ (-). |   |
|   | PeriodUnit | String |   | Yes | Tru e | The billing cycle for created ECS instances. | Valid values: Week. 1, 2, 3, and 4} when the value of the PeriodUnit parameter is Week. AutoRenewPeriod values are 1, 2, "3"}. Month 1, 2, 3, 4, 5, 6, and 7 when the PeriodUnit parameter is set to Month "8", "9", "12", "24", "36", "48", "60"},AutoRenewPeriod can be {"1", "2", "3", "6", "12"}. Default value: Month. |   |
|   | EniMappings | List |   | No. | Tru e | The elastic network interfaces (ENIs) to be attached to a created instance. | Only a single ENI can be attached to each instance. |   |

| AutoReleaseTim e | String | Yes | Rel eas ed | The time scheduled for a created ECS instance to be automatically released. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mmZ format. in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. If the value of seconds (ss) is a value other than 00, the start time is automatically rounded down to the nearest minute based on the value of mm. The minimum release time must be at least 30 minutes later than the current time. The maximum release time must be at most three years from the current time. If you do not specify the AutoReleaseTime it indicates that the auto release feature is disabled and the ECS instance will not be automatically released. | None |
|---|---|---|---|---|---|
| SystemDiskCate gory | String | Yes | Tru e | The type of the system disk. | Valid values: cloud: basic disk cloud efficiency: indicates an ultra disk. _ cloud ssd: indicates a standard SSD. _ ephemeral ssd: local SSD. _ cloud essd: indicates an enhanced SSD _ (ESSD). ESSDs are still in public preview and only available in some regions. For phased-out instance types that are not I/O optimized, the default value is cloud. For other instances, the default value is cloud efficiency. _ |
| LaunchTemplate Name | String | Yes | Tru e | The name of the launch template. | None |
| LaunchTemplate Version | String | Yes | Tru e | The version of the launch template. If you do not specify this parameter, the default version is used. | None |
| InternetMaxBan dwidthIn | String | Opti onal | Rel eas ed | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. | Valid values: 1 to 200. Default value: 200. |

| LaunchTemplate Id | String | Yes | Tru e | The ID of the launch template. | None |
|---|---|---|---|---|---|
| SystemDiskDesc ription | String | Yes | Tru e | The description of the system disk. | The description must be 2 to 256 characters in length and cannot start with http:// or https://. This parameter is empty by default. |
| DeletionProtecti on | Boolea n | Eras ed | Rel eas ed | The release protection attribute of the instance. Specifies whether the ECS console or API DeleteInstance) to release the instance. | Valid values: true false |
| DeploymentSetI d | String | Yes | Tru e | Deployment Set ID. | None |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
```

`]`

**DiskMappings properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Encrypted | String | Yes | Released | Specifies whether to encrypt the data disk. | Valid values: true false Default value :false |
| KMSKeyId | String | Yes | Released | The KMS key ID for data disk N. | None |
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssdDefault _ |
| DiskName | String | Yes | Released | The name of data disk N. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | Yes | Released | The description of data disk N. | Valid values: 2 to 256. Default value: Null. |

| Device | String | Yes | Released | The device name of the data disk attached to an ECS instance. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
|---|---|---|---|---|---|
| SnapshotId | String | Yes | Released | Create a data disk by using a snapshot. | None |

**EniMappings syntax**

```json
"EniMappings": [
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
```

`]`

**EniMappings properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | No | Yes | The ID of the security group to which the ENI belongs. | None |
| VSwitchId | String | No | No | The ID of the VSwitch to which the ENI belongs. | None |
| Description | String | Yes | True | The description of the ENI. | It can contain 2 to 256 English letters or Chinese character. It cannot start with http:// and https:// the beginning. |
| NetworkInterface Name | String | Yes | True | The name of the ENI. | None |
| PrimaryIpAddress | String | Yes | Released | The primary IP address of the ENI. | None |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |

| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |
|---|---|---|---|---|---|

**Response parameters**

Fn::GetAtt InstanceIds: the IDs of instances in the ECS instance group. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIps: the private IP addresses of VPC-type instances. This parameter is valid only when the NetworkType parameter is set to VPC. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["172.16.XX.XX", "172.16.XX.XX", ... "172.16.XX.XX"]. InnerIps: the private IP addresses of instances in the classic network. This parameter is valid only when the NetworkType parameter is set to Classic. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["10.1.XX.XX", "10.1.XX.XX", ... "10.1.XX.XX"]. PublicIps: the public IP addresses of instances in the classic network. This parameter is applicable only when the NetworkType parameter is set is Classic. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["42.1.XX.XX", "42.1.XX.XX", ... "42.1.XX.XX"]. HostNames: the hostnames of all instances. The parameter value is a JSON-formatted array. Example: ["host1", "host2", ... "host3"]. OrderId: the order IDs of all instances. ZoneIds: the IDs of the zones where created instances reside.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroupClone",
      "Properties": {
        "SourceInstanceId": "i-25zsk****",
        "ImageId": "m-25l0r****",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "MaxAmount": 1,
        "MinAmount": 1
```

`},`

```json
  "Outputs": {
    "InstanceIds": {
      "Value": {"get_attr": ["WebServer","InstanceIds"]}
```

`},`

```json
    "PublicIps": {
      "Value": {"get_attr": ["WebServer","PublicIps"]}
```

#### ALIYUN::ECS::Invocation

ALIYUN::ECS::Invocation is used to invoke a Cloud Assistant command for one or more ECS instances.

**Statement**

```json
  "Type": "ALIYUN::ECS::Invocation",
  "Properties": {
    "Timed": Boolean,
    "Frequency": String,
    "CommandId": String,
    "InstanceIds": List
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Timed | Boolean | Erased | Released | Specifies whether to invoke the command on a periodic basis. Default value: false. | None |
| Frequency | String | Yes | Released | The frequency at which the command is invoked. | None |
| CommandId | String | No | No | The ID of the script. | None |
| InstanceIds | List | Yes | No | The IDs of the instances for which you want to invoke the command. A maximum of 20 instance IDs can be specified. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt The execution ID of the InvokeId: command.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Timed": {
      "Type": "Boolean",
      "Description": "Whether it is timed execution. Default is False.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]` `},`

```json
    "Frequency": {
      "Type": "String",
      "Description": "The frequency of timing execution (the shortest frequency is performed every 1
```

```
minute). It is mandatory when Timing is True.The value rule follows the rules of the cron expression.
```

`"` `},`

```json
    "CommandId": {
      "Type": "String",
      "Description": "The id of command."
```

`},`

```json
    "InstanceIds": {
      "Type": "CommaDelimitedList",
      "Description": "The instance id list. Select up to 20 instances at a time.Instances selected ne
twork type must be VPC network, status must be running"
```

`},`

```json
  "Resources": {
    "Invocation": {
      "Type": "ALIYUN::ECS::Invocation",
      "Properties": {
        "Timed": {
          "Ref": "Timed"
```

`},`

```json
        "Frequency": {
          "Ref": "Frequency"
```

`},`

```json
        "CommandId": {
          "Ref": "CommandId"
```

`},`

```json
        "InstanceIds": {
          "Fn::Split": [
            ",",
              "Ref": "InstanceIds"
```

`},`

```json
              "Ref": "InstanceIds"
```

`]` `},`

```json
  "Outputs": {
    "InvokeId": {
      "Description": "The id of command execution.",
      "Value": {
        "Fn::GetAtt": [
          "Invocation",
          "InvokeId"
```

`]`

#### ALIYUN::ECS::JoinSecurityGroup

ALIYUN::ECS::JoinSecurityGroup is used to add one or more ECS instances to a specified security group.

**Syntax**

```json
  "Type": "ALIYUN::ECS::JoinSecurityGroup",
  "Properties": {
    "InstanceId": String,
    "InstanceIdList": List,
    "SecurityGroupId": String,
    "NetworkInterfaceList": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | Yes | No | The ID of the security group. | None |
| InstanceId | String | No | No | The ID of the ECS instance to be added to the security group. | None |
| InstanceIdList | List | No | Yes | The IDs of the ECS instances to be added to the security group. | None |
| NetworkInterfac eList | List | No | Yes | The IDs of the elastic network interfaces (ENIs). | None |

**Response parameters**

Fn::GetAtt None

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  SG:
    Type: ALIYUN::ECS::JoinSecurityGroup
    Properties:
      SecurityGroupId: sg-m5eagh7rzys2z8sa****
      InstanceIdList:
      - i-m5e505h9bgsio0wy****
      - i-m5e505hio0wyjc6r****
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::JoinSecurityGroup",
      "Properties": {
        "SecurityGroupId": "sg-m5eagh7rzys2z8sa****",
        "InstanceIdList": [
          "i-m5e505h9bgsio0wy****",
          "i-m5e505hio0wyjc6r****"
```

`]`

#### ALIYUN::ECS::LaunchTemplate

ALIYUN::ECS::LaunchTemplate is used to create a launch template for an Elastic Compute Service (ECS) instance.

**Syntax**

```json
  "Type": "ALIYUN::ECS::LaunchTemplate",
  "Properties": {
    "LaunchTemplateName": String,
    "VersionDescription": String,
    "ImageId": String,
    "InstanceType": String,
    "SecurityGroupId": String,
    "NetworkType": String,
    "VSwitchId": String,
    "InstanceName": String,
    "Description": String,
    "InternetMaxBandwidthOut": Integer,
    "HostName": String,
    "ZoneId": String,
    "SystemDiskCategory": String,
    "SystemDiskSize": Number,
    "SystemDiskDiskName": String,
    "SystemDiskDescription": String,
    "IoOptimized": String,
    "InternetChargeType": String,
    "UserData": String,
    "KeyPairName": String,
    "RamRoleName": String,
    "AutoReleaseTime": String,
    "SpotStrategy": String,
    "SpotPriceLimit": String,
    "SecurityEnhancementStrategy": String,
    "DiskMappings": List,
    "NetworkInterfaces": List,
    "Tags": List,
    "TemplateTags": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LaunchTempl ateName | String | Yes | No | The name of the launch template. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons(:), underscores ( ), and hyphens _ (-). The name must start with a letter but cannot start with http:// or https:// . |
| VersionDescri ption | String | No | No | The description of the launch template version. | The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| ImageId | String | No | No | The ID of the image. | None. |
| InstanceType | String | No | No | The type of the instance. | None. |
| SecurityGrou pId | String | No | No | The ID of the security group. | None. |
| NetworkType | String | No | No | The network type of the instance. | Valid values: classic: classic network vpc: virtual private cloud (VPC) |
| VSwitchId | String | No | No | The ID of the vSwitch. This property is required when you create an instance of the VPC type. | None. |
| InstanceNam e | String | No | No | The name of the instance. | The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | No | The description of the instance. | The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| InternetMaxB andwidthOut | Integer | No | No | The maximum outbound public bandwidth. | Valid values: 0 to 100. Unit: Mbit/s. |

| HostName | String | No | No | The hostname of the instance. | The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). The hostname must meet the following requirements: Windows instances: The hostname must be 2 to 15 characters in length, and can contain letters, digits, and hyphens (-). The hostname cannot contain only digits. Other instances such as Linux instances: The hostname must be 2 to 64 characters in length, and can contain letters, digits, and hyphens (-). |
|---|---|---|---|---|---|
| ZoneId | String | No | No | The ID of the zone in which the instance is deployed. | None. |
| SystemDiskC ategory | String | No | No | The category of the system disk. | Valid values: cloud: basic disk cloud efficiency: ultra disk. _ cloud ssd: SSD _ ephemeral ssd: local SSD _ |
| SystemDiskSi ze | Number | No | No | The size of the system disk. | Valid values: 20 to 500. Unit: GB. |
| SystemDiskDi skName | String | No | No | The name of the system disk. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| SystemDiskD escription | String | No | No | The description of the system disk. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
| IoOptimized | String | No | No | Specifies whether the instance is an I/O optimized instance. | Valid values: none: a non-I/O optimized instance optimized: an I/O optimized instance |
| InternetCharg eType | String | No | No | The metering method for network usage. | Valid values: PayByBandwidth: pay-by- bandwidth PayByTraffic: pay-by-data- transfer |
| UserData | String | No | No | The user data of the instance. | The user data must be encoded in Base64. The raw data can be up to 16 KB in size. |

|   | http:// |
|---|---|
| https:// |   |

| KeyPairName | String | No | No | The name of the key pair. | The name must meet the following requirements: Windows instances: You can ignore this property. By default, this property is empty. The Password property takes effect even if you specify the KeyPairName property. Linux instances: By default, password-based logon is disabled. |   |   |
|---|---|---|---|---|---|---|---|
| RamRoleNam e | String | No | No | The name of the RAM role for the instance. | None. |   |   |
| AutoReleaseT ime | String | No | No | The time at which the system automatically releases the instance. | Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |   |   |
|   |   |   |   |   |   | yyyy- |   |
| SpotStrategy | String | No | No | The preemption policy for a pay-as-you- go instance. | This property takes effect when you set the InstanceChargeType property to Postpaid. Valid values: NoSpot: The instance is created as a regular pay-as- you-go instance. SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price. SpotAsPriceGo: The instance is created as a preemptible instance whose price is based on the market price at the time of purchase. The market price can be equal to the price of a pay-as-you-go instance. |   |   |
| SpotPriceLimi t | String | No | No | The maximum hourly price that you specify for the instance. | The value of this property can contain up to three decimal places. |   |   |
| SecurityEnha ncementStrat egy | String | No | No | Specifies whether to enable security hardening. | Valid values: Active: enables security hardening. Deactive: disables security hardening. |   |   |
| DiskMappings | List | No | No | The data disks. | You can specify up to 16 data disks. For more information, see DiskMappings properties. |   |   |

| ally | MM-ddTHH:mm:ssZ |
|---|---|

| NetworkInterf aces | List | No | No | The elastic network interfaces (ENIs). | You can specify up to eight ENIs. For more information, see NetworkInterfaces properties. |
|---|---|---|---|---|---|
| Tags | List | No | No | The tags of the instance, security group, disk, or ENI. | You can specify up to 20 tags. For more information, see Tags properties. |
| TemplateTag s | List | No | No | The tags of the launch template. | You can specify up to 20 tags. For more information, see TemplateTags properties. |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "DeleteWithInstance": String
```

`]`

**DiskMappings properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Category | String | No | No | The category of the data disk. | Valid values: cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: SSD _ ephemeral ssd: local SSD _ |
| DiskName | String | No | No | The name of the data disk. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons(:), underscores ( ), and hyphens _ (-). The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | No | The description of the data disk. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
| SnapshotId | String | No | No | The ID of the snapshot that is used to create the data disk. | None. |

| Size | String | No | No | The size of the system disk. | Valid values: Valid values if you set the Category property to cloud: 5 to 2000 Valid values if you set the Category property to cloud efficiency: 20 to _ 32768 Valid values if you set the Category property to cloud ssd: 20 to 32768 _ Valid values if you set the Category property to ephemeral ssd: 5 to 800 _ Unit: GB. |
|---|---|---|---|---|---|
| Encrypted | Boolean | No | No | Specifies whether to encrypt the data disk. | Valid values: true: encrypts the data disk. false: does not encrypt the data disk. |
| DeleteWithIns tance | Boolean | No | No | Specifies whether the system releases the data disk when the instance is released. | Valid values: true: releases the data disk when the instance is released. false: does not release the data disk when the instance is released. |

**NetworkInterfaces syntax**

```json
"NetworkInterfaces": [
    "PrimaryIpAddress": String,
    "VSwitchId": String,
    "SecurityGroupId": String,
    "NetworkInterfaceName": String,
    "Description": String
```

`]`

**NetworkInterfaces properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PrimaryIpAdd ress | String | No | No | The primary private IP address of the ENI. | None. |
| VSwitchId | String | No | No | The ID of the vSwitch to which the ENI belongs. | None. |
| SecurityGrou pId | String | No | No | The ID of the security group to which the ENI belongs. | None. |
| NetworkInterf aceName | String | No | No | The name of the ENI. | None. |

| Description | String | No | No | The description of the ENI. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
|---|---|---|---|---|---|

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

**TemplateTags syntax**

```json
"TemplateTags": [
    "Value": String,
    "Key": String
```

`]`

**TemplateTags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

**Return values**

Fn::GetAtt LaunchTemplateId: the ID of the launch template. LaunchTemplateName: the name of the launch template. DefaultVersionNumber: the default version number of the launch template. LatestVersionNumber: the latest version number of the launch template.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the instance, [2, 256] characters."
```

`},`

```json
    "DiskMappings": {
      "Type": "Json",
      "Description": "Disk mappings to attach to instance. Max support 16 disks.",
      "MaxLength": 16
```

`},`

```json
    "SystemDiskSize": {
      "Type": "Number",
      "Description": "Disk size of the system disk, range from 20 to 500 GB. If you specify with your
own image, make sure the system disk size bigger than image size. ",
      "MinValue": 20
```

`},`

```json
    "UserData": {
      "Type": "String",
      "Description": "User data to pass to instance. [1, 16KB] characters."
```

`},`

```json
    "SystemDiskDescription": {
      "Type": "String",
      "Description": "Description of created system disk."
```

`},`

```json
    "TemplateTags": {
      "Type": "Json",
      "Description": "Template tags to attach to launch template.",
      "MaxLength": 20
```

`},`

```json
    "RamRoleName": {
      "Type": "String",
      "Description": "Instance RAM role name. The name is provided and maintained by Resource Access
Management (RAM) and can be queried using ListRoles. For more information, see RAM API CreateRole and ListRoles."
```

`},`

```json
    "NetworkType": {
      "Type": "String",
      "Description": "Instance network type. Support 'vpc' and 'classic'",
      "AllowedValues": [
        "vpc",
        "classic"
```

`]` `},`

```json
    "NetworkInterfaces": {
      "Type": "Json",
      "Description": "Elastic network interfaces to be attached to instance.",
      "MaxLength": 8
```

`},`

```json
    "ImageId": {
      "Type": "String",
      "Description": "Image ID to create ecs instance."
```

`},` `},`

```json
    "SystemDiskDiskName": {
      "Type": "String",
      "Description": "Name of created system disk."
```

`},`

```json
    "SpotPriceLimit": {
      "Type": "String",
      "Description": "The hourly price threshold of a instance, and it takes effect only when
parameter InstanceChargeType is PostPaid. Three decimals is allowed at most. "
```

`},`

```json
    "InstanceType": {
      "Type": "String",
      "Description": "Ecs instance supported instance type, make sure it should be correct."
```

`},`

```json
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance, security group, disk and network interface.",
      "MaxLength": 20
```

`},`

```json
    "HostName": {
      "Type": "String",
      "Description": "Host name of created ecs instance. at least 2 characters, and '.' '-' Is not th
e first and last characters as hostname, not continuous use. Windows platform can be up to 15 charact ers, allowing letters (without limiting case), numbers and '-', and does not support the number of po ints, not all is digital ('.').Other (Linux, etc.) platform up to 30 characters, allowing support num ber multiple points for the period between the points, each permit letters (without limiting case), n umbers and '-' components."
```

`},`

```json
    "SpotStrategy": {
      "Type": "String",
      "Description": "The spot strategy of a Pay-As-You-Go instance, and it takes effect only when pa
rameter InstanceChargeType is PostPaid. Value range: \"NoSpot: A regular Pay-As-You-Go instance\", \" SpotWithPriceLimit: A price threshold for a spot instance, \"\"SpotAsPriceGo: A price that is based o n the highest Pay-As-You-Go instance. \"",
      "AllowedValues": [
        "NoSpot",
        "SpotWithPriceLimit",
        "SpotAsPriceGo"
```

`]` `},`

```json
    "KeyPairName": {
      "Type": "String",
      "Description": "SSH key pair name."
```

`},`

```json
    "LaunchTemplateName": {
      "Type": "String",
      "Description": "The name of launch template."
```

`},`

```json
    "IoOptimized": {
      "Type": "String",
      "Description": "The 'optimized' instance can provide better IO performance. Support 'none' and
'optimized' only.",
      "AllowedValues": [
        "none",
        "optimized"
```

`]` `},`

```json
    "VersionDescription": {
      "Type": "String",
      "Description": "Description for version 1 of launch template."
```

`},`

```json
    "ZoneId": {
      "Type": "String",
```

```json
      "Description": "Current zone to create the instance."
```

`},`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The vSwitch Id to create ecs instance."
```

`},`

```json
    "SecurityGroupId": {
      "Type": "String",
      "Description": "Security group to create ecs instance. For classic instance need the security g
roup not belong to VPC, for VPC instance, please make sure the security group belong to specified VPC
```

`."` `},`

```json
    "SystemDiskCategory": {
      "Type": "String",
      "Description": "Category of system disk. support
cloud|cloud_efficiency|cloud_ssd|cloud_essd|ephemeral_ssd",
      "AllowedValues": [
        "cloud",
        "cloud_efficiency",
        "cloud_ssd",
        "cloud_essd",
        "ephemeral_ssd"
```

`]` `},`

```json
    "InternetChargeType": {
      "Type": "String",
      "Description": "Instance internet access charge type.Support 'PayByBandwidth' and
'PayByTraffic' only.",
      "AllowedValues": [
        "PayByBandwidth",
        "PayByTraffic"
```

`]` `},`

```json
    "InstanceName": {
      "Type": "String",
      "Description": "Display name of the instance, [2, 128] English or Chinese characters, must star
t with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
```

`},`

```json
    "InternetMaxBandwidthOut": {
      "Type": "Number",
      "Description": "Max internet out bandwidth in Mbps(Mega bit per second). Range is [0,200].While
the property is not 0, public ip will be assigned for instance.",
      "MinValue": 0,
      "MaxValue": 200
```

`},`

```json
    "SecurityEnhancementStrategy": {
      "Type": "String",
      "Description": "Activate or deactivate security enhancement,Value range: \"Active\" and
\"Deactive\"",
      "AllowedValues": [
        "Active",
        "Deactive"
```

`]` `},`

```json
    "AutoReleaseTime": {
      "Type": "String",
      "Description": "Auto release time for created instance, Follow ISO8601 standard using UTC time.
format is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
```

`},`

```json
  "Resources": {
    "LaunchTemplate": {
"Type":"ALIYUN::ECS::LaunchTemplate"
```

```json
      Type: ALIYUN::ECS::LaunchTemplate,
      "Properties": {
        "Description": {
          "Ref": "Description"
```

`},`

```json
        "DiskMappings": {
          "Ref": "DiskMappings"
```

`},`

```json
        "SystemDiskSize": {
          "Ref": "SystemDiskSize"
```

`},`

```json
        "UserData": {
          "Ref": "UserData"
```

`},`

```json
        "SystemDiskDescription": {
          "Ref": "SystemDiskDescription"
```

`},`

```json
        "TemplateTags": {
          "Ref": "TemplateTags"
```

`},`

```json
        "RamRoleName": {
          "Ref": "RamRoleName"
```

`},`

```json
        "NetworkType": {
          "Ref": "NetworkType"
```

`},`

```json
        "NetworkInterfaces": {
          "Ref": "NetworkInterfaces"
```

`},`

```json
        "ImageId": {
          "Ref": "ImageId"
```

`},`

```json
        "SystemDiskDiskName": {
          "Ref": "SystemDiskDiskName"
```

`},`

```json
        "SpotPriceLimit": {
          "Ref": "SpotPriceLimit"
```

`},`

```json
        "InstanceType": {
          "Ref": "InstanceType"
```

`},`

```json
        "Tags": {
          "Ref": "Tags"
```

`},`

```json
        "HostName": {
          "Ref": "HostName"
```

`},`

```json
        "SpotStrategy": {
          "Ref": "SpotStrategy"
```

`},`

```json
        "KeyPairName": {
          "Ref": "KeyPairName"
```

`},`

```json
        "LaunchTemplateName": {
          "Ref": "LaunchTemplateName"
```

`},`

```json
        "IoOptimized": {
          "Ref": "IoOptimized"
```

`},`

```json
        "VersionDescription": {
          "Ref": "VersionDescription"
```

`},`

```json
        "ZoneId": {
```

```json
          "Ref": "ZoneId"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
```

`},`

```json
        "SystemDiskCategory": {
          "Ref": "SystemDiskCategory"
```

`},`

```json
        "InternetChargeType": {
          "Ref": "InternetChargeType"
```

`},`

```json
        "InstanceName": {
          "Ref": "InstanceName"
```

`},`

```json
        "InternetMaxBandwidthOut": {
          "Ref": "InternetMaxBandwidthOut"
```

`},`

```json
        "SecurityEnhancementStrategy": {
          "Ref": "SecurityEnhancementStrategy"
```

`},`

```json
        "AutoReleaseTime": {
          "Ref": "AutoReleaseTime"
```

`},`

```json
  "Outputs": {
    "LaunchTemplateName": {
      "Description": "The name of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateName"
```

`]` `},`

```json
    "LatestVersionNumber": {
      "Description": "The latest version number of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LatestVersionNumber"
```

`]` `},`

```json
    "LaunchTemplateId": {
      "Description": "The id of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateId"
```

`]` `},`

```json
    "DefaultVersionNumber": {
      "Description": "The default version number of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
"DefaltVersionNmber"
```

```
          "DefaultVersionNumber"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
    Type: String
    Description: 'Description of the instance, [2, 256] characters.'
  DiskMappings:
    Type: Json
    Description: Disk mappings to attach to instance. Max support 16 disks.
    MaxLength: 16
  SystemDiskSize:
    Type: Number
    Description: >-
      Disk size of the system disk, range from 20 to 500 GB. If you specify with
      your own image, make sure the system disk size bigger than image size.
    MinValue: 20
  UserData:
    Type: String
    Description: 'User data to pass to instance. [1, 16KB] characters.'
  SystemDiskDescription:
    Type: String
    Description: Description of created system disk.
  TemplateTags:
    Type: Json
    Description: Template tags to attach to launch template.
    MaxLength: 20
  RamRoleName:
    Type: String
    Description: >-
      Instance RAM role name. The name is provided and maintained by Resource
      Access Management (RAM) and can be queried using ListRoles. For more
      information, see RAM API CreateRole and ListRoles.
  NetworkType:
    Type: String
    Description: Instance network type. Support 'vpc' and 'classic'
    AllowedValues:
      - vpc
      - classic
  NetworkInterfaces:
    Type: Json
    Description: Elastic network interfaces to be attached to instance.
    MaxLength: 8
  ImageId:
    Type: String
    Description: Image ID to create ecs instance.
  SystemDiskDiskName:
    Type: String
    Description: Name of created system disk.
  SpotPriceLimit:
    Type: String
    Description: >-
      The hourly price threshold of a instance, and it takes effect only when
      parameter InstanceChargeType is PostPaid. Three decimals is allowed at
      most.
```

`t` `T`

```
  InstanceType:
    Type: String
    Description: 'Ecs instance supported instance type, make sure it should be correct.'
  Tags:
    Type: Json
    Description: 'Tags to attach to instance, security group, disk and network interface.'
    MaxLength: 20
  HostName:
    Type: String
    Description: >-
      Host name of created ecs instance. at least 2 characters, and '.' '-' Is
      not the first and last characters as hostname, not continuous use. Windows
      platform can be up to 15 characters, allowing letters (without limiting
      case), numbers and '-', and does not support the number of points, not all
      is digital ('.').Other (Linux, etc.) platform up to 30 characters,
      allowing support number multiple points for the period between the points,
      each permit letters (without limiting case), numbers and '-' components.
  SpotStrategy:
    Type: String
    Description: >-
      The spot strategy of a Pay-As-You-Go instance, and it takes effect only
      when parameter InstanceChargeType is PostPaid. Value range: "NoSpot: A
      regular Pay-As-You-Go instance", "SpotWithPriceLimit: A price threshold
      for a spot instance, ""SpotAsPriceGo: A price that is based on the highest
      Pay-As-You-Go instance. "
    AllowedValues:
      - NoSpot
      - SpotWithPriceLimit
      - SpotAsPriceGo
  KeyPairName:
    Type: String
    Description: SSH key pair name.
  LaunchTemplateName:
    Type: String
    Description: The name of launch template.
  IoOptimized:
    Type: String
    Description: >-
      The 'optimized' instance can provide better IO performance. Support 'none'
      and 'optimized' only.
    AllowedValues:
      - none
      - optimized
  VersionDescription:
    Type: String
    Description: Description for version 1 of launch template.
  ZoneId:
    Type: String
    Description: Current zone to create the instance.
  VSwitchId:
    Type: String
    Description: The vSwitch Id to create ecs instance.
  SecurityGroupId:
    Type: String
    Description: >-
      Security group to create ecs instance. For classic instance need the
      security group not belong to VPC, for VPC instance, please make sure the
      security group belong to specified VPC.
  SystemDiskCategory:
    Type: String
    Description: >-
      Category of system disk. support
      cloud|cloudefficiency|cloudssd|cloudessd|ephemeralssd
```

`_` `y` `_` `_` `p` `_`

```
    AllowedValues:
      - cloud
      - cloud_efficiency
      - cloud_ssd
      - cloud_essd
      - ephemeral_ssd
  InternetChargeType:
    Type: String
    Description: >-
      Instance internet access charge type.Support 'PayByBandwidth' and
      'PayByTraffic' only.
    AllowedValues:
      - PayByBandwidth
      - PayByTraffic
  InstanceName:
    Type: String
    Description: >-
      Display name of the instance, [2, 128] English or Chinese characters, must
      start with a letter or Chinese in size, can contain numbers, '_' or '.',
      '-'
  InternetMaxBandwidthOut:
    Type: Number
    Description: >-
      Max internet out bandwidth in Mbps(Mega bit per second). Range is
      [0,200].While the property is not 0, public ip will be assigned for
      instance.
    MinValue: 0
    MaxValue: 200
  SecurityEnhancementStrategy:
    Type: String
    Description: >-
      Activate or deactivate security enhancement,Value range: "Active" and
      "Deactive"
    AllowedValues:
      - Active
      - Deactive
  AutoReleaseTime:
    Type: String
    Description: >-
      Auto release time for created instance, Follow ISO8601 standard using UTC
      time. format is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this
      day onwards
Resources:
  LaunchTemplate:
    Type: 'ALIYUN::ECS::LaunchTemplate'
    Properties:
      Description:
        Ref: Description
      DiskMappings:
        Ref: DiskMappings
      SystemDiskSize:
        Ref: SystemDiskSize
      UserData:
        Ref: UserData
      SystemDiskDescription:
        Ref: SystemDiskDescription
      TemplateTags:
        Ref: TemplateTags
      RamRoleName:
        Ref: RamRoleName
      NetworkType:
        Ref: NetworkType
```

```
      NetworkInterfaces:
        Ref: NetworkInterfaces
      ImageId:
        Ref: ImageId
      SystemDiskDiskName:
        Ref: SystemDiskDiskName
      SpotPriceLimit:
        Ref: SpotPriceLimit
      InstanceType:
        Ref: InstanceType
      Tags:
        Ref: Tags
      HostName:
        Ref: HostName
      SpotStrategy:
        Ref: SpotStrategy
      KeyPairName:
        Ref: KeyPairName
      LaunchTemplateName:
        Ref: LaunchTemplateName
      IoOptimized:
        Ref: IoOptimized
      VersionDescription:
        Ref: VersionDescription
      ZoneId:
        Ref: ZoneId
      VSwitchId:
        Ref: VSwitchId
      SecurityGroupId:
        Ref: SecurityGroupId
      SystemDiskCategory:
        Ref: SystemDiskCategory
      InternetChargeType:
        Ref: InternetChargeType
      InstanceName:
        Ref: InstanceName
      InternetMaxBandwidthOut:
        Ref: InternetMaxBandwidthOut
      SecurityEnhancementStrategy:
        Ref: SecurityEnhancementStrategy
      AutoReleaseTime:
        Ref: AutoReleaseTime
Outputs:
  LaunchTemplateName:
    Description: The name of launch template.
    Value:
      'Fn::GetAtt':
        - LaunchTemplate
        - LaunchTemplateName
  LatestVersionNumber:
    Description: The latest version number of launch template.
    Value:
      'Fn::GetAtt':
        - LaunchTemplate
        - LatestVersionNumber
  LaunchTemplateId:
    Description: The id of launch template.
    Value:
      'Fn::GetAtt':
        - LaunchTemplate
        - LaunchTemplateId
  DefaultVersionNumber:
Description:Thedefaultversionnumberoflaunchtemplate.
```

```
    Description: The default version number of launch template.
    Value:
      'Fn::GetAtt':
        - LaunchTemplate
        - DefaultVersionNumber
```

To view more examples, visit LaunchTemplate.json and LaunchTemplate.yml. In the examples, the ALIYUN::ECS::LaunchTemplate and ALIYUN::ECS::AutoProvisioningGroup resource types are used.

#### ALIYUN::ECS::NatGateway

ALIYUN::ECS::NatGateway is used to create a NAT gateway in a virtual private cloud (VPC).

**Syntax**

```json
  "Type": "ALIYUN::ECS::NatGateway",
  "Properties": {
    "DeletionProtection": Boolean,
    "VpcId": String,
    "Description": String,
    "NatGatewayName": String,
    "NatType": String,
    "Duration": Number,
    "AutoPay": Boolean,
    "InstanceChargeType": String,
    "PricingCycle": String,
    "VSwitchId": String,
    "DeletionForce": Boolean,
    "Spec": String,
    "Tags": List,
    "EipBindMode": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VpcId | String | Yes | No | The ID of the VPC in which you want to create the NAT gateway. | None. |
| VSwitchId | String | No | No | The ID of the vSwitch in the VPC. | None. |
| Description | String | No | No | The description of the NAT gateway. | The description must be 2 to 256 characters in length. |

| NatGatewayNam e | String | No | No | The name of the NAT gateway. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). It must start with a letter. |
|---|---|---|---|---|---|
| NatType | String | No | No | The type of the NAT gateway. | Valid values: Normal: standard NAT gateway. Enhanced: enhanced NAT gateway. |
| Duration | Number | No | No | The subscription duration. | Valid values: Valid values when PricingCycle is set to Month: 1 to 9. Valid values when PricingCycle is set to Year: 1 to 3. Note This property must be specified when InstanceCh argeType is set to PrePaid. |

| AutoPay | Boolean | No | No | Specifies whether to enable automatic payment. | Valid values: false: does not enable automatic payment. After an order is generated, you must go to the order center to complete the payment. true: enables automatic payment. After an order is generated, the system automatically deducts the payment from your account balance to complete the payment. Note This property must be specified when InstanceCh argeType is set to PrePaid. |
|---|---|---|---|---|---|
| InstanceChargeT ype | String | No | No | The billing method. | Valid values: PostPaid (default): pay- as-you-go. PrePaid: subscription. |
| PricingCycle | String | No | No | The unit of the subscription duration. | Valid values: Month (default) Year Note This property must be specified when InstanceCh argeType is set to PrePaid. |

| Spec | String | No | No | The size of the Internet NAT gateway. | Valid values: Small (default): Small. Middle: Medium. Large: Large. XLarge.1: Super Large- 1. |
|---|---|---|---|---|---|
| DeletionProtecti on | Boolean | No | No | Specifies whether to enable deletion protection. | Valid values: true false (default) |
| DeletionForce | Boolean | No | No | Specifies whether to forcefully delete SNAT and DNAT entries and disassociate the elastic IP address (EIP) from the NAT gateway. | Valid values: true false (default) |
| Tags | List | No | No | The tags. | You can add up to 20 tags. For more information, see Tags properties. |
| EipBindMode | String | No | No | The mode in which you want to associate the NAT gateway with an EIP. | Valid values: MULTI BINDE _ D (default): Multi-EIP-to- ENI mode. NAT: NAT mode. IPv4 gateways are supported. In NAT mode, you can associate a NAT gateway with up to 50 EIPs. The EIP occupies one private IP address in the vSwitch of the NAT gateway. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The value can be up to 128 characters in length and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |

|   | aliyun |
|---|---|
| acs: |   |

|   | aliyun |
|---|---|
| acs: |   |

**Return values**

Fn::GetAtt ForwardTableId: the ID of the port forwarding table. SNatTableId: the ID of the SNAT table. NatGatewayId: the unique ID of the NAT gateway. BandwidthPackageIps: the IP addresses of the Internet Shared Bandwidth instances. BandwidthPackageIds: the IDs of the Internet Shared Bandwidth instances.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the NAT gateway, [2, 256] characters. Do not fill or empty, the
default is empty."
```

`},`

```json
    "NatGatewayName": {
      "Type": "String",
      "Description": "Display name of the NAT gateway, [2, 128] English or Chinese characters, must s
tart with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
```

`},`

```json
    "InstanceChargeType": {
```

```json
      "Type": "String",
      "Description": "The billing method. The default value is PostPaid (which means pay-as-you-go)."
```

`,`

```json
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
```

`},`

```json
    "PricingCycle": {
      "Type": "String",
      "Description": "Price cycle of the resource. This property has no default value.",
      "AllowedValues": [
        "Month",
        "Year"
```

`]` `},`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The VSwitch id to create NAT gateway."
```

`},`

```json
    "Duration": {
      "Type": "Number",
      "Description": "The subscription duration. While choose by pay by month, it could be from 1 to
9. While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
```

`},`

```json
    "DeletionProtection": {
      "Type": "Boolean",
      "Description": "Whether to enable deletion protection.\nDefault to False.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
```

`},`

```json
    "AutoPay": {
      "Type": "Boolean",
      "Description": "Specifies whether to enable automatic payment. Default is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
```

`},`

```json
    "NatType": {
      "Type": "String",
      "Description": "The type of the NAT gateway. Valid values:\n- Normal: standard NAT gateway.\n-
Enhanced: enhanced NAT gateway.",
      "AllowedValues": [
        "Normal",
        "Enhanced"
```

`]` `},`

```json
    "DeletionForce": {
      "Type": "Boolean",
```

`"` `i` `i` `"` `"``h` `h` `f` `d``l` `h` `l` `i` `d``d` `i` `i` `h` `d`

```json
      "Description": "Whether force delete the relative snat and dnat entries in the net gateway and
unbind eips. Default value is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
```

`},`

```json
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id to create NAT gateway."
```

`},`

```json
    "Spec": {
      "Type": "String",
      "Description": "NAT gateway specification. Now support 'Small|Middle|Large|XLarge.1'"
```

`},`

```json
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to natgateway. Max support 20 tags to add during create
natgateway. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
```

`},`

```json
  "Resources": {
    "NatGateway": {
      "Type": "ALIYUN::ECS::NatGateway",
      "Properties": {
        "Description": {
          "Ref": "Description"
```

`},`

```json
        "NatGatewayName": {
          "Ref": "NatGatewayName"
```

`},`

```json
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
```

`},`

```json
        "PricingCycle": {
          "Ref": "PricingCycle"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "Duration": {
          "Ref": "Duration"
```

`},`

```json
        "DeletionProtection": {
          "Ref": "DeletionProtection"
```

`},`

```json
        "AutoPay": {
          "Ref": "AutoPay"
```

`},`

```json
        "NatType": {
          "Ref": "NatType"
```

`},`

```json
        "DeletionForce": {
          "Ref": "DeletionForce"
```

`},`

```json
        "VpcId": {
          "Ref": "VpcId"
```

`},`

```json
        "Spec": {
```

`p`

```json
          "Ref": "Spec"
```

`},`

```json
        "Tags": {
          "Ref": "Tags"
```

`},`

```json
  "Outputs": {
    "BandwidthPackageIds": {
      "Description": "The bandwidth package ids of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "BandwidthPackageIds"
```

`]` `},`

```json
    "NatGatewayId": {
      "Description": "The Id of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "NatGatewayId"
```

`]` `},`

```json
    "SNatTableId": {
      "Description": "The SNAT table id.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "SNatTableId"
```

`]` `},`

```json
    "BandwidthPackageIps": {
      "Description": "The allocated public IPs.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "BandwidthPackageIps"
```

`]` `},`

```json
    "ForwardTableId": {
      "Description": "The forward table id.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "ForwardTableId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
```

```
  Description:
    Type: String
    Description: >-
      Description of the NAT gateway, [2, 256] characters. Do not fill or empty,
      the default is empty.
  NatGatewayName:
    Type: String
    Description: >-
      Display name of the NAT gateway, [2, 128] English or Chinese characters,
      must start with a letter or Chinese in size, can contain numbers, '_' or
      '.', '-'
  InstanceChargeType:
    Type: String
    Description: >-
      The billing method. The default value is PostPaid (which means
      pay-as-you-go).
    AllowedValues:
      - PrePaid
      - PostPaid
    Default: PostPaid
  PricingCycle:
    Type: String
    Description: Price cycle of the resource. This property has no default value.
    AllowedValues:
      - Month
      - Year
  VSwitchId:
    Type: String
    Description: The VSwitch id to create NAT gateway.
  Duration:
    Type: Number
    Description: >-
      The subscription duration. While choose by pay by month, it could be from
      1 to 9. While choose pay by year, it could be from 1 to 3.
    MinValue: 1
    MaxValue: 9
    Default: 1
  DeletionProtection:
    Type: Boolean
    Description: |-
      Whether to enable deletion protection.
      Default to False.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  AutoPay:
    Type: Boolean
    Description: Specifies whether to enable automatic payment. Default is false.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  NatType:
    Type: String
    Description: |-
      The type of the NAT gateway. Valid values:
      - Normal: standard NAT gateway.
      - Enhanced: enhanced NAT gateway.
```

```
    AllowedValues:
      - Normal
      - Enhanced
  DeletionForce:
    Type: Boolean
    Description: >-
      Whether force delete the relative snat and dnat entries in the net gateway
      and unbind eips. Default value is false.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
    Default: false
  VpcId:
    Type: String
    Description: The VPC id to create NAT gateway.
  Spec:
    Type: String
    Description: NAT gateway specification. Now support 'Small|Middle|Large|XLarge.1'
  Tags:
    Type: Json
    Description: >-
      Tags to attach to natgateway. Max support 20 tags to add during create
      natgateway. Each tag with two properties Key and Value, and Key is
      required.
    MaxLength: 20
Resources:
  NatGateway:
    Type: 'ALIYUN::ECS::NatGateway'
    Properties:
      Description:
        Ref: Description
      NatGatewayName:
        Ref: NatGatewayName
      InstanceChargeType:
        Ref: InstanceChargeType
      PricingCycle:
        Ref: PricingCycle
      VSwitchId:
        Ref: VSwitchId
      Duration:
        Ref: Duration
      DeletionProtection:
        Ref: DeletionProtection
      AutoPay:
        Ref: AutoPay
      NatType:
        Ref: NatType
      DeletionForce:
        Ref: DeletionForce
      VpcId:
        Ref: VpcId
      Spec:
        Ref: Spec
      Tags:
        Ref: Tags
Outputs:
  BandwidthPackageIds:
    Description: The bandwidth package ids of created NAT gateway.
    Value:
      'Fn::GetAtt':
-NatGateway
```

```
         NatGateway
        - BandwidthPackageIds
  NatGatewayId:
    Description: The Id of created NAT gateway.
    Value:
      'Fn::GetAtt':
        - NatGateway
        - NatGatewayId
  SNatTableId:
    Description: The SNAT table id.
    Value:
      'Fn::GetAtt':
        - NatGateway
        - SNatTableId
  BandwidthPackageIps:
    Description: The allocated public IPs.
    Value:
      'Fn::GetAtt':
        - NatGateway
        - BandwidthPackageIps
  ForwardTableId:
    Description: The forward table id.
    Value:
      'Fn::GetAtt':
        - NatGateway
        - ForwardTableId
```

#### ALIYUN::ECS::NetworkInterface

ALIYUN::ECS::NetworkInterface is used to create an elastic network interface (ENI).

**Syntax**

```json
  "Type": "ALIYUN::ECS::NetworkInterface",
  "Properties": {
    "Description": String,
    "SecurityGroupId": String,
    "PrimaryIpAddress": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "NetworkInterfaceName": String,
    "Tags": List,
    "SecurityGroupIds": List,
    "PrivateIpAddresses": List,
    "SecondaryPrivateIpAddressCount": Integer
```

**Properties**

| Property | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The resource group ID. | None. |

| SecurityGrou pId | String | No | Yes | The security group ID. | The security group and the ENI must belong to the same virtual private cloud (VPC). Note You cannot specify both SecurityGroupId and SecurityGroupIds. |
|---|---|---|---|---|---|
| VSwitchId | String | Yes | No | The vSwitch ID. | None. |
| Description | String | No | Yes | The ENI description. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| NetworkInterf aceName | String | No | Yes | The ENI name. | The name must be 2 to 128 characters in length and must start with a letter. The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| PrimaryIpAdd ress | String | No | No | The primary private IP address of the ENI. | The IP address that you specify must be an idle IP address within the CIDR block of the vSwitch that hosts the ENI. If you leave this property empty, the system randomly assigns an idle IP address from the vSwitch CIDR block. |
| SecondaryPri vateIpAddres sCount | Integer | No | No | The number of secondary private IP addresses. | None. |
| Tags | List | No | Yes | The tags. | You can add up to 20 tags. For more information, see Tags properties. |
| SecurityGrou pIds | List | No | Yes | The IDs of one or more security groups. | The security groups and the ENI must belong to the same VPC. Note You cannot specify both SecurityGroupId and SecurityGroupIds. |

| PrivateIpAddr esses | List | No | No | The one or more secondary private IP addresses that you want to select from the CIDR block of the vSwitch that hosts the ENI. | The number of IP addresses that you can bind depends on the following conditions: When the ENI is in the Available status: 1 to 10. When the ENI is in the InUse status: subject to the instance type. |
|---|---|---|---|---|---|

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

**Return values**

Fn::GetAtt NetworkInterfaceId: the ID of the ENI. MacAddress: the MAC Address of the ENI. PrivateIpAddress: the private IP address of the ENI. SecondaryPrivateIpAddresses: the secondary private IP addresses of the ENI.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SecurityGroupId:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Label:
```

`zh-cn:` 安全组`ID`

```
      en: Security Group ID
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    Label:
```

`zh-cn:` 网络交换机`ID`

```
      en: VSwitch ID
Resources:
  EniInstance:
    Type: ALIYUN::ECS::NetworkInterface
    Properties:
      SecurityGroupId:
        Ref: SecurityGroupId
      VSwitchId:
        Ref: VSwitchId
      NetworkInterfaceName: TestNetworkInterface
Outputs:
  PrivateIpAddress:
    Description: The primary private ip address of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - PrivateIpAddress
  SecondaryPrivateIpAddresses:
    Description: The secondary private IP addresses of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - SecondaryPrivateIpAddresses
  MacAddress:
    Description: The MAC address of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - MacAddress
  NetworkInterfaceId:
    Description: ID of your Network Interface.
    Value:
      Fn::GetAtt:
        - EniInstance
        - NetworkInterfaceId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SecurityGroupId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Label": {
```

`"zh-cn": "`安全组`ID",`

```json
        "en": "Security Group ID"
```

`},`

```
"Si hd"
```

```json
    "VSwitchId": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "Type": "String",
      "Label": {
```

`"zh-cn": "`网络交换机`ID",`

```json
        "en": "VSwitch ID"
```

`},`

```json
  "Resources": {
    "EniInstance": {
      "Type": "ALIYUN::ECS::NetworkInterface",
      "Properties": {
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "NetworkInterfaceName": "TestNetworkInterface"
```

`},`

```json
  "Outputs": {
    "PrivateIpAddress": {
      "Description": "The primary private ip address of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "PrivateIpAddress"
```

`]` `},`

```json
    "SecondaryPrivateIpAddresses": {
      "Description": "The secondary private IP addresses of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "SecondaryPrivateIpAddresses"
```

`]` `},`

```json
    "MacAddress": {
      "Description": "The MAC address of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "MacAddress"
```

`]` `},`

```json
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "NetworkInterfaceId"
```

`]` For more examples, see the combined examples of creating an ENI, binding an ENI to a Virtual Private Cloud instance, and authorizing an ENI: JSON example and YAML example.

#### ALIYUN::ECS::NetworkInterfaceAttachment

ALIYUN::ECS::NetworkInterfaceAttachment is used to bind an elastic network interface (ENI) to an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC).

**Syntax**

```json
  "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
  "Properties": {
    "InstanceId": String,
    "NetworkInterfaceId": String,
    "TrunkNetworkInstanceId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | Yes | No | The ID of the instance. | None |
| NetworkInterf aceId | String | Yes | No | The ID of the ENI. | None |
| TrunkNetwor kInstanceId | String | No | No | The ID of the trunk network interface. | None |

**Return values**

Fn::GetAtt NetworkInterfaceId: the ID of the ENI. TrunkNetworkInstanceId: the ID of the trunk network interface. InstanceId: the ID of the instance.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  InstanceId:
    Type: String
    Description: ECS instance id
  TrunkNetworkInstanceId:
    Type: String
  NetworkInterfaceId:
    Type: String
    Description: Network interface id
Resources:
  EniAttachment:
    Type: 'ALIYUN::ECS::NetworkInterfaceAttachment'
    Properties:
      InstanceId:
        Ref: InstanceId
      TrunkNetworkInstanceId:
        Ref: TrunkNetworkInstanceId
      NetworkInterfaceId:
        Ref: NetworkInterfaceId
Outputs:
  TrunkNetworkInstanceId:
    Description: ID of Trunk Network Interface.
    Value:
      'Fn::GetAtt':
        - EniAttachment
        - TrunkNetworkInstanceId
  NetworkInterfaceId:
    Description: ID of your Network Interface.
    Value:
      'Fn::GetAtt':
        - EniAttachment
        - NetworkInterfaceId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "ECS instance id"
```

`},`

```json
    "TrunkNetworkInstanceId": {
      "Type": "String"
```

`},`

```json
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
```

`},`

```json
  "Resources": {
    "EniAttachment": {
      "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
```

`},`

```json
        "TrunkNetworkInstanceId": {
          "Ref": "TrunkNetworkInstanceId"
```

`},`

```json
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
```

`},`

```json
  "Outputs": {
    "TrunkNetworkInstanceId": {
      "Description": "ID of Trunk Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "TrunkNetworkInstanceId"
```

`]` `},`

```json
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "NetworkInterfaceId"
```

`]` To view more examples, visit NetworkInterfaceAttachment.json and NetworkInterfaceAttachment.yml. In the examples, the ALIYUN::ECS::NetworkInterface, ALIYUN::ECS::NetworkInterfaceAttachment, and ALIYUN::ECS::NetworkInterfacePermission resource types are used.

#### ALIYUN::ECS::NetworkInterfacePermission

ALIYUN::ECS::NetworkInterfacePermission is used to grant an account the permission to attach an elastic network interface (ENI) to an instance.

**Syntax**

```json
  "Type": "ALIYUN::ECS::NetworkInterfacePermission",
  "Properties": {
    "NetworkInterfaceId": String,
    "AccountId": String,
    "Permission": String
```

**Properties**

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| NetworkInterfac eId | String | Yes | No | The ID of the ENI. | None |
| AccountId | String | Yes | No | The ID of the account. | None |
| Permission | String | Yes | No | The permission granted to the account. | None |

**Response parameters**

**Fn::GetAtt**

NetworkInterfacePermissionId: the ID of the ENI permission.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  NetworkInterfaceId:
    Type: String
    Description: Network interface id
  Permission:
    Type: String
    Description: the permission
    Default: InstanceAttach
Resources:
  NetworkInterfacePermission:
    Type: ALIYUN::ECS::NetworkInterfacePermission
    Properties:
      NetworkInterfaceId:
        Ref: NetworkInterfaceId
      AccountId:
        Ref: ALIYUN::AccountId
      Permission:
        Ref: Permission
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
```

`},`

```json
    "Permission": {
      "Type": "String",
      "Description": "the permission",
      "Default": "InstanceAttach"
```

`},`

```json
  "Resources": {
    "NetworkInterfacePermission": {
      "Type": "ALIYUN::ECS::NetworkInterfacePermission",
      "Properties": {
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
```

`},`

```json
        "AccountId": {
          "Ref": "ALIYUN::AccountId"
```

`},`

```json
        "Permission": {
          "Ref": "Permission"
```

#### ALIYUN::ECS::Route

ALIYUN::ECS::Route is used to create a custom route entry.

**Syntax**

```json
  "Type": "ALIYUN::ECS::Route",
  "Properties": {
    "DestinationCidrBlock": String,
    "RouteTableId": String,
    "NextHopId": String,
    "NextHopType": String,
    "NextHopList": List
```

**Properties**

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| DestinationCidrBlock | String | Yes | No | The destination CIDR block of the custom route entry. | None |

| RouteTableId | String | Yes | No | The ID of the route table. | None |
|---|---|---|---|---|---|
| NextHopId | String | No | No | The ID of the next- hop instance for the custom route entry. | None |
| NextHopType | String | No | No | The type of the next hop. | Default value: Instance. Valid values: Instance: an Elastic Compute Service (ECS) instance HaVip: a high-availability virtual IP address (HAVIP) RouterInterface: a router interface NetworkInterface: an elastic network interface (ENI) VpnGateway: a VPN gateway IPv6Gateway: an IPv6 gateway NatGateway: a NAT gateway Attachment: a transit router |
| NextHopList | List | No | No | The list of next hops of the custom route entry. | If you set the NextHopList property, the route entry is an equal-cost multipath (ECMP) route. Valid values: 2 to 4. For more information, see NextHopList properties. |

**NextHopList syntax**

```json
"NextHopList": [
    "NextHopId": String,
    "NextHopType": String
```

`]`

**NextHopList properties**

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|

| NextHopId | String | Yes | No | The ID of the next- hop instance for the ECMP route entry. | None |
|---|---|---|---|---|---|
| NextHopType | String | No | No | The type of the next hop for the ECMP route entry. | Set the value to RouterInterface. |

**Return values**

Fn::GetAtt None

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  ECSRoute:
    Type: ALIYUN::ECS::Route
    Properties:
      RouteTableId: vtb-25oud****
      DestinationCidrBlock: 172.16.XX.XX/24
      NextHopId: i-25xzy****
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ECSRoute": {
      "Type": "ALIYUN::ECS::Route",
      "Properties": {
        "RouteTableId": "vtb-25oud****",
        "DestinationCidrBlock": "172.16.XX.XX/24",
        "NextHopId": "i-25xzy****"
```

To view more examples, visit Route.json and Route.yml. In the examples, the ALIYUN::ECS::AssignIpv6Addresses and ALIYUN::ECS::Route resource types are used.

#### ALIYUN::ECS::SNatEntry

Creates an SNAT entry in a NAT Gateway SNAT table.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SNatEntry",
  "Properties": {
    "SNatTableId": String,
    "SNatIp": String,
    "SnatEntryName": String,
    "SourceCIDR": String,
    "SourceVSwitchId": String
```

**Properties**

| Property name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| SNatTableId | String | Yes | Yes | The SNAT table ID. | None |
| SNatIp | String | Yes | Yes | The public IP address for SNAT. | Must be from the NAT Gateway bandwidth plan. A public IP address cannot exist in both the forwarding table and the SNAT table. |
| SnatEntryName | String | No | Yes | The name of the SNAT entry. | The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with http:// or https:// . |
| SourceCIDR | String | No | No | The CIDR block of the vSwitch or ECS instance. vSwitch granularity: Specify a vSwitch CIDR block, such as 192.168.1.0/24, to enable SNAT for all ECS instances in the vSwitch. With one SnatIp address, all instances use that address. With multiple addresses, instances randomly select one. ECS instance granularity: Specify an ECS instance IP address, such as 192.168.1.1/32, to enable SNAT for that instance. With one SnatIp address, the instance uses that address. With multiple addresses, the instance randomly selects one. | Specify either SourceCIDR or SourceVSwitchId. |
| SourceVSwitchId | String | No | Yes | The vSwitch ID. ECS instances in this vSwitch use the SNAT entry to access the Internet. | Specify either SourceCIDR or SourceVSwitchId. |

**Return values**

Fn::GetAtt SNatEntryId: The ID of the SNAT entry.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SourceVSwitchId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Description: The vSwitch that is allowed to access the Internet.
  SNatTableId:
    Type: String
    Description: The SNAT table in which to create the SNAT entry.
Resources:
  SNatTableEntry:
    Type: ALIYUN::ECS::SNatEntry
    Properties:
      SourceVSwitchId:
        Ref: SourceVSwitchId
      SnatEntryName: test_entry_name
      SNatTableId:
        Ref: SNatTableId
      SNatIp: 100.100.100.1
Outputs:
  SNatEntryId:
    Description: The ID of the created SNAT entry.
    Value:
      Fn::GetAtt:
        - SNatTableEntry
        - SNatEntryId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SourceVSwitchId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "Description": "The vSwitch that is allowed to access the Internet."
```

`},`

```json
    "SNatTableId": {
      "Type": "String",
      "Description": "The SNAT table in which to create the SNAT entry."
```

`},`

```json
  "Resources": {
    "SNatTableEntry": {
      "Type": "ALIYUN::ECS::SNatEntry",
      "Properties": {
        "SourceVSwitchId": {
          "Ref": "SourceVSwitchId"
```

`},`

```json
        "SnatEntryName": "test_entry_name",
        "SNatTableId": {
          "Ref": "SNatTableId"
```

`},`

```json
        "SNatIp": "100.100.100.1"
```

`},`

```json
  "Outputs": {
    "SNatEntryId": {
      "Description": "The ID of the created SNAT entry.",
      "Value": {
        "Fn::GetAtt": [
          "SNatTableEntry",
          "SNatEntryId"
```

`]`

#### ALIYUN::ECS::SecurityGroup

The ALIYUN::ECS::SecurityGroup resource is used to create a security group.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SecurityGroup",
  "Properties": {
    "VpcId": String,
    "Description": String,
    "SecurityGroupName": String,
    "Tags": List,
    "SecurityGroupEgress": List,
    "SecurityGroupIngress": List,
    "ResourceGroupId": String,
    "SecurityGroupType": String
```

**Properties**

| Property name | Type | Required | Allow updates | Description | Constraints |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the security group belongs. | None |
| VpcId | String | No | No | The ID of the virtual private cloud (VPC). | None |
| Description | String | No | No | The description of the security group. | The length is 2 to 256 characters. |
| Tags | List | No | Yes | The tags of the security group. | Supports a maximum of 20 tags. For more information, see Tags properties. |
| SecurityGrou pName | String | No | No | The name of the security group. | If not specified, the value is empty. The default value is empty. The length is 2 to 128 characters. Must start with a letter or a Chinese character. Cannot start with http:// or https:// . Can contain letters, Chinese characters, digits, periods (.), underscores ( ), and _ hyphens (-). |
| SecurityGrou pEgress | List | No | Yes | The outbound access rules of the security group. | For more information, see SecurityGroupEgress properties. |
| SecurityGrou pIngress | List | No | Yes | The inbound access rules of the security group. | For more information, see SecurityGroupIngress properties. |
| SecurityGrou pType | String | No | No | The type of the security group. | Valid values: normal: basic security group. enterprise: advanced security group. |

|   | http:// |
|---|---|
| https:// |   |

**Tags syntax**

```json
"Tags": [
    "Value" : String,
    "Key" : String
```

`]`

**Tags properties**

| Property name | Type | Required | Allow Updates | Description | Constraints |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The length is 1 to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | The length is 0 to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |

**SecurityGroupEgress syntax**

```json
"SecurityGroupEgress": [
    "Description": String,
    "PortRange": String,
    "NicType": String,
    "Priority": Integer,
    "DestGroupId": String,
    "DestCidrIp": String,
    "Policy": String,
    "IpProtocol": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String,
    "DestPrefixListId": String,
    "SourcePortRange": String,
    "Ipv6SourceCidrIp": String,
    "SourceCidrIp": String,
    "DestGroupOwnerAccount": String
```

`]`

**SecurityGroupEgress properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| Description | String | No | Yes | The description of the security group rule. | The length is 1 to 512 characters. |

| DestGroupOw nerId | String | No | No | The Alibaba Cloud account ID of the destination security group when you configure a security group rule across accounts. | If you do not set DestGroupOwnerId, the system assumes you configure access permissions for other security groups. If you set the DestCidrIp parameter, the DestGroupOwnerId parameter is invalid. |
|---|---|---|---|---|---|
| IpProtocol | String | Yes | No | The IP protocol. | Valid values: tcp udp icmp gre all: Supports all four protocols. |
| PortRange | String | Yes | No | The port range related to the IP protocol. | The port range related to the transport-layer protocol that the destination security group opens. Valid values: TCP/UDP protocols: 1 to 65,535. Use a forward slash (/) to separate the start port and end port. Correct example: 1/200. Incorrect example: 200/1. ICMP protocol: -1/-1. GRE protocol: -1/-1. all: -1/-1. |
| NicType | String | No | No | The network type. | Valid values: internet (default value) intranet For VPC security group rules, you do not need to set the network interface controller (NIC) type. The default value is intranet, and it can only be intranet. When you configure mutual access between security groups, which means you only specify the DestGroupId parameter, the value can only be intranet. Default value: internet. |

| DestPrefixList Id | String | No | No | The ID of the destination prefix list for which you want to configure outbound access permissions. | Call the DescribePrefixLists interface of Alibaba Cloud service ECS to query available prefix list IDs. Prefix lists are not supported when the security group network type is classic network. If you specify any of the DestCidrIp, Ipv6DestCidrIp, or DestGroupId parameters, the system ignores this parameter. |
|---|---|---|---|---|---|
| Priority | Integer | No | No | The authorization policy priority. | Valid values: 1 to 100. Default value: 1. |
| DestGroupId | String | No | No | The ID of the destination security group in the same region. | Specify either the DestGroupId or DestCidrIp parameter. If you specify both, the system authorizes DestCidrIp by default. If you specify this parameter and do not specify DestCidrIp, NicType can only be intranet. |
| DestCidrIp | String | No | No | The destination IP address range. | Specify the IP address range in CIDR format. Default value: 0.0.0.0/0 (unrestricted). Other supported formats, such as 10.159.XX.XX/12. A maximum of 10 IP addresses or CIDR blocks, separated by commas (,). Note Only IPv4 is supported. |
| Policy | String | No | No | The authorization policy. | Valid values: accept (default value): Accepts access. drop: Denies access. |
| Ipv6DestCidrI p | String | No | No | The destination IPv6 CIDR block. | Supports IP address ranges in CIDR and IPv6 formats. Only supports IP addresses of the VPC type. |

| SourcePortRa nge | String | No | No | The source port range related to the transport- layer protocol that the security group opens. | Valid values: TCP/UDP protocols: 1 to 65,535. Use a forward slash (/) to separate the start port and end port. Example: 1/200. ICMP protocol: -1/-1. GRE protocol: -1/-1. ALL: -1/-1. For quintuple rules, see Security group quintuple rules. |
|---|---|---|---|---|---|
| Ipv6SourceCi drIp | String | No | No | The source IPv6 CIDR block. | Supports IP address ranges in CIDR and IPv6 formats. For quintuple rules, see Security group quintuple rules. Note This parameter is valid only for IPv6-enabled VPC ECS instances. Do not set this parameter and the DestCidrIp parameter at the same time. |
| SourceCidrIp | String | No | No | The source IPv4 CIDR block. | Supports IP address ranges in CIDR and IPv4 formats. For quintuple rules, see Security group quintuple rules. |
| DestGroupOw nerAccount | String | No | No | The Alibaba Cloud account to which the destination security group belongs. | If neither DestGroupOwnerAccount nor DestGroupOwnerId is set, the system revokes access permissions for your other security groups. If you set the DestCidrIp parameter, the DestGroupOwnerAccount parameter is invalid. |

**SecurityGroupIngress syntax**

```json
"SecurityGroupIngress": [
    "SourceGroupOwnerId": String,
    "Description": String,
    "PortRange": String,
    "NicType": String,
    "Ipv6SourceCidrIp": String,
    "Priority": Integer,
    "SourceGroupId": String,
    "Policy": String,
    "IpProtocol": String,
    "SourcePortRange": String,
    "SourceCidrIp": String,
    "SourcePrefixListId": String,
    "Ipv6DestCidrIp": String,
    "SourceGroupOwnerAccount": String,
    "DestCidrIp": String
```

`]`

**SecurityGroupIngress properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| SourceGroup OwnerId | String | No | No | The Alibaba Cloud account ID of the source security group. | None |
| Description | String | No | Yes | The description of the security group rule. | The length is 1 to 512 characters. |
| SourcePrefixL istId | String | No | No | The ID of the source prefix list for which you want to configure inbound access permissions. | Call the DescribePrefixLists interface of Alibaba Cloud service ECS to query available prefix list IDs. Prefix lists are not supported when the security group network type is classic network. If you specify any of the SourceCidrIp, Ipv6DestCidrIp, or DestGroupId parameters, the system ignores this parameter. |
| IpProtocol | String | Yes | No | The IP protocol. | Valid values: tcp udp icmp gre all: Supports all four protocols. |

| PortRange | String | Yes | No | The port range related to the IP protocol. | The port range related to the transport-layer protocol that the destination security group opens. Valid values: TCP/UDP protocols: 1 to 65,535. Use a forward slash (/) to separate the start port and end port. Correct example: 1/200. Incorrect example: 200/1. ICMP protocol: -1/-1. GRE protocol: -1/-1. all: -1/-1. |
|---|---|---|---|---|---|
| SourceGroupI d | String | No | No | The ID of the source security group in the same region. | Specify either the SourceGroupId or SourceCidrIp parameter. If you specify both, the system authorizes SourceCidrIp by default. If you specify this parameter and do not specify SourceCidrIp, NicType can only be intranet. |
| NicType | String | No | No | The network type. | Valid values: internet (default value) intranet |
| Priority | Integer | No | No | The authorization policy priority. | Valid values: 1 to 100. Default value: 1. |
| SourceCidrIp | String | No | No | The source IP address range. | Specify the IP address range in CIDR format. Default value: 0.0.0.0/0 (unrestricted). Other supported formats, such as 10.159.XX.XX/12. A maximum of 10 IP addresses or CIDR blocks, separated by commas (,). Note Only IPv4 is supported. |
| Policy | String | No | No | The authorization policy. | Valid values: accept (default value): Accepts access. drop: Denies access. |

| SourcePortRa nge | String | No | No |   | The range of ports that are open in the source security group for the transport- layer protocol. | Valid values: TCP/UDP protocols: 1 to 65,535. Use a forward slash (/) to separate the start port and end port. Correct example: 1/200. Incorrect example: 200/1. ICMP protocol: -1/-1. GRE protocol: -1/-1. If IpProtocol is set to all: -1/- 1. |   |
|---|---|---|---|---|---|---|---|
| Ipv6SourceCi drIp | String | No | No |   | The source IPv6 CIDR block. | Only supports IP addresses of the VPC type. Supports IP address ranges in CIDR and IPv6 formats. |   |
| Ipv6DestCidrI p | String | No | No |   | The destination IPv6 CIDR block. | Supports IP address ranges in CIDR and IPv6 formats. Note This parameter is valid only for IPv6-enabled VPC ECS instances. Do not set this parameter and the DestCidrIp parameter at the same time. |   |
| SourceGroup OwnerAccoun t | String | No | No |   |   | If neither SourceGroupOwnerAccount nor SourceGroupOwnerId is set, the system assumes you configure access permissions for your other security groups. If you set the SourceCidrIp parameter, the SourceGroupOwnerAccount parameter is invalid. |   |
|   |   |   |   |   |   |   | SourceGroupOwnerAccount |
|   |   |   |   |   | The Alibaba Cloud account to which the source security group belongs. |   |   |
|   |   |   |   |   |   |   | SourceGroupOwnerAccount |
| DestCidrIp | String | No | No |   | The destination IPv4 CIDR block. | Supports IP address ranges in CIDR and IPv4 formats. For quintuple rules, see Security group quintuple rules. |   |

**Return values**

Fn::GetAtt SecurityGroupId: The security group ID. SecurityGroupName: The security group name.

**Examples**

**Scenario 1: Create a basic security group in an existing VPC.**

Quick create YAML JSON

**Scenario 2: Create an advanced security group in an existing VPC.**

Quick create YAML JSON

**Scenario 3: Create an ECS instance and configure the security group to**

**open inbound port 9966.**

Quick create YAML JSON For more examples, see public templates that include this resource.

#### ALIYUN::ECS::SecurityGroupClone

ALIYUN::ECS::SecurityGroupClone is used to clone a security group.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SecurityGroupClone",
  "Properties": {
    "DestinationRegionId": String,
    "VpcId": String,
    "Description": String,
    "SecurityGroupName": String,
    "SourceSecurityGroupId": String,
    "ResourceGroupId": String,
    "NetworkType": String,
    "SecurityGroupType": String
```

**Properties**

| Parameter | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| ResourceGroupI d | String | No | Yes | The ID of the resource group to which the instance belongs. | None. |
| SourceSecurityG roupId | String | Yes | No | The ID of the source security group. | Appropriate security group rules are cloned based on the network type of the new security group. |

| NetworkType | String | No | No | The network type of the new security group. | Valid value: Classic. |
|---|---|---|---|---|---|
| VpcId | String | No | No | The ID of the VPC to which the new security group belongs. | When you specify both VpcId and NetworkType, the NetworkType setting does not take effect. |
| Description | String | No | No | The description of the security group. | The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| SecurityGroupNa me | String | No | No | The name of the security group. | The default value is empty. The name must be 2 to 128 characters in length and must start with a letter. It can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-), but cannot start with http:// or https://. |
| DestinationRegi onId | String | No | No | The ID of the destination region where the new security group resides. | Default value: CURRENT. |
| SecurityGroupTy pe | String | No | No | The type of the security group. | Valid values: normal: basic security group. enterprise: advanced security group. |

**Return values**

Fn::GetAtt SecurityGroupId: the ID of the security group.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SecurityGroupClone": {
```

```json
      "Type": "ALIYUN::ECS::SecurityGroupClone",
      "Properties": {
        "SourceSecurityGroupId": {
          "Ref": "SourceSecurityGroupId"
```

`},`

```json
        "VpcId": {
          "Ref": "VpcId"
```

`},`

```json
        "Description": {
          "Ref": "Description"
```

`},`

```json
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
```

`},`

```json
        "DestinationRegionId": {
          "Ref": "DestinationRegionId"
```

`},`

```json
        "NetworkType": {
          "Ref": "NetworkType"
```

`},`

```json
  "Parameters": {
    "SourceSecurityGroupId": {
      "Type": "String",
      "Description": "Source security group ID is used to copy properties to clone new security
group. If the NetworkType and VpcId is not specified, the same security group will be cloned. If Netw orkType or VpcId is specified, only proper security group rules will be cloned."
```

`},`

```json
    "VpcId": {
      "Type": "String",
      "Description": "Physical ID of the VPC."
```

`},`

```json
    "Description": {
      "Type": "String",
      "Description": "Description of the security group, [2, 256] characters. Do not fill or empty, t
he default is empty."
```

`},`

```json
    "SecurityGroupName": {
      "Type": "String",
      "Description": "Display name of the security group, [2, 128] English or Chinese characters, mus
t start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
```

`},`

```json
    "DestinationRegionId": {
      "Default": "CURRENT",
      "Type": "String",
      "Description": "Clone security group to the specified region. Default to current region."
```

`},`

```json
    "NetworkType": {
      "Type": "String",
      "Description": "Clone new security group as classic network type. If the VpcId is specified, th
e value will be ignored.",
      "AllowedValues": [
        "Classic"
```

`]` `},`

```json
  "Outputs": {
    "SecurityGroupId": {
      "Description": "Generated security group id of new security group.",
      "Value": {
"Fn::GetAtt":[
```

```
        "Fn::GetAtt": [
          "SecurityGroupClone",
          "SecurityGroupId"
```

`]`

#### ALIYUN::ECS::SecurityGroupEgress

The ALIYUN::ECS::SecurityGroupEgress resource creates an outbound access rule for a security group.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SecurityGroupEgress",
  "Properties": {
    "SecurityGroupId": String,
    "IpProtocol": String,
    "PortRange": String,
    "DestGroupId": String,
    "DestCidrIp": String,
    "Policy": String,
    "Priority": String,
    "NicType": String,
    "DestPrefixListId": String,
    "Description": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String
```

**Properties**

| Property Name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| IpProtocol | String | Yes | No | The transport- layer protocol. | Valid values: tcp udp icmp gre all: all four protocols are supported. |

| PortRange | String | Yes | No | The range of destination ports that are open for the transport- layer protocol. | Valid values: For TCP/UDP: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. For example: 1/200. An incorrect example is 200/1. For ICMP: -1/- 1. For GRE: -1/- 1. For all: -1/-1. For more information about common port scenarios, see Commonly used ports. |
|---|---|---|---|---|---|
| SecurityGroupId | String | No | No | The ID of the source security group. | None |
| DestPrefixListId | String | No | No | The ID of the destination prefix list for which you want to set outbound access permissions. | You can call DescribePrefixLi sts to query the IDs of available prefix lists. You cannot set a prefix list for a security group in the classic network. For more information, see Limits on security groups. This parameter is ignored if you specify DestCidrIp, Ipv6DestCidrIp, or DestGroupId. |
| NicType | String | No | No | The network interface controller (NIC) type. | Valid values: internet (default): a public NIC. intranet: a private NIC. If you set mutual access between security groups by specifying DestGroupId but not DestCidrIp, this parameter is set to intranet. |

| Priority | Integer | No | No | The priority of the security group rule. | Valid values: 1 to 100. Default value: 1. |
|---|---|---|---|---|---|
| DestGroupId | String | No | No | The ID of the destination security group for which you want to set access permissions. | Specify either DestGroupId or DestCidrIp. If you specify DestGroupId but not DestCidrIp, NicType is set to intranet. If you specify both DestGroupId and DestCidrIp, the value of DestCidrIp takes precedence. |
| DestCidrIp | String | No | No | The destination IP address range. | Supports IPv4 address ranges. |
| Policy | String | No | No | You can set access permissions. | Valid values: accept (default): grants access. drop: denies access. |
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters long. |
| DestGroupOwne rId | String | No | No | When you set a security group rule across accounts, this is the Alibaba Cloud account ID of the destination security group. | If you do not set DestGroupOwne rId, the rule is considered a rule for another security group within your account. If you have already set DestCidrIp, the DestGroupOwne rId setting is invalid. |
| Ipv6DestCidrIp | String | No | No | The destination IPv6 CIDR block. | Supports CIDR blocks and IPv6 address ranges. Only IP addresses in VPCs are supported. |

**Return value**

Fn::GetAtt None.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test ECS SecurityGroupEgress Parameters:
  SecurityGroupId:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Label:
      zh-cn: Security Group ID
      en: Security Group ID
Resources:
  SgEgress:
    Type: ALIYUN::ECS::SecurityGroupEgress
    Properties:
      IpProtocol: all
      PortRange: '-1/-1'
      NicType: intranet
      SecurityGroupId:
        Ref: SecurityGroupId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test ECS SecurityGroupEgress",
  "Parameters": {
    "SecurityGroupId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Label": {
        "zh-cn": "Security Group ID",
        "en": "Security Group ID"
```

`},`

```json
  "Resources": {
    "SgEgress": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
      "Properties": {
        "IpProtocol": "all",
        "PortRange": "-1/-1",
        "NicType": "intranet",
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
```

#### ALIYUN::ECS::SecurityGroupIngress

Creates an inbound rule for a security group.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SecurityGroupIngress",
  "Properties": {
    "SourceGroupOwnerId": String,
    "Description": String,
    "PortRange": String,
    "SecurityGroupId": String,
    "NicType": String,
    "Ipv6SourceCidrIp": String,
    "Priority": Integer,
    "SourceGroupId": String,
    "Policy": String,
    "IpProtocol": String,
    "SourcePortRange": String,
    "SourceCidrIp": String,
    "SourcePrefixListId": String
```

**Properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| IpProtocol | String | Yes | No | The IP protocol. | Valid values: tcp udp icmp gre all: Supports TCP, UDP, ICMP, and GRE. |
| PortRange | String | Yes | No | The range of transport-layer ports opened in the destination security group. | Valid values: TCP/UDP: 1 to 65535. Use a forward slash (/) to separate the start port from the end port. For example: 1/200. An invalid example is 200/1. ICMP: -1/-1. GRE: -1/-1. all: -1/-1. |

| SourcePrefixListI d | String | No | No | The ID of the destination prefix list to use for inbound access control. | Call the ECS DescribePrefixLi sts operation to query available prefix list IDs. Not supported for classic network security groups. If you specify SourceCidrIp, Ipv6SourceCidrI p, or SourceGroupId, this parameter is ignored. |
|---|---|---|---|---|---|
| SourceGroupId | String | No | No | The ID of the source security group. | You must specify either SourceGroupId or SourceCidrIp. If you specify SourceGroupId but not SourceCidrIp, NicType is set to intranet. If you specify both SourceGroupId and SourceCidrIp, the SourceCidrIp setting takes precedence. |
| SecurityGroupId | String | No | No | The ID of the security group for which you want to create an inbound rule. | None |
| NicType | String | No | No | The network type. | Valid values: internet (default): public NIC. intranet: private NIC. When you configure mutual access between security groups —for example, when you specify DestGroupId but not DestCidrIp— the value of this parameter is intranet. |

| Priority | Integer | No | No | The priority of the security group rule. | Valid values: 1 to 100. Default value: 1. |
|---|---|---|---|---|---|
| SourceCidrIp | String | No | No | The source IPv4 CIDR block. | Only IPv4 CIDR blocks are supported. |
| Policy | String | No | No | The access control policy. | Valid values: accept (default): Allows access. drop: Denies access. |
| SourceGroupOw nerId | String | No | No | The Alibaba Cloud account ID of the source security group owner. Used for cross-account rules. | If SourceGroupOw nerId is not set, access permissions are set for your other security groups by default. If you specify SourceCidrIp, this parameter is ignored. |
| Description | String | No | Yes | The description of the security group rule. | Length: 1 to 512 characters. |
| SourcePortRang e | String | No | No | The range of transport-layer ports open in the source security group. | Valid values: TCP/UDP: 1 to 65535. Use a forward slash (/) to separate the start port from the end port. For example: 1/200. An invalid example is 200/1. ICMP: -1/-1. GRE: -1/-1. all: -1/-1. |
| Ipv6SourceCidrI p | String | No | No | The source IPv6 CIDR block. | Supports IPv6 CIDR blocks and addresses. VPC only. |

**Return values**

Fn::GetAtt None.

**Examples**

**Scenario 1: Select an existing security group and open inbound port**

**3306.**

Quick Create YAML JSON

**Scenario 2: Create a security group and open inbound port 80.**

Quick Create YAML JSON

**Scenario 3: Create an ECS instance and open inbound port 3000 as the**

**service port for a Flowise application.**

Quick Create YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Description: Create an Ubuntu 22.04 ECS instance, configure security groups and networking, automate the installation of Node.js alongside the Flowise AI agent service, and provision an external access URL. Parameters:
  SystemDiskCategory:
    Default: cloud_essd
    AssociationProperty: ALIYUN::ECS::Disk::SystemDiskCategory
    AssociationPropertyMetadata:
      LocaleKey: DiskCategory
      AutoChangeType: false
      InstanceType: ${InstanceType}
      AutoSelectFirst: true
      ZoneId: ${ZoneId}
    Type: String
    Label: System Disk Type
  InstanceType:
    AssociationProperty: ALIYUN::ECS::Instance::InstanceType
    AssociationPropertyMetadata:
      DefaultValueStrategy: recent
      ZoneId: ${ZoneId}
    Type: String
    Label: Instance Type
  InstancePassword:
    AssociationPropertyMetadata:
      Visible:
        Condition:
          Fn::Equals:
            - ${SelectInstance}
            - false
    Description: The logon password for the server. The password must be 8 to 30 characters long and
contain at least three of the following character types: uppercase letters, lowercase letters, digits , and special characters: ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/
    Default: Null
    Type: String
    Label: Instance Password
NoEcho:true
```

```
    NoEcho: true
    AssociationProperty: ALIYUN::ECS::Instance::Password
    ConstraintDescription: The logon password for the server. The password must be 8 to 30 characters
long and contain at least three of the following character types: uppercase letters, lowercase letter s, digits, and special characters: ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/
  ZoneId:
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Type: String
```

`Description:` **<font color='blue'>This template uses Git to clone the FlowiseAI/Flowise repository from**

**GitHub. You may encounter network issues when you use this template in a region within China. You can s**

**witch to a region outside China.</font>**

```
    Label: Availability Zone
Outputs:
  FlowiseUrl:
    Description: The default address for Flowise.
    Value:
      Fn::Sub:
        - http://${IP}:3000
        - IP:
            Fn::Jq:
              - First
              - if .[0].PublicIpAddress != [] then .[0].PublicIpAddress[0] else .
[0].EipAddress.IpAddress end
              - Fn::GetAtt:
                  - DS_Instances
                  - Instances
Resources:
  SecurityGroupIngress_3000:
    Type: ALIYUN::ECS::SecurityGroupIngress
    Properties:
      IpProtocol: tcp
      SecurityGroupId:
        Ref: SecurityGroup
      NicType: intranet
      SourceCidrIp: 0.0.0.0/0
      PortRange: 3000/3000
  InstanceGroup:
    Type: ALIYUN::ECS::InstanceGroup
    Properties:
      SystemDiskCategory:
        Ref: SystemDiskCategory
      VpcId:
        Ref: Vpc
      SecurityGroupId:
        Ref: SecurityGroup
      ImageId: ubuntu_22_04
      IoOptimized: optimized
      VSwitchId:
        Ref: VSwitch
      Password:
        Ref: InstancePassword
      InstanceName: Flowise
      InstanceType:
        Ref: InstanceType
      MaxAmount: 1
  SecurityGroup:
    Type: ALIYUN::ECS::SecurityGroup
    Properties:
      VpcId:
        Ref: Vpc
  DS_Instances:
    Type: DATASOURCE::ECS::Instances
    Properties:
```

```
      InstanceIds:
        Fn::GetAtt:
          - InstanceGroup
          - InstanceIds
  Vpc:
    Type: ALIYUN::ECS::VPC
    Properties:
      CidrBlock: 192.168.0.0/16
  InstallFlowise:
    Type: ALIYUN::ECS::RunCommand
    Properties:
      CommandContent: |
        #!/bin/bash
        echo "#########################"
        echo "# Install NodeJS"
        echo "#########################"
        git clone https://github.com/nvm-sh/nvm.git /opt/nvm && cd /opt/nvm
        ret_code=$?
        if [ $ret_code -ne 0 ]; then
          echo "Git clone https://github.com/nvm-sh/nvm.git failed. Exiting."
          exit $ret_code
```

`fi`

```
        ./install.sh
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
        nvm install 22
        npm config set registry https://registry.npmmirror.com
        npm i -g pnpm
        echo "#########################"
        echo "# Install Flowise"
        echo "#########################"
        git clone --depth 1 https://github.com/FlowiseAI/Flowise.git /opt/Flowise && cd /opt/Flowise
        ret_code=$?
        if [ $ret_code -ne 0 ]; then
          echo "Git clone https://github.com/FlowiseAI/Flowise.git failed. Exiting."
          exit $ret_code
```

`fi`

```
        pnpm install
        pnpm build
        nohup pnpm start > flowise.log 2>&1 &
      Type: RunShellScript
      Sync: true
      InstanceIds:
        Fn::GetAtt:
          - InstanceGroup
          - InstanceIds
      Timeout: 1800
  VSwitch:
    Type: ALIYUN::ECS::VSwitch
    Properties:
      VpcId:
        Ref: Vpc
      CidrBlock: 192.168.0.0/24
      ZoneId:
        Ref: ZoneId
Metadata: {}
```

Explore more public templates for this resource.

#### ALIYUN::ECS::Snapshot

ALIYUN::ECS::Snapshot is used to create a disk snapshot.

**Syntax**

```json
  "Type": "ALIYUN::ECS::Snapshot",
  "Properties": {
    "SnapshotName": String,
    "Timeout": Integer,
    "Description": String,
    "DiskId": String,
    "Tags": List,
    "InstantAccess": Boolean,
    "InstantAccessRetentionDays": Integer
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskId | String | Yes | No | The ID of the disk for which you want to create the snapshot. | None |
| SnapshotNam e | String | No | No | The name of the snapshot. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . The name cannot start with auto because a snapshot whose name starts with auto is recognized as an automatic snapshot. |
| Timeout | Integer | No | No | The timeout period of the snapshot creation task. | If this parameter is specified, the timeout period to create a stack is extended. If the snapshot is not created within the specified timeout period, the entire stack cannot be created. Set this parameter based on the disk size and data volume. Valid values: 200 to 1440. Default value: 200. Unit: minutes. |
| Description | String | No | No | The description of the snapshot. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . This parameter is empty by default. |

| Tags | List | No | Yes | The tags of the snapshot. | A maximum of 20 tags can be specified. For more information, see the Tags properties section in this topic. |
|---|---|---|---|---|---|
| InstantAccess | Boolean | No | No | Specifies whether to enable the instant access feature. | Default value: false. Valid values: true: The instant access feature is enabled. This feature can be enabled only for enhanced SSDs (ESSDs). false: The instant access feature is disabled. If InstantAccess is set to false, normal snapshots are created. |
| InstantAccess RetentionDay s | Integer | No | No | Specifies the retention period of the instant access feature. After the retention period ends, the snapshot is automatically released. | This parameter is valid only when InstantAccess is set to true. Valid values: 1 to 65535. Unit: days. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

**Response parameters**

Fn::GetAtt SnapshotId: the ID of the snapshot.

**Examples**

`JSON` format

|   | "ROSTemplateFormatVersion": "2015-09-01", "Parameters": { "InstantAccess": { "Type": "Boolean", "Description": "Specifies whether to enable the instant access feature. Valid values: \ntrue: enab les the instant access feature. This feature can be enabled only for enhanced SSDs (ESSDs) \nfalse: d isables the instant access feature. If InstantAccess is set to false, normal snapshots are created.\n Default value: false.\nNote This parameter and the Category parameter cannot be specified at the same time. \nFor more information, see the \"Description\" section in this topic.", "AllowedValues": [ "True", "true", "False", "false" ] }, "Description": { "Type": "String", "Description": "The description of a snapshot can be 2 to 256 characters in length and cannot begi n with http:// or https://. The description will appear on the console. By default, the value is zero ." }, "Timeout": { "Type": "Number", "Description": "The number of minutes to wait for create snapshot.", "MinValue": 200, "MaxValue": 1440, "Default": 200 }, "SnapshotName": { "Type": "String", "Description": "The name of the snapshot, [2, 128] English or Chinese characters. It must begin wi th an uppercase/lowercase letter or a Chinese character, and may contain numbers, ' ' or '-'. It cann _ ot begin with http:// or https://." }, "InstantAccessRetentionDays": { "Type": "Number", "Description": "Specifies the retention period of the instant access feature. After the retention period ends, \nthe snapshot is automatically released. This parameter takes effect only when InstantAccess \nis set to true. Unit: days.\nValid values: 1 to 65535. By default, the value of \nthi s parameter is the same as that of RetentionDays." }, "Tags": { "Type": "Json", "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac h tag with two properties Key and Value, and Key is required.", "MaxLength": 20 }, "DiskId": { "Type": "String", "Description": "Indicates the ID of the specified disk." } }, "Resources": { "Snapshot": { "Type": "ALIYUN::ECS::Snapshot", "Properties": { "InstantAccess": { "Ref": "InstantAccess" }, "Description": { "Ref": "Description" |   |
|---|---|---|

`},`

```json
    "Timeout": {
     "Ref": "Timeout"
```

`},`

```json
    "SnapshotName": {
     "Ref": "SnapshotName"
```

`},`

```json
    "InstantAccessRetentionDays": {
     "Ref": "InstantAccessRetentionDays"
```

`},`

```json
    "Tags": {
     "Ref": "Tags"
```

`},`

```json
    "DiskId": {
     "Ref": "DiskId"
```

`},`

```json
 "Outputs": {
  "SnapshotId": {
   "Description": "The snapshot ID.",
   "Value": {
    "Fn::GetAtt": [
     "Snapshot",
     "SnapshotId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 Description:
  Description: The description of a snapshot can be 2 to 256 characters in length
   and cannot begin with http:// or https://. The description will appear on the
   console. By default, the value is zero.
  Type: String
 DiskId:
  Description: Indicates the ID of the specified disk.
  Type: String
 InstantAccess:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Description: "Specifies whether to enable the instant access feature. Valid values:\
   \ \ntrue: enables the instant access feature. This feature can be enabled only\
   \ for enhanced SSDs (ESSDs) \nfalse: disables the instant access feature. If\
   \ InstantAccess is set to false, normal snapshots are created.\nDefault value:\
   \ false.\nNote This parameter and the Category parameter cannot be specified\
   \ at the same time. \nFor more information, see the \"Description\" section\
   \ in this topic."
  Type: Boolean
 InstantAccessRetentionDays:
  Description: "Specifies the retention period of the instant access feature. After\
   \ the retention period ends, \nthe snapshot is automatically released. This\
   \ parameter takes effect only when InstantAccess \nis set to true. Unit: days.\n\
```

```
   Valid values: 1 to 65535. By default, the value of \nthis parameter is the same\
   \ as that of RetentionDays."
  Type: Number
 SnapshotName:
  Description: The name of the snapshot, [2, 128] English or Chinese characters.
   It must begin with an uppercase/lowercase letter or a Chinese character, and
   may contain numbers, '_' or '-'. It cannot begin with http:// or https://.
  Type: String
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
  Type: Json
 Timeout:
  Default: 200
  Description: The number of minutes to wait for create snapshot.
  MaxValue: 1440
  MinValue: 200
  Type: Number
Resources:
 Snapshot:
  Properties:
   Description:
    Ref: Description
   DiskId:
    Ref: DiskId
   InstantAccess:
    Ref: InstantAccess
   InstantAccessRetentionDays:
    Ref: InstantAccessRetentionDays
   SnapshotName:
    Ref: SnapshotName
   Tags:
    Ref: Tags
   Timeout:
    Ref: Timeout
  Type: ALIYUN::ECS::Snapshot
Outputs:
 SnapshotId:
  Description: The snapshot ID.
  Value:
   Fn::GetAtt:
   - Snapshot
   - SnapshotId
```

For more examples, visit DiskAttachment.json and DiskAttachment.yml. In the examples, the ALIYUN::ECS::DiskAttachment and ALIYUN::ECS::Snapshot resource types are involved.

#### ALIYUN::ECS::SSHKeyPair

ALIYUN::ECS::SSHKeyPair creates an SSH key pair or imports an existing one.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SSHKeyPair",
  "Properties": {
    "ResourceGroupId": String,
    "KeyPairName": String,
    "PublicKeyBody": String,
    "Tags": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The resource group ID. | None. |
| KeyPairName | String | Yes | No | The key pair name. | 2 to 128 characters. Can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). Must start with a letter. Cannot start with http:// or https:// . |
| PublicKeyBod y | String | No | No | The public key. | Required only when importing an existing key pair. |
| Tags | List | No | Yes | The tags. | Maximum: 20. For more information, see Tags properties. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | 1 to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | Up to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |

**Return values**

Fn::GetAtt KeyPairFingerPrint: the key pair fingerprint. The MD5 hash is computed based on the public key fingerprint format defined in RFC 4716. PrivateKeyBody: the unencrypted RSA private key in PEM-encoded PKCS#8 format. Returned only when creating a new key pair. Not available for imported keys. KeyPairName: the key pair name. Arn: the Alibaba Cloud Resource Name (ARN).

**Examples**

YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Parameters: {} Resources:
  SSHKeyPair:
    Type: ALIYUN::ECS::SSHKeyPair
    Properties:
      KeyPairName:
        Fn::Sub: ess-${ALIYUN::StackId}
Outputs:
  KeyPairFingerPrint:
    Description: 'The fingerprint of the key pair. The public key fingerprint format defined in RFC47
16: MD5 message digest algorithm. '
    Value:
      Fn::GetAtt:
        - SSHKeyPair
        - KeyPairFingerPrint
  KeyPairName:
    Description: SSH Key pair name.
    Value:
      Fn::GetAtt:
        - SSHKeyPair
        - KeyPairName
  PrivateKeyBody:
    Description: 'The private key of the key pair. Content of the RSA private key in the PKCS#8 forma
t of the unencrypted PEM encoding. Refer to: https://www.openssl.org/docs/apps/pkcs8.html.User only c an get the private key one time when and only when SSH key pair is created.'
    Value:
      Fn::GetAtt:
        - SSHKeyPair
        - PrivateKeyBody
```

Additional YAML examples are available on GitHub.

#### ALIYUN::ECS::SSHKeyPairAttachment

ALIYUN::ECS::SSHKeyPairAttachment is used to attach an SSH key pair to specified ECS instances.

**Syntax**

```json
  "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
  "Properties": {
    "InstanceIds": List,
    "KeyPairName": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceIds | List | Yes | Yes | The IDs of the ECS instances to which the SSH key pair is attached. | Separate IDs with commas (,). Only Linux instances are supported. |
| KeyPairName | String | Yes | No | The name of the SSH key pair. | None |

**Response parameters**

Fn::GetAtt None.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  RegionId:
    Type: String
    AssociationProperty: ALIYUN::ECS::RegionId
  InstanceId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Instance::InstanceId
    AssociationPropertyMetadata:
      RegionId: ${RegionId}
Resources:
  SSHKeyPairAttachment:
    Type: ALIYUN::ECS::SSHKeyPairAttachment
    Properties:
      KeyPairName: ssh_key_pai****
      InstanceIds:
        - Ref: InstanceId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "RegionId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::RegionId"
```

`},`

```json
    "InstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceId",
      "AssociationPropertyMetadata": {
        "RegionId": "${RegionId}"
```

`},`

```json
  "Resources": {
    "SSHKeyPairAttachment": {
      "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
      "Properties": {
        "KeyPairName": "ssh_key_pai****",
        "InstanceIds": [
            "Ref": "InstanceId"
```

`]`

#### ALIYUN::ECS::VPC

Use ALIYUN::ECS::VPC to create a virtual private cloud (VPC).

**Syntax**

```json
  "Type": "ALIYUN::ECS::VPC",
  "Properties": {
    "Description": String,
    "Tags": List,
    "Ipv6CidrBlock": String,
    "EnableIpv6": Boolean,
    "ResourceGroupId": String,
    "VpcName": String,
    "CidrBlock": String,
    "Ipv6Isp": String,
    "UserCidr": String,
    "SecondaryCidrBlocks": List
```

**Properties**

| Property Name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|

| ResourceGro upId | String | No | Yes | The ID of the resource group. | None |
|---|---|---|---|---|---|
| VpcName | String | No | Yes | The name of the VPC. | The value must be 2 to 128 characters in length. It must start with a letter or a Chinese character, but not with http:// or https:// . It can contain letters, Chinese characters, digits, underscores ( ), and hyphens (-). _ |
| CidrBlock | String | No | Yes | The IPv4 CIDR block of the VPC. | Valid values: 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16 and its subnets |
| Description | String | No | Yes | The description of the VPC. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| Ipv6CidrBlock | String | No | No | The IPv6 CIDR block of the VPC. | None |
| EnableIpv6 | Boolean | No | Yes | Specifies whether to enable IPv6 for the VPC. | Valid values: true: The feature is enabled. false (default): shutdown. |
| Tags | List | No | Yes | Tag | You can add up to 20 tags. For more information, see Tags properties. |
| Ipv6Isp | String | No | No | The type of IPv6 address segment for the Virtual Private Cloud (VPC). | Valid values: BGP (default): Alibaba Cloud Border Gateway Protocol (BGP) IPv6 |

| UserCidr | String | No | No | The user CIDR block. | To specify multiple CIDR blocks, separate them with commas (,). You can specify a maximum of three CIDR blocks. Note For more information about user CIDR blocks, see CIDR block FAQ. |
|---|---|---|---|---|---|
| SecondaryCid rBlocks | List | No | No | SecondaryCid rBlocks | None |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Property Name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length. It cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length. It cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

**Return values**

Fn::GetAtt VpcId: The ID of the VPC. VRouterId: The ID of the vRouter. RouteTableId: The ID of the route table. VpcName: The name of the VPC.

**Examples**

**Scenario 1: Create a VPC**

Quick create YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VpcCidrBlock:
    Type: String
    Label: VPC IPv4 CIDR block
    Description: 'The IP address range of the VPC in CIDR block format.<br>You can use the following
IP address ranges and their subnets:<br><font color=''green''>[10.0.0.0/8]</font><br><font color=''gr een''>[172.16.0.0/12]</font><br><font color=''green''>[192.168.0.0/16]</font>'
    Default: 192.168.0.0/16
    AssociationProperty: ALIYUN::VPC::VPC::CidrBlock
  VpcName:
    Type: String
    Label: VPC Name
    Description: The name of the VPC. It must be 2 to 128 characters in length, start with an
uppercase or lowercase letter or a Chinese character, and can contain numbers, underscores (_), and h yphens (-).
    ConstraintDescription: 'The name must be 2 to 128 characters in length.'
    Default: MyVpc
    MinLength: 2
    MaxLength: 128
Resources:
  Vpc:
    Type: ALIYUN::ECS::VPC
    Properties:
      CidrBlock:
        Ref: VpcCidrBlock
      VpcName:
        Ref: VpcName
Outputs:
  VRouterId:
    Description: Router ID of the created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - VRouterId
  RouteTableId:
    Description: The route table ID of the created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - RouteTableId
  VpcId:
    Description: ID of the created VPC.
    Value:
      Fn::GetAtt:
        - Vpc
        - VpcId
```

**Scenario 2: Create a dual-stack (IPv4 and IPv6) ECS instance and**

**configure an IPv6 gateway and bandwidth**

Quick create YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Description:
  en: Create a dual-stack cloud server (ECS) and automatically configure IPv6 public IP, including VP
C, security group, IPv6 gateway and bandwidth settings. Parameters:
  InstanceImageId:
```

`g`

```
    AssociationPropertyMetadata:
      InstanceType: ${InstanceType}
      SupportedImageOwnerAlias:
        - system
        - self
        - others
    Description:
      en: 'The image ID.
For Linux, select: <font color=''red''><b>centos_7</font> For Windows, select: <font color=''red''><b>win2008r2, win2012r2, or win2016</font>'
    Default: centos_7_04_64_20G_alibase_201701015.vhd
    Label:
      en: Image
    AssociationProperty: ALIYUN::ECS::Image::ImageId
    Type: String
  SystemDiskCategory:
    AssociationProperty: ALIYUN::ECS::Disk::SystemDiskCategory
    AssociationPropertyMetadata:
      LocaleKey: DiskCategory
      InstanceType: ${InstanceType}
    Type: String
    Description:
```

`en: '<font color=''blue''>`**Valid values:**`</font>`

```
[cloud_efficiency: <font color=''green''>ultra disk</font>]<br>[cloud_ssd: <font color=''green''>standard SSD</font>]<br>[cloud_essd: <font color=''green''>enterprise SSD</font>]<br> [cloud: <font color=''green''>basic disk</font>]<br>[ephemeral_ssd: <font color=''green''>local SSD</ font>]'
```

**Label:**

**en: System Disk Type**

**SystemDiskSize:**

**Default: 40**

**Type: Number**

**Description:**

**en: 'The size of the system disk. Unit: GB. Valid values: 20 to 500.'**

**Label:**

**en: System Disk Space**

**VpcCidrBlock:**

**Default: 192.168.0.0/16**

**Label:**

**en: VPC IPv4 CIDR Block**

**Type: String**

**Description:**

**en: 'The IPv4 CIDR block of the VPC. We recommend that you use one of the following CIDR blocks:<br**

**><font color=''green''>[10.0.0.0/8]</font><br><font color=''green''>[172.16.0.0/12]</font><br><font col**

**or=''green''>[192.168.0.0/16]</font>'**

**AllowedValues:**

  - **- 192.168.0.0/16**
  - **- 172.16.0.0/12**
  - **- 10.0.0.0/8**

**InstanceType:**

**AssociationProperty: ALIYUN::ECS::Instance::InstanceType**

**AssociationPropertyMetadata:**

**ZoneId: VSwitchZoneId**

**Type: String**

**Description:**

**en: 'The instance type. Make sure that the instance type is available in the selected zone.<br>A comm**

**on instance type is <font color=''red''><b>ecs.c5.large</font>.**

**Note: Some zones may not support all instance types.<br>For more information, see <a href=''https://ww**

**w.alibabacloud.com/help/en/doc-detail/25378.html'' target=''_blank''><b><font color=''blue''>Instance fam**

**ilies</font></a>.'**

**Label:**

**en: Instance Type**

**InstancePassword:**

**Description:**

**en: 'The logon password of the ECS instance. The password must be 8 to 30 characters in length and co**

**ntain at least three of the following character types: uppercase letters, lowercase letters, digits, and speci**

**al characters ()~!@#$%^&_-+=|{}[]:;''<>,.?/.'**

**Type: String**

**Label:**

**en: Instance Password**

**NoEcho: true**

**AssociationProperty: ALIYUN::ECS::Instance::Password**

**ConstraintDescription:**

**en: 'The password must be 8 to 30 characters in length and contain at least three of the following char**

**acter types: uppercase letters, lowercase letters, digits, and special characters ()~!@#$%^&_-+=|{}[]:;''**

**<>,.?/.'**

**VSwitchCidrBlock:**

**Default: 192.168.0.0/24**

**Type: String**

**Description:**

**en: The IPv4 CIDR block of the vSwitch. The CIDR block must be a subnet of the VPC.**

**Label:**

**en: vSwitch IPv4 CIDR Block**

**InternetChargeType:**

**Default: PayByBandwidth**

**AssociationPropertyMetadata:**

**LocaleKey: InternetChargeType**

**Label:**

**en: IPv6 Internet Bandwidth Billing Method**

**Type: String**

**AllowedValues:**

  - **- PayByTraffic**
  - **- PayByBandwidth**

**IPV6Bandwidth:**

**Default: 10**

**Type: Number**

**Description:**

**en: 'The public bandwidth of the IPv6 gateway. Unit: Mbit/s. Valid values: 1 to 5000. If you set the billin**

**g method to pay-by-traffic, the value range is 1 to 2000. If you set the billing method to pay-by-bandwidth,**

**the value range is 1 to 5000.'**

**Label:**

**en: IPv6 Gateway Public Bandwidth**

**VSwitchZoneId:**

**AssociationProperty: ALIYUN::ECS::Instance:ZoneId**

**Type: String**

**Description:**

**en: 'The ID of the zone.**

**<b>Note: <font color=''blue''>Before you select a zone, make sure that the zone supports the ECS resourc**

**es that you want to create. We recommend that you select a zone that is different from the zones of other**

**vSwitches.</font>'**

**Label:**

**en: vSwitch Zone**

**InstancePublicIP:**

**Default: false**

**Type: Boolean**

**Description:**

**en: Specifies whether to assign a public IPv4 address.**

**Label:**

**en: Allocate Public IPv4 Address**

**IPV6GateWaySpec:**

**AssociationPropertyMetadata:**

**p**

**y**

**LocaleKey: NatGatewaySpec**

**Description:**

**en: 'The edition of the IPv6 gateway. Valid values: Small (Free Edition), Medium (Enterprise Edition), a**

**nd Large (Enterprise Enhanced Edition).'**

**Default: Small**

**Label:**

**en: IPv6 Gateway Specification**

**AllowedValues:**

  - **- Small**
  - **- Medium**
  - **- Large**

**Type: String**

**Outputs:**

**EcsInstanceId:**

**Description: EcsInstance InstanceId**

**Value:**

**Fn::GetAtt:**

  - **- EcsInstance**
  - **- InstanceId**

**EcsInstancePrivateIp:**

**Description: EcsInstance PrivateIp**

**Value:**

**Fn::GetAtt:**

  - **- EcsInstance**
  - **- PrivateIp**

**EcsInstanceIpv6Address:**

**Description: EcsInstance Ipv6Address**

**Value:**

**Fn::Select:**

  - **- '0'**
  - **- Fn::GetAtt:**
  - **- EcsAssignIpv6Addresses**
  - **- Ipv6Addresses**

**Conditions: {}**

**Resources:**

**EcsSecurityGroup:**

**Type: ALIYUN::ECS::SecurityGroup**

**Properties:**

**SecurityGroupIngress:**

  - **- Priority: 1**

**IpProtocol: tcp**

**NicType: intranet**

**SourceCidrIp: 0.0.0.0/0**

**PortRange: 3389/3389**

  - **- Priority: 1**

**IpProtocol: all**

**NicType: intranet**

**Ipv6SourceCidrIp: '::/0'**

**PortRange: '-1/-1'**

**VpcId:**

**Ref: EcsVpc**

**SecurityGroupEgress:**

  - **- Priority: 1**

**IpProtocol: tcp**

**DestCidrIp: 0.0.0.0/0**

**NicType: intranet**

**PortRange: 3389/3389**

  - **- Ipv6DestCidrIp: '::/0'**

**IpProtocol: all**

**Priority:1**

**Priority: 1**

**NicType: intranet**

**PortRange: '-1/-1'**

**WaitConditionHandle:**

**Type: ALIYUN::ROS::WaitConditionHandle**

**Properties: {}**

**VpcIpv6InternetBandwidth:**

**Type: ALIYUN::VPC::Ipv6InternetBandwidth**

**Properties:**

**InternetChargeType:**

**Ref: InternetChargeType**

**Bandwidth:**

**Ref: IPV6Bandwidth**

**Ipv6AddressId:**

**Fn::Select:**

  - **- Fn::GetAtt:**
  - **- EcsAssignIpv6Addresses**
  - **- Ipv6AddressIds**

**Ipv6GatewayId:**

**Ref: VpcIpv6Gateway**

**DependsOn:**

  - **- EcsAssignIpv6Addresses**
  - **- VpcIpv6Gateway**

**VpcIpv6Gateway:**

**Type: ALIYUN::VPC::Ipv6Gateway**

**Properties:**

**VpcId:**

**Ref: EcsVpc**

**Name: MyIpv6Gateway**

**Spec:**

**Ref: IPV6GateWaySpec**

**EcsAssignIpv6Addresses:**

**Type: ALIYUN::ECS::AssignIpv6Addresses**

**Properties:**

**NetworkInterfaceId:**

**Fn::GetAtt:**

  - **- EcsInstance**
  - **- PrimaryNetworkInterfaceId**

**Ipv6AddressCount: 1**

**DependsOn:**

  - **- EcsInstance**

**EcsVSwitch:**

**Type: ALIYUN::ECS::VSwitch**

**Properties:**

**Ipv6CidrBlock: 0**

**VpcId:**

**Ref: EcsVpc**

**CidrBlock:**

**Ref: VSwitchCidrBlock**

**ZoneId:**

**Ref: VSwitchZoneId**

**WaitCondition:**

**Type: ALIYUN::ROS::WaitCondition**

**Properties:**

**Count: 1**

**Handle:**

**Ref: WaitConditionHandle**

**Timeout: 900**

**EcsInstance:**

**Type: ALIYUN::ECS::Instance**

**Properties:**

**UserData:**

**Fn::Replace:**

  - **- ros-notify:**

**Fn::GetAtt:**

  - **- WaitConditionHandle**
  - **- CurlCli**
  - **- Fn::Join:**
  - **- ''**
  - **- - '#!/bin/sh'**
  - **- |2**
  - **- |**

**cd /opt**

  - **- |**

**wget http://ecs-image-utils.oss-cn-hangzhou.aliyuncs.com/ipv6/rhel/ecs-utils-ipv6**

  - **- |**

**chmod +x ./ecs-utils-ipv6**

  - **- |**

**./ecs-utils-ipv6**

  - **- |**

**ros-notify -d "{\"Data\" : \"SUCCESS\", \"Status\" : \"SUCCESS\"}"**

**SystemDiskCategory:**

**Ref: SystemDiskCategory**

**VpcId:**

**Ref: EcsVpc**

**SecurityGroupId:**

**Ref: EcsSecurityGroup**

**SystemDiskSize:**

**Ref: SystemDiskSize**

**ImageId:**

**Ref: InstanceImageId**

**AllocatePublicIP:**

**Ref: InstancePublicIP**

**VSwitchId:**

**Ref: EcsVSwitch**

**IoOptimized: optimized**

**Password:**

**Ref: InstancePassword**

**InstanceType:**

**Ref: InstanceType**

**DependsOn:**

  - **- EcsSecurityGroup**
  - **- EcsVSwitch**
  - **- EcsVpc**

**EcsVpc:**

**Type: ALIYUN::ECS::VPC**

**Properties:**

**CidrBlock:**

**Ref: VpcCidrBlock**

**VpcName:**

**Fn::Join:**

  - **- '-'**
  - **- - StackId**
  - **- Ref: ALIYUN::StackId**

**EnableIpv6: true**

**Metadata:**

**ALIYUN::ROS::Interface:**

**ParameterGroups:**

**ParameterGroups:**

  - **- Parameters:**
  - **- VpcCidrBlock**
  - **- VSwitchCidrBlock**
  - **- VSwitchZoneId**
  - **- InstanceType**
  - **- InstanceImageId**
  - **- SystemDiskSize**
  - **- InstancePublicIP**
  - **- InternetChargeType**
  - **- IPV6Bandwidth**
  - **- IPV6GateWaySpec**
  - **- SystemDiskCategory**
  - **- InstancePassword**

**Label:**

**default: ECS**

**Scenario 3: Create a VPC-type Classic Load Balancer (CLB) instance**

Quick create YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Description:
  en: Creates a VPC and a vSwitch, and configures an internal-facing Server Load Balancer (SLB) insta
nce. You can specify the instance type and address type. Parameters:
  VpcCidrBlock:
    Type: String
    Label:
      en: VPC CIDR Block
    Description:
      en: 'The IPv4 CIDR block of the VPC. You can use the following CIDR blocks or their subnets: 10
.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.'
    Default: 192.168.0.0/16
    AllowedValues:
      - 192.168.0.0/16
      - 172.16.0.0/12
      - 10.0.0.0/8
  VSwitchZoneId:
    Type: String
    Label:
      en: Zone ID
    Default: Null
    Description:
      en: The ID of the zone. Make sure that the zone supports SLB.
    AssociationProperty: ALIYUN::ECS::Instance::ZoneId
  VSwitchCidrBlock:
    Type: String
    Label:
      en: vSwitch CIDR Block
    Description:
      en: The CIDR block of the vSwitch. It must be a subnet of the VPC and cannot be in use by anoth
er vSwitch.
    Default: 192.168.0.0/24
  LoadBalancerSpec:
    Type: String
    Label:
      en: Specification
    Description:
      en: 'The specification of the SLB instance. For more information, see <a
```

`p` `,`

```
href=''https://help.aliyun.com/document_detail/85939.html'' target=''_blank''><font color=''blue''>SL
```

**B instance specifications**`</font>.</a>'`

```
    Default: slb.s1.small
Conditions: {} Resources:
  EcsVpc:
    Type: ALIYUN::ECS::VPC
    Properties:
      CidrBlock:
        Ref: VpcCidrBlock
      VpcName:
        Fn::Join:
          - '-'
          - - StackId
            - Ref: ALIYUN::StackId
  EcsVSwitch:
    Type: ALIYUN::ECS::VSwitch
    Properties:
      ZoneId:
        Ref: VSwitchZoneId
      VpcId:
        Ref: EcsVpc
      CidrBlock:
        Ref: VSwitchCidrBlock
      VSwitchName:
        Fn::Join:
          - '-'
          - - StackId
            - Ref: ALIYUN::StackId
  SlbLoadBalancer:
    Type: ALIYUN::SLB::LoadBalancer
    Properties:
      VpcId:
        Ref: EcsVpc
      VSwitchId:
        Ref: EcsVSwitch
      AddressType: intranet
      LoadBalancerName:
        Fn::Join:
          - '-'
          - - StackId
            - Ref: ALIYUN::StackId
      LoadBalancerSpec:
        Ref: LoadBalancerSpec
      PayType: PayOnDemand
    DependsOn: EcsVSwitch
Outputs:
  SlbLoadBalancerId:
    Description:
      en: The ID of the SLB instance.
    Value:
      Fn::GetAtt:
        - SlbLoadBalancer
        - LoadBalancerId
Metadata:
  ALIYUN::ROS::Interface:
    ParameterGroups:
      - Parameters:
          - VpcCidrBlock
          - VSwitchZoneId
          - VSwitchCidrBlock
        Label:
```

```
          default:
            en: VPC
      - Parameters:
          - LoadBalancerSpec
        Label:
          default:
            en: SLB
```

For more examples, see public templates that contain this resource.

#### ALIYUN::ECS::VSwitch

ALIYUN::ECS::VSwitch is used to create a vSwitch.

**Syntax**

```json
  "Type": "ALIYUN::ECS::VSwitch",
  "Properties": {
    "VSwitchName": String,
    "VpcId": String,
    "Description": String,
    "Tags": List,
    "Ipv6CidrBlock": Integer,
    "ZoneId": String,
    "CidrBlock": String,
    "VpcIpv6CidrBlock": String
```

**Properties**

|   | Property |   | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|---|---|
|   | VpcId |   | String | Yes | No | The ID of the virtual private cloud (VPC) in which you create the vSwitch. | None. |
|   | ZoneId |   | String | Yes | No | The ID of the zone. | None. |
|   | VSwitchNam e |   | String | No | Yes | The name of the vSwitch. | The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens _ (-). The name must start with a letter but cannot start with http:// or https:// . |
|   |   | VSwitchNam |   |   |   |   |   |
|   | e |   |   |   |   |   |   |
|   | CidrBlock |   | String | Yes | No | The CIDR block of the vSwitch. | The CIDR block of a vSwitch must be a subset of the CIDR block of the VPC to which the vSwitch belongs and cannot be used by other vSwitches. |
|   |   | CidrBlock |   |   |   |   |   |
|   | Descriptio n |   | String | No | Yes | The description of the vSwitch. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
|   |   | Descriptio |   |   |   |   |   |
|   | n |   |   |   |   |   |   |

|   | Ipv6CidrBl ock |   | Integer | No | No | The IPv6 CIDR block of the vSwitch. | Valid values: 0 to 255. The value must be a decimal integer. By default, the mask of the IPv6 CIDR block of the vSwitch is 64 bits in length. You can specify a custom content for the last eight bits of the mask of the IPv6 CIDR block of the VPC. |
|---|---|---|---|---|---|---|---|
|   |   | Ipv6CidrBl | In |   |   |   |   |
|   | ock |   |   |   |   |   |   |
|   | Tags |   | List | No | Yes | The tags. | You can specify up to 20 tags. For more information, see Tags properties. |
|   | VpcIpv6Cid rBlock |   | String | No | No | The IPv6 CIDR block of the VPC. | None. |
|   |   | VpcIpv6Cid | Strin |   |   |   |   |
|   | rBlock |   |   |   |   |   |   |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The key cannot start with aliyun or acs: . |
| Value | String | No | No | The tag value. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The value cannot start with aliyun or acs: . |

**Return values**

Fn::GetAtt CidrBlock: the CIDR block of the vSwitch. Ipv6CidrBlock: the IPv6 CIDR block of the vSwitch. VSwitchId: the ID of the vSwitch.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VSwitchZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": "The ID of the zone",
      "Label": {
        "en": "VSwitch Availability Zone"
```

`},`

```json
  "Resources": {
    "EcsVSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "VpcId": {
          "Ref": "EcsVpc"
```

`},`

```json
        "ZoneId": {
          "Ref": "VSwitchZoneId"
```

`},`

```json
        "CidrBlock": "192.168.0.0/24"
```

`},`

```json
    "EcsVpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": "192.168.0.0/16",
        "VpcName": {
          "Fn::Join": [
            "-",
```

`[`

```json
              "StackId",
                "Ref": "ALIYUN::StackId"
```

`]` `]` `},`

```json
  "Outputs": {
```

To view more examples, visit SnatEntry.json and SnatEntry.yml. In the examples, the ALIYUN::ECS::VPC, ALIYUN::ECS::VSwitch, ALIYUN::VPC::SnatEntry, ALIYUN::VPC::CommonBandwidthPackage, ALIYUN::VPC::CommonBandwidthPackageIp, ALIYUN::VPC::Ipv6Gateway, and ALIYUN::VPC::Ipv6InternetBandwidth resource types are used.

### ESS

#### ALIYUN::ESS::AlarmTask

ALIYUN::ESS::AlarmTask is used to create a metric-based alarm task.

**Syntax**

```json
  "Type": "ALIYUN::ESS::AlarmTask",
  "Properties": {
    "Statistics": String,
    "Name": String,
    "EvaluationCount": Integer,
    "Period": Integer,
    "MetricType": String,
    "ComparisonOperator": String,
    "Dimensions": List,
    "ScalingGroupId": String,
    "AlarmAction": List,
    "Threshold": Number,
    "MetricName": String,
    "GroupId": Integer,
    "Description": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Statistics | String | No | No | The method used to calculate monitoring data. The statistics must be appropriate for the metric chosen. | Valid values: Average, Minimum, and Maximum. Default value: Average. |
| Name | String | No | Yes | The name of the alarm rule. | None |
| EvaluationCount | Integer | No | No | The number of consecutive times that the threshold must be exceeded before an alarm is triggered. | Default value: 3. Minimum value: 1. |
| Period | Integer | No | No | The metric query period, which must be appropriate for the metric chosen. Unit: seconds. | Valid values: 60, 120, 300, and 900. Default value: 300. |
| MetricType | String | No | No | The metric type. | Valid values: system and custom. |
| ComparisonOpera tor | String | No | No | The alarm comparison operator used to define a condition in the alarm rule. | Valid values: <=, <, >, and > =. |
| Dimensions | List | No | No | The list of instances associated with the alarm rule. | You must include at least one instance in the list. |
| ScalingGroupId | String | Yes | No | The ID of the scaling group. | None |
| AlarmAction | List | Yes | Yes | The list of alarm actions. | You must include one to five alarm actions in the list. |
| Threshold | Number | Yes | No | The alarm threshold, which must be a numeric value. | None |

| MetricName | String | Yes | No | The metric name of a service. For more information, see the metrics defined for each service. | None |
|---|---|---|---|---|---|
| GroupId | Integer | No | No | The group ID. | None |
| Description | String | No | Yes | The description of the alarm task. | None |

**Dimensions syntax**

```json
"Dimensions": [
    "DimensionKey": String,
    "DimensionValue": String
```

`]`

**Dimensions properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DimensionValue | String | Yes | No | None | None |
| DimensionKey | String | Yes | No | None | None |

**Response parameters**

Fn::GetAtt AlarmTaskId: the ID of the alarm task.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AutoScalingGroupId:
    Type: String
    AssociationProperty: ALIYUN::ESS::AutoScalingGroup::AutoScalingGroupId
  AlarmAction:
    Type: CommaDelimitedList
    Description: Alarm Actions
    MinLength: 1
    MaxLength: 5
Resources:
  AlarmTask:
    Type: ALIYUN::ESS::AlarmTask
    Properties:
      ScalingGroupId:
        Ref: AutoScalingGroupId
      AlarmAction:
        - ari:acs:ess:cn-hangzhou:140692647406****:scalingrule/asr-bp1dvirgwkoowxk7****
      Threshold: 1
      MetricName: TestMetric
      MetricType: custom
      Statistics: Average
Outputs:
  AlarmTaskId:
    Description: The alarm task ID
    Value:
      Fn::GetAtt:
        - AlarmTask
        - AlarmTaskId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AutoScalingGroupId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ESS::AutoScalingGroup::AutoScalingGroupId"
```

`},`

```json
    "AlarmAction": {
      "Type": "CommaDelimitedList",
      "Description": "Alarm Actions",
      "MinLength": 1,
      "MaxLength": 5
```

`},`

```json
  "Resources": {
    "AlarmTask": {
      "Type": "ALIYUN::ESS::AlarmTask",
      "Properties": {
        "ScalingGroupId": {
          "Ref": "AutoScalingGroupId"
```

`},`

```json
        "AlarmAction": [
          "ari:acs:ess:cn-hangzhou:140692647406****:scalingrule/asr-bp1dvirgwkoowxk7****"
```

`],`

```json
        "Threshold": 1,
        "MetricName": "TestMetric",
        "MetricType": "custom",
        "Statistics": "Average"
```

`},`

```json
  "Outputs": {
    "AlarmTaskId": {
      "Description": "The alarm task ID",
      "Value": {
        "Fn::GetAtt": [
          "AlarmTask",
          "AlarmTaskId"
```

`]`

#### ALIYUN::ESS::AlarmTaskEnable

ALIYUN::ESS::AlarmTaskEnable is used to start an alarm task. You can call this operation to enable alarm tasks when the task is stopped.

**Statement**

```json
  "Type": "ALIYUN::ESS::AlarmTaskEnable",
  "Properties": {
    "AlarmTaskId": String,
    "Enable": Boolean
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AlarmTaskId | String | No | No | The ID of the monitoring task. | None |
| Enable | String | Retained | Yes | Specifies whether to enable the alarm task. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt None

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Enable": {
      "Type": "Boolean",
      "Description": "Enable alarm task or not",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]` `},`

```json
    "AlarmTaskId": {
      "Type": "String",
      "Description": "The id of alarm task."
```

`},`

```json
  "Resources": {
    "AlarmTaskEnable": {
      "Type": "ALIYUN::ESS::AlarmTaskEnable",
      "Properties": {
        "Enable": {
          "Ref": "Enable"
```

`},`

```json
        "AlarmTaskId": {
          "Ref": "AlarmTaskId"
```

`},`

```json
  "Outputs": {}
```

#### ALIYUN::ESS::LifecycleHook

ALIYUN::ESS::LifecycleHook is used to create a lifecycle hook for a scaling group.

**Syntax**

```json
  "Type": "ALIYUN::ESS::LifecycleHook",
  "Properties": {
    "LifecycleHookName": String,
    "NotificationArn": String,
    "HeartbeatTimeout": Integer,
    "NotificationMetadata": String,
    "ScalingGroupId": String,
    "DefaultResult": String,
    "LifecycleTransition": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LifecycleHookNa me | String | No | Yes | The name of the lifecycle hook. Each lifecycle hook name must be unique within a scaling group. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. The default name is the ID of the lifecycle hook. |
| NotificationArn | String | No | Yes | The Alibaba Cloud Resource Name (ARN) of the notification target that Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. | This target can be either an MNS queue or an MNS topic. The format of the parameter value is acs:ess:{region}: {account-id}:{resource- relative-id}. region : the region where the scaling group resides. account-id : the ID of the Apsara Stack tenant account. Examples: MNS queue: acs:ess: {region}:{account- id}:queue/{queuenam e} MNS topic: acs:ess: {region}:{account- id}:topic/{topicname} |
| HeartbeatTimeout | Integer | No | Yes | The waiting period before the lifecycle hook times out. When the lifecycle hook times out, the scaling group performs the action specified by the DefaultResult parameter. Unit: seconds. | Valid values: 30 to 21600. Default value: 600. |

| NotificationMetad ata | String | No |   |   | The fixed string to include when Auto Scaling sends a notification about the wait state of a scaling activity. Auto Scaling sends the specified NotificationMetadata parameter value along with the notification message so that you can easily categorize notifications. The NotificationMetadata parameter is valid only after you set the NotificationArn parameter. |   | The parameter value cannot exceed 128 characters in length. |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | NotificationMetadata |   |
|   |   |   |   | Yes |   |   |   |
|   |   |   |   |   |   | NotificationMetadata |   |
| ScalingGroupId | String | Yes |   | No | The ID of the scaling group. |   | None |
| DefaultResult | String | No |   | Yes | The action that the scaling group takes when the lifecycle hook times out. If the scaling group has multiple lifecycle hooks and one of them is terminated when the DefaultResult parameter is set to ABANDON during a scale-in event, the remaining lifecycle hooks in the same scaling group will also be terminated. Otherwise, the scaling activity will proceed normally after the waiting period expires and continue with the action specified by the DefaultResult parameter. |   | Valid values: CONTINUE: The scaling group continues the scale-in or scale-out event. ABANDON: The scaling group releases the created ECS instances if the scaling activity type is scale-out or removes the ECS instances to be scaled in if the scaling activity type is scale- in. Default value: CONTINUE. |
| LifecycleTransitio n | String | Yes |   | Yes | The type of scaling activity to which the lifecycle hook applies. |   | Valid values: SCALE OUT: scale-out _ events of the scaling group. SCALE IN: scale-in _ events of the scaling group. |

**Response parameters**

Fn::GetAtt LifecycleHookId: the ID of the lifecycle hook.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LifecycleHookName": {
      "Type": "String",
"Description":"Thenameofthelifecyclehook Eachnamemustbeuniquewithinascalinggroup
```

```json
      "Description": "The name of the lifecycle hook. Each name must be unique within a scaling group
. The name must be 2 to 40 characters in length and can contain letters, numbers, Chinese characters, and special characters including underscores (_), hyphens (-) and periods (.).\nDefault value: Lifecy cle Hook ID",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
```

`},`

```json
    "NotificationArn": {
      "Type": "String",
      "Description": "The Alibaba Cloud Resource Name (ARN) of the notification target that Auto Scal
ing will use to notify you when an instance is in the transition state for the lifecycle hook. This t arget can be either an MNS queue or an MNS topic. The format of the parameter value is acs:ess:{regio n}:{account-id}:{resource-relative-id}.\nregion: the region to which the scaling group locates\naccount-id: Alibaba Cloud ID\nFor example:\nMNS queue: acs:ess:{region}:{account-id}:queue/{ queuename}\nMNS topic: acs:ess:{region}:{account-id}:topic/{topicname}",
      "AllowedPattern": "^acs:ess:([a-zA-Z0-9-]+):(\\d+):(queue|topic)/([a-zA-Z0-9][a-zA-Z0-9-]
{0,255})$",
      "MaxLength": 300
```

`},`

```json
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
```

`},`

```json
    "LifecycleTransition": {
      "Type": "String",
      "Description": "The scaling activities to which lifecycle hooks apply Value range:\n SCALE_OUT:
scale-out event\n SCALE_IN: scale-in event",
      "AllowedValues": [
        "SCALE_OUT",
        "SCALE_IN"
```

`]` `},`

```json
    "HeartbeatTimeout": {
      "Type": "Number",
      "Description": "The time, in seconds, that can elapse before the lifecycle hook times out. If t
he lifecycle hook times out, the scaling group performs the default action (DefaultResult). The range is from 30 to 21,600 seconds. The default value is 600 seconds.\nYou can prevent the lifecycle hook f rom timing out by calling the RecordLifecycleActionHeartbeat operation. You can also terminate the li fecycle action by calling the CompleteLifecycleAction operation.",
      "MinValue": 30,
      "MaxValue": 21600
```

`},`

```json
    "NotificationMetadata": {
      "Type": "String",
      "Description": "The fixed string that you want to include when Auto Scaling sends a message abo
ut the wait state of the scaling activity to the notification target. The length of the parameter can be up to 128 characters. Auto Scaling will send the specified NotificationMetadata parameter along wi th the notification message so that you can easily categorize your notifications. The NotificationMetadata parameter will only take effect after you specify the NotificationArn parameter.
```

`",`

```json
      "MaxLength": 128
```

`},`

```json
    "DefaultResult": {
      "Type": "String",
      "Description": "The action that the scaling group takes when the lifecycle hook times out. Valu
e range:\n CONTINUE: the scaling group continues with the scale-in or scale-out process.\n ABANDON: t he scaling group stops any remaining action of the scale-in or scale-out event.\nDefault value: CONTI NUE\nIf the scaling group has multiple lifecycle hooks and one of them is terminated by the DefaultRe sult=ABANDON parameter during a scale-in event (SCALE_IN), the remaining lifecycle hooks under the sa me scaling group will also be terminated. Otherwise, the action following the wait state is the next action, as specified in the parameter DefaultResult, after the last lifecycle event under the same sc aling group.",
      "AllowedValues": [
        "CONTINUE",
```

```
        "ABANDON"
```

`]` `},`

```json
  "Resources": {
    "LifecycleHook": {
      "Type": "ALIYUN::ESS::LifecycleHook",
      "Properties": {
        "LifecycleHookName": {
          "Ref": "LifecycleHookName"
```

`},`

```json
        "NotificationArn": {
          "Ref": "NotificationArn"
```

`},`

```json
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
```

`},`

```json
        "LifecycleTransition": {
          "Ref": "LifecycleTransition"
```

`},`

```json
        "HeartbeatTimeout": {
          "Ref": "HeartbeatTimeout"
```

`},`

```json
        "NotificationMetadata": {
          "Ref": "NotificationMetadata"
```

`},`

```json
        "DefaultResult": {
          "Ref": "DefaultResult"
```

`},`

```json
  "Outputs": {
    "LifecycleHookId": {
      "Description": "The lifecycle hook ID",
      "Value": {
        "Fn::GetAtt": [
          "LifecycleHook",
          "LifecycleHookId"
```

`]`

#### ALIYUN::ESS::ScalingConfiguration

ALIYUN::ESS::ScalingConfiguration is used to create a scaling configuration for a scaling group.

**Statement**

```json
  "Type": "ALIYUN::ESS::ScalingConfiguration",
  "Properties": {
    "PasswordInherit": Boolean,
    "DiskMappings": List,
    "RamRoleName": String,
    "IoOptimized": String,
    "InternetChargeType": String,
    "KeyPairName": String,
    "InstanceId": String,
    "InstanceTypes": List,
    "ImageId": String,
    "ResourceGroupId": String,
    "SpotStrategy": String,
    "InstanceType": String,
    "SystemDiskCategory": String,
    "SystemDiskSize": Integer,
    "SystemDiskAutoSnapshotPolicyId": String,
    "InternetMaxBandwidthOut": Integer,
    "InstanceName": String,
    "InternetMaxBandwidthIn": Integer,
    "ScalingConfigurationName": String,
    "UserData": String,
    "DeploymentSetId": String,
    "SecurityGroupId": String,
    "SpotPriceLimit": Number,
    "HpcClusterId": String,
    "ScalingGroupId": String,
    "SpotPriceLimitForInstanceType": Map,
    "TagList": List
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | Yes | True | The ID of the resource group to which the instance belongs. | None |
| DeploymentSetId | String | Yes | Released | The ID of the deployment set. | None |
| HpcClusterId | String | Yes | Released | The ID of the E-HPC cluster to which the instance belongs. | None |
| ScalingGroupId | String | No | No | The ID of the scaling group to which the scaling configuration belongs. | None |
| DiskMappings | List | No. | True | The disks to be attached to created instances. | A maximum of 16 disks can be attached to each instance. |
| InternetChargeTy pe | String | Yes | True | The billing method for Internet usage. | Valid values: PayByBandwidth PayByTraffic: pay-by- traffic Default value: PayByTraffic |

| Resource Orchestr | ation Servic | e |   | Us | er Guide·Resource type |
|---|---|---|---|---|---|

| InternetMaxBand widthIn | String | Optional | Released | The maximum inbound bandwidth from the Internet. | Unit: Mbit/s. Valid values: 1 to 100. Default value: 100 |
|---|---|---|---|---|---|
| InternetMaxBand widthOut | String | No. | True | The maximum outbound bandwidth to the Internet. | Valid values: Pay-by-bandwidth: 0 to 100. Default value: 0. Pay-by-data-transfer: 1 to 200. This parameter is required. Unit: Mbit/s. |
| InstanceId | String | Yes | Released | The instance ID of the scaling configuration. | None |
| SystemDiskCateg ory | String | Yes | True | The category of the system disk. | Valid values: cloud: indicates a basic disk. cloud efficiency: _ indicates an ultra disk. cloud ssd: indicates a _ standard SSD. ephemeral ssd: _ indicates a local SSD. cloud essd: enhanced _ SSD (ESSD) Default value: cloud for Generation I instance types that are not I/O optimized, default value: cloud efficiency. _ |
| ImageId | String | Yes | True | The ID of the image used to start the instance. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | None |
| InstanceType | String | Yes | True | The specification of the instance. | None |
| SecurityGroupId | String | Yes | True | The ID of the security group to which the instance belongs. | None |
| IoOptimized | String | Yes | True | Specifies whether the created instances are I/O optimized. | Valid values: none (non-I/O optimized) optimized Default value: none. |

| ScalingConfigurati onName | String | Yes | True | The name of the scaling configuration. | The name must be 2 to 64 characters in length. It can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. The name of the scaling configuration must be unique within a scaling group. If this parameter is not specified, the value of scalingconfigurationid is used. |
|---|---|---|---|---|---|
| KeyPairName | String | Yes | True | The name of the key pair that is bound to the instance. | This parameter is ignored if the instance type is Windows and the default value is null. If the instance type is Linux, password logon is disabled by default. |
| RamRoleName | String | Yes | True | The RAM role name of the instance. | You can use RAM API ListRoles you can call this operation to query the RAM role name of an instance. |
| SystemDiskSize | String | No. | True | The size of the system disk. Unit: GB. | Valid values: 40 to 500. Unit: GB. If a custom image is used to create a system disk, the system disk size must be larger than the size of the custom image. |
| UserData | String | Yes | True | The user data that you pass when you create the instance. | The user can encode up to 16KB in size. You do not need to perform Base64 encoding. Special characters must be escaped with a backslash (\). |
| InstanceTypes | List | No. | True | The instance types from which ECS instances can be created. If you specify InstanceTypes, InstanceType is invalid. | Up to 10 instance types can be configured in a scaling configuration. The priority of each instance type is decreased in the order of its list elements. Auto Scaling creates instances in order of priority. If an instance of the highest priority type cannot be created, Auto Scaling will create an instance of the next highest priority type. |

| PasswordInherit | Boolean | No. |   | True |   | Specifies whether to use the preconfigured password of the specified image. |   | To use this parameter, ensure that a password is configured for the specified image. |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| TagList | List | No. |   |   |   |   |   | Tags must be specified as key-value pairs. You can specify a maximum of five Tag groups in the format of {"key1": |   |   |
|   |   |   |   |   |   |   |   |   | {"key1": |   |
|   |   |   |   |   |   |   |   | "value1", "key2": |   |   |
|   |   |   |   |   |   |   |   | "value2", ... "key5": |   |   |
|   |   |   |   |   |   |   |   | "value5"} |   |   |
|   |   |   |   | True |   | The tags of the instance. |   |   |   |   |
| SpotStrategy | String | Yes |   | True |   | The preemption policy for pay-as-you-go instances. |   | Valid values: NoSpot (pay-as-you-go instance) SpotWithPriceLimit (a preemptible instance with a maximum price) SpotAsPriceGo (the SpotAsPriceGo parameter that is set automatically based on the actual market price.) Default value: NoSpot. |   |   |
| InstanceName | String | Yes |   | True |   | The name of the instance created based on the current scaling configuration. |   | None |   |   |
| SpotPriceLimit | Number | No. |   | True |   | The maximum hourly price of the instance. |   | A maximum of three decimal places can be specified. This parameter takes effect only when the SpotStrategy parameter is set to SpotWithPriceLimit. The value of this parameter can be overwritten by the value of the SpotPriceLimitForInstanc eType parameter. |   |   |

| SpotPriceLimitForI nstanceType |   |   |   |   |   |   |   |   |   | The format is {" |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | {" |
|   |   |   |   |   |   |   |   |   |   | <instance type 1>": _ _ |   |
|   |   |   |   |   |   |   |   |   |   | <price limit 1>, ..., _ _ |   |
|   |   |   |   |   |   |   |   |   |   | {" |   |
|   |   |   |   |   |   |   |   |   |   | <instance type 10>": _ _ |   |
|   | tForI | Map | No. |   |   |   | Preemptible instance |   |   |   |   |
|   |   |   |   |   |   | True | type and bid of the |   |   | <price limit 10>} _ _ |   |
|   |   |   |   |   |   |   | instance. |   |   |   |   |
| SystemDiskAutoS napshotPolicyId |   | String | Yes |   |   | True | The ID of the automatic snapshot policy applied to the data disk. |   |   | None |   |

**DiskMappings syntax**

```json
"DiskMappings": [
    "Category": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String,
    "Encrypted": String,
    "KMSKeyId": String,
    "Description": String,
    "DiskName": String
```

`]`

**DiskMappings properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of the data disk. | Valid values: cloud: 5 to 2000 cloud efficiency: 20 to _ 32768 cloud ssd: 20 to 32768 _ cloud essd: 20 to _ 32768. ephemeral ssd: 5 to 800 _ The value of this parameter must be greater than or equal to that of the snapshot specified by SnapshotId. Unit: GiB. |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, ephemeral ssd, _ _ and cloud essd. For I/O _ optimized instances, the default value is cloud efficiency. For non- _ I/O optimized instances, the default value is cloud. |

| DiskName | String | Yes | Released | The name of the data disk. | The name must be 2 to 128 characters in length It can contain letters, digits, colons (:), underscores ( ), _ and hyphens (-). It must start with a letter and cannot start with http:// or https:// the beginning. |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the data disk. | The description must be 2 to 256 characters in length. Cannot http:// or https:// the beginning. |
| Device | String | Yes | Released | The device name of the data disk. | By default, the system automatically assigns a value for this parameter when the ECS instance is created. The value starts from /dev/xvdb and ends at /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | If this parameter is specified, the Size parameter will be ignored, and the Size of the created disk will be the Size of the specified snapshot. If the snapshot was created on or before July 15, 2013, calling the snapshot is denied and InvalidSnapshot.TooOld is displayed in the response parameter. |
| Encrypted | String | Yes | Released | Specifies whether to encrypt the data disk. | Default value: false. |
| KMSKeyId | String | Yes | Released | The KMS key ID for data disk N. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt ScalingConfigurationId: the ID of the scaling configuration. This ID is a globally unique identifier (GUID) generated by the system.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingConfiguration": {
      "Type": "ALIYUN::ESS::ScalingConfiguration",
      "Properties": {
        "ImageId": "ubuntu1404_64_20G_aliaegis_2015****.vhd",
        "InstanceType": "ecs.t1.small",
        "InstanceId": "i-25xhh****",
        "InternetChargeType": "PayByTraffic",
        "InternetMaxBandwidthIn": 1,
        "InternetMaxBandwidthOut": 20,
        "SystemDisk_Category": "cloud",
        "ScalingGroupId": "bwhtvpcBcKYac9fe3vd0****",
        "SecurityGroupId": "sg-25zwc****",
        "DiskMappings": [
            "Size": 10
```

`},`

```json
            "Category": "cloud",
            "Size": 10
```

`]` `},`

```json
  "Outputs": {
    "ScalingConfiguration": {
      "Value": {"get_attr": ["ScalingConfigurationId"]}
```

#### ALIYUN::ESS::ScalingGroup

ALIYUN::ESS::ScalingGroup creates a scaling group, a collection of ECS instances for the same application scenario. The group does not take effect until you enable it with ALIYUN::ESS::ScalingGroupEnable to trigger scaling activities and execute scaling rules.

**Syntax**

```json
  "Type": "ALIYUN::ESS::ScalingGroup",
  "Properties": {
    "MultiAZPolicy": String,
    "DesiredCapacity": Integer,
    "NotificationConfigurations": List,
    "ProtectedInstances": List,
    "LaunchTemplateId": String,
    "LaunchTemplateVersion": String,
    "ScalingGroupName": String,
    "VSwitchIds": List,
    "DefaultCooldown": Integer,
    "MinSize": Integer,
    "GroupDeletionProtection": Boolean,
    "MaxSize": Integer,
    "InstanceId": String,
    "VSwitchId": String,
    "LoadBalancerIds": List,
    "StandbyInstances": List,
    "RemovalPolicys": List,
    "HealthCheckType": String,
    "DBInstanceIds": List,
    "Tags": List,
    "OnDemandPercentageAboveBaseCapacity": Integer,
    "CompensateWithOnDemand": Boolean,
    "ContainerGroupId": String,
    "ScalingPolicy": String,
    "SpotInstanceRemedy": Boolean,
    "SpotInstancePools": Integer,
    "OnDemandBaseCapacity": Integer,
    "GroupType": String,
    "LaunchTemplateOverrides": List,
    "AllocationStrategy": String,
    "AzBalance": Boolean,
    "MaxInstanceLifetime": Integer,
    "CustomPolicyARN": String,
    "SpotAllocationStrategy": String,
    "HealthCheckTypes": List,
    "ServerGroups": List,
    "ResourceGroupId": String
```

**Properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| MinSize | Integer | Yes | Yes | The minimum number of ECS instances in the scaling group. | Valid values: 0 to 1000. Auto Scaling automatically creates instances when the count falls below this value. |
| MaxSize | Integer | Yes | Yes | The maximum number of ECS instances in the scaling group. | Valid values: 0 to 1000. Auto Scaling automatically removes instances when the count exceeds this value. |

| ScalingGroup Name | String | No | Yes | The display name of the scaling group. | The name must be 2 to 64 characters in length. It must start with a digit, a letter, or a Chinese character. It can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), and periods (.). _ The name must be unique within the same region and under the same Alibaba Cloud account. Default value: the ID of the scaling group. |
|---|---|---|---|---|---|
| LaunchTempl ateId | String | No | Yes | The ID of the launch template used for instance creation. | None |
| LaunchTempl ateVersion | String | No | Yes | The version of the ECS launch template. | Valid values: A fixed template version number. Default: The default version of the template is always used. Latest: The latest version of the template is always used. |
| RemovalPolic ys | List | No | Yes | The policies for removing ECS instances from the scaling group. | Valid values: OldestInstance (Default): Removes the ECS instance that was added to the scaling group at the earliest point in time. NewestInstance: Removes the ECS instance that was added to the scaling group at the latest point in time. OldestScalingConfiguration (Default): Removes ECS instances that are created based on the earliest scaling configuration. |
| VSwitchId | String | No | Yes | The ID of the vSwitch. | None |
| LoadBalancer Ids | List | No | Yes | The IDs of the SLB instances. | JSON array of up to five SLB instance IDs, separated by commas (,). |

| DefaultCoold own | Integer | No | Yes | The cooldown time after a scaling activity is complete. | Valid values: 0 to 86,400. Unit: seconds. Default value: 300. During cooldown, the scaling group rejects other scaling activities. Applies only to activities triggered by CloudMonitor event-triggered tasks. |
|---|---|---|---|---|---|
| DBInstanceId s | List | No | Yes | The IDs of the ApsaraDB RDS instances. | JSON array of up to eight RDS instance IDs, separated by commas (,). |
| VSwitchIds | List | No | Yes | The IDs of multiple vSwitches. | Up to five vSwitch IDs. Overrides VSwitchId when both are specified. vSwitches are prioritized in order; if instance creation fails in a higher- priority zone, the next vSwitch is used. |
| MultiAZPolicy | String | No | Yes | The scaling policy for ECS instances in a multi-zone scaling group. | Valid values: PRIORITY: Scales instances based on the vSwitches you define. If an ECS instance cannot be created in the zone where a higher-priority vSwitch is located, the next- priority vSwitch is automatically used. BALANCE: Evenly distributes ECS instances across the zones specified for the scaling group. COST OPTIMIZED: Creates _ instances by ascending vCPU unit price. Prioritizes spot instances when multiple instance types use spot billing. Falls back to pay-as- you-go instances if spot instances are unavailable. |
| NotificationC onfigurations | List | No | Yes | Event and resource change notification configuration s. | NotificationConfigurations properties. |
| ProtectedInst ances | List | No | Yes | The number of protected ECS instances in the scaling group. | You can specify up to 1,000 instances. |

| StandbyInsta nces | List | No | Yes | The number of standby ECS instances in the scaling group. | You can specify up to 1,000 instances. |
|---|---|---|---|---|---|
| HealthCheckT ypes | List | No | Yes | Health check types for the scaling group. | Valid values: NONE: No health checks are performed. ECS: Performs health checks on instances in the scaling group. This value is used to enable instance health checks for both ECS and ECI scaling groups. LOAD BALANCER: _ Determines the health status of an instance based on the health check results of the load balancer. CLB is not supported. |
| HealthCheckT ype | String | No | Yes | The health check type. | Valid values: ECS NONE |
| GroupDeletio nProtection | Boolean | No | Yes | Enables or disables deletion protection for the scaling group. | Valid values: true: Enables deletion protection. The scaling group cannot be deleted. false (Default): Disables deletion protection. |
| DesiredCapac ity | Integer | No | Yes | The expected number of ECS instances in the scaling group. Auto Scaling maintains the instance count at this value. | The value must be greater than or equal to MinSize and less than or equal to MaxSize. |
| InstanceId | String | No | No | The ID of an ECS instance from which the system derives a scaling configuration during group creation. | None |
| Tags | List | No | Yes | The tags. | You can add up to 20 tags. Tags properties. |

| OnDemandPe rcentageAbov eBaseCapacit y | Integer | No | Yes | The percentage of on-demand instances among the instances that exceed the base capacity. | After meeting OnDemandBaseCapacity, this percentage applies to additional instances beyond the base. Valid values: 0 to 100. |
|---|---|---|---|---|---|
| Compensate WithOnDema nd | Boolean | No | Yes | Whether to create on- demand instances to meet the required ECS instance count. | Effective only when MultiAZPolicy is COST OPTIMIZED. Creates on- _ demand instances when spot instances are unavailable due to price or inventory constraints. Valid values: true (Default): Yes. false: No. |
| ContainerGro upId | String | No | No | The ID of the ECI instance. | None |
| ScalingPolicy | String | No | No | The reclamation mode of the scaling group. | Valid values: recycle: The instances are stopped. release: The instances are released. ScalingPolicy sets the reclamation mode. The actual removal behavior is determined by the RemovePolicy parameter of RemoveInstances. |
| SpotInstance Remedy | Boolean | No | Yes | Enables supplemental spot instances. | Valid values: true: Enables supplemental spot instances. When enabled, the scaling group creates a replacement instance when a spot instance is about to be reclaimed. false: Disables supplemental spot instances. |
| SpotInstance Pools | Integer | No | Yes | The number of available instance types. | The scaling group balances spot instances across the lowest-cost instance types. Valid values: 1 to 10. |
| OnDemandBa seCapacity | Integer | No | Yes | The minimum number of on-demand instances required by the scaling group. | Valid values: 0 to 1000. The system prioritizes on- demand instance creation when the count is below this value. |

| GroupType | String | No | No | The type of instances managed by the scaling group. | Valid values: ECS (Default): The scaling group manages ECS instances. ECI: The scaling group manages ECI instances. |
|---|---|---|---|---|---|
| LaunchTempl ateOverrides | List | No | Yes | Instance type overrides that extend the launch template. | None |
| AllocationStra tegy | String | No | Yes | The capacity allocation policy. | Determines how the scaling group selects instance types to meet capacity requirements. Applies to both on-demand and preemptible capacity. Effective only when MultiAZPolicy is COMPOSABLE . Valid values: priority (Default): Creates instances in the order of the configured instance types. lowestPrice: Creates instances in ascending order of the vCPU unit price of the instance types. |
| AzBalance | Boolean | No | Yes | Evenly distributes the scaling group capacity across multiple zones. | Effective only when MultiAZPolicy is COMPOSABLE . Valid values: true: The capacity of the scaling group is evenly distributed across multiple zones. false (Default): The capacity of the scaling group is not evenly distributed across multiple zones. |
| MaxInstanceL ifetime | Integer | No | Yes | The maximum lifetime of an instance in the scaling group. | Unit: seconds. Valid values: 86400 to Integer.maxValue . Default value: null. |
| CustomPolicy ARN | String | No | Yes | The ARN of the custom scale-in policy function. | This parameter is effective only when the first removal policy in RemovalPolicies is set to CustomPolicy. |

|   | MultiAZPolicy |
|---|---|
| COMPOSABLE |   |

| SpotAllocatio nStrategy | String | No | Yes | The allocation policy for spot capacity. | Distribution strategy for spot capacity. Effective only when MultiAZPolicy is COMPOSABLE . Valid values: priority (Default): Creates instances in the order of the configured instance types. lowestPrice: Creates instances in ascending order of the vCPU unit price of the instance types. |
|---|---|---|---|---|---|
| ServerGroups | List | No | No | Server Load Balancer server group configuration s. | ServerGroups properties. |
| ResourceGro upId | String | No | Yes | The ID of the resource group. | None |

**ServerGroups syntax**

```json
"ServerGroups": [
    "Type": String,
    "ServerGroupId": String,
    "Weight": Number,
    "Port": Number
```

`]`

**ServerGroups properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| Type | String | Yes | No | The Server Load Balancer server group type. | Valid values: ALB: Application Load Balancer. NLB: Network Load Balancer. |
| ServerGroupI d | String | Yes | No | The Server Load Balancer server group ID. | None |

| Weight | Number | Yes | No | The weight of the ECS or ECI instance as a backend server. | Valid values: 0 to 100. A higher weight means more requests are routed to the instance. A weight of 0 means the instance receives no requests. |
|---|---|---|---|---|---|
| Port | Number | Yes | No | The port number of the backend ECS or ECI instance. | Valid values: 1 to 65535. |

**NotificationConfigurations syntax**

```json
"NotificationConfigurations": [
    "NotificationArn": String,
    "NotificationTypes": List
```

`]`

**NotificationConfigurations properties**

| Property name | Type | Required | Updatable |   | Description | Constraints |   |   |
|---|---|---|---|---|---|---|---|---|
| NotificationAr n | String | Yes | No |   | The notification recipient for lifecycle | Valid values: SMQ queue format: acs:ess:{region}: |   |   |
|   |   |   |   |   |   |   | acs:ess:{region}: |   |
|   |   |   |   |   | hooks. | {account- |   |   |
|   |   |   |   |   | Supports Simple | id}:queue/{queuename} |   |   |
|   |   |   |   |   | Message Queue |   |   |   |
|   |   |   |   |   |   |   | acs:ess:{region}: |   |
|   |   |   |   |   | (formerly | {account- |   |   |
|   |   |   |   |   | MNS) queues |   |   |   |
|   |   |   |   |   | or topics. | id}:topic/{topicname} |   |   |
| NotificationTy pes | List | Yes | No |   | Notification types for Auto Scaling events and resource changes. | None |   |   |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property name | Type | Required | Updatable | Description | Constraints |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The key must be 1 to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | The value can be 0 to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https:// . |

**LaunchTemplateOverrides syntax**

```json
"LaunchTemplateOverrides": [
    "InstanceType": String,
    "WeightedCapacity": Integer,
    "SpotPriceLimit": Number
```

`]`

**LaunchTemplateOverrides properties**

| Property name | Type | Required | Updatable |   | Description | Constraints |   |   |
|---|---|---|---|---|---|---|---|---|
| InstanceType | String | No | Yes |   |   | To scale based on instance type capacity, specify both this parameter and LaunchTemplateOverrides.We ightedCapacity . Overwrites the instance type in the launch template. Note This parameter is effective only when a launch template is specified by the LaunchTemplateId parameter. |   |   |
|   |   |   |   |   |   |   | LaunchTemplateOverrides.We |   |
|   |   |   |   |   |   | ightedCapacity |   |   |
|   |   |   |   |   | The ECS instance type. |   |   |   |

| WeightedCap acity | Integer | No | Yes |   |   | To scale based on instance type capacity, specify LaunchTemplateOverrides.In stanceType and this parameter. Represents the capacity of a single instance of this type. A higher weight means fewer instances are needed to meet the expected capacity. Set weights based on performance metrics such as vCPU count and memory size. For example: Current capacity: 0. Expected capacity: 6. Capacity of ecs.c5.xlarge: 4. To meet the expected capacity, the scaling group will scale out two ecs.c5.xlarge instances. Valid values: 1 to 500. Note During a scale-out, the scaling group capacity cannot exceed MaxSize plus the maximum weight of a single instance type. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | LaunchTemplateOverrides.In |   |
|   |   |   |   |   |   | stanceType |   |   |
|   |   |   |   |   | The weight of the instance type. |   |   |   |
| SpotPriceLimi t | Number | No | Yes |   |   | Maximum price for a spot instance of the type specified by LaunchTemplateOverrides.In stanceType . Note This parameter is effective only when a launch template is specified by the LaunchTemplateId parameter. |   |   |
|   |   |   |   |   |   |   | LaunchTemplateOverrides.In |   |
|   |   |   |   |   |   | stanceType |   |   |
|   |   |   |   |   | The maximum price for a spot instance. |   |   |   |

**Return value**

Fn::GetAtt ScalingGroupId: The ID of the scaling group. ScalingGroupName: The name of the scaling group. Arn: The Alibaba Cloud Resource Name (ARN).

**Examples**

YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VSwitch:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    Label:
      zh-cn: VSwitch ID
      en: VSwitch ID
  LaunchTemplateId:
    AssociationProperty: ALIYUN::ECS::LaunchTemplate::LaunchTemplateId
    Type: String
Resources:
  ScalingGroup:
    Type: ALIYUN::ESS::ScalingGroup
    Properties:
      VSwitchId:
        Ref: VSwitch
      LaunchTemplateId:
        Ref: LaunchTemplateId
      MaxSize: 3
      ScalingGroupName: TestScalingGroup
      MinSize: 0
Outputs:
  ScalingGroupId:
    Description: The ID of the scaling group.
    Value:
      Fn::GetAtt:
        - ScalingGroup
        - ScalingGroupId
  ScalingGroupName:
    Description: The name of the scaling group.
    Value:
      Fn::GetAtt:
        - ScalingGroup
        - ScalingGroupName
```

When a scaling group has only one scaling configuration that depends on other resources, set DependsOn on the scaling group to create the required resource dependency. In this example, ScalingGroup depends on SecurityGroup because ScalingConfiguration requires it.

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VpcId:
    AssociationProperty: ALIYUN::ECS::VPC::VPCId
    Type: String
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    Type: String
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
Resources:
  ScalingGroupEnable:
    Type: ALIYUN::ESS::ScalingGroupEnable
    Properties:
      ScalingConfigurationId:
        Ref: ScalingConfiguration
      ScalingGroupId:
        Ref: ScalingGroup
      ScalingRuleArisExecuteVersion: 0
  SecurityGroup:
    Type: ALIYUN::ECS::SecurityGroup
Properties:
```

```
    Properties:
      SecurityGroupName:
        Ref: ALIYUN::StackName
      VpcId:
        Ref: VpcId
      SecurityGroupIngress:
        - PortRange: '-1/-1'
          Priority: 1
          SourceCidrIp: 0.0.X.X/0
          IpProtocol: all
          NicType: internet
      SecurityGroupEgress:
        - PortRange: '-1/-1'
          Priority: 1
          IpProtocol: all
          DestCidrIp: 0.0.X.X/0
          NicType: internet
        - PortRange: '-1/-1'
          Priority: 1
          IpProtocol: all
          DestCidrIp: 0.0.X.X/0
          NicType: intranet
  ScalingConfiguration:
    Type: ALIYUN::ESS::ScalingConfiguration
    DependsOn: ScalingGroup
    Properties:
      InstanceType: ecs.g6e.large
      ImageId: centos_7_04_64_20G_alibase_201701015.vhd
      SystemDiskCategory: cloud_essd
      SystemDiskSize: 100
      ScalingConfigurationName:
        Ref: ALIYUN::StackName
      ScalingGroupId:
        Ref: ScalingGroup
      SecurityGroupId:
        Ref: SecurityGroup
  ScalingGroup:
    Type: ALIYUN::ESS::ScalingGroup
    DependsOn: SecurityGroup
    Properties:
      MaxSize: 3
      MinSize: 0
      DefaultCooldown: 15
      VSwitchId:
        Ref: VSwitchId
Outputs: {}
```

#### ALIYUN::ESS::ScalingGroupEnable

ALIYUN::ESS::ScalingGroupEnable is used to enable a scaling group.

**Syntax**

```json
  "Type": "ALIYUN::ESS::ScalingGroupEnable",
  "Properties": {
    "ScalingConfigurationId": String,
    "ScalingRuleArisExecuteVersion": Integer,
    "ScalingRuleAris": List,
    "ScalingGroupId": String,
    "RemoveInstanceIds": List,
    "InstanceIds": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingGroupId | String | Yes | No | The ID of the scaling group. | None |
| ScalingConfigura tionId | String | No | No | The ID of the scaling configuration to be activated in the scaling group. | None |
| InstanceIds | List | No | Yes | The IDs of ECS instances to be added to the enabled scaling group. | A maximum of 20 instance IDs can be specified. |
| ScalingRuleArisE xecuteVersion | Integer | No | Yes | The version of the identifier for the scaling rule to be executed. If you change this property, all scaling rules specified by ScalingRuleAris will be executed once. | Minimum value: 0. |
| ScalingRuleAris | List | No | Yes | The unique identifiers of scaling rules in the scaling group. Invalid unique identifiers are not displayed in the query results and no errors are reported. | A maximum of 10 scaling rule identifiers can be specified. |
| RemoveInstance Ids | List | No | Yes | The IDs of ECS instances to be deleted. | A maximum of 1,000 instance IDs can be specified. |

**Response parameters**

Fn::GetAtt LifecycleState: the status of the scaling group. ScalingInstances: the instances that are automatically created in the scaling group. ScalingGroupId: the ID of the scaling group. ScalingRuleArisExecuteResultInstancesRemoved: the instances that are removed from the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultNumberOfAddedInstances: the number of instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingInstanceDetails: the instance scaling details. ScalingRuleArisExecuteErrorInfo: the error information about the execution of the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultInstancesAdded: the instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris.

**Examples**

| YAML | format |
|---|---|
| ROSTemplateFormatVersion: '2015-09-01' Resources: ScalingGroupEnable: Type: ALIYUN::ESS::ScalingGroupEnable Properties: ScalingGroupId: r0HUqbJ411cc2eQw8bU**** ScalingConfigurationId: bJlLfdexm77Ldsyptmel**** InstanceIds: '' Outputs: ScalingGroupEnable: Value: Fn::GetAtt: - ScalingGroupEnable - LifecycleState |   |

| JSON | format |
|---|---|
| { "ROSTemplateFormatVersion": "2015-09-01", "Resources": { "ScalingGroupEnable": { "Type": "ALIYUN::ESS::ScalingGroupEnable", "Properties": { "ScalingGroupId": "r0HUqbJ411cc2eQw8bU****", "ScalingConfigurationId": "bJlLfdexm77Ldsyptmel****", "InstanceIds": "", } } }, "Outputs": { "ScalingGroupEnable": { "Value": {"Fn::GetAtt": ["ScalingGroupEnable", "LifecycleState"]} } } } |   |

#### ALIYUN::ESS::ScalingRule

ALIYUN::ESS::ScalingRule is used to create a scaling rule.

**Syntax**

```json
  "Type": "ALIYUN::ESS::ScalingRule",
  "Properties": {
    "AdjustmentValue": Integer,
    "Cooldown": Integer,
    "ScalingGroupId": String,
    "AdjustmentType": String,
    "ScalingRuleName": String,
    "MetricName": String,
    "PredictiveTaskBufferTime": Integer,
    "ScalingRuleType": String,
    "PredictiveValueBuffer": Integer,
    "TargetValue": Number,
    "StepAdjustment": List,
    "PredictiveValueBehavior": String,
    "DisableScaleIn": Boolean,
    "InitialMaxSize": Integer,
    "MinAdjustmentMagnitude": Integer,
    "EstimatedInstanceWarmup": Integer,
    "PredictiveScalingMode": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AdjustmentVal ue | Integer | No | Yes | The number of ECS instances to increase or decrease when scaling occurs. This parameter takes effect only when the ScalingRuleTyp e parameter is set to SimpleScaling Rule or StepScalingRul e. | Valid values based on the AdjustmentType value: Valid values when the AdjustmentType parameter is set to QuantityChangeInCap acity: -500 to 500 Valid values when the AdjustmentType parameter is set to PercentChangeInCapa city: - 100 to 10000 Valid values when the AdjustmentType parameter is set to TotalCapacity: 0 to 1000 Note The number of ECS instances to be adjusted in a single scaling activity cannot exceed 500. |
| Cooldown | Integer | No | Yes | The cooldown period of the scaling rule. This parameter takes effect only when the ScalingRuleTyp e parameter is set to SimpleScaling Rule. | Valid values: 0 to 86400. Unit: seconds. This parameter is empty by default. |

| ScalingGroupId | String | Yes | No | The ID of the scaling group to which the scaling rule belongs. | None |
|---|---|---|---|---|---|
| AdjustmentTyp e | String | No | Yes | The adjustment method of the scaling rule. This parameter takes effect only when the ScalingRuleTyp e parameter is set to SimpleScaling Rule or StepScalingRul e. | Valid values: QuantityChangeInCap acity: increases or decreases the specified number of ECS instances in a scaling group. PercentChangeInCapa city: increases or decreases the specified percentage of ECS instances in a scaling group. TotalCapacity: increases or decreases the number of ECS instances in a scaling group by or to a specific number. |
| ScalingRuleNa me | String | No | Yes | The name of the scaling rule. | The name must be 2 to 64 characters in length and can contain digits, letters, underscores ( ), _ hyphens (-), and periods (.). It must start with a digit or letter. If this parameter is not specified, the ScalingRuleId value is used by default. |

| MetricName | String | No | No | The predefined metric to monitor. This parameter is required and applicable only when the ScalingRuleTyp e parameter is set to TargetTracking ScalingRule or PredictiveScali ngRule. | Valid values when the ScalingRuleType parameter is set to TargetTrackingScaling Rule: CpuUtilization: the average CPU utilization ClassicInternetRx: the average Internet inbound traffic over the classic network ClassicInternetTx: the average Internet outbound traffic over the classic network VpcInternetRx: the average Internet inbound traffic over the VPC VpcInternetTx: the average Internet outbound traffic over the VPC IntranetRx: the average inbound traffic over the internal network IntranetTx: the average outbound traffic over the internal network Valid values when the ScalingRuleType parameter is set to PredictiveScalingRule: CpuUtilization: the average CPU utilization IntranetRx: the average inbound traffic over the internal network IntranetTx: the average outbound traffic over the internal network |
|---|---|---|---|---|---|

| PredictiveTask BufferTime | Integer | No | No | The buffer period ahead of the prediction task execution time. By default, all scheduled tasks that are automatically created for a predictive scaling rule are executed on the hour. You can set a buffer period to execute prediction tasks ahead of schedule, so that resources can be prepared in advance. | Valid values: 0 to 60. Unit: minutes. Default value: 0. |
|---|---|---|---|---|---|
| ScalingRuleTyp e | String | No | No | The type of the scaling rule. | Default value: SimpleScalingRule. Valid values: SimpleScalingRule: scales ECS instances based on the values of AdjustmentType and AdjustmentValue. TargetTrackingScaling Rule: dynamically calculates the number of ECS instances to be scaled and tries to keep the value of a predefined metric close to TargetValue. StepScalingRule: scales ECS instances in steps based on specified thresholds and metric values. PredictiveScalingRule: uses machine learning to analyze historical monitoring data of the scaling group and predict the future values of metrics. The rule then automatically creates scheduled tasks to set the boundary values for the scaling group. |

| PredictiveValu eBuffer | Integer | No | No | The ratio of the increment to the predicted value when PredictiveValu eBehavior is set to PredictiveValu eOverrideMax WithBuffer. If the predicted value increased by this ratio is greater than the initial maximum capacity, the value after the increase is used as the maximum value for prediction tasks. | Valid values: 0 to 100. Default value: 0. |
|---|---|---|---|---|---|
| TargetValue | Number | No | No | The metric value that you expect. This parameter takes effect only when the ScalingRuleTyp e parameter is set to TargetTracking ScalingRule or PredictiveScali ngRule. | The value must be greater than 0 and can have a maximum of three decimal places. |
| StepAdjustmen t | List | No | No | The step adjustments for step scaling. | For more information, see StepAdjustment properties. |

| PredictiveValu eBehavior | String | No | No | The action taken on the predicted maximum value. | Default value: MaxOverridePredictiveV alue. Valid values: MaxOverridePredictiv eValue: uses the initial maximum capacity as the maximum value for prediction tasks when the predicted value is greater than the initial maximum capacity. PredictiveValueOverri deMax: uses the predicted value as the maximum value for prediction tasks when the predicted value is greater than the initial maximum capacity. PredictiveValueOverri deMaxWithBuffer: increases the predicted value by a ratio, which is specified by PredictiveValueBuffer. If the value after the increase is greater than the initial maximum capacity, the value after the increase is used as the maximum value for prediction tasks. |
|---|---|---|---|---|---|
| DisableScaleIn | Boolean | No | No | Specifies whether to disable scale- in. This parameter takes effect only when the ScalingRuleTyp e parameter is set to TargetTracking ScalingRule. | Default value: false. Valid values: true false |
| InitialMaxSize | Integer | No | No | The maximum number of ECS instances in the scaling group, which is used together with the PredictiveValu eBehavior parameter. | The default value of this parameter is the value of MaxSize. |
| MinAdjustment Magnitude | Integer | No | No | The minimum number of ECS instances to be adjusted in the scaling rule. | This parameter takes effect only when the ScalingRuleType parameter is set to SimpleScalingRule or StepScalingRule, and the AdjustmentType parameter is set to PercentChangeInCapacit y. |

| EstimatedInsta nceWarmup | Integer | No | No | The warm-up period of the ECS instances. This parameter takes effect only when the ScalingRuleTyp e parameter is set to TargetTracking ScalingRule or StepScalingRul e. | Valid values: 0 to 86400. Unit: seconds. Default value: 300. The system adds ECS instances that are in the warm-up state to the scaling group, but does not report monitoring data to Cloud Monitor during the warm-up period. Note When the system calculates the number of ECS instances to be adjusted, the system does not count ECS instances in the warm-up state as part of the current capacity of the scaling group. |
|---|---|---|---|---|---|
| PredictiveScali ngMode | String | No | No | The mode of the predictive scaling rule. | Default value: PredictAndScale. Valid values: PredictAndScale: generates predicted results and creates prediction tasks. PredictOnly: generates predicted results but does not create prediction tasks. |

**StepAdjustment syntax**

```json
"StepAdjustment": [
    "MetricIntervalUpperBound": Number,
    "ScalingAdjustment": Integer,
    "MetricIntervalLowerBound": Number
```

`]`

**StepAdjustment properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MetricIntervalU pperBound | Number | No | No | The upper limit value specified in the step adjustment. This parameter takes effect only when the ScalingRuleTyp e parameter is set to StepScalingRul e. | Valid values: - 9.999999E18 to 9.999999E18 |

| ScalingAdjustm ent | Integer | No | No | The specified number of ECS instances to be adjusted in the step adjustment. This parameter takes effect only when the ScalingRuleTyp e parameter is set to StepScalingRul e. | None |
|---|---|---|---|---|---|
| MetricIntervalL owerBound | Number | No | No | The lower limit value specified in the step adjustment. This parameter takes effect only when the ScalingRuleTyp e parameter is set to StepScalingRul e. | Valid values: - 9.999999E18 to 9.999999E18 |

**Response parameters**

Fn::GetAtt ScalingRuleAri: the unique identifier of the scaling rule. ScalingRuleId: the ID of the scaling rule. This ID is a globally unique identifier (GUID) generated by the system.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "TargetValue": {
      "Type": "Number",
      "Description": "The target value of a metric. This parameter is required and applicable only to
target tracking scaling rules and predictive scaling rules. The value of TargetValue must be greater than 0 and can have a maximum of three decimal places."
```

`},`

```json
    "Cooldown": {
      "Type": "Number",
      "Description": "Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The def
ault value is empty.",
      "MinValue": 0,
      "MaxValue": 86400
```

`},`

```json
    "ScalingGroupId": {
      "Type": "String",
      "Description": "ID of the scaling group of a scaling rule."
```

`},`

```json
    "PredictiveValueBehavior": {
      "Type": "String",
      "Description": "The action taken on the predicted maximum value. Valid values:\n-
MaxOverridePredictiveValue: uses the initial maximum capacity as the maximum value for forecast tasks when the predicted value is greater than the initial maximum capacity.\n - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast tasks when the predicted value is greater than the initial maximum capacity.\n - PredictiveValueOverrideMaxWithBuffer: increases the predicted value with a ratio, which is specified
```

```json
by PredictiveValueBuffer. If the value after the increase is greater than the initial maximum capacit y, the value after the increase is used as the maximum value for forecast tasks.\n Default value: Max OverridePredictiveValue",
      "AllowedValues": [
        "MaxOverridePredictiveValue",
        "PredictiveValueOverrideMax",
        "PredictiveValueOverrideMaxWithBuffer"
```

`]` `},`

```json
    "MinAdjustmentMagnitude": {
      "Type": "Number",
      "Description": "The minimum number of ECS instances to be adjusted in a scaling rule. This para
meter takes effect only when the scaling rule type is SimpleScalingRule or StepScalingRule and Adjust mentType is PercentChangeInCapacity.",
      "MinValue": 0,
      "MaxValue": 20
```

`},`

```json
    "DisableScaleIn": {
      "Type": "Boolean",
      "Description": "Specifies whether to disable scale-in. This parameter is applicable only to
target tracking scaling rules.\n Default value: false",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]` `},`

```json
    "StepAdjustment": {
      "Type": "Json",
      "Description": ""
```

`},`

```json
    "AdjustmentType": {
      "Type": "String",
      "Description": "Adjustment mode of a scaling rule. Optional values:\n-
QuantityChangeInCapacity: It is used to increase or decrease a specified number of ECS instances.\n- PercentChangeInCapacity: It is used to increase or decrease a specified proportion of ECS instances.\n- TotalCapacity: It is used to adjust the quantity of ECS instances in the current scalin g group to a specified value.",
      "AllowedValues": [
        "QuantityChangeInCapacity",
        "PercentChangeInCapacity",
        "TotalCapacity"
```

`]` `},`

```json
    "MetricName": {
      "Type": "String",
      "Description": "The predefined metric to monitor. This parameter is required and applicable onl
y to target tracking scaling rules and predictive scaling rules.\nValid values of a target tracking s caling rule:\n- CpuUtilization: the average CPU utilization- ClassicInternetRx: the average public ne twork inbound traffic over the classic network\n- ClassicInternetTx: the average public network outbo und traffic over the classic network\n- VpcInternetRx: the average public network inbound traffic ove r the VPC\n- VpcInternetTx: the average public network outbound traffic over the VPC\n- IntranetRx: t he average internal network inbound traffic\n- IntranetTx: the average internal network outbound traf fic\nValid values of a predictive scaling rule:\n- CpuUtilization: the average CPU utilization\n- Int ranetRx: the average internal network inbound traffic\n- IntranetTx: the average internal network out bound traffic",
      "AllowedValues": [
        "CpuUtilization",
        "ClassicInternetRx",
        "ClassicInternetTx",
        "VpcInternetRx",
        "VpcInternetTx",
```

`pc` `te` `et` `,`

```
        "IntranetRx",
        "IntranetTx"
```

`]` `},`

```json
    "ScalingRuleName": {
      "Type": "String",
      "Description": "Name shown for the scaling group, which is a string containing 2 to 40 English
or Chinese characters. It must begin with a number, a letter (case-insensitive) or a Chinese characte r and can contain numbers, \"_\", \"-\" or \". \". The account name in the same scaling group is uniq ue in the same region. If this parameter value is not specified, the default value is ScalingRuleId.",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
```

`},`

```json
    "AdjustmentValue": {
      "Type": "Number",
      "Description": "Adjusted value of a scaling rule. Value range:\n- QuantityChangeInCapacity: [-5
00, 500]\n- PercentChangeInCapacity: [-100, 10000]\n- TotalCapacity: [0, 1000]",
      "MinValue": -500,
      "MaxValue": 10000
```

`},`

```json
    "InitialMaxSize": {
      "Type": "Number",
      "Description": "The maximum number of ECS instances in the scaling group, which is used
together with PredictiveValueBehavior.\n Default value: the same as the value of MaxSize",
      "MinValue": 0,
      "MaxValue": 1000
```

`},`

```json
    "ScalingRuleType": {
      "Type": "String",
      "Description": "The type of the scaling rule. Valid values:\n- SimpleScalingRule: scales ECS in
stances based on the values of AdjustmentType and AdjustmentValue.\n- TargetTrackingScalingRule: dyna mically calculates the number of ECS instances to be adjusted and tries to keep the value of a predef ined monitoring metric close to TargetValue.\n- StepScalingRule: scales ECS instances in steps based on specified thresholds and metric values.\n- PredictiveScalingRule: uses machine learning to analyze historical monitoring data of the scaling group and then predicts the future values of monitored metr ics, the rule then automatically creates scheduled tasks to set the boundary values for the scaling g roup.\n If this parameter value is not specified, the default value is SimpleScalingRule.",
      "AllowedValues": [
        "SimpleScalingRule",
        "TargetTrackingScalingRule",
        "StepScalingRule",
        "PredictiveScalingRule"
```

`]` `},`

```json
    "EstimatedInstanceWarmup": {
      "Type": "Number",
      "Description": "The warm-up period of the ECS instances. This parameter is applicable to target
tracking scaling rules and step scaling rules. The system adds ECS instances that are in the warm-up state to the scaling group, but does not report monitoring data during the warm-up period to CloudMon itor.\nNote: When calculating the number of ECS instances to be adjusted, the system does not count E CS instances in the warm-up state as part of the current capacity of the scaling group.\nValid values : 0 to 86400. Unit: seconds. Default value: 300.",
      "MinValue": 0,
      "MaxValue": 86400
```

`},`

```json
    "PredictiveScalingMode": {
      "Type": "String",
      "Description": "The mode of the predictive scaling rule. Valid values:\n- PredictAndScale:
generates forecasts and creates forecast tasks.\n- PredictOnly: generates forecasts but does not crea te forecast tasks.\nDefault value: PredictAndScale",
      "AllowedValues": [
        "PredictAndScale",
```

```
        "PredictOnly"
```

`]` `},`

```json
    "PredictiveTaskBufferTime": {
      "Type": "Number",
      "Description": "The amount of buffer time ahead of the forecast task execution time. By
default, all scheduled tasks that are automatically created for a predictive scaling rule are execute d at the beginning of each hour. You can set a buffer time to execute forecast tasks ahead of schedul e, so that resources can be prepared in advance. Valid values: 0 to 60. Unit: minutes.\n Default valu e: 0",
      "MinValue": 0,
      "MaxValue": 60
```

`},`

```json
    "PredictiveValueBuffer": {
      "Type": "Number",
      "Description": "The ratio of the increment to the predicted value when PredictiveValueBehavior
is set to PredictiveValueOverrideMaxWithBuffer. When the value after the increase is greater than the initial maximum capacity, the value after the increase is used for forecast tasks. Valid values: 0 to 100\n Default value: 0",
      "MinValue": 0,
      "MaxValue": 100
```

`},`

```json
  "Resources": {
    "ScalingRule": {
      "Type": "ALIYUN::ESS::ScalingRule",
      "Properties": {
        "TargetValue": {
          "Ref": "TargetValue"
```

`},`

```json
        "Cooldown": {
          "Ref": "Cooldown"
```

`},`

```json
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
```

`},`

```json
        "PredictiveValueBehavior": {
          "Ref": "PredictiveValueBehavior"
```

`},`

```json
        "MinAdjustmentMagnitude": {
          "Ref": "MinAdjustmentMagnitude"
```

`},`

```json
        "DisableScaleIn": {
          "Ref": "DisableScaleIn"
```

`},`

```json
        "StepAdjustment": {
          "Ref": "StepAdjustment"
```

`},`

```json
        "AdjustmentType": {
          "Ref": "AdjustmentType"
```

`},`

```json
        "MetricName": {
          "Ref": "MetricName"
```

`},`

```json
        "ScalingRuleName": {
          "Ref": "ScalingRuleName"
```

`},`

```json
        "AdjustmentValue": {
          "Ref": "AdjustmentValue"
```

`},`

```json
        "InitialMaxSize": {
          "Ref": "InitialMaxSize"
```

`},`

```json
        "ScalingRuleType": {
          "Ref": "ScalingRuleType"
```

`},`

```json
        "EstimatedInstanceWarmup": {
          "Ref": "EstimatedInstanceWarmup"
```

`},`

```json
        "PredictiveScalingMode": {
          "Ref": "PredictiveScalingMode"
```

`},`

```json
        "PredictiveTaskBufferTime": {
          "Ref": "PredictiveTaskBufferTime"
```

`},`

```json
        "PredictiveValueBuffer": {
          "Ref": "PredictiveValueBuffer"
```

`},`

```json
  "Outputs": {
    "ScalingRuleAri": {
      "Description": "Unique identifier of a scaling rule.",
      "Value": {
        "Fn::GetAtt": [
          "ScalingRule",
          "ScalingRuleAri"
```

`]` `},`

```json
    "ScalingRuleId": {
      "Description": "ID of a scaling rule, generated by the system and globally unique.",
      "Value": {
        "Fn::GetAtt": [
          "ScalingRule",
          "ScalingRuleId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  TargetValue:
    Type: Number
    Description: >-
      The target value of a metric. This parameter is required and applicable
      only to target tracking scaling rules and predictive scaling rules. The
      value of TargetValue must be greater than 0 and can have a maximum of
      three decimal places.
  Cooldown:
    Type: Number
    Description: >-
      Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds.
      The default value is empty.
    MinValue: 0
    MaxValue: 86400
  ScalingGroupId:
    Type: String
    Description: ID of the scaling group of a scaling rule.
PredictiveValueBehavior:
```

```
  PredictiveValueBehavior:
    Type: String
    Description: >-
      The action taken on the predicted maximum value. Valid values:
      - MaxOverridePredictiveValue: uses the initial maximum capacity as the
      maximum value for forecast tasks when the predicted value is greater than
      the initial maximum capacity.
       - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast tasks
when the predicted value is greater than the initial maximum capacity.
       - PredictiveValueOverrideMaxWithBuffer: increases the predicted value with a ratio, which is s
pecified by PredictiveValueBuffer. If the value after the increase is greater than the initial maximu m capacity, the value after the increase is used as the maximum value for forecast tasks.
       Default value: MaxOverridePredictiveValue
    AllowedValues:
      - MaxOverridePredictiveValue
      - PredictiveValueOverrideMax
      - PredictiveValueOverrideMaxWithBuffer
  MinAdjustmentMagnitude:
    Type: Number
    Description: >-
      The minimum number of ECS instances to be adjusted in a scaling rule. This
      parameter takes effect only when the scaling rule type is
      SimpleScalingRule or StepScalingRule and AdjustmentType is
      PercentChangeInCapacity.
    MinValue: 0
    MaxValue: 20
  DisableScaleIn:
    Type: Boolean
    Description: >-
      Specifies whether to disable scale-in. This parameter is applicable only
      to target tracking scaling rules.
       Default value: false
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
  StepAdjustment:
    Type: Json
    Description: ''
  AdjustmentType:
    Type: String
    Description: >-
      Adjustment mode of a scaling rule. Optional values:
      - QuantityChangeInCapacity: It is used to increase or decrease a specified
      number of ECS instances.
      - PercentChangeInCapacity: It is used to increase or decrease a specified
      proportion of ECS instances.
      - TotalCapacity: It is used to adjust the quantity of ECS instances in the
      current scaling group to a specified value.
    AllowedValues:
      - QuantityChangeInCapacity
      - PercentChangeInCapacity
      - TotalCapacity
  MetricName:
    Type: String
    Description: >-
      The predefined metric to monitor. This parameter is required and
      applicable only to target tracking scaling rules and predictive scaling
```

```
      rules.
      Valid values of a target tracking scaling rule:
      - CpuUtilization: the average CPU utilization- ClassicInternetRx: the
      average public network inbound traffic over the classic network
      - ClassicInternetTx: the average public network outbound traffic over the
      classic network
      - VpcInternetRx: the average public network inbound traffic over the VPC
      - VpcInternetTx: the average public network outbound traffic over the VPC
      - IntranetRx: the average internal network inbound traffic
      - IntranetTx: the average internal network outbound traffic
      Valid values of a predictive scaling rule:
      - CpuUtilization: the average CPU utilization
      - IntranetRx: the average internal network inbound traffic
      - IntranetTx: the average internal network outbound traffic
    AllowedValues:
      - CpuUtilization
      - ClassicInternetRx
      - ClassicInternetTx
      - VpcInternetRx
      - VpcInternetTx
      - IntranetRx
      - IntranetTx
  ScalingRuleName:
    Type: String
    Description: >-
      Name shown for the scaling group, which is a string containing 2 to 40
      English or Chinese characters. It must begin with a number, a letter
      (case-insensitive) or a Chinese character and can contain numbers, "_",
      "-" or ".". The account name in the same scaling group is unique in the
      same region. If this parameter value is not specified, the default value
      is ScalingRuleId.
    AllowedPattern: '^[a-zA-Z0-9\u4e00-\u9fa5][-_.a-zA-Z0-9\u4e00-\u9fa5]{1,63}$'
  AdjustmentValue:
    Type: Number
    Description: |-
      Adjusted value of a scaling rule. Value range:
      - QuantityChangeInCapacity: [-500, 500]
      - PercentChangeInCapacity: [-100, 10000]
      - TotalCapacity: [0, 1000]
    MinValue: -500
    MaxValue: 10000
  InitialMaxSize:
    Type: Number
    Description: >-
      The maximum number of ECS instances in the scaling group, which is used
      together with PredictiveValueBehavior.
       Default value: the same as the value of MaxSize
    MinValue: 0
    MaxValue: 1000
  ScalingRuleType:
    Type: String
```

`D`

```
iti
```

`>`

```
    Description: >-
      The type of the scaling rule. Valid values:
      - SimpleScalingRule: scales ECS instances based on the values of
      AdjustmentType and AdjustmentValue.
      - TargetTrackingScalingRule: dynamically calculates the number of ECS
      instances to be adjusted and tries to keep the value of a predefined
      monitoring metric close to TargetValue.
      - StepScalingRule: scales ECS instances in steps based on specified
      thresholds and metric values.
      - PredictiveScalingRule: uses machine learning to analyze historical
      monitoring data of the scaling group and then predicts the future values
      of monitored metrics, the rule then automatically creates scheduled tasks
      to set the boundary values for the scaling group.
       If this parameter value is not specified, the default value is SimpleScalingRule.
    AllowedValues:
      - SimpleScalingRule
      - TargetTrackingScalingRule
      - StepScalingRule
      - PredictiveScalingRule
  EstimatedInstanceWarmup:
    Type: Number
    Description: >-
      The warm-up period of the ECS instances. This parameter is applicable to
      target tracking scaling rules and step scaling rules. The system adds ECS
      instances that are in the warm-up state to the scaling group, but does not
      report monitoring data during the warm-up period to CloudMonitor.
      Note: When calculating the number of ECS instances to be adjusted, the
      system does not count ECS instances in the warm-up state as part of the
      current capacity of the scaling group.
      Valid values: 0 to 86400. Unit: seconds. Default value: 300.
    MinValue: 0
    MaxValue: 86400
  PredictiveScalingMode:
    Type: String
    Description: |-
      The mode of the predictive scaling rule. Valid values:
      - PredictAndScale: generates forecasts and creates forecast tasks.
      - PredictOnly: generates forecasts but does not create forecast tasks.
      Default value: PredictAndScale
    AllowedValues:
      - PredictAndScale
      - PredictOnly
  PredictiveTaskBufferTime:
    Type: Number
    Description: >-
      The amount of buffer time ahead of the forecast task execution time. By
      default, all scheduled tasks that are automatically created for a
      predictive scaling rule are executed at the beginning of each hour. You
      can set a buffer time to execute forecast tasks ahead of schedule, so that
      resources can be prepared in advance. Valid values: 0 to 60. Unit:
      minutes.
       Default value: 0
    MinValue: 0
    MaxValue: 60
  PredictiveValueBuffer:
    Type: Number
    Description: >-
```

`p`

```
      The ratio of the increment to the predicted value when
      PredictiveValueBehavior is set to PredictiveValueOverrideMaxWithBuffer.
      When the value after the increase is greater than the initial maximum
      capacity, the value after the increase is used for forecast tasks. Valid
      values: 0 to 100
       Default value: 0
    MinValue: 0
    MaxValue: 100
Resources:
  ScalingRule:
    Type: 'ALIYUN::ESS::ScalingRule'
    Properties:
      TargetValue:
        Ref: TargetValue
      Cooldown:
        Ref: Cooldown
      ScalingGroupId:
        Ref: ScalingGroupId
      PredictiveValueBehavior:
        Ref: PredictiveValueBehavior
      MinAdjustmentMagnitude:
        Ref: MinAdjustmentMagnitude
      DisableScaleIn:
        Ref: DisableScaleIn
      StepAdjustment:
        Ref: StepAdjustment
      AdjustmentType:
        Ref: AdjustmentType
      MetricName:
        Ref: MetricName
      ScalingRuleName:
        Ref: ScalingRuleName
      AdjustmentValue:
        Ref: AdjustmentValue
      InitialMaxSize:
        Ref: InitialMaxSize
      ScalingRuleType:
        Ref: ScalingRuleType
      EstimatedInstanceWarmup:
        Ref: EstimatedInstanceWarmup
      PredictiveScalingMode:
        Ref: PredictiveScalingMode
      PredictiveTaskBufferTime:
        Ref: PredictiveTaskBufferTime
      PredictiveValueBuffer:
        Ref: PredictiveValueBuffer
Outputs:
  ScalingRuleAri:
    Description: Unique identifier of a scaling rule.
    Value:
      'Fn::GetAtt':
        - ScalingRule
        - ScalingRuleAri
  ScalingRuleId:
    Description: 'ID of a scaling rule, generated by the system and globally unique.'
    Value:
      'Fn::GetAtt':
        - ScalingRule
        - ScalingRuleId
```

#### ALIYUN::ESS::ScheduledTask

ALIYUN::ESS::ScheduledTask is used to create a scheduled task based on specified parameters.

**Syntax**

```json
  "Type": "ALIYUN::ESS::ScheduledTask",
  "Properties": {
    "TaskEnabled": Boolean,
    "Description": String,
    "ScheduledTaskName": String,
    "LaunchExpirationTime": Integer,
    "LaunchTime": String,
    "RecurrenceEndTime": String,
    "RecurrenceType": String,
    "RecurrenceValue": String,
    "ScheduledAction": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TaskEnabled | Boolean | No | Yes | Specifies whether to enable the scheduled task. | Valid values: true: enables the task. This is the default value. false: stops the task. |
| Description | String | No | Yes | The description of the scheduled task. | The description must be 2 to 200 characters in length. |
| ScheduledTaskN ame | String | No | Yes | The display name of the scheduled task. | The name must be 2 to 40 characters in length and can contain digits, letters, underscores ( ), _ hyphens (-), and periods (.). It must start with a digit or letter. The name of the scheduled task must be unique to an Alibaba Cloud account in a region. If you do not specify this parameter, the default value is the ID of the scheduled scaling task. |

| LaunchExpiratio nTime | Integer | No | Yes | The period of time over which a failed scheduled task is retried. |   | Valid values: 0 to 21600. Unit: seconds. Default value: 600. |   |   |
|---|---|---|---|---|---|---|---|---|
| LaunchTime | String | Yes | Yes | The time at which the scheduled task is triggered. |   | Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. The time must be in UTC. If the RecurrenceTy pe parameter is specified, the task is executed each day at the time specified by LaunchTime. If the RecurrenceTy pe parameter is not specified, the task is executed only once at the time specified by LaunchTime. You cannot enter a time point later than 90 days from the date of scheduled task creation or modification. |   |   |
|   |   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   |   |   | DDThh:mmZ |   |   |

| RecurrenceEndTi me | String | No | Yes | The end time of the scheduled task to be repeated. | Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation or modification. If you set RecurrenceEndT ime, you must also set both RecurrenceType and RecurrenceValu e. |
|---|---|---|---|---|---|

|   |   | YYYY-MM- |   |
|---|---|---|---|
|   | DDThh:mmZ |   |   |

| RecurrenceType | String | No | Yes | The interval at which the scheduled task is repeated. | Valid values: Daily: The scheduled task is executed once every specified number of days. Weekly: The scheduled task is executed on each specified day of a week. Monthly: The scheduled task is executed on each specified day of a month. Cron: The scheduled task is executed based on the specified Cron expression. If you set RecurrenceType , you must also set both RecurrenceEndT ime and RecurrenceValu e. |
|---|---|---|---|---|---|
|   |   |   |   |   | Valid values when RecurrenceTy pe is set to Daily: 1 to 31. Valid values when RecurrenceTy pe is set to Weekly: 0 to 6. You can enter multiple values separated by commas (,). The values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday. Valid values when RecurrenceTy pe is set to Monthly: two values ranging from 1 to 31 in the |

| RecurrenceValu e | String | No | Yes | The recurrence value of the scheduled task to be repeated. | A-B format. B must be greater than or equal to A. Valid values when RecurrenceTy pe is set to Cron: a Cron expression. A Cron expression is written in UTC time and |
|---|---|---|---|---|---|
|   |   |   |   |   | consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W characters. If you set RecurrenceValu e, you must also set both RecurrenceEndT ime and RecurrenceType . |
| ScheduledAction | String | Yes | Yes | The operations to be performed when the scheduled task is triggered. | The parameter value can be up to 200 characters in length. When you set this parameter, you must also enter the unique identifier of the scaling rule. |

**Response parameters**

Fn::GetAtt ScheduledTaskId: the ID of the scheduled task. This ID is a globally unique identifier (GUID) generated by the system.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  ScheduledTask:
    Type: ALIYUN::ESS::ScheduledTask
    Properties:
      TaskEnabled: 'true'
      Description: scheduledtask
      ScheduledTaskName: task1
      LaunchTime: 2014-08-17T16:52Z
      RecurrenceEndTime: 2014-08-17T16:55Z
      RecurrenceType: Daily
      RecurrenceValue: '1'
      ScheduledAction: ari:acs:ess:cn-qingdao:1344371:scalingRule/cCBpdYdQuBe2cUxOdu6piOk
Outputs:
  ScheduledTaskId:
    Value:
      FN::GetAtt:
        - ScheduledTask
        - ScheduledTaskId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScheduledTask": {
      "Type": "ALIYUN::ESS::ScheduledTask",
      "Properties": {
        "TaskEnabled": "true",
        "Description": "scheduledtask",
        "ScheduledTaskName": "task1",
        "LaunchTime": "2014-08-17T16:52Z",
        "RecurrenceEndTime": "2014-08-17T16:55Z",
        "RecurrenceType": "Daily",
        "RecurrenceValue": "1",
        "ScheduledAction": "ari:acs:ess:cn-qingdao:1344371:scalingRule/cCBpdYdQuBe2cUxOdu6piOk"
```

`},`

```json
  "Outputs": {
    "ScheduledTaskId": {
      "Value": {
        "FN::GetAtt": [
          "ScheduledTask",
          "ScheduledTaskId"
```

`]`

### NAS

#### ALIYUN::NAS::AccessGroup

ALIYUN::NAS::AccessGroup is used to create a permission group.

**Syntax**

```json
  "Type": "ALIYUN::NAS::AccessGroup",
  "Properties": {
    "AccessGroupType": String,
    "AccessGroupName": String,
    "Description": String
```

**Properties**

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| AccessGroupTyp e | String | Yes | No | The type of the permission group. | Valid values: VPC and Classic. |
| AccessGroupNa me | String | Yes | No | The name of the permission group. | The name must be 3 to 64 characters in length. It must start with a letter, digit, or hyphen (-). |
| Description | String | No | Yes | The description of the permission group. The description is the same as the permission group name by default. | None |

**Response parameters**

**FN::GetAtt**

AccessGroupName: the name of the permission group.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessGroup": {
      "Type": "ALIYUN::NAS::AccessGroup",
      "Properties": {
        "AccessGroupType": {
          "Ref": "AccessGroupType"
```

`},`

```json
        "AccessGroupName": {
          "Ref": "AccessGroupName"
```

`},`

```json
        "Description": {
          "Ref": "Description"
```

`},`

```json
  "Parameters": {
    "AccessGroupType": {
      "Type": "String",
      "Description": "Permission group type, including the Vpc and Classic types",
      "AllowedValues": ["Vpc", "Classic"]
```

`},`

```json
    "AccessGroupName": {
      "AllowedPattern": "^[a-zA-Z0-9-]{3,64}$",
      "Type": "String",
      "Description": "Permission group name"
```

`},`

```json
    "Description": {
      "Type": "String",
      "Description": "Permission group description. It is the same as the permission group name by de
fault."
```

`},`

```json
  "Outputs": {
    "AccessGroupName": {
      "Description": "Permission group name",
      "Value": {
        "Fn::GetAtt": ["AccessGroup", "AccessGroupName"]
```

#### ALIYUN::NAS::AccessRule

ALIYUN::NAS::AccessRule is used to create a permission rule.

**Syntax**

```json
  "Type": "ALIYUN::NAS::AccessRule",
  "Properties": {
    "Priority": Integer,
    "UserAccessType": String,
    "AccessGroupName": String,
    "SourceCidrIp": String,
    "RWAccessType": String
```

**Properties**

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| Priority | Integer | No | Yes | The user access priority. | Valid values: 1 to 100. Default value: 1. |
| UserAccessType | String | No | Yes | The user access type. | Valid values: no squash, _ root squash, _ and all squash. _ Default value: no squash. _ |
| AccessGroupNa me | String | Yes | No | The name of the permission group. | None |
| SourceCidrIp | String | Yes | Yes | The authorized IP address or CIDR block. | None |
| RWAccessType | String | No | Yes | The read/write permission type. | Valid values: RDWR and RDONLY. Default value: RDWR. |

**Response parameters**

**FN::GetAtt**

AccessRuleId: the ID of the permission rule.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  AccessRule:
    Type: ALIYUN::NAS::AccessRule
    Properties:
      SourceCidrIp: 0.0.0.0/0
      AccessGroupName: TestAccessGroup
Outputs:
  AccessRuleId:
    Description: Rule serial number
    Value:
      Fn::GetAtt:
        - AccessRule
        - AccessRuleId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessRule": {
      "Type": "ALIYUN::NAS::AccessRule",
      "Properties": {
        "SourceCidrIp": "0.0.0.0/0",
        "AccessGroupName": "TestAccessGroup"
```

`},`

```json
  "Outputs": {
    "AccessRuleId": {
      "Description": "Rule serial number",
      "Value": {
        "Fn::GetAtt": [
          "AccessRule",
          "AccessRuleId"
```

`]`

#### ALIYUN::NAS::FileSystem

ALIYUN::NAS::FileSystem is used to create a file system.

**Syntax**

```json
  "Type": "ALIYUN::NAS::FileSystem",
  "Properties": {
    "SnapshotId": String,
    "Description": String,
    "StorageType": String,
    "DeletionForce": Boolean,
    "EncryptType": Integer,
    "VpcId": String,
    "ZoneId": String,
    "Capacity": Integer,
    "Tags": List,
    "ProtocolType": String,
    "FileSystemType": String,
    "Bandwidth": Integer,
    "VSwitchId": String,
    "Duration": Integer,
    "ChargeType": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| ProtocolTyp e | String | Yes | No | The protocol type. | Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
|---|---|---|---|---|---|
| StorageType | String | Yes | No | The storage type. | Valid values: Valid values if you set the FileSystemType property to standard: Performance Capacity Valid values if you set the FileSystemType property to extreme or cpfs: standard advance |
| DeletionForc e | Boolean | No | Yes | Specifies whether to forcefully delete the file system. | Default value: false. Valid values: true: forcefully deletes the file system. false: does not forcefully delete the file system. |
| Description | String | No | Yes | The description of the file system. | The description must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The description must start with a letter but cannot start with http:// or https:// . |
| ZoneId | String | No | No | The ID of the zone. | None. |
| Tags | List | No | Yes | The tags of the file system. | You can add up to 20 tags to each file system. For more information, see Tags properties. |

| SnapshotId | String | No | No | The ID of the snapshot. | You can configure this property to specify a snapshot from which you create an Apsara File Storage NAS (NAS) file system. This property is supported only for Extreme NAS file systems. Note If you create a file system from a snapshot, the version of the new file system must be the same as the version of the source file system that is contained in the snapshot. If the version of a file system that you create is different from the version of the source file system, you must perform the following operations: 1. Create a file system and copy the data that is stored in the source file of the snapshot to the file system. 2. After you copy the data, migrate the data to the file system. |
|---|---|---|---|---|---|
| EncryptType | Integer | No | No | Specifies whether to encrypt the file system. You can use keys that are hosted by Key Management Service (KMS) to encrypt data that is stored in the file system. When you read and write the encrypted data, you do not need to decrypt the data. | This property takes effect when you set the FileSystemType property to standard or extreme. Valid values: 0: does not encrypt the file system. 1: encrypts the file system. |

| Capacity | Integer | No | No | The capacity of the file system. | This property takes effect and is required when you set the FileSystemType property to extreme or cpfs. Valid values: Valid values if you set the FileSystemType property to extreme: 100 to 262144. Valid values if you set the FileSystemType property to cpfs: 2048 to 512000. Unit: GB. |
|---|---|---|---|---|---|
| FileSystemT ype | String | No | No | The type of the file system. | Default value: standard. Valid values: standard: General-purpose NAS file system extreme: Extreme NAS file system cpfs: Cloud Paralleled File System (CPFS) file system |
| VpcId | String | No | No | The ID of the virtual private cloud (VPC). If you specify the VpcId and VSwitchId properties, a default mount target is preconfigured when the file system is created. | This property is required when you set the FileSystemType property to cpfs. |
| Bandwidth | Integer | No | No | The maximum throughput of the file system. | This property is required when you set the FileSystemType property to cpfs. The value of this property varies based on the value of the Capacity property. For more information, visit the CPFS buy page. Unit: Mbit/s. |
| VSwitchId | String | No | No | The ID of the vSwitch. If you specify the VpcId and VSwitchId properties, a default mount target is preconfigured when the file system is created. | This property is required when you set the FileSystemType property to cpfs. |

| Duration | Integer | No | No | The subscription period of the file system. | This property takes effect and is required when you set the ChargeType property to Subscription. If you do not renew a subscription file system when it expires, the file system is automitically released. Valid values: 1 2 3 6 12 36 Unit: month. |
|---|---|---|---|---|---|
| ChargeType | String | No | No | The billing method of the file system. | Valid values: PayAsYouGo Subscription |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The key cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The value cannot start with aliyun or acs: . |

**Return values**

Fn::GetAtt FileSystemId: the ID of the file system.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test NAS FileSystem Parameters: {} Resources:
  FileSystem:
    Type: ALIYUN::NAS::FileSystem
    Properties:
      ProtocolType: NFS
      StorageType: Capacity
Outputs:
  FileSystemId:
    Description: ID of the file system created
    Value:
      Fn::GetAtt:
        - FileSystem
        - FileSystemId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test NAS FileSystem",
  "Parameters": {
```

`},`

```json
  "Resources": {
    "FileSystem": {
      "Type": "ALIYUN::NAS::FileSystem",
      "Properties": {
        "ProtocolType": "NFS",
        "StorageType": "Capacity"
```

`},`

```json
  "Outputs": {
    "FileSystemId": {
      "Description": "ID of the file system created",
      "Value": {
        "Fn::GetAtt": [
          "FileSystem",
          "FileSystemId"
```

`]` To view more examples, visit NAS.json and NAS.yml. In the examples, the following resource types are used: ALIYUN::NAS::FileSystem, ALIYUN::NAS::AccessGroup, ALIYUN::NAS::AccessRule, and ALIYUN::NAS::MountTarget.

#### ALIYUN::NAS::MountTarget

ALIYUN::NAS::MountTarget is used to create a mount point.

**Syntax**

```json
  "Type": "ALIYUN::NAS::MountTarget",
  "Properties": {
    "Status": String,
    "VpcId": String,
    "FileSystemId": String,
    "VSwitchId": String,
    "NetworkType": String,
    "AccessGroupName": String
```

**Properties**

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| Status | String | No | Yes | The status of a file system. | Valid values: Active and Inactive. |
| VpcId | String | No | No | The ID of the VPC to which the file system belongs. | None |
| FileSystemId | String | Yes | No | The ID of the file system. | None |
| VSwitchId | String | No | No | The ID of the vSwitch in the VPC. | None |
| NetworkType | String | Yes | No | The network type. | Valid values: VPC and Classic. |
| AccessGroupNa me | String | Yes | Yes | The permission group name. | None |

**Response parameters**

**FN::GetAtt**

MountTargetDomain: the domain name of the mount point.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VpcId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VPC::VPCId
  VSwitchId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
  FileSystemId:
    Type: String
    Description: File system ID
Resources:
  MountTarget:
    Type: ALIYUN::NAS::MountTarget
    Properties:
      Status: Active
      VpcId:
        Ref: VpcId
      FileSystemId:
        Ref: FileSystemId
      VSwitchId:
        Ref: VSwitchId
      NetworkType: Vpc
      AccessGroupName: TestAccessGroup
Outputs: {}
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VpcId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId"
```

`},`

```json
    "VSwitchId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "${VpcId}"
```

`},`

```json
    "FileSystemId": {
      "Type": "String",
      "Description": "File system ID"
```

`},`

```json
  "Resources": {
    "MountTarget": {
      "Type": "ALIYUN::NAS::MountTarget",
      "Properties": {
        "Status": "Active",
        "VpcId": {
          "Ref": "VpcId"
```

`},`

```json
        "FileSystemId": {
          "Ref": "FileSystemId"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "NetworkType": "Vpc",
        "AccessGroupName": "TestAccessGroup"
```

`},`

```json
  "Outputs": {
```

### OSS

#### ALIYUN::OSS::Bucket

ALIYUN::OSS::Bucket is used to create an Object Storage Service (OSS) bucket.

**Syntax**

```json
  "Type": "ALIYUN::OSS::Bucket",
  "Properties": {
    "AccessControl": String,
    "RefererConfiguration": Map,
    "ServerSideEncryptionConfiguration": Map,
    "CORSConfiguration": Map,
    "Tags": Map,
    "LoggingConfiguration": Map,
    "LifecycleConfiguration": Map,
    "StorageClass": String,
    "DeletionForce": Boolean,
    "WebsiteConfiguration": Map,
    "Policy": Map,
    "BucketName": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| BucketName | String | Yes | No | The name of the bucket. | The name must be 3 to 63 characters in length and can contain lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or a digit. |
| AccessContro l | String | No | No | The access control configuration s of the bucket. | Valid values: private (default): The bucket is private. public-read: The bucket supports public reads. public-read-write: The bucket supports public reads and writes. |
| CORSConfigu ration | Map | No | No | The configuration s of cross- origin resource sharing (CORS) for objects in the bucket. | For more information, see CORSConfiguration properties. |
| LifecycleConfi guration | Map | No | Yes | The lifecycle configuration s for objects in the bucket. | For more information, see LifecycleConfiguration properties. |
| LoggingConfi guration | Map | No | No | The log storage configuration s. | For more information, see LoggingConfiguration properties. |
| RefererConfig uration | Map | No | Yes | The hotlink protection configuration s. | For more information, see RefererConfiguration properties. |

| DeletionForce | Boolean | No | No | Specifies whether to forcibly delete objects from the OSS bucket. | Valid values: true: forcibly deletes objects from the OSS bucket. false (default): does not forcibly delete objects from the OSS bucket. |
|---|---|---|---|---|---|
| WebsiteConfi guration | Map | No | No | The configuration s of the hosted static website. | For more information, see WebsiteConfiguration properties. |
| ServerSideEn cryptionConfi guration | Map | No | Yes | The server- side encryption rules. | For more information, see ServerSideEncryptionConfigura tion properties. |
| Tags | Map | No | Yes | The tags of the bucket. Tags exist as key-value pairs. | A maximum of 20 tags can be specified. A tag key must be 1 to 64 bytes in length and cannot start with http:// , https:// , or Aliyun . A tag value must be 0 to 128 bytes in length and must be encoded in UTF-8. |
| StorageClass | String | No | No | The type of the bucket. | Default value: Standard. Valid values: Standard: Standard IA: Infrequent Access (IA) Archive: Archive |
| Policy | Map | No | No | The bucket policy configuration s. | None |

|   | http:// |   |
|---|---|---|
| https:// |   |   |

**CORSConfiguration syntax**

```json
"CORSConfiguration": {
  "CORSRule": List
```

**CORSConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CORSRule | List | No | No | The list of rules that define CORS of objects in the bucket. | For more information, see CORSRule properties. |

**CORSRule syntax**

```json
"CORSRule": [
    "MaxAgeSeconds": Number,
    "AllowedMethod": List,
    "ExposeHeader": List,
    "AllowedOrigin": List,
    "AllowedHeader": List
```

`]`

**CORSRule properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllowedHead er | List | No | No | The allowed headers in cross-domain requests. | Valid values: * Cache-Control Content-Language Content-Type Expires Last-Modified Pragma |
| AllowedMetho d | List | No | No | The allowed methods for cross-domain requests. | Valid values: * GET PUT POST DELETE HEAD |
| AllowedOrigin | List | No | No | The origins from which you want to allow cross- domain requests. | None |
| ExposeHeade r | List | No | No | The response headers that you can access from your applications. | Asterisks (*) cannot be used as wildcard characters. |
| MaxAgeSeco nds | Number | No | No | The period of time that the browser can cache the response of a preflight (OPTIONS) request to a specific resource. | None |

**LifecycleConfiguration syntax**

```json
"LifecycleConfiguration": {
  "Rule": List
```

**LifecycleConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Rule | List | Yes | No | The list of rules that define how the bucket manages objects during their lifecycles. | For more information, see Rule properties. |

**Rule syntax**

```json
"Rule": [
    "Status": String,
    "AbortMultipartUpload": Map,
    "Expiration": Map,
    "Prefix": String,
    "ID": String
```

`]`

**Rule properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ID | String | No | No | The unique ID of the rule. | The ID can be up to 255 bytes in length. When this parameter is empty or not specified, OSS generates a unique ID for the rule. |
| Prefix | String | Yes | No | The prefix to which the rule applies. | The rule takes effect only on objects that have a matching prefix. |
| Status | String | No | Yes | Specifies whether to enable the rule. | Valid values: Enabled: enables the rule. Disabled: disables the rule. |
| Expiration | Map | No | No | The expiration attributes of the rule for the specified object. | For more information, see Expiration properties. |
| AbortMultipar tUpload | Map | No | No | The expiration attributes of the multipart upload tasks that are not complete. | For more information, see AbortMultipartUpload properties. |

**Expiration syntax**

```json
"Expiration":{
  "Days": Number,
  "CreatedBeforeDate": String,
  "Date": String
```

**Expiration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days from when the object was last modified to when the rule takes effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |
| CreatedBefor eDate | String | No | No | The date based on which the lifecycle rules are implemented. OSS performs the specified operation on data that was last modified before this date. | Specify the time in the ISO 8601 standard. The time must be at 00:00:00 UTC. Example: 2002-10-11T00:00:00.000Z. |

**AbortMultipartUpload syntax**

```json
"AbortMultipartUpload": {
  "CreatedBeforeDate": String,
  "Days": Number
```

**AbortMultipartUpload properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days from when the object was last modified to when the rule takes effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |
| CreatedBefor eDate | String | No | No | The time before which the rule takes effect. | Specify the time in the ISO 8601 standard. The time must be at 00:00:00 UTC. Example: 2002-10-11T00:00:00.000Z. |

**LoggingConfiguration syntax**

```json
"LoggingConfiguration": {
  "TargetBucket": String,
  "TargetPrefix": String
```

**LoggingConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| TargetBucket | String | No | No | The bucket that is used to store access logs. | None |
|---|---|---|---|---|---|
| TargetPrefix | String | No | No | The prefix of the names of access logs that are saved. | None |

**WebsiteConfiguration syntax**

```json
"WebsiteConfiguration":{
  "IndexDocument": String,
  "ErrorDocument": String
```

**WebsiteConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IndexDocume nt | String | No | No | The homepage for the hosted static website. | None |
| ErrorDocume nt | String | No | No | The error page of the hosted static website. | None |

**RefererConfiguration syntax**

```json
"RefererConfiguration":{
  "AllowEmptyReferer": String,
  "RefererList": List
```

**RefererConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllowEmptyR eferer | Boolean | No | No | Specifies whether to allow access requests that have an empty Referer field. | Valid values: true (default): allows requests that have an empty Referer field. false: denies requests that have an empty Referer field. |
| RefererList | List | No | No | The Referer whitelist. OSS allows requests whose Referer field values are in the Referer whitelist. | None |

**ServerSideEncryptionConfiguration syntax**

```json
"ServerSideEncryptionConfiguration":{
  "KMSMasterKeyID": String,
  "SSEAlgorithm": String
```

**ServerSideEncryptionConfiguration properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| KMSMasterKe yID | String | No | No | The ID of the customer master key. | The key ID is required only when the SSEAlgorithm parameter is set to KMS and a specified key is used for encryption. |
| SSEAlgorithm | String | Yes | No | The default server-side encryption method. | Valid values: KMS AES256 |

**Response parameters**

Fn::GetAtt Name: the bucket name, which is globally unique. DomainName: the public domain name of the specified bucket. InternalDomainName: the internal domain name of the specified bucket.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Policy": {
      "Type": "Json",
      "Description": "Bucket policy"
```

`},`

```json
    "CORSConfiguration": {
      "Type": "Json",
      "Description": "Rules that define cross-origin resource sharing of objects in this bucket."
```

`},`

```json
    "DeletionForce": {
      "Type": "Boolean",
      "Description": "Whether force delete the relative objects in the bucket. Default value is false
.",
      "AllowedValues": [
        "true",
        "false"
```

`],`

```json
      "Default": false
```

`},`

```json
    "BucketName": {
      "Type": "String",
      "Description": "bucket name."
```

`},`

```json
    "StorageClass": {
      "Type": "String",
      "Description": "Specifies the storage class of the bucket. Default is \"Standard\".",
      "AllowedValues": [
        "Standard",
        "IA",
        "Archive"
```

`]` `},`

```json
    "LoggingConfiguration": {
      "Type": "Json",
      "Description": "Settings that defines where logs are stored."
```

`},`

```json
    "WebsiteConfiguration": {
      "Type": "Json",
      "Description": "The properties of website config."
```

`},`

```json
    "RefererConfiguration": {
      "Type": "Json"
```

`},`

```json
    "LifecycleConfiguration": {
      "Type": "Json",
      "Description": "Rules that define how oss bucket manages objects during their lifetime."
```

`},`

```json
    "ServerSideEncryptionConfiguration": {
      "Type": "Json",
      "Description": "Specifies the bucket used to store the server-side encryption rule."
```

`},`

```json
    "AccessControl": {
      "Type": "String",
      "Description": "The access control list.",
      "AllowedValues": [
        "private",
        "public-read",
        "public-read-write"
```

`],`

```json
      "Default": "private"
```

`},`

```json
    "Tags": {
      "Type": "Json",
      "Description": "Bucket tags in k-v pairs format."
```

`},`

```json
  "Resources": {
    "Bucket": {
      "Type": "ALIYUN::OSS::Bucket",
      "Properties": {
        "Policy": {
          "Ref": "Policy"
```

`},`

```json
        "CORSConfiguration": {
          "Ref": "CORSConfiguration"
```

`},`

```json
        "DeletionForce": {
          "Ref": "DeletionForce"
```

`},`

```json
        "BucketName": {
          "Ref": "BucketName"
```

`},`

```json
        "StorageClass": {
          "Ref": "StorageClass"
```

`},`

```json
        "LoggingConfiguration": {
          "Ref": "LoggingConfiguration"
```

`},`

```json
        "WebsiteConfiguration": {
          "Ref": "WebsiteConfiguration"
```

`},`

```json
        "RefererConfiguration": {
          "Ref": "RefererConfiguration"
```

`e` `:`

```
eeeCo guato
```

`},`

```json
        "LifecycleConfiguration": {
          "Ref": "LifecycleConfiguration"
```

`},`

```json
        "ServerSideEncryptionConfiguration": {
          "Ref": "ServerSideEncryptionConfiguration"
```

`},`

```json
        "AccessControl": {
          "Ref": "AccessControl"
```

`},`

```json
        "Tags": {
          "Ref": "Tags"
```

`},`

```json
  "Outputs": {
    "DomainName": {
      "Description": "The public DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "DomainName"
```

`]` `},`

```json
    "InternalDomainName": {
      "Description": "The internal DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "InternalDomainName"
```

`]` `},`

```json
    "Name": {
      "Description": "The name of Bucket",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "Name"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Policy:
    Type: Json
    Description: Bucket policy
  CORSConfiguration:
    Type: Json
    Description: Rules that define cross-origin resource sharing of objects in this bucket.
  DeletionForce:
    Type: Boolean
    Description: >-
      Whether force delete the relative objects in the bucket. Default value is
false.
```

```
      false.
    AllowedValues:
      - 'true'
      - 'false'
    Default: false
  BucketName:
    Type: String
    Description: bucket name.
  StorageClass:
    Type: String
    Description: Specifies the storage class of the bucket. Default is "Standard".
    AllowedValues:
      - Standard
      - IA
      - Archive
  LoggingConfiguration:
    Type: Json
    Description: Settings that defines where logs are stored.
  WebsiteConfiguration:
    Type: Json
    Description: The properties of website config.
  RefererConfiguration:
    Type: Json
  LifecycleConfiguration:
    Type: Json
    Description: Rules that define how oss bucket manages objects during their lifetime.
  ServerSideEncryptionConfiguration:
    Type: Json
    Description: Specifies the bucket used to store the server-side encryption rule.
  AccessControl:
    Type: String
    Description: The access control list.
    AllowedValues:
      - private
      - public-read
      - public-read-write
    Default: private
  Tags:
    Type: Json
    Description: Bucket tags in k-v pairs format.
Resources:
  Bucket:
    Type: 'ALIYUN::OSS::Bucket'
    Properties:
      Policy:
        Ref: Policy
      CORSConfiguration:
        Ref: CORSConfiguration
      DeletionForce:
        Ref: DeletionForce
      BucketName:
        Ref: BucketName
      StorageClass:
        Ref: StorageClass
      LoggingConfiguration:
        Ref: LoggingConfiguration
      WebsiteConfiguration:
        Ref: WebsiteConfiguration
      RefererConfiguration:
        Ref: RefererConfiguration
      LifecycleConfiguration:
        Ref: LifecycleConfiguration
      ServerSideEncryptionConfiguration:
```

```
        Ref: ServerSideEncryptionConfiguration
      AccessControl:
        Ref: AccessControl
      Tags:
        Ref: Tags
Outputs:
  DomainName:
    Description: The public DNS name of the specified bucket.
    Value:
      'Fn::GetAtt':
        - Bucket
        - DomainName
  InternalDomainName:
    Description: The internal DNS name of the specified bucket.
    Value:
      'Fn::GetAtt':
        - Bucket
        - InternalDomainName
  Name:
    Description: The name of Bucket
    Value:
      'Fn::GetAtt':
        - Bucket
        - Name
```

To view more examples, visit Bucket.json and Bucket.yml.

### RDS

#### ALIYUN::RDS::Account

ALIYUN::RDS::Account is used to create a database account for an ApsaraDB for RDS instance.

**Syntax**

```json
  "Type": "ALIYUN::RDS::Account",
  "Properties": {
    "AccountDescription": String,
    "DBInstanceId": String,
    "AccountPassword": String,
    "AccountType": String,
    "AccountName": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountDescripti on | String | No | Yes | The description of the database account. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), _ and hyphens(-). It must start with a letter. |

| DBInstanceId | String | Yes | No | The ID of the instance. | None |
|---|---|---|---|---|---|
| AccountPasswor d | String | Yes | No | The password of the database account. | The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @#$&amp;%^* () +-= _ |
| AccountType | String | No | No | The type of the database account. | Default value: Normal. Valid values: Normal: standard account Super: privileged account Note Privileged accounts in ApsaraDB RDS for SQL Server instances cannot be deleted. |
| AccountName | String | Yes | No | The name of the database account. | None |

**Response parameters**

Fn::GetAtt AccountName: the name of the database account.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DBInstanceId:
    Type: String
    AssociationProperty: ALIYUN::RDS::Instance::InstanceId
Resources:
  Account:
    Type: ALIYUN::RDS::Account
    Properties:
      DBInstanceId:
        Ref: DBInstanceId
      AccountType: Normal
      AccountPassword: Admin@123!
      AccountName: Test
Outputs: {}
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "DBInstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::RDS::Instance::InstanceId"
```

`},`

```json
  "Resources": {
    "Account": {
      "Type": "ALIYUN::RDS::Account",
      "Properties": {
        "DBInstanceId": {
          "Ref": "DBInstanceId"
```

`},`

```json
        "AccountType": "Normal",
        "AccountPassword": "Admin@123!",
        "AccountName": "Test"
```

`},`

```json
  "Outputs": {
```

#### ALIYUN::RDS::AccountPrivilege

ALIYUN::RDS::AccountPrivilege is used to grant database access permissions to accounts.

**Statement**

```json
  "Type": "ALIYUN::RDS::AccountPrivilege",
  "Properties": {
    "AccountPrivilege": String,
    "DBInstanceId": String,
    "DBName": String,
    "AccountName": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountPrivilege | String | No | Yes | The permissions of the database account. | Valid values: ReadWrite: has read and write permissions on the database. ReadOnly: The account has read-only permission on the database. DDLOnly: The account can run only data definition language (DDL) commands in the database. This is applicable to MySQL and MariaDB. DMLOnly: The account can run only data manipulation language (DML) commands in the database. This is applicable to MySQL and MariaDB. DBOwner: The account has full permissions on the database. This is applicable to SQL Server. |
| DBInstanceId | String | No | No | The ID of the RDS instance. | None |
| DBName | String | No | No | The name of the database. | None |
| AccountName | String | No | No | The name of the account. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

**Response parameters**

Fn::GetAtt None

**Sample request**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DBInstanceId:
    Type: String
    AssociationProperty: ALIYUN::RDS::Instance::InstanceId
Resources:
  AccountPrivilege:
    Type: ALIYUN::RDS::AccountPrivilege
    Properties:
      AccountPrivilege: ReadOnly
      DBInstanceId:
        Ref: DBInstanceId
      DBName: dev
      AccountName: DBUser
Outputs: {}
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "DBInstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::RDS::Instance::InstanceId"
```

`},`

```json
  "Resources": {
    "AccountPrivilege": {
      "Type": "ALIYUN::RDS::AccountPrivilege",
      "Properties": {
        "AccountPrivilege": "ReadOnly",
        "DBInstanceId": {
          "Ref": "DBInstanceId"
```

`},`

```json
        "DBName": "dev",
        "AccountName": "DBUser"
```

`},`

```json
  "Outputs": {}
```

#### ALIYUN::RDS::DBInstance

ALIYUN::RDS::DBInstance is used to create an ApsaraDB RDS instance.

**Syntax**

```json
  "Type": "ALIYUN::RDS::DBInstance",
  "Properties": {
    "PeriodType": String,
    "Category": String,
    "PrivateIpAddress": String,
    "ResourceGroupId": String,
    "TargetDedicatedHostIdForSlave": String,
    "DBInstanceNetType": String,
    "DBTimeZone": String,
    "DedicatedHostGroupId": String,
    "EncryptionKey": String,
    "PreferredBackupPeriod": List,
```

`p` `,`

```json
    "SecurityIPList": String,
    "SecurityGroupId": String,
    "DBIsIgnoreCase": Integer,
    "DBInstanceStorage": Integer,
    "DBMappings": List,
    "Port": Integer,
    "ConnectionStringPrefix": String,
    "ConnectionStringType": String,
    "MultiAZ": Boolean,
    "MaintainTime": String,
    "Engine": String,
    "DBParamGroupId": String,
    "DBInstanceDescription": String,
    "Tags": Map,
    "TargetDedicatedHostIdForMaster": String,
    "EngineVersion": String,
    "ZoneId": String,
    "DBInstanceClass": String,
    "AllocatePublicConnection": Boolean,
    "PreferredBackupTime": String,
    "VSwitchId": String,
    "BackupPolicyMode": String,
    "Period": Integer,
    "PayType": String,
    "DBInstanceStorageType": String,
    "RoleARN": String,
    "MasterUserPassword": String,
    "MasterUserType": String,
    "VpcId": String,
    "MasterUsername": String,
    "ConnectionMode": String,
    "BackupRetentionPeriod": Number,
    "TargetDedicatedHostIdForLog": String,
    "SlaveZoneIds": List,
    "AutoRenew": Boolean,
    "SQLCollectorStatus": String,
    "SSLSetting": String,
    "LogBackupFrequency": String,
    "EnableBackupLog": Boolean,
    "ReleasedKeepPolicy": String,
    "ArchiveBackupRetentionPeriod": Integer,
    "ArchiveBackupKeepPolicy": String,
    "ArchiveBackupKeepCount": Integer,
    "LogBackupRetentionPeriod": Integer,
    "HighSpaceUsageProtection": String,
    "LocalLogRetentionSpace": Integer,
    "BackUpCategory": String,
    "CompressType": Integer,
    "LocalLogRetentionHours": Integer,
    "LogBackupLocalRetentionNumber": Integer,
    "ServerlessConfig": Map
```

**Properties**

| Property | Type | Require d | Updata ble | Description | Constraint |
|---|---|---|---|---|---|

| ResourceGroupI d | String | No | Yes | The ID of the resource group. | None. |
|---|---|---|---|---|---|
| Engine | String | Yes | No | The database engine. | Valid values: MySQL SQLServer PostgreSQL PPAS MariaDB |
| DBInstanceStor age | Integer | Yes | Yes | The storage capacity of the instance. | Valid values: MySQL: 5 to 1000. SQLServer: 10 to 1000. PostgreSQL: 5 to 2000. PPAS: 5 to 2000. Unit: GB. Note The value must be a multiple of 5 GB. |
| EngineVersion | String | Yes | No | The database engine version. | Valid values: MySQL: 5.5, 5.6, 5.7, and 8.0. SQLServer: 2008r2, 08r2 ent ha, 2012, _ _ 2012 ent ha, 2012 std ha, _ _ _ _ 2012 web, 2014 std ha, _ _ _ 2016 ent ha, 2016 std ha, _ _ _ _ 2016 web, 2017 std ha, _ _ _ 2017 ent, and 2019 ent. _ _ PostgreSQL: 9.4, 10.0, 11.0, and 12.0. PPAS: 9.3 and 10.0. MariaDB: 10.3. |
| Port | Integer | No | Yes | The port of the instance. | None. |
| ConnectionStrin gPrefix | String | No | Yes | The prefix of the endpoint. | The prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). |
| ConnectionStrin gType | String | No | Yes | The type of the endpoint. | Valid values: Inner: private. Public: public. |

| DBTimeZone | String | No | No | The UTC time zone. | Valid values: -12:59 to +13:00. Note If you do not specify this parameter, the system uses the default time zone of the region. If you create an instance with local SSDs attached, you can name the time zone. |
|---|---|---|---|---|---|
| DBParamGroupI d | String | No | No | The ID of the parameter template. | None. |
| Category | String | No | No | The instance series. | Valid values: Basic: Basic Edition. HighAvailability: High- Availability Edition. AlwaysOn: Cluster Edition. Finance: Enterprise Edition. |
| TargetDedicate dHostIdForMast er | String | No | No | The ID of the host on which you want to create the primary instance within a dedicated cluster. | None. |
| DBIsIgnoreCase | Integer | No | No | Specifies whether table names are case- sensitive. | Valid values: 0: Table names are case- sensitive. 1 (default): Table names are not case-sensitive. |
| EncryptionKey | String | No | No | The ID of the key used for cloud disk encryption in the region where the instance resides. You can view the key ID from the Key Management Service (KMS) console or create a key. | If you specify this property, the system enables cloud disk encryption and you must also specify RoleARN. You cannot disable cloud disk encryption after you enable it. |
| MaintainTime | String | No | No | The maintenance window of the instance. | Format: HH:mmZ-HH:mmZ (UTC time). |

| TargetDedicate dHostIdForSlav e | String | No | No | The ID of the host on which you want to create the secondary instance within a dedicated cluster. | None. |
|---|---|---|---|---|---|
| DedicatedHost GroupId | String | No | No | The ID of the dedicated cluster in which you want to create the instance. | None. |
| DBInstanceStor ageType | String | No | No | The storage type of the instance. | Valid values: local ssd: local SSD _ (recommended). cloud ssd: standard SSD. _ cloud essd: enhanced SSD _ (ESSD). |
| RoleARN | String | No | No | The Alibaba Cloud Resource Name (ARN) of the role. An ApsaraDB RDS instance can use this role to access KMS. | None. |
| DBInstanceClas s | String | Yes | Yes | The instance type. | None. |
| SecurityIPList | String | Yes | Yes | The whitelist of IP addresses that are allowed to access all databases on the instance. | Separate IP addresses with commas (,). Each IP address in the whitelist must be unique. You can specify up to 1,000 IP addresses. Supported formats: IP address. Example: 10.23.XX.XX. CIDR block. Example: 10.23.XX.XX/24. In this example, 24 indicates that the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value that ranges from 1 to 32. |
| SecurityGroupI d | String | No | Yes | The ID of the associated security group. | You can associate up to three security groups. Separate security group IDs with commas (,). To disassociate the instance from all security groups, set this property to an empty string. |
| MultiAZ | Boolean | No | No | Specifies whether the database instance can be deployed across multiple zones. | Valid values: true false |
| VpcId | String | No | No | The ID of the virtual private cloud. | None. |

| DBMappings | List | No | No | The database that you want to create on the instance. | For more information, see DBMappings properties. |
|---|---|---|---|---|---|
| DBInstanceDes cription | String | No | No | The description or remark of the instance. | The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, underscores ( ), and hyphens (-). _ |
| ConnectionMod e | String | No | No | The connection mode of the database. | Valid values: Standard: standard access mode. Safe: database proxy mode. If you do not specify this property, the system assigns a connection mode. Note SQL Server 2012, 2016, and 2017 support only the standard access mode. |
| MasterUsernam e | String | No | No | The name of the primary account for the database instance. | The name must be globally unique and can be up to 16 characters in length. It must start with a letter and can contain letters, digits, and underscores ( ). _ |
| MasterUserPass word | String | No | No | The password of the primary account for the database instance. | The password must be 8 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| ZoneId | String | No | No | The zone ID. | None. |
| DBInstanceNet Type | String | No | No | The network type of the database instance. | Valid values: Internet Intranet (default) |
| VSwitchId | String | No | No | The vSwitch ID. | Separate values with commas (,). You must specify this property if Engine is set to MariaDB. |
| BackupPolicyM ode | String | No | No | The backup type. | Valid values: DataBackupPolicy: data backup. LogBackupPolicy: log backup. |
| AllocatePublicC onnection | Boolean | No | No | Specifies whether to apply for a public endpoint for the instance. | Valid values: true false |

| PreferredBacku pTime | String | No | No |   | The backup time. | Format: HH:mmZ- HH:mmZ . Valid values: 00:00Z-01:00Z, 01:00Z-02:00Z, 02:00Z-03:00Z, 03:00Z-04:00Z, 04:00Z-05:00Z, 05:00Z-06:00Z, 06:00Z-07:00Z, 07:00Z-08:00Z, 08:00Z-09:00Z, 09:00Z-10:00Z, 10:00Z-11:00Z, 11:00Z-12:00Z, 12:00Z-13:00Z, 13:00Z-14:00Z, 14:00Z-15:00Z, 15:00Z-16:00Z, 16:00Z-17:00Z, 17:00Z-18:00Z, 18:00Z-19:00Z, 19:00Z-20:00Z, 20:00Z-21:00Z, 21:00Z-22:00Z, 22:00Z-23:00Z, and 23:00Z-24:00Z. |
|---|---|---|---|---|---|---|
| BackupRetentio nPeriod | Number | No | No |   | The number of days for which the backup can be retained. | Valid values: 7 to 30. Unit: days. Default value: 7. |
| PrivateIpAddres s | String | No | No |   | The private IP address under the VSwitchId. | If you do not specify this property, the system automatically assigns a private IP address. |
| PreferredBacku pPeriod | List | No | No |   | The backup cycle. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| MasterUserTyp e | String | No | No |   | The type of the primary account. | Valid values: Normal (default): standard account. Super: privileged account. Sysadmin: administrator account. Note You can set this property to Sysadmin only when Engine is set to SQLServer. |
| Tags | Map | No | Yes |   | The tags. Each tag consists of a tag key and a tag value. | The tag key is required, and the tag value is optional. Format example: {“key1”:”value1”,“key2”:””} . |
| PeriodType | String | No | No |   | The period type. | Valid values: Month (default) Year |

| PayType | String | No | No | The billing method of the instance. | Valid values: Postpaid: pay-as-you-go. Prepaid: subscription. |   |   |
|---|---|---|---|---|---|---|---|
| Period | Integer | No | No | The subscription duration. | Valid values: When PeriodType is set to Year: 1 to 3. When PeriodType is set to Month: 1 to 9. |   |   |
| TargetDedicate dHostIdForLog | String | No | No | The ID of the host on which you want to create the logger instance within a dedicated cluster. | None. |   |   |
| SlaveZoneIds | List | No | No | The ID of the secondary zone for the High-Availability Edition or Enterprise Edition instance. | You can specify up to two secondary zones. Example: ["zone-b"] or ["zone-b", "zone-c"] . Specify a vSwitch for each primary or secondary zone. For example, if ZoneId= "zone-a" and SlaveZoneIds= ["zone-c", "zone-b"] , set VSwitchID to "vsw-zone-a,vsw-zone- c,vsw-zone-b" . |   |   |
|   |   |   |   |   |   | ["zone-b", |   |
| SQLCollectorSt atus | String | No | Yes | Specifies whether to enable SQL Explorer (SQL Audit). | Valid values: Enable Disabled |   |   |
| SSLSetting | String | No | No | The Secure Sockets Layer (SSL) connection settings of the instance. | Valid values: Disabled (default): disables the SSL connection. EnabledForPublicConnection: enables the SSL connection. SSL certificates are used to protect public endpoints. Note When this property is set to EnabledForPublicConnection , you must set AllocatePublicConnection to true. EnabledForInnerConnection: enables the SSL connection. SSL certificates are used to protect private endpoints. |   |   |

|   |   | ["zone-b"] |
|---|---|---|
|   | "zone-c"] |   |

| nterprise ance. | "zone-b"] |
|---|---|

| AutoRenew | Boolean | No | No | Specifies whether to enable auto-renewal. | Specify this parameter only when you create a subscription instance. Valid values: true false Note If you set PeriodType to Month, the auto- renewal cycle is one month. If you set PeriodType to Year, the auto- renewal cycle is one year. |
|---|---|---|---|---|---|
| LogBackupFreq uency | String | No | No | The log backup frequency. | Valid value: LogInterval, which indicates a backup every 30 minutes. The default value of LogBackupFrequency is the same as that of PreferredBackupPeriod. Note LogBackupFrequency is supported only when Engine is set to SQLServer. |
| EnableBackupL og | Boolean | No | No | Specifies whether to enable the log backup feature. | Valid values: true false Note You must specify this property when you set BackupPolicyMode to LogBackupPolicy. |
| ReleasedKeepP olicy | String | No | No | The policy used to retain archived backups after the instance is released. | Valid values: Lastest: retains only the last archived backup. All: retains all archived backups. |
| ArchiveBackup RetentionPeriod | Integer | No | No | The number of days for which the archived backup can be retained. | Valid values: 30 to 1095. Unit: days. |
| ArchiveBackup KeepPolicy | String | No | No | The cycle based on which the archived backup is retained. | Valid values: ByMonth ByWeek KeepAll |

| ArchiveBackup KeepCount | Integer | No | No | The number of archive backups that can be retained. | Valid values: When you set ArchiveBackupKeepPolicy to ByMonth: 1 to 31. When you set ArchiveBackupKeepPolicy to ByWeek: 1 to 7. When you set ArchiveBackupKeepPolicy to KeepAll: you can leave this property empty. Default value: 1. |
|---|---|---|---|---|---|
| LogBackupRete ntionPeriod | Integer | No | No | The number of days for which the log backup can be retained. | Valid values: 7 to 730. The retention period of log backups cannot be longer than that of data backups. Note You can specify the retention period of log backups if you enable the log backup feature. |
| HighSpaceUsag eProtection | String | No | No | Specifies whether to forcefully delete log backup files when the disk capacity is insufficient. The capacity is considered insufficient if the storage usage of your instance exceeds 80% or the remaining storage capacity is less than 5 GB. | Valid values: Enable Disable You must specify this property when you set BackupPolicyMode to LogBackupPolicy. |
| LocalLogRetenti onSpace | Integer | No | No | The maximum percentage of space that can be used to store log backup files on the instance. | Valid values: 0 to 50. If the space used by log backup files exceeds the value of this property, the system deletes the earliest log backup file until the space usage drops below the value of this property. Note You must specify this property when you set BackupPolicyMode to LogBackupPolicy. |
| BackUpCategor y | String | No | No | Specifies whether to enable the secondary backup feature. | Valid values: Flash: enables the secondary backup feature. Standard: disables the secondary backup feature. |

| CompressType | Integer | No | No | The backup compression method. | Valid values: 1: uses the zlib tool to compress backups into .tar.gz files. 4: uses QuickLZ to compress backups into .xb.gz files. This method is supported only for instances that run MySQL 5.6 or MySQL 5.7. You can use this method to restore individual databases and tables. 8: uses QuickLZ to compress backups into .xb.gz files. This method is supported only for instances that run MySQL 8.0. You cannot use this method to restore individual databases and tables. |
|---|---|---|---|---|---|
| LocalLogRetenti onHours | Integer | No | No | The number of hours for which the local log backups can be retained on the instance. | Valid values: 0 to 168. Unit: hours. A value of 0 indicates that the log backup files are not retained on the instance. Note You must specify this property when you set BackupPolicyMode to LogBackupPolicy. |
| LogBackupLoca lRetentionNum ber | Integer | No | No | The number of log backup files that can be retained on the instance. | Valid values: 6 to 100. Default value: 60. |
| ServerlessConfi g | Map | No | No | The settings of the serverless instance. | For more information, see ServerlessConfig properties. |

**ServerlessConfig syntax**

```json
"ServerlessConfig": {
    "SwitchForce": Boolean,
    "MaxCapacity": Number,
    "MinCapacity": Number,
    "AutoPause": Boolean
```

**ServerlessConfig properties**

| Parameter | Type | Required | Update allowed | Desc ripti on | Constraint |
|---|---|---|---|---|---|

| SwitchForce | Boolean | No | No | Speci fies whet her to enabl e force d scali ng for the serve rless insta nce. | Valid values: true false (default) Note If you set this property to true, a transient disconnection that lasts for up to one minute occurs during the forced scaling process of the instance. Exercise caution when you specify this property. In most cases, the scaling for RDS Capacity Units (RCUs) of a serverless instance immediately takes effect. In some cases, such as the executions of large transactions, the scaling does not immediately take effect. In this case, you can enable forced scaling to forcefully scale the RCUs of the instance. |
|---|---|---|---|---|---|
| MaxCapacity | Number | Yes | No | The maxi mum value of the scali ng rang e for the RCU. | Valid values: 0.5 to 8. Note The value of this property must be greater than or equal to the value of MinCapacity. |

| MinCapacity | Number | Yes | No | The mini mum value of the scali ng rang e for the RCU. | Valid values: 0.5 to 8. Note The value of this property must be less than or equal to the value of MaxCapacity. |
|---|---|---|---|---|---|
| AutoPause | Boolean | No | No | Speci fies whet her to enabl e auto matic start and stop for the serve rless insta nce. | Valid values: true false (default) Note After the automatic start and stop feature is enabled, if no connections to the instance are established within 10 minutes, the instance stops. When a new connection to the instance is established, the instance automatically starts. |

**DBMappings syntax**

```json
"DBMappings": [
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
```

`]`

**DBMappings properties**

| Parameter | Type | Required | Update allowed | Descriptio n | Constraint |
|---|---|---|---|---|---|

| CharacterSetName | String | Yes | No | The character set. | Valid values: MySQL: utf8 gbk latin1 utf8mb4 (applicable to version 5.5 and version 5.6) SQL Server: Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ |
|---|---|---|---|---|---|
| DBName | String | Yes | No | The database name. | The name must be globally unique. The name can be up to 64 characters in length. It must start with a letter and can contain letters, digits, and underscores ( ). _ |
| DBDescription | String | No | No | The database description. | The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, underscores ( ), and _ hyphens (-). |

**Return values**

Fn::GetAtt DBInstanceId: the ID of the database instance. InnerPort: the private port of the database instance. InnerIPAddress: the private IP address. InnerConnectionString: the private endpoint. PublicPort: the public port of the database instance. PublicConnectionString: the public endpoint. PublicIPAddress: the public IP address.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test RDS DBInstance Parameters:
  VpcId:
    AssociationProperty: ALIYUN::ECS::VPC::VPCId
    Type: String
    Description:
      en: Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud
```

`zh-cn:` 现有虚拟专有网络的实例`ID`

```
    Label:
      en: VPC ID
```

`zh-cn:` 专有网络`VPC`实例`ID`

```
  VSwitchId:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
      ZoneId: ${VSwitchZoneId}
    Type: String
    Description:
      en: Instance ID of existing business network switches, console-Virtual Private Cloud-VSwitche
s under query
```

`zh-cn:` 现有业务网络交换机的实例`ID`

```
    Label:
      en: VSwitch ID
```

`zh-cn:` 交换机实例`ID`

```
Resources:
  RDSInstance:
    DependsOn: VSwitch
    Type: ALIYUN::RDS::DBInstance
    Properties:
      VpcId:
        Ref: VpcId
      VSwitchId:
        Ref: VSwitchId
      EngineVersion: '5.6'
      DBInstanceClass: rds.mysql.s2.large
      SecurityIPList: 0.0.0.0/0
      DBInstanceStorage: 5
      Engine: MySQL
      DBMappings:
        - CharacterSetName: utf8
          DBName: DBTest
Outputs:
  DBInstanceId:
    Value:
      Fn::GetAtt:
        - RDSInstance
        - DBInstanceId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test RDS DBInstance",
  "Parameters": {
    "VpcId": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Description": {
        "en": "Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud",
```

`"zh-cn": "`现有虚拟专有网络的实例`ID"` `},` `"`

```
bl"
```

```json
      "Label": {
        "en": "VPC ID",
```

`"zh-cn": "`专有网络`VPC`实例`ID"` `},`

```json
    "VSwitchId": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "${VpcId}",
        "ZoneId": "${VSwitchZoneId}"
```

`},`

```json
      "Type": "String",
      "Description": {
        "en": "Instance ID of existing business network switches, console-Virtual Private Cloud-VSw
itches under query",
```

`"zh-cn": "`现有业务网络交换机的实例`ID"` `},`

```json
      "Label": {
        "en": "VSwitch ID",
```

`"zh-cn": "`交换机实例`ID"` `},`

```json
  "Resources": {
    "RDSInstance": {
      "DependsOn": "VSwitch",
      "Type": "ALIYUN::RDS::DBInstance",
      "Properties": {
        "VpcId": {
          "Ref": "VpcId"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "EngineVersion": "5.6",
        "DBInstanceClass": "rds.mysql.s2.large",
        "SecurityIPList": "0.0.0.0/0",
        "DBInstanceStorage": 5,
        "Engine": "MySQL",
        "DBMappings": [
            "CharacterSetName": "utf8",
            "DBName": "DBTest"
```

`]` `},`

```json
  "Outputs": {
    "DBInstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "RDSInstance",
          "DBInstanceId"
```

`]` For more examples, see the combined examples of creating a database instance, creating an account to manage databases, granting the account access to databases, modifying the database parameter list, modifying the IP address whitelist for an instance, creating a read-only instance for an instance, and creating a database under an instance: JSON example and YAML example.

#### ALIYUN::RDS::DBInstanceParameterGroup

ALIYUN::RDS::DBInstanceParameterGroup is used to modify the parameters of an ApsaraDB RDS instance.

**Syntax**

```json
  "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
  "Properties": {
    "Forcerestart": String,
    "DBInstanceId": String,
    "Parameters": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | Yes | No | The ID of the instance. | N/A |
| Parameters | List | Yes | Yes | The parameters of the instance. | For more information, see Parameters properties. |
| Forcerestart | String | No | Yes | Specifies whether to forcibly restart the instance. | Valid values: true: The system forcibly restarts the instance. false: The system does not forcibly restart the instance. This is the default value. |

**Parameters syntax**

```json
"Parameters": [
    "Key": String,
    "Value": String
```

`]`

**Parameters properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The name of the parameter. | N/A |
| Value | String | Yes | No | The value of the parameter. | N/A |

**Response parameters**

Fn::GetAtt N/A

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DBInstanceId:
    Type: String
    AssociationProperty: ALIYUN::RDS::Instance::InstanceId
Resources:
  DBInstanceParameterGroup:
    Type: ALIYUN::RDS::DBInstanceParameterGroup
    Properties:
      Parameters:
        - Key: back_log
          Value: '3000'
        - Key: wait_timeout
          Value: '86400'
      DBInstanceId:
        Ref: DBInstanceId
      Forcerestart: 'false'
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "DBInstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::RDS::Instance::InstanceId"
```

`},`

```json
  "Resources": {
    "DBInstanceParameterGroup": {
      "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
      "Properties": {
        "Parameters": [
            "Key": "back_log",
            "Value": "3000"
```

`},`

```json
            "Key": "wait_timeout",
            "Value": "86400"
```

`],`

```json
        "DBInstanceId": {
          "Ref": "DBInstanceId"
```

`},`

```json
        "Forcerestart": "false"
```

#### ALIYUN::RDS::DBInstanceSecurityIps

ALIYUN::RDS::DBInstanceSecurityIps is used to modify an IP address whitelist of an ApsaraDB for RDS instance.

**Syntax**

```json
  "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
  "Properties": {
    "DBInstanceId": String,
    "DBInstanceIPArrayName": String,
    "DBInstanceIPArrayAttribute": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | Yes | No | The ID of the instance. | None |
| DBInstanceIPArr ayAttribute | String | Yes | Yes | The attribute of the IP address whitelist. | Whitelists that have the "hidden" attribute are not displayed in the console. |
| DBInstanceIPArr ayName | String | No | No | The name of the IP address whitelist. | The name can only contain lowercase letters and underscores ( ). _ Default value: Default. |

**Response parameters**

Fn::GetAtt SecurityIps: the IP address whitelist after the modification.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  RDSInstance:
    Type: String
    AssociationProperty: ALIYUN::RDS::Instance::InstanceId
Resources:
  DBInstanceSecurityIps:
    Type: ALIYUN::RDS::DBInstanceSecurityIps
    Properties:
      DBInstanceId:
        Ref: RDSInstance
      DBInstanceIPArrayAttribute: 0.0.0.0/0
Outputs:
  SecurityIps:
    Description: The security ips of selected database instance.
    Value:
      Fn::GetAtt:
        - DBInstanceSecurityIps
        - SecurityIps
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "RDSInstance": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::RDS::Instance::InstanceId"
```

`},`

```json
  "Resources": {
    "DBInstanceSecurityIps": {
      "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
      "Properties": {
        "DBInstanceId": {
          "Ref": "RDSInstance"
```

`},`

```json
        "DBInstanceIPArrayAttribute": "0.0.0.0/0"
```

`},`

```json
  "Outputs": {
    "SecurityIps": {
      "Description": "The security ips of selected database instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstanceSecurityIps",
          "SecurityIps"
```

`]`

#### ALIYUN::RDS::PrepayDBInstance

ALIYUN::RDS::PrepayDBInstance is used to create subscription ApsaraDB RDS instances.

**Syntax**

```json
  "Type": "ALIYUN::RDS::PrepayDBInstance",
  "Properties": {
    "DBMappings": List,
    "CouponCode": String,
    "MasterUsername": String,
    "PeriodType": String,
    "DBInstanceNetType": String,
    "MasterUserType": String,
    "AutoRenew": Boolean,
    "PreferredBackupTime": String,
    "PrivateIpAddress": String,
    "Engine": String,
    "MultiAZ": Boolean,
    "VpcId": String,
    "ConnectionMode": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "BackupRetentionPeriod": Number,
    "Quantity": Number,
    "CommodityCode": String,
    "ZoneId": String,
    "AutoPay": Boolean,
    "Port": Integer,
```

```json
ot: tege,
    "ConnectionStringPrefix": String,
    "SubscriptionDeletionForce": Boolean,
    "ConnectionStringType": String,
    "EngineVersion": String,
    "DBInstanceClass": String,
    "PreferredBackupPeriod": List,
    "DBInstanceStorage": Integer,
    "DBInstanceDescription": String,
    "Tags": Map,
    "Period": Number,
    "MasterUserPassword": String,
    "AllocatePublicConnection": Boolean,
    "SlaveZoneIds": List,
    "TargetDedicatedHostIdForMaster": String,
    "RoleARN": String,
    "DBInstanceStorageType": String,
    "Category": String,
    "DBParamGroupId": String,
    "EncryptionKey": String,
    "DBIsIgnoreCase": Integer,
    "SecurityGroupId": String,
    "TargetDedicatedHostIdForLog": String,
    "DBTimeZone": String,
    "DedicatedHostGroupId": String,
    "TargetDedicatedHostIdForSlave": String,
    "MaintainTime": String,
    "SQLCollectorStatus": String,
    "SSLSetting": String,
    "ArchiveBackupRetentionPeriod": Integer,
    "LogBackupRetentionPeriod": Integer,
    "EnableBackupLog": Boolean,
    "LogBackupLocalRetentionNumber": Integer,
    "ArchiveBackupKeepPolicy": String,
    "LocalLogRetentionHours": Integer,
    "HighSpaceUsageProtection": String,
    "CompressType": Integer,
    "LogBackupFrequency": String,
    "BackupPolicyMode": String,
    "ArchiveBackupKeepCount": Integer,
    "LocalLogRetentionSpace": Integer,
    "ReleasedKeepPolicy": String,
    "BackUpCategory": String,
    "ServerlessConfig": Map,
    "InstanceNetworkType": String,
    "StorageAutoScale": String,
    "StorageUpperBound": Number,
    "StorageThreshold": Number,
    "IoAccelerationEnabled": String,
    "ColdDataEnabled": Boolean,
    "BurstingEnabled": Boolean,
    "DeletionProtection": Boolean
```

**Properties**

| Property | Type | Requir ed | Editabl e | Descri ption | Constraint |
|---|---|---|---|---|---|

| ResourceGro upId | String | No | Yes | The ID of the resourc e group. | None. |
|---|---|---|---|---|---|
| DBMappings | List | No | No | The databa ses that you want to create on the instanc e. | For more information, see DBMappings properties. |
| CouponCode | String | No | No | The coupon code. | None. |
| MasterUserna me | String | No | Yes | The name of the databa se accoun t of the instanc e. | The name must be globally unique. It must be 2 to 16 characters in length. It must start with a letter and end with a letter or digit. It can contain letters, digits, and underscores ( ). _ |
| PeriodType | String | Yes | No | The unit of the subscri ption duratio n. | Valid values: Year Month (default) |
| AutoUpgrade MinorVersion | String | No | Yes | The instanc e minor version upgrad e method . | Valid values: Auto: Automatically upgrades to the minor version. Manual: Does not upgrade automatically. Only forces an upgrade when the current version is no longer supported. |
| DBInstanceN etType | String | No | No | The networ k connec tion type of the instanc e. | Valid values: Internet Intranet (default) |

| MasterUserTy pe | String | No | No | The type of the databa se accoun t. | Valid values: Normal (default): standard account Super: privileged account Sysadmin: system admin account Note System admin accounts support only SQL Server databases. |
|---|---|---|---|---|---|
| Port | Integer | No | Yes | The port of the instanc e. | None. |
| ConnectionSt ringPrefix | String | No | Yes | The prefix of the endpoi nt. | The prefix must be 8 to 64 characters in length, and can contain letters, digits, and hyphens (-). |
| ConnectionSt ringType | String | No | Yes | The endpoi nt type. | Valid values: Inner: private Public: public |
| PreferredBac kupTime | String | No | Yes | The backup time. | Specify the time in the HH:mmZ-HH:mmZ format. Valid values: 00:00Z-01:00Z, 01:00Z-02:00Z, 02:00Z- 03:00Z, 03:00Z-04:00Z, 04:00Z-05:00Z, 05:00Z-06:00Z, 06:00Z-07:00Z, 07:00Z-08:00Z, 08:00Z-09:00Z, 09:00Z- 10:00Z, 10:00Z-11:00Z, 11:00Z-12:00Z, 12:00Z-13:00Z, 13:00Z-14:00Z, 14:00Z-15:00Z, 15:00Z-16:00Z, 16:00Z- 17:00Z, 17:00Z-18:00Z, 18:00Z-19:00Z, 19:00Z-20:00Z, 20:00Z-21:00Z, 21:00Z-22:00Z, 22:00Z-23:00Z, and 23:00Z-24:00Z. |
| PrivateIpAddr ess | String | No | No | The private IP addres s that corresp onds to the vSwitch . | If you do not specify this property, the system automatically assigns a private IP address. |
| Engine | String | Yes | No | The type of the databa se engine. | Valid values: MySQL SQLServer PostgreSQL PPAS MariaDB |

| MultiAZ | Boolea n | No | No | Specifi es whethe r to deploy the instanc e across zones. | Valid values: true false |
|---|---|---|---|---|---|
| VpcId | String | No | No | The ID of the virtual private cloud (VPC). | None. |
| ConnectionM ode | String | No | No | The connec tion mode of the databa se. | Valid values: Standard: standard mode Note Instances that run SQL Server 2012, SQL Server 2016, and SQL Server 2017 support only the standard mode. Safe (default): database proxy mode If you do not specify this property, the system assigns a connection mode by default. |
| AutoRenew | Boolea n | No | No | Specifi es whethe r to enable auto- renewa l for the instanc e. | Valid values: true false |
| VSwitchId | String | No | No | The vSwitch ID. | None. |

| BackupReten tionPeriod | Numbe r | No | Yes | The numbe r of days for which you can retain the backup data. | None. |
|---|---|---|---|---|---|
| Quantity | Numbe r | No | No | The numbe r of instanc es that you want to create. | Valid values: 1 to 99. Default value: 1. |
| CommodityC ode | String | Yes | No | The commo dity code. | Valid values: rds bards rords |

| Subscription DeletionForce | Boolea n | No | No | This propert y takes effect only for subscri ption instanc es. If you set this propert y to true for a subscri ption instanc e, the instanc e is change d to a pay-as- you-go one before the instanc e is forceful ly deleted . If you set this propert y to false for a subscri ption instanc e, the instanc e is not forceful ly deleted . This propert y involve s additio nal fees. Exercis e caution when you specify this propert y. | None. |
|---|---|---|---|---|---|
| ZoneId | String | No | No | The zone ID. | None. |

| EngineVersio n | String | Yes | No | The version of the databa se engine. | Valid values: Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0. Valid values when Engine is set to SQLServer: 2008r2, 08r2 ent ha, 2012, 2012 ent ha, _ _ _ _ 2012 std ha, 2012 web, 2014 std ha, 2016 ent ha, _ _ _ _ _ _ _ 2016 std ha, 2016 web, 2017 std ha, 2017 ent, and _ _ _ _ _ _ 2019 ent. _ Valid values when Engine is set to PostgreSQL: 9.4, 10.0, 11.0, and 12.0. Valid values when Engine is set to PPAS: 9.3 and 10.0. Valid value when Engine is set to MariaDB: 10.3. |
|---|---|---|---|---|---|
| DBInstanceCl ass | String | Yes | Yes | The instanc e type. | Examples: rds.mys2.large, rds.mss1.large, and rds.pg.s1.small. |
| PreferredBac kupPeriod | List | No | Yes | The day of a week on which you want to back up data. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| DBInstanceSt orage | Integer | Yes | Yes | The storage capacit y of the instanc e. | Valid values: Valid values when Engine is set to MySQL: 5 to 1000. Valid values when Engine is set to SQLServer: 10 to 1000. Valid values when Engine is set to PostgreSQL or PPAS: 5 to 2000. Unit: GB. Note The value of DBInstanceStorage must be in increments of 5 GB. |
| DBInstanceD escription | String | No | Yes | The descrip tion of the instanc e. | The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, underscores ( ), and hyphens (-). _ |
| Tags | Map | No | Yes | The tags. | None. |
| Period | Numbe r | Yes | No | The subscri ption duratio n. | Valid values: Valid values when PeriodType is set to Month: 1 to 9. Valid values when PeriodType is set to Year: 1 to 3. |

| MasterUserPa ssword | String | No |   | Yes |   | The passwo rd of the databa se accoun | The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ & ; % ^ * ( ) _ + - = . |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | t of the | + - = |   |
|   |   |   |   |   |   | instanc e. |   |   |
| AllocatePubli cConnection | Boolea n | No |   | No |   | Specifi es whethe r to apply for a public endpoi nt for the instanc e. | Valid values: true false |   |
| AutoPay | Boolea n | No |   | No |   | Specifi es whethe r to enable automa tic payme nt. | Valid values: true (default) false |   |
| SlaveZoneIds | List | No |   | No |   | The second ary zone IDs of the High- availab ility | You can specify up to two secondary zones. For example, you can set this property to ["zone-b"] or ["zone-b", "zone-c"] . You must specify a vSwitch for each primary or secondary zone. For example, if you set ZoneId to "zone-a" and SlaveZoneIds to ["zone-c", "zone-b"] , you must set VSwitchId to "vsw-zone- a,vsw-zone-c,vsw-zone-b" . If you want the system to automatically select a secondary zone, you must set SlaveZoneIds to ["Auto"] or ["Auto", "Auto"] . In this case, if you specify a vSwitch ID for the primary zone, the system automatically creates a vSwitch in the secondary zones. |   |
|   |   |   |   |   |   |   |   | "zone-a" |
|   |   |   |   |   |   | Edition | "zone-b"] , |   |
|   |   |   |   |   |   | or |   |   |
|   |   |   |   |   |   | Enterpr |   |   |
|   |   |   |   |   |   | ise Edition instanc e. |   |   |

| ! @ # $ & ; % ^ * ( ) _ |   |
|---|---|

| ["zone-c", |   |   |
|---|---|---|
|   | "vsw-zone- |   |

| TargetDedica tedHostIdFor Master | String | No | No | The host ID of the primar y instanc e that you want to create in a dedicat ed cluster. | None. |
|---|---|---|---|---|---|
| RoleARN | String | No | No | The Alibaba Cloud Resour ce Name (ARN) of the role. You can access Key Manag ement Service (KMS) from Apsara DB RDS by using the role. | None. |
| DBInstanceSt orageType | String | No | Yes | The storage type of the instanc e. | Valid values: local ssd (recommended): local SSD _ cloud ssd: standard SSD _ cloud essd: Enterprise SSD (ESSD) _ |
| Category | String | No | Yes | The edition of the instanc e. | Valid values: Basic: Basic Edition. HighAvailability: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
| DBParamGro upId | String | No | No | The ID of the parame ter templa te. | None. |

| EncryptionKe y | String | No | No | The ID of the key that is used for disk encrypt ion in the region where the instanc e resides . | You can obtain the key ID from the KMS console. You can also create a key. |
|---|---|---|---|---|---|
| DBIsIgnoreCa se | Integer | No | No | Specifi es whethe r the table names are case- insensit ive. | Valid values: 1 (default): The table names are not case-sensitive. 0: The table names are case-sensitive. |
| SecurityGrou pId | String | No | Yes | The ID of the securit y group. | You can associate the instance with up to three security groups. Separate security group IDs with commas (,). If you want to disassociate the instance from all security groups, leave this property empty. |
| TargetDedica tedHostIdFor Log | String | No | No | The host ID of the logger instanc e that you want to create in a dedicat ed cluster. | None. |
| DBTimeZone | String | No | No | The UTC time zone. | Valid values: -12:59 to +13:00. By default, if you do not specify this property, the system uses the default time zone of the region where the instance resides. If you create an instance to which local SSDs are attached, you can name the time zone. |

| DedicatedHo stGroupId | String | No | No | The ID of the dedicat ed cluster in which you want to create the instanc e. | None. |
|---|---|---|---|---|---|
| TargetDedica tedHostIdFor Slave | String | No | No | The host ID of the second ary instanc e that you want to create in a dedicat ed cluster. | None. |
| MaintainTime | String | No | No | The mainte nance window of the instanc e. | Specify the maintenance window in the HH:mmZ- HH:mmZ format. |
| SQLCollector Status | String | No | Yes | Specifi es whethe r to enable SQL Explore r and Audit. | Valid values: Enable Disabled |
| SSLSetting | String | No | No | The SSL connec tion setting s of the instanc e. | Valid values: Disabled (default): disables the SSL connection settings of the instance. EnabledForPublicConnection: enables the SSL connection settings of the instance. SSL certificates are used to protect public endpoints. Note If you set this property to EnabledForPublicConnection, you must set AllocatePublicConnection to true. EnabledForInnerConnection: enables the SSL connection settings of the instance. SSL certificates are used to protect private endpoints. |

| ArchiveBacku pRetentionPe riod | Integer | No | Yes | The numbe r of days for which you want to retain the archive d backup s. | None. |
|---|---|---|---|---|---|
| LogBackupRe tentionPeriod | Integer | No | Yes | The numbe r of days for which you want to retain the log backup s. | None. |
| EnableBacku pLog | Boolea n | No | Yes | Specifi es whethe r to enable log backup . | Valid values: true false |
| LogBackupLo calRetention Number | Integer | No | Yes | The numbe r of local binary logs that you want to retain. | None. |

| ArchiveBacku pKeepPolicy | String | No | Yes | The cycle based on which you want to retain the archive d backup s. | Valid values: ByMonth ByWeek KeepAll ArchiveBackupKeepCount determines the number of backups that can be retained within the cycle. The default number is 0. Note This property takes effect when BackupPolicyMode is set to DataBackupPolicy. |
|---|---|---|---|---|---|
| LocalLogRete ntionHours | Integer | No | Yes | The numbe r of hours for which you want to retain the local log backup s. | None. |

| HighSpaceUs ageProtection | String | No | Yes | Specifi es whethe r to forceful ly delete binary logs if the capacit y usage of the instanc e exceed s 80% or the remaini ng capacit y is less than 5 GB on the instanc e. | Valid values: Disable Enable |
|---|---|---|---|---|---|
| CompressTyp e | Integer | No | Yes | The method that you want to use to compre ss backup data. | Valid values: 0: does not compress backup data. 1: uses zlib to compress backup data. 2: uses zlib to compress backup data in parallel. 4: uses QuickLZ to compress backup data. You can use the compressed backup data to restore databases and tables. 8: uses QuickLZ to compress backup data. You cannot use the compressed backup data to restore databases and tables. This value is available only when the instance runs MySQL 8.0. |

| LogBackupFr equency | String | No | Yes | The frequen cy at which you want to back up logs. | This property is available when Engine is set to SQLServer. Set the value to LogInterval. A value of LogInterval specifies that the system backs up logs every 30 minutes. Note The default value of LogBackupFrequency is the same as the value of PreferredBackupPeriod. |
|---|---|---|---|---|---|
| BackupPolicy Mode | String | No | Yes | The backup type. | Valid values: DataBackupPolicy LogBackupPolicy |
| ArchiveBacku pKeepCount | Integer | No | Yes | The numbe r of archive d backup s that you want to retain. | None. |
| LocalLogRete ntionSpace | Integer | No | Yes | The maxim um capacit y usage of local logs on the instanc e. | None. |
| ReleasedKee pPolicy | String | No | Yes | The policy that you want to use to retain the archive d backup s if the instanc e is release d. | Valid values: None: does not retain archived backups. Lastest: retains only the most recent archived backup. All: retains all archived backups. |

| BackUpCateg ory | String | No | Yes | The edition of the backup instanc e. | Valid values: Basic: Basic Edition. HighAvailability: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
|---|---|---|---|---|---|
| ServerlessCo nfig | Map | No | No | The setting s of the serverl ess instanc e. | For more information, see ServerlessConfig properties. |
| InstanceNetw orkType | String | No | No | The networ k type of the instanc e. | Valid values: VPC Classic Note For the instance that runs MySQL and uses cloud disks, you must set this property to VPC. For the instance that runs PostgreSQL or MariaDB, you must set this property to VPC. For the instance that runs SQL Server Basic or SQL Server Web, you can set this property to VPC or Classic. For other types of instances, you must set this property to VPC. |
| StorageAutoS cale | String | No | No | Specifi es whethe r to enable automa tic storage expansi on. | This property is supported only when Engine is set to MySQL or PostgreSQL. Valid values: Enable Disable (default) Note You can also call the ModifyDasInstanceConfig operation to adjust the settings of automatic storage expansion for an instance after the instance is created. For more information, see Configure automatic storage expansion for an ApsaraDB RDS for MySQL instance. |

| StorageUpper Bound | Numbe r | No | No | The maxim um storage capacit y that is allowed for automa tic storage expansi on. | Automatic storage expansion does not cause the storage capacity of the instance to exceed the value of this property. Unit: GB. Note The value must be greater than or equal to 0. You must specify this property when StorageAutoScale is set to Enable. |
|---|---|---|---|---|---|
| StorageThres hold | Numbe r | No | No | The thresho ld based on which automa tic storage expansi on is trigger ed. Unit: %. | Valid values: 10 20 30 40 50 Note You must specify this property when StorageAutoScale is set to Enable. |
| IoAcceleratio nEnabled | String | No | No | Specifi es whethe r to enable I/O acceler ation. | Valid values: 1: enables I/O acceleration. 0: does not enable I/O acceleration. |
| ColdDataEna bled | Boolea n | No | No | This propert y is reserve d. | None. |
| BurstingEnab led | Boolea n | No | No | Specifi es whethe r to enable I/O burst. | Valid values: true false |

| DeletionProte ction | Boolea n | No | Yes | Specifi es whethe r to enable the deletio n protecti on feature . | Valid values: true false |
|---|---|---|---|---|---|

**ServerlessConfig syntax**

```json
"ServerlessConfig": {
    "SwitchForce": Boolean,
    "MaxCapacity": Number,
    "MinCapacity": Number,
    "AutoPause": Boolean
```

**ServerlessConfig properties**

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|

| SwitchForc e | Boolean | No | No | Specifies whether to enable forced scaling for the serverless instance. | Valid values: true false (default) Note If you set this property to true, a transient disconnection that lasts for approximately 1 minute occurs during the forced scaling process of the instance. Specify this property based on your business requirements. In most cases, the scaling for RDS Capacity Units (RCUs) of an instance immediately takes effect. In some cases, such as the executions of large transactions, the scaling does not immediately take effect. In this case, you can enable the forced scaling feature to forcefully scale the RCUs of the instance. |
|---|---|---|---|---|---|
| MaxCapacit y | Number | Yes | No | The maximum value of RCU scaling of the instance. | Valid values: 0.5 to 8. Note The value of this property must be greater than or equal to the value of MinCapacity. |
| MinCapacit y | Number | Yes | No | The minimum value of RCU scaling of the instance. | Valid values: 0.5 to 8. Note The value of this property must be less than or equal to the value of MaxCapacity. |
| AutoPause | Boolean | No | No | Specifies whether to enable the automatic startup and suspension feature for the serverless instance. | Valid values: true false (default) Note After you enable the feature, the instance is suspended if the instance is not connected within 10 minutes, and the instance is resumed if the instance is connected. |

**DBMappings syntax**

```json
"DBMappings": [
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
```

`]`

**DBMappings properties**

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| DBDescription | String | No | No | The description of the database. | The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, underscores ( ), and _ hyphens (-). |
| CharacterSetName | String | Yes | No | The character set. | Valid values: Valid values when Engine is set to MySQL or MariaDB: utf8 gbk latin1 utf8mb4 Valid values when Engine is set to SQLServer: Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ Valid values when Engine is set to PostgreSQL: KOI8U UTF8 WIN866 WIN874 WIN1250 WIN1251 WIN1252 WIN1253 WIN1254 WIN1255 WIN1256 WIN1257 WIN1258 |

|   |   |   |   |   | EUC CN _ EUC KR _ EUC TW _ EUC JP _ EUC JIS 2004 _ _ KOI8R MULE INTERNAL _ LATIN1 LATIN2 LATIN3 LATIN4 LATIN5 LATIN6 LATIN7 LATIN8 LATIN9 LATIN10 ISO 8859 5 _ _ ISO 8859 6 _ _ ISO 8859 7 |
|---|---|---|---|---|---|
|   |   |   |   |   | _ _ ISO 8859 8 _ _ SQL ASCII _ |
| DBName | String | Yes | No | The database name. | The name must be globally unique. It can be up to 64 characters in length, and can contain lowercase letters, digits, and underscores ( ). It must start _ with a lowercase letter. |

**Return values**

Fn::GetAtt InnerPort: the private port of the instance. OrderId: the order ID. PublicConnectionString: the public endpoint of the instance. InnerIPAddress: the private IP address of the instance. DBInstanceId: the instance ID. PublicIPAddress: the public IP address of the instance. PublicPort: the public port of the instance. InnerConnectionString: the private endpoint of the instance.

**Examples**

YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AllocatePublicConnection:
  AllowedValues:
  - 'True'
'tre'
```

```
  - 'true'
  - 'False'
  - 'false'
  Description: If true, allocate public connection automate.
  Type: Boolean
 ArchiveBackupKeepCount:
  Description: "The number of archived backups that can be retained. Default value:\
   \ 1. Valid values: \nThe value of this parameter ranges from 1 to 31 when the\
   \ ArchiveBackupKeepPolicy \n parameter is set to ByMonth. \nThe value of this\
   \ parameter ranges from 1 to 7 when the ArchiveBackupKeepPolicy \n parameter\
   \ is set to ByWeek. \nNote You do not need to specify this parameter when the\
   \ ArchiveBackupKeepPolicy \nparameter is set to KeepAll."
  MaxValue: 31
  MinValue: 1
  Type: Number
 ArchiveBackupKeepPolicy:
  AllowedValues:
  - ByMonth
  - ByWeek
  - KeepAll
  Description: "The period for which to retain archived backups. The number of archived\
   \ backups that can \n be retained within the specified period is determined\
   \ by the ArchiveBackupKeepCount parameter. \n Default value: 0. Valid values:\
   \ \nByMonth \n ByWeek \n KeepAll"
  Type: String
 ArchiveBackupRetentionPeriod:
  Description: "The number of days for which to retain archived backups. \n The\
   \ default value 0 specifies not to enable the backup archiving function. Valid\
   \ values: 30 to 1095."
  MaxValue: 1095
  MinValue: 30
  Type: Number
 AutoPay:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: true
  Description: Automatic Payment. Default is true.
  Type: Boolean
 AutoRenew:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: false
  Description: Auto renew the prepay instance. If the period type is by year, it
   will renew by year, else it will renew by month.
  Type: Boolean
 BackUpCategory:
  AllowedValues:
  - Flash
  - Standard
  Description: "Specifies whether to enable the second-level backup function. This\
   \ function allows a backup \nto be completed within seconds. Valid values: \n\
   Flash: specifies to enable the second-level backup function. \n Standard: specifies\
   \ to disable the second-level backup function."
  Type: String
 BackupPolicyMode:
  AllowedValues:
  - DataBackupPolicy
```

```
  - LogBackupPolicy
  Description: "Backup type, \nDataBackupPolicy: data backup \nLogBackupPolicy:\
   \ log backup"
  Type: String
 BackupRetentionPeriod:
  Default: 7
  Description: 'The retention period of the data backup. Value range: 7 to 730.
   The default value is the original value. Note When the BackupPolicyMode parameter
   is set to LogBackupPolicy, this parameter is required.'
  Type: Number
 Category:
  AllowedValues:
  - Basic
  - HighAvailability
  - AlwaysOn
  - Finance
  Description: 'The edition of the instance. Valid values:
   Basic: specifies to use the Basic Edition.
   HighAvailability: specifies to use the High-availability Edition.
   AlwaysOn: specifies to use the Cluster Edition.
   Finance: specifies to use the Enterprise Edition.'
  Type: String
 CommodityCode:
  AllowedValues:
  - rds
  - bards
  - rords
  Default: rds
  Description: The CommodityCode of the order.
  Type: String
 CompressType:
  Description: "The format used to compress backups. Valid values: \n 1: The zlib\
   \ tool is used to compress backups into .tar.gz files. \n 4: The QuickLZ tool\
   \ is used to compress backups into .xb.gz files. \nThis compression format is\
   \ supported only when the instance runs MySQL 5.6 or 5.7. \nIt can be used to\
   \ restore individual databases and tables. \n 8: The QuickLZ tool is used to\
   \ compress backups into .xb.gz files. \n This compression format is supported\
   \ only when the instance runs MySQL 8.0. \nIt cannot be used to restore individual\
   \ databases or tables."
  Type: Number
 ConnectionMode:
  Description: 'Connection Mode for database instance,support ''Standard'' and ''Safe''
   mode. Default is RDS system assigns. '
  Type: String
 ConnectionStringPrefix:
  AllowedPattern: '[a-zA-Z0-9-]{8,64}'
  Description: "The prefix of the endpoint. \nOnly the prefix of the CurrentConnectionString\
   \ parameter value can be modified.\nThe prefix must be 8 to 64 characters in\
   \ length and can contain letters, digits, and hyphens (-). "
  Type: String
 ConnectionStringType:
  AllowedValues:
  - Inner
  - Public
  Default: Inner
  Description: 'The endpoint type of the instance, allow values: Inner, Public'
  Type: String
 CouponCode:
```

```
  Description: The coupon code of the order.
  Type: String
 DBInstanceClass:
  Description: Database instance type. Refer the RDS database instance type reference,
   such as 'rds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc
  Type: String
 DBInstanceDescription:
  Description: Description of created database instance.
  Type: String
 DBInstanceNetType:
  AllowedValues:
  - Internet
  - Intranet
  Default: Intranet
  Description: Database instance net type, default is Intranet.Internet for public
   access, Intranet for private access.
  Type: String
 DBInstanceStorage:
  Description: Database instance storage size. mysql is [5,1000]. sql server 2008r2
   is [10,1000], sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and
   PPAS is [5,2000]. Increased every 5 GB, Unit in GB
  Type: Number
 DBInstanceStorageType:
  Description: 'The storage type of the instance. Valid values:
   local_ssd: specifies to use local SSDs. This is the recommended storage type.
   cloud_ssd: specifies to use standard SSDs.
   cloud_essd: specifies to use enhanced SSDs.'
  Type: String
 DBIsIgnoreCase:
  Description: 'Specifies whether table names are case-sensitive. Valid values:
   1: Table names are not case-sensitive. This is the default value.
   0: Table names are case-sensitive.'
  Type: Number
 DBMappings:
  Description: Database mappings to attach to db instance.
  Type: Json
 DBParamGroupId:
  Description: The ID of the parameter template used by the instance.
  Type: String
 DBTimeZone:
  Description: 'The UTC time zone of the instance. Valid values: -12:00 to +12:00.
   The time zone must be an integer value such as +08:00. Values such as +08:30
   are not allowed.'
  Type: String
 DedicatedHostGroupId:
  Description: The ID of the host group to which the instance belongs if you create
   an instance in a host group.
  Type: String
 EnableBackupLog:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Description: "Specifies whether to enable the log backup function. Valid values:\
   \ \nTrue: specifies to enable the log backup function. \nFalse: specifies to\
   \ disable the log backup function. \nNote You must specify this parameter when\
   \ the BackupPolicyMode parameter is set to LogBackupPolicy."
```

```
\te acupo cyodepaaete ssetto ogacupo cy.
  Type: Boolean
 EncryptionKey:
  Description: The ID of the encryption key that is used to encrypt data on SSDs
   in the region. You can view the encryption key ID in the Key Management Service
   (KMS) console. You can also create an encryption key.
  Type: String
 Engine:
  AllowedValues:
  - MySQL
  - SQLServer
  - PostgreSQL
  - PPAS
  - MariaDB
  Description: Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS/MariaDB
   now.
  Type: String
 EngineVersion:
  Description: 'Database instance version of the relative engine type.Support MySQL:
   5.5/5.6/5.7/8.0;
   SQLServer:
2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/2017_std_ha/2017_ent;
   PostgreSQL: 9.4/10.0/11.0/12.0;
   PPAS: 9.3/10.0;
   MariaDB: 10.3.'
  Type: String
 HighSpaceUsageProtection:
  AllowedValues:
  - Enable
  - Disable
  Description: "Specifies whether to forcibly delete log backup files when the space\
   \ usage of the \n instance exceeds 80% or the remaining space is less than 5\
   \ GB. Valid values: \n Enable and Disable. You can retain the default value.\
   \ Note You must specify \n this parameter when the BackupPolicyMode parameter\
   \ is set to LogBackupPolicy."
  Type: String
 LocalLogRetentionHours:
  Description: "The number of hours for which to retain log backup files on the\
   \ instance. \nValid values: 0 to 168. The value 0 specifies not to retain log\
   \ backup files on the instance. \nYou can retain the default value. Note You\
   \ must specify this parameter when the BackupPolicyMode \nparameter is set to\
   \ LogBackupPolicy."
  MaxValue: 168
  MinValue: 0
  Type: Number
 LocalLogRetentionSpace:
  Description: "The maximum percentage of space that is allowed to store log backup\
   \ files on the instance. \n If the space usage for log backup files exceeds\
   \ this percentage, the system deletes earlier \n log backup files until the\
   \ space usage falls below this percentage. Valid values:0 to 50. \n You can\
   \ retain the default value. Note You must specify this parameter when the \n\
   \ BackupPolicyMode parameter is set to LogBackupPolicy."
  MaxValue: 50
  MinValue: 0
  Type: Number
 LogBackupFrequency:
  Description: "The frequency at which to back up logs. Valid values: \nThe value\
   \ LogInterval specifies to back up logs every 30 minutes. \n The default value\
   \ of this parameter is the same as the data backup frequency. \nNote The value\
```

```
   \ LogInterval is supported only when the instance runs SQL Server."
  Type: String
 LogBackupLocalRetentionNumber:
  Description: "The number of log backup files that can be retained on the instance.\
   \ \nDefault value: 60. Valid values: 6 to 100."
  MaxValue: 100
  MinValue: 6
  Type: Number
 LogBackupRetentionPeriod:
  Description: "The number of days for which to retain log backup files. Valid values:\
   \ 7 to 730. The log backup \n retention period cannot be longer than the data\
   \ backup retention period.Note If you enable the log \n backup function, you\
   \ can specify the log backup retention period. This applies only when the \n\
   \ instance runs MySQL, PostgreSQL, or PPAS."
  MaxValue: 730
  MinValue: 7
  Type: Number
 MaintainTime:
  Description: The period during which the maintenance performs. The format is HH:mmZ-HH:mmZ.
  Type: String
 MasterUserPassword:
  Description: 'The master password for the database instance. '
  MaxLength: 32
  MinLength: 8
  Type: String
 MasterUserType:
  AllowedValues:
  - Normal
  - Super
  - Sysadmin
  Default: Normal
  Description: "Privilege type of account.\n Normal: Common privilege. \n Super:\
   \ High privilege. \nSysadmin: Super privileges (SA) (only supported by SQL Server)\n\
   The default value is Normal."
  Type: String
 MasterUsername:
  Description: 'The master user name for the database instance. '
  Type: String
 MultiAZ:
  AllowedValues:
  - 'True'
  - 'true'
  - 'False'
  - 'false'
  Default: false
  Description: 'Specifies if the database instance is a multiple Availability Zone
   deployment. '
  Type: Boolean
 Period:
  Default: 1
  Description: Prepaid time period. While choose by pay by month, it could be from
   1 to 9. While choose pay by year, it could be from 1 to 3.
  MaxValue: 9
  MinValue: 1
  Type: Number
 PeriodType:
  AllowedValues:
  - Month
  - Year
  Default: Month
  Description: Charge period for created instances.
  Type: String
Port:
```

```
 Port:
  Description: The port of the database service.
  MaxValue: 65535
  MinValue: 1
  Type: Number
 PreferredBackupPeriod:
  Description: The backup period. Separate multiple values with commas (,). The
   default value is the original value. Valid values:Monday Tuesday Wednesday Thursday
   Friday Saturday Sunday Note When the BackupPolicyMode parameter is set to DataBackupPolicy,
   this parameter is required.
  Type: CommaDelimitedList
 PreferredBackupTime:
  Description: 'The time when the backup task is performed. Format: yyyy-MM-ddZ-HH:mm:ssZ.Note
   When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter
   is required.'
  Type: String
 PrivateIpAddress:
  Description: The private ip for created instance.
  Type: String
 Quantity:
  Default: 1
  Description: The number of instance to be created, default is 1, max number is
  MaxValue: 99
  MinValue: 1
  Type: Number
 ReleasedKeepPolicy:
  AllowedValues:
  - Lastest
  - All
  Description: "The policy used to retain archived backups if the instance is released.\
   \ Default value: None. \n Valid values: \nLastest: Only the last archived backup\
   \ is retained. \n All: All of the archived backups are retained."
  Type: String
 ResourceGroupId:
  Description: Resource group id.
  Type: String
 RoleARN:
  Description: The Alibaba Cloud Resource Name (ARN) provided to the service account
   of the instance by your Alibaba Cloud account to connect to KMS. You can copy
   the ARN from the RAM console.
  Type: String
 SQLCollectorStatus:
  AllowedValues:
  - Enable
  - Disabled
  Description: "Specifies whether to enable or disable the SQL Explorer (SQL audit)\
   \ feature. \nValid values:Enable | Disabled."
  Type: String
 SSLSetting:
  AllowedValues:
  - Disabled
  - EnabledForPublicConnection
  - EnabledForInnerConnection
  Default: Disabled
  Description: 'Secure Sockets Layer (SSL) link setting of the instance. Valid values:
   Disabled: Disable SSL
   EnabledForPublicConnection: Public connection address will be protected by the
   SSL certificate. It requires AllocatePublicConnection is true.
   EnabledForInnerConnection: Private connection address will be protected by the
```

```
   SSL certificate.
   Default value is Disabled.'
  Type: String
 SecurityGroupId:
  Description: "The ID of the ECS security groups. \nEach RDS instance can be associated\
   \ with up to three ECS security groups. \nYou must separate them with commas\
   \ (,). \nTo delete an ECS Security group, leave this parameter empty. \n"
  Type: String
 SlaveZoneIds:
  Description: List of slave zone ids can specify slave zone ids when creating the
   high-availability or enterprise edition instance. Meanwhile, VSwitchId needs
   to pass in the corresponding vswitch id to the slave zone by order. For example,
   ZoneId = "zone-a" and SlaveZoneIds = ["zone-c", "zone-b"], then the VSwitchId
   must be "vsw-zone-a,vsw-zone-c,vsw-zone-b". Of course, you can also choose automatic
   allocation, for example, ZoneId = "zone-a" and SlaveZoneIds = ["Auto", "Auto"],
   then the VSwitchId must be "vsw-zone-a,Auto,Auto". The list contains up to 2
   slave zone ids, separated by commas.
  MaxLength: 2
  Type: Json
 Tags:
  Description: 'The tags of an instance.
   You should input the information of the tag with the format of the Key-Value,
   such as {"key1":"value1","key2":"value2", ... "key5":"value5"}.
   At most 5 tags can be specified.
   Key
   It can be up to 64 characters in length.
   Cannot begin with aliyun.
   Cannot begin with http:// or https://.
   Cannot be a null string.
   Value
   It can be up to 128 characters in length.
   Cannot begin with aliyun.
   Cannot begin with http:// or https://.
   Can be a null string.'
  Type: Json
 TargetDedicatedHostIdForLog:
  Description: The ID of the host to which the instance belongs if you create a
   log instance in a host group.
  Type: String
 TargetDedicatedHostIdForMaster:
  Description: The ID of the host to which the instance belongs if you create a
   primary instance in a host group.
  Type: String
 TargetDedicatedHostIdForSlave:
  Description: The ID of the host to which the instance belongs if you create a
   secondary instance in a host group.
  Type: String
 VSwitchId:
  Description: The vSwitch id of created instance. For VPC network, the property
isreqired
```

```
   is required.
  Type: String
 VpcId:
  Description: The VPC id of created database instance. For VPC network, the property
   is required.
  Type: String
 ZoneId:
  Description: selected zone to create database instance. You cannot set the ZoneId
   parameter if the MultiAZ parameter is set to true.
  Type: String
Resources:
 PrepayDBInstance:
  Properties:
   AllocatePublicConnection:
    Ref: AllocatePublicConnection
   ArchiveBackupKeepCount:
    Ref: ArchiveBackupKeepCount
   ArchiveBackupKeepPolicy:
    Ref: ArchiveBackupKeepPolicy
   ArchiveBackupRetentionPeriod:
    Ref: ArchiveBackupRetentionPeriod
   AutoPay:
    Ref: AutoPay
   AutoRenew:
    Ref: AutoRenew
   BackUpCategory:
    Ref: BackUpCategory
   BackupPolicyMode:
    Ref: BackupPolicyMode
   BackupRetentionPeriod:
    Ref: BackupRetentionPeriod
   Category:
    Ref: Category
   CommodityCode:
    Ref: CommodityCode
   CompressType:
    Ref: CompressType
   ConnectionMode:
    Ref: ConnectionMode
   ConnectionStringPrefix:
    Ref: ConnectionStringPrefix
   ConnectionStringType:
    Ref: ConnectionStringType
   CouponCode:
    Ref: CouponCode
   DBInstanceClass:
    Ref: DBInstanceClass
   DBInstanceDescription:
    Ref: DBInstanceDescription
   DBInstanceNetType:
    Ref: DBInstanceNetType
   DBInstanceStorage:
    Ref: DBInstanceStorage
   DBInstanceStorageType:
    Ref: DBInstanceStorageType
   DBIsIgnoreCase:
    Ref: DBIsIgnoreCase
   DBMappings:
    Ref: DBMappings
   DBParamGroupId:
    Ref: DBParamGroupId
   DBTimeZone:
    Ref: DBTimeZone
```

```
   DedicatedHostGroupId:
    Ref: DedicatedHostGroupId
   EnableBackupLog:
    Ref: EnableBackupLog
   EncryptionKey:
    Ref: EncryptionKey
   Engine:
    Ref: Engine
   EngineVersion:
    Ref: EngineVersion
   HighSpaceUsageProtection:
    Ref: HighSpaceUsageProtection
   LocalLogRetentionHours:
    Ref: LocalLogRetentionHours
   LocalLogRetentionSpace:
    Ref: LocalLogRetentionSpace
   LogBackupFrequency:
    Ref: LogBackupFrequency
   LogBackupLocalRetentionNumber:
    Ref: LogBackupLocalRetentionNumber
   LogBackupRetentionPeriod:
    Ref: LogBackupRetentionPeriod
   MaintainTime:
    Ref: MaintainTime
   MasterUserPassword:
    Ref: MasterUserPassword
   MasterUserType:
    Ref: MasterUserType
   MasterUsername:
    Ref: MasterUsername
   MultiAZ:
    Ref: MultiAZ
   Period:
    Ref: Period
   PeriodType:
    Ref: PeriodType
   Port:
    Ref: Port
   PreferredBackupPeriod:
    Ref: PreferredBackupPeriod
   PreferredBackupTime:
    Ref: PreferredBackupTime
   PrivateIpAddress:
    Ref: PrivateIpAddress
   Quantity:
    Ref: Quantity
   ReleasedKeepPolicy:
    Ref: ReleasedKeepPolicy
   ResourceGroupId:
    Ref: ResourceGroupId
   RoleARN:
    Ref: RoleARN
   SQLCollectorStatus:
    Ref: SQLCollectorStatus
   SSLSetting:
    Ref: SSLSetting
   SecurityGroupId:
    Ref: SecurityGroupId
   SlaveZoneIds:
    Ref: SlaveZoneIds
   Tags:
    Ref: Tags
```

```
   TargetDedicatedHostIdForLog:
    Ref: TargetDedicatedHostIdForLog
   TargetDedicatedHostIdForMaster:
    Ref: TargetDedicatedHostIdForMaster
   TargetDedicatedHostIdForSlave:
    Ref: TargetDedicatedHostIdForSlave
   VSwitchId:
    Ref: VSwitchId
   VpcId:
    Ref: VpcId
   ZoneId:
    Ref: ZoneId
  Type: ALIYUN::RDS::PrepayDBInstance
Outputs:
 DBInstanceId:
  Description: The instance id of created database instance.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - DBInstanceId
 InnerConnectionString:
  Description: DB instance connection url by Intranet.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - InnerConnectionString
 InnerIPAddress:
  Description: IP Address for created DB instance of Intranet.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - InnerIPAddress
 InnerPort:
  Description: Intranet port of created DB instance.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - InnerPort
 OrderId:
  Description: The order id list of created instance.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - OrderId
 PublicConnectionString:
  Description: DB instance connection url by Internet.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - PublicConnectionString
 PublicIPAddress:
  Description: IP Address for created DB instance of Internet.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - PublicIPAddress
 PublicPort:
  Description: Internet port of created DB instance.
  Value:
   Fn::GetAtt:
   - PrepayDBInstance
   - PublicPort
```

### Redis

#### ALIYUN::REDIS::Instance

ALIYUN::REDIS::Instance is used to create a Tair (Redis OSS-compatible) instance.

**Syntax**

```json
  "Type": "ALIYUN::REDIS::Instance",
  "Properties": {
    "VpcId": String,
    "EvictionPolicy": String,
    "BackupPolicy": Map,
    "ZoneId": String,
    "InstanceClass": String,
    "InstanceMaintainTime": Map,
    "Tags": List,
    "VpcPasswordFree": Boolean,
    "VSwitchId": String,
    "SecurityGroupId": String,
    "EngineVersion": String,
    "SSLEnabled": String,
    "Password": String,
    "InstanceName": String,
    "DeletionForce": Boolean,
    "Connections": Map,
    "ChargeType": String,
    "Period": Integer,
    "AutoRenewDuration": Integer,
    "ProductType": String
    "SecondaryZoneId": String,
    "ResourceGroupId": String,
    "PeriodUnit": String,
    "TairConfig": Map,
    "ShardCount": Integer,
    "NodeType": String,
    "DeletionProtection": Boolean
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| EngineVersio n | String | No | No | The version of the database engine. | Valid values: 2.8 Note This version is unavailable. Select another one. 4.0 5.0 |

| InstanceClass | String | No | Yes | The instance specifications . | For more information, see Instance specifications overview. |
|---|---|---|---|---|---|
| InstanceMaint ainTime | Map | No | Yes | The maintenance window of the instance. | None. |
| Tags | List | No | Yes | The tags of the instance. | You can add up to 20 tags to an instance. For more information, see Tags properties. |
| VpcPassword Free | Boolean | No | No | Specifies whether to enable the password- free access feature for the instance in the virtual private cloud (VPC). | Valid values: true false (default) |
| VpcId | String | No | No | The VPC ID. | None. |
| EvictionPolicy | String | No | No | The data eviction policy. | Valid values: noeviction: The system does not evict keys, but returns an error for write operations. allkeys-lru: The system evicts least recently used (LRU) keys. volatile-lru: The system evicts LRU keys from keys that have time to live (TTL) configured. allkeys-random: The system evicts keys at random. volatile-random: The system evicts keys at random from keys that have TTL configured. volatile-ttl: The system evicts keys with the shortest TTL from keys that have TTL configured. |
| ZoneId | String | No | No | The zone ID of the instance. | You must specify this property when the instance is created in a VPC. If you want to create the instance in multiple zones, call the DescribeZones operation to query the IDs of supported zones. |

| VSwitchId | String | No | No | The ID of the vSwitch that resides in the VPC. | None. |
|---|---|---|---|---|---|
| SecurityGrou pId | String | No | Yes | The ID of the security group. | You can specify up to 10 IDs. Separate multiple IDs with commas (,). |
| Password | String | No | Yes | The password. | The password must be 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. |
| SSLEnabled | String | No | Yes | The status of Secure Sockets Layer (SSL) encryption. | Valid values: Disable: SSL encryption is disabled. Enable: SSL encryption is enabled. Update: The SSL certificate is updated. |
| InstanceNam e | String | No | Yes | The instance name. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). The name must start with a letter. |
| DeletionForce | Boolean | No | Yes | Specifies whether to delete the instance when the instance is moved to the recycle bin. | Valid values: true false (default) |
| Connections | Map | No | Yes | The endpoints of the instance. | For more information, see Connections properties. |
| BackupPolicy | Map | No | Yes | The backup policy. | For more information, see BackupPolicy properties. |
| ChargeType | String | No | No | The billing method of the instance. | Valid values: PostPaid (default): pay-as- you-go PrePaid: subscription |
| Period | Integer | No | No | The billing cycle of the instance. | Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, and 60. Unit: month. |

| AutoRenewD uration | Integer | No | Yes | The auto- renewal duration of the instance. | Valid values: 1 to 12. Unit: month. When an instance is about to expire, the system automatically renews the instance based on the value of this property. Note This property takes effect when ChargeType is set to PrePaid. |
|---|---|---|---|---|---|
| ProductType | String | No | No | The instance edition. | Valid values: Local: a Community Edition instance that supports local disks or a Tair performance- enhanced instance that supports local disks Tair rdb: a Tair performance- _ enhanced instance that supports cloud disks Tair scm: a Tair persistent _ memory-optimized instance Tair essd: a Tair storage- _ optimized instance OnECS: a Community Edition instance that supports cloud disks Note We recommend that you specify ProductType to accelerate parameter queries. |
| SecondaryZo neId | String | No | Yes | The ID of the secondary zone. | You can call the DescribeZones operation to query the ID of the secondary zone. Note If you specify this property, the master node and replica node of the instance can be deployed in different zones, and disaster recovery is implemented across zones. The instance can withstand failures in data centers. |
| ResourceGro upId | String | No | Yes | The ID of the resource group. | None. |

| PeriodUnit | String | No | No | The unit of the subscription duration. | Valid values: Year Month |
|---|---|---|---|---|---|
| TairConfig | Map | No | No | The Tair configuration s. | For more information, see TairConfig properties. |
| ShardCount | Integer | No | No | The number of shards. | This property is available only for cluster instances that use cloud disks. You can use this property to specify a custom number of data shards. |
| NodeType | String | No | No | The node type. | Valid values: MASTER SLAVE: high _ availability (master-replica) STAND ALONE: standalone _ double: master-replica single: standalone Note If you want to create a cloud-native instance, set this property to MASTER SLAVE or _ STAND ALONE. If you _ want to create a classic instance, set this property to double or single. |
| DeletionProte ction | Boolean | No | Yes | Specifies whether to enable the deletion protection feature. | Valid values: true false |

**BackupPolicy syntax**

```json
"BackupPolicy": {
  "PreferredBackupPeriod": "String",
  "PreferredBackupTime": "String",
  "EnableBackupLog": "Integer"
```

**BackupPolicy properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| PreferredBac kupPeriod | String | Yes | Yes | The day of a week on which the system backs up data. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
|---|---|---|---|---|---|
| PreferredBac kupTime | String | Yes | Yes | The time at which the system backs up data. | Specify the time in the ISO 8601 standard in the HH:mmZ-HH:mmZ format. |
| EnableBacku pLog | Integer | No | Yes | Specifies whether to enable incremental backup. | Valid values: 1: enables incremental backup. 0 (default): disables incremental backup. |

**InstanceMaintainTime syntax**

```json
"InstanceMaintainTime": {
  "MaintainStartTime": "String",
  "MaintainEndTime": "String"
```

**InstanceMaintainTime properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MaintainStart Time | String | No | No | The start time of the maintenance window. | Specify the time in the ISO 8601 standard in the HH:mmZ format. The time must be in UTC. For example, if you want the maintenance window to start at 01:00:00 (UTC+8), set this property to 17:00Z . |

| MaintainEndT ime | String | No | No | The end time of the maintenance window. | Specify the time in the ISO 8601 standard in the HH:mmZ format. The time must be in UTC. For example, if you want the maintenance window to end at 02:00:00 (UTC+8), set this property to 18:00Z . Note The end time must be one hour later than the start time. For example, if you set MaintainStartTime to 17:00Z , set MaintainEndTime to 18:00Z . |
|---|---|---|---|---|---|

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | A tag key must be unique within an Alibaba Cloud account in a region. |
| Value | String | No | No | The tag value. | None. |

**Connections syntax**

```json
"Connections": {
  "VpcPrivateConnection": "Map",
  "ClassicInnerConnection": "Map",
  "DirectConnection": "Map",
  "PublicConnection": "Map"
```

**Connections properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VpcPrivateCo nnection | Map | No | Yes | The VPC endpoint. | For more information, see VpcPrivateConnection properties. |

| ClassicInnerC onnection | Map | No | Yes | The classic network endpoint. | For more information, see ClassicInnerConnection properties. |
|---|---|---|---|---|---|
| DirectConnec tion | Map | No | Yes | The private endpoint in direct connection mode. If your instance is a cluster instance, you can apply for a private endpoint in direct connection mode based on your business requirements . | For more information, see DirectConnection properties. |
| PublicConnec tion | Map | No | Yes | The public endpoint. | For more information, see PublicConnection properties. |

**VpcPrivateConnection syntax**

```json
"VpcPrivateConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
```

**VpcPrivateConnection properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | Yes | Yes | The port number used by the instance to provide services. | Valid values: 1024 to 65535. |
| ConnectionSt ring | String | Yes | Yes | The prefix of the VPC endpoint. | The prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. The prefix must start with a lowercase letter. |

**PublicConnection syntax**

```json
"PublicConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
```

**PublicConnection properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | Yes | Yes | The port number used by the instance to provide services. | Valid values: 1024 to 65535. |
| ConnectionSt ring | String | Yes | Yes | The prefix of the public endpoint. | The prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. The prefix must start with a lowercase letter. |

**DirectConnection syntax**

```json
"DirectConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
```

**DirectConnection properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ConnectionPo rt | Integer | Yes | Yes | The port number used by the instance to provide services. | Valid values: 1024 to 65535. |
| ConnectionSt ring | String | Yes | Yes | The prefix of the private endpoint in direct connection mode. | The prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. The prefix must start with a lowercase letter. |

**ClassicInnerConnection syntax**

```json
"ClassicInnerConnection": {
  "ConnectionPort": Integer,
  "ConnectionString": String
```

**ClassicInnerConnection properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| ConnectionPo rt | Integer | Yes | Yes | The port number used by the instance to provide services. | Valid values: 1024 to 65535. |
|---|---|---|---|---|---|
| ConnectionSt ring | String | Yes | Yes | The prefix of the classic network endpoint. | The prefix must be 8 to 64 characters in length and can contain lowercase letters and digits. The prefix must start with a lowercase letter. |

**TairConfig syntax**

```json
"TairConfig": {
  "Storage": "Integer",
  "StorageType": "String",
  "ShardCount": "Integer"
```

**TairConfig properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Storage | Integer | No | No | The storage capacity of the cloud disk. | The storage capacity varies based on the instance specification. For more information, see ESSD/SSD- based instances. |
| StorageType | String | No | No | The storage type of the instance. | Valid values: essd pl0 _ essd pl1 _ essd pl2 _ essd pl3 _ |
| ShardCount | Integer | No | No | The number of data shards on the instance. | Valid values: 1 (default): The instance uses the standard architecture that contains only a single data shard. 2 to 32: The instance uses the cluster architecture that contains a specified number of data shards. |

**Return values**

Fn::GetAtt InstanceId: the instance ID. OrderId: the order ID of the instance. ConnectionDomain: the private endpoint that is used to access the instance. Port: the port number used by the instance to provide services. InstanceName: the instance name. InstanceClass: the instance specifications. VpcId: the VPC ID of the instance. Capacity: the storage capacity of the instance. InstanceType: the type of the database engine. ChargeType: the billing method of the instance. PackageType: the plan type of the instance. Connections: the maximum number of connections that are supported by the instance. ArchitectureType: the architecture type of the instance. NodeType: the node type of the instance. HasRenewChangeOrder: indicates whether the instance has pending renewal or resource scale-out orders within the current Alibaba Cloud account. ResourceGroupId: the ID of the resource group. QPS: the queries per second (QPS) of the instance. The value is the expected maximum QPS. ZoneId: the zone ID of the instance. Bandwidth: the bandwidth of the instance. Unit: Mbit/s. EngineVersion: the version of the database engine. NetworkType: the network type of the instance. VSwitchId: the vSwitch ID of the instance. PrivateIp: the private IP address of the instance. PublicConnectionString: the prefix of the public endpoint that is used to access the instance. VpcPrivateConnectionPort: the port number that is used to access the instance by using the VPC endpoint. ClassicInnerConnectionString: the prefix of the classic network endpoint that is used to access the instance. VpcPrivateConnectionString: the prefix of the VPC endpoint that is used to access the instance. PublicConnectionPort: the port number that is used to access the instance by using the public endpoint. DirectConnectionString: the prefix of the private endpoint that is used to access the instance in direct connection mode. DirectConnectionPort: the port number that is used to access the instance by using the private endpoint in direct connection mode. ClassicInnerConnectionPort: the port number that is used to access the instance by using the classic network endpoint.

**Examples**

YAML JSON

```
ROSTemplateFormatVersion: '2015-09-01' Description: {} Parameters:
  VpcId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VPC::VPCId
  ZoneId:
    Type: String
    Description:
      en: Before you create an instance, confirm that the Availability Zone supports the
specifications of Redis resources.
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Label:
      en: Zone ID
  VSwitchId:
    Type: String
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: ${VpcId}
      ZoneId: ${ZoneId}
Resources:
  RedisInstance:
    Type: ALIYUN::REDIS::Instance
    Properties:
      VpcId:
        Ref: VpcId
      VSwitchId:
        Ref: VSwitchId
      InstanceClass: redis.master.small.default
      EvictionPolicy: noeviction
      ZoneId:
        Ref: ZoneId
      InstanceName: DefaultRedis
      Password: Admin@123!
Outputs:
  InstanceId:
    Value:
      Fn::GetAtt:
        - RedisInstance
        - InstanceId
```

For more examples, visit Instance.yml. In the examples, the following resource types are used: ALIYUN::REDIS::Instance, ALIYUN::REDIS::Whitelist, and ALIYUN::REDIS::Account.

### ROS

#### ALIYUN::ROS::WaitCondition

ALIYUN::ROS::WaitCondition is used to create an instance to process UserData messages.

**Syntax**

```json
  "Type": "ALIYUN::ROS::WaitCondition",
  "Properties": {
    "Count": Number,
    "Handle": String,
    "Timeout": Number,
    "ShowProgressEvent": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Handle | String | Yes | No | The instance created by calling ALIYUN::ROS: :WaitConditio nHandle. | None |
| Timeout | Number | Yes | No | The timeout period for receiving UserData messages. | Valid values: 1 to 43200. Unit: seconds. |
| Count | Number | No | Yes | The total number of received UserData messages. | None |
| ShowProgress Event | String | No | No | Specifies whether to display progress events for receiving UserData messages. | Valid values: EnabledIfCreateStack: Progress events are displayed if you create stacks. Disabled: Progress events are not displayed. |

**Response parameters**

Fn::GetAtt Data: a JSON string that contains the signal data sent to the handle after the latest stack creation or update. JoinedErrorData: a string that contains data associated with wait condition error signals sent to the handle. ErrorData: a JSON string that contains the error signal data sent to the handle after the latest stack creation or update.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ShowProgressEvent": {
      "Type": "String",
      "Description": "Whether to generate progress changed event. Default to Disabled.",
      "AllowedValues": [
        "EnabledIfCreateStack",
        "Disabled"
```

`]` `},`

```json
    "Timeout": {
      "Type": "Number",
      "Description": "The number of seconds to wait for the correct number of signals to arrive.",
      "MinValue": 1,
      "MaxValue": 43200
```

`},`

```json
    "Count": {
      "Type": "Number",
      "Description": "The number of success signals that must be received before the stack creation p
rocess continues.",
      "Default": 1
```

`},`

```json
    "Handle": {
      "Type": "String",
      "Description": "A reference to the wait condition handle used to signal this wait condition."
```

`},`

```json
  "Resources": {
    "WaitCondition": {
      "Type": "ALIYUN::ROS::WaitCondition",
      "Properties": {
        "ShowProgressEvent": {
          "Ref": "ShowProgressEvent"
```

`},`

```json
        "Timeout": {
          "Ref": "Timeout"
```

`},`

```json
        "Count": {
          "Ref": "Count"
```

`},`

```json
        "Handle": {
          "Ref": "Handle"
```

`},`

```json
  "Outputs": {
    "LastErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error
signals sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "LastErrorData"
```

`]` `},`

```json
    "JoinedLastErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to the
handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedLastErrorData"
```

`]` `},`

```json
    "LastData": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
```

```
          "WaitCondition",
          "LastData"
```

`]` `},`

```json
    "JoinedErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to the
handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedErrorData"
```

`]` `},`

```json
    "Data": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "Data"
```

`]` `},`

```json
    "ErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error
signals sent to the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "ErrorData"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Count:
    Default: 1
    Description: The number of success signals that must be received before the stack
      creation process continues.
    Type: Number
  Handle:
    Description: A reference to the wait condition handle used to signal this wait
      condition.
    Type: String
  ShowProgressEvent:
    AllowedValues:
    - EnabledIfCreateStack
    - Disabled
    Description: Whether to generate progress changed event. Default to Disabled.
    Type: String
  Timeout:
    Description: The number of seconds to wait for the correct number of signals to
      arrive.
    MaxValue: 43200
    MinValue: 1
```

```
    Type: Number
Resources:
  WaitCondition:
    Properties:
      Count:
        Ref: Count
      Handle:
        Ref: Handle
      ShowProgressEvent:
        Ref: ShowProgressEvent
      Timeout:
        Ref: Timeout
    Type: ALIYUN::ROS::WaitCondition
Outputs:
  Data:
    Description: JSON serialized dict containing data associated with wait condition
      signals sent to the handle.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - Data
  ErrorData:
    Description: JSON serialized dict containing data associated with wait condition
      error signals sent to the handle.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - ErrorData
  JoinedErrorData:
    Description: String containing data associated with wait condition error signals
      sent to the handle.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - JoinedErrorData
  JoinedLastErrorData:
    Description: String containing data associated with wait condition error signals
      sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - JoinedLastErrorData
  LastData:
    Description: JSON serialized dict containing data associated with wait condition
      signals sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - LastData
  LastErrorData:
    Description: JSON serialized dict containing data associated with wait condition
      error signals sent to the handle backup by update last time.
    Value:
      Fn::GetAtt:
      - WaitCondition
      - LastErrorData
```

#### ALIYUN::ROS::WaitConditionHandle

ALIYUN::ROS::WaitConditionHandle is used to create an instance that sends and receives messages when user data is being executed.

**Syntax**

```json
  "Type": "ALIYUN::ROS::WaitConditionHandle",
  "Properties": {
    "Count": Integer,
    "Mode": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Count | Integer | No | Yes | The total number of messages to be received. | The default value is -1, which specifies that the property does not take effect. This property takes effect when the following conditions are met: The value of Mode is Full. The value of Count is greater than or equal to 0. No signal ID is specified. Signal IDs must be integers that start from 1. The signal ID increments by 1 for each subsequent signal. For example, if the ID of the first signal is 1, the ID of the second signal is 2. If Count takes effect, the signals whose IDs are greater than the Count value are deleted before the update begins. |
| Mode | String | No | Yes | The mode of the instance. | Default value: Full. Valid values: Increment: All signals are deleted before they are updated. Full: No signals are deleted if you do not configure Count. |

**Response parameters**

Fn::GetAtt CurlCli: a cURL command that is generated by the resource. You can use the command to send the user data execution result or status to Resource Orchestration Service (ROS). WindowsCurlCli: provides Windows with cURL CLI command prefixes and sends a message that indicates whether the execution is successful or failed. Windows does not support the cURL command. Therefore, you must manually install curl.exe and add it to PATH. You can add --data-binary "{\"status\": \" SUCCESS \"} to indicate that the execution is successful, and add --data-binary "{\"status\": \" FAILURE \"} to indicate that the execution failed. PowerShellCurlCli: provides PowerShell with cURL CLI command prefixes and sends a message that indicates whether the execution is successful or failed. cmdlet is introduced in PowerShell 3.0. Therefore, you must make sure that your version of PowerShell satisfies the constraints. You can use the

| ber. You can add | -Body '{"status": " |   |
|---|---|---|
| -Body '{"status": "FAILURE "} |   | to |

$PSVersionTable.PSVersion command to query the version number. You can add `-Body '{"status": "` `SUCCESS "}` to indicate that the execution is successful, and add `-Body '{"status": "FAILURE "}` to indicate that the execution failed. Headers: the HTTP POST request headers used to send a message that indicates whether the execution is successful or failed. URL: the HTTP POST request URL used to send a message that indicates whether the execution is successful or failed.

**Examples**

`JSON` format

```json
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "Mode": {
   "Type": "String",
   "Description": "If set to Increment, all old signals will be deleted before update. In this mode,
WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n\nIf set to Full, no old sign al will be deleted unless Count is set. In this mode, WaitCondition.Count should reference a full val ue, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Coun t.\n\nDefault to Full.",
   "AllowedValues": [
    "Increment",
    "Full"
```

`],`

```json
   "Default": "Full"
```

`},`

```json
  "Count": {
   "Type": "Number",
   "Description": "There are 3 preconditions that make Count taking effect:\n1.Mode is set to Full.\n
2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer start ed from 1. For example, the id of the first signal is 1, the id of the second signal is 2, and so on. \n\nIf Count takes effect, signals with id > Count will be deleted before update.\nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
   "Default": -1
```

`},`

```json
 "Resources": {
  "WaitConditionHandle": {
   "Type": "ALIYUN::ROS::WaitConditionHandle",
   "Properties": {
    "Mode": {
     "Ref": "Mode"
```

`},`

```json
    "Count": {
     "Ref": "Count"
```

`},`

```json
 "Outputs": {
  "CurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix, which can be used for sig
nalling handle completion or failure. You can signal success by adding --data-binary '{\"status\": \" SUCCESS\"}' , or signal failure by adding --data-binary '{\"status\": \"FAILURE\"}'",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
```

```
     "CurlCli"
```

`]` `},`

```json
  "WindowsCurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix for Windows, which can be
used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH first. You can signal success by adding --data-binary \"{\\\"s tatus\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" ",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "WindowsCurlCli"
```

`]` `},`

```json
  "Headers": {
   "Description": "HTTP POST Headers used for signalling handle completion or failure.",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "Headers"
```

`]` `},`

```json
  "URL": {
   "Description": "HTTP POST URL used for signalling handle completion or failure.",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "URL"
```

`]` `},`

```json
  "PowerShellCurlCli": {
   "Description": "Convenience attribute, provides curl CLI command prefix for PowerShell, which can
be used for signalling handle completion or failure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by adding -Body '{\"status\": \"SUCCESS\"}' , or s ignal failure by adding -Body '{\"status\": \"FAILURE\"}' ",
   "Value": {
    "Fn::GetAtt": [
     "WaitConditionHandle",
     "PowerShellCurlCli"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 Mode:
  Type: String
  Description: >-
   If set to Increment, all old signals will be deleted before update. In
   this mode, WaitCondition.Count should reference an incremental value
   instead of a full value, such as
   ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.
```

```
   If set to Full, no old signal will be deleted unless Count is set. In this
   mode, WaitCondition.Count should reference a full value, such as the same
   value with InstanceGroup.MaxAmount. It is recommended to use this mode
   with Count.
   Default to Full.
  AllowedValues:
   - Increment
   - Full
  Default: Full
 Count:
  Type: Number
  Description: >-
   There are 3 preconditions that make Count taking effect:
   1.Mode is set to Full.
   2.Count >= 0.
   3.The id of signal is not specified. If so, it will be a self-increasing
   integer started from 1. For example, the id of the first signal is 1, the
   id of the second signal is 2, and so on.
   If Count takes effect, signals with id > Count will be deleted before
   update.
   The default value is -1, which means no effect.
   It is recommended to quote the same value with WaitCondition.Count.
  Default: -1
Resources:
 WaitConditionHandle:
  Type: 'ALIYUN::ROS::WaitConditionHandle'
  Properties:
   Mode:
    Ref: Mode
   Count:
    Ref: Count
Outputs:
 CurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix, which can be used
   for signalling handle completion or failure. You can signal success by
   adding --data-binary '{"status": "SUCCESS"}' , or signal failure by adding
   --data-binary '{"status": "FAILURE"}'
  Value:
   'Fn::GetAtt':
    - WaitConditionHandle
    - CurlCli
 WindowsCurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix for Windows, which
   can be used for signalling handle completion or failure. As Windows does
   not support curl command, you need to install curl.exe and add it to PATH
   first. You can signal success by adding --data-binary "{\"status\":
   \"SUCCESS\"}" , or signal failure by adding --data-binary "{\"status\":
   \"FAILURE\"}"
  Value:
```

```
   'Fn::GetAtt':
    - WaitConditionHandle
    - WindowsCurlCli
 Headers:
  Description: HTTP POST Headers used for signalling handle completion or failure.
  Value:
   'Fn::GetAtt':
    - WaitConditionHandle
    - Headers
 URL:
  Description: HTTP POST URL used for signalling handle completion or failure.
  Value:
   'Fn::GetAtt':
    - WaitConditionHandle
    - URL
 PowerShellCurlCli:
  Description: >-
   Convenience attribute, provides curl CLI command prefix for PowerShell,
   which can be used for signalling handle completion or failure. As this
   cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShell
   satisfies the constraint. (Show the version via
   $PSVersionTable.PSVersion.) You can signal success by adding -Body
   '{"status": "SUCCESS"}' , or signal failure by adding -Body '{"status":
   "FAILURE"}'
  Value:
   'Fn::GetAtt':
    - WaitConditionHandle
    - PowerShellCurlCli
```

For more examples, visit SLS.json and SLS.yml.

#### ALIYUN::ROS::Stack

ALIYUN::ROS::Stack creates a nested stack. You can nest stacks up to five levels deep. A nested stack can contain other nested stacks, forming a stack hierarchy. The root stack is the top-level parent to which all nested stacks belong, and its template is called the top-level template. Use ALIYUN::ROS::Stack to nest a stack as a resource in a top-level template. In a nested stack template, you can pass an output of one stack as an input to another. To retrieve a nested stack output, use Fn::GetAtt with the nested stack name and output name in the Outputs.NestedStackOutputName format. Use nested stacks.

**Syntax**

```json
  "Type": "ALIYUN::ROS::Stack",
  "Properties": {
    "TemplateURL": String,
    "TemplateBody": String,
    "TemplateId": String,
    "TemplateVersion": String,
    "TimeoutMins": Number,
    "Parameters": Map,
    "ResourceGroupId": String,
    "Tags": List
```

**Properties**

| Property | Type | Required | Editable | Descripti on | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| Template URL | String |   |   | The URL | The template body file can be up to 524,288 bytes. The URL can be up to 1,024 bytes. The URL must point to a template on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn- hangzhou . If the region ID of the OSS bucket is not specified, the stack's region ID is used. Specify one of TemplateURL , TemplateBody , or TemplateId . If all three are specified, TemplateBody takes precedence. |   |   |
|   |   | No | Yes | of the template | hangzhou |   |   |
|   |   |   |   | body file. |   |   |   |
| Template Body | Map | No | Yes | The template body content for template delivery. | The content is raw data. Functions in the template content apply only to child templates. Specify one of TemplateURL , TemplateBody , or TemplateId . If all three are specified, TemplateBody takes precedence. |   |   |
| TemplateI d | String | No | Yes | The template ID. | Specify one of TemplateURL , TemplateBody , or TemplateId . If all three are specified, TemplateBody takes precedence. |   |   |
| Template Version | String | No | Yes | The name of the template version. | None. |   |   |
| TimeoutMi ns | Number | No | Yes | The timeout period for creating or updating the parent stack. | Unit: minutes. Default value: 60. |   |   |

|   | TemplateURL |   |
|---|---|---|
| TemplateBody |   |   |

|   | TemplateURL |   |
|---|---|---|
| TemplateBody |   |   |

|   | TemplateURL |   |
|---|---|---|
| TemplateBody |   |   |

| Parameter s | Map | No | Yes | Key-value pairs representi ng the parameter s passed to ROS when the nested stack is created. | Each key-value pair corresponds to a parameter defined in the nested stack template. Required when the nested stack has input parameters. |
|---|---|---|---|---|---|
| Resource GroupId | String | No | No | The ID of the resource group. | None. |
| Tags | List | No | Yes | The tags. | You can specify up to 20 tags. Tags properties. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key can be up to 128 characters. It cannot start with aliyun or acs: and cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | The tag value can be up to 128 characters. It cannot start with aliyun or acs: and cannot contain http:// or https:// . |

**Return values**

Fn::GetAtt Use the following code to obtain the output of a nested stack:

```
  "Fn::GetAtt": [
    "<nested_stack>",
    "Outputs.<nested_stack_output_name>"
```

`]` If you use `Ref` to reference a nested stack resource, the Alibaba Cloud Resource Name (ARN) of the nested stack is returned. Example: `arn:acs:ros::cn-hangzhou:12345****:stacks/test-nested-stack-Demo-`

```
jzkyq7mn****/e71c1e04-1a57-46fc-b9a4-cf7ce0d3**** .
```

**Examples**

The following YAML and JSON examples create a child stack containing a virtual private cloud (VPC), a vSwitch, and a security group. The child stack template is stored at oss://ros/template/vpc.txt. `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: One VPC, vSwitch, security group. Parameters:
  ZoneId:
    Type: String
    Description: The available zone
  SecurityGroupName:
    Type: String
    Description: The security group name
    Default: my-sg-name
  VpcName:
    Type: String
    Description: The VPC name
    MinLength: 2
    MaxLength: 128
    ConstraintDescription: '[2, 128] English or Chinese letters'
    Default: my-vpc-name
  VpcCidrBlock:
    Type: String
    AllowedValues:
      - 192.168.0.0/16
      - 172.16.0.0/12
      - 10.0.0.0/8
    Default: 10.0.0.0/8
  VSwitchCidrBlock:
    Type: String
    Description: The vSwitch subnet which must be within VPC
    Default: 10.0.10.0/24
  UpdateVersion:
    Type: Number
    Default: 0
Resources:
  Vpc:
    Type: ALIYUN::ECS::VPC
    Properties:
      CidrBlock:
        Ref: VpcCidrBlock
      VpcName:
        Ref: VpcName
  VSwitch:
    Type: ALIYUN::ECS::VSwitch
    Properties:
      CidrBlock:
        Ref: VSwitchCidrBlock
      ZoneId:
        Ref: ZoneId
      VpcId:
        Fn::GetAtt:
          - Vpc
          - VpcId
  SecurityGroup:
    Type: ALIYUN::ECS::SecurityGroup
    Properties:
      SecurityGroupName:
        Ref: SecurityGroupName
      VpcId:
Ref:Vpc
```

```
        Ref: Vpc
  WaitConditionHandle:
    Type: ALIYUN::ROS::WaitConditionHandle
    Properties:
      UpdateVersion:
        Ref: UpdateVersion
Outputs:
  SecurityGroupId:
    Value:
      Fn::GetAtt:
        - SecurityGroup
        - SecurityGroupId
  VpcId:
    Value:
      Fn::GetAtt:
        - Vpc
        - VpcId
  VSwitchId:
    Value:
      Fn::GetAtt:
        - VSwitch
        - VSwitchId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One VPC, vSwitch, security group.",
  "Parameters": {
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone"
```

`},`

```json
    "SecurityGroupName": {
      "Type": "String",
      "Description": "The security group name",
      "Default": "my-sg-name"
```

`},`

```json
    "VpcName": {
      "Type": "String",
      "Description": "The VPC name",
      "MinLength": 2,
      "MaxLength": 128,
      "ConstraintDescription": "[2, 128] English or Chinese letters",
      "Default": "my-vpc-name"
```

`},`

```json
    "VpcCidrBlock": {
      "Type": "String",
      "AllowedValues": [
        "192.168.0.0/16",
        "172.16.0.0/12",
        "10.0.0.0/8"
```

`],`

```json
      "Default": "10.0.0.0/8"
```

`},`

```json
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The vSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
```

`},`

```json
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
```

`},`

```json
  "Resources": {
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": {
          "Ref": "VpcCidrBlock"
```

`},`

```json
        "VpcName": {
          "Ref": "VpcName"
```

`},`

```json
    "VSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "CidrBlock": {
          "Ref": "VSwitchCidrBlock"
```

`},`

```json
        "ZoneId": {
          "Ref": "ZoneId"
```

`},`

```json
        "VpcId": {
          "Fn::GetAtt": [
            "Vpc",
            "VpcId"
```

`]` `},`

```json
    "SecurityGroup": {
      "Type": "ALIYUN::ECS::SecurityGroup",
      "Properties": {
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
```

`},`

```json
        "VpcId": {
          "Ref": "Vpc"
```

`},`

```json
    "WaitConditionHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle",
      "Properties": {
        "UpdateVersion": {
          "Ref": "UpdateVersion"
```

`},`

```json
  "Outputs": {
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupId"
```

`]` `},`

```json
    "VpcId": {
      "Value": {
"Fn::GetAtt":[
```

```
::Gettt:[
          "Vpc",
          "VpcId"
```

`]` `},`

```json
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "VSwitch",
          "VSwitchId"
```

`]` The following YAML and JSON examples create a parent stack: `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: One ECS instance. Parameters:
  ImageId:
    Default: centos_7
    Type: String
    Description: Image Id, represents the image resource to startup the ECS instance
  InstanceType:
    Type: String
    Description: The ECS instance type,
    Default: ecs.xn4.small
  ZoneId:
    Type: String
    Description: 'The available zone '
  InstanceChargeType:
    Type: String
    AllowedValues:
      - PrePaid
      - PostPaid
    Default: PostPaid
    Description: The instance charge type
  SecurityGroupName:
    Type: String
    Description: The security group name
    Default: my-sg-name
  NetworkInterfaceName:
    Type: String
    Description: The Network interface name
    Default: my-eni-name
  VpcName:
    Type: String
    Description: The VPC name
    MinLength: 2
    MaxLength: 128
    ConstraintDescription: '[2, 128] English or Chinese letters'
    Default: my-vpc-name
  IoOptimized:
    AllowedValues:
      - none
      - optimized
    Description: IO optimized, optimized is for the IO optimized instance type
    Type: String
    Default: optimized
```

```
  SystemDiskCategory:
    AllowedValues:
      - cloud
      - cloud_efficiency
      - cloud_ssd
    Description: 'System disk category: average cloud disk(cloud), efficient cloud
disk(cloud_efficiency) or SSD cloud disk(cloud_ssd)'
    Type: String
    Default: cloud_ssd
  VpcCidrBlock:
    Type: String
    AllowedValues:
      - 192.168.0.0/16
      - 172.16.0.0/12
      - 10.0.0.0/8
    Default: 10.0.0.0/8
  VSwitchCidrBlock:
    Type: String
    Description: The VSwitch subnet which must be within VPC
    Default: 10.0.10.0/24
  UpdateVersion:
    Type: Number
    Default: 0
Resources:
  NetworkStack:
    Type: ALIYUN::ROS::Stack
    Properties:
      TemplateURL: oss://ros/template/vpc.txt
      TimeoutMins: 5
      Parameters:
        ZoneId:
          Ref: ZoneId
        SecurityGroupName:
          Ref: SecurityGroupName
        VpcName:
          Ref: VpcName
        VpcCidrBlock:
          Ref: VpcCidrBlock
        VSwitchCidrBlock:
          Ref: VSwitchCidrBlock
        UpdateVersion:
          Ref: UpdateVersion
  WebServer:
    Type: ALIYUN::ECS::Instance
    Properties:
      ImageId:
        Ref: ImageId
      InstanceType:
        Ref: InstanceType
      InstanceChargeType:
        Ref: InstanceChargeType
      SecurityGroupId:
        Fn::GetAtt:
          - NetworkStack
          - Outputs.SecurityGroupId
      VpcId:
        Fn::GetAtt:
          - NetworkStack
          - Outputs.VpcId
      VSwitchId:
        Fn::GetAtt:
          - NetworkStack
OtptsVSitchId
```

```
          - Outputs.VSwitchId
      IoOptimized:
        Ref: IoOptimized
      ZoneId:
        Ref: ZoneId
      SystemDisk_Category:
        Ref: SystemDiskCategory
      DiskMappings:
        - Category: cloud_ssd
          Size: 20
Outputs:
  InstanceId:
    Value:
      Fn::GetAtt:
        - WebServer
        - InstanceId
  PublicIp:
    Value:
      Fn::GetAtt:
        - WebServer
        - PublicIp
  SecurityGroupId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.SecurityGroupId
  VpcId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.VpcId
  VSwitchId:
    Value:
      Fn::GetAtt:
        - NetworkStack
        - Outputs.VSwitchId
  NetworkStackArn:
    Value:
      Ref: NetworkStack
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One ECS instance.",
  "Parameters": {
    "ImageId": {
      "Default": "centos_7",
      "Type": "String",
      "Description": "Image Id, represents the image resource to startup the ECS instance"
```

`},`

```json
    "InstanceType": {
      "Type": "String",
      "Description": "The ECS instance type,",
      "Default": "ecs.xn4.small"
```

`},`

```json
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone "
```

`},`

```json
    "InstanceChargeType": {
      "Type": "String",
      "AllowedValues": [
```

```
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid",
      "Description": "The instance charge type"
```

`},`

```json
    "SecurityGroupName": {
      "Type": "String",
      "Description": "The security group name",
      "Default": "my-sg-name"
```

`},`

```json
    "NetworkInterfaceName": {
      "Type": "String",
      "Description": "The Network interface name",
      "Default": "my-eni-name"
```

`},`

```json
    "VpcName": {
      "Type": "String",
      "Description": "The VPC name",
      "MinLength": 2,
      "MaxLength": 128,
      "ConstraintDescription": "[2, 128] English or Chinese letters",
      "Default": "my-vpc-name"
```

`},`

```json
    "IoOptimized": {
      "AllowedValues": [
        "none",
        "optimized"
```

`],`

```json
      "Description": "IO optimized, optimized is for the IO optimized instance type",
      "Type": "String",
      "Default": "optimized"
```

`},`

```json
    "SystemDiskCategory": {
      "AllowedValues": [
        "cloud",
        "cloud_efficiency",
        "cloud_ssd"
```

`],`

```json
      "Description": "System disk category: average cloud disk(cloud), efficient cloud
disk(cloud_efficiency) or SSD cloud disk(cloud_ssd)",
      "Type": "String",
      "Default": "cloud_ssd"
```

`},`

```json
    "VpcCidrBlock": {
      "Type": "String",
      "AllowedValues": [
        "192.168.0.0/16",
        "172.16.0.0/12",
        "10.0.0.0/8"
```

`],`

```json
      "Default": "10.0.0.0/8"
```

`},`

```json
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The VSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
```

`},`

```json
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
```

`},`

```json
  "Resources": {
    "NetworkStack": {
      "Type": "ALIYUN::ROS::Stack",
      "Properties": {
        "TemplateURL": "oss://ros/template/vpc.txt",
        "TimeoutMins": 5,
        "Parameters": {
          "ZoneId": {
            "Ref": "ZoneId"
```

`},`

```json
          "SecurityGroupName": {
            "Ref": "SecurityGroupName"
```

`},`

```json
          "VpcName": {
            "Ref": "VpcName"
```

`},`

```json
          "VpcCidrBlock": {
            "Ref": "VpcCidrBlock"
```

`},`

```json
          "VSwitchCidrBlock": {
            "Ref": "VSwitchCidrBlock"
```

`},`

```json
          "UpdateVersion": {
            "Ref": "UpdateVersion"
```

`},`

```json
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Ref": "ImageId"
```

`},`

```json
        "InstanceType": {
          "Ref": "InstanceType"
```

`},`

```json
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
```

`},`

```json
        "SecurityGroupId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.SecurityGroupId"
```

`]` `},`

```json
        "VpcId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VpcId"
```

`]` `},`

```json
        "VSwitchId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VSwitchId"
```

`]` `},`

```json
        "IoOptimized": {
          "Ref": "IoOptimized"
```

`},`

```json
        "ZoneId": {
```

```json
          "Ref": "ZoneId"
```

`},`

```json
        "SystemDisk_Category": {
          "Ref": "SystemDiskCategory"
```

`},`

```json
        "DiskMappings": [
            "Category": "cloud_ssd",
            "Size": 20
```

`]` `},`

```json
  "Outputs": {
    "InstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceId"
```

`]` `},`

```json
    "PublicIp": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "PublicIp"
```

`]` `},`

```json
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.SecurityGroupId"
```

`]` `},`

```json
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.VpcId"
```

`]` `},`

```json
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.VSwitchId"
```

`]` `},`

```json
    "NetworkStackArn": {
      "Value": {
        "Ref": "NetworkStack"
```

### SLB

#### ALIYUN::SLB::AccessControl

ALIYUN::SLB::AccessControl is used to create an access control list (ACL).

**Syntax**

```json
  "Type": "ALIYUN::SLB::AccessControl",
  "Properties": {
    "AddressIPVersion": String,
    "AclName": String,
    "AclEntrys": List,
    "Tags": List,
    "ResourceGroupId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AddressIPVer sion | String | No | No | The Internet Protocol version. | Valid values: ipv4 ipv6 |
| AclName | String | Yes | Yes | The name of the ACL. | None. |
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the ACL belongs. | None. |
| AclEntrys | List | No | No | The list of ACL entries. | The list can contain a maximum of 50 ACL entries. For more information, see AclEntrys properties. |
| Tags | List | No | Yes | The tags. | You can add up to 20 tags. For more information, see Tags property. |

**AclEntrys syntax**

```json
"AclEntrys": [
    "comment": String,
    "entry": String
```

`]`

**AclEntrys properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| comment | String | No | No | The description of the ACL entry. | None. |
|---|---|---|---|---|---|
| entry | String | Yes | No | The IP address or CIDR block. | None. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags property**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The value of the tag. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

**Return values**

Fn::GetAtt AclId: the ID of the ACL.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters: {} Resources:
  AccessControl:
    Type: ALIYUN::SLB::AccessControl
    Properties:
      AddressIPVersion: ipv4
      AclName:
        Ref: TestAcl
      AclEntrys:
        - entry: 0.0.0.0
Outputs:
  AclId:
    Description: The ID of the access control list.
    Value:
      Fn::GetAtt:
        - AccessControl
        - AclId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
```

`},`

```json
  "Resources": {
    "AccessControl": {
      "Type": "ALIYUN::SLB::AccessControl",
      "Properties": {
        "AddressIPVersion": "ipv4",
        "AclName": {
          "Ref": "TestAcl"
```

`},`

```json
        "AclEntrys": [
            "entry": "0.0.0.0"
```

`]` `},`

```json
  "Outputs": {
    "AclId": {
      "Description": "The ID of the access control list.",
      "Value": {
        "Fn::GetAtt": [
          "AccessControl",
          "AclId"
```

`]` To view more examples, visit AccessControl.json and AccessControl.yml.

#### ALIYUN::SLB::BackendServerAttachment

ALIYUN::SLB::BackendServerAttachment is used to attach backend servers to an SLB instance.

**Syntax**

```json
  "Type": "ALIYUN::SLB::BackendServerAttachment",
  "Properties": {
    "LoadBalancerId": String,
    "BackendServers": List,
    "BackendServerList": List,
    "BackendServerWeightList": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerId | String | Yes | No | The unique ID of the SLB instance. | None. |

| BackendServerLi st | List | No | Yes | The list of backend servers to be attached. | The LoadBalancerId parameter is used together with the BackendServer WeightList parameter. Separate ECS instance IDs with commas (,). This parameter is ignored when the BackendServers parameter is specified. |
|---|---|---|---|---|---|
| BackendServer WeightList | List | No | Yes | The weights of all ECS instances specified by the BackendServerLi st parameter in order. | If this parameter is not specified, the weight of each ECS instance specified by the BackendServerLi st parameter is 100. When the number of items specified by BackendServer WeightList is less than that specified by BackendServerLi st, the remaining ECS instances in the backend server list are assigned the last weight value in the backend server weight list. |
| BackendServers | List | No | Yes | The list of backend servers to be attached. | Only ECS instances that are in the running state can be attached to the SLB instance as backend servers. For more information, see BackendServers properties. |

**BackendServers syntax**

```json
"BackendServers": [
    "ServerId" : String,
    "Weight" : Integer,
    "Type": String,
    "ServerIp": String,
    "Description": String
```

`]`

**BackendServers properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the ECS instance. | Only ECS instances that are in the running state can be attached to the SLB instance as backend servers. A maximum of 20 backend servers can be attached each time. You can specify elastic network interfaces (ENIs) as the backend servers for only guaranteed- performance SLB instances. |
| Weight | Integer | Yes | Yes | The weight of the ECS instance in the SLB instance. | Valid values: 0 to 100. Default value: 100. |
| ServerIp | String | No | No | The IP address of the backend server. | None. |
| Type | String | No | No | The type of the backend server. | Default value: ecs. Valid values: ecs: ECS instance eni: ENI eci: Elastic Container Instance (ECI) |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

**Response parameters**

Fn::GetAtt BackendServers: the backend servers attached to the SLB instance. LoadBalancerId: the ID of the SLB instance.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  BackendServerList:
    Type: Json
    Description: >-
      The comma delimited instance id list. If the property "BackendServers" is
      setting, this property will be ignored.
  LoadBalancerId:
    Type: String
    Description: The id of load balancer.
  BackendServerWeightList:
    Type: CommaDelimitedList
    Description: >-
      The comma delimited weight list. If no value specified will use 100. If
      the length is small than "BackendServerList", it will copy the last one to
      fill the array. If the property "BackendServers" is setting, this property
      will be ignored.
  BackendServers:
    Type: Json
    Description: 'The list of ECS instance, which will attached to load balancer.'
Resources:
  BackendServer:
    Type: 'ALIYUN::SLB::BackendServerAttachment'
    Properties:
      BackendServerList:
        Ref: BackendServerList
      LoadBalancerId:
        Ref: LoadBalancerId
      BackendServerWeightList:
        Ref: BackendServerWeightList
      BackendServers:
        Ref: BackendServers
Outputs:
  LoadBalancerId:
    Description: The id of load balancer.
    Value:
      'Fn::GetAtt':
        - BackendServer
        - LoadBalancerId
  BackendServers:
    Description: The collection of attached backend server.
    Value:
      'Fn::GetAtt':
        - BackendServer
        - BackendServers
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "BackendServerList": {
      "Type": "Json",
```

\ \

```json
      "Description": "The comma delimited instance id list. If the property \"BackendServers\" is s
etting, this property will be ignored."
```

`},`

```json
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The id of load balancer."
```

`},`

```json
    "BackendServerWeightList": {
      "Type": "CommaDelimitedList",
      "Description": "The comma delimited weight list. If no value specified will use 100. If the l
ength is small than \"BackendServerList\", it will copy the last one to fill the array. If the prop erty \"BackendServers\" is setting, this property will be ignored."
```

`},`

```json
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of ECS instance, which will attached to load balancer."
```

`},`

```json
  "Resources": {
    "BackendServer": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Ref": "BackendServerList"
```

`},`

```json
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
```

`},`

```json
        "BackendServerWeightList": {
          "Ref": "BackendServerWeightList"
```

`},`

```json
        "BackendServers": {
          "Ref": "BackendServers"
```

`},`

```json
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The id of load balancer.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "LoadBalancerId"
```

`]` `},`

```json
    "BackendServers": {
      "Description": "The collection of attached backend server.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "BackendServers"
```

`]`

**7.8.3.**

#### ALIYUN::SLB::BackendServerToVServerGroupAddition

ALIYUN::SLB::BackendServerToVServerGroupAddition is used to add backend servers to an existing vServer group.

**Syntax**

```json
  "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
  "Properties": {
    "BackendServers": List,
    "VServerGroupId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGroup Id | String | Yes | No | The ID of the vServer group. | None |
| BackendServ ers | List | Yes | Yes | The list of backend servers. | For more information, see BackendServers properties. |

**BackendServers syntax**

```json
"BackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
```

`]`

**BackendServers properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | None |
| Port | Integer | Yes | Yes | The port that is used by the backend server. | Valid values: 1 to 65535. |
| Weight | Integer | No | Yes | The weight of the backend server. | Valid values: 0 to 100. |

| Type | String | No | Yes | The type of the backend server. | Default value: ecs. Valid values: ecs: Elastic Compute Service (ECS) instances eni: elastic network interfaces (ENIs) Note You can specify ENIs as backend servers only for high- performance SLB instances. |
|---|---|---|---|---|---|
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| ServerIp | String | No | Yes | The IP address of the backend server. | The IP addresses of ECS instances or ENIs are supported. |

**Response parameters**

Fn::GetAtt VServerGroupId: the ID of the vServer group.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VServerGroupId": {
      "Type": "String",
      "Description": "The ID of virtual server group."
```

`},`

```json
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of a combination of ECS Instance-Port-Weight.Same ecs instance with di
fferent port is allowed, but same ecs instance with same port isn't."
```

`},`

```json
  "Resources": {
    "BackendServerToVServerGroupAddition": {
      "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
      "Properties": {
        "VServerGroupId": {
          "Ref": "VServerGroupId"
```

`},`

```json
        "BackendServers": {
          "Ref": "BackendServers"
```

`},`

```json
  "Outputs": {
    "VServerGroupId": {
      "Description": "The ID of virtual server group.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServerToVServerGroupAddition",
          "VServerGroupId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VServerGroupId:
    Type: String
    Description: The ID of virtual server group.
  BackendServers:
    Type: Json
    Description: >-
      The list of a combination of ECS Instance-Port-Weight.Same ecs instance
      with different port is allowed, but same ecs instance with same port
      isn't.
Resources:
  BackendServerToVServerGroupAddition:
    Type: 'ALIYUN::SLB::BackendServerToVServerGroupAddition'
    Properties:
      VServerGroupId:
        Ref: VServerGroupId
      BackendServers:
        Ref: BackendServers
Outputs:
  VServerGroupId:
    Description: The ID of virtual server group.
    Value:
      'Fn::GetAtt':
        - BackendServerToVServerGroupAddition
        - VServerGroupId
```

To view more examples, visit Listener.json and Listener.yml. In the examples, the ALIYUN::SLB::Listener, ALIYUN::SLB::LoadBalancerClone, ALIYUN::SLB::Certificate, ALIYUN::SLB::DomainExtension, ALIYUN::SLB::VServerGroup, ALIYUN::SLB::Rule, and ALIYUN::SLB::BackendServerToVServerGroupAddition resource types are involved.

#### ALIYUN::SLB::Certificate

ALIYUN::SLB::Certificate is used to upload a certificate to a Server Load Balancer (SLB) instance. Server certificates and certificate authority (CA) certificates are supported.

**Important**

If you set CertificateType to CA, you can upload only one CA certificate at a time. If you set CertificateType to Server, you can upload only one server certificate and its corresponding private key at a time.

**Syntax**

```json
  "Type": "ALIYUN::SLB::Certificate",
  "Properties": {
    "CertificateName": String,
    "Certificate": String,
    "AliCloudCertificateName": String,
    "PrivateKey": String,
    "ResourceGroupId": String,
    "CertificateType": String,
    "AliCloudCertificateId": String,
    "Tags": List
```

**Properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The resource group ID. | None. |
| CertificateNa me | String | No | Yes | The certificate name. | None. |
| Certificate | String | Yes | No | The certificate to be uploaded. | None. |
| AliCloudCertif icateName | String | No | No | The name of the certificate that is provided by Alibaba Cloud Certificate Management Service. | None. |
| PrivateKey | String | No | No | The private key to be uploaded. | None. |
| AliCloudCertif icateId | String | No | No | The ID of the certificate that is provided by Alibaba Cloud Certificate Management Service. | This property must be specified when you use a certificate provided by Alibaba Cloud Certificate Management Service. |
| CertificateTyp e | String | No | No | The certificate type. | Valid values: Server CA |
| Tags | List | No | Yes | The tags. | You can add up to 20 tags. For more information, see Tags properties. |

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| > Document V | ersion: 202608 | 28 |   |   | 370 |
|---|---|---|---|---|---|

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The key must be 1 to 128 characters in length. It cannot start with aliyun or acs: , and cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | The value must be 0 to 128 characters in length. It cannot start with aliyun or acs: , and cannot contain http:// or https:// . |

**Return values**

Fn::GetAtt CertificateId: the certificate ID. Fingerprint: the certificate fingerprint.

**Examples**

`JSON` format

```json
 "ROSTemplateFormatVersion": "2015-09-01",
 "Parameters": {
  "CertificateType": {
   "Type": "String",
   "Description": "The type of the certificate.",
   "AllowedValues": [
    "Server",
    "CA"
```

`],`

```json
   "Default": "Server"
```

`},`

```json
  "AliCloudCertificateName": {
   "Type": "String",
   "Description": "The name of the Alibaba Cloud certificate."
```

`},`

```json
  "PrivateKey": {
   "Type": "String",
   "Description": "The private key."
```

`},`

```json
  "ResourceGroupId": {
   "Type": "String",
   "Description": "Resource group id."
```

`},`

```json
  "CertificateName": {
   "Type": "String",
   "Description": "The name of the certificate."
```

`},`

```json
  "Tags": {
   "Type": "Json",
   "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Eac
h tag with two properties Key and Value, and Key is required.",
   "MaxLength": 20
```

`},`

```json
  "Certificate": {
```

`"T` `"`

```
"Sti
```

`"`

```json
   "Type": "String",
   "Description": "The content of the certificate public key."
```

`},`

```json
  "AliCloudCertificateId": {
   "Type": "String",
   "Description": "The ID of the Alibaba Cloud certificate."
```

`},`

```json
 "Resources": {
  "SLBCertificate": {
   "Type": "ALIYUN::SLB::Certificate",
   "Properties": {
    "CertificateType": {
     "Ref": "CertificateType"
```

`},`

```json
    "AliCloudCertificateName": {
     "Ref": "AliCloudCertificateName"
```

`},`

```json
    "PrivateKey": {
     "Ref": "PrivateKey"
```

`},`

```json
    "ResourceGroupId": {
     "Ref": "ResourceGroupId"
```

`},`

```json
    "CertificateName": {
     "Ref": "CertificateName"
```

`},`

```json
    "Tags": {
     "Ref": "Tags"
```

`},`

```json
    "Certificate": {
     "Ref": "Certificate"
```

`},`

```json
    "AliCloudCertificateId": {
     "Ref": "AliCloudCertificateId"
```

`},`

```json
 "Outputs": {
  "Fingerprint": {
   "Description": "The fingerprint of the certificate.",
   "Value": {
    "Fn::GetAtt": [
     "SLBCertificate",
     "Fingerprint"
```

`]` `},`

```json
  "CertificateId": {
   "Description": "The ID of the certificate.",
   "Value": {
    "Fn::GetAtt": [
     "SLBCertificate",
     "CertificateId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
 AliCloudCertificateId:
  Description: The ID of the Alibaba Cloud certificate.
  Type: String
 AliCloudCertificateName:
  Description: The name of the Alibaba Cloud certificate.
  Type: String
 Certificate:
  Description: The content of the certificate public key.
  Type: String
 CertificateName:
  Description: The name of the certificate.
  Type: String
 CertificateType:
  AllowedValues:
  - Server
  - CA
  Default: Server
  Description: The type of the certificate.
  Type: String
 PrivateKey:
  Description: The private key.
  Type: String
 ResourceGroupId:
  Description: Resource group id.
  Type: String
 Tags:
  Description: Tags to attach to instance. Max support 20 tags to add during create
   instance. Each tag with two properties Key and Value, and Key is required.
  MaxLength: 20
  Type: Json
Resources:
 SLBCertificate:
  Properties:
   AliCloudCertificateId:
    Ref: AliCloudCertificateId
   AliCloudCertificateName:
    Ref: AliCloudCertificateName
   Certificate:
    Ref: Certificate
   CertificateName:
    Ref: CertificateName
   CertificateType:
    Ref: CertificateType
   PrivateKey:
    Ref: PrivateKey
   ResourceGroupId:
    Ref: ResourceGroupId
   Tags:
    Ref: Tags
  Type: ALIYUN::SLB::Certificate
Outputs:
 CertificateId:
  Description: The ID of the certificate.
  Value:
   Fn::GetAtt:
   - SLBCertificate
   - CertificateId
 Fingerprint:
Description:Thefingerprintofthecertificate
```

```
  Description: The fingerprint of the certificate.
  Value:
   Fn::GetAtt:
   - SLBCertificate
   - Fingerprint
```

For more examples, see the combined examples of creating an SLB listener, cloning an SLB instance, uploading a certificate, creating an additional domain name, creating a vServer group and adding backend servers to an SLB instance, adding forwarding rules to an HTTP or HTTPS listener, and adding backend servers to a vServer group: JSON examples and YAML examples.

#### ALIYUN::SLB::DomainExtension

ALIYUN::SLB::DomainExtension is used to create a domain extension for an SLB instance.

**Statement**

```json
  "Type": "ALIYUN::SLB::DomainExtension",
  "Properties": {
    "Domain": String,
    "ListenerPort": Integer,
    "ServerCertificateId": String,
    "LoadBalancerId": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Domain | String | No | No | The custom domain name. | None |
| ListenerPort | Integer | Yes | No | The frontend port used by the HTTPS listener of the SLB instance. | Valid values: 1 to 65535. |
| ServerCertificate Id | String | No | Yes | The ID of the certificate corresponding to the domain name. | None |
| LoadBalancerId | String | No | No | The ID of the SLB instance. | None |

**Response parameters**

Fn::GetAtt DomainExtensionId: the ID of the created domain extension. ListenerPort: The frontend port used by the SLB instance.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DomainExtension": {
      "Type": "ALIYUN::SLB::DomainExtension",
      "Properties": {
        "Domain": "*.example.com",
        "ListenerPort": "443",
        "ServerCertificateId": "123157908552****_166f8204689_1714763408_70998****",
        "LoadBalancerId": "lb-bp1o94dp5i6earr9g****"
```

`},`

```json
  "Outputs": {
    "DomainExtensionId": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "DomainExtensionId"
```

`]` `},`

```json
    "ListenerPort": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "ListenerPort"
```

`]`

#### ALIYUN::SLB::Listener

ALIYUN::SLB::Listener is used to create a listener for a Server Load Balancer (SLB) instance.

**Syntax**

```json
  "Type": "ALIYUN::SLB::Listener",
  "Properties": {
    "MasterSlaveServerGroupId": String,
    "AclStatus": String,
    "Protocol": String,
    "AclId": String,
    "ServerCertificateId": String,
    "HealthCheck": Map,
    "RequestTimeout": Integer,
    "IdleTimeout": Integer,
    "ListenerPort": Integer,
    "HttpConfig": Map,
    "Bandwidth": Integer,
    "AclType": String,
    "BackendServerPort": Integer,
    "Scheduler": String,
    "LoadBalancerId": String,
    "CACertificateId": String,
    "Persistence": Map,
    "VServerGroupId": String,
    "Description": String,
    "PortRange": List,
    "StartListener": Boolean
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterSlaveS erverGroupId | String | No | No | The ID of the primary/seco ndary server group. | None |
| AclStatus | String | No | Yes | Specifies whether to enable the access control feature. | Valid values: on (default): enables the access control feature. off: disables the access control feature. |
| AclId | String | No | Yes | The ID of the access control list (ACL) to be associated with the listener. | This parameter is required when the AclStatus parameter is set to on. |

| AclType | String | No | Yes | The type of the ACL. | Valid values: white: specifies the ACL as a whitelist. Only requests from the IP addresses or CIDR blocks in the ACL are forwarded. Whitelists are applicable to scenarios in which you want an application to be accessed only from specific IP addresses. Risks may arise if the whitelist is improperly set. After you configure a whitelist, only the IP addresses that are specified in the whitelist can access the SLB listener. If you enable a whitelist but the whitelist does not contain an IP address, the listener does not forward requests. black: specifies the ACL as a blacklist. All requests from the IP addresses or CIDR blocks in the ACL are rejected. Blacklists are applicable to scenarios in which you want to deny access from specific IP addresses to an application. If you enable a blacklist but the blacklist does not contain an IP address, the listener forwards all requests. This parameter is required when the AclStatus parameter is set to on. |
|---|---|---|---|---|---|
| Protocol | String | Yes | No | The protocol over which the listener forwards requests. | Valid values: http https tcp udp |
| ListenerPort | Integer | Yes | No | The frontend port that is used by the SLB instance. | Valid values: 1 to 65535. |
| Bandwidth | Integer | Yes | No | The bandwidth limit of the listener. | Valid values: 1 to 1000 and -1. Unit: Mbit/s. Valid values: For a pay-by-bandwidth Internet-facing SLB instance, you cannot set this parameter to -1. The sum of bandwidth limits that you specify for all listeners of the SLB instance cannot exceed the bandwidth limit of the SLB instance. For a pay-by-data-transfer Internet-facing SLB instance, you can set this parameter to -1, which specifies that the bandwidth is unlimited. |

| BackendServ erPort | Integer | Yes | No | The backend port that is used by the SLB instance. | Valid values: 1 to 65535. |
|---|---|---|---|---|---|
| LoadBalancer Id | String | Yes | No | The ID of the SLB instance. | None |
| HealthCheck | Map | No | No | The health check settings of the listener. | For more information, see HealthCheck properties. |
| Persistence | Map | No | Yes | The persistence properties. | For more information, see Persistence properties. |
| Scheduler | String | No | No | The scheduling algorithm. | Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed to backend servers in sequence. |
| CACertificateI d | String | No | No | The ID of the certificate authority (CA) certificate. | This parameter is valid only when the Protocol parameter is set to https. |
| ServerCertific ateId | String | No | Yes | The ID of the server certificate. | This parameter is required and valid only when the Protocol parameter is set to https. |
| VServerGroup Id | String | No | No | The ID of the server group. | None |
| RequestTime out | Integer | No | No | The timeout period of a request. | Valid values: 1 to 180. Unit: seconds. |
| IdleTimeout | Integer | No | No | The timeout period of an idle connection. | Valid values: 1 to 60. Unit: seconds. |
| HttpConfig | Map | No | No | The HTTP configuration s. | For more information, see HttpConfig properties. |
| Description | String | No | No | The description of the listener. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| PortRange | List | No | No | The range of ports on which the SLB instance listens. | Set StartPort to 1 and EndPort to 65535. For more information, see PortRange properties. |

| StartListener | Boolean | No | No | Specifies whether to start the listener. | Valid values: true (default): starts the listener. false: does not start the listener. |
|---|---|---|---|---|---|

**HealthCheck syntax**

```json
"HealthCheck": {
  "Domain": String,
  "Interval": Integer,
  "URI": String,
  "HttpCode": String,
  "HealthyThreshold": Integer,
  "HealthCheckType": String,
  "Timeout": Integer,
  "UnhealthyThreshold": Integer,
  "Port": Integer,
  "Switch": String
```

**HealthCheck properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Domain | String | No | No | The domain name that is used for health checks. | Valid values: $ ip _ Custom string: A custom string must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), and periods (.). An empty string Note When this parameter is set to $ ip or _ left empty, the SLB instance uses the private IP addresses of backend servers as the domain names for health checks. |
| Interval | Integer | No | No | The interval between two consecutive health checks. | Valid values: 1 to 5. Unit: seconds. |
| URI | String | No | No | The URI that is used for health checks. | The URI must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URI must start with a forward slash (/). |

| HttpCode | String | No | No | The HTTP status code. | Valid values: http 2xx (default) _ http 3xx _ http 4xx _ http 5xx _ Separate multiple HTTP status codes with commas (,). |
|---|---|---|---|---|---|
| HealthyThres hold | Integer | No | No | The threshold that is used to determine whether a backend server is healthy. This value specifies the number of consecutive successful health checks that is required before the health status of a backend server is changed from fail to success. | Valid values: 1 to 10. |
| HealthCheckT ype | String | No | No | The type of health check. | Valid values: tcp http |
| Timeout | Integer | No | No | The timeout period of a health check response. | Valid values: 1 to 50. Unit: seconds. Note This parameter is valid only when the value is greater than or equal to the value of the Interval parameter. Otherwise, the value of this parameter is overwritten by the value of the Interval parameter. |

| UnhealthyThr eshold | Integer | No | No | The threshold that is used to determine whether a backend server is unhealthy. This value specifies the number of consecutive failed health checks that is required before the health status of a backend server is changed from success to fail. | Valid values: 1 to 10. |
|---|---|---|---|---|---|
| Port | Integer | No | No | The port that is used for health checks. | Valid values: 0 to 65535. |
| Switch | String | No | No | Specifies whether to enable health checks. | Valid values: on: enables health checks. off: disables health checks. Note This parameter is valid only when the Protocol parameter is set to http or https. If the Switch parameter is not set, health checks are disabled by default unless health check items are already configured. |

**Persistence syntax**

```json
"Persistence": {
  "PersistenceTimeout": Integer,
  "CookieTimeout": Integer,
  "XForwardedFor": String,
  "XForwardedFor_SLBID": String,
  "XForwardedFor_proto": String,
  "XForwardedFor_SLBIP": String,
  "Cookie": String,
  "StickySession": String,
  "StickySessionType": String,
  "XForwardedFor_ClientSrcPort": String,
  "XForwardedFor_SLBPORT": String
```

**Persistence properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| StickySession | String | No | Yes | Specifies whether to enable session persistence. | Valid values: on: enables session persistence. off: disables session persistence. |
|---|---|---|---|---|---|
| PersistenceTi meout | Integer | No | Yes | The timeout period for session persistence. | Valid values: 0 to 1000. Default value: 0. 0: disables sessions persistence. Unit: seconds. |
| CookieTimeo ut | Integer | No | Yes | The timeout period of a cookie. | Valid values: 1 to 86400. Unit: seconds. Note This parameter is required when the StickySession parameter is set to on and the StickySessionType parameter is set to insert. |
| XForwardedF or | String | No | Yes | Specifies whether to use the X- Forwarded- For header to obtain the real IP address of a client. | Valid values: on: uses the X-Forwarded- For header to obtain the real IP address of a client. off (default): does not use the X-Forwarded-For header to obtain the real IP address of a client. |
| XForwardedF or proto _ | String | No | Yes | Specifies whether to use the X- Forwarded- Proto header to obtain the listener protocol of the SLB instance. | Valid values: on: uses the X-Forwarded- Proto header to obtain the listener protocol of the SLB instance. off (default): does not use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. |
| XForwardedF or SLBID _ | String | No | Yes | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. | Valid values: on: uses the SLB-ID header to obtain the ID of the SLB instance. off (default): does not use the SLB-ID header to obtain the ID of the SLB instance. |
| XForwardedF or SLBIP _ | String | No | Yes | Specifies whether to use the SLB- IP header to obtain the real IP address that is requested by a client. | Valid values: on: uses the SLB-IP header to obtain the real IP address that is requested by a client. off (default): does not use the SLB-IP header to obtain the real IP address that is requested by a client. |

| Cookie | String | No | Yes | The cookie that is configured on the server. | The cookie must be 1 to 200 characters in length, and cannot start with a dollar sign ($). The cookie can contain letters and digits, and cannot contain commas (,), semicolons (;), or spaces. Note This parameter is required when the StickySession parameter is set to on and the StickySessionType parameter is set to server. |
|---|---|---|---|---|---|
| StickySession Type | String | No | Yes | The method that is used to handle a cookie. | Valid values: insert: inserts a cookie. server: rewrites a cookie. Note This parameter is required when the StickySession parameter is set to on. |
| XForwardedF or ClientSrcP _ ort | String | No | Yes | Specifies whether to use the X- Forwarded- Client-srcport header to obtain the port that is used by a client to connect to the SLB instance. | Valid values: on: uses the X-Forwarded- Client-srcport header to obtain the port that is used by a client to connect to the SLB instance. off (default): does not use the X-Forwarded-Client- srcport header to obtain the port that is used by a client to connect to the SLB instance. |
| XForwardedF or SLBPORT _ | String | No | Yes | Specifies whether to use the X- Forwarded- Proto header to obtain the listener protocol of the SLB instance. | Valid values: on: uses the X-Forwarded- Proto header to obtain the listener protocol of the SLB instance. off (default): does not use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. |

**HttpConfig syntax**

```json
"HttpConfig": {
  "ForwardPort": Integer,
  "ListenerForward": String
```

**HttpConfig properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ForwardPort | Integer | No | No | The port that is used to redirect HTTP requests to HTTPS. | Valid values: 1 to 65535. Default value: 443. |

| ListenerForw ard | String | No | No | Specifies whether to enable redirection from HTTP to HTTPS. | Valid values: on: enables redirection. off (default:) disables redirection. |
|---|---|---|---|---|---|

**PortRange syntax**

```json
"PortRange": [
    "StartPort": Integer,
    "EndPort": Integer
```

`]`

**PortRange properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StartPort | Integer | Yes | No | The start of the port range. | Set the value to 1. |
| EndPort | Integer | Yes | No | The end of the port range. | Set the value to 65535. |

**Response parameters**

Fn::GetAtt LoadBalancerId: the unique ID of the SLB instance. ListenerPortsAndProtocol: the ports and protocols that are used by the SLB listener.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LoadBalancerId": {
      "Type": "String",
      "Label": "SLB instance ID",
      "Default": "slb-*****"
```

`},`

```json
  "Resources": {
    "SlbListener": {
      "Type": "ALIYUN::SLB::Listener",
      "Properties": {
        "Persistence": {
          "CookieTimeout": 60,
          "StickySession": "on",
          "PersistenceTimeout": 180,
          "XForwardedFor": "off",
          "StickySessionType": "insert"
```

`},`

```json
        "ListenerPort": 80,
        "Bandwidth": -1,
        "HealthCheck": {
          "HttpCode": "http_2xx,http_3xx,http_4xx,http_5xx",
          "HealthCheckType": "tcp",
          "UnhealthyThreshold": 3,
          "Timeout": 5,
          "HealthyThreshold": 3,
          "Port": 80,
          "URI": "/",
          "Interval": 2
```

`},`

```json
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
```

`},`

```json
        "BackendServerPort": 80,
        "Protocol": "tcp"
```

`},`

```json
  "Outputs": {
```

To view more examples, visit Listener.json and Listener.yml. The examples describe the following resource types: ALIYUN::SLB::Listener, ALIYUN::SLB::LoadBalancerClone, ALIYUN::SLB::Certificate, ALIYUN::SLB::DomainExtension, ALIYUN::SLB::VServerGroup, ALIYUN::SLB::Rule, and ALIYUN::SLB::BackendServerToVServerGroupAddition.

#### ALIYUN::SLB::LoadBalancer

ALIYUN::SLB::LoadBalancer is used to create an SLB instance.

**Statement**

```json
  "Type": "ALIYUN::SLB::LoadBalancer",
  "Properties": {
    "DeletionProtection": Boolean,
    "AddressType": String,
    "Tags": List,
    "InternetChargeType": String,
    "Bandwidth": Integer,
    "SlaveZoneId": String,
    "ResourceGroupId": String,
    "AutoPay": Boolean,
    "VpcId": String,
    "PricingCycle": String,
    "LoadBalancerName": String,
    "Duration": Number,
    "VSwitchId": String,
    "LoadBalancerSpec": String,
    "MasterZoneId": String,
    "PayType": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the RDS instance belongs. | None |
| DeletionProtecti on | Boolean | Erased | Released | Specifies whether to enable deletion protection to prevent the SLB instance from being deleted by mistake. | Valid values: true false |
| VpcId | String | Yes | Released | The ID of the VPC. | None |
| SlaveZoneId | String | Yes | Released | The ID of the secondary zone to which the SLB instance belongs. | None |

| Bandwidth | String | Optional | Released | The peak bandwidth of SLB instances that are connected to the Internet and billed by fixed bandwidth. | For SLB instances that are connected to the Internet and billed by fixed Bandwidth, this parameter is valid only when the Bandwidth parameter of the SLB Listener is specified. For Internet instances whose billing type is to pay by traffic, we recommend that you set the peak Bandwidth through the Listener parameter. In this case, this parameter is ignored. Valid values: 1 to 1000. Unit: Mbps. Default value: 1 VPC-type instances are billed by traffic. |
|---|---|---|---|---|---|
| AddressType | String | Yes | Released | The address type of the SLB instance. | Valid values: internet intranet Default value: internet. |
| VSwitchId | String | Yes | Released | The ID of the vSwitch in the VPC. | None |

| LoadBalancerNa me | String | Yes | Released | The name of the SLB instance to be created. | A custom string. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ If this parameter is not specified, the system assigns a value. |
|---|---|---|---|---|---|
| InternetChargeT ype | String | Yes | Released | The billing method of SLB instances that are connected to the Internet. | Valid values: paybybandwi dth paybytraffic Default value: paybytraffic. |
| MasterZoneId | String | Yes | Released | The ID of the primary zone to which the SLB instance belongs. | None |
| Tags | List | Erased | Released | The tags to be attached to the SLB instance. The tags are listed in JSON format. Each tag consists of a TagKey and a TagValue. | A maximum of five tags can be attached to an SLB instance. |
| LoadBalancerSp ec | String | Yes | Released | The type of the SLB instance. | Valid values: slb.s1.small slb.s2.small slb.s2.mediu m slb.s3.small slb.s3.mediu m slb.s3.large The available types vary by region. |
| AutoPay | Boolean | Erased | Released | Specifies whether to automatically pay for subscription SLB instances that are connected to the Internet. | Valid values: true false Default value: false. Note This parameter is valid only on the China site (aliyun.com ). |

| PayType | String | Yes | Released | The billing method of the SLB instance. | Valid values: PayOnDeman d PrePay |
|---|---|---|---|---|---|
| PricingCycle | String | Yes | Released | The billing cycle of subscription SLB instances that are connected to the Internet. | Valid values: month year Note This parameter is valid only on the China site (aliyun.com ). |
| Duration | Number | Erased | Released | The subscription period of subscription SLB instances that are connected to the Internet. | Valid values: Valid values when the PricingCycle parameter is set to month: 1 to 9. Valid values when the PricingCycle parameter is set to year: 1 to 3. Note This parameter is valid only on the China site (aliyun.com ). |

**Tags syntax**

```json
"Tags": [
    "Value": String ,
    "Key": String
```

`]`

**Tags properties**

| Property | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |

| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |
|---|---|---|---|---|---|

**Response parameters**

**Fn::GetAtt**

LoadBalancerId: the unique ID of the SLB instance. NetworkType: the network type of the SLB instance, which can be vpc or classic. AddressType: the address type of the SLB instance, which can be intranet or internet. IpAddress: the IP address of the SLB instance. OrderId: the ID of the order.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "CreateLoadBalance": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "createdByHeat",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
```

`},`

```json
  "Outputs": {
    "LoadBalanceDetails": {
      "Value": {
        "Fn::GetAtt": ["CreateLoadBalance", "LoadBalancerId"]}
```

#### ALIYUN::SLB::LoadBalancerClone

Clones an SLB instance.

**Syntax**

```json
  "Type": "ALIYUN::SLB::LoadBalancerClone",
  "Properties": {
    "Tags": List,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "LoadBalancerName": String,
    "SourceLoadBalancerId": String,
    "TagsPolicy": String,
    "BackendServersPolicy": String,
    "BackendServers": List,
    "InstanceChargeType": String,
    "LoadBalancerSpec": String
```

**Properties**

| Property name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| ResourceGroupI d | String | No | No | The ID of the resource group. | None |
| VSwitchId | String | No | No | The ID of the vSwitch. | Must belong to the VPC of the source SLB instance. Default: the source instance's vSwitch. |
| SourceLoadBala ncerId | String | Yes | No | The ID of the source SLB instance to clone. | None |
| BackendServers Policy | String | No | No | The backend server cloning policy. | Valid values: clone (default): Clones all backend servers and weights from the source instance. empty: Adds no backend servers. append: Clones backend servers from the source instance and adds new ones. replace: Adds only new backend servers without cloning from the source instance. |

| BackendServers | List | No | Yes | The new backend servers to add. | BackendServers properties. |
|---|---|---|---|---|---|
| LoadBalancerNa me | String | No | No | The name of the SLB instance. | 1 to 80 characters. Supports letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| Tags | List | No | No | The tags of the SLB instance. | Key-value pairs. Maximum: 5. Tags properties. |
| TagsPolicy | String | No | No | The tag policy. | Valid values: clone: Retains the tags of the source instance. empty (default): Does not set any tags. append: Retains the tags of the source instance and adds new tags. replace: Adds only new tags without retaining the source instance's tags. |
| InstanceChargeT ype | String | No | No | The billing method of the instance. | Valid values: PayBySpec (default): pay- by- specification. PayByCLCU: pay-as-you- go. Note Valid only when PayType is set to PayOnDe mand. |

| LoadBalancerSp ec | String | No | No | The specification of the SLB instance. | Valid values: slb.s1.small (default) slb.s2.small slb.s2.mediu m slb.s3.small slb.s3.mediu m slb.s3.large slb.s3.xlarge slb.s3.xxlarge Supported specifications vary by region. FAQ about CLB instances. |
|---|---|---|---|---|---|

**BackendServers syntax**

```json
"BackendServers": [
    "Type": String,
    "ServerId": String,
    "Description": String,
    "ServerIp": String,
    "Weight": Integer
```

`]`

**BackendServers properties**

| Property name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | The backend server must be in the running state. Maximum: 20 per call. Only guaranteed- performance instances support ENI-type backend servers. |
| Weight | Integer | Yes | Yes | The weight of the backend server. | Valid values: 0 to 100. Default value: 100. |
| ServerIp | String | No | No | The IP address of the backend server. | None |

| Type | String | No | No | The type of the backend server. | Valid values: ecs (default): ECS instance. eni: ENI instance. eci: Elastic Container Instance. |
|---|---|---|---|---|---|
| Description | String | No | Yes | The description of the backend server. | 1 to 80 characters. Supports letters, Chinese characters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

**Tags syntax**

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]`

**Tags properties**

| Property name | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | 1 to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |
| Value | String | No | No | The tag value. | 0 to 128 characters. Cannot start with aliyun or acs: . Cannot contain http:// or https:// . |

|   | aliyun |
|---|---|
| acs: |   |

|   | aliyun |
|---|---|
| acs: |   |

**Return value**

Fn::GetAtt LoadBalancerId: The ID of the new SLB instance.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SourceSLBId:
    AssociationProperty: ALIYUN::SLB::Instance::InstanceId
    Type: String
    Description: The ID of the source SLB instance to clone.
Resources:
  LoadBalancerClone:
    Type: ALIYUN::SLB::LoadBalancerClone
    Properties:
      LoadBalancerName: DemoCloneLoadBalancer
      SourceLoadBalancerId:
        Ref: SourceSLBId
Outputs:
  LoadBalancerId:
    Description: The ID of the generated SLB instance.
    Value:
      Fn::GetAtt:
        - LoadBalancerClone
        - LoadBalancerId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SourceSLBId": {
      "AssociationProperty": "ALIYUN::SLB::Instance::InstanceId",
      "Type": "String",
      "Description": "The ID of the source SLB instance to clone."
```

`},`

```json
  "Resources": {
    "LoadBalancerClone": {
      "Type": "ALIYUN::SLB::LoadBalancerClone",
      "Properties": {
        "LoadBalancerName": "DemoCloneLoadBalancer",
        "SourceLoadBalancerId": {
          "Ref": "SourceSLBId"
```

`},`

```json
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The ID of the generated SLB instance.",
      "Value": {
        "Fn::GetAtt": [
          "LoadBalancerClone",
          "LoadBalancerId"
```

`]`

#### ALIYUN::SLB::MasterSlaveServerGroup

ALIYUN::SLB::MasterSlaveServerGroup is used to create a primary/secondary server group.

**Important**

A primary/secondary server group contains only two ECS instances: a primary server and a secondary server.

**Syntax**

```json
  "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
  "Properties": {
    "MasterSlaveServerGroupName": String,
    "MasterSlaveBackendServers": List,
    "LoadBalancerId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterSlaveServ erGroupName | String | No | No | The name of the primary/seconda ry server group. | None |
| MasterSlaveBac kendServers | List | Yes | No | The list of backend servers in the primary/seconda ry server group. | A primary/seconda ry server group can contain a maximum of two backend servers. If you do not specify this parameter, an empty primary/seconda ry server group is created. |
| LoadBalancerId | String | Yes | No | The ID of the SLB instance. | None |

**MasterSlaveBackendServers syntax**

```json
"MasterSlaveBackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "ServerType": String
```

`]`

**MasterSlaveBackendServers properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | No | The ID of the ECS instance or Elastic Network Interface (ENI) to be added. | None |

| ServerType | String | No | No | The type of the server. | Default value: Master. Valid values: Master Slave |
|---|---|---|---|---|---|
| Port | Integer | Yes | No | The port number used by the backend server. | Valid values: 1 to 65535. |
| Weight | Integer | Yes | No | The weight of the backend server. | Valid values: 0 to 100. |

**Response parameters**

Fn::GetAtt MasterSlaveServerGroupId: the ID of the primary/secondary server group.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "MasterSlaveServerGroup": {
      "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
      "Properties": {
        "MasterSlaveServerGroupName": "Group1",
        "MasterSlaveBackendServers": [
            "ServerId": "vm****",
            "Port": "80",
            "Weight": "100",
            "ServerType": "Master"
```

`},`

```json
            "ServerId": "vm****",
            "Port": "90",
            "Weight": "100",
            "ServerType": "Slave"
```

`],`

```json
        "LoadBalancerId": "lb-bp1hv944r69al4j9j****"
```

`},`

```json
  "Outputs": {
    "MasterSlaveServerGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "MasterSlaveServerGroup",
          "MasterSlaveServerGroupId"
```

`]`

#### ALIYUN::SLB::Rule

ALIYUN::SLB::Rule is used to add forwarding rules for a specified HTTP or HTTPS listener.

**Syntax**

```json
  "Type": "ALIYUN::SLB::Rule",
  "Properties": {
    "ListenerPort": Integer,
    "RuleList": List,
    "LoadBalancerId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ListenerPort | Integer | Yes | No | The frontend listener port number used by the SLB instance. | Valid values: 1 to 65535. |
| RuleList | List | Yes | No | The list of forwarding rules to be added. | A maximum of 10 forwarding rules can be added at a time. Each forwarding rule contains the following parameters: RuleName Domain Url VServerGroup Id You must specify at least one of the Domain and URL parameters. The value combination specified by the Domain and URL parameters must be unique in a listener. |
| LoadBalancerId | String | Yes | No | The ID of the SLB instance. | None. |

**RuleList syntax**

```json
"RuleList": [
    "Url": String,
    "Domain": String,
    "VServerGroupId": String,
    "RuleName": String
```

`]`

**RuleList properties**

| Property | Type | Required | Editable | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| Url | String | No | No | The request URL. |   | The URL must be 2 to 80 characters in length. It must start with a forward slash (/) and can contain letters, digits, and the following special characters: - / . % ? # & |   |   |
|   |   |   |   |   |   |   | - / . % ? |   |
|   |   |   |   |   |   | # & |   |   |
| Domain | String | No | No | The request domain name associated with the forwarding rule. |   | None. |   |   |
| VServerGroupId | String | Yes | No | The ID of the destination VServer group specified in the forwarding rule. |   | None. |   |   |
| RuleName | String | Yes | No | The name of the forwarding rule. |   | The name must be 1 to 40 characters in length and can contain letters, digits, and the following special characters: - / . _ Forwarding rule names must be unique within each listener. |   |   |

**Response parameters**

Fn::GetAtt Rules: the list of forwarding rules.

**Examples**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Rule": {
      "Type": "ALIYUN::SLB::Rule",
      "Properties": {
        "ListenerPort": {
          "Ref": "ListenerPort"
```

`},`

```json
        "RuleList": {
          "Fn::Split": [",", {
            "Ref": "RuleList"
          }, {
            "Ref": "RuleList"
```

`}]` `},`

```json
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
```

`},`

```json
  "Parameters": {
    "ListenerPort": {
      "Type": "Number",
      "Description": "The front-end HTTPS listener port of the Server Load Balancer instance. Valid v
alue:\n1-65535",
      "MaxValue": 65535,
      "MinValue": 1
```

`},`

```json
    "RuleList": {
      "MinLength": 1,
      "Type": "CommaDelimitedList",
      "Description": "The forwarding rules to add.",
      "MaxLength": 10
```

`},`

```json
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The ID of Server Load Balancer instance."
```

`},`

```json
  "Outputs": {
    "Rules": {
      "Description": "A list of forwarding rules. Each element of rules contains \"RuleId\".",
      "Value": {
        "Fn::GetAtt": ["Rule", "Rules"]
```

#### ALIYUN::SLB::VServerGroup

ALIYUN::SLB::VServerGroup is used to create a vServer group and attach backend servers to a Server Load Balancer (SLB) instance.

**Syntax**

```json
  "Type": "ALIYUN::SLB::VServerGroup",
  "Properties": {
    "VServerGroupName": String,
    "BackendServers": List,
    "LoadBalancerId": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGroup Name | String | Yes | No | The name of the vServer group. | None |
| BackendServ ers | List | No | Yes | The list of backend servers. | You can attach a maximum of 20 Elastic Compute Service (ECS) instances. For more information, see BackendServers properties. |
| LoadBalancer Id | String | Yes | No | The ID of the SLB instance. | None |

**BackendServers syntax**

```json
"BackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
```

`]`

**BackendServers properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | None |
| Port | Integer | Yes | Yes | The port that is used by the backend server. | Valid values: 1 to 65535. |

| Weight | Integer | No | Yes | The weight of the backend server. | Valid values: 0 to 100. |
|---|---|---|---|---|---|
| Type | String | No | Yes | The type of the backend server. | Default value: ecs. Valid values: ecs: ECS instances eni: elastic network interfaces (ENIs) |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| ServerIp | String | No | Yes | The IP address of the backend server. | The IP addresses of ECS instances or ENIs are supported. |

**Response parameters**

Fn::GetAtt VServerGroupId: the ID of the vServer group. BackendServers: the list of backend servers attached to the SLB instance.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  LoadBalancerId:
    AssociationProperty: ALIYUN::SLB::Instance::InstanceId
    Type: String
    Description: The id of load balancer.
  ECSInstanceId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Instance::InstanceId
Resources:
  VServerGroup:
    Type: ALIYUN::SLB::VServerGroup
    Properties:
      VServerGroupName:
        Ref: ALIYUN::StackName
      LoadBalancerId:
        Ref: LoadBalancerId
      BackendServers:
        - ServerId:
            Ref: ECSInstanceId
          Port: '80'
Outputs:
  VServerGroupId:
    Description: The id of VServerGroup created.
    Value:
      Fn::GetAtt:
        - VServerGroup
        - VServerGroupId
  BackendServers:
    Description: Backend server list in this VServerGroup.
    Value:
      Fn::GetAtt:
        - VServerGroup
        - BackendServers
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LoadBalancerId": {
      "AssociationProperty":"ALIYUN::SLB::Instance::InstanceId",
      "Type":"String",
      "Description": "The id of load balancer."
```

`},`

```json
    "ECSInstanceId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceId"
```

`},`

```json
  "Resources": {
    "VServerGroup": {
      "Type": "ALIYUN::SLB::VServerGroup",
      "Properties": {
        "VServerGroupName": {
          "Ref": "ALIYUN::StackName"
```

`},`

```json
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
```

`},`

```json
        "BackendServers": [
            "ServerId": {
              "Ref": "ECSInstanceId"
```

`},`

```json
            "Port": "80"
```

`]` `},`

```json
  "Outputs": {
    "VServerGroupId": {
      "Description": "The id of VServerGroup created.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "VServerGroupId"
```

`]` `},`

```json
    "BackendServers": {
      "Description": "Backend server list in this VServerGroup.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "BackendServers"
```

`]`

### SLS

#### ALIYUN::SLS::Index

ALIYUN::SLS::Index is used to create an index for a Simple Log Service (SLS) Logstore.

**Syntax**

```json
  "Type": "ALIYUN::SLS::Index",
  "Properties": {
    "ProjectName": String,
    "FullTextIndex": Map,
    "LogstoreName": String,
    "KeyIndices": List,
    "LogReduce": Boolean
```

**Properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | No | The name of the SLS project. | The name must be 3 to 36 characters in length. It must start and end with a lowercase letter or a digit. It can contain lowercase letters, digits, hyphens (-), and underscores ( ). _ |
| FullTextIndex | Map | Yes | Yes | The full-text index configuration. | For more information, see FullTextIndex properties. |
| LogstoreNam e | String | Yes | No | The Logstore name. | None. |
| KeyIndices | List | No | Yes | The field index configuration. | You must specify at least one of FullTextIndex and KeyIndices. For more information, see Properties. |
| LogReduce | Boolean | No | Yes | Specifies whether to enable the LogReduce feature. | Valid values: true false (default) |

**FullTextIndex syntax**

```json
"FullTextIndex": {
  "CaseSensitive": Boolean,
  "Delimiter": String,
  "IncludeChinese": Boolean,
  "Enable": Boolean
```

**FullTextIndex properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| Enable | Boolean | Yes | Yes | Specifies whether to enable the full-text index. | Valid values: true (default) false |
| CaseSensitive | Boolean | No | Yes | Specifies whether the field is case- sensitive. | Valid values: true false (default) |
| Delimiter | String | No | Yes | The delimiter. | The following special characters are supported: ,'";=()[]{}?@& <>/:\n\t\r |
| IncludeChines e | Boolean | No | Yes | Specifies whether to include Chinese characters. | Valid values: true false (default) |

**KeyIndices syntax**

```json
"KeyIndices": [
    "Name": String,
    "EnableAnalytics": Boolean,
    "Delimiter": String,
    "CaseSensitive": Boolean,
    "JsonKeyIndices": List,
    "Alias": String,
    "IncludeChinese": String,
    "Type": String
```

`]`

**KeyIndices properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | Yes | The field name. | You can specify a name in the nested format separated with periods (.), for example: k1.k2.k3. |

| EnableAnalyti cs | Boolean |   | No |   |   | Yes |   | Specifies whether to enable statistical analysis for the field. |   | Valid values: true (default) false |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Delimiter | String |   | No |   |   | Yes |   | The delimiter. |   | The following special characters are supported: ,'";=()[]{}?@& <>/:\n\t\r |   |
| CaseSensitive | Boolean |   | No |   |   | Yes |   | Specifies whether the field is case- sensitive. |   | Valid values: true false (default) This property takes effect only when Type is set to text or json . |   |
| JsonKeyIndice s | List |   | No |   |   | Yes |   | The JSON index configuration. Format: [{"key1": |   | Supported keys include Name, Alias, Type, and |   |
|   |   |   |   |   |   |   |   |   | [{"key1": | EnableAnalytics. |   |
|   |   |   |   |   |   |   |   | "value1", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | For more information, s |   |
|   |   |   |   |   |   |   |   |   |   | For more in |   |
|   |   |   |   |   |   |   |   | "key2": |   | JsonKeyInd |   |
|   |   |   |   |   |   |   |   | "value2", |   |   |   |
|   |   |   |   |   |   |   |   | ...}] |   |   |   |
| Alias | String |   | No |   |   | Yes |   | The field alias. |   | None. |   |
| IncludeChines e | Boolean |   | No |   |   | Yes |   | Specifies whether to include Chinese characters. |   | Valid values: true false (default) This property takes effect only when Type is set to text. |   |
| Type | String |   | Yes |   |   | Yes |   | The field type. |   | Valid values: text (default) long double json |   |

**JsonKeyIndices syntax**

```json
"JsonKeyIndices": [
    "Type": String,
    "Alias": String,
    "EnableAnalytics": Boolean,
    "Name": String
```

`]`

**JsonKeyIndices properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | Yes | The field name. | None. |
| EnableAnalyti cs | Boolean | No | Yes | Specifies whether to enable query and analysis. | Valid values: true false |
| Alias | String | No | Yes | The field alias. | None. |
| Type | String | Yes | Yes | The field type. | None. |

**Return values**

Fn::GetAtt None.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Index": {
      "Type": "ALIYUN::SLS::Index",
      "Properties": {
        "ProjectName": {
          "Ref": "ProjectName"
```

`},`

```json
        "FullTextIndex": {
          "Ref": "FullTextIndex"
```

`},`

```json
        "LogstoreName": {
          "Ref": "LogstoreName"
```

`},`

```json
        "KeyIndices": {
          "Ref": "KeyIndices"
```

`},`

```json
        "LogReduce": {
          "Ref": "LogReduce"
```

`},`

```json
  "Parameters": {
    "ProjectName": {
      "Type": "String",
      "Description": "Project name:1. Only supports lowercase letters, numbers, hyphens (-) and under
scores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 3-63 charac ters.",
      "MinLength": 3,
      "MaxLength": 63
```

`},`

```json
    "FullTextIndex": {
      "Type": "Map",
      "Description": "Full-text indexing configuration.Full-text indexing and key indexing must have
at least one enabled."
```

`},`

```json
    "LogstoreName": {
      "Type": "String",
      "Description": "Logstore name:1. Only supports lowercase letters, numbers, hyphens (-) and unde
rscores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 3-63 chara cters.",
      "MinLength": 3,
      "MaxLength": 63
```

`},`

```json
    "KeyIndices": {
      "Type": "List",
      "Description": "Key index configurations.Full-text indexing and key indexing must have at least
one enabled."
```

`},`

```json
    "LogReduce": {
      "Default": false,
      "Type": "Boolean",
      "Description": "Whether to enable log reduce. Default to false.",
      "AllowedValues": [
        true,
        false
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  Index:
    Type: ALIYUN::SLS::Index
    Properties:
      ProjectName:
        Ref: ProjectName
      FullTextIndex:
        Ref: FullTextIndex
      LogstoreName:
        Ref: LogstoreName
      KeyIndices:
        Ref: KeyIndices
      LogReduce:
        Ref: LogReduce
Parameters:
  ProjectName:
    MinLength: 3
    MaxLength: 63
    Type: String
    Description: Project name:1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_).2. Must start and end with lowercase letters and numbers.3.
      The name length is 3-63 characters.
  FullTextIndex:
    Type: Map
    Description: Full-text indexing configuration.Full-text indexing and key indexing
      must have at least one enabled.
  LogstoreName:
    MinLength: 3
    MaxLength: 63
    Type: String
    Description: Logstore name:1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_).2. Must start and end with lowercase letters and numbers.3.
      The name length is 3-63 characters.
  KeyIndices:
    Type: List
    Description: Key index configurations.Full-text indexing and key indexing must
      have at least one enabled.
  LogReduce:
    Default: false
    Type: Boolean
    Description: Whether to enable log reduce. Default to false.
    AllowedValues:
    - true
    - false
```

#### ALIYUN::SLS::Logstore

ALIYUN::SLS::Logstore is used to create a Logstore in a Simple Log Service (SLS) project.

**Syntax**

```json
  "Type": "ALIYUN::SLS::Logstore",
  "Properties": {
    "ProjectName": String,
    "ShardCount": Integer,
    "AutoSplit": Boolean,
    "MaxSplitShard": Integer,
    "LogstoreName": String,
    "AppendMeta": Boolean,
    "TTL": Integer,
    "EnableTracking": Boolean,
    "PreserveStorage": Boolean,
    "EncryptConf": Map
```

**Properties**

| Property | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| ProjectName | String | Yes | No | The name of the log project to which the Logstore belongs. | The name must be 3 to 36 characters in length. The name can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must start and end with a _ lowercase letter or a digit. |
| ShardCount | Integer | No | Yes | The number of shards. | Valid values: 1 to 100. Default value: 2. Unit: shards. |
| MaxSplitShar d | Integer | No | Yes | The maximum number of shards that the system can create during automatic sharding. | Valid values: 1 to 64. You must specify MaxSplitShard when AutoSplit is set to true. |
| LogstoreNam e | String | Yes | No | The Logstore name. | The Logstore name must be unique within a log project. The name must be 3 to 36 characters in length. The name can contain lowercase letters, digits, hyphens (-), and underscores ( ). _ The name must start and end with a lowercase letter or a digit. |

| AutoSplit | Boolean | No | Yes | Specifies whether to enable automatic sharding. | Valid values: true false (default) |
|---|---|---|---|---|---|
| TTL | Integer | No | Yes | The data retention period. | Valid values: 1 to 3600. Default value: 30. Unit: days. |
| EnableTracki ng | Boolean | No | Yes | Specifies whether to enable web tracking for data collection. | You can use web tracking to collect information about web browsers, iOS applications, and Android applications. Valid values: true false (default). |
| PreserveStor age | Boolean | No | Yes | Specifies whether to permanently retain logs. | Valid values: true: permanently retains logs. If you set this property to true, the TTL setting does not take effect. false (default): does not permanently retain logs. |
| AppendMeta | Boolean | No | Yes | Specifies whether to automatically add the public IP address of the client and the log arrival time after the log is received. | Valid values: true: automatically adds the public IP address of the client and the log arrival time. false (default): does not automatically add the public IP address of the client and the log arrival time. |
| EncryptConf | Map | No | No | The encryption configuration for data. | For more information, see EncryptConf syntax and EncryptConf properties. |

**EncryptConf syntax**

```json
"EncryptConf": {
    "Enable": Boolean,
    "EncryptType": String,
    "UserCmkInfo": Map
```

**EncryptConf properties**

| Property | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|

| Enable | Boolean | Yes | No | Specifies whether to enable data encryption. | Valid values: true false (default) |
|---|---|---|---|---|---|
| EncryptType | String | Yes | No | The encryption algorithm. | Valid values: default: the AES algorithm. m4: the Chinese cryptographic algorithm. |
| UserCmkInfo | Map | No | No | If you specify UserCmkInfo, the bring- your-own-key (BYOK) method is used to encrypt or decrypt data. If you leave UserCmkInfo empty, the service key of SLS is used to encrypt or decrypt data. | For more information, see UserCmkInfo syntax and UserCmkInfo properties. |

**UserCmkInfo syntax**

```json
"UserCmkInfo": {
    "CmkKeyId": String,
    "Arn": String,
    "RegionId": String
```

**UserCmkInfo properties**

| Property | Type | Required | Update allowed | Description | Constraints |
|---|---|---|---|---|---|
| CmkKeyId | String | Yes | No | The ID of the customer master key (CMK) to which the BYOK key belongs. | None |
| Arn | String | Yes | No | The ID of the region where the CMK resides. | None |
| RegionId | String | Yes | No | The ARN of the RAM role. | None |

**Return values**

Fn::GetAtt LogstoreName: the name of the Logstore.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description: Test SLS Logstore Parameters: {} Resources:
  SlsLogStore:
    Type: ALIYUN::SLS::Logstore
    Properties:
      LogstoreName: mytest
      PreserveStorage: true
      ProjectName: TestProject
      AppendMeta: true
      MaxSplitShard: 64
      AutoSplit: true
      EnableTracking: false
      ShardCount: 2
Outputs: {}
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "Test SLS Logstore",
  "Parameters": {
```

`},`

```json
  "Resources": {
    "SlsLogStore": {
      "Type": "ALIYUN::SLS::Logstore",
      "Properties": {
        "LogstoreName": "mytest",
        "PreserveStorage": true,
        "ProjectName": "TestProject",
        "AppendMeta": true,
        "MaxSplitShard": 64,
        "AutoSplit": true,
        "EnableTracking": false,
        "ShardCount": 2
```

`},`

```json
  "Outputs": {
```

For more examples, see the combined examples of creating a log project, creating a Logstore, creating an index, configuring Logtail parameters, creating a SLS ECS machine group, applying a log configuration to a machine group, creating a log configuration, saving query results as a quick search, and creating an alert: JSON example and YAML example.

#### ALIYUN::SLS::LogtailConfig

ALIYUN::SLS::LogtailConfig is used to configure Logtail properties for data collection.

**Syntax**

```json
  "Type": "ALIYUN::SLS::LogtailConfig",
  "Properties": {
    "ProjectName": String,
    "LogtailConfigName": String,
    "LogstoreName": String,
    "RawConfigData": Map,
    "CloneFrom": Map
```

**Properties**

| Property |   |   | Type |   | Required |   | Update allowed |   | Description |   | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ProjectName |   |   | String |   | Yes |   | No |   | The name of the Simple Log Service (SLS) project. |   | None. |   |
| LogtailConfigNam e |   |   | String |   | Yes |   | No |   | The name of the Logtail configuration. |   | The configuration name must be unique within the same project. The name must be 2 to 128 characters in length and must start and end with a lowercase letter or a digit. The name can contain lowercase letters, digits, hyphens (- ), and underscores ( ). _ |   |
| LogstoreName |   |   | String |   | Yes |   | No |   | The name of the Logstore. |   | None. |   |
|   |   |   |   |   |   |   |   |   |   |   | The format is the same as the response of the Simple Log Service GetConfig API operation. If you specify both CloneFrom and RawConfigData, the system merges the Logtail configuration data with RawConfigData and ignores the configName, outputType, and outputDetail fields in RawConfigData. Example: {"configName": |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {"configName": |
|   |   |   |   |   |   |   |   |   |   |   | "test-logtail- |   |
|   |   |   |   |   |   |   |   |   |   |   | config", |   |
|   |   |   |   |   |   |   |   |   |   |   | "createTime": |   |
|   |   |   |   |   |   |   |   |   |   |   | 1574843554, |   |
|   |   |   |   |   |   |   |   |   |   |   | "inputDetail": |   |
|   |   |   |   |   |   |   |   |   |   |   | {"acceptNoEnoughKeys": |   |
|   |   |   |   |   |   |   |   |   |   |   | false, |   |
|   |   |   |   |   |   |   |   |   |   |   | "adjustTimezone": |   |
|   |   |   |   |   |   |   |   |   |   |   | false, "advanced": { |   |
|   |   |   |   |   |   |   |   |   |   |   | "force multiconfig": _ |   |

|   |   |   |   |   | false }, |
|---|---|---|---|---|---|
|   |   |   |   |   | "autoExtend": true, |
|   |   |   |   |   | "delayAlarmBytes": 0, |
|   |   |   |   |   | "delaySkipBytes": 0, |
|   |   |   |   |   | "discardNonUtf8": |
|   |   |   |   |   | false, |
|   |   |   |   |   | "discardUnmatch": |
|   |   |   |   |   | false, |
|   |   |   |   |   | "dockerExcludeEnv": |
|   |   |   |   |   | {}, |
|   |   |   |   |   | "dockerExcludeLabel": |
|   |   |   |   |   | {}, "dockerFile": |
|   |   |   |   |   | false, |
|   |   |   |   |   | "dockerIncludeEnv": |
|   |   |   |   |   | {}, |
|   |   |   |   |   | "dockerIncludeLabel": |
|   |   |   |   |   | {}, "enableRawLog": |
|   |   |   |   |   | false, "enableTag": |
|   |   |   |   |   | false, |
|   |   |   |   |   | "fileEncoding": |
|   |   |   |   |   | "utf8", |
|   |   |   |   |   | "filePattern": |
|   |   |   |   |   | "test.log*", |
|   |   |   |   |   | "filterKey": [], |
|   |   |   |   | The raw configuration | "filterRegex": [], |
| RawConfigData | Map | No | Yes |   |   |
|   |   |   |   | data. | "key": [ "time", |
|   |   |   |   |   | "logger", "level", |
|   |   |   |   |   | "request id", _ |
|   |   |   |   |   | "user id", _ |
|   |   |   |   |   | "region id", _ |
|   |   |   |   |   | "content" ], |
|   |   |   |   |   | "localStorage": true, |
|   |   |   |   |   | "logPath": |
|   |   |   |   |   | "/var/log/test", |
|   |   |   |   |   | "logTimezone": "", |
|   |   |   |   |   | "logType": |
|   |   |   |   |   | "delimiter log", _ |
|   |   |   |   |   | "maxDepth": 100, |
|   |   |   |   |   | "maxSendRate": -1, |
|   |   |   |   |   | "mergeType": "topic", |
|   |   |   |   |   | "preserve": true, |
|   |   |   |   |   | "preserveDepth": 1, |
|   |   |   |   |   | "priority": 0, |
|   |   |   |   |   | "quote": "\u0001", |
|   |   |   |   |   | "sendRateExpire": 0, |
|   |   |   |   |   | "sensitive keys": [], _ |
|   |   |   |   |   | "separator": ",,,", |
|   |   |   |   |   | "shardHashKey": [], |
|   |   |   |   |   | "tailExisted": false, |
|   |   |   |   |   | "timeFormat": "", |
|   |   |   |   |   | "timeKey": "", |
|   |   |   |   |   | "topicFormat": "none" |
|   |   |   |   |   | }, "inputType": |
|   |   |   |   |   | "file", |
|   |   |   |   |   | "lastModifyTime": |
|   |   |   |   |   | 1574843554, |
|   |   |   |   |   | "logSample": "2019- |
|   |   |   |   |   | 11-27 |
|   |   |   |   |   | 10:48:23,160,,,MAIN,,, |
|   |   |   |   |   | INFO,,,98DCC51D-BE5D- |
|   |   |   |   |   | 49C7-B3FD- |
|   |   |   |   |   | 37B2BAEFB296,,,1234567 |

|   |   |   |   |   | 89,,,cn- |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | hangzhou,,,this is a |   |
|   |   |   |   |   | simple test.", |   |
|   |   |   |   |   | "outputDetail": { |   |
|   |   |   |   |   | "endpoint": "cn- |   |
|   |   |   |   |   | hangzhou- |   |
|   |   |   |   |   | intranet.log.aliyuncs. |   |
|   |   |   |   |   | com", "logstoreName": |   |
|   |   |   |   |   | "test-logstore", |   |
|   |   |   |   |   | "region": "cn- |   |
|   |   |   |   |   | hangzhou"}, |   |
|   |   |   |   |   | "outputType": |   |
|   |   |   |   |   | "LogService"} |   |
| CloneFrom | Map | No | Yes | The Logtail configuration of a project that you clone. | You must specify either CloneFrom or a Logtail configuration. For more information, see CloneFrom properties. |   |

**CloneFrom syntax**

```json
"CloneFrom": {
  "ProjectName": String,
  "LogtailConfigName": String
```

**CloneFrom properties**

| Property | Type | Required | Update allowed | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | Yes | The name of the SLS project. | None. |
| LogtailConfig Name | String | Yes | Yes | The name of the Logtail configuration. | None. |

**Return values**

Fn::GetAtt Endpoint: the endpoint. AppliedMachineGroups: the machine groups to which the Logtail configuration is applied. LogtailConfigName: the name of the Logtail configuration.

**Examples**

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "LogtailConfig": {
      "Type": "ALIYUN::SLS::LogtailConfig",
      "Properties": {
        "ProjectName": {
```

```json
          "Ref": "ProjectName"
```

`},`

```json
        "LogtailConfigName": {
          "Ref": "LogtailConfigName"
```

`},`

```json
        "LogstoreName": {
          "Ref": "LogstoreName"
```

`},`

```json
        "RawConfigData": {
          "Ref": "RawConfigData"
```

`},`

```json
        "CloneFrom": {
          "Ref": "CloneFrom"
```

`},`

```json
  "Parameters": {
    "ProjectName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Project name: 1. Only supports lowercase letters, numbers, hyphens (-) and unde
rscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 cha racters.",
      "MaxLength": 63
```

`},`

```json
    "LogtailConfigName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logtail config name: 1. Only supports lowercase letters, numbers, hyphens (-) a
nd underscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3 -63 characters.",
      "MaxLength": 63
```

`},`

```json
    "LogstoreName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logstore name: 1. Only supports lowercase letters, numbers, hyphens (-) and und
erscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 ch aracters.",
      "MaxLength": 63
```

`},`

```json
    "RawConfigData": {
      "Type": "Json",
      "Description": "The format is the same as the response of SLS API GetConfig. Either CloneFrom o
r RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first. configName, outputType, outputDetail in data will be ignored.For example:\n{\"configName\": \"test-logtail-config\",\"createTime\": 1574843554,\"inputDetail\": { \"acceptNoEnoughKeys\": false, \"adjustTimezone\": false, \"advanced\": { \"force_multiconfig\": false }, \"autoExtend\": true, \"delayAlarmBytes\": 0, \"delaySkipBytes\": 0, \"discardNonUtf8\": false, \"discardUnmatch\": false, \"dockerExcludeEnv\": {}, \"dockerExcludeLabel\": {}, \"dockerFile\": false, \"dockerIncludeEnv\": {}, \"dockerIncludeLabel\": {}, \"enableRawLog\": false, \"enableTag\": false, \"fileEncoding\": \"utf8\", \"filePattern\": \"tes t.log*\", \"filterKey\": [], \"filterRegex\": [], \"key\": [ \"time\", \"logger\", \"level\", \"request_id\", \"user_id\", \"region_id\", \"content\" ], \"localStorage\": true, \"logPath\": \"/var/log/test\", \"logTimezone\": \"\", \"logType\": \"delimiter_log\", \"maxDepth\": 100, \"maxSendRate\": -1, \"mergeType\": \"topic\", \"preserve\": true, \"preserveDepth\": 1, \"priority\": 0, \"quote\": \"\\u0001\", \"sendRateExpire\": 0, \"sensitive_keys\": [], \"separator\": \",,,\", \"shardHashKey\": [], \"tailExisted\": false, \"timeFormat\": \"\", \"timeKey \": \"\", \"topicFormat\": \"none\"}, \"inputType\": \"file\", \"lastModifyTime\": 1574843554, \"logS ample\": \"2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B3FD- 37B2BAEFB296,,,123456789,,,cn-hangzhou,,,this is a simple test.\", \"outputDetail\": {\"endpoint\": \ "cn-hangzhou-intranet.log.aliyuncs.com\",\"logstoreName\":\"test-logstore\",\"region\":\"cn-hangzh
```

```
cnhangzhouintranet.log.aliyuncs.com\, \logstoreName\: \testlogstore\,\region\: \cnhangzh ou\"}, \"outputType\": \"LogService\"}"
```

`},`

```json
    "CloneFrom": {
      "Type": "Json",
      "Description": "Clone logtail config data from existing logtail config. Either CloneFrom or Raw
ConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first."
```

`},`

```json
  "Outputs": {
    "LogtailConfigName": {
     "Description": "Logtail config name.",
     "Value": {
      "Fn::GetAtt": [
       "LogtailConfig",
       "LogtailConfigName"
```

`]` `},`

```json
    "Endpoint": {
      "Description": "Endpoint address.",
      "Value": {
        "Fn::GetAtt": [
          "LogtailConfig",
          "Endpoint"
```

`]` `},`

```json
    "AppliedMachineGroups": {
      "Description": "Applied machine groups.",
      "Value": {
        "Fn::GetAtt": [
          "LogtailConfig",
          "AppliedMachineGroups"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  LogtailConfig:
    Type: ALIYUN::SLS::LogtailConfig
    Properties:
      ProjectName:
        Ref: ProjectName
      LogtailConfigName:
        Ref: LogtailConfigName
      LogstoreName:
        Ref: LogstoreName
      RawConfigData:
        Ref: RawConfigData
      CloneFrom:
        Ref: CloneFrom
Parameters:
  ProjectName:
    MinLength: 3
    Type: String
Description:'Projectname:1.Onlysupportslowercaseletters,numbers,hyphens
```

|   | Description: Project name: 1. Only supports lowercase letters, numbers, hyphens (-) and underscores ( ). 2. Must start and end with lowercase letters and numbers. _ 3. The name length is 3-63 characters.' MaxLength: 63 LogtailConfigName: MinLength: 3 Type: String Description: 'Logtail config name: 1. Only supports lowercase letters, numbers, hyphens (-) and underscores ( ). 2. Must start and end with lowercase letters _ and numbers. 3. The name length is 3-63 characters.' MaxLength: 63 LogstoreName: MinLength: 3 Type: String Description: 'Logstore name: 1. Only supports lowercase letters, numbers, hyphens (-) and underscores ( ). 2. Must start and end with lowercase letters and numbers. _ 3. The name length is 3-63 characters.' MaxLength: 63 RawConfigData: Type: Json Description: \|- The format is the same as the response of SLS API GetConfig. Either CloneFrom or RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be mer ged from both with RawConfigData first. configName, outputType, outputDetail in data will be ignored. For example: {"configName": "test-logtail-config","createTime": 1574843554,"inputDetail": { "acceptNoEnoughKeys": false, "adjustTimezone": false, "advanced": { "force multiconfig": false }, " _ autoExtend": true, "delayAlarmBytes": 0, "delaySkipBytes": 0, "discardNonUtf8": false, "discardUnmatch": false, "dockerExcludeEnv": {}, "dockerExcludeLabel": {}, "dockerFile": false, "dock erIncludeEnv": {}, "dockerIncludeLabel": {}, "enableRawLog": false, "enableTag": false, "fileEncoding": "utf8", "filePattern": "test.log*", "filterKey": [], "filterRegex": [], "key": [ "t ime", "logger", "level", "request id", "user id", "region id", "content" ], "localStorage" _ _ _ : true, "logPath": "/var/log/test", "logTimezone": "", "logType": "delimiter log", "maxDepth": 100, " _ maxSendRate": -1, "mergeType": "topic", "preserve": true, "preserveDepth": 1, "priority": 0, "quote": "\u0001", "sendRateExpire": 0, "sensitive keys": [], "separator": ",,,", "shardHashKey": [], "tailExi _ sted": false, "timeFormat": "", "timeKey": "", "topicFormat": "none"}, "inputType": "file", "lastModi fyTime": 1574843554, "logSample": "2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B3FD-37 B2BAEFB296,,,123456789,,,cn-hangzhou,,,this is a simple test.", "outputDetail": {"endpoint": "cn-hang zhou-intranet.log.aliyuncs.com", "logstoreName": "test-logstore","region": "cn-hangzhou"}, "outputType": "LogService"} CloneFrom: Type: Json Description: Clone logtail config data from existing logtail config. Either CloneFrom or RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first. Outputs: Endpoint: Description: Endpoint address. Value: Fn::GetAtt: - LogtailConfig - Endpoint AppliedMachineGroups: Description: Applied machine groups. Value: Fn::GetAtt: - LogtailConfig - AppliedMachineGroups LogtailConfigName: Description: Logtail config name. Value: Fn::GetAtt: - LogtailConfig |   |
|---|---|---|

```
      - LogtailConfigName
```

For more examples, see the combined examples of creating a project, creating a Logstore in the project, creating an index for a Logstore, configuring Logtail properties for data collection, creating an SLS machine group, applying an SLS configuration to a machine group, creating a log configuration, saving query results as a saved search, and creating an alert: JSON example and YAML example.

#### ALIYUN::SLS::Savedsearch

ALIYUN::SLS::Savedsearch is used to save search results as a saved search.

**Syntax**

```json
  "Type": "ALIYUN::SLS::Savedsearch",
  "Properties": {
    "Project": String,
    "Detail": Map
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Project | String | Yes | No | The name of the Log Service project. | None |
| Detail | Map | Yes | Yes | The details of the query. | For more information, see Detail properties. |

**Detail syntax**

```json
"Detail": {
  "SearchQuery": String,
  "Logstore": String,
  "DisplayName": String,
  "SavedsearchName": String,
  "Topic": String
```

**Detail properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SearchQuery | String | Yes | Yes | The query statement. | None |
| Logstore | String | Yes | Yes | The Logstore in which the query is performed. | None |

| DisplayName | String | No | Yes | The display name that you specify for the saved search. | The name must be 1 to 63 characters in length. |
|---|---|---|---|---|---|
| SavedsearchNa me | String | Yes | No | The name of the saved search, which is generated by the system in the project. | None |
| Topic | String | Yes | Yes | The log topic that is used to classify logs. | None |

**Response parameters**

Fn::GetAtt SavedsearchName: the name of the saved search.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SlsProjectName:
    Type: String
    Description: Project name
    MinLength: 3
    MaxLength: 63
    Default: mytest
Resources:
  SavedSearch:
    Type: ALIYUN::SLS::Savedsearch
    Properties:
      Project:
        Ref: SlsProjectName
      Detail:
        SearchQuery: '*|select date_format(__time__-__time__%60, ''%H:%i:%s'') as time, COUNT(*) as p
v group by time'
        Logstore: aliyun-test-***
        DisplayName: displayname
        SavedsearchName: test
        Topic: test
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SlsProjectName": {
      "Type": "String",
      "Description": "Project name",
      "MinLength": 3,
      "MaxLength": 63,
      "Default": "mytest"
```

`},`

```json
  "Resources": {
    "SavedSearch": {
      "Type": "ALIYUN::SLS::Savedsearch",
      "Properties": {
        "Project": {
          "Ref": "SlsProjectName"
```

`},`

```json
        "Detail": {
          "SearchQuery": "*|select date_format(__time__-__time__%60, '%H:%i:%s') as time, COUNT(*) as
pv group by time",
          "Logstore": "aliyun-test-***",
          "DisplayName": "displayname",
          "SavedsearchName": "test",
          "Topic": "test"
```

#### ALIYUN::SLS::Project

ALIYUN::SLS::Project is used to create a Log Service project.

**Syntax**

```json
  "Type": "ALIYUN::SLS::Project",
  "Properties": {
    "Name": String,
    "Description": String,
    "Tags": List
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | No | The name of the project. | The name must be 3 to 36 characters in length, and can contain lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit. |

| Description | String | No | No | The description of the project. | The description can be up to 64 characters in length, and cannot contain the following special characters: <> ' \ " |
|---|---|---|---|---|---|
| Tags | List | No | Yes | The tags of the project. | You can specify up to 20 tags. For more information, see Tags syntax and Tags properties. |

|   | " |
|---|---|

**Tags syntax**

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]`

**Tags properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |

**Response parameters**

Fn::GetAtt Name: the name of the Log Service project.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters: {} Resources:
  Project:
    Type: ALIYUN::SLS::Project
    Properties:
      Name: TestProject
Outputs:
  Name:
    Description: Project name.
    Value:
      Fn::GetAtt:
        - Project
        - Name
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
```

`},`

```json
  "Resources": {
    "Project": {
      "Type": "ALIYUN::SLS::Project",
      "Properties": {
        "Name": "TestProject"
```

`},`

```json
  "Outputs": {
    "Name": {
      "Description": "Project name.",
      "Value": {
        "Fn::GetAtt": [
          "Project",
          "Name"
```

`]`

### PAI

#### ALIYUN::PAI::Service

ALIYUN::PAI::Service is used to create an Elastic Algorithm Service (EAS) service in Machine Learning Platform for AI (PAI).

**Syntax**

```json
  "Type": "ALIYUN::PAI::Service",
  "Properties": {
    "Develop": String,
    "ServiceConfig": Map,
    "Labels": Map
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Develop | String | No | No | Specifies whether to enter the development mode. | Valid values: true false |

| ServiceConfig | Map | Yes | Yes | The configurations of the service. | Example: { "metadata": { "cpu":1, "instance": 1, "memory":10 24 }, "name":"ech o", "processor _ entry":"lib echo.so", "processor _ path":"http ://oss-cn- hangzhou- zmf.aliyunc s.com/05924 7/echo proc _ essor relea _ se.tar.gz", "processor _ type":"cpp" } |
|---|---|---|---|---|---|
| Labels | Map | No | Yes | The tags of the service. | Example: {"key":"val ue"} |

**Return values**

Fn::GetAtt ServiceGroup: the group to which the service belongs. Message: the summary of the service. Memory: the memory that you applied for each instance. CurrentVersion: the current version of the model. RunningInstance: the number of instances for the running service. Cpu: the CPU that you applied for each instance. Image: the data image of the service. Gpu: the GPU that you applied for each instance. CallerUid: the user ID of the account that is used to create the service. Reason: the reason why the service is in the current state. TotalInstance: the total number of instances of the service. ServiceConfig: the configurations of the service. AccessToken: the request token of the service. InternetEndpoint: the public endpoint of the service. ResourceAlias: the alias of the resource group to which the service belongs. CreateTime: the time when the service was created. Resource: the resource group to which the service belongs. Labels: the tags of the service. ExtraData: the additional information about the service. Namespace: the namespace to which the service belongs. Weight: the weight of the canary release for the service. Role: the role of the service. PendingInstance: the number of instances for the suspended service. LatestVersion: the latest version of the service. ServiceName: the name of the service. SafetyLock: the security lock of the service. UpdateTime: the time when the service was updated. ServiceUid: the service ID. The value of this property is the same as the value of ServiceId. RoleAttrs: the additional attributes of the service role. ParentUid: the user ID of the Alibaba Cloud account that is used to create the service. IntranetEndpoint: the private endpoint of the service.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  ServiceConfig:
    Type: Json
    Description: Service configuration information.
    Default:
      metadata:
        cpu: 1
        instance: 1
        memory: 1024
      name: echo
      processor_entry: libecho.so
      processor_path: http://oss-cn-hangzhou-zmf.aliyuncs.com/059247/echo_processor_release.tar.gz
      processor_type: cpp
  Labels:
    Type: Json
    Description: Service Tag.
    Default:
      key: value
Resources:
  ExtensionResource:
    Type: ALIYUN::PAI::Service
    Properties:
      ServiceConfig:
        Ref: ServiceConfig
      Labels:
        Ref: Labels
Outputs:
  ServiceGroup:
    Description: Group to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceGroup
  Message:
    Description: Latest information on services.
    Value:
      Fn::GetAtt:
        - ExtensionResource
```

`M`

```
        - Message
  Memory:
    Description: Memory of service (MB).
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Memory
  CurrentVersion:
    Description: Current running version of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CurrentVersion
  RunningInstance:
    Description: Number of instances in service running.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - RunningInstance
  Cpu:
    Description: Number of service CPU cores.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Cpu
  Image:
    Description: Service Deployment Mirroring.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Image
  Gpu:
    Description: Number of service GPU cards.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Gpu
  CallerUid:
    Description: The ID of the service creator, which can be the ID of the RAM account.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CallerUid
  Reason:
    Description: Service deployment failure reason.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Reason
  TotalInstance:
    Description: Total number of instances required by the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - TotalInstance
  ServiceConfig:
    Description: Service configuration information.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceConfig
  AccessToken:
    Description: Service Request authentication token.
```

`p` `q`

```
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - AccessToken
  InternetEndpoint:
    Description: Public network Endpoint of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - InternetEndpoint
  ResourceAlias:
    Description: Name of the resource group where the service resides.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ResourceAlias
  CreateTime:
    Description: Creation time of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - CreateTime
  Resource:
    Description: The ID of the resource group to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Resource
  Labels:
    Description: Service Tag.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Labels
  ExtraData:
    Description: Service Extra Information.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ExtraData
  Namespace:
    Description: The namespace to which the service belongs.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Namespace
  Weight:
    Description: Packet Service Traffic Weight.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Weight
  Role:
    Description: Grouping Service Role.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - Role
  PendingInstance:
    Description: Number of instances where the service is not currently ready.
    Value:
      Fn::GetAtt:
```

```
        - ExtensionResource
        - PendingInstance
  LatestVersion:
    Description: The latest version of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - LatestVersion
  ServiceName:
    Description: Service Name.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceName
  SafetyLock:
    Description: Service Security Lock Status.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - SafetyLock
  UpdateTime:
    Description: Service Last Updated.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - UpdateTime
  ServiceUid:
    Description: Unique Service ID.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ServiceUid
  RoleAttrs:
    Description: Grouping Service Role Properties.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - RoleAttrs
  ParentUid:
    Description: Primary account ID of the creator.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - ParentUid
  IntranetEndpoint:
    Description: The intranet Endpoint of the service.
    Value:
      Fn::GetAtt:
        - ExtensionResource
        - IntranetEndpoint
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ServiceConfig": {
      "Type": "Json",
      "Description": "Service configuration information.",
      "Default": {
        "metadata": {
          "cpu": 1,
```

```json
          "instance": 1,
          "memory": 1024
```

`},`

```json
        "name": "echo",
        "processor_entry": "libecho.so",
        "processor_path": "http://oss-cn-hangzhou-
zmf.aliyuncs.com/059247/echo_processor_release.tar.gz",
        "processor_type": "cpp"
```

`},`

```json
    "Labels": {
      "Type": "Json",
      "Description": "Service Tag.",
      "Default": {"key":"value"}
```

`},`

```json
  "Resources": {
    "ExtensionResource": {
      "Type": "ALIYUN::PAI::Service",
      "Properties": {
        "ServiceConfig": {
          "Ref": "ServiceConfig"
```

`},`

```json
        "Labels": {
          "Ref": "Labels"
```

`},`

```json
  "Outputs": {
    "ServiceGroup": {
      "Description": "Group to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceGroup"
```

`]` `},`

```json
    "Message": {
      "Description": "Latest information on services.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Message"
```

`]` `},`

```json
    "Memory": {
      "Description": "Memory of service (MB).",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Memory"
```

`]` `},`

```json
    "CurrentVersion": {
      "Description": "Current running version of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
"CurrentVersion"
```

```
          CurrentVersion
```

`]` `},`

```json
    "RunningInstance": {
      "Description": "Number of instances in service running.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "RunningInstance"
```

`]` `},`

```json
    "Cpu": {
      "Description": "Number of service CPU cores.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Cpu"
```

`]` `},`

```json
    "Image": {
      "Description": "Service Deployment Mirroring.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Image"
```

`]` `},`

```json
    "Gpu": {
      "Description": "Number of service GPU cards.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Gpu"
```

`]` `},`

```json
    "CallerUid": {
      "Description": "The ID of the service creator, which can be the ID of the RAM account.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "CallerUid"
```

`]` `},`

```json
    "Reason": {
      "Description": "Service deployment failure reason.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Reason"
```

`]` `},`

```json
    "TotalInstance": {
      "Description": "Total number of instances required by the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
```

```
          "TotalInstance"
```

`]` `},`

```json
    "ServiceConfig": {
      "Description": "Service configuration information.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceConfig"
```

`]` `},`

```json
    "AccessToken": {
      "Description": "Service Request authentication token.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "AccessToken"
```

`]` `},`

```json
    "InternetEndpoint": {
      "Description": "Public network Endpoint of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "InternetEndpoint"
```

`]` `},`

```json
    "ResourceAlias": {
      "Description": "Name of the resource group where the service resides.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ResourceAlias"
```

`]` `},`

```json
    "CreateTime": {
      "Description": "Creation time of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "CreateTime"
```

`]` `},`

```json
    "Resource": {
      "Description": "The ID of the resource group to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Resource"
```

`]` `},`

```json
    "Labels": {
      "Description": "Service Tag.",
      "Value": {
        "Fn::GetAtt": [
"EtensionResorce"
```

```
          "ExtensionResource",
          "Labels"
```

`]` `},`

```json
    "ExtraData": {
      "Description": "Service Extra Information.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ExtraData"
```

`]` `},`

```json
    "Namespace": {
      "Description": "The namespace to which the service belongs.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Namespace"
```

`]` `},`

```json
    "Weight": {
      "Description": "Packet Service Traffic Weight.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Weight"
```

`]` `},`

```json
    "Role": {
      "Description": "Grouping Service Role.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "Role"
```

`]` `},`

```json
    "PendingInstance": {
      "Description": "Number of instances where the service is not currently ready.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "PendingInstance"
```

`]` `},`

```json
    "LatestVersion": {
      "Description": "The latest version of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "LatestVersion"
```

`]` `},`

```json
    "ServiceName": {
      "Description": "Service Name.",
      "Value": {
        "Fn::GetAtt": [
```

```
          "ExtensionResource",
          "ServiceName"
```

`]` `},`

```json
    "SafetyLock": {
      "Description": "Service Security Lock Status.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "SafetyLock"
```

`]` `},`

```json
    "UpdateTime": {
      "Description": "Service Last Updated.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "UpdateTime"
```

`]` `},`

```json
    "ServiceUid": {
      "Description": "Unique Service ID.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ServiceUid"
```

`]` `},`

```json
    "RoleAttrs": {
      "Description": "Grouping Service Role Properties.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "RoleAttrs"
```

`]` `},`

```json
    "ParentUid": {
      "Description": "Primary account ID of the creator.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "ParentUid"
```

`]` `},`

```json
    "IntranetEndpoint": {
      "Description": "The intranet Endpoint of the service.",
      "Value": {
        "Fn::GetAtt": [
          "ExtensionResource",
          "IntranetEndpoint"
```

`]`

### VPC

#### ALIYUN::VPC::EIP

ALIYUN::VPC::EIP is used to apply for an Elastic IP address.

**Statement**

```json
  "Type": "ALIYUN::VPC::EIP",
  "Properties": {
    "Isp": String,
    "Period": Number,
    "ResourceGroupId": String,
    "AutoPay": Boolean,
    "InstanceChargeType": String,
    "PricingCycle": String,
    "InternetChargeType": String,
    "Bandwidth": Number
```

**Properties**

| Parameter | Type | Require d | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the RDS instance belongs. | None |
| Bandwidth | Number | Erased | Released | The network bandwidth. Unit: Mbit/s. | If this parameter is not specified, the default value 5Mbps is used. |
| InternetChargeT ype | String | Yes | Released | The billing method for network usage. Default value: PayByBandwidt h. | Valid values: PayByBandwidth: pay-by- bandwidth. PayByTraffic Default value: PayByBandwidth. |
| InstanceCharge Type | String | Yes | Released | The billing method of the Elastic IP address. Default value: Postpaid. | Valid values: Prepaid Postpaid: pay-as-you-go Default value: PostPaid. |
| PricingCycle | String | Yes | Released | The billing cycle of the subscription. Default value: Month. | Valid values: Month: paid by month. Year Default value: Month. Note This parameter is required when InstanceChargeType is set to Prepaid. |

| Period | Number | Erased | Released | The subscription period. | Valid values: If pay by month is selected, the billing method can be a fee of 1 to 9. If pay-as-you-go is selected, the payment can be in the range of 1 to 3. Default value: 1 Note This parameter is required when InstanceChargeType is set to Prepaid. |
|---|---|---|---|---|---|
| AutoPay | Boolean | Erased | Released | Specifies whether to enable automatic payment. | Valid values: false: Automatic payment is disabled. After an order is generated, you must go to the Order Center to make the payment. true: Automatic payment is enabled. Payments are automatically made. Note This parameter is required when InstanceChargeType is set to Prepaid. |
| Isp | String | Yes | Released | The ISP tag used for Finance Cloud. This parameter takes effect only when your region is set to China (Hangzhou). | This parameter is ignored if you are not a Finance Cloud user. |

**Response parameters**

Fn::GetAtt EipAddress: the allocated Elastic IP address. AllocationId: the ID of the instance that the Elastic IP address is allocated to. OrderId: The order ID that is returned when you set the InstanceChargeType parameter to Prepaid.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Eip": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "InternetChargeType": "PayByTraffic",
          "Bandwidth": 200
```

`},`

```json
  "Outputs": {
    "EipAddress": {
      "Value" : {"Fn::GetAtt": ["Eip", "EipAddress"]}
```

`},`

```json
    "AllocationId": {
      "Value" : {"Fn::GetAtt": ["Eip", "AllocationId"]}
```

`},`

```json
    "OrderId": {
      "Value" : {"Fn::GetAtt": ["Eip", "OrderId"]}
```

#### ALIYUN::VPC::EIPAssociation

ALIYUN::VPC::EIPAssociation is used to associate an elastic IP address (EIP) with a cloud service instance.

**Syntax**

```json
  "Type": "ALIYUN::VPC::EIPAssociation",
  "Properties": {
    "AllocationId": String,
    "InstanceId": String,
    "PrivateIpAddress": String,
    "Mode": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllocationId | String | Yes | Yes | The ID of the EIP. | None |
| InstanceId | String | Yes | Yes | The ID of the cloud service instance. | The following types of instances are supported: Elastic Compute Service (ECS) instances of the virtual private cloud (VPC) type Server Load Balancer (SLB) instances of the VPC type NAT gateways High-availability virtual IP addresses (HAVIPs) Elastic network interfaces (ENIs) |

| PrivateIpAddr ess | String | No | Yes | The private IP address in the CIDR block of the vSwitch. | If you do not set this property, the system allocates a private IP address based on the VPC ID and vSwitch ID. |
|---|---|---|---|---|---|
| Mode | String | No | Yes | The association mode. | Defaut value: NAT. Valid values: NAT: the standard NAT gateway mode MULTI BINDED: the multi- _ EIP-to-ENI mode BINDED: the cut-through mode |

**Return values**

Fn::GetAtt EipAddress: the EIP. AllocationId: the ID of the EIP.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Description:
  en: Create a VPC type ECS and bind EIP (existing VPC).
Parameters:
  VPC:
    AssociationProperty: ALIYUN::ECS::VPC::VPCId
    Type: String
    Description:
      en: Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud.
    Label:
      en: VPC ID
  VSwitch:
    AssociationProperty: ALIYUN::ECS::VSwitch::VSwitchId
    AssociationPropertyMetadata:
      VpcId: VPC
    Type: String
    Description:
      en: Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch must be u
nder VPC. ECS will be created under this VSwitch.</font>
        </font>
    Label:
      en: VSwitch ID
  SecurityGroup:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Description:
      en: Please search the business security group ID starting with (sg-xxx) from console-ECS-Netw
ork & Security.
        </font>
    Label:
      en: Business Security Group ID
    AssociationPropertyMetadata:
      VpcId: VPC
ECSPassword:
```

```
  ECSPassword:
    NoEcho: true
    Type: String
    Description:
      en: Server login password, Length 8-30, must contain three (Capital letters, lowercase letter
s, numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).
    AllowedPattern: '[0-9A-Za-z\_\-\&:;''<>,=%`~!@#\(\)\$\^\*\+\|\{\}\[\]\.\?\/]+$'
    Label:
      en: Instance Password
    MinLength: 8
    ConstraintDescription:
      en: Length 8-30, must contain three (Capital letters, lowercase letters, numbers,
()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).
    MaxLength: 30
    Default: Null
  EIPInternetChargeType:
    Type: String
    AllowedValues:
      - PayByBandwidth
      - PayByTraffic
    Description:
      en: The charge type of EIP, PayByBandwidth;PayByTraffic.
    Label:
      en: EIP Charge Type
    Default: PayByTraffic
  ECSImageId:
    Type: String
    AssociationProperty: ALIYUN::ECS::Instance::ImageId
    Description:
      en: Image ID, Please use Centos7.
    Label:
      en: Image
    Default: ubuntu_14
  ECSZoneId:
    AssociationProperty: ALIYUN::ECS::Instance:ZoneId
    Type: String
    Description:
      en: 'Availability zone ID.<br><b>Note: <font color=''blue''>Before selecting, please confirm
whether the availability zone supports the specification of creating ECS resources. It is recommend ed to be different from other switch availability zones</font></b ><br><font color=''red''>The swit ch availability zone and the selected switch instance ID must be in the same availability zone.</fo nt>'
        </font>
    Label:
      en: VSwitch Availability Zone
  EIPBandwidth:
    Type: Number
    Description:
      en: 'EIP Bandwidth, Value range: [1,200], unit: Mbps.'
    MinValue: 1
    Label:
      en: EIP Bandwidth
    MaxValue: 200
```

```xml
    Default: 1
  ECSInstanceType:
    AssociationPropertyMetadata:
      ZoneId: ECSZoneId
      InstanceChargeType: InstanceChargeType
    AssociationProperty: ALIYUN::ECS::Instance::InstanceType
    Type: String
    Description:
      en: <font color='blue'><b>1.Before selecting the model please confirm that the current
available zone under the model is in stock, some models need to be reported in advance</b></font><b r><font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font color='g reen'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</font>] <br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1.5Gbps In-grid sending and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color='green'>8vCPU 16GiB Intra net bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]
          </font>]
    Label:
      en: Instance Type
  ECSDiskCategory:
    Type: String
    Description:
      en: '<font color=''blue''><b>Optional values:</b></font><br>[cloud_efficiency: <font
color=''green''>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color=''green''>SSD Cloud Disk</f ont>]<br>[cloud_essd: <font color=''green''>ESSD Cloud Disk</font>]<br>[cloud: <font color=''green''>Cloud Disk</font>]<br>[ephemeral_ssd: <font color=''green''>Local SSD Cloud Disk</f ont>]'
    AssociationProperty: ALIYUN::ECS::Disk::SystemDiskCategory
    AssociationPropertyMetadata:
      ZoneId: ECSZoneId
      InstanceType: ECSInstanceType
    Label:
      en: System Disk Type
  ECSSysDiskSize:
    Type: Number
    Description:
      en: 'System disk size, range of values: 40-500, units: GB.'
    MinValue: 40
    Label:
      en: System Disk Space
    MaxValue: 500
    Default: 40
  InstanceChargeType:
    Type: String
    Label:
      en: Instance Charge Type
    Description:
      en: '<font color=''blue''><b>Optional values:</b></font><br>[PostPaid: <font
color=''green''>Pay as you go.</font>]<br> [PrePaid: <font color=''green''>Prepaid, monthly subscri ption.</font>]'
        </font>]'
    AllowedValues:
      - PostPaid
      - PrePaid
    Default: PostPaid
  KeyPairName:
    Type: String
AssociationPopet ALIYUN ECS KePai KePaiName
```

```
    AssociationProperty: ALIYUN::ECS::KeyPair::KeyPairName
    Label:
      en: Key Pair Name
    Description:
      en: If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>If you h
ave filled in <font color='green'>key pair name</font>, <font color='green'>instance password< The content of /font> will still be set in the instance, but the password login method in the Linux sys tem will be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If you use the instance password Login, the key pair name does not need to be filled in.</font>
           </font>
    Default: Null
Metadata:
  ALIYUN::ROS::Interface:
    ParameterGroups:
      - Parameters:
          - VPC
          - VSwitch
          - SecurityGroup
        Label:
          default: 'VPC '
      - Parameters:
          - EIPBandwidth
          - EIPInternetChargeType
        Label:
          default: EIP
      - Parameters:
          - ECSZoneId
          - ECSImageId
          - ECSInstanceType
          - ECSDiskCategory
          - ECSSysDiskSize
          - InstanceChargeType
          - ECSPassword
          - KeyPairName
        Label:
          default: ECS
    TemplateTags:
      - Specify the image Id and snapshot to create ECS instance.
Resources:
  ECSInstanceGroup:
    Type: ALIYUN::ECS::InstanceGroup
    Properties:
      IoOptimized: optimized
      InstanceChargeType:
        Ref: InstanceChargeType
      ZoneId:
        Ref: ECSZoneId
      SystemDisk_Category:
        Ref: ECSDiskCategory
      SecurityGroupId:
        Ref: SecurityGroup
      VSwitchId:
        Ref: VSwitch
      MaxAmount: 1
      SystemDisk_Size:
        Ref: ECSSysDiskSize
      VpcId:
        Ref: VPC
      ImageId:
        Ref: ECSImageId
      InstanceType:
        Ref: ECSInstanceType
```

```
      AllocatePublicIP: 'false'
      Password:
        Ref: ECSPassword
      KeyPairName:
        Ref: KeyPairName
  ElasticIp:
    Type: ALIYUN::VPC::EIP
    Properties:
      Bandwidth:
        Ref: EIPBandwidth
      InternetChargeType:
        Ref: EIPInternetChargeType
  ElasticIpAssociation:
    Type: ALIYUN::VPC::EIPAssociation
    Properties:
      InstanceId:
        Fn::Select:
          - Fn::GetAtt:
              - ECSInstanceGroup
              - InstanceIds
      AllocationId:
        Ref: ElasticIp
Outputs:
  VpcId:
    Description: VPC Id
    Value:
      Ref: VPC
  SecurityGroupId:
    Description: Security Group Id
    Value:
      Ref: SecurityGroup
  VSwitchId:
    Description: VSwitch Id
    Value:
      Ref: VSwitch
  EipAddress:
    Description: IP address of created EIP.
    Value:
       Fn::GetAtt:
        - ElasticIp
        - EipAddress
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": {
    "en": "Create a VPC type ECS and bind EIP (existing VPC).",
```

`},`

```json
  "Parameters": {
    "VPC": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Description": {
        "en": "Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud.",
```

`},`

```json
      "Label": {
        "en": "VPC ID",
```

`},`

```json
    "VSwitch": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
```

`},`

```json
      "Type": "String",
      "Description": {
        "en": "Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch must
be under VPC. ECS will be created under this VSwitch.</font>",
          </font>"
```

`},`

```json
      "Label": {
        "en": "VSwitch ID",
```

`},`

```json
    "SecurityGroup": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Description": {
        "en": "Please search the business security group ID starting with (sg-xxx) from console-ECS
-Network & Security.",
          </font>"
```

`},`

```json
      "Label": {
        "en": "Business Security Group ID",
```

`},`

```json
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
```

`},`

```json
    "ECSPassword": {
      "NoEcho": true,
      "Type": "String",
      "Description": {
        "en": "Server login password, Length 8-30, must contain three (Capital letters, lowercase l
etters, numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
```

`},`

```json
      "AllowedPattern": "[0-9A-Za-z\\_\\-\\&:;'<>,=%`~!@#\\(\\)\\$\\^\\*\\+\\|\\{\\}\\[\\]\\.\\?\\/
]+$",
      "Label": {
        "en": "Instance Password",
```

`},`

```json
      "MinLength": 8,
      "ConstraintDescription": {
        "en": "Length 8-30, must contain three(Capital letters, lowercase letters, numbers,
()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
```

`},`

```json
      "MaxLength": 30,
      "Default": null
```

`},`

```json
    "EIPInternetChargeType": {
      "Type": "String",
      "AllowedValues": [
        "PayByBandwidth",
        "PayByTraffic"
```

`],`

```json
      "Description": {
        "en": "The charge type of EIP, PayByBandwidth;PayByTraffic.",
```

`},`

```json
      "Label": {
        "en": "EIP Charge Type",
```

`},`

```json
      "Default": "PayByTraffic"
```

`},`

```json
    "ECSImageId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::ImageId",
      "Description": {
        "en": "Image ID,Please use Centos7.",
```

`},`

```json
      "Label": {
        "en": "Image",
```

`},`

```json
      "Default": "ubuntu_14"
```

`},`

```json
    "ECSZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": {
        "en": "Availability zone ID.<br><b>Note: <font color='blue'>Before selecting, please
confirm whether the availability zone supports the specification of creating ECS resources. It is r ecommended to be different from other switch availability zones</font></b ><br><font color='red'>The switch availability zone and the selected switch instance ID must be in the same av ailability zone.</font>",
          </font>"
```

`},`

```json
      "Label": {
        "en": "VSwitch Availability Zone",
```

`},`

```json
    "EIPBandwidth": {
      "Type": "Number",
      "Description": {
        "en": "EIP Bandwidth, Value range: [1,200], unit: Mbps.",
```

`},`

```json
      "MinValue": 1,
      "Label": {
        "en": "EIP Bandwidth",
```

`},`

```json
      "MaxValue": 200,
      "Default": 1
```

`},`

```json
    "ECSInstanceType": {
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceChargeType": "InstanceChargeType"
```

`},`

```json
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceType",
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>1.Before selecting the model please confirm that the current a
ilbl
```

`d` `th`

```
dli
```

`i` `t` `k` `d``l` `d``t` `b`

```
tdi
```

`d`

```
</b></f t><b
```

```
vailable zone under the model is in stock, some models need to be reported in advance</b></font><br ><font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font color='gr een'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</font>]< br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1.5Gbps In-grid sending and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color='green'>8vCPU 16GiB Intra net bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]",
            </font>]"
```

`},`

```json
      "Label": {
        "en": "Instance Type",
```

`},`

```json
    "ECSDiskCategory": {
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[cloud_efficiency: <font
color='green'>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color='green'>SSD Cloud Disk</font>]<br>[cloud_essd: <font color='green'>ESSD Cloud Disk</font>]<br>[cloud: <font color='gr een'>Cloud Disk</font>]<br>[ephemeral_ssd: <font color='green'>Local SSD Cloud Disk</font>]",
```

`},`

```json
      "AssociationProperty": "ALIYUN::ECS::Disk::SystemDiskCategory",
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceType": "ECSInstanceType"
```

`},`

```json
      "Label": {
        "en": "System Disk Type",
```

`},`

```json
    "ECSSysDiskSize": {
      "Type": "Number",
      "Description": {
        "en": "System disk size, range of values: 40-500, units: GB.",
```

`},`

```json
      "MinValue": 40,
      "Label": {
        "en": "System Disk Space",
```

`},`

```json
      "MaxValue": 500,
      "Default": 40
```

`},`

```json
    "InstanceChargeType": {
      "Type": "String",
      "Label": {
        "en": "Instance Charge Type",
```

`},`

```json
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[PostPaid: <font
color='green'>Pay as you go.</font>]<br> [PrePaid: <font color='green'>Prepaid, monthly subscriptio n.</font>]",
          </font>]"
```

`},`

```json
      "AllowedValues": [
        "PostPaid",
        "PrePaid"
```

`],`

```json
      "Default": "PostPaid"
```

`},`

```json
    "KeyPairName": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::KeyPair::KeyPairName",
      "Label": {
        "en": "Key Pair Name",
```

`},`

```json
      "Description": {
        "en": "If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>If
you have filled in <font color='green'>key pair name</font>, <font color='green'>instance password< The content of /font> will still be set in the instance, but the password login method in the Linux system will be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If y ou use the instance password Login, the key pair name does not need to be filled in.</font>",
             </font>"
```

`},`

```json
      "Default": null
```

`},`

```json
  "Metadata": {
    "ALIYUN::ROS::Interface": {
      "ParameterGroups": [
          "Parameters": [
            "VPC",
            "VSwitch",
            "SecurityGroup"
```

`],`

```json
          "Label": {
            "default": "VPC "
```

`},`

```json
          "Parameters": [
            "EIPBandwidth",
            "EIPInternetChargeType"
```

`],`

```json
          "Label": {
            "default": "EIP"
```

`},`

```json
          "Parameters": [
            "ECSZoneId",
            "ECSImageId",
            "ECSInstanceType",
            "ECSDiskCategory",
            "ECSSysDiskSize",
            "InstanceChargeType",
            "ECSPassword",
            "KeyPairName"
```

`],`

```json
          "Label": {
            "default": "ECS"
```

`],`

```json
      "TemplateTags": [
        "Specify the image Id and snapshot to create ECS instance."
```

`]` `},`

```json
  "Resources": {
    "ECSInstanceGroup": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "IoOptimized": "optimized",
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
```

`},`

```json
        "ZoneId": {
          "Ref": "ECSZoneId"
```

`},`

```json
        "SystemDisk_Category": {
          "Ref": "ECSDiskCategory"
```

`},`

```json
        "SecurityGroupId": {
          "Ref": "SecurityGroup"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitch"
```

`},`

```json
        "MaxAmount": 1,
        "SystemDisk_Size": {
          "Ref": "ECSSysDiskSize"
```

`},`

```json
        "VpcId": {
          "Ref": "VPC"
```

`},`

```json
        "ImageId": {
          "Ref": "ECSImageId"
```

`},`

```json
        "InstanceType": {
          "Ref": "ECSInstanceType"
```

`},`

```json
        "AllocatePublicIP": "false",
        "Password": {
          "Ref": "ECSPassword"
```

`},`

```json
        "KeyPairName": {
          "Ref": "KeyPairName"
```

`},`

```json
    "ElasticIp": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "Bandwidth": {
          "Ref": "EIPBandwidth"
```

`},`

```json
        "InternetChargeType": {
          "Ref": "EIPInternetChargeType"
```

`},`

```json
    "ElasticIpAssociation": {
      "Type": "ALIYUN::VPC::EIPAssociation",
      "Properties": {
        "InstanceId": {
          "Fn::Select": [
```

`0,`

```
              "Fn::GetAtt": [
                "ECSInstanceGroup",
"InstanceIds"
```

```
                InstanceIds
```

`]` `]` `},`

```json
        "AllocationId": {
          "Ref": "ElasticIp"
```

`},`

```json
  "Outputs": {
    "VpcId": {
      "Description": "VPC Id",
      "Value": {
        "Ref": "VPC"
```

`},`

```json
    "SecurityGroupId": {
      "Description": "Security Group Id",
      "Value": {
        "Ref": "SecurityGroup"
```

`},`

```json
    "VSwitchId": {
      "Description": "VSwitch Id",
      "Value": {
        "Ref": "VSwitch"
```

`},`

```json
    "EipAddress": {
      "Description": "IP address of created EIP.",
      "Value": {
        "Fn::GetAtt": [
          "ElasticIp",
          "EipAddress"
```

`]`

#### ALIYUN::VPC::PeeringRouterInterfaceBinding

ALIYUN::VPC::PeeringRouterInterfaceBinding is used to associate two router interfaces to be interconnected.

**Statement**

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
  "Properties": {
    "OppositeRouterId": String,
    "OppositeInterfaceId": String,
    "OppositeInterfaceOwnerId": String,
    "RouterInterfaceId": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| RouterInterfaceI d | String | No | No | The ID of the router interface. | None |
|---|---|---|---|---|---|
| OppositeInterfac eId | String | No | No | The ID of the peer router interface. | None |
| OppositeRouterI d | String | Yes | Released | The ID of the router to which the peer router interface belongs. | None |
| OppositeInterfac eOwnerId | String | Yes | Released | The ID of the owner of the peer router interface. | None |

**Response parameters**

Fn::GetAtt RouterInterfaceId: the ID of the vRouter.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
      "Properties": {
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2zex1tkyym98pjaor****",
        "OppositeRouterId": "vrt-2zexb35tzoriu0286****"
```

**7.11.4.**

#### ALIYUN::VPC::PeeringRouterInterfaceConnection

ALIYUN::VPC::PeeringRouterInterfaceConnection is used to initiate a router interface connection.

**Statement**

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
  "Properties": {
    "OppositeInterfaceId": String,
    "RouterInterfaceId": String
```

**Properties**

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| OppositeInterfac eId | String | No | No | The ID of the acceptor router interface. | None |

| RouterInterfaceI d | String | No | No | The ID of the router interface to initiate the connection. | None |
|---|---|---|---|---|---|

**Response parameters**

Fn::GetAtt OppositeInterfaceId: the ID of the acceptor router interface. RouterInterfaceId: the ID of the router interface that initiates the connection.

**Sample request**

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
      "Properties": {
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2ze4k5n2aeardu8cy****"
```

#### ALIYUN::VPC::RouterInterface

ALIYUN::VPC::RouterInterface is used to create a router interface.

**Syntax**

```json
  "Type": "ALIYUN::VPC::RouterInterface",
  "Properties": {
    "OppositeRegionId": String,
    "Description": String,
    "HealthCheckSourceIp": String,
    "RouterType": String,
    "AccessPointId": String,
    "RouterId": String,
    "Role": String,
    "OppositeInterfaceOwnerId": String,
    "OppositeAccessPointId": String,
    "OppositeInterfaceId": String,
    "HealthCheckTargetIp": String,
    "OppositeRouterId": String,
    "Spec": String,
    "OppositeRouterType": String,
    "Name": String,
    "PricingCycle": String,
    "Period": Number,
    "AutoPay": Boolean,
    "InstanceChargeType": String
```

**Properties**

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| RouterId | String | Yes | No | The ID of the router to which the router interface belongs. | None |
|---|---|---|---|---|---|
| Role | String | Yes | No | The role of the router interface. A router interface can either be a connection initiator or a connection acceptor. | Valid values: InitiatingSide This parameter must be set to InitiatingSide when the RouterType parameter is set to VBR. AcceptingSide This parameter must be set to AcceptingSide when the OppositeRouterTyp e parameter is set to VBR. |
| RouterType | String | No | No | The type of the router to which the router interface belongs. | Valid values: VRouter: VPC router VBR: virtual border router |
| AccessPointId | String | No | No | The ID of the access point of the router interface. | This parameter is required when the RouterType parameter is set to VBR. The access point ID cannot be modified after the router interface is created. This parameter cannot be set when the RouterType parameter is set to VRouter. |

| Spec | String | No | No | The specifications of the router interface. | The following list includes available specifications and the corresponding bandwidth values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s This parameter is required when the Role parameter is set to InitiatingSide. The value Negative is used by default when the Role parameter is set to AcceptingSide. |
|---|---|---|---|---|---|
| OppositeRegi onId | String | No | No | The region ID of the peer router interface. | None |
| OppositeInter faceOwnerId | String | No | Yes | The ID of the owner of the peer router interface. | The default value is the ID of the current user. |
| OppositeInter faceId | String | No | Yes | The ID of the peer router interface. | None |
| OppositeRout erId | String | No | Yes | The ID of the router to which the peer router interface belongs. | None |
| OppositeRout erType | String | No | Yes | The type of the router to which the peer router interface belongs. | Valid values: VRouter: VPC router This parameter must be set to VRouter when the RouterType parameter is set to VBR. VBR: virtual border router |

| OppositeAcce ssPointId | String | No | No | The ID of the access point of the peer router interface. | This parameter is required when the OppositeRouterType parameter is set to VBR. The access point ID cannot be modified after the router interface is created. This parameter cannot be set when the OppositeRouterType parameter is set to VRouter. Note When the OppositeRouterTy pe parameter is set to VBR, the VBR specified by the OppositeRouterId parameter must be in the access point specified by the OppositeAccessPo intId parameter. |
|---|---|---|---|---|---|
| Description | String | No | Yes | The description of the router interface. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . This parameter is empty by default. |
| Name | String | No | Yes | The display name of the router interface. | The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |
| HealthCheckS ourceIp | String | No | No | The source IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces that have a peer router interface on a VBR. It must be an unused IP address in the VPC where the local VRouter is located. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both unspecified. |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

| HealthCheckT argetIp | String | No | No | The destination IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces that have a peer router interface on a VBR. Typically, you can use the IP address of a customer premises equipment (CPE) on the user side of the leased line, which is the IP address of the peer gateway on the VBR where the peer router interface is located. You can also specify another IP address on the user side of the leased line as the destination IP address. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both unspecified. |
|---|---|---|---|---|---|
| PricingCycle | String | No | No | The billing cycle of the subscription. | Valid values: Month Year |
| Period | Number | No | No | The subscription period. | Valid values: Valid values when the PricingCycle parameter is set to Month: 1 to 9. Valid values when the PricingCycle parameter is set to Year: 1 to 3. |
| AutoPay | Boolean | No | No | Specifies whether to enable automatic payment. | Default value: true. Valid values: true false |
| InstanceChar geType | String | No | No | The billing method of the router interface. | Valid values: Postpaid: pay-as- you-go Prepaid: subscription |

**Response parameters**

Fn::GetAtt RouterInterfaceId: the ID of the router interface.

**Examples**

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  OppositeInterfaceId:
    Type: String
    Description: The ID of the peer router interface.
  RouterId:
    Type: String
    Description: The router ID to create RouterInterface.
  OppositeRouterId:
    Type: String
    Description: The router ID of the connection peer RouterInterface.
Resources:
  RouterInterface:
    Type: ALIYUN::VPC::RouterInterface
    Properties:
      OppositeInterfaceId:
        Ref: OppositeInterfaceId
      OppositeRouterId:
        Ref: OppositeRouterId
      OppositeInterfaceOwnerId:
        Ref: ALIYUN::TenantId
      OppositeRouterType: VRouter
      Description: Initiating Side
      RouterType: VRouter
      RouterId:
        Ref: RouterId
      Role: InitiatingSide
      Spec: Mini.2
      InstanceChargeType: PostPaid
Outputs:
  RouterInterfaceId:
    Description: The ID of created RouterInterface.
    Value:
      Fn::GetAtt:
        - RouterInterface
        - RouterInterfaceId
```

`JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "OppositeInterfaceId": {
      "Type": "String",
      "Description": "The ID of the peer router interface."
```

`},`

```json
    "RouterId": {
      "Type": "String",
      "Description": "The router ID to create RouterInterface."
```

`},`

```json
    "OppositeRouterId": {
      "Type": "String",
      "Description": "The router ID of the connection peer RouterInterface."
```

`},`

```json
  "Resources": {
    "RouterInterface": {
      "Type": "ALIYUN::VPC::RouterInterface",
      "Properties": {
        "OppositeInterfaceId": {
          "Ref": "OppositeInterfaceId"
```

`},`

```json
        "OppositeRouterId": {
          "Ref": "OppositeRouterId"
```

`},`

```json
        "OppositeInterfaceOwnerId": {
          "Ref": "ALIYUN::TenantId"
```

`},`

```json
        "OppositeRouterType": "VRouter",
        "Description": "Initiating Side",
        "RouterType": "VRouter",
        "RouterId": {
          "Ref": "RouterId"
```

`},`

```json
        "Role": "InitiatingSide",
        "Spec": "Mini.2",
        "InstanceChargeType": "PostPaid"
```

`},`

```json
  "Outputs": {
    "RouterInterfaceId": {
      "Description": "The ID of created RouterInterface.",
      "Value": {
        "Fn::GetAtt": [
          "RouterInterface",
          "RouterInterfaceId"
```

`]`
