---
title: "Application Hybrid Marketplace User Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 31
source_pdf: "5c8978d91d62cfe5_Alibaba Cloud Apsara Stack V3.18.6 Application Hybrid Marketplace User Guide 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%B7%B7%E5%90%88%E4%BA%91%E5%BA%94%E7%94%A8%E4%B8%AD%E5%BF%83AHM/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Application%20Hybrid%20Marketplace%20User%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Application Hybrid Marketplace User Guide 20260630

## Table of Contents

- 1 Overview
- 2 Getting started
  - 2.1 Log on to the Hybrid Cloud Application Center console
  - 2.2 Deploy an application in an ACK cluster
  - 2.3 Deploy an application in an ECS instance
  - 2.4 Deploy the ONSP
- 3 App Store
  - 3.1 Import an application
  - 3.2 Deploy an application
- 4 My Applications
- 5 Task management
- 6 Plug-in center
  - 6.1 Plug-in store
  - 6.2 My plug-ins
- 7 System management
  - 7.1 Image repository management
  - 7.2 Variable management
    - 7.2.1 Manage global variables
    - 7.2.2 Manage cluster variables

## 1 Overview

Hybrid Cloud Application Center serves as the third product R&D and delivery pipeline, in addition to Apsara Infrastructure Management and the Platform as a Service (PaaS) platform. It is used to deliver applications in Apsara Stack and provides features such as application import, application deployment, application upgrade, application unpublishing, basic monitoring, and system configuration and management. Hybrid Cloud Application Center supports the deployment of applications in Kubernetes clusters and Elastic Compute Service (ECS) instances in major application delivery scenarios.

## 2 Getting started

### 2.1 Log on to the Hybrid Cloud Application Center console

**Application Center console**

You can log on to the Hybrid Cloud Application Center console from the Apsara Uni-manager Management Console. The homepage of the Hybrid Cloud Application Center console displays the current system resource usage and monitoring status of each region in charts.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Application > Hybrid Cloud Application**
**Center**.
3. On the homepage of the console, you can view the summary information about all
applications in Hybrid Cloud Application Center.
**My Application Status**: displays the status and number of all applications in Hybrid
Cloud Application Center.
**Alert Overview**: displays the number of alerts at each level and the alert details of all
applications in Hybrid Cloud Application Center.
**Top 10 Resources**: displays the CPU, disk, and memory usage of the 10 applications
with the highest resource consumption in Hybrid Cloud Application Center.
**Cloud Resource Distribution**: displays the distribution of cloud resources in different
regions.

### 2.2 Deploy an application in an ACK cluster

**ACK cluster**

This topic describes how to use the Hybrid Cloud Application Center console to deploy an application in an Apsara Stack Container Service for Kubernetes (ACK) cluster to the application store.

**Before you start**

Before you deploy an application, make the following preparations: Account: Create a user account that has the permissions to use the resources of the specified organization and resource set to which you want to deploy the application. Network resources: Create a virtual private cloud (VPC) and vSwitches in the specified organization and resource set. ACK cluster: Create an ACK cluster in the specified organization and resource set. The specifications of the worker nodes in the cluster must be at least the component container specifications required for application access in the base environment. For example, if the component container specifications are 4 CPU cores and 8 GB of memory, the specifications of a worker node in the ACK cluster must be at least 4 CPU cores and 8 GB of memory. Cluster data authorization: Grant data permissions on the ACK cluster to the user account. Wildcard domain name: Bind an available wildcard domain name to each Ingress of the ACK cluster.

**Note**

