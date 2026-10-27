---
title: "Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service Operations and Maintenance Guide 20241107"
product_version: "V3.18.3"
doc_version: "20241107"
pdf_pages: 18
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service Operations and Maintenance Guide 20241107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E8%BF%90%E7%BB%B4%E7%BC%96%E6%8E%92OSS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Operation%20Orchestration%20Service%20Operations%20and%20Maintenance%20Guide%2020241107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Operation Orchestration Service Operations and Maintenance Guide 20241107

## Table of Contents

- 1 Overview
- 2 Create a template
- 3 Create an execution
- 4 Manage multiple instances at a time
- 5 Start or shut down ECS instances at a scheduled time
- 6 Temporarily upgrade the bandwidth of ECS instances
- 7 Create or update an image
- 8 Perform scheduled O&M
- 9 FAQ

## 1 Overview

This topic describes how to quickly create and execute an Operation Orchestration Service (OOS) template. To create and execute an OOS template, perform the following steps: For more information, see Create a template. Create an execution based on the created template and start the execution. For more information, see Create an execution.

## 2 Create a template

This topic describes how to create an Operation Orchestration Service (OOS) template for querying the IDs of Elastic Compute Service (ECS) instances in the specified state, such as Running or Stopped, within the current account. The template assumes the OOSServiceRole role to call the DescribeInstances operation of ECS and automatically goes through the results to return the IDs of ECS instances in the specified state. If no more than 1,000 ECS instances are in the specified state, the IDs of all these ECS instances are returned. If more than 1,000 ECS instances are in the specified state, the IDs of the first 1,000 ECS instances in the specified state are returned. For more information, see Limits.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Custom Template**. On the page that appears, click
**Create Template**.
3. In the Basic Information section of the Create Template page, configure the basic
information of the template.
4. Configure the **Template Name** parameter. In this example, DescribeInstances is used.
5. On the **YAML** tab, enter the following sample template. You can modify this template to
add multiple tasks and call API operations.

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

4. Click **Create Template**.

## 3 Create an execution

After you create a template, you can create an execution based on the template and start the execution.

**Procedure**

1. Log on to the **Apsara Stack Operation Orchestration Service (OOS) console** .
2. In the left-side navigation pane, click **Custom Template**. On the page that appears, find
the DescribeInstances template that you created and click **Create Execution** in the Actions column.
3. In the **Create Task** wizard, configure the parameters in the **Basic Information** step. In
this example, the **Execution Mode** parameter is set to **Automatic**. The following table describes the parameters.

| Parameter or value | Description |
|---|---|
| Execution Mode | Automatic: After the execution is created, the execution automatically starts. Manual: After the execution is created, you must manually start the execution. |
| Suspend upon Failure | If the execution contains a loop task and a subtask fails, the execution is suspended, and you must manually adjust the subtask and decide whether to continue the execution. |
| Template Category | Public Template: the templates provided by OOS for common scenarios. Custom Template: the templates that you create based on your business requirements. |
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
a time

## 4 Manage multiple instances at a time

**at a time**

**Background information**

Operation Orchestration Service (OOS) allows you to perform an operation on multiple Elastic Compute Service (ECS) instances at a time. OOS supports the following batch operations on multiple instances: **sending remote commands**, **performing basic O&M operations**, and
**modifying instance attributes**. The supported remote commands include shell commands
in Linux and Bat and PowerShell commands in Windows. The supported basic O&M operations include starting, stopping, and restarting ECS instances, and initializing and replacing the system disks of ECS instances. The attributes that can be modified for multiple instances include the instance name, hostname, and instance description.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Common O&M Tasks**. In the left-side pane, click
**Batch Instance Operations**. On the page that appears, click Create.
3. In the **Select Task Type** section, select a task type. You can select **Send Remote**
**Commands** or **Instance Operations**. In this example, **Send Remote Commands** is
selected as the task type. The Command Type parameter is set to **Linux Shell**, and the df h command is entered.
4. In the **Select Instances** section, select instances. Instance selection methods include
**Manually Select Instances**, **Specify Instance Tags**, **Specify Resource Group**, and
**Upload CSV File**. In this example, **Specify Instance Tags** is selected.
5. In the **Advanced** section, configure advanced settings. Select **Automatic** or **Suspend**
**upon Failure** as **Execution Mode**. Configure the **Concurrency** and **Error Threshold**
parameters. You can select **Concurrency-based Control** or **Batch-based Control** as
**Rate control type**. In this example, **Concurrency-based Control** is selected.
6. Click **Create**.
7. On the **Task Execution Management** page, find the execution that you created. If the
execution is created and in the Running state, the command is being run.
8. When the state of the execution changes to Success, the command is successfully run.
9. To view more information about the execution, click **Details** in the Actions column. On the
page that appears, click the **Log** tab in the output section to view the logs of the execution. ces at a scheduled time

## 5 Start or shut down ECS instances at a scheduled time

**instances at a scheduled**

**time**

**Background information**

