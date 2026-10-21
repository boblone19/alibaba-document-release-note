---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 141
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Data%20Management%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Data Management User Guide 20220928

## Table of Contents

- 1 What is DMS?
- 2 Quick start
  - 2.1 Log on to the DMS console
  - 2.2 Customize the top navigation bar
  - 2.3 Add an instance
  - 2.4 Add a user
  - 2.5 Use the sharing feature
- 3 Control modes
- 4 Features that are supported by each role
- 5 Apply for permissions
- 6 SQLConsole
  - 6.1 Single database query
  - 6.2 Cmd Tab
  - 6.3 Super SQL mode
  - 6.4 Cross-database query
- 7 Data plans
  - 7.1 Change data
  - 7.2 Import data
  - 7.3 Data export
  - 7.4 Generate test data
  - 7.5 Clone databases
- 8 Data factory
  - 8.1 Task orchestration
  - 8.2 Data warehouse development
    - 8.2.1 Overview
    - 8.2.2 Create a data warehouse project
    - 8.2.3 Create or import an internal table
    - 8.2.4 Manage task flows
    - 8.2.5 Use the data service feature
  - 8.3 Data service
    - 8.3.1 Overview
    - 8.3.2 Develop an API
    - 8.3.3 Unpublish or test an API
    - 8.3.4 Test an API
    - 8.3.5 Call an API
- 9 Schemas
  - 9.1 Schema design
  - 9.2 Schema synchronization
  - 9.3 Synchronize shadow tables
  - 9.4 Initialize empty databases
  - 9.5 Repair table consistency
- 10 SQL review
- 11 System management
  - 11.1 Manage instances
  - 11.2 Database management
  - 11.3 Manage users
  - 11.4 Enable metadata access control
  - 11.5 Manage tasks
  - 11.6 Configuration management
  - 11.7 Database grouping
  - 11.8 Security management
    - 11.8.1 Manage security rules
    - 11.8.2 DSL syntax for security rules
    - 11.8.3 Configure security rules for a database instance
    - 11.8.4 Customize approval processes
    - 11.8.5 Operation audit
    - 11.8.6 Configure IP whitelists
    - 11.8.7 Row-level control
    - 11.8.8 Manage sensitive data
    - 11.8.9 Data protection
  - 11.9 Security rules
    - 11.9.1 Overview of security rule sets
    - 11.9.2 Manage security rules under checkpoints
    - 11.9.3 SQLConsole for relational databases
    - 11.9.4 SQLConsole for MongoDB
    - 11.9.5 SQLConsole for Redis
    - 11.9.6 Data change
    - 11.9.7 Permission application
    - 11.9.8 Data export
    - 11.9.9 Schema design
    - 11.9.10 Database and table synchronization
    - 11.9.11 Sensitive field change
    - 11.9.12 Test data generation
    - 11.9.13 Database cloning

## 1 What is DMS?

Data Management (DMS) is a fully managed service that is provided by Alibaba Cloud. This service allows you to manage data, schema, development procedures, development specifications, users, and permissions. DMS also provides security control to ensure secure access to databases. Supported databases Relational databases: MySQL, SQL Server, PostgreSQL, PolarDB-X (previously called DRDS), Oracle, and ApsaraDB for OceanBase. NoSQL databases: ApsaraDB for Redis and ApsaraDB for MongoDB. Analytical databases: AnalyticDB for MySQL and AnalyticDB for PostgreSQL. Features DMS provides support for the database development process. The process includes the following stages: 1. Design table structures in an on-premises environment based on the predefined design specification. 2. Publish and produce SQL reviews that are included in code and schemas to a specified environment on demand. The SQL reviews are included in code in schemas. The SQL reviews in code are used to add, remove, modify, or query rows. DMS provides fine-grained access control at the database, table, or field level. You can perform the required operations on databases in the DMS console. The operations can be traced and audited. DMS allows you to configure the required operation specifications and approval processes for multiple modules. These modules include the schema design, data change, data export, and permission request. DMS integrates database development with database interaction. You can manage databases without the need to switch between database endpoints at a high frequency by using database accounts and passwords. DMS provides the task orchestration feature. This feature allows you to orchestrate and schedule SQL tasks for databases on a regular basis. You can use this feature to perform the required operations with ease. For example, you can dump historical data, analyze periodical reports, and generate analytical results.

## 2 Quick start

### 2.1 Log on to the DMS console

This topic uses Google Chrome to describe how to log on to the Data Management (DMS) console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click Login.
4. In the top navigation bar, move the pointer over Product s and click Dat a Management under
Dat abase Services.
5. Set the Organizat ion and Region parameters and click DMS.

> Not e If you log on to the DMS console as a DMS administrator and your account is added to multiple tenants, you can move the pointer over the
> icon in the upper-right corner and
> select Swit ch t enant to switch to another tenant.

### 2.2 Customize the top navigation bar

Data Management (DMS) allows you to customize the top navigation bar so that you can access the features that are commonly used in DMS with ease. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon.
3. Turn on the
switch in the upper-right corner so that you can customize the top navigation bar. on: You can customize the top navigation bar. off: By default, all features are displayed. You cannot customize the top navigation bar.
4. Find a feature that you want to add to favorites and click the
icon. The feature is displayed in the top navigation bar.

> Not e If a great many features are added to favorites, move the pointer over More in the top navigation bar to view the favorite features that are hided.

### 2.3 Add an instance

Before you can manage database instances in Data Management (DMS), you must add database instances to DMS. DMS allows you to add ApsaraDB instances and self-managed database instances for which public IP addresses are specified. This topic describes how to add an ApsaraDB RDS for MySQL instance to DMS. Procedure
1. Log on to the DMS console.
2. In the left-side navigation pane, click Add Inst ance.

> Not e You can also click the + icon in the left-side navigation pane to add an instance.

3. In the Add Instance dialog box, click the Cloud tab.
4. On the Cloud tab, select the type of the instance.
5. In the Basic Information section of the dialog box, set the required parameters. This example shows
how to add an ApsaraDB RDS for MySQL instance.

| Section | Parameter | Description |
|---|---|---|
| Basic Inf ormat ion | Dat a Source | The source of the database. In this example, select Cloud. |
|   | Dat abase T ype | The type of the database. In this example, select MySQL. |
|   | Inst ance Area | The area where the database instance resides. Select a region from the drop-down list. |
|   | Ent ry mode | Valid value: Connect ion st ring address. |
|   | Connect ion st ring address | The endpoint of the database instance. The endpoint contains a port number. |
|   | Dat abase account | The username of the account that is used to log on to the database of the instance. |
|   | Dat abase password | The password of the account. |

|   | User Guide·Quick star |   |
|---|---|---|
| Section | Parameter | Description |
|   | Cont rol Mode | The control mode that is used to manage the database. For more information, see Control modes. Not e If you set this parameter to Securit y Collaborat ion, you must set the Securit y Rules parameter. |
| Advanced Inf ormat ion | Environment t ype | The type of the environment to which the database instance belongs. |
|   | Inst ance Name | The name of the database instance. |
|   | Enable DSQL | Specifies whether to enable the cross-database query feature. To enable the cross-database query feature, you must specify the name of a custom database link. For more information, see Cross-database query. |
|   | Lock-f ree Schema Change | Specifies whether to enable the lock-free schema change feature. |
|   | DBA | The database administrator (DBA) of the database instance. The DBA is used to handle approval processes, such as permission requests. |
|   | query t imeout (s) | The security policy. When the specified timeout period is reached, the execution of the SQL statement is terminated. This way, the security of the database is ensured. |
|   | export t imeout (s) | The security policy. When the specified timeout period is reached, the execution of the SQL export statement is terminated. This way, the security of the database is ensured. |

6. After the preceding parameters are set, click Basic Inf ormat ion and click T est connect ion to
verify the settings.

> Not e If the connection test fails, check the specified parameters based on the error message that appears.

7. Click Submit .
Result After the preceding steps are performed, the ApsaraDB instance is added to DMS. You can view and manage your database instance in the left-side navigation pane of the DMS console.

### 2.4 Add a user

Data Management (DMS) allows you to manage users. You can add users and assign the required roles to each user based on your business requirements. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose Syst em > User.

> Not e On the User tab, you can perform the required operations on the existing users. For example, you can edit, disable, enable, or delete a user.

3. Click New.
4. In the Add User dialog box, set the required parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Alibaba Cloud Account | The ID of an Apsara Stack tenant account. You can enter one of the following IDs: The ID of an Apsara Stack tenant account. You can obtain the ID from the account owner. The ID of a Resource Access Management (RAM) user. You can obtain the required ID from the Service-linked Roles page of the Apsara Uni-manager Management Console. |
| Role | The role that you want to assign to the user based on your business requirements. Valid values: Regular User DBA Administrator Security Administrator Technical Support Not e For more information about the features that are supported by each role, see Features that are supported by each role. |

5. Click OK.

### 2.5 Use the sharing feature

Data Management (DMS) provides the sharing feature for you to share an SQLConsole tab or a ticket. You can use a share link to access an SQLConsole tab or a ticket with ease. This improves efficiency. This topic describes how to use the sharing feature in DMS. Scenarios You can share historical tickets. This improves the audit efficiency of security administrators. You can obtain the information about historical changes to databases based on the share links of historical data change tickets. You can query and update databases based on the share links of SQLConsole tabs. Share an SQLConsole tab
1. Log on to the DMS console.
2. In the left-side navigation pane, enter the name of a database in the search box and press the
Enter key. From the matched results, click the instance in which the database resides and doubleclick the database. The SQLConsole tab appears.
3. On the SQLConsole tab, click the
icon in the upper-right corner.

> Not e You can share the SQLConsole tab of a database only after you obtain the permissions on the database. Otherwise, the
> icon is not displayed.

4. In the dialog box that appears, click Open sharing.
5. Set the parameters as required.

| Parameter | Description |
|---|---|
| Sharing f orm | The content to be shared. Valid values: Console only and Console + SQL. Console only: the SQLConsole tab without SQL statements. Console + SQL: the SQLConsole tab including the SQL statements that you entered. |
| Sharing period | The validity period of the share link. Valid values: 7 Days, 30 Days, 180 Days, and 360 Days. |

6. Click Generat e and copy links.

> Not e After a share link is generated, you can turn off T urn of f sharing if you no longer want to share the SQLConsole tab. Then, the generated share link becomes invalid.

Share a ticket
1. Log on to the DMS console.
2. On the Workbench tab of the DMS console, click Submit t ed T icket s in the My T icket s section.
The My T icket s page appears.
3. On the My T icket s page, find the ticket that you want to share and click the ticket number to go
to the T icket Det ails page.

> Not e Schema design tickets cannot be shared.

4. On the T icket Det ails page, click the
icon in the upper-right corner.
5. In the dialog box that appears, click Open sharing.
6. Set the parameters as required.

| Parameter | Description |
|---|---|
| Share object | The recipients of the share link. You can specify one or more recipients. Valid values: Everyone and Designat ed. Everyone: all the users of the current DMS tenant. Designat ed: one or more specific users of the current DMS tenant. |
| Sharing period | The validity period of the share link. Valid values: 7 Days, 30 Days, 180 Days, and 360 Days. |
| Designat ed | The specific users to whom you want to send the share link. You can specify one or more users. Not e This parameter is displayed only after you set the Share object parameter to Designat ed. |

7. Click Generat e and copy links.

> Not e After a share link is generated, you can turn off T urn of f sharing if you no longer want to share the ticket. Then, the generated share link becomes invalid.

## 3 Control modes

DMS provides three control modes for you to manage instances: Flexible Management, Stable Change, and Security Collaboration. You can specify a control mode for each instance.

| Control mode | Description | Scenario | Logon method |
|---|---|---|---|
| Flexible management | This control mode allows you to manage the visualized data and schemas of multiple types of databases. It also provides a variety of data management solutions. This simplifies the use of databases and facilitates management. | Database instances do not require strict control. Database instances are used by a single user. | A database account and the related password. |
| Stable change | This control mode provides multiple solutions to ensure database reliability. These solutions allow you to change data without the need to lock the related table or schema. All features that are included in the flexible management control mode are available. | Database instances require a high level of availability. This ensures that these database instances function as expected for an extended period of time. Database instances are used by a small-sized group that includes multiple users. | A database account and the related password. |
| Security collaboration | This control mode provides multiple solutions to ensure data security. These solutions include fine-grained access control at the database, table, or field level and sensitive data management. This control mode allows you to produce enterprise-specific database DevOps solutions through custom design specifications and approval processes. All features that are included in the flexible management and stable change control modes are available. | Ensure the data security of database instances. Implement strict access control over development or change workflows. Manage compliance for enterprises. | Logon-free through authorization. |

> Not e The instances that are managed in Stable Change mode consume the billing quota of the instances that are managed in Security Collaboration mode.

rted by each role

## 4 Features that are supported by each role

by each role DMS provides the following roles: regular user, DBA, security administrator, and DMS administrator. This topic describes the features that are supported by each role.

| Category | Feature | Regular user | DBA | Security administ rator | DMS admini strato r | Description |
|---|---|---|---|---|---|---|
| Permission | Permissio n manage ment | √ | √ | √ | √ | You can use this feature to apply for permissions on instances, databases, tables, and sensitive fields. You can also view permissions that you have. |
| Data Plans | Data Changes | √ | √ | √ | √ | You can use this feature to initialize data for a newly published project, clean up historical data, fix bugs, or run a test. |
|   | Data Import | √ | √ | √ | √ | You can use this feature to import a large amount of data to your databases at a time. |
|   | Data Export | √ | √ | √ | √ | You can use this feature to export a large amount of data for analysis or export the required data. |
|   | Data Tracking | √ | √ | √ | √ | If specific data fails to meet your requirements due to reasons such as misoperation, you can use this feature to restore data to the normal state. |
|   | Test Data Generate | √ | √ | √ | √ | Some business scenarios may require frequent data preparation. In this case, you can use this feature to generate test data to ensure data security and discreteness and improve production efficiency. |

rted by each role

| Category | Feature | Regular user | DBA | Security administ rator | DMS admini strato r | Description |
|---|---|---|---|---|---|---|
|   | Data Warehou se Develop ment | √ | √ | √ | √ | DMS uses a database as a computing engine and integrates various tools and services, such as Data Transmission Service (DTS) and Data Lake Analytics (DLA), in the database ecosystem for data warehouse development. You can use this feature to develop and manage data warehouses in DMS with ease. |
|   | Data Service | √ | √ | √ | √ | You can use this feature to export data at the field or row level, display data in a visualized manner, and publish API operations to the Alibaba Cloud Marketplace for sale. |
|   | Database Clone | √ | √ | √ | √ | You can use this feature to clone MySQL databases. |
| Schemas | Schema Design | √ | √ | √ | √ | When you develop or optimize projects or process new business requirements, you can use this feature to change schemas. For example, you can use this feature to create a table or modify an existing table. |
|   | Table Sync | √ | √ | √ | √ | You can use this feature to compare and synchronize the schemas of tables in different environments, such as online and offline environments. This feature helps ensure the consistency of schemas. |
| Optimizati on | SQL Review | √ | √ | √ | √ | You can use this feature to prevent SQL statements that do not use indexes or do not conform to database development standards. This feature helps protect against SQL injection attacks. |

rted by each role

| Category | Feature | Regular user | DBA | Security administ rator | DMS admini strato r | Description |
|---|---|---|---|---|---|---|
| SQLConsol e | Single Database query | √ | √ | √ | √ | You can write SQL statements to query data in a single database. This feature can be used to verify business code, analyze product effects, and identify issues in an online environment. |
|   | Cross- database Query | √ | √ | √ | √ | You can use this feature to perform join queries across online heterogeneous databases that are deployed in different environments. |
| System Managem ent | Instance manage ment | × | √ | × | √ | You can use this feature to manage instances. For example, you can register, view, or edit instances. |
|   | User manage ment | × | × | × | √ | You can use this feature to manage users. For example, you can add, view, or edit users as needed. |
|   | Task manage ment | × | √ | × | √ | You can use this feature to manage tasks. For example, you can create, start, or stop tasks. |
|   | Configur ation manage ment | × | × | × | √ | You can use this feature to view and modify system configurations, or view the historical modifications of the configurations. |
|   | Security Rules | × | √ | × | √ | You can use this feature to configure security rules. Only SQL statements that conform to the security rules can be executed. |
|   | Approval Processe s | × | √ | × | √ | Approval processes are associated with security rules. You can configure different approval processes for different types of tickets. |

rted by each role

| Category Security | Feature | Regular user | DBA | Security administ rator | DMS admini strato r | Description |
|---|---|---|---|---|---|---|
| managem | Operatio n Logs | × | √ | √ | √ | Operations logs record data changes. Each record contains information such as the user who performed the operation, operation details, and time at which the operation was performed. You can use this feature to track historical user operations at any time. |
| ent |   |   |   |   |   |   |
|   | Access IP Whitelist s | × | × | × | √ | After you configure an access IP whitelist, only the IP addresses or Classless Inter-Domain Routing (CIDR) blocks in the whitelist can access the resources within your DMS tenant. This effectively enhances data security. |
|   | Sensitive Data | × | √ | √ | √ | You can use this feature to manage sensitive data. For example, you can use algorithms to de-identify sensitive data or adjust the security levels of sensitive data. |
| Tickets | Ticket manage ment | √ | √ | √ | √ | You can use this feature to configure notification methods. DMS can notify you of the approval or execution status of tickets by using DingTalk notifications or emails. |

## 5 Apply for permissions

You can apply for the query, change, and export permissions on a database, table, or column. After the database owner approves your application, you can query, change, and export data. Permissions Query permissions: the permissions to execute SQL statements in the SQLConsole to query the data of the object on which you want to apply for the permission. Change permissions: the permissions to submit tickets to change data or synchronize data in a database or table. You cannot change data without approval. Export permissions: the permissions to submit tickets to export data from the object on which you want to apply for the permission. You cannot export data without approval. Permission categories that are supported by each control mode

| Permission category | Permissions | Control mode |   |   |
|---|---|---|---|---|
|   |   | Flexible managem ent | Stable change | Security collabora tion |
| Inst ance logon | After you obtain the instance logon permission on an instance, you can use the preset database account and password to log on to the instance. | √ | √ | × |
| Dat abase | Database permissions are classified into query, export, and change permissions. After you obtain the database permissions on a database, you can access the following resources of the database: 1. All the insensitive fields. 2. All the tables to which row-level control settings are not applied. 3. All new tables. Query permission: You can execute SQL statements in the SQLConsole to query data. Change permission: You can submit data change and data import tickets. Export permission: You can submit data export tickets. | × | × | √ |

| Permission category | Permissions | Control mode |   |   |
|---|---|---|---|---|
|   |   | Flexible managem ent | Stable change | Security collabora tion |
| T able | Table permissions are classified query, export, and change permissions. After you obtain the table permissions on a table, you have full access to all data in the table except sensitive fields. Query permission: You can execute SQL statements in the SQLConsole to query data. Change permission: You can submit data change and data import tickets. Export permission: You can submit data export tickets. | × | × | √ |
| Sensit ive f ield | Sensitive field permissions are classified into query, export, and change permissions. After you obtain the sensitive field permissions on sensitive fields in a table, you have full access to all sensitive fields in the table. Before you apply for the sensitive field permissions, you must obtain the database and table permissions to which the sensitive fields belong. Query permission: You can execute SQL statements in the SQLConsole to query data. Change permission: You can submit data change and data import tickets. Export permission: You can submit data export tickets. | × | × | √ |
| Dat abase owner | The owner of a database can manage the permissions on the database. For example, the owner of a database can grant or revoke permissions on the database and tables in the database. The owner of a database can query all data in the database except sensitive or confidential fields. The owner can also submit tickets to perform operations on the data and schemas in the database without the need to apply for permissions. DMS automatically identifies and assigns database owners to owner nodes in approval processes. | √ | √ | √ |

| Permission category | Permissions | Control mode |   |   |
|---|---|---|---|---|
|   |   | Flexible managem ent | Stable change | Security collabora tion |
| T able owner | The owner of a table can manage the permissions on the table. For example, the owner can grant or revoke permissions on the table. The owner of a table can query all data in the table except sensitive or confidential fields. | √ | √ | √ |
| Programmabl e object | Programmable object permissions are classified into query, export, and change permissions. Query permission: You can execute SQL statements in the SQLConsole to query data. Change permission: You can submit data change and data import tickets. Export permission: You can submit data export tickets. | × | × | × |
| Inst ance perf ormance | You can apply for permissions to view the performance of instances that are managed in security collaboration mode. | × | × | √ |
| Inst ance owner | The owner of an instance can manage the permissions on the instance. For example, the owner of an instance can grant or revoke permissions on the instance. The owner of an instance can query all data in the databases of the instance except sensitive or confidential fields. The owner can also submit tickets to perform operations on the data and schemas of the instance without the need to apply for permissions. | √ | √ | √ |

