---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Tablestore Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 179
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Tablestore Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Tablestore%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Tablestore Developer Guide 20220928

## Table of Contents

- 1 API reference
  - 1.1 API
    - 1.1.1 API-based operations
      - 1.1.1.1 GetRow
      - 1.1.1.2 PutRow
      - 1.1.1.3 UpdateRow
      - 1.1.1.4 DeleteRow
      - 1.1.1.5 GetRange
      - 1.1.1.6 BatchGetRow
      - 1.1.1.7 BatchWriteRow
      - 1.1.1.8 CreateTable
      - 1.1.1.9 ListTable
      - 1.1.1.10 DeleteTable
      - 1.1.1.11 UpdateTable
      - 1.1.1.12 DescribeTable
      - 1.1.1.13 ComputeSplitPointsBySize
      - 1.1.1.14 ListStream
      - 1.1.1.15 DescribeStream
      - 1.1.1.16 GetShardIterator
      - 1.1.1.17 GetStreamRecord
      - 1.1.1.18 Tablestore ProtocolBuffer message definitions
      - 1.1.1.19 CreateIndex
      - 1.1.1.20 DeleteIndex
    - 1.1.2 DataType
      - 1.1.2.1 ActionType
      - 1.1.2.2 CapacityUnit
      - 1.1.2.3 ColumnPaginationFilter
      - 1.1.2.4 ComparatorType
      - 1.1.2.5 CompositeColumnValueFilter
      - 1.1.2.6 Condition
      - 1.1.2.7 ConsumedCapacity
      - 1.1.2.8 Direction
      - 1.1.2.9 Error
      - 1.1.2.10 Filter
      - 1.1.2.11 PrimaryKeyOption
      - 1.1.2.12 FilterType
      - 1.1.2.13 LogicalOperator
      - 1.1.2.14 OperationType
      - 1.1.2.15 PartitionRange
      - 1.1.2.16 PlainBuffer
      - 1.1.2.17 PrimaryKeySchema
      - 1.1.2.18 PrimaryKeyType
      - 1.1.2.19 ReservedThroughput
      - 1.1.2.20 ReservedThroughputDetails
      - 1.1.2.21 ReturnContent
      - 1.1.2.22 ReturnType
      - 1.1.2.23 RowExistenceExpectation
      - 1.1.2.24 RowInBatchGetRowResponse
      - 1.1.2.25 RowInBatchWriteRowRequest
      - 1.1.2.26 RowInBatchWriteRowResponse
      - 1.1.2.27 SingleColumnValueFilter
      - 1.1.2.28 StreamDetails
      - 1.1.2.29 StreamRecord
      - 1.1.2.30 StreamSpecification
      - 1.1.2.31 TableInBatchGetRowRequest
      - 1.1.2.32 TableInBatchGetRowResponse
      - 1.1.2.33 TableInBatchWriteRowRequest
      - 1.1.2.34 TableInBatchWriteRowResponse
      - 1.1.2.35 TableMeta
      - 1.1.2.36 TableOptions
      - 1.1.2.37 TimeRange
- 2 SDK reference
  - 2.1 SDK
    - 2.1.1 Java SDK
      - 2.1.1.1 Preface
      - 2.1.1.2 Installation
      - 2.1.1.3 Initialization
      - 2.1.1.4 Use Tablestore SDK for Java
        - 2.1.1.4.1 Table-level operations
        - 2.1.1.4.2 Single-row operations
        - 2.1.1.4.3 Multi-row operations
        - 2.1.1.4.4 Auto-increment function of the primary key column
        - 2.1.1.4.5 Conditional update
        - 2.1.1.4.6 Filters
        - 2.1.1.4.7 Global secondary indexes
      - 2.1.1.5 Error handling
    - 2.1.2 Python SDK
      - 2.1.2.1 Preface
      - 2.1.2.2 Installation
      - 2.1.2.3 Initialization
      - 2.1.2.4 Use the SDK
        - 2.1.2.4.1 Table-level operations
        - 2.1.2.4.2 Single-row operations
        - 2.1.2.4.3 Multi-row operations
        - 2.1.2.4.4 Global secondary indexes
      - 2.1.2.5 Error handling
    - 2.1.3 Go SDK
      - 2.1.3.1 Preface
      - 2.1.3.2 Installation
      - 2.1.3.3 Initialization
      - 2.1.3.4 Use the SDK
        - 2.1.3.4.1 Table-level operations
        - 2.1.3.4.2 Single-row operations
        - 2.1.3.4.3 Multi-row operations
    - 2.1.4 NodeJS SDK
      - 2.1.4.1 Preface
      - 2.1.4.2 Installation
      - 2.1.4.3 Initialization
      - 2.1.4.4 Data types
      - 2.1.4.5 Use the SDK
        - 2.1.4.5.1 Table-level operations
        - 2.1.4.5.2 Single-row operations
        - 2.1.4.5.3 Multi-row operations
      - 2.1.4.6 Error handling
    - 2.1.5. .NET SDK
      - 2.1.5.1 Preface
      - 2.1.5.2 Installation
      - 2.1.5.3 Initialization
      - 2.1.5.4 Use the SDK
        - 2.1.5.4.1 Table-level operations
        - 2.1.5.4.2 Single-row operations
        - 2.1.5.4.3 Multiple-row operations
      - 2.1.5.5 Error handling
    - 2.1.6 Obtain an AccessKey pair

## 1 API reference

### 1.1 API

#### 1.1.1 API-based operations

##### 1.1.1.1 GetRow

Action You can use the GetRow API to read data in a single row based on a specified primary key. Request structure

