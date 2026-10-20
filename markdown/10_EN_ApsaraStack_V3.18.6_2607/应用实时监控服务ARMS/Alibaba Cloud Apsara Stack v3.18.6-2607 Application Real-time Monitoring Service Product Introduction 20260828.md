---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 14
source_pdf: "e1de363dfaf3143e_Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Product Introductio"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%BA%94%E7%94%A8%E5%AE%9E%E6%97%B6%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1ARMS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Application%20Real-time%20Monitoring%20Service%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Product Introduction 20260828

## Table of Contents

- 1 Application Real-Time Monitoring Service
- 2 Features
- 3 Benefits
- 4 Features
- 5 Scenarios
- 6 Limits
- 7 Key concepts

Real-Time Monitoring Service

## 1 Application Real-Time Monitoring Service

**Monitoring Service**

Application Real-Time Monitoring Service (ARMS) is an application performance management (APM) service. If you want to comprehensively monitor an application, you only need to install an ARMS agent for the application without the need to modify code. ARMS can automatically generate application topologies, locate faulty and slow interfaces and request parameters, and discover system bottlenecks. This greatly improves the efficiency of diagnostics in production environments.

## 2 Features

Application Real-Time Monitoring Service (ARMS) provides quick integration, proactive diagnostics, and lossless statistics.

**Quick integration**

You can integrate applications from Enterprise Distributed Application Service into ARMS without installing an ARMS agent.

**Proactive application diagnostics**

ARMS helps you identify the root causes of various typical problems, such as slow calls, slow SQL queries, exceptions, high CPU utilization, memory overflows, and thread dumps.

**Lossless statistics**

By using agent-side pre-aggregation and separately reporting trace data and metric data, ARMS provides accurate application metrics.

**Dynamic configuration delivery**

You can configure the sampling rate, custom thresholds of slow requests, and URL convergence for an ARMS agent in the ARMS console. The configurations can be automatically delivered to the agent and take effect without the need to restart it.

**Various performance metrics**

ARMS provides multidimensional performance analysis and monitoring capabilities for applications, Java virtual machines, hosts, exceptions, errors, SQL queries, and interface snapshots.

## 3 Benefits

Application Real-Time Monitoring Service (ARMS) allows you to monitor Java applications that run in distributed architectures and view application topologies, interface calls, abnormal transactions, and slow transactions.

**Automatic generation of global topologies**

Overview of all application topologies Health status of main calls Categorized statistics of all component calls

**Code-level troubleshooting**

If a fault occurs, traditional application performance management (APM) services can only start with a specific interface or SQL statement of an application, and then locate the code based on logs and code review. However, ARMS directly locates the method stacks based on interface snapshots and automatically analyzes the time consumed by method stacks called by interfaces.

**Capturing of slow calls**

Dynamic thresholds of slow calls Automatic capturing of slow interfaces and methods Analysis of slow SQL queries

**Exception diagnostics, trace analysis, and error analysis**

Without the comparison of historical data, traditional application performance management (APM) services discover new exceptions and spikes only based on exception logs. The exception diagnostics feature of ARMS quickly locates problems by using the following methods: Compare data between the current day and previous day so that you can detect new exceptions and spikes. Display exceptions with each request so that you can clearly view the requests with exceptions and the average number of exceptions thrown by each request. Provide three dimensions to help you quickly locate the core exceptions of the system: exception name, exception details, and abnormal interfaces. The error list of the error analysis feature displays all errors of an application within a specified period of time.

**MQ performance analysis**

Topology: displays how Message Queue (MQ) messages are published and subscribed between an application and MQ data source in real time. Performance metrics: displays the number of requests that are sent and received from the publisher to the consumer, response time, and error statistics. Interface snapshot: provides interface snapshots for message publishing and subscription. Developers can view the complete trace and troubleshoot problems based on the trace ID.

**Dynamic configuration delivery**

Dynamic sampling rate Dynamic plug-in switch Custom thresholds of slow requests URL convergence settings

## 4 Features

Alibaba Cloud ARMS provides powerful application diagnostics and alert monitoring. It lets you monitor and manage application performance in real time, analyze and optimize application performance, and improve system stability.

**Application list**

| Feature | Description |
|---|---|
| Application overview | On the Application Overview page, view application information such as request count, error count, response time, and instance count. |

**Application topology**

| Feature | Description |
|---|---|
| Application topology | On the Application Topology page, view the call relationships between the internal services of an application. |

**Trace analysis**

