---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Static Data Masking and Watermarking User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 150
source_pdf: "f4f5c6a248397f56_Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Static Data Masking and Watermarking User Gui"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AE%A1%E8%AE%A1%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Database%20Audit%20Static%20Data%20Masking%20and%20Watermarking%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Static Data Masking and Watermarking User Guide 20260831

## Table of Contents

- 1 Usage notes
- 2 Getting Started
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
  - 2.3 Deploy the Static Data Masking and Watermarking system
  - 2.4 Log in to the Static Data Masking and Watermarking system
  - 2.5 Upgrade instance specifications
  - 2.6 Basic data masking process
    - 2.6.1 Data masking workflow introduction
    - 2.6.2 Database masking
    - 2.6.3 File masking
  - 2.7 Advanced data masking operation guide
    - 2.7.1 Subset filtering
    - 2.7.2 Expression configuration
    - 2.7.3 Incremental data masking
    - 2.7.4 Composite masking algorithm
    - 2.7.5 Data Masking with Hybrid Masking Algorithm
    - 2.7.6 Data dictionary masking
    - 2.7.7 Text masking algorithm
    - 2.7.8 Group dictionary data masking
- 3 User Guide
  - 3.1 Terms
  - 3.2 Data sources
    - 3.2.1 Database sources
      - 3.2.1.1 Add a database source
      - 3.2.1.2 Modify a database source
      - 3.2.1.3 Delete database sources
      - 3.2.1.4 Query a database source
    - 3.2.2 File sources
      - 3.2.2.1 Add a file source
      - 3.2.2.2 Modify a file source
      - 3.2.2.3 Delete file sources
      - 3.2.2.4 Query a file source
  - 3.3 Data discovery
    - 3.3.1 Discovery tasks
      - 3.3.1.1 Add a data discovery task
      - 3.3.1.2 View the details of a data discovery task
      - 3.3.1.3 Execute a data discovery task
      - 3.3.1.4 Stop a data discovery task
      - 3.3.1.5 Modify a data discovery task
      - 3.3.1.6 Delete data discovery tasks
      - 3.3.1.7 View the execution records of a data discovery task
    - 3.3.2 Sensitive field sorting
      - 3.3.2.1 Add sensitive data sources
      - 3.3.2.2 Verify sensitive data fields
      - 3.3.2.3 Specify sensitive data fields as non-sensitive data fields
      - 3.3.2.4 Confirm the changes of sensitive data types of data fields
      - 3.3.2.5 View field sample data
    - 3.3.3 Sensitive file sorting
      - 3.3.3.1 Verify file columns of sensitive file types
      - 3.3.3.2 Modify sensitive data types of multiple file columns at a time
      - 3.3.3.3 Confirm the changes of sensitive data types of file columns
      - 3.3.3.4 View file sample data
    - 3.3.4 Sensitive field templates
  - 3.4 Data masking
    - 3.4.1 Data subsets
      - 3.4.1.1 Add a data subset
      - 3.4.1.2 Modify a data subset
      - 3.4.1.3 Delete a data subset
      - 3.4.1.4 Manage data tables in a data subset
      - 3.4.1.5 Manage constraints of a data subset
    - 3.4.2 Solution management
      - 3.4.2.1 Add a masking policy
      - 3.4.2.2 View the details of a data masking solution
      - 3.4.2.3 Modify a data masking solution
      - 3.4.2.4 Delete a data masking solution
      - 3.4.2.5 Manage data subsets of a data masking solution
      - 3.4.2.6 Manage masking algorithms of a data masking solution
      - 3.4.2.7 Manage the grouping dictionary column configuration of a data masking solution
      - 3.4.2.8 Manage expressions of a data masking solution
      - 3.4.2.9 Configure a whitelist for a data masking solution
      - 3.4.2.10 Configure a blacklist for a data masking solution
    - 3.4.3 Data masking tasks
      - 3.4.3.1 Create a data masking task
      - 3.4.3.2 Modify a data masking task
      - 3.4.3.3 Delete a data masking task
      - 3.4.3.4 Execute or stop a data masking task
      - 3.4.3.5 View the execution records of a data masking task
      - 3.4.3.6 View the details of a data masking task
      - 3.4.3.7 View the progress of a data masking task
    - 3.4.4 Automatic data masking tasks
      - 3.4.4.1 Create an automatic data masking task
      - 3.4.4.2 Modify an automatic data masking task
      - 3.4.4.3 Execute an automatic data masking task
      - 3.4.4.4 Delete an automatic data masking task
      - 3.4.4.5 View the execution records of an automatic data masking task
  - 3.5 Data watermarking
    - 3.5.1 Watermarking tasks
      - 3.5.1.1 Create a watermarking task
      - 3.5.1.2 Modify a watermarking task
      - 3.5.1.3 Execute a watermarking task
      - 3.5.1.4 View the details of a watermarking task
      - 3.5.1.5 Stop a watermarking task
    - 3.5.2 Data subsets
    - 3.5.3 Watermarking solutions
      - 3.5.3.1 Create a watermarking solution
      - 3.5.3.2 Modify a watermarking solution
      - 3.5.3.3 Delete one or more watermarking solutions
      - 3.5.3.4 View the details of a watermarking solution
    - 3.5.4 Pseudo-column field management
      - 3.5.4.1 Add a pseudo-column field
      - 3.5.4.2 Modify a pseudo-column field
      - 3.5.4.3 Delete one or more pseudo-column fields
      - 3.5.4.4 View the details of a pseudo-column field
    - 3.5.5 Distribution object management
      - 3.5.5.1 Add a distribution object
      - 3.5.5.2 Modify a distribution object
      - 3.5.5.3 Delete one or more distribution objects
      - 3.5.5.4 View the details of a distribution object
    - 3.5.6 Data distribution management
  - 3.6 Data provenance
    - 3.6.1 Add a provenance task
    - 3.6.2 Execute a provenance task
    - 3.6.3 Stop a provenance task
    - 3.6.4 Modify or delete a provenance task
    - 3.6.5 View a provenance task
  - 3.7 K Anonymous Privacy Protection
    - 3.7.1 K-anonymity overview
    - 3.7.2 K-value calculation
    - 3.7.3 Anonymization tasks
  - 3.8 Column-level encryption
    - 3.8.1 Set column encryption
    - 3.8.2 Configure database account permissions
    - 3.8.3 Column encryption overview
    - 3.8.4 Run an encryption task
    - 3.8.5 Set encryption rules
    - 3.8.6 Download encryption logs
  - 3.9 Configurations
    - 3.9.1 Lookup table management
    - 3.9.2 Data dictionary
    - 3.9.3 Custom functions
    - 3.9.4 Discovery rules
    - 3.9.5 Data masking algorithm
    - 3.9.6 Scheduled tasks
    - 3.9.7 Queue tasks
    - 3.9.8 Masking algorithm templates
    - 3.9.9 File templates
    - 3.9.10 Parameter configuration
    - 3.9.11 Database driver management
    - 3.9.12 Host configuration
  - 3.10 Maintenance

## 1 Usage notes

Before you log on to Apsara Stack Security Center, you must verify that your computer meets the configuration requirements. For more information about the configuration requirements, see . Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

d

## 2 Getting Started

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles in Apsara Stack Security Center are provided by default. You cannot create custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see Default roles in Apsara Stack Security. Table 1. Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| Organization security administrator | Uses SOC to manage the security of hosts, applications, and networks for an organization. This role also manages security products related to Elastic Compute Service (ECS). |
| Global organization security administrator | Uses SOC to conduct security management for Apsara Stack and all tenants, and manages security products related to ECS. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. To configure the Cloud Security system, you must log on with a global organization security administrator account. We recommend that you use the Google Chrome browser.
1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. d

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
> **Forgot password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

### 2.3 Deploy the Static Data Masking and Watermarking system

**Masking and Watermarking**

**system**

This topic describes how to deploy the Static Data Masking and Watermarking system.

**Prerequisites**

Your account is granted the permissions on the cloud resources of your department. For example, you have the permissions of the administrator role in your department.

**Background information**

The Static Data Masking and Watermarking system is deployed on Apsara Stack servers as an image. The Static Data Masking and Watermarking system can detect databases in the environment and provides data masking and watermarking features. d
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, choose **Security > Data Security > Static Data**
**Masking and Watermarking**. On the **Static Data Masking and Watermarking** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Static Data Masking and Watermarking** .
4. Click **Create Instance**. In the **Create Instance** panel, create a Static Data Masking and
Watermarking instance.

| Section and parameter | Description |
|---|---|
| Organization | The organization to which the instance belongs. |
| Resource Set | The resource set to which the instance belongs. |
| VPC ID | The ID of the virtual private cloud (VPC) in which the instance resides. |
| vSwitch ID | The ID of the vSwitch to which the instance belongs. |
| Package specifications | Data Masking,Watermarking Standard Edition: supports an instance with 8 vCPUs, 16 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 1 to 10 database instances. Data Masking,Watermarking High-Configuration Edition: supports an instance with 16 vCPUs, 32 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 10 to 20 database instances. Data Masking,Watermarking Top-Configuration Edition: supports an instance with 24 vCPUs, 48 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 20 to 30 database instances. |

d

| Database Instance Quota | The quota of the instance. The value must be greater than 3. Important Total quota = Instance quota * Number of features of the instance. |
|---|---|
| Disaster Recovery | Disabled: The disaster recovery feature is not enabled. Single Data Center: Disaster recovery in a single data center is supported. |
| Select an instance feature | Available options include the Data Masking, Data Watermarking, Column Encryption, and Anonymization features. You can select one or more features. |

5. Click **OK**. The instance is created.

### 2.4 Log in to the Static Data Masking and Watermarking system

**Masking and Watermarking**

**system**

This topic describes how to log in to the Static Data Masking and Watermarking system from the Apsara Uni-manager Management Console.

**Prerequisites**

Your account is granted the permissions on the cloud resources of your department. For example, you have the permissions of the administrator role in your department.

**Background information**

The Static Data Masking and Watermarking system allows you to perform data processing operations on the databases in your department, such as data extraction, data masking, and data hiding.
1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, choose Security > **Data Security > Static Data Masking and**
**Watermarking**. On the Static Data Masking and Watermarking page, select a region from
the Region drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Static Data Masking and Watermarking** .
4. On the Static Data Masking and Watermarking page, find the Static Data Masking and
Watermarking instance that you want to manage and click **Details** in the Actions column to go to the Static Data Masking and Watermarking system.

### 2.5 Upgrade instance specifications

**specifications**

d If the current instance cannot meet your business requirements, you can upgrade your instance on the Static Data Masking and Watermarking page. This topic describes how to upgrade the specifications of a Static Data Masking and Watermarking instance.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, choose **Security** > **Data Security > Static Data**
**Masking and Watermarking**. On the **Static Data Masking and Watermarking** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. On the **Static Data Masking and Watermarking** page, find the instance that you want
to manage and click **Settings** in the **Actions** column.
4. In the **Configure Instance** panel, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Instances Name | The name of the instance that you want to upgrade. |
| Package specifications | The new specification of the instance. Valid values: Data Masking,Watermarking Standard Edition: supports an instance with 8 vCPUs, 16 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 1 to 10 database instances. Data Masking,Watermarking High-Configuration Edition: supports an instance with 16 vCPUs, 32 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 10 to 20 database instances. Data Masking,Watermarking Top-Configuration Edition: supports an instance with 24 vCPUs, 48 GB of memory, a 100 GB system disk, and a 500 GB data disk. We recommend that you use it to mask 20 to 30 database instances. Important You can upgrade your instance only to a higher specification. You cannot roll back the upgrade. Proceed with caution. The upgrade process involves a downtime during which the instance is stopped and being upgraded. The instance is unavailable during the downtime. |
| Database Instance Quota | The quota of the database instances. You must configure this parameter based on the rules of the selected instance edition. |
| Disaster Recovery | Specifies whether to support disaster recovery. Valid values: Disabled and Single Data Center. |
| Data Masking |   |

| tabase Audit | Static Data Masking and Waterm arking User Guide·Getting Start |
|---|---|
|   | You can add a new feature, but not remove an existing one. |
| Data Watermarking |   |
| Column Encryption |   |
| Anonymization |   |

d

### 2.6 Basic data masking process

#### 2.6.1 Data masking workflow introduction

This topic describes the data masking workflow.

**Data masking workflow**

1. Create a data source or file source.
If the target is a database different from the source, create an additional data source as the masking destination.
2. Run a discovery task to identify sensitive data in the source.
3. Review and classify sensitive data.
Manually verify and label sensitive columns identified by the system to ensure accuracy.
4. Create and run a masking task.
Define masking rules based on the classification results, execute the masking job, and write the sanitized data to the target database or generate a new file.

**Workflow diagram**

**Discovery**

**Data**

**Data**

**Source**

**Task**

**masking**

**task**

Data subset Sensitive field Source Database inventory Discovery Task Masking scheme Source Object Sensitive Object inventory task

#### 2.6.2 Database masking

Database masking process: Create a data source, create and execute a discovery task, and then verify sensitive fields. After the sensitive fields are verified, you can directly create a data masking task. When you create the task, you can configure a masking algorithm for the tables and sensitive fields to be masked. Alternatively, you can manually create a data subset and a data masking solution, and then create a data masking task. When you create the task, you can use an existing data masking solution.
1. Log in to Static Data Masking and Watermarking (DMS).
d
2. Click **Data Sources**. Then, click the **Database Sources** tab. On the **Database Sources**
tab, click **Create Database Source** above the database source list. In the Create Database Source dialog box, configure the database information as prompted and click
**Save**.
3. In the message that appears, click **Create Discovery Task**.
4. On the **AddDiscovery Task** page, select the tables to be discovered by the discovery task
and click **Next**. Then, select the discovery rules that are used by the discovery task and click **Save and Run**.
5. After the discovery task is executed, find the discovery task and click **Verify sensitive**
**data** in the Operation column.
6. In the **Sensitive Data List** section of the **Sensitive Field Analysis** tab, check the
sensitive data type of the fields, select the fields that you want to verify, and then click
**Verify fields** in the upper-right corner of the list. If the verification results of the fields
change to **Verified**, click **Complete carding**.
7. In the message that appears, click **Add desensitization task**.
8. On the Add Mask Task page, perform the following steps to configure the data masking
parameters. The scope of the tables to be masked in the data masking task is fixed to the tables discovered by the discovery task. i. Select a masking method and a lookup table. Then, click **Next**. ii. Specify masking algorithms for the sensitive columns to be masked and click **Next**. iii. Configure the masking destination parameters and click **Next**. By default, the masking destination is a database. You can change the masking destination to a local file or a remote file. If the masking destination is changed to a file, the data masking task is database-to-file masking.

> **Important:** In this step, you must verify the schema name before you click **Next**. If you enter the schema name of an Oracle database, the schema name must be in uppercase.

iv. Select an exception handling method and click **Save and Execute** to execute the data masking task. After the data masking task is executed, you can find the masked table that has the same name as the original table in the specified destination database to which the masked data is saved.

#### 2.6.3 File masking

