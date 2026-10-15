---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 8
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%8F%AF%E8%A7%82%E6%B5%8B%E9%93%BE%E8%B7%AF%20OpenTelemetry%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Tracing%20Analysis%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Product Introduction 20260828

ysis

## Tracing Analysis

Tracing Analysis provides developers of distributed applications with tools to restore complete call traces, collect call request statistics, visualize trace topology, and perform application dependency analysis. These capabilities help developers quickly identify and diagnose performance bottlenecks in distributed application architectures and improve development and diagnostic efficiency in the microservice era. ails

## Product details

Tracing Analysis is based on the OpenTracing standard. It supports applications written in multiple languages and reconstructs complete call traces.

**Distributed trace query and diagnostics**

You can track all user requests across microservices in a distributed architecture and aggregate them into distributed call traces.

**Real-time application performance aggregation**

You can trace user requests across your entire application to aggregate individual services and resources in real time.

**Dynamic discovery of distributed topology**

Tracing Analysis collects distributed call data from all your distributed microservice applications and related Platform as a Service (PaaS) products.

**Multi-language program integration**

Built on the OpenTracing standard, it is compatible with open source projects such as Jaeger and Zipkin.

**Rich downstream integration scenarios**

Collected traces can be used directly for log analysis and integrated with downstream analytics platforms such as MaxCompute. e

## Product value

Tracing Analysis monitors and analyzes request flows in distributed systems. It provides realtime monitoring views to help developers and Operations and Maintenance (O&M) teams identify performance bottlenecks, optimize resource allocation, and troubleshoot faults.

**Global topology**

Tracing Analysis provides a global view of your system topology. This view shows metrics such as the queries per second (QPS) and response time for calls between components.

**Response time, request count, and error count**

You can view call information from two dimensions: By node: View the overall response time, request count, and error count for each node instance in the application. By interface: View the response time, request count, and error count for each interface in the application.

**Exception analysis, call stacks, and error analysis**

Tracing Analysis helps you quickly locate problems in several ways: Compare data from today and yesterday to quickly find new and surging exceptions. Associate exceptions with requests to identify the originating requests and view the average number of exceptions per request. This ensures that no critical exceptions are missed. View exceptions from three dimensions: name, message, and interface. This helps you quickly locate the core exceptions in your system.

## Scenarios

Tracing Analysis applies to scenarios such as topology visualization, troubleshooting and diagnostics, and database call statistics.

**Topology visualization**

Tracing Analysis collects distributed calls across your system and stores and analyzes them to provide topology graph visualization, making system dependencies and access patterns immediately clear.

**Troubleshooting and diagnostics**

Tracing Analysis provides abnormal behavior analysis. You can use visualized anomaly reports, call traces, and request statistics to quickly identify issues in your system and accelerate troubleshooting.

**Database call statistics**

Databases are a core component widely used in business applications. Tracing Analysis offers database call analysis so you can monitor database access patterns in your system.
