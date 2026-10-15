---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 10
source_pdf: "0c377bd3eba58721_Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%20EDAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Enterprise%20Distributed%20Application%20Service%20%28EDAS%29%20SchedulerX%202.0%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) SchedulerX 2.0 Product Introduction 20260828

## Table of Contents

- 1 SchedulerX 2.0
  - 1.1 Product details
  - 1.2 Benefits
  - 1.3 Features
  - 1.4 Scenarios
  - 1.5 Key concepts

## 1 SchedulerX 2.0

SchedulerX 2.0 is a next-generation distributed task scheduling platform from Alibaba. It is built on the Akka framework. The platform provides features such as timed scheduling, workflow task orchestration, and distributed batch scheduling. It is highly reliable, supports a massive number of tasks, and can schedule tasks within seconds. In the console, you can configure and manage timed scheduling tasks, query task execution records, and view run logs. You can also use workflows to orchestrate tasks and transfer data. SchedulerX 2.0 provides a simple distributed programming model. This model lets you distribute large volumes of data to multiple machines for execution with only a few lines of code.

### 1.1 Product details

SchedulerX 2.0 provides three main features: scheduling, execution, and Operations and Maintenance (O&M).

**Scheduling**

SchedulerX 2.0 supports timed scheduling and workflow scheduling. Timed scheduling with various expressions Crontab: Supports standard Unix cron expressions. For more information, see Quartz Cron Expressions. Second-level scheduling is not supported. Fixed rate: Cron expressions require intervals that are divisible by 60, which means you cannot schedule a task to run every 40 minutes. The fixed rate option solves this problem. It is designed for periodic polling and uses a simple expression. Second-level scheduling is not supported. Second delay: You can use this for services that require high real-time performance, such as a scheduled task that runs every 10 seconds. This option supports second-level scheduling. Calendar: Supports multiple calendars and lets you import custom ones. This is useful for financial services, such as running a scheduled task on each trading day. Time zone: You can use this for multinational businesses, such as running a scheduled task in the local time zone of each country. Workflow scheduling You can orchestrate tasks using a directed acyclic graph (DAG). You can drag and drop nodes in the console to build your workflow. A detailed task status graph helps you determine why a downstream task did not run. Timed scheduling and workflow scheduling support multiple task types in various languages. Java: You can execute tasks in a user process or dynamically load them by uploading a JAR package. Shell: You can write Shell scripts directly in the console. Python: You can write Python scripts directly in the console. A Python environment is required. Go: You can write Go scripts directly in the console. A Go environment is required. HTTP: HTTP tasks do not require a client. You can configure them in the console to get started. Custom: You can customize task types by implementing a plugin.

**Execution**

SchedulerX 2.0 supports multiple execution methods and mainstream distributed programming models. Multiple execution methods Standalone: Randomly selects one machine to run the task. Broadcast: Runs the task on all machines at the same time and waits for all of them to finish. Parallel computing: Uses the Map/MapReduce model. Supports 1 to 300 subtasks. A subtask list is available. In-memory grid: Uses the Map/MapReduce model. Supports up to 100,000 subtasks. No subtask list is available. This method is based on in-memory computing and is faster than grid computing. Grid computing: Uses the Map/MapReduce model. Supports up to 1,000,000 subtasks. No subtask list is available. This method is based on H2 file-based computing. Sharded execution: Similar to the elastic-job model. You can configure sharding parameters in the console to distribute shards evenly across multiple clients. This feature supports multiple languages. Distributed programming models Map model: Similar to the Map function in Hadoop MapReduce. You can implement a Map method to distribute large amounts of data across multiple machines with just a few lines of code. MapReduce model: The MapReduce model extends the Map model. This model deprecates the postProcess method and adds a Reduce interface. You must implement MapReduceJobProcessor.

**O&M**

SchedulerX 2.0 supports O&M features such as data dashboards, alert monitoring, log collection, failed task retries, data timestamps, and data backfilling. Data dashboard The console provides an execution history dashboard and a list of executions. You can view the history of each task and perform related operations. View logs You can view the running log for each task execution in the details panel. If a task fails, the error log is displayed directly in the console for easy troubleshooting. Rerun in place If a task fails, you can rerun it immediately after you modify and publish the code. Mark as successful If a task fails but you have already manually corrected the data, you can directly mark the task as successful. This saves you from spending hours rerunning the task. Stop a scheduled task You can implement the `kill()` interface of JobProcessor to stop a running task or subtask from the console. Data timestamp SchedulerX 2.0 can process stateful tasks. When you create a task, you set a schedule time. The actual data that you process might have a different timestamp than the task's running time. You can configure a time offset to handle this. The data timestamp is the schedule time plus the offset. For example, a task runs at 00:30 every day to process the previous day's data. You can set the offset to -1 hour. The schedule time does not change. When the task runs, `context.getDataTime()` returns 23:30 of the previous day. Backfill data Because tasks have data timestamps, you may need to backfill data. For example, a workflow generates a report. If business requirements change, such as adding a new field, or if you find an error in last month's data, you must reprocess the data for the past month. The backfill feature lets you reprocess data for specific tasks or workflows. This feature only supports day-level backfills. Each new instance will have a different data timestamp. Automatic retry on failure Automatic instance retry: In the advanced configuration for a task, you can set the number of retries and the retry interval for a failed instance. For example, you can set it to retry 3 times at 30-second intervals. If the instance still fails after all retries, its status changes to Failed and an alert is sent. Automatic subtask retry: For distributed tasks, such as parallel, in-memory grid, and grid computing tasks, subtasks also support automatic retries. You can configure the number of retries and the retry interval in the advanced configuration for the task. Alert monitoring You can receive alert notifications by email, DingTalk, text message, or phone. Alerts are sent for failed tasks, timeouts, and when no active machines are available.

