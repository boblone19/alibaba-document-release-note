---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 75
source_pdf: "f25bba39f752b976_Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%BC%B9%E6%80%A7%E4%BC%B8%E7%BC%A9/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Auto%20Scaling%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling User Guide 20260828

## Table of Contents

- 1 What is Auto Scaling?
- 2 Notes
  - 2.1 Precautions
  - 2.2 Manual operations
  - 2.3 Usage limits
  - 2.4 Scaling group status
  - 2.5 Scaling processes
  - 2.6 Remove unhealthy ECS instances
  - 2.7 Rollback of failed instances in a scaling activity
  - 2.8 Instance lifecycle management
- 3 Quick start
  - 3.1 Quick Start overview
  - 3.2 Log on to the Auto Scaling console
  - 3.3 Create scaling groups
  - 3.4 Create a scaling configuration
  - 3.5 Enable a scaling group
  - 3.6 Create a scaling rule
  - 3.7 Create a scheduled task
  - 3.8 Create an event-triggered task
- 4 Scaling groups
  - 4.1 Create scaling groups
  - 4.2 Expected number of instances
  - 4.3 Enable a scaling group
  - 4.4 View a scaling group
  - 4.5 Edit scaling groups
  - 4.6 Disable scaling groups
  - 4.7 Delete a scaling group
- 5 Instances
  - 5.1 View the instance list
  - 5.2 Manually add instances to a scaling group
  - 5.3 Put an instance into the Standby state
  - 5.4 Move an instance out of the Standby state
  - 5.5 Put an instance into the Protected state
  - 5.6 Move an instance out of the Protected state
  - 5.7 Manually remove an instance from a scaling group
  - 5.8 Manually delete an instance
- 6 Scaling configurations
  - 6.1 Create a scaling configuration
  - 6.2 View scaling configurations
  - 6.3 Modify a scaling configuration
  - 6.4 Apply a scaling configuration
  - 6.5 Delete a scaling configuration
- 7 Scaling activities
  - 7.1 View scaling activity details
  - 7.2 Resolve scaling activity exceptions
- 8 Scaling rules
  - 8.1 Create a scaling rule
  - 8.2 View scaling rules
  - 8.3 Modify a scaling rule
  - 8.4 Execute a scaling rule
  - 8.5 Delete a scaling rule
- 9 Scheduled tasks
  - 9.1 Create scheduled tasks
  - 9.2 View scheduled tasks
  - 9.3 Modify a scheduled task
  - 9.4 Disable a scheduled task
  - 9.5 Enable a scheduled task
  - 9.6 Delete a scheduled task
- 10 Event-triggered tasks
  - 10.1 Create an event-triggered task
  - 10.2 View event-triggered tasks
  - 10.3 Modify an event-triggered task
  - 10.4 Disable an event-triggered task
  - 10.5 Enable an event-triggered task
  - 10.6 Delete an event-triggered task
- 11 Enable the notification feature
  - 11.1 Create event notification rules
  - 11.2 View event notification rules
  - 11.3 Edit event notification rules
  - 11.4 Delete event notification rules
- 12 Manage operation logs
  - 12.1 View operation logs

## 1 What is Auto Scaling?

Auto Scaling automatically adjusts your elastic computing resources based on your business requirements and policies that you define. When demand for services spikes, Auto Scaling automatically scales out Elastic Compute Service (ECS) instances based on your configurations to maintain sufficient computing resources. When demand for services drops, Auto Scaling automatically scales in ECS instances to save costs. Auto Scaling provides the following features: Scale-out When demand for services suddenly grows, Auto Scaling automatically scales out the underlying resources. This ensures that resources are not overloaded and maintains the responsiveness of your servers. For example, if the vCPU utilization of ECS instances exceeds 80%, Auto Scaling scales out ECS resources based on your configurations. During the scale-out event, Auto Scaling automatically creates ECS instances, adds the ECS instances to a scaling group, and then adds the new instances to the backend server groups of the associated Server Load Balancer (SLB) instances and the whitelists of the associated ApsaraDB RDS instances. The following figure shows how a scale-out event is implemented. Scale-in When demand for services drops, Auto Scaling automatically releases underlying resources to prevent waste of resources and reduce costs. For example, if the vCPU utilization of ECS instances in a scaling group falls below 30%, Auto Scaling automatically scales in ECS instances based on your configurations. During the scale-in event, Auto Scaling removes ECS instances from the scaling group and also from the backend server groups of the associated SLB instances and the whitelists of the associated ApsaraDB RDS instances. The following figure shows how a scale-in event is implemented. Elastic recovery If ECS instances in a scaling group are not in the Running state, Auto Scaling considers the instances to be unhealthy. If an ECS instance is considered unhealthy, Auto Scaling automatically releases the instance and creates a new one. This process is called elastic recovery. Elastic recovery ensures that the number of healthy ECS instances in a scaling group does not fall below the minimum number of ECS instances that you specified for the scaling group. The following figure shows how an elastic recovery event is implemented.

## 2 Notes

### 2.1 Precautions

This topic describes the precautions when you use Auto Scaling (ESS).

**Scaling rules**

ESS uses scaling rules to scale ECS instances in a scaling group based on the minimum and maximum numbers of ECS instances specified for the scaling group. Assume that a scaling group can contain up to 45 ECS instances. If you configure a scaling rule to increase the number of ECS instances in the scaling group to 50, ESS only increases the number of ECS instances to 45 at most.

**Scaling activities**

Only one scaling activity can be executed at a time in a scaling group. An ongoing scaling activity cannot be terminated. For example, if a scaling activity is being executed to create 20 ECS instances but only five have been created, you cannot forcibly terminate the scaling activity. If some ECS instances fail to be added to a scaling group during a scaling activity, ESS considers that the scaling activity is complete without trying to add the failed instances to the scaling group. ESS rolls back the ECS instances that fails to be added but not the scaling activity. For example, if ESS has created 20 ECS instances for a scaling group, and 19 of the instances are added to SLB instances, only the one ECS instance that failed to be added is automatically released.

**Cooldown period**

During the cooldown period, if you manually execute a scaling task, such as a scaling rule or scheduled task, the task is immediately executed without waiting for the cooldown period to expire. The cooldown period starts after the last ECS instance is added to or removed from a scaling group during a scaling activity.

### 2.2 Manual operations

If you perform a manual operation when an Auto Scaling operation is in progress, the manual operation takes precedence. Auto Scaling supports manual operations, such as the deletion of automatically created Elastic Compute Service (ECS) instances from the ECS console. The following table describes how Auto Scaling processes manual operations.

| Resource | Manual operation type | Processing method |
|---|---|---|

| ECS | A user deletes an ECS instance from a scaling group by using the ECS console or calling API operations. | Auto Scaling performs health checks to determine whether the ECS instance is unhealthy. If the instance is unhealthy, Auto Scaling removes it from the scaling group. The internal IP address of the ECS instance is not automatically deleted from the whitelist of the associated ApsaraDB RDS instance. If the total number of ECS instances in the scaling group falls below the lower limit after the ECS instance is removed, the scaling group automatically creates an ECS instance to ensure that the number of instances is at least equal to the lower limit. |
|---|---|---|
| ECS | A user revokes the ECS API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests. |
| Server Load Balancer (SLB) | A user manually removes an ECS instance from the associated SLB instance by using the SLB console or calling API operations. | Auto Scaling does not automatically detect this operation or handle this exception. The ECS instance remains in the scaling group. When a scale-in activity is triggered, Auto Scaling releases the ECS instance if the instance meets the conditions specified in the removal policy. |
| SLB | A user manually deletes an SLB instance or disables the health check feature for an SLB instance by using the SLB console or calling API operations. | Auto Scaling does not add ECS instances to scaling groups that are associated with this SLB instance. Auto Scaling removes ECS instances from the scaling groups if a scaling task triggers a scale-in rule or the ECS instances are considered unhealthy after a health check is performed. |
| SLB | An SLB instance is unavailable due to a system error. | All scaling activities fail, except for instance removal tasks that are manually executed. |
| SLB | A user revokes the SLB API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests for the scaling groups that are associated with SLB instances. |
| ApsaraDB RDS | A user manually removes the IP address of an ECS instance from the whitelist of the associated ApsaraDB RDS instance by using the ApsaraDB RDS console or calling API operations. | Auto Scaling does not automatically detect this operation or handle this exception. The ECS instance remains in the scaling group. When a scale-in activity is triggered, Auto Scaling releases the ECS instance if the instance meets the conditions specified in the removal policy. |
| ApsaraDB RDS | A user manually deletes an ApsaraDB RDS instance by using the ApsaraDB RDS console or calling API operations. | Auto Scaling does not add ECS instances that are associated with the ApsaraDB RDS instance to scaling groups. Auto Scaling removes ECS instances from the scaling groups if a scaling task triggers a scale-in rule or the ECS instances are considered as unhealthy after a health check is performed. |
| ApsaraDB RDS | An ApsaraDB RDS instance is unavailable due to a system error. | All scaling activities fail, except for instance removal tasks that are manually executed. |

| ApsaraDB RDS | A user revokes the ApsaraDB RDS API permissions granted to Auto Scaling. | Auto Scaling rejects all scaling activity requests for the scaling groups that are associated with ApsaraDB RDS instances. |
|---|---|---|

### 2.3 Usage limits

This topic describes the limits that apply when you use Auto Scaling. Auto Scaling only supports automatically increasing or decreasing the number of Elastic Compute Service (ECS) instances in a scaling group. It does not support automatic upgrade or downgrade of the vCPU, memory, or bandwidth configurations of a single ECS instance. Applications deployed on ECS instances in a scaling group must be stateless and horizontally scalable. Auto Scaling may automatically release ECS instances in a scaling group. Therefore, these instances are not suitable for storing session records, application data, or logs. If necessary, you can store session records and other state information on independent state servers, store application data in ApsaraDB RDS, and store logs in Simple Log Service. For more information, see the **What is ApsaraDB RDS** section of **ApsaraDB RDS Product**
**Introduction** and the **What is****Simple Log Service** section of **Simple Log Service**
**Product Introduction**.
You can add up to 1,000 ECS instances to a scaling group.

### 2.4 Scaling group status

This topic describes the console status and API status of scaling groups.

| Console-based state | API-based state |
|---|---|
| Creating | Inactive |
| Created | Inactive |
| Enabling | Inactive |
| Enabled | Active |
| Disabling | Inactive |
| Disabled | Inactive |
| Deleting | Deleting |

### 2.5 Scaling processes

Before you use Auto Scaling, you must understand the processes related to scaling activities.

**Automatic scaling of a scaling group**

Automatic scale-out i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. Create ECS instances. iv. Modify Total Capacity. v. Assign IP addresses to the created ECS instances. vi. Add the ECS instances to the whitelist of the associated ApsaraDB RDS instance. vii. Start the ECS instances. viii. Associate the ECS instances with an SLB instance and set the weight to the SLB weight value that is specified when the scaling configuration is created. ix. The cooldown period starts after the scaling activity is complete. Automatic scale-in i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. Remove ECS instances from the associated SLB instance. iv. Stop the ECS instances. v. Remove the ECS instances from the whitelist of the associated ApsaraDB RDS instance. vi. Release the ECS instances. vii. Modify Total Capacity. viii. The cooldown period starts after the scaling activity is complete.

**Manually add or remove existing ECS instances**

Manually add instances i. Check the health status and boundary conditions of the scaling group, and check the status and type of ECS instances. ii. Assign the activity ID and execute the scaling activity. iii. Add the ECS instances. iv. Modify Total Capacity. v. Add the ECS instances to the whitelist of the associated ApsaraDB RDS instance. vi. Associate the ECS instances with an SLB instance and set the weight to the SLB weight value that is specified in the active scaling configuration.

