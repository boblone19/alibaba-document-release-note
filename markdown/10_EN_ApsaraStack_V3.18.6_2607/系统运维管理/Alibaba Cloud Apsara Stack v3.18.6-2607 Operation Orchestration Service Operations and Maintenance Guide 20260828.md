---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 37
source_pdf: "85c28a40ea11f1ef_Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Operations and Maintenance G"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E7%B3%BB%E7%BB%9F%E8%BF%90%E7%BB%B4%E7%AE%A1%E7%90%86/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Operation%20Orchestration%20Service%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Overview
- 2 Create a template
- 3 Create an execution
- 4 Release multiple ECS instances at a time
- 5 Configure a scheduled task to automatically restart ECS instances
- 6 Use DingTalk to approve automated O&M tasks
- 7 Perform a phased release based on commands
- 8 Update an image by using OOS
- 9 FAQ

## 1 Overview

This topic describes how to quickly create and execute an Operation Orchestration Service (OOS) template. To create and execute an OOS template, perform the following steps: For more information, see Create a template. Create an execution based on the created template and start the execution. For more information, see Create an execution.

## 2 Create a template

This topic describes how to create a template to query the IDs of Elastic Compute Service (ECS) instances in the specified state, such as Running or Stopped, within the current account. The created template calls the DescribeInstances operation and automatically goes through the results to return the IDs of ECS instances in the specified state. If no more than 1,000 ECS instances are in the specified state, the IDs of all these ECS instances are returned. If more than 1,000 ECS instances are in the specified state, the IDs of the first 1,000 ECS instances in the specified state are returned. For more information, see Limits.

**Procedure**

1. Log in to the Apsara Stack CloudOps Orchestration Service (OOS) console.
2. In the left-side navigation pane, click Custom Template. On the page that appears, click
**Create Template**.
3. In the Basic Information section of the Create Template page, configure the template
parameters.
4. Enter a **template name**. In this example, DescribeInstances is used.
5. Click the **YAML** tab and enter the following sample code. You can modify the code to add
tasks to call other API operations.

```
---
 Description: DescribeInstances
 FormatVersion: OOS-2019-06-01
 Parameters:
     Status:
         Description: Running or Stopped
         Type: String
 Tasks:
   - Name: describeInstances
     Action: ACS::ExecuteAPI
     Properties:
         Service: ECS
         API: DescribeInstances
         Parameters:
             Status: "{{ Status }}"
     Outputs:
         InstanceIds:
             Type: List
             ValueSelector: .Instances.Instance[].InstanceId
 Outputs:
     InstanceIds:
         Type: List
         Value: "{{ describeInstances.InstanceIds }}"
```

6. Click **Create Template**.

## 3 Create an execution

After you create a template, you can create an execution based on the template and start the execution.

**Procedure**

1. Log in to the **OOS console**.
2. In the left-side navigation pane, click **Task Execution Management**. On the page that
appears, click **Create**.
3. On the **Create** page, configure the parameters in the **Basic Information** step. In this
example, the **Execution Mode** parameter is set to **Automatic**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Execution Mode | Automatic: After the execution is created, the execution automatically starts. Manual: After the execution is created, you must manually start the execution. |
| Suspend upon Failure | If the execution contains a loop task and a subtask fails, the execution is suspended. In this case, you must manually adjust the subtask and decide whether to continue the execution. |
| Template Category | Public Template: the templates that are provided by OOS for common scenarios. Custom Template: the templates that you create based on your business requirements. |
| Template | Select the template that you created. |

4. Click **Next Step: Parameter Settings**. In the Parameter Settings step, configure the
parameters. In this example, the **Status** parameter is set to **Stopped**.
5. Click **Next Step: OK**.
6. Click **Create**.
7. Go to the **Task Execution Management** page and view the execution that you created.
If you set the execution mode to **Automatic**, the execution automatically starts. After the execution is complete, check whether the value in the **Execution Status** column becomes
**Success**.
If you set the execution mode to **Manual**, you must manually start the execution.
8. To view the execution details, click the execution ID or click **Details** in the **Actions** column.
s at a time

## 4 Release multiple ECS instances at a time

**instances at a time**

CloudOps Orchestration Service (OOS) provides public templates for automatically releasing multiple Elastic Compute Service (ECS) instances at a time. To automatically release ECS instances, you can create an execution based on the template and specify the IDs of the ECS instances to be released for the execution. This topic describes the templates for automatically releasing multiple ECS instances at a time and how to release multiple pay-asyou-go ECS instances at a time by using a template.

