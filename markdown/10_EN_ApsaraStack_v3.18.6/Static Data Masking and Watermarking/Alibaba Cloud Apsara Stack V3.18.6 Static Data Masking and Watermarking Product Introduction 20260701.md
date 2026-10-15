---
title: "Static Data Masking and Watermarking Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 16
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Static Data Masking and Watermarking Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-%E6%95%B0%E6%8D%AE%E9%9D%99%E6%80%81%E8%84%B1%E6%95%8F%E4%B8%8E%E6%B0%B4%E5%8D%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Static%20Data%20Masking%20and%20Watermarking%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Static Data Masking and Watermarking Product Introduction 20260701

Static Data Masking and Waterm watermarking?

## What is static data

**desensitization and**

**watermarking?**

Data Desensitization Service (DMS) is a tool used by data managers to convert sensitive data in the original environment into fictitious data and then send it to the target environment. DMS retains the data characteristics required by the business in the target environment to ensure data security. DMS supports database-to-database, database-to-file, file-to-file, and file-to-database data desensitization tasks. Through intelligent sensitive data identification, DMS can provide users with sensitive data identification results, and users can manually adjust and intervene in the results. Based on the final sensitive data identification results, DMS provides a variety of sensitive data de-identification algorithms to convert user production data into de-identified data that can be used by third-party partners. This meets the data protection requirements of test, development, training, and data sharing scenarios. DMS is widely applicable to data-intensive and information-sensitive industries such as finance and carriers. It is also applicable to government departments and secret-related organizations. The product meets the policy compliance requirements of the financial industry, carrier industry, energy industry, and government departments for testing, development, and training environments.

| Feature categor y | Feature | Description |
|---|---|---|
| Data sources | Data source management | Allows you to add, modify, and remove data sources, including databases and files. |
| Data discover y | Sensitive data identification rules | Supports identification rules for sensitive data, including email addresses, Chinese addresses, Chinese names, mobile numbers, bank card numbers, ID card numbers, certificate numbers, names and organization names, military officer certificates, Exit-Entry Permits for Travelling to and from Hong Kong and Macao, Mainland Travel Permits for Hong Kong and Macao Residents, nationalities, landline numbers, enterprise organization names, unified social credit codes, taxpayer identification numbers, business units, organization codes, business registration numbers, amounts, dates, product codes, internal securities IDs, customs registration codes, IP addresses, MAC addresses, license plate numbers, vehicle identification numbers (VINs), International Mobile Equipment Identities (IMEIs), and mobile equipment identifiers (MEIDs). |
|  | Custom sensitive data identification rules | Supports custom identification rules for sensitive data in special formats. |
|  | Automatic discovery | Automatically scans and detects sensitive data in data sources based on sensitive data identification rules, and discovers the association between data. Discovers a field that is composed of multiple sensitive data entries. |
|  | Dictionary- based matching and discovery | Allows you to create sensitive data dictionaries. Discovers sensitive data based on sensitive data dictionaries. A dictionary contains: Fields Sensitive data samples |
|  | Field combination discovery | Identifies sensitive fields only if they are detected in the same table. |
|  | Sensitive field sorting | Allows you to modify and confirm automatically identified results. |

Static Data Masking and Waterm

## Functions and features

|  | Supported database types | Oracle 9i, 10g, 11g, and 12C SQL Server 2005, 2008, 2012, 2014, 2016, and 2017 MySQL, specific versions include: 5.1;5.6;5.7;6.5;8.0 DB2 LUW, including:9.x;10.x Sybase ASE, available in: 12.5;15.7 Sybase IQ , specific versions include: 15.4 Informix, specific versions include: 11.5;11.7;12.1ta; Teradata: 15.10.00.03 and 16.00.00.04 Vertica, specific versions include: 9.2 Redis, the specific version includes: 3.2.9 greenplum. Specific versions include: 6.4 Elasticsearch, the specific version includes: 6.8.6 ClickHouse 21.8 Cassandra 3.11.12 PostgreSQL 8.4, 9.2, 9.3, and 9.4 SAP Hana mariadb Dameng 7.1.6.33 GBase 8a KingbaseES 7.1.2.0598 release 64 bit SALES, V8R3, and V8R6 TiDB 5.7.25-TiDB-v4.0.4 Oscar 7.0.8.181104 MongoDB 4.4.3 GaussA (Gauss200), GaussT (Gauss100), and openGauss 3.0.0.0 SeaQL V2.5.6.1 TDSQL 5.7.35-V2.0 SequoiaDB 3.2 and 3.4.3 GoldenDB Hive 1.2.2 Spark 1.2.1.spark2 Kudu 1.5 and 1.9 HBase 1.2.0-cdh5.13.3 impala MaxCompute(ODPS) OceanBase in Oracle or MySQL mode AnalyticDB MySQL PolarDB Oracle syntax compatibility PolarDB PostgreSQL PolarDB-X MySQL DDM Generic JDBC |
|---|---|---|