**Note**

If you want to manually add an instance to a scaling group, the instance type of the instance must be the same as that specified in the active scaling configuration of the scaling group. Therefore, you must set the weight to the SLB weight value that is specified in the active scaling configuration. vii. The cooldown period starts after the scaling activity is complete. Manually remove instances i. Check the health status and boundary conditions of the scaling group. ii. Assign the activity ID and execute the scaling activity. iii. SLB stops forwarding traffic to ECS instances. iv. Remove the ECS instances from SLB after 60 seconds. v. Remove the ECS instances from the whitelist of the associated ApsaraDB RDS instance. vi. Modify Total Capacity. vii. Remove the ECS instances from the scaling group. viii. After the scaling activity is complete, the cooldown period starts.

### 2.6 Remove unhealthy ECS instances

## instances

Before you use ESS, you must understand information about the removal of unhealthy ECS instances. After an ECS instance is added to a scaling group, ESS checks the status of the instance on a regular basis. If the ECS instance is not in the Running state, ESS removes the ECS instance from the scaling group. The removal method depends on how the ECS instance is added: If an ECS instance is automatically created, ESS immediately removes and releases it. If an ECS instance is manually added, ESS immediately removes it, but does not stop or release it. The removal of unhealthy ECS instances is not limited by the MinSize value. After the unhealthy ECS instances are removed, the number of ECS instances (Total Capacity) may fall below the MinSize value. In this case, ESS automatically creates ECS instances based on the difference between the actual instance number and MinSize value to ensure that the total number of ECS instances is equal to the MinSize value.

### 2.7 Rollback of failed instances in a scaling activity

**a scaling activity**

Before you use Auto Scaling, you must understand how instance rollback works when a scaling activity fails. During a scaling activity, if not all the Elastic Compute Service (ECS) instances are added to the scaling group, the scaling activity fails. Auto Scaling maintains the integrity of ECS instance transactions rather than scaling activity transactions. This means that Auto Scaling performs only ECS instance rollback, not scaling activity rollback. Example: If a scaling group contains 20 ECS instances but only 19 ECS instances are successfully added to the backend server group of a Server Load Balancer (SLB) instance, only the ECS instance that fails to be added is automatically released.

**Important**

When ECS instance rollback occurs in a scaling group, the number of ECS instances does not reach the expected value. This may prevent the scaling group from providing sufficient compute resources or maintaining metric values. In this case, you can use other methods to add ECS instances and ensure that the scaling group meets your business requirements. Automatically add ECS instances When you create ECS instances by calling API operations, Auto Scaling uses the Alibaba Cloud Resource Access Management (RAM) service. The rolled-back ECS instances still incur charges from the time of successful creation until automatic release. For example, five ECS instances in a scaling group must be added to the backend server group of an SLB instance. After creation, two instances are successfully added and three instances fail to be added. Auto Scaling automatically releases the three failed ECS instances. The scaling activity is complete, but the status shows **Partially Succeeded**. On the **Scaling Activities** page, you can view the status, total number of instances after scaling, start time, end time, and description of each scaling activity. A status of Partially Succeeded indicates that the scaling activity only partially succeeded. Click the activity to expand the details panel and view the cause, status information, and detailed information. For example, since the quota for ECS instances that can be attached to the SLB backend server group has been reached, the request to add five ECS instances results in only two being created, and the system marked this activity as as Partially Succeeded. Manually add ECS instances When you manually add existing instances, Auto Scaling automatically removes the rolledback ECS instances from the scaling group but does not release these ECS instances.

### 2.8 Instance lifecycle management

**management**

Before you use Auto Scaling, we recommend that you understand the instance lifecycle.

**Automatically created ECS instances**

The ECS instances are automatically created by Auto Scaling based on user-defined scaling configurations and rules. Auto Scaling manages the entire lifecycle of automatically created ECS instances. Auto Scaling creates ECS instances during scale-out activities, and stops and releases ECS instances during scale-in activities.

**Manually added ECS instances**

The ECS instances are manually added to scaling groups. Auto Scaling does not manage the entire lifecycle of manually added ECS instances. These instances are not automatically created by Auto Scaling but are manually added by a user to a scaling group. If the ECS instances are manually or automatically removed from the scaling group, Auto Scaling removes the instances but does not stop or release them.

**Instance status**

An ECS instance in a scaling group can change to the following status during its lifecycle: Pending: The ECS instance is being added to the scaling group. The instance is being created, added as the backend server of the associated SLB instance, or added to the whitelist of the associated ApsaraDB RDS instance. InService: The ECS instance is added to the scaling group and is providing services as expected. Removing: The ECS instance is being removed from the scaling group.

**Instance health status**

An ECS instance in a scaling group can change to the following health status: Healthy Unhealthy If an ECS instance is not in the Running state, Auto Scaling considers the instance unhealthy and automatically removes it from the scaling group. Auto Scaling stops and releases automatically created ECS instances. Auto Scaling does not stop or release manually added ECS instances.

## 3 Quick start

### 3.1 Quick Start overview

This topic describes how to use Auto Scaling to automatically scale your resources. It introduces the main features and operations of Auto Scaling and explains how the resource overview can help you quickly understand your resource layout. The following procedure describes how to create a scaling group and enable automatic scaling: Manually execute the scaling rule Trigger a scheduled task to Create a Create and apply a Enable the Create a execute the scaling rule scaling scaling scaling rule scaling group configuration group Trigger an event-triggered task toexecutethescalingrule A scaling group defines properties such as the maximum and minimum number of instances it can contain and the scale-in policy.
2. Create and use a scaling configuration
A scaling configuration is a template that Auto Scaling uses to automatically create Elastic Compute Service (ECS) instances. It specifies configurations such as the instance type and image.
3. Enable the scaling group
Scaling activities can occur only in enabled scaling groups. If a scaling group has an active scaling configuration, a message prompts you to enable the group. You can also enable the scaling group from the list of scaling groups. A scaling rule triggers scaling activities. It specifies the number of instances to add to or remove from a scaling group. For example, you can create a scaling rule to add one ECS instance.
5. Execute the scaling rule
You can execute a scaling rule in one of the following ways to scale instances in a scaling group:
**Manual execution**: Manually execute a scaling rule to meet temporary business needs.
**Automatic execution by a scheduled task**: Use a scheduled task to execute a scaling
rule at a specific time. This method is suitable for business fluctuations that occur at regular intervals. For more information, see Create scheduled tasks.
**Automatic execution by an event-triggered task**: Use an event-triggered task to
execute a scaling rule when an alert is triggered based on a monitoring metric. This method is suitable for unpredictable workload fluctuations. For more information, see Create an event-triggered task.

**Auto Scaling overview**

The Auto Scaling Overview page provides a comprehensive view of your resources. It helps you quickly optimize resource configurations and understand your resource layout. The page also provides multiple shortcuts to help you manage resources efficiently.
1. Log on to the Auto Scaling console.
2. In the navigation pane on the left, click **Overview**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Overview** page, view the resource overview.
The following table describes the main features.

| Area | Description |
|---|---|
| Instance overview | Number of scaling groups: The total number of scaling groups in the current organization and its sub-organizations. Number of scheduled tasks: The total number of scheduled tasks in the current organization and its sub-organizations. Number of event-triggered tasks: The total number of event- triggered tasks in the current organization and its sub-organizations. |
| Scaling groups | Total: The total number of scaling groups that can be created in the current organization and its sub-organizations. Assigned: The number of scaling groups that the current organization assigned to its sub-organizations. Used: The number of scaling groups in use by the current organization and its sub-organizations. Assignment rate = Assigned/Total. Usage rate = Used/Total. |
| ESS scaling group maximum instance quota | Total: The sum of the maximum number of instances that are allowed for all scaling groups in the current organization and its sub- organizations. Assigned: The portion of the total instance quota that the current organization assigned to its sub-organizations. Used: The sum of the maximum number of instances for all scaling groups that are created by the current organization and its sub- organizations. Assignment rate = Assigned/Total. Usage rate = Used/Total. |
| Top 10 scaling group quota usage | This section displays the top 10 organizations ranked by their scaling group quota usage. The Resource Usage Trend shows the quota usage for scaling groups in each organization, sorted by their quota usage rate. Note You can view resource usage trends for the last 7, 15, and 30 days. |

### 3.2 Log on to the Auto Scaling console

**console**

Before you use Auto Scaling to manage a group of instances that fall into the same category and can be used for similar business purposes, we recommend that you learn about how to quickly log on to the Auto Scaling console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.
1. In the address bar of your browser, enter the service domain name for the Apsara Uni-
manager Management Console and press Enter.

**Note**

You can click the current language in the upper-right corner to switch to another language. 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. Enter your username and password.

**Note**

You can obtain the username and logon password from an operations administrator. If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.
3. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement. The **Product Service Agreement**, **Privacy Agreement**, and **User**
**Agreement** are displayed only if they have been published. If none of these
agreements are published, you can skip this step.
4. Click **Account Logon** or **Authorized Logon**.

**Note**

The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".
5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of
the following scenarios:

**Note**

When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.
6. In the top navigation bar, choose **Products > Computing > Auto Scaling ESS**.

### 3.3 Create scaling groups

A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar business purposes. If you want to enable automatic increase or decrease of a specific type of instances based on policies to cope with evolving business demands, you can create scaling groups to automatically adjust computing power (the number of instances). For example, when you create a scaling group, you can specify a maximum number and a minimum number of instances to empower the automatic scaling feature. This topic describes how to create a scaling group.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For information about how to create a VPC, see the **Create a VPC** topic of Virtual Private Cloud User Guide. For information about how to create a vSwitch, see the **Create a vSwitch** topic of Virtual Private Cloud Use r Guide. If you want to attach a server load balancer (SLB) instance to a scaling group, make sure that the following requirements are met: You have one or more SLB instances in the **Running** state. For more information about how to create SLB instances, see the **Create an SLB instance** topic of Server Load Bala ncer User Guide. The SLB instance and the scaling group belong to the same organization, resource set, and region. If the network type of the SLB instance and the scaling group is VPC, the SLB instance and the scaling group use the same VPC.

**Important**

If the SLB instance and the scaling group use different VPCs, the attachment will fail. If the network type of the SLB instance is classic network, and that of the scaling group is VPC and one backend server of the SLB instance uses a VPC, the scaling group and the backend server use the same VPC. At least one listener is configured for the SLB instance. For more information, see the
**Listener overview** topic of Server Load Balancer User Guide.
The health check feature is enabled for the SLB instance. For more information, see the
**Configure health checks** topic of Server Load Balancer User Guide.
If you want to attach an ApsaraDB RDS instance to a scaling group, make sure that the following requirements are met: You have one or more ApsaraDB RDS instances that are in the **Running** state. For more information, see the **What is ApsaraDB RDS?** topic of ApsaraDB RDS User Guide. The ApsaraDB RDS instance and the scaling group belong to the same organization, resource set, and region.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scaling Groups** page, click **Create Scaling Group**.
5. In the **Create Scaling Group** dialog box, configure parameters based on your business
requirements. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Scaling Group Name | Yes | The name of the scaling group. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and _ periods (.). It must start with a letter or a digit. |
| Organization/Reso urce Set | Yes | The organization and resource set to which the scaling group belongs. |
| Region | Yes | The region where you want to create the scaling group. |
| Maximum Instances | Yes | The maximum number of instances that the scaling group can contain. To minimize costs, specify a value based on your business requirements. Valid values: 0 to 1000. |
| Minimum Instances | Yes | The minimum number of instances that the scaling group must contain. To ensure service availability, specify a value based on your business requirements. After you enable the scaling group, Auto Scaling automatically adds instances to the scaling group until the minimum number is reached. Valid values: 0 to 1000. |
| Default Cooldown Time (Seconds) | Yes | The cooldown period after each scaling activity is complete. The value must be an integer that is greater than or equal to zero. Unit: Seconds. During the cooldown period, Auto Scaling rejects all scaling requests triggered by event-triggered tasks. However, scaling requests that are triggered by other types of tasks, such as manually triggered tasks and scheduled tasks, can be processed before the cooldown time expires. Default value: 300. |