| Permission category | Permissions | Control mode |   |   |
|---|---|---|---|---|
|   |   | Flexible managem ent | Stable change | Security collabora tion |
| Row | Row permissions are classified into query, export, and change permissions. You can apply for permissions on specific values of a managed field in a table. You can also apply for permissions on all values of a managed field in a table. Query permission: You can execute SQL statements in the SQLConsole to query data. Change permission: You can submit data change and data import tickets. Export permission: You can submit data export tickets. | × | × | × |

Apply for permissions
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Permissions and select a permission category. For more
information about permission categories, see Permission categories that are supported by each control mode.

> Not e In the top search box, you can search for databases or tables by name. In the search results, find the required database or table and click Access apply in the Act ions column.

3. Set the required parameters of the permission for which you want to apply.
i. Select the category of the permission for which you want to apply. ii. Select the databases, tables, or columns on which you want to apply for permissions.

> Not e Enter keywords, specify filter conditions, and then click Search to search for databases or tables. The keywords that you enter can contain percent signs (%) as wildcards. In the search results, select the databases or tables on which you want to apply for permissions. Then, click Add.

iii. Select the type of permissions for which you want to apply and specify the duration for which you want to have the permission. Then, enter the reason for your application.
4. Click Submit and wait for approval.

> Not e You can view the status of application ticket in the My Tickets section of the Workbench tab.

Manage permissions

| Management type | Action | Description |
|---|---|---|
| Active management | Release permissions | On the Workbench tab, click Ef f ect ive Permissions in the Permissions section. Select the object on which you want to release permissions and click Release Permission. |

| Data Management | User Guide·Apply for permission |   |
|---|---|---|
| g |   |   |
| Management type | Action | Description |
|   | Renew permissions | On the Workbench tab, click Expiring Permissions in the Permissions section to view and check the permissions that are about to expire. If you want to renew a permission, submit a ticket to apply for the renewal. |
| Passive management | N/A | The owner of a database can view and assess the rationality of permission assignments at any time and manage the permissions that are granted. |

> Not e All the operations that you perform to apply for, release, revoke, and grant permissions are recorded in operation logs. To view the operation logs, choose Syst em Management > Securit y > Operat ion Logs in the top navigation bar.

## 6 SQLConsole

### 6.1 Single database query

The single database query feature allows you to execute various SQL statements in the SQLConsole of the Data Management (DMS) console with ease. You can use this feature to visualize the add, delete, modify, and query operations on the data in a database. This feature applies to scenarios, such as data queries and data development. Prerequisites You are granted the query permission on the database or table that you want to query. Precautions A table may contain sensitive or confidential fields. You do not have permissions to access these fields. Therefore, the values of these fields are displayed as `******` in the query results. For more information, see Manage sensitive data. By default, a maximum of 200 data rows can be returned for each query. If you are an administrator, you can change this value based on your business requirements. To change this value, perform the following steps: 1. Log on to the Data Management (DMS) console. 2. In the top navigation bar, choose Syst em > Securit y > Securit y Rules. A full scan can be performed on a table that does not exceed 10 GB in size. If you are an administrator, you can change this value based on your business requirements. To change this value, perform the following steps: 1. Log on to the DMS console. 2. In the top navigation bar, choose Syst em > Securit y > Securit y Rules. By default, the timeout period to execute a single SQL statement is 60 seconds. If you are an administrator, you can change this value in the Advanced inf ormat ion section of the Edit inst ance dialog box. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > SQLConsole > Single Dat abase Query.

> Not e To go to the SQLConsole tab, you can also double-click the required database in the left-side instance list of the DMS console.

3. Select the database that you want to query from the drop-down list. You can also search for
databases by keyword. After you find and select the required database, click Conf irm.
4. Enter the SQL statement to be executed on the SQLConsole tab and click Execut e.
GUI of the SQLConsole

| No . | Section | Description |
|---|---|---|
| ① | Visual operation section | In this section, you can visually manage your database. T ables You can view all tables, fields, and indexes of the current database. You can also right-click a table in the database to modify the table schema, import data to the table, or export data from the table. Programmable object s You can create, view, execute, and manage programmable objects, such as views, stored procedures, functions, triggers, and events. Not e A maximum of 1,000 entries can be displayed. Key-value pair information Not e The key-value pair information can be displayed only for a NoSQL database. |

| No . | Section | Description |
|---|---|---|
| ② | Extended feature section | In this section, shortcuts to extended features are provided. You can click the icons of the features to use the features. The following table describes the icons. : the T ables icon. You can click the icon to view the details about the table. Then, click the icon to return to the SQLConsole tab. : the Sync Met adat a icon. After you click this icon, DMS collects most recent metadata information about the database, such as tables, fields, indexes, and programmable objects. This way, you can manage permissions on tables, fields, and programmable objects based on the security level. : the Export icon. You can click this icon to export the data of the database, table schemas of the database, or table creation statements. : the Operat ion audit icon. You can click this icon to view the information about all data query and data change records. For example, you can query the information about an operation, the operator, and the time when the operation is performed. For more information, see View operations logs. |
| ③ | Command running section | In this section, you can write and execute SQL statements to manage the current database. You can also format SQL statements, create execution plans, save commonly used SQL statements, and configure display settings. Not e You can click the icon to add multiple query tabs. |
| ④ | Execution result section | In this section, you can view the execution results after SQL statements are executed. You can also view the details about a single row and add, delete, or modify data. Not e You can click the Execut ion Hist ory tab to view the historical execution records. For example, you can view the time at which the execution of an SQL statement started, the affected database, and the details about the SQL statement. You can also export the execution results as required. |

### 6.2 Cmd Tab

Data Management (DMS) provides the Cmd Tab feature as a CLI for you to write and execute SQL statements. The executed SQL statements and execution results are displayed in the upper part of the Cmd Tab tab. This topic describes the GUI of the Cmd Tab tab and how to use the Cmd Tab tab. Prerequisites The database to be queried is a relational database, such as a MySQL, an Oracle, or an SQL Server database. You are granted the query permissions on the database or table that you want to query. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose SQLConsole > Cmd
T ab.
3. Select the database that you want to query from the drop-down list or enter a keyword in the
field to search for the database. After you select the database, click Conf irm.
4. Enter the SQL statement to be executed in the lower part of the Cmd Tab tab and press `Ctrl+Ent`
`er` or click Execut e to execute the SQL statement.

### 6.3 Super SQL mode

Data Management (DMS) provides the super SQL mode feature. After you enable this feature as a DMS administrator or a database administrator (DBA), all SQL statements that you execute on the SQLConsole tab are executed without being affected by security rules. Prerequisites You are a DMS administrator or a DBA. An instance is managed in Security Collaboration mode. Context To enhance the stability and security of databases, DMS administrators and DBAs may configure security rules for the databases. For example, a security rule is configured to prevent unauthorized users from executing DML statements in a production database on the SQLConsole tab. They can execute those statements only by submitting a ticket. However, these security rules may cause inconvenience to privileged users, such as DMS administrators and DBAs. In view of this, DMS provides the super SQL mode feature. If you enable this feature as a DMS administrator or a DBA, all SQL statements that you execute on the SQLConsole tab are executed without being affected by security rules. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose SQLConsole > Single
Dat abase query.

> Not e To go to the SQLConsole tab, you can also double-click the database that you want to query in the left-side navigation pane of the DMS console.

3. Select the database that you want to query from the drop-down list or enter a keyword in the
field to search for the database. After you select the database, click Conf irm.
4. On the SQLConsole tab, click the
icon in the upper-right corner. In the message that appears, click OK. Then, the outside borders of the SQLConsole tab turn orange. This indicates that the super SQL mode feature is enabled. The SQL statements that you enter on the SQLConsole tab are directly executed.

> Not ice After you enable this feature as a DMS administrator or a DBA, all SQL statements that you execute on the SQLConsole tab are executed without being affected by security rules.

To disable the super SQL mode feature, click the icon in the upper-right corner.

### 6.4 Cross-database query

Data Management (DMS) provides the cross-database query feature that allows you to perform crossdatabase queries on online heterogeneous data sources that are deployed in different environments. The cross-database query feature allows you to perform cross-database queries on databases and tables in database instances that are added to DMS. Prerequisites The type of the database instance that you want to query is MySQL, SQL Server, PostgreSQL, PolarDB-X, or Redis. The cross-database query feature is enabled for each database instance.

> Not e If the cross-database query feature is not enabled for a database instance, you can enable the feature in the Edit instance dialog box in the DMS console. Then, enter a database link name in the Advanced information section. The name of each database link must be unique.

You are granted the query permission on each database or table that you want to query. Limits You can perform cross-database queries only on physical databases. This feature is unavailable for logical databases. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > SQLConsole > Cross-dat abase Query.
3. In the left-side pane of the Cross-dat abase Query tab, view the databases on which you have
the query permission or all the databases.
4. On the SQLConsole tab, enter an SQL statement. You can perform cross-database queries on
databases and tables on which you have the query permission in database instances.

|   | Not e You must specify the table that you want to query in the format of <DBLinkName>.<da tabaseName>.<tableName> , for example, dmstest dblink.dmstestdata.customer . _ In the left-side list, you can double-click a table on which you have the query permission or drag the table to the SQLConsole tab. An SQL statement that is used to query data in the table is automatically generated. |
|---|---|
|   | tabaseName>.<tableName> |

5. Click Execut e(F8). You can view the execution results and execution history in the Execution
History section.

> Not e DMS also provides the format, saved cross-database SQL, and display settings features. You can use these features based on your business requirements.

## 7 Data plans

### 7.1 Change data

DMS provides the data change feature that allows you to change data. This topic describes how to use the data change feature to change data. Context DMS allows you to submit data change tickets to initialize data for a newly published project, clear historical data, fix bugs, or run a test. The operations that you can perform to change data include insert, update, delete, or truncate operations. Data change types

| Type | Description |
|---|---|
| Normal data modify | You can use the normal data modify feature to perform the following data changes: Perform normal data changes. Perform lock-free schema changes. You can perform this type of operations to change character sets and collations for tables, adjust time zones, and change column data types. Compared with normal data change operations, lock-free schema changes can be performed to achieve the following benefits: Ensures business continuity regardless of whether tables are locked due to database schema changes. Ensures consistent synchronization between the primary and secondary databases regardless of whether the latency occurs due to native online data definition language (DDL) operations that are performed on the databases. Reclaims tablespaces and reduces fragmentation rates without the need to lock tables. You no longer need to use the OPTIMIZE TABLE statement that results in table locks. Not e You can use this feature only for MySQL databases. Before you use this feature, you must set the OnlineDDL parameter to Open(DMS OnlineDDL first) in the Advanced inf ormat ion section when you add or edit an instance. For more information, see Register database instances with DMS. |
| Lock-free data modify | You can use this feature to change a large amount of data. For example, you can use this feature to delete historical data and update all fields in a table. Multiple SQL statements for data changes are divided and executed at the same time based on the primary key or unique key. This limits the consumption of database performance and space. Not e You can use this feature only for MySQL databases. |

| Type | Description |
|---|---|
| History data clean | You can use this feature to regularly clean historical data. This way, the stability of the production environment is not affected when you obtain historical data. Not e You can use this feature only for MySQL databases. |
| Programmable object | Databases provide programmable objects such as stored functions and stored procedures. This feature allows you to use the programmable objects to standardize management processes and provide audit records. |

Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Plans and select a data change type.

> Not e This topic describes how to submit a ticket that is used to modif y normal dat a.

3. Specify the required parameters for the data change ticket.

| Parameter | Description |
|---|---|
| Reason Cat egory | The reason for the data change. This helps you identify the ticket in the future. |
| Business Background | The purpose or objective of the data import. This reduces communication costs. |
| Change St akeholder | The stakeholders of the data change. All specified stakeholders can view the details about the ticket and participate in the approval process. Unauthorized users, except for administrators and DBAs, cannot view the details about the ticket. |
| Execut ion Met hod | The method that is used to execute the ticket based on your business requirements. |
| Dat abase | The database on which you have the change permission. If you have only query permissions on the database or the change permission on the tables of the database, you cannot submit a data change ticket. |
| Af f ect ed Rows | The estimated number of data rows that are affected by the data change. To obtain the actual number of affected rows, you can write an SQL statement that includes the COUNT function on the SQLConsole tab. |
| SQL St at ement s f or Change | The executable SQL statements that are used to export data. You can upload a file to provide the SQL statements. DMS verifies the syntax of the SQL statements when you submit the ticket. If the syntax is invalid, DMS rejctes the ticket. |
| SQL St at ement s f or Rollback | The executable SQL statements that are used to roll back the data import operation. You can write the SQL statements in the SQL Text field or upload an SQL that includes the required SQL statements. |

| Guide·Data plans | Data Managemen |
|---|---|
| Parameter | Description |

| At t achment s | The images or files that are uploaded to add more information about the data change. |
|---|---|

4. After you configure the settings, click Submit .
5. After your ticket passes the precheck, click Submit f or Approval. In the message that appears,
click OK.
6. After the ticket is approved, click Execut e Change.
7. Set the Execute Immediately parameter and click Conf irm Execut ion.

> Not e By default, the Execute Immediately switch is turned on. You can turn off the Execut e Immediat ely switch and specify a point in time to run the ticket. The system automatically runs the ticket at the specified point in time.

8. Wait until the execution is completed.

### 7.2 Import data

Data Management (DMS) provides the data import feature that allows you to import large amounts of data to a database with ease. This saves manpower and resources. Supported databases Self-managed MySQL databases and ApsaraDB RDS for MySQL databases PolarDB-X databases Supported file formats for data import TXT format. SQL script. By default, you can use only the INSERT and REPLACE statements to import data to database instances that are managed in Security Collaboration mode. If you want to use other SQL statements to import data, modify the security rules for data import as a database administrator (DBA) or DMS administrator. To modify the security rules, click the SQL Correct tab on the Securit y Rules tab and set the Checkpoints parameter to Bat ch Dat a import rules. CSV format. Values in a CSV file must be separated by commas (,). The first row must be field names.

> Not e The file size cannot exceed 5 GB.

Usage notes If you need to change only a small amount of data, we recommend that you submit a Normal Data Modify or Lockless change ticket to ensure stable data change. For more information, see Change data. If you submit a Large Data Import ticket to import a large amount of data to a table, the table will be locked even if you set the OnlineDDL parameter to Open (DMS OnlineDDL first) for the database instance. We recommend that you use SQL statements with better performance to import a large amount of data, such as the INSERT, UPDATE, and DELETE statements. Indexes of primary keys are used in the UPDATE and DELETE statements. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Dat a Plans > Dat a
Import .
3. On the Large Data Import tab, set the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Reason Cat egory | The reason for the data import. This helps you identify the ticket in the future. |
| Business Background | The purpose or objective of the data import. This reduces unnecessary communication. |

| Parameter | Description |
|---|---|
| Change St akeholder | The stakeholders involved in the data import. All the specified stakeholders can view the ticket details and assist in the approval process. Irrelevant users other than DMS administrators and DBAs are not allowed to view the ticket details. |
| Dat abase | The database on which you have the change permissions. You cannot submit a data import ticket if you have only the permissions to query data in the database or change data in tables. |
| File Encoding | The encoding algorithm to be used by the database. |
| SQL St at ement s f or Rollback | The executable SQL statements for rolling back the data import. You can write the SQL statements in the SQL Text field or upload an SQL script that includes the required SQL statements. |
| At t achment s | The images or files that are uploaded to add more information about the data import. |

4. After you set the parameters, click Submit .
5. After the ticket passes the precheck, click Submit f or Approval. In the message that appears,
click OK.
6. After the ticket is approved, click Execut e Change.
7. Set the Execute Immediately parameter and click Conf irm Execut ion.

> Not e By default, the Execute Immediately switch is turned on. You can turn off the Execut e Immediat ely switch and specify a point in time to execute the ticket. DMS automatically executes the ticket at the specified point in time.

Wait until the execution is complete. 8.

### 7.3 Data export

DMS provides the data export feature. You can use this feature to export a database or SQL result sets. Then, you can extract the required data for data analysis. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Plans and select SQL Result Set Export or
Dat abase Export .
3. On the Data Export Ticket Application tab, set the required parameters.
Set the required parameters on the SQL Result Set Export tab

| Parameter | Description |
|---|---|
| Reason Cat egory | The reason for the data export. This helps you find the ticket in a timely manner in the future. |
| Business Background | The purpose or objective of the data export. This parameter reduces communication costs. |
| Dat abase Name | The database on which you have the export permission. |
| Af f ect ed Rows | The estimated number of data rows that are affected by the data export. To obtain the actual number of affected rows, use the COUNT function in SQL statements on the SQL Editor tab. |
| Skip Validat ion | Specifies whether to skip validation. If you select Skip Validat ion, you must enter a reason in the field next to the check box. Warning If you select Skip Validat ion, DMS does not check the number of rows that are affected by the data export. If a large amount of data is exported, potential risks to your business increase. Proceed with caution. |

| Parameter | Description |
|---|---|
| St akeholder | The stakeholders of the data export. All specified stakeholders can view the details about the ticket and are included in the approval process. Unauthorized users, except for administrators and DBAs, cannot view the details about the ticket. |
| Export St at ement | The executable SQL statement that is used to export data. Example: sel ect * from testtable . DMS verifies the syntax of the SQL statement when you submit the ticket. If the syntax is invalid, you cannot submit the ticket. |
| At t achment s | The images or files that are uploaded to add more information about the data export. |

|   | ect * from testtable |
|---|---|

Configure a database export ticket

| Parameter | Description |
|---|---|
| Dat abase Name | The database on which you have the export permission. After you select the database, you must select the table to which you want to export data and configure filter conditions in the Tables & Filters section. |
| Reason Cat egory | The reason for the data export. This helps you find the ticket in a timely manner in the future. |
| Business Background | The purpose or objective of the data export. This parameter reduces communication costs. |

| Parameter | Description |
|---|---|
| St akeholder | The stakeholders of the data export. All specified stakeholders can view the details about the ticket and are included in the approval process. Unauthorized users, except for DMS administrators and DBAs, cannot view the details about the ticket. |
| Export cont ent | The type of data that you want to export. Valid values: Dat a, St ruct ure, and Dat a & St ruct ure. |
| Export ed St ruct ure T ype | The type of schema that you want to export. |
| More Opt ions | The other objects that you want to export. Click Big dat a t ype export opt ions or SQL script ot her opt ions and select the required options. |
| At t achment s | The images or files that are uploaded to add more information about the data export. |

4. After you complete the configurations, click Submit and wait for approval.

> Not e When you export an SQL result set, DMS prechecks the SQL statements. After the SQL statements pass the precheck, click Submit f or Approval. In the message that appears, click OK.

5. After your ticket is approved, go to the Workbench tab and click Submit t ed T icket s in the My
Tickets section.
6. Find the data export ticket that is submitted and click the ticket number.
7. In the Execut e/Aut omat ic Execut ion section, click Download Export ed File.

### 7.4 Generate test data

DMS provides the test data generation feature that allows you to generate data in a quick manner. You can generate test data for functional or performance tests. Prerequisites A relational database is created to store test data that you generate. The relational database can be a self-managed MySQL, ApsaraDB RDS for MySQL, AnalyticDB for MySQL, or PolarDB-X database. A table is created. You can use the schema design feature to create a table. For more information, see Design a schema. Context Functional tests or performance tests often require test data. You can use one of the following methods to generate test data: Write test data. This method has low efficiency and is not applicable to scenarios in which a large amount of test data is required. Use scripts. This method requires high costs and the data that is generated by using this method cannot meet discreteness requirements. Export data from a production environment as test data. This method is not secure and may cause data leak. DMS provides the test data generation feature that allows you to generate test data in a quick, efficient, and secure manner. You can use this feature to control the discreteness of the data that is generated. Precautions You can use this feature to generate test data in only one table at a time. To generate test data in multiple tables, submit a ticket. To prevent database overload due to the instantaneous generation of excessive data, DMS allows you to perform traffic throttling. Check the following examples for your reference. About 1 minute is required to generate one million rows of data in a table that has four fields. About 2 to 3 minutes are required to generate one million rows of data in a table that has 40 fields. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Plans > T est Dat a Generat ion.
3. In the upper-right corner, click T est Dat a Generat ion.
4. In the Test data build ticket application dialog box, set the required parameters.

