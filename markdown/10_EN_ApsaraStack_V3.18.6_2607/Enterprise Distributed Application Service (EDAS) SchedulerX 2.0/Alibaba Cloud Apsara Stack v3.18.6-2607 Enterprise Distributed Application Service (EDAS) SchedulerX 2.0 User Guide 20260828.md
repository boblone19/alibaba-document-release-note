---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 139
source_pdf: "96760cba07596ff6_Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%20EDAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Enterprise%20Distributed%20Application%20Service%20%28EDAS%29%20SchedulerX%202.0%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 User Guide 20260828

## Table of Contents

- 1 Distributed Task Scheduling Platform SchedulerX 2.0
- 2 Quick Start
  - 2.1 Log on to the Apsara Uni-manager Management Console
  - 2.2 Log on to the SchedulerX console
  - 2.3 Get the domainName for SchedulerX
  - 2.4 Connect clients to SchedulerX
    - 2.4.1 Integrate a Java application with SchedulerX 2.0
    - 2.4.2 Integrate a Spring application with SchedulerX 2.0
    - 2.4.3 Integrate a Spring Boot application with SchedulerX 2.0
  - 2.5 Create standalone script tasks using an agent
  - 2.6 Adapt to IPv6 access
  - 2.7 Client release history
    - 2.7.1 Java SDK
- 3 Scheduling and triggers
  - 3.1 Timed scheduling
  - 3.2 Workflow scheduling
  - 3.3 API trigger
  - 3.4 Backfill data
  - 3.5 Second-level scheduling
- 4 Task types
  - 4.1 Java tasks
  - 4.2 Script tasks
  - 4.3 HTTP tasks
- 5 Distributed programming model
  - 5.1 Standalone
  - 5.2 Broadcast
  - 5.3 Map model
  - 5.4 MapReduce model
  - 5.5 Multi-language sharding models
- 6 Console user guide
  - 6.1 Overview
  - 6.2 Execution List
  - 6.3 Task List
  - 6.4 Workflow Management
  - 6.5 Application Management
  - 6.6 Operation records
- 7 Advanced features
  - 7.1 Create a second-level scheduling task
  - 7.2 Create a new account
  - 7.3 How to pass data between upstream and downstream nodes in a workflow
- 8 Configuration reference
  - 8.1 JobContext parameters
  - 8.2 Advanced configuration parameters for task management
  - 8.3 SchedulerxWorker configuration parameters
- 9 Permission management
  - 9.1 Overview of permission management
  - 9.2 Create users and user groups
  - 9.3 Create a role and attach permissions
  - 9.4 Verify logon permissions
  - 9.5 Verify application-level permissions
- 10 FAQ
  - 10.1 FAQ
  - 10.2 Alert FAQ

buted Task Scheduling Platform SchedulerX 2.0

## 1 Distributed Task Scheduling Platform SchedulerX 2.0

**Scheduling Platform**

**SchedulerX 2.0**

SchedulerX 2.0 is Alibaba Group's next-generation Distributed Task Scheduling Platform, built on the Akka architecture. It supports timed scheduling, workflow task orchestration, and distributed batch scheduling. It delivers high reliability, manages massive task volumes, and schedules tasks in seconds. You configure and manage your timed scheduling tasks in the console. You query task execution records and operational logs. You orchestrate tasks and pass data using workflows. SchedulerX 2.0 provides a simple, easy-to-use distributed programming model. With just a few lines of code, you can distribute large data volumes across multiple machines for execution.

## 2 Quick Start

### 2.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the service domain name for the Apsara Uni-
manager Management Console and press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. Enter your username and password.

> **Note:** You can obtain the username and logon password from an operations administrator.
> If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.

3. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement.

> The **Product Service Agreement**, **Privacy Agreement**, and **User** **Agreement** are displayed only if they have been published. If none of these agreements are published, you can skip this step.

4. Click **Account Logon** or **Authorized Logon**.

> **Note:** The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".

5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of
the following scenarios:

> **Note:** When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.

**Related operations**

**Forgot password**

1. If you forget your logon password, click **Forgot Password** below the password field.
2. On the Forgot Password page, enter your **Account Name** and **Email Address**, complete
the Captcha, and then click **Confirm**.

> **Note:** For Account Name, enter your username. For Email Address, enter the email address that you used to create the account.
> A password reset link is sent to your email address. Open the link to reset your password.

### 2.2 Log on to the SchedulerX console

**console**

This topic describes how to log on to the Distributed Task Scheduling Platform.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the service domain name for the Apsara Uni-
manager Management Console and press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. Enter your username and password.

> **Note:** You can obtain the username and logon password from an operations administrator.
> If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.

3. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement.

> The **Product Service Agreement**, **Privacy Agreement**, and **User** **Agreement** are displayed only if they have been published. If none of these agreements are published, you can skip this step.

4. Click **Account Logon** or **Authorized Logon**.

> **Note:** The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".

5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of
the following scenarios:

> **Note:** When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.
6. In the top navigation bar, choose **Products > Middleware > Microservice Tools And**
**Platforms > SchedulerX** to open the SchedulerX console.
7. Click the floating **Switch Account** icon in the lower-right corner, and then select
**Organization Settings** and **Region Settings**.
8. Click **Access With Administrator Permissions** or **Access With Role-based**
**Authorization** to open the **Overview** page.

> **Note:** If you are an administrator, click **Access With Administrator Permissions**. If you are not an administrator, click **Access With Role-based Authorization**.

### 2.3 Get the domainName for SchedulerX

**SchedulerX**

The domainName is required when connecting a client or an agent to SchedulerX. This topic describes how to obtain the domainName for SchedulerX from the console.

**Procedure**

**Apsara Basic O&M console (new)**

1. Log on to the Apsara Basic O&M console.
2. In the navigation pane on the left, click **Resource Management > Product & Cluster**
**O&M**.
3. On the **Product & Cluster O&M** page, enter `schedulerx2Cluster` in the
**Product|Cluster** search box. In the Action column of the target cluster, click **Cluster**
**Details**.
4. On the **Resource Details** tab of the **Cluster Details** page, find the **Resource** whose
**Name** is **schedulerx2_console_domain**, and click the link in the **Resource Request**
**Result** column.
5. In the **Resource Request Result** dialog box, obtain the domainName for SchedulerX 2.0
and record it.

**Apsara Basic O&M console (old)**

1. Log on to the Apsara Basic O&M console.
2. In the left navigation pane, under **Cluster**, enter
`schedulerX2Cluster` and click the search icon. Hover over the icon to the right of the target cluster, and then click **Dashboard**.
3. In the **Cluster Resources** section of the **Cluster Dashboard** page, find the App whose
**Name** is **schedulerx2_console_domain**, right-click the value in its **Result** column, and
select **Show More**.
4. In the **Details** dialog box, obtain the domainName for SchedulerX 2.0 and record it.
The **domain** value is the domainName for SchedulerX 2.0.

### 2.4 Connect clients to SchedulerX

#### 2.4.1 Integrate a Java application with SchedulerX 2.0

**SchedulerX 2.0**

Integrate SchedulerX 2.0 with your Java application to enable distributed task scheduling.

**Prerequisites**

You have created a resource. For more information, see Application management.

**Procedure**

The process of integrating task scheduling capabilities into an application involves the following steps:
1. Create an application group.
2. Integrate the client with SchedulerX 2.0.

> **Note:** SchedulerX uses at-least-once scheduling semantics. You must implement idempotence as needed. For example, if a worker for a distributed task goes down or is disconnected from the network, a failover is triggered. The tasks that were running on that worker might be executed again.

**Step 1: Create an application group**

SchedulerX 2.0 uses application groups to isolate resources and manage task scheduling. You must create an application group and use its **GroupID** and **AppKey** as configuration parameters to integrate your application with the task scheduler.

> **Note:** To prevent resource waste, a group in SchedulerX 2.0 supports a maximum of 1,000 tasks (Jobs) by default.

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, click **Create**.
4. In the **Create Application** panel, on the **Basic Configurations** tab, configure the
following parameters and click **Next**.

| Parameter | Description | Default value |
|---|---|---|
| Applicatio n Name | A custom name for the application. | None |
| Group ID | The Group ID for the application. The value must be unique in the system. Otherwise, the creation fails. | None |
| Descriptio n | A custom description. | None |
| Load5 Threshold | The value cannot exceed the number of available CPU cores on the client machine. | 0 |
| Memory Usage | The average memory usage of the process in the last 5 minutes cannot be greater than this threshold. Otherwise, the client machine is considered busy. | 90% |

| Disk Usage | The disk usage cannot be greater than this value. Otherwise, the client machine is considered unhealthy and busy. | 95% |
|---|---|---|
| Trigger Busy Machines | Specifies whether to continue triggering client execution when a machine is busy. | Open |
| Throttling | Specifies whether to enable throttling. If you enable this feature, you must set Concurrent Task Instances. | Off |
| Concurren t Task Instances | If throttling is enabled, this is the maximum number of task instances that can run concurrently for an application. Task instances that exceed this limit are not discarded. They are placed in an application- level task queue to wait for execution. | None |
| Maximum Tasks | The maximum number of tasks that a group can have. The value cannot exceed 1,000. | None |
| Calendar | Import a custom calendar. You can set scheduled tasks to run on specified dates to meet specific business requirements. | None |

5. In the **Create Application** panel, on the **Notifications** tab, select an **Alert Method**, add
**Alert Contacts**, and then click **Submit**.

| Configuration Item | Description | Example |
|---|---|---|
| Alert Method | DingTalk Email | DingTalk |
| Add Alert Contact | Enter the Nickname, Email, and DingTalk Access token. _ | None |

After the application group is created, you are redirected to the **Application Management** page. Verify that the application group exists and obtain its **Group ID** and **AppKey**.

**Step 2: Integrate the Java application with SchedulerX 2.0**

Integrate task scheduling into your application by performing the following steps:
1. Initialize SchedulerxWorker.
2. Create a new class to implement task scheduling.
3. Add the SchedulerxWorker dependency to the pom.xml file of your application.

```xml
  <dependency>
    <groupId>com.aliyun.schedulerx</groupId>
    <artifactId>schedulerx2-worker</artifactId>
    <version>${schedulerx2.version}</version>
        <!-- If you use logback, you must exclude log4j and log4j2. -->
        <exclusions>
          <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
          </exclusion>
          <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
          </exclusion>
          <exclusion>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
          </exclusion>
    </exclusions>
  </dependency>
```

> **Note:** To obtain the latest version of the SchedulerX 2.0 client, see Client release history.

4. Initialize SchedulerxWorker in the main function.

```
/**
    * Initializes the SchedulerX client.
    * @throws Exception if the initialization fails.
```

`*/`

```java
   private static void initSchedulerxWorker() throws Exception {
     String groupId = "schedulerx-server.defaultGroup";
     String appKey = "jdslfjsdkflka****==";
     SchedulerxWorker schedulerxWorker = new SchedulerxWorker();
     // Set the domain name.
     schedulerxWorker.setDomainName(${domainName});
     // If your application is deployed in EDAS, you need to configure the namespace.
     schedulerxWorker.setNamespace("system_namespace");
     schedulerxWorker.setGroupId(groupId);
     // For versions later than 1.1.0, you must set the AppKey.
     schedulerxWorker.setAppKey(appKey);
     schedulerxWorker.init();
     LOGGER.info("SchedulerxWorker init success. groupId={}", groupId);
```

`}`

**Note**

For additional configuration options when initializing the SchedulerxWorker client, see SchedulerxWorker configuration parameters.
5. Create a new class to implement the scheduled task.
In your application, add a class named `JobProcessor` to implement task scheduling. This example implements a simple task that periodically prints "hello world". The following code shows the `JobProcessor` class:

```java
package com.alibaba.armon.test.processor.demo; import com.alibaba.schedulerx.worker.domain.JobContext; import com.alibaba.schedulerx.worker.processor.JavaProcessor; import com.alibaba.schedulerx.worker.processor.ProcessResult; import org.springframework.stereotype.Component; @Component public class HelloWorldProcessor extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("hello world");
        return new ProcessResult(true);
```

`}` `}`

**Verify the result**

After you complete the integration, you can verify it in the console.
1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, find the group that you created and click
**Connected Machines** in the **Actions** column.
If the integration is successful, a list of machines is displayed. If the integration fails, a message that indicates no active machines are available is displayed. Java application

> **Note:** You can also check the SchedulerX client logs in the ${user.home}/logs/schedulerx directory. The worker.log file contains the core runtime logs of the SchedulerX client, which include records of exceptions and other runtime events.

**What to do next**

Based on the hello world example in Integrate a Java application with SchedulerX 2.0, create a scheduled task in the console. For the **Processor Class Name** parameter, enter the full path of the JobProcessor, for example, `com.alibaba.armon.test.processor.demo.HelloWorldProcessor` . For more information, see Create a scheduling task.

> **Note:** Cron expressions do not support second-level granularity. To schedule tasks at the second level, use second_delay.

#### 2.4.2 Integrate a Spring application with SchedulerX 2.0

**SchedulerX 2.0**

You can use SchedulerX 2.0 to add distributed task scheduling capabilities to standalone Spring applications.

**Prerequisites**

The resource has been created. For more information, see Application Management.

**Procedure**

The procedure to add task scheduling capabilities to an application is as follows:
1. Create an application group.
2. Integrate the client with SchedulerX 2.0.

> **Note:** SchedulerX provides at-least-once scheduling semantics. You must implement idempotence in your application. For example, if a worker for a distributed task goes down or loses its network connection, a failover is triggered. Tasks that were running on that worker may be executed again.

**Step 1: Create an application group**

SchedulerX 2.0 uses application groups to isolate resources and manage task scheduling. You must create an application group and use its **GroupID** and **AppKey** as configuration parameters to integrate your application with the task scheduler.

> **Note:** To prevent resource waste, a group in SchedulerX 2.0 supports a maximum of 1,000 tasks (Jobs) by default.

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, click **Create**.
4. In the **Create Application** panel, on the **Basic Configurations** tab, configure the
following parameters and click **Next**.

| Parameter | Description | Default value |
|---|---|---|
| Applicatio n Name | A custom name for the application. | None |
| Group ID | The Group ID for the application. The value must be unique in the system. Otherwise, the creation fails. | None |
| Descriptio n | A custom description. | None |
| Load5 Threshold | The value cannot exceed the number of available CPU cores on the client machine. | 0 |
| Memory Usage | The average memory usage of the process in the last 5 minutes cannot be greater than this threshold. Otherwise, the client machine is considered busy. | 90% |
| Disk Usage | The disk usage cannot be greater than this value. Otherwise, the client machine is considered unhealthy and busy. | 95% |
| Trigger Busy Machines | Specifies whether to continue triggering client execution when a machine is busy. | Open |
| Throttling | Specifies whether to enable throttling. If you enable this feature, you must set Concurrent Task Instances. | Off |
| Concurren t Task Instances | If throttling is enabled, this is the maximum number of task instances that can run concurrently for an application. Task instances that exceed this limit are not discarded. They are placed in an application- level task queue to wait for execution. | None |
| Maximum Tasks | The maximum number of tasks that a group can have. The value cannot exceed 1,000. | None |
| Calendar | Import a custom calendar. You can set scheduled tasks to run on specified dates to meet specific business requirements. | None |

5. In the **Create Application** panel, on the **Notifications** tab, select an **Alert Method**, add
**Alert Contacts**, and then click **Submit**.

| Configuration Item | Description | Example |
|---|---|---|

| Alert Method | DingTalk Email | DingTalk |
|---|---|---|
| Add Alert Contact | Enter the Nickname, Email, and DingTalk Access token. _ | None |

After the application group is created, you are redirected to the **Application Management** page. Verify that the application group exists and obtain its **Group ID** and **AppKey**.

**Step 2: Integrate a Spring application with SchedulerX 2.0**

To integrate task scheduling into your application, complete the following steps:
1. Initialize SchedulerxWorker.
2. Create a class to implement task scheduling.
3. Add the SchedulerxWorker dependency to the application's pom.xml file.

```xml
  <dependency>
    <groupId>com.aliyun.schedulerx</groupId>
    <artifactId>schedulerx2-worker</artifactId>
    <version>${schedulerx2.version}</version>
        <!-- If you use logback, exclude log4j and log4j2. -->
        <exclusions>
          <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
          </exclusion>
          <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
          </exclusion>
          <exclusion>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
          </exclusion>
    </exclusions>
  </dependency>
```

> **Note:** To obtain the latest version of the SchedulerX 2.0 client, see Client release notes.

4. Initialize SchedulerxWorker in the XML configuration file by injecting the bean.

```xml
  <bean id="schedulerxWorker" class="com.alibaba.schedulerx.worker.SchedulerxWorker"
init-method="init">
    <!-- Set the domainName. -->
    <property name="domainName">
      <value>${domainName}</value>
    </property>
    <!-- If the application is deployed in EDAS, you must configure the namespace.-->
    <property name="namespace">
      <value>system_namespace</value>
    </property>
    <property name="groupId">
      <value>${groupId}</value>
    </property>
    <!-- For versions 1.1.0 and later, you must set the AppKey. -->
    <property name="appKey">
       <value>${appKey}</value>
    </property>
  </bean>
```

> **Note:** All JobProcessors must be configured as beans. For example, add the @Component annotation.

5. Create a class to implement the scheduling task.
Add a `JobProcessor` class to the application to implement task scheduling. This section describes how to implement a simple timed task that prints "hello world". The following code shows the JobProcessor:

```java
package com.alibaba.armon.test.processor.demo; import com.alibaba.schedulerx.worker.domain.JobContext; import com.alibaba.schedulerx.worker.processor.JavaProcessor; import com.alibaba.schedulerx.worker.processor.ProcessResult; import org.springframework.stereotype.Component; @Component public class HelloWorldProcessor extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("hello world");
        return new ProcessResult(true);
```

`}` `}`

**Verify the result**

After you complete the integration, you can verify it in the console.
1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, find the group that you created and click
**Connected Machines** in the **Actions** column.
If the integration is successful, a list of machines is displayed. If the integration fails, a message that indicates no active machines are available is displayed. Java application

> **Note:** You can also check the SchedulerX client logs in the ${user.home}/logs/schedulerx directory. The worker.log file contains the core runtime logs of the SchedulerX client, which include records of exceptions and other runtime events.

**What to do next**

Based on the "hello world" example in Integrate a Spring application with SchedulerX 2.0, create a timed scheduling task in the console. For the **Processor Class Name** parameter, enter the full path of the JobProcessor class, such as `com.alibaba.armon.test.processor.demo.HelloWorldProcessor` . For more information, see Create a scheduling task.

> **Note:** Cron expressions do not support second-level precision. To schedule tasks by the second, use second_delay.

#### 2.4.3 Integrate a Spring Boot application with SchedulerX 2.0

**with SchedulerX 2.0**

Use SchedulerX 2.0 to add distributed task scheduling capabilities to a standalone Spring Boot application.

**Prerequisites**

An existing Spring Boot project.

**Procedure**

The workflow to integrate task scheduling capabilities into an application consists of the following steps:
1. Create an application group.
2. Integrate the client with SchedulerX.

> **Note:** SchedulerX uses at-least-once scheduling semantics. Make your tasks idempotent to handle repeated executions. For example, if a worker goes down or is disconnected, a failover is triggered. Tasks that were running on the worker might be executed again.

**Step 1: Create an application group**

SchedulerX 2.0 uses application groups to isolate resources and manage task scheduling. You must create an application group and use its **GroupID** and **AppKey** as configuration parameters to integrate your application with the task scheduler.

> **Note:** To prevent resource waste, a group in SchedulerX 2.0 supports a maximum of 1,000 tasks (Jobs) by default.

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, click **Create**.
4. In the **Create Application** panel, on the **Basic Configurations** tab, configure the
following parameters and click **Next**.

