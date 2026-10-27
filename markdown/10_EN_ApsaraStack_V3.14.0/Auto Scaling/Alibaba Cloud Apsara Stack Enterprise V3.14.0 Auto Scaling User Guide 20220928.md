---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Auto Scaling User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 53
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Auto Scaling User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Auto%20Scaling%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Auto Scaling User Guide 20220928

## Table of Contents

- 1 What is Auto Scaling?
- 2 Notes
  - 2.1 Precautions
  - 2.2 Manual intervention
  - 2.3 Limits
  - 2.4 Scaling group status
  - 2.5 Scaling processes
  - 2.6 Remove unhealthy ECS instances
  - 2.7 Instance rollback after a failed scaling activity
  - 2.8 Instance lifecycle management
- 3 Quick start
  - 3.1 Overview
  - 3.2 Log on to the Auto Scaling console
  - 3.3 Create a scaling group
  - 3.4 Create a scaling configuration
  - 3.5 Enable a scaling group
  - 3.6 Create a scaling rule
  - 3.7 Create a scheduled task
  - 3.8 Create an event-triggered task
- 4 Scaling groups
  - 4.1 Create a scaling group
  - 4.2 Enable a scaling group
  - 4.3 View scaling groups
  - 4.4 Modify a scaling group
  - 4.5 Disable a scaling group
  - 4.6 Delete a scaling group
  - 4.7 Query ECS instances
  - 4.8 Put an ECS instance into the Standby state
  - 4.9 Remove an ECS instance from the Standby state
  - 4.10 Put an ECS instance into the Protected state
  - 4.11 Remove an ECS instance from the Protected state
- 5 Scaling configurations
  - 5.1 Create a scaling configuration
  - 5.2 View scaling configurations
  - 5.3 Modify a scaling configuration
  - 5.4 Apply a scaling configuration
  - 5.5 Delete a scaling configuration
- 6 Scaling rules
  - 6.1 Create a scaling rule
  - 6.2 View scaling rules
  - 6.3 Modify a scaling rule
  - 6.4 Delete a scaling rule
- 7 Scaling tasks
  - 7.1 Manually execute a scaling rule
  - 7.2 Manually add an ECS instance
  - 7.3 Manually remove an ECS instance
- 8 Scheduled tasks
  - 8.1 Create a scheduled task
  - 8.2 View scheduled tasks
  - 8.3 Modify a scheduled task
  - 8.4 Disable a scheduled task
  - 8.5 Enable a scheduled task
  - 8.6 Delete a scheduled task
- 9 Event-triggered tasks
  - 9.1 Create an event-triggered task
  - 9.2 View event-triggered tasks
  - 9.3 Modify an event-triggered task
  - 9.4 Disable an event-triggered task
  - 9.5 Enable an event-triggered task
  - 9.6 Delete an event-triggered task

## 1 What is Auto Scaling?

Auto Scaling is a management service that automatically adjusts your elastic computing resources based on your business needs and policies. When business loads increase, Auto Scaling automatically adds ECS instances based on user-defined scaling rules to ensure sufficient computing capabilities. When business loads decrease, Auto Scaling automatically removes ECS instances to save costs. Auto Scaling provides the following features: Scale-out When business loads surge above normal loads, Auto Scaling automatically increases underlying resources. This helps maintain access speed and ensures that resources are not overloaded. For example, if the CPU utilization of ECS instances exceeds 80%, Auto Scaling scales out ECS resources based on your configured rules. During the scale-out event, Auto Scaling automatically creates and adds ECS instances to a scaling group, and adds the new instances to the backend server groups of the associated SLB instances and the whitelists of the associated ApsaraDB RDS instances. The following figure shows the implementation of a scale-out event. Scale-in When your business loads decrease, Auto Scaling automatically releases underlying resources to prevent resource wastage and reduce costs. For example, if the CPU utilization of ECS instances in a scaling group is less than 30%, Auto Scaling automatically scales in ECS instances based on your configured rules. During the scale-in event, Auto Scaling removes ECS instances from the scaling group and also from the backend server groups of the associated SLB instances as well as the whitelists of the associated ApsaraDB RDS instances. The following figure shows the implementation of a scale-in event. Elastic recovery If ECS instances in a scaling group are not in the Running state, Auto Scaling considers the instances to be unhealthy. If an ECS instance is considered unhealthy, Auto Scaling automatically releases the instance and creates a new one. This process is called elastic recovery. It ensures that the number of healthy ECS instances in a scaling group does not fall below the minimum number of ECS instances that you specified for the scaling group. The following figure shows the implementation of elastic recovery.

## 2 Notes

### 2.1 Precautions

This topic describes the precautions when you use Auto Scaling (ESS). Scaling rules ESS uses scaling rules to scale ECS instances in a scaling group based on the minimum and maximum numbers of ECS instances specified for the scaling group. Assume that a scaling group can contain up to 45 ECS instances. If you configure a scaling rule to increase the number of ECS instances in the scaling group to 50, ESS only increases the number of ECS instances to 45 at most. Scaling activities Only one scaling activity can be executed at a time in a scaling group. An ongoing scaling activity cannot be terminated. For example, if a scaling activity is being executed to create 20 ECS instances but only five have been created, you cannot forcibly terminate the scaling activity. If some ECS instances fail to be added to a scaling group during a scaling activity, ESS considers that the scaling activity is complete without trying to add the failed instances to the scaling group. ESS rolls back the ECS instances that fails to be added but not the scaling activity. For example, if ESS has created 20 ECS instances for a scaling group, and 19 of the instances are added to SLB instances, only the one ECS instance that failed to be added is automatically released. Cooldown period During the cooldown period, if you manually execute a scaling task, such as a scaling rule or scheduled task, the task is immediately executed without waiting for the cooldown period to expire. The cooldown period starts after the last ECS instance is added to or removed from a scaling group during a scaling activity.

### 2.2 Manual intervention

If you manually intervene with Auto Scaling operations, Auto Scaling processes the intervention accordingly. Auto Scaling does not prevent you from performing manual intervention, such as deleting automatically created ECS instances in the ECS console. The following table describes how Auto Scaling processes manual intervention.

| Resource | Manual intervention type | Processing method |
|---|---|---|