Log on to the ACK console. In the left-side navigation pane of the details page of your cluster, choose Network > Services. On the Services page, select kubesystem from the Namespace drop-down list and click nginx-ingress-lb in the Name column. On the service details page, the IP addresses in the External Endpoint field are the origin IP addresses to which you need to bind wildcard domain names. If you use DNS to bind domain names, we recommend that you use an A record to bind a wildcard domain name to an Ingress. If you do not bind wildcard domain names, you must configure an A record for each service domain name to point to the IP address of the Ingress. The bound wildcard domain name must be specified in the environment variables of the cluster when you deploy the application. Image repository in Container Registry: Create an image repository in Container Registry and push the required application images to the image repository.
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **System Management** > **Image Repositories**.
On the page that appears, make sure that the Repository URL, Read/Write Account, and Account Password of the image repository are the same as those of the image repository created in Container Registry.
3. In the left-side navigation pane, choose **System Management** > **Variables**. On the page
that appears, you can modify the variable settings based on your business requirements.
4. On the **App Store** page, choose **Import Application** > Import Application to upload a .zip
package of the application baseline or choose **Import Application > One-Click import** to import the full product package.
5. After the import is complete, click the card of the application on the App Store page to go to
the application details page. Click **Deploy Now** in the upper-right corner. Follow on-screen instructions to configure basic information for application deployment and complete application deployment. i. **Basic Settings** In the Basic Settings step, configure the parameters and click **Next**. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Instance Name | Yes | Enter a name for the application. The name must be up to 64 characters in length and can contain letters, hyphens (-), and underscores ( ). The name must start with a letter. _ |
| Service instance description | Yes | Enter the application description. |
| Application System Version | Yes | Select the version number of the application that you want to deploy. |
| Product status | Yes | The system automatically checks the product status. |
| Application System Specification | Yes | Select the specifications for deploying the application. The selected specifications cannot exceed the specifications of a worker node in the ACK cluster. |
| Instance | Yes | Select the cloud platform where you want to deploy the application. |
| Organization | Yes | Select the organization of the ACK cluster where you want to deploy the application. |

| Resource Set | Yes | Select the resource set of the ACK cluster where you want to deploy the application. |
|---|---|---|
| Region | Yes | Select the region of the ACK cluster where you want to deploy the application. |
| Zone | Yes | Select the zone of the ACK cluster where you want to deploy the application. |

ii. **Resource Configuration** In the Resource Configuration step, configure the parameters and click **Next**. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| VPC | Yes | Select the VPC of the ACK cluster where you want to deploy the application. |
| Container Cluster | Yes | Select the ACK cluster where you want to deploy the application. |

iii. **Application Settings** In the Application Settings step, configure the parameters and click **Next**. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Application Administrator | Yes | The default value is admin. |
| Application Administrator Logon Password | Yes | Enter the logon password for the application administrator. |
| Application Configurations | Yes | The custom configurations of the application. |

iv. **Confirmation** Confirm parameter settings in this step. v. **Complete** Click **Start Now** to deploy the application.

### 2.3 Deploy an application in an ECS instance

**ECS instance**

This topic describes how to use the Hybrid Cloud Application Center console to deploy an application in an Elastic Compute Service (ECS) instance in Apsara Stack to the application store.

**Before you start**

Before you deploy an application, make the following preparations: Account: Create a user account that has the permissions to use the resources of the specified organization and resource set to which you want to deploy the application. Resource Access Management (RAM) authorization: The created account must have the required permissions on the ECS instance. You can use RAM-based authorization to grant the account only the permissions required for application deployment.

**Note**

**RAM authorization configuration**

i. Create a RAM role and grant the required permissions to the role in the Apsara Unimanager Management Console. ii. Add a permission policy to the created RAM role. The following code shows the permission policy: `{`

```json
    "Version": "1",
    "Statement":
```

`[` `{`

```json
            "Action":
```

`[`

```
                "rds:Describe*",
                "rds:CreateDBInstance",
                "rds:CreateAccount*",
                "rds:CreateDataBase*",
                "rds:ModifySecurityIps",
                "rds:GrantAccountPrivilege",
                "rds:ReceiveDBInstance",
                "rds:CreateMigrateTask",
                "rds:DescribeMigrateTaskById",
                "rds:CreateOnlineDatabaseTask"
```

`],`

```json
            "Resource": "*",
            "Effect": "Allow"
```

`},` `{`

```json
            "Action":
```

`[`