Static Data Masking and Waterm

| Data masking |  |  |
|---|---|---|
|  | Supported file types | Supports file types such as TXT, CSV, Excel, HTML, XML, and DMP. |
|  | Masking algorithms | Provides built-in identification rules for sensitive data that meets specific characteristics, including ID card numbers, general certificate numbers, bank card numbers, mobile numbers, landline numbers, Chinese names, Chinese addresses, enterprise names, dates, taxpayer identification numbers, email addresses, amounts, unified social credit codes, organization codes, business registration numbers, securities codes, customs registration codes, IP addresses, MAC addresses, license plate numbers, VINs, military officer certificates, Exit-Entry Permits for Travelling to and from Hong Kong and Macao, Mainland Travel Permits for Hong Kong and Macao Residents, Mainland Travel Permits for Taiwan Residents, strings, numeric values, data dictionaries, bits, hash algorithms, and null. Supports different algorithms or mapping versions for the same masking algorithm. This ensures that different masking results can be obtained when different users select the same algorithm or algorithm parameters to mask the same raw data. |
|  | Masking methods | Supports different masking methods, including: Synonym replacement: replaces sensitive data with data that has the same meaning. For example, a name is still meaningful after it is masked, and a residential address is still valid after it is masked. Partial data masking: replaces part or all of the raw data with special characters such as an asterisk (*) or a number sign (#) to mask part or all of the data. Hybrid masking: masks data in related columns as a group to ensure that the masked data in these related columns maintains the same relationship. For example, the city, province, and postal code are consistent after masking. Deterministic masking: ensures that repeatable masked values are generated after data is masked. This ensures that the masked values of specific values such as customer numbers, ID card numbers, and bank card numbers remain the same in all databases. Field expression: uses masked fields to meet the operation requirements of other fields in a table. For example, the values of Masked Field 1 and Masked Field 2 are automatically summed and placed in Field 3. Grouping dictionary: replaces the data that is associated with a category with the data in the category and retains the replaced data in the same category. Custom function: uses custom discovery functions and custom masking functions to detect sensitive data with specific business requirements. |
|  | Masking of field combinations | Combined masking algorithm: masks two types of sensitive data in a column by using their respective algorithms. Hybrid masking algorithm: masks multiple types of sensitive data in a column by using their respective algorithms. |

Static Data Masking and Waterm

|  | Constraint and object preservation | Masks the constraints, associations, and objects such as triggers and indexes of a table to preserve them in the destination environment. |
|---|---|---|
|  | Masking solution management | Supports custom masking solutions. You can combine multiple masking policies of a scenario to create a masking solution that is suitable for the scenario. Custom masking solutions can be reused. |
|  | Data subset management | Allows you to mask specific data in a database. You can specify filter conditions to filter data in data sources and create data subsets. |
|  | Masking task management | Allows you to start and stop masking tasks, and supports concurrent tasks to make full use of system resources and improve masking efficiency. Exceptions are tolerated when masking tasks are running. If exceptions occur, abnormal data can be skipped and the tasks can continue to run. Masking tasks can also be automatically run at the scheduled time on a regular basis. |
|  | Scheduled tasks | Automatically runs masking tasks at the scheduled time on a regular basis. Tasks can be scheduled by date and time. |
|  | Queued tasks | Queues multiple masking tasks and automatically runs the queued tasks in a specific sequence. |
|  | Incremental data masking | Supports incremental data masking based on timestamps or incremental fields. |
|  | Data comparison | Allows you to query the data of a table to compare the data before and after masking. |
|  | Heterogeneous data masking | Supports heterogeneous data masking from MaxCompute to ApsaraDB RDS for MySQL. |
|  | Automated masking for remote file sources | Reads remote FTP files at regular intervals, automatically runs a sensitive data discovery task and a masking task based on the sensitive field template and masking solution template, and then automatically sends the generated data to the destination FTP file path. |
|  | Supported database types | Supports Oracle, SQL Server, MySQL, PostgreSQL, Dameng, KingbaseES, TiDB, Oscar, and MaxCompute. |
|  | Watermarking solutions | Supports custom watermarking solutions. You can use different watermarking algorithms, select field rules based on the watermarking algorithm, and then create a watermarking solution. Custom watermarking solutions can be reused. |

Static Data Masking and Waterm

| Data waterm arking |  |  |
|---|---|---|
|  | Data subset management | Allows you to watermark specific data in a database. You can filter data in data sources and create data subsets. |
|  | Watermarking task management | Allows you to create, run, stop, delete, and view watermarking tasks, and supports concurrent tasks to make full use of system resources and improve watermarking efficiency. Exceptions are tolerated when watermarking tasks are running. If exceptions occur, abnormal data can be skipped and the tasks can continue to run. |
|  | Pseudo-column watermarking algorithm | Allows you to insert a column that contains synthetic data into a table in a relational database. The data in the column is pseudo but is related to the raw data. The information about the extractable watermarking rule can be embedded in the inserted column. |
|  | Pseudo-row watermarking algorithm | Allows you to insert a row that contains synthetic data into a table in a relational database. The data in the row is pseudo but is of the same type as the raw data. The information about an extractable watermark rule can be embedded in the inserted row. |
|  | Space watermarking algorithm | Allows you to add spaces to data of the string type. The watermarked data is the same as the raw data except that it contains spaces. The information about an extractable watermark rule can be embedded together with spaces. |
|  | Masking and watermarking algorithms | Allows you to mask and watermark sensitive data in a relational database. The information about an extractable watermark rule can be embedded in the masked data. |
| Data provena nce | Provenance management | Allows you to trace the source of lost and leaked data, and find the organization where a data breach occurs and the data source information. |
|  | Pseudo column management | Allows you to configure and manage pseudo columns, such as adding pseudo column names and selecting pseudo column types. |
|  | Distribution object management | Allows you to manage distribution objects, including organization name, organization code, organization type, and organization level. |

Static Data Masking and Waterm Static Data Masking and Waterm fits

## Benefits

**Built-in efficient and extensive masking algorithms**

Static Data Masking and Watermarking (DMS) supports efficient data masking methods such as synonym replacement, partial data masking, hybrid masking, deterministic masking, and reversible data masking. It also supports data masking tasks from files to files, files to databases, databases to databases, and databases to files.

**Simple configuration and efficient data masking**

DMS provides automatic discovery, intelligent sorting, and built-in rules to free you from complex data masking tasks. You can configure masking policies with ease to manage data masking tasks. With a masking speed up to more than 50 GB per hour, DMS also provides resumable upload and automatic fault tolerance. It has been tested in numerous high-end scenarios with a scale of more than 10 TB.

**Comprehensive sensitive data management**

DMS divides a data masking process into four steps: discover sensitive data, sort sensitive data, formulate a masking solution, and run a data masking task. Combined with the comprehensive sensitive data dictionary management, data discovery algorithm management, and masking algorithm management modules, DMS implements comprehensive sensitivity data management.

**Flexible data masking task management**

DMS allows you to view the status of data masking tasks that are in progress and the list of data masking tasks that are run. DMS allows you to query historical records in the previous week, previous month, this month, last month, and the specified time range. DMS allows you to export data files with masked data, the run logs of data masking, and database DDL statements. Static Data Masking and Waterm

## Architecture

The following figure shows the product architecture: Data Source Target environment System Development /test Sensitive Data extraction Data Data output data discovery Database source Data analysis env Data source management Sensitive information feature management File Source Manage desensitization rules Data source management Research /teachin User permission management Data source management Static Data Masking and Waterm

## Common scenarios

**Development or testing**

In development or test scenarios, you must quickly build an environment. Traditionally, sensitive data is manually masked, which is inefficient and prone to omissions. The quality of masked data is unsatisfactory. In addition, the data masking process is uncontrollable. You may need to correct errors or mask missed data. In such scenarios, you can use data masking tools to improve the efficiency and performance of data masking.

**Data analysis**

The effectiveness of data analysis often depends on the quality of basic data, and the availability of basic data directly affects data analysis results and business decisions. During data masking, raw data is simulated without changing the association between data. This way, data analysis results can provide reference for subsequent operations.

**Data transmission**

As modern enterprises are increasingly collaborating with external organizations, they more frequently exchange files and data. This increases the risk of the leakage of important documents and data. In such scenarios, data transmission must be controlled. When you transmit sensitive data to low-security zones, you can mask the data to prevent the leakage of privacy data. Static Data Masking and Waterm s

## Limits

Static Data Masking and Watermarking (DMS) supports data masking for GoldenDB databases, SequoiaDB databases, and generic JDBC databases. For these database types, source schema masking and heterogeneous data masking are not supported. In source schema masking mode, filter conditions and expressions for data subsets as well as blacklists and whitelists are supported only if temporary tables are used. Other masking methods in source schema masking mode do not support the preceding features. In source schema masking mode, troubleshooting is optimized only for temporary tables. Troubleshooting is not optimized for other masking methods in source schema masking mode. Static Data Masking and Waterm s

## Terms

**database masking**: a feature that masks the data in a database and saves the masked
data in a database or as files.
**file masking**: a feature that masks the data in specific files and saves the masked data in
a database or as files.
**database source**: a specific database that is used as the data source for database
masking or the destination to which the masked data is saved.
**file source**: a collection of files, which is equivalent to a database. You can upload files to
a local folder over FTP, obtain files from a remote FTP server, or upload files on a web page to your local computer. The files stored in a file source are structured files with certain data characteristics, such as files in the standard CSV or TXT format, XML files, Excel files, DMP files, and DICOM files. A file source can be used as the data source for file masking.
**discovery rule**: a rule that identifies sensitive data. You can use a discovery rule to
identify potentially sensitive data from a large number of data items.
**masking algorithm**: an algorithm that removes the sensitivity of sensitive data, such as
masking or replacement.
**discovery task**: a task that discovers sensitive data in database tables or files based on
specific discovery rules.
**sensitive field verification**: a feature that sorts sensitive fields. After a discovery task is
run on a database source, the types of sensitive data in table fields are manually verified.
**sensitive file verification**: a feature that sorts sensitive files. After a discovery task is run
on a file source, the types of sensitive data in file columns are manually verified.
**data subset**: a collection of tables to be masked. Only the masking of DMP files requires
data subsets. The masking of other files does not involve data subsets. After sensitive fields are verified, you can manually create a data subset or directly create a data masking task. When you configure the task, you can select the scope of tables to be masked and skip the step of configuring a data subset.
**masking solution**: a solution that specifies the masking algorithm used to mask the
selected sensitive fields or file columns, such as masking or replacement. After you create a data subset for database masking, you can manually create a masking solution or directly create a data masking task. When you configure the task, you can configure the scope of tables to be masked and the masking algorithm for sensitive fields, and skip the steps of configuring a data subset and a masking solution. After you verify sensitive files for file masking, you can manually create a masking solution or directly create a data masking task. When you configure the task, you can configure a masking algorithm for sensitive columns and skip the step of configuring a masking solution.
**data masking task**: a task that masks data. To mask data, you must configure the
parameters and exception handling method in a data masking task, and then run the task. When you create a data masking task, you can use an existing masking solution or customize a masking algorithm for sensitive fields or sensitive file columns, and skip the step of creating a masking solution.
**automatic data masking task**: a task that automatically downloads the files to be
masked from the source remote FTP file source, masks the files based on a preset template, and then uploads the masked files to the destination remote FTP file source. Automatic data masking tasks must be used together with remote FTP file sources. You must configure sensitive field templates and masking solution templates in advance.
**lookup table**: a table that determines the mappings used by a replacement algorithm for
data masking. If you use a replacement algorithm based on different lookup tables to mask the same data, the masking results vary. Static Data Masking and Waterm s
**data dictionary**: a user-defined dataset, which can contain multiple columns. A data
dictionary can be used to replace a column or columns of data, or randomly combine specified data into a set. It can also be used to discover sensitive data.
**grouping dictionary**: a data dictionary with grouping columns specified. You can use a
grouping dictionary in combination with the grouping column configurations of a masking solution to mask the data in each group. For example, Class 1 has Zhang San, Li Si, and Wang Wu, and Class 2 has Zhao Liu and Zheng Qi. A grouping dictionary can keep the data of the class column (Class 1 and Class 2) unchanged and mask the data of the name column with the names of their respective classes. After data masking, the data of the name column that corresponds to Class 1 is masked with names in Class 1, and the data of the name column that corresponds to Class 2 is masked with names in Class 2.
**field dictionary**: a collection of field names. You can use a field dictionary together with
custom field dictionary discovery rules to discover sensitive data. If a field name exists in a field dictionary, the field is identified as sensitive data.
**sensitive field template**: a template that specifies the type of sensitive data in a specific
column of a specific file. Sensitive field templates are used for automatic data masking tasks.
**masking solution template**: a template that specifies the masking algorithm and
masking parameters to be used for a specific type of sensitive data. Masking solution templates are used for automatic data masking tasks.
**file template**: a template that specifies whether a file contains information such as table
headers, character sets, field delimiters, and field enclosing characters. File templates are used for discovery tasks and file parsing during file masking.