**Prerequisites**

The ECS instances to be released are **pay-as-you-go** instances.

**Procedure**

1. Log in to the OOS console.
2. In the left-side navigation pane, click **Public Template**.
3. On the Public Template page, search for the ACS-ECS-BulkyDeleteInstances template that
is used to release pay-as-you-go ECS instances.
4. Click **Create Execution**.
5. On the Create page, configure the parameters in the Basic Information step
Configure the **Execution Description**, **Organization**, and **Resource Set** parameters based on your business requirements. The other parameters are automatically configured by the system. s at a time
6. Click **Next Step: Parameter Settings**.
7. In the Parameter Settings step, configure the parameters.
Configure the parameters to execute the ACS-ECS-BulkyDeleteInstances template.

| Parameter | Description |
|---|---|
| Force | Specifies whether to forcibly stop and release running ECS instances. |
| Select Instances | The method used to select the ECS instances to be released. You can manually select instances, specify instance tags, or select all instances. |
| RateControl | You can configure the following parameters: Execution Mode: the execution mode. Valid values: Concurrency-based Control and Batch-based Control. Concurrency: the number or percentage of the tasks to be concurrently run. Error Threshold: the maximum number of errors that can occur before the task stops. Enter a number or percentage. Default value: 0, which specifies that the task stops when an error occurs. If you set the percentage to 100%, the task runs until it is complete, regardless of how many errors occur. |

s at a time

| OOSAssumeRole | Use Existing Permissions of Current Account: This is the default value. OOS has all the permissions granted to your account. Make sure that your account has the permissions to call the ECS API operations that are used to create custom images. Specify RAM Role and Use Permissions Granted to This Role: If a Resource Access Management (RAM) role is specified, OOS assumes the RAM role to execute O&M tasks. |
|---|---|

8. Click **Next Step: OK**.
9. In the OK step, click **Create**.
s at a time
0. On the **Task Execution Management** page, view the created execution. If the execution
is in the Running state, the specified instances are being released.
1. On the task execution details page, click the **Advanced View** tab and view the execution
process on the **Graphical Template** tab. When the state of the execution changes to Success, all specified instances are released. s at a time
2. Check whether all specified instances are released.

**Public templates**

**ACS-ECS-BulkyDeleteInstances**

The template executes the following tasks in sequence:
1. Query ECS instances by ID or tag.
2. Release all specified ECS instances at a time.

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky delete ECS postpaid instances.
  zh-cn: the description in Chinese
  name-en: ACS-ECS-BulkyDeleteInstances
  name-zh-cn: the description in Chinese
  categories:
    - instance_manage
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  force:
    Description:
      en: Whether to force the release of a running instance.
      zh-cn: the description in Chinese
    Type: Boolean
    Default: false
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
      zh-cn: the description in Chinese
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 10
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
      zh-cn: the description in Chinese
    Type: String
    Default: OOSServiceRole
```

s at a time

```
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
      zh-cn: description in Chinese
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
  - Name: deleteInstance
    Action: 'ACS::ExecuteAPI'
    Description:
      en: Deletes ECS instance with the specified instance ID.
      zh-cn: the description in Chinese
    Properties:
      Service: ECS
      API: DeleteInstance
      Parameters:
        InstanceId: '{{ ACS::TaskLoopItem }}'
        Force: '{{ force }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
```

**ACS-ECS-BulkyDeletePrepaidInstances**

The template executes the following tasks in sequence:
1. Query ECS instances by ID or tag.
2. Change the billing method of subscription instances to pay-as-you-go.
3. Release all specified ECS instances at a time.

```
FormatVersion: OOS-2019-06-01 Description:
  en: >-
    Bulky delete prepaid instances.The specified ECS instances must be in
    stopped status.
  zh-cn: the description in Chinese
  name-en: ACS-ECS-BulkyDeletePrepaidInstances
  zh-cn: the description in Chinese
  categories:
    - instance_manage
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
```

s at a time

```
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
      zh-cn: the description in Chinese
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 10
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
      zh-cn: the description in Chinese
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
      zh-cn: description in Chinese
    Action: 'ACS::SelectTargets'
    Properties:
      ResourceType: 'ALIYUN::ECS::Instance'
      Filters:
        - '{{ targets }}'
    Outputs:
      instanceIds:
        Type: List
        ValueSelector: 'Instances.Instance[].InstanceId'
  - Name: modifyInstanceChargeType
    Action: 'ACS::ExecuteAPI'
    Description:
      en: Modify the charge type for prepaid instances to postpaid.
      zh-cn: the description in Chinese
    Properties:
      Service: ECS
      API: ModifyInstanceChargeType
      Parameters:
        InstanceIds: '{{ getInstance.instanceIds }}'
        InstanceChargeType: PostPaid
  - Name: deleteInstance
    Action: 'ACS::ECS::DeleteInstance'
    Description:
      en: Deletes the ECS instance by instance ID.
      zh-cn: the description in Chinese
    Properties:
      instanceId: '{{ ACS::TaskLoopItem }}'
    Loop:
      RateControl: '{{ rateControl }}'
      Items: '{{ getInstance.instanceIds }}'
