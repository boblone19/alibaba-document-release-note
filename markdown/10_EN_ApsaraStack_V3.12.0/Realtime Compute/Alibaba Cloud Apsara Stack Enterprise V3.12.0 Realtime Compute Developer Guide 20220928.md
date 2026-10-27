---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Realtime Compute Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 229
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Realtime Compute Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%A4%A7%E6%95%B0%E6%8D%AE/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Realtime%20Compute%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Realtime Compute Developer Guide 20220928

## Table of Contents

- 1 Flink SQL
  - 1.1 Overview
  - 1.2 Keywords
  - 1.3 Terms
    - 1.3.1 Watermark
    - 1.3.2 Computed column
    - 1.3.3 Time attributes
  - 1.4 Data types
    - 1.4.1 Data types
    - 1.4.2 Data types and operators
  - 1.5 DDL statements
    - 1.5.1 Overview
    - 1.5.2 Create a data source table
      - 1.5.2.1 Overview
      - 1.5.2.2 Create a DataHub source table
      - 1.5.2.3 Create a Log Service source table
    - 1.5.3 Create a data result table
      - 1.5.3.1 Overview
      - 1.5.3.2 Create a DataHub result table
      - 1.5.3.3 Create a Log Service result table
      - 1.5.3.4 Create a Table Store result table
      - 1.5.3.5 Create an RDS result table
    - 1.5.4 Create a data dimension table
      - 1.5.4.1 Overview
      - 1.5.4.2 Create a Table Store dimension table
      - 1.5.4.3 Create an RDS dimension table
  - 1.6 DML statements
    - 1.6.1 INSERT INTO statement
  - 1.7 QUERY statements
    - 1.7.1 SELECT statement
    - 1.7.2 WHERE clause
    - 1.7.3 HAVING clause
    - 1.7.4 GROUP BY clause
    - 1.7.5 JOIN statement
    - 1.7.6 JOIN statement for dimension tables
    - 1.7.7 UNION ALL clause
    - 1.7.8 Top_N statement
    - 1.7.9 Complex event processing (CEP)
  - 1.8 Create a view
  - 1.9 Window functions
    - 1.9.1 Overview
    - 1.9.2 Session window
    - 1.9.3 Sliding window
    - 1.9.4 Tumbling window
    - 1.9.5 Over window
  - 1.10 Logical operations
    - 1.10.7 AND
    - 1.10.8 BETWEEN AND
    - 1.10.9 IS NOT FALSE
    - 1.10.10 IS NOT NULL
    - 1.10.11 IS NOT TRUE
    - 1.10.12 IS NOT UNKNOWN
    - 1.10.13 IS NULL
    - 1.10.14 IS TRUE
    - 1.10.15 IS UNKNOWN
    - 1.10.16 LIKE
    - 1.10.17 NOT
    - 1.10.18 NOT BETWEEN AND
    - 1.10.21 NOT IN
    - 1.10.22 IS DISTINCT FROM
    - 1.10.23 IS NOT DISTINCT FROM
  - 1.11 Built-in functions
    - 1.11.1 String functions
      - 1.11.1.1 Overview
      - 1.11.1.2 CHAR_LENGTH
      - 1.11.1.3 CHR
      - 1.11.1.4 CONCAT
      - 1.11.1.5 CONCAT_WS
      - 1.11.1.6 FROM_BASE64
      - 1.11.1.7 HASH_CODE
      - 1.11.1.8 INITCAP
      - 1.11.1.9 JSON_VALUE
      - 1.11.1.10 KEYVALUE
      - 1.11.1.11 LOWER
      - 1.11.1.12 LPAD
      - 1.11.1.14 OVERLAY
      - 1.11.1.15 PARSE_URL
      - 1.11.1.16 POSITION
      - 1.11.1.17 REGEXP
      - 1.11.1.18 REGEXP_EXTRACT
      - 1.11.1.19 REGEXP_REPLACE
      - 1.11.1.20 REPEAT
      - 1.11.1.21 REVERSE
      - 1.11.1.22 RPAD
      - 1.11.1.23 SPLIT_INDEX
      - 1.11.1.24 STR_TO_MAP
      - 1.11.1.25 SUBSTRING
      - 1.11.1.26 TO_BASE64
      - 1.11.1.27 TRIM
      - 1.11.1.28 UPPER
    - 1.11.2 Mathematical unctions
      - 1.11.2.1 Addition
      - 1.11.2.2 Subtraction
      - 1.11.2.3 Multiplication
      - 1.11.2.4 Division
      - 1.11.2.5 ABS
      - 1.11.2.6 ACOS
      - 1.11.2.7 BIN
      - 1.11.2.8 ASIN
      - 1.11.2.9 ATAN
      - 1.11.2.10 BITAND
      - 1.11.2.11 BITNOT
      - 1.11.2.12 BITOR
      - 1.11.2.13 BITXOR
      - 1.11.2.14 CARDINALITY
      - 1.11.2.15 COS
      - 1.11.2.16 COT
      - 1.11.2.18 EXP
      - 1.11.2.19 FLOOR
      - 1.11.2.21 LOG
      - 1.11.2.22 LOG10
      - 1.11.2.23 LOG2
      - 1.11.2.25 POWER
      - 1.11.2.26 RAND
      - 1.11.2.27 SIN
      - 1.11.2.28 SQRT
      - 1.11.2.29 TAN
      - 1.11.2.30 CEIL
      - 1.11.2.31 CHARACTER_LENGTH
      - 1.11.2.32 DEGREES
      - 1.11.2.33 MOD
      - 1.11.2.34 ROUND
    - 1.11.3 Date functions
      - 1.11.3.1 CURRENT_TIMESTAMP
      - 1.11.3.2 DATEDIFF
      - 1.11.3.3 DATE_ADD
      - 1.11.3.4 DATE_FORMAT
      - 1.11.3.5 DATE_SUB
      - 1.11.3.6 DAYOFMONTH
      - 1.11.3.7 FROM_UNIXTIME
      - 1.11.3.8 HOUR
      - 1.11.3.9 LOCALTIME
      - 1.11.3.10 MINUTE
      - 1.11.3.11 MONTH
      - 1.11.3.12 NOW
      - 1.11.3.13 SECOND
      - 1.11.3.14 TIMESTAMPADD
      - 1.11.3.15 TO_DATE
      - 1.11.3.16 TO_TIMESTAMP
      - 1.11.3.17 UNIX_TIMESTAMP
      - 1.11.3.18 WEEK
      - 1.11.3.19 YEAR
    - 1.11.4 Conditional functions
      - 1.11.4.1 CASE WHEN
      - 1.11.4.2 COALESCE
      - 1.11.4.4 IS_ALPHA
      - 1.11.4.5 IS_DECIMAL
      - 1.11.4.6 IS_DIGIT
      - 1.11.4.7 NULLIF
    - 1.11.5 Table-valued functions
      - 1.11.5.1 GENERATE_SERIES
      - 1.11.5.2 JSON_TUPLE
      - 1.11.5.3 STRING_SPLIT
    - 1.11.6 Type conversion functions
      - 1.11.6.1 CAST
    - 1.11.7 Aggregate functions
      - 1.11.7.1 AVG
      - 1.11.7.2 CONCAT_AGG
      - 1.11.7.3 COUNT
      - 1.11.7.4 FIRST_VALUE
      - 1.11.7.5 LAST_VALUE
      - 1.11.7.6 MAX
      - 1.11.7.7 MIN
      - 1.11.7.8 STDDEV_POP
      - 1.11.7.9 SUM
      - 1.11.7.10 VAR_POP
    - 1.11.8 Other functions
      - 1.11.8.1 UUID
  - 1.12 UDXs
    - 1.12.1 Overview
    - 1.12.2 User-defined scalar function (UDSF)
    - 1.12.3 User-defined aggregation function (UDAF)
    - 1.12.4 User-defined table function (UDTF)
    - 1.12.5 Create a user-defined function (UDF) by using IntelliJ IDEA

## 1 Flink SQL

### 1.1 Overview

As a programming language that conforms to standard SQL semantics, Flink SQL is designed to simplify the computational model, making it easy for users to use Realtime Compute. Flink SQL has the following advantages: Low development cost. Flink SQL enables you to implement complex and varied business logic by using simple SQL statements instead of thousands of lines of Apache Storm code. Low maintenance cost. Flink SQL eliminates the need for you to maintain thousands of lines of Storm code. When you use Apache Storm code, system exceptions, errors, or even breakdown may occur and cause data inaccuracies. Flink SQL features specified semantics to resolve the preceding issues. Realtime Compute has the following advantages: Data accuracy. Realtime Compute provides unique exactly-once semantics to ensure data accuracy in various failover scenarios. Performance optimization. Realtime Compute integrates SQL optimization logic to translate SQL code into underlying Apache Storm code that can be used by universal developers. This helps to improve SQL code compilation efficiency. Programming extensibility. Realtime Compute supports user-defined functions (UDFs). You can customize functions to implement a custom business logic or a logic that cannot be achieved by SQL statements. System scalability. Realtime Compute supports auto scaling upon data surges (for example, during the Double 11) while ensuring job and system stability.

### 1.2 Keywords

This topic describes the keywords in Realtime Compute. Realtime Compute keywords Common keywords

| Keyword type | Keywords |
|---|---|
| Data type | VARCHAR, INT, BIGINT, DOUBLE, DATE, BOOLEAN, TINYINT, SMALLINT, FLOAT, DECIMAL, and VARBINARY |
| DDL statement | CREATE TABLE, CREATE FUNCTION, and CREATE VIEW |
| DML statement | INSERT INTO |
| SELECT clause | SELECT FROM, WHERE, GROUP BY, and JOIN |

Naming conventions Names of source tables, result tables, views, and aliases must follow the standard database naming conventions. The names must start with a letter, and can only contain letters, numbers, and underscores (_). Reserved keywords The following strings are reserved as keywords for later use. If you want to use any of the following

| ` | ), for example, | `value` |
|---|---|---|

keywords as a field name, enclose the keyword in backticks ( ` ), for example, `value` .

```
 A, ABS, ABSOLUTE, ACTION, ADA, ADD, ADMIN, AFTER, ALL, ALLOCATE, ALLOW, ALTER, ALWAYS, AND,
ANY, ARE, ARRAY, AS, ASC, ASENSITIVE, ASSERTION, ASSIGNMENT, ASYMMETRIC, AT, ATOMIC, ATTRIBUTE, ATTRIBUTES, AUTHORIZATION, AVG, BEFORE, BEGIN, BERNOULLI, BETWEEN, BIGINT, BINARY, BIT, BLOB, BOOLEAN, BOTH, BREADTH, BY, C, CALL, CALLED, CARDINALITY, CASCADE, CASCADED, CASE, CAST, CATALOG, CATALOG_NAME, CEIL, CEILING, CENTURY, CHAIN, CHAR, CHARACTER, CHARACTERISTICTS, CHARACTERS, CHARACTER_LENGTH, CHARACTER_SET_CATALOG, CHARACTER_SET_NAME, CHARACTER_SET_SCHEMA, CHAR_LENGTH, CHECK, CLASS_ORIGIN, CLOB, CLOSE, COALESCE, COBOL, COLLATE, COLLATION, COLLATION_CATALOG, COLLATION_NAME, COLLATION_SCHEMA, COLLECT, COLUMN, COLUMN_NAME, COMMAND_FUNCTION, COMMAND_FUNCTION_CODE, COMMIT, COMMITTED, CONDITION, CONDITION_NUMBER, CONNECT, CONNECTION, CONNECTION_NAME, CONSTRAINT, CONSTRAINTS, CONSTRAINT_CATALOG, CONSTRAINT_NAME, CONSTRAINT_SCHEMA, CONSTRUCTOR, CONTAINS, CONTINUE, CONVERT, CORR, CORRESPONDING, COUNT, COVAR_POP, COVAR_SAMP, CREATE, CROSS, CUBE, CUME_DIST, CURRENT, CURRENT_CATALOG, CURRENT_DATE, CURRENT_DEFAULT_TRANSFORM_GROUP, CURRENT_PATH, CURRENT_ROLE, CURRENT_SCHEMA, CURRENT_TIME, CURRENT_TIMESTAMP, CURRENT_TRANSFORM_GROUP_FOR_TYPE, CURRENT_USER, CURSOR, CURSOR_NAME, CYCLE, DATA, DATABASE, DATE, DATETIME_INTERVAL_CODE, DATETIME_INTERVAL_PRECISION, DAY, DEALLOCATE, DEC, DECADE, DECIMAL, DECLARE, DEFAULT, DEFAULTS, DEFERRABLE, DEFERRED, DEFINED, DEFINER, DEGREE, DELETE, DENSE_RANK, DEPTH, DEREF, DERIVED, DESC, DESCRIBE, DESCRIPTION, DESCRIPTOR, DETERMINISTIC, DIAGNOSTICS, DISALLOW, DISCONNECT, DISPATCH, DISTINCT, DOMAIN, DOUBLE, DOW, DOY, DROP, DYNAMIC, DYNAMIC_FUNCTION, DYNAMIC_FUNCTION_CODE, EACH, ELEMENT, ELSE, END, END-EXEC, EPOCH, EQUALS, ESCAPE, EVERY, EXCEPT, EXCEPTION, EXCLUDE, EXCLUDING, EXEC, EXECUTE, EXISTS, EXP, EXPLAIN, EXTEND, EXTERNAL, EXTRACT, FALSE, FETCH, FILTER, FINAL, FIRST, FIRST_VALUE, FLOAT, FLOOR, FOLLOWING, FOR, FOREIGN, FORTRAN, FOUND, FRAC_SECOND, FREE, FROM, FULL, FUNCTION, FUSION, G, GENERAL, GENERATED, GET, GLOBAL, GO, GOTO, GRANT, GRANTED, GROUP, GROUPING, HAVING, HIERARCHY, HOLD, HOUR, IDENTITY, IMMEDIATE, IMPLEMENTATION, IMPORT, IN, INCLUDING, INCREMENT, INDICATOR, INITIALLY, INNER, INOUT, INPUT, INSENSITIVE, INSERT, INSTANCE, INSTANTIABLE, INT, INTEGER, INTERSECT, INTERSECTION, INTERVAL, INTO, INVOKER, IS, ISOLATION, JAVA, JOIN, K, KEY, KEY_MEMBER, KEY_TYPE, LABEL, LANGUAGE, LARGE, LAST, LAST_VALUE, LATERAL, LEADING, LEFT, LENGTH, LEVEL, LIBRARY, LIKE, LIMIT, LN, LOCAL, LOCALTIME, LOCALTIMESTAMP, LOCATOR, LOWER, M, MAP, MATCH, MATCHED, MAX, MAXVALUE, MEMBER, MERGE, MESSAGE_LENGTH, MESSAGE_OCTET_LENGTH, MESSAGE_TEXT, METHOD, MICROSECOND, MILLENNIUM, MIN, MINUTE, MINVALUE, MOD, MODIFIES, MODULE, MONTH, MORE, MULTISET, MUMPS, NAME, NAMES, NATIONAL, NATURAL, NCHAR, NCLOB, NESTING, NEW, NEXT, NO, NONE, NORMALIZE, NORMALIZED, NOT, NULL, NULLABLE, NULLIF, NULLS, NUMBER, NUMERIC, OBJECT, OCTETS, OCTET_LENGTH, OF, OFFSET, OLD, ON, ONLY, OPEN, OPTION, OPTIONS, OR, ORDER, ORDERING, ORDINALITY, OTHERS, OUT, OUTER, OUTPUT, OVER, OVERLAPS, OVERLAY, OVERRIDING, PAD, PARAMETER, PARAMETER_MODE, PARAMETER_NAME, PARAMETER_ORDINAL_POSITION, PARAMETER_SPECIFIC_CATALOG, PARAMETER_SPECIFIC_NAME, PARAMETER_SPECIFIC_SCHEMA, PARTIAL, PARTITION, PASCAL, PASSTHROUGH, PATH, PERCENTILE_CONT, PERCENTILE_DISC, PERCENT_RANK, PLACING, PLAN, PLI, POSITION, POWER, PRECEDING, PRECISION, PREPARE, PRESERVE, PRIMARY, PRIOR, PRIVILEGES, PROCEDURE, PUBLIC, QUARTER, RANGE, RANK, READ, READS, REAL, RECURSIVE, REF, REFERENCES, REFERENCING, REGR_AVGX, REGR_AVGY, REGR_COUNT, REGR_INTERCEPT, REGR_R2, REGR_SLOPE, REGR_SXX, REGR_SXY, REGR_SYY, RELATIVE, RELEASE, REPEATABLE, RESET, RESTART, RESTRICT, RESULT, RETURN, RETURNED_CARDINALITY, RETURNED_LENGTH, RETURNED_OCTET_LENGTH, RETURNED_SQLSTATE, RETURNS, REVOKE, RIGHT, ROLE, ROLLBACK, ROLLUP, ROUTINE, ROUTINE_CATALOG, ROUTINE_NAME, ROUTINE_SCHEMA, ROW, ROWS, ROW_COUNT, ROW_NUMBER, SAVEPOINT, SCALE, SCHEMA,
```

```
SCHEMA_NAME, SCOPE, SCOPE_CATALOGS, SCOPE_NAME, SCOPE_SCHEMA, SCROLL, SEARCH, SECOND, SECTION, SECURITY, SELECT, SELF, SENSITIVE, SEQUENCE, SERIALIZABLE, SERVER, SERVER_NAME, SESSION, SESSION_USER, SET, SETS, SIMILAR, SIMPLE, SIZE, SMALLINT, SOME, SOURCE, SPACE, SPECIFIC, SPECIFICTYPE, SPECIFIC_NAME, SQL, SQLEXCEPTION, SQLSTATE, SQLWARNING, SQL_TSI_DAY, SQL_TSI_FRAC_SECOND, SQL_TSI_HOUR, SQL_TSI_MICROSECOND, SQL_TSI_MINUTE, SQL_TSI_MONTH, SQL_TSI_QUARTER, SQL_TSI_SECOND, SQL_TSI_WEEK, SQL_TSI_YEAR, SQRT, START, STATE, STATEMENT, STATIC, STDDEV_POP, STDDEV_SAMP, STREAM, STRUCTURE, STYLE, SUBCLASS_ORIGIN, SUBMULTISET, SUBSTITUTE, SUBSTRING, SUM, SYMMETRIC, SYSTEM, SYSTEM_USER, TABLE, TABLESAMPLE, TABLE_NAME, TEMPORARY, THEN, TIES, TIME, TIMESTAMP, TIMESTAMPADD, TIMESTAMPDIFF, TIMEZONE_HOUR, TIMEZONE_MINUTE, TINYINT, TO, TOP_LEVEL_COUNT, TRAILING, TRANSACTION, TRANSACTIONS_ACTIVE, TRANSACTIONS_COMMITTED, TRANSACTIONS_ROLLED_BACK, TRANSFORM, TRANSFORMS, TRANSLATE, TRANSLATION, TREAT, TRIGGER, TRIGGER_CATALOG, TRIGGER_NAME, TRIGGER_SCHEMA, TRIM, TRUE, TYPE, UESCAPE, UNBOUNDED, UNCOMMITTED, UNDER, UNION, UNIQUE, UNKNOWN, UNNAMED, UNNEST, UPDATE, UPPER, UPSERT, USAGE, USER, USER_DEFINED_TYPE_CATALOG, USER_DEFINED_TYPE_CODE, USER_DEFINED_TYPE_NAME, USER_DEFINED_TYPE_SCHEMA, USING, VALUE, VALUES, VARBINARY, VARCHAR, VARYING, VAR_POP, VAR_SAMP, VERSION, VIEW, WEEK, WHEN, WHENEVER, WHERE, WIDTH_BUCKET, WINDOW, WITH, WITHIN, WITHOUT, WORK, WRAPPER, WRITE, XML, YEAR, ZONE
```

### 1.3 Terms

#### 1.3.1 Watermark

Realtime Compute aggregates data by using window functions based on a time attribute. To use window functions based on event time, you must define a watermark in the DDL statement of a source table. Watermarking is a mechanism in Flink to measure progress in event time. A watermark provides a time attribute by carrying a timestamp. Flink provides the following statement to define a watermark: Not e For more information about time attributes supported by Realtime Compute, see Time attributes.

```
WATERMARK [watermarkName] FOR <rowtime_field> AS withOffset(<rowtime_field>, offset)
```

| Parameter | Description |
|---|---|
| watermarkName | Specifies the name of a watermark. This parameter is optional. |
| <rowtime field> _ | Specifies a column that is used to generate a watermark. The data type of the column must be TIMESTAMP. The column is labeled as the event time column. You can use this event time column to define windows in queries. |
| withOffset | Specifies the strategy of generating a watermark. The value for a watermark is obtained based on <rowtime field> - offset . In withOffset , _ you must define <rowtime field> as the first _ parameter. |

| Parameter | Description |
|---|---|
| offset | Specifies the offset between a watermark value and an event time, which is measured in milliseconds. |

The time when a data record is generated is indicated by a field. For example, a table has a `rowtime` column of the TIMESTAMP data type, and one value is `1501750584000 (2017-08-03 08:56:24.000)` . Based on the `rowtime` column, you can define a watermark with a four-second offset as follows:

```
WATERMARK FOR rowtime AS withOffset(rowtime, 4000)
```

The watermark value of the specified data record is obtained: `1501750584000 - 4000 =` `1501750580000 (2017-08-03 08:56:20.000)` . The watermark value indicates that all data with the timestamps earlier than `1501750580000 (2017-08-03 08:56:20.000)` has arrived. Not e When you define a watermark based on event time, the data type of the `rowtime` column must be TIMESTAMP. Currently, Realtime Compute only supports 13-bit Unix timestamps measured in milliseconds. If the data type of a rowtime column is not TIMESTAMP or a Unix timestamp is not 13 digits in length, we recommend that you use a Computed column to convert data types. Event time and processing time can only be declared in the DDL statement of a source table. Summary A watermark indicates that all the events with the timestamps t' earlier than the watermark `t` have occurred. After a watermark `t` arrives at an operator, all subsequent records with

| t | arriv |
|---|---|
| mark | t |

timestamps earlier than the watermark `t` are discarded. This is the current watermarking mechanism in Realtime Compute. However, in the future, improvements to Realtime Compute will allow you to update subsequent data. The watermarking mechanism is crucial for handling out-of-order data streams. With watermarks, real-time computing results are accurate even if data streams arrive out of order. When an operator has multiple input data streams, the event time of the operator equals the minimum event time of the data streams.

#### 1.3.2 Computed column

You can calculate a value for a computed column by using data from other columns. If a source table does not have a column of the TIMESTAMP data type, you can use a computed column expression to convert data types. Definition A computed column is a virtual column that is not physically stored in a table. You can create computed columns by using expressions, built-in functions, or user-defined functions. In Flink SQL, a computed column can be used as other columns that are physically stored in a table. Usage Currently, the data type of the event time (also known as rowtime) column in a Watermark must be TIMESTAMP. We are working on support for the LONG data type. You can only define a watermark in the DDL statement of a source table. If a source table does not have a column of the TIMESTAMP data type, you can use a computed column expression to convert data types. Syntax

```
column_name AS computed_column_expression
```

Example The data type of the rowtime column in a watermark must be TIMESTAMP. Currently, Realtime Compute only supports 13-bit Unix timestamps measured in milliseconds. If the TIME column in a DataHub source table is defined as 16-bit Unix timestamps measured in microseconds, you can use a computed column expression to convert data types. An example is described as follows:

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
  Ts AS TO_TIMESTAMP (TIME/1000), -- Converts 16-bit timestamps to 13-bit timestamps by usi
