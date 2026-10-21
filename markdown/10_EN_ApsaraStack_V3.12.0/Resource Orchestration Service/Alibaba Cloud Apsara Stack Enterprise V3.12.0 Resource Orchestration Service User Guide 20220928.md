---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Resource Orchestration Service User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 336
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Resource Orchestration Service User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Resource%20Orchestration%20Service%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Resource Orchestration Service User Guide 20220928

## Table of Contents

- 1 What is ROS?
- 2 Log on to the ROS console
- 3 Create a stack
- 4 Template syntax
  - 4.1 Template structure
  - 4.2 Parameters
  - 4.3 Resources
  - 4.4 Outputs
  - 4.5 Functions
  - 4.6 Mappings
  - 4.7 Conditions
- 5 Resource types
  - 5.1 ECS
    - 5.1.1 ALIYUN::ECS::AutoSnapshotPolicy
    - 5.1.2 ALIYUN::ECS::BandwidthPackage
    - 5.1.3 ALIYUN::ECS::Command
    - 5.1.4 ALIYUN::ECS::CustomImage
    - 5.1.5 ALIYUN::ECS::DedicatedHost
    - 5.1.6 ALIYUN::ECS::Disk
    - 5.1.7 ALIYUN::ECS::DiskAttachment
    - 5.1.8 ALIYUN::ECS::ForwardEntry
    - 5.1.9 ALIYUN::ECS::Instance
    - 5.1.10 ALIYUN::ECS::InstanceClone
    - 5.1.11 ALIYUN::ECS::InstanceGroup
    - 5.1.12 ALIYUN::ECS::InstanceGroupClone
    - 5.1.13 ALIYUN::ECS::Invocation
    - 5.1.14 ALIYUN::ECS::JoinSecurityGroup
    - 5.1.15 ALIYUN::ECS::LaunchTemplate
    - 5.1.16 ALIYUN::ECS::NatGateway
    - 5.1.17 ALIYUN::ECS::NetworkInterface
    - 5.1.18 ALIYUN::ECS::NetworkInterfaceAttachment
    - 5.1.19 ALIYUN::ECS::NetworkInterfacePermission
    - 5.1.20 ALIYUN::ECS::Route
    - 5.1.21 ALIYUN::ECS::SNatEntry
    - 5.1.22 ALIYUN::ECS::SecurityGroup
    - 5.1.23 ALIYUN::ECS::SecurityGroupClone
    - 5.1.24 ALIYUN::ECS::SecurityGroupEgress
    - 5.1.25 ALIYUN::ECS::SecurityGroupIngress
    - 5.1.26 ALIYUN::ECS::Snapshot
    - 5.1.27 ALIYUN::ECS::SSHKeyPair
    - 5.1.28 ALIYUN::ECS::SSHKeyPairAttachment
    - 5.1.29 ALIYUN::ECS::VPC
    - 5.1.30 ALIYUN::ECS::VSwitch
  - 5.2 ESS
    - 5.2.1 ALIYUN::ESS::AlarmTask
    - 5.2.2 ALIYUN::ESS::AlarmTaskEnable
    - 5.2.3 ALIYUN::ESS::LifecycleHook
    - 5.2.4 ALIYUN::ESS::ScalingConfiguration
    - 5.2.5 ALIYUN::ESS::ScalingGroup
    - 5.2.6 ALIYUN::ESS::ScalingGroupEnable
    - 5.2.7 ALIYUN::ESS::ScalingRule
    - 5.2.8 ALIYUN::ESS::ScheduledTask
  - 5.3 OSS
    - 5.3.1 ALIYUN::OSS::Bucket
  - 5.4 RDS
    - 5.4.1 ALIYUN::RDS::Account
    - 5.4.2 ALIYUN::RDS::AccountPrivilege
    - 5.4.3 ALIYUN::RDS::DBInstance
    - 5.4.4 ALIYUN::RDS::DBInstanceParameterGroup
    - 5.4.5 ALIYUN::RDS::DBInstanceSecurityIps
    - 5.4.6 ALIYUN::RDS::PrepayDBInstance
  - 5.5 ROS
    - 5.5.1 ALIYUN::ROS::WaitCondition
    - 5.5.2 ALIYUN::ROS::WaitConditionHandle
    - 5.5.3 ALIYUN::ROS::Stack
  - 5.6 SLB
    - 5.6.1 ALIYUN::SLB::AccessControl
    - 5.6.2 ALIYUN::SLB::BackendServerAttachment
    - 5.6.3 ALIYUN::SLB::BackendServerToVServerGroupAddition
    - 5.6.4 ALIYUN::SLB::Certificate
    - 5.6.5 ALIYUN::SLB::DomainExtension
    - 5.6.6 ALIYUN::SLB::Listener
    - 5.6.7 ALIYUN::SLB::LoadBalancer
    - 5.6.8 ALIYUN::SLB::LoadBalancerClone
    - 5.6.9 ALIYUN::SLB::MasterSlaveServerGroup
    - 5.6.10 ALIYUN::SLB::Rule
    - 5.6.11 ALIYUN::SLB::VServerGroup
  - 5.7 VPC
    - 5.7.1 ALIYUN::VPC::EIP
    - 5.7.2 ALIYUN::VPC::EIPAssociation
    - 5.7.3 ALIYUN::VPC::PeeringRouterInterfaceBinding
    - 5.7.4 ALIYUN::VPC::PeeringRouterInterfaceConnection
    - 5.7.5 ALIYUN::VPC::RouterInterface

## 1 What is ROS?

Resource Orchestration Service (ROS) is a service provided by Alibaba Cloud to simplify the management of cloud computing resources. You can author stack templates based on the template specifications defined in ROS. Within a template, you can define required cloud computing resources such as ECS and ApsaraDB for RDS instances, and the dependencies between resources. The ROS engine automatically creates and configures all resources in a stack based on a template, making automatic deployment and O&M possible. An ROS template is a readable, easy-to-author text file. You can directly edit a JSON-formatted template or use the Visual Editor available in the ROS console to edit the template. You can modify templates at any time. You can use version control tools such as SVN and Git to control the template and infrastructure versions. You can use APIs and SDKs to integrate the orchestration capabilities of ROS with your own applications to implement infrastructure as code. ROS templates are also a standardized way to deliver resources and applications. If you are an independent software vendor (ISV), you can use ROS templates to deliver a holistic system and solution encompassing cloud resources and applications. ISVs can use this method to integrate Alibaba Cloud resources with their own software systems for centralized delivery. ROS manages a group of cloud resources as a single unit called a stack. A stack is a group of Alibaba Cloud resources. You can create, delete, and clone cloud resources by stack. In DevOps practices, you can use ROS to clone the development, testing, and production environments, as well as migrate and scale out applications. le

## 2 Log on to the ROS console

This topic describes how to log on to the ROS console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Resource Orchest rat ion Service.

## 3 Create a stack

This topic describes how to use Resource Orchestration Service (ROS) to create a stack. Prerequisites Log on to the ROS console. For more information, see Log on to the ROS console. Procedure
1. In the upper-right corner of the page, click Creat e St ack.
2. In the Select T emplat e step, set Organizat ion, Resource Set , and regionId.
3. In the Prepare T emplat e section, enter template content in the JSON format. Click Next .
4. In the Conf igure T emplat e Paramet ers step, enter the stack name and parameters, and then click
Next .
5. In the Conf igure St ack step, set Rollback on Failure and Timeout Period.
6. In the Conf irm step, ensure the configurations of template and stack are correct and click Creat e St ack.
What's next On the St acks page in the ROS console: To delete a stack, click Delet e in the Actions column corresponding to the target stack. To update a stack, click Updat e in the Actions column corresponding to the target stack. To recreate a stack, click Recreat e in the Actions column corresponding to the target stack. Not e If you only need to modify the current template and configurations of a specified stack but do not need to change the region where the stack resides, update the stack. If you need to modify the current template and configurations of a specified stack and change the region where the stack resides, recreate the stack.

## 4 Template syntax

### 4.1 Template structure