| Removal Policy | No | The instance removal policy. You can configure the First Filter and Then Filter parameters. However, you cannot set the two parameters to the same value. Valid values: Instances Created from the Earliest Scaling Configuration: Auto Scaling filters instances that are created based on the earliest scaling configuration. Earliest Added ECS Instances: Auto Scaling filters instances that are added at the earliest point in time to the scaling group. Most Recently Added Instances: Auto Scaling filters instances that are most recently added to the scaling group. No Policy: Auto Scaling performs no secondary filtering. You can set only the Then Filter parameter to No Policy. For example, if Auto Scaling filters instances based on the Earliest Added ECS Instances value of the First Filter parameter, you can select only one of the following values for the Then Filter parameter: No Policy: Auto Scaling does not remove instances from the instances that are obtained based on the value of the First Filter parameter. Most Recently Added ECS Instances: Auto Scaling filters the most recently added instances from the instances that are obtained based on the value of the First Filter parameter. Instances Created from the Earliest Scaling Configuration: Auto Scaling filters instances that are created based on the earliest scaling configuration from the instances that are obtained based on the value of the First Filter parameter. |
|---|---|---|
| VPC ID | Yes | The ID of the VPC in which you want to create the scaling group. |
| vSwitch | Yes | The vSwitch with which you want to associate the scaling group. |

| Associate SLB Instance | No | After you attach an SLB instance to the scaling group, the existing ECS instances in the scaling group are automatically added as backend servers of the SLB instance. You can specify the server group to which you want to add the ECS instances. The following server groups are supported: Default server group: the group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group. vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based routing methods, you can use vServer groups. |
|---|---|---|
| Associate ApsaraDB RDS Instance | No | After you attach an ApsaraDB RDS instance to a scaling group, the private IP addresses of the existing ECS instances in the scaling group are automatically added to the IP address whitelist of the ApsaraDB RDS instance. |

6. Click **OK**.

**Result**

The scaling group that you created is displayed on the **Scaling Groups** page but enters the
**Disable** state. You must create and enable a scaling configuration for the scaling group. For
more information, see Create a scaling configuration.

### 3.4 Create a scaling configuration

This topic describes how to create a scaling configuration for a scaling group. Auto Scaling uses the instance types that are specified in the scaling configuration to create instances.

**Prerequisites**

A security group is available in the virtual private cloud (VPC) where your scaling group for which you want to create a scaling configuration resides. For more information, see the
**Create a security group** topic in **ECS User Guide**.

**Background information**

You can create only a limited number of scaling configurations for a scaling group. For more information, see the **Limits** topic in **Auto Scaling Product Introduction**.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instance Configuration Sources** tab.
6. Click **Create Scaling Configuration**.
7. Configure the parameters for the scaling configuration. The following table describes the
parameters.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Region | Yes | The region where you want to create Elastic Compute Service (ECS) instances based on the scaling configuration. |
|   | Zone | Yes | The zone where you want to create ECS instances based on the scaling configuration. |
| Security Group | Security Group | Yes | The security group with which you want to associate ECS instances that you want to create based on the scaling configuration. |
| Instance | Instance Type | Yes | The instance type that you want to use to create ECS instances. |
| Image | Image Type | Yes | Public Image: You can select public images that are provided by Alibaba Cloud. Public images are licensed to provide a secure and stable operating environment for applications on ECS instances. Custom Image: You can create custom images that you can use to install software or deploy projects that have special requirements. Shared Custom Image: You can select a shared custom image. |
| Storage | System Disk (GB) | Yes | The category and size of the system disk. The OS is installed on the system disk. You can select Ultra Disk or Standard SSD. |
|   | Data Disk (GB) | No | The category and size of the data disk. You can select Ultra Disk or Standard SSD. You can add up to 16 data disks. The maximum capacity of each data disk is 32 TiB. You can select Release with Instance and Encryption for each data disk. |

| Password | Password Setting | Yes | The time to specify a password. Valid values: Set Now and Set After Purchase. If you set the Password Setting parameter to Set After Purchase, you must reset the password in the console after the scaling configuration is created. For more information, see the Change the logon password topic in ECS User Guide. |
|---|---|---|---|
|   | Logon Password | No | The password used to log on to the ECS instances that are created based on the scaling configuration. You must configure this parameter if you set the Password Setting parameter to Set Now. The logon password is subject to the image type that you select. For more information, see the Reset the logon password of an instance topic in ECS User Guide. Note The password is used to log on to the OS and is not the VNC password. |
|   | Confirm Password | No | You must enter the password again after you configure the Logon Password parameter. |
| Deployment Set | Deployment Set | No | The deployment set to which the instances that are created based on the scaling configuration belong. You can select a deployment set from the Deployment Set drop- down list. You can also create a deployment set. |
| Instance Name | Scaling Configuration | No | The name of the scaling configuration that you want to create. |
|   | Instance Name | No | The name of the ECS instance that you want to create based on the scaling configuration. |

| User Data | User Data | No | The Windows OS supports batch and PowerShell scripts. Before you perform Base64 encoding of user data, make sure that the first line of the data is included in [bat] or [powershell] . The Linux OS supports shell scripts. |
|---|---|---|---|
| Instances | Quantity | No | The number of instances that you want to create based on the scaling configuration. |

|   | [bat] |
|---|---|
| [powershell] |   |

8. Click **Submit**.

**Result**

After the scaling configuration is created, the scaling configuration enters the **Disable** state and is displayed in your scaling configuration list. You can click Apply in the Actions column to enable the scaling configuration. Auto Scaling can create ECS instances in a scaling group that has an enabled scaling configuration. For more information, see Apply a scaling configuration.

### 3.5 Enable a scaling group

This topic describes how to enable a scaling group. Auto Scaling can trigger scaling activities and create instances in a scaling group only after the scaling group is enabled.

**Prerequisites**

The scaling group is in the **Disable** state. The scaling group has a scaling configuration that is in the **Enable** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scaling group that you want to enable and click **Enable** in the **Actions** column.
5. Click **OK**.

**Result**

The status of the scaling group is changed from **Disable** to **Enable** in the **Status** column.

### 3.6 Create a scaling rule

This topic describes how to create a scaling rule. You can specify the number of instances that you want to add to or remove from a scaling group. For example, you can create a scaling rule to add one instance to a scaling group.

**Background information**

You can create only a limited number of scaling rules for a scaling group. For more information, see the **Limits** topic in **Auto Scaling Product Introduction**. If the total number of instances in a scaling group is out of the specified range after a scaling rule is executed, Auto Scaling creates or removes a specific number of instances to keep the total number within the specified range.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Scaling Rules** tab.
6. Click **Create Scaling Rule**.
7. Configure the parameters for the scaling rule. The following table describes the
parameters.

| Parameter | Required | Description |
|---|---|---|
| Rule Name | Yes | The name of the scaling rule. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). The name must start with a letter or a digit. |
| Scaling Activity | Yes | Valid values: To N Units: changes the number of instances in the scaling group to N. Add N Units: adds N instances to the scaling group. Remove N Units: removes N instances from the scaling group. Note Up to 500 instances can be added to or removed from a scaling group during a scaling activity. |
| Cooldown Time | Yes | The period of cooldown time after a scaling activity is complete. If you do not specify a value for this parameter, the default value is used. |

8. Click **OK**.

**Result**

On the Scaling Rules tab, you can view the information about the new scaling rule, such as the scaling rule name or ID, rule type, time when the rule is executed, and action that is specified in the rule.

### 3.7 Create a scheduled task

This topic describes how to create a scheduled task. If your business workloads are predictable, you can create a scheduled task to prepare sufficient computing resources before the business workloads increase and release excess computing resources after the business workloads decrease.

**Background information**

A scheduled task allows Auto Scaling to execute a scaling rule at the specified point in time. This way, computing resources can be automatically scaled to meet your business requirements and minimize the costs of resources. You can also specify an interval at which a scheduled task is executed to cope with the changes of business workloads in an efficient manner. If multiple scheduled tasks need to be executed within the same minute, Auto Scaling executes the most recently created scheduled task.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, click **Create Scheduled Task**.
5. In the dialog box that appears, configure the parameters. The following table describes the
parameters.

| Parameter | Required | Description |
|---|---|---|
| Name | Yes | The name of the scheduled task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). _ The name must start with a letter or a digit. |
| Description | Yes | The description of the scheduled task. |
| Organization/Resou rce Set | Yes | The organization and resource set in which you want to create the scheduled task. |
| Start From | Yes | The point in time at which you want to execute the scheduled task. |
| Monitoring Resource/Scaling Rule | Yes | The scaling group for which you want to create the scheduled task and the scaling rule that you want to specify in the scheduled task. |
| Retry Expiry Time (Seconds) | No | The timeout period during which Auto Scaling retries the scheduled task. Unit: Seconds. If Auto Scaling does not execute the scheduled task at the specified point in time, Auto Scaling retries the scheduled task during the timeout period. |
| Recurrence Interval Settings (Advanced) | No | Specifies whether to execute the scheduled task on a recurring schedule. After you select Recurrence Interval Settings (Advanced), you must configure the Recurrence Interval and Expires At parameters. Recurrence Interval: You can select By Day, By Week, or By Month. Expires At: You can use the Select Date or Select Time methods. |

6. Click **OK**.

**Result**

On the Scheduled Tasks page, the scheduled task that you created appears. You can view the information about the scheduled task, such as the scaling group for which the scheduled task is created, scaling rule that is specified in the scheduled task, task status, and task description.

### 3.8 Create an event-triggered task

**task**

This topic describes how to create an event-triggered task. If your business workloads are unpredictable or may surge unexpectedly, you can create an event-triggered task. You must specify a metric that is monitored by CloudMonitor in an event-triggered task. After you create and enable an event-triggered task, Auto Scaling collects data for the specified metric in real time and CloudMonitor triggers an alert when the specified condition is met. Then, Auto Scaling executes the scaling rule that is associated with the event-triggered task to scale instances in your scaling group.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, click **Create Event-triggered Task**.
5. In the Create Event-triggered Task dialog box, configure the parameters. The following
table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the event-triggered task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). The name _ must start with a letter or a digit. |
| Description | No | The description of the event-triggered task. |
| Organization/Res ource Set | Yes | The organization and the resource set in which you want to create the event-triggered task. |
| Monitoring Resource/Scaling Rule | Yes | The scaling group for which you want to create the event- triggered task and the scaling rule that you want to specify in the event-triggered task. |
| Monitor Type | Yes | Valid value: System Monitoring. |
| Metric | Yes | The metric that you want to specify in the event-triggered task. Valid values: Average CPU Usage Memory Usage Outbound Traffic over Internal Network Inbound Traffic over Internal Network Average System Load |

| Statistical Period | Yes | The period during which data is collected, aggregated, and analyzed. The shorter the period, the more frequently the alert is triggered. Unit: Minutes. Valid values: 1 2 5 15 |
|---|---|---|
| Statistical Method | Yes | The rule that determines whether to trigger an alert. Select Average, Max Capacity, or Min Capacity, and specify a threshold. For example, you can specify one of the following rules to trigger an alert when the CPU utilization exceeds 80%: Average: triggers an alert when the average CPU utilization of all instances in the scaling group exceeds 80%. Max Capacity: triggers an alert when the highest CPU utilization among all instances in the scaling group exceeds 80%. Min Capacity: triggers an alert when the lowest CPU utilization among all instances in the scaling group exceeds 80%. |
| Trigger Alert After {1} Times | Yes | The number of consecutive times that the threshold must be exceeded before the alert is triggered. Valid values: 1 2 3 5 |