ng a computed column expression.
  WATERMARK FOR ts AS withOffset(ts, 10000)
) WITH (
  type = 'datahub',
  ...
```

);

| f the TIME the TIME ts column | TIME |
|---|---|
| ts |   |

In this example, the data type of the `TIME` column in the source table is BIGINT. A computed column expression is created to convert the `TIME` column of the BIGINT data type to the `ts` column of

#### 1.3.3 Time attributes

This topic describes two time attributes that are supported by Flink SQL: event time and processing time. Event time and processing time are described as follows: Event time: specifies the time at which an event is produced. The event time column must be included in the schema. Processing time: specifies the time at which the system processes an event. Ingestion time and processing time are the time attributes automatically generated by the system for a streaming data record and are not changeable. Event time is the time attribute carried by a streaming data record itself. Assume that data whose event time is t1 is written to Partition 1 and data whose event time is t2 is written to Partition 2. The event time t1 is earlier than t2. However, due to data disorder or network jitter, Realtime Compute may first read and process the data with an event time of t2. Event time Event time is also known as rowtime. The event time attribute must be declared in the DDL statement for creating a source table. You can declare a field in the source table as event time. Currently, only the TIMESTAMP data type is supported for a rowtime field. We are working on providing support for the LONG data type. If the data type of the specified field is not TIMESTAMP, you must create a computed column of the TIMESTAMP data type from existing fields. For more information about computed columns, see Computed column. Due to data disorder or network jitter, the sequence in which Realtime Compute reads and processes data may differ from the sequence in which data arrives. Therefore, after you define the rowtime field, you must define a Watermark. You can perform event time-based window function operations as follows:

```
CREATE TABLE tt_stream(
  a VARCHAR,
  b VARCHAR,
  c TIMESTAMP,
  WATERMARK wk1 FOR c as withOffset(c, 1000)  -- Defines a watermark.
) WITH (
  type = 'sls',
  topic = 'yourTopicName',
  accessId = 'yourAccessId',
  accessKey = 'yourAccessSecret'
```

);

```
CREATE TABLE rds_output(
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) WITH (
  type = 'rds',
  url = 'jdbc:mysql://****3306/test',
  tableName='yourTableName',
  userName = 'yourUserName',
  password = 'yourPassword'
```

);

```
INSERT INTO rds_output SELECT a AS id,
     SESSION_START(c, INTERVAL '1' SECOND) AS c,
     CAST(SESSION_END(c, INTERVAL '1' SECOND) AS TIMESTAMP) AS f,
     COUNT(a) AS cnt
FROM tt_stream GROUP BY SESSION(c, INTERVAL '1' SECOND), a
```

Processing time Processing time is generated by the system and is not included in your original data. Therefore, you need to define a processing time field in a DDL statement.

```
filedName as PROCTIME()
```

You can aggregate data by using a window function based on processing time. An example is described as follows:

```
CREATE TABLE mq_stream (
  a VARCHAR,
  b VARCHAR,
  c BIGINT,
  d AS PROCTIME()   --- Defines a processing time field.
) WITH (
  type = 'rds',
  topic = 'yourTopic',
  accessId = 'yourAccessId',
  accessKey = 'yourAccessSecret'
```

);

```
CREATE TABLE rds_output (
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) with (
  type = 'rds',
  url = 'yourDatebaseURL',
  tableName='yourDatabaseTableName',
  userName = 'yourUserName',
  password = 'yourPassword'
```

);

```
INSERT INTO rds_output SELECT a AS id,
     SESSION_START(d, INTERVAL '1' SECOND) AS c,
     SESSION_END(d, INTERVAL '1' SECOND) AS f,
     COUNT(a) AS cnt
FROM mq_stream GROUP BY SESSION(d, INTERVAL '1' SECOND), a
```

Expiration of time attributes A time attribute field no longer indicates a time attribute if you perform the following two operations: GROUP BY operations (not for window functions) JOIN operations of two data streams Errors will occur if you perform time-based window function operations after the preceding operations. For example, the error message `org. apache. flink. table. api. ValidationException: Window can` `only be defined over a time attribute column.` may appear.

### 1.4 Data types

#### 1.4.1 Data types

This topic describes data types supported by Realtime Compute. Supported data types

| Data type | Description | Value range |
|---|---|---|
| VARCHAR | Character string with a changeable length | Maximum storage capacity: 4 MB |
| BOOLEAN | Logical value | Valid values: TRUE, FALSE, and UNKNOWN |
| TINYINT | Tiny integer (one byte) | -128 to 127 |
| SMALLINT | Small integer (two bytes) | -32768 to 32767 |
| INT | Integer (four bytes) | -2147483648 to 2147483647 |
| BIGINT | Big integer (eight bytes) | -9223372036854775808 to 9223372036854775807 |
| FLOAT | Four-byte floating point number | Six digits of precision |
| DECIMAL | Decimal | An example value for DECIMAL(5,2) is 123.45 . |
| DOUBLE | Eight-byte floating point number | 15 decimal digits of precision |
| DATE | Date | Example: DATE'1969-07-20' |
| TIME | Time | Example: TIME '20:17:40' |
| TIMESTAMP | Timestamp containing both date and time parts | Example: TIMESTAMP '1969-07-20 20:17:40' |
| VARBINARY | Binary data | Byte array |

Type conversion Type conversion example

| var1 (VARCHAR) | big1 (BIGINT) |
|---|---|
| 1000 | 323 |

Sample code

```
CAST(var1 AS BIGINT) AS AA; CAST(big1 AS VARCHAR) AS BB;
```

Output example

| AA (BIGINT) | BB (VARCHAR) |
|---|---|
| 1000 | 323 |

#### 1.4.2 Data types and operators

This topic describes data types and operators in Realtime Compute. You can perform mathematical and logical operations for different data types. Examples are provided in the following table.

| Operator | Description | Data types supported by numeric1 and numeric2 | Example |
|---|---|---|---|
| numeric1 + numeric2 | Addition | INT, DOUBLE, DECIMAL, BIGINT | 2 + 4.2 |
| numeric1 - numeric2 | Subtraction |   | 3 - 5.3 |
| numeric1 * numeric2 | Multiplication |   | 2 * 4 |
| numeric1/numeric2 | Division |   | 2.4/5 |
| numeric1 > numeric2 | > |   | 2.4 > 5 |
| numeric1 < numeric2 | < |   | 2.4 < 5 |
| numeric1 >= numeric2 | >= |   | 2.4 >= 5 |
| numeric1 <= numeric2 | <= |   | 2.4 <= 5 |
| 0 |   | > Document Ve | rsion: 2022092 |

|   |   | 2 + |
|---|---|---|
|   | 4.2 |   |

|   |   | 3 - |
|---|---|---|
|   | 5.3 |   |

|   |   | 2.4 > |
|---|---|---|
|   | 5 |   |

|   |   | 2.4 < |
|---|---|---|
|   | 5 |   |

|   |   | 2.4 >= |
|---|---|---|
|   | 5 |   |

|   |   | 2.4 <= |
|---|---|---|
|   | 5 |   |

| Operator Description numeric1 = numeric2 = numeric1 <> numeric2 <> |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   | Operator | Description | Data types supported by numeric1 and numeric2 |   | Example |   |   |
|   | numeric1 = numeric2 | = | INT, DOUBLE, DECIMAL, BIGINT, VARCHAR |   | ‘iphone’ = 5 |   |   |
|   | numeric1 <> numeric2 | <> |   |   | 'iphone' <> 5 |   |   |
|   |   |   |   |   |   | 'iphone' |   |
|   |   |   |   |   | <> 5 |   |   |

|   |   | ‘iphone’ |   |
|---|---|---|---|
| , | = 5 |   |   |

### 1.5 DDL statements

#### 1.5.1 Overview

Syntax

```
CREATE TABLE tableName
     (columnName dataType [, columnName dataType ]*)
     [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

Description Realtime Compute does not store data from source and result tables. You can only perform operations on source and result tables by using DDL statements to declare references to data stores. Example:

```
create table tt_stream(
    a varchar,
    b varchar,
    c varchar
    ) with (
    type='DataHub',
    topic='blink_tt_test',
    accessId='yourAccessId',
    accessKey='yourAccessSecret'
```

); This Flink SQL statement is not used to create a DataHub topic, but to create a table named tt_stream in Realtime Compute and use the table to declare a reference to a DataHub topic. You can use tt_stream as an alias in subsequent DML statements to perform operations on the table. A declaration of a table (tt_stream in this example) is only valid for the jobs generated from the current SQL file. A job is generated after a SQL file is published. The table can also be declared for reference in other SQL files under the same project. Since Realtime Compute adopts standard SQL, keywords, table names, and field names in DDL statements are case-insensitive. Table and field names must start with a letter or number and can only contain letters, numbers, and underscores (_). The method of mapping fields between a source table and an upstream data store depends on the feature of the data store. If the data store such as DataHub supports mapping based on key values, the field names in the source table must be the same as those in the data store. However, the number of fields can be different. If a data store does not support mapping based on key values, both the number and sequence of fields defined in the source table must the same as those in the data store. We recommend that you use the same field names and the same number of fields in DDL statements as those in external data stores. This can prevent data errors caused by inaccurate definitions. Field mapping Data stores are classified into two types based on whether the data store has a schema. Sequence mapping Systems such as Message Queue (MQ) are non-structured storage systems that do not have a schema. You can customize field names in DDL statements. However, the data types and the number of fields must be the same as those in the data store. The following example shows an MQ record:

```
asavfa,sddd32,sdfdsv
```

You need to set field names of the tt_stream table based on naming conventions.

```
create table tt_stream(
      a varchar,
      b varchar,
      c varchar
      ) with (
      type = 'mq',
      topic='blink_mq_test',
      accessId='yourAccessId',
      accessKey='yourAccessSecret'
```

); Name mapping For structured storage systems such as DataHub, field names and data types are defined based on a table schema. We recommend that you define fields by using Flink SQL based on the table schema. The names, number, and sequence of fields must be the same as those in the data store. Not e If field names in the data store (such as Table Store) are case-sensitive, you need to enclose field names in backticks (`) in Flink SQL statements. Take DataHub as an example. In DDL statements, field names of the declared source table must apply the same casing that DataHub uses. The following table describes a sample schema of DataHub. A sample schema of DataHub

| Field | Data type |
|---|---|
| name | varchar |
| age | bigint |
| value | varchar |

We recommend that you declare references for all fields. Note that you can only reference the fields that are included in the data store. A sample of the DDL statement is provided as follows:

```
create table stream_result (
     name varchar,
     age bigint,
     value varchar
     ) with (
     type='DataHub',
     endpoint='http://dh-cn-hangzhou.aliyuncs.com',
     accessId='yourAccessId',
     accessKey='yourAccessSecret',
     project='project',
     topic = 'topic'
```

); Case insensitivity Realtime Compute adopts standard SQL. Therefore, fields are case-insensitive. For example, the following two statements produce the same effect. Statement 1:

```
create table stream_result (
    name             varchar,
    value            varchar
```

); Statement 2:

```
create table STREAM_RESULT (
     NAME             varchar,
     VALUE            varchar
```

); Realtime Compute references data from multiple data stores. Some data stores, such as Table Store, are case-sensitive in field names. If a NAME parameter is defined in Table Store, the DDL statement must be as follows:

```
create table STREAM_RESULT (
    `NAME`            varchar,
    `VALUE`           varchar
```

); In all subsequent DML statements, the parameter must be enclosed in backticks (`) if it is referenced. A sample code is provided as follows:

```
INSERT INTO Table_A
    SELECT
    `NAME`,
    `VALUE`
    FROM
    Table_B;
```

#### 1.5.2 Create a data source table

##### 1.5.2.1 Overview

Source tables for Realtime Compute store streaming data. Streaming data triggers stream processing jobs in Realtime Compute. To perform stream processing, you must create at least one source table that provides streaming data for Realtime Compute jobs. Syntax

```
  CREATE TABLE tableName
      (columnName dataType [, columnName dataType ]*)
      [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

Examples

```
CREATE TABLE metaq_stream(
 x VARCHAR,
 y VARCHAR,
 z VARCHAR
) WITH (
 type='mq',
 topic='<yourTopicName>',
 endpoint='<yourEndpointName>',
 pullIntervalMs='1000',
 accessId='<yourAccessId>',
 accessKey='<yourAccessKey>',
 startMessageOffset='1000',
 consumerGroup='<yourConsumerGroup>',
 fieldDelimiter='|'
```

); Retrieve attribute fields from a source table Syntax You must add the `HEADER` keyword to the end of a field declaration in the DDL statement of the source table before you can retrieve attribute fields from a source table.

```
CREATE TABLE sourcetable
```

`(`

```
 `timestamp`  VARCHAR HEADER,
  name        VARCHAR,
  MsgID       VARCHAR
)WITH(
     type='RDS'
```

); In this example, the `timestamp` field is defined as `HEADER` . Realtime Compute reads the values of the attribute field from the source table, and then uses the field as a general field. Not e The attribute field varies according to the source table type, such as DataHub, Log Service, and Message Queue. You can customize attribute fields for certain types of source tables. For more information, see the topics about source tables. Example A Log Service source table is used as an example to explain how to retrieve attribute fields. Log Service supports the following three attribute fields.

| Field name | Description |
|---|---|
| source __ __ | The log source |
| topic __ __ | The log topic |
| timestamp __ __ | The time when a data record enters Log Service |

Not e You must add the `HEADER` keyword to the end of a field declaration before you can retrieve attribute fields from a source table. Examples Input example

```
__topic__: ens_altar_flow
        result:  {"MsgID":"ems0a","Version":"0.0.1"}
```

Sample code

```
CREATE TABLE sls_log (
  __topic__  VARCHAR HEADER,
  result     VARCHAR
)WITH(
  type ='sls'
```

);

```
CREATE TABLE sls_out (
  name     varchar,
  MsgID    varchar,
  Version  varchar
)WITH(
  type ='RDS'
```

);

```
INSERT INTO sls_out SELECT __topic__, JSON_VALUE(result,'$.MsgID'), JSON_VALUE(result,'$.Version') FROM sls_log
```

| name (VARCHAT) | MsgID (VARCHAT) | Version (VARCHAT) |
|---|---|---|
| ens altar flow _ _ | ems0a | 0.0.1 |

Source tables for window function-based computing Realtime Compute can aggregate data by using window functions based on the event time or processing time. If window functions are used for a stream processing job, you must define the watermark and computed column in the DDL statement of a source table. For more information about the watermark and computed column, see Watermark and Computed column. For information about data aggregation based on time attributes, see Time attributes.

##### 1.5.2.2 Create a DataHub source table

This topic describes how to create a DataHub source table for Realtime Compute. It introduces attribute fields, parameters in the WITH clause, and type mapping. Introduction to DataHub DataHub is a real-time data distribution platform that is designed to process streaming data. It transmits big data to other Alibaba Cloud Services. DataHub can work with multiple Alibaba Cloud services to build an end-to-end data processing platform. Realtime Compute uses DataHub to store source tables and result tables for stream processing jobs. Data Transmission Services (DTS) and the Internet of Things (IoT) also use DataHub to access big data platforms. DataHub stores streaming data that can be used as input data for Realtime Compute. Example You can use the following sample code to create a DataHub source table:

```
create table datahub_stream(
  name VARCHAR,
  age BIGINT,
  birthday BIGINT
) with (
  type='datahub',
  endPoint='yourEndpoint',
  project='yourProjectName',
  topic = 'yourTopicName',
  accessId='yourAccessId',
  accessKey='yourAccessSecret',
  startTime='2017-07-21 00:00:00'
```

); Attribute field (timestamp) You can use Flink SQL to retrieve the timestamp field of a DataHub source table. You can obtain the system time of each data record by reading the timestamp field of a DataHub source table.

| Field name | Description |
|---|---|
| timestamp | Specifies the system time at which data is written into a DataHub source table. |

At t ribut e f ield inst ruct ions To extract data from the attribute field of DataHub, you need to add the `HEADER` keyword to the end of a field declaration. Attribute fields are not defined in the DataHub topic. To extract the `system time` of each data record, you can define a `timestamp` field, and add `HEADER` to the end of the field declaration. Example: Input example

| name (VARCHAR) | MsgID (VARCHAR) |
|---|---|
| ens altar flow _ _ | ems0a |

Sample code

```
CREATE TABLE datahub_log (
  `timestamp`  varchar HEADER,
  name       varchar,
  MsgID        varchar
```

`)`

```
WITH
```

`(`

```
  type ='datahub'
```

);

```
CREATE TABLE RDS_out (
  `timestamp`     varchar,
  MsgID    varchar,
  name  varchar
```

`)`

```
WITH
```

`(`

```
  type ='RDS'
```

);

```
INSERT INTO RDS_out SELECT `timestamp`, MsgID, name FROM datahub_log;
```

Output example

| TIME (VARCHAR) | MsgID (VARCHAR) | name (VARCHAR) |
|---|---|---|
| 1522652455625 | ems0a | ens altar flow _ _ |

Parameters in the WITH clause Currently, topics only support the data records of the tuple pattern.

| Parameter | Description | Remarks |
|---|---|---|
| endPoint | Specifies the consumer endpoint. | For more information, see Obtain an endpoint in DataHub Developer Guide. |
| accessId | Specifies an AccessKey ID. | N/A |
| accessKey | Specifies an AccessKey secret. | N/A |
| project | Specifies a project in DataHub. | N/A |
| topic | Specifies a topic of the project. | N/A |
| startTime | Specifies a start offset. | The format is yyyy-MM-dd hh:mm:ss . |
| maxRetryTimes | Specifies a maximum number of read attempts. | Optional. The default value is 20. |
| retryIntervalMs | Specifies an interval of retries. | Optional. The default value is 1000. |
| batchReadSize | Specifies the number of data records that are read at a time. | Optional. The default value is 10, and the maximum value is 1000. |

|   | hh:mm:ss |
|---|---|

| Parameter | Description | Remarks |
|---|---|---|
| lengthCheck | Specifies a rule for checking the number of fields parsed from a row of data. | Optional. The default value is NONE, indicating: When the number of fields parsed from a row of data is greater than the number of defined fields, data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is smaller than the number of defined fields, this row of data is skipped. Other valid values are SKIP, EXCEPTION, and PAD. SKIP: When the number of fields parsed from data does not match the number of defined fields, this row of data is skipped. EXCEPTION: When the number of fields parsed from data does not match the number of defined fields, an exception is reported. PAD: Data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is greater than the number of defined fields, data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is smaller than the number of defined fields, the values of the missing fields are null. |
| columnErrorDebug | Specifies whether debugging is enabled. If you enable debugging, parsing exceptions are logged when they occur. | Optional. The default value is false. |

Type mapping The following table lists the mapping between DataHub and Realtime Compute data types. We recommend that you declare the type mapping in the DDL statement.

| DataHub data type | Realtime Compute data type |
|---|---|
| BIGINT | BIGINT |
| STRING | VARCHAR |

|   | Developer Guide·Flink SQL | Realtime Comput | e |
|---|---|---|---|

| DataHub data type | Realtime Compute data type |
|---|---|
| DOUBLE | DOUBLE |
| TIMESTAMP | BIGINT |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |

Not e The TIMESTAMP type field defined in DataHub is a 16-digit Unix timestamp measured in microseconds. In contrast, the TIMESTAMP type field defined in Realtime Compute is a 13-digit Unix timestamp measured in milliseconds. Therefore, we recommend that you convert the TIMESTAMP data type to BIGINT. If you want to use the TIMESTAMP data type in Realtime Compute, we recommend that you use Computed column to convert the time format.

##### 1.5.2.3 Create a Log Service source table

This topic describes how to create a Log Service source table for Realtime Compute. It introduces supported attribute fields, parameters in the WITH clause, and type mapping. Introduction to Log Service Log Service is a one-stop logging service developed by Alibaba Cloud. It has shown superior performance in big data scenarios. Log Service is used to store streaming data. The streaming data can be used as input data for Realtime Compute. The data format of logs is JSON. An example is described as follows: `{`

```json
    "a": 1000,
    "b": 1234,
    "c": "li"
```

`}` You can define a DDL statement as follows (sls in the code represents Log Service):

```
create table sls_stream(
  a int,
  b int,
  c VARCHAR
) with (
  type ='sls',
  endPoint='yourEndpoint',
  accessId ='yourAccessId',
  accessKey ='yourAccessKey',
  startTime = 'yourStartTime',
  project='yourProjectName',
  logStore='yourLogStoreName',
  consumerGroup ='yourConsumerGroupName'
```

); Supported attribute fields Currently, Flink SQL supports three types of Log Service attribute fields by default. Custom fields are also supported.

| Field name | Description |
|---|---|
| source __ __ | Specifies a log source. |
| topic __ __ | Specifies a log topic. |
| timestamp __ __ | Specifies the time when a logged event occurs. |

Attribute field instructions To extract data from the supported fields, you need to add the `HEADER` keyword after the data type in the declaration. An example is described as follows: Input example

```
     __topic__:  ens_altar_flow
        result:  {"MsgID":"ems0a","Version":"0.0.1"}
```

Sample code

```
CREATE TABLE sls_log (
  __topic__  VARCHAR HEADER,
  result     VARCHAR
```

`)`

```
WITH
```

`(`

```
  type ='sls',
```

);

```
CREATE TABLE sls_out (
  name     VARCHAR,
  MsgID    VARCHAR,
  Version  VARCHAR
```

`)`

```
WITH
```

`(`

```
  type ='RDS'
```

);

```
INSERT INTO sls_out SELECT __topic__ JSON_VALUE (result, '$. MsgID '), JSON_VALUE (result, '$. version ') FROM sls_log
```

Output example

| name (VARCHAR) | MsgID (VARCHAR) | Version (VARCHAR) |
|---|---|---|
| ens altar flow _ _ | ems0a | 0.0.1 |

Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| endPoint | Specifies the consumer endpoint. | Log Service Endpoint, for example http://regionid.example.com . |
| accessId | Specifies an AccessKey ID. | N/A |
| accessKey | Specifies an AccessKey Secret. | N/A |
| project | Specifies a project in Log Service. | N/A |
| logStore | Specifies the name of a Logstore in the project. | N/A |
| consumerGroup | Specifies the name of a consumer group. | You can specify a consumer group name. The format of the consumer group name is not fixed. |
| startTime | Specifies the time at which a log starts to be consumed. | N/A |
| heartBeatIntervalM ills | Optional. Specifies a heartbeat interval of a consumption client. | The default value is 10 seconds. |
| maxRetryTimes | Specifies a maximum number of read attempts. | Optional. The default value is 5. |
| batchGetSize | Specifies the number of log groups that are read at a time. | Optional. The default value is 10. |

| Parameter | Description | Remarks |
|---|---|---|
| lengthCheck | Specifies a rule for checking the number of fields parsed from a row of data. | Optional. The default value is NONE, indicating: When the number of fields parsed from a row of data is greater than the number of defined fields, data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is smaller than the number of defined fields, this row of data is skipped. Other optional values are SKIP, EXCEPTION, and PAD. SKIP: When the number of fields parsed from data does not match the number of defined fields, this row of data is skipped. EXCEPTION: When the number of fields parsed from data does not match the number of defined fields, an exception is reported. PAD: Data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is greater than the number of defined fields, data is extracted from left to right based on the order of defined fields. When the number of fields parsed from a row of data is smaller than the number of defined fields, null is used to fill in the missing fields. |
| columnErrorDebug | Specifies whether debugging is enabled. | Optional. The default value is false. If you enable debugging, a log entry that indicates a parsing exception is printed. |
| directMode | Specifies whether the direct connection mode to access Log Service is enabled. | Optional. The default value is false, indicating that the direct connection mode is not enabled. After the direct mode is enabled, you can access Log Service through an Nginx server. An Nginx server demonstrates high performance in handling connection requests. |

Not e Currently, Log Service does not support the MAP data type. We recommend that you define the fields in the same order as the fields in the preceding table. Unordered fields are also supported. If input data is in the JSON format, define a delimiter and use the built-in function JSON_VALUE to analyze the data. Otherwise, a parsing error will occur and the following error message will appear:

```
2017-12-25 15:24:43,467 WARN [Topology-0 (1/1)] com.alibaba.blink.streaming.conne ctors.common.source.parse.DefaultSourceCollector - Field missing error, table col umn number: 3, data column number: 3, data filed number: 1, data: [{"lg_order_cod e":"LP00000005","activity_code":"TEST_CODE1","occur_time":"2017-12-10 00:00:01"}]
```

The batchGetSize value must not exceed 1000. Otherwise, an error will occur. The batchGetSize parameter specifies the number of log groups that are read at a time. If the size of a single log entry and the batchGetSize value are too large, frequent garbage collection is generated. To avoid this issue, you need to set this parameter to a small value. Type mapping The following table describes the mapping between Log Service data types and Realtime Compute data types. We recommend that you declare the mapping in a DDL statement.

| Log Service data type | Realtime Compute data type |
|---|---|
| STRING | VARCHAR |

#### 1.5.3 Create a data result table

##### 1.5.3.1 Overview

Realtime Compute uses the `CREATE TABLE` statement to define the schema of a result table for output data and how data is written into a target data store. Data can be written by using either of the following methods: append and update. Append: If the result table is stored in a relational database with no primary key defined, Log Service, or Message Queue, output data is appended to the result table. Update: If the result table is stored in a relational database or a Hadoop database with a primary key defined, output data is written into the result table as follows: If the value for the primary key is not found in the result table, the data record is inserted into the database. If the value for the primary key is found, the existing data record in the database is overwritten. Result table syntax

```
CREATE TABLE tableName
    (columnName dataType [, columnName dataType ]*)
    [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

Example

```
CREATE TABLE rds_output( id INT, len INT, content VARCHAR, PRIMARY KEY(id) ) WITH ( type='rds', url='yourDatabaseURL', tableName='yourTableName', userName='yourDatabaseUserName', password='yourDatabasePassword'
```

);

##### 1.5.3.2 Create a DataHub result table

This topic describes how to create a DataHub result table for Realtime Compute. Introduction to DataHub DataHub is a data distribution platform that is designed to process streaming data. It provides a channel for other Apsara Stack services to process big data. DataHub works with multiple Alibaba Cloud services to provide an end-to-end data processing solution. In Realtime Compute, you can use DataHub to store input and output data. DDL syntax In Realtime Compute, you can create a DataHub result table to store output data. The sample code is provided as follows:

```
create table datahub_output(
  name varchar,
  age BIGINT,
  birthday BIGINT
)with(
  type='datahub',
  endPoint='yourEndpoint',
  project='yourProjectName',
  topic='yourTopicName',
  accessId='yourAccessId',
  accessKey='yourAccessSecret',
  batchSize='20',
  batchWriteTimeoutMs='1000'
```

); Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| endPoint | Specifies the endpoint. | For more information, see Obtain an endpoint in DataHub Developer Guide. |
| project | Specifies the name of a DataHub project. | N/A |
| topic | Specifies the name of a DataHub topic. | N/A |
| accessId | Specifies the AccessKey ID. | N/A |
| accessKey | Specifies the AccessKey Secret. | N/A |
| maxRetryTimes | Specifies the maximum number of retries for writing data to the result table. | Optional. The default value is 3. |
| batchSize | Specifies the number of data records that are written at a time. | Optional. The default value is 300. |
| batchWriteTimeoutMs | Specifies the timeout period for writing data. | Optional. The default value is 5000. |
| maxBlockMessages | Specifies the maximum number of data blocks that are written at a time. | Optional. The default value is 100. |

##### 1.5.3.3 Create a Log Service result table

This topic describes how to create a Log Service result table for Realtime Compute. Introduction to Log Service Log Service (LOG) provides an end-to-end management solution for real-time log data. Log Service allows you to quickly collect, consume, ship, query, and analyze log data without the need for further development. Log Service has high performance in data O&M. You can use Log Service to process massive logs to meet business demands in the data technology (DT) era. DDL syntax In Realtime Compute, you can use Log Service to store output data. The sample code is provided as follows:

```
create table sls_stream(
 name varchar,
 age BIGINT,
 birthday BIGINT
)with(
 type='sls',
 endPoint='yourEndpoint',
 accessId='yourAccessId',
 accessKey='yourAccessKey',
 project='yourProjectName',
 logStore='yourLogStoreName'
```

); Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| endPoint | Specifies the endpoint. | Log Service Endpoint, for example http://regionid.example.co m . |
| project | Specifies the name of a Log Service project. | N/A |
| topic | Specifies the name of a Log Service topic. | N/A |
| accessId | Specifies the AccessKey ID. | N/A |
| accessKey | Specifies the AccessKey Secret. | N/A |
| mode | Specifies the mode for writing data to the result table. | Optional. The default value is random . If you set this parameter to partition , the result table is partitioned and data is written to the specified partition. |
| partitionColumn | Specifies the partition column. | This parameter is required if the mode parameter is set to partition . |
| source | Specifies the source of logs. For example, you can set this parameter to the IP address of the server where logs are generated. | Optional. The default value is NONE. |

|   |   | http://regionid.example.co |
|---|---|---|
|   | m |   |

##### 1.5.3.4 Create a Table Store result table

This topic describes how to create a Table Store result table for Realtime Compute. This topic also introduces the mapping between Table Store data types and Realtime Compute data types. Introduction to Table Store Table Store is a distributed NoSQL data storage service developed based on the Apsara distributed system. Based on data sharding and load balancing technologies, Table Store has high performance in scaling out and handling concurrent transactions. You can use Table Store to store and query large amounts of structured data. DDL syntax In Realtime Compute, you can use Table Store to store output data. The sample code is provided as follows:

```
CREATE TABLE stream_test_hotline_agent (
 name varchar,
 age BIGINT,
 birthday BIGINT,
 primary key(name,age)
) WITH (
 type='ots',
 instanceName='yourInstanceName',
 tableName='yourTableName',
 accessId='yourAccessId',
 accessKey='yourAccessSecret',
 endPoint='yourEndpoint',
 valueColumns='birthday'
```

); Not e The value of the valueColumns parameter can be the name of any field other than a declared primary key. Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| instanceName | Specifies the name of a Table Store instance. | N/A |
| tableName | Specifies the name of a result table. | N/A |
| endPoint | Specifies the endpoint to access the instance. | Table Store Endpoint, for example http://regionid.example.co m . |
| accessId | Specifies the AccessKey ID. | N/A |
| accessKey | Specifies the AccessKey Secret. | N/A |

|   |   | http://regionid.example.co |
|---|---|---|
|   | m |   |

| ealtime Compute |   | Developer Guide·Flink SQ |
|---|---|---|

| Parameter | Description | Remarks |
|---|---|---|
| valueColumns | Specifies the names of fields to be inserted into the result table. Multiple fields are separated with commas ( , ). | For example, you can insert two fields in the following format: 'ID,NAME' . |
| bufferSize | Specifies the buffer size after data deduplication. | Optional. The default value is 5000, indicating that data output is triggered after 5,000 input data records are processed. |
| batchWriteTimeoutMs | Specifies the timeout period for writing data. | Optional. The default value is 5000, measured in milliseconds. This value indicates that if no data is written to Table Store within 5,000 milliseconds (5 seconds), all cached data is written to the result table. |
| batchSize | Specifies the number of data records that are written at a time. | Optional. The default value is 100. |
| retryIntervalMs | Specifies the retry interval. | Optional. The default value is 1000, measured in milliseconds. |
| maxRetryTimes | Specifies the maximum number of retries for writing data to the result table. | Optional. The default value is 100. |
| ignoreDelete | Specifies whether to skip delete operations. | The default value is false. |

Type mapping

| Table Store data type | Realtime Compute data type |
|---|---|
| INTEGER | BIGINT |
| STRING | VARCHAR |
| BOOLEAN | BOOLEAN |
| DOUBLE | DOUBLE |

Not e You must define a `primary key` in a Table Store result table. Output data is appended to the Table Store result table to update the result.

##### 1.5.3.5 Create an RDS result table

This topic describes how to create a Relational Database Service (RDS) result table for Realtime Compute. This topic also introduces the mapping between Realtime Compute data types and RDS data types. Introduction to RDS ApsaraDB for Relational Database Service (RDS) offers stable, reliable, and scalable online database services. Based on the distributed file system and high-performance storage system developed by Alibaba Cloud, RDS supports a variety of database engines such as MySQL, SQL Server, and PostgreSQL. RDS also supports Postgre Plus Advanced Server (PPAS) that is highly compatible with Oracle databases. RDS provides comprehensive solutions for database operations and management (O&M), including disaster recovery, backup, monitoring, and migration. Not e An RDS result table is consistent with the parameters in the WITH clause. When you create an RDS result table, the RDS data store must have the corresponding table stored in the database. DDL syntax In Realtime Compute, you can use RDS to store output data. Currently, only RDS for MySQL is supported. The sample code is provided as follows:

```
create table rds_output(
 id int,
 len int,
 content varchar,
 primary key(id,len)
) with (
 type='rds',
 url='yourDatabaseURL',
 tableName='yourDatabaseTableName',
 userName='yourDatabaseUserName',
 password='yourDatabasePassword'
```

); Not e In Realtime Compute, each row of output data is converted into a row of strings. The strings are then written into an RDS result table. If you want to write multiple rows of output data at a time, you need to add ? rewriteBatchedStatements=true to the end of the URL. This ensures optimal efficiency when writing multiple rows. For a result table stored in an RDS for MySQL instance, you can define an auto-increment primary key. If you want to use the auto-increment primary key in the result table, do not declare the auto-increment field in the DDL statement. For example, if ID is an autoincrement field in RDS for MySQL, do not declare the ID field in the DDL statement. When writing a row of output data to the database, a value is automatically generated for the auto-increment field. Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| url | Specifies the URL for RDS. | For more information, see Connect to a MySQL instance from a client in RDS for MySQL User Guide. |
| tableName | Specifies the name of a result table. | N/A |
| userName | Specifies the username that is used to access RDS. | N/A |
| password | Specifies the password that is used to access RDS. | N/A |
| maxRetryTimes | Specifies the maximum number of retries for writing data to the result table. | Optional. The default value is 3. |
| batchSize | Specifies the number of data records that are written at a time. | Optional. The default value is 50. |
| bufferSize | Specifies the buffer size after data deduplication. You can only use this parameter when a primary key is defined. | Optional. The default value is 1, indicating that when one data record is processed, an output is generated. The default value is increased to 1000 in Realtime Compute version 1.4.1. |
| flushIntervalMs | Specifies the timeout period of writing data. | Optional. The unit of measurement is milliseconds. The default value is 5000, indicating that if no data is written within 5,000 milliseconds (5 seconds), all cached data is written to the result table. |
| excludeUpdateColumns | Specifies one or more columns to be excluded when you update the result table based on key values. | Optional. The default value is NONE, indicating that only primary key fields are excluded. |
| ignoreDelete | Specifies whether to skip delete operations. | The default value is false. |
| partitionBy | Specifies the partitioning rule for the result table. Before data is written into the result table, Hash partitioning is performed based on a partition key. Data flows to the corresponding node defined by the hash function. | Optional. The default value is NONE. |

Type mapping

| RDS data type | Realtime Compute data type |
|---|---|
| TEXT | VARCHAR |
| BYTE | VARCHAR |
| INTGER | INT |
| LONG | BIGINT |
| DOUBLE | DOUBLE |
| DATE | VARCHAR |
| DATETIME | VARCHAR |
| TIMESTAMP | VARCHAR |
| TIME | VARCHAR |
| YEAR | VARCHAR |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| CHAR | VARCHAR |

JDBC connection parameters

| Parameter | Description | Default value | Since version (JDBC driver) |
|---|---|---|---|
| useUnicode | Specifies whether to use the Unicode character set. If you want to set the characterEncoding parameter to gb2312 or gbk, this parameter must be set to true. | false | 1.1g |
| characterEncoding | Specifies the character encoding when the useUnicode parameter is set to true. You can set this parameter to gb2312 or gbk. | false | 1.1g |

| Parameter | Description | Default value | Since version (JDBC driver) |
|---|---|---|---|
| autoReconnect | Specifies whether to automatically re- establish a connection when the connection to the database is unexpectedly interrupted. | false | 1.1 |
| autoReconnectForPools | Specifies whether to use the reconnection policy for a database connection pool. | false | 3.1.3 |
| failOverReadOnly | Specifies whether to set the connection to read- only after the database is automatically reconnected. | true | 3.0.12 |
| maxReconnects | Specifies the maximum number of connection retries when the autoReconnect parameter is set to true. | 3 | 1.1 |
| initialTimeout | Specifies the interval between two connection retries when the autoReconnect parameter is set to true. The unit of measurement is seconds. | 2 | 1.1 |
| connectTimeout | Specifies the timeout period when you use a socket connection to access the database server. The unit of measurement is seconds. The default value of 0 indicates no timeout (only works on JDK version 1.4 and later). | 0 | 3.0.1 |

| Parameter | Description | Default value | Since version (JDBC driver) |
|---|---|---|---|
| socketTimeout | Specifies the timeout period for a socket- based read/write operation. The unit of measurement is seconds. The value of 0 indicates no timeout. | 0 | 3.0.1 |

FAQ Q: When output data is written to an RDS table, is a new data record generated in the table? If not, is the result table updated based on the primary key value? A: If a primary key is defined in the DDL statement, the result table is updated in the `insert into on` `duplicate key update` method. For a data record, if the value of primary key field does not exist, the record is inserted into the table as a new row. If the value of primary key field exists, the original row of data in the table is updated. If a primary key is not declared in the DDL statement, output data is added to the result table by using the `insert into` method. Q: How can I perform GROUP BY operations based on the unique index of an RDS table? A: An RDS table has only one auto-increment field, which cannot be declared as the primary key in the Realtime Compute DDL statement. If you want to perform GROUP BY operations based on the unique index of an RDS table, declare the unique index in primary key() in the DDL statement.

#### 1.5.4 Create a data dimension table

##### 1.5.4.1 Overview

| PERIOD FOR SYSTEM TIME _ |   | in |
|---|---|---|
| le. | PERIOD FOR SYSTEM TIME _ |   |

You must add `PERIOD FOR SYSTEM_TIME` in the CREATE TABLE statement that is used to create a dimension table. `PERIOD FOR SYSTEM_TIME` defines the period of time when a data record is valid. This means that the table is frequently updated.

```
CREATE TABLE white_list (
   id varchar,
   name varchar,
   age int,
   PRIMARY KEY (id),  -- You must define a primary key for the dimension table.
   PERIOD FOR SYSTEM_TIME -- Defines the period of time when a data record is valid.
   ) with (
   type = 'rds',
   ...
```

`)` Not e When you declare a dimension table, you must specify the primary key. When you join a dimension table with another table, the ON condition must contain an equivalence condition that includes the primary key of either table.

##### 1.5.4.2 Create a Table Store dimension table

This topic describes how to create a Table Store dimension table for Realtime Compute. Table Store is a distributed NoSQL data storage service developed based on the Apsara distributed system. Based on data sharding and load balancing technologies, Table Store has high performance in scaling out and handling concurrent transactions. You can use Table Store to store and query large amounts of structured data. DDL syntax

```
CREATE TABLE ots_dim_table (
 id int,
 len int,
 content VARCHAR,
 PRIMARY KEY (id),
 PERIOD FOR SYSTEM_TIME -- Defines the period of time when a data record is valid. This mea
ns that the table is frequently updated. ) WITH (
 type='ots',
 endPoint='yourEndpoint'
 instanceName='yourInstanceName',
 tableName='yourTableName',
 accessId='yourAccessId',
 accessKey='yourAccessSecret',
```

); Not e When you declare a dimension table, you must specify the primary key. When you join a dimension table with another table, the ON condition must contain an equivalent condition that includes the primary key of either table. The primary key of a Table Store table is the rowkey. Parameters in the WITH clause

| Parameter | Description |
|---|---|
| instanceName | Specifies the name of a Table Store instance. |
| tableName | Specifies the name of a table in the Table Store instance. |
| endPoint | Specifies the endpoint that is used to access the instance. |
| accessId | Specifies the AccessKey ID. |
| accessKey | Specifies the AccessKey Secret. |

Cache parameters

| Parameter | Description | Remarks |
|---|---|---|
| cache | Specifies the cache strategy. | The default value is None. You can set the parameter to LRU. |
| cacheSize | Specifies the cache size. | Specifies the maximum number of data records that can be cached. You can specify this parameter if you set the cache parameter to LRU. The default value is 10000. |
| cacheTTLMs | Specifies the time-to-live (TTL) of each data record that is cached. The TTL is measured in milliseconds. | You can specify this parameter if you set the cache parameter to LRU. No TTL is set by default. |

Sample code

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH ( type='datahub'
```

);

```
CREATE TABLE phoneNumber( name VARCHAR, phoneNumber BIGINT, PRIMARY KEY(name), PERIOD FOR SYSTEM_TIME -- Defines the period of time when a data record is valid. )WITH( type='ots'
```

);

```
CREATE table result_infor( id BIGINT, phoneNumber BIGINT, name VARCHAR )WITH( type='rds'
```

);

```
INSERT INTO result_infor SELECT t.id, w.phoneNumber, t.name FROM datahub_input1 as t JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w -- You must include this clause in t he INSERT INTO statement if you are performing a JOIN query for a dimension table. ON t.name = w.name;
```

##### 1.5.4.3 Create an RDS dimension table

This topic describes how to create an ApsaraDB for RDS dimension table in Realtime Compute. ApsaraDB for RDS offers stable, reliable, and scalable online database services. Based on the distributed file system and high-performance storage services of Apsara Stack, RDS supports a variety of database engines such as MySQL, SQL Server, PostgreSQL, and Postgre Plus Advanced Server (PPAS). PPAS is compatible with Oracle databases. RDS provides a wide range of solutions for database operations and management (O&M), including disaster recovery, backup, restoration, monitoring, and migration. DDL syntax RDS can be used to store dimension tables. Only ApsaraDB RDS for MySQL is supported.

```
CREATE TABLE rds_dim_table(
 id int,
 len int,
 content VARCHAR,
 PRIMARY KEY (id),
 PERIOD FOR SYSTEM_TIME--Indicates that a dimension table is used.
) with (
 type='rds',
 url='rdsDatabaseURL',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
```

); Not e When you declare a dimension table, you must specify the primary key. You can join a dimension table with another table by using a JOIN statement. All the primary key fields of the dimension table must be on the left or right side of the equal operator in the ON clause of the JOIN statement. The primary key of an RDS dimension table can be used as the primary key or unique index of the result table. Parameters in the WITH clause

| Parameter | Description | Remarks |
|---|---|---|
| url | The database URL | N/A |
| tableName | The name of the table in the database | N/A |
| userName | The username that is used to log on to the database | N/A |
| password | The password that is used to log on to the database | N/A |
| maxRetryTimes | The maximum number of INSERT attempts | Optional. The default value is 3. |

Cache parameters

| Parameter | Description | Remarks |
|---|---|---|
| cache | The cache strategy. | The default value is None. Other valid values include LRU and ALL. |
| cacheSize | The cache size. Unit: lines. | If the cache parameter is set to LRU, you must specify the cache size. The default value is 10000. |
| cacheTTLMs | The cache time-out period. Unit: milliseconds. | If the cache parameter is set to LRU, this parameter specifies the time before cache entries expire. By default, cache entries do not expire. If the cache parameter is set to ALL, this parameter specifies the cache refresh interval. By default, cache entries are not refreshed. |
| cacheReloadTimeBlackList | The time periods during which the cache is not refreshed, such as the Double 11. You can specify this parameter only if the cache parameter is set to ALL. | Optional. By default, the parameter is not specified. An example is used to describe the value format: 2017-10-24 14:00 - > 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00. To meet format requirements, separate time periods with commas (,), and separate the start and end time of each period with the right arrow sign (->). |

Not e RDS provides the following three cache strategies: None: indicates that data is not cached. LRU: indicates that the recently used data is cached. If this cache strategy is used, you must specify the cacheSize and cacheTTLMs parameters. ALL: indicates that all data is cached. Before you run a job, all data of the dimension table is loaded into the memory of the operator that runs the JOIN statement. Queries for the dimension table are performed based on the data in the memory. If no result data is found in the memory, no results are returned. All the cached data is refreshed at a specified interval. You can use this cache strategy when a small dimension table is joined with a source table and only a few data records match the condition specified by the ON clause. If this cache strategy is used, you must specify the cacheTTLMs and cacheReloadTimeBlackList parameters. Not e If you set the cache parameter to ALL, Realtime Compute performs asynchronous cache refresh. Therefore, you must increase the memory space of the operator that runs the JOIN statement. The memory space must be twice the size of the dimension table data. If you set the cache parameter to ALL, you must monitor the memory space of the operator to prevent out of memory (OOM) errors. Sample code

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH ( type='datahub'
```

);

```
create table phoneNumber( name VARCHAR, phoneNumber bigint, primary key(name), PERIOD FOR SYSTEM_TIME--Indicates that a dimension table is used. )with( type='rds'
```

);

```
CREATE table result_infor( id bigint, phoneNumber bigint, name VARCHAR )with( type='rds'
```

);

```
INSERT INTO result_infor SELECT t.id ,w.phoneNumber ,t.name FROM datahub_input1 as t JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w--You must add FOR SYSTEM_TIME AS OF PROCTIME() to the end of the dimension table name if you are performing a JOIN operation fo r the dimension table. ON t.name = w.name;
```

### 1.6 DML statements

#### 1.6.1 INSERT INTO statement

This topic describes how to use the INSERT INTO statement in Realtime Compute. Syntax

```
INSERT INTO tableName
        [ (columnName[ , columnName]*) ]
            queryStatement;
```

Example

```
INSERT INTO LargeOrders SELECT * FROM Orders WHERE units > 1000; INSERT INTO Orders(z, v) SELECT c,d FROM OO;
```

A Realtime Compute job created from an SQL file can include multiple DML operations. It also supports multiple data stores for input and output data, and supports multiple dimension tables. For example, a job can contain two paragraphs of SQL statements written for different businesses. You can use SQL statements to write output data into different data stores. In Realtime Compute, you cannot use separate SELECT statements. SELECT statements must be used after CREATE VIEW or INSERT INTO statements. You can update a table by using the INSERT INTO statement. For example, you can use an INSERT INTO statement to write a data record with a key value into an RDS table. If the key value is found in the table, the existing data record in the table is overwritten. If the key value is not found, the data record is added to the table. Table types and statements

| Table type | Statement |
|---|---|
| Source table | You can use the FROM clause. The INSERT INTO statement is not supported. |
| Dimension table | You can use the JOIN statement. The INSERT INTO statement is not supported. |
| Result table | You can only use the INSERT INTO statement. |
| View | You can only use the FROM clause. |

### 1.7 QUERY statements

#### 1.7.1 SELECT statement

You can use the SELECT statement to select data from the table. Syntax

```
SELECT [ DISTINCT ] { * | projectItem [, projectItem ]* } FROM tableExpression;
```

Input example

| a (VARCHAR) | b (INT) | c (DATE) |
|---|---|---|
| a1 | 211 | 1990-02-20 |
| b1 | 120 | 2018-05-12 |

| Developer Guide·Flink SQL |   | Realtime Comput |
|---|---|---|

| a (VARCHAR) | b (INT) | c (DATE) |
|---|---|---|
| c1 | 89 | 2010-06-14 |
| a1 | 46 | 2016-04-05 |

Example 1

```
SELECT * FROM tableName;
```

Out put example

| a (VARCHAR) | b (INT) | c (DATE) |
|---|---|---|
| a1 | 211 | 1990-02-20 |
| b1 | 120 | 2018-05-12 |
| c1 | 89 | 2010-06-14 |
| a1 | 46 | 2016-04-05 |

Example 2

```
SELECT a, c AS d FROM tableName;
```

Input example

| a (VARCHAR) | d (DATE) |
|---|---|
| a1 | 1990-02-20 |
| b1 | 2018-05-12 |
| c1 | 2010-06-14 |
| a1 | 2016-04-05 |

Example 3

```
SELECT DISTINCT a FROM tableName;
```

Out put example a (VARCHAR) a1 b1 a (VARCHAR) c1 Subquery The subquery can be nested in the SELECT statement. In the subquery, the table alias must be used to specify which table reference is to be used. A sample code is provided as follows:

```
INSERT INTO result_table SELECT * from
       (SELECT   t.a,
                 sum(t.b) AS sum_b
                FROM t1 t
                GROUP BY t.a) t1
WHERE t1.sum_b > 100;
```

Out put example

| a (VARCHAR) | b (INT) |
|---|---|
| a1 | 211 |
| b1 | 120 |
| a1 | 257 |

#### 1.7.2 WHERE clause

To specify the condition based on which data is selected from the table, you can add the WHERE clause to the SELECT statement. Syntax

```
SELECT [ ALL | DISTINCT ]
  { * | projectItem [, projectItem ]* }
  FROM tableExpression
  [ WHERE booleanExpression ];
```

The following table describes the operators that can be used in the WHERE clause. Operators

| Operator | Description |
|---|---|
| = | Equal to |
| <> | Not equal to |
| > | More than |

| Developer Guide·Flink SQL | Realtime Comput |
|---|---|

| Operator | Description |
|---|---|
| >= | More than or equal to |
| < | Less than |
| <= | Less than or equal to |

Example Input example

| Address | City |
|---|---|
| Oxford Street | Beijing |
| Fifth Avenue | Beijing |
| Changan Street | Shanghai |

```
SELECT * FROM XXXX WHERE City='Beijing'
```

Output example

| Address | City |
|---|---|
| Oxford Street | Beijing |
| Fifth Avenue | Beijing |

#### 1.7.3 HAVING clause

The WHERE clause cannot be used with aggregate functions. To solve this, you can use a HAVING clause instead. Syntax

```
SELECT [ ALL | DISTINCT ]
  { * | projectItem [, projectItem ]* }
  FROM tableExpression
  [ WHERE booleanExpression ]
  [ GROUP BY { groupItem [, groupItem ]* } ]
  [ HAVING booleanExpression ];
```

Example

| Customer | OrderPrice |
|---|---|
| Bush | 1000 |
| Carter | 1600 |
| Bush | 700 |
| Bush | 300 |
| Adams | 2000 |
| Carter | 100 |

```
SELECT Customer,SUM(OrderPrice) FROM XXX GROUP BY Customer HAVING SUM(OrderPrice)<2000;
```

Output example

| Customer | SUM (OrderPrice) |
|---|---|
| Carter | 1700 |

#### 1.7.4 GROUP BY clause

The GROUP BY clause is used with aggregate functions to split a result set into groups based on one or more columns. Syntax

```
SELECT [ DISTINCT ]
  { * | projectItem [, projectItem ]* }
  FROM tableExpression
  [ GROUP BY { groupItem [, groupItem ]* } ];
```

Example Input example

| Customer | OrderPrice |
|---|---|
| Bush | 1000 |
| Carter | 1600 |
| Bush | 700 |
| Bush | 300 |

| Developer Guide·Flink SQL | Realtime Comput |
|---|---|

| Customer | OrderPrice |
|---|---|
| Adams | 2000 |
| Carter | 100 |

```
SELECT Customer,SUM(OrderPrice) FROM XXXX GROUP BY Customer;
```

Output example

| Customer | SUM (OrderPrice) |
|---|---|
| Bush | 2000 |
| Carter | 1700 |
| Adams | 2000 |

#### 1.7.5 JOIN statement

For JOIN statements, Realtime Compute has the same semantics as BatchCompute. You can use a JOIN statement to join two tables. In Realtime Compute, the two tables are dynamic ones. The result of a JOIN query is dynamically updated. After a specific period, Realtime Compute returns the same result as BatchCompute. Syntax

```
tableReference [, tableReference ]* | tableexpression [ LEFT ] JOIN tableexpression [ joinCondition ];
```

Not e Realtime Compute supports EQUI JOINS. NON EQUI JOINS are not supported. Only INNER JOINS and LEFT OUTER JOINS are supported. The fields and primary key defined in the DDL statement of tables to be joined must exist in the data store. Example 1

```
SELECT o.rowtime, o.productId, o.orderId, o.units,
  p.name, p.unitPrice
  FROM Orders AS o
  JOIN Products AS p
  ON o.productId = p.productId;
```

| rowtime | productId | orderId | units | name | unitPrice |
|---|---|---|---|---|---|
| 10:17:00 | 30 | 5 | 4 | Cheese | 17 |
| 10:17:05 | 10 | 6 | 1 | Beer | 0.25 |
| 10:18:05 | 20 | 7 | 2 | Wine | 6 |
| 10:18:07 | 30 | 8 | 20 | Cheese | 17 |
| 11:02:00 | 10 | 9 | 6 | Beer | 0.25 |
| 11:04:00 | 10 | 10 | 1 | Beer | 0.25 |
| 11:09:30 | 40 | 11 | 12 | Bread | 100 |
| 11:24:11 | 10 | 12 | 4 | Beer | 0.25 |

Example 2 Input example (table name: datahub_stream1)

| a (BIGINT) | b (BIGINT) | c (VARCHAR) |
|---|---|---|
| 0 | 10 | test11 |
| 1 | 10 | test21 |

Input example (table name: datahub_stream2)

| a (BIGINT) | b (BIGINT) | c (VARCHAR) |
|---|---|---|
| 0 | 10 | test11 |
| 1 | 10 | test21 |
| 0 | 10 | test31 |
| 1 | 10 | test41 |

Sample code

```
-- Creates a DataHub source table. create table datahub_stream1 (
 a int,
 b int,
 c varchar
) WITH (
    type='datahub',
    endpoint='yourEndpoint',
    accessId='yourAccessId',
    accessKey='yourAccessSecret',
    projectName='yourProjectName',
    topic='yourTopic',
    project='yourProjectName'
```

);

```
-- Creates another DataHub source table. create table datahub_stream2 (
    a int,
    b int,
    c varchar
) WITH (
    type='datahub',
    endpoint='yourEndpoint',
    accessId='yourAccessId',
    accessKey='yourAccessSecret',
    projectName='yourProjectName',
    topic='yourTopicName',
    project='yourProjectName'
```

);

```
-- Creates an RDS result table. create table rds_output(
     s1_c varchar,
     s2_c varchar
)with(
    type='rds',
    url='yourDatabaseURL',
    tableName='udf',
    userName='yourDatabaseUserName',
    password='yourDatabasePassword'
```

);

```
insert into rds_output select
    s1.c,s2.c
from datahub_stream1 AS s1 join datahub_stream2 AS s2 on s1.a =s2.a where s1.a = 0;
```

Output example

| s1 c (VARCHAR) _ | s2 c (VARCHAR) _ |
|---|---|
| test1 | test11 |

| ealtime Compute | Developer Guide·Flink SQ |
|---|---|

| s1 c (VARCHAR) _ | s2 c (VARCHAR) _ |
|---|---|
| test1 | test31 |

#### 1.7.6 JOIN statement for dimension tables

Introduction Dimension tables are frequently updated. If you want to join a data record with a dimension table, you must specify the creation time of the table snapshot to be used in the JOIN operation. Currently, you can only use the snapshot that is created at the current system time. In the future, Realtime Compute will allow you to use a snapshot created at the time indicated by a value of the rowtime field. Syntax

```
SELECT column-names FROM table1 [AS <alias1>] [LEFT] JOIN table2 FOR SYSTEM_TIME AS OF PROCTIME() [AS <alias2>] ON table1.column-name1 = table2.key-name1
```

Description Dimension tables support INNER JOIN and LEFT JOIN. Dimension tables do not support RIGHT JOIN and FULL JOIN. As shown in the preceding statement, when you join a data record with a dimension table, you must include the `FOR SYSTEM_TIME AS OF PROCTIME()` subclause in the JOIN statement. The subclause indicates that the JOIN operation is performed on the table snapshot created at the current system time. After a data record arrives at the left table, the system searches for matching values in the dimension table and returns the search result. If no search result is found but later a new data record with a matching value is inserted to the dimension table, the previous search result is not updated. JOIN queries work on processing time. Any later operations in the dimension table such as deletion do not change the returned result. An example of joining data records with dimension tables is provided as follows:

```
SELECT e.*, w. * FROM event AS e JOIN white_list FOR SYSTEM_TIME AS OF PROCTIME() AS w ON e.id = w.id
```

Not e In the ON clause, you must specify an equivalent condition that includes the primary key of either table. You can also add other conditions in the ON clause. For example, `ON event.id = white_list.`

```
id AND event.name =white_list.name .
```

You cannot perform JOIN queries between dimension tables. The fields and primary key defined in the DDL statement of a left table must exist in the data store. Example Input example (table name: nameinfor)

| id (BIGINT) | name (VARCHAR) | age (BIGINT) |
|---|---|---|
| 1 | lilei | 22 |
| 2 | hanmeimei | 20 |
| 3 | libai | 28 |

Input example (table name: phoneNumber)

| name (VARCHAR) | phoneNumber (BIGINT) |
|---|---|
| dufu | 18867889855 |
| baijuyi | 18867889856 |
| libai | 18867889857 |
| lilei | 18867889858 |

Sample code

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH ( type='datahub',
```

);

```
create table phoneNumber( name VARCHAR, phoneNumber BIGINT, primary key(name), PERIOD FOR SYSTEM_TIME )with( type='rds'
```

);

```
CREATE table result_infor( id BIGINT, phoneNumber BIGINT, name VARCHAR )with( type='rds'
```

);

```
INSERT INTO result_infor SELECT t.id ,w.phoneNumber ,t.name FROM datahub_input1 as t JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w ON t.name = w.name;
```

Output example

| id (BIGINT) | phoneNumber (BIGINT) | name (VARCHAR) |
|---|---|---|
| 1 | 18867889858 | lilei |
| 3 | 18867889857 | libai |

#### 1.7.7 UNION ALL clause

You can use the UNION ALL clause to merge multiple data streams. Syntax

```
select_statement
  UNION ALL
  select_statement;
```

Not e If you need to merge multiple data streams, the fields of the data streams must have the same data types and sequences. Realtime Compute does not support the UNION clause. The UNION ALL clause returns all merged streaming data records, including duplicates. The UNION statement removes duplicates. Example 1

```
SELECT *
     FROM (
     (SELECT user FROM tableName WHERE a % 2 = 0)
     UNION ALL
     (SELECT user FROM tableName WHERE b = 0)
```

); Example 1 Input example (table name: test_source_union1)

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| test1 | 1 | 10 |

Input example (table name: test_source_union2)

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |

Input example (table name: test_source_union3)

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |
| test1 | 1 | 10 |

Sample code

```
create table test_source_union1 (
 a VARCHAR,
 b BIGINT,
 c BIGINT
) WITH ( type='datahub'
```

```
    type=datahub,
    endpoint='yourEndpoint',
    accessId='yourAccessId',
    accessKey='yourAccessSecret',
    projectName='yourProjectName',
    topic='yourTopicName',
    project='yourProjectName'
```

);

```
create table test_source_union2 (
 a VARCHAR,
 b BIGINT,
 c BIGINT
) WITH (
    type='datahub',
    endpoint='yourEndpoint',
    accessId='yourAccessId',
    accessKey='yourAccessSecret',
    projectName='yourProjectName',
    topic='yourTopicName',
    project='yourProjectName'
```

);

```
create table test_source_union3 (
 a VARCHAR,
 b BIGINT,
 c BIGINT
) WITH (
    type='datahub',
    endpoint='yourEndpoint',
    accessId='yourAccessId',
    accessKey='yourAccessSecret',
    projectName='yourProjectName',
    topic='yourTopicName',
    project='yourProjectName'
```

);

```
create table test_result_union (
    d VARCHAR,
    e BIGINT,
    f BIGINT,
    primary key(d)
) WITH (
      type='rds',
      url='yourDatabaseURL',
      username='yourUserName',
      password='yourPassword',
      tableName='yourTableName'
```

);

```
INSERT into test_result_union SELECT
```

`a,`

```
    sum(b),
    sum(c)
FROM
    (SELECT * from test_source_union1
    UNION ALL
    SELECT * from testsourceunion2
```

`_` `_`

```
    UNION ALL
    SELECT * from test_source_union3
```

`)t`

```
 GROUP BY a;
```

Output example

| d (VARCHAR) | e (BIGINT) | f (BIGINT) |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |
| test1 | 2 | 20 |
| test1 | 3 | 30 |
| test2 | 4 | 40 |
| test1 | 4 | 40 |

#### 1.7.8 Top_N statement

You can use the Top_N statement to retrieve the largest or smallest N data records from data streams based on the specified metric. In Flink SQL, you can define an over window to perform Top_N queries. Syntax

```
SELECT * FROM (
  SELECT *,
    ROW_NUMBER() OVER ([PARTITION BY col1[, col2..]]
    ORDER BY col1 [asc|desc][, col2 [asc|desc]...]) AS rownum
  FROM table_name)
WHERE rownum <= N [AND conditions]
```

The parameters are described as follows: `ROW_NUMBER()` : specifies an over window to compute the row number. The value of the row number starts from 1. `PARTITION BY col1[, col2..]` : optional. Specifies one or more columns based on the data records that are partitioned. ORDER BY col1 [asc|desc][, col2 [asc|desc]...] : specifies one or more columns based on which the rows in a partition are ordered. You can define different ordering directions for different columns. As indicated by the syntax, the query includes two steps. In the first step, the `ROW_NUMBER()` function is used to specify an over window to compute the row number for the rows that are ordered in a partition. The second step is to return the top N data records. For example, if N is 10, only the top 10 data records are returned. When you use Flink SQL to perform Top_N queries, input data records are ordered and ranked based on the specified columns. If the top N data records in a partition change, the changed data records are sent to the downstream data store to update the result. You can only export the top N data records to a result table that is defined with a primary key. The Top_N statement has specific constraints. To allow Flink SQL to identify a Top_N query, you must

| specify the | rownum <= N |   |
|---|---|---|
| rownum - 5 <= N |   | to spe |

specify the `rownum <= N` condition in the WHERE clause. You cannot use an expression such as `rownum - 5 <= N` to specify a condition. If you specify multiple conditions in the WHERE clause, you must use AND to separate the conditions. Example 1 You can use the following example to return the top 100 keywords that are most queried in a city within an hour. For the result table, you must define the rownum, start_time, and city columns as the composite primary key. The composite primary key can uniquely identify a data record.

```
CREATE TABLE rds_output (
  rownum int,
  start_time bigint,
  city varchar,
  keyword varchar,
  pv bigint,
  PRIMARY KEY (rownum, start_time, city)
) with (
  type = 'rds',
  ...
```

`)`

```
INSERT INTO rds_output SELECT rownum, start_time, city, keyword, pv FROM (
  SELECT *,
     ROW_NUMBER() OVER (PARTITION BY start_time, city ORDER BY pv desc) AS rownum
  FROM (
        select substr(time_str,1,12) as start_time,
            keyword,
            count(1) AS pv,
            city
        from tmp_search
        group by substr(time_str,1,12), keyword, city
    ) a
```

`)`

```
WHERE rownum <= 100
```

Example 2 Input example

| ip (varchar) | time (varchar) |
|---|---|
| 192.168.1.1 | 100000000 |
| 192.168.1.2 | 100000000 |

| Developer Guide·Flink SQL | Realtime Comput |
|---|---|

| ip (varchar) | time (varchar) |
|---|---|
| 192.168.1.2 | 100000000 |
| 192.168.1.3 | 100030000 |
| 192.168.1.3 | 100000000 |
| 192.168.1.3 | 100000000 |

Sample code

```
create table source_table (
  IP VARCHAR,
  `TIME` VARCHAR
)with(
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyuncs.com',
  project='Flink_test',
  topic='yourTopicName',
  accessId='yourAccessId',
  accessKey='yourAccessSecret'
```

);

```
create table result_table (
  rownum int,
  start_time VARCHAR,
  IP VARCHAR,
  cc BIGINT,
  PRIMARY KEY (start_time, IP)
) with (
  type = 'rds',
  url='jdbc:mysql://rm-bp1gz4k202t8****s.com:3306/Flink_test',
  tableName='yourTableName',
  userName='yourAccessId',
  password='yourAccessPassword'
```

);

```
INSERT INTO result_table SELECT rownum,start_time,IP,cc FROM (
  SELECT *,
     ROW_NUMBER() OVER (PARTITION BY start_time ORDER BY cc desc) AS rownum
  FROM (
        SELECT SUBSTRING(`TIME`,1,2) AS start_time, -- The input example of the TIME parame
ter is provided in the preceding table. You can change the value of the TIME parameter base d on your situation.
        COUNT(IP) AS cc,
```

`IP`

```
        FROM  source_table
        GROUP BY SUBSTRING(`TIME`,1,2), IP
```

`)a` `)`

```
WHERE rownum <= 3 -- You can change the number 3 based on your situation.
```

| rownum (INT) | start time (VARCHAR) _ | ip (VARCHAR) | cc (BIGINT) |
|---|---|---|---|
| 1 | 10 | 192.168.1.3 | 6 |
| 2 | 10 | 192.168.1.2 | 4 |
| 3 | 10 | 192.168.1.1 | 2 |

No ranking number optimization As indicated by the syntax, the rownum field is written to the result table as one field of the primary key. Many repeated data records may be written to the result table. For example, if a data record with the ninth rank is updated and its rank is changed to the first, all top 9 data records are updated to the result table. During the process, workloads increase significantly for the result table. To resolve this issue, you can discard the rownum field when data records are written to the result table. In most cases, consumers can compute row numbers themselves because the number of top N data records is small. In the preceding example, only the changed records are updated for the result table, rather than nine records. This method helps to significantly reduce the workload for the result table. Synt ax

```
SELECT col1, col2, col3 FROM (
 SELECT col1, col2, col3
   ROW_NUMBER() OVER ([PARTITION BY col1[, col2..]]
   ORDER BY col1 [asc|desc][, col2 [asc|desc]...]) AS rownum
 FROM table_name)
WHERE rownum <= N [AND conditions]
```

Different from the original Top_N syntax, you need to exclude the rownum field from the second step of the query. Not e If the rownum field is excluded, use caution while defining the primary key for the result table. If the definition is inaccurate, a Top_N query may return inconsistent results. Without the rownum field, the primary key of the result table must be the same as the GROUP BY key that is defined before the Top_N operator. Example The following example describes a simplified business scenario for Youku. On Youku, each video generates large amounts of traffic after it is published. The most popular videos can be identified by analyzing the traffic generated by videos. You can return the top 5 videos that generate the most traffic per minute by using the following code.

```
-- Reads data from a Log Service source table. CREATE TABLE sls_cdnlog_stream ( vid VARCHAR, -- video id rowtime timestamp, -- Defines the time when the video is played. response_size BIGINT, -- Defines the traffic generated by the video. WATERMARK FOR rowtime as withOffset(rowtime, 0) ) WITH ( type='sls', ...
```

);

```
-- Defines a one-minute window to aggregate the bandwidth consumed by the video. CREATE VIEW cdnvid_group_view AS SELECT vid, TUMBLE_START(rowtime, INTERVAL '1' MINUTE) AS start_time, SUM(response_size) AS rss FROM sls_cdnlog_stream GROUP BY vid, TUMBLE(rowtime, INTERVAL '1' MINUTE); -- Creates the result table. CREATE TABLE hbase_out_cdnvidtoplog ( vid VARCHAR, rss BIGINT, start_time VARCHAR,
   -- Do not define the rownum field in the result table.
   -- Note that the primary key of the result table must be the same as the GROUP BY key th
at is defined before the Top_N operator. PRIMARY KEY(start_time, vid) ) WITH ( type='RDS', ...
```

);

```
-- Computes and exports the top 5 videos that generate the most traffic per minute. INSERT INTO hbase_out_cdnvidtoplog -- Excludes the rownum field from the second step of the query. SELECT vid, rss, start_time FROM
```

`(`

```
SELECT vid, start_time, rss, ROW_NUMBER() OVER (PARTITION BY start_time ORDER BY rss DESC) as rownum, FROM cdnvid_group_view
```

`)`

```
WHERE rownum <= 5;
```

Input example

| vid (VARCHAR) | rowtime (TIMESTAMP) | response size (BIGINT) _ |
|---|---|---|
| 10000 | 2017-12-18 15:00:10 | 2000 |
| 10000 | 2017-12-18 15:00:15 | 4000 |
| 10000 | 2017-12-18 15:00:20 | 3000 |

| R | ealtime Compute |   | Developer Guide·Flink SQ | L |
|---|---|---|---|---|

| vid (VARCHAR) | rowtime (TIMESTAMP) | response size (BIGINT) _ |
|---|---|---|
| 10001 | 2017-12-18 15:00:20 | 3000 |
| 10002 | 2017-12-18 15:00:20 | 4000 |
| 10003 | 2017-12-18 15:00:20 | 1000 |
| 10004 | 2017-12-18 15:00:30 | 1000 |
| 10005 | 2017-12-18 15:00:30 | 5000 |
| 10006 | 2017-12-18 15:00:40 | 6000 |
| 10007 | 2017-12-18 15:00:50 | 8000 |

Out put example

| start time (VARCHAR) _ | vid (VARCHAR) | rss (BIGINT) |
|---|---|---|
| 2017-12-18 15:00:00 | 10000 | 9000 |
| 2017-12-18 15:00:00 | 10007 | 8000 |
| 2017-12-18 15:00:00 | 10006 | 6000 |
| 2017-12-18 15:00:00 | 10005 | 5000 |
| 2017-12-18 15:00:00 | 10002 | 4000 |

#### 1.7.9 Complex event processing (CEP)

You can use the MATCH_RECOGNIZE clause to identify the events that match the specified pattern from data streams and export matched events by using a specified method. Syntax

```
SELECT [ ALL | DISTINCT ] { * | projectItem [, projectItem ]* } FROM tableExpression [MATCH_RECOGNIZE ( [PARTITION BY {partitionItem [, partitionItem]*}] [ORDER BY {orderItem [, orderItem]*}] [MEASURES {measureItem AS col [, measureItem AS col]*}] [ONE ROW PER MATCH|ALL ROWS PER MATCH|ONE ROW PER MATCH WITH TIMEOUT ROWS|ALL ROWS PER MATC H WITH TIMEOUT ROWS] [AFTER MATCH SKIP] PATTERN (patternVariable[quantifier] [ patternVariable[quantifier]]*) WITHIN intervalExpres sion DEFINE {patternVariable AS patternDefinationExpression [, patternVariable AS patternDefinat ionExpression]*} )];
```

| Clause | Description |
|---|---|
| PARTITION BY | Optional. You can use the PARTITION BY clause to divide the rows of an input table into partitions based on one or more columns. |
| ORDER BY | Optional. You can use the ORDER BY clause to order the rows within a partition based on one or more columns. If you use multiple columns to order the rows, define EVENT TIME or PROCESSING TIME as the first column. |
| MEASURES | You can use the MEASURES clause to define a list of columns for an output table. You can create an expression to compute a value for each column that you have defined. |
| ONE ROW PER MATCH | Specifies that only one summary row is generated for a pattern match. |
| ONE ROW PER MATCH WITH TIMEOUT ROWS | Specifies that both a pattern match and timeout can trigger output. In the PATTERN clause, you can use the WITHIN subclause to define a timeout period. |
| ALL ROWS PER MATCH | Specifies that for a pattern match that spans multiple rows, each input row triggers one output row. |
| ALL ROWS PER MATCH WITH TIMEOUT ROWS | Specifies that both a pattern match and timeout can trigger output. In the PATTERN clause, you can use the WITHIN subclause to define a timeout period. |
| [ONE ROW PER MATCH\|ALL ROWS PER MATCH\|ONE ROW PER MATCH WITH TIMEOUT ROWS\|ALL ROWS PER MATCH WITH TIMEOUT ROWS] | Optional. The default value is ONE ROW PER MATCH . |
| AFTER MATCH SKIP TO NEXT ROW | Specifies that pattern matching resumes from the next row that follows the first row of the current match. |
| AFTER MATCH SKIP PAST LAST ROW | Specifies that pattern matching resumes from the next row that follows the last row of the current match. |
| AFTER MATCH SKIP TO FIRST patternItem | Specifies that pattern matching resumes from the first row that is mapped to the pattern item. |
| AFTER MATCH SKIP TO LAST patternItem | Specifies that pattern matching resumes from the last row that is mapped to the pattern item. |

|   | TIME |
|---|---|

| ROWS PER | MATCH |
|---|---|

| Clause | Description |
|---|---|
| PATTERN | You can use the PATTERN clause to specify a regular expression that defines the pattern to be matched. The regular expression is enclosed in parentheses () . You can specify multiple pattern variables in the clause. Not e If you use a space to separate two pattern variables, no rows are allowed between the two rows that are mapped to the pattern variables. If you use a -> string to separate two pattern variables, rows are allowed between the two rows that are mapped to the pattern variables. |

Quantifiers

|   | Quantifiers |   |
|---|---|---|
| ern variable |   | . |

`Quantifiers` are used to define the number of iterations for the rows that are mapped to a `patt`

| Quantifier | Description |
|---|---|
| * | Zero or more iterations |
| + | One or more iterations |
| ? | Zero or one iteration |
| {n} | n iterations (n > 0) |
| {n,} | n or more iterations (n ≥ 0) |
| {n, m} | From n to m iterations (0 ≤ n ≤ m, 0 < m) |
| {,m} | Between 0 and m iterations (m > 0) |

| ple, if you define | A -> B+ | in |
|---|---|---|
| a b1, a b1 b2, a b1 b2 b3 |   |   |

reluctant, you can add a question mark ( ? ) after the quantifier. Supported reluctant quantifiers are listed as follows: *? +?

```
 {n}?
 {n,}?
 {n, m}?
```

```
 {,m}?
```

In the preceding example, if you use a reluctant quantifier instead, the output is `a b1, a b2, a b1`

```
b2, a b3, a b2 b3, a b1 b2 b3 .
```

| Not e You can use the WITHIN clause to define the maximum time span of the rows that match the pattern. Syntax of a static window: INTERVAL 'string' timeUnit [ TO timeUnit ] . Example: INTERVAL '10' SECOND, INTERVAL '45' DAY, INTERVAL '10:20' MINUTE TO SECOND, INTERV |   |   |   |
|---|---|---|---|
|   | INTERVAL '10' SECOND, INTERVAL '45' DAY, INTERVAL '10:20' MINUTE TO SECOND, INTERV |   |   |
| AL '10:20.10' MINUTE TO SECOND, INTERVAL '10:20' HOUR TO MINUTE, INTERVAL '1-5' YE |   |   |   |
| AR TO MONTH . Syntax of a dynamic window: INTERVAL intervalExpression . Example: INTERVAL A.wi ndowTime + 10 , in which A represents the first pattern variable defined in the PATTERN clause. In an interval expression, you can use the pattern variables defined in the PATTERN clause. Only the first pattern variable can be used. You can use a UDF for an interval expression. The result of the expression indicates the window size (time span), measured in milliseconds. The data type of the result must be LONG. You can use the DEFINE clause to specify the definition of a pattern variable. If a pattern variable is not defined in the DEFINE clause, any row can be mapped to the pattern variable. |   |   |   |

| INTERVAL A.wi |   |
|---|---|

|   | ndowTime + 10 |
|---|---|

Functions in the MEASURES and DEFINE clauses

| Function | Description |
|---|---|
| Row pattern column references | Syntax: patternVariable.col . You can use a row pattern column reference to reference the column in all rows that match a pattern variab le . |
| PREV | You can only use the PREV function in the DEFINE clause. In most cases, the function is used with r ow pattern column references . You can use the PREV function to reference the value of a column in a previous row based on an offset from the current row. Example: DOWN AS DOWN.price < PREV(DOWN.price) . In this example, PREV(DO WN.price) indicates the value of the price column in the previous row. Note that DOWN.pric e is equivalent to PREV(DOWN.price, 0) . P REV(DOWN.price) is equivalent to PREV(DOWN. price, 1) . |

| pattern variab |   |
|---|---|

|   | le |
|---|---|

|   | ow pattern column references |
|---|---|

|   | DOWN AS DOWN.price |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | PREV(DO |   |   |   |   |
|   |   |   |   | price |   |   |   |   |   |
|   |   |   | DOWN.pric |   |   |   |   |   |   |
| PREV(DOWN.price, 0) |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | . | P |   |   |

|   |   | < PREV(DOWN.price) |
|---|---|---|
|   |   | WN.price) |

|   |   |   | e |
|---|---|---|---|
|   |   |   | price, 1) |

| Function | Description |
|---|---|
| FIRST and LAST | In most cases, the FIRST and LAST functions are used with row pattern column references . You can use these functions to reference the value of a column in a row based on an offset from the first or last row that matches a pattern variab le . For example, FIRST(A.price, 3) indicates the value of the price column in the fourth row that matches Pattern Variable A . LAST(A.price, 3) indicates the value of the price column in the fourth row from the last row that matches Pattern Variable A . |

| pattern variab |   |
|---|---|

|   | le |
|---|---|

|   | Pattern Variable |
|---|---|
| LAST(A.price, 3) |   |

|   | A |
|---|---|

Output methods

| Output method | Description |
|---|---|
| ONE ROW PER MATCH | Output columns include the columns specified in the PARTITION BY and MEASURES clauses. If a column is specified in the PARTITION BY clause, you do not need to define the column again in the MEASURES clause. |
| ONE ROW PER MATCH WITH TIMEOUT ROWS | A pattern match and timeout can both trigger output. In the PATTERN clause, you can use the WITHIN subclause to define a timeout period. |

Not e When you define a pattern, you need to define a timeout period for rows that match the pattern. Otherwise, the state may be overwhelming. In the ORDER BY clause, you must define EVENT TIME or PROCESSING TIME as the first column. Example Syntax

```
SELECT * FROM Ticker MATCH_RECOGNIZE ( PARTITION BY symbol ORDER BY tstamp MEASURES STRT.tstamp AS start_tstamp, LAST(DOWN.tstamp) AS bottom_tstamp, LAST(UP.tstamp) AS end_tstamp ONE ROW PER MATCH AFTER MATCH SKIP TO NEXT ROW PATTERN (STRT DOWN+ UP+) WITHIN INTERVAL '10' SECOND DEFINE DOWN AS DOWN.price < PREV(DOWN.price), UP AS UP.price > PREV(UP.price) ) MR ORDER BY MR.symbol, MR.start_tstamp;
```

Input example

| timestamp (TIMESTAMP) | card id (VARCHAR) _ | location (VARCHAR) | action (VARCHAR) |
|---|---|---|---|
| 2018-04-13 12:00:0 0 | 1 | WW | Tom |
| 2018-04-13 12:05:0 0 | 1 | WW1 | Tom |
| 2018-04-13 12:10:0 0 | 1 | WW2 | Tom |
| 2018-04-13 12:20:0 0 | 1 | WW | Tom |

|   | 2018-04-13 12:00:0 |   |
|---|---|---|
| 0 |   |   |

|   | 2018-04-13 12:05:0 |   |
|---|---|---|
| 0 |   |   |

|   | 2018-04-13 12:10:0 |   |
|---|---|---|
| 0 |   |   |

|   | 2018-04-13 12:20:0 |   |
|---|---|---|
| 0 |   |   |

Sample code

```
CREATE TABLE datahub_stream (
    `timestamp`               TIMESTAMP,
    card_id                   VARCHAR,
    location                  VARCHAR,
    `action`                  VARCHAR,
    WATERMARK wf FOR `timestamp` AS withOffset(`timestamp`, 1000)
) WITH (
    type = 'datahub'
    ...
```

);

```
CREATE TABLE rds_out (
    start_timestamp               TIMESTAMP,
    end_timestamp                 TIMESTAMP,
    card_id                       VARCHAR,
    event                         VARCHAR
) WITH (
    type= 'rds'
    ...
```

);

```
-- Example -- When a credit card specified with a unique card_id is found to have two payment record s in different locations within 10 minutes, an alert is triggered. This helps to monitor the unauthorized use of credit cards. -- Defines the computational logic as follows: insert into rds_out select `start_timestamp`, `end_timestamp`, card_id, `event` from datahub_stream MATCH_RECOGNIZE (
    PARTITION BY card_id   -- Partitions rows by the card_id column. The rows with the sa
me card ID are allocated to the same compute node.
    ORDER BY `timestamp`   -- Orders the rows in a partition based on time.
    MEASURES               -- Defines a list of columns for an output table. You can crea
te an expression to compute values for each column that you have defined.
        e2.`action` as `event`,
        e1.`timestamp` as `start_timestamp`,   -- Defines the time of e1 as start_timesta
mp.
        LAST(e2.`timestamp`) as `end_timestamp`-- Defines the time of e2 as end_timestamp
```

`.`

```
    ONE ROW PER MATCH           -- Each match generates an output row.
    AFTER MATCH SKIP TO NEXT ROW-- Resumes the pattern matching from the row that follows
the first row of the current match.
    PATTERN (e1 e2+) WITHIN INTERVAL '10' MINUTE  -- Defines two pattern variables: e1 an
d e2.
    DEFINE                     -- Specifies the conditions for the pattern variables defi
ned in the PATTERN clause.
        e1 as e1.action = 'Tom',    -- Defines the action of e1 as Tom.
        e2 as e2.action = 'Tom' and e2.location <> e1.location -- Defines the action of e
2 as Tom. The locations of e1 and e2 are different.
```

);

| start timestamp _ (TIMESTAMP) |   |   |   | end timestamp _ (TIMESTAMP) |   |   | card id (VARCHAR) _ | event (VARCHAR) |
|---|---|---|---|---|---|---|---|---|
| 2018-04-13 20:00:0 |   |   |   |   |   |   | 1 | Tom |
|   | 2018-04-13 20:00:0 |   |   |   |   | 2018-04-13 20:05:0 | 1 |   |
| 0.0 |   |   |   |   |   |   |   |   |
|   |   |   |   | 0.0 |   |   |   |   |
| 2018-04-13 20:05:0 |   |   |   |   |   |   | 1 | Tom |
|   | 2018-04-13 20:05:0 |   |   |   |   | 2018-04-13 20:10:0 | 1 |   |
| 0.0 |   |   |   |   |   |   |   |   |
|   |   |   |   | 0.0 |   |   |   |   |

### 1.8 Create a view

In Realtime Compute, you can define a view to query data in one or more tables in a database. You can simplify the development process by using views. A view displays a logical table that helps to describe the computational logic. It does not physically store any data. To simplify queries, you can use the SQL statement to define a manageable view. A view can be created based on fields of one or more tables in a database. Views do not require any disk space. Syntax

```
CREATE VIEW viewName
        [ (columnName[ , columnName]*) ]
            AS queryStatement;
```

Example 1

```
 CREATE VIEW  LargeOrders(r, t, c, u) AS
  SELECT rowtime,
    productId,
```

`c,`

```
    units
  FROM Orders;
  INSERT INTO rds_output
  SELECT
  r,t,c,u
  FROM LargeOrders;
```

Example 2 Input example

| a (VARCHAR) | b (BIGINT) | c (TIMESTAMP) |
|---|---|---|
| test1 | 1 | 1506823820000 |
| test2 | 1 | 1506823850000 |
| test1 | 1 | 1506823810000 |
| test2 | 1 | 1506823840000 |

| ealtime Compute |   | Developer Guide·Flink SQ |
|---|---|---|
| a (VARCHAR) | b (BIGINT) | c (TIMESTAMP) |
| test2 | 1 | 1506823870000 |
| test1 | 1 | 1506823830000 |
| test2 | 1 | 1506823860000 |

Sample code

```
CREATE TABLE datahub_stream ( a VARCHAR, b BIGINT, c TIMESTAMP, d AS PROCTIME() ) WITH (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyuncs.com',
  project='blink_test',
  topic='window_count',
  accessId='yourAccessId',
  accessKey='yourAccessSecret'
```

);

```
CREATE TABLE rds_output ( a varchar, b TIMESTAMP, cnt BIGINT, PRIMARY KEY(a) )with(
  type = 'rds',
  url='jdbc:mysql://rm-bp1gz4k20****.mysql.rds.aliyuncs.com:3306/****',
  tableName='yourTableName',
  userName='yourAccessUserName',
  password='yourAccessPassword'
```

);

```
CREATE VIEW rds_view AS SELECT a,
   CAST(HOP_START(d, interval '5' second, interval '30' second) AS TIMESTAMP) AS cc,
   sum(b) AS cnt
FROM datahub_stream GROUP BY HOP(d, interval '5' second, interval '30' second),a; INSERT INTO rds_output SELECT
```

`a,`

```
cc, cnt FROM rds_view WHERE cnt=4
```

| a (VARCHAR) | b (TIMESTAMP) | cnt (BIGINT) |
|---|---|---|
| test2 | 2017-11-06 16:54:10 | 4 |

### 1.9 Window functions

#### 1.9.1 Overview

You can use Flink SQL to aggregate infinite streaming data without defining any window in SQL statements. You can also define a window to aggregate a set of streaming data records as required. For example, you need to calculate the page view for a webpage in the past one minute. You can define a window in the SQL statement to collect data in the past minute and compute the aggregate result. In Flink SQL, you can aggregate data by using group windows and over windows. The core difference is that when you use over windows, each input data record triggers an aggregate and has an aggregate result. Therefore, over windows are applied to ranking, calculating a moving average, and other scenarios. You can aggregate data by using group windows based on two time attributes: event time and processing time. Three types of group windows are available: tumbling window, sliding window, and session window. Time attributes Flink SQL supports the following time attributes: event time and processing time. Event time is the time when a data record is created. You must define the event time in the table schema. Processing time is the local time of the system when the system processes an event. Positions of different time attributes in the workflow of Realtime Compute Ingestion time and processing time are the time attributes automatically generated by the system for a streaming data record. Event time is a time attribute that is carried by a steaming data record. Assume that the event time for a streaming data record is t1, and the event time for another streaming data record is t2 (t2 > t1). The first data record may arrive and be processed by Flink later than the second data record because of data disorder, network jitter, or other reasons. Processing time-based aggregate Processing time is generated by the system and is not included in source data received from data stores. Therefore, you need to define a processing time in a DDL statement as follows:

```
filedName as PROCTIME()
```

An example of processing time-based aggregate is provided as follows:

```
CREATE TABLE tt_stream (
    a VARCHAR,
    b VARCHAR,
    c BIGINT,
    d AS PROCTIME()
    ) with (
    type = 'sls',
    topic = 'yourTopicName',
    accessId = 'yourAccessId',
    accessKey = 'yourAccessSecret'
```

);

```
    CREATE TABLE rds_output (
    id VARCHAR,
    c TIMESTAMP,
    f TIMESTAMP,
    cnt BIGINT
    ) with (
    type = 'rds',
    url = 'yourDatebaseURL',
    tableName='yourTableName',
    userName='yourDatabaseUserName',
    password='yourDatabasePassword'
```

);

```
    INSERT INTO rds_output
    SELECT a AS id,
    SESSION_START(d, INTERVAL '1' SECOND) AS c,
    SESSION_END(d, INTERVAL '1' SECOND) AS f,
    COUNT(a) AS cnt
    FROM tt_stream
    GROUP BY SESSION(d, INTERVAL '1' SECOND), a
```

Event time-based aggregate Event time is included in source data received from data stores. You do not need to define an event time in a DDL statement. However, you must use the watermarking mechanism to handle out-of-order data. If you do not define a watermark, data that arrives late may not be processed and the aggregate result is inaccurate. Wat ermark Watermarking is a mechanism in Flink to measure progress in event time. A watermark flows as part of the data stream and carries a timestamp. A watermark is defined in a DDL statement. You can use the following syntax to define a watermark in Flink:

```
WATERMARK [watermarkName] FOR <rowtime_field> AS withOffset(<rowtime_field>, offset)
```

`watermarkName` : specifies the watermark name. This parameter is optional. `<rowtime_field>` : specifies a column (of the `TIMESTAMP` data type) that is used to generate a watermark. This column is labeled as the event time column. When you perform queries by using window functions, you must include a time attribute column in your table. `withOffset` : specifies the strategy of generating a waterwark. The value for a watermark is obtained based on `<rowtime_field> - offset` . The first parameter in withOffset must be `<rowti`

| me field> _ |   |   |
|---|---|---|
|   | offset | : |

`offset` : specifies the offset between a watermark value and an event time. The unit is measured in milliseconds. For example, a table has a rowtime column of the TIMESTAMP data type, and one value is 1501750584000 (2017-08-03 08:56:24.000). Based on the preceding rowtime column, you can define a watermark with a four-second offset as follows:

```
WATERMARK FOR rowtime AS withOffset(rowtime, 4000)
```

The watermark value of the specified data record is obtained based on the following expression: 1501750584000 - 4000 = 1501750580000 (2017-08-03 08:56:20.000). The watermark indicates that all data with the timestamps earlier than 1501750580000 (2017-08-03 08:56:20.000) has arrived. Not e When you define a watermark based on event time, the data type of the rowtime column must be TIMESTAMP. Currently, Realtime Compute only supports 13-bit Unix timestamps measured in milliseconds. If the data type of a rowtime column is not TIMESTAMP or a Unix timestamp is not 13 digits in length, we recommend that you use a computed column expression to convert data types. You can only define event time and processing time in a DDL statement that is used to create a source table. Summary: A watermark indicates that all the events with the timestamps (t') earlier than the watermark (t) have occurred. After a watermark takes effect, all subsequent records with timestamps earlier than the watermark are discarded. This is the current watermarking mechanism in Realtime Compute. However, in the future, improvements to Realtime Compute will allow you to update subsequent data. The watermarking mechanism is crucial for handling out-of-order data streams. With watermarks, real-time computing results are accurate even if data streams arrive out of order. When an operator has multiple input data streams, the event time of the operator equals the minimum event time of the data streams. Diagram of watermarks in parallel data streams Example of event time-based Aggregation

```
CREATE TABLE tt_stream(
     a VARCHAR,
     b VARCHAR,
     c TIMESTAMP,
     WATERMARK wk1 FOR c as withOffset(c, 1000)
     ) with (
     type = 'sls',
     topic = 'blink_tt2tt_test',
     accessId = 'yourAccessId',
     accessKey = 'yourAccessSecret'
```

);

```
     CREATE TABLE rds_output (
     id VARCHAR,
     c TIMESTAMP,
     f TIMESTAMP,
     cnt BIGINT
     ) with (
     type = 'rds',
     url = 'yourDatebaseURL',
     tableName='yourDatabaseTableName',
     userName='yourDatabaseUserName',
     password='yourDatabasePassword'
```

);

```
     INSERT INTO rds_output
     SELECT a AS id,
     SESSION_START(c, INTERVAL '1' SECOND) AS c,
     CAST(SESSION_END(c, INTERVAL '1' SECOND) AS TIMESTAMP) AS f,
     COUNT(a) AS cnt
     FROM tt_stream
     GROUP BY SESSION(c, INTERVAL '1' SECOND), a
```

#### 1.9.2 Session window

A session window groups elements by sessions of activities. Unlike tumbling windows and sliding windows, session windows do not overlap and are not fixed in size. If a session window does not receive any elements within a certain period, the session is disconnected and the window is closed. A session window is configured by using a gap duration, which defines the required length of an inactive period. For example, a data stream that describes click activities may include highly clustered click events, separated by inactive periods. The data that arrives after a specified gap duration is assigned to a new window. Session window shows a session window. Note that each key has different types of windows due to the irregular distribution of elements. Syntax The SESSION function is used to define a session window in a GROUP BY clause.

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

Not e

```
The <time-attr> parameter specifies a time attribute based on which a computation is pe rformed. The time attribute is processing time or event time.
```

Window identifier functions A window identifier function specifies the start or end time of a window, or the window time attribute. The returned time attribute is used for window joins. Window identifier functions

| Window identifier function | Return type | Description |
|---|---|---|
| SESSION START(time-attr, size- _ interval) | TIMESTAMP | Returns the start time (the boundary value is included) of the window. For example, if the window is [00:10, 00:15), 00:10 is returned. |
| SESSION END(time-attr, size- _ interval) | TIMESTAMP | Returns the end time (the boundary value is included) of the window. For example, if the window is [00:00, 00:15], 00:15 is returned. |
| SESSION ROWTIME(time-attr, _ size-interval) | TIMESTAMP | Returns the end time (the boundary value is excluded) of the window. For example, if the window is [00:00, 00:15], 00:14:59.999 is returned. The return value is a rowtime attribute, based on which time- based operations such as window joins can be performed. |

Example The following example describes how to compute the number of clicks per user during each active session. The session timeout interval is 30 seconds.

```
CREATE TABLE user_clicks(
  username varchar,
  click_url varchar,
  ts timeStamp,
  WATERMARK wk FOR ts as withOffset(ts, 2000)  -- Defines a watermark for rowtime.
) with (
  type='datahub',
  ...
```

);

```
CREATE TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  type='rds'
```

);

```
INSERT INTO tumble_output SELECT
  SESSION_START(ts, INTERVAL '30' SECOND),
  SESSION_END(ts, INTERVAL '30' SECOND),
  username,
  COUNT(click_url)
FROM window_input GROUP BY SESSION(ts, INTERVAL '30' SECOND), username
```

Input example

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

Output example

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:00:00.0 | 2017-10-10 10:00:40.0 | Jark | 2 |
| 2017-10-10 10:00:49.0 | 2017-10-10 10:01:19.0 | Jark | 2 |
| 2017-10-10 10:01:58.0 | 2017-10-10 10:02:28.0 | Jark | 1 |

| ealtime Compute |   |   | Developer Guide·Flink SQ |
|---|---|---|---|

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:02:10.0 | 2017-10-10 10:02:40.0 | Timo | 1 |

#### 1.9.3 Sliding window

Unlike tumbling windows, sliding windows can overlap each other. Sliding windows have two parameters: size and slide. The size parameter specifies the size of a window. The slide parameter defines how frequently a sliding window is started. If the slide is smaller than the window size, sliding windows can overlap each other. In this case, elements are assigned to multiple windows. If the slide is equal to the size, windows do not overlap and can be considered as tumbling windows. If the slide is greater than the size, windows can be considered as tumbling windows that are separated by gaps. In most cases, multiple windows overlap and most elements are assigned to multiple windows. This type of window is useful in computing moving averages. For example, if the average value of data over the past five minutes needs to be computed every 10 seconds, you can set the size to five minutes and the slide to 10 seconds. The Sliding window figure shows a one-minute window that slides every 30 seconds. Syntax The HOP function is used to define a sliding window in a GROUP BY clause.

```xml
HOP(<time-attr>, <slide-interval>, <size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

Not e

```
The <time-attr> parameter specifies a time attribute based on which a computation is pe rformed. The time attribute is processing time or event time.
```

Window identifier function A window identifier function specifies the start or end time of a window, or the window time attribute. The returned time attribute is used for window joins. Window identifier functions

| Window identifier function | Return type | Description |
|---|---|---|
| HOP START(time-attr, size- _ interval) | TIMESTAMP | Returns the start time (the boundary value is included) of the window. For example, if the window is [00:10, 00:15), 00:10 is returned. |
| HOP END(time-attr, size-interval) _ | TIMESTAMP | Returns the end time (the boundary value is included) of the window. For example, if the window is [00:00, 00:15], 00:15 is returned. |
| HOP ROWTIME(time-attr, size- _ interval) | TIMESTAMP | Returns the end time (the boundary value is excluded) of the window. For example, if the window is [00:00, 00:15], 00:14:59.999 is returned. The return value is a rowtime attribute, based on which time- based operations such as window joins can be performed. |

Example The following example describes how to compute the number of clicks per user over the past minute every 30 seconds. That is, a 1-minute window slides every 30 seconds.

```
CREATE TABLE user_clicks(
  username VARCHAR,
  click_url VARCHAR,
  ts TIMESTAMP,
  WATERMARK wk FOR ts as withOffset(ts, 2000) -- Defines a watermark for rowtime.
) with (
  type='datahub',
  ...
```

);

```
CREATE TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  type='rds'
```

);

```
INSERT INTO tumble_output SELECT
  HOP_START(ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
  HOP_END(ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
  username,
  COUNT(click_url)
FROM window_input GROUP BY HOP(ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE), username
```

Input example

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

Output example

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:00:00.0 | 2017-10-10 10:01:00.0 | Jark | 3 |
| 2017-10-10 10:00:30.0 | 2017-10-10 10:01:30.0 | Jark | 2 |
| 2017-10-10 10:01:00.0 | 2017-10-10 10:02:00.0 | Jark | 2 |

| Developer Guide·Flink SQL |   |   | Realtime Comput |
|---|---|---|---|

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:01:30.0 | 2017-10-10 10:02:30.0 | Jark | 1 |
| 2017-10-10 10:01:30.0 | 2017-10-10 10:02:30.0 | Timo | 1 |
| 2017-10-10 10:02:00.0 | 2017-10-10 10:03:00.0 | Timo | 1 |

#### 1.9.4 Tumbling window

In tumbling windows, each element is assigned to a window with a specified size. Tumbling windows are fixed in size and do not overlap. For example, if a 5-minute tumbling window is defined, elements are assigned into windows based on time periods: [0:00, 0:05), [0:05, 0:10), [0:10, 0:15), and so on. Tumbling window shows a 30-second tumbling window. Syntax The TUMBLE function is used to define a tumbling window in a GROUP BY clause.

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

Not e

```
The <time-attr> parameter specifies a time attribute based on which a computation is pe rformed. Time attributes include processing time and event time.
```

Window identifier function A window identifier function specifies the start or end time of a window, or the window time attribute, which is used for window joins. Window identifier functions

| Window identifier function | Return type | Description |
|---|---|---|
| TUMBLE START(time-attr, size- _ interval) | TIMESTAMP | Returns the start time (the boundary value is included) of a window. For example, if the time period of a window is [00:10, 00:15), 00:10 is returned. |
| TUMBLE END(time-attr, size- _ interval) | TIMESTAMP | Returns the end time (the boundary value is included) of a window. For example, if the time period of a window is [00:00, 00:15], 00:15 is returned. |
| TUMBLE ROWTIME(time-attr, size- _ interval) | TIMESTAMP | Returns the end time (the boundary value is excluded) of a window. For example, if the time period of a window is [00:00, 00:15], 00:14:59.999 is returned. The return value is a rowtime attribute, based on which time- based operations such as window joins can be performed. |

Example You can use the following statements to compute the number of clicks per user every one minute.

```
CREATE TABLE user_clicks( username varchar, click_url varchar, ts timeStamp, WATERMARK wk FOR ts as withOffset(ts, 2000) -- Defines the rowtime field in the watermark statement. ) with ( type='datahub', ...
```

);

```
CREATE TABLE tumble_output( window_start TIMESTAMP, window_end TIMESTAMP, username VARCHAR, clicks BIGINT ) with ( type='RDS'
```

);

```
INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, COUNT(click_url) FROM window_input GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username
```

Input example

| username (VARCHAR) | click url (VARCHAR) _ | ts (TIMESTAMP) |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

Output example

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:00:00.0 | 2017-10-10 10:01:00.0 | Jark | 3 |
| 2017-10-10 10:01:00.0 | 2017-10-10 10:02:00.0 | Jark | 2 |

| ealtime Compute |   |   | Developer Guide·Flink SQ |
|---|---|---|---|

| window start _ (TIMESTAMP) | window end _ (TIMESTAMP) | username (VARCHAR) | clicks (BIGINT) |
|---|---|---|---|
| 2017-10-10 10:02:00.0 | 2017-10-10 10:03:00.0 | Timo | 1 |

#### 1.9.5 Over window

Over window aggregates are known from the standard SQL OVER clause. Different from a group window, an over window is generated for each element, and includes a set of adjacent elements. One element in a stream is assigned to multiple windows. The element that triggers computing of a window determines the last row of the window. In a data stream that applies over windows, an over window is generated for each element and an aggregate is computed for each over window. Specifically, Realtime Compute stores only one copy of streaming data, and creates an over window for each element. It computes an aggregate for each over window by using the same data copy. Each time the computing is complete, data that is no longer used is deleted from the data copy. Syntax

```
SELECT
    agg1(col1) OVER (definition1) AS colName,
    ...
    aggN(colN) OVER (definition1) AS colNameN
FROM Tab1
```

Not e OVER (definition1) in the statement must be the same. The alias specified by AS can be queried through an outer SQL statement. Type In Flink SQL, the over window definition follows standard SQL syntax. Over windows are classified into the following two types based on the type of interval each over window uses: Over windows that use a row-count interval: Each row of elements is treated as a new computed row. That is, a new window is generated for each row. Over windows that use a time internal: All rows of elements with the same timestamp value are treated as one computed row and are assigned to the same window. Supported time attributes

| Over window type | Processing time | Event time |
|---|---|---|
| Over window that uses a row- count interval | Yes | Yes |

| Over window type | Processing time | Event time |
|---|---|---|
| Over window that uses a time interval | Yes | Yes |

Over windows that use a row-count interval: The window size is determined by the number of rows of elements. Over windows that use a time interval: The window size is determined by a time range. Over windows that use a row-count interval Description In over windows that use a row-count interval, each element is assigned to a window and triggers computing. Over windows that use a row-count interval have two types: unbounded and bounded. The following figure shows unbounded over windows that use a row-count interval. Not e As shown in the preceding figure, elements in windows w7 and w8 of user 1 arrive at the same time, and so do elements in windows w3 and w4 of user 2. However, the elements are assigned to different windows. In this regard, over windows that use a row-count interval are different from over windows that use a time interval. The following figure shows bounded over windows that use a row-count interval, in which each window has three elements (first two elements have been assigned to the preceding window). Not e As shown in the preceding figure, elements in windows w5 and w6 of user 1 arrive at the same time, and so do elements in windows w2 and w3 of user 2. However, the elements are assigned to different windows. In this regard, over windows that use a row-count interval are different from over windows that use a time interval. Syntax

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     ROWS
     BETWEEN (UNBOUNDED | rowCount) PRECEDING AND CURRENT ROW) AS colName, ...
FROM Tab1
```

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used for sorting elements. rowCount: specifies the number of rows that precede the current row and are included in the window. Example An example of over windows that use a row-count interval is described as follows. Assume a product shelving table, which lists the IDs, types, shelving time, and prices of products. You need to compute the highest price among three similar products before the current product reaches shelves. Input example

| Item ID | Item type | Launch time | Price |
|---|---|---|---|
| Item 001 | Electronic | 2017-11-11 10:01:0 0 | 20 |
| Item 002 | Electronic | 2017-11-11 10:02:0 0 | 50 |
| Item 003 | Electronic | 2017-11-11 10:03:0 0 | 30 |
| Item 004 | Electronic | 2017-11-11 10:03:0 0 | 60 |
| Item 005 | Electronic | 2017-11-11 10:05:0 0 | 40 |
| Item 006 | Electronic | 2017-11-11 10:06:0 0 | 20 |
| Item 007 | Electronic | 2017-11-11 10:07:0 0 | 70 |
| Item 008 | Clothes | 2017-11-11 10:08:0 0 | 20 |

|   |   | 2017-11-11 10:01:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:02:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:03:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:03:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:05:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:06:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:07:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:08:0 |   |
|---|---|---|---|
| hes | 0 |   |   |

Sample code

```
CREATE TABLE tmall_item(
   itemID VARCHAR,
   itemType VARCHAR,
   onSellTime TIMESTAMP,
   price DOUBLE,
   WATERMARK onSellTime FOR onSellTime as withOffset(onSellTime, 0)
```

`)`

```
WITH (
  type = 'sls',
   ...
) ; SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        ROWS BETWEEN 2 preceding AND CURRENT ROW) AS maxPrice
  FROM tmall_item
```

Out put example

| Item ID | Item type | Launch time | Price | Max. Price |
|---|---|---|---|---|
| Item 001 | Electronic | 2017-11-11 10 :01:00 | 20 | 20 |
| Item 002 | Electronic | 2017-11-11 10 :02:00 | 50 | 50 |
| Item 003 | Electronic | 2017-11-11 10 :03:00 | 30 | 50 |
| Item 004 | Electronic | 2017-11-11 10 :03:00 | 60 | 60 |
| Item 005 | Electronic | 2017-11-11 10 :05:00 | 40 | 60 |
| Item 006 | Electronic | 2017-11-11 10 :06:00 | 20 | 60 |
| Item 007 | Electronic | 2017-11-11 10 :07:00 | 70 | 70 |
| Item 008 | Clothes | 2017-11-11 10 :08:00 | 20 | 20 |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| ronic | :01:00 |   |   |

|   |   | 2017-11-11 10 | 50 |
|---|---|---|---|
| ronic | :02:00 |   |   |

|   |   | 2017-11-11 10 | 30 |
|---|---|---|---|
| ronic | :03:00 |   |   |

|   |   | 2017-11-11 10 | 60 |
|---|---|---|---|
| ronic | :03:00 |   |   |

|   |   | 2017-11-11 10 | 40 |
|---|---|---|---|
| ronic | :05:00 |   |   |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| ronic | :06:00 |   |   |

|   |   | 2017-11-11 10 | 70 |
|---|---|---|---|
| ronic | :07:00 |   |   |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| hes | :08:00 |   |   |

Over windows that use a time interval Description In over windows that use a time interval, all elements with the same timestamp are assigned to a window and trigger computing. Over windows that use a time interval have two types: unbounded and bounded. The following figure shows unbounded over windows t hat use a t ime int erval. Not e As shown in the preceding figure, elements in the w7 windows of user 1 arrive at the same time, and so do elements in the w3 windows of user 2. Elements with the same timestamp are assigned to the same window. In this regard, over windows that use a time interval are different from over windows that use a row-count interval. The following figure shows bounded over windows t hat use a t ime int erval, in which a 3second window has an interval of 2 seconds. Not e As shown in the preceding figure, elements in the w6 windows of user 1 arrive at the same time, and so do elements in the w3 windows of user 2. Elements with the same timestamps are assigned to the same window. In this regard, over windows that use a time interval are different from over windows that use a row-count interval. Syntax

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1
```

value_expression: specifies the value expression used for partitioning. timeCol: specifies the time field used for sorting elements. timeInterval: specifies the time interval between the time of the current row and that of the element row that you trace backwards to. Example An example of over windows that use a time interval is described as follows. Assume a product shelving table, which lists the IDs, types, shelving time, and prices of products. You need to compute the highest price among similar products that reach shelves 2 minutes earlier than the current product. Input example

| Item ID | Item type | Launch time | Price |
|---|---|---|---|
| Item 001 | Electronic | 2017-11-11 10:01:0 0 | 20 |
| Item 002 | Electronic | 2017-11-11 10:02:0 0 | 50 |
| Item 003 | Electronic | 2017-11-11 10:03:0 0 | 30 |
| Item 004 | Electronic | 2017-11-11 10:03:0 0 | 60 |
| Item 005 | Electronic | 2017-11-11 10:05:0 0 | 40 |
| Item 006 | Electronic | 2017-11-11 10:06:0 0 | 20 |
| Item 007 | Electronic | 2017-11-11 10:07:0 0 | 70 |

|   |   | 2017-11-11 10:01:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:02:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:03:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:03:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:05:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:06:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

|   |   | 2017-11-11 10:07:0 |   |
|---|---|---|---|
| tronic | 0 |   |   |

| veloper Guide·Flink SQL |   |   | Realtime Comput |
|---|---|---|---|

| Item ID | Item type | Launch time | Price |
|---|---|---|---|
| Item 008 | Clothes | 2017-11-11 10:08:0 0 | 20 |

|   |   | 2017-11-11 10:08:0 |   |
|---|---|---|---|
| hes | 0 |   |   |

Sample code

```
CREATE TABLE tmall_item(
   itemID VARCHAR,
   itemType VARCHAR,
   onSellTime TIMESTAMP,
   price DOUBLE,
   WATERMARK onSellTime FOR onSellTime as withOffset(onSellTime, 0)
```

`)`

```
WITH (
  type = 'sls',
   ...
) ; SELECT
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        RANGE BETWEEN INTERVAL '2' MINUTE preceding AND CURRENT ROW) AS maxPrice
  FROM tmall_item
```

Out put example

| Item ID | Item type | Launch time | Price | Max. Price |
|---|---|---|---|---|
| Item 001 | Electronic | 2017-11-11 10 :01:00 | 20 | 20 |
| Item 002 | Electronic | 2017-11-11 10 :02:00 | 50 | 50 |
| Item 003 | Electronic | 2017-11-11 10 :03:00 | 30 | 50 |
| Item 004 | Electronic | 2017-11-11 10 :03:00 | 60 | 60 |
| Item 005 | Electronic | 2017-11-11 10 :05:00 | 40 | 60 |
| Item 006 | Electronic | 2017-11-11 10 :06:00 | 20 | 40 |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| ronic | :01:00 |   |   |

|   |   | 2017-11-11 10 | 50 |
|---|---|---|---|
| ronic | :02:00 |   |   |

|   |   | 2017-11-11 10 | 30 |
|---|---|---|---|
| ronic | :03:00 |   |   |

|   |   | 2017-11-11 10 | 60 |
|---|---|---|---|
| ronic | :03:00 |   |   |

|   |   | 2017-11-11 10 | 40 |
|---|---|---|---|
| ronic | :05:00 |   |   |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| ronic | :06:00 |   |   |

| Item ID | Item type | Launch time | Price | Max. Price |
|---|---|---|---|---|
| Item 007 | Electronic | 2017-11-11 10 :07:00 | 70 | 70 |
| Item 008 | Clothes | 2017-11-11 10 :08:00 | 20 | 20 |

|   |   | 2017-11-11 10 | 70 |
|---|---|---|---|
| ronic | :07:00 |   |   |

|   |   | 2017-11-11 10 | 20 |
|---|---|---|---|
| hes | :08:00 |   |   |

### 1.10 Logical operations

1.10.1. = Syntax

```
 A = B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |
| B | INT |

Description Returns TRUE if A is equal to B, and returns FALSE in other cases. Example Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 65 | 65 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int3 = int2;
```

Output example aa (INT) 1.10.2. > Syntax

```
 A > B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |
| B | INT |

Description Returns TRUE if A is greater than B, and returns FALSE in other cases. Example Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 65 | 100 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int3 > int2;
```

Output example aa (INT) 1.10.3. >= Syntax

```
 A >= B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |

| ealtime Compute | Developer Guide·Flink SQ |
|---|---|

| Parameter | Data type |
|---|---|
| B | INT |

Description Returns TRUE if A is greater than or equal to B, and returns FALSE in other cases. Example Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 65 | 65 |
| 9 | 6 | 61 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int3 >= int2;
```

Output example aa (INT) 1.10.4. < Syntax

```
 A < B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |
| B | INT |

Description Returns TRUE if A is smaller than B, and returns FALSE in other cases. Example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 66 | 65 |
| 9 | 6 | 5 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int3 < int2;
```

Output example aa (INT) 1.10.5. <= Syntax

```
 A <= B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |
| B | INT |

Description Returns TRUE if A is smaller than or equal to B, and returns FALSE in other cases. Example Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 66 | 65 |
| 9 | 6 | 5 |

```
SELECT int1 as aa FROM T1 WHERE int3 <= int2;
```

Output example aa (INT) 1.10.6. <> Syntax

```
 A <> B
```

Input parameters

| Parameter | Data type |
|---|---|
| A | INT |
| B | INT |

Description Returns TRUE if A is not equal to B, and returns FALSE in other cases. Example Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 97 | 66 | 6 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int3 <> int2;
```

Output example aa (INT)

#### 1.10.7 AND

Syntax

```
 A AND B
```

Argument : Both A and B are of the BOOLEAN type. Description TRUE is returned if both A and B are TRUE. Otherwise, FALSE is returned. Sample code Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 255 | 97 | 65 |

Sample code

```
SELECT int2 as aa FROM T1 WHERE int1 = 255 AND int3 = 65;
```

Output example aa (int)

#### 1.10.8 BETWEEN AND

Syntax

```
A BETWEEN B AND C
```

Argument s: A, B, and C are values of the DOUBLE, BIGINT, INT, VARCHAR, DATE, TIMESTAMP, or TIME type. Description Use the BETWEEN operator to select a value that is between the two given argument values. Example 1

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 90 | 80 | 100 |
| 11 | 10 | 7 |

Sample code

```
SELECT int1 as aa FROM T1 WHERE int1 BETWEEN int2 AND int3;
```

Output example aa(int) Example 2 Input example

| var1 (varchar) | var1 (varchar) | var1 (varchar) |
|---|---|---|
| b | a | c |

Sample code

```
SELECT var1 as aa FROM T1 WHERE var1 BETWEEN var2 AND var3;
```

Output example aa (varchar) b Example 3 Input example

| TIMESTAMP1 (TIMESTAMP) | TIMESTAMP2 (TIMESTAMP) | TIMESTAMP3 (TIMESTAMP) |
|---|---|---|
| 1969-07-20 20:17:30 | 1969-07-20 20:17:20 | 1969-07-20 20:17:45 |

Sample code

```
SELECT TIMESTAMP1 as aa FROM T1 WHERE TIMESTAMP1 BETWEEN TIMESTAMP2 AND TIMESTAMP3;
```

Output example aa (TIMESTAMP) 1969-07-20 20:17:30

#### 1.10.9 IS NOT FALSE

Syntax

```
A IS NOT FALSE
```

Argument : A of the BOOLEAN type Description TRUE is returned if A is true. FALSE is returned if A is false. Examples Input example

| int1(INT) | int2(INT) |
|---|---|
| 255 | 97 |

Sample code

```
SELECT int2 as aa FROM T1 WHERE int1=255 IS NOT FALSE;
```

Output example aa(int)

#### 1.10.10 IS NOT NULL

Syntax

```
A IS NOT NULL
```

Argument s: A of the INT type TRUE is returned if A is null. Otherwise, FALSE is returned. Examples Input example

| int1(INT) | int2(VARCHAR) |
|---|---|
| 97 | null |
| 9 | ww123 |

Not e Here, null indicates empty, rather than a null string. Sample code

```
SELECT int1 as aa FROM T1 WHERE int2 IS NOT NULL;
```

Output example aa(int)

#### 1.10.11 IS NOT TRUE

Syntax

```
A IS NOT TRUE
```

Argument : A specifies a condition of the BOOLEAN type. Description FALSE is returned if the condition is TRUE. TRUE is returned if the condition is FALSE. Examples Input example

| int1 (INT) | int2 (INT) |
|---|---|
| 255 | 97 |

```
SELECT int2 as aa FROM T1 WHERE int1 = 25 IS NOT TRUE;
```

Output example aa (int)

#### 1.10.12 IS NOT UNKNOWN

Syntax

```
A IS NOT UNKNOWN
```

Argument : A is of the BOOLEAN type. Description A is a logical comparison expression, such as 6 < 8. The value of A is TRUE or FALSE if a logical comparison between two numeric values is performed successfully. If a numeric value is compared with a non-numeric value, the logical comparison fails, and the value of A is neither TRUE nor FALSE. IS NOT UNKNOWN is used to check for such failures. It returns FALSE if the value of A is neither TRUE nor FALSE and returns T RUE if the value of A is TRUE or FALSE. Examples Input example

| int1 (INT) | int2 (INT) |
|---|---|
| 255 | 97 |

Sample code 1

```
SELECT int2 as aa FROM T1 WHERE int1 = 25 IS NOT UNKNOWN;
```

Output example 1 aa (int) Sample code 2

```
SELECT int2 as aa FROM T1 WHERE int1 < null IS NOT UNKNOWN;
```

Output example 2 aa (int) Null

#### 1.10.13 IS NULL

Syntax

```
value IS NULL
```

Argument : value specifies a value of any type. Description TRUE is returned if A is null. Otherwise, FALSE is returned. Examples Input example

| int1 (INT) | int2 (VARCHAR) |
|---|---|
| 97 | null |
| 9 | www |

Not e In this case, null indicates empty, rather than a null string. Sample code

```
SELECT int1 as aa FROM T1 WHERE int2 IS NULL;
```

Output example aa (int)

#### 1.10.14 IS TRUE

```
A IS TRUE
```

Argument : A of the BOOLEAN type Description TRUE is returned if A is TRUE. FALSE is returned if A is FALSE. Examples Input example

| int1(INT) | int2(INT) |
|---|---|
| 255 | 97 |

Sample code

```
SELECT int2 as aa FROM T1 WHERE int1=255 IS TRUE;
```

Output example aa(int)

#### 1.10.15 IS UNKNOWN

Syntax

```
A IS UNKNOWN
```

Argument : A of the BOOLEAN type Description A is a logical comparison expression, such as 6 <> 8. The value of A is TRUE or FALSE if a logical comparison between two numeric values is performed successfully. If a numeric value is compared with a non-numeric value, the logical comparison fails, and the value of A is neither TRUE nor FALSE. IS UNKNOWN is used to check for such failures. It returns T RUE if the value of A is neither TRUE nor FALSE and returns FALSE if the value of A is TRUE or FALSE.

| int1(INT) | int2(INT) |
|---|---|
| 255 | 97 |

Sample code 1

```
SELECT int2 as aa FROM T1 WHERE int1=25 IS UNKNOWN;
```

Output example 1 aa(int) Null Sample code 2

```
SELECT int2 as aa FROM T1 WHERE int1 > null IS UNKNOWN;
```

Output example 2 aa(int)

#### 1.10.16 LIKE

Syntax

```
A LIKE B
```

Argument s: A and B of the VARCHAR type Description TRUE is returned if A matches B. Otherwise, FALSE is returned. Not e The percent sign (%) can be used as a wildcard. Examples Sample code

| int1(INT) | VARCHAR2(VARCHAR) | VARCHAR3(VARCHAR) |
|---|---|---|
| 90 | ss97 | 97ss |
| 99 | ss10 | 7ho7 |

Sample code 1

```
SELECT int1 as aa FROM T1 WHERE VARCHAR2 LIKE 'ss%';
```

Output example 1 aa(int) Sample code 2

```
SELECT int1 as aa FROM T1 WHERE VARCHAR3 LIKE '%ss';
```

Output example 2 aa(int) Sample code 3

```
SELECT int1 as aa FROM T1 WHERE VARCHAR3 LIKE '%ho%';
```

Output example 3 aa(int)

#### 1.10.17 NOT

```
NOT A
```

Argument : A of the BOOLEAN type Description FALSE is returned if A is TRUE. TRUE is returned if A is FALSE. Examples Input example

| int2(INT) | int3(INT) |
|---|---|
| 97 | 65 |

Sample code

```
SELECT int2 as aa FROM T1 WHERE NOT int3=62;
```

Output example aa(int)

#### 1.10.18 NOT BETWEEN AND

Syntax

```
A NOT BETWEEN B AND C
```

Argument s: A, B, and C can be of the DOUBLE, BIGINT, INT, VARCHAR, DATE, TIMESTAMP, or TIME types. Description The NOT BETWEEN operator is used to select a value that is not between the two given argument values. Example 1 Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 90 | 97 | 80 |
| 11 | 10 | 7 |

```
SELECT int1 as aa FROM T1 WHERE int1 NOT BETWEEN int2 AND int3;
```

Output example aa (int) Example 2 Input example

| var1 (varchar) | var1 (varchar) | var1 (varchar) |
|---|---|---|
| d | a | c |

Sample code

```
SELECT var1 as aa FROM T1 WHERE var1 NOT BETWEEN var2 AND var3;
```

Output example aa (varchar) d Example 3 Input example

| TIMESTAMP1 (TIMESTAMP) | TIMESTAMP2 (TIMESTAMP) | TIMESTAMP3 (TIMESTAMP) |
|---|---|---|
| 1969-07-20 20:17:30 | 1969-07-20 20:17:40 | 1969-07-20 20:17:45 |

Sample code

```
SELECT TIMESTAMP1 as aa FROM T1 WHERE TIMESTAMP1 NOT BETWEEN TIMESTAMP2 AND TIMESTAMP3;
```

Output example aa (TIMESTAMP) 1969-07-20 20:17:30

#### 1.10.19 OR

Syntax

```
 A OR B
```

Argument s: Both A and B are of the BOOLEAN type Description TRUE is returned if both A and B are TRUE. Otherwise, FALSE is returned. Examples Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 255 | 97 | 65 |

Sample code

```
SELECT int2 as aa FROM T1 WHERE int1 = 255 OR int3 = 65;
```

Output example aa (int)

#### 1.10.20 IN

Syntax

```
SELECT column_name(s)
  FROM table_name
 WHERE column_name IN (value1,value2,...)
```

Argument s: Both value1 and value2 must be constants. Query records that match the arguments.

| id (INT) | LastName (Varchar) |
|---|---|
| 1 | Adams |
| 2 | Bush |
| 3 | Carter |

Sample code

```
SELECT * FROM T1
 WHERE LastName IN ('Adams','Carter')
```

Output example

| id (INT) | LastName (Varchar) |
|---|---|
| 1 | Adams |
| 3 | Carter |

#### 1.10.21 NOT IN

Syntax

```
SELECT column_name(s)
  FROM table_name
 WHERE column_name NOT IN (value1,value2,...)
```

Input paramet ers: value1 and value2, which must be constants Description Searches for records that do not match the values in the arguments. Example Input example

| id (INT) | LastName (VARCHAR) |
|---|---|
| 1 | Adams |
| 2 | Bush |
| 3 | Carter |

```
SELECT * FROM T1
 WHERE LastName NOT IN ('Adams','Carter')
```

Output example

| id (INT) | LastName (VARCHAR) |
|---|---|
| 2 | Bush |

#### 1.10.22 IS DISTINCT FROM

Syntax

```
A IS DISTINCT FROM B
```

Argument s: A and B of generic types Description Check whether two arguments are equal. TRUE is returned if their data types or values are different. FALSE is returned if their data types and values are the same. If either or both arguments are null, they are considered to be the same. Examples Input example

| A(Int) | B(Varchar) |
|---|---|
| 97 | 97 |
| null | sss |
| null | null |

Sample code

```
SELECT
 A IS DISTINCT FROM B as `result`
FROM T1
```

Output example result(BOOLEAN) true true result(BOOLEAN) false

#### 1.10.23 IS NOT DISTINCT FROM

Syntax

```
A IS NOT DISTINCT FROM B
```

Argument s: A and B of generic types Description Check whether two arguments are equal. FALSE is returned if their data types or values are different. TRUE is returned if their data types and values are the same. If either or both arguments are null, they are considered to be the same. Examples Input example

| A(Int) | B(Varchar) |
|---|---|
| 97 | 97 |
| null | sss |
| null | null |

Sample code

```
SELECT
 A IS NOT DISTINCT FROM B as `result`
FROM T1
```

Output example result(BOOLEAN) false false true

### 1.11 Built-in functions

#### 1.11.1 String functions

##### 1.11.1.1 Overview

CHAR_LENGTH Syntax: `CHAR_LENGTH(A)` Input parameter: The A parameter is of the VARCHAR data type. Description: Returns the number of characters in a string. Example Input example var1 (VARCHAR) ss 231ee Sample code

```
SELECT CHAR_LENGTH(var1) as aa FROM T1;
```

Output example aa (INT) ASCII2STR Syntax: `string ascii2str(int ascii)` Description: Converts a number into an ASCII character. If any argument is NULL, the return value is NULL. Input parameter: The value of the ascii parameter ranges from 1 to 127. If the value fall out of the range, an exception occurs. Example:

```
ascii2str(9) = '\t' ascii2str(65) = 'A'
```

CONCAT Syntax: `string concat(string a, string b, ...)` Description: Concatenates all input strings and returns a new string. If any argument is NULL, the return value is NULL. Example:

```
concat('abc', 'def', 'gh') = 'abcdefgh' concat('abc', NULL) = NULL
```

CONCAT_WS

```
Syntax: string concat_ws(string separator, string a, string b, ...)
```

Description: Concatenates all input strings. Different from the CONCAT function, this function adds a separator between two concatenated strings. If any argument is NULL, the return value is NULL. Example:

```
concat_ws(':', 'abc', 'def', 'gh') = 'abc:def:gh' concat(':', 'abc', NULL) = NULL
```

SUBSTR Syntax

```
string substr(string a, int start) string substr(string a, int start, int len)
```

Description: Extracts a substring of the specified length from a string, starting from the specified position. If the length is not specified, a substring is extracted from the specified position to the end of the string. The value of the start parameter begins from 1. If the value is negative, a substring is extracted from the end of the string. If any argument is NULL, the return value is NULL. Example:

```
substr('galaxy_sql', 5) = 'xy_sql' substr('galaxy_sql', -5) = 'y_sql' substr('galaxy_sql', 5, 2) = 'xy'
```

LOWER Syntax

```
string lower(string a) string lcase(string a)
```

Description: Converts uppercase letters in a string into lowercase letters. If any argument is NULL, the return value is NULL. Example: `lower('fOoBaR') = 'foobar'` UPPER

```
string upper(string a) string ucase(string a)
```

Description: Converts lowercase letters in a string into uppercase letters. If any argument is NULL, the return value is NULL. Example: `upper('fOoBaR') = 'FOOBAR'` TRIM Syntax: `string trim(string a)` Description: Removes the leading and trailing spaces of a string. If any argument is NULL, the return value is NULL. Example: trim(' foobar\t ') = 'foobar\t' LTRIM Syntax: `string ltrim(string a)` Description: Removes the leading spaces of a string. If any argument is NULL, the return value is NULL. Example: `ltrim(' foobar ') = 'foobar '` RTRIM Syntax: `string rtrim(string a)` Description: Removes the trailing spaces of a string. If any argument is NULL, the return value is NULL. Example: `rtrim(' foobar ') = ' foobar'` LPAD

```
Syntax: string lpad(string str, int len, string pad)
```

Description: Left-pads a string (str) with another string (pad), to the specified length. If any argument is NULL, the return value is NULL. Example:

```
lpad('hi', 5, '??') = '??? hi' lpad('hi', 1, '??') = 'h' lpad('---', 10, 'abc') = 'abcabca---'
```

RPAD

```
Syntax: string rpad(string str, int len, string pad)
```

Description: Right-pads a string (str) with another string (pad), to the specified length. If any argument is NULL, the return value is NULL. Example:

```
rpad('hi', 5, '??') = 'hi???' rpad('hi', 1, '??') = 'h' rpad('---', 10, 'abc') = '---abcabca'
```

LENGTH Syntax: `int length(string str)` Description: Returns the length of a string. If any argument is NULL, the return value is NULL. Example:

```
length('hi') = 2 length('I') = 1 length(NULL) = NULL
```

REPEAT Syntax: `string repeat(string str, int n)` Description: Returns a new string that repeats the specified string for the specified number of times. If any argument is NULL, the return value is NULL. Example: `repeat('hi', 2) = 'hihi'` REVERSE Syntax: `string reverse(string str)` Description: Reverses a string. If any argument is NULL, the return value is NULL. Example: `reverse('abc') = 'cba'` SPLIT_EX

```
Syntax: string split_ex(string str, string sep, int index)
```

Description: Uses a separator to split a string into several segments and returns the segment identified by the index parameter. If the segment identified by the index parameter does not exist, NULL is returned. The value of the index parameter starts from 0. If any argument is NULL, the return value is NULL. Example:

```
split_ex('1.2.3.4', '.', 1) = '2' split_ex('1.2.3.4', '.', -1) = NULL split_ex('1.2.3.4', '.', 4) = NULL
```

REGEXP_REPLACE

```
Syntax: string regexp_replace(string str, string pattern, string replacement)
```

Description: Returns a string from the str string with its substrings that match the pattern regular expression replaced with the replacement string.

> **Note:** Backslashes (\) are used in a regular expression to escape special characters. If any argument is NULL, the return value is NULL. Example:


```
regexp_replace('100-200', '(\\d+)', 'num') = 'num-num' regexp_replace('2014-03-13', '-', '') = '20140313' regexp_replace('foobar', 'oo|ar', '') = 'fb'
```

REGEXP_EXTRACT

```
Syntax: string regexp_extract(string str, string pattern, int index)
```

Description: Returns a substring of the str string that matches the pattern regular expression. Multiple substrings may all match the pattern. The index parameter identifies the substring to be returned. The value of the index parameter starts from 1.

> **Note:** A backslash (\) is used in a regular expression to escape special characters. If any argument is NULL, the return value is NULL. Example:


```
regexp_extract('foothebar', 'foo(. *?)( bar)', 2) = 'bar' regexp_extract('100-200', '(\\d+)-(\\d+)', 1) = '100'
```

INSTR Syntax: `int instr(string str, string substr)` Description: Returns the position where a substring first appears in a string. The return value starts from 1. If the specified substring does not exist in the string, 0 is returned. If any argument is NULL, the return value is NULL. Example:

```
instr('foobar', 'foo') = 1 instr('foobar', 'abc') = 0
```

KEYVALUE

```
Syntax: string keyvalue(string str, string split1, string split2, string key_name)
```

Description: Parses key-value pairs from the specified string and returns the value that is mapped to the specified key. If the key does not exist, the return value is NULL. If any argument is NULL, the return value is NULL. Example:

```
keyvalue('k1=v1;k2=v2', ';', '=', 'k2') = 'v2' keyvalue('k1:v1,k2:v2', ',', ':', 'k3') = NULL
```

HASH Syntax: `int hash(string str)` Description: Returns the absolute value of the integer returned by the hashCode() function that takes the specified string as an input. If any argument is NULL, the return value is NULL. MD5 Syntax: `string md5(string str)` Description: Returns the MD5 value of a string. If any argument is NULL or an empty string, the return value is an empty string.

##### 1.11.1.2 CHAR_LENGTH

Syntax

```
CHAR_LENGTH(A)
```

Input parameter A: VARCHAR data type Description Returns the number of characters in a string. Example Input example var1 (VARCHAR) ss 231ee Sample code

```
SELECT CHAR_LENGTH(var1) as aa FROM T1;
```

Output example aa (INT)

##### 1.11.1.3 CHR

y

```
VARCHAR CHR(INT ascii)
```

Arguments ascii: specifies an integer of the INT type, ranging from 0 to 255. If the argument falls out of this range, null is returned. Description Convert ASCII codes into characters. Examples Input example

| int1(INT) | int2(INT) | int3 (INT) |
|---|---|---|
| 255 | 97 | 65 |

Sample code

```
SELECT CHR(int1) as var1, CHR(int2) as var2, CHR(int3) as var3 FROM T1
```

Output example

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| ÿ | a | A |

##### 1.11.1.4 CONCAT

Syntax

```
VARCHAR concat(VARCHAR var1, VARCHAR var2, ...)
```

Arguments var1: specifies a common string of the VARCHAR type. var2: specifies a common string of the VARCHAR type. Description Concatenate two or more strings into a single string. If any argument is NULL, the argument is skipped. Examples

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) |
|---|---|---|
| Hello | My | World |
| Hello | null | World |
| null | null | World |
| null | null | null |

Sample code

```
SELECT CONCAT(var1, var2, var3) as var FROM T1
```

Output example var (VARCHAR) HelloMyWorld HelloWorld World ""

##### 1.11.1.5 CONCAT_WS

Syntax

```
VARCHAR CONCAT_WS(VARCHAR separator, VARCHAR var1, VARCHAR var2, ...)
```

Arguments separator: specifies a separator of the VARCHAR type. var1: specifies a value of the VARCHAR type. var2: specifies a value of the VARCHAR type. Description Concatenate each argument's value with a separator to a new string and return the new string, whose length and type depend on the input values. Not e If the separator value is null, it is treated as an empty string for concatenating the argument's values. If any argument is null, the argument is skipped during concatenation.

| sep (VARCHAR) | str1 (VARCHAR) | str2 (VARCHAR) | str3 (VARCHAR) |
|---|---|---|---|
| \| | Jack | Harry | John |
| null | Jack | Harry | John |
| \| | null | Harry | John |
| \| | Jack | null | null |

Sample code

```
SELECT CONCAT_WS(sep, str1, str2, str3) as var FROM T1
```

Output example var (VARCHAR) Jack|Harry|John JackHarryJohn Harry|John Jack

##### 1.11.1.6 FROM_BASE64

Syntax

```
BINARY FROM_BASE64(str)
```

Arguments str: specifies a Base64 string of the VARCHAR type. Description Parse a Base64 string into binary data. Examples Input example

| a (INT) | b (BIGINT) | c (VARCHAR) |
|---|---|---|
| 1 | 1L | null |

Sample code

```
SELECT from_base64(c) as var1,from_base64('SGVsbG8gd29ybGQ=') as var2 FROM T1
```

Output example

| var1 (BINARY) | var2 (BINARY) |
|---|---|
| null | Byte Array: [72('H'), 101('e'), 108('l'), 108('l'), 111('o'), 32(' '), 119('w'), 111('o'), 114('r'), 108('l'), 100('d')] |

##### 1.11.1.7 HASH_CODE

Syntax

```
INT HASH_CODE(VARCHAR str)
```

Arguments str: VARCHAR type Description Return the absolute value of a string on which hashCode() has been executed. Examples Input example

| str1(VARCHAR) | str2(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| k1=v1;k2=v2 | k1:v1,k2:v2 | null |

Sample code

```
SELECT HASH_CODE(str1) as var1, HASH_CODE(str2) as var2, HASH_CODE(nullstr) as var3 FROM T1
```

Output example

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 1099348823 | 401392878 | null |

##### 1.11.1.8 INITCAP

Syntax

```
 INITCAP(A)
```

Input parameter A: VARCHAR data type Description Returns a string with the first letter of each word in uppercase and all other letters in lowercase. Example Input example var1 (VARCHAR) aADvbn Sample code

```
SELECT INITCAP(var1) as aa FROM T1;
```

Output example aa (VARCHAR) Aadvbn

##### 1.11.1.9 JSON_VALUE

Syntax

```
VARCHAR JSON_VALUE(VARCHAR content, VARCHAR path)
```

Arguments content: specifies a JSON object to be parsed, which is represented as a JSON string of the VARCHAR type. path: specifies a path expression of the VARCHAR type to parse the JSON objects. The following table lists the path expressions that are currently supported. Path expressions supported

| Symbol | Feature |
|---|---|
| $ | Root object |
| [] | Array subscript |
| * | Array wildcard |
| . | Specified objects in a parent object |

Description Extract the value of the specified path from a JSON string. If the JSON string is invalid or any argument is NULL, the return value is NULL. Examples Input example

| id (INT) | json(VARCHAR) | path(VARCHAR) |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |
| 2 | {"aaa": "bbb", "ccc": {"ddd": "eee", "fff": "ggg", " +""hhh": ["h0", "h1", "h2"]}, "iii": "jjj"} | $.ccc.hhh [*] |
| 3 | {"aaa": "bbb", "ccc": {"ddd": "eee", "fff": "ggg"," +""hhh": ["h0", "h1", "h2"]}, "iii": "jjj"} | $.ccc.hhh [1] |
| 4 | [10, 20, [30, 40]] | NULL |
| 5 | NULL | $[2] [*] |
| 6 | “{xx]” | “$[2][*]” |

Sample code

```
SELECT
```

`id`，

```
    JSON_VALUE(json, path) AS value
FROM
```

`T1` Output example

| id (INT) | value (VARCHAR) |
|---|---|
| 1 | [30, 40] |
| 2 | ["h0", "h1", "h2"] |

| R | ealtime Compute | Developer Guide·Flink SQ | L |
|---|---|---|---|

| id (INT) | value (VARCHAR) |
|---|---|
| 3 | H1 |
| 4 | NULL |
| 5 | NULL |
| 6 | NULL |

##### 1.11.1.10 KEYVALUE

Syntax

```
VARCHAR KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name)
```

Arguments str: specifies a string of key-value pairs. This argument is of the VARCHAR type. split1: specifies a delimiter of the VARCHAR type to separate the key-value pairs. split2: specifies a delimiter of the VARCHAR type to separate the key and value in a key-value pair. key_name: specifies a key value of the VARCHAR type. Description Parse the key-value pairs in a string to locate a key-value pair that matches the key-value pair delimiter and key-value delimiter. Then return the key value corresponding to the key name in the key-value pair. If the key name does not exist or an exception occurs, the return value is NULL. Examples Input example

| str (VARCHAR) | split1 (VARCHAR) | split2 (VARCHAR) | key1 (VARCHAR) |
|---|---|---|---|
| k1=v1; k2=v2 | ; | = | k2 |
| null | ; | \| | : |
| k1:v1\|k2:v2 | null | = | : |
| k1:v1\|k2:v2 | \| | = | null |
| k1:v1\|k2:v2 | \| | = | : |
| k1:v1\|k2:v2 | \| | = | : |

Sample code

```
SELECT KEYVALUE(str, split1, split2, key1) as result FROM T1
```

Output example result (VARCHAR) v2 null null null null null

##### 1.11.1.11 LOWER

Syntax

```
VARCHAR LOWER(A)
```

Argument A: specifies a value of the VARCHAR type. Description Convert the specified string to a string of lowercase letters. Examples Input example var1 (VARCHAR) Ss yyT Sample code

```
SELECT LOWER(var1) as aa FROM T1;
```

aa (VARCHAR) ss yyt

##### 1.11.1.12 LPAD

Syntax

```
VARCHAR LPAD(VARCHAR str, INT len, VARCHAR pad)
```

Arguments str: specifies a source string of the VARCHAR type. len: specifies the length of a new string. This argument is of the INT type. pad: specifies a string to be repeatedly padded to the source string. This argument is of the VARCHAR type. Description Left pad a source string with another string several times until the new string reaches the specified length. If any argument is NULL, the return value is NULL. If the source string is an empty string or the target length is a negative number, the return value is NULL. If the string to be padded to the source string is an empty string, there are two scenarios. A trimmed source string is returned when the specified length is equal to or less than the length of the source string. NULL is returned when the specified length is greater than the length of the source string. Examples Input example

| str (VARCHAR) | len (INT) | pad (VARCHAR) |
|---|---|---|
| "" | -2 | "" |
| HelloWorld | 15 | John |
| John | 2 | C |
| C | 4 | HelloWorld |
| null | 2 | C |
| c | 2 | null |
| asd | 2 | "" |
| "" | 2 | s |
| asd | 4 | "" |

| Developer Guide·Flink SQL |   | Realtime Comput |
|---|---|---|
| str (VARCHAR) | len (INT) | pad (VARCHAR) |
| "" | 0 | "" |

Sample code

```
SELECT LPAD(str, len, pad) AS result FROM T1
```

Output example result (VARCHAR) null JohnJHelloWorld Jo HelC null null as ss null ""

##### 1.11.1.13 MD5

Syntax

```
VARCHAR MD5(VARCHAR str)
```

Argument str: specifies a string of the VARCHAR type. Description Return the MD5 value of a string. If the argument is NULL, the return value is NULL. If the argument is an empty string, the return value is an empty string.

| str1 (VARCHAR) | str2 (VARCHAR) |
|---|---|
| k1 = v1; k2 = v2 | null |

Sample code

```
SELECT
   MD5(str1) as var1,
   MD5(str2) as var2
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) |
|---|---|
| 19c17f42b4d6a90f7f9ffc2ea9bdd775 | NA |

##### 1.11.1.14 OVERLAY

Syntax

```
VARCHAR OVERLAY ( (VARCHAR x PLACING VARCHAR y FROM INT start_position [ FOR INT length ])
```

`)` Arguments x: VARCHAR type y: VARCHAR type start_position: INT type length (optional): INT type Description Replace a substring of x with y. The replacement starts from start_position and a total of length+1 characters are to be replaced. Examples Sample code

```
OVERLAY('abcdefg' PLACING 'hij' FROM 2 FOR 2) as result FROM T1
```

Output example result(VARCHAR) ahijdefg

##### 1.11.1.15 PARSE_URL

Syntax

```
VARCHAR PARSE_URL(VARCHAR urlStr, VARCHAR partToExtract [, VARCHAR key])
```

Arguments urlStr: specifies a URL string of the VARCHAR type. partToExtract: specifies a value of the VARCHAR type obtained after parsing. key: specifies an argument name of the VARCHAR type. Description Parse a URL to obtain the value of partToExtract, such as QUERY. The options for partToExtract include HOST, PATH, QUERY, REF, PROTOCOL, FILE, AUTHORITY, and USERINFO. Not e If the partToExtract value is NULL, NULL is returned. Examples Input example

| url1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| http://facebook.com/path/p1.php?query=1 | null |

Sample code

```
SELECT PARSE_URL(url1, 'QUERY', 'query') as var1,
       PARSE_URL(url1, 'QUERY') as var2,
       PARSE_URL(url1, 'HOST') as var3,
       PARSE_URL(url1, 'PATH') as var4,
       PARSE_URL(url1, 'REF') as var5,
       PARSE_URL(url1, 'PROTOCOL') as var6,
       PARSE_URL(url1, 'FILE') as var7,
       PARSE_URL(url1, 'AUTHORITY') as var8,
       PARSE_URL(nullstr, 'QUERY') as var9,
       PARSE_URL(url1, 'USERINFO') as var10,
       PARSE_URL(nullstr, 'QUERY', 'query') as var11
FROM T1
```

Output example

| var1( VARC HAR) | var2( VARC HAR) | var3( VARC HAR) | var4(V ARCH AR) | var5(V ARCH AR) | var6(V ARCH AR) | var7(V ARCH AR) | var8(V ARCH AR) | var9(V ARCH AR) | var10( VARC HAR) | var11( VARC HAR) |
|---|---|---|---|---|---|---|---|---|---|---|

| var1( VARC HAR) | var2( VARC HAR) | var3( VARC HAR) | var4(V ARCH AR) | var5(V ARCH AR) | var6(V ARCH AR) | var7(V ARCH AR) | var8(V ARCH AR) | var9(V ARCH AR) | var10( VARC HAR) | var11( VARC HAR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query =1 | faceb ook.c om | /path /p1.p hp | null | http | /path /p1.p hp? query =1 | faceb ook.c om | null | null | null |

##### 1.11.1.16 POSITION

Syntax

```
INTEGER POSITION( x IN y)
```

Arguments x: specifies a value of the VARCHAR type. y: specifies a value of the VARCHAR type. Description Return the position of the first occurrence of string x within string y. The function is similar to LOCATE(substr,str). Examples Sample code

```
POSITION('in' IN 'china') as result FROM T1
```

Output example result (INT)

##### 1.11.1.17 REGEXP

Syntax

```
BOOLEAN REGEXP(VARCHAR str, VARCHAR pattern)
```

Arguments str: specifies a string of the VARCHAR type. pattern: specifies a pattern of the VARCHAR type. Perform regular expression matching on a string to check whether it matches the specified pattern. If the string or pattern is empty or null, FALSE is returned. Examples Input example

| str1(VARCHAR) | pattern1 (VARCHAR) |
|---|---|
| k1=v1;k2=v2 | k2* |
| k1:v1\|k2:v2 | k3 |
| null | k3 |
| k1:v1\|k2:v2 | null |
| k1:v1\|k2:v2 | ( |

Sample code

```
SELECT REGEXP(str1, pattern1) as result FROM T1
```

Output example result(BOOLEAN) true false null null false

##### 1.11.1.18 REGEXP_EXTRACT

Syntax

```
VARCHAR REGEXP_EXTRACT(VARCHAR str, VARCHAR pattern, INT index)
```

Arguments str: specifies a source string of the VARCHAR type. pattern: specifies the regular expression pattern used to match the string to be extracted. This argument is of the VARCHAR type. index: specifies the index number of the substring to be extracted from the source string. This argument is of the INT type. Not e Specify constants in the regular expression with Java format because SQL string constants are completely compiled to Java code. For example, you can specify a digit (0-9) in the regular expression as \d, which is the same as the digit in a regular expression in Java code. Description Use the regular expression pattern to match and extract the indexed substring from a source string. The index starts from 1. If any argument is NULL or the regular expression is invalid, the return value is NULL. Examples Input example

| str1 (VARCHAR) | pattern1 (VARCHAR) | index1 (INT) |
|---|---|---|
| foothebar | foo(. *?)( bar) | 2 |
| 100-200 | (\d+)-(\d+) | 1 |
| null | foo(. *?)( bar) | 2 |
| foothebar | null | 2 |
| foothebar | "" | 2 |
| foothebar | ( | 2 |

Sample code

```
SELECT REGEXP_EXTRACT(str1, pattern1, index1) as result FROM T1
```

Output example result (VARCHAR) bar null null null null

##### 1.11.1.19 REGEXP_REPLACE

Syntax

```
VARCHAR REGEXP_REPLACE(VARCHAR str, VARCHAR pattern, VARCHAR replacement)
```

Arguments str: specifies a string of the VARCHAR type. pattern: specifies the regular expression pattern used to match the string to be replaced. This argument is of the VARCHAR type. replacement: specifies the string used to replace others. This argument is of the VARCHAR type. Not e Specify constants in the regular expression with Java format because SQL string constants are completely compiled to Java code. For example, you can specify a digit (0-9) in the regular expression as \d, which is the same as the digit in a regular expression in Java code. Description Replace a substring that matches the regular expression pattern in a source string with a specified string, and return a new string. If any argument is NULL or the regular expression is invalid, the return value is NULL. Examples Input example

| str1 (VARCHAR) | pattern1 (VARCHAR) | replace1 (VARCHAR) |
|---|---|---|
| 2014-03-13 | - | "" |
| null | - | "" |
| 2014-03-13 | - | null |
| 2014-03-13 | "" | s |
| 2014-03-13 | ( | s |
| 100-200 | (\d+) | num |

Sample code

```
SELECT REGEXP_REPLACE(str1, pattern1, replace1) as result FROM T1
```

Output example result (VARCHAR) 20140313 null null 2014-03-13 null num-num

##### 1.11.1.20 REPEAT

Syntax

```
VARCHAR REPEAT(VARCHAR str, INT n)
```

Arguments str: specifies the string to be repeated. This argument is of the VARCHAR type. n: specifies the number of repetitions. This argument is of the INT type. Description Return a new string consisting of N repetitions of the specified string. If any argument is NULL, the return value is NULL. If the value of n is 0 or a negative number, the return value is an empty string. Examples Input example

| str(VARCHAR) | n(INT) |
|---|---|
| J | 9 |
| Hello | 2 |
| Hello | -9 |
| null | 9 |

Sample code

```
SELECT REPEAT(str,n) as var1 FROM T1
```

result(VARCHAR) JJJJJJJJJ HelloHello “” null

##### 1.11.1.21 REVERSE

Syntax

```
VARCHAR REVERSE(VARCHAR str)
```

Arguments str: specifies a string of the VARCHAR type. Description Return a string in the reverse order of the specified string. If the argument is NULL, the return value is NULL. Examples Input example

| str1(VARCHAR) | str2(VARCHAR) | str3 (VARCHAR) | str4 (VARCHAR) |
|---|---|---|---|
| iPhoneX | Alibaba | World | null |

Sample code

```
SELECT REVERSE(str1) as var1 ,REVERSE(str2) as var2,
        REVERSE(str3) as var3,REVERSE(str4) as var4
FROM T1
```

Output example

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) | var4(VARCHAR) |
|---|---|---|---|
| XenohPi | ababilA | dlroW | null |

##### 1.11.1.22 RPAD

```
VARCHAR RPAD(VARCHAR str, INT len, VARCHAR pad)
```

Arguments str: specifies a source string of the VARCHAR type. len: specifies the length of a new string. This argument is of the INT type. pad: specifies a string to be repeatedly padded to the source string. This argument is of the VARCHAR type. Description Right pad a string with another string several times until the new string reaches the specified length. If any argument is NULL, the return value is NULL. If the source string is an empty string or the specified length is a negative number, the return value is NULL. If the string to be padded to the source string is an empty string, there are two scenarios. A trimmed source string is returned when the specified length is equal to or less than the length of the source string. NULL is returned when the specified length is greater than the length of the source string. Examples Input example

| str (VARCHAR) | len (INT) | pad (VARCHAR) |
|---|---|---|
| "" | -2 | "" |
| HelloWorld | 15 | John |
| John | 2 | C |
| C | 4 | HelloWorld |
| null | 2 | C |
| c | 2 | null |
| asd | 2 | "" |
| "" | 2 | s |
| asd | 4 | "" |
| "" | 0 | "" |

Sample code

```
SELECT RPAD(str, len, pad) as result FROM T1
```

result (VARCHAR) null HelloWorldJohnJ Jo CHel null null as ss null ""

##### 1.11.1.23 SPLIT_INDEX

Syntax

```
VARCHAR SPLIT_INDEX(VARCHAR str, VARCHAR sep, INT index)
```

Arguments str: specifies the string to be split. This argument is of the VARCHAR type. sep: specifies the separator of the VARCHAR type. index: specifies the index number of the substring to be obtained from the split string. This argument is of the INT type. Description Use a separator to split a string into several substrings and return the indexed substring. If no substring is indexed, NULL is returned. The index starts from 0. If any argument is NULL, the return value is NULL. Examples Input example

| str (VARCHAR) | sep (VARCHAR) | index (INT) |
|---|---|---|
| Jack,John,Mary | , | 2 |
| Jack,John,Mary | , | 3 |
| Jack,John,Mary | null | 0 |

| ealtime Compute |   | Developer Guide·Flink SQ |
|---|---|---|

| str (VARCHAR) | sep (VARCHAR) | index (INT) |
|---|---|---|
| null | , | 0 |

Sample code

```
SELECT SPLIT_INDEX(str, sep, index) as var1 FROM T1
```

Output example var1 (VARCHAR) Mary null null null

##### 1.11.1.24 STR_TO_MAP

Syntax

```
MAP STR_TO_MAP(VARCHAR text) MAP STR_TO_MAP(VARCHAR text, VARCHAR listDelimiter, VARCHAR keyValueDelimiter)
```

Arguments text: specifies given text of the VARCHAR type. listDelimiter: specifies the delimiter used to splits the given text into key-value pairs. This argument is of the VARCHAR type. The default delimiter is a comma (,). keyValueDelimiter: specifies the delimiter used to separate the key and value in a key-value pair. This argument is of the VARCHAR type. The default delimiter is an equal sign (=). Not e The delimiters are defined by Java regular expressions. If a special character is used, it needs to be converted to an escape character. Description Use listDelimiter to split the given text into key-value pairs, use keyValueDelimiter to separate the key and value in each key-value pair, and then generate and return a map. Examples

```
SELECT
  STR_TO_MAP('k1 = v1, k2 = v2' ) ['k1'] as a
FROM T1
```

Output example a (VARCHAR) v1

##### 1.11.1.25 SUBSTRING

Syntax

```
VARCHAR SUBSTRING(VARCHAR a, INT start) VARCHAR SUBSTRING(VARCHAR a, INT start, INT len)
```

Arguments a: specifies the string from which a substring is to be obtained. This argument is of the VARCHAR type. len: specifies the length of the substring to be obtained. This argument is of the INT type. start: specifies the start position where the substring is to be obtained from the specified string. This argument is of the INT type. Description Obtain a substring of the specified length from a string, starting from the specified position. If the length is not specified, the entire string is obtained. start begins with 1. If the value is 0, it is regarded as
1. If the value is negative, obtain a substring of the specified length backwards starting from the last
character in the string. Examples Input example

| str (VARCHAR) | nullstr (VARCHAR) |
|---|---|
| k1 = v1; k2 = v2 | null |

Sample code

```
SELECT SUBSTRING('', 222222222) as var1,
       SUBSTRING(str, 2) as var2,
       SUBSTRING(str, -2) as var3,
       SUBSTRING(str, -2, 1) as var4,
       SUBSTRING(str, 2, 1) as var5,
       SUBSTRING(str, 22) as var6,
       SUBSTRING(str, -22) as var7,
       SUBSTRING(str, 1) as var8,
       SUBSTRING(str, 0) as var9,
       SUBSTRING(nullstr, 0) as var10
FROM T1
```

Output example

| var1 (VARCH AR) | var2 (VARCH AR) | var3 (VARCH AR) | var4 (VARCH AR) | var5 (VARCH AR) | var6 (VARCH AR) | var7 (VARCH AR) | var8 (VARCH AR) | var9 (VARCH AR) | var10 (VARCH AR) |
|---|---|---|---|---|---|---|---|---|---|
| "" | 1 = v1; k2 = v2 | v2 | v | 1 | "" | "" | k1 = v1; k2 = v2 | k1 = v1; k2 = v2 | null |

##### 1.11.1.26 TO_BASE64

Syntax

```
VARCHAR TO_BASE64(bin)
```

Argument bin: specifies a value of the BINARY type. Description Convert the input value of the BINARY type to a Base64 string. Examples Input example c (VARCHAR) SGVsbG8gd29ybGQ = SGk = SGVsbG8 =

```
SELECT TO_BASE64(FROM_BASE64(c)) as var1 FROM T1
```

Output example var1 (VARCHAR) SGVsbG8gd29ybGQ = SGk = SGVsbG8 =

##### 1.11.1.27 TRIM

Syntax

```
VARCHAR TRIM( VARCHAR x )
```

Arguments x: VARCHAR type Description Trim leading or trailing characters from a string. The most common use is to trim leading or trailing blank spaces. Examples Test example

```
SELECT TRIM(' Sample '); as result FROM T1
```

Output example result(VARCHAR) Sample

##### 1.11.1.28 UPPER

Syntax

```
VARCHAR UPPER(A)
```

Arguments A: VARCHAR type Convert the specified string to a string of uppercase letters. Examples Input example var1(VARCHAR) ss ttee Sample code

```
SELECT UPPER(var1) as aa FROM T1;
```

Output example aa(VARCHAR) SS TTEE

#### 1.11.2 Mathematical unctions

##### 1.11.2.1 Addition

Syntax

```
A + B
```

Arguments A and B: INT type Description Return the result of adding B to A. Examples Input example

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 10 | 20 | 30 |

Sample code

```
SELECT int1+int2+int3 as aa FROM T1;
```

Output example aa(INT)

##### 1.11.2.2 Subtraction

Syntax

```
A – B
```

Arguments A and B: specify values of the INT type. Description Return the result of subtracting B from A. Examples Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 10 | 10 | 30 |

Sample code

```
SELECT int3 - int2 - int1 as aa FROM T1;
```

Output example aa (INT)

##### 1.11.2.3 Multiplication

Syntax

```
A * B
```

Arguments A and B: specify values of the INT type. Description Return the result of multiplying A by B. Examples Input example

| int1 (INT) | int2 (INT) | int3 (INT) |
|---|---|---|
| 10 | 20 | 3 |

Sample code

```
SELECT int1*int2*int3 as aa FROM T1;
```

Output example aa (INT)

##### 1.11.2.4 Division

Syntax

```
A/B
```

Arguments A and B: INT type Description Return the result of dividing A by B.

| int1(INT) | int2 (INT) |
|---|---|
| 8 | 4 |

Sample code

```
SELECT int1 / int2 as aa FROM T1;
```

Output example aa(INT)

##### 1.11.2.5 ABS

Syntax

```
DOUBLE ABS(A)
```

Arguments A: DOUBLE type Description Return the absolute value of the specified number. Examples Input example int1(DOUBLE) 4.3 Sample code

```
SELECT ABS(in1) as aa FROM T1;
```

Output example aa(DOUBLE) 4.3

##### 1.11.2.6 ACOS

Syntax

```
DOUBLE ACOS(A)
```

Argument A: specifies a number of DOUBLE type. Description Return the arccos value of the specified number. Examples Input example int1 (DOUBLE) 0.7173560908995228 0.4 Sample code

```
SELECT ACOS(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 0.7707963267948966 1.1592794807274085

##### 1.11.2.7 BIN

Syntax

```
VARCHAR BIN(BIGINT number)
```

Arguments number: BIGINT type. INT type arguments support implicit conversion, whereas other types of arguments do not. Convert a value of the BIGINT type to a binary string. Input example

| id(INT) | x (BIGINT) |
|---|---|
| 1 | 12L |
| 2 | 10L |
| 3 | 0L |
| 4 | 10000000000L |

Sample code

```
SELECT id, bin(x) as var1 FROM T1
```

Output example

| id(INT) | var1(VARCHAR) |
|---|---|
| 1 | 1100 |
| 2 | 1010 |
| 3 | 0 |
| 4 | 1001010100000010111110010000000000 |

##### 1.11.2.8 ASIN

Syntax

```
DOUBLE ASIN(A)
```

Arguments A: DOUBLE type Description Return the arcsine value of the specified number. Examples int1 (DOUBLE) 0.7173560908995228 0.4 Sample code

```
SELECT ASIN(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 0.8 0.41151684606748806

##### 1.11.2.9 ATAN

Syntax

```
DOUBLE ATAN(A)
```

Arguments A: DOUBLE type Description Return the arctangent value of the specified number. Examples Input example int1 (DOUBLE) 0.7173560908995228 0.4 Sample code

```
SSELECT ATAN(in1) as aa FROM T1;
```

aa (DOUBLE) 0.6222796222326533 0.3805063771123649

##### 1.11.2.10 BITAND

Syntax

```
INT BITAND(INT number1,INT number2)
```

Arguments number1: specifies a common argument of the INT type. number2: specifies a common argument of the INT type. Description Perform a bitwise AND operation on the specified values. The input and output values are both of the INT type. Examples Input example

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

Sample code

```
SELECT BITAND(a, b) as intt FROM T1
```

Output example intt(INT)

##### 1.11.2.11 BITNOT

Syntax

```
INT BITNOT((INT number)
```

Arguments number: specifies a common argument of the INT type. Perform a bitwise NOT operation on the specified value. The input and output values are both integers. Examples Input example a(INT) Sample code

```
SELECT BITNOT(a) as var1, FROM T1
```

Output example var1(INT) 0xfff8

##### 1.11.2.12 BITOR

Syntax

```
INT BITOR(INT number1, INT number2)
```

Arguments number1: specifies a common argument of the INT type. number2: specifies a common argument of the INT type. Description Perform a bitwise OR operation on the specified values. The input and output values are both of the INT type. Examples Input example

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

```
SELECT BITOR(a, b) as var1, FROM T1
```

Output example var1(INT)

##### 1.11.2.13 BITXOR

Syntax

```
INT BITXOR(INT number1, INT number2)
```

Arguments number1: specifies a common value of the INT type. number2: specifies a common value of the INT type. Description Return the bitwise XOR (exclusive OR) of two given numbers. The argument and result are both of the INT type. Examples Input example

| a (INT) | b (INT) |
|---|---|
| 2 | 3 |

Sample code

```
SELECT BITXOR(a, b) as var1, FROM T1
```

Output example var1 (INT)

##### 1.11.2.14 CARDINALITY

```
CARDINALITY(str)
```

Arguments str: specifies an array. Description Return the number of elements in an array. Examples Input example

| str(INT) | b (Array[INT]) |
|---|---|
| 1 | Array(1, 2, 3) |

Sample code

```
SELECT cardinality(b) AS result FROM T1
```

Output example result(INT)

##### 1.11.2.15 COS

Syntax

```
DOUBLE COS(A)
```

Arguments A: DOUBLE type Description Return the cosine value of the specified number. Examples Input example in1(DOUBLE) 0.8

|   | Developer Guide·Flink SQL Realtime Comput | e |
|---|---|---|

in1(DOUBLE) 0.4 Sample code

```
SELECT COS(in1) as aa FROM T1;
```

Output example aa(DOUBLE) 0.6967067093471654 0.9210609940028851

##### 1.11.2.16 COT

Syntax

```
DOUBLE COT(A)
```

Arguments A: specifies a value of the DOUBLE type. Description Return the cotangent value of the specified number. Examples Input example in1 (DOUBLE) 0.8 0.4 Sample code

```
SELECT COT(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 1.0296385570503641 0.4227932187381618

##### 1.11.2.17 E

Syntax

```
DOUBLE E()
```

Arguments DOUBLE type Description Return the DOUBLE type value of natural constant E. Examples Input example

| id(INT) | X(DOUBLE) |
|---|---|
| 1 | 8.0 |

Sample code

```
SELECT id, e() as dou1, E() as dou2 FROM T1
```

Output example

| id(INT) | dou1(DOUBLE) | dou2 (DOUBLE) |
|---|---|---|
| 1 | 2.718281828459045 | 2.718281828459045 |

##### 1.11.2.18 EXP

Syntax

```
DOUBLE EXP(A)
```

Argument A: specifies a value of the DOUBLE type. Return the power of e, where e is the base of the natural logarithm. Examples Input example in1 (DOUBLE) 8.0 10.0 Sample code

```
SELECT EXP(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 2980.9579870417283 22026.465794806718

##### 1.11.2.19 FLOOR

Syntax

```
DOUBLE FLOOR(A)
```

Arguments A: DOUBLE type Description Return the maximum integer that is less than or equal to the provided number. Examples Input example in1(DOUBLE) 8.123 10.321

```
SELECT FLOOR(in1) as aa FROM T1;
```

Output example aa(INT)

##### 1.11.2.20 LN

Syntax

```
DOUBLE ln(DOUBLE number)
```

Arguments number: specifies a number of the DOUBLE type. If the input value is of the VARCHAR or BIGINT type, it is implicitly converted to the DOUBLE type before an operation. Description Return the natural logarithm of the specified number. The return value is a logarithm of the DOUBLE type. Examples Input example

| ID (INT) | X (DOUBLE) |
|---|---|
| 1 | 100.0 |
| 2 | 8.0 |

Sample code

```
SELECT id, ln(x) as dou1, ln(e()) as dou2 FROM T1
```

Output example

| ID (INT) | dou1 (DOUBLE) | dou2 (DOUBLE) |
|---|---|---|
| 1 | 4.605170185988092 | 1.0 |

| Developer Guide·Flink SQL |   | Realtime Comput |
|---|---|---|

| ID (INT) | dou1 (DOUBLE) | dou2 (DOUBLE) |
|---|---|---|
| 2 | 2.0794415416798357 | 1.0 |

##### 1.11.2.21 LOG

Syntax

```
DOUBLE LOG(DOUBLE base, DOUBLE x) DOUBLE LOG(DOUBLE x)
```

Arguments base: specifies a value of the DOUBLE type. x: specifies a value of the DOUBLE type. Description Return the natural logarithm of x to the base specified by the base argument. The return value is a logarithm of the DOUBLE type. If there is only one argument value, the return value is a natural logarithm to the base specified by the argument. Examples Input example

| ID (INT) | BASE (DOUBLE) | X (DOUBLE) |
|---|---|---|
| 1 | 10.0 | 100.0 |
| 2 | 2.0 | 8.0 |

Sample code

```
SELECT id, LOG(base, x) as dou1, LOG(2) as dou2 FROM T1
```

Output example

| ID (INT) | dou1 (DOUBLE) | dou2 (DOUBLE) |
|---|---|---|
| 1 | 2.0 | 0.6931471805599453 |
| 2 | 3.0 | 0.6931471805599453 |

##### 1.11.2.22 LOG10

```
DOUBLE LOG10(DOUBLE x)
```

Argument x: specifies a value of the DOUBLE type. Description Return the base-10 logarithm of x. If x is NULL, the return value is NULL. If x is a negative number, an exception occurs. Examples Input example

| id (INT) | X (INT) |
|---|---|
| 1 | 100 |
| 2 | 10 |

Sample code

```
SELECT id, log10(x) as dou1 FROM T1
```

Output example

| ID (INT) | dou1 (DOUBLE) |
|---|---|
| 1 | 2.0 |
| 2 | 1.0 |

##### 1.11.2.23 LOG2

Syntax

```
DOUBLE LOG2(DOUBLE x)
```

Arguments x: specifies a multiple of 2. This argument is of the DOUBLE type. Description Return the base-2 logarithm of x. If x is NULL, the return value is NULL. If x is a negative number, an exception occurs.

| id (INT) | X (INT) |
|---|---|
| 1 | 8 |
| 2 | 2 |

Sample code

```
SELECT id, log2(x) as dou1 FROM T1
```

Output example

| ID (INT) | dou1 (DOUBLE) |
|---|---|
| 1 | 3.0 |
| 2 | 1.0 |

##### 1.11.2.24 PI

Syntax

```
DOUBLE PI( )
```

Description Obtain the ratio of circumference to diameter, namely, Pi. Examples Input example

| id (INT) | X (INT) |
|---|---|
| 1 | 8 |

Sample code

```
SELECT id, PI() as dou1 FROM T1
```

Output example

| ID (INT) | dou1 (DOUBLE) |
|---|---|
| 1 | 3.141592653589793 |

##### 1.11.2.25 POWER

Syntax

```
DOUBLE POWER(A, B)
```

Input parameters A and B: DOUBLE data type Description Returns the result of raising A to the power of B. Example Input example

| int1 (DOUBLE) | in2 (DOUBLE) |
|---|---|
| 2.0 | 4.0 |

Sample code

```
SELECT POWER(in1, in2) as aa FROM T1;
```

Output example aa (DOUBLE) 16.0

##### 1.11.2.26 RAND

Syntax

```
DOUBLE RAND([BIGINT seed])
```

Arguments seed: specifies a random number of the BIGINT type. This argument specifies the start number of a random number sequence. Description Return a random number of the DOUBLE type. The return value range is `[0, 1)` .

| id(INT) | X(INT) |
|---|---|
| 1 | 8 |

Sample code

```
SELECT id, rand(1) as dou1, rand(3) as dou2 FROM T1
```

Output example

| id(INT) | dou1(DOUBLE) | dou2(DOUBLE) |
|---|---|---|
| 1 | 0.7308781907032909 | 0.731057369148862 |

##### 1.11.2.27 SIN

Syntax

```
DOUBLE SIN(A)
```

Arguments A: specifies a number of the DOUBLE type. Description Return the sine value of the specified number. Examples Input example in1 (DOUBLE) 8.0 0.4 Sample code

```
SELECT SIN(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 0.9893582466233818 0.3894183423086505

##### 1.11.2.28 SQRT

Syntax

```
DOUBLE SQRT(A)
```

Arguments A: specifies a number of the DOUBLE type. Description Return the square root of the specified number. Examples Input example in1 (DOUBLE) 8.0 Sample code

```
SELECT SQRT(in1) as aa FROM T1;
```

Output example aa (DOUBLE) 2.8284271247461903

##### 1.11.2.29 TAN

Syntax

```
DOUBLE TAN(A)
```

Arguments A: DOUBLE type Return the tangent value of the specified number. Examples Input example in1(DOUBLE) 8.0 0.4 Sample code

```
SELECT TAN(in1) as aa FROM T1;
```

Output example aa(DOUBLE) 1.0296385570503641 0.4227932187381618

##### 1.11.2.30 CEIL

Syntax

```
value_class CEIL(value)
```

Arguments value: specifies a value of the INT, DOUBLE, or BIGINT type. Description Return the smallest integer greater than or equal to a specified value. The value_class data type returned by CEIL is the same as that of the argument. Examples Input example

| ID (INT) | value1 (INT) | value2 (DOUBLE) |
|---|---|---|
| 1 | 3 | 3.6 |

```
SELECT CEIL (value2) as result1 SELECT CEIL (value2) as result2 FROM T1
```

Output example

| ID (INT) | result1 (INT) | result2 (DOUBLE) |
|---|---|---|
| 1 | 3 | 4.0 |

##### 1.11.2.31 CHARACTER_LENGTH

Syntax

```
INTEGER CHARACTER_LENGTH( VARCHAR x )
```

Arguments x: specifies a value of the VARCHAR type. Description Return the number of characters contained in a string. Examples Input example

| ID (INT) | X (VARCHAR) |
|---|---|
| 1 | StreamCompute |

Sample code

```
SELECT CHARACTER_LENGTH( x ) as result FROM T1
```

Output example

| ID (INT) | result (INT) |
|---|---|
| 1 | 13 |

##### 1.11.2.32 DEGREES

```
DOUBLE DEGREES(double x)
```

Arguments x: specifies a radian value of the DOUBLE type. Description Return the result of converting radians to degrees. Examples Sample code

```
SELECT DEGREES( PI() ) as result FROM T1
```

Output example result(DOUBLE) 180.0

##### 1.11.2.33 MOD

Syntax

```
Integer MOD(Integer x,Integer y)
```

Arguments x: specifies a value of the Integer type. y: specifies a value of the Integer type. Description Return the remainder when integer x is divided by integer y, without considering the quotient. When x is a negative integer or both x and y are negative integers, the result is negative. Examples Input example

| X (INT) | Y (INT) |
|---|---|
| 29 | 3 |
| -29 | 3 |
| -29 | -3 |

```
SELECT MOD(x,y) as result FROM T1
```

Output example

| ID (INT) | result (INT) |
|---|---|
| 1 | 2 |
| 2 | -2 |
| 3 | -2 |

##### 1.11.2.34 ROUND

Syntax

```
DECIMAL ROUND(DECIMAL x, INT n)
```

Argument x: DECIMAL type Description Round the x argument's value to n decimal places. Examples Input example in1 (DECIMAL) 0.7173560908995228 0.4 Sample code

```
SELECT ROUND(in1,2) as `result` FROM T1;
```

Output example result (DECIMAL) 0.72 0.40

#### 1.11.3 Date functions

##### 1.11.3.1 CURRENT_TIMESTAMP

Syntax Arguments None Description Return the current UTC (GMT+0) timestamp, which is eight hours earlier than Beijing time. Examples Sample code

```
SELECT CURRENT_TIMESTAMP as var1 FROM T1
```

Output example var1 (TIMESTAMP) 2007-04-30 13:10:02.047

##### 1.11.3.2 DATEDIFF

Syntax

```
INT DATEDIFF(VARCHAR enddate, VARCHAR startdate) INT DATEDIFF(TIMESTAMP enddate, VARCHAR startdate) INT DATEDIFF(VARCHAR enddate, TIMESTAMP startdate) INT DATEDIFF(TIMESTAMP enddate, TIMESTAMP startdate)
```

Arguments startdate: specifies a start date of the TIMESTAMP or VARCHAR type. The format of a VARCHAR type date is yyyy-MM-dd or yyyy-MM-dd HH:mm:ss. enddate: specifies an end date of the TIMESTAMP or VARCHAR type. The format of a VARCHAR type date is yyyy-MM-dd or yyyy-MM-dd HH:mm:ss. Description Compute the number of days between the specified start date and end date. The return value is an integer of the TIMESTAMP type or in the format of `yy-MM-dd HH:mm:ss` or `yy-MM-dd` . If any argument is NULL or a parsing error occurs, the return value is NULL. Examples Input example

| datetime1(VARCHAR) | datetime2 (VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | null |

Sample code

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as int7
FROM T1
```

Output example

| int1(INT) | int2(INT) | int3(INT) | int4(INT) | int5(INT) | int6(INT) | int7 (INT) |
|---|---|---|---|---|---|---|
| 30 | 31 | -31 | null | null | null | 31 |

##### 1.11.3.3 DATE_ADD

Syntax

```
VARCHAR DATE_ADD(VARCHAR startdate, INT days) VARCHAR DATE_ADD(TIMESTAMP time, INT days)
```

Arguments startdate: specifies a date of the VARCHAR type. The format is yyyy-MM-dd or yyyy-MM-dd HH:mm:ss. time: specifies a date of the TIMESTAMP type. days: specifies the number of days of the INT type. Description Return a date that is X (specified by days) days after the specified date of the VARCHAR type. The date format can be yyyy-MM-dd hh:mm:ss, yyyy-MM-dd, and timestamp string. The return value is a string type date in the format of yyyy-MM-dd. If any argument is NULL or a parsing error occurs, the return value is NULL.

| datetime1 (VARCHAR) | nullstr (VARCHAR) |
|---|---|
| 2017-09-15 00:00:00 | null |

Sample code

```
SELECT DATE_ADD(datetime1, 30) as var1,
        DATE_ADD(TIMESTAMP '2017-09-15 23:00:00',30) as var2,
        DATE_ADD(nullstr,30) as var3
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) |
|---|---|---|
| 2017-10-15 | 2017-10-15 | null |

##### 1.11.3.4 DATE_FORMAT

Syntax

```
VARCHAR DATE_FORMAT(TIMESTAMP time, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR from_format, VARCHAR to_format)
```

Input parameters date: specifies a date of the VARCHAR data type. The default format is yyyy-MM-dd HH:mm:ss. time: specifies a date of the TIMESTAMP data type. from_format: specifies a source date format. to_format: specifies a target date format. Description Converts a specified date from a source format to a target format. The date or time parameter specifies a date. The from_format parameter is optional and specifies the source date format. The default format is yyyy-MM-dd hh:mm:ss. The to_format parameter specifies the target date format. The return value is a date in the specified target format. If any argument is NULL or a parsing error occurs, the return value is NULL. Example Input example

| date1 (VARCHAR) | datetime1 (VARCHAR) | nullstr (VARCHAR) |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | null |

Sample code

```
SELECT DATE_FORMAT(datetime1, 'yyMMdd') as var1,
        DATE_FORMAT(nullstr, 'yyMMdd') as var2,
        DATE_FORMAT(datetime1, nullstr) as var3,
        DATE_FORMAT(date1, 'MMdd-yyyy', nullstr) as var4,
        DATE_FORMAT(date1, 'MMdd-yyyy', 'yyyyMMdd') as var5,
        DATE_FORMAT(TIMESTAMP '2017-09-15 23:00:00', 'yyMMdd') as var6
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) | var4 (VARCHAR) | var5 (VARCHAR) | var6 (VARCHAR) |
|---|---|---|---|---|---|
| 170915 | null | null | null | 20170915 | 170915 |

##### 1.11.3.5 DATE_SUB

Syntax

```
VARCHAR DATE_SUB(VARCHAR startdate, INT days) VARCHAR DATE_SUB(TIMESTAMP time, INT days)
```

Arguments startdate: specifies a date of the VARCHAR type. The format is yyyy-MM-dd or yyyy-MM-dd HH:mm:ss. time: specifies a date of the TIMESTAMP type. days: specifies the number of days. This argument is of the INT type. Description Return the date that is X (specified by days) days before the specified date. The return value is a VARCHAR type date in the format of yyyy-MM-dd. If any argument is NULL or a parsing error occurs, the return value is NULL. Examples Input example

| date1 (VARCHAR) | nullstr (VARCHAR) |
|---|---|
| 2017-10-15 | null |

```
SELECT DATE_SUB(date1, 30) as var1,
        DATE_SUB(TIMESTAMP '2017-10-15 23:00:00',30) as var2,
        DATE_SUB(nullstr,30) as var3
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) |
|---|---|---|
| 2017-09-15 | 2017-09-15 | null |

##### 1.11.3.6 DAYOFMONTH

Syntax

```
 INT DAYOFMONTH(TIMESTAMP time)
 INT DAYOFMONTH(DATE date)
```

Arguments date: specifies a date of the DATE type. time: specifies a date of the TIMESTAMP type. Description Return the day number of the specified timestamp or date. Valid range: [1,31]. Examples Input example

| tsStr (VARCHAR) | dateStr (VARCHAR) | tdate (DATE) | ts (TIMESTAMP) |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

Sample code

```
SELECT DAYOFMONTH(TIMESTAMP '2016-09-15 00:00:00') as int1,
       DAYOFMONTH(DATE '2017-09-22') as int2,
       DAYOFMONTH(tdate) as int3,
       DAYOFMONTH(ts) as int4,
       DAYOFMONTH(CAST(dateStr AS DATE)) as int5,
       DAYOFMONTH(CAST(tsStr AS TIMESTAMP))  as int6
FROM T1
```

| int1 (INT) | int2 (INT) | int3 (INT) | int4 (INT) | int5 (INT) | int6 (INT) |
|---|---|---|---|---|---|
| 15 | 22 | 10 | 15 | 15 | 15 |

##### 1.11.3.7 FROM_UNIXTIME

Syntax

```
 VARCHAR FROM_UNIXTIME(BIGINT unixtime[, VARCHAR format])
```

Arguments unixtime: specifies a Unix timestamp (in seconds) of the BIGINT type. An exception occurs if this argument is of another type. format: specifies the target date format of the VARCHAR type. The default format is yyyy-MM-dd hh:mm:ss. This argument is optional. Description Return a VARCHAR type date in the specified date format. The default format is yyyy-MM-dd HH:mm:ss. If any argument is NULL or a parsing error occurs, the return value is NULL. Examples Input example

| unixtime1(INT) | nullstr(VARCHAR) |
|---|---|
| 1505404800 | null |

Sample code

```
SELECT FROM_UNIXTIME(unixtime1) as var1,
        FROM_UNIXTIME(unixtime1,'MMdd-yyyy') as var2,
        FROM_UNIXTIME(unixtime1,nullstr) as var3
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) |
|---|---|---|
| 2017-09-15 00:00:00 | 0915-2017 | null |

##### 1.11.3.8 HOUR

```
  INT HOUR(TIMESTAMP timestamp)
 INT HOUR(TIME time)
```

Arguments time: specifies a time value of the TIME type. time: specifies a time value of the TIMESTAMP type. Description Return the hours (in 24-hour format) from the specified time or timestamp string. The return value ranges from 0 to 23. Examples Input example

| datetime1 (VARCHAR) | time1 (VARCHAR) | time2 (TIME) | timestamp1 (TIMESTAMP) |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

Sample code

```
SELECT HOUR(TIMESTAMP '2016-09-20 23:33:33') as int1,
       HOUR(TIME '23:30:33') as int2,
       HOUR(time2) as int3,
       HOUR(timestamp1) as int4,
       HOUR(CAST(time1 AS TIME)) as int5,
       HOUR(CAST(datetime1 AS TIMESTAMP)) as int6
FROM T1
```

Output example

| int1 (INT) | int2 (INT) | int3 (INT) | int4 (INT) | int5 (INT) | int6 (INT) |
|---|---|---|---|---|---|
| 23 | 23 | 22 | 11 | 22 | 11 |

##### 1.11.3.9 LOCALTIME

Syntax

```
TIME LOCALTIME
```

Arguments The function is a non-parameterized constructor and can be used directly as a variable. Return the current time of the TIME type in the session time zone. Sample code

```
SELECT LOCALTIME as `result` FROM T1
```

Output example result(TIME) 19:00:47

##### 1.11.3.10 MINUTE

Syntax

```
INT MINUTE(TIMESTAMP timestamp)
 INT MINUTE(TIME time)
```

Arguments time: specifies a time value of the TIME type. time: specifies a time value of the TIMESTAMP type. Description Return the minutes from the specified time value. Valid range: [0, 59]. Examples Input example

| datetime1 (VARCHAR) | time1 (VARCHAR) | time2 (TIME) | timestamp1 (TIMESTAMP) |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

Sample code

```
SELECT MINUTE(TIMESTAMP '2016-09-20 23:33:33') as int1,
       MINUTE(TIME '23:30:33') as int2,
       MINUTE(time2) as int3,
       MINUTE(timestamp1) as int4,
       MINUTE(CAST(time1 AS TIME)) as int5,
       MINUTE(CAST(datetime1 AS TIMESTAMP)) as int6
FROM T1
```

| int1 (INT) | int2 (INT) | int3 (INT) | int4 (INT) | int5 (INT) | int6 (INT) |
|---|---|---|---|---|---|
| 33 | 30 | 23 | 12 | 23 | 12 |

##### 1.11.3.11 MONTH

Syntax

```
INT MONTH(TIMESTAMP time)
 INT MONTH(DATE date)
```

Arguments time: specifies a time value of the TIMESTAMP type. date: specifies a time value of the TIME type. Description Return the month number of the specified time or date. Valid range: [1, 12]. Examples Input example

| tsStr (VARCHAR) | dateStr (VARCHAR) | tdate (DATE) | ts (TIMESTAMP) |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

Sample code

```
SELECT MONTH(TIMESTAMP '2016-09-15 00:00:00') as int1,
       MONTH(DATE '2017-09-22') as int2,
       MONTH(tdate) as int3,
       MONTH(ts) as int4,
       MONTH(CAST(dateStr AS DATE)) as int5,
       MONTH(CAST(tsStr AS TIMESTAMP))  as int6
FROM T1
```

Output example

| int1 (INT) | int2 (INT) | int3 (INT) | int4 (INT) | int5 (INT) | int6 (INT) |
|---|---|---|---|---|---|
| 9 | 9 | 11 | 10 | 9 | 10 |

##### 1.11.3.12 NOW

```
BIGINT NOW()
```

Arguments If no argument is specified, the Unix timestamp (in seconds) of the current system time is returned. Description Return the Unix timestamp (in seconds) of the current time zone. You can also specify an INT type argument as an offset (in seconds) and use UNIX_TIMESTAMP(CAST(NOW AS VARCHAR)) to convert the INT type argument to a timestamp value. Then add the offset to the current timestamp to return a value. Examples Input example b(VARCHAR) null Sample code

```
SELECT NOW() as big1, NOW(b) as big2 FROM T1
```

Output example

| big1(BIGINT) | big2 (BIGINT) |
|---|---|
| 1403006911 | null |

##### 1.11.3.13 SECOND

Syntax

```
INT SECOND(TIMESTAMP timestamp)
 INT SECOND(TIME time)
```

Arguments time: specifies a time value of the TIME type. time: specifies a time value of the TIMESTAMP type. Description Extract the seconds from the specified time value. The return value ranges from 0 to 59.

| datetime1(VARCHAR) | time1 (VARCHAR) | time2(TIME) | timestamp1(TIMESTAMP ) |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

Sample code

```
SELECT SECOND(TIMESTAMP '2016-09-20 23:33:33') as int1,
       SECOND(TIME '23:30:33') as int2,
       SECOND(time2) as int3,
       SECOND(timestamp1) as int4,
       SECOND(CAST(time1 AS TIME)) as int5,
       SECOND(CAST(datetime1 AS TIMESTAMP)) as int6
FROM T1
```

Output example

| int1(INT) | int2(INT) | int3(INT) | int4 (INT) | int5 (INT) | int6 (INT) |
|---|---|---|---|---|---|
| 33 | 33 | 24 | 13 | 24 | 13 |

##### 1.11.3.14 TIMESTAMPADD

Syntax

```
TIMESTAMP TIMESTAMPADD(interval,INT int_expr,TIMESTAMP datetime_expr) DATE TIMESTAMPADD(interval,INT int_expr,DATE datetime_expr)
```

Input parameters interval

| FRAC SECOND _ | Specifies an interval in milliseconds. |
|---|---|
| SECOND | Specifies an interval in seconds. |
| MINUTE | Specifies an interval in minutes. |
| HOUR | Specifies an interval in hours. |
| DAY | Specifies an interval in days. |
| WEEK | Specifies an interval in weeks. |
| MONTH | Specifies an interval in months. |
| QUARTER | Specifies an interval in quarters. |

| YEAR | Specifies an interval in years. |
|---|---|

int_expr: specifies an increment that is an integer. datetime_expr: specifies a timestamp or date to which the increment is to be added. Description The data type of a result returned by the TIMESTAMPADD function is the same as that of datetime_expr. The TIMESTAMPADD function adds an increment (int_expr) to a timestamp or date (datetime_expr) and returns the updated time. Example Input example

| a (TIMESTAMP) | b (DATE) |
|---|---|
| 2018-07-09 10:23:56 | 1990-02-20 |

Sample code

```
SELECT TIMESTAMPADD(HOUR,3,a) AS `result1`, TIMESTAMPADD(DAY,3,b) AS `result2` FROM T1
```

Output example

| result1 (TIMESTAMP) | result2 (DATE) |
|---|---|
| 2018-07-09 13:23:56 | 1990-02-23 |

##### 1.11.3.15 TO_DATE

Syntax

```
Date TO_DATE(INT time) Date TO_DATE(VARCHAR date) Date TO_DATE(VARCHAR date, VARCHAR format)
```

Input parameters time: specifies the number of days from January 1, 1970 to a specified date. This parameter is of the INT data type. date: specifies a date of the VARCHAR data type. The default format is yyyy-MM-dd. format: specifies a date format of the VARCHAR data type. Converts a date of the INT or VARCHAR data type into a date of the DATE data type. Example

| date1 (bigint) | date2 (VARCHAR) | date3 (VARCHAR) |
|---|---|---|
| 100 | 2017-09-15 | 20170915 |

Sample code

```
SELECT TO_DATE(date1) as var1,
        TO_DATE(date2) as var2,
        TO_DATE(date3, "yyyyMMdd") as var3
FROM T1
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) | var3 (VARCHAR) |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### 1.11.3.16 TO_TIMESTAMP

Syntax

```
TIMESTAMP TO_TIMESTAMP(BIGINT time) TIMESTAMP TO_TIMESTAMP(VARCHAR date) TIMESTAMP TO_TIMESTAMP(VARCHAR date, VARCHAR format)
```

Arguments time: specifies a time value of the BIGINT type. The unit is milliseconds. date: specifies a date of the VARCHAR type. The default format is yyyy-MM-dd HH:mm:ss[. SSS]. format: specifies the source date format of the VARCHAR type. Description Convert a date of the BIGINT or VARCHAR type to a date of the TIMESTAMP type. Examples Input example

| timestamp1 (bigint) | timestamp2 (VARCHAR) | timestamp3 (VARCHAR) |
|---|---|---|
| 1513135677000 | 2017-09-15 00:00:00 | 20170915000000 |

```
SELECT TO_TIMESTAMP(timestamp1) as var1,
        TO_TIMESTAMP(timestamp2) as var2,
        TO_TIMESTAMP(timestamp3, "yyyyMMddHHmmss") as var3
FROM T1
```

Output example

| var1 (TIMESTAMP) | var2 (TIMESTAMP) | var3 (TIMESTAMP) |
|---|---|---|
| 2017-12-13 03:27:57.0 | 2017-09-15 00:00:00.0 | 2017-09-15 00:00:00.0 |

##### 1.11.3.17 UNIX_TIMESTAMP

Syntax

```
BIGINT UNIX_TIMESTAMP() BIGINT UNIX_TIMESTAMP(VARCHAR date) BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

Arguments date: specifies a date of the VARCHAR type. The default format is yyyy-MM-dd HH:mm:ss. format: specifies the source date format of the VARCHAR type. The default format is yyyy-MM-dd HH:mm:ss. Description Convert the specified date to a Unix timestamp (in seconds) of the BIGINT type. Both the date and format parameters are optional. If neither is specified, the Unix timestamp (in seconds) of the current time is returned. If any argument is NULL or a parsing error occurs, the return value is NULL. Examples Input example nullstr (VARCHAR) null Sample code

```
SELECT UNIX_TIMESTAMP() as big1,
        UNIX_TIMESTAMP(nullstr) as big2
FROM T1
```

Output example

| big1 (BIGINT) | big2 (BIGINT) |
|---|---|
| 1403006911 | null |

##### 1.11.3.18 WEEK

Syntax

```
INT WEEK(DATE date) INT WEEK(TIMESTAMP time)
```

Arguments date: specifies a date of the DATE type. time: specifies a date of the TIMESTAMP type. Description Calculate the week number of the specified date in the year. The valid week number range is from 1 to 53. Examples Input example

| dateStr(VARCHAR) | date1 (DATE) | ts1 (TIMESTAMP) |
|---|---|---|
| 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

Sample code

```
SELECT WEEK(TIMESTAMP '2017-09-15 00:00:00') as int1,
        WEEK(date1) as int2, WEEK(ts1) as int3, WEEK(CAST(dateStr AS DATE)) as int4
FROM T1
```

Output example

| int1 (INT) | int2 (INT) | int3 (INT) | int4 (INT) |
|---|---|---|---|
| 37 | 45 | 41 | 37 |

##### 1.11.3.19 YEAR

Syntax

```
INT YEAR(TIMESTAMP time) INT YEAR(DATE date)
```

Arguments date: specifies a date of the DATE type. time: specifies a date of the TIMESTAMP type. Description Extract the year from the specified date. Examples Input example

| tsStr(VARCHAR) | dateStr(VARCHAR) | tdate (DATE) | ts(TIMESTAMP) |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

Sample code

```
SELECT YEAR(TIMESTAMP '2016-09-15 00:00:00') as int1,
       YEAR(DATE '2017-09-22') as int2,
       YEAR(tdate) as int3,
       YEAR(ts) as int4,
       YEAR(CAST(dateStr AS DATE)) as int5,
       YEAR(CAST(tsStr AS TIMESTAMP))  as int6
FROM T1
```

Output example

| int1 (BIGINT) | int2 (BIGINT) | int3 (BIGINT) | int4 (BIGINT) | int5 (BIGINT) | int6 (BIGINT) |
|---|---|---|---|---|---|
| 2016 | 2017 | 2017 | 2017 | 2015 | 2017 |

#### 1.11.4 Conditional functions

##### 1.11.4.1 CASE WHEN

Syntax

```
CASE WHEN a THEN b [WHEN c THEN d]* [ELSE e] END
```

Input parameters

| Parameter | Data type |
|---|---|
| a | BOOLEAN |
| b | BOOLEAN |
| c | BOOLEAN |

| Parameter | Data type |
|---|---|

| d | BOOLEAN |
|---|---|
| e | BOOLEAN |

Description If a is true, b is returned. If a is false and c is true, d is returned. If both a and c are false, e is returned. Example Not e If the CASE WHEN function returns a constant string, spaces are added after the string. An example is described as follows. When the return value is "ios", several spaces are added after this string.

```
case when device_type = 'android' then 'android' else 'ios' end as os
```

You can resolve the issue in the following two ways: Use the trim() method to remove the spaces. As shown in the following example, you can change os to trim(os) in the statement. Use the cast() method to convert the constant string into the VARCHAR data type. Input example device_type (VARCHAR) android ios win Sample code 1: using the trim() method

```
SELECT
   trim(os), // The trim() method is used.
   CHAR_LENGTH(trim(os)) // The trim() method is used.
from(
   SELECT
     case when device_type = 'android'
     then 'android'
     else 'ios'
end as os FROM T1
```

); Sample code 2: using the cast() method

```
SELECT
 os,
CHAR_LENGTH(os) from (SELECT
 case when device_type = 'android'
 then cast('android' as varchar) // The cast() method is used.
 else cast('ios' as varchar) // The cast() method is used.
end as os FROM T1
```

); Output example

| os (VARCHAR) | length (INT) |
|---|---|
| android | 7 |
| ios | 3 |
| ios | 3 |

##### 1.11.4.2 COALESCE

Syntax

```
 COALESCE(A,B,...)
```

Arguments A and B: specify values to be checked. NULL values are allowed in the list of values. Non-NULL values in the list must be of the same type. Otherwise, an exception occurs. The return type is the same as the argument type. Return the first non-NULL value in the specified list. If all values in the list are NULL, the return value is NULL. Not e The list must contain at least one argument. Otherwise, an exception occurs. Examples Input example

| var1(VARCHAR) | var2(VARCHAR) |
|---|---|
| null | 30 |

Sample code

```
SELECT COALESCE(var1,var2) as aa FROM T1;
```

Output example aa(VARCHAR)

##### 1.11.4.3 IF

Syntax

```
T IF(BOOLEAN testCondition, T valueTrue, T valueFalseOrNull)
```

Not e T indicates any return type. Arguments testCondition: BOOLEAN type valueTrue and valueFalseOrNull: These two arguments must be of the same type. The specific type is not restricted. Description Use the BOOLEAN value of testCondition as the criterion. If the value is true, valueTrue is returned. If the value is false, valueFalseOrNull is returned. If testCondition is NULL, valueFalseOrNull is returned. If any other argument is NULL, the operation is performed based on normal semantics, and the return value is of the T type. Examples Input example

| int1(INT) | int2(INT) | str1(VARCHAR) | str2(VARCHAR) |
|---|---|---|---|
| 1 | 2 | Jack | Harry |
| 1 | 2 | Jack | null |
| 1 | 2 | null | Harry |

Sample code

```
SELECT IF(int1 < int2,str1, str2) as int1 FROM T1
```

Output example int1(VARCHAR) Jack Jack null

##### 1.11.4.4 IS_ALPHA

Syntax

```
BOOLEAN IS_ALPHA(VARCHAR str)
```

Arguments str: specifies a string of the VARCHAR type. Description Check whether the specified string contains only letters. If it contains only letters, TRUE is returned. Otherwise, FALSE is returned. Examples Input example

| e (VARCHAR) | f (VARCHAR) | g (VARCHAR) |
|---|---|---|
| 3 | asd | null |

Sample code

```
SELECT IS_ALPHA(e) as boo1,IS_ALPHA(f) as boo2,IS_ALPHA(g) as boo3 FROM T1
```

| boo1 (BOOLEAN) | boo2 (BOOLEAN) | boo3 (BOOLEAN) |
|---|---|---|
| false | Yes | false |

##### 1.11.4.5 IS_DECIMAL

Syntax

```
 BOOLEAN IS_DECIMAL(VARCHAR str)
```

Input parameter str: specifies a string of the VARCHAR data type. Description If a specified string contains only decimal characters, true is returned. Otherwise, false is returned. Example Input example

| a (VARCHAR) | b (VARCHAR) | c (VARCHAR) | d (VARCHAR) | e (VARCHAR) | f (VARCHAR) | g (VARCHAR) |
|---|---|---|---|---|---|---|
| 1 | 123 | 2 | 11.4445 | 3 | asd | null |

Sample code

```
SELECT IS_DECIMAL(a) as boo1,IS_DECIMAL(b) as boo2,IS_DECIMAL(c) as boo3,
       IS_DECIMAL(d) as boo4,IS_DECIMAL(e) as boo5,IS_DECIMAL(f) as boo6,IS_DECIMAL(g) as b
oo7 FROM T1
```

Output example

| boo1 (BOOLEAN) | boo2 (BOOLEAN) | boo3 (BOOLEAN) | boo4 (BOOLEAN) | boo5 (BOOLEAN) | boo6 (BOOLEAN) | boo7 (BOOLEAN) |
|---|---|---|---|---|---|---|
| true | true | true | true | true | false | false |

##### 1.11.4.6 IS_DIGIT

Syntax

```
 BOOLEAN IS_DIGIT(VARCHAR str)
```

Arguments str: specifies a string of the VARCHAR type. Description Check whether the specified string contains only digits. If it only contains digits, TRUE is returned. Otherwise, FALSE is returned. The return value is of the BOOLEAN type. Examples Input example

| e(VARCHAR) | f(VARCHAR) | g(VARCHAR) |
|---|---|---|
| 3 | asd | null |

Sample code

```
SELECT IS_DIGIT(e) as boo1,IS_DIGIT(f) as boo2,IS_DIGIT(g) as boo3 FROM T1
```

Output example

| boo1(BOOLEAN) | boo2(BOOLEAN) | boo3(BOOLEAN) |
|---|---|---|
| true | false | false |

##### 1.11.4.7 NULLIF

Syntax

```
 NULLIF(A,B)
```

Arguments A and B: INT type Description If A and B have the same value, null is returned. If A and B have different values, the value of the first argument is returned. Examples Input example

| var1(INT) | var2(INT) |
|---|---|
| 30 | 30 |

```
SELECT NULLIF(var1,var2) as aa FROM T1;
```

Output example aa(VARCHAR) null

#### 1.11.5 Table-valued functions

##### 1.11.5.1 GENERATE_SERIES

Syntax

```
 GENERATE_SERIES(INT from, INT to)
```

Arguments from: specifies a lower limit of the INT type. to: specifies an upper limit of the INT type. Description Generate a series of continuous values from the lower limit to the upper limit minus one. Examples Input example

| s(INT) | e(INT) |
|---|---|
| 1 | 3 |
| -2 | 1 |

Sample code

```
SELECT s, e, v FROM T1, lateral table(GENERATE_SERIES(s, e)) as T(v)
```

Output example

| s(INT) | e(INT) | v(INT) |
|---|---|---|
| 1 | 3 | 1 |

| ealtime Compute |   | Developer Guide·Flink SQ |
|---|---|---|

| s(INT) | e(INT) | v(INT) |
|---|---|---|
| 1 | 3 | 2 |
| -2 | 1 | -2 |
| -2 | 1 | -1 |
| -2 | 1 | -0 |

##### 1.11.5.2 JSON_TUPLE

Syntax

```
JSON_TUPLE(str, path1, path2 ..., pathN)
```

Arguments str: specifies a JSON string. path1 to pathN: specify strings that represent paths, which do not need to begin with a dollar sign ($). Description Obtain the value represented by each path string from a JSON string. Examples Input example

| d(VARCHAR) | s(VARCHAR) |
|---|---|
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”a sd3”} | qwe3 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:” asd3”} | qwe2 |

Sample code

```
SELECT d, v FROM T1, lateral table(JSON_TUPLE(d, 'qwe', s)) as T(v)
```

Output example

| d(VARCHAR) | v(VARCHAR) |
|---|---|
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”a sd3”} | asd |

| Developer Guide·Flink SQL | Realtime Comput |
|---|---|

| d(VARCHAR) | v(VARCHAR) |
|---|---|
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”a sd3”} | asd3 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:” asd3”} | asd4 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:” asd3”} | asd5 |

##### 1.11.5.3 STRING_SPLIT

Syntax

```
STRING_SPLIT(VARCHAR , separator)
```

Arguments separator: specifies a separator of the VARCHAR type. Description Use a separator to split a string into multiple substrings. Examples Input example

| d (VARCHAR) | s (VARCHAR) |
|---|---|
| abc-bcd | - |
| hhh | - |

Sample code

```
SELECT d, v FROM T1, lateral table(STRING_SPLIT(d, s)) as T(v)
```

Output example

| d (VARCHAR) | v (VARCHAR) |
|---|---|
| abc-bcd | abc |
| abc-bcd | bcd |
| hhh | hhh |

#### 1.11.6 Type conversion functions

##### 1.11.6.1 CAST

Syntax

```
CAST(A AS type)
```

Argument A: For more information about the argument type, see Data types. Description Convert a value to a specified type. Examples Input example

| var1 (VARCHAR) | var2 (INT) |
|---|---|
| 1000 | 30 |

Sample code

```
SELECT CAST(var1 AS INT) as aa FROM T1;
```

Output example aa (INT)

#### 1.11.7 Aggregate functions

##### 1.11.7.1 AVG

Syntax

```
AVG(A)
```

Argument A: specifies a value of numeric types including TINYINT, SMALLINT, INT, BIGINT, FLOAT, DECIMAL, and DOUBLE. Return the average number. Examples Input example

| var1 (INT) | var2 (INT) |
|---|---|
| 4 | 30 |
| 6 | 30 |

Sample code

```
SELECT AVG(var1) as aa FROM T1;
```

Output example aa (INT)

##### 1.11.7.2 CONCAT_AGG

Syntax

```
CONCAT_AGG([linedelimiter, ] value)
```

Argument linedelimiter: specifies a connector, which currently can only be a string constant. Description Use a connector to concatenate multiple fields. The default connector is "\n". The return value is a new concatenated string of the VARCHAR type. Examples Input example c (VARCHAR) Hi Hi Hi c (VARCHAR) Hi Hi Hi Hi Hi Hi Hi Sample code

```
SELECT concat_agg(c) as var1,
       concat_agg('-', c) as var2
FROM MyTable GROUP BY c
```

Output example

| var1 (VARCHAR) | var2 (VARCHAR) |
|---|---|
| Hi\nHi\nHi\nHi\nHi\nHi\nHi\nHi\nHi\nHi | Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi |

##### 1.11.7.3 COUNT

Syntax

```
 COUNT(A)
```

Arguments A Supported data types include numeric types (TINYINT, SMALLINT, INT, BIGINT, FLOAT, DECIMAL, and DOUBLE), BOOLEAN, and VARCHAR. The DATE, TIME, TIMESTAMP, and VARBINARY data types are not supported. Description Return the number of input parameters. Examples var1 (VARCHAR) Sample code

```
SELECT COUNT(var1) as aa FROM T1;
```

Output example aa (BIGINT)

##### 1.11.7.4 FIRST_VALUE

Syntax

```
 T FIRST_VALUE(value: T)
```

To obtain the first record based on parameters, define the function as follows:

```
 T FIRST_VALUE(value: T, order: Long)
```

Arguments value: specifies a value of any type. Only one argument is supported. order: specifies a record with the smallest order value as the first record. Description Obtain the first non-null record of a stream. Examples Input example

| a (BIGINT) | b (INT) | c (VARCHAR) |
|---|---|---|
| 1L | 1 | "Hello" |
| 2L | 2 | "Hello" |

| R | ealtime Compute |   | Developer Guide·Flink SQ | L |
|---|---|---|---|---|

| a (BIGINT) | b (INT) | c (VARCHAR) |
|---|---|---|
| 3L | 3 | "Hello" |
| 4L | 4 | "Hello" |
| 5L | 5 | "Hello" |
| 6L | 6 | "Hello" |
| 7L | 7 | "Hello World" |
| 8L | 8 | "Hello World" |
| 20L | 20 | "Hello World" |

Sample code

```
SELECT
```

`c,`

```
first_value(b) OVER (PARTITION BY c ORDER BY proctime RANGE UNBOUNDED preceding) as var1 from T1
```

Output example

| c (VARCHAR) | var1 (INT) |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello World | 7 |
| Hello World | 7 |
| Hello World | 7 |

##### 1.11.7.5 LAST_VALUE

Syntax

```
 T LAST_VALUE(value: T)
```

To return the last value in an ordered set of values, define the function as follows:

```
T LAST_VALUE(value: T, order: Long)
```

Arguments value: specifies a value of any type. order: specifies the order of the values. A value with the greatest order value is considered as the last value. Description Obtain the last data record of a stream. Examples Input example

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1L | 1 | "Hello" |
| 2L | 2 | "Hello" |
| 3L | 3 | "Hello" |
| 4L | 4 | "Hello" |
| 5L | 5 | "Hello" |
| 6L | 6 | "Hello" |
| 7L | 7 | "Hello World" |
| 8L | 8 | "Hello World" |
| 20L | 20 | "Hello World" |

Sample code

```
SELECT
```

`c,`

```
last_value(b) OVER (PARTITION BY c ORDER BY proctime RANGE UNBOUNDED preceding) as var1 from T1
```

Output example

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 2 |

| R | ealtime Compute | Developer Guide·Flink SQ | L |
|---|---|---|---|

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 3 |
| Hello | 4 |
| Hello | 5 |
| Hello | 6 |
| Hello World | 7 |
| Hello World | 8 |
| Hello World | 20 |

##### 1.11.7.6 MAX

Syntax

```
 MAX(A)
```

Arguments A Supported data types include numeric values (TINYINT, SMALLINT, INT, BIGINT, FLOAT, DECIMAL, and DOUBLE), BOOLEAN, and VARCHAR. The DATE, TIME, TIMESTAMP, and VARBINARY data types are not supported. Description Return the maximum value of all the input values. Examples Input example var1(INT) Sample code

```
SELECT MAX(a) as aa FROM T1;
```

aa(INT)

##### 1.11.7.7 MIN

Syntax

```
 MIN(A)
```

Arguments A Supported data types include numeric values (TINYINT, SMALLINT, INT, BIGINT, FLOAT, DECIMAL, and DOUBLE), BOOLEAN, and VARCHAR. The DATE, TIME, TIMESTAMP, and VARBINARY data types are not supported. Description Return the minimum value of all the input values. Examples Input example var1(INT) Sample code

```
SELECT MIN(a) as aa FROM T1;
```

Output example aa(INT)

##### 1.11.7.8 STDDEV_POP

Syntax

```
T STDDEV_POP(T value)
```

Argument value: specifies a number of the BIGINT or DOUBLE type. Description Return the standard deviation for the population of all values in the specified expression. Examples Input example

| a (DOUBLE) | c (VARCHAR) |
|---|---|
| 0 | Hi |
| 1 | Hi |
| 2 | Hi |
| 3 | Hi |
| 4 | Hi |
| 5 | Hi |
| 6 | Hi |
| 7 | Hi |
| 8 | Hi |
| 9 | Hi |

Sample code

```
SELECT c, STDDEV_POP(a) as dou FROM MyTable GROUP BY c
```

Output example

| c (VARCHAR) | dou1 (DOUBLE) |
|---|---|
| Hi | 2.8722813232690143 |

##### 1.11.7.9 SUM

Syntax

```
SUM(A)
```

Arguments A: specifies a value of the numeric types including TINYINT, SMALLINT, INT, BIGINT, FLOAT, DECIMAL, and DOUBLE. Description Return the sum of all input values. Examples Input example var1 (INT) Sample code

```
SELECT sum(a) as aa FROM T1;
```

Output example aa (INT)

##### 1.11.7.10 VAR_POP

Syntax

```
T VAR_POP(T value)
```

Argument value: specifies a number of the BIGINT or DOUBLE type. Description Return the statistical variance for the population of all values in the specified expression. Examples Input example

| a (BIGINT) | c (VARCHAR) |
|---|---|
| 2900 | Hi |

| R | ealtime Compute | Developer Guide·Flink SQ | L |
|---|---|---|---|

| a (BIGINT) | c (VARCHAR) |
|---|---|
| 2500 | Hi |
| 2600 | Hi |
| 3100 | Hello |
| 11000 | Hello |

Sample code

```
SELECT
   VAR_POP(a) as `result`,
```

`c`

```
FROM MyTable GROUP BY c
```

Output example

| result (BIGINT) | c |
|---|---|
| 28889 | Hi |
| 15602500 | Hello |

#### 1.11.8 Other functions

##### 1.11.8.1 UUID

Syntax

```
VARCHAR UUID()
```

Arguments None Description Return a globally unique identifier. Examples Sample code

```
SELECT uuid() as `result` FROM T1
```

result(VARCHAR) a364e414-e68b-4e5c-9166-65b3a153e257

### 1.12 UDXs

#### 1.12.1 Overview

You can extend the following three types of user-defined functions (UDFs): A UDSF can be used in a SQL expression and returns only one value. A UDAF aggregates multiple scalar values into one value. A UDTF takes zero, one, or multiple scalar values as input parameters and returns any number of rows. Among UDFs, UDTFs are the only type that can return multiple fields. Download JAR files For Realtime Compute versions earlier than 2.0, download the following JAR files: flink-streaming-java_2.11 flink-table_2.11 Not e After the JAR files are downloaded, you must modify the dependency information in the `pom.xml` file as follows:

```xml
  <dependency>&nbsp;
        <groupId>com.alibaba.blink</groupId>
        <artifactId>flink-table_2.11</artifactId>
        <version>blink-1.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
         <groupId>org.apache.flink</groupId>
         <artifactId>flink-streaming-java_2.11</artifactId>
         <version>blink-1.4-SNAPSHOT</version>
         <scope>provided</scope>
    </dependency>
```

For Realtime Compute version 2.0 and later, download the following JAR files: flink-streaming-java_2.11 flink-table_2.11 flink-core-blink-2.2.4 Not e After the JAR files are downloaded, you must modify the `pom.xml` file as follows:

```xml
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-core</artifactId>
        <version>blink-2.2.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-table_2.11</artifactId>
        <version>blink-2.2.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
         <groupId>org.apache.flink</groupId>
         <artifactId>flink-streaming-java_2.11</artifactId>
         <version>blink-2.2.4-SNAPSHOT</version>
         <scope>provided</scope>
    </dependency>
```

Register and use a UDF
1. Log on to the Realtime Compute console. For more information, see Log on t o t he Realt ime
Comput e console in User Guide.
2. Click Development in the top navigation bar to go to the development page.
3. Click Resources in the left-side navigation pane.
4. On the Resources page, click  Creat e Resource in the upper right corner to go to the Upload
Resource dialog box.
5. Specify settings for a resource as follows.

| Field | Description |
|---|---|
| Location | Currently, you can only upload local resources. |
| Resource | Click Upload Resource to select a resource to be referenced. |
| Resource Name | Enter a name for the resource. |
| Resource Description | Enter the resource description. |
| Resource Type | Select a type for a resource: JAR, DICTIONARY, or PYTHON. |

6. On the Resources page, locate the new resource, and move the pointer over More in the Actions
column.
7. Select Ref erence from the drop-down list to load the resource at runtime.
8. In the code editor, enter a declaration for the user-defined function at the beginning. An example
is described as follows:

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

#### 1.12.2 User-defined scalar function (UDSF)

This topic describes how to create a UDSF for Realtime Compute. Definition A UDSF maps zero, one, or multiple scalar values to a new scalar value. Build the development environment For more information, see Download JAR files. Write code that implements business logic To define a scalar function, you must extend the ScalarFunction class by implementing one or more `eval()` methods. The `open()` and `close()` methods are optional. An example of Java code is provided as follows:

```java
package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.ScalarFunction; public class StringLengthUdf extends ScalarFunction {
    // The open() method is optional.
    // To write the open() method, you must import org.apache.flink.table.functions.Functio
nContext.
    @Override
    public void open(FunctionContext context) {
```

`}`

```
    public long eval(String a) {
        return a == null ? 0 : a.length();
```

`}`

```
    public long eval(String b, String c) {
        return eval(b) + eval(c);
```

`}`

```java
    // The close() method is optional.
    @Override
    public void close() {
```

`}` `}` Publish and use a UDSF For more information about how to publish and use a UDSF, see Publish in User Guide. Sample code of a UDSF

```
-- udf str.length() CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf'; create table sls_stream(
    a int,
    b int,
    c varchar
) with (
    type='sls',
    endPoint='yourEndpoint',
    accessKeyId='yourAccessId',
    accessKeySecret='yourAccessSecret',
    startTime = '2017-07-04 00:00:00',
    project='yourProjectName',
    logStore='yourLogStoreName',
    consumerGroup='consumerGroupTest1'
```

);

```
create table rds_output(
    id int,
    len bigint,
    content VARCHAR
) with (
    type='rds',
    url='yourDatabaseURL',
    tableName='yourDatabaseTableName',
    userName='yourDatabaseUserName',
    password='yourDatabasePassword'
```

);

```
insert into rds_output select
```

`a,`

```
    stringLengthUdf(c),
    c as content
from sls_stream
```

FAQ Q: Why does a UDSF that generates random numbers always returns the same value? A: If no parameters are defined for a UDSF and you do not declare the function as nondeterministic, the function may be optimized during compilation to return a constant value. To avoid this, you can override the `isDeterministic()` method to make it return `false` .

#### 1.12.3 User-defined aggregation function (UDAF)

(UDAF) This topic describes how to create a UDAF for Realtime Compute. Definition A UDAF aggregates multiple values into a single value. Methods of a UDAF The following code describes the core methods of a UDAF. Not e A UDAF can be implemented in Java or Scala. We recommend that you use Java because Scala data types may cause unnecessary overhead when calling functions. createAccumulator() and getValue() methods `/*`

```
* @param <T> The type of the aggregation result returned by a UDAF.
* @param <ACC> The type of a UDAF accumulator. An accumulator stores the intermediate com
puting results of a UDAF. You can design an accumulator for each UDAF as required.
```

`*/`

```
public abstract class AggregateFunction<T, ACC> extends UserDefinedFunction {
```

`/*`

```
* Initializes the accumulator of the AggregateFunction.
* Calls the following method once when aggregation is performed for the first time.
```

`*/`

```
public ACC createAccumulator();
```

`/*`

```
* Calls the following method after each aggregation is complete.
```

`*/`

```
public T getValue(ACC accumulator);
```

`}` Not e The createAccumulator() and getValue() methods can be defined in the AggregateFunction abstract class. A UDAF must contain at least one accumulate() method. accumulate() method

```
public void accumulate(ACC accumulator, ...[ User-specified parameters]...) ;
```

Not e You need to implement an accumulate() method to process input data and update the provided accumulator with the computing result. The first parameter of the accumulate() method must be an accumulator of the ACC type as defined in the AggregateFunction class. During processing, you can use the underlying runtime code to send the previous accumulator and the specified upstream data to the operator for calculation. No limits are set for the data types or the number of data records. retract() and merge() methods The createAccumulator(), getValue(), and accumulate() methods are mandatory for each UDAF. The retract() and merge() methods are also needed in certain Realtime Compute scenarios. In many Realtime Compute scenarios, computing is an early firing for an infinite stream. To refine the early fired results, you need to implement a retract() method. The SQL translation optimizer automatically determines the circumstances under which input data needs to be retracted. It also automatically determines the operations you need to process the data with the retraction labels. You must implement a retract() method to retract input data.

```
public void retract(ACC accumulator, ...[ User-specified parameters]...) ;
```

Not e The retract() method is a reverse operation of the accumulate() method. For example, in a count UDAF, the computing result increases by 1 when the accumulate() method is called to process a data record. The result decreases by 1 when the retract() method is called to process a data record. Similar to the accumulate() method, the first parameter of the retract() method must be an accumulator of the ACC type as defined in the aggregate function class. During data processing, the runtime code sends the previous value in the accumulator and the specified upstream data to the operator for calculation. No limits are set for the data types or the number of data records. The merge() method is required in certain Realtime compute scenarios. For example, when you use session windows to aggregate data, you need to implement the merge() method. Realtime Compute can handle out-of-order data. Newly arrived data may fill the gap between two separate sessions, which results in the merge of the two sessions. In this case, you need to implement the merge() method to integrate multiple accumulators into one accumulator.

```
public void merge(ACC accumulator, Iterable<ACC> its);
```

Not e The first parameter of the merge() method must be an accumulator of the ACC type as defined in the AggregateFunction class. After the merge() method is complete, the state of the AggregateFunction is stored in the first accumulator. The second parameter of the merge() method is an iterator of one or more ACC-type accumulators. Build the development environment For more information about how to build the development environment, see Download JAR files. Write code that implements business logic An example of Java code is provided as follows:

```java
import org.apache.flink.table.functions.AggregateFunction; public class CountUdaf extends AggregateFunction<Long, CountUdaf.CountAccum> {
    // Defines the data schema of the accumulator that stores the state of the count UDAF.
    public static class CountAccum {
        public long total;
```

`}`

```
    // Initializes the accumulator of the count UDAF.
    public CountAccum createAccumulator() {
        CountAccum acc = new CountAccum();
        acc.total = 0;
        return acc;
```

`}`

```
    // Calls the getValue() method to obtain the result of the count UDAF from the accumula
tor that stores the UDAF state.
    public Long getValue(CountAccum accumulator) {
        return accumulator.total;
```

`}`

```
    // Calls the accumulate() method to update the accumulator that stores the state of the
count UDAF based on input data.
    public void accumulate(CountAccum accumulator, Object iValue) {
        accumulator.total++;
```

`}`

```
    public void merge(CountAccum accumulator, Iterable<CountAccum> its) {
         for (CountAccum other : its) {
            accumulator.total += other.total;
```

`}` `}` `}` Not e For a subclass of AggregateFunction, the open() and close() methods are optional. For more information, see the examples of a UDF or UDTF. Publish and use a UDAF For more information about how to publish and use a UDAF, see Publish in User Guide. Sample code of a UDAF

```
-- Uses a UDAF to calculate the count. CREATE FUNCTION countUdaf AS 'com.hjc.test.blink.sql.udx.CountUdaf'; create table sls_stream( a int, b bigint, c varchar ) with ( type='sls', endPoint='yourEndpoint', accessKeyId='yourAccessId', accessKeySecret='yourAccessSecret', startTime = '2017-07-04 00:00:00', project='yourProjectName', logStore='stream-test2', consumerGroup='consumerGroupTest3'
```

);

```
create table rds_output( len1 bigint, len2 bigint ) with ( type='rds', url='yourDatabaseURL', tableName='yourDatabaseTableName', userName='yourDatabaseUserName', password='yourDatabasePassword'
```

);

```
insert into rds_output select count(a), countUdaf(a) from sls_stream
```

#### 1.12.4 User-defined table function (UDTF)

Description Similar to a user-defined scalar function (UDSF), a UDTF uses zero, one, or multiple scalar values as input parameters. The difference is that a UDTF can return a set of values, instead of a single value. The returned set of values can consist of multiple columns and multiple rows. Build a development environment For information about how to build a development environment, see Download JAR files. Write code that implements business logic To define a UDTF, you must implement the eval() method of the TableFunction class. The open() and close() methods are optional. An example of Java code is described as follows:

```java
package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.TableFunction; public class SplitUdtf extends TableFunction<String> {
    // The open() method is optional. To implement the open() method, you must import the o
rg.apache.flink.table.functions.FunctionContext class.
    @Override
    public void open(FunctionContext context) {
        // ...
```

`}`

```
    public void eval(String str) {
        String[] split = str.split("\\|");
        for (String s : split) {
            collect(s);
```

`}` `}`

```java
    // The close() method is optional.
    @Override
    public void close() {
        // ...
```

`}` `}` Return multiple rows A UDTF can return multiple rows. If you want a UDTF to return multiple rows, you can call the collect() method multiple times. Return multiple columns A UDTF can return multiple columns. If you want a UDTF to return multiple columns, you can declare the return value as a Tuple or Row object. The return value is declared as a Tuple object. In Realtime Compute, you can use Tuple1 to Tuple25 to define 1 to 25 columns. For example, you can use Tuple3 to enable the function to return three columns. The sample code is described as follows:

```java
import org.apache.flink.api.java.tuple.Tuple3; import org.apache.flink.table.functions.TableFunction; // If the return value is declared as a Tuple object, you must explicitly declare the dat a type of the object, such as STRING, LONG, and INTEGER in this example. public class ParseUdtf extends TableFunction<Tuple3<String, Long, Integer>> { public void eval(String str) { String[] split = str.split(","); // The following code is used for your reference only. In actual scenarios, you must add code that implements verification logic. String first = split[0]; long second = Long.parseLong(split[1]); int third = Integer.parseInt(split[2]); Tuple3<String, Long, Integer> tuple3 = Tuple3.of(first, second, third); collect(tuple3);
```

`}` `}` Not e If the return value is declared as a Tuple object, column values cannot be null and a maximum of 25 columns are allowed. The returned value is declared as a Row object. For example, you can enable this function to return three columns. The sample code is described as follows:

```java
import org.apache.flink.table.types.DataType; import org.apache.flink.table.types.DataTypes; import org.apache.flink.table.functions.TableFunction; import org.apache.flink.types.Row; public class ParseUdtf extends TableFunction<Row> { public void eval(String str) { String[] split = str.split(","); String first = split[0]; long second = Long.parseLong(split[1]); int third = Integer.parseInt(split[2]); Row row = new Row(3); row.setField(0, first); row.setField(1, second); row.setField(2, third); collect(row);
```

`}`

```java
@Override // If the return value is declared as a Row object, you must explicitly declare the data type of the object by overriding the getResultType() method. public DataType getResultType(Object[] arguments, Class[] argTypes) { return DataTypes.createRowType(DataTypes.STRING, DataTypes.LONG, DataTypes.INT);
```

`}` `}` Not e If the return value is declared as a Row object, column values can be null. If the return value is declared as a Row object, you must override the `getResultType()` method. SQL syntax A UDTF supports CROSS JOIN and LEFT JOIN operations. To perform JOIN operations, you must use the `lateral` and `table` keywords in SQL statements. You must also specify an alias for a UDTF. For example, you can specify an alias for the preceding `ParseUdtf` function:

```
CREATE FUNCTION parseUdtf AS 'com.alibaba.blink.sql.udtf.ParseUdtf';
```

CROSS JOIN: Each row in the left table is joined with a row of data that is generated by the UDTF. If the UDTF does not generate any data for a row, the row is not returned.

```
select S.id, S.content, T.a, T.b, T.c from input_stream as S, lateral table(parseUdtf(content)) as T(a, b, c);
```

LEFT JOIN: Each row in the left table is joined with a row of data that is generated by the UDTF. If the UDTF does not generate any data for a row, the UDTF fields in the row are filled with null. Not e When you perform LEFT JOIN operations for a UDTF, you must end the statement with an `on true` join condition.

```
select S.id, S.content, T.a, T.b, T.c from input_stream as S left join lateral table(parseUdtf(content)) as T(a, b, c) on true;
```

Publish and use a UDTF For information about how to publish and use a UDTF, see the "Publish an SQL file" section in Realtime Compute User Guide. Sample code

```
-- UDTF str.split("\\|"); create function splitUdtf as 'com.hjc.test.blink.sql.udx.SplitUdtf'; create table sls_stream( a INT, b BIGINT, c VARCHAR ) with ( type='sls', endPoint='<yourEndpoint>', accessKeyId='<yourAccessKeyId>', accessKeySecret='<yourAccessSecret>', startTime = '2017-07-04 00:00:00', project='<yourProjectName>', logStore='<yourLogStoreName>', consumerGroup='consumerGroupTest2'
```

);

```
-- Use the splitUdtf function to extract data from the c field. The table T with multiple r ows and one column is returned. The column is named s. create view v1 as select a,b,c,s from sls_stream, lateral table(splitUdtf(c)) as T(s); create table rds_output( id INT, len BIGINT, content VARCHAR ) with ( type='rds', url='yourDatabaseURL', tableName='<yourDatabaseTableName>', userName='<yourDatabaseUserName>', password='<yourDatabasePassword>'
```

);

```
insert into rds_output select a,b,s from v1
```

#### 1.12.5 Create a user-defined function (UDF) by using IntelliJ IDEA

using IntelliJ IDEA This topic takes a Java package named com.hjc.test.blink.sql.udx as an example to describe how to use IntelliJ IDEA to create a UDF for Realtime Compute. Not e This example uses IntelliJ IDEA on macOS. You need to download and install IntelliJ IDEA on your Mac before creating user-defined functions. Preparations
1. Download Maven.
i. Visit the Apache Maven website and download apache-maven-3.5.3-bin.tar.gz. ii. Decompress the downloaded package to a directory, for example, /Users/*****/Documents/m aven.
2. Configure environment variables.
Open Terminal on your Mac and perform the following operations: i. Run the vim ~/.bash_prof ile command to open the .bash_profile file. ii. Enter the following commands in the file: export M2_HOME=/Users/****/Document s/maven/apache-maven-3.5.3 and export PAT H=$PAT H:$M2_HOME/bin. iii. Run the :wq command to save the configurations and exit. Run the following command in Terminal to apply the configurations: source ~/.bash_prof ile.
3. Check whether the configurations take effect.
Run the mvn -v command in Terminal. If the command returns the following result, the configurations have taken effect.

```
Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00
```

`)`

```
Maven home: /Users/****/Documents/maven/apache-maven-3.5.0 Java version: 1.8.0_121, vendor: Oracle Corporation Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre Default locale: zh_CN, platform encoding: UTF-8 OS name: "mac os x", version: "10.12.6", arch: "x86_64", family: "mac"
```

4. Download the required JAR files to a local repository. For more information about the download
URL, see Download JAR files. Configure Maven in IntelliJ IDEA
1. Click Int elliJ IDEA in the top navigation bar.
2. Select Pref erences from the drop-down list.
3. Choose Maven > Maven home direct ory to configure the Maven home directory.
Not e You can find the Maven home directory `Maven home:/Users/****/Documents/maven` `/apache-maven-3.5.0` from the output of the mvn -v command. For more information, see Preparat ions. Create a Maven project
1. Click Create New Project on the home page of IntelliJ IDEA.
2. Select Maven.
3. Enter a project name in the ArtifactId field.
4. Click Finish.
Configure dependencies Open the pom.xml file, and enter the following code to declare dependencies in the code editor: For Realtime Compute versions earlier than 2.0

```xml
<dependency>
        <groupId>com.alibaba.blink</groupId>
        <artifactId>flink-table_2.11</artifactId>
        <version>blink-1.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
         <groupId>org.apache.flink</groupId>
         <artifactId>flink-streaming-java_2.11</artifactId>
         <version>blink-1.4-SNAPSHOT</version>
         <scope>provided</scope>
    </dependency>
```

For Realtime Compute version 2.0 and later

```xml
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-core</artifactId>
        <version>blink-2.2.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-table_2.11</artifactId>
        <version>blink-2.2.4-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
         <groupId>org.apache.flink</groupId>
         <artifactId>flink-streaming-java_2.11</artifactId>
         <version>blink-2.2.4-SNAPSHOT</version>
         <scope>provided</scope>
    </dependency>
```

Test a UDF
1. Create a new package.
2. Create a new Java class.
3. Copy and paste the UDF code you have written to the Java class, and run the code to start the
test. An example of UDF code is provided as follows:

```java
import org.apache.flink.table.functions.ScalarFunction; public class StringLengthUdf extends ScalarFunction { // The open() method is optional.
 // To write the open() method, you must import org.apache.flink.table.functions.Fun
ctionContext;'. @Override public void open(FunctionContext context) { // ...
```

`}`

```
public long eval(String a) { return a == null ? 0 : a.length();
```

`}`

```
public long eval(String b, String c) { return eval(b) + eval(c);
```

`}`

```java
// The close() method is optional. @Override Public void close (){ // ...
```

`}` `}`
4. Package the project into a JAR file.
Not e If your Maven project has other dependencies in addition to the Realtime Compute SDK, you need to package all JAR files in your project. Then, you can export the project as a JAR file. i. Enter the following code in the pom.xml file:

```xml
<build>
    <plugins>
        <plugin>
            <artifactId>maven-assembly-plugin</artifactId>
            <configuration>
              <descriptorRefs>
                <descriptorRef>jar-with-dependencies</descriptorRef>
              </descriptorRefs>
            </configuration>
        </plugin>
    </plugins>
</build>
```

ii. In the T erminal section at the bottom of the page, enter mvn assembly:assembly. The JAR file path is generated, as shown in the following figure.
5. You can reference the JAR file in a Realtime Compute job. For more information, see Register and
use a UDF.
