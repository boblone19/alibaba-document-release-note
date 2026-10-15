---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Tablestore Developer Guide"
product_version: "V3.16.2"
doc_version: "20220905"
pdf_pages: 189
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Tablestore Developer Guide 20220905.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Tablestore%20Developer%20Guide%2020220905.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Tablestore Developer Guide

## API reference

### API-based operations

#### GetRow

Reads a single row of data based on the specified primary key. Request syntax

```
message GetRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2;   // The primary key is encoded in the PlainBuffer form
at.
    repeated string columns_to_get = 3; // If you do not specify this parameter, all column
s are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional bytes filter = 7;
    optional string start_column = 8;
    optional string end_column = 9;
    optional bytes token = 10;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table name _ | string | Yes | The name of the table from which you want to read data. |
| primary key _ | bytes | Yes | All primary key columns of the row whose data you want to read, including the names and values of the primary key columns. The primary key columns are encoded in the PlainBuffer format. |
| columns to get _ _ | string | No | The names of the columns that you want to return. If you do not specify this parameter, all columns of the row are returned. The value of this parameter can contain up to 128 strings. If the specified column does not exist, data of the specified column is not returned. If you specify duplicate column names, the response includes this column only once. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| time range _ | TimeRange | No (You must specify at least one of time range _ and max versions.) _ | The timestamp range of the data that you want to read. The minimum value is 0, and the maximum value is INT64.MAX. Unit: milliseconds. If you want to query data within a specified timestamp range, specify start time and end time. If you want to _ _ query data with a specified timestamp, specify specific time. _ For example, if the value of time range _ is [100, 200), the timestamp of the data in the returned columns must be within the range of [100, 200). |
| max versions _ | int32 | No (You must specify at least one of time range _ and max versions.) _ | The maximum number of versions of data that you want to return. For example, if the value of max versions is 2, a maximum of two _ versions of data is returned for each column. |
| filter | bytes | No | The expression of the filter condition, which is serialized as binary data by using Protobuf. |
| start column _ | string | No | The column from which the read operation starts in the row. This parameter is used for wide-column read. The columns are sorted based on their names in alphabetical order. The response contains the specified start column. For example, if a table contains columns a, b, and c, and the value of start column is b, the read operation _ starts from column b, and columns b and c are returned. |
| end column _ | string | No | The column at which the read operation ends. The response does not contain the specified end column. The columns are sorted based on their names in alphabetical order. For example, if a table contains columns a, b, and c, and the value of end column _ is b, the read operation ends at column b, and only column a is returned. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| token | bytes | No | The position at which the next wide- column read operation starts. This parameter is unavailable. |

Response syntax

```
message GetRowResponse {
    required ConsumedCapacity consumed = 1;
    required bytes row = 2;  // The row is encoded as binary data in the PlainBuffer format
```

`.`

| Parameter | Type | Description |
|---|---|---|
| consumed | ConsumedCapacit y | The number of capacity units (CUs) that are consumed by the operation. |
| row | bytes | The data that is read from the row. If the requested row does not exist, no data is returned. The returned data is encoded in the PlainBuffer format. |

CU consumption If the requested row does not exist, one read CU is consumed. If the requested row exists, the number of consumed read CUs is rounded up from the calculation result of the following formula: Number of consumed read CUs = (Size of data in all primary key columns of the row + Size of data in the attribute columns that are read)/4 KB. If the request times out and the results are undefined, CUs may or may not be consumed. If an HTTP status code 5xx is returned, which indicates that an internal error occurred, the operation does not consume CUs. If other errors are returned, one read CU is consumed.

#### PutRow

Inserts a row. If the row exists, the existing data is overwritten. Otherwise, a new row is added. Request syntax

```
message PutRowRequest {
    required string table_name = 1;
    required bytes row = 2;  // The row is encoded as binary data in the PlainBuffer format
```

`.`

```
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table name _ | string | Yes | The name of the table to which you want to write data. |
| row | bytes | Yes | The row that you want to insert into the table, including primary key columns and attribute columns of the row. The row is encoded in the PlainBuffer format. |
| condition | Condition | Yes | Specifies whether to perform row existence check before a data operation. Valid values: IGNORE: Row existence check is not performed. EXPECT EXIST: The row is expected to _ exist. EXPECT NOT EXIST: The row is _ _ expected not to exist. If the row is expected not to exist but the row exists, the row fails be inserted and an error is returned. If the row is expected to exist but the row does not exist, the row also fails to be inserted and an error is returned. |
| return content _ | ReturnContent | No | The content that you want to return after the row is inserted. Only the primary key can be returned. This parameter is mainly used by the auto- increment primary key column feature. |

Response syntax

```
message PutRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

| Parameter | Type | Description |
|---|---|---|
| consumed | ConsumedCapacity | The number of capacity units (CUs) that are consumed by the operation. |

| Parameter | Type | Description |
|---|---|---|
| row | bytes | The data that is returned if you specify a value for return content. The data is _ encoded in the PlainBuffer format. If you do not specify a value for return content or no data is _ returned, NULL is returned. |

CU consumption If the row that you want to insert does not exist, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to insert)/4 KB. If the value of the condition parameter is EXPECT_NOT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to insert)/4 KB. The number of consumed read CUs is rounded up from the calculation result of the following formula: Number of consumed read CUs = Size of the data in all primary key columns of the row/4 KB. If the value of the condition parameter is EXPECT_EXIST, the row fails to be inserted. One write CU and one read CU are consumed. If the row that you want to insert exists, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to insert)/4 KB. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to insert)/4 KB. The number of consumed read CUs is rounded up from the calculation result of the following formula: Number of consumed read CUs = Size of the data in all primary key columns of the row/4 KB. If the value of the condition parameter is EXPECT_NOT_EXIST, the row fails to be inserted. One write CU and one read CU are consumed. When you use conditional update, the number of consumed CUs is calculated by using the preceding formulas if the operation succeeds. If the operation fails, one write CU and one read CU are consumed. If the request times out and the results are undefined, CUs may or may not be consumed. If an HTTP status code 5xx is returned, which indicates that an internal error occurred, the operation does not consume CUs. If other errors are returned, one write CU is consumed.

#### UpdateRow

Updates the data of a row. Not e If the specified row does not exist, a new row is inserted. If the specified row exists, the values of the specified columns are added, modified, or deleted based on the request. Request syntax

```
message UpdateRowRequest {
 required string table_name = 1;
 required bytes row_change = 2;
 required Condition condition = 3;
 optional ReturnContent return_content = 4;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table name _ | string | Yes | The name of the table whose data you want to update. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| row change _ | bytes | Yes | The data that you want to update, including primary key columns and attribute columns. The data is encoded in the PlainBuffer format. Tablestore adds, modifies, or deletes the values in the specified attribute columns of the row based on the value of UpdateType in row change. The _ columns that exist in the row but are not specified by row change are not _ affected. Valid values of UpdateType: PUT: The value must be a valid value of an attribute column. If the specified column does not exist, a new column is added. If the specified column exists, the existing column is overwritten. DELETE: The value must be empty, and a timestamp must be specified. This update type specifies that data of the specified version is deleted from the column. DELETE ALL: The value and the _ timestamp must be empty. This update type specifies that data of all versions in the column are deleted. Not e The row exists even if all attribute columns of the row are deleted. To delete the row, call the DeleteRow operation. |
| condition | Condition | Yes | Specifies whether to perform row existence check before data is updated. Default value: IGNORE. Valid values: IGNORE: Row existence check is not performed. If you set the condition parameter to IGNORE, the operation is not affected regardless of whether the row exists. EXPECT EXIST: The row is expected to _ exist. If the row is expected to exist but the row does not exist, the operation fails and an error is returned. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| return content _ | ReturnContent | No | The content that you want to return. Only the primary key can be returned. This parameter is mainly used by the auto-increment primary key column feature. |

Response syntax

```
message UpdateRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

| Parameter | Type | Description |
|---|---|---|
| consumed | ConsumedCapacit y | The number of capacity units (CUs) that are consumed by the operation. |
| row | bytes | The data that is returned if you specify a value for return content. If you do not specify a value for return content _ _ or no return value exists, NULL is returned. The return data is encoded in the PlainBuffer format. |

CU consumption If the row that you want to update does not exist, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to update)/4 KB. If UpdateRow contains an attribute column that you want to delete, the length of the column name is calculated as the size of data in the column. If the value of the condition parameter is EXPECT_EXIST, data fails to be written to the row. One write CU and one read CU are consumed. If the row that you want to update exists, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = (Size of data in all primary key columns of the row + Size of data in attribute columns that you want to update)/4 KB. If UpdateRow contains an attribute column that you want to delete, the length of the column name is calculated as the size of data in the column. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is rounded up from the calculation result of the formula that is used when the value of the condition parameter is IGNORE. The number of consumed read CUs is rounded up from the calculation result of the following formula: Number of consumed read CUs = Size of data in all primary key columns of the row/4 KB. If the request times out and the results are undefined, CUs may or may not be consumed. If an HTTP status code 5xx is returned, which indicates that an internal error occurred, the operation does not consume CUs. If other errors are returned, one read CU and one write CU are consumed.

#### DeleteRow

Deletes a row of data. Request syntax

```
message DeleteRowRequest {
    required string table_name = 1;
    required bytes primary_key = 2; // The primary key is encoded in the PlainBuffer format
```

`.`

```
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table name _ | string | Yes | The name of the data table. |
| primary key _ | bytes | Yes | The primary key of the row that you want to delete. The primary key is encoded in the PlainBuffer format. |
| condition | Condition | Yes | Specifies whether to perform row existence check before a data operation. Default value: IGNORE. Valid values: IGNORE: Row existence check is not performed. If you set condition to IGNORE, the operation is successful regardless of whether the row exists. EXPECT EXIST: The row is expected to exist. _ When you set condition to EXPECT EXIST, the _ delete operation is successful if the row exists, and the delete operation fails and an error is reported if the row does not exist. |
| return content _ | ReturnContent | No | The content that you want to return. Only the primary key can be returned. This parameter is mainly used by the auto-increment primary key column feature. |

Response syntax

```
message DeleteRowResponse {
 required ConsumedCapacity consumed = 1;
 optional bytes row = 2;
```

| Parameter | Type | Description |
|---|---|---|
| consumed | ConsumedCapacit y | The number of capacity units (CUs) that are consumed by the operation. |
| row | bytes | The data that is returned if you specify a value for return content. If you do not specify a value for return content _ _ or no return value exists, NULL is returned. The returned data is encoded in the PlainBuffer format. |

CU consumption If the row that you want to delete does not exist, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = Size of the data in all primary key columns of the row/4 KB. If the value of the condition parameter is EXPECT_EXIST, the row fails to be deleted. One write CU and one read CU are consumed. If the row that you want to delete exists, the number of CUs that are consumed varies based on the value that you specified for the condition parameter. If the value of the condition parameter is IGNORE, the number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = Size of the data in all primary key columns of the row/4 KB. If the value of the condition parameter is EXPECT_EXIST, both write and read CUs are consumed. The number of consumed write CUs is rounded up from the calculation result of the following formula: Number of consumed write CUs = Size of the data in all primary key columns of the row/4 KB. The number of consumed read CUs is rounded up from the calculation result of the following formula: Number of consumed read CUs = Size of the data in all primary key columns of the row/4 KB. If the request times out and the results are undefined, CUs may or may not be consumed. If an HTTP status code 5xx is returned, which indicates that an internal error occurred, the operation does not consume CUs. If other errors are returned, one write CU is consumed.

#### GetRange

Reads data whose primary key is within a specified range. Request syntax

```
message GetRangeRequest {
    required string table_name = 1;
    required Direction direction = 2;
    repeated string columns_to_get = 3; // If you do not specify this parameter, all column
s are read.
    optional TimeRange time_range = 4;
    optional int32 max_versions = 5;
    optional int32 limit = 6;
    required bytes inclusive_start_primary_key = 7; // The primary key is encoded in the Pl
ainBuffer format.
    required bytes exclusive_end_primary_key = 8; // The primary key is encoded in the Plai
nBuffer format.
    optional bytes filter = 10;
    optional string start_column = 11;
    optional string end_column = 12;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table name _ | string | Yes | The name of the table whose data you want to read. |
| direction | Direction | Yes | The order in which you want to sort the rows in the response. If you set this parameter to FORWARD, the value of the inclusive start primary parameter must be _ _ smaller than the value of the exclusive end primary parameter, and the rows in _ _ the response are sorted in ascending order of primary key values. If you set this parameter to BACKWARD, the value of the inclusive start primary parameter must be _ _ greater than the value of the exclusive end primary parameter, and the rows in _ _ the response are sorted in descending order of primary key values. |
| columns to g _ _ et | repeated string | No | The names of the columns that you want to return. If you do not specify this parameter, all columns of the rows are returned. The value of this parameter can contain up to 128 strings. If duplicate column names exist, the response includes the column only once. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| time range _ | TimeRang | No. Only one of max versions _ and time range is _ required. | The timestamp range of the data that you want to read. The minimum value is 0, and the maximum value is INT64.MAX. Unit: milliseconds. If you want to query the data within a specified time range, specify start time and end time. If you want _ _ to query the data with a specified timestamp, specify specific time. _ For example, if the value of time range is [100,200), _ the timestamp of the data in the returned columns must be within the range of [100,200). |
| max versions _ | int32 | No. Only one of max versions _ and time range is _ required. | The maximum number of versions of data that you want to return. For example, if the value of max versions is 2, a _ maximum of two versions of data is returned for each column. |
| limit | int32 | No | The maximum number of rows that you want to return. If the number of rows that meet the query conditions exceeds the value of this parameter, the response contains a breakpoint that records the position at which the read operation ends. The next read operation starts from this position. The value of this parameter must be greater than 0. Tablestore returns up to 5,000 rows of data regardless of whether you specify this parameter. The total size of returned rows cannot exceed 4 MB. |
| inclusive start _ primary key _ _ | bytes | Yes | The primary key from which the read operation starts. The start primary key is encoded in the PlainBuffer format. If the primary key of a row in the table from which you want to read data is the same as the start primary key, the row is included in the response. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| exclusive end _ _ primary key _ | bytes | Yes | The primary key at which the read operation ends. The end primary key is encoded in the PlainBuffer format. If the primary key of a row is the same as the end primary key, the row is not included in the response regardless of whether the row is in the table from which you want to read data. For the GetRange operation, the primary key columns in the values of inclusive start primary key _ _ _ and exclusive end primary key can be one of the _ _ _ following types dedicated to this operation: INF MIN and INF MAX. If the type of a primary key _ _ column in the start primary key or end primary key is INF MIN, the value of the column in the start primary _ key or end primary key is smaller than the value of the column in other primary keys. If the type of a primary key column in the start primary key or end primary key is INF MAX, the value of the column in _ the start primary key or end primary key is greater than the value of the column in other primary keys. |
| filter | bytes | No | The expression of the filter condition, which is serialized as binary data by using Protobuf. |
| start column _ | string | No | The column from which the read operation starts in a row. This parameter is used to read wide columns. The response contains the specified start column. The columns are sorted based on their names in alphabetical order. For example, if a table contains columns a, b, and c, and the value of start column is b, the read _ operation starts from column b, and columns b and c are returned. |
| end column _ | string | No | The column at which the read operation ends in a row. This parameter is used to read wide columns. The response does not contain the specified end column. The columns are sorted based on their names in alphabetical order. For example, if a table contains columns a, b, and c, and the value of end column is b, the read _ operation ends at column b, and only column a is returned. |

Response syntax

```
message GetRangeResponse {
    required ConsumedCapacity consumed = 1;
    required bytes rows = 2;
    optional bytes next_start_primary_key = 3;
```

| Parameter | Type | Description |
|---|---|---|
| consumed | ConsumedCapacit y | The number of capacity units (CUs) that are consumed by the operation. |
| rows | bytes | The rows that are returned by the operation. The rows are encoded in the PlainBuffer format. If direction in the request is set to FORWARD, the rows in the response are sorted in ascending order of primary key values. If direction in the request is set to BACKWARD, the rows in the response are sorted in descending order of primary key values. The primary key columns and attribute columns for each row in the response contain only the columns that you specified for columns to get in the request. The order of the columns for _ _ columns to get in the response may be different from the _ _ order of the columns that you specified for columns to get in _ _ the request. The order of the primary key columns in the response may be different from the order of the primary key columns when the table is created. If the value of the columns to get parameter in the request _ _ does not contain a primary key column, rows that do not contain one or more attribute columns specified in columns to get are not included in the response even if the _ _ primary key of the rows is within the query range. |

| Parameter | Type | Description |
|---|---|---|
| next start primary _ _ key _ | bytes | The breakpoint that records the position at which the read operation ends. The breakpoint is encoded in the PlainBuffer format. If this parameter is left empty, the GetRange operation returns all rows that meet the query conditions. If this parameter is not left empty, the GetRange operation returns only the data within the range of [inclusive start primary key, next start primary key). If you _ _ _ _ _ _ want to obtain the remaining data, set inclusive start primary key to the value of _ _ _ next start primary key and retain the value of _ _ _ exclusive end primary key in the original request to call the _ _ _ GetRange operation again. Not e The GetRange operation can return up to 5,000 rows upon each request. The total size of the data in the rows cannot exceed 4 MB. The response to a GetRange request may contain a value of the next start primary key _ _ _ parameter even if you do not specify a limit in the request. When you call the GetRange operation, you must check whether the response contains the next start primary key _ _ _ parameter. |

CU consumption The number of read CUs that are consumed for the GetRange operation is rounded up from the calculation result of the following formula: Number of consumed read CUs = (Size of the data in all primary key columns of the rows that meet the query conditions + Size of the data in the attribute columns that are read)/4 KB. If the request times out and the results are undefined, CUs may or may not be consumed. If an HTTP status code 5xx is returned, which indicates that an internal error occurred, the operation does not consume CUs. If other errors are returned, one read CU is consumed.

#### BatchGetRow

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

#### BatchWriteRow

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

#### CreateTable

Creates a table based on the specified schema. Usage notes You cannot perform read or write operations on a table immediately after you create the table. In most cases, you can perform read and write operations on a table about one minute after the table is created. You can create up to 1,024 tables in an instance. If you need to create more tables in an instance, contact Alibaba Cloud customer service. Request syntax

```
message CreateTableRequest {
    required TableMeta table_meta = 1;
    required ReservedThroughput reserved_throughput = 2;
    optional TableOptions table_options = 3;
    optional StreamSpecification stream_spec = 5;
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| table meta _ | TableMeta | Yes | The schema of the data table. The table name must be unique within the instance. A primary key can contain one to four primary key columns. You must specify the name and data type of each primary key column. The name of each primary key column must comply with the naming conventions and the data type of each primary key column must be STRING, INTEGER, or BINARY. After you create a table, you cannot modify the schema of the table. |
| reserved through _ put | ReservedThrough put | Yes | The reserved read or write throughput of the data table. The reserved read or write throughput of a table cannot exceed 100,000. Unit: capacity unit (CU). You can call the UpdateTable operation to change the reserved read or write throughput of a data table. |
| table options _ | TableOptions | No | The settings of time to live (TTL) and max versions. |
| stream spec _ | StreamSpecificati on | No | Specifies whether to enable Stream- related attributes. |

Response syntax

```
message CreateTableResponse {
```

#### ListTable

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

#### DeleteTable

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

#### UpdateTable

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

#### DescribeTable

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

#### ComputeSplitPointsBySize

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

#### ListStream

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

#### DescribeStream

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

#### GetShardIterator

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

#### GetStreamRecord

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

#### Tablestore ProtocolBuffer message

definitions This topic describes the detailed definitions of table_store.proto and table_store_filter.proto. table_store.proto

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
message CapacityUnit {
    optional int32 read = 1;
    optional int32 write = 2;
message ReservedThroughputDetails {
    required CapacityUnit capacity_unit = 1; // This parameter indicates the current reserv
```

```
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
message DescribeTableRequest {
    required string table_name = 1;
message DescribeTableResponse {
    required TableMeta table_meta = 1;
    required ReservedThroughputDetails reserved_throughput_details = 2;
```

```
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
    required ConsumedCapacity consumed = 1;
    optional bytes row = 2;
/* ########################################################################################
############*/
```

```
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
message BatchGetRowResponse {
    repeated TableInBatchGetRowResponse tables = 1;
/* ########################################################################################
#################*/
```

```
################# /
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
    required bytes inclusive_start_primary_key = 7; // encoded as InplaceRowChangeSet, but
only has primary key
    required bytes exclusive_end_primary_key = 8; // encoded as InplaceRowChangeSet, but on
ly has primary key
    optional bytes filter = 10;
```

```
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

#### CreateIndex

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

#### DeleteIndex

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

### DataType

#### ActionType

ActionType specifies the operation type in the response of the GetStreamRecord operation. Operation types include: PUT_ROW indicates that the operation type is PutRow. UPDATE_ROW indicates that the operation type is UpdateRow. DELETE_ROW indicates that the operation type is DeleteRow. Enumeration values

```
enum ActionType {
    PUT_ROW = 1;
    UPDATE_ROW = 2;
    DELETE_ROW = 3;
```

#### CapacityUnit

CapacityUnit specifies the number of CUs consumed in an operation, or reserved read/write throughput of a table. Data structure

```
message CapacityUnit {
    optional int32 read = 1;
    optional int32 write = 2;
```

read: Type: int32 Description: the number of read CUs consumed by this operation or the reserved read throughput for this table. writ e: Type: int32 Description: the number of write CUs consumed by this operation or the reserved write throughput for this table.

#### ColumnPaginationFilter

ColumnPaginationFilter specifies the filtering conditions for reading wide rows. This API is applicable to the Filter function. Data structure

```
message ColumnPaginationFilter {
 required int32 offset = 1;
 required int32 limit = 2;
```

of f set : Type: int32 Description: the position of the column to start reading from. limit : Type: int32 Description: the number of columns to be read.

#### ComparatorType

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

#### CompositeColumnValueFilter

CompositeColumnValueFilter specifies a group of conditions, for example, column_a > 5 AND column_b = 10. This API is applicable to the ConditionUpdate and Filter functions. Data structure

```
message CompositeColumnValueFilter {
 required LogicalOperator combinator = 1;
 repeated Filter sub_filters = 2;
```

combinat or: Type: LogicalOperator Description: the logical operator. sub_f ilt er: Type: Filter Description: the sub-condition expression.

#### Condition

Condition specifies the row judgment conditions in PutRow, UpdateRow, and DeleteRow. It contains the row_existence and column_condition parameters. Data structure

```
message Condition {
    required RowExistenceExpectation row_existence = 1;
    optional bytes column_condition      = 2;
```

row_exist ence: Type: RowExistenceExpectation Description: the row existence check settings for this row. column_condit ion: Type: bytes Description: the column condition settings. This parameter indicates the binary data (in bytes) after the filter is serialized in the Protobuf format.

#### ConsumedCapacity

ConsumedCapacity indicates the number of capacity units (CUs) consumed by an operation. Data structure

```
message ConsumedCapacity {
    required CapacityUnit capacity_unit = 1;
```

capacit y_unit : Type: CapacityUnit Description: the number of CUs consumed by this operation.

#### Direction

Direction indicates the data query order in the GetRange operation. The two Direction operations are: FORWARD indicates that the query proceeds in ascending order of primary key values. BACKWARD indicates that the query proceeds in descending order of primary key values. Enumeration values

```
enum Direction {
 FORWARD = 0;
 BACKWARD = 1;
```

#### Error

Error indicates an error message returned when an operation fails. This parameter is also used to indicate errors for single-row requests in the BatchGetRow and BatchWriteRow operations. Data structure

```
Error {
 required string code = 1;
 optional string message = 2;
```

code: Type: string Description: the error code for the specified single-row operation. message: Type: string Description: the error message for the specified single-row operation.

#### Filter

Filter specifies the column-based conditions. This API is applicable to the Conditional Update and Filter functions. Data structure

```
message Filter {
 required FilterType type = 1;
 required bytes filter = 2;
```

t ype: Type: FilterType Description: the column condition type. f ilt er: Type: bytes Description: the binary data generated after the condition statements of CompositeColumnValueFilter, ColumnPaginationFilter, or SingleColumnValueFilter are serialized in the Protobuf format.

#### PrimaryKeyOption

PrimaryKeyOption specifies the attribute value of a primary key. Currently, it only supports AUTO_INCREMENT. Enumeration values

```
enum PrimaryKeyOption {
 AUTO_INCREMENT = 1;
```

#### FilterType

FilterType specifies the type for condition updates or filters. The types include: FT_SINGLE_COLUMN_VALUE indicates a single-column condition. FT_COMPOSITE_COLUMN_VALUE indicates a multi-column composite condition. FT_COLUMN_PAGINATION indicates a wide-row read condition. Enumeration values

```
enum FilterType {
 FT_SINGLE_COLUMN_VALUE = 1;
 FT_COMPOSITE_COLUMN_VALUE = 2;
 FT_COLUMN_PAGINATION = 3;
```

#### LogicalOperator

LogicalOperator specifies the enumeration type. The enumeration types include: LO_NOT indicates NOT. LO_AND indicates AND. LO_OR indicates OR. Enumeration values

```
enum LogicalOperator {
 LO_NOT = 1;
 LO_AND = 2;
 LO_OR = 3;
```

#### OperationType

OperationType indicates the modification method for one column in UpdateRow. The types of operations include: PUT indicates that a column is inserted or data in this column is overwritten. UPDATE indicates that a column is updated. DELETE indicates that a column is deleted. Enumeration values

```
enum OperationType {
 PUT = 1;
 UPDATE = 2;
 DELETE = 3;
```

#### PartitionRange

PartitionRange specifies the partition range. Data structure

```
message PartitionRange {
    required bytes begin = 1; // encoded as SQLVariant
    required bytes end = 2; // encoded as SQLVariant
```

begin: Type: bytes Description: the starting key of the partition. The partition range is a left-closed right-open interval, which includes the starting key. end: Type: bytes Description: the ending key of the partition. The partition range is a left-closed right-open interval, which excludes the ending key.

#### PlainBuffer

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

#### PrimaryKeySchema

PrimaryKeySchema specifies the attribute value of a primary key. Data structure

```
message PrimaryKeySchema {
 required string name = 1;
 required PrimaryKeyType type = 2;
 optional PrimaryKeyOption option = 3;
```

name: Type: string Description: the name of the column. t ype: Type: PrimaryKeyType Description: the type of the column. opt ion: Type: PrimaryKeyOption Description: the additional attribute value of the column.

#### PrimaryKeyType

PrimaryKeyType specifies the type of a primary key. Enumeration data types INTEGER STRING BINARY

```
enum PrimaryKeyType {
 INTEGER = 1;
 STRING = 2;
 BINARY = 3;
```

#### ReservedThroughput

ReservedThroughput indicates the reserved read/write throughput value for a table. Data structure

```
message ReservedThroughput {
 required CapacityUnit capacity_unit = 1;
```

capacit y_unit : Type: CapacityUnit Description: the current reserved read/write throughput value for the table.

#### ReservedThroughputDetails

ReservedThroughputDetails indicates the reserved read/write throughput information of a table. Data structure

```
message ReservedThroughputDetails {
    required CapacityUnit capacity_unit = 1;
    required int64 last_increase_time = 2;
    optional int64 last_decrease_time = 3;
    required int32 number_of_decreases_today = 4;
```

capacit y_unit : Type: CapacityUnit Description: the reserved read/write throughput value for this table. last _increase_t ime: Type: int64 Description: the last time the reserved read/write throughput capacity was raised for this table. The value uses UTC time, in seconds. last _decrease_t ime: Type: int64 Description: the last time the reserved read/write throughput capacity was lowered for this table. The value uses UTC time, in seconds. number_of _decreases_t oday: Type: int32 Description: the number of times the reserved read/write throughput capacity was lowered for this table on the current calendar day.

#### ReturnContent

ReturnContent specifies the content of the returned data. Data structure

```
message ReturnContent {
    optional ReturnType return_type = 1;
```

ret urn_t ype: Type: ReturnType Description: the type of the returned data.

#### ReturnType

ReturnType specifies the type of the returned data. Enumeration data types

```
enum ReturnType {
    RT_NONE = 0;
    RT_PK = 1;
```

RT_NONE: the default value. This parameter indicates that no value is returned. RT_PK: This parameter indicates that the primary key is returned.

#### RowExistenceExpectation

RowExistenceExpectation specifies conditions for row existence. Enumeration types are as follows: IGNORE indicates that the row existence check is not performed. EXPECT_EXIST indicates that the row is expected to exist. EXPECT_NOT_EXIST indicates that this row is not expected to exist. Enumeration values

```
enum RowExistenceExpectation {
    IGNORE = 0;
    EXPECT_EXIST = 1;
    EXPECT_NOT_EXIST = 2;
```

#### RowInBatchGetRowResponse

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

#### RowInBatchWriteRowRequest

RowInBatchWriteRowRequest indicates the information of the row to be written, updated, or deleted in the BatchWriteRow operation. Data structure

```
message RowInBatchWriteRowRequest {
    required OperationType type = 1;
    required bytes row_change = 2; // It is encoded as InplaceRowChangeSet.
    required Condition condition = 3;
    optional ReturnContent return_content = 4;
```

t ype: Type: OperationType Description: the operation type. row_change: Type: bytes Description: the data in a row that contains the primary key and attribute columns. The columns are encoded in the PlainBuffer format. condit ion: Type: Condition Description: the value of conditional update, including the row existence condition and columnbased condition. ret urn_cont ent : Type: ReturnContent Required: no This parameter specifies the data type after the row is written. Currently, only the primary key is returned, which is used for the auto-increment function of the primary key column.

#### RowInBatchWriteRowResponse

RowInBatchWriteRowResponse indicates the write operation result for a row in the response of the BatchWriteRow operation. Data structure

```
message RowInBatchWriteRowResponse {
 required bool is_ok = 1 [default = true];
 optional Error error = 2;
 optional ConsumedCapacity consumed = 3;
```

is_ok: Type: bool Description: determines whether the operation for this row succeeds. If the value is true, the row is written and error is invalid. If the value is false, this row fails to be written. error: Type: Error Description: the error message for this row operation. consumed: Type: ConsumedCapacity Description: the number of capacity units consumed by this row operation.

#### SingleColumnValueFilter

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

#### StreamDetails

StreamDetails indicates the stream information of a table. Data structure

```
message StreamDetails {
    required bool enable_stream = 1;
    optional string stream_id = 2;
    optional int32 expiration_time = 3;
    optional int64 last_enable_time = 4;
```

enable_st ream: Type: required bool Description: determines whether stream is enabled for the table. st ream_id: Type: optional string Description: the ID of the table stream. expirat ion_t ime: Type: optional int32 Description: the expiration time of the table stream. last _enable_t ime: Type: optional int64 Description: the time to enable the table stream.

#### StreamRecord

StreamRecord indicates a row of data in the response of the GetStreamRecord operation. Data structure

```
 message StreamRecord {
        required ActionType action_type = 1;
        required bytes record = 2;
```

act ion_t ype: Type: required ActionType Description: the operation type of the row. record: Type: required bytes Description: the data content of the row.

#### StreamSpecification

StreamSpecification indicates the stream specification of a table. Data structure

```
message StreamSpecification {
    required bool enable_stream = 1;
    optional int32 expiration_time = 2;
```

enable_st ream: Type: bool Description: determines whether stream is enabled for the table. expirat ion_t ime: Type: int32 Description: the expiration time of the table stream.

#### TableInBatchGetRowRequest

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

#### TableInBatchGetRowResponse

TableInBatchGetRowResponse indicates data in a table in the response of the BatchGetRow operation. Data structure

```
message TableInBatchGetRowResponse {
 required string table_name = 1;
 repeated RowInBatchGetRowResponse rows = 2;
```

t able_name: Type: string Description: the name of the table. rows: Type: repeated RowInBatchGetRowResponse Description: data of all rows read from the table.

#### TableInBatchWriteRowRequest

TableInBatchWriteRowRequest indicates the request information of the table to be written in the BatchWriteRow operation. Data structure

```
message TableInBatchWriteRowRequest {
 required string table_name = 1;
 repeated RowInBatchWriteRowRequest rows = 2;
```

t able_name: Type: string Description: the name of the table. rows: Type: repeated RowInBatchWriteRowRequest Description: the information of the row to be inserted, updated, or deleted in the table.

#### TableInBatchWriteRowResponse

TableInBatchWriteRowResponse indicates the write results for a table in the BatchWriteRow operation. Data structure

```
message TableInBatchWriteRowResponse {
 required string table_name = 1;
 repeated RowInBatchWriteRowResponse put_rows = 2;
 repeated RowInBatchWriteRowResponse update_rows = 3;
 repeated RowInBatchWriteRowResponse delete_rows = 4;
```

t able_name: Type: string Description: the name of the table. put _rows: Type: RowInBatchWriteRowResponse Description: the result of the PutRow operation for the table. updat e_rows: Type: RowInBatchWriteRowResponse Description: the result of the UpdateRow operation for the table. delet e_rows: Type: RowInBatchWriteRowResponse Description: the result of the DeleteRow operation for the table.

#### TableMeta

TableMeta indicates the structure information of a table. Data structure

```
message TableMeta {
 required string table_name = 1;
 repeated PrimaryKeySchema primary_key = 2;
```

t able_name: Type: string. Description: the name of the table. primary_key: Type: PrimaryKeySchema Description: all primary key columns of the table.

#### TableOptions

TableOptions indicates the table parameters, including TimeToLive and MaxVersions. Data structure

```
message TableOptions {
    optional int32 time_to_live = 1; // This parameter value can be dynamically modified.
    optional int32 max_versions = 2; // This parameter value can be dynamically modified.
    optional int64 deviation_cell_version_in_sec = 5; // This parameter value can be dynami
cally modified.
```

t ime_t o_live: Type: int32 Description: the retention time of data stored in this table, in seconds. max_versions: Type: int32 Description: the maximum number of versions stored in this table. deviat ion_cell_version_in_sec: Type: int64 Description: the maximum version deviation. This parameter is used to forbid writing data that deviates from the expected output. For example, if the value of deviation_cell_version_in_sec is 1,000 and the current timestamp is 10,000, the allowed timestamp range to be written is [10,000 - 1,000, 10,000 + 1,000].

#### TimeRange

TimeRange specifies the timestamp range or timestamp value to query. Data structure

```
message TimeRange {
    optional int64 start_time = 1;
    optional int64 end_time = 2;
    optional int64 specific_time = 3;
```

st art _t ime: Type: int64 Description: the starting timestamp, in milliseconds. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX. end_t ime: Type: int64 Description: the ending timestamp, in milliseconds. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX. specif ic_t ime: Type: int64 Description: the specific timestamp, in milliseconds. You can set either specific_time to query a specific timestamp, or a combination of start_time and end_time to query a range of timestamps. The minimum value of the timestamp is 0. The maximum value of the timestamp is INT64.MAX.

## SDK reference

### Java SDK

#### Overview

This topic describes how to use Tablestore SDK for Java. This topic applies to Tablestore SDK for Java V5.0.0 or later. Prerequisites An authorized account is created, and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. Compatibility Latest version: 5.13.5 Tablestore SDK for Java V4.x.x: compatible. Tablestore SDK for Java V2.x.x: incompatible.

#### Installation

This topic describes the prerequisites, version compatibility, and versions of Tablestore SDK for Java. This topic applies to Tablestore SDK for Java V5.0.0 or later. Prerequisites JDK 6.0 or later is available. Installation methods You can install Tablestore SDK for Java by using one of the following two methods: Add dependencies to a Maven project To use Tablestore SDK for Java in Maven, you need to only add the corresponding dependencies to the pom.xml file. In this example, Tablestore SDK for Java V5.13.5 is used. Add the following content to <dependencies>:

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
    <artifactId>tablestore</artifactId>
    <version>5.13.5</version>
</dependency>
```

Import the JAR package into Eclipse In this example, Tablestore SDK for Java V5.13.5 is used. To import the JAR package into Eclipse, perform the following steps: i. Download the Tablestore SDK for Java package. ii. Decompress the Tablestore SDK for Java package. iii. Copy the tablestore-<versionId>.jar file and all files in the lib folder to your project. <versionId> specifies the version of Tablestore SDK for Java. For example, the file name for V5.13.5 is tablestore-5.13.5.jar. iv. Right-click your project name in Eclipse and choose Propert ies > Java Build Pat h > Add JARs. v. Select all JAR files that you copied in Step 3. Sample programs Tablestore SDK for Java provides a variety of sample programs for your reference or use. You can decompress the downloaded SDK package and view the sample programs in the examples folder.

#### Initialization

OTSClient is a client for Tablestore. OTSClient provides various methods that you can use to manage tables and perform read and write operations on a single row or multiple rows. Before you can use Tablestore SDK for Java to send a request, you must initialize an OTSClient instance and modify the default configurations of ClientConfiguration. Obtain an endpoint An endpoint is a domain name that is used to access a Tablestore instance in a region. The following table describes the examples of endpoints in the supported formats.

| Example | Description |
|---|---|
| http://sun.cn-hangzhou.ots.aliyuncs.com | The public endpoint that is used to access the sun instance in the China (Hangzhou) region over HTTP. |
| https://sun.cn-hangzhou.ots.aliyuncs.com | The public endpoint that is used to access the sun instance in the China (Hangzhou) region over HTTPS. |

Not e You can connect to Tablestore by using public endpoints or private endpoints. To query the endpoints of your Tablestore instance, perform the following steps:
1. Log on to the Tablestore console.
2. Click the name of the instance to go to the Inst ance Det ails tab.
On the Instance Details tab, you can view the endpoints of the instance in Instance Access URL. Initialize a Tablestore instance After you obtain the AccessKey ID and AccessKey secret, you can perform the following steps to initialize a Tablestore instance: Create a client If you want to use the Tablestore SDK, you must create a client and call the operations in the client to access Tablestore. The operations in the client provide the same functions as the RESTful APIs provided by Tablestore. The Tablestore SDK provides the following clients: SyncClient and AsyncClient. SyncClient contains synchronous operations and AsyncClient contains asynchronous operations. If you call a synchronous operation, the operation directly returns a response, which indicates that the request is executed. You can call synchronous operations to obtain information about various features of Tablestore. Compared with synchronous operations, asynchronous operations are more flexible. Multithreading provides higher performance than asynchronous operations. You can choose asynchronous operations or multithreading based on your business requirements. Not e SyncClient and AsyncClient are thread-safe. You can use the clients to manage internal threads and connection resources. We recommend that you create a global client. This way, you do not need to create a client for each thread or request. Sample code Use the default configurations to create a SyncClient

```
final String endPoint = ""; final String accessKeyId = ""; final String accessKeySecret = ""; final String instanceName = ""; SyncClient client = new SyncClient(endPoint, accessKeyId, accessKeySecret, instanceName);
```

Use the custom configurations to create a SyncClient

```
// ClientConfiguration provides multiple configuration items. Only the most commonly used items are listed. ClientConfiguration clientConfiguration = new ClientConfiguration(); // Specify a timeout period during which a connection can be established. clientConfiguration.setConnectionTimeoutInMillisecond(5000); // Specify a timeout period for the socket connection. clientConfiguration.setSocketTimeoutInMillisecond(5000); // Specify a retry policy. If you do not specify a retry policy, the default retry policy is used. clientConfiguration.setRetryStrategy(new AlwaysRetryStrategy()); SyncClient client = new SyncClient(endPoint, accessId, accessKey, instanceName, clientCon figuration);
```

HTTPS Upgrade to Java 7 for connection based on HTTPS. Multithreading Multithreading is supported. We recommend that you use the same OTSClient object to run multithreading tasks.

#### Use Tablestore SDK for Java

##### Table-level operations

Tablestore SDK for Java provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable When you create a table in Tablestore, you must specify TableMeta and TableOptions. You can also set ReservedThroughput. Not e After the table is created, Tablestore loads partitions of the table to a specified node. And you can read data from or write data to the table within a few seconds. An exception may occur if you immediately attempt to read from or write to the table after you create the table. TableMeta TableMeta includes the name and primary key schema of the table.

| Parameter | Description |
|---|---|
| TableName | The name of the table. |
| List | The definition of the primary key. The primary key of a table can contain one to four primary key columns. Primary key columns are sorted in the order in which they are added. For example, PRIMARY KEY (A, B, C) and PRIMARY KEY (A, C, B) have different primary key schemas. Tablestore sorts rows based on the values of all primary key columns. The first primary key column serves as the partition key. Data with the same partition key value is stored in the same partition. Therefore, we recommend that you assign no more than 10 GB of data with the same partition key value. Otherwise, individual partitions are too large and cannot be split. We recommend that you distribute requests in an even manner to read and write data to different partition keys for load balancing. Attribute columns are optional. Different rows in Tablestore can have different data columns. The names of attribute columns can be specified when data is written. |

TableOptions

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| TTL | The time to live, which indicates the validity period of data. The system determines whether data expires based on the timestamp, current time, and timeToLive parameters. Data expires and then is deleted if the values of the parameters meet the following formula: current time - timestamp > timeToLive . When you create a table, you can set TTL to -1 if you expect that data never expires. After the table is created, you can call the UpdateTable operation to dynamically modify the TTL value. When you write data configured with TTL, ensure that you specify a valid timestamp. We recommend that you set MaxTimeDeviation when you specify the timestamp. Unit: seconds. |
| MaxTimeDeviation | The maximum offset between the timestamp of written data and the current system time. By default, the system generates a timestamp for new data. The system checks whether data expires based on the timestamp. You can specify the timestamp of written data. When the offset between the timestamp of written data and the current system time is greater than the specified TTL, the written data immediately expires. To solve this problem, set MaxTimeDeviation. When you create a table, Tablestore uses the default value of 86400 if you do not specify a max version offset. After the table is created, you can call the UpdateTable operation to dynamically modify the MaxTimeDeviation value. Unit: seconds. |
| MaxVersions | The maximum number of versions that can be retained for data in attribute columns of the table. When the number of versions of data in attribute columns exceeds the MaxVersions value, Tablestore automatically deletes data of earlier versions. When you create a table, you can customize the maximum number of versions that can be retained for the data in an attribute column. After the table is created, you can call the UpdateTable operation to dynamically modify the MaxVersions value for the table. |

|   | - timestamp > timeToLive |
|---|---|

ReservedThroughput: the reserved read/write throughput configurations of the table. You can set the reserved read and write throughput only to 0 for capacity instances. Reserved throughput does not apply to these instances. Examples

```java
private static void createTable(SyncClient client) {
        TableMeta tableMeta = new TableMeta(TABLE_NAME);
        tableMeta.addPrimaryKeyColumn(new PrimaryKeySchema(PRIMARY_KEY_NAME, PrimaryKeyType
.STRING)); // Specify a primary key column for the base table.
        int timeToLive = -1; // Specify the validity period of data in seconds. A value of
-1 indicates that the data never expires. You must specify -1 as the TTL value when a table has one or more index tables.
        int maxVersions = 1; // Specify the maximum number of versions that can be retained
. You must specify 1 as the maxVersions value when a table has one or more index tables.
        TableOptions tableOptions = new TableOptions(timeToLive, maxVersions);
        CreateTableRequest request = new CreateTableRequest(tableMeta, tableOptions);
        request.setReservedThroughput(new ReservedThroughput(new CapacityUnit(0, 0))); // S
et the reserved read/write throughout. You can set the value only to 0 for capacity instanc es. However, you can set a non-zero value for high-performance instances.
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

##### Single-row operations

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

##### Multi-row operations

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

##### Auto-increment function of the primary key

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

##### Conditional update

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

| ablestore |   | Dev | eloper Guide·SDK referenc |
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

##### Filters

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

##### Global secondary indexes

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

##### Tunnel Service

###### Quick start

This topic describes how to use Tablestore SDK for Java to get start with Tunnel Service. The sample code is provided at the end of this topic. Get started with Tunnel Service Tablestore SDK for Java allows you to use Tunnel Service.
1. Initialize a tunnel client.

```
// Set endPoint to the endpoint of the Tablestore instance. Example: https://instance.c n-hangzhou.ots.aliyuncs.com. // Set accessKeyId to the AccessKey ID and accessKeySecret to the AccessKey secret that you use to access Tablestore. // Set instanceName to the name of the instance. final String endPoint = ""; final String accessKeyId = ""; final String accessKeySecret = ""; final String instanceName = ""; TunnelClient tunnelClient = new TunnelClient(endPoint, accessKeyId, accessKeySecret, in stanceName);
```

2. Create a tunnel.
Create a data table for testing or prepare an existing data table before you create a tunnel. To create a data table for testing, you can use the createTable method in the SyncClient class or go to the Tablestore console.

```java
// You can create three types of tunnels by using TunnelType.BaseData, TunnelType.Strea m, and TunnelType.BaseAndStream. // The following example shows how to create a differential tunnel. To create a tunnel of another type, set TunnelType in CreateTunnelRequest to the type of the tunnel that y ou want to create. final String tableName = "testTable"; final String tunnelName = "testTunnel"; CreateTunnelRequest request = new CreateTunnelRequest(tableName, tunnelName, TunnelType .BaseAndStream); CreateTunnelResponse resp = tunnelClient.createTunnel(request); // Use tunnelId to initialize TunnelWorkers. You can call the ListTunnel or DescribeTun nel operation to obtain the tunnel ID. String tunnelId = resp.getTunnelId(); System.out.println("Create Tunnel, Id: " + tunnelId);
```

3. Customize the data consumption callback to start automatic data consumption.

```java
// Customize the data consumption callback to implement the IChannelProcessor operation . Specify the process and shutdown methods. private static class SimpleProcessor implements IChannelProcessor {
    @Override
    public void process(ProcessRecordsInput input) {
        // ProcessRecordsInput contains the data that you have obtained.
        System.out.println("Default record processor, would print records count");
        System.out.println(
            // NextToken is used to paginate the data of the tunnel client.
            String.format("Process %d records, NextToken: %s", input.getRecords().size(
), input.getNextToken()));
        try {
            // Simulate the processing of data consumption.
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
    @Override
    public void shutdown() {
        System.out.println("Mock shutdown");
// By default, the system starts a thread pool to read and process data based on Tunnel WorkerConfig. A single server starts multiple TunnelWorkers. // We recommend that TunnelWorkers share the same TunnelWorkerConfig. A custom TunnelWo rkerConfig provides more advanced parameters than the default one. TunnelWorkerConfig config = new TunnelWorkerConfig(new SimpleProcessor()); // Configure TunnelWorkers to start automatic data processing. TunnelWorker worker = new TunnelWorker(tunnelId, tunnelClient, config); try {
    worker.connectAndWorking();
} catch (Exception e) {
    e.printStackTrace();
    worker.shutdown();
    tunnelClient.shutdown();
```

Usage notes By default, the system starts a thread pool to read and process data based on TunnelWorkerConfig. A single server starts multiple TunnelWorkers. We recommend that TunnelWorkers share the same TunnelWorkerConfig. If you create a differential tunnel to consume full and incremental data, the incremental data logs of the tunnel are retained for up to seven days. The specific expiration time of incremental data logs is consistent with that of Stream logs of the data table. If the tunnel does not consume all full data within seven days, an OTSTunnelExpired error occurs when the tunnel starts to consume incremental data. As a result, the tunnel cannot consume incremental data. A TunnelWorker requires time to warm up for initialization. The heartbeatIntervalInSec parameter in TunnelWorkerConfig specifies the time that is required for the TunnelWorker to warm up. You can use the setHeartbeatIntervalInSec method in TunnelWorkerConfig to set this parameter. The default value is 30s. The minimum value is 5s. For more information, see Configure tunnel clients. When a tunnel switches from a full channel to an incremental channel, the full channel is closed and the incremental channel is started. This process requires a period of time for initialization. The heartbeatIntervalInSec parameter in TunnelWorkerConfig specifies the time required for initialization. When the TunnelWorker client is shut down due to an unexpected exit or manual termination, the TunnelWorker uses one of the following methods to automatically reclaim resources: 1. Release the thread pool. 2. Automatically call the shutdown method that you have registered for channels. 3. Shut down the tunnel. Sample code

```java
import com.alicloud.openservices.tablestore.TunnelClient; import com.alicloud.openservices.tablestore.model.tunnel.CreateTunnelRequest; import com.alicloud.openservices.tablestore.model.tunnel.CreateTunnelResponse; import com.alicloud.openservices.tablestore.model.tunnel.TunnelType; import com.alicloud.openservices.tablestore.tunnel.worker.IChannelProcessor; import com.alicloud.openservices.tablestore.tunnel.worker.ProcessRecordsInput; import com.alicloud.openservices.tablestore.tunnel.worker.TunnelWorker; import com.alicloud.openservices.tablestore.tunnel.worker.TunnelWorkerConfig; public class TunnelQuickStart {
    private static class SimpleProcessor implements IChannelProcessor {
        @Override
        public void process(ProcessRecordsInput input) {
            System.out.println("Default record processor, would print records count");
            System.out.println(
                // NextToken is used to paginate the data of the tunnel client.
                String.format("Process %d records, NextToken: %s", input.getRecords().size(
), input.getNextToken()));
            try {
                // Simulate the processing of data consumption.
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
        @Override
        public void shutdown() {
            System.out.println("Mock shutdown");
    public static void main(String[] args) throws Exception {
        //1.Initialize a tunnel client.
        final String endPoint = "";
        final String accessKeyId = "";
        final String accessKeySecret = "";
        final String instanceName = "";
        TunnelClient tunnelClient = new TunnelClient(endPoint, accessKeyId, accessKeySecret
, instanceName);
        //2.Create a tunnel. You must create a data table before you create a tunnel. To cr
eate a data table, you must use the createTable method in the SyncClient class or go to the Tablestore console.
        final String tableName = "testTable";
        final String tunnelName = "testTunnel";
```

`l` `l` `(` `bl` `l` `l`

```java
        CreateTunnelRequest request = new CreateTunnelRequest(tableName, tunnelName, Tunnel
Type.BaseAndStream);
        CreateTunnelResponse resp = tunnelClient.createTunnel(request);
        // Use tunnelId to initialize TunnelWorkers. You can call the ListTunnel or Describ
eTunnel operation to obtain the tunnel ID.
        String tunnelId = resp.getTunnelId();
        System.out.println("Create Tunnel, Id: " + tunnelId);
        //3.Customize the data consumption callback to start automatic data consumption.
        // A custom TunnelWorkerConfig provides more advanced parameters than the default o
ne.
        TunnelWorkerConfig config = new TunnelWorkerConfig(new SimpleProcessor());
        TunnelWorker worker = new TunnelWorker(tunnelId, tunnelClient, config);
        try {
            worker.connectAndWorking();
        } catch (Exception e) {
            e.printStackTrace();
            worker.shutdown();
            tunnelClient.shutdown();
```

###### Configure tunnel clients

Tunnel Service is built on the Tablestore API to provide tunnels that are used to consume data in full, incremental, and differential modes. After you create a tunnel for a data table, you can use the tunnel to consume historical and incremental data in the data table. A tunnel client is the automatic data consumption framework of Tunnel Service. The tunnel client detects heartbeats to perform the following operations: Detect active channels. Update the status of channels and channel connections. Initialize, run, and terminate data processing tasks. TunnelWorkerConfig allows you to configure custom parameters for a tunnel client based on your business requirements. The following table describes the parameters.

| Configuration item | Parameter | Description |
|---|---|---|
| Configure the interval to detect heartbeats and the timeout period to receive heartbeats | heartbeatTimeoutInSec | The timeout period to receive heartbeats. Default value: 300. Unit: seconds. When a heartbeat timeout occurs, the tunnel server considers that the current tunnel client is unavailable. The tunnel client must attempt to reconnect to the tunnel server. |

| Configuration item | Parameter | Description |
|---|---|---|
| Configure the interval to detect heartbeats and the timeout period to receive heartbeats | heartbeatIntervalInSec | The interval to detect heartbeats. You can detect heartbeats to detect active channels, update the status of channels, and automatically initialize data processing tasks. Default value: 30. Minimum value: 5. Unit: seconds. |
| Interval between checkpoints | checkpointIntervalInMilli s | The interval between checkpoints when data is consumed. The interval is recorded on the tunnel server. Default value: 5000. Unit: ms. Not e Data to read is stored in different servers. Various errors may occur when you run processes. For example, the server may restart due to environmental factors. The tunnel server regularly records checkpoints after data is processed. Therefore, a task can process data starting from the previous checkpoint after the task is restarted. In some conditions, Tunnel Service may sequentially synchronize data once or multiple times. If some data is reprocessed, we recommend that you optimize your business logic. To prevent data from being reprocessed when errors occur, record more checkpoints. However, an excessive number of checkpoints may compromise the system throughput. We recommend that you record the checkpoints based on your business requirements. |
| The client tag | clientTag | The custom client tag that is used to generate a tunnel client ID. You can configure this parameter to identify TunnelWorkers. |
| The custom callback that is used to process data | channelProcessor | The callback that you register to process data, including the process and shutdown methods. |
| The configuration of the thread pool to read and process data | readRecordsExecutor | The thread pool to read data. If you do not have special requirements, use the default configuration. |
|   |   | The thread pool to process data. If you do not have special requirements, use the default configuration. |

| ablestore |   | Developer Guide·SDK referenc |   |   |
|---|---|---|---|---|
| Configuration item | Parameter |   | Description Not e |   |
| The configuration of the thread pool to read and process data | processRecordsExecutor | When you configure the thread pool, we recommend that you set the number of threads to the number of the channels in the tunnel. This way, each channel can be quickly allocated with computing resources such as CPUs. Tablestore performs the following operations for the default configurations of the pool to ensure throughput: Allocate 32 core threads in advance to guarantee real-time throughput when a small amount of data or a small number of channels exist. Reduce the queue length when a large amount of data must be processed or when a large number of channels exist. This way, the policy is triggered to create a thread in the pool and quickly allocate more computing resources. We recommend that you set the thread keep-alive time to 60s. If the amount of data that must be processed is reduced, you can recycle thread resources. | When you configure the thread pool, we recommend that you set the number of threads to the number of the channels in the tunnel. This way, each channel can be quickly allocated with computing resources such as CPUs. Tablestore performs the following operations for the default configurations of the pool to ensure throughput: Allocate 32 core threads in advance to guarantee real-time throughput when a small amount of data or a small number of channels exist. Reduce the queue length when a large amount of data must be processed or when a large number of channels exist. This way, the policy is triggered to create a thread in the pool and quickly allocate more computing resources. We recommend that you set the thread keep-alive time to 60s. If the amount of data that must be processed is reduced, you can recycle thread resources. |   |

| Configuration item | Parameter | Description |
|---|---|---|
| Memory control | maxChannelParallel | The concurrency level of channels to read and process data for memory control. The default value is -1, which indicates that the concurrency level is unlimited. Not e This configuration applies only to Tablestore SDK for Java V5.4.0 or later. |
| Maximum backoff time | maxRetryIntervalInMillis | The reference value that is used to calculate the maximum backoff time for the tunnel. Default value: 2000 ms. Minimum value: 200 ms. The maximum backoff time is a random number based on the reference value. Valid values: 0.75 × maxRetryIntervalInMillis to 1.25 × maxRetryIntervalInMillis. Not e This configuration applies only to Tablestore SDK for Java V5.4.0 or later. If the amount of data that must be processed is smaller than 900 KB or 500 pieces for each export, the tunnel client uses exponential backoff for the tunnel until the maximum backoff time is reached. |

###### Create tunnels

You can call the CreateTunnel operation to create one or more tunnels for a data table. When you create a tunnel, you must specify the data table name, tunnel name, and tunnel type. Request parameters

| Parameter | Description |
|---|---|
| TableName | The name of the data table for which you want to create a tunnel. |
| TunnelName | The name of the tunnel. |
| TunnelType | The type of the tunnel. Valid values: BaseData, Stream, and BaseAndStream. |

Response parameters

| Parameter | Description |
|---|---|
| TunnelId | The ID of the tunnel. |
| ResponseInfo | Other returned fields. |
| RequestId | The ID of the request. |

Example

```java
// You can create three types of tunnels by using TunnelType.BaseData, TunnelType.Stream, a nd TunnelType.BaseAndStream. // The following code provides an example on how to create a full tunnel. To create a tunne l of another type, set TunnelType in CreateTunnelRequest to the type of the tunnel that you want to create. private static void createTunnel(TunnelClient client, String tunnelName) {
    CreateTunnelRequest request = new CreateTunnelRequest(TableName, tunnelName, TunnelType
.BaseData);
    CreateTunnelResponse resp = client.createTunnel(request);
    System.out.println("RequestId: " + resp.getRequestId());
    System.out.println("TunnelId: " + resp.getTunnelId());
```

###### Query the tunnel information about a data

table You can call this operation to query the tunnel information about a specified data table. Request parameters

| Parameter | Description |
|---|---|
| TableName | The name of the data table about which you want to query the tunnel information. |

Response parameters

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| List<TunnelInfo> | The details about tunnels, which include the following information: TunnelId: the ID of the tunnel. TunnelType: the type of the tunnel. Valid values: BaseData, Stream, and BaseAndStream. TableName: the name of the data table for which the tunnel is configured. InstanceName: the name of the instance for which the tunnel is configured. Stage: the stage at which the tunnel stays. Valid values: InitBaseDataAndStreamShard, ProcessBaseData, and ProcessStream. Expired: indicates whether the data expires. If true is returned, contact Tablestore technical support through DingTalk. |
| ResponseInfo | Other returned fields. |
| RequestId | The ID of the request. |

Example

```java
private static void listTunnel(TunnelClient client, String tableName) {
    ListTunnelRequest request = new ListTunnelRequest(tableName);
    ListTunnelResponse resp = client.listTunnel(request);
    System.out.println("RequestId: " + resp.getRequestId());
    for (TunnelInfo info : resp.getTunnelInfos()) {
        System.out.println("TunnelInfo::::::");
        System.out.println("\tTunnelName: " + info.getTunnelName());
        System.out.println("\tTunnelId: " + info.getTunnelId());
        // The type of the tunnel. Valid values: BaseData, Stream, and BaseAndStream.
        System.out.println("\tTunnelType: " + info.getTunnelType());
        System.out.println("\tTableName: " + info.getTableName());
        System.out.println("\tInstanceName: " + info.getInstanceName());
        // The stage at which the tunnel stays. Valid values: InitBaseDataAndStreamShard, P
rocessBaseData, and ProcessStream.
        System.out.println("\tStage: " + info.getStage());
        // Indicate whether the data expires. If true is returned, contact Tablestore techn
ical support through DingTalk.
        System.out.println("\tExpired: " + info.isExpired());
```

###### Query the information about a tunnel

You can call the DescribeTunnel operation to query information about the channels in a specified tunnel. A channel corresponds to a shard for the Stream operation of Tablestore. Request parameters

| Parameter | Description |
|---|---|
| TableName | The name of the data table about which you want to query the tunnel information. |
| TunnelName | The name of the tunnel. |

Response parameters

| Parameter | Description |
|---|---|
| TunnelConsumePoint | The most recent time when the tunnel consumed incremental data. The value indicates the point in time when the slowest channel in the tunnel consumed data. Default value: January 1, 1970 (UTC). |
| TunnelInfo | The details about the tunnel, which include the following information: TunnelId: the ID of the tunnel. TunnelType: the type of the tunnel. Valid values: BaseData, Stream, and BaseAndStream. TableName: the name of the data table for which the tunnel is configured. InstanceName: the name of the instance for which the tunnel is configured. Stage: the stage at which the tunnel stays. Valid values: InitBaseDataAndStreamShard, ProcessBaseData, and ProcessStream. Expired: indicates whether the data expires. If true is returned, contact Tablestore technical support through DingTalk. |

| Parameter | Description |
|---|---|
| List<ChannelInfo> | The details about channels in the tunnel, which include the following information: ChannelId: the ID of the channel. ChannelType: the type of the channel. Valid values: BaseData and Stream. ChannelStatus: the state of the channel. Valid values: WAIT, OPEN, CLOSING, CLOSE, and TERMINATED. ClientId: the ID of the tunnel client. By default, the client ID concatenates the hostname of the client and a random string. You can customize the client hostname in TunnelWorkerConfig. ChannelConsumePoint: the most recent time when the channel consumed incremental data. Default value: January 1, 1970 (UTC). This parameter is unavailable for full data consumption. ChannelCount: the number of data entries that the channel synchronized. |
| ResponseInfo | Other returned fields. |
| RequestId | The ID of the request. |

Example

```java
// The ConsumePoint and recovery point objective (RPO) attributes are used for incremental data consumption, not for full data consumption. // Incremental tunnel: The Stage parameter in TunnelInfo is set to ProcessStream. Increment al channel: The ChannelType parameter in ChannelInfo is set to Stream. private static void describeTunnel(TunnelClient client, String tableName, String tunnelName ) {
    DescribeTunnelRequest request = new DescribeTunnelRequest(tableName, tunnelName);
    DescribeTunnelResponse resp = client.describeTunnel(request);
    System.out.println("RequestId: " + resp.getRequestId());
    // The most recent time when the tunnel consumed incremental data. The value indicates
the point in time when the slowest channel in the tunnel consumed data. Default value: Janu ary 1, 1970 (UTC).
    System.out.println("TunnelConsumePoint: " + resp.getTunnelConsumePoint());
    System.out.println("TunnelInfo: " + resp.getTunnelInfo());
    for (ChannelInfo ci : resp.getChannelInfos()) {
        System.out.println("ChannelInfo::::::");
        System.out.println("\tChannelId: " + ci.getChannelId());
        // The type of the channel. Valid values: BaseData and Stream.
        System.out.println("\tChannelType: " + ci.getChannelType());
        // The ID of the tunnel client. By default, the client ID concatenates the hostname
of the client and a random string.
        System.out.println("\tClientId: " + ci.getClientId());
        // The most recent time when the channel consumed incremental data.
        System.out.println("\tChannelConsumePoint: " + ci.getChannelConsumePoint());
        // The number of data entries that the channel synchronized.
        System.out.println("\tChannelCount: " + ci.getChannelCount());
```

###### Delete tunnels

You can call the DeleteTunnel operation to delete a tunnel from a data table by specifying the names of the data table and tunnel. Request parameters

| Parameter | Description |
|---|---|
| TableName | The name of the data table from which you want to delete a tunnel. |
| TunnelName | The tunnel name. |

Response parameters

| Parameter | Description |
|---|---|
| ResponseInfo | Other returned fields. |
| RequestId | The ID of the request. |

Example

```java
private static void deleteTunnel(TunnelClient client, String tableName, String tunnelName)
```

`{`

```java
    DeleteTunnelRequest request = new DeleteTunnelRequest(tableName, tunnelName);
    DeleteTunnelResponse resp = client.deleteTunnel(request);
    System.out.println("RequestId: " + resp.getRequestId());
```

#### Error handling

This topic describes the error handling methods in Tablestore SDK for Java. Methods Tablestore SDK for Python handles errors as exceptions. If an operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions Tablestore SDK for Java has two types of exceptions: OTSClientError and OTSServiceError. Both are inherited from Exception. OTSClientError: an internal SDK exception, such as an invalid parameter value. OTSException: a server error parsed from a server error message. OTSServiceError contains the following parameters: getHttpStatus(): an HTTP status code, such as 200 or 404. getErrorCode(): an error type string returned by Tablestore. getRequestId(): the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help.

### Python SDK

#### Overview

This topic describes how to install and use Tablestore SDK for Python. The content in this topic applies to Tablestore SDK for Python V4.x.x. Prerequisites An authorized account is created, and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for Python You can download Tablestore SDK for Python on GitHub. Compatibility Tablestore SDK for Python V5.x.x: compatible. Tablestore SDK for Python V4.x.x: compatible. Tablestore SDK for Python V2.x.x: incompatible. Tablestore SDK for Python V2.x.x supports primary key columns in random order, which are no longer supported in Tablestore SDK for Python V4.0.0 or later. Compared with Tablestore SDK for Python V2.x.x, the following changes are made to Tablestore SDK for Python V4.x.x or later: The package name is changed from ots2 to tablestore. The TableOptions parameter is added for the Client.create_table operation. The type of the primary_key parameter is changed from dict to list for the put_row, get_row, and update_row operations to ensure the sequence of primary key columns. The type of the attribute_columns parameter is changed from dict to list for the put_row and update_row operations. The timestamp parameter is added to the attribute_columns parameter for the put_row and update_row operations. The max_version and time_range parameters are added for the get_row and get_range operations. You must specify at least one of max_version and time_range. The return_type parameter is added for the put_row, update_row, and delete_row operations. Only RT_PK is supported to return the primary key value of the current row. The return_row parameter is added for the put_row, update_row, and delete_row operations. If you set return_type to RT_PK in the request, the primary key value of the row is returned in return_row. Version Latest version: 5.2.1.

#### Installation

This topic describes how to install Tablestore SDK for Python. Prerequisites Python 2 or Python 3 is available. Installation Method 1: Use pip Run the following command to install Tablestore SDK for Python:

```python
sudo pip install tablestore
```

Method 2: Use GitHub Make sure that you have installed Git. For more information about how to download Git, visit Git. After Git is installed, run the following command:

```python
git clone https://github.com/aliyun/aliyun-tablestore-python-sdk.git sudo python setup.py install
```

Method 3: Use source code i. Download the SDK package. ii. Decompress the SDK package. Then, run the following command:

```python
sudo python setup.py install
```

Verify Tablestore SDK for Python To check the SDK version in the Python environment, enter python on the command line and press Enter.

```
>>> import tablestore >>> tablestore.__version__ '5.1.0'
```

Uninstall Tablestore SDK for Python Run the following command to uninstall Tablestore SDK for Python by using pip:

```python
sudo pip uninstall tablestore
```

#### Initialization

OTSClient is a client for Tablestore. OTSClient provides various methods that you can use to perform operations on tables, a single row, and multiple rows. Obtain an endpoint An endpoint is the domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following operations:
1. Log on to the Tablestore console.
2. Click the name of the instance to go to the Inst ance Det ails tab.
On the Instance Details tab, you can view the endpoints of the instance in the Instance Access URL section. Initialize a Tablestore instance To access Apsara Stack Tablestore, you must have a valid AccessKey pair that consists of an AccessKey ID and an AccessKey secret for signature authentication. After you obtain an AccessKey pair, you can perform the following steps to initialize a Tablestore instance by using an endpoint: API operation

```python
""" Initialize the OTSClient instance. end_point specifies the endpoint used to access the Tablestore instance, which must start with https://. Example: https://instance.cn-hangzhou.ots.aliyun.com:80 access_key_id specifies the AccessKey ID that is used to access the Tablestore instance. To obtain an AccessKey ID, visit the official website of Alibaba Cloud or contact an admi nistrator. access_key_secret specifies the AccessKey secret that is used to access the Tablestore in stance. To obtain an AccessKey secret, visit the official website of Alibaba Cloud or con tact an administrator. instance_name specifies the name of the instance that you want to access. You can create an instance in the Tablestore console or contact an administrator to obtain the name of a n existing instance. sts_token specifies the STS token that is used to access the Tablestore instance. You can use Alibaba Cloud STS to obtain an STS token. The STS token has a validity period. You mu st obtain a new token if the existing token expires. encoding specifies the method that is used to encode the request parameter string. The de fault value is utf8. socket_timeout specifies the timeout period in seconds for each socket connection in the connection pool. It can be an integer or a float number. Default value: 50. max_connection specifies the maximum number of connections in a connection pool. Default value: 50. logger_name is used to display the DEBUG log in the request or display the ERROR log when an error occurs. retry_policy defines the retry policy. The default retry policy is DefaultRetryPolicy. Yo u can define a retry policy based on a RetryPolicy class. For more information, see the c ode in DefaultRetryPolicy. """ class OTSClient(object):
    def __init__(self, endpoint, access_key_id, access_key_secret, instance_name, **kwarg
s):
```

Sample code

```bash
#########    Configure the name of the log file and retry policy.     #########
# The name of the log file is table_store.log. The retry policy is WriteRetryPolicy, whic
h defines the retry attempts to write data to the table when a write operation fails. ots_client = OTSClient('endpoint', 'access_key_id', 'access_key_secret', 'instance_name', logger_name = 'table_store.log', retry_policy = WriteRetryPolicy())
#########    Use STS     #########
ots_client = OTSClient('endpoint', 'STS.K8h*******GB77', 'CkuDj******Wn6', 'instance_name ', sts_token = 'CAISjgJ1q6Ft5B2y********OFcsLLuw==')
```

HTTPS HTTPS is supported in Tablestore SDK for Python V2.0.8 or later. OpenSSL 0.9.8j or later is required. We recommend that you use OpenSSL 1.0.2d. The Tablestore SDK for Python V2.0.8 release package contains a certifi package that can be installed and used. To update the root certificate, download the latest root certificate from Root Certificate.

#### Use the SDK

##### Table-level operations

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

Examples The following code provides an example on how to create a table. In this example, a table that contains two primary key columns is created. time_to_live is set to 31,536,000 seconds (one year), max_version to 3, max_time_deviation to 86,400 seconds (one day), and reserved_throughput to (0,0).

```bash
    # Create a schema for the primary key columns, including the quantity, names, and dat
a types of primary keys.
    # The first primary key column is of the integer type and named pk0. The first primar
y key column is partition key.
    # The second primary key column is of the integer type and named pk1. The data type i
s specified as integer in this example. You can also set the data type to string or binar
```

`y.`

```bash
    schema_of_primary_key = [('pk0', 'INTEGER'), ('pk1', 'INTEGER')]
    # Create a table_meta instance based on the table name and the schema of primary key
columns.
    table_meta = TableMeta('SampleTable', schema_of_primary_key)
    # Create a TableOptions instance. Set time_to_live to 31,536,000 seconds (one year) a
nd delete expired data, max_version to 3, and max_time_deviation to 86,400 seconds (one d ay).
    table_options = TableOptions(31536000, 3, 86400)
    # Set both the reserved read throughput and reserved write throughput to 0.
    reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))
    # Call the create_table method of the client. If no exceptions occur, the table is cr
eated. If an exception occurs, the table fails to be created.
    try:
        ots_client.create_table(table_meta, table_options, reserved_throughput)
        print "create table succeeded"
    # If the task fails, an exception is returned and handled.
    except Exception:
        print "create table failed."
```

For the detailed sample code, visit CreateTable@GitHub. ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

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

##### Single-row operations

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

##### Multi-row operations

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

##### Global secondary indexes

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

#### Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for Python. Methods Tablestore SDK for Python handles errors as exceptions. If the operation succeeds, the called operation does not return an exception. If the operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions Tablestore SDK for Python has two types of exceptions: OTSClientError and OTSServiceError. Both are inherited from Exception. OTSClientError: an internal SDK exception, such as an invalid parameter value or a failure to parse the results returned by the server. OTSServiceError: a server error that comes from the resolution of a server error message. OTSServiceError contains the following parameters: get_http_status: an HTTP status code, such as 200 and 404. get_error_code: an error type string returned by Tablestore. get_error_message: an error message string returned by Tablestore. get_request_id: the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help. Retry Tablestore SDK for Python automatically retries an operation when an error occurs. In the default retry policy, the maximum retry attempts is 20, and the maximum retry interval is 3,000 ms. For more information about the retry policies for throttling errors and internal server errors related to write operations, see tablestore/retry.py. You can also customize a retry policy by inheriting the RetryPolicy class, and configure the custom retry policy when you create an OTSClient object. Tablestore SDK for Python provides the following retry policies: DefaultRetryPolicy: the default retry policy. Only read operations are retried. The maximum retry attempts is 20, and the maximum retry interval is 3,000 ms. NoRetryPolicy: no operation is retried. NoDelayRetryPolicy: a retry policy without any delays. Exercise caution when you configure this policy. WriteRetryPolicy: the write operations are retried based on the default retry policy.

### Go SDK

#### Overview

This topic describes how to install and use Tablestore SDK for Go. Prerequisites An authorized account is created, and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. Download and install Tablestore SDK for Go For the download path of Tablestore SDK for Go, including the package, source code and examples, visit SDK package. For more information about how to install Tablestore SDK for Go, see Installation. Version Latest version: 5.0.2

#### Installation

This topic describes how to install Tablestore SDK for Go. Preparations Go 1.4 or later is available. Installation methods Run the following command to install Tablestore SDK for Go:

```
    go get github.com/aliyun/aliyun-tablestore-go-sdk
```

#### Initialization

TableStoreClient is a client for Tablestore. TableStoreClient provides various methods that you can use to perform operations on tables, a single row, and multiple rows. Obtain an endpoint An endpoint is a domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following steps:
1. Log on to the Tablestore console.
2. Click the name of the instance to go to the Inst ance Det ails tab.
On the Instance Details tab, you can view the endpoints of the instance in the Instance Access URL section. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair that consists of an AccessKey ID and an AccessKey secret for signature authentication. After you obtain an AccessKey pair, you can perform the following steps to initialize a Tablestore instance by using an endpoint: API operation

```
// Initialize a TableStoreClient instance. // endPoint specifies the endpoint used to access the Tablestore instance, which must sta rt with https://. Example: https://instance.cn-hangzhou.ots.aliyun.com:80 // accessKeyId specifies the AccessKey ID that is used to access the Tablestore instance. To obtain an AccessKey ID, visit the official website of Alibaba Cloud or contact an admi nistrator. // accessKeySecret specifies the AccessKey secret that is used to access the Tablestore i nstance. To obtain an AccessKey secret, visit the official website of Alibaba Cloud or co ntact an administrator. // instanceName specifies the name of the instance that you want to access. You can creat e an instance in the Tablestore console or contact an administrator to obtain the name of an existing instance. func NewClient(endPoint, instanceName, accessKeyId, accessKeySecret string, options ...Cl ientOption) *TableStoreClient
```

Examples

```
client = NewClient("your_instance_endpoint", "your_instance_name", "your_user_id", "your _user_key")
```

#### Use the SDK

##### Table-level operations

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

Examples The following code provides an example on how to create a table that contains two primary key columns and a reserved read/write throughput of (0,0):

```
 //Create a schema for the primary key columns, which includes the quantity, names, and t
ypes of primary key columns.
 //The first primary key column is named pk0 and requires an integer value. The first pri
mary key column is also the partition key.
 //The second primary key column is named pk1 and requires an integer value.
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
 createtableRequest.TableMeta = tableMeta
 createtableRequest.TableOption = tableOption
 createtableRequest.ReservedThroughput = reservedThroughput
 response, err = client.CreateTable(createtableRequest)
 if (err != nil) {
     fmt.Println("Failed to create table with error:", err)
 } else {
    fmt.Println("Create table finished")
```

For the detailed sample code, visit CreateTable@GitHub. ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

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

##### Single-row operations

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

##### Multi-row operations

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

##### Tunnel Service

This topic describes how to use Tunnel Service.

###### Installation

This topic describes how to install Tunnel Service. Download the source code package

```
go get github.com/aliyun/aliyun-tablestore-go-sdk/tunnel
```

Install dependencies You can go to the tunnel directory and use the dep tool to install the dependencies. Install the dep tool. dep ensure -v You can also run the go get command to install the dependencies.

```
go get -u go.uber.org/zap go get github.com/cenkalti/backoff go get github.com/golang/protobuf/proto go get github.com/satori/go.uuid go get github.com/stretchr/testify/assert go get github.com/smartystreets/goconvey/convey go get github.com/golang/mock/gomock go get gopkg.in/natefinch/lumberjack.v2
```

###### Quick start

This topic describes how to use Tablestore SDK for Go to get started with Tunnel Service. Tablestore SDK for Go allows you to perform operations such as creating tunnels, querying tunnel information, and deleting tunnels in Tunnel Service. Get started with Tunnel Service Tablestore SDK for Go allows you to use Tunnel Service.
1. Initialize a tunnel client.

```
// Set endpoint to the endpoint of the Tablestore instance. Example: https://instance.c n-hangzhou.ots.aliyun.com. // Set instance to the name of the instance. // Set accessKeyId to the AccessKey ID and accessKeySecret to the AccessKey secret that you use to access Tablestore. tunnelClient := tunnel.NewTunnelClient(endpoint, instance,
   accessKeyId, accessKeySecret)
```

2. Create a tunnel.

```
req := &tunnel.CreateTunnelRequest{
   TableName:  "testTable",
   TunnelName: "testTunnel",
   Type:       tunnel.TunnelTypeBaseStream, // Create a differential tunnel.
resp, err := tunnelClient.CreateTunnel(req) if err != nil {
   log.Fatal("create test tunnel failed", err)
log.Println("tunnel id is", resp.TunnelId)
```

3. Customize the data consumption callback to start automatic data consumption.

```
// Customize the data consumption callback function. func exampleConsumeFunction(ctx *tunnel.ChannelContext, records []*tunnel.Record) error
```

`{`

```
    fmt.Println("user-defined information", ctx.CustomValue)
    for _, rec := range records {
        fmt.Println("tunnel record detail:", rec.String())
    fmt.Println("a round of records consumption finished")
    return nil
// Configure the callback function in the SimpleProcessFactory operation and configure the TunnelWorkerConfig operation. workConfig := &tunnel.TunnelWorkerConfig{
   ProcessorFactory: &tunnel.SimpleProcessFactory{
      CustomValue: "user custom interface{} value",
      ProcessFunc: exampleConsumeFunction,
```

`},`

```
// Use TunnelDaemon to continuously consume data by using the specified tunnel. daemon := tunnel.NewTunnelDaemon(tunnelClient, tunnelId, workConfig) log.Fatal(daemon.Run())
```

Create a tunnel

```
req := &tunnel.CreateTunnelRequest{
   TableName:  "testTable",
   TunnelName: "testTunnel",
   Type:       tunnel.TunnelTypeBaseStream, // Create a differential tunnel.
resp, err := tunnelClient.CreateTunnel(req) if err != nil {
   log.Fatal("create test tunnel failed", err)
log.Println("tunnel id is", resp.TunnelId)
```

Query the information about a tunnel

```
req := &tunnel.DescribeTunnelRequest{
   TableName:  "testTable",
   TunnelName: "testTunnel",
resp, err := tunnelClient.DescribeTunnel(req) if err != nil {
   log.Fatal("describe test tunnel failed", err)
log.Println("tunnel id is", resp.Tunnel.TunnelId)
```

Delete a tunnel

```
req := &tunnel.DeleteTunnelRequest {
   TableName: "testTable",
   TunnelName: "testTunnel",
_, err := tunnelClient.DeleteTunnel(req) if err != nil {
   log.Fatal("delete test tunnel failed", err)
```

###### Configuration items

This topic describes the configuration items of Tunnel Service. Tunnel client When you initialize a tunnel client, you can customize client configurations by using the NewTunnelClientWithConfig operation. If the config parameter is not specified or is set to nil, DefaultTunnelConfig is used.

```
var DefaultTunnelConfig = &TunnelConfig{
      // Specify the maximum exponential backoff value to retry a failed request.
      MaxRetryElapsedTime: 45 * time.Second,
      // Specify the HTTP request timeout period.
      RequestTimeout:      30 * time.Second,
      // Specify http.DefaultTransport.
      Transport:           http.DefaultTransport,
```

Worker The TunnelWorkerConfig operation contains the configurations that are required for a worker. The ProcessorFactory field is required. If other parameters are not specified, the default values are retained.

```
type TunnelWorkerConfig struct {
   // Specify the heartbeat timeout period for the worker. The heartbeat timeout period for
the worker is the same as the heartbeat timeout period for Tunnel Service. In most cases, t he default value can be retained.
   HeartbeatTimeout  time.Duration
   // Specify the interval at which the worker sends heartbeat information. In most cases,
the default value can be retained.
   HeartbeatInterval time.Duration
   // Specify the operation that is used to create channels for tunnels. In most cases, the
default value can be retained.
   ChannelDialer     ChannelDialer
   // Specify the operation that is used to generate the processor for the channels. In mos
t cases, the callback function is used to initialize the SimpleProcessFactory operation.
   ProcessorFactory ChannelProcessorFactory
   // Configure ZAP logs. Default value: DefaultLogConfig.
   LogConfig      *zap.Config
   // Configure log rotation for ZAP. Default value: DefaultSyncer.
   LogWriteSyncer zapcore.WriteSyncer
```

ProcessorFactory is used to configure information such as the callback function information. We recommend that you use the SimpleProcessorFactory operation that is defined in Tablestore SDK for Go.

```
type SimpleProcessFactory struct {
   // Define and configure parameters. User-defined information is passed to the ChannelCon
text parameter contained in ProcessFunc and ShutdownFunc.
   CustomValue interface{}
   // Specify the interval between checkpoints. The interval is recorded by the worker. Whe
n CpInterval is set to a value less than or equal to 0, DefaultCheckpointInterval is used.
   CpInterval time.Duration
   // Specify the synchronous callback function that the worker uses to process data. If an
error is returned from ProcessFunc, the worker sends retry requests to ProcessFunc to obtai n the data based on exponential backoff.
   ProcessFunc  func(channelCtx *ChannelContext, records []*Record) error
   // Specify the synchronous callback function that is used when the worker exits.
   ShutdownFunc func(channelCtx *ChannelContext)
   // Configure logs. If the Logger field is set to nil, DefaultLogConfig is used to initia
lize the logger.
   Logger *zap.Logger
```

Log management The following examples show the default configurations of logs and log rotation: Default configurations of logs

```
// By default, DefaultLogConfig is used in the TunnelWorkerConfig and SimpleProcessFactor y operations to configure logs. var DefaultLogConfig = zap.Config{
   Level:       zap.NewAtomicLevelAt(zap.InfoLevel),
   Development: false,
   Sampling: &zap.SamplingConfig{
      Initial:    100,
      Thereafter: 100,
```

`},`

```
   Encoding: "json",
   EncoderConfig: zapcore.EncoderConfig{
      TimeKey:        "ts",
      LevelKey:       "level",
      NameKey:        "logger",
      CallerKey:      "caller",
      MessageKey:     "msg",
      StacktraceKey:  "stacktrace",
      LineEnding:     zapcore.DefaultLineEnding,
      EncodeLevel:    zapcore.LowercaseLevelEncoder,
      EncodeTime:     zapcore.ISO8601TimeEncoder,
      EncodeDuration: zapcore.SecondsDurationEncoder,
      EncodeCaller:   zapcore.ShortCallerEncoder,
```

`},` Default configurations of log rotation

```
// By default, DefaultSyncer is used in the TunnelWorkerConfig and SimpleProcessFactory o perations to configure log rotation. var DefaultSyncer = zapcore.AddSync(&lumberjack.Logger{
   // Specify the path of log files.
   Filename:   "tunnelClient.log",
   // Specify the maximum log file size.
   MaxSize:    512, //MB
   // Specify the maximum number of rotated log files that can be compressed.
   MaxBackups: 5,
   // Specify the maximum number of days for which rotated log files can be retained.
   MaxAge:     30, //days
   // Specify whether to compress rotated log files.
   Compress:   true,
```

`})`

###### Error handling

This topic describes the error handling methods in Tablestore SDK for Go. After Tunnel Service receives an abnormal request, Tunnel Service returns an HTTP status code and an error message in the Protobuf format. Error message format Error messages are returned in the following Protobuf format:

```
message Error {
    required string code = 1;
    optional string message = 2;
    optional string tunnel_id = 3;
```

Error codes When you use Tablestore SDK for Go, you need to handle only error codes that return error messages. The SDK automatically processes other error codes or retries the requests. We recommend that you handle errors based on the processing logic of the error code.

| HTTP status code | Error code | Description | Processing logic |
|---|---|---|---|
| 400 | OTSParameterInvalid | The error message returned because a parameter in the request is invalid or the requested data table does not exist. | Return an error message. |
| 400 | OTSTunnelExpired | The error message returned because the logs of the incremental or differential tunnel are expired. | Return an error message. |

| HTTP status code | Error code | Description | Processing logic |
|---|---|---|---|
| 403 | OTSPermissionDenied | The error message returned because you are not authorized to access the specified resource. | Return an error message. |
| 409 | OTSTunnelExist | The error message returned because the tunnel that you want to create already exists on the server. | Return an error message. |
| 400 | OTSSequenceNumberN otMatch | The error message returned because the serial numbers of checkpoints are inconsistent between the client and server. This error may occur when the serial numbers of checkpoints on the client are smaller than those on the server or channels compete with each other for data consumption. | Use the checkpoint operation to obtain the serial numbers of checkpoints again. |
| 410 | OTSResourceGone | The error message returned because the request sent to obtain the heartbeat information about the tunnel client times out. | Use the tunnel ID to reconnect to Tunnel Service. |
| 503 | OTSTunnelServerUnavail able | The error message returned because an internal error occurs. | Use exponential backoff to retry the request. |

### NodeJS SDK

#### Overview

This topic describes how to use Tablestore SDK for Node.js. The content in this topic applies to Tablestore SDK for Node.js V4.x.x or later. Prerequisites An authorized account is created, and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for Node.js Download Tablestore SDK for Node.js from GitHub. For more information, visit GitHub. Version Latest version: 5.1.0

#### Installation

This topic describes how to install Tablestore SDK for Node.js. Preparations Node.js 4.0 or later is installed. Not e We recommend that you do not use Node.js later than 12.0 and earlier than 12.14 to avoid compatibility problems. Install Tablestore SDK for Node.js Run the following command to install Tablestore SDK for Node.js:

```
npm install tablestore
```

Not e If you encounter any network problems when you use npm, you can use the npm image provided by Taobao. Sample programs Tablestore SDK for Node.js provides a variety of sample programs for your reference and use. You can obtain the sample programs by using one of the following methods: Download and decompress the Tablestore SDK for Node.js package. Find the sample programs in the examples folder. Access Tablestore SDK for Node.js on GitHub.

#### Initialization

TableStore.Client is a client for Tablestore. TableStore.Client provides various methods that you can use to perform operations on tables, a single row, and multiple rows. Obtain an endpoint An endpoint is a domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following steps:
1. Log on to the Tablestore console.
2. Click the name of the instance to go to the Inst ance Det ails tab.
On the Instance Details tab, you can view the endpoints of the instance in the Instance Access URL section. Initialize a Tablestore instance To access Apsara Stack Tablestore, you must have a valid AccessKey pair that consists of an AccessKey ID and an AccessKey secret for signature authentication. After you obtain an AccessKey pair, you can perform the following steps to initialize a Tablestore instance by using an endpoint:

```
var client = new TableStore.Client({ accessKeyId: '<your access key id>', accessKeySecret: '<your access key secret>', endpoint: '<your endpoint>', instancename: '<your instance name>', maxRetries:20,// The default number of retry attempts is 20. You can ignore this parameter. });
```

#### Data types

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

#### Use the SDK

##### Table-level operations

Tablestore SDK for Node.js provides the following table-level operations: CreateTable, ListTable, DeleteTable, UpdateTable, and DescribeTable. CreateTable You can call this operation to create a table based on the specified table structure. Not e After the table is created, it can take several seconds to load the table. During this period, the read and write operations on the table may fail. You can use applications to perform operations on the table data only after the table is loaded. You must specify the primary key when you create a table. A primary key can contain one to four primary key columns. Each primary key column has a name and a data type. API operation

```
  /**
   * Create a table based on the specified table structure.
```

`*/`

```
  createTable(params, callback)
```

Examples The following code provides an example on how to create a table that has two primary key columns and a reserved read/write throughput of (0,0):

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
    timeToLive: -1,// Specify the validity period of data in seconds. A value of -1 indic
ates that the data never expires. If you set the validity period to a year, the value of timeToLive is 365*24*3600.
    maxVersions: 1// Specify the maximum number of versions that can be saved in each col
umn. A value of 1 indicates that only the latest version is saved in each column.
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

For the detailed sample code, visit CreateTable@GitHub. ListTable You can call this operation to obtain the names of all tables created in the current instance. API operation

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

##### Single-row operations

Tablestore SDK for Node.js provides the following single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can call this operation to insert data into a specified row. Operation

```
  /**
   * Insert data into a specified row. If the row does not exist, a new row is added. If
the row exists, the existing data is overwritten.
```

`*/`

```
  putRow(params, callback)
```

Example Not e RowExistenceExpectation.IGNORE indicates that new data is inserted into a row despite whether the specified row exists or not. If the specified row exists, the existing data is overwritten. RowExistenceExpectation.EXPECT_EXIST indicates that new data is inserted only when the specified row exists. The existing data is overwritten. RowExistenceExpectation.EXPECT_NOT_EXIST indicates that data is inserted only when the specified row does not exist.

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

For the detailed sample code, visit PutRow@GitHub. GetRow You can call this operation to read a single row of data based on a specified primary key. Operation

```
  /**
   * Read a single row of data based on a specified primary key.
```

`*/`

```
  getRow(params, callback)
```

Example The following code provides an example on how to read a row of data:

```
var TableStore = require('../index.js'); var Long = TableStore.Long; var client = require('./client'); var params = {
  tableName: "sampleTable",
  primaryKey: [{ 'gid': Long.fromNumber(20004) }, { 'uid': Long.fromNumber(20004) }],
  maxVersions: 2 // The maximum number of versions that can be read. If you set this para
meter to 2, a maximum of two versions can be read.
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

For the detailed sample code, visit GetRow@GitHub. UpdateRow You can call this operation to update the data of a specified row. If the row does not exist, a new row is added. If the row exists, values are added to the specified columns or the values in the specified columns are changed or deleted based on the request. Operation

```
  /**
   * Update the data of the specified row. If the row does not exist, a new row is added.
If the row exists, values are added to the specified columns or the values in the specifi ed columns are changed or deleted based on the request.
```

`*/`

```
  updateRow(params, callback)
```

Example The following code provides an example on how to update the data of a specified row:

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

For the detailed sample code, visit UpdateRow@GitHub. DeleteRow You can call this operation to delete unwanted data. Operation

```
  /**
   * Delete a row of data.
```

`*/`

```
  deleteRow(params, callback)
```

Example The following code provides an example on how to delete a row of data:

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

##### Multi-row operations

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

#### Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for Node.js. Methods Tablestore SDK for Node.js handles errors as exceptions. If the operation succeeds, the called operation does not return an exception. If the operation fails, an exception is returned. Not e Batch operations such as BatchGetRow and BatchWriteRow can be called only after the system verifies that no exception is returned and that the status of each row is successful. Exceptions All errors are handled by Tablestore SDK for Node.js in a unified manner, and are returned as the value of the err parameter by using the callback method. Before you obtain the returned data, you must check whether the err parameter has a value. If an error occurs at the server side of Tablestore, the request ID is returned. The request ID is the UUID that identifies a request. If you cannot solve the problem, record this request ID and contact Tablestore technical support for help. Retry The system automatically retries the operation when an error occurs in the SDK. The default policy sets a maximum of 20 retry attempts and a maximum retry interval of 3000 ms. For more information about how the system retries the operation on throttling errors and read-related internal server errors, see

```
 tablestore/lib/retry.js .
```

### 2.5. .NET SDK

#### Overview

This topic describes how to use Tablestore SDK for .NET. Prerequisites An authorized account is created, and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret is obtained. For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. Download Tablestore SDK for .NET Download the SDK installation package from NuGet. For more information about the download path, visit https://www.nuget.org/packages/Aliyun.TableStore.SDK/4.1.4. Download the source code from GitHub. For more information about the download path, visit GitHub. Compatibility Tablestore SDK for .NET V3.x.x: compatible. Tablestore SDK for .NET V2.x.x: Some operations are incompatible. The Condition.IGNORE, Condition.EXPECT_EXIST, and Condition.EXPECT_NOT_EXIST parameters are deleted. The DLL file name is changed from Aliyun.dll to Aliyun.TableStore.dll. Version Latest version: 4.1.4.

#### Installation

This topic describes how to install Tablestore SDK for .NET. Version dependency Windows .NET 4.0 or later is required. Visual Studio 2010 or later is required. Install Tablestore SDK for .NET in Windows Install by using NuGet i. After you install NuGet, create a project or open an existing project in Visual Studio, and then choose T ools > NuGet Package Manager > Manage NuGet Packages f or Solut ion. Not e If Visual Studio does not have NuGet installed, download and install NuGet. For more information about the download path, visit NuGet. ii. Enter aliyun.tablestore in the search box and click Search. Find Aliyun.TableStore.SDK in the search results. iii. Select the latest version, and click Inst all. After the installation is complete. Tablestore SDK for .NET is added to the project for application. Install by importing a project i. Download the source code from GitHub. For more information about the download path, visit GitHub. Not e If Git is not installed, download and install Git. For more information about the download path, visit git. ii. In Visual Studio, right-click and select Solut ion from the menu that appears, choose Add > Exist ing project s. iii. In the dialog box that appears, select the aliyun-tablestore-sdk.csproj file, and click Open. iv. Right-click and select Your project . Choose Ref erences > Add Ref erence from the shortcut menu. In the dialog box that appears, click the Project s tab, and select the aliyun-tablestoresdk project. v. Click OK.

#### Initialization

TableStoreClient is a client for Tablestore. TableStoreClient provides various methods that you can use to perform operations on tables, a single row, and multiple rows. Obtain an endpoint An endpoint is a domain name that is used to access a Tablestore instance in a region. To query an endpoint, perform the following steps:
1. Log on to the Tablestore console.
2. Click the name of the instance to go to the Inst ance Det ails tab.
On the Instance Details tab, you can view the endpoints of the instance in the Instance Access URL section. Configure an AccessKey pair To access Apsara Stack Tablestore, you must have a valid AccessKey pair that consists of an AccessKey ID and an AccessKey secret for signature authentication. After you obtain an AccessKey pair, you can perform the following steps to initialize a Tablestore instance by using an endpoint: API operation

```
    /// <summary>
    /// The function used to construct OTSClient.
    /// </summary>
    /// <param name="endPoint">The endpoint that is used to access the Tablestore instanc
e, which must start with https://. Example: https://instance.cn-hangzhou.ots.aliyun.com:8
0. </param>
    /// <param name="accessKeyID">The AccessKey ID that is used to access the Tablestore
instance. You can apply for an AccessKey ID on the Alibaba Cloud official website. </para
```

`m>`

```
    /// <param name="accessKeySecret">The AccessKey secret that is used to access the Tab
lestore instance. You can apply for an AccessKey secret on the Alibaba Cloud official web site. </param>
    /// <param name="instanceName">The name of the Tablestore instance. You can create an
instance in the Tablestore console. </param> public OTSClient(string endPoint, string accessKeyID, string accessKeySecret, string inst anceName);
    /// <summary>
    /// Create an OTSClient instance by configuring the instance of the OTSClientConfig c
lass on the client.
    /// </summary>
    /// <param name="config">The instance for client configurations.</param>
    public OTSClient(OTSClientConfig config);
```

Sample code Not e You can configure the ConnectionLimit parameter in OTSClientConfig. If you do not specify a value for the ConnectionLimit parameter, the default value 300 is used. You can configure OTSDebugLogHandler and OTSErrorLogHandler in OTSClientConfig to specify whether to enable logging. You can configure RetryPolicy in OTSClientConfig to control and specify the retry logic. You can also use the default retry policy.

```
    // Create an OTSClientConfig object.
    var config = new OTSClientConfig(Endpoint, AccessKeyId, AccessKeySecret, InstanceName
```

);

```
    // Disable logging. By default, logging is enabled.
    config.OTSDebugLogHandler = null;
    config.OTSErrorLogHandler = null;
    // Create an OTSClient object by using OTSClientConfig.
    var otsClient = new OTSClient(config);
    // Use OTSClient to insert or query data.
```

Multithreading Multithreading is supported. We recommend that you use the same OTSClient object to run multithreading tasks.

#### Use the SDK

##### Table-level operations

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

Examples The following code provides an example on how to create a table that contains two primary key columns and a reserved read/write throughput of (0,0):

```
 //Create a schema for the primary key columns, which includes the quantity, names, and t
ypes of primary key columns.
 //The first primary key column is named pk0, and is also the partition column.
 //The second primary key column is named pk1, and requires a string value.
 var primaryKeySchema = new PrimaryKeySchema();
 primaryKeySchema.Add("pk0", ColumnValueType.Integer);
 primaryKeySchema.Add("pk1", ColumnValueType.String);
 //Create a tableMeta class based on the table name and the schema for primary key column
```

`s.`

```
 var tableMeta = new TableMeta("SampleTable", primaryKeySchema);
 // Set the reserved read throughput and reserved write throughput to 0.
 var reservedThroughput = new CapacityUnit(0, 0);
 try
```

`{`

```
     // Construct the CreateTableRequest object.
     var request = new CreateTableRequest(tableMeta, reservedThroughput);
     // Call the CreateTable operation of the client. If the table is created, no excepti
on is returned. Otherwise, an exception is returned.
     otsClient.CreateTable(request);
     Console.WriteLine("Create table succeeded.") ;
 // If the task fails, an exception is returned and handled.
 catch (Exception ex)
```

`{`

```
     Console.WriteLine("Create table failed, exception:{0}", ex.Message);
```

For the detailed sample code, visit CreateTable@GitHub. ListTable You can call this operation to query the names of all tables created in the current instance. API operation

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

##### Single-row operations

The Tablestore SDK provides the following APIs for single-row operations: PutRow, GetRow, UpdateRow, and DeleteRow. PutRow You can use the PutRow API to insert data into a specified row. API

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

Not e Each asynchronous invocation starts a thread. A timeout error may occur if too many asynchronous invocations are started consecutively and each invocation consumes an extended period of time. To view the detailed code, see PutRowAsync@GitHub. GetRow You can use the GetRow API to read a single row of data based on a specified primary key. API

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

Not e To view the detailed code, see GetRowWithFilter@GitHub. UpdateRow You can use the UpdateRow API to update the data of a specified row. If the row does not exist, a new row is added. If the row exists, the values of the specified columns are added, modified, or deleted based on the request content. API

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

Not e You can use conditional statements to update rows. To view the detailed code, see UpdateRow@GitHub. DeleteRow API

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

##### Multiple-row operations

The Tablestore SDK provides the following APIs for multiple-row operations: BatchGetRow, BatchWriteRow, GetRange, and GetRangeIterator. BatchGetRow You can use the BatchGetRow API to simultaneously read several rows of data from one or more tables. The BatchGetRow operation is a set of multiple GetRow operations. The execution, returning of results, and capacity unit (CU) consumption of each individual operation are carried out independently. Compared with the execution of a large number of GetRow operations, the use of BatchGetRow can reduce the request response time and increase the data read rate. API

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

Not e You can use conditional statements to filter the results returned by a BatchGetRow operation. To view the detailed code, see BatchGetRow@GitHub. BatchWriteRow You can use the BatchWriteRow API to insert, modify, or delete several rows of data in one or more tables. The BatchWriteRow operation is a set of multiple PutRow, UpdateRow, and DeleteRow operations. The execution, returning of results, and CU consumption of each individual operation are carried out independently. API

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

Not e You can use conditional statements to filter the results returned by a BatchWriteRow operation. To view the detailed code, see BatchWriteRow@GitHub. GetRange You can use the GetRange API to read data within the specified primary key range. API

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

Not e You can use conditional statements to filter the read data returned from the specified range. To view the detailed code, see GetRange@GitHub. GetRangeIterator You can use the GetRangeIterator API to obtain an iterator within the specified range. API

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

#### Error handling

This topic describes the error handling methods and retry policies in Tablestore SDK for .NET. Method The Tablestore .NET SDK adopts the Exception method to handle errors. If an operation succeeds, the called API does not throw an exception. If the operation fails, an exception is thrown. Not e Batch operation APIs such as BatchGetRow and BatchWriteRow are called only when the status check of each row is successful. Error The Tablestore .NET SDK has two types of exceptions: OTSClientException and OTSServerException. Both are inherited from Exception. OTSClientException: indicates an internal SDK exception, such as an incorrect parameter value or a failure to parse the results returned by the server. OTSServerException: indicates a server error arising from the resolution of a server error message. OTSServerException has the following components: HttpStatusCode: an HTTP status code, such as 200 or 404. ErrorCode: an error type string returned by Tablestore. ErrorMessage: an error message string returned by Tablestore. RequestId: the UUID that uniquely identifies a request. If a problem persists, submit the request ID to Tablestore technical support personnel to obtain help. Retry The system retries an operation when an error occurs in the SDK. The operation is retried three times at a maximum interval of two seconds by default. For more information, see the Aliyun.OTS.Retry.DefaultRetryPolicy class. You can modify RetryPolicy in OTSClientConfig to customize a retry policy.

### Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click User
Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of your account.
Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management Accesskey.
6. In the dialog box that appears, view the AccessKey pair of the organization.
