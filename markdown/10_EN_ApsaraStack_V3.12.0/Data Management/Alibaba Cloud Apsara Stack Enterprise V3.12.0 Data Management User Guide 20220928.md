---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Management User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 39
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Management User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Data%20Management%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Management User Guide 20220928

## Table of Contents

- 1 What is Data Management?
- 2 Log on to an ApsaraDB for RDS instance by using DMS
- 3 SQL operations
  - 3.1 Use the command window
  - 3.2 Use the SQL window
    - 3.2.1 Open an empty SQL window
    - 3.2.2 Restore a saved SQL window
    - 3.2.3 Manage common SQL statements
    - 3.2.4 Use the SQL template
  - 3.3 Table operations (based on the Table directory tree)
    - 3.3.1 Open a table-based SQL window
    - 3.3.2 Edit table data
- 4 Database development
  - 4.1 Overview
  - 4.2 Table
    - 4.2.1 Create a table
    - 4.2.2 Edit a table
    - 4.2.3 Delete a table
    - 4.2.4 Duplicate a table
    - 4.2.5 Generate SQL statement templates
    - 4.2.6 Query table information
    - 4.2.7 Clear data
    - 4.2.8 Perform operations on multiple tables
    - 4.2.9 Maintain a table
  - 4.3 Manage indexes
  - 4.4 Manage foreign keys
  - 4.5 Create a partition
  - 4.6 Create a stored procedure
  - 4.7 Create a function
  - 4.8 Create a view
  - 4.9 Create a trigger
  - 4.10 Create an event
- 5 Data processing
  - 5.1 Import data
  - 5.2 Export data
    - 5.2.1 Export a database
    - 5.2.2 Export an SQL result set
- 6 Performance
  - 6.1 Lock wait
    - 6.1.1 View sessions in the lock wait state
    - 6.1.2 Terminate a session in the lock wait state
- 7 Extended tools
  - 7.1 View statistics on table data volumes
  - 7.2 View ER diagrams

nt?

## 1 What is Data Management?

Data Management (DMS) is an integrated database solution that provides data, schema, and server management, access control, business intelligence (BI) insights, data trend analysis, data tracking, and performance optimization. Supported database types ApsaraDB RDS for MySQL ApsaraDB RDS for SQL Server PolarDB and ApsaraDB RDS for PostgreSQL Supported database operations Use of SQL windows Use of the command window Saving of work environment settings SQL statement execution SQL statement optimization SQL statement formatting and improvement Viewing of execution plans Smart SQL completion Operations on database objects Operations on data tables Operations on schemas: modify schemas by adding or deleting columns, indexes, foreign keys, and partitions Changes to table data: insert, update, and delete Table data query and visualized editing Operations on views and programmable objects such as functions, stored procedures, triggers, and events Creation Modification Deletion Enabling and disabling Data import Data export Performance and diagnosis Lock wait analysis Use of data processing tools Drawing of entity-relationship (ER) diagrams nt? Statistics on table data volume Batch operations on tables User-friendly interactions DMS provides user-friendly tips. When an error occurs, DMS displays suggestions on how best to achieve your goal. or RDS instance by using DMS

## 2 Log on to an ApsaraDB for RDS instance by using DMS

RDS instance by using DMS This topic describes how to log on to an ApsaraDB for RDS instance by using DMS. The ApsaraDB for RDS console allows you to log on to ApsaraDB for RDS instances by using DMS. You can use DMS to manage database data and schemas.
1. Log on to the ApsaraDB for RDS console. For more information, see the Log on to the ApsaraDB for
RDS console topic in ApsaraDB for RDS User Guide.
2. In the left-side navigation pane, click Instances. On the Instances page, find the target instance.
Click the instance ID or click Manage in the Act ions column.
3. On the page that appears, click Log On t o DB to go to the logon page of the DMS console.
4. Enter the logon information.

| Paramet er | Description |
|---|---|
| IP address :Port | The internal or public endpoint and corresponding port number of the target ApsaraDB for RDS instance. Example: rm-txxxxxxxxxxxxxxxx.mysql.aliyun-inc.com:3306 . To obtain the internal or public endpoint and the port number, perform the following steps: i. Log on to the ApsaraDB for RDS console. ii. Go to the Instances page, find the target instance, and then click the instance ID or click Manage in the Act ions column. iii. In the Basic Inf ormat ion section of the page that appears, obtain the endpoint and port number. |
| Dat aba se Userna me | The account used to connect to the ApsaraDB for RDS instance. Not e The account is created in the ApsaraDB for RDS instance. |
| Ent er your passwo rd | The password of the account used to connect to the ApsaraDB for RDS instance. Not e The password is that you specified when you create the account in the ApsaraDB for RDS instance. |