```

automatically restart ECS instanc es

## 5 Configure a scheduled task to automatically restart ECS instances

**to automatically restart ECS**

**instances**

This topic describes how to configure a scheduled task to automatically restart Elastic Compute Service (ECS) instances to maintain system stability and security in various scenarios. This helps system administrators simplify maintenance processes, improve system stability, optimize user experience, and enhance system security and compliance.

**Background information**

Server stability is crucial in various business scenarios such as e-commerce, online education, gaming, and streaming media. However, you may encounter the following issues in actual scenarios: System updates: Some operating system or software updates may require a server restart to take effect. In this case, you can restart the server on a regular basis to ensure that the updates are applied as expected. Memory leaks: Some programs use a large amount of memory resources in the server after they run for an extended period of time. This degrades the server performance. In this case, you can restart the server on a regular basis to release the memory. High-load operation: Potential issues may occur if your server runs under a high load condition for an extended period of time. In this case, you can restart the server on a regular basis to prevent these issues. Cached data: Some applications may generate a large amount of cached data. In this case, you can restart the server on a regular basis to clear the cached data and free up the storage space. Security risks: You can restart the server on a regular basis to disrupt the detection and attacks by hackers on your system. This reduces the risks of server attacks. Excessive log files: Some programs generate log files on a regular basis. If you run the programs for an extended period of time, the generated log files may occupy a large amount of disk space. You can restart the server on a regular basis to clear the log files. To resolve the preceding issues, you can use CloudOps Orchestration Service (OOS) to create scheduled O&M tasks to automatically restart your ECS instances. When you configure a scheduled O&M task, evaluate the impacts of the restart on your business and set the restart time to off-peak hours. Otherwise, your business may be affected.

**Procedure**

1. Log in to the OOS console.
2. In the left-side navigation pane, click **Scheduled O&M**. On the **Scheduled O&M** page,
click **Create**. automatically restart ECS instanc es
3. On the Create Scheduled O&M Task page, set the Scheduled Task Type parameter to
Executed Periodically.
4. Select the ACS-ECS-BulkyRebootInstances template, and then configure the parameters to
create an execution. mated O&M tasks

## 6 Use DingTalk to approve automated O&M tasks

**automated O&M tasks**

This topic describes how to use the O&M approval feature of CloudOps Orchestration Service (OOS).

**Background information**

In automated O&M, fully automated high-risk or high-cost operations, such as deleting core resources, starting high-specification instances, and restarting multiple production servers at a time, may cause uncontrolled risk escalation. However, if you do not automate the operations and manually perform them instead, the consistency and traceability of the automated processes will be compromised. To resolve this issue, OOS embeds a manual approval step in automated processes. This ensures that critical operations are subject to manual approvals while retaining the efficiency improvement provided by automated processes.

**Solution**

When the ACS::Approve action is to be executed in a template, OOS suspends the subsequent operations. OOS sets the execution state to Waiting and sends a notification that contains an approval link to the administrator. After the administrator receives the notification, the administrator can approve or reject the operation based on the business requirements. If the operation is approved, OOS continues to perform the subsequent operations. If the operation is rejected, OOS stops the execution and sets the execution state to Canceled.

**Procedure**

1. Log in to the OOS console.
2. In the left-side navigation pane, click **Custom Template**.
3. On the Custom Template page, click **Create Template**.
4. On the Create Template page, configure the parameters in the **Basic Information** section.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Template Name | The template name. The name can be up to 128 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). It cannot start with _ ALIYUN, ACS, ALIBABA, or ALICLOUD. |
| Organization | The organization to which the template belongs. |

mated O&M tasks

| Resource Set | The resource set to which the template belongs. |
|---|---|
| Version Description | The version description of the template. |

5. Click the **YAML** tab and paste the template content in the **Appendix 1: Template for**
**approving restart of ECS instances** section of this topic to the code editor.
6. Click **Create Template**.
7. On the **Custom Template** page, find the created template and click **Create Execution** in
the **Actions** column.
8. On the Create page, configure the parameters in the Basic Information step.
Configure the Organization, Resource Set, and Execution Description parameters. The system automatically configures other parameters.
9. Click **Next Step: Parameter Settings**.
0. In the Parameter Settings step, configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| targets | Yes | The Elastic Compute Service (ECS) instances to be restarted. |

mated O&M tasks

| webHookUrl | Yes | The webhook URL of the DingTalk group assistant for receiving the approval notifications and links. For more information about how to obtain the webhook URL, see the Appendix 2: Obtain the webhook URL section of this topic. |
|---|---|---|
| rateControl | No | The concurrency and error threshold. |
| atMobiles | No | The users to be reminded when an approval notification is sent to the DingTalk group. |
| atAll | No | Specifies whether to remind all group members when an approval notification is sent to the DingTalk group. |
| OOSAssumeRole | No | The Resource Access Management (RAM) role to be assumed by OOS. By default, OOS uses the permissions granted to the current account. If a RAM role is specified, OOS assumes this role to execute O&M tasks. |

1. Click **Next Step: OK**.
2. In the OK step, click **Create**.
3. On the **Task Execution Management** page, view the created execution. If the execution
is created and an operation needs to be approved, OOS suspends the execution, sends an approval notification to the specified DingTalk group, and notifies the specified users in the group. The specified users can click the approval link to approve or reject the operation based on the business requirements.

**Appendix 1: Template for approving restart of ECS instances**

The template executes the following tasks in sequence: i. Query the information about the ECS instances to be restarted. ii. Send a notification that contains an approval link to notify the specified users of approving restart of the ECS instances. mated O&M tasks iii. Restart the ECS instances if the restart request is approved. The following code provides a sample template in the YAML format:

```
FormatVersion: OOS-2019-06-01 Description:
  en: Bulky restarts the ECS instances with Approval.
  zh-cn: the description in Chinese
  name-en: BulkyRebootInstancesWithApproval
  zh-cn: the description in Chinese