| Parameter | Description |
|---|---|
| T ask Name | The name of the task. The name can help you identify and manage the task in the future. |
| Dat abase Name | The name of the database that includes the required table. |
| T able Name | The name of the table in which you want to generate test data. You can search for tables by keyword and then select a table from the matched results. After you select a table, the Conf igure t he algorit hm parameter that contains the field information of the table is displayed. Not e You can use this feature to generate test data only in one table at a time. To generate test data in multiple tables, submit a ticket. |
| Conf igure t he algorit hm | The algorithms that are used to generate test data. Find the required field and click the value of the Generation mode parameter next to the field. Then, set the required parameters in Generation mode dialog box based on your business requirements. Not e For example, you can use the random, customize, or enumeration algorithm to generate test data of the STRING type. The customize algorithm can be used to generate multiple industry- standard types of data. |
| Number of rows generat ed | The number of data rows that you want to generate. |
| Conf lict Handling | The method that is used to handle conflicts based on your business requirements. |
| Change St akeholder | The stakeholders of the ticket. All specified stakeholders can view the details about the ticket and are included in the approval process. Unauthorized users, except for DMS administrators and DBAs, cannot view the details about the ticket. |

5. After you set the parameters, click Submit .
6. After your ticket is approved, DMS generates test data.

### 7.5 Clone databases

The database clone feature allows you to replicate data at the database level. This topic describes how to use the database clone feature. Prerequisites A MySQL database is used. A database instance is managed in flexible management mode. You have logged on to the database instance in the Data Management (DMS) console. Scenarios Create a full database backup. Initialize databases that are deployed in different environments, such as development and test environments. Copy data from a database in an online environment to a database in an offline environment for data processing and analysis. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Plans > Dat abase Clone.
3. In the upper-right corner, click Dat abase Clone.
4. In the Apply step, set the required parameters.

| Parameter | Description |
|---|---|
| T ask Name | The name of the task. The name is used to identify and manage the task. |
| Source dat abase (Only support MySQL) | The source database that you want to clone. You can search for databases by keyword and then select a database from the matched results. |

| Parameter | Description |
|---|---|
| T arget dat abase (Only support MySQL) | The destination database to which you want to write the data that is cloned from the source database. You can search for databases by keyword and then select a database from the matched results. Not e The destination database must be different from the source database. |
| Select source t able | The tables that you want to clone from the source database. You can search for tables by keyword and then select a table from the matched results. Not e To clone all tables, set this parameter to All Tables. |
| Duplicat e object s | The method that is used to handle object conflicts based on your business requirements. Skip duplicat e name object : The system skips objects that have a duplicate name. Overwrit e duplicat e name object (warning: t he st ruct ure and dat a of t he t arget object will be replaced): If the two objects have the same name, the schema and data of the object in the destination database are overwritten by the schema and data of the object in the source database. |
| Migrat ion Object s | The objects that you want to clone. In addition to tables, you can simultaneously clone other objects from the source database to the destination database. These objects include views, stored procedures, functions, triggers, and events. |
| T ime opt ions | Valid values: Running immediat ely and Specif ied t ime. If you set the Time options parameter to Specif ied t ime, you must specify a date and time to run the task. Running immediat ely: The task is run immediately after the ticket is approved. Specif ied t ime: DMS automatically runs the task to clone data at a specified point in time. |

5. After you set the parameters, click Submit .
6. After the ticket is approved, the task is automatically run at a specified point in time.

## 8 Data factory

### 8.1 Task orchestration

The task orchestration feature runs based on a distributed scheduling engine that is developed by Alibaba Cloud. This feature allows you to create task flows and schedule these task flows. This feature also meets requirements for data processing based on powerful task flows that include various types of task nodes. For example, you can use this feature to archive data, integrate data, and transform data. Scenarios Periodically archive and analyze business data. Synchronize online data to data warehouses for complex analysis. Periodically clean and transform offline data. Periodically schedule and orchestrate data definition language (DDL) or data manipulation language (DML) operations on databases. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Fact ory > T ask Orchest rat ion.
3. In the left-side navigation pane, click the
icon.
4. Configure a task flow.
i. Click the icon next to T ask Orchest rat ion. ii. In the dialog box that appears, set the Task Flow Name and Description parameters. iii. Click OK.
5. Configure a task in the task flow.

> Not e You can repeat this step to configure more tasks for the task flow.

i. In the left-side navigation pane of the Task Orchestration tab, find the new task flow and double-click the task flow name. ii. On the Task Orchestration tab, drag a task node from the task node list to the canvas. On the canvas, you can create a directed acyclic graph (DAG) based on your business requirements. iii. In the DAG, click the required task node. iv. In the right-side pane, click a tab and set the required parameters.

| Tab | Parameter | Description |
|---|---|---|

| Tab | Parameter | Description |
|---|---|---|
| Met adat a | Dat abase | a. Select the database that you want to manage from the drop-down list. b. Enter the SQL statements to be executed in the field. c. Click Save. d. In the dialog box that appears, select Exist ed t able or New t able to store the query results. Not e If you select Exist ed t able, you must select a name for the required table from the drop-down list. If you select New t able, you need to enter the name of a new table. e. Click OK. |
| Variable Set t ing | Variable Name | bizdate is the only default system variable. This variable indicates the day before the task is executed. The value of the bizdate variable is in the yyyy-MM-dd format. If the default system variable cannot meet your business requirements, you can create a custom variable and enter the variable name in the Variable Name field. Not e To delete a variable that you set, click the icon. |
|   | Variable Rule | To configure a variable rule, set the Time Format parameter. Then, set the required operator, integer value, and time unit, and click Save. To create more variables, you can click Increase Variable. Not e After you configure a variable, you can reference the variable in the ${Variable name} format in SQL statements on the Cont ent tab. You can also click SQLPreview to check whether the variable is configured. |

6. Configure node dependencies in the task flow.
i. In the DAG, move the pointer over a task node and click and hold the circle, as shown in the following figure. Then, draw a line from the circle to the next node. ii. Repeat the previous step to create dependencies between task nodes based on your business requirements. These dependencies indicate the execution order of each task.

> Not e In the preceding figure, the MySQL-1 node is the first task to be execute and the MySQL-2 node is the second. After that, the MySQL-3 and MySQL-4 nodes are executed at the same time.

7. Specify scheduling information for the task flow.
i. Click the blank area on the canvas. In the right-side pane, click the Scheduling tab.

> Not e You can also click the Propert ies tab to configure the basic information of the task flow or click the Operat ions tab to view the historical operations that are performed on the task flow.

ii. Specify the scheduling information.

| Parameter | Description |
|---|---|
| T urn on/of f | Turn on the T urn on/of f switch to enable scheduling. |
| T rigger t ype | Set this parameter based on your business requirements. If you set this parameter to Cyclic scheduling, you must set the Ef f ect ive T ime, Scheduling cycle, and Specif ic T ime parameters. If you set this parameter to Schedule once, you need to set only the Specif ic T ime parameter. |

iii. Click Save.
8. After the preceding parameters are configured, click T ry Run in the upper-left corner of the tab to
check whether the task flow can be run as expected.
9. In the left-side navigation pane, click the
icon, specify filter conditions, and then view the status of the task flow.

> Not e Click the
> icon next to the task flow name to view the status of each task.

You can perform the following operations on the task flow: DAG: View the DAG of the task flow. Execut ive Hist ory: View the details of the historical operations that are performed on the task flow. More > Exit s: Stop a task flow that is in the running state. More > Rerun: Rerun a task flow that is executed or fails to be executed. More > Pause: Pause a task flow. More > Rest ore: Resume a paused task flow. More > Set Successf ully : Set the status of a task flow that fails to be executed to Success.

### 8.2 Data warehouse development

#### 8.2.1 Overview

Data Management (DMS) provides the data warehouse development feature. This feature uses databases as the computing engine and integrates a variety of tools and services in the database ecosystem. This allows you to develop and manage data warehouses with ease. This feature is designed to provide you with a one-stop development platform for data integration, processing, visualization, and value mining. Benefits A variety of data warehouse engine types You can choose a data warehouse engine type based on your enterprise scale, data volume, and requirement for real-time performance. For example, you can choose AnalyticDB for MySQL or ApsaraDB RDS for MySQL as the data warehouse engine type. Two development modes The data warehouse development feature of DMS provides two development modes: task orchestration and professional development. The two modes meet different business requirements. Task orchestration: This development mode allows you to develop a data warehouse by creating task flows and writing SQL scripts for task nodes. You do not need expertise in data warehouse development. You need only to focus on your business logic. Professional development: This development mode meets the requirements of professional warehouse developers. It provides capabilities such as theme management, hierarchical management, production, release, multi-person collaboration, and data quality control. These capabilities empower professional warehouse development solutions for your enterprise.

> Not e Some of the capabilities are planned to be supported soon.

Support for offline and real-time data warehouses The data warehouse development feature supports offline data synchronization and task scheduling. This allows you to develop offline data warehouses with ease in DMS. In addition, DMS is integrated with Data Transmission Service (DTS) and cloud-native data warehouses. This allows you to build a real-time data warehouse system based on the real-time synchronization feature of DTS and cloud-native data warehouse engines. Then, you can develop data and consume data in real time in DMS. Unified management of online and offline data DMS supports unified database management and permission management. You can manage your online transaction processing (OLTP) databases and online analytical processing (OLAP) databases in a centralized manner in DMS. This avoids security issues that are caused by the isolation between offline and online systems.

#### 8.2.2 Create a data warehouse project

Before you can use the data warehouse development feature of Data Management (DMS), you must create a data warehouse project and select a data source for data warehouse development. This topic describes how to create a data warehouse project. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Dat a Fact ory > Dat a
Warehouse Development .
3. On the left-side navigation submenu, click the
icon.
4. Click the
icon to the right of Dat a warehouse.
5. In the New Warehouse Project dialog box, set the parameters as required.

| Section | Parameter | Description |
|---|---|---|
| Basic Inf ormat ion | Project Name | The name of the project. Specify a descriptive name for easy identification. |
|   | Mode | The mode of the project. Set this parameter to Simple Mode(Single environment ). This way, you can use the same database in a development environment and a production environment. |
|   | Descript ion | The description of the project. |
| Select Dat a Development Services | N/A | DMS automatically completes the configuration in this section. |

| Section | Parameter | Description |
|---|---|---|
| Dat a warehouse engine select ion | Select a type of data warehouse engine. | After you select a data warehouse engine, such as Analyt icDB f or MySQL 3.0, select a database from the Select an exist ing dat abase drop-down list. Not e Only the databases of the instances that are managed in Security Collaboration mode are available in the drop-down list. You must be the owner of the selected database. |

6. Click OK.
What's next

#### 8.2.3 Create or import an internal table

After you create a data warehouse project in Data Management (DMS), you must create or import an internal table for the project. An internal table refers to a table that exists in the data warehouse engine. This topic describes how to create or import an internal table. Prerequisites You have the change permissions on the database for which you want to create or import an internal table. For information about how to apply for permissions, see Apply for permissions. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose Dat a Fact ory > Dat a Warehouse Development .
3. On the left-side navigation submenu, click the
icon.
4. In the left-side navigation pane, expand a data warehouse project and then expand Warehouse
table. Move the pointer over Int ernal t able and then the More icon that appears. Then, select an option from the menu to perform one of the following operations.

> Not e You cannot configure external tables in DMS.

Create an internal table: a. Select Add int ernal t able. b. On the tab that appears, enter an SQL statement to create a table. c. Click Execut e. Import an internal table:

> Not e The data warehouse development feature does not support real-time synchronization of tables that are created by using other means such as a command-line tool. You can import such tables to data warehouse projects in DMS.

a. Select Import int ernal t ables. b. In the Import internal tables dialog box, select the table that you want to import from the Choose t able drop-down list and enter a description in the Remarks field. c. Click OK. Create a folder:

> Not e If you have a large number of tables, you can use folders to organize and classify the tables.

a. Select New f older. b. In the New folder dialog box, enter a folder name. c. Click OK. What's next

#### 8.2.4 Manage task flows

Data Management (DMS) supports task flows and timed scheduling. You can configure a variety of task nodes in task flows. This can meet your requirements for data archiving, integration, and processing. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose Dat a Fact ory > Dat a Warehouse Development .
3. On the left-side navigation submenu, click the
icon.
4. In the left-side navigation pane, expand a data warehouse project. Move the pointer over T ask
Flow and then the icon that appears.
5. In the New Task Flow dialog box, enter a name and the description for the task flow.
6. Click OK.
7. On the tab that appears, configure task nodes for the task flow.

> Not e The configurations of a task flow in professional development mode are basically the same as the configurations of a task flow in task orchestration mode. For more information, see Step 5 in the Task orchestration topic.

#### 8.2.5 Use the data service feature

In Data Management (DMS), the data warehouse development feature is integrated with the data service feature. The data service feature allows you to export the data that is managed by DMS. This feature is applicable to scenarios in which you need to export data at the column or row level, visualize data, or perform complex analysis. Limits When you use the data service feature to create an API for a data warehouse, the data source of the API must be a table in the data warehouse project. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Fact ory > Dat a Warehouse Development .

> Not e You can also choose More > Dat a Fact ory > Dat a Service.

3. On the left-side navigation submenu, click the
icon.
4. In the left-side navigation pane, expand the required data warehouse project and double-click
Dat a Service. Configure an API For information about how to configure an API, see Develop an API, Unpublish or test an API, Test an API, and Call an API.

### 8.3 Data service

#### 8.3.1 Overview

Data Management (DMS) provides the data service feature, which allows you to export the data that is managed by DMS. This feature is applicable to scenarios where you need to export data at the column or row level, display data in a visualized manner, or perform complex analysis. Features You can use the data service feature to create APIs that can be called to access the data that is managed by DMS. When you create the APIs, you can apply the security control features that are used for SQL execution in the SQLConsole, such as permission control and data de-identification. The data service feature works based on a serverless architecture. This feature frees you from the concern about the infrastructure of the runtime environment, such as servers and networks. You need to focus only on how to create APIs and design data query logic. This avoids operations and maintenance (O&M) overheads that are generated by using traditional architectures. The data service feature is fully integrated with API Gateway. You can use this feature to publish APIs to API Gateway. This way, you can use all the features that are provided by API Gateway, such as API permission control, IP address-based access control, throttling, metering and billing, and SDKs. Scenarios

| Scenario | Description |
|---|---|
| Minimize data exposure | Assume that you need to export the data that is managed by DMS to an external environment. In this case, APIs can be called to export the data of specific rows or columns to the external environment. To export the data of specific rows, specify a filter condition in the SQL statement. To export the data of specific columns, specify the columns in the SQL statement. Compared with data export of a whole table, this minimizes data exposure and ensures data security. |
| Connect visualization tools to databases | Most visualization tools can connect to databases by calling APIs. You can connect a visualization tool to your database by calling an API, instead of by using a username and a password. This method is easy to implement and avoids account exposure. |

| Scenario | Description |
|---|---|
| Sell APIs in the Alibaba Cloud Marketplace | If you want to provide paid or free data for other users, publish an API to the Alibaba Cloud Marketplace. |
| Provide processed data for applications | After data is processed and summarized by using the data warehouse development feature of DMS, APIs can be created and provided for applications to read the processed data from DMS to meet business needs. To modify the logic of data reading, you need only to modify the query logic of the required API without the need to republish the application. |

#### 8.3.2 Develop an API

The data service feature of Data Management (DMS) allows you to develop APIs with ease. This topic describes how to create and manage APIs. Prerequisites API Gateway is activated. For more information, see the documentation of API Gateway. Context The data service feature allows you to export the data that is managed by DMS. This feature is applicable to various scenarios. These scenarios include data export at the column or row level, data visualization, or complex data analysis. For more information, see Overview. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Dat a Fact ory > Dat a Service.
3. In the left-side navigation pane, click the API Development tab.
4. On the APIManagement tab, click New API in the upper-right corner.
5. On the tab that appears, set the required parameters.
i. Set the required parameters on the AttributeConfiguration tab.

|   | Parameter |   | Description |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | APIName |   | The name of the API. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores ( ). The name must start _ with a letter. |   |   |   |   |   |   |
|   | Descript ion |   | Optional. The description of the API. Enter an informative description, for example, a description of the data that you want the API to return or the scenarios in which the API can be called. |   |   |   |   |   |   |
|   |   |   | The path of the API. The path must start with a forward slash (/) and can contain letters, digits, underscores (-), and hyphens (-). The specified path forms a part of the URL that is used to call the API. A URL that is used to call an API must be in the https://{Domain name}{ Path} format. For example, if the domain name is xxxx-cn-hangzhou .alicloudapi.com and the path is /item/monthly data , the URL _ that is used to call the API is https://xxxx-cn-hangzhou.alicloudap i.com/item/monthly data . _ |   |   |   |   |   |   |
|   |   |   |   |   |   | https://{Domain name}{ |   |   |   |
|   | Pat h |   | Path} |   |   |   |   |   |   |
|   |   |   |   |   |   |   | xxxx-cn-hangzhou |   |   |
|   |   |   |   |   | /item/monthly data _ |   |   |   |   |
|   |   |   |   |   |   |   |   | , the URL |   |
|   |   |   |   | https://xxxx-cn-hangzhou.alicloudap |   |   |   |   |   |
|   |   |   | i.com/item/monthly data _ |   |   |   |   |   |   |
|   | Ret urnFormat |   | The format in which you want the API to return data. Valid value: JSON. |   |   |   |   |   |   |
|   | Request Mode |   | The request method. Valid values: POST and GET . |   |   |   |   |   |   |
|   | T imeOut (MS) |   | The maximum period of time that the system can wait until an API request expires. Unit: milliseconds. If the execution time of an API exceeds the specified timeout period, the system returns a timeout error. Maximum value: 30000. |   |   |   |   |   |   |
|   | Ret urns t he maximum number of records |   | The maximum number of entries that can be returned for an API request. This parameter limits the number of entries that can be returned for each API query. Not e If the database instance is managed in security collaboration mode, the value of this parameter must be less than the maximum number of entries that is specified in the security rules. |   |   |   |   |   |   |

ii. Click the Execut eConf igurat ion tab and set the required parameters.

| Parameter | Description |
|---|---|
| Inst ance query t ype | Single Inst anceQuery: You can call the API to read data from only one database instance. Cross-inst anceQuery: You can write dynamic SQL statements for the API to query data across multiple database instances. Not e If you set this parameter to Cross-inst anceQuery, you need only to enter dynamic SQL statements in the QuerySQL field. |

| Parameter | Description |
|---|---|
| Dat a source | The database that is queried by the API. You can search for databases on which you have query permissions by keyword and then select a database. |
| Conf igurat ionMode | T able boot mode: You can configure data query by selecting a table and fields. Script mode: You must configure a data query by specifying variables and writing SQL statements. Not e After you set this parameter to Script mode, you need only to enter SQL statements in the QuerySQL field. |
| Select T able | The table to be queried. You can search for tables by keyword. |
| FieldList | The fields in the selected table. You can specify the required fields as request parameters or response parameters. |
| Script mode | The mode in which an SQL script is written to define the data query logic. Not e You can set the Conf igurat ionMode parameter to T able boot mode or Script mode. |
| QuerySQL | The SQL statement that is used to query the data in the table. After you enter an SQL statement, click ParsingScript to verify the syntax and to parse the request parameters and response parameters. Not e Custom variables are supported. Custom variables can be mapped as request parameters in API requests. The variables of an SQL statement must be specified in the ${Variable name} format. For example, the select item id, item _ _ name from ex item where category=${category} SQL _ statement include a variable named category . If you set the Inst ance query t ype parameter to Cross- inst anceQuery, you must use the syntax of cross-database query SQL statements. For more information, see Cross- database query. |

|   | ${Variable |   |   |
|---|---|---|---|
| select item id, item _ _ |   |   |   |

|   |   |   | name} |
|---|---|---|---|

iii. Click the Request Paramet ers tab and set the required parameters.

| Parameter | Description |
|---|---|
| Paramet ersName | The name of the request parameter. The name can contain letters, digits, hyphens (-), and underscores ( ). _ The name must start with a letter or an underscore ( ). _ The name must be 1 to 50 characters in length. |
| FieldName | The name of the field that is specified by the request parameter. The field name is specified on the Execut eConf igurat ion tab and cannot be changed. |
| Cannot be empt y | Specifies whether the request parameter is required. |
| Descript ion | The description of the request parameter. |
| Dat a t ype | The data type of the request parameter. The data type is used to check whether the value of the request parameter in an API request is valid. Valid values: String, Integer, and Floating point. Default value: String. Not e This parameter affects the SQL statement that is executed when the API is called. |
| Example value | The sample value of the request parameter. You can use the sample values that are provided in SDKs and documentation as references when you call API operations. |
| Def ault value | The default value of the request parameter. If the request parameter is optional and not specified in the API request, the default value is used. |

iv. Click the Ret urn paramet er tab and set the required parameters.