```
                "ecs:DescribeSecurityGroupAttribute",
                "ecs:DescribeInstances",
                "ecs:DescribeRegions",
                "ecs:AuthorizeSecurityGroup",
                "ecs:CreateSecurityGroup",
                "ecs:DeleteSecurityGroup",
                "ecs:DescribeSecurityGroups",
                "ecs:JoinSecurityGroup",
                "ecs:LeaveSecurityGroup",
                "ecs:RevokeSecurityGroup",
                "ecs:RunCommand",
                "ecs:SendFile",
                "ecs:DescribeSendFileResults",
                "ecs:ImportImage",
                "ecs:DescribeTasks",
                "ecs:DescribeCommands",
                "ecs:DescribeInvocationResults",
                "ecs:AllocateEipAddress",
                "vpc:AllocateEipAddress",
                "eip:AllocateEipAddress",
                "slb:CreateLoadBalancer",
                "slb:AddBackendServers",
                "slb:CreateLoadBalancerHTTPListener",
                "slb:StartLoadBalancerListener"
```

`],`

```json
            "Resource": "*",
            "Effect": "Allow"
```

`}` `]` `}` iii. Associate the prepared user account with the RAM role by using a user group. Network resources: Create a virtual private cloud (VPC) and vSwitches in the specified organization and resource set.
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **System Management** > **Variables**. On the page
that appears, you can modify the variable settings based on your business requirements.
3. On the **App Store** page, choose **Import Application** > Import Application to upload a .zip
package of the application baseline or choose **Import Application > One-Click import** to import the full product package.
4. After the import is complete, click the card of the application on the App Store page to open
the application details page. Click **Deploy Now** in the upper-right corner. Follow on-screen instructions to configure the basic information about application deployment and complete application deployment. i. **Basic Settings** In the Basic Settings step, configure the parameters and click **Next**. The following tables describe the parameters.

| Parameter | Required | Description |
|---|---|---|
| Instance Name | Yes | Enter a name for the application. The name must be up to 64 characters in length and can contain letters, hyphens (-), and underscores ( ). The name must start _ with a letter. |
| Service instance description | Yes | Enter the application description. |

| Application System Version | Yes | Select the version number of the application that you want to deploy. |
|---|---|---|
| Product status | Yes | The system automatically checks the product status. |
| Application System Specification | Yes | Select the specifications for deploying the application. The selected specifications cannot exceed the specifications of a worker node in the ACK cluster. |
| Instance | Yes | Select the cloud platform where you want to deploy the application. |
| Organization | Yes | Select the organization of the ECS instance where you want to deploy the application. |
| Resource Set | Yes | Select the resource set of the ECS instance where you want to deploy the application. |
| Region | Yes | Select the region of the ECS instance where you want to deploy the application. |
| Zone | Yes | Select the zone of the ECS instance where you want to deploy the application. |

ii. **Resource Configuration** In the Resource Configuration step, configure the parameters and click **Next**. The following tables describe the parameters.

| Parameter | Required | Description |
|---|---|---|
| VPC | Yes | Select the VPC used by the ECS instance where you want to deploy the application. |
| VSwitch | Yes | Select the vSwitch used by the ECS instance where you want to deploy the application. |
| Architecture | Yes | Select the chip architecture of the ECS instance. |
| Instance Type | Yes | Select an ECS instance type. |
| Image | Yes | Select the ECS image required by the application. |
| Creation Method | Yes | By default, Standard Creation is selected. |
| System Disk | Yes | Select a disk category and specify a disk capacity. |
| Data Disk | No | You can add data disks based on your business requirements, set the disk category, and specify the disk size. |
| Instance Quantity | Yes | Specify the number of ECS instances. |
| Security Group | Yes | Select the security group used by the ECS instance where you want to deploy the application. |
| ECS Logon Username | Yes | The default value is root. |
| ECS Logon Password | Yes | Specify the password of the root user to log on to the ECS instance. |

iii. **Application Settings** In the Application Settings step, configure the parameters and click **Next**. The following tables describe the parameters.

| Parameter | Require d | Description |
|---|---|---|
| Application Administrator | Yes | The default value is admin. |
| Application Administrator Logon Password | Yes | Enter the logon password for the application administrator. |
| Application Configurations | Yes | The custom configurations of the application. |