A template is a UTF-8 encoded JSON file that is used to create stacks. Templates serve as the blueprint for underlying infrastructure and architecture. Templates define the configurations and dependencies of Alibaba Cloud resources. ROS template structure

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Description" : "The template description used to provide information such as application scena
rios and stack architecture.",
  "Metadata" : {
    // The template metadata that provides information such as layout for visualizations.
```

`},`

```json
  "Parameters" : {
    // The parameters you can specify when you create a stack.
```

`},`

```json
  "Mappings" : {
    // The mapping tables. Mapping tables are nested tables.
```

`},`

```json
  "Conditions": {
    // The conditions defined using internal condition functions. These conditions determine when
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
    // The outputs used to provide information such as resource properties. You can use the ROS c
onsole or API to obtain the information.
```

ROSTemplateFormatVersion Required. The template versions supported by Resource Orchestration Service (ROS). Current version: 2015-09- 01. Optional. The description of the template, which is used to provide information such as the application scenarios and architecture of the template. A detailed description can help users better understand the content of the template. Metadata Optional. The metadata of the template, in the JSON format. Optional. The parameters that you can specify when you create a stack. An ECS instance type is often defined as a parameter. Parameters have default values. Parameters can improve the flexibility and reusability of the template. When you create a stack, select appropriate specifications. Optional. Mappings are defined as nested mapping tables. You can use Fn::FindInMap to retrieve values corresponding to keys. You can also use parameter values as keys. For example, you can search the regionimage mapping table for desired images by region. Optional. The conditions defined using Fn::And, Fn::Or, Fn::Not, and Fn::Equals. Separate multiple conditions with commas (,). The system will evaluate all conditions in the template before creating or updating a stack. All resources associated with true conditions are created, and all resources associated with false conditions are ignored. Optional. The detailed information of resources in the stack created based on the template. The information includes resource dependencies and configurations. Optional. The outputs that are used to provide information such as resource properties. You can use the ROS console or API to obtain the information.

### 4.2 Parameters

The Parameters section improves the flexibility and reusability of a template. When you create a stack, you can replace parameter values in the template. For example, assume that you have a web application requiring a stack that contains one SLB instance, two ECS instances, and one ApsaraDB for RDS instance. If the web application has a heavy workload, you can select an ECS instance with high specifications when you create the stack. Otherwise, you can select an ECS instance with low specifications. The following example shows how to define the InstanceType parameter for an ECS instance:

```json
"Parameters" : {
  "InstanceType" : {
    "Type" : "String",
    "AllowedValues":["ecs.t1.small","ecs.s1.medium", "ecs.m1.medium", "ecs.c1.large"],
    "Default": "ecs.t1.small",
    "Label": "The ECS instance type",
    "Description" : "The type of the ECS instance you want to create. Default value: ecs.t1.small
. Valid values: ecs.t1.small, ecs.s1.medium, ecs.m1.medium, and ecs.c1.large."
```

You can assign a value to the InstanceType parameter when you create stacks based on templates. If this parameter is not specified, the default value `ecs.t1.small` is used. The following example shows how to reference the InstanceType parameter when you define a resource:

```json
"Webserver" : {
  "Type" : "ALIYUN::ECS::Instance",
  "InstanceType": {
    "Ref": "InstanceType"
```

Syntax Each parameter consists of a name and properties. The parameter name can only contain letters and digits and must be unique within the template. You can use the Label field to define the alias of the parameter. The following table describes the parameters:

| Parameter | Required | Description |
|---|---|---|
| Type | Yes | The data type of the parameter. String: a string value. Example: "ecs.s1.medium" . Number: an integer or floating-point number. Example: 3.14. CommaDelimitedList: a set of strings or numbers separated with commas (,), which can be indexed by using Fn::Select. Example: "80, foo, bar" . Json: a JSON-formatted string. Example: { "foo": "bar" } . Boolean: a Boolean value. Example: true or false . |
| Default | No | If you do not specify a value when you create a stack, Resource Orchestration Service (ROS) checks whether a default value is defined in the template. If a default value is found, it is used. Otherwise, an error is returned. |
| AllowedValues | No | The list of valid parameter values. |
| AllowedPattern | No | The regular expression that is used to check whether the specified parameter value is a string. If the input is not a string, an error is returned. |
| MaxLength | No | The integer value that determines the longest string allowed for a String type parameter. |
| MinLength | No | The integer value that determines the shortest string allowed for a String type parameter. |
| MaxValue | No | The numeric value that determines the maximum value allowed for a Number type parameter. |
| MinValue | No | The numeric value that determines the minimum value allowed for a Number type parameter. |
| NoEcho | No | Specifies whether to mask the parameter value when the GetStack operation is called. If this parameter is set to true, only asterisks (*) are returned. |
| Description | No | The string that describes the parameter. |

| esource Orchestratio | n Service | User Guide·Template synta |
|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| ConstraintDescriptio n | No | The string that explains the parameter constraint. |
| Label | No | The alias of the parameter, encoded in UTF-8. When web forms are generated using templates, labels can be mapped to parameter names. |
| AssociationProperty | No | Automatically verifies the validity of the parameter value and provides a list of valid values. Valid values: ALIYUN::ECS::Instance::ImageId ALIYUN::ECS::Instance::ZoneId ALIYUN::ECS::VPC::VPCId ALIYUN::ECS::VSwitch::VSwitchId When AssociationProperty is set to ALIYUN::ECS::Instance::ImageId , the ROS console verifies whether the specified image ID is available and lists other values in a drop-down list. |
| Confirm | No | Specifies whether to enter the parameter value a second time when the NoEcho parameter is set to true. Default value: false. Not ice This parameter can be set to true only when it is used with a String type parameter and the NoEcho parameter is set to true. |

Examples In the following example, two parameters are defined in the Parameters section.

```
 username
```

Type: String Default value: anonymous. Valid values: anonymous user-one user-two Length: 6 to 12 Not ice The default value must also meet the length and valid value requirements.

```
 password
```

Type: String Length: 1 to 41 The password can contain uppercase letters, lowercase letters, and digits. If you set the NoEcho parameter to true, the GetStack operation does not return any parameter values.

```json
"Parameters" : { "username" : { "Label": "Username", "Description": "Enter the username", "Default": "anonymous", "Type" : "String", "MinLength" : "6", "MaxLength" : "12", "AllowedValues": ["anonymous", "user-one", "user-two"]
```

`},`

```json
"password" : { "Label": "Password", "NoEcho" : "True", "Description": "Enter the password", "Type" : "String", "MinLength" : "1", "MaxLength" : "41", "AllowedPattern" : "[a-zA-Z0-9]*"
```

Pseudo parameters Pseudo parameters are internal parameters provided by the ROS engine. They can be referenced in the same manner as user-defined parameters, and their values are determined while ROS is running. The following pseudo parameters are supported: ALIYUN::StackName: the name of the stack. ALIYUN::StackId: the ID of the stack. ALIYUN::Region: the region where the stack resides. ALIYUN::AccountId: the user ID of the stack. ALIYUN::NoValue: specifies whether the specific resource property is deleted when the resource is created or updated.

### 4.3 Resources

This topic describes the properties of each resource and dependencies of resources in a stack. A resource can be referenced by other resources and output items. Syntax Each resource consists of an ID and a description. All resource descriptions are enclosed in braces {}. Separate multiple resources with commas (,). The following sample code shows the Resources syntax:

```json
"Resources" : {
    "Resource1 ID": {
        "Type": "The resource type",
        "Condition": "The condition that specifies whether to create the resource",
        "Properties" : {
            The description of the resource properties
```

`},`

```json
    "Resource2 ID" : {
        "Type": "The resource type",
        "Condition": "The condition that specifies whether to create the resource",
        "Properties" : {
            The description of the resource properties
```

Parameter description: The resource ID must be unique within the template. You can use the resource ID to reference the resource in other parts of the template. The Type parameter specifies the type of resource that is being declared. For example, ALIYUN::ECS::Instance indicates that the resource is an Elastic Cloud Service (ECS) instance. The Properties section provides additional options that you can specify for a resource. For example, you must specify an image ID for each Alibaba Cloud ECS instance. The image ID is one of the resource properties. Examples

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
```

`},`

```json
    "DeletionPolicy" : "Retain"
```

DependsOn The DependsOn parameter allows you to create a specific resource after you create its dependent resource. If you specify the DependsOn parameter for a resource, the resource is created only after its dependent resource specified by the DependsOn parameter is created. In the following example, WebServer is created only after DatabaseServer is created:

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
```

`},`

```json
  "Conditions": {
    "CreateWebServer": {"Fn::Not": {"Fn::Equals": [0, {"Ref": "MaxAmount"}]}}
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
      "Condition": "CreateWebServer",
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
```

`},`

```json
    "DatabseServer": {
      "Type": "ALIYUN::ECS::Instance",
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
```

Resource declaration example The following example shows how to declare a resource:

```json
"Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
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

### 4.4 Outputs

The Outputs section is used to define the values returned when the GetStack operation is called. For example, if you define an ECS instance ID as an output item, the ECS instance ID is returned when the GetStack operation is called. Syntax Each output item consists of an ID and a description. All output descriptions are enclosed in braces {}. Separate multiple output items with commas (,). Each output item can have multiple values in the array format. The following example shows the Outputs syntax:

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

`]` Output ID: the ID of the output item. Duplicate IDs are not allowed within a template. Description: optional. The description of the output item. Value: required. The value returned when the GetStack operation is called. Condition: optional. The condition that specifies whether to create a resource and provide its information. The resource is created and its information is provided only when the specified condition is true. In the following example, WebServer is created only if the condition determined by the MaxAmount parameter is true:

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
        "ImageId" : "m-25l0r****",
        "InstanceType": "ecs.t1.small"
        "MaxAmount": {"Ref": "MaxAmount"}
  "Outputs": {
    "WebServerIP": {
      "Condition": "CreateWebServer",
      "Value": {
        "Fn::GetAtt": ["WebServer", "PublicIps"]
```

Examples The following example contains two output items. The value of the InstanceId parameter of WebServer. The values of the PublicIp and PrivateIp parameters of WebServer.

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

### 4.5 Functions

Resource Orchestration Service (ROS) provides several built-in functions to help you manage stacks. You can use built-in functions to define Resources and Outputs. Fn::Base64Encode The Fn::Base64Encode function is used to return the Base64 representation of the input string. Declaration

```
"Fn::Base64Encode": "stringToEncode"
```

`stringToEncode` : the string decoded from the Base64-encoded string. Return value The Base64 representation of the input string. Examples

```json
{"Fn::Base64Encode": "string to encode"}
```

`c3RyaW5nIHRvIGVuY29kZQ==` is returned in this example. Fn::Base64Decode The Fn::Base64Decode function is used to return a string decoded from a Base64-encoded string. Declaration

```json
{"Fn::Base64Decode": "stringToEncode"}
```

`stringToDecode` : the string decoded from the Base64-encoded string. Return value The string decoded from the Base64-encoded string. Examples

```json
{"Fn::Base64Decode": "c3RyaW5nIHRvIGVuY29kZQ=="}
```

`string to encode` is returned in this example. Fn::Base64 The Fn::Base64 function returns the Base64 representation of the input string. Declaration

```
 "Fn::Base64": stringToEncode
```

valueToEncode: the string to be encoded in Base64. Return value The Base64 representation of the input string. Examples

```
 "Fn::Base64":"string to encode"
```

Fn::FindInMap The Fn::FindInMap function is used to return the values based on keys in a two-level mapping that is declared in the Mappings section. Declaration

```
"Fn::FindInMap": ["MapName", "TopLevelKey", "SecondLevelKey"]
```

`MapName` : the ID of a mapping declared in the Mappings section that contains keys and values. `TopLevelKey` : the top-level key name. The value is a list of key-value pairs. `SecondLevelKey` : the second-level key name. The value is a string or a number. Return value The value that is assigned to the SecondLevelKey parameter. Examples The ImageId property must be specified when you create a WebServer instance. The Mappings section describes the ImageId mappings by region. The Parameters section describes the regions that must be specified by template users. Fn::FindInMap finds the corresponding ImageId mapping in RegionMap based on the region specified by a user, and then finds the corresponding ImageId in the mapping. MapName can be set to a custom value, which is `"RegionMap"` in this example. TopLevelKey is set to the region where the stack is created, which is `{ "Ref" : "regionParam" }` in this example. SecondLevelKey is set to the required architecture, which is `"32"` in this example.

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

`]` Supported functions Fn::FindInMap Ref Fn::GetAtt The Fn::GetAtt function is used to return the value of a property from a resource in a template. Declaration

```
"Fn::GetAtt": ["resourceID", "attributeName"]
```

`resourceID` : the ID of the resource. `attributeName` : the name of the resource property. Return value The value of the resource property. Examples The ImageId property of MyEcsInstance is returned in this example.

```json
{"Fn::GetAtt" : ["MyEcsInstance" , "ImageID"]}
```

Fn::Join The Fn::Join function is used to append a set of values into a single value that is separated by a specified delimiter. Declaration

```json
{"Fn::Join": ["delimiter", ["string1", "string2", ... ]]}
```

`delimiter` : the value used to divide the string. The delimiter value can be left blank so that all the values are directly combined. `[ "string1", "string2", ... ]` : the list of values that are combined into a string. Return value The combined string. Examples

```json
{"Fn::Join": [ ",", ["a", "b", "c"]]}
```

`"a,b,c"` is returned in this example. Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Select The Fn::Select function is used to return a single data element from a list of data elements by an index. Declaration The following example assumes that the list of data elements is an array:

```
"Fn::Select": ["index", ["value1", "value2", ... ]]
```

The following example assumes that the list of data elements is a mapping table:

```
"Fn::Select": ["index", {"key1": "value1", ... }]
```

`index` : the index of the object data element. If the list of data elements is an array, the index must be an integer ranging from 0 to N-1, where N indicates the number of elements in the array. If the list of data elements is a mapping table, the index must be a key in the mapping table. If the corresponding value of the index cannot be found, the system returns an empty string. Return value The object data element. Examples The following example assumes that the list of data elements is an array:

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
          "CidrBlock": {"Fn::Select": ["0", {"Ref": "userParam"}]}
```

Supported functions For the Fn::Select index value, you can use the Ref function. For the Fn::Select list of data elements, you can use the following functions: Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref Ref The Ref function is used to return the value of a specified parameter or resource. If the specified parameter is a resource ID, the value of the resource is returned. Otherwise, the system will return the value of the specified parameter. Declaration

```json
"Ref": "logicalName"
```

`logicalName` : the logical name of the resource or parameter that you want to reference. Return value The value of the resource or parameter. Examples The following example uses the Ref function to specify regionParam as the region parameter for RegionMap of WebServer:

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

`]` Supported function When you use Ref function, you cannot use other functions in it at the same time. You must specify a string value for the resource logical ID. Fn::GetAZs The Fn::GetAZs function is used to return a list of zones for a specified region. Declaration

```
"Fn::GetAZs": "region"
```

`region` : the ID of the region. Return value The list of zones for the specified region. Examples The following example demonstrates how to create an ECS instance in the first zone of a specified region:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
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

Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Ref Fn::Replace The Fn::Replace function is used to replace a specified substring contained in a string with a new substring. Declaration

```json
{"Fn::Replace": [{"object_key": "object_value"}, "object_string"]}
```

`object_key` : the substring to be replaced. `object_value` : the new substring to replace the previous substring. `object_string` : the string whose `object_key` is replaced. Return value The string after replacement. Examples The following example demonstrates how to replace "print" with "echo" in the specified script:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
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
             "#! /bin/sh\n",
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

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Split The Fn::Split function is used to split a string into a list of values separated by a specified delimiter and return the list. Declaration

```
"Fn::Split": ["delim", "original_string"]
```

| delim | : the specif |
|---|---|
| original string _ |   |

`delim` : the specified delimiter, which can be commas (,), semicolons (;), line breaks (\n), and indents (\t). `original_string` : the string to be split. Return value A list of string values. Examples The following example assumes that the list of data elements is an array:

```json
{"Fn::Split": [";", "foo; bar; achoo"]}
```

`["foo", " bar", "achoo "]` is returned in this example. The following example uses Fn::Split to split InstanceIds:

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
        "BackendServerList": {
          "Fn::Split": [
            ",",
              "Ref": "InstanceIds"
```

`]` Supported functions Fn::Base64Encode Fn::FindInMap Fn::GetAtt Fn::Join Fn::Select Fn::Replace Fn::GetAZs Fn::If Ref Fn::Equals The Fn::Equals function is used to compare whether two values are equal. If the two values are equal, true is returned. If the two values are not equal, false is returned. Declaration

```json
{"Fn::Equals": ["value_1", "value_2"]}
```

`value` : the values to be compared. Return value true or false. Examples The following example uses Fn::Equals to define a condition in the Conditions section:

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

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::And The Fn::And function is used to represent the AND operator, and must contain at least two conditions. If all the specified conditions are evaluated as true, true is returned. If any condition is evaluated as false, false is returned. Declaration

```json
{"Fn::And": ["condition", {...}]}
```

`condition` : the condition to be evaluated. Return value true or false. Examples The following example uses Fn::And to define a condition in the Conditions section:

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

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::Or The Fn::Or function is used to represent the OR operator, and must contain at least two conditions. If any specified condition is evaluated as true, true is returned. If all the conditions are evaluated as false, false is returned. Declaration

```json
{"Fn::Or": ["condition", {...}]}
```

`condition` : the condition to be evaluated. Return value true or false. Examples The following example uses Fn::Or to define a condition in the Conditions section:

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

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::Not The Fn::Not function is used to represent the NOT operator. If a condition is evaluated as false, true is returned. If a condition is evaluated as true, false is returned. Declaration

```json
{"Fn::Not": "condition"}
```

`condition` : the condition to be evaluated. Return value true or false. Examples The following example uses Fn::Not to define a condition in the Conditions section:

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

Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::If This function returns one of two possible values. If a specified condition is evaluated as true, one value is returned. If the specified condition is evaluated as false, the other value is returned. The property values of Resources and Outputs in templates support the Fn::If function. You can use the `ALIYUN::NoValue` pseudo parameter as the return value to delete the corresponding property. Declaration

```json
{"Fn::If": ["condition_name", "value_if_true", "value_if_false"]}
```

`condition_name` : the name of the condition in the Conditions section. A condition is referenced by using the condition name.

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
```

`q`

```json
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

`]` Supported functions Fn::Or Fn::Not Fn::Equals Fn::FindInMap Fn::And Ref Fn::ListMerge The Fn::ListMerge function is used to merge multiple lists into one list. Declaration

```json
{"Fn::ListMerge": [["list_1_item_1", "list_1_imte_2", ...], ["list_2_item_1", "list_2_imte_2", .. .]]}
```

`["list_1_item_1", "list_1_imte_2", ...]` : the first list to merge. `["list_2_item_1", "list_2_imte_2", ...]` : the second list to merge into the first list. Examples The following example demonstrates how to attach two ECS instance groups to an SLB instance:

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
        "LoadBalancerName": "ros",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
```

`},`

```json
    "BackendServer1": {
      "Type": "ALIYUN::ECS::InstanceGroup",
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
        "LoadBalancerId": {"Ref": "LoadBalancer"},
        "BackendServerList": { "Fn::ListMerge": [
            {"Fn::GetAtt": ["BackendServer1", "InstanceIds"]},
            {"Fn::GetAtt": ["BackendServer2", "InstanceIds"]}
```

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Join Fn::If Fn::GetJsonValue The Fn::GetJsonValue function is used to resolve a JSON string and obtain its key value from the first layer. Declaration

```json
{"Fn::GetJsonValue": ["key", "json_string"]}
```

| key | : the key |
|---|---|
| json string _ |   |

`json_string` : the specified JSON string to be resolved. Examples In the following example, the WebServer instance executes UserData and returns a JSON string, and the WebServer2 instance then obtains the corresponding key value from the string.

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "WebServer": {
      "Type": "ALIYUN::ECS::Instance",
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "Password": "Wenqiao****",
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxze****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData": {"Fn::Join": ["", [
             "#! /bin/sh\n",
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
          "Handle": {"Ref": "WaitConHandle"},
          "Timeout": 900
```

`},`

```json
    "WebServer2": {
      "Type": "ALIYUN::ECS::Instance",
"ImageId" "m2e45 oa5fedl****"
```

```json
        "ImageId" : "m-2ze45uwova5fedlu****",
        "InstanceType": "ecs.n1.medium",
        "SecurityGroupId": "sg-2ze7pxymaix640qr****",
        "Password": "Wenqiao****,
        "IoOptimized": "optimized",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "VpcId": "vpc-2zevx9ios1rszqv0a****",
        "SystemDiskCategory": "cloud_ssd",
        "UserData":
          {"Fn::Join": ["", [
             "#! /bin/sh\n",
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

Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Join Fn::If Fn::MergeMapToList The Fn::MergeMapToList function is used to merge multiple mappings into a list of mapping elements. Declaration

```json
{"Fn::MergeMapToList": [{"key_1": ["key_1_item_1", "key_1_item_2", ...]}, {"key_2":["key_2_item_1 ", "key_2_item_2", ...]}, ... ]}
```

| {"key 1": ["key 1 item 1", "key 1 item 2", ...]} _ _ _ _ _ _ _ |   |   |
|---|---|---|
| value must be a list. | " key 1" _ | is the key for each map |

value is `"key_1_item_1"` for the first merged mapping and `"key_1_item_2"` for the second merged mapping. All values follow the same format. The length of the final list of merged mappings is the length of the longest list `"key_x"` from all mappings being merged. If a `"key_y"` list is shorter, the last element of the list is repeated until the list is the longest. `{"key_2": ["key_2_item_1", "key_2_item_2", ...]}` : the second mapping to merge into the first mapping. The `" key_2"` value must be a list. `" key_2"` is the key for each mapping in the merged list. The "key_2" value is `"key_2_item_1"` for the first merged mapping and `"key_2_item_2"` for the second merged mapping. Examples The following example demonstrates how to merge three mappings. The length of the list based on the key values for each mapping is the same.

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

`]` In the following template example, all instances created in WebServer are added to the VServer group of an SLB instance:

```json
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
        "WebServer": {
          "Type": "ALIYUN::ECS::InstanceGroupClone",
              "SourceInstanceId": "i-xxxxx",
               "Password": "Hello****",
               "MinAmount": 1,
               "MaxAmount": 1
```

`},`

```json
        "CreateVServerGroup": {
            "Type": "ALIYUN::SLB::VServerGroup",
                "LoadBalancerId": "lb-****",
                "VServerGroupName": "VServerGroup-****",
                "BackendServers": {
                   "Fn::MergeMapToList": [
                       {"Port": [6666, 9090, 8080]},
                       {"ServerId": {"Fn::GetAtt": ["WebServer", "InstanceIds"]}},
                       {"Weight": [20, 100]}
```

`]` Supported functions Fn::Base64Encode Fn::GetAtt Fn::Join Fn::Select Ref Fn::Join Fn::If Fn::ListMerge Fn::GetJsonValue Fn::Avg The Fn::Avg function is used to return the average value of a set of numbers. Declaration

```json
{"Fn::Avg": [ndigits, [number1, number2, ... ]]}
```

| ndigits | : the number of dec |
|---|---|
| [ number1, number2, ... ] |   |

`ndigits` : the number of decimal places to report. This parameter value must be an integer. `[ number1, number2, ... ]` : the set of numbers for which the average value will be calculated. Each element in the group must be either a number or a string that can be converted into a number. Return value The average value of the set of numbers. Examples

```json
{ "Fn::Avg": [ 1, [1, 2, 6.0] ] } { "Fn::Avg": [ 1, ['1', '2', '6.0'] ] }
```

3.0 is returned in this example. Supported functions Fn::GetAtt Ref Fn::SelectMapList The Fn::SelectMapList function is used to return a list of map elements. Declaration

```json
{"Fn::SelectMapList": ["key2", [{"key1": "value1-1", "key3": "value1-3"}, {"key1": "value2-1", "k ey2": "value2-2"}, {"key1": "value3-1", "key2": "value3-2"}, ...] ] }
```

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

The parameters must be arranged as a list. The parameters in the list can be of the Number, List, or Dictionary type. All the parameters must be of the same type. The list must contain at least two parameters. Return value If the parameter values are numbers, sum the parameter values. If the parameter values are lists, concatenate the values. If the parameter values are dictionaries, merge the values. If the two parameters have the same key, overwrite the former parameter value with the latter. Examples

```json
 "Fn::Add": [
   {"Product": "ROS"},
   {"Fn": "Add"}
```

`]` `{"Fn":"Add","Product":"ROS"}` is returned in this example.

### 4.6 Mappings

The Mappings section is a key-value mapping table. When mappings are used in Resources or Outputs definitions, use Fn::FindInMap to find their values by using corresponding keys. Syntax A mapping consists of key-value pairs, where both the keys and values can be strings or numbers. Multiple mappings are separated with commas (,). Each mapping name must be unique. Mappings must be pure data and cannot parse functions. Examples The following example shows a correct mapping definition:

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

### 4.7 Conditions

There are four conditional operators: Fn::And, Fn::Or, Fn::Not, and Fn::Equals. These operators, along with the parameters that you specify when you create or update a stack, are used to evaluate each condition. You can reference other conditions, parameters, and mappings in your condition. Conditions are used in resource and output definitions to establish dependencies. Use Fn::If or Condition in resource and output definitions to implement conditions. Syntax Each condition consists of a condition name and a condition body. The condition name is a string. The condition body starts with Fn::And, Fn::Or, Fn::Not, or Fn::Equals. You can reference other conditions in your condition and separate multiple conditions with commas (,). Each condition name must be unique. The following functions can be used, but not as the outermost functions: "Fn::Select", "Fn::Join", "Fn::Split", "Fn::Replace","Fn::Base64Encode", "Fn::Base64Decode", "Fn::MemberListToMap","Fn::If", "Fn::ListMerge", "Fn::GetJsonValue", "Fn::MergeMapToList","Fn::SelectMapList", "Fn::Add", "Fn::Avg", "Fn::Str", "Fn::Calculate","Ref"(parameter references only), and "Fn:: FindInMap". Examples The following example shows how to define conditions:

```json
"Conditions" : {
       "DevEnv": {"Fn::Equals": ["Dev", {"Ref": "EnvType"}]},
       "UTEnv": {"Fn::Equals": ["UT", {"Ref": "EnvType"}]},
       "PREEnv": {"Fn::Not": {"Fn::Or": ["DevEnv", "UTEnv"]}},
       "ProdEnv": {"Fn::And": [{"Fn::Equals": ["Prod", {"Ref": "EnvType"}]}, "PREEnv"]}
```

The following example shows how to use conditions in a resource definition: In this example, a condition is used to determine whether to create a data disk and an OSS bucket for an ECS instance based on the EnvType value.

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
```

```json
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
        "OssBucket": {
            "Type": "ALIYUN::OSS::Bucket",
            "Condition": "CreateProdRes",
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

## 5 Resource types

### 5.1 ECS

#### 5.1.1 ALIYUN::ECS::AutoSnapshotPolicy

ALIYUN::ECS::AutoSnapshotPolicy is used to create an automatic snapshot policy. Statement

```json
  "Type" : "ALIYUN::ECS::AutoSnapshotPolicy",
  "Properties" : {
    "TimePoints" : String,
    "RepeatWeekdays" : String,
    "RetentionDays" : Integer,
    "DiskIds" : String,
    "AutoSnapshotPolicyName" : String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TimePoints | List | Retained | Yes | The points in time at which automatic snapshots are created. Unit: hours. | Value range:[0, 23], represents 24 time points from 00:00 to 23:00. For example: 1 indicating 01:00. To schedule multiple automatic snapshot creation tasks in a day, you can set the TimePoints parameter as an array. The maximum number of time points allowed is 24. Use one format for multiple time points like [0, 1,... 23]. Separate time points with commas (,). |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RepeatWeekday s | List | Retained | Yes | The days of a week on which automatic snapshots are created. | Value range:[1, 7], 1 indicates Monday. To schedule multiple automatic snapshot creation tasks in a week, you can set the RepeatWeekda ys parameter as an array. You can specify up to 7 days over a one week period. Use one format for multiple time points like [1, 2,... 7]. Separate the time points with commas (,). |
| RetentionDays | Integer | Retained | Yes | The number of days for which you want to retain automatic snapshots. | Default value: - 1. Valid values: -1: The automatic snapshots are retained indefinitely. [1, 65536]: The automatic snapshots are retained for the specified number of days. Default value: - 1. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskIds | List | Retained | Yes | The ID of the destination disk. When you want to apply the automatic snapshot policy to multiple disks, you can set the diskids "d- zzzzzzzzz"]. Separate multiple disk IDs with commas (,). | None |
| AutoSnapshotP olicyName | String | Yes | True | The name of the automatic snapshot policy. | The name must be 2 to 128 characters in length It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It cannot start with http:// or https://. This parameter is empty by default. |

Response parameters Fn::GetAtt AutoSnapshotPolicyId: the ID of the automatic snapshot policy. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AutoSnapshotPolicy": {
      "Type": "ALIYUN::ECS::AutoSnapshotPolicy",
        "TimePoints": ["0"],
        "RepeatWeekdays": ["1"],
        "RetentionDays": 10,
        "DiskIds": ["<DiskId>"],
        "AutoSnapshotPolicyName": "MyAutoSnapshotPolicy"
```

#### 5.1.2 ALIYUN::ECS::BandwidthPackage

ALIYUN::ECS::BandwidthPackage is used to create a service plan for a NAT gateway. Syntax

```json
  "Type": "ALIYUN::ECS::BandwidthPackage",
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

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
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

#### 5.1.3 ALIYUN::ECS::Command

ALIYUN::ECS::Command is used to create a Cloud Assistant command. Statement

```json
  "Type": "ALIYUN::ECS::Command",
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

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| WorkingDir | String | Yes | True | The working directory on the ECS instance where the command will be run. | None |
| CommandContent | String | Yes | Released | The Base64-encoded content of the command. When you specify request parameters Type you must also specify this parameter. The parameter value must be Base64-encoded and cannot exceed 16 KB in size after encoding. | None |
| Timeout | String | No. | True | The timeout period that is specified for the command to run on ECS instances. Unit: seconds. If the command fails to run within the specified period, the command execution will time out and the process will be forcibly terminated. Default value: 3600. | None |
| Type | String | No | No | The command type. Valid values: RunBatScript: Creates a Bat script for a Windows instance. RunPowerShellScript: Create a PowerShell script to run on a Windows instance. RunShellScript: Creates a Shell script for Linux- based instances. | None |
| Description | String | Yes | True | The description of the command, which supports all character sets. The description can be up to 100 characters in length. | None |

Response parameters Fn::GetAtt CommandId: the ID of the command. Sample request

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
      "Description": "The content of command. Content requires base64 encoding. Maximum size supp
ort 16KB."
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
      "Description": "Total timeout when the command is executed in the instance. Input the time
unit as second. Default is 3600s."
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

#### 5.1.4 ALIYUN::ECS::CustomImage

ALIYUN::ECS::CustomImage is used to create a custom image. Statement

```json
  "Type": "ALIYUN::ECS::CustomImage",
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
| Description | String | Yes | Released | The description of the image. | The description can be up to 256 characters in length. This parameter is empty by default. It cannot start with http:// or https://. |
| InstanceId | String | Yes | Released | The ID of the ECS instance. | If this parameter is specified, an ECS instance will be used to create the custom image. |

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ImageName | String | Yes | Released | The name of the image. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ and hyphens(-). It must start with a letter but cannot start with http:// or https://. |
| ImageVersion | String | Yes | Released | The image version. | The image version must be 1 to 40 characters in length. |
| SnapshotId | String | Yes | Released | The ID of the snapshot. | If this parameter is specified, a snapshot will be used to create the custom image. If both this parameter and the InstanceId parameter are specified, this parameter will be ignored and an instance will be used to create the custom image. |
| Tags | List | Erased | Released | The tags of the image. | None |
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the custom image belongs. | None |
| Platform | String | Yes | Released | If you specify a data disk snapshot to be used to create the system disk of the custom image, you must use the Platform parameter to determine the release version of the operating system for the system disk. | None |
| DiskDeviceMappin g | List | Erased | Released | The mappings between images and snapshots. | None |

| User Guide·Resource | types |   |   | Res | ource Orchestration Servic |
|---|---|---|---|---|---|

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
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
| Size | String | Optional | Released | The size of disk N. Unit: GiB. | Valid values: 5 to 2000. The default value is the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. If the DiskDeviceMapping.N.S napshotId parameter is not specified, the default disk size is 5 GiB. The disk size must be greater than or equal to the size of the snapshot specified by the DiskDeviceMapping.N.S napshotId parameter. |

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskType | String | Yes | Released | The type of disk N in the custom image. You can specify this parameter to create the system disk of the custom image from a data disk snapshot. If you do not specify this parameter, the disk type is determined by the corresponding snapshot. | Valid values: system: indicates a system disk. data: indicates a data disk. |

Response parameters Fn::GetAtt ImageId: the ID of the custom image. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WebServer": {
      "Type": "ALIYUN::ECS::InstanceGroup",
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

#### 5.1.5 ALIYUN::ECS::DedicatedHost

ALIYUN::ECS::DedicatedHost is used to create a dedicated host. Statement

```json
  "Type": "ALIYUN::ECS::DedicatedHost",
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
      "Description": "Unit of prepaid time period, it could be Week/Month. Default value is Month
.",
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
      "Description": "Auto release time for created host, Follow ISO8601 standard using UTC time.
format is 'yyyy-MM-ddTHH:mm:ssZ'. Not bigger than 3 years from this day onwards"
```

`},`

```json
  "Resources": {
    "Host": {
      "Type": "ALIYUN::ECS::DedicatedHost",
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
          "Host",
          "DedicatedHostIds"
```

`]`

#### 5.1.6 ALIYUN::ECS::Disk

ALIYUN::ECS::Disk is used to create an ECS Disk. Statement

```json
  "Type": "ALIYUN::ECS::Disk",
    "DiskName": String,
    "Description": String,
    "Tags": List,
    "AutoSnapshotPolicyId": String,
    "Encrypted": Boolean,
    "ZoneId": String,
    "ResourceGroupId": String,
    "SnapshotId": String,
    "DiskCategory": String,
    "PerformanceLevel": String,
    "DeleteAutoSnapshot": Boolean,
    "Size": Integer
```

Properties

| Parameter | Type |   |   | Required |   |   | Editable |   |   | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ResourceGroup Id | String |   |   | Yes |   |   | Released |   |   | The ID of the resource group to which the instance belongs. |   | None |   |   |
| ZoneId | String |   |   | No |   |   | No |   |   | The ID of the zone where the instance resides. |   | None |   |   |
| DiskName | String |   |   | Yes |   |   | Released |   |   | The name of the disk. |   | The name must be 2 to 128 characters in length And can contain letters, digits, periods, underscores ( ), _ and hyphens (-). It cannot start with http:// or https://. The disk name will be displayed in the ECS console. |   |   |
| Description | String |   |   | Yes |   |   | Released |   |   | The description of the disk. |   | The description must be 2 to 256 characters in length. Cannot http:// or https:// the beginning. The disk description will be displayed in the ECS console. |   |   |
| Tags | List |   |   | Erased |   |   | Released |   |   |   |   | Up to four tags are supported. Example values: [{"Key": |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{"Key": |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "tagKey", |   |   |
|   |   |   |   |   |   |   |   |   |   | The custom |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "Value": |   |   |
|   |   |   |   |   |   |   |   | ed |   | tags of the |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "tagValue"}, |   |   |
|   |   |   |   |   |   |   |   |   |   | instance. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {"Key": |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "tagKey2", |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "Value": |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | "tagValue2"}] |   |   |

|   | of |   |
|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskCategory | String | Yes | Released | The type of the data disk. | Value range cloud: indicates a basic disk. cloud efficiency: _ indicates an ultra disk. cloud ssd: _ indicates a standard SSD. cloud essd: _ enhanced SSD (ESSD) Default value: cloud. |
| SnapshotId | String | Yes | Released | The ID of the snapshot used to create the data disk. | If both this parameter and 'Size' are specified, the value of this parameter prevails. The actual size of the created disk is the size of the specified snapshot. Snapshots created on or before July 15, 2013 cannot be used to create disks. |
| PerformanceLe vel | String | Yes | Released | Specifies the performance level of an ESSD when you create the ESSD. | Default value: PL1. Valid values: PL1: A single enhanced SSD delivers up to 50,000 random read/write IOPS. PL2: A single ESSD delivers up to 100,000 random read/write IOPS. PL3: maximum random read /write IOPS of 100,000 per disk. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | Optional | Released | The size of the disk. Unit: GiB. The value of this parameter must be equal to or greater than the capacity of the specified snapshot. | Valid values: cloud: 5 to 2000 cloud efficiency: _ 20 to 32768 cloud ssd: 20 to _ 32768 cloud essd: 20 to _ 32768 |
| AutoSnapshot PolicyId | String | Yes | Released | The ID of each automatic snapshot policy. | None |
| Encrypted | Boolean | Erased | Released | Specifies whether to encrypt the disk. | Valid values: true false Default value: false. |
| DeleteAutoSna pshot | Boolean | Erased | Released | Specifies whether to delete the automatic snapshots of the disk when the disk is released. | Valid values: true false Default value: true. |

Tags syntax

```json
"Tags" : [
    "Value" : String,
    "Key" : String
```

`]` Tags properties

| Parameter | Type | Required | Editable |
|---|---|---|---|
| Key | String | No | No |
| Value | String | Yes | Released |

Response parameters Fn::GetAtt DiskId: the ID of the disk. Status: The Status of the disk. Sample request

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "DataDisk": {
      "Type": "ALIYUN::ECS::Disk",
        "Size": 10,
        "ZoneId": "cn-beijing-a",
        "DiskName": "DataDisk",
        "Description": "ECSDataDisk"
```

`},`

```json
  "Outputs": {
    "DiskId": {
         "Value" : {"Fn::GetAtt": ["DataDisk","DiskId"]}
```

`},`

```json
    "Status": {
         "Value" : {"Fn::GetAtt": ["DataDisk","Status"]}
```

#### 5.1.7 ALIYUN::ECS::DiskAttachment

ALIYUN::ECS::DiskAttachment is used to attach an ECS disk. Statement

```json
   "Type" : "ALIYUN::ECS::DiskAttachment",
   "Properties" : {
      "DiskId" : String,
      "InstanceId" : String,
      "Device" : String,
      "DeleteWithInstance" : String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | No | No | The ID of the instance. | None |
| DiskId | String | No | No | The ID of the disk. | The disk and the ECS instance must belong to the same zone. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Device | String | Yes | Released | The name of the disk. | If you do not set this parameter, the system will automatically allocate a device name in alphabetical order from /dev/xvdb to /dev/xvdz. |
| DeleteWithInsta nce | Boolean | Erased | Released | Specifies whether the disk is to be released together with the instance. | Valid values: true: The disk will be released when the instance is released. false: The disk will be retained when the instance is released. |

Response parameters Fn::GetAtt DiskId: the ID of the disk. Status: The Status of the disk. The name of the Device: disk. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DiskAttachment": {
      "Type": "ALIYUN::ECS::DiskAttachment",
        "InstanceId": {
          "Ref": "InstanceId"
```

`},`

```json
        "Device": {
          "Ref": "Device"
```

`},`

```json
        "DeleteWithInstance": {
          "Ref": "DeleteWithInstance"
```

`},`

```json
        "DiskId": {
          "Ref": "DiskId"
```

`},`

```json
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "The ID of the instance to attach the disk."
```

`},`

```json
    "Device": {
      "Type": "String",
      "Description": "The device where the volume is exposed on the instance. The device name cou
ld be /dev/xvd[a-z]. If this parameter is not specified, the default value will be used."
```

`},`

```json
    "DeleteWithInstance": {
      "Type": "Boolean",
      "Description": "If this parameter is set to true, the disk will be deleted while the instan
ce is deleted. If this parameter is set to false, the disk will be retained after the instance is deleted.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]` `},`

```json
    "DiskId": {
      "Type": "String",
      "Description": "The ID of the disk to be attached."
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
      "Description": "The device where the volume is exposed on the ECS instance.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "Device"
```

`]` `},`

```json
    "DiskId": {
      "Description": "The ID of the created disk.",
      "Value": {
        "Fn::GetAtt": [
          "DiskAttachment",
          "DiskId"
```

`]`

#### 5.1.8 ALIYUN::ECS::ForwardEntry

ALIYUN::ECS::ForwardEntry is used to configure the DNAT table of a NAT Gateway. Statement

```json
  "Type": "ALIYUN::ECS::ForwardEntry",
    "ExternalIp": String,
    "ExternalPort": String,
    "ForwardTableId": String,
    "InternalIp": String,
    "IpProtocol": String,
    "InternalPort": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ExternalIp | String | No | No | The public IP address of the NAT gateway. | It must be an IP address that is included in the shared NAT Gateway of the bandwidth plan to which the DNAT table belongs. |
| ExternalPort | String | No | No | The public port number. | Valid values: 1 to 65535. |
| ForwardTableId | String | No | No | The ID of the DNAT table. | None |
| InternalIp | String | No | No | The destination IP address to which the request is forwarded. | This IP address is a private IP address. |
| IpProtocol | String | No | No | The type of the protocol. | Valid values: TCP, UDP, and Any. |
| InternalPort | String | No | No | The destination private port. | Valid values: 1 to 65535. |

Response parameters Fn::GetAtt ForwardEntryId: the ID of each entry in the DNAT table. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ForwardEntry": {
      "Type": "ALIYUN::ECS::ForwardEntry",
        "ForwardTableId": "my_forwardtable",
        "ExternalIp": "101.201.XX.XX",
        "ExternalPort": "8080",
        "IpProtocol": "TCP",
        "InternalIp": "10.2.XX.XX",
        "InternalPort": "80"
```

`},`

```json
  "Outputs": {
    "ForwardEntryId": {
      "Value" : {"Fn::GetAttr": ["ForwardEntry","ForwardEntryId"]}
```

#### 5.1.9 ALIYUN::ECS::Instance

ALIYUN::ECS::Instance is used to create an ECS instance. Statement

```json
  "Type": "ALIYUN::ECS::Instance",
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
| PrivateIpAddress | String | Yes | Released | The private IP address of an ECS instance in a VPC. The specified IP address must not be used by other instances in the VPC. | None |

| Parameter |   | Type |   | Required | Editable |   | Description | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|
| InternetMaxBand widthIn |   | String |   | Optional | Released |   | The maximum inbound bandwidth from the Internet. | Valid values: 1 to 100. Default value: 100. Unit: Mbit/s. |   |
| IoOptimized |   | String |   | Yes | Released |   | Specifies whether an I/O optimized instance is created. | Valid values: none (non-I/O optimized) optimized Default value: none. |   |
| DiskMappings |   | List |   | Erased | Released |   | The data disks to be attached to the instance. | A maximum of 16 disks can be attached to each instance. |   |
| SystemDiskCateg ory |   | String |   | Yes | Released |   | The type of the system disk. | Valid values: cloud cloud efficiency _ cloud ssd _ ephemeral ssd _ |   |
| SystemDiskDescri ption |   | String |   | Yes | Released |   | The description of the ECS instance system disk. | None |   |
| SystemDiskDiskN ame |   | String |   | Yes | Released |   | The name of the ECS instance system disk. | None |   |
| SystemDiskSize |   | Number |   | No. | True |   | The size of the system disk. Unit: GB. | Valid values: 40 to 500. If a custom image is used to create a system disk, make sure that the size of the system disk is greater than that of the custom image. |   |
| Tags |   | List |   | Erased | Released |   | The custom tags | A maximum of 20 tags are supported. The format is as follows: [{&ldquo;Key”:”tagKey”,” |   |
|   |   |   |   |   |   |   |   |   | [{&ldquo;Key”:”tagKey”,” |
|   |   |   |   |   |   |   | of the instance. | Value”:”tagValue”}, |   |
|   |   |   |   |   |   |   |   | {&ldquo;Key”:”tagKey2”,”Va |   |
|   |   |   |   |   |   |   |   | lue”:”tagValue2”}] |   |
| UserData |   | String |   | Yes | Released |   | The user data that you provide when you create ECS instances. | The user data can be up to 16KB in size. You do not need to use Base64. you must use special characters. \ Escape. |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ZoneId | String | Yes | Released | The ID of the zone where the instance resides. | None |
| HpcClusterId | String | Yes | Released | The ID of the HPC cluster to which the ECS instance belongs. | None |
| VpcId | String | Yes | Released | The ID of the VPC to which the ECS instance belongs. | None |
| VSwitchId | String | Yes | Released | The ID of the VSwitch for the ECS instance. | None |
| KeyPairName | String | Yes | Released | The name of the key pair that is used to connect to created ECS instances. | For Windows-based instances, this parameter is empty by default. In the Linux, if this parameter is specified, the Password content is still set to the instance, but the Password logon method is disabled by default. The key pair is used to verify the logon. |
| RamRoleName | String | Yes | Released | The RAM role name of the instance. You can call the ListRoles operation to query the role name. | None |
| DeletionProtecti on | Boolean | Erased | Released | The release protection property of created instances. It specifies whether the instances can be released from the ECS console or through the DeleteInstance operation. | Valid values: True False |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
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

#### 5.1.10 ALIYUN::ECS::InstanceClone

ALIYUN::ECS::InstanceClone is used to clone an ECS instance. Statement

```json
  "Type": "ALIYUN::ECS::InstanceClone",
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

| esource Orchest | ration Servic | e |   |   | User Guide·Resource type |
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

#### 5.1.11 ALIYUN::ECS::InstanceGroup

ALIYUN::ECS::InstanceGroup is used to create an ECS instance group. Syntax

```json
  "Type": "ALIYUN::ECS::InstanceGroup",
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

#### 5.1.12 ALIYUN::ECS::InstanceGroupClone

ALIYUN::ECS::InstanceGroupClone is used to clone an ECS instance group. Statement

```json
  "Type": "ALIYUN::ECS::InstanceGroupClone",
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

| esource Orchestrat | ion Service |   |   |   | User Guide·Resource type |
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

#### 5.1.13 ALIYUN::ECS::Invocation

ALIYUN::ECS::Invocation is used to invoke a Cloud Assistant command for one or more ECS instances. Statement

```json
  "Type": "ALIYUN::ECS::Invocation",
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

`]` `},`

```json
    "Frequency": {
      "Type": "String",
      "Description": "The frequency of timing execution (the shortest frequency is performed ever
y 1 minute). It is mandatory when Timing is True.The value rule follows the rules of the cron exp ression. "
```

`},`

```json
    "CommandId": {
      "Type": "String",
      "Description": "The id of command."
```

`},`

```json
    "InstanceIds": {
      "Type": "CommaDelimitedList",
      "Description": "The instance id list. Select up to 20 instances at a time.Instances selecte
d network type must be VPC network, status must be running"
```

`},`

```json
  "Resources": {
    "Invocation": {
      "Type": "ALIYUN::ECS::Invocation",
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

#### 5.1.14 ALIYUN::ECS::JoinSecurityGroup

ALIYUN::ECS::JoinSecurityGroup is used to add one or more ECS instances to a specified security group. Syntax

```json
  "Type": "ALIYUN::ECS::JoinSecurityGroup",
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

Response parameters Fn::GetAtt Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::JoinSecurityGroup",
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

#### 5.1.15 ALIYUN::ECS::LaunchTemplate

ALIYUN::ECS::LaunchTemplate is used to create an ECS instance launch template. Syntax

```json
  "Type": "ALIYUN::ECS::LaunchTemplate",
    "LaunchTemplateName": String,
    "VersionDescription": String,
    "ImageId": String,
    "InstanceType": String,
    "SecurityGroupId": String,
    "NetworkType": String,
    "VSwitchId": String,
    "InstanceName": String,
    "Description": String,
    "InternetMaxBandwidthIn": Integer,
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
| LaunchTemplate Name | String | Yes | No | The name of the instance launch template. | The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| VersionDescriptio n | String | No | No | The description of the version of the instance launch template. | The description must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ImageId | String | No | No | The ID of the image. | None |
| InstanceType | String | No | No | The type of the instance. | None |
| SecurityGroupId | String | No | No | The ID of the security group. | None |
| NetworkType | String | No | No | The network type of the instance. | Valid values: classic vpc |
| VSwitchId | String | No | No | The ID of the VSwitch. You must specify this parameter when you create an instance in a VPC. | None |
| InstanceName | String | No | No | The name of the instance. | The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | No | No | The description of the instance. | The description must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| InternetMaxBand widthIn | Integer | No | No | Maximum inbound bandwidth from the Internet. | Valid values: 1 to 200. Unit: Mbit/s. |
| InternetMaxBand widthOut | Integer | No | No | Maximum outbound bandwidth to the Internet. | Valid values: 0 to 100. Unit: Mbit/s. |
| HostName | String | No | No | The hostname of the instance. | The name cannot start or end with a period (.) or a hyphen (-). It cannot contain consecutive periods (.) or hyphens (-). For Windows instances: The name must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot only contain digits. For other instances such as Linux instances: The name must be 2 to 64 characters in length and can contain letters, digits, and hyphens (-). |
| ZoneId | String | No | No | The ID of the zone where the instance resides. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SystemDiskCateg ory | String | No | No | The category of the system disk. | Valid values: cloud: the basic disk cloud efficiency: the _ ultra disk cloud ssd: the _ standard SSD ephemeral ssd: the _ local SSD |
| SystemDiskSize | Number | No | No | The size of the system disk. | Valid values: 20 to 500. Unit: GiB. |
| SystemDiskDiskN ame | String | No | No | The name of the system disk. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| SystemDiskDescri ption | String | No | No | The description of the system disk. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| IoOptimized | String | No | No | Specifies whether the instance is I/O optimized. | Valid values: none optimized |
| InternetChargeTy pe | String | No | No | The billing method for network usage. | Valid values: PayByBandwidth PayByTraffic |
| UserData | String | No | No | The user data of the instance. | The data must be encoded in Base64. The maximum size of the raw data is 16 KB. |

| Property | Type | Required | Editable | Description |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|
| KeyPairName | String | No | No | The AccessKey pair name. |   | For Windows instances, this parameter is ignored and is empty by default. The Password parameter takes effect even if the KeyPairName parameter is specified. For Linux instances, the username and password authentication method is disabled by default. |   |   |
| RamRoleName | String | No | No | The RAM role name of the instance. |   | None |   |   |
| AutoReleaseTim e | String | No | No | The time scheduled for the instance to be automatically released. |   | Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. |   |   |
|   |   |   |   |   |   |   | yyyy-MM- |   |
|   |   |   |   |   | e eased. | ddTHH:mm:ssZ |   |   |
| SpotStrategy | String | No | No | The preemption policy for pay-as-you-go instances. |   | This parameter takes effect only when the InstanceChargeType parameter is set to PostPaid. Valid values: NoSpot: The instance is created as a regular pay-as-you- go instance. SpotWithPriceLimit: The instance to be created is a preemptible instance with a user-defined maximum hourly price. SpotAsPriceGo: The instance to be created is a preemptible instance whose price is based on the market price at the time of purchase. |   |   |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SpotPriceLimit | String | No | No | The maximum hourly price of the instance. | A maximum of three decimal places can be specified. |
| SecurityEnhance mentStrategy | String | No | No | Specifies whether to enable security hardening. | Valid values: Active: enables security hardening. Deactive: disables security hardening. |
| DiskMappings | List | No | No | The list of data disks. | A maximum of 16 data disks can be specified. |
| NetworkInterfac es | List | No | No | The list of elastic network interfaces (ENIs). | A maximum of eight ENIs can be specified. |
| Tags | List | No | No | The tags of the instance, security group, disks, and ENIs. | A maximum of 20 tags can be specified. |
| TemplateTags | List | No | No | The tags of the launch template. | A maximum of 20 tags can be specified. |

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
| Category | String | No | No | The category of the data disk. | Valid values: cloud: the basic disk cloud efficiency: the _ ultra disk cloud ssd: the _ standard SSD ephemeral ssd: the _ local SSD |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskName | String | No | No | The name of the data disk. | The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| Description | String | No | No | The description of the data disk. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| SnapshotId | String | No | No | The ID of the snapshot used to create the data disk. | None |
| Size | String | No | No | The size of the system disk. | Valid values when the Category parameter is set to cloud: 5 to 2000. Valid values when the Category parameter is set to cloud efficiency: 20 _ to 32768. Valid values when the Category parameter is set to cloud ssd: 20 to _ 32768. Valid values when the Category parameter is set to ephemeral ssd: 5 to _ 800. Unit: GiB. |
| Encrypted | Boolean | No | No | Specifies whether to encrypt the data disk. | None |
| DeleteWithInstan ce | Boolean | No | No | Specifies whether to release the data disk when the instance is released. | None |

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
| PrimaryIpAddress | String | No | No | The primary private IP address of the ENI. | None |
| VSwitchId | String | No | No | The ID of the VSwitch to which the ENI belongs. | None |
| SecurityGroupId | String | No | No | The ID of the security group to which the ENI belongs. | None |
| NetworkInterfac eName | String | No | No | The name of the ENI. | None |
| Description | String | No | No | The description of the ENI. | The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

Tags syntax

```json
"Tags": [
    "Value": String,
    "Key": String
```

`]` Tags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| key | String | Yes | No | None | None |
| value | String | No | No | None | None |

TemplateTags syntax

```json
"TemplateTags": [
    "Value": String,
    "Key": String
```

`]` TemplateTags properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| key | String | Yes | No | None | None |
| value | String | No | No | None | None |

Response parameters Fn::GetAtt LaunchTemplateId: the ID of the instance launch template. LaunchTemplateName: the name of the instance launch template. DefaultVersionNumber: the default version number of the instance launch template. LatestVersionNumber: the latest version number of the instance launch template. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Template1": {
      "Type": "ALIYUN::ECS::LaunchTemplate",
        "LaunchTemplateName": "MyTemplate",
        "VersionDescription": "Launch template with all properties set",
        "ImageId": "m-2ze9uqi7wo61hwep****",
        "InstanceType": "ecs.n4.small",
        "SecurityGroupId": "sg-2ze8yxgempcdsq3i****",
        "NetworkType": "vpc",
        "VSwitchId": "vsw-2zei67xd9nhcqxzec****",
        "InstanceName": "InstanceName",
        "Description": "Description of template",
        "InternetMaxBandwidthIn": 100,
        "InternetMaxBandwidthOut": 200,
        "HostName": "tttinfo",
        "ZoneId": "cn-beijing-a",
        "SystemDiskCategory": "cloud_ssd",
        "SystemDiskSize": "40",
        "SystemDiskDiskName": "TheSystemDiskName",
        "SystemDiskDescription": "The system disk description",
        "IoOptimized": "optimized",
        "InternetChargeType": "PayByBandwidth",
        "UserData": "dGhpcyBpcyBhIHVzZXIgZGF0YSBleG1h****",
        "KeyPairName": "ThisIsKeyPair",
        "RamRoleName": "ThisIsRamRole",
        "AutoReleaseTime": "2050-10-01T00:00:00Z",
"SpotStrategy":"SpotWithPriceLimit",
```

```json
        SpotStrategy: SpotWithPriceLimit,
        "SpotPriceLimit": "100.001",
        "SecurityEnhancementStrategy": "Active",
        "DiskMappings": [
            "Category": "cloud_ssd",
            "Size": 40,
            "SnapshotId": "s-2ze1fr2bipove27b****",
            "Encrypted": true,
            "DiskName": "dataDisk1",
            "Description": "I am data disk 1",
            "DeleteWithInstance": true
```

`},`

```json
            "Category": "cloud_efficiency",
            "Size": 20,
            "SnapshotId": "s-2ze4k0w8b33mlsqu****",
            "Encrypted": false,
            "DiskName": "dataDisk2",
            "Description": "I am data disk 2",
            "DeleteWithInstance": true
```

`],`

```json
     "NetworkInterfaces": [
            "PrimaryIpAddress": "10.10.1.1",
            "VSwitchId": "vsw-2zetgeiqlemyok9z5****",
            "SecurityGroupId": "sg-2ze8yxgempcdsq3i****",
            "NetworkInterfaceName": "my-eni1",
            "Description": "My eni 1"
```

`},` `],`

```json
     "Tags": [
            "Key": "key1",
            "Value": "value1"
```

`},`

```json
            "Key": "key2",
            "Value": "value2"
```

`],`

```json
     "TemplateTags": [
            "Key": "templateKey1",
            "Value": "templateValue1"
```

`},`

```json
            "Key": "templateKey2",
            "Value": "templateValue2"
```

`]` `},`

```json
  "Outputs": {
      "LaunchTemplateId": {
          "Value": {"Fn::GetAtt": ["Template1","LaunchTemplateId"]}
```

`},`

```json
   "LaunchTemplateName": {
        "Value": {"Fn::GetAtt": ["Template1","LaunchTemplateName"]}
```

`},`

```json
   "DefaultVersionNumber": {
          "Value": {"Fn::GetAtt": ["Template1","DefaultVersionNumber"]}
```

`},`

```json
   "LatestVersionNumber": {
          "Value": {"Fn::GetAtt": ["Template1","LatestVersionNumber"]}
```

#### 5.1.16 ALIYUN::ECS::NatGateway

ALIYUN::ECS::NatGateway is used to create a NAT Gateway for a VPC. Statement

```json
  "Type": "ALIYUN::ECS::NatGateway",
    "DeletionProtection": Boolean,
    "VpcId": String,
    "Description": String,
    "NatGatewayName": String,
    "VSwitchId": String,
    "DeletionForce": Boolean,
    "Spec": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VpcId | String | Yse | No | The ID of the VPC that you want to create NAT Gateway. | None |
| VSwitchId | String | Yse | No | The ID of the vSwitch in the specified VPC. | None |
| Description | String | Erased | Released | The description of the NAT Gateway. | The description must be 2 to 256 characters in length. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NatGatewayNa me | String | Erased | Released | The name of the NAT Gateway. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ periods (.), and hyphens (-). It must start with a letter. |
| Spec | String | Erased | Released | The type of the NAT Gateway. | Valid values: Small,Middle, and Large. |
| DeletionProtecti on | Boolean | Erased | Released | Indicates whether deletion protection is enabled. Default value: false. | None |
| DeletionForce | Boolean | Erased | Released | Specifies whether to forcibly delete SNAT and DNAT entries in the Gateway and unbind EIP from the NAT gateway. Default value: false. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt ForwardTableId: the ID of the port forwarding table. The ID of the SNatTableId:SNat source network address translation table. NatGatewayId: the unique ID of the Nat gateway. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "NatGateway": {
      "Type": "ALIYUN::ECS::NatGateway",
        "NatGatewayName": "nat_gateway_1",
        "Description": "my nat gateway",
        "VpcId": "vpc-25o8s****",
        "VSwitchId": "vsw-25rc1****",
        "Spec": "Small"
```

`},`

```json
  "Outputs": {
    "NatGatewayId": {
         "Value": {"Fn::GetAttr": ["NatGateway","NatGatewayId"]}
```

`},`

```json
    "ForwardTableId": {
         "Value": {"Fn::GetAttr": ["NatGateway","ForwardTableId"]}
```

`},`

```json
    "SNatTableId": {
         "Value": {"Fn::GetAttr": ["NatGateway", "SNatTableId"]}
```

#### 5.1.17 ALIYUN::ECS::NetworkInterface

ALIYUN::ECS::NetworkInterface is used to create an elastic network interface (ENI). Statement

```json
  "Type": "ALIYUN::ECS::NetworkInterface",
    "Description": String,
    "SecurityGroupId": String,
    "PrimaryIpAddress": String,
    "ResourceGroupId": String,
    "VSwitchId": String,
    "NetworkInterfaceName": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | No | Yes | The ID of the security group to which the instance belongs. The security group and the instance must be in the same VPC. | None |
| VSwitchId | String | No | No | The ID of the VSwitch in the VPC. | None |
| Description | String | Yes | True | The description of the ENI. It can contain 2 to 256 English letters or Chinese character. It cannot start with http:// and https:// the beginning. This parameter is empty by default. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NetworkInterfa ceName | String | Yes | True | The name of the ENI. The name must be 2 to 128 characters in length Must start with an uppercase or lowercase letter, and cannot start with http:// and https:// the beginning. It can contain letters, digits, colons (:), underscores ( ), _ and hyphens (- ). Default value: null. | None |
| PrimaryIpAddre ss | String | Yes | Released | The primary private IP address of the ENI. The specified IP address must be available within the CIDR block of the VSwitch. If this parameter is not specified, an available IP address in the VSwitch CIDR block is assigned at random. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt NetworkInterfaceId: the ID of the ENI. The MAC address of the MacAddress: Elastic Network Interface. The private IP address of the PrivateIpAddress: Elastic Network Interface. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "Description": {
      "Type": "String",
      "Description": "Description of your ENI. It is a string of [2, 256] English or Chinese char
acters."
```

`},`

```json
    "SecurityGroupId": {
      "Type": "String",
      "Description": "The ID of the security group that the ENI joins. The security group and the
ENI must be in a same VPC."
```

`},`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "VSwitch ID of the specified VPC. Specifies the switch ID for the VPC."
```

`},`

```json
    "NetworkInterfaceName": {
      "Type": "String",
      "Description": "Name of your ENI. It is a string of [2, 128]  Chinese or English characters
. It must begin with a letter and can contain numbers, underscores (_), colons (:), or hyphens (- )."
```

`},`

```json
    "PrimaryIpAddress": {
      "Type": "String",
      "Description": "The primary private IP address of the ENI.  The specified IP address must h
ave the same Host ID as the VSwitch. If no IP addresses are specified, a random network ID is ass igned for the ENI."
```

`},`

```json
  "Resources": {
    "EniInstance": {
      "Type": "ALIYUN::ECS::NetworkInterface",
        "Description": {
          "Ref": "Description"
```

`},`

```json
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
        "NetworkInterfaceName": {
          "Ref": "NetworkInterfaceName"
```

`},`

```json
        "PrimaryIpAddress": {
          "Ref": "PrimaryIpAddress"
```

`},`

```json
  "Outputs": {
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniInstance",
          "NetworkInterfaceId"
```

`]`

#### 5.1.18 ALIYUN::ECS::NetworkInterfaceAttachment

ALIYUN::ECS::NetworkInterfaceAttachment is used to attach an elastic network interface (ENI) to an instance in a VPC. Statement

```json
  "Type": "ALIYUN::ECS::NetworkInterfaceAttachment",
    "InstanceId": String,
    "NetworkInterfaceId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | No | No | The ID of the RDS instance. | None |
| NetworkInterfa ceId | String | No | No | The IDs of the elastic network interfaces (ENIs). | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt NetworkInterfaceId: the ID of the ENI. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "InstanceId": {
      "Type": "String",
      "Description": "ECS instance id"
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
        "InstanceId": {
          "Ref": "InstanceId"
```

`},`

```json
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
```

`},`

```json
  "Outputs": {
    "NetworkInterfaceId": {
      "Description": "ID of your Network Interface.",
      "Value": {
        "Fn::GetAtt": [
          "EniAttachment",
          "NetworkInterfaceId"
```

`]`

#### 5.1.19 ALIYUN::ECS::NetworkInterfacePermission

ALIYUN::ECS::NetworkInterfacePermission is used to grant an account the permission to attach an elastic network interface (ENI) to an instance. Syntax

```json
  "Type": "ALIYUN::ECS::NetworkInterfacePermission",
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
    "NetworkInterfaceId": {
      "Type": "String",
      "Description": "Network interface id"
```

`},`

```json
  "Resources": {
    "EniPermission": {
      "Type": "ALIYUN::ECS::NetworkInterfacePermission",
        "AccountId": {
          "Ref": "AccountId"
```

`},`

```json
        "Permission": {
          "Ref": "Permission"
```

`},`

```json
        "NetworkInterfaceId": {
          "Ref": "NetworkInterfaceId"
```

`},`

```json
  "Outputs": {
    "NetworkInterfacePermissionId": {
      "Description": "the network interface permission id",
      "Value": {
        "Fn::GetAtt": [
          "EniPermission",
          "NetworkInterfacePermissionId"
```

`]`

#### 5.1.20 ALIYUN::ECS::Route

ALIYUN::ECS::Route is used to create a custom route. Syntax

```json
  "Type": "ALIYUN::ECS::Route",
    "DestinationCidrBlock": String,
    "RouteTableId": String,
    "NextHopId": String,
    "NextHopType": String,
    "RouteId": String,
    "NextHopList": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestinationCidrBl ock | String | Yes | No | The destination Classless Inter-Domain Routing (CIDR) block of the route entry. | None |
| RouteTableId | String | Yes | No | The ID of the route table. | None |
| NextHopId | String | No | No | The ID of the next-hop instance of the route entry. | The route is a non-ECMP route. |
| RouteId | String | Yes | No | The ID of the route. | None |
| NextHopType | String | No | No | The type of the next hop. | Default value: Instance. Valid values: Instance Tunnel HaVip RouterInterface |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NextHopList | List | No | No | The list of next hops of the route entry. | You must specify the NextHopType and NextHopId parameters to specify the next hops. If you specify the NextHopList parameter, the route is an ECMP route. The list contains two to four next hops of the ECMP route entry. Not e The NextHopList parameter can be specified only when the route entry belongs to a VRouter. In addition, the next hops must be the router interfaces pointing to the connected VBRs. If you do not specify the NextHopList parameter, the route is a non-ECMP route. |

NextHopList syntax

```json
"NextHopList": [
    "NextHopId": String,
    "NextHopType": String
```

`]` NextHopList properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NextHopId | String | Yes | No | The ID of the next-hop instance of the route entry. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| NextHopType | String | No | No | The type of the next hop. | Default value: RouterInterface. Valid values: Instance Tunnel HaVip RouterInterface |

Response parameters Fn::GetAtt Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ECSRoute": {
      "Type": "ALIYUN::ECS::Route",
 "RouteId": "vrt-25mz0****",
        "RouteTableId": "vtb-25oud****",
        "DestinationCidrBlock": "172.16.XX.XX/24",
        "NextHopId": "i-25xzy****"
```

#### 5.1.21 ALIYUN::ECS::SNatEntry

ALIYUN::ECS::SNatEntry is used to configure a NAT Gateway table in a source network address translation. Statement

```json
  "Type": "ALIYUN::ECS::SNatEntry",
    "SNatTableId": String,
    "SNatIp": String,
    "SourceVSwitchId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SNatTableId | String | Retained | Yes | The ID source network address translation table. | None |
| SNatIp | String | Retained | Yes | The public IP address used to source network address translation. | The public IP address must be NAT Gateway in the bandwidth plan. It cannot exist in both the forwarding table and the SNAT table. |
| SourceVSwitchId | String | Retained | Yes | The ID of the VSwitch that accesses the Internet through the SNAT function of NAT Gateway. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt SNatEntryId: the table entry ID in the source network address translation table. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SNatEntry": {
      "Type": "ALIYUN::ECS::SNatEntry",
        "SNatTableId": "stb-3er41****",
        "SourceVSwitchId": "vsw-25rc1****",
        "SNatIp": "101.201.XX.XX"
```

`},`

```json
  "Outputs": {
    "SNatEntryId": {
         "Value": {"Fn::GetAttr": ["SNatEntry","SNatEntryId"]}
```

#### 5.1.22 ALIYUN::ECS::SecurityGroup

ALIYUN::ECS::SecurityGroup is used to create a security group. Statement

```json
  "Type": "ALIYUN::ECS::SecurityGroup",
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

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |
| VpcId | String | Yes | Released | The ID of the VPC. | None |
| Description | String | Yes | Released | The description of the new security group. | The description must be 2 to 256 characters in length. |
| Tags | List | Erased | Released | The tags of the security group. | A maximum of 20 tags can be specified. |

| Parameter | Type | Required | Editable | Description |   | Constraint |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| SecurityGroupN ame | String | Yes | Released | The name of the new security group. |   | Default value: empty. The name must be 2 to 128 characters in length Must start with an uppercase or lowercase letter, and cannot start with http: // and h |   |   |   |
|   |   |   |   |   |   |   | http: |   |   |
|   |   |   |   |   |   | // | and | h |   |
|   |   |   |   |   |   | ttps:// the beginning. It must start with a letter and cannot start with http:// or https://. |   |   |   |
| SecurityGroupE gress | List | Erased | Released | The outbound access rules of the security group. |   | None |   |   |   |
| SecurityGroupIn gress | List | Erased | Released | The inbound access rules of the security group. |   | None |   |   |   |
| SecurityGroupT ype | String | Yes | Released | The type of the new security group. |   | Valid values: normal (basic security group) enterprise (Advanced Security Group) |   |   |   |

Tags syntax

```json
"Tags": [
    "Value" : String,
    "Key" : String
```

`]` Tags properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | No | No | None | None |
| Value | String | Yes | Released | None | None |

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
    "DestGroupOwnerAccount": String,
    "DestGroupOwnerId": String,
    "Ipv6DestCidrIp": String
```

`]` SecurityGroupEgress properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the security group rule. | The description must be 1 to 512 characters in length. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestGroupOwn erId | String | Yes | Released | The ID of the Alibaba Cloud account that owns the destination security group. This parameter is used to grant the current security group access to security groups in another Alibaba Cloud account. | If neither the DestGroupOwn erId parameter nor the DestGroupOwn erAccount parameter is specified, the current security group is granted access to other security groups in the same Alibaba Cloud account. If the DestCidrIp parameter is specified, the DestGroupOwn erId parameter is ignored. |
| IpProtocol | String | No | No | The Internet protocol over which the listener will forward requests. | Valid values: TCP udp icmp GRE All A value of all specifies that all the four protocols are supported. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortRange | String | Yes | Released | The range of port numbers corresponding to the Internet protocol. | The range of destination ports corresponding to the transport layer protocol. Valid values: When the IpProtocol parameter is set to tcp or udp, the port number range is 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to gre, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to all, the port number range is -1/- |

| Parameter | Type | Required | Editable | Description | 1. Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | Yes | Released | The ID of the security group for which to create the outbound access rules. | None |
| NicType | String | Yes | Released | The network type of the instance. Valid values: | Valid values: internet intranet Default value: internet. |
| Priority | String | Optional | Released | The priority of the authorization policy. | Valid values: 1 to 100. Default value: 1 |
| DestGroupId | String | Yes | Released | The ID of the destination security group within the same region. | You must specify either the DestGroupId parameter or the DestCidrIp parameter. If both parameters are specified, the system authorizes the destination CIDR block specified by the DestCidrIp parameter. If the DestGroupId parameter is specified, but the DestCidrIp parameter is |
|   |   |   |   |   | not, you must set the NicType parameter to intranet. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestCidrIp | String | Yes | Released | The source IPv4 CIDR block. | The value must be in CIDR format. The default value is 0.0.0.0/0, indicating that access from any IP addresses is allowed. Examples of other supported formats include 10.159.XX. XX/12. Only IPv4 addresses are supported. |
| Policy | String | Yes | Released | The authorization policy. | Valid values: accept: grants access drop: denies access Default value: accept. |
| DestGroupOwn erAccount | String | Yes | Released | The Alibaba Cloud account of the destination security group when you grant security group permissions across accounts. | None |
| Ipv6DestCidrIp | String | Yes | Released | The destination IPv6 CIDR block. | IPv6 addresses in CIDR format are supported. You can only specify the IP addresses for ECS instances in VPCs. |

SecurityGroupIngress syntax

```json
"SecurityGroupIngress": [
    "SourceGroupOwnerId": String,
    "SourceGroupOwnerAccount": String,
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

`]` SecurityGroupIngress properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupOw nerId | String | Yes | Released | The ID of the Alibaba Cloud account that owns the source security group. | None |
| Description | String | Yes | Released | The description of the security group rule. | The description must be 1 to 512 characters in length. |
| IpProtocol | String | No | No | The Internet protocol over which the listener will forward requests. | Valid values: tcp, udp, icmp, gre, and all. A value of all specifies that all the four protocols are supported. |
|   |   |   |   |   | The range of destination ports corresponding to the transport layer protocol. Valid values: When the IpProtocol parameter is set to tcp or udp, the port number |

|   |   |   |   |   | range is 1 to |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | Description | Constraint 65535. |
| PortRange | String | Yes | Released | The range of port numbers corresponding to the Internet protocol. | Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to gre, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to all, the port number range is -1/- 1, indicating that all ports are available. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupId | String | Yes | Released | The ID of the source security group within the same region. | You must specify either the SourceGroupId parameter or the SourceCidrIp parameter. If both parameters are specified, the system authorizes the source CIDR block specified by the SourceCidrIp parameter. If the SourceGroupId parameter is specified, but the SourceCidrIp parameter is not, you must set the NicType parameter to intranet. |
| SecurityGroupId | String | Yes | Released | The ID of the security group for which you want to create the inbound access rule. | None |
| NicType | String | Yes | Released | The network type of the instance. Valid values: | Valid values: internet intranet Default value: internet. |
| SourceGroupOw nerAccount | String | Yes | Released | The Alibaba Cloud account of the destination security group when you grant security group permissions across accounts. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Priority | String | Optional | Released | The priority of the authorization policy. | Valid values: 1 to 100. Default value: 1 |
| SourceCidrIp | String | Yes | Released | The source IPv4 CIDR block. | The value must be in CIDR format. The default value is 0.0.0.0/0, indicating that access from any IP addresses is allowed. Examples of other supported formats include 10.159.XX. XX/12. Only IPv4 CIDR blocks are supported. |
| Policy | String | Yes | Released | The authorization policy. | Valid values: accept: accepts the request. drop: access is denied. Default value: accept. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourcePortRang e | String | Yes | Released | The range of source ports relevant to transport layer protocols. | Valid values: When the IpProtocol parameter is set to tcp or udp, the port number range is 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1, indicating that all values are valid. When the IpProtocol parameter is set to gre, the port number range is -1/- 1, indicating that all ports are available. The IpProtocol value is all:- 1/-1. |
| Ipv6SourceCidrI p | String | Yes | Released | The source IPv6 CIDR block. IPv6 addresses in CIDR format are supported. | You can only specify the IP addresses of ECS instances in VPCs. |

Response parameters Fn::GetAtt SecurityGroupId: the ID of the new security group. Sample request

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "SG": {
      "Type": "ALIYUN::ECS::SecurityGroup",
        "SecurityGroupName": {
          "Ref": "SecurityGroupName"
```

`},`

```json
        "SecurityGroupIngress": [
            "SourceCidrIp": "0.0.0.0/0",
            "IpProtocol": "all",
            "NicType": "internet",
            "PortRange": "-1/-1",
            "Priority": 1
```

`},`

```json
            "SourceCidrIp": "0.0.0.0/0",
            "IpProtocol": "all",
            "NicType": "intranet",
            "PortRange": "-1/-1",
            "Priority": 1
```

`],`

```json
        "SecurityGroupEgress": [
            "IpProtocol": "all",
            "DestCidrIp": "0.0.0.0/0",
            "NicType": "internet",
            "PortRange": "-1/-1",
            "Priority": 1
```

`},`

```json
            "IpProtocol": "all",
            "DestCidrIp": "0.0.0.0/0",
            "NicType": "intranet",
            "PortRange": "-1/-1",
            "Priority": 1
```

`],`

```json
        "VpcId": {
          "Ref": "Vpc"
```

`},`

```json
  "Outputs": {
    "SecurityGroupId": {
      "Value" : {"Fn::GetAtt": ["SG","SecurityGroupId"]}
```

#### 5.1.23 ALIYUN::ECS::SecurityGroupClone

ALIYUN::ECS::SecurityGroupClone is used to clone a security group. Syntax

```json
  "Type": "ALIYUN::ECS::SecurityGroupClone",
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
| NetworkType | String | No | No | The network type of the new security group. | Set the value to Classic. |
| VpcId | String | No | No | The ID of the VPC to which the new security group belongs. | The NetworkType parameter is ignored if both the VpcId and NetworkType parameters are specified. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | No | No | The description of the new security group. | The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |
| SecurityGroupN ame | String | No | No | The name of the new security group. | This parameter is empty by default. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. |
| DestinationRegi onId | String | No | No | The ID of the destination region where the new security group resides. | Default value: CURRENT. |
| SecurityGroupT ype | String | No | No | The type of the new security group. | Valid values: normal and enterprise. A value of normal specifies a basic security group. A value of enterprise specifies an advanced security group. |

Response parameters Fn::GetAtt SecurityGroupId: the ID of the new security group. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SecurityGroupClone": {
```

```json
      "Type": "ALIYUN::ECS::SecurityGroupClone",
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
      "Description": "Source security group ID is used to copy properties to clone new security g
roup. If the NetworkType and VpcId is not specified, the same security group will be cloned. If N etworkType or VpcId is specified, only proper security group rules will be cloned."
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
      "Description": "Description of the security group, [2, 256] characters. Do not fill or empt
y, the default is empty."
```

`},`

```json
    "SecurityGroupName": {
      "Type": "String",
      "Description": "Display name of the security group, [2, 128] English or Chinese characters,
must start with a letter or Chinese in size, can contain numbers, '_' or '.', '-'"
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
      "Description": "Clone new security group as classic network type. If the VpcId is specified
, the value will be ignored.",
      "AllowedValues": [
        "Classic"
```

`]` `},`

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

#### 5.1.24 ALIYUN::ECS::SecurityGroupEgress

ALIYUN::ECS::SecurityGroupEgress is used to create an outbound access rule for a security group. Statement

```json
  "Type": "ALIYUN::ECS::SecurityGroupEgress",
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

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IpProtocol | String | No | No | The transport layer protocol. | Valid values: tcp, udp, icmp, gre, and all. A value of all specifies that all the four protocols are supported. |
|   |   |   |   |   | Valid values: When the IpProtocol parameter is set to tcp or udp, the port |

| esource Orchestr | ation Service |   |   | User Gui | de·Resource type |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | Description | number Constraint range is 1 to |
| PortRange | String | No | No | The range of destination ports relevant to transport layer protocols. | 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to gre, the port number range is -1/- 1, indicating that all ports are available. When the IpProtocol parameter is set to all, the port number range is -1/- 1, indicating that all ports are available. For more information about the application scenarios of the ports, see Typical applications of commonly used ports. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SecurityGroupId | String | Yes | Released | The ID of the source security group. | None |
| NicType | String | Yes | Released | The type of the ENI. | Valid values: Network interface controller intranet Default value: internet. If the DestGroupId parameter is specified, but the DestCidrIp parameter is not, this parameter must be set to intranet. |
| Priority | String | Optional | Released | The priority of the security group rule. | Valid values: 1 to 100. Default value: 1 |
| DestGroupId | String | Yes | Released | The ID of the source security group for which you want to set access permissions. | You must specify at least one of the DestGroupId and DestCidrIp parameters. If the DestGroupId parameter is specified, but the DestCidrIp parameter is not, the NicType parameter must be set to intranet. If both the DestGroupId and DestCidrIp parameters are specified, the DestCidrIp parameter prevails by default. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestCidrIp | String | Yes | Released | The destination CIDR block. | Only IPv4 CIDR blocks are supported. |
| Policy | String | Yes | Released | The authorization policy. | Valid values: accept: grants access drop: denies access Default value: accept. |
| DestGroupOwn erAccount | String | Yes | Released | The Alibaba Cloud account that manages the destination security group when you set a security group rule across accounts. | If neither the DestGroupOwn erAccount parameter nor the DestGroupOwn erId parameter is specified, the access permission is configured on another security group managed by your account. If the DestCidrIp parameter is specified, this parameter is ignored. |
| Description | String | Yes | True | The description of the security group rule. | The description must be 1 to 512 characters in length. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DestGroupOwn erId | String | Yes | Released | The ID of the Alibaba Cloud account that manages the destination security group when you set a security group rule across accounts. | If neither the DestGroupOwn erId parameter nor the DestGroupOwn erAccount parameter is specified, the access permission is configured on another security group managed by your account. If the DestCidrIp parameter is specified, the DestGroupOwn erId parameter is ignored. |
| Ipv6DestCidrIp | String | Yes | Released | The destination IPv6 CIDR block. | IPv6 CIDR blocks are supported. You can only specify the IP addresses of ECS instances in VPCs. |

Response parameters Fn::GetAtt Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
        "SecurityGroupId": "sg-25bow****",
        "IpProtocol": "tcp",
        "PortRange": "65535/65535",
        "DestCidrIp": "0.0.0.0/0"
```

#### 5.1.25 ALIYUN::ECS::SecurityGroupIngress

ALIYUN::ECS::SecurityGroupIngress is used to create an inbound access rule for a security group. Syntax

```json
  "Type": "ALIYUN::ECS::SecurityGroupIngress",
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
| IpProtocol | String | Yes | No | The Internet protocol. | Valid values: tcp, udp, icmp, gre, and all. A value of all specifies that all the four protocols are supported. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| PortRange | String | Yes | No | The range of destination ports relevant to transport layer protocols. | When the IpProtocol parameter is set to tcp or udp, the port number range is 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1. When the IpProtocol parameter is set to gre, the port number range is -1/- 1. When the IpProtocol parameter is set to all, the port number range is -1/- 1. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupId | String | No | No | The ID of the source security group for which you want to set access permissions. | You must specify at least one of the SourceGroupId and SourceCidrIp parameters. If the SourceGroupId parameter is specified, but the SourceCidrIp parameter is not, the NicType parameter must be set to intranet. If both the SourceGroupId and SourceCidrIp parameters are specified, the SourceCidrIp value is used by default. |
| SecurityGroupId | String | No | No | The ID of the security group for which you want to create the inbound access rule. | None |
| NicType | String | No | No | The network type of the instance. | Valid values: internet intranet Default value: internet. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupOw nerAccount | String | No | No | The Alibaba Cloud account that manages the source security group when you set a security group rule across accounts. | If neither the SourceGroupO wnerAccount parameter nor the SourceGroupO wnerId parameter is specified, the access permission is configured for another security group managed by your account. If the SourceCidrIp parameter is specified, this parameter is ignored. |
| Priority | Integer | No | No | The priority of the security group rule. | Valid values: 1 to 100. Default value: 1. |
| SourceCidrIp | String | No | No | The source IPv4 CIDR block. | Only IPv4 CIDR blocks are supported. |
| Policy | String | No | No | The access control policy. | Valid values: accept: grants access. drop: denies access. Default value: accept. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourceGroupOw nerId | String | No | No | The ID of the Alibaba Cloud account that manages the source security group when you set a security group rule across accounts. | If neither the SourceGroupO wnerId parameter nor the SourceGroupO wnerAccount parameter is specified, the access permission is configured for another security group managed by your account. If the SourceCidrIp parameter is specified, this parameter is ignored. |
| Description | String | No | Yes | The description of the security group rule. | The description must be 1 to 512 characters in length. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SourcePortRang e | String | No | No | The range of source ports relevant to transport layer protocols. | When the IpProtocol parameter is set to tcp or udp, the port number range is 1 to 65535. Separate the starting port and the ending port with a forward slash (/). Correct example: 1/200. Incorrect example: 200/1. When the IpProtocol parameter is set to icmp, the port number range is -1/- 1. When the IpProtocol parameter is set to gre, the port number range is -1/- 1. When the IpProtocol parameter is set to all, the port number range is -1/- 1. |
| Ipv6SourceCidrI p | String | No | No | The range of source IPv6 addresses. | CIDR blocks and IPv6 addresses are supported. You can only specify the IP addresses of ECS instances in VPCs. |

Response parameters Fn::GetAtt Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SG": {
      "Type": "ALIYUN::ECS::SecurityGroupIngress",
        "SecurityGroupId": "sg-25bow****",
        "IpProtocol": "tcp",
        "PortRange": "65535/65535",
        "SourceCidrIp": "0.0.0.0/0"
```

#### 5.1.26 ALIYUN::ECS::Snapshot

ALIYUN::ECS::Snapshot is used to create a disk Snapshot. Statement

```json
  "Type": "ALIYUN::ECS::Snapshot",
    "SnapshotName": String,
    "Timeout": Integer,
    "Description": String,
    "DiskId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DiskId | String | No | No | The ID of the disk for which you want to create the snapshot. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SnapshotName | String | Yes | Released | The name of the snapshot. | It must be 2 to 128 characters in length. And can contain letters, digits, underscores ( ), _ and hyphens (- ). It cannot start with auto. Snapshot names starting with auto are reserved for automatic snapshots. It cannot start with http:// or https:// . |
| Timeout | String | Optional | Released | The timeout period that is specified for the snapshot creation request. | If this parameter is set, the timeout period to create a resource stack is prolonged. If the snapshot is not created within the specified time period, the entire resource stack fails to be created. You must set the timeout period according to the disk size and data amount. Valid values: 200 to 1440. Unit: minute. The default value is 200 minutes. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | Released | The description of the snapshot. | The length must be 2 to 256 characters in length. This parameter is empty by default. It cannot start with http:// or https:// . |

Response parameters Fn::GetAtt SnapshotId: the ID of the snapshot. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Snapshot": {
      "Type": "ALIYUN::ECS::Snapshot",
        "DiskId": "d-2zedgvuvu8cylvrd****"
```

`},`

```json
  "Outputs": {
    "SnapshotId": {
      "Value": {
        "Fn::GetAtt": [
          "Snapshot",
          "SnapshotId"
```

`]`

#### 5.1.27 ALIYUN::ECS::SSHKeyPair

ALIYUN::ECS::SSHKeyPair is used to create or import an SSH key pair to an ECS instance. Statement

```json
  "Type": "ALIYUN::ECS::SSHKeyPair",
    "ResourceGroupId": String,
    "KeyPairName": String,
    "PublicKeyBody": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |
| KeyPairName | String | No | No | The globally unique name of the SSH key pair. | The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It cannot start with http:// or https:// . |
| PublicKeyBody | String | Yes | Released | Specifies the SSH public key to import. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt KeyPairFingerPrint: the fingerprint of the key pair. The message-digest algorithm 5 (MD5) is used based on the public key fingerprint format defined in RFC 4716. PrivateKeyBody: the private key of the key pair. An unencrypted RSA private key must be encoded using PEM and must be in the PKCS#8 format. The private key of a key pair can only be obtained at the time of its creation. If you import an existing public key, no private key information will be available. KeyPairName: the globally unique name of the SSH key pair. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SSHKeyPair": {
      "Type": "ALIYUN::ECS::SSHKeyPair",
        "KeyPairName": "ssh_key_pair_v1"
```

`},`

```json
  "Outputs": {
    "KeyPairName": {
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "KeyPairName"
```

`]` `},`

```json
    "PrivateKeyBody": {
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "PrivateKeyBody"
```

`]` `},`

```json
    "KeyPairFingerPrint": {
      "Value": {
        "Fn::GetAtt": [
          "SSHKeyPair",
          "KeyPairFingerPrint"
```

`]`

#### 5.1.28 ALIYUN::ECS::SSHKeyPairAttachment

ALIYUN::ECS::SSHKeyPairAttachment is used to bind an SSH key pair to an ECS instance. Statement

```json
  "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
    "InstanceIds": List,
    "KeyPairName": String
```

Properties

| Parameter | Type | Required or Not | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceIds | List | Retained | Yes | The IDs of the ECS instances with which you want to associate the EIP. | Separate the IDs with a comma (,). Only Linux instances are supported. |
| KeyPairName | String | No | No | The name of the SSH key pair. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "SSHKeyPairAttachment": {
      "Type": "ALIYUN::ECS::SSHKeyPairAttachment",
        "KeyPairName": "ssh_key_pair_v1",
        "InstanceIds": [
          'I-2zeiofnh20hj**** has been added * ',
          'I-2zebt3kfvxm2**** has two records *'
```

`]`

#### 5.1.29 ALIYUN::ECS::VPC

ALIYUN::ECS::VPC is used to create a VPC. Statement

```json
  "Type": "ALIYUN::ECS::VPC",
    "Description": String,
    "Ipv6CidrBlock": String,
    "EnableIpv6": Boolean,
    "ResourceGroupId": String,
    "VpcName": String,
    "CidrBlock": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |   |   |   |
|---|---|---|---|---|---|---|---|---|
| ResourceGroupI d | String | Yes | Released | The ID of the resource group to which the instance belongs. | None |   |   |   |
| VpcName | String | Yes | True | The name of the VPC. | The name must be 2 to 128 characters in length Must start with english letters or starts with a Chinese character. It cannot start with h ttp:// or https:// . It must start with a letter and cannot start with http:// or https://. |   |   |   |
|   |   |   |   |   |   |   | h |   |
|   |   |   |   |   |   | ttp:// |   |   |
| CidrBlock | String | Yes | True | The CIDR block of the VPC. | Valid values: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. |   |   |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | True | The description of the VPC. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| Ipv6CidrBlock | String | Yes | Released | The IPv6 CIDR block of the VPC. | None |
| EnableIpv6 | Boolean | No. | True | Specifies whether to enable an IPv6 CIDR block. | Valid values: true false Default value: false. |

Response parameters Fn::GetAtt VpcId: The VPC ID allocated by the system. VRouterId: the ID of the vRouter. RouteTableId: the ID of the routing table. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "EcsVpc": {
      "Type": "ALIYUN::ECS::VPC",
        "CidrBlock": "172.16.0.0/12",
        "VpcName": "vpc-test-del"
```

`},`

```json
  "Outputs": {
    "VpcId": {
      "Value": {
        "Fn::GetAtt": [
          "EcsVpc",
          "VpcId"
```

`]` `},`

```json
    "VRouterId": {
      "Value": {
        "Fn::GetAtt": [
          "EcsVpc",
          "VRouterId"
```

`]` `},`

```json
    "RouteTableId": {
      "Value": {
        "Fn::GetAtt": [
          "EcsVpc",
          "RouteTableId"
```

`]`

#### 5.1.30 ALIYUN::ECS::VSwitch

ALIYUN::ECS::VSwitch is used to create a VSwitch. Statement

```json
  "Type": "ALIYUN::ECS::VSwitch",
    "VSwitchName": String,
    "VpcId": String,
    "Description": String,
    "Ipv6CidrBlock": Integer,
    "ZoneId": String,
    "CidrBlock": String
```

Properties

| Parameter | Type | Required | Editable | Description |   | Constraint |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| VpcId | String | No | No | The ID of the VPC where a vSwitch is to be created |   | None |   |   |   |   |
| ZoneId | String | No | No | The ID of the zone where the instance resides. |   | None |   |   |   |   |
| VSwitchName | String | Yes | True | The name of the VSwitch. |   | The name must be 2 to 128 characters in length It must start with a letter. Cannot htt p:// or h |   |   |   |   |
|   |   |   |   |   |   |   |   | htt |   |   |
|   |   |   |   |   |   | p:// |   |   | h |   |
|   |   |   |   |   |   | ttps:// the beginning. It must start with a letter and cannot start with http:// or https://. | ttps:// |   |   |   |
| CidrBlock | String | No | No | The CIDR block of the VSwitch. |   | The VSwitch CIDR block must be a subset of the CIDR block assigned to the VPC where the VSwitch resides and not be used by other VSwitches. |   |   |   |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Description | String | Yes | True | The description of the vSwitch. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |
| Ipv6CidrBlock | String | Optional | Released | The IPv6 CIDR block of the VSwitch. You can customize the last eight bits of the IPv6 CIDR block. | Valid values: 0 to 255. The value is a decimal integer. By default, the prefix of the IPv6 CIDR block of the VSwitch is set to /64. |

Response parameters Fn::GetAtt VSwitchId: indicates the vSwitch ID allocated by the system. CidrBlock: the IPv4 CIDR block of the vSwitch. Ipv6CidrBlock: the IPv6 CIDR block of the vSwitch. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "VpcName": {
      "Type": "String"
```

`},`

```json
    "VSwitch1CidrBlock": {
      "Type": "String",
      "Default": "172.16.100.0/24"
```

`},`

```json
    "VSwitch2CidrBlock": {
        "Type": "String",
        "Default": "172.16.80.0/24"
```

`},`

```json
  "Resources": {
    "EcsVpc": {
      "Type": "ALIYUN::ECS::VPC",
        "CidrBlock": "172.16.0.0/12",
        "VpcName": {"Ref": "VpcName"},
```

`},` `},`

```json
    "VSwitch1": {
      "Type": "ALIYUN::ECS::VSwitch",
```

```json
        "ZoneId": "cn-beijing-a",
        "CidrBlock": {"Ref": "VSwitch1CidrBlock"},
        "VpcId": { "Fn::GetAtt": [ "EcsVpc", "VpcId" ] },
        "VSwitchName": "create_vpc_vswitch_sg1"
```

`},`

```json
    "VSwitch2": {
      "Type": "ALIYUN::ECS::VSwitch",
        "ZoneId": "cn-beijing-a",
        "CidrBlock": {"Ref": "VSwitch2CidrBlock"},
        "VpcId": { "Fn::GetAtt": [ "EcsVpc", "VpcId" ] },
        "VSwitchName": "create_vpc_vswitch_sg2"
```

`},`

```json
    "SG_VSwitch1": {
      "Type": "ALIYUN::ECS::SecurityGroup",
        "SecurityGroupName": "app_mall",
        "Description": "this is created by heat",
        "VpcId": { "Fn::GetAtt": [ "EcsVpc", "VpcId" ] }
```

`},`

```json
      "Outputs": {
        "SecurityGroupId": {
             "Value": {"get_attr": ["SG_VSwitch1","SecurityGroupId"]}
```

`},`

```json
    "SG_VSwitch1_InRule": {
      "Type": "ALIYUN::ECS::SecurityGroupIngress",
        "SecurityGroupId": { "Fn::GetAtt": [ "SG_VSwitch1", "SecurityGroupId" ] },
        "IpProtocol": "tcp",
        "PortRange": "1/65535",
        "SourceCidrIp": {"Ref": "VSwitch2CidrBlock"}
```

`},`

```json
    "SG_VSwitch1_OutRule": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
        "SecurityGroupId": { "Fn::GetAtt": [ "SG_VSwitch1", "SecurityGroupId" ] },
        "IpProtocol": "tcp",
        "PortRange": "1/65535",
        "DestCidrIp": {"Ref": "VSwitch2CidrBlock"}
```

`},`

```json
    "SG_VSwitch2": {
      "Type": "ALIYUN::ECS::SecurityGroup",
        "SecurityGroupName": "app_mall",
        "Description": "this is created by heat",
        "VpcId": { "Fn::GetAtt": [ "EcsVpc", "VpcId" ] }
```

`},` `},`

```json
    "SG_VSwitch2_InRule": {
      "Type": "ALIYUN::ECS::SecurityGroupIngress",
"Properties":{
```

```json
        "SecurityGroupId": { "Fn::GetAtt": [ "SG_VSwitch2", "SecurityGroupId" ] },
        "IpProtocol": "tcp",
        "PortRange": "1/65535",
        "SourceCidrIp": {"Ref": "VSwitch1CidrBlock"}
```

`},`

```json
    "SG_VSwitch2_OutRule": {
      "Type": "ALIYUN::ECS::SecurityGroupEgress",
        "SecurityGroupId": { "Fn::GetAtt": [ "SG_VSwitch2", "SecurityGroupId" ] },
        "IpProtocol": "tcp",
        "PortRange": "1/65535",
        "DestCidrIp": {"Ref": "VSwitch1CidrBlock"}
```

### 5.2 ESS

#### 5.2.1 ALIYUN::ESS::AlarmTask

ALIYUN::ESS::AlarmTask is used to create a metric-based alarm task. Syntax

```json
  "Type": "ALIYUN::ESS::AlarmTask",
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

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Statistics | String | No | No | The method used to calculate monitoring data. The statistics must be appropriate for the metric chosen. | Valid values: Average, Minimum, and Maximum. Default value: Average. |
| Name | String | No | Yes | The name of the alarm rule. | None |
| EvaluationCount | Integer | No | No | The number of consecutive times that the threshold must be exceeded before an alarm is triggered. | Default value: 3. Minimum value: 1. |
| Period | Integer | No | No | The metric query period, which must be appropriate for the metric chosen. Unit: seconds. | Valid values: 60, 120, 300, and 900. Default value: 300. |
| MetricType | String | No | No | The metric type. | Valid values: system and custom. |
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

`]` `},`

```json
    "Description": {
      "Type": "String",
      "Description": "Description"
```

`},`

```json
    "ScalingGroupId": {
      "Type": "String",
      "Description": "The ID of the scaling group."
```

`},`

```json
    "MetricType": {
      "Type": "String",
      "Description": "Metric Type",
      "AllowedValues": [
        "system",
        "custom"
```

`]` `},`

```json
    "EvaluationCount": {
      "Type": "Number",
      "Description": "Evaluation Count",
      "MinValue": 1
```

`},`

```json
    "Period": {
      "Type": "Number",
      "Description": "Period",
      "AllowedValues": [
        60,
        120,
        300,
```

`]` `},`

```json
    "Dimensions": {
      "Type": "CommaDelimitedList",
      "Description": "Dimensions",
      "MinLength": 1
```

`},`

```json
    "Statistics": {
      "Type": "String",
      "Description": "Statistics",
      "AllowedValues": [
        "Average",
        "Minimum",
        "Maximum"
```

`]` `},`

```json
    "Name": {
      "Type": "String",
      "Description": "Name"
```

`},`

```json
    "GroupId": {
      "Type": "Number",
      "Description": "Group Id"
```

`},`

```json
    "MetricName": {
      "Type": "String",
      "Description": "Metric Name"
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
    "Threshold": {
      "Type": "Number",
      "Description": "Threshold"
```

`},`

```json
  "Resources": {
    "AlarmTask": {
      "Type": "ALIYUN::ESS::AlarmTask",
        "ComparisonOperator": {
          "Ref": "ComparisonOperator"
```

`},`

```json
        "Description": {
          "Ref": "Description"
```

`},` `},`

```json
        "ScalingGroupId": {
          "Ref": "ScalingGroupId"
```

`},`

```json
        "MetricType": {
          "Ref": "MetricType"
```

`},`

```json
        "EvaluationCount": {
          "Ref": "EvaluationCount"
```

`},`

```json
        "Period": {
          "Ref": "Period"
```

`},`

```json
        "Dimensions": {
          "Fn::Split": [
            ",",
              "Ref": "Dimensions"
```

`},`

```json
              "Ref": "Dimensions"
```

`]` `},`

```json
        "Statistics": {
          "Ref": "Statistics"
```

`},`

```json
        "Name": {
          "Ref": "Name"
```

`},`

```json
        "GroupId": {
          "Ref": "GroupId"
```

`},`

```json
        "MetricName": {
          "Ref": "MetricName"
```

`},`

```json
        "AlarmAction": {
          "Fn::Split": [
            ",",
              "Ref": "AlarmAction"
```

`},`

```json
              "Ref": "AlarmAction"
```

`]` `},`

```json
        "Threshold": {
          "Ref": "Threshold"
```

`},`

```json
  "Outputs": {
    "AlarmTaskId": {
      "Description": "The alarm task ID",
      "Value": {
        "Fn::GetAtt": [
```

```
          "AlarmTask",
          "AlarmTaskId"
```

`]`

#### 5.2.2 ALIYUN::ESS::AlarmTaskEnable

ALIYUN::ESS::AlarmTaskEnable is used to start an alarm task. You can call this operation to enable alarm tasks when the task is stopped. Statement

```json
  "Type": "ALIYUN::ESS::AlarmTaskEnable",
    "AlarmTaskId": String,
    "Enable": Boolean
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AlarmTaskId | String | No | No | The ID of the monitoring task. | None |
| Enable | String | Retained | Yes | Specifies whether to enable the alarm task. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt Sample request

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

#### 5.2.3 ALIYUN::ESS::LifecycleHook

ALIYUN::ESS::LifecycleHook is used to create a lifecycle hook for a scaling group. Syntax

```json
  "Type": "ALIYUN::ESS::LifecycleHook",
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
```

`},`

```json
    "NotificationArn": {
      "Type": "String",
      "Description": "The Alibaba Cloud Resource Name (ARN) of the notification target that Auto
Scaling will use to notify you when an instance is in the transition state for the lifecycle hook . This target can be either an MNS queue or an MNS topic. The format of the parameter value is ac s:ess:{region}:{account-id}:{resource-relative-id}.\nregion: the region to which the scaling grou p locates\naccount-id: Alibaba Cloud ID\nFor example:\nMNS queue: acs:ess:{region}:{account-id}:q ueue/{queuename}\nMNS topic: acs:ess:{region}:{account-id}:topic/{topicname}",
      "AllowedPattern": "^acs:ess:([a-zA-Z0-9-]+):(\\d+):(queue|topic)/([a-zA-Z0-9][a-zA-Z0-9-]{0
,255})$",
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
      "Description": "The scaling activities to which lifecycle hooks apply Value range:\n SCALE_
OUT: scale-out event\n SCALE_IN: scale-in event",
      "AllowedValues": [
        "SCALE_OUT",
        "SCALE_IN"
```

`]` `},`

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
```

`},`

```json
    "NotificationMetadata": {
      "Type": "String",
      "Description": "The fixed string that you want to include when Auto Scaling sends a message
about the wait state of the scaling activity to the notification target. The length of the parame ter can be up to 128 characters. Auto Scaling will send the specified NotificationMetadata parame ter along with the notification message so that you can easily categorize your notifications. The NotificationMetadata parameter will only take effect after you specify the NotificationArn parame ter.",
      "MaxLength": 128
```

`},`

```json
    "DefaultResult": {
      "Type": "String",
      "Description": "The action that the scaling group takes when the lifecycle hook times out.
Value range:\n CONTINUE: the scaling group continues with the scale-in or scale-out process.\n AB ANDON: the scaling group stops any remaining action of the scale-in or scale-out event.\nDefault value: CONTINUE\nIf the scaling group has multiple lifecycle hooks and one of them is terminated by the DefaultResult=ABANDON parameter during a scale-in event (SCALE_IN), the remaining lifecycl e hooks under the same scaling group will also be terminated. Otherwise, the action following the wait state is the next action, as specified in the parameter DefaultResult, after the last lifecy cle event under the same scaling group.",
      "AllowedValues": [
        "CONTINUE",
        "ABANDON"
```

`]` `},`

```json
  "Resources": {
    "LifecycleHook": {
      "Type": "ALIYUN::ESS::LifecycleHook",
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

#### 5.2.4 ALIYUN::ESS::ScalingConfiguration

ALIYUN::ESS::ScalingConfiguration is used to create a scaling configuration. Syntax

```json
  "Type": "ALIYUN::ESS::ScalingConfiguration",
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

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | No | Yes | The ID of the resource group to which the instance belongs. | None |
| DeploymentSetId | String | No | No | The ID of the deployment set. | None |
| HpcClusterId | String | No | No | The ID of the E-HPC cluster to which the instance belongs. | None |
| ScalingGroupId | String | Yes | No | The ID of the scaling group to which the scaling configuration belongs. | None |
| DiskMappings | List | No | No | The data disks to be attached to the instance. | A maximum of 16 data disks can be attached. |
| InternetChargeTy pe | String | No | No | The billing method for Internet usage. | Valid values: PayByBandwidth and PayByTraffic. Default value: PayByTraffic |
| InternetMaxBand widthIn | Integer | No | No | The maximum inbound bandwidth from the Internet. Unit: Mbit/s. | Valid values: 1 to 100. Default value: 100. |
| InternetMaxBand widthOut | Integer | No | No | The maximum outbound bandwidth to the Internet. Unit: Mbit/s. | Valid values for the PayByBandwidth mode: 0 to 200. Default value: 0. Valid values for the PayByTraffic mode: 1 to 200. If you choose to use the PayByTraffic mode, you must specify this parameter. |
| InstanceId | String | No | No | The ID of the ECS instance whose properties are used to create the scaling configuration. | None |
| SystemDiskCateg ory | String | No | No | The type of the system disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, and _ ephemeral ssd. _ |

| User Guide·Resource | types |   |   | Reso | urce Orchestration Servic |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |
| ImageId | String | No | No | The ID of the image used to start the ECS instance. You can use a public image, custom image, or Alibaba Cloud Marketplace image. | N/A |
| InstanceType | String | No | No | The type of the ECS instance. | N/A |
| SecurityGroupId | String | No | No | The ID of the security group to which the created instance belongs. | None |
| IoOptimized | String | No | No | Specifies whether the instance is I/O optimized. | Valid values: none (non-I/O optimized) and optimized (I/O optimized). Default value: none. |
| ScalingConfigura tionName | String | No | No | The display name of the scaling configuration. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. This parameter must be unique in a scaling group. The default name is the ID of the scaling configuration. |
| KeyPairName | String | No | No | The name of the key pair that is used to connect to the ECS instance. | For Windows ECS instances, this parameter is ignored and is empty by default. The Password parameter takes effect even if the KeyPairName parameter is specified. However, Linux instances do not allow logon by password, and the KeyPairName value is used instead. |
| RamRoleName | String | No | No | The RAM role name of the instance. | You can call the ListRoles operation to query the role name. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SystemDiskSize | Integer | No | Yes | The size of the system disk. Unit: GB. | Valid values: 40 to 500. If a custom image is used to create a system disk, ensure that the size of the system disk is greater than that of the custom image. |
| UserData | String | No | No | The user data provided to create the ECS instance. | The user data can be up to 16 KB in size. You must convert the data into Base64-encoded strings. If the data contains special characters, add a backslash (\) immediately before each special character. |
| InstanceTypes | List | No | No | The ECS instance types that can be used in a scaling group. | A maximum of 10 ECS instance types can be specified. If this parameter is specified, the InstanceType parameter is ignored. |
| PasswordInherit | Boolean | No | Yes | Specifies whether to use the preconfigured password of the specified image. To use this parameter, ensure that a password is configured for the specified image. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TagList | List | No | Yes | The tags of the instance. Tags must be specified as key-value pairs. A maximum of 20 tags can be specified. The following rules apply to keys and values: A key can contain a maximum of 64 characters and cannot start with aliyun, http://, or https://. You cannot specify an empty string as a key. A value can contain a maximum of 128 characters and cannot start with aliyun, http://, or https://. You can specify an empty string as a value. | None |
| SpotStrategy | String | No | Yes | The preemption policy for pay-as-you-go instances. Valid values: NoSpot: applies to regular pay-as-you- go instances. SpotWithPriceLimit: applies to preemptible instances with a maximum hourly price. SpotAsPriceGo: applies to pay-as- you-go instances priced at the market price at the time of purchase. Default value: NoSpot. | Valid values: NoSpot, SpotWithPriceLimit, and SpotAsPriceGo. |
| InstanceName | String | No | Yes | The name of the instance created based on the current scaling configuration. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| SpotPriceLimit | Number | No | Yes | The maximum hourly price for preemptible instance N. Valid values of N: 1 to 10. This parameter is valid only when the SpotStrategy parameter is set to SpotWithPriceLimit. A maximum of three decimal places can be specified. The default value of InstanceTypes can be overridden by the value of SpotPriceLimitForInstan ceType. | None |
| SpotPriceLimitFo rInstanceType | Map | No | Yes | The instance type of preemptible instance N. Valid values of N: 1 to 10. This parameter is valid only when the SpotStrategy parameter is set to SpotWithPriceLimit. Example: {"key1":"value1","key2": "value2", ... "key5":"value5"}. A key is an ECS instance type. A value can have a maximum of three decimal places. | None |

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

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Size | String | Yes | No | The size of the data disk. Unit: GB. | None |
| Category | String | No | No | The type of the data disk. | Valid values: cloud, cloud efficiency, _ cloud ssd, and _ ephemeral ssd. _ |
| DiskName | String | No | No | The name of the data disk. | The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. This parameter is empty by default. |
| Description | String | No | No | The description of the data disk. | The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| Device | String | No | No | The device name of the data disk. | The system allocates a device name in alphabetical order from /dev/xvda to /dev/xvdz. |
| SnapshotI d | String | No | No | The ID of the snapshot used to create the data disk. | None |
| Encrypted | String | No | No | Specifies whether to encrypt the data disk. | Default value: false. |
| KMSKeyId | String | No | No | The KMS key ID for the data disk. | None |

TagList syntax

```json
"TagList": [
    "Value": String,
    "Key": String
```

`]` TagList properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Key | String | Yes | No | None | None |
| Value | String | Yes | No | None | None |

Response parameters Fn::GetAtt ScalingConfigurationId: the ID of the scaling configuration. This ID is a globally unique identifier (GUID) generated by the system. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingConfiguration": {
      "Type": "ALIYUN::ESS::ScalingConfiguration",
        "ImageId": "ubuntu1404_64_20G_aliaegis_20150325.vhd",
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

#### 5.2.5 ALIYUN::ESS::ScalingGroup

ALIYUN::ESS::ScalingGroup is used to create a scaling group. A scaling group is a group of ECS instances that are dynamically scaled based on the configured scenario. A scaling group does not take effect immediately after being created. You must use ALIYUN::ESS::ScalingGroupEnable to enable the scaling group to trigger scaling rules and execute scaling activities. Syntax

```json
  "Type": "ALIYUN::ESS::ScalingGroup",
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
    "DBInstanceIds": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MinSize | Integer | Yes | Yes | The minimum number of ECS instances in the scaling group. | Valid values: 0 to 1000. When the number of ECS instances in the scaling group is less than the value of MinSize, Auto Scaling automatically creates ECS instances until the number of instances is equal to the value of MinSize. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MaxSize | Integer | Yes | Yes | The maximum number of ECS instances in the scaling group. | Valid values: 0 to 1000. When the number of ECS instances in the scaling group is greater than the value of MaxSize, Auto Scaling removes the ECS instances from the scaling group until the number of instances is equal to the value of MaxSize. |
| ScalingGroupNa me | String | No | Yes | The display name of the scaling group. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), hyphens _ (-), and periods (.). It must start with a letter or digit. The name must be unique to an Alibaba Cloud account in a region. The default value is the ID of the scaling group. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LaunchTemplat eId | String | No | Yes | The ID of the instance launch template from which the scaling group obtains launch configurations. | None |
| LaunchTemplat eVersion | String | No | Yes | The version of the instance launch template. | Valid values: The fixed template version number. Default: The default template version is always used. Latest: The latest template version is always used. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RemovalPolicys | List | No | Yes | The policies to remove ECS instances from the scaling group. | Default value: OldestScalingC onfiguration or OldestInstance. Valid values: OldestInstan ce: removes the ECS instance that is added to the scaling group at the earliest point in time. NewestInsta nce: removes the ECS instance that is added to the scaling group at the latest point in time. OldestScalin gConfigurati on: removes the ECS instance that is created based on the earliest scaling configuration . |
| VSwitchId | String | No | No | The ID of the VSwitch. | None |
| LoadBalancerId s | List | No | Yes | The IDs of the SLB instances. | This value can be a JSON array that contains up to five SLB instance IDs. Separate multiple IDs with commas (,). |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DefaultCooldo wn | Integer | No | Yes | The cooldown period after a scaling activity (adding or removing ECS instances) is executed. | Valid values: 0 to 86400. Unit: seconds. Default value: 300. During the cooldown period, the scaling group does not execute any other scaling activities triggered by CloudMonitor event-triggered tasks. |
| DBInstanceIds | List | No | Yes | The IDs of ApsaraDB for RDS instances. | This value can be a JSON array that contains up to eight RDS instance IDs. Separate multiple IDs with commas (,). |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VSwitchIds | List | No | No | The IDs of VSwitches. | You can specify a maximum of five VSwitch IDs. If this parameter is specified, the VSwitchId parameter is ignored. VSwitches are sorted in descending order of priority. When an ECS instance cannot be created in the zone where the VSwitch with the highest priority resides, the system automatically uses the VSwitch with the next highest priority to create the ECS instance. |
|   |   |   |   |   | Valid values: PRIORITY: ECS instances are scaled based on the specified VSwitch. When an ECS instance cannot be created in the zone where the VSwitch with the highest priority resides, the system automaticall y uses the VSwitch with the next highest priority to create the ECS instance. |

| Property | Type | Required | Editable | Description | BALANCE: Constraint ECS instances |
|---|---|---|---|---|---|
| MultiAZPolicy | String | No | No | The ECS instance scaling policy for the multi-zone scaling group. | are distributed evenly in multiple zones specified in the scaling group. COST OPTIMI _ ZED: ECS instances are created |
|   |   |   |   |   | based on the unit price of vCPUs, from low to high. Preemptible instances are created first when preemptible instance types are specified for the scaling configuration . Pay-as-you- go instances are created automaticall y when all types of preemptible instances are unavailable due to issues such as insufficient ECS resources. |
| NotificationCon figurations | List | No | Yes | The notification configurations for event and resource changes. | None |
| ProtectedInstan ces | List | No | Yes | The number of protected ECS instances in the scaling group. | Maximum value: 1000. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StandbyInstanc es | List | No | Yes | The number of ECS instances that are in the standby state in the scaling group. | Maximum value: 1000. |
| HealthCheckTyp e | String | No | Yes | The health check type. | Valid values: ECS NONE |
| GroupDeletionP rotection | Boolean | No | Yes | Specifies whether to enable deletion protection for the scaling group. | Valid values: true: enables deletion protection for the scaling group. In this case, you cannot delete the scaling group. false: disables deletion protection for the scaling group. This is the default value. |
| DesiredCapacity | Integer | No | Yes | The expected number of ECS instances in the scaling group. The scaling group automatically keeps the number of ECS instances at the expected value. | The number of ECS instances must be greater than the value of MinSize and be less than the value of MaxSize. |
| InstanceId | String | No | No | The ID of the ECS instance from which the scaling group obtains configuration information of the specified instance. | None |

Response parameters Fn::GetAtt ScalingGroupId: the ID of the scaling group. This ID is a globally unique identifier (GUID) generated by the system. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingGroup": {
      "Type": "ALIYUN::ESS::ScalingGroup",
        "MaxSize": 1,
        "MinSize": 1,
        # "ScalingGroupName": "HeatCreatedR****",
        # "DefaultCooldown": 500,
        # "RemovalPolicy_1": "",
        # "RemovalPolicy_2": "",
```

`},`

```json
  "Outputs": {
    "ScalingGroup": {
         "Value": {"Fn::GetAtt": ["ScalingGroup", "ScalingGroupId"]}
```

#### 5.2.6 ALIYUN::ESS::ScalingGroupEnable

ALIYUN::ESS::ScalingGroupEnable is used to enable a scaling group. Syntax

```json
  "Type": "ALIYUN::ESS::ScalingGroupEnable",
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

| esource Orchestr | ation Service |   |   | User Gui | de·Resource type |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |
| ScalingConfigur ationId | String | No | No | The ID of the scaling configuration to be activated in the scaling group. | None |
| InstanceIds | List | No | Yes | The IDs of ECS instances to be added to the enabled scaling group. | A maximum of 20 instance IDs can be specified. |
| ScalingRuleArisE xecuteVersion | Integer | No | Yes | The version of the identifier for the scaling rule to be executed. If you change this property, all scaling rules specified by ScalingRuleAris will be executed once. | Minimum value: 0. |
| ScalingRuleAris | List | No | Yes | The unique identifiers of scaling rules in the scaling group. Invalid unique identifiers are not displayed in the query results and no errors are reported. | A maximum of 10 scaling rule identifiers can be specified. |
| RemoveInstanc eIds | List | No | Yes | The IDs of ECS instances to be deleted. | A maximum of 1,000 instance IDs can be specified. |

Response parameters Fn::GetAtt LifecycleState: the status of the scaling group. ScalingInstances: the instances that are automatically created in the scaling group. ScalingGroupId: the ID of the scaling group. ScalingRuleArisExecuteResultInstancesRemoved: the instances that are removed from the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultNumberOfAddedInstances: the number of instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris. ScalingInstanceDetails: the instance scaling details. ScalingRuleArisExecuteErrorInfo: the error information about the execution of the scaling rules specified by ScalingRuleAris. ScalingRuleArisExecuteResultInstancesAdded: the instances that are added to the scaling group by executing the scaling rules specified by ScalingRuleAris. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingGroupEnable": {
      "Type": "ALIYUN::ESS::ScalingGroupEnable",
        "ScalingGroupId": "r0HUqbJ411cc2eQw8bU****",
        "ScalingConfigurationId": "bJlLfdexm77Ldsyptmel****",
        "InstanceIds": "",
```

`},`

```json
  "Outputs": {
    "ScalingGroupEnable": {
      "Value": {"Fn::GetAtt": ["ScalingGroupEnable", "LifecycleState"]}
```

#### 5.2.7 ALIYUN::ESS::ScalingRule

ALIYUN::ESS::ScalingRule is used to create a scaling rule. Syntax

```json
  "Type": "ALIYUN::ESS::ScalingRule",
    "AdjustmentValue": Integer,
    "Cooldown": Integer,
    "ScalingGroupId": String,
    "AdjustmentType": String,
    "ScalingRuleName": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AdjustmentValue | Integer | No | Yes | The number of ECS instances to add or release when scaling occurs. The number of ECS instances to be adjusted in a single scaling activity cannot exceed 500. | Valid values in different adjustment modes: QuantityChangeInCap acity: -500 to 500. PercentChangeInCapa city: -100 to 10000. TotalCapacity: 0 to 1000. |
| Cooldown | Integer | No | Yes | The cooldown period of the scaling rule. Unit: seconds. | Valid values: 0 to 86400. This parameter is empty by default. |
| ScalingGroupId | String | Yes | No | The ID of the scaling group to which the scaling rule belongs. | None |
| AdjustmentType | String | Yes | Yes | The adjustment mode of the scaling rule. | Valid values: QuantityChangeInCap acity: adds or removes a specified number of ECS instances. PercentChangeInCapa city: adds or removes a specified proportion of ECS instances. TotalCapacity: adds or removes ECS instances to ensure that the current scaling group has a specified number of ECS instances. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScalingRuleName | String | No | Yes | The display name of the scaling rule. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. The name of a scaling rule must be unique within the scaling group that it belongs to. The default value is the ID of the scaling rule. |

Response parameters Fn::GetAtt ScalingRuleAri: the unique identifier of the scaling rule. ScalingRuleId: the ID of the scaling rule. It is a globally unique identifier (GUID) generated by the system. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScalingRule": {
      "Type": "ALIYUN::ESS::ScalingRule",
        "ScalingRuleName": {
          "Ref": "ScalingRuleName"
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
        "AdjustmentType": {
          "Ref": "AdjustmentType"
```

`},`

```json
        "AdjustmentValue": {
          "Ref": "AdjustmentValue"
```

`},`

```json
  "Parameters": {
    "ScalingRuleName": {
      "AllowedPattern": "^[a-zA-Z0-9\\u4e00-\\u9fa5][-_.a-zA-Z0-9\\u4e00-\\u9fa5]{1,63}$",
      "Type": "String",
      "Description": "Name shown for the scaling group, which is a string containing 2 to 40 Engl
ish or Chinese characters. It must begin with a number, a letter (case-insensitive) or a Chinese character and can contain numbers, \"_\", \"-\" or \". \". The account name in the same scaling g
```

`i` `i` `i` `h` `i` `f` `hi` `l` `i`

```
ifid
```

`h` `d``f` `l` `l` `i`

```
roup is unique in the same region. If this parameter value is not specified, the default value is ScalingRuleId."
```

`},`

```json
    "Cooldown": {
      "Type": "Number",
      "Description": "Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The
default value is empty.",
      "MaxValue": 86400,
      "MinValue": 0
```

`},`

```json
    "ScalingGroupId": {
      "Type": "String",
      "Description": "ID of the scaling group of a scaling rule."
```

`},`

```json
    "AdjustmentType": {
      "Type": "String",
      "Description": "Adjustment mode of a scaling rule. Optional values:\n- QuantityChangeInCapa
city: It is used to increase or decrease a specified number of ECS instances.\n- PercentChangeInC apacity: It is used to increase or decrease a specified proportion of ECS instances.\n- TotalCapa city: It is used to adjust the quantity of ECS instances in the current scaling group to a specif ied value.",
      "AllowedValues": [
        "QuantityChangeInCapacity",
        "PercentChangeInCapacity",
        "TotalCapacity"
```

`]` `},`

```json
    "AdjustmentValue": {
      "Type": "Number",
      "Description": "Adjusted value of a scaling rule. Value range:\n- QuantityChangeInCapacity:
[-500, 500]\n- PercentChangeInCapacity: [-100, 10000]\n- TotalCapacity: [0, 1000]",
      "MaxValue": 10000,
      "MinValue": -500
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

`]`

#### 5.2.8 ALIYUN::ESS::ScheduledTask

ALIYUN::ESS::ScheduledTask is used to create a scheduled task based on input parameters. Syntax

```json
  "Type": "ALIYUN::ESS::ScheduledTask",
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
| TaskEnabled | Boolean | No | Yes | Specifies whether to start the scheduled task. true: starts the scheduled task. false: stops the scheduled task. Default value: true. | None |
| Description | String | No | Yes | The description of the scheduled task. | The description must be 2 to 200 characters in length. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScheduledTask Name | String | No | Yes | The display name of the scheduled task. | The name must be 2 to 40 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It must start with a letter or digit. This parameter must be unique in a region and under an Apsara Stack tenant account. The default value is the ID of the scheduled scaling task. |
| LaunchExpiratio nTime | Integer | No | Yes | The time period during which a failed scheduled task is retried. Unit: seconds. Default value: 600. | Valid values: 0 to 21600. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LaunchTime | String | Yes | Yes | The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. The time must be in UTC. If the RecurrenceType parameter is specified, the task is executed each day at the time specified by LaunchTime. If the RecurrenceType parameter is not specified, the task is only executed once at the date and time specified by LaunchTime. You cannot enter a point in time later than 90 days from the date of scheduled task creation or modification. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RecurrenceEndT ime | String | No | Yes | The end time after which the scheduled task will not be repeated. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mmZ format. The time must be in UTC. You cannot enter a point in time later than 90 days from the date of scheduled task creation or modification. If you set RecurrenceEndTime, you must also set both RecurrenceType and RecurrenceValue. | None |
| RecurrenceType | String | No | Yes | The interval that the scheduled task is repeated at. | Valid values: Daily: The scheduled task is executed once every specified number of days. Weekly: The scheduled task is executed on each specified day of a week. Monthly: The scheduled task is executed on each specified day of a month. Cron: The scheduled task is executed based on the specified Cron expression. If you set RecurrenceType, you must also set both RecurrenceEndTime and RecurrenceValue. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RecurrenceValu e | String | No | Yes | Specifies how often the scheduled task recurs. | Daily: indicates the interval of days that the scheduled task is repeated on. You can enter a single value ranging from 1 to 31. Weekly: indicates which days of the week that the scheduled task is repeated on. You can enter multiple values separated by commas (,). The values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday. Monthly: indicates which days of the month that the scheduled task is repeated on. You can enter two values ranging from 1 to 31. The format is A-B. B must be greater than or equal to A. Cron: indicates a user- defined Cron expression that the scheduled task is repeated on. A Cron expression is written in UTC time and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W characters. If you set RecurrenceValue, you must also set both RecurrenceEndTime and RecurrenceType. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ScheduledActio n | String | Yes | Yes | The operations to be performed when the scheduled task is triggered. When you set this parameter, you must also enter the unique identifier of the scaling rule. | The parameter value can be up to 200 characters in length. |

Response parameters Fn::GetAtt ScheduledTaskId: the ID of the scheduled task. This ID is a globally unique identifier (GUID) generated by the system. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "ScheduledTask": {
      "Type": "ALIYUN::ESS::ScheduledTask",
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

### 5.3 OSS

#### 5.3.1 ALIYUN::OSS::Bucket

ALIYUN::OSS::Bucket is used to create an OSS bucket. Syntax

```json
  "Type": "ALIYUN::OSS::Bucket",
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
| BucketName | String | Yes | No | The name of the bucket. | The name must be 3 to 63 characters in length and can contain lowercase letters, digits, and hyphens (-). It must start and end with a lowercase letter or digit. |
| AccessControl | String | No | No | The access control policy. | Valid values: private, public-read, and public-read-write. |
| CORSConfiguration | Map | No | No | The configuration of cross-origin resource sharing for objects in the bucket. | None |
| LifecycleConfiguration | Map | No | No | The lifecycle configuration for objects in the bucket. | None |
| LoggingConfiguration | Map | No | No | The logging configuration. | None |
| RefererConfiguration | Map | No | No | The hotlinking protection configuration. | None |

| esource Orchestration S | ervice |   |   | U | ser Guide·Resource type |
|---|---|---|---|---|---|
| Property | Type | Required | Editable | Description | Constraint |
| DeletionForce | Boolean | No | No | Specifies whether to forcibly delete objects from an OSS bucket | Valid values: true false Default value: false. |
| WebsiteConfiguration | Map | No | No | The information used to configure the bucket as a static website. | None |
| ServerSideEncryptionC onfiguration | Map | No | No | The server-side encryption rules. | None |
| Tags | Map | No | No | The tags of the bucket. Tags exist as key-value pairs. | A maximum of 20 tags can be specified. A tag key must be 1 to 64 bytes in length and cannot start with http:/ / , https:// , or Aliyun . A tag value can be up to 128 bytes in length and must be encoded in UTF-8. |
| StorageClass | String | No | No | The type of the bucket. | Valid values: Standard, IA, and Archive. |
| Policy | Map | No | No | The bucket policy configuration. | None |

|   | / |   |
|---|---|---|
|   |   | Aliyun |

CORSConfiguration syntax

```json
"CORSConfiguration": {
  "CORSRule": [
      "AllowedHeader": String,
      "AllowedMethod": List,
      "AllowedOrigin": List,
      "ExposeHeader": List,
      "MaxAgeSeconds": Integer
```

`]` CORSConfiguration properties

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| CORSRule | List | No | No | The rules that define cross- origin resource sharing of objects in the bucket. | None |
| AllowedHeader | String | No | No | The allowed cross- origin request headers. | Valid values: *, Cache- Control, Content- Language, Content-Type, Expires, Last-Modified, and Pragma. |
| AllowedMethod | List | No | No | The allowed cross- origin request methods. | Valid values: *, GET, PUT, POST, DELETE, and HEAD. |
| AllowedOrigin | List | No | No | The origins from which cross- origin requests are allowed. | None |
| ExposeHeader | List | No | No | The response headers for allowed access requests from applicatio ns. | Asterisks (*) cannot be used as wildcard characters. |

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| MaxAgeSeconds | Integer | No | No | The period of time that the browser can cache the response of a preflight (OPTIONS) request to a specific resource. | None |

LifecycleConfiguration syntax

```json
"LifecycleConfiguration": {
  "Rule": [
      "ID": String,
      "Prefix": String,
      "Status": String,
      "Expiration": Map,
      "AbortMultipartUpload": Map
```

`]` LifecycleConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Rule | List | No | No | The lifecycle rule. | None |
| ID | String | No | No | The unique ID of the rule. | The ID can be up to 255 characters in length. When this parameter is empty or not specified, OSS generates a unique rule ID. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Prefix | String | No | No | The prefix to which the rule applies. | The rule takes effect only on objects that have a matching prefix. |
| Status | String | No | No | Specifies whether to enable or disable the rule. | Valid values: Enable and Disable. |
| Expiration | Map | No | No | The expiration attributes of the rule for the specified object. | None |
| AbortMultipartUpload | Map | No | No | The expiration attributes of the multipart upload tasks that are not complete. | None |

Expiration syntax

```json
"Expiration":{
  "Days": Number,
  "CreatedBeforeDate": String
```

Expiration properties

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days since the object was last modified after which the rule will take effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| CreatedBeforeDate | String | No | No | The date before which the rule takes effect. | Specify the time in the ISO 8601 standard. The time must be UTC 00:00. Example: 2002-10- 11T00:00:00.000Z. |

AbortMultipartUpload syntax

```json
"AbortMultipartUpload": {
  "CreatedBeforeDate": String,
  "Days": Number
```

AbortMultipartUpload properties

| Property | Type | Required | Editable | Descriptio n | Constraint |
|---|---|---|---|---|---|
| Days | Number | No | No | The number of days since the object was last modified after which the rule will take effect. | When the number of days since the object was last modified exceeds the specified number of days, the object is deleted. If you set the Days parameter to 30, objects that were last modified on January 1, 2016 are deleted by the backend application on January 31, 2016. |
| CreatedBeforeDate | String | No | No | The date before which the rule takes effect. | Specify the time in the ISO 8601 standard. The time must be UTC 00:00. Example: 2002-10- 11T00:00:00.000Z. |

LoggingConfiguration syntax

```json
"LoggingConfiguration": {
  "TargetBucket": String,
  "TargetPrefix": String
```

LoggingConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TargetBucket | String | No | No | The storage space for storing access logs. | None |

| User Guide·Resource types |   |   |   | Resource Orches | tration Servic |
|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| TargetPrefix | String | No | No | The prefix of the names of saved access log files. | None |

WebsiteConfiguration syntax

```json
"WebsiteConfiguration":{
  "IndexDocument": String,
  "ErrorDocument": String
```

WebsiteConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| IndexDocument | String | No | No | The default homepage for a static website. | None |
| ErrorDocument | String | No | No | The default error page for a static website. | None |

RefererConfiguration syntax

```json
"RefererConfiguration":{
  "AllowEmptyReferer": String,
  "RefererList": List
```

RefererConfiguration properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllowEmptyReferer | String | No | No | Specifies whether the Referer field can be left empty in an access request. | None |
| RefererList | List | No | No | The referer whitelist. OSS allows requests whose Referer field values are in the referer whitelist. | None |

ServerSideEncryptionConfiguration syntax

```json
"ServerSideEncryptionConfiguration":{
  "KMSMasterKeyID": String,
  "SSEAlgorithm": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| KMSMasterKeyID | String | No | No | The ID of the customer master key. | The key ID is required only when the SSEAlgorithm value is KMS and the specified key is used for encryption. |
| SSEAlgorithm | String | Yes | No | The default server- side encryption method. | Valid values: KMS and AES256. |

Response parameters Fn::GetAtt Name: the bucket name, which must be globally unique. DomainName: the public domain name of the specified bucket. InternalDomainName: the internal domain name of the specified bucket. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Bucket": {
      "Type": "ALIYUN::OSS::Bucket",
        "AccessControl": "private",
        "BucketName": "rostest",
        "WebsiteConfiguration":{
            "IndexDocument": "index1.html",
            "ErrorDocument": "error404.html"
```

`},`

```json
        "LoggingConfiguration": {
            "TargetBucket": "cos-mirror",
            "TargetPrefix": "test404"
```

`},`

```json
        "CORSConfiguration": {
            "CORSRule": [{
                "AllowedHeader": ["*"],
                "AllowedMethod": ["GET", "PUT"],
                "AllowedOrigin": ["*"],
                "ExposeHeader": ["Date"],
                "MaxAgeSeconds": 3600
```

`}]` `},`

```json
        "LifecycleConfiguration": {
            "Rule": [{
                "ID": "deleteRule",
                "Prefix": "test/",
                "Status": "Enabled",
                "Expiration":{
                    "Days": 2
```

`},`

```json
                "AbortMultipartUpload":{
                    "CreatedBeforeDate": "2014-10-11T00:00:00.000Z"
```

`}]` `},`

```json
        "RefererConfiguration": {
            "AllowEmptyReferer": true,
            "RefererList": ["http://www.aliyun.com", "https://www.?.aliyuncs.com"]
```

`},`

```json
  "Outputs": {
    "Name": {
         "Value": {"Fn::GetAtt": ["Bucket","Name"]}
```

`},`

```json
    "DomainName": {
         "Value": {"Fn::GetAtt": ["Bucket","DomainName"]}
```

### 5.4 RDS

#### 5.4.1 ALIYUN::RDS::Account

ALIYUN::RDS::Account is used to create a database management Account. Statement

```json
  "Type": "ALIYUN::RDS::Account",
    "AccountDescription": String,
    "DBInstanceId": String,
    "AccountPassword": String,
    "AccountType": String,
    "AccountName": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountDescrip tion | String | Yes | True | The description of the account. | The name must be 2 to 256 characters in length. It can contain digits, letters, underscores ( ), _ and hyphens (- ); but must start with a letter. |
| DBInstanceId | String | No | No | The ID of the RDS instance. | None |
| AccountPasswo rd | String | No | No | The password of the database account. | The password must be 8 to 32 characters in length. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccountType | String | Yes | Released | The type of the database account. | Valid values: Normal: indicates a standard account. Super: indicates a privileged account. Default value: Normal. |
| AccountName | String | No | No | The name of the database account. | Valid values: 1025 to 10000. You cannot use the following commonly used port numbers: 2222, 4500, 4510, 4560, 7505, 9000, 9001, and 9002. |

Response parameters Fn::GetAtt AccountName: the name of the database account. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Account": {
      "Type": "ALIYUN::RDS::Account",
        "AccountDescription": {
          "Ref": "AccountDescription"
```

`},`

```json
        "DBInstanceId": [
          "Ref": "DBInstanceId"
```

`},`

```json
        "AccountPassword": {
          "Ref": "AccountPassword"
```

`},`

```json
        "AccountType": {
          "Ref": "AccountType"
```

`},`

```json
        "AccountName": {
          "Ref": "AccountName"
```

`},`

```json
  "Parameters": {
    "AccountDescription": {
      "Type": "String",
      "Description": "Account remarks.\nIt cannot begin with http:// or https://.\nIt must start
with a Chinese character or English letter.\nIt can include Chinese and English characters/letter s, underscores (_), hyphens (-), and digits.\nThe length may be 2-256 characters."
```

`},`

```json
    "DBInstanceId": [
      "Type": "String",
      "Description": "RDS instance ID."
```

`},`

```json
    "AccountPassword": {
      "MinLength": 8,
      "Type": "String",
      "Description": "The account password for the database instance. It may consist of letters,
digits, or underlines, with a length of 8 to 32 characters.",
      "MaxLength": 32
```

`},`

```json
    "AccountType": {
      "Default": "Normal",
      "Type": "String",
      "Description": "Privilege type of account.\nNormal: Common privilege.\nSuper: High privileg
e. And the default value is Normal.\nThis parameter is valid for MySQL 5.5/5.6 only.\nMySQL 5.7, SQL Server 2012/2016, PostgreSQL, and PPAS each can have only one initial account. Other accounts are created by the initial account that has logged on to the database.",
      "AllowedValues": ["Normal", "Super"]
```

`},`

```json
    "AccountName": {
      "Type": "String",
      "Description": "Account name, which must be unique and meet the following requirements:\nSt
art with a letter;\nConsist of lower-case letters, digits, and underscores (_);\nContain no more than 16 characters.\nFor other invalid characters, see Forbidden keywords table."
```

`},`

```json
  "Outputs": {
    "AccountName": {
      "Description": "Account name",
      "Value": {
        "Fn::GetAtt": ["Account", "AccountName"]
```

#### 5.4.2 ALIYUN::RDS::AccountPrivilege

ALIYUN::RDS::AccountPrivilege is used to grant database access permissions to accounts. Statement

```json
  "Type": "ALIYUN::RDS::AccountPrivilege",
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

Response parameters Fn::GetAtt Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccountPrivilege": {
      "Type": "ALIYUN::RDS::AccountPrivilege",
        "AccountPrivilege": {
          "Ref": "AccountPrivilege"
```

`},`

```json
        "DBInstanceId": [
          "Ref": "DBInstanceId"
```

`},`

```json
        "DBName": {
          "Ref": "DBName"
```

`},`

```json
        "AccountName": {
          "Ref": "AccountName"
```

`},`

```json
  "Parameters": {
    "AccountPrivilege": {
      "Type": "String",
      "Description": "RDS account privilege",
      "AllowedValues": ["ReadOnly", "ReadWrite", "DDLOnly", "DMLOnly", "DBOwner"]
```

`},`

```json
    "DBInstanceId": [
      "Type": "String",
      "Description": "RDS instance ID."
```

`},`

```json
    "DBName": {
      "Type": "String",
      "Description": "RDS database name"
```

`},`

```json
    "AccountName": {
      "Type": "String",
      "Description": "RDS account name."
```

`},`

```json
  "Outputs": {}
```

#### 5.4.3 ALIYUN::RDS::DBInstance

ALIYUN::RDS::DBInstance is used to create an ApsaraDB for RDS instance. Syntax

```json
  "Type": "ALIYUN::RDS::DBInstance",
    "Engine": String,
    "MultiAZ": Boolean,
    "VpcId": String,
    "DBMappings": List,
    "DBInstanceDescription": String,
    "ConnectionMode": String,
    "MasterUsername": String,
    "MasterUserPassword": String,
    "ZoneId": String,
    "DBInstanceNetType": String,
    "DBInstanceStorage": Integer,
    "VSwitchId": String,
    "AllocatePublicConnection": Boolean,
    "EngineVersion": String,
    "PreferredBackupTime": String,
    "DBInstanceClass": String,
    "SecurityIPList": String,
    "BackupRetentionPeriod": Integer,
    "PrivateIpAddress": String,
    "PreferredBackupPeriod": List,
    "PeriodType": String,
    "PayType": String,
    "Period": Integer,
    "ResourceGroupId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroup Id | String | No | No | The ID of the resource group. | None |
| Engine | String | Yes | No | The type of the database | Valid values: MySQL SQLServer PostgreSQL PPAS |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceStor age | Integer | Yes | Yes | The storage capacity of the instance. | Valid values when Engine is set to MySQL: 5 to 1000. Valid values when Engine is set to SQLServer: 10 to 1000. Valid values when Engine is set to PostgreSQL: 5 to 2000. Valid values when Engine is set to PPAS: 5 to 2000. Unit: GB. Not e This value must be in 5 GB increments. |
| EngineVersion | String | Yes | No | The engine version of the database. | Valid values: When Engine is set to MySQL, the valid values are 5.5, 5.6, 5.7, and 8.0. When Engine is set to SQLServer, set the value to 2008r2. When Engine is set to PostgreSQL, set the value to 9.4. When Engine is set to PPAS, set the value to 9.3. |
| DBInstanceClas s | String | Yes | Yes | The type of the instance. | Valid values: rds.mys2.large rds.mss1.large rds.pg.s1.small |
| SecurityIPList | String | Yes | Yes | The whitelist of IP addresses that are allowed to access all databases in the instance. | Separate multiple IP addresses with commas (,). Each IP address in the whitelist must be unique. A maximum of 1,000 IP addresses can be specified. The 0.0.0.0/0 format is supported. You can specify IP addresses in the 10.23.XX.XX format and CIDR blocks in the 10.23.XX.XX/24 format. In 10.23.XX.XX/24, /24 indicates the length of the prefix in the CIDR block, and a prefix can be 1 to 32 characters in length. 0.0.0.0/0 indicates that no access restriction is applied. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MultiAZ | Boolean | No | No | Specifies whether the instance can be deployed in multiple zones. | None |
| VpcId | String | No | No | The ID of the VPC. | None |
| DBMappings | List | No | No | The list of databases created in the instance. | None |
| DBInstanceDes cription | String | No | No | The description or remarks of the instance. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and hyphens _ (-). It must start with a letter but cannot start with http:// or https:// . |
| ConnectionMo de | String | No | No | The database connection mode. | Valid values: Performance: standard connection mode Safety: safe connection mode If this parameter is not specified, the connection mode assigned by the system is used by default. |
| MasterUserna me | String | No | No | The name for the primary account of the instance. | The name must be unique. The name cannot exceed 16 characters in length and can contain letters, digits, and underscores ( ). It must start _ with a letter. |
| MasterUserPas sword | String | No | No | The password for the primary account of the instance. | The password must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| ZoneId | String | No | No | The ID of the zone. | None |
| DBInstanceNet Type | String | No | No | The network type of the instance. | Default value: Intranet. Valid value: Internet Intranet |
| VSwitchId | String | No | No | The ID of the VSwitch that is connected to the specified VPC. | None |

| R | esource Orchest | ration Servic | e |   |   | User Guide·Resource type | s |
|---|---|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| AllocatePublic Connection | Boolean | No | No | Specifies whether to apply for a public endpoint for the instance. | None |   |   |
| PreferredBacku pTime | String | No | No | The backup time. | Specify the time in the HH:mm Z- HH:mmZ format. Valid values: 00:00Z-01:00Z, 01:00Z-02:00Z, 02:00Z- 03:00Z, 03:00Z-04:00Z, 04:00Z-05:00Z, 05:00Z- 06:00Z, 06:00Z-07:00Z, 07:00Z-08:00Z, 08:00Z- 09:00Z, 09:00Z-10:00Z, 10:00Z-11:00Z, 11:00Z- 12:00Z, 12:00Z-13:00Z, 13:00Z-14:00Z, 14:00Z- 15:00Z, 15:00Z-16:00Z, 16:00Z-17:00Z, 17:00Z- 18:00Z, 18:00Z-19:00Z, 19:00Z-20:00Z, 20:00Z- 21:00Z, 21:00Z-22:00Z, 22:00Z-23:00Z, and 23:00Z- 24:00Z. |   |   |
|   |   |   |   |   |   | HH:mm |   |
| BackupRetenti onPeriod | Number | No | No | The number of days for which backup files can be retained. | Valid values: 7 to 30. Unit: days. Default value: 7. |   |   |
| PrivateIpAddre ss | String | No | No | The private IP address of the instance on the specified VSwitch. | If this parameter is not specified, the system automatically allocates a private IP address. |   |   |
| PreferredBacku pPeriod | List | No | No | The backup periods. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |   |   |
| MasterUserTyp e | String | No | No | The type of the primary account. | Default value: Normal. Valid values: Normal Super |   |   |

|   | Z- HH:mmZ |
|---|---|

| Property | Type | Required | Editable | Description |   | Constraint |   |
|---|---|---|---|---|---|---|---|
| Tags | Map | No | Yes | The list of tags. Each tag consists of a TagKey and a TagValue. |   | The TagKey is required and the TagValue is optional. Format example: {"key1":" |   |
|   |   |   |   |   |   |   | {"key1":" |
|   |   |   |   |   |   | value1","key2":""} |   |
| PeriodType | String | No | No | The subscription period type. |   | Default value: Month. Valid values: Month Year |   |
| PayType | String | No | No | The billing method of the instance. |   | Valid values: PostPaid: pay-as-you-go PrePaid: subscription |   |
| Period | Integer | No | No | The subscription period of the instance. |   | Valid values when the PeriodType parameter is set to Year: 1 to 3. Valid values when the PeriodType parameter is set to Month: 1 to 9. |   |

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

| Property | Type | Required | Editable | Description | Constraint |   |   |
|---|---|---|---|---|---|---|---|
| CharacterSetName | String | Yes | No | The character set. | Valid values when Engine is set to MySQL: utf8 gbk latin1 utf8mb4 (applicable to versions 5.5 and 5.6) Valid values when Engine is set to SQLServer: Chinese PRC CI AS _ _ _ Chinese PRC CS AS _ _ _ SQL Latin1 General CP _ _ _ 1 CI AS _ _ SQL Latin1 General CP _ _ _ 1 CS AS _ _ Chinese PRC BIN _ _ |   |   |
| DBName | String | Yes | No | The name of the database. | The name must be unique. The name can be up to 64 characters in length and can contain letters, digits, and underscores ( ). It must _ start with a letter. |   |   |
| DBDescription | String | No | No | The description of the database. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with h ttp:// or https:// . |   |   |
|   |   |   |   |   |   | h |   |

Response parameters Fn::GetAtt DBInstanceId: the ID of the RDS instance. InnerPort: the internal port of the RDS instance. InnerIPAddress: the internal IP address of the RDS instance. InnerConnectionString: the internal endpoint of the RDS instance. PublicPort: the public port of the RDS instance. PublicConnectionString: the public endpoint of the RDS instance. PublicIPAddress: the public IP address of the RDS instance. Examples The following example demonstrates how to create an ApsaraDB for RDS instance in the classic network:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Database": {
      "Type": "ALIYUN::RDS::DBInstance",
        "Engine": "MySQL",
        "EngineVersion": "5.6",
        "DBInstanceClass":"rds.mysql.t1.small",
        "DBInstanceStorage": 10,
        "DBInstanceNetType": "Internet",
        "SecurityIPList": "0.0.0.0/0",
        "MasterUsername": "A****",
        "DBMappings":[{
            "DBName": "hope",
            "CharacterSetName": "utf8"
```

`}]` `},`

```json
  "Outputs": {
    "DBInstanceId": {
      "Value": {"get_attr": ["DBInstanceId"]}
```

`},`

```json
    "PublicConnectionString": {
      "Value": {"get_attr": ["ConnectionString"]}
```

`},`

```json
    "PublicPort": {
      "Value": {"get_attr": ["Port"]}
```

The following example demonstrates how to create an ApsaraDB for RDS instance in a VPC:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Database": {
      "Type": "ALIYUN::RDS::DBInstance",
        "Engine":"MySQL",
        "EngineVersion":"5.6",
        "DBInstanceClass":"rds.mys2.small",
        "DBInstanceStorage":"10",
        "DBInstanceNetType":"Intranet",
        "SecurityIPList": "0.0.0.0/0",
        "VSwitchId": "ttt",
        "VpcId": "myvp****"
```

`},`

```json
  "Outputs": {
    "DBInstanceId": {
      "Value": {"get_attr": ["DBInstanceId"]}
```

`},`

```json
    "InnerConnectionString": {
      "Value": {"get_attr": ["ConnectionString"]}
```

`},`

```json
    "InnerPort": {
      "Value": {"get_attr": ["Port"]}
```

#### 5.4.4 ALIYUN::RDS::DBInstanceParameterGroup

ALIYUN::RDS::DBInstanceParameterGroup is used to modify the parameter list of an apsaradb for RDS instance. Statement

```json
  "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
    "Forcerestart": String,
    "DBInstanceId": String,
    "Parameters": List
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | No | No | The ID of the ApsaraDB RDS instance to query. | None |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | Description | Constraint |
| Parameters | List | Yes | No | parameter. | Parameters in JSON format and their values. Example: {"auto increme _ nt increment":" _ 1","character s _ et client":"utf8 _ "}. |
| Forcerestart | String | Yes | Released | Specifies whether to force a restart of the ApsaraDB for RDS instance. | Valid values: true: specifies to forcibly restart the database. false: Do not force restart Default value: false. |

Response parameters Fn::GetAtt Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Database": {
      "Type": "ALIYUN::RDS::DBInstance",
        "Engine": "MySQL",
        "EngineVersion": "5.6",
        "DBInstanceClass": "rds.mys2.small",
        "DBInstanceStorage": "10",
        "DBInstanceNetType": "Intranet",
        "SecurityIPList": "0.0.0.0/0"
```

`},`

```json
    "DatabaseConfig": {
      "Type": "ALIYUN::RDS::DBInstanceParameterGroup",
        "DBInstanceId": {
          "Ref": "Database"
```

`},`

```json
        "Parameters": [
            "Key": "auto_increment_increment",
            "Value": "xxx"
```

`]` `},`

```json
  "Outputs": {
    "DBInstanceId": {
      "Value": {
        "Fn::GetAtt": [
          "Database",
          "DBInstanceId"
```

`]`

#### 5.4.5 ALIYUN::RDS::DBInstanceSecurityIps

ALIYUN::RDS::DBInstanceSecurityIps is used to modify the instance whitelist. Statement

```json
  "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
    "DBInstanceId": String,
    "DBInstanceIPArrayName": String,
    "DBInstanceIPArrayAttribute": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceId | String | No | No | The ID of the RDS instance. | None |
| DBInstanceIP ArrayAttribut e | String | No | Yes | The attribute of the IP address whitelist. | The console does not display groups labeled with hidden. |
| DBInstanceIP ArrayName | String | Yes | Released | The name of the IP address whitelist. | The name can contain only lowercase letters and underscores ( ). _ Default value: Default. |

Response parameters Fn::GetAtt SecurityIps: the IP address whitelist after the modification. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "DBInstanceSecurityIps": {
      "Type": "ALIYUN::RDS::DBInstanceSecurityIps",
        "DBInstanceIPArrayName": {
          "Ref": "DBInstanceIPArrayName"
```

`},`

```json
        "DBInstanceId": [
          "Ref": "DBInstanceId"
```

`},`

```json
        "DBInstanceIPArrayAttribute": {
          "Ref": "DBInstanceIPArrayAttribute"
```

`},`

```json
  "Parameters": {
    "DBInstanceIPArrayName": {
      "Type": "String",
      "Description": "Group name of the security ips, only support lower characters and '_'. Advi
ce use a new group name avoid effect your database system. If the properties is not specified, it will set to default group, please be careful."
```

`},`

```json
    "DBInstanceId": [
      "Type": "String",
      "Description": "Database instance id to update security ips."
```

`},`

```json
    "DBInstanceIPArrayAttribute": {
      "Type": "String",
      "Description": "Security ips to add or remove."
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

#### 5.4.6 ALIYUN::RDS::PrepayDBInstance

ALIYUN::RDS::PrepayDBInstance is used to create a subscription ApsaraDB for RDS instance. Statement

```json
  "Type": "ALIYUN::RDS::PrepayDBInstance",
    "DBMappings": List,
    "CouponCode": String,
    "MasterUsername": String,
    "PeriodType": String,
    "PayType": String,
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
    "EngineVersion": String,
    "DBInstanceClass": String,
    "PreferredBackupPeriod": List,
    "DBInstanceStorage": Integer,
    "DBInstanceDescription": String,
    "Tags": Map,
    "Period": Number,
    "MasterUserPassword": String,
    "AllocatePublicConnection": Boolean
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupId | String | Yes | Released | The ID of the resource group to which the RDS instance belongs. | None |
| DBMappings | List | Erased | Released | The databases created in the instance. | None |
| CouponCode | String | Yes | Released | None | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterUsername | String | Yes | Released | The name of the Apsara Stack tenant account for the instance. | The name must be unique. The name must be 1 to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a _ letter. |
| PeriodType | String | No | No | The type of the billing cycle. | Valid values: Year Month Default value: Month. |
| DBInstanceNetTy pe | String | Yes | Released | The network type of the instance. | Valid values: Internet: used for access from public networks. Intranet: used for private network access. Default value: Intranet. |
| MasterUserType | String | Yes | Released | The permission type of the account. | Valid values: Normal Master |
| PreferredBackup Time | String | Yes | Released | The preferred backup time. | Specify the time in the HH:mmZ- HH:mmZ format. Valid values: 00:00Z- 01:00Z, 01:00Z-02:00Z, 02:00Z-03:00Z, and 03:00Z-04:00 to 23:00Z-24:00Z. |
| PrivateIpAddress | String | Yes | Released | The private IP address of the instance on the specified VSwitch. | If this parameter is not specified, the system automatically assigns a value. |
| Engine | String | No | No | The database engine that the instance runs. | Valid values: MySQL SQLServer PostgreSQL PPAS |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MultiAZ | Boolean | Erased | Released | Specifies whether the instance can be deployed across multiple zones. | None |
| VpcId | String | Yes | Released | The ID of the VPC. | None |
| ConnectionMode | String | Yes | Released | The access mode of the instance. | Valid values: Performance: a standard access mode. Safty: high security access mode. If this parameter is not specified, apsaradb for RDS immediately assigns a value to it. Default value: Safty |
| AutoRenew | Boolean | Erased | Released | Specifies whether to enable automatic renewal for the instance. | Valid values: True False |
| VSwitchId | String | Yes | Released | The ID of the VSwitch in the specified VPC. | None |
| BackupRetention Period | Number | Erased | Released | The retention period of backup data. Unit: days. | None |
| Quantity | Number | Erased | Released | The number of instances to be created. | Valid values: 1 to 99. Default value: 1 |
| CommodityCode | String | No | No | The commodity code. | Valid values: rds bards rords |
| ZoneId | String | Yes | Released | The ID of the zone where the instance resides. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| EngineVersion | String | No | No | The version of the database engine that the instance runs. | The range of valid engine version values varies by database type. For an ApsaraDB RDS for MySQL instance, the valid values are 5.5 and 5.6. For an ApsaraDB RDS for SQL Server instance, set the value to 2008r2. For an ApsaraDB RDS for PostgreSQL instance, set the value to 9.4. For an ApsaraDB RDS for PPAS instance, set the value to 9.3. |
| DBInstanceClass | String | No | Yes | The specification of the instance. | Examples of RDS instance types: rds.mys2.large, rds.mss1.large, and rds.pg.s1.small. |
| PreferredBackup Period | List | Erased | Released | The list of preferred backup periods. | Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| DBInstanceStora ge | Integer | Retained | Yes | The storage capacity of the instance. | The range of valid storage capacity values varies by database type. MySQL: 5 to 1000 SQL Server: 10 to 1000 PostgreSQL and PPAS: 5 to 2000 Unit: GB. Every 5GB. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBInstanceDescri ption | String | Yes | Released | The description of the instance. | The value must be 2 to 256 bytes in length. It must start with a letter and cannot start with http:// or https://. It must start with a letter and cannot start with http:// or https://. |
| Tags | MAP | No. | True | The tags of the instance. | None |
| Period | Number | Yes | No | The subscription period of the instance. | Select monthly payment. Valid values: 1 to 9. Select pay by year. Valid values: 1 to 3. |
| MasterUserPass word | String | Yes | Released | The password of the Apsara Stack tenant account for the instance. | The password must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |
| AllocatePublicCo nnection | Boolean | Erased | Released | Specifies whether to apply for a public connection string for the instance. | None |
| PayType | String | Yes | Released | The billing method of the router interface. | Valid values: Postpaid: pay-as- you-go Prepaid: Subscription |
| AutoPay | Boolean | Erased | Released | Specifies whether to enable automatic payment. | Valid values: True False Default value: False. |

DBMappings syntax

```json
"DBMappings": [
    "DBDescription": String,
    "CharacterSetName": String,
    "DBName": String
```

`]` DBMappings properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| DBDescription | String | Yes | Released | The description of the database. | The description must be 2 to 256 characters in length It cannot start with http:// or https://. It must start with a letter and cannot start with http:// or https://. |
| CharacterSetName | String | No | No | The character set of the database. | Valid values: Valid values for MySQL: utf8 \| gbk \| latin1 \| utf8mb4 (applicable to version 5.5 and 5.6). Valid values for an SQL Server database: Chinese PRC CI AS, _ _ _ Chinese PRC CS AS, _ _ _ SQL Latin1 General CP1 _ _ _ _ CI AS, _ SQL Latin1 General CP1 _ _ _ _ CS AS, and _ Chinese PRC BIN. _ _ |
| DBName | String | No | No | The name of the database. | The name must be unique. It can be up to 64 characters in length and can contain lowercase letters, digits, and underscores ( ). It must _ start with a lowercase letter. |

Response parameters Fn::GetAtt InnerPort: the internal port of the RDS instance. OrderId: the ID of the order. PublicConnectionString: public network connection string. InnerIPAddress: the internal IP address of the instance. DBInstanceId: the ID of the RDS instance. PublicIPAddress: the public IP address of the instance. PublicPort: The public port of the RDS instance. InnerConnectionString: intranet connection string. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Parameters": {
    "PeriodType": {
      "Type": "String",
"Description":"Chargeperiodforcreatedinstances"
```

```json
      Description: Charge period for created instances.,
      "AllowedValues": [
        "Month",
        "Year"
```

`],`

```json
      "Default": "Month"
```

`},`

```json
    "PrivateIpAddress": {
      "Type": "String",
      "Description": "The private ip for created instance."
```

`},`

```json
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
```

`},`

```json
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
```

`},`

```json
    "PreferredBackupPeriod": {
      "Type": "CommaDelimitedList",
      "Description": "Automate backups cycle if automated backups are enabled.",
      "AllowedValues": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
```

`]` `},`

```json
    "DBInstanceStorage": {
      "Type": "Number",
      "Description": "Database instance storage size. mysql is [5,1000]. sql server 2008r2 is [10
,1000], sql server 2012/2012_web/2016-web is [20,1000]. PostgreSQL and PPAS is [5,2000]. Increase d every 5 GB, Unit in GB"
```

`},`

```json
    "CommodityCode": {
      "Type": "String",
      "Description": "The CommodityCode of the order.",
      "AllowedValues": [
        "rds",
        "bards",
```

`,`

```
        "rords"
```

`],`

```json
      "Default": "rds"
```

`},`

```json
    "DBMappings": {
      "Type": "CommaDelimitedList",
      "Description": "Database mappings to attach to db instance."
```

`},`

```json
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
```

`},`

```json
    "Engine": {
      "Type": "String",
      "Description": "Database instance engine type. Support MySQL/SQLServer/PostgreSQL/PPAS now.
```

`",`

```json
      "AllowedValues": [
        "MySQL",
        "SQLServer",
        "PostgreSQL",
        "PPAS"
```

`]` `},`

```json
    "DBInstanceDescription": {
      "Type": "String",
      "Description": "Description of created database instance."
```

`},`

```json
    "Tags": {
      "Type": "Json",
      "Description": "The tags of an instance.\nYou should input the information of the tag with
the format of the Key-Value, such as {\"key1\":\"value1\",\"key2\":\"value2\", ... \"key5\":\"val ue5\"}.\nAt most 5 tags can be specified.\nKey\nIt can be up to 64 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or https://.\nCannot be a null string.\nValue\nIt c an be up to 128 characters in length.\nCannot begin with aliyun.\nCannot begin with http:// or ht tps://.\nCan be a null string."
```

`},`

```json
    "EngineVersion": {
      "Type": "String",
      "Description": "Database instance version of the relative engine type.Support MySQL: 5.5/5.
6/5.7; SQLServer: 2008r2, 20012, 2012_web, 2012_std_ha, 2012_ent_ha, 2016_web, 2016_std_ha, 2016_ ent_ha; PostgreSQL:9.4; PPAS: 9.3.",
      "AllowedValues": [
        "5.5",
        "5.6",
        "5.7",
        "2008r2",
        "2012",
        "2012_web",
        "2012_std_ha",
```

```
        "2012_ent_ha",
        "2016_web",
        "2016_std_ha",
        "2016_ent_ha",
        "9.4",
        "9.3"
```

`]` `},`

```json
    "ZoneId": {
      "Type": "String",
      "Description": "selected zone to create database instance. You cannot set the ZoneId parame
ter if the MultiAZ parameter is set to true."
```

`},`

```json
    "DBInstanceClass": {
      "Type": "String",
      "Description": "Database instance type. Refer the RDS database instance type reference, suc
h as 'rds.mys2.large', 'rds.mss1.large', 'rds.pg.s1.small' etc"
```

`},`

```json
    "AllocatePublicConnection": {
      "Type": "Boolean",
      "Description": "If true, allocate public connection automate.",
      "AllowedValues": [
        "True",
        "true",
        "False",
        "false"
```

`]` `},`

```json
    "PreferredBackupTime": {
      "Type": "String",
      "Description": "The daily time range during which automated backups are created if automate
d backups are enabled.",
      "AllowedValues": [
        "00:00Z-01:00Z",
        "01:00Z-02:00Z",
        "02:00Z-03:00Z",
        "03:00Z-04:00Z",
        "04:00Z-05:00Z",
        "05:00Z-06:00Z",
        "06:00Z-07:00Z",
        "07:00Z-08:00Z",
        "08:00Z-09:00Z",
        "09:00Z-10:00Z",
        "10:00Z-11:00Z",
        "11:00Z-12:00Z",
        "12:00Z-13:00Z",
        "13:00Z-14:00Z",
        "14:00Z-15:00Z",
        "15:00Z-16:00Z",
        "16:00Z-17:00Z",
        "17:00Z-18:00Z",
        "18:00Z-19:00Z",
        "19:00Z-20:00Z",
        "20:00Z-21:00Z",
        "21:00Z-22:00Z",
        "22:00Z-23:00Z",
        "23:00Z-24:00Z"
```

`]` `]` `},`

```json
    "VSwitchId": {
      "Type": "String",
      "Description": "The vSwitch id of created instance. For VPC network, the property is requir
ed."
```

`},`

```json
    "Quantity": {
      "Type": "Number",
      "Description": "The number of instance to be created, default is 1, max number is 99",
      "MinValue": 1,
      "MaxValue": 99,
      "Default": 1
```

`},`

```json
    "Period": {
      "Type": "Number",
      "Description": "Prepaid time period. While choose by pay by month, it could be from 1 to 9.
While choose pay by year, it could be from 1 to 3.",
      "MinValue": 1,
      "MaxValue": 9,
      "Default": 1
```

`},`

```json
    "MasterUserPassword": {
      "Type": "String",
      "Description": "The master password for the database instance. ",
      "MinLength": 8,
      "MaxLength": 32
```

`},`

```json
    "CouponCode": {
      "Type": "String",
      "Description": "The coupon code of the order."
```

`},`

```json
    "MasterUserType": {
      "Type": "String",
      "Description": "Privilege type of account.\n Normal: Common privilege. \n Super: High privi
lege. And the default value is Normal.This parameter is valid for MySQL 5.5/5.6 only. MySQL 5.7, SQL Server 2012/2016, PostgreSQL, and PPAS each can have only one initial account. \nOther accoun ts are created by the initial account that has logged on to the database.",
      "AllowedValues": [
        "Normal",
        "Super"
```

`],`

```json
      "Default": "Normal"
```

`},`

```json
    "VpcId": {
      "Type": "String",
      "Description": "The VPC id of created database instance. For VPC network, the property is r
equired."
```

`},`

```json
    "MasterUsername": {
      "Type": "String",
      "Description": "The master user name for the database instance. "
```

`},`

```json
    "ConnectionMode": {
      "Type": "String",
      "Description": "Connection Mode for database instance,support 'Performance' and 'Safty' mod
e. Default is RDS system assigns. ", "AllowedValues":[
```

```
      AllowedValues: [
        "Performance",
        "Safty"
```

`]` `},`

```json
    "BackupRetentionPeriod": {
      "Type": "Number",
      "Description": "The number of days for which automatic DB backups are retained.",
      "MinValue": 7,
      "MaxValue": 30,
      "Default": 7
```

`},`

```json
  "Resources": {
    "PrepayDBInstance": {
      "Type": "ALIYUN::RDS::PrepayDBInstance",
        "PeriodType": {
          "Ref": "PeriodType"
```

`},`

```json
        "PrivateIpAddress": {
          "Ref": "PrivateIpAddress"
```

`},`

```json
        "DBInstanceNetType": {
          "Ref": "DBInstanceNetType"
```

`},`

```json
        "AutoRenew": {
          "Ref": "AutoRenew"
```

`},`

```json
        "PreferredBackupPeriod": {
          "Fn::Split": [
            ",",
              "Ref": "PreferredBackupPeriod"
```

`},`

```json
              "Ref": "PreferredBackupPeriod"
```

`]` `},`

```json
        "DBInstanceStorage": {
          "Ref": "DBInstanceStorage"
```

`},`

```json
        "CommodityCode": {
          "Ref": "CommodityCode"
```

`},`

```json
        "DBMappings": {
          "Fn::Split": [
            ",",
              "Ref": "DBMappings"
```

`},`

```json
              "Ref": "DBMappings"
```

`]` `},`

```json
        "MultiAZ": {
```

```json
          "Ref": "MultiAZ"
```

`},`

```json
        "Engine": {
          "Ref": "Engine"
```

`},`

```json
        "DBInstanceDescription": {
          "Ref": "DBInstanceDescription"
```

`},`

```json
        "Tags": {
          "Ref": "Tags"
```

`},`

```json
        "EngineVersion": {
          "Ref": "EngineVersion"
```

`},`

```json
        "ZoneId": {
          "Ref": "ZoneId"
```

`},`

```json
        "DBInstanceClass": {
          "Ref": "DBInstanceClass"
```

`},`

```json
        "AllocatePublicConnection": {
          "Ref": "AllocatePublicConnection"
```

`},`

```json
        "PreferredBackupTime": {
          "Ref": "PreferredBackupTime"
```

`},`

```json
        "VSwitchId": {
          "Ref": "VSwitchId"
```

`},`

```json
        "Quantity": {
          "Ref": "Quantity"
```

`},`

```json
        "Period": {
          "Ref": "Period"
```

`},`

```json
        "MasterUserPassword": {
          "Ref": "MasterUserPassword"
```

`},`

```json
        "CouponCode": {
          "Ref": "CouponCode"
```

`},`

```json
        "MasterUserType": {
          "Ref": "MasterUserType"
```

`},`

```json
        "VpcId": {
          "Ref": "VpcId"
```

`},`

```json
        "MasterUsername": {
          "Ref": "MasterUsername"
```

`},`

```json
        "ConnectionMode": {
          "Ref": "ConnectionMode"
```

`},`

```json
        "BackupRetentionPeriod": {
          "Ref": "BackupRetentionPeriod"
```

`},`

```json
  "Outputs": {
    "InnerConnectionString": {
      "Description": "DB instance connection url by Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerConnectionString"
```

`]` `},`

```json
    "DBInstanceId": [
      "Description": "The instance id of created database instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "DBInstanceId"
```

`]` `},`

```json
    "InnerIPAddress": {
      "Description": "IP Address for created DB instance of Intranet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerIPAddress"
```

`]` `},`

```json
    "PublicConnectionString": {
      "Description": "DB instance connection url by Internet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicConnectionString"
```

`]` `},`

```json
    "PublicIPAddress": {
      "Description": "IP Address for created DB instance of Internet.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicIPAddress"
```

`]` `},`

```json
    "OrderId": {
      "Description": "The order id list of created instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "OrderId"
```

`]` `},`

```json
"PublicPort":{
```

```json
    PublicPort: {
      "Description": "Internet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "PublicPort"
```

`]` `},`

```json
    "InnerPort": {
      "Description": "Intranet port of created DB instance.",
      "Value": {
        "Fn::GetAtt": [
          "PrepayDBInstance",
          "InnerPort"
```

`]`

### 5.5 ROS

#### 5.5.1 ALIYUN::ROS::WaitCondition

ALIYUN::ROS::WaitCondition is used to create an instance to process UserData messages. Statement

```json
  "Type": "ALIYUN::ROS::WaitCondition",
    "Count": Number,
    "Handle": String,
    "Timeout": Number
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Handle | String | No | No | Reference ALIYUN::ROS:: WaitConditionH andle. | None |
| Timeout | Number | Yes | No | The length of time to wait for UserData messages. | Valid values: 1 to 43200. Unit: seconds. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Count | Number | No. | True | The total number of messages to be received. | None |

Response parameters Fn::GetAtt Data: A JSON-serialized dictionary that contains the signal Data after the most recent stack creation or update. LastData: a JSON-serialized dictionary that contains the signal data before the most recent stack update. JoinedErrorData: a string consisting of the ErrorData signal data. JoinedLastErrorData: a string consisting of the LastErrorData signal data. ErrorData: a JSON-serialized dictionary that contains the error signal data after the most recent stack creation or update. Lasterprotodata: a JSON-serialized dictionary that contains the error signal data before the most recent stack update. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "WaitCondition": {
      "Type": "ALIYUN::ROS::WaitCondition",
        "Handle": {
          "Ref": "WaitConHandle"
```

`},`

```json
        "Timeout": 5,
        "Count": 2
```

`},`

```json
    "WaitConHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle"
```

`},`

```json
  "Outputs": {
    "CurlCli": {
      "Value": {
        "Fn::GetAtt": [
          "WaitConHandle",
          "CurlCli"
```

`]` `},`

```json
    "Data": {
      "Value": {
        "Fn::GetAtt": [
          "WaitCondition",
          "Data"
```

`]`

#### 5.5.2 ALIYUN::ROS::WaitConditionHandle

ALIYUN::ROS::WaitConditionHandle is used to create an instance that sends and receives messages during UserData execution. Statement

```json
  "Type": "ALIYUN::ROS::WaitConditionHandle",
    "Count": Integer,
    "Mode": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Count | Integer | No. | True | The total number of messages to be received. | Default value: - 1. |
| Mode | String | Yes | True | If you set this parameter to Increment, all previous signals will be updated before they are deleted. If you set this parameter to Full, no previous signals will be deleted unless the Count parameter is specified. | Valid values: Increment Full Default value: Full. |

Response parameters Fn::GetAtt CurlCli: A curl Command is generated by the resource. You can use the command to send the UserData execution result or status to Resource Orchestration Service. WindowsCurlCli: provides Windows with cURL CLI command prefixes and sends a message indicating that the execution is completed or failed. Windows does not support the curl command. Therefore, you must install

| PATH. You can add | --data-binary "{\"status\": \" success \"} |   |
|---|---|---|
| --data-binary "{\"status\": \" failure \"} |   | to indicate failure. |

PowerShellCurlCli: provides PowerShell with cURL CLI command prefixes and sends a message indicating that the execution is completed or failed. Because this cmdlet was introduced in PowerShell 3.0, make sure

| $PSVersionTable.PSVersion |   | displays the version. |
|---|---|---|
| ndicate success, or by adding | -Body '{"status": "fa |   |

that the PowerShell version meets this constraint. By $PSVersionTable.PSVersion displays the version. `ilure "}` to indicate failure. Sample request

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

`],` `],`

```json
      "Default": "Full"
```

`},`

```json
    "Count": {
      "Type": "Number",
      "Description": "There are 3 preconditions that make Count taking effect:\n1.Mode is set to
Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing in teger started from 1. For example, the id of the first signal is 1, the id of the second signal i s 2, and so on.\n\nIf Count takes effect, signals with id > Count will be deleted before update.\ nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
      "Default": -1
```

`},`

```json
  "Resources": {
    "WaitConditionHandle": {
      "Type": "ALIYUN::ROS::WaitConditionHandle",
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
      "Description": "Convenience attribute, provides curl CLI command prefix, which can be used
for signalling handle completion or failure. You can signal success by adding --data-binary '{\" status\": \"SUCCESS\"}' , or signal failure by adding --data-binary '{\"status\": \"FAILURE\"}'",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "CurlCli"
```

`]` `},`

```json
    "WindowsCurlCli": {
      "Description": "Convenience attribute, provides curl CLI command prefix for Windows, which
can be used for signalling handle completion or failure. As Windows does not support curl command , you need to install curl.exe and add it to PATH first. You can signal success by adding --databinary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or signal failure by adding --data-binary \"{\\\"s tatus\\\": \\\"FAILURE\\\"}\" ",
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "WindowsCurlCli"
```

`]` `},`

```json
    "PowerShellCurlCli": {
      "Description": "Convenience attribute, provides curl CLI command prefix for PowerShell, whi
ch can be used for signalling handle completion or failure. As this cmdlet was introduced in Powe rShell 3.0, ensure the version of PowerShell satisfies the constraint. (Show the version via $PSV ersionTable.PSVersion.) You can signal success by adding -Body '{\"status\": \"SUCCESS\"}' , or s ignal failure by adding -Body '{\"status\": \"FAILURE\"}' ",
```

```json
      "Value": {
        "Fn::GetAtt": [
          "WaitConditionHandle",
          "PowerShellCurlCli"
```

`]`

#### 5.5.3 ALIYUN::ROS::Stack

ALIYUN::ROS::Stack is used to create a nested stack. You can have a maximum of five nested levels. ALIYUN::ROS::Stack is used in a top-level template to nest stacks as resources. You can add output values from a nested stack contained within the template. You can use Fn::GetAtt together with the logical name of the nested stack and the output name in the Outputs.NestedStackOutputName format. Not e We recommend that you run an update to the Nested stack from the parent stack. When you apply a template change to update a top-level stack, ROS updates the top-level stack and initiates an update to its nested stacks. Resource orchestration service (ROS) updates resources that have been modified in the nested stack, but does not update resources that have not been modified in the nested stack. Statement

```json
  "Type": "ALIYUN::ROS::Stack",
    "TemplateURL": String,
    "TimeoutMins": Number,
    "Parameters": Map
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type |   | Required |   |   | Editable |   | Description |   | Constraint |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TemplateURL | String |   | No |   |   | Yes |   | The URL of the file containing the template body. The template file can be up to 524,288 bytes in size. The URL must point to a template located on the http or https Web server or Alibaba Cloud OSS bucket. For example: oss://ros/t emplate/demo , oss://ros/t |   | The URL can be up to 1,024 bytes in length. |   |
|   |   |   |   |   |   |   |   |   | oss://ros/t | up to 1,024 |   |
|   |   |   |   |   |   |   |   | emplate/demo |   |   |   |
|   |   |   |   |   |   |   |   | emplate/demo? |   |   |   |
|   |   |   |   |   |   |   |   | RegionId=cn- |   |   |   |
|   |   |   |   |   |   |   |   | hangzhou |   |   |   |
| TimeoutMins | Number |   | No. |   |   | True |   | The length of time that ROS will wait for the nested stack to be created or updated. |   | Unit: minutes. Default value: 60. |   |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Parameters | Map | No. | True | A set of value pairs that represent the parameters passed to ROS when this Nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and the value to which you want to set the parameter. This parameter is required if the nested stack needs input parameters. | None |

Response parameters Fn::GetAtt You can use the following code to obtain the output of the nested stack:

```
  "Fn::GetAtt": [
    "<nested_stack>",
    "Outputs.<nested_stack_output_name>"
```

`]` When you use `Ref` to reference resources in a nested stack, the Alibaba Cloud Resource Name (ARN) of the nested stack is returned. Example: `arn:acs:ros::cn-hangzhou:12345****:stacks/test-nested-stack-Demo-`

```
jzkyq7mn2ykj/e71c1e04-1a57-46fc-b9a4-cf7ce0d3****
```

Examples The following code provides an example of how to create a VPC, a VSwitch, and a security group in a nested stack and save the output results to the oss://ros/template/vpc.txt directory:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One VPC, VSwitch, security group.",
  "Parameters": {
    "ZoneId": {
      "Type": "String",
      "Description": "The available zone"
```

`},`

```json
    "SecurityGroupName": {
```

```json
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
    "Vpc": {
      "Type": "ALIYUN::ECS::VPC",
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
        "Fn::GetAtt": [
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

`]` The following code provides an example of a top-level stack:

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Description": "One ECS instance.",
  "Parameters": {
    "ImageId": {
```

```json
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
      "Description": "System disk category: average cloud disk(cloud), efficient cloud disk(clo
ud_efficiency) or SSD cloud disk(cloud_ssd)", "Tpe" "String"
```

```json
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
        "ImageId": {
          "Ref": "ImageId"
```

`},`

```json
        "InstanceType": {
          "Ref": "InstanceType"
```

`e` `:`

```
staceype
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

### 5.6 SLB

#### 5.6.1 ALIYUN::SLB::AccessControl

ALIYUN::SLB::AccessControl is used to create an access control list (ACL). Syntax

```json
  "Type": "ALIYUN::SLB::AccessControl",
    "AddressIPVersion": String,
    "AclName": String,
    "AclEntrys": List
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AddressIPVersio n | String | No | No | The Internet protocol version. | Valid values: ipv4 and ipv6. |
| AclName | String | Yes | Yes | The name of the ACL. | None |
| AclEntrys | List | No | No | The list of ACL entries. | A list can contain up to 50 ACL entries. |

AclEntrys syntax

```json
"AclEntrys": [
    "comment": String,
    "entry": String
```

`]` AclEntrys properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| comment | String | No | No | The comments on ACL entries. | None |
| entry | String | Yes | No | The authorized IP addresses or CIDR blocks. | None |

Response parameters Fn::GetAtt AclId: the ID of the ACL. Examples Resource usage example

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AccessControl": {
      "Type": "ALIYUN::SLB::AccessControl",
        "AddressIPVersion": {
          "Ref": "AddressIPVersion"
```

`},`

```json
        "AclName": {
          "Ref": "AclName"
```

`},`

```json
        "AclEntrys": {
          "Fn::Split": [",", {
            "Ref": "AclEntrys"
          }, {
            "Ref": "AclEntrys"
```

`}]` `},`

```json
  "Parameters": {
    "AddressIPVersion": {
      "Type": "String",
      "Description": "IP version. Could be \"ipv4\" or \"ipv6\".",
      "AllowedValues": ["ipv4", "ipv6"]
```

`},`

```json
    "AclName": {
      "Type": "String",
      "Description": "The name of the access control list."
```

`},`

```json
    "AclEntrys": {
      "Type": "CommaDelimitedList",
      "Description": "A list of acl entrys. Each entry can be IP addresses or CIDR blocks. Max le
ngth: 50.",
      "MaxLength": 50
```

`},`

```json
  "Outputs": {
    "AclId": {
      "Description": "The ID of the access control list.",
      "Value": {
        "Fn::GetAtt": ["AccessControl", "AclId"]
```

Example of combined use of SLB-related resources

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
"Properties":{
```

```json
        "LoadBalancerName": "slb-with-listener-and-acl",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth",
        "Bandwidth": 10,
        "VpcId": "vpc-xxxxxxxxxxxxxxxxxxxx",
        "VSwitchId": "vsw-xxxxxxxxxxxxxxxxxxxx"
```

`},`

```json
    "ACL": {
      "Type": "ALIYUN::SLB::AccessControl",
        "AclName": "acl-for-listener",
        "AddressIPVersion": "ipv4",
        "AclEntrys": [
            "entry": "192.168.x.x"
```

`},`

```json
            "entry": "10.0.x.x/24",
            "comment": "just comment"
```

`]` `},`

```json
    "CreateListener": {
      "Type": "ALIYUN::SLB::Listener",
        "LoadBalancerId": {
          "Ref": "LoadBalancer"
```

`},`

```json
        "ListenerPort": "80",
        "BackendServerPort": 8080,
        "Bandwidth": 1,
        "Protocol": "http",
        "HealthCheck": {
          "HealthyThreshold": 3,
          "UnhealthyThreshold": 3,
          "Interval": 2,
          "Timeout": 5
```

`},`

```json
        "Scheduler": "wrr",
        "RequestTimeout": 179,
        "IdleTimeout": 59,
        "AclId": {
          "Ref": "ACL"
```

`},`

```json
        "AclStatus": "on",
        "AclType": "white"
```

`},`

```json
  "Outputs": {
    "LoadBalanceDetails": {
      "Value": {
        "Fn::GetAtt": [
          "LoadBalancerId",
          "Listeners"
```

`]`

#### 5.6.2 ALIYUN::SLB::BackendServerAttachment

ALIYUN::SLB::BackendServerAttachment is used to add backend servers. Statement

```json
  "Type": "ALIYUN::SLB::BackendServerAttachment",
    "LoadBalancerId": String,
    "BackendServers": List,
    "BackendServerList": List,
    "BackendServerWeightList": List
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerId | String | No | No | The unique ID of the SLB instance. | None |
| BackendServerLi st | List | No. | True | The list of backend servers to add. | You can call this operation with LoadBalancerId and BackendServer WeightList. Separate ECS instance IDs with commas (,). This parameter is ignored when the BackendServers parameter is specified. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| BackendServer WeightList | List | No. | True | The weights of the ECS instances in the BackendServerLi st, which are specified in order. | If this parameter is not specified, the weight of all ECS instances included in the BackendServerLi st is 100. When the BackendServer WeightList length is less than BackendServerLi st, the last value in the BackendServer WeightList is used to weight the remaining ECS instances in the BackendServerLi st. |
| BackendServers | List | No. | True | The list of backend servers to add. | Only backend servers in the running state can be attached to the SLB instance. |

BackendServers syntax

```json
"BackendServers": [
    "ServerId" : String,
    "Weight" : Integer
```

`]` BackendServers properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | No | Yes | The ID of the ECS instance that acts as a backend server. | The ECS instance must be in the Running state. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Weight | Integer | Retained | Yes | The weight of the ECS instance in the SLB instance. | Valid values: 0 to 100. Default value: 100. |

Response parameters Fn::GetAtt BackendServers: the backend servers added to the SLB instance. LoadBalancerId: the ID of the SLB instance. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Attachment2": {
      "Type": "ALIYUN::SLB::BackendServerAttachment",
        "LoadBalancerId": "15187200816-cn-beijing-btc-****",
        "BackendServerList": [
          "i-25o0m****",
          "i-25zsk****"
```

`],`

```json
        "BackendServerWeightList": [
          "20",
          "100"
```

`]`

#### 5.6.3 ALIYUN::SLB::BackendServerToVServerGroupAddition

ALIYUN::SLB::BackendServerToVServerGroupAddition is used to add backend servers to an existing VServer group. Statement

```json
  "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
    "BackendServers": List,
    "VServerGroupId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGroupId | String | No | No | The ID of the VServer group. | None |
| BackendServers | List | Retained | Yes | The list of ECS instances to be added. | None |

BackendServers syntax

```json
"BackendServers": [
    "ServerId": String,
    "Port": Integer,
    "Weight": Integer
```

`]` BackendServers properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | No | Yes | The ID of the ECS instance that acts as a backend server. | None |
| Port | Integer | Retained | Yes | The ECS port number that is listened to in the server load balancer instance. | Valid values: 1 to 65535. |
| Weight | Integer | Retained | Yes | The weight of the ECS instance to be attached to the SLB instance. | Valid values: 0 to 100. |

Response parameters Fn::GetAtt VServerGroupId: the ID of the VServer group. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "AttachVServerGroup": {
      "Type": "ALIYUN::SLB::BackendServerToVServerGroupAddition",
        "VServerGroupId": "sg-2zenh4ndwrqg14yt0****",
        "BackendServers": [
            "ServerId": "i-25zsk****",
            "Weight": 20,
            "Port": 8080
```

`},`

```json
            "ServerId": "i-25zsk****",
            "Weight": 100,
            "Port": 8081
```

`]`

#### 5.6.4 ALIYUN::SLB::Certificate

ALIYUN::SLB::Certificate is used to upload a certificate to an SLB instance. Server certificates and CA certificates are supported. Not ice You can upload only one CA certificate at a time ("CertificateType": "CA "). You can upload only one server certificate and the corresponding private key at a time ("CertificateType": "Server "). Syntax

```json
  "Type": "ALIYUN::SLB::Certificate",
    "CertificateName": String,
    "Certificate": String,
    "AliCloudCertificateName": String,
    "PrivateKey": String,
    "ResourceGroupId": String,
    "CertificateType": String,
    "AliCloudCertificateId": String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ResourceGroupI d | String | No | No | The ID of the resource group. | None |
| CertificateName | String | No | Yes | The name of the certificate. | None |
| Certificate | String | Yes | No | The public key of the certificate. | None |
| AliCloudCertific ateName | String | No | No | The name of the Alibaba Cloud certificate. | None |
| PrivateKey | String | No | No | The server private key that you want to upload. | None |
| AliCloudCertific ateId | String | No | No | The ID of the Alibaba Cloud certificate. | This parameter is required if you use a certificate from Alibaba Cloud SSL Certificates Service. |
| CertificateType | String | No | No | The type of the certificate. | Valid values: Server and CA. |

Response parameters Fn::GetAtt CertificateId: the ID of the certificate. Fingerprint: the fingerprint of the certificate. Examples

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
    "CertificateName": {
      "Type": "String",
      "Description": "The name of the certificate."
```

`},`

```json
    "Certificate": {
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
    "Certificate": {
      "Type": "ALIYUN::SLB::Certificate",
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
        "CertificateName": {
          "Ref": "CertificateName"
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
          "Certificate",
          "Fingerprint"
```

`]` `},`

```json
    "CertificateId": {
      "Description": "The ID of the certificate.",
      "Value": {
        "Fn::GetAtt": [
          "Certificate",
```

```
          "CertificateId"
```

`]`

#### 5.6.5 ALIYUN::SLB::DomainExtension

ALIYUN::SLB::DomainExtension is used to create a domain extension for an SLB instance. Statement

```json
  "Type": "ALIYUN::SLB::DomainExtension",
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

#### 5.6.6 ALIYUN::SLB::Listener

ALIYUN::SLB::Listener is used to create a listener for an SLB instance. Statement

```json
  "Type": "ALIYUN::SLB::Listener",
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
    "VServerGroupId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| MasterSlaveSer verGroupId | String | Yes | Released | The ID of the active/standby server group. | None |
| AclStatus | String | Yes | Released | Specifies whether to enable access control on the listener. | Valid values: on off Default value: off. |
| AclId | String | Yes | Released | The ID of the access control list (ACL) to which the listener is bound. This parameter is required when the AclStatus parameter is set to on. | None |
|   |   |   |   | The type of the ACL. Valid values: white and black. white: specifies the |   |

| User Guide·Resourc | e types |   |   | Resource Or | chestration Servic |
|---|---|---|---|---|---|
| Parameter | Type | Required | Editable | ACL as a Description whitelist. | Constraint |
| AclType | String | Yes | Released | Only requests from the IP addresses or CIDR blocks specified in the ACL are forwarded. Whitelists are applicable to scenarios where you want an application to only be accessed from specific IP addresses. Configuring a whitelist poses risks to your services. After a whitelist is configured, only the IP addresses specified in the whitelist are able to access the SLB listener. If a whitelist is enabled without any IP addresses specified, the SLB listener will not forward any requests. black: specifies the ACL as a blacklist. Requests from the IP addresses or CIDR blocks specified in the ACL are not forwarded. Blacklists are applicable to | Valid values: White Black |

| Parameter | Type | Required | Editable | scenarios Description where you | Constraint |
|---|---|---|---|---|---|
|   |   |   |   | want an application to only be denied access from specific IP addresses. If a blacklist is enabled without any IP addresses specified, the SLB listener will forward all requests. This parameter is required when the AclStatus parameter is set to on. |   |
| Protocol | String | No | No | The Internet protocol over which the listener will forward requests. | Valid values: http https tcp udp |
| ListenerPort | Integer | Yes | No | The frontend port used by the SLB instance. | Valid values: 1 to 65535. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Bandwidth | Integer | Yes | No | The peak bandwidth of the listener. Unit: Mbit/s. | Valid values:-1 and 1 to 1000. For an SLB instance that is connected to the Internet and billed by fixed bandwidth, this parameter cannot be set to -1, and the sum of peak bandwidth values assigned to different listeners cannot exceed the Bandwidth value specified when the SLB instance is created. For an SLB instance that is connected to the Internet and billed by traffic, this parameter can be set to -1. Unit: Mbit/s. |
| BackendServerP ort | Integer | Yes | No | The backend port used by the SLB instance. | Valid values: 1 to 65535. |
| LoadBalancerId | String | No | No | The ID of the SLB instance. | None |
| HealthCheck | Map | Erased | Released | The health check settings of the listener. | None |

| R | esource Orchestr | ation Service |   |   | User Gui | de·Resource type | s |
|---|---|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Persistence | Map | Erased | Released | The persistence properties. | None |
| Scheduler | String | Yes | Released | The algorithm used to direct traffic to individual servers. | Valid values: wrr wlc Default value: wrr |
| CACertificateId | String | Yes | Released | The ID of the CA certificate. | Only valid for. HTTPS |
| ServerCertificat eId | String | Yes | Released | The ID of the server certificate. | This parameter is required and valid only for HTTPS listeners. |
| VServerGroupId | String | Yes | Released | The ID of the VServer group. | None |
| RequestTimeou t | String | Optional | Released | The request timeout period. Unit: seconds. | Valid values: 1 to 180. |
| IdleTimeout | String | Optional | Released | The idle connection timeout period. Unit: seconds. | Valid values: 1 to 60. |
| HttpConfig | Map | Erased | Released | The HTTP configurations. | None |

HealthCheck syntax

```json
"HealthCheck": {
  "Domain": String,
  "Interval": Integer,
  "URI": String,
  "HttpCode": String,
  "HealthyThreshold": Integer,
  "Timeout": Integer,
  "UnhealthyThreshold": Integer,
  "Port": Integer
```

HealthCheck properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Domain | String | Yes | Released | The domain name used for health checks. | The value can be $ ip, _ a custom string, or an empty string. A custom string must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), and periods (.). When this parameter is set to $ ip or _ left empty, the SLB instance uses the private IP addresses of backend servers as the domain names for health checks. |
| Interval | String | Optional | Released | The time interval between consecutive health checks. Unit: seconds. | Valid values: 1 to 5. Unit: seconds. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| URI | String | Yes | Released | The URI used for health checks. | The URI must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). It must start with a forward slash (/). |
| HttpCode | String | Yes | Released | The HTTP status code that indicates a positive health status of the backend servers. | Valid values: http 2xx, _ http 3xx, _ http 4xx, _ and http 5xx. _ Separate multiple HTTP status codes with commas (,). Default value: http 2xx _ |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HealthyThresho ld | String | Optional | Released | The threshold used to determine that the backend servers are healthy. This value indicates the number of consecutive successful health checks required before the health status of a backend server can be changed from fail to success. | Valid values: 1 to 10. |
| Timeout | String | Optional | Released | The length of time to wait for the response from a health check. Unit: seconds. | Valid values: 1 to 50. Not ice This parameter is valid only when its value is greater than or equal to that of the Interval parameter. Otherwise, this parameter will be overridden by the Interval value. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| UnhealthyThres hold | String | Optional | Released | The threshold used to determine that the backend servers are unhealthy. This value indicates the number of consecutive failed health checks required before the health status of a backend server can be changed from success to fail. | Valid values: 1 to 10. |
| Port | String | Optional | Released | The port used for health checks. | Valid values: 0 to 65535. |

Persistence syntax

```json
"Persistence": {
  "PersistenceTimeout": Integer,
  "CookieTimeout": Integer,
  "XForwardedFor": String,
  "Cookie": String,
  "StickySession": String,
  "StickySessionType": String
```

Persistence properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| StickySession | String | No | No | Specifies whether to enable session persistence. | Valid values: on off |
| PersistenceTim eout | String | Optional | Released | The maximum duration that the client can be connected to the server. Unit: seconds. | Valid values: 0 to 1000. The default value is 0, which indicates that connection persistence is disabled. Unit: seconds. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| CookieTimeout | String | Optional | Released | The maximum duration the cookie can be retained before it expires. Unit: seconds. | This parameter is required when the StickySession parameter is set to on and the StickySessionTy pe parameter is set to insert. Valid values: 1 to 86400. Unit: seconds. |
| XForwardedFor | String | Yes | Released | Specifies whether to use the X- Forwarded-For header field to obtain the real IP address of the client. | Valid values: on off Default value: on |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Cookie | String | Yes | Released | The cookie configured on the backend server. | The parameter value must be 1 to 200 characters in length and follow the RFC 2965 standard. It can contain only ASCII characters. It cannot contain commas (,), semicolons (;), or spaces, and cannot start with a dollar sign ($). This parameter is required when the StickySession parameter is set to on and the StickySession Type parameter is set to server. |
|   |   |   |   |   | Valid values: insert and server. When this parameter is set to insert, SLB adds a cookie to the first response from the backend server. Then, the next request contains the cookie and the listener distributes the request to the same |

| Parameter | Type | Required | Editable | Description | backend Constraint server. When |
|---|---|---|---|---|---|
| StickySessionTy | String | Yes | Released | The method for processing | this parameter is set to server, SLB overwrites the original |
| pe |   |   |   | cookies. | cookie when a new cookie is set. The next time the client carries the new cookie to access SLB, the listener distributes the request to the previously recorded backend server. This parameter is required when the StickySession parameter is set to on. This parameter is ignored when the StickySession parameter is set to off. |

HttpConfig syntax

```json
"HttpConfig": {
  "ForwardPort": Integer,
  "ListenerForward": String
```

HttpConfig properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ForwardPort | String | Optional | Released | The port used to redirect HTTP requests to HTTPS. | Valid values: 1 to 65535. Default value: 443. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ListenerForward | String | No | No | Specifies whether to enable HTTP- to-HTTPS redirection. | Valid values: on off Default value: off. |

Response parameters Fn::GetAtt LoadBalancerId: the unique ID of the SLB instance. ListenerPortsAndProtocol: an array consisting of the ports and protocols used by the SLB listener. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "LoadBalancer": {
      "Type": "ALIYUN::SLB::LoadBalancer",
        "LoadBalancerName": "createdByHeat",
        "AddressType": "internet",
        "InternetChargeType": "paybybandwidth"
```

`},`

```json
    "CreateListener": {
      "Type": "ALIYUN::SLB::Listener",
        "LoadBalancerId": {"Ref": "LoadBalancer"},
        "ListenerPort": "8094",
        "BackendServerPort": 8080,
        "Bandwidth": 1,
        "Protocol": "http",
        "HealthCheck": {
          "HealthyThreshold": 3,
          "UnhealthyThreshold": 3,
          "Interval": 2,
          "Timeout": 5,
          "HttpCode": "http_2xx,http_3xx,http_4xx,http_5xx"
```

`},`

```json
        "Scheduler": "wrr",
          "Persistence": {
          "PersistenceTimeout": 1,
          "XForwardedFor": "on",
          "StickySession": "on",
          "StickySessionType": "insert",
          "CookieTimeout": 10,
          "Cookie": "1"
```

`},`

```json
  "Outputs": {
  "LoadBalanceDetails": {
     "Value": {"Fn::GetAtt": ["LoadBalancer", "LoadBalancerId"]}
```

#### 5.6.7 ALIYUN::SLB::LoadBalancer

ALIYUN::SLB::LoadBalancer is used to create an SLB instance. Statement

```json
  "Type": "ALIYUN::SLB::LoadBalancer",
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

#### 5.6.8 ALIYUN::SLB::LoadBalancerClone

ALIYUN::SLB::LoadBalancerClone is used to clone an SLB instance. Syntax

```json
  "Type": "ALIYUN::SLB::LoadBalancerClone",
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
| ResourceGroupI d | String | No | No | The ID of the resource group. | None |
| VSwitchId | String | No | No | The ID of the VSwitch. | The VSwitch must exist in the VPC to which the source SLB instance belongs. If the parameter is not specified, the VSwitch to which the source SLB instance belongs is used. |
| SourceLoadBala ncerId | String | Yes | No | The ID of the SLB instance to be cloned. | None |
|   |   |   |   |   | Valid values: clone: The ECS instances listened by the source SLB instance and the ECS instance weights are cloned to the new SLB instance. empty: No ECS instances are attached to the new |

| Property | Type | Required | Editable | Description | SLB instance. Constraint append: The |
|---|---|---|---|---|---|
|   |   |   |   |   | ECS instances |
| BackendServers Policy | String | No | No | The clone policy. The ECS instances listened by the new SLB instance and the weight of each ECS instance are specified in the policy. | listened by the source SLB instance and the ECS instance weights are cloned to the new SLB instance. New ECS instances with specified weights are also attached to the new SLB instance. replace: New ECS instances with specified weights are attached to the new SLB instance. However, the ECS instances listened by the source SLB instance and the ECS instance weights are not cloned to the new SLB instance. Default value: clone. |
| BackendServers | List | No | Yes | The new ECS instances to be listened. | None |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| LoadBalancerNa me | String | No | No | The name of the new SLB instance. | You can set the name to any string. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| Tags | List | No | Yes | The tags of the SLB instance. | Tags must be specified as key-value pairs. A maximum of five tags can be specified. |
| TagsPolicy | String | No | No | The policy of the tags. | Valid values: clone: The tags of the source SLB instance are used. empty: No tags are configured. append: The tags of the source SLB instance are reserved while new tags are added. replace: The tags of the source SLB instance are deleted while new tags are added. Default value: empty. |

BackendServers syntax

```json
"BackendServers": [
    "ServerId": String,
    "Weight": Integer
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the ECS instance. | The ECS instances must be in the running state. |
| Weight | Integer | Yes | Yes | The weight of the ECS instance to be attached to the SLB instance. | Valid values: 0 to 100. Default value: 100. |

Response parameters Fn::GetAtt LoadBalancerId: the ID of the new SLB instance. Examples

```json
  "ROSTemplateFormatVersion" : "2015-09-01",
  "Resources" : {
    "CloneLoadBalance": {
      "Type": "ALIYUN::SLB::LoadBalancerClone",
        "SourceLoadBalancerId": "150ebed5f06-cn-beijing-btc-***",
        "LoadBalancerName": "rosnew",
        "BackendServersPolicy": "replace",
        "BackendServers": [
                "ServerId": "i-25zsk****",
                "Weight": 20
```

`]` `},`

```json
  "Outputs": {
    "LoadBalanceDetails": {
         "Value" : {"Fn::GetAtt": ["CloneLoadBalance", "LoadBalancerId"]}
```

#### 5.6.9 ALIYUN::SLB::MasterSlaveServerGroup

ALIYUN::SLB::MasterSlaveServerGroup is used to create a primary/secondary server group. Not ice A primary/secondary server group contains only two ECS instances: a primary server and a secondary server. Syntax

```json
  "Type": "ALIYUN::SLB::MasterSlaveServerGroup",
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

#### 5.6.10 ALIYUN::SLB::Rule

ALIYUN::SLB::Rule is used to add forwarding rules for a specified HTTP or HTTPS listener. Statement

```json
  "Type": "ALIYUN::SLB::Rule",
    "ListenerPort": Integer,
    "RuleList": List,
    "LoadBalancerId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ListenerPort | Integer | Yes | No | The frontend listener port used by the SLB instance. | Valid values: 1 to 65,535. |
| RuleList | List | Yes | No | The list of forwarding rules to be added. | A maximum of 10 forwarding rules can be added at a time. Each forwarding rule contains the following parameters: RuleName, Domain, Url, and VServerGroupId. You must specify at least one of the following parameters: Domain and URL. The combination of Domain and URL must be unique in a listener. |
| LoadBalancerId | String | No | No | The IDs of SLB instances. | None |

RuleList syntax

```json
"RuleList": [
    "Url": String,
    "Domain": String,
    "VServerGroupId": String,
    "RuleName": String
```

`]` RuleList properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|

| Parameter | Type | Required |   | Editable |   |   | Description |   |   | Constraint |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Url | String | Yes |   | Released |   |   | The request URL. |   |   | The name must be 1 to 80 characters in length and can contain letters, numbers, and special characters. - |   |   |
|   |   |   |   |   |   |   |   |   |   |   | - |   |
|   |   |   |   |   |   |   |   |   |   | /. percent |   |   |
|   |   |   |   |   |   |   |   |   |   | signs (%), |   |   |
|   |   |   |   |   |   |   |   |   |   | question |   |   |
|   |   |   |   |   |   |   |   |   |   | marks (?), #& |   |   |
| Domain | String | Yes |   | Released |   |   | The request domain name associated with the forwarding rule. |   |   | None |   |   |
| VServerGroupId | String | No |   | No |   |   | The ID of the destination VServer group specified in the forwarding rule. |   |   | None |   |   |
| RuleName | String | No |   | No |   |   | The name of the forwarding rule. |   |   | The name must be 1 to 40 characters in length and can contain letters, numbers, and special characters. - /. . _ Forwarding rule names must be unique within each listener. |   |   |

| - |   |
|---|---|

|   | /. _ |
|---|---|

Response parameters Fn::GetAtt Rules: the list of forwarding rules. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Rule": {
      "Type": "ALIYUN::SLB::Rule",
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
      "Description": "The front-end HTTPS listener port of the Server Load Balancer instance. Val
id value:\n1-65535",
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

#### 5.6.11 ALIYUN::SLB::VServerGroup

ALIYUN::SLB::VServerGroup is used to create a VServer group and adds backend servers to the SLB instance. Syntax

```json
    "Type" : "ALIYUN::SLB::VServerGroup",
    "Properties" : {
         "VServerGroupName" : String,
         "BackendServers" : List,
         "LoadBalancerId" : String
```

Properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| VServerGroupN ame | String | Yes | No | The name of the VServer group. | None |
| BackendServers | List | Yes | Yes | The list of ECS instances to be added. | A list can contain up to 20 instances. |
| LoadBalancerId | String | Yes | No | The ID of the SLB instance. | None |

BackendServers syntax

```json
"BackendServers" : [
        "ServerId" : String,
        "Port" : Integer,
        "Weight" : Integer
```

`]` BackendServers properties

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| ServerId | String | Yes | Yes | The ID of the ECS instance. | None |
| Port | Integer | Yes | Yes | The backend port used by the SLB instance. | Valid values: 1 to 65535. |
| Weight | Integer | Yes | Yes | The weight of the ECS instance to be attached to the SLB instance. | Valid values: 0 to 100. |

Response parameters Fn::GetAtt VServerGroupId: the ID of the VServer group. BackendServers: the list of backend servers added to the SLB instance Examples

```json
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
        "CreateVServerGroup": {
            "Type": "ALIYUN::SLB::VServerGroup",
                "LoadBalancerId": "lb-2zenh4ndwrqg14yt0****",
                "VServerGroupName": "VServerGroup-****",
                "BackendServers": [
                        "ServerId": "i-25zsk****",
                        "Weight": 20,
                        "Port": 8080
```

`},`

```json
                        "ServerId": "i-25zsk****",
                        "Weight": 100,
                        "Port": 8081
```

`]` `},`

```json
    "Outputs": {
        "VServerGroupId": {
            "Value" : {"Fn::GetAttr": ["CreateVServerGroup",  "VServerGroupId"]
```

### 5.7 VPC

#### 5.7.1 ALIYUN::VPC::EIP

ALIYUN::VPC::EIP is used to apply for an Elastic IP address. Statement

```json
  "Type": "ALIYUN::VPC::EIP",
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
| PricingCycle | String | Yes | Released | The billing cycle of the subscription. Default value: Month. | Valid values: Month: paid by month. Year Default value: Month. Not e This parameter is required when InstanceChargeType is set to Prepaid. |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Period | Number | Erased | Released | The subscription period. | Valid values: If pay by month is selected, the billing method can be a fee of 1 to 9. If pay-as-you-go is selected, the payment can be in the range of 1 to 3. Default value: 1 Not e This parameter is required when InstanceChargeType is set to Prepaid. |
| AutoPay | Boolean | Erased | Released | Specifies whether to enable automatic payment. | Valid values: false: Automatic payment is disabled. After an order is generated, you must go to the Order Center to make the payment. true: Automatic payment is enabled. Payments are automatically made. Not e This parameter is required when InstanceChargeType is set to Prepaid. |
| Isp | String | Yes | Released | The ISP tag used for Finance Cloud. This parameter takes effect only when your region is set to China (Hangzhou). | This parameter is ignored if you are not a Finance Cloud user. |

Response parameters Fn::GetAtt EipAddress: the allocated Elastic IP address. AllocationId: the ID of the instance that the Elastic IP address is allocated to. OrderId: The order ID that is returned when you set the InstanceChargeType parameter to Prepaid. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Eip": {
      "Type": "ALIYUN::VPC::EIP",
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

#### 5.7.2 ALIYUN::VPC::EIPAssociation

ALIYUN::VPC::EIPAssociation is used to associate an Elastic IP address with a cloud service instance. Statement

```json
  "Type": "ALIYUN::VPC::EIPAssociation",
    "AllocationId": String,
    "InstanceId": String,
    "PrivateIpAddress": String,
    "Mode": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AllocationId | String | No | Yes | The ID of the Elastic IP address. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceId | String | No | Yes | The ID of the cloud service instance. | The following instance types are supported: VPC- connected ECS instances VPC- connected SLB instances NAT gateways HAVIP Elastic network interfaces |
| PrivateIpAddres s | String | Yes | True | The private IP address in the CIDR block of the VSwitch. | None |
| Mode | String | Yes | True | The association mode. | Valid values: NAT MULTI BINDE _ D |

Response parameters Fn::GetAtt EipAddress: The allocated Elastic IP address. AllocationId: The ID of the instance to which the Elastic IP address is allocated. Examples `JSON` format

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "Eip": {
      "Type": "ALIYUN::VPC::EIP",
        "InternetChargeType": "PayByTraffic",
          "Bandwidth": 200
```

`},`

```json
    "EipAssociation": {
      "Type": "ALIYUN::VPC::EIPAssociation",
        "InstanceId": "<LoadBalancerId>",
        "InstanceType": "EcsInstance",
        "AllocationId": {
          "Fn::GetAtt": ["Eip", "AllocationId"]
```

`},`

```json
  "Outputs": {
    "EipAddress": {
      "Value" : {"Fn::GetAtt": ["EipAssociation", "EipAddress"]}
```

`},`

```json
    "AllocationId": {
      "Value" : {"Fn::GetAtt": ["EipAssociation", "AllocationId"]}
```

`YAML` format

```
ROSTemplateFormatVersion: '2015-09-01' Resources:
  Eip:
    Type: ALIYUN::VPC::EIP
    Properties:
      InternetChargeType: PayByTraffic
      Bandwidth: 200
  EipAssociation:
    Type: ALIYUN::VPC::EIPAssociation
    Properties:
      InstanceId: "<LoadBalancerId>"
      InstanceType: EcsInstance
      AllocationId:
        Fn::GetAtt:
        - Eip
        - AllocationId
Outputs:
  EipAddress:
    Value:
      Fn::GetAtt:
      - EipAssociation
      - EipAddress
  AllocationId:
    Value:
      Fn::GetAtt:
      - EipAssociation
      - AllocationId
```

#### 5.7.3 ALIYUN::VPC::PeeringRouterInterfaceBinding

ALIYUN::VPC::PeeringRouterInterfaceBinding is used to associate two router interfaces to be interconnected. Statement

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
    "OppositeRouterId": String,
    "OppositeInterfaceId": String,
    "OppositeInterfaceOwnerId": String,
    "RouterInterfaceId": String
```

Properties

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| RouterInterfaceI d | String | No | No | The ID of the router interface. | None |

| Parameter | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| OppositeInterfa ceId | String | No | No | The ID of the peer router interface. | None |
| OppositeRouter Id | String | Yes | Released | The ID of the router to which the peer router interface belongs. | None |
| OppositeInterfa ceOwnerId | String | Yes | Released | The ID of the owner of the peer router interface. | None |

Response parameters Fn::GetAtt RouterInterfaceId: the ID of the vRouter. Sample request

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "InitiatorRouterInterfaceBinding": {
      "Type": "ALIYUN::VPC::PeeringRouterInterfaceBinding",
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2zex1tkyym98pjaor****",
        "OppositeRouterId": "vrt-2zexb35tzoriu0286****"
```

#### 5.7.4 ALIYUN::VPC::PeeringRouterInterfaceConnection

ALIYUN::VPC::PeeringRouterInterfaceConnection is used to initiate a router interface connection. Statement

```json
  "Type": "ALIYUN::VPC::PeeringRouterInterfaceConnection",
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
        "RouterInterfaceId": "ri-2zedgo0ih64g1me29****",
        "OppositeInterfaceId": "ri-2ze4k5n2aeardu8cy****"
```

#### 5.7.5 ALIYUN::VPC::RouterInterface

ALIYUN::VPC::RouterInterface is used to create a router interface. Syntax

```json
  "Type": "ALIYUN::VPC::RouterInterface",
    "OppositeRegionId": String,
    "Description": String,
    "HealthCheckSourceIp": String,
    "RouterType": String,
    "AccessPointId": String,
    "RouterId": String,
    "Role": String,
    "OppositeInterfaceOwnerId": String,
    "OppositeAccessPointId": String,
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
| RouterId | String | Yes | No | The ID of the router | None |
| Role | String | Yes | No | The role of the router interface. | When RouterType is set to VBR, set the value to InitiatingSide. When OppositeRouterTy pe is set to VBR, set the value to AcceptingSide. |
| RouterType | String | No | No | The type of the router to which the router interface belongs. | Valid values: VRouter VBR |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| AccessPointI d | String | No | No | The ID of the access point of the router interface. | This parameter is required when RouterType is set to VBR. The access point ID cannot be modified after the router interface is created. This parameter is not required when RouterType is set to VRouter. |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| Spec | String | No | No | The specifications of the router interface. | The following list includes available specifications and the corresponding bandwidth values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s Not e This paramet er is required when Role is set to Initiating Side. The value Negative is used by default when Role is set to Acceptin gSide. |
| OppositeReg ionId | String | No | No | The region ID of the peer router interface. | None |

|   | User Guide·Reso | urce types |   |   | Resourc | e Orchestration Servic | e |
|---|---|---|---|---|---|---|---|

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| OppositeInte rfaceOwnerI d | String | No | No | The ID of the owner of the peer router interface. | The default value is the ID of the current user. |
| OppositeRou terId | String | No | No | The ID of the router to which the peer router interface belongs. | None |
| OppositeRou terType | String | No | No | The type of the router to which the peer router interface belongs. | Valid values: When RouterType is set to VBR, set the value to VRouter. VBR |
| OppositeAcc essPointId | String | No | No | The ID of the access point of the peer router interface. | When OppositeRouterTy pe is set to VBR, this parameter is required . The access point ID cannot be modified after the router interface is created. When OppositeRouterTy pe is set to VRouter, this parameter is not required. When OppositeRouterTy pe is set to VBR, the VBR specified by the OppositeRouterId parameter must be in the access point specified by the OppositeAccessPoi ntId parameter. |
| Description | String | No | No | The description of the router interface. | The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . The parameter is empty by default. |

| Property | Type | Required | Editable | Description | Constraint |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Name | String | No | No | The display name of the router interface. | The name must be 2 to 128 characters in length and can contain letters, digits, periods(.), underscores ( ), _ and hyphens (-). It must start with a letter but cannot start with http: // or https:/ / . |   |   |   |
|   |   |   |   |   |   |   | http: |   |
|   |   |   |   |   |   | https:/ |   |   |
| HealthCheck SourceIp | String | No | No | The source IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces with a peer router interface on a VBR. It must be an unused IP address in the VPC where the local VRouter is located. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both left unspecified. |   |   |   |

|   |   | // |
|---|---|---|
|   |   | / |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| HealthCheck TargetIp | String | No | No | The destination IP address of health check packets used in leased line disaster recovery and ECMP scenarios. | This parameter is valid only for VRouter interfaces with a peer router interface on a VBR. Typically, you can use the IP address of a customer premises equipment (CPE) on the user side of the leased line, which is the IP address of the peer gateway on the VBR where the peer router interface is located. You can also specify another IP address on the user side of the leased line as the destination IP address. The HealthCheckSourceIp and HealthCheckTargetIp parameters must either both be specified or both left unspecified. |
| PricingCycle | String | No | No | The billing cycle of the subscription. | Valid values: Month Year |
| Period | Number | No | No | The subscription duration. | Valid values when the PricingCycle parameter is set to Month: 1 to 9. Valid values when the PricingCycle parameter is set to Year: 1 to 3. |
| AutoPay | Boolean | No | No | Specifies whether to enable automatic payment. | Default value: false. Valid values: true false |

| Property | Type | Required | Editable | Description | Constraint |
|---|---|---|---|---|---|
| InstanceChar geType | String | No | No | The billing method of the instance. | Valid values: Postpaid: pay-as- you-go Prepaid: subscription |

Response parameters Fn::GetAtt RouterInterfaceId: the ID of the router interface. Examples

```json
  "ROSTemplateFormatVersion": "2015-09-01",
  "Resources": {
    "RouterInterface": {
      "Type": "ALIYUN::VPC::RouterInterface",
        "Name": "RouterInterface_1",
        "Description": "VPC initiator RouterInterface",
        "RouterId": "vrt-2ze2i147e5n0bicoe****",
        "Role": "AcceptingSide",
        "OppositeRegionId": "cn-beijing",
        "HealthCheckSourceIp": "10.0.XX.XX",
        "HealthCheckTargetIp": "192.168.XX.XX"
```

`},`

```json
  "Outputs": {
    "RouterInterfaceId": {
      "Value": {"Fn::GetAtt": ["RouterInterface", "RouterInterfaceId"]}
```