| Parameter | Description |
|---|---|
| Paramet ersName | The name of the response parameter. The name can contain letters, digits, hyphens (-), and underscores ( ). _ The name must start with a letter or an underscore ( ). _ The name must be 1 to 50 characters in length. |
| FieldName | The name of the field that is returned. The name cannot be changed. |
| Descript ion | The description of the response parameter. |
| Dat a t ype | The data type of the response parameter. Valid values: String, Integer, and Floating point. Default value: String. This parameter is used by DMS to convert the type of the data in API responses. This parameter affects the JSON data that is returned. |
| Example value | The sample value of the response parameter. You can use the sample values that are provided in SDKs and documentation as references to help you understand API responses. |

6. Click Save.
7. In the left-side navigation pane, click the API Development tab.
8. Perform the following operations to manage the API based on your business requirements:
Publish the API On the APIManagement tab, find the required API and click Publish in the Operat ion column of the API. In the message that appears, click OK. Modify the API On the APIManagement tab, find the required API and click Modif y in the Operat ion column of the API. Modify the configurations of the API based on the descriptions in Step 5 and click Save. Delete the API: On the APIManagement tab, find the required API and click Delet e in the Operat ion column of the API. In the message that appears, click OK.

#### 8.3.3 Unpublish or test an API

This topic describes how to unpublish or test an API that has been published. Prerequisites An API is created. For more information, see Develop an API. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, click DT S. In the left-side navigation pane, choose Data Application >
Dat a Service.
3. Click the API Publish tab on the left side.
The APIPublishList tab displays all the published APIs.
4. Find the API that you want to manage and perform the following operations based on your
business requirements: Unpublish the API: Click Of f line in the Operat ion column. In the message that appears, click OK. Test the API: Click T est in the Operat ion column. For more information, see Test an API.

#### 8.3.4 Test an API

After you create an API, you can test the API to verify whether the API meets your business requirements. Prerequisites Procedure
1. Log on to the DMS console.
2. In the top navigation bar, click DT S. In the left-side navigation pane, choose Data Application >
Dat a Service.
3. Click the API T est tab on the left side.
4. On the APITest tab, test an API.
i. Select the API that you want to test from the drop-down list. ii. Enter values in the Parameter value column. iii. Click T est . After the test is complete, the execution information and return results appear on the right side. You can evaluate whether the API meets your business requirements based on the information.

> Not e You can click the JSON tab in the Ret urnResult s section so that the return results are displayed in the JSON format.

#### 8.3.5 Call an API

After you create, publish, and test an API, you can call the API in an application by using an SDK. Prerequisites An API is created and published. For more information, see Develop an API. API Gateway is activated. For more information, see the documentation of API Gateway. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, click DT S. In the left-side navigation pane, choose Data Application >
Dat a Service.
3. Click the API Call tab on the left side.
4. View the API call address and the authentication information.
Simple ident it y aut hent icat ion: requires only an AppCode. This authentication method is suitable for calling APIs by using URLs. This authentication method has a low security level and is generally used in scenarios in which data visualization is involved, such as calling APIs in DataV. Encrypt ed signat ure ident it y aut hent icat ion: requires an AppKey and an AppSecret, which are used to dynamically generate an encrypted signature for calling an API. This authentication method has a high security level.
5. Call the API in an application by using an SDK.

> Not e For more information about how to call an API in an application by using an SDK, see the documentation of API Gateway.

## 9 Schemas

### 9.1 Schema design

Data Management (DMS) provides the schema design feature. This feature allows you to change schemas with ease. This topic describes how to change schemas. Prerequisites The destination database is a MySQL, a PolarDB-X, or an ApsaraDB for OceanBase database. Context When you create projects, process new business requirements, or optimize business operations, you may need to change schemas. These schema operations include creating and editing tables. For example, you may need to add or delete fields or indexes, adjust field attributes, or adjust the index composition. In these scenarios, you can use the schema design feature of DMS. This feature allows multiple users to simultaneously change a schema in the DMS console at the same time. This feature allows you to send verified scripts to other environments. This ensures consistency between schemas in different environments. Precautions When you submit a schema design ticket to delete a table, make sure that the table is created by using a schema design ticket. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Schemas > Schema Design.
3. In the upper-right corner of the Schema Design tab, click Schema Design.
4. On the Schema Design tab, specify the required parameters for a schema design ticket.

| Parameter | Description |
|---|---|
| Project Name | The name of the project. Specify a name that can help you identify the project. |
| Project descript ion | The background information about the project, such as the purpose or objective of the project. The description is used to reduce communication costs. |
| Change Base Dat abase | The database whose schema you want to change. You can search for databases by keyword. Prefix match is applied. Only databases on which you have permissions in test or development environments are displayed. Not e You must have at least the query, export, or change permissions on the database that you select. |
| Securit y Rules | No configurations are required. The default setting is specified. |
| Change St akeholder | The stakeholders of the changes. The specified stakeholders can view the ticket details and are included in the approval process. Unauthorized users, except for administrators and database administrators (DBAs), cannot view the ticket details. |

5. Click Creat e T icket .
6. Change a schema based on your business requirements.
Create a table: a. Click Creat e Physical T able.

> Not e If the destination database is a logical database, click Creat e Logical T able.

b. On the Create Physical Table tab, set the required parameters. The parameters include the table name, character set, fields, and indexes. c. Click Save.

> Not e After you click Save, DMS verifies the specified information based on design specifications. If the information does not comply with the design specifications, a message appears.

d. After the information passes the precheck, click Conf irm Changes and Submit t o Save. Change the schema of a table: a. In the left-side table list, right-click the name of the required table. b. On the menu that appears, select Design T able. c. Change the schema as required and click Save.

> Not e After you click Save, DMS verifies the specified information based on design specifications. If the information does not comply with the design specifications, a message appears.

d. After the specified information passes the verification, click Conf irm Changes and Submit t o Save.
7. After the schema is changed, click Perf orm Changes t o Base Dat abase.
8. In the Perform Changes to Base Database dialog box, set the Execution Strategy parameter to
Execut e Now or Schedule.
9. Click Submit f or Execut ion and wait until the ticket is approved.
10. After the ticket is approved, click Go t o Next Node.

> Not e
> After the ticket is approved, DMS applies the changes at the specified point in time. If you do not specify the execution time, the changes are automatically applied after the ticket is approved at the last approval node. You can view the execution status and operation logs. After all changes are applied, you can repeat the preceding procedure to change the schema again. If no additional changes are required for the schema, click Go to Next Node.
> After the ticket is submitted to the next node, whether you can go back to the previous node is subject to the predefined design specifications.

11. In the Go to Next Node message, click Go t o Next Node.
12. On the Project Homepage tab, click Perf orm Changes t o T arget Dat abase.
13. In the Perform Changes to Target Database dialog box, set the Target Database and Execution
Strategy parameters and click Submit f or Execut ion.

> Not e The required database must reside in a production environment.

14. Wait until the ticket is approved and the changes are applied.
15. Click Go t o Next Node.
The schema design process ends and the ticket is closed.

### 9.2 Schema synchronization

Data Management (DMS) provides the schema synchronization feature. You can use this feature to compare the schemas of two databases, generate a script to synchronize schemas, and then run the script on the destination database. This topic describes the schema synchronization feature and how to synchronize schemas. Prerequisites The source databases and destination databases are ApsaraDB for OceanBase or MySQL databases. Precautions You cannot synchronize schemas to a destination database that resides in a production environment. The empty database initialization feature allows you to synchronize some or all tables from a physical or logical database. Scenarios You can use the schema synchronization feature to synchronize schemas and ensure schema consistency in the following scenarios: Synchronize data between a database in a production environment and a database in a test environment. Synchronize data between different databases that are deployed in a test environment. Synchronize data between different databases that are deployed in a production environment. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Schemas > Schema Synchronizat ion.
3. Specify the required parameters for a schema synchronization ticket.

| Parameter | Description |
|---|---|
| Source Dat abase | The name of the source database from which you want to synchronize schemas. You must have the read permissions on the source database. |
| T arget Dat abase | The name of the destination database to which you want to synchronize schemas. You must have the change permissions on the destination database. |
| Synchronized T able | The tables that you want to synchronize. Valid values: Part ial T ables: Synchronize one or more tables in the source database. You can click Bat ch Add to add multiple tables. Not e If you do not set this parameter, the names of the destination tables are the same as the names of the source tables. All T ables: Synchronize all tables in the source database. |
| Whet her t o Ignore Error | Not Ignore: If an error occurs when SQL scripts are executed in serial mode, the system immediately stops executing the current and remaining SQL scripts. Ignore: If an error occurs when SQL scripts are executed, DMS stops executing the current SQL script and continues to execute the next statement until all remaining SQL scripts are executed. |

4. Click Submit . DMS starts to analyze the schemas.
5. Check the comparison results.

> Not e If the schemas are changed when the system analyzes the schemas, click Re- analyze in the Schema Analysis step.

6. Verify the script that is used to synchronize schemas and click Submit and Synchronize t o
T arget Dat abase.

> Not e If the schemas of the source database and destination database are the same, you do not need to submit the script, and the schema synchronization ticket is closed.

### 9.3 Synchronize shadow tables

Data Management (DMS) provides the shadow table synchronization feature to automatically create a shadow table based on the schema of a source table. DMS generates the name of the shadow table by attaching a prefix or suffix to the name of the source table. You can use this feature for end-to-end stress testing. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Schemas > Shadow
T able Synchronize.
3. On the T able/Dat abase Synchronizat ion Applicat ion page, set the parameters that are
described in the following table.

| Parameter | Description |
|---|---|
| Source Dat abase | The database whose data is to be synchronized. |
| Pref ix / Suf f ix | The prefix or suffix that is used to create a shadow table name. The name can be in the Pref ix + Source table name format or Source table name + Suf f ix format. You can use a custom prefix or suffix as needed. By default, the Prefix + Source table name format is used. Default shadow table name: test Source table name . __ _ |
| Synchronized T able | The tables whose schemas you want to synchronize. Valid values: Part ial T ables All T ables |

| Parameter | Description |
|---|---|
| Synchronizat io n Policy | The policy that is used for shadow table synchronization. Valid values: Synchronize Now: DMS immediately synchronizes the tables after you submit the ticket. In this case, the tables are synchronized only once. Scheduled Synchronizat ion: DMS synchronizes the tables at the specified time on a regular basis. You can use a crontab expression to schedule synchronization based on your requirements. The minimum interval for synchronization is 1 hour. By default, the shadow tables start to be synchronized at 02:00 every day. For more information, see the Crontab expressions section of this topic. |
| Whet her t o Ignore Error | Specifies whether to skip errors that occur when SQL statements are being executed. Valid values: Not Ignore: If an error occurs when SQL statements are being executed, DMS stops executing the current and subsequent SQL statements. Ignore: If an error occurs when SQL statements are being executed, DMS skips the current SQL statement and continues to execute subsequent SQL statements until all remaining statements are executed. |
| Business Background(Re marks) | The business background of the project, such as the purposes and objectives of the project. |

4. Click Submit . DMS starts to analyze the schemas.
5. Check the analysis results.

> Not e If the schemas are changed during schema analysis, click Re-analyze in the Schema Analysis step.

6. Verify the script that is used to synchronize schemas and click Submit and Synchronize t o
T arget Dat abase.

> Not e If the schemas of the source database and destination database are the same, you do not need to submit the script. The schema synchronization ticket is closed.

Crontab expressions If you need to schedule the synchronization task to be run in a more precise manner, you can use a crontab expression. The interval for running the task can be specified by using a combination of minutes, hours, days, weeks, or months. A crontab expression consists of five fields of the NUMERIC type. Valid values of each field: Minut es: `0 to 59` . Hours: `0 to 23` . A value of 0 indicates the midnight. Days: `1 to 31` . A value of this field indicates a specific day of a month. Mont hs: `1 to 12` . A value of 1 indicates January, and a value of 2 indicates February. Similarly, the specific month that is indicated by a specific value can be obtained. Weeks: `1 to 7` . A value of 1 indicates Sunday, and a value of 2 indicates Monday. In other words, the seven week days from Sunday to Saturday are indicated by values 1 to 7. Usage notes Specify the time for running a stress testing task by the day or week. You cannot specify the day and week at the same time. After you specify one of the preceding two values, you must set the other value to ? . A value of ? indicates an unspecified value. For example, if you schedule the task to be run on the first and second days of each month, the Weeks field must be set to ? . Limit the characters in a crontab expression to English special characters. The special characters can be wildcards such as asterisks (*) and question marks (?). Separate multiple values with commas (,). Use a hyphen (-) to indicate a value range. For example, if you set the Days field to `1-5` , the task is scheduled to be run on the first to fifth days of a month. Use a forward slash (/) to indicate an interval for running the task. For example, if you set the Days field to `*/2` , the task is scheduled to be run every two days. Crontab expression examples To schedule the task to be run at 23:00 every Saturday and Sunday, use the following crontab expression: 0 23 ? * 7,1. To schedule the task to be run at 09:30 on the fifth, fifteenth, and twenty-fifth days of each month, use the following crontab expression: 30 9 5,15,25 * ?. To schedule the task to be run at 00:00 every two days, use the following crontab expression: 0 0 */2 * ?.

### 9.4 Initialize empty databases

DMS provides the empty database initialization feature. This feature allows you to compare the schemas of two databases, generate a script that is used to synchronize data from the source database to the destination database, and run the script on the destination database. To use this feature, the destination databases must be empty. This topic describes how to initialize empty databases. Prerequisites The source databases and destination databases are MySQL or ApsaraDB for OceanBase databases. The destination databases are empty databases that do not contain tables. Features The empty database initialization feature allows you to synchronize some or all tables from a physical or logical database. Scenario Synchronize data between databases that are deployed in different regions or units. For example, this feature is applicable to the following scenarios: Synchronize data between a database that is deployed in a production environment and a database that is deployed in a test environment. Synchronize data between different databases that are deployed in the test environment. Synchronize data between different databases that are deployed in the production environment. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Schemas > Empt y Dat abase Init ializat ion.
3. On the Table/Database Synchronization Application tab, set the required parameters to create an
empty database initialization ticket.

| Parameter | Description |
|---|---|
| Source Dat abase | The name of the source database from which data is synchronized. You must have the read permissions on the source database. |
| T arget Dat abase | The name of the destination database to which data is synchronized. You must have the write permissions on the destination database. Not e The type of the destination database must be the same as the type of the source database. |
| Init ialized T able | The tables that you want to synchronize. Valid values: Part ial T ables: Synchronize one or more tables in the source database. To add a table, click the + icon and specify a name for the source table. Not e You can also click Bat ch Add. In the Batch Add dialog box, select the required tables and click Bat ch Add. If you do not set this parameter, the names of the destination tables are the same as the names of the source tables. All T ables: Synchronize all tables in the source database. |
| Whet her t o Ignore Error | Not Ignore: If an error occurs when an SQL script is being executed in serial mode, the system immediately stops executing the current and remaining SQL scripts. Ignore: If an error occurs when an SQL script is being executed, DMS stops executing the current SQL script and continue to execute the next statement until all remaining SQL scripts are executed. |

4. Click Submit . DMS starts to analyze the schemas.
5. Check the analysis results.

> Not e If the schemas are changed during schema analysis, click Re-analyze in the Schema Analysis step.

6. Verify the script that is used to synchronize schemas and click Submit and Synchronize t o
T arget Dat abase.

> Not e If the schemas of the source database and destination database are the same, you do not need to submit the script. The schema synchronization ticket is closed.

### 9.5 Repair table consistency

DMS provides the table consistency repairing feature. This feature is used to compare schemas between tables in databases that are deployed in different environments, provides an efficient way to identify schema differences, and execute SQL statements that are specific to the required environment. This ensures schema consistency between different environments. Prerequisites The source databases and destination databases are MySQL or ApsaraDB for OceanBase databases. Scenarios Ensure the schema consistency between physical tables that are deployed in the test environment and the production environment. Ensure the schema consistency between physical tables and logical tables in a physical database or a logical database. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Schemas > T able Consist ency Repairing.
3. On the Table/Database Synchronization Application tab, set the required parameters to create a
Repair Table Consistency ticket.

| Parameter | Description |
|---|---|
| Base Dat abase(Physical Dat abase) | The source database based on which schema consistency is to be repaired. You must have the query permissions on the source database. |
| T arget Dat abase | The destination database whose data is to be modified. You must have the change permissions on the destination database. |
| Repaired T able | The tables between which schema consistency is to be repaired. To add tables, click the + icon and specify the required table names. Not e If you do not specify the destination table name, the system names the destination table after the name of the specified source table. |

| Parameter | Description |
|---|---|
| Whet her t o Ignore Error | Not Ignore: If an error occurs when SQL statements are being executed in serial mode, the system immediately stops executing the current and remaining SQL statements. Ignore: If an error occurs when DMS is executing an SQL statement, DMS stops executing the current SQL statement and continues to execute the remaining SQL statement. |
| Business Background | The business background of the ticket. This parameter reduces communication costs. |

4. Click Submit . DMS starts to analyze the schemas.
5. Check the analysis results.

> Not e If the schemas are changed during schema analysis, click Re-analyze in the Schema Analysis step.

6. Verify the script that is used to synchronize schemas and click Submit and Synchronize t o
T arget Dat abase.

> Not e If the schemas of the source database and destination database are the same, you do not need to submit the script. The schema synchronization ticket is closed.

## 10 SQL review

DMS provides the SQL review feature to help you prevent SQL statements that do not use indexes or do not conform to database development standards. This reduces the risk of SQL injection attacks. Prerequisites The environment type of the database instance in which you want to use the SQL review feature is T est in the DMS console. This is because SQL review is performed before DMS publishes SQL statements to an online environment. Context When you develop a project, you need to execute SQL statements on databases to add, delete, modify, and query data so that you can implement business logic and display data. Before the project is published, you must review all SQL statements that are used. This prevents SQL statements that do not conform to database development standards from being published to an online environment and accordingly impeding the business. If DBAs manually review all SQL statements one by one, excessive human resources are consumed and the R&D efficiency is low. The SQL review feature helps you review SQL statements and also provides optimization suggestions. Usage notes Only XML or TXT files can be uploaded. Tables that are involved in SQL statements must exist in the database that you select. Otherwise, DMS cannot review these SQL statements. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose Opt imizat ion > SQL Review.
3. On the tab that appears, click New in the upper-right corner.
4. Configure information about an SQL review ticket.

| Parameter | Description |
|---|---|
| Project name | Enter a project name based on your business requirements so that the ticket can be distinguished from others in subsequent processing. |
| Dat a source | Select the database in the test environment that is used in your project. You must have the change permission on the database. |
| Business Descript ion | Enter detailed information about the business scope of the project as required to help relevant users know about the project. |
| Relevant personnel | Enter an at sign (@) and select a user. Not e You can repeat this operation to select multiple users. |

| Parameter | Description |
|---|---|
| Upload a f ile | Click Add, select files, and then click Upload. Not e The iBATIS and MyBatis files are in the XML format. SQL statements are saved as TXT files. Multiple SQL statements are separated by semicolons (;). To remove an added file, you can select the check box before the file name and click Delet e. |

5. Click Submit applicat ion.
6. View SQL review results.

> Not e
> If SQL statements in a file conform to database development standards and use indexes, DMS determines that these SQL statements pass the SQL review and offers no suggestion about indexes.
> If SQL statements in a file conform to database development standards but do not use indexes, DMS determines that these SQL statements pass the SQL review and offers suggestions about indexes.
> If SQL statements in a file do not conform to database development standards, DMS determines that these SQL statements fail the SQL review.

7. Find a failed SQL review result and click View reason to check the reason. You can also click
Det ails, Adjust SQL, or More in the Operat ion column to perform other operations.

> Not e After you optimize SQL statements in a file and click Conf irm, DMS reviews the SQL statements again. For dynamic SQL statements in XML files, you must optimize each SQL statement combination.

8. When all SQL statements pass the SQL review, click Inspect ion result s.
9. In the dialog box that appears, click Submit f or approval and wait for approval.

> Not e The approval process of the ticket is based on the security rules that are configured for the current database instance.

## 11 System management

### 11.1 Manage instances

Data Management (DMS) allows you to manage database instances. For example, you can export the information about instance configurations. Prerequisites You are a database administrator (DBA) or a DMS administrator. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > Inst ance.
3. On the Inst ance List tab, select one or more database instances that you want to manage. Then,
you can perform the following operations based on your business requirements:

> Not e You can click Expand f ilt er to show more filter conditions.

Click New and register a database instance with DMS. For more information, see Register database instances with DMS. Edit multiple instances at a time Click Bat ch edit . In the dialog box that appears, modify the instance information and click OK.

> Not e The database instances that you select must be of the same database type, such as MySQL.

Synchronize the data dictionary Click Sync dict ionary. In the message that appears, click OK.

