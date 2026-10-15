---
title: "Auto Scaling Product Introduction 20250728"
product_version: "V3.18.6"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Auto Scaling Product Introduction 20250728.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BC%B9%E6%80%A7%E4%BC%B8%E7%BC%A9%20ESS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Auto%20Scaling%20Product%20Introduction%2020250728.pdf"
converter: line-classifier (PyMuPDF)
---

# Auto Scaling Product Introduction 20250728

## Auto Scaling

Auto Scaling is a service that automatically adjusts computing capacity (the number of ECS instances) as needed and policies. You can configure scaling policies to automatically increase the number of instances to ensure sufficient computing capacity when business demands grow, and automatically reduce the number of instances to save costs when business demands decrease. Auto Scaling is a free service that offers advantages such as automation, cost reduction, high availability (HA), flexible intelligence, and log recording. Auto Scaling helps you automatically adjust the number of instances and is suitable for applications with fluctuating business volumes along with applications with stable business volumes.

### Product details

Auto Scaling is a management service that dynamically adjusts the number of computing resources (ECS) based on your actual business load. Auto Scaling automatically increases the number of ECS instances to ensure sufficient computing capacity when business demands grow, and automatically decreases the number of ECS instances to reduce costs when business demands decline. The core concepts of Auto Scaling are as follows:

**Scaling group**

Scaling groups are the core unit of Auto Scaling. Instances in a scaling group are of the same type and can be used in similar business scenarios. If you have different business scenarios, you can create multiple scaling groups. Auto Scaling adjusts the number of instances in each scaling group based on your configurations and business requirements. You must specify the minimum number of instances that must be included and the maximum number of instances that is allowed for your scaling groups. You must also associate your scaling groups with SLB instances and RDS instances.

**Scaling configuration source**

Scaling configuration source defines the instance configuration information. The instance configuration source is the instance configuration template used when the scaling group scales out ECS instances. During automatic scale-out, the scaling group creates ECS instances based on the instance configuration source and adds the created instances to the scaling group. You can specify a launch template or scaling configuration as your scaling configuration source. You can specify a launch template only for scaling groups that contain ECS instances. You can have only one active scaling configuration source in your scaling group at a time. If you apply a new scaling configuration source to your scaling group, the current scaling configuration source becomes invalid.

**Scaling rule**

Scaling rules define specific scaling operations, such as adding or removing N ECS instances. The purpose of a scaling rule varies based on its type. You can use a scaling rule to trigger a scaling activity or adjust the maximum and minimum numbers of instances for a scaling group. Auto Scaling supports step scaling rules, predictive scaling rules, target tracking scaling rules, and simple scaling rules. Predictive scaling rules can be used to predict future metric values based on historical monitoring data. These rules can automatically adjust the maximum and minimum numbers of instances in scaling groups. Step scaling rules, target tracking scaling rules, and simple scaling rules can be used to add or remove instances.

**Scaling activity**

When you execute a scaling rule or manually add instances to or remove instances from a scaling group, a scaling activity is triggered. A scaling activity describes an event in which the number of ECS instances in a scaling group changes, the maximum or minimum number of instances that are allowed in a scaling group changes, or the expected number of instances in a scaling group changes. After a scaling activity is triggered, Auto Scaling automatically completes all scale-out and scale-in operations.

**Automatic task triggering**

In a scaling task, Auto Scaling executes a specific scaling rule. Auto Scaling supports scheduled and event-triggered tasks.
**Scheduled task**: If your business loads have specific patterns, such as periodic peak hours
and off-peak hours, you can create scheduled tasks to manage your business loads in the Auto Scaling console. Through scheduled tasks, you can scale resources at specified times, preparing sufficient computing resources before peak hours arrive or releasing idle computing resources after peak hours.
**Event-triggered task**: If your business loads do not have specific patterns or are
unpredictable, scheduled tasks may not meet your business needs. Auto Scaling supports event-triggered tasks that dynamically scale resources based on specified monitoring metrics, providing more flexible ways to trigger scaling rules. During peak hours, Auto Scaling executes event-triggered tasks to add instances to scaling groups to alleviate business pressure. During off-peak hours, Auto Scaling executes event-triggered tasks to release instances from scaling groups to reduce production costs.

### Benefits

Compared with manually managing ECS instances, Auto Scaling effectively reduces infrastructure and operations and maintenance costs. Auto Scaling provides the following benefits: automation, cost-effectiveness, high availability, intelligence, and easy audit.

**Automation**

Auto Scaling automatically scales out or scales in instances in your scaling group based on your configurations. This prevents the issues that are caused by manual operations. Auto Scaling integrates with Server Load Balancer (SLB) and ApsaraDB RDS. This allows Auto Scaling to automatically add instances to or remove instances from the backend servers of the SLB instances that are associated with your scaling group. Auto Scaling can also automatically add the private IP addresses of ECS instances to the whitelists of the ApsaraDB RDS instances that are associated with your scaling group.

**Cost reduction**