5. Click Login.
Not e If you want the browser to remember the password, select Remember your password and then click Login.

## 3 SQL operations

### 3.1 Use the command window

This topic describes how to use the command window in DMS. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose SQL Operat ions > Command Window.
An empty command window appears, as shown in Command window. Command window
3. Enter an SQL statement in the command window, and then click execut e, as shown in Execution of
an SQL statement. Execution of an SQL statement The following table describes the numbered items in the command window. Numbered items in the command window

| No. | Name | Description |
|---|---|---|
| 1 | Command window | The area displays execution results of SQL statements. |
| 2 | SQL statement input area | You can enter SQL statements in this area. |
| 3 | execute button | You can click this button to execute the entered SQL statements. |
| 4 | Result display area | DMS appends execution results to the result display area. |
| 5 | Up and down arrows | You can click the up or down arrow to view an executed SQL statement and execute it again. |

4. (Optional)If the execution process takes longer than expected, you can click Cancel to abort the
execution.
5. (Optional)Click Clear Screen to clear the results for proper display of subsequent results.
To switch to another database, select the new database from the Database drop-down list.

### 3.2 Use the SQL window

#### 3.2.1 Open an empty SQL window

This topic describes how to use SQL windows. A MySQL database is used in this example. A maximum of 20 SQL windows (including the homepage) can be opened in DMS. We recommend that you open no more than five SQL windows at a time.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose SQL Operat ions > SQL Window to open the SQL Window tab.
Empty SQL window shows the empty SQL window you opened. Empty SQL window describes the numbered items in the SQL window. Numbered items in the SQL window

| No. | Name | Description |
|---|---|---|
| 1 | SQL window | The green-framed area is the main body of the SQL window. |
| 2 | execut e(F8) but t on | You can click this button to execute the entered SQL statements. |
| 3 | SQL Diagnost ics button | You can click this button to diagnose the current SQL statements. |
| 4 | Format button | You can click this button to format the entered SQL statements for readability. |
| 5 | Plan button | You can click this button to display the execution plans of the selected SQL statements. You can optimize the SQL statements and improve SQL processing performance based on the execution plans. |

3. Enter the SQL statement that you want to execute and click execut e(F8) to complete the SQL
query or update, as shown in Execute SQL statements.. Execute SQL statements.
4. You can view the result set, as shown in View the result set.
View the result set Numbered items in the result set

| No. | Description |
|---|---|
| 1 | The Result Set tab displays the results returned by the SQL query statement. |
| 2 | The first row of the table shows the column names. If an alias has been specified for a column in the SQL statement, the alias is displayed in this table. |
| 3 | The data area of the table displays the queried data in rows. If the data area is not big enough to show all of the queried data, horizontal and vertical scroll bars will appear to help you navigate the result set. |
| 4 | You can set Current Page or Per Page to view the result set. Each page displays 100 data entries by default. Go to the next page to view more data. You can set the number of data entries displayed per page as needed. The obtained data entries on the next page are displayed in the dat a area numbered 3 in the figure. |

| No. | Description |
|---|---|
| 5 | You can view the progress of data acquisition and time elapsed. |

5. View the SQL execution message.
Each time a data query (SELECT) or data correction (INSERT, UPDATE, or DELETE) statement is executed, DMS returns a message about the execution including the status and impact. Data query shows the message returned for data query. Data query Data correction shows the message returned for data correction. Data correction describes the numbered items in the data correction window. Numbered items in the data correction window

| No. | Description |
|---|---|

| No. | Description |
|---|---|
| 1 | After you execute an SQL statement, you can click the Messages tab to view the execution status. No result set is returned for data correction. DMS displays a message after data correction has been completed. |
| 2 | DMS executes the entered SQL statements step by step: Analyzes the entered SQL statements. Executes the SQL statements in the database. Displays the queried data. Displays statistics, including the number of data rows that are queried or affected. |
| 3 | DMS displays the SQL execution results: Whether the execution is successful. Number of queried rows, or number of rows affected by the Add, Delete, or Modify operation. The amount of time consumed to execute the SQL statements. |