You can use the Scheduled Startup/Shutdown feature of Operation Orchestration Service (OOS) to start or shut down multiple Elastic Compute Service (ECS) instances at a scheduled time. You can run a scheduled startup and shutdown task every day or on the specified days of each week.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Common O&M Tasks**. In the left-side pane, click
**Scheduled Startup/Shutdown**. On the page that appears, click Create.
3. In the **Select Task Type** section, configure the **Task Name**, Execution Cycle, Task Type,
**Time Zone**, **Startup Time**, **Shutdown Time**, and End Time parameters.The duration
between the startup time and the shutdown time must be at least 10 minutes.
4. Configure the **Stop Mode** parameter.
5. Turn on or off **Hibernate Instance**. A hibernated instance is different from a stopped
instance. A hibernated instance automatically restores the applications on the instance to the original status before hibernation when the instance is awoken. This allows the instance to resume the provision of services in a short period of time. For more information about the limits of hibernation, see ECS documentation.
6. Set the **Permissions** parameter to **Specify RAM Role and Use Permissions Granted to**
**This Role** and select a Resource Access Management (RAM) role from the drop-down list.
In this example, **OOSServiceRole** is selected. If no RAM roles are available, create a RAM role for OOS. For more information, see Use RAM to grant permissions to OOS. If you know how to grant permissions to OOS by using RAM, you can click **View Authorization**
**Policies** and **Manual Authorization** to create a RAM role for OOS and grant permissions
to the RAM role in the RAM console.
7. In the **Select Instances** section, select **Specify Instance Tags** and specify tags. Instance
selection methods include **Manually Select Instances** and **Specify Instance Tags**. In this example, **Specify Instance Tags** is selected. Enter the preset tag keys and tag values.
8. In the **Advanced** section, configure advanced settings. Configure the **Concurrency** and
**Error Threshold** parameters. You can select **Concurrency-based Control** or **Batch-**
**based Control** as **Rate control type**. In this example, **Concurrency-based Control** is
selected.
9. Click **Create**. In the message that appears, confirm the parameters and click OK.
0. On the **Task Execution Management** page, find the execution that you created. If the
execution is created and in the Waiting state, the scheduled startup and shutdown task is created.
1. When the scheduled startup time or shutdown time is reached, the state of the execution
changes to Running and the specified ECS instances automatically start or shut down.
2. To view more information about the execution, click **Details** in the Actions column. On the
page that appears, click the **Log** tab in the output section to view the logs of the execution. width of ECS instances

## 6 Temporarily upgrade the bandwidth of ECS instances

**bandwidth of ECS instances**

This topic describes how to use Operation Orchestration Service (OOS) to temporarily upgrade the bandwidth of Elastic Compute Service (ECS) instances at a scheduled time.

**Background information**

If you want to temporarily upgrade the bandwidth of ECS instances, you can use the Temporary Bandwidth Upgrade feature of OOS to specify the upgrade time. You can run a temporary bandwidth upgrade task every day or on the specified days of each week. After you configure the parameters on the Create Task Temporary Bandwidth Upgrade page, you can view the bandwidth fee for a single cycle in the lower-right corner of the page.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Common O&M Tasks**. In the left-side pane, click
**Temporary Bandwidth Upgrade**.
3. On the page that appears, click **Create**.
4. In the **Parameter Settings** section, configure the parameters.
5. Select **Daily** or **Select Time** as **Execution Cycle**. In this example, **Daily** is selected.
6. Configure the **Start Time**, **Execution Duration (Hours)**, **Maximum Internet Outbound**
**Bandwidth (Mbit/s)**, and **End Time** parameters.
7. Set the **Permissions** parameter to **Specify RAM Role and Use Permissions Granted to**
**This Role** and select a Resource Access Management (RAM) role from the drop-down list.
In this example, **OOSServiceRole** is selected. If no RAM roles are available, create a RAM role for OOS. For more information, see Grant RAM permissions for OOS. If you know how to grant permissions to OOS by using RAM, you can click **View Authorization Policies** and
**Manual Authorization** to create a RAM role for OOS and grant permissions to the RAM
role in the RAM console. For more information about the required policy, see the following JSON script: width of ECS instances

```json
    "Version": "1",
```

`{`

```json
            "Action": "oos:*",
            "Resource": "*",
            "Effect": "Allow"
```

`},` `{`

```json
            "Action": "ram:PassRole",
            "Resource": "*",
            "Effect": "Allow",
            "Condition": {
                "StringEquals": {
                    "acs:Service": "oos.aliyuncs.com"
```

`}` `}` `},` `{`

```json
            "Action": [
                "ecs:DescribeInstances",
                "ecs:ModifyInstanceNetworkSpec"
```

`],`

```json
            "Resource": "*",
            "Effect": "Allow"
```

`}` `]` `}`
8. In the **Select Instances** section, select **Manually Select Instances** and select one or
more ECS instances for which you want to temporarily upgrade the bandwidth. Instance selection methods include **Manually Select Instances**, **Specify Instance Tags**, and
**Specify Resource Group**.
9. In the Advanced section, configure advanced settings.Configure the **Concurrency and**
**Error Threshold** parameters. For more information about concurrency-related terms, see
Loop. You can select **Concurrency-based Control** or **Batch-based Control** as **Rate**
**control type**. In this example, **Concurrency-based Control** is selected.
0. View the bandwidth fee in the lower-right corner of the page and click **Create**.

