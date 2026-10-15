---
title: "Operation Orchestration Service Developer Guide 20250925"
product_version: "V3.18.6"
pdf_pages: 64
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Operation Orchestration Service Developer Guide 20250925.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%BF%90%E7%BB%B4%E7%BC%96%E6%8E%92%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Operation%20Orchestration%20Service%20Developer%20Guide%2020250925.pdf"
converter: line-classifier (PyMuPDF)
---

# Operation Orchestration Service Developer Guide 20250925

Operation Orchestration Service

## Common action attributes

An action is the minimum O&M unit that defines a specific operation.

**Action types**

Actions can be divided into the following types: ApsaraDB RDS actions

**Name format**

The name of an action is in the following format: `ACS::<name>` .

**Common attributes**

Unless otherwise specified, each action has the following attributes:

```
--- Tasks:
  - Name: task_name_1
    Action: 'Action'
    Description: describe the purpose of the task
    OnError: 'ACS::END/<other-task-name>' # The process to be executed if an error occu
rs when the task is being executed. Default value: ACS::END, which specifies that the e xecution ends when an error occurs.
    OnSuccess: 'ACS::NEXT/<other-task-name>/ACS::END' # The process to be executed when
the task is successfully executed. Default value: ACS::NEXT, which specifies that the n ext task is executed after the current task is successfully executed.
    Properties:
      Service: ECS/RDS/RAM
      API: DeleteInstance/CreateDBInstance/CreateRamRole
      Parameters:
        InstanceId: "i-XXX"
    Outputs:
      Output_parameter_name_1:
        Type: String/List
        ValueSelector": ".Key1"
```

**Basic attributes**

Name: the name of the task. The name can contain letters, digits, underscores (_), and hyphens (-). It can be up to 200 characters in length, and cannot contain colons (:). Action: the action of the task. The value must be an atom action or a cloud product action. The action name must start with `ACS::` . Operation Orchestration Service Description: the purpose of the task. Properties: the properties of the task. For more information, see ACS::ExecuteAPI

**Process control attributes**

`OnError: ACS::END` : The task ends if an error occurs. This is the default value. `OnSuccess: ACS::NEXT` : The next task is executed after the current task is successfully executed. This is the default value. `OnError: <task_name>` : The specified task is executed if an error occurs when the current task is being executed. `OnSuccess: <task_name>` : The specified task is executed after the current task is successfully executed.

**Examples**

The following template is used to create a Cloud Assistant command that is run on an ECS instance. YAML format

```
FormatVersion: OOS-2019-06-01 Description: Creates a cloud assistant command and triggers it on one ECS instance. Parameters:
  regionId:
    Description: The ID of region.
    Type: String
    Default: '{{ ACS::RegionId }}'
  commandContent:
    Description: The content of command.
    Type: String
  instanceId:
    Description: The ID of ECS instance that will invoke command.
    Type: String
    MinLength: 1
    MaxLength: 30
  commandType:
    Description: The type of command.
    Type: String
    AllowedValues:
    - RunBatScript
    - RunPowerShellScript
    - RunShellScript
  workingDir:
    Description: The directory where the created command runs on the ECS instances.
    Type: String
    Default: ""
  timeout:
    Description: The value of the invocation timeout period of a command on ECS instanc
es.
    Type: Number
    Default: 600
Tasks:
- Name: runCommand
  Description: Executes a cloud assistant command.
  Properties:
```

Operation Orchestration Service

```
    Service: ECS
    API: RunCommand
    Parameters:
      RegionId: '{{ regionId }}'
      CommandContent: '{{ commandContent }}'
      InstanceIds:
        - '{{instanceId}}'
      Name: '{{ ACS::ExecutionId }}'
      Type: '{{ commandType }}'
      WorkingDir: '{{ workingDir }}'
      Timeout: '{{ timeout }}'
  Outputs:
    invokeId:
      Type: String
      ValueSelector: InvokeId
- Name: untilInvocationReady
  Description: Waits for the command to be completed.
  OnError: ACS::END
  Retries: 20
  Properties:
    Service: ECS
    API: DescribeInvocations
    Parameters:
      RegionId: '{{ regionId }}'
      InvokeId: '{{ runCommand.invokeId }}'
    DesiredValues:
    - Finished
    StopRetryValues:
    - Failed
    PropertySelector: Invocations.Invocation[].InvokeStatus
- Name: describeInvocationResults
  Description: Views the command output of a cloud assistant command in the specified E
```

`CS`

```
    instance.
  Properties:
    Service: ECS
    API: DescribeInvocationResults
    Parameters:
      RegionId: '{{ regionId }}'
      InvokeId: '{{ runCommand.invokeId }}'
  Outputs:
    invocationResult:
      Type: String
      ValueSelector: 'Invocation.InvocationResults.InvocationResult[].Output'
- Name: checkInvocationResult
  Description: Check the command exitcode of a cloud assistant command.
  OnError: 'ACS::END'
  Properties:
    Service: ECS
    API: DescribeInvocationResults
    Parameters:
```

Operation Orchestration Service

```
      RegionId: '{{ regionId }}'
      InvokeId: '{{ runCommand.InvokeId }}'
    PropertySelector: 'Invocation.InvocationResults.InvocationResult[].ExitCode'
    DesiredValues:
      - 0
Outputs:
  invocationOutput:
    Type: String
    Value:
      'Fn::Base64Decode': '{{ describeInvocationResults.invocationResult }}'
```

JSON format

```json
{
  "FormatVersion": "OOS-2019-06-01",
  "Description": "Creates a cloud assistant command and triggers it on one ECS instance
.",
  "Parameters": {
    "regionId": {
      "Description": "The ID of region.",
      "Type": "String",
      "Default": "{{ ACS::RegionId }}"
    },
    "commandContent": {
      "Description": "The content of command.",
      "Type": "String"
    },
    "instanceId": {
      "Description": "The ID of ECS instance that will invoke command.",
      "Type": "String",
      "MinLength": 1,
      "MaxLength": 30
    },
    "commandType": {
      "Description": "The type of command.",
      "Type": "String",
      "AllowedValues": [
        "RunBatScript",
        "RunPowerShellScript",
        "RunShellScript"
```

]

```json
    },
    "workingDir": {
      "Description": "The directory where the created command runs on the ECS
instances.",
      "Type": "String",
      "Default": ""
    },
    "timeout": {
      "Description": "The value of the invocation timeout period of a command on ECS in
stances.",
      "Type": "Number",
      "Default": 600
    }
```

Operation Orchestration Service

```json
  },
  "Tasks": [
    {
      "Name": "runCommand",
      "Action": "ACS::ExecuteAPI",
      "Description": "Executes a cloud assistant command.",
      "Properties": {
        "Service": "ECS",
        "API": "RunCommand",
        "Parameters": {
          "RegionId": "{{ regionId }}",
          "CommandContent": "{{ commandContent }}",
          "InstanceIds": [
            "{{instanceId}}"
```

`],`

```json
          "Name": "{{ ACS::ExecutionId }}",
          "Type": "{{ commandType }}",
          "WorkingDir": "{{ workingDir }}",
          "Timeout": "{{ timeout }}"
        }
      },
      "Outputs": {
        "invokeId": {
          "Type": "String",
          "ValueSelector": "InvokeId"
        }
      }
    },
    {
      "Name": "untilInvocationReady",
      "Action": "ACS::WaitFor",
      "Description": "Waits for the command to be completed.",
      "OnError": "ACS::END",
      "Retries": 20,
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInvocations",
        "Parameters": {
          "RegionId": "{{ regionId }}",
          "InvokeId": "{{ runCommand.invokeId }}"
        },
        "DesiredValues": [
          "Finished"
```

`],`

```json
        "StopRetryValues": [
          "Failed"
```

`],`

```json
        "PropertySelector": "Invocations.Invocation[].InvokeStatus"
      }
    },
    {
      "Name": "describeInvocationResults",
      "Action": "ACS::ExecuteAPI",
      "Description": "Views the command output of a cloud assistant command in the spec
```

Operation Orchestration Service

```json
ified ECS instance.",
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInvocationResults",
        "Parameters": {
          "RegionId": "{{ regionId }}",
          "InvokeId": "{{ runCommand.invokeId }}"
        }
      },
      "Outputs": {
        "invocationResult": {
          "Type": "String",
          "ValueSelector": "Invocation.InvocationResults.InvocationResult[].Output"
        }
      }
    },
    {
      "Name": "checkInvocationResult",
      "Action": "ACS::CheckFor",
      "Description": "Check the command exitcode of a cloud assistant command.",
      "OnError": "ACS::END",
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInvocationResults",
        "Parameters": {
          "RegionId": "{{ regionId }}",
          "InvokeId": "{{ runCommand.InvokeId }}"
        },
        "PropertySelector": "Invocation.InvocationResults.InvocationResult[].ExitCode",
        "DesiredValues": [
```

]

```
      }
    }
```

`],`

```json
  "Outputs": {
    "invocationOutput": {
      "Type": "String",
      "Value": {
        "Fn::Base64Decode": "{{ describeInvocationResults.invocationResult }}"
      }
    }
  }
}
```

**Task output attributes**

Task output attributes include Type and ValueSelector. If you want to declare multiple output items, separate them with commas (,). For more information, see the syntax in the following example.

**Examples**

The following template is used to query all ECS instances in the specified state. YAML format Operation Orchestration Service