| Resource | Manual intervention type | Processing method |
|---|---|---|
| ECS | A user deletes an ECS instance from a scaling group by using the ECS console or calling API operations. | Auto Scaling performs health checks to determine whether the ECS instance is unhealthy. If the instance is unhealthy, Auto Scaling removes it from the scaling group. The internal IP address of the ECS instance is not automatically deleted from the whitelist of the associated ApsaraDB RDS (RDS) instance. If the total number of ECS instances in the scaling group falls below the lower limit after the ECS instance is removed, the scaling group automatically creates an ECS instance to ensure that the number of instances reaches the lower limit. |
| ECS | A user revokes the ECS API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests. |
| SLB | A user manually removes an ECS instance from an SLB instance by using the SLB console or calling API operations. | Auto Scaling does not automatically detect this action or handle such exceptions. The ECS instance remains in the scaling group. When a scale-in event is triggered, Auto Scaling releases the ECS instance if the instance meets the removal policy. |
| SLB | A user manually deletes an SLB instance or disables the health check feature for an SLB instance by using the SLB console or calling API operations. | Auto Scaling does not add ECS instances to scaling groups that are associated with this SLB instance. Auto Scaling removes ECS instances from the scaling groups if a scaling task triggers a scale-in rule or the ECS instances are recognized as unhealthy after a health check is performed. |
| SLB | An SLB instance is unavailable because of system-related reasons. | All scaling activities fail except for instance removal tasks that are manually executed. |
| SLB | A user revokes the SLB API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests for scaling groups with which SLB instances are associated. |
| RDS | A user manually removes the IP address of an ECS instance from the whitelist of the associated RDS instance by using the RDS console or calling API operations. | Auto Scaling does not automatically detect this action or handle such exceptions. The ECS instance remains in the scaling group. When a scale-in event is triggered, Auto Scaling releases the ECS instance if the instance meets the removal policy. |

| Resource | Manual intervention type | Processing method |
|---|---|---|
| RDS | A user manually deletes an RDS instance by using the RDS console or calling API operations. | Auto Scaling does not add ECS instances that are associated with this RDS instance to scaling groups. Auto Scaling removes ECS instances from the scaling groups if a scaling task triggers a scale-in rule or the ECS instances are recognized as unhealthy after a health check is performed. |
| RDS | An RDS instance is unavailable because of system-related reasons. | All scaling activities fail except for instance removal tasks that are manually executed. |
| RDS | A user revokes the RDS API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests for the scaling groups associated with RDS instances. |

### 2.3 Limits

This topic describes the limits of ESS. ESS does not support vertical scaling. It can only scale the number of ECS instances. The CPU, memory, and bandwidth configurations of ECS instances cannot be automatically adjusted. The following table describes the quantity limits that are applied to a scaling group.

| Item | Quota |
|---|---|
| Scaling configuration | You can create a maximum of 10 scaling configurations for a scaling group. |
| Scaling rule | You can create a maximum of 50 scaling rules for a scaling group. |
| ECS instance | A scaling group can contain a maximum of 1,000 ECS instances. |

### 2.4 Scaling group status

This topic describes the states of a scaling group in the console and in an API operation.

| State in the console | State in an API operation |
|---|---|
| Creating | Inactive |
| Created | Inactive |
| Enabling | Inactive |
| Enabled | Active |
| Disabling | Inactive |
| Disabled | Inactive |

| User Guide·Notes | Auto Scalin |
|---|---|
| State in the console | State in an API operation |
| Deleting | Deleting |

### 2.5 Scaling processes

Before you use Auto Scaling, you must understand the processes related to scaling activities. Automatic scaling of a scaling group Automatic scale-out i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. Create ECS instances. iv. Modify Total Capacity. v. Assign IP addresses to the created ECS instances. vi. Add the ECS instances to the whitelist of the associated ApsaraDB RDS instance. vii. Start the ECS instances. viii. Associate the ECS instances with an SLB instance and set the weight to the SLB weight value that is specified when the scaling configuration is created. ix. The cooldown period starts after the scaling activity is complete. Automatic scale-in i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. Remove ECS instances from the associated SLB instance. iv. Stop the ECS instances. v. Remove the ECS instances from the whitelist of the associated ApsaraDB RDS instance. vi. Release the ECS instances. vii. Modify Total Capacity. viii. The cooldown period starts after the scaling activity is complete. Manually add or remove existing ECS instances Manually add instances i. Check the health status and boundary conditions of the scaling group, and check the status and type of ECS instances. ii. Assign the activity ID and execute the scaling activity. iii. Add the ECS instances. iv. Modify Total Capacity. v. Add the ECS instances to the whitelist of the associated ApsaraDB RDS instance. vi. Associate the ECS instances with an SLB instance and set the weight to the SLB weight value that is specified in the active scaling configuration. Not e If you want to manually add an instance to a scaling group, the instance type of the instance must be the same as that specified in the active scaling configuration of the scaling group. Therefore, you must set the weight to the SLB weight value that is specified in the active scaling configuration. vii. The cooldown period starts after the scaling activity is complete. Manually remove instances i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. SLB stops forwarding traffic to ECS instances. iv. Remove the ECS instances from SLB after 60 seconds. v. Remove the ECS instances from the whitelist of the associated ApsaraDB RDS instance. vi. Modify Total Capacity. vii. Remove the ECS instances from the scaling group. viii. After the scaling activity is complete, the cooldown period starts.

### 2.6 Remove unhealthy ECS instances

Before you use ESS, you must understand information about the removal of unhealthy ECS instances. After an ECS instance is added to a scaling group, ESS checks the status of the instance on a regular basis. If the ECS instance is not in the Running state, ESS removes the ECS instance from the scaling group. The removal method depends on how the ECS instance is added: If an ECS instance is automatically created, ESS immediately removes and releases it. If an ECS instance is manually added, ESS immediately removes it, but does not stop or release it. The removal of unhealthy ECS instances is not limited by the MinSize value. After the unhealthy ECS instances are removed, the number of ECS instances (Total Capacity) may fall below the MinSize value. In this case, ESS automatically creates ECS instances based on the difference between the actual instance number and MinSize value to ensure that the total number of ECS instances is equal to the MinSize value.

### 2.7 Instance rollback after a failed scaling activity

scaling activity Before you use ESS, you must understand the mechanism of instance rollback after a failed scaling activity. If some ECS instances fail to be added to a scaling group during a scaling activity, ESS considers that the scaling activity is complete without trying to add the failed instances to the scaling group. ESS rolls back ECS instances, not the scaling activity. For example, if a scaling group has created 20 ECS instances, and 19 of the instances are added to SLB instances, only the one ECS instance that failed to be added is automatically released.

### 2.8 Instance lifecycle management

Before you use Auto Scaling (ESS), you must understand concepts related to the instance lifecycle. Automatically created ECS instances ECS instances are automatically created by ESS based on user-defined scaling configurations and rules. ESS manages the entire lifecycle of automatically created ECS instances. ESS creates ECS instances during scale-out events, and stops and releases them during scale-in events. Manually added ECS instances ECS instances are manually added to a scaling group. ESS does not manage the entire lifecycle of manually added ECS instances. These instances are not automatically created by ESS, but are manually added by a user to a scaling group. If the ECS instances are manually or automatically removed from the scaling group, ESS removes the instances but does not stop or release them. Instance status An ECS instance in a scaling group goes through the following states during its lifecycle: Pending: The ECS instance is being added to the scaling group. The instance is being created, added to an SLB instance, or added to the whitelist of the associated ApsaraDB RDS instance. InService: The ECS instance is added to the scaling group and is providing services normally. Removing: The ECS instance is being removed from the scaling group. Instance health status An ECS instance in a scaling group has the following health states: Healthy Unhealthy If an ECS instance is not in the Running state, ESS considers the instance to be unhealthy and automatically removes it from the scaling group. ESS stops and releases automatically created ECS instances. ESS does not stop or release manually added ECS instances.