> Not e
> If you change schemas for a database instance by using DMS, DMS automatically synchronizes the data dictionary of the instance.
> If you change schemas for a database instance by using a service other than DMS, you must manually synchronize the data dictionary of the instance.

Disable or enable one or more instances Click Forbidden inst ance or Enable inst ance. In the message that appears, click OK.

> Not e
> After you disable a database instance, the instance is removed from the left-side instance list. DMS users can no longer find databases or tables in this instance in the DMS console.
> After you enable a database instance, the instance appears in the left-side instance list. Databases in this instance become available. Relevant permissions that have been granted to DMS users on this instance also become valid.

Remove one or more instances Click Delet e Inst ance. In the message that appears, click OK. After you remove a database instance, the instance is removed from the left-side instance list. DMS users can no longer use databases in this instance in the DMS console. Relevant permissions that have been granted to DMS users on this instance also become invalid and are revoked.

> Not e On the Inst ance List tab, you can find database instances in the Delete state and enable these instances to recover them.

Export configuration information Click Export conf ig. The browser automatically downloads a CSV file named instances. You can use Excel or a text editor to view this file. Configure a whitelist Click Conf igure Whit elist . In the message that appears, click OK. The IP addresses of DMS servers are automatically added to the whitelists of the specified database instances.

> Not e The destination database instances must be ApsaraDB instances.

Other operations You can find a database instance and click Details in the Actions column to view the details about databases and tables in this instance. You can also move the pointer over More and perform other operations. For example, you can log on to the instance or edit the instance.

### 11.2 Database management

On the Database List tab, you can manage databases. For example, you can specify the database owner, transfer the ownership, revoke the owner permission, grant and revoke user permissions, and export the information about database configurations or permissions. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, click Dat a Asset s. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, choose Syst em > Inst ance.
4. Click the Dat abase List tab.
5. Set filter conditions and select one or more databases that you want to manage. Then, you can
perform the following operations based on your business requirements:

> Not e You can click Expand f ilt er to show more filter conditions.

Specify an owner Specify an owner for the selected databases. You can specify multiple owners for multiple databases at a time. Transfer the ownership Transfer the ownership of the selected databases to a user. If you transfer the ownership of multiple databases at a time, you can select only a user that assumes the ownership of all of the databases as the original owner. Revoke owner permissions Revoke the owner permission from the owners of the selected databases. Grant permissions Grant the query, export, or change permission on the selected databases to one or more users. You can also specify an expiration time for the permission. Revoke permissions Revoke the query, export, or change permission on the selected databases from one or more users. If a user does not have the related permissions, the following message appears: `No corr`

```
esponding permissions. You do not need to recycle or release permissions .
```

Export configurations Export the configurations of the selected databases to an Excel file. The configurations include the instance status, environment, DBA, and owner. Export permission information Export the permission information about the selected databases to an Excel file. The permission information includes the database information, users, permissions, and users who grant the permissions. Other operations You can click Tables in the Actions column of a database to view the details about tables in the database. You can also move the pointer over More and select the required operation that you want to perform. For example, you can query data in the database, manage permissions, view the details about the instance to which the database belongs, and find the instance on the Instance List tab.

### 11.3 Manage users

Data Management (DMS) allows you to manage users. For example, you can manage user permissions and roles. Prerequisites You are a DMS administrator. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > User.
3. Select the user that you want to manage. Then, you can perform the following operations based
on your business requirements: Click New and set parameters to add a user. For more information, see Add a user. Edit a user Click Change in the Act ions column. In the dialog box that appears, modify the user configurations and click Conf irm Change. Disable or enable a user Move the pointer over More in the Act ions column and select Disable or Enable. Remove a user Move the pointer over More in the Act ions column and select Delet e. In the message that appears, click OK. Grant permissions Move the pointer over Aut horize in the Act ions column and select the object on which you want to grant permissions to the user. For example, you can select Aut horize inst ance, Aut horize dat abase, Aut horize t able, Aut horize Line, or Aut horize sensit ive column. In the dialog box that appears, enter a keyword to filter objects, set the Permission and Expire Date parameters, and then click OK. Release permissions Move the pointer over More in the Act ions column and select Permission Det ails. You can set conditions to filter the permissions that are granted to the user, select the permission type that you want to manage, and then click Release Permission to release the permissions.

### 11.4 Enable metadata access control

Data Management (DMS) provides the metadata access control feature. You can use this feature to allow users to view the information about and access a database or database instance on which they have permissions. Before this feature is enabled, regular users can query all databases and database instances within the current tenant account. After this feature is enabled, you can allow specific users to view the information about and access the databases or database instances on which they have permissions. This further enhances the data security of your enterprise. Background information As a centralized data management service, DMS provides different roles that are assigned different permissions. This helps you manage data in your enterprise in a secure manner. After you enable metadata access control for a database instance or database, only users who have permissions on the instance or database can view the information about and access the instance or database. This way, users can view the information about and access only databases on which they have permissions. This further enhances data security.

> Not e In DMS, permissions on a database include the query, export, and change permissions. If you have one of these permissions on a database, you can view the following information about the database:

Information about the database. You can search for the database in the search box in the upper part of the left-side navigation pane or in the top navigation bar of the DMS console. Alternatively, you can search for the database in the search box of the Select the databases, tables, or columns on which you want to apply for permissions field on the Permission Application Ticket page. Whether you can query the data in the database depends on whether you have the query permissions on the database. Information about the instance to which the database belongs. Whether you can view the information about other databases in this instance depends on whether you have permissions on the other databases. You can enable metadata control access for the following objects: A user: The user can view the information about and access only databases on which the user has permissions. A database: Only users who have permissions on the database can view the information about and access the database. A database instance: Only users who have permissions on the database instance can view the information about and access the database instance. If a user has permissions on a database in this database instance, the user can view the information about and access this database. Enable metadata access control for a user
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > User.

> Not e You are a DMS administrator.

3. Find the user for whom you want to enable metadata access control, move the pointer over More
in the Act ions column, and then select Access cont rol.
4. In the User access control dialog box, turn on Met adat a access cont rol and click OK.
Enable metadata access control for a database instance
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > Inst ance.

> Not e You are a database administrator (DBA) or a DMS administrator.

3. On the Inst ance List tab, find the instance for which you want to enable metadata access
control. Then, select the instance and click Access cont rol in the upper part of this tab.

> Not e You can also enable metadata access control for multiple instances at a time. Select multiple instances and click Access cont rol in the upper part of this tab.

4. In the dialog box that appears, turn on Met adat a access cont rol and click OK.
Enable metadata access control for a database
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > Inst ance.

> Not e You are a DBA or a DMS administrator.

3. On the Dat abase List tab, find the database for which you want to enable metadata access
control. Move the pointer over More in the Act ions column and select Access cont rol.

> Not e You can also enable metadata access control for multiple databases at a time. Select multiple databases and click Access cont rol in the upper part of this tab.

4. In the dialog box that appears, turn on Met adat a access cont rol and click OK.

### 11.5 Manage tasks

The task management feature allows you to manage various tasks that are created by using tickets. You can also use this feature to directly create or manage tasks. Prerequisites You are a database administrator (DBA) or an administrator. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > T ask.
3. On the T ask tab, view and manage tasks that are created by using tickets.
4. Find a task and perform one of the following operations based on your business requirements: For
example, you can pause, ret ry, ordelet e a task. Pause a task Click Pause to pause a task. Retry a task If a task is in the Failure state, click Ret ry to run the task again. Delete a task Click Delet e to delete a task. After a task is deleted, the status of the task changes to Delet e and the task cannot be run. Create a task Click Add SQL t ask. In the Add SQL task dialog box, enter the task description, the database that you want to manage, and the SQL statements that you want to execute. Then, click Submit T ask.

### 11.6 Configuration management

DMS allows you to manage system configurations. To implement flexible management, you must log on to the DMS console as an administrator to modify the required system configurations. Prerequisites An administrator account is required to perform the operation. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > Conf igurat ion.
3. Find the required parameter and click Change in the Act ions column of the parameter.

> Not e You can click Change Hist ory to view the change history of the parameter.

4. In the Change Parameter Configuration dialog box, enter the required value.
5. Click Conf irm Change.
Types of data changes

| key | value | Description |
|---|---|---|
| config correct _ | Modify Config | Modifies configurations. |
| project init data _ _ | Init Project Data | Initializes the data for a project. |
| program bug _ | Program Bug | Fixes a bug. |

| key | value | Description |
|---|---|---|
| require deal without backend fu _ _ _ _ nction | Requirements Without Backend Function | Manages the data of an application that does not support backend management. |
| history data clear _ _ | History Data Clean | Clears historical data. |
| test | Test | Runs a test. |
| mis operation _ | Mis Operation | Restores data after a misoperation. |
| others | Others | Changes data for other reasons. |

### 11.7 Database grouping

This topic describes how to create a database group in Data Management (DMS). You can use this feature to apply a data change or a schema change to all of the databases in a database group with ease. Prerequisites The databases that you want to add to a database group meet the following conditions: All of the instances to which the databases belong are managed in Security Collaboration mode. All of the databases are physical databases or logical databases. All of the databases are deployed in the same environment, such as the development environment. The engines of the databases are of the same type. For example, all of the databases are MySQL databases. Create a database group
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > Dat abase
grouping.
3. Click New Group.
4. In the NewGrouping dialog box, perform the following steps:
i. Enter a group name in the Group name field. ii. Set the Grouping t ype parameter to General grouping.

> Not e You cannot set this parameter to Remot e live. This feature will be available soon.

iii. Click Add dat abase. In the Search dat abase dialog box, enter a prefix in the search box to search for databases. Select one or more databases to be grouped from the matched results and click Add in the Operation column. iv. After you add all the databases to be grouped, click the icon in the upper-right corner to close the Search database dialog box.
5. After you complete the configurations, click Save.
Scenarios For example, you want to create a ticket to perform a data change on a database, and the database belongs to a database group. After you select the database, DMS displays a message to remind you that the selected database belongs to a database group. If you click OK, DMS adds all the other databases in the group as the databases on which the data change will be performed. This saves your effort in selecting databases one by one. If you click Cancel, the other databases in the group will not be selected. The following figure shows the message. This feature applies to the data change and data import tickets that are supported by DMS. For more information about how to create a ticket, see Change data and Import data. For example, you want to create a schema design ticket and select a database that belongs to a database group as a base database. After you click Perf orm Changes t o Base Dat abase, DMS displays a message. This message is used to remind you that the base database belongs to a database group and the current operation will apply to all the other databases in the group. The following figure shows the message. For more information about how to use the schema design feature, see Design a schema.

### 11.8 Security management

#### 11.8.1 Manage security rules

Security rules are implemented by using a collection of domain-specific languages (DSLs) to control user access to databases based on several factors. These factors include the type of databases, the syntax of database operations, and the number of affected rows. You can use security rules to standardize database operations, development processes, and approval processes as required. This topic describes how to manage security rules. Prerequisites You are a database administrator (DBA) or an administrator. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > Securit y Rules.
3. Perform one of the following operations based on your business requirements:
Create a rule set Click Creat e Rule Set . In the Create Rule Set dialog box, set the Engine Type, Rule Set Name, and Remarks parameters, and click Submit . Edit a rule set a. Find the required rule set and click Edit in the Act ions column of the rule set. b. In the left-side pane, click the required rule subset, for example, SQLConsole. In the rightside pane, select a checkpoint. c. Find the required rule and click Edit next to the rule. For more information about the related syntax, see DSL syntax for security rules.

> Not e You can disable or delete a rule.

Create a similar rule set a. Find the required rule set and click Creat e As in the Act ions column of the rule set. b. In the dialog box that appears, enter a name and a description for the new rule set. c. Click Submit . The system copies the configurations of the original rule set to the new rule set. Delete a rule set Find the required rule set and click Delet e in the Act ions column of the rule set. In the message that appears, click OK.

> Not e
> A deleted rule set cannot be recovered. Proceed with caution.
> You can delete only custom rule sets. You cannot delete built-in rule sets.

Set a rule set as the default rule set Find the required rule set and click Set as Def ault next to the rule set. In the message that appears, click OK. The rule set is used as the default rule set for the related database engine.

#### 11.8.2 DSL syntax for security rules

DMS provides a domain-specific language (DSL) to describe security rules. You can use the DSL syntax to define security rules. This allows you to define database development standards based on your business requirements. Overview The DSL syntax can include one or more conditions and related actions that are specified by an IF-ELSE statement.

> Not e The if clause is required. Zero or more elseif clauses can be specified. Zero or one else clause can be specified.

Example 1: If Condition 1 is met, DMS performs Action 1. `if`

```
    Condition 1
then
    Action 1
end
```

Example 2: If Condition 1 is met, DMS performs Action 1. If Condition 2 is met, DMS performs Action 2. If Condition 1 and Condition 2 are not met, DMS performs Action 3.

> Not e If the `else Action 3` clause is removed and Condition 1 and Condition 2 are not met,
> DMS performs no action.

`if`

```
    Condition 1
then
    Action 1
elseif
    Condition 2
then
    Action 2
[else Action 3] end
```

DSL syntax Conditional clauses DMS uses conditional clauses to evaluate whether to perform actions. The result of a conditional clause is true or false. A conditional clause consists of one or more connectors, operators, and factors. Connectors include AND and OR. Factors are predefined system variables. The following examples are valid conditional clauses:

```
1. true                    // This is the simplest conditional clause. The result is true
```

`.`

```
2. 1 > 0
3. 1 > 0 and 2 > 1
4. 1 <= 0 or 1 == 1
```

Connectors Connectors include AND and OR. The AND connector has higher priority than the OR connector. The

| se is | 1 <= 0 or 1 |   |
|---|---|---|
| 1 == 1 |   |   |

two connectors have lower priority than operators. For example, a conditional clause is `1 <= 0 or 1` `== 1` . DMS evaluates the result of the `1 <= 0` expression and the result of the `1 == 1` expression. Then, DMS evaluates the result of the OR expression based on the preceding results. Operators Operators are used to connect factors and constants to perform logical operations. The following table describes the operators that are supported by DMS.

| Operator | Description | Examples |
|---|---|---|

| Operator | Description | Examples |
|---|---|---|
| == | Evaluates whether a value is equal to another value. | 1 == 1 |
| != | Evaluates whether a value is not equal to another value. | 1 != 2 |
| > | Evaluates whether a value is greater than another value. | 1 > 2 |
| >= | Evaluates whether a value is greater than or equal to another value. | 1 >= 2 |
| < | Evaluates whether a value is less than another value. | 1 < 2 |
| <= | Evaluates whether a value is less than or equal to another value. | 1 <= 2 |
| in | Evaluates whether a value belongs to an array of values. | 'a' in ['a', 'b', 'c'] |
| not in | Evaluates whether a value does not belong to an array of values. | 'a' not in ['a', 'b', 'c'] |
| matchs | Evaluates whether a string matches a regular expression. | 'idxaa' matchs 'idx\w+' |
| not matchs | Evaluates whether a string does not match a regular expression. | 'idxaa' not matchs 'idx\w+' |
| isBlank | Evaluates whether a value is empty. | '' isBlank |
| isNotBlank | Evaluates whether a value is not empty. | '' isNotBlank |

|   | Not e If you need to use a backslash (\) in a regular expression, you must add another backslash (\) as an escape character before the backslash that you want to use. For example, if you want to write the idx \w+ expression, you must enter idx \\w+ . _ _ If a conditional clause includes nested expressions, we recommend that you enclose the required expressions in parentheses (). For example, a conditional clause is 1 <= 2 == tru e . To specify the priority, you can change the clause to (1 <= 2) == true . DMS first evaluates the result of the 1 <= 2 expression in the parentheses. |   |   |
|---|---|---|---|
|   |   | 1 <= 2 == tru |   |
|   | e |   |   |

Factors A factor is a predefined variable in DMS. You can use factors to obtain the context to be validated by security rules. The context includes command categories and the number of affected rows. A factor name is prefixed by `@fac.` .Each tab of the Security Rules tab includes different factors for different checkpoints. The following table describes the factors that are supported by DMS.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.sql type _ | The type of the SQL statement, for example, UPDATE or INSERT. For more information, see the SQL subcategories that are described in the "SQLConsole for relational databases" topic. |
| @fac.detail type _ | The type of the data change. Valid values: COMMON: a normal data modify ticket CHUNK DML: a lock-free data modify ticket _ PROCEDURE: a programmable object ticket CRON CLEAR DATA: a history data clean ticket _ _ BIG FILE: a large data import ticket _ |
| @fac.is logic _ | A Boolean value that indicates whether the affected database is a logical database. |
| @fac.extra info _ | Other information about the ticket. This factor is not in use. |
| @fac.is ignore affect rows _ _ _ | A Boolean value that indicates whether to skip the validation. |
| @fac.insert rows _ | The number of data rows to be inserted. |
| @fac.update delete rows _ _ | The number of data rows to be updated. |
| @fac.max alter table size _ _ _ | The size of the largest tablespace in which the table to be modified is stored. |
| @fac.is has security column _ _ _ | A Boolean value that indicates whether sensitive fields are specified in the SQL statement to be executed. |
| @fac.security column list _ _ | The sensitive fields that are specified in the SQL statement to be executed. |
| @fac.risk level _ | The risk level that is identified. |
| @fac.risk reason _ | The reason based on which the operation is identified as this risk level. |

|   | Not e You can use factors in conditional clauses. For example, you can write @fac.sql typ _ e == 'DML' to evaluate whether an SQL statement is a DML statement. |   |   |
|---|---|---|---|
|   |   | @fac.sql typ _ |   |
|   | e == 'DML' |   |   |

Action clauses An action indicates an operation that is performed when the if clause evaluates to true. For example, DMS can disable the submission of a ticket, select an approval process, approve a ticket, or reject a ticket. An action indicates the usage of a security rule. An action name is prefixed by `@act.` .Each tab of the Security Rules tab includes different actions for different checkpoints. The following table describes the actions that are supported by DMS.

| Action |   |   | Description |   |   |
|---|---|---|---|---|---|
| @act.allow submit _ |   |   | Requires the submission of SQL statements to be executed in a ticket. |   |   |
| @act.allow execute direct _ _ |   |   | Allows the execution of SQL statements in the SQLConsole. |   |   |
| @act.forbid execute _ |   |   | Disables the execution of SQL statements. |   |   |
| @act.mark risk _ |   |   | Marks the risk level of a data change. Example: @ |   |   |
|   |   |   |   | @ |   |
|   |   |   | act.mark risk 'medium-level risk: online e _ |   |   |
|   |   |   | nvironment' |   |   |
| @act.do not approve _ _ |   |   | Specifies the ID of an approval template. |   |   |
| @act.choose approve template _ _ |   |   |   |   |   |
| @act.choose approve template with reason _ _ _ _ |   |   |   |   |   |

Predefined functions DMS provides predefined functions that can be used in conditional clauses and action clauses. A function name is prefixed by `@fun.` .

| Function | Description | Format |
|---|---|---|
| @fun.concat | Connects strings to form a single string. Output: a string. Input: multiple strings. | @fun.concat('d', 'm', 's') // The output is the string 'dms'. @fun.concat('[Development standards] The [', @fac.column name, '] You must enter remarks.') _ // The output is a prompt that reminds the user who submits the ticket to enter a value in the field. |
| @fun.char len _ gth | Calculates the length of a string. Output: an integer. Input: a string. | @fun.char length('dms') // The output is 3. _ @fun.char length(@fac.table name) // The output _ _ is the length of the table name. |
| @fun.is char l _ _ ower | Evaluates whether all the letters in a string are lowercase letters. Output: true or false. Input: a string. | @fun.is char lower('dms') // The output is true. _ _ @fun.is char lower(@fac.table name) // If the _ _ _ output is true, it indicates that all the letters in the table name are lowercase. |