## 7 Create or update an image

This topic describes how to use Operation Orchestration Service (OOS) to create or update an image for an Elastic Compute Service (ECS) instance.

**Background information**

You may often need to update the software of your ECS instances, such as updating the backend service version or installing security patches. You can use the Create or Update Images feature of OOS to facilitate software updates. OOS allows you to create an image from an existing ECS instance or update an image.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Common O&M Tasks**. In the left-side pane, click
**Create or Update Images**. On the page that appears, click Create.
3. In the **General Settings** section, configure general settings.
4. Select **Create Image from Existing Instance** or **Update Image**. In this example, **Create**
**Image from Existing Instance** is selected.
5. Configure the **New Image Name** parameter.
6. Set the Permissions parameter to Use Existing Permissions of Current Account or Specify
RAM Role and Use Permissions Granted to This Role. In this example, Specify RAM Role and Use Permissions Granted to This Role is selected and OOSServiceRole is selected as the Resource Access Management (RAM) role assumed by OOS. If no RAM roles are available, create a RAM role for OOS. For more information, see Grant RAM permissions for OOS. If you know how to grant permissions to OOS by using RAM, you can click View Authorization Policies and Manual Authorization to create a RAM role for OOS and grant permissions to the RAM role in the RAM console. For more information about the required policy, see the following JSON script. Policy for creating an image from an existing ECS instance and policy for updating an image:

```json
  "Version": "1",
```

`{`

```json
      "Action": [
        "ecs:CreateImage",
        "ecs:DescribeImages",
        "ecs:ModifyImageSharePermission",
        "ecs:CopyImage",
        "ecs:RunCommand",
        "ecs:DescribeInvocationResults",
        "ecs:DescribeRegions",
        "ecs:DescribeInstances",
        "ecs:DescribeInvocations"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "ess:ModifyScalingConfiguration"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": "oos:*",
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": "ram:PassRole",
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "acs:Service": "oos.aliyuncs.com"
```

`}` `}` `}` `]` `}`

```json
  "Version": "1",
```

`{`

```json
      "Action": "oos:*",
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": "ram:PassRole",
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "acs:Service": "oos.aliyuncs.com"
```

`}` `}` `},` `{`

```json
      "Action": [
        "ecs:RunCommand",
        "ecs:RunInstances",
        "ecs:StopInstance",
        "ecs:DescribeRegions",
        "ecs:DeleteInstance",
        "ecs:CreateImage",
        "ecs:DescribeImages",
        "ecs:ModifyImageSharePermission",
        "ecs:CopyImage",
        "ecs:RebootInstance",
        "ecs:DescribeInvocationResults",
        "ecs:InstallCloudAssistant",
        "ecs:DescribeCloudAssistantStatus",
        "ecs:DescribeInstances",
        "ecs:DescribeInvocations"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "ess:ModifyScalingConfiguration"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`}` `]` `}`
7. In the **Select Instances** section, select an ECS instance.
8. In the **Send Remote Commands** section, configure the Command Type parameter. In this
example, **Linux Shell** is selected.
9. Click **Create**.
0. On the **Task Execution Management** page, find the execution that you created. If the
execution is created and in the Running state, an image is being created or updated.
1. To view more information about the execution, click **Details** in the Actions column. On the
page that appears, click the **Log** tab in the output section to view the logs of the execution.

## 8 Perform scheduled O&M

**Background information**

If you want to perform O&M operations at a specific point in time, you can use the **Scheduled**
**O&M** feature of Operation Orchestration Service (OOS). OOS allows you to run a scheduled
O&M task once at the specified time or periodically.

**Procedure**

1. Log on to the Apsara Stack OOS console.
2. In the left-side navigation pane, click **Scheduled O&M**. On the page that appears, click
Create.
3. In the Set Scheduled Task section, configure the **Scheduled Task Type** parameter. You
can select **Executed Once at the Specified Time** or **Executed Periodically**. In this example, **Executed Once at the Specified Time** is selected. Then, configure the
**Execution Duration** parameter.
4. In the **Select Template** section, select a template. You can select **Public Template** or **My**
**Template**. In this example, **Public Template** is selected.
5. In the **Configure Template Parameters** section, configure the template parameters.
6. Click **Create**.
7. On the **Task Execution Management** page, find the execution that you created. If the
execution is created and in the Waiting state, the scheduled O&M task is created.
8. To view more information about the execution, click **Details** in the Actions column. On the
page that appears, click the **Log** tab in the output section to view the logs of the execution.

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

Cause: The RAM user is not allowed to use OOS as the specified RAM role because the RAM user does not have the PassRole permission. Solution: Log on to the **RAM console** with an Apsara Stack tenant account or an administrator account. Grant the PassRole permission to the RAM user. For more information, see **Access control**.

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