6. Click **OK**.

**Result**

On the Event-triggered Tasks page, the event-triggered task that you created appears. You can view the information about the event-triggered task, such as the monitoring type, statistical period, alert condition, and task description.

## 4 Scaling groups

### 4.1 Create scaling groups

A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar business purposes. If you want to enable automatic increase or decrease of a specific type of instances based on policies to cope with evolving business demands, you can create scaling groups to automatically adjust computing power (the number of instances). For example, when you create a scaling group, you can specify a maximum number and a minimum number of instances to empower the automatic scaling feature. This topic describes how to create scaling groups.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For information about how to create a VPC, see the **Create a VPC** topic of Virtual Private Cloud User Guide. For information about how to create a vSwitch, see the **Create a vSwitch** topic of Virtual Private Cloud User Guide. If you want to attach a server load balancer (SLB) instance to a scaling group, make sure that the following requirements are met: You have one or more SLB instances in the **Running** state. For more information about how to create SLB instances, see the **Create an SLB instance** topic of Server Load Bala ncer User Guide. The SLB instance and scaling group must belong to the same organization, resource set, and region. The SLB instance and scaling group must share the same VPC if both are VPC-type.

**Important**

If their VPCs differ, the attachment will fail. If the SLB instance uses the classic network, but the scaling group is in a VPC, then any backend server in the SLB instance that uses a VPC must belong to the same VPC as the scaling group. At least one listener is configured for the SLB instance. For more information, see the
**Listener overview** topic of Server Load Balancer User Guide.
The health check feature is enabled for the SLB instance. For more information, see the
**Configure health checks** topic of Server Load Balancer User Guide.
If you want to attach an ApsaraDB RDS instance to a scaling group, make sure that the following requirements are met: You have one or more ApsaraDB RDS instances that are in the **Running** state. For more information, see the **What is ApsaraDB RDS?** topic of ApsaraDB RDS User Guide. The ApsaraDB RDS instance and scaling group must belong to the same organization, resource set, and region.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scaling Groups** page, click **Create Scaling Group**.
5. In the **Create Scaling Group** dialog box, configure the following parameters based on
your business requirements.

| Parameter | Required | Description |
|---|---|---|
| Scaling Group Name | Yes | The name of the scaling group. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must _ start with a letter or a digit. |
| Organization/Resour ce Set | Yes | The organization and resource set to which the scaling group belongs. |
| Region | Yes | The region where you want to create the scaling group. |
| Maximum Instances | Yes | The scaling group's upper instance limit. Set this value based on your business needs to optimize costs. Valid values: 0 to 1000. |
| Minimum Instances | Yes | The scaling group's lower instance limit. Set this value according to your workload needs to ensure service availability. After you enable the scaling group, Auto Scaling automatically adds instances to the scaling group until the minimum number is reached. Valid values: 0 to 1000. |
| Expected Instances | No | The desired number of instances in the scaling group. This parameter is required if you turn on the Enable Expected Number of Instances switch. If you enable this feature, Auto Scaling automatically ensures that the actual number of instances in the scaling group equals the desired number. For more information, see Expected number of instances. |
| Default Cooldown Time (Seconds) | Yes | The waiting period after each scaling activity completes. The value must be an integer that is greater than or equal to zero. Unit: Seconds. During the cooldown time, Auto Scaling rejects all scaling requests of event-triggered tasks. However, scaling requests that are triggered by other types of tasks, such as manually triggered tasks and scheduled tasks, can be processed before the cooldown time expires. Default value: 300. |

| Removal Policy | Yes | The instance removal policy. You can configure the First Filter and Then Filter parameters. However, you cannot set the two parameters to the same value. Valid values: Instances Created from the Earliest Scaling Configuration: Auto Scaling filters out instances that are created from the earliest scaling configuration. Earliest Added ECS Instances: Auto Scaling filters out instances that are added at the earliest point in time. Most Recently Added Instances: Auto Scaling filters out instances that are most recently added. No Policy: Auto Scaling performs no secondary filtering. You can set only the Then Filter parameter to No Policy. For example, if Auto Scaling filters out instances based on the Earliest Added ECS Instances value of the First Filter parameter, you can select only one of the following values for the Then Filter parameter: No Policy: Auto Scaling does not remove instances selected by the First Filter parameter. Most Recently Added ECS Instances: Auto Scaling removes the most recently added ECS instances from the filtered results obtained by using the First Filter parameter. Instances Created from the Earliest Scaling Configuration: Auto Scaling removes the instances created from the earliest scaling configuration from the filtered results obtained by using the First Filter parameter. |
|---|---|---|
| VPC ID | Yes | The ID of the VPC in which you want to create the scaling group. |
| vSwitch | Yes | The vSwitch with which you want to associate the scaling group. |
| Associate SLB Instance | No | After you attach an SLB instance to the scaling group, the existing ECS instances in the scaling group are automatically added as backend servers of the SLB instance. You can specify the server group to which you want to add the ECS instances. The following server groups are supported: Default server group: the group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group. vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL- based routing methods, you can use vServer groups. |

| Associate ApsaraDB RDS Instance | No | After you attach an ApsaraDB RDS instance to the scaling group, the private IP addresses of the ECS instances that are added to the scaling group are automatically whitelisted for the ApsaraDB RDS instance. This enables secure internal network communication between them. |
|---|---|---|

6. Click **OK**.
The scaling group that you created is displayed in the scaling group list but is in the
**Disabled** state. You must create and enable a scaling configuration for the scaling group.
For more information, see Create scaling configurations.

### 4.2 Expected number of instances

If you enable the Expected Number of Instances feature for a scaling group, Auto Scaling adjusts the number of instances in the scaling group to maintain the specified expected number. Auto Scaling also flexibly executes parallel scaling activities, without the need for manual intervention. This topic describes the usage notes, instance change patterns, and usage examples of the Expected Number of Instances feature.

**Introduction**

Auto Scaling ensures that the total number of instances in a scaling group equals to the expected number of instances if you enable the Expected Number of Instances feature for the scaling group. If you enable the Expected Number of Instances feature for a scaling group and the current number of instances in the scaling group does not match the specified expected number, Auto Scaling executes scaling activities in the scaling group to ensure that the number of instances matches the expected number. No manual intervention is required during the process.

**Benefits**

The Expected Number of Instances feature improves the utilization of scaling groups and automates the execution of scaling operations, which effectively resolves the following issues: Low utilization of scaling groups. If you do not enable the Expected Number of Instances feature for a scaling group, Auto Scaling rejects new scaling requests when the scaling group has an ongoing scaling activity. For example, if the Health Check feature attempts to trigger a scaling activity in a scaling group while the scaling group has an ongoing scaling activity, Auto Scaling rejects the scaling request from the Health Check feature. Manual retry upon scaling failures. If you do not enable the Expected Number of Instances feature for a scaling group, you must manually retry the scaling operation when a scaling failure occurs.

**Note**

For more information about the results you see when the Expected Number of Instances feature is enabled, see Differences between scaling groups with an expected number of instances and scaling groups without an expected number of instances.

**Enable or disable the Expected Number of Instances feature**

You can enable or disable the Expected Number of Instances feature in the following ways: When you create a scaling group or modify an existing scaling group, you can configure the
**Expected Number of Instances** parameter to enable the Expected Number of Instances
feature. For more information, see Create scaling groups.

**Note**

After you enable the Expected Number of Instances feature for a scaling group, you can subsequently modify the expected number of instances based on your business requirements. You can call an API operation to disable the Expected Number of Instances feature for a scaling group.

**Concepts**

Before you use the Expected Number of Instances feature, we recommend that you understand the concepts described in the following table.

| Concept | Description |
|---|---|
| Stable instance | An instance that is in the In Service, Protected, or Standby state in a scaling group. |
| Parallel scaling activity | A scaling activity that can be executed in parallel with other ongoing scaling activities in a scaling group. Parallel scaling activities can be triggered by the following actions: Execute a scaling rule manually or by using a scheduled task. Manually add or remove instances. Automatically check the expected number of instances, instance health, minimum number of instances, and maximum number of instances. |
| Non-parallel scaling activity | A scaling activity that cannot be executed in parallel with other ongoing scaling activities in a scaling group. A scaling activity that is not a parallel scaling activity is a non-parallel scaling activity. Non-parallel scaling activities can be triggered by the following actions: Execute a scaling rule by using an event-triggered task. Manually execute a rebalancing task on the Instances tab. Automatically supplement preemptible instances. Note If you set the Scaling Policy parameter to Cost Optimization Policy and turn on the Enable Supplemental Preemptible Instances switch when you create a scaling group, Auto Scaling creates preemptible instances to supplement the instances that are going to be reclaimed in five minutes. |

**Usage notes**

Scaling groups for which the Expected Number of Instances feature is enabled cannot have parallel scaling activities and non-parallel scaling activities in progress at the same time. You must set the Expected Number of Instances parameter to a value that ranges from the Minimum Number of Instances value to the Maximum Number of Instances value.

**Rules for changes to the expected number of instances**

You can manually specify an expected number of instances. You can also manually execute scaling activities to modify the expected number of instances. The change patterns of the expected number of instances vary based on how scaling activities are triggered.

| Scaling activity type | Method to trigger a scaling activity | Scaling activity result | Change pattern | Example |
|---|---|---|---|---|
|   | Manually execute a scaling rule. | Only the expected number of instances is changed. You must wait for Auto Scaling to check the new expected number of instances and determine whether to add or remove instances. | Number of stable instances ± Number of added or removed instances | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 The scaling rule specifies to create four ECS instances. Result: The expected number of instances is changed to 6, but the ECS instances are not immediately created. You must wait for Auto Scaling to perform a check on the expected number of instances and determine whether to add or remove instances. |
|   | Execute a scaling rule by using a schedule d task. | Only the expected number of instances is changed. You must wait for Auto Scaling to check the new expected number of instances and determine whether to add or remove instances. | Number of stable instances ± Number of added or removed instances | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 The scaling rule specifies to create four ECS instances. Result: The expected number of instances is changed to 6, but the ECS instances are not immediately created. You must wait for Auto Scaling to check the expected number of instances and determine whether to create instances. |

| Parallel scaling activities |   |   |   |   |
|---|---|---|---|---|
|   | Manually add instances . | The instances are immediately added, and the expected number of instances is changed. | Current expected number of instances + Number of manually added instances | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 Manually add four ECS instances to the scaling group. Result: Four ECS instances are added to the scaling group. The number of stable instances is changed to 6, and the expected number of instances is changed to 7. |
|   | Manually remove instances . | The instances are immediately removed, and the expected number of instances is changed. | Current expected number of instances - Number of manually removed instances | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 Manually remove one ECS instance from the scaling group. Result: One instance is removed from the scaling group. The number of stable instances is changed to 1, and the expected number of instances is changed to 2. |
|   | Check the minimum and maximu m numbers of instances . | - | Manually specify an expected number of instances . | Scenario: Current maximum number of instances: 5 Current minimum number of instances: 0 Current expected number of instances: 3 Current number of stable instances: 2 Manually change the maximum number of instances to one. Result: The maximum number failed to be changed. You must manually specify the expected number of instances. |