| Feature | Description |
|---|---|
| End-to-end trace aggregation | Query for the Trace ID of a distributed trace by specifying conditions. Spans are then aggregated to generate the final result and ensure trace integrity. |
| Trace details | View the details of a trace. These details include all interfaces in the trace, the trace start time, total response time, interface status, and the response time of each interface call. |

**Application diagnostics**

| Feature | Description |
|---|---|
| Continuous profiling | ARMS proactively discovers bottlenecks in Java programs that are caused by CPU, memory, and I/O. It helps developers optimize their programs. |

**Event hub**

| Feature | Description |
|---|---|
| Topology view | Generates topology graphs for application resources. These resources include compute and storage resources such as ECS, pods, RDS, and Redis, and network resources such as SLB and NAT. |

**Alert rules**

| Feature | Description |
|---|---|
| Threshold detection | Create alert rules for specific applications. When a rule is triggered, an alert notification is sent, prompting for corrective action. |
| Interval Detection | Use dynamic thresholds to perform anomaly detection on metric data. This is suitable for fluctuating metrics, such as response time (RT) and queries per second (QPS). |
| Manage alert rules | Start, stop, edit, and delete alert rules. You can also test alerts to verify that the rules are effective. |

## 5 Scenarios

Application Real-Time Monitoring Service (ARMS) discovers application topologies, and captures exceptions and slow interfaces to diagnose application problems.

**Application topology discovery**

An ARMS agent can automatically detect upstream and downstream dependencies to efficiently capture, intelligently calculate, and automatically display the traces between different applications through the RPC framework.

**Capturing of application exceptions, slow interfaces, and slow**

**SQL queries**

Developers can obtain the stack analysis reports of slow SQL queries, accumulated Message Queue (MQ) messages, or exceptions, and conduct more detailed analysis.

**Automatic detection and monitoring of interfaces**

ARMS can automatically discover and monitor common web frameworks and RPC frameworks in application code. ARMS can also automatically collect statistics on metrics such as the number of calls, response time, and number of abnormal interfaces.

**Application problem diagnostics**

By using trace drill-down analysis, thread analysis, and exception analysis, ARMS analyzes the performance, availability, and errors of applications, and helps you locate root causes of the errors.

## 6 Limits

This topic lists the ARMS limits.

**Application monitoring**

| Item | Maximum value |
|---|---|
| Maximum nodes per application (by default, TLog outputs data from three physical machines) | 500 |
| Trace retention period | 7 days. A longer retention period requires separate evaluation. |
| Metric retention period | 7 days. A longer retention period requires separate evaluation. |
| Supported JDK versions | 1.6 1.7 1.8 |
| Maximum number of unique SQL patterns per user | 1,000 |
| Supported plugins | Refer to the ARMS User Guide > Custom Configurations. |

**Custom monitoring**

| Item | Maximum value/Description |
|---|---|
| Supported data sources | Log collection and message queue (MQ). |
| MQ data source support | Supports only topics in the default namespace. |

**General limits**

| Item | Maximum value/Description |
|---|---|
| Alerting | Available for application monitoring and custom monitoring. |

| Maximum contacts per user | 100 |
|---|---|
| Maximum alerting rules per user | 1,000 |

s

## 7 Key concepts

This topic introduces key concepts for ARMS.
**APM**: Application Performance Management. It monitors application performance by
tracking how requests are processed across frontend, backend, and server-side services. Open-source APM products include Skywalking, Pinpoint, and Zipkin. The application monitoring and trace analysis features of ARMS also fall into the APM category.
**Trace**: A trace represents the execution path of a transaction or process in a distributed
system. In the OpenTracing standard, a trace consists of multiple spans that form a Directed Acyclic Graph (DAG). Each span represents a named and timed segment of work within the trace.
**Span**: A span is the smallest execution unit of a trace. It can represent a method call, a
code block execution, a remote procedure call (RPC), or a database access. Any operation with a defined start and end time can be a span. A trace typically consists of multiple spans.
**Apdex (Application Performance Index)**: Apdex is an industry standard for measuring
user satisfaction with application performance. It classifies user experience into three levels: Satisfied (0 to T) Tolerated (T to 4T) Frustrated (greater than 4T) The formula is:

```
Apdex = (Satisfied Count + Tolerated Count / 2) / Total Samples
```

**Instance**: An instance is a machine or Pod where a monitored application is deployed.
Instances are identified at the JVM level.
**Request count**: The number of requests to an application or instance, and the number of
database operations.
**Response time**: The average response time for calls to an application or instance, and the
average execution time for database operations. Error rate: The number of failed calls for an application, instance, or database operation, divided by the total request count.