iv. **Confirmation** Confirm parameter settings in this step. v. Click **Start Now** to deploy the application.

### 2.4 Deploy the ONSP

This topic describes how to use the Hybrid Cloud Application Center console to deploy Open Network Service Platform (ONSP).
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **Plug-in Center** > **Plug-in Store**. On the page
that appears, click **Import Plug-in**. In the Import Plug-in dialog box, click Upload JAR File for Remote Plugins to select the plug-in package of ONSP, and then click **OK** to import the ONSP plug-in package.
3. Click the ONSP plug-in on the All Plug-ins page to open the details page. Click **Deploy**
**Application**. In the Deploy panel, select the version number of the ONSP plug-in and click
**Next**. Wait until the plug-in is deployed.
4. On the **My Plugins** page, click the ONSP plug-in to open the details page. In the **Access**
**Portal** section, click **onsp** next to **Domain Name** to go to the ONSP console.

## 3 App Store

### 3.1 Import an application

You can import various cloud applications that are supported by Hybrid Cloud Application Center and deploy the applications by using the Hybrid Cloud Application Center console to meet your business requirements. The Hybrid Cloud Application Center console allows you to import OAM-compliant cloud applications published by Alibaba Cloud or third-party Independent Software Vendors (ISVs) in the form of cloud service packages. These packages are ZIP files formatted in accordance with OAM specifications.

**Import an application**

1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, click App Store. On the **App Store** page, choose **Import**
**Application > Import Application**.
3. In the **Import Application** dialog box, click **Upload File**. Select a .zip file of the cloud
application baseline and click **OK**. After the application is imported, you can view the application on the App Store page and choose to try it out or deploy the application.

**One-click import**

1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, click App Store. On the **App Store** page, choose **Import**
**Application > One-Click import**.
3. Follow the instructions in the **One-Click import** dialog box to perform one-click import
operations. i. Upload the product file to the operations machine. ii. Enter the absolute path of the product file on the operations machine and click **Generate**
**command**. The generated command is valid for 2 hours.
iii. Click **Copy command** and go to the operations machine to run the copied command. The success message indicates that the command is successfully executed.

### 3.2 Deploy an application

This topic describes how to deploy an application. The WordPress application is used in the example. Before application deployment, you need to prepare the relevant network resources, account, and Container Service for Kubernetes (ACK) cluster in Apsara Stack.
1. Log on to the Hybrid Cloud Application Center console.
2. On the **App Store** page, find the application that you want to deploy, such as WordPress,
and go to the application details page.
3. On the application details page, click **Deploy Now** in the upper-right corner.
4. In the dialog box that appears, click **I understand and confirm the same** . On the page
that appears, follow on-screen instructions to configure the basic information for application deployment and complete application deployment. Two application deployment modes are supported: Deploy applications in Kubernetes clusters. For more information, see Deploy an application in an ACK cluster. Deploy applications in Elastic Compute Service (ECS) instances. For more information, see Deploy an application in an ECS instance.

## 4 My Applications

After an application is deployed, you can view all purchased and trial applications in the Hybrid Cloud Application Center console. You can also unpublish applications that have been deployed.

**Note**

You must have the necessary permissions to manage applications. Applications that you are not authorized to manage are not displayed on the My Applications page.
1. Log on to the Hybrid Cloud Application Center console.
2. On the **My Applications** page, click the card of the application that you want to view. In
the panel that appears, click an instance in the Instances Deployed in Application System section to go to the application details page.
3. On the application details page, view the information about the application on the **Basic**
**Information** and **Deployment Logs** tabs.
4. Unpublish an application.
i. On the application details page, click **Delete** in the upper-right corner. ii. In the message that appears, click **Deprecate Application** to unpublish the application and release resources.

**Important**

After an application is unpublished, the resources that you use in the production environment will be released, and the generated application data will be deleted. Perform the operation after confirmation.
5. View application system configurations.
i. On the application details page, click **Configure** in the upper-right corner. ii. You can view the **Input Configurations**, **Output Configurations**, and **System**
**Configurations** of the application.