| Parameter | Description | Default value |
|---|---|---|
| Applicatio n Name | A custom name for the application. | None |
| Group ID | The Group ID for the application. The value must be unique in the system. Otherwise, the creation fails. | None |
| Descriptio n | A custom description. | None |
| Load5 Threshold | The value cannot exceed the number of available CPU cores on the client machine. | 0 |
| Memory Usage | The average memory usage of the process in the last 5 minutes cannot be greater than this threshold. Otherwise, the client machine is considered busy. | 90% |
| Disk Usage | The disk usage cannot be greater than this value. Otherwise, the client machine is considered unhealthy and busy. | 95% |

| Trigger Busy Machines | Specifies whether to continue triggering client execution when a machine is busy. | Open |
|---|---|---|
| Throttling | Specifies whether to enable throttling. If you enable this feature, you must set Concurrent Task Instances. | Off |
| Concurren t Task Instances | If throttling is enabled, this is the maximum number of task instances that can run concurrently for an application. Task instances that exceed this limit are not discarded. They are placed in an application- level task queue to wait for execution. | None |
| Maximum Tasks | The maximum number of tasks that a group can have. The value cannot exceed 1,000. | None |
| Calendar | Import a custom calendar. You can set scheduled tasks to run on specified dates to meet specific business requirements. | None |

5. In the **Create Application** panel, on the **Notifications** tab, select an **Alert Method**, add
**Alert Contacts**, and then click **Submit**.

| Configuration Item | Description | Example |
|---|---|---|
| Alert Method | DingTalk Email | DingTalk |
| Add Alert Contact | Enter the Nickname, Email, and DingTalk Access token. _ | None |

After the application group is created, you are redirected to the **Application Management** page. Verify that the application group exists and obtain its **Group ID** and **AppKey**.

**Integrate the Spring Boot application with SchedulerX 2.0**

To integrate task scheduling into your application, follow these steps:
1. You can initialize SchedulerxWorker.
2. You can create a class to implement the scheduling task.
3. Add the SchedulerxWorker dependency to the pom.xml file of your application.

```xml
<dependency>
    <groupId>com.aliyun.schedulerx</groupId>
    <artifactId>schedulerx2-spring-boot-starter</artifactId>
    <version>${schedulerx2.version}</version>
    <!-- If you use logback, exclude log4j and log4j2. -->
    <exclusions>
      <exclusion>
        <groupId>org.apache.logging.log4j</groupId>
          <artifactId>log4j-api</artifactId>
      </exclusion>
      <exclusion>
        <groupId>org.apache.logging.log4j</groupId>
          <artifactId>log4j-core</artifactId>
      </exclusion>
      <exclusion>
        <groupId>log4j</groupId>
        <artifactId>log4j</artifactId>
      </exclusion>
      </exclusions>
</dependency>
```

> **Note:** To obtain the latest version of the SchedulerX 2.0 client, see Client release notes.

4. Add the **GroupID** and **AppKey** of your group to the `application.properties` file.

```bash
# Specify the domain name without http://.
spring.schedulerx2.domainName=xxx.xxx.xxx
# If the application is deployed in EDAS, configure the namespace.
spring.schedulerx2.namespace=system_namespace
# Find the GroupID in Application Management.
spring.schedulerx2.groupId=app1.defaultGroup
# For versions 1.1.0 and later, set the AppKey. Find the AppKey in Application Manage
ment. spring.schedulerx2.appKey=sfhdsfhdjshdgf****==
```

> **Note:** All JobProcessors must be set as beans. For example, add the `@Component` annotation.

Parameter descriptions:

| Key | Description | Value | Supp orted from versi on |
|---|---|---|---|

| spring.schedulerx2.enabled | Specifies whether to enable the SchedulerX 2.0 starter. It is enabled by default and does not need to be configured. | `true` or `false`. Default value: `true`. | 0.1.7 |
|---|---|---|---|
| spring.schedulerx2.groupId | The group ID. | None | 0.1.7 |
| spring.schedulerx2.domain Name | The domain name of the environment. | None | All |
| spring.schedulerx2.enable Units | The whitelist for unit isolation. Separate multiple units with commas (,). Do not include spaces. SchedulerxWorker worker = new SchedulerxWorker(); // Enable only in the center and zbyun units. worker.setEnableUnites("center ,zbyun"); | None | 0.1.7 |
| spring.schedulerx2.disable Units | The blacklist for unit isolation. Separate multiple units with commas (,). Do not include spaces. If a whitelist is set, the whitelist takes precedence and the blacklist is ignored. SchedulerxWorker worker = new SchedulerxWorker(); // Isolate the center unit. worker.setDisableUnites("cente r"); | None | 0.1.7 |
| spring.schedulerx2.enableS ites | The whitelist for data center isolation. Separate multiple data centers with commas (,). Do not include spaces. SchedulerxWorker worker = new SchedulerxWorker(); // Enable only in the na61 and na62 data centers of the center unit. worker.setEnableSites("center. na61,center.na62"); | None | 0.1.7 |

| spring.schedulerx2.disable Sites | The blacklist for data center isolation. Separate multiple data centers with commas (,). Do not include spaces. If a whitelist is set, the whitelist takes precedence and the blacklist is ignored. SchedulerxWorker worker = new SchedulerxWorker(); // Isolate the na61 data center of the center unit. worker.setDisableUnites("cente r.na61"); | None | 0.1.7 |
|---|---|---|---|
| spring.schedulerx2.enableB atchWork | Specifies whether to enable grid computing. This parameter is enabled by default. If you do not use grid computing, do not configure this parameter. If you use grid computing, enable this parameter. Otherwise, the first trigger on each machine is delayed by at least 20 seconds. | `true` or `false`. Default value: `true`. | 0.1.7 |
| spring.schedulerx2.host | If the client has multiple network interface cards (NICs) or is in a VPN environment, the automatically obtained local IP address might be incorrect. Use this parameter to specify the correct IP address. | None | 0.1.7 |
| spring.schedulerx2.port | The custom listener port for the SchedulerX client. If not set, a random available port is selected by default. | None | 0.1.7 |
| spring.schedulerx2.appKey | The AppKey that corresponds to the GroupID. You can obtain it from the Application Management page in the console. | None | 1.1.0 |
| spring.schedulerx2.blockAp pStart | Specifies whether to block the application from starting if SchedulerX fails to initialize. | `true` or `false`. Default value: `true`. | 1.1.0 |
| spring.schedulerx2.shareCo ntainerPool | Specifies whether all task executions on the client share a thread pool. | `true` or `false`. Default value: `false`. | 1.2.1. 3 |
| spring.schedulerx2.sharePo olSize | If you enable a shared thread pool, you can customize its size. | Default value: 64. | 1.2.1. 3 |

| spring.schedulerx2.label | Set labels for different clients. In Task Management, you can specify labels for task execution. Common scenarios include grayscale releases and stress testing. | None | 1.2.2. 4 |
|---|---|---|---|
| spring.schedulerx2.enableC groupMetrics | Specifies whether to use cgroups to collect metrics for client instances. You must manually enable this in container environments such as Kubernetes (K8s). | `true` or `false`. Default value: `false`. | 1.2.2. 4 |
| spring.schedulerx2.cgroupP athPrefix | The cgroup path within the container. | The default path is /sys/fs/cgroup/cp u/. If this path exists, you do not need to set this parameter. | 1.2.2. 4 |
| spring.schedulerx2.enable HeartbeatLog | Specifies whether to print heartbeat logs to ${user.home}/logs/schedulerx/heartb eat.log. | `true` or `false`. Default value: `true`. | 1.2.4. 3 |
| spring.schedulerx2.mapMa sterStatusCheckInterval | The frequency in milliseconds at which the Map model checks whether all subtasks are complete. You can set this parameter to increase the scheduling frequency for second-level tasks. | 3000 | 1.2.5 |
| spring.schedulerx2.enableS econdDealyCycleIntervalMs | Sets the unit of the `second delay` to _ milliseconds. If you set this parameter to `true`, the second-level delay configured in the console becomes a millisecond-level delay. This can increase the scheduling frequency. | `true` or `false`. Default value: `false`. | 1.2.5 |

5. Create a class that implements the scheduling task.
Add a class that implements `JobProcessor` to your application. The following example shows a simple `JobProcessor` that prints "hello world" at a scheduled time:

```java
package com.alibaba.armon.test.processor.demo; import com.alibaba.schedulerx.worker.domain.JobContext; import com.alibaba.schedulerx.worker.processor.JavaProcessor; import com.alibaba.schedulerx.worker.processor.ProcessResult; import org.springframework.stereotype.Component; @Component public class HelloWorldProcessor extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("hello world");
        return new ProcessResult(true);
```

`}` `}`

**Verify the result**

After you complete the integration, you can verify it in the console.
1. Log on to the SchedulerX console.
2. In the navigation pane on the left, choose **Application Management**.
3. On the **Application Management** page, find the group that you created and click
**Connected Machines** in the **Actions** column.
If the integration is successful, a list of machines is displayed. If the integration fails, a message that indicates no active machines are available is displayed. Java application

> **Note:** You can also check the SchedulerX client logs in the ${user.home}/logs/schedulerx directory. The worker.log file contains the core runtime logs of the SchedulerX client, which include records of exceptions and other runtime events.

**What to do next**

Create a timed scheduling task in the console based on the "hello world" example in Integrate a Spring Boot application with SchedulerX 2.0. For the **Processor Class** parameter, enter the full path of the JobProcessor, such as `com.alibaba.armon.test.processor.demo.HelloWorldProcessor` . For more information, see Create a scheduling task.

> **Note:** Cron expressions do not support second-level precision. To schedule tasks at the second level, use the second_delay parameter.

### 2.5 Create standalone script tasks using an agent

**using an agent**

You can use an agent to create standalone Shell, Python, and Go script tasks.

**Prerequisites**

Ensure that the Java Runtime Environment (JRE) is version 1.8 or later.

**Background information**

To run only script tasks, such as Shell, Python, and Go tasks, you can download the SchedulerX agent and start it on your client. Then, you can create a script task in the console and add the script content. The agent automatically schedules the script to run on the client.

**Download the agent**

You can download the agent in two ways: Enter the agent download URL in the address bar of your browser. Run the **wget** command on the client machine to download the agent. If your machine has a public IP address, run the following command to download the agent:

> **Note:** X.X.X is a placeholder for the version number. Replace this placeholder with the required version number, such as 1.12.5.

```
wget https://schedulerx2.oss-cn-hangzhou.aliyuncs.com/agent/schedulerxAgent-X.X.X.tar
```

| Version | Download URL | Release notes |
|---|---|---|

| Agent 1.12.5 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.12.5.tar | New features: Supports obtaining task system variables using placeholders. Supports custom thread pool sizes for HTTP tasks. Allows script tasks to return the last line of standard output as the execution result. |
|---|---|---|
| Agent 1.11.5 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.11.5.tar | Fixed issues: Fixed security vulnerabilities in Netty and Logback. Fixed the "too old resource version" issue for Kubernetes (K8s) tasks. |
| Agent 1.10.13 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.10.13.tar | New features: Supports deploying multiple agents on one machine. Supports responses larger than 1,000 bytes for HTTP agent tasks. Optimized logs to reduce historical log storage. |
| Agent 1.10.5 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.10.5.tar | New features: Supports graceful shutdown. Simple Log Service supports isolation by application group. |
| Agent 1.9.8 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent-1.9.8.tar | New features: Supports HTTP tasks in agent mode. Supports returning the last line of the log after a script task fails. Supports K8s tasks. |
| Agent 1.7.10 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.7.10.tar.gz | Fixed issues: Fixed the issue where second-level tasks run slowly. Fixed an issue where Simple Log Service might cause an out-of-memory (OOM) error. |
| Agent 1.4.2 | https://schedulerx2.oss-cn- hangzhou.aliyuncs.com/age nt/schedulerxAgent- 1.4.2.tar.gz | New feature: Supports Simple Log Service. |

**Run the agent**

1. Decompress the downloaded package.
2. Go to the schedulerxAgent/conf directory, edit the agent.properties file, and configure the
**GroupID** and **AppKey** parameters.

```bash
# The domain name. Do not add the http:// prefix.
domainName=
# The ID of the application group.
groupId=
# The AppKey of the application group.
appKey=
```

3. Go to the schedulerxAgent/bin directory and run **start-1g.sh**.
You can also run **start-2g.sh**, **start-4g.sh**, or **start-8g.sh**, depending on the task payload and machine configuration.

> **Note:** You can also view the SchedulerX client logs. The log path is ${user.home}/logs/schedulerx. The worker.log file is the core runtime log for the SchedulerX client. It records all runtime activities, including exceptions.

**Verify the result**

After you start the agent, check the ${user.home}/schedulerx/worker.log file. The agent has started successfully if the log contains the message Schedulerx Worker started.

**Stop the agent**

To stop the agent, go to the schedulerxAgent/bin directory and run **stop.sh**.

### 2.6 Adapt to IPv6 access

SchedulerX 2.0 supports IPv4/IPv6 dual-stack communication for the console, server, and worker components.

**Operation Guide**

**Prepare Client Programs**

For example, in a Spring Boot project, import the following POM dependencies:

```xml
<dependency>
     <groupId>com.aliyun.schedulerx</groupId>
     <artifactId>schedulerx2-spring-boot-starter</artifactId>
     <version>${verison}</version>
</dependency>
```

> **Note:** The version used in this document is 1.13.1-ipv6-SNAPSHOT, published to the EDAS Maven repository.

**Upgrade SchedulerX2 Server-side**

1. Log on to the Apsara Infrastructure Management console.
2. In the Apsara Uni-manager Operations Console, from the top menu bar, select **Platform**
**O&M > Apsara Infrastructure Management > Resource Management**.
3. In the navigation pane on the left, click **Resource Management > Product Cluster**
**O&M**. In the **Product | Cluster** search box, enter Schedulerx to search.
4. In the list of search results, click **Cluster Details** next to the destination cluster.
5. On the Cluster Details page, click the **Desired State Configuration** tab. To enable the
IPv6 feature, configure kv.conf and tag.conf as follows: `"vip_protocols": "ipv4+ipv6"` .

**Worker IPv6 Access**

1. You have created an application. For more information, see Application Management.
2. Package and upload the Worker program to an IPv6-enabled machine. Configure the
Worker's `application.yaml` file and place it in the same directory as the program. For information about obtaining the `domainName` in the configuration, see Obtain SchedulerX DomainName. On the **Application Management** page, obtain the values for `groupId` and `appKey` . For more information, see Application Management.

```
spring:
  schedulerx2:
    domainName: <your domainName>
    groupId: <your groupId>
    appKey: <your appKey>
```

> **Note:** By default, Spring Boot applications read the application.yaml file in the current program directory as the configuration file.

3. Start the program. To enable IPv6 networking, add `-Djava.net.preferIPv6Addresses=true`
to the command line parameters. Replace `demo.jar` with your actual program name.

```
java -Djava.net.preferIPv6Addresses=true -jar demo.jar
```

After startup, the logs in the log directory display IPv6 addresses.

**Validate Results**

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Application Management**.
3. On the **Application Management** page, in the **Actions** column, click **Connect Machine**
to query machine IP information.

### 2.7 Client release history

This topic provides the release notes for the SchedulerX client SDK.

#### 2.7.1 Java SDK

This topic describes the updates for the SchedulerX Java software development kit (SDK), which include new features, optimizations, and important bug fixes for each release.

| Version | Change type | Feature description | Release date | References |
|---|---|---|---|---|

| 1.13.1 | Bug fix | Fixed an issue where heartbeats were registered and reported prematurely in scenarios with Spring parent-child containers. Fixed an issue where Map tasks would stop abnormally during an upgrade from an earlier version to the new SDK. | July 28, 2025 | None |
|---|---|---|---|---|
| 1.13.0 | New feature | Added support for link encryption. For applications in the Professional Edition, sensitive data is encrypted during communication between the server and the client. | June 18, 2025 | None |
| 1.12.7 | Optimiz ation | Refactored the placeholder logic for script tasks to resolve placeholder replacement failures caused by Spring conflicts. Upgraded the Spring version to 5.3.31 to fix security vulnerabilities. | May 29, 2025 | None |
|   | Bug fix | Fixed an issue where automatic retries for failed subtasks were not supported for shard 0 in broadcast tasks and sharded tasks. Fixed an issue where context retrieved an incorrect triggerType when a visualized MapReduce task was manually rerun. |   | None |
| 1.12.5 | Optimiz ation | Optimized Spring tasks to be compatible with scenarios where other components implement TaskScheduler. | February 8, 2025 | None |

|   |   |   | Added support for configuring the SDK log directory. Add the startup command - Dschedulerx.log.path=log root p _ _ ath. The final path is {schedulerx.log.path}/logs/s chedulerx . Added support for overwriting the default Logback configuration for SDK framework logs. You can also output logs to your own Simple Log Service (SLS) repository. You can write to your own Logstore using SLS configurations. |   | January 3, 2025 | None |
|---|---|---|---|---|---|---|
|   |   |   |   | {schedulerx.log.path}/logs/s |   |   |
|   |   |   | chedulerx |   |   |   |
|   | 1.12.3 | New feature |   |   |   |   |
|   |   | Optimiz ation | Optimized Spring tasks to be compatible with Spring 6.x. Fixed an H2 `DriverClass Not Found` exception that occurred when the driver class was not configured for the application Java Database Connectivity (JDBC). Fixed an issue where Map tasks failed due to concurrency problems during status checks. |   |   |   |

| Version | Chang e type | Feature description | Release date | References |
|---|---|---|---|---|
| 1.12.2 | Optimiz ation | Fixed security vulnerabilities in visualized MapReduce tasks. Fixed security vulnerabilities in some Akka interfaces. | November 20, 2024 | None |
| 1.12.1 | New feature | Added support for custom thread pool sizes for HTTP agent tasks. Added support for custom loggers for SchedulerX logs. Added the @SchedulerX annotation. This annotation can work with the Spring @Scheduled annotation to take over some of the Spring scheduled tasks. | October 12, 2024 | None |
|   | Optimiz ation | Removed the fastjson package to fix security vulnerabilities. |   | None |

| 1.11.5 | Optimiz ation | Optimized the log output of SLS. Fixed an issue where heartbeat reporting was affected when multiple application groups failed to read configurations. Reduced the number of fault- tolerant retries for heartbeat timeout exceptions. | June 17, 2024 | None |
|---|---|---|---|---|
| 1.11.4 | New feature | JobContext can now get the workflow ID. | March 20, 2024 | For more information, see JobContext parameter description. |
|   | Optimiz ation | Reduced the SDK size by removing unused dependencies. Removed the unused Log4j2.xml file from the SDK to prevent log configuration conflicts. |   | None |
| 1.11.1 | New feature | Added support for getting task parameters from environment variables. | February 20, 2024 | None |
|   | New feature | Added support for application-level isolation. |   | None |
|   | Bug fix | Fixed Netty security vulnerabilities. Fixed Logback security vulnerabilities. Fixed an issue where SchedulerX framework logs were not displayed due to log conflicts. |   | None |
|   | New feature | Added support for graceful shutdown. Before an application stops, it waits for all running tasks to complete. This ensures that no services are interrupted during release and restart. |   | None |
|   | New feature | Added support for configuring the distribution rate of subtasks. |   | None |