|   | Check the health status of instances . | The instances are immediately removed from the scaling group. | The expected number of instances remains unchang ed. | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 One ECS instance is considered unhealthy. Result: The expected number of instances remains unchanged. The unhealthy instance is removed from the scaling group, and the number of stable instances is changed to 1. Auto Scaling detects the difference between the expected number of instances and the number of stable instances when it checks the expected number of instances, and then creates two ECS instances. |
|---|---|---|---|---|
|   | Check the expected number of instances . | The instances are immediately added to or removed from the scaling group. | The expected number of instances remains unchang ed. | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 Result: The expected number of instances remains unchanged. Auto Scaling detects the difference between the expected number of instances and the number of stable instances when it checks the expected number of instances, and then creates one ECS instance. |
| Non- parallel scaling activities | Execute a scaling rule by using an event- triggered task. | The instances are immediately added to or removed from the scaling group, and the specified expected number of instances is changed. | Number of stable instances ± Number of added or removed instances | Scenario: Current expected number of instances: 3 Current number of stable instances: 2 The scaling rule specifies to create four ECS instances. Result: A scaling activity is triggered to create four instances, and the expected number of instances is changed to 6. |

**Note**

For more information about how to specify the expected number of instances, see Examples of parallel scaling activities and Examples of non-parallel scaling activities.

**Differences between scaling groups with an expected number**

**of instances and scaling groups without an expected number of**

**instances**

The following table describes the differences between scaling groups with an expected number of instances and scaling groups without an expected number of instances.

| Item | With an expected number of instances | Without an expected number of instances |
|---|---|---|
| Maintenance costs | Automatic maintenance: Auto Scaling automatically scales instances to maintain the expected number of instances in a scaling group. If a scaling activity fails in the scaling group, Auto Scaling automatically retries the failed scaling activity. | Manual maintenance: You must manually adjust the number of instances in a scaling group. If a scaling activity fails in the scaling group, you must manually retry the failed scaling activity. |
| Execution results of scaling activities | The execution results of scaling activities vary based on how scaling rules are executed. If you manually execute a scaling rule or if you use a scheduled task to execute a scaling rule in a scaling group, Auto Scaling does not immediately execute a scaling activity. Auto Scaling just automatically changes the expected number of instances. During the check on the expected number of instances, Auto Scaling calculates the difference between the number of stable instances and the expected number of instances and scales instances based on the difference. If you manually add instances to or remove instances from a scaling group, manually delete instances, or use an event-triggered task to execute a scaling rule, Auto Scaling immediately executes a scaling activity and automatically changes the expected number of instances. | If you manually execute a scaling rule, use an event- triggered task or scheduled task to execute a scaling rule, manually add instances to or remove instances from a scaling group, or manually delete instances, Auto Scaling immediately executes a scaling activity to add or remove instances. |
| Execution of parallel scaling activities | Scaling groups support the execution of parallel scaling activities. For more information, see Examples of parallel scaling activities. | A scaling group supports only one scaling activity at a time. The scaling activity may take a long time to execute. During this period, you cannot adjust the number of instances in the scaling group. |

**Examples of parallel scaling activities**

After you specify the expected number of instances, Auto Scaling can execute parallel scaling activities at the same time.

**Example 1: Manually execute scaling rules in a consecutive**

**manner**

**Scenario:**

Expected number of instances: 3 Number of stable instances: 3 The add3 scaling rule specifies to create three ECS instances. The add1 scaling rule specifies to create one ECS instance. Manually execute the add3 scaling rule and the add1 scaling rule in sequence.

**Result:**

After the add3 scaling rule is executed, the expected number of instances is changed from 3 to 6. The add1 scaling rule is immediately executed, and the expected number of instances is changed from 6 to 4. After the parallel scaling activity is executed, one instance is created and the number of stable instances in the scaling group is changed to 4.

**Example 2: Manually execute a scaling rule and add instances**

**at the same time**

**Scenario:**

Expected number of instances: 3 Number of stable instances: 3 The add1 scaling rule specifies to create one ECS instance. Manually execute the add1 scaling rule and add an existing ECS instance at the same time.

**Result:**

After the add1 scaling rule is executed, the expected number of instances is changed from 3 to 4. One existing ECS instance is immediately added to the scaling group, and the expected number of instances is changed from 4 to 5. After the parallel scaling activity is complete, one ECS instance is created, one existing ECS instance is added, and the number of stable instances in the scaling group is changed to 5.

**Examples of non-parallel scaling activities**

After you specify the expected number of instances, Auto Scaling cannot execute parallel and non-parallel scaling activities at the same time. Example:

**Scenario:**

Expected number of instances: 1 Number of stable instances: 1. The scaling rule associated with an event-triggered task specifies to create three ECS instances. The add1 scaling rule specifies to create one ECS instance. You trigger the event-trigger task and then manually execute the add1 scaling rule.

**Result:**

Result: After you execute the event-triggered task, the expected number of instances is changed from 1 to 4. The scaling activity caused by the event-triggered task is a non-parallel scaling activity and cannot be immediately executed. The request to execute the add1 scaling rule is rejected, and the expected number of instances remains unchanged. After the non-parallel scaling activity is complete, three ECS instances are created, and the number of stable instances in the scaling group is changed to 4.

### 4.3 Enable a scaling group

This topic describes how to enable a scaling group. Auto Scaling can trigger scaling activities and create instances in a scaling group only after the scaling group is enabled.

**Prerequisites**

The scaling group is in the **Disable** state. The scaling group has a scaling configuration that is in the **Enable** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scaling group that you want to enable and click **Enable** in the **Actions** column.
5. Click **OK**.

**Result**

The status of the scaling group is changed from **Disable** to **Enable** in the **Status** column.

### 4.4 View a scaling group

After you create a scaling group, you can view the details of the scaling group. If you have multiple existing scaling groups, you can view the list of scaling groups. The details of a scaling group include its basic information, instance list, instance configuration sources, and scaling rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scaling Groups** page, search for the scaling group whose details you want to
query. Filter by single condition: Select **Scaling Group Name**, **Scaling Group ID**, or **Tag**, enter the filter information, and then click . Filter by multiple conditions: Click **Advanced Filter**, enter multiple filters, and then click
**Search**. You can select multiple filters to narrow down your search for scaling groups. By
applying these filters one by one, you can quickly identify the specific scaling groups you need. To set a new filter condition, click **Reset**.

| Filter condition | Example |
|---|---|

| Scaling Group Name | You can search for a scaling group by name. |
|---|---|
| Scaling Group ID | You can search for a scaling group by ID. Separate multiple scaling group IDs with commas (,). |
| Tag | If you have added tags to your scaling groups for centralized management, you can search for the desired scaling group by entering a tag key or tag value. Note To add or remove tags to or from scaling groups, perform the following operations: Add tags to scaling groups: Select multiple scaling groups and click Add Tags. In the dialog box that appears, add tag keys and tag values and click OK. Then, click OK in the message that appears. Remove tags: Select multiple scaling groups and clickR emove Tags. In the dialog box that appears, remove the unwanted tag keys and tag values and click OK. Then, click OK in the message that appears. |

5. Click the name of the desired scaling group in the **Scaling Group Name/ID** column.
6. View the details of the scaling group.

| Tab | Example |
|---|---|
| Basic Information | Basic Information: provides the basic information about the scaling group, such as the scaling group ID, scaling group name, time when the scaling group was created, and time when the scaling group was last modified. Auto Scaling Architecture: provides information about the instances in the scaling group, such as the maximum number of instances, the minimum number of instances, cooldown time (seconds), and instance status. Scaling Group Information: provides information about the configurations of the scaling group, such as the total number of instances, removal policy, multi- zone scaling policy, instance configuration source, and reclaim mode. You can click the links next to the Instance Configuration Source parameter, the VPC ID parameter, and the vSwitch parameter to go to the corresponding details pages. |
| Instances | Provides information about the instances in the scaling group, such as the automatically created instances, manually added instances, and instances in In service, Adding, or other states. |
| Instance Configurati on Sources | Provides information about all scaling configurations in the scaling group. You can create, modify, apply, or delete scaling configurations based on your business requirements. |

| Scaling Activities | Provides information about all scaling activities that are triggered in the scaling group, such as the total number of instances after scaling activities are complete, start time of scaling activities, end time of scaling activities, description or reason for scaling activities, status information of scaling activities, and status of scaling activities. |
|---|---|
| Scaling Rules | Provides information about all scaling rules that are created in the scaling group. You can create, execute, modify, or delete scaling rules based on your business requirements. |
| Notification Settings | Provides information about the event notifications in the scaling group. You can create, edit, or delete event notification rules based on your needs. |
| Operation Logs | Provides information about operation logs in the scaling group, such as the operation name, operator, operation time, and operation source IP address. |

**Note**

On the **Scaling Groups** page, you can refresh, delete, disable, or enable a scaling group. You can also refresh, delete, disable, or enable a scaling group on the scaling group details page. On the **Scaling Groups** page, you can click the link in the **Scaling Group**
**Configuration** column of a scaling group to view the effective scaling
configuration of the scaling group. You can also go to the **Instance**
**Configuration Sources** tab of the scaling group details page to view the
effective scaling configuration.

### 4.5 Edit scaling groups

If your current scaling group's properties no longer meet your needs, you can update them— such as adjusting the maximum or minimum number of instances—without creating a new scaling group.

**Note**

After you adjust the minimum or maximum instance limits for a scaling group, Auto Scaling automatically adds or removes instances to keep the total within the specified range.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scaling group you want to edit and click **Modify** in the **Actions** column.
5. Modify the scaling group's properties.
You cannot modify the **Organization/Resource Set** or **VPC ID** parameters. However, you can adjust the following: **Region**, **Maximum Instances**, **Minimum Instances**, **Scaling**
**Group Configuration**, and others. For more information, see Create scaling groups.

**Note**

If no scaling configuration exists, create one before modifying the **Select a scaling**
**configuration** parameter. Click **Add Scaling Configuration** to proceed.
6. Click **OK**.
After editing a scaling group, you can view its updated properties. For example, the new scaling configuration appears in the **Scaling Group Configuration** column.

### 4.6 Disable scaling groups

If a scaling group is **enabled** but no longer needed for scaling activities, you can disable it. Once disabled, the scaling group rejects all subsequent scaling requests.

**Prerequisites**

Ensure the scaling group you want to disable has no **ongoing** scaling activities. The scaling group is in the **Enabled** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scaling group you want to disable and click **Disable** in the **Actions** column.
5. In the message that appears, click **OK**.
The scaling group status updates from **Enabled** to **Disabled**.

### 4.7 Delete a scaling group

This topic describes how to permanently delete a scaling group. When you delete a scaling group, Auto Scaling removes and releases instances that are automatically created, removes instances that are manually added, and deletes the scaling configurations and scaling rules. However, the scheduled tasks and event-triggered tasks that are associated with the scaling group are not deleted.

**Prerequisites**

The scaling group is no longer needed.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the scaling group that you want to delete and click **Delete** in the **Actions** column.
5. In the message that appears, click **OK**.

**Result**

After you delete the scaling group and refresh the Scaling Groups page, the scaling group does not appear.

## 5 Instances

### 5.1 View the instance list

After you manually or automatically add instances to a scaling group, you can query details about the instance list in the scaling group, the number of instances in the scaling group, and the cooldown time as needed.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target scaling group and click the name of the scaling group in the **Scaling Group**
**Name/ID** column.
5. On the scaling group details page, click the **Instances** tab to view instance-related
information and available operations.

**Automatically created instances**