```
FormatVersion: OOS-2019-06-01 Description: Views the ECS instances by specifying instance status. Parameters:
  regionId:
    Description: The ID of region.
    Type: String
    Default: '{{ ACS::RegionId }}'
  status:
    Description: The ECS instances status for query instances.
    Type: String
Tasks:
- Name: describeInstances
  Description: Views the ECS instances by specifying instance status.
  Properties:
    Service: ECS
    API: DescribeInstances
    Parameters:
      RegionId: '{{ regionId }}'
      Status: '{{ status }}'
  Outputs:
    instanceIds:
      Type: List
      ValueSelector: Instances.Instance[].InstanceId
Outputs:
  instanceIds:
    Type: List
    Value: '{{ describeInstances.instanceIds }}'
```

JSON format

```json
{ "FormatVersion": "OOS-2019-06-01", "Description": "Views the ECS instances by speci fying instance status.", "Parameters": { "regionId": { "Description": "The ID of region.", "Type": "String", "Default": "{{ ACS::RegionId }}" }, "stat us": { "Description": "The ECS instances status for query instances.", "Type": "String" } }, "Tasks": [ { "Name": "describeInstances", "Actio n": "ACS::ExecuteAPI", "Description": "Views the ECS instances by specifying insta nce status.", "Properties": { "Service": "ECS", "API": "DescribeInstances", "Parameters": { "RegionId": "{{ regionId }}", "Status": "{{ status }}" } }, "Outputs": { "instanceIds": { "Type": "List", "ValueSelector": "Instances.Instance[].InstanceId" } } } ], "Outputs": { "instanceIds": { "Type": "List", "Value": "{{ desc ribeInstances.instanceIds }}" } }}
```

**Output item name**

Required. The unique identifier of the output item in the template, such as InstanceIds in the example.

**Type**

Required. The type of the output item, such as `String` or `List` .

**ValueSelector**

Operation Orchestration Service Required. The value of the output item returned after the template is executed. You can specify the value of the ValueSelector attribute in the template by using a jQuery selector, such as .Instances or .Instances.Instance[].Status. Operation Orchestration Service

## Atom actions

### API actions

#### ACS::ExecuteAPI

**Description**

The ACS::ExecuteAPI action can be used to call an API operation of a cloud service such as Elastic Compute Service (ECS). If the API operation is called asynchronously, you can use the ACS: WaitFor action to wait for the specified instance to enter the expected state. For more information, see ACS::WaitFor.

**Syntax**

**RPC API operations**

**Note**: In the Properties parameter of the Tasks parameter, the API parameter specifies the
API operation to be called, so you do not need to specify it again in the Parameters parameter. YAML format

```
Tasks:
  - Name: executeAPITaskExample
    Properties:
      Service: ECS # Required. The Alibaba Cloud Resource Name (ARN) of the cloud servi
ce in Resource Access Management (RAM). The name is case insensitive, such as ECS, RDS, and FC.
      API: DescribeInstances # Required. The name of an API operation of the cloud serv
ice. The name is case insensitive, such as DescribeInstances.
      AutoPaging: false # Optional. Specifies whether to automatically go through pages
to obtain all results for API operations that return results on different pages. Defaul t value: true.
      Parameters: # The parameters required for calling an API operation. For more info
rmation, see the relevant documentation.
        Parameter1: Value1
        Parameter2: Value2
    Outputs:
      OutputParameter1:
        ValueSelector: 'jq selector' # The jQuery selector for selecting the required J
SON data. For example, when you call an API operation for a task, the jQuery selector e xtracts the required information from the returned JSON data. For more information, see https://stedolan.github.io/jq/.
        Type: String/Boolean/List(Array)/Number/Object
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
  "Tasks": [
    {
      "Name": "executeAPITaskExample",
      "Action": "ACS::ExecuteAPI",
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInstances",
        "AutoPaging": false,
        "Parameters": {
          "Parameter1": "Value1",
          "Parameter2": "Value2"
        }
      },
      "Outputs": {
        "OutputParameter1": {
          "ValueSelector": "jq selector",
          "Type": "String/Boolean/List(Array)/Number/Object"
        }
      }
    }
```

]

```
}
```

**ROA API operations**

YAML format

```xml
Tasks:
  - Name: executeAPITaskExample2
    Properties:
      Service: OOS # Required. The ARN of the cloud service in RAM. The name is case in
sensitive, such as OOS, ECS, RDS, and FC.
      API: PutBucket # Required. The name of an API operation of the cloud service. The
name is case insensitive, such as PutBucket.
      Method: PUT  # Required. The HTTP request method of the API operation.
      URI: ''  # The URI used by the API operation.
      Headers: # Optional. The request header of the API operation. Set this parameter
as follows:
        requestHeader1: 'requestHeader1Value'
      Parameters: # Optional. The common parameters of the API operation.
        commonParameter1: 'commonParameter1Value'
        commonParameter2: 'commonParameter2Value'
    # Optional. The request elements of the API operation. Set this parameter in the XM
L format.
      Body: |
        <?xml version="1.0" encoding="UTF-8"?> <supKey1> <parameter1> Value1
        </parameter1> <parameter2> Value2 </parameter2> </supKey1>
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
  "Tasks": [
    {
      "Name": "executeAPITaskExample2",
      "Action": "ACS::ExecuteAPI",
      "Properties": {
        "Service": "OOS",
        "API": "PutBucket",
        "Method": "PUT",
        "URI": "",
        "Headers": {
          "requestHeader1": "requestHeader1Value"
        },
        "Parameters": {
          "commonParameter1": "commonParameter1Value",
          "commonParameter2": "commonParameter2Value"
        },
        "Body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?> <supKey1> <parameter1>
Value1\n</parameter1> <parameter2> Value2 </parameter2> </supKey1>\n"
      }
    }
```

]

```
}
```

**Sample code**

**Sample code for calling RPC API operations**

The following is the sample code for calling the ECS API operation DescribeInstances: YAML format Operation Orchestration Service

```
FormatVersion: OOS-2019-06-01 Description: Views the ECS instances by specifying instance status. Parameters:
  status:
    Description: The ECS instances status for query instances.
    Type: String
Tasks:
- Name: describeInstances
  Description: Views the ECS instances by specifying instance status.
  Properties:
    Service: ECS
    API: DescribeInstances
    Parameters:
      Status: '{{ status }}'
  Outputs:
    instanceIds:
      Type: List
      ValueSelector: Instances.Instance[].InstanceId
Outputs:
  instanceIds:
    Type: List
    Value: '{{ describeInstances.instanceIds }}'
```

JSON format Operation Orchestration Service

```json
{
  "FormatVersion": "OOS-2019-06-01",
  "Description": "Views the ECS instances by specifying instance status.",
  "Parameters": {
    "status": {
      "Description": "The ECS instances status for query instances.",
      "Type": "String"
    }
  },
  "Tasks": [
    {
      "Name": "describeInstances",
      "Action": "ACS::ExecuteAPI",
      "Description": "Views the ECS instances by specifying instance status.",
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInstances",
        "Parameters": {
          "Status": "{{ status }}"
        }
      },
      "Outputs": {
        "instanceIds": {
          "Type": "List",
          "ValueSelector": "Instances.Instance[].InstanceId"
        }
      }
    }
```

`],`

```json
  "Outputs": {
    "instanceIds": {
      "Type": "List",
      "Value": "{{ describeInstances.instanceIds }}"
    }
  }
}
```

**Sample code for calling ROA API operations**

The following is the sample code for calling the OSS API operation PutBucket. YAML format

```
FormatVersion: OOS-2019-06-01 Description:
  en: Create multiple buckets in different region at the same time.
Parameters:
  Regions:
    Description:
      en: The region id..
    Type: List
  BucketName:
    Description:
      en: The bucket name.
Type:String
```

Operation Orchestration Service

```xml
    Type: String
  DataRedundancyType:
    Description:
      en: Specifies the data disaster tolerance type of the bucket.
    Type: String
    AllowedValues:
      - LRS
      - ZRS
  StorageClass:
    Description:
      en: Specify the bucket storage type.
    Type: String
    AllowedValues:
      - Standard
      - IA
      - Archive
  XOssAcl:
    Description:
      en: Specify bucket access rights.
    Type: String
    AllowedValues:
      - public-read-write
      - public-read
      - private
  RateControl:
    Description:
      en: Concurrency ratio of task execution.
    Type: Json
    AssociationProperty: RateControl
  OOSAssumeRole:
    Description: The RAM role to be assumed by OOS.
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: PutBucket
    Description:
      en: Create buckets in different regions.
    Properties:
      Service: OSS
      API: PutBucket
      Method: PUT
      URI: ''
      Headers:
        x-oss-acl: '{{ XOssAcl }}'
      Parameters:
        BucketName: '{{ BucketName }}-{{ACS::TaskLoopItem}}'
        RegionId: '{{ACS::TaskLoopItem}}'
      Body: |
        <?xml version="1.0" encoding="UTF-8"?>
        <CreateBucketConfiguration>
          <StorageClass>{{ StorageClass }}</StorageClass>
          <DataRedundancyType>{{ DataRedundancyType }}</DataRedundancyType>
</CreateBucketConfiguration>
```

Operation Orchestration Service

```
        </CreateBucketConfiguration>
    Loop:
      Items: '{{ Regions }}'
      RateControl: '{{ RateControl }}'
      Outputs:
        imageIds:
          AggregateType: 'Fn::ListJoin'
          AggregateField: imageIds
    Outputs:
      imageIds:
        Type: String
        ValueSelector: .
```

JSON format