|   |   |   |   |   |   | For more information, see Connect a Spring Boot application to SchedulerX 2.0. None None None None |
|---|---|---|---|---|---|---|
|   |   |   | Added support for configuring a user and password. spring.schedulerx2.h2DatabaseU ser : Sets the user for the built-in H2 database. spring.schedulerx2.h2DatabaseP assword : Sets the password for the built-in H2 database. |   |   |   |
|   |   |   |   | spring.schedulerx2.h2DatabaseU |   |   |
|   |   | New | ser |   |   |   |
|   |   | feature |   |   |   |   |
|   |   |   |   | spring.schedulerx2.h2DatabaseP |   |   |
|   |   |   | assword |   |   |   |
|   | 1.10.14 |   |   |   |   |   |
|   |   | Optimiz ation | Added support for isolation by application group. |   |   |   |
|   |   | Optimiz ation | Added support for distribution sorted by worker IP address. |   |   |   |
|   |   | Optimiz ation | Added support for earlier versions of Spring 4. The timed method for Spring tasks now supports any return value. |   |   |   |
|   |   | Optimiz ation | Prevents the creation of duplicate heartbeat threads when the Spring container is reinitialized. Added support for automatic restarts when an Akka Actor terminates unexpectedly. |   |   |   |

|   | Bug fix | Fixed an issue where an exception was returned immediately after Spring failed to read a processor bean. Fixed an issue introduced in version 1.10.x where Map tasks would get stuck. Fixed an issue where a task instance could not be terminated after the preProcess method of a broadcast task failed to execute. Fixed an issue where a task timeout alert was triggered by residual threads when a task instance terminated abnormally. Fixed an issue where task status could be lost and tasks could get stuck after an application started in shared thread pool mode. Fixed a configuration loading exception that occurred when multiple application groups or appKeys contained special characters. Fixed an issue where Professional Edition features for visualized Map tasks could not be used. |   | None |
|---|---|---|---|---|

| Version | Chang e type | Feature description | Release date | References |
|---|---|---|---|---|
| 1.9.6 | New feature | Added support for standard and custom templates. Standard template: You can modify the image and image pull policy. Custom template: Compatible with native Kubernetes content. The schedulerx2-plugin-kubernetes must be version 1.0.5 or later. | July 4, 2023 | None |
|   | New feature | Map tasks now support starting distribution from a random position. To enable this, set the spring.schedulerx2.mapMasterDispatc hRandom parameter to true . The default value is `false`. |   | None |
| 9 |   |   | > Document V |   |

|   |   |   |   |   |   |   |   | None None None None None |
|---|---|---|---|---|---|---|---|---|
|   |   |   | New feature | Shell tasks now support common built- in system parameters. `schedule.timestamp`: The time when the task is scheduled. `data.timestamp`: The data timestamp for the scheduling. |   |   |   | None |
|   |   |   |   | Adjusted the execution thread model. The model is switched to the non- shared thread pool mode. Parameters for the shared thread pool model. spring.schedulerx2.shareCont ainerPool=true : Enables the shared thread pool. spring.schedulerx2.sharePool Size=32 : The global size of the shared thread pool. Default: 64. spring.schedulerx2.sharePool QueueSize=20480 : The queue size of the shared thread pool. Default: `Integer.MAX VALUE`. _ |   |   |   | None |
|   |   |   |   |   |   | spring.schedulerx2.shareCont |   |   |
|   |   |   | New | ainerPool=true |   |   |   |   |
|   |   |   | feature |   |   |   |   |   |
|   |   |   |   |   |   | spring.schedulerx2.sharePool |   |   |
|   |   |   |   | Size=32 |   |   |   |   |
|   |   |   |   |   |   | spring.schedulerx2.sharePool |   |   |
|   |   |   |   | QueueSize=20480 |   |   |   |   |
|   |   |   |   | The following parameters are added. spring.schedulerx2.broadcastMa sterExecEnable=false : Specifies whether the master node participates in broadcast task execution. Default: true. spring.schedulerx2.broadcastDi spatchRetryTimes=5 : The number of retry attempts for broadcast distribution. |   |   |   | None |
|   |   |   |   |   | spring.schedulerx2.broadcastMa |   |   |   |
|   |   |   |   | sterExecEnable=false |   |   |   |   |
|   |   |   | New feature |   |   |   |   |   |
|   |   |   |   |   | spring.schedulerx2.broadcastDi |   |   |   |
|   |   |   |   | spatchRetryTimes=5 |   |   |   |   |
|   |   |   |   |   |   |   | September 8, 2023 |   |
|   |   | 1.8.13 |   |   |   |   |   |   |
|   |   |   | Optimiz ation | Optimized the performance of Map tasks during large-scale application publishing and scale-in. |   |   |   | None |
|   |   |   | Optimiz ation | Optimized the timing of heartbeat reporting at application startup to prevent long task processing times caused by slow application container startup. |   |   |   | None |

|   | Bug fix | Fixed an issue where tasks were rejected after running for a long time in shared thread pool mode. Fixed an issue where null pointer logs occasionally appeared during task status reporting. Fixed an issue where the number of threads for broadcast tasks continuously increased in versions later than 1.7.x. Fixed a memory leak in shared thread pool mode. Fixed an issue where dynamic proxy objects could not execute the Reduce method. Fixed an issue where acknowledgements for second-level tasks were lost during merging. Fixed an exception that occurred when Diamond read environment addresses. Fixed an issue with long heartbeat timeouts when connecting to the public cloud. Fixed alerts related to the log4j log format. Fixed an issue where standalone tasks would get stuck if a distribution exception occurred. Fixed an issue where new versions were not compatible with the `ClassName:BeanId` configuration mode. Modified the maximum file size limit for Logback standalone logs. |   | None |
|---|---|---|---|---|

| Version | Chang e type | Feature description | Release date | References |
|---|---|---|---|---|
|   | New feature | Added support for integrating native Spring scheduled tasks. Added support for integrating Tracing Analysis. |   | None |
|   | Optimiz ation | Enabled fast responses for client shutdown and offline operations. |   | None |

| nterprise Di ervice (EDA | stributed A S) | pplication | SchedulerX 2.0 | User Guide·Quic Star |
|---|---|---|---|---|
| 1.7.10 |   |   | August 30, 2022 |   |
|   | Bug fix | Fixed an out-of-memory issue caused by many SLS log outputs for high-frequency tasks. Fixed a delay issue that occurred when many second-level tasks ran concurrently. |   | None |
| 1.6.1 | Bug fix | Fixed an issue of high CPU usage by the detection thread for second-level broadcast tasks. | August 3, 2022 | None |
| 1.6.0 | New feature | Added support for integrating Kubernetes Job scheduling. | June 24, 2022 | None |
|   | Optimiz ation | Processor classes are now compatible with Spring AOP proxy configurations. Optimized the content of ERROR log messages that occasionally appeared in the monitoring timer for active workers. Added support for log collection for `second delay` tasks. _ |   | None |
| 1.5.1.1 | New feature | Added support for dynamically enabling or disabling Simple Log Service. | April 19, 2022 | None |
|   | Bug fix | Fixed an issue where version 1.5.0.x was not compatible with Spring Boot 2.0.3. Fixed a potential JobSyncService bean initialization error in version 1.5.0.x. |   |   |
| 1.5.0.2 | New feature | Added support for declarative task definitions in Spring Boot. You can declare namespaces, applications, tasks, and alerts in configuration files to manage tasks within an application. The file declarations can be modified, which lets you start applications in any environment with a single click. | April 1, 2022 | None |

|   |   |   | Visualized MapReduce tasks, formerly parallel computing, now support subtask-level lists, logs, and reruns. You can also define custom tags for subtasks and search for subtasks by tag. |   |   | None |
|---|---|---|---|---|---|---|
| 1.4.2 |   | New feature | With the log service for SchedulerX 2.0, you can view the application logs for each task scheduling, including distributed tasks, in the console by adding a Log4j or Logback configuration. No code changes are required. |   | March 7, 2022 | None |
|   |   |   | You can now view the stack of running tasks directly in the console to troubleshoot stuck tasks. To use this feature, upgrade your client to version 1.4.0 or later. |   |   | None |
|   |   |   | Added support for connecting to executors developed with ElasticJob. |   |   |   |
| 1.3.4 |   | New | Added support for DataWorks tasks. Added schedulerx2-plugin- xxljob to be compatible with Xxl- job interfaces. |   | January 6, 2022 | None |
|   |   |   |   | schedulerx2-plugin- |   |   |
|   |   | feature | xxljob |   |   |   |

|   | Version | Chang e type | Feature description |   | Release date | References |
|---|---|---|---|---|---|---|
|   | 1.3.2 | Optimiz ation | Optimized an issue by upgrading the default log4j2 dependency to version 2.15.0. |   | December 15, 2021 | None |
|   |   | New feature | Enhanced second-level standalone tasks: Second-level standalone loops now support distribution and switching between different instances. For Spring Boot applications, set the following parameter: spring.schedulerx2.enableSecondD elayStandaloneDispatch=true . The default value is false . |   |   | None |
|   |   |   |   | spring.schedulerx2.enableSecondD |   |   |
|   |   |   | elayStandaloneDispatch=true |   |   |   |

|   |   |   |   |   |   | None None None None None |
|---|---|---|---|---|---|---|
|   |   | Optimiz ation | Enabled fast responses for client shutdown and offline operations. |   |   | None |
|   | 1.3.0.3 |   |   |   | November 26, 2021 |   |
|   |   | Bug fix | Fixed an issue where instance heartbeats were reported only to the specified scheduling service when the client was connected to multiple application groups. Fixed issues with occasional thread interruptions and null pointer exceptions in second-level tasks. Fixed a compatibility issue where tasks would lock up and time out when the SchedulerX client was integrated with Spring Cloud. Fixed an issue where broadcast tasks were interrupted under concurrent conditions. Fixed an issue where the worker instance list was not regularly refreshed during the execution of second-level tasks. Fixed an issue where the scan thread did not terminate after a stop instruction was executed for a second-level broadcast task. Fixed an issue where tasks had a probability of getting stuck during batch releases of many workers in second-level broadcast task scenarios. |   |   | None |
|   | 1.2.9.1 | Bug fix | Fixed an issue where tasks would lock up and time out when the worker was integrated with Spring Cloud. |   | August 30, 2021 | None |
|   |   | New feature | Enhanced second-level standalone tasks: Second-level standalone loops now support distribution and switching between different instances. Set the parameter spring.schedulerx2.enableSecondD elayStandaloneDispatch=true . The default value is false . |   |   | None |
|   |   |   |   | spring.schedulerx2.enableSecondD |   |   |
|   |   |   | elayStandaloneDispatch=true |   |   |   |
|   |   |   |   |   | August 27, 2021 |   |
|   | 1.2.9 |   |   |   |   |   |
|   |   | Bug fix | Fixed an issue where broadcast tasks received an interrupt signal under concurrent conditions and the worker instance list was not updated. |   |   | None |

|   | 1.2.8.3 | Bug fix | Fixed an issue where the scan thread did not terminate after a stop instruction was executed for a second- level broadcast task. |   | August 13, 2021 | None |
|---|---|---|---|---|---|---|
|   | 1.2.8.2 | Bug fix | Fixed an issue where tasks had a probability of getting stuck during batch releases of many workers in second-level broadcast task scenarios. |   | August 6, 2021 | None |
|   |   |   | Enhanced broadcast tasks: The postProcess method can now get the execution status of all machines from JobContext.getTaskStatuses() and the execution results from JobContext.getTaskResults() . Broadcast sharding model: Broadcast tasks can get shardingNum and sharingId from JobContext to perform distributed data processing based on the machine's index. Enhanced sharding model: JobContext can get the total number of shards from shardingNum . |   | June 23, 2021 | None |
|   |   |   |   | JobContext.getTaskStatuses() |   |   |
|   | 1.2.8 | New feature |   |   |   |   |
|   | 1.2.7 | New feature | Added a switch to disable the failover feature. |   | April 28, 2021 | None |
|   |   | Bug fix | Fixed a potential socket leak caused by heartbeat check failures. Fixed an issue where the MapTask Master might frequently trigger false failovers when there were many subtasks. |   |   | None |
|   | 1.2.5.2 | New feature | The interval for second-level tasks now supports millisecond-level precision. |   | April 8, 2021 | None |
|   |   | Optimiz ation | In the MapReduce model, the root task is now fixed to run on the master node to simplify troubleshooting. Removed the strong dependency on log4j2. If you use Logback, you can remove the log4j and log4j2 dependencies. |   |   | None |

| 1.2.4.3 | New feature | Added support for progress reporting for running broadcast tasks. Heartbeat logs can now be disabled with a switch. | January 21, 2021 | None |
|---|---|---|---|---|
|   | Bug fix | The heartbeat interval is adjusted to 10 seconds. Fixed a critical issue where broadcast tasks could get stuck. |   | None |

|   |   | Version | Chang e type | Feature description |   | Release date | References |
|---|---|---|---|---|---|---|---|
|   |   | 1.2.3.1 | Optimiz ation | Fixed an issue where high client load could cause the persistent connection for task scheduling to fail, preventing further task scheduling. |   | December 16, 2020 | None |
|   |   |   |   | Added support for collecting the actual CPU usage of a container. You need to add configurations. For example, for a starter, add spring.schedulerx2.enableCgroupMe trics=true and spring.schedulerx2.cgroupPathP refix=/sys/fs/cgroup/cpu/ . The `cgroupPathPrefix` parameter is optional. If the container has the ` /sys/fs/cgroup/cpu/ ` path, you do not need to configure it. Otherwise, change it to the actual cgroup path. Added support for tags. You can add custom tags when the client starts. For example, for a starter, add spring.schedulerx2.labels=xxx . In task management, you can specify machines and run tasks on instances with a specific tag. This is useful for scenarios such as grayscale releases and unitization. |   |   | None |
|   |   |   |   |   | spring.schedulerx2.cgroupPathP |   |   |
|   |   |   |   | refix=/sys/fs/cgroup/cpu/ |   |   |   |
|   |   |   |   |   |   | December 10, 2020 |   |
|   |   | 1.2.2.2 | New feature |   |   |   |   |
|   |   |   |   |   | spring.schedulerx2.labels=xxx |   |   |
|   |   |   | Optimiz ation | Separated the client heartbeat thread and the Akka core thread to ensure that high application load does not affect heartbeat checks. Removed h2 from the shade. Shading h2 might cause MySQL driver loading to fail. |   |   | None |

| 1.2.1.2 | New feature | Added support for a shared ContainerPool. All tasks on the client can share the same thread pool, which greatly improves client performance and stability when scheduling many tasks with high concurrency. Shaded Scala to resolve Scala conflicts. Added support for appKey authentication for the public cloud. Enhanced the MapReduce model to support configuring whether the Reduce method is executed only after all subtasks succeed. The client now supports setting the appKey using - Dschedulerx.appKey . | October 20, 2020 | None |
|---|---|---|---|---|
|   | Optimiz ation | Optimized the client Netty thread pool. |   | None |
|   | Bug fix | Fixed an issue where broadcast tasks could get stuck. Fixed an issue where the AccessKey ID or AccessKey secret for the SLS feature could be leaked. |   | None |
| 1.2.0.2 | New feature | An application now supports more than 100,000 tasks. This feature is available only on the public cloud. Added a switch for client logs. It is enabled by default. You can now set the status when creating a task using OpenAPI. Removed dependencies on diamond-client, logger.API, and log4j. | August 19, 2020 | None |
|   | Bug fix | Fixed an issue where the client would lose connection with the server during network disconnection drills. EDAS applications could not read the AccessKey secret. |   | None |

|   | - | Oct |
|---|---|---|
| Dschedulerx.appKey |   |   |

|   | 1.1.4.REL EASE | New feature | Added support for custom namespaces. Added support for initializing multiple SchedulerxWorker instances. Enhanced the MapReduce model. The Reduce method can be executed even if a subtask fails. JobContext.getTaskStatuses can determine the status of each task. In the Map<Long, TaskStatus> struct, the key is the task ID and the value is the task status. |   | May 15, 2020 | None |
|---|---|---|---|---|---|---|
|   |   | Bug fix | A null pointer exception occurred if the result in ProcessResult was empty. Tasks would get stuck if thread- dispatcher-delivery was suspended. |   |   | None |
|   |   |   | shade protobuf and netty from AccessKey IDka , which resolves over 90% of JAR package conflicts. |   | February 10, 2020 | None |
|   |   |   |   | shade protobuf and netty from |   |   |
|   |   |   | AccessKey IDka |   |   |   |
|   | 1.1.2.REL EASE | New feature |   |   |   |   |
|   |   | Optimiz ation | AppKeys do not support multiple groups. |   |   | None |

|   |   | Map<Long, |   |
|---|---|---|---|
|   | TaskStatus> |   |   |

| thread- |   |
|---|---|

|   | dispatcher-delivery |
|---|---|

| Version | Chang e type | Feature description | Release date | References |
|---|---|---|---|---|
|   | New feature | Added support for a multi-language sharding model similar to elastic-job . For more information, see Multi-language sharding model. When you create a group using OpenAPI, an AppKey can be returned. Added support for rerunning tasks with a successful status. Rerunning a task instance in a workflow also reruns its downstream tasks. |   | None |

|   | Optimiz ation | Optimized server performance by changing the communication with the client from synchronous to asynchronous and optimizing the default Akka dispatcher configuration. Using client version 1.1.0 improves heartbeat performance by three times. Redesigned the task management list on the frontend to display more information. |   | None |
|---|---|---|---|---|
| 1.1.0 |   |   | December 17, 2019 |   |
|   | Bug fix | Fixed an issue where global subtasks might not work in the distributed pull model. Fixed an issue where startup might fail in an isolated environment if a domain was not configured. |   | None |
|   | New feature | Added the BlockAppStart configuration. It specifies whether to block the application startup if SchedulerX fails to start. The default value is true . Added an API operation to query the running status of a workflow. The API operation is GetWorkflowInstanceRequest . Added the `jobName` field to the JobContext context. This lets users get the task name during runtime. |   | None |

|   | 1.0.9 |   |   |   | November 28, 2019 | None |
|---|---|---|---|---|---|---|
|   |   |   | Deserializing BigDecimal using Hessian returned 0. An error occurred when deserializing LocalDateTime using Hessian. Fixed an issue with the specify machines feature. If a task ran for a certain period, subtasks were sent to unspecified machines. The client's springContext.getBean call throws the AnnotationConfigApplicationCon |   |   |   |
|   |   |   |   | AnnotationConfigApplicationCon |   |   |
|   |   |   | text has not been refreshed |   |   |   |
|   |   |   | yet |   |   |   |
|   |   | Bug fix |   |   |   |   |
|   |   |   |   | AnnotationConfigApplicationCon |   |   |
|   |   |   | text has been closed already |   |   |   |

| 1.0.8 | New feature | 【Important】Refactored the JobProcessor.postProcess interface and added the ProcessResult return value. If you used the postProcess interface before, you need to modify your code. Enhanced broadcast execution. BroadcastJobProcessor now supports preProcess and postProcess . The preProcess method is executed once before all machines execute the process method. The postProcess method is executed once after all machines execute the process method. JobContext.getTaskAttempt can now get the current number of retries for a subtask. The client now supports custom listener ports, such as SchedulerxWorker.setPort . Java tasks can now implement JobProcessor and do not have to inherit JavaProcessor . | August 6, 2019 | None |
|---|---|---|---|---|
|   | Bug fix | Fixed a bug where subtasks with TaskId=1 did not support automatic retries. If the root task of a distributed task failed, the failure reason could not be viewed. Subtasks could not be retried from the subtask list of a parallel task. |   | None |

|   | preProcess |
|---|---|
| postProcess |   |
| preProcess |   |