File masking process: Create a file source, upload a file to the specified location, specify a file template, create and execute a discovery task, and then verify a sensitive file. After the sensitive file is verified, you can directly create a data masking task. When you create the task, you can configure a masking algorithm for sensitive columns. Alternatively, you can manually create a data masking solution and then create a data masking task. When you create the task, you can use an existing data masking solution. 1.
2. Click **Data Sources**. Then, click the **File Sources** tab. On the File Sources tab, click
**Create File Source**.
3. In the Create File Source dialog box, configure the **File Type** and **Upload Type**
parameters, upload a file, and then click **Next**. d
4. Configure a file template based on the uploaded file and click **Save**. In the message that
appears, click OK.
5. On the File Sources tab, find the file source that you created and click **Create Discovery**
**Task** in the Oper column. On the discovery task configuration page, select the file to be
discovered by the discovery task and click **Next**. Then, select the discovery rules that you want to use and click **Save and Run**.
6. After the discovery task is executed, find the discovery task and click **Verify sensitive**
**data** in the Operation column.
7. On the Sensitive File Analysis tab, check the sensitive data types of the file columns, select
the sensitive columns that you want to verify, and then click **Verify fields** to verify the sensitive columns.
8. If the verification results of the sensitive columns change to Verified, click Complete
carding.
9. In the message that appears, click Add desensitization task.
0. On the Add Mask Task page, perform the following steps to configure the data masking
parameters: i. Select a lookup table and click **Next**. ii. Specify masking algorithms for the sensitive columns to be masked and click **Next**. iii. Set the Output Target parameter to Local File or Remote File and click Next. By default, the masking destination is a database. If the masking destination is a database, the data masking task is file-to-database masking. In this case, you must specify the table to be imported to the database for each file. d iv. Select an exception handling method and click Save and Execute to execute the data masking task.
1. After the data masking task is executed, click **Data Masking**. Then, click the **Masking**
**Tasks** tab. On the Masking Tasks tab, find the data masking task and click History in the
Oper column to download the masked file.

### 2.7 Advanced data masking operation guide

**operation guide**

#### 2.7.1 Subset filtering

DMS allows you to configure filter conditions for tables in a data subset within a data masking scheme. The system masks only the data in the source table that meets specific conditions. This topic describes how to configure subset filtering.

**Considerations**

**Supported scope**:
Database source: Supported for cross-schema masking. Not supported for source schema masking. File source: Not supported.
**Prerequisites**: Before you use the subset filtering feature, you must complete sensitive
data discovery, manually create a data subset and a masking scheme. Do not skip these steps and directly create a masking task.

**Masking effect**

After you configure filter conditions by using the subset filtering feature, the target table contains only masked data that meets the filter conditions. d For example, the following figure indicates that the system masks only data whose ID is greater than 3. The masking effect is as follows:

**Prerequisites**

Complete the following operations before you configure subset filtering:
1. Add a database source.
2. Add a data discovery task.
3. Verify sensitive data fields.
4. Add a data subset.
5. Add a masking policy.

**Configure subset filtering**

1. Select **Data Masking > Solution Management**.
d
2. Select **Database Project**, and click the
icon next to the specified data subset on the
**Data subset** tab.
3. Configure filter conditions.
d
4. Select the field for which you want to configure filter conditions and configure expressions
as needed.
5. After you save the configuration, the configured filter conditions appear in the filter
condition list. You can also configure logical combinations for multiple filter conditions. d
6. If built-in conditions cannot meet your requirements, you can use extended conditions to
supplement the configured filter conditions.
7. Click **Save** to complete the configuration of filter conditions for the data subset.
8. Create a data masking task when you use the preceding masking scheme.
d

#### 2.7.2 Expression configuration

DMS supports setting expression configurations (using JavaScript syntax) during data masking. These expressions set the value of a specified column to a fixed value or calculate it based on other columns. If an expression references a column that has already been masked, the calculation uses the masked value. This article describes how to configure these expressions.

**Important notes**

**Supported scope**:
Database source: Source schema masking is not supported; cross-schema masking is supported. File source: Supported.
**Prerequisites**: Before using the expression configuration feature, you must complete
sensitive data identification and manually create a data subset and a masking policy. You cannot skip these steps and create a masking task directly.

**Masking effect**

For example, configure the SEX and AGE columns in the original table using the expression configuration feature. Set the AGE column to a random number between 1 and 100, and randomly populate the SEX column with gender values. Masking effect: d

**Prerequisites**

1. Add a database source or Add a file source.
2. Add a data discovery task.
3. Complete sensitive field type verification or Verify file columns of sensitive file types.
4. Add a data subset.

> **Note:** If the data source is a file, you do not need to perform this operation.

5. Add a masking policy.

**Steps to configure expressions**

1. Select **Data Masking > Solution Management**.
2. In the **Project list**, select a masking policy and click the **Expression config** tab.
3. Configure the expression.
d After you configure the expression, the masking result follows the expression settings. You can switch operators and built-in functions (attributes) via buttons.
4. Click **Save** to complete the expression configuration.
5. Create a data masking task using the above masking policy.

#### 2.7.3 Incremental data masking

DMS allows you to specify an auto-increment column in a masking scheme as the incremental masking column. Each time you run a masking task, DMS records the current maximum value of this column. The next time you run the same masking task, DMS masks only data whose value in this column is greater than the recorded maximum value. This achieves incremental masking. This topic describes how to configure incremental data masking.

**Notes**

**Supported scope**:
Database source: Cross-schema masking is supported. Source schema masking is not supported. File source: Not supported.
**Prerequisites**: Before you use the incremental masking feature, you must complete
sensitive data identification and manually create a data subset and a masking scheme. You cannot skip these steps and directly create a masking task.

**Masking effect**

d For example, when you run a masking task for the first time, the source table contains five rows of data. DMS records the maximum value of the incremental column at that time. After masking, the destination database contains five masked rows. When you run the masking task for the second time, the source table contains eight rows, meaning three new rows have been added. DMS filters out rows where the incremental column value is greater than the maximum value recorded during the previous masking task. DMS masks only these newly added three rows.

**Prerequisites**

Before you configure incremental data masking, you must complete the following operations:
1. Add a database source.
2. Add a data discovery task.
3. Verify sensitive data fields.
4. Add a data subset.
5. Add a masking policy.

**Configure incremental data masking**

1. When you configure Subset filtering, select **Set to Incremental**.
2. When you configure Create a data masking task, perform the following operations in the
**Destination parameter** section.
i. Change the **Table Processing** method to **If the table already exists, add data to it** . d ii. In the **Incremental configuration** step, specify the **Incremental value**.

> **Note:** The incremental value ensures that DMS masks only rows where the field value is greater than this value. For the first run, you can set this value to a number smaller than the current minimum value to mask all existing data in the table. After the masking task runs, DMS automatically updates this value to the maximum value recorded at that time. DMS uses this updated value to identify incremental data during subsequent masking runs.

#### 2.7.4 Composite masking algorithm

Use a custom composite masking algorithm to handle scenarios where a single column contains multiple types of sensitive data (for example, “Name|Phone Number”). This algorithm works with a custom composite discovery rule to split the data by delimiter or fixed position and apply different masking strategies to each sensitive field, enabling precise masking of complex-format data. This topic describes how to configure a composite masking algorithm.

**Notes**

You must have a corresponding custom composite discovery rule before you create a custom composite masking algorithm.

**Masking effect**

For example, one column stores data in the format “Chinese Name|Phone Number”, containing two sensitive data types: Chinese name and phone number, separated by “|”. With a custom composite masking algorithm, you can mask the Chinese name using a Chinese name replacement policy and mask the phone number using a phone number replacement policy. The following figure shows a comparison before and after masking:

**Configure the composite masking algorithm**

d
1. Select **Configuration > Discovery Rules**, and add a discovery rule that detects data in
composite format.
2. Configure segmented content.
3. Select **Configuration > Masking Algorithms**, and add a composite masking algorithm.
4. Add a database source or Add a file source.
d
5. When adding Discovery tasks, select the newly created composite discovery rule in
**Configure discovery rules**.
6. Perform sensitive field type verification or Verify file columns of sensitive file types.
7. Create a data masking task, and select the newly created composite masking algorithm for
the composite column. You can also manually Add a data subset, Add a masking policy, and Create a data masking task to configure masking. When adding a masking scheme, you must select the newly created composite masking algorithm for the composite column.

#### 2.7.5 Data Masking with Hybrid Masking Algorithm

**Algorithm**

For scenarios where a single column contains multiple sensitive data types across different rows, DMS supports custom hybrid masking algorithms that automatically match the appropriate masking method for each type of sensitive data. This article describes how to configure a hybrid masking algorithm.

**Masking effect**

For example, if one column contains both Chinese personal names and company names, you can use different masking algorithms by defining a custom hybrid masking algorithm. Apply the Chinese name replacement algorithm (preserving given name) to Chinese personal names, and apply the 3–6 character masking algorithm to company names. d
1. Select **Configuration > Masking Algorithm**, and add a hybrid masking algorithm.
2. Add a database source or Add a file source.
3. Add Discovery tasks**.**
4. Perform sensitive field type verification or Verify file columns of sensitive file types.
5. Create a data masking task, and select the newly created hybrid masking algorithm for
composite columns. You can also manually configure masking by Add a data subset, Add a masking policy, and Create a data masking task. When adding a masking scheme, you must select the newly created hybrid masking algorithm for composite columns.

#### 2.7.6 Data dictionary masking

DMS supports data dictionary masking. The system replaces sensitive data with content from the dictionary. Multi-column dictionaries maintain one-to-one correspondence between columns. This ensures consistent relational integrity after masking multiple columns. This topic describes how to configure data dictionary masking.

**Notes**

Use dictionary replacement if the original data exists in the data dictionary. Otherwise, select the dictionary random algorithm.

**Masking effect**

d After the system applies the dictionary replacement algorithm for masking, the masked result is content from the data dictionary.

**Configure the data dictionary**

1. Select **Configuration > Data Dictionary** to configure the data dictionary.
Use a built-in data dictionary. Create a new data dictionary. a. Click the icon. After you complete the configuration, click **Save**. If the data dictionary is a grouped dictionary: Configure the group column index. The column index must be numeric. Separate multiple columns with commas. If the data dictionary is a standard data dictionary: Leave the group column index blank. d b. Add dictionary content. After you add all dictionary entries, click the icon to archive.
2. Create a discovery rule. Set **Recommended Mask Algorithm** to **Dictionary**
**Replacement** or **Dictionary Random**.
Create N discovery rules for the data dictionary, where N equals the number of columns in the data dictionary.
3. Add a database source or Add a file source.
4. When you add Discovery tasks, select the newly created discovery rule based on the data
dictionary under **Determine the data range**.
5. Perform sensitive field type verification or Verify file columns of sensitive file types.
d
6. Create a data masking task. Select the dictionary replacement algorithm for columns
requiring masking. Specify the corresponding data dictionary and column index. Alternatively, add a "data subset", add a "masking scheme", and add a "masking task". Follow the manual process to create the data subset, masking scheme, and masking task. When you manually create the masking scheme, select the dictionary replacement algorithm for columns requiring masking and specify the corresponding data dictionary and column index.

#### 2.7.7 Text masking algorithm

DMS supports masking of large text, including JSON-formatted text and alphanumeric text, to intelligently identify sensitive information. This topic describes how to configure the text masking algorithm.

**Configure the text masking algorithm**

1. Select **Configuration > Masking Algorithm**.
2. Click the
icon to add a text masking algorithm.

#### 2.7.8 Group dictionary data masking

DMS provides the group dictionary data masking feature. This feature replaces values within a target column while preserving business associations between fields. For example, if your data contains “Province” and “City” columns, and you need to mask the “City” column while keeping the original “Province” values and the mapping relationship between province and city intact, you can use a group dictionary to precisely control the masking result. This topic describes how to configure group dictionary data masking. d

**Masking effect**

For example, if your data has two columns — city and district — and you mask the district column but not the city column, the masked district value must still correspond correctly to the preceding city value.
1. Select **Configuration > Data Dictionary**.
2. Create a group dictionary, enter its data, and archive it.
3. Add discovery rules. Set **Recommended masking algorithm** to **Dictionary**
**replacement** or **Dictionary randomization**.
Create N discovery rules based on the data dictionary, where N equals the number of columns in the data dictionary.
4. Add a database source or Add a file source.
d
5. When adding Discovery tasks, select the newly created discovery rule in **Determine the**
**data range**.
6. Perform sensitive field type verification or Verify file columns of sensitive file types.
7. Add a data subset. Skip this step if the data source is a file.
8. Add a masking policy.
9. Select **Data Masking > Solution Management**, then configure **Grouped Dictionary**
**Column Config**.
0. Create a data masking task, using the masking plan created in the previous step.

## 3 User Guide

### 3.1 Terms

| Term | Description |
|---|---|
| Datab ase maski ng | A feature that masks the data in a database and saves the masked data to a database or as files. |
| File maski ng | A feature that masks the data in specific files and saves the masked data to a database or as files. |
| Datab ase sourc e | A specific database that is used as the data source for database masking or the destination database to which the masked data is saved. |
| File sourc e | A collection of files, which is equivalent to a database. You can upload files to your on- premises machine on a web page. The files stored in a file source are structured files with certain data characteristics, such as standard CSV and TXT files, EXCEL files, and DMP files. A file source can be used as the data source for file masking. |
| Disco very rule | A rule that identifies sensitive data. You can use a discovery rule to identify potentially sensitive data from a large number of data items. |
| Maski ng algori thm | An algorithm that removes the sensitivity of sensitive data, such as masking or replacement. |
| Disco very task | A task that discovers sensitive data in database tables or files based on specific discovery rules. |
| Sensit ive field verific ation | A feature that sorts sensitive fields. After a discovery task is run on a database source, the types of sensitive data in table fields are manually verified. |

| Sensit ive file verific ation | A feature that sorts sensitive files. After a discovery task is run on a file source, the types of sensitive data in file columns are manually verified. |
|---|---|
| Data subse t | A collection of tables to be masked. Only the masking of DMP files requires data subsets. The masking of other files does not involve data subsets. After sensitive fields are verified, you can manually create a data subset or directly create a data masking task. When you create the task, you can select the scope of tables to be masked and skip the step of configuring a data subset. |
| Data maski ng soluti on | A solution that specifies the masking algorithm, such as masking or replacement, to mask the selected sensitive fields or file columns. After you create a data subset for database masking, you can manually create a data masking solution or directly create a data masking task. When you create the task, you can configure the scope of tables to be masked and a masking algorithm for sensitive fields, and skip the steps of configuring a data subset and a data masking solution. After you verify sensitive files for file masking, you can manually create a data masking solution or directly create a data masking task. When you create the task, you can configure a masking algorithm for sensitive columns and skip the step of configuring a data masking solution. |
| Data maski ng task | A task that masks data. To mask data, you must configure the parameters and exception handling method in a data masking task, and then run the task. When you create a data masking task, you can use an existing data masking solution. Alternatively, you can customize a masking algorithm for sensitive fields or sensitive file columns and skip the step of creating a data masking solution. |
| Looku p table | A table that determines the mappings used by a replacement algorithm for data masking. If you use a replacement algorithm based on different lookup tables to mask the same data, the masking results vary. |
| Data dictio nary | A user-defined dataset, which can contain multiple columns. A data dictionary can be used to replace one or more columns of data, or randomly combine the specified data into a set. It can also be used to discover sensitive data. |
| Group ing dictio nary | A data dictionary with grouping columns specified. You can use a grouping dictionary in combination with the grouping column configurations of a data masking solution to mask the data in each group. For example, Class 1 has Zhang San, Li Si, and Wang Wu, and Class 2 has Zhao Liu and Zheng Qi. A grouping dictionary can keep the data of the class column (Class 1 and Class 2) unchanged and mask the data of the name column with the names of their respective classes. After data masking, the data of the name column that corresponds to Class 1 is masked with names in Class 1, and the data of the name column that corresponds to Class 2 is masked with names in Class 2. |
| Field dictio nary | A collection of field names. You can use a field dictionary together with custom field dictionary discovery rules to discover sensitive data. If a field name exists in a field dictionary, the field is identified as sensitive data. |