Parameters:
  targets:
    Type: Json
    AssociationProperty: Targets
    AssociationPropertyMetadata:
      ResourceType: 'ALIYUN::ECS::Instance'
  rateControl:
    Description:
      en: Concurrency ratio of task execution.
      zh-cn: the description in Chinese
    Type: Json
    AssociationProperty: RateControl
    Default:
      Mode: Concurrency
      MaxErrors: 0
      Concurrency: 100%
  webHookUrl:
    Description:
      en: >-
        The webHook url of dingtalk group assistant,
        e.g.https://oapi.dingtalk.com/robot/send?access_token=1234zxcvaksdq31414.
      zh-cn: >-
        the description in Chinese
    Type: String
  atMobiles:
    Description:
      en: >-
        The telephone numbers of member in dingtalk group assistant @, when
        notify comes.
      zh-cn: the description in Chinese
    Type: List
    Default:
      - '12345678901'
  atAll:
    Description:
      en: 'assistant @ all members in dingtalk group or not, when notify comes.'
      zh-cn: the description in Chinese
    Type: String
    Default: 'false'
  OOSAssumeRole:
    Description:
      en: The RAM role to be assumed by OOS.
      zh-cn: the description in Chinese
    Type: String
    Default: OOSServiceRole
```

mated O&M tasks

```
RamRole: '{{ OOSAssumeRole }}' Tasks:
  - Name: getInstance
    Description:
      en: Views the ECS instances.
      zh-cn: description in Chinese
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
    Action: 'ACS::Approve'
    Properties:
      NotifyType: WebHook
      WebHook:
        URI: '{{webhookUrl}}'
        Headers:
          Content-Type: application/json
        Content:
          msgtype: text
          text:
            content: >-
              Notify: please approve instances restart, instance names to
              approve  are {{getInstance.instanceNames}}, sent by
              {{ACS::RegionId}} oos {{ACS::ExecutionId}}.
          at:
            atMobiles: '{{atMobiles}}'
            isAtAll: '{{atAll}}'
  - Name: rebootInstance
    Action: 'ACS::ECS::RebootInstance'
    Description:
      en: Restarts the ECS instances.
      zh-cn: the description in Chinese
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