Auto Scaling automatically creates these instances based on the scaling configuration that you enable when a scaling rule runs. On the **Auto Create** tab, view the details of automatically created instances. Examples:
**ECS Instance ID/Name**: The ID or name of the instance that has been automatically
added to the scaling group.
**Instance Configuration Source**: The scaling configuration that the current scaling
group uses.
**Status**: The current status of the instance after it is automatically added to the scaling
group.
**Warmup**: Indicates whether the newly added instance requires warmup.
**Health Status**: Indicates whether the instance that has been automatically added to the
scaling group is healthy.
**Default SLB Weight**: The weight that Auto Scaling sets when it adds the instance to the
vServer group. The default value is 50.
**Added At**: The time when the instance is automatically added to the scaling group.
You can select an automatically created instance and then click **Enter Standby**, **Enter**
**Protected**, **Remove**, or **Remove and Delete** to perform the corresponding operation on
the instance. You can also select multiple automatically created instances and then click
**Remove and Delete** to remove and delete multiple instances at a time.

**Manually added instances**

These are instances that you manually add to the scaling group instead of instances that Auto Scaling automatically creates. On the **Manually Added** tab, view the details of manually added instances. Examples:
**ECS Instance ID/Name**: The ID or name of the instance that manually joins the scaling
group.
**Status**: The current status of the instance after it manually joins the scaling group.
**Warmup Status**: Whether the newly added instance requires warmup.
**Health Status**: Whether the instance that manually joins the scaling group is healthy.
**Default Server Group Weight in SLB**: The weight that Auto Scaling sets when it adds
the instance to the vServer group. The default value is 50.
**Added At**: The time when the instance manually joins the scaling group.
You can select an instance and then click **Switch to Standby State**, **Switch to**
**Protected State**, or **Remove from Scaling Group** to perform the corresponding
operation on the manually added instance. You can also select multiple instances and then click **Remove from Scaling Group** to remove multiple manually added instances in batches.

**Note**

To learn about the standby state and the protected state, click **About Standby**
**Instances** or **About Protected Instances** on the **Manually Added** tab to view
details.
6. Click the **Basic Information** tab to view the number of instances in the scaling group and
the cooldown time. In the **Auto Scaling Architecture: ECS Instance** section, you can view the following information:
**Total**: The total number of instances in the scaling group.
**Maximum Number of Instances**: The maximum number of instances that the scaling
group can contain.
**Minimum Number of Instances**: The minimum number of instances that the scaling
group must contain.
**Cooldown Time (Seconds):** : The default cooldown time after a scaling activity occurs
in the scaling group, in seconds.
**In Service**: The number of instances that are in normal use.
**Standby**: The number of instances that are in the standby state.
**Protected**: The number of instances that are in the protected state.
**Adding**: The number of instances that are being added to the scaling group.
**Removing**: The number of instances that are being removed from the scaling group.

**Note**

The Stopped, Pending Add, and Pending Remove states are unavailable.

### 5.2 Manually add instances to a scaling group

**scaling group**

This topic describes how to manually add instances to a scaling group. You can add existing instances to a scaling group to utilize computing resources.

**Prerequisites**

The instances that you want to add to a scaling group must meet the following requirements: The instances that you want to add and the scaling group to which you want to add the instances are in the same region, organization, and resource set. The instances are in the **Running** state. The instances do not belong to other scaling groups. The instances and the scaling group are in the same virtual private cloud (VPC). The scaling group to which you want to add instances must meet the following requirements: The scaling group is in the **Enable** state. The scaling group has no scaling activities in progress.

**Background information**

You can manually add instances to a scaling group even before the cooldown time expires. If the number of instances in the scaling group is greater than the maximum number of instances after you manually add instances to the scaling group, you cannot add the instances. The instance types of the instances that you want to manually add to a scaling group can be different from the instance types specified in the scaling configuration that is in the
**Enable** state of the scaling group.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. On the **Add Manually** tab, click **Add Existing Instance**.
7. In the Manually Add ECS Instance dialog box, select the instances that you want to add and
click **OK**.

**Result**

After you manually add instances to the scaling group, the instances appear on the **Add**
**Manually** tab.

### 5.3 Put an instance into the Standby state

**Standby state**

This topic describes how to put an instance into the Standby state. Auto Scaling does not release or perform health checks on instances that are in the Standby state.

**Background information**

After you put an instance into the Standby state, the following rules apply: The instance remains in the Standby state until you manually move it out of the Standby state. Auto Scaling stops managing the lifecycle of the instance. You must manually manage the lifecycle of the instance. If a scale-in activity is triggered, Auto Scaling does not remove the instance from the scaling group. When the instance is stopped or restarted, the health check status of the instance is not updated. To release the instance, you must first remove the instance from the scaling group. If you delete the scaling group, the instance is automatically removed from the Standby state and subsequently released. You can perform the following operations on the instance: stop the instance, restart the instance, change the instance type, and change the OS.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Select the source of an instance.
To select an automatically created instance, click the **Auto Created** tab. To select a manually added instance, click the **Manually Added** tab.
7. Find the instance that you want to put into the Standby state and click **Switch to Standby**
in the **Actions** column.
8. Click **OK**.

### 5.4 Move an instance out of the Standby state

**Standby state**

You can move an instance out of the Standby state to reuse the instance.

**Background information**

After you move an instance out of the Standby state, the following rules apply: The instance enters the In Service state. When the instance is stopped or restarted, the health status of the instance is updated. Auto Scaling continues to manage the lifecycle of the instance, and can remove the instance from the scaling group during a scale-in activity.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Specify the source of instances.
To select an automatically created instance, click the **Auto Create** tab. To select a manually added instance, click the **Add Manually** tab.
7. Find the instance that you want to manage and click **Remove from Standby** in the
**Actions** column.
8. Click **OK**.

### 5.5 Put an instance into the Protected state

**Protected state**

If you do not want an instance to be removed from your scaling group, you can put the instance into the Protected state. Auto Scaling does not check the health status of instances that are in the Protected state or release the instances.

**Background information**

After you put an instance into the Protected state, the following rules apply: The instance remains in the Protected state until you manually move it out of the Protected state. If a scale-in activity is triggered, Auto Scaling does not remove the instance from the scaling group. The instance can be released only after you move it out of the Protected state. When the instance is stopped or restarted, the health check status of the instance is not updated.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Select the source of an instance.
To select an automatically created instance, click the **Auto Created** tab. To select a manually added instance, click the **Manually Added** tab.
7. Find the instance that you want to manage and click **Switch to Protected** in the **Actions**
column.
8. Click **OK**.

### 5.6 Move an instance out of the Protected state

**Protected state**

You can move an instance out of the Protected state. This way, Auto Scaling manages the lifecycle of the instance.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Specify the source of instances.
To select an automatically created instance, click the **Auto Create** tab. To select a manually added instance, click the **Add Manually** tab.
7. Find the instance that you want to manage and click **Remove from Protected** in the
**Actions** column.
8. Click **OK**.

### 5.7 Manually remove an instance from a scaling group

**from a scaling group**

If you no longer need an instance, you can manually remove the instance from your scaling group. However, the instance is not released.

**Prerequisites**

Before you manually remove an instance from a scaling group, make sure that the following conditions are met: The scaling group is in the **Enable** state. No scaling activity is in progress in the scaling group.

**Background information**

You can manually remove an instance from a scaling group without the need to wait for the cooldown time to expire. After you remove an instance from a scaling group, the number of instances in the scaling group must be greater than or equal to the minimum number of instances allowed. Otherwise, you cannot remove the instance from the scaling group.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Select the source of an instance.
To select an automatically created instance, click the **Auto Created** tab. To select a manually added instance, click the **Manually Added** tab.
7. Find the instance that you want to remove from the scaling group and click **Remove from**
**Scaling Group** in the **Actions** column.
8. Click **OK**.

### 5.8 Manually delete an instance

If you no longer need an instance, you can manually remove the instance from your scaling group and permanently delete the instance.

**Prerequisites**

Before you delete an instance in a scaling group, make sure that the following conditions are met: The scaling group is in the **Enable** state. No scaling activity is in progress in the scaling group.

**Background information**

You can manually remove an instance from a scaling group and delete the instance without the need to wait for the cooldown time to expire. After you remove an instance from a scaling group and delete the instance, the number of instances in the scaling group must be greater than or equal to the minimum number of instances allowed. Otherwise, you cannot delete the instance.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Instances** tab.
6. Select the source of an instance.
To select an automatically created instance, click the **Auto Created** tab. To select a manually added instance, click the **Manually Added** tab.
7. Find the instance that you want to delete and click **Remove and Delete** in the **Actions**
column.
8. Click **OK**.
s

## 6 Scaling configurations

### 6.1 Create a scaling configuration

You can define a scaling configuration to specify the instance template for automatic scaling. When a scale-out is triggered in the scaling group, Auto Scaling uses the scaling configuration as the template to scale out instances. This simplifies instance creation and management and improves the success rate of scale-outs. This topic describes how to create a scaling configuration.

**Important**

You can create only a limited number of scaling configurations for each scaling group. For more information, see the **Limits** topic of the **Notes** chapter in Auto Scaling User Guide.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target scaling group and click the name of the scaling group in the **Scaling Group**
**Name/ID** column.
5. On the details page of the scaling group, click the **Instance Configuration Sources** tab.
6. Click **Create Scaling Configuration**.
7. On the **Scaling Configuration** page, configure parameters based on your business
requirements. The following table describes the parameters.

| Section | Parameter | Required | Example |
|---|---|---|---|
| Area | Region | Yes | The region of the Elastic Compute Service (ECS) instances created from the scaling configuration. The default value is the same as that of the scaling group. You do not need to configure this parameter. |
|   | Zone | Yes | The zone of the ECS instances created from the scaling configuration. |
| Deploym ent Set | Deployment Set | No | The deployment set of the ECS instances created from the scaling configuration. You can also click Create Deployment Set to create a deployment set. For more information, see the Create a deployment set topic in ECS User Guide. |

s

| Security Group | Security Group | Yes | The security group to which the ECS instances created from the scaling configuration belong. You can configure multiple security groups. Make sure that a security group is available in the virtual private cloud (VPC) of the scaling group. You can also click Create Security Group to create a security group in the VPC of the scaling group. For more information, see the Create a security group topic in ECS User Guide. |
|---|---|---|---|
| Instance | Specificatio n | Yes | The ECS instance type. |
| Image ID | Image Type | Yes | Public Image: You can select public images that are provided by Alibaba Cloud. Public images are licensed to provide a secure and stable environment for applications deployed on ECS instances. Custom Image: You can create custom images to install software or deploy projects if you have special requirements. Shared Custom Image: You can select a shared custom image. |
| Storage | System Disk | Yes | The category and size of the system disk. The system disk is used to install the OS. Valid values: Ultra Disk, Standard SSD, Premium Performance Disk, and Standard Performance Disk. Valid values: 20 to 500. Unit: GB. |
|   | Data Disks | No | The size and category of data disks. Valid values: Ultra Disk, Standard SSD, Premium Performance Disk, and Standard Performance Disk. You can specify up to 16 data disks. The size of each data disk ranges from 20 GB to 32,768 GB. The default size is 20 GB. Note You can configure the Release with Instance and Encryption parameters for each data disk based on your business requirements. |
|   | Set Password | Yes | Specify when to set the password. You can select Custom Password or Later. If you select Later, you must set the password in the ECS console after the ECS instance is created. For more information, see the Change an instance logon password topic in ECS User Guide. |