| Function | Description | Format |
|---|---|---|
| @fun.is char _ _ upper | Evaluates whether all the letters in a string are uppercase letters. Output: true or false. Input: a string. | @fun.is char upper('dms') // The output is false. _ _ @fun.is char upper(@fac.table name) // If all the _ _ _ letters in the table name are uppercase letters, the output is true. |
| @fun.array siz _ e | Counts the number of values in an array. Output: an integer. Input: an array of values. | @fun.array size([1, 2, 3]) // The output is 3. _ @fun.array size(@fac.table index array) // The _ _ _ output is the number of indexes of the table. |
| @fun.add | Adds multiple numeric values. Output: a numeric value. Input: multiple numeric values. | @fun.add(1, 2, 3) // 6 |
| @fun.sub | Deducts a numeric value from another numeric value. Output: a numeric value. Input: two numeric values. | @fun.sub(6, 1) // 5 |
| @fun.betwee n | Evaluates whether a value belongs to a specific closed range. The supported data types are NUMERIC, DATE, and TIME. Output: true or false. Input: three values. The first value is the value to be evaluated. The second value indicates the lower limit. The third value indicates the upper limit. | @fun.between(1, 1, 3) // The output is true because the value 1 belongs to [1, 3]. @fun.between(2, 1, 3) // The output is true because the value 2 belongs to [1, 3]. @fun.between(7, 1, 3) // The output is false because the value 7 does not belong to [1, 3]. @fun.between(@fac.export rows, 2001, 100000) _ // If the number of exported rows belongs to [2001, 100000], the output is true. @fun.between(@fun.current datetime(), '2019-10- _ 31 00:00:00', '2019-11-04 00:00:00') // If the current date and time belong to [2019-10-31 00:00:00, 2019-11-04 00:00:00], the output is true. @fun.between(@fun.current date(), '2019-10-31', _ '2019-11-04') // If the current date belongs to [2019-10-31, 2019-11-04], the output is true. @fun.between(@fun.current time(), '13:30:00', _ '23:59:59') // If the current time belongs to [13:30:00, 23:59:59], the output is true. |
| @fun.current _ datetime | Returns the current date and time, in the format of yyyy-MM- dd HH:mm:ss. Output: a string. Input: none. | @fun.current datetime() // For example, the _ output is 2019-10-31 00:00:00. |
| @fun.current _ date | Returns the current date, in the format of yyyy-MM-dd. Output: a string. Input: none. | @fun.current date() // For example, the output is _ 2020-01-13. |
| @fun.current _ time | Returns the current time, in the format of HH:mm:ss. Output: a string. Input: none. | @fun.current time() // For example, the output is _ 19:43:20. |

DSL configuration examples Limit the number of SQL statements in a ticket: If the number of SQL statements in a ticket exceeds 1,000, DMS rejects the ticket and returns the related message. `if`

```
    @fac.sql_count > 1000
then
    @act.reject_execute 'The number of SQL statements in a ticket cannot exceed 1,000.'
else
    @act.allow_execute
end
```

Allows the submission of only data manipulation language (DML) statements: If the SQL statements in a ticket are DML statements such as the UPDATE, DELETE, and INSERT statements, DMS allows the execution of the statements. `if`

```
    @fac.sql_type in [ 'UPDATE','DELETE','INSERT','INSERT_SELECT']
then
    @act.allow_submit
end
```

#### 11.8.3 Configure security rules for a database instance

instance This topic describes how to configure security rules for a database instance. Prerequisites You are a database administrator (DBA) or an administrator. The control mode of the database instance is securit y collaborat ion. Procedure
1. Log on to the DMS console.
2. In the left-side navigation pane, right-click the required database instance.
3. In the shortcut menu that appears, choose Cont rol Mode > Securit y Collaborat ion and select
the required security rule set.

> Not e You can also change the security rule set of the database instance on the Instance tab. For more information, see Instance management.

#### 11.8.4 Customize approval processes

Data Management (DMS) allows you to configure instance-level security rules so that you can customize different approval processes for different database instances or database operations. However, instance-level security rules have some limits in the production environment. This topic describes how to customize an approval process. Prerequisites You are a database administrator (DBA) or an administrator. Context Each database instance has only one DBA. However, multiple DBAs are included in an approval process to ensure business continuity regardless of whether one of the DBAs is unavailable. If multiple business units share the same database in a database instance, each business unit must approve the tickets for their respective business operations in an approval process. To resolve the issues in the preceding scenarios, you can customize approval processes. Precautions Do not assign only one approver to an approval node. We recommend that you assign at least two approvers to each approval node and at least two data owners to a database. You can assign a maximum of three data owners to a database. If multiple business units share the same database, you can specify these business units in an approval process by performing the following steps: Create an approval node and add the data owners of the business units as approvers. Then, add the new node instead of the system node Owner to an approval template. Procedure This topic describes how to customize an approval process and specify multiple DBAs in the approval process. You can perform similar steps to customize an approval process in other scenarios.
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > Approval Processes.
3. Create an approval node.
i. Click the Approval Node tab. Then, click Creat e Approval Node. ii. The following table describes the parameters that you can specify for the approval node.

| Parameter | Description |
|---|---|
| Node Name | The name of the approval node. The name must be globally unique. |
| Remarks | The description of the approval node. This parameter distinguishes the approval node from other approval nodes. |
| Approver | The Apsara Stack tenant accounts of the approvers for the approval node. You can search for approvers by keyword. Prefix match is used. Not e In this example, three approvers are selected. |

iii. Click Submit .
4. Create an approval template.
i. Click the Approval T emplat e tab. Then, click Creat e Approval T emplat e. ii. The following table describes the parameters that you can specify for the approval template.

| Parameter | Description |
|---|---|
| T emplat e Name | The name of the approval template. The name must be globally unique. |
| Remarks | The description of the approval template. This parameter distinguishes the approval template from other approval templates. |
| Approval Node | Click Add Node and select the required approval nodes. In this example, the system node Owner and the approval node that is created in Step 3 are selected to allow multiple DBAs to participate in the approval process. Not e The approval process is implemented based on the values of the Approval Order parameter in ascending order. |

iii. Click Submit . After the approval template is created, you can view the template ID. In this example, the template ID is 9.
5. Apply a new approval process.
This example shows how to edit a rule that is applied to medium-level risk approval processes under the Risk Approval Rules checkpoint. You can perform similar steps to apply a rule to other scenarios. i. In the top navigation bar, choose Syst em > Securit y > Securit y Rules. ii. Find the required rule set that you want to edit and click Edit in the Act ions column of the rule set. iii. In the left-side navigation pane, click the SQL Correct tab. iv. Select Risk Approval Rules as the checkpoint. v. Find the rule that is related to the medium-level risk approval process and click Edit . vi. In the Rule DSL field, change the template ID.

> Not e In this example, change `3` to `9` , as shown in the preceding figure. The ID

9 is the ID of the approval template that is created in Step 4. vii. Click Submit . Result If the data change tickets that you submit match the rule, all specified DBAs receive ticket approval notifications and can participate in the approval process.

#### 11.8.5 Operation audit

Data Management (DMS) provides the operation audit feature in addition to the basic features of operation log management. You can use this feature to troubleshoot database issues with ease and audit the operations that are performed on databases. You can also use this feature to view and manage the SQL statements that are used in the SQLConsole, tickets, logon information, and operation logs. Features The following table describes the two modules of the operation audit feature in DMS: Operation Logs and Operation audit.

| Module | Description | Item |
|---|---|---|
| Operation Logs | Displays the logs of all the operations that are performed in DMS. | Includes the logs of management and configuration operations, SQL statements that are used in the SQLConsole, tickets, and logon information. |
| Operation audit | Displays all the operations that are performed on databases in DMS. Not e This module provides a user interface (UI) for you to audit operations in a centralized manner. This also helps you troubleshoot database issues with ease. | Includes SQL statements that are used in the SQLConsole, tickets, and logon information. Not e Only a DMS administrator, a database administrator (DBA), a ticket submitter, and stakeholders involved in the ticket approval process are allowed to view the ticket details. |

Log data is permanently retained in DMS. You can access and view the log data of the instances that are managed in St able Change or Securit y Collaborat ion mode at any time.

> Not e You can view the log data of the instances that are managed in Flexible Management mode only for the last seven days. To view all log data, change the control mode of the instances.

Links and supported roles The following table describes the roles that you can assume to use the operation audit feature. It also shows you how to go to the Operation audit tab in the DMS console.

| Auditing dimension | Limit | Link to operation audit | Supported role |
|---|---|---|---|
| Database | You can view and audit only the operations that are performed on the current database. | On the SQLConsole tab of the database that you want to audit, click the icon in the upper-right corner. In the left-side navigation pane of the DMS console, click the instance in which the database you want to audit resides, right-click the database, and then select Operat ion audit . | You can be a DMS administrator, a security administrator, a DBA, an instance owner, or a regular user. Not e If you are a regular user, you can view and audit only the operations that you performed on the current database. |
| Instance | You can view and audit only the operations that are performed on the current instance. | In the left-side navigation pane of the DMS console, right-click the instance that you want to audit and select Operat ion audit . | You can be a DMS administrator, a security administrator, a DBA, an instance owner, or a regular user. Not e If you are a regular user, you can view and audit only the operations that you performed on the current instance. |
| Global | You can view and audit all the operations that are performed in DMS. | In the top navigation bar, move the pointer over the More icon and choose Syst em > Operat ion audit . | You can be a DMS administrator, a security administrator, or a DBA. |

View and download operation records This example shows you how to view and download all the SQL statements that are used in the SQLConsole in the last month.
1. Log on to the DMS console.
2. In the top navigation bar, move the pointer over the More icon and choose Syst em > Operat ion
audit . By default, a list of SQL statements appears.
3. Set the Time parameter to Last One Mont h and click Search.
Then, DMS returns the search results.
4. Click the
icon to download the results. Then, DMS exports an XLSX file that contains the search results on the current page.

> Not e To preview and export more results, you can set the It ems per page parameter to 100.

#### 11.8.6 Configure IP whitelists

DMS allows you to configure IP whitelists to control the service scope of DMS. You can allow user access to DMS only from specific trusted network environments. Prerequisites You are an administrator. Procedure
1. Log on to the DMS console.
2. In the top navigation, choose More > Syst em > Access IP Whit elist s.
3. Perform the following operations based on your business requirements:
Enable or disable the whitelist control feature Click Click t o Open or Click t o Close to enable or disable the whitelist control feature. Create a whitelist a. Click Creat e Whit elist . b. In the dialog box that appears, enter the IP addresses and description.

> Not e
> Separate IP addresses with semicolons (;). Make sure that each IP address in a whitelist is unique.
> You can specify IP addresses such as 10.23.12.24 or CIDR blocks such as 10.23.12.24/24, where /24 indicates the length of the IP address prefix in the CIDR block. The IP address prefix can be 1 to 32 bits in size.
> The 0.0.0.0/0 value indicates that all IP addresses are allowed.

c. Click Submit . Edit a whitelist a. Find the required IP address whitelist and click Edit in the Act ions column of the IP address. b. In the dialog box that appears, modify the IP address information. c. Click Submit . Delete a whitelist a. Find the required IP address whitelist and click Delet e in the Act ions column of the IP address. b. In the message that appears, click OK.

> Not e You cannot delete all IP address whitelists. At least one IP address whitelist must be retained.

#### 11.8.7 Row-level control

In some cases, different users may access different rows in the same table, which can be achieved by using views. Data Management (DMS) provides an alternative solution that is called the row-level control feature to control access at the row level. Prerequisites You are a security administrator, a database administrator (DBA), or an administrator. Context Row-level control is used to provide horizontal data protection for tables. All the rows in a table are distinguished by one or more specified values. These values are called control values. To access a row that corresponds to a control value in the DMS console, you must have permissions on the row.

> Not e A control value may correspond to multiple rows. If a user has permissions on a control value that corresponds to multiple rows, the user has permissions on all the rows that correspond to the control value.

Limits The sensitive data management feature applies only to relational databases, such as MySQL. However, this feature is unavailable for NoSQL databases. You can use the row-level control feature only on database instances managed in security collaboration mode. This feature applies only to physical databases. However, this feature is unavailable for logical databases. When you execute SQL statements to query, modify, or delete the data of a row-level control table, the following limits are set on filter conditions. i. The control field must be specified in SQL statements to filter data. ii. The system controls access to all the rows of a row-level control table. Users who do not have permissions on all rows can use only the `=` and `IN` operators to specify a control field. The control value that is specified in an SQL statement must be one of the control values for the table. iii. Users who do not have permissions on all rows cannot use some operators, such as OR, XOR, and logical NOT. Terms

| Term | Description |
|---|---|
| row permission | You can apply for permissions on a control value to access rows that correspond to the control value. Permissions on the rows of a table are defined as row permissions and are incorporated into the existing permissions of DMS. Permissions that can be controlled in security collaboration mode include permissions on databases, tables, columns (fields), and rows. |
| single control value | When a user applies for permissions on the rows of a row-level control table, the user can select Single to apply for permissions on a single control value. Not e A control value may correspond to multiple rows. If a user has permissions on a control value that corresponds to multiple rows, the user has permissions on all the rows that correspond to this control value. |
| all control values | When a user applies for permissions on the rows of a row-level control table, the user can select ALL to apply for permissions on all control values. After the application is approved, the user has permissions on all the rows of the table. In this case, the user can access the entire row-level control table without limits. Even if the control values are changed or more control values are added, the user still has permissions on all the rows of the table. |

| Term | Description |
|---|---|
| row-level control table | A table that requires row-level control is called a row-level control table. |
| control field | A control field is a field to which the control values of a row-level control table are added. |
| control group | A control group is a group of row-level control tables that have the same control values. For example, if Table A and Table B have the same control values, you can add the two tables to a control group. This way, you can manage the two tables at the same time by using one set of control values. |

Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > Sensit ive Dat a.
3. Click the Row Level Securit y tab.
4. Add a control group.
i. Click Add cont rol group. ii. In the Add control group dialog box, set the required parameters.

| Parameter | Description |
|---|---|
| Cont rol Group | Enter a name for the control group. |
| Row Conf igurat ion | Click Add to add a row configuration in which you can specify a database, table, and field. Not e You can repeat this step to add multiple row configurations. |
| DB T able Column | Search for databases by keyword and select a database. Then, select a table and a field from the drop-down lists. Not e The selected field is the control field. |

iii. Click Add.
5. Add control values.
i. Find the new control group and click Det ails in the Act ions column of the control group. ii. Click Add Row Value. iii. In the Import Row Value dialog box, specify whether to append row values and enter the required row values.

> Not e Separate multiple row values with commas (,).

iv. Click Import . What to do next After you configure row-level control settings for a table, a user may still have no permission on a control value that corresponds to one or more rows in the table. In this case, an error appears when the user queries row data. The error indicates that the user does not have permissions to access the row. The user can apply for permissions on the control value to access the rows. For more information, see Apply for permissions.

#### 11.8.8 Manage sensitive data

Data Management (DMS) allows you to manage all classified sensitive and confidential fields in a unified manner. You can configure encryption algorithms for sensitive and confidential fields. This improves the control over the data masking feature. Prerequisites You are a security administrator, a database administrator (DBA), or an administrator. Context When you query a table that contains sensitive or confidential fields on which and you do not have permissions on the fields, the values of the fields are displayed as `******` in the query results. In this case, sensitive data is fully masked. In some scenarios, developers or test engineers may need to view a part of sensitive data for troubleshooting. To meet this requirement, you can configure masking algorithms to show some sensitive data. Limits The sensitive data management feature applies only to relational databases such as MySQL. However, this feature is unavailable for NoSQL databases. To use this feature, the required database instance must be managed in security collaboration mode. Procedure
1. Log on to the DMS console.
2. Specify security levels for fields in the required table.

> Not e If security levels are specified for the fields, skip this step.

i. In the left-side database instance list, click the icon next to the required database instance to show the databases in the instance. ii. Find the required database, right-click the database, and then select T ables. iii. Click the icon next to the table name to show the table details. iv. Click Adjust . v. In the Adjust Security Level dialog box, change the security levels of fields. vi. Click Submit f or Securit y Depart ment Approval.

> Not e The application to increase the security level of a field is automatically approved. The application to decrease the security level of a field is approved based on the approval process specified by an administrator or DBA.

vii. In the message that appears, click OK.
3. In the top navigation bar, choose More > Syst em > Sensit ive Dat a.
4. Find the required field and click Add Algorit hm in the Act ions column of the field.
5. In the dialog box that appears, configure a masking algorithm.

| Parameter | Description |
|---|---|
| Algorit hm T ype | The type of the algorithm. You can select an algorithm type based on your business requirements. |
| Algorit hm Conf igurat ion It em | The algorithm configuration items vary based on the specified algorithm type. Fixed Posit ion algorithm type You must set the Masking String and Masking Position parameters. For example, you can set the Masking String parameter to ***. The Masking Position parameter specifies the positions of the characters to be masked in the field values. The positions are in the format of coordinates. Examples: (1, 4): masks the first four characters. You can also enter (4) to simplify the format. (-4): masks the last four characters. Not e You can specify a maximum of three positions. For example, (1, 4), (8, 10), (-4) indicates to mask the first four characters, the eighth to tenth characters, and the last four characters. Fixed Charact er algorithm type You must set the Masking String and Character to Be Replaced parameters. Not e The Character to Be Replaced parameter specifies the characters that you want to mask in the format of a string. You can specify a maximum of three strings. Full Masking algorithm type You need to set only the Masking String parameter. |
| Algorit hm Descript ion | Enter a description that can help you identify the algorithm. |

6. Click Add.

#### 11.8.9 Data protection

Data Management (DMS) provides the data protection feature. This topic describes how to use the data protection feature. Context Data protection is one of the greatest challenges in the process of data application. Data is the core of an enterprise. Most critical and sensitive information is stored as structured data. The information includes ID numbers, bank account numbers, phone numbers, customer records, medical records, transaction records, and salary records. Security events may cause enormous economic loss and damage the reputation of enterprises. These security events include data tampering, data theft, and data misuse. To ensure data security, you need to understand how to protect your data from these security risks. The data protection feature helps the security management team achieve the following goals: Intelligently recognizes and classifies sensitive data. Then, you can group the data based on the security level of fields for DMS. Audits databases and prevents against data loss. Provides an efficient method to identify data application mode. Then, you can use the user and entity behavior analytics identification model and big data security expert rules of Ant Financial to identify and manage risks. Provides unified masking SDKs to protect sensitive information. These SDKs are used to intelligently identify sensitive data that exists in the system content that is displayed and mask the data. These operations are performed based on the definition of sensitive information and masking policies that are specified in the data protection feature. These SDKs are also used to provide a unified method to manage masking rules within an enterprise, and increase the efficiency of security management. Control access Data protection is a tool that is provided by DMS to data security administrators. To enable and use the data protection feature, you must log on to the DMS console with security administrator permissions.
1. Log on to the DMS console.

> Not e You must use an account with administrator permissions to log on to the DMS console.

2. In the top navigation bar, choose More > Syst em > User.
3. Click Change.
4. Select Securit y Administ rat or and click Conf irm Change.
5. Use the account to re-log on to the Log on to the DMS console again.
6. In the top navigation bar, choose More > Securit y > Dat a Prot ect ion.

> Not e To enable a user to use the data protection feature, you must log on to the DMS console with security administrator permission to enable the feature and authorize the user to use the feature.

Data classification The data protection feature classifies fields based on the custom automatic classification setting that is specified in the metadata of these fields. The classification results are used to update the levels of these DMS fields. This feature facilitates the access control over DMS fields.
1. Log on to the DMS console.

> Not e You must use an account with security administrator permissions to log on to the DMS console.

2. In the top navigation bar, choose More > Securit y > Dat a Prot ect ion.
3. In the left-side navigation pane, choose Rule Conf igurat ion > Dat a Ident if icat ion Rules.
4. In the upper-right corner, click Creat e Rule. Then, set the Dat a T ype, Dat a Name, Owner and
Remarks parameters.
5. Click Next .
6. Set the Level parameter. Valid values: Internal, Sensitive, and Confidential. Select Field Scanning in
the Data Recognition Rules field.
7. Click Next . After the rule is configured, click Save and Enable.

> Not e
> You can view all rules on the Dat a Ident if icat ion Rules page. You can also modify, disable, or enable a rule on this page.
> After a rule is applied, the system identifies and classifies data based on metadata every hour on the hour. The security level of a field in DMS Enterprise is updated based on the classification result. This enables field-level access control over DMS operations.

Manually correct data The Manual Data Correction page shows all identified fields. This way, you can verify these fields. If some fields are incorrectly identified, you can remove these fields or change the related types. After data is corrected, the results are immediately synchronized to the DMS Enterprise console. Data detection The data detection feature is used to collect statistics based on the results of data identification from multiple dimensions and show the details of fields that are identified in the field details list. These dimensions include the security level and related instance.

### 11.9 Security rules

#### 11.9.1 Overview of security rule sets

Security rule sets are implemented by using a collection of domain-specific languages (DSLs) to control user access to databases based on several factors. These factors include the type of databases, the syntax of database operations, and the number of affected rows. You can use security rule sets to standardize database operations, development processes, and approval processes as required. This topic describes the features that are supported by security rule sets. You can click the link of a feature to view the information about the feature. The information includes the basic configuration items, checkpoints, factors, actions, and supported statements or commands.

#### 11.9.2 Manage security rules under checkpoints

This topic describes how to configure a security rule under the SQL Execution Quantity Criteria checkpoint on the SQL Editor tab. You can configure security rules under other checkpoints by using a method similar to that described in this topic. Procedure
1. Log on to the DMS console.
2. In the top navigation bar, choose More > Syst em > Securit y Rules.
3. Find the required security rule set and click Edit in the Act ions column of the security rule.