6. Execute SQL statements in batches.
DMS supports batch execution of SQL statements, as shown in Batch execution. Batch execution 1: Displays the execution result of the first SQL statement. 2: Displays the execution result of the second SQL statement. i. Separate each SQL statement with a semicolon (;) or another separator. ii. To execute only some SQL statements, select the SQL statements that you want to execute. To execute all SQL statements, deselect or select all SQL statements, and click execut e(F8). Wait until all SQL statements have been executed. iii. View the execution results. If you execute the SELECT statement, DMS displays the result set. If you execute other statements, DMS displays the execution results, such as the number of affected rows.
7. Click Row Det ails to view the details of a single entry in the result set, as shown in Row details.
Row details The following table describes the numbered items in the Row Det ails dialog box. Numbered items in the Row Details dialog box

| No. | Description |
|---|---|
| 1 | On the Result Set tab, select a single data entry that you want to display, and click Row Det ails to view details of the entry. The Row Det ails dialog box displays the name, value, and type of each column of the data entry. |
| 2 | Column Name: If you have specified an alias for a column, the alias is displayed. |
| 3 | Value: DMS automatically parses and displays the column values. Data such as time and binary code is formatted as a string to ease reading. |
| 4 | Type: You can view the type and length of each column. |
| 5 | The navigation area. You can click Previous Row, Next Row, First Row, and Last Row to view the details of the corresponding data entry. |

8. (Optional)Edit the queried data in the result set.
Click New to add a row of data to the currently queried table. Click Delet e to delete the selected row of data from the result set table. Select the row that you want to perform operations on. Update the column values in the selected row directly. After you modify data, click Submit Change to save the modified data to the database. After you click Submit Change, DMS displays the SQL statements required to save your changes. This allows you to confirm the changes and prevent misoperations that can result in data loss. Click OK to apply the changes to the database as expected.
9. Click Format to format the selected SQL statements to make them easier to read and write.
Only the selected SQL statements are formatted. If you do not select any SQL statements, all entered SQL statements will be formatted. This feature transforms your SQL statements into standard, easy-to-read statements without changing the SQL execution logic and syntax or affecting the execution. Example: Original SQL statements shows the original SQL statements. Original SQL statements Formatted SQL statements shows the formatted SQL statements. Formatted SQL statements
10. Click Plan to view the execution plan if you want to troubleshoot SQL-related problems or
optimize SQL performance. After you click Plan, DMS displays the execution plan of the selected SQL statement. If no SQL statement is selected, DMS displays the execution plans of all SQL statements. DMS displays an execution plan in detail. You can view information such as the execution plan type and possible keys. Different databases display execution plans in different ways and in varying levels of detail. If you want to view the execution plans of several SQL statements, DMS displays the execution plan of each SQL statement in detail on different tabs, as shown in Plan. Plan 1: Shows the execution plan of the first SQL statement in detail. 2: Shows the execution plan of the second SQL statement in detail.

#### 3.2.2 Restore a saved SQL window

This topic describes how to restore a saved SQL window. A MySQL database is used in this example. A maximum of 20 SQL windows (including the homepage) can be opened or stored in DMS. We recommend that you open no more than five SQL windows at a time.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose SQL Operat ions > SQL Window.
3. Save the current SQL work environment.
DMS automatically saves the work environment when you close the operation page. The next time that you log on to the DMS console, DMS automatically restores the last saved work environment, including the last used database, the open SQL windows, and the SQL statements entered in the SQL windows. When you close a SQL window, DMS prompts you to confirm whether to save the content of the window, as shown in Confirm to close a SQL window. Confirm to close a SQL window 1: Click the Close icon in the upper-right corner of the SQL window to close the window. 2: DMS prompts you to confirm whether to save the content. Click Save and Close SQL. DMS saves the content of the SQL window before it is closed. If you click Close Now, DMS does not save the content of the SQL window.
4. Restore a saved SQL window.
i. Choose SQL Operat ions > Saved SQL Windows. DMS displays all saved SQL windows. ii. Click View SQL next to a saved SQL window to restore the SQL window. iii. When you log on to the database through DMS, DMS automatically restores the most recently saved content of the SQL window, as shown in Restored SQL window. Restored SQL window