## 3 Quick start

### 3.1 Overview

This topic describes how to create a scaling group and how to add or remove ECS instances. You can perform the following steps to create a scaling group, and add or remove ECS instances. Set the parameters for the scaling group, such as the Maximum Capacity and Minimum Capacity of ECS instances. Set the parameters for the scaling configuration, such as Instance Type and Image. Enable the scaling group after creating the scaling configuration. Specify how to add or remove ECS instances. For example, add an ECS instance to a scaling group. Create scheduled tasks to add or remove instances at a specified time point. Auto Scaling executes the scheduled tasks and scaling rules at the specified time. For example, Auto Scaling can trigger a task to execute a specific scaling rule at 08:00 everyday.

### 3.2 Log on to the Auto Scaling console

console This topic describes how to log on to the Auto Scaling console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Aut o Scaling.

### 3.3 Create a scaling group

This topic describes how to create a scaling group. A scaling group is a group of Elastic Compute Service (ECS) instances that is dynamically scaled based on the configured scenario. You can specify the minimum and maximum numbers of ECS instances in a scaling group. Prerequisites A virtual private cloud (VPC) and a vSwitch are created. For more information, see Create a VPC and Create a vSwitch in VPC User Guide. To associate a scaling group with Server Load Balancer (SLB) instances, make sure that the following requirements are met: You have one or more SLB instances in the Running state. The SLB instances and the scaling group are in the same organization, resource set, and region. To associate a scaling group with ApsaraDB RDS instances, make sure that the following requirements are met: You have one or more RDS instances in the Running state. The RDS instances and the scaling group are in the same organization, resource set, and region. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click Scaling groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Scaling Groups page, click Creat e Scaling Group.
5. Configure parameters for the scaling group.

| Parameter | Required | Description |
|---|---|---|
| Scaling Group | Yes | The name of the scaling group. It must be 2 to 64 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must _ start with a letter or a digit. |

| Parameter | Required | Description |
|---|---|---|
| Organization/Resourc e Group | Yes | The organization and resource set in which to create the scaling group. |
| Maximum Capacity | Yes | The maximum number of instances that the scaling group can contain. Set the value based on your business requirements to control costs. Valid values: 0 to 1000. |
| Minimum Capacity | Yes | The minimum number of instances that a scaling group must contain. Set the value based on your business requirements to ensure service availability. When the scaling group is enabled, Auto Scaling automatically creates this number of ECS instances. Valid values: 0 to 1000. |
| Cooldown (Seconds) | Yes | The period of time after each scaling activity is complete. During the cooldown time, Auto Scaling rejects all scaling activity requests triggered by event-triggered tasks from CloudMonitor. However, scaling activities triggered by other types of tasks such as manually triggered tasks and scheduled tasks are not limited by the cooldown time and are immediately executed. The value must be an integer that is greater than or equal to zero. Unit: seconds. |

| Parameter | Required | Description |
|---|---|---|
| Scale-In Policy | No | The policy for automatically removing ECS instances from the scaling group. This parameter contains the Select and From t he list , select fields. You cannot specify the same values for the two fields. Valid values: Earliest Inst ance Creat ed Using Scaling Conf igurat ion: filters instances that were created based on the earliest scaling configuration. Earliest Creat ed Inst ance: filters instances that were added to the scaling group at the earliest point in time. Newest Inst ances: filters instances that were most recently added to the scaling group. None: is available only for From t he list , select . This value indicates that Auto Scaling does not filter instances based on the From the list, select field. For example, if Auto Scaling filters instances based on the Earliest Creat ed Inst ance value of Select, you can select one of the following values for From the list, select: None: indicates that Auto Scaling does not filter instances based on the From the list, select field. Newest Inst ances: filters instances obtained based on the Select field and then filters instances that were most recently added to the scaling group. |
| Region/VPC | Yes | The region and VPC in which to create the scaling group. |
| Vswitch | Yes | The ID of the vSwitch with which to associate the scaling group. |

| Parameter | Required | Description |
|---|---|---|
| Associate SLB Instance | No | After you associate SLB instances with the scaling group, ECS instances that are added to the scaling group are automatically added as SLB backend servers. You can specify a server group to which to add the ECS instances. ECS instances can be added to the following types of server groups: Default server group: the group of ECS instances that are used to receive requests. If the listener is not configured with a vServer group or a primary/secondary server group, requests are forwarded to the ECS instances in the default server group. vServer group: If you want to distribute different requests to different backend servers or configure domain name- or URL-based routing methods, you can use vServer groups. |
| Associate RDS Instance | No | After you associate RDS instances with the scaling group, the internal IP addresses of ECS instances that are added to the scaling group are automatically added to the whitelists of the RDS instances to allow communication over the internal network. |

6. Click OK.
Result The created scaling group is displayed in the scaling group list but is in the Disabled state. To enable the scaling group, you must create a scaling configuration. For more information, see Create a scaling configuration.

### 3.4 Create a scaling configuration

This topic describes how to create a scaling configuration for a scaling group. Prerequisites At least one security group is available. If you do not have any security groups, create a security group. For more information, see Create a security group in ECS User Guide. Context You can create only a limited number of scaling configurations for a scaling group. For more information, see the Limits topic in Auto Scaling Product Introduction. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. Choose Creat e > Creat e Scaling Conf igurat ion.
6. Configure parameters for the scaling configuration.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Region | Yes | The region where the ECS instance is located. |
|   | Zone | Yes | The zone where the ECS instance is located. |
| Security Group | Security Group | Yes | The security group to which the ECS instance belongs. |
| Instance | Instance Family | Yes | The instance family to which the ECS instance belongs. |
|   | Instance Type | Yes | The instance type of the ECS instance. |
| Image | Image Type | Yes | Public Image: Public images provided by Alibaba Cloud are fully licensed to offer a secure and stable operating environment for applications on ECS instances. Cust om Image: You can create custom images to install software or deploy projects that have special requirements. |
| Storage | System Disk | Yes | Specify the category and size of the system disk. The operating system is installed on the system disk. You can select Ult ra Disk or St andard SSD. |

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Data Disk | No | Specify the category and size of the data disk. You can select Ult ra Disk or St andard SSD. You can add a maximum of 16 data disks. The maximum capacity of each data disk is 32 TiB. You can set Release wit h Inst ance and Encrypt for each data disk. |
| Password | Set Password | Yes | Select when to set password. You can select Now or Lat er. If you select Later, you can use the Change Password feature in the console to set the password. For more information, see the Change Password topic in ECS User Gui de. |
|   | Logon Password | No | The password used to log on to the ECS instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: digits, uppercase letters, lowercase letters, and special characters. Not e The password is used to log on to the operating system and is not the VNC password. |
|   | Confirm Password | No | Enter the password again. |
| Deployment Set | Deployment Set | No | The deployment set to which the instance belongs. |
| Instance Name | Configuration Name | No | The name of the scaling configuration. |
|   | Instance Name | No | The name of the ECS instance. |