> Not e In this example, the security rule that is configured for MySQL databases is used.

4. Click a tab and then click a checkpoint based on your business requirements. In this example, click
the SQL Edit or tab and then click the SQL Execut ion Quant it y Crit eria checkpoint.

> Not e

For more information about the tabs and checkpoints, see Overview of security rule sets. You can click Creat e Rule to create a security rule. For more information about the syntax, see DSL syntax for security rules.
5. Find the required security rule and click Edit in the Act ions column of the security rule.

> Not e You can click Disable to disable a security rule or click Delet e to delete a security rule.

6. In the Change Rule - SQL Editor dialog box, modify the DSL statements of the security rule based on
your business requirements. For more information about the syntax, see DSL syntax for security rules. In this example, change the maximum number of SQL statements that can be executed at a time from 1,000 to 500.

> Not e
> A large number of security rule templates are provided for each checkpoint. You can click Load f rom T emplat e Dat abase to use a template.

For more information about factors and actions, see Overview of security rule sets.
7. Click Submit .

#### 11.9.3 SQLConsole for relational databases

DMS allows you to manage relational and non-relational databases on the SQLConsole tab. The definition and classification of security rules are different for relational and non-relational databases. This topic describes the security rules for relational databases on the SQLConsole tab, such as MySQL databases. Default security rules Constraints on SQL statement categories: No constraints are imposed on data query language (DQL) statements. By default, DML statements, DDL statements, data control language (DCL) statements, and SQL statements that cannot be identified by DMS are all blocked. To execute DML, DDL, or DCL statements on the SQLConsole tab, you must configure and enable corresponding security rules. Constraints on permissions on databases, tables, and fields: By default, users can perform operations on databases, tables, and fields without permission validation. To enable permission validation, you must configure and enable security rules under the SQL Permission Crit eria checkpoint. For more information, see Supported checkpoints. Basic configuration items

| Configuration item | Description |
|---|---|
| Maximum number of ret urned rows per query | The maximum number of rows that can be returned for a query. |
| Maximum number of rows ret urned f or a single query wit h sensit ive column condit ions | The maximum number of rows that can be returned for a query that contains query conditions for sensitive fields. |
| Limit t he maximum allowed SQL f ull t able scan (MB) | The maximum size of data that can be scanned. Before an SQL statement is executed, DMS checks the execution plan. If the size of the data to be scanned exceeds the specified threshold, the SQL statement fails to be executed. Not e This item can be configured only for MySQL and Oracle databases. |
| T urn of f t he execut ion of change SQL validat ion af f ect s t he number of rows and prompt s | Specifies whether to check the number of rows to be affected and display a prompt before DMS executes an SQL statement to change data. By default, this item is disabled. |
| How many rows does result set page support | The maximum number of rows that can be returned in the query result set on the SQLConsole tab. |
| Does t he result set support paging | Specifies whether the query result set can be displayed on multiple pages on the SQLConsole tab. |
| Does t he result set support edit ing | Specifies whether the query result set can be edited on the SQLConsole tab. |

Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| SQL Execut ion Quant it y Crit eria | Allows you to limit the number of SQL statements that can be submitted at a time. |
| DQL SQL Crit eria | Allows you to set constraints on DQL statements. |

| Checkpoint | Description |
|---|---|
| Ot her SQL Crit eria | Allows you to set constraints on multiple categories of SQL statements. Different enterprises may define different high-risk SQL statements, which may include specific subcategories of DML, DCL, and DDL statements. Not e You can also set constraints on SQL statements that cannot be identified by DMS. |
| SQL Permission Crit eria | Allows you to set constraints on the execution of SQL statements from the aspect of permissions. For example, DMS checks whether a user has the required permissions on the corresponding databases, tables, and fields. |
| SQL Execut ion Perf ormance Crit eria | Allows you to set constraints on the execution of SQL statements from the aspect of performance. For example, you can specify that a DML statement is not executed if the number of rows to be affected by the statement exceeds the specified threshold, or that a DDL statement is not executed if the size of the table involved exceeds the specified threshold. |
| Except ion Recognit ion Crit eria of Dat abase and T able Column Permissions | After a user submits SQL statements on the SQLConsole tab, DMS parses the SQL statements and checks whether the user has the required permissions on the corresponding databases, tables, and fields. You can configure security rules under this checkpoint to ensure that if exceptions occur when DMS parses complex SQL statements, these statements can be executed. Not e If you configure and enable security rules under the Except ion Recognit ion Crit eria of Dat abase and T able Column Permissions checkpoint, security rules under the SQL Permission Criteria, DQL SQL Criteria, Other SQL Criteria, and SQL Execution Performance Criteria checkpoints are automatically disabled. |
| SQL Execut ion Crit eria in Logical Dat abases | This checkpoint is reserved for logical databases and not suitable for physical databases. |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors for relational databases on the SQLConsole tab.

| Factor | Description |
|---|---|
| @fac.sql count _ | The number of SQL statements that are submitted at a time. |
| @fac.select sql count _ _ | The number of DQL statements among the SQL statements that are submitted at a time. |

| Factor | Description |
|---|---|
| @fac.dml sql count _ _ | The number of DML statements among the SQL statements that are submitted at a time. |
| @fac.sql type _ | The category and subcategory of the SQL statement. For more information, see Supported SQL statements. |
| @fac.sql sub type _ _ |   |
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.fulltable delete _ | A Boolean value that indicates whether the current SQL statement deletes a full table. Valid values: true and false. |
| @fac.fulltable update _ | A Boolean value that indicates whether the current SQL statement updates a full table. Valid values: true and false. |
| @fac.current sql _ | The current SQL statement. |
| @fac.user is admin _ _ | A Boolean value that indicates whether the current user is a DMS administrator. Valid values: true and false. |
| @fac.user is dba _ _ | A Boolean value that indicates whether the current user is a DBA. Valid values: true and false. |
| @fac.user is inst dba _ _ _ | A Boolean value that indicates whether the current user is the DBA of the current instance. Valid values: true and false. |
| @fac.user is sec admin _ _ _ | A Boolean value that indicates whether the current user is a security administrator. Valid values: true and false. |
| @fac.sql affected rows _ _ | The number of rows to be affected by the current SQL statement. Warning This factor triggers COUNT operations, which may affect the database performance. Use this factor with caution. |
| @fac.sql relate table store size _ _ _ _ | The estimated total size of the table to be accessed by the current SQL statement. Unit: MB. Not e This value is estimated based on the metadata that is obtained by DMS. It is not an actual value. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions for relational databases on the SQLConsole tab.

| Action | Description |
|---|---|
| @act.reject execute _ | Rejects the request to execute the current SQL statement. |
| @act.allow execute _ | Allows the current SQL statement to be executed. |
| @act.reject sql type execute _ _ _ | Rejects the request to execute a specific subcategory of SQL statements. You must specify an SQL statement subcategory after the action name. Example: @act.reject sql type execute _ _ _ 'UPDATE' . |
| @act.allow sql type execute _ _ _ | Allows a specific subcategory of SQL statements to be executed. You must specify an SQL statement subcategory after the action name. Example: @act.allow sql type execute 'UPDATE' . _ _ _ |
| @act.check dml sec column per _ _ _ _ mission | Checks whether a user has the required permissions on sensitive fields. If the user does not have the permissions, the DML statement for data change is not executed. |
| @act.uncheck dml sec column p _ _ _ _ ermission | Does not check whether a user has the required permissions on sensitive fields. |
| @act.check sql access permissio _ _ _ n | Checks whether a user has the required permissions, such as query and change permissions, on the databases, tables, and fields that are involved in the SQL statements to be executed. |
| @act.uncheck sql access permis _ _ _ sion | Does not check whether a user has the required permissions on the objects that are involved in the SQL statements to be executed. |
| @act.enable sec column mask _ _ _ | De-identifies sensitive fields in query result sets that are returned for SQL statements that are submitted by users who do not have permissions on the sensitive fields. |
| @act.disable sec column mask _ _ _ | Does not de-identify sensitive fields in query result sets that are returned for SQL statements that are submitted by users who do not have permissions on the sensitive fields. |

|   | 'UPDATE' |
|---|---|

Supported SQL statements

| Category | Subcategory |
|---|---|
| DQL | SELECT DESC EXPLAIN SHOW |

| Category | Subcategory |
|---|---|
| DML | INSERT INSERT SELECT _ REPLACE REPLACE INTO _ UPDATE DELETE MERGE |
| DDL | DATABASE OP _ CREATE CREATE INDEX _ CREATE VIEW _ CREATE SEQUENCE _ CREATE TABLE _ CREATE SELECT _ TRUNCATE DROP INDEX _ DROP VIEW _ DROP TABLE _ RENAME ALTER ALTER INDEX _ ALTER VIEW _ ALTER TABLE _ ALTER SEQUENCE _ CREATE FUNCTION _ CREATE PROCEDURE _ ALTER FUNCTION _ ALTER PROCEDURE _ DROP FUNCTION _ DROP PROCEDURE _ |
| DCL | GRANT DECLARE SET ANALYZE FLUSH OPTIMIZE KILL |

#### 11.9.4 SQLConsole for MongoDB

DMS allows you to manage relational and non-relational databases on the SQLConsole tab. The definition and classification of security rules are different for relational and non-relational databases. This topic describes the security rules for MongoDB databases on the SQLConsole tab. Basic configuration items Maximum number of ret urned rows per query: the maximum number of rows that can be returned for a query. Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| User Permission Validat ion | Allows you to specify whether to check the permissions of specific users when they submit commands. |
| Collect ion St at ement Crit eria | Allows you to specify whether to allow DMS to run a specific category of commands. |
| DB St at ement Crit eria |   |
| Cache Query St at ement Crit eria |   |
| User Management St at ement Crit eria |   |
| Role Management St at ement Crit eria |   |
| Replicat ion Set St at ement Crit eria |   |
| Sharding St at ement Crit eria |   |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as command categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors for MongoDB databases on the SQLConsole tab.

| Factor | Description |
|---|---|

| Factor | Description |
|---|---|
| @fac.sql sub type _ _ | The subcategory of the current command. For more information about the supported commands, see Supported MongoDB commands. |
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT . |
| @fac.current sql _ | The current command. |
| @fac.user is admin _ _ | A Boolean value that indicates whether the current user is a DMS administrator. Valid values: true and false. |
| @fac.user is dba _ _ | A Boolean value that indicates whether the current user is a DBA. Valid values: true and false. |
| @fac.user is inst dba _ _ _ | A Boolean value that indicates whether the current user is the DBA of the current instance. Valid values: true and false. |
| @fac.user is sec admin _ _ _ | A Boolean value that indicates whether the current user is a security administrator. Valid values: true and false. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions for MongoDB databases on the SQLConsole tab.

| Action | Description |
|---|---|
| @act.reject execute _ | Rejects the request to run the current command. |
| @act.allow execute _ | Allows the current command to be run. |
| @act.reject sql type execute _ _ _ | Rejects the request to run a specific subcategory of commands. You must specify a subcategory after the action name. Example: @act.reject sql type execute 'UPDATE' . _ _ _ |
| @act.allow sql type execute _ _ _ | Allows a specific subcategory of commands to be run. You must specify a subcategory after the action name. |

Supported MongoDB commands

| Category | Subcategory | Command |
|---|---|---|

| Category | Subcategory | Command |
|---|---|---|
| Collection commands | Query commands | aggregate find findOne count distinct getIndexes getShardDistribution isCapped stats dataSize storageSize totalIndexSize totalSize |
|   | Data update commands | insert save findAndModify remove update |
|   | Collection modification commands | drop renameCollection |
|   | Index modification commands | createIndex createIndexes dropIndexes reIndex |
|   | Other commands | validate |

| Category | Subcategory | Command |
|---|---|---|
| Database commands | Database query commands | commandHelp currentOp getCollectionInfos getCollectionNames getLastError getLastErrorObj getLogComponents getPrevError getProfilingStatus getReplicationInfo getSiblingDB help isMaster listCommands printCollectionStats printReplicationInfo version serverBuildInfo serverStatus,stats |
|   | Collection creation commands | createCollection |
|   | High-risk commands | dropDatabase fsyncLock fsyncUnlock killOp repairDatabase resetError runCommand |
| Commands related to the query plan cache | Read commands | getPlanCache getPlansByQuery listQueryShapes |
|   | Write commands | clearPlansByQuery |
|   | User query commands | getUser getUsers |

| User Guide·System management |   |   |
|---|---|---|
|   | Data Managemen |   |
| Category | Subcategory | Command |
| User management commands | User modification commands | createUser changeUserPassword dropUser dropAllUsers grantRolesToUser revokeRolesFromUser updateUser |
| Role management commands | Role query commands | getRole getRoles |
|   | Role modification commands | createRole dropRole dropAllRoles grantPrivilegesToRole revokePrivilegesFromRole revokeRolesFromRole updateRole |
| Replica set commands | N/A | help printReplicationInfo status conf |
| Sharding commands | N/A | getBalancerState isBalancerRunning |

#### 11.9.5 SQLConsole for Redis

DMS allows you to manage relational and non-relational databases on the SQLConsole tab. The definition and classification of security rules are different for relational and non-relational databases. This topic describes the security rules for Redis databases on the SQLConsole tab. Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| Permission Execut ion St at ement Crit eria | Allows you to set constraints on the permissions for command execution. |

| ata Management | User Guide·System managemen |
|---|---|

| Checkpoint | Description |
|---|---|
| St at ement Crit eria: Keys | Allows you to specify whether to check the permissions of specific users when they submit commands. |
| St at ement Crit eria: St ring | Allows you to specify whether to allow the execution of various Redis commands. |
| St at ement Crit eria: List |   |
| St at ement Crit eria: SET |   |
| St at ement Crit eria: Sort edSet |   |
| St at ement Crit eria: Hash |   |
| St at ement Crit eria: Ot her |   |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors for Redis databases on the SQLConsole tab.

| Factor | Description |
|---|---|
| @fac.cmd type _ | The type of the Redis command. For more information about valid values, see Supported Redis commands. |
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT . |
| @fac.is read _ | A Boolean value that indicates whether the current command is a read command. Valid values: true and false. |
| @fac.is write _ | A Boolean value that indicates whether the current command is a write command. Valid values: true and false. |
| @fac.current sql _ | The current command. |
| @fac.user is admin _ _ | A Boolean value that indicates whether the current user is a DMS administrator. Valid values: true and false. |

|   | User Guide·System management | Data Managemen | t |
|---|---|---|---|

| Factor | Description |
|---|---|
| @fac.user is dba _ _ | A Boolean value that indicates whether the current user is a DBA. Valid values: true and false. |
| @fac.user is inst dba _ _ _ | A Boolean value that indicates whether the current user is the DBA of the current instance. Valid values: true and false. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions for Redis databases on the SQLConsole tab.

| Action | Description |
|---|---|
| @act.reject execute _ | Rejects the request to run the current command. |
| @act.allow execute _ | Allows the current command to be run. |

Supported Redis commands

| Category | Subcategory | Command |
|---|---|---|
| Key-related commands | Key-related read commands | EXISTS TTL PTTL RANDOMKEY TYPE SCAN OBJECTS |

| Category | Subcategory | Command |
|---|---|---|
|   | Key-related write commands | DEL DUMP EXPIRE EXPIREART MOVE PERSIST PEXPIRE PEXPIREAT RENAME RENAMENX RESTORE SORT TOUCH UNLIMK WAIT MIGRATE |
| String-related commands | String-related read commands | GET GETRANGE BITCOUNT GETBIT MGET STRLEN BITOPS |
|   | String-related write commands | APPEND BITFIELD BITOP DECR DECRBY GETSET INCR INCRBY INCRBYFLOAT MSET MSETNX PSETEX SET SETNX |

|   | Data Managemen |   |
|---|---|---|
| Category | Subcategory | Command |
| List-related commands | List-related read commands | LINDEX LLEN LRANGE |
|   | List-related write commands | BLPOP BRPOP BRPOPLPUSH LINSERT LPOP LPUSH LPUSHX LREM LSET LTRIM RTOP RPOPLPUSH RPUSH RPUSHX |
| Set-related commands | Set-related read commands | SCARD SISMEMBER SRANDMEMBER SSCAN |
|   | Set-related write commands | SADD SMOVE SPOP SREM |

| Category | Subcategory | Command |
|---|---|---|
|   | Sorted set-related read commands | ZCARD ZCOUNT ZLEXCOUNT ZRANGE ZRANGEBYLEX ZRANGEBYSCORE ZRANK ZREVRNGE ZREVRANGEBYLEX ZREVRANGEBYSCORE ZREVRANK ZSCAN ZSCORE |
| Sorted set-related commands |   |   |
|   | Sorted set-related write commands | ZADD ZINCRBY ZINTERSTORE ZPOPMAX ZPOPMIN ZREM ZUNIONSTORE BZPOPMIN BZPOPMAX |
| Hash-related commands | Hash-related read commands | HEXISTS HGET HLEN HMGET HSCAN HSTRLEN |
|   | Hash-related write commands | HDEL HINCRBY HINCRBYFLOAT HMESET HSET HSETNX |

#### 11.9.6 Data change

In DMS, you can execute SQL statements for data changes. However, the execution requires a high level of security. DMS allows you to configure security rules on the SQL Correct tab to validate the submission and approval of tickets for data changes. Only the SQL statements that are validated by the security rules can be executed. Background information Based on a DSL, new security rules are flexible to use. You can apply new security rules to define risk levels for tickets so that a ticket can be submitted to the approval process that is designed for the specified risk level. For more information, see DSL syntax for security rules. Basic configuration items

| Configuration item | Description |
|---|---|
| Dat a change def ault approval T emplat e | By default, this approval template takes effect if you do not configure different approval rules for data changes at different risk levels under the Risk Approval Rules checkpoint. In the Switch Approval Template dialog box, you can change the approval process of the default approval template. For more information, see Customize approval processes. |
| Dat a Change risk level list | This risk level list defines risk levels that are used in the Risk Ident if icat ion Rules and Risk Approval Rules checkpoints to identify and classify risks in data changes. You can set risk levels based on the type and scenario of data changes. Data changes at different risk levels are submitted to different approval processes. DMS allows you to set the following four risk levels: low: a low risk level. middle: a medium risk level. high: a high risk level. highest: a critical risk level. |

Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|

| Checkpoint | Description |
|---|---|
| SQL execut ion rules | SQL execution rules are used to limit the SQL statements that can be submitted for execution. If you do not enable SQL execution rules, all SQL statements that are used for data changes cannot be executed. Assume that you want to use DML statements to change the data of a database in an online environment. You can create the following SQL execution rule: Example: if @fac.env type not in ['product'] _ and @fac.sql type in [ 'UPDATE','DELETE','INSERT'] _ then @act.allow submit _ end Note: The preceding rule specifies that you can only submit data change tickets to execute UPDATE, DELETE, and INSERT statements on a database that is deployed in an online environment. |
| Risk Ident if icat ion Rules | If a ticket conforms to the preset SQL execution rules, DMS continues to validate the ticket based on the risk identification rules. Risk identification rules are used to identify and classify risks in data changes. You can create risk identification rules based on your database environment, the number of rows in which data is affected, and the categories and subcategories of SQL statements. Not e Different risk identification rules apply to different check items. DMS automatically identifies the highest risk level for a data change. For example, if the risk level of a data change is identified as high, medium, and low by one, three, and five risk identification rules, DMS assumes that the data change is at high risk. Example: if @fac.env type not in ['product','pre'] _ then @act.mark risk 'low 'Low risk level: offline environment' _ end Note: The preceding rule specifies that if the destination database is deployed in an offline environment, data changes are at low risk. |

| Checkpoint | Description |
|---|---|
| Risk Approval Rules | After the risk level of a data change is identified by the risk identification rules, DMS processes the ticket based on the risk approval rules. You can customize risk approval rules under the Risk Approval Rules checkpoint. Not e If a data change does not hit risk approval rules, DMS uses the default approval template that is specified under the Basic Configuration Item checkpoint to process the ticket. By default, an offline environment is identified as a factor at low risk and requires no approval. |
| Bat ch Dat a import rules | These rules apply only to the validation of data import tickets. You can use the default rules that are provided in templates, or configure rules based on your actual needs. |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the SQL Correct tab.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.sql type _ | The type of the SQL statement. The value is the subcategory of the SQL statement, such as UPDATE or INSERT. For more information, see Supported SQL statements. |
| @fac.detail type _ | The type of the data change. Valid values: COMMON: a Normal Data Modify ticket. CHUNKDML: a Lock-Free Data Modify ticket. _ PROCEDURE: a Programmable Object ticket. CRONCLEARDATA: a History Data Clean ticket. _ _ BIGFILE: a Large Data Import ticket. _ |
| @fac.is logic _ | A Boolean value that indicates whether the database to be affected is a logical database. |
| @fac.extra info _ | The additional information about the data change. This factor is not in use. |
| @fac.is ignore affect rows _ _ _ | A Boolean value that indicates whether to skip the validation. |
| @fac.insert rows _ | The number of rows of data to be inserted. |

