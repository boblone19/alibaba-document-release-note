---
title: "Managed Service for Prometheus Product Introduction 20260703"
product_version: "V3.18.6"
pdf_pages: 16
source_pdf: "4f878744af3f7ab0_Alibaba Cloud Apsara Stack V3.18.6 Managed Service for Prometheus Product Introduction 20260703.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%8F%AF%E8%A7%82%E6%B5%8B%E7%9B%91%E6%8E%A7%20Prometheus%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Managed%20Service%20for%20Prometheus%20Product%20Introduction%2020260703.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Managed Service for Prometheus Product Introduction 20260703

## Table of Contents

- 1 Prometheus monitoring
- 2 Product details
- 3 Product value
- 4 Features
- 5 Scenarios
- 6 Limitations
- 7 Key concepts

monitoring

## 1 Prometheus monitoring

Alibaba Cloud Prometheus Monitoring is a fully managed Prometheus service. It fully integrates with the open source Prometheus ecosystem, supports monitoring for a wide range of components, and provides multiple out-of-the-box dashboards. ails

## 2 Product details

Prometheus Monitoring provides service discovery, data collection, dashboards, and horizontal scaling for agents. It also lets you create custom visual dashboards and alerts for container metrics.

**Service discovery (ServiceMonitor and PodMonitor)**

You can use the ServiceMonitor Custom Resource Definition (CRD) for custom service discovery. ServiceMonitor lets you define the namespace scope for pod discovery and select services to monitor using MatchLabel. Automatically discovers pods for metric collection by detecting their annotation configurations in the cluster.

**Container cluster metric collection**

The service is compatible with the data collection capabilities of standard Prometheus. It supports data collection for container nodes, GPUs, and Kube State. You can view the metric information collected by targets.

**Grafana dashboard visualization**

By default, dashboards are provided for Kubernetes DaemonSet, Kubernetes State, Kubernetes StatefulSet, Kubernetes container replicas, Kubernetes overview, Kubernetes deployments, Node Summary, Node TopN, Physical Resources, Pod TopN, and Prometheus host details. Prometheus Monitoring displays monitoring data on Grafana dashboards.

**Prometheus Agent installation and horizontal scaling (HPA)**

You can install the Prometheus Agent using Helm 2 or Helm 3. Automatic scale-out is also supported for collector agents that require persistence for critical states.

**Visualization center (Custom dashboards)**

You can quickly create visual analytics dashboards and use Prometheus Query Language (PromQL) expressions to define cluster data. You can choose from a variety of chart types, such as line charts, area charts, column charts, bar charts, pie charts, ticker boards, and gauges. You can customize chart styles and resize charts by dragging and dropping. This lets you gain real-time insights into system status and visually analyze operational trends. Dashboards also support features such as filtering, auto-refresh, grouping, import, and export.

**Alert management (Custom alerts and alert templates)**

You can add alert policies for metrics reported by the cluster. You can use various built-in container alert templates or configure data with custom PromQL expressions. Multiple notification channels are supported, such as phone calls, text messages, emails, and DingTalk. If an abnormality occurs, the system promptly notifies the responsible owner. The system also supports alert compression mechanisms, such as alert suppression, silencing, and convergence.

**Unified provisioning**

You can centrally manage connected ACK managed clusters on the **Provisioning** page. This page provides a unified portal to configure service discovery, manage the installation and uninstallation of Prometheus probes, and view Prometheus Agent self-monitoring dashboards. e

## 3 Product value

Alibaba Cloud Prometheus Service is more stable, saves time, and uses fewer resources than open source Prometheus.

**Deploy up to 50 times faster**

Alibaba Cloud Prometheus Service requires no deployment. It features built-in integration with Grafana and Alertmanager and provides pre-built dashboards. An integrated agent automates deployment and collection configurations. You can set up monitoring for your Kubernetes clusters in 10 minutes.

**More stable architecture with horizontal scaling and high**

**availability**

Alibaba Cloud Prometheus Service supports horizontal scaling for data processing and uses a high availability (HA) architecture for data storage. The agent uses an automatic retransmission mechanism and a message queue to handle high traffic.

**Less intrusive and uses 50% fewer resources**

Alibaba Cloud Prometheus Service uses an integrated agent that runs as a single process. This design limits the agent's resource consumption and optimizes memory and CPU usage.

## 4 Features

**Integration Center**