| Guide·Quick start |   |   |   |
|---|---|---|---|
|   | Auto Scalin |   |   |
| Section | Parameter | Required | Description |
| User Data | User Data | No | Windows supports two formats: Bat and Powershell. Before you perform Base64 encoding, make sure to include [bat] or [powershell] as the first line. You can run shell scripts for Linux ECS instances. |
| Quantity | Quantity | No | The number of instances to purchase. |

|   |   | [bat] |
|---|---|---|

7. Click Submit .
Result After the scaling configuration is created, it is in the Disabled state and is displayed in your scaling configuration list. To automatically create ECS instances, you must apply a scaling configuration. For more information, see Apply a scaling configuration.

### 3.5 Enable a scaling group

This topic describes how to enable a scaling group. You can enable a scaling group to trigger scaling activities. Prerequisites The scaling group is in the Disabled state. The scaling group has a scaling configuration that is in the Enable state. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the scaling group that you want to enable and click Enable in the Act ions column.
4. In the message that appears, click OK.
Result The status of the scaling group is changed from Disabled to Enable in the St at us column.

### 3.6 Create a scaling rule

This topic describes how to create a scaling rule. You can create scaling rules to add or remove ECS instances. For example, you can add an ECS instance to a scaling group. Context You can create only a limited number of scaling rules for a scaling group. For more information, see the Limits topic in Auto Scaling Product Introduction. After a scaling rule is executed, the resulting number of ECS instances in the scaling group may fall outside of the specified range. In this case, Auto Scaling automatically adjusts the number of ECS instances to ensure that the number of ECS instances in the scaling group is within the specified range. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. Click Creat e Scaling Rule.
6. Configure parameters for the scaling rule.

| Parameter | Required | Description |
|---|---|---|
| Rule Name | Yes | The name of the scaling rule. It must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods _ (.). It must start with a letter or digit. |
| Scaling Activity | Yes | The operation that is performed when the scaling rule is triggered. The operations include: Change t o N inst ances: After the scaling rule is executed, the number of instances in the scaling group is changed to N. Add N inst ances: After the scaling rule is executed, N instances are added to the scaling group. Remove N inst ances: After the scaling rule is executed, N instances are removed from the scaling group. |
| Default Cooldown (Seconds) | No | The cooldown period. If this parameter is not specified, the default value is used. |

7. Click OK.

### 3.7 Create a scheduled task

This topic describes how to create a scheduled task to scale computing resources in response to predictable business changes in the future. Scheduled tasks enable the system to automatically obtain sufficient computing resources before business peaks and release idle computing resources after the business peaks. Context A scheduled task is preconfigured to execute the specified scaling rule at the specified time. When the specified time arrives, the scheduled task automatically scales computing resources. This allows you to reduce costs and meet business requirements. You can also specify recurring schedules for scheduled tasks if business changes are regular. If multiple scheduled tasks need to be executed in 1 minute, Auto Scaling executes the most recently created scheduled task. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Scheduled Tasks page, click Creat e Scheduled T ask.
5. In the dialog box that appears, configure parameters for the scheduled task.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the scheduled task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It _ must start with a letter or a digit. |
| Description | Yes | The description of the scheduled task. |
| Organization/Resou rce Group | Yes | The organization and resource set in which to create the scheduled task. |
| Start Time | Yes | The time to execute the scheduled task. |
| Scaling Rules | Yes | The scaling group to be monitored and the scaling rule to be executed. |
| Retry Interval (Seconds) | No | The period of time during which the system retires to execute the scheduled task. Unit: seconds. If a scaling activity fails to be executed at the specified time, Auto Scaling executes the scheduled task again within the period of time that is specified by the Retry Interval (Seconds) parameter. |
| Recurrence Settings (Advanced) | No | Specifies whether to execute the scheduled task on a recurring schedule. Select Recurrence Set t ings (Advanced) and set the Recurrence and Expire parameters. The valid values for Recurrence include Daily, Weekly, and Mont hly. |

6. Click OK.
Result The scheduled task that you created is displayed in the scheduled task list.

### 3.8 Create an event-triggered task

This topic describes how to create an event-triggered task associated with monitoring metrics in response to emergent or unpredictable business changes. After you create and enable an eventtriggered task, Auto Scaling collects data for the specified metric in real time and triggers an alert when the specified condition is met. Then, Auto Scaling executes the corresponding scaling rule to scale Elastic Compute Service (ECS) instances in the scaling group. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert T asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Event-Triggered Tasks page, click Creat e Alert .
5. In the dialog box that appears, configure parameters for the event-triggered task.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the event-triggered task. It must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must start _ with a letter or a digit. |
| Description | No | The description of the event-triggered task. |
| Organization/Res ource Group | Yes | The organization and resource set in which to create the event-triggered task. |
| Monitoring Metrics/Scaling Rule | Yes | The scaling group to be monitored and the scaling rule to be executed. |
| Monitoring Type | Yes | Syst em-Level Monit oring is selected by default. |
| Monitoring Metrics | Yes | The metrics that you want to monitor. Valid values: Average CPU Ut ilizat ion Memory Usage Out bound T raf f ic Inbound T raf f ic Average Syst em Load |
| Monitoring Period | Yes | The period during which data is aggregated and analyzed. The shorter the period, the higher the frequency that the alert is triggered. Unit: minutes. Valid values: 1 2 5 15 |

| Parameter | Required | Description |
|---|---|---|
| Statistic | Yes | The rule that determines whether to trigger an alert. Select Average, Max Capacit y, or Min Capacit y, and specify a threshold value. For example, to trigger an alert when the CPU utilization exceeds 80%, you can use one of the following methods to specify the trigger condition: Average: An alert is triggered when the average CPU utilization of all ECS instances in the scaling group exceeds 80%. Max Capacity: An alert is triggered when the highest CPU utilization among the ECS instances in the scaling group exceeds 80%. Min Capacity: An alert is triggered when the lowest CPU utilization among the ECS instances in the scaling group exceeds 80%. |
| Trigger After | Yes | The number of consecutive times that the threshold must be exceeded before the alert is triggered. Valid values: 1 2 3 5 |

6. Click OK.

## 4 Scaling groups

### 4.1 Create a scaling group