| Maski ng algori thm templ ate | A template that specifies a masking algorithm and masking parameters to be used for a specific type of sensitive data. |
|---|---|
| File templ ate | A template that specifies whether a file contains information such as table headers, character sets, field delimiters, and field enclosing characters. File templates are used for discovery tasks and file parsing during file masking. |
| Space water marki ng | An algorithm that allows you to add spaces to the end of the data of the specified columns, thus embedding watermark information. |
| Pseud o-row water marki ng | An algorithm that allows you to insert a synthetic data tuple into a table in a relational database. The added row data is pseudo but is similar to the raw data. The information about an extractable watermark rule can be embedded in the inserted data tuple. |
| Pseud o- colum n water marki ng | An algorithm that allows you to insert a column that contains synthetic data into a table in a relational database. The data in the column is pseudo but is related to the raw data. The information about an extractable watermark rule can be embedded in the inserted column. |
| Water marki ng soluti on | A solution that extracts data and generates watermarks based on different scenarios. |
| Water marki ng task | A task that extracts data, generates watermarks, and generates output data based on different watermarking solutions. |
| Data tracea bility | A feature that allows you to extract the watermark information of leaked data, and use the watermark information to query the data information such as distribution sources and distribution objects. |

### 3.2 Data sources

#### 3.2.1 Database sources

##### 3.2.1.1 Add a database source

This topic explains how to add a database as a data source.

**Background**

The Data Discovery and Desensitization system supports various database types as data sources, including Oracle, MySQL, and SQL Server.

**Notes**

Database names must be unique. Each database source must have unique connection information. For Oracle databases, the combination of the host IP address, port, and database instance name must be unique. Batch creation of cloud database instances is supported only for MySQL and PostgreSQL databases.

**Individual creation**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Source > Database Source** tab.
3. In the upper-right corner of the **Database Source List**, click **Create Database Source**.
4. In the **Add Database Source** dialog box, enter the database connection details. Click
**Expand Advanced Options** to configure additional settings such as the JDBC URL, single-
byte decoding character set, and custom database driver.
5. Click **Test Connection** to verify the connection.

> **Note:** If the test connection fails, verify that the database information you entered is correct. Save the database information only after the test connection succeeds.

6. After the connection test succeeds, click **Save**.

**Batch creation**

1. To add multiple cloud database sources, you can also click **Batch Add Cloud Database**
**Instances** in the upper-right corner of the **Database Source List**.
2. Select the cloud databases to add, and then click **Batch Add Databases**.

##### 3.2.1.2 Modify a database source

This topic describes how to modify the information about a database specified as a data source.

**Background information**

If the information about a database specified as a data source changes, such as the IP address, port number, and username, you can modify the database information by clicking Edit in the Oper column on the Database Sources tab.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Sources**. Then, click the **Database Sources** tab.
3. In the **Database Sources List** section, find the database source that you want to modify
and click **Edit** in the Oper column.
4. In the **Edit Database Source** dialog box, modify the database information.

> **Note:** The database type cannot be modified.

5. Click **Save**.

##### 3.2.1.3 Delete database sources

This topic describes how to delete one or more database sources.

**Background information**

If a database is no longer used as a data source, you can delete the information about the database. If the information about a database used as a data source is associated with other data in Static Data Masking and Watermarking (DMS), the information about the database cannot be deleted. In this case, you must disassociate the data from the database, and then delete the information about the database.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Sources**. The **Database Sources** tab is displayed.
3. On the **Database Sources** tab, select one or more database sources that you want to
delete and click **Delete** above the database source list.
4. In the **Confirm** message, click **OK**.

##### 3.2.1.4 Query a database source

This topic describes how to query a database source.

**Background information**

You can quickly search for a database source and view its details.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Sources**. The **Database Sources** tab is displayed.
3. On the **Database Sources** tab, configure the **Database Source Name** and **Database IP**
parameters and click **Search**.

> **Note:** Fuzzy search is supported.

4. Find the database source from the query results and click **Edit** in the Oper column. In the
Edit Database Source dialog box, view the details of the database source.

#### 3.2.2 File sources

##### 3.2.2.1 Add a file source

This topic describes how to add a file source.

**Background information**

The Static Data Masking and Watermarking system allows you to mask data files that are exported from databases as data sources. Flat files in the CSV and TXT formats are supported. A flat file exported from a database is equivalent to a database table, and a collection of flat files is equivalent to a database. In Apsara Stack data security, a file source is defined as a collection of logically related flat files that share a common storage location and management method.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Sources**. Then, click the **File Sources** tab.
3. Click **Create File Source** at the top right of **File Source List**.
4. In the **Create File Source** dialog box, configure the file source name, upload method, and
description, and select a file or enter the Object Storage Service (OSS) URL of the file.

> **Note:** The file source name must be unique.

5. Click **Upload**.
6. Click **Next** to configure a custom file template or select an existing template.
7. Click **Save**.

##### 3.2.2.2 Modify a file source

This topic describes how to modify the information about a file source.

**Background information**

You can modify the template information or description of a file source.
1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Sources > File Sources**.
3. In the **File Sources List** section, find the file source that you want to modify and click **Edit**.
4. In the **Edit File Source** dialog box, modify the parameters of the file source.
5. Click **Next** to modify the custom file template or select an existing template.
6. Click **Save**.

##### 3.2.2.3 Delete file sources

This topic describes how to delete one or more file sources.

**Prerequisites**

The file sources to be deleted are not associated with other data in Static Data Masking and Watermarking (DMS).
1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Sources > Sources**.
3. In the **File Source List**, select the file sources that you want to delete and click **Delete**.
4. In the **Confirm** dialog box, click **OK** to delete the file source.

##### 3.2.2.4 Query a file source

This topic describes how to query a file source.

**Background information**

You can use the query feature to quickly find and view the details of a file source.
1. Log in to the Static Data Masking and Watermarking system.
2. Navigate to **Data Source > File Source**.
3. In the **search conditions**, enter a **file source name**, select a **file type**, and then click
**Query**.

> **Note:** The file source search feature supports fuzzy search.

4. In the search results, click **Edit** next to a file source to view its details.

### 3.3 Data discovery

#### 3.3.1 Discovery tasks

##### 3.3.1.1 Add a data discovery task

Learn how to add a data discovery task for a database.

**Background**

Data discovery automatically identifies sensitive data. When a discovery task runs, it scans your data based on predefined or custom rules to find and classify sensitive data.
1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Discovery > Discovery Task** tab.
3. Click **Add discovery task** to open the **Add discovery task** dialog box.
4. Configure the data scope for the discovery task.

| Parameter | Description |
|---|---|
| Data source type | Select Database or File. |
| Data source name | Select the target data source for the discovery task. |

| Task name | Enter a name for the discovery task. Note The Task name must be unique. |
|---|---|
| Select all data tables that meet the current query conditions | Select this option to scan all data tables that match your current query. Note If you do not select this option, you must manually select the tables or files to scan. Use the search box to find specific ones. |

5. In the **Sampling** section, configure the sampling rules, and then click **Next**.
For example: If a data table contains 10,000 rows and you set the sampling to the first 1,000 rows, the task scans those 1,000 rows to discover sensitive data. If a data table contains 800 rows and you set the sampling to the first 1,000 rows, the task scans all 800 rows.
6. Configure the discovery rules.
Select the discovery rules for the task. You can use system-defined and custom discovery rules.

**Note**

For more information, see Discovery Rules.
7. Configure the **Use sensitive field template**, **Count personal information**, and
**Synchronize classification and grading from Sensitive Data Protection** settings,
and then click **Save**.

##### 3.3.1.2 View the details of a data discovery task

This topic describes how to view the details of a database discovery task.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, find the database discovery task that you want to view, click
**More** in the **Operation** column, and then select **Task Details**.
4. On the **Discovery Task Details** page, view the details of the database discovery task.

##### 3.3.1.3 Execute a data discovery task

This topic describes how to execute a database discovery task.

**Background information**

You can use a discovery task to check whether the data source of the discovery task contains sensitive data.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, find the database discovery task that you want to execute and
click **Run Task** in the **Operation** column to execute the task.

##### 3.3.1.4 Stop a data discovery task

This topic describes how to stop a database discovery task.

**Background information**

You can stop a database discovery task that is running.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, find the database discovery task that you want to stop and
click **Stop the task** in the **Operation** column. If a discovery task is complete, the **Stop the task** button is not displayed.

##### 3.3.1.5 Modify a data discovery task

This topic describes how to modify a database discovery task.

**Background information**

You can modify the data source, discovery rules, and sampling data configurations of a database discovery task.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, find the database discovery task that you want to modify, click
**More** in the **Operation** column, and then select **Edit Task**.
4. On the **EditDiscovery Task** page, modify the database discovery task.

> **Note:** The task name, task type, and database cannot be modified. You can modify data configurations, rule configurations, and sampling configurations.

5. Click **Save**.

##### 3.3.1.6 Delete data discovery tasks

This topic describes how to delete one or more database discovery tasks.

**Prerequisites**

The database discovery tasks to be deleted are not associated with other data in the Apsara Stack data security system.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, select one or more database discovery tasks that you want to
delete and click **Delete** above the discovery task list.
4. In the **Information prompt** message, click **OK**.

##### 3.3.1.7 View the execution records of a data discovery task

**discovery task**

This topic describes how to view the execution records of a database discovery task.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Discovery Tasks** tab.
3. On the Discovery Tasks tab, find the database discovery task that you want to view, click
**More** in the **Operation** column, and then click **View History**.
4. In the **Discovery Task History** dialog box, find the task execution record that you want to
manage and click the icon in the Oper column.
5. On the **Discovery Task Execution Report** page, view the execution information about
the database discovery task.
6. In the **Discovery Task History** dialog box, find the task execution record that you want to
manage and click the icon in the Oper column to download the execution log of the database discovery task to your on-premises machine.

#### 3.3.2 Sensitive field sorting

##### 3.3.2.1 Add sensitive data sources

After a database discovery task is executed, the Apsara Stack data security system displays all fields in database tables and matched sensitive data discovery rules on the Sensitive Field Analysis tab.
1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Discovery > Sensitive Field Analysis**. On the page that appears, click the
expand icon on the left. In the Data Source List section, click the icon.
3. In the **Add Sensitive Data** dialog box, configure the Data Source, UserName, and
Password parameters and click **Connect**, as shown in the following figure. Figure 1: Add sensitive data

> **Note:** After the database is connected, the database table names and schema names are displayed on the right of the Add Sensitive Data dialog box.

4. Select the database tables to be discovered and click **Save**.
The added sensitive fields are displayed in the sensitive data list on the Sensitive Field Analysis tab.

##### 3.3.2.2 Verify sensitive data fields

This topic describes how to verify sensitive data fields.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive Field Analysis** tab.
3. In the Sensitive Data List section of the Sensitive Field Analysis tab, verify the discovered
sensitive data fields. To verify a single sensitive data field, find the sensitive data field that you want to verify and click **Check** in the Oper column, as shown in the following figure. Figure 1: Verify a single sensitive data field To verify multiple sensitive data fields at a time, select the sensitive data fields that you want to verify and click **Verify fields** above the sensitive data list.

##### 3.3.2.3 Specify sensitive data fields as non-sensitive data fields

**sensitive data fields**

This topic describes how to specify sensitive data fields as non-sensitive data fields.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive Field Analysis** tab.
3. In the Sensitive Data List section of the Sensitive Field Analysis tab, select the discovered
sensitive data fields, set the **Modify type** parameter to Non-sensitive Type, and then click
**Batch Modify**.

> **Note:** The data fields that are identified as non-sensitive data in the Sensitivity Type column cannot be specified as non-sensitive data fields.

4. In the **Confirm** message, click **OK**, as shown in the following figure.
Figure 2: Prompt for setting non-sensitive data fields

> **Note:** The sensitivity type of the data fields that are specified as non-sensitive data fields changes to Non-sensitive Type. The data fields in the corresponding discovery rules also change to non-sensitive data.

##### 3.3.2.4 Confirm the changes of sensitive data types of data fields

**types of data fields**

If a sensitive data discovery task is not executed for the first time and the sensitive data type of a data field changes, you must confirm the change of the sensitive data type of the data field. Otherwise, a data masking task that involves the data field cannot be executed. For example, the value of a data field is identified as a mobile phone number for the first time, and a data masking task that involves the data field is created. When a sensitive data discovery task is executed again, the value of the data field is identified as a telephone number. In this case, you must confirm the change of the data type of the data field before the data masking task is executed again.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive Field Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the database source discovery task that you want to manage and click
**Verify sensitive data** in the Operation column to go to the **Sensitive Field Analysis** tab.
The database source displayed on the Sensitive Field Analysis tab is the database source of the corresponding discovery task.
3. On the Sensitive Field Analysis tab, find the data field whose sensitive data type changes
and click **change** in the **Change State** column.
4. In the Change Sensitive Data message, click Confirm Change to confirm the change of the
sensitive data type of the data field, or click Not Change to leave the sensitive data type of the data field unchanged. To confirm the changes of sensitive data types of multiple data fields at a time, select the data fields whose sensitive data types change and click **Confirm**
**Change** above the sensitive data list. You can also click **Not Change** to leave the sensitive
data types of the data fields unchanged. You can also select the data field whose sensitive data type changes and click **Contrast**
**Change**. In the Compare change fields dialog box, click Change in the Oper column to
confirm the change of the sensitive data type of the data field, or click Unchange in the Oper column to leave the sensitive data type of the data field unchanged.

##### 3.3.2.5 View field sample data

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive Field Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the database source discovery task that you want to manage and click
**Verify sensitive data** in the Operation column to go to the **Sensitive Field Analysis** tab.
The database source displayed on the Sensitive Field Analysis tab is the database source of the corresponding discovery task.
3. On the **Sensitive Field Analysis** tab, click a value in the Sample column.
4. In the **More Sample Data** dialog box, view some of the sample values, sensitive data
types, and the proportion of each sensitive data type in the sample.

#### 3.3.3 Sensitive file sorting

##### 3.3.3.1 Verify file columns of sensitive file types

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive File Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the file source discovery task that you want to manage and click **Verify**
**sensitive data** in the Operation column to go to the **Sensitive File Analysis** tab. The file
source displayed on the Sensitive File Analysis tab is the file source of the corresponding discovery task.
3. On the **Sensitive File Analysis** tab, change the sensitive data types of file columns,
confirm the sensitive data types, select the file columns that you want to verify, and then click **Verify fields** to verify the file columns. You can select the file columns on the current page or all file columns across pages. To verify a file column, find the file column and click
**Check** in the Oper column.
If you go to the **Sensitive File Analysis** tab by clicking Verify sensitive data in the Operation column of a file source discovery task, click **Complete carding** after file columns of sensitive data types are verified. Then, we recommend that you click **Add**
**mask task** in the dialog box that appears to create a data masking task.
If you directly go to the **Sensitive File Analysis** tab, no **Complete carding** button appears after file columns of sensitive data types are verified. Then, you must manually create a data masking task.