| Feature | Description |
|---|---|
| Container service registration | Connect container service clusters to the Prometheus monitoring platform for integrated monitoring of clusters and workloads. |
| Custom registration | Integrate custom service discovery for custom data collection. View metrics, dashboards, and alert information. |
| Cloud service registration | Integrate with Hybrid Cloud Monitoring and cloud product self- monitoring to view monitoring data from your cloud products. |
| Component monitoring registration | Install and configure components with a single click and use out-of- the-box monitoring dashboards. |

**Instance management**

| Feature | Description |
|---|---|
| Integration Center | Use the Integration Center as the entry point for Prometheus instances. Install developer component objects with a single click. Flexibly view metrics, service discovery configurations, and Grafana dashboards. |
| Dashboard list | View all dashboards and core metrics for a Prometheus instance. |
| Service discovery | Use multiple service discovery mechanisms to optimize the monitoring scope for Kubernetes clusters and ECS. This ensures that the required metric data is collected. |
| Settings | View basic probe information and health check results. Set the number of agent replicas and restart probes. |

**Global configuration**

| Feature | Description |
|---|---|
| Aggregation instances | Use region-level GlobalView aggregation instances for unified metric queries and alerting. |

**Alert management**

| Feature | Description |
|---|---|
| Prometheus alert rules | Create alert rules for specific Prometheus instances. Alert events are generated when conditions are met. Multiple notification methods are supported. |
| Prometheus alert rule templates | Create the same alert rules for multiple Prometheus instances across different regions. This improves the efficiency of rule management. |

**Data shipping**

| Feature | Description |
|---|---|
| Create data shipping tasks | Remotely write data from one Prometheus instance to another. Stream data to other cloud products, such as Kafka and MaxCompute. |

## 5 Scenarios

Managed Service for Prometheus provides unified monitoring for Alibaba Cloud services such as ECS and Kafka, container services (ACK), and application performance (ARMS). It also supports multicloud and on-premises components and custom metrics to provide full-stack observability for operations and maintenance (O&M).

**Unified metric monitoring for Alibaba Cloud services**

Managed Service for Prometheus integrates with Cloud Monitor (CMS) to support a unified display, query, and alert experience for monitoring data from various Alibaba Cloud services. This provides operations and maintenance (O&M) teams with a convenient interface for daily monitoring.

**Container layer metric monitoring**

The service is deeply integrated with ACK. You can enable monitoring during cluster configuration. The service provides components to monitor container performance for workloads, ingresses, and CoreDNS. Dedicated dashboards display metrics for container services, application components, Alibaba Cloud services, and the application itself. The service also syncs cloud resource tags to display monitoring data organized by business dimension.
**Monitored object:** ACK.

**Application performance metric monitoring**

The service integrates with ARMS to provide one-click access to application performance metrics and prebuilt dashboards. It also supports service discovery to collect application performance data.
**Monitored object:** ARMS.

**Multicloud application component metric monitoring**

The service provides exporter integration solutions for third-party clouds and on-premises IDCs to monitor component metrics in these environments. For more information, see

**Managed Service for Prometheus User Guide > Create Service Discovery by Using a**

**ServiceMonitor**.

**Business custom metric monitoring**

You can define custom metrics that align with your business needs, such as metrics for business objectives, service quality, technical components, and infrastructure resources. You can then configure scrape tasks for these metrics and display them together to improve data correlation.
**Monitored objects:** Simple Log Service (SLS) and Elasticsearch.

## 6 Limitations

This topic describes the limitations of Prometheus monitoring.

**Limitations**

By default, metric data is retained for 7 days. Prometheus monitoring does not support multi-region deployment or disaster recovery. Horizontal scaling is limited to two physical machines. Prometheus monitoring data is retained for 7 days by default. To extend this period, contact your Technical Account Manager (TAM). A metric can have up to 20 labels, and a label can have up to 20 values. A standard two-machine deployment supports monitoring for up to 30 container clusters. Historical data is not automatically recovered after a physical machine failure. s

## 7 Key concepts

This topic describes key concepts of Alibaba Cloud Container Service for Kubernetes (ACK).
**Kubernetes**: An open-source, portable, and extensible platform for managing
containerized workloads and services. It simplifies both declarative configuration and automation.
**Alibaba Cloud Container Service for Kubernetes:** Alibaba Cloud Container Service for
Kubernetes (ACK) is a Kubernetes-certified service platform. It offers high-performance management and lifecycle management for enterprise-grade containerized applications.
**node**: A server, such as a virtual machine instance or a physical server, with Docker Engine
installed for deploying and managing containers. The ACK agent is installed on each node to register it with a cluster. You can scale the number of nodes in a cluster as needed.