This topic describes how to create a scaling group. A scaling group is a group of Elastic Compute Service (ECS) instances that is dynamically scaled based on the configured scenario. You can specify the minimum and maximum numbers of ECS instances in a scaling group. Prerequisites A virtual private cloud (VPC) and a vSwitch are created. For more information, see Create a VPC and Create a vSwitch in VPC User Guide. To associate a scaling group with Server Load Balancer (SLB) instances, make sure that the following requirements are met: You have one or more SLB instances in the Running state. The SLB instances and the scaling group are in the same organization, resource set, and region. To associate a scaling group with ApsaraDB RDS instances, make sure that the following requirements are met: You have one or more RDS instances in the Running state. The RDS instances and the scaling group are in the same organization, resource set, and region. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click Scaling groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Scaling Groups page, click Creat e Scaling Group.
5. Configure parameters for the scaling group.

| Parameter | Required | Description |
|---|---|---|
| Scaling Group | Yes | The name of the scaling group. It must be 2 to 64 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must _ start with a letter or a digit. |
| Organization/Resourc e Group | Yes | The organization and resource set in which to create the scaling group. |
| Maximum Capacity | Yes | The maximum number of instances that the scaling group can contain. Set the value based on your business requirements to control costs. Valid values: 0 to 1000. |

| Parameter | Required | Description |
|---|---|---|
| Minimum Capacity | Yes | The minimum number of instances that a scaling group must contain. Set the value based on your business requirements to ensure service availability. When the scaling group is enabled, Auto Scaling automatically creates this number of ECS instances. Valid values: 0 to 1000. |
| Cooldown (Seconds) | Yes | The period of time after each scaling activity is complete. During the cooldown time, Auto Scaling rejects all scaling activity requests triggered by event-triggered tasks from CloudMonitor. However, scaling activities triggered by other types of tasks such as manually triggered tasks and scheduled tasks are not limited by the cooldown time and are immediately executed. The value must be an integer that is greater than or equal to zero. Unit: seconds. |
| Scale-In Policy | No | The policy for automatically removing ECS instances from the scaling group. This parameter contains the Select and From t he list , select fields. You cannot specify the same values for the two fields. Valid values: Earliest Inst ance Creat ed Using Scaling Conf igurat ion: filters instances that were created based on the earliest scaling configuration. Earliest Creat ed Inst ance: filters instances that were added to the scaling group at the earliest point in time. Newest Inst ances: filters instances that were most recently added to the scaling group. None: is available only for From t he list , select . This value indicates that Auto Scaling does not filter instances based on the From the list, select field. For example, if Auto Scaling filters instances based on the Earliest Creat ed Inst ance value of Select, you can select one of the following values for From the list, select: None: indicates that Auto Scaling does not filter instances based on the From the list, select field. Newest Inst ances: filters instances obtained based on the Select field and then filters instances that were most recently added to the scaling group. |

| Parameter | Required | Description |
|---|---|---|
| Region/VPC | Yes | The region and VPC in which to create the scaling group. |
| Vswitch | Yes | The ID of the vSwitch with which to associate the scaling group. |
| Associate SLB Instance | No | After you associate SLB instances with the scaling group, ECS instances that are added to the scaling group are automatically added as SLB backend servers. You can specify a server group to which to add the ECS instances. ECS instances can be added to the following types of server groups: Default server group: the group of ECS instances that are used to receive requests. If the listener is not configured with a vServer group or a primary/secondary server group, requests are forwarded to the ECS instances in the default server group. vServer group: If you want to distribute different requests to different backend servers or configure domain name- or URL-based routing methods, you can use vServer groups. |
| Associate RDS Instance | No | After you associate RDS instances with the scaling group, the internal IP addresses of ECS instances that are added to the scaling group are automatically added to the whitelists of the RDS instances to allow communication over the internal network. |

6. Click OK.
Result The created scaling group is displayed in the scaling group list but is in the Disabled state. To enable the scaling group, you must create a scaling configuration. For more information, see Create a scaling configuration.

### 4.2 Enable a scaling group

This topic describes how to enable a scaling group. You can enable a scaling group to trigger scaling activities. Prerequisites The scaling group is in the Disabled state. The scaling group has a scaling configuration that is in the Enable state.
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the scaling group that you want to enable and click Enable in the Act ions column.
4. In the message that appears, click OK.
Result The status of the scaling group is changed from Disabled to Enable in the St at us column.

### 4.3 View scaling groups

This topic describes how to view the scaling group list and the details of a specific scaling group. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
The scaling groups that correspond to the specified organization, resource set, and region are displayed.
3. Select a filter option, enter the corresponding information, and then click Search.
You can select multiple filter options to narrow down the search results.

| Option | Description |
|---|---|
| Scaling Group | Enter a scaling group name to search for the scaling group. |
| Scaling Group ID | Enter a scaling group ID to search for the scaling group. |

4. Click the name of the scaling group in the Scaling Group Name/ID column.
5. View the details of the specified scaling group.

| Parameter | Description |
|---|---|
| Basic Information | The configurations of the scaling group, such as the scaling group ID, scaling group name, total instances, minimum number of instances, maximum number of instances, and scale-in policy. |
| ECS Instances | The details of ECS instances, such as the list of automatically created ECS instances, the list of manually added ECS instances, and the number of ECS instances that are in service. |
| Scaling Activities | All the scaling activities that have been executed in the scaling group. |
| Scaling Configuration | The information of scaling configurations in the scaling group. |
| Scaling Rules | The information of scaling rules. |

### 4.4 Modify a scaling group

This topic describes how to modify a scaling group. You can modify the parameters of a specific scaling group, such as the minimum and maximum numbers of ECS instances. Context After you modify the minimum or maximum number of ECS instances that a scaling group can have, if the number of instances in the scaling group is outside this range, Auto Scaling automatically creates or removes ECS instances until the number of instances are within the range. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click Edit in the Act ions column.
4. Modify the parameters of the scaling group.
You can modify the scaling configuration and other parameters, but not the organization and resource set. For more information about other parameters, see Create a scaling group.
5. Click OK.

### 4.5 Disable a scaling group

This topic describes how to disable a scaling group. Prerequisites The scaling group does not have scaling activities in progress. The scaling group is in the Enable state. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click Disable in the Act ions column.
4. Click OK.
Result The status of the scaling group is changed from Enable to Disabled in the St at us column.

### 4.6 Delete a scaling group

This topic describes how to delete a scaling group. When you delete a scaling group, Auto Scaling removes and releases ECS instances that are automatically created, removes ECS instances that are manually added, and deletes the scaling configurations and rules in the scaling group. However, the scheduled tasks and event-triggered tasks that are associated with the scaling group are not deleted.
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click Delet e in the Act ions column.
4. Click OK.

### 4.7 Query ECS instances

You can query all ECS instances in a scaling group and their states. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click Scaling groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
5. In the left-side navigation pane, click ECS inst ances.
6. View the details of ECS instances.

| Category | Description |
|---|---|
| Automatically created ECS instances | The ECS instances that are automatically created based on the active scaling configuration when a scaling rule is triggered. |
| Manually added ECS instances | The ECS instances that are manually added to the specified scaling group. |
| The number of ECS instances in each state. | The following section describes the states: Total: all ECS instances in the scaling group In Service: the ECS instances that are in normal use On Standby: the ECS instances that are on standby Protected: the ECS instances that are protected Adding: the ECS instances that are being added to the scaling group Removing: the ECS instances that are being removed from the scaling group Not e The Disabled, Adding:wait, and Suspending states are unavailable. |