##### 3.3.3.2 Modify sensitive data types of multiple file columns at a time

**columns at a time**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive File Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the file source discovery task that you want to manage and click **Verify**
**sensitive data** in the Operation column to go to the **Sensitive File Analysis** tab. The file
source displayed on the Sensitive File Analysis tab is the file source of the corresponding discovery task.
3. Select the file columns whose sensitive data types you want to modify at a time, choose the
target sensitive data type from the **Modify type** drop-down list, and then click **Batch**
**Modify**. In the Confirm dialog box that appears, click **OK**.

##### 3.3.3.3 Confirm the changes of sensitive data types of file columns

**types of file columns**

If a sensitive data discovery task is not executed for the first time and the sensitive data type of a file column changes, you must confirm the change of the sensitive data type of the file column. Otherwise, a data masking task that involves the file column cannot be executed. For example, the value of a file column is identified as a mobile phone number for the first time, and a data masking task that involves the file column is created. When a sensitive data discovery task is executed again, the value of the file column is identified as a telephone number. In this case, you must confirm the change of the data type of the file column before the data masking task is executed again.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive File Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the file source discovery task that you want to manage and click **Verify**
**sensitive data** in the Operation column to go to the **Sensitive File Analysis** tab. The file
source displayed on the Sensitive File Analysis tab is the file source of the corresponding discovery task.
3. On the Sensitive File Analysis tab, find the file column whose sensitive data type changes
and click **change** in the **Change State** column.
4. In the Change Sensitive Data message, click Confirm Change to confirm the change of the
sensitive data type of the file column, or click Not Change to leave the sensitive data type of the file column unchanged. To confirm the changes of sensitive data types of multiple file columns at a time, select the file columns whose sensitive data types change and click
**Confirm Change** above the sensitive data list. You can also click **Not Change** to leave the
sensitive data types of the file columns unchanged. You can also select the file column whose sensitive data type changes and click **Contrast**
**Change**. In the Compare change fields dialog box, click Change in the Oper column to
confirm the change of the sensitive data type of the file column, or click Unchange in the Oper column to leave the sensitive data type of the file column unchanged.

##### 3.3.3.4 View file sample data

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Discovery**. Then, click the **Sensitive File Analysis** tab.
You can also click **Data Discovery**. Then, click the **Discovery Tasks** tab. On the Discovery Tasks tab, find the file source discovery task that you want to manage and click **Verify**
**sensitive data** in the Operation column to go to the **Sensitive File Analysis** tab. The file
source displayed on the Sensitive File Analysis tab is the file source of the corresponding discovery task.
3. On the **Sensitive File Analysis** page, click a value in the Sample column.
4. In the More Sample Data dialog box, view some of the sample values, sensitive data types,
and the proportion of each sensitive data type in the sample.

#### 3.3.4 Sensitive field templates

A sensitive field template specifies the type of sensitive data in the column of a specific file for automatic data masking tasks.

**Add a sensitive field template**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Discovery > Sensitive Field Templates**.
3. In the left-side Sensitive Field Template List, click the
icon.
4. In the dialog box that appears, configure the Template Name, Template Type, and Out of
template processing strategy parameters, and then click **Save**. Valid values for the Template Type parameter: Database sensitive field template and File sensitive field template. Description of the Out of template processing strategy parameter:
**System auto discovery**: The system automatically identifies the data that is not
detected by the sensitive field template as the corresponding types of sensitive data.
**Marked as insensitive**: The system identifies the data that is not detected by the
sensitive field template as insensitive data.
5. In the left-side sensitive field template list, click the sensitive field template that you added.
6. In the Dictionary List of Sensitive Fields section, click the
icon.
7. In the **Add Database Sensitive Field Dictionary** or **Add File Sensitive Field**
**Dictionary** dialog box, configure the sensitive field information and click **Save**.

**Add a database sensitive field dictionary**

**Add a file sensitive field dictionary**

**Modify a sensitive field template and a sensitive field**

1. Choose **Data Discovery > Sensitive Field Templates** and find the sensitive field
template that you want to manage in the left-side Sensitive Field Template List.
2. Click the
icon to the right of the template that you want to modify.
3. Modify the values of the Template Name and Out of template processing strategy
parameters, and then click **Save**.
4. In the Dictionary List of Sensitive Fields section, find the sensitive field that you want to
modify and click the icon in the Oper column.
5. Modify the field information and click **Save**.

**Export a sensitive field dictionary**

1. Choose **Data Discovery > Sensitive Field Templates** and find the sensitive field
template that you want to manage in the left-side Sensitive Field Template List.
2. Click the
icon to the right of the template that you want to export.
3. Follow the on-screen instructions to download and save the CSV file.

**Import a sensitive field dictionary**

1. Modify the exported CSV file.
A database sensitive field dictionary file must meet the following requirements: The file must contain at least four columns of data: schema name, table name, field name, and sensitivity type. Empty rows in the file are not imported. Duplicate data in the file is imported only once. Data that already exists in the template is not imported. A file sensitive field dictionary file must meet the following requirements: The file must contain at least three columns of data: file name, file column sequence number, and sensitivity type. Empty rows in the file are not imported. Duplicate data in the file is imported only once. Data that already exists in the template is not imported.
2. Choose **Data Discovery > Sensitive Field Templates** and find the sensitive field
template that you want to manage in the left-side Sensitive Field Template List.
3. Click the
icon to the right of the template that you want to import.
4. Follow the on-screen instructions to upload the CSV file of the sensitive field template and
configure the template file parameters.
5. Click **Import**.

**Delete a sensitive field and a sensitive field template**

1. Choose **Data Discovery > Sensitive Field Templates**, and click the sensitive field
template that you want to manage in the left-side Sensitive Field Template List.
2. In the Dictionary List of Sensitive Fields section, find the sensitive field that you want to
delete and click the icon in the Oper column.
3. In the message that appears, click **OK**.
4. In the left-side Sensitive Field Template List, click the
icon to the right of the sensitive field template that you want to delete.
5. In the message that appears, click **OK**.

### 3.4 Data masking

#### 3.4.1 Data subsets

##### 3.4.1.1 Add a data subset

You can configure a collection of the tables to be masked. File source masking does not support this operation. You can also skip this step to directly create a data masking task.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Data Subsets** tab.
3. In the left-side Data Subset List section, click the
icon.
4. On the Basic Information tab of the Add Data Subset dialog box, configure the **Subset**
**Name**, **Subset Type**, **Data Source**, and Description parameters. Then, click **Next**.
5. If the driving table feature is not required, click **Next** on the Driver Table Config tab.
6. If the driving table feature is required, set the Config Driver Table parameter to **ON**, specify
a table as the driving table, and then click **Next** on the Driver Table Config tab. After a primary key table is specified as the driving table and is filtered by using the subset filtering feature, the foreign key table is automatically filtered based on the conditions of the primary key table and not all data in the foreign key table is masked. If the primary keys of a table do not have relationships with foreign keys of the table and the driving table feature is required, you can configure logical relationships between the primary keys and the foreign keys.
7. On the Data Table Config tab, select the tables to be masked and click **Save**. By default, all
tables in the DMP file source are selected and cannot be cleared.
8. We recommend that you create a data masking solution later.

##### 3.4.1.2 Modify a data subset

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Data Subsets** tab.
3. In the left-side Data Subset List section of the Data Subsets tab, find the data subset that
you want to modify and click the Edit icon.
4. In the Edit Data Subset dialog box, modify the information about the data subset and click
**Save**.
You can modify only the name and description of the data subset. For more information about how to modify the data tables in a data subset, see **Manage data tables in a data**

**subset.**

##### 3.4.1.3 Delete a data subset

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Data Subsets** tab.
3. In the left-side Data Subset List section of the Data Subsets tab, find the data subset that
you want to delete and click the Delete icon.
4. In the message that appears, click **OK**.

> **Important:** If the data subset is used by a data masking solution, a message appears indicating that the data subset fails to be deleted.

##### 3.4.1.4 Manage data tables in a data subset

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Data Subsets** tab.
3. On the **Data Table** tab of the Data Subsets tab, find the data table that you want to
manage and click **Enable** or **Disable** in the State column to enable or disable the data table. To enable or disable multiple data tables at a time, select the data tables that you want to manage and click **Enable Data Table** or **Disable Data Table** above the data table list. After a data subset is created, all tables in the data subset are enabled by default. If the state of a table is changed from Enable to Disable, the table will not be masked and migrated when the data masking task that involves the table is executed.
4. To add one or more data tables to a data subset, select the desired data subset in the left-
side Data Subset List section and click **Add Data Table** on the **Data Table** tab. Then, in the Add Data Table dialog box, select the tables that you want to add and click **Save**.
5. To delete one or more data tables from the data subset, select the tables that you want to
delete and click **Delete** on the **Data Table** tab. In the message that appears, click **OK**.

> **Important:** If the data subset is used by a data masking solution, a message appears indicating that the tables fail to be deleted.

##### 3.4.1.5 Manage constraints of a data subset

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Data Subsets** tab.
3. On the **Constraint** tab, find the constraint that you want to manage and click **Enable** or
**Disable** in the **State** column to enable or disable the constraint.
4. On the **Constraint** tab, click **Add Constraint**. In the Add Constraint dialog box, enter a
constraint name, select a child table and a parent table, and then click **Next**. Then, configure the mappings between child table columns and parent table columns and click
**Save**. You can configure multiple mappings between child table columns and parent table
columns. In the message that appears, click OK.
5. On the **Constraint** tab, select one or more constraints that you want to delete and click
**Delete**. In the message that appears, click OK.
6. On the **Constraint** tab, find the constraint that you want to view and click the **View**
**details** icon in the Operation column. In the Constraint Details message, view the details of
the constraint.

#### 3.4.2 Solution management

##### 3.4.2.1 Add a masking policy

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **data masking > policy management** tab.
3. In the policy list on the left, click the add icon.
4. In the **Add masking policy** dialog box, select a data source type (database source, file
source, or DMP file source) and a data source. DMS automatically generates a default policy name (editable). For a database source, you must select a masking mode: out-of-place masking or in-place masking. In-place masking updates the data directly in the source table, whereas out-ofplace masking writes the masked data to a new table. Not all database types support inplace masking. When you are finished, click **Next**.
5. Select the data subset to mask and click **Next**.
This step is skipped for file sources.
6. For each sensitive data type, configure a masking algorithm and its parameters, and then
click **Save**. By default, only recommended masking algorithms are displayed for each sensitive data type. To display general algorithms, click the button in the Current Algorithm column.

> **Important:** On this page, you can configure only one masking algorithm for each sensitive data type.

7. In the message box, click **Add masking task** to go to the **data masking > masking**
**task** tab. For the next steps, see the **masking task** section.

##### 3.4.2.2 View the details of a data masking solution

**solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side **Project List** section of the Solution Management tab, find the data masking
solution that you want to view and click the View Project icon.
4. On the **Details of Mask Project** page, view the details of the data masking solution.

##### 3.4.2.3 Modify a data masking solution

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side Project List section of the Solution Management tab, find the data masking
solution that you want to modify and click the Edit Project icon.
4. In the **Edit Project** dialog box, modify the name and description of the data masking
solution and click **Save**.
5. In the message that appears, click **Add Mask Task** to go to the **Add Mask Task** page of
the **Masking Tasks** tab. For more information, see **Data masking tasks**.

##### 3.4.2.4 Delete a data masking solution

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the Project List section of the Solution Management tab, select a data masking solution
that you want to delete and click the **Delete Project** icon.
4. In the message that appears, click **OK**.

> **Important:** If the data masking solution is referenced by a data masking task, a message appears and the data masking solution fails to be deleted.

##### 3.4.2.5 Manage data subsets of a data masking solution

**solution**

> **Note:** Data masking solutions whose data source type is file source do not support data subset operations.

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side Project List section of the Solution Management tab, find the data masking
solution that you want to manage and click its name. Then, perform the following steps to add data subsets to the data masking solution: i. On the **Data Subset** tab, click **Add Data Subset**. ii. In the Add Data Subset dialog box, select the data subsets to be added and click **Save**.
4. Delete data subsets from the data masking solution.
i. On the **Data Subset** tab, select the data subsets that you want to delete and click
**Delete**.
ii. In the dialog box that appears, click **OK**.

> **Important:** If the data masking solution is referenced by a data masking task, a message appears indicating that the data subsets fail to be deleted.

5. Configure the subset filtering feature.
The subset filtering feature allows you to add filter conditions for tables. During data masking, only the table data that meets the filter conditions is masked, and the table data that does not meet the conditions is not masked and not migrated. In addition, you can configure an incremental field for incremental data masking when you configure the subset filtering feature. i. On the **Data Subset** tab, find the data subset that you want to manage and click the
**Configure Filter Conditions** icon in the Operation column.
ii. In the Data Subset-filtering Condition dialog box, configure filter conditions. You can configure filter conditions on a page or by using extension conditions.

**Configure filter conditions on a page.**

a. In the Data Subset-filtering Condition dialog box, click the table for which you want to add a subset filter condition on the left. On the Filter Condition tab of the Data Subset-filtering Condition dialog box, click the Add Filter Condition icon. b. On the **Expression** tab of the Add Filter Condition dialog box, select the column for which you want to add a filter condition from the left-side list and configure a filter condition on the right.

> **Important:** Selecting**Set to Incremental Field** is used to configure an incremental field for incremental data masking and is not used to configure the subset filtering feature.

c. Click the **Logical Combination** tab of the Add Filter Condition dialog box. On the Logical Combination tab, configure the logical relationship between multiple conditions and click Save. d. Repeat the preceding steps to configure filter conditions for multiple fields of multiple tables and click **Save**.

**Configure filter conditions by using extension conditions.**

On the **Filter Condition** tab of the Data Subset-filtering Condition dialog box, write SQL statements in the Extension Condition field to configure filter conditions.
**Partition Selection**: The Partition Selection tab of the Data Subset-filtering Condition
dialog box is specific to Apache Hive. Partitioned tables of Apache Hive can be masked by partition. The configured filter conditions are displayed in the **Configure SQL for Filter Criteria** field.

##### 3.4.2.6 Manage masking algorithms of a data masking solution

**masking solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side Project List section of the Solution Management tab, find the data masking
solution that you want to manage and click its name. Then, click the **Algorithm Config** tab.
4. On the **Algorithm Config** tab, modify masking algorithms.
Find the field column that you want to manage, modify the configurations in the Masking Algorithm and Algorithm Parameter columns, and then click the **Save** icon. Repeat this step to modify the masking algorithms and algorithm parameters of other field columns. After masking algorithms of multiple field columns are modified, select the field columns and click **Save** above the algorithm configuration list to save the modified masking algorithms.
5. On the **Algorithm Config** tab, configure a masking algorithm for multiple field columns at
a time. i. Select the field columns for which you want to configure a masking algorithm and click
**Batch Setting Algorithms**.
ii. In the Batch Setting Algorithms dialog box, configure a masking algorithm and the corresponding algorithm parameters, and click **Save**.
6. On the **Algorithm Config** tab, configure algorithms.
For the data subsets selected in the data masking solution and the table fields for which you do not configure masking algorithms in the data masking solution (such as the scenario of manually deleting some masking algorithms or manually adding data subsets to the data masking solution), you can configure masking algorithms for sensitive data types. i. Click **Config Algorithm**. ii. In the **Configuration of Masking Algorithm** dialog box, configure masking algorithms and parameters for sensitive data types and click **Add**.
7. On the **Algorithm Config** tab, delete algorithms.
i. Select the field columns that you want to delete and click **Delete**. ii. In the message that appears, click **OK**.