## 5 Task management

On the Task Management page of Hybrid Cloud Application Center, you can view application deployment tasks. If a task fails to be executed, you can manually retry or skip the steps.
1. Log on to the Hybrid Cloud Application Center console.
2. On the **Task Management** page, you can view the following information about an
application deployment task: **Ticket ID**, **Application Name**, **Version**, **Change Type**,
**Submitted By**, **Start Time**, **End Time**, and **Ticket Status**.
You can filter tasks by **Application Name**, **Submitted By**, or **Ticket Status**.
3. Click the ticket ID of a task to open the task details page. You can view the ticket
information and **Progress** of the task. You can retry or skip a failed task: Click **retry**. In the message that appears, click **OK** to restart the step. Click **skip**. In the message that appears, click **OK** to skip the step.

## 6 Plug-in center

### 6.1 Plug-in store

**Import a plug-in**

1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **Plug-in Center > Plug-in Store**.
3. On the All Plug-ins page, click **Import Plug-in**. In the dialog box that appears, upload the
ZIP package of an Open Application Model (OAM) application plug-in or the JAR package of a remote application plug-in and click **OK**.
4. View the imported plug-in.

**View a plug-in**

1. On the All Plug-ins page, enter a plug-in name in the search box to search for an imported
plug-in.
2. Find the plug-in that you want to view, move the pointer over the
icon, and then click
**Details**. Alternatively, click the card of the plug-in that you want to view to go to the details
page of the plug-in.

**Deploy a plug-in**

1. Go to the plug-in deployment panel by using one of the following methods:
On the All Plug-ins page, find the plug-in that you want to deploy, move the pointer over the icon, and then click **Deploy**. On the details page of the plug-in that you want to deploy, click **Deploy Application**.
2. In the Deploy panel, select the version number of the plug-in and click **Next**. Wait until the
plug-in is deployed.

**Delete a plug-in**

1. On the All Plug-ins page, find the plug-in that you want to delete, move the pointer over the
icon, and then click **Delete Plug-in**.
2. In the message that appears, click **OK**.

### 6.2 My plug-ins

**Restart Plug-in Center**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. On the My Plugins page, click **Restart Plugin Center**.
3. In the message that appears, click **OK**.

**View the details of a plug-in**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. Go to the details page of a plug-in by using one of the following methods:
On the My Plugins page, find the plug-in that you want to view, move the pointer over the icon, and then click **Details**. On the My Plugins page, find the plug-in that you want to view and click the card of the plug-in.
3. View the details of the plug-in.

**Stop a plug-in**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. On the My Plugins page, find the plug-in that you want to stop, move the pointer over the
icon, and then click **Stop**.
3. In the message that appears, click **OK**.

**Restart a plug-in**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. On the My Plugins page, find the plug-in that you want to restart, move the pointer over the
icon, and then click **Restart Plugin**.
3. In the message that appears, click **OK**.

**Uninstall a plug-in**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. Uninstall a plug-in by using one of the following methods:
On the My Plugins page, find the plug-in that you want to uninstall, move the pointer over the icon, and then click **Uninstall**. On the details page of a plug-in, click **Uninstall**.
3. In the message that appears, click **Uninstall**.

**Update a plug-in**

1. In the left-side navigation pane, choose **Plug-in Center > My Plugins**.
2. Go to the details page of a plug-in and click **Update**.
3. Select the version number of the plug-in and click **Next**. Wait until the plug-in is updated.

## 7 System management

### 7.1 Image repository management

An image repository is a Docker image repository. It provides images for specified clusters. You can configure an image repository for a specified cluster. When you deploy an application in the specified cluster, the system reads the configurations of the corresponding image repository to obtain the Docker image of the application. You can also configure a default image repository. If no image repository is configured for a cluster, the system obtains images from the default image repository.
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **System Management** > **Image Repositories**.
On the page that appears, click **Add Image Repository**, configure the related parameters, and then click **OK**.

| Name | Description |
|---|---|
| Source | Select the host platform for the cluster in which an application is deployed. In Apsara Stack, select Alibaba Private Cloud. |
| Repository URL | Enter the domain name of the Docker image repository to be bound. |