### 4.8 Put an ECS instance into the Standby state

Standby state This topic describes how to put an ECS instance into the Standby state. Auto Scaling does not perform health checks on or release ECS instances in the Standby state. Context After an ECS instance is put into the Standby state: The ECS instance stays in the Standby state until you change its status. Auto Scaling stops managing the lifecycle of the ECS instance. You must manually manage the lifecycle of the ECS instance. If a scale-in event is triggered, Auto Scaling will not remove the ECS instance. When the ECS instance is stopped or restarted, its health check status is not affected. To release the ECS instance, you must first remove it from the scaling group. If you delete the scaling group, the ECS instance is automatically put out of the Standby state and is released. You can also perform other operations on the ECS instance, such as stopping, restarting, changing the instance type of, or changing the operating system of the ECS instance. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Select the source of the ECS instance.
To select an automatically created ECS instance, click the Aut o Creat ed tab. To select a manually added ECS instance, click the Manually Added tab.
6. Find the target ECS instance and choose Act ions > Swit ch t o St andby in the Act ions column.
7. Click OK.

### 4.9 Remove an ECS instance from the Standby state

Standby state This topic describes how to remove an ECS instance from the Standby state. You can remove an instance from the Standby state to reuse it. Context After an ECS instance is removed from the Standby state: The ECS instance enters the In Service state. When the ECS instance is stopped or restarted, its health status is updated. Auto Scaling continues to manage the lifecycle of the ECS instance, and can remove the ECS instance from the scaling group during a scale-in event.
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Select the source of the ECS instance.
To select an automatically created ECS instance, click the Aut o Creat ed tab. To select a manually added ECS instance, click the Manually Added tab.
6. Find the target ECS instance and choose Act ions > Move Out Of St andby in the Act ions
column.
7. Click OK.

### 4.10 Put an ECS instance into the Protected state

Protected state This topic describes how to put an ECS instance into the Protected state. Auto Scaling does not perform health checks on or release ECS instances that are in the Protected state. Context After an ECS instance is put into the Protected state: The ECS instance stays in the Protected state until you change its status. If a scale-in event is triggered, Auto Scaling will not remove the ECS instance. To release the ECS instance, you must remove the ECS instance from the Protected state and then remove it from the scaling group. When the ECS instance is stopped or restarted, its health check status is not affected. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Select the source of the ECS instance.
To select an automatically created ECS instance, click the Aut o Creat ed tab. To select a manually added ECS instance, click the Manually Added tab.
6. Find the target ECS instance and choose Act ions > Swit ch t o Prot ect ion in the Act ions column.
7. Click OK.

### 4.11 Remove an ECS instance from the Protected state

the Protected state This topic describes how to remove an ECS instance from the Protected state. After an ECS instance is removed from the Protected state, Auto Scaling continues to manage the lifecycle of the ECS instance.
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Select the source of the ECS instance.
To select an automatically created ECS instance, click the Aut o Creat ed tab. To select a manually added ECS instance, click the Manually Added tab.
6. Find the target ECS instance and choose Act ions > Move Out Of Prot ect ion in the Act ions
column.
7. Click OK.

## 5 Scaling configurations

### 5.1 Create a scaling configuration

This topic describes how to create a scaling configuration for a scaling group. Prerequisites At least one security group is available. If you do not have any security groups, create a security group. For more information, see Create a security group in ECS User Guide. Context You can create only a limited number of scaling configurations for a scaling group. For more information, see the Limits topic in Auto Scaling Product Introduction. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. Choose Creat e > Creat e Scaling Conf igurat ion.
6. Configure parameters for the scaling configuration.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Region | Yes | The region where the ECS instance is located. |
|   | Zone | Yes | The zone where the ECS instance is located. |
| Security Group | Security Group | Yes | The security group to which the ECS instance belongs. |
| Instance | Instance Family | Yes | The instance family to which the ECS instance belongs. |
|   | Instance Type | Yes | The instance type of the ECS instance. |

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Image Type | Yes | Public Image: Public images provided by Alibaba Cloud are fully licensed to offer a secure and stable operating environment for applications on ECS instances. Cust om Image: You can create custom images to install software or deploy projects that have special requirements. |
| Image |   |   |   |
| Storage | System Disk | Yes | Specify the category and size of the system disk. The operating system is installed on the system disk. You can select Ult ra Disk or St andard SSD. |
|   | Data Disk | No | Specify the category and size of the data disk. You can select Ult ra Disk or St andard SSD. You can add a maximum of 16 data disks. The maximum capacity of each data disk is 32 TiB. You can set Release wit h Inst ance and Encrypt for each data disk. |
| P d | Set Password | Yes | Select when to set password. You can select Now or Lat er. If you select Later, you can use the Change Password feature in the console to set the password. For more information, see the Change Password topic in ECS User Gui de. |

| Password Section | Parameter | Required | Description |
|---|---|---|---|
|   | Logon Password | No | The password used to log on to the ECS instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: digits, uppercase letters, lowercase letters, and special characters. Not e The password is used to log on to the operating system and is not the VNC password. |
|   | Confirm Password | No | Enter the password again. |
| Deployment Set | Deployment Set | No | The deployment set to which the instance belongs. |
| Instance Name | Configuration Name | No | The name of the scaling configuration. |
|   | Instance Name | No | The name of the ECS instance. |
| User Data | User Data | No | Windows supports two formats: Bat and Powershell. Before you perform Base64 encoding, make sure to include [bat] or [powershell] as the first line. You can run shell scripts for Linux ECS instances. |
| Quantity | Quantity | No | The number of instances to purchase. |

|   |   | [bat] |
|---|---|---|

7. Click Submit .
Result After the scaling configuration is created, it is in the Disabled state and is displayed in your scaling configuration list. To automatically create ECS instances, you must apply a scaling configuration. For more information, see Apply a scaling configuration.

### 5.2 View scaling configurations

This topic describes how to view scaling configurations.
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
The scaling groups that correspond to the specified organization, resource set, and region are displayed.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. View the list of scaling configurations.

### 5.3 Modify a scaling configuration

This topic describes how to modify a scaling configuration. You can modify the parameters of a scaling configuration based on your actual needs. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. Find the target scaling configuration and click its name in the Scaling Conf igurat ion Name/ID
column.
6. Modify the parameters of the scaling configuration.
For more information about parameters of the scaling configuration, see Create a scaling configuration.
7. Click OK.

### 5.4 Apply a scaling configuration

This topic describes how to apply a scaling configuration. You can create multiple scaling configurations for a scaling group and apply one. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. Find the target scaling configuration and click Select in the Act ions column.
Only one scaling configuration can be in the Enabled state in a scaling group. After a scaling configuration is applied, other scaling configurations are put into the Disabled state.
6. Click OK.
Result The status of the scaling configuration changes from Disabled to Enable in the St at us column.