```json
{
  "FormatVersion": "OOS-2019-06-01",
  "Description": {
    "en": "Create multiple buckets in different region at the same time."
  },
  "Parameters": {
    "Regions": {
      "Description": {
        "en": "The region id.."
      },
      "Type": "List"
    },
    "BucketName": {
      "Description": {
        "en": "The bucket name."
      },
      "Type": "String"
    },
    "DataRedundancyType": {
      "Description": {
        "en": "Specifies the data disaster tolerance type of the bucket."
      },
      "Type": "String",
      "AllowedValues": [
        "LRS",
        "ZRS"
```

]

```json
    },
    "StorageClass": {
      "Description": {
        "en": "Specify the bucket storage type."
      },
      "Type": "String",
      "AllowedValues": [
        "Standard",
        "IA",
        "Archive"
```

]

```json
    },
"XOssAcl":{
```

Operation Orchestration Service

```json
    XOssAcl: {
      "Description": {
        "en": "Specify bucket access rights."
      },
      "Type": "String",
      "AllowedValues": [
        "public-read-write",
        "public-read",
        "private"
```

]

```json
    },
    "RateControl": {
      "Description": {
        "en": "Concurrency ratio of task execution."
      },
      "Type": "Json",
      "AssociationProperty": "RateControl"
    },
    "OOSAssumeRole": {
      "Description": "The RAM role to be assumed by OOS.",
      "Type": "String",
      "Default": "OOSServiceRole"
    }
  },
  "RamRole": "{{ OOSAssumeRole }}",
  "Tasks": [
    {
      "Name": "PutBucket",
      "Action": "ACS::ExecuteAPI",
      "Description": {
        "en": "Create buckets in different regions."
      },
      "Properties": {
        "Service": "OSS",
        "API": "PutBucket",
        "Method": "PUT",
        "URI": "",
        "Headers": {
          "x-oss-acl": "{{ XOssAcl }}"
        },
        "Parameters": {
          "BucketName": "{{ BucketName }}-{{ACS::TaskLoopItem}}",
          "RegionId": "{{ACS::TaskLoopItem}}"
        },
        "Body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?
>\n<CreateBucketConfiguration>\n <StorageClass>{{ StorageClass }}</StorageClass>\n <D ataRedundancyType>{{ DataRedundancyType }} </DataRedundancyType>\n</CreateBucketConfiguration>\n"
      },
      "Loop": {
        "Items": "{{ Regions }}",
        "RateControl": "{{ RateControl }}",
        "Outputs": {
          "imageIds": {
"AggregateType":"Fn::ListJoin",
```

Operation Orchestration Service

```
ggegateype:
```

`::`

```
stJo
```

,

```json
            "AggregateField": "imageIds"
          }
        }
      },
      "Outputs": {
        "imageIds": {
          "Type": "String",
          "ValueSelector": "."
        }
      }
    }
```

]

```
}
```

#### ACS::WaitFor

**Description**

The ACS::WaitFor action is used to wait for the specified resource to enter the expected state after an API operation is called. You can call the API operations of cloud services to query the statuses of specified resources until the resources enter the expected state. For example, after you call the `RunInstances` operation of Elastic Compute Service (ECS) to create an ECS instance, you can call the `ACS::WaitFor` action to wait for the ECS instance to enter the Running state, indicating that the ECS instance is created.

**Syntax**

Operation Orchestration Service

```bash
Tasks:
  - Name: waitForTaskExample
    Properties:
      # The following attributes are the same as those of the ACS::ExecuteAPI action. F
or more information, see the syntax description for the ACS::ExecuteAPI action.
      Service: ECS
      API: DescribeInstances
      Parameters:
        InstanceId: i-12345678abcedfg
      # The following attributes are unique attributes of the ACS::WaitFor action.
      PropertySelector: "jq selector" # Required. The jQuery selector for selecting the
JSON data to wait for. For more information, see the description of ValueSelector in AC S::ExecuteAPI.
      StopRetryValues: # Optional. A task terminates the Waiting state and the API acti
on retries when a specified state is returned. For example, the task stops if the Stopp ed state is returned.
        - status1
      DesiredValues: # The expected values. If the value selected by PropertySelector m
atches one of the expected values, the operation is successful. If the value selected b y PropertySelector does not match any of the expected values, the operation times out a nd fails. This parameter is required if you do not specify the NotDesiredValues paramet er.
        - value1
        - value2
      NotDesiredValues: # The values that are not expected. If the value selected by Pr
opertySelector does not match any of the expected values, the operation is successful. If the value selected by PropertySelector matches one of the expected values, the opera tion times out and fails. This parameter is required if you do not specify the DesiredV alues parameter.
        - value3
        - value4
    Retries: times # Optional. The maximum number of retries. The value must be a posit
ive integer, such as 5. The retry interval grows in an exponential manner. The interval is 1 second after the first retry, 2 seconds after the second retry, 4 seconds after th e third retry, 8 seconds after the forth retry, and so on.
    Outputs:  # The output parameters of the task where the ACS::WaitFor action resides
. When the task is successfully executed, the output parameter values that meet the Not DesiredValues or DesiredValues condition are returned.
      OutputParameter1:
        ValueSelector: 'jq selector' # The jQuery selector for selecting the required J
SON data. For example, when you call an API operation for a task, the jQuery selector e xtracts the required information from the returned JSON data. For more information, see https://stedolan.github.io/jq/.
        Type: String/Boolean/List(Array)/Number/Object
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
  "Tasks": [
    {
      "Name": "waitForTaskExample",
      "Action": "ACS::WaitFor",
      "Properties": {
        "Service": "ECS",
        "API": "DescribeInstances",
        "Parameters": {
          "InstanceId": "i-12345678abcedfg"
        },
        "PropertySelector": "jq selector",
        "StopRetryValues":["status1"],
        "DesiredValues": [
          "value1",
          "value2"
```

`],`

```json
        "NotDesiredValues": [
          "value3",
          "value4"
```

]

```json
      },
    "Outputs": {
        "OutputParameter1": {
          "ValueSelector": "jq selector",
          "Type": "String/Boolean/List(Array)/Number/Object"
        }
      }
    }
```

]

```
}
```

**Sample code**

The following sample code is used to start an instance and call the ACS::WaitFor action to wait for the instance to enter the Running state: YAML format Operation Orchestration Service

```
--- FormatVersion: OOS-2019-06-01 Parameters:
  InstanceId:
    Description: the instance id that you will start.
    Type: String
Tasks:
- Name: startInstance
  Description: start instance with specified parameters
  Properties:
    Service: ECS
    API: StartInstance
    Parameters:
      InstanceId: '{{ InstanceId }}'
- Name: untilInstanceReady
  Description: describe instances with specified parameters
  Properties:
    Service: ECS
    API: DescribeInstances
    Parameters:
      InstanceIds:
      - '{{ InstanceId }}'
    PropertySelector: Instances.Instance[].Status
    DesiredValues:
    - Running
```

JSON format Operation Orchestration Service

```json
{
    "FormatVersion": "OOS-2019-06-01",
    "Parameters": {
        "InstanceId": {
            "Description": "the instance id that you will start.",
            "Type": "String"
        }
    },
    "Tasks": [
        {
            "Name": "startInstance",
            "Action": "ACS::ExecuteAPI",
            "Description": "start instance with specified parameters",
            "Properties": {
                "Service": "ECS",
                "API": "StartInstance",
                "Parameters": {
                    "InstanceId": "{{ InstanceId }}"
                }
            }
        },
        {
            "Name": "untilInstanceReady",
            "Action": "ACS::WaitFor",
            "Description": "describe instances with specified parameters",
            "Properties": {
                "Service": "ECS",
                "API": "DescribeInstances",
                "Parameters": {
                    "InstanceIds": [ "{{ InstanceId }}"]
                },
                "PropertySelector": "Instances.Instance[].Status",
                "DesiredValues": [ "Running" ],
            }
        }
```

]

```
}
```

#### ACS::CheckFor

**Features**

The ACS::CheckFor action is used to check whether the cloud product instances are in the expected status. If the instances are in the specified status, the task is successful. If the instances are not in the specified status, the task fails. This action is usually used to perform pre-checks. For example, if you want to stop an ECS instance, you can check whether the instance is in the Running status first. If it is not in the Running status, you cannot perform the operation.

**Syntax**

Except that the `Type` attribute is set to `ACS::CheckFor` , all other attributes of the ACS::CheckFor action are the same as those of the `ACS::WaitFor` action. For more information, see the syntax description for the ACS::WaitFor action. Operation Orchestration Service YAML format

```bash
Tasks:
  - Name: checkForTaskExample
    Properties:
      # The following attributes are the same as those of the ACS::ExecuteAPI action. F
or more information, see the syntax description for the ACS::ExecuteAPI action.
      Service: ECS
      API: DescribeInstances
      Parameters:
        InstanceId: i-12345678abcedfg
      # The following attributes are unique attributes of the ACS::CheckFor action.
      PropertySelector: "jq selector" # Required. The jQuery selector for selecting the
JSON data to wait for. For more information, see the description of ValueSelector in AC S::ExecuteAPI.
      DesiredValues: # Either DesiredValues or NotDesiredValues is required. This attri
bute specifies the expected values. If the value selected by PropertySelector matches o ne of the following values, the operation is successful. If the value selected by Prope rtySelector does not match any of the following values, the operation times out and fai ls.
        - value1
        - value2
      NotDesiredValues: # Either DesiredValues or NotDesiredValues is required. This at
tribute specifies the values that are not expected. If the value selected by PropertySe lector does not match any of the following values, the operation is successful. If the value selected by PropertySelector matches one of the following values, the operation t imes out and fails.
        - value3
        - value4
    Outputs: # The output parameters of the task where the ACS::CheckFor action resides
. When the task is successfully executed, the output parameter values that meet the Not DesiredValues or DesiredValues condition are returned.
      OutputParameter1:
        ValueSelector: 'jq selector' # The jQuery selector for selecting the required J
SON data. For example, when you call an API operation for a task, the jQuery selector e xtracts the required information from the returned JSON data. For more information, see https://stedolan.github.io/jq/.
        Type: String/Boolean/List(Array)/Number/Object
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
    "Tasks": [
        {
            "Name": "checkForTaskExample",
            "Type": "ACS::CheckFor",
            "Properties": {
                "Service": "ECS",
                "API": "DescribeInstances",
                "Parameters": {
                    "InstanceId": "i-12345678abcedfg"
                },
                "PropertySelector": "jq selector",
                "DesiredValues": [
                    "value1",
                    "value2"
```