| 1.0.6- compatib le |   |   | Optimiz ation | This is a compatible version for the schedulerx1.0(DTS) interface. It does not support depending on both the schedulerx-client and schedulerx-worker packages at the same time. You can only depend on the schedulerx-worker package. This means you need to migrate all DTS tasks to SchedulerX 2.0. |   |   | July 2, 2019 | None |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | Added shade for some packages: aliyun-log, commons- |   |   |   |   |   |
|   |   |   |   |   | aliyun-log, commons- |   |   |   |   |
|   |   |   |   | validator, gson, fastjson, |   |   |   |   |   |
|   |   |   |   | guava, commons-collections |   |   |   |   |   |
| 1.0.6 |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   | ProcessResult(false, |   |   |   |   |
|   |   |   |   | errorMsg) |   |   |   |   |   |
|   |   |   | New feature |   |   |   |   |   |   |
|   |   |   |   |   |   | at- |   |   |   |
|   |   |   |   |   |   |   | July 2, 2019 |   |   |
|   |   |   | Bug fix | Broadcast tasks become stuck. Fixed an issue where second-level tasks would get stuck. at-least-once-delivery could cause infinite retries of subtask statuses. If logcollector failed to initialize, an exception was thrown and the startup failed. Fixed an issue where cleaning up workflow task instances from the DB caused the workflow to fail to resume scheduling. The kill command was not supported for Spring-based startups. |   |   |   |   |   |

|   | schedulerx-client |
|---|---|
| schedulerx-worker |   |

|   | least-once-delivery |
|---|---|

| 1.0.3 | New feature | The MapReduce model now supports returning the results of all subtasks to be processed by the Reduce method. The distributed model now supports a pull model. This resolves the bottleneck effect caused by single- machine performance and supports dynamic scale-out to pull subtasks. The pull model supports global subtask concurrency for rate limiting. Added wfInstanceId to JobContext. If the client fails to start, it throws an exception and blocks the JVM startup. This helps you identify problems early. When the client starts, it prints the versions and paths of Maven dependency JAR files to help you troubleshoot JAR package conflicts. The subtask details of the distributed model now include a queue dimension, which lets you see the cached subtask queue on each machine. | June 6, 2019 | None |
|---|---|---|---|---|
|   | Bug fix | If a worker was mistakenly quarantined due to high server load, it can now recover automatically without restarting the client. The subtask details of the distributed model can now show the actual number of running subtasks on each machine. If a master node fails, the server cleans up the resources on the slave nodes to prevent memory leaks. |   | None |

| 1.0.0 | New feature | Supports periodic timed scheduling using crontab and fixed rate expressions. _ Supports workflow scheduling for flow orchestration. Supports second-level scheduling using the second delay _ expression. Supports Java, Shell, Python, and Go task types. Supports standalone execution, broadcast execution, parallel computing, in-memory grid, and grid computing. Supports Map and MapReduce distributed programming models. Supports automatic retries for failed task instances and subtasks. Retries are disabled by default. Supports data timestamps and data refresh. | April 30, 2019 | None |
|---|---|---|---|---|

|   | crontab |
|---|---|
| fixed rate _ |   |

duling and triggers

## 3 Scheduling and triggers

### 3.1 Timed scheduling

Timed scheduling includes methods such as Cron, Second delay, and Fixed rate.

**Cron**

Cron is a time-based task management system for Unix-like operating systems. You can use Cron to run scheduled tasks, such as commands and scripts, at fixed times and intervals. The expression format is **Second****Minute****Hour****Day Of Month****Month****Day Of Week**
**[Year]**.
The following are examples of common Cron expressions:

| Cron example | Description |
|---|---|
| 0 */1 * * * ? | Triggers once every minute. |
| 0 0 5-15 * * ? | Triggers on the hour from 5:00 to 15:00 every day. |
| 0 0/3 * * * ? | Triggers every 3 minutes. |
| 0 0-5 14 * * ? | Triggers every minute from 14:00 to 14:05 every day. |
| 0 0/5 14 * * ? | Triggers every 5 minutes from 14:00 to 14:55 every day. |
| 0 0/5 14,18 * * ? | Triggers every 5 minutes from 14:00 to 14:55 and from 18:00 to 18:55 every day. |
| 0 0/30 9-17 * * ? | Triggers every half hour from 9:00 to 17:00 every day. |
| 0 0 10,14,16 * * ? | Triggers at 10:00, 14:00, and 16:00 every day. |
| 0 0 12 ? * WED | Triggers at 12:00 every Wednesday. |
| 0 0 17 ? * TUES,THUR,SAT | Triggers at 17:00 every Tuesday, Thursday, and Saturday. |

duling and triggers

| 0 10,44 14 ? 3 WED | Triggers at 14:10 and 14:44 every Wednesday in March. |
|---|---|
| 0 15 10 ? * MON-FRI | Triggers at 10:15 every weekday from Monday to Friday. |
| 0 0 23 L * ? | Triggers at 23:00 on the last day of every month. |
| 0 15 10 L * ? | Triggers at 10:15 on the last day of every month. |
| 0 15 10 ? * 6L | Triggers at 10:15 on the last Friday of every month. |
| 0 15 10 * * ? 2005 | Triggers at 10:15 every day in 2005. |
| 0 15 10 ? * 6L 2002-2005 | Triggers at 10:15 on the last Friday of every month from 2002 to 2005. |
| 0 15 10 ? * 6#3 | Triggers at 10:15 on the third Friday of every month. |

**Second delay**

Second delay scheduling is designed for services that require high real-time performance. It schedules the next task to run after a delay of 1 to 60 seconds from the completion of the previous task. For example, you can configure a scheduled task to run 10 seconds after the previous execution completes.

**Fixed rate**

This method schedules tasks at a fixed frequency. The frequency is measured in seconds and must be 60 seconds or longer.

### 3.2 Workflow scheduling

Orchestrate tasks using visual workflows. You can trigger these workflows using cron expressions or APIs. Jobs in a workflow do not have independent schedules. Instead, they follow the schedule of the workflow. You can transfer data between upstream and downstream nodes in a workflow. For more information, see How to pass data between upstream and downstream nodes in a workflow. To schedule a workflow, it must contain at least two Jobs with a dependency. If you have only one Job, use task management instead.

### 3.3 API trigger

You can use an API to trigger job scheduling. duling and triggers For information on using the API trigger, see the **Integration Guide** section of the
**SchedulerX Developer Guide**.

### 3.4 Backfill data

You can use the data backfill feature to re-trigger instances for a specific time range to backfill business data. For instructions and examples, see Backfill data for scheduling tasks.

### 3.5 Second-level scheduling

Second-level tasks are ideal for services that require high real-time performance, such as near-real-time services that perform continuous polling. A memory grid and second-level scheduling enable you to continuously process massive amounts of data. Second-level tasks in SchedulerX are a type of timed scheduling. They support simple Java tasks, distributed Java tasks, script tasks, and various execution methods. For more information, see How to create a second-level scheduling task. types

## 4 Task types

### 4.1 Java tasks

You can run Java scheduled tasks in your application process. This topic describes how to manage Java tasks.

**Create a Java scheduled task**

For more information about how to create a scheduled task, see Create a scheduled task. This topic describes only the configurations that are specific to Java tasks.
**Task Type**: **java**.
**Processor Class Name**: The fully qualified name of the implementation class, for

```
example, com.apache.armon.test.schedulerx.processor.MySimpleJob .
```

types
**Execution Mode**: The Java job type supports six execution modes: **Standalone**
**Execution**, **Broadcast****Execution**, **Parallel Computing**, **In-memory Grid**, **Grid**
**Computing**, and **Sharded Execution**. **Standalone Execution** and **Broadcast**
**Execution** require you to implement JavaProcessor, while **Parallel Computing**, **In-**
**memory Grid**, **Grid Computing**, and **Sharded Execution** require you to implement
MapJobProcessor.
**Standalone**: A random machine with the same `groupId` executes the task.
**Broadcast**: All machines with the same `groupId` execute the task at the same time.
**Parallel Computing**: Supports fewer than 300 subtasks and provides a subtask list.
**In-memory Grid**: Performs memory-based computing. It supports fewer than 50,000
subtasks and offers high execution speeds.
**Grid Computing**: Performs file-based computing. It supports fewer than 1,000,000
subtasks.
**Sharding**: Distributes shards evenly across multiple clients for execution based on
sharding parameters.

**Programming model**

Java tasks support two programming models: JavaProcessor and MapJobProcessor. JavaProcessor
**Optional:** `public void preProcess(JobContext context)`

```
Required: public ProcessResult process(JobContext context) throws Exception
```

**Optional:** `public void preProcess(JobContext context)`
**Optional:** `public void kill(JobContext context)`
MapJobProcessor

```
Required: public ProcessResult process(JobContext context) throws Exception
```

**Optional:** `public void postProcess(JobContext context)`
**Required method:** `public ProcessResult process(JobContext context) throws`

```
Exception
```

**Optional:** `public void kill(JobContext context)`

```
Required: public ProcessResult map(List<? extends Object> taskList, String taskName)
```

**ProcessResult**

Each process method must return a ProcessResult object. This object indicates the status, result, and error message of the task execution. Task succeeded: `return new ProcessResult(true)` . Task failed: `return new ProcessResult(false, ErrorMsg)` or throw an exception. Task succeeded and returns a result: `return new ProcessResult(true, result)` . The `result` is a string that cannot exceed 1,000 bytes.

**Example of a HelloSchedulerx2.0 task**

types

```java
@Component public class MyProcessor1 extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        // TODO
        System.out.println("Hello, schedulerx2.0!");
        return new ProcessResult(true);
```

`}` `}`

**Example of a task that supports the kill feature**

```java
@Component public class MyProcessor2 extends JavaProcessor {
    private volatile boolean stop = false;
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        int N = 10000;
        while (!stop && N >= 0) {
            // TODO
            N--;
```

`}`

```
        return new ProcessResult(true);
```

`}`

```java
    @Override
    public void kill(JobContext context) {
        stop = true;
```

`}`

```java
    @Override
    public void preProcess(JobContext context) {
        stop = false;  // If you use Spring to start the application, the bean is a sin
gleton. You must use preProcess to reset the flag.
```

`}` `}`

**Example of a batch processing task that uses the Map model**

```
/**
 * Performs distributed batch processing on a single table:
 * 1. The root task queries a table to obtain the minimum and maximum IDs.
 * 2. The root task creates PageTask objects and distributes them using the map method.
 * 3. If a sub-node receives a PageTask object, it processes the data.
```

`*` `*/`

```java
@Component public class ScanSingleTableJobProcessor extends MapJobProcessor {
    private static final int pageSize = 100;
staticclassPageTask{
```

types

```java
    static class PageTask {
        private int startId;
        private int endId;
        public PageTask(int startId, int endId) {
             this.startId = startId;
             this.endId = endId;
```

`}`

```
        public int getStartId() {
              return startId;
```

`}`

```
        public int getEndId() {
              return endId;
```

`}` `}`

```java
    @Override
    public ProcessResult process(JobContext context) {
        String taskName = context.getTaskName();
        Object task = context.getTask();
        if (isRootTask(context)) {
            System.out.println("start root task");
            Pair<Integer, Integer> idPair = queryMinAndMaxId();
            int minId = idPair.getFirst();
            int maxId = idPair.getSecond();
            List<PageTask> taskList = Lists.newArrayList();
            int step = (int) ((maxId - minId) / pageSize); // Calculate the number of p
ages.
            for (int i = minId; i < maxId; i+=step) {
                taskList.add(new PageTask(i, (i+step > maxId ? maxId : i+step)));
```

`}`

```
            return map(taskList, "Level1Dispatch");
        } else if (taskName.equals("Level1Dispatch")) {
            PageTask record = (PageTask)task;
            long startId = record.getStartId();
            long endId = record.getEndId();
            // TODO
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(true);
```

`}`

```java
    @Override
    public void postProcess(JobContext context) {
        // TODO
        System.out.println("all tasks is finished.");
```

`}`

```java
    private Pair<Integer, Integer> queryMinAndMaxId() {
        // TODO: select min(id),max(id) from xxx
        return null;
```

`}` `}` types

### 4.2 Script tasks

You can create a script task by writing a Shell, Python, or Go script.

**Connection types**

Script tasks support two connection types: Embedded in the application process A standalone agent installed from schedulerxAgent-1.1.0.tar.gz

**Creation method**

You can create a script task by writing a script when you create a scheduling task. For more information, see Create a scheduling task.

**Shell task example without parameters**

**Shell task example with parameters**

types

**Python task example**

**Go task example**

types

### 4.3 HTTP tasks

SchedulerX 2.0 supports HTTP tasks. You do not need a client. You can configure the task in the console.

**Limits**

Only GET and POST requests are supported. The HTTP request must return a result in JSON format. The service parses a specified key to check whether the request is successful. Second-level tasks are not supported. The minimum supported interval is one minute.

**Task configuration**

For information about how to create a scheduling task, see Create a Scheduling Task. This topic describes only the configurations for HTTP tasks. types
**Tasktype**: Select http.
**Full URL**: Enter the full URL, including `http://` .
**Response Validation Key** and **Response Validation Value**: By default, the service
expects the HTTP request to return a result in JSON format. The service validates the success of the request based on the key and value that you enter. For example, you can validate that the value of the `success` key is `true` or that the value of the `code` key is `200`. types `{`

```
  code: 200,
  data: "true",
  message: "",
  requestId: "446655068791923614103381232971",
  success: true
```

`}`
**Execution Timeout**: The value can be from 0 to 30 seconds.
**Cookie**: For example, key1=val1;key2=val2 . Use semicolons (;) to separate multiple
values. The maximum length is 300 bytes.

**Code configuration**

The code configuration is different for GET and POST methods. GET

```
@GET @Path("hi") @Produces(MediaType.APPLICATION_JSON) public RestResult hi(@QueryParam("user") String user) {
    TestVo vo = new TestVo();
    vo.setName(user);
    RestResult result = new RestResult();
    result.setCode(200);
    result.setData(vo);
    return result;
```

`}` POST

```java
import com.alibaba.schedulerx.common.constants.CommonConstants; @POST @Path("createUser") @Produces(MediaType.APPLICATION_JSON) public RestResult createUser(@FormParam("userId") String userId,
        @FormParam("userName") String userName) {
    TestVo vo = new TestVo();
    System.out.println("userId=" + userId + ", userName=" + userName);
    vo.setName(userName);
    RestResult result = new RestResult();
    result.setCode(200);
    result.setData(vo);
    return result;
```

`}`

**Obtain task information**

HTTP tasks record basic task information in the HTTP header. To obtain this information, add the required dependency and code to your project.
1. Add the dependency to the pom.xml file.
types

```xml
<dependency>
    <groupId>com.aliyun.schedulerx</groupId>
    <artifactId>schedulerx2-common</artifactId>
    <version>1.1.5-SNAPSHOT</version>
</dependency>
```

2. Add the code to obtain task information.
The following example shows how to obtain basic task information for a GET method.

```java
import com.alibaba.schedulerx.common.constants.CommonConstants; @GET @Path("hi") @Produces(MediaType.APPLICATION_JSON) public RestResult hi(@QueryParam("user") String user,
        @HeaderParam(CommonConstants.JOB_ID_HEADER) String jobId,
        @HeaderParam(CommonConstants.JOB_NAME_HEADER) String jobName) {
    TestVo vo = new TestVo();
    vo.setName("armon");
    System.out.println("user=" + user + ", jobId=" + jobId + ", jobName=" + jobName);
    RestResult result = new RestResult();
    result.setCode(200);
    result.setData(vo);
    return result;
```

`}` The following table lists the basic task information that you can obtain.

| CommonConstants constant | Key | Value description |
|---|---|---|
| JOB ID HEADER _ _ | schedulerx-jobId | The task ID. |
| JOB NAME HEADER _ _ | schedulerx-jobName | The task name. The name must be in English because the header does not support Chinese characters. |
| SCHEDULE TIMESTAMP HEADE _ _ R | schedulerx- scheduleTimestamp | The timestamp of the scheduling time. |
| DATA TIMESTAMP HEADER _ _ | schedulerx-dataTimestamp | The data timestamp. |
| GROUP ID HEADER _ _ | schedulerx-groupId | The application ID. |
| USER HEADER _ | schedulerx-user | The username. |

types

| MAX ATTEMPT HEADER _ _ | schedulerx-maxAttempt | The maximum number of retries for the instance. |
|---|---|---|
| ATTEMPT HEADER _ | schedulerx-attempt | The current number of retries for the instance. |
| JOB PARAMETERS HEADER _ _ | schedulerx-jobParameters | The task parameters. |
| INSTANCE PARAMETERS HEAD _ _ ER | schedulerx- instanceParameters | The task instance parameters. This requires an API trigger. |

**Verify results**

On the **Execution List** page, you can query the execution results of the HTTP task. If a task fails, click **Details** to view the cause of the failure. This topic describes possible failure scenarios: The return value does not match the expected value. The error message is: `Unexpected`

```
return value val:{"code":-1,"data":{},"success":false,******} .
```

The execution timed out. Error message: `Service request error: Read timed out` .

**Error alerts**

HTTP tasks support error alerts. You can configure alerts for exceptions, such as unexpected return values and execution timeouts, when you create a task. buted programming model

## 5 Distributed programming model

**model**

### 5.1 Standalone

Standalone execution is a mode where a task instance is triggered on a single, randomly selected Worker. This mode supports all task types.

### 5.2 Broadcast

In a broadcast execution, a task instance is sent to all Workers in a group. The task is considered complete only after all Workers finish executing. If any Worker fails, the entire task fails.

**Scenarios**

Batch operations Periodically broadcast a script to execute on all machines. Periodically broadcast a command to clear the cache on all machines. Data aggregation You can use a JavaProcessor to reset the database count to 0 during the preProcess phase. When each machine executes the process method, it increments the count in the database based on its memory or log values. During the postProcess phase, you can read the count value from the database and pass it to a downstream task.

**Task types**

Various task types are available, such as script and Java tasks. Java tasks support advanced attributes, such as preProcess and postProcess. To use a Java task, inherit from the JavaProcessor class (version 1.0.7 or later). The interface is as follows:

| : | public ProcessResult process(JobContext context) throws Exception |
|---|---|
| public void preProcess(JobContext context) |   |
| public ProcessResult postProcess(JobContext context) |   |

preProcess executes once before any machine executes the process method. postProcess executes once after all machines have successfully executed the process method. It can return a result to pass data within a workflow.

**Demo**

buted programming model

```java
@Component public class TestBroadcastJobProcessor extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("this is process");
        return new ProcessResult(true);
```

`}`

```java
    @Override
    public void preProcess(JobContext context) {
        System.out.println("this is preProcess");
```

`}`

```java
    @Override
    public ProcessResult postProcess(JobContext context) {
        System.out.println("this is postProcess");
        return new ProcessResult(true, "hello broadcast");
```

`}` `}` If you start three machines, the execution results are as follows: Worker 1

```
this is preProcess this is process this is postProcess
```

Worker 2

```
this is process
```

Worker 3

```
this is process
```

### 5.3 Map model

You can use the `MapJobProcessor` and call the `map` method to run distributed batch jobs for big data.

**Notes**

Scheduler X does not guarantee that sub-tasks are executed only once. A failover can cause sub-tasks to run multiple times. You must implement idempotence in your service logic. Scheduler X uses the Hessian serialization framework. This framework does not support the
**LocalDateTime** or **BigDecimal** data structures. If your sub-tasks use these data
structures, you must replace them. For **BigDecimal**, serialization does not cause an error, but the value becomes 0 after it is deserialized.

**Interfaces**

buted programming model