| to Scaling |   |   |   |
|---|---|---|---|
| Password |   |   |   |
|   | Logon Password | No | If you set the Set Password parameter to Custom Password, you must enter a password for logging on to the ECS instance. The principle that governs the logon password setting varies based on the image type you use. For more information about how to set a logon password, see the Change an instance logon password topic in ECS User Guide. Important The password is used for logon purposes and is not equivalent to the VNC password. |
|   | Confirm Password | No | Enter the password again for confirmation. |
| Basic Informati on | Scaling Configuratio n Name | No | The name of the scaling configuration. |
|   | Instance name | No | The name of the ECS instance that you want to create based on the scaling configuration. |
|   | Custom Data Format | No | The Windows OS supports batch and PowerShell scripts. Before you perform Base64 encoding on user data, make sure that the first line of the data is included in [bat] or [powershell] . The Linux OS supports shell scripts. |
| Advanced Configur ation Show | Hostname | No | The hostname used in the OS of the ECS instance. |
|   | Instance RAM Role | No | After you attach an instance RAM role to an ECS instance, the ECS instance inherits the permissions of the RAM role. |
|   | SLB Weight | No | The weight of each ECS instance that is created from the scaling configuration after Auto Scaling attaches the ECS instances to the associated Server Load Balancer (SLB) instance. Valid values: 1 to 100. If you have specified the weight when you associate the scaling group with an SLB instance, the weight that you specified is preferentially used. |

s s

|   | Dedicated Host | No | You can specify a dedicated host and then create ECS instances on the dedicated host in the scaling group. Associated Host: If you select Associated Host, after you restart an ECS instance, the ECS instance is deployed on the current host. If you do not select Associated Host, after you restart an ECS instance, the ECS instance may be scheduled to another host within your Alibaba Cloud account. |
|---|---|---|---|

8. Click **Submit**.
After the scaling configuration is created, the scaling configuration enters the **Disabled** state and is displayed in your scaling configuration list. You can click Apply in the Operation column to enable the scaling configuration. Auto Scaling can create ECS instances only in a scaling group for which a scaling configuration is enabled. For more information, see Apply a scaling configuration. You can also modify or delete a scaling configuration based on your business requirements.

### 6.2 View scaling configurations

This topic describes how to view scaling configurations.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
The scaling groups that correspond to the specified organization, resource set, and region are displayed.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Instance Configuration Sources** tab.
6. View scaling configurations.
On the Scaling Configuration Sources tab, you can view information about the scaling configurations such as instance families, images, system disk categories, data disks, and status.

### 6.3 Modify a scaling configuration

This topic describes how to modify a scaling configuration. You can modify the information about a scaling configuration based on your business requirements.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Instance Configuration Sources** tab.
6. Find the scaling configuration that you want to modify and click its name in the **Scaling**
s
**Configuration Name/ID** column.
7. Modify the information about the scaling configuration.
For more information about the parameters of the scaling configuration, see Create a scaling configuration.
8. Click **Submit**.

### 6.4 Apply a scaling configuration

This topic describes how to apply a scaling configuration. You can create multiple scaling configurations for a scaling group and apply one of the scaling configurations based on your business requirements.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Instance Configuration Sources** tab.
6. Find the scaling configuration that you want to apply and click **Apply** in the **Actions**
column. You can put only one scaling configuration into the **Enable** state in a scaling group. After you apply a scaling configuration, other scaling configurations in the scaling group enter the **Disable** state.
7. Click **OK**.

**Result**

The status of the scaling configuration changes from **Disable** to **Enable** in the **Status** column.

### 6.5 Delete a scaling configuration

This topic describes how to delete a scaling configuration that you no longer require. After you delete a scaling configuration, Elastic Compute Service (ECS) instances that are created based on the scaling configuration are retained in the scaling group.

**Prerequisites**

The scaling configuration is in the **Disable** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Instance Configuration Sources** tab.
6. Find the scaling configuration that you want to delete and click **Delete** in the **Actions**
column.
7. Click **OK**.

## 7 Scaling activities

### 7.1 View scaling activity details

You can view scaling activity details to check the results of scaling activities triggered by scheduled jobs, alarm tasks, or manual execution of scaling rules.

**Background information**

The possible statuses of a scaling activity include **Rejected**, **Executing**, **Successful**,
**Partially Successful**, and **Failed**. For scaling activities in the **Rejected**, **Partially**
**Successful**, or **Failed** status, check the cause and status information in detail.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target scaling group and click the name of the scaling group in the **Scaling Group**
**Name/ID** column.
5. On the scaling group details page, click the **Scaling Activities** tab to view scaling activity
details. You can view the ID, total number of instances after the change, start time, end time, description and cause, status information, and activity status for each scaling activity.

### 7.2 Resolve scaling activity exceptions

**exceptions**

An ongoing scaling activity may be interrupted by some unexpected factors. This topic describes how to resolve scaling activity exceptions.

**Exception description**

A scaling activity may be in one of the following states: **Rejected**, **Executing**, **Successful**,
**Partially Succeeded**, and **Failed**. If a scaling activity enters the **Rejected**, **Partially**
**Succeeded**, or **Failed** state, an exception occurs. You can find the scaling activity on which
an exception occurred on the **Scaling Activities** tab and view the **Description/Reason** to resolve the exception.

**Solutions**

An exception occurs when a scaling activity enters the **Rejected**, **Failed**, or **Partially**
**Succeeded** state. You can use one of the following solutions to resolve the exception:
**DIY troubleshooting**: On the Auto Scaling console, find the scaling activity on which an
exception occurred and check the **Description/Reason** column or the **Status**
**Information** column to do the troubleshooting. For more information, see View the details
of a scaling activity.
**Technical support**: If the exception persists after you complete the DIY troubleshooting,
submit a ticket to ask for technical support.

## 8 Scaling rules

### 8.1 Create a scaling rule

A scaling rule specifies the specific action performed in a scale-out or scale-in. The execution of a scaling rule triggers a scaling activity or enables the automatic adjustment of the boundary values of a scaling group. For example, you can create a scaling rule to add one instance to a scaling group. This topic describes how to create a scaling rule.

**Background information**

You can create only a limited number of scaling rules for a scaling group. For information about the scaling rule quota, see the **Limits** topic in the **Notes** chapter of Auto Scaling Use r Guide. If the addition or removal of a specific number of instances causes the total number of instances in a scaling group to drop below the designated lower limit or exceed the designated upper limit, Auto Scaling automatically adjusts the number of instances to be added or removed. This ensures that the total number of instances in the scaling group maintains between the lower and upper limits.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target scaling group and click the name of the scaling group in the **Scaling Group**
**Name/ID** column.
5. On the details page of the scaling group, click the **Scaling Rules** tab.
6. Click **Create Scaling Rule**.
7. In the **Create Scaling Rule** dialog box, configure parameters based on your business
requirements. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Rule Name | Yes | The name of the scaling rule. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must _ start with a letter or a digit. |

| Scaling Activity | Yes | The following actions are supported: To N Units: changes the number of instances in the scaling group to N. Add N Units: adds N instances to the scaling group. Add N%: adds the specified percentage of instances to the scaling group. Remove N Units: removes N instances from the scaling group. Remove N%: removes the specified percentage of instances from the scaling group. Important Up to 500 instances are supported in the following actions: To N Units, Add N Units, and Remove N Units. If you specify a number greater than 500 in one of the actions, an error is reported. If you want to perform one of the following actions during a scaling activity, the number of instances added or removed in the action is 500 at most: To N Units, Add N%, and Remove N%. |
|---|---|---|
| Default Cooldown (Seconds) | Yes | The cooldown period after a scaling activity is complete. Valid values: 0 to 86400. Default value: 20. |

8. Click **OK**.

**Result**

On the **Scaling Rules** tab, you can view the settings of the following parameters of the created scaling rule: **Scaling Rule ID/Name**, **Scaling Rule Type**, **Executed At**, and
**Actions**. You can also click **Execute**, **Edit**, or **Delete** in the **Operation** column of the scaling
rule based on your business requirements.

### 8.2 View scaling rules

This topic describes how to view scaling rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
The scaling groups that belong to the specified organization, resource set, and region are displayed.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Scaling Rules** tab.
6. View scaling rules.
On the Scaling Rules tab, you can view information about the scaling rules, such as the scaling rule IDs, rule types, and actions that are specified in the rules.

**What to do next**

On the Scaling Rules tab, you can manage the scaling rules. For example, you can click Edit, Execute, or Delete in the **Actions** column. For more information, see the following topics:

### 8.3 Modify a scaling rule

This topic describes how to modify a scaling rule. You can modify the information about a scaling rule, such as the rule name, action that is specified in the rule, and cooldown time.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Scaling Rules** tab.
6. Find the scaling rule that you want to modify and click **Edit** in the **Actions** column.
7. Modify the rule name and change the action that you want to perform and the cooldown
time based on your business requirements.
8. Click **OK**.

### 8.4 Execute a scaling rule

This topic describes how to manually execute a scaling rule.

**Prerequisites**

The scaling group for which the scaling rule is created is in the **Enable** state. No scaling activity is in progress in the scaling group for which the scaling rule is created.

**Background information**

If the total number of instances in a scaling group is out of the specified range after a scaling rule is executed, Auto Scaling creates or removes a specific number of instances to keep the total number within the specified range. Auto Scaling allows you to manually execute scaling rules. You can also associate scaling rules with scheduled tasks or event-triggered tasks to enable auto scaling. For information about how to create scheduled tasks and event-triggered tasks, see Create scheduled tasks and Create an event-triggered task.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Scaling Rules** tab.
6. Find the scaling rule that you want to execute and click **Execute** in the **Actions** column.
7. Click **OK**.

**Result**

On the **Scaling Activity** tab, a scaling activity is generated. You can view the execution status of the scaling activity.

### 8.5 Delete a scaling rule

This topic describes how to delete a scaling rule that you no longer require.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the details page of the scaling group, click the **Scaling Rules** tab.
6. Find the scaling rule that you want to delete and click **Delete** in the **Actions** column.
7. Click **OK**.

## 9 Scheduled tasks

### 9.1 Create scheduled tasks

If your business workloads have specific patterns, you can create scheduled tasks to prepare sufficient computing resources for peak-hours or release idle computing resources during offpeak hours. This ensures your business continuity at a minimum resource cost. This topic describes how to create scheduled tasks for a scaling group.

**Background information**

A scheduled task is a predefined task that triggers the automatic execution of a scaling rule at the specified point in time. It ensures an automatic scaling of computing resources to fulfill your business demands at a minimum cost. You can specify a time window for a scheduled task to repeatedly run at the specified point in time. This enhances the adaptability of the scheduled task and effectively addresses the demands of your business. If multiple scheduled tasks need to be complete within one minute, Auto Scaling will execute the most recent scheduled task.

**Note**

Before you create a scheduled task, make sure that a scaling group and scaling rule are created. For more information, see Create scaling groups and Create a scaling rule.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Event-driven Tasks > Timed tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, click **Create Scheduled Task**.
5. In the **Create Scheduled Task** dialog box, configure parameters based on your business
requirements. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Name | Yes | The name of the scheduled task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must start _ with a letter or a digit. |
| Description | No | The description of the scheduled task. |
| Organization/Resou rce Set | Yes | The organization and resource set in which you want to create the scheduled task. |
| Start From | Yes | The point in time at which you want to execute the scheduled task. |

| Scaling Group/Scaling Rule | Yes | The scaling group for which you want to create the scheduled task and the scaling rule that you want to specify in the scheduled task. |
|---|---|---|
| Retry Expiry Time (Seconds) | Yes | The time window within which Auto Scaling can retry the scheduled task upon failure. Valid values: 0 to 1800. Default value: 600. If Auto Scaling fails to execute the scheduled task at the specified point in time, Auto Scaling retries the scheduled task during the timeout window. |
| Recurrence Interval Settings (Advanced) | No | Specifies whether to execute the scheduled task on a recurring schedule. After you select Recurrence Interval Settings (Advanced), you must configure the Recurrence Interval and Expired At parameters. Recurrence Interval: You can select By Day, By Week, or By Month. Expired At: You can click Select Date to specify the end time of the recurrence interval. |