| Namespace | Enter the namespace of the Docker image repository to be bound, which is the logical grouping space supported by the image repository. |
|---|---|
| Read/Write Account | Enter the name of the account that is used to access the Docker image repository. You can leave this parameter unspecified when you bind a public image repository. |
| Account Password | Enter the password of the account that is used to access the Docker image repository. You can leave this parameter unspecified when you bind a public image repository. |
| Default | Yes: indicates that the image repository is the default image repository for the clusters from the specified host platform. If no repository URL is specified for the application and the cluster that hosts the application, this repository URL is used to avoid the issue that the system cannot obtain images. No: indicates that the image repository is dedicated to specific clusters and requires explicit association with the clusters. |
| Associated Cluster | Select a Kubernetes cluster to which the image repository is bound. When you create a non-default image repository, you must select the associated cluster. You can select multiple clusters. |

3. After an image repository is created, view the information about all existing image
repositories in the system on the **Image Repository Management** page. Move the pointer over the number in the **Clusters** column to view the list of the clusters that are managed in the image repository.
4. On the **Image Repository Management** page, perform management operations on the
existing image repositories: To modify an image repository, click **Modify** in the **Actions** column. In the dialog box that appears, modify the values of **Source**, **Repository URL**, **Namespace**, **Read/Write**
**Account**, **Account Password**, **Default**, and **Associated Cluster** based on your
business requirement and then click **OK**. To delete an image repository, click **Delete** in the **Actions** column. In the message that appears, click **OK**.

### 7.2 Variable management

#### 7.2.1 Manage global variables

A global variable is a global configuration in the key-value form. The effective scope of global variables is system-wide. Global variables maintain consistent values across all applications and clusters.
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **System Management** > **Variables**. On the page
that appears, click the **Global Variables** tab, click **Add Variable**, configure the variable information, and then click **OK**.

| Name | Description |
|---|---|
| Variable Type | Select Global Variables. |
| Variable Name | Enter a name for the variable. The variable name must be unique. |
| Global Variable Value | Enter the value for the variable. |
| Variable Description | Enter the remarks or description of the variable for easy understanding. |

3. On the **Global Variables** tab of the **Variable Management** page, view the information
about all global variables and modify or delete existing global variables. To modify a variable, find the variable that you want to modify and click **Modify** in the
**Actions** column. In the dialog box that appears, modify the values of the **Variable**
**Name**, **Global Variable Value**, and **Variable Description** parameters and then click
**OK**.
To delete a variable, find the variable that you want to delete and click **Delete** in the
**Actions** column. In the message that appears, click **OK**.

#### 7.2.2 Manage cluster variables

Cluster variables are configuration variables of a cluster in the key-value form. The effective scope of a cluster variable is limited to the associated cluster. Therefore, if different clusters are associated with different cluster variables, the variables with the same name may have different values.
1. Log on to the Hybrid Cloud Application Center console.
2. In the left-side navigation pane, choose **System Management** > **Variables**. On the page
that appears, click the **Cluster Variables** tab and click **Add Variable**. In the dialog box that appears, configure the variable information and click **OK**.

| Name | Description |
|---|---|
| Variable Type | Select Cluster Variables. |
| Variable Name | Enter a name for the variable. The variable name must be unique. |
| Cluster | Select the cluster with which the variable is associated. The cluster indicates the effective scope of the variable. |
| Cluster Variable Value | Enter the value for the variable. |
| Variable Description | Enter the remarks or description of the variable for easy understanding. |

3. On the **Cluster Variables** tab of the **Variable Management** page, view the information
about all cluster variables and modify or delete existing cluster variables. To modify a variable, find the variable that you want to modify and click **Modify** in the
**Actions** column. In the dialog box that appears, modify the values of the **Variable**
**Name**, **Cluster**, **Cluster Variable Value**, and **Variable Description** parameters and
then click **OK**. To delete a variable, find the variable that you want to delete and click **Delete** in the
**Actions** column. In the message that appears, click **OK**.