`],`

```json
                "NotDesiredValues": [
                    "value3",
                    "value4"
```

]

```json
                          },
        "Outputs": {
        "OutputParameter1": {
          "ValueSelector": "jq selector",
          "Type": "String/Boolean/List(Array)/Number/Object"
        }
      }
        }
```

]

```
}
```

**Example**

The following template is used to create a snapshot for the specified disk: Use the ACS::CheckFor action to check whether the specified instance is in the Running or Stopped status. YAML format

```
FormatVersion: OOS-2019-06-01 Parameters:
  DiskId:
    Description: the disk id of the snap shot to copy
    Type: String
  InstanceId:
    Description: the instances id  of the snap shot to copy
    Type: String
  SnapshotName:
    Description: snap shot name of the new snap
    Type: String
Tasks:
- Name: checkInstanceReady
Properties:
```

Operation Orchestration Service

```
  Properties:
      Service: ECS
    API: DescribeInstances
    DesiredValues:
    - Running
    - Stopped
    Parameters:
      InstanceIds:
      - '{{ InstanceId }} '
    PropertySelector: Instances.Instance[].Status
- Name: createSnapshot
  Properties:
      Service: ECS
    API: CreateSnapshot
    Parameters:
      DiskId: '{{ DiskId }}'
      SnapshotName: '{{ SnapshotName }}'
        Outputs:
      SnapshotId:
        Type: String
        ValueSelector: SnapshotId
- Name: waitSnapshotsReady
  Properties:
      Service: ECS
    API: DescribeSnapshots
    DesiredValues:
    - accomplished
    Parameters:
      SnapshotIds:
      - '{{ createSnapshot.SnapshotId }}'
    PropertySelector: Snapshots.Snapshot[].Status
Outputs:
  SnapshotId:
    Type: String
    Value: '{{ createSnapshot.SnapshotId }}'
```

JSON format

```json
{
    "FormatVersion": "OOS-2019-06-01",
    "Parameters": {
        "DiskId": {
            "Description": "the disk id of the snap shot to copy ",
            "Type": "String"
        },
        "InstanceId": {
            "Description": "the instances id  of the snap shot to copy ",
            "Type": "String"
        },
"SnapshotName":{
```

Operation Orchestration Service

```json
        SnapshotName: {
            "Description": "snap shot name of the new snap",
            "Type": "String"
        }
    },
    "Tasks": [
        {
            "Name": "checkInstanceReady",
            "Action": "ACS::CheckFor",
            "Properties": {
                "Service": "ECS",
                "API": "DescribeInstances",
                "DesiredValues": ["Running", "Stopped"],
                "Parameters": {
                    "InstanceIds": ["{{ InstanceId }} "]
                },
                "PropertySelector": "Instances.Instance[].Status"
            }
        },
        {
            "Name": "createSnapshot",
            "Action": "ACS::ExecuteAPI",
            "Properties": {
                "Service": "ECS",
                "API": "CreateSnapshot",
                "Parameters": {
                    "DiskId": "{{ DiskId }}",
                    "SnapshotName": "{{ SnapshotName }}"
                }
            },
            "Outputs": {
                "SnapshotId": {
                    "Type": "String",
                    "ValueSelector": "SnapshotId"
                }
            }
        },
        {
            "Name": "waitSnapshotsReady",
            "Action": "ACS::WaitFor",
            "Properties": {
                "Service": "ECS",
                "API": "DescribeSnapshots",
                "DesiredValues": ["accomplished"],
                "Parameters": {
                    "SnapshotIds": ["{{ createSnapshot.SnapshotId }}"]
                },
                "PropertySelector": "Snapshots.Snapshot[].Status"
            }
        }
```

`],`

```json
    "Outputs": {
        "SnapshotId": {
            "Type": "String",
            "Value": "{{ createSnapshot.SnapshotId }}"
```

| Product | Full name | API version | Release time |
|---|---|---|---|
| ActionTrail | ActionTrail | v20171204 | June 2019 |
| Alibaba Cloud DNS | Alibaba Cloud DNS | v20150109 | July 2019 |
| BOA | BSS OpenAPI | v20171214 | July 2019 |
| CAS | Alibaba Cloud Certificates Service | v20180813 | July 2019 |
| CDN | Content Delivery Network | v20180510 | July 2019 |
| CMS | CloudMonitor | v20190101 | July 2019 |
| DCDN | Dynamic Route for Content Delivery Network | v20180115 | July 2019 |
| DM | DirectMail | v20170622 | July 2019 |
| Dysmsapi | Short Message Service | v20170525 | July 2019 |
| ECS | Elastic Compute Service | v20140526 | June 2019 |
| ECI | Elastic Container Instance | v20180808 | July 2019 |
| EMR | Elastic MapReduce | v20160408 | August 2019 |
| ESS | Elastic Scaling Service | v20140828 | June 2019 |
| FC | Function Compute | v20160815 | July 2019 |
| gpdb | HybridDB for PostgreSQL | v20160503 | July 2019 |
| Market | Alibaba Cloud Marketplace | v20151101 | July 2019 |
| NAS | Network Attached Storage | v20170626 | July 2019 |

Operation Orchestration Service

```
aue: {{ceateSapsot.Sapsotd}}
        }
    }
}
```

#### List of supported cloud products

If you need to perform API actions on other cloud products, join the DingTalk group 23330931. We will offer help as soon as possible. The following table lists the cloud products that support API actions. The cloud products are sorted in alphabetical order.

| Operation Orchestration S | ervice | Devel | oper Guide ·Atom action |
|---|---|---|---|

| Product | Full name | API version | Release time |
|---|---|---|---|
| nls-cloud-meta | Intelligent Speech Interaction | v20190228 | July 2019 |
| Ons | RocketMQ | v20190214 | July 2019 |
| OSS | Object Storage Service |  | July 2019 |
| PetaData | HybridDB for MySQL | v20160101 | July 2019 |
| POLARDB | ApsaraDB for POLARDB | v20170801 | July 2019 |
| Push | Alibaba Cloud Mobile Push | v20160801 | July 2019 |
| RAM | Resource Access Management | v20150501 | June 2019 |
| RDS | Relational Database Service | v20140815 | June 2019 |
| SAS | Threat Detection Service | v20181203 | July 2019 |
| SCDN | Secure Content Delivery Network | v20171115 | July 2019 |
| SLB | Server Load Balancer | v20140515 | June 2019 |
| STS | Security Token Service | v20150401 | July 2019 |
| VOD | ApsaraVideo for VOD | v20170321 | July 2019 |
| VPC | Virtual Private Network | v20160428 | June 2019 |
| WAF | Web Application Firewall | v20180117 | July 2019 |
| R-KVSTORE | Cloud Database Redis | v20150101 | October 2019 |
| CR | Container Services Enterprise | v20181201 | October 2019 |
| OOS | Operation Orchestration Service | v20190601 | October 2019 |
| DDS | Cloud Database MongoDB | v20151201 | October 2019 |
| DDOSPRO | DDoS High Level Protection IP | v20170725 | October 2019 |
| ARMS | Application Real-Time Monitoring Service | v20190808 | October 2019 |
| HDR | Hybrid Disaster Recovery | v20170925 | October 2019 |

|  | Developer Guide ·Atom a | ctions | Opera | tion Orchestration Servic | e |
|---|---|---|---|---|---|

| Product | Full name | API version | Release time |
|---|---|---|---|
| DDOSCOO | New BGP High Level Protection IP | v20171228 | October 2019 |
| RDC-INNER | Cloud Efficiency(Inner) | v20180821 | October 2019 |
| ROS | Resource Orchestration | v20190910 | October 2019 |
| DDOSBGP | DDoS Protection Suite | v20180720 | October 2019 |

### Trigger actions

### Control actions

#### ACS::Approve

**Features**

During automatic O&M, you need to pay special attention to some operations, such as deleting important resources or purchasing instances with high costs. If these operations are performed automatically, you may lose control and exceed the budget. However, if these operations are performed automatically, you need to perform them manually or in some other non-automatic ways. In this case, you can use the ACS::Approve action to strike a balance between automatic execution and operations that need special attention. When executing an ACS::Approve action in a template, the CloudOps Orchestration Service (OOS) execution engine suspends the execution of the subsequent operations, sets the execution status to Waiting, and sends a notification. After receiving the notification, you can determine whether to approve or reject the operation based on the business requirements. If the operation is approved, the OOS engine continues to perform the subsequent operations. If the operation is rejected, the OOS engine stops the execution, and sets the execution status to Cancelled.

**Syntax**

**Webhook**

You can configure webhooks to send notifications to clients, such as DingTalk. YAML format Operation Orchestration Service