##### 3.4.2.7 Manage the grouping dictionary column configuration of a data masking solution

**configuration of a data masking solution**

To use the grouping dictionary-based data masking of a data dictionary, you must configure the grouping dictionary column on a table. For example, the grouping dictionary A has two columns (Hebei/Tangshan, Henan/Zhengzhou, and Henan/Luoyang). A table named T has two columns (Henan/Zhengzhou). The first column of the T table is specified as a grouping dictionary column and is not masked. The dictionary replacement algorithm is used for the second column of the T table. The values in the second column are replaced with the cities of the Henan province in the dictionary and will not be replaced with Tangshan (a city of the Hebei province). The grouping dictionary column of the table is configured in the data masking solution.
1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side Project List section of the Solution Management tab, select the data masking
solution that you want to manage. Then, click the **Grouped Dictionary Column Config** tab.
4. Modify the grouping dictionary column configuration of a table.
i. Find the table whose grouping dictionary column configuration is to be modified and click the icon in the **Operation** column. ii. In the dialog box that appears, select a grouping dictionary, configure the mapping between the grouping dictionary column and the column in the table, and then click
**Save**.
5. Delete the grouping dictionary column configuration of a table.
i. Find the table whose grouping dictionary column configuration is to be deleted and click the icon in the Operation column. ii. In the dialog box that appears, click **OK**.

##### 3.4.2.8 Manage expressions of a data masking solution

**solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Solution Management** tab.
3. In the left-side Project List section of the Solution Management tab, find the data masking
solution that you want to manage and click its name. Then, click the **Expression Config** tab.
4. Add expressions.
i. On the **Expression Config** tab, click **Add Expression**. ii. In the Add Expression dialog box, select a table on the left and add expressions. JavaScript syntax is supported. Click a table column in the **Optional Field List** column. Click an operator in the
**Operational Symbol** column. You can click the icon next to Operational Symbol to
switch to Built-in Functions (properties). Click the Add icon next to the first expression to add multiple expressions. iii. If multiple expressions exist in the same table, they have priorities. The expression that is configured first in the Add Expression dialog box has a higher priority. The expression whose value is smaller in the Add Expression dialog box has a higher priority. For example, the value of the original data column named B is 0, and two expressions are configured: B = 1 and C = B + 1. If the expression B = 1 has a higher priority than the expression C = B + 1, the expression B = 1 is executed first. In this case, the value of the B column is 1. Then, the expression C = B + 1 is executed. After data masking, the value of the B column is 1 and the value of the C column is 2. If the expression B = 1 has a lower priority than the expression C = B + 1, the expression C = B + 1 is executed first. In this case, the value of the B column is still 0 and the value of the C column is 1 (0 + 1 = 1). Then, the expression B = 1 is executed. In this case, the value of the B column is 1.
5. Modify an expression.
i. Find the expression that you want to modify and click the **Edit** icon in the Operation column. ii. In the **Edit Expression** dialog box, modify the expression and click Save. For more information, see the **Add expressions** section of this topic.
6. Delete an expression.
i. Select the expression that you want to delete and click **Delete**. ii. In the message that appears, click **OK**.

##### 3.4.2.9 Configure a whitelist for a data masking solution

**solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Masking > Solution Management**.
3. In the left-side Project List section of the Solution Management tab, select the data masking
solution that you want to manage. Then, click the **White List** tab.
4. On the **White List** tab, click **Add White List**.
5. In the Add White List dialog box, configure the Schema Name, Table Name, and Field
parameters in the **Condition Judgment Field** section.
6. Set the **Matching Mode** parameter to **Regular Expression**. Then, enter a regular
expression in the input box. For example, if the password field matches a column that starts with once, the regular expression is ^once.
7. In the **Non-Masking Field** section, select a value from the Field drop-down list and click
the + icon to add one or more fields that are not masked. This configuration indicates the fields that are not masked if the preceding regular expression is hit. You can also click **Batch Add White List** to configure multiple whitelists at a time as prompted.

##### 3.4.2.10 Configure a blacklist for a data masking solution

**solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Masking > Solution Management**.
3. In the left-side Project List section, select the data masking solution that you want to
manage. Then, click the **Black List** tab.
4. On the **Black List** tab, click **Add Black List**.
5. In the Add Black List dialog box, configure the Schema Name, Table Name, and Field
parameters in the **Condition Judgment Field** section.
6. Set the **Matching Mode** parameter to **Regular Expression**. Then, enter a regular
expression in the input box. For example, if the password field matches a column that starts with once, the regular expression is ^once. The configuration indicates that the fields matched by the regular expression are not migrated. For example, when masking data for a special group of people, the entire row of data that involves these conditions is not migrated. You can also click **Batch Add Black List** to configure multiple blacklists at a time as prompted.

#### 3.4.3 Data masking tasks

A data masking task is used to mask data. To mask data, you must configure the parameters and exception handling method in a data masking task, and then run the task. When you create a data masking task, you can use an existing data masking solution. Alternatively, you can customize a masking algorithm for sensitive fields or sensitive file columns and skip the step of creating a data masking solution.

##### 3.4.3.1 Create a data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab. On the Masking Tasks tab, click
**Add Mask Task**.
You can also choose **Data Discovery > Discovery Tasks**, find the discovery task that you want to manage, and click **Add desensitization task** in the Operation column**.**
3. In the Select desensitization range step, configure the Task Type, Source, Mask Project, and
Select Code Table parameters and click **Next**. The valid values of the Task Type parameter are Database and File. You can select a data source or a file source from the Source dropdown list. If you set the Mask Project parameter to Custom Mask Project, the Masking Mode parameter is required. If you set the Mask Project parameter to Use an Existing Projects, the Select Mask Project parameter is required.

> **Important:** If you create a data masking task by clicking Add desensitization task on the Discovery Tasks tab, the values of the Task Type and Source parameters cannot be changed and an existing data masking solution cannot be selected.

> If you set the **Task Type** parameter to **Database** and the Mask Project parameter to Custom Mask Project, the **Masking Mode** parameter is required. If the selected database does not support source mode masking, the value of the Masking Mode parameter cannot be changed.
> If you set the **Mask Project** parameter to **Use an Existing Projects**, the Select Mask Project parameter is required and the Masking Mode parameter is not displayed.

4. In the Configure Data Subset step, select the tables or files to be masked and click **Next**.
If you create a data masking task by clicking Add desensitization task on the Discovery Tasks tab, the value of the Mask Scope parameter is the table discovered by the corresponding discovery task by default. The Configure Data Subset step in the configuration process will be skipped. If you set the **Mask Project** parameter to **Use an Existing Projects** in the previous step, the Configure Data Subset step in the configuration process will be skipped. This is because the selected data masking solution contains a data subset, and the data subset is the data masking scope.
5. In the Configure Algorithm step, configure algorithms.
Configure data masking algorithms and parameters for sensitive data types. i. By default, the data masking algorithms displayed on the rule algorithm configuration page are the recommended data masking algorithms for the sensitive data types. You can click **General Algorithm** in the Oper column to display the general data masking algorithm. You can also click unmasked in the Oper column to unmask the data of a sensitive data type. ii. To configure different data masking algorithms for different fields of the same sensitive data type, click **Field Algorithm Configuration**. You can also click **Set Field** in the Oper column of the corresponding sensitive data type to go to the field algorithm configuration page. On the field algorithm configuration page, configure different data masking algorithms and parameters for fields. You can configure data masking algorithms for fields one by one. You can also select multiple fields and click **Batch Setting Algorithms** to configure data masking algorithms for the fields at a time. iii. Click **Save** to save the configurations. Then, click **Rule Algorithm Configuration** to return to the rule algorithm configuration page. iv. After the configurations are complete, click **Next**.

> **Important:** To configure a data masking algorithm for another field on the field algorithm configuration page, you must click **Save** and **Rule Algorithm Configuration** to return to the rule algorithm configuration page and repeat the previous operations. Then, click **Next** to complete algorithm configuration.

6. In the Desensitization Parameter step, configure the parameters and click **Next**.

> **Important:** The configuration items displayed in the Desensitization Parameter step vary based on your selection. For example, if you set the **Output Target** parameter to Local File or Remote File, database-related configurations are not displayed. If some types of databases do not support object migration or do not have the tablespace concept, the related configurations are not displayed.

| Paramete r | Description |
|---|---|
| Output Target | Database: If you set this parameter to Database, configure the Target Database and Batch Database Input parameters. Local File: If you set this parameter to Local File, you can download the file on the Masking Tasks tab after data masking. Remote File: If you set this parameter to Remote File, the file is directly uploaded after data masking. You must set the remote file source. |
| Schema Name/Dat abase Name | If you set the Output Target parameter to Database, the Schema Name/Database Name parameter is required. The database name. Valid values: Use the database name of the same name as the source and Database Name. If you set the Schema Name/Database Name parameter to Database Name, enter a custom database name. |
| Tablespac e | If the Output Target parameter is set to Database, set the destination tablespace. You can select a tablespace with the same name as the original table, or specify a tablespace. |

| Table Processin g | The table processing method. If you set the Output Target parameter to Database, this parameter is required. |
|---|---|
| Migrating objects | The object to be migrated during data masking. If you set theO utput Target parameter to Database, this parameter is required. You can select multiple objects. |
| File Extension | The file name extension after data masking. If you set theO utput Target parameter to Local File or Remote File, this parameter is required. |
| Whether With Header | Specifies whether the file includes a header after data masking. If you set theO utput Target parameter to Local File or Remote File, this parameter is required. |
| Whether to write BOM | Specifies whether a Bill of Material (BOM) is written to the file after data masking. If you set the Output Target parameter to Local File or Remote File, this parameter is required. |

The MaxCompute data source supports the masked data migration feature. As shown in the following figure, if you set the Move Masked Data parameter to YES, the Move Target parameter is required. In this case, the database selected from the Target Database dropdown list in the **Output Target** section is used as the intermediate database, and the database specified in the **Move Target** section is the destination database for masked data migration. You can select MaxCompute(ODPS) or MySQL from the Database Type drop-down list and configure the Table Processing parameter in the Move Target section. If you set the Table Processing Of Target Database parameter to Delete, the data in the destination database is deleted after the data migration is complete. If you set the Table Processing Of Target Database parameter to Reserve, the data in the destination database is retained after the data migration is complete.
7. In the Exception handling step, configure the Exception Handling, Task Name, and Task
Description parameters and click **Save** or **Save And Execute**. The value of the Task Name parameter is generated by default and can be modified. Valid values of the Exception Handling parameter: discard: All the data in the row in which abnormal field resides is discarded. This may cause data loss. set null: The value of the abnormal field is left empty, and other fields in the row in which the abnormal field resides are masked as expected. If the abnormal field has a NOT NULL constraint, the data in the row in which the abnormal field resides cannot be inserted into the database. fill: By default, the value of the abnormal field remains unchanged, and other fields in the row in which the abnormal field resides are masked as expected. In this case, sensitive data may be exposed. You can select **Out-of-format data, try to generate randomly during masking** . However, not all data types support the option, and sensitive data may be exposed. If the steps of creating a data subset and data masking solution are skipped when you create the data masking task, you can select **Save the data subset and mask**
**algorithm of this task as mask project**. When you save the data masking task, a data
subset and data masking solution are automatically generated based on the configurations of the data masking task. The automatically generated data subset and data masking solution can be reused by other data masking tasks. If a data masking task requires expression configurations and subset filtering, the corresponding data subset and data masking solution need to be generated.
8. In the Incremental Configuration step, specify a value for an incremental field. If you set the
Mask Project parameter to Use an Existing Projects in the Select desensitization range step and an incremental field is configured in the data masking solution, this step is required. This step is to specify a value for an incremental field. The value of the incremental field is used to mask the data in the rows whose field data is greater than this value. For the first time, you can set the value of the incremental field to a value smaller than the current minimum value to mask all data in the current table. After the data masking task is executed, the value of the incremental field is automatically changed to the current maximum value. This is to distinguish the incremental data when the data masking task is executed next time.

##### 3.4.3.2 Modify a data masking task

> **Important:** Only data masking tasks that are not being executed can be modified.

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, find the data masking task that you want to modify, click **More**
in the Oper column, and then select **Edit Task**. On the page that appears, modify the data masking task. For more information about parameter configurations, see **Create a data masking task** .

##### 3.4.3.3 Delete a data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, select the data masking task that you want to delete and click
**Delete**.
4. In the message that appears, click **OK**.

##### 3.4.3.4 Execute or stop a data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, find the data masking task that you want to execute and click
**Run Task** in the Oper column to execute the data masking task.
4. When a data masking task is being executed, find the data masking task that you want to
stop and click **Stop Task** in the Oper column to stop the data masking task.

##### 3.4.3.5 View the execution records of a data masking task

**masking task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, find the data masking task that you want to view and click
**History** in the Oper column.
4. In the **Mask Task History** dialog box, view the execution records of the data masking
task. When the data masking task is executed once, a record is generated in this dialog box. Click the icon. On the **Masking Task Execution Report** page, view the execution report of the data masking task, including the data masking duration, data masking speed, data masking status of a single table or file, and exception information. Select a table in the Execution Information List section and click **Re-Run** to re-execute the data masking task for the selected table. Find the table that you want to manage and click the icon in the Oper column. On the **Data Comparison of Masking Tasks** page, compare the data before and after data masking. Click **Connect** to connect to the database. Then, click **Data**
**Comparison** to compare the data of the table to be queried. The data comparison
feature is available only when the data masking mode of the database is cross-mode masking. Click the or icon to download the masked file. The download feature is only available when the Output Target parameter is set to Local File during data masking task creation. Click the icon to download the execution log of the data masking task.

**In most cases, you can use the error information in the execution report and**

**execution log to troubleshoot the error.**

##### 3.4.3.6 View the details of a data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, find the data masking task that you want to view, click **More** in
the Oper column, and then select **Task Details**.
4. On the **Details of Masking Task** page, view the configurations of the data masking task,
including the information about the source and destination databases, data masking algorithms and parameters of sensitive fields, table processing, and exception handling.

##### 3.4.3.7 View the progress of a data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Masking Tasks** tab.
3. On the Masking Tasks tab, find the data masking task that you want to view, click **More** in
the Oper column, and then select **Task Progress**.
4. In the Implementation of Mask Task dialog box, view the current data masking speed,
tables that are being masked, and status of the tables that are masked.

#### 3.4.4 Automatic data masking tasks

An automatic data masking task refers to a task that automatically downloads the files to be masked from the source remote FTP file source, masks the files based on a preset template, and then uploads the masked files to the destination remote FTP file source. Automatic data masking tasks must be used together with remote FTP file sources. You must configure sensitive field templates and masking algorithm templates in advance.

