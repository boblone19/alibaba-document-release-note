---
title: "Alibaba Cloud Apsara Stack V3.18.3 Container Registry Operations and Maintenance Guide 20241025"
product_version: "V3.18.3"
doc_version: "20241025"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Container Registry Operations and Maintenance Guide 20241025.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F%E6%9C%8D%E5%8A%A1ACR/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Container%20Registry%20Operations%20and%20Maintenance%20Guide%2020241025.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Container Registry Operations and Maintenance Guide 20241025

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
- 2 Manage components
- 3 Component features
- 4 Component O&M

cture Management console

## 1 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Procedure**

1. Open your browser.

## 2 Manage components

This topic describes common operations on components, including viewing monitoring information of components, logging on to component machines, and restarting component machines.

**View monitoring information of components**

## 1 Log on to the Apsara Infrastructure Management console.

2. In the top navigation bar, choose **Operations > Service Operations**.
3. On the Service Operations page, enter acr in the **Fuzzy Search** text box, and then click
**Management** in the **Actions** column corresponding to acr.
4. On the **Details** page, click the **Service Instance** tab and then click an instance name in
the **Service Instance** column.
5. In the **Server Role List** section of the **Service Instance Information Dashboard** page,
click **Details** in the **Actions** column corresponding to the server role that you want to manage.
6. On the **Server Role Dashboard** page, view the server role monitoring information of
machines and server role monitoring information.

**Log on to a component machine**

2. In the top navigation bar, choose **Operations > Service Operations**.
3. On the Service Operations page, enter acr in the **Fuzzy Search** text box, and then click
**Management** in the **Actions** column corresponding to acr.
4. On the **Details** page, click the **Service Instance** tab and then click an instance name in
the **Service Instance** column.
5. In the **Server Role List** section of the **Service Instance Information Dashboard** page,
click **Details** in the **Actions** column corresponding to the server role that you want to manage.
6. In the **Machine Information** section of the **Server Role Dashboard** page, click **Terminal**
in the **Actions** column corresponding to the machine that you want to manage.

**Restart a component machine**

2. In the top navigation bar, choose **Operations > Service Operations**.
3. On the Service Operations page, enter acr in the **Fuzzy Search** text box, and then click
**Management** in the **Actions** column corresponding to acr.
4. On the **Details** page, click the **Service Instance** tab and then click an instance name in
the **Service Instance** column.
5. In the **Server Role List** section of the **Service Instance Information Dashboard** page,
click **Details** in the **Actions** column corresponding to the server role that you want to manage.
6. In the **Machine Information** section of the **Server Role Dashboard** page, click **Restart**
in the **Actions** column corresponding to the machine that you want to manage.
7. In the message that appears, click **OK**.

## 3 Component features

This topic describes the features of container images.

**Deployment-oriented components**

This topic does not describe features of components for deployment. If the CrInit component does not reach the desired state, you must first find out the reason and resolve the issue. If the ServiceTests component does not reach the desired state, you can check whether functional components do not reach the desired state. CrInit: The component initializes the product when you deploy a product. If the component does not reach the desired state, you can troubleshoot issues that occur during the initialization process based on container logs. For example, the system may fail to register APIs with POP. You must resolve the issues before you proceed with the deployment. ServiceTests: The component periodically executes test cases to check whether the product works as expected.

**Functional components**

The following list describes the features of functional components. If the product has functional issues, such as system exceptions and non-business exceptions, you need to first check whether the functional components reach the desired state. CrRegistry: pushes and pulls container images. CrAuthentication: provides identification authentication services. CrOpenapi: provides API operations. CrManager: handles business logic of the product. CrSync: provides the image replication service.

## 4 Component O&M

This topic describes common O&M operations for components.

**Common O&M operations on deployment-oriented components**

You can perform O&M operations on deployment-oriented components without entering containers. If the components do not reach the desired state, you can identify the cause of the exception based on container logs and perform O&M operations. CrInit does not reach the desired state: Log on to the machine where the component is located. Run related commands, such as `docker ps` and `docker logs` , to identify and query container logs of the component. Find out the reason of the issue based on the exception information in the container logs. The issues are usually caused by external dependencies. After you resolve the issue, restart the component in the Apsara Infrastructure Management console. For information about how to log on to a component machine and restart a component machine, see Log on to a component machine and Restart a component machine. ServiceTests does not reach the desired state: View the monitoring information of the component to identify the cause of the exception. If the container does not exit correctly, the test case fails. Check whether functional components work as expected. For other exceptions, check whether the exception is caused by the environment or other issues. For information about how to view the monitoring information of components, see View monitoring information of components.

**Common O&M operations on functional components**

You need to query logs in component containers. If the components do not reach the desired state or experience other exceptions, you can identify the cause of the exception based on container logs and perform O&M operations. Identify the cause of the exception The component does not reach the desired state. View the monitoring information of the component to identify the cause of the exception. If the exception is a failure in container health checks, the Apsara Infrastructure Management console does not correctly issue an HTTPS certificate, or there is a problem with external dependencies. For information about how to view the monitoring information of components, see View monitoring information of components. The component reaches the desired state. Log on to the component machine and view logs (/alidata/www/logs/tengine) in the container. For information about how to log on to a component machine, see Log on to a component machine. If the log in the tengine directory shows a certificate exception, the Apsara Infrastructure Management console does not correctly issue an HTTPS certificate. If the log in the tengine directory shows a failure in health checks, there is a problem with external dependencies. Handle exceptions HTTPS certificate exception: The exception usually occurs on the CrAuthentication and CrRegistry components. You need to check the cluster configurations to verify that the system issued a certificate that contained correct content. If the exception is due to an external dependency, check whether the external dependency reaches the desired state. Then, restart the component to handle the exception. For information about how to restart a component, see Restart a component machine. If other exceptions occur, check whether the exceptions are caused by the environment.