#### 3.2.3 Manage common SQL statements

This topic describes how to manage common SQL statements in DMS. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose SQL Operat ions > SQL Window to open the SQL Window tab.
3. Perform the following operations:
Add a common SQL statement. Choose My SQL Script s > Add SQL to add a common SQL statement. The applicable scope is described as follows: Current Instance: You can only view the custom SQL statement through the instance (with the specified IP address and port number) that is currently connected to. Current Database: You can only view the custom SQL statement through the database that is currently connected to. If you switch the current database to another one, you cannot view the custom SQL statement by choosing My SQL Script s > Select SQL. View saved SQL statements. To view saved SQL statements, choose My SQL Script s > Select SQL. Manage SQL statements. To manage your SQL statements, choose My SQL Script s > Manage SQL. In the Manage SQL dialog box that appears, click Edit or Delet e to edit or delete SQL statements. In the Manage SQL dialog box, click New to add an SQL statement. Double-click an SQL statement to insert the statement into SQL Window. The statement appears in the SQL window and is selected.

#### 3.2.4 Use the SQL template

This topic describes how to use the SQL template in DMS.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose SQL Operat ions > SQL Window. A SQL window appears.
The SQL template is displayed in the rightmost part of the SQL window.
3. Double-click an SQL command or drag it into the SQL window. Then you can use or reference the
command. You can directly modify the commands referenced from the template even if you are not familiar with the commands.

### 3.3 Table operations (based on the Table directory tree)

Table directory tree)

#### 3.3.1 Open a table-based SQL window

This topic describes how to open a table-based SQL window in DMS. A MySQL database is used as an example.
1. Log on to an RDS instance through DMS.
2. In the left-side directory tree, right-click a table and choose SQL Operat ion Dat a from the
shortcut menu to open an SQL window. DMS automatically runs the SQL statement that queries top 50 records of the table.

#### 3.3.2 Edit table data

This topic describes how to edit table data. An ApsaraDB RDS for MySQL database is used in this example. This feature applies to tables with a small volume of data. For tables containing a large volume of data, you must find the target data before you can edit the data. It may take time to find the data to be edited.
1. Log on to an RDS instance through DMS.
2. In the left-side navigation pane, right-click a table and select Open T able.
A tab appears on the right, displaying the data of the selected table, as shown in Table tab. Table tab 1: Right-click a table and select Open T able. 2: Modify the values of the columns in the table. 3: Click Submit Change to submit the modified data.

## 4 Database development

### 4.1 Overview

This topic describes how to add, modify, delete, and manage objects such as indexes, foreign keys, and stored procedures.

### 4.2 Table

#### 4.2.1 Create a table

This topic describes how to create a table in DMS.
1. Log on to an RDS instance through DMS.
2. You can create a table in one of the following ways:
In the top navigation bar, choose Creat e > T able. In the left-side navigation pane, click T able, right-click a table, and then select Creat e T able.
3. Edit columns.
On the New: T able tab, the Edit Column tab appears by default. You can edit the basic information and extended information about the fields as needed. You can also click Columns to edit the table information.
4. Click Index to edit indexes.
Click New to add an index. Click Remove to delete an index. Click the index row to modify index information.
5. Click Foreign Key to go to the Edit Foreign Key tab.
Click New to add a foreign key. The new key is editable. Click Remove to delete a foreign key. To edit a foreign key, enter the key name, column name, and information about the referenced database, table, and column.
6. Click Part it ion to edit the partition information. The SQL statements of the partition must be
configured.
7. Click Basic to edit the basic information about the table.
You can edit the table name, storage engine, character set, and description. You can click Advanced to edit table parameters.
8. Click Save. DMS generates the SQL statements used to create a table.
In the Submit Change dialog box, click OK after you confirm the SQL statements. DMS then adds the table to your database.

#### 4.2.2 Edit a table

This topic describes how to edit a table in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click a table and choose Edit T able St ruct ure from the
shortcut menu to edit the table structure.
3. The Edit Table window is similar to the Create Table window. DMS automatically loads the table
structure into the window. 1: Select a table object type, such as Columns or Index. 2: Click a specific operation on the table object, which is similar to the Create and Edit operations on tables. 3: Click Open T able to view and modify table data. 4: Click Creat e to view the statements used to create a table.
4. Click Save. DMS displays the SQL statements used to modify the table structure.
Click OK after you confirm the SQL statements. DMS then saves the modified table structure to your database.