##### 3.4.4.1 Create an automatic data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Masking > Auto Masking Tasks**. Then, click the
icon to create an automatic data masking task.
3. Set **Basic Information** and click **Next**.
4. On the Template Configuration Information tab, configure the **Sensitive Field Template**
and **Mask Algorithm Template** parameters and the parameters in the Output Target Information section. Then, click **Next**. A sensitive field template maps a specific column in a file to a defined sensitive data type. A masking algorithm template then specifies the algorithm and parameters to be used for masking that data type.
5. On the **Exception Handling** tab, select an exception handling method and click **Save**.
If you select **Fill**, you can select **Out-of-format data, try to generate randomly during**
**masking**. However, as this capability is not supported by all data types, some sensitive
data may remain unmasked.

##### 3.4.4.2 Modify an automatic data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Auto Masking Tasks** tab.
3. On the Auto Masking Tasks tab, find the automatic data masking task that you want to
modify, click the Operation List icon in the Oper column, and then select **Edit Task**. In the Edit Automatic Mask Task dialog box, modify the automatic data masking task. For more information about parameter configurations, see **Create an automatic data ma**
**sking task**.

##### 3.4.4.3 Execute an automatic data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Auto Masking Tasks** tab.
3. On the Auto Masking Tasks tab, find the automatic data masking task that you want to
execute, click the Operation List icon in the Oper column, and then select **Run Task**.

> **Important:** The source remote file directory must have a feature file. The presence of the feature file indicates that the files in the source FTP folder are transferred. This prevents data loss due to the execution of an automatic data masking task when a file is being uploaded to the source FTP folder. An automatic data masking task can be executed only if this feature file is detected; otherwise, the task fails to launch and an error is generated.

##### 3.4.4.4 Delete an automatic data masking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Auto Masking Tasks** tab.
3. On the Auto Masking Tasks tab, find the automatic data masking task that you want to
delete, click the Operation List icon in the Oper column, and then select **Delete Task**.
4. In the message that appears, click **OK**.

##### 3.4.4.5 View the execution records of an automatic data masking task

**automatic data masking task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Masking**. Then, click the **Auto Masking Tasks** tab.
3. On the Auto Masking Tasks tab, find the automatic data masking task that you want to
view, click the Operation List icon in the Oper column, and then select **History**.
4. In the Automatic Mask Task Execution Record dialog box, view the execution records of the
automatic data masking task. When the automatic data masking task is executed once, a record is generated in this dialog box. Find the execution record that you want to manage and click the icon in the Oper column to download the execution report. Find the execution record that you want to manage and click the icon in the Oper column to download the execution log.

### 3.5 Data watermarking

#### 3.5.1 Watermarking tasks

##### 3.5.1.1 Create a watermarking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Tasks** tab.
3. On the Watermarking Tasks tab, click **Add Watermark Task**.
4. In the Add Watermark Task dialog box, configure the parameters on the Basic Information,
Select Watermark Scheme, and Task Configuration tabs. i. On the Basic Information tab, configure the Task Name, Distribution Source Unit, Distribution Target, and Task Description parameters, set the **Task Type** parameter to
**Database**, and then click **Next**. The new task name cannot be the same as the name of
an existing task. For more information about how to manage distribution objects, see **Distribution object**
**management**.
ii. On the Select Watermark Scheme tab, select a watermarking solution, configure the information about the destination database, and then click **Next**. For more information about how to manage watermarking solutions, see **Watermarking**
**solutions**.
iii. On the Task Configuration tab, select an object processing method and click **Save**. If you select a MaxCompute solution that contains a partitioned table, you must enter the name of the partition to which you want to add watermarks.

##### 3.5.1.2 Modify a watermarking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Tasks** tab.
3. On the Watermarking Tasks tab, find the watermarking task that you want to modify and
click **Edit** in the Operation column.
4. In the **Edit Watermark Task** dialog box, modify the basic information on the Basic
Information tab and click **Next**. Only the Task Name and Task Description parameters can be modified.
5. On the Select Watermark Scheme tab, modify the parameters in the Select Scheme Name
and Output Destination Information sections and click **Next**.
6. On the Task Configuration tab, modify the table processing method and click **Save**.

##### 3.5.1.3 Execute a watermarking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Tasks** tab.
3. On the Watermarking Tasks tab, find the watermarking task that you want to execute and
click **Run** in the Operation column. In the Run Watermark Task dialog box, fill in the
**Username** and **Password** fields and click **Run Task**.

##### 3.5.1.4 View the details of a watermarking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Tasks** tab.
3. On the Watermarking Tasks tab, find the watermarking task that you want to view and click
**View** in the Operation column.
4. In the View Watermark Task dialog box, view the information on the **Basic Information**
tab and click **Next**.
5. On the Select Watermark Scheme tab, view the information in the Select Scheme Name and
Output Destination Information sections and click **Next**.
6. On the Task Configuration tab, view the information in the Table Processing and Partition
Selection sections and click **Cancel**.

##### 3.5.1.5 Stop a watermarking task

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Tasks** tab.
3. On the Watermarking Tasks tab, find the watermarking task that you want to stop and click
**Stop** in the Operation column.
4. In the message that appears, click **OK**.

#### 3.5.2 Data subsets

To use this feature, refer to **Data masking > Data subsets**.

#### 3.5.3 Watermarking solutions

##### 3.5.3.1 Create a watermarking solution

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Schemes** tab.
3. On the Watermarking Schemes tab, click **Add Watermark Scheme**.
4. In the Add Scheme dialog box, configure the following parameters on the Basic Information
tab and click **Next**: Scheme Name, Data Source Type, Data Source, Watermark Algorithm, and Scheme Description. The new solution name cannot be the same as the name of an existing solution.
5. On the Configure Data Subset tab, select one or more data subsets and click **Next**.
6. On the Configure Field Rules tab, configure field rules and click **Save**.
Configure field rules of the watermarking algorithm. Select at least two fields for generating watermarks for a pseudo-row and a field for generating watermarks for a pseudo-column. Only one pseudo-column field can be generated for each data table. For more information about how to manage pseudo-column fields, see **Pseudo-column field management**. In the message that appears, click **OK**.

##### 3.5.3.2 Modify a watermarking solution

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Schemes** tab.
3. On the Watermarking Schemes tab, find the watermarking solution that you want to modify
and click **Edit** in the Operation column.
4. In the Edit Scheme dialog box, modify the basic information on the Basic Information tab
and click **Next**. Only the Watermark Algorithm and Scheme Description parameters can be modified.
5. On the Configure Data Subset tab, modify the data subsets and click **Next**.
6. On the Configure Field Rules tab, modify the field rules of the watermarking algorithm and
click **Save**. In the message that appears, click **OK**.

##### 3.5.3.3 Delete one or more watermarking solutions

**solutions**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Schemes** tab.
3. To delete a single watermarking solution, find the watermarking solution that you want to
delete on the Watermarking Schemes tab and click **Delete** in the Operation column. To delete multiple watermarking solutions at a time, select the watermarking solutions that you want to delete and click **Delete** above the watermarking solution list.
4. In the message that appears, click **OK**.

##### 3.5.3.4 View the details of a watermarking solution

**solution**

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Watermarking Schemes** tab.
3. On the Watermarking Schemes tab, find the watermarking solution that you want to view
and click **View** in the Operation column.
4. On the **Watermark Scheme Details** page, view the details of the watermarking solution,
including the basic information, data subsets, watermarking algorithm, and field rules.

#### 3.5.4 Pseudo-column field management

##### 3.5.4.1 Add a pseudo-column field

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Pseudo Column Management** tab.
3. On the Pseudo Column Management tab, click **Add** to add a pseudo-column field.
4. In the Add Pseudo Column dialog box, configure the Pseudo Column Name, Pseudo Column
Type, and Description parameters and click **Save**. The pseudo-column field types include ID card numbers, bank card numbers, mobile numbers, names, addresses, Email addresses, and license plate numbers.

##### 3.5.4.2 Modify a pseudo-column field

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Pseudo Column Management** tab.
3. On the Pseudo Column Management tab, find the pseudo-column field that you want to
modify and click **Edit** in the Operation column.
4. In the Edit Pseudo Column dialog box, modify the Pseudo Column Name, Pseudo Column
Type, and Description parameters and click **Save**. The pseudo-column field types include ID card numbers, bank card numbers, mobile numbers, names, addresses, Email addresses, and license plate numbers.

##### 3.5.4.3 Delete one or more pseudo-column fields

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Pseudo Column Management** tab.
3. To delete a single pseudo-column field, find the pseudo-column field that you want to
delete on the Pseudo Column Management tab and click **Delete** in the Operation column. To delete multiple pseudo-column fields at a time, select the pseudo-column fields that you want to delete and click **Delete** above the pseudo-column field list.
4. In the message that appears, click **OK**.

##### 3.5.4.4 View the details of a pseudo-column field

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Data Watermarking > Pseudo Column Management**.
3. Find the pseudo-column field that you want to view and click **View** in the Operation
column.

#### 3.5.5 Distribution object management

##### 3.5.5.1 Add a distribution object

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Distribution Object Management** tab.
3. On the **Distribution Object Management** tab, click **Add** above the distribution object list.
4. In the **Add Distribution Target** dialog box, configure the following parameters and click
**Save**: Unit Name, Unit Code, Unit Type, Unit Level, and Description.
In the message that appears, click **OK**.

##### 3.5.5.2 Modify a distribution object

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Distribution Object Management** tab.
3. On the Distribution Object Management tab, find the distribution object that you want to
modify and click **Edit** in the Operation column.
4. In the **Edit Distribution Target** dialog box, modify the configurations and click **Save**.
In the message that appears, click **OK**.

##### 3.5.5.3 Delete one or more distribution objects

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Distribution Object Management** tab.
3. To delete a single distribution object, find the distribution object that you want to delete on
the Distribution Object Management tab and click **Delete** in the Operation column. To delete multiple distribution objects at a time, select the distribution objects that you want to delete and click **Delete** above the distribution object list.
4. In the message that appears, click **OK**.

##### 3.5.5.4 View the details of a distribution object

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Distribution Object Management** tab.
3. On the Distribution Object Management tab, find the distribution object that you want to
view and click **View** in the Operation column.
4. In the **View Distribution Target** dialog box, view the details of the distribution object.

#### 3.5.6 Data distribution management

> **Important:** After distribution objects are distributed, related watermarking tasks cannot be executed, modified, or deleted.

1. Log in to the Static Data Masking and Watermarking system.
2. Click **Data Watermarking**. Then, click the **Data Distribution Management** tab.
3. On the Data Distribution Management tab, find the distribution object that you want to
distribute in the Data Distribution List section and click **Distribute** in the Operation column. The distribution status is changed to Distributed. List of distributed data:

### 3.6 Data provenance

#### 3.6.1 Add a provenance task

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Click **Add Task**.
4. In the Add Trace Task dialog box, configure the Task Name, Task Type, and Data Source
parameters, and then click **Next**.
5. Click **Connect**. After the connection succeeds, select the source table and click **Save**.
A save success message is displayed. Click **OK**.

#### 3.6.2 Execute a provenance task

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Find the provenance task that you want to manage, and click **Run** in the Operation column.
4. Enter the username and password and click **Run Task**.

#### 3.6.3 Stop a provenance task

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Find the provenance task that you want to manage, and click **Stop** in the Operation
column.
4. In the dialog box that appears, click **OK**.

#### 3.6.4 Modify or delete a provenance task

**Modify a provenance task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Find the provenance task that you want to manage, and click **Edit** in the Operation column.
4. Modify the basic information and click **Next**. The task type cannot be modified.
5. Modify the table for source tracing and click **Save**.

**Delete a provenance task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Find the provenance task that you want to delete and click **Delete** in the Operation
column. Alternatively, select multiple provenance tasks and click **Delete** above the task list.
4. In the message that appears, click **OK**.

#### 3.6.5 View a provenance task

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Data Provenance > Provenance Tasks** tab.
3. Find the provenance task that you want to manage, and click **View** in the Operation
column.
4. In the dialog box that appears, view the data provenance details, including the provenance
task information and results. The provenance results include the distribution source, distribution object, distribution description (watermark content), and watermark task execution time.

### 3.7 K Anonymous Privacy Protection

**Protection**

#### 3.7.1 K-anonymity overview

This topic explains how to view the k-anonymity overview.
1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-anonymity overview** tab, enter search
criteria, and click **Search**. You can search by **data source**, **database name**, and **table name**.
3. Review the k-anonymization list.
The list shows the **data source**, **database name**, **table name**, **quasi-identifier**,
**sensitive attribute**, and **calculated k-value**.
4. Click k-value calculation to open the **k-value calculation** tab. For more information, see k-
value calculation.
5. Click anonymization task to open the **anonymization task** tab. For more information, see
anonymization task.

#### 3.7.2 K-value calculation

This topic describes how to add and manage k-value calculation tasks.

**Add and run a K-value calculation task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-value calculation** tab.
3. Click **Add Task**, select the data for k-value calculation, and then click **Next**.

| Parameter | Description |
|---|---|
| data source type | You can select database or file. Important Only DICOM files are supported. |
| data source | Select a specific data source. |
| schema name | This parameter is required only when the data source type is set to database. You can also select a schema name from the list that the system provides. |

| table name | This parameter is required only when the data source type is set to database. You can also select a table name from the list that the system provides. |
|---|---|

4. Classify the fields as **quasi-identifier** or **sensitive attribute**, and then click **Next**.
5. Set the **task name** and **task description**, and then click **Save**.
You can also use the default **task name** and **task description**.
6. On the **task list** page, in the **Actions** column, click **Run Task**.

**Edit a task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-value calculation** tab.
3. Enter search criteria and click **Search** in the upper-right corner.
4. Locate the target task. In the **Actions** column, click **More > Edit Task**, and then follow the
on-screen instructions to modify the task.

**View the task list and task details**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-value calculation** tab.
3. Enter search criteria and click **Search** in the upper-right corner.
4. Locate the target task. In the **Actions** column, click **More > task details**.

**View task history**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-value calculation** tab.
3. Enter search criteria and click **Search** in the upper-right corner.
4. Locate the target task and click **Task history** in the **Actions** column.
5. The task execution records are displayed.

**Delete a task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > k-value calculation** tab.
3. In the task list, select the tasks to delete and click **Delete** in the upper-right corner.

#### 3.7.3 Anonymization tasks

This topic describes how to create and manage anonymization tasks.

**Create and run an anonymization task**

1. Log in to the Static Data Masking and Watermarking system.
2. On the **k-anonymity privacy protection > anonymization task** tab, click **Add Task**.
3. Select the data source for the anonymization task and click **Next**.

| Parameter | Description |
|---|---|
| Data source type | Select whether the data source is a Database or a File. Important Only files in DICOM format are supported. |
| Data source | Specify the data source for the anonymization task. |
| Schema name | This parameter is required only when data source type is set to Database. You can also select a schema name from the system's auto-detected list. |
| Table name | This parameter is required only when data source type is set to Database. You can also select a table name from the system's auto-detected list. |

4. Configure the **field type** and **anonymization method**, and then click **Next**.

| Field type | Anonymization method |
|---|---|
| quasi-identifier | full masking (pattern) Numeric Age Gender Zip Code |
| Sensitive attribute | No anonymization method is required. |

5. Configure the **output target library**, **schema name/database name**, and **target k-**
**value**, and then click **Save**.
6. Return to the **task list**. In the **Actions** column, click **Run Task**.

**Edit task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > anonymization task** tab.
3. Enter search criteria and click **Search** in the upper-right corner to view the task list.
4. Find the target task. In the **Actions** column, choose **More > Edit Task**.