```
Tasks:
  - Name: approvalTask
    Properties:
      NotifyType: WebHook
      AppendExecutionLink: 'true'  # Append execution link or not . ACS::Approve defaul
t option is true.
      WebHook:
        URI: url # Required. The webhook URL, such as
https://oapi.dingtalk.com/robot/send?access_token=xxxxxx.
        Headers: # Optional. The headers of the Hypertext Transfer Protocol (HTTP) requ
est, such as Content-Type.
          Content-Type: 'application/json; charset=utf-8'
        Content: # Required. This attribute is set based on the specific requirements o
f webhooks. For more information about the content of the DingTalk webhook, see https:/ /open-doc.dingtalk.com/docs/doc.htm?treeId=257&articleId=105735&docType=1.
          msgtype: text
          text:
            content: 'the approve notify to user'  # Required,the notice content to
send with approve link.
          at:  #  in dingtalk group  @ user when approval notice sent.
            atMobiles: # Optional, @ specified user in dingtalk group,the phone number
is account specified user signed in with.
            - 138albb1234
            - 130albb1234
            isAtAll: 'false'  # Optional, @ all users in dingtalk group or not, "true"
or "false" optional.
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
  "Tasks": [
    {
      "Name": "approvalTask",
      "Action": "ACS::Approve",
      "Properties": {
        "NotifyType": "WebHook",
        "AppendExecutionLink": "true",
        "WebHook": {
          "URI": "url",
          "Headers": {
            "Content-Type": "application/json; charset=utf-8"
          },
          "Content": {
            "msgtype": "text",
            "text": {
              "content": "the approve notify to user"
            },
            "at": {
              "atMobiles": [
                "138albb1234",
                "130albb1234"
```

`],`

```json
              "isAtAll": "false"
            }
          }
        }
      }
    }
```

]

```
}
```

**Example**

The following template is used to delete an ECS after approval: YAML format

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky restarts the ECS instances with Approval.
  name-en: BulkyRebootInstancesWithApproval
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
    Type: Json
    AssociationProperty: RateControl
    Default:
Mode:Concurrency
```

Operation Orchestration Service

```
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 100%
  webHookUrl:
    Description:
      en: 'The webHook url of dingtalk group assistant,
e.g.https://oapi.dingtalk.com/robot/send?access_token=1234zxcvaksdq31414.'
    Type: String
  atMobiles:
    Description:
      en: 'The telephone numbers of member in dingtalk group assistant @, when notify c
omes.'
    Type: List
    Default:
      - '12345678901'
  atAll:
    Description:
      en: 'assistant @ all members in dingtalk group or not, when notify comes.'
    Type: String
    Default: 'false'
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
      instanceNames:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceName'
  - Name: approveRestart
    Properties:
      NotifyType: WebHook
      WebHook:
        URI: '{{webhookUrl}}'
        Headers:
          Content-Type: application/json
        Content:
          msgtype: text
          text:
            content: 'Notify: please approve instances restart, instance names to
are{{getInstance.instanceNames}},sentby{{ACS::RegionId}}oos
```

Operation Orchestration Service

```
approve are {{getInstance.instanceNames}}, sent by {{ACS::RegionId}} oos {{ACS::ExecutionId}}.'
          at:
            atMobiles: '{{atMobiles}}'
            isAtAll: '{{atAll}}'
  - Name: rebootInstance
    Action: 'ACS::ECS::RebootInstance'
    Description:
      en: Restarts the ECS instances.
    Properties:
      instanceId: '{{ ACS::TaskLoopItem }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
Outputs:
  instanceIds:
    Type: List
    Value: '{{ getInstance.instanceIds }}'