|   | Interface |   | Description | Required |
|---|---|---|---|---|
|   | ProcessResult |   | The entry point for the business logic of each sub-task. Get the taskName from the context to identify the sub-task and process its logic. After the task is executed, return a `ProcessResult`. For more information about the `ProcessResult` interface, see ProcessResult. | Yes |
|   |   | ProcessResult | identify the sub- process its logic. |   |
|   | process(JobContext |   |   |   |
|   | context) |   |   |   |
|   | ProcessResult map(List<? |   | The `map` method distributes a batch of sub-tasks across multiple machines for execution. You can call the | Yes |
|   |   | ProcessResult map(List<? | `map` method multiple times. If `taskList` is empty, the |   |
|   | extends Object> taskList, |   | If `taskList` is e |   |
|   |   |   | method fails. Aft |   |
|   | String taskName) |   |   |   |
|   | void kill(JobContext context) |   | This method is triggered when a task is killed from the console. You must implement the logic to break the business process. | No |

|   | void kill(JobContext | a t co |
|---|---|---|
| context) |   |   |

**Execution modes**

Parallel computing: Supports up to 300 tasks and requires a list of sub-tasks.

> **Important:** Do not use parallel computing for tasks that complete within seconds.

Memory grid: An in-memory computing mode. It supports fewer than 50,000 sub-tasks and provides high performance. Grid computing: A file-based computing mode. It supports up to 1,000,000 sub-tasks.

**Advanced configuration**

For more information about advanced configurations, see Advanced configuration parameters for task management.

**Demo: Send 50 messages (for Map model)**

buted programming model

```java
@Component public class TestMapJobProcessor extends MapJobProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        String taskName = context.getTaskName();
        int dispatchNum = 50;
        if (isRootTask(context)) {
            System.out.println("start root task");
            List<String> msgList = Lists.newArrayList();
            for (int i = 0; i <= dispatchNum; i++) {
                msgList.add("msg_" + i);
```

`}`

```java
            return map(msgList, "Level1Dispatch");
        } else if (taskName.equals("Level1Dispatch")) {
            String task = (String)context.getTask();
            System.out.println(task);
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}` `}`

**Demo: Process data from a single table (for Map or MapReduce**

**models)**

```java
@Component public class ScanSingleTableJobProcessor extends MapJobProcessor {
    @Service
    private XXXService xxxService;
    private final int PAGE_SIZE = 500;
    static class PageTask {
        private long startId;
        private long endId;
        public PageTask(long startId, long endId) {
            this.startId = startId;
            this.endId = endId;
```

`}`

```
        public long getStartId() {
            return startId;
```

`}`

```
        public long getEndId() {
            return endId;
```

`}` `}` buted programming model

```java
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        // The backend code can be the same for multiple jobs. Configure the job parame
ter in the console to specify the table name.
        String tableName = context.getJobParameters();
        String taskName = context.getTaskName();
        Object task = context.getTask();
        if (isRootTask(context)) {
            Pair<Long, Long> idPair = queryMinAndMaxId(tableName);
            long minId = idPair.getFirst();
            long maxId = idPair.getSecond();
            List<PageTask> tasks = Lists.newArrayList();
            // Calculate the number of pages.
            int step = (int) ((maxId - minId) / PAGE_SIZE);
            for (long i = minId; i < maxId; i+=step) {
                tasks.add(new PageTask(i, (i+step > maxId ? maxId : i+step)));
```

`}`

```
            return map(tasks, "PageTask");
        } else if (taskName.equals("PageTask")) {
            PageTask pageTask = (PageTask)task;
            long startId = pageTask.getStartId();
            long endId = pageTask.getEndId();
            List<Record> records = queryRecord(tableName, startId, endId);
            // TODO: Handle records.
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    private Pair<Long, Long> queryMinAndMaxId(String tableName) {
        // TODO: select min(id), max(id) from [tableName]
        return new Pair<Long, Long>(1L, 10000L);
```

`}`

```java
    private List<Record> queryRecord(String tableName, long startId, long endId) {
        List<Record> records = Lists.newArrayList();
        // TODO: select * from [tableName] where id >= [startId] and id < [endId]
        return records;
```

`}` `}`

**Demo: Process sharded database and table data (for Map or**

**MapReduce models)**

```java
@Component public class ScanShardingTableJobProcessor extends MapJobProcessor {
    @Service
    private XXXService xxxService;
priatefinalintPAGESIZE
```

buted programming model

```java
    private final int PAGE_SIZE = 500;
    static class PageTask {
        private String tableName;
        private long startId;
        private long endId;
        public PageTask(String tableName, long startId, long endId) {
            this.tableName = tableName;
            this.startId = startId;
            this.endId = endId;
```

`}`

```
        public String getTableName() {
            return tableName;
```

`}`

```
        public long getStartId() {
            return startId;
```

`}`

```
        public long getEndId() {
            return endId;
```

`}` `}`

```java
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        String taskName = context.getTaskName();
        Object task = context.getTask();
        if (isRootTask(context)) {
            // First, shard the databases.
            List<String> dbList = getDbList();
            return map(dbList, "DbTask");
        } else if (taskName.equals("DbTask")) {
            // Then, shard the tables based on the sharded databases.
            String dbName = (String)task;
            List<String> tableList = getTableList(dbName);
            return map(tableList, "TableTask");
        } else if (taskName.equals("TableTask")) {
            // If a sharded table is also large, perform paging.
            String tableName = (String)task;
            Pair<Long, Long> idPair = queryMinAndMaxId(tableName);
            long minId = idPair.getFirst();
            long maxId = idPair.getSecond();
            List<PageTask> tasks = Lists.newArrayList();
            // Calculate the number of pages.
            int step = (int) ((maxId - minId) / PAGE_SIZE);
            for (long i = minId; i < maxId; i+=step) {
                tasks.add(new PageTask(tableName, i, (i+step > maxId ? maxId : i+step)))
```

; `}`

```
            return map(tasks, "PageTask");
        } else if (taskName.equals("PageTask")) {
PageTaskpageTask=(PageTask)task;
```

buted programming model

```
            PageTask pageTask  (PageTask)task;
            String tableName = pageTask.getTableName();
            long startId = pageTask.getStartId();
            long endId = pageTask.getEndId();
            List<Record> records = queryRecord(tableName, startId, endId);
            // TODO: Handle records.
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    private List<String> getDbList() {
        List<String> dbList = Lists.newArrayList();
        // TODO: Return the list of sharded databases.
        return dbList;
```

`}`

```java
    private List<String> getTableList(String dbName) {
        List<String> tableList = Lists.newArrayList();
        // TODO: Return the list of sharded tables.
        return tableList;
```

`}`

```java
    private Pair<Long, Long> queryMinAndMaxId(String tableName) {
        // TODO: select min(id), max(id) from [tableName]
        return new Pair<Long, Long>(1L, 10000L);
```

`}`

```java
    private List<Record> queryRecord(String tableName, long startId, long endId) {
        List<Record> records = Lists.newArrayList();
        // TODO: select * from [tableName] where id >= [startId] and id < [endId]
        return records;
```

`}` `}`

### 5.4 MapReduce model

The MapReduce model is an extension of the Map model. It adds a Reduce interface and requires the implementation of `MapReduceJobProcessor`.

**Notes**

The MapReduce model has a single Reduce method that runs after all subtasks are complete. You can use this method to return the execution result of the task instance, which is then passed as output data in the workflow. The Reduce method does not run if a subtask fails. If the Reduce method fails, the entire task instance fails. Scheduler X does not guarantee that a subtask runs only once. A failover can occur under certain conditions, which may cause the subtask to run multiple times. Therefore, you must implement idempotence for your services. Scheduler X uses the Hessian serialization framework. This framework does not support
**LocalDateTime** or **BigDecimal**. If a subtask contains these data structures, you must
replace them. For **BigDecimal**, serialization does not cause an error, but its value becomes buted programming model 0 after deserialization.

**Interfaces**

|   | Interface |   | Description | Required |
|---|---|---|---|---|
|   | ProcessResult |   | The entry point for the business logic of each subtask. Get the taskName from the context to identify the subtask and process its logic. After the task runs, return a `ProcessResult`. For more information about the `ProcessResult` interface, see ProcessResult. | Yes |
|   |   | ProcessResult | taskName from identify the subt |   |
|   | process(JobContext |   |   |   |
|   | context) |   |   |   |
|   | ProcessResult map(List<? |   | Run the `map` method to distribute a batch of subtasks across multiple machines. You | Yes |
|   |   | ProcessResult map(List<? | can run the `map` method multiple times. If `taskList` is |   |
|   | extends Object> taskList, |   |   |   |
|   |   |   | empty, the meth |   |
|   | String taskName) |   |   |   |
|   | void kill(JobContext context) |   | Killing a task in the frontend triggers this method. You must implement the logic to break your business process. | No |

|   | void kill(JobContext | tri |
|---|---|---|
| context) |   |   |

**Execution modes**

Parallel computing: Supports up to 300 tasks and includes a subtask list.

> **Important:** Do not use parallel computing for tasks that run in seconds.

Memory grid: Performs high-speed, in-memory computing and supports fewer than 50,000 subtasks. Grid computing: Performs file-based computing and supports up to 1,000,000 subtasks.

**Advanced configuration**

For more information about advanced configurations, see Advanced configuration parameters for task management.

**Demo: Send 500 messages (for the MapReduce model)**

buted programming model

```java
@Component public class TestMapReduceJobProcessor extends MapReduceJobProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        String taskName = context.getTaskName();
        int dispatchNum=500;
        if (isRootTask(context)) {
            System.out.println("start root task");
            List<String> msgList = Lists.newArrayList();
            for (int i = 0; i <= dispatchNum; i++) {
                msgList.add("msg_" + i);
```

`}`

```java
            return map(msgList, "Level1Dispatch");
        } else if (taskName.equals("Level1Dispatch")) {
            String task = (String)context.getTask();
            System.out.println(task);
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    @Override
    public ProcessResult reduce(JobContext context) throws Exception {
        return new ProcessResult(true, "TestMapReduceJobProcessor.reduce");
```

`}` `}`

**Demo: Process data from a single table (for Map or MapReduce**

**models)**

```java
@Component public class ScanSingleTableJobProcessor extends MapJobProcessor {
    @Service
    private XXXService xxxService;
    private final int PAGE_SIZE = 500;
    static class PageTask {
        private long startId;
        private long endId;
        public PageTask(long startId, long endId) {
            this.startId = startId;
            this.endId = endId;
```

`}`

```
        public long getStartId() {
            return startId;
```

`}` buted programming model

```
        public long getEndId() {
            return endId;
```

`}` `}`

```java
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        // The backend code can be the same for multiple jobs. Use the console to confi
gure the job parameter that specifies the table name.
        String tableName = context.getJobParameters();
        String taskName = context.getTaskName();
        Object task = context.getTask();
        if (isRootTask(context)) {
            Pair<Long, Long> idPair = queryMinAndMaxId(tableName);
            long minId = idPair.getFirst();
            long maxId = idPair.getSecond();
            List<PageTask> tasks = Lists.newArrayList();
            // Calculate the number of pages.
            int step = (int) ((maxId - minId) / PAGE_SIZE);
            for (long i = minId; i < maxId; i+=step) {
                tasks.add(new PageTask(i, (i+step > maxId ? maxId : i+step)));
```

`}`

```
            return map(tasks, "PageTask");
        } else if (taskName.equals("PageTask")) {
            PageTask pageTask = (PageTask)task;
            long startId = pageTask.getStartId();
            long endId = pageTask.getEndId();
            List<Record> records = queryRecord(tableName, startId, endId);
            //TODO: handle records
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    private Pair<Long, Long> queryMinAndMaxId(String tableName) {
        //TODO: select min(id),max(id) from [tableName]
        return new Pair<Long, Long>(1L, 10000L);
```

`}`

```java
    private List<Record> queryRecord(String tableName, long startId, long endId) {
        List<Record> records = Lists.newArrayList();
        //TODO: select * from [tableName] where id>=[startId] and id<[endId]
        return records;
```

`}` `}`

**Demo: Process sharded data (for Map or MapReduce models)**

```java
@Component public class ScanShardingTableJobProcessor extends MapJobProcessor {
```

buted programming model

```java
    @Service
    private XXXService xxxService;
    private final int PAGE_SIZE = 500;
    static class PageTask {
        private String tableName;
        private long startId;
        private long endId;
        public PageTask(String tableName, long startId, long endId) {
            this.tableName = tableName;
            this.startId = startId;
            this.endId = endId;
```

`}`

```
        public String getTableName() {
            return tableName;
```

`}`

```
        public long getStartId() {
            return startId;
```

`}`

```
        public long getEndId() {
            return endId;
```

`}` `}`

```java
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        String taskName = context.getTaskName();
        Object task = context.getTask();
        if (isRootTask(context)) {
            // First, perform database sharding.
            List<String> dbList = getDbList();
            return map(dbList, "DbTask");
        } else if (taskName.equals("DbTask")) {
            // Then, perform table sharding based on the database shards.
            String dbName = (String)task;
            List<String> tableList = getTableList(dbName);
            return map(tableList, "TableTask");
        } else if (taskName.equals("TableTask")) {
            // If a sharded table is also large, perform paging.
            String tableName = (String)task;
            Pair<Long, Long> idPair = queryMinAndMaxId(tableName);
            long minId = idPair.getFirst();
            long maxId = idPair.getSecond();
            List<PageTask> tasks = Lists.newArrayList();
            // Calculate the number of pages.
            int step = (int) ((maxId - minId) / PAGE_SIZE);
            for (long i = minId; i < maxId; i+=step) {
                tasks.add(new PageTask(tableName, i, (i+step > maxId ? maxId : i+step)))
```

; buted programming model `}`

```
            return map(tasks, "PageTask");
        } else if (taskName.equals("PageTask")) {
            PageTask pageTask = (PageTask)task;
            String tableName = pageTask.getTableName();
            long startId = pageTask.getStartId();
            long endId = pageTask.getEndId();
            List<Record> records = queryRecord(tableName, startId, endId);
            //TODO: handle records
            return new ProcessResult(true);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    private List<String> getDbList() {
        List<String> dbList = Lists.newArrayList();
        //TODO: Return the list of database shards.
        return dbList;
```

`}`

```java
    private List<String> getTableList(String dbName) {
        List<String> tableList = Lists.newArrayList();
        //TODO: Return the list of table shards.
        return tableList;
```

`}`

```java
    private Pair<Long, Long> queryMinAndMaxId(String tableName) {
        //TODO: select min(id),max(id) from [tableName]
        return new Pair<Long, Long>(1L, 10000L);
```

`}`

```java
    private List<Record> queryRecord(String tableName, long startId, long endId) {
        List<Record> records = Lists.newArrayList();
        //TODO: select * from [tableName] where id>=[startId] and id<[endId]
        return records;
```

`}` `}`

**Demo: Process 50 messages and have Reduce aggregate the**

**subtask results (for the MapReduce model)**

buted programming model

```java
@Component public class TestMapReduceJobProcessor extends MapReduceJobProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        String taskName = context.getTaskName();
        int dispatchNum = 50;
        if (context.getJobParameters() != null) {
            dispatchNum = Integer.valueOf(context.getJobParameters());
```

`}`

```java
        if (isRootTask(context)) {
            System.out.println("start root task");
            List<String> msgList = Lists.newArrayList();
            for (int i = 0; i <= dispatchNum; i++) {
                msgList.add("msg_" + i);
```

`}`

```
            return map(msgList, "Level1Dispatch");
        } else if (taskName.equals("Level1Dispatch")) {
            String task = (String)context.getTask();
            Thread.sleep(2000);
            return new ProcessResult(true, task);
```

`}`

```
        return new ProcessResult(false);
```

`}`

```java
    @Override
    public ProcessResult reduce(JobContext context) throws Exception {
        for (Entry<Long, String> result : context.getTaskResults().entrySet()) {
            System.out.println("taskId:" + result.getKey() + ", result:" +
result.getValue());
```

`}`

```
        return new ProcessResult(true, "TestMapReduceJobProcessor.reduce");
```

`}` `}`

### 5.5 Multi-language sharding models

**models**

SchedulerX can schedule various tasks, such as timed scheduling, orchestration, and historical data reprocessing. To handle big data requirements, it provides multi-language sharding models for Java, Python, Shell, and Go.

**Background information**

Sharding models include static sharding and dynamic sharding. Static sharding: Processes a fixed number of shards. For example, you can use multiple machines to process 1,024 fixed tables in a sharded database. buted programming model Dynamic sharding: Processes data of an unknown volume in a distributed manner. For example, you can run distributed batch jobs on a large, constantly changing table. The mainstream framework for this is the MapReduce model in SchedulerX 2.0, which is not yet open source.

**Features**

The multi-language sharding models have the following features. Compatible with the static sharding model of Elastic-Job. Supports four languages: Java, Python, Shell, and Go. High availability: The sharding model is based on the Map model and inherits its high availability (HA) features. If an exception occurs on a worker, the master worker fails the shard over to another slave node for execution. Traffic shaping: The sharding model is based on the Map model and inherits its traffic shaping features. This lets you control the concurrency of subtasks on a single machine. For example, if you have 1,000 shards and 10 machines, you can limit concurrent execution to a maximum of 5 shards. The remaining shards wait in a queue. Automatic retry on shard failure: The sharding model is based on the Map model and inherits its automatic retry feature for failed subtasks. You can set availability and traffic shaping in the advanced configuration when you create a task. For more information, see Create a scheduling task and Advanced configuration parameters for task management.

> **Note:** Only client versions 1.1.0 and later support the multi-language sharding models.

**Java sharding task**

1. Log on to the SchedulerX console.
2. In the left navigation pane, click **Task List**.
3. On the **Task List** page, click **Create**.
4. On the **Basic Information** page, set **Execution Mode** to **Shard** and configure the **Shard**
**Parameters**.
buted programming model buted programming model The following table describes the parameters.

|   | Parameter |   | Description |   |   |
|---|---|---|---|---|---|
|   | Task Name |   | A custom name for the task. |   |   |
|   | Description |   | A custom description of the task. |   |   |
|   | Group ID |   | The group to which the task belongs. Select one from the drop-down list. |   |   |
|   | Task Type |   | The language of the task. For this scenario, select java. |   |   |
|   | Processor Class Name |   | The full path of the JobProcessor class, for example, xxx.xxx.xxx.HelloProcessor. |   |   |
|   | Execution Mode |   | The execution mode of the task. For this scenario, select Shard. |   |   |
|   | Priority |   | The priority of the task. For this scenario, select the default value Medium. |   |   |
|   | Shard Parameters |   | Set shard parameters to distribute shards evenly across multiple clients for execution. Separate shard parameters with commas (,) or line breaks. For example, shard ID 1=shard |   |   |
|   |   |   |   | shard ID 1=shard |   |
|   |   |   | parameter 1,shard ID 2=shard parameter |   |   |
|   |   |   | 2,... |   |   |

|   | JobContext.getShardingId() |
|---|---|
| JobContext.getShardingParameter() |   |

parameter. Example: buted programming model

```java
@Component public class HelloWorldProcessor extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("shardId=" + context.getShardingId() + ",
shardingParameter=" + context.getShardingParameter());
        return new ProcessResult(true);
```

`}` `}`
6. View shard details.
i. In the navigation pane on the left, click **Execution List**. ii. On the **Execution List** page, click **Shard Details**.

**Python sharding task**

To run distributed batch jobs for a Python application, install the agent. This allows SchedulerX 2.0 to maintain the scripts.
1. Download the SchedulerX agent and use it to deploy the script task. For more information,
see Create a standalone script task using an agent.
2. Create a Python sharding task in SchedulerX 2.0. For more information, see Create a
scheduling task. The script receives the shard ID as `sys.argv[1]` and the shard parameter as

```
 sys.argv[2] .
```

In the console, you can define the parameters for multiple shards by separating them with commas (,) or line breaks. For example: `shard ID 1=shard parameter 1,shard ID 2=shard`

```
parameter 2,... .
```

3. View shard details.
i. In the navigation pane on the left, click **Execution List**. ii. On the **Execution List** page, click **Shard Details**. buted programming model

**Shell and Go sharding tasks**

Shell and Go sharding tasks are similar to Python sharding tasks. For the creation steps, see Python sharding task. ole user guide

## 6 Console user guide

### 6.1 Overview

The Overview page displays a summary of Jobs, task instances, and a list of failed instances.

**View Job Summary**

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Overview**.
3. On the **Overview** page, in the **Job Summary** area, view **Total Jobs**, **Enabled Jobs**, and
**Disabled Jobs**.

**View Task Instance Summary**

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Overview**.
3. On the **Overview** page, in the **Task Instance Summary** area, select a **Time Range** to
view **Total Task Instances**, **Running Task Instances**, **Failed Task Instances**,
**Successful Task Instances**, **Pending Task Instances**, and **Task Instances in Pool**.

**View Failed Instance List**

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Overview**.
3. On the **Overview** page, in the **Failed Instance List** area, view **ID**, **Job Name**, **Job ID**,
**Flow Instance ID**, **Group ID**, **Status**, **Start Time**, **End Time**, and **Operator**.
4. In the failed instance list, click **Details** in the **Operation** column for the target failed
instance. In the **Basic Information** panel, view **Instance ID**, **Retries**, **Job ID**, **Job Name**,
**Start Time**, **End Time**, **Scheduled Time**, **Data Timestamp**, **Server IP**, **Worker**
**Address**, and **Result or Error Message**.

### 6.2 Execution List

Use the Execution List to view today’s task execution status. The list includes two tabs: Task Instances and Workflow Instances.

**View the Execution List**

> **Note:** By default, SchedulerX retains the most recent 60 records for each task and workflow.

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Execution List**.
3. On the **Execution List** page, click the **Task Instances** tab or the **Workflow Instances**
tab. By default, the page displays all execution records under **All Groups** and **All**. To filter records, select a specific task group and then filter by status: **All**, **Succeeded**,
**Failed**, **Running**, **In Pool**, or **Waiting**. You can also search by task ID and time range.
Enter the task ID in the text box next to **Task ID**, and select a time range. ole user guide

**View Task Instance Details**

1. On the **Execution List** page, go to the **Task Instances** tab. Find the task you want to
view. In the **Operation** column, click **Details**.
2. On the **Basic Information** page, view the following details: **Instance ID**, **Retry Count**,
**Task ID**, **Task Name**, **Start Time**, **End Time**, **Scheduled Time**, **Data Timestamp**,
**serverIp**, **workAddr**, and **Result or Error Message**.
3. On the **Basic Information** page, click **View Details** next to **Task ID** to view the task
details. For more information, see Create a Scheduling Task.
4. On the **Task Instances** tab, perform actions based on the task status.
**Waiting**: Mark as succeeded.
**Failed**: Rerun or mark as succeeded.
**Running**: Stop or mark as succeeded.
**In Pool**: No action available.
**Succeeded**: Rerun.

**View Workflow Instance Details**

1. On the **Execution List** page, go to the **Workflow Instances** tab. Find the workflow you
want to view. In the **Workflow Instance Graph** column, click the workflow instance ID link.
2. On the **Workflow Instance Details** page, view the workflow details in the **Workflow**
**Canvas**.
Each task is color-coded by its execution status. For example, red indicates failure. Tasks that depend on it remain in the waiting state (blue).
3. Right-click a failed task. In the shortcut menu, click **Details** to view the failure reason.
4. After making changes, right-click the task again. In the shortcut menu, click **Rerun** to re-
execute it. If the task succeeds, downstream tasks run. If you do not want to rerun the task, click **Mark as Succeeded** in the shortcut menu. This forces the task into the succeeded state, and downstream tasks start running.

### 6.3 Task List

On the Task Management page, you can create, edit, run, copy, enable, disable, import, export, and delete scheduling tasks. You can also refresh task data and assign specific machines to a task.

**Create a Scheduling Task**

ole user guide

**Important**

Before creating a task, make sure you have created a task group. For more information, see Create an Application Group.
1. Log on to the Distributed Task Scheduler console.
2. In the navigation pane on the left, click **Task List**.
3. On the **Task List** page, click **Create**.
4. On the **Basic Configuration** tab, set basic parameters for the scheduling task and optional
**Advanced Configuration**. Then click **Next**.
Parameter descriptions for basic configuration:

| Configuration Name | Meaning | Default Value |
|---|---|---|
| Task Name | The name of the task. | None |
| Description | A brief description of the business logic. This helps with later searches. | None |
| Group ID | The group that the task belongs to. Select from the drop-down list. | None |
| Task Type | The implementation language of the task. The following five languages are supported: Java Shell Python Go HTTP For Shell, Python, and Go, an editor appears. Write your task script in the editor. | None |
| Processor Class Name | Appears only when you select Task Type as Java. Enter the full path of the JobProcessor class, such as xxx.xxx.xxx.HelloProcessor. | None |

ole user guide

| Execution Mode | The mode used to execute the task. The following modes are supported: Standalone: Run on one randomly selected machine. Broadcast: Run on all machines at once and wait for all to finish. Parallel Computing: Map model. Supports up to 300 subtasks. Shows a subtask list. In-Memory Grid: Map model. Supports up to 50,000 subtasks. No subtask list. Fast execution. Grid Computing: Map model. Supports up to 1,000,000 subtasks. No subtask list. Sharding: Similar to Elastic- Job. Configure sharding parameters to distribute shards evenly across multiple clients. Supports multi-language versions. Note Advanced settings change based on the execution mode you select. | None |
|---|---|---|
| Full URL | Enter the full URL, including http:// . Note Appears only when you select Task Type as HTTP. | None |
| Request Method | Select GET or POST. Note Appears only when you select Task Type as HTTP. | None |

ole user guide

| Response Parsing Mode | Select HTTP Status Code, Custom JSON, or Custom String. Note Appears only when you select Task Type as HTTP. | None |
|---|---|---|
| HTTP Status Code | Set the HTTP status code that indicates success. Note Appears when you select Response Parsing Mode as HTTP Status Code. | 200 |
| Return Verification Key | Supports only JSON-formatted return values. Enter the key that indicates success. Note Appears when you select Response Parsing Mode as Custom JSON. | None |
| Return Verification Value | Return values are supported only in JSON format. If the request succeeds, the validated value is returned. Note Appears when you select Response Parsing Mode as Custom JSON. | None |

ole user guide

| Custom String | Enter a keyword or phrase that indicates success. Note Appears when you select Response Parsing Mode as Custom String. | None |
|---|---|---|
| Execution Timeout | Set the maximum time to wait for task execution. Valid values: 0 seconds to 30 seconds. | None |
| Cookie | Add cookies to the request header. Separate multiple values with semicolons (;). Maximum length: 300 bytes. | None |
| Execution Method | Agent: Deploy schedulerxAgent first. The client initiates the request and supports internal URLs. Note Supported only for client versions 1.8.2 and later. | agent |
| Priority | Low Chinese High Very High | Medium |
| Task Parameters | Any string. Retrieve it at runtime from the context. | None |

If advanced configuration is needed for your business, see Advanced Configuration Parameters for Task Management.
5. On the **Schedule Configuration** tab, set schedule parameters and optional advanced
configuration. Then click **Next**. ole user guide Schedule parameter descriptions:

| Configuration Name | Significance | Default Value |
|---|---|---|
| Time Type | None: No scheduling. Usually triggered by workflows. Cron: Cron expression. API: Triggered by API calls. Fixed Rate: Fixed frequency. Second Delay: Fixed delay in seconds. | cron |

ole user guide

| Time Expression | Enter the time expression based on the time type: None: Not required. Cron: Enter a cron expression. Use standard cron syntax or generate and validate it using a tool. API: Not required. Fixed Rate: Enter the interval in seconds. For example, 65 runs the task every 65 seconds. Second Delay: Enter the delay in seconds. Valid range: 1 to 60 seconds. For example, 5 triggers the task after a 5-second delay. | None |
|---|---|---|

When you select Cron as the time type, advanced configuration options appear. Advanced configuration parameter descriptions:

| Configuration Name | Significance | Default Value |
|---|---|---|
| Time Offset | The offset of the data timestamp relative to the scheduled time. Retrieve this value from the context during scheduling. | None |
| Time Zone | Select a time zone based on your needs. Options include common countries and regions, and standard GMT formats. | None |
| Calendar | Examples: custom scheduling calendar, skip weekends, skip specific dates. | None |

6. On the **Alert Configuration** tab, set alert parameters. Then click **Submit**.
ole user guide Alert parameter descriptions:

| Configuration Name | Meaning | Default Value |
|---|---|---|
| Timeout Alert | Open Shut down | Open |
| Timeout Duration | Displays when timeout alerts are enabled. Set the duration in seconds before triggering an alert. | 2 hours |
| Terminate on Timeout | Displays when timeout alerts are enabled. Automatically kills the task if it runs longer than the specified time. Open Shut down | Shut down |
| Failure Alert | Open Shut down | Open |
| No Available Machine Alert | Open Shut down | Open |

ole user guide
7. Return to the **Task Management** page. Check whether the task you just created appears
and whether its parameters match your configuration.

> **Note:** After creation, a scheduling task is enabled by default. You can disable or re-enable it as needed. For more information, see Enable and Disable Scheduling Tasks.

**Edit a Scheduling Task**

1. On the **Task List** page, click **Edit** in the **Actions** column.
2. On the **Edit Task** page, configure parameters for **Basic Configuration**, **Schedule**
**Configuration**, and **Alert Configuration**.

> **Note:** You cannot change the task group or task type while editing. For other parameters, refer to Create a Scheduling Task.

**Run a Scheduling Task Once**

On the **Task List** page, click **Run Once** in the **Actions** column to run the task immediately.

**Enable and Disable Scheduling Tasks**

Enable or disable a single task i. On the **Task List** page, click **Actions**, then click **Enable/Disable** to enable or disable the scheduling task. ii. In the **Confirm** dialog box, click **OK**. Enable or disable multiple tasks On the **Task List** page, select the target tasks. Click **Batch Enable** or **Batch Disable** below the list. In the **Confirm** dialog box, click
**OK**.

**Copy a Scheduling Task**

On the **Task Progress** page, click in the Actions column, and then click **Copy** in the popup menu. This copies the configuration of the scheduling task, and you can edit the copied task to create a new scheduling task.

**Refresh Scheduling Task Data**

If your business changes—for example, you add a field to your database or find errors in last month’s data—you can refresh task data to rerun tasks for a past time period.

> **Note:** Both tasks and workflows support data refresh. Only day-level scheduling cycles are supported.

If data from a previous task run contains drift or gaps, reset the runtime parameters and run the task again to retrieve correct data. ole user guide
1. On the **Task Management** page, click
in the Actions column of the task list, and in the pop-up menu, click **Refresh Data**.
2. On the **Refresh Task** page, set **Start and End Time** and **Data Timestamp**. Then click
**OK**.
**Start and End Date**: The time range for data refresh.
**Data Timestamp**: The timestamp used for each refresh within the time range.
Example Start and End Date: 2025-08-01 to 2025-08-03. Runs from 00:00:00 on August 1, 2025, to 23:59:59 on August 3, 2025. Data Timestamp: 10:10:10 The task runs three times, with these data timestamps: 2025-08-01 10:10:10 2025-08-02 10:10:10 2025-08-03 10:10:10

**View Execution and Management Records**

View execution records: On the **Task Progress** page, click in the **Actions** column, and then click **History** in the pop-up menu to view the execution records of this scheduling task. View operation records: On the **Task List** page, click in the **Actions** column, and then click **Operation Records** to view the management operation records for the scheduled task.

**Delete a Scheduling Task**

Delete a single task i. On the **Task Progress** page, click in the **Actions** column. In the pop-up menu, click
**Delete**.
ii. In the **Confirm** dialog box, click **OK**. Delete multiple tasks On the **Task List** page, select the target tasks. Click **Batch Delete** below the list. In the **Confirm** dialog box, click **OK**.

**Import Tasks**

1. On the **Task List** page, click **Import** above the list.
2. In the **Import Task** dialog box, configure the following parameters. Then click **OK**.

| Parameter | Description |
|---|---|
| Select Application ID | Select the application to import the task into. |

ole user guide

| Same Task | Overwrite: Replace an existing task with the same name or ID. Skip: Skip importing a duplicate task and keep the existing one. |
|---|---|
| Import Task | Click the icon. Select the local file. Click Open. |

**Export task**

1. On the **Task List** page, click **Export** above the list.
2. In the **Export Task** dialog box, select an application ID. Then click **OK**.

> **Note:** By default, all tasks are exported.

3. In the dialog box that appears, click **Download**. View the downloaded tasks locally.

**Assign Machines to a Task**

1. On the **Task List** page, in the **Actions** column, click
, and in the pop-up menu, click
**Specify Machine**.
2. In the **Machine List**, select machines. Then click **OK**.

> **Note:** If machine transfer is enabled, the task runs on non-assigned machines when all assigned machines go offline.

### 6.4 Workflow Management

SchedulerX supports cross-application task orchestration. You can orchestrate tasks from the same or different applications into a single workflow based on their execution logic.

**Create Workflow**

You can create workflow Scheduling Tasks.

> **Note:** Currently, workflow scheduling supports only Cron expressions and API scheduling.

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Workflow Management**.
3. On the **Workflow Management** page, click **Create**.
4. On the **Create Workflow** page, set the following parameters and click **OK**.
ole user guide

| Parameter | Description |
|---|---|
| Name | Customize the workflow name. |
| Description | The description of the workflow. |
| Group ID | Select an application group. If no application groups are available, refer to Application Management to create an application group. |
| Time Type | Select Cron or API. |
| Cron Expression | Note This field appears when Time Type is set to Cron. Enter a cron expression. You can also click to use the generation tool to automatically generate one. For more information, see Cron. |
| Time Zone | Select a time zone as needed. Options include common countries or regions and standard GMT expressions. |
| Instance Concurrency | The maximum number of instances a workflow supports. The default value is 1, and the maximum is 100,000,000. |
| Calendar | Import a custom calendar. This lets you schedule tasks to run on specific dates, meeting particular business needs. |

5. In the workflow list, click the name of the workflow that you created, or click **Edit** in the
**Actions** column.
6. On the **Workflow Details** page, click **Create Job** or **Import Job** to add scheduling tasks.
**Create Job**: The steps are the same as those for creating a scheduling task. For more
information, see Create Scheduling Tasks.
**Import Job**: Import an existing Job into the workflow.

> **Note:** When you import a Job, a prompt appears: "Importing this Job will remove its scheduled configuration." Click **OK**. The Job will no longer be scheduled independently and will instead follow the workflow's scheduling cycle.

ole user guide
7. After you add the scheduling tasks, connect them with lines to define their dependencies
and complete the workflow. In a workflow, you can pass data from upstream Jobs to downstream Jobs. For more information, see Passing data between upstream and downstream Jobs in a workflow. To delete a dependency between two tasks, select the connecting line, right-click it, and select **Remove**. To delete a task, right-click the scheduling task and click **Remove** in the shortcut menu. You can also click a task name and select **Edit** to modify the task. An example workflow is shown below: In this workflow, after Job 101 finishes executing, Jobs 102 and 103 start executing simultaneously. After Jobs 104, 105, and 106 all execute successfully, Job 107 starts executing.
8. After you configure the workflow, click **Save Changes** and return to the **Workflow**
**Management** page. In the **Actions** column for the target workflow, click **Run Once** to test
it. After you confirm that it works correctly, click **Enable**. The workflow is then enabled and scheduled automatically.

**Enable/Disable Workflows**

1. On the **Workflow Management** page, click **Enable/Disable** in the **Actions** column to
enable or disable the workflow.
2. In the **Confirm** dialog box, click **OK**.

**Modify Workflow**

1. On the **Workflow Management** page, click **Edit** in the **Actions** column.
2. On the **Workflow Details** page, click **Edit Workflow**.
3. In the **Edit Workflow** panel, modify the workflow parameters and click **OK**.

**Delete Workflow**

1. On the **Workflow Management** page, click the
icon in the **Actions** column and select
**Delete**.
2. In the **Confirm** dialog box, click **OK**.

**View Workflow History and Operation Records**

ole user guide View execution records: On the **Workflow Management** page, click the icon in the
**Actions** column and select **History** to view the execution records of the workflow. For
more information, see Execution list. View operation records: On the **Workflow Management** page, click the icon in the
**Actions** column and select **Operation Records** to view the management operation
records for the workflow. For more information, see Operation records.

**Refresh Workflow Data**

If your business requirements change, such as adding a field to a database or discovering incorrect data from a previous month, you can re-run a workflow's tasks for a past period by refreshing the workflow data.

> **Note:** Only day-level scheduling cycles are supported.

1. On the **Workflow Management** page, click the
icon in the **Actions** column and select
**Flush Data**.
2. On the **Refresh Data** page, set **Start and End Time** and **Data Timestamp**, and click **OK**.
**Start and End Date**: The time range for the data refresh.
**Data Timestamp**: The specific time for the data refresh within the specified time range.
Example Start and End Date: 2025-08-01 to 2025-08-03. By default, this specifies the period from 00:00:00 on August 1, 2025, to 23:59:59 on August 3, 2025. Data Timestamp: 10:10:10 The tasks in this workflow will be re-run three times, with the following data timestamps: 2025-08-1 10:10:10 2025-08-2 10:10:10 2025-08-3 10:10:10

**Import Workflow**

1. On the **Workflow Management** page, click **Import** above the list.
2. In the **Import Workflow** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

ole user guide

| Select Application ID | Select the target application to import the workflow into. Note The application ID of the original workflow and the application IDs of tasks within the workflow must match the application ID of the new environment. |
|---|---|
| Identical Tasks | Overwrite: If the target environment already has tasks with the same name or ID, the imported tasks will replace the existing tasks. Skip: If duplicate tasks are found, skip importing them and keep the existing tasks. |
| Import Workflow | Click the icon, select the local object file, then click Open. |

**Export Workflow**

1. On the **Workflow Management** page, click **Export** above the list.
2. In the **Export Workflow** dialog box, select the application ID and click **OK**.
3. In the pop-up dialog box, click **Download** to save the workflow file to your local machine.

### 6.5 Application Management

The Application Management page lets you create application groups, test machine connections, authorize RAM users, and delete unneeded groups.

**Create Application Group**

You can create an application group. The Group ID and AppKey for this group are configuration parameters that applications use to access task scheduling.
1. Log on to the SchedulerX console.
2. In the left navigation pane, select **Application Management**.
3. On the **Application Management** page, click **Create**.
4. On the **Create Application** panel, configure the following parameters on the **Basic**
**Configuration** tab, and then click **Next**.

| Parameter | Description | Default |
|---|---|---|
| Applicatio n Name | Customize the application name. | None |

ole user guide

| Group ID | The Group ID for application access. This value must be unique in the system; otherwise, creation fails. | None |
|---|---|---|
| Descriptio n | Custom description. | None |
| Load5 Threshold | Cannot exceed the number of available CPU cores on the client machine. | 0 |
| Memory Usage | The average memory usage of the process over the last 5 minutes cannot exceed this threshold. If it does, the client machine is considered busy. | 90% |
| Disk Usage | Disk usage cannot exceed this value. If it does, the client machine is considered unhealthy and busy. | 95% |
| Allow triggers on busy machines? | Continue triggering client execution when the machine is busy. | Open |
| Throttle | Select whether to enable throttling. If enabled, set the Task Instance Concurrency. | Disabled |
| Task Instance Concurren cy | If throttling is enabled, this is the maximum number of task instances an application can run concurrently. Task instances exceeding this concurrency are not discarded; they wait in an application-level task queue for execution. | None |
| Maximum Number of Tasks | The maximum number of tasks a group supports. The maximum task count cannot exceed 1000. | None |
| Calendar | Import a custom calendar. Set scheduled tasks to run on specific dates to meet specific business needs. | None |

5. On the **Create Application** panel, select the **Alert Method** and add **Alert Contacts** on
the **Notification Configuration** tab. Then, click **Submit**.

| Configuration Item | Description | Example Value |
|---|---|---|
| Alert Method | DingTalk Email | DingTalk |
| Add Alert Contact | Enter the Nickname, Email, and DingTalk access token. _ | None |

ole user guide After the application group is created, you are automatically returned to the **Application**
**Management** page. Find the application group and obtain its **Group ID** and **AppKey**.

**View Application Group Details**

After you create an application group, you can view its details.
1. On the **Application Management** page, in the group list, click **Details** in the **Actions**
column.
2. You can view the application group's **Basic Configuration** and **Notification**
**Configuration** on the **Details** panel.

**Connect Machines**

After an application connects to task scheduling, you can check if the scheduling task is successfully connected by connecting machines. To do this, follow these steps:
1. On the **Application Management** page, in the **Actions** column of the group list, click
**Connect Machines**.

> **Note:** If the message "No available machines" appears and you are not directed to the **Connect Machines** page, the application's task scheduling connection failed.

2. On the **Connect Machines** page, view the list of client machines in this task group and the
status of each client machine. The number in parentheses after the client machine's IP address indicates how many SchedulerX clients are on that machine. Typically, there is one client, but a single machine supports multiple clients. Client machines have two statuses: healthy and busy. By default, tasks are not sent to busy machines. This can cause tasks to fail if all connected machines are busy. To force tasks to be sent to busy machines, you can set the **Filter Busy Machines** switch to disabled in the alert configuration.

**Authorization**

An Alibaba Cloud account can authorize RAM users based on application groups. To do this, follow these steps:
1. On the **Application Management** page, in the group list, click
in the **Actions** column. In the menu, click **Authorize**.
2. In the **Authorization Management** dialog box, select the RAM users to authorize from the
left list. Click **>>** to add the RAM users to the right list. Then, click **Authorize**.

**Delete Application Group**

ole user guide You can delete an application group after confirming that you will no longer create scheduling tasks through it. After deletion, all scheduling tasks associated with that group will no longer execute.
1. On the **Application Management** page, click **Delete** in the **Actions** column of the group
list.
2. In the delete confirmation dialog box, click **OK**.

**Modify Application Group**

1. On the **Application Management** page, in the **Actions** column of the group list, click
. Then, click **Edit**.
2. On the **Edit Application** panel, you can modify the task group information.

**View Application Group Operation Records**

1. On the **Application Management** page, in the **Actions** column of the group list, click
and then select **Operation Records**.
2. You can view the application group's operation details on the **Operation Records** page.
For more information, see the referenced document.

### 6.6 Operation records

The Operation records page lists the operation records for application groups, jobs, and flows.

**Procedure**

1. Log on to the SchedulerX console.
2. In the navigation pane on the left, click **Operation Records**.
3. On the **Operation Records** page, set **Type** to **Application Group**, **Task**, or **Flow**, enter
the corresponding ID in the text box, and then click Search.
4. In the search results, view the operation records for the corresponding group, task, or flow.
nced features

## 7 Advanced features

### 7.1 Create a second-level scheduling task

**scheduling task**

Second-level tasks are ideal for services with high real-time requirements, such as near-realtime services that perform continuous polling. Memory grid and second-level scheduling allow you to continuously process large volumes of data. This topic provides an example of how to create a second-level scheduling task. In SchedulerX 2.0, second-level tasks are a type of timed scheduling. They apply to simple Java tasks, distributed Java tasks, and script tasks, and support all execution methods. Because second-level scheduling is a type of timed scheduling, set the **Time Type** to second_delay and the **Fixed Delay** to 50 seconds in the scheduling configuration step. For more information, see Create a scheduling task.

**View second-level scheduling task details**

To view the details of a task instance, see Execution list. The details page of a second-level task instance includes a **Second-level Task Statistics** tab. This tab provides the following information: The total number of executions, successes, and failures for the current day. The total number of executions, successes, and failures for the previous day. The results of the 10 most recent executions. Details for subtasks in each loop, including the total number of subtasks and the number of successes and failures for each distribution level. nced features

**Set alerts for second-level scheduling tasks**

A task execution failure alert is triggered if the initial execution fails. After a successful initial execution, subsequent failures do not trigger this alert. A consecutive failure alert is triggered if a task fails more than 10 times consecutively after a successful initial execution. To receive these two alerts, enable the failure alert switch in the task's alert configuration.

### 7.2 Create a new account

This topic explains how to create a new account for SchedulerX.

**Prerequisites**

Contact the operations administrator to request an account. nced features

**Verify the result**

Log on to the console with your username and password to verify that the account was created successfully.

**Log out**

Click the profile picture in the upper-right corner, and then click **Log Out**.

### 7.3 How to pass data between upstream and downstream nodes in a workflow

**upstream and downstream nodes**

**in a workflow**

The workflow feature in SchedulerX 2.0 enables you to orchestrate multiple nodes. It also supports passing data between upstream and downstream nodes to simplify your business processes. This topic demonstrates how to pass data between nodes in a workflow using three scheduled jobs as an example.

**Background information**

Currently, data passing is supported only for simple Java tasks. For distributed Java tasks, use the MapReduce model to pass data. For more information, see MapReduce model.

**Usage**

Data passing is currently supported only for Java tasks. For distributed Java tasks, you must use the MapReduce model. Return an execution result

```
/**
```

`*`

```
 * @param status
 * @param result The size must be less than 1000 bytes.
 * @throws Exception
```

`*/`

```
public ProcessResult(boolean status, String result) throws Exception;
```

Use this method at the end of the processor to return the execution result. nced features

> **Important:** The size of `result` cannot exceed 1000 bytes. This limit is based on the byte size, not the number of characters in the string. A string that contains multi-byte characters can exceed this limit. If the size exceeds 1000 bytes, the task fails.

Obtain input data

```
List<JobInstanceData> upstreamDatas = JobContext.getUpstreamData();
```

In a processor, you can use this interface to obtain input data from JobContext. The input data is a list because a node can have multiple parent nodes. The JobInstanceData object has two properties: **jobName** and **data** (String).

**Procedure**

The following procedure demonstrates how to pass data between upstream and downstream nodes in a workflow.
1. Implement the job processor classes JobProcessor A, JobProcessor B, and JobProcessor C in
three separate applications. JobProcessor A

```java
public class TestSimpleJobA extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("TestSimpleJobA " + DateTime.now().toString("yyyy-MM-dd
HH:mm:ss"));
        return new ProcessResult(true, String.valueOf(1));
```

`}` `}` JobProcessor B

```java
public class TestSimpleJobB extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        System.out.println("TestSimpleJobB " + DateTime.now().toString("yyyy-MM-dd
HH:mm:ss"));
        return new ProcessResult(true, String.valueOf(2));
```

`}` `}` JobProcessor C nced features

```java
public class TestSimpleJobC extends JavaProcessor {
    @Override
    public ProcessResult process(JobContext context) throws Exception {
        List<JobInstanceData> upstreamDatas = context.getUpstreamData();
        int sum = 0;
        for (JobInstanceData jobInstanceData : upstreamDatas) {
            System.out.println("jobName=" + jobInstanceData.getJobName()
                    + ", data=" + jobInstanceData.getData());
            sum += Integer.valueOf(jobInstanceData.getData());
```

`}`

```java
        System.out.println("TestSimpleJobC sum=" + sum);
        return new ProcessResult(true, String.valueOf(sum));
```

`}` `}`
2. Create an application group and a scheduled job for each of the three applications: jobA,
jobB, and jobC. For more information, see Create an application group and Create a scheduled job.
3. Create a workflow and import the three scheduled jobs. For more information, see Create a
workflow. The created workflow is shown in the following figure.
4. On the **Flow Management** page, find the workflow and click **Run Once** in the **Actions**
column.

**Execution result**

Go to the **Workflow Details** page. To view the details for the task instances, right-click jobA, jobB, and jobC, and select **Details** from the shortcut menu. The **Result or Error Message** for Job A is 1, which matches the output of JobProcessor A. Similarly, the result for jobB is 2, which matches the output of JobProcessor B. The result for jobC is 3 (1+2). This shows that the upstream nodes jobA and jobB passed their data to jobC. This behavior matches the code in JobProcessor C. The console displays the same output.

```
jobName=jobB, data=2 jobName=jobA, data=1 TestSimpleJobC sum=3
```

guration reference

## 8 Configuration reference

### 8.1 JobContext parameters

This topic describes the JobContext parameters. The following table describes the JobContext parameters.

| Parameter | Description |
|---|---|
| long jobId | The Job ID. |
| long jobInstanceId | The job instance ID. |
| long wfInstanceId | The workflow instance ID. |
| long taskId | The subtask ID of a distributed task. The ID of the root task is 0. |
| DateTime scheduleTime | The scheduled time of the instance. |
| DateTime dataTime | The data timestamp of the instance. |
| String jobType | The job type. |
| String taskName | The subtask name. |
| Object task | The body of the subtask. |
| String jobParameters | The static job parameters configured in the console. |
| String instanceParameters | The dynamic instance parameters triggered by an API call. |
| int maxAttempt | The maximum number of retries for the instance. |
| int attempt | The current number of retries for the instance. |
| int taskMaxAttempt | The maximum number of retries for the subtask. |

guration reference

| int taskAttempt | The current number of retries for the subtask. |
|---|---|
| List<JobInstanceData> upstreamData | The upstream data of the workflow instance. A workflow instance can have multiple upstream sources. The data is in the List<JobInstanceData> format. |

### 8.2 Advanced configuration parameters for task management

**parameters for task management**

This topic describes the advanced configuration parameters for task management. The following table describes the advanced configuration parameters for task management.

| Parameter | Applicable execution modes | Description | Default value |
|---|---|---|---|
| Instance retries on failure | All | The number of times a task automatically retries if it fails. | 0 |
| Instance retry interval on failure | General | The interval between retries if a task fails. Unit: seconds. | 30 |
| Instance concurrency | General | The number of instances of the same Job that can run concurrently. A value of 1 means that concurrent execution is not allowed. | 1 |
| Sub-task concurrency per machine | Parallel computing Memory grid Grid computing | In a distributed model, this is the number of sub-tasks that a single machine can concurrently process. | 5 |
| Sub-task retries on failure | Parallel computing Memory grid Grid computing | In a distributed model, this is the number of times a sub-task automatically retries if it fails. | 0 |

guration reference

| Sub-task retry interval on failure | Parallel computing Memory grid Grid computing | In a distributed model, this is the interval between automatic retries if a sub-task fails. Unit: seconds. | 0 |
|---|---|---|---|
| Sub-task dispatch method | Parallel computing Memory grid Grid computing | Push model: Sub-tasks are evenly assigned to each machine. Pull model: Each machine actively pulls sub- tasks. This prevents the slowest machine from creating a bottleneck. During the pull process, all sub- tasks are cached on the Master node, which consumes memory. The number of sub-tasks should not exceed 10,000. | None |
| Number of sub-tasks per pull (pull model only) | Parallel computing Memory grid Grid computing | The number of sub- tasks that a slave node pulls from the Master node in a single attempt. | 5 |
| Sub-task queue capacity (pull model only) | Parallel computing Memory grid Grid computing | The size of the queue on a slave node that caches sub-tasks. | 10 |
| Global sub-task concurrency (pull model only) | Parallel computing Memory grid Grid computing | The distributed pull model supports global sub-task concurrency, which can be used for rate limiting. | 0 |

### 8.3 SchedulerxWorker configuration parameters

**configuration parameters**

This topic describes the parameters for configuring SchedulerxWorker. The following table lists each parameter and its description. guration reference

| Parameter | Description | Default value |
|---|---|---|
| setGroupId(String groupId) | Specifies the ID of the task group. Before you connect a client, create a task group and obtain its groupId. | None |
| setAppKey(String appKey) | The appKey that corresponds to the groupId. You can obtain the appKey from the Application Management page in the console. | None |
| setEndpoint(String endpoint) | The server endpoint for each region. | None |
| setNamespace(String namespace) | The ID of the namespace. | None |
| setEnableBatchWork(boolean enableBatchWork) | Specifies whether to enable grid computing. This feature is enabled by default. If you do not use grid computing, do not configure this parameter. If you use grid computing, enable this parameter. Otherwise, the first trigger on each machine is delayed by at least 20 seconds. | true |
| setHost(String host) | If a client has multiple network interface cards (NICs) or is in a VPN environment, the automatically obtained local IP address might be incorrect. Use this parameter to specify the correct IP address. | None |
| setPort(int port) | Lets you specify a custom listener port for the client. | None |
| setClassLoader(ClassLoader userClassLoader) | For non-Spring applications that use other third-party frameworks, you may need to set a custom class loader. | None |
| setBlockAppStart(boolean block) | Specifies whether to block the application process from starting if SchedulerX initialization fails. | true |

|   | setGroupId(String |   |
|---|---|---|
| groupId) |   |   |

|   | setAppKey(String |
|---|---|
| appKey) |   |

|   | setEndpoint(String | T |
|---|---|---|
| endpoint) |   |   |

|   | setNamespace(String | The |
|---|---|---|
| namespace) |   |   |

|   | setEnableBatchWork(boolean | computing, do this parameter. |
|---|---|---|
| enableBatchWork) |   |   |

|   | setClassLoader(ClassLoader | use other third-pa |
|---|---|---|
| userClassLoader) |   |   |

|   | setBlockAppStart(boolean | appli |
|---|---|---|
| block) |   |   |

ssion management

## 9 Permission management

### 9.1 Overview of permission management

**management**

This topic describes the key permission management capabilities of SchedulerX when integrated with Resource Access Management (RAM).

**Support for Alibaba Cloud accounts and RAM users**

SchedulerX uses the authentication system for Alibaba Cloud accounts and RAM users. An Alibaba Cloud account has full permissions on all its resources and for all operations in SchedulerX. The Alibaba Cloud account creates RAM users and grants them permissions. Currently, the only permission that SchedulerX manages through RAM is the logon permission. After an Alibaba Cloud account grants the logon permission to a RAM user, the RAM user has full permissions for all operations in SchedulerX. Resources created by a RAM user are not visible to other RAM users. The Alibaba Cloud account can view all resources created by its RAM users.

**Logon permission control**

A RAM user cannot directly log on to SchedulerX. To log on, the RAM user must meet the following two conditions: The RAM user must have the **Resource User** role. The Alibaba Cloud account must grant the RAM user the permission to log on to SchedulerX. The access policy for this permission is: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": "schedulerx:ManageMenu",
      "Resource": "acs:schedulerx:*:*:*",
      "Effect": "Allow"
```

`}` `]` `}`

**Application-level permission management**

Different RAM users are typically responsible for different applications. An application created by a RAM user is not visible to other RAM users, but is visible to the Alibaba Cloud account. Both the Alibaba Cloud account and the RAM user who created the application can grant permissions on it to other RAM users.

### 9.2 Create users and user groups

You can use an Alibaba Cloud account to create users and assign roles to them to manage system access.

**Create an organization**

An organization is required to create users and user groups. ssion management
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Organizations**.
4. In the left-side Organization Structure pane of the **Organizations** page, select a parent
organization and click **Create Organization** in the upper-right corner of the page.

> **Note:** If you select the root organization, a level-1 organization is created.
> If you want to create a level-2 organization, you must select a level-1 organization. The same method applies to subordinate organizations. You can create up to five levels of organizations.
> An operations administrator can create level-1 to level-5 organizations. An organization administrator can create only subordinate organizations under the organization to which the organization administrator belongs.

5. In the **Add Organization** dialog box, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|
| Name | The name of the organization. The name must be 2 to 128 characters in length. The name cannot start or end with a space. Note The organization name must be unique in the organizational architecture. |
| Description | The description of the organization. |
| Associate Third-party Authenticatio n | If no global identity provider (IdP) is configured in the Apsara Uni-manager Management Console, you can select Set Now or Set Later. If you select Set Now, you must select a local IdP name from the IdP Name drop-down list. You can associate only one IdP with the organization. If you select Set Later, third-party authentication is not associated. Important The Associate Third-party Authentication parameter is displayed only when you create a level-1 organization. If a global IdP has been configured in the Apsara Uni-manager Management Console, third-party authentication cannot be associated with level-1 organizations. In this case, Set Now and Set Later are dimmed. |

6. Click **OK**.

**Create a user group**

ssion management Roles cannot be attached directly to users. Instead, roles are attached to user groups. Users in a group inherit the permissions of the roles attached to that group.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users** > **User Groups**.
3. On the **User Groups** page, click **Create User Group**.
4. In the **Create User Group** dialog box, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|
| User Group Name | The name of the user group. The name must be 3 to 255 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), and at signs _ (@). |
| Organization | The organization to which the user group belongs. |
| Role authorized | The roles that are assigned to the user group. |

5. Click **OK**.

**Create a user**

You can create users as needed.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users** > **Users.**
3. On the **System Users** tab, click **Create User**.
ssion management
4. In the **Create User** dialog box, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| User Name | The name of the user. The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), periods (.), hyphens (-), and at signs (@). _ |
| Display Name | The display name of the user. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), spaces, and at signs (@). |
| Role | The roles that you want to assign to the user. |
| Organization | The organization to which the user belongs. |
| Logon Policy | The logon policy that limits the logon time and IP address of the user. Default value: Default Policies. |
| Phone | The mobile number of the user. This mobile number is used to receive system notifications about resource applications and usage. Make sure that the mobile number is valid. Note Make sure that you select the correct country code for the mobile number. |
| Landline | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | The email address of the user. This email address is used to receive system notifications about resource applications and usage. Make sure that the email address is valid. |
| DingTalk Key | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |

ssion management

| Message | Notify User by Email: If the user is configured as an alert contact, the Apsara Uni-manager Management Console notifies the user by email when an alert is generated. Note If you enable email notifications, you must configure an email server. For more information, contact on-site O&M engineers. If you enable email notifications, you can select After creation, the user is notified of information such as the username and password by email. Notify User by DingTalk: If the user is configured as an alert contact, the Apsara Uni-manager Management Console notifies the user by DingTalk when an alert is generated. |
|---|---|

ssion management
5. Click **OK**.

**Add a user to a user group**

When a user is added to a user group, the user inherits the permissions of the roles attached to the group.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users > User Groups**.
3. On the User Groups page, select a condition from the drop-down list and then enter a
keyword in the search box to search for a user group. Alternatively, specify advanced filter conditions above the user group list to search for a user group.
4. Find the user group that you want to manage and click **Add User** in the **Actions** column.
ssion management
5. In the **Add User** dialog box, add users. You can manually add users or upload multiple
users at a time.

| Adding Method | Description |
|---|---|
| Manually Add | i. Set the Adding Method parameter to Manually Add ii. Select one or more users that you want to add from the left-side section and click the icon to add the selected users to the right-side section. Note You can manually add up to five users at a time. To add more than five users at a time, we recommend that you use the batch upload method. You can also select one or more users added to the right-side section and click the icon to remove the users from the right-side section. iii. Click OK. |

ssion management

|   | i. Set the Adding Method parameter to Batch Upload ii. Click Download Batch Operation Template to download the template file in the XLSX format to your local computer. |
|---|---|
| Batch Upload | iii. Fill the template file with the names of the users to be added in the template file and save the file. Note You can add up to 300 users by using a template file and upload only one template file at a time. iv. In the file upload section, upload the template file that you filled in. v. Click OK. |

ssion management

### 9.3 Create a role and attach permissions

**permissions**

SchedulerX uses the authentication system for Alibaba Cloud accounts and RAM (Resource Access Management) users. It also supports RAM authorization. You can create custom roles and attach access policies. Then, assign these roles to users to manage permissions. This topic describes how to create a role and attach user groups and access policies.

**Create a role**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Permission Management** > **Role**
**Authorization**.
4. Click **Create Custom Role** to go to the **Create Custom Role** page.
5. On the **Create Custom Role** page, expand **Advanced Create** at the bottom of the page,
and then click **Create RAM Authorization**.
6. Enter the **Basic Information**.

| Paramete r | Description |
|---|---|
| Role Name | The name of the role. |
| Descripti on | (Optional) The description of the role. |
| Sharing Scope | The visibility of the role. When an operations administrator creates a role, only Global is supported. Global: The role is shared across all organizations. This organization: The role is shared only within the current organization. Subordinate organizations: The role is shared with the current organization and its subordinate organizations. |

7. Click **Create RAM Authorization and Configure** . On the **Role Authorization** page,
configure the role authorization. Attach a user group to the role.

**Note**

You can choose not to attach a user group when you create the role. Instead, you can attach the role on the user group page. For more information, see Attach a role to a user group. a. On the **Role Authorization** page, click the **User Group Management** tab, and then click **Add User Group**. ssion management b. In the **Add User Group** dialog box, select the target user group, and then click **OK**. Attach a custom policy to the role. a. On the **Role Authorization** page, click the **Permission Management** tab, and then click **Add Access Policy**. b. In the **Add Access Policy** dialog box, click **Create Access Policy**. In the **Create**
**Access Policy** dialog box, set the basic information for the policy, and then click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a custom policy name. The name can be up to 50 characters in length. For example, ScxManageMenu . |

ssion management

| Remarks | The description of the policy. This is often used to describe the permissions that the policy grants. |
|---|---|
| Policy Document | The custom policy document is as follows: { "Version": "1", "Statement": [ { "Action": "schedulerx:ManageMenu", "Resource": "acs:schedulerx:*:*:*", "Effect": "Allow" } ] } The action in this policy, schedulerx:ManageMenu, grants the logon permission for SchedulerX. The resource is the wildcard character *, which represents all SchedulerX resources. Note Currently, only the logon permission for SchedulerX uses RAM authorization. Other permissions still use the authentication system for Alibaba Cloud accounts and RAM users. |

8. After you complete the configuration, click **OK**.

**Attach a role to a user group**

After you attach a role to a user group, all users in the group gain the permissions of that role. You can attach only one role to a user group.
1. In the top menu bar, click **Enterprise**.
2. In the navigation pane on the left, choose **Personnel Management > User Group**
**Management**.
3. On the **User Group Management** page, select the target user group, click the
in its
**Actions** column, and select **Grant Permissions**.
4. In the **Authorize** dialog box, select the target role from the **Role Authorization** drop-
down list, and then click **OK**.
5. In the **Add Role** dialog box, select the target role, and then click **OK**.

### 9.4 Verify logon permissions

This topic describes how to verify logon permissions after SchedulerX is integrated with Resource Access Management (RAM).

**Prerequisites**

A user with the **Resource User** role has been created. For more information, see Create a user. ssion management

**Log on to SchedulerX as a new user**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Middleware > Microservice Tools And**
**Platforms > SchedulerX** to open the SchedulerX console.
3. On the **Distributed Task Scheduling Platform** page, click the **Switch Account** floating
button in the lower-right corner. Select **Organization Settings** and **Region Settings**. Then, click **Administrator Access**. If the user you created does not have the permissions to log on to SchedulerX, the following error message is returned:

```json
{"errMsg":"please grant ram policy to this user","policy": { "Version": "1", "Stateme nt": [ { "Action": "schedulerx:ManageMenu", "Resource": "acs:schedulerx:*:*:*", "Effe ct": "Allow" } ] } }
```

**Grant logon permissions to the user**

You cannot use an Alibaba Cloud account to directly grant permissions to a user. Instead, you must create a role, grant the role the permissions to log on to SchedulerX, and then attach the role to a user group. Users in the user group will then have the permissions to log on to SchedulerX.
1. Create a role and grant it the permissions to log on to SchedulerX.
For more information, see: Attach SchedulerX permissions to a role
2. Attach the role to a user group.
For more information, see Attach a role to a user group.
3. **Optional:**Add the user to the user group.
If the user is already in the user group, skip this step. For more information about how to add a user to a user group, see Add a user to a user group.

**Log on to SchedulerX again**

When a user with the required permissions logs on to SchedulerX, no error message is displayed.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Middleware > Microservice Tools And**
**Platforms > SchedulerX** to open the SchedulerX console.
3. On the **Distributed Task Scheduling Platform** page, click the **Switch Account** floating
button in the lower-right corner. Select **Organization Settings** and **Region Settings**. Then, click **Role-based Access**. The user successfully logs on to the SchedulerX console.

### 9.5 Verify application-level permissions

**permissions**

This topic describes how to verify application-level permissions after SchedulerX is integrated with Resource Access Management (RAM).

**Background information**

ssion management

**g**

Different RAM users are typically responsible for different applications. Applications created by a RAM user are visible to the Alibaba Cloud account but not to other RAM users. The Alibaba Cloud account can grant permissions for an application to other RAM users. A RAM user can also grant permissions for an application to other RAM users.

**Grant application permissions to a RAM user**

1. Log on to the SchedulerX console as the Alibaba Cloud account.
2. In the navigation pane on the left, click **Application Management**.

> **Note:** The Alibaba Cloud account can view applications created by all RAM users.

3. On the **Application Management** page, select the application you want to authorize, click
in the **Actions** column, and select **Authorization**.
4. In the **Authorization Management** dialog box, enter the ID of the RAM user in the **User**
**ID** search box, click **Add**, and then click **Grant**.
You can add multiple RAM user IDs to grant permissions in a batch.

> **Note:** To revoke permissions for a user, select the user ID in the lower-right corner and click **Revoke Authorization**.

**Grant application permissions to another RAM user**

1. Log on to the SchedulerX console as a RAM user.
2. In the navigation pane on the left, click **Application Management**.

> **Note:** By default, a RAM user can view only the applications that they created and cannot view applications created by other RAM users.

3. On the **Application Management** page, select the application you want to authorize, click
in the **Actions** column, and select **Authorization**. ssion management
4. In the **Authorization Management** dialog box, enter the ID of the RAM user in the **User**
**ID** search box, click **Add**, and then click **Grant**.
You can add multiple RAM user IDs to grant permissions in a batch.

> **Note:** To revoke permissions for a user, select the user ID in the lower-right corner and click **Revoke Authorization**.

## 10 FAQ

### 10.1 FAQ

You might encounter issues when you use SchedulerX. This topic describes how to resolve common issues.

**Machine is busy**

Symptom In the console, go to the **Application Management** page. In the **Operation** column for a group, click **Connected Machines**. In the **Machine List** panel, the machine's **Status** is Busy. Possible causes The **load5** on the machine exceeds the threshold set for the task group. The machine's **Memory Usage** exceeds the task group threshold. The machine's **Disk Usage** exceeds the task group threshold. Impact If a machine is busy, scheduling tasks cannot be triggered. Solution i. In the **Connected Instances** panel, hover over **Busy** to view the machine's **Load**,
**Memory Usage**, and **Disk Usage**.
ii. Based on the values of **load5**, **Memory Usage**, and **Disk Usage**, identify the cause and take appropriate action, such as clearing the disk, releasing memory, or reducing the load. If the machine is still busy, you can upgrade its configuration. To trigger tasks on a busy machine for testing purposes, go to the **Application**
**Management** page. In the **Operation** column, click the
icon and select **Edit**. In the
**Edit Application** panel, modify the advanced configuration and enable **Trigger On Busy**
**Machine**.

**No available machines**

Symptom When you connect an application to SchedulerX and try to verify the connection, the message No available machines is displayed. Possible causes The application failed to connect to SchedulerX. There were conflicts between JAR packages. The SchedulerXWorker was configured incorrectly. Solution i. Log on to the ECS instance where the application is deployed and check if the log directory /home/${user.home}/logs/schedulerx/worker.log exists.

> **Note:** If the process is started by the root account, the log is located at /root/logs/schedulerx/worker.log.
> If the process is started by the admin account, the log is located at /home/admin/schedulerx/worker.log.

If the directory does not exist, the ECS instance is not connected to the SchedulerX client. Connect the client again. For more information, see Connect a client to SchedulerX. If the directory exists, proceed to the next step. ii. Check the `worker.log` file for abnormal logs. If the log contains groupId is not existed, it indicates a configuration issue. Search for `Schedulerx WorkerConfig` in worker.log to view the current configuration, and then compare it with the configuration on the console to confirm that it is correct.

> **Important:** Obtain the namespace ID from the **Namespace ID** on the **Namespace** page.

If there are abnormal logs, check for JAR package conflicts. For more information, see JAR package conflicts. If there are no abnormal logs, search for "started" and check if the SchedulerXWorker configuration is correct.

**JAR package conflicts**

Symptom When you deploy a scheduling task, the message JAR package conflict is displayed. Possible cause A JAR package conflict can be caused by conflicts between specific sub-packages. You can search for **maven dependencies** in the log to view the version and path of each JAR package. This helps you quickly locate and resolve the conflict, as shown in the following figure: Solution Upgrade the packages that have earlier versions, as specified in the following table.

| JAR package | Version |
|---|---|
| guava | 20.0 |

| com.typesafe.config | 1.3.0 |
|---|---|
| protobuf-java | 2.6.1 |
| io.netty | 3.10.6.Final |
| javaassist | 3.21.0-GA |
| hessian | 4.0.51 |
| commons-configuration | 1.10 |
| commons-validator | 1.4.0 |

Examples The following list describes typical JAR conflict symptoms: guava conflict com.typesafe.config package conflict protobuf conflict

```
2019-03-20 14:49:41.742 [33471_69216-akka.actor.default-dispatcher-4] WARN co m.alibaba.schedulerx.worker.SchedulerxWorker:315 - heartbeat error java.lang.VerifyError: class com.alibaba.schedulerx.protocol.Worker$WorkerHeartBeatRequest overrides final me thod getUnknownFields.()Lcom/google/protobuf/UnknownFieldSet; at java.lang.ClassLoader.defineClass1(Native Method) ~[?:1.8.0_181] at java.lang.ClassLoader.defineClass(ClassLoader.java:763) ~[?:1.8.0_181] at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142) ~[?:1. 8.0_181]
```

A Netty conflict causes the ActorSystem.create method to time out, which prevents the system from starting.

```
2019-03-20 11:52:48.030 [main] ERROR com.alibaba.schedulerx.worker.SchedulerxWorker:142 - Schedulerx Worker error java.util.concurrent.TimeoutException: Futures timed out after [10000 milliseconds] at scala.concurrent.impl.Promise$DefaultPromise.ready(Promise.scala:223) ~[scalalibrary-2.11.11.jar:?] at scala.concurrent.impl.Promise$DefaultPromise.result(Promise.scala:227) ~[scala -library-2.11.11.jar:?] at scala.concurrent.Await$$anonfun$result$1.apply(package.scala:190) ~[scala-libr ary-2.11.11.jar:?]
```

`at`

```
scala.concurrent.BlockContext$DefaultBlockContext$.blockOn(BlockContext.scala:53) ~[scala-library-2.11.11.jar:?] at scala.concurrent.Await$.result(package.scala:190) ~[scala-library-2.11.11.jar:
```

?]

```
at akka.remote.Remoting.start(Remoting.scala:189) ~[akka-remote_2.11- 2.4.20.jar:?] at akka.remote.RemoteActorRefProvider.init(RemoteActorRefProvider.scala:212) ~[ak ka-remote_2.11-2.4.20.jar:?] at akka.actor.ActorSystemImpl.liftedTree2$1(ActorSystem.scala:828) ~[akka-actor_2 .11-2.4.20.jar:?] at akka.actor.ActorSystemImpl._start$lzycompute(ActorSystem.scala:825) ~[akka-act or_2.11-2.4.20.jar:?] at akka.actor.ActorSystemImpl._start(ActorSystem.scala:825) ~[akka-actor_2.11-2.4 .20.jar:?] at akka.actor.ActorSystemImpl.start(ActorSystem.scala:841) ~[akka-actor_2.11-2.4. 20.jar:?] at akka.actor.ActorSystem$.apply(ActorSystem.scala:245) ~[akka-actor_2.11-2.4.20. jar:?] at akka.actor.ActorSystem$.apply(ActorSystem.scala:288) ~[akka-actor_2.11-2.4.20. jar:?] at akka.actor.ActorSystem$.apply(ActorSystem.scala:263) ~[akka-actor_2.11-2.4.20. jar:?] at akka.actor.ActorSystem$.create(ActorSystem.scala:191) ~[akka-actor_2.11-2.4.20 .jar:?] at akka.actor.ActorSystem.create(ActorSystem.scala) ~[akka-actor_2.11- 2.4.20.jar:?] at com.alibaba.schedulerx.worker.SchedulerxWorker.init(SchedulerxWorker.java:119) [schedulerx-worker-0.2.0.jar:?]
```

Hessian conflict

```
java.lang.NoSuchMethodError: com.caucho.hessian.io.SerializerFactory.createDefault()Lcom/caucho/hessian/io/Seriali rFactory;
```

commons-validator conflict

```
Caused by: java.lang.NoClassDefFoundError: org/apache/commons/validator/routines/InetAddressValidator
```

`at`

```
com.aliyun.openservices.log.util.NetworkUtils.getLocalMachineIP(NetworkUtils.java:33) ~[aliyun-log-0.6.31.jar:?]
    at com.aliyun.openservices.log.Client.<init>(Client.java:250) ~[aliyun-log-0.6.
31.jar:?]
```

`at`

```
com.aliyun.openservices.aliyun.log.producer.ProjectConfigs.buildClient(ProjectConfigs ava:34) ~[aliyun-log-producer-0.2.0.jar:?]
```

`at`

```
com.aliyun.openservices.aliyun.log.producer.ProjectConfigs.put(ProjectConfigs.java:13 ~[aliyun-log-producer-0.2.0.jar:?]
    at com.alibaba.schedulerx.worker.logcollector.SlsLogCollector.<init>
(SlsLogCollector.java:64) ~[schedulerx-worker-1.0.3.jar:?]
    at sun.reflect.GeneratedConstructorAccessor156.newInstance(Unknown Source) ~[?:
```

?] `at`

```
sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccess Impl.java:45) ~[?:1.8.0_161]
    at java.lang.reflect.Constructor.newInstance(Constructor.java:423) ~
[?:1.8.0_161]
```

`at`

```
com.alibaba.schedulerx.common.util.ReflectionUtil.newInstance(ReflectionUtil.java:31) ~[schedulerx-common-1.0.2.jar:?]
```

javaassist conflict httpclient conflict

**Incompatibility between tablestore protobuf-2.4.1 and**

**SchedulerX**

For more information, see Protobuf library conflict when using Java SDK.

**Spring application cannot find a bean**

Symptom The Spring application cannot find the corresponding bean. Possible causes Incorrect connection type. A bean is not injected into the JobProcessor. The `spring-boot-devtools` dependency is added to the pom.xml file. Transaction annotations are added to the JobProcessor and the process method. The bean is proxied by other aspects. Inconsistent classLoaders. Solution On the **Application Management** page in the console, click **Connected Machines** in the **Operation** column of the target group. In the **Connected Machines** panel, check that the startup mode is Spring or Spring Boot. If the startup mode is not Spring or Spring Boot, check your application. Check whether the JobProcessor is injected as a bean in the application code, for example, by adding the @Component annotation. If the JobProcessor is not injected as a bean, inject it as a bean. Check whether `spring-boot-devtools` is added to the pom.xml file.

| If | spring-boot-devtools |   |
|---|---|---|
| devtools |   |   |
|   |   | dependency. |

If `spring-boot-devtools` is added to the pom.xml file, delete the `spring-boot-` Check whether transaction annotations are added to the JobProcessor and the process method. If transaction annotations are added to the JobProcessor and the process method, delete the annotations. Check whether the bean list is proxied by other aspects. Set a breakpoint in the DefaultListableBeanFactory class. Check whether the beanDefiniti onNames member list, which is the list of beans registered with Spring, is proxied by other aspects. If the bean list is proxied by other aspects, delete the proxy. Debug ThreadContainer.start and check for a class.forName error. If a class.forName error occurs but the class exists, the issue is with the classLoader. This might be because a framework you are using causes classLoader inconsistency. You can use SchedulerxWorker.setClassLoader to resolve this issue. If none of these methods resolve the issue, contact the SchedulerX helpdesk.

**Incompatibility between tablestore protobuf-2.4.1 and**

**SchedulerX**

For more information, see Protobuf or HttpClient library conflict when using Java SDK.

**submit jobInstanceId to worker timeout**

Symptom

```
submit jobInstanceId=28384771 to worker=WorkerInfo [ip=192.168.32.166, port=41114, workerId=30574_7365, metrics=Metrics(cpuLoad1=0.01, cpuLoad5=0.05600000000000001, cpuProcessors=2, heap1Usage=0.20147679324894516, heap5Usage=0.20379746835443036, heap1Used=191, heapMax=948, diskUsage=0.24241670191853087, diskUsed=9742, diskMax=40187)] timeout, cost=5004ms
```

Possible causes JAR package conflicts. High machine load or machine restart. Solution Check the worker.log file for abnormal logs. If abnormal logs exist, the cause might be JAR package conflicts. For more information, see JAR package conflicts. If no abnormal logs exist, the cause might be a high machine load or a machine restart. You can check the machine.

**Task gets stuck after application restart**

Symptom The application is published without issues. However, when you restart the application using Aone, tasks get stuck. Possible cause If the system environment variable for starting the process is `user.dir="/"` but the process is not started by the root account, the underlying message notifications of SchedulerX fail. This occurs because the account does not have the permissions to write to the akka.persistence.snapshot directory. Solution Upgrade SchedulerX to version 1.0.9-hotfix-v3 or later.

**Task gets stuck during execution**

Symptom A scheduling task is always in the running state and does not end. Possible causes A business logic issue. A SchedulerX issue. Solution When `schedulerx-worker` executes each processor, it adds the task instance ID to the thread name to help you view the thread stack. This section uses a stuck sub-task of a distributed task as an example. The solution for a standalone task or a broadcast task is similar. i. On the **Execution List** page in the console, view the details of the stuck task instance to retrieve its instance ID. ii. Log on to the stuck machine and run **jstack [pid] | grep [instance id] -A 20** to view the thread stack. If the execution result is similar to the one shown in the following figure, the cause is a business logic issue. Otherwise, contact the SchedulerX helpdesk.

### 10.2 Alert FAQ

This topic describes how to handle the alerts that you may receive when using SchedulerX.

**killed from server**

Alert message The timed scheduling task in your ****** environment, namespace: default space, jobid:******, trigger instance id:******, failed at 2025-10-15 07:40:57. The task ran on machine ******. The reason may be 'killed from server'. Please monitor the task. [SchedulerX access ******.com]. Description This alert indicates that a task was automatically purged because it timed out.

**don't update progress more than 30s**

Alert message The timed scheduling task in your ****** environment, namespace: default space, jobid:******check_if_complete_BACKIP1), trigger instance id:******, failed at 2025-10-15 07:40:57. The task ran on machine ******. The reason may be 'jobInstance=*** don't update progress more than 30s, maybe worker=****** is down'. Please monitor the task. [SchedulerX access ******.com]. Description The connection between the client and the server was lost because no heartbeat was sent for more than 30 s. This issue is typically caused by a client deployment or high load. If the issue is caused by a deployment or restart, you can configure automatic retries for failed tasks.
