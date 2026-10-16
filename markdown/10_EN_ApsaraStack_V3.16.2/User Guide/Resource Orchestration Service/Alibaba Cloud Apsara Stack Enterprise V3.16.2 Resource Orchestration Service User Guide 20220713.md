---
title: "Alibaba Cloud Apsara Stack Enterprise V3.16.2 Resource Orchestration Service User Guide"
product_version: "V3.16.2"
doc_version: "20220713"
pdf_pages: 545
source_pdf: "d2a7be7ab2c1dd01_Alibaba Cloud Apsara Stack Enterprise V3.16.2 Resource Orchestration Service User Guide 20220713.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.16.2%20Resource%20Orchestration%20Service%20User%20Guide%2020220713.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise V3.16.2 Resource Orchestration Service User Guide

## Table of Contents

- 1 What is ROS?
- 2 Log on to the ROS console
- 3 Manage stacks
  - 3.1 Create a stack
  - 3.2 Update a stack
  - 3.3 Recreate a stack
  - 3.4 Delete a stack
- 4 Manage templates
  - 4.1 Create a template
  - 4.2 Edit a template
  - 4.3 Delete a template
- 5 Template syntax
  - 5.1 Template structure
  - 5.2 Overview
  - 5.3 Resources
  - 5.4 Outputs
  - 5.5 Functions
  - 5.6 Mappings
  - 5.7 Conditions
- 6 Resource types
  - 6.1 ECS
    - 6.1.1 ALIYUN::ECS::AutoSnapshotPolicy
    - 6.1.2 ALIYUN::ECS::BandwidthPackage
    - 6.1.3 ALIYUN::ECS::Command
    - 6.1.4 ALIYUN::ECS::CustomImage
    - 6.1.5 ALIYUN::ECS::DedicatedHost
    - 6.1.6 ALIYUN::ECS::Disk
    - 6.1.7 ALIYUN::ECS::DiskAttachment
    - 6.1.8 ALIYUN::ECS::ForwardEntry
    - 6.1.9 ALIYUN::ECS::Instance
    - 6.1.10 ALIYUN::ECS::InstanceClone
    - 6.1.11 ALIYUN::ECS::InstanceGroup
    - 6.1.12 ALIYUN::ECS::InstanceGroupClone
    - 6.1.13 ALIYUN::ECS::Invocation
    - 6.1.14 ALIYUN::ECS::JoinSecurityGroup
    - 6.1.15 ALIYUN::ECS::LaunchTemplate
    - 6.1.16 ALIYUN::ECS::NatGateway
    - 6.1.17 ALIYUN::ECS::NetworkInterface
    - 6.1.18 ALIYUN::ECS::NetworkInterfaceAttachment
    - 6.1.19 ALIYUN::ECS::NetworkInterfacePermission
    - 6.1.20 ALIYUN::ECS::Route
    - 6.1.21 ALIYUN::ECS::SNatEntry
    - 6.1.22 ALIYUN::ECS::SecurityGroup
    - 6.1.23 ALIYUN::ECS::SecurityGroupClone
    - 6.1.24 ALIYUN::ECS::SecurityGroupEgress
    - 6.1.25 ALIYUN::ECS::SecurityGroupIngress
    - 6.1.26 ALIYUN::ECS::Snapshot
    - 6.1.27 ALIYUN::ECS::SSHKeyPair
    - 6.1.28 ALIYUN::ECS::SSHKeyPairAttachment
    - 6.1.29 ALIYUN::ECS::VPC
    - 6.1.30 ALIYUN::ECS::VSwitch
  - 6.2 ESS
    - 6.2.1 ALIYUN::ESS::AlarmTask
    - 6.2.2 ALIYUN::ESS::AlarmTaskEnable
    - 6.2.3 ALIYUN::ESS::LifecycleHook
    - 6.2.4 ALIYUN::ESS::ScalingConfiguration
    - 6.2.5 ALIYUN::ESS::ScalingGroup
    - 6.2.6 ALIYUN::ESS::ScalingGroupEnable
    - 6.2.7 ALIYUN::ESS::ScalingRule
    - 6.2.8 ALIYUN::ESS::ScheduledTask
  - 6.3 NAS
    - 6.3.1 ALIYUN::NAS::AccessGroup
    - 6.3.2 ALIYUN::NAS::AccessRule
    - 6.3.3 ALIYUN::NAS::FileSystem
    - 6.3.4 ALIYUN::NAS::MountTarget
  - 6.4 OSS
    - 6.4.1 ALIYUN::OSS::Bucket
  - 6.5 RDS
    - 6.5.1 ALIYUN::RDS::Account
    - 6.5.2 ALIYUN::RDS::AccountPrivilege
    - 6.5.3 ALIYUN::RDS::DBInstance
    - 6.5.4 ALIYUN::RDS::DBInstanceParameterGroup
    - 6.5.5 ALIYUN::RDS::DBInstanceSecurityIps
    - 6.5.6 ALIYUN::RDS::PrepayDBInstance
  - 6.6 ROS
    - 6.6.1 ALIYUN::ROS::WaitCondition
    - 6.6.2 ALIYUN::ROS::WaitConditionHandle
    - 6.6.3 ALIYUN::ROS::Stack
  - 6.7 SLB
    - 6.7.1 ALIYUN::SLB::AccessControl
    - 6.7.2 ALIYUN::SLB::BackendServerAttachment
    - 6.7.3 ALIYUN::SLB::BackendServerToVServerGroupAddition
    - 6.7.4 ALIYUN::SLB::Certificate
    - 6.7.5 ALIYUN::SLB::DomainExtension
    - 6.7.6 ALIYUN::SLB::Listener
    - 6.7.7 ALIYUN::SLB::LoadBalancer
    - 6.7.8 ALIYUN::SLB::LoadBalancerClone
    - 6.7.9 ALIYUN::SLB::MasterSlaveServerGroup
    - 6.7.10 ALIYUN::SLB::Rule
    - 6.7.11 ALIYUN::SLB::VServerGroup
  - 6.8 SLS
    - 6.8.1 ALIYUN::SLS::Index
    - 6.8.2 ALIYUN::SLS::Logstore
    - 6.8.3 ALIYUN::SLS::LogtailConfig
    - 6.8.4 ALIYUN::SLS::Savedsearch
    - 6.8.5 ALIYUN::SLS::Project
  - 6.9 VPC
    - 6.9.1 ALIYUN::VPC::EIP
    - 6.9.2 ALIYUN::VPC::EIPAssociation
    - 6.9.3 ALIYUN::VPC::PeeringRouterInterfaceBinding
    - 6.9.4 ALIYUN::VPC::PeeringRouterInterfaceConnection
    - 6.9.5 ALIYUN::VPC::RouterInterface

## 1 What is ROS?

Resource Orchestration Service (ROS) is a service provided by Apsara Stack to simplify the management of cloud computing resources. You can author a stack template based on the template specifications defined in ROS. In the template, you can define required cloud computing resources, such as Elastic Compute Service (ECS) and ApsaraDB RDS instances, and the dependencies between resources. The ROS engine automatically creates and configures all resources in a stack based on the template. This helps achieve automatic deployment and O&M. An ROS template is a readable, easy-to-author text file. You can directly edit a JSON template or use version control tools, such as Apache Subversion (SVN) and Git, to manage the template and infrastructure versions. You can call APIs and use SDKs to integrate the orchestration capabilities of ROS with your applications to implement Infrastructure as Code (IaC). An ROS template is a standardized method to deliver resources and applications. If you are an independent software vendor (ISV), you can use ROS templates to deliver a holistic system or solution that encompasses cloud resources and applications. This way, Apsara Stack resources can be integrated with your software systems for centralized delivery. ROS manages a collection of cloud resources in a centralized manner by using a single unit named a stack. A stack is a collection of Apsara Stack resources. You can create, delete, and recreate cloud resources by stack. le

## 2 Log on to the ROS console

This topic describes how to log on to the Resource Orchestration Service (ROS) console. Prerequisites The URL, username, and password of the Apsara Uni-manager Management Console are obtained from the operations administrator before you log on. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter key.
2. Enter the correct username and password.
The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your Apsara Stack tenant account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase and lowercase letters Digits Special characters including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations in the
following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in Apsara Uni-manager Operations Console User Guide.
5. In the top navigation bar, choose Product s > Elast ic Comput ing > Resource Orchest rat ion Service.

## 3 Manage stacks

### 3.1 Create a stack

Resource Orchestration Service (ROS) allows you to create a stack and manage a group of resources in the stack. This topic describes how to create a stack. Method 1: (Recommended) On the Stacks page
1. Log on to the ROS console.
2. In the left-side navigation pane, click St acks.
3. On the St acks page, click Creat e St ack.
4. In the Select T emplat e step, configure Organizat ion, Resource Set , and Region.
5. Select a value for Specify Template Import Method. Enter the content of your template in the Prepare
Template section. Then, click Next . Ent er T emplat e Cont ent : Enter the content of a JSON template in the Prepare T emplat e section. My T emplat es: Select an existing template. For more information about how to create a template, see Create a template.
6. In the Conf igure T emplat e Paramet ers step, configure parameters in the Stacks and Set Parameters
sections. Then, click Next . Not e The parameters that you must configure vary based on the template. Follow on-screen instructions to configure the parameters. You can also click Preview to view the resource name, resource type, and resource properties.
7. In the Conf igure St ack step, configure Rollback on Failure and Timeout Period based on your business
requirements, and click Next .
8. In the Conf irm step, confirm the template and stack configurations, and click Creat e St ack.
After the stack is created, the state of the stack is Creat ed. You can click the ID of the stack to go to the following tabs: Stack Information, Events, Resources, Outputs, Parameters, and Template. Method 2: Use an existing template If you have an existing template, you can perform the following steps to create a stack. For more information about how to create a template, see Create a template.
1. Log on to the ROS console.
2. In the left-side navigation pane, click My T emplat es.
3. On the My T emplat es page, find the template that you want to use and click Creat e in the Act ions
column.
4. In the Select T emplat e step, configure Organizat ion, Resource Set , and Region. Then, click Next .
5. In the Conf igure T emplat e Paramet ers step, configure parameters in the Stacks and Set Parameters
sections. Then, click Next .
6. In the Conf igure St ack step, configure Rollback on Failure and Timeout Period based on your business
requirements, and click Next .
7. In the Conf irm step, confirm the template and stack configurations, and click Creat e St ack.
After the stack is created, the state of the stack is Creat ed. You can click the ID of the stack to go to the following tabs: Stack Information, Events, Resources, Outputs, Parameters, and Template.

### 3.2 Update a stack

You can update a stack if you want to modify only the template that is used to create the stack or the stack configurations. The update operation does not change the organization, resource set, or region of your stack. This topic describes how to update a stack. Prerequisites A stack is in the Creat ed state. For more information, see Create a stack. Procedure
1. Log on to the ROS console.
2. In the left-side navigation pane, click St acks.
3. On the St acks page, find the stack that you want to update and click Updat e in the Act ions column.
4. In the Select T emplat e step, select a value for Specify Template Import Method. Then, click Next .
Ent er T emplat e Cont ent : Enter the content of a JSON template in the Prepare T emplat e section. My T emplat es: Select an existing template.
5. In the Conf igure T emplat e Paramet ers step, modify the parameter settings in the Set Parameter
section. Then, click Next . Not e The parameters that you must configure vary based on the template. Follow on-screen instructions to configure the parameters.
6. In the Conf igure St ack step, set the timeout period and click Next .
7. In the Conf irm step, confirm the template and stack configurations, and click Updat e St ack.

### 3.3 Recreate a stack

You can recreate a stack if you want to change your template, stack configurations, and the organization, resource set, and region of the stack. This topic describes how to recreate a stack. Prerequisites A stack is in the Creat ed state. For more information, see Create a stack. Procedure
1. Log on to the ROS console.
2. In the left-side navigation pane, click St acks.
3. On the St acks page, find the stack that you want to recreate and click Re-creat e in the Act ions
column.
4. In the Select T emplat e step, configure Organizat ion, Resource Set , and Region.
5. Select a value for Specify Template Import Method. Enter the content of your template in the Prepare
Template section. Then, click Next . Ent er T emplat e Cont ent : Enter the content of a JSON template in the Prepare T emplat e section. My T emplat es: Select an existing template.
6. In the Conf igure T emplat e Paramet ers step, modify the parameter settings in the Stacks and Set
Parameters sections. Then, click Next . Not e The parameters that you must configure vary based on the template. Follow on-screen instructions to configure the parameters. The name must be unique in your Apsara Stack tenant account.
7. In the Conf igure St ack step, configure Rollback on Failure and Timeout Period based on your business
requirements, and click Next .
8. In the Conf irm step, confirm the template and stack configurations, and click Creat e St ack.

### 3.4 Delete a stack

You cannot delete a stack that is in the process of an operation such as create or update. Prerequisites A stack is created. For more information, see Create a stack. Procedure
1. Log on to the ROS console.
2. In the left-side navigation pane, click St acks.
3. On the St acks page, find the stack that you want to delete and click Delet e in the Act ions column.
4. In the Delet e St ack dialog box, set the method to delete the stack.
Ret ain Resources: retains the resources in a stack when the stack is deleted. Release Resources: releases the resources in a stack when the stack is deleted. Proceed with caution.
5. Click OK.

## 4 Manage templates

### 4.1 Create a template

You can use Resource Orchestration Service (ROS) to create a JSON template, and then use the template to create a stack. This topic describes how to create a template. Procedure
1. Log on to the ROS console. For more information, see Log on to the ROS console.
2. In the left-side navigation pane, click My T emplat es.
3. On the My T emplat es page, click Creat e T emplat e.
4. In the Creat e T emplat e dialog box, configure T emplat e Name, T emplat e Descript ion,
Organizat ion, Resource Set , and T emplat e Cont ent .
5. Click OK.

### 4.2 Edit a template

You can edit the name, description, and content of a template based on your business requirements. Prerequisites A template is created. For more information, see Create a template. Procedure
1. Log on to the ROS console. For more information, see Log on to the ROS console.
2. In the left-side navigation pane, click My T emplat es.
3. On the My T emplat es page, find the template that you want to edit and click Edit in the Act ions
column.
4. In the Edit T emplat e dialog box, configure T emplat e Name, T emplat e Descript ion, and T emplat e
Cont ent .
5. Click OK.

### 4.3 Delete a template

You can delete templates that you no longer need. Prerequisites A template is created. For more information, see Create a template. Procedure
1. Log on to the ROS console.
2. In the left-side navigation pane, click My T emplat es.
3. On the My T emplat es page, find the template that you want to delete and click Delet e in the Act ions
column.
4. In the Delet e T emplat e message, click Conf irm.

## 5 Template syntax

### 5.1 Template structure

A template is a UTF-8 encoded JSON file that is used to create stacks. Templates serve as the blueprint for underlying infrastructure and architecture. Templates define the configurations of Apsara Stack resources and dependencies between the resources. ROS template structure

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Description" : "The description of the template, which is used to provide information such as
use scenarios and architecture of the template",
  "Metadata" : {
    // The template metadata that provides information such as the layout for visualizations.
  "Parameters" : {
    // The parameters that you can specify when you create a stack.
  "Mappings" : {
    // The mapping tables. Mapping tables are nested tables.
  "Conditions": {
    // The conditions defined by using internal condition functions. These conditions determine w
hen to create associated resources.
  "Resources" : {
    // The detailed information of resources such as configurations and dependencies.
  "Outputs" : {
    // The outputs that are used to provide information such as resource properties. You can use
the Resource Orchestration Service (ROS) console or API to obtain the information.
```

ROSTemplateFormatVersion Required. The template versions supported by ROS. Current version: 2015-09-01. Optional. The description of the template, which is used to provide information such as use scenarios and architecture of the template. A detailed description can help users better understand the content of the template. Metadata Optional. The metadata of the template, in the JSON format. Parameters Optional. The parameters that you can specify when you create a stack. An Elastic Compute Service (ECS) instance type is often defined as a parameter. Parameters have default values. Parameters can improve the flexibility and reusability of the template. When you create a stack, select appropriate specifications. Optional. Mappings are defined as nested mapping tables. You can use Fn::FindInMap to retrieve values corresponding to keys. You can also use parameter values as keys. For example, you can search the regionimage mapping table for desired images by region. Optional. The conditions defined by using Fn::And, Fn::Or, Fn::Not, and Fn::Equals. Multiple conditions are separated by commas (,). The system evaluates all conditions in the template before it creates or updates a stack. All resources associated with `true` conditions are created, and all resources associated with `false` conditions are ignored. Optional. The detailed information of resources in the stack created based on the template. The information includes resource dependencies and configurations. Optional. The outputs that are used to provide information such as resource properties. You can use the ROS console or API to obtain the information.

### 5.2 Overview

The Parameters section improves the flexibility and reusability of a template. When you create a stack, you can replace the parameter values in the template based on your business requirements. Syntax Each parameter consists of a name and several properties. The parameter name can contain only letters and digits and must be unique within the template. You can use the Label field to define the alias of a parameter. The following table describes the parameter properties.

| Property | Required | Description |
|---|---|---|

| Property | Required | Description |   |   |
|---|---|---|---|---|
| Type | Yes | The data type of the parameter. Valid values: String : a string. Example: "ecs.s1.medium" . Number : an integer or a floating-point number. Example: 3.14. CommaDelimitedList: a set of strings that are separated by commas (,). You can use the Fn::Select function to select an element from the string list. Example: "80, foo, bar" . Json : a JSON string. Example: {"foo": "bar"} , [1, 2, 3] . Boolean : a Boolean value. Example: true or false . ALIYUN::OOS::Parameter::Value : a common parameter that is stored in Operation Orchestration Service (OOS) Parameter Store. Example: my image . _ ALIYUN::OOS::SecretParameter::Value : an encryption parameter that is stored in OOS Parameter Store. Example: my _ password . Not e The ALIYUN::OOS::Parameter::Value and ALIYUN::OOS::SecretParameter::Value parameter types cannot be verified by using the AllowedPattern property. |   |   |
|   |   |   | my _ |   |
| Default | No | The default value of the parameter. If you do not specify a value for a parameter when you create a stack, Resource Orchestration Service (ROS) checks whether a default value is defined in the template. If a default value is found, ROS uses the default value. Otherwise, an error is returned. Not e The default value can be set to null , which indicates that this parameter is left empty, and parameter verification is skipped. |   |   |
| AllowedValues | No | The list of valid parameter values. |   |   |
| AllowedPattern | No | The regular expression that is used to check whether the specified parameter value is a string. If the input is not a string, an error is returned. If you use the following special characters, add two backslashes (\\) immediately before the characters that you want to escape: *.?+-$^[ ]( ){ }\|\/ Not e A hyphen (-) that is used as the first or last character in the range does not need to be escaped. Example: [a-z-]. |   |   |

|   | 3] |
|---|---|

|   | password |
|---|---|

| Property | Required | Description |
|---|---|---|
| MaxLength | No | The integer value that determines the maximum length of String- type parameters. |
| MinLength | No | The integer value that determines the minimum length of String- type parameters. |
| MaxValue | No | The numeric value that determines the maximum value that is allowed for a Number-type parameter. |
| MinValue | No | The numeric value that determines the minimum value that is allowed for a Number-type parameter. |
| NoEcho | No | Specifies whether to mask the parameter value when the GetStack operation is called. If you set this parameter property to true , only asterisks (*) are returned. |
| Description | No | The string that describes the parameter. |
| ConstraintDescriptio n | No | The string that explains the constraint of the parameter. |
| Label | No | The alias of the parameter. The alias is encoded in UTF-8. When you create a web form based on a template, the value of the label field can be mapped to the parameter name. |
| AssociationProperty | No | The associated resource property. If you specify this parameter property, ROS verifies whether the specified parameter value is valid and provides a list of valid values based on the associated resource property. For more information about the values of AssociationProperty that are supported by ROS and examples, see . |
| AssociationProperty Metadata | No | The metadata map that explains the constraint of AssociationProperty. This property is of the Map type. For more information about the values of AssociationPropertyMetadata that correspond to the values of AssociationProperty and examples, see AssociationProperty and AssociationPropertyMetadata. |
| Confirm | No | Specifies whether to enter the parameter value for a second time if NoEcho is set to true . Default value: false . Not e Confirm can be set to true only if it is used with a String-type parameter and NoEcho is set to true . |

| Property | Required | Description |
|---|---|---|
| TextArea | No | Specifies whether the parameter supports line breaks. Default value: false. Valid values: true : The parameter supports line breaks. false : The parameter does not support line breaks. In the following example, the Content parameter supports line breaks. { "ROSTemplateFormatVersion": "2015-09-01", "Parameters": { "Content": { "Type": "String", "TextArea": true } }, "Outputs": { "TestContent": { "Value": { "Ref": "Content" } } } } |

Example: Create a stack in a web application For example, you want to create a stack in a web application, and the stack needs to contain one Server Load Balancer (SLB) instance, two Elastic Compute Service (ECS) instances, and one ApsaraDB RDS instance. If the web application is under heavy workload, you can select an ECS instance that has advanced specifications when you create the stack. Otherwise, you can select an ECS instance that has basic specifications. The following example shows how to specify the InstanceType parameter for an ECS instance:

```json
"Parameters" : {
  "InstanceType" : {
    "Type" : "String",
    "AllowedValues":["ecs.t1.small","ecs.s1.medium", "ecs.m1.medium", "ecs.c1.large"],
    "Default": "ecs.t1.small",
    "Label": "ECS instance type",
    "Description" : "The type of the ECS instance that you want to create. Default value: ecs.t1.
small. Valid values: ecs.t1.small, ecs.s1.medium, ecs.m1.medium, and ecs.c1.large."
```

You can specify the InstanceType parameter each time you create a stack based on the template. If you do not specify a value for the parameter, the default value `ecs.t1.small` is used. The following example shows how to reference the InstanceType parameter when you define a resource:

```json
"Webserver" : {
  "Type" : "ALIYUN::ECS::Instance",
  "InstanceType": {
    "Ref": "InstanceType"
```

### 5.3 Resources

This topic describes the properties of each resource and dependencies between resources in a stack. A resource can be referenced by other resources and output items. Syntax Each resource consists of an ID and a description. All resource descriptions are enclosed in braces {}. Multiple resources are separated by commas (,). The following sample code shows the Resources syntax:

```json
"Resources" : {
    "Resource1 ID" : {
        "Type" : "The resource type",
        "Condition": "The condition that specifies whether to create the resource",
        "Properties" : {
            The description of the resource properties
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

DeletionPolicy The DeletionPolicy parameter specifies whether to retain a resource when its stack is deleted. The following sample code shows how to use the DeletionPolicy parameter to retain an ECS instance when its stack is deleted:

```json
"Resources" : {
  "ECSInstance" : {
    "Type" : "ALIYUN::ECS::Instance",
    "Properties" : {
      "ImageId" : "m-25l0r****"
    "DeletionPolicy" : "Retain"
```

DependsOn The DependsOn parameter allows you to create a specific resource after you create its dependent resource. If you specify the DependsOn parameter for a resource, the resource is created only after its dependent resource specified by the DependsOn parameter is created. In the following example, WebServer is created only after DatabaseServer is created:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "DependsOn": "DatabseServer"
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
```

Condition The Condition parameter specifies whether to create the resource. The resource can be created only when the Condition parameter is set to true. In the following example, WebServer is created only if the condition determined by the MaxAmount parameter is true:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Parameters": {
    "MaxAmount": {
      "Type": "Number",
      "Default": 1
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
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
```

Resource declaration example The following example shows how to declare a resource:

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

`]`

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
                "Category": "cloud",
                "Size": 10
```

`]`

### 5.4 Outputs

The Outputs section is used to define the values returned when the GetStack operation is called. For example, if you define an Elastic Compute Service (ECS) instance ID as an output item, the ECS instance ID is returned when the GetStack operation is called. Syntax Each output item consists of an ID and a description. All output descriptions are enclosed in braces {}. Multiple output items are separated by commas (,). Each output item can have multiple values in an array format. The following example shows the Outputs syntax:

```json
"Outputs" : {
  "Output1 ID" : {
    "Description": "The description of the output item",
    "Condition": "The condition that specifies whether to provide resource properties",
    "Value": "The output value expression"
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

Examples The following example contains two output items: The InstanceId value of WebServer The PublicIp and PrivateIp values of WebServer

```json
"Outputs": {
  "InstanceId": {
    "Value" : {"Fn::GetAtt": ["WebServer", "InstanceId"]}
  "PublicIp & PrivateIp": {
    "Value" : [
      {"Fn::GetAtt": ["WebServer", "PublicIp"]},
      {"Fn::GetAtt": ["WebServer", "PrivateIp"]}
```

`]`

### 5.5 Functions

Resource Orchestration Service (ROS) provides several built-in functions to help you manage stacks. You can use built-in functions to define Resources and Outputs. Fn::Base64Encode The Fn::Base64Encode function is used to return the Base64 representation of the input string. Declaration

```
"Fn::Base64Encode": "stringToEncode"
```

Parameters `stringToEncode` : the string to be encoded in Base64. Return value The Base64 representation of the input string. Examples

```json
{"Fn::Base64Encode": "string to encode"}
```

`c3RyaW5nIHRvIGVuY29kZQ==` is returned in this example. Fn::Base64Decode The Fn::Base64Decode function is used to return a string decoded from a Base64-encoded string. Declaration

```json
{"Fn::Base64Decode": "stringToEncode"}
```

Parameters `stringToDecode` : the string decoded from the Base64-encoded string. Return value The string decoded from the Base64-encoded string. Examples

```json
{"Fn::Base64Decode": "c3RyaW5nIHRvIGVuY29kZQ=="}
```

`string to encode` is returned in this example. Fn::Base64 The Fn::Base64 function returns the Base64 representation of the input string. Declaration

```
 "Fn::Base64": stringToEncode
```

Parameters valueToEncode: the string to be encoded in Base64. Return value The Base64 representation of the input string. Examples

```
 "Fn::Base64":"string to encode"
```

Fn::FindInMap The Fn::FindInMap function is used to return the values based on keys in a two-level mapping that is declared in the Mappings section. Declaration

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

`]`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
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

`]`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "key1",
            "Value": "value1"
            "Key": "key2",
            "Value": "value2"
```

`]` Supported functions Fn::FindInMap Ref Fn::GetAtt The Fn::GetAtt function is used to return the value of a property from a resource in a template. Declaration

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

Fn::Join The Fn::Join function is used to combine a set of values into a single value that is separated by a specified delimiter. Declaration

```json
{"Fn::Join": ["delimiter", ["string1", "string2", ... ]]}
```

Parameters `delimiter` : the value used to divide the string. The delimiter value can be left blank so that all the values are directly combined. `[ "string1", "string2", ... ]` : the list of values that are combined into a string. Return value The combined string. Examples

```json
{"Fn::Join": [ ",", ["a", "b", "c"]]}
```

`"a,b,c"` is returned in this example. Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Select The Fn::Select function is used to return a single data element from a list of data elements by using an index. Declaration The following example assumes that the list of data elements is an array:

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

Supported functions For the Fn::Select index value, you can use the Ref function. For the Fn::Select list of data elements, you can use the following functions: Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref Ref The Ref function is used to return the value of a specified parameter or resource. If the specified parameter is a resource ID, the value of the resource is returned. Otherwise, the system returns the value of the specified parameter. Declaration

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

`]`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
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

`]`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "tiantt",
            "Value": "ros"
            "Key": "tiantt1",
            "Value": "ros1"
```

`]` Supported function When you use the Ref function, you cannot use other functions in it at the same time. You must specify a string value for the logical ID of a resource. Fn::GetAZs The Fn::GetAZs function is used to return a list of zones for a specified region. Declaration

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
  "Outputs": {
    "InstanceId": {
         "Value": {"Fn::GetAtt": ["WebServer","InstanceId"]}
    "PublicIp": {
         "Value": {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref Fn::Replace The Fn::Replace function is used to replace a specified substring contained in a string with a new substring. Declaration

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
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Split The Fn::Split function is used to split a string into a list of values separated by a specified delimiter and return the list. Declaration

```
"Fn::Split": ["delim", "original_string"]
```

Parameters

| delim | : the specif |
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
  "Resources": {
    "resourceID": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Fn::Split": [
            ",",
              "Ref": "InstanceIds"
```

`]` Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Fn::Replace Fn::GetAZs Fn::If Ref Fn::Equals The Fn::Equals function is used to compare whether two values are equal. If the two values are equal, true is returned. If the two values are not equal, false is returned. Declaration

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
  "Conditions": {
    "TestEqualsCond": {
      "Fn::Equals": [
        "prod",
        {"Ref": "EnvType"}
```

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::And The Fn::And function is used to represent the AND operator, and must contain at least two conditions. If all the specified conditions are evaluated as true, true is returned. If any condition is evaluated as false, false is returned. Declaration

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
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestAndCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::Or The Fn::Or function is used to represent the OR operator, and must contain at least two conditions. If any specified condition is evaluated as true, true is returned. If all the conditions are evaluated as false, false is returned. Declaration

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
  "Conditions": {
    "TestEqualsCond": {"Fn::Equals": ["prod", {"Ref": "EnvType"}]},
    "TestOrCond": {"Fn::And": ["TestEqualsCond", {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}]}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::Not The Fn::Not function is used to represent the NOT operator. If a condition is evaluated as false, true is returned. If a condition is evaluated as true, false is returned. Declaration

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
  "Conditions": {
    "TestNotCond": {"Fn::Not": {"Fn::Equals": ["pre", {"Ref": "EnvType"}]}}
```

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::If This function returns one of two possible values. If a specified condition is evaluated as true, one value is returned. If the specified condition is evaluated as false, the other value is returned. The property values of Resources and Outputs in templates support the Fn::If function. You can use the `ALIYUN::NoValue` pseudo parameter as the return value to delete the corresponding property. Declaration

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
    "Conditions":{
        "CreateDisk":{
            "Fn::Equals":[
                "prod",
                    "Ref":"EnvType"
```

`]`

```json
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
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
                                "Category":"cloud_ssd",
                                "DiskName":"SecondDataDiskName",
                                "Size":40
```

`],`

```json
                            "Ref":"ALIYUN::NoValue"
```

`]`

```json
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

`]`

```json
        "ZoneId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "ZoneId"
```

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::ListMerge The Fn::ListMerge function is used to merge multiple lists into one list. Declaration

```json
{"Fn::ListMerge": [["list_1_item_1", "list_1_imte_2", ...], ["list_2_item_1", "list_2_imte_2", ...]]}
```

Parameters `["list_1_item_1", "list_1_imte_2", ...]` : the first list to merge. `["list_2_item_1", "list_2_imte_2", ...]` : the second list to merge into the first list. Examples The following example demonstrates how to attach two ECS instance groups to a Server Load Balancer (SLB) instance:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "ros",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
    "BackendServer1": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3****",
        "MaxAmount": 1,
        "MinAmount": 1
    "BackendServer2": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "ImageId" : "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3iu****",
        "MaxAmount": 1,
        "MinAmount": 1
    "Attachment": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "LoadBalancerId": {"Ref": "LoadBalancer"},
        "BackendServerList": { "Fn::ListMerge": [
            {"Fn::GetAtt": ["BackendServer1", "InstanceIds"]},
            {"Fn::GetAtt": ["BackendServer2", "InstanceIds"]}
```

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If Fn::GetJsonValue The Fn::GetJsonValue function is used to resolve a JSON string and obtain its key value from the first layer. Declaration

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
    "WaitConHandle": {
        "Type": "ALIYUN::ROS::WaitConditionHandle"
    "WaitCondition": {
        "Type": "ALIYUN::ROS::WaitCondition",
        "Properties": {
          "Handle": {"Ref": "WaitConHandle"},
          "Timeout": 900
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
  "Outputs": {
    "InstanceId": {
         "Value" : {"Fn::GetAtt": ["WebServer","InstanceId"]}
    "PublicIp": {
         "Value" : {"Fn::GetAtt": ["WebServer","PublicIp"]}
```

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If Fn::MergeMapToList The Fn::MergeMapToList function is used to merge multiple mappings into a list of mapping elements. Declaration

```json
{"Fn::MergeMapToList": [{"key_1": ["key_1_item_1", "key_1_item_2", ...]}, {"key_2":["key_2_item _1", "key_2_item_2", ...]}, ... ]}
```

Parameters `{"key_1": ["key_1_item_1", "key_1_item_2", ...]}` : the first mapping to merge. The `"key_1"` value must be a list. `"key_1"` is the key for each mapping in the list of merged mappings. The "key_1" value is `"key_1_item_1"` for the first merged mapping and `"key_1_item_2"` for the second merged mapping. All values follow the same format. The length of the final list of merged mappings is the length of the longest list `"key_x"` from all mappings being merged. If a `"key_y"` list is shorter, the last element of the list is repeated until the list is the longest. `{"key_2": ["key_2_item_1", "key_2_item_2", ...]}` : the second mapping to merge into the first mapping. The `"key_2"` value must be a list. `"key_2"` is the key for each mapping in the merged list. The "key_2" value is `"key_2_item_1"` for the first merged mapping and `"key_2_item_2"` for the second merged mapping. All values follow the same format. Examples The following example demonstrates how to merge three mappings. The length of the list based on the key values for each mapping is the same.

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
      "key_1": "kye_1_item_2",
      "key_2": "kye_2_item_2",
      "key_3": "kye_3_item_2"
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

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::If Fn::ListMerge Fn::GetJsonValue Fn::Avg The Fn::Avg function is used to return the average value of a set of numbers. Declaration

```json
{"Fn::Avg": [ndigits, [number1, number2, ... ]]}
```

Parameters

| ndigits | : the number of dec |
|---|---|
| [ number1, number2, ... ] |   |

`ndigits` : the number of decimal places to display. This parameter value must be an integer. `[ number1, number2, ... ]` : the set of numbers for which the average value will be calculated. Each element in the group must be a number or a string that can be converted into a number. Return value The average value of the set of numbers. Examples

```json
{ "Fn::Avg": [ 1, [1, 2, 6.0] ] } { "Fn::Avg": [ 1, ['1', '2', '6.0'] ] }
```

3.0 is returned in this example. Supported functions Fn::GetAtt Ref Fn::SelectMapList The Fn::SelectMapList function is used to return a list of map elements. Declaration

```json
{"Fn::SelectMapList": ["key2", [{"key1": "value1-1", "key3": "value1-3"}, {"key1": "value2-1", "key2": "value2-2"}, {"key1": "value3-1", "key2": "value3-2"}, ...] ] }
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

`]` `]` `["value2-2","value3-2"]` is returned in this example. Fn::Add The Fn::Add function is used to sum the values of parameters. Declaration

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

### 5.6 Mappings

The Mappings section is a key-value mapping table. When mappings are used in resource and output definitions, use Fn::FindInMap to find their values by specifying corresponding keys. Syntax A mapping consists of key-value pairs, where both the keys and values can be strings or numbers. Multiple mappings are separated by commas (,). Each mapping name must be unique. Mappings must be pure data and cannot parse functions. Examples The following example shows a correct mapping definition:

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

`]`

```json
  "Mappings": {
    "RegionMap": {
      "hangzhou": {
        "32": "m-25l0rcfjo",
        "64": "m-25l0rcfj1"
      "beijing": {
        "32": "m-25l0rcfj2",
        "64": "m-25l0rcfj3"
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
      "Properties": {
        "ImageId": {
          "Fn::FindInMap": [
            "RegionMap",
              "Ref": "regionParam"
            "32"
```

`]`

```json
        "InstanceType": "ecs.t1.small",
        "SecurityGroupId": "sg-25zwc****",
        "ZoneId": "cn-beijing-b",
        "Tags": [
            "Key": "Department1",
            "Value": "HumanResource"
            "Key": "Department2",
            "Value": "Finance"
```

`]`

### 5.7 Conditions

Condition bodies are defined by Fn::And, Fn::Or, Fn::Not, and Fn::Equals operators. These operators, along with the parameters that you specify when you create or update a stack, are used to evaluate each condition. You can reference other conditions, parameters, and mappings in your condition. Conditions are used in resource and output definitions to establish dependencies. Use Fn::If or Condition in resource and output definitions to implement conditions. Syntax Each condition consists of a condition name and a condition body. The condition name is a string. The condition body starts with Fn::And, Fn::Or, Fn::Not, or Fn::Equals. You can reference other conditions in your condition. Separate multiple conditions with comma (,). Each condition name must be unique. The following functions can be used, but not as the outermost functions: "Fn::Select", "Fn::Join", "Fn::Split", "Fn::Replace","Fn::Base64Encode", "Fn::Base64Decode", "Fn::MemberListToMap","Fn::If", "Fn::ListMerge", "Fn::GetJsonValue", "Fn::MergeMapToList","Fn::SelectMapList", "Fn::Add", "Fn::Avg", "Fn::Str", "Fn::Calculate","Ref"(parameter references only), and "Fn:: FindInMap". Examples The following example shows how to define conditions:

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
    "Conditions":{
        "CreateProdRes":{
            "Fn::Equals":[
                "prod",
                    "Ref":"EnvType"
```

`]`

```json
    "Resources":{
        "WebServer":{
            "Type":"ALIYUN::ECS::Instance",
            "Properties":{
```

```json
            Properties:{
                "DiskMappings":{
                    "Fn::If":[
                        "CreateProdRes",
```

`[`

```json
                                "Category":"cloud_efficiency",
                                "DiskName":"FirstDataDiskName",
                                "Size":40
                                "Category":"cloud_ssd",
                                "DiskName":"SecondDataDiskName",
                                "Size":40
```

`],`

```json
                            "Ref":"ALIYUN::NoValue"
```

`]`

```json
                "VpcId":"vpc-2zew9pxh2yirtzqxd****",
                "SystemDiskCategory":"cloud_efficiency",
                "SecurityGroupId":"sg-2zece6wcqriejf1v****",
                "SystemDiskSize":40,
                "ImageId":"centos_6_8_64_40G_base_2017****.vhd",
                "IoOptimized":"optimized",
                "VSwitchId":"vsw-2zed9txvy7h2srqo6****",
                "InstanceType":"ecs.n1.medium"
        "OssBucket": {
            "Type": "ALIYUN::OSS::Bucket",
            "Condition": "CreateProdRes",
            "Properties": {
                "AccessControl": "private",
                "BucketName": "myprodbucket"
    "Outputs":{
        "InstanceId":{
            "Value":{
                "Fn::GetAtt":[
                    "WebServer",
                    "InstanceId"
```

`]`

```json
        "OssDomain":{
            "Condition": "CreateProdRes",
            "Value":{
                "Fn::GetAtt":[
                    "OssBucket",
                    "DomainName"
```

`]`

## 6 Resource types

### 6.1 ECS

#### 6.1.1 ALIYUN::ECS::AutoSnapshotPolicy

ALIYUN::ECS::AutoSnapshotPolicy is used to create an automatic snapshot policy. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TimePoints | List | Yes | Yes | The points in time of a day at which to create automatic snapshots. | Valid values: 0 to 23. The values from 0 to 23 indicate the 24 points in time on the hour from 00:00 to 23:00. For example, 1 indicates 01:00. Unit: hours. If you need automatic snapshots to be created at several times in a day, you can specify multiple hours. You can specify up to 24 hours. You must set this property to a list. Example: [0, 1, ... 23]. Separate multiple hours with commas (,). |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RepeatWeek days | List | Yes | Yes | The days of a week on which to create automatic snapshots. | Valid values: 1 to 7. The values from 1 to 7 indicate the seven days in a week from Monday to Sunday. Cycle: week. If you need automatic snapshots to be created at several times in a week, you can specify multiple days. You must set this property to a list. Example: [1, 2, ... 7]. Separate multiple days with commas (,). You can specify up to seven days. |
| RetentionDay s | Integer | Yes | Yes | The number of days for which the system retains automatic snapshots. | Default value: -1. Valid values: -1: permanently retains automatic snapshots. 1 to 65535: retains automatic snapshots based on the number of days that you specify. Unit: days. |
| DiskIds | List | No | Yes | The IDs of disks to which you want to apply the automatic snapshot policy. | If you need to apply the automatic snapshot policy to multiple disks, you must set this property to a list in the ["d-xxxxxxxxx", "d-yyyyyyyyy", … "d-zzzzzzzzz"] format. Separate multiple IDs with commas (,). |
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the automatic snapshot policy belongs. | None |
| Tags | List | No | Yes | The tags of the automatic snapshot policy. | You can add up to 20 tags. For more information, see Tags properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AutoSnapsh otPolicyNam e | String | No | Yes | The name of the automatic snapshot policy. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . By default, this property is empty. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The tag value can be up to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with aliyun or acs: . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return value Fn::GetAtt AutoSnapshotPolicyId: the ID of the automatic snapshot policy. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "TimePoints": {
      "Type": "CommaDelimitedList",
```

`"D`

```
iti
```

`"`

```
"Th
```

`t` `ti` `h``t` `ti`

```
hdl dth
```

`it` `f` `t``i` `h`

```json
      "Description": "The automatic snapshot creation schedule, and the unit of measurement is ho
ur. Value range: [0, 23], which represents from 00:00 to 24:00, for example 1 indicates 01:00. Wh en you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the Ti mePoints to an array.\nA maximum of 24 time points can be selected.\nThe format is a list of [0, 1, ..., 23] and the time points are separated by commas (,)."
    "DiskIds": {
      "Type": "Json",
      "Description": "The disk ID. When you want to apply the automatic snapshot policy to multip
le disks, you can set the DiskIds to an array. The format is list of [\"d-xxxxxxxxx\", \"d-yyyyyy yyy\", ..., \"d-zzzzzzzzz\"] and the IDs are separated by commas (,)."
    "RetentionDays": {
      "Type": "Number",
      "Description": "The snapshot retention time, and the unit of measurement is day. Optional v
alues:\n-1: The automatic snapshots are retained permanently.\n[1, 65536]: The number of days ret ained.\nDefault value: -1.",
      "MinValue": -1,
      "MaxValue": 65536
    "RepeatWeekdays": {
      "Type": "Json",
      "Description": "The automatic snapshot repetition dates. The unit of measurement is day and
the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1 indicates Monday. When you want to schedule multiple automatic snapshot tas ks for a disk in a week, you can set the RepeatWeekdays to an array.\nA maximum of seven time poi nts can be selected.\nThe format is a list of [1, 2, ..., 7] and the time points are separated by commas (,)."
    "AutoSnapshotPolicyName": {
      "Type": "String",
      "Description": "The name of the automatic snapshot policy.\nIt can consist of [2, 128] Engl
ish or Chinese characters.\nMust begin with an uppercase or lowercase letter or a Chinese charact er. Can contain numbers, periods (.), colons (:), underscores (_), and hyphens (-).\nCannot start with http:// or https://.\nDefault value: null."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
  "Resources": {
    "AutoSnapshotPolicy": {
      "Type": "ALIYUN::ECS::AutoSnapshotPolicy",
      "Properties": {
        "TimePoints": {
          "Ref": "TimePoints"
        "DiskIds": {
          "Ref": "DiskIds"
        "RetentionDays": {
          "Ref": "RetentionDays"
        "RepeatWeekdays": {
"Ref":"RepeatWeekdays"
```

```json
          Ref: RepeatWeekdays
        "AutoSnapshotPolicyName": {
          "Ref": "AutoSnapshotPolicyName"
        "Tags": {
          "Ref": "Tags"
  "Outputs": {
    "AutoSnapshotPolicyId": {
      "Description": "The automatic snapshot policy ID.",
      "Value": {
        "Fn::GetAtt": [
          "AutoSnapshotPolicy",
          "AutoSnapshotPolicyId"
```

`]` `YAML` format

```json
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AutoSnapshotPolicyName:
    Description: 'The name of the automatic snapshot policy.
      It can consist of [2, 128] English or Chinese characters.
      Must begin with an uppercase or lowercase letter or a Chinese character. Can
      contain numbers, periods (.), colons (:), underscores (_), and hyphens (-).
      Cannot start with http:// or https://.
      Default value: null.'
    Type: String
  DiskIds:
    Description: The disk ID. When you want to apply the automatic snapshot policy
      to multiple disks, you can set the DiskIds to an array. The format is list of
      ["d-xxxxxxxxx", "d-yyyyyyyyy", ..., "d-zzzzzzzzz"] and the IDs are separated
      by commas (,).
    Type: Json
  RepeatWeekdays:
    Description: 'The automatic snapshot repetition dates. The unit of measurement
      is day and the repeating cycle is a week. Value range: [1, 7], which represents
      days starting from Monday to Sunday, for example 1 indicates Monday. When you
      want to schedule multiple automatic snapshot tasks for a disk in a week, you
      can set the RepeatWeekdays to an array.
      A maximum of seven time points can be selected.
      The format is a list of [1, 2, ..., 7] and the time points are separated by
      commas (,).'
    Type: Json
  RetentionDays:
    Description: 'The snapshot retention time, and the unit of measurement is day.
      Optional values:
      -1: The automatic snapshots are retained permanently.
      [1, 65536]: The number of days retained.
```

`D``f` `lt` `l` `1``'`

```
      Default value: -1.'
    MaxValue: 65536
    MinValue: -1
    Type: Number
  Tags:
    Description: Tags to attach to instance. Max support 20 tags to add during create
      instance. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
  TimePoints:
    Description: 'The automatic snapshot creation schedule, and the unit of measurement
      is hour. Value range: [0, 23], which represents from 00:00 to 24:00, for example
      1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks
      for a disk in a day, you can set the TimePoints to an array.
      A maximum of 24 time points can be selected.
      The format is a list of [0, 1, ..., 23] and the time points are separated by
      commas (,).'
    Type: CommaDelimitedList
Resources:
  AutoSnapshotPolicy:
    Properties:
      AutoSnapshotPolicyName:
        Ref: AutoSnapshotPolicyName
      DiskIds:
        Ref: DiskIds
      RepeatWeekdays:
        Ref: RepeatWeekdays
      RetentionDays:
        Ref: RetentionDays
      Tags:
        Ref: Tags
      TimePoints:
        Ref: TimePoints
    Type: ALIYUN::ECS::AutoSnapshotPolicy
Outputs:
  AutoSnapshotPolicyId:
    Description: The automatic snapshot policy ID.
    Value:
      Fn::GetAtt:
      - AutoSnapshotPolicy
      - AutoSnapshotPolicyId
```

For more examples, visit AutoSnapshotPolicy.json and AutoSnapshotPolicy.yml.

#### 6.1.2 ALIYUN::ECS::BandwidthPackage

ALIYUN::ECS::BandwidthPackage is used to create a service plan for a NAT gateway. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NatGatewayId | String | Yes | No | The ID of the NAT gateway to which you want to bind the service plan. | None |
| Bandwidth | Integer | Yes | No | The bandwidth. | Valid values: 5 to 5000. Unit: Mbit/s. Default value: 5. |
| IpCount | Integer | Yes | No | The number of public IP addresses assigned to the NAT gateway. | Valid values: 1 to 5. |
| Description | String | No | No | The description of the service plan. | The description must be 2 to 256 characters in length. |
| ZoneId | String | No | No | The ID of the zone where the NAT gateway resides. | None |
| BandwidthPac kageName | String | No | No | The name of the service plan. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter. |

Response parameters Fn::GetAtt BandwidthPackageId: the ID of the service plan. BandwidthPackageIps: all IP addresses included in the service plan. Examples

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
  "Outputs": {
    "BandwidthPackageId": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageId"]}
    "BandwidthPackageIps": {
         "Value": {"Fn::GetAttr": ["BandwidthPackage","BandwidthPackageIps"]}
```

#### 6.1.3 ALIYUN::ECS::Command

ALIYUN::ECS::Command is used to create a Cloud Assistant command. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | True | The name of the command, which supports all character sets. The name can be up to 30 characters in length. | None |
| WorkingDir | String | Yes | True | The working directory on the ECS instance where the command will be run. | None |
| CommandContent | String | Yes | Released | The Base64-encoded content of the command. When you specify request parameters Type you must also specify this parameter. The parameter value must be Base64-encoded and cannot exceed 16 KB in size after encoding. | None |
| Timeout | String | No. | True | The timeout period that is specified for the command to run on ECS instances. Unit: seconds. If the command fails to run within the specified period, the command execution will time out and the process will be forcibly terminated. Default value: 3600. | None |
| Type | String | No | No | The command type. Valid values: RunBatScript: Creates a Bat script for a Windows instance. RunPowerShellScript: Create a PowerShell script to run on a Windows instance. RunShellScript: Creates a Shell script for Linux- based instances. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | True | The description of the command, which supports all character sets. The description can be up to 100 characters in length. | None |

Response parameters Fn::GetAtt CommandId: the ID of the command. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "WorkingDir": {
      "Type": "String",
      "Description": "The path where command will be executed in the instance."
    "CommandContent": {
      "Type": "String",
      "Description": "The content of command. Content requires base64 encoding. Maximum size supp
ort 16KB."
    "Type": {
      "Type": "String",
      "Description": "The type of command."
    "Description": {
      "Type": "String",
      "Description": "The description of command."
    "Timeout": {
      "Type": "Number",
      "Description": "Total timeout when the command is executed in the instance. Input the time
unit as second. Default is 3600s."
    "Name": {
      "Type": "String",
      "Description": "The name of command."
  "Resources": {
    "Command": {
      "Type": "ALIYUN::ECS::Command",
      "Properties": {
        "WorkingDir": {
          "Ref": "WorkingDir"
        "CommandContent": {
          "Ref": "CommandContent"
        "Type": {
"Ref" "Tpe"
```

```json
          "Ref": "Type"
        "Description": {
          "Ref": "Description"
        "Timeout": {
          "Ref": "Timeout"
        "Name": {
          "Ref": "Name"
  "Outputs": {
    "CommandId": {
      "Description": "The id of command created.",
      "Value": {
        "Fn::GetAtt": [
          "Command",
          "CommandId"
```

`]`

#### 6.1.4 ALIYUN::ECS::CustomImage

ALIYUN::ECS::CustomImage is used to create a custom image. Statement

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

Properties

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the image. | The description can be up to 256 characters in length. This parameter is empty by default. It cannot start with http:// or https://. |
| InstanceId | String | Yes | Released | The ID of the ECS instance. | If this parameter is specified, an ECS instance will be used to create the custom image. |
| ImageName | String | Yes | Released | The name of the image. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ and hyphens(-). It must start with a letter but cannot start with http:// or https://. |
| ImageVersion | String | Yes | Released | The image version. | The image version must be 1 to 40 characters in length. |
| SnapshotId | String | Yes | Released | The ID of the snapshot. | If this parameter is specified, a snapshot will be used to create the custom image. If both this parameter and the InstanceId parameter are specified, this parameter will be ignored and an instance will be used to create the custom image. |
| Tags | List | Erased | Released | The tags of the image. | None |
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the custom image belongs. | None |

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Platform | String | Yes | Released | If you specify a data disk snapshot to be used to create the system disk of the custom image, you must use the Platform parameter to determine the release version of the operating system for the system disk. | None |
| DiskDeviceMappin g | List | Erased | Released | The mappings between images and snapshots. | None |
| Architecture | String | Yes | Released | If you specify a data disk snapshot to be used to create the system disk of the custom image, you must use the Architecture parameter to determine the architecture of the system disk. Default value: x86 64. _ | Valid values: i386 x86 64 _ |

Tag syntax

```json
"Tag": [
    "Key": String,
    "Value": String
```

`]` Tag properties

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | Released | The tag key of the image. | The tag key cannot be a null string. The key can be up to 64 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://. |
| Value | String | Yes | Released | The tag value of the image. | The tag value can be an empty string. The value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://. |

DiskDeviceMapping

```json
"DiskDeviceMapping": [
    "Device": String,
    "SnapshotId": String,
    "Size": Integer,
    "DiskType": String
```

`]` DiskDeviceMapping properties

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Device | String | Yes | Released | The device name of disk N in the custom image. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot that is used to create the custom image. | None |

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | Optional | Released | The size of disk N. Unit: GiB. | Valid values: 5 to 2000. The default value is the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. If the DiskDeviceMapping.N.S napshotId parameter is not specified, the default disk size is 5 GiB. The disk size must be greater than or equal to the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. |
| DiskType | String | Yes | Released | The type of disk N in the custom image. You can specify this parameter to create the system disk of the custom image from a data disk snapshot. If you do not specify this parameter, the disk type is determined by the corresponding snapshot. | Valid values: system: indicates a system disk. data: indicates a data disk. |

Response parameters Fn::GetAtt ImageId: the ID of the custom image. Sample request

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
        "IoOptimized": "optimized",
        "SystemDisk_Description": "SystemDisk.Description",
        "SystemDisk_DiskName": "SystemDisk.DiskName",
        "SystemDisk_Category": "cloud_ssd",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "Password": "Wenqiao****",
        "InstanceType": "ecs.n1.medium",
        "MaxAmount": 1
    "CustomImage": {
      "Type": "ALIYUN::ECS::CustomImage",
      "Properties": {
        "InstanceId": "i-2zefq1f3ynnrr89q****",
        "SnapshotId": "s-2ze0ibk1pvak4mw6****",
        "ImageName": "image-test-****",
        "ImageVersion": "verison-6-1"
  "Outputs": {
    "CustomImage": {
      "Value": {
        "Fn::GetAtt": [
          "CustomImage",
          "ImageId"
```

`]`

```json
    "InstanceIds": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceIds"
```

`]`

#### 6.1.5 ALIYUN::ECS::DedicatedHost

ALIYUN::ECS::DedicatedHost is used to create a dedicated host. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DedicatedHo stType | String | No | No | The dedicated host type. | None |
| DedicatedHo stName | String | Yes | Released | The name of the dedicated host. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), _ and hyphens (-). Must start with an uppercase or lowercase letter, and cannot start with http:// or https:// the beginning. It can contain digits, colons (:), underscores ( ), _ and hyphens (-). |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AutoRelease Time | String | Yes | Released | The time scheduled for the dedicated host to be automatically released. If you do not specify the AutoReleaseTime parameter, the dedicated host will not be automatically released. The minimum release time must be at least 30 minutes after the current time. The maximum release time must be at most three years from the current time. If the value of ss is not 00 , the start time is automatically rounded down to the nearest minute based on the value of mm . | None |
| Description | String | Yes | Released | The description of the dedicated host. | None |
| ZoneId | String | Yes | Released | The ID of the zone where the dedicated host resides. This parameter is empty by default. If this parameter is not specified, the system will automatically select a zone. | None |
| ChargeType | String | Yes | Released | The billing method of the dedicated host. | Valid values: PostPaid and pay-as- you-go. |

|   | ss |
|---|---|
| 00 |   |

| Parameter | Type |   | Required |   | Editable |   | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AutoPlaceme nt | String |   | Yes |   | Released |   | Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify a DedicatedHostId when you create an instance on a DDH, Alibaba Cloud automatically selects a DDH from the resource pool to host the instance. |   | Valid values: on off Not e If you do not specify this parameter, the dedicated host is added to the automatic deployment resource pool. If you do not want to add the dedicated host to the resource pool for automatic deployment, set the value to off. |   |   |
| Tags | List |   | Erased |   | Released |   | The custom tags of |   | A maximum of 20 tags are supported. The format is as follows: [{"Key": |   |   |
|   |   |   |   |   |   |   |   |   |   | [{"Key": |   |
|   |   |   |   |   |   |   |   | gs of | "tagKey", "Value": |   |   |
|   |   |   |   |   |   |   | the instance. |   |   |   |   |
|   |   |   |   |   |   |   |   |   | "tagValue"}, |   |   |
|   |   |   |   |   |   |   |   |   | {"Key": "tagKey2", |   |   |
|   |   |   |   |   |   |   |   |   | "Value": |   |   |
|   |   |   |   |   |   |   |   |   | "tagValue2"}] |   |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ActionOnMai ntenance | String | Yes | Released | The method used to migrate the instances on the DDH when the DDH fails or needs to be repaired online. | Valid valus: Migrate: specifies that the instances are migrated to another physical server and restarted. Stop: specifies that all the instances on the DDH are stopped. If the DDH cannot be repaired, the instances are migrated to another physical server and restarted. The default value is "Migrate" for a dedicated host and "Stop" for a local disk. |
| NetworkAttri butesSlbUdp Timeout | String | Optional | Released | The timeout period for a UDP session. | Valid values: 15 to 310. Unit: seconds. |
| ResourceGro upId | String | Yes | Released | The ID of the resource group to which the dedicated host belongs. | None |
| NetworkAttri butesUdpTi meout | String | Optional | Released | The timeout period for UDP sessions that users can access for cloud services running on the dedicated host. | Valid values: 15 to 310. Unit: seconds. |
| Quantity | String | Optional | Released | The number of DDHs that you want to create this time. | Valid values: 1 to 100. Default value: 1 |

Response parameters Fn::GetAtt OrderId: the ID of the order. DedicatedHostIds: the list of host IDs. Sample request

|   | { "ROSTemplateFormatVersion": "2015-09-01", "Parameters": { "AutoRenewPeriod": { "Type": "Number", "Description": "The time period of auto renew. When the parameter InstanceChargeType is Pre Paid, it will take effect.It could be 1, 2, 3, 6, 12\. Default value is 1.", "AllowedValues": [ 1, 2, 3, 6, 12 ], "Default": 1 }, "Description": { "Type": "String", "Description": "The description of host." }, "ZoneId": { "Type": "String", "Description": "The zone to create the host." }, "DedicatedHostName": { "Type": "String", "Description": "The name of the dedicated host, [2, 128] English or Chinese characters. It must begin with an uppercase/lowercase letter or a Chinese character, and may contain numbers, ' _ ' or '-'. It cannot begin with http:// or https://." }, "ChargeType": { "Type": "String", "Description": "Instance Charge type, allowed value: Prepaid and Postpaid. If specified Pre paid, please ensure you have sufficient balance in your account. Or instance creation will be fai lure. Default value is Postpaid.", "AllowedValues": [ "PrePaid", "PostPaid" ], "Default": "PostPaid" }, "AutoRenew": { "Type": "String", "Description": "Whether renew the fee automatically? When the parameter InstanceChargeType is PrePaid, it will take effect. Range of value:True: automatic renewal.False: no automatic renew al. Default value is False.", "AllowedValues": [ "True", "False" ], "Default": "False" }, "Period": { "Type": "Number", "Description": "Prepaid time period. Unit is month, it could be from 1 to 9 or 12, 24, 36, 48, 60\. Default value is 1.", "AllowedValues": [ 1, |   |
|---|---|---|

`2,` `3,` `4,` `5,` `6,` `7,` `8,` `9,`

```
        12,
        24,
        36,
        48,
```

`],`

```json
      "Default": 1
    "DedicatedHostType": {
      "Type": "String",
      "Description": "The instance type of host."
    "PeriodUnit": {
      "Type": "String",
      "Description": "Unit of prepaid time period, it could be Week/Month. Default value is Month
.",
      "AllowedValues": [
        "Week",
        "Month"
```

`],`

```json
      "Default": "Month"
    "AutoReleaseTime": {
      "Type": "String",
      "Description": "Auto release time for created host, Follow ISO8601 standard using UTC time.
format is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
  "Resources": {
    "Host": {
      "Type": "ALIYUN::ECS::DedicatedHost",
      "Properties": {
          "Description": {
          "Ref": "Description"
        "ZoneId": {
          "Ref": "ZoneId"
        "DedicatedHostName": {
          "Ref": "DedicatedHostName"
        "ChargeType": {
          "Ref": "ChargeType"
          "DedicatedHostType": {
          "Ref": "DedicatedHostType"
        "PeriodUnit": {
          "Ref": "PeriodUnit"
```

```json
        "AutoReleaseTime": {
          "Ref": "AutoReleaseTime"
  "Outputs": {
    "OrderId": {
      "Description": "The order id list of created instance.",
      "Value": {
        "Fn::GetAtt": [
          "Host",
          "OrderId"
```

`]`

```json
    "DedicatedHostIds": {
      "Description": "The host id list of created hosts",
      "Value": {
        "Fn::GetAtt": [
          "Host",
          "DedicatedHostIds"
```

`]`

#### 6.1.6 ALIYUN::ECS::Disk

ALIYUN::ECS::Disk is used to create a disk for an Elastic Compute Service (ECS) instance. Syntax

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
    "ProvisionedIops": Integer
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the disk belongs. | None |
| ZoneId | String | Yes | No | The ID of the zone. | None |
| DiskName | String | No | No | The name of the disk. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons(:), underscores ( ), _ and hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | No | The description of the disk. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Tags | List | No | No | The tags of the disk. | You can specify up to 20 tags. For more information, see Tags properties. |
| DiskCategory | String | No | No | The category of the disk. | Default value: cloud. Valid values: cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: standard SSD _ cloud essd: enhanced SSD _ (ESSD) |
| SnapshotId | String | No | No | The ID of the snapshot. | If you set the SnapshotId property and the Size property at the same time, the SnapshotId property takes precedence. The actual size of the created disk is the size of the specified snapshot. Not e Snapshots that were created on or before July 15, 2013 cannot be used to create disks. |
| Performance Level | String | No | No | The performance level of the ESSD. | Default value: PL1. Valid values: PL0: A single ESSD can deliver up to 10,000 random read/write IOPS. PL1: A single ESSD can deliver up to 50,000 random read/write IOPS. PL2: A single ESSD can deliver up to 100,000 random read/write IOPS. PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS. For more information about performance levels of ESSDs, see ESSDs. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | Integer | No | No | The size of the disk. | Valid values if you set the DiskCategory property to cloud: 5 to 2000. Valid values if you set the DiskCategory property to cloud efficiency: 20 to _ 32768. Valid values if you set the DiskCategory property to cloud ssd: 20 to 32768. _ Valid values if you set the DiskCategory property to cloud essd: 20 to 32768. _ Unit: GiB. The value of this property must be greater than or equal to the size of the specified snapshot. |
| BurstingEnab led | Boolean | No | No | Specifies whether to enable bursting. | Default value: false. Valid values: true: enables bursting. false: disables bursting. |
| ProvisionedIo ps | Integer | No | No | The provisioned IOPS volume. | None |
| AutoSnapsh otPolicyId | String | No | No | The ID of the automatic snapshot policy. | None |
| Encrypted | Boolean | No | No | Specifies whether to encrypt the disk. | Default value: false. Valid values: true: encrypts the disk. false: does not encrypt the disk. |
| DeleteAutoS napshot | Boolean | No | No | Specifies whether to delete automatic snapshots of a disk when the disk is released. | Default value: true. Valid values: true : deletes automatic snapshots of a disk when the disk is released. false: does not delete automatic snapshots of a disk when the disk is released. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StorageSetId | String | No | No | The ID of the storage set. | None |
| KMSKeyId | String | No | No | The ID of the Key Management Service (KMS) key used by the disk. | None |
| StorageSetP artitionNumb er | Integer | No | No | The number of partitions in the storage set. | None |

Tags syntax

```json
"Tags" : [
    "Value" : String,
    "Key" : String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt DiskId: the ID of the disk. Status: the status of the disk. Examples `JSON` format

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "DataDisk": {
      "Type": "ALIYUN::ECS::Disk",
      "Properties": {
        "Size": 10,
        "ZoneId": "cn-beijing-a",
        "DiskName": "DataDisk",
        "Description": "ECSDataDisk"
  "Outputs": {
    "DiskId": {
         "Value" : {"Fn::GetAtt": ["DataDisk","DiskId"]}
    "Status": {
         "Value" : {"Fn::GetAtt": ["DataDisk","Status"]}
```

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  DataDisk:
    Type: 'ALIYUN::ECS::Disk'
    Properties:
      Size: 10
      ZoneId: cn-beijing-a
      DiskName: DataDisk
      Description: ECSDataDisk
Outputs:
  DiskId:
    Value:
      'Fn::GetAtt':
        - DataDisk
        - DiskId
  Status:
    Value:
      'Fn::GetAtt':
        - DataDisk
        - Status
```

To view more examples, visit Disk.json and Disk.yml.

#### 6.1.7 ALIYUN::ECS::DiskAttachment

ALIYUN::ECS::DiskAttachment is used to attach a disk to an ECS instance. Syntax

```json
  "Type": "ALIYUN::ECS::DiskAttachment",
  "Properties": {
    "InstanceId": String,
    "Device": String,
    "DeleteWithInstance": Boolean,
    "DiskId": String,
    "DeleteAutoSnapshot": Boolean
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | Yes | No | The ID of the ECS instance to which you want to attach the disk. | None |
| DiskId | String | Yes | No | The ID of the disk. | The disk and ECS instance must reside within the same zone. |
| Device | String | No | No | The device name of the disk. | If you do not set this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| DeleteWithInsta nce | Boolean | No | No | Specifies whether to release the disk together with the instance. | Valid values: true: releases the disk when the instance is released. false: retains the disk when the instance is released. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DeleteAutoSna pshot | Boolean | No | No | Specifies whether to delete automatic snapshots of the disk when the disk is released. | Default value: true. Valid values: true: false |

Response parameters Fn::GetAtt DiskId: the ID of the created disk. Status: the status of the created disk. Device: the device name of the created disk. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DiskAttachment": {
      "Type": "ALIYUN::ECS::DiskAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
        "Device": {
          "Ref": "Device"
        "DeleteWithInstance": {
          "Ref": "DeleteWithInstance"
        "DiskId": {
          "Ref": "DiskId"
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "The instanceId to attach the disk."
    "Device": {
      "Type": "String",
      "Description": "The device where the volume is exposed on the instance. could be /dev/xvd[a
-z]. If not specification, will use default value."
    "DeleteWithInstance": {
      "Type": "Boolean",
      "Description": "If property is true, the disk will be deleted while instance is deleted, if
property is false, the disk will be retain after instance is deleted.",
      "AllowedValues": [
```

```
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "DiskId": {
      "Type": "String",
      "Description": "The disk id to attached."
  "Outputs": {
    "Status": {
      "Description": "The disk status now.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Status"
```

`]`

```json
    "Device": {
      "Description": "The device where the volume is exposed on ecs instance.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Device"
```

`]`

```json
    "DiskId": {
      "Description": "The disk id of created disk",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "DiskId"
```

`]`

#### 6.1.8 ALIYUN::ECS::ForwardEntry

ALIYUN::ECS::ForwardEntry is used to configure the Destination Network Address Translation (DNAT) table of a Network Address Translation (NAT) gateway. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ExternalIp | String | Yes | No | The public IP address. | The value of the ExternalIp property must be an IP address that is included in the shared service plan of the NAT gateway to which the DNAT table belongs. |
| ExternalPort | String | Yes | No | The public port number. | Valid values: 1 to 65535. |
| ForwardTableId | String | Yes | No | The ID of the DNAT table. | None |
| InternalIp | String | Yes | No | The destination IP address to which you want to forward the request. | The value of the InternalIp property must be a private IP address. |
| IpProtocol | String | Yes | No | The protocol type. | Valid values: TCP UDP Any |
| InternalPort | String | Yes | No | The port number of the private network. | Valid values: 1 to 65535. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortBreak | Boolean | No | No | Specifies whether to remove limits on the port range. | Default value: false. Valid values: true: removes limits on the port range. false: does not remove limits on the port range. Not e If an SNAT entry and a DNAT entry use the same public IP address and you want to specify a port number that is greater than 1024, set the Portbreak property to true. |
| ForwardEntryNa me | String | No | No | The name of the DNAT entry. | The name must be 2 to 128 characters in length and must start with a letter. The name cannot start with http:// or https:// . |

Return values Fn::GetAtt ForwardEntryId: the ID of each entry in the DNAT table. Examples `JSON` format

```json
  "Parameters": {
    "ExternalPort": {
      "Type": "String",
      "Description": "Source port, now support [1-65535]|Any|x/y"
    "ExternalIp": {
      "Type": "String",
      "Description": "Source IP, must belongs to bandwidth package internet IP"
    "IpProtocol": {
      "Type": "String",
      "Description": "Supported protocol, Now support 'TCP|UDP|Any'",
      "AllowedValues": [
        "TCP",
        "UDP",
        "Any"
```

`]`

```json
    "PortBreak": {
      "Type": "Boolean",
      "Description": "Specifies whether to remove limits on the port range.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "InternalPort": {
      "Type": "String",
      "Description": "Destination port, now support [1-65535]|Any|x/y"
    "ForwardEntryName": {
      "Type": "String",
      "Description": "the name of the DNAT rule is 2-128 characters long and must start with a le
tter or Chinese, but cannot begin with HTTP:// or https://."
    "InternalIp": {
      "Type": "String",
      "Description": "Destination IP, must belong to VPC private IP"
    "ForwardTableId": {
      "Type": "String",
      "Description": "Create forward entry in specified forward table."
  "ROSTemplateFormatVersion": "2015-09-01",
  "Outputs": {
    "ForwardEntryId": {
      "Description": "The id of created forward entry.",
      "Value": {
        "Fn::GetAtt": [
          "ForwardTableEntry",
          "ForwardEntryId"
```

`]`

```json
  "Resources": {
    "ForwardTableEntry": {
      "Type": "ALIYUN::ECS::ForwardEntry",
      "Properties": {
        "ExternalPort": {
          "Ref": "ExternalPort"
        "ExternalIp": {
          "Ref": "ExternalIp"
        "IpProtocol": {
          "Ref": "IpProtocol"
        "PortBreak": {
          "Ref": "PortBreak"
        "InternalPort": {
          "Ref": "InternalPort"
        "ForwardEntryName": {
          "Ref": "ForwardEntryName"
        "InternalIp": {
          "Ref": "InternalIp"
        "ForwardTableId": {
          "Ref": "ForwardTableId"
```

`YAML` format

```
Parameters:
  ExternalPort:
    Type: String
    Description: 'Source port, now support [1-65535]|Any|x/y'
  ExternalIp:
    Type: String
    Description: 'Source IP, must belongs to bandwidth package internet IP'
  IpProtocol:
    Type: String
    Description: 'Supported protocol, Now support ''TCP|UDP|Any'''
    AllowedValues:
      - TCP
      - UDP
      - Any
  PortBreak:
    Type: Boolean
    Description: Specifies whether to remove limits on the port range.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
```

```
      - 'false'
  InternalPort:
    Type: String
    Description: 'Destination port, now support [1-65535]|Any|x/y'
  ForwardEntryName:
    Type: String
    Description: >-
      the name of the DNAT rule is 2-128 characters long and must start with a
      letter or Chinese, but cannot begin with HTTP:// or https://.
  InternalIp:
    Type: String
    Description: 'Destination IP, must belong to VPC private IP'
  ForwardTableId:
    Type: String
    Description: Create forward entry in specified forward table.
ROSTemplateFormatVersion: '2015-09-01' Outputs:
  ForwardEntryId:
    Description: The id of created forward entry.
    Value:
      'Fn::GetAtt':
        - ForwardTableEntry
        - ForwardEntryId
Resources:
  ForwardTableEntry:
    Type: 'ALIYUN::ECS::ForwardEntry'
    Properties:
      ExternalPort:
        Ref: ExternalPort
      ExternalIp:
        Ref: ExternalIp
      IpProtocol:
        Ref: IpProtocol
      PortBreak:
        Ref: PortBreak
      InternalPort:
        Ref: InternalPort
      ForwardEntryName:
        Ref: ForwardEntryName
      InternalIp:
        Ref: InternalIp
      ForwardTableId:
        Ref: ForwardTableId
```

To view more examples, visit ForwardEntry.json and ForwardEntry.yml.

#### 6.1.9 ALIYUN::ECS::Instance

ALIYUN::ECS::Instance is used to create an ECS instance. Statement

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
    "DiskMappings": List
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ImageId | String | No | Yes | The ID of the image used to start the ECS instance. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | When editing a template, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (*) to represent part of an image ID. Take all Ubuntu public images provided by Alibaba Cloud as an example. You can use one of the following methods to specify the public image ID for the ECS instance: If you enter ubuntu, the system matches it with the following ID: ubuntu16 0402 64 20G alib _ _ _ _ ase 20170818.vhd _ If you enter ubuntu 14, the _ system matches it with the following ID: ubuntu 14 0405 64 20G ali _ _ _ _ _ base 20170824.vhd _ If you enter ubuntu*14*32, the system matches it with the following ID: ubuntu 14 0405 32 40G ali _ _ _ _ _ base 20170711.vhd _ If you enter ubuntu 16 0402 32, the _ _ _ system matches it with the following ID: ubuntu 16 0402 32 40G ali _ _ _ _ _ base 20170711.vhd _ |
| InstanceType | String | No | No | The type of the ECS instance. | None |
| SecurityGroupId | String | No | No | The ID of the security group to which the created instance will belong. | None |
| Description | String | Yes | Released | The description of created instances. | The description can be up to 256 characters in length. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceName | String | Yes | Released | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), _ and hyphens (-). |
| Password | String | Yes | Released | The password used to log on to the ECS instance. | The characters in length is 8 to 30. And must contain at least one of the following character types: uppercase letters, lowercase letters, digits, and special character. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ‘ < > , . ? / - / - If you specify the Password parameter in the API request, use HTTPS to secure the API and protect your password. |
| HostName | String | Yes | Released | The hostname of the instance. | The password must be at least 2 characters in length. It cannot And hyphens (-) cannot start or end the hostname and cannot be used consecutively. On Windows, the hostname can be up to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot contain periods (.) and cannot be composed of only digits. On other OSs such as Linux, the hostname can contain a maximum of 30 characters, including periods (.), each segment can contain uppercase or lowercase letters, digits, and hyphens (-). |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PrivateIpAddress | String | Yes | Released | The private IP address of an ECS instance in a VPC. The specified IP address must not be used by other instances in the VPC. | None |
| InternetMaxBand widthIn | String | Optional | Released | The maximum inbound bandwidth from the Internet. | Valid values: 1 to 100. Default value: 100. Unit: Mbit/s. |
| IoOptimized | String | Yes | Released | Specifies whether an I/O optimized instance is created. | Valid values: none (non-I/O optimized) optimized Default value: none. |
| DiskMappings | List | Erased | Released | The data disks to be attached to the instance. | A maximum of 16 disks can be attached to each instance. |
| SystemDiskCateg ory | String | Yes | Released | The type of the system disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ |
| SystemDiskDescri ption | String | Yes | Released | The description of the ECS instance system disk. | None |
| SystemDiskDiskN ame | String | Yes | Released | The name of the ECS instance system disk. | None |
| SystemDiskSize | Number | No. | True | The size of the system disk. Unit: GB. | Valid values: 40 to 500. If a custom image is used to create a system disk, make sure that the size of the system disk is greater than that of the custom image. |

| Parameter |   | Type |   | Required | Editable |   | Description | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|
| Tags |   | List |   | Erased | Released |   | The custom tags | A maximum of 20 tags are supported. The format is as follows: [{&ldquo;Key”:”tagKey”,” |   |
|   |   |   |   |   |   |   |   |   | [{&ldquo;Key”:”tagKey”,” |
|   |   |   |   |   |   |   | of the instance. | Value”:”tagValue”}, |   |
|   |   |   |   |   |   |   |   | {&ldquo;Key”:”tagKey2”,”Va |   |
|   |   |   |   |   |   |   |   | lue”:”tagValue2”}] |   |
| UserData |   | String |   | Yes | Released |   | The user data that you provide when you create ECS instances. | The user data can be up to 16KB in size. You do not need to use Base64. you must use special characters. \ Escape. |   |
| ZoneId |   | String |   | Yes | Released |   | The ID of the zone where the instance resides. | None |   |
| HpcClusterId |   | String |   | Yes | Released |   | The ID of the HPC cluster to which the ECS instance belongs. | None |   |
| VpcId |   | String |   | Yes | Released |   | The ID of the VPC to which the ECS instance belongs. | None |   |
| VSwitchId |   | String |   | Yes | Released |   | The ID of the VSwitch for the ECS instance. | None |   |
| KeyPairName |   | String |   | Yes | Released |   | The name of the key pair that is used to connect to created ECS instances. | For Windows-based instances, this parameter is empty by default. In the Linux, if this parameter is specified, the Password content is still set to the instance, but the Password logon method is disabled by default. The key pair is used to verify the logon. |   |
| RamRoleName |   | String |   | Yes | Released |   | The RAM role name of the instance. You can call the ListRoles operation to query the role name. | None |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DeletionProtecti on | Boolean | Erased | Released | The release protection property of created instances. It specifies whether the instances can be released from the ECS console or through the DeleteInstance operation. | Valid values: True False |
| DeploymentSetId | String | Yes | True | Deployment Set ID. | None |

DiskMappings syntax

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
```

`]` DiskMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ Default value: cloud. |
| DiskName | String | Yes | Released | The name of data disk N. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of data disk N. | Valid values: 2 to 256. Default value: Null. |
| Device | String | Yes | Released | The device name of the data disk. | If you do not specify this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | None |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |
| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt InstanceId: the ID of the instance. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIp: The private IP address of the instance in a VPC. This parameter takes effect only when the NetworkType parameter is set to VPC. InnerIp: The private IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. PublicIp: the public IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. ZoneId: the zone ID. HostName: the hostname of the instance. Sample request

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

`]`

```json
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
```

#### 6.1.10 ALIYUN::ECS::InstanceClone

ALIYUN::ECS::InstanceClone is used to clone an ECS instance. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroup Id | String | Yes | Release d | The ID of the resource group to which the instance belongs. | None |
| SourceInstance Id | String | No | No | The ID of the ECS instance to be cloned. | The clone operation clones the specified instance, including its instance type, image, bandwidth billing method, bandwidth limit, and network type. If the source ECS instance belongs to multiple security groups, the cloned instance is added only to the first of these security groups. |
| BackendServer Weight | String | Optional | Release d | The weight of the ECS instance in the Server Load Balancer instance. | Value range:[0, 100]. Default value: 100. |
| LoadBalancerI dToAttach | String | Yes | Release d | The ID of the SLB instance to which the ECS instance is to be attached. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Release d | The description of created instances. | The description can be up to 256 characters in length. |
| ImageId | String | Yes | True | The ID of the image used to start created instances. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | When editing a template, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (*) to represent part of an image ID. Take all Ubuntu public images provided by Alibaba Cloud as an example. You can use one of the following methods to specify the public image ID for the ECS instance: If you enter ubuntu, the system matches it with the following ID: ubuntu16 0402 64 20G alibase _ _ _ _ _ 20170818.vhd If you enter ubuntu 14, _ the system matches it with the following ID: ubuntu 14 0405 64 20G alibase _ _ _ _ _ _ 20170824.vhd If you enter ubuntu*14*32, the system matches it with the following ID: ubuntu 14 0405 32 40G alibase _ _ _ _ _ _ 20170711.vhd If you enter ubuntu 16 0402 32, _ _ _ the system matches it with the following ID: ubuntu 16 0402 32 40G alibase _ _ _ _ _ _ 20170711.vhd |
| SecurityGroupI d | String | Yes | Release d | The ID of the security group to which the created instance will belong. | None |
| InstanceName | String | Yes | Release d | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and _ hyphens (-). |

| User Guide·Resour | ce types |   |   |   | Resource Orchestration Servic |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Password | String | Yes | Release d | The password used to log on to the ECS instance. | The password must be 8 to 30 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; < > , . ? / If you specify the password parameter in the API request, use HTTPS to secure the API and protect your password. |
| DiskMappings | List | Erased | Release d | The disks to be attached to created instances. | A maximum of 16 disks can be attached to each instance. |
| Tags | List | Erased | Release d | The custom tags of the instance. | A maximum of 20 tags can be specified in the [{"Key":"tagKey","Value":"tagValu e" },{ "Key":"tagKey2","Value":"tagValu e2"}]. |
| ZoneId | String | Yes | Release d | The ID of the zone where the instance resides. | None |
| InstanceCharg eType | String | Yes | Release d | The billing method of the new ECS instance. | Valid values: PrePaid and PostPaid. Default value: Postpaid. If you set this parameter to Prepaid, make sure that you have sufficient balance in your account. Otherwise, the instance fails to be created. |
| Period | Number | Erased | Release d | The subscription period of the new ECS instance. This parameter is required when the InstanceChargeType parameter is set to PrePaid. This parameter is ignored when the InstanceChargeType parameter is set to PostPaid. | Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, and 36. Unit: month. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| KeyPairName | String | Yes | Release d | The name of the key pair that is used to connect to created ECS instances. | For Windows-based instances, this parameter is empty by default. In the Linux, if this parameter is specified, the Password content is still set to the instance, but the Password logon method is disabled by default. The key pair is used to verify the logon. |
| RamRoleName | String | Yes | Release d | The RAM role name of the instance. You can call the ListRoles operation to query the role name. | None |
| SpotPriceLimit | String | Yes | Release d | The maximum hourly price of the instance. | Parameter SpotStrategy this parameter takes effect only when the value is SpotWithPriceLimit. |
| SpotStrategy | String | Yes | Release d | The bidding policy for the pay-as-you- go instance. | This parameter is valid only when the InstanceChargeType parameter is set to PostPaid. Valid values: NoSpot: applies to regular pay- as-you-go instances. SpotWithPriceLimit: applies to preemptible instances with a maximum hourly price. SpotAsPriceGo: applies to pay- as-you-go instances priced at the market price at the time of purchase. Default value: NoSpot. |
| InternetMaxBa ndwidthIn | String | Optional | Release d | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. | Valid values: 1 to 200. |
| DeletionProtec tion | Boolean | Erased | Release d | Specifies whether to enable instance release protection in the console or by calling an API operation. ( DeleteInstance) Release instances. | Valid values: true and false. |

DiskMappings syntax

```json
"DiskMappings": [
    "Category": String,
    "DiskName": String,
    "Description": String,
    "Device": String,
    "SnapshotId": String,
    "Size": String
```

`]` DiskMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, and _ ephemeral ssd _ Default value: cloud. |
| DiskName | String | Yes | Released | Disk name. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | Yes | Released | The description of data disk N. | The description must be 2 to 256 characters in length. This parameter is empty by default. |
| Device | String | Yes | Released | The device name of the data disk. | If you do not specify this parameter, the system automatically allocates a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | None |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key, which cannot be an empty string. It can be up to 64 characters in length, cannot start with acs: or aliyun, and cannot contain http:// or https://. | None |
| Value | String | Yes | Released | The tag value, which can be an empty string. It can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt InstanceId: the ID of the instance. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIp: The private IP address of the instance in a VPC. This parameter takes effect only when the NetworkType parameter is set to VPC. InnerIp: The private IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. PublicIp: the public IP address of the instance in a Classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. ZoneId: the zone ID. HostName: the hostname of the instance. Sample request

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

`]`

```json
  "Outputs": {
    "InstanceId": {
         "Value": {"get_attr": ["WebServer","InstanceId"]}
    "PublicIp": {
         "Value": {"get_attr": ["WebServer","PublicIp"]}
```

#### 6.1.11 ALIYUN::ECS::InstanceGroup

ALIYUN::ECS::InstanceGroup is used to create an ECS instance group. Syntax

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
    "SystemDiskPerformanceLevel": String
```

Properties

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGrou pId | String | No | Yes | The ID of the resource group to which a created instance belongs. | None. |

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HpcClusterId | String | No | Yes | The ID of the HPC cluster to which a created instance belongs. | None. |
| MaxAmount | Integer | Supported | Yes | The maximum number of ECS instances that can be created at a time. | Valid values: 1 to 100. The MaxAmount parameter must be set to a value greater than or equal to the value of MinAmount. |
| MinAmount | String | Yes | Yes | The minimum number of ECS instances that can be created at a time. | Valid values: 1 to 100. The MinAmount parameter must be set to a value less than or equal to the value of MaxAmount. |
| Description | String | No | Yes | The description of created instances. | The description can be up to 256 characters in length. |
| InstanceType | String | Yes | Yes | The type of the ECS instance. | None. |
| ImageId | String | Yes | Yes | The ID of the image used to start an ECS instance. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | You can specify a partial public image ID instead of providing the complete ID. The following example shows how to use a CNAME record: Ubuntu is specified and ubuntu 16 0402 64 _ _ _ _ 20G alibase 201708 _ _ 18.vhd are matched. If ubuntu1432 is specified, ubuntu 14 0405 32 _ _ _ _ 40G alibase 201707 _ _ 11.vhd is matched. |
| SecurityGroupI d | String | No | No | The ID of the security group to which created instances belong. | None. |

| Attribute | Type |   | Required |   |   | Editable |   | Description |   | Constraint |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| InstanceName | String |   | No |   |   | No |   | The name of an instance. |   | The names can be up to 128 characters in length It can contain English letters, Chinese characters, digits, underscores ( ), _ periods (.), and hyphens (-). By name prefix[begin _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | name prefix[begin _ _ |   |   |
|   |   |   |   |   |   |   |   |   |   | number,bits]name su _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ffix |   |   |   |
| Password | String |   | No |   |   | Yes |   | The password used to log on to created ECS instances. |   | The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported :( |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | :( |   |
|   |   |   |   |   |   |   |   |   |   | ) '~! @ # $ % ^ & |   |   |   |
|   |   |   |   |   |   |   |   |   |   | * - + = \| { } [ ] |   |   |   |
|   |   |   |   |   |   |   |   |   |   | : ; ‘ < > , . ? / |   |   |   |
| HostName | String |   | No |   |   | No |   | The hostname of created ECS instances. |   | The hostname must contain at least two characters in length. The periods and hyphens (-) cannot start or end the hostname and cannot be used together. |   |   |   |

| Attribute | Type | Required | Editable | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| AutoReleaseTi me | String | No | No | The time scheduled for created ECS instances to be automatically released. |   | The time format must comply with ISO8601 specifications, for example, "yyyy-MM- |   |   |
|   |   |   |   |   |   |   | "yyyy-MM- |   |
|   |   |   |   |   | ces to | ddTHH:mm:ssZ" |   |   |
| PrivateIpAddre ss | String | No | No | The private IP address of an ECS instance in a VPC. |   | The specified IP address must not be used by other instances in the VPC. |   |   |
| DiskMappings | List | No | Yes | The data disks to be attached to created instances. |   | None. |   |   |
| InternetMaxBa ndwidthIn | Integer | No | No | The maximum inbound bandwidth from the Internet. |   | Unit: Mbit/s. Valid values: 1 to 100 Default value: 100. |   |   |
| IoOptimized | String | No | No | Specifies whether the created instances are I/O optimized. |   | Valid values: none (non-I/O optimized) optimized Default value: none. |   |   |
| SystemDiskCat egory | String | No | Yes | The category of the system disk. |   | Valid values: cloud: basic disk cloud efficiency: the _ ultra disk cloud ssd: standard _ SSDs cloud essd: enhanced _ SSD ephemeral ssd: local _ SSDs |   |   |
| SystemDiskDe scription | String | No | Yes | The description of the ECS instance system disk. |   | None. |   |   |

| Attribute |   | Type |   | Required |   | Editable |   | Description | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|---|
| SystemDiskDis kName |   | String |   | No |   | Yes |   | The name of the ECS instance system disk. | None. |   |
| SystemDiskSiz e |   | Number |   | No |   | Yes |   | The size of the system disk. | Valid values: 40 to 500. If a custom image is used to create a system disk, make sure that the size of the system disk is greater than that of the custom image. |   |
| Tags |   | List |   | No |   | Yes |   | The custom tags of a | A maximum of 20 tags are supported. The format is as follows: [{"Key":"tagKey"," |   |
|   |   |   |   |   |   |   |   |   |   | [{"Key":"tagKey"," |
|   |   |   |   |   |   |   |   | created | Value":"tagValue"}, |   |
|   |   |   |   |   |   |   |   | instance. | {"Key":"tagKey2","V |   |
|   |   |   |   |   |   |   |   |   | alue":"tagValue2"}] |   |
| UserData |   | String |   | No |   | Yes |   | The user data that you provide when you create ECS instances. | The user data can be up to 16 KB in size. You do not need to use Base64 for transcoding. Special characters need to be escaped. |   |
| ZoneId |   | String |   | No |   | No |   | The zone ID of the disk. | None. |   |
| VpcId |   | String |   | No |   | No |   | The ID of the VPC. | None. |   |
| VSwitchId |   | String |   | No |   | No |   | The ID of the VSwitch for the ECS instance. | None. |   |
| KeyPairName |   | String |   | No |   | Yes |   | The name of the key pair that is used to connect to created ECS instances. | For Windows-based ECS instances, this parameter is ignored. and it is empty by default. For Linux- based ECS instances, the Password parameter still takes effect if this parameter is specified. However, logon by password is disabled, and the KeyPairName value is used. |   |

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RamRoleName | String | No | Yes | The name of the instance RAM role. | You can call the ListRoles operation to query the role name. |
| DedicatedHos tId | String | No | No | The ID of the dedicated host. | None. |
| LaunchTempla teName | String | No | Yes | The name of the launch template for the instance. | None. |
| EniMappings | List | No | Yes | The elastic network interfaces (ENIs) to be attached to created instances. | Only one ENI can be attached to each instance. |
| LaunchTempla teId | String | No | Yes | The ID of the launch template. | None. |
| LaunchTempla teVersion | String | No | Yes | The version of the launch template. | If you do not specify a version, the default version is used. |
| NetworkType | String | No | No | The network type of created ECS instances. | Valid values: vpc classic Default value: classic. |
| DeletionProte ction | Boolean | No | No | The release protection attribute of the instance. It specifies whether you can use the ECS console or call the DeleteInstanc e operation to release the instance. | Valid values: true false |
| DeploymentSe tId | String | No | Yes | Deployment Set ID. | None. |

DiskMappings syntax

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

`]` DiskMappings properties

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | Yes | No | The size of a data disk. | Unit: GB. |
| Category | String | No | No | The type of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ cloud essd _ ephemeral ssd _ For I/O optimized instances, the default value is cloud efficiency. For _ non-I/O optimized instances, the default value is cloud. |
| DiskName | String | No | No | The name of data disk N. | The name can be up to 128 characters in length. It can contain English letters, Chinese characters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | No | No | The description of data disk N. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Device | String | No | No | The device name of the data disk. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
| SnapshotId | String | No | No | The ID of the snapshot. | None. |
| Encrypted | Boolean | No | No | Specifies whether to encrypt the data disk. | Valid values: true false Default value: false |
| KMSKeyId | String | No | No | The ID of the KMS key corresponding to the data disk. | None. |
| AutoSnapshot PolicyId | String | No | Yes | The ID of the automatic snapshot policy. | None. |
| PerformanceL evel | String | No | No | The performance level of the enhanced SSD used as the data disk. | (Default): Maximum random read /write IOPS of 50,000 per disk PL2: A single enhanced SSD delivers up to 100,000 random read/write IOPS. PL3: A single enhanced SSD delivers up to 1,000,000 random read/write IOPS. |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of tag N. | It must be 1 to 128 characters in length, and cannot start with aliyun and acs: beginning, cannot contain http:// or https:// . |
| Value | String | No | No | The value of tag N. | It must be 0 to 128 characters in length and cannot start with aliyun and acs: beginning, cannot contain http:// or https:// . |

EniMappings syntax

```json
"EniMappings": [
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
```

`]` EniMappings properties

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupI d | String | Yes | Yes | The ID of the security group to which an instance belongs. | The security group and the instance must be in the same VPC. |
| VSwitchId | String | Yes | No | The ID of the VSwitch to which the instance is connected. | None. |
| Description | String | No | Yes | The description of the ENI. | It can contain 2 to 256 English letters or Chinese character. It cannot start with http:// or https:// the beginning. |

| Attribute | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NetworkInterf aceName | String | No | Yes | The ENI name. | The name must be 2 to 128 characters in length Must start with an uppercase or lowercase letter, and cannot start with http:// or https:// the beginning. It must start with a letter and cannot start with http:// or https://. |
| PrimaryIpAddr ess | String | No | No | The primary private IP address of ENI N. | The specified IP address must be available within the CIDR block of the VSwitch. If this parameter is not specified, an available IP address in the VSwitch CIDR block will be selected at random. |

Return value Fn::GetAtt InstanceIds: the IDs of created instances in the ECS instance group. An ID is a system-generated globally unique identifier (GUID) for an instance. PrivateIps: the list of private IP addresses of instances in a VPC. This parameter takes effect only when the NetworkType parameter is set to VPC. For example, a Json-formatted Array: `["172.16.XX.XX", "172.16.XX` .XX",&hellip; "172.16.XX.XX"] the maximum number of IP addresses that can be specified. Separate multiple IP addresses with commas (,). InnerIps: the list of private IP addresses of instances in a classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. For example, a Json-formatted Array: `["10.1.XX.XX",` "10.1.XX.XX",&hellip; "10.1.XX.XX"] the maximum number of IP addresses that can be specified. Separate multiple IP addresses with commas (,). PublicIps: the list of public IP addresses of instances in a classic network. This parameter takes effect only when the NetworkType parameter is set to Classic. For example, a Json-formatted Array: `["42.1.XX.XX",` "42.1.XX.XX",&hellip; "42.1.XX.XX"] the maximum number of IP addresses that can be specified. Separate multiple IP addresses with commas (,). HostNames: the list of hostnames of all instances. OrderId: the list of order IDs of all instances. ZoneIds: the IDs of the zones where created instances reside. RelatedOrderIds: the list of related order IDs of created ECS instances. Examples

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

`]`

```json
  "Outputs": {
    "InstanceIds": {
         "Value":{"get_attr": ["WebServer","InstanceIds"]}
    "PublicIps": {
         "Value":{"get_attr": ["WebServer","PublicIps"]}
```

#### 6.1.12 ALIYUN::ECS::InstanceGroupClone

ALIYUN::ECS::InstanceGroupClone is used to clone an ECS instance group. Statement

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

Properties

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Rel eas ed | The ID of the enterprise resource group to which a created instance belongs. | None |
| HpcClusterId | String | Yes | Tru e | The ID of the E-HPC cluster to which a created instance belongs. | None |

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| SourceInstanceI d | String | No | No | The ID of the ECS instance to be cloned. | The clone operation clones the specified instance, including its instance type, image, bandwidth limit, and network type. If the source ECS instance belongs to multiple security groups, the cloned instance is added only to the first of these security groups. |
| MaxAmount | Intege r | Ret ain ed | Yes | The maximum number of ECS instances to be created. | Valid values: 1 to 100. The MaxAmount parameter must be set to a value greater than or equal to the value of the MinAmount parameter. |
| MinAmount | String | No | Yes | The minimum number of ECS instances to be created. | Valid values: 1 to 100. The MinAmount parameter must be set to a value less than or equal to the value of the MaxAmount parameter. |
| BackendServer Weight | String | Opt ion al | Rel eas ed | The weight assigned to the ECS instance in the Server Load Balancer instance. | Valid values: 0 to 100. Default value: 100. |
| LoadBalancerId ToAttach | String | Yes | Rel eas ed | The ID of the SLB instance to which the ECS instance is to be attached. | None |
| Description | String | Yes | Rel eas ed | The description of created instances. | The description can be up to 256 characters in length. |

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| ImageId | String | Yes | Tru e | The ID of the image used to start created instances. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | You can specify a partial public image ID instead of providing the complete ID. When editing a template used to deploy an ECS instance, you can specify the image type and version or only the image type. ROS automatically selects an appropriate public image ID. You can use the wildcard character (\*) to represent part of an image ID. You can use one of the following methods to specify the public image ID for the ECS instance: If you set the parameter to ubuntu, ubuntu 16 0402 64 20G alibase 2017081 _ _ _ _ _ _ 8.vhd. If this parameter is set to ubuntu 14, _ ubuntu 14 0405 64 20G alibase 2017082 _ _ _ _ _ _ 4.vhd is returned. Specify: ubuntu1432, which will eventually match: ubuntu 14 0405 32 40G alibase 2017071 _ _ _ _ _ _ 1.vhd Specify: ubuntu 16 0402 32, which will _ _ _ eventually match: ubuntu 16 0402 32 40G alibase 2017071 _ _ _ _ _ _ 1.vhd |
| SecurityGroupId | String | Yes | Rel eas ed | The ID of the security group to which created instances belong. | None |
| InstanceName | String | Yes | Rel eas ed | The name of a created instance. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and hyphens (-). _ |
| Password | String | Yes | Rel eas ed | The password used to log on to the ECS instance. | The password The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special character. Special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / If the Password parameter is specified, you must use HTTPS to call the operation to ensure that the Password remains confidential. |
| DiskMappings | List | Era sed | Rel eas ed | The data disks to be attached to the instance. | A maximum of 16 disks can be attached to each instance. |

|   | Parameter | Type |   |   | Req uire d | Edit abl e | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   | Tags | List |   |   | Era | Rel | The custom tags of | You can specify a maximum of 20 tags. The format is as follows: [{"Key":"tagKey","Value":"tagValue"} |   |   |
|   |   |   |   |   |   |   |   |   | [{"Key":"tagKey","Value":"tagValue"} |   |
|   |   |   |   |   | sed | eas | the instance. | , |   |   |
|   |   |   |   |   |   | ed |   |   |   |   |
|   |   |   |   |   |   |   |   | {"Key":"tagKey2","Value":"tagValue2"} |   |   |
|   |   |   |   |   |   |   |   | ] |   |   |
|   | ZoneId | String |   |   | Yes | Rel eas ed | The ID of the zone where the instance resides. | None |   |   |
|   | KeyPairName | String |   |   | Yes | Rel eas ed | The name of the key pair that is used to connect to the ECS instance. For Windows-based ECS instances, this parameter is ignored. Default value: empty. For Linux-based instances, the Password parameter still takes effect if this parameter is specified. However, logon by Password is disabled, and the KeyPairName value is used. | None |   |   |
|   | RamRoleName | String |   |   | Yes | Rel eas ed | The RAM role name of the instance. | You can use RAM API ListRoles you can call this operation to query the RAM role name of an instance. |   |   |
|   | SpotPriceLimit | String |   |   | Yes | Rel eas ed | The maximum hourly price of the instance. | This parameter supports up to three decimal places. Parameter SpotStrategy this parameter takes effect only when the value is SpotWithPriceLimit. |   |   |
|   | SystemDiskDisk Name | String |   |   | Yes | Tru e | The name of the system disk of created instances. | The name must be 2 to 128 characters in length Must start with an uppercase or lowercase letter, and cannot start with http:// or https:// and can contain digits, colons (:), underscores ( ), _ and hyphens (-). |   |   |

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| PeriodUnit | String | Yes | Tru e | The billing cycle for created ECS instances. | Valid values: Week. 1, 2, 3, and 4} when the value of the PeriodUnit parameter is Week. AutoRenewPeriod values are 1, 2, "3"}. Month 1, 2, 3, 4, 5, 6, and 7 when the PeriodUnit parameter is set to Month "8", "9", "12", "24", "36", "48", "60"},AutoRenewPeriod can be {"1", "2", "3", "6", "12"}. Default value: Month. |
| EniMappings | List | No. | Tru e | The elastic network interfaces (ENIs) to be attached to a created instance. | Only a single ENI can be attached to each instance. |

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| AutoReleaseTi me | String | Yes | Rel eas ed | The time scheduled for a created ECS instance to be automatically released. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. If the value of seconds (ss) is a value other than 00, the start time is automatically rounded down to the nearest minute based on the value of mm. The minimum release time must be at least 30 minutes later than the current time. The maximum release time must be at most three years from the current time. If you do not specify the AutoReleaseTime it indicates that the auto release feature is disabled and the ECS instance will not be automatically released. | None |

| Parameter | Type | Req uire d | Edit abl e | Description | Constraint |
|---|---|---|---|---|---|
| SystemDiskCate gory | String | Yes | Tru e | The type of the system disk. | Valid values: cloud: basic disk cloud efficiency: indicates an ultra disk. _ cloud ssd: indicates a standard SSD. _ ephemeral ssd: local SSD. _ cloud essd: indicates an enhanced SSD _ (ESSD). ESSDs are still in public preview and only available in some regions. For phased-out instance types that are not I/O optimized, the default value is cloud. For other instances, the default value is cloud efficiency. _ |
| LaunchTemplat eName | String | Yes | Tru e | The name of the launch template. | None |
| LaunchTemplat eVersion | String | Yes | Tru e | The version of the launch template. If you do not specify this parameter, the default version is used. | None |
| InternetMaxBan dwidthIn | String | Opt ion al | Rel eas ed | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. | Valid values: 1 to 200. Default value: 200. |
| LaunchTemplat eId | String | Yes | Tru e | The ID of the launch template. | None |
| SystemDiskDes cription | String | Yes | Tru e | The description of the system disk. | The description must be 2 to 256 characters in length and cannot start with http:// or https://. This parameter is empty by default. |
| DeletionProtect ion | Boolea n | Era sed | Rel eas ed | The release protection attribute of the instance. Specifies whether the ECS console or API DeleteInstance) to release the instance. | Valid values: true false |
| DeploymentSet Id | String | Yes | Tru e | Deployment Set ID. | None |

DiskMappings syntax

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

`]` DiskMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Encrypted | String | Yes | Released | Specifies whether to encrypt the data disk. | Valid values: true false Default value :false |
| KMSKeyId | String | Yes | Released | The KMS key ID for data disk N. | None |
| Size | String | No | No | The size of data disk N. Unit: GB. | None |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssdDefaul _ t |
| DiskName | String | Yes | Released | The name of data disk N. | The name can be up to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). |
| Description | String | Yes | Released | The description of data disk N. | Valid values: 2 to 256. Default value: Null. |
| Device | String | Yes | Released | The device name of the data disk attached to an ECS instance. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
| SnapshotId | String | Yes | Released | Create a data disk by using a snapshot. | None |

| User Guide·Resource | types |   |   | Reso | urce Orchestration Servic |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | Description | Constraint |

EniMappings syntax

```json
"EniMappings": [
    "SecurityGroupId": String,
    "VSwitchId": String,
    "Description": String,
    "NetworkInterfaceName": String,
    "PrimaryIpAddress": String
```

`]` EniMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | No | Yes | The ID of the security group to which the ENI belongs. | None |
| VSwitchId | String | No | No | The ID of the VSwitch to which the ENI belongs. | None |
| Description | String | Yes | True | The description of the ENI. | It can contain 2 to 256 English letters or Chinese character. It cannot start with http:// and https:// the beginning. |
| NetworkInterfac eName | String | Yes | True | The name of the ENI. | None |
| PrimaryIpAddress | String | Yes | Released | The primary IP address of the ENI. | None |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |
| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt InstanceIds: the IDs of instances in the ECS instance group. An ID is a globally unique identifier (GUID) generated by the system for an instance. PrivateIps: the private IP addresses of VPC-type instances. This parameter is valid only when the NetworkType parameter is set to VPC. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["172.16.XX.XX", "172.16.XX.XX", ... "172.16.XX.XX"]. InnerIps: the private IP addresses of instances in the classic network. This parameter is valid only when the NetworkType parameter is set to Classic. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["10.1.XX.XX", "10.1.XX.XX", ... "10.1.XX.XX"]. PublicIps: the public IP addresses of instances in the classic network. This parameter is applicable only when the NetworkType parameter is set is Classic. The parameter value is a JSON-formatted array, containing up to 100 IP addresses separated by commas (,). Example: ["42.1.XX.XX", "42.1.XX.XX", ... "42.1.XX.XX"]. HostNames: the hostnames of all instances. The parameter value is a JSON-formatted array. Example: ["host1", "host2", ... "host3"]. OrderId: the order IDs of all instances. ZoneIds: the IDs of the zones where created instances reside. Sample request

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
  "Outputs": {
    "InstanceIds": {
      "Value": {"get_attr": ["WebServer","InstanceIds"]}
    "PublicIps": {
      "Value": {"get_attr": ["WebServer","PublicIps"]}
```

#### 6.1.13 ALIYUN::ECS::Invocation

ALIYUN::ECS::Invocation is used to invoke a Cloud Assistant command for one or more ECS instances. Statement

```json
  "Type": "ALIYUN::ECS::Invocation",
  "Properties": {
    "Timed": Boolean,
    "Frequency": String,
    "CommandId": String,
    "InstanceIds": List
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Timed | Boolean | Erased | Released | Specifies whether to invoke the command on a periodic basis. Default value: false. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Frequency | String | Yes | Released | The frequency at which the command is invoked. | None |
| CommandId | String | No | No | The ID of the script. | None |
| InstanceIds | List | Yes | No | The IDs of the instances for which you want to invoke the command. A maximum of 20 instance IDs can be specified. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt The execution ID of the InvokeId: command. Sample request

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

`]`

```json
    "Frequency": {
      "Type": "String",
      "Description": "The frequency of timing execution (the shortest frequency is performed ever
y 1 minute). It is mandatory when Timing is True.The value rule follows the rules of the cron exp ression. "
    "CommandId": {
      "Type": "String",
      "Description": "The id of command."
    "InstanceIds": {
      "Type": "CommaDelimitedList",
      "Description": "The instance id list. Select up to 20 instances at a time.Instances selecte
d network type must be VPC network, status must be running"
```

```json
  "Resources": {
    "Invocation": {
      "Type": "ALIYUN::ECS::Invocation",
      "Properties": {
        "Timed": {
          "Ref": "Timed"
        "Frequency": {
          "Ref": "Frequency"
        "CommandId": {
          "Ref": "CommandId"
        "InstanceIds": {
          "Fn::Split": [
            ",",
              "Ref": "InstanceIds"
              "Ref": "InstanceIds"
```

`]`

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

#### 6.1.14 ALIYUN::ECS::JoinSecurityGroup

ALIYUN::ECS::JoinSecurityGroup is used to add one or more ECS instances to a specified security group. Syntax

```json
  "Type": "ALIYUN::ECS::JoinSecurityGroup",
  "Properties": {
    "InstanceId": String,
    "InstanceIdList": List,
    "SecurityGroupId": String,
    "NetworkInterfaceList": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | Yes | No | The ID of the security group. | None |
| InstanceId | String | No | No | The ID of the ECS instance to be added to the security group. | None |
| InstanceIdList | List | No | Yes | The IDs of the ECS instances to be added to the security group. | None |
| NetworkInterfa ceList | List | No | Yes | The IDs of the elastic network interfaces (ENIs). | None |

Response parameters Fn::GetAtt None Examples `JSON` format

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

`]` `YAML` format

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

#### 6.1.15 ALIYUN::ECS::LaunchTemplate

ALIYUN::ECS::LaunchTemplate is used to create a launch template for an Elastic Compute Service (ECS) instance. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LaunchTemp lateName | String | Yes | No | The name of the launch template. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons(:), underscores ( ), _ and hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| VersionDescri ption | String | No | No | The description of the launch template version. | The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| ImageId | String | No | No | The ID of the image. | None. |
| InstanceType | String | No | No | The type of the instance. | None. |
| SecurityGrou pId | String | No | No | The ID of the security group. | None. |
| NetworkTyp e | String | No | No | The network type of the instance. | Valid values: classic: classic network vpc: virtual private cloud (VPC) |
| VSwitchId | String | No | No | The ID of the vSwitch. This property is required when you create an instance of the VPC type. | None. |
| InstanceNam e | String | No | No | The name of the instance. | The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | No | The description of the instance. | The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InternetMaxB andwidthOut | Integer | No | No | The maximum outbound public bandwidth. | Valid values: 0 to 100. Unit: Mbit/s. |
| HostName | String | No | No | The hostname of the instance. | The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). The hostname must meet the following requirements: Windows instances: The hostname must be 2 to 15 characters in length, and can contain letters, digits, and hyphens (-). The hostname cannot contain only digits. Other instances such as Linux instances: The hostname must be 2 to 64 characters in length, and can contain letters, digits, and hyphens (-). |
| ZoneId | String | No | No | The ID of the zone in which the instance is deployed. | None. |
| SystemDiskC ategory | String | No | No | The category of the system disk. | Valid values: cloud: basic disk cloud efficiency: ultra disk. _ cloud ssd: SSD _ ephemeral ssd: local SSD _ |
| SystemDiskSi ze | Number | No | No | The size of the system disk. | Valid values: 20 to 500. Unit: GB. |
| SystemDiskDi skName | String | No | No | The name of the system disk. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| SystemDiskD escription | String | No | No | The description of the system disk. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |   |   |
| IoOptimized | String | No | No | Specifies whether the instance is an I/O optimized instance. | Valid values: none: a non-I/O optimized instance optimized: an I/O optimized instance |   |   |
| InternetChar geType | String | No | No | The metering method for network usage. | Valid values: PayByBandwidth: pay-by- bandwidth PayByTraffic: pay-by-data- transfer |   |   |
| UserData | String | No | No | The user data of the instance. | The user data must be encoded in Base64. The raw data can be up to 16 KB in size. |   |   |
| KeyPairName | String | No | No | The name of the key pair. | The name must meet the following requirements: Windows instances: You can ignore this property. By default, this property is empty. The Password property takes effect even if you specify the KeyPairName property. Linux instances: By default, password-based logon is disabled. |   |   |
| RamRoleNa me | String | No | No | The name of the RAM role for the instance. | None. |   |   |
| AutoRelease Time | String | No | No | The time at which the system automaticall y releases the instance. | Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. |   |   |
|   |   |   |   |   |   | yyyy- |   |

| call | MM-ddTHH:mm:ssZ |
|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SpotStrateg y | String | No | No | The preemption policy for a pay-as-you- go instance. | This property takes effect when you set the InstanceChargeType property to Postpaid. Valid values: NoSpot: The instance is created as a regular pay- as-you-go instance. SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price. SpotAsPriceGo: The instance is created as a preemptible instance whose price is based on the market price at the time of purchase. The market price can be equal to the price of a pay-as- you-go instance. |
| SpotPriceLim it | String | No | No | The maximum hourly price that you specify for the instance. | The value of this property can contain up to three decimal places. |
| SecurityEnha ncementStra tegy | String | No | No | Specifies whether to enable security hardening. | Valid values: Active: enables security hardening. Deactive: disables security hardening. |
| DiskMapping s | List | No | No | The data disks. | You can specify up to 16 data disks. For more information, see DiskMappings properties. |
| NetworkInter faces | List | No | No | The elastic network interfaces (ENIs). | You can specify up to eight ENIs. For more information, see NetworkInterfaces properties. |
| Tags | List | No | No | The tags of the instance, security group, disk, or ENI. | You can specify up to 20 tags. For more information, see Tags properties. |

| esource Orches | tration Service |   |   |   | User Guide·Resource type |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TemplateTa gs | List | No | No | The tags of the launch template. | You can specify up to 20 tags. For more information, see TemplateTags properties. |

DiskMappings syntax

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

`]` DiskMappings properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Category | String | No | No | The category of the data disk. | Valid values: cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: SSD _ ephemeral ssd: local SSD _ |
| DiskName | String | No | No | The name of the data disk. | The name must be 2 to 128 characters in length, and can contain letters, digits, colons(:), underscores ( ), _ and hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | No | The description of the data disk. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
| SnapshotId | String | No | No | The ID of the snapshot that is used to create the data disk. | None. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of the system disk. | Valid values: Valid values if you set the Category property to cloud: 5 to 2000 Valid values if you set the Category property to cloud efficiency: 20 to _ 32768 Valid values if you set the Category property to cloud ssd: 20 to 32768 _ Valid values if you set the Category property to ephemeral ssd: 5 to 800 _ Unit: GB. |
| Encrypted | Boolean | No | No | Specifies whether to encrypt the data disk. | Valid values: true: encrypts the data disk. false: does not encrypt the data disk. |
| DeleteWithIn stance | Boolean | No | No | Specifies whether the system releases the data disk when the instance is released. | Valid values: true: releases the data disk when the instance is released. false: does not release the data disk when the instance is released. |

NetworkInterfaces syntax

```json
"NetworkInterfaces": [
    "PrimaryIpAddress": String,
    "VSwitchId": String,
    "SecurityGroupId": String,
    "NetworkInterfaceName": String,
    "Description": String
```

`]` NetworkInterfaces properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PrimaryIpAdd ress | String | No | No | The primary private IP address of the ENI. | None. |
| VSwitchId | String | No | No | The ID of the vSwitch to which the ENI belongs. | None. |
| SecurityGrou pId | String | No | No | The ID of the security group to which the ENI belongs. | None. |
| NetworkInter faceName | String | No | No | The name of the ENI. | None. |
| Description | String | No | No | The description of the ENI. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

TemplateTags syntax

```json
"TemplateTags": [
    "Value": String,
    "Key": String
```

`]` TemplateTags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | The tag key. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt LaunchTemplateId: the ID of the launch template. LaunchTemplateName: the name of the launch template. DefaultVersionNumber: the default version number of the launch template. LatestVersionNumber: the latest version number of the launch template. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the instance, [2, 256] characters."
    "DiskMappings": {
      "Type": "Json",
      "Description": "Disk mappings to attach to instance. Max support 16 disks.",
      "MaxLength": 16
    "SystemDiskSize": {
      "Type": "Number",
      "Description": "Disk size of the system disk, range from 20 to 500 GB. If you specify with
your own image, make sure the system disk size bigger than image size. ",
      "MinValue": 20
```

```json
    "UserData": {
      "Type": "String",
      "Description": "User data to pass to instance. [1, 16KB] characters."
    "SystemDiskDescription": {
      "Type": "String",
      "Description": "Description of created system disk."
    "TemplateTags": {
      "Type": "Json",
      "Description": "Template tags to attach to launch template.",
      "MaxLength": 20
    "RamRoleName": {
      "Type": "String",
      "Description": "Instance RAM role name. The name is provided and maintained by Resource Acc
ess Management (RAM) and can be queried using ListRoles. For more information, see RAM API Create Role and ListRoles."
    "NetworkType": {
      "Type": "String",
      "Description": "Instance network type. Support 'vpc' and 'classic'",
      "AllowedValues": [
        "vpc",
        "classic"
```

`]`

```json
    "NetworkInterfaces": {
      "Type": "Json",
      "Description": "Elastic network interfaces to be attached to instance.",
      "MaxLength": 8
    "ImageId": {
      "Type": "String",
      "Description": "Image ID to create ecs instance."
    "SystemDiskDiskName": {
      "Type": "String",
      "Description": "Name of created system disk."
    "SpotPriceLimit": {
      "Type": "String",
      "Description": "The hourly price threshold of a instance, and it takes effect only when par
ameter InstanceChargeType is PostPaid. Three decimals is allowed at most. "
    "InstanceType": {
      "Type": "String",
      "Description": "Ecs instance supported instance type, make sure it should be correct."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance, security group, disk and network interface.",
      "MaxLength": 20
    "HostName": {
      "Type": "String",
      "Description": "Host name of created ecs instance. at least 2 characters, and '.' '-' Is no
```

```json
t the first and last characters as hostname, not continuous use. Windows platform can be up to 15 characters, allowing letters (without limiting case), numbers and '-', and does not support the n umber of points, not all is digital ('.').Other (Linux, etc.) platform up to 30 characters, allow ing support number multiple points for the period between the points, each permit letters (withou t limiting case), numbers and '-' components."
    "SpotStrategy": {
      "Type": "String",
      "Description": "The spot strategy of a Pay-As-You-Go instance, and it takes effect only whe
n parameter InstanceChargeType is PostPaid. Value range: \"NoSpot: A regular Pay-As-You-Go instan ce\", \"SpotWithPriceLimit: A price threshold for a spot instance, \"\"SpotAsPriceGo: A price tha t is based on the highest Pay-As-You-Go instance. \"",
      "AllowedValues": [
        "NoSpot",
        "SpotWithPriceLimit",
        "SpotAsPriceGo"
```

`]`

```json
    "KeyPairName": {
      "Type": "String",
      "Description": "SSH key pair name."
    "LaunchTemplateName": {
      "Type": "String",
      "Description": "The name of launch template."
    "IoOptimized": {
      "Type": "String",
      "Description": "The 'optimized' instance can provide better IO performance. Support 'none'
and 'optimized' only.",
      "AllowedValues": [
        "none",
        "optimized"
```

`]`

```json
    "VersionDescription": {
      "Type": "String",
      "Description": "Description for version 1 of launch template."
    "ZoneId": {
      "Type": "String",
      "Description": "Current zone to create the instance."
    "VSwitchId": {
      "Type": "String",
      "Description": "The vSwitch Id to create ecs instance."
    "SecurityGroupId": {
      "Type": "String",
      "Description": "Security group to create ecs instance. For classic instance need the securi
ty group not belong to VPC, for VPC instance, please make sure the security group belong to speci fied VPC."
    "SystemDiskCategory": {
      "Type": "String",
      "Description": "Category of system disk. support cloud|cloud_efficiency|cloud_ssd|cloud_ess
d|ephemeral_ssd",
```

```json
      "AllowedValues": [
        "cloud",
        "cloud_efficiency",
        "cloud_ssd",
        "cloud_essd",
        "ephemeral_ssd"
```

`]`

```json
    "InternetChargeType": {
      "Type": "String",
      "Description": "Instance internet access charge type.Support 'PayByBandwidth' and 'PayByTra
ffic' only.",
      "AllowedValues": [
        "PayByBandwidth",
        "PayByTraffic"
```

`]`

```json
    "InstanceName": {
      "Type": "String",
      "Description": "Display name of the instance, [2, 128] English or Chinese characters, must
start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "InternetMaxBandwidthOut": {
      "Type": "Number",
      "Description": "Max internet out bandwidth in Mbps(Mega bit per second). Range is [0,200].W
hile the property is not 0, public ip will be assigned for instance.",
      "MinValue": 0,
      "MaxValue": 200
    "SecurityEnhancementStrategy": {
      "Type": "String",
      "Description": "Activate or deactivate security enhancement,Value range: \"Active\" and \"D
eactive\"",
      "AllowedValues": [
        "Active",
        "Deactive"
```

`]`

```json
    "AutoReleaseTime": {
      "Type": "String",
      "Description": "Auto release time for created instance, Follow ISO8601 standard using UTC t
ime. format is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
  "Resources": {
    "LaunchTemplate": {
      "Type": "ALIYUN::ECS::LaunchTemplate",
      "Properties": {
        "Description": {
          "Ref": "Description"
        "DiskMappings": {
          "Ref": "DiskMappings"
        "SystemDiskSize": {
          "Ref": "SystemDiskSize"
"UserData":{
```

```json
        UserData: {
          "Ref": "UserData"
        "SystemDiskDescription": {
          "Ref": "SystemDiskDescription"
        "TemplateTags": {
          "Ref": "TemplateTags"
        "RamRoleName": {
          "Ref": "RamRoleName"
        "NetworkType": {
          "Ref": "NetworkType"
        "NetworkInterfaces": {
          "Ref": "NetworkInterfaces"
        "ImageId": {
          "Ref": "ImageId"
        "SystemDiskDiskName": {
          "Ref": "SystemDiskDiskName"
        "SpotPriceLimit": {
          "Ref": "SpotPriceLimit"
        "InstanceType": {
          "Ref": "InstanceType"
        "Tags": {
          "Ref": "Tags"
        "HostName": {
          "Ref": "HostName"
        "SpotStrategy": {
          "Ref": "SpotStrategy"
        "KeyPairName": {
          "Ref": "KeyPairName"
        "LaunchTemplateName": {
          "Ref": "LaunchTemplateName"
        "IoOptimized": {
          "Ref": "IoOptimized"
        "VersionDescription": {
          "Ref": "VersionDescription"
        "ZoneId": {
          "Ref": "ZoneId"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "SecurityGroupId": {
```

`y` `p`

```json
          "Ref": "SecurityGroupId"
        "SystemDiskCategory": {
          "Ref": "SystemDiskCategory"
        "InternetChargeType": {
          "Ref": "InternetChargeType"
        "InstanceName": {
          "Ref": "InstanceName"
        "InternetMaxBandwidthOut": {
          "Ref": "InternetMaxBandwidthOut"
        "SecurityEnhancementStrategy": {
          "Ref": "SecurityEnhancementStrategy"
        "AutoReleaseTime": {
          "Ref": "AutoReleaseTime"
  "Outputs": {
    "LaunchTemplateName": {
      "Description": "The name of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateName"
```

`]`

```json
    "LatestVersionNumber": {
      "Description": "The latest version number of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LatestVersionNumber"
```

`]`

```json
    "LaunchTemplateId": {
      "Description": "The id of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
          "LaunchTemplateId"
```

`]`

```json
    "DefaultVersionNumber": {
      "Description": "The default version number of launch template.",
      "Value": {
        "Fn::GetAtt": [
          "LaunchTemplate",
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
```

`yp` `g`

```
    Description: >-
      The hourly price threshold of a instance, and it takes effect only when
      parameter InstanceChargeType is PostPaid. Three decimals is allowed at
      most.
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
```

```
    Type: String
    Description: >-
      Security group to create ecs instance. For classic instance need the
      security group not belong to VPC, for VPC instance, please make sure the
      security group belong to specified VPC.
  SystemDiskCategory:
    Type: String
    Description: >-
      Category of system disk. support
      cloud|cloud_efficiency|cloud_ssd|cloud_essd|ephemeral_ssd
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
```

`R``f` `D`

```
iti
```

```
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
```

```
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
    Description: The default version number of launch template.
    Value:
      'Fn::GetAtt':
        - LaunchTemplate
        - DefaultVersionNumber
```

To view more examples, visit LaunchTemplate.json and LaunchTemplate.yml. In the examples, the ALIYUN::ECS::LaunchTemplate and ALIYUN::ECS::AutoProvisioningGroup resource types are used.

#### 6.1.16 ALIYUN::ECS::NatGateway

ALIYUN::ECS::NatGateway is used to create a NAT gateway for ECS instances in a VPC. Syntax

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
    "Tags": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VpcId | String | Yes | No | The ID of the VPC in which you want to create the NAT gateway. | None |
| VSwitchId | String | No | No | The ID of the VSwitch in the VPC. | None |
| Description | String | No | No | The description of the NAT gateway. | The description must be 2 to 256 characters in length. |
| NatGatewayNa me | String | No | No | The name of the NAT gateway. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). It must start with a letter. |
| NatType | String | No | No | The type of the NAT gateway. | Valid values: Normal Enhanced |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Duration | Number | No | No | The subscription period. | Valid values: Valid values when PricingCycle is set to Month: 1 to 9. Valid values when PricingCycle is set to Year: 1 to 3. Not e This parameter is required when the InstanceCh argeType parameter is set to PrePaid. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AutoPay | Boolean | No | No | Specifies whether to enable automatic payment. | Valid values: false: disables automatic payment. After an order is generated, you must go to the Order Center to complete the payment. true: enables automatic payment. Payments are automaticall y completed. Not e This parameter is required when the InstanceCh argeType parameter is set to PrePaid. |
| InstanceCharge Type | String | No | No | The billing method. | Default value: PostPaid. Valid values: PostPaid: pay-as-you- go PrePaid: subscription |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PricingCycle | String | No | No | The billing cycle of subscription NAT gateways. | Default value: Month. Valid values: Month Year Not e This parameter is required when the InstanceCh argeType parameter is set to PrePaid. |
| Spec | String | No | No | The specifications of the NAT gateway. | Default value: Small. Valid values: Small Middle Large XLarge.1 |
| DeletionProtecti on | Boolean | No | No | Specifies whether to enable deletion protection. | Default value: false. Valid values: true false |
| DeletionForce | Boolean | No | No | Specifies whether to forcibly delete SNAT and DNAT entries in the gateway and unbind the EIP from the NAT gateway. | Default value: false. Valid values: true false |
| Tags | List | No | No | The tags of the NAT gateway. | A maximum of 20 tags can be specified. For more information, see Tags properties. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The value of the tag. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

Response parameters Fn::GetAtt ForwardTableId: the ID of the port forwarding table. SNatTableId: the ID of the SNAT table. NatGatewayId: the unique ID of the NAT gateway. BandwidthPackageIps: the IP addresses included in all EIP bandwidth plans. BandwidthPackageIds: the IDs of all EIP bandwidth plans. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the NAT gateway, [2, 256] characters. Do not fill or empty,
the default is empty." "NatGatewayName":{
```

```json
    NatGatewayName: {
      "Type": "String",
      "Description": "Display name of the NAT gateway, [2, 128] English or Chinese characters, mu
st start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "InstanceChargeType": {
      "Type": "String",
      "Description": "The billing method. The default value is PostPaid (which means pay-as-you-g
o).",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
    "PricingCycle": {
      "Type": "String",
      "Description": "Price cycle of the resource. This property has no default value.",
      "AllowedValues": [
        "Month",
        "Year"
```

`]`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The VSwitch id to create NAT gateway."
    "Duration": {
      "Type": "Number",
      "Description": "The subscription duration. While choose by pay by month, it could be from 1
to 9. While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
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
    "NatType": {
```

```json
      "Type": "String",
      "Description": "The type of the NAT gateway. Valid values:\n- Normal: standard NAT gateway.
\n- Enhanced: enhanced NAT gateway.",
      "AllowedValues": [
        "Normal",
        "Enhanced"
```

`]`

```json
    "DeletionForce": {
      "Type": "Boolean",
      "Description": "Whether force delete the relative snat and dnat entries in the net gateway
and unbind eips. Default value is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id to create NAT gateway."
    "Spec": {
      "Type": "String",
      "Description": "NAT gateway specification. Now support 'Small|Middle|Large|XLarge.1'"
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to natgateway. Max support 20 tags to add during create natg
ateway. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
  "Resources": {
    "NatGateway": {
      "Type": "ALIYUN::ECS::NatGateway",
      "Properties": {
        "Description": {
          "Ref": "Description"
        "NatGatewayName": {
          "Ref": "NatGatewayName"
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        "PricingCycle": {
          "Ref": "PricingCycle"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "Duration": {
          "Ref": "Duration"
```

```json
        "DeletionProtection": {
          "Ref": "DeletionProtection"
        "AutoPay": {
          "Ref": "AutoPay"
        "NatType": {
          "Ref": "NatType"
        "DeletionForce": {
          "Ref": "DeletionForce"
        "VpcId": {
          "Ref": "VpcId"
        "Spec": {
          "Ref": "Spec"
        "Tags": {
          "Ref": "Tags"
  "Outputs": {
    "BandwidthPackageIds": {
      "Description": "The bandwidth package ids of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "BandwidthPackageIds"
```

`]`

```json
    "NatGatewayId": {
      "Description": "The Id of created NAT gateway.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "NatGatewayId"
```

`]`

```json
    "SNatTableId": {
      "Description": "The SNAT table id.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
          "SNatTableId"
```

`]`

```json
    "BandwidthPackageIps": {
      "Description": "The allocated public IPs.",
      "Value": {
        "Fn::GetAtt": [
          "NatGateway",
"BandwidthPackageIps"
```

```
          "BandwidthPackageIps"
```

`]`

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
```

```
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
```

```
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
        - NatGateway
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

#### 6.1.17 ALIYUN::ECS::NetworkInterface

ALIYUN::ECS::NetworkInterface is used to create an elastic network interface (ENI). Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the ENI belongs. | None.You can call the ListResourceGroups operation to query the resource group ID. |
| SecurityGrou pId | String | No | Yes | The ID of the security group to which the ENI belongs. | The security groups and the ENI must belong to the same VPC. Not e You cannot configure the SecurityGroupId and SecurityGroupIds properties at the same time. |
| VSwitchId | String | Yes | No | The vSwitch ID of the ENI. | None |
| Description | String | No | Yes | The description of the ENI. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NetworkInter faceName | String | No | Yes | The name of the ENI. | The name must be 2 to 128 characters in length and can contain letters, digits, colons(:), underscores ( ), _ and hyphens (-). The name must start with a letter but cannot start with http:// or https:// . |
| PrimaryIpAdd ress | String | No | No | The primary private IP address of the ENI. | The specified IP address must be an idle IP address within the CIDR block of the vSwitch. If this property is not specified, an idle IP address is assigned from the vSwitch CIDR block at random. |
| SecondaryPri vateIpAddres sCount | Integer | No | No | The number of secondary private IP addresses. | None |
| Tags | List | No | Yes | The tags of the ENI. | You can add up to 20 tags. For more information, see Tags properties. |
| SecurityGrou pIds | List | No | Yes | The IDs of one or more security groups to which the ENI belongs. | The security groups and the ENI must belong to the same VPC. Not e You cannot configure the SecurityGroupId and SecurityGroupIds properties at the same time. |
| PrivateIpAdd resses | List | No | No | The secondary private IP addresses selected from the CIDR block of the vSwitch that hosts the ENI. | Valid values if the ENI is in the Available state: 1 to 10. Valid values vary based on the instance type if the ENI is in the InUse state. For more information, see Instance family. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt NetworkInterfaceId: the ID of the ENI. MacAddress: the MAC address of the ENI. PrivateIpAddresses: the private IP addresses assigned to the ENI. SecondaryPrivateIpAddresses: the secondary private IP addresses assigned to the ENI. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of your ENI. It is a string of [2, 256] English or Chinese char
acters."
    "PrivateIpAddresses": {
      "Type": "Json",
      "Description": "Specifies secondary private IP addresses of the ENI. This IP address must b
e an available IP address in the CIDR block of the VSwitch to which the ENI belongs.",
      "MaxLength": 10
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
```

```json
    "SecondaryPrivateIpAddressCount": {
      "Type": "Number",
      "Description": "The number of private IP addresses that can be created automatically by ECS
```

`."`

```json
    "SecurityGroupId": {
      "Type": "String",
      "Description": "The ID of the security group that the ENI joins. The security group and the
ENI must be in a same VPC."
    "VSwitchId": {
      "Type": "String",
      "Description": "VSwitch ID of the specified VPC. Specifies the switch ID for the VPC."
    "NetworkInterfaceName": {
      "Type": "String",
      "Description": "Name of your ENI. It is a string of [2, 128]  Chinese or English characters
. It must begin with a letter and can contain numbers, underscores (_), colons (:), or hyphens (- )."
    "PrimaryIpAddress": {
      "Type": "String",
      "Description": "The primary private IP address of the ENI.  The specified IP address must h
ave the same Host ID as the VSwitch. If no IP addresses are specified, a random network ID is ass igned for the ENI."
    "SecurityGroupIds": {
      "Type": "Json",
      "Description": "The IDs of the security groups that the ENI joins. The security groups and
the ENI must belong to the same VPC.",
      "MaxLength": 16
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
  "Resources": {
    "EniInstance": {
      "Type": "ALIYUN::ECS::NetworkInterface",
      "Properties": {
        "Description": {
          "Ref": "Description"
        "PrivateIpAddresses": {
          "Ref": "PrivateIpAddresses"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "SecondaryPrivateIpAddressCount": {
          "Ref": "SecondaryPrivateIpAddressCount"
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
```

|   | }, "VSwitchId": { "Ref": "VSwitchId" }, "NetworkInterfaceName": { "Ref": "NetworkInterfaceName" }, "PrimaryIpAddress": { "Ref": "PrimaryIpAddress" }, "SecurityGroupIds": { "Ref": "SecurityGroupIds" }, "Tags": { "Ref": "Tags" } } } }, "Outputs": { "PrivateIpAddress": { "Description": "The primary private ip address of your Network Interface.", "Value": { "Fn::GetAtt": [ "EniInstance", "PrivateIpAddress" ] } }, "SecondaryPrivateIpAddresses": { "Description": "The secondary private IP addresses of your Network Interface.", "Value": { "Fn::GetAtt": [ "EniInstance", "SecondaryPrivateIpAddresses" ] } }, "MacAddress": { "Description": "The MAC address of your Network Interface.", "Value": { "Fn::GetAtt": [ "EniInstance", "MacAddress" ] } }, "NetworkInterfaceId": { "Description": "ID of your Network Interface.", "Value": { "Fn::GetAtt": [ "EniInstance", "NetworkInterfaceId" ] } } } |   |
|---|---|---|

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
    Description: Description of your ENI. It is a string of [2, 256] English or Chinese
      characters.
    Type: String
  NetworkInterfaceName:
    Description: Name of your ENI. It is a string of [2, 128]  Chinese or English
      characters. It must begin with a letter and can contain numbers, underscores
      (_), colons (:), or hyphens (-).
    Type: String
  PrimaryIpAddress:
    Description: The primary private IP address of the ENI.  The specified IP address
      must have the same Host ID as the VSwitch. If no IP addresses are specified,
      a random network ID is assigned for the ENI.
    Type: String
  PrivateIpAddresses:
    Description: Specifies secondary private IP addresses of the ENI. This IP address
      must be an available IP address in the CIDR block of the VSwitch to which the
      ENI belongs.
    MaxLength: 10
    Type: Json
  ResourceGroupId:
    Description: Resource group id.
    Type: String
  SecondaryPrivateIpAddressCount:
    Description: The number of private IP addresses that can be created automatically
      by ECS.
    Type: Number
  SecurityGroupId:
    Description: The ID of the security group that the ENI joins. The security group
      and the ENI must be in a same VPC.
    Type: String
  SecurityGroupIds:
    Description: The IDs of the security groups that the ENI joins. The security groups
      and the ENI must belong to the same VPC.
    MaxLength: 16
    Type: Json
  Tags:
    Description: Tags to attach to instance. Max support 20 tags to add during create
      instance. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
  VSwitchId:
    Description: VSwitch ID of the specified VPC. Specifies the switch ID for the
      VPC.
    Type: String
Resources:
  EniInstance:
    Properties:
      Description:
        Ref: Description
      NetworkInterfaceName:
```

```
        Ref: NetworkInterfaceName
      PrimaryIpAddress:
        Ref: PrimaryIpAddress
      PrivateIpAddresses:
        Ref: PrivateIpAddresses
      ResourceGroupId:
        Ref: ResourceGroupId
      SecondaryPrivateIpAddressCount:
        Ref: SecondaryPrivateIpAddressCount
      SecurityGroupId:
        Ref: SecurityGroupId
      SecurityGroupIds:
        Ref: SecurityGroupIds
      Tags:
        Ref: Tags
      VSwitchId:
        Ref: VSwitchId
    Type: ALIYUN::ECS::NetworkInterface
Outputs:
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
```

To view more examples, visit NetworkInterfaceAttachment.json and NetworkInterfaceAttachment.yml. In the examples, the ALIYUN::ECS::NetworkInterface, ALIYUN::ECS::NetworkInterfaceAttachment, and ALIYUN::ECS::NetworkInterfacePermission resource types are used.

#### 6.1.18 ALIYUN::ECS::NetworkInterfaceAttachment

ALIYUN::ECS::NetworkInterfaceAttachment is used to bind an elastic network interface (ENI) to an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). Syntax

```json
  "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
  "Properties": {
    "InstanceId": String,
    "NetworkInterfaceId": String,
    "TrunkNetworkInstanceId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | Yes | No | The ID of the instance. | None |
| NetworkInter faceId | String | Yes | No | The ID of the ENI. | None |
| TrunkNetwor kInstanceId | String | No | No | The ID of the trunk network interface. | None |

Return values Fn::GetAtt NetworkInterfaceId: the ID of the ENI. TrunkNetworkInstanceId: the ID of the trunk network interface. InstanceId: the ID of the instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "ECS instance id"
    "TrunkNetworkInstanceId": {
      "Type": "String"
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
  "Resources": {
    "EniAttachment": {
      "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
        "TrunkNetworkInstanceId": {
          "Ref": "TrunkNetworkInstanceId"
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
  "Outputs": {
    "TrunkNetworkInstanceId": {
      "Description": "ID of Trunk Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "TrunkNetworkInstanceId"
```

`]`

```json
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "NetworkInterfaceId"
```

`]` `YAML` format

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

To view more examples, visit NetworkInterfaceAttachment.json and NetworkInterfaceAttachment.yml. In the examples, the ALIYUN::ECS::NetworkInterface, ALIYUN::ECS::NetworkInterfaceAttachment, and ALIYUN::ECS::NetworkInterfacePermission resource types are used.

#### 6.1.19 ALIYUN::ECS::NetworkInterfacePermission

ALIYUN::ECS::NetworkInterfacePermission is used to grant an account the permission to attach an elastic network interface (ENI) to an instance. Syntax

```json
  "Type": "ALIYUN::ECS::NetworkInterfacePermission",
  "Properties": {
    "NetworkInterfaceId": String,
    "AccountId": String,
    "Permission": String
```

Properties

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| NetworkInterfa ceId | String | Yes | No | The ID of the ENI. | None |
| AccountId | String | Yes | No | The ID of the account. | None |
| Permission | String | Yes | No | The permission granted to the account. | None |

Response parameters Fn::Get At t NetworkInterfacePermissionId: the ID of the ENI permission. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AccountId": {
      "Type": "String",
      "Description": "the account id"
    "Permission": {
      "Type": "String",
      "Description": "the permission",
      "Default": "InstanceAttach"
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
  "Resources": {
    "EniPermission": {
      "Type": "ALIYUN::ECS::NetworkInterfacePermission",
      "Properties": {
        "AccountId": {
          "Ref": "AccountId"
        "Permission": {
          "Ref": "Permission"
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
  "Outputs": {
    "NetworkInterfacePermissionId": {
      "Description": "the network interface permission id",
      "Value": {
        "Fn::GetAtt": [
          "EniPermission",
          "NetworkInterfacePermissionId"
```

`]`

#### 6.1.20 ALIYUN::ECS::Route

ALIYUN::ECS::Route is used to create a custom route entry. Syntax

```json
  "Type": "ALIYUN::ECS::Route",
  "Properties": {
    "DestinationCidrBlock": String,
    "RouteTableId": String,
    "NextHopId": String,
    "NextHopType": String,
    "NextHopList": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestinationCidrBloc k | String | Yes | No | The destination CIDR block of the custom route entry. | None |
| RouteTableId | String | Yes | No | The ID of the route table. | None |
| NextHopId | String | No | No | The ID of the next- hop instance for the custom route entry. | None |
| NextHopType | String | No | No | The type of the next hop. | Default value: Instance. Valid values: Instance: an Elastic Compute Service (ECS) instance HaVip: a high-availability virtual IP address (HAVIP) RouterInterface: a router interface NetworkInterface: an elastic network interface (ENI) VpnGateway: a VPN gateway IPv6Gateway: an IPv6 gateway NatGateway: a NAT gateway Attachment: a transit router |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NextHopList | List | No | No | The list of next hops of the custom route entry. | If you set the NextHopList property, the route entry is an equal-cost multipath (ECMP) route. Valid values: 2 to 4. For more information, see NextHopList properties. |

NextHopList syntax

```json
"NextHopList": [
    "NextHopId": String,
    "NextHopType": String
```

`]` NextHopList properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NextHopId | String | Yes | No | The ID of the next- hop instance for the ECMP route entry. | None |
| NextHopType | String | No | No | The type of the next hop for the ECMP route entry. | Set the value to RouterInterface. |

Return values Fn::GetAtt None Examples

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

#### 6.1.21 ALIYUN::ECS::SNatEntry

ALIYUN::ECS::SNatEntry is used to configure the Source Network Address Translation (SNAT) table of a NAT gateway. Syntax

```json
  "Type": "ALIYUN::ECS::SNatEntry",
  "Properties": {
    "SNatTableId": String,
    "SNatIp": String,
    "SnatEntryName": String,
    "SourceCIDR": String,
    "SourceVSwitchId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SNatTableId | String | Yes | Yes | The ID of the SNAT table. | None |
| SNatIp | String | Yes | Yes | The public IP address to be translated. | The public IP address must be included in the NAT service plan. It cannot exist in both the forwarding table and the SNAT table. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SnatEntryName | String | No | Yes | The name of the SNAT entry. | The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| SourceCIDR | String | No | No | The CIDR block of the vSwitch or the IP address of the ECS instance. vSwitch granularity: specifies the CIDR block of the vSwitch such as 192.168.1.0/24. When an ECS instance attached to the vSwitch requires Internet access, the NAT gateway provides the SNAT service (Internet proxy service) for the ECS instance. If you specify only one public IP address for the SnatIp parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses for the SnatIp parameter, the ECS instance randomly selects a public IP address from SnatIp to access the Internet. ECS granularity: specifies the IP address of the ECS instance such as 192.168.1.1/32. When the ECS instance requires Internet access, the NAT gateway provides the SNAT service (Internet proxy service) for the ECS instance. If you specify only one | You must specify one of the SourceCIDR and SourceVSwtichId parameters, but you cannot specify both of them. |

| Property | Type | Required | Editable | public IP address for Description the SnatIp | Constraint |
|---|---|---|---|---|---|
|   |   |   |   | parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses for the SnatIp parameter, the ECS instance randomly selects a public IP address from SnatIp to access the Internet. |   |
| SourceVSwitchId | String | No | Yes | The vSwitch ID of the ECS instance that accesses the Internet by using the SNAT feature. | You must specify one of the SourceCIDR and SourceVSwtichId parameters, but you cannot specify both of them. |

Response parameters Fn::GetAtt SNatEntryId: the ID of each entry in the SNAT table. Example `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SourceVSwitchId": {
      "Type": "String",
      "Description": "Allow which switch can access internet."
    "SnatEntryName": {
      "Type": "String",
      "Description": "he name of the SNAT rule is 2-128 characters long and must start with a let
ter or Chinese, but cannot begin with HTTP:// or https://."
    "SourceCIDR": {
      "Type": "String",
      "Description": "Specifies the network segment of the switch. For example, 10.0.0.1/24. This
parameter and the SourceVSwtichId parameter are mutually exclusive and cannot appear at the same time."
    "SNatTableId": {
      "Type": "String",
      "Description": "Create SNAT entry in specified SNAT table."
    "SNatIp": {
      "Type": "String",
"Description":"SourceIP mustbelongstobandwidthpackageinternetIP"
```

```json
      Description: Source IP, must belongs to bandwidth package internet IP
  "Resources": {
    "SNatTableEntry": {
      "Type": "ALIYUN::ECS::SNatEntry",
      "Properties": {
        "SourceVSwitchId": {
          "Ref": "SourceVSwitchId"
        "SnatEntryName": {
          "Ref": "SnatEntryName"
        "SourceCIDR": {
          "Ref": "SourceCIDR"
        "SNatTableId": {
          "Ref": "SNatTableId"
        "SNatIp": {
          "Ref": "SNatIp"
  "Outputs": {
    "SNatEntryId": {
      "Description": "The id of created SNAT entry.",
      "Value": {
        "Fn::GetAtt": [
          "SNatTableEntry",
          "SNatEntryId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SourceVSwitchId:
    Type: String
    Description: Allow which switch can access internet.
  SnatEntryName:
    Type: String
    Description: >-
      he name of the SNAT rule is 2-128 characters long and must start with a
      letter or Chinese, but cannot begin with HTTP:// or https://.
  SourceCIDR:
    Type: String
    Description: >-
      Specifies the network segment of the switch. For example, 10.0.0.1/24.
      This parameter and the SourceVSwtichId parameter are mutually exclusive
      and cannot appear at the same time.
  SNatTableId:
    Type: String
    Description: Create SNAT entry in specified SNAT table.
  SNatIp:
    Type: String
    Description: 'Source IP, must belongs to bandwidth package internet IP'
Resources:
  SNatTableEntry:
    Type: 'ALIYUN::ECS::SNatEntry'
    Properties:
      SourceVSwitchId:
        Ref: SourceVSwitchId
      SnatEntryName:
        Ref: SnatEntryName
      SourceCIDR:
        Ref: SourceCIDR
      SNatTableId:
        Ref: SNatTableId
      SNatIp:
        Ref: SNatIp
Outputs:
  SNatEntryId:
    Description: The id of created SNAT entry.
    Value:
      'Fn::GetAtt':
        - SNatTableEntry
        - SNatEntryId
```

#### 6.1.22 ALIYUN::ECS::SecurityGroup

ALIYUN::ECS::SecurityGroup is used to create a security group. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the security group belongs. | None |
| VpcId | String | No | No | The ID of the virtual private cloud (VPC) in which you want to create the security group. | None |
| Description | String | No | No | The description of the security group. | The description must be 2 to 256 characters in length. |
| Tags | List | No | Yes | The tags of the security group. | You can specify up to 20 tags. For more information, see Tags properties. |

| Property | Type | Required | Editable | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| SecurityGrou pName | String | No | No | The name of the security group. | By default, this property is empty. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or http s:// . The name can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |   |   |
|   |   |   |   |   |   | http |   |
| SecurityGrou pEgress | List | No | Yes | The outbound rule of the security group. | For more information, see SecurityGroupEgress properties. |   |   |
| SecurityGrou pIngress | List | No | Yes | The inbound rule of the security group. | For more information, see SecurityGroupIngress properties. |   |   |
| SecurityGrou pType | String | No | No | The type of the security group. | Valid values: normal: basic security group enterprise: advanced security group |   |   |

|   | s:// |
|---|---|

Tags syntax

```json
"Tags": [
    "Value" : String,
    "Key" : String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key of the security group. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Value | String | No | No | The tag value of the security group. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

SecurityGroupEgress syntax

```json
"SecurityGroupEgress": [
    "Description": String,
    "PortRange": String,
    "SecurityGroupId": String,
    "NicType": String,
    "Priority": Integer,
    "DestGroupId": String,
    "DestCidrIp": String,
    "Policy": String,
    "IpProtocol": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String,
    "DestPrefixListId": String
```

`]` SecurityGroupEgress properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters in length. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestGroupO wnerId | String | No | No | The ID of the Alibaba Cloud account that is used to manage the destination security group when you configure a security group rule across multiple Alibaba Cloud accounts. | If you do not specify the DestGroupOwnerId property, the access permissions are configured for another security group that is managed by your Alibaba Cloud account. If you specify the DestCidrIp property, the DestGroupOwnerId property is ignored. |
| IpProtocol | String | Yes | No | The transport layer protocol. | Valid values: tcp udp icmp gre all: All the preceding protocols are supported. |
| PortRange | String | Yes | No | The range of destination port numbers that correspond to the transport layer protocol. | Valid values if you set the IpProtocol property to tcp or udp: 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. Valid values if you set the IpProtocol property to icmp: -1/-1. Valid values if you set the IpProtocol property to gre: -1/-1. Valid values if you set the IpProtocol property to all: -1/-1. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGrou pId | String | No | No | The ID of the security group for which you want to create an outbound rule. | None |
| NicType | String | No | No | The network type. | Default value: internet. Valid values: internet intranet |
| DestPrefixLis tId | String | No | No | The ID of the destination prefix list to which you want to control outbound access. | You can call the DescribePrefixLists operation to query the IDs of available prefix lists. If a security group is in the classic network, you cannot configure prefix lists in the security group rules. If you specify one of the DestCidrIp, Ipv6DestCidrIp, and DestGroupId properties, DestPrefixListId is ignored. |
| Priority | Integer | No | No | The priority of the authorizatio n policy. | Valid values: 1 to 100. Default value: 1. |
| DestGroupId | String | No | No | The ID of the destination security group within the same region. | You must specify at least one of the DestGroupId and DestCidrIp properties. If you specify both the DestGroupId and DestCidrIp properties, DestCidrIp takes precedence. If you specify only the DestGroupId property, set the NicType property to intranet. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestCidrIp | String | No | No | The destination IPv4 CIDR block. | The value must be in the CIDR format. The default value is 0.0.0.0/0, which includes all possible IPv4 addresses. Examples of other supported formats include 10.159.XX.XX/12. You can specify up to 10 IP addresses or CIDR blocks. Separate multiple IP addresses or CIDR blocks with commas (,). Not e Only IPv4 addresses are supported. |
| Policy | String | No | No | The authorizatio n policy. | Default value: accept. Valid values: accept: allows access. drop: denies access. |
| Ipv6DestCidrI p | String | No | No | The destination IPv6 CIDR block. | IPv6 addresses in the CIDR format are supported. You can specify only the IP addresses of ECS instances of the VPC type. |

SecurityGroupIngress syntax

```json
"SecurityGroupIngress": [
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

`]` SecurityGroupIngress properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroup OwnerId | String | No | No | The ID of the Alibaba Cloud account to which the source security group belongs. | None |
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters in length. |
| SourcePrefix ListId | String | No | No | The ID of the source prefix list to which you want to control inbound access. | You can call the DescribePrefixLists operation to query the IDs of available prefix lists. If a security group is in the classic network, you cannot configure prefix lists in the security group rules. If you specify one of the SourceCidrIp, Ipv6DestCidrIp, and DestGroupId properties, SourcePrefixListId is ignored. |
| IpProtocol | String | Yes | No | The transport layer protocol. | Valid values: tcp udp icmp gre all: All the preceding protocols are supported. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortRange | String | Yes | No | The range of destination port numbers that correspond to the transport layer protocol. | Valid values if you set the IpProtocol property to tcp or udp: 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. Valid values if you set the IpProtocol property to icmp: -1/-1. Valid values if you set the IpProtocol property to gre: -1/-1. Valid values if you set the IpProtocol property to all: -1/-1. |
| SourceGroupI d | String | No | No | The ID of the source security group within the same region. | You must specify the SourceGroupId property or the SourceCidrIp property. If you specify both the SourceGroupId and SourceCidrIp properties, SourceCidrIp takes precedence. If you specify only the SourceGroupId property, set the NicType property to intranet. |
| SecurityGrou pId | String | No | No | The ID of the security group for which you want to create an inbound rule. | None |
| NicType | String | No | No | The network type. | Default value: internet. Valid values: internet intranet |
| Priority | Integer | No | No | The priority of the authorizatio n policy. | Valid values: 1 to 100. Default value: 1. |

| R | esource Orches | tration Service |   |   |   | User Guide·Resource type | s |
|---|---|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceCidrIp | String | No | No | The source IPv4 CIDR block. | The value must be in the CIDR format. The default value is 0.0.0.0/0, which includes all possible IP addresses. Examples of other supported formats include 10.159.XX.XX/12. You can specify up to 10 IP addresses or CIDR blocks. Separate multiple IP addresses or CIDR blocks with commas (,). Not e Only IPv4 CIDR blocks are supported. |
| Policy | String | No | No | The authorizatio n policy. | Default value: accept. Valid values: accept: allows access. drop: denies access. |
| SourcePortR ange | String | No | No | The range of source port numbers that correspond to the transport layer protocol. | Valid values if you set the IpProtocol property to tcp or udp: 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. Valid values if you set the IpProtocol property to icmp: -1/-1. Valid values if you set the IpProtocol property to gre: -1/-1. Valid values if you set the IpProtocol property to all: -1/-1. |
| Ipv6SourceCi drIp | String | No | No | The source IPv6 CIDR block. | You can specify only the IP addresses of ECS instances of the VPC type. IPv6 addresses in the CIDR format are supported. |

Return values Fn::GetAtt SecurityGroupId: the ID of the security group. SecurityGroupName: the name of the security group. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of the security group, [2, 256] characters. Do not fill or empt
y, the default is empty."
    "VpcId": {
      "Type": "String",
      "Description": "Physical ID of the VPC."
    "SecurityGroupName": {
      "Type": "String",
      "Description": "Display name of the security group, [2, 128] English or Chinese characters,
must start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "SecurityGroupType": {
      "Type": "String",
      "Description": "The type of the security group. Valid values:\nnormal: basic security group
\nenterprise: advanced security group",
      "AllowedValues": [
        "normal",
        "enterprise"
```

`]`

```json
    "SecurityGroupIngress": {
      "Type": "Json",
      "Description": "Ingress rules for the security group."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "SecurityGroupEgress": {
      "Type": "Json",
      "Description": "egress rules for the security group."
  "Resources": {
    "SecurityGroup": {
```

```json
      "Type": "ALIYUN::ECS::SecurityGroup",
      "Properties": {
        "Description": {
          "Ref": "Description"
        "VpcId": {
          "Ref": "VpcId"
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "SecurityGroupType": {
          "Ref": "SecurityGroupType"
        "SecurityGroupIngress": {
          "Ref": "SecurityGroupIngress"
        "Tags": {
          "Ref": "Tags"
        "SecurityGroupEgress": {
          "Ref": "SecurityGroupEgress"
  "Outputs": {
    "SecurityGroupName": {
      "Description": "The name of security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupName"
```

`]`

```json
    "SecurityGroupId": {
      "Description": "generated security group id for security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
    Description: Description of the security group, [2, 256] characters. Do not fill
```

```
    Description: Description of the security group, [2, 256] characters. Do not fill
      or empty, the default is empty.
    Type: String
  ResourceGroupId:
    Description: Resource group id.
    Type: String
  SecurityGroupEgress:
    Description: egress rules for the security group.
    Type: Json
  SecurityGroupIngress:
    Description: Ingress rules for the security group.
    Type: Json
  SecurityGroupName:
    Description: Display name of the security group, [2, 128] English or Chinese characters,
      must start with a letter or Chinese in size, can contain numbers, '_' or '.',
      '-'
    Type: String
  SecurityGroupType:
    AllowedValues:
    - normal
    - enterprise
    Description: 'The type of the security group. Valid values:
      normal: basic security group
      enterprise: advanced security group'
    Type: String
  Tags:
    Description: Tags to attach to instance. Max support 20 tags to add during create
      instance. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
  VpcId:
    Description: Physical ID of the VPC.
    Type: String
Resources:
  SecurityGroup:
    Properties:
      Description:
        Ref: Description
      ResourceGroupId:
        Ref: ResourceGroupId
      SecurityGroupEgress:
        Ref: SecurityGroupEgress
      SecurityGroupIngress:
        Ref: SecurityGroupIngress
      SecurityGroupName:
        Ref: SecurityGroupName
      SecurityGroupType:
        Ref: SecurityGroupType
      Tags:
        Ref: Tags
      VpcId:
        Ref: VpcId
    Type: ALIYUN::ECS::SecurityGroup
Outputs:
  SecurityGroupId:
    Description: generated security group id for security group.
    Value:
      Fn::GetAtt:
```

```
      - SecurityGroup
      - SecurityGroupId
  SecurityGroupName:
    Description: The name of security group.
    Value:
      Fn::GetAtt:
      - SecurityGroup
      - SecurityGroupName
```

To visit more examples, visit JoinSecurityGroup.json and JoinSecurityGroup.yml. In the examples, the ALIYUN::ECS::SecurityGroup and ALIYUN::ECS::JoinSecurityGroup resource types are used.

#### 6.1.23 ALIYUN::ECS::SecurityGroupClone

ALIYUN::ECS::SecurityGroupClone is used to clone a security group. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | No | Yes | The ID of the resource group to which the instance belongs. | None |
| SourceSecurityG roupId | String | Yes | No | The ID of the source security group. | Only applicable security group rules are copied to the new security group. The security group rules are selected based on the network type of the new security group. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NetworkType | String | No | No | The network type of the new security group. | Set the value to Classic. |
| VpcId | String | No | No | The ID of the VPC to which the new security group belongs. | The NetworkType parameter is ignored if both the VpcId and NetworkType parameters are specified. |
| Description | String | No | No | The description of the new security group. | The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |
| SecurityGroupN ame | String | No | No | The name of the new security group. | This parameter is empty by default. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. |
| DestinationRegi onId | String | No | No | The ID of the destination region where the new security group resides. | Default value: CURRENT. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupT ype | String | No | No | The type of the new security group. | Valid values: normal and enterprise. A value of normal specifies a basic security group. A value of enterprise specifies an advanced security group. |

Response parameters Fn::GetAtt SecurityGroupId: the ID of the new security group. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SecurityGroupClone": {
      "Type": "ALIYUN::ECS::SecurityGroupClone",
      "Properties": {
        "SourceSecurityGroupId": {
          "Ref": "SourceSecurityGroupId"
        "VpcId": {
          "Ref": "VpcId"
        "Description": {
          "Ref": "Description"
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
        "DestinationRegionId": {
          "Ref": "DestinationRegionId"
        "NetworkType": {
          "Ref": "NetworkType"
  "Parameters": {
    "SourceSecurityGroupId": {
      "Type": "String",
      "Description": "Source security group ID is used to copy properties to clone new security g
roup. If the NetworkType and VpcId is not specified, the same security group will be cloned. If N etworkType or VpcId is specified, only proper security group rules will be cloned."
    "VpcId": {
"Type":"String",
```

```
ype:
```

`St` `g``,`

```json
      "Description": "Physical ID of the VPC."
    "Description": {
      "Type": "String",
      "Description": "Description of the security group, [2, 256] characters. Do not fill or empt
y, the default is empty."
    "SecurityGroupName": {
      "Type": "String",
      "Description": "Display name of the security group, [2, 128] English or Chinese characters,
must start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "DestinationRegionId": {
      "Default": "CURRENT",
      "Type": "String",
      "Description": "Clone security group to the specified region. Default to current region."
    "NetworkType": {
      "Type": "String",
      "Description": "Clone new security group as classic network type. If the VpcId is specified
, the value will be ignored.",
      "AllowedValues": [
        "Classic"
```

`]`

```json
  "Outputs": {
    "SecurityGroupId": {
      "Description": "Generated security group id of new security group.",
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroupClone",
          "SecurityGroupId"
```

`]`

#### 6.1.24 ALIYUN::ECS::SecurityGroupEgress

ALIYUN::ECS::SecurityGroupEgress is used to create an outbound access rule for a security group. Syntax

```json
  "Type": "ALIYUN::ECS::SecurityGroupEgress",
  "Properties": {
    "SecurityGroupId": String,
    "IpProtocol": String,
    "PortRange": String,
    "DestGroupId": String,
    "DestGroupOwnerAccount": String,
    "DestCidrIp": String,
    "Policy": String,
    "Priority": String,
    "NicType": String,
    "Ipv6DestCidrIp": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IpProtocol | String | Yes | No | The transport layer protocol. | Valid values: tcp udp icmp gre all Not e The value all indicates that all the four protocol s are support ed. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortRange | String | Yes | No | The range of destination port numbers corresponding to the transport layer protocol. | Valid values when IpProtocol is set to tcp or udp: 1 to 65535. Separate the starting and ending port numbers with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. Set the value to -1/-1 when IpProtocol is set to icmp. Set the value to -1/-1 when IpProtocol is set to gre. Set the value to -1/-1 when IpProtocol is set to all. |
| SecurityGroupId | String | No | No | The ID of the source security group. | None |
| NicType | String | No | No | The type of the network interface controller (NIC). | Default value: internet. Valid values: internet intranet If the DestGroupId parameter is specified, but the DestCidrIp parameter is not, set the value to intranet. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Priority | Integer | No | No | The priority of the security group rule. | Valid values: 1 to 100 Default value: 1. |
| DestGroupId | String | No | No | The ID of the destination security group for which you want to set access permissions. | You must specify at least one of the DestGroupId and DestCidrIp parameters. If the DestGroupId parameter is specified, but the DestCidrIp parameter is not, set the NicType value to intranet. If both the DestGroupId and DestCidrIp parameters are specified, the DestCidrIp parameter takes precedence. |
| DestCidrIp | String | No | No | The destination CIDR block. | Only IPv4 CIDR blocks are supported. |
| Policy | String | No | No | The authorization policy. | Default value: accept. Valid values: accept: allows access. drop: denies access. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestGroupOwn erAccount | String | No | No | The Alibaba Cloud account that manages the destination security group when you set a security group rule across accounts. | If you specify neither of the DestGroupOwn erAccount parameter nor the DestGroupOwn erId parameter, the access permission is configured on another security group managed by your account. If you specify the DestCidrIp parameter, the DestGroupOwn erAccount parameter is ignored. |
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters in length. |
| DestGroupOwn erId | String | No | No | The ID of the Alibaba Cloud account that manages the destination security group when you set a security group rule across accounts. | If you specify neither of the DestGroupOwn erAccount parameter nor the DestGroupOwn erId parameter, the access permission is configured on another security group managed by your account. If you specify the DestCidrIp parameter, the DestGroupOwn erId parameter is ignored. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Ipv6DestCidrIp | String | No | No | The destination IPv6 CIDR block. | IPv6 addresses in the CIDR format are supported. You can specify only the IP addresses of ECS instances in VPCs. |

Response parameters Fn::GetAtt None Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
      "Properties": {
        "SecurityGroupId": "sg-25bow****",
        "IpProtocol": "tcp",
        "PortRange": "65535/65535",
        "DestCidrIp": "0.0.0.0/0"
```

#### 6.1.25 ALIYUN::ECS::SecurityGroupIngress

ALIYUN::ECS::SecurityGroupIngress is used to create an inbound access rule for a security group. Syntax

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
    "SourceCidrIp": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IpProtocol | String | Yes | No | The Internet protocol. | Valid values: tcp udp icmp gre all |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortRange | String | Yes | No | The range of destination ports relevant to the transport layer protocol. | Valid values: If TCP or UDP is used, specify the source ports from 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1. When the IpProtocol parameter is set to gre, the port number range is -1/- 1. When the IpProtocol parameter is set to all, the port number range is -1/- 1. For use cases of ports, see Typical applications of commonly used ports. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupId | String | No | No | The ID of the source security group to which you want to grant access permissions. | You must specify at least one of the SourceGroupId and SourceCidrIp parameters. If the SourceGroupId parameter is specified, but the SourceCidrIp parameter is not, the NicType parameter must be set to intranet. If both the SourceGroupId and SourceCidrIp parameters are specified, the SourceCidrIp value is used by default. |
| SecurityGroupId | String | No | No | The ID of the security group for which you want to create the inbound access rule. | None |
| NicType | String | No | No | The type of the NIC. | Default value: internet. Valid values: internet intranet If the DestGroupId parameter is specified, but the DestCidrIp parameter is not, this parameter must be set to intranet. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Priority | Integer | No | No | The priority of the security group rule. | Valid values: 1 to 100. Default value: 1. |
| SourceCidrIp | String | No | No | The source IPv4 CIDR block. | Only IPv4 CIDR blocks are supported. |
| Policy | String | No | No | The access control policy. | Default value: accept. Valid values: accept: grants access. drop: denies access. |
| SourceGroupOw nerId | String | No | No | The ID of the Alibaba Cloud account that manages the source security group when you set a security group rule across accounts. | If this parameter is not specified, the access permission is automatically configured for another security group managed by your account. If the SourceCidrIp parameter is specified, this parameter is ignored. |
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters in length. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourcePortRang e | String | No | No | The range of source ports relevant to the transport layer protocol. | Valid values: If TCP or UDP is used, specify the source ports from 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1. When the IpProtocol parameter is set to gre, the port number range is -1/- 1. When the IpProtocol parameter is set to all, the port number range is -1/- 1. |
| Ipv6SourceCidrI p | String | No | No | The range of source IPv6 addresses. | CIDR blocks and IPv6 addresses are supported. You can only specify the IP addresses of ECS instances in VPCs. |

Response parameters Fn::GetAtt None. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "SourceGroupId": {
      "Type": "String",
      "Description": "Source Group Id"
    "Policy": {
      "Type": "String",
      "Description": "Authorization policies, parameter values can be: accept (accepted access),
drop (denied access). Default value is accept.",
      "AllowedValues": [
        "accept",
        "drop"
```

`]`

```json
    "PortRange": {
      "Type": "String",
      "Description": "Ip protocol relative port range. For tcp and udp, the port rang is [1,65535
], using format '1/200'For icmp|gre|all protocel, the port range should be '-1/-1'"
    "Description": {
      "Type": "String",
      "Description": "Description of the security group rule, [1, 512] characters. The default is
empty.",
      "MinLength": 1,
      "MaxLength": 512
    "SourcePortRange": {
      "Type": "String",
      "Description": "The range of the ports enabled by the source security group for the transpo
rt layer protocol. Valid values: TCP/UDP: Value range: 1 to 65535. The start port and the end por t are separated by a slash (/). Correct example: 1/200. Incorrect example: 200/1.ICMP: -1/-1.GRE: -1/-1.ALL: -1/-1."
    "Priority": {
      "Type": "Number",
      "Description": "Authorization policies priority range[1, 100]",
      "MinValue": 1,
      "MaxValue": 100,
      "Default": 1
    "SecurityGroupId": {
      "Type": "String",
      "Description": "Id of the security group."
    "SourceCidrIp": {
      "Type": "String",
      "Description": "Source CIDR Ip Address range. Only IPV4 supported."
```

```json
    "SourceGroupOwnerId": {
      "Type": "String",
      "Description": "Source Group Owner Account ID"
    "IpProtocol": {
      "Type": "String",
      "Description": "Ip protocol for in rule.",
      "AllowedValues": [
        "tcp",
        "udp",
        "icmp",
        "gre",
        "all"
```

`]`

```json
    "Ipv6SourceCidrIp": {
      "Type": "String",
      "Description": "Source IPv6 CIDR address segment. Supports IP address ranges in CIDR format
and IPv6 format.\nNote Only VPC type IP addresses are supported."
    "NicType": {
      "Type": "String",
      "Description": "Network type, could be 'internet' or 'intranet'. Default value is internet.
```

`",`

```json
      "AllowedValues": [
        "internet",
        "intranet"
```

`]`

```json
  "Resources": {
    "SecurityGroupIngress": {
      "Type": "ALIYUN::ECS::SecurityGroupIngress",
      "Properties": {
        "SourceGroupId": {
          "Ref": "SourceGroupId"
        "Policy": {
          "Ref": "Policy"
        "PortRange": {
          "Ref": "PortRange"
        "Description": {
          "Ref": "Description"
        "SourcePortRange": {
          "Ref": "SourcePortRange"
        "Priority": {
          "Ref": "Priority"
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        "SourceCidrIp": {
          "Ref": "SourceCidrIp"
```

```json
        "SourceGroupOwnerId": {
          "Ref": "SourceGroupOwnerId"
        "IpProtocol": {
          "Ref": "IpProtocol"
        "Ipv6SourceCidrIp": {
          "Ref": "Ipv6SourceCidrIp"
        "NicType": {
          "Ref": "NicType"
```

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  SourceGroupId:
    Type: String
    Description: Source Group Id
  Policy:
    Type: String
    Description: >-
      Authorization policies, parameter values can be: accept (accepted access),
      drop (denied access). Default value is accept.
    AllowedValues:
      - accept
      - drop
  PortRange:
    Type: String
    Description: >-
      Ip protocol relative port range. For tcp and udp, the port rang is
      [1,65535], using format '1/200'For icmp|gre|all protocel, the port range
      should be '-1/-1'
  Description:
    Type: String
    Description: >-
      Description of the security group rule, [1, 512] characters. The default
      is empty.
    MinLength: 1
    MaxLength: 512
  SourcePortRange:
    Type: String
    Description: >-
      The range of the ports enabled by the source security group for the
      transport layer protocol. Valid values: TCP/UDP: Value range: 1 to 65535.
      The start port and the end port are separated by a slash (/). Correct
      example: 1/200. Incorrect example: 200/1.ICMP: -1/-1.GRE: -1/-1.ALL:
      -1/-1.
  Priority:
    Type: Number
    Description: 'Authorization policies priority range[1, 100]'
```

```
    MinValue: 1
    MaxValue: 100
    Default: 1
  SecurityGroupId:
    Type: String
    Description: Id of the security group.
  SourceCidrIp:
    Type: String
    Description: Source CIDR Ip Address range. Only IPV4 supported.
  SourceGroupOwnerId:
    Type: String
    Description: Source Group Owner Account ID
  IpProtocol:
    Type: String
    Description: Ip protocol for in rule.
    AllowedValues:
      - tcp
      - udp
      - icmp
      - gre
      - all
  Ipv6SourceCidrIp:
    Type: String
    Description: >-
      Source IPv6 CIDR address segment. Supports IP address ranges in CIDR
      format and IPv6 format.
      Note Only VPC type IP addresses are supported.
  NicType:
    Type: String
    Description: >-
      Network type, could be 'internet' or 'intranet'. Default value is
      internet.
    AllowedValues:
      - internet
      - intranet
Resources:
  SecurityGroupIngress:
    Type: 'ALIYUN::ECS::SecurityGroupIngress'
    Properties:
      SourceGroupId:
        Ref: SourceGroupId
      Policy:
        Ref: Policy
      PortRange:
        Ref: PortRange
      Description:
        Ref: Description
      SourcePortRange:
        Ref: SourcePortRange
      Priority:
        Ref: Priority
      SecurityGroupId:
        Ref: SecurityGroupId
      SourceCidrIp:
        Ref: SourceCidrIp
      SourceGroupOwnerId:
        Ref: SourceGroupOwnerId
IpProtocol:
```

```
      IpProtocol:
        Ref: IpProtocol
      Ipv6SourceCidrIp:
        Ref: Ipv6SourceCidrIp
      NicType:
        Ref: NicType
```

#### 6.1.26 ALIYUN::ECS::Snapshot

ALIYUN::ECS::Snapshot is used to create a disk snapshot. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskId | String | Yes | No | The ID of the disk for which you want to create the snapshot. | None |
| SnapshotNa me | String | No | No | The name of the snapshot. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . The name cannot start with auto because a snapshot whose name starts with auto is recognized as an automatic snapshot. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Timeout | Integer | No | No | The timeout period of the snapshot creation task. | If this parameter is specified, the timeout period to create a stack is extended. If the snapshot is not created within the specified timeout period, the entire stack cannot be created. Set this parameter based on the disk size and data volume. Valid values: 200 to 1440. Default value: 200. Unit: minutes. |
| Description | String | No | No | The description of the snapshot. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . This parameter is empty by default. |
| Tags | List | No | Yes | The tags of the snapshot. | A maximum of 20 tags can be specified. For more information, see the Tags properties section in this topic. |
| InstantAcces s | Boolean | No | No | Specifies whether to enable the instant access feature. | Default value: false. Valid values: true: The instant access feature is enabled. This feature can be enabled only for enhanced SSDs (ESSDs). false: The instant access feature is disabled. If InstantAccess is set to false, normal snapshots are created. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstantAcces sRetentionDa ys | Integer | No | No | Specifies the retention period of the instant access feature. After the retention period ends, the snapshot is automaticall y released. | This parameter is valid only when InstantAccess is set to true. Valid values: 1 to 65535. Unit: days. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

Response parameters Fn::GetAtt SnapshotId: the ID of the snapshot. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
"InstantAccess":{
```

```json
    InstantAccess: {
      "Type": "Boolean",
      "Description": "Specifies whether to enable the instant access feature. Valid values: \ntru
e: enables the instant access feature. This feature can be enabled only for enhanced SSDs (ESSDs) \nfalse: disables the instant access feature. If InstantAccess is set to false, normal snapshots are created.\nDefault value: false.\nNote This parameter and the Category parameter cannot be spe cified at the same time. \nFor more information, see the \"Description\" section in this topic.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "Description": {
      "Type": "String",
      "Description": "The description of a snapshot can be 2 to 256 characters in length and cann
ot begin with http:// or https://. The description will appear on the console. By default, the va lue is zero."
    "Timeout": {
      "Type": "Number",
      "Description": "The number of minutes to wait for create snapshot.",
      "MinValue": 200,
      "MaxValue": 1440,
      "Default": 200
    "SnapshotName": {
      "Type": "String",
      "Description": "The name of the snapshot, [2, 128] English or Chinese characters. It must b
egin with an uppercase/lowercase letter or a Chinese character, and may contain numbers, '_' or ' -'. It cannot begin with http:// or https://."
    "InstantAccessRetentionDays": {
      "Type": "Number",
      "Description": "Specifies the retention period of the instant access feature. After the ret
ention period ends, \nthe snapshot is automatically released. This parameter takes effect only wh en InstantAccess \nis set to true. Unit: days.\nValid values: 1 to 65535. By default, the value o f \nthis parameter is the same as that of RetentionDays."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "DiskId": {
      "Type": "String",
      "Description": "Indicates the ID of the specified disk."
  "Resources": {
    "Snapshot": {
      "Type": "ALIYUN::ECS::Snapshot",
      "Properties": {
        "InstantAccess": {
          "Ref": "InstantAccess"
```

```json
        "Description": {
          "Ref": "Description"
        "Timeout": {
          "Ref": "Timeout"
        "SnapshotName": {
          "Ref": "SnapshotName"
        "InstantAccessRetentionDays": {
          "Ref": "InstantAccessRetentionDays"
        "Tags": {
          "Ref": "Tags"
        "DiskId": {
          "Ref": "DiskId"
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
\false\nNoteThisparameterandtheCategoryparametercannotbespecified\
```

```
      \ false.\nNote This parameter and the Category parameter cannot be specified\
      \ at the same time. \nFor more information, see the \"Description\" section\
      \ in this topic."
    Type: Boolean
  InstantAccessRetentionDays:
    Description: "Specifies the retention period of the instant access feature. After\
      \ the retention period ends, \nthe snapshot is automatically released. This\
      \ parameter takes effect only when InstantAccess \nis set to true. Unit: days.\n\
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

#### 6.1.27 ALIYUN::ECS::SSHKeyPair

ALIYUN::ECS::SSHKeyPair is used to create an SSH key pair or import an existing SSH key pair to access an Elastic Compute Service (ECS) instance. Syntax

```json
  "Type": "ALIYUN::ECS::SSHKeyPair",
  "Properties": {
    "ResourceGroupId": String,
    "KeyPairName": String,
    "PublicKeyBody": String,
    "Tags": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the ECS instance belongs. | None |
| KeyPairName | String | Yes | No | The name of the key pair. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| PublicKeyBod y | String | No | No | The public key of the key pair. | This parameter is required only when you import an SSH key pair. |
| Tags | List | No | Yes | The tags of the key pair. | A maximum of 20 tags can be specified. For more information, see Tags properties. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

Response parameters Fn::GetAtt KeyPairFingerPrint: the fingerprint of the key pair. The fingerprint uses the message-digest algorithm 5 (MD5) based on the public key fingerprint format defined in RFC 4716. PrivateKeyBody: the private key of the key pair. An unencrypted RSA private key must be encoded in the PKCS#8 format by using PEM. The private key of a key pair can be obtained only when the key pair is first created. If you import an existing public key, no private key information is available. KeyPairName: the name of the key pair. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "KeyPairName": {
      "Type": "String",
      "Description": "SSH key pair name. It must be unique. [2, 128] characters. All character se
ts are supported. Do not start with a special character, digit, http://, or https://. It can cont ain digits, \".\", \"_\", or \"-\"."
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "PublicKeyBody": {
      "Type": "String",
      "Description": "SSH Public key. If PublicKeyBody is specified, existed public key body will
be imported instead of creating new SSH key pair."
```

```json
  "Resources": {
    "SSHKeyPair": {
      "Type": "ALIYUN::ECS::SSHKeyPair",
      "Properties": {
        "KeyPairName": {
          "Ref": "KeyPairName"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "Tags": {
          "Ref": "Tags"
        "PublicKeyBody": {
          "Ref": "PublicKeyBody"
  "Outputs": {
    "KeyPairFingerPrint": {
      "Description": "The fingerprint of the key pair. The public key fingerprint format defined
in RFC4716: MD5 message digest algorithm.",
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "KeyPairFingerPrint"
```

`]`

```json
    "KeyPairName": {
      "Description": "SSH Key pair name.",
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "KeyPairName"
```

`]`

```json
    "PrivateKeyBody": {
      "Description": "The private key of the key pair. Content of the RSA private key in the PKCS
#8 format of the unencrypted PEM encoding. Refer to: https://www.openssl.org/docs/apps/pkcs8.html
.User only can get the private key one time when and only when SSH key pair is created.",
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "PrivateKeyBody"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  KeyPairName:
    Description: SSH key pair name. It must be unique. [2, 128] characters. All character
      sets are supported. Do not start with a special character, digit, http://, or
      https://. It can contain digits, ".", "_", or "-".
    Type: String
  PublicKeyBody:
    Description: SSH Public key. If PublicKeyBody is specified, existed public key
      body will be imported instead of creating new SSH key pair.
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
  SSHKeyPair:
    Properties:
      KeyPairName:
        Ref: KeyPairName
      PublicKeyBody:
        Ref: PublicKeyBody
      ResourceGroupId:
        Ref: ResourceGroupId
      Tags:
        Ref: Tags
    Type: ALIYUN::ECS::SSHKeyPair
Outputs:
  KeyPairFingerPrint:
    Description: 'The fingerprint of the key pair. The public key fingerprint format
      defined in RFC4716: MD5 message digest algorithm.'
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
    Description: 'The private key of the key pair. Content of the RSA private key
      in the PKCS#8 format of the unencrypted PEM encoding. Refer to: https://www.openssl.org/doc
s/apps/pkcs8.html.User
      only can get the private key one time when and only when SSH key pair is created.'
    Value:
      Fn::GetAtt:
      - SSHKeyPair
      - PrivateKeyBody
```

For more examples, visit Instance.json and Instance.yml. In the examples, the ALIYUN::ECS::Instance, ALIYUN::ECS::SSHKeyPair, and ALIYUN::ECS::SSHKeyPairAttachment resource types are involved.

#### 6.1.28 ALIYUN::ECS::SSHKeyPairAttachment

ALIYUN::ECS::SSHKeyPairAttachment is used to attach an SSH key pair to specified ECS instances. Syntax

```json
  "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
  "Properties": {
    "InstanceIds": List,
    "KeyPairName": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceIds | List | Yes | Yes | The IDs of the ECS instances to which the SSH key pair is attached. | Separate IDs with commas (,). Only Linux instances are supported. |
| KeyPairName | String | Yes | No | The name of the SSH key pair. | None |

Response parameters Fn::GetAtt None. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SSHKeyPairAttachment": {
      "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
      "Properties": {
        "KeyPairName": "ssh_key_pai****",
        "InstanceIds": [
          'i-2zeiofnh20hj8fej****',
          'i-2zebt3kfvxm28y9o****'
```

`]`

#### 6.1.29 ALIYUN::ECS::VPC

ALIYUN::ECS::VPC is used to create a virtual private cloud (VPC). Syntax

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
    "SecondaryCidrBlock": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group. | None. |
| VpcName | String | No | Yes | The name of the VPC. | The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens _ (-). The name must start with a letter but cannot start with http:// or https:// . |
| CidrBlock | String | No | Yes | The CIDR block of the VPC. | Valid values: 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16 and its subnets |
| Description | String | No | Yes | The description of the VPC. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
| Ipv6CidrBlock | String | No | No | The IPv6 CIDR block of the VPC. | None. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| EnableIpv6 | Boolean | No | Yes | Specifies whether to enable IPv6 CIDR blocks. | Default value: false. Valid values: true: enables IPv6 CIDR blocks. false: does not enable IPv6 CIDR blocks. |
| Tags | List | No | Yes | The tags of the VPC. | You can specify up to 20 tags. For more information, see Tags propertes. |
| Ipv6Isp | String | No | No | The type of the IPv6 CIDR block of the VPC. | Set the value to BGP, which specifies Alibaba Cloud Border Gateway Protocol (BGP) IPv6. This is the default value. |
| UserCidr | String | No | No | The user CIDR block. | You can specify up to three CIDR blocks. Separate multiple CIDR blocks with commas (,). Not e For more information about user CIDR blocks, see FAQ about CIDR blocks. |
| SecondaryCi drBlock | String | No | No | The secondary IPv4 CIDR block. | Valid values: 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16 and its subnets When you add a secondary IPv4 CIDR block, take note of the following items: The CIDR block cannot start with 0. The CIDR block cannot be the same as the value of the CidrBlock property. The subnet mask must be 8 to 24 bits in length. |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags propertes

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The key cannot start with acs: or aliyun . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt VpcId: the ID of the VPC. VRouterId: the ID of the VRouter. RouteTableId: the ID of the route table. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Ipv6Isp": {
      "Type": "String",
      "Description": "The Internet service provider (ISP) for IPv6 addresses of the VPC. Valid va
lues:\nBGP(default): Alibaba Cloud BGP IPv6\nChinaMobile: China Mobile (single line)\nChinaUnicom : China Unicom (single line)\nChinaTelecom: China Telecom (single line)\nNote If your Alibaba Clo ud account is allowed to activate single-ISP bandwidth, you can set the parameter to ChinaTelecom , ChinaUnicom, and ChinaMobile."
    "Description": {
      "Type": "String",
      "Description": "Description of the vpc, [2, 256] characters. Do not fill or empty, the defa
ult is empty."
    "SecondaryCidrBlock": {
      "Type": "String",
      "Description": "The secondary IPv4 CIDR block. \nYou can specify one of the following stand
```

```json
ard IPv4 CIDR blocks or their \nsubnets as the secondary IPv4 CIDR block: 192.168.0.0/16, 172.16. 0.0/12, \nand 10.0.0.0/8.To use a public CIDR block as the secondary IPv4 CIDR block, \nsubmit a ticket. When you add a secondary IPv4 CIDR block, take note of \nthe following rules: \n1. The CI DR block cannot start with 0. \n2. The subnet mask must be 8 to 24 bits in length.\nThe secondary CIDR block cannot overlap with the primary \nCIDR block or an existing secondary CIDR block."
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "CidrBlock": {
      "Type": "String",
      "Description": "The IP address range of the VPC in the CIDR block form. You can use the fol
lowing IP address ranges and their subnets:\n10.0.0.0/8\n172.16.0.0/12 (Default)\n192.168.0.0/16"
    "VpcName": {
      "Type": "String",
      "Description": "Display name of the vpc instance, [2, 128] English or Chinese characters, m
ust start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "Ipv6CidrBlock": {
      "Type": "String",
      "Description": "IPv6 network cidr of the VPC.",
      "MinLength": 1
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to vpc. Max support 20 tags to add during create vpc. Each t
ag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "EnableIpv6": {
      "Type": "Boolean",
      "Description": "Whether to enable an IPv6 network cidr, the value is:False (default): not t
urned on.True: On.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "UserCidr": {
      "Type": "String",
      "Description": "The user CIDR block. Separate multiple CIDR blocks with commas (,). At most
three CIDR blocks are supported."
  "Resources": {
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "Ipv6Isp": {
          "Ref": "Ipv6Isp"
        "Description": {
```

```json
          "Ref": "Description"
        "SecondaryCidrBlock": {
          "Ref": "SecondaryCidrBlock"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "CidrBlock": {
          "Ref": "CidrBlock"
        "VpcName": {
          "Ref": "VpcName"
        "Ipv6CidrBlock": {
          "Ref": "Ipv6CidrBlock"
        "Tags": {
          "Ref": "Tags"
        "EnableIpv6": {
          "Ref": "EnableIpv6"
        "UserCidr": {
          "Ref": "UserCidr"
  "Outputs": {
    "VRouterId": {
      "Description": "Router id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VRouterId"
```

`]`

```json
    "RouteTableId": {
      "Description": "The router table id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "RouteTableId"
```

`]`

```json
    "VpcId": {
      "Description": "Id of created VPC.",
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VpcId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  CidrBlock:
    Description: 'The IP address range of the VPC in the CIDR block form. You can
      use the following IP address ranges and their subnets:
      10.0.0.0/8
      172.16.0.0/12 (Default)
      192.168.0.0/16'
    Type: String
  Description:
    Description: Description of the vpc, [2, 256] characters. Do not fill or empty,
      the default is empty.
    Type: String
  EnableIpv6:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Default: false
    Description: 'Whether to enable an IPv6 network cidr, the value is:False (default):
      not turned on.True: On.'
    Type: Boolean
  Ipv6CidrBlock:
    Description: IPv6 network cidr of the VPC.
    MinLength: 1
    Type: String
  Ipv6Isp:
    Description: 'The Internet service provider (ISP) for IPv6 addresses of the VPC.
      Valid values:
      BGP(default): Alibaba Cloud BGP IPv6
      ChinaMobile: China Mobile (single line)
      ChinaUnicom: China Unicom (single line)
      ChinaTelecom: China Telecom (single line)
      Note If your Alibaba Cloud account is allowed to activate single-ISP bandwidth,
      you can set the parameter to ChinaTelecom, ChinaUnicom, and ChinaMobile.'
    Type: String
  ResourceGroupId:
    Description: Resource group id.
    Type: String
  SecondaryCidrBlock:
    Description: "The secondary IPv4 CIDR block. \nYou can specify one of the following\
      \ standard IPv4 CIDR blocks or their \nsubnets as the secondary IPv4 CIDR block:\
      \ 192.168.0.0/16, 172.16.0.0/12, \nand 10.0.0.0/8.To use a public CIDR block\
      \ as the secondary IPv4 CIDR block, \nsubmit a ticket. When you add a secondary\
      \ IPv4 CIDR block, take note of \nthe following rules: \n1. The CIDR block cannot\
      \ start with 0. \n2. The subnet mask must be 8 to 24 bits in length.\nThe secondary\
      \ CIDR block cannot overlap with the primary \nCIDR block or an existing secondary\
      \ CIDR block."
    Type: String
  Tags:
    Description: Tags to attach to vpc. Max support 20 tags to add during create vpc.
```

```
      Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
  UserCidr:
    Description: The user CIDR block. Separate multiple CIDR blocks with commas (,).
      At most three CIDR blocks are supported.
    Type: String
  VpcName:
    Description: Display name of the vpc instance, [2, 128] English or Chinese characters,
      must start with a letter or Chinese in size, can contain numbers, '_' or '.',
      '-'
    Type: String
Resources:
  Vpc:
    Properties:
      CidrBlock:
        Ref: CidrBlock
      Description:
        Ref: Description
      EnableIpv6:
        Ref: EnableIpv6
      Ipv6CidrBlock:
        Ref: Ipv6CidrBlock
      Ipv6Isp:
        Ref: Ipv6Isp
      ResourceGroupId:
        Ref: ResourceGroupId
      SecondaryCidrBlock:
        Ref: SecondaryCidrBlock
      Tags:
        Ref: Tags
      UserCidr:
        Ref: UserCidr
      VpcName:
        Ref: VpcName
    Type: ALIYUN::ECS::VPC
Outputs:
  RouteTableId:
    Description: The router table id of created VPC.
    Value:
      Fn::GetAtt:
      - Vpc
      - RouteTableId
  VRouterId:
    Description: Router id of created VPC.
    Value:
      Fn::GetAtt:
      - Vpc
      - VRouterId
  VpcId:
    Description: Id of created VPC.
    Value:
      Fn::GetAtt:
      - Vpc
      - VpcId
```

To view more examples, visit SnatEntry.json and SnatEntry.yml. In the examples, the ALIYUN::ECS::VPC, ALIYUN::ECS::VSwitch, ALIYUN::VPC::SnatEntry, ALIYUN::VPC::CommonBandwidthPackage, ALIYUN::VPC::CommonBandwidthPackageIp, ALIYUN::VPC::Ipv6Gateway, and ALIYUN::VPC::Ipv6InternetBandwidth resource types are involved.

#### 6.1.30 ALIYUN::ECS::VSwitch

ALIYUN::ECS::VSwitch is used to create a vSwitch. Syntax

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

Properties

|   | Property |   | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|---|---|
|   | VpcId |   | String | Yes | No | The ID of the virtual private cloud (VPC) in which you create the vSwitch. | None. |
|   | ZoneId |   | String | Yes | No | The ID of the zone. | None. |
|   | VSwitchNa me |   | String | No | Yes | The name of the vSwitch. | The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens _ (-). The name must start with a letter but cannot start with http:// or https:// . |
|   |   | VSwitchNa |   |   |   |   |   |
|   | me |   |   |   |   |   |   |
|   | CidrBlock |   | String | Yes | No | The CIDR block of the vSwitch. | The CIDR block of a vSwitch must be a subset of the CIDR block of the VPC to which the vSwitch belongs and cannot be used by other vSwitches. |
|   |   | CidrBlock |   |   |   |   |   |

|   | Property |   | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|---|---|
|   | Descripti on |   | String | No | Yes | The description of the vSwitch. | The description must be 2 to 256 characters in length. The description cannot start with http:// or https:// . |
|   |   | Descripti | S |   |   |   |   |
|   | on |   |   |   |   |   |   |
|   | Ipv6CidrB lock |   | Integer | No | No | The IPv6 CIDR block of the vSwitch. | Valid values: 0 to 255. The value must be a decimal integer. By default, the mask of the IPv6 CIDR block of the vSwitch is 64 bits in length. You can specify a custom content for the last eight bits of the mask of the IPv6 CIDR block of the VPC. |
|   | Tags |   | List | No | Yes | The tags. | You can specify up to 20 tags. For more information, see Tags properties. |
|   | VpcIpv6Ci drBlock |   | String | No | No | The IPv6 CIDR block of the VPC. | None. |
|   |   | VpcIpv6Ci | String |   |   |   |   |
|   | drBlock |   |   |   |   |   |   |

| Ipv6CidrB | Int |
|---|---|

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The key cannot start with aliyun or acs: . |
| Value | String | No | No | The tag value. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The value cannot start with aliyun or acs: . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt CidrBlock: the CIDR block of the vSwitch. Ipv6CidrBlock: the IPv6 CIDR block of the vSwitch. VSwitchId: the ID of the vSwitch. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VSwitchZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": "The ID of the zone",
      "Label": {
        "en": "VSwitch Availability Zone"
  "Resources": {
    "EcsVSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "VpcId": {
          "Ref": "EcsVpc"
        "ZoneId": {
          "Ref": "VSwitchZoneId"
        "CidrBlock": "192.168.0.0/24"
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

`]` `]`

```json
  "Outputs": {
```

To view more examples, visit SnatEntry.json and SnatEntry.yml. In the examples, the ALIYUN::ECS::VPC, ALIYUN::ECS::VSwitch, ALIYUN::VPC::SnatEntry, ALIYUN::VPC::CommonBandwidthPackage, ALIYUN::VPC::CommonBandwidthPackageIp, ALIYUN::VPC::Ipv6Gateway, and ALIYUN::VPC::Ipv6InternetBandwidth resource types are used.

### 6.2 ESS

#### 6.2.1 ALIYUN::ESS::AlarmTask

ALIYUN::ESS::AlarmTask is used to create a metric-based alarm task. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Statistics | String | No | No | The method used to calculate monitoring data. The statistics must be appropriate for the metric chosen. | Valid values: Average, Minimum, and Maximum. Default value: Average. |
| Name | String | No | Yes | The name of the alarm rule. | None |
| EvaluationCount | Integer | No | No | The number of consecutive times that the threshold must be exceeded before an alarm is triggered. | Default value: 3. Minimum value: 1. |
| Period | Integer | No | No | The metric query period, which must be appropriate for the metric chosen. Unit: seconds. | Valid values: 60, 120, 300, and 900. Default value: 300. |
| MetricType | String | No | No | The metric type. | Valid values: system and custom. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ComparisonOper ator | String | No | No | The alarm comparison operator used to define a condition in the alarm rule. | Valid values: <=, <, >, and > =. |
| Dimensions | List | No | No | The list of instances associated with the alarm rule. | You must include at least one instance in the list. |
| ScalingGroupId | String | Yes | No | The ID of the scaling group. | None |
| AlarmAction | List | Yes | Yes | The list of alarm actions. | You must include one to five alarm actions in the list. |
| Threshold | Number | Yes | No | The alarm threshold, which must be a numeric value. | None |
| MetricName | String | Yes | No | The metric name of a service. For more information, see the metrics defined for each service. | None |
| GroupId | Integer | No | No | The group ID. | None |
| Description | String | No | Yes | The description of the alarm task. | None |

Dimensions syntax

```json
"Dimensions": [
    "DimensionKey": String,
    "DimensionValue": String
```

`]` Dimensions properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DimensionValue | String | Yes | No | None | None |
| DimensionKey | String | Yes | No | None | None |

Response parameters Fn::GetAtt AlarmTaskId: the ID of the alarm task. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "ComparisonOperator": {
      "Type": "String",
      "Description": "Comparison Operator",
      "AllowedValues": [
        ">=",
        "<=",
        ">",
        "<"
```

`]`

```json
    "Description": {
      "Type": "String",
      "Description": "Description"
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
    "MetricType": {
      "Type": "String",
      "Description": "Metric Type",
      "AllowedValues": [
        "system",
        "custom"
```

`]`

```json
    "EvaluationCount": {
      "Type": "Number",
      "Description": "Evaluation Count",
      "MinValue": 1
    "Period": {
      "Type": "Number",
      "Description": "Period",
      "AllowedValues": [
        60,
        120,
        300,
```

`]`

```json
    "Dimensions": {
      "Type": "CommaDelimitedList",
      "Description": "Dimensions",
      "MinLength": 1
    "Statistics": {
      "Type": "String",
      "Description": "Statistics",
      "AllowedValues": [
        "Average",
        "Minimum",
```

```
        "Maximum"
```

`]`

```json
    "Name": {
      "Type": "String",
      "Description": "Name"
    "GroupId": {
      "Type": "Number",
      "Description": "Group Id"
    "MetricName": {
      "Type": "String",
      "Description": "Metric Name"
    "AlarmAction": {
      "Type": "CommaDelimitedList",
      "Description": "Alarm Actions",
      "MinLength": 1,
      "MaxLength": 5
    "Threshold": {
      "Type": "Number",
      "Description": "Threshold"
  "Resources": {
    "AlarmTask": {
      "Type": "ALIYUN::ESS::AlarmTask",
      "Properties": {
        "ComparisonOperator": {
          "Ref": "ComparisonOperator"
        "Description": {
          "Ref": "Description"
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
        "MetricType": {
          "Ref": "MetricType"
        "EvaluationCount": {
          "Ref": "EvaluationCount"
        "Period": {
          "Ref": "Period"
        "Dimensions": {
          "Fn::Split": [
            ",",
              "Ref": "Dimensions"
              "Ref": "Dimensions"
```

`]` `]`

```json
        "Statistics": {
          "Ref": "Statistics"
        "Name": {
          "Ref": "Name"
        "GroupId": {
          "Ref": "GroupId"
        "MetricName": {
          "Ref": "MetricName"
        "AlarmAction": {
          "Fn::Split": [
            ",",
              "Ref": "AlarmAction"
              "Ref": "AlarmAction"
```

`]`

```json
        "Threshold": {
          "Ref": "Threshold"
  "Outputs": {
    "AlarmTaskId": {
      "Description": "The alarm task ID",
      "Value": {
        "Fn::GetAtt": [
          "AlarmTask",
          "AlarmTaskId"
```

`]`

#### 6.2.2 ALIYUN::ESS::AlarmTaskEnable

ALIYUN::ESS::AlarmTaskEnable is used to start an alarm task. You can call this operation to enable alarm tasks when the task is stopped. Statement

```json
  "Type": "ALIYUN::ESS::AlarmTaskEnable",
  "Properties": {
    "AlarmTaskId": String,
    "Enable": Boolean
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AlarmTaskId | String | No | No | The ID of the monitoring task. | None |
| Enable | String | Retained | Yes | Specifies whether to enable the alarm task. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt None Sample request

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

`]`

```json
    "AlarmTaskId": {
      "Type": "String",
      "Description": "The id of alarm task."
  "Resources": {
    "AlarmTaskEnable": {
      "Type": "ALIYUN::ESS::AlarmTaskEnable",
      "Properties": {
        "Enable": {
          "Ref": "Enable"
        "AlarmTaskId": {
          "Ref": "AlarmTaskId"
  "Outputs": {}
```

#### 6.2.3 ALIYUN::ESS::LifecycleHook

ALIYUN::ESS::LifecycleHook is used to create a lifecycle hook for a scaling group. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LifecycleHookNa me | String | No | Yes | The name of the lifecycle hook. Each lifecycle hook name must be unique within a scaling group. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. The default name is the ID of the lifecycle hook. |
| NotificationArn | String | No | Yes | The Alibaba Cloud Resource Name (ARN) of the notification target that Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. | This target can be either an MNS queue or an MNS topic. The format of the parameter value is acs:ess:{region}: {account-id}:{resource- relative-id}. region : the region where the scaling group resides. account-id : the ID of the Apsara Stack tenant account. Examples: MNS queue: acs:ess: {region}:{account- id}:queue/{queuenam e} MNS topic: acs:ess: {region}:{account- id}:topic/{topicname} |
| HeartbeatTimeo ut | Integer | No | Yes | The waiting period before the lifecycle hook times out. When the lifecycle hook times out, the scaling group performs the action specified by the DefaultResult parameter. Unit: seconds. | Valid values: 30 to 21600. Default value: 600. |

| Property | Type | Required |   | Editable | Description |   | Constraint |
|---|---|---|---|---|---|---|---|
| NotificationMeta data | String | No |   |   | The fixed string to include when Auto Scaling sends a notification about the wait state of a scaling activity. Auto Scaling sends the specified NotificationMetada |   | The parameter value cannot exceed 128 characters in length. |
|   |   |   |   |   |   | NotificationMetada |   |
|   |   |   |   | Yes | ta |   |   |
|   |   |   |   |   | ta |   |   |
| ScalingGroupId | String | Yes |   | No | The ID of the scaling group. |   | None |
| DefaultResult | String | No |   | Yes | The action that the scaling group takes when the lifecycle hook times out. If the scaling group has multiple lifecycle hooks and one of them is terminated when the DefaultResult parameter is set to ABANDON during a scale-in event, the remaining lifecycle hooks in the same scaling group will also be terminated. Otherwise, the scaling activity will proceed normally after the waiting period expires and continue with the action specified by the DefaultResult parameter. |   | Valid values: CONTINUE: The scaling group continues the scale- in or scale-out event. ABANDON: The scaling group releases the created ECS instances if the scaling activity type is scale-out or removes the ECS instances to be scaled in if the scaling activity type is scale-in. Default value: CONTINUE. |

| NotificationMetada |   |
|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LifecycleTransitio n | String | Yes | Yes | The type of scaling activity to which the lifecycle hook applies. | Valid values: SCALE OUT: scale- _ out events of the scaling group. SCALE IN: scale-in _ events of the scaling group. |

Response parameters Fn::GetAtt LifecycleHookId: the ID of the lifecycle hook. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LifecycleHookName": {
      "Type": "String",
      "Description": "The name of the lifecycle hook. Each name must be unique within a scaling g
roup. The name must be 2 to 40 characters in length and can contain letters, numbers, Chinese cha racters, and special characters including underscores (_), hyphens (-) and periods (.).\nDefault value: Lifecycle Hook ID",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    "NotificationArn": {
      "Type": "String",
      "Description": "The Alibaba Cloud Resource Name (ARN) of the notification target that Auto
Scaling will use to notify you when an instance is in the transition state for the lifecycle hook . This target can be either an MNS queue or an MNS topic. The format of the parameter value is ac s:ess:{region}:{account-id}:{resource-relative-id}.\nregion: the region to which the scaling grou p locates\naccount-id: Alibaba Cloud ID\nFor example:\nMNS queue: acs:ess:{region}:{account-id}:q ueue/{queuename}\nMNS topic: acs:ess:{region}:{account-id}:topic/{topicname}",
      "AllowedPattern": "^acs:ess:([a-zA-Z0-9-]+):(\\d+):(queue|topic)/([a-zA-Z0-9][a-zA-Z0-9-]{0
,255})$",
      "MaxLength": 300
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
    "LifecycleTransition": {
      "Type": "String",
      "Description": "The scaling activities to which lifecycle hooks apply Value range:\n SCALE_
OUT: scale-out event\n SCALE_IN: scale-in event",
      "AllowedValues": [
        "SCALE_OUT",
        "SCALE_IN"
```

`]`

```json
    "HeartbeatTimeout": {
      "Type": "Number",
"Description":"Thetime,inseconds,thatcanelapsebeforethelifecyclehooktimesout.
```

```json
      Description: The time, in seconds, that can elapse before the lifecycle hook times out.
If the lifecycle hook times out, the scaling group performs the default action (DefaultResult). T he range is from 30 to 21,600 seconds. The default value is 600 seconds.\nYou can prevent the lif ecycle hook from timing out by calling the RecordLifecycleActionHeartbeat operation. You can also terminate the lifecycle action by calling the CompleteLifecycleAction operation.",
      "MinValue": 30,
      "MaxValue": 21600
    "NotificationMetadata": {
      "Type": "String",
      "Description": "The fixed string that you want to include when Auto Scaling sends a message
about the wait state of the scaling activity to the notification target. The length of the parame ter can be up to 128 characters. Auto Scaling will send the specified NotificationMetadata parame ter along with the notification message so that you can easily categorize your notifications. The NotificationMetadata parameter will only take effect after you specify the NotificationArn parame ter.",
      "MaxLength": 128
    "DefaultResult": {
      "Type": "String",
      "Description": "The action that the scaling group takes when the lifecycle hook times out.
Value range:\n CONTINUE: the scaling group continues with the scale-in or scale-out process.\n AB ANDON: the scaling group stops any remaining action of the scale-in or scale-out event.\nDefault value: CONTINUE\nIf the scaling group has multiple lifecycle hooks and one of them is terminated by the DefaultResult=ABANDON parameter during a scale-in event (SCALE_IN), the remaining lifecycl e hooks under the same scaling group will also be terminated. Otherwise, the action following the wait state is the next action, as specified in the parameter DefaultResult, after the last lifecy cle event under the same scaling group.",
      "AllowedValues": [
        "CONTINUE",
        "ABANDON"
```

`]`

```json
  "Resources": {
    "LifecycleHook": {
      "Type": "ALIYUN::ESS::LifecycleHook",
      "Properties": {
        "LifecycleHookName": {
          "Ref": "LifecycleHookName"
        "NotificationArn": {
          "Ref": "NotificationArn"
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
        "LifecycleTransition": {
          "Ref": "LifecycleTransition"
        "HeartbeatTimeout": {
          "Ref": "HeartbeatTimeout"
        "NotificationMetadata": {
          "Ref": "NotificationMetadata"
        "DefaultResult": {
          "Ref": "DefaultResult"
```

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

#### 6.2.4 ALIYUN::ESS::ScalingConfiguration

ALIYUN::ESS::ScalingConfiguration is used to create a scaling configuration for a scaling group. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | Yes | True | The ID of the resource group to which the instance belongs. | None |
| DeploymentSetId | String | Yes | Released | The ID of the deployment set. | None |
| HpcClusterId | String | Yes | Released | The ID of the E-HPC cluster to which the instance belongs. | None |
| ScalingGroupId | String | No | No | The ID of the scaling group to which the scaling configuration belongs. | None |
| DiskMappings | List | No. | True | The disks to be attached to created instances. | A maximum of 16 disks can be attached to each instance. |
| InternetChargeTy pe | String | Yes | True | The billing method for Internet usage. | Valid values: PayByBandwidth PayByTraffic: pay-by- traffic Default value: PayByTraffic |
| InternetMaxBand widthIn | String | Optional | Released | The maximum inbound bandwidth from the Internet. | Unit: Mbit/s. Valid values: 1 to 100. Default value: 100 |
| InternetMaxBand widthOut | String | No. | True | The maximum outbound bandwidth to the Internet. | Valid values: Pay-by-bandwidth: 0 to 100. Default value: 0. Pay-by-data- transfer: 1 to 200. This parameter is required. Unit: Mbit/s. |
| InstanceId | String | Yes | Released | The instance ID of the scaling configuration. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SystemDiskCateg ory | String | Yes | True | The category of the system disk. | Valid values: cloud: indicates a basic disk. cloud efficiency: _ indicates an ultra disk. cloud ssd: indicates _ a standard SSD. ephemeral ssd: _ indicates a local SSD. cloud essd: _ enhanced SSD (ESSD) Default value: cloud for Generation I instance types that are not I/O optimized, default value: cloud efficiency. _ |
| ImageId | String | Yes | True | The ID of the image used to start the instance. You can use a public image, a custom image, or an Alibaba Cloud Marketplace image. | None |
| InstanceType | String | Yes | True | The specification of the instance. | None |
| SecurityGroupId | String | Yes | True | The ID of the security group to which the instance belongs. | None |
| IoOptimized | String | Yes | True | Specifies whether the created instances are I/O optimized. | Valid values: none (non-I/O optimized) optimized Default value: none. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingConfigura tionName | String | Yes | True | The name of the scaling configuration. | The name must be 2 to 64 characters in length. It can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. The name of the scaling configuration must be unique within a scaling group. If this parameter is not specified, the value of scalingconfigurationi d is used. |
| KeyPairName | String | Yes | True | The name of the key pair that is bound to the instance. | This parameter is ignored if the instance type is Windows and the default value is null. If the instance type is Linux, password logon is disabled by default. |
| RamRoleName | String | Yes | True | The RAM role name of the instance. | You can use RAM API ListRoles you can call this operation to query the RAM role name of an instance. |
| SystemDiskSize | String | No. | True | The size of the system disk. Unit: GB. | Valid values: 40 to 500. Unit: GB. If a custom image is used to create a system disk, the system disk size must be larger than the size of the custom image. |

| Parameter | Type | Required |   | Editable | Description |   | Constraint |   |
|---|---|---|---|---|---|---|---|---|
| UserData | String | Yes |   | True | The user data that you pass when you create the instance. |   | The user can encode up to 16KB in size. You do not need to perform Base64 encoding. Special characters must be escaped with a backslash (\). |   |
| InstanceTypes | List | No. |   | True | The instance types from which ECS instances can be created. If you specify InstanceTypes, InstanceType is invalid. |   | Up to 10 instance types can be configured in a scaling configuration. The priority of each instance type is decreased in the order of its list elements. Auto Scaling creates instances in order of priority. If an instance of the highest priority type cannot be created, Auto Scaling will create an instance of the next highest priority type. |   |
| PasswordInherit | Boolean | No. |   | True | Specifies whether to use the preconfigured password of the specified image. |   | To use this parameter, ensure that a password is configured for the specified image. |   |
| TagList | List | No. |   |   |   |   | Tags must be specified as key-value pairs. You can specify a maximum of five Tag groups in the format of {"key1": "value1", |   |
|   |   |   |   |   |   |   |   | {"key1": "value1", |
|   |   |   |   |   |   |   | "key2": "value2", |   |
|   |   |   |   |   |   |   | ... "key5": |   |
|   |   |   |   |   | The tags of the |   | "value5"} |   |
|   |   |   |   | True | instance. |   |   |   |

| Parameter |   | Type | Required |   |   | Editable | Description |   |   | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SpotStrategy |   | String | Yes |   |   | True | The preemption policy for pay-as-you-go instances. |   |   | Valid values: NoSpot (pay-as-you- go instance) SpotWithPriceLimit (a preemptible instance with a maximum price) SpotAsPriceGo (the SpotAsPriceGo parameter that is set automatically based on the actual market price.) Default value: NoSpot. |   |
| InstanceName |   | String | Yes |   |   | True | The name of the instance created based on the current scaling configuration. |   |   | None |   |
| SpotPriceLimit |   | Number | No. |   |   | True | The maximum hourly price of the instance. |   |   | A maximum of three decimal places can be specified. This parameter takes effect only when the SpotStrategy parameter is set to SpotWithPriceLimit. The value of this parameter can be overwritten by the value of the SpotPriceLimitForInstan ceType parameter. |   |
| SpotPriceLimitFo rInstanceType |   |   |   |   |   |   |   |   |   | The format is {" |   |
|   |   |   |   |   |   |   |   |   |   |   | {" |
|   |   |   |   |   |   |   |   |   |   | <instance type 1>": _ _ |   |
|   |   |   |   |   |   |   |   |   |   | <price limit 1>, _ _ |   |
|   |   |   |   |   |   |   |   |   |   | ..., {" |   |
|   |   |   |   |   |   |   |   |   |   | <instance type 10>": _ _ |   |
|   |   |   |   |   |   |   | Preemptible instance |   |   | <price limit 10>} _ _ |   |
|   |   | Map | No. |   |   | True | type and bid of the instance. |   |   |   |   |
| SystemDiskAutoS napshotPolicyId |   | String | Yes |   |   | True | The ID of the automatic snapshot policy applied to the data disk. |   |   | None |   |

DiskMappings syntax

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

`]` DiskMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | No | No | The size of the data disk. | Valid values: cloud: 5 to 2000 cloud efficiency: 20 to _ 32768 cloud ssd: 20 to 32768 _ cloud essd: 20 to _ 32768. ephemeral ssd: 5 to _ 800 The value of this parameter must be greater than or equal to that of the snapshot specified by SnapshotId. Unit: GiB. |
| Category | String | Yes | Released | The type of the data disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, _ ephemeral ssd, and _ cloud essd. For I/O _ optimized instances, the default value is cloud efficiency. For non- _ I/O optimized instances, the default value is cloud. |
| DiskName | String | Yes | Released | The name of the data disk. | The name must be 2 to 128 characters in length It can contain letters, digits, colons (:), underscores ( ), and hyphens (-). It _ must start with a letter and cannot start with http:// or https:// the beginning. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the data disk. | The description must be 2 to 256 characters in length. Cannot http:// or https:// the beginning. |
| Device | String | Yes | Released | The device name of the data disk. | By default, the system automatically assigns a value for this parameter when the ECS instance is created. The value starts from /dev/xvdb and ends at /dev/xvdz. |
| SnapshotI d | String | Yes | Released | The ID of the snapshot used to create the data disk. | If this parameter is specified, the Size parameter will be ignored, and the Size of the created disk will be the Size of the specified snapshot. If the snapshot was created on or before July 15, 2013, calling the snapshot is denied and InvalidSnapshot.TooOld is displayed in the response parameter. |
| Encrypted | String | Yes | Released | Specifies whether to encrypt the data disk. | Default value: false. |
| KMSKeyId | String | Yes | Released | The KMS key ID for data disk N. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt ScalingConfigurationId: the ID of the scaling configuration. This ID is a globally unique identifier (GUID) generated by the system. Sample request

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
            "Category": "cloud",
            "Size": 10
```

`]`

```json
  "Outputs": {
    "ScalingConfiguration": {
      "Value": {"get_attr": ["ScalingConfigurationId"]}
```

#### 6.2.5 ALIYUN::ESS::ScalingGroup

ALIYUN::ESS::ScalingGroup is used to create a scaling group. A scaling group is a group of ECS instances that are dynamically scaled based on the configured scenario. A scaling group does not take effect immediately after it is created. You must use ALIYUN::ESS::ScalingGroupEnable to enable the scaling group to trigger scaling rules and execute scaling activities. Syntax

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
    "Tags": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MinSize | Integer | Yes | Yes | The minimum number of ECS instances in the scaling group. | Valid values: 0 to 1000. When the number of ECS instances in the scaling group is smaller than the value of MinSize, Auto Scaling creates ECS instances till the number of instances is equal to the MinSize value. |
| MaxSize | Integer | Yes | Yes | The maximum number of ECS instances in the scaling group. | Valid values: 0 to 1000. When the number of ECS instances in the scaling group is greater than the MaxSize value, Auto Scaling removes ECS instances from the scaling group till the number of instances is equal to the MaxSize value. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingGroup Name | String | No | Yes | The display name of the scaling group. | The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It must start with a letter or digit. The name must be unique to an Alibaba Cloud account within a region. The default value is the ID of the scaling group. |
| LaunchTemp lateId | String | No | Yes | The ID of the instance launch template from which the scaling group obtains launch configuratio ns. | None |
| LaunchTemp lateVersion | String | No | Yes | The version of the instance launch template. | Valid values: The fixed template version number. Default: The default template version is always used. Latest: The latest template version is always used. |
| RemovalPolic ys | List | No | Yes | The policies that are used to remove ECS instances from the scaling group. | Default value: OldestScalingConfiguration or OldestInstance. Valid values: OldestInstance: removes the ECS instance that is added to the scaling group at the earliest point in time. NewestInstance: removes the ECS instance that is added to the scaling group at the latest point in time. OldestScalingConfiguration : removes the ECS instance that is created based on the earliest scaling configuration. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VSwitchId | String | No | No | The ID of the vSwitch. | None |
| LoadBalance rIds | List | No | Yes | The ID of the Server Load Balancer (SLB) instance. | This value can be a JSON array that consists of up to five SLB instance IDs. Separate multiple IDs with commas (,). |
| DefaultCoold own | Integer | No | Yes | The cooldown time after a scaling activity (adding or removing ECS instances) is executed. | Valid values: 0 to 86400. Unit: seconds. Default value: 300. During the cooldown time, the scaling group executes only scaling activities that are triggered by CloudMonitor event-triggered tasks. |
| DBInstanceId s | List | No | Yes | The IDs of ApsaraDB RDS instances. | This value can be a JSON array that contains up to eight ApsaraDB RDS instance IDs. Separate multiple IDs with commas (,). |
| VSwitchIds | List | No | No | The IDs of vSwitches. | You can specify up to five vSwitch IDs. If you specify this parameter, the VSwitchId parameter is ignored. vSwitches are sorted in descending order of priority. When an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, the system uses the vSwitch that has the next highest priority to create the instance. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MultiAZPolicy | String | No | No | The ECS instance scaling policy for the multi- zone scaling group. | Valid values: PRIORITY: ECS instances are scaled based on the specified vSwitch. When an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, the system uses the vSwitch that has the next highest priority to create the instance. BALANCE: ECS instances are evenly distributed in multiple zones specified in the scaling group. COST OPTIMIZED: ECS _ instances are created based on the unit price of vCPUs, from low to high. Preemptible instances are created first when preemptible instance types are specified for the scaling configuration. Pay- as-you-go instances are created when no preemptible instances are available due to issues such as insufficient ECS resources. |
| NotificationC onfiguration s | List | No | Yes | The notification configuratio ns for event and resource changes. | For more information, see the NotificationConfigurations properties section in this topic. |
| ProtectedIns tances | List | No | Yes | The number of protected ECS instances in the scaling group. | Maximum value: 1000. |
| StandbyInsta nces | List | No | Yes | The number of ECS instances that are in the standby state in the scaling group. | Maximum value: 1000. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HealthCheck Type | String | No | Yes | The health check type. | Valid values: ECS NONE |
| GroupDeletio nProtection | Boolean | No | Yes | Specifies whether to enable deletion protection for the scaling group. | Default value: false. Valid values: true: Deletion protection is enabled for the scaling group. In this case, you cannot delete the scaling group. false: Deletion protection is disabled for the scaling group. |
| DesiredCapa city | Integer | No | Yes | The expected number of ECS instances in the scaling group. The scaling group automaticall y keeps the number of ECS instances at the expected value. | The expected number must be greater than or equal to the value of MinSize and less than or equal to the value of MaxSize. |
| InstanceId | String | No | No | The ID of the ECS instance from which the scaling group obtains configuratio n information to create scaling configuratio ns. | None |
| Tags | List | No | Yes | The tags of the scaling group. | A maximum of 20 tags can be specified. For more information, see the Tags properties section in this topic. |

NotificationConfigurations syntax

```json
"NotificationConfigurations": [
    "NotificationArn": String,
    "NotificationTypes": List
```

`]` NotificationConfigurations properties

| Property | Type | Required |   |   | Editable | Description |   |   | Constraint |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NotificationA rn | String | Yes |   |   |   | The Alibaba Cloud Resource Name (ARN) of the notification object that Auto Scaling uses to notify you |   |   | Format: MNS queue: acs:ess:{r |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | acs:ess:{r |   |   |
|   |   |   |   |   |   |   |   | you | egion}:{account-id}:que |   |   |   |   |
|   |   |   |   |   | No | when an |   |   | ue/{queuename} |   |   |   |   |
|   |   |   |   |   |   | instance is in the |   |   | MNS topic: | acs:ess:{re |   |   |   |
|   |   |   |   |   |   |   |   |   | gion}:{account-id}:topi |   |   |   |   |
|   |   |   |   |   |   | transition state for the |   |   | c/{topicname} |   |   |   |   |
|   |   |   |   |   |   | lifecycle hook. This object can be an MNS queue or an MNS topic. |   |   |   |   |   |   |   |
| NotificationT ypes | List | Yes |   |   | No | The types of the notification configuratio ns for ESS events and resource changes. |   |   | None |   |   |   |   |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

Response parameters Fn::GetAtt ScalingGroupId: the ID of the scaling group. ScalingGroupName: the name of the scaling group. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "The ID of the ECS instance from which the scaling group obtains configurati
on information of the specified instance."
    "VSwitchIds": {
      "Type": "CommaDelimitedList",
      "Description": "Parameter VSwitchIds.N is used to create instance in multiple zones. Parame
ter VSwitchIds.N has a priority over parameter VSwitchId.\nThe valid range of N is [1, 5], and yo u can specify at most 5 VSwitches in a VPC.\nThe priority of VSwitches descends from 1 to 5, and 1 indicates the highest priority.\nWhen you fail to create an instance in the zone to which a spe cified VSwitch belongs, another VSwitch with less priority replaces the specified one automatical ly.",
      "MinLength": 0,
      "MaxLength": 5
    "NotificationConfigurations": {
      "Type": "Json",
      "Description": "When a scaling event occurs in a scaling group, ESS will send a notificatio
n to Cloud Monitor or MNS."
    "VSwitchId": {
      "Type": "String",
      "Description": "If you create a VPC scaling group, you must specify the ID of a VSwitch."
    "LoadBalancerIds": {
      "Type": "CommaDelimitedList",
```

```json
      "Description": "ID list of a Server Load Balancer instance. A Json Array with format: [ \"l
b-id0\", \"lb-id1\", ... \"lb-idz\" ], support up to 100 Load Balancer instance.",
      "MaxLength": 100
    "DesiredCapacity": {
      "Type": "Number",
      "Description": "The expected number of ECS instances in a scaling group. The scaling group
automatically keeps the number of ECS instances as expected. The number of ECS instances cannot b e greater than the value of MaxSize and cannot be less than the value of MinSize."
    "GroupDeletionProtection": {
      "Type": "Boolean",
      "Description": "Whether to enable deletion protection for scaling group.\nDefault to False.
```

`",`

```json
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "LaunchTemplateId": {
      "Type": "String",
      "Description": "The ID of the instance launch template from which the scaling group obtains
launch configurations."
    "MaxSize": {
      "Type": "Number",
      "Description": "Maximum number of ECS instances in the scaling group. Value range: [0, 1000
].",
      "MinValue": 0,
      "MaxValue": 1000
    "ScalingGroupName": {
      "Type": "String",
      "Description": "Name shown for the scaling group, which must contain 2-40 characters (Engli
sh or Chinese). The name must begin with a number, an upper/lower-case letter or a Chinese charac ter and may contain numbers, \"_\", \"-\" or \".\". The account name is unique in the same region .\nIf this parameter is not specified, the default value is ScalingGroupId.",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    "MinSize": {
      "Type": "Number",
      "Description": "Minimum number of ECS instances in the scaling group. Value range: [0, 1000
].",
      "MinValue": 0,
      "MaxValue": 1000
    "DefaultCooldown": {
      "Type": "Number",
      "Description": "Default cool-down time (in seconds) of the scaling group. Value range: [0,
86400].\nThe default value is 300s.",
      "MinValue": 0,
      "MaxValue": 86400
    "StandbyInstances": {
```

`"` `"` `"C`

```
lii
```

`d``i` `"`

```json
      "Type": "CommaDelimitedList",
      "Description": "ECS instances of standby mode in the scaling group.",
      "MaxLength": 1000
    "LaunchTemplateVersion": {
      "Type": "String",
      "Description": "The version of the instance launch template. Valid values:\nA fixed templat
e version numbe.\nDefault: The default template version is always used.\nLatest: The latest templ ate version is always used."
    "MultiAZPolicy": {
      "Type": "String",
      "Description": "ECS scaling strategy for multi availability zone. Allow value:\n1. PRIORITY
: scaling the capacity according to the virtual switch (VSwitchIds.N) you define. ECS instances a re automatically created using the next priority virtual switch when the higher priority virtual switch cannot be created in the available zone.\n2. BALANCE: evenly allocate ECS instances betwee n the multiple available zone specified by the scaling group.",
      "AllowedValues": [
        "PRIORITY",
        "BALANCE"
```

`]`

```json
    "RemovalPolicys": {
      "Type": "CommaDelimitedList",
      "AllowedValues": [
        "OldestScalingConfiguration",
        "OldestInstance",
        "NewestInstance"
```

`],`

```json
      "Description": "Policy for removing ECS instances from the scaling group.\nOptional values:
\nOldestInstance: removes the first ECS instance attached to the scaling group.\nNewestInstance: removes the first ECS instance attached to the scaling group.\nOldestScalingConfiguration: remove s the ECS instance with the oldest scaling configuration.\nDefault values: OldestScalingConfigura tion and OldestInstance. You can enter up to two removal policies.",
      "MaxLength": 2
    "ProtectedInstances": {
      "Type": "CommaDelimitedList",
      "Description": "ECS instances of protected mode in the scaling group.",
      "MaxLength": 1000
    "DBInstanceIds": {
      "Type": "CommaDelimitedList",
      "Description": "ID list of an RDS instance. A Json Array with format: [ \"rm-id0\", \"rm-id
1\", ... \"rm-idz\" ], support up to 100 RDS instance.",
      "MaxLength": 100
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "HealthCheckType": {
      "Type": "String",
      "Description": "The health check type. Allow values is \"ECS\" and \"NONE\", default to \"E
CS\".", "AllowedValues":[
```

```
      AllowedValues: [
        "ECS",
        "NONE"
```

`]`

```json
  "Resources": {
    "ScalingGroup": {
      "Type": "ALIYUN::ESS::ScalingGroup",
      "Properties": {
        "InstanceId": {
          "Ref": "InstanceId"
        "VSwitchIds": {
          "Ref": "VSwitchIds"
        "NotificationConfigurations": {
          "Ref": "NotificationConfigurations"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "LoadBalancerIds": {
          "Ref": "LoadBalancerIds"
        "DesiredCapacity": {
          "Ref": "DesiredCapacity"
        "GroupDeletionProtection": {
          "Ref": "GroupDeletionProtection"
        "LaunchTemplateId": {
          "Ref": "LaunchTemplateId"
        "MaxSize": {
          "Ref": "MaxSize"
        "ScalingGroupName": {
          "Ref": "ScalingGroupName"
        "MinSize": {
          "Ref": "MinSize"
        "DefaultCooldown": {
          "Ref": "DefaultCooldown"
        "StandbyInstances": {
          "Ref": "StandbyInstances"
        "LaunchTemplateVersion": {
          "Ref": "LaunchTemplateVersion"
        "MultiAZPolicy": {
          "Ref": "MultiAZPolicy"
        "RemovalPolicys": {
          "Ref": "RemovalPolicys"
```

```json
        "ProtectedInstances": {
          "Ref": "ProtectedInstances"
        "DBInstanceIds": {
          "Ref": "DBInstanceIds"
        "Tags": {
          "Ref": "Tags"
        "HealthCheckType": {
          "Ref": "HealthCheckType"
  "Outputs": {
    "ScalingGroupId": {
      "Description": "Scaling group Id",
      "Value": {
        "Fn::GetAtt": [
          "ScalingGroup",
          "ScalingGroupId"
```

`]`

```json
    "ScalingGroupName": {
      "Description": "Scaling group name",
      "Value": {
        "Fn::GetAtt": [
          "ScalingGroup",
          "ScalingGroupName"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  DBInstanceIds:
    Description: 'ID list of an RDS instance. A Json Array with format: [ "rm-id0",
      "rm-id1", ... "rm-idz" ], support up to 100 RDS instance.'
    MaxLength: 100
    Type: CommaDelimitedList
  DefaultCooldown:
    Description: 'Default cool-down time (in seconds) of the scaling group. Value
      range: [0, 86400].
      The default value is 300s.'
    MaxValue: 86400
    MinValue: 0
    Type: Number
  DesiredCapacity:
    Description: The expected number of ECS instances in a scaling group. The scaling
      group automatically keeps the number of ECS instances as expected. The number
ofECSinstancescannotbegreaterthanthevalueofMaxSizeandcannotbeless
```

```json
      of ECS instances cannot be greater than the value of MaxSize and cannot be less
      than the value of MinSize.
    Type: Number
  GroupDeletionProtection:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Default: false
    Description: 'Whether to enable deletion protection for scaling group.
      Default to False.'
    Type: Boolean
  HealthCheckType:
    AllowedValues:
    - ECS
    - NONE
    Description: The health check type. Allow values is "ECS" and "NONE", default
      to "ECS".
    Type: String
  InstanceId:
    Description: The ID of the ECS instance from which the scaling group obtains configuration
      information of the specified instance.
    Type: String
  LaunchTemplateId:
    Description: The ID of the instance launch template from which the scaling group
      obtains launch configurations.
    Type: String
  LaunchTemplateVersion:
    Description: 'The version of the instance launch template. Valid values:
      A fixed template version numbe.
      Default: The default template version is always used.
      Latest: The latest template version is always used.'
    Type: String
  LoadBalancerIds:
    Description: 'ID list of a Server Load Balancer instance. A Json Array with format:
      [ "lb-id0", "lb-id1", ... "lb-idz" ], support up to 100 Load Balancer instance.'
    MaxLength: 100
    Type: CommaDelimitedList
  MaxSize:
    Description: 'Maximum number of ECS instances in the scaling group. Value range:
      [0, 1000].'
    MaxValue: 1000
    MinValue: 0
    Type: Number
  MinSize:
    Description: 'Minimum number of ECS instances in the scaling group. Value range:
      [0, 1000].'
    MaxValue: 1000
    MinValue: 0
    Type: Number
  MultiAZPolicy:
    AllowedValues:
    - PRIORITY
    - BALANCE
    Description: 'ECS scaling strategy for multi availability zone. Allow value:
      1. PRIORITY: scaling the capacity according to the virtual switch (VSwitchIds.N)
      you define. ECS instances are automatically created using the next priority
```

```
      virtual switch when the higher priority virtual switch cannot be created in
      the available zone.
      2. BALANCE: evenly allocate ECS instances between the multiple available zone
      specified by the scaling group.'
    Type: String
  NotificationConfigurations:
    Description: When a scaling event occurs in a scaling group, ESS will send a notification
      to Cloud Monitor or MNS.
    Type: Json
  ProtectedInstances:
    Description: ECS instances of protected mode in the scaling group.
    MaxLength: 1000
    Type: CommaDelimitedList
  RemovalPolicys:
    AllowedValues:
    - OldestScalingConfiguration
    - OldestInstance
    - NewestInstance
    Description: 'Policy for removing ECS instances from the scaling group.
      Optional values:
      OldestInstance: removes the first ECS instance attached to the scaling group.
      NewestInstance: removes the first ECS instance attached to the scaling group.
      OldestScalingConfiguration: removes the ECS instance with the oldest scaling
      configuration.
      Default values: OldestScalingConfiguration and OldestInstance. You can enter
      up to two removal policies.'
    MaxLength: 2
    Type: CommaDelimitedList
  ScalingGroupName:
    AllowedPattern: ^[a-zA-Z0-9\u4e00-\u9fa5][-_.a-zA-Z0-9\u4e00-\u9fa5]{1,63}$
    Description: 'Name shown for the scaling group, which must contain 2-40 characters
      (English or Chinese). The name must begin with a number, an upper/lower-case
      letter or a Chinese character and may contain numbers, "_", "-" or ".". The
      account name is unique in the same region.
      If this parameter is not specified, the default value is ScalingGroupId.'
    Type: String
  StandbyInstances:
    Description: ECS instances of standby mode in the scaling group.
    MaxLength: 1000
    Type: CommaDelimitedList
  Tags:
    Description: Tags to attach to instance. Max support 20 tags to add during create
      instance. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
  VSwitchId:
    Description: If you create a VPC scaling group, you must specify the ID of a VSwitch.
    Type: String
  VSwitchIds:
    Description: 'Parameter VSwitchIds.N is used to create instance in multiple zones.
      Parameter VSwitchIds.N has a priority over parameter VSwitchId.
      The valid range of N is [1, 5], and you can specify at most 5 VSwitches in a
      VPC.
      The priority of VSwitches descends from 1 to 5, and 1 indicates the highest
      priority.
      When you fail to create an instance in the zone to which a specified VSwitch
      belongs, another VSwitch with less priority replaces the specified one automatically.'
```

```
    MaxLength: 5
    MinLength: 0
    Type: CommaDelimitedList
Resources:
  ScalingGroup:
    Properties:
      DBInstanceIds:
        Ref: DBInstanceIds
      DefaultCooldown:
        Ref: DefaultCooldown
      DesiredCapacity:
        Ref: DesiredCapacity
      GroupDeletionProtection:
        Ref: GroupDeletionProtection
      HealthCheckType:
        Ref: HealthCheckType
      InstanceId:
        Ref: InstanceId
      LaunchTemplateId:
        Ref: LaunchTemplateId
      LaunchTemplateVersion:
        Ref: LaunchTemplateVersion
      LoadBalancerIds:
        Ref: LoadBalancerIds
      MaxSize:
        Ref: MaxSize
      MinSize:
        Ref: MinSize
      MultiAZPolicy:
        Ref: MultiAZPolicy
      NotificationConfigurations:
        Ref: NotificationConfigurations
      ProtectedInstances:
        Ref: ProtectedInstances
      RemovalPolicys:
        Ref: RemovalPolicys
      ScalingGroupName:
        Ref: ScalingGroupName
      StandbyInstances:
        Ref: StandbyInstances
      Tags:
        Ref: Tags
      VSwitchId:
        Ref: VSwitchId
      VSwitchIds:
        Ref: VSwitchIds
    Type: ALIYUN::ESS::ScalingGroup
Outputs:
  ScalingGroupId:
    Description: Scaling group Id
    Value:
      Fn::GetAtt:
      - ScalingGroup
      - ScalingGroupId
  ScalingGroupName:
    Description: Scaling group name
    Value:
Fn::GetAtt:
```

```
      Fn::GetAtt:
      - ScalingGroup
      - ScalingGroupName
```

For more examples, visit ScalingGroup.json and ScalingGroup.yml. In the examples, the ALIYUN::ESS::ScalingGroup, ALIYUN::ESS::ScalingRule, ALIYUN::ESS::AlarmTask, ALIYUN::ESS::AlarmTaskEnable, ALIYUN::ESS::LifecycleHook, and ALIYUN::ESS::ScheduledTask resource types are involved.

#### 6.2.6 ALIYUN::ESS::ScalingGroupEnable

ALIYUN::ESS::ScalingGroupEnable is used to enable a scaling group. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingGroupId | String | Yes | No | The ID of the scaling group. | None |
| ScalingConfigur ationId | String | No | No | The ID of the scaling configuration to be activated in the scaling group. | None |
| InstanceIds | List | No | Yes | The IDs of ECS instances to be added to the enabled scaling group. | A maximum of 20 instance IDs can be specified. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingRuleArisE xecuteVersion | Integer | No | Yes | The version of the identifier for the scaling rule to be executed. If you change this property, all scaling rules specified by ScalingRuleAris will be executed once. | Minimum value: 0. |
| ScalingRuleAris | List | No | Yes | The unique identifiers of scaling rules in the scaling group. Invalid unique identifiers are not displayed in the query results and no errors are reported. | A maximum of 10 scaling rule identifiers can be specified. |
| RemoveInstanc eIds | List | No | Yes | The IDs of ECS instances to be deleted. | A maximum of 1,000 instance IDs can be specified. |

Response parameters Fn::GetAtt LifecycleState: the status of the scaling group. ScalingInstances: the instances that are automatically created in the scaling group. ScalingGroupId: the ID of the scaling group. ScalingRuleArisExecuteResultInstancesRemoved: the instances that are removed from the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultNumberOfAddedInstances: the number of instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingInstanceDetails: the instance scaling details. ScalingRuleArisExecuteErrorInfo: the error information about the execution of the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultInstancesAdded: the instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingGroupEnable": {
      "Type": "ALIYUN::ESS::ScalingGroupEnable",
      "Properties": {
        "ScalingGroupId": "r0HUqbJ411cc2eQw8bU****",
        "ScalingConfigurationId": "bJlLfdexm77Ldsyptmel****",
        "InstanceIds": "",
  "Outputs": {
    "ScalingGroupEnable": {
      "Value": {"Fn::GetAtt": ["ScalingGroupEnable", "LifecycleState"]}
```

#### 6.2.7 ALIYUN::ESS::ScalingRule

ALIYUN::ESS::ScalingRule is used to create a scaling rule. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AdjustmentVa lue | Integer | No | Yes | The number of ECS instances to increase or decrease when scaling occurs. This parameter takes effect only when the ScalingRuleTy pe parameter is set to SimpleScaling Rule or StepScalingRu le. | Valid values based on the AdjustmentType value: Valid values when the AdjustmentType parameter is set to QuantityChangeInCa pacity: -500 to 500 Valid values when the AdjustmentType parameter is set to PercentChangeInCap acity: - 100 to 10000 Valid values when the AdjustmentType parameter is set to TotalCapacity: 0 to 1000 Not e The number of ECS instances to be adjusted in a single scaling activity cannot exceed 500. |
| Cooldown | Integer | No | Yes | The cooldown period of the scaling rule. This parameter takes effect only when the ScalingRuleTy pe parameter is set to SimpleScaling Rule. | Valid values: 0 to 86400. Unit: seconds. This parameter is empty by default. |
| ScalingGroupI d | String | Yes | No | The ID of the scaling group to which the scaling rule belongs. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AdjustmentTy pe | String | No | Yes | The adjustment method of the scaling rule. This parameter takes effect only when the ScalingRuleTy pe parameter is set to SimpleScaling Rule or StepScalingRu le. | Valid values: QuantityChangeInCa pacity: increases or decreases the specified number of ECS instances in a scaling group. PercentChangeInCap acity: increases or decreases the specified percentage of ECS instances in a scaling group. TotalCapacity: increases or decreases the number of ECS instances in a scaling group by or to a specific number. |
| ScalingRuleNa me | String | No | Yes | The name of the scaling rule. | The name must be 2 to 64 characters in length and can contain digits, letters, underscores ( ), hyphens (-), and _ periods (.). It must start with a digit or letter. If this parameter is not specified, the ScalingRuleId value is used by default. |
|   |   |   |   |   | Valid values when the ScalingRuleType parameter is set to TargetTrackingScalin gRule: CpuUtilization: the average CPU utilization ClassicInternetRx: the average Internet inbound traffic over the classic network ClassicInternetTx: the average Internet outbound traffic over the classic network |

| Property | Type | Required | Editable | TDheescription predefined | VpcInternetRx: Constraint the average |
|---|---|---|---|---|---|
|   |   |   |   | metric to monitor. This parameter is required and applicable | Internet inbound traffic over the VPC VpcInternetTx: the average |
| MetricName | String | No | No | only when the ScalingRuleTy pe parameter is set to TargetTrackin gScalingRule or PredictiveScali ngRule. | Internet outbound traffic over the VPC IntranetRx: the average inbound traffic over the internal network IntranetTx: the average outbound traffic over the internal network Valid values when the ScalingRuleType parameter is set to PredictiveScalingRule : CpuUtilization: the average CPU utilization IntranetRx: the average inbound traffic over the internal network IntranetTx: the average outbound traffic over the internal network |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PredictiveTask BufferTime | Integer | No | No | The buffer period ahead of the prediction task execution time. By default, all scheduled tasks that are automatically created for a predictive scaling rule are executed on the hour. You can set a buffer period to execute prediction tasks ahead of schedule, so that resources can be prepared in advance. | Valid values: 0 to 60. Unit: minutes. Default value: 0. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingRuleTy pe | String | No | No | The type of the scaling rule. | Default value: SimpleScalingRule. Valid values: SimpleScalingRule: scales ECS instances based on the values of AdjustmentType and AdjustmentValue. TargetTrackingScalin gRule: dynamically calculates the number of ECS instances to be scaled and tries to keep the value of a predefined metric close to TargetValue. StepScalingRule: scales ECS instances in steps based on specified thresholds and metric values. PredictiveScalingRule : uses machine learning to analyze historical monitoring data of the scaling group and predict the future values of metrics. The rule then automatically creates scheduled tasks to set the boundary values for the scaling group. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PredictiveValu eBuffer | Integer | No | No | The ratio of the increment to the predicted value when PredictiveValu eBehavior is set to PredictiveValu eOverrideMax WithBuffer. If the predicted value increased by this ratio is greater than the initial maximum capacity, the value after the increase is used as the maximum value for prediction tasks. | Valid values: 0 to 100. Default value: 0. |
| TargetValue | Number | No | No | The metric value that you expect. This parameter takes effect only when the ScalingRuleTy pe parameter is set to TargetTrackin gScalingRule or PredictiveScali ngRule. | The value must be greater than 0 and can have a maximum of three decimal places. |
| StepAdjustme nt | List | No | No | The step adjustments for step scaling. | For more information, see StepAdjustment properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PredictiveValu eBehavior | String | No | No | The action taken on the predicted maximum value. | Default value: MaxOverridePredictiveV alue. Valid values: MaxOverridePredictiv eValue: uses the initial maximum capacity as the maximum value for prediction tasks when the predicted value is greater than the initial maximum capacity. PredictiveValueOverri deMax: uses the predicted value as the maximum value for prediction tasks when the predicted value is greater than the initial maximum capacity. PredictiveValueOverri deMaxWithBuffer: increases the predicted value by a ratio, which is specified by PredictiveValueBuffe r. If the value after the increase is greater than the initial maximum capacity, the value after the increase is used as the maximum value for prediction tasks. |
| DisableScaleIn | Boolean | No | No | Specifies whether to disable scale- in. This parameter takes effect only when the ScalingRuleTy pe parameter is set to TargetTrackin gScalingRule. | Default value: false. Valid values: true false |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InitialMaxSize | Integer | No | No | The maximum number of ECS instances in the scaling group, which is used together with the PredictiveValu eBehavior parameter. | The default value of this parameter is the value of MaxSize. |
| MinAdjustmen tMagnitude | Integer | No | No | The minimum number of ECS instances to be adjusted in the scaling rule. | This parameter takes effect only when the ScalingRuleType parameter is set to SimpleScalingRule or StepScalingRule, and the AdjustmentType parameter is set to PercentChangeInCapaci ty. |
| EstimatedInst anceWarmup | Integer | No | No | The warm-up period of the ECS instances. This parameter takes effect only when the ScalingRuleTy pe parameter is set to TargetTrackin gScalingRule or StepScalingRu le. | Valid values: 0 to 86400. Unit: seconds. Default value: 300. The system adds ECS instances that are in the warm-up state to the scaling group, but does not report monitoring data to Cloud Monitor during the warm-up period. Not e When the system calculates the number of ECS instances to be adjusted, the system does not count ECS instances in the warm-up state as part of the current capacity of the scaling group. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PredictiveScali ngMode | String | No | No | The mode of the predictive scaling rule. | Default value: PredictAndScale. Valid values: PredictAndScale: generates predicted results and creates prediction tasks. PredictOnly: generates predicted results but does not create prediction tasks. |

StepAdjustment syntax

```json
"StepAdjustment": [
    "MetricIntervalUpperBound": Number,
    "ScalingAdjustment": Integer,
    "MetricIntervalLowerBound": Number
```

`]` StepAdjustment properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MetricInterval UpperBound | Number | No | No | The upper limit value specified in the step adjustment. This parameter takes effect only when the ScalingRuleTy pe parameter is set to StepScalingRu le. | Valid values: - 9.999999E18 to 9.999999E18 |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingAdjust ment | Integer | No | No | The specified number of ECS instances to be adjusted in the step adjustment. This parameter takes effect only when the ScalingRuleTy pe parameter is set to StepScalingRu le. | None |
| MetricIntervalL owerBound | Number | No | No | The lower limit value specified in the step adjustment. This parameter takes effect only when the ScalingRuleTy pe parameter is set to StepScalingRu le. | Valid values: - 9.999999E18 to 9.999999E18 |

Response parameters Fn::GetAtt ScalingRuleAri: the unique identifier of the scaling rule. ScalingRuleId: the ID of the scaling rule. This ID is a globally unique identifier (GUID) generated by the system. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "TargetValue": {
      "Type": "Number",
      "Description": "The target value of a metric. This parameter is required and applicable onl
y to target tracking scaling rules and predictive scaling rules. The value of TargetValue must be greater than 0 and can have a maximum of three decimal places."
    "Cooldown": {
      "Type": "Number",
      "Description": "Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The
defaultvalueisempty",
```

```json
default value is empty.,
      "MinValue": 0,
      "MaxValue": 86400
    "ScalingGroupId": {
      "Type": "String",
      "Description": "ID of the scaling group of a scaling rule."
    "PredictiveValueBehavior": {
      "Type": "String",
      "Description": "The action taken on the predicted maximum value. Valid values:\n- MaxOverri
dePredictiveValue: uses the initial maximum capacity as the maximum value for forecast tasks when the predicted value is greater than the initial maximum capacity.\n - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast tasks when the predicted value is grea ter than the initial maximum capacity.\n - PredictiveValueOverrideMaxWithBuffer: increases the pr edicted value with a ratio, which is specified by PredictiveValueBuffer. If the value after the i ncrease is greater than the initial maximum capacity, the value after the increase is used as the maximum value for forecast tasks.\n Default value: MaxOverridePredictiveValue",
      "AllowedValues": [
        "MaxOverridePredictiveValue",
        "PredictiveValueOverrideMax",
        "PredictiveValueOverrideMaxWithBuffer"
```

`]`

```json
    "MinAdjustmentMagnitude": {
      "Type": "Number",
      "Description": "The minimum number of ECS instances to be adjusted in a scaling rule. This
parameter takes effect only when the scaling rule type is SimpleScalingRule or StepScalingRule an d AdjustmentType is PercentChangeInCapacity.",
      "MinValue": 0,
      "MaxValue": 20
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

`]`

```json
    "StepAdjustment": {
      "Type": "Json",
      "Description": ""
    "AdjustmentType": {
      "Type": "String",
      "Description": "Adjustment mode of a scaling rule. Optional values:\n- QuantityChangeInCapa
city: It is used to increase or decrease a specified number of ECS instances.\n- PercentChangeInC apacity: It is used to increase or decrease a specified proportion of ECS instances.\n- TotalCapa city: It is used to adjust the quantity of ECS instances in the current scaling group to a specif ied value.",
      "AllowedValues": [
        "QuantityChangeInCapacity",
        "PercentChangeInCapacity",
        "TotalCapacity"
```

`]`

```json
    "MetricName": {
      "Type": "String",
      "Description": "The predefined metric to monitor. This parameter is required and applicable
only to target tracking scaling rules and predictive scaling rules.\nValid values of a target tra cking scaling rule:\n- CpuUtilization: the average CPU utilization- ClassicInternetRx: the averag e public network inbound traffic over the classic network\n- ClassicInternetTx: the average publi c network outbound traffic over the classic network\n- VpcInternetRx: the average public network inbound traffic over the VPC\n- VpcInternetTx: the average public network outbound traffic over t he VPC\n- IntranetRx: the average internal network inbound traffic\n- IntranetTx: the average int ernal network outbound traffic\nValid values of a predictive scaling rule:\n- CpuUtilization: the average CPU utilization\n- IntranetRx: the average internal network inbound traffic\n- IntranetTx : the average internal network outbound traffic",
      "AllowedValues": [
        "CpuUtilization",
        "ClassicInternetRx",
        "ClassicInternetTx",
        "VpcInternetRx",
        "VpcInternetTx",
        "IntranetRx",
        "IntranetTx"
```

`]`

```json
    "ScalingRuleName": {
      "Type": "String",
      "Description": "Name shown for the scaling group, which is a string containing 2 to 40 Engl
ish or Chinese characters. It must begin with a number, a letter (case-insensitive) or a Chinese character and can contain numbers, \"_\", \"-\" or \". \". The account name in the same scaling g roup is unique in the same region. If this parameter value is not specified, the default value is ScalingRuleId.",
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$"
    "AdjustmentValue": {
      "Type": "Number",
      "Description": "Adjusted value of a scaling rule. Value range:\n- QuantityChangeInCapacity:
[-500, 500]\n- PercentChangeInCapacity: [-100, 10000]\n- TotalCapacity: [0, 1000]",
      "MinValue": -500,
      "MaxValue": 10000
    "InitialMaxSize": {
      "Type": "Number",
      "Description": "The maximum number of ECS instances in the scaling group, which is used tog
ether with PredictiveValueBehavior.\n Default value: the same as the value of MaxSize",
      "MinValue": 0,
      "MaxValue": 1000
    "ScalingRuleType": {
      "Type": "String",
      "Description": "The type of the scaling rule. Valid values:\n- SimpleScalingRule: scales EC
S instances based on the values of AdjustmentType and AdjustmentValue.\n- TargetTrackingScalingRu le: dynamically calculates the number of ECS instances to be adjusted and tries to keep the value of a predefined monitoring metric close to TargetValue.\n- StepScalingRule: scales ECS instances in steps based on specified thresholds and metric values.\n- PredictiveScalingRule: uses machine learning to analyze historical monitoring data of the scaling group and then predicts the future values of monitored metrics, the rule then automatically creates scheduled tasks to set the bound ary values for the scaling group.\n If this parameter value is not specified, the default value i
```

```json
s SimpleScalingRule.",
      "AllowedValues": [
        "SimpleScalingRule",
        "TargetTrackingScalingRule",
        "StepScalingRule",
        "PredictiveScalingRule"
```

`]`

```json
    "EstimatedInstanceWarmup": {
      "Type": "Number",
      "Description": "The warm-up period of the ECS instances. This parameter is applicable to ta
rget tracking scaling rules and step scaling rules. The system adds ECS instances that are in the warm-up state to the scaling group, but does not report monitoring data during the warm-up period to CloudMonitor.\nNote: When calculating the number of ECS instances to be adjusted, the system d oes not count ECS instances in the warm-up state as part of the current capacity of the scaling g roup.\nValid values: 0 to 86400. Unit: seconds. Default value: 300.",
      "MinValue": 0,
      "MaxValue": 86400
    "PredictiveScalingMode": {
      "Type": "String",
      "Description": "The mode of the predictive scaling rule. Valid values:\n- PredictAndScale:
generates forecasts and creates forecast tasks.\n- PredictOnly: generates forecasts but does not create forecast tasks.\nDefault value: PredictAndScale",
      "AllowedValues": [
        "PredictAndScale",
        "PredictOnly"
```

`]`

```json
    "PredictiveTaskBufferTime": {
      "Type": "Number",
      "Description": "The amount of buffer time ahead of the forecast task execution time. By def
ault, all scheduled tasks that are automatically created for a predictive scaling rule are execut ed at the beginning of each hour. You can set a buffer time to execute forecast tasks ahead of sc hedule, so that resources can be prepared in advance. Valid values: 0 to 60. Unit: minutes.\n Def ault value: 0",
      "MinValue": 0,
      "MaxValue": 60
    "PredictiveValueBuffer": {
      "Type": "Number",
      "Description": "The ratio of the increment to the predicted value when PredictiveValueBehav
ior is set to PredictiveValueOverrideMaxWithBuffer. When the value after the increase is greater than the initial maximum capacity, the value after the increase is used for forecast tasks. Valid values: 0 to 100\n Default value: 0",
      "MinValue": 0,
      "MaxValue": 100
  "Resources": {
    "ScalingRule": {
      "Type": "ALIYUN::ESS::ScalingRule",
      "Properties": {
        "TargetValue": {
          "Ref": "TargetValue"
        "Cooldown": {
"Ref":"Cooldown"
```

```json
          "Ref": "Cooldown"
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
        "PredictiveValueBehavior": {
          "Ref": "PredictiveValueBehavior"
        "MinAdjustmentMagnitude": {
          "Ref": "MinAdjustmentMagnitude"
        "DisableScaleIn": {
          "Ref": "DisableScaleIn"
        "StepAdjustment": {
          "Ref": "StepAdjustment"
        "AdjustmentType": {
          "Ref": "AdjustmentType"
        "MetricName": {
          "Ref": "MetricName"
        "ScalingRuleName": {
          "Ref": "ScalingRuleName"
        "AdjustmentValue": {
          "Ref": "AdjustmentValue"
        "InitialMaxSize": {
          "Ref": "InitialMaxSize"
        "ScalingRuleType": {
          "Ref": "ScalingRuleType"
        "EstimatedInstanceWarmup": {
          "Ref": "EstimatedInstanceWarmup"
        "PredictiveScalingMode": {
          "Ref": "PredictiveScalingMode"
        "PredictiveTaskBufferTime": {
          "Ref": "PredictiveTaskBufferTime"
        "PredictiveValueBuffer": {
          "Ref": "PredictiveValueBuffer"
  "Outputs": {
    "ScalingRuleAri": {
      "Description": "Unique identifier of a scaling rule.",
      "Value": {
        "Fn::GetAtt": [
          "ScalingRule",
          "ScalingRuleAri"
```

`]` `]`

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
    Type: String
    Description: >-
      The action taken on the predicted maximum value. Valid values:
      - MaxOverridePredictiveValue: uses the initial maximum capacity as the
      maximum value for forecast tasks when the predicted value is greater than
      the initial maximum capacity.
       - PredictiveValueOverrideMax: uses the predicted value as the maximum value for forecast t
asks when the predicted value is greater than the initial maximum capacity.
       - PredictiveValueOverrideMaxWithBuffer: increases the predicted value with a ratio, which
is specified by PredictiveValueBuffer. If the value after the increase is greater than the initia l maximum capacity, the value after the increase is used as the maximum value for forecast tasks.
       Default value: MaxOverridePredictiveValue
    AllowedValues:
      - MaxOverridePredictiveValue
      - PredictiveValueOverrideMax
      - PredictiveValueOverrideMaxWithBuffer
  MinAdjustmentMagnitude:
    Type: Number
    Description: >-
      The minimum number of ECS instances to be adjusted in a scaling rule. This
parametertakeseffectonlywhenthescalingruletypeis
```

```
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
```

`p`

```
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
```

```
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
```

`dj`

```
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

#### 6.2.8 ALIYUN::ESS::ScheduledTask

ALIYUN::ESS::ScheduledTask is used to create a scheduled task based on specified parameters. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TaskEnabled | Boolean | No | Yes | Specifies whether to enable the scheduled task. | Valid values: true: enables the task. This is the default value. false: stops the task. |
| Description | String | No | Yes | The description of the scheduled task. | The description must be 2 to 200 characters in length. |
| ScheduledTask Name | String | No | Yes | The display name of the scheduled task. | The name must be 2 to 40 characters in length and can contain digits, letters, underscores ( ), _ hyphens (-), and periods (.). It must start with a digit or letter. The name of the scheduled task must be unique to an Alibaba Cloud account in a region. If you do not specify this parameter, the default value is the ID of the scheduled scaling task. |
| LaunchExpiratio nTime | Integer | No | Yes | The period of time over which a failed scheduled task is retried. | Valid values: 0 to 21600. Unit: seconds. Default value: 600. |

| Property | Type | Required | Editable | Description |   |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|
| LaunchTime | String | Yes | Yes | The time at which the scheduled task is triggered. |   |   | Specify the time in the ISO 8601 standard in the YYYY- MM- DDThh:mmZ format. The time must be in UTC. If the RecurrenceTy pe parameter is specified, the task is executed each day at the time specified by LaunchTime. If the RecurrenceTy pe parameter is not specified, the task is executed only once at the time specified by LaunchTime. You cannot enter a time point later than 90 days from the date of scheduled task creation or modification. |   |   |
|   |   |   |   |   |   |   |   | YYYY- |   |
|   |   |   |   |   |   |   | MM- |   |   |
|   |   |   |   |   |   |   | DDThh:mmZ |   |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RecurrenceEndT ime | String | No | Yes | The end time of the scheduled task to be repeated. | Specify the time in the ISO 8601 standard in the YYYY- MM- DDThh:mmZ format. The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation or modification. If you set RecurrenceEndT ime, you must also set both RecurrenceType and RecurrenceValu e. |

|   |   |   | YYYY- |   |
|---|---|---|---|---|
|   |   | MM- |   |   |
|   |   | DDThh:mmZ |   |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RecurrenceType | String | No | Yes | The interval at which the scheduled task is repeated. | Valid values: Daily: The scheduled task is executed once every specified number of days. Weekly: The scheduled task is executed on each specified day of a week. Monthly: The scheduled task is executed on each specified day of a month. Cron: The scheduled task is executed based on the specified Cron expression. If you set RecurrenceType , you must also set both RecurrenceEndT ime and RecurrenceValu e. |
|   |   |   |   |   | Valid values when RecurrenceTy pe is set to Daily: 1 to 31. Valid values when RecurrenceTy pe is set to Weekly: 0 to 6. You can enter multiple |

| Property | Type | Required | Editable | Description | values Constraint separated by |
|---|---|---|---|---|---|
| RecurrenceValu e | String | No | Yes | The recurrence value of the scheduled task to be repeated. | commas (,). The values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday. Valid values when RecurrenceTy pe is set to Monthly: two values ranging from 1 to 31 in the A-B format. B must be greater than or equal to A. Valid values when RecurrenceTy pe is set to Cron: a Cron expression. A Cron expression is written in UTC time and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W characters. |

| Property | Type | Required | Editable | Description | If you set Constraint RecurrenceValu |
|---|---|---|---|---|---|
|   |   |   |   |   | e, you must also set both RecurrenceEndT ime and RecurrenceType . |
| ScheduledActio n | String | Yes | Yes | The operations to be performed when the scheduled task is triggered. | The parameter value can be up to 200 characters in length. When you set this parameter, you must also enter the unique identifier of the scaling rule. |

Response parameters Fn::GetAtt ScheduledTaskId: the ID of the scheduled task. This ID is a globally unique identifier (GUID) generated by the system. Examples

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
  "Outputs": {
    "ScheduledTaskId": {
      "Value": {
        "FN::GetAtt": [
          "ScheduledTask",
          "ScheduledTaskId"
```

`]`

### 6.3 NAS

#### 6.3.1 ALIYUN::NAS::AccessGroup

ALIYUN::NAS::AccessGroup is used to create a permission group. Syntax

```json
  "Type": "ALIYUN::NAS::AccessGroup",
  "Properties": {
    "AccessGroupType": String,
    "AccessGroupName": String,
    "Description": String
```

Properties

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| AccessGroupTy pe | String | Yes | No | The type of the permission group. | Valid values: VPC and Classic. |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| AccessGroupNa me | String | Yes | No | The name of the permission group. | The name must be 3 to 64 characters in length. It must start with a letter, digit, or hyphen (-). |
| Description | String | No | Yes | The description of the permission group. The description is the same as the permission group name by default. | None |

Response parameters FN::Get At t AccessGroupName: the name of the permission group. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessGroup": {
      "Type": "ALIYUN::NAS::AccessGroup",
      "Properties": {
        "AccessGroupType": {
          "Ref": "AccessGroupType"
        "AccessGroupName": {
          "Ref": "AccessGroupName"
        "Description": {
          "Ref": "Description"
  "Parameters": {
    "AccessGroupType": {
      "Type": "String",
      "Description": "Permission group type, including the Vpc and Classic types",
      "AllowedValues": ["Vpc", "Classic"]
    "AccessGroupName": {
      "AllowedPattern": "^[a-zA-Z0-9-]{3,64}$",
      "Type": "String",
      "Description": "Permission group name"
    "Description": {
      "Type": "String",
      "Description": "Permission group description. It is the same as the permission group name b
y default."
  "Outputs": {
    "AccessGroupName": {
      "Description": "Permission group name",
      "Value": {
        "Fn::GetAtt": ["AccessGroup", "AccessGroupName"]
```

#### 6.3.2 ALIYUN::NAS::AccessRule

ALIYUN::NAS::AccessRule is used to create a permission rule. Syntax

```json
  "Type": "ALIYUN::NAS::AccessRule",
  "Properties": {
    "Priority": Integer,
    "UserAccessType": String,
    "AccessGroupName": String,
    "SourceCidrIp": String,
    "RWAccessType": String
```

Properties

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| Priority | Integer | No | Yes | The user access priority. | Valid values: 1 to 100. Default value: 1. |
| UserAccessType | String | No | Yes | The user access type. | Valid values: no squash, _ root squash, _ and all squash. _ Default value: no squash. _ |
| AccessGroupNa me | String | Yes | No | The name of the permission group. | None |
| SourceCidrIp | String | Yes | Yes | The authorized IP address or CIDR block. | None |
| RWAccessType | String | No | Yes | The read/write permission type. | Valid values: RDWR and RDONLY. Default value: RDWR. |

Response parameters FN::Get At t AccessRuleId: the ID of the permission rule. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessRule": {
      "Type": "ALIYUN::NAS::AccessRule",
      "Properties": {
        "Priority": {
          "Ref": "Priority"
```

`"` `"``{`

```json
        "RWAccessType ":{
          "Ref": "RWAccessType"
        "UserAccessType": {
          "Ref": "UserAccessType"
        "SourceCidrIp": {
          "Ref": "SourceCidrIp"
        "AccessGroupName": {
          "Ref": "AccessGroupName"
  "Parameters": {
    "Priority": {
      "Default": 1,
      "Type": "Number",
      "Description": "Priority level. Range: 1-100. Default value: 1",
      "MaxValue": 100,
      "MinValue": 1
    "RWAccessType": {
      "Default": "RDWR",
      "Type": "String",
      "Description": "Read-write permission type: RDWR (default), RDONLY",
      "AllowedValues": ["RDWR", "RDONLY"]
    "UserAccessType": {
      "Default": "no_squash",
      "Type": "String",
      "Description": "User permission type: no_squash (default), root_squash, all_squash",
      "AllowedValues": ["no_squash", "root_squash", "all_squash"]
    "SourceCidrIp": {
      "Type": "String",
      "Description": "Address or address segment"
    "AccessGroupName": {
      "Type": "String",
      "Description": "Permission group name"
  "Outputs": {
    "AccessRuleId": {
      "Description": "Rule serial number",
      "Value": {
        "Fn::GetAtt": ["AccessRule", "AccessRuleId"]
```

#### 6.3.3 ALIYUN::NAS::FileSystem

ALIYUN::NAS::FileSystem is used to create a file system. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ProtocolTy pe | String | Yes | No | The protocol type. | Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
| StorageTyp e | String | Yes | No | The storage type. | Valid values: Valid values if you set the FileSystemType property to standard: Performance Capacity Valid values if you set the FileSystemType property to extreme or cpfs: standard advance |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DeletionFor ce | Boolean | No | Yes | Specifies whether to forcefully delete the file system. | Default value: false. Valid values: true: forcefully deletes the file system. false: does not forcefully delete the file system. |
| Description | String | No | Yes | The description of the file system. | The description must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). The description must start with a letter but cannot start with http:// or https:// . |
| ZoneId | String | No | No | The ID of the zone. | None. |
| Tags | List | No | Yes | The tags of the file system. | You can add up to 20 tags to each file system. For more information, see Tags properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SnapshotId | String | No | No | The ID of the snapshot. | You can configure this property to specify a snapshot from which you create an Apsara File Storage NAS (NAS) file system. This property is supported only for Extreme NAS file systems. Not e If you create a file system from a snapshot, the version of the new file system must be the same as the version of the source file system that is contained in the snapshot. If the version of a file system that you create is different from the version of the source file system, you must perform the following operations: 1. Create a file system and copy the data that is stored in the source file of the snapshot to the file system. 2. After you copy the data, migrate the data to the file system. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| EncryptTyp e | Integer | No | No | Specifies whether to encrypt the file system. You can use keys that are hosted by Key Management Service (KMS) to encrypt data that is stored in the file system. When you read and write the encrypted data, you do not need to decrypt the data. | This property takes effect when you set the FileSystemType property to standard or extreme. Valid values: 0: does not encrypt the file system. 1: encrypts the file system. |
| Capacity | Integer | No | No | The capacity of the file system. | This property takes effect and is required when you set the FileSystemType property to extreme or cpfs. Valid values: Valid values if you set the FileSystemType property to extreme: 100 to 262144. Valid values if you set the FileSystemType property to cpfs: 2048 to 512000. Unit: GB. |
| FileSystemT ype | String | No | No | The type of the file system. | Default value: standard. Valid values: standard: General- purpose NAS file system extreme: Extreme NAS file system cpfs: Cloud Paralleled File System (CPFS) file system |
| VpcId | String | No | No | The ID of the virtual private cloud (VPC). If you specify the VpcId and VSwitchId properties, a default mount target is preconfigured when the file system is created. | This property is required when you set the FileSystemType property to cpfs. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Bandwidth | Integer | No | No | The maximum throughput of the file system. | This property is required when you set the FileSystemType property to cpfs. The value of this property varies based on the value of the Capacity property. For more information, visit the CPFS buy page. Unit: Mbit/s. |
| VSwitchId | String | No | No | The ID of the vSwitch. If you specify the VpcId and VSwitchId properties, a default mount target is preconfigured when the file system is created. | This property is required when you set the FileSystemType property to cpfs. |
| Duration | Integer | No | No | The subscription period of the file system. | This property takes effect and is required when you set the ChargeType property to Subscription. If you do not renew a subscription file system when it expires, the file system is automitically released. Valid values: 1 2 3 6 12 36 Unit: month. |
| ChargeType | String | No | No | The billing method of the file system. | Valid values: PayAsYouGo Subscription |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The key cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The value cannot start with aliyun or acs: . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt FileSystemId: the ID of the file system. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "File system description.",
      "Default": "mytest"
    "ProtocolType": {
      "Type": "String",
      "Description": "Type of protocol used.",
      "AllowedValues": [
        "NFS",
        "SMB"
```

`],`

```json
      "Default": "NFS"
    "StorageType": {
      "Type": "String",
      "Description": "The file system type.",
      "AllowedValues": [
        "Performance",
        "Capacity"
```

`],`

```json
      "Default": "Capacity"
  "Resources": {
    "FileSystem": {
      "Type": "ALIYUN::NAS::FileSystem",
      "Properties": {
        "ProtocolType": {
          "Ref": "ProtocolType"
        "StorageType": {
          "Ref": "StorageType"
        "Description": {
          "Ref": "Description"
  "Outputs": {
    "FileSystemId": {
      "Description": "ID of the file system created",
      "Value": {
        "Fn::GetAtt": [
          "FileSystem",
          "FileSystemId"
```

`]` To view more examples, visit NAS.json and NAS.yml. In the examples, the following resource types are used: ALIYUN::NAS::FileSystem, ALIYUN::NAS::AccessGroup, ALIYUN::NAS::AccessRule, and ALIYUN::NAS::MountTarget.

#### 6.3.4 ALIYUN::NAS::MountTarget

ALIYUN::NAS::MountTarget is used to create a mount point. Syntax

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

Properties

| Name | Type | Required | Editable | Description | Validity |
|---|---|---|---|---|---|
| Status | String | No | Yes | The status of a file system. | Valid values: Active and Inactive. |
| VpcId | String | No | No | The ID of the VPC to which the file system belongs. | None |
| FileSystemId | String | Yes | No | The ID of the file system. | None |
| VSwitchId | String | No | No | The ID of the vSwitch in the VPC. | None |
| NetworkType | String | Yes | No | The network type. | Valid values: VPC and Classic. |
| AccessGroupNa me | String | Yes | Yes | The permission group name. | None |

Response parameters FN::Get At t MountTargetDomain: the domain name of the mount point. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "MountTarget": {
      "Type": "ALIYUN::NAS::MountTarget",
      "Properties": {
        "Status": {
          "Ref": "Status"
        "VpcId": {
          "Ref": "VpcId"
        "FileSystemId": {
          "Ref": "FileSystemId"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "NetworkType": {
          "Ref": "NetworkType"
        "AccessGroupName": {
          "Ref": "AccessGroupName"
  "Parameters": {
    "Status": {
      "Type": "String",
      "Description": "Status, including Active and Inactive",
      "AllowedValues": ["Active", "Inactive"]
    "VpcId": {
      "Type": "String",
      "Description": "VPC network ID"
    "FileSystemId": {
      "Type": "String",
      "Description": "File system ID"
    "VSwitchId": {
      "Type": "String",
      "Description": "vSwitch ID."
    "NetworkType": {
      "Type": "String",
      "Description": "Network type, including Vpc and Classic networks.",
      "AllowedValues": ["Vpc", "Classic"]
    "AccessGroupName": {
      "Type": "String",
      "Description": "Permission group name"
  "Outputs": {
    "MountTargetDomain": {
      "Description": "Mount point domain name",
```

`"` `l` `"`

```json
      "Value": {
        "Fn::GetAtt": ["MountTarget", "MountTargetDomain"]
```

### 6.4 OSS

#### 6.4.1 ALIYUN::OSS::Bucket

ALIYUN::OSS::Bucket is used to create an Object Storage Service (OSS) bucket. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| BucketName | String | Yes | No | The name of the bucket. | The name must be 3 to 63 characters in length and can contain lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or a digit. |
| AccessContr ol | String | No | No | The access control configuratio ns of the bucket. | Valid values: private (default): The bucket is private. public-read: The bucket supports public reads. public-read-write: The bucket supports public reads and writes. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CORSConfigu ration | Map | No | No | The configuratio ns of cross- origin resource sharing (CORS) for objects in the bucket. | For more information, see CORSConfiguration properties. |
| LifecycleConf iguration | Map | No | Yes | The lifecycle configuratio ns for objects in the bucket. | For more information, see LifecycleConfiguration properties. |
| LoggingConfi guration | Map | No | No | The log storage configuratio ns. | For more information, see LoggingConfiguration properties. |
| RefererConfi guration | Map | No | Yes | The hotlink protection configuratio ns. | For more information, see RefererConfiguration properties. |
| DeletionForc e | Boolean | No | No | Specifies whether to forcibly delete objects from the OSS bucket. | Valid values: true: forcibly deletes objects from the OSS bucket. false (default): does not forcibly delete objects from the OSS bucket. |
| WebsiteConfi guration | Map | No | No | The configuratio ns of the hosted static website. | For more information, see WebsiteConfiguration properties. |
| ServerSideEn cryptionConfi guration | Map | No | Yes | The server- side encryption rules. | For more information, see ServerSideEncryptionConfigur ation properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Tags | Map | No | Yes | The tags of the bucket. Tags exist as key-value pairs. | A maximum of 20 tags can be specified. A tag key must be 1 to 64 bytes in length and cannot start with http:// , https:// , or Aliyun . A tag value must be 0 to 128 bytes in length and must be encoded in UTF-8. |
| StorageClass | String | No | No | The type of the bucket. | Default value: Standard. Valid values: Standard: Standard IA: Infrequent Access (IA) Archive: Archive |
| Policy | Map | No | No | The bucket policy configuratio ns. | None |

CORSConfiguration syntax

```json
"CORSConfiguration": {
  "CORSRule": List
```

CORSConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CORSRule | List | No | No | The list of rules that define CORS of objects in the bucket. | For more information, see CORSRule properties. |

CORSRule syntax

```json
"CORSRule": [
    "MaxAgeSeconds": Number,
    "AllowedMethod": List,
    "ExposeHeader": List,
    "AllowedOrigin": List,
    "AllowedHeader": List
```

`]` CORSRule properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllowedHea der | List | No | No | The allowed headers in cross- domain requests. | Valid values: * Cache-Control Content-Language Content-Type Expires Last-Modified Pragma |
| AllowedMeth od | List | No | No | The allowed methods for cross- domain requests. | Valid values: * GET PUT POST DELETE HEAD |
| AllowedOrigi n | List | No | No | The origins from which you want to allow cross- domain requests. | None |
| ExposeHead er | List | No | No | The response headers that you can access from your applications. | Asterisks (*) cannot be used as wildcard characters. |
| MaxAgeSeco nds | Number | No | No | The period of time that the browser can cache the response of a preflight (OPTIONS) request to a specific resource. | None |

LifecycleConfiguration syntax

```json
"LifecycleConfiguration": {
  "Rule": List
```

LifecycleConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Rule | List | Yes | No | The list of rules that define how the bucket manages objects during their lifecycles. | For more information, see Rule properties. |

Rule syntax

```json
"Rule": [
    "Status": String,
    "AbortMultipartUpload": Map,
    "Expiration": Map,
    "Prefix": String,
    "ID": String
```

`]` Rule properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ID | String | No | No | The unique ID of the rule. | The ID can be up to 255 bytes in length. When this parameter is empty or not specified, OSS generates a unique ID for the rule. |
| Prefix | String | Yes | No | The prefix to which the rule applies. | The rule takes effect only on objects that have a matching prefix. |
| Status | String | No | Yes | Specifies whether to enable the rule. | Valid values: Enabled: enables the rule. Disabled: disables the rule. |
| Expiration | Map | No | No | The expiration attributes of the rule for the specified object. | For more information, see Expiration properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AbortMultipa rtUpload | Map | No | No | The expiration attributes of the multipart upload tasks that are not complete. | For more information, see AbortMultipartUpload properties. |

Expiration syntax

```json
"Expiration":{
  "Days": Number,
  "CreatedBeforeDate": String,
  "Date": String
```

Expiration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days from when the object was last modified to when the rule takes effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |
| CreatedBefor eDate | String | No | No | The date based on which the lifecycle rules are implemente d. OSS performs the specified operation on data that was last modified before this date. | Specify the time in the ISO 8601 standard. The time must be at 00:00:00 UTC. Example: 2002-10-11T00:00:00.000Z. |

AbortMultipartUpload syntax

```json
"AbortMultipartUpload": {
  "CreatedBeforeDate": String,
  "Days": Number
```

AbortMultipartUpload properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days from when the object was last modified to when the rule takes effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |
| CreatedBefor eDate | String | No | No | The time before which the rule takes effect. | Specify the time in the ISO 8601 standard. The time must be at 00:00:00 UTC. Example: 2002-10-11T00:00:00.000Z. |

LoggingConfiguration syntax

```json
"LoggingConfiguration": {
  "TargetBucket": String,
  "TargetPrefix": String
```

LoggingConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TargetBucket | String | No | No | The bucket that is used to store access logs. | None |
| TargetPrefix | String | No | No | The prefix of the names of access logs that are saved. | None |

WebsiteConfiguration syntax

```json
"WebsiteConfiguration":{
  "IndexDocument": String,
  "ErrorDocument": String
```

WebsiteConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IndexDocum ent | String | No | No | The homepage for the hosted static website. | None |
| ErrorDocume nt | String | No | No | The error page of the hosted static website. | None |

RefererConfiguration syntax

```json
"RefererConfiguration":{
  "AllowEmptyReferer": String,
  "RefererList": List
```

RefererConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllowEmptyR eferer | Boolean | No | No | Specifies whether to allow access requests that have an empty Referer field. | Valid values: true (default): allows requests that have an empty Referer field. false: denies requests that have an empty Referer field. |
| RefererList | List | No | No | The Referer whitelist. OSS allows requests whose Referer field values are in the Referer whitelist. | None |

ServerSideEncryptionConfiguration syntax

```json
"ServerSideEncryptionConfiguration":{
  "KMSMasterKeyID": String,
  "SSEAlgorithm": String
```

ServerSideEncryptionConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| KMSMasterKe yID | String | No | No | The ID of the customer master key. | The key ID is required only when the SSEAlgorithm parameter is set to KMS and a specified key is used for encryption. |
| SSEAlgorith m | String | Yes | No | The default server-side encryption method. | Valid values: KMS AES256 |

Response parameters Fn::GetAtt Name: the bucket name, which is globally unique. DomainName: the public domain name of the specified bucket. InternalDomainName: the internal domain name of the specified bucket. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Policy": {
      "Type": "Json",
      "Description": "Bucket policy"
    "CORSConfiguration": {
      "Type": "Json",
      "Description": "Rules that define cross-origin resource sharing of objects in this bucket."
    "DeletionForce": {
      "Type": "Boolean",
      "Description": "Whether force delete the relative objects in the bucket. Default value is f
alse.",
      "AllowedValues": [
        "true",
        "false"
```

`],`

```json
      "Default": false
    "BucketName": {
      "Type": "String",
      "Description": "bucket name."
    "StorageClass": {
      "Type": "String",
      "Description": "Specifies the storage class of the bucket. Default is \"Standard\".",
      "AllowedValues": [
        "Standard",
        "IA",
        "Archive"
```

`]` `]`

```json
    "LoggingConfiguration": {
      "Type": "Json",
      "Description": "Settings that defines where logs are stored."
    "WebsiteConfiguration": {
      "Type": "Json",
      "Description": "The properties of website config."
    "RefererConfiguration": {
      "Type": "Json"
    "LifecycleConfiguration": {
      "Type": "Json",
      "Description": "Rules that define how oss bucket manages objects during their lifetime."
    "ServerSideEncryptionConfiguration": {
      "Type": "Json",
      "Description": "Specifies the bucket used to store the server-side encryption rule."
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
    "Tags": {
      "Type": "Json",
      "Description": "Bucket tags in k-v pairs format."
  "Resources": {
    "Bucket": {
      "Type": "ALIYUN::OSS::Bucket",
      "Properties": {
        "Policy": {
          "Ref": "Policy"
        "CORSConfiguration": {
          "Ref": "CORSConfiguration"
        "DeletionForce": {
          "Ref": "DeletionForce"
        "BucketName": {
          "Ref": "BucketName"
        "StorageClass": {
          "Ref": "StorageClass"
        "LoggingConfiguration": {
          "Ref": "LoggingConfiguration"
```

```json
        "WebsiteConfiguration": {
          "Ref": "WebsiteConfiguration"
        "RefererConfiguration": {
          "Ref": "RefererConfiguration"
        "LifecycleConfiguration": {
          "Ref": "LifecycleConfiguration"
        "ServerSideEncryptionConfiguration": {
          "Ref": "ServerSideEncryptionConfiguration"
        "AccessControl": {
          "Ref": "AccessControl"
        "Tags": {
          "Ref": "Tags"
  "Outputs": {
    "DomainName": {
      "Description": "The public DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "DomainName"
```

`]`

```json
    "InternalDomainName": {
      "Description": "The internal DNS name of the specified bucket.",
      "Value": {
        "Fn::GetAtt": [
          "Bucket",
          "InternalDomainName"
```

`]`

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
```

`li`

```
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
Ref:CORSConfiguration
```

```
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

### 6.5 RDS

#### 6.5.1 ALIYUN::RDS::Account

ALIYUN::RDS::Account is used to create a database account for an ApsaraDB for RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::Account",
  "Properties": {
    "AccountDescription": String,
    "DBInstanceId": String,
    "AccountPassword": String,
    "AccountType": String,
    "AccountName": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountDescrip tion | String | No | Yes | The description of the database account. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), _ and hyphens(-). It must start with a letter. |
| DBInstanceId | String | Yes | No | The ID of the instance. | None |
| AccountPasswo rd | String | Yes | No | The password of the database account. | The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @#$&amp;%^ *() +-= _ |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountType | String | No | No | The type of the database account. | Default value: Normal. Valid values: Normal: standard account Super: privileged account Not e Privilege d account s in ApsaraD B RDS for SQL Server instance s cannot be deleted. |
| AccountName | String | Yes | No | The name of the database account. | None |

Response parameters Fn::GetAtt AccountName: the name of the database account. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AccountDescription": {
      "Type": "String",
      "Description": "Account remarks.\nIt cannot begin with http:// or https://.\nIt must start
with a Chinese character or English letter.\nIt can include Chinese and English characters/letter s, underscores (_), hyphens (-), and digits.\nThe length may be 2-256 characters."
    "DBInstanceId": {
      "Type": "String",
      "Description": "RDS instance ID."
    "AccountType": {
      "Type": "String",
```

`"D`

```
iti
```

`"`

```
"Piil
```

`t` `f`

```
t\N
```

`l`

```
iil
```

\`S`

```
Hih iil
```

```json
      "Description": "Privilege type of account.\nNormal: Common privilege.\nSuper: High privileg
e. And the default value is Normal.\nThis parameter is valid for MySQL 5.5/5.6 only.\nMySQL 5.7, SQL Server 2012/2016, PostgreSQL, and PPAS each can have only one initial account. Other accounts are created by the initial account that has logged on to the database.",
      "AllowedValues": [
        "Normal",
        "Super"
```

`],`

```json
      "Default": "Normal"
    "AccountPassword": {
      "Type": "String",
      "Description": "The account password for the database instance. It may consist of letters,
digits, or underlines, with a length of 8 to 32 characters.",
      "MinLength": 8,
      "MaxLength": 32
    "AccountName": {
      "Type": "String",
      "Description": "Account name, which must be unique and meet the following requirements:\nSt
art with a letter;\nConsist of lower-case letters, digits, and underscores (_);\nContain no more than 16 characters.\nFor other invalid characters, see Forbidden keywords table."
  "Resources": {
    "Account": {
      "Type": "ALIYUN::RDS::Account",
      "Properties": {
        "AccountDescription": {
          "Ref": "AccountDescription"
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        "AccountType": {
          "Ref": "AccountType"
        "AccountPassword": {
          "Ref": "AccountPassword"
        "AccountName": {
          "Ref": "AccountName"
  "Outputs": {
    "AccountName": {
      "Description": "Account name",
      "Value": {
        "Fn::GetAtt": [
          "Account",
          "AccountName"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AccountDescription:
    Type: String
    Description: >-
      Account remarks.
      It cannot begin with http:// or https://.
      It must start with a Chinese character or English letter.
      It can include Chinese and English characters/letters, underscores (_),
      hyphens (-), and digits.
      The length may be 2-256 characters.
  DBInstanceId:
    Type: String
    Description: RDS instance ID.
  AccountType:
    Type: String
    Description: >-
      Privilege type of account.
      Normal: Common privilege.
      Super: High privilege. And the default value is Normal.
      This parameter is valid for MySQL 5.5/5.6 only.
      MySQL 5.7, SQL Server 2012/2016, PostgreSQL, and PPAS each can have only
      one initial account. Other accounts are created by the initial account
      that has logged on to the database.
    AllowedValues:
      - Normal
      - Super
    Default: Normal
  AccountPassword:
    Type: String
    Description: >-
      The account password for the database instance. It may consist of letters,
      digits, or underlines, with a length of 8 to 32 characters.
    MinLength: 8
    MaxLength: 32
  AccountName:
    Type: String
    Description: |-
      Account name, which must be unique and meet the following requirements:
      Start with a letter;
      Consist of lower-case letters, digits, and underscores (_);
      Contain no more than 16 characters.
      For other invalid characters, see Forbidden keywords table.
Resources:
  Account:
    Type: 'ALIYUN::RDS::Account'
    Properties:
      AccountDescription:
        Ref: AccountDescription
      DBInstanceId:
        Ref: DBInstanceId
      AccountType:
        Ref: AccountType
```

`A` `tP` `d`

```
      AccountPassword:
        Ref: AccountPassword
      AccountName:
        Ref: AccountName
Outputs:
  AccountName:
    Description: Account name
    Value:
      'Fn::GetAtt':
        - Account
        - AccountName
```

#### 6.5.2 ALIYUN::RDS::AccountPrivilege

ALIYUN::RDS::AccountPrivilege is used to grant database access permissions to accounts. Statement

```json
  "Type": "ALIYUN::RDS::AccountPrivilege",
  "Properties": {
    "AccountPrivilege": String,
    "DBInstanceId": String,
    "DBName": String,
    "AccountName": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountPrivileg e | String | No | Yes | The permissions of the database account. | Valid values: ReadWrite: has read and write permissions on the database. ReadOnly: The account has read- only permission on the database. DDLOnly: The account can run only data definition language (DDL) commands in the database. This is applicable to MySQL and MariaDB. DMLOnly: The account can run only data manipulation language (DML) commands in the database. This is applicable to MySQL and MariaDB. DBOwner: The account has full permissions on the database. This is applicable to SQL Server. |
| DBInstanceId | String | No | No | The ID of the RDS instance. | None |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBName | String | No | No | The name of the database. | None |
| AccountName | String | No | No | The name of the account. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt None Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccountPrivilege": {
      "Type": "ALIYUN::RDS::AccountPrivilege",
      "Properties": {
        "AccountPrivilege": {
          "Ref": "AccountPrivilege"
        "DBInstanceId": [
          "Ref": "DBInstanceId"
        "DBName": {
          "Ref": "DBName"
        "AccountName": {
          "Ref": "AccountName"
  "Parameters": {
    "AccountPrivilege": {
      "Type": "String",
      "Description": "RDS account privilege",
      "AllowedValues": ["ReadOnly", "ReadWrite", "DDLOnly", "DMLOnly", "DBOwner"]
    "DBInstanceId": [
      "Type": "String",
      "Description": "RDS instance ID."
    "DBName": {
      "Type": "String",
      "Description": "RDS database name"
    "AccountName": {
      "Type": "String",
      "Description": "RDS account name."
  "Outputs": {}
```

#### 6.5.3 ALIYUN::RDS::DBInstance

ALIYUN::RDS::DBInstance is used to create an ApsaraDB RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::DBInstance",
  "Properties": {
    "PeriodType": String,
    "Category": String,
    "PrivateIpAddress": String,
"ResourceGroupId":String
```

```json
    ResourceGroupId: String,
    "TargetDedicatedHostIdForSlave": String,
    "DBInstanceNetType": String,
    "DBTimeZone": String,
    "DedicatedHostGroupId": String,
    "EncryptionKey": String,
    "PreferredBackupPeriod": List,
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
    "LogBackupLocalRetentionNumber": Integer
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroup Id | String | No | Yes | The ID of the resource group. | None |
| Engine | String | Yes | No | The database engine that the instance runs. | Valid values: MySQL SQLServer PostgreSQL PPAS MariaDB |
| DBInstanceStor age | Integer | Yes | Yes | The storage capacity of the instance. | Valid values when Engine is set to MySQL: 5 to 1000. Valid values when Engine is set to SQLServer: 10 to 1000. Valid values when Engine is set to PostgreSQL: 5 to 2000. Valid values when Engine is set to PPAS: 5 to 2000. Unit: GB. Not e This value must be in 5 GB increments. |
| EngineVersion | String | Yes | No | The version of the database engine. | Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0. Valid values when Engine is set to SQLServer: 2008r2, 08r2 ent ha, 2012, _ _ 2012 ent ha, 2012 std ha, _ _ _ _ 2012 web, 2014 std ha, _ _ _ 2016 ent ha, 2016 std ha, _ _ _ _ 2016 web, 2017 std ha, _ _ _ 2017 ent, and 2019 ent. _ _ Valid values when Engine is set to PostgreSQL: 9.4, 10.0, 11.0, and 12.0. Valid values when Engine is set to PPAS: 9.3 and 10.0. Set the value to 10.3 when Engine is set to MariaDB. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Port | Integer | No | Yes | The port that is used to connect to the instance. | None |
| ConnectionStri ngPrefix | String | No | Yes | The prefix of the endpoint. | The prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). |
| ConnectionStri ngType | String | No | Yes | The type of the endpoint. | Valid values: Inner: virtual private cloud (VPC) Public: Internet |
| DBTimeZone | String | No | No | The UTC time zone of the instance. | Valid values: -12:59 to +13:00. Not e If you do not specify this parameter, the system assigns the default time zone of the region to which the instance belongs. If you create an instance that has local SSDs attached, you can name the time zone. |
| DBParamGroup Id | String | No | No | The ID of the parameter template to be used by the instance. | None |
| Category | String | No | No | The edition of the instance. | Valid values: Basic: Basic Edition HighAvailability: High- availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TargetDedicat edHostIdForMa ster | String | No | No | The ID of the host on which to create a primary instance within a dedicated cluster. | None |
| DBIsIgnoreCase | Integer | No | No | Specifies whether table names are case-sensitive in the instance. | Default value: 1. Valid values: 0: Table names are case- sensitive. 1: Table names are case- insensitive. |
| EncryptionKey | String | No | No | The ID of the encryption key that is used to encrypt data on SSDs in the region. You can view the ID of an existing encryption key or create an encryption key in the Key Management Service (KMS) console. | If this parameter is specified, disk encryption is enabled and you must also specify the RoleARN parameter. Disk encryption cannot be disabled after it is enabled. |
| MaintainTime | String | No | No | The maintenance window of the cloned instance. | Specify the maintenance window in the HH:mmZ-HH:mmZ format. The time must be in UTC. |
| TargetDedicat edHostIdForSl ave | String | No | No | The ID of the host on which to create a secondary instance within a dedicated cluster. | None |
| DedicatedHost GroupId | String | No | No | The ID of the dedicated cluster in which to create instances. | None |
| DBInstanceStor ageType | String | No | No | The storage type of the instance. | Valid values: local ssd: local SSD. This is the _ recommended storage type. cloud ssd: standard SSD. _ cloud essd: enhanced SSD _ (ESSD). |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RoleARN | String | No | No | The Alibaba Cloud Resource Name (ARN) that is provided to the service account of the instance by your Alibaba Cloud account. This ARN is used to connect to KMS. | For more information, see Authorize an ApsaraDB RDS for MySQL instance to access KMS. |
| DBInstanceClas s | String | Yes | Yes | The instance type. | For more information, see Primary ApsaraDB RDS instance types. |
| SecurityIPList | String | Yes | Yes | The whitelist of IP addresses that are allowed to access all databases in the instance. | Separate multiple IP addresses with commas (,). Each IP address in the whitelist must be unique. A maximum of 1,000 IP addresses can be specified. Supported formats: IP addresses. Example: 10.23.XX.XX. CIDR blocks. For example, 10.23.X.24/24. 24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32. |
| SecurityGroupI d | String | No | Yes | The ID of the associated security group. | Each ApsaraDB RDS instance can be associated with up to three security groups. Separate multiple security groups with commas (,). To delete all security groups, set this parameter to an empty string. |
| MultiAZ | Boolean | No | No | Specifies whether the instance can be deployed across multiple zones. | Valid values: true false |
| VpcId | String | No | No | The ID of the VPC. | None |
| DBMappings | List | No | No | The list of one or more databases to be created in the instance. | For more information, see DBMappings properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceDes cription | String | No | No | The description of the instance. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ It must start with a letter and cannot start with http:// or https:// . |
| ConnectionMo de | String | No | No | The connection mode of the instance. | Valid values: Standard: the standard mode Safe: the database proxy mode If you do not specify this parameter, the system assigns a connection mode. Not e If you create an instance that runs SQL Server 2012, SQL Server 2016, or SQL Server 2017, you can set this parameter only to Standard. |
| MasterUserna me | String | No | No | The name of the database account. | The name must be globally unique. The name can be up to 16 characters in length and can contain letters, digits, and underscores ( ). It must start _ with a letter. |
| MasterUserPas sword | String | No | No | The password of the database account. | The password must be 8 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| ZoneId | String | No | No | The ID of the zone. | None |
| DBInstanceNet Type | String | No | No | The network type of the instance. | Default value: Intranet. Valid values: Internet Intranet |
| VSwitchId | String | No | No | The ID of the vSwitch. | Separate multiple vSwitch IDs with commas (,). This parameter is required if the Engine parameter is set to MariaDB. |

| Property | Type | Required | Editable | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| BackupPolicyM ode | String | No | No | The type of the backup. | Valid values: DataBackupPolicy LogBackupPolicy |   |   |
| AllocatePublic Connection | Boolean | No | No | Specifies whether to apply for a public endpoint for the instance. | Valid values: true false |   |   |
| PreferredBacku pTime | String | No | No | The backup window. | Specify the window in the HH :mmZ- HH:mmZ format. Valid values: 00:00Z-01:00Z, 01:00Z-02:00Z, 02:00Z- 03:00Z, 03:00Z-04:00Z, 04:00Z-05:00Z, 05:00Z- 06:00Z, 06:00Z-07:00Z, 07:00Z-08:00Z, 08:00Z- 09:00Z, 09:00Z-10:00Z, 10:00Z-11:00Z, 11:00Z- 12:00Z, 12:00Z-13:00Z, 13:00Z-14:00Z, 14:00Z- 15:00Z, 15:00Z-16:00Z, 16:00Z-17:00Z, 17:00Z- 18:00Z, 18:00Z-19:00Z, 19:00Z-20:00Z, 20:00Z- 21:00Z, 21:00Z-22:00Z, 22:00Z-23:00Z, and 23:00Z- 24:00Z. |   |   |
|   |   |   |   |   |   | HH |   |
| BackupRetenti onPeriod | Number | No | No | The number of days for which backup files can be retained. | Valid values: 7 to 30. Unit: days. Default value: 7. |   |   |
| PrivateIpAddre ss | String | No | No | The private IP address within the CIDR block of the vSwitch. | If you do not specify this parameter, the system allocates a private IP address. |   |   |
| PreferredBacku pPeriod | List | No | No | The backup cycle. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |   |   |

| Property | Type | Required | Editable |   | Description | Constraint |   |
|---|---|---|---|---|---|---|---|
| MasterUserTyp e | String | No | No |   | The type of the database account. | Default value: Normal. Valid values: Normal: standard account Super: privileged account Sysadmin: administrator account Not e This parameter can be set to Sysadmin only when the Engine parameter is set to SQLServer. |   |
| Tags | Map | No | Yes |   | The list of one or more tags. Each tag consists of a tag key | The tag key is required and the tag value is optional. Format example: {"key1":"value1","key2":"" |   |
|   |   |   |   |   |   |   | {"key1":"value1","key2":"" |
|   |   |   |   |   | and a tag value. | } |   |
| PeriodType | String | No | No |   | The unit of the subscription period. | Default value: Month. Valid values: Month Year |   |
| PayType | String | No | No |   | The billing method of the instance. | Valid values: Postpaid: pay-as-you-go Prepaid: subscription |   |
| Period | Integer | No | No |   | The subscription period of the instance. | Valid values when PeriodType is set to Year: 1 to 3. Valid values when PeriodType is set to Month: 1 to 9. |   |
| TargetDedicat edHostIdForLo g | String | No | No |   | The ID of the host on which to create a logger instance within a dedicated cluster. | None |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SlaveZoneIds | List | No | No | The list of one or more secondary zone IDs that you need to specify when you create a High-availability or Enterprise Edition instance. | A maximum of two secondary zones can be specified. For example, you can set this parameter to ["zone-b"] or ["zone-b", "zone-c"] . You must specify a vSwitch in each primary or secondary zone. For example, if ZoneId is set to "zone-a" and SlaveZoneIds is set to ["zone-c", "zone- b"] , you must set the VSwitchID value in the following format: "vsw-zone-a,vsw-zone- c,vsw-zone-b" |
| SQLCollectorSt atus | String | No | Yes | Specifies whether to enable SQL Explorer and Audit. | Valid values: Enable Disabled |
| SSLSetting | String | No | No | The settings of the SSL connection for the instance. | Default value: Disabled. Valid values: Disabled: The SSL connection is disabled. EnabledForPublicConnection: The SSL connection is enabled. SSL certificates are used to protect public endpoints. Not e If you set this parameter to EnabledForPublicConnecti on, you must set the AllocatePublicConnection parameter to true. EnabledForInnerConnection: The SSL connection is enabled. SSL certificates are used to protect internal endpoints. |

| erprise Edition | b"] |
|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AutoRenew | Boolean | No | No | Specifies whether to enable auto-renewal for the instance. | This parameter is required only when the instance uses the subscription billing method. Valid values: true false Not e If you set the Period parameter to Month, the auto-renewal cycle is one month. If you set the Period parameter to Year, the auto-renewal cycle is one year. |
| LogBackupFre quency | String | No | No | The backup frequency of logs. | Set the value to LogInterval. The value of LogInterval indicates that logs are backed up every 30 minutes. The default value of LogBackupFrequency is the same as that of PreferredBackupPeriod. Not e The LogBackupFrequency parameter is supported only when the instance runs SQL Server. |
| EnableBackupL og | Boolean | No | No | Specifies whether to enable the log backup feature. | Valid values: True: The log backup feature is enabled. False: The log backup feature is disabled. Not e This parameter is required if the BackupPolicyMode parameter is set to LogBackupPolicy. |
| ReleasedKeep Policy | String | No | No | The policy based on which ApsaraDB RDS retains archived backup files after the instance is released. | Valid values: Lastest: Only the last archived backup file is retained. All: All archived backup files are retained. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ArchiveBackup RetentionPerio d | Integer | No | No | The number of days for which archived backup files can be retained. | Valid values: 30 to 1095. Unit: days. |
| ArchiveBackup KeepPolicy | String | No | No | The cycle based on which archived backup files are retained. | Valid values: ByMonth ByWeek KeepAll |
| ArchiveBackup KeepCount | Integer | No | No | The number of archived backup files that can be retained. | Valid values when ArchiveBackupKeepPolicy is set to ByMonth: 1 to 31. Valid values when ArchiveBackupKeepPolicy is set to ByWeek: 1 to 7. When you set ArchiveBackupKeepPolicy to KeepAll, this parameter is not required. Default value: 1. |
| LogBackupRet entionPeriod | Integer | No | No | The number of days for which log backup files can be retained. | Valid values: 7 to 730. The retention period of log backup files cannot be longer than that of data backup files. Not e You can specify the retention period of log backup files if you enable the log backup feature. |
| HighSpaceUsa geProtection | String | No | No | Specifies whether to delete log backup files if the disk capacity is insufficient. The capacity is insufficient if the storage usage of your RDS instance exceeds 80%, or the remaining storage space is less than 5 GB. | Valid values: Enable Disable This parameter is required if the BackupPolicyMode parameter is set to LogBackupPolicy. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LocalLogReten tionSpace | Integer | No | No | The maximum percentage of space allowed to store log backup files on the instance. | Valid values: 0 to 50. If the space usage for log backup files exceeds this percentage, the system deletes earlier binary log files until the space usage falls below this percentage. Not e This parameter is required if the BackupPolicyMode parameter is set to LogBackupPolicy. |
| BackUpCatego ry | String | No | No | Specifies whether to enable level-2 backup. | Valid values: Flash: Level-2 backup is enabled. Standard: Level-2 backup is disabled. |
| CompressType | Integer | No | No | The format used to compress backup data. | Valid values: 1: uses zlib to compress backup data into .tar.gz files. 4: uses QuickLZ to compress backup data into .xb.gz files. This compression format is supported only when the instance runs MySQL 5.6 or 5.7. This format can be used to restore individual databases and tables. 8: uses QuickLZ to compress backup data into .xb.gz files. This compression format is supported only when the instance runs MySQL 8.0. This format cannot be used to restore individual databases or tables. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LocalLogReten tionHours | Integer | No | No | The number of hours for which log backup files can be retained on the instance. | Valid values: 0 to 168. Unit: hours. A value of 0 indicates that log backup files are not retained on the instance. Not e This parameter is required if the BackupPolicyMode parameter is set to LogBackupPolicy. |
| LogBackupLoc alRetentionNu mber | Integer | No | No | The number of log backup files that can be retained on the instance. | Valid values: 6 to 100. Default value: 60. |

DBMappings syntax

```json
"DBMappings": [
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
```

`]` DBMappings properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CharacterSetName | String | Yes | No | The character set. | Valid values when Engine is set to MySQL: utf8 gbk latin1 utf8mb4 (applicable to versions 5.5 and 5.6) Valid values when Engine is set to SQLServer: Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ |
| DBName | String | Yes | No | The name of the database. | The name must be globally unique. The name can be up to 64 characters in length and can contain letters, digits, and underscores ( ). It must _ start with a letter. |
| DBDescription | String | No | No | The description of the database. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |

Response parameters Fn::GetAtt DBInstanceId: the ID of the instance. InnerPort: the internal port of the instance. InnerIPAddress: the internal IP address of the instance. InnerConnectionString: the internal endpoint of the instance. PublicPort: the public port of the instance. PublicConnectionString: the public endpoint of the instance. PublicIPAddress: the public IP address of the instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "PeriodType": {
      "Type": "String",
      "Description": "Charge period for created instances.",
      "AllowedValues": [
        "Month",
        "Year"
```

`],`

```json
      "Default": "Month"
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "ArchiveBackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The number of days for which to retain archived backups. \n The default val
ue 0 specifies not to enable the backup archiving function. Valid values: 30 to 1095.",
      "MinValue": 30,
      "MaxValue": 1095
    "DBTimeZone": {
      "Type": "String",
      "Description": "The UTC time zone of the instance. Valid values: -12:00 to +12:00. The time
zone must be an integer value such as +08:00. Values such as +08:30 are not allowed."
    "Port": {
      "Type": "Number",
      "Description": "The port of the database service.",
      "MinValue": 1,
      "MaxValue": 65535
    "ArchiveBackupKeepCount": {
      "Type": "Number",
      "Description": "The number of archived backups that can be retained. Default value: 1. Vali
d values: \nThe value of this parameter ranges from 1 to 31 when the ArchiveBackupKeepPolicy \n p arameter is set to ByMonth. \nThe value of this parameter ranges from 1 to 7 when the ArchiveBack upKeepPolicy \n parameter is set to ByWeek. \nNote You do not need to specify this parameter when the ArchiveBackupKeepPolicy \nparameter is set to KeepAll.",
      "MinValue": 1,
      "MaxValue": 31
    "LogBackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The number of days for which to retain log backup files. Valid values: 7 to
730. The log backup \n retention period cannot be longer than the data backup retention period. N ote If you enable the log \n backup function, you can specify the log backup retention period. Th is applies only when the \n instance runs MySQL, PostgreSQL, or PPAS.",
      "MinValue": 7,
      "MaxValue": 730
    "DBInstanceStorage": {
      "Type": "Number",
```

`"` `i` `i` `"` `"` `b` `i` `i` `l``i`

```
[51000]
```

`l`

```
20082i [10
```

```json
      "Description": "Database instance storage size. mysql is [5,1000]. sql server 2008r2 is [10
,1000], sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and PPAS is [5,2000]. Increase d every 5 GB, Unit in GB"
    "DBMappings": {
      "Type": "Json",
      "Description": "Database mappings to attach to db instance."
    "ConnectionStringPrefix": {
      "Type": "String",
      "Description": "The prefix of the endpoint. \nOnly the prefix of the CurrentConnectionStrin
g parameter value can be modified.\nThe prefix must be 8 to 64 characters in length and can conta in letters, digits, and hyphens (-). ",
      "AllowedPattern": "[a-zA-Z0-9-]{8,64}"
    "MultiAZ": {
      "Type": "Boolean",
      "Description": "Specifies if the database instance is a multiple Availability Zone deployme
nt. ",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "Engine": {
      "Type": "String",
      "Description": "Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS/Mari
aDB now.",
      "AllowedValues": [
        "MySQL",
        "SQLServer",
        "PostgreSQL",
        "PPAS",
        "MariaDB"
```

`]`

```json
    "Tags": {
      "Type": "Json",
      "Description": "The tags of an instance.\nYou should input the information of the tag with
the format of the Key-Value, such as {\"key1\":\"value1\",\"key2\":\"value2\", ... \"key5\":\"val ue5\"}.\nAt most 5 tags can be specified.\nKey\nIt can be up to 64 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or https://.\nCannot be a null string.\nValue\nIt c an be up to 128 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or ht tps://.\nCan be a null string."
    "DBInstanceDescription": {
      "Type": "String",
      "Description": "Description of created database instance."
    "TargetDedicatedHostIdForMaster": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a primary in
stance in a host group." "EngineVersion":{
```

```json
    EngineVersion: {
      "Type": "String",
      "Description": "Database instance version of the relative engine type.Support MySQL: 5.5/5.
6/5.7/8.0;\nSQLServer: 2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_ web/2017_std_ha/2017_ent;\nPostgreSQL: 9.4/10.0/11.0/12.0;\nPPAS: 9.3/10.0;\nMariaDB: 10.3."
    "DBInstanceClass": {
      "Type": "String",
      "Description": "Database instance type. Refer the RDS database instance type reference, suc
h as 'rds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc"
    "ArchiveBackupKeepPolicy": {
      "Type": "String",
      "Description": "The period for which to retain archived backups. The number of archived bac
kups that can \n be retained within the specified period is determined by the ArchiveBackupKeepCo unt parameter. \n Default value: 0. Valid values: \nByMonth \n ByWeek \n KeepAll",
      "AllowedValues": [
        "ByMonth",
        "ByWeek",
        "KeepAll"
```

`]`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The vSwitch id of created instance. For VPC network, the property is requir
ed."
    "BackupPolicyMode": {
      "Type": "String",
      "Description": "Backup type, \nDataBackupPolicy: data backup \nLogBackupPolicy: log backup"
```

`,`

```json
      "AllowedValues": [
        "DataBackupPolicy",
        "LogBackupPolicy"
```

`]`

```json
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. While choose by pay by month, it could be from 1 to 9.
While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
    "LocalLogRetentionHours": {
      "Type": "Number",
      "Description": "The number of hours for which to retain log backup files on the instance. \
nValid values: 0 to 168. The value 0 specifies not to retain log backup files on the instance. \n You can retain the default value. Note You must specify this parameter when the BackupPolicyMode \nparameter is set to LogBackupPolicy.",
      "MinValue": 0,
      "MaxValue": 168
    "PayType": {
      "Type": "String",
      "Description": "The charge type of created instance.",
      "AllowedValues": [
        "Subscription",
```

```
        "PrePaid",
        "PrePay",
        "Prepaid",
        "PayAsYouGo",
        "PostPaid",
        "PayOnDemand",
        "Postpaid"
```

`],`

```json
      "Default": "Postpaid"
    "HighSpaceUsageProtection": {
      "Type": "String",
      "Description": "Specifies whether to forcibly delete log backup files when the space usage
of the \n instance exceeds 80% or the remaining space is less than 5 GB. Valid values: \n Enable and Disable. You can retain the default value. Note You must specify \n this parameter when the B ackupPolicyMode parameter is set to LogBackupPolicy.",
      "AllowedValues": [
        "Enable",
        "Disable"
```

`]`

```json
    "RoleARN": {
      "Type": "String",
      "Description": "The Alibaba Cloud Resource Name (ARN) provided to the service account of th
e instance by your Alibaba Cloud account to connect to KMS. You can copy the ARN from the RAM con sole."
    "MasterUserPassword": {
      "Type": "String",
      "Description": "The master password for the database instance. ",
      "MinLength": 8,
      "MaxLength": 32
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id of created database instance. For VPC network, the property is r
equired."
    "SSLSetting": {
      "Type": "String",
      "Description": "Secure Sockets Layer (SSL) link setting of the instance. Valid values:\nDis
abled: Disable SSL\nEnabledForPublicConnection: Public connection address will be protected by th e SSL certificate. It requires AllocatePublicConnection is true.\nEnabledForInnerConnection: Priv ate connection address will be protected by the SSL certificate.\nDefault value is Disabled.",
      "AllowedValues": [
        "Disabled",
        "EnabledForPublicConnection",
        "EnabledForInnerConnection"
```

`],`

```json
      "Default": "Disabled"
    "MasterUsername": {
      "Type": "String",
      "Description": "The master user name for the database instance. "
    "ConnectionMode": {
      "Type": "String",
```

```json
      "Description": "Connection Mode for database instance,support 'Standard' and 'Safe' mode. D
efault is RDS system assigns. "
    "LocalLogRetentionSpace": {
      "Type": "Number",
      "Description": "The maximum percentage of space that is allowed to store log backup files o
n the instance. \n If the space usage for log backup files exceeds this percentage, the system de letes earlier \n log backup files until the space usage falls below this percentage. Valid values :0 to 50. \n You can retain the default value. Note You must specify this parameter when the \n B ackupPolicyMode parameter is set to LogBackupPolicy.",
      "MinValue": 0,
      "MaxValue": 50
    "Category": {
      "Type": "String",
      "Description": "The edition of the instance. Valid values:\nBasic: specifies to use the Bas
ic Edition.\nHighAvailability: specifies to use the High-availability Edition.\nAlwaysOn: specifi es to use the Cluster Edition.\nFinance: specifies to use the Enterprise Edition.",
      "AllowedValues": [
        "Basic",
        "HighAvailability",
        "AlwaysOn",
        "Finance"
```

`]`

```json
    "PrivateIpAddress": {
      "Type": "String",
      "Description": "The private ip for created instance."
    "TargetDedicatedHostIdForSlave": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a secondary
instance in a host group."
    "DBInstanceNetType": {
      "Type": "String",
      "Description": "Database instance net type, default is Intranet.Internet for public access,
Intranet for private access.",
      "AllowedValues": [
        "Internet",
        "Intranet"
```

`],`

```json
      "Default": "Intranet"
    "ReleasedKeepPolicy": {
      "Type": "String",
      "Description": "The policy used to retain archived backups if the instance is released. Def
ault value: None. \n Valid values: \nLastest: Only the last archived backup is retained. \n All: All of the archived backups are retained.",
      "AllowedValues": [
        "Lastest",
        "All"
```

`]`

```json
    "DedicatedHostGroupId": {
      "Type": "String",
      "Description": "The ID of the host group to which the instance belongs if you create an ins
tanceinahostgroup"
```

```json
tance in a host group."
    "AutoRenew": {
      "Type": "Boolean",
      "Description": "Specifies whether to enable auto-renewal. Valid values: true and false. Not
e\n:Monthly subscription: The auto-renewal cycle is one month.\nAnnual subscription: The auto-ren ewal cycle is one year.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "EncryptionKey": {
      "Type": "String",
      "Description": "The ID of the encryption key that is used to encrypt data on SSDs in the re
gion. You can view the encryption key ID in the Key Management Service (KMS) console. You can als o create an encryption key."
    "PreferredBackupPeriod": {
      "Type": "CommaDelimitedList",
      "Description": "The backup period. Separate multiple values with commas (,). The default va
lue is the original value. Valid values:Monday Tuesday Wednesday Thursday Friday Saturday Sunday Note When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
    "LogBackupLocalRetentionNumber": {
      "Type": "Number",
      "Description": "The number of log backup files that can be retained on the instance. \nDefa
ult value: 60. Valid values: 6 to 100.",
      "MinValue": 6,
      "MaxValue": 100
    "SlaveZoneIds": {
      "Type": "Json",
      "Description": "List of slave zone ids can specify slave zone ids when creating the high-av
ailability or enterprise edition instance. Meanwhile, VSwitchId needs to pass in the correspondin g vswitch id to the slave zone by order. For example, ZoneId = \"zone-a\" and SlaveZoneIds = [\"z one-c\", \"zone-b\"], then the VSwitchId must be \"vsw-zone-a,vsw-zone-c,vsw-zone-b\". Of course, you can also choose automatic allocation, for example, ZoneId = \"zone-a\" and SlaveZoneIds = [\" Auto\", \"Auto\"], then the VSwitchId must be \"vsw-zone-a,Auto,Auto\". The list contains up to 2 slave zone ids, separated by commas.",
      "MaxLength": 2
    "SecurityIPList": {
      "Type": "String",
      "Description": "Security ip to access the database instance, combine with comma, 0.0.0.0/0
means no limitation."
    "DBIsIgnoreCase": {
      "Type": "Number",
      "Description": "Specifies whether table names are case-sensitive. Valid values:\n1: Table n
ames are not case-sensitive. This is the default value.\n0: Table names are case-sensitive."
    "MaintainTime": {
      "Type": "String",
      "Description": "The period during which the maintenance performs. The format is HH:mmZ-HH:m
mZ."
```

```json
    "DBParamGroupId": {
      "Type": "String",
      "Description": "The ID of the parameter template used by the instance."
    "ZoneId": {
      "Type": "String",
      "Description": "selected zone to create database instance. You cannot set the ZoneId parame
ter if the MultiAZ parameter is set to true."
    "TargetDedicatedHostIdForLog": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a log instan
ce in a host group."
    "AllocatePublicConnection": {
      "Type": "Boolean",
      "Description": "If true, allocate public connection automate.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "PreferredBackupTime": {
      "Type": "String",
      "Description": "The time when the backup task is performed. Format: yyyy-MM-ddZ-HH:mm:ssZ.N
ote When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
    "SecurityGroupId": {
      "Type": "String",
      "Description": "The ID of the ECS security groups. \nEach RDS instance can be associated wi
th up to three ECS security groups. \nYou must separate them with commas (,). \nTo delete an ECS Security group, leave this parameter empty. \n"
    "DBInstanceStorageType": {
      "Type": "String",
      "Description": "The storage type of the instance. Valid values:\nlocal_ssd: specifies to us
e local SSDs. This is the recommended storage type.\ncloud_ssd: specifies to use standard SSDs.\n cloud_essd: specifies to use enhanced SSDs."
    "BackUpCategory": {
      "Type": "String",
      "Description": "Specifies whether to enable the second-level backup function. This function
allows a backup \nto be completed within seconds. Valid values: \nFlash: specifies to enable the second-level backup function. \n Standard: specifies to disable the second-level backup function.
```

`",`

```json
      "AllowedValues": [
        "Flash",
        "Standard"
```

`]`

```json
    "CompressType": {
      "Type": "Number",
      "Description": "The format used to compress backups. Valid values: \n 1: The zlib tool is u
sed to compress backups into .tar.gz files. \n 4: The QuickLZ tool is used to compress backups in
```

```json
to .xb.gz files. \nThis compression format is supported only when the instance runs MySQL 5.6 or 5.7. \nIt can be used to restore individual databases and tables. \n 8: The QuickLZ tool is used to compress backups into .xb.gz files. \n This compression format is supported only when the inst ance runs MySQL 8.0. \nIt cannot be used to restore individual databases or tables."
    "LogBackupFrequency": {
      "Type": "String",
      "Description": "The frequency at which to back up logs. Valid values: \nThe value LogInterv
al specifies to back up logs every 30 minutes. \n The default value of this parameter is the same as the data backup frequency. \nNote The value LogInterval is supported only when the instance ru ns SQL Server."
    "ConnectionStringType": {
      "Type": "String",
      "Description": "The endpoint type of the instance, allow values: Inner, Public",
      "AllowedValues": [
        "Inner",
        "Public"
```

`],`

```json
      "Default": "Inner"
    "MasterUserType": {
      "Type": "String",
      "Description": "Privilege type of account.\n Normal: Common privilege. \n Super: High privi
lege. \nSysadmin: Super privileges (SA) (only supported by SQL Server)\nThe default value is Norm al.",
      "AllowedValues": [
        "Normal",
        "Super",
        "Sysadmin"
```

`],`

```json
      "Default": "Normal"
    "EnableBackupLog": {
      "Type": "Boolean",
      "Description": "Specifies whether to enable the log backup function. Valid values: \nTrue:
specifies to enable the log backup function. \nFalse: specifies to disable the log backup functio n. \nNote You must specify this parameter when the BackupPolicyMode parameter is set to LogBackup Policy.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "SQLCollectorStatus": {
      "Type": "String",
      "Description": "Specifies whether to enable or disable the SQL Explorer (SQL audit) feature
. \nValid values:Enable | Disabled.",
      "AllowedValues": [
        "Enable",
        "Disabled"
```

`]`

```json
    "BackupRetentionPeriod": {
      "Type": "Number",
```

`"` `i` `i` `"` `"``h` `i` `i``d` `f` `h` `d` `b` `k` `l` `h` `d``f` `l`

```json
      "Description": "The retention period of the data backup. Value range: 7 to 730. The default
value is the original value. Note When the BackupPolicyMode parameter is set to LogBackupPolicy, this parameter is required.",
      "Default": 7
  "Resources": {
    "DBInstance": {
      "Type": "ALIYUN::RDS::DBInstance",
      "Properties": {
        "PeriodType": {
          "Ref": "PeriodType"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "ArchiveBackupRetentionPeriod": {
          "Ref": "ArchiveBackupRetentionPeriod"
        "DBTimeZone": {
          "Ref": "DBTimeZone"
        "Port": {
          "Ref": "Port"
        "ArchiveBackupKeepCount": {
          "Ref": "ArchiveBackupKeepCount"
        "LogBackupRetentionPeriod": {
          "Ref": "LogBackupRetentionPeriod"
        "DBInstanceStorage": {
          "Ref": "DBInstanceStorage"
        "DBMappings": {
          "Ref": "DBMappings"
        "ConnectionStringPrefix": {
          "Ref": "ConnectionStringPrefix"
        "MultiAZ": {
          "Ref": "MultiAZ"
        "Engine": {
          "Ref": "Engine"
        "Tags": {
          "Ref": "Tags"
        "DBInstanceDescription": {
          "Ref": "DBInstanceDescription"
        "TargetDedicatedHostIdForMaster": {
          "Ref": "TargetDedicatedHostIdForMaster"
        "EngineVersion": {
          "Ref": "EngineVersion"
```

```json
        "DBInstanceClass": {
          "Ref": "DBInstanceClass"
        "ArchiveBackupKeepPolicy": {
          "Ref": "ArchiveBackupKeepPolicy"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "BackupPolicyMode": {
          "Ref": "BackupPolicyMode"
        "Period": {
          "Ref": "Period"
        "LocalLogRetentionHours": {
          "Ref": "LocalLogRetentionHours"
        "PayType": {
          "Ref": "PayType"
        "HighSpaceUsageProtection": {
          "Ref": "HighSpaceUsageProtection"
        "RoleARN": {
          "Ref": "RoleARN"
        "MasterUserPassword": {
          "Ref": "MasterUserPassword"
        "VpcId": {
          "Ref": "VpcId"
        "SSLSetting": {
          "Ref": "SSLSetting"
        "MasterUsername": {
          "Ref": "MasterUsername"
        "ConnectionMode": {
          "Ref": "ConnectionMode"
        "LocalLogRetentionSpace": {
          "Ref": "LocalLogRetentionSpace"
        "Category": {
          "Ref": "Category"
        "PrivateIpAddress": {
          "Ref": "PrivateIpAddress"
        "TargetDedicatedHostIdForSlave": {
          "Ref": "TargetDedicatedHostIdForSlave"
        "DBInstanceNetType": {
          "Ref": "DBInstanceNetType"
```

```json
        "ReleasedKeepPolicy": {
          "Ref": "ReleasedKeepPolicy"
        "DedicatedHostGroupId": {
          "Ref": "DedicatedHostGroupId"
        "AutoRenew": {
          "Ref": "AutoRenew"
        "EncryptionKey": {
          "Ref": "EncryptionKey"
        "PreferredBackupPeriod": {
          "Ref": "PreferredBackupPeriod"
        "LogBackupLocalRetentionNumber": {
          "Ref": "LogBackupLocalRetentionNumber"
        "SlaveZoneIds": {
          "Ref": "SlaveZoneIds"
        "SecurityIPList": {
          "Ref": "SecurityIPList"
        "DBIsIgnoreCase": {
          "Ref": "DBIsIgnoreCase"
        "MaintainTime": {
          "Ref": "MaintainTime"
        "DBParamGroupId": {
          "Ref": "DBParamGroupId"
        "ZoneId": {
          "Ref": "ZoneId"
        "TargetDedicatedHostIdForLog": {
          "Ref": "TargetDedicatedHostIdForLog"
        "AllocatePublicConnection": {
          "Ref": "AllocatePublicConnection"
        "PreferredBackupTime": {
          "Ref": "PreferredBackupTime"
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        "DBInstanceStorageType": {
          "Ref": "DBInstanceStorageType"
        "BackUpCategory": {
          "Ref": "BackUpCategory"
        "CompressType": {
          "Ref": "CompressType"
```

```json
        "LogBackupFrequency": {
          "Ref": "LogBackupFrequency"
        "ConnectionStringType": {
          "Ref": "ConnectionStringType"
        "MasterUserType": {
          "Ref": "MasterUserType"
        "EnableBackupLog": {
          "Ref": "EnableBackupLog"
        "SQLCollectorStatus": {
          "Ref": "SQLCollectorStatus"
        "BackupRetentionPeriod": {
          "Ref": "BackupRetentionPeriod"
  "Outputs": {
    "InnerConnectionString": {
      "Description": "DB instance connection url by Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "InnerConnectionString"
```

`]`

```json
    "DBInstanceId": {
      "Description": "The instance id of created database instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "DBInstanceId"
```

`]`

```json
    "InnerIPAddress": {
      "Description": "IP Address for created DB instance of Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "InnerIPAddress"
```

`]`

```json
    "PublicConnectionString": {
      "Description": "DB instance connection url by Internet.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "PublicConnectionString"
```

`]`

```json
    "PublicIPAddress": {
      "Description": "IP Address for created DB instance of Internet.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "PublicIPAddress"
```

`]`

```json
    "PublicPort": {
      "Description": "Internet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "PublicPort"
```

`]`

```json
    "InnerPort": {
      "Description": "Intranet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstance",
          "InnerPort"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AllocatePublicConnection:
    AllowedValues:
    - 'True'
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
```

```
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
  AutoRenew:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Description: 'Specifies whether to enable auto-renewal. Valid values: true and
      false. Note
      :Monthly subscription: The auto-renewal cycle is one month.
      Annual subscription: The auto-renewal cycle is one year.'
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
Type:String
```

```
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
```

```
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
      SQLServer: 2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/20
17_std_ha/2017_ent;
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
```

```
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
      \ backup retention period. Note If you enable the log \n backup function, you\
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
```

`f` `l` `l`

```
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
  PayType:
    AllowedValues:
    - Subscription
    - PrePaid
    - PrePay
    - Prepaid
    - PayAsYouGo
    - PostPaid
    - PayOnDemand
    - Postpaid
    Default: Postpaid
    Description: The charge type of created instance.
    Type: String
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
Description:'Thetimewhenthebackuptaskisperformed Format:yyyy-MM-ddZ-HH:mm:ssZNote
```

```
    Description: The time when the backup task is performed. Format: yyyyMMddZHH:mm:ssZ.Note
      When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter
      is required.'
    Type: String
  PrivateIpAddress:
    Description: The private ip for created instance.
    Type: String
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
      SSL certificate.
      Default value is Disabled.'
    Type: String
  SecurityGroupId:
    Description: "The ID of the ECS security groups. \nEach RDS instance can be associated\
      \ with up to three ECS security groups. \nYou must separate them with commas\
      \ (,). \nTo delete an ECS Security group, leave this parameter empty. \n"
    Type: String
  SecurityIPList:
    Description: Security ip to access the database instance, combine with comma,
      0.0.0.0/0 means no limitation.
    Type: String
  SlaveZoneIds:
    Description: List of slave zone ids can specify slave zone ids when creating the
      high-availability or enterprise edition instance. Meanwhile, VSwitchId needs
      to pass in the corresponding vswitch id to the slave zone by order. For example,
      ZoneId = "zone-a" and SlaveZoneIds = ["zone-c", "zone-b"], then the VSwitchId
```

```
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
  DBInstance:
    Properties:
      AllocatePublicConnection:
        Ref: AllocatePublicConnection
      ArchiveBackupKeepCount:
        Ref: ArchiveBackupKeepCount
      ArchiveBackupKeepPolicy:
        Ref: ArchiveBackupKeepPolicy
      ArchiveBackupRetentionPeriod:
        Ref: ArchiveBackupRetentionPeriod
```

```
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
      CompressType:
        Ref: CompressType
      ConnectionMode:
        Ref: ConnectionMode
      ConnectionStringPrefix:
        Ref: ConnectionStringPrefix
      ConnectionStringType:
        Ref: ConnectionStringType
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
Ref:LogBackupRetentionPeriod
```

```
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
      PayType:
        Ref: PayType
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
      SecurityIPList:
        Ref: SecurityIPList
      SlaveZoneIds:
        Ref: SlaveZoneIds
      Tags:
        Ref: Tags
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
    Type: ALIYUN::RDS::DBInstance
Outputs:
  DBInstanceId:
```

```
    Description: The instance id of created database instance.
    Value:
      Fn::GetAtt:
      - DBInstance
      - DBInstanceId
  InnerConnectionString:
    Description: DB instance connection url by Intranet.
    Value:
      Fn::GetAtt:
      - DBInstance
      - InnerConnectionString
  InnerIPAddress:
    Description: IP Address for created DB instance of Intranet.
    Value:
      Fn::GetAtt:
      - DBInstance
      - InnerIPAddress
  InnerPort:
    Description: Intranet port of created DB instance.
    Value:
      Fn::GetAtt:
      - DBInstance
      - InnerPort
  PublicConnectionString:
    Description: DB instance connection url by Internet.
    Value:
      Fn::GetAtt:
      - DBInstance
      - PublicConnectionString
  PublicIPAddress:
    Description: IP Address for created DB instance of Internet.
    Value:
      Fn::GetAtt:
      - DBInstance
      - PublicIPAddress
  PublicPort:
    Description: Internet port of created DB instance.
    Value:
      Fn::GetAtt:
      - DBInstance
      - PublicPort
```

To view more examples, visit DBInstance.json and DBInstance.yml. In the examples, the ALIYUN::RDS::DBInstance, ALIYUN::RDS::Account, ALIYUN::RDS::AccountPrivilege, ALIYUN::RDS::DBInstanceParameterGroup, ALIYUN::RDS::DBInstanceSecurityIps, ALIYUN::RDS::ReadOnlyDBInstance, and ALIYUN::RDS::Database resource types are involved.

#### 6.5.4 ALIYUN::RDS::DBInstanceParameterGroup

ALIYUN::RDS::DBInstanceParameterGroup is used to modify the parameters of an ApsaraDB RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
  "Properties": {
    "Forcerestart": String,
    "DBInstanceId": String,
    "Parameters": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | Yes | No | The ID of the instance. | N/A |
| Parameters | List | Yes | Yes | The parameters of the instance. | For more information, see Parameters properties. |
| Forcerestart | String | No | Yes | Specifies whether to forcibly restart the instance. | Valid values: true: The system forcibly restarts the instance. false: The system does not forcibly restart the instance. This is the default value. |

Parameters syntax

```json
"Parameters": [
    "Key": String,
    "Value": String
```

`]` Parameters properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The name of the parameter. | N/A |
| Value | String | Yes | No | The value of the parameter. | N/A |

Response parameters Fn::GetAtt N/A Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Parameters": {
      "Type": "Json",
      "Description": "Parameters to update for selected database instance.",
      "Default": {"delayed_insert_timeout":"600","max_length_for_sort_data":"2048"}
    "DBInstanceId": {
      "Type": "String",
      "Description": "Database InstanceId to update properties."
      "Default": rm-uf6wjk5xxxxxxx
    "Forcerestart": {
      "Type": "String",
      "Description": "whether restart database instance.",
      "AllowedValues": [
        "true",
        "false"
```

`],`

```json
      "Default": "false"
  "Resources": {
    "DBInstanceParameterGroup": {
      "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
      "Properties": {
        "Parameters": {
          "Ref": "Parameters"
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        "Forcerestart": {
          "Ref": "Forcerestart"
```

#### 6.5.5 ALIYUN::RDS::DBInstanceSecurityIps

ALIYUN::RDS::DBInstanceSecurityIps is used to modify an IP address whitelist of an ApsaraDB for RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
  "Properties": {
    "DBInstanceId": String,
    "DBInstanceIPArrayName": String,
    "DBInstanceIPArrayAttribute": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | Yes | No | The ID of the instance. | None |
| DBInstanceIPArr ayAttribute | String | Yes | Yes | The attribute of the IP address whitelist. | Whitelists that have the "hidden" attribute are not displayed in the console. |
| DBInstanceIPArr ayName | String | No | No | The name of the IP address whitelist. | The name can only contain lowercase letters and underscores ( ). _ Default value: Default. |

Response parameters Fn::GetAtt SecurityIps: the IP address whitelist after the modification. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DBInstanceSecurityIps": {
      "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
      "Properties": {
        "DBInstanceIPArrayName": {
          "Ref": "DBInstanceIPArrayName"
        "DBInstanceId": {
          "Ref": "DBInstanceId"
        "DBInstanceIPArrayAttribute": {
          "Ref": "DBInstanceIPArrayAttribute"
  "Parameters": {
    "DBInstanceIPArrayName": {
      "Type": "String",
      "Description": "Group name of the security ips, only support lower characters and '_'. Advi
ce use a new group name avoid effect your database system. If the properties is not specified, it will set to default group, please be careful."
    "DBInstanceId": {
      "Type": "String",
      "Description": "Database instance id to update security ips."
    "DBInstanceIPArrayAttribute": {
      "Type": "String",
      "Description": "Security ips to add or remove."
  "Outputs": {
    "SecurityIps": {
      "Description": "The security ips of selected database instance.",
      "Value": {
        "Fn::GetAtt": [
          "DBInstanceSecurityIps",
          "SecurityIps"
```

`]`

#### 6.5.6 ALIYUN::RDS::PrepayDBInstance

ALIYUN::RDS::PrepayDBInstance is used to create a subscription ApsaraDB RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::PrepayDBInstance",
"Properties":{
```

```json
  Properties: {
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
    "ConnectionStringPrefix": String,
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
```

`g` `p` `q` `y` `g,`

```json
    "BackupPolicyMode": String,
    "ArchiveBackupKeepCount": Integer,
    "LocalLogRetentionSpace": Integer,
    "ReleasedKeepPolicy": String,
    "BackUpCategory": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | No | Yes | The ID of the resource group to which the instance belongs. | None |
| DBMappings | List | No | No | The list of one or more databases to be created in the instance. | For more information, see DBMappings properties. |
| CouponCode | String | No | No | The coupon code. | None |
| MasterUsername | String | No | No | The name of the database account. | The name must be globally unique. The name must be 2 to 16 characters in length and can contain letters, digits, and underscores ( ). It must _ start with a letter and end with a letter or digit. |
| PeriodType | String | Yes | No | The unit of the subscriptio n period. | Default value: Month. Valid values: Year Month |
| DBInstanceNetType | String | No | No | The network type of the instance. | Default value: Intranet. Valid values: Internet Intranet |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterUserType | String | No | No | The type of the database account. | Default value: Normal. Valid values: Normal: standard account Super: privileged account Sysadmin: administrator account Not e This parameter can be set to Sysadmin only when the Engine parameter is set to SQLServer. |
| Port | Integer | No | Yes | The port that is used to connect to the instance. | None |
| ConnectionStringPre fix | String | No | Yes | The prefix of the endpoint. | The prefix must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). |
| ConnectionStringTy pe | String | No | Yes | The type of the endpoint. | Valid values: Inner: VPC Public: Internet |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PreferredBackupTim e | String | No | No | The backup window. | Specify the window in the HH:mmZ-HH:mmZ format. Value values: 00:00Z- 01:00Z, 01:00Z-02:00Z, 02:00Z-03:00Z, 03:00Z- 04:00Z, 04:00Z-05:00Z, 05:00Z-06:00Z, 06:00Z- 07:00Z, 07:00Z-08:00Z, 08:00Z-09:00Z, 09:00Z- 10:00Z, 10:00Z-11:00Z, 11:00Z-12:00Z, 12:00Z- 13:00Z, 13:00Z-14:00Z, 14:00Z-15:00Z, 15:00Z- 16:00Z, 16:00Z-17:00Z, 17:00Z-18:00Z, 18:00Z- 19:00Z, 19:00Z-20:00Z, 20:00Z-21:00Z, 21:00Z- 22:00Z, 22:00Z-23:00Z, and 23:00Z-24:00Z. |
| PrivateIpAddress | String | No | No | The private IP address in the CIDR block of the specified vSwitch. | If you do not specify this parameter, the system allocates a private IP address. |
| Engine | String | Yes | No | The type of the database engine. | Valid values: MySQL SQLServer PostgreSQL PPAS MariaDB |
| MultiAZ | Boolean | No | No | Specifies whether the instance can be deployed across multiple zones. | Valid values: true false |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VpcId | String | No | No | The ID of the virtual private cloud (VPC). | None |
| ConnectionMode | String | No | No | The connection mode of the instance. | Default value: Safe. Valid values: Standard: the standard mode Not e If you create an instance that runs SQL Server 2012, SQL Server 2016, or SQL Server 2017, you can set this parameter only to Standard. Safe: the database proxy mode If you do not specify this parameter, the system assigns a connection mode. |
| AutoRenew | Boolean | No | No | Specifies whether to enable auto- renewal for the instance. | Valid values: true false |
| VSwitchId | String | No | No | The ID of the vSwitch in the specified VPC. | None |
| BackupRetentionPer iod | Number | No | No | The number of days for which backup files can be retained. | None |
| Quantity | Number | No | No | The number of instances to be created. | Valid values: 1 to 99. Default value: 1. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CommodityCode | String | Yes | No | The commodity code. | Valid values: rds bards rords |
| ZoneId | String | No | No | The zone ID of the instance. | None |
| EngineVersion | String | Yes | No | The version of the database engine. | Valid values: Valid values when Engine is set to MySQL: 5.5, 5.6, 5.7, and 8.0. Valid values when Engine is set to SQLServer: 2008r2, 08r2 ent ha, _ _ 2012, 2012 ent ha, _ _ 2012 std ha, 2012 web, _ _ _ 2014 std ha, _ _ 2016 ent ha, _ _ 2016 std ha, 2016 web, _ _ _ 2017 std ha, 2017 ent, _ _ _ and 2019 ent. _ Valid values when Engine is set to PostgreSQL: 9.4, 10.0, 11.0, and 12.0. Valid values when Engine is set to PPAS: 9.3 and 10.0. Set the value to 10.3 when Engine is set to MariaDB. |
| DBInstanceClass | String | Yes | Yes | The instance type. | Examples: rds.mys2.large, rds.mss1.large, and rds.pg.s1.small. |
| PreferredBackupPeri od | List | No | No | The backup cycle. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

| Property | Type | Required | Editable |   | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| DBInstanceStorage | Integer | Yes | Yes |   | The storage capacity of the instance. | Valid values: Valid values when Engine is set to MySQL: 5 to 1000. Valid values when Engine is set to SQLServer: 10 to 1000. Valid values when Engine is set to PostgreSQL or PPAS: 5 to 2000. Unit: GB. Not e This value must be in 5 GB increments. |   |   |
| DBInstanceDescripti on | String | No | No |   | The description of the instance. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |   |   |
| Tags | Map | No | Yes |   | The tags of the instance. | None |   |   |
| Period | Number | Yes | No |   | The subscriptio n period. | Valid values: Valid values when PeriodType is set to Month: 1 to 9. Valid values when PeriodType is set to Year: 1 to 3. |   |   |
| MasterUserPasswor d | String | No | No |   | The password of the database account. | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !@ # $ &amp ; % ^ * ( |   |   |
|   |   |   |   |   |   |   | !@ # $ &amp ; % ^ * ( |   |
|   |   |   |   |   |   | ) + - = . _ |   |   |

| Property | Type | Required | Editable |   | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|
| AllocatePublicConn ection | Boolean | No | No |   | Specifies whether to apply for a public endpoint for the instance. |   | Valid values: true false |   |   |
| AutoPay | Boolean | No | No |   | Specifies whether to enable automatic payment for the instance. |   | Default value: false. Valid values: true false |   |   |
| SlaveZoneIds | List | No | No |   |   |   | A maximum of two secondary zones can be specified. For example, you can set this parameter to ["zone-b"] or ["zone-b", "zone- c"] . You must specify a vSwitch for each primary or secondary zone. For example, if ZoneId is set to "zone-a" and SlaveZoneIds is set to ["zone-c", "zone- b"] , you must set the VSwitchID value in the following format: "vsw- |   |   |
|   |   |   |   |   |   |   | c"] |   |   |
|   |   |   |   |   | The list of one or more secondary |   |   |   |   |
|   |   |   |   |   | zone IDs that you |   | b"] |   |   |
|   |   |   |   |   | must specify when you |   |   |   |   |
|   |   |   |   |   |   |   |   | "vsw- |   |
|   |   |   |   |   |   | u | zone-a,vsw-zone-c,vsw- |   |   |
|   |   |   |   |   | create a |   | zone-b" |   |   |
|   |   |   |   |   | High- availability or Enterprise Edition instance. |   |   |   |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TargetDedicatedHo stIdForMaster | String | No | No | The ID of the host on which to create a primary instance within a dedicated cluster. | None |
| RoleARN | String | No | No | The Alibaba Cloud Resource Name (ARN) that is provided to the service account of the instance by your Alibaba Cloud account. This ARN is used to connect to Key Manageme nt Service (KMS). | None |
| DBInstanceStorageT ype | String | No | No | The storage type of the instance. | Valid values: local ssd: local SSD. This _ is the recommended storage type. cloud ssd: standard _ SSD. cloud essd: enhanced _ SSD (ESSD). |
| Category | String | No | No | The edition of the instance. | Valid values: Basic: Basic Edition HighAvailability: High- availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBParamGroupId | String | No | No | The ID of the parameter template to be used by the instance. | None |
| EncryptionKey | String | No | No | The ID of the encryption key that is used to encrypt data on SSDs in the region. | You can view the ID of an existing encryption key or create an encryption key in the KMS console. |
| DBIsIgnoreCase | Integer | No | No | Specifies whether table names are case- sensitive. | Default value: 1. Valid values: 1: Table names are case- insensitive. 0: Table names are case- sensitive. |
| SecurityGroupId | String | No | Yes | The ID of the associated security group. | Each ApsaraDB RDS instance can be associated with up to three security groups. Separate multiple security groups with commas (,). To delete all security groups, set this parameter to an empty string. |
| TargetDedicatedHo stIdForLog | String | No | No | The ID of the host on which to create a logger instance within a dedicated cluster. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBTimeZone | String | No | No | The UTC time zone of the instance. | Valid values: -12:59 to +13:00. If you do not specify this parameter, the system assigns the default time zone of the region to which the instance belongs. If you create an instance that has local SSDs attached, you can name the time zone. |
| DedicatedHostGrou pId | String | No | No | The ID of the dedicated cluster in which to create instances. | None |
| TargetDedicatedHo stIdForSlave | String | No | No | The ID of the host on which to create a secondary instance within a dedicated cluster. | None |
| MaintainTime | String | No | No | The maintenanc e window of the instance. | Specify the window in the HH:mmZ-HH:mmZ format. |
| SQLCollectorStatus | String | No | Yes | Specifies whether to enable SQL Explorer and Audit. | Valid values: Enable Disabled |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SSLSetting | String | No | No | The settings of the SSL connection for the instance. | Default value: Disabled. Valid values: Disabled: The SSL connection is disabled. EnabledForPublicConnect ion: The SSL connection is enabled. SSL certificates are used to protect public endpoints. Not e If you set this parameter to EnabledForPublicCon nection, you must set the AllocatePublicConne ction parameter to true. EnabledForInnerConnecti on: The SSL connection is enabled. SSL certificates are used to protect internal endpoints. |
| ArchiveBackupReten tionPeriod | Integer | No | No | The number of days for which archived backup files can be retained. | None |
| LogBackupRetentio nPeriod | Integer | No | No | The number of days for which log backup files can be retained. | None |
| EnableBackupLog | Boolean | No | No | Specifies whether to enable the log backup feature. | Valid values: true: The log backup feature is enabled. false: The log backup feature is disabled. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LogBackupLocalRet entionNumber | Integer | No | No | The number of binary log files that can be retained on the instance. | None |
| ArchiveBackupKeep Policy | String | No | No | The cycle based on which archived backup files are retained. | Valid values: ByMonth ByWeek KeepAll ArchiveBackupKeepCount determines the number of backup files that can be retained within the cycle. The default value is 0. Not e This parameter is valid when the BackupPolicyMode parameter is set to DataBackupPolicy. |
| LocalLogRetentionH ours | Integer | No | No | The number of hours for which log backup files can be retained on the instance. | None |
| HighSpaceUsagePro tection | String | No | No | Specifies whether to enable the feature that is used to delete binary log files if the disk usage exceeds 80% or the remaining disk space is less than 5 GB on the instance. | Valid values: Disable: Binary log files are not deleted. Enable: Binary log files are deleted. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CompressType | Integer | No | No | The format used to compress backup data. | Valid values: 0: Data is not compressed. 1: Backup data is compressed by using zlib. 2: Backup data is compressed by using zlib that invokes more than one thread in parallel for each backup. 4: Backup data is compressed by using QuickLZ and can be used to restore individual databases and tables. 8: Backup data is compressed by using QuickLZ but cannot be used to restore individual databases or tables. This value is available only when the instance runs MySQL 8.0. |
| LogBackupFrequenc y | String | No | No | The backup frequency of logs. | This parameter is available only when the instance runs SQL Server. Set the value to LogInterval. The value of LogInterval indicates that logs are backed up every 30 minutes. Not e The default frequency is the same as the value of the PreferredBackupPeriod parameter. |
| BackupPolicyMode | String | No | No | The type of the backup. | Valid values: DataBackupPolicy LogBackupPolicy |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ArchiveBackupKeep Count | Integer | No | No | The number of archived backup files that can be retained. | None |
| LocalLogRetentionS pace | Integer | No | No | The maximum disk usage that is allowed for log backup files on the instance. | None |
| ReleasedKeepPolicy | String | No | No | The policy that is used to retain archived backup files if the instance is released. | Valid values: None: No archived backup files are retained. Lastest: Only the last archived backup file is retained. All: All archived backup files are retained. |
| BackUpCategory | String | No | No | The edition of the secondary instance. | Valid values: Basic: Basic Edition HighAvailability: High- availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |

DBMappings syntax

```json
"DBMappings": [
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
```

`]` DBMappings properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBDescription | String | No | No | The description of the database. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| CharacterSetName | String | Yes | No | The character set. | Valid values: Valid values when Engine is set to MySQL or MariaDB: utf8 gbk latin1 utf8mb4 Valid values when Engine is set to SQLServer: Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ Valid values when Engine is set to PostgreSQL: KOI8U UTF8 WIN866 WIN874 WIN1250 WIN1251 WIN1252 WIN1253 WIN1254 WIN1255 WIN1256 WIN1257 WIN1258 EUC CN _ EUC KR _ EUC TW _ EUC JP _ EUC JIS 2004 _ _ |

| Property | Type | Required | Editable | Description | KOI8R Constraint MULE INTERNAL |
|---|---|---|---|---|---|
|   |   |   |   |   | _ LATIN1 LATIN2 LATIN3 LATIN4 LATIN5 LATIN6 LATIN7 LATIN8 LATIN9 LATIN10 ISO 8859 5 _ _ ISO 8859 6 _ _ ISO 8859 7 _ _ ISO 8859 8 _ _ SQL ASCII _ |
| DBName | String | Yes | No | The database name. | The name must be globally unique. It can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must _ start with a lowercase letter. |

Response parameters Fn::GetAtt InnerPort: the internal port of the instance. OrderId: the ID of the order. PublicConnectionString: the public endpoint of the instance. InnerIPAddress: the internal IP address of the instance. DBInstanceId: the ID of the instance. PublicIPAddress: the public IP address of the instance. PublicPort: the public port of the instance. InnerConnectionString: the internal endpoint of the instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "PeriodType": {
      "Type": "String",
      "Description": "Charge period for created instances.",
```

```json
      "AllowedValues": [
        "Month",
        "Year"
```

`],`

```json
      "Default": "Month"
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "ArchiveBackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The number of days for which to retain archived backups. \n The default val
ue 0 specifies not to enable the backup archiving function. Valid values: 30 to 1095.",
      "MinValue": 30,
      "MaxValue": 1095
    "DBTimeZone": {
      "Type": "String",
      "Description": "The UTC time zone of the instance. Valid values: -12:00 to +12:00. The time
zone must be an integer value such as +08:00. Values such as +08:30 are not allowed."
    "Port": {
      "Type": "Number",
      "Description": "The port of the database service.",
      "MinValue": 1,
      "MaxValue": 65535
    "ArchiveBackupKeepCount": {
      "Type": "Number",
      "Description": "The number of archived backups that can be retained. Default value: 1. Vali
d values: \nThe value of this parameter ranges from 1 to 31 when the ArchiveBackupKeepPolicy \n p arameter is set to ByMonth. \nThe value of this parameter ranges from 1 to 7 when the ArchiveBack upKeepPolicy \n parameter is set to ByWeek. \nNote You do not need to specify this parameter when the ArchiveBackupKeepPolicy \nparameter is set to KeepAll.",
      "MinValue": 1,
      "MaxValue": 31
    "LogBackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The number of days for which to retain log backup files. Valid values: 7 to
730. The log backup \n retention period cannot be longer than the data backup retention period. N ote If you enable the log \n backup function, you can specify the log backup retention period. Th is applies only when the \n instance runs MySQL, PostgreSQL, or PPAS.",
      "MinValue": 7,
      "MaxValue": 730
    "DBInstanceStorage": {
      "Type": "Number",
      "Description": "Database instance storage size. mysql is [5,1000]. sql server 2008r2 is [10
,1000], sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and PPAS is [5,2000]. Increase d every 5 GB, Unit in GB"
    "DBMappings": {
      "Type": "Json",
      "Description": "Database mappings to attach to db instance."
```

```json
    "ConnectionStringPrefix": {
      "Type": "String",
      "Description": "The prefix of the endpoint. \nOnly the prefix of the CurrentConnectionStrin
g parameter value can be modified.\nThe prefix must be 8 to 64 characters in length and can conta in letters, digits, and hyphens (-). ",
      "AllowedPattern": "[a-zA-Z0-9-]{8,64}"
    "MultiAZ": {
      "Type": "Boolean",
      "Description": "Specifies if the database instance is a multiple Availability Zone deployme
nt. ",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "Engine": {
      "Type": "String",
      "Description": "Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS/Mari
aDB now.",
      "AllowedValues": [
        "MySQL",
        "SQLServer",
        "PostgreSQL",
        "PPAS",
        "MariaDB"
```

`]`

```json
    "Tags": {
      "Type": "Json",
      "Description": "The tags of an instance.\nYou should input the information of the tag with
the format of the Key-Value, such as {\"key1\":\"value1\",\"key2\":\"value2\", ... \"key5\":\"val ue5\"}.\nAt most 5 tags can be specified.\nKey\nIt can be up to 64 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or https://.\nCannot be a null string.\nValue\nIt c an be up to 128 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or ht tps://.\nCan be a null string."
    "DBInstanceDescription": {
      "Type": "String",
      "Description": "Description of created database instance."
    "TargetDedicatedHostIdForMaster": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a primary in
stance in a host group."
    "EngineVersion": {
      "Type": "String",
      "Description": "Database instance version of the relative engine type.Support MySQL: 5.5/5.
6/5.7/8.0;\nSQLServer: 2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_ web/2017_std_ha/2017_ent;\nPostgreSQL: 9.4/10.0/11.0/12.0;\nPPAS: 9.3/10.0;\nMariaDB: 10.3."
    "DBInstanceClass": {
      "Type": "String",
"Description" "Databaseinstancetpe RefertheRDSdatabaseinstancetpereference
```

`s``c`

```json
      "Description": "Database instance type. Refer the RDS database instance type reference, suc
h as 'rds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc"
    "ArchiveBackupKeepPolicy": {
      "Type": "String",
      "Description": "The period for which to retain archived backups. The number of archived bac
kups that can \n be retained within the specified period is determined by the ArchiveBackupKeepCo unt parameter. \n Default value: 0. Valid values: \nByMonth \n ByWeek \n KeepAll",
      "AllowedValues": [
        "ByMonth",
        "ByWeek",
        "KeepAll"
```

`]`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The vSwitch id of created instance. For VPC network, the property is requir
ed."
    "BackupPolicyMode": {
      "Type": "String",
      "Description": "Backup type, \nDataBackupPolicy: data backup \nLogBackupPolicy: log backup"
```

`,`

```json
      "AllowedValues": [
        "DataBackupPolicy",
        "LogBackupPolicy"
```

`]`

```json
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. While choose by pay by month, it could be from 1 to 9.
While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
    "LocalLogRetentionHours": {
      "Type": "Number",
      "Description": "The number of hours for which to retain log backup files on the instance. \
nValid values: 0 to 168. The value 0 specifies not to retain log backup files on the instance. \n You can retain the default value. Note You must specify this parameter when the BackupPolicyMode \nparameter is set to LogBackupPolicy.",
      "MinValue": 0,
      "MaxValue": 168
    "HighSpaceUsageProtection": {
      "Type": "String",
      "Description": "Specifies whether to forcibly delete log backup files when the space usage
of the \n instance exceeds 80% or the remaining space is less than 5 GB. Valid values: \n Enable and Disable. You can retain the default value. Note You must specify \n this parameter when the B ackupPolicyMode parameter is set to LogBackupPolicy.",
      "AllowedValues": [
        "Enable",
        "Disable"
```

`]`

```json
    "RoleARN": {
"Type":"String",
```

```
ype:
```

`St` `g``,`

```json
      "Description": "The Alibaba Cloud Resource Name (ARN) provided to the service account of th
e instance by your Alibaba Cloud account to connect to KMS. You can copy the ARN from the RAM con sole."
    "MasterUserPassword": {
      "Type": "String",
      "Description": "The master password for the database instance. ",
      "MinLength": 8,
      "MaxLength": 32
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id of created database instance. For VPC network, the property is r
equired."
    "SSLSetting": {
      "Type": "String",
      "Description": "Secure Sockets Layer (SSL) link setting of the instance. Valid values:\nDis
abled: Disable SSL\nEnabledForPublicConnection: Public connection address will be protected by th e SSL certificate. It requires AllocatePublicConnection is true.\nEnabledForInnerConnection: Priv ate connection address will be protected by the SSL certificate.\nDefault value is Disabled.",
      "AllowedValues": [
        "Disabled",
        "EnabledForPublicConnection",
        "EnabledForInnerConnection"
```

`],`

```json
      "Default": "Disabled"
    "MasterUsername": {
      "Type": "String",
      "Description": "The master user name for the database instance. "
    "ConnectionMode": {
      "Type": "String",
      "Description": "Connection Mode for database instance,support 'Standard' and 'Safe' mode. D
efault is RDS system assigns. "
    "LocalLogRetentionSpace": {
      "Type": "Number",
      "Description": "The maximum percentage of space that is allowed to store log backup files o
n the instance. \n If the space usage for log backup files exceeds this percentage, the system de letes earlier \n log backup files until the space usage falls below this percentage. Valid values :0 to 50. \n You can retain the default value. Note You must specify this parameter when the \n B ackupPolicyMode parameter is set to LogBackupPolicy.",
      "MinValue": 0,
      "MaxValue": 50
    "Category": {
      "Type": "String",
      "Description": "The edition of the instance. Valid values:\nBasic: specifies to use the Bas
ic Edition.\nHighAvailability: specifies to use the High-availability Edition.\nAlwaysOn: specifi es to use the Cluster Edition.\nFinance: specifies to use the Enterprise Edition.",
      "AllowedValues": [
        "Basic",
        "HighAvailability",
        "AlwaysOn",
        "Finance"
```

`]`

```json
    "PrivateIpAddress": {
      "Type": "String",
      "Description": "The private ip for created instance."
    "TargetDedicatedHostIdForSlave": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a secondary
instance in a host group."
    "DBInstanceNetType": {
      "Type": "String",
      "Description": "Database instance net type, default is Intranet.Internet for public access,
Intranet for private access.",
      "AllowedValues": [
        "Internet",
        "Intranet"
```

`],`

```json
      "Default": "Intranet"
    "ReleasedKeepPolicy": {
      "Type": "String",
      "Description": "The policy used to retain archived backups if the instance is released. Def
ault value: None. \n Valid values: \nLastest: Only the last archived backup is retained. \n All: All of the archived backups are retained.",
      "AllowedValues": [
        "Lastest",
        "All"
```

`]`

```json
    "DedicatedHostGroupId": {
      "Type": "String",
      "Description": "The ID of the host group to which the instance belongs if you create an ins
tance in a host group."
    "AutoRenew": {
      "Type": "Boolean",
      "Description": "Auto renew the prepay instance. If the period type is by year, it will rene
w by year, else it will renew by month.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "EncryptionKey": {
      "Type": "String",
      "Description": "The ID of the encryption key that is used to encrypt data on SSDs in the re
gion. You can view the encryption key ID in the Key Management Service (KMS) console. You can als o create an encryption key."
    "PreferredBackupPeriod": {
      "Type": "CommaDelimitedList",
      "Description": "The backup period. Separate multiple values with commas (,). The default va
```

```json
lue is the original value. Valid values:Monday Tuesday Wednesday Thursday Friday Saturday Sunday Note When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
    "LogBackupLocalRetentionNumber": {
      "Type": "Number",
      "Description": "The number of log backup files that can be retained on the instance. \nDefa
ult value: 60. Valid values: 6 to 100.",
      "MinValue": 6,
      "MaxValue": 100
    "SlaveZoneIds": {
      "Type": "Json",
      "Description": "List of slave zone ids can specify slave zone ids when creating the high-av
ailability or enterprise edition instance. Meanwhile, VSwitchId needs to pass in the correspondin g vswitch id to the slave zone by order. For example, ZoneId = \"zone-a\" and SlaveZoneIds = [\"z one-c\", \"zone-b\"], then the VSwitchId must be \"vsw-zone-a,vsw-zone-c,vsw-zone-b\". Of course, you can also choose automatic allocation, for example, ZoneId = \"zone-a\" and SlaveZoneIds = [\" Auto\", \"Auto\"], then the VSwitchId must be \"vsw-zone-a,Auto,Auto\". The list contains up to 2 slave zone ids, separated by commas.",
      "MaxLength": 2
    "DBIsIgnoreCase": {
      "Type": "Number",
      "Description": "Specifies whether table names are case-sensitive. Valid values:\n1: Table n
ames are not case-sensitive. This is the default value.\n0: Table names are case-sensitive."
    "CommodityCode": {
      "Type": "String",
      "Description": "The CommodityCode of the order.",
      "AllowedValues": [
        "rds",
        "bards",
        "rords"
```

`],`

```json
      "Default": "rds"
    "MaintainTime": {
      "Type": "String",
      "Description": "The period during which the maintenance performs. The format is HH:mmZ-HH:m
mZ."
    "DBParamGroupId": {
      "Type": "String",
      "Description": "The ID of the parameter template used by the instance."
    "ZoneId": {
      "Type": "String",
      "Description": "selected zone to create database instance. You cannot set the ZoneId parame
ter if the MultiAZ parameter is set to true."
    "TargetDedicatedHostIdForLog": {
      "Type": "String",
      "Description": "The ID of the host to which the instance belongs if you create a log instan
ce in a host group."
    "AllocatePublicConnection": {
      "Type": "Boolean",
"Description":"Iftrue allocatepublicconnectionautomate"
```

```json
      Description: If true, allocate public connection automate.,
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "PreferredBackupTime": {
      "Type": "String",
      "Description": "The time when the backup task is performed. Format: yyyy-MM-ddZ-HH:mm:ssZ.N
ote When the BackupPolicyMode parameter is set to DataBackupPolicy, this parameter is required."
    "SecurityGroupId": {
      "Type": "String",
      "Description": "The ID of the ECS security groups. \nEach RDS instance can be associated wi
th up to three ECS security groups. \nYou must separate them with commas (,). \nTo delete an ECS Security group, leave this parameter empty. \n"
    "Quantity": {
      "Type": "Number",
      "Description": "The number of instance to be created, default is 1, max number is 99",
      "MinValue": 1,
      "MaxValue": 99,
      "Default": 1
    "AutoPay": {
      "Type": "Boolean",
      "Description": "Automatic Payment. Default is false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "DBInstanceStorageType": {
      "Type": "String",
      "Description": "The storage type of the instance. Valid values:\nlocal_ssd: specifies to us
e local SSDs. This is the recommended storage type.\ncloud_ssd: specifies to use standard SSDs.\n cloud_essd: specifies to use enhanced SSDs."
    "BackUpCategory": {
      "Type": "String",
      "Description": "Specifies whether to enable the second-level backup function. This function
allows a backup \nto be completed within seconds. Valid values: \nFlash: specifies to enable the second-level backup function. \n Standard: specifies to disable the second-level backup function.
```

`",`

```json
      "AllowedValues": [
        "Flash",
        "Standard"
```

`]`

```json
    "CompressType": {
      "Type": "Number",
      "Description": "The format used to compress backups. Valid values: \n 1: The zlib tool is u
sed to compress backups into .tar.gz files. \n 4: The QuickLZ tool is used to compress backups in
```

```json
to .xb.gz files. \nThis compression format is supported only when the instance runs MySQL 5.6 or 5.7. \nIt can be used to restore individual databases and tables. \n 8: The QuickLZ tool is used to compress backups into .xb.gz files. \n This compression format is supported only when the inst ance runs MySQL 8.0. \nIt cannot be used to restore individual databases or tables."
    "LogBackupFrequency": {
      "Type": "String",
      "Description": "The frequency at which to back up logs. Valid values: \nThe value LogInterv
al specifies to back up logs every 30 minutes. \n The default value of this parameter is the same as the data backup frequency. \nNote The value LogInterval is supported only when the instance ru ns SQL Server."
    "ConnectionStringType": {
      "Type": "String",
      "Description": "The endpoint type of the instance, allow values: Inner, Public",
      "AllowedValues": [
        "Inner",
        "Public"
```

`],`

```json
      "Default": "Inner"
    "CouponCode": {
      "Type": "String",
      "Description": "The coupon code of the order."
    "MasterUserType": {
      "Type": "String",
      "Description": "Privilege type of account.\n Normal: Common privilege. \n Super: High privi
lege. \nSysadmin: Super privileges (SA) (only supported by SQL Server)\nThe default value is Norm al.",
      "AllowedValues": [
        "Normal",
        "Super",
        "Sysadmin"
```

`],`

```json
      "Default": "Normal"
    "EnableBackupLog": {
      "Type": "Boolean",
      "Description": "Specifies whether to enable the log backup function. Valid values: \nTrue:
specifies to enable the log backup function. \nFalse: specifies to disable the log backup functio n. \nNote You must specify this parameter when the BackupPolicyMode parameter is set to LogBackup Policy.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "SQLCollectorStatus": {
      "Type": "String",
      "Description": "Specifies whether to enable or disable the SQL Explorer (SQL audit) feature
. \nValid values:Enable | Disabled.",
      "AllowedValues": [
        "Enable",
        "Disabled"
```

`]`

```json
    "BackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The retention period of the data backup. Value range: 7 to 730. The default
value is the original value. Note When the BackupPolicyMode parameter is set to LogBackupPolicy, this parameter is required.",
      "Default": 7
  "Resources": {
    "PrepayDBInstance": {
      "Type": "ALIYUN::RDS::PrepayDBInstance",
      "Properties": {
        "PeriodType": {
          "Ref": "PeriodType"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "ArchiveBackupRetentionPeriod": {
          "Ref": "ArchiveBackupRetentionPeriod"
        "DBTimeZone": {
          "Ref": "DBTimeZone"
        "Port": {
          "Ref": "Port"
        "ArchiveBackupKeepCount": {
          "Ref": "ArchiveBackupKeepCount"
        "LogBackupRetentionPeriod": {
          "Ref": "LogBackupRetentionPeriod"
        "DBInstanceStorage": {
          "Ref": "DBInstanceStorage"
        "DBMappings": {
          "Ref": "DBMappings"
        "ConnectionStringPrefix": {
          "Ref": "ConnectionStringPrefix"
        "MultiAZ": {
          "Ref": "MultiAZ"
        "Engine": {
          "Ref": "Engine"
        "Tags": {
          "Ref": "Tags"
        "DBInstanceDescription": {
          "Ref": "DBInstanceDescription"
        "TargetDedicatedHostIdForMaster": {
"Ref" "TargetDedicatedHostIdForMaster"
```

```json
          "Ref": "TargetDedicatedHostIdForMaster"
        "EngineVersion": {
          "Ref": "EngineVersion"
        "DBInstanceClass": {
          "Ref": "DBInstanceClass"
        "ArchiveBackupKeepPolicy": {
          "Ref": "ArchiveBackupKeepPolicy"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "BackupPolicyMode": {
          "Ref": "BackupPolicyMode"
        "Period": {
          "Ref": "Period"
        "LocalLogRetentionHours": {
          "Ref": "LocalLogRetentionHours"
        "HighSpaceUsageProtection": {
          "Ref": "HighSpaceUsageProtection"
        "RoleARN": {
          "Ref": "RoleARN"
        "MasterUserPassword": {
          "Ref": "MasterUserPassword"
        "VpcId": {
          "Ref": "VpcId"
        "SSLSetting": {
          "Ref": "SSLSetting"
        "MasterUsername": {
          "Ref": "MasterUsername"
        "ConnectionMode": {
          "Ref": "ConnectionMode"
        "LocalLogRetentionSpace": {
          "Ref": "LocalLogRetentionSpace"
        "Category": {
          "Ref": "Category"
        "PrivateIpAddress": {
          "Ref": "PrivateIpAddress"
        "TargetDedicatedHostIdForSlave": {
          "Ref": "TargetDedicatedHostIdForSlave"
        "DBInstanceNetType": {
          "Ref": "DBInstanceNetType"
```

`e` `:` `B`

```json
staceetype
        "ReleasedKeepPolicy": {
          "Ref": "ReleasedKeepPolicy"
        "DedicatedHostGroupId": {
          "Ref": "DedicatedHostGroupId"
        "AutoRenew": {
          "Ref": "AutoRenew"
        "EncryptionKey": {
          "Ref": "EncryptionKey"
        "PreferredBackupPeriod": {
          "Ref": "PreferredBackupPeriod"
        "LogBackupLocalRetentionNumber": {
          "Ref": "LogBackupLocalRetentionNumber"
        "SlaveZoneIds": {
          "Ref": "SlaveZoneIds"
        "DBIsIgnoreCase": {
          "Ref": "DBIsIgnoreCase"
        "CommodityCode": {
          "Ref": "CommodityCode"
        "MaintainTime": {
          "Ref": "MaintainTime"
        "DBParamGroupId": {
          "Ref": "DBParamGroupId"
        "ZoneId": {
          "Ref": "ZoneId"
        "TargetDedicatedHostIdForLog": {
          "Ref": "TargetDedicatedHostIdForLog"
        "AllocatePublicConnection": {
          "Ref": "AllocatePublicConnection"
        "PreferredBackupTime": {
          "Ref": "PreferredBackupTime"
        "SecurityGroupId": {
          "Ref": "SecurityGroupId"
        "Quantity": {
          "Ref": "Quantity"
        "AutoPay": {
          "Ref": "AutoPay"
        "DBInstanceStorageType": {
          "Ref": "DBInstanceStorageType"
```

```json
        "BackUpCategory": {
          "Ref": "BackUpCategory"
        "CompressType": {
          "Ref": "CompressType"
        "LogBackupFrequency": {
          "Ref": "LogBackupFrequency"
        "ConnectionStringType": {
          "Ref": "ConnectionStringType"
        "CouponCode": {
          "Ref": "CouponCode"
        "MasterUserType": {
          "Ref": "MasterUserType"
        "EnableBackupLog": {
          "Ref": "EnableBackupLog"
        "SQLCollectorStatus": {
          "Ref": "SQLCollectorStatus"
        "BackupRetentionPeriod": {
          "Ref": "BackupRetentionPeriod"
  "Outputs": {
    "InnerConnectionString": {
      "Description": "DB instance connection url by Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerConnectionString"
```

`]`

```json
    "DBInstanceId": {
      "Description": "The instance id of created database instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "DBInstanceId"
```

`]`

```json
    "InnerIPAddress": {
      "Description": "IP Address for created DB instance of Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerIPAddress"
```

`]`

```json
    "PublicConnectionString": {
      "Description": "DB instance connection url by Internet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicConnectionString"
```

`]`

```json
    "PublicIPAddress": {
      "Description": "IP Address for created DB instance of Internet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicIPAddress"
```

`]`

```json
    "OrderId": {
      "Description": "The order id list of created instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "OrderId"
```

`]`

```json
    "PublicPort": {
      "Description": "Internet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicPort"
```

`]`

```json
    "InnerPort": {
      "Description": "Intranet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerPort"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AllocatePublicConnection:
    AllowedValues:
    - 'True'
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
    Default: false
    Description: Automatic Payment. Default is false.
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
```

\ \

```
      Flash: specifies to enable the second-level backup function. \n Standard: specifies\
      \ to disable the second-level backup function."
    Type: String
  BackupPolicyMode:
    AllowedValues:
    - DataBackupPolicy
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
```

```
    AllowedValues:
    - Inner
    - Public
    Default: Inner
    Description: 'The endpoint type of the instance, allow values: Inner, Public'
    Type: String
  CouponCode:
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
```

```
    - 'true'
    - 'False'
    - 'false'
    Description: "Specifies whether to enable the log backup function. Valid values:\
      \ \nTrue: specifies to enable the log backup function. \nFalse: specifies to\
      \ disable the log backup function. \nNote You must specify this parameter when\
      \ the BackupPolicyMode parameter is set to LogBackupPolicy."
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
      SQLServer: 2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/20
17_std_ha/2017_ent;
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
```

```
      \ BackupPolicyMode parameter is set to LogBackupPolicy."
    MaxValue: 50
    MinValue: 0
    Type: Number
  LogBackupFrequency:
    Description: "The frequency at which to back up logs. Valid values: \nThe value\
      \ LogInterval specifies to back up logs every 30 minutes. \n The default value\
      \ of this parameter is the same as the data backup frequency. \nNote The value\
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
      \ backup retention period. Note If you enable the log \n backup function, you\
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
Defalt
```

```
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
```

```
abe
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
```

```
    Type: String
  TargetDedicatedHostIdForSlave:
    Description: The ID of the host to which the instance belongs if you create a
      secondary instance in a host group.
    Type: String
  VSwitchId:
    Description: The vSwitch id of created instance. For VPC network, the property
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
```

```
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
```

```
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
```

```
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

### 6.6 ROS

#### 6.6.1 ALIYUN::ROS::WaitCondition

ALIYUN::ROS::WaitCondition is used to create an instance to process UserData messages. Syntax

```json
  "Type": "ALIYUN::ROS::WaitCondition",
  "Properties": {
    "Count": Number,
    "Handle": String,
    "Timeout": Number,
    "ShowProgressEvent": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Handle | String | Yes | No | The instance created by calling ALIYUN::ROS ::WaitCondit ionHandle. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Timeout | Number | Yes | No | The timeout period for receiving UserData messages. | Valid values: 1 to 43200. Unit: seconds. |
| Count | Number | No | Yes | The total number of received UserData messages. | None |
| ShowProgres sEvent | String | No | No | Specifies whether to display progress events for receiving UserData messages. | Valid values: EnabledIfCreateStack: Progress events are displayed if you create stacks. Disabled: Progress events are not displayed. |

Response parameters Fn::GetAtt Data: a JSON string that contains the signal data sent to the handle after the latest stack creation or update. JoinedErrorData: a string that contains data associated with wait condition error signals sent to the handle. ErrorData: a JSON string that contains the error signal data sent to the handle after the latest stack creation or update. Examples `JSON` format

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

`]`

```json
    "Timeout": {
      "Type": "Number",
      "Description": "The number of seconds to wait for the correct number of signals to arrive."
```

`,`

```json
      "MinValue": 1,
      "MaxValue": 43200
    "Count": {
      "Type": "Number",
"Description":"Thenumberofsuccesssignalsthatmustbereceivedbeforethestackcreati
```

```json
      Description: The number of success signals that must be received before the stack creati
on process continues.",
      "Default": 1
    "Handle": {
      "Type": "String",
      "Description": "A reference to the wait condition handle used to signal this wait condition
```

`."`

```json
  "Resources": {
    "WaitCondition": {
      "Type": "ALIYUN::ROS::WaitCondition",
      "Properties": {
        "ShowProgressEvent": {
          "Ref": "ShowProgressEvent"
        "Timeout": {
          "Ref": "Timeout"
        "Count": {
          "Ref": "Count"
        "Handle": {
          "Ref": "Handle"
  "Outputs": {
    "LastErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error s
ignals sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "LastErrorData"
```

`]`

```json
    "JoinedLastErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to
the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedLastErrorData"
```

`]`

```json
    "LastData": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle backup by update last time.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "LastData"
```

`]`

```json
    "JoinedErrorData": {
      "Description": "String containing data associated with wait condition error signals sent to
the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "JoinedErrorData"
```

`]`

```json
    "Data": {
      "Description": "JSON serialized dict containing data associated with wait condition signals
sent to the handle.",
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "Data"
```

`]`

```json
    "ErrorData": {
      "Description": "JSON serialized dict containing data associated with wait condition error s
ignals sent to the handle.",
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
```

```
      arrive.
    MaxValue: 43200
    MinValue: 1
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
```

```
      - LastErrorData
```

#### 6.6.2 ALIYUN::ROS::WaitConditionHandle

ALIYUN::ROS::WaitConditionHandle is used to create an instance that sends and receives messages when user data is being executed. Syntax

```json
  "Type": "ALIYUN::ROS::WaitConditionHandle",
  "Properties": {
    "Count": Integer,
    "Mode": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Count | Integer | No | Yes | The total number of messages to be received. | The default value is -1, which specifies that the property does not take effect. This property takes effect when the following conditions are met: The value of Mode is Full. The value of Count is greater than or equal to 0. No signal ID is specified. Signal IDs must be integers that start from 1. The signal ID increments by 1 for each subsequent signal. For example, if the ID of the first signal is 1, the ID of the second signal is 2. If Count takes effect, the signals whose IDs are greater than the Count value are deleted before the update begins. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Mode | String | No | Yes | The mode of the instance. | Default value: Full. Valid values: Increment: All signals are deleted before they are updated. Full: No signals are deleted if you do not configure Count. |

Response parameters Fn::GetAtt CurlCli: a cURL command that is generated by the resource. You can use the command to send the user data execution result or status to Resource Orchestration Service (ROS). WindowsCurlCli: provides Windows with cURL CLI command prefixes and sends a message that indicates whether the execution is successful or failed. Windows does not support the cURL command. Therefore, you must manually install curl.exe and add it to PATH. You can add --data-binary "{\"status\": \" SUCC ESS \"} to indicate that the execution is successful, and add --data-binary "{\"status\": \" FAILURE \"} to indicate that the execution failed. PowerShellCurlCli: provides PowerShell with cURL CLI command prefixes and sends a message that indicates whether the execution is successful or failed. cmdlet is introduced in PowerShell 3.0. Therefore, you must

| the constraints. You can use the $PSVersionTable.PSVe u can add -Body '{"status": " SUCCESS "} to -Body '{"status": "FAILURE "} to indicate that the | $PSVersionTable.PSVe |
|---|---|
| -Body '{"status": "FAILURE "} |   |

`rsion` command to query the version number. You can add `-Body '{"status": " SUCCESS "}` to execution failed. Headers: the HTTP POST request headers used to send a message that indicates whether the execution is successful or failed. URL: the HTTP POST request URL used to send a message that indicates whether the execution is successful or failed. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Mode": {
      "Type": "String",
      "Description": "If set to Increment, all old signals will be deleted before update. In this
mode, WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n\nIf set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCondition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mo de with Count.\n\nDefault to Full.",
      "AllowedValues": [
        "Increment",
        "Full"
```

`],`

```json
      "Default": "Full"
```

```json
    "Count": {
      "Type": "Number",
      "Description": "There are 3 preconditions that make Count taking effect:\n1.Mode is set to
Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing in teger started from 1. For example, the id of the first signal is 1, the id of the second signal i s 2, and so on.\n\nIf Count takes effect, signals with id > Count will be deleted before update.\ nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
      "Default": -1
  "Resources": {
    "WaitConditionHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle",
      "Properties": {
        "Mode": {
          "Ref": "Mode"
        "Count": {
          "Ref": "Count"
  "Outputs": {
    "CurlCli": {
      "Description": "Convenience attribute, provides curl CLI command prefix, which can be used
for signalling handle completion or failure. You can signal success by adding --data-binary '{\" status\": \"SUCCESS\"}' , or signal failure by adding --data-binary '{\"status\": \"FAILURE\"}'",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "CurlCli"
```

`]`

```json
    "WindowsCurlCli": {
      "Description": "Convenience attribute, provides curl CLI command prefix for Windows, which
can be used for signalling handle completion or failure. As Windows does not support curl command , you need to install curl.exe and add it to PATH first. You can signal success by adding --databinary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"s tatus\\\": \\\"FAILURE\\\"}\" ",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "WindowsCurlCli"
```

`]`

```json
    "Headers": {
      "Description": "HTTP POST Headers used for signalling handle completion or failure.",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "Headers"
```

`]`

```json
    "URL": {
      "Description": "HTTP POST URL used for signalling handle completion or failure.",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "URL"
```

`]`

```json
    "PowerShellCurlCli": {
      "Description": "Convenience attribute, provides curl CLI command prefix for PowerShell, whi
ch can be used for signalling handle completion or failure. As this cmdlet was introduced in Powe rShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSV ersionTable.PSVersion.) You can signal success by adding -Body '{\"status\": \"SUCCESS\"}' , or s ignal failure by adding -Body '{\"status\": \"FAILURE\"}' ",
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
```

```
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
      for signalling handle completion or failure.  You can signal success by
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
```

```
      'Fn::GetAtt':
        - WaitConditionHandle
        - PowerShellCurlCli
```

For more examples, visit SLS.json and SLS.yml.

#### 6.6.3 ALIYUN::ROS::Stack

ALIYUN::ROS::Stack is used to create a nested stack. You can have a maximum of five nested levels. Nested stacks can themselves contain other nested stacks. This results in a hierarchy of stacks. The root stack is the top-level stack to which all the nested stacks belong. The template of the root stack is called the toplevel template. The ALIYUN::ROS::Stack type nests a stack as a resource in a top-level template. In a nested stack template, you can use outputs from one stack as inputs to another stack. To obtain the output of the nested stack, you can use the Fn::GetAtt function and set the function parameters to the name of the nested stack and the output value in the Outputs.NestedStackOutputName format. For more information, see Use nested stacks. Syntax

```json
  "Type": "ALIYUN::ROS::Stack",
  "Properties": {
    "TemplateURL": String,
    "TemplateBody": String,
    "TemplateId": String,
    "TemplateVersion": String,
    "TimeoutMins": Number,
    "Parameters": Map,
    "ResourceGroupId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable |   | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| TemplateUR L | String | No | Yes |   |   | The file that contains the template body can be up to 524,288 bytes in size. The URL can be up to 1,024 bytes in length. The URL must point to a template that is located in an HTTP or HTTPS web server or an Object Storage Service (OSS) bucket. Example: oss://ros/template/demo |   |   |
|   |   |   |   |   |   |   | oss://ros/template/demo |   |
|   |   |   |   |   | The URL of |   |   | or |
|   |   |   |   |   | the file that |   |   |   |
|   |   |   |   |   | contains the | ?RegionId=cn-hangzhou |   |   |
|   |   |   |   |   | template body. |   |   |   |
| TemplateBo dy | Map | No | Yes |   | The structure that contains the template body, which is used to facilitate the delivery of the template. | The content is raw data. Functions in the template body are not resolved in the parent stack. You must specify one of the TemplateURL , TemplateBody , and TemplateId parameters. If all the parameters are specified, the TemplateBody parameter takes precedence. |   |   |
| TemplateId | String | No | Yes |   | The ID of the template. | You must specify one of the TemplateURL , TemplateBody , and TemplateId parameters. If all the parameters are specified, the TemplateBody parameter takes precedence. |   |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TemplateVer sion | String | No | Yes | The name of the template version. | None |
| TimeoutMins | Number | No | Yes | The timeout period for creating or updating a stack. | Unit: minutes. Default value: 60. |
| Parameters | Map | No | Yes | A set of key- value pairs that represent the parameters passed to Resource Orchestratio n Service (ROS) when the nested stack is created. | Each parameter has a key corresponding to a parameter name defined in the template of the nested stack and a value representing the value that you want to set for the parameter. This parameter is required if the nested stack requires input parameters. |
| ResourceGro upId | String | No | No | The ID of the resource group. | None |

Response parameters Fn::GetAtt You can use the following code to obtain the output of the nested stack:

```
  "Fn::GetAtt": [
    "<nested_stack>",
    "Outputs.<nested_stack_output_name>"
```

`]` When you use `Ref` to reference resources in a nested stack, the Alibaba Cloud Resource Name (ARN) of the nested stack is returned. Example: `arn:acs:ros::cn-hangzhou:12345****:stacks/test-nested-stack-Demo-`

```
jzkyq7mn****/e71c1e04-1a57-46fc-b9a4-cf7ce0d3**** .
```

Examples The following code provides an example on how to create a virtual private cloud (VPC), a vSwitch, and a security group in a nested stack and save the output results to the oss://ros/template/vpc.txt directory:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One VPC, vSwitch, security group.",
  "Parameters": {
```

```json
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone"
    "SecurityGroupName": {
      "Type": "String",
      "Description": "The security group name",
      "Default": "my-sg-name"
    "VpcName": {
      "Type": "String",
      "Description": "The VPC name",
      "MinLength": 2,
      "MaxLength": 128,
      "ConstraintDescription": "[2, 128] English or Chinese letters",
      "Default": "my-vpc-name"
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
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The vSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
  "Resources": {
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
      "Properties": {
        "CidrBlock": {
          "Ref": "VpcCidrBlock"
        "VpcName": {
          "Ref": "VpcName"
    "VSwitch": {
      "Type": "ALIYUN::ECS::VSwitch",
      "Properties": {
        "CidrBlock": {
          "Ref": "VSwitchCidrBlock"
        "ZoneId": {
          "Ref": "ZoneId"
```

`"V`

```
Id"
```

```json
        "VpcId": {
          "Fn::GetAtt": [
            "Vpc",
            "VpcId"
```

`]`

```json
    "SecurityGroup": {
      "Type": "ALIYUN::ECS::SecurityGroup",
      "Properties": {
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
        "VpcId": {
          "Ref": "Vpc"
    "WaitConditionHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle",
      "Properties": {
        "UpdateVersion": {
          "Ref": "UpdateVersion"
  "Outputs": {
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "SecurityGroup",
          "SecurityGroupId"
```

`]`

```json
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "Vpc",
          "VpcId"
```

`]`

```json
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "VSwitch",
          "VSwitchId"
```

`]` Example of a parent stack

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One ECS instance.",
  "Parameters": {
    "ImageId": {
      "Default": "centos_7",
      "Type": "String",
      "Description": "Image Id, represents the image resource to startup the ECS instance"
    "InstanceType": {
      "Type": "String",
      "Description": "The ECS instance type,",
      "Default": "ecs.xn4.small"
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone "
    "InstanceChargeType": {
      "Type": "String",
      "AllowedValues": [
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid",
      "Description": "The instance charge type"
    "SecurityGroupName": {
      "Type": "String",
      "Description": "The security group name",
      "Default": "my-sg-name"
    "NetworkInterfaceName": {
      "Type": "String",
      "Description": "The Network interface name",
      "Default": "my-eni-name"
    "VpcName": {
      "Type": "String",
      "Description": "The VPC name",
      "MinLength": 2,
      "MaxLength": 128,
      "ConstraintDescription": "[2, 128] English or Chinese letters",
      "Default": "my-vpc-name"
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
    "SystemDiskCategory": {
      "AllowedValues": [
        "cloud",
```

`"``l` `d`

```
ffii
```

`"`

```
        "cloud_efficiency",
        "cloud_ssd"
```

`],`

```json
      "Description": "System disk category: average cloud disk(cloud), efficient cloud disk(clo
ud_efficiency) or SSD cloud disk(cloud_ssd)",
      "Type": "String",
      "Default": "cloud_ssd"
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
    "VSwitchCidrBlock": {
      "Type": "String",
      "Description": "The VSwitch subnet which must be within VPC",
      "Default": "10.0.10.0/24"
    "UpdateVersion": {
      "Type": "Number",
      "Default": 0
  "Resources": {
    "NetworkStack": {
      "Type": "ALIYUN::ROS::Stack",
      "Properties": {
        "TemplateURL": "oss://ros/template/vpc.txt",
        "TimeoutMins": 5,
        "Parameters": {
          "ZoneId": {
            "Ref": "ZoneId"
          "SecurityGroupName": {
            "Ref": "SecurityGroupName"
          "VpcName": {
            "Ref": "VpcName"
          "VpcCidrBlock": {
            "Ref": "VpcCidrBlock"
          "VSwitchCidrBlock": {
            "Ref": "VSwitchCidrBlock"
          "UpdateVersion": {
            "Ref": "UpdateVersion"
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
"Properties":{
```

```json
      Properties: {
        "ImageId": {
          "Ref": "ImageId"
        "InstanceType": {
          "Ref": "InstanceType"
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        "SecurityGroupId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.SecurityGroupId"
```

`]`

```json
        "VpcId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VpcId"
```

`]`

```json
        "VSwitchId": {
          "Fn::GetAtt": [
            "NetworkStack",
            "Outputs.VSwitchId"
```

`]`

```json
        "IoOptimized": {
          "Ref": "IoOptimized"
        "ZoneId": {
          "Ref": "ZoneId"
        "SystemDisk_Category": {
          "Ref": "SystemDiskCategory"
        "DiskMappings": [
            "Category": "cloud_ssd",
            "Size": 20
```

`]`

```json
  "Outputs": {
    "InstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "WebServer",
          "InstanceId"
```

`]`

```json
    "PublicIp": {
      "Value": {
        "Fn::GetAtt": [
```

```
          "WebServer",
          "PublicIp"
```

`]`

```json
    "SecurityGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.SecurityGroupId"
```

`]`

```json
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.VpcId"
```

`]`

```json
    "VSwitchId": {
      "Value": {
        "Fn::GetAtt": [
          "NetworkStack",
          "Outputs.VSwitchId"
```

`]`

```json
    "NetworkStackArn": {
      "Value": {
        "Ref": "NetworkStack"
```

For more examples, see MongoDBInstance.json and MongoDBInstance.yml.

### 6.7 SLB

#### 6.7.1 ALIYUN::SLB::AccessControl

ALIYUN::SLB::AccessControl is used to create an access control list (ACL). Syntax

```json
  "Type": "ALIYUN::SLB::AccessControl",
  "Properties": {
    "AddressIPVersion": String,
    "AclName": String,
    "AclEntrys": List,
    "Tags": List,
    "ResourceGroupId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AddressIPVer sion | String | No | No | The Internet Protocol version. | Valid values: ipv4 ipv6 |
| AclName | String | Yes | Yes | The name of the ACL. | None. |
| ResourceGro upId | String | No | Yes | The ID of the resource group to which the ACL belongs. | None. |
| AclEntrys | List | No | No | The list of ACL entries. | The list can contain a maximum of 50 ACL entries. For more information, see AclEntrys properties. |
| Tags | List | No | Yes | The tags. | You can add up to 20 tags. For more information, see Tags property. |

AclEntrys syntax

```json
"AclEntrys": [
    "comment": String,
    "entry": String
```

`]` AclEntrys properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| comment | String | No | No | The description of the ACL entry. | None. |
| entry | String | Yes | No | The IP address or CIDR block. | None. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags property

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The tag key must be 1 to 128 characters in length, and cannot contain http:// or https:// . The tag key cannot start with acs: or aliyun . |
| Value | String | No | No | The value of the tag. | The tag value must be 0 to 128 characters in length, and cannot contain http:// or https:// . The tag value cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Return values Fn::GetAtt AclId: the ID of the ACL. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "AclEntrys": {
      "Type": "Json",
      "Description": "A list of acl entrys. Each entry can be IP addresses or CIDR blocks. Max le
ngth: 50.",
      "MaxLength": 50
```

```json
    "AddressIPVersion": {
      "Type": "String",
      "Description": "IP version. Could be \"ipv4\" or \"ipv6\".",
      "AllowedValues": [
        "ipv4",
        "ipv6"
```

`]`

```json
    "AclName": {
      "Type": "String",
      "Description": "The name of the access control list."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
  "Resources": {
    "AccessControl": {
      "Type": "ALIYUN::SLB::AccessControl",
      "Properties": {
        "AclEntrys": {
          "Ref": "AclEntrys"
        "AddressIPVersion": {
          "Ref": "AddressIPVersion"
        "AclName": {
          "Ref": "AclName"
        "Tags": {
          "Ref": "Tags"
  "Outputs": {
    "AclId": {
      "Description": "The ID of the access control list.",
      "Value": {
        "Fn::GetAtt": [
          "AccessControl",
          "AclId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AclEntrys:
    Description: 'A list of acl entrys. Each entry can be IP addresses or CIDR blocks.
      Max length: 50.'
    MaxLength: 50
    Type: Json
  AclName:
    Description: The name of the access control list.
    Type: String
  AddressIPVersion:
    AllowedValues:
    - ipv4
    - ipv6
    Description: IP version. Could be "ipv4" or "ipv6".
    Type: String
  Tags:
    Description: Tags to attach to instance. Max support 20 tags to add during create
      instance. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
    Type: Json
Resources:
  AccessControl:
    Properties:
      AclEntrys:
        Ref: AclEntrys
      AclName:
        Ref: AclName
      AddressIPVersion:
        Ref: AddressIPVersion
      Tags:
        Ref: Tags
    Type: ALIYUN::SLB::AccessControl
Outputs:
  AclId:
    Description: The ID of the access control list.
    Value:
      Fn::GetAtt:
      - AccessControl
      - AclId
```

To view more examples, visit AccessControl.json and AccessControl.yml.

#### 6.7.2 ALIYUN::SLB::BackendServerAttachment

ALIYUN::SLB::BackendServerAttachment is used to attach backend servers to an SLB instance. Syntax

```json
  "Type": "ALIYUN::SLB::BackendServerAttachment",
  "Properties": {
    "LoadBalancerId": String,
    "BackendServers": List,
    "BackendServerList": List,
    "BackendServerWeightList": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerId | String | Yes | No | The unique ID of the SLB instance. | None. |
| BackendServerLi st | List | No | Yes | The list of backend servers to be attached. | The LoadBalancerId parameter is used together with the BackendServer WeightList parameter. Separate ECS instance IDs with commas (,). This parameter is ignored when the BackendServers parameter is specified. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| BackendServer WeightList | List | No | Yes | The weights of all ECS instances specified by the BackendServerLi st parameter in order. | If this parameter is not specified, the weight of each ECS instance specified by the BackendServerLi st parameter is 100. When the number of items specified by BackendServer WeightList is less than that specified by BackendServerLi st, the remaining ECS instances in the backend server list are assigned the last weight value in the backend server weight list. |
| BackendServers | List | No | Yes | The list of backend servers to be attached. | Only ECS instances that are in the running state can be attached to the SLB instance as backend servers. For more information, see BackendServers properties. |

BackendServers syntax

```json
"BackendServers": [
    "ServerId" : String,
    "Weight" : Integer,
    "Type": String,
    "ServerIp": String,
    "Description": String
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the ECS instance. | Only ECS instances that are in the running state can be attached to the SLB instance as backend servers. A maximum of 20 backend servers can be attached each time. You can specify elastic network interfaces (ENIs) as the backend servers for only guaranteed- performance SLB instances. |
| Weight | Integer | Yes | Yes | The weight of the ECS instance in the SLB instance. | Valid values: 0 to 100. Default value: 100. |
| ServerIp | String | No | No | The IP address of the backend server. | None. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Type | String | No | No | The type of the backend server. | Default value: ecs. Valid values: ecs: ECS instance eni: ENI eci: Elastic Container Instance (ECI) |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

Response parameters Fn::GetAtt BackendServers: the backend servers attached to the SLB instance. LoadBalancerId: the ID of the SLB instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "BackendServerList": {
      "Type": "Json",
      "Description": "The comma delimited instance id list. If the property \"BackendServers\" is
setting, this property will be ignored."
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The id of load balancer."
    "BackendServerWeightList": {
      "Type": "CommaDelimitedList",
      "Description": "The comma delimited weight list. If no value specified will use 100. If the
length is small than \"BackendServerList\", it will copy the last one to fill the array. If the p roperty \"BackendServers\" is setting, this property will be ignored."
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of ECS instance, which will attached to load balancer."
```

```json
  "Resources": {
    "BackendServer": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
      "Properties": {
        "BackendServerList": {
          "Ref": "BackendServerList"
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        "BackendServerWeightList": {
          "Ref": "BackendServerWeightList"
        "BackendServers": {
          "Ref": "BackendServers"
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The id of load balancer.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "LoadBalancerId"
```

`]`

```json
    "BackendServers": {
      "Description": "The collection of attached backend server.",
      "Value": {
        "Fn::GetAtt": [
          "BackendServer",
          "BackendServers"
```

`]` `YAML` format

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

#### 6.7.3 ALIYUN::SLB::BackendServerToVServerGroupAddition

ALIYUN::SLB::BackendServerToVServerGroupAddition is used to add backend servers to an existing vServer group. Syntax

```json
  "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
  "Properties": {
    "BackendServers": List,
    "VServerGroupId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGrou pId | String | Yes | No | The ID of the vServer group. | None |
| BackendServ ers | List | Yes | Yes | The list of backend servers. | For more information, see BackendServers properties. |

BackendServers syntax

```json
"BackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | None |
| Port | Integer | Yes | Yes | The port that is used by the backend server. | Valid values: 1 to 65535. |
| Weight | Integer | No | Yes | The weight of the backend server. | Valid values: 0 to 100. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Type | String | No | Yes | The type of the backend server. | Default value: ecs. Valid values: ecs: Elastic Compute Service (ECS) instances eni: elastic network interfaces (ENIs) Not e You can specify ENIs as backend servers only for high-performance SLB instances. |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| ServerIp | String | No | Yes | The IP address of the backend server. | The IP addresses of ECS instances or ENIs are supported. |

Response parameters Fn::GetAtt VServerGroupId: the ID of the vServer group. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VServerGroupId": {
      "Type": "String",
      "Description": "The ID of virtual server group."
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of a combination of ECS Instance-Port-Weight.Same ecs instance wit
h different port is allowed, but same ecs instance with same port isn't."
  "Resources": {
    "BackendServerToVServerGroupAddition": {
      "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
      "Properties": {
        "VServerGroupId": {
          "Ref": "VServerGroupId"
        "BackendServers": {
          "Ref": "BackendServers"
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

#### 6.7.4 ALIYUN::SLB::Certificate

ALIYUN::SLB::Certificate is used to upload a certificate to a Server Load Balancer (SLB) instance. Server certificates and CA certificates are supported. Not ice You can upload only a single CA certificate at a time ("CertificateType": "CA "). You can upload only a single server certificate and its corresponding private key at a time ("CertificateType": "Server "). Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGro upId | String | No | Yes | The ID of the resource group. | None |
| CertificateNa me | String | No | Yes | The name of the certificate. | None |
| Certificate | String | Yes | No | The CA certificate to be uploaded. | None |
| AliCloudCerti ficateName | String | No | No | The name of the Alibaba Cloud certificate. | None |
| PrivateKey | String | No | No | The private key to be uploaded. | None |
| AliCloudCerti ficateId | String | No | No | The ID of the Alibaba Cloud certificate. | This parameter is required if you use a certificate from Alibaba Cloud SSL Certificates Service. |
| CertificateTy pe | String | No | No | The type of the certificate. | Valid values: Server CA |
| Tags | List | No | Yes | The tags of the certificate. | A maximum of 20 tags can be specified. For more information, see the Tags properties section in this topic. |

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot contain http:// or https:// . It cannot start with acs: or aliyun . |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

|   | http:// |
|---|---|
| https:// |   |

|   | acs: |
|---|---|
| aliyun |   |

Response parameters Fn::GetAtt CertificateId: the ID of the certificate. Fingerprint: the fingerprint of the certificate. Examples `JSON` format

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
    "AliCloudCertificateName": {
      "Type": "String",
      "Description": "The name of the Alibaba Cloud certificate."
    "PrivateKey": {
      "Type": "String",
```

`"D`

```
iti
```

`"`

```
"Th
```

`i` `t` `k` `"`

```json
      "Description": "The private key."
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "CertificateName": {
      "Type": "String",
      "Description": "The name of the certificate."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to instance. Max support 20 tags to add during create instan
ce. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "Certificate": {
      "Type": "String",
      "Description": "The content of the certificate public key."
    "AliCloudCertificateId": {
      "Type": "String",
      "Description": "The ID of the Alibaba Cloud certificate."
  "Resources": {
    "SLBCertificate": {
      "Type": "ALIYUN::SLB::Certificate",
      "Properties": {
        "CertificateType": {
          "Ref": "CertificateType"
        "AliCloudCertificateName": {
          "Ref": "AliCloudCertificateName"
        "PrivateKey": {
          "Ref": "PrivateKey"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "CertificateName": {
          "Ref": "CertificateName"
        "Tags": {
          "Ref": "Tags"
        "Certificate": {
          "Ref": "Certificate"
        "AliCloudCertificateId": {
          "Ref": "AliCloudCertificateId"
  "Outputs": {
"Fingerprint":{
```

```json
    Fingerprint: {
      "Description": "The fingerprint of the certificate.",
      "Value": {
        "Fn::GetAtt": [
          "SLBCertificate",
          "Fingerprint"
```

`]`

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
```

`P` `ti`

```
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
    Description: The fingerprint of the certificate.
    Value:
      Fn::GetAtt:
      - SLBCertificate
      - Fingerprint
```

For more examples, visit Listener.json and Listener.yml. In the examples, the ALIYUN::SLB::Listener, ALIYUN::SLB::LoadBalancerClone, ALIYUN::SLB::Certificate, ALIYUN::SLB::DomainExtension, ALIYUN::SLB::VServerGroup, ALIYUN::SLB::Rule, and ALIYUN::SLB::BackendServerToVServerGroupAddition resource types are involved.

#### 6.7.5 ALIYUN::SLB::DomainExtension

ALIYUN::SLB::DomainExtension is used to create a domain extension for an SLB instance. Statement

```json
  "Type": "ALIYUN::SLB::DomainExtension",
  "Properties": {
    "Domain": String,
    "ListenerPort": Integer,
    "ServerCertificateId": String,
    "LoadBalancerId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Domain | String | No | No | The custom domain name. | None |
| ListenerPort | Integer | Yes | No | The frontend port used by the HTTPS listener of the SLB instance. | Valid values: 1 to 65535. |
| ServerCertificat eId | String | No | Yes | The ID of the certificate corresponding to the domain name. | None |
| LoadBalancerId | String | No | No | The ID of the SLB instance. | None |

Response parameters Fn::GetAtt DomainExtensionId: the ID of the created domain extension. ListenerPort: The frontend port used by the SLB instance. Sample request

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
  "Outputs": {
    "DomainExtensionId": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "DomainExtensionId"
```

`]`

```json
    "ListenerPort": {
      "Value": {
        "Fn::GetAtt": [
          "DomainExtension",
          "ListenerPort"
```

`]`

#### 6.7.6 ALIYUN::SLB::Listener

ALIYUN::SLB::Listener is used to create a listener for a Server Load Balancer (SLB) instance. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterSlaveS erverGroupId | String | No | No | The ID of the primary/sec ondary server group. | None |
| AclStatus | String | No | Yes | Specifies whether to enable the access control feature. | Valid values: on (default): enables the access control feature. off: disables the access control feature. |
| AclId | String | No | Yes | The ID of the access control list (ACL) to be associated with the listener. | This parameter is required when the AclStatus parameter is set to on. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AclType | String | No | Yes | The type of the ACL. | Valid values: white: specifies the ACL as a whitelist. Only requests from the IP addresses or CIDR blocks in the ACL are forwarded. Whitelists are applicable to scenarios in which you want an application to be accessed only from specific IP addresses. Risks may arise if the whitelist is improperly set. After you configure a whitelist, only the IP addresses that are specified in the whitelist can access the SLB listener. If you enable a whitelist but the whitelist does not contain an IP address, the listener does not forward requests. black: specifies the ACL as a blacklist. All requests from the IP addresses or CIDR blocks in the ACL are rejected. Blacklists are applicable to scenarios in which you want to deny access from specific IP addresses to an application. If you enable a blacklist but the blacklist does not contain an IP address, the listener forwards all requests. This parameter is required when the AclStatus parameter is set to on. |
| Protocol | String | Yes | No | The protocol over which the listener forwards requests. | Valid values: http https tcp udp |
| ListenerPort | Integer | Yes | No | The frontend port that is used by the SLB instance. | Valid values: 1 to 65535. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Bandwidth | Integer | Yes | No | The bandwidth limit of the listener. | Valid values: 1 to 1000 and - 1. Unit: Mbit/s. Valid values: For a pay-by-bandwidth Internet-facing SLB instance, you cannot set this parameter to -1. The sum of bandwidth limits that you specify for all listeners of the SLB instance cannot exceed the bandwidth limit of the SLB instance. For a pay-by-data-transfer Internet-facing SLB instance, you can set this parameter to -1, which specifies that the bandwidth is unlimited. |
| BackendServ erPort | Integer | Yes | No | The backend port that is used by the SLB instance. | Valid values: 1 to 65535. |
| LoadBalance rId | String | Yes | No | The ID of the SLB instance. | None |
| HealthCheck | Map | No | No | The health check settings of the listener. | For more information, see HealthCheck properties. |
| Persistence | Map | No | Yes | The persistence properties. | For more information, see Persistence properties. |
| Scheduler | String | No | No | The scheduling algorithm. | Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed to backend servers in sequence. |
| CACertificateI d | String | No | No | The ID of the certificate authority (CA) certificate. | This parameter is valid only when the Protocol parameter is set to https. |

| User Guide·Reso | urce types |   |   |   | Resource Orchestration Servic |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |
| ServerCertific ateId | String | No | Yes | The ID of the server certificate. | This parameter is required and valid only when the Protocol parameter is set to https. |
| VServerGrou pId | String | No | No | The ID of the server group. | None |
| RequestTime out | Integer | No | No | The timeout period of a request. | Valid values: 1 to 180. Unit: seconds. |
| IdleTimeout | Integer | No | No | The timeout period of an idle connection. | Valid values: 1 to 60. Unit: seconds. |
| HttpConfig | Map | No | No | The HTTP configuratio ns. | For more information, see HttpConfig properties. |
| Description | String | No | No | The description of the listener. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| PortRange | List | No | No | The range of ports on which the SLB instance listens. | Set StartPort to 1 and EndPort to 65535. For more information, see PortRange properties. |
| StartListener | Boolean | No | No | Specifies whether to start the listener. | Valid values: true (default): starts the listener. false: does not start the listener. |

HealthCheck syntax

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

HealthCheck properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Domain | String | No | No | The domain name that is used for health checks. | Valid values: $ ip _ Custom string: A custom string must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), and periods (.). An empty string Not e When this parameter is set to $ ip _ or left empty, the SLB instance uses the private IP addresses of backend servers as the domain names for health checks. |
| Interval | Integer | No | No | The interval between two consecutive health checks. | Valid values: 1 to 5. Unit: seconds. |
| URI | String | No | No | The URI that is used for health checks. | The URI must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URI must start with a forward slash (/). |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HttpCode | String | No | No | The HTTP status code. | Valid values: http 2xx (default) _ http 3xx _ http 4xx _ http 5xx _ Separate multiple HTTP status codes with commas (,). |
| HealthyThres hold | Integer | No | No | The threshold that is used to determine whether a backend server is healthy. This value specifies the number of consecutive successful health checks that is required before the health status of a backend server is changed from fail to success. | Valid values: 1 to 10. |
| HealthCheck Type | String | No | No | The type of health check. | Valid values: tcp http |
| Timeout | Integer | No | No | The timeout period of a health check response. | Valid values: 1 to 50. Unit: seconds. Not e This parameter is valid only when the value is greater than or equal to the value of the Interval parameter. Otherwise, the value of this parameter is overwritten by the value of the Interval parameter. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| UnhealthyThr eshold | Integer | No | No | The threshold that is used to determine whether a backend server is unhealthy. This value specifies the number of consecutive failed health checks that is required before the health status of a backend server is changed from success to fail. | Valid values: 1 to 10. |
| Port | Integer | No | No | The port that is used for health checks. | Valid values: 0 to 65535. |
| Switch | String | No | No | Specifies whether to enable health checks. | Valid values: on: enables health checks. off: disables health checks. Not e This parameter is valid only when the Protocol parameter is set to http or https. If the Switch parameter is not set, health checks are disabled by default unless health check items are already configured. |

Persistence syntax

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

Persistence properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StickySession | String | No | Yes | Specifies whether to enable session persistence. | Valid values: on: enables session persistence. off: disables session persistence. |
| PersistenceTi meout | Integer | No | Yes | The timeout period for session persistence. | Valid values: 0 to 1000. Default value: 0. 0: disables sessions persistence. Unit: seconds. |
| CookieTimeo ut | Integer | No | Yes | The timeout period of a cookie. | Valid values: 1 to 86400. Unit: seconds. Not e This parameter is required when the StickySession parameter is set to on and the StickySessionType parameter is set to insert. |
| XForwardedF or | String | No | Yes | Specifies whether to use the X- Forwarded- For header to obtain the real IP address of a client. | Valid values: on: uses the X-Forwarded- For header to obtain the real IP address of a client. off (default): does not use the X-Forwarded-For header to obtain the real IP address of a client. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| XForwardedF or proto _ | String | No | Yes | Specifies whether to use the X- Forwarded- Proto header to obtain the listener protocol of the SLB instance. | Valid values: on: uses the X-Forwarded- Proto header to obtain the listener protocol of the SLB instance. off (default): does not use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. |
| XForwardedF or SLBID _ | String | No | Yes | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. | Valid values: on: uses the SLB-ID header to obtain the ID of the SLB instance. off (default): does not use the SLB-ID header to obtain the ID of the SLB instance. |
| XForwardedF or SLBIP _ | String | No | Yes | Specifies whether to use the SLB- IP header to obtain the real IP address that is requested by a client. | Valid values: on: uses the SLB-IP header to obtain the real IP address that is requested by a client. off (default): does not use the SLB-IP header to obtain the real IP address that is requested by a client. |
| Cookie | String | No | Yes | The cookie that is configured on the server. | The cookie must be 1 to 200 characters in length, and cannot start with a dollar sign ($). The cookie can contain letters and digits, and cannot contain commas (,), semicolons (;), or spaces. Not e This parameter is required when the StickySession parameter is set to on and the StickySessionType parameter is set to server. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StickySession Type | String | No | Yes | The method that is used to handle a cookie. | Valid values: insert: inserts a cookie. server: rewrites a cookie. Not e This parameter is required when the StickySession parameter is set to on. |
| XForwardedF or ClientSrcP _ ort | String | No | Yes | Specifies whether to use the X- Forwarded- Client- srcport header to obtain the port that is used by a client to connect to the SLB instance. | Valid values: on: uses the X-Forwarded- Client-srcport header to obtain the port that is used by a client to connect to the SLB instance. off (default): does not use the X-Forwarded-Client- srcport header to obtain the port that is used by a client to connect to the SLB instance. |
| XForwardedF or SLBPORT _ | String | No | Yes | Specifies whether to use the X- Forwarded- Proto header to obtain the listener protocol of the SLB instance. | Valid values: on: uses the X-Forwarded- Proto header to obtain the listener protocol of the SLB instance. off (default): does not use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. |

HttpConfig syntax

```json
"HttpConfig": {
  "ForwardPort": Integer,
  "ListenerForward": String
```

HttpConfig properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ForwardPort | Integer | No | No | The port that is used to redirect HTTP requests to HTTPS. | Valid values: 1 to 65535. Default value: 443. |
| ListenerForw ard | String | No | No | Specifies whether to enable redirection from HTTP to HTTPS. | Valid values: on: enables redirection. off (default:) disables redirection. |

PortRange syntax

```json
"PortRange": [
    "StartPort": Integer,
    "EndPort": Integer
```

`]` PortRange properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StartPort | Integer | Yes | No | The start of the port range. | Set the value to 1. |
| EndPort | Integer | Yes | No | The end of the port range. | Set the value to 65535. |

Response parameters Fn::GetAtt LoadBalancerId: the unique ID of the SLB instance. ListenerPortsAndProtocol: the ports and protocols that are used by the SLB listener. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LoadBalancerId": {
      "Type": "String",
      "Label": "SLB instance ID",
      "Default": "slb-*****"
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
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        "BackendServerPort": 80,
        "Protocol": "tcp"
  "Outputs": {
```

To view more examples, visit Listener.json and Listener.yml. The examples describe the following resource types: ALIYUN::SLB::Listener, ALIYUN::SLB::LoadBalancerClone, ALIYUN::SLB::Certificate, ALIYUN::SLB::DomainExtension, ALIYUN::SLB::VServerGroup, ALIYUN::SLB::Rule, and ALIYUN::SLB::BackendServerToVServerGroupAddition.

#### 6.7.7 ALIYUN::SLB::LoadBalancer

ALIYUN::SLB::LoadBalancer is used to create an SLB instance. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the RDS instance belongs. | None |
| DeletionProtecti on | Boolean | Erased | Released | Specifies whether to enable deletion protection to prevent the SLB instance from being deleted by mistake. | Valid values: true false |
| VpcId | String | Yes | Released | The ID of the VPC. | None |
| SlaveZoneId | String | Yes | Released | The ID of the secondary zone to which the SLB instance belongs. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Bandwidth | String | Optional | Released | The peak bandwidth of SLB instances that are connected to the Internet and billed by fixed bandwidth. | For SLB instances that are connected to the Internet and billed by fixed Bandwidth, this parameter is valid only when the Bandwidth parameter of the SLB Listener is specified. For Internet instances whose billing type is to pay by traffic, we recommend that you set the peak Bandwidth through the Listener parameter. In this case, this parameter is ignored. Valid values: 1 to 1000. Unit: Mbps. Default value: 1 VPC-type instances are billed by traffic. |
| AddressType | String | Yes | Released | The address type of the SLB instance. | Valid values: internet intranet Default value: internet. |
| VSwitchId | String | Yes | Released | The ID of the vSwitch in the VPC. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerNa me | String | Yes | Released | The name of the SLB instance to be created. | A custom string. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ If this parameter is not specified, the system assigns a value. |
| InternetChargeT ype | String | Yes | Released | The billing method of SLB instances that are connected to the Internet. | Valid values: paybybandwi dth paybytraffic Default value: paybytraffic. |
| MasterZoneId | String | Yes | Released | The ID of the primary zone to which the SLB instance belongs. | None |
| Tags | List | Erased | Released | The tags to be attached to the SLB instance. The tags are listed in JSON format. Each tag consists of a TagKey and a TagValue. | A maximum of five tags can be attached to an SLB instance. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerSp ec | String | Yes | Released | The type of the SLB instance. | Valid values: slb.s1.small slb.s2.small slb.s2.mediu m slb.s3.small slb.s3.mediu m slb.s3.large The available types vary by region. |
| AutoPay | Boolean | Erased | Released | Specifies whether to automatically pay for subscription SLB instances that are connected to the Internet. | Valid values: true false Default value: false. Not e This parameter is valid only on the China site (aliyun.com ). |
| PayType | String | Yes | Released | The billing method of the SLB instance. | Valid values: PayOnDeman d PrePay |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PricingCycle | String | Yes | Released | The billing cycle of subscription SLB instances that are connected to the Internet. | Valid values: month year Not e This parameter is valid only on the China site (aliyun.com ). |
| Duration | Number | Erased | Released | The subscription period of subscription SLB instances that are connected to the Internet. | Valid values: Valid values when the PricingCycle parameter is set to month: 1 to 9. Valid values when the PricingCycle parameter is set to year: 1 to 3. Not e This parameter is valid only on the China site (aliyun.com ). |

Tags syntax

```json
"Tags": [
    "Value": String ,
    "Key": String
```

`]` Tags properties

| Property | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |
| Value | String | Yes | Released | None | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::Get At t LoadBalancerId: the unique ID of the SLB instance. NetworkType: the network type of the SLB instance, which can be vpc or classic. AddressType: the address type of the SLB instance, which can be intranet or internet. IpAddress: the IP address of the SLB instance. OrderId: the ID of the order. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "CreateLoadBalance": {
      "Type": "ALIYUN::SLB::LoadBalancer",
      "Properties": {
        "LoadBalancerName": "createdByHeat",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
  "Outputs": {
    "LoadBalanceDetails": {
      "Value": {
        "Fn::GetAtt": ["CreateLoadBalance", "LoadBalancerId"]}
```

#### 6.7.8 ALIYUN::SLB::LoadBalancerClone

ALIYUN::SLB::LoadBalancerClone is used to clone an SLB instance. Syntax

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
    "BackendServers": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | No | No | The ID of the resource group to which the SLB instance belongs. | None. |
| VSwitchId | String | No | No | The ID of the vSwitch. | The vSwitch must be in the same VPC as the source SLB instance. If you do not specify this parameter, the vSwitch of the source SLB instance is used. |
| SourceLoadBala ncerId | String | Yes | No | The ID of the SLB instance to be cloned. | None. |
|   |   |   |   |   | Default value: clone. Valid values: clone: The ECS instances listened by the source SLB instance and the weight of |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | each ECS Constraint instance are |
| BackendServers Policy | String | No | No | The clone policy, which specifies the ECS instances listened by the new SLB instance and the weight of each ECS instance. | cloned to the new SLB instance. empty: No ECS instances are attached to the new SLB instance. append: The ECS instances listened by the source SLB instance and the weight of each ECS instance are cloned to the new SLB instance. New ECS instances that have weights specified are also attached to the new SLB instance. replace: New ECS instances that have weights specified are attached to the new SLB instance. However, the ECS instances listened by the source SLB instance and the weight of each ECS instance are not cloned to the new SLB instance. |
| BackendServers | List | No | Yes | The list of new ECS instances to be listened. | For more information, see BackendServers properties. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerNa me | String | No | No | The name of the new SLB instance. | You can customize the instance name. The name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| Tags | List | No | Yes | The list of tags to be bound to the SLB instance. | Tags must be specified as key-value pairs. A maximum of five tags can be specified. For more information, see Tags properties. |
| TagsPolicy | String | No | No | The policy for handling tags. | Default value: empty. Valid values: clone: The tags of the source SLB instance are used. empty: No tags are configured. append: The tags of the source SLB instance are reserved while new tags are added. replace: The tags of the source SLB instance are deleted while new tags are added. |

BackendServers syntax

```json
"BackendServers": [
    "Type": String,
    "ServerId": String,
    "Description": String,
    "ServerIp": String,
    "Weight": Integer
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | Only ECS instances in the running state can be attached to the SLB instance as backend servers. A maximum of 20 backend servers can be attached each time. You can specify elastic network interfaces (ENIs) as the backend servers for only guaranteed- performance SLB instances. |
| Weight | Integer | Yes | Yes | The weight of the ECS instance to be attached to the SLB instance. | Valid values: 0 to 100. Default value: 100. |
| ServerIp | String | No | No | The IP address of the backend server. | None. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Type | String | No | No | The type of the backend server. | Default value: ecs. Valid values: ecs: ECS instance eni: ENI eci: Elastic Container Instance (ECI) |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The tag key. | The tag key must be 1 to 128 characters in length and cannot start with acs: or aliyun . It cannot contain http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Value | String | No | No | The tag value. | The tag value must be 0 to 128 characters in length and cannot start with acs: or aliyun . It cannot contain http:// or https:// . |

Response parameters Fn::GetAtt LoadBalancerId: the ID of the new SLB instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LoadBalancerName": {
      "Type": "String",
      "Description": "Name of created load balancer. Length is limited to 1-80 characters, allowe
d to contain letters, numbers, '-, /, _,.' When not specified, a default name will be assigned."
    "SourceLoadBalancerId": {
      "Type": "String",
      "Description": "Source load balancer id to clone"
    "ResourceGroupId": {
      "Type": "String",
      "Description": "Resource group id."
    "TagsPolicy": {
      "Type": "String",
      "Description": "Solution for handle the tags. If select 'clone', it will clone from source
load balancer. If select 'empty' it will not coppy tags. If select 'append' it will append the ne w tags. If select 'replace' it will add new tags.\nDefault is 'empty'. ",
      "AllowedValues": [
        "clone",
        "empty",
        "append",
        "replace"
```

`],`

```json
      "Default": "empty"
    "VSwitchId": {
      "Type": "String",
      "Description": "The new vSwitch ID to create load balancer instance. For VPC network only a
nd the vSwitch should belong to the VPC which source load balancer is located. When not specified , source load balancer VSwitch ID will be used."
```

```
,souce oadbaace Swtc
```

`w`

```json
beused.
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of ECS instance, which will attached to load balancer."
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to slb. Max support 5 tags to add during create slb. Each ta
g with two properties Key and Value, and Key is required.",
      "MaxLength": 5
    "BackendServersPolicy": {
      "Type": "String",
      "Description": "Solution for handle the backend server and weights. If select 'clone', it w
ill clone from source load balancer. If select 'empty' it will not attach any backend servers. If select 'append' it will append the new backend server list to source backed servers. If select 'r eplace' it will only attach new backend server list. Default is 'clone'. ",
      "AllowedValues": [
        "clone",
        "empty",
        "append",
        "replace"
```

`],`

```json
      "Default": "clone"
  "Resources": {
    "LoadBalancerClone": {
      "Type": "ALIYUN::SLB::LoadBalancerClone",
      "Properties": {
        "LoadBalancerName": {
          "Ref": "LoadBalancerName"
        "SourceLoadBalancerId": {
          "Ref": "SourceLoadBalancerId"
        "ResourceGroupId": {
          "Ref": "ResourceGroupId"
        "TagsPolicy": {
          "Ref": "TagsPolicy"
        "VSwitchId": {
          "Ref": "VSwitchId"
        "BackendServers": {
          "Ref": "BackendServers"
        "Tags": {
          "Ref": "Tags"
        "BackendServersPolicy": {
          "Ref": "BackendServersPolicy"
```

```json
  "Outputs": {
    "LoadBalancerId": {
      "Description": "The id of load balance generated",
      "Value": {
        "Fn::GetAtt": [
          "LoadBalancerClone",
          "LoadBalancerId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  LoadBalancerName:
    Type: String
    Description: >-
      Name of created load balancer. Length is limited to 1-80 characters,
      allowed to contain letters, numbers, '-, /, _,.' When not specified, a
      default name will be assigned.
  SourceLoadBalancerId:
    Type: String
    Description: Source load balancer id to clone
  ResourceGroupId:
    Type: String
    Description: Resource group id.
  TagsPolicy:
    Type: String
    Description: >-
      Solution for handle the tags. If select 'clone', it will clone from source
      load balancer. If select 'empty' it will not coppy tags. If select
      'append' it will append the new tags. If select 'replace' it will add new
      tags.
      Default is 'empty'.
    AllowedValues:
      - clone
      - empty
      - append
      - replace
    Default: empty
  VSwitchId:
    Type: String
    Description: >-
      The new vSwitch ID to create load balancer instance. For VPC network only
      and the vSwitch should belong to the VPC which source load balancer is
      located. When not specified, source load balancer vSwitch ID will be used.
  BackendServers:
    Type: Json
    Description: 'The list of ECS instance, which will attached to load balancer.'
  Tags:
    Type: Json
    Description: >-
      Tags to attach to slb. Max support 5 tags to add during create slb. Each
      tag with two properties Key and Value, and Key is required.
```

```
tagwt twopopetes eyad aue,ad
```

`ey` `s`

```
equ ed.
    MaxLength: 5
  BackendServersPolicy:
    Type: String
    Description: >-
      Solution for handle the backend server and weights. If select 'clone', it
      will clone from source load balancer. If select 'empty' it will not attach
      any backend servers. If select 'append' it will append the new backend
      server list to source backed servers. If select 'replace' it will only
      attach new backend server list. Default is 'clone'.
    AllowedValues:
      - clone
      - empty
      - append
      - replace
    Default: clone
Resources:
  LoadBalancerClone:
    Type: 'ALIYUN::SLB::LoadBalancerClone'
    Properties:
      LoadBalancerName:
        Ref: LoadBalancerName
      SourceLoadBalancerId:
        Ref: SourceLoadBalancerId
      ResourceGroupId:
        Ref: ResourceGroupId
      TagsPolicy:
        Ref: TagsPolicy
      VSwitchId:
        Ref: VSwitchId
      BackendServers:
        Ref: BackendServers
      Tags:
        Ref: Tags
      BackendServersPolicy:
        Ref: BackendServersPolicy
Outputs:
  LoadBalancerId:
    Description: The id of load balance generated
    Value:
      'Fn::GetAtt':
        - LoadBalancerClone
        - LoadBalancerId
```

#### 6.7.9 ALIYUN::SLB::MasterSlaveServerGroup

ALIYUN::SLB::MasterSlaveServerGroup is used to create a primary/secondary server group. Not ice A primary/secondary server group contains only two ECS instances: a primary server and a secondary server. Syntax

```json
  "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
  "Properties": {
    "MasterSlaveServerGroupName": String,
    "MasterSlaveBackendServers": List,
    "LoadBalancerId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterSlaveSer verGroupName | String | No | No | The name of the primary/second ary server group. | None |
| MasterSlaveBac kendServers | List | Yes | No | The list of backend servers in the primary/second ary server group. | A primary/second ary server group can contain a maximum of two backend servers. If you do not specify this parameter, an empty primary/second ary server group is created. |
| LoadBalancerId | String | Yes | No | The ID of the SLB instance. | None |

MasterSlaveBackendServers syntax

```json
"MasterSlaveBackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "ServerType": String
```

`]` MasterSlaveBackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | No | The ID of the ECS instance or Elastic Network Interface (ENI) to be added. | None |
| ServerType | String | No | No | The type of the server. | Default value: Master. Valid values: Master Slave |
| Port | Integer | Yes | No | The port number used by the backend server. | Valid values: 1 to 65535. |
| Weight | Integer | Yes | No | The weight of the backend server. | Valid values: 0 to 100. |

Response parameters Fn::GetAtt MasterSlaveServerGroupId: the ID of the primary/secondary server group. Examples

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
            "ServerId": "vm****",
            "Port": "90",
            "Weight": "100",
            "ServerType": "Slave"
```

`],`

```json
        "LoadBalancerId": "lb-bp1hv944r69al4j9j****"
  "Outputs": {
    "MasterSlaveServerGroupId": {
      "Value": {
        "Fn::GetAtt": [
          "MasterSlaveServerGroup",
          "MasterSlaveServerGroupId"
```

`]`

#### 6.7.10 ALIYUN::SLB::Rule

ALIYUN::SLB::Rule is used to add forwarding rules for a specified HTTP or HTTPS listener. Syntax

```json
  "Type": "ALIYUN::SLB::Rule",
  "Properties": {
    "ListenerPort": Integer,
    "RuleList": List,
    "LoadBalancerId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ListenerPort | Integer | Yes | No | The frontend listener port number used by the SLB instance. | Valid values: 1 to 65535. |
| RuleList | List | Yes | No | The list of forwarding rules to be added. | A maximum of 10 forwarding rules can be added at a time. Each forwarding rule contains the following parameters: RuleName Domain Url VServerGrou pId You must specify at least one of the Domain and URL parameters. The value combination specified by the Domain and URL parameters must be unique in a listener. |
| LoadBalancerId | String | Yes | No | The ID of the SLB instance. | None. |

RuleList syntax

```json
"RuleList": [
    "Url": String,
    "Domain": String,
    "VServerGroupId": String,
    "RuleName": String
```

`]` RuleList properties

| Property | Type | Required | Editable | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| Url | String | No | No | The request URL. |   | The URL must be 2 to 80 characters in length. It must start with a forward slash (/) and can contain letters, digits, and the following special characters: - / . % ? # & |   |   |
|   |   |   |   |   |   |   | - / . % ? |   |
|   |   |   |   |   |   | # & |   |   |
| Domain | String | No | No | The request domain name associated with the forwarding rule. |   | None. |   |   |
| VServerGroupId | String | Yes | No | The ID of the destination VServer group specified in the forwarding rule. |   | None. |   |   |
| RuleName | String | Yes | No | The name of the forwarding rule. |   | The name must be 1 to 40 characters in length and can contain letters, digits, and the following special characters: - / . _ Forwarding rule names must be unique within each listener. |   |   |

Response parameters Fn::GetAtt Rules: the list of forwarding rules. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Rule": {
      "Type": "ALIYUN::SLB::Rule",
      "Properties": {
        "ListenerPort": {
          "Ref": "ListenerPort"
        "RuleList": {
          "Fn::Split": [",", {
            "Ref": "RuleList"
          }, {
            "Ref": "RuleList"
```

`}]`

```json
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
  "Parameters": {
    "ListenerPort": {
      "Type": "Number",
      "Description": "The front-end HTTPS listener port of the Server Load Balancer instance. Val
id value:\n1-65535",
      "MaxValue": 65535,
      "MinValue": 1
    "RuleList": {
      "MinLength": 1,
      "Type": "CommaDelimitedList",
      "Description": "The forwarding rules to add.",
      "MaxLength": 10
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The ID of Server Load Balancer instance."
  "Outputs": {
    "Rules": {
      "Description": "A list of forwarding rules. Each element of rules contains \"RuleId\".",
      "Value": {
        "Fn::GetAtt": ["Rule", "Rules"]
```

#### 6.7.11 ALIYUN::SLB::VServerGroup

ALIYUN::SLB::VServerGroup is used to create a vServer group and attach backend servers to a Server Load Balancer (SLB) instance. Syntax

```json
  "Type": "ALIYUN::SLB::VServerGroup",
  "Properties": {
    "VServerGroupName": String,
    "BackendServers": List,
    "LoadBalancerId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGrou pName | String | Yes | No | The name of the vServer group. | None |
| BackendServ ers | List | No | Yes | The list of backend servers. | You can attach a maximum of 20 Elastic Compute Service (ECS) instances. For more information, see BackendServers properties. |
| LoadBalance rId | String | Yes | No | The ID of the SLB instance. | None |

BackendServers syntax

```json
"BackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer,
    "Type": String,
    "Description": String,
    "ServerIp": String
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the backend server. | None |
| Port | Integer | Yes | Yes | The port that is used by the backend server. | Valid values: 1 to 65535. |

| esource Orches | tration Service |   |   |   | User Guide·Resource type |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |
| Weight | Integer | No | Yes | The weight of the backend server. | Valid values: 0 to 100. |
| Type | String | No | Yes | The type of the backend server. | Default value: ecs. Valid values: ecs: ECS instances eni: elastic network interfaces (ENIs) |
| Description | String | No | Yes | The description of the backend server. | The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| ServerIp | String | No | Yes | The IP address of the backend server. | The IP addresses of ECS instances or ENIs are supported. |

Response parameters Fn::GetAtt VServerGroupId: the ID of the vServer group. BackendServers: the list of backend servers attached to the SLB instance. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VServerGroupName": {
      "Type": "String",
      "Description": "Display name of the VServerGroup."
    "LoadBalancerId": {
      "Type": "String",
      "Description": "The id of load balancer."
    "BackendServers": {
      "Type": "Json",
      "Description": "The list of a combination of ECS Instance-Port-Weight.Same ecs instance wit
h different port is allowed, but same ecs instance with same port isn't."
  "Resources": {
    "VServerGroup": {
      "Type": "ALIYUN::SLB::VServerGroup",
      "Properties": {
        "VServerGroupName": {
          "Ref": "VServerGroupName"
        "LoadBalancerId": {
          "Ref": "LoadBalancerId"
        "BackendServers": {
          "Ref": "BackendServers"
  "Outputs": {
    "VServerGroupId": {
      "Description": "The id of VServerGroup created.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "VServerGroupId"
```

`]`

```json
    "BackendServers": {
      "Description": "Backend server list in this VServerGroup.",
      "Value": {
        "Fn::GetAtt": [
          "VServerGroup",
          "BackendServers"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  VServerGroupName:
    Type: String
    Description: Display name of the VServerGroup.
  LoadBalancerId:
    Type: String
    Description: The id of load balancer.
  BackendServers:
    Type: Json
    Description: >-
      The list of a combination of ECS Instance-Port-Weight.Same ecs instance
      with different port is allowed, but same ecs instance with same port
      isn't.
Resources:
  VServerGroup:
    Type: 'ALIYUN::SLB::VServerGroup'
    Properties:
      VServerGroupName:
        Ref: VServerGroupName
      LoadBalancerId:
        Ref: LoadBalancerId
      BackendServers:
        Ref: BackendServers
Outputs:
  VServerGroupId:
    Description: The id of VServerGroup created.
    Value:
      'Fn::GetAtt':
        - VServerGroup
        - VServerGroupId
  BackendServers:
    Description: Backend server list in this VServerGroup.
    Value:
      'Fn::GetAtt':
        - VServerGroup
        - BackendServers
```

To view more examples, visit Listener.json and Listener.yml. In the examples, the ALIYUN::SLB::Listener, ALIYUN::SLB::LoadBalancerClone, ALIYUN::SLB::Certificate, ALIYUN::SLB::DomainExtension, ALIYUN::SLB::VServerGroup, ALIYUN::SLB::Rule, and ALIYUN::SLB::BackendServerToVServerGroupAddition resource types are involved.

### 6.8 SLS

#### 6.8.1 ALIYUN::SLS::Index

ALIYUN::SLS::Index is used to create an index for a specified Logstore. Syntax

```json
  "Type": "ALIYUN::SLS::Index",
  "Properties": {
    "ProjectName": String,
    "FullTextIndex": Map,
    "LogstoreName": String,
    "KeyIndices": List,
    "LogReduce": Boolean
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | No | The name of the Log Service project. | The name must be 3 to 36 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). _ It must start with a lowercase letter or digit. |
| FullTextIndex | Map | Yes | Yes | The full-text index configurations. | For more information, see FullTextIndex properties. |
| LogstoreName | String | Yes | No | The name of the Logstore. | None |
| KeyIndices | List | No | Yes | The field index configurations. | You must specify at least one of the FullTextIndex and KeyIndices parameters. For more information, see Properties. |
| LogReduce | Boolean | No | Yes | Specifies whether to enable LogReduce. | Default value: false. Valid values: true false |

FullTextIndex syntax

```json
"FullTextIndex": {
  "CaseSensitive": Boolean,
  "Delimiter": String,
  "IncludeChinese": Boolean,
  "Enable": Boolean
```

FullTextIndex properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Enable | Boolean | Yes | Yes | Specifies whether to enable full-text indexing. | Default value: true. Valid values: true false |
| CaseSensitive | Boolean | No | Yes | Specifies whether the field is case- sensitive. | Default value: false. Valid values: true false |
| Delimiter | String | No | Yes | The delimiter that is used to separate keywords. | Valid values: ,'";=()[] {}? @& <>/:\n\t\r |
| IncludeChinese | Boolean | No | Yes | Specifies whether to support Chinese word segmentation. | Default value: false. Valid values: true false |

KeyIndices syntax

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

`]` KeyIndices properties

| Property | Type | Required |   |   | Editable |   | Description |   | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|---|
| Name | String | Yes |   |   | Yes |   | The name of the field. |   | You can use a nested name that is separated with periods (.). Example: k1.k2.k3. |   |
| EnableAnalytics | Boolean | No |   |   | Yes |   | Specifies whether to enable statistical analysis on the field. |   | Default value: true. Valid values: true false |   |
| Delimiter | String | No |   |   | Yes |   | The delimiter that is used to separate keywords. |   | Valid values: ,'";=()[] {}? @& <>/:\n\t\r |   |
| CaseSensitive | Boolean | No |   |   | Yes |   | Specifies whether the field is case- sensitive. |   | Default value: false. Valid values: true false This parameter takes effect only when the Type parameter is set to text or json. |   |
| JsonKeyIndices | List | No |   |   | Yes |   | The JSON index configurations. Format: [{"key1": |   | Supported keys are Name, Alias, Type, and EnableAnalytics |   |
|   |   |   |   |   |   |   |   | [{"key1": | . |   |
|   |   |   |   |   |   |   | "value1", |   |   |   |
|   |   |   |   |   |   |   |   |   | For more |   |
|   |   |   |   |   |   |   | "key2": |   | inform |   |
|   |   |   |   |   |   |   | "value2", |   |   |   |
|   |   |   |   |   |   |   | ...}] |   |   |   |
| Alias | String | No |   |   | Yes |   | The alias of the field. |   | None |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IncludeChinese | Boolean | No | Yes | Specifies whether to support Chinese word segmentation. | Default value: false. Valid values: true false This parameter takes effect only when the Type parameter is set to text. |
| Type | String | Yes | Yes | The type of the field. | Default value: text. Valid values: text long double json |

JsonKeyIndices syntax

```json
"JsonKeyIndices": [
    "Type": String,
    "Alias": String,
    "EnableAnalytics": Boolean,
    "Name": String
```

`]` JsonKeyIndices properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | Yes | The name of the field. | None |
| EnableAnalytics | Boolean | No | Yes | Specifies whether to enable statistical analysis on the field. | Valid values: true false |
| Alias | String | No | Yes | The alias of the field. | None |
| Type | String | Yes | Yes | The type of the field. | None |

Response parameters Fn::GetAtt None Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Index": {
      "Type": "ALIYUN::SLS::Index",
      "Properties": {
        "ProjectName": {
          "Ref": "ProjectName"
        "FullTextIndex": {
          "Ref": "FullTextIndex"
        "LogstoreName": {
          "Ref": "LogstoreName"
        "KeyIndices": {
          "Ref": "KeyIndices"
        "LogReduce": {
          "Ref": "LogReduce"
  "Parameters": {
    "ProjectName": {
      "Type": "String",
      "Description": "Project name:1. Only supports lowercase letters, numbers, hyphens (-) and u
nderscores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 3-6 3 characters.",
      "MinLength": 3,
      "MaxLength": 63
    "FullTextIndex": {
      "Type": "Map",
      "Description": "Full-text indexing configuration.Full-text indexing and key indexing must h
ave at least one enabled."
    "LogstoreName": {
      "Type": "String",
      "Description": "Logstore name:1. Only supports lowercase letters, numbers, hyphens (-) and
underscores (_).2. Must start and end with lowercase letters and numbers.3. The name length is 3- 63 characters.",
      "MinLength": 3,
      "MaxLength": 63
    "KeyIndices": {
      "Type": "List",
```

`"` `i` `i` `"` `"` `i``d` `fi` `i` `ll` `i``d` `i` `d``k` `i``d` `i` `h` `l`

```json
      "Description": "Key index configurations.Full-text indexing and key indexing must have at l
east one enabled."
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

#### 6.8.2 ALIYUN::SLS::Logstore

ALIYUN::SLS::Logstore is used to create a Logstore in a Log Service project. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | No | The name of the Log Service project that the Logstore belongs to. | The name must be 3 to 36 characters in length. The name can contain lowercase letters, digits, hyphens (-), and underscores ( ). The name must start and _ end with a lowercase letter or digit. |
| ShardCount | Integer | No | Yes | The number of shards. | Valid values: 1 to 100. Default value: 2. |
| MaxSplitShar d | Integer | No | Yes | The maximum number of shards that can be obtained during automatic splitting. | Valid values: 1 to 64. MaxSplitShard is required if autoSplit is set to true. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LogstoreNa me | String | Yes | No | The name of the Logstore. | The name must be unique in a project. The name must be 3 to 36 characters in length. The name can contain lowercase letters, digits, hyphens (-), and underscores ( ). _ The name must start and end with a lowercase letter or digit. |
| AutoSplit | Boolean | No | Yes | Specifies whether to automaticall y split shards. | Default value: false. Valid values: true: automatically splits shards. false: does not automatically split shards. |
| TTL | Integer | No | Yes | The data retention period. | Valid values: 1 to 3600. Default value: 30. Unit: days. |
| EnableTracki ng | Boolean | No | Yes | Specifies whether to enable web tracking. | You can use web tracking to collect access information about web browsers, iOS applications, and Android applications. Default value: false. Valid values: true: enables web tracking. false: disables web tracking. |
| PreserveStor age | Boolean | No | Yes | Specifies whether to permanently retain logs. | Default value: false. Valid values: true: permanently retains logs. The TTL parameter does not take effect if PreserveStorage is set to true. false: does not permanently retain logs. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AppendMeta | Boolean | No | Yes | Specifies whether to automaticall y add the public IP address of the client and the log arrival time after the log is received. | Default value: false. Valid values: true: automatically adds the public IP address of the client and the log collection time after the log is received. false: does not automatically add the public IP address of the client and the log collection time after the log is received. |
| EncryptConf | Map | No | No | The data encryption configuratio ns. | For more information, see EncryptConf syntax and EncryptConf properties. |

EncryptConf syntax

```json
"EncryptConf": {
    "Enable": Boolean,
    "EncryptType": String,
    "UserCmkInfo": Map
```

EncryptConf properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Enable | Boolean | Yes | No | Specifies whether to enable data encryption. | Default value: false. Valid values: true: enables data encryption. false: does not enable data encryption. |
| EncryptType | String | Yes | No | The encryption algorithm. | Valid values: default: the Advanced Encryption Standard (AES) algorithm. m4: the SM4 encryption algorithm. Not e For more information about data encryption, see Encrypt data. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| UserCmkInfo | Map | No | No | We recommend that you use the bring- your-own- key (BYOK) method to encrypt or decrypt data if UserCmkInfo is specified. If UserCmkInfo is not specified, the service key of Log Service is used to encrypt or decrypt data. | For more information, see UserCmkInfo syntax and UserCmkInfo properties. |

UserCmkInfo syntax

```json
"UserCmkInfo": {
    "CmkKeyId": String,
    "Arn": String,
    "RegionId": String
```

UserCmkInfo properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CmkKeyId | String | Yes | No | The ID of the customer master key (CMK) to which the BYOK key belongs. | None |
| Arn | String | Yes | No | The ID of the region to which the CMK belongs. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RegionId | String | Yes | No | The Alibaba Cloud Resource Name (ARN) of the RAM role. | For more information about how to obtain the ARN of a RAM role, see Ship log data from Log Service to OSS. |

Response parameters Fn::GetAtt LogstoreName: the name of the Logstore. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "LogstoreName": {
      "Type": "String",
      "Description": "Logstore name:\n1. Only supports lowercase letters, numbers, hyphens (-) an
d underscores (_).\n2. Must start and end with lowercase letters and numbers.\n3. The name length is 3-63 characters.",
      "MinLength": 3,
      "MaxLength": 63
    "PreserveStorage": {
      "Type": "Boolean",
      "Description": "Whether to keep the log permanently.\nIf set to true, TTL will be ignored.\
nDefault to false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "ProjectName": {
      "Type": "String",
      "Description": "Project name:\n1. Only supports lowercase letters, numbers, hyphens (-) and
underscores (_).\n2. Must start and end with lowercase letters and numbers.\n3. The name length i s 3-63 characters.",
      "AllowedPattern": "^[a-zA-Z0-9_-]+$",
      "MinLength": 3,
      "MaxLength": 63
    "AppendMeta": {
      "Type": "Boolean",
      "Description": "Whether to add client external network IP and log arrival time after receiv
ing the log.\nDefault to false.",
      "AllowedValues": [
        "True",
        "true",
```

```
        "False",
        "false"
```

`],`

```json
      "Default": false
    "MaxSplitShard": {
      "Type": "Number",
      "Description": "The maximum number of shards when splitting automatically. Must be specifie
d if AutoSplit is set to true.\nAllowed Values: 1-64.",
      "MinValue": 1,
      "MaxValue": 64
    "AutoSplit": {
      "Type": "Boolean",
      "Description": "Whether to automatically split the shard.\nDefault to false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "EnableTracking": {
      "Type": "Boolean",
      "Description": "Whether to enable WebTracking, which supports fast capture of various brows
ers and iOS/Android/APP access information.\nDefault to false.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`],`

```json
      "Default": false
    "EncryptConf": {
      "Type": "Json",
      "Description": "Data encryption config"
    "TTL": {
      "Type": "Number",
      "Description": "The lifecycle of log in the logstore in days.\nAllowed Values: 1-3600, defa
ult to 30.",
      "MinValue": 1,
      "MaxValue": 3600,
      "Default": 30
    "ShardCount": {
      "Type": "Number",
      "Description": "The number of Shards.\nAllowed Values: 1-100, default to 2.",
      "MinValue": 1,
      "MaxValue": 100,
      "Default": 2
  "Resources": {
    "Logstore": {
```

```json
      "Type": "ALIYUN::SLS::Logstore",
      "Properties": {
        "LogstoreName": {
          "Ref": "LogstoreName"
        "PreserveStorage": {
          "Ref": "PreserveStorage"
        "ProjectName": {
          "Ref": "ProjectName"
        "AppendMeta": {
          "Ref": "AppendMeta"
        "MaxSplitShard": {
          "Ref": "MaxSplitShard"
        "AutoSplit": {
          "Ref": "AutoSplit"
        "EnableTracking": {
          "Ref": "EnableTracking"
        "EncryptConf": {
          "Ref": "EncryptConf"
        "TTL": {
          "Ref": "TTL"
        "ShardCount": {
          "Ref": "ShardCount"
  "Outputs": {
    "LogstoreName": {
      "Description": "Logstore name.",
      "Value": {
        "Fn::GetAtt": [
          "Logstore",
          "LogstoreName"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  AppendMeta:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
```

```
    - 'false'
    Default: false
    Description: 'Whether to add client external network IP and log arrival time after
      receiving the log.
      Default to false.'
    Type: Boolean
  AutoSplit:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Default: false
    Description: 'Whether to automatically split the shard.
      Default to false.'
    Type: Boolean
  EnableTracking:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Default: false
    Description: 'Whether to enable WebTracking, which supports fast capture of various
      browsers and iOS/Android/APP access information.
      Default to false.'
    Type: Boolean
  EncryptConf:
    Description: Data encryption config
    Type: Json
  LogstoreName:
    Description: 'Logstore name:
      1. Only supports lowercase letters, numbers, hyphens (-) and underscores (_).
      2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
    MinLength: 3
    Type: String
  MaxSplitShard:
    Description: 'The maximum number of shards when splitting automatically. Must
      be specified if AutoSplit is set to true.
      Allowed Values: 1-64.'
    MaxValue: 64
    MinValue: 1
    Type: Number
  PreserveStorage:
    AllowedValues:
    - 'True'
    - 'true'
    - 'False'
    - 'false'
    Default: false
    Description: 'Whether to keep the log permanently.
      If set to true, TTL will be ignored.
      Default to false.'
    Type: Boolean
  ProjectName:
```

```
    AllowedPattern: ^[a-zA-Z0-9_-]+$
    Description: 'Project name:
      1. Only supports lowercase letters, numbers, hyphens (-) and underscores (_).
      2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
    MinLength: 3
    Type: String
  ShardCount:
    Default: 2
    Description: 'The number of Shards.
      Allowed Values: 1-100, default to 2.'
    MaxValue: 100
    MinValue: 1
    Type: Number
  TTL:
    Default: 30
    Description: 'The lifecycle of log in the logstore in days.
      Allowed Values: 1-3600, default to 30.'
    MaxValue: 3600
    MinValue: 1
    Type: Number
Resources:
  Logstore:
    Properties:
      AppendMeta:
        Ref: AppendMeta
      AutoSplit:
        Ref: AutoSplit
      EnableTracking:
        Ref: EnableTracking
      EncryptConf:
        Ref: EncryptConf
      LogstoreName:
        Ref: LogstoreName
      MaxSplitShard:
        Ref: MaxSplitShard
      PreserveStorage:
        Ref: PreserveStorage
      ProjectName:
        Ref: ProjectName
      ShardCount:
        Ref: ShardCount
      TTL:
        Ref: TTL
    Type: ALIYUN::SLS::Logstore
Outputs:
  LogstoreName:
    Description: Logstore name.
    Value:
      Fn::GetAtt:
      - Logstore
      - LogstoreName
```

To view more examples, visit SLS.json and SLS.yml. In the examples, the ALIYUN::SLS::Project, ALIYUN::SLS::Logstore, ALIYUN::SLS::Index, ALIYUN::SLS::LogtailConfig, ALIYUN::SLS::MachineGroup, ALIYUN::SLS::ApplyConfigToMachineGroup, ALIYUN::ApiGateway::LogConfig, ALIYUN::SLS::Savedsearch, and ALIYUN::SLS::Alert resource types are used.

#### 6.8.3 ALIYUN::SLS::LogtailConfig

ALIYUN::SLS::LogtailConfig is used to configure Logtail parameters for data collection. Syntax

```json
  "Type": "ALIYUN::SLS::LogtailConfig",
  "Properties": {
    "ProjectName": String,
    "LogtailConfigName": String,
    "LogstoreName": String,
    "RawConfigData": Map,
    "CloneFrom": Map
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | No | The name of the Log Service project. | None |
| LogtailConfigNa me | String | Yes | No | The name of the Logtail configuration file. | The configuration file name must be unique in a project. The name must be 2 to 128 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It must _ start and end with a lowercase letter or digit. |
| LogstoreName | String | Yes | No | The name of the Logstore. | None |
|   |   |   |   |   | The format is the same as that of the response from the GetConfig operation of Log Service. |

| esource Orchestrat |   |   | ion Service |   |   |   |   |   |   | User Guide·Resource type |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Property |   |   | Type |   | Required | Editable |   | Description |   | If CloneFrom and Constraint RawConfigData are |   |
|   |   |   |   |   |   |   |   |   |   | both specified, the data of LogtailConfig and RawConfigData is merged. In this case, configName, outputType, and outputDetail of RawConfigData are ignored. Sample value: {"configName": |   |
|   |   |   |   |   |   |   |   |   |   |   | {"configName": |
|   |   |   |   |   |   |   |   |   |   | "test-logtail- |   |
|   |   |   |   |   |   |   |   |   |   | config", |   |
|   |   |   |   |   |   |   |   |   |   | "createTime": |   |
|   |   |   |   |   |   |   |   |   |   | 1574843554, |   |
|   |   |   |   |   |   |   |   |   |   | "inputDetail": |   |
|   |   |   |   |   |   |   |   |   |   | {"acceptNoEnoughKeys |   |
|   |   |   |   |   |   |   |   |   |   | ": false, |   |
|   |   |   |   |   |   |   |   |   |   | "adjustTimezone": |   |
|   |   |   |   |   |   |   |   |   |   | false, "advanced": { |   |
|   |   |   |   |   |   |   |   |   |   | "force multiconfig": _ |   |
|   |   |   |   |   |   |   |   |   |   | false }, |   |
|   |   |   |   |   |   |   |   |   |   | "autoExtend": true, |   |
|   |   |   |   |   |   |   |   |   |   | "delayAlarmBytes": |   |
|   |   |   |   |   |   |   |   |   |   | 0, "delaySkipBytes": |   |
|   |   |   |   |   |   |   |   |   |   | 0, "discardNonUtf8": |   |
|   |   |   |   |   |   |   |   |   |   | false, |   |
|   |   |   |   |   |   |   |   |   |   | "discardUnmatch": |   |
|   |   |   |   |   |   |   |   |   |   | false, |   |
|   |   |   |   |   |   |   |   |   |   | "dockerExcludeEnv": |   |
|   |   |   |   |   |   |   |   |   |   | {}, |   |
|   |   |   |   |   |   |   |   |   |   | "dockerExcludeLabel" |   |
|   |   |   |   |   |   |   |   |   |   | : {}, "dockerFile": |   |
|   |   |   |   |   |   |   |   |   |   | false, |   |
|   |   |   |   |   |   |   |   |   |   | "dockerIncludeEnv": |   |
|   |   |   |   |   |   |   |   |   |   | {}, |   |
|   |   |   |   |   |   |   |   |   |   | "dockerIncludeLabel" |   |
|   |   |   |   |   |   |   |   |   |   | : {}, |   |
|   |   |   |   |   |   |   |   |   |   | "enableRawLog": |   |
|   |   |   |   |   |   |   |   |   |   | false, "enableTag": |   |
|   |   |   |   |   |   |   |   |   |   | false, |   |
|   |   |   |   |   |   |   |   |   |   | "fileEncoding": |   |
|   |   |   |   |   |   |   |   |   |   | "utf8", |   |
| RawConfigData |   |   | Map |   | No | Yes |   | The raw configuration |   | "filePattern": |   |
|   |   |   |   |   |   |   |   | data. |   | "test.log*", |   |
|   |   |   |   |   |   |   |   |   |   | "filterKey": [], |   |
|   |   |   |   |   |   |   |   |   |   | "filterRegex": [], |   |
|   |   |   |   |   |   |   |   |   |   | "key": [ "time", |   |
|   |   |   |   |   |   |   |   |   |   | "logger", "level", |   |
|   |   |   |   |   |   |   |   |   |   | "request id", _ |   |
|   |   |   |   |   |   |   |   |   |   | "user id", _ |   |
|   |   |   |   |   |   |   |   |   |   | "region id", _ |   |
|   |   |   |   |   |   |   |   |   |   | "content" ], |   |
|   |   |   |   |   |   |   |   |   |   | "localStorage": |   |
|   |   |   |   |   |   |   |   |   |   | true, "logPath": |   |

|   |   |   |   |   | "/var/log/test", |   |   |
|---|---|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |   |   |
|   |   |   |   |   | "logTimezone": "", |   |   |
|   |   |   |   |   | "logType": |   |   |
|   |   |   |   |   | "delimiter log", _ |   |   |
|   |   |   |   |   | "maxDepth": 100, |   |   |
|   |   |   |   |   | "maxSendRate": -1, |   |   |
|   |   |   |   |   | "mergeType": |   |   |
|   |   |   |   |   | "topic", "preserve": |   |   |
|   |   |   |   |   | true, |   |   |
|   |   |   |   |   | "preserveDepth": 1, |   |   |
|   |   |   |   |   | "priority": 0, |   |   |
|   |   |   |   |   | "quote": "\u0001", |   |   |
|   |   |   |   |   | "sendRateExpire": 0, |   |   |
|   |   |   |   |   | "sensitive keys": _ |   |   |
|   |   |   |   |   | [], "separator": |   |   |
|   |   |   |   |   | ",,,", |   |   |
|   |   |   |   |   | "shardHashKey": [], |   |   |
|   |   |   |   |   | "tailExisted": |   |   |
|   |   |   |   |   | false, "timeFormat": |   |   |
|   |   |   |   |   | "", "timeKey": "", |   |   |
|   |   |   |   |   | "topicFormat": |   |   |
|   |   |   |   |   | "none" }, |   |   |
|   |   |   |   |   | "inputType": "file", |   |   |
|   |   |   |   |   | "lastModifyTime": |   |   |
|   |   |   |   |   | 1574843554, |   |   |
|   |   |   |   |   | "logSample": "2019- |   |   |
|   |   |   |   |   | 11-27 |   |   |
|   |   |   |   |   | 10:48:23,160,,,MAIN, |   |   |
|   |   |   |   |   | ,,INFO,,,98DCC51D- |   |   |
|   |   |   |   |   | BE5D-49C7-B3FD- |   |   |
|   |   |   |   |   | 37B2BAEFB296,,,12345 |   |   |
|   |   |   |   |   | 6789,,,cn- |   |   |
|   |   |   |   |   | hangzhou,,,this is a |   |   |
|   |   |   |   |   | simple test.", |   |   |
|   |   |   |   |   | "outputDetail": { |   |   |
|   |   |   |   |   | "endpoint": "cn- |   |   |
|   |   |   |   |   | hangzhou- |   |   |
|   |   |   |   |   | intranet.log.aliyunc |   |   |
|   |   |   |   |   | s.com", |   |   |
|   |   |   |   |   | "logstoreName": |   |   |
|   |   |   |   |   | "test-logstore", |   |   |
|   |   |   |   |   | "region": "cn- |   |   |
|   |   |   |   |   | hangzhou"}, |   |   |
|   |   |   |   |   | "outputType": |   |   |
|   |   |   |   |   | "LogService"} | . |   |
| CloneFrom | Map | No | Yes | The configurations for cloning LogtailConfig data of another Log Service project. | You must specify one of the CloneFrom and LogtailConfig parameters. For more information, see CloneFrom properties. |   |   |

CloneFrom syntax

```json
"CloneFrom": {
  "ProjectName": String,
  "LogtailConfigName": String
```

CloneFrom properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ProjectName | String | Yes | Yes | The name of the Log Service project. | None |
| LogtailConfi gName | String | Yes | Yes | The name of the Logtail configuratio n file. | None |

Response parameters Fn::GetAtt Endpoint: the endpoint. AppliedMachineGroups: a list of machines configured for log collection. LogtailConfigName: the name of the Logtail configuration file. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "LogtailConfig": {
      "Type": "ALIYUN::SLS::LogtailConfig",
      "Properties": {
        "ProjectName": {
          "Ref": "ProjectName"
        "LogtailConfigName": {
          "Ref": "LogtailConfigName"
        "LogstoreName": {
          "Ref": "LogstoreName"
        "RawConfigData": {
          "Ref": "RawConfigData"
        "CloneFrom": {
          "Ref": "CloneFrom"
  "Parameters": {
"ProjectName":{
```

```json
    "ProjectName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Project name: 1. Only supports lowercase letters, numbers, hyphens (-) and
underscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 characters.",
      "MaxLength": 63
    "LogtailConfigName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logtail config name: 1. Only supports lowercase letters, numbers, hyphens (
-) and underscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name len gth is 3-63 characters.",
      "MaxLength": 63
    "LogstoreName": {
      "MinLength": 3,
      "Type": "String",
      "Description": "Logstore name: 1. Only supports lowercase letters, numbers, hyphens (-) and
underscores (_). 2. Must start and end with lowercase letters and numbers. 3. The name length is 3-63 characters.",
      "MaxLength": 63
    "RawConfigData": {
      "Type": "Json",
      "Description": "The format is the same as the response of SLS API GetConfig. Either CloneFr
om or RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail config data will be merged from both with RawConfigData first. configName, outputType, outputDeta il in data will be ignored.For example:\n{\"configName\": \"test-logtail-config\",\"createTime\": 1574843554,\"inputDetail\": { \"acceptNoEnoughKeys\": false, \"adjustTimezone\": false, \"advance d\": { \"force_multiconfig\": false }, \"autoExtend\": true, \"delayAlarmBytes\": 0, \"delaySki pBytes\": 0, \"discardNonUtf8\": false, \"discardUnmatch\": false, \"dockerExcludeEnv\": {}, \"do ckerExcludeLabel\": {}, \"dockerFile\": false, \"dockerIncludeEnv\": {}, \"dockerIncludeLabel\": {}, \"enableRawLog\": false, \"enableTag\": false, \"fileEncoding\": \"utf8\", \"filePattern\": \ "test.log*\", \"filterKey\": [], \"filterRegex\": [], \"key\": [ \"time\", \"logger\", \"le vel\", \"request_id\", \"user_id\", \"region_id\", \"content\" ], \"localStorage\": true, \"logPath\": \"/var/log/test\", \"logTimezone\": \"\", \"logType\": \"delimiter_log\", \"maxDepth \": 100, \"maxSendRate\": -1, \"mergeType\": \"topic\", \"preserve\": true, \"preserveDepth\": 1, \"priority\": 0, \"quote\": \"\\u0001\", \"sendRateExpire\": 0, \"sensitive_keys\": [], \"separat or\": \",,,\", \"shardHashKey\": [], \"tailExisted\": false, \"timeFormat\": \"\", \"timeKey\": \ "\", \"topicFormat\": \"none\"}, \"inputType\": \"file\", \"lastModifyTime\": 1574843554, \"logSa mple\": \"2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B3FD-37B2BAEFB296,,,12345678 9,,,cn-hangzhou,,,this is a simple test.\", \"outputDetail\": {\"endpoint\": \"cn-hangzhou-intran et.log.aliyuncs.com\", \"logstoreName\": \"test-logstore\",\"region\": \"cn-hangzhou\"}, \"output Type\": \"LogService\"}"
    "CloneFrom": {
      "Type": "Json",
      "Description": "Clone logtail config data from existing logtail config. Either CloneFrom or
RawConfigData must be specified. If CloneFrom and RawConfigData are both specified, logtail confi g data will be merged from both with RawConfigData first."
  "Outputs": {
    "LogtailConfigName": {
      "Description": "Logtail config name.",
      "Value": {
```

```
        "Fn::GetAtt": [
          "LogtailConfig",
          "LogtailConfigName"
```

`]`

```json
    "Endpoint": {
      "Description": "Endpoint address.",
      "Value": {
        "Fn::GetAtt": [
          "LogtailConfig",
          "Endpoint"
```

`]`

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
    Description: 'Project name: 1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_). 2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
  LogtailConfigName:
    MinLength: 3
    Type: String
    Description: 'Logtail config name: 1. Only supports lowercase letters, numbers,
hyphens()andunderscores() Muststartandendwithlowercaseletters
```

```json
      hyphens (-) and underscores (_). 2. Must start and end with lowercase letters
      and numbers. 3. The name length is 3-63 characters.'
    MaxLength: 63
  LogstoreName:
    MinLength: 3
    Type: String
    Description: 'Logstore name: 1. Only supports lowercase letters, numbers, hyphens
      (-) and underscores (_). 2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.'
    MaxLength: 63
  RawConfigData:
    Type: Json
    Description: |-
      The format is the same as the response of SLS API GetConfig. Either CloneFrom or RawConfigD
ata must be specified. If CloneFrom and RawConfigData are both specified, logtail config data wil l be merged from both with RawConfigData first. configName, outputType, outputDetail in data will be ignored.For example:
      {"configName": "test-logtail-config","createTime": 1574843554,"inputDetail": { "acceptNoEno
ughKeys": false, "adjustTimezone": false, "advanced": { "force_multiconfig": false }, "autoExte nd": true, "delayAlarmBytes": 0, "delaySkipBytes": 0, "discardNonUtf8": false, "discardUnmatch": false, "dockerExcludeEnv": {}, "dockerExcludeLabel": {}, "dockerFile": false, "dockerIncludeEnv": {}, "dockerIncludeLabel": {}, "enableRawLog": false, "enableTag": false, "fileEncoding": "utf8", "filePattern": "test.log*", "filterKey": [], "filterRegex": [], "key": [ "time", "logger", "level", "request_id", "user_id", "region_id", "content" ], "localStorage": true, "logPat h": "/var/log/test", "logTimezone": "", "logType": "delimiter_log", "maxDepth": 100, "maxSendRate ": -1, "mergeType": "topic", "preserve": true, "preserveDepth": 1, "priority": 0, "quote": "\u000 1", "sendRateExpire": 0, "sensitive_keys": [], "separator": ",,,", "shardHashKey": [], "tailExist ed": false, "timeFormat": "", "timeKey": "", "topicFormat": "none"}, "inputType": "file", "lastMo difyTime": 1574843554, "logSample": "2019-11-27 10:48:23,160,,,MAIN,,,INFO,,,98DCC51D-BE5D-49C7-B 3FD-37B2BAEFB296,,,123456789,,,cn-hangzhou,,,this is a simple test.", "outputDetail": {"endpoint" : "cn-hangzhou-intranet.log.aliyuncs.com", "logstoreName": "test-logstore","region": "cn-hangzhou "}, "outputType": "LogService"}
  CloneFrom:
    Type: Json
    Description: Clone logtail config data from existing logtail config. Either CloneFrom
      or RawConfigData must be specified. If CloneFrom and RawConfigData are both
      specified, logtail config data will be merged from both with RawConfigData first.
Outputs:
  Endpoint:
    Description: Endpoint address.
    Value:
      Fn::GetAtt:
      - LogtailConfig
      - Endpoint
  AppliedMachineGroups:
    Description: Applied machine groups.
    Value:
      Fn::GetAtt:
      - LogtailConfig
      - AppliedMachineGroups
  LogtailConfigName:
    Description: Logtail config name.
    Value:
      Fn::GetAtt:
      - LogtailConfig
      - LogtailConfigName
```

To view more examples, visit SLS.json and SLS.yml. In the examples, the ALIYUN::SLS::Project, ALIYUN::SLS::Logstore, ALIYUN::SLS::Index, ALIYUN::SLS::LogtailConfig, ALIYUN::SLS::MachineGroup, ALIYUN::SLS::ApplyConfigToMachineGroup, ALIYUN::ApiGateway::LogConfig, ALIYUN::SLS::Savedsearch, and ALIYUN::SLS::Alert resource types are involved.

#### 6.8.4 ALIYUN::SLS::Savedsearch

ALIYUN::SLS::Savedsearch is used to save search results as a saved search. Syntax

```json
  "Type": "ALIYUN::SLS::Savedsearch",
  "Properties": {
    "Project": String,
    "Detail": Map
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Project | String | Yes | No | The name of the Log Service project. | None |
| Detail | Map | Yes | Yes | The details of the query. | For more information, see Detail properties. |

Detail syntax

```json
"Detail": {
  "SearchQuery": String,
  "Logstore": String,
  "DisplayName": String,
  "SavedsearchName": String,
  "Topic": String
```

Detail properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SearchQuery | String | Yes | Yes | The query statement. | None |
| Logstore | String | Yes | Yes | The Logstore in which the query is performed. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DisplayName | String | No | Yes | The display name that you specify for the saved search. | The name must be 1 to 63 characters in length. |
| SavedsearchNa me | String | Yes | No | The name of the saved search, which is generated by the system in the project. | None |
| Topic | String | Yes | Yes | The log topic that is used to classify logs. | None |

Response parameters Fn::GetAtt SavedsearchName: the name of the saved search. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Project": {
      "Type": "String",
      "Description": "Project name"
    "Detail": {
      "Type": "Json",
      "Description": ""
  "Resources": {
    "SavedSearch": {
      "Type": "ALIYUN::SLS::Savedsearch",
      "Properties": {
        "Project": {
          "Ref": "Project"
        "Detail": {
          "Ref": "Detail"
  "Outputs": {
    "SavedsearchName": {
      "Description": "Savedsearch name.",
      "Value": {
        "Fn::GetAtt": [
          "SavedSearch",
          "SavedsearchName"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Project:
    Type: String
    Description: Project name
  Detail:
    Type: Json
    Description: ''
Resources:
  SavedSearch:
    Type: 'ALIYUN::SLS::Savedsearch'
    Properties:
      Project:
        Ref: Project
      Detail:
        Ref: Detail
Outputs:
  SavedsearchName:
    Description: Savedsearch name.
    Value:
      'Fn::GetAtt':
        - SavedSearch
        - SavedsearchName
```

#### 6.8.5 ALIYUN::SLS::Project

ALIYUN::SLS::Project is used to create a Log Service project. Syntax

```json
  "Type": "ALIYUN::SLS::Project",
  "Properties": {
    "Name": String,
    "Description": String,
    "Tags": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Name | String | Yes | No | The name of the project. | The name must be 3 to 36 characters in length, and can contain lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | No | No | The description of the project. | The description can be up to 64 characters in length, and cannot contain the following special characters: <> ' \ " |
| Tags | List | No | Yes | The tags of the project. | You can specify up to 20 tags. For more information, see Tags syntax and Tags properties. |

|   | " |
|---|---|

Tags syntax

```json
"Tags": [
    "Key": String,
    "Value": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | The key of the tag. | The key must be 1 to 128 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
| Value | String | No | No | The value of the tag. | The value must be 0 to 128 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

Response parameters Fn::GetAtt Name: the name of the Log Service project. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Project description: <>'\"\\ is not supported, up to 64 characters.",
      "MaxLength": 64
    "Tags": {
      "Type": "Json",
      "Description": "Tags to attach to project. Max support 20 tags to add during create project
. Each tag with two properties Key and Value, and Key is required.",
      "MaxLength": 20
    "Name": {
      "Type": "String",
      "Description": "Project name:\n1. Only supports lowercase letters, numbers, hyphens (-) and
underscores (_).\n2. Must start and end with lowercase letters and numbers.\n3. The name length i s 3-63 characters.",
      "AllowedPattern": "^[a-zA-Z0-9_-]+$",
      "MinLength": 3,
      "MaxLength": 63
  "Resources": {
    "Project": {
      "Type": "ALIYUN::SLS::Project",
      "Properties": {
        "Description": {
          "Ref": "Description"
        "Tags": {
          "Ref": "Tags"
        "Name": {
          "Ref": "Name"
  "Outputs": {
    "Name": {
      "Description": "Project name.",
      "Value": {
        "Fn::GetAtt": [
          "Project",
          "Name"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  Description:
    Type: String
    Description: 'Project description: <>''"\ is not supported, up to 64 characters.'
    MaxLength: 64
  Tags:
    Type: Json
    Description: >-
      Tags to attach to project. Max support 20 tags to add during create
      project. Each tag with two properties Key and Value, and Key is required.
    MaxLength: 20
  Name:
    Type: String
    Description: >-
      Project name:
      1. Only supports lowercase letters, numbers, hyphens (-) and underscores
      (_).
      2. Must start and end with lowercase letters and numbers.
      3. The name length is 3-63 characters.
    AllowedPattern: '^[a-zA-Z0-9_-]+$'
    MinLength: 3
    MaxLength: 63
Resources:
  Project:
    Type: 'ALIYUN::SLS::Project'
    Properties:
      Description:
        Ref: Description
      Tags:
        Ref: Tags
      Name:
        Ref: Name
Outputs:
  Name:
    Description: Project name.
    Value:
      'Fn::GetAtt':
        - Project
        - Name
```

For more information about examples, visit SLS.json and SLS.yml. You can specify the following resource types that are involved in the examples to use relevant features: ALIYUN::SLS::MachineGroup ALIYUN::SLS::ApplyConfigToMachineGroup ALIYUN::ApiGateway::LogConfig ALIYUN::SLS::Alert

### 6.9 VPC

#### 6.9.1 ALIYUN::VPC::EIP

ALIYUN::VPC::EIP is used to apply for an Elastic IP address. Statement

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

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the RDS instance belongs. | None |
| Bandwidth | Number | Erased | Released | The network bandwidth. Unit: Mbit/s. | If this parameter is not specified, the default value 5Mbps is used. |
| InternetCharge Type | String | Yes | Released | The billing method for network usage. Default value: PayByBandwidt h. | Valid values: PayByBandwidth: pay-by- bandwidth. PayByTraffic Default value: PayByBandwidth. |
| InstanceCharge Type | String | Yes | Released | The billing method of the Elastic IP address. Default value: Postpaid. | Valid values: Prepaid Postpaid: pay-as-you-go Default value: PostPaid. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PricingCycle | String | Yes | Released | The billing cycle of the subscription. Default value: Month. | Valid values: Month: paid by month. Year Default value: Month. Not e This parameter is required when InstanceChargeType is set to Prepaid. |
| Period | Number | Erased | Released | The subscription period. | Valid values: If pay by month is selected, the billing method can be a fee of 1 to 9. If pay-as-you-go is selected, the payment can be in the range of 1 to 3. Default value: 1 Not e This parameter is required when InstanceChargeType is set to Prepaid. |
| AutoPay | Boolean | Erased | Released | Specifies whether to enable automatic payment. | Valid values: false: Automatic payment is disabled. After an order is generated, you must go to the Order Center to make the payment. true: Automatic payment is enabled. Payments are automatically made. Not e This parameter is required when InstanceChargeType is set to Prepaid. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Isp | String | Yes | Released | The ISP tag used for Finance Cloud. This parameter takes effect only when your region is set to China (Hangzhou). | This parameter is ignored if you are not a Finance Cloud user. |

Response parameters Fn::GetAtt EipAddress: the allocated Elastic IP address. AllocationId: the ID of the instance that the Elastic IP address is allocated to. OrderId: The order ID that is returned when you set the InstanceChargeType parameter to Prepaid. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Eip": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "InternetChargeType": "PayByTraffic",
          "Bandwidth": 200
  "Outputs": {
    "EipAddress": {
      "Value" : {"Fn::GetAtt": ["Eip", "EipAddress"]}
    "AllocationId": {
      "Value" : {"Fn::GetAtt": ["Eip", "AllocationId"]}
    "OrderId": {
      "Value" : {"Fn::GetAtt": ["Eip", "OrderId"]}
```

#### 6.9.2 ALIYUN::VPC::EIPAssociation

ALIYUN::VPC::EIPAssociation is used to associate an elastic IP address (EIP) with a cloud service instance. Syntax

```json
  "Type": "ALIYUN::VPC::EIPAssociation",
  "Properties": {
    "AllocationId": String,
    "InstanceId": String,
    "PrivateIpAddress": String,
    "Mode": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllocationId | String | Yes | Yes | The ID of the EIP. | None |
| InstanceId | String | Yes | Yes | The ID of the cloud service instance. | The following types of instances are supported: Elastic Compute Service (ECS) instances of the virtual private cloud (VPC) type Server Load Balancer (SLB) instances of the VPC type NAT gateways High-availability virtual IP addresses (HAVIPs) Elastic network interfaces (ENIs) |
| PrivateIpAdd ress | String | No | Yes | The private IP address in the CIDR block of the vSwitch. | If you do not set this property, the system allocates a private IP address based on the VPC ID and vSwitch ID. |
| Mode | String | No | Yes | The association mode. | Defaut value: NAT. Valid values: NAT: the standard NAT gateway mode MULTI BINDED: the multi- _ EIP-to-ENI mode BINDED: the cut-through mode |

Return values Fn::GetAtt EipAddress: the EIP. AllocationId: the ID of the EIP. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": {
    "en": "Create a VPC type ECS and bind EIP (existing VPC).",
  "Parameters": {
    "VPC": {
      "AssociationProperty": "ALIYUN::ECS::VPC::VPCId",
      "Type": "String",
      "Description": {
        "en": "Please search the ID starting with (vpc-xxx) from console-Virtual Private Cloud.",
      "Label": {
        "en": "VPC ID",
    "VSwitch": {
      "AssociationProperty": "ALIYUN::ECS::VSwitch::VSwitchId",
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
      "Type": "String",
      "Description": {
        "en": "Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch mu
st be under VPC. ECS will be created under this VSwitch.</font>",
          </font>"
      "Label": {
        "en": "VSwitch ID",
    "SecurityGroup": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::SecurityGroup::SecurityGroupId",
      "Description": {
        "en": "Please search the business security group ID starting with (sg-xxx) from console-E
CS-Network & Security.",
          </font>"
      "Label": {
        "en": "Business Security Group ID",
      "AssociationPropertyMetadata": {
        "VpcId": "VPC"
    "ECSPassword": {
      "NoEcho": true,
      "Type": "String",
      "Description": {
        "en": "Server login password, Length 8-30, must contain three (Capital letters, lowercase
letters, numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
      "AllowedPattern": "[0-9A-Za-z\\_\\-\\&:;'<>,=%`~!@#\\(\\)\\$\\^\\*\\+\\|\\{\\}\\[\\]\\.\\?\
\/]+$", "Lbl"
```

```json
      "Label": {
        "en": "Instance Password",
      "MinLength": 8,
      "ConstraintDescription": {
        "en": "Length 8-30, must contain three(Capital letters, lowercase letters, numbers, ()`~!
@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).",
      "MaxLength": 30,
      "Default": null
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
      "Label": {
        "en": "EIP Charge Type",
      "Default": "PayByTraffic"
    "ECSImageId": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::Instance::ImageId",
      "Description": {
        "en": "Image ID,Please use Centos7.",
      "Label": {
        "en": "Image",
      "Default": "ubuntu_14"
    "ECSZoneId": {
      "AssociationProperty": "ALIYUN::ECS::Instance:ZoneId",
      "Type": "String",
      "Description": {
        "en": "Availability zone ID.<br><b>Note: <font color='blue'>Before selecting, please conf
irm whether the availability zone supports the specification of creating ECS resources. It is rec ommended to be different from other switch availability zones</font></b ><br><font color='red'>Th e switch availability zone and the selected switch instance ID must be in the same availability z one.</font>",
          </font>"
      "Label": {
        "en": "VSwitch Availability Zone",
    "EIPBandwidth": {
      "Type": "Number",
      "Description": {
        "en": "EIP Bandwidth, Value range: [1,200], unit: Mbps.",
      "MinValue": 1,
"Label":{
```

```json
      Label: {
        "en": "EIP Bandwidth",
      "MaxValue": 200,
      "Default": 1
    "ECSInstanceType": {
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceChargeType": "InstanceChargeType"
      "AssociationProperty": "ALIYUN::ECS::Instance::InstanceType",
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>1.Before selecting the model please confirm that the current
available zone under the model is in stock, some models need to be reported in advance</b></font> <br><font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font colo r='green'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</ font>]<br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1.5Gbps In-grid sen ding and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color='green'>8vCPU 16GiB Intranet bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]",
            </font>]"
      "Label": {
        "en": "Instance Type",
    "ECSDiskCategory": {
      "Type": "String",
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[cloud_efficiency: <font colo
r='green'>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color='green'>SSD Cloud Disk</font>]< br>[cloud_essd: <font color='green'>ESSD Cloud Disk</font>]<br>[cloud: <font color='green'>Cloud Disk</font>]<br>[ephemeral_ssd: <font color='green'>Local SSD Cloud Disk</font>]",
      "AssociationProperty": "ALIYUN::ECS::Disk::SystemDiskCategory",
      "AssociationPropertyMetadata": {
        "ZoneId": "ECSZoneId",
        "InstanceType": "ECSInstanceType"
      "Label": {
        "en": "System Disk Type",
    "ECSSysDiskSize": {
      "Type": "Number",
      "Description": {
        "en": "System disk size, range of values: 40-500, units: GB.",
      "MinValue": 40,
      "Label": {
        "en": "System Disk Space",
      "MaxValue": 500,
      "Default": 40
    "InstanceChargeType": {
      "Type": "String",
```

```json
      "Label": {
        "en": "Instance Charge Type",
      "Description": {
        "en": "<font color='blue'><b>Optional values:</b></font><br>[PostPaid: <font color='green
'>Pay as you go.</font>]<br> [PrePaid: <font color='green'>Prepaid, monthly subscription.</font>]
```

`",`

```json
          </font>]"
      "AllowedValues": [
        "PostPaid",
        "PrePaid"
```

`],`

```json
      "Default": "PostPaid"
    "KeyPairName": {
      "Type": "String",
      "AssociationProperty": "ALIYUN::ECS::KeyPair::KeyPairName",
      "Label": {
        "en": "Key Pair Name",
      "Description": {
        "en": "If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>I
f you have filled in <font color='green'>key pair name</font>, <font color='green'>instance passw ord< The content of /font> will still be set in the instance, but the password login method in th e Linux system will be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If you use the instance password Login, the key pair name does not need to be filled in.</f ont>",
             </font>"
      "Default": null
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
          "Parameters": [
            "EIPBandwidth",
            "EIPInternetChargeType"
```

`],`

```json
          "Label": {
            "default": "EIP"
          "Parameters": [
```

```
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

`]`

```json
  "Resources": {
    "ECSInstanceGroup": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Properties": {
        "IoOptimized": "optimized",
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        "ZoneId": {
          "Ref": "ECSZoneId"
        "SystemDisk_Category": {
          "Ref": "ECSDiskCategory"
        "SecurityGroupId": {
          "Ref": "SecurityGroup"
        "VSwitchId": {
          "Ref": "VSwitch"
        "MaxAmount": 1,
        "SystemDisk_Size": {
          "Ref": "ECSSysDiskSize"
        "VpcId": {
          "Ref": "VPC"
        "ImageId": {
          "Ref": "ECSImageId"
        "InstanceType": {
          "Ref": "ECSInstanceType"
        "AllocatePublicIP": "false",
        "Password": {
          "Ref": "ECSPassword"
        "KeyPairName": {
"Ref":"KeyPairName"
```

```json
          "Ref": "KeyPairName"
    "ElasticIp": {
      "Type": "ALIYUN::VPC::EIP",
      "Properties": {
        "Bandwidth": {
          "Ref": "EIPBandwidth"
        "InternetChargeType": {
          "Ref": "EIPInternetChargeType"
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

`]` `]`

```json
        "AllocationId": {
          "Ref": "ElasticIp"
  "Outputs": {
    "VpcId": {
      "Description": "VPC Id",
      "Value": {
        "Ref": "VPC"
    "SecurityGroupId": {
      "Description": "Security Group Id",
      "Value": {
        "Ref": "SecurityGroup"
    "VSwitchId": {
      "Description": "VSwitch Id",
      "Value": {
        "Ref": "VSwitch"
    "EipAddress": {
      "Description": "IP address of created EIP.",
      "Value": {
        "Fn::GetAtt": [
```

`[`

```
          "ElasticIp",
          "EipAddress"
```

`]` `YAML` format

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
      en: Existing VSwitch ID, query under console-VPC-VSwitch, <font color='red'>VSwitch must be
under VPC. ECS will be created under this VSwitch.</font>
        </font>
    Label:
      en: VSwitch ID
  SecurityGroup:
    Type: String
    AssociationProperty: ALIYUN::ECS::SecurityGroup::SecurityGroupId
    Description:
      en: Please search the business security group ID starting with (sg-xxx) from console-ECS-Ne
twork & Security.
        </font>
    Label:
      en: Business Security Group ID
    AssociationPropertyMetadata:
      VpcId: VPC
  ECSPassword:
    NoEcho: true
    Type: String
    Description:
      en: Server login password, Length 8-30, must contain three (Capital letters, lowercase lett
ers, numbers, ()`~!@#$%^&*_-+=|{}[]:;'<>,.?/ Special symbol in).
    AllowedPattern: '[0-9A-Za-z\_\-\&:;''<>,=%`~!@#\(\)\$\^\*\+\|\{\}\[\]\.\?\/]+$'
    Label:
      en: Instance Password
    MinLength: 8
    ConstraintDescription:
      en: Length 8-30, must contain three (Capital letters, lowercase letters, numbers, ()`~!@#$%
^&*_-+=|{}[]:;'<>,.?/ Special symbol in). MaxLength:30
```

```
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
      en: 'Availability zone ID.<br><b>Note: <font color=''blue''>Before selecting, please confir
m whether the availability zone supports the specification of creating ECS resources. It is recom mended to be different from other switch availability zones</font></b ><br><font color=''red''>Th e switch availability zone and the selected switch instance ID must be in the same availability z one.</font>'
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
    Default: 1
  ECSInstanceType:
    AssociationPropertyMetadata:
      ZoneId: ECSZoneId
      InstanceChargeType: InstanceChargeType
    AssociationProperty: ALIYUN::ECS::Instance::InstanceType
    Type: String
    Description:
      en: <font color='blue'><b>1.Before selecting the model please confirm that the current avai
lable zone under the model is in stock, some models need to be reported in advance</b></font><br> <font color='blue'><b>2.List of optional models</font><br></b></font>[ecs.c5.large <font color='g reen'>2vCPU 4GiB Intranet bandwidth1Gbps In-grid sending and receiving packages30MillionPPS</font >]<br></b>[ecs.c5.xlarge <font color='green'>4vCPU 8GiB Intranet bandwidth1.5Gbps In-grid sending and receiving packages50MillionPPS</font>]<br></b>[ecs.c5.2xlarge <font color='green'>8vCPU 16GiB Intranet bandwidth2.5Gbps In-grid sending and receiving packages80MillionPPS</font>]
          </font>]
    Label:
      en: Instance Type
```

`yp`

```
  ECSDiskCategory:
    Type: String
    Description:
      en: '<font color=''blue''><b>Optional values:</b></font><br>[cloud_efficiency: <font color=
''green''>Efficient Cloud Disk</font>]<br>[cloud_ssd: <font color=''green''>SSD Cloud Disk</font> ]<br>[cloud_essd: <font color=''green''>ESSD Cloud Disk</font>]<br>[cloud: <font color=''green''> Cloud Disk</font>]<br>[ephemeral_ssd: <font color=''green''>Local SSD Cloud Disk</font>]'
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
      en: '<font color=''blue''><b>Optional values:</b></font><br>[PostPaid: <font color=''green'
'>Pay as you go.</font>]<br> [PrePaid: <font color=''green''>Prepaid, monthly subscription.</font >]'
        </font>]'
    AllowedValues:
      - PostPaid
      - PrePaid
    Default: PostPaid
  KeyPairName:
    Type: String
    AssociationProperty: ALIYUN::ECS::KeyPair::KeyPairName
    Label:
      en: Key Pair Name
    Description:
      en: If it is a Windows ECS instance, ignore this parameter. The default is blank.<br>If you
have filled in <font color='green'>key pair name</font>, <font color='green'>instance password< T he content of /font> will still be set in the instance, but the password login method in the Linu x system will be forbidden.<br><font color='red'>Please enter the name of the existing key pair. If you use the instance password Login, the key pair name does not need to be filled in.</font>
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
```

```
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
```

`d`

```
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

#### 6.9.3 ALIYUN::VPC::PeeringRouterInterfaceBinding

ALIYUN::VPC::PeeringRouterInterfaceBinding is used to associate two router interfaces to be interconnected. Statement

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
  "Properties": {
    "OppositeRouterId": String,
    "OppositeInterfaceId": String,
    "OppositeInterfaceOwnerId": String,
    "RouterInterfaceId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RouterInterfaceI d | String | No | No | The ID of the router interface. | None |
| OppositeInterfa ceId | String | No | No | The ID of the peer router interface. | None |

| esource Orchestr | ation Service |   |   | User Gui | de·Resource type |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | Description | Constraint |
| OppositeRouter Id | String | Yes | Released | The ID of the router to which the peer router interface belongs. | None |
| OppositeInterfa ceOwnerId | String | Yes | Released | The ID of the owner of the peer router interface. | None |

Response parameters Fn::GetAtt RouterInterfaceId: the ID of the vRouter. Sample request

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

#### 6.9.4 ALIYUN::VPC::PeeringRouterInterfaceConnection

ALIYUN::VPC::PeeringRouterInterfaceConnection is used to initiate a router interface connection. Statement

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
  "Properties": {
    "OppositeInterfaceId": String,
    "RouterInterfaceId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| OppositeInterfa ceId | String | No | No | The ID of the acceptor router interface. | None |
| RouterInterfaceI d | String | No | No | The ID of the router interface to initiate the connection. | None |

Response parameters Fn::GetAtt OppositeInterfaceId: the ID of the acceptor router interface. RouterInterfaceId: the ID of the router interface that initiates the connection. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
      "Properties": {
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2ze4k5n2aeardu8cy****"
```

#### 6.9.5 ALIYUN::VPC::RouterInterface

ALIYUN::VPC::RouterInterface is used to create a router interface. Syntax

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

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RouterId | String | Yes | No | The ID of the router to which the router interface belongs. | None |
| Role | String | Yes | No | The role of the router interface. A router interface can either be a connection initiator or a connection acceptor. | Valid values: InitiatingSide This parameter must be set to InitiatingSide when the RouterType parameter is set to VBR. AcceptingSide This parameter must be set to AcceptingSide when the OppositeRouterTy pe parameter is set to VBR. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RouterType | String | No | No | The type of the router to which the router interface belongs. | Valid values: VRouter: VPC router VBR: virtual border router |
| AccessPointI d | String | No | No | The ID of the access point of the router interface. | This parameter is required when the RouterType parameter is set to VBR. The access point ID cannot be modified after the router interface is created. This parameter cannot be set when the RouterType parameter is set to VRouter. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Spec | String | No | No | The specifications of the router interface. | The following list includes available specifications and the corresponding bandwidth values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s This parameter is required when the Role parameter is set to InitiatingSide. The value Negative is used by default when the Role parameter is set to AcceptingSide. |
| OppositeReg ionId | String | No | No | The region ID of the peer router interface. | None |
| OppositeInte rfaceOwnerI d | String | No | Yes | The ID of the owner of the peer router interface. | The default value is the ID of the current user. |
| OppositeInte rfaceId | String | No | Yes | The ID of the peer router interface. | None |
| OppositeRou terId | String | No | Yes | The ID of the router to which the peer router interface belongs. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| OppositeRou terType | String | No | Yes | The type of the router to which the peer router interface belongs. | Valid values: VRouter: VPC router This parameter must be set to VRouter when the RouterType parameter is set to VBR. VBR: virtual border router |
| OppositeAcc essPointId | String | No | No | The ID of the access point of the peer router interface. | This parameter is required when the OppositeRouterType parameter is set to VBR. The access point ID cannot be modified after the router interface is created. This parameter cannot be set when the OppositeRouterType parameter is set to VRouter. Not e When the OppositeRouterT ype parameter is set to VBR, the VBR specified by the OppositeRouterI d parameter must be in the access point specified by the OppositeAccessP ointId parameter. |
| Description | String | No | Yes | The description of the router interface. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . This parameter is empty by default. |

| esource Orches | tration Service |   |   | Us | er Guide·Resource type |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |

| Name | String | No | Yes | The display name of the router interface. | The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |
|---|---|---|---|---|---|
| HealthCheck SourceIp | String | No | No | The source IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces that have a peer router interface on a VBR. It must be an unused IP address in the VPC where the local VRouter is located. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both unspecified. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HealthCheck TargetIp | String | No | No | The destination IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces that have a peer router interface on a VBR. Typically, you can use the IP address of a customer premises equipment (CPE) on the user side of the leased line, which is the IP address of the peer gateway on the VBR where the peer router interface is located. You can also specify another IP address on the user side of the leased line as the destination IP address. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both unspecified. |
| PricingCycle | String | No | No | The billing cycle of the subscription. | Valid values: Month Year |
| Period | Number | No | No | The subscription period. | Valid values: Valid values when the PricingCycle parameter is set to Month: 1 to 9. Valid values when the PricingCycle parameter is set to Year: 1 to 3. |
| AutoPay | Boolean | No | No | Specifies whether to enable automatic payment. | Default value: false. Valid values: true false |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceChar geType | String | No | No | The billing method of the router interface. | Valid values: Postpaid: pay-as- you-go Prepaid: subscription |

Response parameters Fn::GetAtt RouterInterfaceId: the ID of the router interface. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "OppositeInterfaceId": {
      "Type": "String",
      "Description": "The ID of the peer router interface."
    "OppositeInterfaceOwnerId": {
      "Type": "String",
      "Description": "Owner account ID of the connection peer RouterInterface. The default value
is current user Id."
    "Description": {
      "Type": "String",
      "Description": "Custom description of the RouterInterface, [2, 256] characters. Don't fill
or empty, the default is empty."
    "OppositeRouterId": {
      "Type": "String",
      "Description": "The router ID of the connection peer RouterInterface."
    "OppositeRegionId": {
      "Type": "String",
      "Description": "The region where the connection peer RouterInterface locates. The default v
alue is region where stack is created."
    "PricingCycle": {
      "Type": "String",
      "Description": "Unit of the payment cycle. It could be Month (default) or Year.",
      "AllowedValues": [
        "Month",
        "Year"
```

`]`

```json
    "InstanceChargeType": {
      "Type": "String",
      "Description": "The billing method of the router interface. Valid values: PrePaid (Subscrip
tion), PostPaid (default, Pay-As-You-Go)",
      "AllowedValues": [
```

```
        "PrePaid",
        "PostPaid"
```

`],`

```json
      "Default": "PostPaid"
    "HealthCheckSourceIp": {
      "Type": "String",
      "Description": "Source IP address of the packet for leased line HealthCheck in leased line
disaster tolerance and ECMP scenarios. It is valid only for a VRouter RouterInterface with a peer on a VBR. The source IP address must be in the VPC of the local VRouter and is not used. HealthCh eckSourceIp and HealthCheckTargetIp parameters must be both specified or left unspecified."
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. It could be from 1 to 9 when PricingCycle is Month, or
1 to 3 when PricingCycle is Year. Default value is 3.",
      "AllowedValues": [
```

`1,` `2,` `3,` `4,` `5,` `6,` `7,` `8,` `]`

```json
    "RouterId": {
      "Type": "String",
      "Description": "The router ID to create RouterInterface."
    "AutoPay": {
      "Type": "Boolean",
      "Description": "Indicates whether automatic payment is enabled. Valid values:false: Automat
ic payment is disabled. You need to go to Orders to make the payment once an order is generated. true: Automatic payment is enabled. The payment is automatically made.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]`

```json
    "Name": {
      "Type": "String",
      "Description": "Custom name of the RouterInterface, [2, 128] English or Chinese characters,
must start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
    "Role": {
      "Type": "String",
      "Description": "RouterInterface role. Now support 'InitiatingSide|AcceptingSide'. If 'Route
rType' is specified as 'VBR', the value must be 'InitiatingSide'.If 'OppositeRouterType' is speci fied as 'VBR', the value must be 'AcceptingSide'.",
      "AllowedValues": [
        "InitiatingSide",
        "AcceptingSide"
```

`]`

```json
    "OppositeRouterType": {
      "Type": "String",
      "Description": "Router type of the connection peer router. Now support 'VRouter|VBR'. If 'R
outerType' is specified as 'VBR', the value must be 'VRouter'.",
      "AllowedValues": [
        "VRouter",
        "VBR"
```

`],`

```json
      "Default": "VRouter"
    "RouterType": {
      "Type": "String",
      "Description": "Router type. Now support 'VRouter|VBR'",
      "AllowedValues": [
        "VRouter",
        "VBR"
```

`],`

```json
      "Default": "VRouter"
    "AccessPointId": {
      "Type": "String",
      "Description": "Access point ID. If 'RouterType' is specified as 'VBR', the value is requir
ed."
    "OppositeAccessPointId": {
      "Type": "String",
      "Description": "Access point ID of the connection peer RouterInterface. If 'OppositeRouterT
ype' is specified as 'VBR', the value is required."
    "Spec": {
      "Type": "String",
      "Description": "RouterInterface specification. If 'Role' is specified as 'InitiatingSide',
the value is required. If 'Role' is specified as 'AcceptingSide', the value is set as 'Negative' by default."
    "HealthCheckTargetIp": {
      "Type": "String",
      "Description": "Target IP address of the packet for leased line HealthCheck in leased line
disaster tolerance and ECMP scenarios. It is valid only for a VRouter RouterInterface with a peer on a VBR. Usually you can use the CPE IP address of the leased line user's client (that is, the P eerGatewayIP on the VBR of the peer RouterInterface), you can also specify another IP address of the leased line user's client as the HealthCheck target IP address. HealthCheckSourceIp and Healt hCheckTargetIp parameters must be both specified or left unspecified."
  "Resources": {
    "RouterInterface": {
      "Type": "ALIYUN::VPC::RouterInterface",
      "Properties": {
        "OppositeInterfaceId": {
          "Ref": "OppositeInterfaceId"
        "OppositeInterfaceOwnerId": {
          "Ref": "OppositeInterfaceOwnerId"
"Description":{
```

```json
        Description: {
          "Ref": "Description"
        "OppositeRouterId": {
          "Ref": "OppositeRouterId"
        "OppositeRegionId": {
          "Ref": "OppositeRegionId"
        "PricingCycle": {
          "Ref": "PricingCycle"
        "InstanceChargeType": {
          "Ref": "InstanceChargeType"
        "HealthCheckSourceIp": {
          "Ref": "HealthCheckSourceIp"
        "Period": {
          "Ref": "Period"
        "RouterId": {
          "Ref": "RouterId"
        "AutoPay": {
          "Ref": "AutoPay"
        "Name": {
          "Ref": "Name"
        "Role": {
          "Ref": "Role"
        "OppositeRouterType": {
          "Ref": "OppositeRouterType"
        "RouterType": {
          "Ref": "RouterType"
        "AccessPointId": {
          "Ref": "AccessPointId"
        "OppositeAccessPointId": {
          "Ref": "OppositeAccessPointId"
        "Spec": {
          "Ref": "Spec"
        "HealthCheckTargetIp": {
          "Ref": "HealthCheckTargetIp"
  "Outputs": {
    "RouterInterfaceId": {
      "Description": "The ID of created RouterInterface.",
      "Value": {
```

```
        "Fn::GetAtt": [
          "RouterInterface",
          "RouterInterfaceId"
```

`]` `YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Parameters:
  OppositeInterfaceId:
    Type: String
    Description: The ID of the peer router interface.
  OppositeInterfaceOwnerId:
    Type: String
    Description: >-
      Owner account ID of the connection peer RouterInterface. The default value
      is current user Id.
  Description:
    Type: String
    Description: >-
      Custom description of the RouterInterface, [2, 256] characters. Don't fill
      or empty, the default is empty.
  OppositeRouterId:
    Type: String
    Description: The router ID of the connection peer RouterInterface.
  OppositeRegionId:
    Type: String
    Description: >-
      The region where the connection peer RouterInterface locates. The default
      value is region where stack is created.
  PricingCycle:
    Type: String
    Description: Unit of the payment cycle. It could be Month (default) or Year.
    AllowedValues:
      - Month
      - Year
  InstanceChargeType:
    Type: String
    Description: >-
      The billing method of the router interface. Valid values: PrePaid
      (Subscription), PostPaid (default, Pay-As-You-Go)
    AllowedValues:
      - PrePaid
      - PostPaid
    Default: PostPaid
  HealthCheckSourceIp:
    Type: String
    Description: >-
      Source IP address of the packet for leased line HealthCheck in leased line
      disaster tolerance and ECMP scenarios. It is valid only for a VRouter
      RouterInterface with a peer on a VBR. The source IP address must be in the
      VPC of the local VRouter and is not used. HealthCheckSourceIp and
HealthCheckTargetIpparametersmustbebothspecifiedorleftunspecified
```

```
      HealthCheckTargetIp parameters must be both specified or left unspecified.
  Period:
    Type: Number
    Description: >-
      Prepaid time period. It could be from 1 to 9 when PricingCycle is Month,
      or 1 to 3 when PricingCycle is Year. Default value is 3.
    AllowedValues:
  RouterId:
    Type: String
    Description: The router ID to create RouterInterface.
  AutoPay:
    Type: Boolean
    Description: >-
      Indicates whether automatic payment is enabled. Valid values:false:
      Automatic payment is disabled. You need to go to Orders to make the
      payment once an order is generated. true: Automatic payment is enabled.
      The payment is automatically made.
    AllowedValues:
      - 'True'
      - 'true'
      - 'False'
      - 'false'
  Name:
    Type: String
    Description: >-
      Custom name of the RouterInterface, [2, 128] English or Chinese
      characters, must start with a letter or Chinese in size, can contain
      numbers, '_' or '.', '-'
  Role:
    Type: String
    Description: >-
      RouterInterface role. Now support 'InitiatingSide|AcceptingSide'. If
      'RouterType' is specified as 'VBR', the value must be 'InitiatingSide'.If
      'OppositeRouterType' is specified as 'VBR', the value must be
      'AcceptingSide'.
    AllowedValues:
      - InitiatingSide
      - AcceptingSide
  OppositeRouterType:
    Type: String
    Description: >-
      Router type of the connection peer router. Now support 'VRouter|VBR'. If
      'RouterType' is specified as 'VBR', the value must be 'VRouter'.
    AllowedValues:
      - VRouter
      - VBR
    Default: VRouter
  RouterType:
    Type: String
```

`yp` `g`

```
    Description: Router type. Now support 'VRouter|VBR'
    AllowedValues:
      - VRouter
      - VBR
    Default: VRouter
  AccessPointId:
    Type: String
    Description: >-
      Access point ID. If 'RouterType' is specified as 'VBR', the value is
      required.
  OppositeAccessPointId:
    Type: String
    Description: >-
      Access point ID of the connection peer RouterInterface. If
      'OppositeRouterType' is specified as 'VBR', the value is required.
  Spec:
    Type: String
    Description: >-
      RouterInterface specification. If 'Role' is specified as 'InitiatingSide',
      the value is required. If 'Role' is specified as 'AcceptingSide', the
      value is set as 'Negative' by default.
  HealthCheckTargetIp:
    Type: String
    Description: >-
      Target IP address of the packet for leased line HealthCheck in leased line
      disaster tolerance and ECMP scenarios. It is valid only for a VRouter
      RouterInterface with a peer on a VBR. Usually you can use the CPE IP
      address of the leased line user's client (that is, the PeerGatewayIP on
      the VBR of the peer RouterInterface), you can also specify another IP
      address of the leased line user's client as the HealthCheck target IP
      address. HealthCheckSourceIp and HealthCheckTargetIp parameters must be
      both specified or left unspecified.
Resources:
  RouterInterface:
    Type: 'ALIYUN::VPC::RouterInterface'
    Properties:
      OppositeInterfaceId:
        Ref: OppositeInterfaceId
      OppositeInterfaceOwnerId:
        Ref: OppositeInterfaceOwnerId
      Description:
        Ref: Description
      OppositeRouterId:
        Ref: OppositeRouterId
      OppositeRegionId:
        Ref: OppositeRegionId
      PricingCycle:
        Ref: PricingCycle
      InstanceChargeType:
        Ref: InstanceChargeType
      HealthCheckSourceIp:
        Ref: HealthCheckSourceIp
      Period:
        Ref: Period
      RouterId:
        Ref: RouterId
      AutoPay:
```

```
        Ref: AutoPay
      Name:
        Ref: Name
      Role:
        Ref: Role
      OppositeRouterType:
        Ref: OppositeRouterType
      RouterType:
        Ref: RouterType
      AccessPointId:
        Ref: AccessPointId
      OppositeAccessPointId:
        Ref: OppositeAccessPointId
      Spec:
        Ref: Spec
      HealthCheckTargetIp:
        Ref: HealthCheckTargetIp
Outputs:
  RouterInterfaceId:
    Description: The ID of created RouterInterface.
    Value:
      'Fn::GetAtt':
        - RouterInterface
        - RouterInterfaceId
```