```
message GetRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2;   // The PlainBuffer encoding is binary.
    repeated string columns_to_get = 3; // If this parameter is not specified, all columns
are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional bytes filter = 7;
    optional string start_column = 8;
    optional string end_column = 9;
    optional bytes token = 10;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table containing the data to be read. primary_key: Type: bytes Required: yes This parameter specifies all primary key columns in the row, including the primary key names and values. The primary key columns are encoded in the PlainBuffer format. columns_t o_get : Type: repeated string Required: no This parameter specifies the names of all columns to be returned. If the parameter is not configured, all columns of this row are returned. If the specified column does not exist, data in this column is not returned. If a duplicate column name exists, the response only includes this column once. In columns_to_get, the maximum number of strings is 128. t ime_range: Type: TimeRange Required: At least one of the time_range and max_versions parameters must be specified. This parameter specifies the range of timestamps to read versions of data. The minimum timestamp value is 0. The maximum timestamp value is INT64.MAX. To query data within a time range, specify start_time and end_time. To query data within a specific timestamp, specify specific_time. Example: If the value of time_range is (100, 200), the timestamp of the returned column data must be within the range of [100, 200). max_versions: Type: int32 Required: At least one of the max_versions and time_range parameters must be specified. This parameter specifies the maximum number of versions of data to be returned. Example: If the value of max_versions is 2, data of a maximum of two versions is returned for each column. f ilt er: Type: bytes Required: no This parameter specifies the expression of the filtering condition. It indicates the binary data after the filter is serialized in the Protobuf format. st art _column: Type: string Required: no This parameter specifies the column to start to read from and is used to read wide rows. The response contains the specified starting column. The column names are sorted lexicographically. Example: If a table contains columns A, B, and C, and the value of start_column is B, the data is read starting from column B. Columns B and C are returned. end_column: Type: string Required: no This parameter specifies the column to stop reading data and is used to read wide rows. The response does not contain the specified ending column. The column names are sorted lexicographically. Example: If a table contains columns A, B, and C, and the value of end_column is B, the reading stops at column B. Only column A is returned. Response structure

```
message GetRowResponse {
    required ConsumedCapacity consumed = 1;
    required bytes row = 2; // The PlainBuffer encoding is binary.
```

consumed: Type: CapacityUnit This parameter specifies the number of CUs consumed by this operation. row: Type: bytes The read data is encoded in the PlainBuffer format. If this row does not exist, null is returned. CU consumption: If the requested row does not exist, one read CU is consumed. If the requested row exists, the number of consumed read CUs is calculated based on the following formula: Number of consumed read CUs = [(Size of all primary key columns in the row + Size of actually read attribute columns)/4 KB] rounded up. If the request times out and the results are undefined, a CU may or may not be consumed. If an internal error code is returned (HTTP status code: 5XX), this operation does not consume CUs. If other errors are returned, one read CU is consumed.

##### 1.1.1.2 PutRow

Action You can use the PutRow API to insert data into the specified row. If the row does not exist, a new row is added. If the row exists, the original row is overwritten. Request structure

```
message PutRowRequest {
    required string table_name = 1;
    required bytes row = 2; // The PlainBuffer encoding is binary.
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table to write data to. row: Type: bytes Required: yes This parameter specifies the data to be written into the row. It is in the PlainBuffer format and contains the primary key and attribute columns. condit ion: Type: Condition Required: yes This parameter determines whether to perform the row existence check before writing data. It can be one of three values: IGNORE indicates that the row existence check is not performed. EXPECT_EXIST indicates that the row is expected to exist. EXPECT_NOT_EXIST indicates that the row is not expected to exist. If the row is not expected to exist but it does, the row cannot be inserted and an error is returned. If the row is expected to exist but it does not, the row also fails to be inserted and an error is returned. ret urn_cont ent : Type: ReturnContent Required: no This parameter specifies the data type after the row is written. Only the primary key is returned. It is used for the auto-increment function of the primary key column. Response structure

```
message PutRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

consumed: Type: ConsumedCapacity This parameter specifies the number of CUs consumed by this operation. CU consumpt ion: If this row does not exist: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of primary key columns in the row + Size of attribute columns to be inserted)/4 KB] rounded up. If the value of the condition parameter is EXPECT_NOT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of primary key columns in the row + Size of attribute columns to be inserted)/4 KB] rounded up. The number of consumed read CUs is calculated based on the following formula: Number of consumed read CUs = (Size of primary key columns in the row/4 KB) rounded up. If the value of the condition parameter is EXPECT_EXIST, the row fails to be inserted. One write CU and one read CU are consumed. If this row exists: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of all primary key columns in the row + Size of attribute columns to be inserted)/4 KB] rounded up. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of all primary key columns in the row + Size of attribute columns to be inserted)/4 KB] rounded up. The number of consumed read CUs is calculated based on the following formula: Number of consumed read CUs = (Size of all primary key columns in the row/4 KB) rounded up. If the value of the condition parameter is EXPECT_NOT_EXIST, the row fails to be inserted. One write CU and one read CU are consumed. Conditional Update: If the operation succeeds, the number of consumed CUs are calculated based on the preceding formulas. If the operation fails, one write CU and one read CU are consumed. If an internal error code is returned (HTTP status code: 5XX), this operation does not consume CUs. If other errors are returned, one write CU is consumed. If the request times out and the results are undefined, a CU may or may not be consumed. row: Type: bytes This parameter specifies the returned data when return_content is set. If return_content is not set or no value is returned, NULL is returned. It is in the PlainBuffer format.

##### 1.1.1.3 UpdateRow

Description You can call this operation to update the data of a specified row. If the specified row does not exist, a new row is added. If the specified row exists, the values in the specified columns are added, modified, or deleted based on the request. Request structure

```
message UpdateRowRequest {
 required string table_name = 1;
 required bytes row_change = 2;
 required Condition condition = 3;
 optional ReturnContent return_content = 4;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table whose data is to be updated. row_change: Type: bytes Required: yes This parameter specifies the data that you use to update the row, including primary key columns and attribute columns. The data is in the PlainBuffer format. This parameter specifies all the attribute columns whose data you want to update for this row. Tablestore adds, modifies, or deletes the values in the specified attribute columns based on each specified update type in row_change. Columns that exist in this row but are not specified by row_change are not affected. Valid values of UpdateType: PUT: The value you use to update the specified column must be a valid attribute column value. This update type indicates that if the specified column does not exist, a new column is added. If the specified column exists, the existing column is overwritten. DELETE: The value you use to update the specified column must be empty, and a timestamp must be specified. This update type indicates that data of the specified version is deleted from the column. DELETE_ALL: The value you use to update the specified column and the timestamp must be empty. This update type indicates that all versions of data in the column are deleted. Not e A row exists even if all attribute columns in the row are deleted. To delete a row, use the DeleteRow operation. condit ion: Type: Condition Required: yes This parameter determines whether to perform existence check before data is updated. You can set this parameter to one of the following values: IGNORE: the row existence check is not performed. EXPECT_EXIST: the row is expected to exist. If a row that is expected to exist does not exist, the row cannot be updated and an error is returned. If the existence of the row is ignored, the operation result is not affected by the row existence. ret urn_cont ent : Type: ReturnContent Required: no This parameter specifies the type of the data to return after the row is updated. Only the primary key is returned. It is used for the auto-increment function of the primary key column. Response structure

```
message UpdateRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

consumed: Type: ConsumedCapacity This parameter specifies the number of capacity units (CUs) consumed by this operation. CU consumpt ion: If the row does not exist: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of primary key columns in the row + Size of attribute columns to be updated)/4 KB] rounded up. If UpdateRow specifies an attribute column to delete, the length of the column name is calculated as the column size. If the value of the condition parameter is EXPECT_EXIST, the row fails to be inserted. One write CU and one read CU are consumed. If the row exists: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = [(Size of primary key columns in the row + Size of attribute columns to be updated)/4 KB] rounded up. If UpdateRow specifies an attribute column to delete, the length of the column name is calculated as the column size. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is calculated by using the same method that is used when the value of the condition parameter is IGNORE. The number of consumed read CUs is calculated based on the following formula: Number of consumed read CUs = (Size of primary key columns in the row/4 KB) rounded up. If the request times out and the results are undefined, CUs may or may not be consumed. If an internal error is returned and the 5xx HTTP status code is displayed, this operation does not consume CUs. If other errors are returned, one write CU and one read CU are consumed. row: Type: bytes This parameter indicates the returned data when return_content is set. If return_content is not set or no value is returned, NULL is returned. The returned data is in the PlainBuffer format.

##### 1.1.1.4 DeleteRow

Action You can use the DeleteRow API to delete a row of data. Request structure

```
message DeleteRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2; // The PlainBuffer encoding is binary.
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table whose data is to be updated. primary_key: Type: bytes Required: yes This parameter specifies the primary key of the row to be deleted, which is in the PlainBuffer format. condit ion: Type: Condition Required: yes This parameter determines whether to perform existence check before data updates. It can be one of two values: IGNORE indicates that the row existence check is not performed. EXPECT_EXIST indicates that the row is expected to exist. If this row is expected to exist but does not, the delete operation fails and an error is returned. If the existence of the row is ignored, this operation succeeds regardless of the row existence. ret urn_cont ent : Type: ReturnContent Required: no This parameter specifies the data type after the row is written. Only the primary key is returned. It is used for the auto-increment function of the primary key column. Response structure

```
message DeleteRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

consumed: Type: ConsumedCapacity This parameter specifies the number of capacity units (CUs) consumed by this operation. CU consumpt ion: If this row does not exist: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = (Size of primary key columns in the row/4 KB) rounded up. If the value of the condition parameter is EXPECT_EXIST, the row fails to be deleted, and one write CU and one read CU are consumed. If this row exists: If the value of the condition parameter is IGNORE, the number of consumed write CUs is calculated based on the following formula: Number of consumed write CUs = (Size of primary key columns in the row/4 KB) rounded up. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs and the number of consumed read CUs are calculated based on the following formula: Number of consumed read/write CUs = (Size of primary key columns in the row/4 KB) rounded up. If an internal error code is returned (HTTP status code: 5XX), this operation does not consume CUs. If other errors are returned, one write CU is consumed. If the request times out and the results are undefined, a CU may or may not be consumed. row: Type: bytes This parameter specifies the returned data when return_content is set. If return_content is not set or no value is returned, NULL is returned. The returned data is in the PlainBuffer format.

##### 1.1.1.5 GetRange

Description You can call this operation to read data within the specified primary key range. Request structure

```
message GetRangeRequest {
    required string table_name = 1;
    required Direction direction = 2;
    repeated string columns_to_get = 3;  // If this parameter is not specified, all columns
are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional int32 limit = 6;
    required bytes inclusive_start_primary_key = 7; // Encode the parameter value in the Pl
ainBuffer format to obtain binary data.
    required bytes exclusive_end_primary_key = 8; // Encode the parameter value in the Plai
nBuffer format to obtain binary data.
    optional bytes filter = 10;
    optional string start_column = 11;
    optional string end_column = 12;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table that contains the data to read. direct ion: Type: Direction Required: yes This parameter specifies the query direction. If the query direction is forward, the value of inclusive_start_primary must be smaller than that of exclusive_end_primary, and the rows in the response are sorted in ascending order of primary key values. If the query direction is backward, the value of inclusive_start_primary must be greater than that of exclusive_end_primary, and the rows in the response are sorted in descending order of primary key values. columns_t o_get : Type: repeated string Required: no This parameter specifies the names of all columns to return. If the parameter is not configured, all columns of each row in the read results are returned. If a duplicate column name exists, the response only includes this column once. The maximum number of strings that can be specified in columns_to_get is 128. t ime_range: Type: TimeRange Required: At least one of the time_range and max_versions parameters must be specified. This parameter specifies the range of timestamps to read versions of data. The timestamp in the value of time_range ranges from 0 to INT64.MAX. To query data of a time range, specify start_time and end_time. To query data of a specific timestamp, specify specific_time. Example: If the value of time_range is (100, 200), the timestamp of the returned column data must be within the range of [100, 200). max_versions: Type: int32 Required: At least one of the time_range and max_versions parameters must be specified. This parameter specifies the maximum number of versions of data to return. Example: If the value of max_versions is 2, a maximum of two versions of data is returned for each column. limit : Type: int32 Required: no This parameter specifies the maximum number of rows to read and return in a single operation. If the number of rows queried exceeds this value, the response includes a breakpoint to record the position where read ends in this operation. The next read continues from the recorded position. This value must be greater than 0. Tablestore returns a maximum of 5,000 rows of data if this parameter is not set. The total data size does not exceed 4 MB. inclusive_st art _primary_key: Type: bytes Required: yes This parameter specifies a start primary key. The read starts from the row that contains the start primary key. If the row exists, the response contains this row. The start primary key is encoded in the PlainBuffer format. exclusive_end_primary_key: Type: bytes Required: yes This parameter specifies an end primary key. The read stops at the row that contains the end primary key. The response does not contain the row regardless of the row existence. The end primary key is encoded in the PlainBuffer format. For GetRange, the type of Column in inclusive_start_primary_key or exclusive_end_primary_key can be set to INF_MIN or INF_MAX. If the type of column is set to INF_MIN, the value of the column is always smaller than that of other columns. If the type of column is set to INF_MAX, the value of the column is always greater than that of other columns. Columns. f ilt er: Type: bytes Required: no This parameter specifies the expression of the filter condition. It indicates the binary data after the filter is serialized in the Protobuf format. st art _column: Type: string Required: no This parameter specifies the column from which the read of each row starts. This parameter is used to read wide rows. The response contains the specified start column. The columns are sorted based on their names in alphabetical order. Example: If a table contains columns a, b, and c, and the value of start_column is b, the read of data starts from column b. Columns b and c are returned. end_column: Type: string Required: no This parameter specifies the column where the read of each row ends. This parameter is used to read wide rows. The response does not contain the specified end column. The columns are sorted based on their names in alphabetical order. Example: If a table contains columns a, b, and c, and the value of end_column is b, the read of data stops at column b. Only column a is returned. Response structure

```
message GetRangeResponse {
    required ConsumedCapacity consumed = 1;
    required bytes rows = 2;
    optional bytes next_start_primary_key = 3;
```

consumed: Type: ConsumedCapacity This parameter specifies the number of capacity units (CUs) consumed by this operation. rows: Type: bytes It is encoded in the PlainBuffer format. This parameter indicates all the read data. If the direction specified in the request is forward, all rows are sorted in ascending order of primary key values. If the direction specified in the request is backward, all rows are sorted in descending order of primary key values. primary_key_columns and attribute_columns for each row only contain the columns specified by columns_to_get. Their orders may not be consistent with the order of columns_to_get in the request. The order of primary_key_columns may not be consistent with the order specified when the table is created. If the specified columns_to_get in the request does not contain any primary key column, rows that do not contain any attribute column specified in columns_to_get are not included in the response although the primary key column of the rows is within the query range. next _st art _primary_key: Type: bytes This parameter specifies the breakpoint information for this GetRange operation. It is encoded in the PlainBuffer format. If this parameter is not specified, the response to this GetRange operation contains all data within the request range. If this parameter is specified, the response to this GetRange operation includes only the data within the [inclusive_start_primary_key, next_start_primary_key) range. If you want to obtain the remaining data, you must use next_start_primary_key as inclusive_start_primary_key, and retain exclusive_end_primary_key in the original request to continue the GetRange operation. Not e Tablestore limits the number of rows in the response to a GetRange operation to 5,000 rows, whose size cannot exceed 4 MB. Furthermore, the volume of returned data cannot exceed the remaining reserved read throughput. Even if no limit is set in the GetRange request, next_start_primary_key may still appear in the response. Therefore, when you use GetRange, you must check whether the response contains next_start_primary_key and proceed accordingly. CU consumpt ion: The number of read CUs consumed by the GetRange operation is calculated based on the following formula: Number of read CUs consumed by the GetRange operation = [(Size of primary key columns of the row within the query range + Size of actually read attribute columns)/4 KB] rounded up. If the request times out and the results are undefined, CUs may or may not be consumed. If an internal error is returned (HTTP status code: 5xx), this operation does not consume CUs. If other errors are returned, one read CU is consumed.

##### 1.1.1.6 BatchGetRow

Action You can use the BatchGetRow API to simultaneously read data in several rows from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the request response time and increase the data read rate. Request structure

```
message BatchGetRowRequest {
    repeated TableInBatchGetRowRequest tables = 1;
```

t ables: Type: repeated TableInBatchGetRowRequest Required: yes This parameter specifies the information of rows to be read. The entire operation fails and returns an error if any of the following conditions appears in tables: Any table listed in the tables parameter does not exist. The name of any table does not comply with the table naming conventions. The primary key is not specified for any row in a table, the primary key column name does not comply with the conventions, or the primary key column type is incorrect. A column name in columns_to_get of any table does not comply with the column naming conventions. Tables with the same name exist. Any table in the tables contains rows with identical primary keys. The total number of RowInBatchGetRowRequest in all tables exceeds 100. Any table in the tables does not contain any RowInBatchGetRowRequest. The value of columns_to_get of any table exceeds 128. Response structure

```
message BatchGetRowResponse {
    repeated TableInBatchGetRowResponse tables = 1;
```

t ables: Type: repeated TableInBatchGetRowResponse The value of this parameter corresponds to the data to be read in each table. The TableInBatchGetRowResponse object order in the response is the same as the TableInBatchGetRowRequest object order in BatchGetRowRequest. The object order of each RowInBatchGetRowResponse under TableInBatchGetRowResponse is the same as that of RowInBatchGetRowRequest under TableInBatchGetRowRequest. If a row does not exist or contains no data in the specified columns_to_get, a corresponding RowInBatchGetRowResponse still appears in TableInBatchGetRowResponse. However, the primary_key_columns and attribute_columns of the row are null. If a row fails to be read, the is_ok value in RowInBatchGetRowResponse for the row is false and the row is null. Not e The BatchGetRow operation may partially fail at the row level. However, it still returns an HTTP status code of 200. The application must check for errors in RowInBatchGetRowResponse to confirm the execution results for each row and then proceed accordingly. CU consumpt ion: If the entire operation fails, it does not consume any CU. If the request times out and the results are undefined, a CU may or may not be consumed. In other situations, each RowInBatchGetRowRequest operation is considered as one GetRow operation when write CUs are calculated.

##### 1.1.1.7 BatchWriteRow

Action You can use the BatchWriteRow API to simultaneously insert, modify, or delete data in several rows in one or more tables. It is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of write operations, the use of BatchWriteRow can reduce the request response time and increase the data write rate. Request structure

```
message BatchWriteRowRequest {
    repeated TableInBatchWriteRowRequest tables = 1;
```

t ables: Type: repeated TableInBatchWriteRowRequest Required: yes This parameter specifies the information of rows that require write operations. An error is returned if any of the following conditions occurs: Any table listed in the tables parameter does not exist. Tables with the same name exist. The name of any table does not comply with the table naming conventions. The primary key is not specified for any row in a table, the primary key column name does not comply with the conventions, or the primary key column type is incorrect. For any attribute column in a table, the column name does not comply with the column naming conventions. Any row in a table contains an attribute column with the same name as the primary key column. The value of any primary key or attribute column in a table exceeds the upper limit. Any table in the tables contains rows with identical primary keys. The total number of rows for all tables listed in the tables parameter exceeds 200 or the total size of the data exceeds 4 MB. If any table contains no rows, the OTSParameterInvalidException error is returned. The number of columns included in any PutRowInBatchWriteRowRequest of a table exceeds 1,024. The number of ColumnUpdate objects included in any UpdateRowInBatchWriteRowRequest in a table exceeds 1,024. Response structure

```
message BatchWriteRowResponse {
    repeated TableInBatchWriteRowResponse tables = 1;
```

t ables: Type: TableInBatchWriteRowResponse This parameter specifies the response information corresponding to the operations for each table. The response information contains the execution results, error codes, and number of CUs consumed. The TableInBatchWriteRowResponse object order in the response is the same as the TableInBatchWriteRowRequest object order in BatchWriteRowRequest. The RowInBatchWriteRowResponse object orders contained in put_rows, update_rows, and delete_rows in each TableInBatchWriteRowRequest are the same as the respective PutRowInBatchWriteRowRequest, UpdateRowInBatchWriteRowRequest, and DeleteRowInBatchWriteRowRequestobject orders contained in put_rows, update_rows, and delete_rows in TableInBatchWriteRowRequest. If a row fails to be read, the is_ok value of the row in RowInBatchWriteRowResponse is false. Not e The BatchWriteRow operation may partially fail at the row level. However, it still returns an HTTP status code of 200. The application must check for errors in RowInBatchWriteRowResponse to confirm the execution results for each row and then proceed accordingly. CU consumpt ion: If the entire operation fails, it does not consume any CUs. If the request times out and the results are undefined, a CU may or may not be consumed. In other situations, each PutRowInBatchWriteRowRequest, UpdateRowInBatchWriteRowRequestDelete, or RowInBatchWriteRowRequest operation is considered as one write operation when write CUs are calculated.

##### 1.1.1.8 CreateTable

Action You can use the CreateTable API to create a table based on the specified table structure information. Request structure

```
message CreateTableRequest {
    required TableMeta table_meta = 1;
    required ReservedThroughput reserved_throughput = 2;
    optional TableOptions table_options = 3;
    optional StreamSpecification stream_spec = 5;
```

t able_met a: Type: TableMeta Required: yes This parameter specifies the structural information of the table you want to create. The value of table_name must be unique among the current instance. The value of ColumnSchemas in primary_key must be between 1 and 4. The value of the name parameter in ColumnSchema of primary_key must comply with the naming conventions. The value of the type parameter can only be STRING, INTEGER, or BINARY. After a table is created, its schema cannot be modified. reserved_t hroughput : Type: ReservedThroughput Required: yes This parameter specifies the initial reserved read/write throughput for the table to be created. The maximum reserved throughput is 5,000 for each table. The reserved read/write throughput settings for a table can be modified by using the UpdateTable operation. t able_opt ions: Type: TableOptions Required: yes This parameter specifies TimeToLive and MaxVersions. Response structure

```
message CreateTableResponse {
```

Note No read/write operation can be performed on a table immediately after it is created. Typically, you can perform read/write operations on a new table one minute after it is created. A single instance can contain up to 64 tables. If you need to raise the upper limit of the table quantity for a single instance, contact Alibaba Cloud customer service.

##### 1.1.1.9 ListTable

Action You can use the ListTable API to obtain the names of all tables created in the current instance. Request structure

```
message ListTableRequest {
```

Response structure

```
message ListTableResponse {
    repeated string table_names = 1;
```

t able_names: Type: repeated string This parameter specifies the names of all tables in the current instance. Note If a table is created, its table name can be returned by ListTableResponse, but this does not necessarily mean that this table can be read or written at the time.

##### 1.1.1.10 DeleteTable

Action You can use the DeleteTable API to delete the specified table in an instance. Request structure

```
message DeleteTableRequest {
    required string table_name = 1;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table you want to delete. Response structure

```
message DeleteTableResponse {
```

If the response of DeleteTable does not contain an error, the table has been deleted.

##### 1.1.1.11 UpdateTable

Action You can use the UpdateTable API to update the reserved read or write throughput settings of the specified table. New settings take effect within one minute of a successful update. Request structure

```
message UpdateTableRequest {
    required string table_name = 1;
    optional ReservedThroughput reserved_throughput = 2;
    optional TableOptions table_options = 3;
    optional StreamSpecification stream_spec = 4;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table for which you want to modify the reserved read/write throughput settings. reserved_t hroughput : Type: ReservedThroughput Required: yes This parameter specifies the reserved read/write throughput settings you want to modify for the table. New settings take effect within one minute of a successful update. You may modify the reserved read/write throughput settings of the table as required. You must specify a non-null value for either the read or write parameter of capacity_unit. Otherwise, the request fails and an error is returned. t able_opt ions: Type: TableOptions Required: yes This parameter specifies TimeToLive and MaxVersions. Response structure

```
message UpdateTableResponse {
    required ReservedThroughputDetails reserved_throughput_details = 1;
    required TableOptions table_options = 2;
```

reserved_t hroughput _det ails: Type: ReservedThroughputDetails After the update, the reserved read/write throughput settings information of the table contains the current reserved throughput settings, the time these settings were last updated, and the number of times they have been lowered on the current date. t able_opt ions: Type: TableOptions The latest value of the table_options parameter after the modification. Note The minimum interval between updates to the reserved read/write throughput of a table is two minutes. If the current UpdateTable operation is requested within two minutes of the previous operation, it will be rejected. The reserved read/write throughput of a table can be raised or lowered an unlimited number of times within a single day (from 00:00:00 to 00:00:00 the next day in UTC time).

##### 1.1.1.12 DescribeTable

Action You can use the DescribeTable API to query the structure information and reserved read/write throughput value of the specified table. Request structure

```
message DescribeTableRequest {
 required string table_name = 1;
```

t able_name: Type: string Required: yes This parameter specifies the name of the table you want to query. Response structure

```
message DescribeTableResponse {
    required TableMeta table_meta = 1;
    required ReservedThroughputDetails reserved_throughput_details = 2;
    required TableOptions table_options = 3;
    optional StreamDetails stream_details = 5;
    repeated bytes shard_splits = 6;
```

t able_met a: Type: TableMeta This parameter specifies the schema of the table. The schema is the same as the schema provided when the table is created. reserved_t hroughput _det ails: Type: ReservedThroughputDetails This parameter specifies the reserved read/write throughput settings information of the table. The information contains the current reserved read/write throughput settings, the time these settings were last updated, and the number of times they have been lowered on the current date. t able_opt ions: Type: TableOptions This parameter specifies the latest value of the table_options parameter. St reamSpecif icat ion: Type: StreamSpecification Required: no This parameter specifies whether to enable Stream-related attributes. shard_split s: Type: bytes This parameter specifies the split points of all partitions in the current table.

##### 1.1.1.13 ComputeSplitPointsBySize

Action You can use the ComputeSplitPointsBySize API to logically split data in a table into several partitions whose sizes are close to the specified size. The API can return the split points between the partitions and prompt about hosts where the partitions reside. This API is typically used to implement plans on compute engines, such as concurrency plans. Request structure

```
message ComputeSplitPointsBySizeRequest {
    required string table_name = 1;
    required int64 split_size = 2; // in 100MB
```

t able_name: Type: string Required: yes This parameter specifies the name of the table that contains the data you want to split. split _size: Type: int64 Required: yes This parameter specifies the approximate size of each partition, rounded to the nearest 100 MB. Response structure

```
message ComputeSplitPointsBySizeResponse {
    required ConsumedCapacity consumed = 1;
    repeated PrimaryKeySchema schema = 2;
    /**
     * Split points between splits, in the ascending order.
```

`*`

```
     * A split is a consecutive range of primary keys,
     * whose data size is approximately split_size specified in the request.
     * The size could be hard to be precise.
```

`*`

```
     * A split point is an array of primary-key column w.r.t. table schema,
     * which is never longer than that of table schema.
     * Tailing -inf will be omitted to reduce transmission payloads.
```

`*/`

```
    repeated bytes split_points = 3;
    /**
     * Locations where splits lie.
```

`*`

```
     * By the managed nature of TableStore, these locations are no more than hints.
     * If a location is not suitable to be seen, an empty string will be placed.
```

`*/`

```
     message SplitLocation {
         required string location = 1;
         required sint64 repeat = 2;
     repeated SplitLocation locations = 4;
```

consumed: Type: ConsumedCapacity This parameter specifies the number of CUs consumed by this request. schema: Type: PrimaryKeySchema This parameter specifies the schema of the table. The schema is the same as the schema provided when the table is created. split _point s: Type: repeated bytes The split points between partitions. The split points must increase monotonically between the partitions. Each split point is a PlainBuffer-encoded line and contains only primary keys. The last -inf of each split point is not transmitted to reduce the volume of data transmitted. locat ions: Type: repeated SplitLocation This parameter specifies the prompt about the hosts where the split points reside. It can be null. For example, a table contains three columns of primary keys, where the first column is of the string type. After this API is called, five partitions are obtained, which are (-inf,-inf,-inf) to ("a",-inf,-inf), ("a",inf,-inf) to ("b",-inf,-inf), ("b",-inf,-inf) to ("c",-inf,-inf), ("c",-inf,-inf) to ("d",-inf,-inf), and ("d",-inf,-inf) to (+inf,+inf,+inf). The first three partitions reside in machine-A, while the last two in machine-B. In this

| case, split points is (example) _ | [("a"),("b"),("c"),("d")] |   |
|---|---|---|
| "machine-A"*3, "machine-B"*2 |   | . |

CU consumption The number of consumed read CUs is the same as that of the partitions. No write CUs are consumed.

##### 1.1.1.14 ListStream

Action You can use the ListStream API to obtain information about the stream that is enabled for all tables in the current instance. Request structure

```
message ListStreamRequest {
    optional string table_name = 1;
```

t able_name: Type: optional string This parameter specifies the name of the table for which the current stream is enabled. Response structure

```
message ListStreamResponse {
    repeated Stream streams = 1;
message Stream {
    required string stream_id = 1;
    required string table_name = 2;
    required int64 creation_time = 3;
```

st ream_id: Type: repeated string This parameter specifies the ID of the current stream. t able_name: Type: required string This parameter specifies the name of the table for which the current stream is enabled. creat ion_t ime: Type: required int64 This parameter specifies the time the current stream is enabled.

##### 1.1.1.15 DescribeStream

Action You can use the DescribeStream API to obtain information about the partitions of the current stream. Request structure

```
message DescribeStreamRequest {
    required string stream_id = 1;
    optional string inclusive_start_shard_id = 2;
    optional int32 shard_limit = 3;
```

st ream_id: Type: required string This parameter specifies the ID of the current stream. inclusive_st art _shard_id: Type: required string This parameter specifies the ID of the starting partition in a query. shard_limit : Type: required string This parameter specifies the upper limit of the returned partition quantity in a single query. Response structure

```
message DescribeStreamResponse {
    required string stream_id = 1;
    required int32 expiration_time = 2;
    required string table_name = 3;
    required int64 creation_time = 4;
    required StreamStatus stream_status = 5;
    repeated StreamShard shards = 6;
    optional string next_shard_id = 7;
message StreamShard {
    required string shard_id = 1;
    optional string parent_id = 2;
    optional string parent_sibling_id = 3;
```

st ream_id: Type: required string This parameter specifies the ID of the current stream. expirat ion_t ime: Type: required int32 This parameter specifies the expiration time of the stream. t able_name: Type: required string This parameter specifies the name of the table for which the current stream is enabled. creat ion_t ime: Type: required int32 This parameter specifies the time the current stream is enabled. st ream_st at us: Type: required StreamStatus This parameter specifies the status of the current stream, which can be enabling or active. shards: Type: required StreamShard This parameter specifies the information about the streamShard, including the partition ID, parent partition ID, and information about the neighbor partition of the parent partition (applicable when the parent partition is merged). next _shard_id: Type: optional string This parameter specifies the start ID of the next partition in a paging query. Note Data reading for the parent partition must be completed before data of the current partition is read.

##### 1.1.1.16 GetShardIterator

Action You can use the GetShardIterator API to obtain the response of the start iterator for reading the record information of the current partition. Request structure

```
message GetShardIteratorRequest {
    required string stream_id = 1;
    required string shard_id = 2;
```

st ream_id: Type: required string This parameter specifies the ID of the current stream. shard_id: Type: required string This parameter specifies the ID of the current partition. Response structure

```
message GetShardIteratorResponse {
    required string shard_iterator = 1;
```

shard_it erat or: Type: required string This parameter specifies the start iterator for reading the record of the current partition.

##### 1.1.1.17 GetStreamRecord

Action You can use the GetStreamRecord API to obtain the incremental content of the current partition. Request structure

```
message GetStreamRecordRequest {
    required string shard_iterator = 1;
    optional int32 limit = 2;
```

shard_it erat or: Type: required string This parameter specifies the iterator for reading the current partition next time. Response structure

```
message GetStreamRecordResponse {
    message StreamRecord {
        required ActionType action_type = 1;
        required bytes record = 2;
    repeated StreamRecord stream_records = 1;
    optional raw_string next_shard_iterator = 2;
    optional ConsumedCapacity consumed = 3;
```

St reamRecord: Type: repeated StreamRecord This parameter specifies the record entry for reading the current partition. shard_it erat or: Type: required string This parameter specifies the iterator for reading the current partition next time. consumed: Type: ConsumedCapacity This parameter specifies the number of CUs consumed by this operation. The sum of data in all rows of a table for stream read is calculated based on the following formula: Number of consumed read CUs = (Size of actually read columns/4 KB) rounded up.

##### 1.1.1.18 Tablestore ProtocolBuffer message definitions

This topic describes the detailed definitions of table_store.proto and table_store_filter.proto. table_store.proto

```java
package com.alicloud.openservices.tablestore.core.protocol; message Error {
    required string code = 1;
    optional string message = 2;
enum PrimaryKeyType {
    INTEGER = 1;
    STRING = 2;
    BINARY = 3;
enum PrimaryKeyOption {
    AUTO_INCREMENT = 1;
message PrimaryKeySchema {
    required string name = 1;
    required PrimaryKeyType type = 2;
    optional PrimaryKeyOption option = 3;
message TableOptions {
    optional int32 time_to_live = 1; // This parameter value can be dynamically modified.
    optional int32 max_versions = 2; // This parameter value can be dynamically modified.
    optional int64 deviation_cell_version_in_sec = 5; // This parameter value can be dynami
cally modified. message TableMeta {
    required string table_name = 1;
    repeated PrimaryKeySchema primary_key = 2;
enum RowExistenceExpectation {
    IGNORE = 0;
    EXPECT_EXIST = 1;
    EXPECT_NOT_EXIST = 2;
message Condition {
    required RowExistenceExpectation row_existence = 1;
    optional bytes column_condition      = 2;
message CapacityUnit { optionalint32read
```

```
    optional int32 read = 1;
    optional int32 write = 2;
message ReservedThroughputDetails {
    required CapacityUnit capacity_unit = 1; // This parameter indicates the current reserv
ed throughput of the table.
    required int64 last_increase_time = 2; // This parameter indicates the last time the re
served throughput was raised.
    optional int64 last_decrease_time = 3; // This parameter indicates the last time the re
served throughput was lowered. message ReservedThroughput {
    required CapacityUnit capacity_unit = 1;
message ConsumedCapacity {
    required CapacityUnit capacity_unit = 1;
/* ############################################# CreateTable ############################
################# */
/**
 * table_meta is used to store schema attributes that cannot be modified in a table. The Re
servedThroughput and TableOptions attributes that can be modified are stored as the paramet ers for UpdateTable.
 * message CreateTableRequest {
 *         required TableMeta table_meta = 1;
 *         required ReservedThroughput reserved_throughput = 2;
 *         required TableOptions table_options = 3;
 * }
```

`*/`

```
message CreateTableRequest {
    required TableMeta table_meta = 1;
    required ReservedThroughput reserved_throughput = 2;
    optional TableOptions table_options = 3;
message CreateTableResponse { /* ########################################################################################
################# */
/* ############################################# UpdateTable ############################
################# */
message UpdateTableRequest {
    required string table_name = 1;
    optional ReservedThroughput reserved_throughput = 2;
    optional TableOptions table_options = 3;
message UpdateTableResponse {
    required ReservedThroughputDetails reserved_throughput_details = 1;
    required TableOptions table_options = 2;
/* ########################################################################################
################# */
/* ############################################# DescribeTable ##########################
################### */
message DescribeTableRequest { requiredstringtablename=1;
```

```
    required string table_name  1;
message DescribeTableResponse {
    required TableMeta table_meta = 1;
    required ReservedThroughputDetails reserved_throughput_details = 2;
    required TableOptions table_options = 3;
    repeated bytes shard_splits = 6;
/* ########################################################################################
################### */
/* ############################################# ListTable ##############################
############### */
message ListTableRequest { /**
 * Only a simple name list is returned.
```

`*/`

```
message ListTableResponse {
    repeated string table_names = 1;
/* ########################################################################################
############### */
/* ############################################# DeleteTable ############################
################# */
message DeleteTableRequest {
    required string table_name = 1;
message DeleteTableResponse { /* ############################################# UnloadTable ############################
################# */
message UnloadTableRequest {
    required string table_name = 1;
message UnloadTableResponse { /* ########################################################################################
################## */
/**
 * Valid values: [0, INT64.MAX).
 * 1. To query data of a time range, specify start_time and end_time.
 * 2. To query data of a specific timestamp, specify specific_time.
```

`*/`

```
message TimeRange {
    optional int64 start_time = 1;
    optional int64 end_time = 2;
    optional int64 specific_time = 3;
/* ############################################# GetRow #################################
############ */
enum ReturnType {
    RT_NONE = 0;
    RT_PK = 1;
message ReturnContent {
```

`g`

```
    optional ReturnType return_type = 1;
/**
 * 1. You can specify the timestamp range or time to read the specified version of a column
```

`.`

```
 * 2. Intra-row breakpoints are not supported.
```

`*/`

```
message GetRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2; // encoded as InplaceRowChangeSet, but only has primary
key
    repeated string columns_to_get = 3; // If this parameter is not specified, all columns
are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional bytes filter = 7;
    optional string start_column = 8;
    optional string end_column = 9;
    optional bytes token = 10;
message GetRowResponse {
    required ConsumedCapacity consumed = 1;
    required bytes row = 2; // encoded as InplaceRowChangeSet
    optional bytes next_token = 3;
/* ########################################################################################
############ */
/* ############################################# UpdateRow ##############################
############### */
message UpdateRowRequest {
    required string table_name = 1;
    required bytes row_change = 2;
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
message UpdateRowResponse {
    required ConsumedCapacity consumed = 1;
    optional bytes row = 2;
/* ########################################################################################
############### */
/* ############################################# PutRow #################################
############ */
/**
 * You can set a timestamp for each column instead of configuring a unified timestamp for t
he entire row.
```

`*/`

```
message PutRowRequest {
    required string table_name = 1;
    required bytes row = 2; // encoded as InplaceRowChangeSet
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
message PutRowResponse {
```

```
    required ConsumedCapacity consumed = 1;
    optional bytes row = 2;
/* ########################################################################################
############ */
/* ############################################# DeleteRow ##############################
############### */
/**
 * Tablestore allows you only to delete versions of all columns from a row. It does not all
ow you to:
 *  1. Delete the specified version and versions earlier than it.
```

`*/`

```
message DeleteRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2; // encoded as InplaceRowChangeSet, but only has primary
key
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
message DeleteRowResponse {
    required ConsumedCapacity consumed = 1;
    optional bytes row = 2;
/* ########################################################################################
############### */
/* ############################################# BatchGetRow ############################
################# */
message TableInBatchGetRowRequest {
    required string table_name = 1;
    repeated bytes primary_key = 2; // encoded as InplaceRowChangeSet, but only has primary
key
    repeated bytes token = 3;
    repeated string columns_to_get = 4; &nbsp;// If this parameter is not specified, all co
lumns are read.
    optional TimeRange time_range = 5;
    optional int32 max_versions = 6;
    optional bytes filter = 8;
    optional string start_column = 9;
    optional string end_column = 10;
message BatchGetRowRequest {
    repeated TableInBatchGetRowRequest tables = 1;
message RowInBatchGetRowResponse {
    required bool is_ok = 1;
    optional Error error = 2;
    optional ConsumedCapacity consumed = 3;
    optional bytes row = 4; // encoded as InplaceRowChangeSet
    optional bytes next_token = 5;
message TableInBatchGetRowResponse {
    required string table_name = 1;
    repeated RowInBatchGetRowResponse rows = 2;
```

```
message BatchGetRowResponse {
    repeated TableInBatchGetRowResponse tables = 1;
/* ########################################################################################
################# */
/* ############################################# BatchWriteRow ##########################
################### */
enum OperationType {
    PUT = 1;
    UPDATE = 2;
    DELETE = 3;
message RowInBatchWriteRowRequest {
    required OperationType type = 1;
    required bytes row_change = 2; // encoded as InplaceRowChangeSet
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
message TableInBatchWriteRowRequest {
    required string table_name = 1;
    repeated RowInBatchWriteRowRequest rows = 2;
message BatchWriteRowRequest {
    repeated TableInBatchWriteRowRequest tables = 1;
message RowInBatchWriteRowResponse {
    required bool is_ok = 1;
    optional Error error = 2;
    optional ConsumedCapacity consumed = 3;
    optional bytes row = 4;
message TableInBatchWriteRowResponse {
    required string table_name = 1;
    repeated RowInBatchWriteRowResponse rows = 2;
message BatchWriteRowResponse {
    repeated TableInBatchWriteRowResponse tables = 1;
/* ########################################################################################
################### */
/* ############################################# GetRange ###############################
############## */
enum Direction {
    FORWARD = 0;
    BACKWARD = 1;
message GetRangeRequest {
    required string table_name = 1;
    required Direction direction = 2;
    repeated string columns_to_get = 3;  // If this parameter is not specified, all columns
are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional int32 limit = 6;
```

`i`

```
dbt
```

`i` `l` `i` `t` `t` `i` `k` `//` `d``d` `l` `R` `Ch` `S``t` `b``t`

```
    required bytes inclusive_start_primary_key = 7; // encoded as InplaceRowChangeSet, but
only has primary key
    required bytes exclusive_end_primary_key = 8; // encoded as InplaceRowChangeSet, but on
ly has primary key
    optional bytes filter = 10;
    optional string start_column = 11;
    optional string end_column = 12;
    optional bytes token = 13;
message GetRangeResponse {
    required ConsumedCapacity consumed = 1;
    required bytes rows = 2; // encoded as InplaceRowChangeSet
    optional bytes next_start_primary_key = 3; // If this parameter is not specified, all d
ata is read. next_start_primary_key is encoded as InplaceRowChangeSet, but only contains pr imary key.
    optional bytes next_token = 4;
/* #################### ComputeSplitPointsBySize #################### */ message ComputeSplitPointsBySizeRequest {
    required string table_name = 1;
    required int64 split_size = 2; // in 100MB
message ComputeSplitPointsBySizeResponse {
    required ConsumedCapacity consumed = 1;
    repeated PrimaryKeySchema schema = 2;
    /**
     * Split points between splits, in the increasing order
```

`*`

```
     * A split is a consecutive range of primary keys,
     * whose data size is about split_size specified in the request.
     * The size could be hard to be precise.
```

`*`

```
     * A split point is an array of primary-key column w.r.t. table schema,
     * which is never longer than that of table schema.
     * Tailing -inf will be omitted to reduce transmission payloads.
```

`*/`

```
    repeated bytes split_points = 3;
    /**
     * Locations where splits lies in.
```

`*`

```
     * By the managed nature of TableStore, these locations are no more than hints.
     * If a location is not suitable to be seen, an empty string will be placed.
```

`*/`

```
     message SplitLocation {
         required string location = 1;
         required sint64 repeat = 2;
     repeated SplitLocation locations = 4;
```

table_store_filter.proto

```java
package com.alicloud.openservices.tablestore.core.protocol; enum FilterType {
    FT_SINGLE_COLUMN_VALUE = 1;
    FT_COMPOSITE_COLUMN_VALUE = 2;
    FT_COLUMN_PAGINATION = 3;
enum ComparatorType {
    CT_EQUAL = 1;
    CT_NOT_EQUAL = 2;
    CT_GREATER_THAN = 3;
    CT_GREATER_EQUAL = 4;
    CT_LESS_THAN = 5;
    CT_LESS_EQUAL = 6;
message SingleColumnValueFilter {
    required ComparatorType comparator = 1;
    required string column_name = 2;
    required bytes column_value = 3;
    required bool filter_if_missing = 4;
    required bool latest_version_only = 5;
enum LogicalOperator {
    LO_NOT = 1;
    LO_AND = 2;
    LO_OR = 3;
message CompositeColumnValueFilter {
    required LogicalOperator combinator = 1;
    repeated Filter sub_filters = 2;
message ColumnPaginationFilter {
    required int32 offset = 1;
    required int32 limit = 2;
message Filter {
    required FilterType type = 1;
    required bytes filter = 2;  // Serialized string of filter of the type
```

##### 1.1.1.19 CreateIndex

You can call this operation to create an index table for the specified base table. Request syntax

```
message CreateIndexRequest {
    required string main_table_name = 1;
    required IndexMeta index_meta = 2;
    optional bool include_base_data = 3;
```

main_table_name Type: string. Required: yes. This parameter specifies the name of the base table for which to create an index table. index_meta Type: IndexMeta. Required: yes. This parameter specifies the schema of the index table to be created. include_base_data Type: Boolean. Required: no. This parameter specifies whether the existing data of the base table is included in the index table to be created. Response syntax

```
message CreateIndexResponse {
```

##### 1.1.1.20 DeleteIndex

You can call this operation to delete an index table from the specified base table. Request syntax

```
message DropIndexRequest {
    required string main_table_name = 1;
    required string index_name = 2;
```

main_table_name Type: string. Required: yes. This parameter specifies the name of the base table from which to delete an index table. index_name Type: string. Required: yes. This parameter specifies the name of the index table to be deleted. Response syntax

```
message DropIndexResponse {
```

#### 1.1.2 DataType

##### 1.1.2.1 ActionType

ActionType specifies the operation type in the response of the GetStreamRecord operation. Operation types include: PUT_ROW indicates that the operation type is PutRow. UPDATE_ROW indicates that the operation type is UpdateRow. DELETE_ROW indicates that the operation type is DeleteRow. Enumeration values

```
enum ActionType {
    PUT_ROW = 1;
    UPDATE_ROW = 2;
    DELETE_ROW = 3;
```

##### 1.1.2.2 CapacityUnit

CapacityUnit specifies the number of CUs consumed in an operation, or reserved read/write throughput of a table. Data structure

```
message CapacityUnit {
    optional int32 read = 1;
    optional int32 write = 2;
```

read: Type: int32 Description: the number of read CUs consumed by this operation or the reserved read throughput for this table. writ e: Type: int32 Description: the number of write CUs consumed by this operation or the reserved write throughput for this table.

##### 1.1.2.3 ColumnPaginationFilter

ColumnPaginationFilter specifies the filtering conditions for reading wide rows. This API is applicable to the Filter function. Data structure

```
message ColumnPaginationFilter {
 required int32 offset = 1;
 required int32 limit = 2;
```

of f set : Type: int32 Description: the position of the column to start reading from. limit : Type: int32 Description: the number of columns to be read.

##### 1.1.2.4 ComparatorType

ComparatorType is an arithmetical operator. It includes the following enumeration types: CT_EQUAL indicates equal to. CT_NOT_EQUAL indicates not equal to. CT_GREATER_THAN indicates greater than. CT_GREATER_EQUAL indicates not smaller than. CT_LESS_THAN indicates smaller than. CT_LESS_EQUAL indicates not greater than. Enumeration values

```
enum ComparatorType {
 CT_EQUAL = 1;
 CT_NOT_EQUAL = 2;
 CT_GREATER_THAN = 3;
 CT_GREATER_EQUAL = 4;
 CT_LESS_THAN = 5;
 CT_LESS_EQUAL = 6;
```

##### 1.1.2.5 CompositeColumnValueFilter

CompositeColumnValueFilter specifies a group of conditions, for example, column_a > 5 AND column_b = 10. This API is applicable to the ConditionUpdate and Filter functions. Data structure

```
message CompositeColumnValueFilter {
 required LogicalOperator combinator = 1;
 repeated Filter sub_filters = 2;
```

combinat or: Type: LogicalOperator Description: the logical operator. sub_f ilt er: Type: Filter Description: the sub-condition expression.

##### 1.1.2.6 Condition

Condition specifies the row judgment conditions in PutRow, UpdateRow, and DeleteRow. It contains the row_existence and column_condition parameters. Data structure

```
message Condition {
    required RowExistenceExpectation row_existence = 1;
    optional bytes column_condition      = 2;
```

row_exist ence: Type: RowExistenceExpectation Description: the row existence check settings for this row. column_condit ion: Type: bytes Description: the column condition settings. This parameter indicates the binary data (in bytes) after the filter is serialized in the Protobuf format.

##### 1.1.2.7 ConsumedCapacity

ConsumedCapacity indicates the number of capacity units (CUs) consumed by an operation. Data structure

```
message ConsumedCapacity {
    required CapacityUnit capacity_unit = 1;
```

capacit y_unit : Type: CapacityUnit Description: the number of CUs consumed by this operation.

##### 1.1.2.8 Direction

Direction indicates the data query order in the GetRange operation. The two Direction operations are: FORWARD indicates that the query proceeds in ascending order of primary key values. BACKWARD indicates that the query proceeds in descending order of primary key values. Enumeration values

```
enum Direction {
 FORWARD = 0;
 BACKWARD = 1;
```

##### 1.1.2.9 Error

Error indicates an error message returned when an operation fails. This parameter is also used to indicate errors for single-row requests in the BatchGetRow and BatchWriteRow operations. Data structure

```
Error {
 required string code = 1;
 optional string message = 2;
```

code: Type: string Description: the error code for the specified single-row operation. message: Type: string Description: the error message for the specified single-row operation.

##### 1.1.2.10 Filter

Filter specifies the column-based conditions. This API is applicable to the Conditional Update and Filter functions. Data structure

```
message Filter {
 required FilterType type = 1;
 required bytes filter = 2;
```

t ype: Type: FilterType Description: the column condition type. f ilt er: Type: bytes Description: the binary data generated after the condition statements of CompositeColumnValueFilter, ColumnPaginationFilter, or SingleColumnValueFilter are serialized in the Protobuf format.

##### 1.1.2.11 PrimaryKeyOption

PrimaryKeyOption specifies the attribute value of a primary key. Currently, it only supports AUTO_INCREMENT. Enumeration values

```
enum PrimaryKeyOption {
 AUTO_INCREMENT = 1;
```

##### 1.1.2.12 FilterType

FilterType specifies the type for condition updates or filters. The types include: FT_SINGLE_COLUMN_VALUE indicates a single-column condition. FT_COMPOSITE_COLUMN_VALUE indicates a multi-column composite condition. FT_COLUMN_PAGINATION indicates a wide-row read condition. Enumeration values

```
enum FilterType {
 FT_SINGLE_COLUMN_VALUE = 1;
 FT_COMPOSITE_COLUMN_VALUE = 2;
 FT_COLUMN_PAGINATION = 3;
```

##### 1.1.2.13 LogicalOperator

LogicalOperator specifies the enumeration type. The enumeration types include: LO_NOT indicates NOT. LO_AND indicates AND. LO_OR indicates OR. Enumeration values

```
enum LogicalOperator {
 LO_NOT = 1;
 LO_AND = 2;
 LO_OR = 3;
```

##### 1.1.2.14 OperationType

OperationType indicates the modification method for one column in UpdateRow. The types of operations include: PUT indicates that a column is inserted or data in this column is overwritten. UPDATE indicates that a column is updated. DELETE indicates that a column is deleted. Enumeration values

```
enum OperationType {
 PUT = 1;
 UPDATE = 2;
 DELETE = 3;
```

##### 1.1.2.15 PartitionRange

PartitionRange specifies the partition range. Data structure

```
message PartitionRange {
    required bytes begin = 1; // encoded as SQLVariant
    required bytes end = 2; // encoded as SQLVariant
```

begin: Type: bytes Description: the starting key of the partition. The partition range is a left-closed right-open interval, which includes the starting key. end: Type: bytes Description: the ending key of the partition. The partition range is a left-closed right-open interval, which excludes the ending key.

##### 1.1.2.16 PlainBuffer

Compared with Protocol Buffer, PlainBuffer delivers better performance for serialization and resolution of small objects. Therefore, PlainBuffer is used to format data in Tablestore. Format definition

```
plainbuffer = tag_header row1 [row2] [row3] row = ( pk [attr] | [pk] attr | pk attr ) [tag_delete_marker] row_checksum; pk = tag_pk cell_1 [cell_2] [cell_3] attr = tag_attr cell1 [cell_2] [cell_3] cell = tag_cell cell_name [cell_value] [cell_op] [cell_ts] cell_checksum cell_name = tag_cell_name formated_value cell_value = tag_cell_value formated_value cell_op = tag_cell_op cell_op_value cell_ts = tag_cell_ts cell_ts_value row_checksum = tag_row_checksum row_crc8 cell_checksum = tag_cell_checksum row_crc8 formated_value = value_type value_len value_data value_type = int8 value_len = int32 cell_op_value = delete_all_version | delete_one_version cell_ts_value = int64 delete_all_version = 0x01 (1byte) delete_one_version = 0x03 (1byte)
```

Tag values

```
tag_header = 0x75 (4byte) tag_pk = 0x01 (1byte) tag_attr = 0x02 (1byte) tag_cell = 0x03 (1byte) tag_cell_name = 0x04 (1byte) tag_cell_value = 0x05 (1byte) tag_cell_op = 0x06 (1byte) tag_cell_ts = 0x07 (1byte) tag_delete_marker = 0x08 (1byte) tag_row_checksum = 0x09 (1byte) tag_cell_checksum = 0x0A (1byte)
```

ValueType values Valid values of value_type in formated_value:

```
VT_INTEGER = 0x0 VT_DOUBLE = 0x1 VT_BOOLEAN = 0x2 VT_STRING = 0x3 VT_NULL = 0x6 VT_BLOB = 0x7 VT_INF_MIN = 0x9 VT_INF_MAX = 0xa VT_AUTO_INCREMENT = 0xb
```

Checksum calculation The checksum is calculated based on the following basic logic: The name, value, type, and timestamp of each cell is calculated. The delete mark of each row is calculated. A byte of 1 is added for each row that has a delete mark. A byte of 0 is added for each row that does not have a delete mark. After the checksum is calculated for each cell in a row, these cell checksums are used to calculate the row checksum. The CRC is performed only on the cells in the row, instead of data in the row. The following code provides an example on how to implement CRC in C++:

```
void GetChecksum(uint8_t* crc, const InplaceCell& cell)
```

`{`

```
    Crc8(crc, cell.GetName());
    Crc8(crc, cell.GetValue().GetInternalSlice());
    Crc8(crc, cell.GetTimestamp());
    Crc8(crc, cell.GetOpType());
void GetChecksum(uint8_t* crc, const InplaceRow& row)
```

`{`

```
    const std::deque<InplaceCell>& pk = row.GetPrimaryKey();
    for (size_t i = 0; i < pk.size(); i++) {
        uint8_t* cellcrc;
        *cellcrc = 0;
        GetChecksum(cellcrc, pk[i]);
        Crc8(crc, *cellcrc);
    for (int i = 0; i < row.GetCellCount(); i++) {
        uint8_t* cellcrc;
        *cellcrc = 0;
        GetChecksum(cellcrc, row.GetCell(i));
        Crc8(crc, *cellcrc);
    uint8_t del = 0;
    if (row.HasDeleteMarker()) {
        del = 1;
    Crc8(crc, del);
```

Example A row contains two primary key columns and four attribute columns. The data types of the primary key columns are string and integer, while the data types in the attribute columns are string, integer, and double. The versions are 1001, 1002, and 1003. The fourth attribute column indicates whether to delete all versions. Primary key columns: [pk1:string:iampk] [pk2:integer:100] Attribute columns: [column1:string:bad:1001] [column2:integer:128:1002] [column3:double:34.2:1003] [column4:del_all_versions] Encoding:

```xml
 <The start position for headers>[0x75]
 <The start position for primary key columns>[0x1]
 <Cell1>[0x3][0x4][3][pk1][0x5][3][5][iampk]
 <Cell2>[0x3][0x4][3][pk2][0x5][0][100]
 <The start position for attribute columns>[0x2]
 <Cell1>[0x3][0x4][7][column1][0x5][0x3][3][bad][0x7][1001]
 <Cell2>[0x3][0x4][7][column2][0x5][0x0][128][0x7][1002]
 <Cell3>[0x3][0x4][7][column3][0x5][0x1][34.2][0x7][1003]
 <Cell4>[0x3][0x4][7][column4][0x5][0x6][1]
```

##### 1.1.2.17 PrimaryKeySchema

PrimaryKeySchema specifies the attribute value of a primary key. Data structure

```
message PrimaryKeySchema {
 required string name = 1;
 required PrimaryKeyType type = 2;
 optional PrimaryKeyOption option = 3;
```

name: Type: string Description: the name of the column. t ype: Type: PrimaryKeyType Description: the type of the column. opt ion: Type: PrimaryKeyOption Description: the additional attribute value of the column.

##### 1.1.2.18 PrimaryKeyType

PrimaryKeyType specifies the type of a primary key. Enumeration data types INTEGER STRING BINARY

```
enum PrimaryKeyType {
 INTEGER = 1;
 STRING = 2;
 BINARY = 3;
```

##### 1.1.2.19 ReservedThroughput

ReservedThroughput indicates the reserved read/write throughput value for a table. Data structure

```
message ReservedThroughput {
 required CapacityUnit capacity_unit = 1;
```

capacit y_unit : Type: CapacityUnit Description: the current reserved read/write throughput value for the table.

##### 1.1.2.20 ReservedThroughputDetails

ReservedThroughputDetails indicates the reserved read/write throughput information of a table. Data structure

```
message ReservedThroughputDetails {
    required CapacityUnit capacity_unit = 1;
    required int64 last_increase_time = 2;
    optional int64 last_decrease_time = 3;
    required int32 number_of_decreases_today = 4;
```

capacit y_unit : Type: CapacityUnit Description: the reserved read/write throughput value for this table. last _increase_t ime: Type: int64 Description: the last time the reserved read/write throughput capacity was raised for this table. The value uses UTC time, in seconds. last _decrease_t ime: Type: int64 Description: the last time the reserved read/write throughput capacity was lowered for this table. The value uses UTC time, in seconds. number_of _decreases_t oday: Type: int32 Description: the number of times the reserved read/write throughput capacity was lowered for this table on the current calendar day.

##### 1.1.2.21 ReturnContent

ReturnContent specifies the content of the returned data. Data structure

```
message ReturnContent {
    optional ReturnType return_type = 1;
```

ret urn_t ype: Type: ReturnType Description: the type of the returned data.

##### 1.1.2.22 ReturnType

ReturnType specifies the type of the returned data. Enumeration data types

```
enum ReturnType {
    RT_NONE = 0;
    RT_PK = 1;
```

RT_NONE: the default value. This parameter indicates that no value is returned. RT_PK: This parameter indicates that the primary key is returned.

##### 1.1.2.23 RowExistenceExpectation

RowExistenceExpectation specifies conditions for row existence. Enumeration types are as follows: IGNORE indicates that the row existence check is not performed. EXPECT_EXIST indicates that the row is expected to exist. EXPECT_NOT_EXIST indicates that this row is not expected to exist. Enumeration values

```
enum RowExistenceExpectation {
    IGNORE = 0;
    EXPECT_EXIST = 1;
    EXPECT_NOT_EXIST = 2;
```

##### 1.1.2.24 RowInBatchGetRowResponse

RowInBatchGetRowResponse indicates a row of data in the response of the BatchGetRow operation. Data structure

```
message RowInBatchGetRowResponse {
 required bool is_ok = 1 [default = true];
 optional Error error = 2;
 optional ConsumedCapacity consumed = 3;
 optional bytes row = 4;
 optional bytes next_token = 5;
```

is_ok: Type: bool Description: determines whether the operation for this row succeeds. If true is returned, the row is read and error is invalid. If false is returned, the row fails to be read and the row is invalid. error: Type: Error Description: the error message for this row operation. consumed: Type: ConsumedCapacity Description: the number of capacity units consumed by this row operation. row: Type: bytes The read data is encoded in the PlainBuffer format. If this row does not exist, null is returned. next _t oken: Type: bytes This parameter specifies the starting position of a wide row in the next read operation. This function is currently unavailable.

##### 1.1.2.25 RowInBatchWriteRowRequest

RowInBatchWriteRowRequest indicates the information of the row to be written, updated, or deleted in the BatchWriteRow operation. Data structure

```
message RowInBatchWriteRowRequest {
    required OperationType type = 1;
    required bytes row_change = 2; // It is encoded as InplaceRowChangeSet.
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

t ype: Type: OperationType Description: the operation type. row_change: Type: bytes Description: the data in a row that contains the primary key and attribute columns. The columns are encoded in the PlainBuffer format. condit ion: Type: Condition Description: the value of conditional update, including the row existence condition and columnbased condition. ret urn_cont ent : Type: ReturnContent Required: no This parameter specifies the data type after the row is written. Currently, only the primary key is returned, which is used for the auto-increment function of the primary key column.

##### 1.1.2.26 RowInBatchWriteRowResponse

RowInBatchWriteRowResponse indicates the write operation result for a row in the response of the BatchWriteRow operation. Data structure

```
message RowInBatchWriteRowResponse {
 required bool is_ok = 1 [default = true];
 optional Error error = 2;
 optional ConsumedCapacity consumed = 3;
```

is_ok: Type: bool Description: determines whether the operation for this row succeeds. If the value is true, the row is written and error is invalid. If the value is false, this row fails to be written. error: Type: Error Description: the error message for this row operation. consumed: Type: ConsumedCapacity Description: the number of capacity units consumed by this row operation.

##### 1.1.2.27 SingleColumnValueFilter

SingleColumnValueFilter specifies a single condition, for example, column_a > 5. This API is applicable to the ConditionUpdate and Filter functions. Data structure

```
message SingleColumnValueFilter {
 required ComparatorType comparator = 1;
 required string column_name = 2;
 required bytes column_value = 3;
 required bool filter_if_missing = 4;
 required bool latest_version_only = 5;
```

comparat or: Type: ComparatorType Description: the comparison type. column_name: Type: string Description: the column name. column_value: Type: bytes Description: the value of ColumnValue serialized by protobuf. f ilt er_if _missing: Type: bool Description: determines whether a filtering condition is applicable if the column of a row does not exist. Assume that the condition is column_a > 0, and the value of filter_if_missing is true. If column_a does not exist for a row, the condition column_a > 0 is true. lat est _version_only: Type: bool Description: determines whether a condition is applicable only for the latest version. If the value is true, the value of the latest version is checked to determine whether it meets the condition. If the value is false, the values of all versions are checked to determine whether they meet the conditions.

##### 1.1.2.28 StreamDetails

StreamDetails indicates the stream information of a table. Data structure

```
message StreamDetails {
    required bool enable_stream = 1;
    optional string stream_id = 2;
    optional int32 expiration_time = 3;
    optional int64 last_enable_time = 4;
```

enable_st ream: Type: required bool Description: determines whether stream is enabled for the table. st ream_id: Type: optional string Description: the ID of the table stream. expirat ion_t ime: Type: optional int32 Description: the expiration time of the table stream. last _enable_t ime: Type: optional int64 Description: the time to enable the table stream.

##### 1.1.2.29 StreamRecord

StreamRecord indicates a row of data in the response of the GetStreamRecord operation. Data structure

```
 message StreamRecord {
        required ActionType action_type = 1;
        required bytes record = 2;
```

act ion_t ype: Type: required ActionType Description: the operation type of the row. record: Type: required bytes Description: the data content of the row.

##### 1.1.2.30 StreamSpecification

StreamSpecification indicates the stream specification of a table. Data structure

```
message StreamSpecification {
    required bool enable_stream = 1;
    optional int32 expiration_time = 2;
```

enable_st ream: Type: bool Description: determines whether stream is enabled for the table. expirat ion_t ime: Type: int32 Description: the expiration time of the table stream.

##### 1.1.2.31 TableInBatchGetRowRequest

TableInBatchGetRowRequest indicates the request information of the table to be read in the BatchGetRow operation. Data structure

```
message TableInBatchGetRowRequest {
    required string table_name = 1;
    repeated bytes primary_key = 2; // The primary key columns are encoded in the PlainBuff
er format.
    repeated bytes token = 3;
    repeated string columns_to_get = 4;  // If this parameter is not specified, all columns
are read.
    optional TimeRange time_range = 5;
    optional int32 max_versions = 6;
    optional bool cache_blocks = 7 [default = true]; // This parameter specifies whether th
e read data is written to BlockCache.
    optional bytes filter = 8;
    optional string start_column = 9;
    optional string end_column = 10;
```

t able_name: Type: string Description: the name of the table. primary_key: Type: repeated bytes Required: yes This parameter specifies all primary key columns in the row, including the primary key names and values. The primary key columns are encoded in the PlainBuffer format. t oken: Type: repeated bytes Required: no This parameter specifies the starting position of a wide row in the next read operation. This function is currently unavailable. columns_t o_get : Type: repeated string Description: the names of all columns to be returned from this table. t ime_range: Type: TimeRange Required: At least one of the time_range and max_versions parameters must be specified. This parameter specifies the range of timestamps to read versions of data. Unit: millisecond. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX. To query data of a time range, specify start_time and end_time. To query data of a specific timestamp, specify specific_time. Example: If the value of time_range is (100, 200), the timestamp of the returned column data must be within the range of [100, 200). max_versions: Type: int32 Required: At least one of the max_versions and time_range parameters must be specified. This parameter specifies the maximum number of versions of data to be returned. Example: If the value of max_versions is 2, data of a maximum of two versions is returned for each column. cache_blocks: Type: bool Required: no This parameter specifies whether the read data is written to BlockCache. The default value is true. This parameter cannot be set to false. f ilt er: Type: bytes Required: no This parameter specifies the expression of the filtering condition. It indicates the binary data after the filter is serialized in the Protobuf format. st art _column: Type: string Required: no This parameter specifies the first column to be read. It is useful for reading wide rows. The response contains the specified starting column. The column names are sorted lexicographically. Example: If a table contains columns A, B, and C, and the value of start_column is B, the data is read starting from column B. Columns B and C are returned. end_column: Type: string Required: no This parameter specifies the last column to be read. It is useful for reading wide rows. The response does not contain the specified ending column. The column names are sorted lexicographically. Example: If a table contains columns A, B, and C, and the value of end_column is B, the reading stops at column B. Only column A is returned.

##### 1.1.2.32 TableInBatchGetRowResponse

TableInBatchGetRowResponse indicates data in a table in the response of the BatchGetRow operation. Data structure

```
message TableInBatchGetRowResponse {
 required string table_name = 1;
 repeated RowInBatchGetRowResponse rows = 2;
```

t able_name: Type: string Description: the name of the table. rows: Type: repeated RowInBatchGetRowResponse Description: data of all rows read from the table.

##### 1.1.2.33 TableInBatchWriteRowRequest

TableInBatchWriteRowRequest indicates the request information of the table to be written in the BatchWriteRow operation. Data structure

```
message TableInBatchWriteRowRequest {
 required string table_name = 1;
 repeated RowInBatchWriteRowRequest rows = 2;
```

t able_name: Type: string Description: the name of the table. rows: Type: repeated RowInBatchWriteRowRequest Description: the information of the row to be inserted, updated, or deleted in the table.

##### 1.1.2.34 TableInBatchWriteRowResponse

TableInBatchWriteRowResponse indicates the write results for a table in the BatchWriteRow operation. Data structure

```
message TableInBatchWriteRowResponse {
 required string table_name = 1;
 repeated RowInBatchWriteRowResponse put_rows = 2;
 repeated RowInBatchWriteRowResponse update_rows = 3;
 repeated RowInBatchWriteRowResponse delete_rows = 4;
```

t able_name: Type: string Description: the name of the table. put _rows: Type: RowInBatchWriteRowResponse Description: the result of the PutRow operation for the table. updat e_rows: Type: RowInBatchWriteRowResponse Description: the result of the UpdateRow operation for the table. delet e_rows: Type: RowInBatchWriteRowResponse Description: the result of the DeleteRow operation for the table.

##### 1.1.2.35 TableMeta

TableMeta indicates the structure information of a table. Data structure

```
message TableMeta {
 required string table_name = 1;
 repeated PrimaryKeySchema primary_key = 2;
```

t able_name: Type: string. Description: the name of the table. primary_key: Type: PrimaryKeySchema Description: all primary key columns of the table.

##### 1.1.2.36 TableOptions

TableOptions indicates the table parameters, including TimeToLive and MaxVersions. Data structure

```
message TableOptions {
    optional int32 time_to_live = 1; // This parameter value can be dynamically modified.
    optional int32 max_versions = 2; // This parameter value can be dynamically modified.
    optional int64 deviation_cell_version_in_sec = 5; // This parameter value can be dynami
cally modified.
```

t ime_t o_live: Type: int32 Description: the retention time of data stored in this table, in seconds. max_versions: Type: int32 Description: the maximum number of versions stored in this table. deviat ion_cell_version_in_sec: Type: int64 Description: the maximum version deviation. This parameter is used to forbid writing data that deviates from the expected output. For example, if the value of deviation_cell_version_in_sec is 1,000 and the current timestamp is 10,000, the allowed timestamp range to be written is [10,000 - 1,000, 10,000 + 1,000].

##### 1.1.2.37 TimeRange

TimeRange specifies the timestamp range or timestamp value to query. Data structure

```
message TimeRange {
    optional int64 start_time = 1;
    optional int64 end_time = 2;
    optional int64 specific_time = 3;
```

st art _t ime: Type: int64 Description: the starting timestamp, in milliseconds. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX. end_t ime: Type: int64 Description: the ending timestamp, in milliseconds. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX. specif ic_t ime: Type: int64 Description: the specific timestamp, in milliseconds. You can set either specific_time to query a specific timestamp, or a combination of start_time and end_time to query a range of timestamps. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX.

## 2 SDK reference

### 2.1 SDK

#### 2.1.1 Java SDK

##### 2.1.1.1 Preface

This topic describes how to use Tablestore SDK for Java. This topic applies to Tablestore SDK for Java V5.0.0 and later. Prerequisites An authorized account is created, and an AccessKey pair (AccessKey ID and AccessKey secret) is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Unimanager Management Console, see Obtain an AccessKey pair. Compatibility Latest version: 5.7.0 Tablestore SDK for Java V4.x.x: compatible Tablestore SDK for Java V2.x.x: incompatible

##### 2.1.1.2 Installation

This topic describes how to install Tablestore SDK for Java. Preparations To install Tablestore SDK for Java, you must use JDK 6.0 or later versions. Install SDK You can install Tablestore SDK for Java by using one of the two following methods: Add dependencies to a Maven project To use Tablestore SDK for Java in Maven, you need only to add the corresponding dependencies to the pom.xml file. Tablestore SDK for Java V5.4.0. is used in this example. Add the following content to <dependencies>:

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
    <artifactId>tablestore</artifactId>
    <version>5.4.0</version>
</dependency>
```

Import JAR packages into Eclipse Take Tablestore SDK for Java V5.4.0 as an example. To import JAR packages into Eclipse, perform the following operations: i. Download the SDK for Java package. ii. Decompress the SDK for Java package. iii. Copy the tablestore-<versionId>.jar file and all files in the lib folder to your project. iv. Right-click your project name in Eclipse and choose Propert ies > Java Build Pat h > Add JARs. v. Select all JAR packages you copied in step 3. Sample programs Tablestore SDK for Java provides a variety of sample programs for your reference or use. You can decompress the downloaded SDK package and view the sample programs in the examples folder.

##### 2.1.1.3 Initialization

OTSClient is the client for Tablestore. It provides a series of methods for you to manage tables and perform read and write operations on a single row or multiple rows. To use Tablestore SDK for Java to initiate a request, you must initialize an OTSClient instance and modify the default configuration items of ClientConfiguration. Obtain an endpoint An endpoint is the domain name used to access a Tablestore instance in a region. The following table lists the examples of endpoints in the supported format.

| Examples | Description |
|---|---|
| http://sun.cn-hangzhou.ots.aliyuncs.com | The public endpoint used to access the sun instance in the China (Hangzhou) region over HTTP. |
| https://sun.cn-hangzhou.ots.aliyuncs.com | The public endpoint used to access the sun instance in the China (Hangzhou) region over HTTPS. |

Not e Tablestore supports access over the Internet and internal network. To query the endpoints of your Tablestore instance, perform the following operations:
1. Log on to the Tablestore console.
2. Click the instance name to go to the Inst ance Management page.
On the Instance Details tab, you can view the endpoints of the instance in Instance Access URL. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair (AccessKey ID and AccessKey secret) for signature authentication. The following types of AccessKey pairs are supported: The AccessKey pair (AccessKey ID and AccessKey secret) of your Apsara Stack tenant account. i. Create an Apsara Stack tenant account on the official Alibaba Cloud website. ii. Log on to the Apsara Uni-manager Management Console to apply for an AccessKey pair. The AccessKey pair (AccessKey ID and AccessKey secret) of a RAM user authorized to access Tablestore. i. Use your Apsara Stack tenant account to access RAM and create a new RAM user or use an existing one. ii. Use your Apsara Stack tenant account to authorize the RAM user to access Tablestore. iii. You can then use the AccessKey pair (AccessKey ID and AccessKey secret) of the authorized RAM user to access Tablestore. The AccessKey pair in temporary access credentials. i. The application server uses RAM or STS to obtain access credentials that consist of a temporary AccessKey ID, an AccessKey secret, and a token. After the access credentials are obtained, the application server sends them to you. ii. Use the received AccessKey ID, AccessKey Secret, and token to access Tablestore. Initialize a Tablestore client instance After you obtain the AccessKey ID and AccessKey secret, you can perform the following operation to initialize a Tablestore client instance: Create a client When you use Tablestore SDKs, you must create a client and then call the operations in the client to access Tablestore. The operations in the client provide the same functions as the RESTful API provided by Tablestore. Tablestore SDKs offer two client types: SyncClient and AsyncClient. SyncClient is designed for synchronous operations and AsyncClient is for asynchronous operations. After a synchronous operation is called, the service request succeeds. You can call synchronous operations to learn more about the various features of Tablestore. Compared with synchronous operations, asynchronous operations provide greater flexibility. If you require high performance, you can choose between the use of asynchronous operations and multithreading. Not e Both SyncClient and AsyncClient are thread-safe and can internally manage threads and connection resources. You do not need to create a client for each thread or request. Instead, create a global client. Examples The following code provides an example on how to use the default configurations to create a SyncClient:

```
        final String endPoint = "";
        final String accessKeyId = "";
        final String accessKeySecret = "";
        final String instanceName = "";
        SyncClient client = new SyncClient(endPoint, accessKeyId, accessKeySecret, instan
ceName);
```

The following code provides an example on how to use the custom configurations to create a SyncClient:

```
        // ClientConfiguration provides multiple configuration items. Only the most commo
nly used items are listed.
        ClientConfiguration clientConfiguration = new ClientConfiguration();
        // Set the timeout period for establishing a connection.
        clientConfiguration.setConnectionTimeoutInMillisecond(5000);
        // Set the timeout period for the socket connection.
        clientConfiguration.setSocketTimeoutInMillisecond(5000);
        // Configure a retry policy. If you do not configure policies, the default retry
policy is used.
        clientConfiguration.setRetryStrategy(new AlwaysRetryStrategy());
        SyncClient client = new SyncClient(endPoint, accessId, accessKey, instanceName, c
lientConfiguration);
```

HTTPS Upgrade to Java 7 for HTTPS access. Multithreading Multithreading is supported. We recommend that you use the same OTSClient object to perform multithreading tasks.

##### 2.1.1.4 Use Tablestore SDK for Java

###### 2.1.1.4.1 Table-level operations

Tablestore SDK for Java provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable When you create a table in Tablestore, you must specify TableMeta and TableOptions. You can also set ReservedThroughput. Not e After the table is created, Tablestore loads partitions of the table to a specified node. And you can read data from or write data to the table within a few seconds. An exception may occur if you immediately attempt to read from or write to the table after you create the table.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| tableMeta | The schema information of the data table. The schema information contains the following items: tableName: the name of the data table. primaryKey: the schema of the primary key for the data table. Not e Attribute columns are optional. Different rows in Tablestore can have different attribute columns. You can specify the names of attribute columns when you write data to the attribute columns. The primary key of a data table can contain one to four primary key columns. Primary key columns are sorted in the order in which they are added. For example, PRIMARY KEY (A, B, C) and PRIMARY KEY (A, C, B) have different primary key schemas. Tablestore sorts rows based on the values of all primary key columns. The first primary key column serves as the partition key. Data that has the same partition key value is stored in the same partition. Therefore, we recommend that you assign no more than 10 GB of data to partitions that have the same partition key value. Otherwise, a single partition may be too large to split. We recommend that you evenly distribute requests to read and write data to partitions that have different partition keys for load balancing. definedColumns: the predefined columns of the table and the data types of the predefined column values. Primary key columns cannot be specified as predefined columns. You can use predefined columns as the indexed columns or attribute columns for index tables. |

| Parameter | Description |
|---|---|
| tableOptions | The configuration information of the data table. The configurations include the following items: timeToLive: the period for which data in the data table can be retained. This period is the validity period of data. When the retention period exceeds the timeToLive value, Tablestore automatically deletes expired data. The minimum timeToLive is 86400, which is equal to one day. A value of -1 specifies that data never expires. When you create a data table, you can set timeToLive to -1 if you expect that data never expires. After the table is created, you can call the UpdateTable operation to modify the timeToLive value. Unit: seconds. Not e You must set timeToLive to -1 if you want to create an index table for a data table. maxVersions: the maximum number of versions of data that can be retained for a single attribute column. When the number of versions of data in attribute columns exceeds the maxVersions value, Tablestore automatically deletes the data of earlier versions. When you create a data table, you can customize the maximum number of versions that can be retained for the data in an attribute column. After the data table is created, you can call the UpdateTable operation to modify the maxVersions value for the data table. Not e You must set maxVersions to 1 if you want to create an index table for a data table. maxTimeDeviation: the max version offset, which is the maximum difference between the timestamp of the written data and the current system time. The difference between the version number and the data written time must be within the value of maxTimeDeviation. Otherwise, an error occurs when the data is written. Unit: seconds. The valid version range of data in an attribute column is calculated based on the formula: Valid version range = [max{Dat a writ t en t ime - Max version of f set , Dat a writ t en t ime - T T L value}, Dat a writ t en t ime + Max version of f set ). When you create a data table, Tablestore uses the default value of 86400 if you do not specify a max version offset. After the data table is created, you can call the UpdateTable operation to modify the max version offset value. Unit: seconds. |

| Parameter | Description |
|---|---|
| reservedThroughtput | The reserved read throughput and reserved write throughput of the data table. The reserved read throughput and reserved write throughput can be set to 0 for data tables only in capacity instances. Reserved throughput does not apply to these instances. The default value 0 specifies that all throughput is billed on a pay-as- you-go basis. Unit: capacity unit (CU). If reserved read throughput or reserved write throughput is set to a value greater than 0 for a data table, Tablestore allocates and reserves related resources for the data table. If reserved read throughput or reserved write throughput is set to 0, Tablestore does not allocate or reserve related resources for the table. |

| Parameter | Description |
|---|---|
| indexMetas | The schema information of the index tables. Each indexMeta contains the following items: indexName: the name of the index table. primaryKey: the indexed columns of the index table. The indexed columns are a combination of primary key columns and predefined columns of the data table. If you use the local secondary index feature, the first primary key column of an index table must be the same as the first primary key column of the corresponding data table. definedColumn: the indexed attribute columns. The attribute columns are a combination of predefined columns of the data table. indexType: the type of the index. Valid values: IT GLOBAL INDEX and _ _ IT LOCAL INDEX. _ _ If indexType is not specified or is set to IT GLOBAL INDEX, the _ _ global secondary index feature is used. If you use the global secondary index feature, Tablestore automatically synchronizes the columns to index and data in primary key columns from a data table to an index table in asynchronous mode. The synchronization latency is within a few milliseconds. If indexType is set to IT LOCAL INDEX, the local secondary index _ _ feature is used. If you use the local secondary index feature, Tablestore automatically synchronizes data from the indexed columns and the primary key columns of a data table to the columns of an index table in synchronous mode. After the data is written to the data table, you can query the data from the index table. indexUpdateMode: the update mode of the global secondary index. Valid values: IUM ASYNC INDEX and IUM SYNC INDEX. _ _ _ _ If indexUpdateMode is not specified or set to IUM ASYNC INDEX, _ _ the asynchronous mode is used to update the global secondary index. If you use the global secondary index feature, you must set the index update mode to IUM ASYNC INDEX. _ _ If you set indexUpdateMode to IUM SYNC INDEX, the synchronous _ _ update mode is used. If you use the local secondary index feature, you must set the update mode to IUM SYNC INDEX. _ _ |

Examples Create a data table without creating an index table

```java
private static void createTable(SyncClient client) {
        TableMeta tableMeta = new TableMeta(TABLE_NAME);
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME, PrimaryKeyTy
pe.STRING)); // Specify a primary key column for the data table.
        int timeToLive = -1; // Specify the validity period of data. A value of -1 specif
ies that the data never expires. Unit: seconds. You must set timeToLive to -1 for a data table that has index tables.
        int maxVersions = 3; // Specify the maximum number of versions that can be retain
ed for each column. A value of 1 specifies that only the latest version is retained for e ach column. You must set maxVersions to 1 if you want to create an index table for a data table.
        TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
        CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions);
        request.setReservedThroughput(new ReservedThroughput(new CapacityUnit(0, 0))); //
Set the reserved read throughput and reserved write throughout. The reserved read through put and reserved write throughput can be set to 0 for data tables only in capacity instan ces. However, you can set a non-zero value for data tables in high-performance instances.
        client.createTable(request);
```

Create a data table and an index table whose index type is global secondary index

```java
private static void createTable(SyncClient client) {
    TableMeta tableMeta = new TableMeta(TABLE_NAME);
    tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_1, PrimaryKeyType
.STRING)); // Add a primary key column to the data table.
    tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_2, PrimaryKeyType
.INTEGER)); // Add a primary key column to the data table.
    tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_1, DefinedColumnT
ype.STRING)); // Add a predefined column to the data table.
    tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_2, DefinedColumnT
ype.INTEGER)); // Add a predefined column to the data table.
    int timeToLive = -1; // Specify the validity period of data. A value of -1 specifies
that the data never expires. Unit: seconds. You must set timeToLive to -1 for a data tabl e that has index tables.
    int maxVersions = 1; // Specify the maximum number of versions that can be retained f
or each column. A value of 1 specifies that only the latest version is retained for each column. You must set maxVersions to 1 if you want to create an index table for a data tab le.
    TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
    ArrayList<IndexMeta> indexMetas = new ArrayList<IndexMeta>();
    IndexMeta indexMeta = new IndexMeta(INDEX_NAME);
    indexMeta.addPrimaryKeyColumn(DEFINED_COL_NAME_1); // Add a primary key column to the
index table.
    indexMeta.addDefinedColumn(DEFINED_COL_NAME_2); // Add an attribute column to the ind
ex table.
    indexMetas.add(indexMeta);
    CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions, indexMet
as); // Create the index table when you create the data table.
    client.createTable(request);
```

Create a data table and an index table whose index type is local secondary index

```java
private static void createTable(SyncClient client) {
    TableMeta tableMeta = new TableMeta(TABLE_NAME);
    tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_1, PrimaryKeyType
.STRING)); // Add a primary key column to the data table.
    tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_2, PrimaryKeyType
.INTEGER)); // Add a primary key column to the data table.
    tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_1, DefinedColumnT
ype.STRING)); // Add a predefined column to the data table.
    tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_2, DefinedColumnT
ype.INTEGER)); // Add a predefined column to the data table.
    int timeToLive = -1; // Specify the validity period of data. A value of -1 specifies
that the data never expires. Unit: seconds. You must set timeToLive to -1 for a data tabl e that has index tables.
    int maxVersions = 1; // Specify the maximum number of versions that can be retained f
or each column. A value of 1 specifies that only the latest version is retained for each column. You must set maxVersions to 1 if you want to create an index table for a data tab le.
    TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
    ArrayList<IndexMeta> indexMetas = new ArrayList<IndexMeta>();
    IndexMeta indexMeta = new IndexMeta(INDEX_NAME);
    indexMeta.setIndexType(IT_LOCAL_INDEX);     // Set the index type to IT_LOCAL_INDEX,
which specifies a local secondary index.
    indexMeta.setIndexUpdateMode(IUM_SYNC_INDEX);  // Set the index update mode to IUM_SY
NC_INDEX, which specifies the synchronous update mode. If the index type is set to IT_LOC AL_INDEX, the index update mode must be set to IUM_SYNC_INDEX.
    indexMeta.addPrimaryKeyColumn(PRIMARY_KEY_NAME_1); // Add a primary key column to the
index table. The first primary key column of the index table must be the same as that of the data table.
    indexMeta.addPrimaryKeyColumn(DEFINED_COL_NAME_1); // Add a primary key column to the
index table.
    indexMeta.addDefinedColumn(DEFINED_COL_NAME_2); // Add an attribute column to the ind
ex table.
    indexMetas.add(indexMeta);
    CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions, indexMet
as); // Create the index table when you create the data table.
    client.createTable(request);
```

ListTable You can call this operation to query the names of all tables created in the current instance. Examples The following code provides an example on how to query the names of all tables in an instance:

```java
private static void listTable(SyncClient client) {
    ListTableResponse response = client.listTable();
    System.out.println("List of tables:");
    for (String tableName : response.getTableNames()) {
        System.out.println(tableName);
```

UpdateTable You can call this operation to update the reserved read/write throughput and table options of a table. For more information about the ReservedThroughput and TableOptions parameters, see the CreateTable section. The minimum interval between attempts to modify the value of ReservedThroughput is one minute. Examples The following code provides an example on how to update the timeToLive and MaxVersions values of a table:

```java
private static void updateTable(SyncClient client) {
    int timeToLive = -1;
    int maxVersions = 5; // Update the value of MaxVersions to 5.
    TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
    UpdateTableRequest request = new UpdateTableRequest(TABLE_NAME);
    request.setTableOptionsForUpdate(tableOptions);
    client.updateTable(request);
```

DescribeTable You can call this operation to query the structure information, table option configurations, and reserved read/write throughput settings of a table. For more information about the TableMeta and TableOptions parameters, see the CreateTable section. Besides the reserved read/write throughput, ReservedThroughputDetails shows the most recent time when the throughput was increased or decreased. Examples The following code provides an example on how to query the description of a table:

```java
private static void describeTable(SyncClient client) {
    DescribeTableRequest request = new DescribeTableRequest(TABLE_NAME);
    DescribeTableResponse response = client.describeTable(request);
    TableMeta tableMeta = response.getTableMeta();
    System.out.println("The name of the table:" + tableMeta.getTableName());
    System.out.println("The primary key of the table:");
    for (PrimaryKeySchema primaryKeySchema : tableMeta.getPrimaryKeyList()) {
        System.out.println(primaryKeySchema);
    TableOptions tableOptions = response.getTableOptions();
    System.out.println("TTL of the table:" + tableOptions.getTimeToLive());
    System.out.println("MaxVersions the table:" + tableOptions.getMaxVersions());
    ReservedThroughputDetails reservedThroughputDetails = response.getReservedThroughputDet
ails();
    System.out.println("Reserved read throughput of the table:"
            + reservedThroughputDetails.getCapacityUnit().getReadCapacityUnit());
    System.out.println("Reserved write throughput of the table:"
            + reservedThroughputDetails.getCapacityUnit().getWriteCapacityUnit());
```

DeleteTable You can call this operation to delete a specified table from the current instance. Examples The following code provides an example on how to delete a specified table from the current instance:

```java
private static void deleteTable(SyncClient client) {
    DeleteTableRequest request = new DeleteTableRequest(TABLE_NAME);
    client.deleteTable(request);
```

###### 2.1.1.4.2 Single-row operations

Tablestore SDK for Java provides the following single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can call this operation to insert a row of data. If this row already exists, it is overwritten. When you perform PutRow, you can use conditional update to set conditions for the existence of the row to write or values in certain columns of the existing row. For more information, see Conditional update. Example 1 The following code provides an example on how to write a row that contains 10 attribute columns and write one version of data for each column. The version number (timestamp) is specified by the server.

```java
private static void putRow(SyncClient client, String pkValue) {
    // Create the primary key.
    PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString(pk
Value));
    PrimaryKey primaryKey = primaryKeyBuilder.build();
    RowPutChange rowPutChange = new RowPutChange(TABLE_NAME, primaryKey);
    // Add attribute columns.
    for (int i = 0; i < 10; i++) {
        rowPutChange.addColumn(new Column("Col" + i, ColumnValue.fromLong(i)));
    client.putRow(new PutRowRequest(rowPutChange));
```

Example 2 The following code provides an example on how to write a row that contains 10 attribute columns and write three versions of data for each column. The version number (timestamp) is specified by the client.

```java
private static void putRow(SyncClient client, String pkValue) {
    // Create the primary key.
    PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString(pk
Value));
    PrimaryKey primaryKey = primaryKeyBuilder.build();
    RowPutChange rowPutChange = new RowPutChange(TABLE_NAME, primaryKey);
    // Add attribute columns.
    long ts = System.currentTimeMillis();
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 3; j++) {
            rowPutChange.addColumn(new Column("Col" + i, ColumnValue.fromLong(j), ts + j)
```

);

```
    client.putRow(new PutRowRequest(rowPutChange));
```

Example 3 The following code provides an example on how to write data when the target row does not exist:

```java
private static void putRow(SyncClient client, String pkValue) {
    // Create the primary key.
    PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString(pk
Value));
    PrimaryKey primaryKey = primaryKeyBuilder.build();
    RowPutChange rowPutChange = new RowPutChange(TABLE_NAME, primaryKey);
    // Set a condition to specify that the target row does not exist.
    rowPutChange.setCondition(new Condition(RowExistenceExpectation.EXPECT_NOT_EXIST));
    // Add attribute columns.
    long ts = System.currentTimeMillis();
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 3; j++) {
            rowPutChange.addColumn(new Column("Col" + i, ColumnValue.fromLong(j), ts + j)
```

);

```
    client.putRow(new PutRowRequest(rowPutChange));
```

Example 4 The following code provides an example on how to write data when the target row exists and the value of Col0 is greater than 100:

```java
private static void putRow(SyncClient client, String pkValue) {
    // Create the primary key.
    PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString(pk
Value));
    PrimaryKey primaryKey = primaryKeyBuilder.build();
    RowPutChange rowPutChange = new RowPutChange(TABLE_NAME, primaryKey);
    // Set a condition to specify that the target row exists and the value in Col0 of the
target row is greater than 100.
    Condition condition = new Condition(RowExistenceExpectation.EXPECT_EXIST);
    condition.setColumnCondition(new SingleColumnValueCondition("Col0",
            SingleColumnValueCondition.CompareOperator.GREATER_THAN, ColumnValue.fromLong
(100)));
    rowPutChange.setCondition(condition);
    // Add attribute columns.
    long ts = System.currentTimeMillis();
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 3; j++) {
            rowPutChange.addColumn(new Column("Col" + i, ColumnValue.fromLong(j), ts + j)
```

);

```
    client.putRow(new PutRowRequest(rowPutChange));
```

GetRow You can call this operation to read a single row of data. The following table describes the parameter you can use for this operation.

| Parameter | Description |
|---|---|
| PrimaryKey | The primary key of the row to read. This parameter is required. |
| ColumnsToGet | The set of the columns to read. If you do not set this parameter, all columns are read. |
| MaxVersions | The maximum number of versions to read. You must set at least one of the following parameters: MaxVersions or TimeRange. |
| TimeRange | The range of versions to read. You must set at least one of the following parameters: MaxVersions or TimeRange. |
| Filter | Filters are used by the server to filter the read results based on the specified conditions. |

Example 1 The following code provides an example on how to read the latest version of data in the columns specified by ColumnsToGet of a row:

```java
        private static void getRow(SyncClient client, String pkValue) {
            // Create the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            // Read a row of data.
            SingleRowQueryCriteria criteria = new SingleRowQueryCriteria(TABLE_NAME, prim
aryKey);
            // Set MaxVersions to 1 to read the latest version of data.
            criteria.setMaxVersions(1);
            GetRowResponse getRowResponse = client.getRow(new GetRowRequest(criteria));
            Row row = getRowResponse.getRow();
            System.out.println("Read complete, result: ");
            System.out.println(row);
            // Specify the columns to read.
            criteria.addColumnsToGet("Col0");
            getRowResponse = client.getRow(new GetRowRequest(criteria));
            row = getRowResponse.getRow();
            System.out.println("Read complete, result:");
            System.out.println(row);
```

Example 2 The following code provides an example on how to set a filter:

```java
        private static void getRow(SyncClient client, String pkValue) {
            // Create the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            // Read a row of data.
            SingleRowQueryCriteria criteria = new SingleRowQueryCriteria(TABLE_NAME, prim
aryKey);
            // Set MaxVersions to 1 to read the latest version of data.
            criteria.setMaxVersions(1);
            // Set the filter so that this row is returned when the value in Col0 is 0.
            SingleColumnValueFilter singleColumnValueFilter = new SingleColumnValueFilter
("Col0",
                    SingleColumnValueFilter.CompareOperator.EQUAL, ColumnValue.fromLong(0
));
            // If Col0 does not exist, the data is not returned.
            singleColumnValueFilter.setPassIfMissing(false);
            criteria.setFilter(singleColumnValueFilter);
            GetRowResponse getRowResponse = client.getRow(new GetRowRequest(criteria));
            Row row = getRowResponse.getRow();
            System.out.println("Read complete, result: ");
            System.out.println(row);
```

UpdateRow You can call this operation to update a single row of data. If the target row does not exist, a new row is added. The update operations include writing a column, deleting a column, and deleting a version of data in a column. When you perform UpdateRow, you can use conditional update to configure conditions for the existence of the row to update or values in certain columns of the existing row. For more information, see Conditional update. Example 1 The following code provides an example on how to update several columns, delete the specified version of data in a column, and delete the specified column:

```java
        private static void updateRow(SyncClient client, String pkValue) {
            // Construct the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            RowUpdateChange rowUpdateChange = new RowUpdateChange(TABLE_NAME, primaryKey)
```

;

```
            // Update columns.
            for (int i = 0; i < 10; i++) {
                rowUpdateChange.put(new Column("Col" + i, ColumnValue.fromLong(i)));
            // Delete a specified version of data in the specified column.
            rowUpdateChange.deleteColumn("Col10", 1465373223000L);
            // Delete the specified column.
            rowUpdateChange.deleteColumns("Col11");
            client.updateRow(new UpdateRowRequest(rowUpdateChange));
```

Example 2 The following code provides an example on how to configure update conditions:

```java
        private static void updateRow(SyncClient client, String pkValue) {
            // Create the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            RowUpdateChange rowUpdateChange = new RowUpdateChange(TABLE_NAME, primaryKey)
```

;

```
            // Update data when the specified row exists and the value in Col0 is greater
than 100.
            Condition condition = new Condition(RowExistenceExpectation.EXPECT_EXIST);
            condition.setColumnCondition(new SingleColumnValueCondition("Col0",
                    SingleColumnValueCondition.CompareOperator.GREATER_THAN, ColumnValue.
fromLong(100)));
            rowUpdateChange.setCondition(condition);
            // Update columns.
            for (int i = 0; i < 10; i++) {
                rowUpdateChange.put(new Column("Col" + i, ColumnValue.fromLong(i)));
            // Delete a specified version of data in the specified column.
            rowUpdateChange.deleteColumn("Col10", 1465373223000L);
            // Delete the specified column.
            rowUpdateChange.deleteColumns("Col11");
            client.updateRow(new UpdateRowRequest(rowUpdateChange));
```

DeleteRow You can call this operation to delete a row. When you perform DeleteRow, you can use conditional update to configure conditions for the existence of the row to delete or values in certain columns of the existing row. For more information, see Conditional update. Example 1 The following code provides an example on how to delete a row:

```java
        private static void deleteRow(SyncClient client, String pkValue) {
            // Create the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            RowDeleteChange rowDeleteChange = new RowDeleteChange(TABLE_NAME, primaryKey)
```

;

```
            client.deleteRow(new DeleteRowRequest(rowDeleteChange));
```

Example 2 The following code provides an example on how to set deletion conditions:

```java
        private static void deleteRow(SyncClient client, String pkValue) {
            // Create the primary key.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuild
er();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromS
tring(pkValue));
            PrimaryKey primaryKey = primaryKeyBuilder.build();
            RowDeleteChange rowDeleteChange = new RowDeleteChange(TABLE_NAME, primaryKey)
```

;

```
            // Delete data when the specified row exists and the value in Col0 exceeds 10
```

`0.`

```
            Condition condition = new Condition(RowExistenceExpectation.EXPECT_EXIST);
            condition.setColumnCondition(new SingleColumnValueCondition("Col0",
                    SingleColumnValueCondition.CompareOperator.GREATER_THAN, ColumnValue.
fromLong(100)));
            rowDeleteChange.setCondition(condition);
            client.deleteRow(new DeleteRowRequest(rowDeleteChange));
```

###### 2.1.1.4.3 Multi-row operations

Tablestore SDK for Java provides multi-row operations such as BatchGetRow, BatchWriteRow, GetRange, and createRangeIterator. BatchGetRow You can call this operation to read data from multiple rows by sending a single request. The parameters are the same as those of the GetRow operation. Note that BatchGetRow uses the same parameter configurations for all rows. For example, if ColumnsToGet is set to colA, only the value of colA is read for all the rows. Similar to the use of the BatchWriteRow operation, you must check the response when you use the BatchGetRow operation. If the operation fails for some rows, an exception may not occur, but information about the failed rows is stored in BatchGetRowResponse. You can use the BatchGetRowResponse#getFailedRows method to query information about the failed rows. Use the BatchGetRowResponse#isAllSucceed method to determine whether all rows is obtained. Examples The following code provides an example on how to read 10 rows of data, and configure the version conditions, columns to read, and filters:

```java
        private static void batchGetRow(SyncClient client) {
            MultiRowQueryCriteria multiRowQueryCriteria = new MultiRowQueryCriteria(TABLE_N
AME);
            // Add 10 rows to read.
            for (int i = 0; i < 10; i++) {
                PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBui
lder();
                primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fro
mString("pk" + i));
                PrimaryKey primaryKey = primaryKeyBuilder.build();
                multiRowQueryCriteria.addRow(primaryKey);
            // Add conditions.
            multiRowQueryCriteria.setMaxVersions(1);
            multiRowQueryCriteria.addColumnsToGet("Col0");
            multiRowQueryCriteria.addColumnsToGet("Col1");
            SingleColumnValueFilter singleColumnValueFilter = new SingleColumnValueFilter("
Col0",
                    SingleColumnValueFilter.CompareOperator.EQUAL, ColumnValue.fromLong(0))
```

;

```
            singleColumnValueFilter.setPassIfMissing(false);
            multiRowQueryCriteria.setFilter(singleColumnValueFilter);
            BatchGetRowRequest batchGetRowRequest = new BatchGetRowRequest();
            // BatchGetRow allows you to read data from multiple tables. A single multiRowQ
ueryCriteria corresponds to a query condition for one table. You can add multiple multiRowQ ueryCriteria conditions to read data from multiple tables.
            batchGetRowRequest.addMultiRowQueryCriteria(multiRowQueryCriteria);
            BatchGetRowResponse batchGetRowResponse = client.batchGetRow(batchGetRowRequest
```

);

```java
            System.out.println("Were all successful:" + batchGetRowResponse.isAllSucceed())
```

;

```java
            if (!batchGetRowResponse.isAllSucceed()) {
                for (BatchGetRowResponse.RowResult rowResult : batchGetRowResponse.getFaile
dRows()) {
                    System.out.println("Failed rows:" + batchGetRowRequest.getPrimaryKey(ro
wResult.getTableName(), rowResult.getIndex()));
                    System.out.println("Cause of failure:" + rowResult.getError());
                /**
                 * You can use the createRequestForRetry method to construct another reques
t to retry failed rows. Only the retry request is constructed here.
                 * We recommend that you use the custom retry policy in Tablestore SDK for
Java as the retry method. This feature allows you to retry failed rows after batch operatio ns. After you set the retry policy, you do not need to add retry code when you call the ret ry operation.
```

`*/`

```
                BatchGetRowRequest retryRequest = batchGetRowRequest.createRequestForRetry(
batchGetRowResponse.getFailedRows());
```

BatchWriteRow You can call this operation to write data to multiple rows by sending a single request. The write operations include PutRow, UpdateRow, and DeleteRow. This operation also allows you to write data to multiple tables at a time. The process to create a BatchWriteRow operation is the same as that to create a PutRow, UpdateRow, or DeleteRow operation. You can also set update conditions. When you call the BatchWriteRow operation, you must check the response. When multiple rows are written, some rows may fail to be written. If the operation fails for some rows, an exception may not occur, but information about the index and error messages of the failed rows is stored in BatchWriteRowResponse. You can use the isAllSucceed method in BatchWriteRowResponse to determine whether all rows are written. We recommend that you check the response in case of failed operations. In some situations, exceptions may occur when you call the BatchWriteRow operation. For example, if the server detects incorrect parameters during some operations, a parameter exception may occur when none of the operations are completed for the request. Examples The following code provides an example of how to send a single BatchWriteRow request, which includes two PutRow operations, one UpdateRow operation, and one DeleteRow operation.

```java
        private static void batchWriteRow(SyncClient client) {
            BatchWriteRowRequest batchWriteRowRequest = new BatchWriteRowRequest();
            // Construct rowPutChange1.
            PrimaryKeyBuilder pk1Builder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            pk1Builder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString("pk
1"));
            RowPutChange rowPutChange1 = new RowPutChange(TABLE_NAME, pk1Builder.build());
            // Add columns.
            for (int i = 0; i < 10; i++) {
                rowPutChange1.addColumn(new Column("Col" + i, ColumnValue.fromLong(i)));
            // Add rowPutChange1 to the batch operation.
            batchWriteRowRequest.addRowChange(rowPutChange1);
            // Construct rowPutChange2.
            PrimaryKeyBuilder pk2Builder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            pk2Builder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString("pk
2"));
            RowPutChange rowPutChange2 = new RowPutChange(TABLE_NAME, pk2Builder.build());
            // Add columns.
            for (int i = 0; i < 10; i++) {
                rowPutChange2.addColumn(new Column("Col" + i, ColumnValue.fromLong(i)));
            // Add rowPutChange2 to the batch operation.
            batchWriteRowRequest.addRowChange(rowPutChange2);
            // Construct rowUpdateChange.
            PrimaryKeyBuilder pk3Builder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            pk3Builder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString("pk
3"));
            RowUpdateChange rowUpdateChange = new RowUpdateChange(TABLE_NAME, pk3Builder.bu
ild());
            // Add columns.
            for (int i = 0; i < 10; i++) {
                rowUpdateChange.put(new Column("Col" + i, ColumnValue.fromLong(i)));
```

```java
            // Delete the specified column.
            rowUpdateChange.deleteColumns("Col10");
            // Add rowUpdateChange to the batch operation.
            batchWriteRowRequest.addRowChange(rowUpdateChange);
            // Construct rowDeleteChange.
            PrimaryKeyBuilder pk4Builder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            pk4Builder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString("pk
4"));
            RowDeleteChange rowDeleteChange = new RowDeleteChange(TABLE_NAME, pk4Builder.bu
ild());
            // Add rowDeleteChange to the batch operation.
            batchWriteRowRequest.addRowChange(rowDeleteChange);
            BatchWriteRowResponse response = client.batchWriteRow(batchWriteRowRequest);
            System.out.println("Were all successful:" + response.isAllSucceed());
            if (!response.isAllSucceed()) {
                for (BatchWriteRowResponse.RowResult rowResult : response.getFailedRows())
```

`{`

```java
                    System.out.println("Failed rows:" + batchWriteRowRequest.getRowChange(r
owResult.getTableName(), rowResult.getIndex()).getPrimaryKey());
                    System.out.println("Cause of failure:" + rowResult.getError());
                /**
                 * You can use the createRequestForRetry method to construct another reques
t to retry failed rows. Only the retry request is constructed here.
                 * We recommend that you use the custom retry policy in Tablestore SDK for
Java as the retry method. This feature allows you to retry failed rows after batch operatio ns. After you set the retry policy, you do not need to add retry code when you call the ret ry operation.
```

`*/`

```
                BatchWriteRowRequest retryRequest = batchWriteRowRequest.createRequestForRe
try(response.getFailedRows());
```

GetRange You can call this operation to read data within a range. In Tablestore tables, all rows are sorted by primary key. The primary key of a table sequentially consists of all primary key columns. Therefore, do not assume that the rows are sorted based on a certain primary key column. The GetRange operation allows you to read data in a forward or backward direction within a specified range. You can also specify the number of rows to read. If the range is large and the number of scanned rows or the volume of data exceeds the limit, the scan stops and the read rows and the next primary key are returned. If the rows are not all read, you can initiate a request to start from where the last operation left off and read the remaining rows based on the next primary key returned by the previous operation. The following table describes the parameters of GetRange requests.

| Parameter | Description |
|---|---|
| Direction | The enumeration type. Valid values: FORWARD and BACKWARD. |
| InclusiveStartPrimaryKey | The primary key of the row from which the range read starts. The row that contains the start primary key is within the valid range to read. If you set Direction to BACKWARD, the value of the start primary key must be greater than that of the end primary key. |
| ExclusiveEndPrimaryKey | The primary key of the row at which the range read ends. The row that contains the end primary key is not within the valid range to read. If you set Direction to BACKWARD, the value of the start primary key must be greater than that of the end primary key. |
| Limit | The maximum number of rows to return for this request. |
| ColumnsToGet | The set of columns to read. If you do not specify this parameter, all columns are read. |
| MaxVersions | The maximum number of versions to read. You must set at least one of the following parameters: MaxVersions or TimeRange. |
| TimeRange | The range of versions to read. You must set at least one of the following parameters: MaxVersions or TimeRange. |
| Filter | Filters are used by the server to filter the read results based on the specified conditions. |

Examples The following code provides an example on how to read data within a specified range in forward order and return NextStartPrimaryKey. If the value of NextStartPrimaryKey is null, all data within the range is read.

```java
       private static void getRange(SyncClient client, String startPkValue, String endPkVal
ue) {
            RangeRowQueryCriteria rangeRowQueryCriteria = new RangeRowQueryCriteria(TABLE_N
AME);
            // Specify the primary key to start from.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder
();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromStr
ing(startPkValue));
            rangeRowQueryCriteria.setInclusiveStartPrimaryKey(primaryKeyBuilder.build());
            // Specify the primary key to end with.
            primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromStr
ing(endPkValue));
            rangeRowQueryCriteria.setExclusiveEndPrimaryKey(primaryKeyBuilder.build());
            rangeRowQueryCriteria.setMaxVersions(1);
            System.out.println("GetRange result:");
            while (true) {
                GetRangeResponse getRangeResponse = client.getRange(new GetRangeRequest(ran
geRowQueryCriteria));
                for (Row row : getRangeResponse.getRows()) {
                    System.out.println(row);
                // If the NextStartPrimaryKey value is not null, continue the read operatio
```

`n.`

```
                if (getRangeResponse.getNextStartPrimaryKey() != null) {
                    rangeRowQueryCriteria.setInclusiveStartPrimaryKey(getRangeResponse.getN
extStartPrimaryKey());
                } else {
                    break;
```

createRangeIterator You can call this operation to read data by iteration. Examples

```java
        private static void getRangeByIterator(SyncClient client, String startPkValue, Stri
ng endPkValue) {
            RangeIteratorParameter rangeIteratorParameter = new RangeIteratorParameter(TABL
E_NAME);
            // Specify the primary key to start from.
            PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder
();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromStr
ing(startPkValue));
            rangeIteratorParameter.setInclusiveStartPrimaryKey(primaryKeyBuilder.build());
            // Specify the primary key to end with.
            primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
            primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromStr
ing(endPkValue));
            rangeIteratorParameter.setExclusiveEndPrimaryKey(primaryKeyBuilder.build());
            rangeIteratorParameter.setMaxVersions(1);
            Iterator<Row> iterator = client.createRangeIterator(rangeIteratorParameter);
            System.out.println("Results obtained when Iterator is used to implement GetRang
e:");
            while (iterator.hasNext()) {
                Row row = iterator.next();
                System.out.println(row);
```

###### 2.1.1.4.4 Auto-increment function of the primary key column

column This topic describes how to create an auto-increment primary key column. An auto-increment primary key column cannot be the partition key. If you write data to a table that contains an auto-increment primary key column, you do not need to specify a value for the auto-increment primary key column because Tablestore generates a value for the auto-increment primary key column. The generated value for the auto-increment primary key column is unique, and all values in auto-increment primary key columns increase sequentially in a partition. This feature applies to system design scenarios that require auto-increment primary key columns, such as item IDs on e-commerce websites, user IDs of large websites, post IDs in forums, and message IDs in chat tools. Not e Tablestore SDK for Java V4.2.0 and later support auto-increment function of the primary key column. Features Auto-increment function of the primary key column have the following features: The values in auto-increment primary key columns are unique and increase sequentially but not always continuously in a partition. The data type of the value in an auto-increment primary key column is 64-bit signed long integer. You can create an auto-increment primary key column for a table. Tables that contain and do not contain auto-increment primary key columns can be in the same instance. Not e Auto-increment function of the primary key column do not affect the rule of conditional update. Limits Auto-increment function of the primary key column has the following limits: You can create at most one auto-increment primary key column for a table. An auto-increment primary key column cannot be the partition key. You can create an auto-increment primary key column only when you create a table. You cannot create an auto-increment primary key column for an existing table. An auto-increment primary key column can only be an integer column. The data type of the generated value for an auto-increment primary key column is 64-bit signed long integer. An auto-increment column cannot be an attribute column. API operations The following table lists the operations for auto-increment function of the primary key column.

| API operation | Description |
|---|---|
| CreateTable | When you create a table, you cannot set the partition key to be an auto-increment primary key column. If you set the partition key to be an auto-increment primary key column, values in the column cannot be generated automatically. |
| UpdateTable | After a table is created, you cannot use the UpdateTable operation to change a primary key column to an auto-increment primary key column. |
| PutRow | When you write data to a table, you do not need to specify a value for the auto-increment primary key column. Tablestore generates a value for the auto-increment primary key column. You can set ReturnType to RT PK to obtain a complete primary key _ value and use the value in GetRow to query data. |
| UpdateRow |   |
| BatchWriteRow |   |
| GetRow | You must use a complete primary key value when you use GetRow. To obtain a complete primary key value, you can set ReturnType to RT PK _ in PutRow, UpdateRow, or BatchWriteRow. |
| BatchGetRow |   |

Examples The use of auto-increment primary key columns involve the CreateTable, PutRow, UpdateRow, and BatchWriteRow operations.
1. Create a table
To create an auto-increment primary key column when you create a table, you must set AUTO_INCREMENT as the attribute of the primary key column.

```java
private static void createTable(SyncClient client) {
        TableMeta tableMeta = new TableMeta("table_name");
        // Create the first primary key column, which is also the partition key.
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema("PK_1", PrimaryKeyType.STRIN
G));
        // Create the second primary key column, and set it to be an auto-increment col
umn. The type is set to integer, and the attribute is set to AUTO_INCREMENT.
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema("PK_2", PrimaryKeyType.INTEG
ER, PrimaryKeyOption.AUTO_INCREMENT));
        int timeToLive = -1;  // Specify that data never expires.
        int maxVersions = 1;  // Specify that only one version is saved.
        TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
        CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions);
        client.createTable(request);
```

2. Write data
When you write data to a table, you do not need to specify a value for the auto-increment primary key column. Instead, you can set the value in the auto-increment primary key column to AUTO_INCREMENT.

```java
    private static void putRow(SyncClient client, String receive_id) {
        // Create the primary key.
        PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder
();
        // Specify the value in the first primary key column to the first four digits o
f md5(receive_id).
        primaryKeyBuilder.addPrimaryKeyColumn("PK_1", PrimaryKeyValue.fromString("Hangz
hou");
        // Specify the value in the second primary key column to AUTO_INCREMENT. The se
cond primary key column is an auto-increment primary key column, and you do not need to specify a value for it. Tablestore generates a value for the auto-increment primary key column.
        primaryKeyBuilder.addPrimaryKeyColumn("PK_2", PrimaryKeyValue.AUTO_INCREMENT);
        PrimaryKey primaryKey = primaryKeyBuilder.build();
        RowPutChange rowPutChange = new RowPutChange("table_name", primaryKey);
        // Set ReturnType to RT_PK to include the primary key value in the returned res
ult. If ReturnType is not set, no result is returned by default.
        rowPutChange.setReturnType(ReturnType.RT_PK);
        // Add attribute columns.
        rowPutChange.addColumn(new Column("content", ColumnValue.fromString(content)));
        // Write data to the table.
        PutRowResponse response = client.putRow(new PutRowRequest(rowPutChange));
        // Display the returned primary key value.
        Row returnRow = response.getRow();
        if (returnRow != null) {
            System.out.println("PrimaryKey:" + returnRow.getPrimaryKey().toString());
        // Display the consumed capacity units (CUs).
        CapacityUnit  cu = response.getConsumedCapacity().getCapacityUnit();
        System.out.println("Read CapacityUnit:" + cu.getReadCapacityUnit());
        System.out.println("Write CapacityUnit:" + cu.getWriteCapacityUnit());
```

###### 2.1.1.4.5 Conditional update

If you use conditional update, data in the table can be updated only when the conditions are met. If the conditions are not met, the update fails. Conditional update supports arithmetic operations including =, !, =, >, >=, <, and <= and logic operations including NOT, AND, and OR. You can use a combination of up to 10 conditions in an update operation. You can use conditional update in the PutRow, UpdateRow, DeleteRow, and BatchWriteRow operations. Conditional updates can be used to implement optimistic locking. When you update a row, the value of the specified column is obtained. For example, the value in Column A is 1. Obtain the value in Column A and set a condition that t he value in Column A is 1. Update t he value in Column A t o 2. If Column A of the row is updated by other clients, the update fails. Column-based judgment conditions include column-based conditions and the row existence condition.

| Column-based judgment condition | Description |
|---|---|
| Column-based condition | Column-based conditions support SingleColumnValueCondition and CompositeColumnValueCondition, which are used to perform the condition- based judgment based on the values of one or more columns. Column-based conditions are similar to the conditions used by Tablestore filters. |
| Row existence condition | When you update a table, the system checks the row existence condition. If the row existence condition is not met, an error occurs during the update. The row existence condition is classified into the following types: IGNORE EXPECT EXIST _ EXPECT NOT EXIST _ _ For more information, see Row existence condition update rules. |

Row existence condition update rules Not e BatchWriteRow is a set of multiple PutRow, UpdateRow, and DeleteRow operations. when you manage data in the table by using the BatchWriteRow operation, see the update rules of the corresponding operation based on the operation type.

| API operations | IGNORE | EXPECT EXIST _ | EXPECT NOT EXIST _ _ |
|---|---|---|---|
| PutRow: The row exists. | Fail | Succeed | Fail |
| PutRow: The row does not exist. | Succeed | Fail | Fail |
| UpdateRow: The row exists. | Fail | Succeed | Fail |
| UpdateRow: The row does not exist. | Succeed | Fail | Fail |

| Developer Guide·SDK refere | nce |   | Tablestor |
|---|---|---|---|
| API operations | IGNORE | EXPECT EXIST _ | EXPECT NOT EXIST _ _ |

| DeleteRow: The row exists. | Succeed | Succeed | Fail |
|---|---|---|---|
| DeleteRow: The row does not exist. | Fail | Fail | Fail |

Examples The following code provides examples on how to use column-based judgment conditions and implement optimistic locking: Construct a SingleColumnValueCondition.

```
 // Set the condition: Col0==0.
 SingleColumnValueCondition singleColumnValueCondition = new SingleColumnValueCondition("
Col0",
         SingleColumnValueCondition.CompareOperator.EQUAL, ColumnValue.fromLong(0));
 // If Col0 does not exist, the condition is not met.
 singleColumnValueCondition.setPassIfMissing(false);
 // Only check the latest version.
 singleColumnValueCondition.setLatestVersionsOnly(true);
```

Construct a CompositeColumnValueCondition.

```
 // Set the condition composite1: (Col0 = 0) AND (Col1 > 100).
 CompositeColumnValueCondition composite1 = new CompositeColumnValueCondition(CompositeCo
lumnValueCondition.LogicOperator.AND);
 SingleColumnValueCondition single1 = new SingleColumnValueCondition("Col0",
         SingleColumnValueCondition.CompareOperator.EQUAL, ColumnValue.fromLong(0));
 SingleColumnValueCondition single2 = new SingleColumnValueCondition("Col1",
         SingleColumnValueCondition.CompareOperator.GREATER_THAN, ColumnValue.fromLong(10
0));
 composite1.addCondition(single1);
 composite1.addCondition(single2);
 // Set the condition composite2: ( (Col0 == 0) AND (Col1 > 100) ) OR (Col2 <= 10).
 CompositeColumnValueCondition composite2 = new CompositeColumnValueCondition(CompositeCo
lumnValueCondition.LogicOperator.OR);
 SingleColumnValueCondition single3 = new SingleColumnValueCondition("Col2",
         SingleColumnValueCondition.CompareOperator.LESS_EQUAL, ColumnValue.fromLong(10))
```

;

```
 composite2.addCondition(composite1);
 composite2.addCondition(single3);
```

The following code provides an example of how to implement optimistic locking by incrementing the value of a column:

```java
 private static void updateRowWithCondition(SyncClient client, String pkValue) {
     // Create the primary key.
     PrimaryKeyBuilder primaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
     primaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME, PrimaryKeyValue.fromString(p
kValue));
     PrimaryKey primaryKey = primaryKeyBuilder.build();
     // Read a row of data.
     SingleRowQueryCriteria criteria = new SingleRowQueryCriteria(TABLE_NAME, primaryKey)
```

;

```java
     criteria.setMaxVersions(1);
     GetRowResponse getRowResponse = client.getRow(new GetRowRequest(criteria));
     Row row = getRowResponse.getRow();
     long col0Value = row.getLatestColumn("Col0").getValue().asLong();
     // Configure the conditional update to increment the value of Col0 by 1.
     RowUpdateChange rowUpdateChange = new RowUpdateChange(TABLE_NAME, primaryKey);
     Condition condition = new Condition(RowExistenceExpectation.EXPECT_EXIST);
     ColumnCondition columnCondition = new SingleColumnValueCondition("Col0", SingleColum
nValueCondition.CompareOperator.EQUAL, ColumnValue.fromLong(col0Value));
     condition.setColumnCondition(columnCondition);
     rowUpdateChange.setCondition(condition);
     rowUpdateChange.put(new Column("Col0", ColumnValue.fromLong(col0Value + 1)));
     try {
         client.updateRow(new UpdateRowRequest(rowUpdateChange));
     } catch (TableStoreException ex) {
         System.out.println(ex.toString());
```

###### 2.1.1.4.6 Filters

Tablestore filters are used to filter the query results on the server side. The server returns only the rows or columns that match the filter conditions. Filters can be used for GetRow, BatchGetRow, and GetRange operations. Tablestore supports only SingleColumnValueFilter and CompositeColumnValueFilter, which are used to determine whether to filter out a row based on reference column values. SingleColumnValueFilter can be used to determine whether to filter out of a row based on a single reference column value. CompositeColumnValueFilter can be used to determine whether to filter out of a row based on the combination of multiple reference column values. Note that filters are used to filter the read data. Therefore, the reference columns used by SingleColumnValueFilter or CompositeColumnValueFilter must be included in the read data. If the data to read does not contain the reference columns, filters cannot obtain the values in the reference columns. Examples The following code provides an example on how to construct a SingleColumnValueFilter:

```
        // Set the filter so that when the value in Col0 is 0, the row is returned.
        SingleColumnValueFilter singleColumnValueFilter = new SingleColumnValueFilter("Co
l0",
                SingleColumnValueFilter.CompareOperator.EQUAL, ColumnValue.fromLong(0));
        // If Col0 does not exist, the data is not returned.
        singleColumnValueFilter.setPassIfMissing(false);
        // Only check the latest version.
        singleColumnValueFilter.setLatestVersionsOnly(true);
```

The following code provides an example on how to construct a CompositeColumnValueFilter:

```
        // Set filters composite1: (Col0 == 0) AND (Col1 > 100).
        CompositeColumnValueFilter composite1 = new CompositeColumnValueFilter(CompositeC
olumnValueFilter.LogicOperator.AND);
        SingleColumnValueFilter single1 = new SingleColumnValueFilter("Col0",
                SingleColumnValueFilter.CompareOperator.EQUAL, ColumnValue.fromLong(0));
        SingleColumnValueFilter single2 = new SingleColumnValueFilter("Col1",
                SingleColumnValueFilter.CompareOperator.GREATER_THAN, ColumnValue.fromLon
g(100));
        composite1.addFilter(single1);
        composite1.addFilter(single2);
        // Set filters composite2: ( (Col0 == 0) AND (Col1 > 100) ) OR (Col2 <= 10).
        CompositeColumnValueFilter composite2 = new CompositeColumnValueFilter(CompositeC
olumnValueFilter.LogicOperator.OR);
        SingleColumnValueFilter single3 = new SingleColumnValueFilter("Col2",
                SingleColumnValueFilter.CompareOperator.LESS_EQUAL, ColumnValue.fromLong(
10));
        composite2.addFilter(composite1);
        composite2.addFilter(single3);
```

###### 2.1.1.4.7 Global secondary indexes

This topic describes how to create, use, and delete a global secondary index. Create a global secondary index You can create a global secondary index when you create a table. You can also create a global secondary index for an existing table. Create a global secondary index when you create a table

```java
   private static void createTable(SyncClient client) {
        TableMeta tableMeta = new TableMeta(TABLE_NAME);
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_1, PrimaryKey
Type.STRING)); // Add a primary key column to the table.
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME_2, PrimaryKey
Type.INTEGER)); // Add a primary key column to the table.
        tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_1, DefinedCol
umnType.STRING)); // Add a predefined attribute column to the table.
        tableMeta.addDefinedColumn(new DefinedColumnSchema(DEFINED_COL_NAME_2, DefinedCol
umnType.INTEGER)); // Add a predefined attribute column to the table.
        int timeToLive = -1; // Specify the validity period of data in seconds. A value o
f -1 indicates that the data never expires. You must specify -1 as the timeToLive value w hen a table has one or more index tables.
        int maxVersions = 1; // Specify the maximum number of versions. You must specify
1 as the value when a table has one or more index tables.
        TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
        ArrayList<IndexMeta> indexMetas = new ArrayList<IndexMeta>();
        IndexMeta indexMeta = new IndexMeta(INDEX_NAME);
        indexMeta.addPrimaryKeyColumn(DEFINED_COL_NAME_1); // Add a primary key column to
the index table.
        indexMeta.addDefinedColumn(DEFINED_COL_NAME_2); // Add an attribute column to the
index table.
        indexMetas.Add(indexMeta);
        CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions, inde
xMetas); // Create an index table when you create a table.
        client.createTable(request);
```

Create a global secondary index for an existing table Not e You can set the IncludeBaseData parameter in CreateInexRequest to specify whether the index table includes the existing data in the table. When the IncludeBaseData parameter in CreateInexRequest is set to true, the index table includes the existing data. When the value is false, the index table does not include the existing data.

```java
private static void createIndex(SyncClient client) {
    IndexMeta indexMeta = new IndexMeta(INDEX_NAME); // Create an index named Meta.
    indexMeta.addPrimaryKeyColumn(DEFINED_COL_NAME_2); // Specify DEFINED_COL_NAME_2 as t
he first primary key column of the index table.
    indexMeta.addPrimaryKeyColumn(DEFINED_COL_NAME_1); // Specify DEFINED_COL_NAME_1 as t
he second primary key column of the index table.
    CreateIndexRequest request = new CreateIndexRequest(TABLE_NAME, indexMeta, true); //
Add the index to the base table. Specify that the existing data of the base table is incl uded in the index table.
    CreateIndexRequest request = new CreateIndexRequest(TABLE_NAME, indexMeta, false); //
Add the index to the base table. Specify that the existing data of the base table is not included in the index table.
    /**If you set IncludeBaseData to true, the existing data of the base table is synchro
nized to the index table. Then you can query all data from the index table. The time used to synchronize data depends on the size of the existing data in the base table.
```

`*/`

```
    request.setIncludeBaseData(true);
    client.createIndex(request); // Create the index table.
```

Query data from a global secondary index If the index table includes the attribute columns to return, you can query data from the index table. If the index table does not include the attribute columns to return, the base table is queried. Query data from the index table when the index table includes the attribute columns to return.

```java
private static void scanFromIndex(SyncClient client) {
    RangeRowQueryCriteria rangeRowQueryCriteria = new RangeRowQueryCriteria(INDEX_NAME);
// Specify the index table name.
    // Specify the primary key from which the query starts.
    PrimaryKeyBuilder startPrimaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder(
```

);

```java
    startPrimaryKeyBuilder.addPrimaryKeyColumn(DEFINED_COL_NAME_1, PrimaryKeyValue.INF_MI
N); // Specify the minimum value for an indexed attribute column.
    startPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_1, PrimaryKeyValue.INF_MI
N); // Specify the minimum value for a primary key column.
    startPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_2, PrimaryKeyValue.INF_MI
N); // Specify the minimum value for a primary key column.
    rangeRowQueryCriteria.setInclusiveStartPrimaryKey(startPrimaryKeyBuilder.build());
    // Specify the primary key at which the query ends.
    PrimaryKeyBuilder endPrimaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    endPrimaryKeyBuilder.addPrimaryKeyColumn(DEFINED_COL_NAME_1, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for an indexed attribute column.
    endPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_1, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for a primary key column.
    endPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_2, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for a primary key column.
    rangeRowQueryCriteria.setExclusiveEndPrimaryKey(endPrimaryKeyBuilder.build());
    rangeRowQueryCriteria.setMaxVersions(1);
    System.out.println("The results returned from an index table:");
    while (true) {
        GetRangeResponse getRangeResponse = client.getRange(new GetRangeRequest(rangeRowQ
ueryCriteria));
        for (Row row : getRangeResponse.getRows()) {
            System.out.println(row);
        // If the nextStartPrimaryKey value is not null, continue to read data.
        if (getRangeResponse.getNextStartPrimaryKey() != null) {
            rangeRowQueryCriteria.setInclusiveStartPrimaryKey(getRangeResponse.getNextSta
rtPrimaryKey());
        } else {
            break;
```

Query data from the base table when the index table does not include the attribute columns to return.

```java
private static void scanFromIndex(SyncClient client) {
    RangeRowQueryCriteria rangeRowQueryCriteria = new RangeRowQueryCriteria(INDEX_NAME);
// Specify the index table name.
    // Specify the primary key from which the query starts.
    PrimaryKeyBuilder startPrimaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder(
```

);

```
    startPrimaryKeyBuilder.addPrimaryKeyColumn(DEFINED_COL_NAME_1, PrimaryKeyValue.INF_MI
N); // Specify the minimum value for an indexed attribute column.
    startPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_1, PrimaryKeyValue.INF_MI
N); // Specify the minimum value for a primary key column.
    startPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_2, PrimaryKeyValue.INF_MI
```

```java
N); // Specify the minimum value for a primary key column.
    rangeRowQueryCriteria.setInclusiveStartPrimaryKey(startPrimaryKeyBuilder.build());
    // Specify the primary key at which the query ends.
    PrimaryKeyBuilder endPrimaryKeyBuilder = PrimaryKeyBuilder.createPrimaryKeyBuilder();
    endPrimaryKeyBuilder.addPrimaryKeyColumn(DEFINED_COL_NAME_1, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for an indexed attribute column.
    endPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_1, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for a primary key column.
    endPrimaryKeyBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME_2, PrimaryKeyValue.INF_MAX)
; // Specify the maximum value for a primary key column.
    rangeRowQueryCriteria.setExclusiveEndPrimaryKey(endPrimaryKeyBuilder.build());
    rangeRowQueryCriteria.setMaxVersions(1);
    while (true) {
        GetRangeResponse getRangeResponse = client.getRange(new GetRangeRequest(rangeRowQ
ueryCriteria));
        for (Row row : getRangeResponse.getRows()) {
            PrimaryKey curIndexPrimaryKey = row.getPrimaryKey();
            PrimaryKeyColumn pk1 = curIndexPrimaryKey.getPrimaryKeyColumn(PRIMARY_KEY_NAM
E1);
            PrimaryKeyColumn pk2 = curIndexPrimaryKey.getPrimaryKeyColumn(PRIMARY_KEY_NAM
E2);
            PrimaryKeyBuilder mainTablePKBuilder = PrimaryKeyBuilder.createPrimaryKeyBuil
der();
            mainTablePKBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME1, pk1.getValue());
            mainTablePKBuilder.addPrimaryKeyColumn(PRIMARY_KEY_NAME2, ke2.getValue());
            PrimaryKey mainTablePK = mainTablePKBuilder.build(); // Construct the primary
key to query the base table based on the primary key of the index table.
            // Query the table.
            SingleRowQueryCriteria criteria = new SingleRowQueryCriteria(TABLE_NAME, main
TablePK);
            criteria.addColumnsToGet(DEFINED_COL_NAME3); // Read the DEFINED_COL_NAME3 at
tribute column from the base table.
            // Set the latest version to read.
            criteria.setMaxVersions(1);
            GetRowResponse getRowResponse = client.getRow(new GetRowRequest(criteria));
            Row mainTableRow = getRowResponse.getRow();
            System.out.println(row);
        // If the nextStartPrimaryKey value is not null, continue to read data.
        if (getRangeResponse.getNextStartPrimaryKey() != null) {
            rangeRowQueryCriteria.setInclusiveStartPrimaryKey(getRangeResponse.getNextSta
rtPrimaryKey());
        } else {
            break;
```

Delete a global secondary index Delete an index table.

```java
private static void deleteIndex(SyncClient client) {
    DeleteIndexRequest request = new DeleteIndexRequest(TABLE_NAME, INDEX_NAME); // Specify
the name of the index table that you want to delete and the name of the corresponding base table.
    client.deleteIndex(request); // Delete the index table.
```

##### 2.1.1.5 Error handling

This topic describes the error handling methods in Tablestore SDK for Java. Methods Tablestore SDK for Python handles errors as exceptions. If an operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions Tablestore SDK for Java has two types of exceptions: OTSClientError and OTSServiceError. Both are inherited from Exception. OTSClientError: an internal SDK exception, such as an invalid parameter value. OTSException: a server error parsed from a server error message. OTSServiceError contains the following parameters: getHttpStatus(): an HTTP status code, such as 200 or 404. getErrorCode(): an error type string returned by Tablestore. getRequestId(): the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help.

#### 2.1.2 Python SDK

##### 2.1.2.1 Preface

This topic describes how to use Tablestore SDK for Python. The content in this topic applies to Tablestore SDK for Python V4.x.x. Prerequisites An authorized account is created, and an AccessKey pair (AccessKey ID and AccessKey secret) is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Unimanager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for Python Download Tablestore SDK for Python by using the SDK package. For more information, see SDK package. Download Tablestore SDK for Python by using GitHub. For more information, visit GitHub. Compatibility Tablestore SDK for Python V5.x.x: compatible. Tablestore SDK for Python V4.x.x: compatible. Tablestore SDK for Python V2.x.x: incompatible. Tablestore SDK for Python V2.x.x supports primary key columns in random order, which are no longer supported in Tablestore SDK for Python V4.0.0 and later. Tablestore SDK for Python V4.x.x and Tablestore SDK for Python V2.x.x are incompatible in the following respects: The package name is changed from ots2 to tablestore. The TableOptions parameter is added for the Client.create_table operation. The type of the primary_key parameter is changed from dict to list for the put_row, get_row, and update_row operations to ensure the sequence of primary keys. The type of the attribute_columns parameter is changed from dict to list for the put_row and update_row operations. The timestamp parameter is added to the attribute_columns parameter for the put_row and update_row operations. The max_version and time_range parameters are added for the get_row and get_range operations. You must specify at least one of max_version and time_range. The return_type parameter is added for the put_row, update_row, and delete_row operations. Only RT_PK is supported to return the primary key value of the current row. The return_row parameter is added for the put_row, update_row, and delete_row operations. If you set return_type to RT_PK in the request, the primary key value of the row is returned in return_row. Version Latest version: 5.1.0.

##### 2.1.2.2 Installation

This topic describes how to install Tablestore SDK for Python. Preparations Python 2 or Python 3 is available. Install Tablestore SDK for Python Method 1: Use pip. Run the following command to install Tablestore SDK for Python:

```python
sudo pip install tablestore
```

Method 2: Use GitHub. Ensure that you have installed Git. For more information about how to download Git, visit Git. After Git is installed, run the following command:

```python
git clone https://github.com/aliyun/aliyun-tablestore-python-sdk.git sudo python setup.py install
```

Method 3: Use source code. i. Download the SDK package. ii. Decompress the SDK package, and then run the following command:

```python
sudo python setup.py install
```

Verify Tablestore SDK for Python To check the SDK version in the Python environment, enter python on the command line and then press Enter.

```
>>> import tablestore >>> tablestore.__version__ '5.1.0'
```

Uninstall Tablestore SDK for Python Use pip to uninstall Tablestore SDK for Python.

```python
sudo pip uninstall tablestore
```

##### 2.1.2.3 Initialization

OTSClient provides a series of methods for users to manage tables and perform read and write operations on one or more rows. Obtain an endpoint An endpoint is the domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following operations:
1. Log on to the Tablestore console.
2. Click the instance name to go to the Inst ance Management page.
On the Instance Details page, you can view the endpoints of the instance in Instance Access URL. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair (AccessKey ID and AccessKey secret) for signature authentication. After you obtain the AccessKey pair, you can perform the following operation to initialize an OTSClient instance by using an endpoint: API operation

```
    // Initialize the TableStoreClient instance.
    // endPoint indicates the endpoint that is used to access the Tablestore instance, wh
ich must start with https://. Example: https://instance.cn-hangzhou.ots.aliyun.com:80.
    // accessKeyId indicates the AccessKey ID that is used to access the Tablestore insta
nce. You can visit the official website or contact an administrator to obtain an AccessKe y ID.
    // accessKeySecret indicates the AccessKey secret that is used to access the Tablesto
re instance. You can visit the official website or contact an administrator to obtain an AccessKey secret.
    // instanceName indicates the name of the instance to access. You can create an insta
nce in the Tablestore console or contact an administrator to obtain the name of an existi ng instance. func NewClient(endPoint, instanceName, accessKeyId, accessKeySecret string, options ...Cl ientOption) *TableStoreClient
```

Examples

```
    client = NewClient("your_instance_endpoint", &nbsp;"your_instance_name", "your_user_i
d", "your_user_key")
```

HTTPS HTTPS is supported in Python 2.0.8 and later. OpenSSL 0.9.8j or later is required. We recommend that you use OpenSSL 1.0.2d. The Python 2.0.8 release package contains a certifi package that can be installed and used. To update the root certificate, download the latest root certificate from Root Certificate.

##### 2.1.2.4 Use the SDK

###### 2.1.2.4.1 Table-level operations

Tablestore SDK for Python provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable You can call this operation to create a table based on the specified table structure. Not e After the table is created, it takes several seconds to load the table. During this period, read and write operations on the table may fail. You can use applications to perform operations on the table data only after the table is loaded. You must specify the primary key when you create a table. A primary key contains one to four primary key columns. Each primary key column has a name and a data type. API operation

```python
       Description: You can call this operation to create a table based on the specified
table schema information.
        table_meta indicates an instance of the tablestore.metadata.TableMeta class. tabl
e_meta specifies the table name and primary key schema.
        For more information, see the documentation for the TableMeta class. After you cr
eate a table, it takes about several seconds to load the partitions in the table. You can perform operations on the table only after the partitions are loaded.
        table_options is an instance of the tablestore.metadata.TableOptions class. table
_options contains the time_to_live, max_version, and max_time_deviation parameters.
        reserved_throughput is an instance of the tablestore.metadata.ReservedThroughput
class. reserved_throughput specifies the reserved read throughput and reserved write thro ughput.
        Return value: none.
        def create_table(self, table_meta, reserved_throughput):
```

Examples Create a data table without creating an index table The following code provides an example on how to create a data table. The data table contains two primary key columns. In this example, time_to_live is set to 31536000 (one year), max_versions to 3, max_time_deviation to 86400 (one day), and reserved_throughput to (0,0).

```bash
# Create a schema for primary key columns, including the number, names, and types of th
e primary key columns.
# The first primary key column is named pk0 and requires an INTEGER value. The first pr
imary key column is also the partition key.
# The second primary key column is named pk1 and requires an INTEGER value. The data ty
pe is specified as INTEGER in this example. You can also set the data type to STRING or BINARY. schema_of_primary_key = [('pk0', 'INTEGER'), ('pk1', 'INTEGER')]
# Create a tableMeta instance based on the name of the data table and the schema of the
primary key columns. table_meta = TableMeta('SampleTable', schema_of_primary_key)
# Create a TableOptions instance. Set time_to_live to 31536000 to automatically delete
expired data, max_versions to 3, and max_time_deviation to 86,400 (one day). table_options = TableOptions(31536000, 3, 86400)
# Set the reserved read throughput and reserved write throughput to 0.
reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
# Call create_table of the client. If no exceptions occur, the data table is created. I
f an exception occurs, the data table fails to be created. try:
    ots_client.create_table(table_meta, table_options, reserved_throughput)
    print "create table succeeded"
# If the task fails, an exception is returned and handled.
except Exception:
    print "create table failed."
```

For the detailed sample code, visit CreateTable@GitHub. Create a data table and an index table whose index type is global secondary index

```
schema_of_primary_key = [('gid', 'INTEGER'), ('uid', 'STRING')] defined_columns = [('i', 'INTEGER'), ('bool', 'BOOLEAN'), ('d', 'DOUBLE'), ('s', 'STRIN G'), ('b', 'BINARY')] table_meta = TableMeta(table_name, schema_of_primary_key, defined_columns) table_option = TableOptions(-1, 1) reserved_throughput = ReservedThroughput(CapacityUnit(0, 0)) secondary_indexes = [
    SecondaryIndexMeta('index1', ['i', 's'], ['bool', 'b', 'd']),
```

`]`

```
client.create_table(table_meta, table_option, reserved_throughput, secondary_indexes)
```

Create a data table and an index table whose index type is local secondary index

```
schema_of_primary_key = [('gid', 'INTEGER'), ('uid', 'STRING')] defined_columns = [('i', 'INTEGER'), ('bool', 'BOOLEAN'), ('d', 'DOUBLE'), ('s', 'STRIN G'), ('b', 'BINARY')] table_meta = TableMeta(table_name, schema_of_primary_key, defined_columns) table_option = TableOptions(-1, 1) reserved_throughput = ReservedThroughput(CapacityUnit(0, 0)) secondary_indexes = [
    SecondaryIndexMeta('index1', ['gid', 's'], ['bool', 'b', 'd'],index_type= Secondary
IndexType.LOCAL_INDEX),
```

`]`

```
client.create_table(table_meta, table_option, reserved_throughput, secondary_indexes)
```

ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

```python
""" Description: You can call this operation to query all table names. Return value: the table name list. "table_list" indicates the table name list of the tuple type. Example: ('MyTable1', 'MyTa ble2'). """ def list_table(self):
```

Examples The following code provides an example on how to obtain the names of all tables in an instance.

```
    try:
        list_response = ots_client.list_table()
        print 'table list:'
        for table_name in list_response:
            print table_name
        print "list table succeeded"
    except Exception:
        print "list table failed."
```

For the detailed sample code, visit ListTable@GitHub. UpdateTable You can call this operation to update the maximum number of versions and the reserved read/write throughput of a table. API operation

```python
    """
        Description: You can call this method to update the attributes of a table. This m
ethod can modify only the reserved read/write throughput of a table.
        ``table_name`` specifies the name of the table.
        ``table_options`` is an instance of the ``tablestore.metadata.TableOptions`` clas
s. It contains the time_to_live, max_version, and max_time_deviation parameters.
        ``reserved_throughput`` is an instance of the ``ots2.metadata.ReservedThroughput`
` class. It specifies the reserved read throughput and reserved write throughput.
        Return value: the time when the reserved read throughput or reserved write throug
hput was raised or lowered most recently for this table and the number of times it was lo wered today.
        ``update_table_response`` indicates the update result. It is an instance of the o
ts2.metadata.UpdateTableResponse class.
        """
        def update_table(self, table_name, table_options, reserved_throughput):
```

Examples The following code provides an example on how to update the maximum number of versions of a table to five.

```bash
        # Set both the reserved read throughput and reserved write throughput to 0.
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
        # Create a TableOptions instance. Set time_to_live to 31536000 seconds (one year)
and delete expired data, max_version to 3, and max_time_deviation to 86400 seconds (one d ay).
        table_options = TableOptions(31536000, 5, 86400)
        try:
            # Call the operation to update the reserved read/write throughput of the tabl
```

`e.`

```bash
            ots_client.update_table('SampleTable', reserved_throughput)
            # If the task succeeds, no exception is returned.
            print "update table succeeded"
        except Exception:
            # If the task fails, an exception is returned and handled.
            print "update table failed"
```

For the detailed sample code, visit UpdateTable@GitHub. DescribeTable You can call this operation to query the structure information and reserved read/write throughput value of the specified table. API operation

```python
        """
        Description: You can call this method to obtain the description of a table.
        ``table_name`` specifies the name of the table.
        Return value: the description of the table.
        ``describe_table_response`` indicates the description of the table, which is an i
nstance of the ots2.metadata.DescribeTableResponse class.
        """
        def describe_table(self, table_name):
```

Examples The following code provides an example on how to obtain the description of a table.

```bash
    try:
        describe_response = ots_client.describe_table('myTable')
        # If no exception is returned, the description is obtained and the following info
rmation is displayed.
        print "describe table succeeded."
        print ('TableName: %s' % describe_response.table_meta.table_name)
        print ('PrimaryKey: %s' % describe_response.table_meta.schema_of_primary_key)
        print ('Reserved read throughput: %s' % describe_response.reserved_throughput_det
ails.capacity_unit.read)
        print ('Reserved write throughput: %s' % describe_response.reserved_throughput_de
tails.capacity_unit.write)
        print ('Last increase throughput time: %s' % describe_response.reserved_throughpu
t_details.last_increase_time)
        print ('Last decrease throughput time: %s' % describe_response.reserved_throughpu
t_details.last_decrease_time)
        print ('table options\'s time to live: %s' % describe_response.table_options.time
_to_live)
        print ('table options\'s max version: %s' % describe_response.table_options.max_v
ersion)
        print ('table options\'s max_time_deviation: %s' % describe_response.table_option
s.max_time_deviation)
    except Exception:
        # If the task fails, an exception is returned and handled.
        print "describe table failed."
```

For the detailed sample code, visit DescribeTable@GitHub. DeleteTable You can call this operation to delete a specified table from the current instance. API operation

```python
        """
        Description: You can call this method to delete a table based on the table name.
        ``table_name`` specifies the name of the table.
        Return value: none.
        """
        def delete_table(self, table_name):
```

Examples The following code provides an example on how to delete a table.

```bash
try:
    # Call the operation to delete the table named SampleTable.
    ots_client.delete_table('SampleTable')
    # If the task succeeds, no exception is returned.
    print "delete table succeeded"
    # If the task fails, an exception is returned and handled.
except Exception:
    print "delete table failed"
```

For the detailed sample code, visit DeleteTable@GitHub.

###### 2.1.2.4.2 Single-row operations

Tablestore SDK for Python provides the following single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can call this operation to insert a row of data. If this row already exists, it is overwritten. API operation

```python
        """
        Description: This operation writes a single row of data. Thu number of capacity u
nites (CUs) consumed by the operation is returned.
        table_name specifies the name of the table.
        row specifies the row you want to insert to the table, including a primary key an
d attribute columns.
        condition is an instance of the tablestore.metadata.Condition class. By specifyin
g conditions, the system checks whether the specified conditions are met before the syste m performs the operation. If the conditions are met, the operation is performed. This fun ction supports only row existence checks. Check conditions include IGNORE, EXPECT_EXIST, and EXPECT_NOT_EXIST.
        return_type specifies the data type to return. return_type is an instance of the
tablestore.metadata.ReturnType class. You can only use return_type to specify the type of primary key data to return. This parameter applies to auto-increment primary key columns.
        Response: the number of capacity units (CUs) consumed by this operation and the r
ow data to return.
        consumed is an instance of the tablestore.metadata.CapacityUnit class.  This para
meter indicates the number of CUs consumed by this operation.
        return_row indicates the row to return, including the primary key and attribute c
olumns.
        """
        def put_row(self, table_name, row, condition = None, return_type = None)
```

Examples The following code provides an example on how to insert a row of data: Not e RowExistenceExpectation.IGNORE indicates that a row of data is inserted regardless of whether the specified row exists or not. If the specified row exists, the existing data is overwritten. RowExistenceExpectation.EXPECT_EXIST indicates that a row of data is inserted only when the specified row exists. The existing data is overwritten. RowExistenceExpectation.EXPECT_NOT_EXIST indicates that a row of data is inserted only when the specified row does not exist. In the following example, the data version in the age attribute column is 1498184687000, which indicates June 23, 2017. If the current time minus max_time_deviation (specified during table creation) is greater than 1498184687000, PutRow is disabled.

```bash
    ## The first primary key column of the primary key is gid and its value is the intege
r 1. The second primary key column is uid and its value is the integer 101.
    primary_key = [('gid',1), ('uid',101)]
    ## Insert the following attribute columns:
    ##                        The name of the first attribute column is name and its valu
e is the string John. The version is not specified, so the current system time is used as the version.
    ##                        The name of the second attribute column is mobile and its v
alue is the integer 15100000000. The version is not specified, so the current system time is used as the version.
    ##                        The name of the third attribute column is address and its v
alue is the binary string China. The version is not specified, so the current system time is used as the version.
    ##                        The name of the fourth attribute column is age and its valu
e is 29.7. The version number is 1498184687.
    attribute_columns = [('name','John'), ('mobile',15100000000),('address', bytearray('C
hina')),('female', False), ('age', 29.7, 1498184687000)]
    ## Construct a row by using primary_key and attribute_columns.
    row = Row(primary_key, attribute_columns)
    # The condition for row check is that the expected row does not exist. If the specifi
ed row exists, the Condition Update Failed error occurs.
    condition = Condition(RowExistenceExpectation.EXPECT_NOT_EXIST)
    try :
        # If ReturnType is not specified when you call the put_row method, the value of r
eturn_row is None.
        consumed, return_row = client.put_row(table_name, row, condition)
        # The write CUs consumed by this request is displayed.
        print ('put row succeed, consume %s write cu.' % consumed.write)
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "put row failed, http_status:%d, error_message:%s" % (e.get_http_status(),
e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "put row failed, http_status:%d, error_code:%s, error_message:%s, request_i
d:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id ())
```

For the detailed code, visit PutRow@GitHub. GetRow You can call this opertaion to read a row of data. The following results of the read request may be returned: If the row exists, the primary key columns and attribute columns of the row are returned. If the row does not exist, no row is returned and no error is reported. API operation

```python
       """
        Description: This operation reads a single row of data.
        table_name specifies the name of the table.
        primary_key specifies the primary key. Type: list.
        columns_to_get is optional. This parameter specifies the columns to read. If you
do not specify this parameter, all columns are read. Type: list.
        column_filter is optional. This parameter specifies the filter conditions for col
umns. Only rows that meet the condition are returned.
        max_version is optional. This parameter specifies the maximum number of versions
that can be read. You must specify at least one of max_version and time_range.
        time_range is optional. This parameter specifies a range of versions to read or a
version of data to read. You must specify at least one of max_version and time_range.
        Response: the number of CUs consumed by this operation and the primary key column
s and attribute columns.
        consumed is an instance of the tablestore.metadata.CapacityUnit class. This param
eter indicates the number of CUs consumed by this operation.
        return_row indicates the row to return, including the primary key and attribute c
olumns. Type: list. Example: [('PK0',value0), ('PK1',value1)].
        next_token indicates the start column of a wide row to read next time. The data t
ype of the column is binary.
        """
        def get_row(self, table_name, primary_key, columns_to_get=None,
                column_filter=None, max_version=None, time_range=None,
                start_column=None, end_column=None, token=None):
```

Examples The following code provides an example on how to read a row of data:

```bash
    # The first primary key column of the primary key is uid and its value is the integer
1. The second primary key column is gid and its value is the integer 101.
    primary_key = [('uid',1), ('gid',101)]
    # The attribute columns to return are name, growth, and type. If the value of columns
_to_get is [], all attribute columns are returned.
    columns_to_get = ['name', 'growth', 'type']
    # Set filters for the columns. If the value in the growth column is not 0.9 and the v
alue in the name column is Hangzhou, this row is returned.
    cond = CompositeColumnCondition(LogicalOperator.AND)
    cond.add_sub_condition(SingleColumnCondition("growth", 0.9, ComparatorType.NOT_EQUAL)
```

`)`

```
    cond.add_sub_condition(SingleColumnCondition("name", 'Hangzhou', ComparatorType.EQUAL
```

`))`

```bash
    try:
        # If you set the value of the last parameter to 1 when you call the get_row opera
tion, only a version of data is returned in the response.
        consumed, return_row, next_token = client.get_row(table_name, primary_key, column
s_to_get, cond, 1)
        print ('Read succeed, consume %s read cu.' % consumed.read)
        print ('Value of primary key: %s' % return_row.primary_key)
        print ('Value of attribute: %s' % return_row.attribute_columns)
        for att in return_row.attribute_columns:
            # Display the key, value, and version of each column.
            print ('name:%s\tvalue:%s\ttimestamp:%d' % (att[0], att[1], att[2]))
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "get row failed, http_status:%d, error_message:%s" % (e.get_http_status(),
e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "get row failed, http_status:%d, error_code:%s, error_message:%s, request_i
d:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id ())
```

For the detailed code, visit GetRow@GitHub. UpdateRow You can call this operation to update data of a specified row. You can add or delete attribute columns of a row, delete a specified version of data from an attribute column, or update the existing data in an attribute column. If the row does not exist, a new row is added. Not e If the UpdateRow request only contains columns to delete, and the specified row does not exist, a new row is not added. API operation

```python
        """
        Description: This operation updates a single row of data.
        table_name specifies the name of the table.
        row specifies the row you want to delete, including a primary key and attribute c
olumns of the list type.
        condition is an instance of the tablestore.metadata.Condition class. By specifyin
g conditions, the system checks whether the specified conditions are met before the syste m performs the operation. If the conditions are met, the operation is performed. This fun ction supports row existence and column conditions checks. Check conditions for row inclu de IGNORE, EXPECT_EXIST, and EXPECT_NOT_EXIST.
        return_type specifies the data type to return. return_type is an instance of the
tablestore.metadata.ReturnType class. You can only use return_type to specify the type of primary key data to return. This parameter applies to auto-increment primary key columns.
        Response: the number of CUs consumed by this operation and the row data that is s
pecified by return_row to return.
        consumed is an instance of the tablestore.metadata.CapacityUnit class. This param
eter indicates the number of CUs consumed by this operation.
        return_row indicates the row to return.
        """
        def update_row(self, table_name, row, condition, return_type = None)
```

Examples The following code provides an example on how to update the data of a specified row:

```json
    # The first primary key column of the primary key is uid and its value is the integer
1. The second primary key column is gid and its value is the integer 101.
    primary_key = [('uid',1), ('gid',101)]
    # The update types include PUT, DELETE, and DELETE_ALL.
    # PUT: adds a value to the column or updates the existing value in the column. In the
example, two columns are added. The first column is name and its value is David. The seco nd column is address and its value is Hongkong.
    # DELETE: deletes a specified version (timestamp) of data. In this example, data of t
he 1488436949003 version in the address column is deleted.
    # DELETE_ALL: deletes the column. In the example, the date of all versions in the mob
ile and age columns are deleted.
    update_of_attribute_columns = {
        'PUT' : [('name','David'), ('address','Hongkong')],
        'DELETE' : [('address', None, 1488436949003)],
        'DELETE_ALL' : [('mobile'), ('age')],
    row = Row(primary_key, update_of_attribute_columns)
    # The condition for row check is that the row existence is ignored. No matter whether
the row exists, the row is updated.
    condition = Condition(RowExistenceExpectation.IGNORE, SingleColumnCondition("age", 20
, ComparatorType.EQUAL)) # update row only when this row is exist
    try:
        consumed, return_row = client.update_row(table_name, row, condition)
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "update row failed, http_status:%d, error_message:%s" % (e.get_http_status(
), e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "update row failed, http_status:%d, error_code:%s, error_message:%s, reques
t_id:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request _id())
```

For the detailed code, visit UpdateRow@GitHub. DeleteRow You can call this operation to delete a row of data. If the row to delete does not exist, no changes are made to the table. API operation

```python
        """
        Description: This operation deletes a single row of data.
        table_name specifies the name of the table.
        row specifies the row you want to delete, including only the primary key.
        condition is an instance of the tablestore.metadata.Condition class. By specifyin
g conditions, the system checks whether the specified conditions are met before the syste m performs the operation. If the conditions are met, the operation is performed. This fun ction supports row existence and column conditions checks. Check conditions for row inclu de IGNORE, EXPECT_EXIST, and EXPECT_NOT_EXIST.
        Response: the number of CUs consumed by this operation and the row data that is s
pecified by return_row to return.
        consumed is an instance of the tablestore.metadata.CapacityUnit class. This param
eter indicates the number of CUs consumed by this operation.
        return_row indicates the row to return.
        """
        def delete_row(self, table_name, row, condition, return_type = None):
```

Examples The following code provides an example on how to delete a row of data:

```bash
    primary_key = [('gid',1), ('uid','101')]
    row = Row(primary_key)
    try:
        consumed, return_row = client.delete_row(table_name, row, None)
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "update row failed, http_status:%d, error_message:%s" % (e.get_http_status(
), e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "update row failed, http_status:%d, error_code:%s, error_message:%s, reques
t_id:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request _id())
    print ('Delete succeed, consume %s write cu.' % consumed.write)
```

For the detailed sample code, visit DeleteRow@GitHub.

###### 2.1.2.4.3 Multi-row operations

Tablestore SDK for Python provides multi-row operations, such as BatchGetRow, BatchWriteRow, and GetRange. BatchGetRow You can call this operation to read several rows of data from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the response time for requests and increase the data read rate. API operation

```python
        """
        Description: This operation reads the specified rows of data.
        request = BatchGetRowRequest()
        request.add(TableInBatchGetRowItem(myTable0, primary_keys, column_to_get=None, co
lumn_filter=None))
        request.add(TableInBatchGetRowItem(myTable1, primary_keys, column_to_get=None, co
lumn_filter=None))
        request.add(TableInBatchGetRowItem(myTable2, primary_keys, column_to_get=None, co
lumn_filter=None))
        request.add(TableInBatchGetRowItem(myTable3, primary_keys, column_to_get=None, co
lumn_filter=None))
        response = client.batch_get_row(request)
        response: the response to the request. Type: tablestore.metadata.BatchGetRowRespo
nse
        """
        def batch_get_row(self, request):
```

Examples The following code provides an example on how to read three rows of data at a time:

```bash
    # Specify the columns to return.
    columns_to_get = ['name', 'mobile', 'address', 'age']
    # Read three rows of data.
    rows_to_get = []
    for i in range(0, 3):
        primary_key = [('gid',i), ('uid',i+1)]
        rows_to_get.append(primary_key)
    # Configure filtering conditions. Set name to John and address to China.
    cond = CompositeColumnCondition(LogicalOperator.AND)
    cond.add_sub_condition(SingleColumnCondition("name", "John", ComparatorType.EQUAL))
    cond.add_sub_condition(SingleColumnCondition("address", 'China', ComparatorType.EQUAL
```

`))`

```bash
    # Create a request to read multiple rows.
    request = BatchGetRowRequest()
    # Add rows to read from table_name. The 1 parameter specifies that the latest version
is read.
    request.add(TableInBatchGetRowItem(table_name, rows_to_get, columns_to_get, cond, 1))
    # Add rows to read from notExistTable.
    request.add(TableInBatchGetRowItem('notExistTable', rows_to_get, columns_to_get, cond
, 1))
    try:
           result = client.batch_get_row(request)
        print ('Result status: %s'%(result.is_all_succeed()))
        table_result_0 = result.get_result_by_table(table_name)
        table_result_1 = result.get_result_by_table('notExistTable')
        print ('Check first table\'s result:')
        for item in table_result_0:
            if item.is_ok:
                print ('Read succeed, PrimaryKey: %s, Attributes: %s' % (item.row.primary
_key, item.row.attribute_columns))
            else:
                print ('Read failed, error code: %s, error message: %s' % (item.error_cod
e, item.error_message))
        print ('Check second table\'s result:')
        for item in table_result_1:
            if item.is_ok:
                print ('Read succeed, PrimaryKey: %s, Attributes: %s' % (item.row.primary
_key, item.row.attribute_columns))
            else:
                print ('Read failed, error code: %s, error message: %s' % (item.error_cod
e, item.error_message))
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "get row failed, http_status:%d, error_message:%s" % (e.get_http_status(),
e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "get row failed, http_status:%d, error_code:%s, error_message:%s, request_i
d:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id ())
```

For the detailed sample code, visit BatchGetRow@GitHub. BatchWriteRow You can call this operation to insert, modify, or delete several rows of data in one or more tables. The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently. API operation

```python
        """
        Description: This operation writes data to multiple rows.
        request = MiltiTableInBatchWriteRowItem()
        request.add(TableInBatchWriteRowItem(table0, row_items))
        request.add(TableInBatchWriteRowItem(table1, row_items))
        response = client.batch_write_row(request)
        response indicates the returned result. Type: tablestore.metadata.BatchWriteRowRe
sponse.
        """
        def batch_write_row(self, request):
```

Examples The following code provides an example on how to write multiple rows of data.

```bash
    put_row_items = []
    # Add rows for PutRow.
    for i in range(0, 10):
        primary_key = [('gid',i), ('uid',i+1)]
        attribute_columns = [('name','somebody'+str(i)), ('address','somewhere'+str(i)),
('age',i)]
        row = Row(primary_key, attribute_columns)
        condition = Condition(RowExistenceExpectation.IGNORE)
        item = PutRowItem(row, condition)
        put_row_items.append(item)
    # Add rows for UpdateRow.
    for i in range(10, 20):
        primary_key = [('gid',i), ('uid',i+1)]
        attribute_columns = {'put': [('name','somebody'+str(i)), ('address','somewhere'+s
tr(i)), ('age',i)]}
        row = Row(primary_key, attribute_columns)
        condition = Condition(RowExistenceExpectation.IGNORE, SingleColumnCondition("age"
, i, ComparatorType.EQUAL))
        item = UpdateRowItem(row, condition)
        put_row_items.append(item)
    # Add rows for DeleteRow.
    delete_row_items = []
    for i in range(10, 20):
        primary_key = [('gid',i), ('uid',i+1)]
        row = Row(primary_key)
        condition = Condition(RowExistenceExpectation.IGNORE)
        item = DeleteRowItem(row, condition)
        delete_row_items.append(item)
    # Create a request to write multiple rows.
    request = BatchWriteRowRequest()
```

```bash
    request.add(TableInBatchWriteRowItem(table_name, put_row_items))
    request.add(TableInBatchWriteRowItem('notExistTable', delete_row_items))
    # When you call the batch_write_row method to write multiple rows, exceptions may occ
ur if errors such as request parameter errors occur. If the operation fails for some rows , an exception may not occur but the internal items may fail.
    try:
        result = client.batch_write_row(request)
        print ('Result status: %s'%(result.is_all_succeed()))
        # Check the result of inserting rows.
        print ('check first table\'s put results:')
        succ, fail = result.get_put()
        for item in succ:
            print ('Put succeed, consume %s write cu.' % item.consumed.write)
        for item in fail:
            print ('Put failed, error code: %s, error message: %s' % (item.error_code, it
em.error_message))
        # Check the result of updating rows.
        print ('check first table\'s update results:')
        succ, fail = result.get_update()
        for item in succ:
            print ('Update succeed, consume %s write cu.' % item.consumed.write)
        for item in fail:
            print ('Update failed, error code: %s, error message: %s' % (item.error_code,
item.error_message))
        # Check the result of deleting rows.
        print ('check second table\'s delete results:')
        succ, fail = result.get_delete()
        for item in succ:
            print ('Delete succeed, consume %s write cu.' % item.consumed.write)
        for item in fail:
            print ('Delete failed, error code: %s, error message: %s' % (item.error_code,
item.error_message))
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "get row failed, http_status:%d, error_message:%s" % (e.get_http_status(),
e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "get row failed, http_status:%d, error_code:%s, error_message:%s, request_i
d:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id ())
```

For the detailed sample code, visit BatchWriteRow@GitHub. GetRange You can call this operation to read data within the specified primary key range. API operation

```python
        """
        Description: This operation reads data from multiple rows within the specified ra
nge.
        table_name: the name of the table.
        direction: the order for this query. Data type: string. Valid values: FORWARD and
BACKWARD.
        inclusive_start_primary_key: the primary key column from which the read starts. I
f the specified row exists, the row is included in the response.
        exclusive_end_primary_key: the primary key column at which the read ends. The end
primary key column is excluded from the response even if the row exists.
        columns_to_get: optional. This parameter specifies the names of columns to read.
If you do not specify this parameter, all columns are read. Type: list.
        limit: optional. This parameter specifies the maximum number of rows to read. If
you do not specify this parameter, all rows are read.
        column_filter: optional. This parameter specifies the filter conditions for colum
ns. Only rows that meet the condition are returned.
        max_version: optional. This parameter specifies the maximum number of versions to
return. You must specify at least one of max_version and time_range.
        time_range: optional. This parameter specifies the range of versions from which d
ata is read. You must specify at least one of max_version and time_range.
        start_column: optional. This parameter specifies the column from which the read s
tarts, which is used to read wide rows.
        end_column: optional. This parameter specifies the column at which the read ends,
which is used to read wide rows.
        token: optional. This parameter specifies the start column of a wide row to read
next time. The value of this parameter is returned by the last read request, and encoded as binary data.
        Response: the results that meet the conditions.
        consumed: the number of CUs consumed by this operation. This parameter specifies
an instance of the tablestore.metadata.CapacityUnit class.
        next_start_primary_key indicates the primary key column from which you want to st
art the next get_range operation. Type: dict.
        row_list indicates the list of returned rows of data. Format: [Row, ...].
        """
   def get_range(self, table_name, direction,
                  inclusive_start_primary_key,
                  exclusive_end_primary_key,
                  columns_to_get=None,
                  limit=None,
                  column_filter=None,
                  max_version=None,
                  time_range=None,
                  start_column=None,
                  end_column=None,
                  token = None):
```

Examples The following code provides an example on how to read data within the specified range:

```bash
    # Specify the start primary key.
    inclusive_start_primary_key = [('uid',INF_MIN), ('gid',INF_MIN)]
    # Specify the end primary key.
exclusiveendprimarykey=[('uid',INFMAX),('gid',INFMAX)]
```

```bash
    exclusive_end_primary_key  [(uid,INF_MAX), (gid,INF_MAX)]
    # Query all columns.
    columns_to_get = []
    # Set limit to 90 to return a maximum of 90 rows of data. If a total of 100 rows are
to return, you can set limit to 90 in the first query. The next_start_primary_key value i s not None.
    limit = 90
    # Configure the filter conditions.
    cond = CompositeColumnCondition(LogicalOperator.AND)
    cond.add_sub_condition(SingleColumnCondition("address", 'China', ComparatorType.EQUAL
```

`))`

```bash
    cond.add_sub_condition(SingleColumnCondition("age", 50, ComparatorType.LESS_THAN))
    try:
        # Call the get_range operation.
        consumed, next_start_primary_key, row_list, next_token  = client.get_range(
                table_name, Direction.FORWARD,
                inclusive_start_primary_key, exclusive_end_primary_key,
                columns_to_get,
                limit,
                column_filter = cond,
                max_version = 1
                time_range = (1557125059000, 1557129059000) # The start_time value is equ
al to or greater than 1557125059000. The end_time value is smaller than 1557129059000.
```

`)`

```bash
        all_rows = []
        all_rows.extend(row_list)
        # If the next_start_primary_key value is not None, the read continues until all r
emaining data is read.
        while next_start_primary_key is not None:
            inclusive_start_primary_key = next_start_primary_key
            consumed, next_start_primary_key, row_list, next_token = client.get_range(
                table_name, Direction.FORWARD,
                inclusive_start_primary_key, exclusive_end_primary_key,
                columns_to_get, limit,
                column_filter = cond,
                max_version = 1
```

`)`

```bash
            all_rows.extend(row_list)
        # Display the primary key and attribute columns.
        for row in all_rows:
            print (row.primary_key, row.attribute_columns)
        print ('Total rows: ', len(all_rows))
    # Client exceptions are caused by parameter errors or network exceptions.
    except OTSClientError as e:
        print "get row failed, http_status:%d, error_message:%s" % (e.get_http_status(),
e.get_error_message())
    # Server exceptions are caused by parameter or throttling errors.
    except OTSServiceError as e:
        print "get row failed, http_status:%d, error_code:%s, error_message:%s, request_i
d:%s" % (e.get_http_status(), e.get_error_code(), e.get_error_message(), e.get_request_id ())
```

For the detailed sample code, visit GetRange@GitHub.

###### 2.1.2.4.4 Global secondary indexes

This topic describes how to create and delete a global secondary index. Create a global secondary index You can create a global secondary index when you create a table. You can also create a global secondary index for an existing table. The fields of a global secondary index must be specified in defined_columns when you create a table. Create a global secondary index when you create a table

```
schema_of_primary_key = [('gid', 'INTEGER'), ('uid', 'STRING')] defined_columns = [('i', 'INTEGER'), ('bool', 'BOOLEAN'), ('d', 'DOUBLE'), ('s', 'STRING' ), ('b', 'BINARY')] table_meta = TableMeta(table_name, schema_of_primary_key, defined_columns) table_option = TableOptions(-1, 1) reserved_throughput = ReservedThroughput(CapacityUnit(0, 0)) secondary_indexes = [
    SecondaryIndexMeta('index1', ['i', 's'], ['bool', 'b', 'd']),
```

`]`

```
client.create_table(table_meta, table_option, reserved_throughput, secondary_indexes)
```

Create a global secondary index for an existing table

```
index_meta = SecondaryIndexMeta('index2', ['i', 's'], ['bool', 'b', 'd']) client.create_secondary_index(table_name, index_meta)
```

Delete a global secondary index Delete an index table.

```
client.delete_secondary_index(table_name, 'index1')
```

##### 2.1.2.5 Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for Python. Methods Tablestore SDK for Python handles errors as exceptions. If the operation succeeds, the called operation does not return an exception. If the operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions Tablestore SDK for Python has two types of exceptions: OTSClientError and OTSServiceError. Both are inherited from Exception. OTSClientError: an internal SDK exception, such as an invalid parameter value or a failure to parse the results returned by the server. OTSServiceError: a server error that comes from the resolution of a server error message. OTSServiceError contains the following parameters: get_http_status: an HTTP status code, such as 200 and 404. get_error_code: an error type string returned by Tablestore. get_error_message: an error message string returned by Tablestore. get_request_id: the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help. Retry Tablestore SDK for Python automatically retries an operation when an error occurs. In the default retry policy, the maximum retry attempts is 20, and the maximum retry interval is 3,000 ms. For more information about the retry policies for throttling errors and internal server errors related to write operations, see tablestore/retry.py. You can also customize a retry policy by inheriting the RetryPolicy class, and configure the custom retry policy when you create an OTSClient object. Tablestore SDK for Python provides the following retry policies: DefaultRetryPolicy: the default retry policy. Only read operations are retried. The maximum retry attempts is 20, and the maximum retry interval is 3,000 ms. NoRetryPolicy: no operation is retried. NoDelayRetryPolicy: a retry policy without any delays. Exercise caution when you configure this policy. WriteRetryPolicy: the write operations are retried based on the default retry policy.

#### 2.1.3 Go SDK

##### 2.1.3.1 Preface

This topic describes how to install and use Tablestore SDK for Go. Prerequisites An authorized account is created, and an AccessKey pair (AccessKey ID and AccessKey secret) is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Unimanager Management Console, see Obtain an AccessKey pair. Download and install Tablestore SDK for Go For the download path of SDK for Go, visit SDK package (including package, source code and examples). For more information about how to install Tablestore SDK for Go, see Installation. Version Latest version: 5.0.2

##### 2.1.3.2 Installation

This topic describes how to install Tablestore SDK for Go. Preparations Go 1.4 or later is available. Installation methods Run the following command to install Tablestore SDK for Go:

```
    go get github.com/aliyun/aliyun-tablestore-go-sdk
```

##### 2.1.3.3 Initialization

TableStoreClient provides a series of methods for users to manage tables and perform read/write operations on a single row or multiple rows. Obtain an endpoint An endpoint is the domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following operations:
1. Log on to the Tablestore console.
2. Click the instance name to go to the Inst ance Management page.
On the Instance Details tab, you can view the endpoints of the instance in Instance Access URL. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair (AccessKey ID and AccessKey secret) for signature authentication. After you obtain the AccessKey pair, you can perform the following operation to initialize an OTSClient instance by using an endpoint: API operation

```
    // Initialize the TableStoreClient instance.
    // endPoint indicates the endpoint used to access the Tablestore instance, which must
start with https://. Example: https://instance.cn-hangzhou.ots.aliyun.com:80.
    // accessKeyId indicates the AccessKey ID used to access the Tablestore instance. You
can visit the official website or contact an administrator to obtain an AccessKey ID.
    // accessKeySecret indicates the AccessKey secret used to access the Tablestore insta
nce. You can visit the official website or contact an administrator to obtain an AccessKe y secret.
    // instanceName indicates the name of the instance to access. You can create an insta
nce in the Tablestore console or contact an administrator to obtain the name of an existi ng instance. func NewClient(endPoint, instanceName, accessKeyId, accessKeySecret string, options ...Cl ientOption) *TableStoreClient
```

Examples

```
    client = NewClient("your_instance_endpoint", &nbsp;"your_instance_name", "your_user_i
d", "your_user_key")
```

##### 2.1.3.4 Use the SDK

###### 2.1.3.4.1 Table-level operations

Tablestore SDK for Go provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable You can call this operation to create a table based on the specified table structure. Not e After a table is created, it takes several seconds to load the table. During this period, the read and write operations on the table may fail. You can use applications to perform operations on the table data only after the table is loaded. You must specify the primary key when you create a table. A primary key can contain one to four primary key columns. Each primary key column has a name and a data type. API operation

```
  // Create a table based on the specified table structure.
  // request is an instance of the CreateTableRequest class, which contains tablemeta, Ta
bleOption, and ReservedThroughput.
  // For more information, see the documentation of the TableMeta class.
  After you create a table, it takes several seconds to load the partitions in the table.
You can perform operations on the table only after the partitions are loaded.
  // Response: CreateTableResponse
        CreateTable(request *CreateTableRequest) (*CreateTableResponse, error)
```

Examples Create a data table without creating an index table The following sample code provides an example on how to create a data table that has two primary key columns and reserved read and write throughput of (0, 0):

```
func CreateTableSample(client *tablestore.TableStoreClient, tableName string) {
    createTableRequest := new(tablestore.CreateTableRequest)
    // Create a schema for primary key columns, which includes the number, names, and t
ypes of the primary key columns.
    // The first primary key column is named pk0 and requires an INTEGER value. The fir
st primary key column is also the partition key.
    // The second primary key column is named pk1 and requires an INTEGER value.
    tableMeta := new(tablestore.TableMeta)
    tableMeta.TableName = tableName
    tableMeta.AddPrimaryKeyColumn("pk0", tablestore.PrimaryKeyType_INTEGER)
    tableMeta.AddPrimaryKeyColumn("pk1", tablestore.PrimaryKeyType_STRING)
    tableOption := new(tablestore.TableOption)
    tableOption.TimeToAlive = -1
    tableOption.MaxVersion = 3
    reservedThroughput := new(tablestore.ReservedThroughput)
    reservedThroughput.Readcap = 0
    reservedThroughput.Writecap = 0
    createTableRequest.TableMeta = tableMeta
    createTableRequest.TableOption = tableOption
    createTableRequest.ReservedThroughput = reservedThroughput
    response, err := client.CreateTable(createTableRequest)
    if (err != nil) {
        fmt.Println("Failed to create table with error:", err)
    } else {
        fmt.Println("Create table finished")
```

For the detailed sample code, visit CreateTable@GitHub. Create a data table and an index table whose index type is global secondary index

```
func CreateTableWithGlobalIndexSample(client *tablestore.TableStoreClient, tableName st ring) {
    createTableRequest := new(tablestore.CreateTableRequest)
    tableMeta := new(tablestore.TableMeta)
    tableMeta.TableName = tableName
    tableMeta.AddPrimaryKeyColumn("pk1", tablestore.PrimaryKeyType_STRING)
    tableMeta.AddPrimaryKeyColumn("pk2", tablestore.PrimaryKeyType_INTEGER)
    tableMeta.AddDefinedColumn("definedcol1", tablestore.DefinedColumn_STRING)
    tableMeta.AddDefinedColumn("definedcol2", tablestore.DefinedColumn_INTEGER)
    indexMeta := new(tablestore.IndexMeta) // Create IndexMeta for the index table.
    indexMeta.AddPrimaryKeyColumn("definedcol1") // Add a primary key column to the ind
ex table. Specify the definedcol1 column of the data table as the primary key column of the index table.
    indexMeta.AddDefinedColumn("definedcol2") // Add an attribute column to the index t
able. Specify the definedcol2 column of the data table as the attribute column of the i ndex table.
    indexMeta.IndexName = "indexSample"
    tableOption := new(tablestore.TableOption)
    tableOption.TimeToAlive = -1 // Specify the validity period of data. A value of -1
specifies that the data never expires. Unit: seconds. You must set TimeToAlive to -1 fo r a data table that has index tables.
    tableOption.MaxVersion = 1 // Specify the maximum number of versions that can be re
tained for each column. A value of 1 specifies that only the latest version is retained for each column. You must set MaxVersion to 1 for a data table that has index tables.
    reservedThroughput := new(tablestore.ReservedThroughput)
    createTableRequest.TableMeta = tableMeta
    createTableRequest.TableOption = tableOption
    createTableRequest.ReservedThroughput = reservedThroughput
    createTableRequest.AddIndexMeta(indexMeta)
    _, err := client.CreateTable(createTableRequest)
    if err != nil {
        fmt.Println("Failed to create table with error:", err)
    } else {
        fmt.Println("Create table finished")
```

Create a data table and an index table whose index type is local secondary index

```
func CreateTableWithLocalIndexSample(client *tablestore.TableStoreClient, tableName str ing) {
    createTableRequest := new(tablestore.CreateTableRequest)
    tableMeta := new(tablestore.TableMeta)
    tableMeta.TableName = tableName
    tableMeta.AddPrimaryKeyColumn("pk1", tablestore.PrimaryKeyType_STRING)
    tableMeta.AddPrimaryKeyColumn("pk2", tablestore.PrimaryKeyType_INTEGER)
    tableMeta.AddDefinedColumn("definedcol1", tablestore.DefinedColumn_STRING)
    tableMeta.AddDefinedColumn("definedcol2", tablestore.DefinedColumn_INTEGER)
    indexMeta := new(tablestore.IndexMeta) // Create IndexMeta for the index table.
    indexMeta.IndexType = IT_LOCAL_INDEX // Set the index type to IT_LOCAL_INDEX.
    indexMeta.AddPrimaryKeyColumn("pk1") // Add a primary key column to the index table
. The first primary key column of the index table must be the same as the first primary key column of the data table.
    indexMeta.AddPrimaryKeyColumn("definedcol1") // Add a primary key column to the ind
ex table. Specify the definedcol1 column of the data table as the primary key column of the index table.
    indexMeta.AddDefinedColumn("definedcol2") // Add an attribute column to the index t
able. Specify the definedcol2 column of the data table as the attribute column of the i ndex table.
    indexMeta.IndexName = "indexSample"
    tableOption := new(tablestore.TableOption)
    tableOption.TimeToAlive = -1 // Specify the validity period of data. A value of -1
specifies that the data never expires. Unit: seconds. You must set TimeToAlive to -1 fo r a data table that has index tables.
    tableOption.MaxVersion = 1 // Specify the maximum number of versions that can be re
tained for each column. A value of 1 specifies that only the latest version is retained for each column. You must set MaxVersion to 1 for a data table that has index tables.
    reservedThroughput := new(tablestore.ReservedThroughput)
    createTableRequest.TableMeta = tableMeta
    createTableRequest.TableOption = tableOption
    createTableRequest.ReservedThroughput = reservedThroughput
    createTableRequest.AddIndexMeta(indexMeta)
    _, err := client.CreateTable(createTableRequest)
    if err != nil {
        fmt.Println("Failed to create table with error:", err)
    } else {
        fmt.Println("Create table finished")
```

ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

```
// List all tables. If the operation succeeds, names of all tables are returned. ListTable() (*ListTableResponse, error)
```

Examples The following code provides an example of how to obtain the names of all tables in an instance.

```
tables, err := client.ListTable() if err != nil {
    fmt.Println("Failed to list table")
} else {
    fmt.Println("List table result is")
    for _, table := range (tables.TableNames) {
        fmt.Println("TableName: ", table)
```

For the detailed sample code, visit ListTable@GitHub. UpdateTable You can use the UpdateTable API to update the reserved read/write throughput settings of the specified table. API operation

```
// Update the configurations of tableoptions and reservedthroughput for a table. UpdateTable(request *UpdateTableRequest) (*UpdateTableResponse, error)
```

Examples The following code provides an example on how to update the setting of MaxVersion of a table to 5:

```
updateTableReq := new(tablestore.UpdateTableRequest) updateTableReq.TableName = tableName updateTableReq.TableOption = new(tablestore.TableOption) updateTableReq.TableOption.TimeToAlive = -1 updateTableReq.TableOption.MaxVersion = 5 _, err := client.UpdateTable(updateTableReq) if (err != nil) {
    fmt.Println("failed to update table with error:", err)
} else {
    fmt.Println("update finished")
```

For the detailed sample code, visit UpdateTable@GitHub. DescribeTable You can call this operation to query the structure information and the reserved read/write throughput settings of a table. API operation

```
// Query the description of a table by using the table name. DescribeTable(request *DescribeTableRequest) (*DescribeTableResponse, error)
```

Examples The following code provides an example on how to obtain the description of a table:

```
describeTableReq := new(tablestore.DescribeTableRequest) describeTableReq.TableName = tableName describ, err := client.DescribeTable(describeTableReq) if err != nil {
    fmt.Println("failed to update table with error:", err)
} else {
    fmt.Println("DescribeTableSample finished. Table meta:", describ.TableOption.MaxVersi
on, describ.TableOption.TimeToAlive)
```

For the detailed sample code, visit DescribeTable@GitHub. DeleteTable You can call this operation to delete a specified table from the current instance. API operation

```
DeleteTable(request *DeleteTableRequest) (*DeleteTableResponse, error)
```

Examples The following code provides an example on how to delete a table:

```
deleteReq := new(tablestore.DeleteTableRequest) deleteReq.TableName = tableName _, err := client.DeleteTable(deleteReq) if (err != nil) {
    fmt.Println("Failed to delete table with error:", err)
} else {
    fmt.Println("Delete table finished")
```

For the detailed sample code, visit DeleteTable@GitHub.

###### 2.1.3.4.2 Single-row operations

Tablestore SDK for Go provides the following single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can call this operation to insert data into a specified row. API operation

```
    // @param PutRowRequest    Encapsulate the parameters required to perform the PutRow
operation.
    // @return PutRowResponse
    PutRow(request *PutRowRequest) (*PutRowResponse, error)
```

Examples The following code provides an example on how to insert a row of data: Not e RowExistenceExpectation.IGNORE indicates that new data is inserted into a row despite whether the specified row exists or not. If the specified row exists, the existing data is overwritten. RowExistenceExpectation.EXPECT_EXIST indicates that new data is inserted only when the specified row exists. The existing data is overwritten. RowExistenceExpectation.EXPECT_NOT_EXIST indicates that data is inserted only when the specified row does not exist.

```
    putRowRequest := new(tablestore.PutRowRequest)
    putRowChange := new(tablestore.PutRowChange)
    putRowChange.TableName = tableName
    putPk := new(tablestore.PrimaryKey)
    putPk.AddPrimaryKeyColumn("pk1", "pk1value1")
    putPk.AddPrimaryKeyColumn("pk2", int64(2))
    putPk.AddPrimaryKeyColumn("pk3", []byte("pk3"))
    putRowChange.PrimaryKey = putPk
    putRowChange.AddColumn("col1", "col1data1")
    putRowChange.AddColumn("col2", int64(3))
    putRowChange.AddColumn("col3", []byte("test"))
    putRowChange.SetCondition(tablestore.RowExistenceExpectation_IGNORE)
    putRowRequest.PutRowChange = putRowChange
    _, err := client.PutRow(putRowRequest)
    if err != nil {
        fmt.Println("putrow failed with error:", err)
    } else {
        fmt.Println("putrow finished")
```

For the detailed sample code, visit PutRow@GitHub. GetRow You can call this operation to read a single row of data based on a specified primary key.

```
    //Return a row of data from a table.
```

`//`

```
    // @param GetRowRequest             Encapsulate the parameters required to perform th
e GetRow operation.
    // @return  GetRowResponse          The content of the response to the GetRow operati
on.
    GetRow(request *GetRowRequest) (*GetRowResponse, error)
```

Examples The following code provides an example on how to read a row of data:

```
getRowRequest := new(tablestore.GetRowRequest)
    criteria := new(tablestore.SingleRowQueryCriteria);
    putPk := new(tablestore.PrimaryKey)
    putPk.AddPrimaryKeyColumn("pk1", "pk1value1")
    putPk.AddPrimaryKeyColumn("pk2", int64(2))
    putPk.AddPrimaryKeyColumn("pk3", []byte("pk3"))
    criteria.PrimaryKey = putPk
    getRowRequest.SingleRowQueryCriteria = criteria
    getRowRequest.SingleRowQueryCriteria.TableName = tableName
    getRowRequest.SingleRowQueryCriteria.MaxVersion = 1
    getResp, err := client.GetRow(getRowRequest)
    if err != nil {
        fmt.Println("getrow failed with error:", err)
    } else {
        fmt.Println("get row col0 result is ", getResp.Columns[0].ColumnName, getResp.Col
umns[0].Value)
```

For the detailed sample code, visit GetRow@GitHub. UpdateRow You can call this operation to update the data of a specified row. If the row does not exist, a new row is added. If the row exists, the values of the specified columns are added, modified, or deleted based on the request content. API operation

```
    // Update a row of data in a table.
    // @param UpdateRowRequest      Encapsulate the parameters required to perform the Up
dateRow operation.
    // @return UpdateRowResponse    The content of the response to the UpdateRow operatio
```

`n.`

```
    UpdateRow(request *UpdateRowRequest) (*UpdateRowResponse, error)
```

Examples The following code provides an example on how to update the data of a specified row:

```
    updateRowRequest := new(tablestore.UpdateRowRequest)
    updateRowChange := new(tablestore.UpdateRowChange)
    updateRowChange.TableName = tableName
    updatePk := new(tablestore.PrimaryKey)
    updatePk.AddPrimaryKeyColumn("pk1", "pk1value1")
    updatePk.AddPrimaryKeyColumn("pk2", int64(2))
    updatePk.AddPrimaryKeyColumn("pk3", []byte("pk3"))
    updateRowChange.PrimaryKey = updatePk
    updateRowChange.DeleteColumn("col1")
    updateRowChange.PutColumn("col2", int64(77))
    updateRowChange.PutColumn("col4", "newcol3")
    updateRowChange.SetCondition(tablestore.RowExistenceExpectation_EXPECT_EXIST)
    updateRowRequest.UpdateRowChange = updateRowChange
    _, err := client.UpdateRow(updateRowRequest)
    if err != nil {
        fmt.Println("update failed with error:", err)
    } else {
        fmt.Println("update row finished")
```

For the detailed sample code, visit UpdateRow@GitHub. DeleteRow You can call this operation to delete data you no longer need. API operation

```
    // Delete a row of data from a table.
    // @param DeleteRowRequest           Encapsulate the parameters required to perform t
he DeleteRow operation.
    // @return DeleteRowResponse         The content of the response to the DeleteRow ope
ration.
    DeleteRow(request *DeleteRowRequest) (*DeleteRowResponse, error)
```

Examples The following code provides an example on how to delete a row of data:

```
    deleteRowReq := new(tablestore.DeleteRowRequest)
    deleteRowReq.DeleteRowChange = new(tablestore.DeleteRowChange)
    deleteRowReq.DeleteRowChange.TableName = tableName
    deletePk := new(tablestore.PrimaryKey)
    deletePk.AddPrimaryKeyColumn("pk1", "pk1value1")
    deletePk.AddPrimaryKeyColumn("pk2", int64(2))
    deletePk.AddPrimaryKeyColumn("pk3", []byte("pk3"))
    deleteRowReq.DeleteRowChange.PrimaryKey = deletePk
    deleteRowReq.DeleteRowChange.SetCondition(tablestore.RowExistenceExpectation_EXPECT_E
XIST)
    clCondition1 := tablestore.NewSingleColumnCondition("col2", tablestore.CT_EQUAL, int6
4(3))
    deleteRowReq.DeleteRowChange.SetColumnCondition(clCondition1)
    _, err := client.DeleteRow(deleteRowReq)
    if err != nil {
        fmt.Println("delete failed with error:", err)
    } else {
        fmt.Println("delete row finished")
```

For the detailed sample code, visit DeleteRow@GitHub.

###### 2.1.3.4.3 Multi-row operations

Tablestore SDK for Go provides multi-row operations such as BatchGetRow, BatchWriteRow, GetRange, and GetByIterator. BatchGetRow You can call this operation to simultaneously read multiple rows of data from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the response time for requests and increase the data read rate. API operation

```
    // Return multiple rows of data from a table.
```

`//`

```
    // @param BatchGetRowRequest             Encapsulate the parameters required to perfo
rm the BatchGetRow operation.
    // @return  BatchGetRowResponse          The content of the response to the BatchGetR
ow operation.
    BatchGetRow(request *BatchGetRowRequest) (*BatchGetRowResponse, error)
```

Examples The following code provides an example on how to read 10 rows of data at a time: Not e You can use conditional statements to filter the returned results of BatchWriteRow operations.

```
batchGetReq := &tablestore.BatchGetRowRequest{} mqCriteria := &tablestore.MultiRowQueryCriteria{} for i := 0; i < 10; i++ {
    pkToGet := new(tablestore.PrimaryKey)
    pkToGet.AddPrimaryKeyColumn("pk1", "pk1value1")
    pkToGet.AddPrimaryKeyColumn("pk2", int64(i))
    pkToGet.AddPrimaryKeyColumn("pk3", []byte("pk3"))
    mqCriteria.AddRow(pkToGet)
    mqCriteria.MaxVersion = 1
mqCriteria.TableName = tableName batchGetReq.MultiRowQueryCriteria = append(batchGetReq.MultiRowQueryCriteria, mqCriteria) batchGetResponse, err := client.BatchGetRow(batchGetReq) if err != nil {
    fmt.Println("batachget failed with error:", err)
} else {
    fmt.Println("batchget finished")
```

For the detailed sample code, visit BatchGetRow@GitHub. BatchWriteRow You can call this operation to simultaneously insert, modify, or delete multiple rows of data in one or more tables. The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently. API operation

```
    // Add, delete, or modify multiple rows of data in multiple tables.
```

`//`

```
    // @param BatchWriteRowRequest             Encapsulate the parameters required to per
form the BatchWriteRow operation.
    // @return  BatchWriteRowResponse          The content of the response to the BatchWr
iteRow operation.
    BatchWriteRow(request *BatchWriteRowRequest) (*BatchWriteRowResponse,error)
```

Examples The following code provides an example on how to write 100 rows of data: Not e You can use conditional statements to filter the returned results of BatchWriteRow operations.

```
    batchWriteReq := &tablestore.BatchWriteRowRequest{}
    for i := 0; i < 100; i++ {
        putRowChange := new(tablestore.PutRowChange)
        putRowChange.TableName = tableName
        putPk := new(tablestore.PrimaryKey)
        putPk.AddPrimaryKeyColumn("pk1", "pk1value1")
        putPk.AddPrimaryKeyColumn("pk2", int64(i))
        putPk.AddPrimaryKeyColumn("pk3", []byte("pk3"))
        putRowChange.PrimaryKey = putPk
        putRowChange.AddColumn("col1", "fixvalue")
        putRowChange.SetCondition(tablestore.RowExistenceExpectation_IGNORE)
        batchWriteReq.AddRowChange(putRowChange)
    response, err := client.BatchWriteRow(batchWriteReq)
    if err != nil {
        fmt.Println("batch request failed with:", response)
    } else {
        fmt.Println("batch write row finished")
```

For the detailed sample code, visit BatchWriteRow@GitHub. GetRange You can call this operation to read data within a specified primary key range. API operation

```
    // Query multiple rows of data within a specified range in a table.
```

`//`

```
    // @param GetRangeRequest            Encapsulate the parameters required to perform t
he GetRange operation.
    // @return GetRangeResponse          The content of the response to the GetRange oper
ation.
    GetRange(request *GetRangeRequest) (*GetRangeResponse,error)
```

Examples The following code provides an example on how to read data within a specified range: Not e You can use conditional statements to filter the returned results of GetRange operations. Note that the data may be paged when you perform the GetRange operation.

```
getRangeRequest := &tablestore.GetRangeRequest{}
    rangeRowQueryCriteria := &tablestore.RangeRowQueryCriteria{}
    rangeRowQueryCriteria.TableName = tableName
    startPK := new(tablestore.PrimaryKey)
    startPK.AddPrimaryKeyColumnWithMinValue("pk1")
    startPK.AddPrimaryKeyColumnWithMinValue("pk2")
    startPK.AddPrimaryKeyColumnWithMinValue("pk3")
    endPK := new(tablestore.PrimaryKey)
    endPK.AddPrimaryKeyColumnWithMaxValue("pk1")
    endPK.AddPrimaryKeyColumnWithMaxValue("pk2")
    endPK.AddPrimaryKeyColumnWithMaxValue("pk3")
    rangeRowQueryCriteria.StartPrimaryKey = startPK
    rangeRowQueryCriteria.EndPrimaryKey = endPK
    rangeRowQueryCriteria.Direction = tablestore.FORWARD
    rangeRowQueryCriteria.MaxVersion = 1
    rangeRowQueryCriteria.Limit = 10
    getRangeRequest.RangeRowQueryCriteria = rangeRowQueryCriteria
    getRangeResp, err := client.GetRange(getRangeRequest)
    fmt.Println("get range result is " ,getRangeResp)
    for {
        if err != nil {
            fmt.Println("get range failed with error:", err)
        for _, row := range getRangeResp.Rows {
            fmt.Println("range get row with key", row.PrimaryKey.PrimaryKeys[0].Value, ro
w.PrimaryKey.PrimaryKeys[1].Value, row.PrimaryKey.PrimaryKeys[2].Value)
        if getRangeResp.NextStartPrimaryKey == nil {
            break
        } else {
            fmt.Println("next pk is :", getRangeResp.NextStartPrimaryKey.PrimaryKeys[0].V
alue, getRangeResp.NextStartPrimaryKey.PrimaryKeys[1].Value, getRangeResp.NextStartPrimar yKey.PrimaryKeys[2].Value)
            getRangeRequest.RangeRowQueryCriteria.StartPrimaryKey = getRangeResp.NextStar
tPrimaryKey
            getRangeResp, err = client.GetRange(getRangeRequest)
        fmt.Println("continue to query rows")
    fmt.Println("putrow finished")
```

For the detailed sample code, visit GetRange@GitHub.

#### 2.1.4 NodeJS SDK

##### 2.1.4.1 Preface

This topic describes how to use Tablestore SDK for Node.js. The content in this topic applies to Tablestore SDK for Node.js V4.x.x. Prerequisites An authorized account is created, and an AccessKey pair (AccessKey ID and AccessKey secret) is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Unimanager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for Node.js SDK package GitHub Version Latest version: V4.1.0.

##### 2.1.4.2 Installation

This topic describes how to install Tablestore SDK for Node.js. Preparations Node.js 4.0 or later is installed. Not e We recommend that you do not use Node.js later than 12.0 and earlier than 12.14 to avoid compatibility problems. Install Tablestore SDK for Node.js Run the following command to install Tablestore SDK for Node.js:

```
npm install tablestore
```

Not e If you encounter any network problems when you use npm, you can use the npm image provided by Taobao. Sample programs Tablestore SDK for Node.js provides a variety of sample programs for your reference and use. You can obtain the sample programs by using one of the following methods: Download and decompress the Tablestore SDK for Node.js package. Find the sample programs in the examples folder. Access Tablestore SDK for Node.js on GitHub.

##### 2.1.4.3 Initialization

TableStore.Client is the client for Tablestore. It provides a series of methods for you to perform operations on individual rows, multiple rows, or entire tables. Obtain an endpoint An endpoint is the domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following operations:
1. Log on to the Tablestore console.
2. Click the instance name to go to the Inst ance Management page.
On the Instance Details tab, you can view the endpoints of the instance in Instance Access URL. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair (AccessKey ID and AccessKey secret) for signature authentication. After you obtain the AccessKey pair, you can perform the following operation to initialize a Tablestore instance by using an endpoint:

```
var client = new TableStore.Client({ accessKeyId: '<your access key id>', accessKeySecret: '<your access key secret>', endpoint: '<your endpoint>', instancename: '<your instance name>', maxRetries:20,// The default number of retry attempts is 20. You can ignore this parameter.
    });
```

##### 2.1.4.4 Data types

Tablestore supports five data types. This topic describes how each of these data types corresponds to those supported in Tablestore SDK for Node.js.

| Data type in Tablestore | Data type in SDK for Node.js | Description |
|---|---|---|
| String | string | The basic data type in JavaScript. |
| Integer | int64 | The type of data encapsulated by Node.js SDK. |
| Double | number | The basic data type in JavaScript. |
| Boolean | boolean | The basic data type in JavaScript. |
| Binary | Buffer | The Buffer object of Node.js. |

The integer data in Tablestore is a 64-bit signed integer, which does not have a corresponding data type in JavaScript. Therefore, a data type that can indicate a 64-bit signed integer is required for Node.js. The following code provides an example on how to convert the integer data type of Tablestore:

```
var numberA = TableStore.Long.fromNumber(1000); var numberB = TableStore.Long.fromString('2000'); var num = numberA.toNumber();
    num = numberA.toString();
var str = numberB.toNumber();
    str = numberB.toString();
```

##### 2.1.4.5 Use the SDK

###### 2.1.4.5.1 Table-level operations

Tablestore SDK for Node.js provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable You can call this operation to create a table based on the specified table structure. Not e After the table is created, it can take several seconds to load the table. During this period, the read and write operations on the table may fail. You can use applications to perform operations on the table data only after the table is loaded. You must specify the primary key when you create a table. A primary key can contain one to four primary key columns. Each primary key column has a name and a data type. API operation

```
  /**
   * Create a table based on the specified table structure.
```

`*/`

```
  createTable(params, callback)
```

Examples Create a data table without creating an index table The following code provides an example on how to create a data table that has two primary key columns and reserved read and write throughput of (0, 0):

```
var client = require('./client'); var params = {
  tableMeta: {
    tableName: 'sampleTable',
    primaryKey: [
```

`{`

```
        name: 'gid',
        type: 'INTEGER'
```

`},` `{`

```
        name: 'uid',
        type: 'INTEGER'
```

`]` `},`

```
  reservedThroughput: {
    capacityUnit: {
      read: 0,
      write: 0
```

`},`

```
  tableOptions: {
    timeToLive: -1, // Specify the validity period of data. A value of -1 specifies tha
t the data never expires. Unit: seconds. If you set the validity period to a year, the value of timeToLive is 31,536,000 (365 × 24 × 3600).
    maxVersions: 1  // Specify the maximum number of versions that can be retained for
each column. A value of 1 specifies that only the latest version is retained for each c olumn.
```

};

```
client.createTable(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  console.log('success:', data);
});
```

For the detailed sample code, visit CreateTable@GitHub. Create a data table and an index table whose index type is global secondary index

```
var client = require('./client'); var TableStore = require('../index.js'); var params = {
  tableMeta: {
    tableName: 'sdkGlobalTest',
    primaryKey: [
```

`{`

```
        name: 'pk1',
        type: TableStore.PrimaryKeyType.INTEGER
```

`},` `{`

```
name:'pk2',
```

```
        name: pk2,
        type: TableStore.PrimaryKeyType.INTEGER
```

`],`

```
    definedColumn: [
```

`{`

```json
        "name": "col1",
        "type": TableStore.DefinedColumnType.DCT_INTEGER
```

`},` `{`

```json
        "name": "col2",
        "type": TableStore.DefinedColumnType.DCT_INTEGER
```

`],` `},`

```
  reservedThroughput: {
    capacityUnit: {
      read: 0,
      write: 0
```

`},`

```
  tableOptions: {
    timeToLive: -1, // Specify the validity period of data. A value of -1 specifies tha
t the data never expires. Unit: seconds. You must set timeToLive to -1 for a data table that has index tables.
    maxVersions: 1  // Specify the maximum number of versions that can be retained for
each column. A value of 1 specifies that only the latest version is retained for each c olumn. You must set maxVersions to 1 for a data table that has index tables.
```

`},`

```
  streamSpecification: {
    enableStream: false,// The stream feature cannot be enabled for secondary indexes.
```

`},`

```
  indexMetas: [
```

`{`

```
      name: "sdkGlobalIndex1",
      primaryKey: ["pk2"],
      definedColumn: ["col1", "col2"]
```

`},` `{`

```
      name: "sdkGlobalIndex2",
      primaryKey: ["col1"],
      definedColumn: ["col2"]
```

`]` };

```
client.createTable(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  console.log('success:', data);
});
```

Create a data table and an index table whose index type is local secondary index `/`

```
var client = require('./client'); var TableStore = require('../index.js'); var params = {
  tableMeta: {
    tableName: 'sdkLocalTest',
    primaryKey: [
```

`{`

```
        name: 'pk1',
        type: TableStore.PrimaryKeyType.INTEGER
```

`},` `{`

```
        name: 'pk2',
        type: TableStore.PrimaryKeyType.INTEGER
```

`],`

```
    definedColumn: [
```

`{`

```json
        "name": "col1",
        "type": TableStore.DefinedColumnType.DCT_INTEGER
```

`},` `{`

```json
        "name": "col2",
        "type": TableStore.DefinedColumnType.DCT_INTEGER
```

`],` `},`

```
  reservedThroughput: {
    capacityUnit: {
      read: 0,
      write: 0
```

`},`

```
  tableOptions: {
    timeToLive: -1, // Specify the validity period of data. A value of -1 specifies tha
t the data never expires. Unit: seconds. You must set timeToLive to -1 for a data table that has index tables.
    maxVersions: 1  // Specify the maximum number of versions that can be retained for
each column. A value of 1 specifies that only the latest version is retained for each c olumn. You must set maxVersions to 1 for a data table that has index tables.
```

`},`

```
  streamSpecification: {
    enableStream: false,// The stream feature cannot be enabled for secondary indexes.
```

`},`

```
  indexMetas: [
```

`{`

```
      name: "sdklocalIndex1",
      primaryKey: ["pk1","col1"],// Add primary key columns to the index table. The fir
st primary key column of the index table must be the same as the first primary key colu mn of the data table.
      definedColumn: ["col2"],
      indexUpdateMode: TableStore.IndexUpdateMode.IUM_SYNC_INDEX,// Set the index updat
e mode to IUM_SYNC_INDEX, which specifies the synchronous update mode. If the index typ e is set to IT_LOCAL_INDEX, the index update mode must be set to IUM_SYNC_INDEX.
      indexType: TableStore.IndexType.IT_LOCAL_INDEX,// Set the index type to IT_LOCAL_
INDEX whichspecifiesalocalsecondaryindex
```

```
INDEX, which specifies a local secondary index.
```

`},` `{`

```
      name: "sdklocalIndex2",
      primaryKey: ["pk1","col2"],
      definedColumn: ["col1"],
      indexUpdateMode: TableStore.IndexUpdateMode.IUM_SYNC_INDEX,// Set the index updat
e mode to IUM_SYNC_INDEX, which specifies the synchronous update mode. If the index typ e is set to IT_LOCAL_INDEX, the index update mode must be set to IUM_SYNC_INDEX.
      indexType: TableStore.IndexType.IT_LOCAL_INDEX,// Set the index type to IT_LOCAL_
INDEX, which specifies a local secondary index.
```

`]` };

```
client.createTable(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  console.log('success:', data);
});
```

ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

```
  /**
   * Obtain the names of all tables in the current instance.
```

`*/`

```
  listTable(params, callback)
```

Examples The following code provides an example on how to obtain the names of all tables in the current instance:

```
var client = require('./client'); client.listTable({}, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit ListTable@GitHub. UpdateTable You can call this operation to update the maximum number of versions and reserved read/write throughput of a table. API operation

```
  /**
   * Update the reserved read/write throughput of a specified table.
```

`*/`

```
  updateTable(params, callback)
```

Examples Set the maximum number of versions of a table to 5.

```
var client = require('./client'); var params = {
    tableName: 'sampleTable',
    tableOptions: {
        maxVersions: 5,
```

};

```
client.updateTable(params, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit UpdateTable@GitHub. DescribeTable You can call this operation to query the structure information and the reserved read/write throughput settings of a table. API operation

```
  /**
   * Query the structure information and the reserved read/write throughput of the specif
ied table.
```

`*/`

```
  describeTable(params, callback)
```

Examples The following code provides an example on how to obtain the description of a table:

```
var client = require('./client'); var params = {
    tableName: 'sampleTable'
```

};

```
client.describeTable(params, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit DescribeTable@GitHub. DeleteTable You can call this operation to delete a specified table from the current instance. API operation

```
  /**
   * Delete a specified table from the current instance.
```

`*/`

```
  deleteTable(params, callback)
```

Examples The following code provides an example on how to delete a specified table from the current instance:

```
var client = require('./client'); var params = {
    tableName: 'sampleTable'
```

};

```
client.deleteTable(params, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit DeleteTable@GitHub.

###### 2.1.4.5.2 Single-row operations

Tablestore SDK for Node.js provides the following single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can call this operation to insert data into a specified row. API operation

```
  /**
   * Insert data into a specified row. If the row exists, the existing data is overwritte
n. Otherwise, a new row is added.
```

`*/`

```
  putRow(params, callback)
```

Examples Not e RowExistenceExpectation.IGNORE indicates that new data is inserted into a row despite whether the specified row exists or not. If the specified row exists, the existing data is overwritten. RowExistenceExpectation.EXPECT_EXIST indicates that new data is inserted only when the specified row exists. The existing data is overwritten. RowExistenceExpectation.EXPECT_NOT_EXIST indicates that data is inserted only when the specified row does not exist.

```json
var TableStore = require('../index.js'); var Long = TableStore.Long; var client = require('./client'); var currentTimeStamp = Date.now(); var params = {
  tableName: "sampleTable",
  condition: new TableStore.Condition(TableStore.RowExistenceExpectation.IGNORE, null),
  primaryKey: [{ 'gid': Long.fromNumber(20013) }, { 'uid': Long.fromNumber(20013) }],
  attributeColumns: [
    { 'col1': 'Tablestore' },
    { 'col2': '2', 'timestamp': currentTimeStamp },
    { 'col3': 3.1 },
    { 'col4': -0.32 },
    { 'col5': Long.fromNumber(123456789) }
```

`],`

```
  returnContent: { returnType: TableStore.ReturnType.Primarykey }
```

};

```
client.putRow(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  console.log('success:', data);
});
```

For the detailed sample code, visit PutRow@GitHub. GetRow You can call this operation to read a single row of data based on a specified primary key. API operation

```
  /**
   * Read a single row of data based on a specified primary key.
```

`*/`

```
  getRow(params, callback)
```

Examples The following code provides an example on how to read a row of data:

```
var TableStore = require('../index.js'); var Long = TableStore.Long; var client = require('./client'); var params = {
  tableName: "sampleTable",
  primaryKey: [{ 'gid': Long.fromNumber(20004) }, { 'uid': Long.fromNumber(20004) }],
  maxVersions: 2 // The maximum number of versions that can be read. A value of 2 indicat
es that you can read a maximum of 2 versions of data.
```

};

```
var condition = new TableStore.CompositeCondition(TableStore.LogicalOperator.AND); condition.addSubCondition(new TableStore.SingleColumnCondition('name', 'john', TableStore .ComparatorType.EQUAL)); condition.addSubCondition(new TableStore.SingleColumnCondition('addr', 'china', TableStor e.ComparatorType.EQUAL)); params.columnFilter = condition; client.getRow(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  console.log('success:', data);
});
```

For the detailed sample code, visit GetRow@GitHub. UpdateRow You can call this operation to update the data of a specified row. If the row does not exist, a new row is added. If the row exists, the values in the specified columns are added, modified, or deleted based on the request. API operation

```
  /**
   * Update the data of the specified row. If the row does not exist, a new row is added.
If the row exists, the values of the specified columns are added, modified, or deleted ba sed on the request content.
```

`*/`

```
  updateRow(params, callback)
```

Examples The following code provides an example on how to update the data of a specified row:

```json
var TableStore = require('../index.js'); var Long = TableStore.Long; var client = require('./client'); var params = {
    tableName: "sampleTable",
    condition: new TableStore.Condition(TableStore.RowExistenceExpectation.IGNORE, null),
    primaryKey: [{ 'gid': Long.fromNumber(9) }, { 'uid': Long.fromNumber(90) }],
    updateOfAttributeColumns: [
        { 'PUT': [{ 'col4': Long.fromNumber(4) }, { 'col5': '5' }, { 'col6': Long.fromNum
ber(6) }] },
        { 'DELETE': [{ 'col1': Long.fromNumber(1496826473186) }] },
        { 'DELETE_ALL': ['col2'] }
```

`]` };

```
client.updateRow(params,
    function (err, data) {
        if (err) {
            console.log('error:', err);
            return;
        console.log('success:', data);
    });
```

For the detailed sample code, visit UpdateRow@GitHub. DeleteRow You can call this operation to delete data you no longer need. API operation

```
  /**
   * Delete a row of data.
```

`*/`

```
  deleteRow(params, callback)
```

Examples The following code provides an example on how to delete a row of data:

```
var TableStore = require('../index.js'); var Long = TableStore.Long; var client = require('./client'); var params = {
    tableName: "sampleTable",
    condition: new TableStore.Condition(TableStore.RowExistenceExpectation.IGNORE, null),
    primaryKey: [{ 'gid': Long.fromNumber(8) }, { 'uid': Long.fromNumber(80) }]
```

};

```
client.deleteRow(params, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit DeleteRow@GitHub.

###### 2.1.4.5.3 Multi-row operations

Tablestore SDK for Node.js provides multi-row operations, such as BatchGetRow, BatchWriteRow, and GetRange. BatchGetRow You can call this operation to simultaneously read multiple rows of data from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the response time for requests and increase the data read rate. API operation

```
  /**
   * Simultaneously read multiple rows of data from one or more tables.
```

`*/`

```
  batchGetRow(params, callback)
```

Examples The following code provides an example of how to simultaneously read multiple rows of data from multiple tables, and retry the operation if an error occurs in the read of a single row: Not e You can use conditional statements to filter the returned results of BatchWriteRow operations.

```
var client = require('./client'); var TableStore = require('../index.js'); var Long = TableStore.Long; var params = {
    tables: [{
```

```
        tableName: 'sampleTable',
        primaryKey: [
            [{ 'gid': Long.fromNumber(20013) }, { 'uid': Long.fromNumber(20013) }],
            [{ 'gid': Long.fromNumber(20015) }, { 'uid': Long.fromNumber(20015) }]
```

`],`

```
        startColumn: "col2",
        endColumn: "col4"
```

`},` `{`

```
        tableName: 'notExistTable',
        primaryKey: [
            [{ 'gid': Long.fromNumber(10001) }, { 'uid': Long.fromNumber(10001) }]
```

`]` `],` };

```
var maxRetryTimes = 3; var retryCount = 0; function batchGetRow(params) {
    client.batchGetRow(params, function (err, data) {
        if (err) {
            console.log('error:', err);
            return;
        var isAllSuccess = true;
        var retryRequest = { tables: [] };
        for (var i = 0; i < data.tables.length; i++) {
            var faildRequest = { tableName: data.tables[i][0].tableName, primaryKey: [] }
```

;

```
            for (var j = 0; j < data.tables[i].length; j++) {
                if (!data.tables[i][j].isOk && null != data.tables[i][j].primaryKey) {
                    isAllSuccess = false;
                    var pks = [];
                    for (var k in data.tables[i][j].primaryKey) {
                        var name = data.tables[i][j].primaryKey[k].name;
                        var value = data.tables[i][j].primaryKey[k].value;
                        var kp = {};
                        kp[name] = value;
                        pks.push(kp);
                    faildRequest.primaryKey.push(pks);
                } else {
                    // get success data
            if (faildRequest.primaryKey.length > 0) {
                retryRequest.tables.push(faildRequest);
        if (!isAllSuccess && retryCount++ < maxRetryTimes) {
            batchGetRow(retryRequest);
        console.log('success:', data);
    });
```

```
batchGetRow(params, maxRetryTimes);
```

For the detailed sample code, visit BatchGetRow@GitHub. BatchWriteRow You can call this operation to simultaneously insert, modify, or delete multiple rows of data in one or more tables. The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently. API operation

```
  /**
   * Simultaneously modify multiple rows of data.
```

`*/`

```
  batchWriteRow(params, callback)
```

Examples The following code provides an example of how to simultaneously write multiple rows of data: Not e You can use conditional statements to filter the returned results of BatchWriteRow operations.

```
var client = require('./client'); var TableStore = require('../index.js'); var Long = TableStore.Long; var params = {
    tables: [{
        tableName: 'sampleTable',
        rows: [{
            type: 'PUT',
            condition: new TableStore.Condition(TableStore.RowExistenceExpectation.IGNORE
, null),
            primaryKey: [{ 'gid': Long.fromNumber(8) }, { 'uid': Long.fromNumber(80) }],
            attributeColumns: [{ 'attrCol1': 'test1' }, { 'attrCol2': 'test2' }],
            returnContent: { returnType: TableStore.ReturnType.Primarykey }
        }],
    }],
```

};

```
client.batchWriteRow(params, function (err, data) {
    if (err) {
        console.log('error:', err);
        return;
    console.log('success:', data);
});
```

For the detailed sample code, visit BatchWriteRow@GitHub. GetRange You can call this operation to read data within a specified primary key range. API operation

```
  /**
   * Read data within the specified primary key range.
```

`*/`

```
  getRange(params, callback)
```

Examples The following code provides an example on how to read data within a specified range: Not e You can use conditional statements to filter the data read from a specified range. Note that the data may be paged when you perform the GetRange operation.

```
var Long = TableStore.Long; var client = require('./client'); var params = {
  tableName: "sampleTable",
  direction: TableStore.Direction.FORWARD,
  inclusiveStartPrimaryKey: [{ "gid": TableStore.INF_MIN }, { "uid": TableStore.INF_MIN }
```

`],`

```
  exclusiveEndPrimaryKey: [{ "gid": TableStore.INF_MAX }, { "uid": TableStore.INF_MAX }],
  limit: 50
```

};

```
client.getRange(params, function (err, data) {
  if (err) {
    console.log('error:', err);
    return;
  //If the value of data.next_start_primary_key is not null, the read operation is contin
ued.
  if (data.next_start_primary_key) {
  console.log('success:', data);
});
```

For the detailed sample code, visit GetRange@GitHub.

##### 2.1.4.6 Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for Node.js. Methods Tablestore SDK for Node.js handles errors as exceptions. If the operation succeeds, the called operation does not return an exception. If the operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions All errors are handled by Tablestore SDK for Node.js in a unified manner, and are returned as the value of the err parameter by using the callback method. Before you obtain the returned data, you must check whether the err parameter has a value. If an error occurs at the server side of Tablestore, the request ID is returned. The request ID is the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help. Retry The system automatically retries the operation when an error occurs in the SDK. The default policy sets a maximum of 20 retry attempts and a maximum retry interval of 3000 ms. For more information about how the system retries the operation on throttling errors and read-related internal server errors, see

```
 tablestore/lib/retry.js .
```

#### 2.1.5. .NET SDK

##### 2.1.5.1 Preface

This topic describes how to use Tablestore SDK for .NET. Prerequisites An authorized account is created, and an AccessKey pair (AccessKey ID and AccessKey secret) is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Unimanager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for .NET Download the SDK installation package from NuGet. For more information about the download path, visit https://www.nuget.org/packages/Aliyun.TableStore.SDK/4.1.4. Download the source code from GitHub. For more information about the download path, visit GitHub. Compatibility For SDKs V3.x.x: compatible. For SDKs V2.x.x: Some operations are incompatible. The Condition.IGNORE, Condition.EXPECT_EXIST, and Condition.EXPECT_NOT_EXIST parameters are deleted. The DLL file name is changed from Aliyun.dll to Aliyun.TableStore.dll. Version Latest version: 4.1.4.

##### 2.1.5.2 Installation

This topic describes how to install Tablestore SDK for .NET. Version dependency Windows .NET 4.0 or later is required. Visual Studio 2010 or later is required. Install Tablestore SDK for .NET in Windows Install by using NuGet i. After you install NuGet, create a project or open an existing project in Visual Studio, and then choose T ools > NuGet Package Manager > Manage NuGet Packages f or Solut ion. Not e If Visual Studio does not have NuGet installed, download and install NuGet. For more information about the download path, visit NuGet. ii. Enter aliyun.tablestore in the search box and click Search. Find Aliyun.TableStore.SDK in the search results. iii. Select the latest version, and click Inst all. After the installation is complete. Tablestore SDK for .NET is added to the project for application. Install by importing a project i. Download the source code from GitHub. For more information about the download path, visit GitHub. Not e If Git is not installed, download and install Git. For more information about the download path, visit git. ii. In Visual Studio, right-click and select Solut ion from the menu that appears, choose Add > Exist ing project s. iii. In the dialog box that appears, select the aliyun-tablestore-sdk.csproj file, and click Open. iv. Right-click and select Your project . Choose Ref erences > Add Ref erence from the shortcut menu. In the dialog box that appears, click the Project s tab, and select the aliyun-tablestoresdk project. v. Click OK.

##### 2.1.5.3 Initialization

TableStoreClient provides a series of methods for users to manage tables and perform read/write operations on one or more rows. Obtain an endpoint An endpoint is the domain name that is used to access a Tablestore instance within a region. To query an endpoint, perform the following operations:
1. Log on to the Tablestore console.
2. Click the instance name to go to the Inst ance Management page.
On the Instance Details page, you can view the endpoints of an instance in Instance Access URL. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair (AccessKey ID and AccessKey secret) for signature authentication. After you obtain the AccessKey pair, you can perform the following operation to initialize an OTSClient instance by using an endpoint: API operation

```
    /// <summary>
    /// OTSClient constructor.
    /// </summary>
    /// <param name="endPoint">The endpoint of the Tablestore instance. Example: https://
instance.cn-hangzhou.ots.aliyun.com:80. It must start with https://. </param>
    /// <param name="accessKeyID">The AccessKey ID to access the Tablestore instance. You
can apply for an AccessKey ID on the Alibaba Cloud official website. </param>
    /// <param name="accessKeyID">The AccessKey secret that is used to access the Tablest
ore instance. You can apply for an AccessKey secret on the Alibaba Cloud official website . </param>
    /// <param name="instanceName">The name of the Tablestore instance. You can create an
instance name in the Tablestore console. </param> public OTSClient(string endPoint, string accessKeyID, string accessKeySecret, string inst anceName);
    /// <summary>
    /// Create an OTSClient instance by configuring the instance of the OTSClientConfig c
lass.
    /// </summary>
    /// <param name="config">The instance for client configurations.</param>
    public OTSClient(OTSClientConfig config);
```

Examples Not e You can set the ConnectionLimit parameter in the OTSClientConfig instance. If you do not specify the value of the ConnectionLimit parameter, the default value 300 is used. You can set OTSDebugLogHandler and OTSErrorLogHandler in OTSClientConfig to specify whether to enable logging. The retry logic is customizable and controlled by RetryPolicy in OTSClientConfig. A default retry policy is provided.

```
    // Create an OTSClientConfig instance.
    var config = new OTSClientConfig(Endpoint, AccessKeyId, AccessKeySecret, InstanceName
```

);

```
    // Disable logging. By default, logging is enabled.
    config.OTSDebugLogHandler = null;
    config.OTSErrorLogHandler = null;
    // Create an OTSClient instance by using OTSClientConfig.
    var otsClient = new OTSClient(config);
    // Use OTSClient to insert or query data.
```

Multithreading Multithreading is supported. We recommend that you use the same OTSClient instance to perform multithreading tasks.

##### 2.1.5.4 Use the SDK

###### 2.1.5.4.1 Table-level operations

Tablestore SDK for .NET provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable You can call this operation to create a table based on the specified table structure. Not e After the table is created, it takes several seconds to load the table. During this period, read and write operations on the table may fail. You can use applications to perform operations on the table data only after the table is loaded. You must specify the primary key when you create a table. A primary key contains one to four primary key columns. Each primary key column has a name and a data type. API operation

```
/// <summary>
 /// Create a table based on table information including the table name, primary key sche
ma, and reserved read/write throughput.
 /// </summary>
 /// <param name="request">Request parameter</param>
 /// <returns>Information returned by CreateTable. The result is null.
 /// </returns>
        public CreateTableResponse CreateTable(CreateTableRequest request);
        /// <summary>
        /// Asynchronous mode of CreateTable.
        /// </summary>
        public Task<CreateTableResponse> CreateTableAsync(CreateTableRequest request);
```

Examples Create a data table without creating an index table The following code provides an example on how to create a table that has two primary key columns and a reserved read and write throughput of (0, 0):

```
 //Create a schema for the primary key columns, which includes the count, names, and ty
pes of primary key columns.
 //The first primary key column is named pk0 and requires an INTEGER value. The first p
rimary key column is also the partition key.
 //The second primary key column is named pk1 and requires an INTEGER value.
 var primaryKeySchema = new PrimaryKeySchema();
 primaryKeySchema.Add("pk0", ColumnValueType.Integer);
 primaryKeySchema.Add("pk1", ColumnValueType.String);
 //Create a tableMeta class based on the table name and the schema for primary key colu
mns.
 var tableMeta = new TableMeta("SampleTable", primaryKeySchema);
 // Set the reserved read throughput and reserved write throughput to 0.
 var reservedThroughput = new CapacityUnit(0, 0);
 try
```

`{`

```bash
     // Construct the CreateTableRequest object.
     var request = new CreateTableRequest(tableMeta, reservedThroughput);
     // Call the CreateTable operation of the client. If the table is created, no excep
tion is returned. Otherwise, an exception is returned.
     otsClient.CreateTable(request);
     Console.WriteLine("Create table succeeded.") ;
 # If the task fails, an exception is returned for you to handle.
 catch (Exception ex)
```

`{`

```
     Console.WriteLine("Create table failed, exception:{0}", ex.Message);
```

For the detailed sample code, visit CreateTable@GitHub. Create an index table when you create the data table

```
        public static void CreateTableWithGlobalIndex()
```

`{`

```
            // Create a table that contains two primary key columns Pk1 and Pk2 and the
predefined columns Col1 and col2.
            //Create a global secondary index. Specify Col1 as the first primary key co
lumn of the index table.
            OTSClient otsClient = Config.GetClient();
            Console.WriteLine("Start create table with globalIndex...") ;
            PrimaryKeySchema primaryKeySchema = new PrimaryKeySchema
```

`{`

```
                    { Pk1, ColumnValueType.String },
                    { Pk2, ColumnValueType.String }
```

};

```
            TableMeta tableMeta = new TableMeta(TableName, primaryKeySchema);
            tableMeta.DefinedColumnSchema = new DefinedColumnSchema {
                   { Col1, DefinedColumnType.STRING},
                   { Col2, DefinedColumnType.STRING}
```

};

```
            IndexMeta indexMeta = new IndexMeta(IndexName);
            indexMeta.PrimaryKey = new List<string>() { Col1 };
            indexMeta.DefinedColumns = new List<string>() { Col2 };
            //indexMeta.IndexType = IndexType.IT_GLOBAL_INDEX;
            //indexMeta.IndexUpdateModel = IndexUpdateMode.IUM_ASYNC_INDEX;
            List<IndexMeta> indexMetas = new List<IndexMeta>() { };
            indexMetas.Add(indexMeta);
            CapacityUnit reservedThroughput = new CapacityUnit(0, 0);
            CreateTableRequest request = new CreateTableRequest(tableMeta, reservedThro
ughput, indexMetas);
            otsClient.CreateTable(request);
            Console.WriteLine("Table is created: " + TableName);
```

ListTable You can call this operation to query the names of all tables created in the current instance. API operation

```
 /// <summary>
 /// Query the names of all tables created in the current instance.
 /// </summary>
 /// <param name="request">Request parameter</param>
 /// <returns>Information returned by ListTable that contains the table name list.</retur
ns> </returns>
 public ListTableResponse ListTable(ListTableRequest request);
 /// <summary>
 /// Asynchronous mode of ListTable.
 /// </summary>
 public Task<ListTableResponse> ListTableAsync(ListTableRequest request);
```

Examples The following code provides an example on how to obtain the names of all tables in the current instance:

```
 var request = new ListTableRequest();
 try
```

`{`

```
     var response = otsClient.ListTable(request);
     foreach (var tableName in response.TableNames)
```

`{`

```
         Console.WriteLine("Table name:{0}", tableName);
     Console.Writeline("List table succeeded.");
 catch (Exception ex)
```

`{`

```
     Console.WriteLine("List table failed, exception:{0}", ex.Message);
```

UpdateTable You can call this operation to update the settings of reserved read/write throughput of a table. API operation

```
 /// <summary>
 /// Update the reserved read/write throughput settings of the specified table. New setti
ngs take effect within a minute after the update succeeds.
 /// </summary>
 /// <param name="request">Request parameter, including the table name and reserved read/
write throughput.</param>
 /// <returns>Contains information such as the updated reserved read/write throughput.</r
eturns>
 public UpdateTableResponse UpdateTable(UpdateTableRequest request);
 /// <summary>
 /// Asynchronous mode of UpdateTable.
 /// </summary>
 public Task<UpdateTableResponse> UpdateTableAsync(UpdateTableRequest request);
```

Examples The following code provides an example on how to update the numbers of read capacity units (CUs) of a table to 1 and write CUs to 2:

```
 // Update the reserved read throughput to 1 and the reserved write throughput to 2.
 var reservedThroughput = new CapacityUnit(1, 2);
 // Construct an UpdateTableRequest object.
 var request = new UpdateTableRequest("SampleTable", reservedThroughput);
 try
```

`{`

```
     // Call the API to update the reserved read/write throughput of the table.
     otsClient.UpdateTable(request);
     // If the task succeeds, no exception is returned.
     Console.Writeline("Update table succeeded.");
 catch (Exception ex)
```

`{`

```
     // If the task fails, an exception is returned and handled.
     Console.WriteLine("Update table failed, exception:{0}", ex.Message);
```

For the detailed sample code, visit UpdateTable@GitHub. DescribeTable You can call this operation to query the structure information and reserved read/write throughput value of the specified table. API operation

```
 /// <summary>
 /// Query the structure information and reserved read/write throughput settings of the s
pecified table.
 /// </summary>
 /// <param name="request">Request parameter, including the table name.</param>
 /// <returns>Contains the structure information and reserved read/write throughput setti
ngs of the specified table.</returns> </returns>
 public DescribeTableResponse DescribeTable(DescribeTableRequest request);
 /// <summary>
 /// Asynchronous mode of DescribeTable.
 /// </summary>
 public Task<DescribeTableResponse> DescribeTableAsync(DescribeTableRequest request);
```

Examples The following code provides an example on how to obtain the description of a table:

```
 try
```

`{`

```
     var request = new DescribeTableRequest("SampleTable");
     var response = otsClient.DescribeTable(request);
     //Display the descriptive information of the specified table.
     Console.Writeline("Describe table succeeded.") ;
     Console.WriteLine("LastIncreaseTime: {0}", response.ReservedThroughputDetails.LastIn
creaseTime);
     Console.WriteLine("LastDecreaseTime: {0}", response.ReservedThroughputDetails.LastDe
creaseTime);
     Console.WriteLine("NumberOfDecreaseToday: {0}", response.ReservedThroughputDetails.L
astIncreaseTime);
     Console.WriteLine("ReadCapacity: {0}", response.ReservedThroughputDetails.CapacityUn
it.Read);
     Console.WriteLine("WriteCapacity: {0}", response.ReservedThroughputDetails.CapacityU
nit.Write);
 catch (Exception ex)
```

`{`

```
     // If the task fails, an exception is returned and handled.
     Console.WriteLine("Describe table failed, exception:{0}", ex.Message);
```

For the detailed sample code, visit DescribeTable@GitHub. DeleteTable You can call this operation to delete a specified table from an instance. API operation

```
 /// <summary>
 /// Delete the table of the specified name.
 /// </summary>
 /// <param name="request">Request parameter, including the table name.</param>
 /// <returns>Information returned by DeleteTable. The result is null.
 /// </returns>
 public DeleteTableResponse DeleteTable(DeleteTableRequest request);
 /// <summary>
 /// Asynchronous mode of DeleteTable.
 /// </summary>
 public Task<DeleteTableResponse> DeleteTableAsync(DeleteTableRequest request);
```

Examples The following code provides an example on how to delete a table:

```
 var request = new DeleteTableRequest("SampleTable");
 try
```

`{`

```
     otsClient.DeleteTable(request);
     Console.Writeline("Delete table succeeded.");
 catch (Exception ex)
```

`{`

```
     Console.WriteLine("Delete table failed, exception:{0}", ex.Message);
```

For the detailed sample code, visit DeleteTable@GitHub.

###### 2.1.5.4.2 Single-row operations

The Tablestore SDK provides the following APIs for single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can use the PutRow API to insert data into a specified row.

```
        /// <summary>
        /// Write a row of data based on the specified table name, primary keys, and attrib
utes. Thu number of CUs consumed by the operation is returned.
        /// </summary>
        /// <param name="request">Data insertion request</param>
        /// <returns>The number of CUs consumed by the operation</returns>
        public PutRowResponse PutRow(PutRowRequest request);
        /// <summary>
        /// Asynchronous mode of PutRow.
        /// </summary>
        public Task<PutRowResponse> PutRowAsync(PutRowRequest request);
```

Example 1 The following code provides an example of how to insert a row of data:

```
        // Define the primary keys of the row. These primary keys must be consistent with t
he primary keys defined in TableMeta during table creation.
        var primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        // Define the attribute columns of the row.
        var attribute = new AttributeColumns();
        attribute.Add("col0", new ColumnValue(0));
        attribute.Add("col1", new ColumnValue("a"));
        attribute.Add("col2", new ColumnValue(true));
        try
```

`{`

```
            // Construct the request object for data insertion. RowExistenceExpectation.IGN
ORE indicates that data is inserted regardless of whether the specified row exists.
            var request = new PutRowRequest("SampleTable", new Condition(RowExistenceExpect
ation.IGNORE),
                                    primaryKey, attribute);
            // Call the PutRow API to insert data.
            otsClient.PutRow(request);
            // If task execution succeeds, no exception is thrown.
            Console.WriteLine("Put row succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Put row failed, exception:{0}", ex.Message);
```

Not e Condition.IGNORE, Condition.EXPECT_EXIST, and Condition.EXPECT_NOT_EXIST are deprecated in V3.0.0 and later. Use new Condition (RowExistenceExpectation. IGNORE), new Condition (RowExistenceExpectation.EXPECT_EXIST), and new Condition (RowExistenceExpectation. EXPECT_NOT_EXIST) instead. RowExistenceExpectation.IGNORE indicates that new data is inserted regardless of whether the specified row exists. If the row exists, the existing data is overwritten. RowExistenceExpectation.EXPECT_EXIST indicates that new data is inserted only when the specified row exists. The existing data is overwritten. RowExistenceExpectation.EXPECT_NOT_EXIST indicates that data is inserted only when the specified row does not exist. In addition to row conditions, the Condition parameter also supports column conditions in V2.2.0 and later. To view the detailed code, see PutRow@GitHub. Example 2 The following code provides an example of how to insert a row of data based on specified conditions. Assume that data is inserted only when a specified row exists and the value of col1 is greater than 24.

```
        // Define the primary keys of the row. These primary keys must be consistent with t
he primary keys defined in TableMeta during table creation.
        var primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        // Define the attribute columns of the row.
        AttributeColumns attribute = new AttributeColumns();
        attribute.Add("col0", new ColumnValue(0));
        attribute.Add("col1", new ColumnValue("a"));
        attribute.Add("col2", new ColumnValue(true));
        var request = new PutRowRequest(tableName, new Condition(RowExistenceExpectation.EX
PECT_EXIST),
                                    primaryKey, attribute);
        // When the value of col0 is greater than 24, rerun PutRow to overwrite the existin
g value.
        try
```

`{`

```
            request.Condition.ColumnCondition = new RelationalCondition("col0",
                                                RelationalCondition.CompareOperator.GREATER
_THAN,
                                                new ColumnValue(24));
            otsClient.PutRow(request);
            Console.WriteLine("Put row succeeded.");
        catch (Exception ex)
```

`{`

```
            Console.WriteLine("Put row failed. error:{0}", ex.Message);
```

Not e You can set a single condition or a combination of conditions. For example, you can set two conditions for data insertion such as col1 > 5 and pk2 < 'xyz'. Attribute columns and primary key columns can be used to set conditions. When the column specified in a condition does not exist in a row, PassIfMissing in RelationCondition determines the next action. The default value is true. To view the detailed code, see ConditionPutRow@GitHub. Example 3 The following code provides an example of how to asynchronously insert a row of data:

```
        try
```

`{`

```
            var putRowTaskList = new List<Task<PutRowResponse>>();
            for (int i = 0; i < 100; i++)
```

`{`

```
                // Define the primary keys of the row. These primary keys must be consisten
t with the primary keys defined in TableMeta during table creation.
                var primaryKey = new PrimaryKey();
                primaryKey.Add("pk0", new ColumnValue(i));
                primaryKey.Add("pk1", new ColumnValue("abc"));
                // Define the attribute columns of the row.
                var attribute = new AttributeColumns();
                attribute.Add("col0", new ColumnValue(i));
                attribute.Add("col1", new ColumnValue("a"));
                attribute.Add("col2", new ColumnValue(true));
                var request = new PutRowRequest(TableName, new Condition(RowExistenceExpect
ation.IGNORE),
                                                primaryKey, attribute);
                putRowTaskList.Add(TabeStoreClient.PutRowAsync(request));
            // Wait until each asynchronous invocation returns results and displays the con
sumed CUs.
            foreach (var task in putRowTaskList)
```

`{`

```
                task.Wait();
                Console.WriteLine("consumed read:{0}, write:{1}", task.Result.ConsumedCapac
ityUnit.Read,
                                    task.Result.ConsumedCapacityUnit.Write);
            // Data is inserted if no exception is thrown.
            Console.WriteLine("Put row async succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Put row async failed. exception:{0}", ex.Message);
```

Not e Each asynchronous invocation starts a thread. A timeout error may occur if too many asynchronous invocations are started consecutively and each invocation consumes an extended period of time. To view the detailed code, see PutRowAsync@GitHub. GetRow You can use the GetRow API to read a single row of data based on a specified primary key.

```
        /// <summary>
        /// Read a single row of data based on a specified primary key.
        /// </summary>
        /// <param name="request">Data query request</param>
        /// <returns>Response of GetRow</returns>
        public GetRowResponse GetRow(GetRowRequest request);
        /// <summary>
        /// Asynchronous mode of GetRow.
        /// </summary>
        public Task<GetRowResponse> GetRowAsync(GetRowRequest request);
```

Example 1 The following code provides an example of how to read a row of data:

```
        // Define the primary keys of the row. These primary keys must be consistent with t
he primary keys defined in TableMeta during table creation.
        PrimaryKey primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        try
```

`{`

```
            // Construct a query request object. The entire row is read if no column is spe
cified.
            var request = new GetRowRequest(TableName, primaryKey);
            // Call the GetRow API to query data.
            var response = otsClient.GetRow(request);
            // Generate the data of the row. The generated data is not shown here. For more
information, see the GitHub link.
            // If task execution succeeds, no exception is thrown.
            Console.WriteLine("Get row succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Update table failed, exception:{0}", ex.Message);
```

Not e If you query a row of data, the system returns the data in all columns of the row. You can use the columnsToGet parameter to read data from specified columns. For example, the system returns only the data in col0 and col1 if col0 and col1 are inserted into columnsToGet. Conditional filtering is supported. For example, you can configure the system to return results only when the value of col0 is greater than 24. When the columnsToGet and Condition parameters are both used, the system returns results based on columnsToGet, and then filters the returned columns by the Condition parameter. When the specified column does not exist, PassIfMissing determines the next action. To view the detailed code, see GetRow@GitHub. Example 2 The following code provides an example of how to use the filter feature to read a row of data. In the example, data is queried. Only data in col0 and col1 is returned. The data in col0 is filtered based on the condition of col0=24.

```
        // Define the primary keys of the row. These primary keys must be consistent with t
he primary keys defined in TableMeta during table creation.
        PrimaryKey primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        var rowQueryCriteria = new SingleRowQueryCriteria("SampleTable");
        rowQueryCriteria.RowPrimaryKey = primaryKey;
        // Condition 1: The value of col0 is 5.
        var filter1 = new RelationalCondition("col0",
                    RelationalCondition.CompareOperator.EQUAL,
                    new ColumnValue(5));
        // Condition 2: The value of col1 is not ff.
        var filter2 = new RelationalCondition("col1", RelationalCondition.CompareOperator.N
OT_EQUAL, new ColumnValue("ff"));
        // Construct a combination of Condition 1 and Condition 2 with the OR relationship.
        var filter = new CompositeCondition(CompositeCondition.LogicOperator.OR);
        filter.AddCondition(filter1);
        filter.AddCondition(filter2);
        rowQueryCriteria.Filter = filter;
        // Configure the rows you want to query with the condition [col0, col1], and then f
ilter the queried data based on the previously specified conditions.
        rowQueryCriteria.AddColumnsToGet("col0");
        rowQueryCriteria.AddColumnsToGet("col1");
        // Construct GetRowRequest.
        var request = new GetRowRequest(rowQueryCriteria);
        try
```

`{`

```
            // Query data.
            var response = otsClient.GetRow(request);
            // Generate data or perform the related logical operation (omitted).
            // If task execution succeeds, no exception is thrown.
            Console.WriteLine("Get row with filter succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Get row with filter failed, exception:{0}", ex.Message);
```

Not e To view the detailed code, see GetRowWithFilter@GitHub. UpdateRow You can use the UpdateRow API to update the data of a specified row. If the row does not exist, a new row is added. If the row exists, the values of the specified columns are added, modified, or deleted based on the request content.

```
        /// <summary>
        /// Update the data of the specified row. If the row does not exist, a new row is a
dded. If the row exists, the values of the specified columns are added, modified, or delete d based on the request content.
        /// </summary>
        /// <param name="request">Request instance</param>
        public UpdateRowResponse UpdateRow(UpdateRowRequest request);
        /// <summary>
        /// Asynchronous mode of UpdateRow.
        /// </summary>
        /// <param name="request"></param>
        /// <returns></returns>
        public Task<UpdateRowResponse> UpdateRowAsync(UpdateRowRequest request);
```

Examples The following code provides an example of how to update the data of a specified row:

```
        // Define the primary keys of the row. These primary keys must be consistent with t
he primary keys defined in TableMeta during table creation.
        PrimaryKey primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        // Define the attribute columns of the row.
        UpdateOfAttribute attribute = new UpdateOfAttribute();
        attribute.AddAttributeColumnToPut("col0", new ColumnValue(0));
        attribute.AddAttributeColumnToPut("col1", new ColumnValue("b")); // Change the orig
inal value a to b.
        attribute.AddAttributeColumnToPut("col2", new ColumnValue(true));
        try
```

`{`

```
            // Construct the request object for row updating. RowExistenceExpectation.IGNOR
E indicates that data is updated regardless of whether the specified row exists.
            var request = new UpdateRowRequest(TableName, new Condition(RowExistenceExpecta
tion.IGNORE),
                                    primaryKey, attribute);
            // Call the UpdateRow API to run the following line of code:
            otsClient.UpdateRow(request);
            // If task execution succeeds, no exception is thrown.
            Console.Writeline("Update row succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Update row failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to update rows. To view the detailed code, see UpdateRow@GitHub. DeleteRow

```
        /// <summary>
        /// Delete a row of data based on the specified table name and primary keys.
        /// </summary>
        /// <param name="request">Request instance</param>
        /// <returns>Response instance</returns>
        public DeleteRowResponse DeleteRow(DeleteRowRequest request);
        /// <summary>
        /// Asynchronous mode of DeleteRow.
        /// </summary>
        public Task<DeleteRowResponse> DeleteRowAsync(DeleteRowRequest request);
```

Examples The following code provides an example of how to delete a row of data:

```
        // The values of the primary key columns of the row to be deleted are 0 and "abc".
        var primaryKey = new PrimaryKey();
        primaryKey.Add("pk0", new ColumnValue(0));
        primaryKey.Add("pk1", new ColumnValue("abc"));
        try
```

`{`

```
            // Construct a request. Condition.EXPECT_EXIST indicates that the row is delete
d only when it exists.
            var deleteRowRequest = new DeleteRowRequest("SampleTable", Condition.EXPECT_EXI
ST, primaryKey);
            // Call the DeleteRow API to delete the row.
            otsClient.DeleteRow(deleteRowRequest);
            // If task execution succeeds, no exception is thrown.
            Console.Writeline("Delete table succeeded.");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Delete table failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to delete rows. To view the detailed code, see DeleteRow@GitHub.

###### 2.1.5.4.3 Multiple-row operations

The Tablestore SDK provides the following APIs for multiple-row operations: BatchGetRow, BatchWriteRow, GetRange, and GetRangeIterator. BatchGetRow You can use the BatchGetRow API to simultaneously read several rows of data from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the request response time and increase the data read rate.

```
        /// <summary>
        /// <para>Simultaneously read several rows of data from one or more tables. </para>
        /// <para>The BatchGetRow operation is a set of multiple GetRow operations. The exe
cution, returning of results, and CU consumption of each individual operation are carried o ut independently. </para>
        /// Compared with the execution of a large number of GetRow operations, the use of
BatchGetRow can reduce the request response time and increase the data read rate.
        /// </summary>
        /// <param name="request">Request instance</param>
        /// <returns>Response instance</returns>
        public BatchGetRowResponse BatchGetRow(BatchGetRowRequest request);
        /// <summary>
        /// Asynchronous mode of BatchGetRow.
        /// </summary>
        public Task<BatchGetRowResponse> BatchGetRowAsync(BatchGetRowRequest request);
```

Examples The following code provides an example of how to simultaneously read 10 rows of data:

```
        // Construct a batch-read request object, including the primary key values of the 1
0 rows.
        List<PrimaryKey> primaryKeys = new List<PrimaryKey>();
        for (int i = 0; i < 10; i++)
```

`{`

```
            PrimaryKey primaryKey = new PrimaryKey();
            primaryKey.Add("pk0", new ColumnValue(i));
            primaryKey.Add("pk1", new ColumnValue("abc"));
            primaryKeys.Add(primaryKey);
        try
```

`{`

```
            BatchGetRowRequest request = new BatchGetRowRequest();
            request.Add(TableName, primaryKeys);
            // Call BatchGetRow to read 10 rows of data.
            var response = otsClient.BatchGetRow(request);
            var tableRows = response.RowDataGroupByTable;
            var rows = tableRows[TableName];
            // Enter the input data for the rows. The input data is not shown here. For mor
e information, see the GitHub link.
            // BatchGetRow may partially fail. Therefore, you must check the status of each
row. For more information, see the GitHub link.
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Batch get row failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to filter the results returned by a BatchGetRow operation. To view the detailed code, see BatchGetRow@GitHub. BatchWriteRow You can use the BatchWriteRow API to insert, modify, or delete several rows of data in one or more tables. The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently.

```
        /// <summary>
        /// <para>You can use the BatchWriteRow API to insert, modify, or delete several ro
ws of data in one or more tables. </para>
        /// <para>The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and D
eleteRow operations. The execution, returning of results, and CU consumption of each indivi dual operation are carried out independently. </para>
        /// <para>Compared with the execution of a large number of write operations, the us
e of BatchWriteRow can reduce the request response time and increase the data write rate. < /para>
        /// </summary>
        /// <param name="request">Request instance</param>
        /// <returns>Response instance</returns>
        public BatchWriteRowResponse BatchWriteRow(BatchWriteRowRequest request);
        /// <summary>
        /// Asynchronous mode of BatchWriteRow.
        /// </summary>
        /// <param name="request"></param>
        /// <returns></returns>
        public Task<BatchWriteRowResponse> BatchWriteRowAsync(BatchWriteRowRequest request)
```

; Examples The following code provides an example of how to simultaneously import 100 rows of data:

```
        // Construct a batch-import request object, including the primary key values of the
100 rows.
        var request = new BatchWriteRowRequest();
        var rowChanges = new RowChanges();
        for (int i = 0; i < 100; i++)
```

`{`

```
            PrimaryKey primaryKey = new PrimaryKey();
            primaryKey.Add("pk0", new ColumnValue(i));
            primaryKey.Add("pk1", new ColumnValue("abc"));
            // Define the attribute columns of the 100 rows.
            UpdateOfAttribute attribute = new UpdateOfAttribute();
            attribute.AddAttributeColumnToPut("col0", new ColumnValue(0));
            attribute.AddAttributeColumnToPut("col1", new ColumnValue("a"));
            attribute.AddAttributeColumnToPut("col2", new ColumnValue(true));
            rowChanges.AddUpdate(new Condition(RowExistenceExpectation.IGNORE), primaryKey,
attribute);
        request.Add(TableName, rowChanges);
        try
```

`{`

```
            // Call the BatchWriteRow API.
            var response = otsClient.BatchWriteRow(request);
            var tableRows = response.TableRespones;
            var rows = tableRows[TableName];
            // BatchWriteRow may partially fail. Therefore, you must check the status of ea
ch row. For more information, see the GitHub link.
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Batch put row failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to filter the results returned by a BatchWriteRow operation. To view the detailed code, see BatchWriteRow@GitHub. GetRange You can use the GetRange API to read data within the specified primary key range.

```
        /// <summary>
        /// Obtain data from multiple rows within a specified range.
        /// </summary>
        /// <param name="request">Request instance</param>
        /// <returns>Response instance</returns>
        public GetRangeResponse GetRange(GetRangeRequest request);
        /// <summary>
        /// Asynchronous mode of GetRange.
        /// </summary>
        /// <param name="request"></param>
        /// <returns></returns>
        public Task<GetRangeResponse> GetRangeAsync(GetRangeRequest request);
```

Examples The following code provides an example of how to read data within the specified range:

```
        // Read all rows in the range from (0, INF_MIN) to (100, INF_MAX).
        var inclusiveStartPrimaryKey = new PrimaryKey();
        inclusiveStartPrimaryKey.Add("pk0", new ColumnValue(0));
        inclusiveStartPrimaryKey.Add("pk1", ColumnValue.INF_MIN);
        var exclusiveEndPrimaryKey = new PrimaryKey();
        exclusiveEndPrimaryKey.Add("pk0", new ColumnValue(100));
        exclusiveEndPrimaryKey.Add("pk1", ColumnValue.INF_MAX);
        try
```

`{`

```
            // Construct a read request object in the specified range.
            var request = new GetRangeRequest(TableName, GetRangeDirection.Forward,
                            inclusiveStartPrimaryKey, exclusiveEndPrimaryKey);
            var response = otsClient.GetRange(request);
            // Continue the read operation if only partial data is returned.
            var rows = response.RowDataList;
            var nextStartPrimaryKey = response.NextPrimaryKey;
            while (nextStartPrimaryKey != null)
```

`{`

```
                request = new GetRangeRequest(TableName, GetRangeDirection.Forward,
                                nextStartPrimaryKey, exclusiveEndPrimaryKey);
                response = otsClient.GetRange(request);
                nextStartPrimaryKey = response.NextPrimaryKey;
                foreach (RowDataFromGetRange row in response.RowDataList)
```

`{`

```
                    rows.Add(row);
            // Generate the data of the rows. The generated data is not shown here. For mor
e information, see the GitHub link.
            // If task execution succeeds, no exception is thrown.
            Console.WriteLine("Get range succeeded");
        catch (Exception ex)
```

`{`

```
            // If task execution fails, an exception is thrown and an error message is disp
layed.
            Console.WriteLine("Get range failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to filter the read data returned from the specified range. To view the detailed code, see GetRange@GitHub. GetRangeIterator You can use the GetRangeIterator API to obtain an iterator within the specified range.

```
        /// <summary>
        /// Obtain data from multiple rows within the specified range. Return the iterator
used to process each row of data.
        /// </summary>
        /// <param name="request"><see cref="GetIteratorRequest"/></param>
        /// <returns>Return the <see cref="RowDataFromGetRange"/> iterator. </returns>
        public IEnumerable<RowDataFromGetRange> GetRangeIterator(GetIteratorRequest request
```

); Examples The following code provides an example of how to obtain an iterator:

```
        // Read all rows in the range from (0, "a") to (1000, "xyz").
        PrimaryKey inclusiveStartPrimaryKey = new PrimaryKey();
        inclusiveStartPrimaryKey.Add("pk0", new ColumnValue(0));
        inclusiveStartPrimaryKey.Add("pk1", new ColumnValue("a"));
        PrimaryKey exclusiveEndPrimaryKey = new PrimaryKey();
        exclusiveEndPrimaryKey.Add("pk0", new ColumnValue(1000));
        exclusiveEndPrimaryKey.Add("pk1", new ColumnValue("xyz"));
        // Construct a CapacityUnit to record the number of CUs consumed by iteration.
        var cu = new CapacityUnit(0, 0);
        try
```

`{`

```
            // Construct a GetIteratorRequest. Filter conditions are supported.
            var request = new GetIteratorRequest(TableName, GetRangeDirection.Forward, incl
usiveStartPrimaryKey,
                                                exclusiveEndPrimaryKey, cu);
            var iterator = otsClient.GetRangeIterator(request);
            // Iterator that reads data in a traversal method.
            foreach (var row in iterator)
```

`{`

```
                // Processing logic.
            Console.WriteLine("Iterate row succeeded");
        catch (Exception ex)
```

`{`

```
            Console.WriteLine("Iterate row failed, exception:{0}", ex.Message);
```

Not e You can use conditional statements to filter the data read through an iterator. To view the detailed code, see GetRangeIterator@GitHub.

##### 2.1.5.5 Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for .NET. Method The Tablestore .NET SDK adopts the Exception method to handle errors. If an operation succeeds, the called API does not throw an exception. If the operation fails, an exception is thrown. Not e Batch operation APIs such as BatchGetRow and BatchWriteRow are called only when the status check of each row is successful. Error The Tablestore .NET SDK has two types of exceptions: OTSClientException and OTSServerException. Both are inherited from Exception. OTSClientException: indicates an internal SDK exception, such as an incorrect parameter value or a failure to parse the results returned by the server. OTSServerException: indicates a server error arising from the resolution of a server error message. OTSServerException has the following components: HttpStatusCode: an HTTP status code, such as 200 or 404. ErrorCode: an error type string returned by Tablestore. ErrorMessage: an error message string returned by Tablestore. RequestId: the UUID that uniquely identifies a request. If a problem persists, submit the request ID to Tablestore technical support personnel to obtain help. Retry The system retries an operation when an error occurs in the SDK. The operation is retried three times at a maximum interval of two seconds by default. For more information, see the Aliyun.OTS.Retry.DefaultRetryPolicy class. You can modify RetryPolicy in OTSClientConfig to customize a retry policy.

#### 2.1.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top navigation bar, click Ent erprise.
5. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
6. In the organization navigation tree, click an organization name.
7. In the Current Organization section, click Obt ain an accesskey.
8. In the AccessKey message, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to each level-1 organization. Subordinate organizations use the same AccessKey pair of their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
5. In the Apsara St ack AccessKey Pair section, view your AccessKey pair.
Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs of accounts grant you full permissions to access Apsara Stack resources. You must keep your AccessKey pair confidential.
