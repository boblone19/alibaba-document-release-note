---
title: "Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 524
source_pdf: "7b13c149aeee2b2f_Alibaba Cloud Apsara Stack V3.18.6 Realtime Compute for Apache Flink (Compute-Storage Separation Edi"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%9E%E6%97%B6%E8%AE%A1%E7%AE%97FLink/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Realtime%20Compute%20for%20Apache%20Flink%20%28Compute-Storage%20Separation%20Edition%29%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Realtime Compute for Apache Flink (Compute-Storage Separation Edition) User Guide 20260701

## Table of Contents

- 1 What is Realtime Compute
- 2 Preparations
  - 2.1 Log in to the Realtime Compute for Apache Flink console
  - 2.2 Configure project access permissions
  - 2.3 Go to the Overview page
  - 2.4 Create a workspace
  - 2.5 Create a namespace
- 3 Getting started
  - 3.1 Get started with an SQL deployment
  - 3.2 Get started with a JAR deployment
  - 3.3 Getting started with a Python deployment
- 4 Draft development
  - 4.1 Sample center
    - 4.1.1 Data synchronization templates
    - 4.1.2 Code templates
  - 4.2 Develop an SQL draft
  - 4.3 Develop a JAR draft
  - 4.4 Develop a Python API draft
  - 4.5 Debug a deployment
  - 4.6 Use Python dependencies
- 5 Data connectors
  - 5.1 Supported connectors
  - 5.2 Manage custom connectors
  - 5.3 Datagen connector
  - 5.4 Blackhole connector
  - 5.5 Print connector
  - 5.6 Faker connector
  - 5.7 Apache Iceberg connector
  - 5.8 Postgres CDC connector
  - 5.9 TSDB for InfluxDB connector
  - 5.10 Tablestore connector
  - 5.11 ClickHouse connector
  - 5.12 Elasticsearch connector
  - 5.13 Upsert Kafka connector
  - 5.14 AnalyticDB for PostgreSQL connector
  - 5.15 AnalyticDB for MySQL V3.0 connector
  - 5.16 ApsaraDB for HBase connector
  - 5.17 Lindorm connector
  - 5.18 ApsaraMQ for RocketMQ connector
  - 5.19 ApsaraDB for Redis connector
  - 5.20 Tair (Redis OSS-compatible) connector
  - 5.21 ApsaraDB RDS for MySQL connector
  - 5.22 JDBC connector
  - 5.23 MongoDB connector
  - 5.24 DataHub connector
  - 5.25 StarRocks connector
  - 5.26 SLS connector
  - 5.27 Apache Paimon
  - 5.28 MaxCompute connector
  - 5.29 Kafka connector
  - 5.30 Hologres connector
  - 5.31 MySQL connector
- 6 O&M management
  - 6.1 Deployment management
    - 6.1.1 Default draft settings
    - 6.1.2 Create a deployment
    - 6.1.3 Start a deployment
    - 6.1.4 Cancel a deployment
  - 6.2 Artifact management
  - 6.3 Metadata management
    - 6.3.1 Manage user-defined functions (UDFs)
    - 6.3.2 Manage Apache Paimon catalogs
    - 6.3.3 Manage Hologres catalogs
    - 6.3.4 Manage MySQL catalogs
  - 6.4 Configure a session cluster
  - 6.5 Security management
  - 6.6 Configure an external storage IP address
  - 6.7 Deployment logs
    - 6.7.1 View startup and running logs
    - 6.7.2 View running exception logs
    - 6.7.3 View historical deployment instance logs
    - 6.7.4 Modify the log level for a running deployment
    - 6.7.5 View Flink audit events
- 7 Flink MCP Server

ime Compute

## 1 What is Realtime Compute

Alibaba Cloud Realtime Compute is an all-one, high-performance real-time big data processing platform built on Apache Flink, applicable for multiple scenarios, including streaming data processing and offline data processing.

**Features**

Powerful real-time processing capabilities Alibaba Cloud Realtime Compute integrates comprehensive end-to-end features to simplify your real-time computing development across the entire pipeline. These include: Powerful stream computing engine. Alibaba Cloud Realtime Compute provides Flink SQL and supports automatic recovery in various failure scenarios to ensure data processing accuracy during failures. The system supports multiple built-in functions, including functions for strings, dates, and aggregation. The system offers precise control of computing resources to ensure strong isolation for user jobs. Key performance metrics are three to four times higher than those of open-source Flink. The system optimizes data compute latency to sub-second or even second-level. A single job can achieve throughput at the million (records/second) level. A single cluster can scale to thousands of nodes. Deep integration with various cloud data storage services. Hosted Realtime Compute service Unlike open-source or self-managed streaming services, Alibaba Cloud Realtime Compute is a fully hosted stream computing engine. With it, you can run queries on streaming data without provisioning or managing any infrastructure, and gain instant access to streaming data processing capabilities. The platform natively integrates data storage, data development, data operations, and monitoring and alerting features, allowing you to trial and migrate to stream computing at low cost. Additionally, Realtime Compute provides fully tenant-isolated, managed runtime services. From the top-level workspace down to the underlying execution machines, the system delivers highly effective isolation and comprehensive protection so you can use Realtime Compute with confidence. Low labor and cluster costs The highly optimized SQL execution engine delivers more efficient and cost-effective computing jobs than native Flink jobs. Whether in development cost or runtime cost, Alibaba Cloud Realtime Compute is significantly lower than open-source streaming frameworks.

## 2 Preparations

### 2.1 Log in to the Realtime Compute for Apache Flink console

**Compute for Apache Flink console**

This topic describes how to log in to the Realtime Compute for Apache Flink (Computestorage Decoupled Edition) console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

> **Note:** **First login**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forgotten password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

5. In the top navigation bar, move the pointer over **Products** and choose **Big Data**
**Computing > Realtime Compute for Apache Flink**.
6. In the left-side navigation pane, choose **Flink (Compute-storage Decoupled Edition) >**
**Workspace Management**.
You can click the icon in the lower-right floating menu to show or hide the floating menu. : the price calculator. Click the icon to go to the **Price Calculator** page. : the shopping cart. Click the icon to go to the **Configure, Price, Quote (CPQ)** page. : the documentation of the service. Click the icon to view the service documentation.

### 2.2 Configure project access permissions

**permissions**

This topic describes how to create a target user and configure project access permissions.

**Background information**

As the product evolves and on-site metering requirements grow, management of Flink project (Namespace) resources has migrated from to Apsara Uni-manager Management Console to better align with user behavior when creating resources in Apsara Uni-manager Management Console. Flink permissions consist of the following two parts, targeting the Realtime Compute for Apache Flink management console and the Realtime Compute for Apache Flink development console respectively:

| Permission category | Description |
|---|---|
| Resource management | Permissions for managing project resources, including creating, modifying, deleting, and querying workspaces. Users with these permissions can manage project resources in the Realtime Compute for Apache Flink management console. |
| Business role | Permissions for deplolyments within a specific project, including owner, editor, and view (read-only). These permissions primarily affect actual business operations. Users authorized with business roles can log in to the Realtime Compute for Apache Flink development console via Realtime Compute for Apache Flink management console to perform draft development and O&M management. |

> **Note:** This topic describes resource management role authorization. To configure business role permissions and grant access to the Realtime Compute for Apache Flink development console, see Security management.

**Procedure**

1. Create the target organization.
For detailed steps, see **Apsara Uni-manager Management Console User Guide >**

**Enterprise > Resource management > Organization management > Create an**

**organization**.
2. Create the target resource set (when you create an organization, the system automatically
creates a default resource set for that organization. You can create additional sets as needed). For detailed steps, see **Apsara Uni-manager Management Console User Guide >**

**Enterprise > Resource management > Resource set management > Create a**

**resource set**.
3. Create the target user.
For detailed steps, see **Apsara Uni-Manager Management Console User Guide >**
**Enterprise center > User management > Users > Create a user**, and assign
corresponding roles based on role permission scope.

> **Note:** We recommend selecting the preset Resource Set Administrator or Organization Administrator role. These preset roles grant permissions to create, modify, delete, and view workspaces and projects.
> If you select the preset Resource User role, the user can view and modify workspaces and projects.
> To view role permissions or create custom roles, see **Apsara Uni-manager** **Management Console User Guide > Enterprise > Access control > Role** **authorization**.

4. Add the target user to the target resource set.
For detailed steps, see **Apsara Uni-manager Management Console User Guide >**

**Enterprise > Resource management > Resource set management > Manage**

**resource set members**, and add the target user to the corresponding resource set.
5. Assign additional roles to the target user (optional).
For detailed steps, see **Apsara Uni-manager Management Console User Guide >**
**Enterprise > User Management > Users > User role authorization**, to modify or add
the target user's management permissions for project resources.

**Next operations**

Switch the owner role to Go to the security center, assign business roles to the target user, and access the Realtime Compute for Apache Flink development console via Realtime Compute for Apache Flink management console.

### 2.3 Go to the Overview page

The Overview page of Realtime Compute for Apache Flink (Compute-storage Decoupled Edition) displays the number of namespaces in the current workspace.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces** page, find the workspace and namespace that you want to manage
and click **Console** in the **Actions** column.
3. In the left-side navigation pane, choose **Flink (Compute-storage Decoupled Edition) >**
**Overview**.
4. View the number of namespaces in the workspace.

### 2.4 Create a workspace

This topic describes how to create a workspace in the Realtime Compute for Apache Flink console.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, choose **Flink (Compute-storage Decoupled Edition) >**
**Workspace Management**.
3. On the **Workspaces** page, click **Create Workspace**.
4. On the **Create Workspace**page**,**configure the parameters.

| Parameter |   | Description |
|---|---|---|
| Section | Organization | Select the organization to which the user belongs. |
|   | Resource Set | Select a resource set. |
|   | Region | Select a region. |
| Basic Informati on | Name | Enter a name for the workspace. The name must meet the following naming conventions: The name can contain lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a lowercase letter or a digit. The name must be unique within the selected region. |
|   | Architecture | Select an architecture based on the on-screen instructions. |
|   | User Name | By default, the username of the current account is displayed. |

5. Click **Submit**.
After you submit the configuration, you can find the created workspace on the
**Workspaces**page.When the status of the workspace changes from **Configuring** to
**Available**, the workspace is created. To delete a workspace, click**Delete** in the Actions
column.

### 2.5 Create a namespace

This topic describes how to create a namespace in the Realtime Compute for Apache Flink console.

**Background information**

To meet the increasing demand for Realtime Compute for Apache Flink iteration and on-site metering, the namespace management feature of Realtime Compute for Apache Flink is migrated from Apsara Big Data Manager (ABM) to the Apsara Uni-manager Management Console. The Apsara Uni-manager Management Console is more suitable for creating resources. Realtime Compute for Apache Flink permissions are divided into the following categories.

| Permission category | Description |
|---|---|
| Resource management permissions | Allow you to manage namespaces, such as creating, modifying, deleting, and querying namespaces. This category of permissions is commonly used in the Realtime Compute for Apache Flink console where you can manage resources. To manage namespaces of Realtime Compute for Apache Flink, you must obtain this category of permissions. |

| Business permissions | This category of permissions is commonly used to manage deployments in namespaces, and is classified into owner permissions, editor permissions, and view permissions. To manage businesses, you must obtain this category of permissions. The owner role can be used to grant business access permissions, such as editor or view permissions, to Resource Access Management (RAM) users in the same organization. Note that permissions cannot be granted to users across level 1 organizations. Even if the users are granted the permissions, the deployment list is not available to the users. |
|---|---|

**Prerequisites**

1. An organization is created.
For more information, see **Apsara Uni-manager Management Console User Guide >**

**Enterprise Center > Resource management > Organization management >**

**Create an organization**.
2. A resource set is created. If you create an organization, the system creates a resource set
for the organization by default. You can also create a resource set based on your business requirements. For more information, see **Apsara Uni-manager Management Console User Guide >**

**Enterprise Center > Resource management > Resource set management >**

**Create a resource set**.
3. A user is created.
For more information, see **Apsara Uni-manager Management Console User Guide >**
**Enterprise Center > Member management > User management > Create a user**.

> **Important:** Make sure that the user has permissions to create and view namespaces in Realtime Compute for Apache Flink.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
2. Create a namespace.
i. In the left-side navigation pane, choose **Flink (Compute-storage Decoupled Edition)**
**> Workspace Management**.
ii. Find the workspace in which you want to create a namespace and click **Create**
**Namespace** in the **Actions** column.
iii. On the **Create Namespace** page, configure the parameters in the **Section** and **Basic**
**Information** sections.

**Section**

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the user belongs. |
| Resource Set | Select a resource set. |
| Region | Select a region. |

**Basic Information**

| Parameter | Description |
|---|---|
| Workspace | The current workspace is automatically selected and cannot be changed. |
| Namespace name | Enter a name for the namespace. The name must meet the following naming conventions: The name can contain lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a lowercase letter or a digit. The name must be unique within the selected region. The name can be up to 40 characters in length. |
| CPU Architecture | Select a chip architecture. |
| Deployment Mode | Select a deployment mode. Supported deployment modes: Single-zone instance Example of Disaster Recovery in the Same City |
| Availability Zone | Select a zone. |
| CU Resources | Specify the number of CUs based on your business requirements .The number of CUs cannot exceed the remaining number of CUs of the workspace. |
| User Name | The name of the user who has permissions on the current organization. |

3. Click **Confirm Order**.
4. After the namespace is created, refresh the **namespace list** to view the namespace
information.

**What to do next**

Go to the Realtime Compute console Find the namespace that you want to manage and click **Console** in the **Actions** column. Modify the number of CUs Find the namespace that you want to manage and click **Change CU Count** in the **Actions** column.

**Important**

If you reduce the number of CUs, the Realtime Compute for Apache Flink instance may fail to recover after a restart. Check the CUs that are consumed in the namespace before you modify the number of CUs. Proceed with caution. Find the namespace that you want to manage and click **Configure IP Address for**
**External Data Store** in the **Actions** column. For more information, see Configure an
external storage IP address. Delete a namespace Find the namespace that you want to delete and click **Delete** in the **Actions** column. View the information about a namespace In the search box below the **namespace list**, enter a keyword to search for namespaces.

**FAQ**

Problem: Why is the namespace not displayed after I am granted permissions on the namespace? Possible causes: This issue may arise in two situations: Your account is not added to the resource set to which the namespace belongs. Your account and the UID specified when you created the namespace are not in the same organization. Problem: Why are some action buttons not displayed or displayed but dimmed after I log in to the Realtime Compute for Apache Flink with my account and go to the namespace management page? Possible causes: The current role of your account is not granted permissions on these actions. Check whether your role has permissions on the Realtime Compute console. Problem: Why is the following error reported after I perform a creation, modification, or deletion operation with my account? Possible causes: The current role of the account is not authorized to perform this operation, as shown in the following figure. Check whether your role has permissions on the Realtime Compute console. ed

## 3 Getting started

### 3.1 Get started with an SQL deployment

**deployment**

Realtime Compute for Apache Flink allows you to edit and run deployments by using JAR code. This topic describes how to create and run an SQL deployment.

**Procedure**

1. Step 1: Create an SQL draft and write business code
On the Draft Editor page, create an SQL streaming draft and write DDL and DML code of the draft.
2. Step 2: Start the deployment and view the computing result
On the Developments page, start the deployment and view the status of the deployment.

**Step 1: Create an SQL draft and write business code**

1. Create an SQL draft.
i. Log on to the Realtime Compute for Apache Flink Console. ii. In the left-side navigation pane, click **Namespaces**. iii. Find the namespace that you want to manage and click **Console** in the **Actions** column. iv. In the left-side navigation pane, choose Applications > **Draft Editor**. v. Click **New**. ed vi. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Example | description |
|---|---|---|
| Name | flink-test | The name of the draft that you want to create. Note The draft name must be unique in the current project. |
| Type | STREAM / SQL | Streaming drafts and batch drafts support the following file types: SQL JAR PYTHON |
| Deployment Target | vvp-workload | The name of the cluster in which you want to deploy the draft. Realtime Compute for Apache Flink supports per- job clusters and session clusters. For more information about the differences between the two types of clusters, see Configure a session cluster. |
| Location | Development | The folder in which the code file of the draft is stored. By default, the code file of the draft is stored in the Development folder. You can also click the icon to the right of an existing folder to create a subfolder. |

vii. Click **OK**.
2. Copy the following code of a draft to the code editor.
Create the datagen source table that generates random data, and insert the data in the name field in the datagen source table into a blackhole result table. The following example shows the draft code. ed

```
CREATE TEMPORARY TABLE datagen_source(
  randstr VARCHAR
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE print_table(
  randstr  VARCHAR
) WITH (
  'connector' = 'print',
  'logger' = 'true'
```

);

```
INSERT INTO print_table SELECT SUBSTRING(randstr,0,8) from datagen_source;
```

3. Click **Validate** to check the syntax.
4. After the check is passed, click **Publish**.
5. Click **OK**.

**Step 2: Start the deployment and view the computing result**

1. In the left-side navigation pane, click **Deployments**.
2. Find the deployment that you want to manage and click **Start** in the **Actions** column.
i. Configure resource settings. By default, **Resource Setting Mode** is set to **Basic**. Configure **Parallelism** and **Flink**
**Configuration** based on your business requirements. Then, click **Next**.
ed ii. Configure basic settings. Specify **Starting Strategy**. Click **More** and configure the parameters. Then, click **Start**.
3. After you click Start, you can view the transition process from the current state to a desired
state and the final result. When the state changes to **RUNNING**, the deployment is running properly.
4. View the computing result.
i. On the **Deployments** page, click the name of the deployment that you want to manage. The **Overview** tab appears by default. ii. In the **Current Job** section, click **Flink UI**. The **Overview** page of **Apache Flink**
**Dashboard** appears by default.
iii. In the left-side navigation pane, click **Task Managers**. iv. Click the value in the **Path, ID** column. Click the **Logs** tab to view the computing result. ed

### 3.2 Get started with a JAR deployment

**deployment**

Realtime Compute for Apache Flink allows you to edit and run deployments by using JAR code. This topic describes how to create and run a JAR streaming deployment and a JAR batch deployment in the development console of Realtime Compute for Apache Flink.

**Procedure**

Step 1: Create a JAR streaming draft and configure the draft information or Step 1: Create a JAR batch draft and configure the draft information Step 3: Start the deployment and view the computing result

**Step 1: Create a JAR streaming draft and configure the draft**

**information**

1. Create a JAR streaming draft.
i. Log on to the Realtime Compute for Apache Flink Console. ii. In the left-side navigation pane, click **Namespaces**. iii. Find the namespace that you want to manage and click **Console** in the **Actions** column. iv. In the left-side navigation pane, click **Draft Editor**. v. Click **New**. ed vi. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| Name | flink-streaming- test-jar | The name of the draft that you want to create. Note The draft name must be unique in the current project. |
| Type | STREAM / JAR | Streaming drafts and batch drafts support the following file types: SQL JAR PYTHON |
| Deployment Target | vvp-workload | The name of the cluster in which you want to deploy the draft. Realtime Compute for Apache Flink supports per- job clusters and session clusters. For more information about the differences between the two types of clusters, see Configure a session cluster. |
| Location | Development | The folder in which the code file of the draft is stored. By default, the code file of the draft is stored in the Development folder. You can also click the icon to the right of an existing folder to create a subfolder. |

vii. Click **OK**.
2. On the Draft Editor page, configure basic settings.

| Parameter | Example | Description |
|---|---|---|
| Deployment Target | vvp-workload | You can change the cluster that you selected when you created the draft to another one. |
| JAR URI | hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/FlinkQuickStar t-1.0-SNAPSHOT.jar | Click FlinkQuickStart-1.0-SNAPSHOT.jar to download the test JAR package, and click the icon on the right side of the JAR URI field to select the test JAR package and upload the package. |

ed

| Entry Point Class | org.example.WordCou ntStreaming | Specify the entry point class of the application. If you do not specify a main class for the JAR package, enter a standard path in the Entry Point Class field. Note In this example, the test JAR package contains both streaming draft code and batch draft code. Therefore, you must configure this parameter to specify a program entry point for the streaming draft. |
|---|---|---|
| Entry Point Main Arguments | --input hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/Shakespeare | The OSS directory in which you want to store the input data file. Note In this example, the input data file and the test JAR package are stored in the same directory. Click Shakespeare to download the input data file Shakespeare. You must also upload the input data file Shakespeare to the specified directory on the Artifacts page in the console of Realtime Compute for Apache Flink. The uploaded files are stored in the hdfs:///vvp/data/artifacts/namespace s/<Your NameSpace> directory. _ |
| Additional Dependencies | None | You can enter the OSS bucket in which the required dependency file is stored or the URL of the dependency file. |

3. In the upper-right corner of the Draft Editor page, click **Publish**.
4. Click **OK**.

**Step 1: Create a JAR batch draft and configure the draft**

**information**

1. Create a JAR batch draft.
i. Log on to the Realtime Compute for Apache Flink Console. ii. In the left-side navigation pane, click **Namespaces**. iii. Find the namespace that you want to manage and click **Console** in the **Actions** column. iv. In the left-side navigation pane, choose Applications > **Draft Editor**. v. Click **New**. ed vi. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| Name | flink-batch-test- jar | The name of the draft that you want to create. Note The draft name must be unique in the current project. |
| Type | BATCH / JAR | Streaming drafts and batch drafts support the following file types: SQL JAR PYTHON |
| Deployment Target | vvp-workload | The name of the cluster in which you want to deploy the draft. Realtime Compute for Apache Flink supports per- job clusters and session clusters. For more information about the differences between the two types of clusters, see Configure a session cluster. |
| Location | Development | The folder in which the code file of the draft is stored. By default, the code file of the draft is stored in the Development folder. You can also click the icon to the right of an existing folder to create a subfolder. |

vii. Click **OK**.
2. On the Draft Editor page, configure basic settings.

| Parameter | Example | Description |
|---|---|---|
| Deployment Target | vvp-workload | You can change the cluster that you selected when you created the draft to another one. |
| JAR URI | hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/FlinkQuickStar t-1.0-SNAPSHOT.jar | Click FlinkQuickStart-1.0-SNAPSHOT.jar to download the test JAR package, and click the icon on the right side of the JAR URI field to select the test JAR package and upload the package. |

ed

| Entry Point Class | org.example.WordCou ntBatch | Specify the entry point class of the application. If you do not specify a main class for the JAR package, enter a standard path in the Entry Point Class field. Note In this example, the test JAR package contains both streaming draft code and batch draft code. Therefore, you must configure this parameter to specify a program entry point for the batch draft. |
|---|---|---|
| Entry Point Main Arguments | --input hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/Shakespeare --output hdfs:///vvp/data/artifa cts/namespaces/flink- test-default/batch- quickstart-test- output.txt | Enter the directory in which the input data file and the output data file are stored. Note In this example, the input data file, output file, and test JAR package are stored in the same directory. This example shows how to configure this parameter to write the computing result to the specified directory. You need to only specify the directory and name of the output data file. You do not need to create a directory in advance. Click Shakespeare to download the input data file Shakespeare. You must also upload the input data file Shakespeare to the specified directory on the Artifacts page in the console of Realtime Compute for Apache Flink. The uploaded files are stored in the hdfs:///vvp/data/artifacts/namespace s/<Your NameSpace> directory. _ |
| Additional Dependencies | None | You can enter the OSS bucket in which the required dependency file is stored or the URL of the dependency file. |

3. In the upper-right corner of the Draft Editor page, click **Publish**.
4. Click **OK**.

**Step 3: Start the deployment and view the computing result**

1. In the left-side navigation pane, click **Deployments**.
2. Find the deployment that you want to manage and click **Start** in the **Actions** column.
ed i. Configure resource settings. By default, **Resource Setting Mode** is set to **Basic**. Configure CPU cores, memory, parallelism, and Flink configuration based on your business requirements. Then, click
**Next**.
ii. Configure basic settings. Specify **Starting Strategy**. Click **More** and configure the parameters. Then, click **Start**.
3. After you click Start, you can view the transition process from the current state to a desired
state and the final result. When the state changes to RUNNING, the deployment is running properly.

> **Important:** If you want to start a batch deployment, you must change the deployment type from STREAM to **BATCH** on the **Deployments** page. By default, the system displays **streaming deployments**. To start a batch deployment, follow the instructions in the console.

4. View the computing result
ed View the computing result of a streaming deployment: a. On the **Deployments** page, click the name of the deployment that you want to manage. The **Overview** tab appears by default. b. In the **Current Job** section, click **Flink UI**. The **Overview** page of **Apache Flink**
**Dashboard** appears by default.
c. In the left-side navigation pane, click **Task Managers**. d. Click the value in the **Path, ID** column. Click the **Logs** tab to view the computing result. View the computing result of a batch deployment: In the left-side navigation pane, click
**Artifacts**. Download the result file to view.

### 3.3 Getting started with a Python deployment

**deployment**

ed Realtime Compute for Apache Flink allows you to edit and run deployments by using Python code. This topic describes how to create and run a Python streaming deployment and a Python batch deployment in the Realtime Compute for Apache Flink console.

**Limits**

Python deployments are supported only by Ververica Runtime (VVR) 8.x and later if you use Compute-storage Decoupled Edition that runs on the Advanced RISC Machine (ARM) architecture.

**Procedure**

Step 1: Create and configure a Python streaming draft or Create and configure a Python batch draft Step 2: Start the deployment and view the computing result

**Step 1: Create and configure a Python streaming draft**

1. Create a Python streaming draft.
i. Log on to the Realtime Compute for Apache Flink Console. ii. In the left-side navigation pane, click **Namespaces**. iii. Find the namespace that you want to manage and click **Console** in the **Actions** column. iv. In the left-side navigation pane, click **Draft Editor**. v. Click **New**. ed vi. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| Name | flink-streaming- test-python | The name of the draft that you want to create. Note The draft name must be unique in the current project. |
| Type | Stream/Python | Streaming drafts and batch drafts support the following file types: SQL JAR PYTHON |
| Deployment Target | vvp-workload | The cluster in which the draft is deployed. Note Python drafts support only Per-Job clusters. |
| Location | Development | The folder in which the code file of the draft is stored. By default, the code file of the draft is stored in the Development folder. You can also click the icon to the right of an existing folder to create a subfolder. |

vii. Click **OK**.
2. On the Draft Editor page, configure the basic settings.

| Parameter | Example | Description |
|---|---|---|
| Deployment Target | vvp-workload | You can change the cluster that you selected for the draft to another one. |
| Python Uri | hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/word count st _ _ reaming.py | The Python file. Download the test Python file word count streaming.py and click the icon _ _ on the right side of the Python Uri field to select and upload the test Python file. |

ed

| Entry Module | You do not need to configure this parameter. | The entry point class of the Python program. If the file that you upload is a .py file, you do not need to configure this parameter. If the file that you upload is a .zip file, you must configure this parameter. For example, you can set the Entry Module parameter to word count. _ |
|---|---|---|
| Entry Point Main Arguments | --input hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/Shakespeare --output hdfs:///vvp/data/artifa cts/namespaces/flink- test-default/ | The Object Storage Service (OSS) directory in which you want to store the input data file. Note In this example, the input data file, output file, and test Python file are stored in the same directory. This example shows how to configure this parameter to write the computing result to the specified directory. You only need to specify the directory and name of the output data file. You do not need to create a directory in advance. Click Shakespeare to download the input data file Shakespeare. You must also upload the input data file Shakespeare to the specified directory on the Artifacts page in the console of Realtime Compute for Apache Flink. The uploaded files are stored in the hdfs:///vvp/data/artifacts/namespace s/<Your NameSpace> directory. _ |
| Python Libraries | You do not need to configure this parameter. | Specify the third-party Python package that you want to use. The third-party Python package that you uploaded is added to PYTHONPATH of the Python worker process so that the package can be directly accessed in Python user-defined functions (UDFs). |

ed

| Python Archives | You do not need to configure this parameter. | Archive files. Only ZIP files such as .zip, .jar, .whl, and .egg are supported. Archive files are decompressed to the working directory of the Python worker process. For example, if the name of the compressed file where the archive files are located is mydata.zip, the following code can be written in the Python UDFs to access the mydata.zip archive file: def map(): with open("mydata.zip/mydata/data.txt") as f: ... |
|---|---|---|
| Additional Dependencies | You do not need to configure this parameter. | You can enter the OSS bucket in which the required dependency file is stored or the URL of the dependency file. |

3. In the upper-right corner of the Draft Editor page, click **Publish**.
4. Click **OK**.

**Step 1: Create and configure a Python batch draft**

1. Create a Python batch draft.
i. Log on to the Realtime Compute for Apache Flink Console. ii. In the left-side navigation pane, click **Namespaces**. iii. Find the namespace that you want to manage and click **Console** in the **Actions** column. iv. In the left-side navigation pane, click **Draft Editor**. v. Click **New**. ed vi. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| Name | flink-batch-test- python | The name of the draft that you want to create. Note The draft name must be unique in the current project. |
| Type | Batch/PYTHON | Streaming drafts and batch drafts support the following file types: SQL JAR PYTHON |
| Deployment Target | vvp-workload | The name of the cluster in which you want to deploy the draft. Realtime Compute for Apache Flink supports per- job clusters and session clusters. For more information about the differences between the two types of clusters, see Configure a session cluster. |
| Location | Development | The folder in which the code file of the draft is stored. By default, the code file of the draft is stored in the Development folder. You can also click the icon to the right of an existing folder to create a subfolder. |

vii. Click **OK**.
2. On the Draft Editor page, configure the basic settings.

| Parameter | Example | Description |
|---|---|---|
| Deployment Target | vvp-workload | You can change the cluster that you selected for the draft to another one. |

ed

| Python Uri | hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/word count b _ _ atch.py | The Python file. Download the test Python file word count batch.py and click the icon on _ _ the right side of the Python Uri field to select and upload the test Python file. |
|---|---|---|
| Entry Module | You do not need to configure this parameter. | The entry point class of the Python program. If the file that you upload is a .py file, you do not need to configure this parameter. If the file that you upload is a .zip file, you must configure this parameter. For example, you can set the Entry Module parameter to word count. _ |

ed

| Entry Point Main Arguments | --input hdfs:///vvp/data/artifa cts/namespaces/flink- test- default/Shakespeare --output hdfs:///vvp/data/artifa cts/namespaces/flink- test-default/ | The OSS directory in which you want to store the input data file. Note In this example, the input data file, output file, and test Python file are stored in the same directory. This example shows how to configure this parameter to write the computing result to the specified directory. You only need to specify the directory and name of the output data file. You do not need to create a directory in advance. Click Shakespeare to download the input data file Shakespeare. You must also upload the input data file Shakespeare to the specified directory on the Artifacts page in the console of Realtime Compute for Apache Flink. The uploaded files are stored in the hdfs:///vvp/data/artifacts/namespace s/<Your NameSpace> directory. _ |
|---|---|---|
| Python Libraries | You do not need to configure this parameter. | Specify the third-party Python package that you want to use. The third-party Python package that you uploaded is added to PYTHONPATH of the Python worker process so that the package can be directly accessed in Python UDFs. |

ed

| Python Archives | You do not need to configure this parameter. | Archive files. Only ZIP files such as .zip, .jar, .whl, and .egg are supported. Archive files are decompressed to the working directory of the Python worker process. For example, if the name of the compressed file where the archive files are located is mydata.zip, the following code can be written in the Python UDFs to access the mydata.zip archive file: def map(): with open("mydata.zip/mydata/data.txt") as f: ... |
|---|---|---|
| Additional Dependencies | You do not need to configure this parameter. | You can enter the OSS bucket in which the required dependency file is stored or the URL of the dependency file. |

3. In the upper-right corner of the Draft Editor page, click **Publish**.
4. Click **OK**.

**Step 2: Start the deployment and view the computing result**

1. In the left-side navigation pane, click **Deployments**.
2. Select **STREAM** or **BATCH** from the drop-down list, find the deployment that you want to
start, and then click **Start** in the **Actions** column. i. Configure resource settings. By default, **Resource Setting Mode** is set to **Basic**. Configure CPU cores, memory, parallelism, and Flink settings based on your business requirements. Then, click **Next**. ed ii. Configure basic settings. Specify **Starting Strategy**. Click **More**, configure the parameters, and then click **Start**.
3. After you click Start, you can view the transition process from the current state to a desired
state and the final result. When the state changes to RUNNING, the deployment is running properly.

> **Important:** If you want to start a batch deployment, you must change the deployment type from STREAM to **BATCH** on the **Deployments** page. By default, the system displays **streaming deployments**. To start a batch deployment, follow the instructions in the console.

4. View the computing result.
In the left-side navigation pane, click **Artifacts**. Download the result file. In this example, the result file is 2025-05-30--15/prefix-db40307b-47ff-4cba-acbc-18febf890137-0.ext. pment

## 4 Draft development

### 4.1 Sample center

#### 4.1.1 Data synchronization templates

Flink CDC connectors can be used to synchronize data and table schema changes in real time. You can use a data synchronization template to quickly generate Flink SQL deployment code for data synchronization. This topic describes how to use a multi-database multi-table synchronization template or a sharded-data merging template to synchronize data.

**Background information**

Realtime Compute for Apache Flink supports the following data synchronization methods: multi-database multi-table synchronization and sharded-data merging. The following table describes the differences between the methods.

| Synchronizat ion method | Description |
|---|---|
| Multi-database and multi-table synchronizatio n | If you want to synchronize one or more business data tables from one or more databases to another database in real time, you can use the multi-database multi- table synchronization template. Flink CDC connectors can automatically synchronize the full and incremental data of an entire database. Flink CDC connectors can also synchronize the schema changes of each source table, such as added columns, to the destination table in real time. Multi-database and multi-table synchronization templates translate parameters into CREATE DATABASE AS statements. |
| Sharded-data merging | If your business data is scattered in different databases or business tables, you need to merge multiple tables in a sharded database to synchronize data from the tables that have a similar schema to one destination table. Flink CDC connectors can automatically synchronize the full and incremental data of all table shards in the sharded database from source databases. The tables include the new tables that meet regular expressions. Flink CDC connectors can also synchronize the table schema changes of each source table, such as added columns, to the destination table in real time. Sharded-data merging templates translate parameters into CREATE DATABASE AS statements. |

**Limits**

Flink CDC connectors can synchronize data only from MySQL to Hologres.

**Usage notes**

If you use a Flink CDC connector to synchronize data from MySQL to Hologres, the table schema changes are also synchronized. Take note of the following items: You do not need to manually create a table in Hologres. Realtime Compute for Apache Flink automatically creates a table in Hologres. However, if the required table already exists in Hologres, Realtime Compute for Apache Flink synchronizes data based on the destination database and table that you select. Hologres does not allow you to change the data types of columns. pment If the data type of the current field is different from the data type of the Hologres table, the data fails to be written. In this case, you must modify the data type of the column and synchronize the data again.

**Procedure**

**Configure the MySQL and Hologres storage IP addresses**

1. Log in to the MySQL and Hologres instances and obtain the instance domain name
information.
2. Log in to the OPS machine and run the `ping` command to obtain the IP addresses of
MySQL and Hologres.
3. For more information about how to configure the storage IP addresses of MySQL and
Hologres, see Configure an external storage IP address.

**Create a MySQL catalog and a Hologres catalog**

1. Log on to the Realtime Compute for Apache Flink Console.
2. In the left-side navigation pane, click **Namespaces**.
3. Find the namespace that you want to manage and click **Console** in the **Actions** column.
4. In the left-side navigation pane, click **Draft Editor**, click **Schemas**, click the **+** icon, and
then click **Create Catalog**.
5. Select MySQL and configure the catalog information.
pment

| Parameter | Description |
|---|---|
| catalog name | The custom name of the catalog. |
| hostname | The IP address or host name of the MySQL database server. |
| port | The port that is used to connect to the host. The default port is 3306. |
| default-database | The name of the default database. |
| username | The username that is used to connect to the ApsaraDB RDS for MySQL database server. |
| password | The password that is used to connect to the ApsaraDB RDS for MySQL database server. |

6. Repeat the preceding step to create a Hologres catalog.
pment

| Parameter | Description |
|---|---|
| catalog name | The custom name of the catalog. |
| endpoint | The endpoint of the Hologres instance. |
| username | The username is the AccessKey ID of the enterprise. |
| password | The password is the AccessKey secret of the enterprise. |
| dbname | The name of the Hologres database. |

**Data synchronization**

1. In the left-side navigation pane, click **Sample Center**.
2. On the **Flink CDC** tab, click **Data Synchronization from MySQL to Hologres** and click
**Next** in the lower-right corner of the tab.
3. Configure the synchronization task.
i. Configure the source, sink, and the parameters in the **MySQL(source) Configuration** section, and then click **Next**. pment

| Section | Parameter | Description |
|---|---|---|
| Source | MySQL Catalog | You can select the MySQL catalog that you created. If no MySQL catalog exists, click Create Catalog. |
|   | MySQL server-id | Enter a unique ID for each MySQL database client. Valid values: 5400 to 6400. This parameter can also be set to an ID range, such as 5400-5408. If you enable parallel reading in incremental reading mode, we recommend that you set this parameter to a value range to ensure that the server ID for each parallel thread is unique. Important We recommend that you do not use the same server ID for different deployments or services that access the database. |
| Sink | Hologres Catalog | You can select the Hologres catalog that you created. If no Hologres catalog exists, click Create Catalog. |

ii. Create a plan. pment Multi-database and multi-table synchronization a. On the **To Single Database** tab, select the source database and table name. b. Click **Save Plan** and then click **Next**. c. View the SQL code that is generated based on the destination database and table that you selected. Then, click **OK**. You can modify the **Name**, **Location**, or **Engine Version** parameter based on your business requirements. pment Sharded-data merging a. On the **To Multiple Databases** tab, select the names of the source databases and tables, or enter the names of the destination databases and tables.

> **Note:** We recommend that you use regular expressions to specify the source databases and source tables.

b. Click **Save Plan** and then click **Next**. You can create multiple plans for multi-database and multi-table synchronization and sharded-data merging at the same time in a draft. c. View the SQL code that is generated based on the destination database and table that you selected. Then, click **OK**. You can modify the **Name**, **Location**, or **Engine Version** parameter based on your business requirements. After the draft is created, the draft development page appears. The subsequent operations are the same as the operations that are used to develop a common draft. For more information about the parameter configurations and subsequent operations, see Draft development and Start a deployment.

#### 4.1.2 Code templates

Realtime Compute for Apache Flink provides various code templates. Each code template provides use scenarios, code samples, and instructions. Code templates can help you quickly understand the features and syntax of Realtime Compute for Apache Flink and implement your own business logic. This topic describes the use scenarios for code templates and how to use a code template.

**Usage notes**

If a code template that is used for a draft does not contain the INSERT INTO statement, you cannot deploy the draft.

**Supported code templates**

pment The following table describes the code templates that are provided by Realtime Compute for Apache Flink and the applicable scenario of each code template. You can view the supported code templates in the Realtime Compute for Apache Flink console.

| Category | Template name | Applicable scenario |
|---|---|---|
| Basic templates | Create Table | If you want to create a table and save the table in a catalog, you can execute the CREATE TABLE statement. The operation on a table is similar to the operation on a database. |
|   | Create Temporary Table | If you want to use a table only in the current session or an SQL script, you can execute the CREATE TEMPORARY TABLE statement to create a temporary table. |
|   | Create Temporary View | If you want to reuse code, create a long query, or write an SQL script to simplify draft development when you develop a Flink SQL draft, you can execute the CREATE TEMPORARY VIEW statement to create a temporary view. |
|   | INSERT INTO | If you want to write query results to a table in a downstream storage system, you can execute the INSERT INTO statement. |
|   | STATEMENT SET | If you want to write query results to two or more downstream storage systems, you can use the STATEMENT SET syntax. |
|   | Watermark | If you want Realtime Compute for Apache Flink to correctly process out-of-order data, you can use the WATERMARK clause in DDL statements. You can use the WATERMARK clause in a CREATE TABLE DDL statement to create a watermark. This clause defines an expression to generate watermarks based on an existing field and marks the field as a time attribute field. For more information, see Event Time and Watermarks. |
|   | GROUP BY | If you want to aggregate and analyze data in real time, you can use the GROUP BY clause. |
|   | Tumble Window Aggregation | If you want to group time series data and aggregate and analyze the data in each group, you can use the TUMBLE function. |
|   | Hop Window Aggregation | If you want to update data in a window at a specified interval, you can use the HOP function. |

pment

|   | Aggregation and analysis templates |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   | Cumulate Window Aggregation | If you want to view the calculation results of a window in advance, such as viewing the latest result of the window at an interval of one minute, you can use the CUMULATE function. Note The CUMULATE function cannot be used to aggregate Change Data Capture (CDC) data. If you use the CUMULATE function to aggregate CDC data, the error message "org.apache.flink.table.api.TableException: Not |   |   |   |
|   |   |   |   | Note The CUMULATE function cannot be used to aggregate Change Data Capture (CDC) data. If you use the CUMULATE function to aggregate CDC data, the error message "org.apache.flink.table.api.TableException: Not |   |   |
|   |   |   |   |   | "org.apache.flink.table.api.TableException: Not |   |
|   |   |   |   | supported window type: CUMULATE(max size=[xxx _ |   |   |
|   |   |   |   | ms], step=[xxx min])" |   |   |
|   |   | Session Window Aggregation | If you want to collect the statistics of data in an active session in real time, you can use a SESSION function. |   |   |   |
|   |   | Over Window Aggregation | If you want to perform statistical analysis on each element in a window, you can use an OVER window. |   |   |   |
|   |   | Chained Window Aggregation | If you want to aggregate data of the same stream in different time dimensions, such as 1 minute, 5 minutes, 30 minutes, or 1 hour, you can use cascading windows. |   |   |   |
|   | Deduplication templates | Deduplication | If you want to remove duplicate data from a data stream, you can use the deduplication syntax. |   |   |   |
|   | Top-N templates | Top-N | If you want to sort the computing results in ascending or descending order based on your business requirements and obtain the first N data records, you can use the Top-N syntax. |   |   |   |
|   |   | Window Top-N | If you want to sort the computing results in ascending or descending order and obtain the first N data records in a specified time range, you can use the window Top-N syntax. |   |   |   |
|   | Complex event processing (CEP) templates | Pattern Recognizing | If you want to search for a set of event patterns in data streams, you can use the MATCH RECOGNIZE syntax. _ |   |   |   |
|   | JOIN templates | Regular Join | If you want to perform a join query on data of a table and a stream table, you can use a regular join. |   |   |   |
|   |   | Interval Join | If you want to perform a join query on data of a table and a stream table in a specified period of time, you can use an interval join. |   |   |   |
|   |   | Temporal Join | If you want to perform a join query on data of a stream table and the related time version data in another table, you can use a temporal join. |   |   |   |
|   | 4 |   |   |   |   |   |

pment

|   | Look-up Join | If you want to perform a join query on data of a static dimension table and a stream table, you can use a look-up join. |
|---|---|---|

**Procedure**

This procedure describes how to use a code template. In this example, the **Create Table** template is used.
1. Log on to the Realtime Compute for Apache Flink Console.
2. In the left-side navigation pane, click **Namespaces**.
3. Find the namespace that you want to manage and click **Console** in the **Actions** column.
4. In the left-side navigation pane, click **Sample Center**.
5. On the **SQL Scripts** tab, click the name of the template that you want to manage. In the
lower-left corner of the page, click **Next**.
6. Modify **Name**, **Deployment Target**, **Location**, and the SQL code based on your business
requirements. pment
7. Click **Ok**.
After you click **Ok**, the SQL Editor page appears. The subsequent operations are the same as the operations that are used to develop a common draft. For more information about the parameter configurations and subsequent operations, see Draft development and Start a deployment.

### 4.2 Develop an SQL draft

This topic describes how to develop an SQL draft in the Realtime Compute for Apache Flink console.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
i. Log in to the Realtime Compute for Apache Flink console. ii. Find the namespace that you want to manage and click **Console** in the Actions column.
2. Create an SQL streaming draft.
i. In the left-side navigation pane, click **SQL Editor**. In the upper-left corner of the SQL Editor page, click **New**. ii. On the SQL Scripts tab of the New Draft dialog box, click **Blank Stream Draft**. Realtime Compute for Apache Flink provides various code templates and data synchronization templates. Each code template provides use scenarios, code samples, and instructions. You can click a template to learn about the features and the related syntax of Realtime Compute for Apache Flink and implement your business logic. iii. Click **Next**. pment iv. In the **New Draft** dialog box, configure the parameters of the draft. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of the draft that you want to create. Note The draft name must be unique in the current namespace. |
| Location | The folder in which the code file of the draft is stored. You can also click the icon to the right of an existing folder to create a subfolder. |
| Engine Version | You can view the engine version of Flink that is used by the deployment. |

v. Click **Create**.
3. Write DDL and DML statements.

> **Note:** The metadata management feature allows you to reuse the table schema that is created in different drafts. When you edit an SQL draft on the SQL Editor page in the console of fully managed Flink, the system automatically completes the fields and table names after you enter only specific characters.

The following sample code shows how to configure the partition.discovery.interval.ms option: pment

```
-- Create a source table named datagen_source. CREATE TEMPORARY TABLE datagen_source(
  name VARCHAR
) WITH (
  'connector' = 'datagen'
```

);

```
-- Create a sink table named blackhole_sink. CREATE TEMPORARY TABLE blackhole_sink(
  name  VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
-- Insert data from the source table datagen_source into the sink table blackhole_sink. INSERT INTO blackhole_sink SELECT
  name
from datagen_source;
```

4. On the right side of the **SQL Editor** page, click a desired tab to view or enter the
configuration information on the tab based on your business requirements.

| Tab name | Description |
|---|---|
| Configur ations | Engine Version: We recommend that you use a recommended version or a stable version. Engine versions are classified into the following types: Recommend: the latest minor version of the current major version. Stable: the latest minor version of the major version that is still in use within the validity period for renewal. Defects in previous versions are fixed. Normal: other minor versions that are still in use within the validity period for renewal. Deprecated: the version that exceeds the service period of the product. Additional Dependencies: the additional dependencies that are used in the draft, such as temporary functions. |
| Structur e | Flow Diagram: the flow diagram that allows you to view the directions in which data flows. Tree Diagram: the tree diagram that allows you to view the source from which data is processed. |
| Versions | You can view the draft version on this tab. |

5. Click **Validate**.
Check the SQL semantics of the draft and the metadata information of the tables that are used by the draft.
6. **Optional:** Click **Debug**.
pment You can enable the debugging feature to simulate deployment running, check outputs, and verify the business logic of SELECT and INSERT statements. This feature improves development efficiency and reduces the risks of poor data quality. For more information, see Debug a deployment.
7. Click **Deploy**.
After the draft development and syntax check are complete, you can deploy the draft to publish the data to the production environment.
8. In the **Deploy draft** dialog box, enter a comment, select an option in the **Advanced**
**Options** section, and then click **Confirm**.

### 4.3 Develop a JAR draft

Realtime Compute for Apache Flink DataStream provides flexible programming models and APIs, which allow you to specify data conversions, perform operations, and configure operators to meet requirements for complex business logic and data processing. This topic describes how to develop and debug a JAR draft of Realtime Compute for Apache Flink.

**Limits**

To prevent the impact of factors such as deployment and network environments, take note of the following points: Only DataStream JAR drafts can be published. A JAR draft can use only one main JAR file and multiple JAR dependencies. Realtime Compute for Apache Flink cannot read local configurations by using the main() method in a JAR draft. Workspaces that use x86 CPUs support only JDK 8. Workspaces that use Advanced RISC Machine (ARM) CPUs support JDK 8 and JDK 11. Only open source Scala V2.12 is supported.

**Usage notes**

The parameters in the deployment code take precedence over the parameters that you configured in the Realtime Compute for Apache Flink console. To ensure that your deployment runs as expected, we recommend that you configure checkpoint-related parameters in the Realtime Compute for Apache Flink console instead of in the deployment code. If the upstream and downstream storage systems that Flink DataStream deployments access use a whitelist mechanism, you must configure whitelists. To prevent conflicts between JAR package dependencies, take note of the following items: Make sure that the Realtime Compute for Apache Flink version that you select on the Draft Editor page is the same as that specified in the dependency library of Apache Flink in the POM file. Specify `<scope>provided</scope>` for dependencies related to Realtime Compute for Apache Flink. Dependencies related to Realtime Compute for Apache Flink mainly include non-connector dependencies whose names start with `flink-` in the `org.apache.flink` group, such as flink-streaming-java, flink-streaming-java_2.11, flinkjava, and flink-runtime.

> **Note:** We recommend that you configure dependencies during draft development to avoid Flink dependency conflicts.

pment Use the Shade plug-in to package other third-party dependencies. For more information, see Apache Maven Shade plug-in. Call only methods that are explicitly marked with @Public or @PublicEvolving in the source code of Apache Flink. Apsara Stack Realtime Compute for Apache Flink only ensures compatibility with these methods. Use the built-in dependencies of Realtime Compute for Apache Flink if the DataStream APIs supported by the built-in connectors of Realtime Compute for Apache Flink are used.

**Develop a draft**

> **Note:** You must develop drafts in your on-premises environment before you deploy the drafts for running in the Realtime Compute for Apache Flink console.

**References**

For more information about the description, architecture, applications, and features of Apache Flink, see Introduction to Apache Flink. For more information about how to develop business code of Apache Flink 1.17, see Flink DataStream API Programming Guide and Flink Table API and SQL. For more information about the coding guide, Java and Scala language guides, and component and formatting guides, see Apache Flink Code Style and Quality Guide. For more information about the configuration of the source code of Apache Flink deployments, see Project Configuration. For more information about DataStream connector dependencies of Realtime Compute for Apache Flink, see Connector dependencies. Issues may occur when you develop code in Apache Flink. For more information about the issues and fixes, see FAQ.

**Write business code**

1. Integrate external data sources into data streaming programs of Realtime Compute for
Apache Flink. `Watermarks` are computing strategies based on time semantics in Realtime Compute for Apache Flink. In most cases, watermarks are used together with timestamps. In this example, watermark strategies are not used. For more information, see Generating Watermarks.

```
         // Integrate external data sources into data streaming programs of Realtime
Compute for Apache Flink.
        // Specify WatermarkStrategy.noWatermarks(), which indicates that no
watermark strategy is used.
        DataStreamSource<String> stream = env.fromSource(kafkaSource,
WatermarkStrategy.noWatermarks(), "kafka Source");
```

2. Convert operators.

| In this example, the | DataStream<String> |   |
|---|---|---|
| DataStream<Student> |   |   |
|   |   | . For more informat |

`DataStream<Student>` . For more information about how to convert and process more complex operators, see Operators. pment

```java
          // Convert the operator whose data structure is student.
          DataStream<student> source = stream
                .map(new MapFunction<String, student>() {
                    @Override
                    public student map(String s) throws Exception {
                        // Separate data with commas (,).
                        String[] data = s.split(",");
                        return new student(Integer.parseInt(data[0]), data[1], Integer
.parseInt(data[2]));
```

`}`

```
                }).filter(student -> student.score >=60); // Obtain data records whose
score is greater than 60.
```

**Package the JAR file of the draft**

Package the JAR file of the draft by using maven-shade-plugin.

> **Important:** If you upload the uber JAR files of the connectors to the development console of Realtime Compute for Apache Flink and call the uber JAR files as additional dependency files in a DataStream draft, you must specify
> `<scope>provided</scope>` for dependencies of the connectors when you package the JAR file of the draft.
> If you package the connectors as project dependencies into the JAR file of your draft, you must specify <scope>compile</scope> for dependencies of the connectors when you package the JAR file of the draft.

Configuration of maven-shade-plugin for reference

```xml
<build>
        <plugins>
            <!-- Java compiler -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${target.java.version}</source>
                    <target>${target.java.version}</target>
                </configuration>
            </plugin>
            <!-- Use maven-shade-plugin to create a fat JAR file that contains all the
necessary dependencies. -->
            <!-- Modify the value of <mainClass> if your program entry point changes. -
```

`->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
```

`l` pment

```xml
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <!-- Remove unnecessary dependencies. -->
                        <configuration>
                            <artifactSet>
                                <excludes>
                                    <exclude>org.apache.flink:force-shading</exclude>
                                    <exclude>com.google.code.findbugs:jsr305</exclude>
                                    <exclude>org.slf4j:*</exclude>
                                    <exclude>org.apache.logging.log4j:*</exclude>
                                </excludes>
                            </artifactSet>
                            <filters>
                                <filter>
                                    <!-- Do not copy the signature in the META-INF
folder. Otherwise, a security error may occur when you use the JAR file. -->
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                            <transformers>
                                <transformer
implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.aliyun.FlinkDemo</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```

**Test and deploy the draft**

By default, Realtime Compute for Apache Flink cannot access the Internet. In this case, you may be unable to directly test your code in an on-premises machine. We recommend that you separately perform unit tests. For more information, seeCreate a deployment.

> **Note:** If you use the JAR files of the connectors when you deploy the draft, you must upload the JAR files of the connectors to the Realtime Compute for Apache Flink console.
> If you want to read the configuration file, you must add the configuration file to the Additional Dependencies field in the Create Jar Deployment dialog box.

pment

**Complete sample code**

In this example, data of the Kafka data source is processed and written to the MySQL database. This example is for reference only. For more information about the code style and quality guidelines, see Apache Flink Code Style and Quality Guide.

> **Note:** The example does not include some runtime configurations, such as the checkpoint, time- to-live (TTL), and restart policy. You can customize the preceding configurations on the **Deployment Details** page after the deployment is created. Configurations submitted by code take precedence. We recommend that you use custom configurations when you create deployments to facilitate subsequent modification and use.

**FlinkDemo.java**

```java
package com.aliyun; import org.apache.flink.api.common.eventtime.WatermarkStrategy; import org.apache.flink.api.common.functions.MapFunction; import org.apache.flink.connector.jdbc.JdbcConnectionOptions; import org.apache.flink.connector.jdbc.JdbcExecutionOptions; import org.apache.flink.connector.jdbc.JdbcSink; import org.apache.flink.connector.jdbc.JdbcStatementBuilder; import org.apache.flink.connector.kafka.source.KafkaSource; import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer; import org.apache.flink.connector.kafka.source.reader.deserializer.KafkaRecordDeserializationSch
```

a;

```java
import org.apache.flink.kafka.shaded.org.apache.kafka.common.serialization.StringDeserializer; import org.apache.flink.streaming.api.datastream.DataStream; import org.apache.flink.streaming.api.datastream.DataStreamSource; import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment; import java.io.FileInputStream; import java.io.IOException; import java.io.InputStream; import java.sql.PreparedStatement; import java.sql.SQLException; import java.util.HashMap; import java.util.Map; import java.util.Properties; public class FlinkDemo {
    // Define the data structure.
    public static class Student {
        public int id;
        public String name;
        public int score;
        public Student(int id, String name, int score) {
            this.id = id;
            this.name = name;
            this.score = score;
```

pment `}` `}`

```
    public static void main(String[] args) throws Exception {
        // Create a Flink execution environment.
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        Properties properties = new Properties();
        Map<String,String> configMap = new HashMap<>();
        try (InputStream input = new
FileInputStream("/flink/usrlib/config.properties")) {
            // Load the property file.
            properties.load(input);
            // Obtain the property values.
configMap.put("bootstrapServers",properties.getProperty("bootstrapServers")) ;
            configMap.put("inputTopic",properties.getProperty("inputTopic"));
            configMap.put("groupId",properties.getProperty("groupId"));
            configMap.put("url",properties.getProperty("database.url")) ;
            configMap.put("username",properties.getProperty("database.username"));
            configMap.put("password",properties.getProperty("database.password"));
        } catch (IOException ex) {
            ex.printStackTrace();
```

`}`

```java
        // Build Kafka source
        KafkaSource<String> kafkaSource = KafkaSource.<String>builder()
                        .setBootstrapServers(configMap.get("bootstrapServers"))
                        .setTopics(configMap.get("inputTopic"))
                        .setStartingOffsets(OffsetsInitializer.latest())
                        .setGroupId(configMap.get("groupId"))
.setDeserializer(KafkaRecordDeserializationSchema.valueOnly(StringDeserializer.class))
                        .build();
        // Integrate the external data source into the Flink DataStream program
        // Specify WatermarkStrategy.noWatermarks(), which indicates that no watermark
strategy is used.
        DataStreamSource<String> stream = env.fromSource(kafkaSource,
WatermarkStrategy.noWatermarks(), "kafka Source");
        // Obtain data records whose score is greater than 60.
        DataStream<Student> source = stream
                .map(new MapFunction<String, Student>() {
                    @Override
                    public Student map(String s) throws Exception {
                        String[] data = s.split(",");
                        return new Student(Integer.parseInt(data[0]), data[1], Integer.p
arseInt(data[2]));
```

`}`

```
                }).filter(Student -> Student.score >=60);
```

pment

```
        source.addSink(JdbcSink.sink("INSERT IGNORE INTO student (id, username, score)
VALUES (?, ?, ?)",
                new JdbcStatementBuilder<Student>() {
                    public void accept(PreparedStatement ps, Student data) {
                        try {
                            ps.setInt(1, data.id);
                            ps.setString(2, data.name);
                            ps.setInt(3, data.score);
                        } catch (SQLException e) {
                            throw new RuntimeException(e);
```

`}` `}` `},`

```
                new JdbcExecutionOptions.Builder()
                        .withBatchSize(5) // The number of records to be written in each
batch.
                        .withBatchIntervalMs(2000) // The maximum delay that is allowed
for a retry. Unit: milliseconds.
                        .build(),
                new JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
                        .withUrl(configMap.get("url"))
                        .withDriverName("com.mysql.cj.jdbc.Driver")
                        .withUsername(configMap.get("username"))
                        .withPassword(configMap.get("password"))
                        .build()
        )).name("Sink MySQL");
        env.execute("Flink Demo");
```

`}` `}`

**pom.xml**

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v
4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.aliyun</groupId>
    <artifactId>FlinkDemo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>FlinkDemo</name>
    <packaging>jar</packaging>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <flink.version>1.17.1</flink.version>
        <vvr.version>1.17-vvr-8.0.4-1</vvr.version>
        <target.java.version>1.8</target.java.version>
        <maven.compiler.source>${target.java.version}</maven.compiler.source>
        <maven.compiler.target>${target.java.version}</maven.compiler.target>
        <log4j.version>2.14.1</log4j.version>
    </properties>
<dependencies>
```

pment

```xml
    <dependencies>
        <!-- Apache Flink dependencies -->
        <!-- Provide the dependencies to prevent them from being packaged in a JAR file
. -->
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-java</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-clients</artifactId>
            <version>${flink.version}</version>
            <scope>provided</scope>
        </dependency>
        <!-- Add the connector dependencies and specify <scope>compile</scope> for the
dependencies. -->
        <dependency>
            <groupId>com.alibaba.ververica</groupId>
            <artifactId>ververica-connector-kafka</artifactId>
            <version>${vvr.version}</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba.ververica</groupId>
            <artifactId>ververica-connector-mysql</artifactId>
            <version>${vvr.version}</version>
        </dependency>
        <!-- Add a logging framework to generate output data in the development console
of Realtime Compute for Apache Flink when you run the deployment. -->
        <!-- By default, these dependencies are excluded from the JAR file in the progr
am. -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j-impl</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
```

pment `g` `p` `g` `p` `gg` `g`

```
gj/g
```

`p`

```xml
            <artifactId>log4j-core</artifactId>
            <version>${log4j.version}</version>
            <scope>runtime</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <!-- Java compiler -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${target.java.version}</source>
                    <target>${target.java.version}</target>
                </configuration>
            </plugin>
            <!-- Use maven-shade-plugin to create a fat JAR file that contains all the
necessary dependencies. -->
            <!-- Modify the value of <mainClass> if your program entry point changes. -
```

`->`

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <!-- Remove unnecessary dependencies. -->
                        <configuration>
                            <artifactSet>
                                <excludes>
                                    <exclude>org.apache.flink:force-shading</exclude>
                                    <exclude>com.google.code.findbugs:jsr305</exclude>
                                    <exclude>org.slf4j:*</exclude>
                                    <exclude>org.apache.logging.log4j:*</exclude>
                                </excludes>
                            </artifactSet>
                            <filters>
                                <filter>
                                    <!-- Do not copy the signature in the META-INF
folder. Otherwise, a security error may occur when you use the JAR file. -->
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
```

pment

```xml
                            </filters>
                            <transformers>
                                <transformer
implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.aliyun.FlinkDemo</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 4.4 Develop a Python API draft

This topic describes the background information, limits, development methods, and debugging methods of Python API draft development in Realtime Compute for Apache Flink. This topic also describes how to use a connector.

**Background information**

You must develop a Python API draft in your on-premises environment. Then, you can deploy the draft and start the deployment for the draft in the development console of Realtime Compute for Apache Flink. For more information, see Getting started with a Python deployment. The following table lists the software packages that are installed in Realtime Compute for Apache Flink workspaces.

| Software package | Version |
|---|---|
| apache-beam | 2.23.0 |
| avro-python3 | 1.9.1 |
| certifi | 2020.12.5 |
| cloudpickle | 1.2.2 |
| crcmod | 1.7 |
| cython | 0.29.16 |
| dill | 0.3.1.1 |

pment

| docopt | 0.6.2 |
|---|---|
| fastavro | 0.23.6 |
| future | 0.18.2 |
| grpcio | 1.29.0 |
| hdfs | 2.6.0 |
| httplib2 | 0.17.4 |
| idna | 2.10 |
| jsonpickle | 1.2 |
| mock | 2.0.0 |
| numpy | 1.19.5 |
| oauth2client | 3.0.0 |
| pandas | 0.25.3 |
| pbr | 5.5.1 |
| pip | 20.1.1 |
| protobuf | 3.15.3 |
| py4j | 0.10.8.1 |
| pyarrow | 0.17.1 |
| pyasn1-modules | 0.2.8 |
| pyasn1 | 0.4.8 |

pment

| pydot | 1.4.2 |
|---|---|
| pymongo | 3.11.3 |
| pyparsing | 2.4.7 |
| python-dateutil | 2.8.0 |
| pytz | 2021.1 |
| requests | 2.25.1 |
| rsa | 4.7.2 |
| setuptools | 47.1.0 |
| six | 1.15.0 |
| typing-extensions | 3.7.4.3 |
| urllib3 | 1.26.3 |
| wheel | 0.36.2 |

**Limits**

Services provided by Realtime Compute for Apache Flink are subject to deployment environments and network environments. Therefore, when you develop Python API drafts, take note of the following items: Only Ververica Runtime (VVR) 8.0.7 and later that use Advanced RISC Machine (ARM) CPUs support Python drafts. Python 3.7.9 is pre-installed in your Realtime Compute for Apache Flink workspace, and common Python libraries such as pandas, NumPy, and PyArrow are pre-installed in the Python environment. Therefore, you must develop code in Python 3.7. Workspaces that use x86 CPUs support only JDK 8. Workspaces that use ARM CPUs support JDK 8 and JDK 11. Only open source Scala 2.11 is supported. If your Python API draft depends on a third-party JAR package, make sure that the JAR package is compatible with Scala 2.11.

**Develop a draft**

You can develop business code of Flink in your on-premises environment. For more information, see the following references: pment For more information about how to develop business code of Apache Flink 1.17, see Python API. Issues may occur when you develop code in Apache Flink. For more information about the issues and fixes, see FAQ.

**Debug the draft**

In the code of Python user-defined functions (UDFs), you can use the logging method to generate logs and locate errors based on the logs. The following code shows an example.

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

After logs are generated, you can view the logs in the log file of the TaskManager.

**Use a connector**

1. Log in to the Realtime Compute for Apache Flink console.
2. Find the namespace that you want to manage and click **Console** in the Actions column.
3. In the left-side navigation pane, click **Artifacts**.
4. Click **Upload Artifact** and select the Python package of the desired connector that you
want to upload. You can upload the Python package of a connector that you develop or a connector provided by Realtime Compute for Apache Flink. You can visit Connectors to download the official Python packages provided by Realtime Compute for Apache Flink.
5. On the **Deployments** page, click **Create Deployment**. In the Create Deployment dialog
box, select the Python package of the desired connector from the drop-down list of
**Additional Dependencies**.
6. On the Deployments page, click the name of the desired deployment. In the upper-right
corner of the **Parameters** section on the **Configuration** tab, click **Edit**. Then, add related configurations to the **Other Configuration** field. If your deployment depends on the Python packages of multiple connectors and the packages are named connector-1.jar and connector-2.jar, configure the following information:

```
pipeline.classpaths: 'file:///flink/usrlib/connector- 1.jar;file:///flink/usrlib/connector-2.jar'
```

### 4.5 Debug a deployment

You can enable the debugging feature to simulate deployment running, check outputs, and verify the business logic of the SELECT and INSERT statements. This feature improves development efficiency and reduces the risks of poor data quality. This topic describes how to debug a deployment.

**Limits**

You can debug only SQL deployments by clicking Debug on the SQL Editor page in the Realtime Compute for Apache Flink console. pment By default, Realtime Compute for Apache Flink reads a maximum of 1,000 data records. If the number of data records that are read by Realtime Compute for Apache Flink reaches the upper limit, Realtime Compute for Apache Flink stops reading data. Metrics of deployments that are deployed in session clusters cannot be displayed. Session clusters do not support the monitoring and alerting feature and the Autopilot feature.

**Procedure**

1. Develop an SQL draft. For more information, see Develop an SQL draft.
2. On the **SQL Editor** page, click **Debug**.
3. **Select a cluster for debugging** and click **Next**.
If no session cluster is available, you can create and start one. For more information, see Configure a session cluster.
4. Configure debugging data.
If you use online data for debugging, click **Confirm**. If you use mock data, click **Download mock data template**, enter your mock data in the template, and then click Upload mock data to upload the template. The following table describes the parameters in this step.

| Parameter | Description |
|---|---|
| Download mock data template | The template is adapted to the schema of the source table. |
| Upload mock data | If you need to debug a deployment by using mock data, you can download the mock data template, upload the data after you edit the template, and then select Use mock data. Limits on using a mock data file: Only CSV files can be uploaded. A CSV file must contain a table header, such as id(INT). A CSV file can contain a maximum of 1,000 data records but cannot be greater than 1 MB. |

pment

| Data Preview | After you upload mock data, click the icon on the left side of the source table name to preview the data and download the mock data. |
|---|---|
| Code Preview | The debugging feature automatically modifies the DDL statements of source and result tables. However, it does not change the draft code. You can preview code details in the lower part of Code Preview. |

5. Click **Confirm**.
After you click **Confirm**, the debugging result appears in the lower part of the SQL script editor.

### 4.6 Use Python dependencies

You can use custom Python virtual environments, third-party Python packages, JAR packages, and data files in a Flink Python Job. This topic describes how to use these dependencies in a Python Job.

**Background information**

This topic describes how to use Python dependencies in the following scenarios: Use a custom Python virtual environment Use third-party Python packages Use JAR packages Use data files

**Use a custom Python virtual environment**

The system currently supports only Python 3.7 virtual environments. The following procedure describes how to prepare a Python 3.7 virtual environment.
1. Prepare a Python 3.7 virtual environment.
i. Prepare the build.sh script locally. The content of the script is as follows:

```bash
#!/bin/bash
set -e -x yum install -y zip wget cd /root/ bash /build/setup-pyflink-virtual-env.sh mv venv.zip /build/
```

pment ii. Prepare the setup-pyflink-virtual-env.sh script locally. The content of the script is as follows:

```bash
set -e
# Download the Python 3.7 miniconda.sh script.
wget "https://repo.continuum.io/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh" -O "miniconda.sh"
# Add execution permissions to the Python 3.7 miniconda.sh script.
chmod +x miniconda.sh
# Create a Python virtual environment.
./miniconda.sh -b -p venv
# Activate the Conda Python virtual environment.
source venv/bin/activate ""
# Install PyFlink dependencies.
# update the PyFlink version if needed
pip install "apache-flink==1.12.1"
# Deactivate the Conda Python virtual environment.
conda deactivate
# Delete cached packages.
rm -rf venv/pkgs
# Package the prepared Conda Python virtual environment.
zip -r venv.zip venv
```

iii. Run the following command in the CMD command line:

```bash
docker run -it --rm -v $PWD:/build -w /build quay.io/pypa/manylinux2014_x86_64 ./b uild.sh
```

After you run this command, the system generates a file named **venv.zip**. This file is the virtual environment for **Python 3.7**. You can also modify the preceding script to install required third-party Python packages in the virtual environment.
2. Use the Python 3.7 virtual environment in a Python Job.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Artifacts** page, click **Upload Artifact** to upload the venv.zip file.

> **Note:** Realtime Compute for Apache Flink allows you to upload files up to 200 MB in size, while the size of a Python virtual environment usually exceeds this limit. Therefore, you must upload the file by using the OSS management console.

iii. On the **Deployments** page, click the name of the target Job. iv. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner. On the right side of the **Python Archives** parameter, select the venv.zip file. pment v. In the **Parameters** section, click **Edit** in the upper-right corner. On the right side of the
**Other Configuration** parameter, add the following configuration:

```
python.executable: venv.zip/venv/bin/python
```

vi. Click **Save**.

**Use third-party Python packages**

The following section describes how to use third-party Python packages in two scenarios: Use third-party Python packages that you can directly import If your third-party Python package is Zip Safe, you can use it in a Python job without installation. Perform the following steps: i. Download a third-party Python package that you can directly import. a. Open the PyPI page in your browser. b. In the search box, enter the name of the target third-party Python package, for example, **apache-flink 1.12.2**. c. In the search results, click the name of the target result. d. In the left-side navigation pane, click **Download files**. e. Click the package name that contains **cp37-cp37m-manylinux1** in the file name to download the package. ii. Log in to the Realtime Compute for Apache Flink console. iii. On the **Artifacts** page, click **Upload Artifacts** to upload the third-party Python package. iv. On the **Deployments** page, click the name of the target job. v. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner. vi. On the right side of the **Python Libraries** parameter, select the uploaded third-party Python package. vii. Click **Save**. Use third-party Python packages that require compilation If your third-party Python package is a compressed package in **tar.gz** format or a source code package downloaded from another location, and a **setup.py** file exists in the root directory of the compressed package, this type of third-party Python package usually requires compilation before use. You must first compile the third-party Python package in an environment compatible with Flink, and then call the third-party Python package in a Python job. We recommend that you use **quay.io/pypa/manylinux2014_x86_64** container image with **Python 3.7** to compile third-party Python packages. The packages compiled by using this container are compatible with most Linux environments. For more information about this container image, see manylinux.

> **Note:** The installation path of **Python 3.7** is **/opt/python/cp37-cp37m/bin/python3**.

The following section uses the **opencv-python-headless** third-party Python package as an example to describe how to compile and use this third-party Python package. i. Compile the third-party Python package. pment a. Prepare the **build.sh** script locally. The content of the script is as follows:

```bash
#!/bin/bash
set -e -x yum install -y zip PYBIN=/opt/python/cp37-cp37m/bin "${PYBIN}/pip" install --target __pypackages__ -r requirements.txt --no-deps cd __pypackages__ && zip -r deps.zip . && mv deps.zip ../ && cd .. rm -rf __pypackages__
```

b. Prepare the **requirements.txt** file locally. The content of the file is as follows:

```
opencv-python-headless
```

c. Run the following command in the CMD command line:

```bash
docker run -it --rm -v $PWD:/build -w /build quay.io/pypa/manylinux2014_x86_64 / bin/bash build.sh
```

After you run this command, the system generates a file named **deps.zip**. This file is the compiled third-party Python package. You can also modify **requirements.txt** to install other required third-party Python packages. In addition, the **requirements.txt** file can specify multiple Python dependencies. ii. Use the third-party Python package **deps.zip** in a Python job. a. Log in to the Realtime Compute for Apache Flink console. b. On the **Artifacts** page, click **Upload Artifact** to upload **deps.zip**.

> **Note:** Realtime Compute for Apache Flink allows you to upload files up to 200 MB in size, while the size of a Python virtual environment usually exceeds this limit. Therefore, you must upload the file by using the OSS management console.

c. On the **Deployments** page, click the name of the target job. d. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner. e. On the right side of the **Python Libraries** parameter, select **deps.zip**. f. Click **Save**.

**Use JAR packages**

If your Flink Python job uses Java classes, such as connectors or Java user-defined functions, you can specify the JAR packages of connectors or Java user-defined functions by using the following method.
1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Artifacts** page, click **Upload Artifact** to upload the JAR packages that you want to
use.
3. On the **Deployments** page, click the name of the target job.
4. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner.
pment
5. On the right side of the **Additional Dependencies** parameter, select the JAR packages
that you want to use.
6. In the **Parameters** section, click **Edit** in the upper-right corner. On the right side of the
**Other Configuration** parameter, add the following configuration:
If you need to depend on multiple JAR packages named **jar1.jar** and **jar2.jar**, configure the content as follows:

```
pipeline.classpaths: 'file:///flink/usrlib/jar1.jar;file:///flink/usrlib/jar2.jar'
```

7. Click **Save**.

**Use data files**

The following section describes how to use data files in two scenarios: Use the Python Archives option If you have a large number of data files, you can package them into a ZIP file and use them in a Python job by using the following procedure: i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Artifacts** page, click **Upload Artifact** to upload the required data file ZIP package. iii. On the **Deployments** page, click the name of the target job. iv. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner. v. On the right side of the **Python Archives** parameter, select the required data file ZIP package. vi. In a Python user-defined function, you can access the data file by using the following method. Assume that the name of the compressed package that contains the data file is
**mydata.zip**.

```python
def map():
    with open("mydata.zip/mydata/data.txt") as f:
    ...
```

Use the Additional dependencies option If you have a small number of data files, you can use them in a Python job by using the following procedure: i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Artifacts** page, click **Upload Artifact** to upload the required data file ZIP package. iii. On the **Deployments** page, click the name of the target job. iv. On the **Configuration** tab, find the **Basic** section and click **Edit** in the upper-right corner. v. On the right side of the **Additional dependencies** parameter, select the required data file. vi. In a Python user-defined function, you can access the data file by using the following method. Assume that the name of the data file is **data.txt**.

```python
def map():
    with open("/flink/usrlib/data.txt") as f:
    ...
```

## 5 Data connectors

### 5.1 Supported connectors

This document defines the table types and describes the connectors—both built-in and custom—available in Realtime Compute for Apache Flink.

**Table types**

In Realtime Compute for Apache Flink, you can define tables in Flink SQL or use the DataStream API to read from and write to external systems. Flink SQL supports the following table types:

**Source table**

A source table provides data for a Flink job and drives the computation. Its records trigger subsequent processing steps. It typically contains large-scale business data that requires transformation, with volumes of tens or hundreds of millions of records. It ingests data as a continuous stream from sources such as a message queue or a database change log. It contains key fields for joins and lookups, such as business keys (e.g., user IDs and order IDs).

**Sink table**

A sink table stores the results of a Flink job. It stores computed results, such as aggregated results and filtered data. You can write the output to external systems, such as databases, message queues, or files, for further analysis. It is the final destination for the job's output.

**Built-in connector**

The following sections describe each engine version and built-in connector. The console shows the most current information.

**VVR engine version: vvr-8.0.7-flink-1.17**

| Data source | Connector name | Source table | Sink table |
|---|---|---|---|
| AnalyticDB for MySQL 3.0 | adb3.0 | × | √ |
| AnalyticDB for PostgreSQL | adbpg | × | √ |
| blackhole | blackhole | × | √ |
| ClickHouse | clickhouse | × | √ |

| ApsaraDB for HBase | cloudhbase | × | √ |
|---|---|---|---|
| datagen | datagen Note A debugging connector that periodically generates random data matching the source table schema. | √ | × |
| DataHub | datahub | √ | √ |
| Elasticsearch Note Only versions 6.x and 7.x are supported. | elasticsearch | √ | √ |
| faker | faker | √ | × |
| Hologres | hologres | √ | √ |
| Hudi | hudi | √ | √ |
| Iceberg | iceberg | √ | √ |
| InfluxDB Note Only version 1.x is supported. | influxdb | × | √ |
| JDBC | jdbc | √ | √ |
| Kafka Note Only versions 0.11 and later are supported. | kafka | √ | √ |

| Lindorm | lindorm | × | √ |
|---|---|---|---|
| ApsaraDB for MongoDB | mongodb | √ | √ |
| MongoDB CDC Note Verified for specific versions. | mongodb-cdc | √ | × |
| RocketMQ | mq | √ | √ |
| MySQL Note Only versions 5.6, 5.7, and 8.0 are supported. | mysql Note Connects to ApsaraDB RDS for MySQL, PolarDB for MySQL, and self- managed MySQL databases. | √ | √ |
| MySQL CDC Note Only versions 5.6, 5.7, and 8.0 are supported. | mysql-cdc | √ | × |
| MaxCompute | odps | √ | √ |
| Tablestore | ots | × | √ |
| Paimon Note Only version 0.9 is supported. | paimon | √ | √ |

| PostgreSQL CDC Note Only versions 9.6 and later are supported. | postgres-cdc | √ | × |
|---|---|---|---|
| print | print Note A debugging connector that prints a specified number of input records. | × | √ |
| ApsaraDB RDS for MySQL | rds | × | √ |
| ApsaraDB for Redis | redis | × | √ |
| Log Service (SLS) | sls | √ | √ |
| StarRocks | starrocks | √ | √ |
| Tair | tair | × | √ |
| Upsert Kafka Note Only versions 0.11 and later are supported. | upsertkafka | √ | √ |

**VVR engine version: vvr-6.0.0-flink-1.15**

| Data source | Connector name | Source table support | Result table support |
|---|---|---|---|
| AnalyticDB for MySQL | adb3.0 | × | √ |
| AnalyticDB for PostgreSQL | adbpg | × | √ |
| blackhole | blackhole | × | √ |

| ClickHouse | clickhouse | × | √ |
|---|---|---|---|
| ApsaraDB for HBase | cloudhbase | × | √ |
| datagen | datagen Note A debugging connector that periodically generates random data matching the source table schema. | √ | × |
| DataHub | datahub | √ | √ |
| Elasticsearch Note Only versions 6.x and 7.x are supported. | elasticsearch | √ | √ |
| Faker | faker | √ | × |
| Hologres | hologres | √ | √ |
| Apache Hudi | hudi | √ | √ |
| Apache Iceberg | iceberg | √ | √ |
| InfluxDB Note Only version 1.x is supported. | influxdb | × | √ |
| JDBC | jdbc | √ | √ |
| ApsaraMQ for Kafka | kafka | √ | √ |

| Lindorm | lindorm | × | √ |
|---|---|---|---|
| ApsaraDB for MongoDB | mongodb | × | √ |
| ApsaraMQ for RocketMQ | mq | √ | √ |
| MySQL Note Only versions 5.6, 5.7, and 8.0 are supported. | mysql Note Supports connections to ApsaraDB RDS for MySQL, PolarDB for MySQL, and self- managed MySQL. | √ | √ |
| MaxCompute | odps | √ | √ |
| Tablestore | ots | √ | √ |
| Apache Paimon Note Only version 0.9 is supported. | paimon | √ | √ |
| PostgreSQL CDC Note Only versions 9.6 and later are supported. | postgres-cdc | √ | × |
| print | print Note A debugging connector that receives and prints a specified number of input records. | × | √ |
| ApsaraDB RDS for MySQL | rds | × | √ |

| ApsaraDB for Tair (Redis open- source edition) | redis | × | √ |
|---|---|---|---|
| Log Service | sls | √ | √ |
| StarRocks | starrocks | √ | √ |
| ApsaraDB for Tair (Tair Enterprise Edition) | tair | × | √ |
| Upsert Kafka Note Only versions 0.11 and later are supported. | upsertkafka | √ | √ |

**VVR engine version: vvr-4.0.18-flink-1.13**

| Data source | Connector name | As source | As sink |
|---|---|---|---|
| AnalyticDB for MySQL | adb3.0 | × | √ |
| AnalyticDB for PostgreSQL | adbpg | × | √ |
| blackhole | blackhole | × | √ |
| ClickHouse | clickhouse | × | √ |
| ApsaraDB for HBase | cloudhbase | × | √ |
| datagen | datagen Note A debugging connector that periodically generates random data matching the source table's schema. | √ | × |

| DataHub | datahub | √ | √ |
|---|---|---|---|
| elasticsearch Note Only versions 6.x and 7.x are supported. | elasticsearch | √ | √ |
| faker | faker | √ | × |
| Hologres | hologres | √ | √ |
| Hudi | hudi | √ | √ |
| Iceberg | iceberg | √ | √ |
| ApsaraDB for InfluxDB | influxdb | × | √ |
| ApsaraMQ for Kafka | kafka | √ | √ |
| Lindorm | lindorm | × | √ |
| ApsaraDB for MongoDB | mongodb | × | √ |
| ApsaraMQ for RocketMQ | mq | √ | √ |
| MySQL | mysql Note Supports connections to ApsaraDB RDS for MySQL, PolarDB for MySQL, and self- managed MySQL databases. | √ | √ |
| MySQL CDC | mysql-cdc | √ | × |
| MaxCompute | odps | √ | √ |

| Tablestore | ots | × | √ |
|---|---|---|---|
| PostgreSQL CDC | postgres-cdc | √ | × |
| print | print Note A debugging connector that prints a specified number of incoming records. | × | √ |
| random | random | √ | × |
| ApsaraDB RDS for MySQL | rds | × | √ |
| Tair | redis | × | √ |
| Log Service (SLS) | sls | √ | √ |
| Upsert Kafka | upsertkafka | √ | √ |

**Custom connectors**

When developing jobs with Flink SQL, you use SQL connectors to connect to source and sink tables. Flink supports many common connectors, but they cover only a small subset of the vast big data technology stack. To support a wider range of data sources, you can create and upload custom connectors. For detailed instructions, see Manage custom connectors.

### 5.2 Manage custom connectors

This topic describes how to manage custom connectors. For example, you can create, update, and delete a custom connector.

**Background information**

When you use Flink SQL to develop drafts, you must use SQL connectors to access your source tables, sink tables, and dimension tables. Flink supports multiple connector types that are commonly used on the cloud. However, these connector types are a small portion of the commonly used big data technology stacks. To support more connector types, Flink allows you to develop custom connectors. To use a custom connector, you must upload the JAR file of the connector. When you use custom connectors, take note of the following items: To allow Flink to identify and use your custom connector, you must develop your custom connector based on the connector standards that are defined by the Apache Flink community. Therefore, you must obtain the .meta file of the custom connector that you want to develop and declare the factory class. For more information about how to develop custom connectors, see User-defined Sources & Sinks. You can upload the JAR file of connectors of the same type only once. To prevent conflicts between JAR package dependencies, take note of the following items: Make sure that the version of the Flink image is the same as the Flink version in the Project Object Model (POM) dependencies. Do not upload JAR files at the runtime layer. This indicates that you need to add `<scope>provided</scope>` to the dependencies. Use the Shade plug-in to package third-party dependencies. For more information, see Apache Maven Shade plug-in.

**Create a custom connector**

1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces**page, find the workspace and namespace that you want to manage
and click **Console** in the **Actions** column.
3. In the left-side navigation pane, click **Connectors**.
4. On the **Connectors** tab, click **Custom Connector**.
5. Click **Create Custom Connector**. In the **Create Custom Connector** dialog box, perform
the following operations: i. **Upload a JAR package** Select the JAR file that you want to upload and click **Next**. In this example, the lindormconnector-1.0-SNAPSHOT.jar file is used. ii. **View the connector** In the **Create Custom Connector** step, configure the parameters.

| Parameter | Description |
|---|---|
| Connector | The connector name. |
| Lookup | Whether it can be used as a lookup table. Configure this parameter based on your business requirements. |
| Formats | Click the drop-down list to select a supported format. |
| Properties | Configure the attributes of the connector based on your business requirements. |

6. Click **Complete**.

**Update a custom connector**

1. In the custom connector list, find the connector that you want to update and click **Edit** in
the Actions column.
2. You can upload a new JAR package as needed. You can also select **Skip** to modify the
attributes of an existing connector.
3. Click **Complete**.

**Delete a custom connector**

If you no longer use a custom connector, perform the following steps to delete it:
1. In the custom connector list, find the connector that you want to delete and click **Delete** in
the Actions column.
2. In the message that appears, click **OK**.

### 5.3 Datagen connector

This topic describes how to use the Datagen connector.

**Background information**

The Datagen connector is used for debugging. The connector periodically generates random data of the type that corresponds to the Datagen source table. If you want to use test data to efficiently check the business logic during development or testing, you can use the Datagen connector to generate random data. The Datagen connector supports the computed column syntax to generate data in a flexible manner. The following table describes the capabilities supported by the Datagen connector.

| Item | Description |
|---|---|
| Table types | Source table |
| Running modes | Batch mode and streaming mode |
| Data formats | None |
| Monitoring metrics | None |
| API types | SQL |
| Data updates or deletion in a sink table | N/A (The connector supports only source tables) |

**Syntax**

```
CREATE TABLE datagen_source (
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'datagen'
```

);

**Parameters in the WITH clause**

| Paramete r | Description | Data type | Requi red | Defaul t value | Remarks |
|---|---|---|---|---|---|
| connector | The type of the source table. | String | Yes | None | Set the value to datagen . |
| rows-per- second | The rate at which random data is generated. | Long | No | 10000 (rows of data per second) | None. |
| number-of- rows | The total number of rows of data that can be generated. | Long | No | None | By default, an unbounded data source table is generated. If a field generator is a sequence generator, data generation for the source is complete, and a bounded table is generated after the sequence of a field is generated. |
| fields. <field>.kin d | The type of the generator that generates data for <field>. | String | No | random | Valid values: random: a random generator. sequence: a sequence generator. For more information about generators, see Generators. |
| fields. <field>.mi n | The minimum random value that can be generated. | Same as the data type of <field> | No | Minimu m value for the data type of <field> | This parameter takes effect when the fields. <field>.kind parameter is set to random. Only numeric data types are supported. |
| fields. <field>.ma x | The maximum random value that can be generated. | Same as the data type of <field> | No | Maximu m value for the data type of <field> | This parameter takes effect when the fields. <field>.kind parameter is set to random. Only numeric data types are supported. |

| fields. <field>.ma x-past | The maximum past time relative to the current timestamp of the on-premises machine when a random timestamp is generated. | Duration | No | 0 | Only the timestamp type is supported. |
|---|---|---|---|---|---|
| fields. <field>.len gth | The length of the random string that is generated or the capacity of a set of data that is generated. | Integer | No | 100 | The following data types are supported: char varchar binary varbinary string array map multiset |
| fields. <field>.sta rt | The start value of the sequence generator. | Same as the data type of <field> | No | None | This parameter takes effect when the fields. <field>.kind parameter is set to sequence. |
| fields. <field>.en d | The end value of the sequence generator. | Same as the data type of <field> | No | None | This parameter takes effect when the fields. <field>.kind parameter is set to sequence. |

> **Note:** Replace <field> in the parameter with the name of the field that you defined in the DDL statement.

**Generators**

The Datagen connector can use one of the following types of generators to generate random data: Random generator: generates random values. You can specify the maximum and minimum values for data that is randomly generated. Sequence generator: generates ordered values within a specific range. When the generated sequence reaches the end value, the data generation process ends. Therefore, if a sequence generator is used, a bounded table is generated. You can specify the start and end values of the sequence. The following table describes the generator types that are supported for each data type.

| Type | Supported generator | Description |
|---|---|---|
| BOOLEAN | random | None. |
| CHAR | random/sequence | None. |
| VARCHAR | random/sequence | None. |
| BINARY | random/sequence | None. |
| VARBINARY | random/sequence | None. |
| STRING | random/sequence | None. |
| DECIMAL | random/sequence | None. |
| TINYINT | random/sequence | None. |
| SMALLINT | random/sequence | None. |
| INT | random/sequence | None. |
| BIGINT | random/sequence | None. |
| FLOAT | random/sequence | None. |
| DOUBLE | random/sequence | None. |
| DATE | random | Uses the current date of the on- premises machine. |
| TIME | random | Uses the current time of the on- premises machine. |
| TIMESTAMP | random | Generates values within the maximum past time range relative to the current timestamp of the on-premises machine. |

| TIMESTAMP LTZ _ | random | Generates values within the maximum past time range relative to the current timestamp of the on-premises machine. |
|---|---|---|
| ROW | random | Generates random subfields. |
| ARRAY | random | Generates random elements. |
| MAP | random | Generates random pairs of (key,value). |
| MULTISET | random | Generates random elements. |

**Sample code**

In most cases, the Datagen connector is used together with the LIKE clause to simulate a table. Sample code:

```
CREATE TABLE datagen_source (
 id INT,
 score INT
) WITH (
 'connector' = 'datagen',
 'fields.id.kind'='sequence',
 'fields.id.start'='1',
 'fields.id.end'='50',
 'fields.score.kind'='random',
 'fields.score.min'='70',
 'fields.score.max'='100'
```

);

### 5.4 Blackhole connector

This topic describes how to use the Blackhole connector.

**Background information**

The Blackhole connector is used for deployment debugging and can receive all input data records. If an error is returned when you create a sink table that uses another connector type, but you cannot determine whether the error is caused by a system error or an invalid configuration of a parameter in the WITH clause of the sink table, you can change the value of the **connector** parameter to blackhole and click **Validate** in the upper-right corner of the Drafts tab. If no error is returned, the system is normal. You must check the configuration of parameters in the WITH clause. The Blackhole connector can be used in the following debugging scenarios: Check whether performance consumption occurs when a deployment is in the RUNNING state. This helps reduce the impact on performance consumption when you insert data into a table. Check whether the output data of user-defined functions (UDFs) is valid. You can view the output data of UDFs by using the Blackhole connector. If you use the Blackhole connector, you do not need to use a physical table to check whether the output data of UDFs is valid. The following table describes the capabilities supported by the Blackhole connector.

| Item | Description |
|---|---|
| Table types | Sink table |
| Running modes | Batch mode and streaming mode |
| Data formats | None |
| Monitoring metrics | None |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Syntax**

```
CREATE TABLE blackhole_sink(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
```

); You can also create a Blackhole sink table by using the `LIKE` clause based on the definition of an existing table. Sample statement:

```
CREATE TABLE blackhole_sink WITH ('connector' = 'blackhole') LIKE table_source (EXCLUDING ALL);
```

**Parameters in the WITH clause**

| Paramete r | Description | Data type | Required | Default value | Remarks |
|---|---|---|---|---|---|
| connector | The type of the sink table. | String | Yes | None | Set the value to blackhole . |

**Sample code**

```
CREATE TEMPORARY TABLE table_source(
  name VARCHAR,
  score BIGINT
) WITH (
  ...
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT * from table_source;
```

### 5.5 Print connector

This topic describes how to use the Print connector.

**Background information**

The Print connector is used to write every row to the system output or system error stream. It is designed for debugging. If you want to view the intermediate results or the output of an SQL statement, you can add **'connector'='print'** to the WITH clause of the SQL statement and click **Run**. Then, you can view the output in JobManager logs. The Print connector can be used to check whether the messages sent to other result tables meet the expectations. The following table describes the capabilities supported by the Print connector.

| Item | Description |
|---|---|
| Table types | Sink table |
| Running modes | Batch mode and streaming mode |
| Data formats | None |
| Monitoring metrics | None |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

If you want to view the output of a Print sink table, make sure that the log level is set to INFO. A maximum of 2,000 log entries can be displayed in Taskmanager.out. If you want to check for dirty data or specific data, we recommend that you specify conditions in the WHERE clause to perform the print operation. The print operation allows you to effectively check required data, even when the number of data records displayed is limited.

**Syntax**

```
CREATE TABLE print_table (
  a INT,
  b varchar
) WITH (
  'connector'='print',
  'logger'='true'
```

); You can also create a Print table by using the `LIKE` clause based on an existing table schema. Sample statements:

```
CREATE TABLE print_table WITH ('connector' = 'print') LIKE table_source (EXCLUDING ALL)
```

**Parameters in the WITH clause**

| Paramete r | Description | Data type | Required | Defaul t value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | Set the value to print. |
| logger | Specifies whether to display the data result in the console. | Boolean | No | false | Valid values: false: The data result is not displayed in the console. This is the default value. true: The data result is displayed in the console. |
| print- identifier | The identifier of the data sink. | String | No | None | The log information is retrieved by using the identifier of the data result. |

| sink.parall elism | The parallelism of the sink table. | Int | No | A value that is the same as the upstrea m parallel ism | None. |
|---|---|---|---|---|---|

**Sample code**

```
CREATE TABLE table_source(
  name VARCHAR,
  score BIGINT
) WITH (
  ...
```

);

```
CREATE TABLE print_sink(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'print'
```

);

```
INSERT INTO print_sink SELECT * from table_source;
```

### 5.6 Faker connector

This topic describes how to use the Faker connector.

**Background information**

The Faker connector is a built-in connector of Realtime Compute for Apache Flink. The connector generates test data based on Java Faker expressions that are provided for each field in a table. If you want to use test data to verify the business logic during deployment development or testing, we recommend that you use the Faker connector. The following table describes the capabilities supported by the Faker connector.

| Item | Description |
|---|---|
| Table types | Source table |
| Running modes | Batch mode and streaming mode |

| Data formats | N/A |
|---|---|
| Monitoring metrics | None |
| API types | SQL |
| Data updates or deletion in a sink table | N/A (The connector supports only source tables) |

**Limits**

The Faker connector supports only the following data types: CHAR(n), VARCHAR(n), STRING, TINYINT, SMALLINT, INT, BIGINT, FLOAT, DOUBLE, DECIMAL, BOOLEAN, TIMESTAMP, ARRAY, MAP, MULTISET, and ROW.

**Syntax**

```
CREATE TABLE faker_source (
  `name` STRING,
  `age` INT
) WITH (
  'connector' = 'faker',
  'fields.name.expression' = '#{superhero.name}',
  'fields.age.expression' = '#{number.numberBetween ''0'',''1000''}'
```

);

**Parameters in the WITH clause**

| Parameter | Description | Data type | Require d | Defaul t value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | The value of the parameter is faker. |
| fields. <field>.expressio n | The Java Faker expression that generates the value of the field. | String | Yes | None | For more information, see the Field expression section of this topic. |
| fields.<field>.null- rate | The rate at which the value in this field is null. | Float | No | 0.0 | None |
| fields. <field>.length | The length of the field of the ARRAY, MAP, or MULTISET data type. | Integer | No | 1 | None |

| number-of-rows | The number of rows of data that is generated. | Integer | No | -1 | If you specify this parameter, the source table is bounded. If you do not specify this parameter, the source table is unbounded. |
|---|---|---|---|---|---|
| rows-per-second | The rate at which random data is generated. | Integer | No | 10000 | Default value: 10000. Unit: records per second. |

**Sample code**

```
CREATE TEMPORARY TABLE heros_source (
  `character_id` INT,
  `name` STRING,
  `power` STRING,
  `phone_number` STRING,
  `age` INT,
  `address` STRING,
  `score` MAP<STRING, INT>,
  `work_locations` ARRAY<STRING>,
  `spells` MULTISET<STRING>,
  `house-points` ROW<`house` STRING, `points` INT>,
  `user_ip` STRING,
  `request_url` STRING,
  `status_code` STRING,
  `sys_time` AS PROCTIME(),
  `event_time` TIMESTAMP(3),
  WATERMARK FOR event_time AS event_time
) WITH (
  'connector' = 'faker',
  'fields.character_id.expression' = '#{number.numberBetween ''0'',''10000''}',
  'fields.name.expression' = '#{superhero.name}',
  'fields.power.expression' = '#{superhero.power}',
  'fields.power.null-rate' = '0.05',
  'fields.phone_number.expression' = '#{PhoneNumber.cellPhone}',
  'fields.age.expression' = '#{number.numberBetween ''0'',''1000''}',
  'fields.address.expression' ='#{harry_potter.location}',
  'fields.score.key.expression' = '#{harry_potter.character}',
  'fields.score.value.expression' = '#{number.numberBetween ''10'',''100''}',
  'fields.score.length' = '2',
  'fields.work_locations.expression' = '#{harry_potter.location}',
  'fields.work_locations.length' = '2',
  'fields.spells.expression' = '#{harry_potter.spell}',
  'fields.spells.length' = '2',
  'fields.house-points.house.expression' = '#{harry_potter.house}',
  'fields.house-points.points.expression' = '#{number.numberBetween ''10'',''100''}',
  'fields.user_ip.expression' = '#{Internet.publicIpV4Address}',
  'fields.request_url.expression' = '#{Internet.url}',
  'fields.status_code.expression' = '#{regexify ''(200|201|204|400|401|403|301){1}''}',
'fieldseventtimeexpression'='#{Datefuture''365''''DAYS''}'
```

```
  fields.event_time.expression = #{Date.future
```

`,`

```
DAYS
```

`}``,`

```
  'number-of-rows' = '30'
```

);

```
CREATE TEMPORARY table blackhole_sink(
  `character_id` INT,
  `name` STRING,
  `power` STRING,
  `phone_number` STRING,
  `age` INT,
  `address` STRING,
  `score` MAP<STRING, INT>,
  `work_locations` ARRAY<STRING>,
  `spells` MULTISET<STRING>,
  `house-points` ROW<`house` STRING, `points` INT>,
  `user_ip` STRING,
  `request_url` STRING,
  `status_code` STRING,
  `sys_time` TIMESTAMP,
  `event_time` TIMESTAMP(3)
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT * FROM heros_source;
```

**Field expression**

Procedure When you use the Faker connector, you must define an expression in the WITH clause for each field in the DDL statement. The expression is in the **'fields.<field>.expression' =**
**'#{className.methodName ''parameter'', ...}'** format. The following table describes
the fields in the expression.

| Field | Description |
|---|---|
| field | The name of a field in the DDL statement. |
| className | The name of a Faker class. Java Faker provides around 80 Faker classes to generate field expressions. You can select the classes based on your business requirements. Note Faker class names are not case-sensitive. |

| methodNam e | The name of a method. Note Method names are not case-sensitive. |
|---|---|
| parameter | The input parameters of a method. Note Each input parameter of a method must be enclosed in single quotation marks ('). Separate multiple input parameters with commas (,). |

Examples In this example, the **'fields.age.expression' = '#{number.numberBetween**
**''0'',''1000''}'** expression for the age field in Syntax is generated based on the Java Faker
API reference by performing the following steps: i. Find the Number class in the Java Faker API reference. ii. Find the numberBetween method in the Number class and view the method description. The numberBetween method specifies the numbers between which the return value falls. iii. Obtain the SQL expression **'fields.age.expression' = '#{number.numberBetween**
**''0'',''1000''}'** for the age field based on the Number class and the values 0 and 1000
that are specified by the numberBetween method. This expression indicates that the generated value of the age field is in the range of 0 to 1000.

### 5.7 Apache Iceberg connector

This topic describes how to use the Apache Iceberg connector.

**Background information**

Apache Iceberg is an open table format for data lakes. You can use Apache Iceberg to quickly build your own data lake storage service on Hadoop Distributed File System (HDFS) or Alibaba Cloud Object Storage Service (OSS). Then, you can use a computing engine of the open source big data ecosystem, such as Apache Flink, Apache Spark, Apache Hive, or Apache Presto, to analyze data in your data lake.

| Item | Description |
|---|---|
| Table types | Source table and sink table |
| Running modes | Batch mode and streaming mode |
| Data formats | Not supported |

| Monitoring metrics | Not supported |
|---|---|
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Features**

Apache Iceberg provides the following core capabilities: Builds a low-cost lightweight data lake storage service based on HDFS or OSS. Provides comprehensive atomicity, consistency, isolation, durability (ACID) semantics. Supports historical version backtracking. Supports efficient data filtering. Supports schema evolution. Supports partition evolution. Can be used together with self-managed Hive Metastores.

> **Note:** You can use the efficient fault tolerance and stream processing capabilities of Flink to import a large amount of behavioral data in logs into an Apache Iceberg data lake in real time. Then, you can use Flink or another analytics engine to extract the value of your data.

**Limits**

Apache Iceberg must be used together with a Data Lake Formation (DLF) catalog. DLF Catalog supports Apache Iceberg v1 and v2 table formats.

> **Note:** Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.7 or later supports the Apache Iceberg table format of version 2.

In streaming read mode, only Apache Iceberg tables in which data is written in Append Only mode can be used as source tables.

**Syntax**

```
CREATE TABLE iceberg_table (
  id    BIGINT,
  data  STRING
  PRIMARY KEY(`id`) NOT ENFORCED
```

`)`

```
 PARTITIONED BY (data)
 WITH (
 'connector' = 'iceberg',
  ...
```

);

**Parameters in the WITH clause**

**Common parameters (source table)**

| Parameter | Descripti on |   | Data type | Requi red | Def ault val ue | Remarks |   |   |
|---|---|---|---|---|---|---|---|---|
| connector | The type of the source table. |   | Strin g | Yes | Non e | Set the value to iceberg . |   |   |
| catalog- name | The name of the catalog. |   | Strin g | Yes | Non e | Enter a custom name. |   |   |
| catalog- database | The database name. |   | Strin g | Yes | defa ult | Set the value to the name of the database that is created on DLF. Example: dlf db. _ |   |   |
| io-impl | The name of the implement ation class in the distributed file system. |   | Strin | Yes | Non | Set the value to org.apache.iceberg.aliyun.oss.OSSFil eIO . |   |   |
|   |   |   |   |   |   |   | org.apache.iceberg.aliyun.oss.OSSFil |   |
|   |   | in the distributed | g |   | e | eIO |   |   |
| oss.endpoint | The endpoint of your OSS bucket. |   | Strin g | No | Non e | We recommend that you set oss.endpoint to a VPC endpoint of OSS. For example, if you select the China (Hangzhou) region, set oss.endpoint to oss-cn-hangzhou-internal.aliyuncs.com. |   |   |

| access.ke y.id: VVR 8.0.6 and earlier access- key-id: VVR 8.0.7 and later | The AccessKey ID of your Apsara Stack tenant account. | Strin g | Yes | Non e | None. |
|---|---|---|---|---|---|
| access.ke y.secret: VVR 8.0.6 and earlier access- key- secret: VVR 8.0.7 and later | The AccessKey secret of your Apsara Stack tenant account. | Strin g | Yes | Non e |   |
| catalog-impl | The class name of the catalog. | Strin g | Yes | Non e | Set the value to org.apache.iceberg.aliyun.dlf.DlfCatalog. |
| warehouse | The OSS directory in which table data is stored. | Strin g | Yes | Non e | None. |
| dlf.catalog-id | The ID of your Apsara Stack tenant account. | Strin g | Yes | Non e | None. |
| dlf.endpoint | The endpoint of DLF. | Strin g | Yes | Non e | We recommend that you set dlf.endpoint to the VPC endpoint of DLF. For example, if you select the China (Hangzhou) region, set the dlf.endpoint parameter to dlf- vpc.cn-hangzhou.aliyuncs.com. |
| dlf.region-id | The name of the region in which the DLF service is activated. | Strin g | Yes | Non e | Make sure that the region you selected matches the endpoint you selected for dlf.endpoint. |

| uri | The Thrift URI of the Hive Metastore. | Strin g | This param eter is require d only when a Hive catalo g is used. | Non e | Specify this parameter when you use Apache Iceberg together with a self- managed Hive Metastore. |
|---|---|---|---|---|---|

**Sink table-specific parameters**

| Paramet er | Descri ption | Data type | Req uire d | Defaul t value | Remarks |
|---|---|---|---|---|---|
| write.oper ation | The write operati on mode. | Strin g | No | upsert | upsert: Data is updated. This is the default value. insert: Data is written to the table in append mode. bulk insert: A specific amount of data is _ written at a time, and existing data is not updated. |
| hive sync. _ enable | Specifi es whethe r to enable the synchr onizati on of metada ta to Hive. | boole an | No | false | Valid values: true: The synchronization of metadata to Hive is enabled. false: The synchronization of metadata to Hive is disabled. This is the default value. |
| hive sync. _ mode | The Hive data synchr onizati on mode. | Strin g | No | hms | hms: If you use a Hive metastore or DLF catalog, retain the default value. This is the default value. jdbc: If the Java Database Connectivity (JDBC) catalog is used, set this value to jdbc. |

| hive sync. _ db | The name of the Hive databa se to which data is synchr onized. | Strin g | No | Databa se name of the current table in the catalog | None. |
|---|---|---|---|---|---|
| hive sync. _ table | The name of the Hive table to which data is synchr onized. | Strin g | No | Name of the current table | None. |
| dlf.catalo g.region | The name of the region in which the DLF service is activat ed. | Strin g | No | None | Note The dlf.catalog.region parameter takes effect only when the hive sync.mode parameter is set to _ hms . Make sure that the value of this parameter matches the endpoint specified by the dlf.catalog.endpoint parameter. |
| dlf.catalo g.endpoin t | The endpoi nt of DLF. | Strin g | No | None | Note The dlf.catalog.endpoint parameter takes effect only when the hive sync.mode parameter is _ set to hms. We recommend that you set the dlf.catalog.endpoint parameter to a VPC endpoint of DLF. For example, if you select the China (Hangzhou) region, set the dlf.catalog.endpoint parameter to dlf-vpc.cn- hangzhou.aliyuncs.com. |

**Data type mappings**

| Data type of Apache Iceberg | Data type of Realtime Compute for Apache Flink |
|---|---|

| BOOLEAN | BOOLEAN |
|---|---|
| INT | INT |
| LONG | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(P,S) | DECIMAL(P,S) |
| DATE | DATE |
| TIME | TIME Note Apache Iceberg timestamps are accurate to the microsecond, and timestamps of Realtime Compute for Apache Flink are accurate to the millisecond. When you use Realtime Compute for Apache Flink to read Apache Iceberg data, the time precision is aligned to milliseconds. |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP LTZ _ |
| STRING | STRING |
| FIXED(L) | BYTES |
| BINARY | VARBINARY |
| STRUCT<...> | ROW |
| LIST<E> | LIST |
| MAP<K,V> | MAP |

**Sample code**

Confirm that an OSS bucket and a DLF database are created.

> **Note:** When you specify a **directory** for your DLF database, we recommend that you enter a directory in the ${warehouse}/${database_name}.db format. For example, if the value of the warehouse parameter is oss://iceberg-test/warehouse and the value of the database_name parameter is dlf_db, set the OSS directory of the dlf_db database to oss://iceberg-test/warehouse/dlf_db.db.

**Sample code for an Apache Iceberg sink table**

This example shows how to use the Datagen connector to randomly generate streaming data and write the data to an Apache Iceberg sink table.

```
CREATE TEMPORARY TABLE datagen(
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE dlf_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
```

);

```
INSERT INTO dlf_iceberg SELECT * FROM datagen;
```

**Sample code for an Apache Iceberg source table**

Specify a Hive catalog and a self-managed Hive Metastore. Make sure that network communication is established between Flink and the Hive Metastore cluster. Data is stored in the `oss://<bucket>/<path>/<database-` `name>/flink_table` directory.

```
CREATE TEMOPORY TABLE flink_table (
  id   BIGINT,
  data STRING
) WITH (
  'connector'='iceberg',
  'catalog-name'='<yourCatalogName>',
  'catalog-database'='<yourDatabaseName>',
  'uri'='thrift://<ip>:<post>',
  'warehouse'='oss://<bucket>/<path>',
  'io-impl'='org.apache.iceberg.aliyun.oss.OSSFileIO',
  'access-key-id'='<aliyun ak>',
  'access-key-secret'='<aliyun sk>',
  'oss.endpoint'='<yourOSSEndpoint>'
```

); Use a DLF catalog to write data from the Iceberg source table to the Iceberg sink table.

```
CREATE TEMPORARY TABLE src_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
```

);

```
CREATE TEMPORARY TABLE dst_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '${secret_values.ak_id}',
  'access.key.secret' = '${secret_values.ak_secret}',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
```

);

```
BEGIN STATEMENT SET; INSERT INTO src_iceberg VALUES (1, 'AAA'), (2, 'BBB'), (3, 'CCC'), (4, 'DDD'), (5, 'E EE'); INSERT INTO dst_iceberg SELECT * FROM src_iceberg; END;
```

### 5.8 Postgres CDC connector

The PostgreSQL change data capture (CDC) connector is used to read existing data and changed data from a PostgreSQL database. The process is divided into two phases based on the data type: full scan phase and incremental capture phase. If a failure occurs, the connector recovers data in an exactly-once manner to ensure that no data is duplicated or lost. This topic describes how to use the PostgreSQL CDC connector.

**Background information**

The following table describes the capabilities of the PostgreSQL CDC connector.

| Item | Description |
|---|---|
| Table types | Source table Note You can use the Java Database Connectivity (JDBC) connector to create a sink or dimension table. |
| Running modes | Streaming mode |
| Data formats | None |
| Monitoring metrics | currentFetchEventTimeLag: the interval between data generation and data fetching to the source operator. currentEmitEventTimeLag: the interval between data generation and data departure from the source operator. sourceIdleTime: the duration from the most recent data generation time in the CDC source to the current time. Note The currentFetchEventTimeLag and currentEmitEventTimeLag metrics are valid only in the incremental capture phase. The metric values are 0 in the full scan phase. |
| API types | SQL |
| Data updates or deletion in a sink table | N/A (The connector supports only source tables) |

**Features**

The PostgreSQL CDC connector supports the incremental snapshot reading feature in Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.6 or later. When the connector starts running, it first initiates the full scan phase to read the snapshot of a PostgreSQL database. After the full scan is completed, the connector automatically switches to the incremental capture phase to read write-ahead log (WAL) files of the database. If a failure occurs, the connector recovers data in an exactly-once manner to prevent data duplication or loss. In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the connector supports the incremental snapshot reading feature. You can use the connector to create a source table, which provides the following advantages: Supports reading full and incremental data to facilitate unified stream and batch processing. Supports full data reading in multiple subtasks at the same time. This way, data can be read in a more efficient manner. Seamlessly switches between full and incremental data reading and supports automatic scale-in operations. This reduces the computing resources that are consumed. Supports data resumption in the full scan phase to enhance stability. Supports lock-free reading in the full scan phase to ensure normal business operation.

**Prerequisites**

The PostgreSQL CDC connector uses the logical replication feature of PostgreSQL to capture data changes. To use the connector, make sure that the following conditions are met: The wal_level parameter is set to logical, which specifies that the information required for logical decoding is included in WAL files. The REPLICA IDENTITY parameter of the subscribed table is set to FULL by using the `ALTER` TABLE schema.table REPLICA IDENTITY FULL; command. This ensures data consistency.

> **Note:** REPLICA IDENTITY is a PostgreSQL-specific table-level parameter. The parameter specifies whether to include the previous values of the involved table columns in the INSERT and UPDATE events that are generated by the logical decoding plug-in. For more information, see REPLICA IDENTITY.

The max_wal_senders and max_replication_slots parameters are set to a value greater than the number of occupied replication slots in the monitored database and the number of required replication slots for the Flink deployment. Your database account is assigned a superuser role or granted the LOGIN and REPLICATION permissions. Your database account is also granted the SELECT permission on the subscribed table for full data query.

> **Note:** Configurations related to the preceding conditions may be different in ApsaraDB RDS for PostgreSQL, Amazon RDS for PostgreSQL, and self-managed PostgreSQL databases.

**Limits**

The incremental snapshot reading feature of the PostgreSQL CDC connector requires Realtime Compute for Apache Flink that uses VVR 8.0.6 or later.

**You must manually manage replication slots to avoid disk space waste.**

Replication slots are used to retain WAL segments. If a Flink job is restarted, the job can resume from the most recent checkpoint based on the WAL segments, thereby preventing data loss. If you confirm that a Flink job no longer requires a restart, we recommend that you manually delete the corresponding replication slots to free up the occupied resources. In addition, if the progress marker of a replication slot remains stagnant for a long period of time, PostgreSQL retains the WAL records after the marked position. The retention of unnecessary WAL records may result in a significant increase in disk space usage.

**If you enable the incremental snapshot reading feature of the PostgreSQL CDC**

**connector, you must enable checkpointing for the connector and define a primary**

**key in the source table. When the incremental snapshot reading feature is**

**enabled, multiple temporary replication slots are created to achieve parallel**

**reading in the full scan phase.**

If the incremental snapshot reading feature is disabled, the PostgreSQL CDC connector reads data from the source at 1 parallelism. In this case, only one global slot is required. The number of required replication slots in the full scan phase is equal to `Number of` sources × Parallelism + 1 . After the PostgreSQL CDC connector switches from the full scan phase to the incremental capture phase, the system automatically removes temporary replication slots and retains only one replication slot. If you want to limit the number of replication slots used in the full scan phase, you can reduce the parallelism. Take note that this also reduces the reading speed. If the downstream operator or storage supports idempotence, you can use the following configuration to skip log reading in the full scan phase: `scan.incremental.snapshot.backfill.skip = true` . In this case, the connector provides only at-least-once guarantees. If you use SQL to perform operations such as aggregation and association, we recommend that you do not skip log reading in the full scan phase. If you disable the incremental snapshot reading feature, the PostgreSQL CDC connector cannot perform checkpoints during the full scan phase. If the feature is disabled and checkpoints are triggered during the full scan phase, the deployment may perform a failover due to a checkpoint timeout. To prevent this issue, we recommend that you add the following configurations to the **Additional Configuration** section:

```
execution.checkpointing.interval: 10min execution.checkpointing.tolerable-failed-checkpoints: 100 restart-strategy: fixed-delay restart-strategy.fixed-delay.attempts: 2147483647
```

The following table describes the parameters in the preceding configurations.

| Parameter | Description | Remarks |
|---|---|---|
| execution.check pointing.interval | The interval at which checkpoints are triggered. | Data type: DURATION. Example: 10min and 30s. |
| execution.check pointing.tolerabl e-failed- checkpoints | The maximum number of checkpoint failures that are allowed. | The product of the value of this parameter and the checkpoint scheduling interval is the maximum duration of the full scan phase. Note If the scanned table is excessively large, we recommend that you specify a sufficiently large value. |
| restart-strategy | The restart policy. | Valid values: fixed-delay: The deployment is restarted at a fixed delay. failure-rate: The deployment is restarted based on the failure rate. exponential-delay: The deployment is restarted with an exponential delay. For more information, see Restart Strategies. |

| restart- strategy.fixed- delay.attempts | The maximum number of restart attempts when you set the restart- strategy parameter to fixed-delay. | None. |
|---|---|---|

**Syntax**

```
CREATE TABLE postgrescdc_source (
  shipment_id INT,
  order_id INT,
  origin STRING,
  destination STRING,
  is_arrived BOOLEAN
) WITH (
  'connector' = 'postgres-cdc',
  'hostname' = '<yourHostname>',
  'port' = '5432',
  'username' = '<yourUserName>',
  'password' = '<yourPassWord>',
  'database-name' = '<yourDatabaseName>',
  'schema-name' = '<yourSchemaName>',
  'table-name' = '<yourTableName>'
```

);

**Parameters in the WITH clause**

| Parame ter | Description | Dat a typ e | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | STRI NG | Yes | None | Set the value to postgres-cdc . |
| hostna me | The IP address or hostname of the PostgreSQL database. | STRI NG | Yes | None | None. |
| userna me | The username that is used to access the PostgreSQL database service. | STRI NG | Yes | None | None. |

| passwor d | The password that is used to access the PostgreSQL database service. | STRI NG | Yes | None | None. |
|---|---|---|---|---|---|
| databas e-name | Set the value of this parameter to the name of a PostgreSQL database. | STRI NG | Yes | None | If you want to read data from multiple databases, set this parameter to a regular expression. |
| schema -name | The schema name of the PostgreSQL database. | STRI NG | Yes | None | If you want to read data from multiple schemas, set this parameter to a regular expression. |
| table- name | The name of the table in the PostgreSQL database. | STRI NG | Yes | None | If you want to read data from multiple tables, set this parameter to a regular expression. |
| port | The port that is used to access the PostgreSQL database service. | INTE GER | No | 5432 | None. |

|   | decodin g.plugin .name | The name of the logical decoding plug-in that is installed in the PostgreSQL database service. |   | STRI NG | No | deco derb ufs | The plug-in name is determined based on the plug-in that is installed in the PostgreSQL database service. Valid values: decoderbufs (default value) pgoutput wal2json wal2json rds _ wal2json streaming _ wal2json rds streaming _ _ |   |
|---|---|---|---|---|---|---|---|---|
|   | slot.na me | The name of the logical decoding slot. |   | STRI NG | Yes (app lies to VVR | flink (appli es to VVR versi ons earlie r than 8.0.1) | We recommend that you configure the slot.name parameter for each table to prevent the following error: PSQLException: |   |
|   |   |   |   |   |   |   |   | PSQLException: |
|   |   |   |   |   | 8.0. 1 | or N/A | ERROR: replication slot "debezium" is |   |
|   |   |   |   |   | and | (appli | active for PID 974 |   |
|   |   |   |   |   | later ) | es to VVR 8.0.1 and later) |   |   |
|   | debeziu m.* | The Debezium properties. |   | STRI |   |   | This parameter is used to implement fine- grained control over the Debezium client. For example, 'debezium.snapshot.mode' = 'never' specifies that the connector does not generate snapshots. For more information, see Connector properties. |   |
|   |   |   | s. | NG | No | None | 'never' |   |
|   | scan.inc rement al.snaps hot.ena bled | Specifies whether to enable the incremental snapshot reading feature. |   | BOO LEA N | No | false | Valid values: false (default): disables the incremental snapshot reading feature. true: enables the incremental snapshot reading feature. Note This experimental feature is supported only in Realtime Compute for Apache Flink that uses VVR 8.0.6 or later. |   |

| 'debezium.snapshot.mode' = |   |
|---|---|

| scan.sta rtup.mo de | The startup mode that is used to consume data. | STRI NG | No | initial | Valid values: initial (default): performs a full scan on the monitored database during the first startup and then continues to read the most recent WAL files. latest-offset: skips the full scan on the monitored database during the first startup and reads from the end of the WAL files. In this case, only the most recent changes after the connector is started are recorded. snapshot: performs a full scan on the monitored database, reads the generated WAL files during the full scan phase, and then stops reading. |   |
|---|---|---|---|---|---|---|
| changel og- mode | The changelog mode that is used to encode streaming changes. | Strin g | No | all | Valid values: ALL: encodes all types of changes, including INSERT, DELETE, UPDATE BEFORE, and _ UPDATE AFTER changes. _ UPSERT: encodes only upsert-type changes, including INSERT, DELETE, and UPDATE AFTER changes. _ |   |
| heartbe at.interv al.ms | The interval at which heartbeat packets are sent. | Dur atio n | No | 30s | The default value indicates that the cache is never refreshed. Unit: milliseconds. The PostgreSQL CDC connector sends heartbeat packets to the monitored database to synchronize the progress offset of replication slots. If table changes are not frequent, configure this parameter to remove unnecessary WAL files at the earliest opportunity. |   |
| scan.inc rement al.snaps hot.chu nk.key- column | The column that is used to split tables into chunks in the full scan phase. | STRI NG | No | None | By default, the first column of the primary key is used. |   |
| scan.inc rement al.close- idle- reader.e nabled | Specifies whether to close the | Bool |   |   | This parameter is valid only if you set the execution.checkpointing.checkpoints- after-tasks-finish.enabled parameter to true. |   |
|   |   |   |   |   |   | execution.checkpointing.checkpoints- |
|   | idle readers at the end of | ean | No | false | after-tasks-finish.enabled |   |
|   | the full scan phase. |   |   |   |   |   |

| scan.inc rement al.snaps hot.bac kfill.skip | Specifies whether to skip log reading in the full scan phase. | Bool ean | No | false | Valid values: true: skips log reading. In this case, the connector reads logs from the low watermark in the incremental capture phase. If the downstream operator or storage supports idempotence, we recommend that you set this parameter to true. This reduces the number of required replication slots and provides at-least-one instead of exactly-once guarantees. false: does not skip log reading. In this case, the connector reads the logs between the low watermark and high watermark to ensure consistency. If you use SQL to perform operations such as aggregation and association, we recommend that you set this parameter to false. |
|---|---|---|---|---|---|

**Data type mappings**

The following table describes the mapping between data types in Postgres CDC and Realtime Compute for Apache Flink.

| Data type of Postgres CDC | Data type of Realtime Compute for Apache Flink |
|---|---|
| SMALLINT | SMALLINT |
| INT2 |   |
| SMALLSERIAL |   |
| SERIAL2 |   |
| INTEGER | INT |
| SERIAL |   |
| BIGINT | BIGINT |
| BIGSERIAL |   |
| REAL | FLOAT |
| 08 | > Document Version: 2026070 |

|   | Realtime Compute for Apache Fl nk (Compute-Storage Separation Edition) User Guide·Data connec or |
|---|---|
| FLOAT4 |   |
| FLOAT8 | DOUBLE |
| DOUBLE PRECISION |   |
| NUMERIC(p, s) | DECIMAL(p, s) |
| DECIMAL(p, s) |   |
| BOOLEAN | BOOLEAN |
| DATE | DATE |
| TIME [(p)] [WITHOUT TIMEZONE] | TIME [(p)] [WITHOUT TIMEZONE] |
| TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| CHAR(n) | STRING |
| CHARACTER(n) |   |
| VARCHAR(n) |   |
| CHARACTER VARYING(n) |   |
| TEXT |   |
| BYTEA | BYTES |

**Sample code**

```
CREATE TABLE source (
  id INT NOT NULL,
  name STRING,
  description STRING,
  weight DECIMAL(10,3)
) WITH (
  'connector' = 'postgres-cdc',
  'hostname' = '<host name>',
  'port' = '<port>',
  'username' = '<user name>',
  'password' = '<password>',
  'database-name' = '<database name>',
  'schema-name' = '<schema name>',
  'table-name' = '<table name>'
```

);

```
SELECT * FROM source;
```

### 5.9 TSDB for InfluxDB connector

This topic describes how to use the Time Series Database (TSDB) for InfluxDB connector.

**Background information**

TSDB for InfluxDB is a time series database service that can process large numbers of write and query requests. This service stores and analyzes large amounts of time series data in real time, including DevOps monitoring data, application metric data, and data that is collected from Internet of Things (IoT) sensors. The following table describes the capabilities supported by the TSDB for InfluxDB connector.

| Item | Description |
|---|---|
| Table types | Sink table |
| Running modes | Streaming mode |
| Data formats | Point |
| Monitoring metrics | numRecordsOut numRecordsOutPerSecond currentSendTime |
| API types | SQL |
| Data updates or deletion in a sink table | No |

**Prerequisites**

A TSDB for InfluxDB is created.

**Syntax**

```
CREATE TABLE stream_test_influxdb(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `tag_value1` VARCHAR,
 `field_fieldValue1` DOUBLE
) WITH (
  'connector' = 'influxdb',
  'url' = 'http://service.cn.influxdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='300',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
```

); Default format for the created table: Column 0: metric (VARCHAR). This column is required. Column 1: timestamp (BIGINT). This column is required. Unit: milliseconds. Column 2: tag_value1 (VARCHAR). This column is required. You must enter at least one value in this column. Column 3: field_fieldValue1 (DOUBLE). This column is required. You must enter at least one value in this column. To specify multiple field_fieldValue values, use the following format:

```
field_fieldValue1 <Data type>, field_fieldValue2 <Data type>, ... field_fieldValueN <Data type>
```

Sample code:

```
field_fieldValue1 DOUBLE, field_fieldValue2 INTEGER, ... field_fieldValueNINTEGER
```

> **Note:** A TSDB for InfluxDB sink table can contain only the following fields: **metric**, **timestamp**, tag_*, and field_*.

**Parameters in the WITH clause**

| > Document Ver | sion: 20260701 |   | 111 |
|---|---|---|---|

| Parameter | Description | Requir ed | Remarks |
|---|---|---|---|
| connector | The type of the sink table. | Yes | Set the value to influxdb. |
| url | The URL of the TSDB for InfluxDB database. | Yes | Contact Apsara Stack O&M engineers to obtain the required information. |
| database | The name of the TSDB for InfluxDB database. | Yes | Example: db-flink. |
| username | The username of the account that is used to access the database. | Yes | You must have write permissions on the TSDB for InfluxDB database. |
| password | The password that is used to access the database. | Yes | None. |
| batchSize | The number of data records that are submitted at the same time. | No | By default, 300 records are submitted at the same time. |
| retentionPoli cy | The retention policy. | No | If you do not configure this parameter, the default retention policy autogen for each database is used. |
| ignoreErrorD ata | Specifies whether to ignore abnormal data. | No | Valid values: true: ignores abnormal data. false: does not ignore abnormal data. This is the default value. |

**Data type mappings**

| Data type of TSDB for InfluxDB | Data type in Realtime Compute for Apache Flink |
|---|---|
| BOOLEAN | BOOLEAN |

| INT | INT |
|---|---|
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |

**Sample code**

```
CREATE TEMPORARY TABLE datahub_source(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `filedvalue` DOUBLE,
 `tagvalue` VARCHAR
) WITH (
  'connector' = 'datagen',
  'fields.metric.length' = '3',
  'fields.tagvalue.length' = '3',
  'fields.timestamp.min' = '1587539547000',
  'fields.timestamp.max' = '1619075547000',
  'fields.filedvalue.min' = '1',
  'fields.filedvalue.max' = '100000',
  'rows-per-second' = '50'
```

);

```
CREATE TEMPORARY TABLE influxdb_sink(
  `metric` VARCHAR,
  `timestamp` BIGINT,
  `field_fieldValue1` DOUBLE,
  `tag_value1` VARCHAR
) WITH (
  'connector' = 'influxdb',
  'url' = 'https://***********.influxdata.tsdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='100',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
```

);

```
INSERT INTO influxdb_sink SELECT
  `metric`,
  `timestamp`,
  `filedvalue`,
  `tagvalue`
FROM datahub_source;
```

### 5.10 Tablestore connector

This topic describes how to use the Tablestore connector.

**Background information**

Tablestore is a table-based, low-cost serverless storage service that is optimized for storing large amounts of structured data. Tablestore allows you to query and retrieve online data within milliseconds and analyze stored data in multiple dimensions. Tablestore is suitable for various scenarios such as a large number of bills, instant messaging (IM), IoT, Internet of Vehicles (IoV), risk management, and intelligent recommendation. Tablestore also provides a deeply optimized end-to-end storage solution for IoT applications. The following table describes the capabilities supported by the Tablestore connector.

| Item | Description |
|---|---|
| Running modes | Streaming mode |
| API types | SQL |
| Table types | Dimension table and sink table |
| Data formats | None |
| Monitoring metrics | Metrics for dimension tables: none Sink table numBytesOut numBytesOutPerSecond numRecordsOut numRecordsOutPerSecond currentSendTime |
| Data updates or deletion in a sink table | Yes |

**Prerequisites**

A Tablestore instance and a table are created.

**Syntax**

Sink table

```
CREATE TABLE ots_sink (
  name VARCHAR,
  age BIGINT,
  birthday BIGINT,
  primary key(name,age) not enforced
) WITH (
  'connector'='ots',
  'instanceName'='<yourInstanceName>',
  'tableName'='<yourTableName>',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}',
  'endPoint'='<yourEndpoint>',
  'valueColumns'='birthday'
```

);

> **Note:** You must specify a primary key for a Tablestore sink table. The latest output data is appended to the Tablestore sink table to update the table data.

Dimension table

```
CREATE TABLE ots_dim (
  id int,
  len int,
  content STRING
) WITH (
  'connector'='ots',
  'endPoint'='<yourEndpoint>',
  'instanceName'='<yourInstanceName>',
  'tableName'='<yourTableName>',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}'
```

);

**Parameters in the WITH clause**

Common parameters

| Parameter | Description | Remar ks | Requi red | Default value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | Set the value to ots . |
| instanceNam e | The name of the Tablestore instance. | String | Yes | None | None. |
| endPoint | The endpoint of the Tablestore instance. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| tableName | The name of the table | String | Yes | None | None. |

| accessId | The AccessKey ID of your Apsara Stack tenant account or a Resource Access Management (RAM) user. | String | Yes | None | None. |
|---|---|---|---|---|---|
| accessKey | The AccessKey secret of your Apsara Stack tenant account or a RAM user. | String | Yes | None | None. |
| connectTime out | The timeout period for the Tablestore connector to connect to Tablestore. | Integer | No | 30000 | Unit: milliseconds. |
| socketTimeo ut | The socket timeout period for the Tablestore connector to connect to Tablestore. | Integer | No | 30000 | Unit: milliseconds. |
| ioThreadCou nt | The number of I/O threads. | Integer | No | 4 | None. |
| callbackThre adPoolSize | The size of the callback thread pool. | Integer | No | 4 | None. |

Sink table-specific parameters

| Parameter | Description | Rema rks | Requ ired | Default value | Remarks |
|---|---|---|---|---|---|
| retryIntervalMs | The retry interval. | Integ er | No | 1000 | Unit: milliseconds. |

| maxRetryTimes | The maximum number of retries. | Integ er | No | 10 | None. |
|---|---|---|---|---|---|
| valueColumns | The names of the columns that you want to insert. | String | Yes | None | Separate multiple fields, such as the ID or NAME field, with commas (,). |
| bufferSize | The maximum number of data records that can be stored in the buffer before data deduplication is triggered. | Integ er | No | 5000 | None. |
| batchWriteTimeo utMs | The write timeout period. | Integ er | No | 5000 | Unit: milliseconds. If the number of cached data records does not reach the upper limit within the period of time specified by the batchWriteTimeoutMs parameter, all cached data is written to the sink table. |
| batchSize | The number of data records that can be written at a time. | Integ er | No | 100 | Maximum value: 200. |
| ignoreDelete | Specifies whether to ignore delete operations. | Boole an | No | False | None. |
| autoIncrementK ey | The name of the auto-increment primary key column of the sink table when the sink table contains an auto-increment primary key column. | String | No | None | If the sink table does not have an auto-increment primary key column, do not configure this parameter. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.4 or later supports this parameter. |

| overwriteMode | The data overwrite mode. | Enum | No | PUT | Valid values: PUT UPDATE Data is written to a Tablestore table in PUT or UPDATE mode. Limits: Only the UPDATE mode is supported in dynamic column mode. |
|---|---|---|---|---|---|
| defaultTimestam pInMillisecond | The default timestamp. | Long | No | -1 | The default timestamp that is used to write data to the Tablestore table. If you do not specify this parameter, the timestamp of the current system time is used. |
| dynamicColumn Sink | Specifies whether to enable the dynamic column mode. | Boole an | No | false | The dynamic column mode is suitable for scenarios in which no columns are specified for a table and data columns are inserted into the table based on the deployment status. You must specify the first several columns as the primary key columns in the table creation statement. The value of the second to the last column is used as a column name variable, the value of the last column is used as the value of the column name variable, and the data type of the second to the last column must be String. Limits: If you enable the dynamic column mode, the auto-increment primary key column feature is not supported, and you must set the overwriteMode parameter to UPDATE. |

| checkSinkTable Meta | Specifies whether to check the metadata of the sink table. | Boole an | No | true | If you set this parameter to true, the system checks whether the primary key column of the Tablestore table is the same as the primary key specified in the table creation statement. |
|---|---|---|---|---|---|
| enableRequestC ompression | Specifies whether to enable data compression during data writing. | Boole an | No | false | None. |

Dimension table-specific parameters

| Parameter | Description | Rema rks | Requir ed | Defaul t value | Remarks |
|---|---|---|---|---|---|
| retryIntervalMs | The retry interval. | Integ er | No | 1000 | Unit: milliseconds. |
| maxRetryTimes | The maximum number of retries. | Integ er | No | 10 | None. |
|   |   |   |   |   | Valid values: None: No data is cached. |

|   |   |   |   |   | LRU: Only specific data in the dimension table is cached. Each time the system receives a data record, the system searches the cache. If |
|---|---|---|---|---|---|
| cache | The cache policy. | String | No | ALL | the system does not find the record in the cache, the system searches for the data record in the physical dimension table. If this cache policy is used, you must configure the cacheSize and cacheTTLMs parameters. |
| Document Version: | 20260701 |   |   |   | 12 |

|   |   |   |   |   | ALL (default): All data in the dimension table is cached. Before a job runs, the system loads all data in the dimension table to the |
|---|---|---|---|---|---|
| cacheSize | The maximum number of rows of data records that can be cached. | Integ er | No | None | cache. This way, the cache is searched for If you set the cache all subsequent queries parameter to LRU, you in the dimension table. can configure this If the system does not parameter. find the data record in the cache, the join key |
| cacheTTLMs | The cache timeout period. | Integ er | No | None | does not exist. The Unsity:s mteimllis reeclooanddss .a Tllh deata coninf igthuer actaiocnh eo fa tfhteer cache cacehnetrTieTsL Mesx ppiarera.meter varIfi etsh eb aasmeodu onnt tohfe d vaatalu ien of ath ree mcaocthee t apbalrea mis estmera.ll aIfn ydo ua slaertg teh en ucmacbheer of mpairsasminge tkeer ytso eNxoisnte, ,w thee rceaccohmeTmTeLMnds tphaarta ymoeuter sceatn tbheis leofptt ieomn ptoty A. LTLh.is The source and indicates that cache dimension table cannot entries do not expire. be associated based on tIfh yeo OuN s ectla tuhsee c. aIfc yhoeu upsaera tmhiest cear cthoe L RpoUl,i ctyh,e ycaocuh meTuTsLt Mcos npfaigruarmee ttheer cspaecchiefieTsT LthMes t iamnedout cpaercihode Roef ltohaed cTaicmhee.B Blayc kdeLfiasut lpt,a craamcheet eernst.ries do not expire. If you seNto tthee cache parameter to ALL, the If you set the cache cacheTTLMs parameter parameter to ALL, specifies the interval at you must increase which the system the memory of the reloads the cache. By node for joining default, the cache is not tables because the reloaded. system asynchronously loads data from the dimension table. The increased |
| cacheEmpty | Specifies whether to cache empty results. | Boole an | No | None | memory size is trutew: icEem tphtayt roefs uthltes are cacrehmedo.te table. false: Empty results are not cached. |

| cacheReloadTim eBlackList | The time periods during which cache is not refreshed. This parameter takes effect when the cache parameter is set to ALL. The cache is not refreshed during the periods of time that you specify for this parameter. This parameter is suitable for large-scale online promotional events such as Double 11. | String | No | None | The following example shows the format of the values: 2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00. Use delimiters based on the following rules: Separate multiple time periods with commas (,). Separate the start time and end time of each time period with an arrow (->) that is a combination of a hyphen (-) and a closing angle bracket (>). |
|---|---|---|---|---|---|
| async | Specifies whether to enable data synchronization in asynchronous mode. | Boole an | No | false | true: Data synchronization in asynchronous mode is enabled. By default, the returned data is not sorted when data is synchronized in asynchronous mode. You can configure the asyncResultOrder parameter to specify whether the returned data is sorted when data is synchronized in asynchronous mode. false: Data synchronization in asynchronous mode is disabled. This is the default value. |

| asyncResultOrd er | Specifies whether the returned data is sorted when data is synchronized in asynchronous mode. | String | No | unorder ed | unordered: The returned data is not sorted when data is synchronized in asynchronous mode. This is the default value. ordered: The returned data is sorted when data is synchronized in asynchronous mode. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.0 or later supports this parameter. |
|---|---|---|---|---|---|

**Data type mappings**

| Data type of Realtime Compute for Apache Flink | Data type of fields in Tablestore |
|---|---|
| BINARY | BINARY |
| VARBINARY |   |
| CHAR | STRING |
| VARCHAR |   |
| TINYINT | INTEGER |
| SMALLINT |   |
| INTEGER |   |
| BIGINT |   |
| FLOAT | DOUBLE |
| DOUBLE |   |

| BOOLEAN | BOOLEAN |
|---|---|

**Sample code**

```
CREATE TEMPORARY TABLE ots_sink (
  `order` VARCHAR,
  orderid VARCHAR,
  customerid VARCHAR,
  customername VARCHAR,
  PRIMARY KEY (`order`,orderid) NOT ENFORCED
) WITH (
  'connector'='ots',
  'endPoint'='<yourEndpoint>',
  'instanceName'='flink-sink',
  'tableName'='flink_sink_table',
  'accessId'='${ak_id}',
  'accessKey'='${ak_secret}',
  'valueColumns'='customerid,customername',
  'autoIncrementKey'='${auto_increment_primary_key_name}'
```

);

### 5.11 ClickHouse connector

This topic describes how to use the ClickHouse connector.

**Background information**

ClickHouse is a column-oriented database management system that is used for online analytical processing (OLAP). The following table describes the capabilities supported by the ClickHouse connector.

| Item | Description |
|---|---|
| Table types | Sink table |
| Running modes | Batch mode and streaming mode |
| Data formats | None |
| Monitoring metrics | numRecordsOut numRecordsOutPerSecond currentSendTime |
| API types | SQL |

| Data updates or deletion in a sink table | If a primary key is specified in the DDL statement that is used to create a Flink result table and the ignoreDelete parameter is set to false, data in the result table can be updated or deleted. However, the data processing performance is significantly reduced. |
|---|---|

**Features**

For a ClickHouse distributed table, data is directly written to a ClickHouse local table that corresponds to the ClickHouse distributed table. For a ClickHouse cluster that is deployed in Apsara Stack E-MapReduce (EMR), you can use the exactly-once semantics.

**Prerequisites**

A ClickHouse table is created. A whitelist is configured.

**Limits**

The ClickHouse connector does not support the sink.parallelism parameter. ClickHouse sink tables support the at-least-once semantics. You can set the writeMode parameter to balance to evenly write data to a ClickHouse local table only in Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.7 or later.

**Syntax**

```
CREATE TABLE clickhouse_sink (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'maxRetryTimes' = '3',
  'batchSize' = '8000',
  'flushIntervalMs' = '1000'
  'ignoreDelete' = 'true',
  'shardWrite' = 'false',
  'writeMode' = 'partition',
  'shardingKey' = 'id'
```

);

**Parameters in the WITH clause**

| 26 |   |   |   |   | > Document Version: 2026070 |
|---|---|---|---|---|---|

| Paramet er | Description | Data type | Requir ed | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| connecto r | The type of the sink table. | String | Yes | None | Set the value to clickhouse. |
| url | The Java Database Connectivity (JDBC) URL of ClickHouse. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. If you do not specify the database name, the database named default is used. Note If you want to write data to a ClickHouse distributed table, the URL is the JDBC URL of the node to which the ClickHouse distributed table belongs. |
| userNam e | The username that is used to access ClickHouse. | String | Yes | None | None. |
| passwor d | The password that is used to access ClickHouse. | String | Yes | None | None. |
| tableNa me | The name of the ClickHouse table. | String | Yes | None | None. |
| maxRetr yTimes | The maximum number of retries for writing data to the result table. | Int | No | 3 | None. |

| batchSiz e | The number of data records that can be written at a time. | Int | No | 100 | If the number of data records in the cache reaches the value of the batchSize parameter or the interval at which the cache is cleared is greater than the value of the flushIntervalMs parameter, the system automatically writes the cached data to the ClickHouse table. |
|---|---|---|---|---|---|
| flushInte rvalMs | The interval at which the cache is cleared. | Long | No | 1000 | Unit: milliseconds. |
| ignoreDe lete | Specifies whether to ignore the delete messages. | Boolean | No | true | Valid values: true: ignores the delete messages. This is the default value. false: does not ignore the delete messages. If you set this parameter to false and specify a primary key in the DDL statement, the system executes the ALTER statement to delete data from the ClickHouse table. Note If you set the ignoreDelete parameter to false, data cannot be written to a ClickHouse local table that corresponds to the ClickHouse distributed table in partition write mode. In this case, you cannot set the writeMode parameter to partition. |
|   |   |   |   |   | Valid values: false: The system writes data to the ClickHouse distributed table and then to a ClickHouse local table that corresponds to the ClickHouse distributed table. This is the default value. In this case, if you set the shardWrite parameter to false, you must set the tableName parameter to the name of the ClickHouse distributed table. |

|   |   |   |   |   | true: The system skips the |
|---|---|---|---|---|---|
| shardWri te | Specifies whether to directly write data to a ClickHouse local table if the current table is a ClickHouse distributed table. | Boolean | No | false | ClickHouse distributed table and directly writes data to a ClickHouse local table that corresponds to the ClickHouse distributed table. If you want to increase the throughput for writing data to the ClickHouse distributed table, we recommend that you set this parameter to true. If you want to manually specify the nodes on which data is written to the ClickHouse local tables in the url parameter, you must set the tableName parameter to the names of the ClickHouse local tables. Sample code: 'url' = 'jdbc:clickhouse://192 .XX.XX.1:8123,192.XX.X X.2:8123/default' 'tableName' = 'local table' _ |
| > Document V | ersion: 20260701 |   |   |   | 12 |

|   |   |   |   |   | If you do not want to manually specify the nodes on which data is written to |
|---|---|---|---|---|---|
| inferLoca lTable | Specifies whether to automatically infer the information about the ClickHouse local tables that correspond to a ClickHouse distributed table if you want to write data to the ClickHouse distributed table and directly write data to the ClickHouse local tables. | Boolean | No | false | the ClickHouse local tables Validi nv atlhuee su:rl parameter, you can configure the false: If you want to write data inferLocalTable parameter to a ClickHouse distributed together with the table and specify only one shardWrite parameter to node in the url parameter, the allow Realtime Compute for system does not automatically Apache Flink to infer the information about the automatically infer the ClickHouse local tables that nodes of the ClickHouse correspond to the ClickHouse local tables. In this case, distributed table. The system you must set the tableName writes data to the ClickHouse parameter to the name of distributed table and then to the ClickHouse distributed the ClickHouse local tables. table and the url parameter This is the default value. to the JDBC URL of the node truteo: wThheic hsy tshtee mClickHouse audtoismtraibtiuctaelldy tianbfelers b tehleongs. infSoarmmaptlieo nc oadbeo:ut the ClickHouse local tables that corre'suproln'd =t o the ClickHouse distr'ibjudtbecd: ctalbilcek ahnodu sdei:re/c/t1ly92 writes data to the ClickHouse .XX.XX.1:8123/default' local tables. In this case, if you // Set the url set the inferLocalTable parapmaertaemre ttoe rtr uteo, ytohue must set tJhDeB sCh aUrRdLW orift et phaer anmoedete r to true, the tableName to which the parameter to the name of the ClickHouse ClickHouse distributed table, and dthies turril bpuatraemd ettaebrl teo the JDBCb eUlRoLn ogsf .the node to which the ClickHouse distributed 'tableName' = table belongs. 'distribute table' _ Note If you want to write data to a ClickHouse non- distributed table, you do not need to configure this parameter. |

| writeMod e | The policy based on which data is written to a ClickHouse local table. | Enum | No | defau lt | Valid values: default: Data is written to the ClickHouse local table on the first node of the ClickHouse cluster. This is the default value. partition: Data with the same key is written to the same ClickHouse local table on a specific node. random: Data is randomly written to the ClickHouse local table on a node. balance: The round-robin algorithm is used to evenly write data to the ClickHouse local table on a node. Note If you set the writeMode parameter to partition, make sure that the ignoreDelete parameter is set to true. |
|---|---|---|---|---|---|
| sharding Key | The key based on which data is written to the same ClickHouse local table on a specific node. | default | No | None | If you set the writeMode parameter to partition, you must configure the shardingKey parameter. The value of the shardingKey parameter can contain multiple fields. Separate multiple fields with commas (,). |

| exactlyO nce | Specifies whether to use the exactly- once semantics. | Boolean | No | false | Valid values: true: The exactly-once semantics is used. false: The exactly-once semantics is not used. This is the default value. Note You can use the exactly-once semantics to write data only to a ClickHouse cluster that is deployed in Apsara Stack EMR. Therefore, you can set this parameter to true only if you want to write data to a ClickHouse cluster that is deployed in Apsara Stack EMR. If you set the writeMode parameter to partition and you want to write data to a ClickHouse local table, you cannot use the exactly-once semantics. Therefore, if you set the exactlyOnce parameter to true, you cannot set the writeMode parameter to partition. |
|---|---|---|---|---|---|

**Data type mappings**

| Data type in Realtime Compute for Apache Flink | Data type of ClickHouse |
|---|---|
| BOOLEAN | UInt8 / Boolean Note ClickHouse V21.12 and later support the BOOLEAN data type. If the version of ClickHouse that you use is earlier than V21.12, the BOOLEAN data type of Realtime Compute for Apache Flink corresponds to the UINT8 data type of ClickHouse. |

| TINYINT | Int8 |
|---|---|
| SMALLINT | Int16 |
| INTEGER | Int32 |
| BIGINT | Int64 |
| BIGINT | UInt32 |
| FLOAT | Float32 |
| DOUBLE | Float64 |
| CHAR | FixedString |
| VARCHAR | String |
| BINARY | FixedString |
| VARBINARY | String |
| DATE | Date |
| TIMESTAMP(0) | DateTime |
| TIMESTAMP(x) | Datetime64(x) |
| DECIMAL | DECIMAL |
| ARRAY | ARRAY |
|   | Nested |

> **Note:** ClickHouse does not support the following data types of Realtime Compute for Apache Flink: TIME, MAP, MULTISET, and ROW.

To use the NESTED data type of ClickHouse, you must map this data type to the ARRAY data type of Realtime Compute for Apache Flink. Sample code:

```
-- ClickHouse CREATE TABLE visits (
  StartDate Date,
  Goals Nested
```

`(`

```
    ID UInt32,
    OrderID String
```

`)`

```
  ...
```

); Map the NESTED data type of ClickHouse to the ARRAY data type of Realtime Compute for Apache Flink.

```
-- Flink CREATE TABLE visits (
  StartDate DATE,
  `Goals.ID` ARRAY<LONG>,
  `Goals.OrderID` ARRAY<STRING>
```

);

> **Note:** The DATETIME data type of ClickHouse can be accurate to the second, and the DATETIME64 data type can be accurate to the nanosecond. For Realtime Compute for Apache Flink that uses VVR of a version earlier than 6.0.6, when the JDBC driver provided by ClickHouse writes data of the DATETIME64 data type, a precision loss occurs and the data can be accurate only to the second. Therefore, Realtime Compute for Apache Flink can write data of the TIMESTAMP data type only in seconds. The value is displayed in the TIMESTAMP(0) format. For Realtime Compute for Apache Flink that uses VVR 6.0.6 or later, the precision loss issue is resolved. Realtime Compute for Apache Flink can write data of the DATETIME64 data type as expected.

**Sample code**

Example 1: Data is written to a ClickHouse local table on a node.

```
CREATE TEMPORARY TABLE clickhouse_source (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
```

);

```
CREATE TEMPORARY TABLE clickhouse_output (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
```

);

```
INSERT INTO clickhouse_output SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

Example 2: Data is written to a ClickHouse distributed table. Three ClickHouse local tables named local_table_test exist on the 192.XX.XX.1, 192.XX.XX.2, and 192.XX.XX.3 nodes. A ClickHouse distributed table named distributed_table_test is created based on the ClickHouse local tables. If you want to directly write data that has the same key to the same ClickHouse local table on a specific node, execute the following statements:

```
CREATE TEMPORARY TABLE clickhouse_source (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
```

);

```
CREATE TEMPORARY TABLE clickhouse_output (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' =
'jdbc:clickhouse://192.XX.XX.1:8123,192.XX.XX.2:8123,192.XX.XX.3:8123/default',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = 'local_table_test',
  'shardWrite' = 'true',
  'writeMode' = 'partition',
  'shardingKey' = 'name'
```

);

```
INSERT INTO clickhouse_output SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

If you do not want to manually specify the nodes on which data is written to the ClickHouse local tables in the url parameter, execute the following statements to allow the system to automatically infer the nodes of the ClickHouse local tables:

```
CREATE TEMPORARY TABLE clickhouse_source (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
```

);

```
CREATE TEMPORARY TABLE clickhouse_output (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = 'jdbc:clickhouse://192.XX.XX. 1:8123/default', -- Set the url parameter t
o the JDBC URL of the node to which the ClickHouse distributed table belongs.
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = 'distributed_table_test', -- Set the tableName parameter to the nam
e of the ClickHouse distributed table.
  'shardWrite' = 'true',
  'inferLocalTable' = 'true', -- Set the inferLocalTable parameter to true.
  'writeMode' = 'partition',
  'shardingKey' = 'name'
```

);

```
INSERT INTO clickhouse_output SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

### 5.12 Elasticsearch connector

This topic describes how to use the Elasticsearch connector.

**Background information**

Apsara Stack Elasticsearch is compatible with the features of open source Elasticsearch, such as Security, Machine Learning, Graph, and Application Performance Monitoring (APM). Apsara Stack Elasticsearch provides enterprise-class services, such as access control, security monitoring and alerting, and automatic generation of reports. The following table describes the capabilities supported by the Elasticsearch connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Batch mode and streaming mode |
| Data formats | JSON |
| Monitoring metrics | Metrics for source tables: pendingRecords numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerSecond Metrics for dimension tables: none Metrics for sink tables in Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.6 or later numRecordsOut numRecordsOutPerSecond |
| API types | DataStream API and SQL API |

**Prerequisites**

An Elasticsearch index is created. A whitelist is configured to allow access to an Elasticsearch cluster over the Internet or a virtual private cloud (VPC).

**Limits**

The Elasticsearch connector can be used for source tables and dimension tables only if the related Elasticsearch cluster is of a version that is later than or equal to V5.5 but earlier than V8.X. The Elasticsearch connector can be used for sink tables only if the related Elasticsearch cluster is of V6.X, V7.X, or V8.X. The Elasticsearch connector can be used only for full Elasticsearch source tables and cannot be used for incremental Elasticsearch source tables.

**Syntax**

Source table

```
CREATE TABLE elasticsearch_source(
  name STRING,
  location STRING,
  value FLOAT
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'indexName' = '<yourIndexName>'
```

); Dimension table

```
CREATE TABLE es_dim(
  field1 STRING, --- If this field is used as a key to join a dimension table with an
other table, the value of this field must be of the STRING data type.
  field2 FLOAT,
  field3 BIGINT,
  PRIMARY KEY (field1) NOT ENFORCED
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'indexName' = '<yourIndexName>'
```

);

> **Note:** If you define a primary key for a dimension table, only one key can be used to join the dimension table with another table. The key is the ID of a document in your Elasticsearch index.
> If you do not define a primary key for the dimension table, one or more keys can be used to join the dimension table with another table. The keys are the fields of a document in your Elasticsearch index.
> By default, the .keyword suffix is added to the names of the fields of the STRING data type to ensure compatibility. If the fields of the TEXT data type in the Elasticsearch table cannot be matched, you can set the value of the ignoreKeywordSuffix parameter to true.

Sink table

```
CREATE TABLE es_sink(
  user_id   STRING,
  user_name   STRING,
  uv BIGINT,
  pv BIGINT,
  PRIMARY KEY (user_id) NOT ENFORCED
) WITH (
  'connector' = 'elasticsearch-7' -- If the Elasticsearch version is V6.X, enter elas
ticsearch-6.
  'hosts' = '<yourHosts>',
  'index' = '<yourIndex>'
```

);

> **Note:** The Elasticsearch sink table is determined to work in upsert mode or append mode based on whether a primary key is defined.
> If a primary key is defined for the Elasticsearch sink table, the primary key must be a document ID, and the Elasticsearch sink table works in upsert mode. In this mode, the Elasticsearch sink table can consume UPDATE and DELETE messages.
> If no primary key is defined for the Elasticsearch sink table, Elasticsearch automatically generates a random document ID, and the Elasticsearch sink table works in append mode. In this mode, the Elasticsearch sink table can consume only INSERT messages.
> Specific data types, such as BYTES, ROW, ARRAY, and MAP, cannot be represented as strings. Therefore, fields of these data types cannot be used as primary key fields.
> The fields in the DDL statement correspond to the fields in an Elasticsearch document. Metadata, such as document IDs, is maintained on Elasticsearch clusters. Therefore, metadata cannot be written to Elasticsearch sink tables.

**Parameters in the WITH clause**

Source table-specific parameters

| Parameter | Description | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| connector | The type of the source table. | String | Yes | Non e | Set the value to elasticsearch. |
| endPoint | The endpoint of the Elasticsearch cluster. | String | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |
| indexName | The name of the Elasticsearch index. | String | Yes | Non e | None. |
| accessId | The username that is used to access the Elasticsearch cluster. | String | No | Non e |   |
| 0 |   |   |   |   | > Document Version: 2026070 |

|   |   |   |   |   | or |
|---|---|---|---|---|---|
|   |   |   |   |   | By default, this parameter is empty. This indicates that permission verification is not required. If you configure the accessId parameter, you must also configure the accessKey parameter. |
| accessKey | The password that is used to access the Elasticsearch cluster. | String | No | Non e |   |
| typeNames | The names of types. | String | No | doc _ | We recommend that you do not configure this parameter if the version of your Elasticsearch cluster is later than V7.0. |
| batchSize | The maximum number of documents that can be obtained from the Elasticsearch cluster for each scroll request. | Int | No | 2000 | None. |
| keepScrollA liveSecs | The maximum retention period of the scroll context. | Int | No | 3600 | Unit: seconds. |

Sink table-specific parameters

| Parame ter | Description | Data type | Require d | Default value | Remarks |
|---|---|---|---|---|---|
| connect or | The type of the sink table. | String | Yes | None | Set the value to elasticsearch-6 , elasticsearch-7 , or elasticsearch-8 . |
| hosts | The endpoint of the Elasticsearch cluster. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |

| index | The name of the Elasticsearch index. | String | Yes |   |   |   |   | The Elasticsearch sink table supports both static and dynamic indexes. When you use static and dynamic indexes, take note of the following points: If you use a static index, the index option value must be a string, such as myusers . All records are written to the myusers index. If you use a dynamic index, you can use {field name} to _ reference the field values in the records to dynamically generate the destination index. You can also use {field namedate for _ _ mat string} to _ convert field values of the TIMESTAMP, DATE, and TIME data types into the format specified by date format string _ _ . date format string _ _ is compatible with DateTimeFormatter in Java. For example, if you set the dynamic index to myusers- {log tsyyyy-MM-dd} , _ the record 2020-03- 27 12:25:55 in the value of the log ts field _ is written to the myusers-2020-03- 27 index. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | {field namedate for _ _ |   |   |
|   |   |   |   |   |   |   | None | mat string} _ |   |   |   |
|   |   |   |   |   |   |   |   |   | date format string _ _ |   |   |
|   |   |   |   |   |   |   |   |   |   | . |   |
|   |   |   |   |   |   |   |   |   | myusers-2020-03- |   |   |
|   |   |   |   |   |   |   |   | 27 |   |   |   |

|   | {log tsyyyy-MM-dd} _ |   |   |   |
|---|---|---|---|---|
|   |   |   | , |   |
|   | the record |   |   |   |
|   | 27 12:25:55 |   |   |   |

| docume nt-type | The type of a document. | String | If the connec tor param eter is set to elastics earch- 6, this param eter must be configu red. If the connec tor param eter is set to elastics earch- 7, this param eter is not suppor ted. | None | If the connector parameter is set to elasticsearch-6 , the value of this parameter must be the same as the value of the type parameter that is configured for Elasticsearch. |
|---|---|---|---|---|---|
| userna me | The username that is used to access the Elasticsearch cluster. | String | No | Left empty | By default, this parameter is empty. This indicates that permission verification is not required. If you configure the username parameter, you must also configure the password parameter. |
| passwo rd | The password that is used to access the Elasticsearch cluster. | String | No | Left empty |   |

| docume nt- id.key- delimit er | The delimiter that is used to separate multiple document IDs. | String | No | _ | In the Elasticsearch sink table, the primary key is used to calculate document IDs of Elasticsearch. The Elasticsearch sink table concatenates all primary key fields in the order that is defined in the DDL statement by using the key delimiter that is specified by document- id.key-delimiter. A document ID is also generated for each row. Note A document ID is a string that contains a maximum of 512 bytes without spaces. |
|---|---|---|---|---|---|
| failure- handler | The fault handling policy that is used when an Elasticsearch request fails. | String | No | fail | Valid values: fail: The deployment fails if the request fails. This is the default value. ignore: The failure is ignored, and the request is deleted. retry rejected: The _ request is retried if the failure is caused by full queue capacity. custom class name: The ActionRequestFailureHa ndler subclass is used to troubleshoot the failure. |

| sink.flu sh-on- checkpo int | Specifies whether the flush operation is triggered during checkpointing. | Boolean | No | true | true: The flush operation is triggered during checkpointing. This is the default value. false: The flush operation is not triggered during checkpointing. After this feature is disabled, the Elasticsearch connector does not wait to check whether all pending requests are complete during checkpointing. Therefore, the Elasticsearch connector does not provide the at- least-once guarantee for requests. |
|---|---|---|---|---|---|
| sink.bul k- flush.ba ckoff.st rategy | You can configure the sink.bulk- flush.backoff.s trategy parameter to specify a retry policy if the flush operation fails due to a temporary request error. | Enum | No | DISABLED | DISABLED: The flush operation is not retried. The flush operation fails when the first request error occurs. This is the default value. CONSTANT: The waiting time for each flush operation is the same. EXPONENTIAL: The waiting time for each flush operation exponentially increases. |
| sink.bul k- flush.ba ckoff.m ax- retries | The maximum number of retries. | Int | No | None | None. |

| sink.bul k- flush.ba ckoff.de lay | The delay between retries. | Duration | No | None | If the sink.bulk- flush.backoff.strategy parameter is set to CONSTANT, the value of this parameter is the delay between retries. If the sink.bulk- flush.backoff.strategy parameter is set to EXPONENTIAL, the value of this parameter is the initial baseline delay. |
|---|---|---|---|---|---|
| sink.bul k- flush.m ax- actions | The maximum number of flush operations that can be performed for each batch of requests. | Int | No | 1000 | The value 0 indicates that this feature is disabled. |
| sink.bul k- flush.m ax-size | The maximum memory size of the buffer in which requests are saved. | String | No | 2 MB | Default value: 2. Unit: MB. If this parameter is set to 0, this feature is disabled. |
| sink.bul k- flush.in terval | The interval at which flush operations are performed. | Duration | No | 1s | Default value: 1. Unit: seconds. If this parameter is set to 0, this feature is disabled. |
| connect ion.pat h-prefix | The prefix that must be added to each REST communication. | String | No | Left empty | None. |

| retry- on- conflict | The maximum number of retries that are allowed due to version conflicts in an update operation. If the number of retries exceeds the value of this parameter, an exception occurs and the deployment fails. | Int | No | 0 | This parameter takes effect only when a primary key is specified. |
|---|---|---|---|---|---|
| routing- fields | Specifies one or more names for fields in the Elasticsearch sink table. The field names are used to route documents to the specified shards of the Elasticsearch cluster. | String | No | None | Separate multiple field names with semicolons (;). If a field is empty, the field is set to null. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter when the connector parameter is set to elasticsearch-7 or elasticsearch-8. |

Dimension table-specific parameters

| Parameter | Descriptio n | Dat a typ e | Requ ired | Def aul t val ue | Remarks |
|---|---|---|---|---|---|
| connector | The type of the dimension table. | Stri ng | Yes | Non e | Set the value to elasticsearch. |

| endPoint | The endpoint of the Elasticsear ch cluster. | Stri ng | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |
|---|---|---|---|---|---|
| indexName | The name of the Elasticsear ch index. | Stri ng | Yes | Non e | None. |
| accessId | The username that is used to access the Elasticsear ch cluster. | Stri ng | No | Non e | By default, this option is empty. This indicates that permission verification is not required. If you configure the accessId option, you must also configure the accessKey option. Important To enhance security, use variables instead of hardcoding your AccessKey pair in plaintext.. |
| accessKey | The password that is used to access the Elasticsear ch cluster. | Stri ng | No | Non e |   |
| typeNames | The names of types. | Stri ng | No | do _ c | We recommend that you do not configure this parameter if the version of your Elasticsearch cluster is later than V7.0. |
| maxJoinRo ws | The maximum number of rows that can be joined. | Inte ger | No | 102 4 | None. |

| cache | The cache policy. | Stri ng | No | ALL | Valid values: ALL: All data in the dimension table is cached. Before a deployment runs, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If no keys exist, the system cannot find the data record in the cache. The system reloads all data in the cache after cache entries expire. LRU: Partial data in the dimension table is cached. The system searches for data in the cache each time a data record is read from the source table. If the data is not found, the system searches for the data in the physical dimension table. None: No data is cached. |
|---|---|---|---|---|---|
| cacheSize | The maximum number of rows of data that can be cached. | Lon g | No | 100 000 | The cacheSize parameter takes effect only when you set the cache parameter to LRU. |
| cacheTTLM s | The cache timeout period. | Lon g | No | Lon g.M AX _ VAL UE | Unit: milliseconds. The configuration of the cacheTTLMs parameter varies based on the cache parameter. If the cache parameter is set to LRU, the cacheTTLMs parameter specifies the cache timeout period. By default, cache entries do not expire. If you set the cache parameter to ALL, the cacheTTLMs parameter specifies the interval at which the system refreshes the cache. By default, the cache is not refreshed. |

| ignoreKey wordSuffix | Specifies whether to ignore the .keyword suffix that is automatical ly added to the name of the field of the STRING data type. | Bool ean | No | fals e | Realtime Compute for Apache Flink converts fields of the TEXT data type into fields of the STRING data type to ensure compatibility. By default, the .keyword suffix is added to the names of the fields of the STRING data type. Valid values: true: The .keyword suffix is ignored. If the fields of the TEXT data type in the Elasticsearch sink table cannot be matched, set this parameter to true. false: The .keyword suffix is not ignored. |
|---|---|---|---|---|---|
| cacheEmpt y | Specifies whether to cache the empty results that are found in the physical dimension table. | Bool ean | No | tru e | The cacheEmpty parameter takes effect only when the cache parameter is set to LRU. |

**Data type mappings**

Realtime Compute for Apache Flink parses Elasticsearch data in the JSON format. For more information, see Data Type Mapping.

**Sample code**

Sample code for a source table

```
CREATE TEMPORARY TABLE elasticsearch_source (
  name STRING,
  location STRING,
  `value` FLOAT
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'indexName' = '<yourIndexName>',
  'typeNames' = '<yourTypeName>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  name STRING,
  location STRING,
  `value` FLOAT
) WITH (
  'connector' ='blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT name, location, `value` FROM elasticsearch_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source (
  id STRING,
  data STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE es_dim (
  id STRING,
  `value` FLOAT,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' ='elasticsearch',
  'endPoint' = '<yourEndPoint>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'indexName' = '<yourIndexName>',
  'typeNames' = '<yourTypeName>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  id STRING,
  data STRING,
  `value` FLOAT
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT e.*, w.* FROM datagen_source AS e JOIN es_dim FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
  id STRING,
  name STRING,
  uv BIGINT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE es_sink (
  user_id STRING,
  user_name STRING,
  uv BIGINT,
  PRIMARY KEY (user_id) NOT ENFORCED -- The primary key is optional. If you specify a
primary key, the primary key is used as the document ID. If you do not specify a prim ary key, a random value is used as the document ID. ) WITH (
  'connector' = 'elasticsearch-6',
  'hosts' = '<yourHosts>',
  'index' = '<yourIndex>',
  'document-type' = '<yourElasticsearch.types>',
  'username' ='${secret_values.ak_id}',
  'password' ='${secret_values.ak_secret}'
```

);

```
INSERT INTO es_sink SELECT id, name, uv FROM datagen_source;
```

### 5.13 Upsert Kafka connector

This topic describes how to use the Upsert Kafka connector.

**Background information**

The Upsert Kafka connector can be used to read data from and write data to Kafka topics in the upsert fashion. The Upsert Kafka connector for a source table can convert data that is stored in Kafka topics into a changelog stream. Each data record in the changelog stream represents an update or a delete event. If a Kafka topic contains a key that is the same as the key in a data record, the value in the data record overwrites the value of the key. The data record is interpreted as UPDATE. If a Kafka topic does not contain such a key in a data record, the value in the data record is inserted into the Kafka topic. The data record is interpreted as INSERT. Each data record in a changelog stream is interpreted as UPSERT (INSERT or UPDATE) because an existing row with the same key is always overwritten. If the value of the key in a data record is null, the data record is interpreted as DELETE. The Upsert Kafka connector for a result table can consume changelog streams that are produced by the source. The Upsert Kafka connector can write INSERT and UPDATE_AFTER data to Kafka topics as normal Kafka messages. The Upsert Kafka connector can write DELETE data to Kafka topics as Kafka messages with null values. If the value of the key in a data record is null, the Kafka message that uses the key is deleted. Flink partitions data based on the values of the primary key column. This ensures that messages with the same primary key are sorted by value. Therefore, UPDATE or DELETE data that contains the same primary key is written to the same partition.

| Item | Description |
|---|---|
| Table types | Source table and sink table |
| Running modes | Streaming mode |
| Data formats | avro, avro-confluent, csv, json, and raw |
| Monitoring metrics | Metrics for source tables: numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime pendingRecords Metrics for sink tables: numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

A Kafka cluster is created.

**Limits**

The Upsert Kafka connector can be used to read or write only data of Apache Kafka 0.10 or later. The Upsert Kafka connector supports only the client parameters of Apache Kafka 2.8. For more information about the configuration parameters of the Kafka producer and consumer, see Consumer Configs and Producer Configs. If an Upsert Kafka sink table uses the exactly-once semantics, you must enable the Kafka transaction mechanism to write data to a Kafka cluster. The version of the Kafka cluster must be Apache Kafka 0.11 or later.

**Syntax**

```
CREATE TABLE upsert_kafka_sink( user_region STRING, pv BIGINT, uv BIGINT, PRIMARY KEY(user_region) NOT ENFORCED )WITH( 'connector'='upsert-kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'key.format'='avro', 'value.format'='avro'
```

);

**Parameters in the WITH clause**

Common parameters

| Parameter | Description | Data type | Requi red | Defau lt value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | Set the value to upsert-kafka. |
| properties.bo otstrap.server s | The IP address and port number of a Kafka broker. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |

| properties.* | The parameters that are configured for the Kafka client. | String |   |   |   | The suffix of this option must comply with the rules that are defined in Producer Configs and Consumer Configs. Flink removes the properties. prefix and passes the transformed key and values to the Kafka client. For example, you can set properties.allow.auto.crea te.topics to false to disable automatic topic creation. You cannot modify the configurations of the following parameters by adding the properties. prefix, because the values of the parameters are overwritten after you use the Upsert Kafka connector: key.deserializer value.deserializer |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | properties.allow.auto.crea |   |
|   |   |   |   |   |   | te.topics |   |   |
|   |   |   |   | No | None |   |   |   |
| key.format | The format of the Kafka message key. | String |   | Yes | None | You must configure the key.fields or key.fields- prefix parameter if you configure this parameter. Valid values: csv json avro debezium-json canal-json maxwell-json avro-confluent raw |   |   |

| key.fields- prefix | The custom prefix for all key fields in Kafka messages. You can configure this parameter to prevent name conflicts with the value fields. | String | No | None | This parameter is used only to distinguish the column names of source tables and sink tables. The prefix is removed from the column names when the key fields of Kafka messages are parsed or generated. Note If you configure this parameter, you must set the value.fields-include parameter to EXCEPT KEY. _ |
|---|---|---|---|---|---|
| value.format | The format used to read or write the value field of Kafka messages. | String | Yes | None | The configuration of this parameter is equivalent to the configuration of the format parameter. The format parameter cannot be used together with the value.format parameter. If you configure both parameters, a conflict occurs. |
| value.fields- include | Specifies whether to include corresponding message keys when parsing or generating Kafka message values. | String | Yes | ALL | Valid values: ALL: All fields are processed as value fields of Kafka messages. This is the default value. EXCEPT KEY: All fields except _ for the fields specified by the key.fields parameter are processed as value fields of Kafka messages. |
| topic | The name of the topic from which data is read or to which data is written. | String | Yes | None | None. |

Sink table-specific parameters

| Parameter | Description | Data type | Requi red | Defau lt value | Remarks |
|---|---|---|---|---|---|

| sink.parallelis m | The parallelism of operators for the Kafka sink table. | Integer | No | The paralle lism of upstre am operat ors, which is deter mined by the frame work. | None. |
|---|---|---|---|---|---|
| sink.buffer- flush.max- rows | The maximum number of data records that can be cached before the cache is refreshed. | Integer | No | 0 (disabl ed) | If the sink table receives a large number of updates on the same key, only the last data record of the key is retained in the cache. In this case, data caching in the sink table helps reduce the amount of data that is written to Kafka topics. This prevents potential tombstone messages from being sent to Kafka topics. Note If you want to enable data caching for sink tables, you must set the sink.buffer- flush.max-rows and sink.buffer- flush.interval parameters to values that are greater than 0. |

| sink.buffer- flush.interval | The interval at which the cache is refreshed. | Durati on | No |   |   | The unit can be milliseconds, seconds, minutes, or hours. For example, you can configure 'sink.buffer- flush.interval'='1 s' . If the sink table receives a large number of updates on the same key, only the last data record of the key is retained in the cache. In this case, data caching in the sink table helps reduce the amount of data that is written to Kafka topics. This prevents potential tombstone messages from being sent to Kafka topics. Note If you want to enable data caching for sink tables, you must set the sink.buffer- flush.max-rows and sink.buffer- flush.interval parameters to values that are greater than 0. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | 'sink.buffer- |   |
|   |   |   |   |   |   | flush.interval'='1 s' |   |   |
|   |   |   |   |   | 0 (disabl ed) |   |   |   |

**Sample code**

Sample code for a source table Create a Kafka source table that contains the browsing data of website users.

```
CREATE TABLE pageviews( user_id BIGINT, page_id BIGINT, viewtime TIMESTAMP, user_region STRING, WATERMARK FOR viewtime AS viewtime - INTERVAL '2' SECOND )WITH( 'connector'='kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'format'='json'
```

); Sample code for a sink table Create an Upsert Kafka sink table.

```
CREATE TABLE pageviews_per_region( user_region STRING, pv BIGINT, uv BIGINT, PRIMARY KEY(user_region) NOT ENFORCED )WITH( 'connector'='upsert-kafka', 'topic'='<yourTopicName>', 'properties.bootstrap.servers'='...', 'key.format'='avro', 'value.format'='avro'
```

); Write the browsing data of website users to the sink table.

```
INSERT INTO pageviews_per_region SELECT user_region, COUNT(*), COUNT(DISTINCTuser_id) FROM pageviews GROUP BY user_region;
```

### 5.14 AnalyticDB for PostgreSQL connector

**connector**

This topic describes how to use the AnalyticDB for PostgreSQL connector.

**Background information**

AnalyticDB for PostgreSQL is a data warehouse for massively parallel processing (MPP). It provides online analysis services for a large amount of data. The following table describes the capabilities supported by the AnalyticDB for PostgreSQL connector.

| Item | Description |
|---|---|
| Table types | Dimension table and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | None |

| Monitoring metrics | Metrics for sink tables: numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime Metrics for dimension tables: none |
|---|---|
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

A whitelist is configured. An AnalyticDB for PostgreSQL instance and an AnalyticDB for PostgreSQL table are created.

**Limits**

Self-managed PostgreSQL databases are not supported. Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.0 or later supports the AnalyticDB for PostgreSQL connector. Only Realtime Compute for Apache Flink that uses VVR 8.0.1 or later supports AnalyticDB for PostgreSQL V7.0.

**Syntax**

```
CREATE TABLE adbpg_table (
 id INT,
 len INT,
 content VARCHAR,
 PRIMARY KEY(id)
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
```

);

**Parameters in the WITH clause**

| Cate gory | Parameter | Description | Data type | Requ ired | Defa ult value | Description |
|---|---|---|---|---|---|---|

| Com mon para meter s | connector | The type of tables. | String | Yes | None | Set the value to adbpg. |
|---|---|---|---|---|---|---|
|   | url | The Java Database Connectivity (JDBC) URL of the database. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|   | tableName | The name of the table | String | Yes | None | None. |
|   | userName | The username. | String | Yes | None | None. |
|   | password | The password. | String | Yes | None | None. |
|   | maxRetryTi mes | The maximum number of retries to write data after a data write fails. | Integ er | No | 3 | None. |
|   | targetSchem a | The name of the schema. | String | No | public | None. |
|   | caseSensitiv e | Specifies whether to enable case sensitivity. | String | No | false | Valid values: true: enables case sensitivity. false: disables case sensitivity. This is the default value. |
|   | connectionM axActive | The maximum number of connections in the connection pool. | Integ er | No | 5 | The system automatically releases idle connections to the database service. Important If this parameter is set to an excessively large value, the number of server connections may be abnormal. |

| Sink table- specif ic para meter s | retryWaitTim e | The interval between retries. | Integ er | No | 100 | Unit: milliseconds. |
|---|---|---|---|---|---|---|
|   | batchSize | The number of data records that can be written to the table at a time. | Integ er | No | 500 | None. |
|   | flushInterval Ms | The interval at which the cache is cleared. | Integ er | No | None | If the number of cached data records does not reach the upper limit within the specified period of time, all cached data is written to the result table. Unit: milliseconds. |
|   | writeMode | The write mode in which the system attempts to write data to the table for the first time. | String | No | insert | Valid values: insert: Data is directly inserted into the result table. If a conflict occurs, the handling policy is determined by the conflictMode parameter. This is the default value. upsert: Data in the table is automatically updated when a conflict occurs. This value is suitable only for tables that have a primary key. |

|   | conflictMode | The policy based on which a primary key conflict or index conflict is handled when data is inserted into a table. | String | No | strict | Valid values: strict: If a conflict occurs, the system reports an error. This is the default value. ignore: If a conflict occurs, the system ignores the conflict. update: If a conflict occurs, the system automatically updates data. This value is suitable for tables that do not have a primary key. This policy reduces the data processing efficiency. upsert: If a conflict occurs, the system automatically updates data in the table. This value is suitable only for tables that have a primary key. |
|---|---|---|---|---|---|---|
|   | maxJoinRow s | The maximum number of rows that can be joined. | Integ er | No | 1024 | None. |

| Dime nsion table- specif ic |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | cache | The cache policy. | String | No | ALL | Valid values: ALL: All data in the dimension table is cached. This is the default value. Before a job runs, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If the system does not find the data record in the cache, the join key does not exist. The system reloads all data in the cache after cache entries expire. LRU: Partial data in the dimension table is cached. The system searches for data in the cache each time a data record is read from the source table. If the data is not found, the system searches for the data in the physical dimension table. None: No data is cached. |
| para meter s |   |   |   |   |   |   |
|   | cacheSize | The maximum number of data records that can be cached. | Long | No | 1000 00 | The cacheSize parameter takes effect only when you set the cache parameter to LRU. |

|   | cacheTTLMs | The cache timeout period. | Long | No | Long. MAX _ VALU E | The setting of cacheTTLMs is related to cache. If the cache parameter is set to LRU, the cacheTTLMs parameter specifies the cache timeout period. By default, cache entries do not expire. If you set the cache parameter to ALL, the cacheTTLMs parameter specifies the interval at which the system refreshes the cache. By default, the cache is not refreshed. Unit: milliseconds. |
|---|---|---|---|---|---|---|

**Data type mappings**

| Data type of AnalyticDB for PostgreSQL | Data type of Realtime Compute for Apache Flink |
|---|---|
| boolean | boolean |
| smallint | int |
| int | int |
| bigint | bigint |
| float | double |
| varchar | varchar |
| text | varchar |
| timestamp | timestamp |
| date | date |

**Sample code**

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
 `name` VARCHAR,
 `age` INT
```

`)`

```
COMMENT 'datagen source table' WITH (
 'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE adbpg_sink (
 name VARCHAR,
 age INT
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
```

);

```
INSERT INTO adbpg_sink SELECT * FROM datagen_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source(
 a INT,
 b BIGINT,
 c STRING,
 `proctime` AS PROCTIME()
```

`)`

```
COMMENT 'datagen source table' WITH (
 'connector' = 'datagen'
```

};

```
CREATE TEMPORARY TABLE adbpg_dim (
 a INT,
 b VARCHAR,
 c VARCHAR
) WITH (
 'connector'='adbpg',
 'url'='jdbc:postgresql://yourAddress:yourPortId/yourDatabaseName',
 'tableName'='yourDatabaseTableName',
 'userName'='yourDatabaseUserName',
 'password'='yourDatabasePassword'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
 a INT,
 b STRING
```

`)`

```
COMMENT 'blackhole sink table' WITH (
 'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.a,H.b FROM datagen_source AS T JOIN adb_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

### 5.15 AnalyticDB for MySQL V3.0 connector

**connector**

This topic describes how to use the AnalyticDB for MySQL V3.0 connector.

**Background information**

AnalyticDB for MySQL V3.0 is a cloud-native enterprise-class data warehousing service that integrates database and big data technologies. AnalyticDB for MySQL supports highthroughput real-time data addition, removal, and modification, low-latency real-time data analysis, and complex extract, transform, and load (ETL) operations. AnalyticDB for MySQL is compatible with upstream and downstream ecosystem tools and can be used to build enterprise-class report systems, data warehouses, and data service engines. The following table describes the capabilities supported by the AnalyticDB for MySQL V3.0 connector.

| Item | Description |
|---|---|
| Table types | Dimension table and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | None |
| Monitoring metrics | None |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

A whitelist is configured. An AnalyticDB for MySQL cluster and an AnalyticDB for MySQL table are created.

**Syntax**

```
CREATE TEMPORARY TABLE adb_table (
  `id` INT,
  `num` BIGINT,
  PRIMARY KEY (`id`) NOT ENFORCED
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
```

);

> **Important:** **The primary key that is specified in the Flink DDL statement must be consistent** **with the primary key of the physical table in the AnalyticDB for MySQL** **database. The primary key must be specified in the Flink DDL statement and** **exist in the physical table in the AnalyticDB for MySQL database at the same** **time. The name of the primary key specified in the Flink DDL statement must** **be the same as the name of the primary key of the physical table. If the primary** **keys are not the same, data may be incorrect.**

**Parameters in the WITH clause**

Common parameters

| Parameter | Descriptio n | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| connector | The type of the sink table. | String | Yes | Non e | Set the value to adb3.0. |
| url | The Java Database Connectivit y (JDBC) URL of the database. | String | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |
| userName | The username that is used to access the database. | String | Yes | Non e | None. |
| password | The password that is used to access the database. | String | Yes | Non e | None. |
| tableName | The name of the table | String | Yes | Non e | None. |
| maxRetryTi mes | The maximum number of retries that are allowed if a data writing or reading attempt fails. | Integer | No | 10 | None. |

Sink table-specific parameters

| Para mete r | Descripti on | Data type | Requ ired | Defau lt value | Remarks |
|---|---|---|---|---|---|

| batch Size | The number of data records that can be written at a time. | Integ er | No | 1000 | This parameter takes effect only after you specify the primary key. |
|---|---|---|---|---|---|
| buffer Size | The maximum number of data records that can be cached in the memory. Write operation s are triggered if the value of the batchSiz e or bufferSiz e paramete r reaches the specified threshold. | Integ er | No | 1000 | This parameter takes effect only after you specify the primary key. |
| flushI nterv alMs | The interval at which the cache is cleared. This value indicates that if the number of cached data records does not reach the upper limit in a specified period of time, all cached data is written to the sink table. | Integ er | No | 3000 | Unit: milliseconds. |

|   | ignor eDele te | Specifies whether to skip delete operation s. | Boole an |   | No |   | false | Valid values: true: The delete operations are ignored. false: The delete operations are not ignored. |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | replac eMod e | Specified whether to use the REPLACE INTO statement to insert data into the table if a primary key is specified in the DDL statement . | Boole an |   |   |   |   | Valid values: true: The REPLACE INTO statement is used to insert data into the table. false: The INSERT INTO ON DUPLICATE KEY UPDATE statement is used to insert data into the table. Note Only AnalyticDB for MySQL V3.1.3.5 or later supports this parameter. This parameter takes effect only when a primary key is specified in the DDL statement. The statement that is used to insert data into the table varies based on whether a primary key is specified and the value of the replaceMode parameter. If a primary key is specified in the DDL statement and the replaceMode parameter is set to true, the REPLACE INTO statement is used. If a primary key is specified in the DDL statement and the replaceMode parameter is set to false, the INSERT INTO ON DUPLICATE KEY UPDATE statement is used. If no primary key is specified in the DDL statement, the INSERT INTO statement is used. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | INSERT INTO ON DUPLICATE |   |   |   |   |
|   |   |   |   |   |   |   |   | KEY UPDATE |   |   |   |   |   |   |   |
|   |   |   |   |   | No |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | REPLACE |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | INSERT |   |   |
|   |   |   |   |   |   |   |   |   |   | INTO ON DUPLICATE KEY |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | UPDATE |   |   |   |   |   |   |
|   |   |   |   |   |   |   | true |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | INSERT |   |   |   |

| exclu deUp dateC olum ns | The fields that are not updated when data that has the same primary key is updated. |   |   |   |   | Separate multiple fields with commas (,). Example: excludeUpdateColumns=column1,column2 . Note This parameter takes effect only when the replaceMode parameter is set to false. If the replaceMode parameter is set to true, the values of the fields specified by this parameter are changed to null. Make sure that the columns that you want to ignore are written in one line and are not wrapped. |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | excludeUpdateColumns=column1,column2 |
|   |   | The fields |   |   |   |   |   |
|   |   |   | String | No | An empty string |   |   |
| conne ction MaxA ctive | The maximum size of the thread pool. |   | Integ er | No | 40 | None. |   |

Dimension table-specific parameters

| Param eter | Descrip tion | Data type | Req uire d | Defaul t value | Remarks |
|---|---|---|---|---|---|

| cache | The cache policy. | String | No | ALL | Valid values: None: No data is cached. LRU: Only specific data in the dimension table is cached. Each time the system receives a data record, the system searches the cache. If the system does not find the record in the cache, the system searches for the data record in the physical dimension table. ALL: All data in the dimension table is cached. This is the default value. Before a job runs, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If the system does not find the data record in the cache, the join key does not exist. The system reloads all data in the cache after cache entries expire. If the amount of data in a remote table is small and a large number of missing keys exist, we recommend that you set this parameter to ALL. The source table and dimension table cannot be associated based on the ON clause. Note If you set the cache parameter to ALL, you must monitor the memory usage of the node to prevent out of memory (OOM) errors. If you set the cache parameter to ALL, you must increase the memory of the node for joining tables because the system asynchronously loads data from the dimension table. The increased memory size is twice that of the remote table. |
|---|---|---|---|---|---|
| cacheSi ze | The maximu m number of data records that can be cached. | Integ er | No | 100000 | You must configure the cacheSize parameter when the cache parameter is set to LRU. |

| cacheT TLMs | The cache timeout period. Unit: milliseco nds. | Integ er | No | Long.M AX VAL _ UE | You must configure the cacheTTLMs parameter when the cache parameter is set to LRU or ALL. If the cache parameter is set to LRU, the cacheTTLMs parameter specifies the cache timeout period. Default value: Long.MAX VALUE . The default value _ indicates that cache entries do not expire. If the cache parameter is set to ALL, the cacheTTLMs parameter specifies the interval at which the system reloads the data in the physical table. Default value: Long.MAX VALUE . The default value _ indicates that data in the physical table is not reloaded. Note If the cache parameter is set to None, you do not need to configure the cacheTTLMs parameter. If the cache parameter is set to None, data is not cached. Therefore, you do not need to configure the cacheTTLMs parameter. |
|---|---|---|---|---|---|
| maxJoi nRows | The maximu m number of results returned after each data record in the primary table is mapped to the data in the dimensi on table. | Integ er | No | 1024 | If you can estimate that each data record in the primary table is mapped to a maximum of n data records in the dimension table, you can configure maxJoinRows='n' to ensure efficient matching in Realtime Compute for Apache Flink. Note When you join the primary table with a dimension table, the number of results returned, after an input data record in the primary table is mapped to the data records in the dimension table, is limited by this parameter. |

**Data type mappings**

| Data type of AnalyticDB for MySQL V3.0 | Data type of Realtime Compute for Apache Flink |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(p, s) or NUMERIC(p, s) | DECIMAL(p, s) |
| VARCHAR | STRING |
| BINARY | BYTES |
| DATE | DATE |
| TIME | TIME |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| POINT | STRING |

**Sample code**

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE adb_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
```

);

```
INSERT INTO adb_sink SELECT * FROM datagen_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source(
  `a` INT,
  `b` VARCHAR,
  `c` STRING,
  `proctime` AS PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE adb_dim (
  `a` INT,
  `b` VARCHAR,
  `c` VARCHAR
) WITH (
  'connector' = 'adb3.0',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  `a` INT,
  `b` VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.a,H.b FROM datagen_source AS T JOIN adb_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

### 5.16 ApsaraDB for HBase connector

**connector**

This topic describes how to use the ApsaraDB for HBase connector.

**Background information**

ApsaraDB for HBase is a cost-effective cloud-based intelligent NoSQL service that provides high scalability and is compatible with open source HBase. ApsaraDB for HBase provides benefits such as low storage costs, high throughput and scalability, and intelligent data processing. ApsaraDB for HBase supports core services of Alibaba such as Taobao recommendations, risk control for Ant Credit Pay, advertising, data dashboards, Cainiao logistics track, Alipay transaction records, and Taobao Mobile messages. ApsaraDB for HBase is a fully managed service that provides enterprise-level capabilities such as the processing of petabytes of data, high concurrency, quick scaling within seconds, low response latency within milliseconds, high availability across data centers, and global distribution. The following table describes the capabilities supported by the ApsaraDB for HBase connector.

| Item | Description |
|---|---|
| Table types | Dimension table and sink table |
| Running modes | Streaming mode |
| Data formats | None |
| Monitoring metrics | Dimension table: None Sink table: numBytesOut, numBytesOutPerSecond, numRecordsOut, numRecordsOutPerSecond, and currentSendTime |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

A whitelist is configured. An HBase cluster and a table are created.

**Usage notes**

You can use the ApsaraDB for HBase connector to connect Realtime Compute for Apache Flink only to an ApsaraDB for HBase database. If you use the ApsaraDB for HBase connector to connect Realtime Compute for Apache Flink to an open source HBase database, data validity cannot be ensured.

**Syntax**

```
CREATE TABLE hbase_table(
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q2 STRING, q3 BIGINT>,
  family3 ROW<q4 DOUBLE, q5 BOOLEAN, q6 STRING>
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
```

); Column families of an ApsaraDB for HBase table must be declared as the ROW type. Each column family name is the field name of a row. In the DDL syntax, the following column families are declared: family1, family2, and family3. A column in a column family corresponds to a field in a row. The column name is the field name. In the DDL syntax, the q2 and q3 columns are declared in the family2 column family. In addition to the fields of the ROW type, only one field of the atomic type, such as STRING and BIGINT, can exist in an ApsaraDB for HBase table. The field of the atomic type is considered as the row key of the table, such as rowkey in the DDL statement. The row key of an ApsaraDB for HBase table must be defined as the primary key of the result table. If no primary key is defined, the row key is used as the primary key. You need to only declare the required column families and columns of an ApsaraDB for HBase table in the result table.

**Parameters in the WITH clause**

Common parameters

| Paramete r | Description | Dat a type | Req uire d | Default value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | Strin g | Yes | None | Set the value to cloudhbase . |
| table- name | The name of the ApsaraDB for HBase table. | Strin g | Yes | None | None. |
| zookeeper .znode.qu orum | The URL that is used to access the ZooKeeper service of ApsaraDB for HBase. | Strin g | Yes | None | None. |
| zookeeper .znode.par ent | The root directory of ApsaraDB for HBase in the ZooKeeper service. | Strin g | No | /hbase | This parameter takes effect only in the ApsaraDB for HBase Standard Edition. |
| userName | The username. | Strin g | No | None | This parameter takes effect only in the ApsaraDB for HBase Performance-enhanced Edition. |
| password | The password. | Strin g | No | None | This parameter takes effect only in the ApsaraDB for HBase Performance-enhanced Edition. |

|   |   | /hbase |
|---|---|---|
| No |   |   |

| haclient.cl uster.id |   | The ID of the ApsaraDB for HBase cluster in high availability (HA) mode. |   | Strin g | No | None | This parameter is required only when you access zone-disaster recovery clusters. This parameter takes effect only in the ApsaraDB for HBase Performance- enhanced Edition. |
|---|---|---|---|---|---|---|---|
| retires.nu mber |   | The number of retries that are allowed for the ApsaraDB for HBase client to connect to the ApsaraDB for HBase database. |   | Inte ger | No | 31 | None. |
| null-string- literal |   | If the data type of a field of ApsaraDB for HBase is STRING and the field data of Realtime Compute for Apache Flink is null, null- string-literal is assigned to the field of ApsaraDB for HBase and is written to the ApsaraDB for HBase database. |   |   | No | null | None. |
|   |   |   | null- | Strin | N |   |   |
|   |   | string-literal |   |   |   |   |   |
|   |   |   |   | g |   |   |   |

Sink table-specific parameters

| Parameter | Description | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| sink.buffer- flush.max- size | The size of data in bytes cached in the memory before data is written to the ApsaraDB for HBase database. A larger value of this parameter improves the write performance of ApsaraDB for HBase but prolongs the write latency and consumes more memory. | Strin g | No | 2MB | Unit: B, KB, MB, or GB. The unit is not case-sensitive. If this parameter is set to 0, no data is cached. |

| sink.buffer- flush.max- rows | The number of data records cached in the memory before data is written to the ApsaraDB for HBase database. A larger value of this parameter improves the write performance of ApsaraDB for HBase but prolongs the write latency and consumes more memory. | Integ er | No | 1000 | If this parameter is set to 0, no data is cached. |
|---|---|---|---|---|---|
| sink.buffer- flush.interv al | The interval at which cached data is written to the ApsaraDB for HBase database. This parameter controls the latency of writing data to the ApsaraDB for HBase database. | Dura tion | No | 1s | Unit: ms, s, min, h, or d. If this parameter is set to 0, periodic data writing is disabled. |
| dynamic.ta ble | Specifies whether to use an ApsaraDB for HBase table that supports dynamic columns. | Bool ean | No | false | Valid values: true: An ApsaraDB for HBase table that supports dynamic columns is used. false: An ApsaraDB for HBase table that supports dynamic columns is not used. |
| sink.ignore- delete | Specifies whether to ignore retraction messages. | Bool ean | No | false | Valid values: true: Retraction messages are ignored. false: Retraction messages are not ignored. |

| sink.sync- write | Specifies whether to write data to ApsaraDB for HBase in synchronous mode. | Bool ean | No | true | Valid values: true: Data is written in synchronous mode. In this mode, data is written in sequence but the write performance is compromised. false: Data is written in asynchronous mode. In this mode, data may not be written in sequence but the write performance is improved. |
|---|---|---|---|---|---|
| sink.buffer- flush.batch -rows | The number of data records that are cached in the memory when data is written to ApsaraDB for HBase in synchronous mode. A larger value improves the write performance of ApsaraDB for HBase, but increases the write latency and memory usage. | Integ er | No | 100 | This parameter takes effect only when the sink.sync-write parameter is set to true. |

Dimension table-specific parameters

| Para mete r | Description | Data type | Requ ired | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
|   |   |   |   |   | Valid values: None: No data is cached. LRU: Only specific data in the dimension table is cached. Each time the system receives a data record, the system searches the cache. If the system does not find the record in the cache, the system searches for the data record in the physical dimension table. Note If this cache policy is used, you must configure the cacheSize and cacheTTLMs parameters. |

| cach e | The cache policy. | Strin g | No | ALL | ALL (default): All data in the dimension table is cached. Before a job runs, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If the system does not find the data record in the cache, the join key does not exist. The system reloads all data in the cache after cache entries expire. |
|---|---|---|---|---|---|
|   |   |   |   |   | Note If the amount of data in a remote table is small and a large number of missing keys exist, we recommend that you set this option to ALL. The source and dimension table cannot be associated based on the ON clause. If you use this cache policy, you must configure the cacheTTLMs and cacheReloadTimeBlackList parameters. If you set the cache parameter to ALL, you must increase the memory of the node for joining tables because the system asynchronously loads data from the dimension table. The increased memory size is twice that of the remote table. |
| cach eSize | The maximum number of rows of data that can be cached. | Long | No | 1000 0 | You can configure this parameter when you set the cache parameter to LRU. |

| cach eTTL Ms | The cache timeout period. Unit: milliseconds. | Long | No | None | The configuration of the cacheTTLMs parameter varies based on the cache parameter. If you set the cache parameter to None, the cacheTTLMs parameter can be left empty. This indicates that cache entries do not expire. If you set the cache option to LRU, the cacheTTLMs option specifies the cache timeout period. By default, cache entries do not expire. If you set the cache parameter to ALL, the cacheTTLMs parameter specifies the interval at which the system reloads the cache. By default, the cache is not reloaded. |
|---|---|---|---|---|---|
| cach eEmp ty | Specifies whether to cache empty results. | Boole an | No | true | None. |
| cach eRelo adTi meBl ackLi st | The time periods during which cache is not refreshed. This parameter takes effect when the cache parameter is set to ALL. The cache is not refreshed during the periods of time that you specify for this parameter. This parameter is suitable for large-scale online promotional events such as Double 11. | Strin g | No | None | The following example shows the format of the values: 2017-10-24 14:00 -> 2017- 10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00. Use delimiters based on the following rules: Separate multiple time periods with commas (,). Separate the start time and end time of each time period with an arrow (->) that is a combination of a hyphen (-) and a closing angle bracket (>). |

| cach eSca nLimi t | The number of rows that the remote procedure call (RPC) server returns to a client when the server reads full data from an ApsaraDB for HBase dimension table. | Integ er | No | 100 | This parameter is available only when you set the cache parameter to ALL. |
|---|---|---|---|---|---|

**Data type mappings**

A value of a data type of Realtime Compute for Apache Flink is converted into a byte array by using `org.apache.hadoop.hbase.util.Bytes` in an ApsaraDB for HBase table. The decoding process varies based on the following scenarios: If the data type of Realtime Compute for Apache Flink is a non-STRING type and a value in the ApsaraDB for HBase table is an empty byte array, the value is decoded as null. If the data type of Realtime Compute for Apache Flink is the STRING type and a value in the ApsaraDB for HBase dimension table is the byte array specified by `null-string-literal` , the value is decoded as null.

| Flink SQL data type | Function used to convert a value into bytes for ApsaraDB for HBase | Function used to read bytes from ApsaraDB for HBase |
|---|---|---|
| CHAR | byte[] toBytes(String s) | String toString(byte[] b) |
| VARCHAR |   |   |
| STRING |   |   |
| BOOLEAN | byte[] toBytes(boolean b) | boolean toBoolean(byte[] b) |
| BINARY | byte[] | byte[] |
| VARBINARY |   |   |
| DECIMAL | byte[] toBytes(BigDecimal v) | BigDecimal toBigDecimal(byte[] b) |
| TINYINT | new byte[] { val } | bytes[0] |
| SMALLINT | byte[] toBytes(short val) | short toShort(byte[] bytes) |

| INT | byte[] toBytes(int val) |   | int toInt(byte[] bytes) |   |   |
|---|---|---|---|---|---|
| BIGINT | byte[] toBytes(long val) |   | long toLong(byte[] bytes) |   |   |
| FLOAT | byte[] toBytes(float val) |   | float toFloat(byte[] bytes) |   |   |
| DOUBLE | byte[] toBytes(double val) |   | double toDouble(byte[] bytes) |   |   |
| DATE | Converts a date into an INT value that represents the number of days since January 1, 1970 and then into a byte array by using byte[] toBytes(int val) . |   | Converts a byte array of the ApsaraDB for HBase database into the INT data type by using int toInt(byte[] bytes) . The value of the INT data type represents the number of days since January 1, 1970. |   |   |
|   | val) |   |   |   |   |
| TIME | Converts a time into an INT value that represents the number of milliseconds since 00:00:00 and then into a byte array by using byte[] toBytes(int val) . |   | Converts a byte array of the ApsaraDB for HBase database into the INT data type by using int toInt(byte[] bytes) . The value of the INT data type represents the number of milliseconds since 00:00:00. |   |   |
|   | val) |   |   |   |   |
| TIMESTAMP | Converts a timestamp into a LONG value that represents the number of milliseconds since 00:00:00 on January 1, 1970 and then into a byte array by using byte[] toBytes(long val) . |   | Converts a byte array of the ApsaraDB for HBase database into the LONG data type by using long toLong(byte[] bytes) . The value of the LONG data type represents the number of milliseconds since 00:00:00 on January 1, 1970. |   |   |
|   |   |   |   | long |   |
|   |   | ary by | toLong(byte[] bytes) |   |   |

| int toInt(byte[] |   |
|---|---|

| byt | e[] toBytes(int | by | tes) |
|---|---|---|---|

| int toInt(byte[] |   |
|---|---|

| e[] toBytes(int | by |
|---|---|

**Sample code**

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source (
  a INT,
  b BIGINT,
  c STRING,
  `proc_time` AS PROCTIME()
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE hbase_dim (
  rowkey INT,
  family1 ROW<col1 INT>,
  family2 ROW<col1 STRING, col2 BIGINT>,
  family3 ROW<col1 DOUBLE, col2 BOOLEAN, col3 STRING>
) WITH (
  'connector' = 'cloudhbase',
  'table-name' = '<yourTableName>',
  'zookeeper.quorum' = '<yourZookeeperQuorum>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  a INT,
  f1c1 INT,
  f3c3 STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink
     SELECT a, family1.col1 as f1c1,  family3.col3 as f3c3 FROM datagen_source
JOIN hbase_dim FOR SYSTEM_TIME AS OF datagen_source.`proc_time` as h ON datagen_sourc e.a = h.rowkey;
```

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
  rowkey INT,
  f1q1 INT,
  f2q1 STRING,
  f2q2 BIGINT,
  f3q1 DOUBLE,
  f3q2 BOOLEAN,
  f3q3 STRING
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE hbase_sink (
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q1 STRING, q2 BIGINT>,
  family3 ROW<q1 DOUBLE, q2 BOOLEAN, q3 STRING>,
  PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
```

);

```
INSERT INTO hbase_sink SELECT rowkey, ROW(f1q1), ROW(f2q1, f2q2), ROW(f3q1, f3q2, f3q3) FROM datagen_source;
```

Sample code for a sink table that supports dynamic columns

```
CREATE TEMPORARY TABLE datagen_source (
  id INT,
  f1hour STRING,
  f1deal BIGINT,
  f2day STRING,
  f2deal BIGINT
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE hbase_sink (
  rowkey INT,
  f1 ROW<`hour` STRING, deal BIGINT>,
  f2 ROW<`day` STRING, deal BIGINT>
) WITH (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>',
  'dynamic.table'='true'
```

);

```
INSERT INTO hbase_sink SELECT id, ROW(f1hour, f1deal), ROW(f2day, f2deal) FROM datagen_source;
```

If **dynamic.table** is set to true, an ApsaraDB for HBase table that supports dynamic columns is used. Two fields must be declared in the rows that correspond to each column family. The value of the first field indicates the dynamic column, and the value of the second field indicates the value of the dynamic column. For example, the datagen_source table contains a row of data. The row of data indicates that the ID of the commodity is 1, the transaction amount of the commodity between 10:00 and 11:00 is 100, and the transaction amount of the commodity on July 26, 2020 is 10000. In this case, a row whose rowkey is 1 is inserted into the ApsaraDB for HBase table. **f1:10** is 100, and **f2:2020-7-26** is 10000.

### 5.17 Lindorm connector

This topic describes how to use the Lindorm connector.

**Background information**

Lindorm is a cloud-native multi-mode hyper-converged database service that is designed and optimized for Internet of Things (IoT), Internet, and Internet of Vehicles (IoV). Lindorm is suitable for various scenarios, such as logging, monitoring, billing, advertising, social networking, travel, and risk management. Lindorm is also one of the database services that support the core business of Alibaba Cloud. Lindorm provides the following features: Supports unified access and processing of various data, such as wide tables, time series, text, objects, streams, and spaces. Compatible with multiple standard interfaces, such as SQL, Apache HBase, Apache Cassandra, Amazon S3, Time Series Database (TSDB), Hadoop Distributed File System (HDFS), Apache Solr, and Kafka. Lindorm can also be seamlessly integrated with third-party ecosystem tools. The following table describes the capabilities supported by the Lindorm connector.

| Item | Description |
|---|---|
| Table types | Dimension table and sink table |
| Running modes | Streaming mode |
| Data formats | None |
| Monitoring metrics | Metrics for dimension tables: none Metrics for sink tables: numBytesOut numBytesOutPerSecond numRecordsOut numRecordsOutPerSecond |

| API types | SQL |
|---|---|
| Lindorm engine | LindormTable |
| Data updates or deletion in a sink table | Yes |

**Prerequisites**

A LindormTable engine and a Lindorm table are created. A network connection is established between the Lindorm cluster and Realtime Compute for Apache Flink. For example, the Lindorm cluster and Realtime Compute for Apache Flink reside in the same virtual private cloud (VPC).

**Syntax**

```
CREATE TABLE white_list ( id varchar, name varchar, age int, PRIMARY KEY (id) NOT ENFORCED ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>'
```

);

**Parameters in the WITH clause**

| Type | Parame ter | Description | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|---|
|   | connecto r | The type of tables. | Strin g | Yes | None | Set the value to lindorm. |
|   | seedserv er | The endpoint of the Lindorm server. | Strin g | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|   | namespa ce | The namespace of the Lindorm database. | Strin g | Yes | None | None. |

|   | usernam e | The username that is used to access the Lindorm database. | Strin g | Yes | None | None. |
|---|---|---|---|---|---|---|
| Comm on param eters |   |   |   |   |   |   |
|   | passwor d | The password that is used to access the Lindorm database. | Strin g | Yes | None | None. |
|   | tableNa me | The name of the Lindorm table. | Strin g | Yes | None | None. |
|   | columnF amily | The name of the column family of the Lindorm table. | Strin g | Yes | None | If the column family name is not specified when you create the Lindorm table, enter the default column family name f. |
|   | retryInte rvalMs | The interval at which the read operation is retried when data reading fails. | Integ er | No | 1000 | Unit: milliseconds. |
|   | maxRetr yTimes | The maximum number of retries for reading or writing data. | Integ er | No | 5 | None. |
|   | bufferSiz e | The number of data records that can be written at a time. | Integ er | No | 500 | None. |
|   | flushInte rvalMs | The interval at which data is written to the table when the amount of data is small. | Integ er | No | 2000 | Unit: milliseconds. |

| Sink table- specifi c param eters |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | ignoreDe lete | Specifies whether to skip delete operations. | Bool ean | No | false | Valid values: true: Delete operations are ignored. false: Delete operations are not ignored. This is the default value. |
|   | dynamic ColumnS ink | Specifies whether to enable the dynamic table feature. | Bool ean | No | false | Valid values: true: enables the dynamic table feature. false: disables the dynamic table feature. This is the default value. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.2 or later supports this parameter. |
|   | partition edJoin | Specifies whether to use the JoinKey for partitioning. | Bool ean | No | false | Valid values: true: The JoinKey is used for partitioning. Data is distributed to each JOIN node to improve the cache hit rate. false (default): The JoinKey is not used for partitioning. |
|   | shuffleE mptyKey | Specifies whether to randomly shuffle empty upstream keys to downstream nodes. | Bool ean | No | false | Valid values: true: The system randomly shuffles empty upstream keys to downstream nodes. false (default): The system shuffles empty upstream keys to the first parallel thread of each downstream node. The first parallel thread is numbered 0. |
|   | cache | The cache policy. | Strin g | No | None | Valid values: None (default): No data is cached. LRU: Only recently accessed data in the dimension table is cached. If you set the cache parameter to LRU, you must configure the cacheSize and cacheTTLMs parameters. |

| Dimen sion table- specifi c param eters |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | cacheSiz e | The number of rows of data that can be cached. | Integ er | No | 1000 | If you set the cache parameter to LRU, you can configure the cacheSize parameter. |
|   | cacheTT LMs | The cache timeout period. | Integ er | No | None | Unit: milliseconds. If you set the cache parameter to LRU, you can configure the cacheTTLMs parameter. By default, cache entries do not expire. |
|   | cacheEm pty | Specifies whether to cache the JOIN queries whose return results are empty. | Bool ean | No | true | None. |
|   | async | Specifies whether to enable data synchronizatio n in asynchronous mode. | Bool ean | No | false | Valid values: true: enables data synchronization in asynchronous mode. false: disables data synchronization in asynchronous mode. This is the default value. |
|   | asyncLin dormRpc Timeout Ms | The timeout period when data is requested in asynchronous mode. | Integ er | No | 3000 00 | Unit: milliseconds. |

**Dynamic table**

The dynamic table feature is suitable for scenarios in which no columns are specified in a table and columns are created and inserted into the table based on the deployment status. For example, you use days as the primary key and hours as columns to calculate the hourly transaction volume per day. Data for each hour is dynamically generated. The following table shows the dynamic table.

| Primary key | Column name: 00:00 | Column name: 01:00 |
|---|---|---|
| 2025-06-01 | 45 | 32 |
| 2025-06-02 | 76 | 34 |

The dynamic table must comply with the following DDL rules: The first several columns are defined as the primary key. The value of the first column in the last two columns is used as the column name, the value of the last column is used as the value of the previous column, and the data type of the last two columns must be VARCHAR. Sample code:

```
CREATE TABLE lindorm_dynamic_output( pk1varchar, pk2varchar, pk3varchar, c1varchar, c2varchar, PRIMARYKEY(pk1,pk2,pk3)notenforced ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>'
```

); In the preceding example, pk1, pk2, and pk3 are used as the primary key. c1 and c2 are the two columns that are required for the dynamic table and must be the last two columns. Except for c1 and c2, columns that are not used as the primary key are not allowed. Each time data is written to the Lindorm sink table, a column is added to or modified in the data record that corresponds to the values <pk1, pk2, pk3> of the primary key. The value of c1 is used as the name of the column, and the value of c2 is used as the value of the column. Each time a data record is received, only the value in one column is added or changed. The values of other columns remain unchanged.

**Data type mappings**

All data in Lindorm is in the binary format. The following table shows how to convert data into bytes of binary data or parse bytes of binary data based on the data type of a field in Realtime Compute for Apache Flink.

| Data type of Flink SQL | Method used to convert data into bytes for Lindorm | Method used to parse bytes from Lindorm |
|---|---|---|
| CHAR | org.apache.flink.table.data.StringD ata::toBytes | org.apache.flink.table.data.StringData::fromByte s |
| VARCHAR |   |   |
| BOOLEAN | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(boolean) | com.alibaba.lindorm.client.core.utils.Bytes::toBi gDecimal |
| BINARY | Directly convert data into bytes. | Directly return bytes. |
| VARBINARY |   |   |

| DECIMAL | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(BigDecimal) | com.alibaba.lindorm.client.core.utils.Bytes::toBi gDecimal |
|---|---|---|
| TINYINT | Directly encapsulate data into the first byte of byte[]. | Directly return bytes[0]. |
| SMALLINT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(short) | com.alibaba.lindorm.client.core.utils.Bytes::toSh ort |
| INT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int) | com.alibaba.lindorm.client.core.utils.Bytes::toInt |
| BIGINT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(long) | com.alibaba.lindorm.client.core.utils.Bytes::toLo ng |
| FLOAT | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(float) | com.alibaba.lindorm.client.core.utils.Bytes::toFlo at |
| DOUBLE | com.alibaba.lindorm.client.core.util s.Bytes::toBytes(double) | com.alibaba.lindorm.client.core.utils.Bytes::toDo uble |
| DATE | Call com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int) after the number of days since January 1, 1970 is obtained. | Call com.alibaba.lindorm.client.core.utils.Bytes::toInt to obtain the number of days since January 1, 1970. |
| TIME | Call com.alibaba.lindorm.client.core.util s.Bytes::toBytes(int) after the number of milliseconds since 00:00:00 of the current day is obtained. | Call com.alibaba.lindorm.client.core.utils.Bytes::toInt to obtain the number of milliseconds since 00:00:00 of the current day. |
| TIMESTAMP | Call com.alibaba.lindorm.client.core.util s.Bytes::toBytes(long) after the number of milliseconds since 00:00:00 on January 1, 1970 is obtained. | Call com.alibaba.lindorm.client.core.utils.Bytes::toLo ng to obtain the number of milliseconds since 00:00:00 on January 1, 1970. |

**Sample code**

```
CREATE TEMPORARY TABLE example_source(
 id INT,
 proc_time AS PROCTIME()
) WITH (
 'connector' = 'datagen',
 'number-of-rows' = '10',
 'fields.id.kind' = 'sequence',
 'fields.id.start' = '0',
 'fields.id.end' = '9'
```

);

```
CREATE TEMPORARY TABLE lindorm_hbase_dim(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_dim_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
```

);

```
CREATE TEMPORARY TABLE lindorm_hbase_sink(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_sink_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
```

);

```
INSERT INTO lindorm_hbase_sink SELECT example_source.id as id, lindorm_hbase_dim.name as name, lindorm_hbase_dim.birth as birth FROM example_source JOIN lindorm_hbase_dim FOR SYSTEM_TIME AS OF PROCTIME() ON example_ source.id = lindorm_hbase_dim.id;
```

### 5.18 ApsaraMQ for RocketMQ connector

**connector**

This topic describes how to use the ApsaraMQ for RocketMQ connector.

**Important**

> ApsaraMQ for RocketMQ 4.x Standard Edition can process up to 5,000 messages per second. If you use ApsaraMQ for RocketMQ 4.x Standard Edition as the messaging middleware to connect to Realtime Compute for Apache Flink, deployments of Realtime Compute for Apache Flink may be unstable. Therefore, we recommend that you evaluate the impact if you want to use or plan to use ApsaraMQ for RocketMQ 4.x Standard Edition as the messaging middleware to connect to Realtime Compute for Apache Flink. We recommend that you use another messaging middleware service, such as Kafka, Simple Log Service (SLS), or DataHub, instead of ApsaraMQ for RocketMQ 4.x Standard Edition as the messaging middleware based on your business requirements. If you must use ApsaraMQ for RocketMQ 4.x Standard Edition to process a large number of messages, contact technical support to increase the number of messages that can be processed by ApsaraMQ for RocketMQ 4.x Standard Edition per second.

**Background information**

ApsaraMQ for RocketMQ is a distributed messaging middleware service developed by Alibaba Cloud based on Apache RocketMQ. The service provides low latency, high concurrency, high availability, and high reliability. ApsaraMQ for RocketMQ provides the asynchronous decoupling and load shifting features for distributed application systems. The service also supports features for Internet applications, including massive message accumulation, high throughput, and reliable retry. The following table describes the capabilities supported by the ApsaraMQ for RocketMQ connector.

| Item | Description |
|---|---|
| Table types | Source table and sink table |
| Running modes | Streaming mode |
| Data formats | CSV and binary formats |
| Monitoring metrics | Source table: numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime Sink table: numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |

| API types | DataStream API and SQL API. Only ApsaraMQ for RocketMQ 4.x instances support DataStream APIs. |
|---|---|
| Data updates or deletion in a sink table | Data cannot be deleted from a sink table. Data can only be updated or inserted into a sink table. |

**Features**

The following tables describe the fields that are supported for an ApsaraMQ for RocketMQ source table and an ApsaraMQ for RocketMQ result table. Fields in an ApsaraMQ for RocketMQ source table

| Field | Field data type | Description |
|---|---|---|
| topic | VARCHAR METADATA VIRTUAL | The topic of the message. |
| queue-id | INT METADATA VIRTUAL | The ID of the queue in which an ApsaraMQ for RocketMQ message is placed. |
| queue-offset | BIGINT METADATA VIRTUAL | The consumption offset of an ApsaraMQ for RocketMQ message. |
| msg-id | VARCHAR METADATA VIRTUAL | The ID of an ApsaraMQ for RocketMQ message. |
| store- timestamp | TIMESTAMP(3) METADATA VIRTUAL | The time at which an ApsaraMQ for RocketMQ message is stored. |
| born- timestamp | TIMESTAMP(3) METADATA VIRTUAL | The time at which an ApsaraMQ for RocketMQ message is generated. |
| keys | VARCHAR METADATA VIRTUAL | The keys of an ApsaraMQ for RocketMQ message. |
| tags | VARCHAR METADATA VIRTUAL | The tags of an ApsaraMQ for RocketMQ message. |

Fields in an ApsaraMQ for RocketMQ sink table

| Field | Field data type | Description |
|---|---|---|
| keys | VARCHAR METADATA | The keys of an ApsaraMQ for RocketMQ message. |

| tags | VARCHAR METADATA | The tags of an ApsaraMQ for RocketMQ message. |
|---|---|---|

**Prerequisites**

ApsaraMQ for RocketMQ resources are created.

**Limits**

Only Realtime Compute for Apache Flink that uses VVR 8.0.3 or later supports ApsaraMQ for RocketMQ 5.x instances. In Realtime Compute for Apache Flink that uses the VVR version earlier than 6.0.2, the deployment parallelism for an ApsaraMQ for RocketMQ source table must be less than or equal to the number of partitions in a topic of ApsaraMQ for RocketMQ. This limit is removed from Realtime Compute for Apache Flink that uses VVR 6.0.2 or later. You can set the deployment parallelism to a value that is greater than the number of partitions in the topic of ApsaraMQ for RocketMQ in advance. You do not need to manually adjust the deployment parallelism when an ApsaraMQ for RocketMQ instance is scaled in. The ApsaraMQ for RocketMQ connector uses pull consumers to consume messages. All subtasks share data consumption.

**Syntax**

```
CREATE TABLE mq_source(
  x varchar,
  y varchar,
  z varchar
) WITH (
  'connector' = 'mq5',
  'topic' = '<yourTopicName>',
  'endpoint' = '<yourEndpoint>',
  'consumerGroup' = '<yourConsumerGroup>'
```

);

**Parameters in the WITH clause**

Common parameters

| Parame ter | Description | Data type | Require d | Default value | Remarks |
|---|---|---|---|---|---|
| connect or | The type of the connector. | String | Yes | None | ApsaraMQ for RocketMQ 4.x: Set the value to mq . ApsaraMQ for RocketMQ 5.x: Set the value to mq5 . |
| endPoin t | The endpoint of ApsaraMQ for RocketMQ. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |

| topic | The name of the topic. | String | Yes | None | None. |
|---|---|---|---|---|---|
| accessId | ApsaraMQ for RocketMQ 4.x: the AccessKey ID of your Apsara Stack tenant account. ApsaraMQ for RocketMQ 5.x: the username of the ApsaraMQ for RocketMQ instance. The username of the ApsaraMQ for RocketMQ instance. | String | Apsar aMQ for Rocket MQ 4.x: yes Apsar aMQ for Rocket MQ 5.x: no | None | None. |
| accessK ey | ApsaraMQ for RocketMQ 4.x: the AccessKey secret of your Apsara Stack tenant account. ApsaraMQ for RocketMQ 5.x: the password of the ApsaraMQ for RocketMQ instance. | String | Apsar aMQ for Rocket MQ 4.x: yes Apsar aMQ for Rocket MQ 5.x: no | None | None. |

| tag | The tag of the message that is subscribed to or written. | String | No | None | For an ApsaraMQ for RocketMQ source table, only a single tag can be read. For an ApsaraMQ for RocketMQ result table, you can configure multiple tags. Separate multiple tags with commas (,). Note For an ApsaraMQ for RocketMQ result table, only ApsaraMQ for RocketMQ 4.x instances are supported. If you use an ApsaraMQ for RocketMQ 5.x instance, you can specify the tag of a message by using the fields in an ApsaraMQ for RocketMQ result table. |
|---|---|---|---|---|---|
| encodin g | The encoding format. | String | No | UTF-8 | None. |
| instance ID | The ID of the ApsaraMQ for RocketMQ instance. | String | No | None | If the ApsaraMQ for RocketMQ instance does not use a separate namespace, the instanceID parameter cannot be configured. If the ApsaraMQ for RocketMQ instance uses a separate namespace, you must configure the instanceID parameter. Note Only ApsaraMQ for RocketMQ 4.x instances support this parameter. If you use an ApsaraMQ for RocketMQ 5.x instance, you do not need to configure this parameter. |

Source table-specific parameters

| Parameter | Descriptio n | Data type | Requi red | Default value | Remarks |
|---|---|---|---|---|---|
| consumerGr oup | The name of the consumer group. | String | Yes | None | None. |
| pullInterval Ms | The wait interval of the source if no data can be consumed from the upstream storage system. | Int | Yes | None | The default value indicates that the cache is never refreshed. Unit: milliseconds. You cannot configure the rate of reading ApsaraMQ for RocketMQ messages because no throttling mechanism is available. Note Only ApsaraMQ for RocketMQ 4.x instances support this parameter. If you use an ApsaraMQ for RocketMQ 5.x instance, you do not need to configure this parameter. |
| timeZone | The time zone of the instance. | String | No | None | Example: Asia or Shanghai. |
| startTimeMs | The time to start reading data. | Long | No | None | The timestamp. Unit: milliseconds. |
| startMessag eOffset | The start offset to consume messages. | Int | No | None | This parameter is optional. If you configure this parameter, messages are consumed from the time specified by this parameter. |
| lineDelimite r | The row delimiter used when a message block is parsed. | String | No | \n | None. |

| fieldDelimite r | The field delimiter. | String | No | \u0001 | The delimiter varies based on the mode in which the terminal of ApsaraMQ for RocketMQ works. In read-only mode, the delimiter is \u0001 . This is the default mode. In this mode, the delimiter is not visible. In edit mode, the delimiter is ^A . |
|---|---|---|---|---|---|
| lengthCheck | The rule for checking the number of fields parsed from a row of data. | Int | No | NONE | Valid values: NONE: This is the default value. If the number of fields that are parsed from a row of data is greater than the specified number of fields, data is extracted from left to right based on the order of specified fields. If the number of fields that are parsed from a row of data is less than the specified number of fields, this row of data is skipped. SKIP: If the number of fields that are parsed from a row of data does not match the number of specified fields, this row of data is skipped. EXCEPTION: If the number of fields that are parsed from a row of data is different from the specified number of fields, an exception is reported. PAD: Data is padded from left to right based on the order of defined fields. If the number of fields that are parsed from a row of data is greater than the specified number of fields, data is extracted from left to right based on the order of specified fields. If the number of fields parsed from a row of data is less than the number of defined fields, the values of the missing fields are padded with null. |

|   |   |   |   |   | Note SKIP, EXCEPTION, and PAD are optional values. |
|---|---|---|---|---|---|
| columnError Debug | Specifies whether to enable debugging. | Boolea n | No | false | If you set this parameter to true, a log entry that indicates a parsing exception is returned. |
| pullBatchSiz e | The maximum number of messages that can be pulled at a time. | Int | No | 64 | Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |

Sink table-specific parameters

| Paramete r | Description | Data type | Requir ed | Default value | Remarks |
|---|---|---|---|---|---|
| producerG roup | The name of the producer group. | String | Yes | None | None. |
| retryTimes | The number of retries for writing data to the table. | Int | No | 10 | None. |
| sleepTime Ms | The retry interval. | Long | No | 5000 | None. |

| partitionFi eld | The partition key column. You can specify a field as a partition key column. | String | No | None | This parameter is required if the mode parameter is set to partition . |
|---|---|---|---|---|---|

**Data type mappings**

| Data type of Flink | Data type of ApsaraMQ for RocketMQ |
|---|---|
| VARCHAR | STRING |

**Sample code**

Sample code for a source table CSV format For example, a CSV message is recorded in the following format:

```
1,name,male 2,name,female
```

> **Note:** An ApsaraMQ for RocketMQ message can contain zero to more data records. Multiple data records are separated by \n .

You can use the following DDL statement to declare an ApsaraMQ for RocketMQ source table in a Realtime Compute for Apache Flink deployment: RocketMQ 5.x

```
CREATE TABLE mq_source(
  id varchar,
  name varchar,
  gender varchar,
  topic varchar metadata virtual
) WITH (
  'connector' = 'mq5',
  'topic' = 'mq-test',
  'endpoint' = '<yourEndpoint>',
  'consumerGroup' = 'mq-group',
  'fieldDelimiter' = ','
```

); RocketMQ 4.x

```
CREATE TABLE mq_source(
  id varchar,
  name varchar,
  gender varchar,
  topic varchar metadata virtual
) WITH (
  'connector' = 'mq',
  'topic' = 'mq-test',
  'endpoint' = '<yourEndpoint>',
  'pullIntervalMs' = '1000',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'consumerGroup' = 'mq-group',
  'fieldDelimiter' = ','
```

); Binary format RocketMQ 5.x

```
CREATE TEMPORARY TABLE source_table (
  mess varbinary
) WITH (
  'connector' = 'mq5',
  'endpoint' = '<yourEndpoint>',
  'topic' = 'mq-test',
  'consumerGroup' = 'mq-group'
```

);

```
CREATE TEMPORARY TABLE out_table (
  commodity varchar
) WITH (
  'connector' = 'print'
```

);

```
INSERT INTO out_table select
  cast(mess as varchar)
FROM source_table;
```

RocketMQ 4.x

```
CREATE TEMPORARY TABLE source_table (
  mess varbinary
) WITH (
  'connector' = 'mq',
  'endpoint' = '<yourEndpoint>',
  'pullIntervalMs' = '500',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'topic' = 'mq-test',
  'consumerGroup' = 'mq-group'
```

);

```
CREATE TEMPORARY TABLE out_table (
  commodity varchar
) WITH (
  'connector' = 'print'
```

);

```
INSERT INTO out_table select
  cast(mess as varchar)
FROM source_table;
```

Sample code for a sink table Create a sink table RocketMQ 5.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR
) WITH (
  'connector'='mq5',
  'endpoint'='<yourEndpoint>',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
```

); ApsaraMQ for RocketMQ 4.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR
) WITH (
  'connector'='mq',
  'endpoint'='<yourEndpoint>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
```

);

> **Note:** If the messages of your ApsaraMQ for RocketMQ instance are in the binary format, only one field can be defined in the DDL statement and the field must be of the VARBINARY data type.

Create an ApsaraMQ for RocketMQ result table in which the keys and tags fields are defined as the `keys` and `tags` of ApsaraMQ for RocketMQ messages. RocketMQ 5.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR,
  keys VARCHAR METADATA,
  tags VARCHAR METADATA
) WITH (
  'connector'='mq5',
  'endpoint'='<yourEndpoint>',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
```

); RocketMQ 4.x

```
CREATE TABLE mq_sink (
  id INTEGER,
  len BIGINT,
  content VARCHAR,
  keys VARCHAR METADATA,
  tags VARCHAR METADATA
) WITH (
  'connector'='mq',
  'endpoint'='<yourEndpoint>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'topic'='<yourTopicName>',
  'producerGroup'='<yourGroupName>'
```

);

**DataStream API**

> **Important:** Only ApsaraMQ for RocketMQ 4.x instances support DataStream APIs.
> If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink.

The VVR engine of Realtime Compute for Apache Flink provides `MetaQSource` for reading data from ApsaraMQ for RocketMQ and the implementation class `MetaQOutputFormat` of `OutputFormat` for writing data to ApsaraMQ for RocketMQ. The following sample code shows how to use the ApsaraMQ for RocketMQ DataStream connector to read data from and write data to ApsaraMQ for RocketMQ:

```
/**
 * A demo that illustrates how to consume messages from RocketMQ, convert
 * messages, then produce messages to RocketMQ.
```

`*/`

```java
public class RocketMQDataStreamDemo2 {
```

```
    public static final String ENDPOINT = "<yourEndpoint>";
    public static final String ACCESS_ID = "<accessID>";
    public static final String ACCESS_KEY = "<accessKey>";
    public static final String INSTANCE_ID = "<instanceID>";
    public static final String SOURCE_TOPIC = "<sourceTopicName>";
    public static final String CONSUMER_GROUP = "<consumerGroup>";
    public static final String SINK_TOPIC = "<sinkTopicName>";
    public static final String PRODUCER_GROUP = "<producerGroup>";
    public static void main(String[] args) throws Exception {
        // Sets up the streaming execution environment
        Configuration config = new Configuration();
       // This is only required for local testing
        config.setString("classloader.parent-first-patterns.additional",
"com.alibaba.ververica.connectors.metaq.source.reader.deserializer.MetaQRecordDeserializa onSchema;com.alibaba.ververica.connector.mq.shaded.");
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment(config);
        // Creates and adds RocketMQ source.
        env.fromSource(createRocketMQSource(), WatermarkStrategy.noWatermarks(),
"source")
                // Converts message body to upper case.
                .map(RocketMQDataStreamDemo2::convertMessages)
                // Creates and adds RocketMQ sink.
                .addSink(new OutputFormatSinkFunction<>(createRocketMQOutputFormat()))
                .name(RocketMQDataStreamDemo2.class.getSimpleName());
        // Compiles and submits job.
        env.execute("RocketMQ connector end-to-end DataStream demo");
```

`}`

```java
    private static MetaQSource<MessageExt> createRocketMQSource() {
        Properties mqProperties = createMQProperties();
        return new MetaQSource<>(SOURCE_TOPIC,
                CONSUMER_GROUP,
                null, // always null
                null, // tag of the messages to consumer
                Long.MAX_VALUE, // stop timestamp in milliseconds
                -1, // Start timestamp in milliseconds. Set to -1 to disable starting fr
om offset.
                0, // Start offset.
                300_000, // Partition discover interval.
                mqProperties,
                Boundedness.CONTINUOUS_UNBOUNDED,
                new MyDeserializationSchema());
```

`}`

```java
    private static MetaQOutputFormat createRocketMQOutputFormat() {
        return new MetaQOutputFormat.Builder()
                .setTopicName(SINK_TOPIC)
                .setProducerGroup(PRODUCER_GROUP)
                .setMqProperties(createMQProperties())
```

```
                .build();
```

`}`

```java
    private static Properties createMQProperties() {
        Properties properties = new Properties();
        properties.put(PROPERTY_ONS_CHANNEL, "ALIYUN");
        properties.put(NAMESRV_ADDR, ENDPOINT);
        properties.put(PROPERTY_ACCESSKEY, ACCESS_ID);
        properties.put(PROPERTY_SECRETKEY, ACCESS_KEY);
        properties.put(PROPERTY_ROCKET_AUTH_ENABLED, true);
        properties.put(PROPERTY_INSTANCE_ID, INSTANCE_ID);
        return properties;
```

`}`

```java
    private static List<MessageExt> convertMessages(MessageExt messages) {
        return Collections.singletonList(messages);
```

`}`

```java
    public static class MyDeserializationSchema implements
MetaQRecordDeserializationSchema<MessageExt> {
        @Override
        public void deserialize(List<MessageExt> list, Collector<MessageExt> collector)
```

`{`

```
            for (MessageExt messageExt : list) {
                collector.collect(messageExt);
```

`}` `}`

```java
        @Override
        public TypeInformation<MessageExt> getProducedType() {
            return TypeInformation.of(MessageExt.class);
```

`}` `}` `}` `}` `}`

### 5.19 ApsaraDB for Redis connector

**connector**

This topic describes how to use the ApsaraDB for Redis connector.

**Background information**

ApsaraDB for Redis is a database service compatible with the open source Redis protocol and provides hybrid storage of memory and disks. Based on reliable hot standby architectures and scalable cluster architectures, ApsaraDB for Redis is suitable for scenarios that require flexible configuration changes, high throughput, and low latency. The following table describes the capabilities supported by the ApsaraDB for Redis connector.

| Item | Description |
|---|---|
| Table types | Dimension table and sink table |
| Running modes | Streaming mode |
| Data formats | String |
| Monitoring metrics | Metrics for dimension tables: none Metrics for sink tables: numBytesOut numRecordsOutPerSecond numBytesOutPerSecond currentSendTime |
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

A whitelist is configured. An ApsaraDB for Redis instance is created.

**Limits**

The ApsaraDB for Redis connector supports only the best-effort delivery and does not support the exactly-once semantics. You must ensure semantic idempotence. Limits on only dimension tables ApsaraDB for Redis dimension tables can read only data of the STRING and HASHMAP types from ApsaraDB for Redis databases. The fields in ApsaraDB for Redis dimension tables must be of the STRING type. You must declare only one primary key for an ApsaraDB for Redis dimension table. When you join an ApsaraDB for Redis dimension table with another table, the ON clause must contain the equality conditions for primary key fields.

**Syntax**

```
CREATE TABLE redis_table (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED -- Required.
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'mode' = 'STRING' -- This parameter is required for result tables.
```

);

**Parameters in the WITH clause**

Common parameters

| Param eter | Description | Data type | Requi red | Default value | Remarks |
|---|---|---|---|---|---|
| connec tor | The type of tables. | String | Yes | None | Set the value to redis. |
| host | The IP address that is used to access the ApsaraDB for Redis database. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| port | The port number that is used to access the ApsaraDB for Redis database. | Int | No | 6379 | None. |
| passw ord | The password that is used to access the ApsaraDB for Redis database. | String | No | An empty string | None. |
| dbNu m | The sequence number of the ApsaraDB for Redis database. | Int | No | 0 | None. |
| cluster Mode | Specifies whether the ApsaraDB for Redis database is in cluster mode. | Boolea n | No | false | None. |

| hostAn dPorts | The host and port number of the ApsaraDB for Redis database. Note If the ClusterMode parameter is set to true and connections in high availability (HA) mode are not required, you can configure the host and port parameters to specify only one of the hosts. You can also configure only this parameter. The priority of this parameter is higher than the priority of the host and port parameters. | String | No |   | Left empty | If the ClusterMode parameter is set to true and HA is required for the connection from Jedis to the self-managed Redis database in cluster mode, you must configure this parameter. The value of this parameter must be a string that is in the "host1:port1,host2:po rt2" format. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | "host1:port1,host2:po |   |
|   |   |   |   |   |   | rt2" |   |   |

| key- prefix | The prefix of the primary key value of the table. | String | No | None | After you configure this parameter, a prefix specified by key-prefix is automatically added to the value of the primary key column when you query data in an ApsaraDB for Redis dimension table or write data to an ApsaraDB for Redis result table. A delimiter specified by key- prefix-delimiter is used to separate the prefix and the primary key value. Note Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| key- prefix- delimit er | The delimiter that is used to separate the prefix and the primary key value. | String | No | None |   |

Sink table-specific parameters

| Param eter | Descriptio n | Data type | Requi red | Defau lt value | Remarks |
|---|---|---|---|---|---|
| mode | The data type of the data that is stored in the ApsaraDB for Redis result table. | String | Yes | None | ApsaraDB for Redis result tables support five data structures. When you execute a DDL statement to create an ApsaraDB for Redis result table, make sure that the DDL statement complies with the specified data structure and a primary key is specified for the ApsaraDB for Redis result table. |

| flatten Hash | Specifies whether to write data of the HASHMAP type in multi-value mode. | Boole an | No | false | Valid values: true: Data of the HASHMAP type is written to a result table in multi-value mode. In this case, you must declare multiple non-primary key fields in a DDL statement. The value of the primary key field corresponds to the key, the name of each non-primary key field corresponds to a field, and the value of each non-primary key field corresponds to the value of the field. false: Data of the HASHMAP type is written to a result table in single-value mode. In this case, you must declare three fields in a DDL statement. The value of the primary key field corresponds to the key, the value of the first non-primary key field corresponds to the field, and the value of the second non-primary key field corresponds to the value. Note This parameter takes effect only when the mode parameter is set to HASHMAP. Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| ignore Delete | Specifies whether to ignore retraction messages. | Boole an | No | false | Valid values: true: ignores the retraction message when it is received. false: deletes the inserted data and the key of the data when the retraction message is received. |
| expirat ion | Specifies whether to configure the time-to- live (TTL) for the key of the inserted data. | Long | No | 0 | The default value 0 indicates that the TTL is not configured for the key of the inserted data. If the value of this parameter is greater than 0, the TTL is configured for the key of the inserted data. Unit: milliseconds. |

Dimension table-specific parameters

| Para mete r | Description | Data type | Requ ired | Defa ult value | Remarks |
|---|---|---|---|---|---|

| mode | The data type of the data that ApsaraDB for Redis dimension tables read. | String | No | STRIN G | Valid values: STRING: If you do not configure this parameter, ApsaraDB for Redis dimension tables read data of the STRING type by default. HASHMAP: If you set the mode parameter to HASHMAP, data of the HASHMAP type is read in multi- value mode. In this case, you must declare multiple non-primary key fields in a DDL statement. The value of the primary key field corresponds to the key, the name of each non-primary key field corresponds to a field, and the value of each non-primary key field corresponds to the value of the field. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. If you want ApsaraDB for Redis dimension tables to read data of the HASHMAP type in single-value mode, you must configure the hashName parameter. |
|---|---|---|---|---|---|
| hashN ame | The key that is used when data of the HASHMAP type is read in single-value mode. | String | No | None | If you do not configure the mode parameter and you want ApsaraDB for Redis dimension tables to read data of the HASHMAP type in single-value mode, you must configure the hashName parameter. In this case, you must declare only two fields in a DDL statement. The value of the primary key field corresponds to the field and the value of the non-primary key field corresponds to the value. |

| cache | The cache policy. | String | No | None | Valid values: None: Data is not cached. This is the default value. LRU: Only specific data in the dimension table is cached. Each time the system receives a data record, the system searches the cache. If the system does not find the record in the cache, the system searches for the data record in the physical dimension table. ALL: All data in the dimension table is cached. Before a deployment runs, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If the data that meets the requirement cannot be found in the cache, the key does not exist. The system reloads all data in the cache after cache entries expire. Important Only Realtime Compute for Apache Flink that uses VVR 8.0.3 or later supports the ALL cache policy. You can set the cache parameter to ALL only when the hashName parameter is configured and the mode parameter is left empty. This is because data of the HASHMAP type can be read only in single-value mode if you use the ALL cache policy. If you configure the cache parameter, you must configure the cacheSize and cacheTTLMs parameters. |
|---|---|---|---|---|---|
| cache Size | The maximum number of rows of data that can be cached. | Long | No | 1000 0 | If you set the cache parameter to LRU, you must configure this parameter. |

| cache TTLMs | The cache timeout period. Unit: milliseconds. | Long | No | None | The configuration of the cacheTTLMs parameter varies based on the value of the cache parameter. If you set the cache parameter to None, the cacheTTLMs parameter can be left empty. This indicates that cache entries do not expire. If you set the cache parameter to LRU, the cacheTTLMs parameter specifies the timeout period of the cache. By default, cache entries do not expire. If you set the cache parameter to ALL, the cacheTTLMs parameter specifies the interval at which the system reloads the cache. By default, the cache is not reloaded. |
|---|---|---|---|---|---|
| cache Empty | Specifies whether to cache empty results. | Boole an | No | true | None. |
| cache Reloa dTime Black List | The time periods during which cache is not refreshed. This parameter takes effect when the cache parameter is set to ALL. The cache is not refreshed during the periods of time that you specify for this parameter. This parameter is suitable for large- scale online promotional events such as Double 11. | String | No | None | The following example shows the format of the values: 2017-10-24 14:00 -> 2017-10-24 15:00, 2017- 11-10 23:30 -> 2017-11-11 08:00. Use delimiters based on the following rules: Separate multiple time periods with commas (,). Separate the start time and end time of each time period with an arrow (->) that is a combination of a hyphen (-) and a closing angle bracket (>). |

**Data structures supported by an ApsaraDB for Redis result**

**table**

| Data type | Data structure | Command used to insert data into an ApsaraDB for Redis result table |
|---|---|---|

| STRING | A DDL statement has two columns. The first column lists keys of the STRING type. The second column lists values of the STRING type. |   | set key value |   |   |
|---|---|---|---|---|---|
| LIST | A DDL statement has two columns. The first column lists keys of the STRING type. The second column lists values of the STRING type. |   | lpush key value |   |   |
| SET | A DDL statement has two columns. The first column lists keys of the STRING type. The second column lists values of the STRING type. |   | sadd key value |   |   |
| HASHMAP | By default, a DDL statement has three columns. The first column lists keys of the STRING type. The second column lists fields of the STRING type. The third column lists values of the STRING type. |   | hmset key field value |   |   |
|   | If the flattenHash parameter is set to true, a DDL statement can have multiple columns. In this example, a DDL statement has four columns. The first column lists keys of the STRING type. The second column lists field names and field values of the STRING type. For example, the field name col1 corresponds to a field, and the field value value1 corresponds to the value of the field. The third column lists field names and field values of the STRING type. For example, the field name col2 corresponds to a field, and the field value value2 corresponds to the value of the field. The fourth column lists field names and field values of the STRING type. For example, the field name col3 corresponds to a field, and the field value value3 corresponds to the value of the field. |   | hmset key col1 value1 col2 value2 col3 value3 |   |   |
|   |   |   |   | hmset key col1 value1 col2 |   |
|   |   | ird column lists field names | value2 col3 value3 |   |   |

| SORTEDSET | A DDL statement has three columns. The first column lists keys of the STRING type. The second column lists scores of the DOUBLE type. The third column lists values of the STRING type. | zadd key score value |
|---|---|---|

**Data type mappings**

| Type | Data type of ApsaraDB for Redis | Data type in Realtime Compute for Apache Flink |
|---|---|---|
| General | STRING | STRING |
| Sink table- specific | SCORE | DOUBLE |

> **Note:** The data of the SCORE type is added to the values of the SORTEDSET data type in ApsaraDB for Redis databases. You must manually set a score of the DOUBLE type for each sorted value and sort the values based on their scores in ascending order.

**Sample code**

Sample code for a sink table Write data of the STRING type to ApsaraDB for Redis. In this example, the value of the `col1` column in the `redis_sink` result table is used as the key, and the value of the `col2` column is used as the value.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  col2 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'STRING',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
```

);

```
INSERT INTO redis_sink SELECT * FROM datagen_source;
```

Write data of the HASHMAP type in single-value mode to ApsaraDB for Redis. In this

|   | col1 |
|---|---|
| col2 |   |

example, the value of the `col1` column in the `redis_sink` result table is used as the key, the value of the `col2` column is used as the field, and the value of the `col3` column is used as the value.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'HASHMAP',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
```

);

```
INSERT INTO redis_sink SELECT * FROM datagen_source;
```

Write data of the HASHMAP type in multi-value mode to ApsaraDB for Redis. In this

|   | col1 |
|---|---|
| col2 |   |

example, the value of the `col1` column in the `redis_sink` result table is used as the key, the value of the `col2` column is used as the value of the field col2, the value of the `col3` column is used as the value of the field col3, and the value of the `col4` column is used as the value of the field col4.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'mode' = 'HASHMAP',
  'flattenHash' = 'true',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
```

);

```
INSERT INTO redis_sink SELECT * FROM datagen_source;
```

Sample code for a dimension table Read data of the STRING type. In this example, the value of the `col1` column in the `redis_dim` dimension table is used as the key, and the value of the `col2` column is used as the value.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT t1.col1, t2.col1, t2.col2 FROM datagen_source AS t1 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

Read data of the HASHMAP type in single-value mode. In this example, the value testKey

|   | hashName |
|---|---|
| redis dim _ |   |

of the `hashName` parameter is used as the key, the value of the `col1` column in the `redis_dim` dimension table is used as the field, and the value of the `col2` column is used as the value.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'hashName' = 'testkey'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT t1.col1, t2.col1, t2.col2 FROM datagen_source AS t1 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

Read data of the HASHMAP type in multi-value mode. In this example, the value of the `col1` column in the `redis_dim` dimension table is used as the key, the value of the `col2` column is used as the value of the field col2, the value of the `col3` column is used as the value of the field col3, and the value of the `col4` column is used as the value of the field col4.

```
CREATE TEMPORARY TABLE datagen_source (
  col1 STRING,
  proctime as PROCTIME()
) WITH (
  'connector' = 'datagen',
  'number-of-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE redis_dim (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
  PRIMARY KEY (col1) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'mode' = 'HASHMAP'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  col1 STRING,
  col2 STRING,
  col3 STRING,
  col4 STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT t1.col1, t2.col2, t2.col3, t2.col4 FROM datagen_source AS t1 JOIN redis_dim FOR SYSTEM_TIME AS OF t1.proctime AS t2 ON t1.col1 = t2.col1;
```

### 5.20 Tair (Redis OSS-compatible) connector

**connector**

This topic describes how to use the Tair (Redis OSS-compatible) connector.

**Background information**

Tair (Redis OSS-compatible) is a cloud-native in-memory database developed by Alibaba Cloud. It is compatible with open source Redis and provides rich data models and enterpriseclass capabilities to support real-time online scenarios. Tair (Redis OSS-compatible) also introduces persistent memory-optimized instances that are based on the new non-volatile memory (NVM) storage medium. The instances can help reduce costs by more than 30%, ensure data persistence, and provide approximately the same performance as in-memory databases. The following table describes the capabilities supported by the Tair (Redis OSS-compatible) connector.

| Item | Description |
|---|---|
| Table types | Sink table |
| Running modes | Streaming mode |
| Data formats | String |
| Monitoring metrics | numBytesSend numBytesSendPerSecond numRecordsSend numRecordsSendPerSecond numRecordSendErrors currentSendTime |
| API types | SQL |
| Data update or deletion in a sink table | Supported |

**Prerequisites**

A whitelist is configured. A Tair (Redis OSS-compatible) instance is created.

**Limits**

The Tair (Redis OSS-compatible) connector does not allow you to configure multiple hosts. Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.6 or later supports the Tair (Redis OSS-compatible) connector.

**Syntax**

Tair (Redis OSS-compatible) supports all self-developed Tair (Redis OSS-compatible) data structures based on the compatibility with the following Redis data structures: STRING, LIST, SET, HASHMAP, and SORTEDSET. To create a Tair (Redis OSS-compatible) sink table, execute the following DDL statement:

```
CREATE TABLE tair_table (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED -- This parameter is required.
) WITH (
  'connector'= 'tair',
  'host' = '<yourHost>'
```

);

> **Note:** Tair (Redis OSS-compatible) is compatible with Redis data structures.

**Parameters in the WITH clause**

| Parameter | Description | Data type | Requ ired | Def ault valu e | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | Non e | Set the value to tair. |
| host | The endpoint of the Tair (Redis OSS-compatible) server. | String | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |

| mode | The data structure of Tair (Redis OSS- compatible). | String | Yes | Non e | Valid values: string list set hashmap sortedset tairstring tairhash tairzset tairbloom tairdoc tairsearch tairts taircpc tairroaring tairgis tairvector Tair (Redis OSS-compatible) supports Redis data structures and self- developed Tair (Redis OSS- compatible) data structures. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.1 or later supports TairTs, TairCpc, TairRoaring, TairVector, and TairGis. Tair (Redis OSS- compatible) sink tables support self-developed Tair (Redis OSS- compatible) data structures. The DDL statement that is used to create a Tair (Redis OSS- compatible) sink table must define the table based on the specified format, and a primary key must be specified for the table. |
|---|---|---|---|---|---|
| port | The port number of the Tair (Redis OSS- compatible) server. | Int | No | 637 9 | None. |

| password | The password that is used to access the Tair (Redis OSS- compatible) database. | String | No | An emp ty strin g | An empty string indicates that no verification is performed. |
|---|---|---|---|---|---|
| dbNum | The ID of the destination database. | Int | No | 0 | None. |
| clusterMode | Specifies whether to use the cluster architecture. | Boole an | No | false | Valid values: true: uses the cluster architecture. false: uses the standalone architecture. |
| ignoreDelet e | Specifies whether to ignore retraction messages. | Boole an | No | false | Valid values: false: deletes the inserted data and the key of the data when the retraction message is received. This is the default value. true: retains the inserted data and the key of the data when the retraction message is received. |
| expiration | The time-to-live (TTL) that is specified for the keys of the inserted data. | Long | No | 0 | A value of 0 indicates that the TTL is not configured. If the value of this parameter is greater than 0, the TTL is configured for the key of the inserted data. Unit: milliseconds. |
| expirationAt | The absolute expiration time that is specified for the keys of the inserted data. | Long | No | 0 | Unit: milliseconds. Default value: 0. The default value indicates that no expiration time is specified. If the value of this parameter is greater than 0 and the expiration parameter is set to 0, an absolute expiration time is specified for the keys of the inserted data. |

| incrMode | The sink mode of the Tair (Redis OSS- compatible) database. | String | No | Non e | Valid values: None: indicates the insert operation. This is the default value. int: indicates the INCRBY operation. The value of INCR is fixed to the value of the incrValue parameter. float: indicates the INCRBYFLOAT operation. The value of INCR is fixed to the value of the incrValue parameter. dynamic int: indicates the INCRBY _ operation. The value of INCR is the name of the column to which the value of INCR belongs in a DDL statement. dynamic float: indicates the _ INCRBYFLOAT operation. The value of INCR is the name of the column to which the value of INCR belongs in a DDL statement. |
|---|---|---|---|---|---|
| incrValue | The value of INCR that is determined based on the value of the incrMode parameter. | String | No | Non e | Valid values: If the incrMode parameter is set to None, you do not need to configure the incrValue parameter. If the incrMode parameter is set to int or float, the value of the incrValue parameter is the value of INCR. If the incrMode parameter is set to dynamic int or dynamic float, the _ _ value of the incrValue parameter is the name of the column to which the value of INCR belongs in a DDL statement. |

| fieldExpireM ode | The expiration mode of the fields in TairHash or skeys in TairTS. | String | No | Non e | Valid values: None: No expiration time is specified. millisecond: A relative expiration time is specified. The expiration time is fixed to the value of the fieldExpireValue parameter. Note The expiration mode of the skeys in TairTS must be millisecond. unixtime: An absolute expiration time is specified. The expiration time is fixed to the value of the fieldExpireValue parameter. dynamic millisecond: A relative _ expiration time is specified. The expiration time is the name of the column to which the value of fieldExpireValue belongs in a DDL statement. dynamic unixtime: An absolute _ expiration time is specified. The expiration time is the name of the column to which the value of fieldExpireValue belongs in a DDL statement. |
|---|---|---|---|---|---|
| fieldExpireV alue | The expiration time of the fields in TairHash or skeys in TairTS. | String | No | Non e | Valid values: If the fieldExpireMode parameter is set to None, no expiration time is specified. If the fieldExpireMode parameter is set to millisecond or unixtime, the value of the fieldExpireValue parameter is the expiration time. If the fieldExpireMode parameter is set to dynamic millisecond or _ dynamic unixtime, the value of the _ fieldExpireValue parameter is the name of the column to which the value of the fieldExpireValue parameter belongs in a DDL statement. |

**Data type mappings**

| Data type in Realtime Compute for Apache Flink | Data type of Tair (Redis OSS-compatible) |
|---|---|
| VARCHAR | STRING |

|   | Edition) User Guide·Data connec or |
|---|---|

| DOUBLE | DOUBLE |
|---|---|

**Formats of Tair (Redis OSS-compatible) data structures**

| Type | Data structure | Command for inserting data into a Tair (Redis OSS-compatible) sink table |
|---|---|---|
| TairString | If the incrMode parameter is set to None, a DDL statement has two columns. The first column lists keys of the STRING type. The second column lists values of the STRING type. | exset key value |
|   | If the incrMode parameter is set to int or float, a DDL statement has only one column and the column lists keys of the STRING type. | exincrby/exincrbyfloat key incrValue |
|   | If the incrMode parameter is set to dynamic int or dynamic float, a DDL _ _ statement has two columns. The first column lists keys of the STRING type. The second column lists incrValue values of the STRING type. | exincrby/exincrbyfloat key incrValue |
| TairHash | If the incrMode parameter is set to None, a DDL statement has three columns. The first column lists keys of the STRING type. The second column lists fields of the STRING type. The third column lists field values of the STRING type. | exhset key field value |
|   | If the incrMode parameter is set to int or float, a DDL statement has two columns. The first column lists keys of the STRING type. The second column lists fields of the STRING type. | exhincrby/exincrbyfloat key field incrValue |

|   | If the incrMode parameter is set to dynamic int or dynamic float, a DDL _ _ statement has three columns. The first column lists keys of the STRING type. The second column lists fields of the STRING type. The third column lists incrValue values of the STRING type that correspond to fields. | exhincrby/exincrbyfloat key field incrValue |
|---|---|---|
| TairZset | If the incrMode parameter is set to None, TairZset supports multi-dimensional data sorting. TairZset allows you to sort data of the DOUBLE type from a maximum of 256 dimensions. Therefore, a DDL statement has 3 to 258 columns. The first column lists keys of the STRING type. The second column lists members of the STRING type. The remaining columns list scores of the DOUBLE type. | exzadd key score member Note If you want to sort data from multiple dimensions, make sure that the score formats of all dimensions are the same. |
|   | If the incrMode parameter is set to int or float, a DDL statement has two columns. The first column lists keys of the STRING type. The second column lists members of the STRING type. | exzincyby key member incrValue |
|   | If the incrMode parameter is set to dynamic int or dynamic float, a DDL _ _ statement has three columns. The first column lists keys of the STRING type. The second column lists members of the STRING type. The third column lists incrValue values of the STRING type. | exzincyby key member incrValue |

| TairBloo m | The incrMode parameter must be set to None. When data is inserted into a Tair (Redis OSS-compatible) sink table for the first time, a TairBloom key that has a default capacity of 100 elements and an error rate of 0.01 is created. A DDL statement has two columns. The first column lists keys of the STRING type. The second column lists items of the STRING type. | BF.ADD key item |
|---|---|---|
| TairDoc | The incrMode parameter must be set to None. A DDL statement has three columns. The first column lists keys of the STRING type. The second column lists paths of the STRING type. The third column lists JSON elements of the STRING type. | JSON.SET key path json |
|   | If the incrMode parameter is set to None, a DDL statement has four columns. The first column lists indexes of the STRING type. The second column lists document IDs of the STRING type. The third column lists documents of the STRING type. The documents must be in the JSON format. The fourth column lists mappings of the STRING type. | TFT.ADDDOC index document docid Note Before you insert data into a Tair (Redis OSS-compatible) sink table, you must create an index and add a mapping. Sample command: TFT.CREATEINDEX index mappings |

| TairSearc h |   |   |
|---|---|---|
|   | If the incrMode parameter is set to int or float, a DDL statement has four columns. The first column lists indexes of the STRING type. The second column lists document IDs of the STRING type. The third column lists fields of the STRING type. The fourth column lists mappings of the STRING type. | Sample command for document operations: TFT.INCRLONGDOCFIELD/TFT.INCRFLOATDO CFIELD index doc id field increment _ Note Before you insert data into a Tair (Redis OSS-compatible) sink table, you must create an index and add a mapping. Sample command: TFT.CREATEINDEX index mappings |
|   | If the incrMode parameter is set to dynamic int or dynamic float, a DDL _ _ statement has five columns. The first column lists indexes of the STRING type. The second column lists document IDs of the STRING type. The third column lists fields of the STRING type. The fourth column lists mappings of the STRING type. The fifth column lists incrValue values of the STRING type. | Sample command for document operations: TFT.INCRLONGDOCFIELD/TFT.INCRFLOATDO CFIELD index doc id field increment _ Note Before you insert data into a Tair (Redis OSS-compatible) sink table, you must create an index and add a mapping. Sample command: TFT.CREATEINDEX index mappings |
| TairCpc | The incrMode parameter must be set to None. A DDL statement has two columns. The first column lists keys of the STRING type. The second column lists items of the STRING type. | CPC.UPDATE key item |
| TairGis | The incrMode parameter must be set to None. A DDL statement has three columns. The first column lists keys of the STRING type. The second column lists polygon names of the STRING type. The third column lists Well-known Text (WKT) values of polygons. The values are of the STRING type. | GIS.ADD area polygonName polygonWkt |

| TairRoari ng | The incrMode parameter must be set to None. A DDL statement has three columns. The first column lists keys of the STRING type. The second column lists the specified offsets of the BIGINT type. The third column lists values of the BIGINT type. Valid values: 0 and 1. | TR.SETBIT key offset value |
|---|---|---|
| TairVecto r | The incrMode parameter must be set to None. A DDL statement has six columns. The first column lists index names of the STRING type. The second column lists the primary keys of records. The values are of the STRING type. The third column lists vector data of the STRING type. The fourth column lists vector dimensions of the INT type. The fifth column lists algorithms that are used to build and query indexes. The values are of the STRING type. The sixth column lists distance methods that are used to calculate the vector distance. The values are of the STRING type. | TVS.HSET index name key VECTOR _ vector data _ Note Before you insert data into a Tair (Redis OSS-compatible) sink table, you must create an index and add a mapping. Sample command: TVS.CREATEINDEX index name dims _ algorithm distance method _ |
|   | If the incrMode parameter is set to None, a DDL statement has four columns. The first column lists pkeys of the STRING type. A pkey indicates a group of timelines. The second column lists skeys of the STRING type. An skey indicates a timeline. The third column lists timestamps of the STRING type. The fourth column lists values of the STRING type. | EXTS.S.RAW MODIFY Pkey Skey _ timestamp value |

| TairTs |   |   |
|---|---|---|
|   | If the incrMode parameter is set to float, a DDL statement has three columns. The first column lists pkeys of the STRING type. The second column lists skeys of the STRING type. The third column lists timestamps of the STRING type. | EXTS.S.RAW INCRBY Pkey Skey _ timestamp incrValue |
|   | If the incrMode parameter is set to dynamic float, a DDL statement has four _ columns. The first column lists pkeys of the STRING type. The second column lists skeys of the STRING type. The third column lists timestamps of the STRING type. The fourth column lists incrValue values of the STRING type. The incrValue values correspond to the timestamps that are listed in the third column. | EXTS.S.RAW INCRBY Pkey Skey _ timestamp incrValue |

**Sample code**

Sample code for inserting data into a Tair (Redis OSS-compatible) sink table in common mode

```
CREATE TEMPORARY TABLE datagen_stream (
  v STRING,
  p STRING
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE tair_output (
  index_name STRING,
  doc_id STRING,
  doc STRING,
  mapping STRING,
  PRIMARY KEY(index_name) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairsearch',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}'
```

);

```
INSERT INTO tair_output SELECT 'index' as index,v,p,'{"mappings":{"_source":{"enabled":true},"properties":{"p roduct_id":{"type":"keyword","ignore_above":128},"product_name":{"type":"text"}}}}' a s mapping FROM datagen_stream;
```

Sample code for inserting data into a Tair (Redis OSS-compatible) sink table when the incrMode parameter is configured

```
CREATE TEMPORARY TABLE datagen_stream (
  v STRING,
  p STRING
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE tair_output (
  key STRING,
  step STRING,
  PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairstring',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'incrMode' = 'dynamic_float',
  'incrValue' = 'step'
```

);

```
INSERT INTO tair_output SELECT * FROM datagen_stream; CREATE TEMPORARY TABLE datagen_stream (
  v STRING,
  p STRING
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE tair_output (
  key STRING,
  PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairstring',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'incrMode' = 'float',
  'incrValue' = '11.11'
```

);

```
INSERT INTO tair_output SELECT v FROM datagen_stream;
```

Sample code for inserting data into a Tair (Redis OSS-compatible) sink table when the fieldExpireMode parameter is configured

```
CREATE TEMPORARY TABLE datagen_stream (
  v STRING,
  p STRING,
  s STRING
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE tair_ouput (
 key STRING,
 field STRING,
 value STRING,
 PRIMARY KEY (key) NOT ENFORCED
) WITH (
  'connector' = 'tair',
  'mode' = 'tairhash',
  'host' = '${tairHost}',
  'port' = '${tairPort}',
  'password' = '${password}',
  'fieldExpireMode' = 'millisecond',
  'fieldExpireValue' = '1000'
```

);

```
INSERT INTO tair_output SELECT v, p, s FROM datagen_stream;
```

### 5.21 ApsaraDB RDS for MySQL connector

**connector**

This topic describes how to use the ApsaraDB RDS for MySQL connector. ApsaraDB RDS for MySQL is developed based on a branch of MySQL and provides excellent performance. ApsaraDB RDS for MySQL is a tried and tested solution that can withstand the high-volume concurrent traffic during Double 11. ApsaraDB RDS for MySQL provides basic features such as whitelist configuration, backup and restoration, Transparent Data Encryption (TDE), data migration, and management of instances, accounts, and databases. The following table describes the capabilities supported by the ApsaraDB RDS for MySQL connector.

| Item | Description |
|---|---|
| Table types | Sink table and dimension table |
| Running modes | Batch mode and streaming mode |
| Data formats | None |

| Monitoring metrics | Metrics for dimension tables: none Monitoring metrics for sink tables: numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime numRecordsOutErrors |
|---|---|
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

An IP address whitelist is configured. An ApsaraDB RDS for MySQL database and a table are created.

**Limits**

The ApsaraDB RDS for MySQL connector supports only ApsaraDB RDS for MySQL databases. The at-least-once semantics can be used. If an ApsaraDB RDS for MySQL sink table contains a primary key, idempotence can be used to ensure data correctness. We recommend that you use the latest version of Realtime Compute for Apache Flink to ensure high performance and stability. For example, you can use Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.X or later.

**Syntax**

Sink table

```
CREATE TABLE rds_sink(
  id INT,
  num BIGINT,
  PRIMARY KEY(id) NOT ENFORCED
) WITH (
  'connector'='rds',
  'tableName'='your-table-name',
  'userName'='your-user-name',
  'password'='your-password',
  'url'='your-url'
```

);

|   | Note The ApsaraDB RDS for MySQL connector converts each row of output data into an SQL statement and then executes the statement to write data into the sink table. If the sink table does not contain a primary key, the ApsaraDB RDS for MySQL connector executes INSERT INTO table name (column1, column2, ...) _ VALUES (value1, value2, ...); statement. If the sink table contains a primary key, the ApsaraDB RDS for MySQL connector executes the INSERT INTO |   |
|---|---|---|
|   |   | INSERT INTO |
|   | table name (column1, column2, ...) VALUES (value1, value2, ...) ON DUPLICATE _ |   |
|   | KEY UPDATE column1 = VALUES(column1), column2 = VALUES(column2), ...; |   |

|   | INSERT INTO table name (column1, column2, ...) _ |
|---|---|
| VALUES (value1, value2, ...); |   |

> statement. If a physical table contains a unique index constraint besides a primary key constraint and two records with different primary keys but the same unique index are inserted into the physical table, downstream data is overwritten due to a conflict between the unique indexes. This causes data loss.
> If an auto-increment primary key is specified in an ApsaraDB RDS for MySQL database, you cannot declare the auto-increment field in the Flink DDL statement. During data writing, the database automatically configures the auto- increment field. The ApsaraDB RDS for MySQL connector can only be used to write or delete data that contains auto-increment fields but cannot be used to update the data.

Dimension table

```
CREATE TABLE rds_dim(
 id1 INT,
 id2 VARCHAR
) WITH (
  'connector'='rds',
  'tableName'='your-table-name',
  'userName'='your-user-name',
  'password'='your-password',
  'url'='your-url'
  'cache'='NONE'
```

);

**Parameters in the WITH clause**

Common parameters

| Param eter | Descri ption | Data type | Requir ed | Default value | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | String | Yes | None. | Set the value to rds. |
| tableNa me | The table name. | String | Yes | None. | None. |

| userNa me | The userna me that is used to access the databas e. | String | Yes | None. | None. |
|---|---|---|---|---|---|
| passwor d | The passwor d that is used to access the databas e. | String | Yes | None. | None. |
| url | The URL that is used to access the table. | String | Yes | None. | Contact Apsara Stack O&M engineers to obtain the required information. |

| maxRet ryTimes | The maximu m number of retries that can be perform ed when you fail to query data in a dimensi on table or write data to a sink table. | Integer | No | 10 | None. |
|---|---|---|---|---|---|

Sink table-specific parameters

| Paramet er | Descripti on | Data type | Required | Default value | Remarks |
|---|---|---|---|---|---|
| batchSize | The number of data records that can be written at a time. | Integer | No | 4096 | None. |

| bufferSize | The maximum number of data records that can be cached in the memory. Write operation s are triggered if the threshold specified by the batchSize or bufferSize paramete r is reached. | Integer | No | 10000 | This parameter takes effect only after you specify the primary key. |
|---|---|---|---|---|---|

| flushInter valMs | The interval at which you want to flush the memory buffer. If the number of cached data records does not reach the upper limit that is specified by the batchSize or bufferSize paramete r within the specified period of time, the system automatic ally writes all cached data to the sink table. | Integer | No | 2000 | If you do not configure this parameter in a version for which the default value of this parameter is 0, a small amount of data may never be written to the sink table. To resolve this issue, we recommend that you use a later version of Realtime Compute for Apache Flink. |
|---|---|---|---|---|---|
| ignoreDel ete | Specifies whether to ignore delete operation s. | Boolean | No | false | Delete operations may occur when you use Flink SQL. If multiple output operators update different fields in the same sink table based on the primary key, the data result may be incorrect. For example, a data record is deleted in a task, and then only some fields of the data record are updated in another task. In this case, the values of the fields that are not updated become null or default values because the fields are deleted. To prevent delete operations, you can set the ignoreDelete parameter to true. |

| connectio nMaxActiv e | The size of the database connectio n pool. | Integer | No | 40 | If access to a database connection pool times out, the number of database connections in the pool may be insufficient. You can increase the size of the database connection pool. If the maximum number of parallel connections supported by the database is small, you can reduce the size of the connection pool or reduce the parallelism of operators. |
|---|---|---|---|---|---|

Dimension table-specific parameters

| Paramet er | Descripti on | Dat a type | Requ ired | Default value | Remarks |
|---|---|---|---|---|---|
| cache | The cache policy for the dimension table. | Strin g | No | ALL | Valid values: None, LRU, and ALL. |
| cacheSize | The maximum number of rows of data records that can be cached. | Integ er | No | 100000 | If you set the cache parameter to LRU, you must configure the cacheSize parameter. If you set the cache parameter to NONE or ALL, you do not need to configure the cacheSize parameter. |

| cacheTTL Ms | The cache timeout period. | Long | No | If you set the cache parameter to NONE, you do not need to configure the cacheTTLMs parameter. This indicates that cache entries do not expire. If you set the cache parameter to LRU, the cacheTTLMs parameter specifies the cache timeout period. By default, cache entries do not expire. If you set the cache parameter to ALL, the cacheTTLMs parameter specifies the interval at which the system reloads the cache. By default, the cache is not refreshed. | Unit: milliseconds. |
|---|---|---|---|---|---|
| maxJoinR ows | The maximum number of results returned after each data record in the primary table is mapped to the data in the dimension table. | Integ er | No | 1024 | When you join the primary table and a dimension table, the number of results returned after an input data record in the primary table is mapped to the data records in the dimension table is limited by this parameter. If you can estimate that a data record in the primary table corresponds to a maximum of n data records in the dimension table, you can set the maxJoinRows parameter to n to ensure efficient matching of Realtime Compute for Apache Flink. |

**Data type mappings**

| Data type of Realtime Compute for Apache Flink | Data type of ApsaraDB RDS for MySQL |
|---|---|
| BOOLEAN | BOOLEAN |

| TINYINT | TINYINT |
|---|---|
| TINYINT(1) Note Only dimension tables support this mapping. | BOOLEAN |
| SMALLINT | SMALLINT |
| SMALLINT | TINYINT UNSIGNED |
| INT | INT |
| INT | SMALLINT UNSIGNED |
| BIGINT | BIGINT |
| BIGINT | INT UNSIGNED |
| DECIMAL(20,0) | BIGINT UNSIGNED |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARBINARY | VARBINARY |

**Sample code**

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source(
 `name` VARCHAR,
 `age` INT
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE rds_sink(
 `name` VARCHAR,
 `age` INT
) WITH (
  'connector'='rds',
  'password'='your-password',
  'tableName'='your-tablename',
  'url'='your-url',
  'userName'='your-username'
```

);

```
INSERT INTO rds_sink SELECT * FROM datagen_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source(
 a INT,
 b BIGINT,
 c STRING,
 `proctime` AS PROCTIME()
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE rds_dim(
 a INT,
 b VARCHAR,
 c VARCHAR
) WITH (
 'connector'='rds',
 'password'='<yourPassword>',
 'tableName'='<yourTablename>',
 'url'='jdbc:mysql://xxx',
 'userName'='<yourUsername>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
 a INT,
 b STRING
) WITH (
 'connector'='blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.a, H.b FROM datagen_source AS T JOIN rds_dim FOR SYSTEM_TIME AS OF T.`procti me` AS H ON T.a=H.a;
```

### 5.22 JDBC connector

This topic describes how to use the Java Database Connectivity (JDBC) connector.

**Background information**

The JDBC connector is provided by Apache Flink and can be used to read data from and write data to common databases, such as MySQL, PostgreSQL, and Oracle. The following table describes the capabilities supported by the JDBC connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | Not supported |

| Monitoring metrics | Not supported |
|---|---|
| API types | SQL |
| Data updates or deletion in a sink table | Supported |

**Prerequisites**

The database and table to which you want to connect are created.

**Limits**

Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.1 or later supports the JDBC connector. A JDBC source table is a bounded source. After the system reads all data from a JDBC source table in a task, the task is complete. If you want to capture real-time change data, use a Change Data Capture (CDC) connector. If you use the JDBC sink connector to connect to a PostgreSQL database, make sure that the database version is PostgreSQL 9.5 or later. PostgreSQL uses the ON CONFLICT syntax to insert or update data when a primary key is specified in a DDL statement. The ON CONFLICT syntax is supported only in PostgreSQL 9.5 or later. Realtime Compute for Apache Flink supports only the open source JDBC connector that does not include a JDBC driver for a specific database. When you use the JDBC connector, you need to manually upload the JAR package of the destination database driver as an additional dependency file. The following table describes the JDBC drivers supported by Realtime Compute for Apache Flink.

| Driver | Group Id | Artifact Id |
|---|---|---|
| MySQL | mysql | mysql-connector-java |
| Oracle | com.oracle.database.jdbc | ojdbc8 |
| PostgreSQL | org.postgresql | postgresql |

If you use a JDBC driver that is not included in the table, you must test the validity and availability of the JDBC driver. When the JDBC connector writes data to a MySQL sink table, the JDBC connector concatenates each received data record into an SQL statement and executes the SQL statement. In a MySQL sink table that contains a primary key, the `INSERT INTO`

```
table_name (column1, column2, ...) VALUES (value1, value2, ...) ON DUPLICATE KEY
```

UPDATE column1 = VALUES(column1), column2 = VALUES(column2), ...; statement is concatenated and executed. If a physical table contains a unique index constraint besides a primary key constraint and two records with different primary keys but the same unique index are inserted into the physical table, downstream data is overwritten due to a conflict between the unique indexes. This causes data loss.

**Syntax**

```
CREATE TABLE jdbc_table (
  `id` BIGINT,
  `name` VARCHAR,
   PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
```

);

**Parameters in the WITH clause**

Common parameters

| Parameter | Description | Data type | Requir ed | Defa ult value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | Set the value to jdbc. |
| url | The URL of the database. | String | Yes | None | None. |
| table-name | The name of the JDBC table. | String | Yes | None | None. |
| username | The name of the JDBC user. | String | No | None | If you configure one of the username and password parameters, you must also configure the other parameter. |
| password | The password of the JDBC user. | String | No | None |   |

Source table-specific parameters

| Parameter | Description | Data type | Requir ed | Defaul t value | Remarks |
|---|---|---|---|---|---|
| scan.partitio n.column | The name of the column that is used to partition the input data. | String | No | None | The values in the column must be of the NUMERIC, DATE, or TIMESTAMP type. For more information about partitioned scan, see Partitioned Scan. |

| scan.partitio n.num | The number of partitions. | Integer | No | None | None. |
|---|---|---|---|---|---|
| scan.partitio n.lower- bound | The smallest value of the first partition. | Integer | No | None | None. |
| scan.partitio n.upper- bound | The largest value of the last partition. | Integer | No | None | None. |
| scan.fetch- size | The number of rows of data that are obtained from the database each time data is read from a source table. | Integer | No | 0 | If you set this parameter to 0, this parameter is ignored. |
| scan.auto- commit | Specifies whether to enable auto- commit. | Boolea n | No | true | None. |

Sink table-specific parameters

| Parameter | Description | Data type | Requir ed | Defaul t value | Remarks |
|---|---|---|---|---|---|
| sink.buffer- flush.max- rows | The maximum number of data records that can be cached before the flush operation is performed. | Integer | No | 100 | If you set this parameter to 0, data records are not cached before the flush operation is performed. |

| sink.buffer- flush.interva l | The interval at which data is flushed. If data records are cached for a period that exceeds the duration specified by this parameter, the flush operation is performed in an asynchronous thread. | Duratio n | No | 1 s | If you set this parameter to 0, data records are not cached before the flush operation is performed. Note If you want to process cached flush events in asynchronous mode, you can set the sink.buffer- flush.max-rows parameter to 0 and configure the sink.buffer- flush.interval parameter based on your business requirements. |
|---|---|---|---|---|---|
| sink.max- retries | The maximum number of retries that are allowed when data fails to be written to the database. | Integer | No | 3 | None. |

Dimension table-specific parameters

| Parameter | Description | Data type | Requir ed | Defaul t value | Remarks |
|---|---|---|---|---|---|
| lookup.cach e.max-rows | The maximum number of rows of data that can be cached. If the number of rows of data in the cache exceeds the value of this parameter, the earliest row of data expires and is replaced by a new row of data. | Integer | No | None | By default, caching for dimension tables is disabled. You can configure the lookup.cache.max- rows and lookup.cache.ttl parameters to enable caching for dimension tables. If caching for dimension tables is enabled, the LRU cache policy is used. |

| lookup.cach e.ttl | The maximum time to live (TTL) of each row of data in the cache. If the time period for which a row of data is cached exceeds the value of this parameter, the row of data expires. | Duratio n | No | None |   |
|---|---|---|---|---|---|
| lookup.cach e.caching- missing-key | Specifies whether to cache empty query results. | Boolea n | No | true | Valid values: true: Empty query results are cached. This is the default value. false: Empty query results are not cached. |
| lookup.max- retries | The maximum number of retries allowed when the database fails to be queried. | Integer | No | 3 | None. |

PostgreSQL database-specific parameters

| Parameter | Description | Data type | Requir ed | Defa ult value | Remarks |
|---|---|---|---|---|---|
| source.exte nd- type.enable d | Specifies whether data of the JSONB and UUID extension types can be read and mapped to the data types supported by Flink when a PostgreSQL table is used as a source table or a dimension table. | Boolea n | No | false | Valid values: true: Data of the JSONB and UUID extension types can be read and mapped to the data types supported by Flink. false: Data of the JSONB and UUID extension types cannot be read or mapped to the data types supported by Flink. This is the default value. |

**Data type mappings**

| Data type of MySQL | Data type of Oracle | Data type of PostgreSQL | Data type of Flink SQL |
|---|---|---|---|
| TINYINT | None | None | TINYINT |

| SMALLINT TINYINT UNSIGNED | None | SMALLINT INT2 SMALLSERIAL SERIAL2 | SMALLINT |
|---|---|---|---|
| INT MEDIUMINT SMALLINT UNSIGNED | None | INTEGER SERIAL | INT |
| BIGINT INT UNSIGNED | None | BIGINT BIGSERIAL | BIGINT |
| BIGINT UNSIGNED | None | None | DECIMAL(20, 0) |
| BIGINT | None | BIGINT | BIGINT |
| FLOAT | BINARY FLOAT _ | REAL FLOAT4 | FLOAT |
| DOUBLE DOUBLE PRECISION | BINARY DOUBLE _ | FLOAT8 DOUBLE PRECISION | DOUBLE |
| NUMERIC(p, s) DECIMAL(p, s) | SMALLINT FLOAT(s) DOUBLE PRECISION REAL NUMBER(p, s) | NUMERIC(p, s) DECIMAL(p, s) | DECIMAL(p, s) |
| BOOLEAN TINYINT(1) | None | BOOLEANcan | BOOLEAN |
| DATE | DATE | DATE | DATE |
| TIME [(p)] | DATE | TIME [(p)] [WITHOUT TIMEZONE] | TIME [(p)] [WITHOUT TIMEZONE] |

| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
|---|---|---|---|
| CHAR(n) VARCHAR(n) TEXT | CHAR(n) VARCHAR(n) CLOB | CHAR(n) CHARACTER(n) VARCHAR(n) CHARACTER VARYING(n) TEXT JSONB UUID | STRING |
| BINARY VARBINARY BLOB | RAW(s) BLOB | BYTEA | BYTES |
| None | None | ARRAY | ARRAY |

**Sample code**

Sample code for a source table

```
CREATE TEMPORARY TABLE jdbc_source (
  `id` INT,
  `name` VARCHAR
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  `id` INT,
  `name` VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT * FROM jdbc_source ;
```

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE jdbc_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
```

);

```
INSERT INTO jdbc_sink SELECT * FROM datagen_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source(
 `id` INT,
 `data` BIGINT,
 `proctime` AS PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE jdbc_dim (
  `id` INT,
  `name` VARCHAR
) WITH (
  'connector' = 'jdbc',
  'url' = 'jdbc:xxx',
  'table-name' = '<yourTable>',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  `id` INT,
  `data` BIGINT,
  `name` VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.`id`,T.`data`, H.`name` FROM datagen_source AS T JOIN jdbc_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.id = H.id;
```

### 5.23 MongoDB connector

This topic describes how to use the MongoDB connector.

**Background information**

MongoDB is a document-oriented unstructured database that simplifies application development and expansion. The following table describes the capabilities supported by the MongoDB connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode |

| Monitoring metrics | Metrics for source tables: numBytesIn numBytesInPerSecond numRecordsIn numRecordsInPerSecond numRecordsInErrors currentFetchEventTimeLag currentEmitEventTimeLag watermarkLag sourceIdleTime Metrics for dimension tables and sink tables: none |
|---|---|
| API types | DataStream API and SQL API |
| Data updates or deletion in a sink table | Yes |

**Features**

A MongoDB Change Data Capture (CDC) source table is a streaming source table of MongoDB databases. The MongoDB connector for a MongoDB CDC source table is referred to as a MongoDB CDC connector. The MongoDB CDC connector reads full historical data from a MongoDB database and then reads operations log data. This way, data accuracy is ensured. If an error occurs, the exactly-once semantics can be used to ensure data accuracy. The MongoDB CDC connector can use the Change Stream API to efficiently capture document changes in MongoDB databases and collections, monitor document insertion, modification, replacement, and deletion events, and convert the events into changelog streams that can be processed by Realtime Compute for Apache Flink. The MongoDB CDC connector provides the following features: Efficiently monitors document changes by using the Change Stream API that is supported in MongoDB 3.6. Ensures the exactly-once semantics for deployments that fail at any phase. Supports full and incremental data monitoring. After the snapshot reading phase is complete, MongoDB CDC connector automatically switches to the incremental reading phase. Supports parallel reading in the initial snapshot phase. Only MongoDB 4.0 or later supports this feature. Supports the following startup modes: initial: If the MongoDB CDC connector starts for the first time, the connector performs an initial snapshot for the monitored database table and continues to read the latest operations log data. latest-offset: If the MongoDB CDC connector starts for the first time, the connector does not perform a snapshot for the monitored database table. The connector only reads data from the end of the operations log data. This indicates that the connector can read only data changes after the connector starts. timestamp: The MongoDB CDC connector skips the snapshot reading phase and reads the oplog events from a specific timestamp. Only MongoDB 4.0 or later supports this mode. Supports full changelog event streams. Only MongoDB 6.0 or later supports this feature.

**Prerequisites**

CDC source table The MongoDB CDC connector can read data from ApsaraDB for MongoDB replica set or sharded cluster database instances. The MongoDB CDC connector can also read data from self-managed MongoDB databases. The replica set feature is enabled for the MongoDB database that you want to monitor. This ensures that you can use the basic features of the MongoDB CDC connector. For more information, see Replication. The preimage and postimage features are enabled for the MongoDB database if you want to use the full changelog event stream feature. For more information, see Document Preimages. If the authentication feature of MongoDB is enabled, you must use a MongoDB user that has the following database permissions: splitVector listDatabases listCollections collStats find changeStream Permissions to access the config.collections and config.chunks collections MongoDB dimension table and sink table A MongoDB database and a table are created. An IP address whitelist is configured to access MongoDB.

**Limits**

CDC source table Only Realtime Compute for Apache Flink that uses VVR 8.0.1 or later supports the MongoDB CDC connector. Only MongoDB 6.0 or later supports full changelog event streams. Sink table In Realtime Compute for Apache Flink that uses a Ververica Runtime (VVR) version earlier than 8.0.5, data can only be inserted into a sink table. In Realtime Compute for Apache Flink that uses VVR 8.0.5 or later, if a primary key is defined in the DDL statement that is used to create a sink table, data can be inserted into, updated in, or deleted from the sink table. If no primary key is defined in the DDL statement that is used to create a sink table, data can only be inserted into the sink table. Dimension table Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports MongoDB dimension tables.

**Syntax**

```
CREATE TABLE tableName(
  _id STRING,
  [columnName dataType,]*
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'localhost:27017',
  'username' = 'mongouser',
  'password' = '${secret_values.password}',
  'database' = 'testdb',
  'collection' = 'testcoll'
```

`)`

> **Note:** When you create a MongoDB CDC source table, you must declare the `_id STRING` column as the unique primary key.

**Parameters in the WITH clause**

Common parameters

| Paramete r | Description | Data type | Requir ed | Defa ult valu e | Remarks |
|---|---|---|---|---|---|

| connector | The name of the connector. | String | Yes | None | If you use the MongoDB connector for a source table, you must specify a value for this parameter based on the VVR version that Realtime Compute for Apache Flink uses. VVR 8.0.4 and earlier: Set this parameter to mongodb-cdc. VVR 8.0.5 and later: Set this parameter to mongodb or mongodb-cdc. If you use the MongoDB connector for a dimension table or a sink table, you must set this parameter to mongodb. |
|---|---|---|---|---|---|
| uri | The URI that is used to access the MongoDB database. | String | No | None | Note You must specify one of the uri and hosts parameters. If you specify the uri parameter, you do not need to specify the scheme , hosts , username , password , or connector.options parameter. If you specify both the uri and hosts parameters, the URI specified by the uri parameter is used to access the MongoDB database. |
| hosts | The name of the host where the MongoDB database resides. | String | No | None | Separate multiple hostnames with commas ( , ). |

|   | scheme |
|---|---|
| username |   |

| scheme | The connection protocol that is used to access the MongoDB database. | String | No | mon godb | Valid values: mongodb : The default MongoDB protocol is used to access the MongoDB database. mongodb+srv : The DNS SRV record protocol is used to access the MongoDB database. |
|---|---|---|---|---|---|
| username | The username that is used to access the MongoDB database. | String | No | None | This parameter is required if the identity verification feature is enabled for the MongoDB database. |
| password | The password that is used to access the MongoDB database. | String | No | None | This parameter is required if the identity verification feature is enabled for the MongoDB database. |
| database | The name of the MongoDB database. | String | No | None | If you use the MongoDB connector for a source table, a regular expression can be used to match the name of the MongoDB database. If you do not configure this parameter, all databases are monitored. |

| collection | The name of the MongoDB collection. | String | No | None | If you use the MongoDB connector for a source table, a regular expression can be used to match the name of the collection. Important If the name of the collection that you want to monitor contains special characters of regular expressions, you must provide a fully qualified namespace (database name.collection name). Otherwise, the changes to the collection cannot be captured. If you do not configure this parameter, all collections are monitored. |
|---|---|---|---|---|---|
| connectio n.options | The parameters that are specified to access the MongoDB database. | String | No | None | The parameters are key-value pairs that are in the key=value format and separated by ampersands ( & ), such as connectTimeoutMS=12000&socketTi meoutMS=13000. |

Source table-specific parameters

| Paramet er | Descriptio n | Data type | Required | Def ault valu e | Remarks |
|---|---|---|---|---|---|

| scan.start up.mode | The startup mode of the MongoDB CDC connector. | String | No | initi al | Valid values: initial: pulls all data from the initial offset. latest-offset: pulls change data from the current offset. timestamp: Pulls change data from a specific timestamp. For more information, see Startup Properties. |
|---|---|---|---|---|---|
| scan.start up.timest amp- millis | The start timestamp for the consumptio n at the specified offset. | Long | Depending on the value of the scan.startup. mode parameter: initial: no latest- offset: no timestamp: yes | Non e | The value of this parameter is the number of milliseconds that have elapsed since 00:00:00 UTC on January 1, 1970. The timestamp follows the UNIX time format. This parameter is required only when the scan.startup.mode parameter is set to timestamp . |
| initial.sna pshotting. queue.siz e | The maximum queue size for the initial snapshot phase. | Integer | No | 102 40 | This parameter takes effect only when the scan.startup.mode parameter is set to initial . |
| batch.siz e | The batch processing size of the cursor. | Integer | No | 102 4 | None. |
| poll.max. batch.siz e | The maximum number of change documents that can be processed in a batch. | Integer | No | 102 4 | This parameter determines the maximum number of change documents that can be pulled at a time during stream processing. A larger value of this parameter indicates a larger buffer that is allocated in the connector. |

| poll.await .time.ms | The interval at which data is pulled. | Integer | No | 100 0 | Unit: milliseconds. |
|---|---|---|---|---|---|
| heartbeat .interval. ms | The interval at which heartbeat packets are sent. | Integer | No | 0 | The default value indicates that the cache is never refreshed. Unit: milliseconds. The MongoDB CDC connector periodically sends heartbeat packets to the MongoDB database to ensure the latest backtracking status. If you set this parameter to 0, heartbeat packets are never sent. Important We strongly recommend that you specify this parameter for collections that are not frequently updated. |
| scan.incr emental.s napshot.e nabled | Specifies whether to enable the parallel reading mode in the initial snapshot phase. | Boolean | No | false | This is an experimental feature. |
| scan.incr emental.s napshot.c hunk.size. mb | The size of the shard when the parallel snapshot reading mode is enabled. | Integer | No | 64 | This is an experimental feature. Unit: MB. This parameter takes effect only when the parallel snapshot reading mode is enabled. |

| scan.full- changelo g | Specifies whether to generate a complete full changelog event stream. | Boolean | No | false | This is an experimental feature. Note This parameter is available only when the version of the MongoDB database is MongoDB 6.0 or later and the preimage and postimage features are enabled for the MongoDB database. For more information about how to enable the preimage and postimage features, see Document Preimages. |
|---|---|---|---|---|---|
| scan.flatt en- nested- columns. enabled | Specifies whether to read a nested field in a Binary JSON (BSON)- formatted document as a field whose name is separated with a period ( . ). | Boolean | No | false | If you set this parameter to true, the col field in the following BSON-formatted document is named nested.col in the obtained schema. {"nested":{"col":true}} Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. |
| scan.prim itive-as- string | Specifies whether to infer all basic data types in BSON- formatted documents as the STRING type. | Boolean | No | false | Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. |

Dimension table-specific parameters

| Paramete r | Description | Data type | Requ ired | Defa ult valu e | Remarks |
|---|---|---|---|---|---|

| lookup.cac he | The cache policy. | String | No | NON E | Valid values: None: No data is cached. Partial: Specific data that is looked up in an external database is cached. |
|---|---|---|---|---|---|
| lookup.ma x-retries | The maximum number of retries allowed when the database fails to be queried. | Integer | No | 3 | None. |
| lookup.retr y.interval | The interval between retries when the database fails to be queried. | Duratio n | No | 1s | None. |
| lookup.part ial- cache.expi re-after- access | The maximum period of time for which data records in the cache can be retained. | Duratio n | No | Non e | Unit: ms (milliseconds), s (seconds), min (minutes), h (hour), or d (day). To use this parameter, you must set the lookup.cache parameter to PARTIAL . |
| lookup.part ial- cache.expi re-after- write | The maximum period of time for which data records can be retained after they are written to the cache. | Duratio n | No | Non e | To use this parameter, you must set the lookup.cache parameter to PARTIAL . |
| lookup.part ial- cache.max -rows | The maximum number of data records that can be cached. If the number of data records that are cached exceeds the value of this parameter, the earliest data records expire. | Long | No | Non e | To use this parameter, you must set the lookup.cache parameter to PARTIAL . |

| lookup.part ial- cache.cach e-missing- key | Specifies whether to cache empty data records if no data is associated with the physical table. | Boolean | No | True | To use this parameter, you must set the lookup.cache parameter to PARTIAL . |
|---|---|---|---|---|---|

Sink table-specific parameters

| Paramete r | Description | Data type | Requir ed | Defa ult value | Remarks |
|---|---|---|---|---|---|
| sink.buffer- flush.max- rows | The maximum number of data records that can be written at a time. | Integer | No | 1000 | None. |
| sink.buffer- flush.interv al | The interval at which data is flushed. | Duratio n | No | 1s | None. |
| sink.deliver y- guarantee | The semantics used when data is written. | String | No | at- least- once | Valid values: none at-least-once Note The exactly-once semantics are not supported. |
| sink.max- retries | The maximum number of retries allowed when data fails to be written to the database. | Integer | No | 3 | None. |

| sink.retry.i nterval | The interval between retries when data fails to be written to the database. | Duratio n | No | 1s | None. |
|---|---|---|---|---|---|
| sink.parall elism | The degree of parallelism of the sink. | Integer | No | Left empt y | None. |

**Data type mappings**

MongoDB CDC source table

| Data type of BSON | Data type of Flink SQL |
|---|---|
| Int32 | INT |
| Int64 | BIGINT |
| Double | DOUBLE |
| Decimal128 | DECIMAL(p, s) |
| Boolean | BOOLEAN |
| Date Timestamp | DATE |
| Date Timestamp | TIME |
| DateTime | TIMESTAMP(3) TIMESTAMP LTZ(3) _ |
| Timestamp | TIMESTAMP(0) TIMESTAMP LTZ(0) _ |

| String ObjectId UUID Symbol MD5 JavaScript Regex | STRING |
|---|---|
| Binary | BYTES |
| Object | ROW |
| Array | ARRAY |
| DBPointer | ROW<$ref STRING, $id STRING> |
| GeoJSON | Point: ROW<type STRING, coordinates ARRAY<DOUBLE>> Line: ROW<type STRING, coordinates ARRAY<ARRAY< DOUBLE>>> |

Dimension table and sink table

| Data type of BSON | Data type of Flink SQL |
|---|---|
| Int32 | INT |
| Int64 | BIGINT |
| Double | DOUBLE |
| Decimal128 | DECIMAL |
| Boolean | BOOLEAN |
| DateTime | TIMESTAMP LTZ(3) _ |
| Timestamp | TIMESTAMP LTZ(0) _ |
| String ObjectId | STRING |

| Binary | BYTES |
|---|---|
| Object | ROW |
| Array | ARRAY |

**Sample code**

Sample code for a CDC source table

```
CREATE TEMPORARY TABLE mongo_source (
  `_id` STRING, --must be declared
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  db_name STRING METADATA FROM 'database_name' VIRTUAL,
  collection_name STRING METADATA VIRTUAL,
  op_ts TIMESTAMP_LTZ(3) METADATA VIRTUAL,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection',
  'scan.incremental.snapshot.enabled' = 'true',
  'scan.full-changelog' = 'true'
```

);

```
CREATE TEMPORARY TABLE productssink (
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price_amount DECIMAL,
  suppliers_name STRING,
  db_name STRING,
  collection_name STRING,
  op_ts TIMESTAMP_LTZ(3)
) WITH (
  'connector' = 'print',
  'logger' = 'true'
```

);

```
INSERT INTO productssink SELECT
  name,
  weight,
  tags,
  price.amount,
  suppliers[1].name,
  db_name,
  collection_name,
  op_ts
FROM
  mongo_source;
```

Sample code for a dimension table

```
CREATE TEMPORARY TABLE datagen_source (
  id STRING,
  a int,
  b BIGINT,
  `proctime` AS PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE mongo_dim (
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection',
  'lookup.cache' = 'PARTIAL',
  'lookup.partial-cache.expire-after-access' = '10min',
  'lookup.partial-cache.expire-after-write' = '10min',
  'lookup.partial-cache.max-rows' = '100'
```

);

```
CREATE TEMPORARY TABLE print_sink (
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price_amount DECIMAL,
  suppliers_name STRING
) WITH (
  'connector' = 'print',
  'logger' = 'true'
```

);

```
INSERT INTO print_sink SELECT
  T.id,
  T.a,
  T.b,
  H.name
FROM
  datagen_source AS T JOIN mongo_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T.id
= H._id;
```

Sample code for a sink table

```
CREATE TEMPORARY TABLE datagen_source (
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE mongo_sink (
  `_id` STRING,
  name STRING,
  weight DECIMAL,
  tags ARRAY<STRING>,
  price ROW<amount DECIMAL, currency STRING>,
  suppliers ARRAY<ROW<name STRING, address STRING>>,
  PRIMARY KEY(_id) NOT ENFORCED
) WITH (
  'connector' = 'mongodb',
  'hosts' = 'dds-bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,dds-
bp169b982fc25****.mongodb.rds.aliyuncs.com:3717,',
  'username' = 'root',
  'password' = '${secret_values.password}',
  'database' = 'flinktest',
  'collection' = 'flinkcollection'
```

);

```
INSERT INTO mongo_sink SELECT * FROM datagen_source;
```

**Metadata**

MongoDB CDC source tables support the metadata column syntax. The following table describes the metadata that you can access by using metadata columns.

| Metadata key | Metadata type | Description |
|---|---|---|
| database name _ | STRING NOT NULL | The name of the database to which the document belongs. |
| collection name _ | STRING NOT NULL | The name of the collection to which the document belongs. |
| op ts _ | TIMESTAMP LTZ(3) _ NOT NULL | The time when the document changes in the database. If the document is generated based on the historical data of the table instead of the changelog streams, the value of the metadata key is fixed to 0. |

**Preimage and postimage features**

By default, a MongoDB database whose version is earlier than 6.0 does not retain pre-change documents or deleted documents. If you do not enable the preimage and postimage features for a MongoDB database, the MongoDB database supports only the UPSERT semantics based on the data in the database. As a result, UPDATE_BEFORE messages are missing. However, multiple operators of Realtime Compute for Apache Flink require a complete changelog stream, which contains change messages, including INSERT, UPDATE_BEFORE, UPDATE_AFTER, and DELETE. To supplement the missing UPDATE_BEFORE messages, the Flink SQL planner automatically generates the ChangelogNormalize operator for data sources of the UPSERT change type. This operator caches the savepoints of the current version of all documents in the state data of deployments. If a document is updated or deleted, you can obtain the pre-update state of the document by querying the state data that is stored in the ChangelogNormalize operator. However, this method requires the operator to store a huge amount of state data. MongoDB 6.0 supports the preimage and postimage features for the MongoDB database. For more information about the preimage and postimage features, see Document Preimages. After the preimage and postimage features are enabled for the MongoDB database, the MongoDB database records the complete state data of a document in a specific collection each time the document changes. If you configure the `scan.full-changelog` parameter for your deployment, the MongoDB CDC connector can generate UPDATE_BEFORE messages from the collection that stores the state data of the change document. This helps generate a complete changelog event stream and the ChangelogNormalize operator is not used.

**Mongo CDC DataStream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink.

Create a DataStream API program and use MongoDBSource. Sample code:

```
MongoDBSource.builder()
  .hosts("mongo.example.com:27017")
  .username("mongouser")
  .password("mongopasswd")
  .databaseList("testdb")
  .collectionList("testcoll")
  .startupOptions(StartupOptions.initial())
  .deserializer(new JsonDebeziumDeserializationSchema())
  .build();
```

> **Note:** To enable the incremental snapshot feature when you use the DataStream API, use the
> `MongoDBSource#builder()` method in the
> `com.ververica.cdc.connectors.mongodb.source` package during the construction of the MongoDBSource data source. If you do not need to enable the incremental snapshot

|   | MongoDBSource#builder() |
|---|---|
| com.ververica.cdc.connectors.mongodb |   |

The following table describes the parameters that you must specify during the construction of the MongoDBSource data source.

| Parameter | Description |
|---|---|
| hosts | The hostname of the MongoDB database that you want to access. |
| username | The username of the MongoDB database service. Note If authentication is not enabled on the MongoDB server, you do not need to specify this parameter. |
| password | The password of the MongoDB database service. Note If authentication is not enabled on the MongoDB server, you do not need to specify this parameter. |
| databaseList | The name of the MongoDB database that you want to monitor. Note If you want to read data from multiple databases, you can set this parameter to a regular expression. You can use a combination of a period and an asterisk (.*) to match all databases. |
| collectionList | The name of the MongoDB collection that you want to monitor. Note If you want to read data from multiple collections, you can set this parameter to a regular expression. You can use .* to match all collections. |

| startupOptions | The startup mode of the MongoDB CDC connector. Valid values: StartupOptions.initial() Pulls all data from the initial offset. StartupOptions.latest-offset() Pulls change data from the current offset. StartupOptions.timestamp() Pulls change data from a specific timestamp. For more information, see Startup Properties. |
|---|---|
| deserializer | A deserializer, which deserializes SourceRecords to a specified type. Valid values: MongoDBConnectorDeserializationSchema: deserializes SourceRecords that are generated in Upsert mode into the internal data structure RowData of the Flink Table API or Flink SQL API. MongoDBConnectorFullChangelogDeserializationSchema: deserializes SourceRecords that are generated in full changelog mode into the internal data structure RowData of the Flink Table API or Flink SQL API. JsonDebeziumDeserializationSchema: deserializes SourceRecords into JSON strings. |

### 5.24 DataHub connector

This topic describes how to use the DataHub connector.

**Background information**

DataHub is a real-time data distribution platform designed to process streaming data. You can publish and subscribe to streaming data in DataHub and distribute the data to other platforms. DataHub allows you to analyze streaming data and build applications based on the streaming data.

> **Note:** DataHub is compatible with the Kafka protocol. You can use the standard Kafka connector instead of the Upsert Kafka connector to read data from or write data to DataHub.

The following table describes the capabilities supported by the DataHub connector.

| Item | Description |
|---|---|
| Table types | Source and sink |
| Running modes | Streaming mode and batch mode |
| Data formats | Not supported |

| Monitoring metrics | Not supported |
|---|---|
| API types | DataStream API and SQL API |
| Data updates or deletion in a sink | Not supported. The sink can write insert-only rows to the destination topic. |

**Syntax**

```
CREATE TEMPORARY TABLE datahub_input (
  `time` BIGINT,
  `sequence`  STRING METADATA VIRTUAL,
  `shard-id` BIGINT METADATA VIRTUAL,
  `system-time` TIMESTAMP METADATA VIRTUAL
) WITH (
  'connector' = 'datahub',
  'subId' = '<yourSubId>',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
```

);

**Parameters in the WITH clause**

Common parameters

| Paramet er | Descripti on | Data type | Requi red | Defau lt value | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | None | The value must be datahub. |
| endPoint | The consumer endpoint. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| project | The DataHub project name. | String | Yes | None | None. |
| topic | The DataHub topic name. | String | Yes | None | For DataHub topics of the BLOB type (for untyped and unstructured data), the corresponding Flink table must contain exactly one VARBINARY column. |

| accessId | The AccessKey ID of your Apsara Stack tenant account. | String | Yes | None | None. |
|---|---|---|---|---|---|
| accessKey | The AccessKey secret of your Apsara Stack tenant account. | String | Yes | None | None. |
| retryTime out | The maximum timeout period for a retry. | Integer | No | 18000 00 | We recommend that you use the default value. Unit: milliseconds. |
| retryInter val | The retry interval. | Integer | No | 1000 | We recommend that you use the default value. Unit: milliseconds. |
| enableSch emaRegis try | Specifies whether to enable schema registry. | Boolean | No | false | Set the option to true. |
| Compress Type | The compressi on policy for reads and writes. | String | No | lz4 | lz4: lz4 compression algorithm. deflate: deflate compression algorithm. "": an empty string, which indicates that data compression is disabled. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.5 or later supports this option. |

Source table-specific parameters

| Paramete r | Descriptio n | Data type | Requi red | Defa ult valu e | Remarks |
|---|---|---|---|---|---|

| subId | The subscription ID. | String | Yes | None | None. |
|---|---|---|---|---|---|
| maxFetchS ize | The number of data records that are read at a time. | Intege r | No | 50 | This parameter influences the read performance. You can set it to a bigger value to increase the read throughput. |
| maxBuffer Size | The maximum number of cached data records that are read asynchrono usly. | Intege r | No | 50 | This parameter influences the read performance. You can set it to a bigger value to increase the read throughput. |
| fetchLatest Delay | The sleep duration after which no data is fetched from the data source. | Intege r | No | 500 | Unit: milliseconds. If data is infrequently sent from the data source, specify a smaller value for this option to optimize read throughput. |

| lengthChec k | The rule for checking the number of fields per row. | String | No | NONE | NONE: If the number of fields that are parsed from a row is greater than the number of defined fields, data is extracted from left to right based on the number of defined fields. If the number of fields that are parsed from a row is less than the defined number of fields, this row is skipped. SKIP: If the number of fields that are parsed from a row is different from the number of defined fields, this row is skipped. EXCEPTION: If the number of fields that are parsed from a row is different from the defined number of fields, an exception is reported. PAD: Data is padded from left to right based on the order of defined fields. If the number of fields that are parsed from a row is greater than the number of defined fields, data is extracted from left to right based on the number of defined fields. If the number of fields that are parsed from a row is less than the defined number of fields, the values of the missing fields are padded with "Null" from left to right. |
|---|---|---|---|---|---|
| columnErr orDebug | Specifies whether to enable debugging. | Boolea n | No | false | false: disables debugging. true: enables debugging and prints the logs about parsing errors. |
| startTime | The time at which log consumptio n starts. | String | No | The curre nt time. | Format: yyyy-MM-dd hh:mm:ss. |
| endTime | The time at which log consumptio n is stopped. | String | No | None | Format: yyyy-MM-dd hh:mm:ss. |

Sink table-specific parameters

| Parameter | Description | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| batchCount | The number of rows that can be written at a time. | Intege r | No | 500 | Increasing the value improves write throughput at the cost of higher latency. |
| batchSize | The size of data that can be written at a time. | Intege r | No | 5120 00 | Increasing the value improves write throughput at the cost of higher latency. Unit: bytes. |
| flushInterva l | The data flush interval. | Intege r | No | 5000 | Increasing the value improves write throughput at the cost of higher latency. Unit: milliseconds. |
| hashFields | The column names. After column names are specified, the values of the columns with the same name are written to the same shard. | String | No | null (rand om write s) | Separate multiple column values with commas (,), for example, hashFields=a,b . The default value "null" indicates random writes. |
| timeZone | The time zone of the data. | String | No | None | The option value affects the conversion of TIMESTAMP fields between time zones. |
| schemaVers ion | The version in the registered schema. | Intege r | No | -1 | Specify this parameter. |

**Data type mappings**

| Realtime Compute for Apache Flink | DataHub |
|---|---|
| TINYINT | TINYINT |

| BOOLEAN | BOOLEAN |
|---|---|
| INTEGER | INTEGER |
| BIGINT | BIGINT |
| BIGINT | TIMESTAMP |
| TIMESTAMP |   |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL | DECIMAL |
| VARCHAR | STRING |
| SMALLINT | SMALLINT |
| VARBINARY | BLOB |

**Attribute fields**

| Field | Field type | Description |
|---|---|---|
| shard-id | BIGINT METADATA VIRTUAL | The shard ID. |
| sequence | STRING METADATA VIRTUAL | The data sequence. |
| system-time | TIMESTAMP METADATA VIRTUAL | The system time. |

**Sample code**

Sample code for a source table

```
CREATE TEMPORARY TABLE datahub_input (
  `time` BIGINT,
  `sequence`  STRING METADATA VIRTUAL,
  `shard-id` BIGINT METADATA VIRTUAL,
  `system-time` TIMESTAMP METADATA VIRTUAL
) WITH (
  'connector' = 'datahub',
  'subId' = '<yourSubId>',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
```

);

```
CREATE TEMPORARY TABLE test_out (
  `time` BIGINT,
  `sequence`  STRING,
  `shard-id` BIGINT,
  `system-time` TIMESTAMP
) WITH (
  'connector' = 'print',
  'logger' = 'true'
```

);

```
INSERT INTO test_out SELECT
  `time`,
  `sequence` ,
  `shard-id`,
  `system-time`
FROM datahub_input;
```

Sample code for a sink table

```
CREATE TEMPORARY table datahub_source(
  name VARCHAR
) WITH (
  'connector'='datahub',
  'endPoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'subId'='<yourSubId>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'startTime'='2018-06-01 00:00:00'
```

);

```
CREATE TEMPORARY table datahub_sink(
  name varchar
) WITH (
  'connector'='datahub',
  'endPoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'accessId'='${secret_values.ak_id}',
  'accessKey'='${secret_values.ak_secret}',
  'batchSize'='512000',
  'batchCount'='500'
```

);

```
INSERT INTO datahub_sink SELECT
  LOWER(name)
from datahub_source;
```

**Datastream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink.

**DataHub source**

Realtime Compute for Apache Flink provides the DatahubSourceFunction class that implements the SourceFunction interface. You can use the class to read data from a DataHub source. The following sample code shows how to read data from DataHub.

```xml
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); env.setParallelism(1); // Configure the connection. DatahubSourceFunction datahubSource =
    new DatahubSourceFunction(
    <yourEndPoint>,
    <yourProjectName>,
    <yourTopicName>,
    <yourSubId>,
    <yourAccessId>,
    <yourAccessKey>,
    "public",
    <enableSchemaRegistry>, // Specifies whether to enable schemaRegistry. This
parameter is set to false in most cases.
    <yourStartTime>,
    <yourEndTime>
```

);

```java
datahubSource.setRequestTimeout(30 * 1000); datahubSource.enableExitAfterReadFinished(); env.addSource(datahubSource)
    .map((MapFunction<RecordEntry, Tuple2<String, Long>>) this::getStringLongTuple2)
    .print();
env.execute(); private Tuple2<String, Long> getStringLongTuple2(RecordEntry recordEntry) {
    Tuple2<String, Long> tuple2 = new Tuple2<>();
    TupleRecordData recordData = (TupleRecordData) (recordEntry.getRecordData());
    tuple2.f0 = (String) recordData.getField(0);
    tuple2.f1 = (Long) recordData.getField(1);
    return tuple2;
```

`}`

**DataHub sink**

Realtime Compute for Apache Flink provides the OutputFormatSinkFunction class that implements the DatahubSinkFunction interface. You can use the class to write data to DataHub. The following sample code shows how to write data to DataHub.

```xml
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); // Configure the connection. env.generateSequence(0, 100)
    .map((MapFunction<Long, RecordEntry>) aLong -> getRecordEntry(aLong, "default:"))
    .addSink(
    new DatahubSinkFunction<>(
       <yourEndPoint>,
       <yourProjectName>,
       <yourTopicName>,
       <yourSubId>,
       <yourAccessId>,
       <yourAccessKey>,
       "public",
       <enableSchemaRegistry>, // Specifies whether to enable schemaRegistry. This
parameter is set to false in most cases.
       <schemaVersion> // If schemaRegistry is enabled, you must specify the value of s
chemaVersion for data writes. In other cases, you can set this schemaVersion to 0.
```

);

```java
env.execute(); private RecordEntry getRecordEntry(Long message, String s) {
    RecordSchema recordSchema = new RecordSchema();
    recordSchema.addField(new Field("f1", FieldType.STRING));
    recordSchema.addField(new Field("f2", FieldType.BIGINT));
    recordSchema.addField(new Field("f3", FieldType.DOUBLE));
    recordSchema.addField(new Field("f4", FieldType.BOOLEAN));
    recordSchema.addField(new Field("f5", FieldType.TIMESTAMP));
    recordSchema.addField(new Field("f6", FieldType.DECIMAL));
    RecordEntry recordEntry = new RecordEntry();
    TupleRecordData recordData = new TupleRecordData(recordSchema);
    recordData.setField(0, s + message);
    recordData.setField(1, message);
    recordEntry.setRecordData(recordData);
    return recordEntry;
```

`}`

**XML**

You can use the DataHub DataStream connectors of different versions stored in the Maven central repository.

```xml
<dependency>
    <groupId>com.alibaba.ververica</groupId>
    <artifactId>ververica-connector-datahub</artifactId>
    <version>${vvr-version}</version>
</dependency>
```

### 5.25 StarRocks connector

This topic describes how to use the StarRocks connector.

**Background information**

StarRocks is a new generation of Massively Parallel Processing (MPP) data warehouses that provide extremely fast query performance in all scenarios. StarRocks is dedicated to providing extremely fast and unified analytics experience. StarRocks provides the following benefits: Is compatible with the MySQL protocol. You can use a MySQL client or a common business intelligence (BI) tool to access StarRocks for data analytics. Uses a distributed architecture that provides the following capabilities: Horizontally splits tables and stores data in multiple replicas. Scales clusters in a flexible manner to support analytics of 10 PB of data. Supports the MPP architecture to accelerate data computing. Supports multiple replicas to ensure fault tolerance. Flink connectors cache data and use Stream Load to import data in batches to generate sink tables, and read data in batches to generate source tables. The following table describes the capabilities supported by the StarRocks connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | JSON and CSV |
| Monitoring metrics | None |
| API types | DataStream API and SQL API |
| Data updates or deletion in a sink table | Supported |

**Features**

StarRocks of E-MapReduce (EMR) supports the CREATE TABLE AS and CREATE DATABASE AS statements. The CREATE TABLE AS statement can be used to synchronize the schema and data of a single table. The CREATE DATABASE AS statement can be used to synchronize data of an entire database or the schema and data of multiple tables in the same database.

**Prerequisites**

A StarRocks cluster is created. The StarRocks cluster can be a StarRocks cluster of EMR or a self-managed StarRocks cluster that is hosted on Elastic Compute Service (ECS) instances.

**Limits**

Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.5 or later supports the StarRocks connector. The StarRocks connector supports only the at-least-once and exactly-once semantics.

**Syntax**

```
CREATE TABLE USER_RESULT(
 name VARCHAR,
 score BIGINT
 ) WITH (
 'connector' = 'starrocks',
 'jdbc-url'='jdbc:mysql://fe1_ip:query_port,fe2_ip:query_port,fe3_ip:query_port?xxxxx',
 'load-url'='fe1_ip:http_port;fe2_ip:http_port;fe3_ip:http_port',
 'database-name' = 'xxx',
 'table-name' = 'xxx',
 'username' = 'xxx',
 'password' = 'xxx'
```

);

**Parameters in the WITH clause**

| Cate gory | Paramete r | Description | Data type | Req uire d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|---|
| Com mon para mete rs | connector | The type of tables. | Strin g | Yes | None | Set the value to starrocks. |
|   | jdbc-url | The Java Database Connectivity (JDBC) URL that is used to connect to the database. | Strin g | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|   | database- name | The name of the StarRocks database. | Strin g | Yes | None | None. |
|   | table-name | The name of the StarRocks table. | Strin g | Yes | None | None. |
|   | username | The username that is used to connect to the StarRocks instance. | Strin g | Yes | None | None. |
|   | password | The password that is used to connect to the StarRocks instance. | Strin g | Yes | None | None. |

|   | starrocks.c reate.table. properties | The properties of the StarRocks table. | Strin g | No | None | The initial properties of the StarRocks table, such as the engine and the number of replicas, are specified. Example: 'starrocks.create.table.pro perties' = 'buckets 8','starrocks.create.table.p roperties' = 'replication num=1' _ |
|---|---|---|---|---|---|---|
|   | scan-url | The URL for data scan. | Strin g | No | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|   | scan.conne ct.timeout- ms | The timeout period for the StarRocks connector of Realtime Compute for Apache Flink to connect to the StarRocks database. If the connection duration exceeds the value of this parameter, an error is returned. | Strin g | No | 1000 | Unit: milliseconds. |
| Sour ce table - speci fic para mete rs |   |   |   |   |   |   |
|   | scan.para ms.keep- alive-min | The keep-alive period of the query task. | Strin g | No | 10 | None. |
|   | scan.para ms.query- timeout-s | The timeout period of the query task. If no query result is returned within the period specified by this parameter, the query task is stopped. | Strin g | No | 600 | Unit: seconds. |
|   | scan.para ms.mem- limit-byte | The maximum memory for a single query in a backend (BE) node. | Strin g | No | 1073 7418 24 (1 GB) | Unit: byte. |

|   | scan.max- retries | The maximum number of retries when a query fails. If the number of retries reaches the value of this parameter, an error is returned. | Strin g | No | 1 | None. |
|---|---|---|---|---|---|---|
|   | load-url | The URL for data import. | Strin g | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|   | sink.seman tic | The semantics for data writing. | Strin g | No | at- least - once | Valid values: at-least-once: The at- least-once semantics is used. This is the default value. exactly-once: The exactly-once semantics is used. |
|   | sink.buffer- flush.max- bytes | The maximum amount of data that is allowed in the buffer. | Strin g | No | 9437 1840 (90 MB) | Valid values: 64 MB to 10 GB. |
|   | sink.buffer- flush.max- rows | The maximum number of rows that are allowed in the buffer. | Strin g | No | 5000 00 | Valid values: 64000 to 5000000. |
| Sink table - speci fic para mete rs |   |   |   |   |   |   |
|   | sink.buffer- flush.interv al-ms | The interval at which the buffer is refreshed. | Strin g | No | 3000 00 | Valid values: 1000 to 3600000. Unit: milliseconds. |
|   | sink.max- retries | The maximum number of retries for writing data to the table. | Strin g | No | 1 | Valid values: 0 to 10. |
|   | sink.conne ct.timeout- ms | The timeout period for connecting to the StarRocks database. | Strin g | No | 1000 | Valid values: 100 to 60000. Unit: milliseconds. |

|   | sink.proper ties.* | The properties of the sink table. | Strin g | No | None | The import properties of Stream Load. For example, the sink.properties.format parameter specifies the format of data that is imported in Stream Load mode. The data format can be CSV or JSON. |
|---|---|---|---|---|---|---|
| Dime nsion table - speci fic para mete rs | lookup.cac he.enabled | Specifies whether to enable the dimension table cache mechanism. | Bool ean | No | true | Valid values: true After table data is read for the first time, it is cached to the memory. Subsequent requests directly read the memory data within the cache validity period to reduce I/O overheads. false Each query accesses the data source. |

**Data type mappings**

| Data type of StarRocks | Data type of Realtime Compute for Apache Flink |
|---|---|
| NULL | NULL |
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| LARGEINT | STRING |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DATE | DATE |

| DATETIME | TIMESTAMP |
|---|---|
| DECIMAL | DECIMAL |
| DECIMALV2 | DECIMAL |
| DECIMAL32 | DECIMAL |
| DECIMAL64 | DECIMAL |
| DECIMAL128 | DECIMAL |
| CHAR | CHAR |
| VARCHAR | STRING |

**Sample code**

```
CREATE TEMPORARY TABLE IF NOT EXISTS `runoob_tbl_source` (
  `runoob_id` BIGINT NOT NULL,
  `runoob_title` STRING NOT NULL,
  `runoob_author` STRING NOT NULL,
  `submission_date` DATE NULL
) WITH (
  'connector' = 'starrocks',
  'jdbc-url' = 'jdbc:mysql://ip:9030',
  'scan-url' = 'ip:18030',
  'database-name' = 'db_name',
  'table-name' = 'table_name',
  'password' = 'xxxxxxx',
  'username' = 'xxxxx'
```

);

```
CREATE TEMPORARY TABLE IF NOT EXISTS `runoob_tbl_sink` (
  `runoob_id` BIGINT NOT NULL,
  `runoob_title` STRING NOT NULL,
  `runoob_author` STRING NOT NULL,
  `submission_date` DATE NULL
  PRIMARY KEY(`runoob_id`)
  NOT ENFORCED
) WITH (
  'jdbc-url' = 'jdbc:mysql://ip:9030',
  'connector' = 'starrocks',
  'load-url' = 'ip:18030',
  'database-name' = 'db_name',
  'table-name' = 'table_name',
  'password' = 'xxxxxxx',
  'username' = 'xxxx',
  'sink.buffer-flush.interval-ms' = '5000'
```

);

```
INSERT INTO runoob_tbl_sink SELECT * FROM runoob_tbl_source;
```

### 5.26 SLS connector

This topic describes how to use the Simple Log Service (SLS) connector.

**Background information**

SLS is an end-to-end data logging service that is developed by Alibaba Cloud. SLS allows you to collect, consume, ship, query, and analyze log data in a quick manner. It improves the O&M efficiency and provides the capability to process large amounts of log data. The following table describes the capabilities supported by the SLS connector.

| Item | Description |
|---|---|
| Table types | Source table and sink table |

| Running modes | Streaming mode |
|---|---|
| Monitoring metrics | None |
| Data formats | None |
| API types | SQL |
| Data updates or deletion in a sink table | Data in a sink table cannot be updated or deleted. Data can only be inserted into a sink table. |

**Features**

The SLS source connector can be used to read the attribute fields of messages. The following table describes the attribute fields supported by the SLS source connector.

| Field | Field data type | Description |
|---|---|---|
| source __ __ | STRING METADATA VIRTUAL | The message source. |
| topic __ __ | STRING METADATA VIRTUAL | The message topic. |
| timestamp __ __ | BIGINT METADATA VIRTUAL | The time when the log is generated. |
| tag __ __ | MAP<VARCHAR, VARCHAR> METADATA VIRTUAL | The mesasge tag. The " tag : receive time ":"1616742274" , __ __ __ _ __ ' receive time ' , and '1616742274' attributes are __ _ __ logged as key-value pairs in a map and accessed in tag [' receive time '] mode in SQL. __ __ __ _ __ |

|   | " tag : receive time ":"1616742274" __ __ __ _ __ |
|---|---|
| ' receive time ' __ _ __ |   |

**Prerequisites**

An SLS project and a Logstore are created.

**Limits**

The SLS connector supports only the at-least-once semantics. We recommended that you do not set the deployment parallelism for a source node to a value greater than the number of shards. If the deployment parallelism for a source node is greater than the number of shards, resources may be wasted. In Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.5 or earlier, if the number of shards changes, automatic failovers of deployments may become invalid and specific shards may not be consumed.

**Syntax**

```
CREATE TABLE sls_table(
  a INT,
  b INT,
  c VARCHAR
) WITH (
  'connector' = 'sls',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'logStore' = '<yourLogStoreName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}'
```

);

**Parameters in the WITH clause**

Common parameters

| Parameter | Description | Data type | Requi red | Def aul t val ue | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | Non e | Set the value to sls. |
| endPoint | The endpoint of SLS. | String | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |
| project | The name of the SLS project. | String | Yes | Non e | None. |
| logStore | The name of a Logstore or Metricstore of SLS. | String | Yes | Non e | Data in a Logstore is consumed in the same way as in a Metricstore. |
| accessId | The AccessKey ID of your Apsara Stack tenant account. | String | Yes | Non e | None. |

| accessKey | The AccessKey secret of your Apsara Stack tenant account. | String | Yes | Non e | None. |
|---|---|---|---|---|---|

Source table-specific parameters

| Param eter | Descripti on | Data type | Require d | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| startTi me | The time at which log consumpti on starts. | String | No | The curre nt time. | The value of this parameter is in the yyyy-MM-dd hh:mm:ss format. Note The startTime and stopTime parameters are configured based on the receive time attribute __ _ __ field in an SLS source table not the timestamp attribute field. __ __ |
| stopTim e | The time at which log consumpti on is stopped. | String | No | None | Format: yyyy-MM-dd hh:mm:ss. Note If you want Realtime Compute for Apache Flink to exit after log consumption is complete, you must configure the exitAfterFinish parameter together with this parameter and set the exitAfterFinish parameter to true. |

| consum erGrou p | The name of the consumer group. | String | No | None | A consumer group records the consumption progress. You can specify a custom consumer group name. The format of the name is not fixed. Note A consumer group cannot be shared by multiple deployments for collaborative consumption. We recommend that you specify different consumer groups for different Realtime Compute for Apache Flink deployments. If you specify the same consumer group for different Realtime Compute for Apache Flink deployments, all data is consumed. When Realtime Compute for Apache Flink consumes data of SLS, the data is not sharded in an SLS consumer group. Therefore, if the deployments share the same consumer group, all messages in the consumer group are consumed by each deployment. |
|---|---|---|---|---|---|

| consum eFromC heckpoi nt | Specifies whether to consume logs from the checkpoin t that is stored in the specified consumer group. | String | No | false | Valid values: true: If you set this parameter to true, you must specify a consumer group. After you specify a consumer group, Realtime Compute for Apache Flink consumes logs from the checkpoint that is stored in the consumer group. If no checkpoint exists in the consumer group, Realtime Compute for Apache Flink consumes logs from the time specified by the startTime parameter. false: Realtime Compute for Apache Flink does not consume logs from the checkpoint that is stored in the specified consumer group. This is the default value. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.5 or later supports this parameter. |
|---|---|---|---|---|---|
| directM ode | Specifies whether to enable the direct connectio n mode of SLS. | String | No | false | Valid values: true: enables the direct connection mode. false: disables the direct connection mode. This is the default value. |
| maxRet ries | The number of retries that are allowed when data fails to be read from SLS. | String | No | 3 | None. |
| batchG etSize | The number of log groups from which data is read in a request. | String | No | 100 | The value of the batchGetSize parameter cannot exceed 1000. Otherwise, an error is returned. |

| exitAfte rFinish | Specifies whether Realtime Compute for Apache Flink exits after data consumpti on is complete. | String |   | No | false | Valid values: true: Realtime Compute for Apache Flink exits after data consumption is complete. false: Realtime Compute for Apache Flink does not exit after data consumption is complete. This is the default value. |   |   |
|---|---|---|---|---|---|---|---|---|
| query | The query statement that is used to preproces s data before data consumpti on in SLS. | String |   |   |   | If you configure the query parameter, Realtime Compute for Apache Flink can filter out data from SLS before Realtime Compute for Apache Flink consumes data in SLS. This helps prevent Realtime Compute for Apache Flink from consuming all data in SLS. This reduces costs and improves data processing efficiency. For example, if you execute the 'query' = '*\| where request method = ''GET''' _ statement, Realtime Compute for Apache Flink matches the data whose value of the request method field is _ equal to the value of the GET clause before Realtime Compute for Apache Flink reads data from a Logstore of SLS. The query must use the Search Processing Language (SPL) of SLS. Important Only Realtime Compute for Apache Flink that uses VVR 8.0.1 or later supports this parameter. This feature is free during public preview. A service fee of SLS may be charged in later versions. |   |   |
|   |   |   |   |   |   |   | 'query' = '*\| where |   |
|   |   |   |   |   |   | request method = ''GET''' _ |   |   |
|   |   |   |   | No | None |   |   |   |

Sink table-specific parameters

| Paramet er | Description | Data type | Req uire d | Defau lt value | Remarks |
|---|---|---|---|---|---|

| topicField | Specifies a field name. The value of this parameter overwrites the value of the topic attribute __ __ field to indicate the topic of the log. | String | No | None | The value of this parameter must be an existing field in the table. |
|---|---|---|---|---|---|
| timeField | Specifies a field name. The value of this parameter overwrites the value of the timestamp __ __ attribute field to indicate the log write time. | String | No | The curren t time. | The value of this parameter must be an existing field of the INT type in the table. If no field is specified, the current time is used by default. |
| sourceFiel d | Specifies a field name. The value of this parameter overwrites the value of the source __ __ attribute field to indicate the origin of the log. For example, the value is the IP address of the machine that generates the log. | String | No | None | The value of this parameter must be an existing field in the table. |
| partitionFi eld | Specifies a field name. A hash value is calculated based on the value of this parameter when data is written to SLS. Data that includes the same hash value is written to the same shard. | String | No | None | If you do not specify this parameter, each data entry is randomly written to an available shard. |

| buckets | The number of buckets that are regrouped based on the hash value when the partitionField parameter is specified. | String | No | 64 | Valid values: [1,256]. The value of this parameter must be an integer power of 2. The number of buckets must be greater than or equal to the number of shards. Otherwise, no data is written to specific shards. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.5 or later supports this parameter. |
|---|---|---|---|---|---|
| flushInter valMs | The interval at which data writing is triggered. | String | No | 2000 | Unit: milliseconds. |
| writeNullP roperties | Specifies whether to write null values as empty strings to SLS. | Boolean | No | true | Valid values: true: Null values are written as empty strings to SLS. This is the default value. false: Null values are not written to SLS. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. |

**Data type mappings**

| Data type in Realtime Compute for Apache Flink | Data type of SLS |
|---|---|
| BOOLEAN | STRING |
| VARBINARY |   |
| VARCHAR |   |
| TINYINT |   |
| INTEGER |   |

| BIGINT |   |
|---|---|
| FLOAT |   |
| DOUBLE |   |
| DECIMAL |   |

**Sample code**

```
CREATE TEMPORARY TABLE sls_input(
  `time` BIGINT,
  url STRING,
  dt STRING,
  float_field FLOAT,
  double_field DOUBLE,
  boolean_field BOOLEAN,
  `__topic__` STRING METADATA VIRTUAL,
  `__source__` STRING METADATA VIRTUAL,
  `__timestamp__` STRING METADATA VIRTUAL,
   __tag__ MAP<VARCHAR, VARCHAR> METADATA VIRTUAL,
  proctime as PROCTIME()
) WITH (
  'connector' = 'sls',
  'endpoint' ='cn-hangzhou.log.aliyuncs.com',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'starttime' = '2023-08-30 00:00:00',
  'project' ='sls-test',
  'logstore' ='sls-input'
```

);

```
CREATE TEMPORARY TABLE sls_sink(
  `time` BIGINT,
  url STRING,
  dt STRING,
  float_field FLOAT,
  double_field DOUBLE,
  boolean_field BOOLEAN,
  `__topic__` STRING,
  `__source__` STRING,
  `__timestamp__` BIGINT ,
  receive_time BIGINT
) WITH (
  'connector' = 'sls',
  'endpoint' ='cn-hangzhou.log.aliyuncs.com',
  'accessId' = '${ak_id}',
  'accessKey' = '${ak_secret}',
  'project' ='sls-test',
  'logstore' ='sls-output'
```

`)` );

```
INSERT INTO sls_sink SELECT
 `time`,
  url,
  dt,
  float_field,
  double_field,
  boolean_field,
  `__topic__` ,
  `__source__` ,
  `__timestamp__` ,
  cast(__tag__['__receive_time__'] as bigint) as receive_time
FROM sls_input;
```

**DataStream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink. The SLS DataStream connectors of different versions are stored in the Maven central repository.

Read data from SLS VVR of Realtime Compute for Apache Flink provides the implementation class SlsSourceFunction of SourceFunction to read data from SLS. Sample code:

```java
public class SlsDataStreamSource {
    public static void main(String[] args) throws Exception {
        // Sets up the streaming execution environment
        final StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        // Creates and adds SLS source and sink.
        env.addSource(createSlsSource())
                .map(SlsDataStreamSource::convertMessages)
                .print();
        env.execute("SLS Stream Source");
```

`}`

```java
    private static SlsSourceFunction createSlsSource() {
        SLSAccessInfo accessInfo = new SLSAccessInfo();
        accessInfo.setEndpoint("yourEndpoint");
        accessInfo.setProjectName("yourProject");
        accessInfo.setLogstore("yourLogStore");
        accessInfo.setAccessId("yourAccessId");
        accessInfo.setAccessKey("yourAccessKey");
        // The batch get size must be given.
        accessInfo.setBatchGetSize(10);
        // Optional parameters
```

`//` `p` `p`

```
        accessInfo.setConsumerGroup("yourConsumerGroup");
        accessInfo.setMaxRetries(3);
        // time to start consuming, set to current time.
        int startInSec = (int) (new Date().getTime() / 1000);
        // time to stop consuming, -1 means never stop.
        int stopInSec = -1;
        return new SlsSourceFunction(accessInfo, startInSec, stopInSec);
```

`}`

```java
    private static List<String> convertMessages(SourceRecord input) {
        List<String> res = new ArrayList<>();
        for (FastLogGroup logGroup : input.getLogGroups()) {
            int logsCount = logGroup.getLogsCount();
            for (int i = 0; i < logsCount; i++) {
                FastLog log = logGroup.getLogs(i);
                int fieldCount = log.getContentsCount();
                for (int idx = 0; idx < fieldCount; idx++) {
                    FastLogContent f = log.getContents(idx);
                    res.add(String.format("key: %s, value: %s", f.getKey(), f.getValue
()));
```

`}` `}` `}`

```
        return res;
```

`}` `}` Write data to SLS VVR of Realtime Compute for Apache Flink provides the implementation class SLSOutputFormat of OutputFormat to write data to SLS. Sample code:

```java
public class SlsDataStreamSink {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
        env.fromSequence(0, 100)
                .map((MapFunction<Long, SinkRecord>) aLong -> getSinkRecord(aLong))
                .addSink(createSlsSink())
                .name(SlsDataStreamSink.class.getSimpleName());
        env.execute("SLS Stream Sink");
```

`}`

```java
    private static OutputFormatSinkFunction createSlsSink() {
        Configuration conf = new Configuration();
        conf.setString(SLSOptions.ENDPOINT, "yourEndpoint");
        conf.setString(SLSOptions.PROJECT, "yourProject");
        conf.setString(SLSOptions.LOGSTORE, "yourLogStore");
        conf.setString(SLSOptions.ACCESS_ID, "yourAccessId");
        conf.setString(SLSOptions.ACCESS_KEY, "yourAccessKey");
        SLSOutputFormat outputFormat = new SLSOutputFormat(conf);
        return new OutputFormatSinkFunction<>(outputFormat);
```

`}`

```java
    private static SinkRecord getSinkRecord(Long seed) {
        SinkRecord record = new SinkRecord();
        LogItem logItem = new LogItem((int) (System.currentTimeMillis() / 1000));
        logItem.PushBack("level", "info");
        logItem.PushBack("name", String.valueOf(seed));
        logItem.PushBack("message", "it's a test message for " + seed.toString());
        record.setContent(logItem);
        return record;
```

`}` `}`

### 5.27 Apache Paimon

We recommend that you use the Apache Paimon connector together with Apache Paimon catalogs. This topic describes how to use the Apache Paimon connector.

**Background information**

Apache Paimon is a unified lake storage that allows you to process data in streaming and batch modes. Apache Paimon supports data writing with high throughput and data queries with low latency. Apache Paimon is compatible with common computing engines of Alibaba Cloud E-MapReduce (EMR), such as Flink, Spark, Hive, and Trino. You can use Apache Paimon to deploy your data lake storage service on Apsara File Storage for HDFS (HDFS) or Object Storage Service (OSS) in an efficient manner, and connect to the preceding computing engines to perform data lake analytics. For more information, visit Apache Paimon.

| Item | Description |
|---|---|

| Supported type | Source table, dimension table, and sink table |
|---|---|
| Mode | Streaming mode and batch mode |
| Data format | None |
| Metrics | None |
| API type | SQL |
| Data updates or deletion in a sink table | Supported |

**Features**

Apache Paimon provides the following features: Low-cost lightweight data lake storage service based on HDFS or OSS. Reading and writing large numbers of datasets in streaming and batch modes. Batch queries and online analytical processing (OLAP) queries within minutes or even seconds. Consumption and generation of incremental data. Apache Paimon can be used as storage for a traditional offline data warehouse and a streaming data warehouse. Data pre-aggregation to reduce storage costs and downstream computing workloads. Data backtracking of historical versions. Efficient data filtering. Table schema changes.

**Syntax**

If you create an Apache Paimon table in an Apache Paimon catalog, you do not need to specify the `connector` parameter. The following sample code shows the syntax for creating an Apache Paimon table in an Apache Paimon catalog:

```
CREATE TABLE `<your-paimon-catalog>`.`<your-db>`.paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  ...
```

);

> **Note:** If you have created an Apache Paimon table in the Apache Paimon catalog, you can directly use the table without the need to create another table.

If you want to create a temporary Apache Paimon table in a catalog of storage other than Apache Paimon, you must specify the connector parameter and the storage path of the Apache Paimon table. The following sample code shows the syntax for creating an Apache Paimon table in such a catalog:

```
CREATE TEMPORARY TABLE paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' = 'paimon',
  'path' = '<path-to-paimon-table-files>',
  'auto-create'='true', -- If no Apache Paimon table file exists in the specified pat
h, a file is automatically created.
  ...
```

);

**Parameters for the WITH clause**

| Param eter | Description | Data type | Req uir ed | Def ault val ue | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | String | No | No defa ult valu e. | If you create an Apache Paimon table in an Apache Paimon catalog, you do not need to specify this parameter. If you create a temporary Apache Paimon table in a catalog of storage other than Apache Paimon, set the value to paimon . |
| path | The storage path of the table. | String | No | No defa ult valu e. | If you create an Apache Paimon table in an Apache Paimon catalog, you do not need to specify this parameter. If you create a temporary Apache Paimon table in a catalog of storage other than Apache Paimon, set this parameter to the HDFS or OSS directory in which you want to store the table. |

| auto- create | Specifies whether to automatically create an Apache Paimon table file if no Apache Paimon table file exists in the specified path when you create a temporary Apache Paimon table. | Boolean |   | No | fals e | Valid values: false: If no Apache Paimon table file exists in the specified path, an error is returned. This is the default value. true: If the specified path does not exist, the system automatically creates an Apache Paimon table file. |   |   |
|---|---|---|---|---|---|---|---|---|
| bucket | The number of buckets in each partition. | Integer |   | No | 1 | Data written to the Apache Paimon table is distributed to each bucket based on the columns that are specified by the bucket-key parameter. Note We recommend that the data in each bucket be less than 5 GB in size. |   |   |
| bucket- key | The bucket key columns. | String |   |   |   | The columns based on which the data written to the Apache Paimon table is distributed to different buckets. Separate column names with commas (,). For example, 'bucket-key' = 'order id,cust id' indicates that _ _ data is distributed to buckets based on the order id and cust id columns. _ _ Note If you do not configure this parameter, data is distributed based on the primary key. If no primary key is specified for the Apache Paimon table, data is distributed based on the values of all columns. |   |   |
|   |   |   |   |   |   |   | 'bucket-key' = |   |
|   |   |   |   |   |   | 'order id,cust id' _ _ |   |   |
|   |   |   |   | No | No defa ult valu e. |   |   |   |

| changel og- produc er | The incremental data generation mechanism. | String | No | non e | Apache Paimon can generate complete incremental data for any input data stream to facilitate downstream data consumption. Each UPDATE AFTER data _ record corresponds to an UPDATE BEFORE data record. Valid _ values: none: No incremental data is generated. This is the default value. The downstream consumer can read data from the Apache Paimon table in streaming mode. However, the incremental data that is read by the downstream consumer contains only UPDATE AFTER data and does not _ contain UPDATE BEFORE data. _ input: The input data streams are written to an incremental data file as incremental data in dual-write mode. full-compaction: Complete incremental data is generated each time full compaction is performed. lookup: Complete incremental data is generated before commit snapshot is performed. |
|---|---|---|---|---|---|
| full- compac tion.del ta- commit s | The maximum interval at which full compaction is performed. | Integer | No | No defa ult valu e. | A full compaction is definitely triggered when the number of commit snapshots reaches the value of this parameter. |
| lookup. cache- max- memor y-size | The memory cache size of the Apache Paimon dimension table. | String | No | 256 MB | The value of this parameter determines the cache sizes of both the dimension table and the lookup changelog producer. |
| merge- engine | The mechanism for merging data that has the same primary key. | String | No | ded upli cate | Valid values: deduplicate: Only the latest data record is retained. partial-update: Existing data that has the same primary key as the latest data is overwritten by the latest data in the non-null columns. Data in other columns remains unchanged. aggregation: An aggregate function is specified to perform pre-aggregation. |

| partial- update. ignore- delete | Specifies whether to ignore delete messages when the merge-engine parameter is set to partial- update. | Boolean | No | fals e | Valid values: true: Delete messages are ignored. false: If a delete message appears, the Flink system reports an error. Note Whether delete messages need to be ignored depends on the actual scenario. You need to specify this parameter based on your business requirements. |
|---|---|---|---|---|---|
| partitio n.defau lt-name | The default name of the partition. | String | No | D __ EFA ULT PA _ RTIT ION _ _ | If the value of a partition key column is null or an empty string, the value of this parameter is used as the partition name. |
| partitio n.expir ation- check- interval | The interval at which the system checks partition expiration. | String | No | 1h | None. |
| partitio n.expir ation- time | The validity period of a partition. | String | No | No defa ult valu e. | If the period of time for which a partition exists exceeds the value of this parameter, the partition expires. By default, a partition never expires. |
| partitio n.times tamp- formatt er | The pattern that is used to convert a time string into a timestamp. | String | No | No defa ult valu e. | The format of the partition validity period converted from the partition.expiration- time parameter. |

| partitio n.times tamp- pattern | The pattern that is used to convert a partition value into a time string. | String | No | No defa ult valu e. | The format of the partition validity period converted from the partition.expiration- time parameter. |
|---|---|---|---|---|---|
| scan.bo unded. waterm ark | The end condition for bounded streaming mode. If the watermark of data in an Apache Paimon source table exceeds the value of this parameter, the generation of data in the Apache Paimon source table ends. | Long | No | No defa ult valu e. | None. |
| scan.m ode | The consumer offset of the Apache Paimon source table. | String | No | defa ult | None. |
| scan.sn apshot- id | The ID of the snapshot from which the Apache Paimon source table starts to consume data. | Integer | No | No defa ult valu e. | None. |
| scan.ti mesta mp- millis | The point in time from which the Apache Paimon source table starts to consume data. | Integer | No | No defa ult valu e. | None. |
| snapsh ot.num- retaine d.max | The maximum number of the latest snapshots that can be retained. | Integer | No | 214 748 364 7 | The snapshot expiration is triggered only if the condition specified by the snapshot.num-retained.max parameter or the snapshot.time-retained parameter is met and the condition specified by the snapshot.num-retained.min parameter is met. |

| snapsh ot.num- retaine d.min | The minimum number of the latest snapshots that can be retained. | Integer | No | 10 | None. |
|---|---|---|---|---|---|
| snapsh ot.time- retaine d | The duration for which snapshots can be retained. | String | No | 1h | The snapshot expiration is triggered only if the condition specified by the snapshot.num-retained.max parameter or the snapshot.time-retained parameter is met and the condition specified by the snapshot.num-retained.min parameter is met. |
| write- mode | The write mode of the Apache Paimon table. | String | No | cha nge- log | Valid values: change-log: Data is inserted into, deleted from, and updated in the Apache Paimon table based on the primary key. append-only: The Apache Paimon table allows only data insertion and does not support operations based on the primary key. This mode is more efficient than the change-log mode. |
| scan.inf er- paralleli sm | Specifies whether to automatically infer the degree of parallelism of the Apache Paimon source table. | Boolean | No | fals e | Valid values: true: The parallelism of the Apache Paimon source table is automatically inferred based on the number of buckets. false: The default degree of parallelism that is configured based on Ververica Platform (VVP) is used. If the resource configuration is in expert mode, the degree of parallelism that is configured is used. |
| scan.pa rallelis m | The degree of parallelism of the Apache Paimon source table. | Integer | No | No defa ult valu e. | None. |
| sink.par allelism | The parallelism of the Apache Paimon sink table. | Integer | No | No defa ult valu e. | None. |

> **Note:** For more information about the configuration items, see Configuration.

**Feature description**

**Data freshness and consistency assurance**

An Apache Paimon sink table uses the two-phase commit protocol (2PC) to commit the written data each time a checkpoint is generated in a Flink deployment. Therefore, the data freshness is based on the checkpoint interval of the Flink deployment. A maximum of two snapshots can be generated each time data is committed. If two Flink deployments write data to an Apache Paimon table at the same time but write data to different buckets, serializable consistency is ensured. If the Flink deployments write data to the same bucket, only isolation-level consistency of snapshots is ensured. In this case, the table may contain the results of the two deployments, but no data is lost.

**Data merging mechanism**

When an Apache Paimon sink table receives multiple data records that have the same primary key, the Apache Paimon sink table merges the data records into one data record to ensure the uniqueness of the primary key. You can specify the `merge-engine` parameter to specify the data merging mechanism. The following table describes the different data merging mechanisms.

| Data merging mechanis m | Description |
|---|---|
| deduplicat e | This is the default value of the merge-engine parameter. If the data merging mechanism is deduplicate and multiple data records have the same primary key, the Apache Paimon sink table retains only the latest data record and discards other data records. Note If the latest data record is a delete message, all the data records that have the same primary key are discarded. |

| partial- update | The partial-update mechanism allows you to use multiple messages to update data and finally obtain complete data. New data that has the same primary key as the existing data overwrites the existing data. Columns that have NULL values cannot overwrite existing data. For example, the Apache Paimon sink table receives the following data records in sequence: <1, 23.0, 10, NULL> <1, NULL, NULL, 'This is a book'> <1, 25.2, NULL, NULL> If the first column is the primary key, the final result is <1, 25.2, 10, 'This is a book'>. Note If you want the Apache Paimon sink table to read the result that is obtained by using the partial-update mechanism in streaming mode, you must set the changelog-producer parameter to lookup or full-compaction. When you use the partial-update mechanism, delete messages cannot be processed. You can set the partial-update.ignore-delete parameter to true to ignore delete messages. |
|---|---|

| aggregatio n | In specific scenarios, you may require only the aggregated values. The aggregation mechanism can aggregate data that has the same primary key based on the specified aggregate function. You must use fields.<field-name>.aggregate-function to specify an aggregate function for each column that is not the primary key. If you do not specify an aggregate function for a column that is not the primary key, the column uses the last non null value aggregate function by default. The following sample code _ _ _ provides an example on how to create an Apache Paimon table by using the aggregation mechanism: CREATE TABLE MyTable ( product id BIGINT, _ price DOUBLE, sales BIGINT, PRIMARY KEY (product id) NOT ENFORCED _ ) WITH ( 'merge-engine' = 'aggregation', 'fields.price.aggregate-function' = 'max', 'fields.sales.aggregate-function' = 'sum' ); In this example, data in the price column is aggregated based on the max function, and data in the sales column is aggregated based on the sum function. If the input data records are <1, 23.0, 15> and <1, 30.2, 20>, the result is <1, 30.2, 35>. Mappings between the supported aggregate functions and data types: sum: DECIMAL, TINYINT, SMALLINT, INTEGER, BIGINT, FLOAT, and DOUBLE min and max: DECIMAL, TINYINT, SMALLINT, INTEGER, BIGINT, FLOAT, DOUBLE, DATE, TIME, TIMESTAMP, and TIMESTAMP LTZ _ last value and last non null value: all data types _ _ _ _ listagg: STRING bool and and bool or: BOOLEAN _ _ Note Only the sum function supports data retraction and deletion. If you want specific columns to ignore retraction and deletion messages, you can specify 'fields.${field name}.ignore-retract'='true' . _ If you want the Apache Paimon sink table to read the aggregation result in streaming mode, you must set the changelog-producer parameter to lookup or full-compaction. |
|---|---|

**Incremental data generation mechanism**

The incremental data generation mechanism is specified by the changelog-producer parameter. Apache Paimon can generate complete incremental data for any input data stream. Each UPDATE_AFTER data record corresponds to an UPDATE_BEFORE data record. The following table describes all incremental data generation mechanisms.

| Increm ental data generat ion mechan ism | Description |
|---|---|
| None | This is the default value of the changelog-producer parameter. If you use the default value, the Apache Paimon source table of the downstream consumer can obtain only the latest situation of data when specific data records have the same primary key. In this case, the downstream consumer cannot learn the complete incremental data to effectively calculate data. The downstream consumer can view the latest data and determine whether existing data is deleted, but cannot learn more information about the deleted data. For example, if the downstream consumer wants to calculate the sum of a column and the consumer obtains only the latest value 5, the downstream consumer cannot determine how to update the sum. If the original value is 4, the sum should be increased by 1. If the original value is 6, the sum should be decreased by 1. This type of consumer is sensitive to UPDATE BEFORE data. For this type of consumer, we recommend that you do not set _ the changelog-producer parameter to none. However, other incremental data generation mechanisms may cause performance loss. Note If your downstream consumer is a database that is not sensitive to UPDATE BEFORE _ data, you can set the changelog-producer parameter to none. We recommend that you specify this parameter based on your business requirements. |
| Input | If you set the changelog-producer parameter to input, the Apache Paimon sink table writes input data streams to an incremental data file as incremental data in dual-write mode. Therefore, this incremental data generation mechanism can be used only when the input data streams, such as Change Data Capture (CDC) data, are complete. |
| Lookup | If you set the changelog-producer parameter to lookup, the Apache Paimon sink table uses a point query mechanism that is similar to a dimension table to generate complete incremental data that corresponds to the savepoint before commit savepoint is performed. The incremental data generation mechanism allows the Apache Paimon sink table to generate complete incremental data regardless of whether the input incremental data is complete. The lookup mechanism is more efficient than the full-compaction mechanism in the generation of incremental data. However, the lookup mechanism consumes more resources. We recommend that you use the lookup mechanism in scenarios in which the requirement for the freshness of incremental data is high. For example, incremental data within minutes is required. |

| Full Compac tion | If you set the changelog-producer parameter to full-compaction, the Apache Paimon sink table generates complete incremental data each time full compaction is performed. The incremental data generation mechanism allows the Apache Paimon sink table to generate complete incremental data regardless of whether the input incremental data is complete. The time interval at which full compaction is performed is specified by the full-compaction.delta-commits parameter. Compared with the lookup mechanism, the full compaction mechanism is less efficient in generating incremental data. However, the full compaction mechanism does not cause additional computations based on the full compaction process of data. Therefore, fewer resources are consumed. We recommend that you use the full compaction mechanism in scenarios where the requirement for the freshness of incremental data is not high. For example, incremental data within hours is required. |
|---|---|

**Write mode**

The following table describes the write modes supported by Apache Paimon tables.

| Write mode | Description |   |   |
|---|---|---|---|
| Change- log | change-log is the default write mode for Apache Paimon tables. In change-log mode, data can be inserted into, deleted from, and updated in an Apache Paimon table based on the primary key of the table. In change-log mode, you can also use the data merging mechanism and incremental data generation mechanism. |   |   |
| Append- only | In append-only mode, the Apache Paimon table allows only data insertion and does not support operations based on the primary key. The append-only mode is more efficient than the change-log mode. In append-only mode, an Apache Paimon table can be used as a substitute of Message Queue in scenarios where the data freshness requirement is not high. For example, data within hours is required. For more information about the append-only mode, see Configuration. When you use the append-only mode, take note of the following points: We recommend that you specify the bucket-key parameter based on your business requirements. Otherwise, data of the Apache Paimon table is distributed to buckets based on the values of all columns. This results in low computing efficiency. The append-only mode ensures the data generation order based on the following rules: i. If two data records come from different partitions, and the scan.plan-sort- partition parameter is specified, data that has the smaller partition value is preferentially generated. Otherwise, data from the partition that is created earlier is preferentially generated. ii. If two data records come from the same bucket in the same partition, the data that is written earlier is preferentially generated. iii. If two data records come from different buckets in the same partition, the data generation order cannot be ensured because data in different buckets is processed in different parallel subtasks. |   |   |
|   |   | scan.plan-sort- |   |
|   | partition |   |   |

**Data synchronization based on the CREATE TABLE AS and**

**CREATE DATABASE AS statements**

You can execute the CREATE TABLE AS or CREATE DATABASE AS statement to synchronize data from a single table or an entire database to an Apache Paimon table in real time. The changes to the schema of the source table can also be synchronized to the related Apache Paimon table in real time during data synchronization of a database or table.

### 5.28 MaxCompute connector

This topic describes how to use the MaxCompute connector.

**Background information**

MaxCompute is a fast and fully managed computing platform for large-scale data warehousing. MaxCompute can process exabytes of data. It provides solutions for storing and computing mass structured data in data warehouses and provides analytics and modeling services. The following table describes the capabilities supported by the MaxCompute connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | None |
| Monitoring metrics | Source table numRecordsIn: the total number of data records that are read by using the MaxCompute connector. numRecordsInPerSecond: the number of data records that are read by using the MaxCompute connector per second. numBytesIn: the total number of bytes of data that is read by using the MaxCompute connector after data is decompressed. numBytesInPerSecond: the number of bytes of data that is read by using the MaxCompute connector per second after data is decompressed. Sink table numRecordsOut: the total number of data records that are written by using the MaxCompute connector. numRecordsOutPerSecond: the number of data records that are written by using the MaxCompute connector per second. numBytesOut: the total number of bytes of data that is written by using the MaxCompute connector before data is compressed. numBytesOutPerSecond: the number of bytes of data that is written by using the MaxCompute connector per second before data is compressed. Dimension table dim.odps.cacheSize: the number of data records that are cached in a dimension table. |

| API types | DataStream API and SQL API |
|---|---|
| Data updates or deletion in a sink table | If MaxCompute Batch Tunnel or MaxCompute Streaming Tunnel is used, data can only be inserted into a sink table. If MaxCompute Upsert Tunnel is used, data in a sink table can be updated or deleted, and data can be inserted into a sink table. |

**Prerequisites**

A MaxCompute table is created.

**Limits**

The MaxCompute connector supports only the at-least-once semantics.

> **Note:** The at-least-once semantics is used to prevent data losses. In specific cases, duplicate data may be written to MaxCompute. MaxCompute provides different types of tunnels. Duplicate data may be generated based on the tunnel that you use.

By default, a source table that operates in full mode reads data only from the partition specified by the partition parameter. Once all data from the partition is read, the deployment finishes and does not monitor for new partitions. To continuously monitor for new partitions, create an incremental source by specifying the startPartition parameter in the WITH clause.

> **Note:** Each time a dimension table is updated, the dimension table checks for the latest partition.
> After the source table starts to run, it does not read the data that is newly added to a partition. We recommend that you run a deployment when the partition has complete data.

**Syntax**

```
CREATE TABLE odps_source(
  id INT,
  user_name VARCHAR,
  content VARCHAR
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'tunnelEndpoint' = '<yourTunnelEndpoint>',
  'project' = '<yourProjectName>',
  'schemaName' = '<yourSchemaName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=2018****'
```

);

**Parameters in the WITH clause**

Common parameters

| Parame ter | Descripti on | Data type | Req uire d | Default value | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | String | Yes | None | Set the value to odps. |
| endpoin t | The endpoint of MaxCompu te. | String | Yes | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| tunnelE ndpoint | The endpoint of MaxCompu te Tunnel. | String | No | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| project | The name of the MaxCompu te project. | String | Yes | None | None. |
| schema Name | The name of the MaxCompu te schema. | String | No | None | This parameter is required only when the MaxCompute schema feature is enabled. In this case, you must set this parameter to the name of the MaxCompute table's schema. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. |
| tableNa me | The name of the MaxCompu te table. | String | Yes | None | None. |
| accessId | The AccessKey ID that is used to access MaxCompu te. | String | Yes | None | None. |

| accessK ey | The AccessKey secret that is used to access MaxCompu te. | String | Yes | None | None. |
|---|---|---|---|---|---|
| partition | The name of the partition in the MaxCompu te table. | String | No | None | You do not need to specify this parameter for a non-partitioned MaxCompute table or an incremental source. |
| compres sAlgorit hm | The compressi on algorithm that is used by MaxCompu te Tunnel. | String | No | ZLIB (for VVR 4.0.13 and later) SNAPP Y (for VVR 6.0.1 and later) | Valid values: RAW (no compression) ZLIB SNAPPY Compared with ZLIB, SNAPPY can significantly improve the throughput. In test scenarios, the throughput is increased by about 50%. |
| quotaNa me | The name of the quota for the exclusive Tunnel resource groups of MaxCompu te. | String | No | None | You can specify this parameter to use the exclusive Tunnel resource groups of MaxCompute. Important Only Realtime Compute for Apache Flink that uses VVR 8.0.3 or later supports this parameter. If you specify this parameter, you must delete the tunnelEndpoint parameter. Otherwise, the tunnel that is specified by the tunnelEndpoint parameter is used. |

Source table-specific parameters

| Paramete r | Descri ption | Data type | Requi red | Defaul t value | Remarks |
|---|---|---|---|---|---|

| maxPartiti onCount | The maxim um numbe r of partitio ns from which data can be read. |   |   |   |   | If the number of partitions from which data is read exceeds the value of this parameter, this error message appears: "The number of matched partitions exceeds the default limit" . Important If data is read from a large number of partitions of a MaxCompute table, the workload on the MaxCompute service is high. In this case, the startup speed of the deployment slows down. To prevent this issue, you need to check whether data needs to be read from a large number of partitions and specify the partition parameter based on your business requirements. If your business requires data from a large number of partitions, manually increase the value of this parameter. |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   | exceeds the default limit" |
|   |   |   | Integer | No | 100 |   |

Incremental source table-specific parameters The incremental source table monitors new partitions by intermittently polling the MaxCompute server to obtain all partition information. Before the source table reads data from new partitions, data writing in the partitions must be complete. You can configure the startPartition parameter to specify the start partition from which data is read. Only data in the partitions whose **alphabetical order** is greater than or equal to the alphabetical order of the partition that is specified by the startPartition parameter is read. For example, the

| er of the partition | year=2023,month=10 |   |
|---|---|---|
|   |   | In this case, you c |

the month to the name of the partition that is declared in the code to ensure that the alphabetical order of the partition is valid. This way, you can change the value of the partition parameter from year=2023,month=9 to `year=2023,month=09` .

| Paramete r | Descripti on | Data type | Req uire d | Defa ult value | Remarks |
|---|---|---|---|---|---|
| startPartiti on | The start partition from which increment al data is read. | String | Yes | None | If you specify this parameter, the incremental source is used. As a result, the partition parameter is ignored. If the source table is a multi-level partitioned table, you must configure the value of each partition column in descending order based on partition levels. |

| subscribeI ntervalInS ec | The interval at which MaxComp ute is polled to obtain the informatio n about partitions. | Integer | No | 30 | Unit: seconds. |
|---|---|---|---|---|---|
| modifiedT ableOpera tion | The operation that is performed when data in a partition is modified during partition reading. | Enum (NONE, SKIP) | No | NONE | Download sessions are saved in checkpoints. Each time you resume a session from a checkpoint, Realtime Compute for Apache Flink attempts to resume the reading progress from the session. However, the session is unavailable because data in the partition is modified. In this case, the deployment is repeatedly restarted. To resolve this issue, you can specify this parameter. Valid values: NONE: If you set this parameter to NONE, you must change the value of the startPartition parameter to make the alphabetical order of the partition that is specified by the startPartition parameter greater than the alphabetical order of the unavailable partition and start the deployment without states. SKIP: If you do not want to start the deployment without states, you can set this parameter to SKIP. In this case, Realtime Compute for Apache Flink skips the unavailable partition when it attempts to resume the session from the checkpoint. Important If you set this parameter to NONE or SKIP, the data that is read from the partition in which data is modified is retained, and the data that is not read is ignored. |

Sink table-specific parameters

| Paramete r | Descrip tion | Data type | Req uire d | Defaul t value | Remarks |
|---|---|---|---|---|---|

| useStream Tunnel | Specifie s whether to use MaxCom pute Streami ng tunnel to upload data. | Boolean | No | false | Valid values: true: MaxCompute Streaming Tunnel is used to upload data. false: MaxCompute Batch Tunnel is used to upload data. |
|---|---|---|---|---|---|
| flushInterv alMs | The interval at which the flush operatio n is perform ed in the buffer of a writer in MaxCom pute Tunnel. | Long | No | 30000 (30 second s) | The MaxCompute sink inserts data into the buffer. Then, the MaxCompute sink writes the data in the buffer to the destination MaxCompute table at the interval that is specified by the flushIntervalMs parameter. The sink also writes the data to the destination table in MaxCompute when the size of the buffer data exceeds the specified threshold. If you use Streaming Tunnel, the data that is flushed to the destination MaxCompute table becomes available immediately. If you use Batch Tunnel, flushed data is not available until the checkpointing operation is complete. We recommend that you set this parameter to 0 to disable the scheduled flushing feature. Unit: milliseconds. Note This parameter can be used together with the batchSize parameter. The flush operation is triggered when the condition that is specified by the batchSize parameter or the flushIntervalMs parameter is met. |

| batchSize | The interval at which a flush operatio n is perform ed in the buffer of a writer in MaxCom pute Tunnel. | Long | No | 671088 64 (64 MB) | The MaxCompute sink inserts data into the buffer. Then, the MaxCompute sink writes the data in the buffer to the destination MaxCompute table when the size of the buffer data exceeds the value that is specified by the batchSize parameter. Unit: byte. Note This parameter can be used together with the flushIntervalMs parameter. The flush operation is triggered when the condition that is specified by the batchSize parameter or the flushIntervalMs parameter is met. |
|---|---|---|---|---|---|
| numFlushT hreads | The number of threads that are used to flush data in the buffer of a writer in MaxCom pute Tunnel. | Integer | No | 1 | Each MaxCompute sink creates the number of threads that is specified by the numFlushThreads parameter to flush data. If the value of this parameter is greater than 1, the data in different partitions can be flushed at the same time. This improves the flush operation efficiency. |
| dynamicPa rtitionLimit | The maximu m number of dynamic partition s to which data can be written. | Integer | No | 100 | If the number of dynamic partitions to which data is written from the sink between two checkpoints exceeds the value of the dynamicPartitionLimit parameter, this error message appears: "Too many dynamic partitions" . Important If data is written to a large number of partitions of a MaxCompute table, the workload on the MaxCompute service is high, slowing down checkpointing and flushing. To prevent this issue, you need to check whether data needs to be written to a large number of partitions. If your business requires data to be written to a large number of partitions, manually increase the value of the dynamicPartitionLimit parameter. |

| retryTimes | The maximu m number of retries that can be perform ed for a request on the MaxCom pute server. | Integer | No | 3 | The MaxCompute service may be unavailable for a short period of time when you create a session or submit a session, or data is flushed in the sink table. If the MaxCompute service becomes unavailable, the MaxCompute server is requested based on the configuration of this parameter. |   |   |
|---|---|---|---|---|---|---|---|
| sleepMillis | The retry interval. | Integer | No | 1000 | Unit: milliseconds. |   |   |
| enableUps ert | Specifie s whether to use MaxCom pute Upsert Tunnel to upload data. | Boolean | No | false | Valid values: true: MaxCompute Upsert Tunnel is used to process INSERT, UPDATE AFTER, and DELETE data in _ Realtime Compute for Apache Flink. false: MaxCompute Batch Tunnel or MaxCompute Streaming Tunnel that is specified by the useStreamTunnel parameter is used to process INSERT and UPDATE AFTER data in Realtime _ Compute for Apache Flink. Important If an issue, such as an error, a deployment failure, or a long-time processing fault, occurs when the MaxCompute sink commits a session in upsert mode, we recommend that you set the Parallelism parameter of sink operators to a value that is less than or equal to 10. Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this |   |   |
|   |   |   |   |   |   | Important If an issue, such as an error, a deployment failure, or a long-time processing fault, occurs when the MaxCompute sink commits a session in upsert mode, we recommend that you set the Parallelism parameter of sink operators to a value that is less than or equal to 10. Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this |   |
|   |   |   |   |   |   | parameter. |   |

| upsertAsy ncCommit | Specifie s whether to use the asynchr onous mode when a MaxCom pute sink commits a session in upsert mode. | Boolean | No | false | Valid values: true: The asynchronous mode is used. If you use the asynchronous mode, the time that is consumed to commit the session is reduced but the data that is written after the session is committed cannot be immediately queried. false: The synchronous mode is used by default. When the MaxCompute sink commits the session, the system waits until the server processes the session. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. |
|---|---|---|---|---|---|
| upsertCom mitTimeou tMs | The timeout period for which a MaxCom pute sink commits a session in upsert mode. | Integer | No | 120000 (120 second s) | Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. |

Dimension table-specific parameters When a deployment starts, the dimension table pulls full data from a partition that is specified by the partition parameter. This parameter supports the max_pt() function. If the cache is reloaded after the cache entries expire, data of the latest partition specified by the partition parameter is re-parsed. If the partition parameter is set to max_two_pt(), the dimension table can pull data from two partitions. If the partition parameter is not set to max_two_pt(), data of only one partition can be pulled.

| Param eter | Descript ion | Data type | Require d | Defa ult value | Remarks |
|---|---|---|---|---|---|

|   |   |   |   |   | or |
|---|---|---|---|---|---|
| cache | The cache policy. | String | Yes | None | You must set the cache parameter to ALL for a dimension table and explicitly declare the setting in the DDL statement. If the amount of data in a remote table is small and a large number of missing keys exist, we recommend that you set this parameter to ALL. The source and dimension table cannot be associated based on the ON clause. ALL: indicates that all data in the dimension table is cached. Before the system runs a deployment, the system loads all data in the dimension table to the cache. This way, the cache is searched for all subsequent queries in the dimension table. If no keys exist, the system cannot find the data record in the cache. The system reloads all data in the cache after cache entries expire. Note If the cache parameter is set to ALL, you must increase the memory of the join node because the system asynchronously loads data of the dimension table. We recommend that you increase the size of the memory at least four times the amount of data in the remote table. The size of the memory is related to the MaxCompute storage compression algorithm. If a dimension table contains a large amount of data, you can use the SHUFFLE HASH hint to _ evenly distribute the data of the dimension table to each subtask. If you use an ultra-large dimension table, frequent garbage collections (GCs) of Java virtual machine (JVM) may cause deployment exceptions. To resolve this issue, you can increase the memory of the node on which the dimension table is joined with another table. If the issue persists, we recommend that you convert the dimension table to a key- value dimension table that supports the least recently used (LRU) cache policy. For example, you can use an ApsaraDB for HBase dimension table as the key-value dimension table. |

|   |   |   |   |   |   |   | If the number of data records in the dimension table exceeds the value of the cacheSize parameter, this error message appears: "Row count of table <table- |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | "Row count of table <table- |
|   |   |   |   |   |   |   | name> partition <partition-name> |   |
|   |   |   |   |   |   |   | exceeds maxRowCount limit" |   |
|   | cacheS ize | The maximu m number of rows of data that can be cached. | Long |   | No | 1000 00 |   |   |
|   |   |   |   |   |   |   | data records need to be cached. If your business requires a large number of data records to be cached in a dimension table, manually increase the value of this parameter. |   |

| cacheT TLMs | The cache timeout period. | Long | No | Long. MAX _ VALU E (neve r refres h) | Unit: milliseconds. |
|---|---|---|---|---|---|
| cache Reload TimeBl ackList | The time periods during which cache is not refreshe d. The cache is not refreshe d during the time periods specified by this paramet er. | String | No | None | This parameter is applicable to large-scale online promotional events such as peak hours of activities. You can specify this parameter to prevent deployments from being unstable when the cache is refreshed. |

| maxLo adRetr ies | The maximu m number of retries that can be performe d to refresh the cache. The first time that data is pulled when the deploym ent is started, the cache is refreshe d. If the number of retries exceeds the value of this paramet er, the deploym ent fails to run. | Intege r | No | 10 | None. |
|---|---|---|---|---|---|

**Data type mappings**

| Data type of MaxCompute | Data type of Realtime Compute for Apache Flink |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INTEGER |
| BIGINT | BIGINT |
| FLOAT | FLOAT |

| DOUBLE | DOUBLE |
|---|---|
| DECIMAL(precision, scale) | DECIMAL(precision, scale) |
| CHAR(n) | CHAR(n) |
| VARCHAR(n) | VARCHAR(n) |
| STRING | STRING |
| BINARY | BYTES |
| DATE | DATE |
| DATETIME | TIMESTAMP(3) |
| TIMESTAMP | TIMESTAMP(9) |
| ARRAY | ARRAY |
| MAP | MAP |
| STRUCT | ROW |
| JSON | STRING |

> **Important:** If a MaxCompute physical table contains a field of a nested composite data type (ARRAY, MAP, or STRUCT, etc) and a field of JSON type, you must specify
> `tblproperties('columnar.nested.type'='true')` when you create the MaxCompute physical table to allow Realtime Compute for Apache Flink to read data from and write data to the physical table correctly.

**Sample code**

**SQL**

Sample code for a source table Read data from a full MaxCompute source table:

```
CREATE TEMPORARY TABLE odps_source (
  cid VARCHAR,
  rt DOUBLE
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpointName>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=201809*'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  cid VARCHAR,
  invoke_count BIGINT
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT
   cid,
   COUNT(*) AS invoke_count
FROM odps_source GROUP BY cid;
```

Read data from an incremental MaxCompute source table:

```
CREATE TEMPORARY TABLE odps_source (
  cid VARCHAR,
  rt DOUBLE
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpointName>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  startPartition'='yyyy=2018, MM=09,dd=05' -- Data is read from the partition 20180
905.
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  cid VARCHAR,
  invoke_count BIGINT
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT cid, COUNT(*) AS invoke_count FROM odps_source GROUP BY cid;
```

Sample code for a sink table Write data to static partitions:

```
CREATE TEMPORARY TABLE datagen_source (
  id INT,
  len INT,
  content VARCHAR
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE odps_sink (
  id INT,
  len INT,
  content VARCHAR
) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905' -- Data is written to the static partition 20180905.
```

);

```
INSERT INTO odps_sink SELECT
  id, len, content
FROM datagen_source;
```

Write data to dynamic partitions:

```
CREATE TEMPORARY TABLE datagen_source (
  id INT,
  len INT,
  content VARCHAR,
  c TIMESTAMP
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE odps_sink (
  id  INT,
  len INT,
  content VARCHAR,
  ds VARCHAR -- The partition key column that you use to create dynamic partitions
must be explicitly specified. ) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds' -- The partition value is not provided. This indicates that da
ta is written to a partition specified by the ds field.
```

);

```
INSERT INTO odps_sink SELECT
   id,
   len,
   content,
   DATE_FORMAT(c, 'yyMMdd') as ds
FROM datagen_source;
```

Sample code for a dimension table Join a dimension table and another table:

```
CREATE TEMPORARY TABLE datagen_source (
  k INT,
  v VARCHAR
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE odps_dim (
  k INT,
  v VARCHAR,
  PRIMARY KEY (k) NOT ENFORCED  -- You must declare a primary key when you join a d
imension table and another table. ) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905',
  'cache' = 'ALL'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  k VARCHAR,
  v1 VARCHAR,
  v2 VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT k, s.v, d.v FROM datagen_source AS s INNER JOIN odps_dim FOR SYSTEM_TIME AS OF PROCTIME() AS d ON s.k = d.k;
```

Join a dimension table and multiple tables:

```
CREATE TEMPORARY TABLE datagen_source (
  k INT,
  v VARCHAR
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE odps_dim (
  k INT,
  v VARCHAR
  -- You do not need to declare a primary key when you join a dimension table and m
ultiple tables. ) WITH (
  'connector' = 'odps',
  'endpoint' = '<yourEndpoint>',
  'project' = '<yourProjectName>',
  'tableName' = '<yourTableName>',
  'accessId' = '${secret_values.ak_id}',
  'accessKey' = '${secret_values.ak_secret}',
  'partition' = 'ds=20180905',
  'cache' = 'ALL'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  k VARCHAR,
  v1 VARCHAR,
  v2 VARCHAR
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT k, s.v, d.v FROM datagen_source AS s INNER JOIN odps_dim FOR SYSTEM_TIME AS OF PROCTIME() AS d ON s.k = d.k;
```

**DataStream**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink. The MaxCompute DataStream connectors of different versions are stored in the Maven central repository.
> To protect intellectual property, VVR 6.0.6 or later supports on-premises debugging of DataStream programs using the MaxCompute connector for up to 30 minutes. Any longer debugging session will result in the program being terminated with an error.

> If you submit a deployment in the development console of Realtime Compute for Apache Flink, an issue that MaxCompute-related classes cannot be found may occur. In this case, you must download the file with the uber.jar name extension from the Maven central repository, and add the file as an additional dependency of the deployment. For example, if the version of the ververica-connector-odps dependency of MaxCompute is 1.15-vvr-6.0.6, you can view the ververica- connector-odps-1.15-vvr-6.0.6-uber.jar package in the directory of the Maven repository and download the package to your on-premises directory.

The Maven dependencies of the MaxCompute connector contain the classes required to create the full source, incremental source, sink, and dimension tables.

```xml
<dependency>
    <groupId>com.alibaba.ververica</groupId>
    <artifactId>ververica-connector-odps</artifactId>
    <version>${connector.version}</version>
</dependency>
```

We recommend that you declare a MaxCompute table by using SQL statements when you use the MaxCompute DataStream connector. You can call Table API operations to access MaxCompute tables or call DataStream API operations to access data streams. Access a source table by using the DataStream connector

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); StreamTableEnvironment tEnv = StreamTableEnvironment.create(env); tEnv.executeSql(String.join(
    "\n",
    "CREATE TEMPORARY TABLE IF NOT EXISTS odps_source (",
    "  cid VARCHAR,",
    "  rt DOUBLE",
    ") WITH (",
    "  'connector' = 'odps',",
    "  'endpoint' = '<yourEndpointName>',",
    "  'project' = '<yourProjectName>',",
    "  'tableName' = '<yourTableName>',",
    "  'accessId' = '<yourAccessId>',",
    "  'accessKey' = '<yourAccessPassword>',",
    "  'partition' = 'ds=201809*'",
    ")");
DataStream<Row> source = tEnv.toDataStream(tEnv.from("odps_source")); source.print(); env.execute("odps source");
```

Access a sink table by using the DataStream connector

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); StreamTableEnvironment tEnv = StreamTableEnvironment.create(env); tEnv.executeSql(String.join(
    "\n",
    "CREATE TEMPORARY TABLE IF NOT EXISTS odps_sink (",
    "  cid VARCHAR,",
    "  rt DOUBLE",
    ") WITH (",
    "  'connector' = 'odps',",
    "  'endpoint' = '<yourEndpointName>',",
    "  'project' = '<yourProjectName>',",
    "  'tableName' = '<yourTableName>',",
    "  'accessId' = '<yourAccessId>',",
    "  'accessKey' = '<yourAccessPassword>',",
    "  'partition' = 'ds=20180905'",
    ")");
DataStream<Row> data = env.fromElements(
    Row.of("id0", 3.),
    Row.of("id1", 4.));
tEnv.fromDataStream(data).insertInto("odps_sink").execute();
```

### 5.29 Kafka connector

This topic describes how to use the Kafka connector.

**Background information**

Apache Kafka is an open source distributed message queue service. This service is widely used in big data scenarios, such as high-performance data processing, streaming analytics, and data integration. The Kafka connector supports high-performance data throughput, read and write operations on data in various formats, and exactly-once semantics for Realtime Compute for Apache Flink based on the Apache Kafka client.

| Item | Description |
|---|---|
| Table types | Source table and sink table |
| Running modes | Streaming mode |

| Data formats | CSV JSON Apache Avro Confluent Avro Debezium JSON Canal JSON Maxwell JSON Raw Note You can configure the parameter that is related to each data format in the WITH clause. For more information, see Formats. |
|---|---|
| Monitoring metrics | Metrics for source tables: numRecordsIn numRecordsInPerSecond numBytesIn numBytesInPerScond currentEmitEventTimeLag currentFetchEventTimeLag sourceIdleTime pendingRecords Metrics for sink tables: numRecordsOut numRecordsOutPerSecond numBytesOut numBytesOutPerSecond currentSendTime |
| API types | SQL API and DataStream API |
| Data update or deletion in a sink table | Data in a sink table cannot be updated or deleted. Data can only be inserted into a sink table. Note For more information about how to update or delete data in a sink table, see Upsert Kafka connector. |

**Prerequisites**

The prerequisites vary based on the type of the Kafka cluster to which Realtime Compute for Apache Flink needs to connect. ApsaraMQ for Kafka cluster An ApsaraMQ for Kafka cluster is created. The ApsaraMQ for Kafka cluster resides in the same virtual private cloud (VPC) as Realtime Compute for Apache Flink. The CIDR blocks of Realtime Compute for Apache Flink are added to the whitelist of the ApsaraMQ for Kafka cluster.

> **Important:** Take note of the following items for writing data into ApsaraMQ for Kafka:
> ApsaraMQ for Kafka does not support the data compression algorithm Zstandard for data writing.
> ApsaraMQ for Kafka does not support idempotent or transactional write operations. Therefore, you cannot use the exactly-once semantics supported by Kafka sink tables. If your Realtime Compute for Apache Flink uses **Ververica** **Runtime (VVR) 8.0.0** or later, you must disable the idempotent write feature by configuring `properties.enable.idempotence=false` for the **sink table**.

Self-managed Apache Kafka cluster The version of the self-managed Apache Kafka cluster is 0.11 or later. A network connection is established between Realtime Compute for Apache Flink and the self-managed Apache Kafka cluster. Only the client parameters of Apache Kafka 2.8 are supported. For more information about the configuration parameters of Kafka producers and consumers, see Consumer Configs and Producer Configs.

**Limits**

**Limits on VVR and Kafka cluster versions**

| Kafka cluster version | VVR version |
|---|---|
| 1.x | 6.x |
| 2.x and 3.x | 6.x and 8.x |

**Limits on the CREATE TABLE AS statement**

The CREATE TABLE AS statement can infer column data types only from a JSON source and synchronize schema changes of such a table. The CREATE TABLE AS statement can infer the data types only for value fields from a Kafka source and synchronize schema changes to those fields. To synchronize data of key fields from a Kafka source, you must specify them in the DDL statement.

**Troubleshoot network connectivity**

If the error message `Timed out waiting for a node assignment` appears when you start a deployment, it indicates a network connectivity problem between your Realtime Compute for Apache Flink workspace and the Kafka cluster. The process for establishing a connection between a Kafka client and a Kafka broker consists of the following steps:
1. The client initiates a connection with a broker by using the IP address and port number
specified by the properties.bootstrap.servers parameter. Then, the client returns the metadata of each broker, including the endpoint, based on the configuration.
2. The client uses the endpoint obtained in Step 1 to connect to a broker to produce or
consume data. If the broker is misconfigured, the client will receive an incorrect endpoint. In this case, even if the initial connection can be correctly established by using the IP address and port number specified in the **properties.bootstrap.servers** parameter, data cannot be read from or written to Kafka. In most cases, this issue occurs if a forwarding mechanism, such as a proxy, a port forwarding, or a leased line, is used to establish the connection between Realtime Compute for Apache Flink and Kafka. You can perform the following steps to check whether the configuration of your Kafka cluster is valid:
1. Use the ZooKeeper command line tool, zkCli.sh or zookeeper-shell.sh, to log in to the
ZooKeeper service that is used by your Kafka cluster.
2. Run a command based on the information about your Kafka cluster to obtain the metadata
of your Kafka broker. In most cases, you can run the `get /brokers/ids/0` command to obtain the metadata of Kafka brokers. The endpoints of Kafka brokers are specified in the endpoints field and are obtained by the Kafka client when the Kafka client connects to the Kafka brokers. The following figure shows the endpoints of Kafka brokers.
3. Run commands such as ping or telnet to test the connectivity to the returned endpoint. If
the endpoint is inaccessible, contact the O&M engineers of Kafka to configure the listeners and advertised.listeners properties of the Kafka broker for Realtime Compute for Apache Flink. For more information about how the Kafka client is connected to a Kafka broker, see Troubleshoot Connectivity.

**Syntax**

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL
) WITH (
  'connector' = 'kafka',
  'topic' = 'user_behavior',
  'properties.bootstrap.servers' = 'localhost:9092',
  'properties.group.id' = 'testGroup',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'csv'
```

`)`

**Metadata columns**

You can define metadata columns in a Kafka source table or a Kafka sink table to obtain the metadata of Kafka messages. For example, if multiple topics are defined in the WITH clause for a Kafka source table and a metadata column is defined in the source table, the topic from which Flink reads data is marked. The following sample code provides an example on how to use metadata columns:

```
CREATE TABLE kafka_source (
  -- Read the topic to which the message belongs as the value of the record_topic field
```

`.`

```
  `record_topic` STRING NOT NULL METADATA FROM 'topic' VIRTUAL,
  -- Read the timestamp in ConsumerRecord as the value of the ts field.
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL,
  -- Read the offset of the message as the value of the record_offset field.
  `record_offset` BIGINT NOT NULL METADATA FROM 'offset' VIRTUAL,
  ...
) WITH (
  'connector' = 'kafka',
  ...
```

);

```
CREATE TABLE kafka_sink (
  -- Write the timestamp in the ts field as the timestamp of ProducerRecord to Kafka.
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp' VIRTUAL,
  ...
) WITH (
  'connector' = 'kafka',
  ...
```

); The following table describes the metadata columns supported by Kafka source tables and sink tables.

| Key | Data type | Description | Source table or sink table |
|---|---|---|---|
| topic | STRING NOT NULL METADATA VIRTUAL | The name of the topic to which the Kafka message belongs. | Source table |
| partition | INT NOT NULL METADATA VIRTUAL | The ID of the partition to which the Kafka message belongs. | Source table |
| headers | MAP<STRING, BYTES> NOT NULL METADATA VIRTUAL | Headers of the Kafka message. | Source table and sink table |
| leader-epoch | INT NOT NULL METADATA VIRTUAL | The leader epoch of the Kafka message. | Source table |

| offset | BIGINT NOT NULL METADATA VIRTUAL | The offset of the Kafka message. | Source table |
|---|---|---|---|
| timestamp | TIMESTAMP(3) WITH LOCAL TIME ZONE NOT NULL METADATA VIRTUAL | The timestamp of the Kafka message. | Source table and sink table |
| timestamp- type | STRING NOT NULL METADATA VIRTUAL | The timestamp type of the Kafka message. Valid values: NoTimestampType: indicates that no timestamp is defined in the message. CreateTime: indicates the time when the message was generated. LogAppendTime: indicates the time when the message was added to Kafka brokers. | Source table |

**Parameters in the WITH clause**

Common parameters

| Parameter | Description | Data type | Requi red | Def ault valu e | Remarks |
|---|---|---|---|---|---|
| connector | The type of tables. | String | Yes | Non e | Set the value to kafka. |
| properties.b ootstrap.ser vers | The IP address and port number of a Kafka broker. | String | Yes | Non e | Format: host:port,host:port,host:port. Separate multiple host:port pairs with commas (,). |

| properties.* | The parameters that are configured for the Kafka client. |   |   |   |   | The suffix of this parameter must comply with the rules that are defined in Producer Configs and Consumer Configs. Realtime Compute for Apache Flink removes the "properties." prefix and passes the transformed key and values to the Kafka client. For example, you can configure properties.allow.auto.create.to pics=false to disable automatic topic creation. You cannot add the "properties." prefix to modify the configurations of the following parameters because the values of the parameters are overwritten after you use the Kafka connector: key.deserializer value.deserializer |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | properties.allow.auto.create.to |   |
|   |   | red | String | No | Non e | pics=false |   |   |
| format | The format used to read or write the value field of Kafka messages. |   | String | No | Non e | Valid values: csv json avro debezium-json canal-json maxwell-json avro-confluent raw Note For more information, see Format Options in Apache Flink documentation. |   |   |

| key.format | The format of the Kafka message key. | String | No | Non e | Valid values: csv json avro debezium-json canal-json maxwell-json avro-confluent raw Note If you configure this parameter, you must configure the key.options parameter. |   |   |
|---|---|---|---|---|---|---|---|
| key.fields | The key fields in the source table or sink table that corresponds to the key fields of Kafka messages. | String | No | Non e | Separate multiple field names with semicolons (;), such as field 1;field2 . |   |   |
|   |   |   |   |   |   | field |   |
| key.fields- prefix | The custom prefix for all key fields in Kafka messages. You can configure this parameter to prevent name conflicts with the value fields. | String | No | Non e | This parameter is used only to distinguish the column names of source tables and sink tables. The prefix is removed from the column names when the key fields of Kafka messages are parsed or generated. Note If you configure this parameter, you must set the value.fields- include parameter to EXCEPT KEY. _ |   |   |
| value.format | The format of the Kafka message value. | String | No | Non e | The configuration of this parameter is equivalent to the configuration of the format parameter. The format parameter cannot be used together with the value.format parameter. If you configure both parameters, a conflict occurs. |   |   |

| Non | 1;field2 |
|---|---|

| value.fields- include | Specifies whether to include correspondi ng message keys when parsing or generating Kafka message values. | String | No | ALL | Valid values: ALL: All fields are processed as value fields of Kafka messages. This is the default value. EXCEPT KEY: All fields except for _ the fields specified by the key.fields parameter are processed as value fields of Kafka messages. |
|---|---|---|---|---|---|

Source table-specific parameters

| Parameter | Descriptio n | Data type | Requir ed | Defau lt value | Remarks |
|---|---|---|---|---|---|
| topic | The name of the topic from which you want to read data. | String | No | None | Separate multiple topic names with semicolons (;), such as topic-1;topic- 2. Note The topic parameter cannot be used together with the topic- pattern parameter. |
| topic- pattern | The regular expression that is used to match topics. Data of all topics whose names match the specified regular expression is read when a deployment is running. | String | No | None | The topic parameter cannot be used together with the topic-pattern parameter. |
| properties.g roup.id | The consumer group ID. | String | No | KafkaS ource- {Nam e of the source table} | If the specified group ID is used for the first time, you must set the properties.auto.offset.reset parameter to "earliest" or "latest" to specify the initial start offset. |

| scan.startup .mode | The start offset for Kafka to read data. |   | String | No | group- offsets | Valid values: earliest-offset: Kafka reads data from the earliest offset. latest-offset: Kafka reads data from the latest offset. group-offsets: reads data from the offset that is committed by the consumer group with the ID that is specified by the properties.group.id parameter. This is the default value. timestamp: reads data from the timestamp that is specified by the scan.startup.timestamp-millis parameter. specific-offsets: reads data from the offset that is specified by the scan.startup.specific-offsets parameter. Note This parameter takes effect when the deployment is started without states. When the deployment is restarted from a checkpoint or resumes from the specified state, the deployment preferentially starts to read data at the progress that is saved in the state data. |   |
|---|---|---|---|---|---|---|---|
| scan.startup .specific- offsets | The start offset of each partition when the scan.startu p.mode parameter is set to specific- offsets. |   | String | No | None | Example: partition:0,offset:42;partitio n:1,offset:300 . |   |
|   |   |   |   |   |   |   | partition:0,offset:42;partitio |
|   |   |   |   |   |   | n:1,offset:300 |   |
| scan.startup .timestamp- millis | The timestamp of the start offset when the scan.startu p.mode parameter is set to timestamp. |   | Long | No | None | Unit: milliseconds. |   |

| scan.topic- partition- discovery.in terval | The time interval for dynamically detecting Kafka topics and partitions. | Durati on | No | 5 minute s | The default partition discovery interval is 5 minutes. To disable the dynamic partition discovery feature, you must explicitly set this parameter to a non-positive value. After the dynamic partition discovery feature is enabled, the Kafka source can automatically discover new partitions and read data from the partitions. In topic- pattern mode, the Kafka source reads data from new partitions of existing topics and data from all partitions of new topics that match the regular expression. Note For Realtime Compute for Apache Flink that uses VVR 6.0.X, the dynamic partition discovery feature is disabled by default. For Realtime Compute for Apache Flink that uses VVR 8.0 or later, this feature is enabled by default. The default partition discovery interval is 5 minutes. |
|---|---|---|---|---|---|

| scan.header -filter | Kafka data filtering based on whether the data contains a specific message header. |   |   |   |   | Separate a header key and the value with a colon (:). Separate multiple headers with logical operators such as AND (&) or OR (\|). The logical operator NOT (!) is supported. For example, depart:toy\|depart:book&!env:te st indicates that the Kafka data whose header contains depart=toy or depart=book and does not contain env=test is retained. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. Parenthesis operations are not supported. Logical operations are performed from left to right in sequence. The header value in the UTF-8 format is converted into a string and compared with the header value specified by the scan.header-filter parameter. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | depart:toy\|depart:book&!env:te |   |
|   |   |   |   |   |   | st |   |   |
|   |   |   | String | No | None |   |   |   |

|   | scan.check. duplicated.g roup.id |   | Specifies whether to check duplicate consumer groups specified by the properti |   | Boole an | No | false | Valid values: true: Duplicate consumer groups are checked before a deployment starts. If duplicate consumer groups exist, an error is reported to prevent conflicts with existing consumer groups. false: Duplicate consumer groups are not checked before a deployment starts. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.4 or later supports this parameter. |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   | properti |   |   |   |   |
|   |   |   | es.group.i |   |   |   |   |   |
|   |   |   | d |   |   |   |   |   |

Sink table-specific parameters

| Parameter | Description | Data type | Requi red | Defa ult value | Remarks |
|---|---|---|---|---|---|
| topic | The name of the topic to which data is written. | String | Yes | None | None |
| sink.partitio ner | The mapping pattern between Realtime Compute for Apache Flink partitions and Kafka partitions. | String | No | defau lt | Valid values: default: The default Kafka partitioner is used to partition data. fixed: Each Flink partition corresponds to a fixed Kafka partition. round-robin: Data in a Flink partition is distributed to the Kafka partitions in round-robin sequence. Custom partition mapping pattern: You can create a subclass of FlinkKafkaPartitioner to configure a custom partition mapping pattern, such as org.mycompany.MyPartitioner. |

| sink.deliver y-guarantee | The delivery semantics for the Kafka sink table. | String | No | at- least- once | Valid values: none: The delivery semantics are not ensured. Data may be lost or duplicated. at-least-once: It ensures that no data is lost. However, duplicate data may exist. exactly-once: Kafka transactions are used to ensure the exactly- once semantics. This ensures that data is not lost or duplicated. Note You must configure the sink.transactional-id-prefix parameter if you set this parameter to exactly-once. |
|---|---|---|---|---|---|
| sink.transac tional-id- prefix | The prefix of the Kafka transaction ID that is used in the exactly-once semantics. | String | No | None | This parameter takes effect only when the sink.delivery-guarantee parameter is set to exactly-once. |
| sink.paralleli sm | The parallelism of operators for the Kafka sink table. | Integ er | No | None | The parallelism of upstream operators, which is determined by the framework. |

Parameters for data synchronization by using the CREATE TABLE AS statement

| Parameter | Descript ion | Data type | Requi red | Defaul t value | Remarks |
|---|---|---|---|---|---|

| json.infer- schema.flat ten-nested- columns.en able | Specifies whether to recursive ly expand nested columns in a JSON text. | Boolean | No | false |   | Valid values: true: Nested columns are recursively expanded. Realtime Compute for Apache Flink uses the path that indexes the value of the column that is expanded as the name of the column. For example, in the JSON {"nested": {"col": true}} , the column col becomes nested.col after expansion. false: Nested types are parsed as the STRING type. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | {"nested": |   |
|   |   |   |   |   | false | {"col": true}} |   |   |
| json.infer- schema.pri mitive-as- string | Specifies whether to infer all basic types as the STRING type. | Boolean | No | false |   | Valid values: true: All basic data types are inferred as the STRING type. false: Data types are inferred based on basic rules. |   |   |

You can add the `properties.` prefix to the names of all parameters that are supported by Kafka consumers and producers and configure the parameters in the WITH clause. For example, if you want to set the **request.timeout.ms** parameter of Kafka consumers or producers to 60000 (measured in milliseconds), you can configure `'properties.request.timeout.ms'='60000'` in the WITH clause. For more information about the parameters supported by Kafka consumers and producers, see Apache Kafka official documentation.

**Security and authentication**

If your Kafka cluster requires secure connection or authentication, add the `properties.` prefix to the names of the parameters related to security and authentication and configure the parameters in the WITH clause. The following sample code provides an example on how to configure a Kafka table to use PLAIN as the Simple Authentication and Security Layer (SASL) mechanism and provide Java Authentication and Authorization Service (JAAS) configurations.

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN',
  'properties.sasl.jaas.config' =
'org.apache.flink.kafka.shaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="username" password="password";'
```

`)` The following sample code provides an example on how to configure a Kafka table to use SASL_SSL as the security protocol and SCRAM-SHA-256 as the SASL mechanism.

```
CREATE TABLE KafkaTable (
  `user_id` BIGINT,
  `item_id` BIGINT,
  `behavior` STRING,
  `ts` TIMESTAMP_LTZ(3) METADATA FROM 'timestamp'
) WITH (
  'connector' = 'kafka',
  ...
  'properties.security.protocol' = 'SASL_SSL',
  /*Configure SSL.*/
  /*Specify the path of the CA certificate truststore provided by the server.*/
  'properties.ssl.truststore.location' = '/flink/usrlib/kafka.client.truststore.jks',
  'properties.ssl.truststore.password' = 'test1234',
  /*Specify the path of the private key file keystore if client authentication is requi
red.*/
  'properties.ssl.keystore.location' = '/flink/usrlib/kafka.client.keystore.jks',
  'properties.ssl.keystore.password' = 'test1234',
  /*The algorithm used by the client to verify the server address. A null value indicat
es that server address verification is disabled.*/
  'properties.ssl.endpoint.identification.algorithm' = '',
  /*Configure SASL.*/
  /*Configure SCRAM-SHA-256 as the SASL mechanism.*/
  'properties.sasl.mechanism' = 'SCRAM-SHA-256',
  /*Configure JAAS.*/
  'properties.sasl.jaas.config' =
'org.apache.flink.kafka.shaded.org.apache.kafka.common.security.scram.ScramLoginModule required username="username" password="password";'
```

`)` You can click Upload Artifact on the Artifacts page in the development console of Realtime Compute for Apache Flink to upload the CA certificate file and private key file. The uploaded files are stored in the /flink/usrlib directory. For example, if the name of the CA certificate file that you want to use is my-truststore.jks, you can configure

```
 'properties.ssl.truststore.location' = '/flink/usrlib/my-truststore.jks'  in the WITH
```

clause to use the certificate after you upload the certificate file.

> **Note:** The preceding code snippets provide examples of the configurations that are used in most cases. Before you configure the Kafka connector, contact Kafka server O&M personnel to obtain the correct security and authentication configuration information.
> Unlike Apache Flink, the SQL editor of Realtime Compute for Apache Flink escapes double quotation marks (") by default. Therefore, you do not need to add backslashes (\) as escape characters to the double quotation marks (") that are used to enclose the username and password when you configure the
> `properties.sasl.jaas.config` parameter.

**Start offset for a Kafka source table**

**Startup mode**

You can configure the **scan.startup.mode** parameter to specify the data reading startup mode for a Kafka source table. earliest-offset: reads data from the earliest offset of the current partition. latest-offset: reads data from the latest offset of the current partition. group-offsets: reads data from the offset that is committed by the consumer group that has the ID specified by the **properties.group.id** parameter. timestamp: reads data from the first message whose timestamp is greater than or equal to the timestamp that is specified by the **scan.startup.timestamp-millis** parameter. specific-offsets: reads data from the partition offset that is specified by the
**scan.startup.specific-offsets** parameter.

> **Note:** If you do not specify the start offset, the Kafka source table starts to read data from the offset that is committed by the consumer group that has the specified ID.
> The **scan.startup.mode** parameter takes effect only on the deployments that are started without states. If a deployment that uses the required states is started, data is read from the offset that is stored in a state backend.

Sample code:

```
CREATE TEMPORARY TABLE kafka_source (
  ...
) WITH (
  'connector' = 'kafka',
  ...
  -- Consume data from the earliest offset.
  'scan.startup.mode' = 'earliest-offset',
  -- Consume data from the latest offset.
  'scan.startup.mode' = 'latest-offset',
  -- Consume data from the offset that is committed by the consumer group my-group.
  'properties.group.id' = 'my-group',
  'scan.startup.mode' = 'group-offsets',
  'properties.auto.offset.reset' = 'earliest', -- If my-group is used for the first tim
e, the consumption starts from the earliest offset.
  'properties.auto.offset.reset' = 'latest', -- If my-group is used for the first time,
the consumption starts from the latest offset
  -- Consume data from the timestamp 1655395200000, in milliseconds.
  'scan.startup.mode' = 'timestamp',
  'scan.startup.timestamp-millis' = '1655395200000',
  -- Consume data from the specified offset.
  'scan.startup.mode' = 'specific-offsets',
  'scan.startup.specific-offsets' = 'partition:0,offset:42;partition:1,offset:300'
```

);

**Priority of start offsets**

The source table consumes data based on the following priorities of start offsets in descending order:
1. The offset that is stored in checkpoints or savepoints.
2. The start time that you specified in the Realtime Compute for Apache Flink console.
3. The start offset that is specified by the **scan.startup.mode** parameter in the WITH clause.
4. **group-offsets** is used if the **scan.startup.mode** parameter is not configured.
If one of the preceding offsets becomes invalid due to expiration or an issue in the Kafka cluster, the reset strategy that is specified by the **properties.auto.offset.reset** parameter is used to reset the offset. If you do not configure this parameter, an exception occurs. In most cases, the Kafka source table starts to read data from the offset that is committed by a consumer group that has a new group ID. When the Kafka source table queries the offset that is committed by the consumer group in the Kafka cluster, no valid offset is returned because the group ID is used for the first time. In this case, the reset strategy that is specified by the **properties.auto.offset.reset** parameter is used to reset the offset. Therefore, you must configure the **properties.auto.offset.reset** parameter in the scenario when the Kafka source table starts to read data from the offset that is committed by a consumer group that has a new group ID.

**Consumer offsets**

The Kafka source table commits a consumer offset to the Kafka cluster only after the checkpointing operation is successful. If the checkpoint interval that you specify is excessively large, the consumer offset is committed with a delay to the Kafka cluster. During the checkpointing operation, the Kafka source table stores the current data reading progress in the state backend. The offset that is committed to the Kafka cluster is not used for fault recovery. The committed offset is used to only monitor the data reading progress in Kafka. Data accuracy is not affected even if the offset fails to be committed.

**Custom partitioner for a sink table**

If the built-in Kafka producer cannot meet your business requirements, you can use a custom Kafka partitioner to write data to the related partitions. A custom partitioner needs to inherit FlinkKafkaPartitioner. After you configure a custom partitioner, compile the JAR package for the partitioner and click Upload Artifact on the Artifacts page in the development console of Realtime Compute for Apache Flink to upload the package. After the package is uploaded and referenced, you need to configure the **sink.partitioner** parameter in the WITH clause. The value of this parameter must be a complete classpath of the partitioner, such as

```
 org.mycompany.MyPartitioner .
```

**Selection of Kafka, Upsert Kafka, and a Kafka JSON catalog**

Kafka is a message queue system that allows for only data addition and does not support data updates or deletions. Therefore, Kafka cannot process Change Data Capture (CDC) data of upstream systems and the retraction logic of operators such as aggregate and join during streaming SQL computing. If you want to write data that contains change data or retraction data to Kafka, use an Upsert Kafka sink table that can perform special processing on change data. If you want to synchronize change data from one or more data tables in an upstream database to Kafka in batches, you can use a Kafka JSON catalog. If data that is stored in Kafka is in the JSON format, you can use a Kafka JSON catalog. This way, you do not need to configure the schema and parameters in the WITH clause.

**Data source for data synchronization by using the CREATE**

**TABLE AS statement**

The CREATE TABLE AS statement can perform data synchronization from a Kafka source table in the JSON format. If specific fields do not exist in a predefined table schema during data synchronization, Flink attempts to automatically infer the data types of the columns. If the inferred data types do not meet your business requirements, you can perform auxiliary type inference to declare the data types of the columns.

> **Note:** For more information about the JSON format, see JSON Format.

Type inference By default, Realtime Compute for Apache Flink displays only the first layer of data in the JSON text during type inference. Realtime Compute for Apache Flink infers the SQL data types based on the JSON data types, values, and the data type mappings. The following table lists the mappings between JSON data types and Flink SQL data types.

| JSON data type | Flink SQL data type |
|---|---|
| BOOLEAN | BOOLEAN |
| STRING | DATE, TIMESTAMP, TIMESTAMP LTZ, TIME, or STRING _ |
| INT or LONG | BIGINT |

| BIGINT | DECIMAL or STRING Note The precision of the DECIMAL type in Realtime Compute for Apache Flink is limited. If an integer exceeds the maximum allowed digits for DECIMAL, Realtime Compute for Apache Flink casts it to STRING to avoid precision loss. |
|---|---|
| FLOAT, DOUBLE, or BIG DECIMAL | DOUBLE |
| ARRAY | STRING |
| OBJECT | STRING |

Example JSON text `{`

```json
  "id": 101,
  "name": "VVP",
  "properties": {
    "owner": "Alibaba Cloud",
    "engine": "Flink"
```

`}`

```json
    "type": ["Big data"]
```

`}` Information about the table to which Realtime Compute for Apache Flink writes data

| id | name | properties | type |
|---|---|---|---|
| 101 | VVP | { "owner": "Alibaba Cloud", "engine": "Flink" } | ["Big data"] |

Auxiliary type inference If type inference based on the preceding rules does not meet your needs, you can explicitly declare the data type of a specific column in the DDL statement of the source table. Realtime Compute for Apache Flink prioritizes the declared type during parsing. In this example, Realtime Compute for Apache Flink parses the price field as DECIMAL instead of converting it to DOUBLE based on the data type mappings.

```
CREATE TABLE evolvingKafkaSource (
  price DECIMAL(18, 2)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = 'localhost:9092',
  'topic' = 'evolving_kafka_demo',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'json'
```

); However, if the data type that you specify in the DDL statement is different from the actual data type, you can use one of the following methods to handle the issue: If a column's declared data type has a wider range than the actual data type, the field is parsed according to the declared data type. For example, if a column declared as the DOUBLE type is used to hold BIGINT data, the data type of the column is parsed as DOUBLE. If the actual data type has a wider range than or is incompatible with the declared data type, an error is returned because CREATE TABLE AS does not support type changes. To resolve this, you must restart your deployment and declare a correct data type. The following figure shows the ranges of data types and the compatibility between the data types.

> **Note:** In the preceding figure, data types closer to the root node have wider ranges. Data types on different branches are incompatible.
> Auxiliary type inference is not supported for complex data types, such as ROW, ARRAY, MAP, and MULTISET.
> By default, Realtime Compute for Apache Flink parses complex data types as STRING.

In most cases, the JSON text in Kafka topics has a nested structure. If you want to extract nested columns from JSON texts, you can use one of the following methods: Declare `'json.infer-schema.flatten-nested-columns.enable'='true'` in the source table's DDL statement. This way, all nested columns are expanded to the top level in sequence. To prevent column name conflicts, Realtime Compute for Apache Flink uses path-based approach to name expanded columns.

> **Important:** Column name conflicts cannot be directly resolved. However, you can walk around this by setting 'json.ignore-parse-errors' to 'true' in the source table's DDL statement to ignore conflicts.

Add `rowkey` AS JSON_VALUE(`properties`, `$.rowkey`) to the CREATE TABLE AS syntax in the DDL statement to add a computed column and specify the column that you want to expand.

**Examples**

**Example 1: Read data from a Kafka topic and write the data**

**into another Kafka topic**

The following code sample reads data from the source Kafka topic and then writes the data into the sink Kafka topic. The data is in the CSV format.

```
CREATE TEMPORARY TABLE kafka_source (
  id INT,
  name STRING,
  age INT
) WITH (
  'connector' = 'kafka',
  'topic' = 'source',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'properties.group.id' = '<yourKafkaConsumerGroupId>',
  'format' = 'csv'
```

);

```
CREATE TEMPORARY TABLE kafka_sink (
  id INT,
  name STRING,
  age INT
) WITH (
  'connector' = 'kafka',
  'topic' = 'sink',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'properties.group.id' = '<yourKafkaConsumerGroupId>',
  'format' = 'csv'
```

);

```
INSERT INTO kafka_sink SELECT id, name, age FROM kafka_source;
```

**Example 2: Synchronize table schema and data**

Use the Kafka connector to synchronize messages from a Kafka topic to Hologres in real time. By configuring the offset and partition ID of Kafka messages as primary keys, you can prevent duplicate messages in Hologres in case of a failover.

```
CREATE TEMPORARY TABLE kafkaTable (
  `offset` INT NOT NULL METADATA,
  `part` BIGINT NOT NULL METADATA FROM 'partition',
  PRIMARY KEY (`part`, `offset`) NOT ENFORCED
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'format' = 'json',
  'json.infer-schema.flatten-nested-columns.enable' = 'true'
    -- Optional. Expand all nested columns.
```

);

```
CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka` WITH (
  'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable;
```

**Example 3: Synchronize the table schema and data in the key**

**and value columns of Kafka messages**

The key fields of Kafka messages store relevant information. You can synchronize data in the key and value columns of Kafka messages at the same time.

```
CREATE TEMPORARY TABLE kafkaTable (
  `key_id` INT NOT NULL,
  `val_name` VARCHAR(200)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'key.format' = 'json',
  'value.format' = 'json',
  'key.fields' = 'key_id',
  'key.fields-prefix' = 'key_',
  'value.fields-prefix' = 'val_',
  'value.fields-include' = 'EXCEPT_KEY'
```

);

```
CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka`( WITH (
  'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable;
```

> **Note:** The key columns in a Kafka message do not support table schema changes and type inference. Manual declaration is required.

**Example 4: Synchronize table schema and data and perform**

**computation**

When you synchronize data from Kafka to Hologres, lightweight calculation is required.

```
CREATE TEMPORARY TABLE kafkaTable (
  `distinct_id` INT NOT NULL,
  `properties` STRING,
  `timestamp` TIMESTAMP_LTZ METADATA,
  `date` AS CAST(`timestamp` AS DATE)
) WITH (
  'connector' = 'kafka',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'topic' = 'kafka_evolution_demo',
  'scan.startup.mode' = 'earliest-offset',
  'key.format' = 'json',
  'value.format' = 'json',
  'key.fields' = 'key_id',
  'key.fields-prefix' = 'key_'
```

);

```
CREATE TABLE IF NOT EXISTS hologres.kafka.`sync_kafka` WITH (
   'connector' = 'hologres'
) AS TABLE vvp.`default`.kafkaTable ADD COLUMN
  `order_id` AS COALESCE(JSON_VALUE(`properties`, '$.order_id'), 'default');
-- Use COALESCE to handle null values.
```

**Datastream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink. The Kafka DataStream connectors of different versions are stored in the Maven central repository.

Create a Kafka source You can use the KafkaSource class to create a Kafka source. The following sample code shows how to create a Kafka source to consume messages from the earliest offset of the "input-topic" topic. The consumer group is my-group. The value of each message is deserialized as a string.

```
KafkaSource<String> source = KafkaSource.<String>builder()
    .setBootstrapServers(brokers)
    .setTopics("input-topic")
    .setGroupId("my-group")
    .setStartingOffsets(OffsetsInitializer.earliest())
    .setValueOnlyDeserializer(new SimpleStringSchema())
    .build();
env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source");
```

The following table describes the parameters that you must configure when you create a Kafka source.

| Parameter | Description |
|---|---|
| BootstrapServers | The addresses of Kafka brokers. You can call the setBootstrapServers(String) operation to configure the addresses. |
| GroupId | The ID of the consumer group. You can call the setGroupId(String) method to configure the ID. |
| Topics or Partition | The topics or names of the partitions to which you subscribe. You can configure a Kafka source to subscribe to topics or partitions by using one of the following subscription patterns: Topic list. After you configure a topic list, the Kafka source subscribes to all partitions of the specified topics. KafkaSource.builder().setTopics("topic-a","topic-b") Topic pattern. After you specify a regular expression, the Kafka source subscribes to all partitions of the topics that match the specified regular expression. KafkaSource.builder().setTopicPattern("topic.*") Partition list. After you configure a partition list, the Kafka source subscribes to the specified partitions. final HashSet<TopicPartition> partitionSet = new HashSet<>(Arrays.asList( new TopicPartition("topic-a", 0), // Partition 0 of topic "topic-a" new TopicPartition("topic-b", 5))); // Partition 5 of topic "topic-b" KafkaSource.builder().setPartitions(partitionSet) |

| Deserializer | A deserializer that deserializes Kafka messages. You can call the setDeserializer(KafkaRecordDeserializationSchema) method to specify a deserializer. The KafkaRecordDeserializationSchema interface defines how a ConsumerRecord object is deserialized. You can use one of the following methods to deserialize only the Value fields in the Kafka messages of the ConsumerRecord object: A Kafka source provides the setValueOnlyDeserializer(DeserializationSchema) method. The DeserializationSchema class defines how a Kafka message that is stored as a binary value is deserialized. Use the classes that implement the Deserializer interface of Kafka. For example, you can use the StringDeserializer class to deserialize a message into a string. import org.apache.kafka.common.serialization.StringDeserializer KafkaSource.<String>builder() .setDeserializer(KafkaRecordDeserializationSchema.valueO ly(StringDeserializer.class)); Note If you want to deserialize a ConsumerRecord object, you must create a class that implements the KafkaRecordDeserializationSchema interface. |
|---|---|

When you use a Kafka DataStream connector, you must configure the following Kafka properties: Start offset You can use an offset initializer to specify an offset for a Kafka source when the Kafka source starts to read data. An offset initializer is an object that is based on the OffsetsInitializer interface. The KafkaSource class provides the following built-in offset initializers.

| Offset initializer | Code |
|---|---|

| Specifies that the Kafka source starts to consume messages | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. arliest()) |   |   |
|---|---|---|---|
|   |   | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. | e |
| from the earliest | arliest()) |   |   |
| record of each partition. |   |   |   |
| Specifies that the Kafka source starts to | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. atest()) |   |   |
|   |   | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. | l |
| consume messages from the latest record | atest()) |   |   |
| of each partition. |   |   |   |
| Specifies that the Kafka source starts to consume messages from the first record of each partition. The first record has a timestamp that is greater than or equal | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. imestamp(1592323200000L)) |   |   |
|   |   | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. |   |
| to the specified timestamp. Unit: | imestamp(1592323200000L)) |   |   |
| milliseconds. |   |   |   |
| Specifies that the Kafka source starts to consume messages from the committed offset of each partition and a reset strategy is specified. If a partition | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. ommittedOffsets(OffsetResetStrategy.EARLIEST)) |   |   |
|   |   | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. |   |
| does not have a | ommittedOffsets(OffsetResetStrategy.EARLIEST)) |   |   |
| committed offset, the reset strategy resets the offset and the Kafka source starts from the earliest record of the partition. |   |   |   |
| Specifies that the Kafka source starts to consume messages | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. ommittedOffsets()) |   |   |
|   |   | KafkaSource.builder().setStartingOffsets(OffsetsInitializer. |   |
| from the committed offset of each partition | ommittedOffsets()) |   |   |
| and no reset strategy is specified. |   |   |   |

> **Note:** If the built-in offset initializers do not meet your business requirements, you can create custom offset initializers.
> If you do not specify an offset initializer, the OffsetsInitializer.earliest() offset initializer is used by default.

Streaming mode and batch mode A Kafka source can operate in streaming mode or batch mode. By default, a Kafka source operates in streaming mode. In this mode, the deployment continues to run until the deployment fails or is canceled. If you want a Kafka source to operate in batch mode, you can call the setBounded(OffsetsInitializer) method to specify a stop offset. When all partitions reach their stop offsets, the Kafka source exits.

> **Note:** In most cases, a Kafka source that operates in streaming mode does not have a stop offset. If you want to debug a Kafka source that operates in streaming mode, you can call the setUnbounded(OffsetsInitializer) method to specify a stop offset. The methods that you can use to specify a stop offset vary based on whether you use the streaming mode or batch mode.

Dynamic partition discovery If you want a running deployment to process data from new topics and from new partitions that match your subscription pattern without the need to restart the deployment, you can enable the dynamic partition discovery feature on the Kafka source.

> **Note:** By default, the dynamic partition discovery feature is enabled, with an interval of 5 minutes. To disable this feature, you must explicitly set this parameter to a non- positive value. The following sample code shows how to configure the partition.discovery.interval.ms parameter:

```
KafkaSource.builder()
    .setProperty("partition.discovery.interval.ms", "10000") // Discover new pa
rtitions per 10 seconds.
```

Event time and watermarks By default, a Kafka source uses the timestamp that is attached to a record as the event time for the record. You can define a watermark strategy based on the event time of each record and send the watermarks to downstream services.

```
env.fromSource(kafkaSource, new CustomWatermarkStrategy(), "Kafka Source With Custo m Watermark Strategy")
```

For more information about how to define a watermark strategy, see Generating Watermarks. Consumer offsets When a checkpoint is generated, a Kafka source commits the Kafka consumer offset of each partition to Kafka brokers. This way, the Kafka consumer offsets that are recorded on Kafka brokers are consistent with the state of the checkpoint. The Kafka consumer can automatically commit the offsets on each partition to Kafka brokers on a regular basis. You can configure the automatic offset commission feature by using the enable.auto.commit and auto.commit.interval.ms parameters. If you disable the checkpointing feature, a Kafka source relies on the Kafka consumer to commit the offsets to Kafka brokers.

> **Note:** Kafka sources do not use the committed offsets that are recorded on Kafka brokers for fault tolerance. When you commit offsets, Kafka brokers can monitor the progress of record consumption on each partition.

Additional properties You can call the setProperties(Properties) and setProperty(String, String) methods to configure additional properties for the Kafka source and Kafka consumer. The following table describes the properties of a Kafka source.

| Property | Description |
|---|---|
| client.id.prefix | Specifies the prefix for the client ID of the Kafka consumer. |
| partition.discov ery.interval.ms | Specifies the time interval at which the Kafka source checks for new partitions. Note If the Kafka source operates in batch mode, the property is automatically set to -1. |
| register.consum er.metrics | Specifies whether to register metrics for the Kafka consumer in Realtime Compute for Apache Flink. |
| Additional properties for a Kafka consumer | For more information about the properties of a Kafka consumer, see Apache Kafka. Important The Kafka DataStream connector overwrites the values of the following properties: key.deserializer: The value of this property is set to ByteArrayDeserializer. value.deserializer: The value of this property is set to ByteArrayDeserializer. auto.offset.reset.strategy: The value of this property is set to OffsetsInitializer#getAutoOffsetResetStrategy(). |

The following sample code shows how the Kafka consumer connects to the Kafka cluster by using a JAAS configuration and the SASL/PLAIN authentication mechanism.

```
KafkaSource.builder()
    .setProperty("sasl.mechanism", "PLAIN")
    .setProperty("sasl.jaas.config",
"org.apache.kafka.common.security.plain.PlainLoginModule required username=\"username\" password=\"password\";")
```

Monitoring Kafka sources register metrics in Realtime Compute for Apache Flink for monitoring and diagnosis. Metric scope All metrics of a Kafka source are registered under the KafkaSourceReader metric group. KafkaSourceReader is a subgroup of the operator metric group. The metrics for a specific partition are registered in the KafkaSourceReader.topic. <topic_name>.partition.<partition_id> metric group. For example, a topic is named my-topic and the partition of the topic is named 1. The consumer offset of the partition is reported by the <some_parent_groups>.operator.KafkaSourceReader.topic.mytopic.partition.1.currentOffset metric. The number of successful commits of consumer offsets is measured by the <some_parent_groups>.operator.KafkaSourceReader.commitsSucceeded metric. Metrics

| Metric | Description | Scope |
|---|---|---|
| currentOffset | Reports the Kafka consumer offset of a partition. | TopicPartition |
| committedOffset | Reports the committed consumer offset of a partition. | TopicPartition |
| commitsSucceeded | Reports the number of successful commits of consumer offsets. | KafkaSourceReader |
| commitsFailed | Reports the number of failed commits of consumer offsets. | KafkaSourceReader |

Metrics for a Kafka consumer The metrics for a Kafka consumer are registered in the KafkaSourceReader.KafkaConsumer metric group. For example, the records-consumedtotal metric is registered at <some_parent_groups>.operator.KafkaSourceReader.KafkaConsumer.recordsconsumed-total. You can configure the register.consumer.metrics parameter to specify whether to register metrics for the Kafka consumer. By default, the register.consumer.metrics parameter is set to true. For more information about the metrics for a Kafka consumer, see Apache Kafka. Create a Kafka producer A Kafka producer can write data from multiple streams to one or more Kafka topics.

```
DataStream<String> stream = ... Properties properties = new Properties(); properties.setProperty("bootstrap.servers", "localhost:9092"); FlinkKafkaProducer<String> myProducer = new FlinkKafkaProducer<>(
        "my-topic",                  // target topic
        new SimpleStringSchema(),    // serialization schema
        properties,                  // producer config
        FlinkKafkaProducer.Semantic.EXACTLY_ONCE); // fault-tolerance
stream.addSink(myProducer);
```

The following table describes the parameters.

| Parameter | Description |
|---|---|
| Topic | The name of the default topic to which data is written. |
| Serialization schema | The serialization schema. The schema is specified by the SerializationSchema or KafkaSerializationSchema class. A producer converts Java or Scala objects into binary data and then writes the data to the required topic. You can use the KafkaSerializationSchema or SerializationSchema class to specify the schema that the Kafka producer uses during data serialization. A Kafka producer calls the ProducerRecord<byte[], byte[]> serialize(T element, Long timestamp) method for each incoming record to generate a ProducerRecord object that represents the serialized record. Then, the Kafka producer writes the ProducerRecord object to the required topic. The ProducerRecord class provides properties that you can configure to manage behavior when the Kafka producer writes a record to the required Kafka topic. You can configure the following properties of the ProducerRecord class: The name of the target topic. The message key. The name of the partition to which the record is written. |
| Properties of the Kafka client | The bootstrap.servers property is required. This property specifies the addresses of the Kafka brokers. Separate multiple addresses with a comma (,). |

| Delivery guarantee | After you enable the checkpointing feature, a Kafka producer can ensure exactly-once delivery. You can also configure the semantic parameter of a Kafka producer to specify one of the following fault tolerance semantics: Semantic.NONE: The Kafka producer does not ensure the delivery of data. Data may be lost or duplicated. Semantic.AT LEAST ONCE: By default, the Kafka producer ensures _ _ that data is not lost. However, data may be duplicated. Semantic.EXACTLY ONCE: The Kafka producer ensures that data is _ not lost or duplicated. The Kafka transaction mechanism is used to ensure exactly-once delivery. |
|---|---|

**Usage notes of Semantic.EXACTLY_ONCE**

When you use the transaction mechanism to write data into a Kafka topic, you must configure the isolation.level parameter for all Kafka consumers. The parameter has the following valid values: read_committed: Only the committed data is read. read_uncommitted: Data that is not committed can be read. This is the default value. Semantic.EXACTLY_ONCE mode relies on the ability to commit transactions that were started before taking a checkpoint, after recovering from the checkpoint. If the duration between the time when a deployment fails and the time when the deployment is restarted exceeds the specified transaction timeout period, data may be lost because Kafka automatically terminates the transactions that time out. Therefore, we recommend that you configure a transaction timeout period appropriately to your expected downtime. By default, the transaction.max.timeout.ms parameter of Kafka brokers is set to 15 minutes. The transaction timeout that you configure for a Kafka producer cannot exceed the transaction timeout setting for Kafka brokers. The default value of the transaction.timeout.ms parameter for a Kafka producer is 1 hour. Therefore, you must adjust the transaction timeout period for the Kafka brokers. The Semantic.EXACTLY_ONCE mode uses a fixed-size pool for each FlinkKafkaProducer instance. One of each of those producers is used per one checkpoint. If the number of concurrent checkpoints exceeds the pool size, FlinkKafkaProducer will throw an exception and fail the entire deployment. You must configure a maximum pool size and the maximum number of concurrent checkpoints accordingly. When a deployment starts, the Kafka producer that operates in Semantic.EXACTLY_ONCE execution mode tries to terminate transactions that are not committed during checkpointing. These uncommitted transactions may block consumers from reading data. If a Realtime Compute for Apache Flink deployment fails before the first checkpoint is taken, the information about the transactions that are used by the Kafka producer is lost when the deployment is restarted. If you want to reduce the deployment parallelism before the first checkpoint is taken, make sure that the value after you divide the original parallelism by the new parallelism is greater than or equal to the value of FlinkKafkaProducer.SAFE_SCALE_DOWN_FACTOR. Otherwise, memory leaks may occur because of untracked transactions. For a Kafka consumer for which the isolation.level is set to read_committed, any uncommitted transaction (neither terminated nor completed) will block all reads from the Kafka topic. Example: i. A user creates a transaction to write data to a topic. ii. The user creates another transaction to write data to the topic. iii. The user commits the second transaction. In this case, the Kafka consumer cannot read the data from the second transaction until the first transaction is committed or terminated. Therefore, take note of the following items: You can estimate the delay at which data is written to the required Kafka topic, and set the checkpoint interval to the value of the delay. If a Realtime Compute for Apache Flink deployment fails, the topics that are written by the deployment block consumers from reading data until the deployment is restarted or the transactions time out.

### 5.30 Hologres connector

This topic describes how to use the Hologres connector.

**Background information**

Hologres is an end-to-end real-time data warehouse service that allows you to write, update, and analyze large amounts of data in real time. Hologres is compatible with the PostgreSQL protocol and supports standard SQL syntax. Hologres supports online analytical processing (OLAP) and ad hoc queries on petabytes of data, and provides high-concurrency, low-latency online data services. Hologres is seamlessly integrated with MaxCompute, Realtime Compute for Apache Flink, and DataWorks, and provides full-stack online and offline data warehouse solutions. The following table describes the capabilities supported by the Hologres connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode and batch mode |
| Data formats | Not supported |
| Monitoring metrics | Metrics for source tables: numRecordsIn numRecordsInPerSecond Metrics for sink tables: numRecordsOut numRecordsOutPerSecond currentSendTime |
| API types | DataStream API and SQL API |
| Data updates or deletion in a sink table | Supported |

**Features**

**Source table**

| Feature | Description |
|---|---|
| Real-time consumption of Hologres data | Reads data from a Hologres source table in which the binary logging feature is disabled. Consumes the binary log data of Hologres in real time. Consumes data in non-Change Data Capture (CDC) mode. Consumes data in CDC mode. Consumes full and incremental data by using a source table. |

**Sink table**

| Feature | Description |
|---|---|
| Streaming semantics | Writes changelogs to a Hologres sink table. |
| Merges data into a wide table | Updates only data in specific fields instead of data in an entire row. |
| Data synchronization based on the CREATE TABLE AS and CREATE DATABASE AS statements | Synchronizes data from an entire database or a single table to Hologres tables in real time and synchronizes schema changes of each table to Hologres tables in real time. |
| Data update in specific columns Note Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 6.0.7 or later supports this feature. | Pushes down the column names that are specified in the INSERT statement of Realtime Compute for Apache Flink to the Hologres connector to update only the specified columns. |

**Prerequisites**

A Hologres table is created.

**Limits**

Limits on all types of Hologres tables: The Hologres connector cannot be used to access Hologres external tables. Limits only on Hologres source tables: By default, Realtime Compute for Apache Flink performs a full table scan only once to read all data from a Hologres source table at a time. Data consumption is complete when the data scan ends. Realtime Compute for Apache Flink does not read the data that is appended to the Hologres source table after the data consumption. In Realtime Compute for Apache Flink that uses VVR 6.0.3 or later, filter pushdown is supported when the Hologres connector reads data from Hologres. For more information, see the description of the `enable_filter_push_down` parameter that is used only for source tables. Realtime Compute for Apache Flink that uses a VVR version earlier than 8.0 does not support watermarks for a Hologres source table in CDC mode. If you want to perform window aggregation on a Hologres source table, you can use a different approach to perform time-based aggregation. Limits only on Hologres sink tables: None. Limits only on Hologres dimension tables: We recommend that you specify a primary key as the JOIN condition for a Hologres dimension table when you join the Hologres dimension table with another table and use row-oriented storage to create a Hologres dimension table. Column-oriented storage incurs large performance overheads for point queries. When you use row-oriented storage to create a Hologres dimension table, you must specify the primary key as the clustering key. If you cannot use the primary key as the JOIN condition and you perform a point query by using a non-primary key, we recommend that you use column-oriented storage when you create a Hologres table. If you perform a point query by using a non-primary key, a row of data is queried, and multiple rows of data are returned. In this case, we recommend that you specify the distribution key and event time column (segment key) to optimize query performance.

**Usage notes**

**If you set the sdkMode parameter to rpc for a table, take note of the following**

**items when you upgrade the VVR version:**

The SDK modes that can be configured for dimension tables and sink tables of Hologres V2.0 and later are changed. You cannot set the sdkMode parameter to rpc for dimension tables or sink tables. Only the Java Database Connectivity (JDBC)-related modes can be used for tables. The JDBC-related modes include the JDBC, jdbc_fixed, and jdbc_copy modes. If you set the sdkMode parameter to rpc for a table, Realtime Compute for Apache Flink does not deduplicate data that has the same primary key in the same batch. If you want to retain complete data, you can use a JDBC-related mode for the table and set the jdbcWriteBatchSize parameter to 1 to avoid deduplication. You can also upgrade the VVR version to 8.0.5 and set the deduplication.enabled parameter to false to avoid deduplication. If you want to upgrade the VVR version from 4.X to 6.X or from 4.X to 8.X for a deployment in which data of Hologres V2.0 is read or written in remote procedure call (RPC) mode, you can configure the SDK mode based on the upgrade scenario. If you upgrade the VVR version from 4.X to a 6.X minor version that ranges from 6.0.4 to 6.0.6, an error may be returned. We recommend that you set the sdkMode parameter to jdbc or jdbc_fixed for dimension tables and sink tables. If you upgrade the VVR version from 4.X to 6.0.7 or later, no operation is required. Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to JDBC-related modes.

**If you set the sdkMode parameter to holohub for a binary log source table, take**

**note of the following items when you upgrade the VVR version:**

In Hologres V2.0 and later, you can set the sdkMode to holohub for Hologres binlog source tables only in specific scenarios. In Hologres V2.1 and later, you cannot set the sdkMode parameter to holohub for Hologres binlog source tables, and you can only set the sdkMode parameter to jdbc for Hologres binlog source tables. If a binary log source table is consumed in your deployment and you do not set the sdkMode parameter to jdbc, the HoloHub mode is used for the binary log source table by default. If you want to upgrade the VVR version from 4.X to 6.X or from 4.X to 8.X, take note of the following points based on the Hologres version when you configure the SDK mode. Hologres V2.0 If you upgrade the VVR version from 4.X to a VVR version that ranges from 6.0.7 to 8.0.3, Realtime Compute for Apache Flink still reads data from a binary log source table in HoloHub mode. If you upgrade the VVR version to 8.0.4 or later, an insufficient permission error may be returned. To address the issue, you must obtain the required permissions. Hologres V2.1 If you upgrade the VVR version from 4.X to a VVR version that ranges from 6.0.7 to 8.0.4, binary log data may not be consumed as expected. We recommend that you upgrade the VVR version to 8.0.5. If you upgrade the VVR version from 4.X to 8.0.5 or later, no operation is required. Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to JDBC.

**Syntax**

```
CREATE TABLE hologres_table (
  name VARCHAR,
  age BIGINT,
  birthday BIGINT,
  PRIMARY KEY (name) NOT ENFORCED
) WITH (
  'connector' = 'hologres',
  'dbname' = '<yourDBName>',
  'tablename' = '<yourTableName>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint' = '<yourEndpoint>',
  'sdkmode' = 'jdbc'
```

);

**Parameters in the WITH clause**

Common parameters

| Param eter | Descript ion | Data type | Req uire d | Def aul t val ue | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | String | Yes | Non e | Set the value to hologres . |

| dbname | The name of the database. | String | Yes |   | Non | Hologres V2.0 introduces virtual warehouse instances as a new type of elastic and high- availability instances. Computing resources are divided into multiple virtual warehouses that are more suitable for high-availability scenarios. Different virtual warehouses share the same endpoint. You can add a specific suffix to the value of the dbname parameter to specify the virtual warehouse to which you want to connect. For example, if you want to connect a dimension table to the virtual warehouse read warehouse, _ you can specify 'dbname' = 'db test@read warehouse' . _ _ Note Virtual warehouses are supported only when JDBC-related modes are used for tables. For more information, see the sdkMode parameter of the source table, dimension table, and sink table in the "Parameters in the WITH clause" section of this topic. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | _ 'dbname' = |   |
|   |   |   |   | es | e | 'db test@read warehouse' _ _ |   |   |
| tablena me | The table name. | String | Yes |   | Non e | If the public schema is not used, you must specify tablename in the schema.tableName format. |   |   |
| userna me | The username that is used to access the database. Enter the AccessKe y ID of your Apsara Stack tenant account. | String | Yes |   | Non e | None. |   |   |

| passwo rd | The password that is used to access the database. Enter the AccessKe y secret of your Apsara Stack tenant account. | String | Yes | Non e | None. |
|---|---|---|---|---|---|
| endpoin t | The endpoint of Hologres. | String | Yes | Non e | Contact Apsara Stack O&M engineers to obtain the required information. |

| connect ion.ssl. mode | Specifies whether to enable SSL- encrypte d transmiss ion and specifies the SSL- encrypte d transmiss ion mode that you want to use. | String | No | disa ble | Valid values: disable: disables SSL-encrypted transmission. This is the default value. require: enables SSL-encrypted transmission. The client uses SSL-encrypted transmission to encrypt only the connections that are used to transmit data. verify-ca: enables SSL-encrypted transmission. The client uses SSL-encrypted transmission to encrypt the connections that transmit data and uses certificate authority (CA) certificates to verify the Hologres server. verify-full: enables SSL-encrypted transmission. The client uses SSL-encrypted transmission to encrypt the connections that transmit data, uses CA certificates to verify the Hologres server, and checks whether the common name (CN) or Domain Name System (DNS) specified in the CA certificates is consistent with the Hologres endpoint that is specified during connection setup. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. You can set the connection.ssl.mode parameter to require in Hologres V1.1 and later. You can set the connection.ssl.mode parameter to verify-ca or verify-full in Hologres V2.1 and later. If you set this parameter to verify-ca or verify-full, you must specify the connection.ssl.root-cert.location parameter. |
|---|---|---|---|---|---|
| connect ion.ssl.r oot- cert.loc ation | The path of the certificat e if a CA certificat e is used. | String | No | Non e | If you set the connection.ssl.mode parameter to verify-ca or verify-full, you must specify this parameter. You can click Upload Artifact on the Artifacts page in the development console of Realtime Compute for Apache Flink to upload the CA certificate file. The uploaded file is stored in the /flink/usrlib directory. For example, if the name of the CA certificate file that you want to use is certificate.crt, you must set this parameter to '/flink/usrlib/certificate.crt' in the WITH clause. This way, you can use the certificate after you upload the certificate file. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. |

| jdbcRet ryCount | The maximum number of retries allowed to read and write data if a connectio n failure occurs. | Intege r | No | 10 | None. |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | The actual waiting duration for a retry is calculated by using the following formula: Value of the jdbcRetrySleepInitMs |   |
|   |   |   |   |   |   | Value of the jdbcRetrySleepInitMs |
|   | The fixed |   |   |   | parameter + Number of retries up to the |   |
| jdbcRet |   |   |   |   |   |   |
|   | waiting |   |   | 100 | current retry × Value of the |   |
| rySleepI | duration | Long | No |   |   |   |
| nitMs | for each |   |   | 0 | jdbcRetrySleepStepMs parameter |   |
|   | retry. |   |   |   |   |   |
| jdbcRet rySleep | The accumula ted waiting duration |   |   |   | The actual waiting duration for a retry is calculated by using the following formula: Value of the jdbcRetrySleepInitMs |   |
|   |   |   |   |   |   | Value of the jdbcRetrySleepInitMs |
|   | for each retry. | Long | No | 500 | parameter + Number of retries up to the |   |
| StepMs |   |   |   | 0 |   |   |
|   |   |   |   |   | current retry × Value of the |   |
|   |   |   |   |   | jdbcRetrySleepStepMs parameter |   |
| jdbcCon nection MaxIdle Ms | The maximum duration for which the JDBC connectio n can remain idle. | Long | No | 600 00 | If a JDBC connection remains idle for a period of time that exceeds the value of this parameter, the connection is closed and released. Unit: milliseconds. |   |
| jdbcMet aCache TTL | The maximum time for storing the TableSch ema informati on in the cache. | Long | No | 600 00 | Unit: milliseconds. |   |

| jdbcMet aAutoR efreshF actor | The factor for triggering automati c cache refresh. If the remainin g time for storing data in the cache is less than the time for triggering an automati c refresh of the cache, Realtime Compute for Apache Flink automati cally refreshes the cache. | Intege r | No | 4 | The remaining time for storing data in the cache is calculated by using the following formula: Remaining time for storing data in the cache = Maximum time that is allowed to store data in the cache - Duration for which data is cached. After the cache is automatically refreshed, the duration for which data is cached is recalculated from 0. The time for triggering automatic cache refresh is calculated by using the following formula: Time for triggering an automatic refresh of the cache = Value of the jdbcMetaCacheTTL parameter/Value of the jdbcMetaAutoRefreshFactor parameter. |
|---|---|---|---|---|---|
| type- mappin g.timest amp- converti ng.lega cy | Specifies whether to perform time type conversio ns between Realtime Compute for Apache Flink and Hologres. | Boole an | No | true | Valid values: true: does not perform time type conversions between Realtime Compute for Apache Flink and Hologres. Time zone conversion is performed based on the time zone of Java Virtual Machine (JVM) in the runtime environment. false: recommended. Performs time type conversions between Realtime Compute for Apache Flink and Hologres. Time zone conversion is performed based on the time zone of Realtime Compute for Apache Flink. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.6 or later supports this parameter. If you set the property-version parameter to 0, the default value of this parameter is true. If you set the property-version parameter to 1, the default value of this parameter is false. |

| proper ty- versio n | The paramete r version of the connector . | Intege r | No | 0 | Valid values: 0 and 1. Default value: 0. Note Only Realtime Compute for Apache Flink that uses Ververica Runtime (VVR) 8.0.6 or later supports this parameter. The set of available parameters and the default values of the parameters may be different in different parameter versions. If the set of available parameters and the default values of the parameters are different, the differences are described in the description of the parameters. We recommend that you set this parameter to 1. |
|---|---|---|---|---|---|

Source table-specific parameters

| Parame ter | Description | Data type | Requ ired | Default value | Remarks |
|---|---|---|---|---|---|
| field deli _ miter | The delimiter that is used between rows of the data that you want to export. | String | No | "\u0002 " | None. |
| binlog | Specifies whether to consume binary log data. | Boole an | No | false | Valid values: true: Binary log data is consumed. false: Binary log data is not consumed. This is the default value. Note In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the default value of this parameter varies based on the parameter version of the connector. If you set the property- version parameter to 0, the default value of this parameter is false. If you set the property- version parameter to 1, the default value of this parameter is true. |

|   |   |   |   |   | Valid values: holohub: Binary log data is consumed in HoloHub mode. This is the default value. jdbc: Binary log data is consumed in JDBC mode. jdbc fixed: Binary log data is _ consumed in fixed JDBC mode. Compared with data consumption in JDBC mode, data consumption in fixed JDBC mode does not occupy connections and is not subject to limits on the number of connections. Note VVR 6.0.3 and an earlier 6.X version: This parameter is not supported. VVR 6.0.4 to VVR 6.0.6: We recommend that you set this parameter to holohub. VVR 6.0.7 or later: We recommend that you set this parameter to jdbc. If the Hologres instance is of a version earlier than Hologres V2.0, Realtime Compute for Apache Flink uses the SDK mode that you configure. In Hologres V2.0 or later, the HoloHub mode is no longer supported. If you set this parameter to holohub, Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to JDBC. If you set this parameter to jdbc, Realtime Compute for Apache Flink uses the JDBC mode. |
|---|---|---|---|---|---|

|   | sdkMode | The SDK mode. | String | No | holohub |   | VVR 8.0.4 to VVR 8.0.5: In Hologres V2.0, Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to JDBC. Issues such as insufficient permissions may arise. In Hologres V2.1 or later, Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to JDBC. VVR 8.0.6 and later: For Hologres V2.1.27 or later, Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to fixed JDBC. For Hologres V2.1.0 to Hologres V2.1.26, Realtime Compute for Apache Flink automatically changes the SDK mode from HoloHub to JDBC. In Hologres V2.0, Realtime Compute for Apache Flink first attempts to use the JDBC mode. If an exception occurs, such as insufficient permission, |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | Realtime Compute for Apache Flink automatically switches to the HoloHub mode. | Realtime Compute for Apache Flink automatically switches to the HoloHub mode. |   |   |

| jdbcBinl ogSlotN ame | The slot name of the binary log source table in JDBC mode. | String | No | None | This parameter takes effect only when the sdkMode parameter is set to jdbc. If you do not configure this parameter, the Hologres connector creates a slot by default. Note You do not need to specify this parameter when the version of the Hologres instance is 2.1 or later. The Hologres connector does not attempt to automatically create a slot. |
|---|---|---|---|---|---|
| binlogM axRetry Times | The number of retries after Realtime Compute for Apache Flink fails to read binary log data. | Intege r | No | 60 | None. |
| binlogRe tryInterv alMs | The interval between retries after Realtime Compute for Apache Flink fails to read binary log data. | Long | No | 2000 | Unit: milliseconds. |
| binlogBa tchRead Size | The number of rows in which binary log data is read at a time. | Intege r | No | 100 | None. |

| cdcMode | Specifies whether to read binary log data in CDC mode. | Boole an | No | false | Valid values: true: Binary log data is read in CDC mode. false: Binary log data is read in non- CDC mode. This is the default value. Note In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the default value of this parameter varies based on the parameter version of the connector. If you set the property- version parameter to 0, the default value of this parameter is false. If you set the property- version parameter to 1, the default value of this parameter is true. |
|---|---|---|---|---|---|
| upsertSo urce | Specifies whether the source table reads a changelog stream that contains UPSERT messages. | Boole an | No | false | This parameter takes effect only in CDC mode. Valid values: true: The source table reads a changelog stream that contains only UPSERT messages, including INSERT, DELETE, and UPDATE AFTER. _ false: The source table reads a changelog stream that contains full change messages, including INSERT, DELETE, UPDATE BEFORE, and _ UPDATE AFTER. This is the default _ value. Note For example, if the ROW NUMBER() function together _ with an OVER clause of Flink SQL is used to perform deduplication and retract operators exist in the sink table, you must set upsertSource to true. In this case, the source table reads data from Hologres in the upsert fashion. |

| binlogSt artupMo de | The mode in which binary log data is consumed. | String | No | earliest Offset | Valid values: initial: The system consumes full data and then reads binary log data to consume incremental data. earliestOffset: The system starts data consumption from the earliest binary log data. timestamp: The system consumes binary log data from the point in time that is specified by the startTime parameter. Note If the startTime parameter is configured or the start time is specified in the dialog box for starting a deployment, the timestamp mode is forcefully used for the binlogStartupMode parameter. The other two values of this parameter cannot be used. In this case, the configuration of the startTime parameter has a higher priority. Note In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the default value of this parameter varies based on the parameter version of the connector. If you set the property- version parameter to 0, the default value of this parameter is false. If you set the property- version parameter to 1, the default value of this parameter is true. |
|---|---|---|---|---|---|
| startTim e | The start time when Hologres data is consumed. | String | No | None | The time is in the yyyy-MM-dd hh:mm:ss format. If this parameter is not specified and deployments are not resumed from the state, Realtime Compute for Apache Flink starts to consume the Hologres data from the earliest generated binary log. |

| jdbcSca nFetchSi ze | The number of data records that can be processed at a time during the scan operation. | Intege r | No | 256 | None. |
|---|---|---|---|---|---|
| jdbcSca nTimeou tSecond s | The timeout period of the scan operation. | Intege r | No | 60 | Unit: seconds. |
| jdbcSca nTransa ctionSes sionTim eoutSec onds | The timeout period for the transaction to which the scan operation belongs. | Intege r | No | 600 | If this parameter is set to 0, the scan operation never times out. This parameter corresponds to the Grand Unified Configuration (GUC) parameter idle in transaction session timeout of _ _ _ _ Hologres. |

| enable f _ ilter pus _ h down _ | Specifies whether to perform filter pushdown during the full data reading phase. | Boole an | No | false | Valid values: false: Filter pushdown is not performed. true: The supported filter conditions are pushed down to Hologres during the full data reading phase. The filter pushdown operation is performed in the following full data reading scenarios: full data reading from a Hologres source table in which the binary logging feature is disabled, and full data reading in a binary log source table when the Hologres connector consumes full and incremental data in a source table. Important In Realtime Compute for Apache Flink whose engine version is from vvr-6.0.3-flink- 1.15 to vvr-6.0.5-flink-1.15, filter pushdown is automatically performed. However, if a deployment uses a Hologres dimension table and the DML statement that is used to write data contains filter conditions for non-primary key fields in the dimension table, the filter conditions of the dimension table are incorrectly pushed down. As a result, an error may occur when the dimension table is joined with another table. To resolve this issue, we recommend that you use Realtime Compute for Apache Flink whose engine version is vvr-6.0.6-flink-1.15 or later and add this parameter to the WITH clause in the DDL statement that is used to create the source table to enable filter pushdown. |
|---|---|---|---|---|---|

Sink table-specific parameters

| Para mete r | Desc ripti on | Data type | Requ ired | Defa ult valu e | Remarks |
|---|---|---|---|---|---|
| sdkM ode | The SDK mode . | String | No | jdbc | Valid values: jdbc: Data is written by using a JDBC driver. jdbc copy: Data is written in jdbc copy mode, _ _ which refers to the copy mode of a JDBC driver. This mode is a new feature that is supported in Hologres 1.3. Data writing in this mode provides higher throughput and lower data latency, and consumes less client memory resources than data writing in JDBC mode because data is written in streaming mode. If the jdbc copy _ mode is used, data cannot be deleted, data cannot be written to a parent partitioned table, and the ignoreNullWhenUpdate parameter is not supported. rpc: Data is written in RPC mode. The effect when you set this parameter to rpc is similar to the effect when you set the useRpcMode parameter to true. Compared with data writing in JDBC mode, data writing in RPC mode does not occupy connections. Data of the Jsonb and RoarinBitmap data type cannot be written to Hologres. jdbc fixed: In this mode, data writing is _ performed by using a fixed JDBC driver. This feature is in public preview. Only Hologres 1.3 or later supports this feature. Compared with data writing that is performed in JDBC mode, data writing that is performed in jdbc fixed mode do not occupy connections. _ Data of the Jsonb and RoarinBitmap data type cannot be written to Hologres. Note VVR 6.0.3 or an earlier 6.X version: This parameter is not supported. VVR 6.0.4 to VVR 6.0.6: We recommend that you set this parameter to jdbc. |

|   |   |   |   |   |   | VVR 6.0.7 to VVR 8.0.1: We recommend that you set this parameter to jdbc. If the Hologres instance is of a version earlier than Hologres V2.0, the Flink system uses the SDK mode that you configure. In Hologres V2.0 or later, the RPC mode is no longer supported. If you set this parameter to rpc, Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to jdbc fixed. If _ you set this parameter to a value other than rpc, Realtime Compute for Apache Flink uses the SDK mode that you configure. If you use the RPC mode for a table, Realtime Compute for Apache Flink does not perform deduplication on the data that has the same primary key. If you want to retain complete data, you can use a JDBC- related mode for the table and set the jdbcWriteBatchSize parameter to 1 to avoid deduplication. VVR 8.0.3 and a later 8.X version: We recommend that you set this parameter to jdbc. For Realtime Compute for Apache Flink that uses VVR 8.0.3 or later, the RPC mode is no longer supported for tables regardless of the versions of Hologres instances. If the RPC mode is used for tables, Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to jdbc fixed, and you _ can set the jdbcWriteBatchSize |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | parameter to 1 to avoid deduplication. VVR 8.0.5 and later: We recommend that you set this parameter to jdbc. If you use the RPC mode for tables, Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to jdbc fixed, and you can set |   |
|   |   |   |   |   |   | _ the deduplication.enabled parameter to false to avoid deduplication. |   |

| bulkl oad | Speci fies whet her to write data in bulklo ad mode . | Boole an | No | false | This parameter takes effect only when the sdkMode parameter is set to jdbc copy. You can write data _ in bulkload mode to tables that do not have primary keys or tables whose primary keys have the same value. Compared with the jdbc copy _ mode, less Hologres resources are used when you write data in bulkload mode. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later and Hologres V2.1 or later support this parameter. |
|---|---|---|---|---|---|

| useR pcMo de | Speci fies whet her to conn ect to the Holog res conn ector by using RPC. | Boole an | No | false | Valid values: true: RPC is used to connect to the Hologres connector. The effect of this setting is the same as the effect when you set the sdkMode parameter to rpc. If RPC is used, the number of SQL connections is reduced. false: A JDBC driver is used to connect to the Hologres connector. This is the default value. JDBC drivers require SQL connections. This increases the number of JDBC connections. Note The RPC mode is no longer supported in Hologres V2.0. We recommend that you specify the sdkMode parameter to write data in JDBC or jdbc fixed mode. _ Realtime Compute for Apache Flink that uses VVR 6.0.7 or VVR 8.0.1 automatically changes the SDK mode from RPC to jdbc fixed for a table when _ it detects that the version of Hologres is V2.0 or later. Realtime Compute for Apache Flink that uses VVR 8.0.3 or later automatically changes the SDK mode from RPC to jdbc fixed. _ If you use the RPC mode for a table, Realtime Compute for Apache Flink does not perform deduplication on the data that has the same primary key. If you want to retain complete data, we recommend that you use Realtime Compute for Apache Flink that uses VVR 8.0.5 or later, set the sdkMode parameter to jdbc, and set the deduplication.enabled parameter to false to avoid deduplication. If you set the property-version parameter to 1, this parameter is not supported. |
|---|---|---|---|---|---|

| muta tetyp e | The data writin g mode . | String | No | insert orign ore | In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the default value of this parameter varies based on the parameter version of the connector. If you set the property-version parameter to 0, the default value of this parameter is insertorignore. If you set the property-version parameter to 1, the default value of this parameter is insertorupdate. |
|---|---|---|---|---|---|
| partit ionro uter | Speci fies whet her to write data to a partiti oned table. | Boole an | No | false | None. |

| creat epart table | Speci fies whet her to auto matic ally creat e a partiti oned table to which data is writte n based on partiti on value s. | Boole an | No | false | In RPC mode, if the partition values contain hyphens (-), partitioned tables cannot be automatically created. Note In Hologres V1.3.22 or later, a field of the DATE type can be used as the partition key. For Realtime Compute for Apache Flink that uses VVR 8.0.3 or later, a partitioned table can be automatically created when you use a field of the DATE type as the partition key. Make sure that partition values do not contain dirty data. If dirty data exists, a failover occurs because an invalid partitioned table is created. Proceed with caution when you use this parameter. If you set the sdk mode parameter to _ jdbc copy, data cannot be written to a _ parent partitioned table. |
|---|---|---|---|---|---|
| ignor edele te | Speci fies whet her to ignor e retrac tion mess ages. | Boole an | No | true | This parameter takes effect only for Hologres. In Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, the default value of this parameter varies based on the parameter version of the connector. If you set the property-version parameter to 0, the default value of this parameter is true. If you set the property-version parameter to 1, the default value of this parameter is false. |

| conn ectio nSize | The size of the JDBC conn ectio n pool that is creat ed in a single Realti me Comp ute for Apac he Flink deplo ymen t. | Intege r | No | 3 | If the deployment provides poor performance, we recommend that you increase the size of the connection pool. The size of the JDBC connection pool is proportional to data throughput. |
|---|---|---|---|---|---|
| jdbc Write Batch Size | The maxi mum numb er of rows of data that can be proce ssed by a Holog res strea ming sink node at a time when a JDBC driver is used. | Intege r | No | 256 | Unit: row. Note You can configure only one of the following parameters: jdbcWriteBatchSize, jdbcWriteBatchByteSize, and jdbcWriteFlushInterval. If you specify all the preceding parameters, the system writes data to a Hologres sink table when one of the related conditions is met. |

| jdbc Write Batch ByteS ize | The maxi mum numb er of bytes of data that can be proce ssed by a Holog res strea ming sink node at a time when a JDBC driver is used. | Long | No | 2097 152 (2 × 1024 × 1024 bytes = 2 MB) | You can configure only one of the following parameters: jdbcWriteBatchSize, jdbcWriteBatchByteSize, and jdbcWriteFlushInterval. If you specify all the preceding parameters, the system writes data to a Hologres sink table when one of the related conditions is met. |
|---|---|---|---|---|---|

| jdbc Write FlushI nterv al | The maxi mum perio d of time that is requir ed to wait for a Holog res strea ming sink node to write data from multi ple rows to Holog res at the same time when a JDBC driver is used. | Long | No | 1000 0 | Unit: milliseconds. You can configure only one of the following parameters: jdbcWriteBatchSize, jdbcWriteBatchByteSize, and jdbcWriteFlushInterval. If you specify all the preceding parameters, the system writes data to a Hologres sink table when one of the related conditions is met. |
|---|---|---|---|---|---|

| ignor eNull When Upda te | Speci fies whet her to ignor e the null value that is writte n in the data if mutat etype ='ins ertOr Updat e' is specif ied. | Boole an | No | false | Valid values: false: The null value is written to a Hologres sink table. true: The null value that is written in the data is ignored. Note If you set the sdk mode parameter to _ jdbc copy, this parameter is not supported. _ |
|---|---|---|---|---|---|

| conn ectio nPool Name | The name of the conn ectio n pool. In the same Task Mana ger, table s for which the same conn ectio n pool is confi gured can share the conn ectio n pool. | String | No | None | Set the value to a string other than default . If the same connection pool is configured for multiple tables, the value of the connectionSize parameter for the tables must be the same. Note VVR 4.0.12 to VVR 8.0.3: By default, tables do not share a connection pool. Each table uses its connection pool. VVR 8.0.4 or later: By default, tables that use the same endpoint in the same deployment share a connection pool. If the number of tables in a deployment is excessively large, the connections in a connection pool may be relatively insufficient. This affects the deployment performance. In this case, we recommend that you set the connectionPoolName parameter to different values for different tables. You can specify this parameter based on your business requirements. For example, a deployment uses the following Hologres tables: Dimension Table A, Dimension Table B, Sink Table C, Sink Table D, and Sink Table E. You can configure the connection pool pool1 for Dimension Table A and Dimension Table B, and the connection pool pool2 for Sink Table C and Sink Table D. You can configure the connection pool pool3 for Sink Table E in which a large number of data is processed. |
|---|---|---|---|---|---|

|   |   |   |   |   | or |
|---|---|---|---|---|---|
| jdbcE nable Defa ultFor NotN ullCol umn | Speci fies whet her to allow the Holog res conn ector to fill a defau lt value if a null value is writte n to a non- null colu mn for which the defau lt value is not confi gured in the Holog res table. | Boole an | No | true | Valid values: true: The Hologres connector fills a default value. This is the default value. If you set this parameter to true, the system converts a null value into a default value based on the following rules: If the column is of the STRING type, the column is left empty. If the column is of the NUMBER data type, the null value is converted into 0. If the column is of the DATE, TIMESTAMP, or TIMESTAMPTZ data type, the null value is converted into 1970-01-01 00:00:00. false: The Hologres connector does not fill a default value. If a null value is written to a non- null column for which the default value is not configured in the Hologres table, an error is returned. |

| remo ve- u000 0-in- text.e nable d | Speci fies whet her to allow the Holog res conn ector to remo ve the invali d chara cters \u000 0 from data of the STRIN G type that is writte n to the sink table if the data conta ins the invali d chara cters \u000 0. | Boole an |   |   |   | Valid values: false: The Hologres connector does not process data. If the data that is written to the sink table contains dirty data, the "ERROR: invalid byte sequence for encoding "UTF8": 0x00" error message may be reported. This is the default value. In this case, you need to remove the dirty data from the source table in advance or define the dirty data processing logic in the SQL statement. true: The Hologres connector removes the invalid characters \u0000 from the data of the STRING type to prevent the error message from being reported. |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | "ERROR: invalid byte |
|   |   |   |   |   |   | sequence for encoding "UTF8": 0x00" |   |
|   |   |   |   | No | false |   |   |

| partia l- insert .enab led | Speci fies whet her to insert only the fields decla red in the INSER T state ment. | Boole an | No | false | Valid values: false: All fields that are declared in the DDL statement of the sink table are updated regardless of which fields are declared in the INSERT statement. Fields that are not declared in the INSERT statement are updated to null values. This is the default value. true: The fields that are declared in the INSERT statement are pushed down to a connector. In this case, only the declared fields are updated in the sink table or inserted into the sink table. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. This parameter takes effect only if the mutatetype parameter is set to InsertOrUpdate. |
|---|---|---|---|---|---|

| dedu plicat ion.e nable d | Speci fies whet her to perfor m dedu plicati on when data is writte n in batch es in jdbc or jdbc f _ ixed mode . | Boole an | No | true | Valid values: true: If the data that is written in batches contains data that has the same primary key, deduplication is performed. Only the last data record is retained. This is the default value. In this example, two fields are used and the first field is the primary key. If the INSERT (1,'a') and INSERT (1,'b') records are written to the sink table in chronological order, only the record (1,'b') that arrives later is retained and written to the Hologres sink table after deduplication is performed. The (1,'a') record already exists in the Hologres sink table. In this case, the DELETE (1,'a') and INSERT (1,'b') records are written to the sink table in chronological order. Only the (1,'b') record that arrives later is retained and written to the Hologres sink table. In this case, data is directly updated rather than deleted and then inserted into the table. false: No deduplication is performed when data is written in batches. If the primary key of the inserted data has the same value as the primary key of the data that is written in batches, the data in batches is written, and then the data that needs to be inserted is written. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. In extreme cases, if no deduplication is performed when data is written in batches and all data has the same primary key, data is not written in batches. This may affect the performance. |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | DELETE |   |

|   |   | INSERT (1,'a') |
|---|---|---|
|   | (1,'b') |   |

| INSERT |   |
|---|---|

|   | (1,'a') |
|---|---|

Parameters only for dimension tables

| Para mete r | Desc ripti on | Data type | Req uire d | Default value | Remarks |
|---|---|---|---|---|---|
|   |   |   |   |   | Valid values: jdbc: Queries are performed in JDBC mode. Point queries based on a primary key and queries based on a non-primary key are supported. However, queries based on a non-primary key affect the query performance, and the query speed is slow. This is the default value. |

|   |   |   |   |   | nk (Compute-Storage Separation Edition) User Guide·Data connec or |
|---|---|---|---|---|---|
| sdkMo de | The SDK mode . | Strin g | No | jdbc | rpc: Point queries are performed in RPC mode. If you set this parameter to rpc, the effect is similar to the effect when you set the useRpcMode parameter to true. Only point queries based on a primary key are supported. When you join a Hologres dimension table with another table, you must specify all the fields in the primary keys of the dimension table in the ON clause. Compared with point queries that are performed in JDBC mode, point queries that are performed in RPC mode do not occupy connections. Data of the Jsonb and RoarinBitmap data type cannot be queried in Hologres. jdbc fixed: In this mode, point queries are _ performed by using a fixed JDBC driver. This feature is in public preview. Only Hologres 1.3 or later supports this feature. Compared with point queries that are performed in JDBC mode, point queries that are performed in jdbc fixed mode do _ not occupy connections. Data of the Jsonb and RoarinBitmap data type cannot be queried in Hologres. Only point queries based on a primary key are supported. When you join a Hologres dimension table with another table, you must specify all the fields in the primary keys of the dimension table in the ON clause. Note VVR 6.0.3 or an earlier 6.X version: This parameter is not supported. VVR 6.0.4 to VVR 6.0.6: We recommend that you set this parameter to jdbc. For Realtime Compute for Apache Flink that uses VVR 6.0.6, if you set this parameter to jdbc, a null pointer error may occur when data of the STRING data type is queried in JDBC mode and the query results contain null values. To resolve this issue, we recommend that you use the RPC mode. |

|   |   |   |   |   |   | VVR 6.0.7 and VVR 8.0.1: We recommend that you set this parameter to jdbc. If the Hologres instance is of a version earlier than Hologres V2.0, Flink uses the SDK mode that you configure. In Hologres V2.0 or later, the RPC mode is no longer supported. If you set this parameter to rpc, Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to jdbc fixed. If you set _ this parameter to a value other than rpc, Flink uses the SDK mode that you configure. VVR 8.0.3 and a later 8.X version: We recommend that you set this parameter to jdbc. For Realtime Compute for Apache Flink that uses VVR 8.0.3 or later, the RPC mode is no longer supported for tables regardless of the versions |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | of Hologres instances. If the RPC mode is used for tables, Realtime Compute for Apache Flink automatically changes the SDK mode from RPC to jdbc fixed. _ |   |

| useRp cMode | Speci fies whet her to conn ect to the Holog res conn ector by using RPC. | Bool ean | No | false | Valid values: true: RPC is used to connect to the Hologres connector. The effect of this setting is equivalent to the effect when you set the sdkMode parameter to rpc. If RPC is used, the number of SQL connections is reduced. false: A JDBC driver is used to connect to the Hologres connector. This is the default value. JDBC drivers require SQL connections. This increases the number of JDBC connections. Note The RPC mode is no longer supported in Hologres V2.0. We recommend that you set the sdkMode parameter to jdbc or jdbc fixed. _ Realtime Compute for Apache Flink that uses VVR 6.0.7 or VVR 8.0.1 automatically changes the SDK mode from RPC to jdbc fixed for a table when it _ detects that the version of Hologres is V2.0 or later. Realtime Compute for Apache Flink that uses VVR 8.0.3 or later automatically changes the SDK mode from RPC to jdbc fixed. _ |
|---|---|---|---|---|---|
| conne ctionS ize | The size of the JDBC conn ectio n pool that is creat ed in a Realti me Com pute for Apac he Flink deplo ymen t. | Integ er | No | 3 | If the deployment provides poor performance, we recommend that you increase the size of the connection pool. The size of the JDBC connection pool is proportional to data throughput. |

| conne ctionP oolNa me | The name of the conn ectio n pool. In the same Task Mana ger, table s for whic h the same conn ectio n pool is confi gure d can share the conn ectio n pool. | Strin g | No | None | Set the value to a string other than default . If the same connection pool is configured for multiple tables, the value of the connectionSize parameter for the tables must be the same. You can specify this parameter based on your business requirements. For example, a deployment uses the following Hologres tables: Dimension Table A, Dimension Table B, Sink Table C, Sink Table D, and Sink Table E. You can configure the connection pool pool1 for Dimension Table A and Dimension Table B, and the connection pool pool2 for Sink Table C and Sink Table D. You can configure the connection pool pool3 for Sink Table E in which a large number of data is processed. Note VVR 4.0.12 to VVR 8.0.3: By default, tables do not share a connection pool. Each table uses its connection pool. VVR 8.0.4 or later: By default, tables that use the same endpoint in the same deployment share a connection pool. If the number of tables in a deployment is excessively large, the connections in a connection pool may be relatively insufficient. This affects the deployment performance. In this case, we recommend that you set the connectionPoolName parameter to different values for different tables. |
|---|---|---|---|---|---|

| jdbcR eadBa tchSiz e | The maxi mum numb er of data recor ds that can be proce ssed at the same time for a point query in a Holog res dime nsion table. | Integ er | No | 128 | None. |
|---|---|---|---|---|---|
| jdbcR eadBa tchQu eueSiz e | The maxi mum numb er of queu ed requ ests allow ed in a threa d to perfo rm a point query in a Holog res dime nsion table. | Integ er | No | 256 | None. |

| jdbcR eadTi meout Ms | The timeo ut perio d for perfo rmin g a point query in a Holog res dime nsion table. | Long | No | 0 | The default value 0 specifies that the point query in a Hologres dimension table never times out. Only Realtime Compute for Apache Flink whose engine version is vvr- 4.0.15-flink-1.13, vvr-6.0.2-flink-1.15, or their later minor versions supports this parameter. |
|---|---|---|---|---|---|
| jdbcR eadRe tryCo unt | The numb er of retrie s when a point query perfo rmed in a Holog res dime nsion table times out. | Inter ger | No | VVR version earlier than 8.0.5: 1 VVR 8.0.5 or later: 10 | Only Realtime Compute for Apache Flink that uses VVR 6.0.3 or later supports this parameter. This parameter is different from the jdbcRetryCount parameter. The jdbcRetryCount parameter specifies the maximum number of retries allowed to read and write data if a connection failure occurs. |

| jdbcSc anFet chSize | The numb er of data recor ds that can be proce ssed at the same time by callin g the scan opera tion when you perfo rm a one- to- many table join. In a one- to- many table join, no comp lete prim ary key is used. | Integ er | No | 256 | None. |
|---|---|---|---|---|---|
| jdbcSc anTim eoutS econd s | The maxi mum time perio d for whic h you need to wait for a scan opera tion to comp lete. | Integ er | No | 60 | Unit: seconds. |

| cache | The cach e polic y. | Strin g | No | None | Hologres supports only None and LRU cache policy. |
|---|---|---|---|---|---|
| cache Size | The maxi mum numb er of rows of data recor ds that can be cach ed. | Integ er | No | 10000 | If you set the cache parameter to LRU, you can configure the cacheSize parameter. Unit: row. |
| cache TTLMs | The inter val at whic h the syste m refre shes the cach e. | Long | No | For more information, see the Remarks column. | Unit: milliseconds. The default value of the cacheTTLMs parameter varies based on the value of the cache parameter: If you set the cache parameter to LRU, the cacheTTLMs parameter specifies the timeout period of the cache. By default, cache entries do not expire. If you set the cache parameter to None, the cacheTTLMs parameter can be left empty. This indicates that cache entries do not expire. |
| cache Empty | Speci fies whet her to cach e the JOIN queri es whos e retur n result s are empt y. | Bool ean | No | true | true: The JOIN queries whose return value is empty are cached. This is the default value. false: The JOIN queries whose return value is empty are not cached. |

| async | Speci fies whet her to enabl e data sync hroni zatio n in asyn chron ous mode . | Bool ean | No | false | true: enables data synchronization in asynchronous mode. false: disables data synchronization in asynchronous mode. This is the default value. Note Data is not sorted when data is synchronized in asynchronous mode. |
|---|---|---|---|---|---|

**Sample code**

**Sample code for a source table**

**Statement for creating a Hologres source table in which the**

**binary logging feature is disabled**

```
CREATE TEMPORARY TABLE hologres_source (
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
  'field_delimiter'='|' -- This parameter is optional.
  'sdkmode' = 'jdbc'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT name, age, birthday from hologres_source;
```

**Statement for creating a Hologres source table in which the**

**binary logging feature is enabled**

Realtime Compute for Apache Flink can consume the binary log data of Hologres in real time.

**Sample code for a sink table**

```
CREATE TEMPORARY TABLE datagen_source(
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='datagen'
```

);

```
CREATE TEMPORARY TABLE hologres_sink (
  name varchar,
  age BIGINT,
  birthday BIGINT
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>'
```

);

```
INSERT INTO hologres_sink SELECT * from datagen_source;
```

**Sample code for a dimension table**

```
CREATE TEMPORARY TABLE datagen_source (
  a INT,
  b BIGINT,
  c STRING,
  proctime AS PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE hologres_dim (
  a INT,
  b VARCHAR,
  c VARCHAR
) WITH (
  'connector' = 'hologres',
   ...
```

);

```
CREATE TEMPORARY TABLE blackhole_sink (
  a INT,
  b STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.a,H.b FROM datagen_source AS T JOIN hologres_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

**Feature description**

**Streaming semantics**

Stream processing, which is also known as streaming data or streaming event processing, refers to the continuous processing of a series of unbounded data or events. In most cases, the system that processes streaming data or events allows you to specify a reliability pattern or processing semantics to ensure data accuracy. This prevents data loss caused by network or device failures. Semantics can be classified into the following types based on the configurations of the Hologres streaming sink that you use and the attributes of the Hologres table: Exactly-once: The system processes data or events only once even if multiple failures occur. At-least-once: If the streaming data or events that you want to process are lost, the system transfers the data again from the transmission source. The system may process streaming data or events multiple times. If the first retry is successful, no subsequent retries are required. When you use streaming semantics in a Hologres sink table, take note of the following items: If no primary keys are configured in the Hologres physical table, the Hologres streaming sink uses the at-least-once semantics. If primary keys are configured in the Hologres physical table, the Hologres streaming sink uses the exactly-once semantics based on the primary keys. If multiple records with the same primary key are written to the table, you must specify the **mutatetype** parameter to determine how the sink table is updated. Valid values of the **mutatetype** parameter:
**insertorignore**: retains the first record and discards the subsequent records. This is the
default value.
**insertorreplace**: replaces the existing record in an entire row with the one that arrives
later.
**insertorupdate**: updates specific columns of the existing data. For example, a table has
fields a, b, c, and d. The a field is the primary key. Only data in the a and b fields are written to Hologres. If duplicate primary keys exist, the system updates only data in the b field. Data in the c and d fields remains unchanged.

> **Note:** If the **mutatetype** parameter is set to `insertorreplace` or `insertorupdate` , the system updates data based on the primary key.
> The number of columns in the sink table that is defined by Realtime Compute for Apache Flink can be different from the number of columns in the Hologres physical table. Make sure that the null value can be used to pad the missing columns. If the null value cannot be used to pad the missing columns, an error is returned.

By default, the Hologres streaming sink node can import data to only one non-partitioned table. If the sink node imports data to the parent table of a partitioned table, data queries fail even if the data import is successful. To enable data to be automatically written to a partitioned table, you can set the **partitionRouter** parameter to true. Take note of the following items: You must set the **tablename** parameter to the name of the parent table. If no partitioned table is created, you must specify **createparttable=true** in the WITH clause to enable the automatic creation of a partitioned table. If you do not perform the preceding configuration, data import fails.

**Data merging into a wide table**

If you want to write data from multiple streaming deployments to a Hologres wide table, you can merge the data into a wide table. In this example, two methods are used to merge data into a wide table.

> **Note:** Take note of the following limits:
> The wide table must have a primary key.
> The data of each stream must contain all fields in the primary key.
> If the wide table is a column-oriented table and the requests per second (RPS) value is large, the CPU utilization increases. We recommend that you disable dictionary encoding for the fields in the table.

**Method 1 (recommended)**

> **Note:** You can use this method to merge data into a wide table only in Realtime Compute for Apache Flink that uses VVR 6.0.7 or later.

For example, one Realtime Compute for Apache Flink data stream contains fields a, b, and c, and the other Realtime Compute for Apache Flink data stream contains fields a, d, and e. The Hologres wide table WIDE_TABLE contains fields a, b, c, d, and e, among which field a is the primary key. To merge data into a wide table, perform the following operations:
1. Execute Flink SQL statements to create a Hologres sink table. Declare fields a, b, c, d, and e
in the Flink SQL statements. Map the Hologres sink table to the Hologres wide table WIDE_TABLE.
2. Parameter settings of the Hologres sink table:
Set mutatetype to insertorupdate. This indicates that data is updated based on the primary key. Set ignoredelete to true. This prevents retraction messages from generating Delete requests.
3. Insert data from the two Flink data streams into the two sink tables.

```
// In this example, the data sources are source1 and source2. CREATE TEMPORARY TABLE hologres_sink ( -- Declare fields a, b, c, d, and e.
  a BIGINT,
  b STRING,
  c STRING,
  d STRING,
  e STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>', -- Specify the Hologres wide table. The table co
ntains fields a, b, c, d, and e.
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
  'mutatetype'='insertorupdate',    -- Update data based on the primary key.
  'ignoredelete'='true',            -- Ignore Delete requests.
  'partial-insert.enabled'='true' -- Set the partial-insert.enabled parameter to true
to update only the fields that are declared in the INSERT statement.
```

);

```
BEGIN STATEMENT SET; INSERT INTO hologres_sink(a,b,c) select * from source1; -- Declare that only fields a , b, and c are inserted into the wide table. INSERT INTO hologres_sink(a,d,e) select * from source2; -- Declare that only fields a , d, and e are inserted into the wide table. END;
```

**Method 2**

> **Note:** You can use this method to merge data into a wide table only in Realtime Compute for Apache Flink that uses VVR 6.0.6 or earlier.

For example, one Realtime Compute for Apache Flink data stream contains fields a, b, and c, and the other Realtime Compute for Apache Flink data stream contains fields a, d, and e. The Hologres wide table WIDE_TABLE contains fields a, b, c, d, and e, among which field a is the primary key. To merge data into a wide table, perform the following operations:
1. Execute Flink SQL statements to create two Hologres sink tables. One table is used to
declare fields a, b, and c, and the other is used to declare fields a, d, and e. Map the two sink tables to the Hologres wide table named WIDE_TABLE.
2. Parameter settings of the two Hologres sink tables:
Set mutatetype to insertorupdate. This indicates that data is updated based on the primary key. Set ignoredelete to true. This prevents retraction messages from generating Delete requests.
3. Insert data from the two Flink data streams into the two sink tables.

```
// In this example, the data sources are source1 and source2. CREATE TEMPORARY TABLE hologres_sink_1 ( -- Declare only fields a, b, and c.
  a BIGINT,
  b STRING,
  c STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>', -- Specify the Hologres wide table. The table co
ntains fields a, b, c, d, and e.
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
  'mutatetype' = 'insertorupdate', -- Update data based on the primary key.
  'ignoredelete' = 'true'             -- Ignore Delete requests.
```

);

```
CREATE TEMPORARY TABLE hologres_sink_2 ( -- Declare only the fields a, d, and e.
  a BIGINT,
  d STRING,
  e STRING,
  primary key(a) not enforced
) WITH (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourWideTablename>', -- Specify the Hologres wide table. The table co
ntains fields a, b, c, d, and e.
  'username' = '${secret_values.ak_id}',
  'password' = '${secret_values.ak_secret}',
  'endpoint'='<yourEndpoint>',
  'mutatetype'='insertorupdate',    -- Update data based on the primary key.
  'ignoredelete'='true'             -- Ignore Delete requests.
```

);

```
BEGIN STATEMENT SET; INSERT INTO hologres_sink_1 select * from source1; INSERT INTO hologres_sink_2 select * from source2; END;
```

**Data synchronization based on the CREATE TABLE AS and**

**CREATE DATABASE AS statements**

You can execute the CREATE TABLE AS or CREATE DATABASE AS statements to synchronize data from a single table or an entire database in real time. The changes to the schema of the source table can also be synchronized to the related Hologres table in real time during database or table synchronization. If the schema of the source table is changed, Realtime Compute for Apache Flink synchronizes the changes to the table schema to the related Hologres table and then writes data to the Hologres table. The preceding steps are automatically performed by Realtime Compute for Apache Flink. You do not need to manage the details.

**DataStream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink. You can use the Hologres DataStream connectors of different versions stored in the Maven central repository. For Realtime Compute for Apache Flink that uses VVR 6.0.7, use the dependency of 1.15-vvr-6.0.7-1.

**Build a class to read data from a Hologres source table**

VVR provides the HologresBulkreadInputFormat class that implements the RichInputFormat interface to read data from a Hologres source table. The following examples show how to build the HologresBulkreadInputFormat class to read data from a Hologres source table.

**VVR 6.0.7**

```
// set up the Java DataStream API final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); // Initialize the schema of the sink table to which you want to write data. You can def ine fields in the schema for each column or some columns of the Hologres table based on your business requirements. TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .build();
// Configure Hologres-related parameters. Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName"); // Build JDBC options. JDBCOptions jdbcOptions = JDBCUtils.getJDBCOptions(config); HologresBulkreadInputFormat inputFormat = new HologresBulkreadInputFormat(new HologresC onnectionParam(config), jdbcOptions, schema, "", -1); TypeInformation<RowData> typeInfo = InternalTypeInfo.of(schema.toRowDataType().getLogicalType()); env.addSource(new InputFormatSourceFunction<>(inputFormat, typeInfo)).returns(typeInfo)
  .print();
env.execute();
```

**Build a class to read data from a Hologres source table for**

**which binary logging is enabled**

VVR provides the HologresBinlogSource class of the Source interface to read data from a Hologres source table for which binary logging is enabled. The following examples show how to build the HologresBinlogSource class to read data from a Hologres source table for which binary logging is enabled.

**VVR 6.0.7**

```
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); // Initialize the schema of the sink table to which you want to write data. You can def ine fields in the schema for each column or some columns of the Hologres table based on your business requirements. TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .build();
// Configure Hologres-related parameters. Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName"); config.setString(HologresConfigs.SDK_MODE, "jdbc"); config.setBoolean(HologresBinlogConfigs.OPTIONAL_BINLOG, true); config.setBoolean(HologresBinlogConfigs.BINLOG_CDC_MODE, true); // Build JDBC options. JDBCOptions jdbcOptions = JDBCUtils.getJDBCOptions(config); // Create a slot and configure the default name of the slot. config.setString(HologresBinlogConfigs.JDBC_BINLOG_SLOT_NAME, HoloBinlogUtil.getOrCreateDefaultSlotForJDBCBinlog(jdbcOptions)); boolean cdcMode = config.get(HologresBinlogConfigs.BINLOG_CDC_MODE)
  && config.get(HologresBinlogConfigs.OPTIONAL_BINLOG);
// Build the record converter to read data from the Hologres source table for which bin ary logging is enabled. JDBCBinlogRecordConverter recordConverter = new JDBCBinlogRecordConverter(
  jdbcOptions.getTable(),
  schema,
  new HologresConnectionParam(config),
  cdcMode,
  Collections.emptySet());
// Build HologresBinlogSource to read data from the Hologres source table for which bin ary logging is enabled. long startTimeMs = 0; HologresJDBCBinlogSource source = new HologresJDBCBinlogSource(
  new HologresConnectionParam(config),
  schema,
  config,
  jdbcOptions,
  startTimeMs,
  StartupMode.TIMESTAMP,
  recordConverter,
  "",
  -1);
env.fromSource(source, WatermarkStrategy.noWatermarks(), "Test source").print(); env.execute();
```

> **Note:** The buildRecordConverter method is not included in the dependency of the VVR connector. This method is provided in ververica-connector-demo.

**Build a class to write data to a Hologres sink table**

VVR provides the HologresSinkFunction class of the OutputFormatSinkFunction interface to write data to a Hologres sink table. The following examples show how to build the OutputFormatSinkFunction class to write data to a Hologres sink table.

**VVR 6.0.7&VVR 8.0.1**

```
// set up the Java DataStream API final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment(); // Initialize the schema of the sink table to which you want to write data. You can def ine fields in the schema for each column or some columns of the Hologres table based on your business requirements. TableSchema schema = TableSchema.builder()
  .field("a", DataTypes.INT())
  .field("b", DataTypes.STRING())
  .build();
// Configure Hologres-related parameters. Configuration config = new Configuration(); config.setString(HologresConfigs.ENDPOINT, "yourEndpoint"); config.setString(HologresConfigs.USERNAME, "yourUserName"); config.setString(HologresConfigs.PASSWORD, "yourPassword"); config.setString(HologresConfigs.DATABASE, "yourDatabaseName"); config.setString(HologresConfigs.TABLE, "yourTableName"); config.setString(HologresConfigs.SDK_MODE, "jdbc"); HologresConnectionParam hologresConnectionParam = new HologresConnectionParam(config); // Build a Hologres Writer to write data in the data structure of the RowData class. AbstractHologresWriter<RowData> hologresWriter = HologresJDBCWriter.createRowDataWriter(
  hologresConnectionParam, schema, HologresTableSchema.get(hologresConnectionParam), ne
w Integer[0]); // Build HologresSinkFunction to write data to the Hologres sink table. HologresSinkFunction sinkFunction = new HologresSinkFunction(hologresConnectionParam, h ologresWriter); TypeInformation<RowData> typeInfo = InternalTypeInfo.of(schema.toRowDataType().getLogicalType()); int offset = (int) (System.currentTimeMillis() % Integer.MAX_VALUE); env.fromElements((RowData)GenericRowData.of(2 + offset, StringData.fromString("2")), Ge nericRowData.of(3 + offset, StringData.fromString("3"))).returns(typeInfo)
  .addSink(sinkFunction);
env.execute();
```

> **Note:** The buildHologresWriter method is not included in the dependency of the VVR connector. This method is provided in ververica-connector-demo.

**Time zones of Realtime Compute for Apache Flink and Hologres**

**Time types**

| Servic e | Time type | Description |
|---|---|---|
| Flink | Flink TIMESTA MP | The date and time without the time zone. Data of the TIMESTAMP type is a timestamp that represents the year, month, day, hour, minute, second, and fractional second. Data of the TIMESTAMP type can be a string, such as 1970-01-01 00:00:04.001 . |
|   | Flink TIMESTA MP LTZ _ | An absolute point in time on the timeline. Data of the LONG type indicates the number of milliseconds that have elapsed since the epoch time. Data of the INT type indicates the number of nanoseconds in milliseconds. The epoch time refers to 00:00:00 UTC on January 1, 1970 in Java. Data of the TIMESTAMP LTZ type is interpreted for calculations _ and visualization based on the time zone that is configured in the current session. The TIMESTAMP LTZ type can be used for calculations _ across time zones. A value of the TIMESTAMP LTZ type represents the _ same absolute point in time in different time zones based on the epoch time. A value of the TIMESTAMP LTZ type may indicate different local values _ of the TIMESTAMP type in different time zones. For example, if a value of the TIMESTAMP LTZ type is 2024-03-19T04:00:00Z , the local _ timestamp in the time zone of Shanghai (UTC+8) is expressed as 2024-03-19T12:00:00 , and the local timestamp in the time zone of Greenwich (UTC+0) is expressed as 2024-03-19T04:00:00 . |
| Hologre s | TIMESTAMP | The date and time without the time zone, which is similar to the TIMESTAMP type of Realtime Compute for Apache Flink. Data of the TIMESTAMP type in Hologres does not change even if the time zone of the Hologres client changes. For example, data of the TIMESTAMP type can be expressed as 2022-01-01 01:01:01.123456 . |
|   | TIMESTAMP WITH TIME ZONE (TIMESTAMPTZ ) | The date and time with the time zone, which is similar to the TIMESTAMP LTZ type of Realtime Compute for Apache Flink. When _ Hologres stores TIMESTAMPTZ data, Hologres converts the data into the values of the time zone in UTC. When you query data, Hologres converts the values of the time zone in UTC into the values of the time zone on the client based on the time zone parameters of the client. For example, if the timestamp of the time zone of Beijing (UTC+8) is 2022-02-01 10:33:20.125+08 and the timestamp is stored as the TIMESTAMPTZ type in Hologres, the timestamp is expressed as 2022- 02-01 10:33:20.125+08 . |

|   | 02-01 10:33:20.125+08 |
|---|---|

**Read data from or write data to Hologres**

If you set the `type-mapping.timestamp-converting.legacy` parameter to false in Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, you can perform conversions of all Hologres instances.

| Flink |   | Hologres | Description |   |
|---|---|---|---|---|
| TIMESTAMP |   | TIMESTAMP | Time type conversions are performed without time zone conversions. We recommend that you use this type of time type conversion to read data from or write data to Hologres. |   |
| TIMESTAMP L TZ |   | TIMESTAMP TZ |   |   |
| TIMESTAMP |   | TIMESTAMP TZ | Time type conversions are performed with time zone conversions. To maintain accuracy in the conversion, you need to set the Flink time zone by configuration items the parameter table.local-time-zone . For example, you configure 'table.local-time-zone': 'Asia/Shanghai' to set the time zone of Realtime Compute for Apache Flink to the time zone of Shanghai (UTC+8). After you write the data 2022-01-01 01:01:01.123456 of the TIMESTAMP type from Realtime Compute for Apache Flink to Hologres, the data is converted to 2022-01-01 01:01:01.123456+8 of the TIMESTAMPTZ type. |   |
| TIMESTAMP L TZ |   |   |   |   |
|   | STAMP L |   | 'Asia/Shanghai' |   |
|   |   | TIMESTAMP |   |   |

In Realtime Compute for Apache Flink that uses VVR of a version earlier than 8.0.5, or if you set the `type-mapping.timestamp-converting.legacy` parameter to false in Realtime Compute for Apache Flink that uses VVR 8.0.6 or later, data deviation may occur during time type conversions except for the conversions of the TIMESTAMP type.

| Flink | Hologres | Description |
|---|---|---|
| TIMESTAMP | TIMESTAMP | Time type conversions are performed without time zone conversions. We recommend that you use this type of time type conversion to read data from or write data to Hologres. |
| TIMESTAMP L TZ | TIMESTAMP TZ | Data of the TIMESTAMP LTZ and TIMESTAMPTZ types is expressed as the time without the time zone when Realtime Compute for Apache Flink reads data from or writes data to Hologres. This may cause data deviation. For example, if data of the TIMESTAMP LTZ type in Realtime Compute for Apache Flink is 2024-03-19T04:00:00Z, the time without the time zone in Shanghai (UTC+8) is 2024-03- 19T12:00:00. However, when data is written to Hologres, 2024- 03-19T04:00:00 is used as the time without the time zone and is converted to 2024-03-19T04:00:00+08 of the TIMESTAMPTZ type in Hologres. This causes an 8-hour data deviation. |

| TIMESTAMP | TIMESTAMP TZ | Time zone conversions are performed based on the time zone of JVM in the runtime environment instead of the time zone of Realtime Compute for Apache Flink. This is different from the time zone conversions in Realtime Compute for Apache Flink. If the time zone of Realtime Compute for Apache Flink is different from the time zone of JVM, data deviation may occur. We recommend that you read data from and write data to Hologres based on the time zone of Realtime Compute for Apache Flink. |
|---|---|---|
| TIMESTAMP L TZ | TIMESTAMP |   |

### 5.31 MySQL connector

This topic describes how to use the MySQL connector.

**Background information**

The MySQL connector supports all databases that are compatible with the MySQL protocol. The databases include ApsaraDB RDS for MySQL, PolarDB for MySQL, and self-managed MySQL databases. The following table describes the capabilities supported by the MySQL connector.

| Item | Description |
|---|---|
| Table types | Source table, dimension table, and sink table |
| Running modes | Streaming mode |
| Data formats | None |
| Monitoring metrics | Source table: currentFetchEventTimeLag: the interval from the time when data is generated to the time when the data is pulled to the source operator. The value of this metric is greater than 0 only in the binary log data reading phase. The value of this metric is fixed to 0 in the savepoint reading phase. currentEmitEventTimeLag: the interval from the time when data is generated to the time when the data leaves the source operator. The value of this metric is greater than 0 only in the binary log data reading phase. The value of this metric is fixed to 0 in the savepoint reading phase. sourceIdleTime: the period of time for which no new data is generated in the source table. Dimension tables and sink tables: none. |
| API types | DataStream API and SQL API |

| Data updates or deletion in a sink table | Yes |
|---|---|

**Features**

A MySQL Change Data Capture (CDC) source table is a streaming source table of MySQL databases. The MySQL CDC source connector reads full historical data from a MySQL database and then reads binary log data. This way, data accuracy is ensured. If an error occurs, the exactly-once semantics can be used to ensure data accuracy. The MySQL CDC source connector supports full data reading in multiple subtasks at the same time. You can use the incremental savepoint algorithm to perform lock-free reading and resumable uploads. The MySQL CDC source connector supports the following features: Integrates stream processing and batch processing to support full and incremental data reading. This way, you do not need to separately implement stream processing and batch processing. Supports full data reading in multiple subtasks at the same time. This way, data can be read in a more efficient manner. Seamlessly switches between full and incremental data reading and supports automatic scale-in operations. This reduces the computing resources that are consumed. Supports resumable uploads during full data reading. This way, data can be uploaded in a more stable manner. Reads full data without locks. This way, online business is not affected. Supports the reading of backup logs from ApsaraDB RDS for MySQL. Parses binary log files in parallel to reduce the read latency.

**Prerequisites**

CDC source table Before you use a MySQL CDC source table, you must perform operations that are described in the Configure a MySQL database topic to meet the following prerequisites for using a MySQL CDC source table: A network connection is established between your MySQL database and Ververica Platform (VVP). The MySQL server configuration meets the following requirements: The MySQL version is V5.6, V5.7, or V8.0.X. Binary logging is enabled. The format of binary logs is set to ROW. The binlog_row_image parameter is set to FULL. The interactive_timeout and wait_timeout parameters are configured in the MySQL configuration file. A MySQL user is created and granted the SELECT, SHOW DATABASES, REPLICATION SLAVE, and REPLICATION CLIENT permissions. Dimension table and sink table A MySQL database and a table are created. An IP address whitelist is configured.

**Limits**

CDC source table You must select a VVR version based on the MySQL version. The following table describes the mappings between VVR and MySQL versions. You can run the select version() command to query the MySQL version.

| VVR version | Supported MySQL version |
|---|---|
| VVR 4.0.11 and later | 5.6.x |
|   | 5.7.x |
|   | 8.0.x |

> **Important:** The default value of the scan.incremental.snapshot.enabled parameter is true. This indicates that the incremental savepoint feature is enabled by default. This ensures that ApsaraDB RDS for MySQL 5.6.X runs as expected. You cannot disable the incremental savepoint feature for ApsaraDB RDS for MySQL 5.6.X. This limit is removed from ApsaraDB RDS for MySQL 6.0.8 and ApsaraDB RDS for MySQL 8.0.1. Therefore, you can disable the incremental savepoint feature for ApsaraDB RDS for MySQL 6.0.8 and ApsaraDB RDS for MySQL 8.0.1. We recommend that you do not disable the incremental savepoint feature. If you disable this feature, the MySQL database is locked and the online business processing performance may be affected.

MySQL CDC source tables do not support watermarks. Only MySQL users who are granted specific permissions can use the MySQL CDC source connector to read full data and incremental data from a MySQL database. The permissions include SELECT, SHOW DATABASES, REPLICATION SLAVE, and REPLICATION CLIENT. If you use the CREATE TABLE AS statement together with the CREATE DATABASE AS statement to perform data synchronization, specific schema changes of the MySQL CDC source table can be synchronized to the sink table. In other scenarios, the schema changes of the MySQL CDC source table cannot be synchronized to the sink table. MySQL CDC source tables do not support the synchronization of truncate operations. We recommend that you do not read data from a secondary instance or a read-only secondary instance of ApsaraDB RDS for MySQL. By default, the binary log retention period of the secondary instance or read-only secondary instance of ApsaraDB RDS for MySQL is short. If the binary log file is deleted due to expiration, the deployment cannot consume the binary log data and an error occurs. Data of Multi-master Cluster (Database/Table) Edition of PolarDB for MySQL of 1.0.19 or earlier cannot be read for the MySQL CDC source table. Duplicate table IDs may be generated in binary log data of Multi-master Cluster (Database/Table) Edition of PolarDB for MySQL of 1.0.19 or earlier. This leads to incorrect mapping of the schema of the MySQL CDC source table. As a result, an error occurs when the binary log data is parsed. This issue is resolved in PolarDB for MySQL of a version later than 1.0.19. Dimension table and sink table The at-least-once semantics can be used. If an ApsaraDB RDS for MySQL sink table contains a primary key, idempotence can be used to ensure data correctness.

**Precautions**

CDC source table You must specify a unique server ID for each MySQL CDC data source. Use of server IDs Each client that synchronizes data from a database has a unique server ID. The MySQL server maintains network connections and binary log file positions based on the server ID. If a large number of clients that have different server IDs connect to the MySQL server, the CPU utilization of the MySQL server may significantly increase. This affects the stability of online business. If multiple MySQL CDC data sources use the same server ID and the data sources cannot be merged as one source operator, the checkpoints for binary log positions may be out of order. As a result, the amount of data that is read may be greater than or less than expected. A conflict between server IDs may also occur. To prevent the preceding issue, we recommend that you specify a unique server ID for each MySQL CDC data source. Configuration methods of server IDs You can specify server IDs in DDL statements or by using dynamic hints. We recommend that you use dynamic hints to configure server IDs instead of configuring server IDs in DDL statements. Configuration of server IDs in different scenarios Scenario 1: Incremental snapshot is disabled or the parallelism is 1. Specify a unique server ID:

```
SELECT * FROM source_table /*+ OPTIONS('server-id'='123456') */ ;
```

Scenario 2: Incremental snapshot is enabled, and the parallelism is greater than 1. Specify a server ID range. Make sure that the number of available server IDs in the range is not less than the degree of parallelism. For example, when the parallelism is 3, execute the following statement to set a server ID range:

```
SELECT * FROM source_table /*+ OPTIONS('server-id'='123456-123458') */ ;
```

Scenario 3: The CREATE TABLE AS statement is used to synchronize data. If you execute the CREATE TABLE AS statement to synchronize data, and the configurations of multiple MySQL CDC data sources are the same, the data sources are automatically merged as one source operator. In this case, you can specify the same server ID for multiple MySQL CDC data sources. Scenario 4: A job contains multiple MySQL CDC source tables, and the CREATE TABLE AS statement is not used for data synchronization. If multiple MySQL CDC source tables are used in a deployment and the CREATE TABLE AS statement is not executed, the data sources cannot be merged as one source operator. You must specify a unique server ID for each MySQL CDC source table. Similarly, if the incremental savepoint algorithm is enabled and the parallelism is greater than 1, you must specify the server ID range.

```
select * from
  source_table1 /*+ OPTIONS('server-id'='123456-123457') */
left join
  source_table2 /*+ OPTIONS('server-id'='123458-123459') */
on source_table1.id=source_table2.id;
```

Only deployments that use VVR 4.0.8 or later support lock-free reading, parallel reading, and resumable uploads during full data reading. If your deployment uses a VVR version that is earlier than 4.0.8, you must grant the RELOAD permission to the MySQL user to obtain the global read lock. This ensures data reading consistency. The global read lock may block write operations for a few seconds. This may affect online business. If your deployment uses a VVR version that is earlier than 4.0.8, checkpoints cannot be generated during full data reading. If your deployment fails in the process, the deployment reads full data again. This reduces the stability of data reading performance. Therefore, we recommend that you update the version of VVR that is used by your deployment to 4.0.8 or later. Sink table ApsaraDB RDS for MySQL supports the auto-increment primary key. Therefore, you do not need to declare the auto-increment field in the DDL statement. For example, if you use ID as an auto-increment field, you do not need to declare the ID field in the DDL statement. When a row of output data is written to the ApsaraDB RDS for MySQL database, a value is automatically filled for the auto-increment field. You must declare at least one non-primary key in the DDL statement. Otherwise, an error is returned. NOT ENFORCED indicates that Flink does not perform mandatory verification on the primary key. You must ensure the correctness and integrity of the primary key. Flink does not fully support mandatory verification. Flink considers that the primary key is correct based on the assumption that the nullability of columns is aligned with the columns in the primary key. Dimension table If you want to perform queries by index when the MySQL connector is used for a dimension table, you must follow the leftmost prefix matching principle of MySQL to sort the columns that are specified in the JOIN operation. However, this cannot ensure that indexes are used for queries. Specific filter conditions may be rewritten or modified due to SQL optimization. As a result, the filter conditions that are obtained by the connector may not hit indexes. To determine whether the connector queries data by index, check the specific SELECT statements that are executed on the related database.

**Syntax**

```
CREATE TABLE mysqlcdc_source (
   order_id INT,
   order_date TIMESTAMP(0),
   customer_name STRING,
   price DECIMAL(10, 5),
   product_id INT,
   order_status BOOLEAN,
   PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
```

);

| Note When the connector writes data to a sink table, the connector concatenates each received data record into an SQL statement and executes the SQL statement based on the following rules: The following SQL statements are executed: If the sink table does not have a primary key, the INSERT INTO table name _ (column1, column2, ...) VALUES (value1, value2, ...); statement is executed. If the sink table has a primary key, the INSERT INTO table name (column1, _ |   |
|---|---|
|   | INSERT INTO table name (column1, _ |
| column2, ...) VALUES (value1, value2, ...) ON DUPLICATE KEY UPDATE |   |
| column1 = VALUES(column1), column2 = VALUES(column2), ...; |   |

|   |   | INSERT INTO table name _ |
|---|---|---|
|   | (column1, column2, ...) VALUES (value1, value2, ...); |   |

> executed. If a unique index constraint other than a primary key constraint exists in a physical table and two records that have different primary keys but the same unique index are inserted into the physical table, downstream data is overwritten due to an index conflict, which causes data loss.
> If an auto-increment primary key is defined in the MySQL database, the auto- increment field cannot be declared in Flink DDL statements. During data writing, the database automatically configures the auto-increment field. The connector can be used to only write and delete data that has auto-increment fields and cannot be used to update such data.

**Parameters in the WITH clause**

Common parameters

| Parame ter | Description | Requir ed | Data type | Default value | Remarks |
|---|---|---|---|---|---|
| connect or | The type of tables. | Yes | STRING | None | When you use the MySQL connector for a source table, you can set this parameter to mysql-cdc or mysql . The two values are equivalent. When you use the MySQL connector for a dimension table or a sink table, you must set this parameter to mysql . |

| hostnam e | The IP address or hostname that is used to access your ApsaraDB RDS for MySQL database. | Yes | STRING | None | Contact Apsara Stack O&M engineers to obtain the required information. |
|---|---|---|---|---|---|
| usernam e | The username that is used to access the ApsaraDB RDS for MySQL database. | Yes | STRING | None | None. |
| passwor d | The password that is used to access the ApsaraDB RDS for MySQL database. | Yes | STRING | None | None. |

| databas e-name | The name of the MySQL database that you want to access. | Yes | STRING | None | You can set this parameter to a regular expression to read data from multiple databases. When you use a regular expression, we recommend that you do not use the caret symbol (^) and dollar sign ($) to match the beginning and end of the regular expression. For more information about the reason, see the Remarks column of the table-name parameter. |
|---|---|---|---|---|---|
|   |   |   |   |   | If you want to read data from multiple tables, you can set this parameter to a regular expression. When you use the MySQL connector to read data from multiple MySQL tables, you can commit multiple CREATE TABLE AS statements as one deployment to prevent multiple Binlog listeners from being enabled. This improves performance and efficiency. When you use a regular expression, we recommend that you do not use the caret symbol (^) and dollar sign ($) to match the beginning and end of the regular expression. For more information about the reason, see the following note. |

| table- name | The name of the MySQL table. | Yes | STRING | None | Note When the MySQL CDC source table matches a table name in a regular expression, the character string (\\.) is used to concatenate the values of the database-name and table-name parameters that you specify as a full-path regular expression. In Realtime Compute for Apache Flink that uses VVR 8.0.1 or earlier, a period (.) is used instead of the character string (\\.). Then, the regular expression and the fully qualified names of tables in the MySQL database are used to perform regular expression matching. |
|---|---|---|---|---|---|
|   |   |   |   |   | For example, if you specify database- name'='db . and table- _ name'='tb .+, the _ connector uses the regular expression db .*\\.tb .+ to match _ _ the fully qualified names of tables to determine the tables that need to be read. In Realtime Compute for Apache Flink whose VVR version is earlier than 8.0.1, the regular expression is db .*.tb .+. _ _ |
| port | The port that is used to access your MySQL database. | No | INTEGER | 3306 | None. |

Source table-specific parameters

| Paramet er | Descrip tion | Requ ired | Data type | Defau lt value | Remarks |
|---|---|---|---|---|---|
| server-id | The numeric ID that is allocate d to a databas e client. | No | STRIN G | By defaul t, a value in the range of 5400 to 6400 is rando mly gener ated. | The ID must be unique in a MySQL cluster. We recommend that you configure a unique server ID for each deployment in the same database. This parameter can also be set to an ID range, such as 5400-5408. If the incremental snapshot algorithm is enabled, parallel reading is supported. In this case, we recommend that you set this parameter to an ID range so that each parallel deployment uses a unique ID. |
| scan.incr emental.s napshot.e nabled | Specifie s whether to enable the increme ntal savepoi nt algorith m. | No | BOOL EAN | true | By default, the incremental savepoint algorithm is enabled. The incremental savepoint algorithm is a new mechanism that is used to read savepoints of full data. Compared with the original savepoint reading algorithm, the incremental savepoint algorithm has the following advantages: When the MySQL CDC source connector reads full data, the connector can read data in multiple subtasks at the same time. When the MySQL CDC source connector reads full data, the connector can generate checkpoints for chunks. When the MySQL CDC source connector reads full data, the connector does not need to execute the FLUSH TABLES WITH READ LOCK statement to obtain a global read lock. If you want the MySQL CDC source connector to support parallel reading, a unique server ID must be allocated to each parallel reader. Therefore, you must set the server-id parameter to a range that is greater than or equal to the value of the Parallelism parameter. For example, you can set the server-id parameter to 5400- 6400. |

| scan.incr emental.s napshot.c hunk.size | The chunk size of the table. The chunk size indicate s the number of rows. | No | INTEG ER | 8096 | If the incremental savepoint algorithm is enabled, the table is split into multiple chunks for data reading. Before data in a chunk is read, the data is cached in the memory. A smaller number of rows in a chunk indicates a larger number of chunks in the table. Therefore, if the chunk size is small, a small number of data records are read after fault recovery. This may reduce data throughput and cause an OOM error. Therefore, you must specify a reasonable chunk size based on your business requirements. |
|---|---|---|---|---|---|
| scan.snap shot.fetch .size | The maximu m number of data records that can be extracte d each time full data of a table is read. | No | INTEG ER | 1024 | None. |
|   |   |   |   |   | Valid values: initial: When the MySQL CDC source connector starts for the first time, the connector scans all historical data and reads the most recent binary log data. This is the default value. latest-offset: When the MySQL CDC source connector starts for the first time, the connector reads binary log data from the most recent offset instead of scanning all historical data. This way, the connector reads only the most recent incremental data after the connector starts. earliest-offset: The MySQL CDC source connector does not scan full historical data. The connector starts to read accessible binary log data from the earliest offset. |

| scan.start up.mode | The startup mode when data is consum | No | STRIN G | initial | specific-offset: The MySQL CDC source connector does not scan full historical data. The connector starts to scan binary log data from the specified offset. You can specify the scan.startup.specific- offset.file and scan.startup.specific- offset.pos parameters to specify the name of the binary log file and offset at which the scan starts. You can also specify the scan.startup.specific- offset.gtid-set parameter to specify a |   |   |
|---|---|---|---|---|---|---|---|
|   | ed. |   |   |   | global transaction identifier (GTID) set at which the scan starts. timestamp: The MySQL CDC source connector does not scan full historical data. The connector starts to read binary log data from the specified timestamp. The timestamp is specified by the scan.startup.timestamp-millis parameter. Unit: milliseconds. Important You can set the scan.startup.mode parameter to earliest-offset, specific- offset, or timestamp in Realtime Compute for Apache Flink that uses VVR 6.0.4 or later. If the scan.startup.mode parameter is set to earliest- offset, specific-offset, or timestamp for a deployment and the table schema at the startup time is different from the table schema at the specified start offset time, an error is reported in the deployment. If you use one of the three startup modes for a deployment, make sure that the table schema does not change between the specified binary log consumption offset time and the startup time of the deployment. |   |   |
|   |   |   |   |   |   | Important You can set the scan.startup.mode parameter to earliest-offset, specific- offset, or timestamp in Realtime Compute for Apache Flink that uses VVR 6.0.4 or later. If the scan.startup.mode parameter is set to earliest- offset, specific-offset, or timestamp for a deployment and the table schema at the startup time is different from the table schema at the specified start offset time, an error is reported in the deployment. If you use one of the three startup modes for a deployment, make sure that the table schema does not change between the specified binary log consumption offset time and the startup time of the deployment. |   |

| scan.start up.specifi c- offset.file | The name of the binary log file that is used to specify the startup offset when the scan.sta rtup.mo de paramet er is set to specific- offset. | No |   | STRIN G | None | This parameter is required when the scan.startup.mode parameter is set to specific-offset. Example of a file name: mysql-bin.000003 . |   |   |
|---|---|---|---|---|---|---|---|---|
| scan.start up.specifi c- offset.pos | The startup offset that is specifie d in the specifie d binary log file when the scan.sta rtup.mo de paramet er is set to specific- offset. | No |   | INTEG ER | None | This parameter is required when the scan.startup.mode parameter is set to specific-offset. |   |   |
| scan.start up.specifi c- offset.gti d-set | A GTID set that is used to specify the startup offset when the scan.sta rtup.mo de paramet er is set to specific- offset. | No |   | STRIN G | None | This parameter is required when the scan.startup.mode parameter is set to specific-offset. Example of a GTID: 24DA167-0C0C-11E8-8442- 00059A3C7B00:1-19 . |   |   |
|   |   |   |   |   |   |   | 24DA167-0C0C-11E8-8442- |   |

| scan.start up.timest amp- millis | The timesta mp in millisec onds that is used to specify the startup offset when the scan.sta rtup.mo de paramet er is set to timesta mp. | No | LONG | None | This parameter is required when the scan.startup.mode parameter is set to timestamp. Unit: milliseconds. Important If you set the scan.startup.mode parameter to timestamp, the MySQL CDC source connector attempts to read the initial event of each binary log file to determine the timestamp of the file and finally locates the binary log file that corresponds to the specified timestamp. Make sure that the binary log file that corresponds to the specified timestamp is not deleted from the database and can be read. |
|---|---|---|---|---|---|
| server- time-zone |   |   | STRIN G |   | Example: Asia/Shanghai. This parameter determines how to convert data in the MySQL database from the TIMESTAMP type to the STRING type. |

|   | The time zone of the session that is used by the databas e. | Requi red only in a VVR versio n that is earlie r than 6.0.2 |   | If you do not specif y this param eter, the syste m uses the time zone of the enviro nment in which the Realti me Comp ute for Apach e Flink deploy ment runs |   |
|---|---|---|---|---|---|
|   |   |   |   | as the time zone of the datab ase server . The time zone is the |   |

time zone of the zone that you select ed.

| debezium .min.row. count.to.s tream.res ults | The minimu m number of data records allowed in a table to trigger the batch data read mode. If the number of data records in a table is greater than the value of this paramet er, the batch data read mode is used. | No | INTEG ER | 1000 | Realtime Compute for Apache Flink reads data from a MySQL source table in one of the following modes: Full data read: reads all data from the table and writes the data to the memory. Data is read at a high speed, but memory space is consumed. If the source table contains a large amount of data, an OOM error may occur in this mode. Batch data read: reads data of a specific number of rows at the specified point in time until all data is read. An OOM error is prevented even if the table contains a large amount of data. However, data is read at a low speed. |
|---|---|---|---|---|---|

| connect.ti meout | The maximu m duration for which the connect or waits before the connect or makes a retry if the connecti on to the MySQL databas e server times out. | No | DURA TION | 30s | None. |
|---|---|---|---|---|---|
| connect. max- retries | The maximu m number of retries after the connecti on to the MySQL databas e server fails. | No | INTEG ER | 3 | None. |
| connectio n.pool.siz e | The size of the databas e connecti on pool. | No | INTEG ER | 20 | The database connection pool is used to reuse connections. This can reduce the number of database connections. |
| jdbc.prop erties.* | Custom JDBC URL paramet ers. | No | STRIN G | None | You can pass custom JDBC parameters. For example, if you do not want to use the SSL protocol, you can set the jdbc.properties.useSSL parameter to false. |

| debezium .* | The custom Debeziu m paramet er that is used to read binary log data. | No | STRIN G | None | You can pass custom Debezium parameters. For example, you can use 'debezium.event.deserialization.failure.han dling.mode'='ignore' to specify the logic for handling parsing errors. |
|---|---|---|---|---|---|
| heartbeat .interval | The interval at which the source moves forward the binary log file position by using heartbe at events. | No | DURA TION | 30s | Heartbeat events are used to identify the latest position of the binary log file that is read from the source. For slowly updated tables in MySQL, the binary log file position cannot automatically move forward. The source can move forward the binary log file position by using heartbeat events. This prevents the binary log file position from expiring. If the binary log file position expires, the deployment fails to run and cannot recover from the failure. If this occurs, you can only select Start without state for Start Method and specify Start Time for Reading Data to start the deployment. |
| scan.incr emental.s napshot.c hunk.key- column | Specifie s columns for shardin g in the savepoi nt phase. | For more infor matio n, see the Rema rks colum n of this para meter . | STRIN G | None | This parameter is required for a table that does not have a primary key. The selected columns must be of the NOT NULL data type. This parameter is optional for a table that has a primary key. You can select only one column from the primary key of the table for sharding. Note Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |

| rds.regio n-id | The ID of the region where an ApsaraD B RDS for MySQL instance resides. | This para meter is requir ed when you use the featur e of readi ng Objec t Stora ge Servic e (OSS) archiv ed logs. | STRIN G | None | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| rds.acces s-key-id | The AccessK ey ID of the account that is used to access ApsaraD B RDS for MySQL. | This para meter is requir ed when you use the featur e of readi ng OSS archiv ed logs. | STRIN G | None | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |

| rds.acces s-key- secret | The AccessK ey secret of the account that is used to access ApsaraD B RDS for MySQL. | This para meter is requir ed when you use the featur e of readi ng OSS archiv ed logs. | STRIN G | None | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| rds.db- instance- id | The ID of the ApsaraD B RDS for MySQL instance . | This para meter is requir ed when you use the featur e of readi ng OSS archiv ed logs. | STRIN G | None | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
| rds.main- db-id | The ID of the primary databas e of the ApsaraD B RDS for MySQL instance . | No | STRIN G | None | Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |

| rds.downl oad.time out | The timeout period for downloa ding a single archive d log from OSS. | No | DURA TION | 60s | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| scan.incr emental.c lose-idle- reader.en abled | Specifie s whether to close the idle reader after the savepoi nt is created. | No | BOOL EAN | false | Only Realtime Compute for Apache Flink that uses VVR 8.0.1 or later supports this parameter. To make the configuration of this parameter take effect, you must set the execution.checkpointing.checkpoints- after-tasks-finish.enabled parameter to true. |
| scan.read - changelo g-as- append- only.enab led | Specifie s whether to convert a changel og stream to an append- only stream. | No | BOOL EAN | false | Valid values: true: All types of messages are converted into messages of the INSERT type. The message types are INSERT, DELETE, UPDATE BEFORE, and UPDATE AFTER. _ _ Set this parameter to true for special scenarios in which the data and metadata of messages that are deleted from an upstream table need to be stored. false: All types of messages are sent without conversion. This is the default value. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |

| scan.only .deseriali ze.captur ed.tables. changelo g.enabled | Specifie s whether to deseriali ze only events in the table that you specify during increme ntal data reading. | No | BOOL EAN | false | Valid values: true: Only events in the table that you specify are deserialized. This reduces the number of change events that require deserialization and accelerates binary log reading. false: Events in all tables are deserialized. This is the default value. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| scan.para llel- deserializ e- changelo g.enabled | Specifie s whether to use multiple threads to parse change events during increme ntal data reading. | No | BOOL EAN | false | Valid values: true: Multiple threads are used to parse change events when the change events are deserialized. The order of binary log events remains unchanged. This accelerates binary log reading. false: A single thread is used to parse change events when the change events are deserialized. This is the default value. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |

Dimension table-specific parameters

| Paramet er | Descripti on | Requir ed | Data type | Defaul t value | Remarks |
|---|---|---|---|---|---|
| url | MySQL JDBC URL | No | STRING | None | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |

| lookup.m ax-retries | The maximum number of retries to read data after a data read fails. | No | INTEGE R | 3 | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
|---|---|---|---|---|---|
| lookup.ca che.strate gy | The cache policy. | No | STRING | None | Valid values: None, LRU, and ALL. Note If you set this parameter to LRU, you must also specify the lookup.cache.max-rows parameter. |
| lookup.ca che.max- rows | The maximum number of data records that can be cached. | No | INTEGE R | 100000 | You must configure this parameter if the cache parameter is set to LRU. You do not need to specify this parameter if the lookup.cache.strategy parameter is set to ALL. |
| lookup.ca che.ttl | The cache timeout period. | No | DURATI ON | 10 s | The configuration of the lookup.cache.ttl parameter varies based on the value of the lookup.cache.strategy parameter. If you set the lookup.cache.strategy parameter to None, you do not need to specify the lookup.cache.ttl parameter. This indicates that cache entries do not expire. If you set the lookup.cache.strategy parameter to LRU, the lookup.cache.ttl parameter indicates the cache timeout period. By default, cache entries do not expire. If you set the lookup.cache.strategy parameter to ALL, the lookup.cache.ttl parameter indicates the cache refresh period. By default, the cache is not reloaded. The value of this parameter must be in the time format. For example, you can set this parameter to 1min or 10s. |

| lookup.m ax-join- rows | The maximum number of results that are returned each time a data record in the primary table is queried and matched with data records in the dimension table. | No | INTEGE R | 1024 | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |
|---|---|---|---|---|---|

Sink table-specific parameters

| Paramet er | Descriptio n | Requir ed | Data type | Default value | Remarks |
|---|---|---|---|---|---|
| url | MySQL JDBC URL | No | STRING | None | Contact Apsara Stack O&M engineers to obtain the required information. |
| sink.max- retries | The maximum number of retries to write data to the table after data fails to be written. | No | INTEGER | 3 | None. |
| sink.buffe r- flush.batc h-size | The number of data records that can be written at a time. | No | INTEGER | 4096 | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. |

| sink.buffe r- flush.max -rows | The maximum number of data records that can be cached in the memory. | No | INTEGER | If Realtime Compute for Apache Flink uses a VVR version earlier than 6.0.7, the default value of this parameter is 100. If Realtime Compute for Apache Flink uses VVR 6.0.7 or later, the default value of this parameter is 10000. | This parameter takes effect only after you specify the primary key. |
|---|---|---|---|---|---|

| sink.buffe r- flush.inter val | The interval at which the cache is cleared. The value of this parameter indicates that if the number of input data records does not reach the value specified by the batchSize parameter within a specific period of time, all cached data is written to the sink table. | No | DURATIO N | 1s | None. |
|---|---|---|---|---|---|

| sink.ignor e-delete | Specifies whether to ignore delete operations. | No | BOOLEAN | false | Only Realtime Compute for Apache Flink that uses VVR 6.0.7 or later supports this parameter. Delete operations may occur when you use Flink SQL. If multiple output operators update different fields in the same sink table based on the primary key, the data result may be incorrect. For example, a data record is deleted in a task and then only some fields of the data record are updated in another task. In this case, the values of the fields that are not updated become null or default values because the fields are deleted. To prevent delete operations, you can set the ignoreDelete parameter to true. |
|---|---|---|---|---|---|
|   |   |   |   |   | Valid values: |

|   | Specifies |   |   |   | true: The fields are not updated. You can set this parameter to true only for a Realtime Compute for Apache Flink table in which a primary key is specified. If you set this parameter to true, take note of the following points: If Realtime |
|---|---|---|---|---|---|
| sink.ignor e-null- when- update | whether to update the fields whose input values are null during data updates. | No | BOOLEAN | false | Compute for Apache Flink that uses VVR 8.0.6 or earlier is used, data cannot be batch written to the sink table. If Realtime Compute for Apache Flink that uses VVR 8.0.7 or later is used, data can be batch written to the sink table. Batch write operations can significantly improve data write efficiency and increase the overall throughput. However, this may cause data latency issues and OOM errors. You need to determine whether to perform batch write operations based on your business requirements. false: The fields are updated with null values. Note Only Realtime Compute for Apache Flink that uses VVR 8.0.5 or later supports this parameter. |

**Data type mappings**

CDC source table

| Data type of MySQL CDC | Data type of Realtime Compute for Apache Flink |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED |   |
| TINYINT UNSIGNED ZEROFILL |   |
| INT | INT |
| MEDIUMINT |   |
| SMALLINT UNSIGNED |   |
| SMALLINT UNSIGNED ZEROFILL |   |
| BIGINT | BIGINT |
| INT UNSIGNED |   |
| INT UNSIGNED ZEROFILL |   |
| MEDIUMINT UNSIGNED |   |
| MEDIUMINT UNSIGNED ZEROFILL |   |
| BIGINT UNSIGNED | DECIMAL(20, 0) |
| BIGINT UNSIGNED ZEROFILL |   |
| SERIAL |   |
| FLOAT [UNSIGNED] [ZEROFILL] | FLOAT |

| DOUBLE [UNSIGNED] [ZEROFILL] | DOUBLE |
|---|---|
| DOUBLE PRECISION [UNSIGNED] [ZEROFILL] |   |
| REAL [UNSIGNED] [ZEROFILL] |   |
| NUMERIC(p, s) [UNSIGNED] [ZEROFILL] | DECIMAL(p, s) |
| DECIMAL(p, s) [UNSIGNED] [ZEROFILL] |   |
| BOOLEAN | BOOLEAN |
| TINYINT(1) |   |
| DATE | DATE |
| TIME [(p)] | TIME [(p)] [WITHOUT TIME ZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIME ZONE] |
| TIMESTAMP [(p)] | TIMESTAMP [(p)] |
|   | TIMESTAMP [(p)] WITH LOCAL TIME ZONE |
| CHAR(n) | STRING |
| VARCHAR(n) |   |
| TEXT |   |
| BINARY | BYTES |
| VARBINARY |   |
| BLOB |   |

**Important**

> We recommend that you use fields of the TINYINT(1) data type of MySQL to store only values 0 and 1. When the MySQL database uses the TINYINT(1) data type to store data of the BOOLEAN data type, the MySQL CDC source table maps the TINYINT(1) data type to the BOOLEAN data type of Realtime Compute for Apache Flink. If you use fields of the TINYINT(1) data type of MySQL to store values other than 0 and 1, the data may be inaccurate.

Dimension table and sink table

| Data type of MySQL | Data type of Realtime Compute for Apache Flink |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED |   |
| INT | INT |
| MEDIUMINT |   |
| SMALLINT UNSIGNED |   |
| BIGINT | BIGINT |
| INT UNSIGNED |   |
| BIGINT UNSIGNED | DECIMAL(20, 0) |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DOUBLE PRECISION |   |
| NUMERIC(p, s) | DECIMAL(p, s) Note The value of p is less than or equal to 38. |
| DECIMAL(p, s) |   |

| BOOLEAN | BOOLEAN |
|---|---|
| TINYINT(1) |   |
| DATE | DATE |
| TIME [(p)] | TIME [(p)] [WITHOUT TIME ZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIME ZONE] |
| TIMESTAMP [(p)] |   |
| CHAR(n) | CHAR(n) |
| VARCHAR(n) | VARCHAR(n) |
| BIT(n) | BINARY(⌈n/8⌉) |
| BINARY(n) | BINARY(n) |
| VARBINARY(N) | VARBINARY(N) |
| TINYTEXT | STRING |
| TEXT |   |
| MEDIUMTEXT |   |
| LONGTEXT |   |
| TINYBLOB | BYTES Important Realtime Compute for Apache Flink supports only MySQL binary large object (BLOB) records that are less than or equal to 2,147,483,647(2^31 - 1). |
| BLOB |   |
| MEDIUMBLOB |   |
| LONGBLOB |   |

**Sample code**

Sample code for a MySQL CDC source table

```
CREATE TEMPORARY TABLE mysqlcdc_source (
   order_id INT,
   order_date TIMESTAMP(0),
   customer_name STRING,
   price DECIMAL(10, 5),
   product_id INT,
   order_status BOOLEAN,
   PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  order_id INT,
  customer_name STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT order_id, customer_name FROM mysqlcdc_source;
```

Sample code for a MySQL dimension table

```
CREATE TEMPORARY TABLE datagen_source(
  a INT,
  b BIGINT,
  c STRING,
  `proctime` AS PROCTIME()
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE mysql_dim (
  a INT,
  b VARCHAR,
  c VARCHAR
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
```

);

```
CREATE TEMPORARY TABLE blackhole_sink(
  a INT,
  b STRING
) WITH (
  'connector' = 'blackhole'
```

);

```
INSERT INTO blackhole_sink SELECT T.a, H.b FROM datagen_source AS T JOIN mysql_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T. a = H.a;
```

Sample code for a MySQL sink table

```
CREATE TEMPORARY TABLE datagen_source (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'datagen'
```

);

```
CREATE TEMPORARY TABLE mysql_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'mysql',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
```

);

```
INSERT INTO mysql_sink SELECT * FROM datagen_source;
```

**Basic concepts about MySQL CDC source tables**

How it works When the MySQL CDC source connector is started, the connector scans the whole table whose data needs to be read, splits the table into multiple chunks based on the primary key, and then records the binary log file position at this time. Then, the MySQL CDC source connector uses the incremental savepoint algorithm to read data from each chunk by using the SELECT statement. The deployment periodically generates checkpoints to record the chunks whose data is read. If a failover occurs, the MySQL CDC connector needs to only continue reading data from the chunks whose data is not read. After the data of all chunks is read, incremental change records are read from the previous binary log file position. The deployment continues periodically generating checkpoints to record the binary log file position. If a failover occurs, the MySQL CDC source connector processes data from the previous binary log file position. This way, the exactly-once semantics are implemented. Metadata In most cases, access to metadata is required when you merge and synchronize tables in a sharded database. If you expect to identify data records by the source database names and table names after tables are merged, you can configure metadata columns in the data merging statement to read the source database name and table name of each data record. This way, you can identify the source of each data record after tables are merged. MySQL CDC source tables that are used by Realtime Compute for Apache Flink of vvr- 4.0.11-flink-1.13 or later support the metadata column syntax. The following table describes the metadata that you can access by using metadata columns.

| Metadata key | Metadata type | Description |
|---|---|---|
| database nam _ e | STRING NOT NULL | The name of the source database to which the current data record belongs. |

| table name _ | STRING NOT NULL | The name of the source table to which the current data record belongs. |
|---|---|---|
| op ts _ | TIMESTAMP LTZ(3) _ NOT NULL | The time when the current data record changes in the database. If the data record is obtained from the historical data of the table instead of from the binary log file, the value of the metadata key is fixed to 0. |
| op type _ | STRING NOT NULL | The change type of the current data record. Valid values: +I: indicates an INSERT message. -D: indicates a DELETE message. -U: indicates an UPDATE BEFORE message. _ +U: indicates an UPDATE AFTER message. _ Note Only Realtime Compute for Apache Flink that uses VVR 8.0.7 or later supports this parameter. |

The following sample code shows how to merge multiple orders tables in database shards of a MySQL instance into a MySQL table named mysql_orders and synchronize data from the MySQL table to a Hologres table named holo_orders.

```
CREATE TABLE mysql_orders (
  db_name STRING METADATA FROM 'database_name' VIRTUAL,  -- Read the database name.
  table_name STRING METADATA  FROM 'table_name' VIRTUAL, -- Read the table name.
  operation_ts TIMESTAMP_LTZ(3) METADATA FROM 'op_ts' VIRTUAL, -- Read the change tim
```

`e.`

```
  op_type STRING METADATA FROM 'op_type' VIRTUAL, -- Read the change type.
  order_id INT,
  order_date TIMESTAMP(0),
  customer_name STRING,
  price DECIMAL(10, 5),
  product_id INT,
  order_status BOOLEAN,
  PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',
  'hostname' = 'localhost',
  'port' = '3306',
  'username' = 'flinkuser',
  'password' = 'flinkpw',
  'database-name' = 'mydb_.*', -- Use a regular expression to match multiple database
shards.
  'table-name' = 'orders_.*'   -- Use a regular expression to match multiple tables i
n the sharded database.
```

);

```
INSERT INTO holo_orders SELECT * FROM mysql_orders;
```

If you add the 'scan.read-changelog-as-append-only.enabled' = 'true' configuration to the WITH clause in the preceding sample code, the output of the sample code varies based on the primary key of the downstream table: If the primary key of the downstream table is order_id, the output contains only the last change data of each primary key value of the upstream table. If the last change of a primary key value of the upstream table is a delete operation, a data record with the same primary key value and op_type as -D is contained in the downstream table. If the primary key of the downstream table is composed of order_id, operation_ts, and op_type, the output contains the complete change data of each primary key value of the upstream table. Regular expressions MySQL CDC source tables allow you to use regular expressions in table names or database names to match multiple tables or databases. The following sample code provides an example on how to use a regular expression to specify multiple tables.

```
CREATE TABLE products (
  db_name STRING METADATA FROM 'database_name' VIRTUAL,
  table_name STRING METADATA  FROM 'table_name' VIRTUAL,
  operation_ts TIMESTAMP_LTZ(3) METADATA FROM 'op_ts' VIRTUAL,
  order_id INT,
  order_date TIMESTAMP(0),
  customer_name STRING,
  price DECIMAL(10, 5),
  product_id INT,
  order_status BOOLEAN,
  PRIMARY KEY(order_id) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',
  'hostname' = 'localhost',
  'port' = '3306',
  'username' = 'root',
  'password' = '123456',
  'database-name' = '(^(test).*|^(tpc).*|txc|.*[p$]|t{2})', -- Use the regular expres
sion to match multiple databases.
  'table-name' = '(t[5-8]|tt)' -- Use the regular expression to match multiple tables
```

`.` ); Elements in the preceding regular expressions: In this example, ^(test).* is used to match a database whose name starts with the specified prefix. This expression can be used to match databases whose names start with test, such as test1 or test2. In this example, .*[p$] is used to match a database whose name ends with the specified suffix. This expression can be used to match databases whose names end with p, such as cdcp or edcp. In this example, txc is used to match the specified database name. This expression can be used to match a database that has a specific name, such as txc. When the MySQL CDC source connector matches a full-path table name, the connector uses the database name and table name to uniquely identify a table. This way, databasename.table-name is used as the pattern to match a table. For example, the (^(test).*| ^(tpc).*| txc |.*[p$]| t{2}).(t[ 5-8]| tt) pattern can match the txc.tt and test2.test5 tables in the database.

> **Important:** Values of table-name and database-name can also be separated by commas (,) to specify multiple tables or databases, such as `'table-name' = 'mytable1,mytable2'` . However, the separator conflicts with the commas (,) in regular expressions. If you use a regular expression that contains commas (,), you must rewrite the regular expression into an equivalent regular expression that contains vertical bars (|). For example, if you use the mytable_\d{1, 2) regular expression, you must rewrite the regular expression into an equivalent regular expression (mytable_\d{1}|mytable_\d{2}) to prevent comma conflicts.

Parallelism control The MySQL CDC source connector can read full data in multiple subtasks at the same time. This improves the efficiency of data loading. If you use the MySQL CDC source connector together with the Autopilot feature that is provided by the VVP of Realtime Compute for Apache Flink, automatic scale-in can be performed during incremental data reading after parallel reading is complete. This helps reduce the computing resources that are consumed. You can configure the Parallelism parameter in Basic mode or Expert mode in the Deployment Starting Configuration - Streaming dialog box in the development console of Realtime Compute for Apache Flink. The setting of the Parallelism parameter varies based on the resource configuration mode. In Basic mode, the Parallelism parameter specifies the global parallelism of all deployments. In Expert mode, you can configure the Parallelism parameter for a specific vertex node based on your business requirements.

> **Important:** When you configure the Parallelism parameter for a deployment in Basic mode or Expert mode, make sure that the range of the server-id parameter declared in the table is greater than or equal to the value of the Parallelism parameter for the deployment. For example, if the range of the server-id parameter is 5404-5412, eight unique server IDs can be used. Therefore, you can configure a maximum of eight parallel subtasks. In addition, the range specified by the server-id parameter for the same MySQL instance in different deployments cannot overlap. Each deployment must be explicitly configured with a unique server ID.

Automatic scale-in by using Autopilot When full data is read, a large amount of historical data is accumulated. In most cases, Realtime Compute for Apache Flink reads historical data in parallel to improve the efficiency of data reading. When incremental data is read, only a single subtask is run because the amount of binary log data is small and the global order must be ensured. The numbers of compute units (CUs) that are required during full data reading and incremental data reading are different. You can use the Autopilot feature to balance performance and resource consumption. Autopilot monitors the traffic for each task that is used by the MySQL CDC source table. If the binary log data is read in only one task and other tasks are idle during incremental data reading, Autopilot automatically reduces the number of CUs and the degree of parallelism. To enable Autopilot, you need to only set the Mode parameter of Autopilot to Active on the Deployments page.

> **Note:** By default, the minimum interval at which the degree of parallelism is decreased is 24 hours.

Startup mode You can configure the scan.startup.mode parameter to specify the mode in which the MySQL CDC source connector starts to read data from a MySQL database. Valid values: initial: When the MySQL CDC source connector starts for the first time, the connector reads full data in a database table. After the full data reading is complete, the connector switches to the incremental reading mode to read binary log data. This is the default value. earliest-offset: The MySQL CDC source connector skips the savepoint reading phase and starts to read accessible binary log data from the earliest offset. latest-offset: The MySQL CDC source connector skips the savepoint reading phase and starts to read binary log data from the most recent offset. In this mode, the MySQL CDC source connector can read only data changes after the deployment is started. specific-offset: The MySQL CDC source connector skips the savepoint reading phase and starts to read binary log data from the specified offset. You can specify the startup offset by using the name of a binary log file and the binary log file position or by using a GTID set. timestamp: The MySQL CDC source connector skips the savepoint reading phase and starts to read binary log events from the specified timestamp. Sample code:

```
CREATE TABLE mysql_source (...) WITH (
    'connector' = 'mysql-cdc',
    'scan.startup.mode'='earliest-offset, ' -- Starts to read data from the earliest
offset.
    'scan.startup.mode' = 'latest-offset', -- Starts to read data from the most recen
t offset.
    'scan.startup.mode' = 'specific-offset', -- Starts to read data from the specifie
d offset.
    'scan.startup.mode' = 'timestamp', -- Starts to read data from the specified time
stamp.
    'scan.startup.specific-offset.file' = 'mysql-bin.000003', -- Specifies the name o
f the binlog log file when the scan.startup.mode parameter is set to specific-offset.
    'scan.startup.specific-offset.pos' = '4', -- Specifies the binary log file positi
on when the scan.startup.mode parameter is set to specific-offset.
    'scan.startup.specific-offset.gtid-set' = '24DA167-0C0C-11E8-8442-00059A3C7B00:1-
19', -- Specifies the GTID set when the scan.startup.mode parameter is set to specifi c-offset.
    'scan.startup.timestamp-millis' = '1667232000000' -- Specifies the startup timest
amp when the scan.startup.mode parameter is set to timestamp.
    ...
```

`)`

> **Important:** When a checkpoint is created, the MySQL CDC source connector records the current binary log event at the current offset as a log entry of the INFO level. The prefix of the log entry is `Binlog offset on checkpoint {checkpoint-id}` . The log entry can help you start the deployment from a specific checkpoint.
> If the schema of a table is changed after the table is read, an error may occur when the scan.startup.mode parameter is set to earliest-offset, specific-offset, or timestamp. This is because the Debezium reader saves the latest table schema and earlier data that does not match the table schema cannot be correctly parsed.

MySQL CDC source tables that do not have a primary key In Realtime Compute for Apache Flink that uses VVR 6.0.7 or later, you can use MySQL CDC source tables that do not have a primary key. To use a MySQL CDC source table that does not have a primary key, you must configure the scan.incremental.snapshot.chunk.key-column parameter and specify only non-null fields. The processing semantics of a MySQL CDC source table that does not have a primary key is determined based on the behavior of the columns that are specified by the scan.incremental.snapshot.chunk.key-column parameter. If no update operation is performed on the specified columns, the exactly-once semantics are ensured. If the update operation is performed on the specified columns, only the at-least-once semantics are ensured. However, you can specify the downstream primary key and perform the idempotence operation to ensure data correctness. Reading of backup binary log files from ApsaraDB RDS for MySQL The MySQL CDC source connector supports the reading of backup binary log files from ApsaraDB RDS for MySQL. This operation is suitable for scenarios in which full data reading takes a long period of time, local binary log files are automatically deleted, and the backup binary log files that are automatically or manually uploaded are available. Sample code:

```
CREATE TABLE mysql_source (...) WITH (
    'connector' = 'mysql-cdc',
    'rds.region-id' = 'cn-beijing',
    'rds.access-key-id' = 'xxxxxxxxx',
    'rds.access-key-secret' = 'xxxxxxxxx',
    'rds.db-instance-id' = 'rm-xxxxxxxxxxxxxxxxx',
    'rds.main-db-id' = '12345678',
    'rds.download.timeout' = '60s'
    ...
```

`)` Enable binary log parsing acceleration Binary log files record the change data of all tables. During incremental data reading, the MySQL CDC source connector parses the change data. You can configure the following parameters to accelerate the parsing of binary log data: scan.only.deserialize.captured.tables.changelog.enabled: Parse only events in specific tables. scan.only.deserialize.captured.tables.changelog.enabled: Use multiple threads to parse events in binary log files and send the parsed events to the consumption queue based on the event order in the binary log files. Sample code:

```
CREATE TABLE mysql_source (...) WITH (
    'connector' = 'mysql-cdc',
    'scan.only.deserialize.captured.tables.changelog.enabled' = 'true', -- Parses onl
y events in the specified tables.
    'scan.parallel-deserialize-changelog.enabled' = 'true' -- Uses multiple threads t
o parse events in binlog files.
    ...
```

`)`

**MySQL CDC DataStream API**

> **Important:** If you use DataStream to read and write data, you must use a DataStream connector to connect to Realtime Compute for Apache Flink.

Create a DataStream API program and use the MySqlSource class. Sample code:

```java
import org.apache.flink.api.common.eventtime.WatermarkStrategy; import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment; import com.ververica.cdc.debezium.JsonDebeziumDeserializationSchema; import com.ververica.cdc.connectors.mysql.source.MySqlSource; public class MySqlSourceExample {
  public static void main(String[] args) throws Exception {
    MySqlSource<String> mySqlSource = MySqlSource.<String>builder()
        .hostname("yourHostname")
        .port(yourPort)
        .databaseList("yourDatabaseName") // set captured database
        .tableList("yourDatabaseName.yourTableName") // set captured table
        .username("yourUsername")
        .password("yourPassword")
        .deserializer(new JsonDebeziumDeserializationSchema()) // converts SourceRecord
to JSON String
        .build();
    StreamExecutionEnvironment env =
StreamExecutionEnvironment.getExecutionEnvironment();
    // enable checkpoint
    env.enableCheckpointing(3000);
    env
      .fromSource(mySqlSource, WatermarkStrategy.noWatermarks(), "MySQL Source")
      // set 4 parallel source tasks
      .setParallelism(4)
      .print().setParallelism(1); // use parallelism 1 for sink to keep message orderin
```

`g`

```
    env.execute("Print MySQL Snapshot + Binlog");
```

`}` `}` The following table describes the parameters that you must configure for the MySqlSource class.

| Paramete r | Description |
|---|---|
| hostname | The IP address or hostname that is used to access your ApsaraDB RDS for MySQL database. |
| port | The port that is used to access your MySQL database. |
| databaseL ist | Your MySQL database name. Note If you want to read data from multiple databases, you can set this parameter to a regular expression. You can use a combination of a period and an asterisk (.*) to match all databases. |

| username | The username that is used to access the ApsaraDB RDS for MySQL database. |
|---|---|
| password | The password that is used to access your MySQL database. |
| deserialize r | A deserializer, which deserializes SourceRecords to a specified type. Valid values: RowDataDebeziumDeserializeSchema: deserializes SourceRecords to Flink Table/SQL internal data structure RowData. JsonDebeziumDeserializationSchema: deserializes SourceRecords to JSON strings. |

ement

## 6 O&M management

### 6.1 Deployment management

#### 6.1.1 Default draft settings

The Configurations page displays the default configurations of streaming drafts and batch drafts. You can modify the configurations to meet your business requirements.

**Default settings for streaming drafts**

1. Log in to the Realtime Compute for Apache Flink console.

| e | workspace and namespace that you want to manage |   |
|---|---|---|
| column. |   |   |

and click **Console** in the **Actions** column.
3. In the left-side navigation pane, click **Configurations**.
4. On the **Deployments Defaults** page, click **Defaults for Stream**.
5. Modify the parameters.

| Parameter |   | Description |
|---|---|---|
| Staring Parameters | Checkpointing Interval | The interval at which checkpoints are scheduled. If you do not specify this parameter, the default value of the job engine version is used. The default interval is 180 seconds. |
|   | Min Interval Between Checkpoints | The minimum time interval between two system checkpoints. If the maximum parallelism of checkpoints is 1, this configuration ensures a minimum time interval between two checkpoints. If you do not specify this parameter, the default value of the job engine version is used. The default interval is 180 seconds. |
|   | State Expiration Time | The time-to-live (TTL) of the Flink state. The state service clears the current state every time the specified time duration ends. The default time duration is 36 hours. |

ement

|   | Flink Restart Policy | Supported policies: Failure Rate: The deployment is restarted if the number of failures within the specified interval exceeds the upper limit. If you select this option, you must configure the Failure Rate Interval, Max failures per interval, and Delay Between Restart Attempts parameters. Fixed Delay: Deployments are restarted at a fixed interval. If you select this option, you must also configure the Number of Restart Attempts and Delay Between Restart Attempts parameters. No Restarts: Deployments are not restarted if the task fails. |
|---|---|---|
|   | Number of Restart Attempts | The number of retries that Realtime Compute for Apache Flink performs before it declares a deployment failure. If checkpointing is enabled, the value of the Integer.MAX VALUE parameter applies. The default _ value is 2147483647. |
|   | Delay Between Restart Attempts | After a deployment fails, retries are not immediately performed, but are performed after the specified delay. Default value: 10. |
| Additional Flink Configuratio n | / | Configure other Flink settings, such as taskmanager.numberOfTaskSlots: 1 . |
| Logging | Root Log Level | Valid values: TRACE, DEBUG, INFO, WARN, and ERROR. |
|   | Log Levels | The log name and log level. |
|   | Logging Profile | Both system templates and user-defined templates are supported. The default value is default, which specifies system templates. |

6. Click **Save Changes**.
If you click **Discard Changes** before you save the changes, the changes are discarded.

**Defaults for Batch**

1. Log in to the Realtime Compute for Apache Flink console.

| e | workspace and namespace that you want to manage |   |
|---|---|---|
| column. |   |   |

and click **Console** in the **Actions** column.
3. In the left-side navigation pane, click **Configurations**.
4. On the **Deployment Defaults** page, click the **Defaults for Batch** tab.
ement
5. Modify the parameters.

| Parameter |   | Description |
|---|---|---|
| Staring Parameters | Flink Restart Policy | Supported policies: Failure Rate: The deployment is restarted if the number of failures within the specified interval exceeds the upper limit. If you select this option, you must configure the Failure Rate Interval, Max failures per interval, and Delay Between Restart Attempts parameters. Fixed Delay: Deployments are restarted at a fixed interval. If you select this option, you must also configure the Number of Restart Attempts and Delay Between Restart Attempts parameters. No Restarts: Deployments are not restarted if the task fails. |
|   | Number of Restart Attempts | The number of retries that Realtime Compute for Apache Flink performs before it declares a deployment failure. If checkpointing is enabled, the value of the Integer.MAX VALUE parameter applies. _ The default value is 2147483647. |
|   | Delay Between Restart Attempts | After a deployment fails, retries are not immediately performed, but are performed after the specified delay. Default value: 10. |
| Additional Flink Configuration | / | Configure other Flink settings, such as taskmanager.numberOfTaskSlots: 1 . |
| Logging | Root Log Level | Valid values: TRACE, DEBUG, INFO, WARN, and ERROR. |
|   | Log Levels | The log name and log level. |
|   | Logging Profile | The log template. You can use the system template or configure a custom template. |

6. Click **Save Changes**.
If you click **Discard Changes** before you save the changes, the changes are discarded.

#### 6.1.2 Create a deployment

After you develop a draft, you must publish the draft as a deployment. Then, you can start and run the deployment. This topic describes how to create an SQL deployment, a JAR deployment, and a Python deployment.

**Procedure**

ement

**Deploy an SQL draft**

1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces** page, find the namespace that you want to manage and click **Console**
in the **Actions** column.
3. On the **SQL Editor** page, develop an SQL draft. For more information, see Develop an SQL
draft.
4. After the SQL draft is developed, click **Deploy** in the upper-right corner of the SQL Editor
page.
5. In the Deploy draft dialog box, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Comment | Optional. Enter a description for the deployment. |
| Deploy to Session Cluster (not recommended) | We recommend that you do not select this option in the production environment. If you select this option, you must select the desired session cluster from the drop-down list below this option. For more information about how to create a session cluster, see Configure a session cluster |
| Skip validation on draft before deploying | If you select this option, you can skip the syntax check before you deploy a draft as a deployment. |

6. Click **Confirm**.

**Create a JAR deployment**

Make sure that a JAR package is developed before you deploy a JAR draft. For more information, see Develop a JAR draft.
1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces** page, find the namespace that you want to manage and click **Console**
in the **Actions** column.
3. In the left-side navigation pane, click **Deployments**. On the Deployments page, click
**Create Deployment**.
4. In the Create Deployment dialog box, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Deployment Type | Select JAR. |
| Deployment Mode | Select Stream Mode or Batch Mode. |

ement

| Deployment Name | Enter the name of the JAR deployment. |
|---|---|
| Engine Version | We recommend that you use a recommended version or a stable version. Engine versions are classified into the following types: Recommended version: the latest minor version of the latest major version. Stable version: the latest minor version of a major version that is still in the service period of the product. Defects in previous versions are fixed in such a version. Normal version: other minor versions that are still in the service period of the product. Deprecated version: the versions that exceed the service period of the product. |
| JAR URI | Select a file or manually upload a new file. You can drag the file that you want to upload to this field or click the icon on the right to select the file that you want to upload. Note If your deployment is a Python API deployment, upload the official JAR file of PyFlink. To download the official JAR file of the required version, click PyFlink V1.11 or PyFlink V1.12. |
| Entry Point Class | Specify the entry point class of the JAR application. If you do not specify a main class for the JAR file, enter a standard path in the Entry Point Class field. Note If your deployment is a Python API deployment, enter org.apache.flink.client.python.PythonDriver in the Entry Point Class field. |
| Entry Point Main Arguments | You can pass parameters and call them in the main method. Note The parameter information cannot be greater than 1,024 characters in length. We recommend that you do not use complex parameters. The parameters that include line breaks, spaces, or other special characters are considered complex parameters. If you want to pass complex parameters, use a dependency file. If your deployment is a Python API deployment, upload the Python deployment file first. By default, after you upload the Python deployment file, the file is uploaded to the /flink/usrlib/ directory of the node that runs the deployment. If the Python deployment file is named word count.py, enter -py _ /flink/usrlib/word count.py in the Entry Point Main Arguments _ field. Enter the full path of the Python deployment file. You cannot omit or change /flink/usrlib/. |

| -py |   |
|---|---|

ement

| Additional Dependenci es | (Recommended) Select the dependency file that you uploaded. You must upload a dependency file in advance. To upload a dependency file, click Upload Artifacts in the upper-left corner of the Artifacts page or click the icon on the right side of Additional Dependencies in the Create Deployment dialog box. The uploaded dependency file is saved in the oss://ossBucketName/artifacts/namespaces/namespaceName/<file> directory. Enter the OSS bucket where the required dependency file is stored. You must upload the dependency file to the OSS bucket that corresponds to the current instance in advance. The OSS bucket to which the dependency file is uploaded must be the OSS bucket that you selected to activate Realtime Compute for Apache Flink. Enter the URL of the required dependency file. Only URLs that end with file names are supported, such as http://xxxxxx/<file>. You must upload the dependency file to the publicly accessible HTTP service in advance. Note The dependency file that you upload by using one of the preceding methods can also be downloaded to the destination machine. When the deployment is running, the dependency file is loaded to the /flink/usrlib directory of the pod in which the JobManager and TaskManager reside. If you select Deploy to Session Cluster (not recommended) when you create the deployment, you cannot specify the path of the dependency file for the deployment. |
|---|---|
| Description | Optional. Enter a description for the deployment. |
| More Setting | If you turn on the switch, you must configure the following parameters: Kerberos Name: Select a Hive cluster that supports Kerberos authentication from the drop-down list. For more information about how to create a Hive cluster that supports Kerberos authentication, see Security management. principal: a Kerberos principal, which can be a user or a service. A Kerberos principal is used to uniquely identify an identity in the Kerberos encryption system. |

5. Click **Deploy**.

**Create a Python deployment**

Make sure that a Python package is developed before you create a Python deployment. For more information, see Develop a Python API draft.
1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces** page, find the namespace that you want to manage and click **Console**
in the **Actions** column.
3. In the left-side navigation pane, click **Deployments**. On the Deployments page, click
**Create Deployment**.
4. In the Create Deployment dialog box, configure the parameters. The following table
describes the parameters. ement

| Parameter | Description |
|---|---|
| Deployment Type | Select PYTHON. |
| Deployment Mode | Select Stream Mode or Batch Mode. |
| Deployment Name | The name of the Python deployment. |
| Engine Version | We recommend that you use a recommended version or a stable version. Engine versions are classified into the following types: Recommended version: the latest minor version of the latest major version. Stable version: the latest minor version of a major version that is still in the service period of the product. Defects in previous versions are fixed in such a version. Normal version: other minor versions that are still in the service period of the product. Deprecated version: the versions that exceed the service period of the product. |
| Python Uri | The Uniform Resource Identifier (URI) used to access the Python deployment file that you want to upload. Python deployment files can be .py files or .zip files. |
| Entry Module | Specify the entry point class of the JAR application. If the Python deployment file that you select is a .py file, you do not need to configure this parameter. If the Python deployment file that you select is a .zip file, you must configure this parameter. For example, you can enter example.word count in the Entry Module _ field. |
| Entry Point Main Arguments | Enter the parameters of the deployment. |
| Python Libraries | Specify the third-party Python package that you want to use. The third-party Python package that you uploaded is added to PYTHONPATH of the Python worker process so that the package can be directly accessed in Python user-defined functions (UDFs). |

ement

| Python Archives | Specify the archive files. Only ZIP files such as .zip, .jar, .whl, and .egg are supported. Archive files are decompressed to the working directory of the Python worker process. For example, if the name of the compressed file where the archive files are located is mydata.zip, the following code can be written in Python UDFs to access the mydata.zip archive file. def map(): with open("mydata.zip/mydata/data.txt") as f: ... |
|---|---|
| Additional Dependencie s | You can upload a file for the deployment, such as a Python deployment file and a data file that the deployment requires. For more information about Python dependencies, see Python Dependency. By default, the dependency file that you upload is downloaded to the /flink/usrlib/ directory of the node on which the deployment runs. Note Session clusters do not support the configuration of the Additional Dependencies parameter. Only per-job clusters support the configuration of the Additional Dependencies parameter. |
| Description | Optional. Enter a description for the deployment. |
| More Setting | If you turn on the switch, you must configure the following parameters: Kerberos Name: Select a Hive cluster that supports Kerberos authentication from the drop-down list. For more information about how to create a Hive cluster that supports Kerberos authentication, see Security management. principal: a Kerberos principal, which can be a user or a service. A Kerberos principal is used to uniquely identify an identity in the Kerberos encryption system. |

5. Click **Deploy**.

**References**

After you create the deployment, start the deployment on the **Deployments** page. For more information about how to start a deployment, see Start a deployment.

#### 6.1.3 Start a deployment

After you develop a draft and deploy the draft as a deployment, you must start the deployment on the Deployments page to run the deployment. If you want to resume a deployment that is canceled, or if you want to make the parameter configuration take effect after you modify the parameter configuration, you must also start the deployment. This topic describes how to start a deployment.

**Limits**

You can specify startup options for only streaming deployments. ement Only the Simple Log Service (SLS)and ApsaraMQ for Kafka source table connectors allow you to configure the Specify source's start time (SLS/Kafka) parameter in the Start Job dialog box. The Specify source's start time (SLS/Kafka) parameter that is configured in the Start Job dialog box takes precedence over the startTime parameter that is configured in the DDL code of a draft. If you configure the Specify source's start time (SLS/Kafka) parameter in the Start Job dialog box and the startTime parameter in the DDL code, the configuration of the Specify source's start time (SLS/Kafka) parameter takes effect.

> **Note:** Not all connector types support the startTime parameter. For more information about whether the parameters in the WITH clause for each type of connector include the startTime parameter, see the related topic of the specific type of connector.
> The startTime parameter takes effect only if a new deployment is started and the startTime parameter is configured. If you start a deployment based on a checkpoint or savepoint, the startTime parameter does not take effect even if this parameter is configured.

**Usage notes**

If you select Latest State or Specific State when you start a deployment, the system performs a state data compatibility check.

**Procedure**

1. Go to the Deployments page to start the desired deployment.
i. Log in to the Realtime Compute for Apache Flink console. ii. Find the namespace that you want to manage and click **Console** in the **Operation** column. iii. In the left-side navigation pane, click **Deployments**.
2. On the **Deployments** page, select **STREAM** or **BATCH** from the drop-down list of the
deployment type.
3. Find the deployment that you want to start and click **Start** in the **Actions** column.
4. Optional. In the Start Job dialog box, configure the startup parameters. This step is required
only for streaming deployments.
**Initial Mode**: If you start a deployment for the first time without the need to reuse
states, select this option. If a deployment cannot reuse a state, you can also select this option. If you select **Initial Mode**, you can select **Specify source's start time**
**(SLS/Kafka)** to specify the start time for reading data.
**Resume Mode**: You can choose a specific startup strategy based on your business
requirements.

| Policy | Description |
|---|---|

ement

| Latest State | If you want to resume a deployment from the latest state of a savepoint or a checkpoint, select this option. If you select this option to start a deployment, the system performs a state data compatibility check. |
|---|---|
| Specific State | Select a savepoint. |
| Other deployment state | If you select this option, you must specify a savepoint of another deployment to resume the current deployment. Savepoints can be shared between deployments, but only when the deployments are compatible with the states saved in the savepoints. |

5. Click **Start**.
On the **Deployments** page, view the deployment status.

#### 6.1.4 Cancel a deployment

If you modify the SQL logic, change the deployment version, add or delete parameters to or from the WITH clause, or add parameters for a deployment, the changes take effect after you cancel the deployment and then restart it. This topic describes how to stop a deployment in the RUNNING state.

**Usage notes**

If you restart a deployment that is canceled, you can select Start without state for Start Method and specify Start Time for Reading Data. You can also resume a deployment from the savepoint that you select. For more information about the configuration, see Start a deployment.

> **Note:** If the state of the savepoint that is used to resume the deployment is not supported because you modify the deployment configurations, such as changing the SQL logic, the deployment can only be started without state.

**Procedure**

1. Go to the Deployments page to stop the desired deployment.
i. Log in to the Realtime Compute for Apache Flink console. ii. Find the namespace that you want to manage and click **Console** in the **Operation** column. iii. In the left-side navigation pane, click **Deployments**.
2. On the Deployments page, find the deployment that you want to manage and click **Cancel**
in the **Actions** column.
3. Click **OK**.
ement More Strategies provides the following options:
**Stop With Savepoint**: If you want the system to create a savepoint before the
deployment is canceled, you can click **More Strategies** and select **Stop With**
**Savepoint** in the Cancel this deployment dialog box. If you select **Stop With**
**Savepoint**, the system creates a savepoint for the deployment and then the deployment
enters the cancel process. If you do not select **Stop With Savepoint**, the deployment directly enters the cancel process.
**Stop With Drain**: If you select this option, the deployment is permanently terminated.
If you want to restart the deployment later, do not select this option. If you select this option, an error may occur when the deployment is resumed.

### 6.2 Artifact management

Realtime Compute for Apache Flink creates directories that are used to store data files required for or generated during deployment running. Data files include checkpoints, savepoints, logs, and JAR packages. This topic describes how to manage artifacts.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
2. Find the workspace and namespace that you want to manage and click **Console** in the
**Actions** column.
3. In the left-side navigation pane, click **Artifacts**.
4. Manage artifacts.

|   | Operation | Description |   |
|---|---|---|---|
|   |   | Click Upload Artifact and select an on-premises file that you want to upload. Alternatively, drag the file that you want to upload to the artifact list. After the file is uploaded, it is stored in the oss://flink-fullymanaged-<The |   |
|   |   |   | oss://flink-fullymanaged-<The |
|   | Upload | ID of the workspace>/artifacts/namespaces/<The name of the |   |
|   | artifacts |   |   |
|   |   | namespace><The File name> |   |
|   | Download artifacts | Click Download in the Actions column to download the file to your on-premises machine. |   |

ement

| Delete artifacts | Click Delete in the Actions column to delete the file. |
|---|---|

### 6.3 Metadata management

#### 6.3.1 Manage user-defined functions (UDFs)

To use a user-defined function (UDF) in a SQL job, you must register it. This topic describes how to register, update, and delete UDFs.

**Usage notes**

To avoid JAR file dependency conflicts: Ensure that the version of the Flink image is consistent with the Flink version specified as a dependency in your `pom.xml` file. Do not upload runtime-level JAR files. To exclude them, add `<scope>provided</scope>` to the dependency declaration. For other third-party dependencies, package them into your JAR file by using the Apache Maven Shade Plugin.

**Register a user-defined function**

You must register a UDF before using it in a SQL job.
1. Log on to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, click **SQL Development**.
3. On the **Functions** tab, click **Register UDF**. You can also click the
icon in the upperright corner.
4. Upload the UDF JAR file and click **Confirm**.
ement You can upload the UDF JAR file in one of the following ways:
**Upload File**: Next to the **Select File** option, click **Select File** and select the UDF artifact
file. If there are dependency files, click **Select File** next to the **Dependency File** option and select the dependency files.
**External URL**: Enter the external URL of the file.
The Realtime Compute for Apache Flink console parses your JAR file, automatically detects classes that implement Flink UDF, UDAF, and UDTF interfaces, and fills the Function Name field with the class names. For Java UDFs, you can package dependencies into the UDF JAR file or upload them separately as a dependency file. For Python UDFs, we recommend uploading dependencies as a separate dependency file. When a custom function's artifact file or its dependency files are large, you can upload them by using an external URL. Note that if the external URL is an OSS bucket address, the dependency files must be located in the `sql-artifacts/namespaces/{namespace}` directory.

> **Note:** The bucket must have at least public read access. The URL must use the HTTP protocol and cannot contain encoded characters.

5. In the **Manage Functions** dialog box, verify the function information and click **Create**
**Function**.
ement After the function is registered, the dialog box displays information about the **Registered**
**Functions**. You can then remove any unnecessary functions.
After you remove functions, the dialog box appears as shown. Verify the function details, and then close the dialog box. ement
6. In the **Functions** list on the left of the SQL editor, you can view all registered UDFs.

**Manage user-defined functions**

If you need to add or remove functions from a registered UDF JAR file, follow these steps.
1. On the **Functions** tab, hover over the name of the target JAR file and click the
icon.
2. Add or remove functions.

**Update a user-defined function**

If you add new functions to a JAR file or modify the code of existing registered functions, you can update the JAR file. ement
1. On the **Function** tab, hover over the name of the target custom function and click the
icon.
2. Update the JAR file.
You can upload the updated JAR file in one of the following ways:
**Upload File**: Next to the **Select File** option, click **Select File** and select the UDF artifact
file. If there are dependency files, click **Select File** next to the **Dependency File** option and select the dependency files.
**External URL**: Enter the external URL of the file.

> **Important:** The new JAR file that you upload must contain the classes for all currently registered UDFs. You cannot remove the class of a UDF during an update.
> The new UDF JAR file takes effect only when you restart a job or submit a new one. Running jobs continue to use the old JAR file until they are restarted.

3. Click **Modify**.

**Delete a user-defined function**

If a JAR file is no longer needed, you can delete it.
1. In the left-side navigation pane, click **SQL Development**.
2. On the **Functions** tab, hover over the name of the target JAR file and click the
icon.

> **Note:** Before you delete a JAR file, make sure that no jobs or SQL files reference any UDFs registered from it.

3. Select the **Delete the associated file** checkbox.
Deleting the UDF JAR file also deletes all UDFs registered from it. This action is required to prevent orphaned data and references.
4. Click **OK**.

#### 6.3.2 Manage Apache Paimon catalogs

After you configure an Apache Paimon catalog, you can directly access the Apache Paimon tables in the catalog stored in Alibaba Cloud Object Storage Service (OSS) from Realtime Compute for Apache Flink. This topic describes how to create, view, and delete an Apache Paimon catalog and manage Apache Paimon databases and tables in the development console of Realtime Compute for Apache Flink.

**Create an Apache Paimon Filesystem catalog**

1. Go to the Catalogs page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Workspaces** page, find the namespace that you want to manage and click
**Console** in the **Actions** column.
iii. In the left-side navigation pane, click **Catalogs**. ement
2. Click **Create Catalog**. On the Built-in Catalog tab of the wizard that appears, choose
**Apache Paimon** and click **Next**.
3. In the Configure Catalog step, configure the parameters.

| Parameter | Description | Requir ed | Remarks |
|---|---|---|---|
| catalog name | The name of the Apache Paimon catalog. | Yes | Enter a custom name. |
| metastore | The metadata storage type. | Yes | Set the value to Filesystem. |
| warehouse | The data warehouse directory that is specified in OSS. | Yes | Format: oss://<bucket>/<object>. Parameters in the directory: bucket: the name of the OSS bucket that you created. object: the path in which your data is stored. |
| fs.oss.endpoint | The endpoint of OSS. | Yes | For example, select oss-cn- hangzhou.aliyuncs.com for the China (Hangzhou) region. |
| fs.oss.accessKeyI d | The AccessKey ID that is used to access OSS. | Yes | None |
| fs.oss.accessKeyS ecret | The AccessKey secret that is used to access OSS. | Yes |   |

4. Click **Confirm**.

**Manage an Apache Paimon database**

In the script editor on the SQL Editor page, enter the following commands, select the command line and click **Run** on the left side of the command line.

**Create a database**

After you create an Apache Paimon catalog, a database named `default` is automatically created in the catalog.

```
-- Replace my-catalog with the name of the actual Apache Paimon catalog. USE CATALOG `my-catalog`; -- Replace my_db with a custom database name. CREATE DATABASE `my_db`;
```

**Drop a database**

**Important**

ement

> You cannot drop the default database from an Apache Paimon DLF catalog, an Apache Paimon MaxCompute catalog, or an Apache Paimon Sync catalog. You can only drop the default database from an Apache Paimon Filesystem catalog.

```
-- Replace my-catalog with the name of the actual Apache Paimon catalog. USE CATALOG `my-catalog`; -- Replace my_db with the name of the database that you want to drop. DROP DATABASE 'my_db'; -- Drop an empty database. DROP DATABASE `my_db` CASCADE; -- Drop the database and all the associated tables.
```

**View or delete an Apache Paimon catalog**

On the **Catalogs** page, view or delete an Apache Paimon catalog. View an Apache Paimon catalog: In the **Catalog List** section, find the catalog that you want to manage and view the information in the **Name** and **Type** columns. To view the databases and tables in the catalog, click **View** in the Actions column. Delete an Apache Paimon catalog: In the **Catalog List** section, find the catalog that you want to manage and click **Delete** in the **Actions** column. You can also delete an Apache Paimon catalog by executing the `DROP CATALOG <catalog` name>; command on the SQL Editor page.

> **Note:** After the Apache Paimon catalog is deleted, only the catalog information on the Catalogs page in the Flink namespace is deleted. The data files of the Apache Paimon tables are retained. After the Apache Paimon catalog is deleted, you can re-create the Apache Paimon catalog by executing an SQL statement. Then, you can use the Apache Paimon tables in the catalog again.

#### 6.3.3 Manage Hologres catalogs

After you create a Hologres catalog, you can directly read Hologres metadata in the console of fully managed Flink without the need to manually register Hologres tables. Hologres catalogs improve the efficiency of draft development and help ensure data accuracy. This topic describes how to create, view, use, and drop a Hologres catalog in the Realtime Compute for Apache Flink console.

**Background information**

Hologres catalogs provide metadata, such as databases, tables, partitions, and views. The metadata also includes functions and information that are required for accessing data stored in a database or other external systems. For more information, see Catalogs. You can perform the following operations to manage Hologres catalogs: Create a Hologres catalog View a Hologres catalog Use a Hologres catalog Drop a Hologres catalog

**Limits**

Only Flink 1.13 and later support Hologres catalogs. ement You cannot modify the DDL statements that are related to catalogs.

**Create a Hologres catalog**

1. Log in to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, click **Draft Editor**.
3. In the upper-left corner of the Draft Editor page, click **New**. In the New Draft dialog box,
select STREAM/SQL from the Type drop-down list.
4. In the code editor, enter the following statement to create a Hologres catalog:

```
CREATE CATALOG <catalogname> WITH (
  'type' = 'hologres',
  'endpoint' = '<endpoint>',
  'username' = '<AccessKey>',
  'password' = '<AccessSecret>',
  'dbname' = '<dbname>'
```

);
**<catalogname>** specifies the name of the Hologres catalog. The name can contain only
lowercase letters and digits. It cannot contain uppercase letters or special characters such as hyphens (-) and underscores (_). The following table describes the parameters in the WITH clause.

| Parameter | Description | Required |
|---|---|---|
| type | The type of the catalog. Set the value to hologres. | Yes |
| endpoint | The endpoint of the Hologres instance. | Yes |
| username | The AccessKey ID of your Apsara Stack tenant account. | Yes |
| password | The AccessKey secret of your Apsara Stack tenant account. | Yes |
| dbname | The name of the default Hologres database that you want to access. | Yes |

5. Click **Execute**.
After the statement is executed, the message "Query has been executed" appears. For more information about how to delete a Hologres catalog, see Delete a Hologres catalog.
6. On the left side of the Draft Editor page, click the **Schemas** tab.
7. Click the
icon to refresh and view the Hologres catalog that you created. ement

**View a Hologres catalog**

After you create a Hologres catalog, you can perform the following operations to view the metadata in the Hologres catalog.
1. Log in to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, click **Draft Editor**.
3. Click the **Schemas** tab.
4. In the top navigation bar, switch to the Hologres catalog that you want to view. In this
example, the Hologres catalog named holo is used.
5. View the databases, tables, and functions in the Hologres catalog.
ement

> **Note:** If the public schema is used, the schema prefix is not added to a table name. In this case, only the table name is used.

**Use a Hologres catalog**

Create a table in Hologres. Execute the `USE CATALOG HoloName` statement to directly reference the information of the Hologres service.

```
USE CATALOG ${catalog_name}; CREATE TABLE `${db_name}`.`${schema_name.table_name}`(
  ...
 ) WITH (
   'connector' = 'hologres'
```

); For more information about the USE syntax, see USE statements. ement Directly reference the information about the Hologres service in DDL statements.

```
CREATE TABLE `${catalog_name}`.`${db_name}`.`${schema_name.table_name}` (
  ...
) WITH (
  'connector' = 'hologres'
```

);

> **Note:** When you create a table for a registered Hologres service, you must set the connector parameter to hologres in the WITH clause. Other parameters, such as endpoint, are optional.
> You are not allowed to directly add or modify parameters in the WITH clause for a Hologres table. You can use SQL hints to add or modify the parameters in the WITH clause in the INSERT statement.

Read data from a Hologres table.

```
INSERT INTO ${other_sink_table} SELECT ... FROM `${catalog_name}`.`${db_name}`.`${schema_name.table_name}`
```

Insert result data into a Hologres table.

```
INSERT INTO `${catalog_name}`.`${db_name}`.`${schema_name.table_name}` SELECT ... FROM ${other_source_table}
```

> **Note:** If the public schema is used, ${table_name} is used instead of **${schema_name.table_name}**. This is because the schema prefix is not added to the table name in this case.

**Drop a Hologres catalog**

1. Log in to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, click **Draft Editor**.
3. In the upper-left corner of the Draft Editor page, click **New**. In the New Draft dialog box,
select SQ from the Type drop-down list.
4. In the script editor, enter the following command:

```
DROP CATALOG ${catalog_name}
```

catalog_name is the name of the Hologres catalog that you want to drop from the development console of Realtime Compute for Apache Flink.

> **Note:** The drop operation does not affect the deployments that are running. However, deployments that are not published or deployments that you want to suspend and then resume are affected. Proceed with caution.

ement
5. Click **Execute**.
6. On the left side of the Draft Editor page, click the **Schemas** tab.
7. Click the
icon to refresh the page and check whether the Hologres catalog is dropped.

#### 6.3.4 Manage MySQL catalogs

After creating a MySQL catalog, you can directly access tables in MySQL instances under the catalog in the Realtime Compute for Apache Flink console and use them in Flink SQL deployments. This topic describes how to create and manage MySQL catalogs.

**Background information**

MySQL catalogs have the following features: Access tables in MySQL instances directly, with no need to manually register MySQL tables by using DDL statements. This improves development efficiency and accuracy. Use tables provided by MySQL catalogs as MySQL CDC source tables, MySQL sink tables, and MySQL dimension tables in Flink SQL deployments. Support ApsaraDB RDS for MySQL, PolarDB for MySQL, or self-managed MySQL. Support direct access to logical tables for sharding. Support the CDAS and CTAS syntax to synchronize entire databases, merge and synchronize sharded tables, and synchronize schema changes based on MySQL data sources.

**Prerequisites**

You have created a MySQL instance and obtained its basic information. Network interconnection requirements: You must configure allowlists correctly on both the MySQL instance side and the Apache Flink console side. MySQL instance side: Add the IP CIDR block of your Flink SQL deployment to the allowlist by using the **whitelist** feature. Apache Flink console side: Add the VIP address of your MySQL instance to the allowlist by using the **configure IP address of external data storage** feature.

**Limits**

You cannot modify the configuration of a catalog after creation. To modify the configuration, delete the catalog and create another one. You can query only existing databases and tables, and cannot use Realtime Compute for Apache Flink to create databases or tables. When using a table as a source table, you can read data in streaming mode but not in batch mode.

> **Note:** If you use a table provided by a MySQL catalog as a MySQL CDC source table, you must enable Binlog and other configurations on your ApsaraDB RDS for MySQL, PolarDB for MySQL, or self-managed MySQL instance.

ement The system cannot identify tables whose CREATE TABLE statements contain PolarDBspecific syntax.

```
Example: PARTITION BY KEY(`idempotent_id`) PARTITIONS 16, UNIQUE KEY `uk_order_id` (`order_id`).
```

If you use Realtime Compute engine VVR 8.0.7 or later, you cannot use views as Flink tables after you create them. MySQL supports only versions 5.7 and 8.0.x.

**Configure a MySQL catalog**

Create a MySQL catalog by using the UI or SQL command.

**UI method (recommended)**

1. Log in to the Realtime Compute for Apache Flink console.
2. In the left-side navigation pane, click **Catalogs**.
3. Click **Create Catalog**, select **MySQL**, and then click **Next**.
4. Fill in the configuration information.

| Parameter | Description | Required |
|---|---|---|

ement

| catalog name | Customize the MySQL catalog name. The name must meet the following requirements: It can contain only lowercase letters, numbers, hyphens (-), and periods (.), and must not end with a symbol. | Yes |
|---|---|---|
| hostname | The IP address or hostname of the MySQL database. | Yes |
| port | The port number of the MySQL database service. Default value: 3306. | Yes |
| default-database | The default MySQL database name. | Yes |
| username | The username used to connect to the MySQL database server. | Yes |
| password | The password used to connect to the MySQL database server. | Yes |

5. Click **Confirm**.
You can view the created catalog in the **Catalogs** section on the left.

**SQL commands**

1. Log in to the Realtime Compute for Apache Flink console.
2. Go to the **SQL Editor** page and click **New**.
3. Create a **blank stream draft**. In the text editor, enter the command to configure the
MySQL catalog. For more information, see Develop an SQL draft.

```
CREATE CATALOG YourCatalogName WITH(
  'type' = 'mysql',
  'hostname' = 'rm-bp1gcn0q0j0******.mysql.rds.aliyuncs.com',
  'port' = '3306',
  'username' = 'usertest',
  'password' = '${secret_values.mysqlpw}',
  'default-database' = 'flinktest',
  'catalog.table.metadata-columns'='table_name'
```

);

| Parameter | Description | Required |
|---|---|---|
| YourCatalogNam e | The custom name of the MySQL catalog. | Yes |
| type | The type. The value is fixed to mysql. | Yes |

ement

| hostname | The IP address or hostname of the MySQL database. | Yes |
|---|---|---|
| port | The port number of the MySQL database service. Default value: 3306. | No |
| username | The username for accessing the MySQL database service. | Yes |
| password | The password for accessing the MySQL database service. | Yes |
| default-database | The default MySQL database name. | Yes |
| property-version | The parameter version of the catalog. Valid values: 0 (default) and 1 (recommended). The available parameter sets and default values may vary with parameter versions. See specific differences in the parameter descriptions. Note This parameter is supported only in VVR 8.0.6 and later. The default value is 1 in VVR 11.1 and later. | No |
| catalog.table.met adata-columns | Specifies whether to add metadata columns from the MySQL CDC source table to the schema when retrieving data tables. By default, no metadata columns are added. Separate multiple metadata columns with semicolons (;), example: op ts;table name;database name . _ _ _ Note This parameter is supported only in Realtime Compute engine VVR 6.0.5 and later. While configuring this parameter, the returned table schema includes additional specified metadata columns. These columns apply only to MySQL CDC source tables. Therefore, tables returned by this catalog can be used only as source tables, not as sink tables or dimension tables. | No |

ement

| catalog.table.tre at-tinyint1-as- boolean | Specifies whether to map MySQL TinyInt(1) and Boolean types to the Flink Boolean type when retrieving the data table schema. Valid values: true: Map to the Boolean type. false: Map to the TINYINT type. Default values: property-version=0: Default value is true. property-version=1: Default value is false. Note This parameter is supported only in Realtime Compute engine VVR 8.0.4 and later. We recommend that you do not use TinyInt(1) in MySQL to store values other than 0 and 1. Choose an appropriate data type for mapping. For more information, see Realtime Comput for Apache Flink Developer Guide > Connectors > MySQL. | No |
|---|---|---|

4. Select the code that creates the catalog and click **Run**.
After execution, the system displays the message `Query has been executed` . You can view the created catalog on the **Catalogs** page.

**View and delete a MySQL catalog**

**UI method (recommended)**

Under **Catalog List** of the **Catalogs** page, you can perform the following operations on the target catalog:
**View**: Click **View** in the **Actions** column corresponding to the target catalog name to view
database and table information under the catalog. Click **Delete** in the **Actions** column corresponding to the target catalog name. In the deletion dialog box, click **Delete**.

> **Important:** The deletion operation removes only the created catalog and does not delete these tables in the corresponding service. Running deployments that use tables under this catalog are unaffected after deletion, but an error occurs (table not found) when redeploying or restarting them. Proceed with caution.

**SQL commands**

1. In the text editing area of the **SQL Editor** page, enter the following commands.

```
--View the schema information of tables under the catalog in Flink. Field comment inf ormation is not supported for display. DESCRIBE `<catalogname>`.`<dbname>`.`<tablename>`; --Delete catalog DROP CATALOG `<catalogname>`;
```

ement

> **Important:** The deletion operation removes only the created catalog and does not delete these tables in the corresponding service. Running deployments that use tables under this catalog are unaffected after deletion, but an error occurs (table not found) when redeploying or restarting them. Proceed with caution.

2. Select the corresponding command and click **Run**.

**Use a MySQL catalog**

**Read data from a MySQL source table**

```
INSERT INTO `<othersinktable>` SELECT ... FROM `<mysqlcatalog>`.`<dbname>`.`<tablename>` /*+ OPTIONS('server-id' = '6000-6008') *
```

/; When you use a MySQL catalog as a MySQL CDC source table, we recommend that you use Table Hints to specify different server IDs for deployments. If the source table requires multiconcurrency reading, you must configure server IDs in range format. The number of server IDs in the range must be greater than or equal to the concurrency.

**Read data from logical tables of sharded databases and tables**

A MySQL catalog supports using regular expressions to use database names and table names as logical table names to read data from sharded databases and tables. For example, assume that you have a MySQL database with sharded databases and tables. The database contains multiple tables such as user01, user02 to user99, which are distributed across databases such as db01 to db10. All tables have compatible schemas. You can access all sharded tables of users by using the following regular expressions for database names and table names.

```
SELECT ... FROM `db.*`.`user.*` /*+ OPTIONS('server-id'='6000-6018') */;
```

The logical tables of sharded databases and tables return two additional system fields: _db_name (STRING) and _table_name (STRING). These two fields, together with the primary keys of the original sharded tables, serve as the new composite primary key of the logical table to ensure uniqueness. If the primary key of user01 to user99 is id, the composite primary key of the user logical table is (_db_name, _table_name, id). A MySQL catalog supports combining regular expressions to match multiple tables to be synchronized, enabling merged synchronization of sharded databases and tables.

**Use CTAS and CDAS to synchronize MySQL data changes and**

**schema changes in real time**

ement

> **Note:** Before synchronization, confirm the upstream and downstream storage supported by CTAS and CDAS. For example, MongoDB cannot be used as a sink table. An error occurs

|   | CREATE TABLE ... AS TABLE ... statement requires target catalog |
|---|---|
| ... implements org.apache.flink.table.catalog.CatalogTableProvider interface. |   |

CTAS supports single-table synchronization, schema change synchronization, merged synchronization of sharded databases and tables, and synchronization with custom computed columns. You can add new CTAS statements to data synchronization deployments. CDAS supports real-time synchronization of schemas and data at the database level, and synchronization of schema changes.

```
-- Synchronize a single table and synchronize schema changes and data changes at the ta ble level in real time. CREATE TABLE IF NOT EXISTS `<targetcatalog>`.`<targetdbname>`.`<targettablename>` WITH (...) AS TABLE `<mysqlcatalog>`.`<dbname>`.`<tablename>` /*+ OPTIONS('server-id'='6000-6018') */; -- Synchronize an entire database and synchronize schema changes and data changes at th e database level in real time. CREATE DATABASE `<targetcatalog>`.`<targetdbname>` WITH (...) AS DATABASE `<mysqlcatalog>`.`<dbname>` INCLUDING ALL TABLES /*+ OPTIONS('server-id'='6000-6018') */;
```

**Read data from a MySQL dimension table**

```
INSERT INTO `<othersinktable>` SELECT ... FROM `<othersourcetable>` AS e JOIN `<mysqlcatalog>`.`<dbname>`.`<tablename>` FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

**Write data to a MySQL table**

```
INSERT INTO `<mysqlcatalog>`.`<dbname>`.`<tablename>` SELECT ... FROM `<othersourcetable>`
```

### 6.4 Configure a session cluster

Session clusters are applicable only to testing. Do not use session clusters in the production environment. Session clusters do not support disaster recovery. You can deploy or debug deployments in a session cluster. This improves the resource utilization of JobManager and spins up the deployment startup.

**Background information**

Realtime Compute for Apache Flink supports per-job clusters and session clusters. The two types of clusters have the following differences: ement Per-job clusters: This is the default cluster type. Each deployment requires an independent JobManager to implement resource isolation between deployments. The resource utilization of JobManagers for deployments that involve a small amount of data is low. Therefore, this type of cluster is suitable for deployments that consume a large number of resources or deployments that run in a continuous and stable manner. Session clusters: This type of cluster allows multiple deployments to use the same JobManager, which increases the resource utilization of the JobManager. This type of cluster is suitable for deployments that consume only a few resources or deployments that frequently start and stop. This effectively reduces resource costs.

> **Note:** Session clusters do not support the autopilot feature.
> When you create a session cluster, the cluster resources are consumed regardless of whether you use the session cluster. The resource consumption is based on the configurations that you select when you create the cluster.

**Limits**

Session clusters have the following limits: You cannot change the Flink version for a session cluster that is suspended. You cannot decrease the number of TaskManagers or CUs for a session cluster that is suspended. Metrics of session clusters cannot be displayed. Session clusters do not support the monitoring and alerting feature. Realtime Compute for Apache Flink (Compute-storage Decoupled Edition) does not support disaster recovery.

**Precautions**

If a JobManager is faulty, all deployments of a cluster that runs on the JobManager are affected. If a TaskManager is faulty, the deployments that have tasks running on the TaskManager are affected. If processes are not isolated for tasks that run on the same TaskManager, the tasks may be affected by each other. If the session cluster uses the default configurations, take note of the following items: For a single small deployment, we recommend that the total number of such deployments in a cluster be no more than 100. For complex deployments, we recommend that the number of parallel deployments be no more than 512, and the number of clusters in which 64 medium-sized deployments run in parallel be no more than 32. Otherwise, issues such as heartbeat timeouts may occur, and the stability of the cluster may be affected. In this case, you must increase the heartbeat interval and heartbeat timeout period. If you want to run more tasks in parallel, you must configure more resources for the session cluster. We recommend that you do not run deployments in a session cluster for which Use for SQL Editor Previews is enabled. If you run deployments in a session cluster for which Use for SQL Editor Previews is enabled, you must stop the session cluster and manually configure the Flink engine when a new version is released. Otherwise, an error is returned during local debugging. ement

**Create a session cluster**

1. Go to the **Session Clusters** page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Workspaces**page, find the workspace and namespace that you want to manage and click **Console** in the **Actions** column.

| Administration | Session Clusters |
|---|---|

iii. In the left-side navigation pane, choose **Administration**Session Clusters.
2. In the upper-left corner of the Session Clusters page, click **Create Session Cluster**. Then,
configure the parameters. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Standar d | Name | Enter a name for the cluster. |
|   | State | Select a state for the cluster. Valid values: STOPPED: The cluster is stopped after it is configured, and the deployments in the cluster are also stopped. RUNNING: The cluster keeps running after it is configured. |
|   | Label key | You can configure labels for deployments in the Labels section. This allows you to find a deployment on the Overview page in an efficient manner. |
|   | Label value | None. |

ement

| Configur ation | Engine Version | Select the version of the Flink engine that is used by the current deployment. |
|---|---|---|
|   | Flink Restart Policy | Valid values: Failure Rate: The deployment is restarted if the number of failures within the specified interval reaches the upper limit. If you select this option, you must also configure the Failure Rate Interval, Max Failures per Interval, and Delay Between Restart Attempts parameters. Fixed Delay: Deployments are restarted at a fixed interval. If you select this option, you must also configure the Number of Restart Attempts and Delay Between Restart Attempts parameters. No Restarts: Deployments are not restarted if the task fails. Note If you leave this parameter empty, the default Apache Flink restart policy is used. In this case, if a task fails and checkpointing is disabled, the JobManager is not restarted. If you enable checkpointing, the JobManager is restarted. |
| Additional Configuration |   | Configure other Flink settings, such as taskmanager.numberOfTaskSlots: 1 . |
|   | Number of Task Managers | By default, the value is the same as the parallelism. |
|   | JobManager CPU Cores | Default value: 1. |
|   | JobManager Memory | Recommended value: 4 GiB. Minimum value: 1 GiB. Unit: GiB. Example: 1 GiB or 1.5 GiB. We recommend that you configure JobManager resources and heartbeat-related parameters for the JobManager. When you configure this parameter, take note of the following items: JobManagers provide features, such as TaskManager heartbeat, task serialization, and resource scheduling. Therefore, we recommend that the resource configuration for the JobManager be no less than the default configuration. Adjust the configuration based on your cluster workload. To ensure cluster stability, you must prevent heartbeat timeout that is caused by the busy main thread of the JobManager. Therefore, we recommend that you set the heartbeat.interval parameter to at least 10 seconds and the heartbeat.timeout parameter to at least 50 seconds. You can increase the values of these parameters based on the number of TaskManagers and the increase in the number of deployments. |
|   | TaskManager CPU Cores | Default value: 2. |

ement

| Resourc es |   |   |
|---|---|---|
|   | TaskManager Memory | Recommended value: 8 GiB. Minimum value: 1 GiB. Unit: GiB. Example: 1 GiB or 1.5 GiB. We recommend that you specify the number of slots for each TaskManager and the amount of resources that are available for TaskManagers. The number of slots is specified by the taskmanager.numberOfTaskSlots parameter. When you configure this parameter, take note of the following items: For a single small deployment, we recommend that you set the CPU-to-memory ratio of a single slot to 1:4 and configure at least 1 CPU core and 2 GiB of memory for each slot. For a complex deployment, we recommend that you configure at least 1 CPU core and 4 GiB of memory for each slot. If you use the default resource configuration, you can configure two slots for each TaskManager. We recommend that you use the default resource configuration for each TaskManager and set the number of slots to 2. Note Insufficient TaskManager resources affect the stability of the deployments that run on the TaskManager. In addition, configuring only a small number of slots underutilizes resources because the overhead of the TaskManager cannot be effectively spread across tasks. If you configure a large number of resources for a TaskManager, a large number of deployments run on the TaskManager. If the TaskManager is faulty, all the deployments are affected. |
| Logging | Root Log Level | Valid values: TRACE, DEBUG, INFO, WARN, and ERROR. |
|   | Logger name | Enter a name for the log. |
|   | Logger level | Select a log level. |
|   | Logging Profile | Select a log template. You can use the system template or configure a custom template. |

4. Click **Create Session Cluster**.
After the session cluster is created, click **Start**. After the session cluster is started, you can select the session cluster from the Deployment Target drop-down list when you create a deployment.

### 6.5 Security management

ement The security center of Realtime Compute for Apache Flink supports member management and secret hosting.

**Go to the security center**

1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Workspaces**page, find the workspace and namespace that you want to manage
and click **Console** in the **Actions** column.
3. In the left-side navigation pane, click **Security**.

**Manage members**

1. On the **Security** page, click the **Members** tab.

| mber | . In the |   |
|---|---|---|
| parameters. |   |   |

2. Click **Add Member**. In the **Add Member** dialog box, configure the **Role** and **Member**
**Information** parameters.
The following section describes parameters:

**Role**

Supported roles include **owner**, **editor**, and **viewer**. The following table describes the differences among the roles.

| Feature | owner | editor | viewer |
|---|---|---|---|
| View deployments | Y | Y | Y |
| Start and cancel deployments | Y | Y | N |
| Modify deployment configurations | Y | Y | N |
| Upload JAR packages | Y | Y | N |
| Write SQL statements | Y | Y | N |
| Create user-defined functions (UDFs) | Y | Y | N |
| Register metadata | Y | Y | N |
| View deployment templates | Y | Y | Y |
| Add, delete, or modify deployment templates | Y | Y | N |

ement

| Manage members | Y | N | N |
|---|---|---|---|

**Member Information**: In the upper-right corner of the Apsara Uni-manager
Management Console, click the profile picture of the current user to view the **UID**.

> **Important:** A member that has already been added cannot be added again.

3. Click **OK**.

| the role in the | Actions | column. |
|---|---|---|

After you add the role, you can **modify** and **delete** the role in the **Actions** column.

**Host secrets**

1. In the left-side navigation pane, click Security. On the **Security** page, click the **Secret**
**Values** tab.
2. Click **Add Secret Value**.
3. In the **Add Secret Value** dialog box, configure the secret information.

| Parameter | Description |
|---|---|
| Secret Name | You can enter a custom name that meets the following requirements: The name can be up to 64 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ |
| Secret Value | Enter the value of the key. |

4. Click **OK**.
To delete a secret, click **Delete** in the **Actions** column.

### 6.6 Configure an external storage IP address

**IP address**

This topic describes how to configure an external storage IP address to allow the outbound traffic of deployments.

**Background information**

To prevent the security vulnerabilities caused by unauthorized outbound access, Realtime Compute for Apache Flink enables the NetworkPolicy feature. By default, this feature blocks the outbound traffic of all deployments. To allow the outbound traffic of deployments, you must configure an external storage IP address and add the IP address to the whitelist. The NetworkPolicy feature uses the following default rules: Blocks all outbound traffic. Allows mutual access between pods in the same namespace. Allows access to the Hadoop Distributed File System (HDFS) deployed in the Ververica namespace. ement Allows access to APIServer. Allows access to CoreDNS. Allows access to Cloud Monitor to report metric data.

**Limits**

If you upgrade Realtime Compute for Apache Flink to version 3.18.1 or later, or deploy Realtime Compute for Apache Flink of version 3.18.1 or later, the NetworkPolicy feature is enabled for all namespaces by default. Therefore, you need to configure an external storage IP address to allow outbound traffic.

**Limits**

After a namespace is created, **Configure IP Address for External Data Store** is displayed in the Operate column of the namespace on the Namespace page. This button is displayed only if you have the same permissions as on the **Modify CU** button. In other words, you must have permission to modify the namespace. Otherwise, the button is dimmed. The IP addresses or CIDR blocks that you add to the whitelist cannot overlap with those in the blacklist. Otherwise, an error message is returned.

**Procedure**

1. Log in to the Realtime Compute for Apache Flink console.
2. On the **Namespace** page, find the namespace that you want to manage and click
**Configure IP Address for External Data Store** in the **Operate** column.
3. Click **+ IP Address**, enter an IP address, and then click **OK**.
The IP address is the virtual IP address (VIP) of the storage service. You can add a single IP address or a CIDR block in the CIDR notation, such as `192.168.0.1` and `192.168.0.1/24` . If the format of the IP address is invalid, an error message is returned, as shown in the following figure.
4. Click **OK**.

**Example**

Create and start a deployment for a DataHub result table without configuring an external storage IP address. A network connection error is returned. ement After an external storage IP address is configured, the deployment runs as expected.

### 6.7 Deployment logs

#### 6.7.1 View startup and running logs

When a deployment is in the running state, you can view its startup and running logs. This topic describes how to view startup and running logs.

**Background information**

ement

| Type | Description |
|---|---|
| Startup log | Logs generated after a Flink deployment starts, covering the period from when the Flink environment initializes until the Job Manager starts. Note The startup logs do not include scheduling logs. You must view scheduling-related logs in the operational events. For example, insufficient resources or insufficient switch IP addresses are scheduling issues. |
| Running log | You can view logs of the Flink Job Manager and Task Managers on the deployment log page or in the Flink UI. |

**Prerequisites**

The deployment is in the running state.

**Notes**

Logs support pagination. Each page displays 1 MB of logs, approximately 8,000 to 9,000 lines, which is generally sufficient for troubleshooting. If you do not locate the issue on the first page, switch pages to view more logs.

**View startup logs**

1. Go to the **Deployments** page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. On the **Logs** tab, click **Startup Logs** on the left to view the startup logs.

**View running logs**

**View running logs on the deployment log page**

1. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
ement
2. On the **Logs** page, go to the **Running Logs** tab. Click the drop-down list next to **Job** and
select a running deployment.
3. View logs of the Job Manager and Task Managers.
View Job Manager logs On the **Job Manager** tab, click **Logs**. View Task Managers logs a. On the **Running Task Managers** tab, click **Path, ID**. ement b. Click **Logs**.

**View running logs in the Flink UI**

1. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. In the **Actions** row of the **Status** tab, click **Flink UI** to enter the **Overview** page of
**Apache Flink Dashboard**.

> **Note:** The **Flink UI** entry appears only when the deployment state is **RUNNING**.

3. In the left-side navigation pane, click **Task Managers** or **Job Manager**.
After you click **Task Managers**, click the target **Path, ID**. On the **Logs** tab, view the Task Manager logs of the deployment. After you click **Job Manager**, on the **Logs** tab, view the Job Manager logs of the deployment.

#### 6.7.2 View running exception logs

When a deployment fails to start or encounters a running exception, you can view the running exception logs to troubleshoot the issue. This topic describes how to view Job Manager exceptions, logs of failed Task Managers, and logs of Task Managers associated with slow checkpoints.

**Background information**

| Type | Description |
|---|---|
| Job Manager exceptions | If a deployment undergoes failover and fails to run, check the Job Manager exception. Note If the Job Manager fails to start, this is not classified as a Job Manager exception. Check the startup logs instead. |

ement

| Logs of failed Task Managers | Deployments in normal running state do not have failed Task Managers. However, for deploymentss with higher risk levels, Task Managers may fail but restart automatically. In such cases, review archived logs of the failed Task Managers to identify potential causes. Note You can view failed Task Managers logs only after enabling log archiving. Additionally, you can access only logs within the retention period configured in log archiving settings. |
|---|---|
| Logs of Task Managers associated with slow checkpoints | During deployment execution, if a checkpoint takes an unusually long time to complete, review the logs of its associated Task Manager to determine the root cause. |

**Prerequisites**

The deployment instance must be in the running state.

**Notes**

Logs support pagination. Each page displays 1 MB of data, approximately 8,000–9,000 lines, which is generally sufficient for troubleshooting. If you do not locate the issue on the first page, switch pages to view more logs.

**View Job Manager exceptions**

1. Go to the **Deployements** page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. On the **Logs** tab, select the **JM Exceptions** tab on the left to view Job Manager exceptions.

> **Note:** In the **Exception History** section, you can view exceptions generated within the last seven days and filter by exception type to view history exceptions.

**View logs of failed Task Managers**

1. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. On the **Logs** tab, select **Running Logs**, then select a running job instance.
3. Click the **Failed Task Managers** tab to view logs of failed Task Managers.

**Locate slow checkpoints and view logs of corresponding Task**

**Managers**

1. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. Review slow checkpoint log information.
i. On the **Deployments** tab, click the **Checkpoints** tab, then click **Checkpoints History**. ement ii. Review values under the **End to End Duration** column to identify the ID of the slow checkpoint. iii. Click to the left of the slow checkpoint's ID to confirm the Operators node associated with the slow checkpoint. iv. Click to the left of the Operators node to expand and view details for each SubTask. v. Click the **ID** corresponding to the SubTask associated with the slow checkpoint. vi. On the redirected page, go to the **Running Task Managers > Logs** tab to review the slow checkpoint log information. ement

#### 6.7.3 View historical deployment instance logs

**logs**

When the Flink UI is inaccessible or you need to analyze running issues with historical deployments, view the historical deployment instance logs to locate the problem. This topic describes how to view historical deployment instance logs on the deployment log page.

**Background information**

You must view logs of historical deployment instances in the following scenarios: You need to view, search, and analyze running logs of historical deployment instances. By default, the system retains the most recent 5 MB of running logs. The Flink UI is inaccessible, and you need to view JobManager logs to locate the issue.

**Prerequisites**

To view historical deployment instance logs, you must enable log archiving in the log configuration. The system enables log archiving by default, and retains archived logs for seven days.

**Notes**

When a log file reaches the specified size, the system automatically archives the log by default and periodically deletes log files that exceed the archive retention period. After a deployment stops, uncleaned archived logs are retained and not automatically deleted. If you delete a deployment, its corresponding logs are also deleted. By default, the log configuration retains two files, each 5 MB in size. We recommend that you do not modify this value. ement

> **Note:** The number of files shown in the image does not include the file currently being written. For example, if you configure this parameter as 1, the system saves up to two files: one in memory and one on your local disk.

**View logs on the deployment log page**

1. Go to the **Deployments** page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. On the **Logs** tab, click **Running Logs** on the left.
3. Click the drop-down list next to **Job** and select a history job.
4. View Job Manager and Task Managers logs.
ement On the **Job Manager** or **Task Managers** tab, click the corresponding log name to view it.

#### 6.7.4 Modify the log level for a running deployment

**deployment**

When logs at the INFO level cannot meet your troubleshooting needs, you can change the log level to DEBUG. This topic describes how to dynamically modify the log level, and provides usage limits and notes.

**Background information**

The system supports log levels in ascending order, as listed in the following table.

| Level | Description |
|---|---|
| DEBUG | Logs that record the system operating status. |
| INFO | Logs about important or interesting information. |

**Limits**

You can set the log level only to INFO or DEBUG, and cannot set it to other levels to avoid failure to locate root causes due to excessively high log levels. You can modify the log level for the entire JobManager (JM). You can modify the log level for a single TaskManager (TM), but not for all TMs at once. To modify the log level for all TMs, you must configure each TM separately.

**Notes**

After you set the log level to DEBUG, the system prints logs at the DEBUG, INFO, WARN, and ERROR levels. After you set the log level to INFO, the system prints logs only at the INFO, WARN, and ERROR levels. Changing the log level affects only newly generated logs. Previously generated logs remain unchanged. Enabling DEBUG logs slightly affects deployment performance. We recommend that you set the log level to INFO unless you need to troubleshoot issues.

**Procedure**

1. Go to the **Deployments** page.
i. Log in to the Realtime Compute for Apache Flink console. ii. On the **Deployments** page, click the name of the target deployment to enter the
**deployment details** page by default.
2. On the **Logs** tab, click **Running Logs** on the left-side navigation pane, and select a
running deployment instance.
3. Modify the log level for the Job Manager or Task Managers.

**Modify the log level for Job Manager**

a. On the **Job Manager** tab, click **Logs**. ement b. Click **Edit** to the right of **Log Level**. c. Click **OK**. d. Select the target log level from the drop-down list. e. Click **Confirm**.

**Modify the log level for Task Managers**

a. On the **Running Task Managers** tab, click **Path, ID**. b. Click **Logs**. c. Click **Edit**to the right of **Log Level**. d. Click **OK**. e. Select the target log level from the drop-down list. f. After you modify the log level, click **Confirm**.

#### 6.7.5 View Flink audit events

This topic describes how to view Flink audit events by using Apsara Stack Security - Security Audit.

**Background information**

Apsara Stack Security helps you monitor and record activities of your Alibaba Cloud account. You can download these event logs or save them to Simple Log Service (SLS) for behavior analysis, security analysis, resource change tracking, and compliance auditing. ement

**Procedure**

1. Log in to the Apsara Uni-Manager Operations Console.
2. In the top navigation bar, hover the mouse over **Security Management**, select **Security**
**Audit > Apsara Stack Security - Security Audit** . The system navigates to the **Security**
**Audit** page by default.
3. On the **Security Audit** page, click the **Raw Logs** tab.
4. Set **Audit Type** to **Cloud Product**, set **Audit Target** to **vvp_OPERATE_LOG**, specify the
**Start At**, and then click **Search**.

**FAQ**

Q: Why does not the Raw Logs section display any data after I enter the audit page? A: This may occur for one of the following reasons: You did not perform any operations on the vvp platform during the queried time period. You performed operations on the vvp platform, but log reporting may have failed. Contact Alibaba Cloud technical support for troubleshooting guidance. Q: Why are raw logs present but no audit data displayed after I enter the audit page? A: This may occur for one of the following reasons: You did not perform any high-risk operations during the queried time range. You performed high-risk operations, but the daily log audit quota for Apsara Stack Security has been reached. Contact the Apsara Stack Security team to increase the daily audit quota. rver

## 7 Flink MCP Server

Powered by the MCP protocol, Flink enables users to retrieve information such as namespaces and deployments by calling APIs through Apsara Copilot in Hosting mode. Alternatively, users can deploy their own MCP Server for queries. This empowers users to build natural language-driven data query agents, enabling an intelligent data processing workflow from natural language queies to visualization. This topic describes how to use Apsara Copilot in Hosting mode and how to deploy your own MCP Server.

**Supported MCP modes**

Apsara Copilot - Hosting mode The Apsara Copilot in Hosting mode is an out-of-the-box feature requiring no user configuration. You can access it directly through a large language model. Deploy your own MCP Server You can deploy it independently within your applications, agents, or AI systems.

**Apsara Copilot - Hosting mode**

> **Note:** Before using Apsara Copilot in Hosting mode, refer to the **Apsara Uni-manager** **Management Console > Apsara Copilot User Guide** to enable Apsara Copilot.

1. Procedure.
2. View the preset MCP list provided by the system.
In the left-side navigation pane, select **AI Hub > AI-Native API: MCP Service** to view the system's preset MCP list. The current preset tools are as follows:

| Tool name | API | Description |
|---|---|---|
| Engine version list query | ListFlinkVersions | List all Flink engine versions supported in the specified namespace. This helps users select an appropriate engine to create and run deployments. |
| Workspace list query | DescribeWorkspacesFlin kOnOss | Query the list of workspaces for the current user. This helps users manage workspaces and optimize resource management. |
| Query namespaces under a workspace | ListNamespacesByWorks paceIdFlinkOnOss | Query the list of namespaces under the specified workspace. This helps users manage namespaces and optimize resource allocation and management. |
| Query a user's full namespace list | DescribeNamespacesFlin kOnOss | Query the full list of namespaces for the specified user. This helps users manage namespaces and optimize resource allocation and management. |

rver

| Job list query | ListJobs | Query the deployment list by specifying the namespace name. This helps users manage deployments and optimize deployment resources and execution plans. |
|---|---|---|
| Query job deployment list | ListDeployments | Query the list of deployed drafts by specifying the namespace name. This helps users manage deployments and optimize deployment resources and execution plans. |
| User resource query | ListArtifacts | List user resources in the specified namespace and workspace. This helps users manage deployments and optimize deployment resource management. |

3. Use Apsara Copilot to invoke preset tools.
i. At the top of the page, click the icon in the toolbar to go to the **Apsara Copilot** page. ii. At the bottom of the dialog box, click the icon to turn on the **MCP** switch. Then, click the icon to open the **Select MCP** page. iii. Select an existing Flink MCP. iv. Click **OK** to return to the dialog box. Use natural language to describe your query, for example, "Query the list of workspaces for the current user". v. Click the icon on the right to send and execute the command. vi. Wait for the task to complete. You can then view the returned result information.

**Deploy your own MCP Server**

1. Download the MCP service package.
2. Deploy it on ECS, containers, or external cloud servers.
3. Integrate into applications or agents: Embed the MCP as a backend service into AI
applications, agents, or RPA workflows.
4. Call the MCP feature through RESTful APIs.