#### 4.2.3 Delete a table

This topic describes how to delete a table in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table you want to delete and choose Delet e
T able from the shortcut menu.

> **Warning:** Deleting tables is a high-risk operation. Therefore, exercise caution when deleting tables.

3. Click Yes to delete the table.

#### 4.2.4 Duplicate a table

This topic describes how to duplicate a table in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side navigation pane, click T able, right-click the table that you want to duplicate, and
then choose T o Duplicat e T able from the shortcut menu. The dialog box to enter the name of the destination table appears.
3. Enter the name of the destination table and then click OK. DMS duplicates the selected table.
4. The schema of the created destination table is the same as that of the selected source table.
A new table is created, as shown in Schema of the destination table. Schema of the destination table

#### 4.2.5 Generate SQL statement templates

This topic describes how to generate SQL templates in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table you want to copy and choose Creat e
SQL T emplat e from the shortcut menu.
3. DMS generates SQL INSERT, UPDATE, SELECT and CREATE TABLE statement templates as a
reference when you perform SQL operations.

#### 4.2.6 Query table information

This topic describes how to query table information in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table you want to query and choose Object
Inf o from the shortcut menu.
3. DMS obtains information about the table object. Click the Basic Inf o tab to view basic information
of the table.
4. Click the Creat e St at ement tab to view the table creation statements.

#### 4.2.7 Clear data

This topic describes how to clear table data in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table that you want to clear data from and
choose Clear T able from the shortcut menu. Not ice Clearing table data is a high-risk operation and may affect your data usage. DMS prompts you to confirm whether to clear table data.
3. Click Yes if you want to clear table data. DMS then clears data of the selected table.
4. Open the table to check whether its data is cleared.

#### 4.2.8 Perform operations on multiple tables

This topic describes how to perform operations on multiple tables in DMS.
1. Log on to an RDS instance through DMS.
2. Delete multiple tables at a time.
i. In the left-side navigation pane, click T able, right-click a table name, and then choose Bat ch Operat ions > Drop Bat ch T ables. The dialog box for you to select multiple tables to delete appears. ii. Select the tables to be deleted. iii. Click OK. DMS prompts you to confirm whether you want to perform the batch operation. iv. Click Drop. DMS deletes the selected tables at a time.
3. Perform other operations on multiple tables.
You can clear data, delete or maintain tables, and modify table name prefixes in batches. i. In the left-side navigation pane, click T able, right-click a table name, and then choose Bat ch Operat ions > More. ii. Select multiple tables and then perform a batch operation. For example, click T runcat e Dat a. iii. In the Inf ormat ion dialog box that appears, click Yes. DMS performs the batch operation.

#### 4.2.9 Maintain a table

This topic describes how to maintain and optimize a table in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table you want to maintain and choose
Maint ain T able > Opt imize T able.
3. Click Yes.
Click Yes if you want to optimize the table. Then DMS starts optimization. Optimization allows you to reuse the table space in the database and organize file fragments. Not e You can check, restore, and analyze tables in a way similar to optimizing tables.

### 4.3 Manage indexes

This topic describes how to add, modify, or delete indexes in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, expand the table you want to modify and choose Index >
Add Index. The Add Index page appears.
3. Set index parameters.
1: Enter an index name and select an index type. 2: Click + or － to add or delete a field to or from the index. 3: Edit the fields of the index. You can enter or select values from the drop-down list. You can set a prefix length for a variable-length field (such as varchar) to save space occupied by the index.
4. Click Save.
DMS generates SQL statements used to add the index. Confirm the change.
5. Click Run.
6. After the index is added, check the indexes of the table to verify that the new index takes effect.
You can modify or delete the new index as needed. In the left-side Table directory tree, right-click an index and choose Modif y Index from the shortcut menu. The Modif y Index window appears. The method of modifying an index is similar to that of adding one, except that the SQL statements delete the old index before adding a new one. In the left-side Table directory tree, right-click an index and choose Delet e Index from the shortcut menu. The Delet e Index window appears. Click OK to delete the index.

### 4.4 Manage foreign keys