**Appendix 2: Obtain the webhook URL**

mated O&M tasks
1. Log in to DingTalk. Go to the DingTalk group for receiving approval notifications and click
the icon in the upper-right corner.
2. In the Group Settings panel, click **Group Assistant**.
3. In the Group Assistant panel, click **Add Robot**.
4. Click **Custom**.
mated O&M tasks
5. In the Robot details dialog box, click **Add**.
mated O&M tasks
6. In the Add Robot dialog box, configure the **Chatbot name** and Security Settings
parameters. In this example, **Custom Keywords** is selected for **Security Settings**. Set keywords for the DingTalk chatbot by using words in the notification. In this example, the notification content in the sample template contains the word "Notify". Therefore, you can set "Notify" as a keyword for the DingTalk chatbot. Then, click **Finished**.
7. In the Add Robot dialog box, click **Copy** to copy the webhook URL.
ed on commands

## 7 Perform a phased release based on commands

**based on commands**

**Scenario**

In daily O&M, you may need to frequently perform the following operations: Perform rolling deployment for or update versions of online applications. Install multiple security patches for operating systems or software. Ideally, these operations can be performed as expected on all specified machines. In practice, if scripts contain defects, required dependencies are missing, or scripts are executed in different environments, all instances may simultaneously fail, resulting in a large-scale service interruption. CloudOps Orchestration Service (OOS) aims to avoid this risk. Therefore, OOS adopts a rolling update execution policy. OOS divides the specified machines into multiple batches, executes tasks in batches, and verifies the results of each batch. This limits the impact scope of failures, improves change stability, and ensures that changes can be rolled back. Traditional solutions typically rely on self-developed scripts, in combination with tools such as `pssh` or `Ansible` , to perform remote execution. However, in most cases, such solutions require significant additional development to implement fine-grained batch control, execution status visualization, and automatic suspension upon failures. In addition, the processes are opaque and difficult to audit, which makes it challenging to meet the security, compliance, and observability requirements of enterprise-grade O&M.

**Solution**

OOS can execute tasks in batches and monitors the status of each batch throughout the process. OOS provides the Fail Fast with Pause capability: If any instance in a batch fails to be released, OOS immediately suspends the subsequent tasks of the batch and automatically prevents the subsequent batches from starting. You can use the OOS console or call API operations to view the complete execution process, task status, and detailed logs at any time. This helps you quickly identify causes of failures. After an issue is analyzed, you can flexibly make a decision: continue to execute the subsequent batches after the issue is fixed or terminate the release process. This mechanism prevents interruptions of all services due to minor issues (over-conservative) and prevents further execution in case of serious faults (uncontrolled risk escalation). It enables a controllable release process in which risks can be detected and operations can be rolled back.

**Procedure**

1. Log in to the OOS console.
2. In the left-side navigation pane, click **Public Template**.
3. On the Public Template page, find the **ACS-ECS-BulkyRunCommand** template.
4. Click **Create Execution**.
5. On the Create page, configure the **Organization** and **Resource Set** parameters in the
Basic Information step.
6. Click **Next Step: Parameter Settings**.
7. In the Parameter Settings step, configure the parameters.
ed on commands i. In the **run command options** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| CommandType | The type of the command to be run. Valid values: Run Shell Script Run Python Script Run Perl Script Run BAT Script Run PowerShell Script |
| CommandContent | The command to be run. |
| WorkingDir | The directory in which the command is run. For Linux ECS instances, the working directory is the /root home directory of the root user. For Windows instances, the working directory is the directory in which the Cloud Assistant client process resides. Example: C:\Windows\System32. |
| Timeout | The timeout period for command execution. |

ii. In the **Select Ecs Instances** section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region | The ID of the region in which the instances reside. |
| TargetInstance | The method used to select instances. Valid values: Manually Select Instances Specify Instance Tags Select All |

ed on commands iii. In the Control Options section, configure the parameters that are described in the following table.