Auto Scaling provisions resources when demand increases and releases resources when demand decreases. This improves resource utilization and significantly reduces costs. For example, Auto Scaling automatically adjusts the number of instances as needed. Auto Scaling automatically adds ECS instances during peak hours and automatically removes excess instances during off-peak hours. You do not need to invest substantial time and manpower to adjust the number of instances. Auto Scaling automatically scales instances, which reduces infrastructure and manpower costs and saves time.

**High availability**

Auto Scaling monitors the instances in your scaling group in real time. Auto Scaling automatically replaces unhealthy instances with new instances to ensure high availability of your business. This effectively prevents business interruptions caused by unavailable ECS instances.

**Intelligence**

Auto Scaling supports various scaling modes, such as fixed-number mode, health mode, scheduled mode, dynamic mode, and custom mode. You can combine the scaling modes to configure scaling policies that meet your business requirements. Compared with manual operation, Auto Scaling lets you scale instances in a more intelligent and efficient manner.

**Easy audit**

Auto Scaling logs the details of each scaling activity that is triggered. This facilitates troubleshooting. Auto Scaling also integrates with CloudMonitor. You can use CloudMonitor to monitor instances in scaling groups. You do not need to repeatedly check the status of multiple ECS instances. This helps you quickly understand the overall capacity of your business.

### Scenarios

Auto Scaling is suitable for a wide range of applications, whether they have constantly fluctuating or stable workloads.

**Business scenarios with regular peaks and valleys**

**Scenario example**

A government service system needs to handle high access pressure from 9:00 AM to 5:00 PM every day. Between 5:00 PM and 9:00 AM the next day, the access volume decreases significantly, eliminating the need to maintain high-load resource configurations.

**Solution**

To address these predictable and regular business fluctuations, you can use **scheduled**
**scaling policies**. By configuring **scheduled tasks** in the scaling group, you can
automatically increase the number of ECS instances at 9:00 AM every day to ensure system performance, and automatically reduce the number of ECS instances at 5:00 PM. This effectively reduces resource costs while meeting business requirements.

**Scenario example**

A flood prevention system may receive many flood information reporting requests in a short period during sudden extreme weather conditions such as heavy rain, causing a sharp increase in access load. If scaling is not performed in time, the system may crash. Manual scaling cannot meet real-time response requirements, which may lead to delays in flood warning.

**Solution**

To address these sudden and unpredictable business peaks, you can use **dynamic scaling**
**policies**. By configuring alert tasks based on load metrics (such as average **CPU**
**utilization, total request volume**) in the scaling group, when the cluster load reaches
the preset threshold, the number of ECS instances automatically increases to ensure stable system operation and maintain good response capabilities. After the load drops back to a safe range, resources are automatically reduced, achieving efficient and stable resource utilization.

**Business scenarios that require guaranteed instance numbers**

**Scenario example**

An internal management system for government services needs to operate 24/7, with access volume remaining relatively stable throughout the time period, without obvious peak or valley periods. If the existing computing resources suddenly fail, manual intervention may not repair the fault in time.

| Feature |  | Description |
|---|---|---|
| Scaling policies | Scheduled scaling | A scheduled task is a predefined action that automatically triggers a scaling rule at a specified time. It enables cost-efficient, automated scaling of computing resources to meet your business needs. You can configure a scheduled task to run repeatedly within a defined time window, increasing adaptability and ensuring it aligns with your business requirements. If multiple scheduled tasks must be completed within one minute, Auto Scaling will prioritize and execute the latest one. |
|  | Dynamic scaling | If your workloads are unpredictable or prone to sudden surges, you can configure an event-triggered task in Auto Scaling to dynamically adjust resources. You must define a CloudMonitor metric that will be tracked in real time. Upon detecting the alert, Auto Scaling automatically executes the associated scaling rule, adding or removing instances in your scaling group to match demand. |
|  | Manual scaling | You can manually run a scaling rule to add or remove instances anytime. |
|  | Suspending scaling operations | Auto Scaling supports suspending ongoing scaling operations. |
|  | Scaling based on ECS metrics | Auto Scaling supports scaling operations based on Elastic Compute Service (ECS) metrics. |
|  | Scaling based on non-ECS metrics | Auto Scaling supports scaling operations based on non-ECS metrics. |
| DDH cluster scaling |  | Auto Scaling supports scaling of dedicated hosts. |
| Max. number of instances |  | The highest number of ECS instances allowed in a scaling group. Configure this based on your business needs to manage costs effectively. Value range: 0 to 1000. |

**Solution**

Using the **elastic self-healing** mechanism of the scaling group, the system regularly checks the running status of ECS instances. If abnormalities occur, it creates new instances to replace the abnormal ones in a timely manner, ensuring business stability.

### Features

| Min. number of instances | The smallest number of ECS instances allowed in a scaling group. Configure this based on your business needs to maintain normal operations. Value range: 0 to 1000. |
|---|---|
| Expected number of instances | After this feature is enabled, Auto Scaling automatically maintains the desired instance count. The scaling group also supports parallel scaling operations. |
| Instance removal policy | Auto Scaling removes ECS instances in two phases: first, it removes instances based on the earliest-added, most recently-added, or earliest scaling configuration criteria; if further removals are needed, it repeats the same selection process on the remaining instances. Otherwise, the process stops after the initial phase. |