This topic describes how to add foreign keys in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side T able directory tree, right-click the table to be modified and choose Edit T able
St ruct ure from the shortcut menu.
3. On the Edit T able page that appears, click the Foreign Key tab to edit foreign keys.
4. Enter the foreign key information, and set the fields of foreign keys and referenced tables.
5. Click Save.

### 4.5 Create a partition

This topic describes how to create partitions in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side navigation page, click T able, right-click a table name, and then choose Creat e
T able from the shortcut menu.
3. Enter the basic table information and set the table fields and partition information.
4. Click Save to save the created table schema.
A dialog box appears to prompt you to confirm the SQL statements used to create the table.
5. Click OK. DMS creates the partitioned table based on the configured partition fields and
partitioning logic.
6. After you execute the SQL statements, check whether the partitioned table has been created.

### 4.6 Create a stored procedure

This topic describes how to create and manage stored procedures in DMS. A MySQL database is used as an example. Stored procedures, functions, triggers, and events are considered programmable objects in DMS.
1. Log on to an RDS instance through DMS.
2. Click the left-side Programmable Object directory tree, and choose St ored Procedure >
Creat e (St ored Procedure). The Create Stored Procedure tab is displayed.
3. Enter a name and a description for the stored procedure.
4. Click OK.
5. DMS provides a template for creating stored procedures. You only need to edit the stored
procedure part.
6. Click Save to save the stored procedure to the database.
If a syntax error is found, DMS returns the cause of the error.
7. Click Run to run the stored procedure.
DMS displays a page for you to set the input parameters for the stored procedure. Set the input parameters. In this example, set cnt to 80 to search for records that meet the Value=80 condition.
8. Click Execut e to execute the stored procedure.
DMS displays output parameters or intermediate result set of the stored procedure, if any. The Message tab displays messages about the execution, such as output variables and intermediate result sets. The Int ermediat e Result Set 1 tab displays the result set generated during the execution. If multiple intermediate result sets are available, DMS will generate multiple tabs, such as Intermediate Result Set 1, Intermediate Result Set 2, and Intermediate Result Set 3.
9. Click the Int ermediat e Result Set 1 tab.
DMS displays records with the value of 80.
10. You can set the options when creating the stored procedure. Click Opt ion Set t ings to set options
for the stored procedure.
11. After a stored procedure is created, it is added to the Programmable Object directory tree.
You can perform other operations related to the stored procedure through the following menu options: Create Edit Delete Execute
12. You can run the stored procedure in the SQL window.
1: Run the call stored_procedure_name command to call a stored procedure. 2: The SQL window shows the result set of the stored procedure, if any.

### 4.7 Create a function

This topic describes how to create a function in DMS. Functions, stored procedures, triggers, and events are considered programmable objects in DMS.
1. Log on to an RDS instance through DMS.
2. In the left-side Programmable Object directory tree, choose Funct ion > Creat e (Funct ion).
The Creat e Funct ion page is displayed.
3. Set basic information of the new function.
4. Click OK.
The Edit Function page appears. DMS generates a function creation template.
5. Enter information in the function part.
6. Click Save. DMS then checks whether the function is correctly defined. If not, DMS returns an error
message. DMS runs the correct function definition in your database, and returns a message, indicating that the function is saved.
7. Click Execut e to execute the function.
8. Enter a parameter such as wednesday and click Execut e to execute the function.
9. Click Opt ion Set t ings to set different options for the function.
You can also run the function in the SQL window.

### 4.8 Create a view

This topic describes how to create and manage custom views in DMS.
1. Log on to an RDS instance through DMS.
2. Click the View directory tree on the left side to check the views of the current database.
3. Right-click the blank space and choose New View from the shortcut menu.
The Creat e: View page is displayed.
4. Set basic information of the view.
The following example shows how to filter records in the dmstest table whose values are even numbers, and output the id and name fields.
5. Click Save Changes. DMS generates SQL statements used to create the view based on your
settings.
6. Click OK after you confirm the SQL statements. DMS saves the defined view to your database.
7. The saved view is added to the View directory tree on the left side. You can click the view to
display its definition. Check the view
8. Right-click View and choose Check View from the shortcut menu to query data through the newly
created view.
9. You can perform view-related operations in DMS.
The menu options include: View Data Create View Edit View Delete View Refresh Views

### 4.9 Create a trigger