| Parameter |   | Description |
|---|---|---|
| RateControl | Execution Mode | The execution mode. Valid values: Concurrency-based Control Batch-based Control |
|   | Concurrency | This parameter is available only when you set the Execution Mode parameter to Concurrency-based Control. Specify a number or percentage of tasks to be concurrently run. |
|   | Batch Array | This parameter is available only when you set the Execution Mode parameter to Batch-based Control. You can run tasks in multiple batches for an execution. A new batch of tasks does not run until the previous batch of tasks is complete. You can specify an array that consists of numbers or percentages to specify batches. For example, [1, 5%, 10%] specifies that 1 task is run in the first batch, 5% of the tasks in the execution are run in the second batch, and 10% of the tasks in the execution are run in the third batch. |
|   | Concurrency- based Control | This parameter is available only when you set the Execution Mode parameter to Batch-based Control. Valid values: Automatic Suspend Each Batch Suspend First Batch |
|   | Error Threshold | Specifies the maximum number of errors that can occur before the task stops. Enter a number or percentage. Default value: 0, which specifies that the task stops when an error occurs. If you set the percentage to 100%, the task runs until it is complete, regardless of how many errors occur. |
| OOSAssumeRole |   | Valid values: Use Existing Permissions of Current Account Specify RAM Role and Use Permissions Granted to This Role |

ed on commands
8. Click **Next Step: OK**.
9. In the OK step, click **Create**.
S

## 8 Update an image by using OOS

**OOS**

**Background information**

You may frequently update your custom images for security reasons in the following scenarios: Regularly install the latest patches for your operating system. Update middleware software. Reinstall the latest third-party software in images. To update an existing image, you need to perform the following four steps:
1. Create an Elastic Compute Service (ECS) instance from the existing image.
2. Log in to the ECS instance and perform operations such as updating software.
3. Create a new image based on the updated ECS instance.
4. Release the ECS instance.
The preceding procedure is time-consuming and error-prone.

**Solution**

CloudOps Orchestration Service (OOS) provides a public template for updating custom images. After you create an execution based on the template, OOS automatically updates your custom images. To update a custom image by using OOS, you need to only select a
**source image** to be updated, specify the required parameters such as the shell command
for updating a Linux instance image, and then click **Create Execution**. No extra tools are required to update images by using OOS. In addition, you do not need to manually create, log in to, modify, or release ECS instances, or configure environment variables or AccessKey pairs. OOS also allows you to create custom templates to schedule automatic image updates or update multiple images at a time.

**Procedure**

1. Log in to the OOS console.
2. In the left-side navigation pane, click **Public Template**. The Public Template page
appears.
3. On the Public Template page, find the **ACS-ECS-UpdateImage** template and click **Create**
**Execution**.
S
4. On the Create page, configure the **Organization** and **Resource Set** parameters in the
Basic Information step.
5. Click **Next Step: Parameter Settings**.
6. In the Parameter Settings step, configure the following parameters:
**targetImageName**: the name of the new image.
**sourceImageId**: the ID of the source image to be updated. You can select a public
image, a custom image, or a shared image.
**instanceType**: the type of the temporary ECS instance that is used for the image
update.
**commandType**: the type of the Cloud Assistant commands to be run. Cloud Assistant
supports the following three types of commands: RunShellScript (shell commands for Linux ECS instances), RunBatScript (batch commands for Windows ECS instances), and RunPowerShellScript (PowerShell commands for Windows ECS instances).
**commandContent**: the Cloud Assistant commands to be run on the temporary ECS
instance for updating the image. For more information about the Cloud Assistant commands, see the overview of Cloud Assistant in ECS documentation. S
**OOSAssumeRole**: the Resource Access Management (RAM) role to be assumed by OOS
for the image update. By default, OOS uses the permissions granted to the current account. If a RAM role is specified, OOS assumes this role to execute O&M tasks.
7. Click **Next Step: OK**.
8. In the OK step, click **Create**.
9. On the **Task Execution Management** page, view the created execution. If the execution
is in the Running state, the image update is in progress.
0. Wait until the state of the execution changes to Success. When the state of the execution
changes to Success, the image is updated. You can click Details in the Actions column corresponding to the execution to go to the execution details page and then view the ID of the new image in the **Output Parameters** section of the **Basic Information** tab.
1. View the execution status and progress.
i. After the execution is created, find the execution and click **Details** in the Actions column. ii. On the execution details page, click the **Advanced View** tab. S iii. On the Advanced View tab, click the **Execution Logs** tab to view the real-time execution progress and status.

**Public template**

The public template ACS-ECS-UpdateImage contains the following code:

```
FormatVersion: OOS-2019-06-01 Description: Updates an existing ECS image via ECS Cloud Assistant then creates a
  ECS image.
Parameters:
  sourceImageId:
    Description: The image ID for the ECS instances,
centos_6_10_64_20G_alibase_20190326.vhd,
      for example.
    Type: String
    AllowedPattern: '[A-Za-z0-9_\-\.]*'
    MinLength: 1
    MaxLength: 40
  instanceType:
    Description: The instance type for the ECS instances, ecs.g5.large, for example.
    Type: String
    AllowedPattern: ecs\.[A-Za-z0-9\.\-]*
    MinLength: 1
    MaxLength: 30
  securityGroupId:
    Description: The security group ID for the ECS instances, sg-xxxxxxxxxxxxxxxxxxxx,
      for example.
    Type: String
    AllowedPattern: sg-[A-Za-z0-9]*
    MinLength: 1
    MaxLength: 30
  vSwitchId:
    Description: The virtual switch ID for the ECS instances, vsw-xxxxxxxxxxxxxxxxxxxx,
```

`f` `l` S

```
      for example.
    Type: String
    AllowedPattern: vsw-[A-Za-z0-9]*
    MinLength: 1
    MaxLength: 30
  commandContent:
    Description: The content of command.
    Type: String
  commandType:
    Description: The type of command to run in ECS instance.
    Type: String
    AllowedValues:
    - RunBatScript
    - RunPowerShellScript
    - RunShellScript
    MinLength: 1
    MaxLength: 30
  targetImageName:
    Description: The name of image.
    Type: String
    AllowedPattern: '[A-Za-z0-9\-_]*'
    MinLength: 1
    MaxLength: 30
  OOSAssumeRole:
    Description: The RAM role to be assumed by OOS.
    Type: String
    Default: OOSServiceRole
RamRole: '{{ OOSAssumeRole }}' Tasks:
- Name: checkNewImageName
  Action: ACS::CheckFor
  Description: Check image name is available.
  Properties:
    Service: ECS
    API: DescribeImages
    Parameters:
      ImageName: '{{ targetImageName }}'
    DesiredValues:
    PropertySelector: TotalCount
- Name: runInstances
  Action: ACS::ECS::RunInstances
  Description: Create a ECS instance for the cloud assistant.
  Properties:
    imageId: '{{ sourceImageId }}'
    instanceType: '{{ instanceType }}'
    securityGroupId: '{{ securityGroupId }}'
    vSwitchId: '{{ vSwitchId }}'
  Outputs:
    instanceId:
      ValueSelector: instanceIds[0]
      Type: String
- Name: installCloudAssistant
  Action: ACS::ECS::InstallCloudAssistant
Description:InstallcloudassostantforECSinstance
```

S

```
  Description: Install cloud assostant for ECS instance.
  OnError: deleteInstance
  Properties:
    instanceId: '{{ runInstances.instanceId }}'
- Name: runCommand
  Action: ACS::ECS::RunCommand
  Description: Run command on ECS instance.
  OnError: deleteInstance
  Properties:
    commandContent: '{{ commandContent }}'
    commandType: '{{ commandType }}'
    instanceId: '{{ runInstances.instanceId }}'
- Name: stopInstance
  Action: ACS::ECS::StopInstance
  Description: Stops the ECS instance by the instance ID.
  Properties:
    instanceId: '{{ runInstances.instanceId }}'
- Name: createImage
  Action: ACS::ECS::CreateImage
  Description: Create image with the specified image name and instance ID.
  OnError: deleteInstance
  Properties:
    imageName: '{{ targetImageName }}'
    instanceId: '{{ runInstances.instanceId }}'
  Outputs:
    imageId:
      ValueSelector: imageId
      Type: String
- Name: deleteInstance
  Action: ACS::ExecuteAPI
  Description: Deletes the ECS instance by the instance ID.
  Properties:
    Service: ECS
    API: DeleteInstance
    Risk: Normal
    Parameters:
      InstanceId: '{{ runInstances.instanceId }}'
      Force: true
Outputs:
  imageId:
    Type: String
    Value: '{{ createImage.imageId }}'
```

The template executes the following tasks in sequence:
1. Check whether the name of the new image is valid.
2. Create a temporary ECS instance. The instance is created based on the source image that
you provide and configured parameters. This indicates that the image used by the instance is the source image that you want to update, and the instance attributes are defined based on the configured parameters.
3. Install the Cloud Assistant client on the temporary ECS instance if the client is not installed.
4. Run the Cloud Assistant commands for the image update on the temporary ECS instance
and wait until the commands are run. S
5. Stop the temporary ECS instance.
6. Create an image for the temporary ECS instance and wait until the creation is complete.
7. Release the temporary ECS instance.