6. Click **OK**.

**Result**

After you create a scheduled task, you can view the values of the following parameters of the scheduled task on the **Scheduled Tasks** page: **Scheduled Task Name/ID**, **Scaling**
**Group/Scaling Rule**, **Status**, **Start From**, and **Retry Expiry Time**. You can also click **Edit**,
**Disable**, or **Delete** in the **Operation** column of the scheduled task based on your business
requirements.

### 9.2 View scheduled tasks

This topic describes how to view scheduled tasks.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
The scheduled tasks that correspond to the specified organization, resource set, and region are displayed.
4. Enter a scheduled task name or ID and click **Search**.
You can select multiple filter options to narrow down the search results.

| Filter option | Description |
|---|---|
| Scheduled Task Name | You can search for a scheduled task by name. |

| Scheduled Task ID | You can search for a scheduled task by ID. |
|---|---|

5. View scheduled tasks.
On the **Scheduled Tasks** page, you can view information about scheduled tasks, such as scheduled task IDs, organizations, resource sets, scaling rules that are specified in scheduled tasks, and task status.

**What to do next**

On the **Scheduled Tasks** page, you can manage a specific scheduled task. You can click
**Edit**, **Disable**, **Enable**, or **Delete** in the **Operation** column of the scheduled task that you
want to manage.

### 9.3 Modify a scheduled task

This topic describes how to modify a scheduled task. You can modify the information about a scheduled task, such as the scheduled task name and description, point in time at which the scheduled task is executed, resource for which the scheduled task is created, scaling rule that is specified in the scheduled task, and timeout period during which Auto Scaling can retry the scheduled task.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, find the scheduled task that you want to modify and click
**Edit** in the **Actions** column.
5. Modify the information about the scheduled task.
If you select Recurrence Interval Settings (Advanced) when you create the scheduled task, you can modify the Recurrence Interval and Expires At settings. However, you cannot clear Recurrence Interval Settings (Advanced). For more information about other parameter settings, see Create scheduled tasks.
6. Click **OK**.

### 9.4 Disable a scheduled task

This topic describes how to disable a scheduled task that you no longer require.

**Prerequisites**

The scheduled task is in the **Running** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, find the scheduled task that you want to disable and click
**Disable** in the **Actions** column.
5. In the message that appears, click **OK**.

**Result**

The status of the scheduled task changes from **Running** to **Stop** in the **Status** column.

### 9.5 Enable a scheduled task

This topic describes how to enable a scheduled task. You can enable a scheduled task that is in the Stop state. This way, Auto Scaling automatically executes the scheduled task at the specified point in time.

**Prerequisites**

The scheduled task is in the **Stop** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, find the scheduled task that you want to enable and click
**Enable** in the **Actions** column.
5. In the message that appears, click **OK**.

**Result**

The status of the scheduled task changes from **Stop** to **Running** in the **Status** column.

### 9.6 Delete a scheduled task

This topic describes how to permanently delete a scheduled task that you no longer require.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Scheduled Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Scheduled Tasks** page, find the scheduled task that you want to delete and click
**Delete** in the **Actions** column.
5. In the message that appears, click **OK**.

## 10 Event-triggered tasks

### 10.1 Create an event-triggered task

**task**

This topic describes how to create an event-triggered task. If your business workloads are unpredictable or may surge unexpectedly, you can create an event-triggered task. You must specify a metric that is monitored by CloudMonitor in an event-triggered task. After you create and enable an event-triggered task, Auto Scaling collects data for the specified metric in real time and CloudMonitor triggers an alert when the specified condition is met. Then, Auto Scaling executes the scaling rule that is associated with the event-triggered task to scale instances in your scaling group.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, click **Create Event-triggered Task**.
5. In the Create Event-triggered Task dialog box, configure the parameters. The following
table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Task Name | Yes | The name of the event-triggered task. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). The name _ must start with a letter or a digit. |
| Description | No | The description of the event-triggered task. |
| Organization/Res ource Set | Yes | The organization and the resource set in which you want to create the event-triggered task. |
| Monitoring Resource/Scaling Rule | Yes | The scaling group for which you want to create the event- triggered task and the scaling rule that you want to specify in the event-triggered task. |
| Monitor Type | Yes | Valid value: System Monitoring. |
| Metric | Yes | The metric that you want to specify in the event-triggered task. Valid values: Average CPU Usage Memory Usage Outbound Traffic over Internal Network Inbound Traffic over Internal Network Average System Load |

| Statistical Period | Yes | The period during which data is collected, aggregated, and analyzed. The shorter the period, the more frequently the alert is triggered. Unit: Minutes. Valid values: 1 2 5 15 |
|---|---|---|
| Statistical Method | Yes | The rule that determines whether to trigger an alert. Select Average, Max Capacity, or Min Capacity, and specify a threshold. For example, you can specify one of the following rules to trigger an alert when the CPU utilization exceeds 80%: Average: triggers an alert when the average CPU utilization of all instances in the scaling group exceeds 80%. Max Capacity: triggers an alert when the highest CPU utilization among all instances in the scaling group exceeds 80%. Min Capacity: triggers an alert when the lowest CPU utilization among all instances in the scaling group exceeds 80%. |
| Trigger Alert After {1} Times | Yes | The number of consecutive times that the threshold must be exceeded before the alert is triggered. Valid values: 1 2 3 5 |

6. Click **OK**.

**Result**

On the Event-triggered Tasks page, the event-triggered task that you created appears. You can view the information about the event-triggered task, such as the monitoring type, statistical period, alert condition, and task description.

### 10.2 View event-triggered tasks

This topic describes how to view event-triggered tasks.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
The event-triggered tasks that correspond to the specified organization, resource set, and region are displayed.
4. Enter an event-triggered task name or ID and click **Search**.
You can select multiple filter options to narrow down the search results.

| Filter option | Description |
|---|---|

| Event-triggered Task Name | You can search for an event-triggered task by name. |
|---|---|
| Scaling Group ID | You can search for an event-triggered task by scaling group ID. |

### 10.3 Modify an event-triggered task

**task**

If an existing event-triggered task no longer meets your business requirements, you can modify the parameter settings of the event-triggered task, without the need to create a new task. For an existing event-triggered task, you can modify the following parameters: Task Name, Description, Scaling Rule, and Metric.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Event-driven Tasks > Alert Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, find the event-triggered task that you want to
modify and click **Edit** in the **Actions** column.
5. In the Edit Event-triggered Task dialog box, modify the parameter settings based on your
business requirements. For more information about the parameters of event-triggered tasks, see Create an eventtriggered task. Take note that you cannot modify the following parameters:

**Organization/Resource Set**

**Monitoring Resource**

**Monitoring Type**

6. In the Execute Scaling Rule message, click **OK**.

### 10.4 Disable an event-triggered task

**task**

This topic describes how to disable an event-triggered task. You can disable an eventtriggered task that you no longer require.

**Prerequisites**

The event-triggered task is in the **Normal** or **Insufficient Data** state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, find the event-triggered task that you want to
disable and click **Disable** in the **Actions** column.
5. In the message that appears, click **OK**.

### 10.5 Enable an event-triggered task

**task**

This topic describes how to enable an event-triggered task. You can enable an eventtriggered task that is in the Disable state. This way, Auto Scaling continues to collect data of the metric that is specified in the event-triggered task and the scaling activity that is based on the event-triggered task can be triggered when the specified conditions are met.

**Prerequisites**

The event-triggered task is in the Disable state.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, find the event-triggered task that you want to enable
and click **Enable** in the **Actions** column.
5. In the message that appears, click **OK**.

### 10.6 Delete an event-triggered task

**task**

This topic describes how to permanently delete an event-triggered task that you no longer require.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, choose **Scaling Tasks > Event-Triggered Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Event-triggered Tasks** page, find the event-triggered task that you want to delete
and click **Delete** in the **Actions** column.
5. In the message that appears, click **OK**.
n feature

## 11 Enable the notification feature

**feature**

### 11.1 Create event notification rules

**rules**

Auto Scaling's event notification feature sends notifications to CloudMonitor when specific events occur. This topic describes how to set up event notification rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Notification Settings** tab.
6. Click **Create Notification Rule**.
7. In the **Create Notification Rule** dialog box, configure the following parameters based on
your business requirements.

| Parameter | Required | Example |
|---|---|---|
| Notification Method | Yes | Set the value to CloudMonitor. This ensures that users are notified of events via CloudMonitor. |
| Event Notification Type | Yes | You can select one or more of the following events: Scale-out Activity Successful Scale-in Activity Successful Scale-out Activity Failed Scale-in Activity Failed Scaling Activity Denied Scale-out Activity Started Scale-in Activity Started Scheduled Task Expiration Scale-out Activity Partially Successful Scale-in Activity Partially Successful |

8. Click **OK**.

**Results**

On the **Notification Settings** tab, you can view your newly created event notification rule, including details like the event type and notification method. n feature

### 11.2 View event notification rules

Once an event notification rule is created, you can view details like the event type and notification method on the **Notification Settings** tab. This topic describes how to view event notification rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Notification Settings** tab.
6. On the **Notification Settings** tab, view details like **Event Notification Type** and
**Notification Method**. You can also click **Delete** or **Edit** in the **Operation** column to
manage event notification rules. For more information about how to manage event notification rules, see the following topics:

### 11.3 Edit event notification rules

This topic describes how to edit event notification rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Notification Settings** tab.
6. Find the event notification rule you want to edit and click **Edit** in the **Operation** column.
7. In the **Edit Notification Rule** dialog box, modify the following parameters based on your
business requirements.

| Parameter | Required | Description |
|---|---|---|
| Notification Method | Yes | Set the value to CloudMonitor. This ensures that users are notified of events via CloudMonitor. |

n feature

| Event Notification Type | Yes | You can select one or more of the following events: Scale-out Activity Successful Scale-in Activity Successful Scale-out Activity Failed Scale-in Activity Failed Scaling Activity Denied Scale-out Activity Started Scale-in Activity Started Scheduled Task Expiration Scale-out Activity Partially Successful Scale-in Activity Partially Successful |
|---|---|---|

8. Click **OK**.

### 11.4 Delete event notification rules

**rules**

This topic describes how to delete event notification rules.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Scaling Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the name of the scaling group in the **Scaling Group Name/ID** column.
5. On the scaling group details page, click the **Notification Settings** tab.
6. Find the event notification rule you want to delete and click **Delete** in the **Operation**
column.
7. In the message that appears, click **Delete**.
gs

## 12 Manage operation logs

### 12.1 View operation logs

On the **Operation Logs** page, you can view operation events, operators, and operation names. This topic describes how to view operation logs and their details.
1. Log on to the Auto Scaling console.
2. In the left-side navigation pane, click **Operation Logs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Operation Logs** page, search for operation logs by using the following filters and
click **Search**.

| Filter | Description |
|---|---|
| Resource Type | You can select Auto Scaling Group, ESS Event-triggered Task, or Scheduled Tasks. |
| Event Type | Follow the on-screen instructions to select one of the following types of events: Query Events Create Events Modify Events Delete Events |
| Time Range | You can specify a time range to filter operation logs. |
| Resource ID | You can filter operation logs by resource ID to view specific resource activity. |
| IP Address | You can filter operation logs by the host IP address that initiated the operation. |
| Read/Write Type | You can filter operation logs by read or write action. |
| Operation Result | You can filter operation logs by operation result. |
| Keywords | You can filter operation logs by event ID, resource ID, source IP address, or operation name. |

5. View the operation details.
gs On the **Operation Logs** page, find the operation log you want to view and click **View** in the **Details** column. In the **View Operation Details** panel, you can view parameters such as **Operator**, **Operation Name**, **IP Address**, and **Instance Details**.