### 5.5 Delete a scaling configuration

This topic describes how to delete a scaling configuration that is no longer needed. After you delete a scaling configuration, existing ECS instances that are created from the scaling configuration are not removed. Prerequisites The scaling configuration is in the Disabled state. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Conf igurat ion.
5. Find the target scaling configuration and click Delet e in the Act ions column.
6. Click OK.

## 6 Scaling rules

### 6.1 Create a scaling rule

This topic describes how to create a scaling rule. You can create scaling rules to add or remove ECS instances. For example, you can add an ECS instance to a scaling group. Context You can create only a limited number of scaling rules for a scaling group. For more information, see the Limits topic in Auto Scaling Product Introduction. After a scaling rule is executed, the resulting number of ECS instances in the scaling group may fall outside of the specified range. In this case, Auto Scaling automatically adjusts the number of ECS instances to ensure that the number of ECS instances in the scaling group is within the specified range. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. Click Creat e Scaling Rule.
6. Configure parameters for the scaling rule.

| Parameter | Required | Description |
|---|---|---|
| Rule Name | Yes | The name of the scaling rule. It must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods _ (.). It must start with a letter or digit. |
| Scaling Activity | Yes | The operation that is performed when the scaling rule is triggered. The operations include: Change t o N inst ances: After the scaling rule is executed, the number of instances in the scaling group is changed to N. Add N inst ances: After the scaling rule is executed, N instances are added to the scaling group. Remove N inst ances: After the scaling rule is executed, N instances are removed from the scaling group. |
| Default Cooldown (Seconds) | No | The cooldown period. If this parameter is not specified, the default value is used. |

7. Click OK.

### 6.2 View scaling rules

This topic describes how to view scaling rules. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
The scaling groups that correspond to the specified organization, resource set, and region are displayed.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. View the list of scaling rules.

### 6.3 Modify a scaling rule

This topic describes how to modify a scaling rule. You can modify the following parameters of a scaling rule: Rule Name, Scaling Activity, and Default Cooldown. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. Find the target scaling rule and click Edit in the Act ions column.
6. Modify the Rule Name, Scaling Activity, and Default Cooldown parameters.
7. Click OK.

### 6.4 Delete a scaling rule

This topic describes how to delete a scaling rule that is no longer needed. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. Find the target scaling rule and click Delet e in the Act ions column.
6. In the message that appears, click OK.

## 7 Scaling tasks

### 7.1 Manually execute a scaling rule

This topic describes how to manually execute a scaling rule to add or remove ECS instances. Prerequisites The scaling group to which the scaling rule belongs is in the Enable state. No scaling activity is in progress in the scaling group to which the scaling rule belongs. Context After the scaling rule is executed, if the number of ECS instances is greater than the maximum number or less than the minimum number, Auto Scaling automatically adjusts the number of ECS instances to be within the valid range. Auto Scaling enables you to manually execute scaling rules. You can also associate an event-triggered task or scheduled task with the scaling rule to automatically adjust the number of ECS instances. For more information, see Create a scheduled task and Create an event-triggered task. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click Scaling Rules.
5. Find the scaling rule that you want to execute and click Run in the Act ions column.
6. In the message that appears, click OK.
Result The Scaling Act ivit ies page appears. You can view the details of your scaling activity.

### 7.2 Manually add an ECS instance

This topic describes how to manually add an ECS instance to a scaling group. You can add existing ECS instances to a scaling group to take full advantage of the computing resources. Prerequisites The ECS instance to be added must meet the following conditions: The ECS instance and the scaling group to which to add the instance share the same region, organization, and resource set. The ECS instance is in the Running state. The ECS instance does not belong to any scaling groups. The ECS instance and the scaling group are in the same VPC. The scaling group to which to add the ECS instance must meet the following conditions: The scaling group is in the Enable state. No scaling activity is in progress in the scaling group. Context When no scaling activity is being executed in the scaling group, you can add an ECS instance to the scaling group without the need to wait for the cooldown time to expire. If the number of instances in the scaling group is greater than the maximum number of instances after an ECS instance is added to the scaling group, the ECS instance cannot be added. The ECS instances that are manually added to a scaling group are not limited by scaling configurations. The instance types of the manually added instances can be different from that of the scaling configuration in the Enable state. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Click Add Inst ance.
6. Select the ECS instance to be added and click OK.
Result The manually added instance is displayed on the Manually Added tab.

### 7.3 Manually remove an ECS instance

This topic describes how to manually remove an ECS instance that is no longer needed from a scaling group. Prerequisites The scaling group must meet the following conditions: The scaling group is in the Enable state. No scaling activity is in progress in the scaling group. Context When no scaling activity is being executed in the scaling group, you can immediately remove an ECS instance from the scaling group without the need to wait for the cooldown time to expire. After an ECS instances is removed from a scaling group, the number of instances in the scaling group must be greater than or equal to the minimum number of instances. Otherwise, the ECS instance cannot be removed. Procedure
1. Log on to the Auto Scaling console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Find the target scaling group and click the name of the scaling group in the Scaling Group
Name/ID column.
4. In the left-side navigation pane, click ECS Inst ances.
5. Select the source of the ECS instance.
To select an automatically created ECS instance, click the Aut o Creat ed tab. To select a manually added ECS instance, click the Manually Added tab.
6. Use one of the following methods to remove one or more ECS instances from a scaling group:
Manually added ECS instances can only be removed, but cannot be released. Find the ECS instance that you want to remove and choose Act ions > Remove f rom Scaling Group in the Act ions column. Find the ECS instance that you want to remove and release, and choose Act ions > Remove f rom Scaling Group and Release in the Act ions column.
7. In the message that appears, click OK.

## 8 Scheduled tasks

### 8.1 Create a scheduled task

This topic describes how to create a scheduled task to scale computing resources in response to predictable business changes in the future. Scheduled tasks enable the system to automatically obtain sufficient computing resources before business peaks and release idle computing resources after the business peaks. Context A scheduled task is preconfigured to execute the specified scaling rule at the specified time. When the specified time arrives, the scheduled task automatically scales computing resources. This allows you to reduce costs and meet business requirements. You can also specify recurring schedules for scheduled tasks if business changes are regular. If multiple scheduled tasks need to be executed in 1 minute, Auto Scaling executes the most recently created scheduled task. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Scheduled Tasks page, click Creat e Scheduled T ask.
5. In the dialog box that appears, configure parameters for the scheduled task.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the scheduled task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It _ must start with a letter or a digit. |
| Description | Yes | The description of the scheduled task. |
| Organization/Resou rce Group | Yes | The organization and resource set in which to create the scheduled task. |
| Start Time | Yes | The time to execute the scheduled task. |
| Scaling Rules | Yes | The scaling group to be monitored and the scaling rule to be executed. |
| Retry Interval (Seconds) | No | The period of time during which the system retires to execute the scheduled task. Unit: seconds. If a scaling activity fails to be executed at the specified time, Auto Scaling executes the scheduled task again within the period of time that is specified by the Retry Interval (Seconds) parameter. |