**Appendix 2: Comparison of different methods for updating**

**images**

The following table describes and compares various methods that Alibaba Cloud supports for updating images.

| Method | Requirement | Advantage | Disadvantage |
|---|---|---|---|
| Update an image by using OOS | You need to only activate OOS. No other tool is required. | This method is secure, reliable, and officially recommended. The operations are performed online. No installation is required. OOS provides a public template with built-in code. No AccessKey pair is required. OOS allows you to create and use custom templates. OOS provides a visualized execution process. OOS supports batch and scheduled operations. | None |
| Create a custom image by using a snapshot Create a custom image by using an ECS instance | No other tool is required. | This method provides easy and convenient operations in the ECS console. | You need to manually create instances and snapshots. The procedure is complicated, error- prone, and inefficient. |
| Create a custom image by using Packer | Packer must be installed. | Packer is an open source tool that is supported by various cloud service providers. | You need to install and maintain Packer. You need to write code. |

## 9 FAQ

This topic provides answers to frequently asked questions about Operation Orchestration Service (OOS). Why is the following error message returned when I use OOS as a RAM user: User has no permission to do the action: (ListTemplates)? Why is the following error message returned when I use OOS as a RAM user: User has no permission to do the action: (PassRole)? Why is the following error message returned when I use a template: Assumes role failed. Code: EntityNotExist.Role, msg: The role not exists: acs:111111:role/OOSServiceRole? Why is the following error message returned when I use a template: Assumes role failed. Code: NoPermission, msg: You are not authorized to do this action. You should be authorized by RAM?

**Why is the following error message returned when I use OOS**

**as a RAM user: User has no permission to do the action:**

**(ListTemplates)?**

Cause: The Resource Access Management (RAM) user does not have the permissions to call the specified API operation of OOS. Solution: Log on to the **RAM console** with an Apsara Stack tenant account or an administrator account. Authorize the RAM user to call the specified API operation or all API operations of OOS. For example, configure `"Action": "oos:*"` to authorize the RAM user to call all API operations of OOS. For more information, see **Access control**. `{`

```json
  "Statement": [
```

`{`

```json
          "Effect": "Allow",
          "Action": "oos:*",
          "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}`

**Why is the following error message returned when I use OOS**

**as a RAM user: User has no permission to do the action:**

**(PassRole)?**

Cause: The RAM user is not allowed to use OOS as the specified RAM role because the RAM user does not have the PassRole permission. Solution: Log on to the **RAM console** with an Apsara Stack tenant account or an administrator account. Grant the PassRole permission to the RAM user. For more information, see **Access control**. `{`

```json
  "Statement": [
```

`{`

```json
          "Effect": "Allow",
          "Action": "oos:*",
          "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}`

**Why is the following error message returned when I use a**

**template: Assumes role failed. Code: EntityNotExist.Role, msg:**

**The role not exists: acs:111111:role/OOSServiceRole?**

Cause: You have not created a default RAM role for your OOS service to access your Apsara Stack resources. Solution: Log on to the **RAM console** with an Apsara Stack tenant account or an administrator account. Create the default RAM role OOSServiceRole for your OOS service. For more information, see **Grant RAM permissions to OOS** .

**Why is the following error message returned when I use a**

**template: Assumes role failed. Code: NoPermission, msg: You**

**are not authorized to do this action. You should be authorized**

**by RAM?**

Cause: You have not attached the required trust policy to the RAM role OOSServiceRole for your OOS service. Solution: Log on to the **RAM console** with an Apsara Stack tenant account or an administrator account. Attach the required trust policy to the RAM role OOSServiceRole assumed by your OOS service. For more information, see **Grant RAM permissions to OOS** .
1. Log on to the **RAM console**. In the left-side navigation pane, choose Identities > Roles. On
the Roles page, enter OOSServiceRole in the search box to search for the role.
2. Click the role name to go to the details page of the role. Click the Trust Policy Management
tab.
3. Modify the trust policy of the role.Replace the trust policy with the following content:
`{`

```json
  "Statement": [
```

`{`

```json
          "Action": "sts:AssumeRole",
          "Effect": "Allow",
          "Principal": {
              "Service": [
                  "oos.aliyuncs.com"
```

`]` `}` `}` `],`

```json
  "Version": "1"
```

`}`
