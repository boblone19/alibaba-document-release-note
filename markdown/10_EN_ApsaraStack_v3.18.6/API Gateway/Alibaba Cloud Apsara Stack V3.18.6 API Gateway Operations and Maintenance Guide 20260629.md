---
title: "API Gateway Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 11
source_pdf: "b0c891296a2a6191_Alibaba Cloud Apsara Stack V3.18.6 API Gateway Operations and Maintenance Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/API%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20API%20Gateway%20Operations%20and%20Maintenance%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# API Gateway Operations and Maintenance Guide

## Table of Contents

  - 1.1 O&M overview
  - 1.2 O&M architecture
- 2 O&M process
- 3 FAQ

## 1 O&M

### 1.1 O&M overview

This topic describes the purpose, requirements, and precautions for API Gateway O&M, and explains how to get technical support.

**Purpose**

This guide helps maintenance personnel perform preventive maintenance on API Gateway to ensure its long-term stability. Maintenance personnel can use this guide to troubleshoot system issues discovered during maintenance. If an issue cannot be resolved using this guide, contact Alibaba Cloud technical support.

**Requirements**

Maintenance personnel must have professional IT skills, including knowledge of computer networks, experience with distributed storage, and problem analysis and troubleshooting skills. Maintenance personnel must complete the Alibaba Cloud pre-job training for system roles. This training covers essential knowledge of Alibaba Cloud API Gateway, including but not limited to its system principles, networking, feature usage, and O&M tools.

**Important**

During O&M, maintenance personnel must follow all operational procedures to ensure their safety and system security. Keep all user data strictly confidential. Do not copy or distribute user data without written permission from the user.

**Precautions**

To ensure system stability and prevent accidents, maintenance personnel must follow these precautions: Layered and role-based access control: Apply layered and role-based management to networks, devices, systems, and data. Personnel in each service role should have only the minimum permissions required for their tasks. This prevents system failures caused by unauthorized operations. System security: Understand the potential impact of an operation before performing it to avoid risks to system stability. Keep clear records of all operational issues to simplify subsequent problem analysis and troubleshooting. Personal and data security: Follow all required safety precautions when working with electrical equipment. Use secure devices to access the service network. Do not copy or distribute data without authorization.

**Technical support**

If maintenance personnel require assistance, contact Alibaba Cloud technical support.

### 1.2 O&M architecture

This topic describes the O&M architecture of API Gateway. As shown in the preceding figure, the O&M mainly focuses on the base console, the tenantside control plane, and the data plane.

## 2 O&M process

This topic describes the O&M process for API Gateway.

**Gateway component list**

**cop-console**: The gateway product console.
**higress-controller**: The gateway controller that monitors Kubernetes resources for
updates and pushes them to the gateway data plane.
**higress-gateway**: The gateway data plane that forwards traffic.
**higress-plugin-server**: Provides plugin dependencies that the gateway data plane pulls
on demand.
**redis-builtin**: A built-in Redis instance used for scenarios such as token-based rate limiting
and MCP session persistence.
**rrsa-info-server**: A dependency required for credential loading when content security is
enabled.

**Inspect gateway management component pods**

Log in to the OPS server and run `kubectl get pod -n csb-cop` to check if the gateway management component pods are in a terminal state.

**Inspect gateway customer cluster component pods**

1. Log in to the master node or bastion host of the customer cluster.
2. Run the following command to check if the AI gateway component pods are in a terminal
state.

```bash
kubectl get pod –n higress-system
```

3. Run the following command to check if the API Gateway component pods are in a terminal
state.

```bash
kubectl get pod -n apigateway-system
```

**Gateway management component logs**

1. Log in to the cop-console container.
2. Run `cd /home/admin/cop-console/logs` to enter the log directory.
3. Run `ls` to view the log files.

**Note**

debug.log: Business log. import.log: Data migration log. remoting.log: Network connection log. scheduler_task.log: Scheduled task log.

**Gateway data plane logs**

Run the following commands to view the logs:

```bash
kubectl logs <higress-gateway-pod-name> -n higress-system kubectl logs <cop-gateway-pod-name> -n apigateway-system
```

**Gateway route management**

Run the following command:

```bash
kubectl get ingress -n higress-system
```

**Gateway plugin management**

Run the following command:

```bash
kubectl get wasmplugin -n higress-system
```

## 3 FAQ

This topic describes common issues with API Gateway and their solutions.

**Troubleshooting gateway data plane issues**

The `deployment/higress-gateway` data plane component typically handles a large volume of traffic. Therefore, issues with this component can have a wide impact and require quick diagnosis.

**Determine which node generated the response**

Check if the `x-envoy-upstream-service-time` response header is present. If present, Higress-gateway forwarded the request to the upstream service, which then returned an error. In this case, investigate the upstream service to find the cause. If absent, Higress-gateway returned the error directly. This can happen for two reasons: The gateway has a misconfigured forwarding rule or interception rule. The gateway cannot connect to the upstream service. Rationale: This check can help you identify the root cause in about 50% of cases.

**Check for incorrect forwarding rules in Higress-gateway**

Check the Higress-gateway log to identify any plugins that failed to apply their configuration. Rationale: The Higress-gateway log can reveal the root cause in about 40% of cases.

**Gateway cannot reach the model service**

**Symptom**

Direct requests to the model service succeed, but requests made through the gateway fail.

**Solution**

1. Verify that the route, service, and domain name configurations are correct.
2. Examine the Higress-gateway log, which can often reveal the root cause directly.
3. Verify that the ai-proxy configuration is set as expected.
4. Log in to the Higress-gateway container and use `telnet or curl` to test the connection to
the model service. This helps rule out network or security group issues.
5. Check the Higress-gateway log for configuration delivery issues.

**401 Unauthorized errors**

**Symptom**

A 401 status code from the gateway typically indicates an authentication problem. Determine whether authentication failed at the gateway or at the backend service.

**Solution**

1. Inspect the `server` field in the response header. If it contains "envoy", the request was
not forwarded to the backend service, indicating that gateway authentication failed.
2. If gateway authentication is the issue, investigate the following:
i. Verify that a consumer credential was included in the request. ii. Verify that the token includes the "Bearer" prefix if required.
3. Check the Higress-gateway log for configuration delivery issues.

**403 Forbidden errors**

**Symptom**

A 403 status code from the gateway usually indicates an authorization problem. Determine whether authorization failed at the gateway or at the backend service.

**Solution**

1. Determine at which point in the request flow the authorization failed.
2. If the failure is at the gateway, verify that the consumer is authorized for the route.
3. Check the Higress-gateway log for configuration delivery issues.

**404 Not Found errors**

**Symptom**

A 404 error from the gateway typically indicates a route configuration issue. Determine if the gateway could not find a matching route or if the upstream service does not provide the requested API.

**Solution**

1. Determine at which point in the request flow the service endpoint could not be found.
2. If the gateway could not find the route, investigate the following:
i. Does the route configuration exist? ii. Do the route conditions in the configuration match the incoming request? iii. Was the route configuration delivered to the data plane? You can verify this by running the following command: kubectl exec ${higress-gateway-pod-name} -nhigress-system --

```bash
curl -v "127.0.0.1:15000/config_dump" > config_dump.json .
```

3. Check the Higress-gateway log for configuration delivery issues.

**503 Service Unavailable errors**

**Symptom**

A 503 response from the gateway usually indicates a problem with the upstream service for that route.

**Solution**

1. Check if the associated upstream service is accessible.
Test the connectivity directly from the Higress-gateway pod using the `curl` command. This prevents connectivity problems that can result from different DNS settings across environments.
2. Verify that the configuration for the associated upstream service is correct.
3. Verify that the route configuration was delivered to the data plane. Use the following

```
command: kubectl exec ${higress-gateway-pod-name} -nhigress-system -- curl -v "127.0.0.1:15000/config_dump" > config_dump.json .
```

4. Examine the Higress-gateway logs to troubleshoot issues with configuration delivery.

**Rate limiting is not working**

**Symptom**

You have configured the `ai-token-ratelimit` or `cluster-key-rate-limit` plugin, but rate limiting is not working.

**Solution**

1. Review the documentation and verify the plugin configuration. Check for issues such as
incorrect formatting or a missing Redis configuration.
2. Check for Redis connection issues in the Higress-gateway log.
3. Check the Higress-gateway log for configuration parsing errors.
4. Check the rate-limiting values in the response header to confirm they have not reached the
configured threshold.