```

JSON format

```json
{
  "FormatVersion": "OOS-2019-06-01",
  "Description": {
    "en": "Bulky restarts the ECS instances with Approval.",
    "name-en": "BulkyRebootInstancesWithApproval"
  },
  "Parameters": {
    "targets": {
      "Type": "Json",
      "AssociationProperty": "Targets",
      "AssociationPropertyMetadata": {
        "ResourceType": "ALIYUN::ECS::Instance"
      }
    },
    "rateControl": {
      "Description": {
        "en": "Concurrency ratio of task execution."
      },
      "Type": "Json",
      "AssociationProperty": "RateControl",
      "Default": {
        "Mode": "Concurrency",
        "MaxErrors": 0,
        "Concurrency": "100%"
      }
    },
    "webHookUrl": {
      "Description": {
        "en": "The webHook url of dingtalk group assistant,
e.g.https://oapi.dingtalk.com/robot/send?access_token=1234zxcvaksdq31414."
      },
      "Type": "String"
    },
"atMobiles":{
```

Operation Orchestration Service

```json
    atMobiles: {
      "Description": {
        "en": "The telephone numbers of member in dingtalk group assistant @, when
notify comes."
      },
      "Type": "List",
      "Default": [
        "12345678901"
```

]

```json
    },
    "atAll": {
      "Description": {
        "en": "assistant @ all members in dingtalk group or not, when notify comes."
      },
      "Type": "String",
      "Default": "false"
    },
    "OOSAssumeRole": {
      "Description": {
        "en": "The RAM role to be assumed by OOS."
      },
      "Type": "String",
      "Default": "OOSServiceRole"
    }
  },
  "RamRole": "{{ OOSAssumeRole }}",
  "Tasks": [
    {
      "Name": "getInstance",
      "Description": {
        "en": "Views the ECS instances."
      },
      "Action": "ACS::SelectTargets",
      "Properties": {
        "ResourceType": "ALIYUN::ECS::Instance",
        "Filters": [
          "{{ targets }}"
```

]

```json
      },
      "Outputs": {
        "instanceIds": {
          "Type": "List",
          "ValueSelector": "Instances.Instance[].InstanceId"
        },
        "instanceNames": {
          "Type": "List",
          "ValueSelector": "Instances.Instance[].InstanceName"
        }
      }
    },
    {
      "Name": "approveRestart",
      "Action": "ACS::Approve",
      "Properties": {
        "NotifyType": "WebHook",
```

Operation Orchestration Service `ot`

```
yype: eboo
```

,

```json
        "WebHook": {
          "URI": "{{webhookUrl}}",
          "Headers": {
            "Content-Type": "application/json"
          },
          "Content": {
            "msgtype": "text",
            "text": {
              "content": "Notify: please approve instances restart, instance names to
approve are {{getInstance.instanceNames}}, sent by {{ACS::RegionId}} oos {{ACS::ExecutionId}}."
            },
            "at": {
              "atMobiles": "{{atMobiles}}",
              "isAtAll": "{{atAll}}"
            }
          }
        }
      }
    },
    {
      "Name": "rebootInstance",
      "Action": "ACS::ECS::RebootInstance",
      "Description": {
        "en": "Restarts the ECS instances."
      },
      "Properties": {
        "instanceId": "{{ ACS::TaskLoopItem }}"
      },
      "Loop": {
        "RateControl": "{{ rateControl }}",
        "Items": "{{ getInstance.instanceIds }}"
      }
    }
```

`],`

```json
  "Outputs": {
    "instanceIds": {
      "Type": "List",
      "Value": "{{ getInstance.instanceIds }}"
    }
  }
}
```

#### ACS::Choice

**Description**

The ACS::Choice action can be used to determine the task to be run based on the judgment of the conditions For example, before you restart an instance, you want to query the status of the instance and select the task to be run based on the returned result. If the instance is in the Running state, the restart task is run. If the instance is in the Stopped state, the start task is run. If the instance is in other states, the query task is run. Operation Orchestration Service

**Syntax**

YAML JSON

```bash
Tasks:
- Name: chooseNextTaskToRun # The name of the task.
  Properties:
    DefaultTask: task1 # The default task that is run if no condition specified by Choi
ces is met after the chooseNextTaskToRun task is run. The name of the task1 task cannot be the name of a parameter. It must be a certain string.
    Choices:
      - When: condition1 # The first condition for judgment.
        NextTask: task2 # The task that is run if the first condition is met.
      - When: condition2 # The second condition for judgment.
        NextTask: task3 # The task that is run if the second condition is met.
        # If necessary, you can use more WHEN conditions in the command.
        #...
```

**Examples**

YAML JSON

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky restarts the ECS instances.
  null-null-null
  name-en: ACS-ECS-BulkyRebootInstances
  null-null-null
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
      null-null-null
    Type: Json
    AssociationProperty: RateControl
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
      null-null-null
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
nllnllnll
```

Operation Orchestration Service

```
      null-null-null
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
  - Name: describeInstances
    Description: Views A ECS instances Status.
    Properties:
      Service: ECS
      API: DescribeInstances
      Parameters:
        InstanceIds: '{{ getInstance.instanceIds }}'
    Outputs:
      status:
        Type: String
        ValueSelector: Instances.Instance[].Status
  - Name: whetherStatusRunning
    Properties:
      DefaultTask: describeInstancesFinally
      Choices:
        - When:
            'Fn::Equals':
              - Running
              - '{{ describeInstances.status }}'
          NextTask: rebootInstance
        - When:
            'Fn::Equals':
              - Stopped
              - '{{ describeInstances.status }}'
          NextTask: startInstance
  - Name: startInstance
    Action: 'ACS::ECS::StartInstance'
    Description:
      en: Starts the ECS instances.
      null-null-null
    Properties:
      instanceId: '{{ ACS::TaskLoopItem }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
  - Name: rebootInstance
    Action: 'ACS::ECS::RebootInstance'
    Description:
      en: Restarts the ECS instances.
      null-null-null
    Properties:
instanceId:'{{ACS::TaskLoopItem}}'
```

Operation Orchestration Service

```
      instanceId: {{ ACS::TaskLoopItem }}
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
  - Name: describeInstancesFinally
    Description: Views the ECS instances Status.
    Properties:
      Service: ECS
      API: DescribeInstances
      Parameters:
        InstanceIds: '{{ getInstance.instanceIds }}'
    Outputs:
      status:
        Type: String
        ValueSelector: Instances.Instance[].Status
Outputs:
  instanceIds:
    Type: List
    Value: '{{ getInstance.instanceIds }}'
```

#### ACS::Notify

**Description**

The ACS::Notify action notifies you when an operations and maintenance (O&M) task is completed. For example, after you purchase an Elastic Compute Service (ECS) instance, you can receive a DingTalk notification to view the bill in real time.

**Syntax**

ACS::Notify supports webhook and email notifications. You can use the following syntax to configure webhook and email notifications.

**Webhook**

YAML format Operation Orchestration Service

```
Tasks:
  - Name: notifyTask
    Properties:
      NotifyType: WebHook
   AppendExecutionLink: 'false' # Specifies whether to append execution links. Valid va
lues: true and false. Default value: false.
      WebHook:
        URI: url # Required. The webhook URL. Example:
https://oapi.dingtalk.com/robot/send?access_token=xxxxxx.
        Headers: # Optional. The header of the HTTP request. Example: Content-Type.
          Content-Type: 'application/json; charset=utf-8'
        Content: # Required. The content of the webhook notification. Set the value bas
ed on the requirements for the webhook. For information about the content of the DingTa lk webhook, visit https://www.alibabacloud.com/help/doc-detail/144679.htm#h2-appendix-2 -obtain-the-webhook-url5.
          msgtype: text
          text:
            content: 'this is a dingtalk message with a parameter {{ p1 }}'
```

JSON format For more information, see the parameter description for the YAML format.

```json
{
  "Tasks": [
    {
      "Name": "notifyTask",
      "Action": "ACS::Notify",
      "Properties": {
        "NotifyType": "WebHook",
        "AppendExecutionLink": "false",
        "WebHook": {
          "URI": "url",
          "Headers": {
            "Content-Type": "application/json; charset=utf-8"
          },
          "Content": {
            "msgtype": "text",
            "text": {
              "content": "this is a dingtalk message with a parameter {{ p1 }}"
            }
          }
        }
      }
    }
```

]

```
}
```

**Email**

YAML format Operation Orchestration Service

```
Tasks:
    Name: testNotifyByMail
    Properties:
        NotifyType: Mail
        Mail:
         Host: SMTPHostAddress # The Simple Mail Transfer Protocol (SMTP) server addres
s. Example: smtp.example1.com.
            Port: SMTPPort # The port number of the SMTP server. Example: 465.
            Username: sender  # The email account that is used to send the
notification. Example: usr001@example1.com.
            Password: senderPassword # The password of the email account that is used t
o send the notification. Example: 123456zxcv.
            Subject: mailSubject # The subject of the email notification. Example:
hello world.
            Body: mailBody # The body of the email notification. Example: hello
world!!!
            From: senderAddress # The email address of the sender. Example:
usr001@example1.com.
            To:  receiverAddresses # The email addresses of the recipients. Example: [u
sr1234@example2.com,usr123@example2.com].
```

JSON format For more information, see the parameter description for the YAML format.

```json
{
  "Tasks": [
    {
      "Action": "ACS::Notify",
      "Name": "testNotifyByMail",
      "Properties": {
        "NotifyType": "Mail",
        "Mail": {
          "Host": "SMTPHostAddress",
          "Port": "SMTPPort",
          "Username": "sender",
          "Password": "senderPassword",
          "Subject": "mailSubject",
          "Body": "mailBody",
          "From": "senderAddress",
          "To": "receiverAddresses"
        }
      }
    }
```

]

```
}
```

**Examples**

YAML format Operation Orchestration Service

```
--- FormatVersion: OOS-2019-06-01 Outputs:
    InstanceIds:
        Type: List
        Value: ' {{ runInstances.InstanceIds }} '
Parameters:
    ImageId:
        Description: the image id for the new instances.
        Type: String
    InstanceType:
        Description: the Instance Type for the new instances.
        Type: String
    OOSAssumeRole:
        Default: OOSServiceRole
        Description: oos assume this role to execution task
        Type: String
    SecurityGroupId:
        Description: the security group id for the new instances.
        Type: String
    VSwitchId:
        Description: the virtual switch id for the new instances.
        Type: String
RamRole: '{{OOSAssumeRole}}' Tasks:
    Description: 'run instances with specified parameters, refer them here:
https://help.aliyun.com/document_detail/63440.html'
    Name: runInstances
    Outputs:
        InstanceIds:
            Type: List
            ValueSelector: .InstanceIdSets.InstanceIdSet[]
    Properties:
        API: RunInstances
        Parameters:
            ImageId: '{{ ImageId }}'
            InstanceType: '{{ InstanceType }}'
            SecurityGroupId: '{{ SecurityGroupId }}'
            VSwitchId: '{{ VSwitchId }}'
        Service: ECS
    Name: test_notify
    Properties:
        NotifyType: WebHook
        WebHook:
            Content:
                msgtype: text
                text:
                 content:
            Headers:
                Content-Type: application/json
            URI: https://oapi.dingtalk.com/robot/send?access_token=your_access_token
```

Operation Orchestration Service JSON format

```json
{
    "FormatVersion": "OOS-2019-06-01",
    "Outputs": {
        "InstanceIds": {
            "Type": "List"
            "Value": " {{ runInstances.InstanceIds }} "
        }
    },
    "Parameters": {
        "ImageId": {
            "Description": "the image id for the new instances.",
            "Type": "String"
        },
        "InstanceType": {
            "Description": "the Instance Type for the new instances.",
            "Type": "String"
        },
        "SecurityGroupId": {
            "Description": "the security group id for the new instances.",
            "Type": "String"
        },
        "VSwitchId": {
            "Description": "the virtual switch id for the new instances.",
            "Type": "String"
        },
          "OOSAssumeRole": {
        "Type": "String",
        "Description":  "oos assume this role to execution task",
        "Default": "OOSServiceRole"
    }
    },
    "RamRole": "{{OOSAssumeRole}}",
    "Tasks": [
        {
            "Action": "ACS::ExecuteAPI",
            "Description": "run instances with specified parameters, refer them here:
https://help.aliyun.com/document_detail/63440.html",
            "Name": "runInstances",
            "Outputs": {
                "InstanceIds": {
                    "Type": "List",
                    "ValueSelector": ".InstanceIdSets.InstanceIdSet[]"
                }
            },
            "Properties": {
                "API": "RunInstances",
                "Parameters": {
                    "ImageId": "{{ ImageId }}",
                    "InstanceType": "{{ InstanceType }}",
                    "SecurityGroupId": "{{ SecurityGroupId }}",
                    "VSwitchId": "{{ VSwitchId }}"
                },
"Service":"ECS"
```

Operation Orchestration Service

```json
                "Service": "ECS"
            }
        },
       {
      "Name": "test_notify",
      "Action": "ACS::Notify",
      "Properties": {
        "NotifyType": "WebHook",
        "WebHook": {
          "URI": "https://oapi.dingtalk.com/robot/send?access_token=your_access_token",
          "Headers": {
            "Content-Type": "application/json"
          },
          "Content": {
            "msgtype": "text",
            "text": {
              "content":"test"
            }
          }
        }
      }
    }
```

]

```
}
```

#### ACS::Sleep

**Features**

The ACS::Sleep action can be used if waiting is required during O&M. For example, a newly created ECS instance with an application needs to be pre-loaded for a period of time before the subsequent O&M operations can be performed.

**Syntax**

YAML format

```
Tasks:
  - Name: sleepTask # The name of the task.
    Properties:
      Duration: PT15M # Required. The waiting duration.
```

JSON format (For more information, see the parameter description for the YAML format.) Operation Orchestration Service

```json
{
  "Tasks": [
    {
      "Name": "sleepTask",
      "Action": "ACS::Sleep",
      "Properties": {
        "Duration": "PT15M"
      }
    }
```

]

```
}
```

**Description**

**Duration**

The ISO 8601 standard is used to define the waiting duration. The duration ranges from 1 minute to 4 hours. The value is not case-sensitive. Examples: 1M or 1m: indicates 1 minute in the contracted form. 1H or 1h: indicates 1 hour in the contracted form. 1H2M: indicates 1 hour and 2 minutes in the contracted form. PT1H2M: indicates 1 hour and 2 minutes in the standard form.

### Embedding actions

#### Embedding actions

**Features**

The ACS::Template action can be used to embed another template to the current template as a child template. You can use this action to modularize a complex template and split it into multiple child templates for calling. You can also define common O&M operations as reusable child templates. In addition, Operation Orchestration Service (OOS) provides operation templates of common cloud product actions. You can embed these templates in your template. For more information, see Cloud product actions.

**Syntax**

General format (applicable to all embedded templates) YAML format

```
Tasks:
- Name: callChildTemplate1
Action: ACS::Template Properties: TemplateName: child_template_name # Required. The name of the child template. Parameters: # Optional. The parameters required for executing the child template.
  ParameterName1: value1
```

Operation Orchestration Service JSON format (For more information, see the parameter description for the YAML format.)

```json
{ "Tasks": [ { "Name": "callChildTemplate1", "Action": "ACS::Template", "Properties": {
  "TemplateName": "child_template_name",
  "Parameters": {
    "ParameterName1": "value1"
  }
} }
```

]

```
}
```

Simplified format (only applicable to the cloud product actions) YAML format