**View the task list and task details**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > anonymization task** tab.
3. Enter search criteria and click **Search** in the upper-right corner to view the task list.
4. Find the target task. In the **Actions** column, choose **More > task details**.

**View historical tasks**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > anonymization task** tab.
3. Enter search criteria and click **Search** in the upper-right corner to view the task list.
4. Find the target task and click **historical tasks** in the **Actions** column.
5. View the execution history of the task.

**Delete task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **k-anonymity privacy protection > anonymization task** tab.
3. In the task list, select the tasks to delete, and click **Delete** in the upper-right corner.

### 3.8 Column-level encryption

#### 3.8.1 Set column encryption

Column encryption is a data security capability that protects sensitive data in databases by storing specified columns in an encrypted form. It prevents unauthorized personnel from directly obtaining sensitive data in plaintext through cloud platform software or database connection tools. This effectively mitigates both internal and external security threats and safeguards data security. This topic describes how to configure column encryption.

**Overview**

The column encryption feature consists of **encryption settings** and **database account**
**permissions**. The former defines the encryption algorithm, method, and scope, whereas the
latter controls which database accounts can access encrypted data and their permissions. The column encryption feature employs industry-standard encryption algorithms and uses local keys to encrypt columns.

> **Important:** PolarDB-X 2.0 also supports encryption with Key Management Service (KMS). Databases of other types do not support this method.

**Database types that support column encryption**

| Database type | Encryption method | Encryption algorithm |
|---|---|---|
| RDS PolarDB Oralce | Local encryption | AES 256 GCM _ _ |
| PolarDB-X 2.0 | Local encryption | AES 128 GCM, AES 128 CBC, AES 128 CTR, _ _ _ _ _ _ AES 128 ECB, AES 256 CBC, AES 256 CTR, _ _ _ _ _ _ AES 256 ECB, AES 256 GCM, SM4 128 CBC, _ _ _ _ _ _ SM4 128 CTR, SM4 128 ECB, and SM4 128 GCM _ _ _ _ _ _ |
|   | KMS-based encryption |   |

**Prerequisites**

The database has been added as a data source. For details, see Add one or more database sources. The data discovery task has been enabled for the data source. For details, see Create a data discovery task. Appropriate access permissions have been set for the database account. For details, see Configure database account permissions.

**Note**

For RDS PolarDB Oracle type databases, permission configuration cannot be performed​ before encryption is enabled. If you choose to use a key from KMS for encryption, ensure the key is created in KMS first.

**Set column encryption**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Column Encryption > Encryption Configuration** and set search conditions to
find the database for which you want to set column encryption. Search conditions include **Database Type**, **Encryption Status**, and **Data Source**.
3. Find the database that you want to encrypt and click **Encryption** in the **Operation** column.
4. In the **Encryption Configuration** dialog box, configure the **Encryption Algorithm**,
**Encryption Mode**, and **Plaintext Permission Accounts** parameters.
5. Filter the columns that you want to encrypt based on the search conditions, select the
columns that you want to encrypt, and then click **Enable Encryption** at the bottom of the page.

#### 3.8.2 Configure database account permissions

**permissions**

When you use the column encryption feature, fine-grained management of account permissions is particularly important. It determines which users can directly access the plaintext data of the encrypted column and which users can only view the encrypted results. This topic describes how to configure the permissions of a database account.

**Database account permission type**

The following three types of account permissions are supported.

| Permission | Description |
|---|---|

| Plaintext Permission | Allows accounts to access plaintext data of encrypted columns in the databases for which column encryption is enabled. |
|---|---|
| Ciphertext Permission (JDBC Decryption) | Allows accounts to access the ciphertext data of encrypted columns. The accounts can use an SDK to decrypt ciphertext data with an encryption key through an always-confidential client driver to view plaintext data. |
| Ciphertext Permission (No Decryption Permission) | Allows accounts to access only the ciphertext data of encrypted columns. The accounts cannot decrypt ciphertext data to view plaintext data. |

**Configure database account permissions**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Column Encryption > Encryption Configuration** and set search conditions to
find your target database.
3. Click **Permission Settings** in the **Operation** column.
4. The first time you configure permissions, click **Account Synchronization** at the bottom of
the page to obtain the database account list.
5. In the account list, find the account that you want to manage and click **Permission**
**Settings** in the **Operation** column.
6. Find the account for which you want to modify permissions and click **Modify Permissions**.
7. In the **Modify Permissions** dialog box, select a permission and click **OK**.

#### 3.8.3 Column encryption overview

This page provides an overview of column encryption across all connected databases.
1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Column Encryption > Encryption Configuration** tab to view the column
encryption overview.
**Total Columns**: Total number of columns in tables across all database instances
connected to DMS.
**Sensitive Data**: Statistics for your sensitive data, including the counts of sensitive,
encrypted, and unencrypted columns, and columns where encryption failed.
**Account Data**:
**Total Accounts**: Total number of database accounts. An account is counted for each
database it can access. For example, Account C with access to both Database A and B counts as two accounts.
**Plaintext Permission** or **Ciphertext Permission** count: The number of accounts
configured with permission to access encrypted data as either plaintext or ciphertext.
**Encryption Not Configured**: The status for accounts that have access to databases
where **column encryption is not configured**.

#### 3.8.4 Run an encryption task

This topic explains how to run an encryption task.

**Prerequisites**

You have added a database as a data source. For more information, see Add a database source. You have enabled a data discovery task for the data source. For more information, see Add a data discovery task. You have granted the required permissions to the database account. For more information, see Configure database account permissions.

> **Important:** For RDS PolarDB for Oracle databases, we recommend that you use one-click encryption to configure database account permissions before you configure the encryption task.

You have configured an encryption rule. For more information, see Configure an encryption rule.

**Run an encryption task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Column Encryption > Encryption Task** tab, and then click **Add Task**.
3. On the **Add Task** tab, configure the parameters and click **Save**.

| Parameter | Description |
|---|---|
| Task Name | Enter a custom task name. |
| Encryption Rule | Select the encryption rule that you configured. |
| Start Time | The schedule for the task. Select Manual for a one-time execution or Periodic to run the task daily. If you select Periodic, you must also configure Execution Time and End Time. |
| Database Type | Select the type of database. |
| Data Source | Select a data source. |
| Encryption Algorithm | Select an encryption algorithm. If a data source does not support the selected algorithm, the system uses its default algorithm. The default algorithm for RDS PolarDB for Oracle is AES-256-GCM. |
| Encryption Method | Select Local Key or KMS Key. If you select KMS Key, you must also select a Key ID. Note Only PolarDB-X 2.0 databases support encryption using a KMS key. |
| Task Description | Enter a custom description. |

After a task is created, you can find it in the **Encryption Task List** to **Run**, **Edit**, or **View**
**Details**.

**View task execution history**

1. In the **Encryption Task List**, find the target task.
2. In the **Actions** column, click **Execution History** to view its run history.
**View Details**: Shows the run status of the data source, including the database name,
total number of tables, and the number of successful and failed operations. Click **View**
**Details** again to view the encryption status of each table.
**Download**: Displays a link to download the log. Copy and paste the link into your browser
to download the log.
**Task Details**: Displays the task's configuration details.

**Delete a task**

1. In the **Encryption Task List**, find the target task.
2. Select the checkbox next to the task and then click **Delete**.
3. In the **Message** dialog box, click **OK**.

#### 3.8.5 Set encryption rules

This topic describes how to add, edit, and delete an encryption rule.

**Add an encryption rule**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Column Encryption > Encryption Rule** and click **Add Rule**.
3. In the **Add Rule** panel, configure the parameters and click **Save**.

| Parameter | Description |
|---|---|
| Rule Name | Enter the name of the rule. |

| Template | Select a template from the drop-down list. The available templates are synchronized from the templates configured in the SDDP. |
|---|---|
| Detection Models | Select a detection model. |
| Risk Level | Select a risk level. |
| Description | Enter a custom description. |

**Edit an encryption rule**

1. In the **Encryption Rule List** section, find the encryption rule that you want to modify.
2. Click **Edit** in the **Operation** column.
3. Click **Save** after modification.

**Delete an encryption rule**

> **Important:** You can delete only encryption rules that are not associated with encryption tasks.

1. In the **Encryption Rule List** section, select the encryption rule that you want to delete.
2. In the upper-right corner of the page, click **Delete**.
3. In the **Confirm** dialog box, click **OK**.

#### 3.8.6 Download encryption logs

This topic describes how to download encryption task logs.

**Download encryption logs**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Column Encryption > Encryption Log**.
3. In the Query Conditions section, fill in the **Task Name** or **Status** field to query.
4. In the **Encryption Task Log List** section, click **Download** in the **Operation** column.
5. The encryption task download link appears. You can copy the link to the browser to
download the log to your computer.

### 3.9 Configurations

#### 3.9.1 Lookup table management

A lookup table defines the mappings for substitution-based data masking algorithms. The same data will produce different masking results after a substitution algorithm is performed by using different lookup tables.

**Add a lookup table**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration** tab. Then, click the **Code Table Management** tab.
3. Click **Add**.
4. In the **Add Code Table** dialog box, configure the Name, System Version, Max Year, Type,
Enable Code Table, and Allow Export parameters. Valid values for the Type parameter: Token Generation and File Import. When you set the Type parameter to Token Generation, you can click **Auto Generate** to generate a random string. When you set the Type parameter to File Import, you can import a lookup table file that is exported from another Static Data Masking and Watermarking system.
5. Click **Ok**.

**Enable or disable a lookup table**

1. On the **Configuration > Code Table Management** tab, find the lookup table that you
want to manage.
2. Click **Enable** or **Disable** in the **Status** column to disable or enable the lookup table.

> **Important:** If a masking task associated with the lookup table is running when you disable the lookup table, an error message is displayed and the lookup table cannot be disabled.

**View the token for a lookup table**

1. On the **Configuration > Code Table Management** tab, find the lookup table that you
want to manage.
2. Click the
icon in the Oper column.

**Export a lookup table file**

1. On the **Configuration > Code Table Management** tab, find the lookup table that you
want to manage.
2. Click the
icon in the Oper column.
3. In the dialog box that appears, configure the Expiration Date parameter and click **Ok**.

**Delete a lookup table**

1. On the **Configuration > Code Table Management** tab, find the lookup table that you
want to manage.
2. Click the
icon in the Oper column.
3. In the message that appears, click **OK** to delete the lookup table.
If an existing masking task is associated with the lookup table, a message appears indicating the existing association and the deletion fails.

#### 3.9.2 Data dictionary

**Add a data dictionary**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Configuration > Data Dictionary**.
3. In the left-side dictionary list, click the
icon.
4. In the **Add Dictionary** dialog box, configure the Dictionary Name, Group Column Number,
and Unique Column Number parameters. If the data dictionary is a grouped dictionary, you need to specify the Group Column Number parameter. Separate multiple columns with commas (,). If the data dictionary is a general data dictionary, leave the Group Column Number parameter empty.
5. Click **Save**.

**Modify a data dictionary**

1. In the left-side dictionary list, click the
icon to the right of the added data dictionary.
2. In the **Edit Dictionary** dialog box, modify the data dictionary information. The Unique
Column Number parameter cannot be modified. Click **Save**.

**Delete a data dictionary**

1. In the left-side dictionary list, click the
icon to the right of the added data dictionary.
2. In the message that appears, click **OK**.

**Configure dictionary content**

**Single addition**

1. Choose **Configuration > Data Dictionary** , and click the added data dictionary in the left-
side dictionary list.
2. In the right-side dictionary details list, click the
icon.
3. In the Add Dictionary Content dialog box, enter the dictionary content and click **Ok**.

**Batch addition**

1. In the left-side dictionary list of the **Configuration > Data Dictionary** tab, click the added
data dictionary.
2. In the right-side dictionary details list, click the
icon.
3. In the **Upload Dictionary Content** dialog box, click **Dictionary Template Download** to
download a TXT file.
4. Open the downloaded TXT template file, enter the dictionary content as prompted, and
then save the file.
5. Go back to the **Upload Dictionary Content** dialog box, click the
icon, select the template file that you saved, and then select **Column Bounder**.
6. Click **Save**.

**Update dictionary content**

**Modify dictionary content**

1. In the right-side dictionary details list, find the dictionary content that you want to modify
and click the icon in the Oper column.
2. In the dialog box that appears, modify the dictionary content and click **OK**.

**Delete dictionary content**

1. In the right-side dictionary details list, find the dictionary content that you want to delete
and click the icon in the Oper column.
2. In the message that appears, click **OK**.

**Archive a data dictionary**

**Important**

> A data dictionary can be used only after it is archived. After a data dictionary is archived, you cannot modify or delete the dictionary content.

1. Choose **Configuration > Data Dictionary**, and click the added data dictionary in the left-
side dictionary list.
2. In the right-side dictionary details list, click the
icon.
3. In the message that appears, click **OK**.

**View a data dictionary**

1. Choose **Configuration > Data Dictionary**, and in the left-side dictionary list, click the
icon to the right of the data dictionary that you want to view.
2. In the **View Dictionary** dialog box, view the information about the data dictionary and
click **Close**.
3. In the left-side dictionary list, click the data dictionary that you want to view.
4. In the right-side dictionary details list, you can view the content in the data dictionary.

#### 3.9.3 Custom functions

You can write a custom function in JavaScript for sensitive data discovery. The input is the data to be checked for sensitive information, and the function returns true or false based on logical conditions.

**Add a custom function**

**Manually add a custom function**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Configuration > Custom Functions**.
3. In the left-side custom function list, click the
icon.
4. Configure the **Custom Function Name** and **Custom Discovery Rule Function**
parameters, enter test data, and then click **Test**.
5. After the test is passed, click the
icon in the upper-right corner.

**Import a custom function**

1. Prepare a custom function file in the TXT format.
The following sample code shows the file content format. The `value` field is a fixed field, and its value is the custom function rule. The custom function rule is in string format. If it is in another format, it needs to be converted to string format. `{`

```json
    "value": "function customRuleMatch(paramValue) {\r\n    if(paramValue > 60){\r\n
return true;\r\n }\r\n else{\r\n return false;\r\n }\r\n}\r\n"
```

`}`
2. Log in to the Static Data Masking and Watermarking system.
3. Choose **Configuration > Custom Functions**.
4. In the left-side custom function list, click the
icon.
5. In the **Import** dialog box, select the function rule file that you prepared and click **Import**.
After the function rule file is imported, the name of the custom function is automatically generated in the `Import Function_Import Time` format and displayed in the Custom Function List section. You can change the name of the custom function.

**Modify a custom function**

1. Choose **Configuration > Custom Functions**, and find the custom function that you want
to manage in the left-side custom function list.
2. Click the
icon to the right of the custom function.
3. Modify the **Custom Function Name** and **Custom Discovery Rule Function** parameters.
Click Test to perform a test. Then, click the icon in the upper-right corner.

**Export a custom function**

1. Choose **Configuration > Custom Functions**, and find the custom function that you want
to manage in the left-side custom function list.
2. Click the
icon to the right of the custom function.
3. Download the TXT file named **Custom Function Name**. The following code shows its
content. `{`

```json
    "name": "test",
    "value": "function customRuleMatch(paramValue) {\r\n    if(paramValue > 60){\r\n
return true;\r\n }\r\n else{\r\n return false;\r\n }\r\n}\r\n"
```