| Parameter | Required | Description |
|---|---|---|
| Recurrence Settings (Advanced) | No | Specifies whether to execute the scheduled task on a recurring schedule. Select Recurrence Set t ings (Advanced) and set the Recurrence and Expire parameters. The valid values for Recurrence include Daily, Weekly, and Mont hly. |

6. Click OK.
Result The scheduled task that you created is displayed in the scheduled task list.

### 8.2 View scheduled tasks

This topic describes how to view scheduled tasks. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
The scheduled tasks that correspond to the specified organization, resource set, and region are displayed.
4. Select a filter option, enter the corresponding information, and then click Search.
You can select multiple filter options to narrow down the search results.

| Option | Description |
|---|---|
| Task Name | Enter a task name to search for the scheduled task. |
| Task ID | Enter a task ID to search for the scheduled task. |

5. View the scheduled task list.

### 8.3 Modify a scheduled task

This topic describes how to modify a scheduled task. You can modify parameters such as Start Time, Scaling Rules, and Retry Expiry Time for a scheduled task. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scheduled task that you want to modify and click Edit in the Act ions column.
5. Modify the parameters of the scheduled task.
You can modify the Recurrence and Expire parameters if you have enabled the Recurrence Settings (Advanced) feature when you create the scheduled task, but the Recurrence Settings (Advanced) feature cannot be disabled. For more information about other parameters of the scheduled task, see Create a scheduled task.
6. Click OK.

### 8.4 Disable a scheduled task

This topic describes how to disable a scheduled task. You can disable a scheduled task that is no longer needed. Prerequisites The scheduled task is in the Running state. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scheduled task that you want to disable and click Disabled in the Act ions column.
5. In the message that appears, click OK.
Result The status of the scheduled task is changed from Running to St op in the St at us column.

### 8.5 Enable a scheduled task

This topic describes how to enable a scheduled task. You can enable a scheduled task that has been disabled and use it to trigger scaling activities at the specified time point. Prerequisites The scheduled task is in the St op state. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scheduled task that you want to enable and click Enable in the Act ions column.
5. In the message that appears, click OK.
Result The status of the scheduled task is changed from St op to Running in the St at us column.

### 8.6 Delete a scheduled task

This topic describes how to delete a scheduled task that is no longer needed.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > T imed t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scheduled task that you want to delete and click Delet e in the Act ions column.
5. In the message that appears, click OK.

## 9 Event-triggered tasks

### 9.1 Create an event-triggered task

This topic describes how to create an event-triggered task associated with monitoring metrics in response to emergent or unpredictable business changes. After you create and enable an eventtriggered task, Auto Scaling collects data for the specified metric in real time and triggers an alert when the specified condition is met. Then, Auto Scaling executes the corresponding scaling rule to scale Elastic Compute Service (ECS) instances in the scaling group. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert T asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the upper-right corner of the Event-Triggered Tasks page, click Creat e Alert .
5. In the dialog box that appears, configure parameters for the event-triggered task.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the event-triggered task. It must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must start _ with a letter or a digit. |
| Description | No | The description of the event-triggered task. |
| Organization/Res ource Group | Yes | The organization and resource set in which to create the event-triggered task. |
| Monitoring Metrics/Scaling Rule | Yes | The scaling group to be monitored and the scaling rule to be executed. |
| Monitoring Type | Yes | Syst em-Level Monit oring is selected by default. |
| Monitoring Metrics | Yes | The metrics that you want to monitor. Valid values: Average CPU Ut ilizat ion Memory Usage Out bound T raf f ic Inbound T raf f ic Average Syst em Load |

| Parameter | Required | Description |
|---|---|---|
| Monitoring Period | Yes | The period during which data is aggregated and analyzed. The shorter the period, the higher the frequency that the alert is triggered. Unit: minutes. Valid values: 1 2 5 15 |
| Statistic | Yes | The rule that determines whether to trigger an alert. Select Average, Max Capacit y, or Min Capacit y, and specify a threshold value. For example, to trigger an alert when the CPU utilization exceeds 80%, you can use one of the following methods to specify the trigger condition: Average: An alert is triggered when the average CPU utilization of all ECS instances in the scaling group exceeds 80%. Max Capacity: An alert is triggered when the highest CPU utilization among the ECS instances in the scaling group exceeds 80%. Min Capacity: An alert is triggered when the lowest CPU utilization among the ECS instances in the scaling group exceeds 80%. |
| Trigger After | Yes | The number of consecutive times that the threshold must be exceeded before the alert is triggered. Valid values: 1 2 3 5 |

6. Click OK.

### 9.2 View event-triggered tasks

This topic describes how to view event-triggered tasks. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert T asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
The event-triggered tasks that correspond to the specific organization, resource set, and region are displayed.
4. Select a filter option, enter the corresponding information, and then click Search.
You can select multiple filter options to narrow down the search results.

| Option | Description |
|---|---|
| Alert Name | Enter an event-triggered task name to search for the event-triggered task. |
| Scaling Group ID | Enter a scaling group ID to search for the event- triggered task associated with the scaling group. |

### 9.3 Modify an event-triggered task

This topic describes how to modify an event-triggered task. You can modify parameters such as Scaling Rules, Monitoring Type, and Statistic for an event-triggered task. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert T asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the event-triggered task that you want to modify and click Edit in the Act ions column.
5. Modify the parameters of the event-triggered task.
For more information about other parameters of the scheduled task, see Create an event-triggered task. The following parameters cannot be modified: Organization Resource Group Monitoring Metrics Monitoring Period
6. Click OK.

### 9.4 Disable an event-triggered task

This topic describes how to disable an event-triggered task. You can disable an event-triggered task if you no longer want to use it to trigger scaling activities. Prerequisites The event-triggered task is in the Normal, Alert s, or Insuf f icient Dat a state. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the event-triggered task that you want to disable and click Disable in the Act ions column.
5. In the message that appears, click OK.
Result The status of the event-triggered task is changed to St opped in the St at us column.

### 9.5 Enable an event-triggered task

This topic describes how to enable an event-triggered task. You can enable an event-triggered task that has been disabled to continue to monitor metrics and trigger scaling activities for a scaling group. Prerequisites The event-triggered task is in the St opped state. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert t asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the event-triggered task that you want to enable and click Enable in the Act ions column.
5. In the message that appears, click OK.
Result The status of the event-triggered task changes from St opped to Normal in the St at us column.

### 9.6 Delete an event-triggered task

This topic describes how to delete an event-triggered task. You can delete an event-triggered task that is no longer needed. Procedure
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose Event -driven T asks > Alert T asks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the event-triggered task that you want to delete and click Delet e in the Act ions column.
5. In the message that appears, click OK.