```
Tasks:
- Name: taskName # Required. The name of the task. Example: runMyInstances.
  Action: CloudProductActionName1 # Required. The name of the cloud product action.
Example: ACS::ECS::RunInstances.
  Properties:
    ParameterName1: value1 # Optional. The parameter required for executing the clo
ud production action. Example: ImageId.
```

JSON format (For more information, see the parameter description for the YAML format.)

```json
{ "Tasks": [
  {
    "Name": "taskName",
    "Action": "CloudProductActionName1",
    "Properties": {
      "ParameterName1": "parameterName1"
    }
  }
```

]

```
}
```

**Restrictions**

The embedding actions have the following restrictions: The template cannot embed itself. Loop embedding, for example, A embeds B, B embeds C, and C embeds A, is not allowed. The total number of embedding layers cannot exceed three. The embedding of a cloud product action is regarded as one layer of embedding, while loop tasks cannot be treated as embedding.

**Example**

Operation Orchestration Service The following template is used to create an image for an ECS instance by embedding the cloud product action `ACS::ECS::CreateImage` : General format (applicable to all embedded templates) YAML format

```
--- FormatVersion: OOS-2019-06-01 Description: Creates a custom image. Parameters:
  imageName:
    Description: The image name.
    Type: String
  instanceId:
    Description: The ID of the instance.
    Type: String
    AllowedPattern: i-[A-Za-z0-9]*
    MinLength: 1
    MaxLength: 30
  OOSAssumeRole:
    Type: String
    Description: oos assume this role to execution task
    Default: OOSServiceRole
RamRole: '{{OOSAssumeRole}}' Tasks:
- Name: createImage
  Action: ACS::Template
  Description: Creates a custom image.
  Properties:
    TemplateName: 'ACS::ECS::CreateImage'
    Parameters:
      ImageName: '{{ imageName }}'
      InstanceId: '{{ instanceId }}'
  Outputs:
    imageId:
      Type: String
      ValueSelector: ImageId
Outputs:
  imageId:
    Type: String
    Value: '{{ createImage.imageId }}'
```

JSON format Operation Orchestration Service

```json
{
    "FormatVersion": "OOS-2019-06-01",
    "Description": "Creates a custom image.",
    "Parameters": {
        "imageName": {
            "Description": "The image name.",
            "Type": "String"
        },
        "instanceId": {
            "Description": "The ID of the instance.",
            "Type": "String",
            "AllowedPattern": "i-[A-Za-z0-9]*",
            "MinLength": 1,
            "MaxLength": 30
        },
        "OOSAssumeRole": {
            "Type": "String",
            "Description": "oos assume this role to execution task",
            "Default": "OOSServiceRole"
        }
    },
    "RamRole": "{{OOSAssumeRole}}",
    "Tasks": [
        {
            "Name": "createImage",
            "Action": "ACS::Template",
            "Description": "Creates a custom image.",
            "Properties": {
                "TemplateName": "ACS::ECS::CreateImage",
                "Parameters": {
                    "ImageName": "{{ imageName }}",
                    "InstanceId": "{{ instanceId }}"
                }
            },
            "Outputs": {
                "imageId": {
                    "Type": "String",
                    "ValueSelector": "ImageId"
                }
            }
        }
```

`],`

```json
    "Outputs": {
        "imageId": {
            "Type": "String",
            "Value": "{{ createImage.imageId }}"
        }
    }
}
```

Simplified format (only applicable to the cloud product actions) YAML format Operation Orchestration Service

```
--- FormatVersion: OOS-2019-06-01 Description: Creates a new Image from existing ECS Instance. Parameters:
  InstanceId:
    Description: the Instance Type for the new instances
    Type: String
  ImageName:
    Description:  name of the new image
    Type: String
  OOSAssumeRole:
    Type: String
    Description: oos assume this role to execution task
    Default: OOSServiceRole
RamRole: "{{OOSAssumeRole}}" Tasks:
  - Name: createImage
    Action: ACS::ECS::CreateImage
    Properties:
      ImageName: "{{ ImageName }}"
      InstanceId: "{{ InstanceId }}"
    Outputs:
      ImageId:
        ValueSelector: ImageId
        Type: String
Outputs:
  ImageId:
    Type: String
    Value: "{{ createImage.ImageId }}"
```

JSON format Operation Orchestration Service

```json
{
  "FormatVersion": "OOS-2019-06-01",
  "Description": "Creates a new Image from existing ECS Instance.",
  "Parameters": {
    "InstanceId": {
      "Description": "the Instance Type for the new instances",
      "Type": "String"
    },
    "ImageName": {
      "Description": "name of the new image",
      "Type": "String"
    },
    "OOSAssumeRole": {
      "Type": "String",
      "Description": "oos assume this role to execution task",
      "Default": "OOSServiceRole"
    }
  },
  "RamRole": "{{OOSAssumeRole}}",
  "Tasks": [
    {
      "Name": "createImage",
      "Action": "ACS::ECS::CreateImage",
      "Properties": {
        "ImageName": "{{ ImageName }}",
        "InstanceId": "{{ InstanceId }}"
      },
      "Outputs": {
        "ImageId": {
          "ValueSelector": "ImageId",
          "Type": "String"
        }
      }
    }
```

`],`

```json
  "Outputs": {
    "ImageId": {
      "Type": "String",
      "Value": "{{ createImage.ImageId }}"
    }
  }
}
```

| Cloud product action | Description | API operation | Parameter | Output | Sample code |
|---|---|---|---|---|---|
| ACS::ECS::De scribeInstanc esByTag | You can use this action to query ECS instances by tag. | DescribeInsta nces | tagKey: String tagValue: String | instanceIds : List | YAML |
| ACS::ECS::Ru nInstances | You can use this action to start one or more ECS instances. | RunInstances DescribeInsta nces | imageId: String instanceTy pe: String securityGro upId: String vSwitchId: String amount: String | instanceIds : List | YAML |
| ACS::ECS::Ru nInstancesFro mTemplate | You can use this action to create an ECS instance by executing a template. | RunInstances DescribeInsta nces | launchTem plateId: String launchTem plateName: String amount: Number | instanceIds : List | YAML |
| ACS::ECS::Del eteInstance | You can use this action to delete an ECS instance. | DeleteInstanc e | instanceId: String | - | YAML |
| ACS::ECS::Sta rtInstance | You can use this action to start an ECS instance. | StartInstance DescribeInsta nces | instanceId: String | - | YAML |

Operation Orchestration Service

## Cloud product actions

### ECS actions

This topic describes the Elastic Compute Service (ECS) actions specific to various scenarios, including their usage, involved API operations, parameters, outputs, and sample code. You can use the ACS::Template action to call the cloud product actions. For more information, see ACS::Template.

**Instance operation scenarios**

| ACS::ECS::Sto pInstance | You can use this action to stop an ECS instance. | StopInstance DescribeInsta nces | instanceId: String | - | YAML |
|---|---|---|---|---|---|
| ACS::ECS::Re bootInstance | You can use this action to restart an ECS instance. | RebootInstan ce DescribeInsta nces | instanceId: String | - | YAML |
| ACS::ECS::De scribeInstanc esByName | You can use this action to query ECS instances by name. | DescribeInsta nces | instanceNa me: String | instanceIds : List | YAML |
| ACS::ECS::De scribeInstanc esByStatus | You can use this action to query ECS instances by status. | DescribeInsta nces | status: String | instanceIds : List | YAML |

| Cloud product action | Description | API operation | Parameter | Output | Sample code |
|---|---|---|---|---|---|
| ACS::ECS::Re sizeDisk | You can use this action to expand a cloud disk. | DescribeInsta nces ResizeDisk DescribeDisks RebootInstan ce DescribeInsta nces | diskId: String instanceId: String newSize: String | - | YAML |
| ACS::ECS::Mo difyInstanceV pcAttribute | You can use this action to modify the VPC attributes of an ECS instance. | StopInstance DescribeInsta nces ModifyInstanc eVpcAttribute | instanceId: String vSwitchId: String | - | YAML |

Operation Orchestration Service

**Instance modification scenarios**

| ACS::ECS::Re setPassword | You can use this action to change the password of an ECS instance. | ModifyInstanc eAttribute RebootInstan ce DescribeInsta nces | instanceId: String password: String | instanceId: String | YAML |
|---|---|---|---|---|---|
| ACS::ECS::Mo difyVncPassw ord | You can use this action to change the Virtual Network Computing (VNC) password of an ECS instance. | ModifyInstanc eVncPasswd RebootInstan ce DescribeInsta nces | instanceId: String vncPasswor d: String | - | YAML |
| ACS::ECS::Mo difyPrepaySp ec | You can use this action to upgrade or downgrade the specification of a subscribed ECS instance. | StopInstance DescribeInsta nces ModifyPrepayI nstanceSpec StartInstance DescribeInsta nces | instanceId: String autoPay: String instanceTy pe: String | orderId: String | YAML |
| ACS::ECS::Att achDisk | You can use this action to attach a cloud disk to an ECS instance. | AttachDisk DescribeDisks | instanceId: String diskId: String | - | YAML |
| ACS::ECS::Det achDisk | You can use this action to detach a cloud disk from an ECS instance. | DetachDisk DescribeDisks | instanceId: String diskId: String | - | YAML |

| Cloud product action | Description | API operation | Parameter | Output | Sample code |
|---|---|---|---|---|---|

Operation Orchestration Service

**Cloud Assistant scenarios**