`}`

**Delete a custom function**

1. Choose **Configuration > Custom Functions**, and find the custom function that you want
to manage in the left-side custom function list.
2. Click the
icon to the right of the custom function.
3. In the dialog box that appears, click **OK**.

#### 3.9.4 Discovery rules

**Add a custom rule**

1. Log in to the Static Data Masking and Watermarking system.
2. Choose **Configuration > Discovery Rules**.
3. In the left-side Discovery Rule List section, click the
icon.
4. In the right-side pane, configure the basic information of the rule, including the rule name
and discovery mode. If you set **Discovery Mode** to **Discover by Custom Logic**, sensitive data is identified based on a regular expression. If data matches the regular expression, the data is considered sensitive data. In this mode, you need to configure **Confirmation Ratio**, Pre-judgment Settings, DISCOVERY LOGIC SET, and Recommended Mask Algorithm. When the percentage of sampled data identified as sensitive reaches the confirmation ratio, the column is considered as sensitive data of this discovery rule type.
**Pre-judgment Settings** are optional. You can configure a custom rule for the number of
characters or character positions to verify data before the regular expression is matched. If the data does not meet the pre-judgment rule, the data is considered non-sensitive, and the regular expression is not matched. On the **Pre-judgment Settings** tab, select a rule type (Character Quantity Rule or Character Position Rule), and then click the icon. If you set **Discovery Mode** to **Discover by Complex Method**, when a single column stores multiple types of sensitive data in fixed-length or delimiter-separated formats (Examples: fixed-length data such as "01200501013015001234567", where the first 12 digits represent a fixed student ID and the last 11 digits represent a fixed mobile number, with a total fixed length of 23 characters; or delimiter-separated data such as "Zhang San|15001234567", where the Chinese name and mobile number are separated by "|"), a composite discovery rule can be used. By configuring discovery rules based on the data format, this method enables the identification of multiple types of sensitive data within the same column and must be used in conjunction with a composite data masking algorithm. In this mode, you need to configure the **Confirmation Ratio** parameter. On the **Data**
**Splitting** tab, select the split type (Split by Bits or Split by Separator). On the
**Recommended Mask Algorithm** tab, select a recommended data masking algorithm
(typically a custom composite data masking algorithm).
**Data splitting**:
If you set **Split Type** to **Split by Bits**, input sample data, and then click **Split** to obtain the digit-position split chart (which shows from which digit to which digit the sensitive data resides). You can click **Add Interval** to add a sensitive data range, specify the start and end digits of sensitive data, and specify the discovery rule for detecting sensitive data. You can add multiple intervals. If you set **Split Type** to **Split by Separator**, enter a delimiter. Then, click the icon on the right for each additional separator you want to add. After you add all the delimiters, input sample data, and click Split. Then, select a discovery rule for each segment separated by the delimiters.
5. In the Test Sample section, enter test data and click **Test**.
6. After the test is passed, click the
icon in the upper-right corner.

**Update a discovery rule**

**Update a custom discovery rule**

1. In the left-side Discovery Rule List section of the **Configuration > Discovery Rules** tab,
find the custom discovery rule that you want to manage.
2. Click the
icon to the right of the custom discovery rule.
3. Modify the configurations of the custom discovery rule and click the
icon in the upperright corner.

**Modify the confirmation ratio of a built-in discovery rule**

1. Choose **Configuration > Discovery Rules**, and in the left-side Discovery Rule List
section, expand the built-in discovery rule that you want to manage.
2. Click the built-in discovery rule. In the Basic Rule Information section, click **Modify** next to
**Confirmation Ratio**.
3. Enter a new value and click **Save**.

**Delete a custom discovery rule**

1. In the left-side Discovery Rule List section of the **Configuration > Discovery Rules** tab,
expand the custom discovery rule that you want to manage.
2. Click the
icon to the right of the custom discovery rule.
3. In the dialog box that appears, click **OK**.

#### 3.9.5 Data masking algorithm

**Add a custom algorithm**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > Data Masking Algorithm** tab.
3. In the data masking algorithm list on the left, click the Add Custom Algorithm
icon.
4. On the right, set the algorithm name and algorithm type.
The following table describes the **Algorithm Type** options.
**Composite masking algorithm**: Masks sensitive data structured into multiple
segments. This algorithm is useful when multiple types of sensitive data are stored in the same row and column, using fixed length or a delimiter. It uses a composite discovery rule to apply the corresponding basic masking algorithm to each segment. For more information about discovery rules, see the **Discovery Rules** chapter. You cannot create a composite masking algorithm without a corresponding composite discovery rule.
**Mixed masking algorithm**: Masks different types of sensitive data mixed within the
same column across different rows. It identifies the data type in each row based on a prioritized list of discovery rules and applies the corresponding basic masking algorithm. In the **Masking Parameters** section, click **Add Basic Algorithm** to associate a discovery rule with a specific data masking algorithm and its parameters. You can repeat this step to add multiple rules. The mixed masking algorithm processes data by checking it against discovery rules by priority. If the data matches the first rule, the system applies the corresponding data masking algorithm. If not, the system checks the data against the second rule, and so on.
**Custom function algorithm**: Uses a custom JS function to mask data. It takes the
original data as input and returns the masked data. This algorithm is ideal for masking tasks that require custom business logic. In the **Masking Parameters** section, enter your JS function in the **Custom masking**
**algorithm****function** field.
**Text masking algorithm**: Masks large blocks of text containing various types of
sensitive information, such as names and locations. In the **Masking Parameters** section, click **Add Basic Algorithm** to associate a discovery rule with a specific data masking algorithm and its parameters. You can repeat this step to add multiple rules.
5. In the **Data Masking Algorithm Test** section, enter sample data, then click **Masking**
**Test** and **Restoration Test** (available only for reversible algorithms).
6. After the test passes, click the Save
icon in the upper-right corner.

**Edit a custom data masking algorithm**

Pre-defined data masking algorithms cannot be edited.
1. On the **Configuration > Data Masking Algorithm** tab, find your custom algorithm in the
list on the left.
2. Click the Edit
icon for the custom algorithm.
3. Modify the configuration (the **Algorithm Type** cannot be changed), and then click the Save
icon in the upper-right corner.

**Test a data masking algorithm**

1. On the **Configuration > Data Masking Algorithm** tab, find the target algorithm in the
list on the left.
2. In the **Data Masking Algorithm Test** section, select an appropriate code table, enter
sample data, and then click **Masking Test** and **Restoration Test** (available only for reversible algorithms).

**Delete a custom algorithm**

Pre-defined data masking algorithms cannot be deleted.
1. On the **Configuration > Data Masking Algorithm** tab, find your custom algorithm in the
list on the left.
2. Click the Delete
icon for the custom algorithm.
3. In the confirmation dialog box, click **OK**.

#### 3.9.6 Scheduled tasks

You can use a scheduled task to call the discovery task, masking task, automatic masking task, queue task, and watermarking task once at a specific time or periodically.

**Add a scheduled task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > Scheduled Tasks** tab.
3. In the Schedule Task List section, click the
icon
4. In the right-side pane, configure the parameters such as Schedule Task Name, Task Type,
Task List, Execution Type, and Whether to Enable. Then, click **Test Connection**. Valid values for the Task Type parameter: Discovery Task, Mask Task, Automatic Mask Task, Mask Task Queue, and Water Task. Valid values for the Execution Type parameter: Single Execution, Execute once a day, Execution once a week, Execute once a month, Execution once a year, Interval hour execution, and Interval minutes execution.
5. After the source database is connected, click **Save**.

**Modify a scheduled task**

1. In the left-side scheduled task list of the **Configuration > Scheduled Tasks** tab, find the
scheduled task that you want to manage.
2. Click the
icon in the Oper column.
3. Modify the settings of the scheduled task parameters and click **Save**.

**View task execution records**

1. In the left-side scheduled task list of the **Configuration > Scheduled Tasks** tab, find the
scheduled task that you want to manage.
2. Click the
icon in the Oper column.
3. In the **Schedule Task History** dialog box, specify a time to view the execution records.

**Delete a scheduled task**

1. In the left-side scheduled task list of the **Configuration > Scheduled Tasks** tab, find the
scheduled task that you want to manage.
2. Click the
icon in the Oper column.
3. In the message that appears, click **OK**.

#### 3.9.7 Queue tasks

Multiple data masking tasks can be combined into one queue task and be executed in the specified sequence.

**Application scenarios**

You can use this feature if you want to execute multiple data masking tasks in sequence at a time. For more information about how to configure a data masking task, see **Data masking**
**> Data masking task**.

**Add a queue task**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > Queue Tasks** tab.
3. Click **Add queue task**.
4. In the Add queue task dialog box, enter a queue task name, select the data masking tasks
that you want to execute, and set the execution order. You can select **Ignore single task errors, other tasks continue to run**. In this case, if a task fails to be executed, the execution of subsequent tasks is not affected.

**Modify a queue task**

1. In the queue task list, find the queue task that you want to manage.
2. Click **Edit** in the operation column.
3. Modify the queue task name, data masking tasks, and their execution sequence, and then
click **Save**.

**Execute a queue task**

1. In the queue task list, find the queue task that you want to manage.
2. Click **Run Queue** in the operation column.

**View the execution records of a queue task**

1. In the queue task list, find the queue task that you want to manage.
2. Click **View Detail** in the operation column.
3. In the **View queue details** dialog box, find the data masking task that you want to view
and click **View Detail** in the operation column.
4. In the **Mask Task History** dialog box, specify a time range to view the execution records.
For more information, see **Data masking > Data masking task > View historical**
**tasks**.

**Delete a queue task**

1. In the queue task list, select the queue task that you want to delete.
2. Click **Delete queue task** above the list.
3. In the message that appears, click **OK**.

#### 3.9.8 Masking algorithm templates

A masking algorithm template specifies the masking algorithm and parameters to use for a particular type of sensitive data.

**Add a masking algorithm template**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > Masking Algorithm Templates** tab.
3. In the left-side Mask Algorithm Template List section, click the
icon.
4. In the **Add Mask Algorithm Template** dialog box, configure the Template Name and Out
of template processing strategy parameters, and then click **Save**.
5. In the right-side Template Details List section, click the
icon.
6. In the**Add Mask Algorithm Template Content**dialog box, configure the discovery rule,
masking algorithm, and algorithm parameters of the template, and then click Save.
7. Repeat the previous step to add multiple discovery rules, masking algorithms, and
algorithm parameters.

**Modify a masking algorithm template and its content**

1. On the **Configuration > Masking Algorithm Templates** tab, find the masking algorithm
template that you want to manage in the left-side masking algorithm template list.
2. Click the
icon to the right of the template that you want to modify.
3. Modify the settings of the Template Name and Out of template processing strategy
parameters. You cannot modify the name of the default template. Then, click **Save**.
4. In the right-side Template Details List section, find the entry that you want to modify and
click the icon in the Oper column.
5. In the dialog box that appears, modify the discovery rule, masking algorithm, and algorithm
parameters, and then click **Save**.

**Export a masking algorithm template**

1. On the **Configuration > Masking Algorithm Templates** tab, find the masking algorithm
template that you want to manage in the left-side masking algorithm template list.
2. Click the
icon to the right of the template that you want to export.
3. Follow the on-screen instructions to download and save the CSV file.

**Import a masking algorithm template**

1. Edit the exported CSV file.
2. On the **Configuration > Masking Algorithm Templates** tab, find the masking algorithm
template that you want to manage in the left-side masking algorithm template list.
3. Click the
icon to the right of the template that you want to import.
4. Follow the on-screen instructions to upload the CSV file of the masking algorithm template
and configure the template file parameters.
5. Click **Import**.

**Delete a masking algorithm template and its content**

1. On the **Configuration > Masking Algorithm Templates** tab, click the masking
algorithm template that you want to manage in the left-side masking algorithm template list.
2. In the right-side Template Details List section, find the entry that you want to delete and
click the icon in the Oper column.
3. In the message that appears, click **OK**.
4. In the left-side Masking Algorithm Template List section, click the
icon to the right of the template that you want to delete.
5. In the message that appears, click **OK**.

#### 3.9.9 File templates

A file template specifies whether a file contains information such as a table header, character set, field separator, and field enclosure. Such information is used for file parsing in discovery tasks and source file masking.

**Add a file template**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > File Templates** tab.
3. In the left-side file template list, click the
icon.
4. Configure the file template information and click **Save File Template**.

**Modify a custom file template**

You cannot modify the default template.
1. On the **Configuration > File Templates** tab, find the file template that you want to
manage in the left-side file template list.
2. Click the
icon to the right of the template that you want to modify.
3. Modify the file template information and click **Save File Template**.

**Clone a file template**

1. On the **Configuration > File Templates** tab, find the file template that you want to
manage in the left-side file template list.
2. Click the
icon to the right of the template that you want to clone. A new file template is generated. The name of the new file template is in the `Source file` `template name_Number` format.

**Delete a file template**

1. On the **Configuration > File Templates** tab, find the file template that you want to
manage in the left-side file template list.
2. Click the
icon to the right of the template that you want to delete.
3. In the message that appears, click **OK**.

#### 3.9.10 Parameter configuration

**Modify parameter configurations**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration > Parameter Configuration** tab.
3. In the parameter configuration list, find the configuration item name that you want to
manage and modify the value in the **Attribute Value** column.
4. Click the
icon in the **Oper** column. You can click the icon in the upper-right corner of the list to save all configuration item changes.

**Restore parameter configurations**

1. In the parameter configuration list, find the configuration item name that you want to
manage.
2. Click the
icon in the **Oper** column. You can click the icon in the upper-right corner of the list to restore all configuration item changes.

#### 3.9.11 Database driver management

**Add a database driver**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration** tab. Then, click the **Database Driver Management** tab.
3. Click **Add Database Driver**.
4. After you select a database type from the **Database Type** drop-down list, the system
automatically generates **Database Driver Name**. You can modify the database driver name. Then, upload a driver file and click **Save**.

**Apply a database driver**

On the **Data Sources > Database Sources** tab, click Create Database Source. In the dialog box that appears, click Expand Advanced Options, and set **Custom Database Driver** to the database driver you added. For more information, see **Data sources > Database sources**
**> Create a database source**.

#### 3.9.12 Host configuration

**Add a host**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Configuration** tab. Then, click the **HOST Configuration** tab.
3. Click the
icon.
4. Configure the **Host IP** and **Host Name** parameters, and then click the
icon.

**Modify a host**

1. In the host configuration list, find the host that you want to manage.
2. Click the
icon in the **Oper** column.
3. Modify the **Host IP** and **Host Name** parameters, and then click the
icon.

**Delete a host**

1. In the host configuration list, find the host that you want to manage.
2. Click the
icon in the **Oper** column. Alternatively, select the hosts that you want to delete and click the icon above the list to delete the selected hosts at a time.
3. In the message that appears, click **OK**.

### 3.10 Maintenance

**Data source detection**

1. Log in to the Static Data Masking and Watermarking system.
2. Click the **Maintenance** tab.
3. Select the database source, data source detection type (All, Source, or Target), and the
parameters to be checked. Click a check option to download the SQL script.
4. Click **Start** in the upper-right corner to start the check.
5. After the check is complete, view the check results in the **Database Source Diagnostic**
**List** section. Click the
icon in the **Operation** column to download the check results.