This topic describes how to create and manage a trigger in DMS. Triggers, functions, stored procedures, and events are considered programmable objects in DMS.
1. Log on to an RDS instance through DMS.
2. Click the Programmable Object directory tree on the left side, and choose T rigger > Creat e
(T rigger). The Creat e: T rigger tab is displayed. 1: Trigger table. 2: Trigger settings. Enter a name for the trigger. Select dmstest from the drop-down list as the trigger table. Select AFTER from the drop-down list as the trigger time. Select INSERT from the drop-down list as the trigger event. 3: Set a trigger statement. Set the operations to be performed when the trigger event occurs. When data is inserted into the dmstest table, the trigger in this example inserts data into the copy_test table and records the insertion time in copy_test.time.
3. Click Save after you finish the trigger settings. DMS then generates the SQL statement to be
executed by the trigger based on your settings. Confirm the SQL statement.
4. Click OK. DMS then saves the trigger to your database. DMS returns a message, indicating that the
trigger has been saved. In the left-side navigation pane, choose Programmable Object > T rigger to view the trigger you created.
5. You can insert data into the dmstest table to check whether the data is recorded in the copy_test
table. 1: Insert data into the dmstest table and query the copy_test table for the inserted data. 2: The SQL window displays messages about the execution of the SQL statements. The messages indicate that a row is inserted into the dmstest table and that this row is also added to the copy_test table.
6. Check the result set in the SQL window to verify whether the insert operation is correctly performed
by the trigger.
7. In the left-side navigation pane, choose Programmable Object > T rigger to perform trigger-
related operations through the following menu options: Create (Trigger) Edit (Trigger) Delete (Trigger)

### 4.10 Create an event

This topic describes how to create and manage events in DMS. Prerequisites After you log on to a database, make sure that event support has been enabled for the database. Execute the SELECT @@event_scheduler; statement to check whether the database supports events. If ON is returned, event support is enabled. If OFF is returned, event support is disabled. You need to enable event support by modifying the configuration file or executing the SET GLOBAL event_scheduler = ON; statement. Events, triggers, functions, and stored procedures are considered programmable objects in DMS.
1. Log on to an RDS instance through DMS.
2. Click the Programmable Object directory tree on the left side, and choose Event > Creat e
(Event ). The Create Event page is displayed. 1: In the event setup area, set the event name, cycle, start time, end time, status, and comment, and choose whether to enable cyclic execution. 2: In the event execution Statement area, set the operations to be performed when a scheduled event is triggered.
3. Set an event trigger rule and the SQL statements for event execution.
4. Click Save. DMS generates the SQL statements used to create the event.
5. After you confirm that the SQL statements are correct, click OK. DMS then executes the edited
event in your database. If the event is created, DMS returns a message, indicating that the event is saved. In the left-side navigation pane, choose Programmable Object > Event to view the event you created.
6. Check whether the event is properly executed in the SQL window.
In this example, the event executes SQL statements to insert a piece of data into the copy_testtable every minute. Check the copy_test table to see whether the data is inserted as programmed.
7. You can perform various event-related operations in DMS.
The menu options include: Create (Event) Edit (Event) Delete (Event)

## 5 Data processing

### 5.1 Import data

This topic describes how to use DMS to import data. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose Dat a Operat ion > Import .
The Import tab appears, as shown in Import tab. Import tab The Import tab contains the import toolbar and import history. If you have imported data, you can view previous data import tasks in Hist ory.
3. Click New T ask.
The Import File dialog box appears, as shown in Import File dialog box. Import File dialog box Select the file type of the file to be imported. Currently, only SQL and CSV files are supported. If the data file uses a specific character set, you can manually specify the character set. By default, DMS detects the character sets used in a file. If an error occurs while an SQL statement is being executed, DMS will terminate the import task. You can select Ignore Error to proceed. However, this operation may affect subsequent operations. You can enter a brief description of the import task for later review.
4. Click St art to start the import task.
If the imported data has any error, DMS terminates the import process and returns an error message. You can modify the data file to correct the error and import it again. If the imported data and SQL statements are correct, DMS displays the import progress, volume of imported data, and time elapsed. After the import is complete, you can view the import task in Hist ory. Click a t ask ID to view the execution details of the task.

### 5.2 Export data

#### 5.2.1 Export a database