| ACS::ECS::Ins tallCloudAssis tant | You can use this action to install Cloud Assistant. | InstallCloudAs sistant RebootInstan ce DescribeInsta nces DescribeClou dAssistantSta tus | instanceId: String | - | YAML |
|---|---|---|---|---|---|
| ACS::ECS::Ru nCommand | You can use this action to run a command in the Cloud Assistant client. | CreateComm and InvokeComm and DescribeInvoc ations DescribeInvoc ationResults DeleteComm and | instanceId: String commandC ontent: String commandT ype: String | invocationR esult: String | YAML |

| Cloud product action | Description | API operation | Parameter | Output | Sample code |
|---|---|---|---|---|---|
| ACS::ECS::Cre ateImage | You can use this action to create an image. | DescribeInsta nces CreateImage DescribeImag es | instanceId: String imageNam e: String | imageId: String | YAML |
| ACS::ECS::Cre ateSnapshot | You can use this action to create a snapshot. | DescribeInsta nces CreateSnapsh ot | instanceId: String diskId: String snapshotN ame: String | snapshotId: String | YAML |
| ACS::ECS::Re setDisk | You can use this action to restore a cloud disk to a specific snapshot status at a given time point. | StopInstance DescribeInsta nces DescribeInsta nces | instanceId: String diskId: String snapshotId: String | - | YAML |

Operation Orchestration Service

**Other scenarios**

| ACS::ECS::Cre ateAndAttach Disk | You can use this action to create a cloud disk and attach it to an ECS instance. | DescribeInsta nces CreateDisk DescribeDisks AttachDisk | instanceId: String diskName: String zoneId: String diskCatego ry: String size: String | diskId: String | YAML |
|---|---|---|---|---|---|
| ACS::ECS::Re placeSystem Disk | You can use this action to replace the system disk. | StopInstance DescribeInsta nces ReplaceSyste mDisk StartInstance | instanceId: String imageId: String | - | YAML |
| ACS::ECS::ReI nitDisk | You can use this action to initialize a cloud disk. | DescribeDisks DescribeInsta nces ReInitDisk StartInstance DescribeInsta nces | diskId: String | - | YAML |
| ACS::ECS::All ocatePublicIp Address | You can use this action to assign a public IP address to an instance. | DescribeInsta nces AllocatePublic IpAddress RebootInstan ce DescribeInsta nces | instanceId: String | - | YAML |
| ACS::ECS::Cre ateAndAttach NetworkInterf ace | You can use this action to create and install a network interface card (NIC). | DescribeInsta nces CreateNetwor kInterface AttachNetwor kInterface | instanceId: String securityGro upId: String vSwitchId: String | networkInt erfaceId: String | YAML |

Operation Orchestration Service

| ACS::ECS::Del eteImage | You can use this action to delete an image. | DeleteImage | imageId: String | - | YAML |
|---|---|---|---|---|---|
| ACS::ECS::Ins tallLogtail | You can use this action to install Logtail. | DescribeInsta nces CreateComm and InvokeComm and DescribeInvoc ations DescribeInvoc ationResults DeleteComm and | instanceId: String logTailUser DefinedId: String OOSAssum eRole: String | exitCode: String invocationR esult: String | YAML |

| Cloud product action | Description | Parameter | Output | Sample code |
|---|---|---|---|---|
| ACS::Notify::Ding TalkWebhook | You can use this action to send notifications to DingTalk through webhooks. | webhook: String msgtype: String text: JSON link: JSON markdown: JSON at: JSON | - | YAML |

Operation Orchestration Service

### DingTalk actions

This topic describes the DingTalk actions, including their usage, parameters, outputs, and sample code. You can use the ACS::Template action to call the cloud product actions. For more information, see ACS::Template.

| Cloud product action | Description | Parameter | Output | Sample code |
|---|---|---|---|---|
| ACS::Approve::Di ngTalkWebhook | You can use this action to send notifications to DingTalk through webhooks for approval. The execution remains in the Waiting status until the execution is approved or rejected. The execution continues if it is approved. Otherwise, the execution ends. | webhook: String msgtype: String text: JSON link: JSON markdown: JSON at: JSON | - | YAML |

Operation Orchestration Service Operation Orchestration Service

## Executions

### Overview

Operation Orchestration Service (OOS) allows you to execute a public or custom template in multiple execution modes.

**Execution modes**

Automatic: We recommend that you execute a template in this mode in the test environment first. In this way, you can have a better understanding of the O&M operations performed by the template. If the test result meets the expectations, you can execute the template in this mode in the production environment. Automatic execution: All tasks defined in the template are automatically executed in sequence. Execution that requires risk confirmation: When OOS automatically executes an irrevocable task in the template, such as the delete, release, or stop task, the execution state of the template changes to **Waiting** until you approve the task. Manual: This execution mode is similar to debugging. If you want to know more about the execution of each task, we recommend that you use the manual execution mode.

**Risk confirmation modes**

Require confirmation for high-risk tasks: For irrevocable O&M operations, such as deleting an ECS instance, you must manually confirm the operations. We recommend that you give priority to this mode when you execute a new template. Skip confirmation for high-risk tasks: If you are familiar with all the tasks orchestrated by a template, you can select this mode to skip the confirmation.

### Execute a template in

**automatic execution mode**

You can execute a public template provided by Operation Orchestration Service (OOS) or a custom template that you create. If you are aware of the risks of all tasks in the template, you can select Automatic for the Execution Mode parameter when you create an execution. This topic describes how to execute a public template in automatic execution mode.
1. Log on to the **OOS console**.
2. In the left-side navigation pane, click **Public Template**. On the Public Template page,
select the public template that you want to execute and click **Create Execution**.
3. In the Create Task wizard, configure basic information. Then, click **Next Step: Parameter**
**Settings**.
4. Configure the parameters required for the template.
5. Click **Next Step: OK**.
6. Click **Create**.
7. On the Task Execution Management page, find the execution that you created and click
**Details** in the Actions column to view the execution details.
Operation Orchestration Service

### Execute a template in manual

**execution mode**

You can execute a public template provided by Operation Orchestration Service (OOS) or a custom template that you create. If you want to manually execute a specific task in the template, you can select the manual execution mode when you create an execution. This topic describes how to execute a public template in manual execution mode in the console.
1. Log on to the **OOS console**.
2. In the left-side navigation pane, click **Public Template**. On the Public Template page,
select the public template that you want to execute and click **Create Execution**.
3. Select **Manual** for the Execution Mode parameter.
4. Click **Next Step: Parameter Settings**.
5. Configure the parameters required for the template.
6. Click **Next Step: OK**.
7. Click **Create**.
8. On the Task Execution Management page, find the execution that you created and click
**Details** in the Actions column to view the execution details.
9. Click **Configure Next Task**.
0. Click **OK**.
1. Click **Log**. View the run logs of the task being debugged.

### View the details of an

**execution**

When you use Operation Orchestration Service (OOS), you can view the information about the existing executions at any time.
1. Log on to the **OOS console**.
2. In the left-side navigation pane, click **Task Execution Management**.
3. On the Task Execution Management page, find the execution that you want to view and
click **Details** in the Actions column.
4. On the page that appears, you can view the execution information shown in the following
figure.
5. In the **execution result** section, click a task node to view the details of the task.

### Cancel an execution

Operation Orchestration Service (OOS) allows you to cancel an execution.
1. Log on to the **Apsara Stack OOS console**.
2. In the left-side navigation pane, click Task Execution Management. On the page that
appears, find the execution that you want to manage and click Details in the Actions column.
3. In the upper-right corner of the Basic Information section, click **cancel execution**.
4. In the cancel execution message, click **OK**.

| State | State | Description |
|---|---|---|
| Started | Started | The execution is started. After an execution is created, it immediately enters this state. |
| Queued | Queued | The execution is waiting in the queue due to traffic control. In most cases, the executions that you start skip this state and directly enter the Running state. |

Operation Orchestration Service

### Delete an execution

Operation Orchestration Service (OOS) allows you to delete an execution in a final state. If the execution that you want to delete is in a non-final state, such as Waiting or Running, you must cancel the execution before you delete it.
1. Log on to the **Apsara Stack OOS console**.
2. In the left-side navigation pane, click **Task Execution Management**.
3. On the Task Execution Management page, find the execution that you want to delete and
clickDeletein the Actions column.
4. In the delete execution message, click **OK**.

### View the logs of an execution

You can view the logs of an execution to better understand the execution process. The logs can help you identify and troubleshoot issues.

**Procedure**

1. Log on to the **Apsara Stack Operation Orchestration Service (OOS) console** .
2. In the left-side navigation pane, click **Task Execution Management**. On the page that
appears, find the execution that you want to manage and click **Details** in the Actions column.
3. On the page that appears, click the **Log** tab in the output section to view the logs of the
execution.

### Status transition diagram

The initial state of an execution is Started. The execution may go through multiple states before it enters a final state. The following figure shows the status transition process of an execution.

**States**

| Running | Running | The execution is running. |
|---|---|---|
| Success | Success | The execution is complete, and the result is successful. |
| Failed | Failed | The execution is complete, but the result indicates a failure. |
| Canceled | Canceled | The execution is canceled. |
| Waiting | Waiting | The execution is waiting for inputs from external systems. If a trigger action is defined in the template based on which the execution is created, the execution is in the Waiting state before the execution is triggered. For example, if the ACS::TimerTrigger action is defined in the template, the execution is in the Waiting state before the specified point in time arrives. If the ACS::Approve action is defined in the template based on which the execution is created, the execution is in the Waiting state before the execution is approved by a user who has the permissions to approve the execution. |

Operation Orchestration Service
**Note** `Final states` include the Success, Failed, and Canceled states. In such states, the
execution is complete, and no subsequent execution is performed.