### 1.2 Benefits

SchedulerX 2.0 is a high-performance and highly reliable service that is easy to use and supports various scenarios.

**High performance**

SchedulerX 2.0 uses a distributed architecture and the asynchronous capabilities of Akka to support a massive number of tasks and second-level scheduling.

**High reliability**

SchedulerX 2.0 uses a primary/standby mechanism, at-least-once message delivery, and periodic polling to ensure high reliability for task scheduling and execution.

**Various scheduling and computing scenarios**

It supports timed scheduling, API scheduling, and task orchestration. It also supports multiple computing models, such as standalone, broadcast, and distributed computing.

**Ease of use**

The service is easy to integrate and provides many user-friendly Operations and Maintenance (O&M) tools. The frontend displays execution records and run logs. It also supports operations such as in-place reruns and data reprocessing.

### 1.3 Features

This topic describes the features of SchedulerX 2.0.

**Task scheduling capabilities**

| Feature | Description |
|---|---|
| Supports multiple types of scheduled tasks | Supports various task types across multiple languages for both timed scheduling and workflows. |

| Automatic retry on failure | Supports automatic retries for failed tasks. |
|---|---|
| Timed scheduling | Supports timed scheduling. It also supports crontab, fixed rate, and _ fixed delay expressions. _ |
| Specify machines | Supports scheduling tasks on specified machines. |
| Data timestamp | Supports data timestamp offsets to process jobs that span across days. |
| Workflow orchestration | Supports visual workflow orchestration to simplify task dependency management. |

**Task O&M capabilities**

| Features | Description |
|---|---|
| Operation records | Supports operation records for changes to applications and tasks. |

**Multi-tenant resource management**

| Feature | Description |
|---|---|
| Namespaces | Supports environment fencing using namespaces. |
| Multiple regions | Supports deployment across multiple regions, including central and regional units. |
| Permission management | Supports logon through ASCM and application-level permission management. |

**Monitoring and alerts**

| Feature | Description |
|---|---|
| Monitoring and alerts | Supports monitoring and alerts. |

**High availability capabilities**

| Feature | Description |
|---|---|

| Server-side high availability | If any server-side machine becomes unavailable, task scheduling is not affected. |
|---|---|
| Client-side high availability | If any client machine becomes unavailable, tasks do not stall. |

### 1.4 Scenarios

SchedulerX can trigger scheduled tasks at a specific time, periodically, or manually.

**Tasks triggered at a specific time**

For example, a task that runs once at 00:00 on November 11, 2025.

**Periodically triggered tasks**

For example, a task that runs every second, hour, day, week, or month.

**Manually triggered tasks from the console**

For example, you can manually trigger scheduled tasks from the console. After a task is triggered, your implementation of the Job processor interface performs the business logic. This can include actions such as scanning tables, triggering Remote Procedure Call (RPC) invocations, writing to a database, or running local scripts.

### 1.5 Key concepts

This topic describes the key concepts of SchedulerX 2.0.

**AppGroup**

An AppGroup is an application group that isolates your services. Before using SchedulerX 2.0, you must create an AppGroup, which generates a unique groupId.

**Job**

A Job is the smallest scheduling unit in SchedulerX 2.0.

**Workflow**

A workflow is a Directed Acyclic Graph (DAG) used for task orchestration.

**Job instance**

Each execution of a Job is called a job instance.

**Task**

In parallel, grid, or batch computing, the Map method generates subtasks, which are referred to simply as tasks.

**Schedule time**

The schedule time is the designated execution time for a `jobInstance` . A `jobProcessor` can retrieve this time by calling `context.getScheduleTime()` .

**Data time**

SchedulerX 2.0 introduces data time, which allows you to specify a data offset for a Job. For example, a Job might be scheduled to run at 00:30 every day but needs to process data from the previous day. You can set a backward data offset of one hour. The schedule time remains 00:30, but a call to `context.getDataTime()` during execution returns 23:30 from the previous day.