This topic describes how to use DMS to export a database. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose Dat a Operat ion > Export . The Export tab appears.
3. On the Export tab, choose New > Export Dat abase.
4. In the New dialog box that appears, select a database, a file type (SQL or CSV), and the content to
be exported (schema and data, only data, or only schema). Select tables on the right side, and select additional information in the Addit ional Inf ormat ion section.
5. Click OK.
6. In the Inf ormat ion dialog box that appears, click Yes. DMS then starts executing the export task.
DMS refreshes the export progress every two seconds. You can close the Export tab, and view and download the exported file in the export task list later. After the export is complete, DMS automatically downloads the exported file to your local computer. You can also click Download to download the exported file. You can view previously submitted export tasks in the export task list. You can click a task ID to view the task details, and can download the corresponding exported file.

#### 5.2.2 Export an SQL result set

This topic describes how to use DMS to export an SQL result set. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose Dat a Operat ion > Export . The Export tab appears.
3. On the Export tab, choose New > Export SQL result set s.
4. In the New dialog box that appears, complete the settings as needed.
Select a file type (CSV or SQL_Insert) and a database, set the maximum number of rows of the result set, and enter the SQL statements.
5. Click OK. DMS then executes the task of exporting the SQL result set in the background.
After the export task is complete, DMS automatically downloads the exported files to your local computer. You can also click Download to download the exported files. DMS also summarizes the export results and automatically downloads the files of exported SQL result sets. You can view the export tasks of SQL result sets that you submitted in the export task list and download SQL result set files.

## 6 Performance

### 6.1 Lock wait

#### 6.1.1 View sessions in the lock wait state

When a session of an ApsaraDB RDS for MySQL instance is waiting for a row exclusive lock held by another session, an InnoDB lock wait will occur. This topic describes how to use DMS to view sessions in the lock wait state. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose Perf ormance > InnoDB Lock Wait s.
If transactions of the current instance are waiting for locks, the Lock and Lock-Wait icons are displayed.
3. Move the pointer over the Lock or Lock-Wait icon to view the sessions that hold a lock or sessions
that are waiting for a lock, and related session IDs.
4. Click
to reload the data.

#### 6.1.2 Terminate a session in the lock wait state

This topic describes how to use DMS to terminate a session in the lock wait state. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose Perf ormance > InnoDB Lock Wait s.
If transactions of the current instance are waiting for locks, the Lock and Lock-Wait icons are displayed.
3. Move the pointer over the Lock or Lock-Wait icon to view the sessions that hold a lock or sessions
that are waiting for a lock, and related session IDs.
4. Click the Lock or Lock-Wait icon.
The Delet e Session message appears.
5. Click Yes to terminate the current session.
InnoDB Lock Waits tab shows the page when no transactions are waiting for locks. InnoDB Lock Waits tab

## 7 Extended tools

### 7.1 View statistics on table data volumes

volumes This topic describes how to view statistics on table data volumes in DMS. A MySQL database is used in this example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose T ools > T able Dat a Amount .
The T able Dat a Amount tab appears, as shown in Collection of statistics on table data volumes. Collection of statistics on table data volumes
3. This tab displays the information about all user tables of the current instance, including the
database name, table name, storage engine, number of rows, row size (in bytes), data, index, total table size, creation time, and collation rules. You can filter statistics on table data volumes based on a range of criteria such as database name, table name, total table size (in MB), number of table rows, global sorting, and storage engine. You can also perform the paging, refresh, and reset operations.

### 7.2 View ER diagrams

This topic describes how to view ER diagrams in DMS. This topic uses a MySQL database as an example.
1. Log on to an RDS instance through DMS.
2. In the top navigation bar, choose T ools > ER Diagram.
The ER Diagram tab appears, as shown in ER Diagram tab. ER Diagram tab The ER Diagram tab displays the relationship between tables in the current database and provides methods for representing table names, column names, indexes, and relationships.
3. You can perform the following operations:
Select a database from the DB:<Dat abase name> drop-down list to switch to the database. Select a value from the Order:<Sort ing opt ion> drop-down list. Tables can be sorted by table name or column count in ascending or descending order. Click Ref resh to refresh the current ER Diagram tab. Click View SQL Script s to view the SQL statements used to create tables in the current database. Click Download SQL Script s to download the SQL statements used to create tables in the current database. Click Download XML f iles to download the SQL statements used to create tables in the current database in XML format. Double-click the name of a table column to view the column definition. Double-click a table name to edit the table on a new tab.