| ata Management | User Guide·System managemen |
|---|---|

| Factor | Description |
|---|---|
| @fac.update delete rows _ _ | The number of rows of data to be updated. |
| @fac.max alter table size _ _ _ | The size of the largest tablespace where the table to be modified is stored. |
| @fac.is has security column _ _ _ | A Boolean value that indicates whether the SQL statement to be executed involves sensitive fields. |
| @fac.security column list _ _ | A list of sensitive fields that the SQL statement to be executed involves. |
| @fac.risk level _ | The risk level of the operation that is to be performed by the SQL statement. |
| @fac.risk reason _ | The reason for identifying the operation to be performed as at the risk level. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported action on the SQL Correct tab.

| Action |   | Description |   |   |
|---|---|---|---|---|
| @act.allow submit _ |   | Requires the submission of SQL statements to be executed in a ticket. |   |   |
| @act.allow execute direct _ _ |   | Allows the execution of SQL statements in the SQLConsole. |   |   |
| @act.forbid execute _ |   | Forbids the execution of SQL statements. |   |   |
| @act.mark risk _ |   | Marks the risk level of a data change. Example: @act.mark risk 'Medium risk level: online _ environment' . |   |   |
|   |   |   | @act.mark risk 'Medium risk level: online _ |   |
|   | _ | environment' |   |   |
| @act.do not approve _ _ |   | Specifies the ID of an approval template. |   |   |
| @act.choose approve template _ _ |   |   |   |   |
| @act.choose approve template with reason _ _ _ _ |   |   |   |   |

#### 11.9.7 Permission application

DMS allows you to configure security rules on the Access apply tab to validate applications for permissions, including permissions on instances, databases, and tables. Background information In DMS, security rules are flexible to use. You can apply security rules to define risk levels for tickets so that a ticket can be submitted to the approval process that is designed for the specified risk level. For more information about the DSL syntax, see DSL syntax for security rules. Basic configuration items The following table describes the basic configuration items that are supported on the Access apply tab.

| Configuration item | Description |
|---|---|
| [Inst ance-permission applicat ion] def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for instance permission applications at different risk levels under the Validat ion f or Inst ance Permission Applicat ion checkpoint. Not e In the Switch Approval Template dialog box, you can change the approval process of the default approval template. |
| [DB-permission applicat ion] def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for database permission applications at different risk levels under the Dat abase Permission Applicat ion Validat ion checkpoint. |
| T able-permission request def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for table permission applications at different risk levels under the T able Permission Applicat ion Validat ion checkpoint. |
| [Programmable object - permission applicat ion] def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for programmable object permission applications at different risk levels under the Programmable object verif icat ion checkpoint. |
| [Field-permission applicat ion] def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for sensitive field permission applications at different risk levels under the Sensit ive Field Applicat ion Validat ion checkpoint. |
| Line-permission applicat ion def ault approval T emplat e | By default, this approval template takes effect if you do not set different approval processes for row permission applications at different risk levels under the Line permission applicat ion verif icat ion checkpoint. |
| [Owner-applicat ion] def ault approval t emplat e (when t he resource has no Owner) | By default, this approval template takes effect if you do not set different approval processes for data ownership applications at different risk levels under the Owner Applicat ion Validat ion checkpoint and the data that is involved in the application has no owner. |

| Configuration item | Description |
|---|---|
| [Owner-applicat ion] def ault approval t emplat e (when t he resource has an Owner) | By default, this approval template takes effect if you do not set different approval processes for data ownership applications at different risk levels under the Owner Applicat ion Validat ion checkpoint and the data that is involved in the application has one or more owners. |

Supported checkpoints When a user submits a ticket to apply for permissions, DMS checks whether the ticket conforms to rules that are specified under checkpoints. The ticket can be submitted only after DMS determines that the ticket conforms to all rules that are specified under checkpoints.

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| Owner Applicat ion Validat ion | Allows you to set approval processes or constraints for Inst ance- OWNER, T able-OWNER, and Dat abase-OWNER tickets. |
| Validat ion f or Inst ance Permission Applicat ion | Allows you to set approval processes or constraints for Inst ance- Perf ormance and Inst ance-Login tickets. |
| Dat abase Permission Applicat ion Validat ion | Allows you to set approval processes or constraints for Dat abase- Permission tickets. |
| T able Permission Applicat ion Validat ion | Allows you to set approval processes or constraints for T able- Permission tickets. |
| Programmable object verif icat ion | Allows you to set approval processes or constraints for Programmable Object tickets. |
| Sensit ive Field Applicat ion Validat ion | Allows you to set approval processes or constraints for Sensit ive Column-Permission tickets. |
| Line permission applicat ion verif icat ion | Allows you to set approval processes or constraints for Row- Permission tickets. |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and database names. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Access apply tab.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |

| User Guide·System management | Data Managemen |
|---|---|

| Factor | Description |
|---|---|
| @fac.schema name _ | The name of the database. |
| @fac.perm apply duration _ _ | The period of time during which the applicant needs the permission. Unit: hours. |
| @fac.column security level _ _ | The security level of the field. Valid values: sensitive confidential inner |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported action on the Access apply tab.

| Action | Description |
|---|---|
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. |
| @act.do not approve _ _ | Specifies the ID of an approval template. |
| @act.choose approve template _ _ |   |
| @act.choose approve template with reason _ _ _ _ |   |

#### 11.9.8 Data export

DMS allows you to manage security rules on the Data Export tab to validate the permissions of applicants on involved databases, tables, sensitive fields, and rows during the submission and approval of data export tickets. This helps ensure data security. Basic configuration items Dat a export def ault approval T emplat e: the default approval template that takes effect if you do not set different approval processes for data export tickets at different risk levels under the Approval Rule Validation checkpoint. In the Switch Approval Template dialog box, you can change the approval process of the default approval template. For more information, see Customize approval processes. Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| Pre-check Validat ion | Allows you to specify whether to validate the permissions of applicants on involved databases, tables, sensitive fields, and rows by configuring security rules. |
| Approval Rule Validat ion | Allows you to submit data export tickets to different approval processes by configuring security rules. For example, you can submit tickets for exporting more than a specific number of rows to an approval process and other tickets to another approval process. |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Data Export tab.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.is ignore export rows check _ _ _ _ | A Boolean value that indicates whether to skip the check on the number of rows to be affected. |
| @fac.export rows _ | The number of rows to be exported. |
| @fac.include sec columns _ _ | A Boolean value that indicates whether the data to be exported contains sensitive fields. |
| @fac.sec columns list _ _ | The sensitive fields that require or do not require approval before data is exported. The sensitive fields are displayed in the format of Table name.Field name,[Table name.Field name, ...] . |
| @fac.user is admin _ _ | A Boolean value that indicates whether the applicant is a DMS administrator. |
| @fac.user is dba _ _ | A Boolean value that indicates whether the applicant is a DBA. |
| @fac.user is inst dba _ _ _ | A Boolean value that indicates whether the applicant is the DBA of the current instance. |
| @fac.user is sec admin _ _ _ | A Boolean value that indicates whether the applicant is a security administrator. |

|   |   |   | Table |
|---|---|---|---|
|   |   | name.Field name,[Table name.Field name, |   |
|   |   | ...] |   |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Data Export tab.

| Action | Description |
|---|---|
| @act.do not approve _ _ | Allows a ticket to be processed without approval. |
| @act.choose approve template _ _ | Specifies an approval template. |
| @act.choose approve template with reason _ _ _ _ | Specifies an approval template with a reason provided. |
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. |
| @act.enable check permission _ _ | Validates the permissions of an applicant on involved databases and tables. |
| @act.disable check permission _ _ | Does not validate the permissions of an applicant on involved databases and tables. |
| @act.enable check sec column _ _ _ | Validates the permissions of an applicant on involved sensitive fields. |
| @act.disable check sec column _ _ _ | Does not validate the permissions of an applicant on involved sensitive fields. |

#### 11.9.9 Schema design

DMS allows you to configure security rules on the Schema Design tab to check the design rules and risk identification rules that apply to schema design tickets. This helps ensure data security. Basic configuration items

| Configuration item | Description |
|---|---|
| Enable non-peer Publishing | Specifies whether to enable non-peer publishing. By default, data changes to a table can be published only to a table with the same name in another database. After you enable non-peer publishing, you can perform data changes on all tables. Warning This feature may bring high risks. We recommend that you proceed with caution and enable this feature only for special requirements. |
| R & D process | The whole process of a schema design ticket. It is the most important configuration item on the Schema Design tab. For more information about the parameters of the configuration item, see Parameters involved in the R&D process. |

| Configuration item | Description |
|---|---|
| Field t ype conf igurat ion | The supported data types of fields to be added. |
| Index t ype conf igurat ion | The supported data types of indexes to be added. |
| It is f orbidden t o modif y t he original f ield dat a t ype | Specifies whether to prohibit the data types of the original fields from being modified when the original table is to be modified. |
| Prohibit delet ing original f ields | Specifies whether to prohibit the existing fields from being deleted when the original table is to be modified. Not e We recommend that you enable this feature because deleting existing fields may bring high risks. |
| Prohibit renaming original f ields | Specifies whether to prohibit the existing fields from being renamed when the original table is to be modified. Not e We recommend that you enable this feature because reaming existing fields may bring high risks. |
| T able charact er set license conf igurat ion | The range of character sets that are allowed to be used when you create a table. For example, you can specify utf8 and utf8mb4. |
| Def ault approval t emplat e f or St ruct ural design | The default approval template that is used for a schema design ticket if you do not configure the Approval Rule Validation checkpoint. In the Switch Approval Template dialog box, you can change the approval process of the default approval template. |
| When published, t he t icket will aut omat ically advance t o t he end st at e | The point that is used to stop the schema change process. If you enable this feature, after the node that is set as the anchor in the R&D process is run, DMS automatically turns the ticket to the Finished state. Not e To use this feature, you must set the last node in the R&D process as the anchor. |

Supported checkpoints

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

The Schema Design tab contains the following two processes: Process of saving changes: DMS provides the following three checkpoints for this process. The checkpoints validate the table headings, fields, and indexes. Save Changes and Validat e Header Save Changes and Validat e Field Save Changes and Validat e Index Process of applying changes: DMS provides the following five checkpoints for this process. The first four checkpoints identify the risks that arise from changing schemas without locking tables, and the last checkpoint assigns an approval process to each type of risk. T able Creat ion Risk Cont rol Field Change Risk Cont rol Index Change Risk Cont rol SQL Execut ion Risk Cont rol Approval Rule Validat ion Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Schema Design tab.

| Factor | Description |
|---|---|
| @fac.table kind _ | The type of the table whose schema is to be changed. Valid values: new: a newly created table. old: an existing table. |
| @fac.column kind _ | The type of the field to be changed. Valid values: new: a newly created field. old: an existing field. |
| @fac.xxxx old _ | The value of an existing field or index that is used for comparison. |
| @fac.column is primary _ _ | A Boolean value that indicates whether the current field serves as a primary key. Valid values: true and false. |
| @fac.column type support defa _ _ _ ult | A Boolean value that indicates whether the data type of the current field supports a default value. Valid values: true and false. Not e For example, a field of the CHAR type supports a default value, whereas a field of the TEXT type does not. |
| @fac.index kind _ | The type of the index to be changed. Valid values: new: a newly created index. old: an existing index. |
| @fac.index column count _ _ | The number of fields in the index. |

| Factor | Description |
|---|---|
| @fac.change type _ | The type of the schema change to be performed by DDL statements. Valid values: add: adds one or more fields or indexes. modify: modifies one or more fields or indexes. delete: deletes one or more fields or indexes. |
| @fac.altered table size _ _ | The size of the table whose schema is to be changed. Unit: MB. |
| @fac.online execute _ | A Boolean value that indicates whether the schema change can be performed in an online environment. Valid values: true and false. |
| @fac.change risk level _ _ | The risk level of the schema change. Valid values: high: a high risk level. middle: a medium risk level. low: a low risk level. |
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Schema Design tab.

| Action | Description | Format |
|---|---|---|
| @act.block submit _ | Blocks the submission of the schema change and displays the error message. This action can be used in the process of saving changes. | @act.block submit 'Reason for _ blocking the submission' |
| @act.show warning _ | Displays the error message without blocking the submission of the schema change. This action can be used in the process of saving changes. | @act.show warning 'Error _ message' |
| @act.mark middle risk _ _ | Specifies that the schema change is at medium risk. This action can be used in the process of identifying the risk level. | @act.mark middle risk 'Reason _ _ for the identification' |
| @act.mark high risk _ _ | Specifies that the schema change is at high risk. This action can be used in the process of identifying the risk level. | @act.mark high risk 'Reason for _ _ the identification' |

| U | ser Guide·System management |   | Data Managemen | t |
|---|---|---|---|---|

| Action | Description | Format |
|---|---|---|
| @act.forbid submit publish _ _ | Rejects the ticket. This action can be used in the process of setting the approval process. | @act.forbid submit publish _ _ 'Reason for the rejection' |
| @act.do not approve _ _ | Specifies the ID of an approval template. | N/A |
| @act.choose approve template _ _ |   |   |
| @act.choose approve template _ _ _ with reason _ |   |   |

Parameters involved in the R&D process

| Parameter | Description |
|---|---|
| St ep | The type of the node. Valid values: Design: The design node in the R&D process is generated by default and cannot be removed. It determines the environment where the schema change is designed. Publish: A publish node in the R&D process is used to publish the schema change after the change is designed. You can set multiple publish nodes. |
| Node Name | The name of the node. The node name can be up to 10 characters in length. |
| Dat abase Environment | The environment where the node is run. |
| Execut ion St rat egy | The way in which the node is run. Valid values: Immediat ely: The node is run immediately after it is approved. Periodically: The node is run at the time that you specify. Not e If a node is approved before the specified point in time, it is run as scheduled. Otherwise, the node is interrupted and not run. |
| Can Go Back | Specifies whether a publish node can be rolled back to the design node. |
| Can Skip | Specifies whether the current node can be skipped. |
| Anchor | The point that is used to stop the schema change process. If you set a node as the anchor, after the node is published, the nodes that follow the anchor cannot be run and the schema change process ends. At this time, the ticket enters the Published state. |
| Act ions | The operation that you can perform on a publish node. You can remove a publish node as required. |

#### 11.9.10 Database and table synchronization

DMS allows you to configure security rules on the Table Sync tab to validate operations that are related to schema synchronization, empty database initialization, and table consistency repair. Basic configuration items

| Configuration item | Description |
|---|---|
| Enable execut ion capabilit y | Specifies whether to enable SQL-based synchronization. If this configuration item is set to OFF, applicants can compare table schemas but cannot execute SQL statements to synchronize databases and tables. Other configuration items and security rules you set under checkpoints on the Table Sync tab also become invalid. |
| Dat abase t able synchronizat ion def ault approval T emplat e | The default approval template for database and table synchronization applications. You can use the default approval template or click Switch Approval Template and select another template. For more information, see Customize approval processes. |
| Analysis phase script Expirat ion T ime (unit : hours) | The timeout period of the analysis phase. You can set an appropriate timeout period in which synchronization can be canceled if schemas are changed in the destination database. |

Supported checkpoints The Table Sync tab contains three checkpoints that are corresponding to the three features that are supported by the tab. The three checkpoints are unrelated to each other. For example, when you submit a Schema Synchronization ticket, only the basic configuration items and the security rules that are specified under the Schema Synchronization Validation checkpoint are used to validate the ticket.

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

| Checkpoint | Description |
|---|---|
| Schema Synchronizat ion Validat ion | Allows you to set approval processes or constraints for Schema Synchronization tickets. |
| Empt y Dat abase Init ializat ion Validat ion | Allows you to set approval processes or constraints for Empty Database Initialization tickets. |
| T able Consist ency Repair Validat ion | Allows you to set approval processes or constraints for Repair Table Consistency tickets. |

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Table Sync tab.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.schema name _ | The name of the schema. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Table Sync tab.

| Action | Description |
|---|---|
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. The statement is in the following format: @act.forbid submit order 'Reason for _ _ forbidding the submission of the ticket' . |
| @act.do not approve _ _ | Specifies the ID of an approval template. |
| @act.choose approve template _ _ |   |
| @act.choose approve template with reason _ _ _ _ |   |

|   |   | @act.forbid submit order 'Reason for _ _ |
|---|---|---|
|   | forbidding the submission of the ticket' |   |

#### 11.9.11 Sensitive field change

The topic describes the security rules on the Sensitive Column Change tab. Basic configuration items Sensit ive column def ault approval T emplat e: the default approval template that takes effect if you do not set approval processes for tickets that apply to change the security levels of sensitive fields under the Approval Rule Validation checkpoint. In the Switch Approval Template dialog box, you can change the approval process of the default approval template. Supported checkpoints Approval Rule Validat ion: When a user submits a ticket to change the security level of a sensitive field, DMS checks whether the ticket conforms to the rules that are specified under the Approval Rule Validation checkpoint.

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Sensitive Column Change tab.

| Factor | Description |
|---|---|
| @fac.column level change type _ _ _ | The type of security level change that the applicant wants to perform on a sensitive field. Valid values: upper: raises the current security level, including the following three cases: From inner to sensitive From inner to confidential From sensitive to confidential sensitiveto inner: lowers the security level from sensitive to inner. _ _ confidentialto sensitive: lowers the security level from confidential _ _ to sensitive. confidentialto inner: lowers the security level from confidential to _ _ inner. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Sensitive Column Change tab.

| Action | Description |
|---|---|
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. The statement is in the following format: @act.forbid submit order 'Reason for _ _ forbidding the submission of the ticket' . |
| @act.do not approve _ _ | Specifies the ID of an approval template. |
| @act.choose approve template _ _ |   |
| @act.choose approve template with reason _ _ _ _ |   |

|   |   | @act.forbid submit order 'Reason for _ _ |
|---|---|---|
|   | forbidding the submission of the ticket' |   |

#### 11.9.12 Test data generation

This topic describes the security rules on the Test Data Generate tab. Supported checkpoints Approval rule validat ion: When a user submits a ticket to generate test data, DMS checks whether the ticket conforms to the rules that are specified under the Approval rule validation checkpoint.

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

Supported factors A factor is a built-in variable in DMS. You can use factors to obtain the context to be validated by security rules, such as SQL statement categories and the number of rows to be affected. A factor name starts with the prefix `@fac.` .The following table describes the supported factors on the Test Data Generate tab.

| Factor | Description |
|---|---|
| @fac.env type _ | The type of the environment. The value is the display name of the environment type, such as DEV or PRODUCT. |
| @fac.schema name _ | The name of the schema. |

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Test Data Generate tab.

| Action | Description |
|---|---|
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. The statement is in the following format: @act.forbid submit order 'Reason for _ _ forbidding the submission of the ticket' . |
| @act.do not approve _ _ | Specifies the ID of an approval template. |
| @act.choose approve template _ _ |   |
| @act.choose approve template with reason _ _ _ _ |   |

|   |   | @act.forbid submit order 'Reason for _ _ |
|---|---|---|
|   | forbidding the submission of the ticket' |   |

#### 11.9.13 Database cloning

This topic describes the security rules on the Database Clone tab. Basic configuration items Dat abase clone def ault approval T emplat e: the default approval template that takes effect if you do not set approval processes for database clone tickets under the Approval rule validation checkpoint. In the Switch Approval Template dialog box, you can change the approval process of the default approval template. Supported checkpoints Approval rule validat ion: When a user submits a database clone ticket, DMS checks whether the ticket conforms to the rules that are specified under the Approval rule validation checkpoint.

> Not e Various security rule templates are built in each checkpoint. You can configure security rules based on these templates or create custom security rules as needed.

Supported actions An action in a security rule is an operation that DMS performs when the if condition in the rule is met. For example, DMS can forbid the submission of a ticket, approve a ticket, or reject a ticket. An action in a security rule denotes the purpose of the security rule. An action name starts with the prefix `@act.` .The following table describes the supported actions on the Database Clone tab.

| Action | Description |
|---|---|
| @act.forbid submit order _ _ | Forbids a ticket from being submitted. The statement is in the following format: @act.forbid submit order 'Reason for _ _ forbidding the submission of the ticket' . |
| @act.do not approve _ _ | Specifies the ID of an approval template. |
| @act.choose approve template _ _ |   |
| @act.choose approve template with reason _ _ _ _ |   |

|   |   | @act.forbid submit order 'Reason for _ _ |
|---|---|---|
|   | forbidding the submission of the ticket' |   |
