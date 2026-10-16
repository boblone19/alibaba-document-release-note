---
title: "MaxCompute Developer Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 316
source_pdf: "bd45728b747ee2b2_Alibaba Cloud Apsara Stack V3.18.6 MaxCompute Developer Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AE%A1%E7%AE%97%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20MaxCompute%20Developer%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# MaxCompute Developer Guide 20260629

## Table of Contents

- 1 Java SDK
  - 1.1 Java SDK
  - 1.2 Prerequisites
    - 1.2.1 Overview
    - 1.2.2 Obtain an AccessKey pair
      - 1.2.2.1 Log on to the Apsara Uni-manager Management Console
      - 1.2.2.2 Obtain the AccessKey pair of an organization
      - 1.2.2.3 Obtain the AccessKey pair of an Alibaba Cloud account
    - 1.2.3 Obtain an endpoint
  - 1.3 Major APIs
    - 1.3.1 AliyunAccount
    - 1.3.2 Odps
    - 1.3.3 Projects
    - 1.3.4 Project
    - 1.3.5 SQLTask
    - 1.3.6 Instances
    - 1.3.7 Instance
    - 1.3.8 Tables
    - 1.3.9 Table
    - 1.3.10 Resources
    - 1.3.11 Resource
    - 1.3.12 Functions
    - 1.3.13 Function
    - 1.3.14 Spark Shell
    - 1.3.15 Spark R
    - 1.3.16 Spark SQL
    - 1.3.17 Spark JDBC
    - 1.3.18 Document APIs
    - 1.3.19 Search APIs
    - 1.3.20 CheckPermissionTest
    - 1.3.21 Volume2
- 2 SDK for Python
- 3 MaxCompute SQL
  - 3.1 Overview
    - 3.1.1 Scenarios
    - 3.1.2 Reserved words
    - 3.1.3 Partitioned table
    - 3.1.4 Type conversion
      - 3.1.4.1 Explicit conversions of data types
      - 3.1.4.2 Implicit type conversion and its scope
      - 3.1.4.3 SQL built-in functions
      - 3.1.4.4 CASE WHEN
      - 3.1.4.5 Conversions between the STRING and DATETIME types
  - 3.2 Operators
    - 3.2.1 Relational operators
    - 3.2.2 Arithmetic operators
    - 3.2.3 Bitwise operators
    - 3.2.4 Logical operators
  - 3.3 LOAD
  - 3.4 DDL statements
    - 3.4.1 Table operations
      - 3.4.1.1 Create a table
      - 3.4.1.2 Delete a table
      - 3.4.1.3 Rename a table
      - 3.4.1.4 Change the owner of a table
      - 3.4.1.5 Modify the comment of a table
      - 3.4.1.6 Modify the lifecycle settings of a table
      - 3.4.1.7 Disable or enable the lifecycle feature
      - 3.4.1.8 Modify the value of LastDataModifiedTime for a table
      - 3.4.1.9 Modify the clustering attributes of a table
      - 3.4.1.10 Delete data from a non-partitioned table
      - 3.4.1.11 Archive table data
      - 3.4.1.12 Forcibly delete data from a table or partition
    - 3.4.2 View-based operation
      - 3.4.2.1 Create a view
      - 3.4.2.2 Delete a view
      - 3.4.2.3 Rename a view
    - 3.4.3 Materialized view operations
    - 3.4.4 Column and partition operations
      - 3.4.4.1 Add partitions
      - 3.4.4.2 Delete a partition
      - 3.4.4.3 Add columns or comments
      - 3.4.4.4 Change the name of a column
      - 3.4.4.5 Modify the comment of a column
      - 3.4.4.6 Modify the name and comment of a column at the same time
      - 3.4.4.7 Change LastDataModifiedTime of a non-partitioned table or a partition in a partitioned table.
      - 3.4.4.8 Modify partition values
      - 3.4.4.9 Merge partitions
  - 3.5 DML statements
    - 3.5.1 INSERT
      - 3.5.1.1 Update data in a table
      - 3.5.1.2 Insert data into multiple objects
      - 3.5.1.3 Insert data into dynamic partitions
      - 3.5.1.4 VALUES
    - 3.5.2 SELECT
      - 3.5.2.1 SELECT operations
      - 3.5.2.2 Subquery
      - 3.5.2.3 UNION ALL
      - 3.5.2.4 JOIN
      - 3.5.2.5 MAPJOIN hint
      - 3.5.2.6 SELECT TRANSFORM
        - 3.5.2.6.1 Overview
        - 3.5.2.6.2 SELECT TRANSFORM examples
          - 3.5.2.6.2.1 Call shell scripts
          - 3.5.2.6.2.2 Call Python scripts
          - 3.5.2.6.2.3 Call Java scripts
          - 3.5.2.6.2.4 Call the scripts of other programming languages
          - 3.5.2.6.2.5 Call scripts in series
        - 3.5.2.6.3 Performance
      - 3.5.2.7 GROUPING SETS
        - 3.5.2.7.1 Overview
        - 3.5.2.7.2 Example
        - 3.5.2.7.3 CUBE and ROLLUP
        - 3.5.2.7.4 GROUPING and GROUPING_ID
      - 3.5.2.8 UNION, INTERSECT, and EXCEPT
    - 3.5.3 EXPLAIN
    - 3.5.4 IF statement
    - 3.5.5 UPDATE and DELETE
  - 3.6 Built-in functions
    - 3.6.1 Mathematical functions
      - 3.6.1.1 ABS
      - 3.6.1.2 ACOS
      - 3.6.1.3 ASIN
      - 3.6.1.4 ATAN
      - 3.6.1.5 CEIL
      - 3.6.1.6 CONV
      - 3.6.1.7 COS
      - 3.6.1.8 COSH
      - 3.6.1.9 COT
      - 3.6.1.10 EXP
      - 3.6.1.11 FLOOR
      - 3.6.1.13 LOG
      - 3.6.1.14 POW
      - 3.6.1.15 RAND
      - 3.6.1.16 ROUND
      - 3.6.1.17 SIN
      - 3.6.1.18 SINH
      - 3.6.1.19 SQRT
      - 3.6.1.20 TAN
      - 3.6.1.21 TANH
      - 3.6.1.22 TRUNC
      - 3.6.1.23 Additional mathematical functions
        - 3.6.1.23.1 Usage notes
        - 3.6.1.23.2 LOG2
        - 3.6.1.23.3 LOG10
        - 3.6.1.23.4 BIN
        - 3.6.1.23.5 HEX
        - 3.6.1.23.6 UNHEX
        - 3.6.1.23.7 RADIANS
        - 3.6.1.23.8 DEGREES
        - 3.6.1.23.9 SIGN
        - 3.6.1.23.12 FACTORIAL
        - 3.6.1.23.13 CBRT
        - 3.6.1.23.14 SHIFTLEFT
        - 3.6.1.23.15 SHIFTRIGHT
        - 3.6.1.23.16 SHIFTRIGHTUNSIGNED
        - 3.6.1.23.17 FORMAT_NUMBER
        - 3.6.1.23.18 WIDTH_BUCKET
    - 3.6.2 String functions
      - 3.6.2.1 CHAR_MATCHCOUNT
      - 3.6.2.2 CHR
      - 3.6.2.3 CONCAT
      - 3.6.2.4 INSTR
      - 3.6.2.5 IS_ENCODING
      - 3.6.2.6 KEYVALUE
      - 3.6.2.7 LENGTH
      - 3.6.2.8 LENGTHB
      - 3.6.2.10 PARSE_URL
      - 3.6.2.11 REGEXP_EXTRACT
      - 3.6.2.12 REGEXP_INSTR
      - 3.6.2.13 REGEXP_SUBSTR
      - 3.6.2.14 REGEXP_COUNT
      - 3.6.2.15 REGEXP_REPLACE
      - 3.6.2.16 SPLIT_PART
      - 3.6.2.17 SUBSTR
      - 3.6.2.18 TOLOWER
      - 3.6.2.19 TOUPPER
      - 3.6.2.20 TO_CHAR
      - 3.6.2.21 TRIM
      - 3.6.2.22 LTRIM
      - 3.6.2.23 RTRIM
      - 3.6.2.24 REVERSE
      - 3.6.2.25 SPACE
      - 3.6.2.26 REPEAT
      - 3.6.2.27 ASCII
      - 3.6.2.28 Additional string functions
        - 3.6.2.28.1 Usage notes
        - 3.6.2.28.2 CONCAT_WS
        - 3.6.2.28.3 LPAD
        - 3.6.2.28.4 RPAD
        - 3.6.2.28.5 REPLACE
        - 3.6.2.28.6 SOUNDEX
        - 3.6.2.28.7 SUBSTRING_INDEX
        - 3.6.2.28.8 TRANSLATE
        - 3.6.2.28.9 URL_ENCODE
        - 3.6.2.28.10 URL_DECODE
        - 3.6.2.28.11 JSON_TUPLE
        - 3.6.2.28.12 FROM_JSON
        - 3.6.2.28.13 TO_JSON
    - 3.6.3 Date functions
      - 3.6.3.1 DATEADD
      - 3.6.3.2 DATEDIFF
      - 3.6.3.3 DATEPART
      - 3.6.3.4 DATETRUNC
      - 3.6.3.5 GETDATE
      - 3.6.3.6 ISDATE
      - 3.6.3.7 LASTDAY
      - 3.6.3.8 TO_DATE
      - 3.6.3.9 TO_CHAR
      - 3.6.3.10 UNIX_TIMESTAMP
      - 3.6.3.11 FROM_UNIXTIME
      - 3.6.3.12 WEEKDAY
      - 3.6.3.13 WEEKOFYEAR
      - 3.6.3.14 Additional date functions
        - 3.6.3.14.1 Usage notes
        - 3.6.3.14.2 YEAR
        - 3.6.3.14.3 QUARTER
        - 3.6.3.14.4 MONTH
        - 3.6.3.14.5 DAY
        - 3.6.3.14.6 DAYOFMONTH
        - 3.6.3.14.7 HOUR
        - 3.6.3.14.8 MINUTE
        - 3.6.3.14.9 SECOND
        - 3.6.3.14.10 FROM_UTC_TIMESTAMP
        - 3.6.3.14.11 CURRENT_TIMESTAMP
        - 3.6.3.14.12 ADD_MONTHS
        - 3.6.3.14.13 LAST_DAY
        - 3.6.3.14.14 NEXT_DAY
        - 3.6.3.14.15 MONTHS_BETWEEN
        - 3.6.3.14.16 EXTRACT
    - 3.6.4 Window functions
      - 3.6.4.1 Overview
      - 3.6.4.2 COUNT
      - 3.6.4.3 AVG
      - 3.6.4.4 MAX
      - 3.6.4.5 MIN
      - 3.6.4.6 MEDIAN
      - 3.6.4.7 STDDEV
      - 3.6.4.8 STDDEV_SAMP
      - 3.6.4.9 SUM
      - 3.6.4.10 DENSE_RANK
      - 3.6.4.11 RANK
      - 3.6.4.12 LAG
      - 3.6.4.13 LEAD
      - 3.6.4.14 PERCENT_RANK
      - 3.6.4.15 ROW_NUMBER
      - 3.6.4.16 CLUSTER_SAMPLE
      - 3.6.4.17 NTILE
      - 3.6.4.18 NTH_VALUE
      - 3.6.4.19 CUME_DIST
      - 3.6.4.20 FIRST_VALUE
      - 3.6.4.21 LAST_VALUE
    - 3.6.5 Aggregate functions
      - 3.6.5.1 Expressions of filter conditions in aggregate functions
      - 3.6.5.2 COUNT
      - 3.6.5.3 COUNT_IF
      - 3.6.5.4 AVG
      - 3.6.5.5 MAX
      - 3.6.5.6 MIN
      - 3.6.5.7 MEDIAN
      - 3.6.5.8 STDDEV
      - 3.6.5.9 STDDEV_SAMP
      - 3.6.5.10 SUM
      - 3.6.5.11 WM_CONCAT
      - 3.6.5.12 PERCENTILE
      - 3.6.5.13 Additional aggregate functions
        - 3.6.5.13.1 Usage notes
        - 3.6.5.13.2 COLLECT_LIST
        - 3.6.5.13.3 COLLECT_SET
        - 3.6.5.13.4 VARIANCE or VAR_POP
        - 3.6.5.13.5 VAR_SAMP
        - 3.6.5.13.6 COVAR_POP
        - 3.6.5.13.7 COVAR_SAMP
        - 3.6.5.13.8 ANY_VALUE
        - 3.6.5.13.9 NUMERIC_HISTOGRAM
        - 3.6.5.13.10 PERCENTILE_APPROX
        - 3.6.5.13.11 APPROX_DISTINCT
    - 3.6.6 Other functions
      - 3.6.6.1 ARRAY
      - 3.6.6.2 ARRAY_CONTAINS
      - 3.6.6.3 CAST
      - 3.6.6.4 COALESCE
      - 3.6.6.5 DECODE
      - 3.6.6.6 EXPLODE
      - 3.6.6.7 GET_IDCARD_AGE
      - 3.6.6.8 GET_IDCARD_BIRTHDAY
      - 3.6.6.9 GET_IDCARD_SEX
      - 3.6.6.10 GREATEST
      - 3.6.6.11 INDEX
      - 3.6.6.12 MAX_PT
      - 3.6.6.13 ORDINAL
      - 3.6.6.14 LEAST
      - 3.6.6.15 SIZE
      - 3.6.6.16 SPLIT
      - 3.6.6.17 STR_TO_MAP
      - 3.6.6.18 UUID
      - 3.6.6.19 UNIQUE_ID
      - 3.6.6.20 SAMPLE
      - 3.6.6.21 CASE WHEN expression
      - 3.6.6.23 Additional functions
        - 3.6.6.23.1 Usage notes
        - 3.6.6.23.2 MAP
        - 3.6.6.23.3 MAP_KEYS
        - 3.6.6.23.4 MAP_VALUES
        - 3.6.6.23.5 SORT_ARRAY
        - 3.6.6.23.6 POSEXPLODE
        - 3.6.6.23.7 STRUCT
        - 3.6.6.23.8 NAMED_STRUCT
        - 3.6.6.23.9 INLINE
        - 3.6.6.23.10 BETWEEN AND expression
        - 3.6.6.23.11 NVL
        - 3.6.6.23.12 TABLE_EXISTS
        - 3.6.6.23.13 PARTITION_EXISTS
  - 3.7 UDFs
    - 3.7.1 Java UDFs
      - 3.7.1.1 Overview
      - 3.7.1.2 Types of parameters and return values
      - 3.7.1.3 UDF
      - 3.7.1.4 UDAF
      - 3.7.1.5 UDTFs
        - 3.7.1.5.1 Overview
        - 3.7.1.5.2 Examples of using UDTFs
    - 3.7.2 Python UDFs
      - 3.7.2.1 Before you start
      - 3.7.2.2 Limits
      - 3.7.2.3 Third-party libraries
      - 3.7.2.4 Types of parameters and return values
      - 3.7.2.5 UDF
      - 3.7.2.6 UDAF
      - 3.7.2.7 UDTF
      - 3.7.2.8 Resource reference
    - 3.7.3 Python 3 UDF
    - 3.7.4 SQL Function
    - 3.7.5 Embedded UDF
      - 3.7.5.1 Background information
      - 3.7.5.2 Feature summary
      - 3.7.5.3 Limits
      - 3.7.5.4 Examples
  - 3.8 UDTs
    - 3.8.1 Scenarios and limits
    - 3.8.2 Feature summary
    - 3.8.3 Implementation principles and feature description
    - 3.8.4 Benefits
    - 3.8.5 Performance advantages
    - 3.8.6 Security advantages
    - 3.8.7 More examples
      - 3.8.7.1 Example of using Java arrays
      - 3.8.7.2 Example of using JSON
      - 3.8.7.3 Example of using complex data types
      - 3.8.7.4 Aggregation example
      - 3.8.7.5 Example of using table-valued functions
  - 3.9 UDJ
    - 3.9.1 Background information
    - 3.9.2 Examples of using UDJ
      - 3.9.2.1 Cross join operation by using UDJ
      - 3.9.2.2 Pre-sorting
    - 3.9.3 Performance
  - 3.10 Parameterized view
  - 3.11 CLONE TABLE
  - 3.12 Geographic functions
    - 3.12.1 Usage notes
    - 3.12.2 Constructors
      - 3.12.2.1 ST_AsBinary
      - 3.12.2.2 ST_AsGeoJson
      - 3.12.2.3 ST_AsJson
      - 3.12.2.4 ST_AsShape
      - 3.12.2.5 ST_AsText
      - 3.12.2.6 ST_GeomCollection
      - 3.12.2.7 ST_GeomFromGeoJson
      - 3.12.2.8 ST_GeomFromJSON
      - 3.12.2.9 ST_GeomFromShape
      - 3.12.2.10 ST_GeomFromText
      - 3.12.2.11 ST_GeomFromWKB
      - 3.12.2.12 ST_GeometryType
      - 3.12.2.13 ST_LineString
      - 3.12.2.14 ST_LineFromWKB
      - 3.12.2.15 ST_MultiLineString
      - 3.12.2.16 ST_MLineFromWKB
      - 3.12.2.17 ST_MultiPoint
      - 3.12.2.18 ST_MPointFromWKB
      - 3.12.2.19 ST_MultiPolygon
      - 3.12.2.20 ST_MPolyFromWKB
      - 3.12.2.21 ST_Point
      - 3.12.2.22 ST_PointFromWKB
      - 3.12.2.23 ST_PointZ
      - 3.12.2.24 ST_Polygon
      - 3.12.2.25 ST_PolyFromWKB
      - 3.12.2.26 ST_SetSRID
    - 3.12.3 Accessors
      - 3.12.3.1 ST_Area
      - 3.12.3.2 ST_Centroid
      - 3.12.3.3 ST_CoordDim
      - 3.12.3.4 ST_Dimension
      - 3.12.3.5 ST_Distance
      - 3.12.3.6 ST_GeodesicLengthWGS84
      - 3.12.3.7 ST_GeometryN
      - 3.12.3.9 ST_IsClosed
      - 3.12.3.10 ST_IsEmpty
      - 3.12.3.11 ST_IsMeasured
      - 3.12.3.12 ST_IsSimple
      - 3.12.3.13 ST_IsRing
      - 3.12.3.14 ST_Length
      - 3.12.3.16 ST_MaxM
      - 3.12.3.17 ST_MinM
      - 3.12.3.21 ST_MaxX
      - 3.12.3.22 ST_MaxY
      - 3.12.3.23 ST_MaxZ
      - 3.12.3.24 ST_MinX
      - 3.12.3.25 ST_MinY
      - 3.12.3.26 ST_MinZ
      - 3.12.3.27 ST_NumGeometries
      - 3.12.3.28 ST_NumInteriorRing
      - 3.12.3.29 ST_NumPoints
      - 3.12.3.30 ST_PointN
      - 3.12.3.31 ST_StartPoint
      - 3.12.3.32 ST_EndPoint
      - 3.12.3.33 ST_SRID
    - 3.12.4 Operations
      - 3.12.4.1 ST_Aggr_ConvexHull
      - 3.12.4.2 ST_Aggr_Intersection
      - 3.12.4.3 ST_Aggr_Union
      - 3.12.4.4 ST_Bin
      - 3.12.4.5 ST_BinEnvelope
      - 3.12.4.6 ST_Boundary
      - 3.12.4.7 ST_Buffer
      - 3.12.4.8 ST_ConvexHull
      - 3.12.4.9 ST_Difference
      - 3.12.4.10 ST_Envelope
      - 3.12.4.11 ST_ExteriorRing
      - 3.12.4.12 ST_InteriorRingN
      - 3.12.4.13 ST_Intersection
      - 3.12.4.14 ST_SymmetricDiff
      - 3.12.4.15 ST_Union
    - 3.12.5 Relationship tests
      - 3.12.5.1 ST_Contains
      - 3.12.5.2 ST_Crosses
      - 3.12.5.3 ST_Disjoint
      - 3.12.5.4 ST_EnvIntersects
      - 3.12.5.5 ST_Equals
      - 3.12.5.6 ST_Intersects
      - 3.12.5.7 ST_Overlaps
      - 3.12.5.8 ST_Relate
      - 3.12.5.9 ST_Touches
      - 3.12.5.10 ST_Within
    - 3.12.6 Geohash index functions
      - 3.12.6.1 ST_GeoHash
      - 3.12.6.2 ST_PointFromGeoHash
      - 3.12.6.3 ST_EnvelopeFromGeoHash
      - 3.12.6.4 ST_GeoHashNeighbours
    - 3.12.7 S2 mesh functions
      - 3.12.7.1 ST_S2CellIdsFromGeom
      - 3.12.7.2 ST_S2CellIdsFromText
      - 3.12.7.3 ST_S2CellCenterPoint
      - 3.12.7.4 ST_S2CellNeighbours
    - 3.12.8 Geodesic functions
      - 3.12.8.1 ST_AreaWGS84
      - 3.12.8.2 ST_DistanceWGS84
      - 3.12.8.3 ST_BufferWGS84
      - 3.12.8.4 ST_GeodesicDistance
      - 3.12.8.5 ST_Distance_Sphere
      - 3.12.8.6 ST_Area_Sphere
    - 3.12.9 R-tree index functions
      - 3.12.9.1 ST_BuildRTreeIndex
      - 3.12.9.2 ST_ContainsFromRTree
      - 3.12.9.3 ST_CrossesFromRTree
      - 3.12.9.4 ST_EqualsFromRTree
      - 3.12.9.5 ST_IntersectsFromRTree
      - 3.12.9.6 ST_OverlapsFromRTree
      - 3.12.9.7 ST_TouchesFromRTree
      - 3.12.9.8 ST_WithinFromRTree
      - 3.12.9.9 ST_KNNFromRTree
    - 3.12.10 Other functions
      - 3.12.10.1 ST_IsValid
      - 3.12.10.2 ST_Transform
  - 3.13 MaxCompute Hash Clustering
    - 3.13.1 Background information
    - 3.13.2 Descriptions
      - 3.13.2.1 Enable Hash Clustering
      - 3.13.2.2 Create a hash-clustered table
      - 3.13.2.3 Modify table attributes
      - 3.13.2.4 View and verify table attributes
    - 3.13.3 Benefits
      - 3.13.3.1 Bucket pruning and index optimization
      - 3.13.3.2 Aggregation optimization
      - 3.13.3.3 Storage optimization
    - 3.13.4 ShuffleRemove
    - 3.13.5 Limits
  - 3.14 Common MaxCompute SQL parameter settings
    - 3.14.1 Map configurations
    - 3.14.2 Join configurations
    - 3.14.3 Reduce configurations
    - 3.14.4 UDF configurations
    - 3.14.5 MapJoin configurations
    - 3.14.6 Configurations of data skew
  - 3.15 MapReduce-to-SQL conversion for execution
    - 3.15.1 Overview
    - 3.15.2 Configure the MaxCompute client
    - 3.15.3 Configure running settings in DataWorks
    - 3.15.4 View details
    - 3.15.5 Perform operations on the distributed file system
  - 3.16 Analysis of the mapping between SQL input and output fields
    - 3.16.1 Overview
    - 3.16.2 Usage notes
  - 3.17 Common MaxCompute SQL errors and solutions
    - 3.17.1 Data skew
      - 3.17.1.1 Overview
      - 3.17.1.2 GROUP BY data skew
      - 3.17.1.3 DISTRIBUTE BY data skew
      - 3.17.1.4 Data skew caused by JOIN operations
      - 3.17.1.5 Data skew caused by multiple DISTINCT operations
      - 3.17.1.6 Data skew caused by misuse of dynamic partitions
      - 3.17.1.7 Use SKEWJOIN HINT to avoid skewed hot key values
    - 3.17.2 Insufficient computing resources
    - 3.17.3 MaxCompute storage optimization tips
    - 3.17.4 UDF OOM
  - 3.18 Limits of MaxCompute SQL statements
  - 3.19 Appendix
    - 3.19.1 Escape characters
    - 3.19.2 LIKE usage
    - 3.19.3 Regular expressions
    - 3.19.4 Reserved words and keywords
    - 3.19.5 Settings of new data types
    - 3.19.6 ACID semantics of MaxCompute parallel write jobs
- 4 Open source features of MaxCompute

## 1 Java SDK

### 1.1 Java SDK

This document introduces the MaxCompute Java SDK packages and links to the complete API reference. Complete API reference for MaxCompute Use Maven to manage the SDK version. The following shows an example configuration.

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.36.2</version>
</dependency>
```

The MaxCompute SDK includes the following packages:

| Package name | Description |
|---|---|
| odps-sdk-core | Provides the core functionality of MaxCompute. This package encapsulates fundamental concepts and programming interfaces, such as Odps , Project , and Table , as well as Tunnel-related features. |
| odps-sdk-core-internal | Provides extended functionality for MaxCompute. It encapsulates less commonly used concepts and operations, such as Event and XFlow . |
| odps-sdk-commons | Provides infrastructure components for MaxCompute. It includes infrastructure elements such as TableSchema , Column , Record , and OdpsType , as well as various utilities. |
| odps-sdk-udf | Provides programming interfaces for MaxCompute UDFs. |
| odps-sdk-mapred | Provides programming interfaces for MaxCompute MapReduce jobs. |

To download an SDK package, go to Download SDK package. For the SDK packages provided for MaxCompute, if you use a MaxCompute version earlier than V3.8.0, download and use SDK package version **0.27.2**. If you use a MaxCompute version from V3.8.0 to V3.11.0, download and use SDK package version **0.30.8** or **0.30.9**. If you use MaxCompute V3.12.0 or later, download and use SDK package version **0.36.2**.

### 1.2 Prerequisites

#### 1.2.1 Overview

Before you use MaxCompute SDKs, you must prepare the required environment. Create an Alibaba Cloud account that is authorized to access MaxCompute and obtain an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. Obtain the endpoint of MaxCompute.

#### 1.2.2 Obtain an AccessKey pair

##### 1.2.2.1 Log on to the Apsara Uni-manager Management Console

This topic describes how to log on to the Apsara Uni-manager Management Console. The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters such as the exclamation point (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%).
3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations in the
following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**. For more information, see the **Manage MFA** section in **Apsara Uni-manager Management Console User**
**Guide**.

##### 1.2.2.2 Obtain the AccessKey pair of an organization

This topic describes how to obtain the AccessKey pair of an organization. Only the operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the Organizations navigation tree, find the organization that you want to add and click the
icon on the right of an organization.
5. Select **AccessKey** from the drop-down list.
6. In the message that appears, view the AccessKey pair of the organization.
An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations of the level-1 organization use the AccessKey pair of the level-1 organization.

##### 1.2.2.3 Obtain the AccessKey pair of an Alibaba Cloud account

To ensure the security of cloud resources, the system must verify the identity of visitors and ensure that they have the relevant permissions. You must obtain the AccessKey ID and AccessKey secret of your Apsara Stack tenant to access cloud resources. This topic describes how to obtain the AccessKey pair of an Alibaba Cloud account.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.
The AccessKey pair provides full access to cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

#### 1.2.3 Obtain an endpoint

This topic describes how to obtain the endpoint of MaxCompute in the Apsara Uni-manager Operations Console. The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domainid.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser. In the address bar, enter the URL (ops.asconsole.intranet-domain-id.com). Then, press Enter.
You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, the password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
3. Click **Log On** to log on to the Apsara Uni-manager Operations Console.
4. In the top navigation bar of the Apsara Uni-manager Operations Console, click **O&M**. In the left-side navigation pane,
choose **Product Management > Products**. In the **Apsara Stack O&M** section, click **Apsara Infrastructure**
**Management Framework**.
5. In the left-side navigation pane, choose **Operations > Machine Operations**. The **Machine Operations** page
appears.
6. In the Machines search box, search for a machine. Click **Terminal** in the Actions column of the machine to log on to
the machine.
7. Run the following command on the machine to obtain JSON data:

```bash
curl -l "http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?c.sr.service_registration"
```

8. Find the endpoint of MaxCompute based on the service ID (odps-service-frontend) and the key value (odps_frontend_
server.endpoint) of MaxCompute.

### 1.3 Major APIs

#### 1.3.1 AliyunAccount

This topic describes the AliyunAccount API provided by SDK for Java. You can call this API to obtain your Alibaba Cloud account. The input parameters are **accessId** and **accessKey**. This API is also considered a class that is used to initialize MaxCompute.
**accessId** indicates the AccessKey ID that uniquely identifies an Alibaba Cloud account. **accessKey**
indicates the AccessKey secret that is used to authenticate the identity of the account.

#### 1.3.2 Odps

This topic describes the Odps API provided by SDK for Java. This API is also considered a class that is the entry point of MaxCompute SDK for Java. This class allows you to access all types of objects in MaxCompute, including projects, tables, resources, functions, and instances. You can pass this class into the AliyunAccount instance to construct a MaxCompute object. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}`

#### 1.3.3 Projects

This topic describes the Projects API provided by SDK for Java. This API is a collection of all projects in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Project p = odps.projects().get("my_exists"); p.reload(); Map<String, String> properties = prj.getProperties(); ...
```

#### 1.3.4 Project

This topic describes the Project API provided by SDK for Java. This API provides descriptions of projects. You can call the Projects API to obtain the projects.

#### 1.3.5 SQLTask

This topic describes the SQLTask API provided by SDK for Java. You can call this API to run and process SQL tasks. You can use SQLTask.run to run SQL tasks. SQLTask.run returns an instance, and obtains the running status and results of SQL tasks from the instance. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance instance = SQLTask.run(odps, "my_project", "select ...") ; String id = instance.getId(); instance.waitforsuccess(); Set<String> taskNames = instance.getTaskNames(); for (String name taskNames) { TaskSummary summary = instance.getTaskSummary(name); String s = summary.getSummaryText();
```

`}`

```
Map<String, String> results = instance.getTaskResults(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { String result = results.get(status.getKey());
```

`}` To create a table, you must call the SQLTask API instead of the Table API. In this case, you must pass the CREATE TABLE statement into SQLTask.

#### 1.3.6 Instances

This topic describes the Instances API provided by SDK for Java. This API is a collection of all instances in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Instance i : odps.instances ()) { ....
```

`}`

#### 1.3.7 Instance

This topic describes the Instance API provided by SDK for Java. This API provides descriptions of instances. You can call the Instances API to obtain the instances. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps (account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Instance ins = odps.instances().get("instance id"); Date startTime = instance.getStartTime(); Date endTime = instance.getEndTime(); ... Status instanceStatus = instance.getStatus(); String instanceStatusStr = null; if (instanceStatus == Status.TERMINATED) { instanceStatusStr = TaskStatus.Status.SUCCESS.toString(); Map<String, TaskStatus> taskStatus = instance.getTaskStatus(); for (Entry<String, TaskStatus> status : taskStatus.entrySet()) { if (status.getValue().getStatus() ! = TaskStatus.Status.SUCCESS) { instanceStatusStr = status.getValue().getStatus().toString(); break;
```

`}` `}`

```
} else { instanceStatusStr = instanceStatus.toString();
```

`}`

```
... TaskSummary summary = instance.getTaskSummary("instance name"); String s = summary.getSummaryText();
```

#### 1.3.8 Tables

This topic describes the Tables API provided by SDK for Java. This API is a collection of tables in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Table t : odps.tables()) { ....
```

`}`

#### 1.3.9 Table

This topic describes the Table API provided by SDK for Java. This API provides descriptions of tables in MaxCompute. You can call the Tables API to obtain the tables. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Table t = odps.tables().get("table name"); t.reload(); Partition part = t.getPartition(new PartitionSpec(tableSpec[1])); part.reload(); ...
```

#### 1.3.10 Resources

This topic describes the Resources API provided by SDK for Java. This API is a collection of resources in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Resource r : odps.resources()) { ....
```

`}`

#### 1.3.11 Resource

This topic describes the Resource API provided by SDK for Java. This API provides descriptions of resources. You can call the Resources API to obtain the resources. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Resource r = odps.resources().get("resource name"); r.reload(); if (r.getType() == Resource.Type.TABLE) { TableResource tr = new TableResource(r); String tableSource = tr.getSourceTable().getProject() + "." + tr.getSourceTable().getName(); if (tr.getSourceTablePartition() ! = null) { tableSource += " partition(" + tr.getSourceTablePartition().toString() + ")";
```

`}`

```
....
```

`}` The following sample code shows how to create a file resource:

```
String projectName = "my_porject"; String source = "my_local_file.txt"; File file = new File(source); InputStream is = new FileInputStream(file); FileResource resource = new FileResource(); String name = file.getName(); resource.setName(name); odps.resources().create(projectName, resource, is);
```

The following sample code shows how to create a table resource:

```
TableResource resource = new TableResource(tableName, tablePrj, partitionSpec); //resource.setName(INVALID_USER_TABLE); resource.setName("table_resource_name"); odps.resources().update(projectName, resource);
```

#### 1.3.12 Functions

This topic describes the Functions API provided by SDK for Java. This API is a collection of functions in MaxCompute. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); odps.setDefaultProject("my_project"); for (Function f : odps.functions()) { ....
```

`}`

#### 1.3.13 Function

This topic describes the Function API provided by SDK for Java. This API provides descriptions of functions. You can call the Functions API to obtain the functions. Sample code:

```
Account account = new AliyunAccount("my_access_id", "my_access_key"); Odps odps = new Odps(account); String odpsUrl = "<your odps endpoint>"; odps.setEndpoint(odpsUrl); Function f = odps.functions().get("function name"); List<Resource> resources = f.getResources();
```

The following sample code shows how to create a function:

```
String resources = "xxx:xxx"; String classType = "com.aliyun.odps.mapred.open.example.WordCount"; ArrayList<String> resourceList = new ArrayList<String>(); for (String r : resources.split(":")) { resourceList.add(r);
```

`}`

```
Function func = new Function(); func.setName(name); func.setClassType(classType); func.setResources(resourceList); odps.functions().create(projectName, func);
```

#### 1.3.14 Spark Shell

This topic describes the Spark Shell API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the Spark directory. $bin/spark-shell --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
sc.parallelize(0 to 100, 2).collect sql("show tables").show sql("select * from spark_user_data").show(200,100)
```

#### 1.3.15 Spark R

This topic describes the Spark R API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$mkdir -p /home/admin/R && unzip . /R/R.zip -d /home/admin/R/ -- Create a directory named R and decompress R.zip in the directory. $export PATH=/home/admin/R/bin/:$PATH -- Configure environment variables. $bin/sparkR --master yarn --archives . /R/R.zip -- Select the running mode and enable the API.
```

Sample code:

```
df <- as.DataFrame(faithful)
```

`df`

```
head(select(df, df$eruptions)) head(select(df, "eruptions")) head(filter(df, df$waiting < 50)) results <- sql("FROM spark_user_data SELECT *") head(results)
```

#### 1.3.16 Spark SQL

This topic describes the Spark SQL API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$cd $SPARK_HOME -- Access the Spark directory. $bin/spark-sql --master yarn -- Select the running mode and enable the API.
```

Sample code:

```
show tables; select * from spark_user_data limit 3; quit;
```

#### 1.3.17 Spark JDBC

This topic describes the Spark JDBC API provided by SDK for Java. This API is commonly used by Spark to submit tasks to a cluster. Run the following commands to enable the API:

```
$sbin/stop-thriftserver.sh -- Stop a thread. $sbin/start-thriftserver.sh -- Restart a thread. $bin/beeline -- Enable the API.
```

Sample code:

```
! connect jdbc:hive2://localhost:10000/odps_smoke_test show tables; select * from mr_input limit 3; ! quit
```

#### 1.3.18 Document APIs

This topic describes the Document APIs provided by SDKs for Java. Document APIs are a set of open source APIs that are compatible with Elasticsearch on MaxCompute. For more information, see Document APIs.

#### 1.3.19 Search APIs

This topic describes the Search APIs provided by SDK for Java. It is an open source API repository that is compatible with Elasticsearch on MaxCompute. For more information, see Search APIs.

#### 1.3.20 CheckPermissionTest

This topic describes the CheckPermissionTest API provided by SDK for Java. You can call this API to check whether a specified user has the specified permission on a resource. Sample code:

```java
Account account = new AliyunAccount("accessId", "accessKey"); Odps odps = new Odps(account); SecurityManager sm = odps.projects().get().getSecurityManager(); SecurityManager.PermissionDesc desc = new SecurityManager.PermissionDesc(
    odps.getDefaultProject(),
    CheckPermissionConstants.ObjectType.Table,
    "table_name",
    CheckPermissionConstants.ActionType.Describe);
desc.setColumns(Arrays.asList("col1", "col2")); desc.setPrincipal("ALIYUN$t***@aliyun.com"); SecurityManager.CheckPermissionResultInfo res = sm.checkPermission(desc); System.out.println("Result: " + res.getResult()); System.out.println("Message: " + res.getMessage());
```

#### 1.3.21 Volume2

This topic describes the Volume2 API provided by SDK for Java. If you use the Volume2 API on Apsara Stack with type set to `new` , you do not need to specify Apsara Stack external volumn information, such as `extLocationt` .

**Project dependency**

Before you manage external volumes by using the SDK for Java, you need to add the following dependency:

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-core</artifactId>
  <version>0.44.0-SNAPSHOT</version>
</dependency>
```

**Create an external volume**

Create

```
/**
* Create an external volume.
* @param builder Parameter settings of the external volume
* @throws OdpsException
```

`*/`

```
public void create(VolumeBuilder builder) throws OdpsException
    /**
* Create an external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the external volume for the
VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @throws OdpsException
```

`*/`

```
public void create(String volumeName, String comment, Volume.Type type)
    /**
* Create an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the external volume for the
VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type)
    /**
* Create an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @param comment
* @param type Create the original external volume {@link Volume}.Type.Old,Create the external volume for the
VolumeFS feature{@link Volume} *. Type.New. The VolumeFS feature can be used only if the feature is enabled for the project.
* @param lifecycle Lifecycle
* @throws OdpsException
```

`*/`

```
public void create(String projectName, String volumeName, String comment, Volume.Type type, Long lifecycle) t hrows OdpsException
```

`/*`

```
 Create an external volume.
```

`*/`

```
public void createExternalVolume() throws Exception {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    String externalLocation = "oss://...";
    Long lifecycle;
    String comment;
    String roleArn;
    Volumes.VolumeBuilder builder = new Volumes.VolumeBuilder();
builder.project(projectName).volumeName(extVolumeName).type(Volume.Type.EXTERNAL).extLocation(externalLocation)
    if (lifecycle != null) {
        builder.lifecycle(lifecycle);
```

`}`

```
    if (comment != null) {
        builder.comment(comment);
```

`}`

```
    if (roleArn != null) {
        builder.addProperty(Volumes.EXTERNAL_VOLUME_ROLEARN_KEY, roleArn);
```

`}`

```
    getCurrentOdps().volumes().create(builder);
```

`}`

**Obtain the information about a specified external volume**

Get

```
/**
* Obtain the information about a specified external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @return
```

`*/`

```
public Volume get(String volumeName) /**
* Obtain the information about a specified external volume.
```

`*`

```
* @param projectName Name of the project
* @param volumeName Name of the external volume
* @return
```

`*/`

```
public Volume get(String projectName, String volumeName)
```

`/*`

```
Obtain the information about a specified external volume.
```

`*/`

```
public Volume getVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    Volume volume = odps.volumes().get(projectName, extVolumeName);
    return volume;
```

`}`

**Obtain an external volume iterator**

Iterator

```
/**
* Obtain all external volume iterators of the default project.
```

`*`

```
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator()
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param projectName Name of the project
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final String projectName)
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param filter Filter condition
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final VolumeFilter filter)
    /**
* Obtain the external volume iterator.
```

`*`

```
* @param projectName Name of the project
* @param filter Filter condition
* @return Volume iterator
```

`*/`

```
public Iterator<Volume> iterator(final String projectName, final VolumeFilter filter)
```

`/*`

```
Obtain an external volume iterator.
```

`*/`

```
public Iterator<Volume> getVolumeIterator() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    VolumeFilter volumeFilter = new VolumeFilter();
    volumeFilter.setName(extVolumeName);
    Iterator<Volume> iterator = odps.volumes().iterator(projectName, volumeFilter);
    return iterator;
```

`}`

**Delete an external volume**

Delete

```
/**
* Delete an external volume.
```

`*`

```
* @param volumeName Name of the external volume
* @throws OdpsException
```

`*/`

```
public void delete(String volumeName) /**
* Delete an external volume.
```

`*`

```
* @param projectName Name of the project to which the external volume belongs
* @param volumeName Name of the external volume
* @throws OdpsException
```

`*/`

```
public void delete(String projectName, String volumeName)
```

`/*`

```
Delete an external volume.
```

`*/`

```
public void deleteVolume() {
    String projectName = "test_project";
    String extVolumeName = "test_ext_1";
    try {
        odps.volumes().delete(projectName, extVolumeName);
    } catch (OdpsException e) {
        throw new RuntimeException(e);
```

`}` `}`

**Obtain the FS file of an external volume**

getVolumeFSFile

```
/**
* Obtain the FS file of an external volume from a path.
```

`*`

```
* @param path The path
```

`*` `*/`

```
public VolumeFSFile getVolumeFSFile(String path) throws VolumeException;
```

`/*`

```
Obtain detailed information about the FS file of an external volume.
```

`*/`

```
public void getVolumeIterator() {
    String projectName = "test_project";
    String volumeName = "test_volume";
    String testFilePath = "/" + volumeName + "/file";;
    VolumeFSFile volumeFSFile = odps.volumes().get(projectName, volumeName).getVolumeFSFile(testFilePath);
    bool isDir = volumeFSFile.getIsdir());
    long length = volumeFSFile.getLength();
```

`}`

## 2 SDK for Python

This topic describes how to use SDK for Python to create, view, and delete tables. PyODPS is MaxCompute SDK for Python. It provides easy-to-use Python programming interfaces. Similar to pandas, PyODPS provides fast, flexible, and expressive data structures. You can use the data processing feature of PyODPS, which is similar to that of pandas, by calling the DataFrame API provided by PyODPS. For more information, see aliyunodps-python-sdk and PyODPS: ODPS Python SDK and data analysis framework. For more information about PyODPS, see the relevant description in MaxCompute User Guide. The following sections describe how to use SDK for Python to create, view, and delete tables.

**Install PyODPS**

PyODPS supports Python 2.6 and later (including Python 3.0). After you install pip in the system, you need only to run the `pip install pyodps` command. After you run this command, related dependencies of PyODPS are automatically installed. For more information, see the **Installation guide** section in MaxCompute User Guide.

**Perform initialization**

Use your Apsara Stack tenant account to initialize a MaxCompute entry object. Example:

```python
from odps import ODPS odps = ODPS('**your-access-id**', '**your-secret-access-key**', '**your-default-project**',
            endpoint='**your-end-point**')
```

After initialization, you can perform operations on tables, resources, and functions. Unless otherwise specified, **objects** in the following sections all refer to MaxCompute entry objects.

**Obtain a PyODPS project**

A project is the basic organizational unit in MaxCompute, similar to a database.

| You can call the | get project _ | method to obtain information about a project. Example: |
|---|---|---|
| project = odps.get project('my project') # Obtain information about a project. _ _ project = odps.get project() # Obtain information about the default project. _ |   |   |

If no parameters are specified, information about the default project is obtained. You can call the `exist_project` method to check whether a project exists. A table is the data storage unit in MaxCompute.

**Perform operations on PyODPS tables**

| Call the | list tables _ | method to query all tables in a project. Example: |
|---|---|---|
| for table in odps.list tables(): # Process each table. _ |   |   |

Call the `exist_table` method to check whether a table exists. Call the `get_table` method to obtain information about a table.

```
 t = odps.get_table('dual')
 t.schema
odps.Schema {
  c_int_a                 bigint
  c_int_b                 bigint
  c_double_a              double
  c_double_b              double
  c_string_a              string
  c_string_b              string
  c_bool_a                boolean
  c_bool_b                boolean
  c_datetime_a            datetime
  c_datetime_b            datetime
```

`}`

```python
 t.lifecycle
 print(t.creation_time)
2014-05-15 14:58:43
 t.is_virtual_view
False
 t.size
 t.schema.columns
[<column c_int_a, type bigint>,
 <column c_int_b, type bigint>,
 <column c_double_a, type double>,
 <column c_double_b, type double>,
 <column c_string_a, type string>,
 <column c_string_b, type string>,
 <column c_bool_a, type boolean>,
 <column c_bool_b, type boolean>,
 <column c_datetime_a, type datetime>,
 <column c_datetime_b, type datetime>]
```

**Create the schema of a PyODPS table**

Use one of the following methods to initialize the schema of a PyODPS table: Initialize the schema by using table columns and optional partitions.

| from odps.models import Schema, Column, Partition columns = [Column(name='num', type='bigint', comment='the column')] partitions = [Partition(name='pt', type='string', comment='the partition')] schema = Schema(columns=columns, partitions=partitions) schema.columns [<column num, type bigint>, <partition pt, type string>] |   |   |
|---|---|---|
| Call the | Schema.from lists _ | method. Although this method is more convenient, you cannot directly set comments |

for columns and partitions when you use this method.

```
 schema = Schema.from_lists(['num'], ['bigint'], ['pt'], ['string'])
 schema.columns
[<column num, type bigint>, <partition pt, type string>]
```

**Create a PyODPS table**

You can use a table schema to create a table. Example:

```
table = odps.create_table('my_new_table', schema) table = odps.create_table('my_new_table', schema, if_not_exists=True) # Create a table only if no table with t he same name exists. table = o.create_table('my_new_table', schema, lifecycle=7) # Set the lifecycle of the table.
```

You can also use a comma-delimited string of field names and field data types to create a table. Example:

```bash
 # Create a non-partitioned table.
 table = o.create_table('my_new_table', 'num bigint, num2 double', if_not_exists=True)
 # Create a partitioned table with table columns and partitions specified.
 table = o.create_table('my_new_table', ('num bigint, num2 double', 'pt string'), if_not_exists=True)
```

When you create a table, you can only use the BIGINT, DOUBLE, DECIMAL, STRING, DATETIME, BOOLEAN, MAP, and ARRAY data types, unless otherwise specified. To use other data types, such as TINYINT and STRUCT, you can set `options.sql.use_odps2_extension` to True. Example:

```python
 from odps import options
 options.sql.use_odps2_extension = True
 table = o.create_table('my_new_table', 'cat smallint, content struct<title:varchar(100), body string>')
```

**Obtain PyODPS table data**

Use one of the following methods to obtain table data:

| Call the | head | method to retrieve up to the first 10,000 data records in a table. Example: |   |
|---|---|---|---|
| t = odps.get table('dual') _ for record in t.head(3): print(record[0]) # Obtain the value at position 0. print(record['c double a']) # Obtain a value based on a field. _ _ print(record[0: 3]) # Perform slicing operations. print(record[0, 2, 3]) # Obtain values at multiple positions. print(record['c int a', 'c double a']) # Obtain values based on multiple fields. _ _ _ _ |   |   |   |
| Call the | open reader _ |   | method for a table to open a reader and use the reader to read the table data. You can open |

the reader with or without a WITH clause.

| # Open the reader with a WITH clause: with t.open reader(partition='pt=test') as reader: _ count = reader.count for record in reader[5:10] # You can execute the statement multiple times until all records are read. T he number of records is specified by count. You can change it to parallel-operation code. # Process a record. # Open the reader without a WITH clause: reader = t.open reader(partition='pt=test') _ count = reader.count for record in reader[5:10] # Process a record. |   |   |
|---|---|---|
| Call the Tunnel API to read table data. The | open reader _ | method encapsulates the Tunnel API. |

**Use PyODPS to write data**

Similar to `open_reader` , you can use `open_writer` for a table to open a writer and use the writer to write data to a table. Example:

```bash
 # Open the writer with a WITH clause:
 with t.open_writer(partition='pt=test') as writer:
     writer.write(records)  # records can be iterable records and are written to block 0 by default.
 with t.open_writer(partition='pt=test', blocks=[0, 1]) as writer:  # Enable two blocks.
     writer.write(0, gen_records(block=0))
     writer.write(1, gen_records(block=1))  # The two write operations can be performed at the same time by usi
ng the multithreading technology. Each block is independent.
 # Open the writer without a WITH clause:
 writer = t.open_writer(partition='pt=test', blocks=[0, 1])
 writer.write(0, gen_records(block=0))
 writer.write(1, gen_records(block=1))
 writer.close()  # You must close the writer. Otherwise, the written data may be incomplete.
```

Writing data to a table is a process that encapsulates the Tunnel API.

**Delete a PyODPS table**

Delete a table. Example:

```
 odps.delete_table('my_table_name', if_exists=True)  #  Delete a table only if the table exists.
 t.drop()  # Call the drop() method to delete a table if the table exists.
```

**Perform operations on PyODPS table partitions**

Basic operations Traverse all partitions of a table. Example:

```python
 for partition in table.partitions:
     print(partition.name)
 for partition in table.iterate_partitions(spec='pt=test'):
     # Traverse subpartitions.
```

Check whether a partition exists. Example:

```
table.exist_partition('pt=test,sub=2019')
```

Obtain information about a partition. Example:

```python
 partition = table.get_partition('pt=test')
 print(partition.creation_time)
2019-09-18 22:22:27
 partition.size
```

Create a partition

```
t.create_partition('pt=test', if_not_exists=True) # Create a partition only if no partition with the same nam e exists. t.delete_partition('pt=test', if_exists=True) # Delete a partition only if the partition exists.
 Use the drop() method to delete a partition only if the partition exists.
```

**PyODPS SQL**

PyODPS supports MaxCompute SQL queries and provides methods to obtain query results. Execute SQL statements

```
odps.execute_sql('select * from dual') # Execute SQL statements in synchronous mode. Threads are blocked un til the SQL statements are executed. instance = odps.run_sql('select * from dual') # Execute SQL statements in asynchronous mode. instance.wait_for_success() # Threads are blocked until the SQL statements are executed.
```

Obtain SQL query results You can call the `open_reader` method to obtain SQL query results. In the following example, structured data is returned.

| with odps.execute sql('select * from dual').open reader() as reader: _ _ for record in reader: # Process each record. |   |   |   |   |
|---|---|---|---|---|
| When you run the | DESC | command, you can use | reader.raw | to obtain the raw SQL query results. |
| with odps.execute sql('desc dual').open reader() as reader: _ _ print(reader.raw) |   |   |   |   |

**PyODPS Resource**

Resources commonly apply to user-defined functions (UDFs) and MapReduce on MaxCompute.

| list resources _ |   | method |
|---|---|---|
| and the | delete resource _ |   |

You can call the `list_resources` method to query all resources, the `exist_resource` method to check whether a resource exists, and the `delete_resource` method to delete a resource. You can also call the `drop()` method to delete a resource. PyODPS supports two resource types: files and tables. File resources Files of basic file types and the .py, .jar, and .archive types are supported. Create a file resource You can specify a resource name, a file type, and a **file-like** or string object to create a file resource. Example:

```
resource = odps.create_resource('test_file_resource', 'file', file_obj=open('/to/path/file')) # Create a f ile-like object. resource = odps.create_resource('test_py_resource', 'py', file_obj='import this') # Create a string object
```

`.` Read and modify a file resource

| open resource _ |   | meth |
|---|---|---|
| t. Similar to the | open |   |

You can call the `open` method for a file resource or call the `open_resource` method at the MaxCompute entry to open a file resource. The opened object is a **file-like** object. Similar to the `open` method built in Python, file resources also support various opening modes. Example:

```
 with resource.open('r') as fp:  # Open the file in read mode.
    content = fp.read()  # Read all content.
     fp.seek(0)  # Return to the beginning of the file.
     lines = fp.readlines()  # Read multiple lines.
     fp.write('Hello World')  # Error. Data cannot be written to a file in read mode.
 with odps.open_resource('test_file_resource', mode='r+') as fp:  # Open the file in read/write mode.
     fp.read()
     fp.tell()  # Current position.
     fp.seek(10)
     fp.truncate()  # Truncate the file to the specified length.
     fp.writelines(['Hello\n', 'World\n'])  # Write multiple lines into the file.
     fp.write('Hello World')
     fp.flush()  # Manually call the method to submit the update to MaxCompute.
```

PyODPS supports the following opening modes: r: read mode. The file can be opened but data cannot be written to it. w: write mode. Data can be written to the file, but data in the file cannot be read. If a file is opened in write mode, the file content is deleted first. a: append mode. Data can be appended to the file. r+: read/write mode. You can read data from and write data to the file. w+: This mode is similar to r+, but the file content is deleted first. a+: This mode is similar to r+, but data can only be appended to the file. In PyODPS, file resources can be opened in binary mode. For example, some compressed files must be opened in binary mode. **rb** indicates that a file is opened in binary read mode, and **r+b** indicates that a file is opened in binary read/write mode. Table resources Create a table resource.

```
 odps.create_resource('test_table_resource', 'table', table_name='my_table', partition='pt=test')
```

Update a table resource.

```
 table_resource = odps.get_resource('test_table_resource')
 table_resource.update(partition='pt=test2', project_name='my_project2')
```

**DataFrame**

PyODPS provides a pandas-like API called PyODPS DataFrame. This API makes full use of the computing power of MaxCompute. For more information, see DataFrame. The following DataFrame examples are provided for reference only. You must create a MaxCompute object before you perform the following steps.

```
 odps = ODPS('**your-access-id**', '**your-secret-access-key**',
             project='**your-project**', endpoint='**your-end-point**'))
```

Assume that the following tables exist: **pyodps_ml_100k_movies** (movie-related data), **pyodps_ml_100k_users** (user-related data), and **pyodps_ml_100k_ratings** (rating-related data). You need only to specify a table object to create a DataFrame object. Example:

```
 from odps.df import DataFrame
 users = DataFrame(o.get_table('pyodps_ml_100k_users'))
```

You can use the **dtypes** attribute to view the fields of DataFrame and the types of these fields. Example:

```
users.dtypes
```

You can call the `head` method to obtain the first N data records for data preview. Example:

```
 users.head(10)
```

| number | user id _ | age | sex | occupation | zip code _ |
|---|---|---|---|---|---|
| 0 | 1 | 24 | M | technician | 85711 |
| 1 | 2 | 53 | F | other | 94043 |
| 2 | 3 | 23 | M | writer | 32067 |
| 3 | 4 | 24 | M | technician | 43537 |
| 4 | 5 | 33 | F | other | 15213 |
| 5 | 6 | 42 | M | executive | 98101 |
| 6 | 7 | 57 | M | administrator | 91344 |
| 7 | 8 | 36 | M | administrator | 05201 |
| 8 | 9 | 29 | M | student | 01002 |
| 9 | 10 | 53 | M | lawyer | 90703 |

You can add a filter on the fields to view specified fields. Example:

```
 users[['user_id', 'age']].head(5)
```

| number | user id _ | age |
|---|---|---|
| 0 | 1 | 24 |
| 1 | 2 | 53 |
| 2 | 3 | 23 |
| 3 | 4 | 24 |
| 4 | 5 | 33 |

You can also exclude several fields from results. Example:

```
users.exclude('zip_code', 'age').head(5)
```

| number | user id _ | sex | occupation |
|---|---|---|---|
| 0 | 1 | M | technician |
| 1 | 2 | F | other |
| 2 | 3 | M | writer |
| 3 | 4 | M | technician |
| 4 | 5 | F | other |

If you exclude some fields, you may want to obtain new columns by using computation. For example, add the sex_bool attribute and set this attribute to True if sex is M. Otherwise, set this attribute to False. Example:

```
users.select(users.exclude('zip_code', 'sex'), sex_bool=users.sex == 'M').head(5)
```

| number | user id _ | age | occupation | sex bool _ |
|---|---|---|---|---|
| 0 | 1 | 24 | technician | True |
| 1 | 2 | 53 | other | False |
| 2 | 3 | 23 | writer | True |

| 3 | 4 | 24 | technician | True |
|---|---|---|---|---|
| 4 | 5 | 33 | other | False |

Obtain the number of users aged between 20 and 25. Example:

```
users.age.between(20, 25).count().rename('count')
```

Obtain the numbers of male and female users. Example:

```
users.groupby(users.sex).count()
```

| number | sex | count |
|---|---|---|
| 0 | F | 273 |
| 1 | M | 670 |

To divide users by occupation, obtain the top 10 occupations, and sort the occupations in descending order based on population. Example:

```
df = users.groupby('occupation').agg(count=users['occupation'].count()) df.sort(df['count'], ascending=False)[:10]
```

| number | occupation | count |
|---|---|---|
| 0 | student | 196 |
| 1 | other | 105 |
| 2 | educator | 95 |
| 3 | administrator | 79 |
| 4 | engineer | 67 |
| 5 | programmer | 66 |
| 6 | librarian | 51 |
| 7 | writer | 45 |
| 8 | executive | 32 |
| 9 | scientist | 31 |

The DataFrame API provides the value_counts method for the same purpose. Example:

```
users.occupation.value_counts()[:10]
```

| number | occupation | count |
|---|---|---|
| 0 | student | 196 |
| 1 | other | 105 |
| 2 | educator | 95 |
| 3 | administrator | 79 |
| 4 | engineer | 67 |
| 5 | programmer | 66 |
| 6 | librarian | 51 |
| 7 | writer | 45 |
| 8 | executive | 32 |

| 9 | scientist | 31 |
|---|---|---|

Show data in an intuitive graph. Example:

```
 %matplotlib inline
```

Use a horizontal column chart to visualize data. Example:

```
 users['occupation'].value_counts().plot(kind='barh', x='occupation',
ylabel='prefession')
```

Divide users into 30 groups by age and view the histogram of age distribution. Example:

```
users.age.hist(bins=30, title="Distribution of users' ages", xlabel='age', ylabel='count of users')
```

Use JOIN to join three tables and save the joined tables as a new table. Example:

```
movies = DataFrame(o.get_table('pyodps_ml_100k_movies')) ratings = DataFrame(o.get_table('pyodps_ml_100k_ratings')) o.delete_table('pyodps_ml_100k_lens', if_exists=True) lens = movies.join(ratings).join(users).persist('pyodps_ml_100k_lens') lens.dtypes odps.Schema {
  movie_id                            int64
  title                               string
  release_date                        string
  video_release_date                  string
  imdb_url                            string
  user_id                             int64
  rating                              int64
  unix_timestamp                      int64
  age                                 int64
  sex                                 string
  occupation                          string
  zip_code                            string
```

`}` Divide users who are aged from 0 to 80 into eight age groups. Example:

```
 labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
 cut_lens = lens[lens, lens.age.cut(range(0, 81, 10), right=False, labels=labels).rename('age_group')]
```

View the first 10 data records of a single age in a group. Example:

```
cut_lens['age_group', 'age'].distinct()[:10]
```

| number | age group _ | age |
|---|---|---|
| 0 | 0-9 | 7 |
| 1 | 10-19 | 10 |
| 2 | 10-19 | 11 |
| 3 | 10-19 | 13 |
| 4 | 10-19 | 14 |
| 5 | 10-19 | 15 |
| 6 | 10-19 | 16 |
| 7 | 10-19 | 17 |
| 8 | 10-19 | 18 |
| 9 | 10-19 | 19 |

View the total rating and average rating of users in each age group. Example:

```
 cut_lens.groupby('age_group').agg(cut_lens.rating.count().rename('total_rating'),
cut_lens.rating.mean().rename('avg_rating'))
```

| number | age group _ | average rating _ | total rating _ |
|---|---|---|---|
| 0 | 0-9 | 3.767442 | 43 |
| 1 | 10-19 | 3.486126 | 8181 |
| 2 | 20-29 | 3.467333 | 39535 |
| 3 | 30-39 | 3.554444 | 25696 |
| 4 | 40-49 | 3.591772 | 15021 |
| 5 | 50-59 | 3.635800 | 8704 |
| 6 | 60-69 | 3.648875 | 2623 |
| 7 | 70-79 | 3.649746 | 197 |

**Configurations**

PyODPS provides a series of configuration options, which can be obtained by using `odps.options` . The following table describes configurable MaxCompute options. General configurations

| Option | Description | Default value |
|---|---|---|
| end point _ | MaxCompute Endpoint | None |
| default project _ | The default project. | None |
| log view host _ _ | The hostname of Logview. | None |
| log view hours _ _ | The retention time of Logview. Unit: hours. | 24 |
| local timezone _ | The time zone to be used. True indicates local time, and False indicates UTC. You can also use the pytz time zone. | 1 |
| lifecycle | The lifecycle of all tables. | None |
| temp lifecycle _ | The lifecycle of temporary tables. | 1 |
| biz id _ | The ID of a user. | None |
| verbose | Specifies whether to display logs. | False |
| verbose log _ | The log receiver. | None |
| chunk size _ | The size of the write buffer. | 1496 |
| retry times _ | The number of request retries. | 4 |
| pool connections _ | The number of cached connections in the connection pool. | 10 |
| pool maxsize _ | The maximum capacity of the connection pool. | 10 |
| connect timeout _ | The time to wait before the connection times out. | 5 |
| read timeout _ | The time to wait before the read operation times out. | 120 |
| completion size _ | The limit on the number of object completion listing items. | 10 |

| notebook repr widget _ _ | Specifies whether to use interactive graphs. | True |
|---|---|---|
| sql.settings | MaxCompute SQL runs global hints. | None |
| sql.use odps2 extension _ _ | Specifies whether to enable MaxCompute V2.0 language extension. | False |

Data upload and download configurations

| Option | Description | Default value |
|---|---|---|
| tunnel.endpoint | Tunnel Endpoint | None |
| tunnel.use instance tunnel _ _ | Specifies whether to use Instance Tunnel to obtain the upload or download results. | True |
| tunnel.limited instance tunnel _ _ | Specifies whether to limit the number of data records obtained by using Instance Tunnel. | True |
| tunnel.string as binary _ _ | Specifies whether to use bytes instead of unicode for data of the STRING type. | False |

DataFrame configurations

| Option | Description | Default value |
|---|---|---|
| interactive | Specifies whether DataFrame is used in an interactive environment. | Based on the measured value |
| df.analyze | Specifies whether to enable non- MaxCompute built-in functions. | True |
| df.optimize | Specifies whether to enable full DataFrame optimization. | True |
| df.optimizes.pp | Specifies whether to enable DataFrame predicate push optimization. | True |
| df.optimizes.cp | Specifies whether to enable DataFrame column pruning optimization. | True |
| df.optimizes.tunnel | Specifies whether to enable DataFrame tunnel optimization. | True |
| df.quote | Specifies whether to use a double grave accent (``) to mark fields and table names in the backend of MaxCompute SQL. | True |
| df.libraries | The resource name of the third-party library that is used for the DataFrame operation. | None |

PyODPS ML configurations

| Option | Description | Default value |
|---|---|---|
| ml.xflow project _ | The default name of the XFlow project. | algo public _ |
| ml.use model transfer _ _ | Specifies whether to use ModelTransfer to obtain the PMML model. | True |
| ml.model volume _ | The volume name used when ModelTransfer is used. | pyodps volume _ |

## 3 MaxCompute SQL

### 3.1 Overview

#### 3.1.1 Scenarios

This topic describes the scenarios of MaxCompute SQL. MaxCompute SQL offline computing is applicable to scenarios where you need to process terabytes of data but do not require real-time processing. It requires a relatively long time to prepare and submit jobs for MaxCompute SQL offline computing. Therefore, MaxCompute SQL is not well-suited for scenarios where thousands or even tens of thousands of transactions need to be processed per second. MaxCompute SQL online computing provides near real-time (NRT) processing capabilities. The MaxCompute SQL syntax is similar to the SQL syntax. The MaxCompute SQL syntax can be considered a subset of standard SQL. MaxCompute SQL lacks many database features, such as transactions, primary key constraints, and indexes. Therefore, MaxCompute SQL cannot be regarded as a database. The maximum size of each SQL statement supported by MaxCompute is 2 MB.

#### 3.1.2 Reserved words

The keywords of SQL statements are reserved words in MaxCompute. Do not use the reserved words when you name tables, columns, or partitions. If you use the reserved words, an error is reported. Reserved words are not casesensitive. This section lists the common reserved words. For a complete list of reserved words, see Reserved words.

```
% & && ( ) * + - . / ; < <= <> = > >= ? ADD ALL ALTER AND AS ASC BETWEEN BIGINT BOOLEAN BY CASE CAST COLUMN COMMENT CREATE DESC DISTINCT DISTRIBUTE DOUBLE DROP ELSE FALSE FROM FULL GROUP IF IN INSERT INTO IS JOIN LEFT LIFECYCLE LIKE LIMIT MAPJOIN NOT NULL ON OR ORDER OUTER OVERWRITE PARTITION RENAME REPLACE RIGHT RLIKE SELECT SORT STRING TABLE THEN TOUCH TRUE UNION VIEW WHEN WHERE
```

#### 3.1.3 Partitioned table

This topic describes the advantages and disadvantages of MaxCompute partitioned tables. You can specify partition key columns of a partitioned table as filter conditions in WHERE clauses of SELECT statements. This improves SQL query performance and reduces costs. However, some SQL statements for partition operations are less efficient. For example, if more than 10,000 partitions exist in an output table for a job, a large number of parallel operations are performed to write data to partitions. As a result, the SQL statements may fail. If you use a partitioned table, you must properly evaluate the number and levels of partitions based on the data source to ensure query performance and stability. MaxCompute allows a maximum of six levels of partitions in a partitioned table. For some statements, the syntax differs between partitioned and non-partitioned tables. For more information, see DDL statements and DML statements. For more information about the statements that are used to create tables, see Create a table.

#### 3.1.4 Type conversion

##### 3.1.4.1 Explicit conversions of data types

An explicit conversion uses CAST to convert a value type into another one. This topic describes explicit conversions. For more information about CAST, see CAST. The following table lists the explicit conversions supported by MaxCompute SQL.Table 1. Explicit conversions

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|
| BIGINT | N/A | Y | Y | N | N | Y |
| DOUBLE | Y | N/A | Y | N | N | Y |

| STRING | Y | Y | N/A | Y | N | Y |
|---|---|---|---|---|---|---|
| DATETIME | N | N | Y | N/A | N | N |
| BOOLEAN | N | N | N | N | N/A | N |
| DECIMAL | Y | Y | Y | N | N | N/A |

Y indicates that the conversion is supported. N indicates that the conversion is not supported. N/A indicates that the conversion is not required. If the DOUBLE type is converted into the BIGINT type, the fractional part is truncated. Example: **cast(1.6 as**
**bigint) = 1**.
If the STRING type that meets the format of the DOUBLE type is converted into the BIGINT type, the STRING type is first converted into the DOUBLE type and then to the BIGINT type. Therefore, the fractional part is truncated. Example: **cast("1.6" as bigint) = 1**. If the STRING type that meets the format of the BIGINT type is converted into the DOUBLE type, one digit is retained after the decimal point. Example: **cast("1" as double) = 1.0**. To convert a constant string into the DECIMAL type, enclose the constant string within a pair of double quotation marks ("). If the value is not enclosed in quotation marks, it is considered a DOUBLE-type value. Example: **cast("1.234567890123456789" as decimal)**. An unsupported explicit conversion causes an exception. If a conversion fails, the system returns an error and exits. The conversion of the DATETIME type uses the default format **yyyy-mm-dd hh:mi:ss:ff3**. For more information, see Conversion between string and datetime types. Some data types cannot be explicitly converted, but can be converted by using SQL built-in functions. For example, you can use the TO_CHAR function to convert the BOOLEAN type into the STRING type. For more information, see TO_CHAR. You can also use the TO_DATE function to convert the STRING type into the DATETIME type. If the values of the DECIMAL type are not within the value range, the cast string to decimal operation may return an error, such as most significant bit overflow or least significant bit overflow truncation.

##### 3.1.4.2 Implicit type conversion and its scope

An implicit type conversion allows MaxCompute to automatically convert data types based on the context and predefined rules. This topic describes the rules of implicit conversions. The following table lists the rules of implicit conversions supported by MaxCompute. Table 1. Implicit conversion 1

| From/To | BOOLEAN | TINYINT | SMALLINT | INT | BIGINT | FLOAT |
|---|---|---|---|---|---|---|
| BOOLEAN | T | F | F | F | F | F |
| TINYINT | F | T | T | T | T | T |
| SMALLINT | F | F | T | T | T | T |
| INT | F | F | F | T | T | T |
| BIGINT | F | F | F | F | T | T |
| FLOAT | F | F | F | F | F | T |
| DOUBLE | F | F | F | F | F | F |
| DECIMAL | F | F | F | F | F | F |
| STRING | F | F | F | F | F | F |
| VARCHAR | F | F | F | F | F | F |
| TIMESTAMP | F | F | F | F | F | F |
| BINARY | F | F | F | F | F | F |

Table 2. Implicit conversion 2

| From/To | DOUBLE | DECIMAL | STRING | VARCHAR | TIMESTAMP | BINARY |
|---|---|---|---|---|---|---|
| BOOLEAN | F | F | F | F | F | F |
| TINYINT | T | T | T | T | F | F |
| SMALLINT | T | T | T | T | F | F |
| INT | T | T | T | T | F | F |
| BIGINT | T | T | T | T | F | F |
| FLOAT | T | T | T | T | F | F |
| DOUBLE | T | T | T | T | F | F |
| DECIMAL | F | T | T | T | F | F |
| STRING | T | T | T | T | F | F |
| VARCHAR | T | T | T | T | F | F |
| TIMESTAMP | F | F | T | T | T | F |
| BINARY | F | F | F | F | F | T |

T indicates that the conversion is supported. F indicates that the conversion is not supported. If an unsupported implicit conversion is performed, an error is returned. If a conversion fails, the system returns an error and exits. MaxCompute automatically performs implicit conversions on data types based on the context. If the types do not match, you can use the CAST function to explicitly convert data types. The rules of implicit conversions apply to specific scopes. In specific scenarios, only some rules take effect.

**Implicit conversions with relational operators**

Relational operators include =, <>, <, ≤, >, ≥, IS NULL, IS NOT NULL, LIKE, RLIKE, and IN. The rules for implicit conversions that use LIKE, RLIKE, and IN are different from those that use other relational operators. The rules described in this section do not apply to the three operators. The following table lists the rules of implicit conversions when relational operations are used for data of different types. Table 3. Implicit conversions with relational operators

| From/To | BIGINT | DOUBLE | STRING | DATETIME | BOOLEAN | DECIMAL |
|---|---|---|---|---|---|---|
| BIGINT | N/A | DOUBLE | DOUBLE | N | N | DECIMAL |
| DOUBLE | DOUBLE | N/A | DOUBLE | N | N | DECIMAL |
| STRING | DOUBLE | DOUBLE | N/A | DATETIME | N | DECIMAL |
| DATETIME | N | N | DATETIME | N/A | N | N |
| BOOLEAN | N | N | N | N | N/A | N |
| DECIMAL | DECIMAL | DECIMAL | DECIMAL | N | N | N/A |

If an implicit conversion is not supported between two values that you want to compare, the relational operation cannot be performed and an error is returned. For more information about relational operators, see Relational operators.

**Implicit conversion with special relational operators**

Special relational operators include LIKE, RLIKE, and IN. Syntax of LIKE and RLIKE:

```
source like pattern; source rlike pattern;
```

Take note of the following points for the two relational operators in implicit conversions: The **source** and **pattern** parameters of LIKE and RLIKE must be of the STRING type. Other types can neither be involved in the operation nor be implicitly converted into the STRING type. If the value of **source** or **pattern** is NULL, NULL is returned. Syntax of IN:

```
key in (value1, value2,...);
```

Rules of implicit conversions for IN: The data types of the **values** on the right of the IN keyword must be consistent. MaxCompute automatically compares the values in the column specified by **key** and **values** on the right of the IN keyword. If these values are of the BIGINT, DOUBLE, and STRING types, the values are converted into the DOUBLE type for comparison. If these values are of the DATETIME and STRING types, the values are converted into the DATETIME type for comparison. Conversions between other types are not allowed. The memory used by the compiler increases with the number of parameters used in the IN operation. If 5,000 parameters are used in an IN operation, the GCC compiler consumes 17 GB of memory for compilation. We recommend that you limit the number of parameters to 1,024. In this case, the compiler consumes a maximum of 1 GB of memory and requires 39 seconds for compilation.

**Implicit conversions with arithmetic operators**

Arithmetic operators include addition (+), subtraction (−), multiplication (×), division (/), and percent (%). This section describes the rules for implicit conversions that use these operators. Only the STRING, BIGINT, DECIMAL, and DOUBLE types can be used in arithmetic operations. Before an arithmetic operation, STRING data is implicitly converted into DOUBLE data. If an arithmetic operation involves data of the BIGINT and DOUBLE types, BIGINT data is implicitly converted into DOUBLE data. The DATETIME and BOOLEAN types cannot be used in arithmetic operations. For more information about arithmetic operators, see Arithmetic operators.

**Implicit conversions with logical operators**

Logical operators include AND, OR, and NOT. This section describes the rules for implicit conversions that use these operators. Only the BOOLEAN type can be used in logical operations. The other types are not supported by logical operations or implicit conversions. For more information about logical operators, see Logical operators.

##### 3.1.4.3 SQL built-in functions

MaxCompute SQL provides a variety of built-in functions. These functions can be used to calculate one or more columns of a row and provide data of any type. The following rules apply to implicit conversions: If you call a function and the data type of an input parameter is different from that defined in the function, the data type of the input parameter is converted into the function-defined data type. The parameters of each built-in function in MaxCompute SQL have different requirements for implicit conversions. For more information, see Built-in functions.

##### 3.1.4.4 CASE WHEN

This topic describes the implicit conversion rules for CASE WHEN. Implicit conversion rules for CASE WHEN: If return values are of the BIGINT and DOUBLE types, all the values are converted into the DOUBLE type. If return values include those of the STRING type, all the values are converted into the STRING type. If a conversion, such as conversion from BOOLEAN into STRING, fails, an error is returned. Conversions between other types are not allowed.

##### 3.1.4.5 Conversions between the STRING and DATETIME types

MaxCompute supports conversions between the STRING and DATETIME types. The format used in conversions is **yyyy-mm-dd hh:mi:ss.ff3**. Table 1. Valid values of time units

| Time unit | String (not case-sensitive) | Valid value |
|---|---|---|
| Year | yyyy | 0001 to 9999 |
| Month | mm | 01 to 12 |
| Day | dd | 01 to 31 |
| Hour | hh | 00 to 23 |
| Minute | mi | 00 to 59 |
| Second | ss | 00 to 59 |
| Millisecond | ff3 | 00 to 999 |

If the first digit of a valid value for each time unit is 0, 0 cannot be omitted. For example, **2017-1-9**
**12:12:12** is an invalid DATETIME format and it cannot be converted from the STRING type into the
DATETIME type. It must be written as **2017-01-09 12:12:12**. Only the STRING type that meets the preceding format requirements can be converted into the DATETIME type. For example, **cast("2017-12-31 02:34:34" as datetime)** converts **2017-12-31 02:34:34** of the STRING type into the DATETIME type. Similarly, if the DATETIME type is converted into the STRING type, the default conversion format is **yyyy-mm-dd hh:mi:ss**. Conversions that use the following or similar statements may fail, and errors are returned.

```
cast("2017/12/31 02/34/34" as datetime) cast("20171231023434" as datetime) cast("2017-12-31 2:34:34" as datetime)
```

MaxCompute provides the TO_DATE function to convert the STRING type that does not meet the DATETIME format requirements into the DATETIME type. For more information, see TO_DATE.

### 3.2 Operators

#### 3.2.1 Relational operators

This topic describes the relational SQL operators in MaxCompute. Table 1. Relational operators

| Operator | Description |
|---|---|
| A=B | If A or B is NULL, NULL is returned. If A is equal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A<>B | If A or B is NULL, NULL is returned. If A is unequal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A<B | If A or B is NULL, NULL is returned. If A is less than B, TRUE is returned. Otherwise, FALSE is returned. |
| A<=B | If A or B is NULL, NULL is returned. If A is less than or equal to B, TRUE is returned. Otherwise, FALSE is returned. |
| A>B | If A or B is NULL, NULL is returned. If A is greater than B, TRUE is returned. Otherwise, FALSE is returned. |

| A>=B | If A or B is NULL, NULL is returned. If A is greater than or equal to B, TRUE is returned. Otherwise, FALSE is returned. |
|---|---|
| A IS NULL | If A is NULL, TRUE is returned. Otherwise, FALSE is returned. |
| A IS NOT NULL | If A is not NULL, TRUE is returned. Otherwise, FALSE is returned. |
| A LIKE B | If A or B is NULL, NULL is returned. A is a string, and B is the pattern that you want to match. If A matches B, TRUE is returned. Otherwise, FALSE is returned. The percent sign (%) is a wildcard character that matches an arbitrary number of characters. The underscore ( ) is a wildcard character that matches a _ single character. To use these two characters as regular characters, use backslashes (\) to escape them: \% and \ . _ 'aaa'like 'a ' = FALSE 'aaa'like'a%' = TRUE 'aaa'like'aab' = FALSE 'a%b'like'a\%b' = TRUE 'axb'like'a\%b' = FALSE |
| A RLIKE B | If A or B is NULL, NULL is returned. A is a string, and B is a regular expression consisting of string constants. If A matches B, TRUE is returned. Otherwise, FALSE is returned. If B is an empty string, the system returns an error and exits. |
| A IN B | B is a set. If A is NULL, NULL is returned. If A is in B, TRUE is returned. Otherwise, FALSE is returned. If B contains only one element NULL, namely, A IN (NULL), NULL is returned. If B contains NULL, the type of NULL is considered the same as the other elements in B. B must be a constant and have at least one element. All elements must be of the same type. |

The values of the DOUBLE type in MaxCompute are different in precision. We recommend that you do not use the equal sign (=) for comparison between two values of the DOUBLE type. You can deduct a value of the DOUBLE type from the other value of the DOUBLE type and use the absolute value of the difference to determine whether the two values are equal. If the absolute value is negligible, the two values of the DOUBLE type are considered equal. Example:

```
abs(0.9999999999 - 1.0000000000) < 0.000000001 -- 0.9999999999 and 1.0000000000 have a precision of 10 decimal digits, whereas 0.000000001 has a precision of 9 decimal digits. -- 0.9999999999 is considered to be equal to 1.0000000000.
```

ABS is a built-in function provided by MaxCompute to take the absolute value of its input. For more information, see ABS. In most cases, a value of the DOUBLE type in MaxCompute can retain 16 valid digits.

#### 3.2.2 Arithmetic operators

This topic describes arithmetic operators in MaxCompute SQL operators. Table 1. Arithmetic operators

| Operator | Description |
|---|---|
| A + B | If A or B is NULL, NULL is returned. Otherwise, the result of A + B is returned. |
| A - B | If A or B is NULL, NULL is returned. Otherwise, the result of A - B is returned. |
| A * B | If A or B is NULL, NULL is returned. Otherwise, the result of A × B is returned. |

| A / B | If A is NULL, B is NULL or 0 , NULL is returned. Otherwise, the result of A/B is returned. If both A and B are of the BIGINT type, a value of the DOUBLE type is returned. |
|---|---|
| A % B | If A or B is NULL, NULL is returned. Otherwise, the result of A % B is returned. |
| +A | A is returned. |
| -A | If A is NULL, NULL is returned. Otherwise, -A is returned. |

You can use only the values of the STRING, BIGINT, DOUBLE, or DECIMAL type to perform arithmetic operations. You cannot use the values of the DATETIME or BOOLEAN type to perform arithmetic operations. Values of the STRING type are implicitly converted into values of the DOUBLE type before arithmetic operations. If you use the values of the BIGINT and DOUBLE types to perform arithmetic operations, the value of the BIGINT type is implicitly converted into the value of the DOUBLE type before arithmetic operations. A value of the DOUBLE type is returned. If both A and B are of the BIGINT type, a value of the DOUBLE type is returned after you perform the A/B operation. For other arithmetic operations, a value of the BIGINT type is returned.

#### 3.2.3 Bitwise operators

This topic describes bitwise operators in MaxCompute SQL operators. Table 1. Bitwise operators

| Operator | Description |
|---|---|
| A & B | The bitwise AND result of A and B is returned. For example, the result of 1&2 is 0, and the result of 1&3 is 1. The bitwise AND result of NULL and a value is NULL. Both A and B must be of the BIGINT type. |
| A \| B | The bitwise OR result of A and B is returned. For example, the result of 1\|2 is 3, and the result of 1\|3 is 3. The bitwise OR result of NULL and a value is NULL. Both A and B must be of the BIGINT type. |

**Important**

Bitwise operators do not support implicit type conversions. You can use the values only of the BIGINT type in bitwise operations.

#### 3.2.4 Logical operators

This topic describes logical operators in MaxCompute SQL. Table 1. Logical operators

| Operator | Description |
|---|---|
| A and B | TRUE and TRUE = TRUE |
|   | TRUE and FALSE = FALSE |
|   | FALSE and TRUE = FALSE |
|   | FALSE and NULL = FALSE |
|   | FALSE and FALSE = FALSE |
|   | NULL and FALSE = FALSE |
|   | TRUE and NULL = NULL |
|   | NULL and TRUE = NULL |
|   | NULL and NULL = NULL |

| A or B | TRUE or TRUE = TRUE |
|---|---|
|   | TRUE or FALSE = TRUE |
|   | FALSE or TRUE = TRUE |
|   | FALSE or NULL = NULL |
|   | NULL or FALSE = NULL |
|   | TRUE or NULL = TRUE |
|   | NULL or TRUE = TRUE |
|   | NULL or NULL = NULL |
| NOT A | If A is NULL, NULL is returned. |
|   | If A is TRUE, FALSE is returned. |
|   | If A is FALSE, TRUE is returned. |

Logical operators do not support implicit type conversions. You can use only the values of the BOOLEAN type in logical operations.

### 3.3 LOAD

This topic describes how to use LOAD statements to import data from external storage, such as Object Storage Service (OSS), to a table or a table partition in MaxCompute.

**Precautions**

MaxCompute must be authorized to access data in external storage. The methods used to authorize MaxCompute to access external data by using LOAD statements are the same as the methods used to authorize MaxCompute external tables. You can use one of the following methods for authorization: Specify the AccessKey ID and AccessKey secret in the directory in which data is stored. In this example, a directory on OSS is used.

```
'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhou-zmf.aliyuncs.com/my_bucket_id/my_location/'
```

**Important**

If you use this authorization method, you must use the plaintext of the AccessKey ID and AccessKey secret. This may pose security risks. We recommend that you do not use this method. Use Security Token Service (STS). For more information about the STS mode authorization for OSS, see STS mode authorization for OSS.

**Use an extractor or a storage handler to import data**

Syntax

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [STORED BY StorageHandler] [WITH SERDEPROPERTIES (Options)];
```

Parameters:
**table_name**: the name of the destination table into which you want to insert data. You must create a destination
table before you insert data into the table. The schema of the destination table must be the same as the format of the external data.
**LOAD INTO**: inserts data into a table or partition.
**LOAD OVERWRITE**: clears the existing data from a table or partition and inserts data into the table or partition.
**SORTED BY**: specifies the name of the storage handler. You can use this clause in the same way as you use the
clause for MaxCompute external tables.
**LOCATION**: specifies the OSS directory in which the data files you want to read are saved. The system reads all files
in the directory by default.
**WITH SERDEPROPERTIES**: specifies the properties of the MaxCompute external table. The properties supported by
WITH SERDEPROPERTIES are the same as those supported by the MaxCompute external table. For example, the vehicle.csv file contains the following data:

```
1,1,51,1,46.81006,-92.08174,9/14/2014 0:00,S 1,2,13,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,3,48,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,4,30,1,46.81006,-92.08174,9/14/2014 0:00,W 1,5,47,1,46.81006,-92.08174,9/14/2014 0:00,S 1,6,9,1,46.81006,-92.08174,9/14/2014 0:00,S 1,7,53,1,46.81006,-92.08174,9/14/2014 0:00,N 1,8,63,1,46.81006,-92.08174,9/14/2014 0:00,SW 1,9,4,1,46.81006,-92.08174,9/14/2014 0:00,NE 1,10,31,1,46.81006,-92.08174,9/14/2014 0:00,N oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/ -- Save the vehicle.csv file to a folder in an OSS bucket. Obtain the structure of the directory where the MaxC ompute external table is saved. CREATE TABLE ambulance_data_csv_load ( vehicleId INT, recordId INT, patientId INT, calls INT, locationLatitute DOUBLE, locationLongtitue DOUBLE, recordTime STRING, direction STRING ); -- Create a destination table named ambulance_data_csv_load. LOAD OVERWRITE TABLE ambulance_data_csv_load FROM LOCATION 'oss://oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/' STORED BY 'com.aliyun.odps.CsvStorageHandler' WITH SERDEPROPERTIES ( 'odps.properties.rolearn'='acs:ram::xxxxx:role/aliyunodpsdefaultrole', -- The Alibaba Cloud Resource Name (AR N) of the AliyunODPSDefaultRole role. 'odps.text.option.delimiter'=','
```

);

```
-- Import the CSV file from OSS to the destination table.
```

**Import data stored in an open source format**

Syntax

```
LOAD OVERWRITE|INTO TABLE table_name [PARTITION(partcol1=val1, partcol2=val2 ...)] FROM LOCATION external_location [ROW FORMAT SERDE '<serde class>'
  [WITH SERDEPROPERTIES ('odps.properties.rolearn'='${roleran}' [,'name2'='value2',...])]
```

`]`

```
STORED AS <file format>;
```

Parameters:
**table_name**: the name of the destination table into which you want to insert data. You must create a destination
table before you insert data into it. The schema of the destination table must be the same as the format of the external data.
**LOAD INTO**: inserts data into a table or partition.
**LOAD OVERWRITE**: clears the existing data from a table or partition and inserts data into the table or partition.
**STORED AS**: specifies the format of the imported data file. Valid values include ORC, PARQUET, RCFILE,
SEQUENCEFILE, and TEXTFILE. You can use this clause in the same way as you use the clause for MaxCompute external tables.
**ROW FORMAT SERDE**: This clause is optional. You can use this clause in the same way as you use the clause for
MaxCompute external tables. Mappings between file formats and SerDe classes: SEQUENCEFILE: org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe TEXTFILE: org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe RCFILE: org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe ORC: org.apache.hadoop.hive.ql.io.orc.OrcSerde ORCFILE: rg.apache.hadoop.hive.ql.io.orc.OrcSerde PARQUET: org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe AVRO: org.apache.hadoop.hive.serde2.avro.AvroSerDe
**SERDEPROPERTIES**: If you use STS to grant MaxCompute the required permissions, you must use this parameter to
specify the value of the **odps.properties.rolearn** property. This property indicates the ARN of the
**AliyunODPSDefaultRole** role. If the owner of MaxCompute and the owner of OSS use the same account, one-click
authorization is allowed.

```
oss://${accessKeyId}:${accessKeySecret}@oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/ds=20200910/' -- The OSS directory where the MaxCompute external table is saved uses the preceding structure. The MaxCompute external table in the directory does not include partition key columns. The information of partition key column s is included in the directory information. CREATE TABLE ambulance_data_csv_load_pt ( vehicleId STRING, recordId STRING, patientId STRING, calls STRING, locationLatitute STRING, locationLongtitue STRING, recordTime STRING, direction STRING) PARTITIONED BY (ds STRING); -- Create a destination table named ambulance_data_csv_load_pt. LOAD OVERWRITE TABLE ambulance_data_csv_load_pt PARTITION(ds='20200910') FROM LOCATION 'oss://<yourAccessKeyId>:<yourAccessKeySecret>@oss-cn-hangzhou-zmf.aliyuncs.com/bucket/data_location/' ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' STORED AS TEXTFILE; -- Import data stored in open source formats from OSS to the destination table.
```

If you download data to a partitioned table, the schema of the external table in the OSS directory does not include partition key columns. In the preceding example, the external table in the directory contains only the business fields. The table does not include partition key columns.

### 3.4 DDL statements

#### 3.4.1 Table operations

##### 3.4.1.1 Create a table

This topic describes how to use DDL statements to create a table.

```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name [(col_name data_type [DEFAULT value] [COMMENT col_comment], ...)] [COMMENT table_comment] [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] [CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_name [ ASC | DESC] ...])] INTO number_of_buckets BUCKETS] -- Specify the shuffle and sort attributes when you create a clustered table. [STORED BY StorageHandler] -- Used only for external tables. [WITH SERDEPROPERTIES (Options)] -- Used only for external tables. [LOCATION OSSLocation] -- Used only for external tables. [STORED AS AliOrc]-- Specify the storage format of the table. You can specify AliORC only for newly created int ernal tables. [TBLPROPERTIES("compressionstrategy"="normal/high/extreme",-- Specify the compression policy for data storage.
               "transactional"="true")] -- Specify a transactional table. You can then execute UPDATE or DELETE
statements on the table. [LIFECYCLE days]; CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE existing_table_name];
```

Parameters:
**table_name** and **col_name**: the table name and column name. The names are not case-sensitive. The names
cannot contain special characters. A table or column name can contain only letters, digits, and underscores (_) and can be up to 128 bytes in length. We recommend that you start the table or column name with a letter. A table can contain a maximum of 1,200 columns.
**data_type**: the type of data. Valid values: BIGINT, DOUBLE, BOOLEAN, DATETIME, DECIMAL, STRING, ARRAY<T>,
and MAP<T1,T2>. If you want to use new data types, such as TINYINT, SMALLINT, INT, FLOAT, VARCHAR, TIMESTAMP, and BINARY, you must enable these data types. To enable new data types at the session level, add set odps.sql.type.system.odps2=true; before the SQL statement. Then, commit them for execution. To enable new data types at the project level, run the following command as the project owner:

```
setproject odps.sql.type.system.odps2=true;
```

**DEFAULT value**: the default value of the column. If you do not specify the value of the column in an INSERT
operation, the default value is used for the column.
**COMMENT table_comment**: the comment of the table. The comment must be a valid string that can be up to 1,024
bytes in length.
**PARTITIONED BY (col_name data_type [COMMENT col_comment], …)** : the partition field of the table. The
following data types are supported: TINYINT, SMALLINT, INT, BIGINT, VARCHAR, and STRING. The value of the partition field cannot contain double-byte characters. It must start with a letter, followed by letters, digits, or special characters. The value can be a maximum of 128 bytes in length. The value can contain the following special characters: spaces, colons (:), underscores (_), dollar signs ($), number signs (#), periods (.), exclamation points (!), and at signs (@). Other characters, such as \t, \n, and /, are considered undefined characters. After you use partition fields to partition a table, a full table scan is not triggered when you add partitions, update partition data, or read partition data. This makes data processing more efficient. A table can contain a maximum of 60,000 partitions at six or lower levels.

**CLUSTERED BY | RANGE CLUSTERED BY (col_name [, col_name, …]) [SORTED BY (col_name [ASC | DESC]**

**[, col_name [ASC | DESC] …])] INTO number_of_buckets BUCKETS**: specifies the shuffle and sort attributes
when you create a clustered table. Clustered tables are classified into hash-clustered tables and range-clustered tables. Hash-clustered tables
**CLUSTERED BY**: the hash key. MaxCompute performs a hash operation on specified columns and distributes
data to each bucket based on the hash values. We recommend that you specify a column that has large value ranges and a small number of duplicate key-value pairs in **CLUSTERED BY**. This prevents data skew and hot spots and makes concurrent execution more efficient. To optimize JOIN operations, we recommend that you select commonly used join or aggregation keys. The join and aggregation keys are similar to the primary keys in conventional databases.
**SORTED BY**: specifies how the data in a bucket is sorted. To achieve better performance, we recommend that
you set **SORTED BY** and **CLUSTERED BY** to the same value. If you specify the **SORTED BY** clause, MaxCompute automatically generates indexes and uses these indexes to speed up your queries.
**INTO number_of_buckets BUCKETS**: the number of hash buckets. This parameter is required, and the value
of this parameter varies based on the amount of data. By default, MaxCompute supports a maximum of 1,111 reducers. Therefore, MaxCompute supports a maximum of 1,111 hash buckets. You can run the `set` odps.sql.reducer.instances=xxx; command to increase the number of hash buckets. The maximum number of hash buckets that is supported is 4,000. If the value exceeds 4000, computing performance deteriorates. To ensure optimal performance, we recommend that you take note of the following rules when you specify the number of hash buckets: Keep the size of each bucket around 500 MB. For example, if you want to add 1,000 buckets to a partition whose size is 500 GB, you must make sure that the average size of each bucket is 500 MB. If a table contains a large amount of data, you can increase the size of each bucket from 500 MB to a size in the range of 2 GB to 3 GB. You can also execute the set odps.sql.reducer.instances=xxx; statement to set the maximum number of hash buckets to a value greater than 1111. To optimize JOIN operations, we recommend that you do not specify the shuffle and sort attributes. The number of hash buckets of a table must be a multiple of the number of hash buckets of the other table. For example, one table has 256 hash buckets and the other table has 512 hash buckets. We recommend that you set the number of hash buckets to 2n, such as 512, 1,024, 2,048, or 4,096. This way, MaxCompute can automatically split and merge hash buckets. To make the execution more efficient, we recommend that you do not specify the shuffle and sort attributes. Range-clustered tables
**RANGE CLUSTERED BY**: the column for range clustering. MaxCompute performs the bucket operation on the
specified columns and distributes data to each bucket based on the bucket ID.
**SORTED BY**: specifies how the data in a bucket is sorted. You can use this clause in the same way you use it for
a hash-clustered table.
**INTO number_of_buckets BUCKETS**: the number of hash buckets. Compared with hash-clustered tables,
range-clustered tables have no limits on the number of buckets if the data is reasonably distributed. If you do not specify the number of buckets for a range-clustered table, MaxCompute automatically determines the optimal number of buckets based on your data volume. If join and aggregate operations are performed on range-clustered tables and the join or group key is the range clustering key or the prefix of the range clustering key, you can control flags to remove data shuffling. This makes the execution more efficient. You can set `odps.optimizer.enable.range.partial.repartitioning` to true or false to control shuffling. By default, this parameter is set to false. The default value indicates that shuffling is disabled.
**STORED AS**: the storage format of the table. The default value is CFile2. AliORC in C++ is now available. It is
developed by the MaxCompute storage team. AliORC is fully compatible with the open source Optimized Row Columnar (ORC). Compared with CFile2, AliORC frees up more than 10% of storage and improves read performance by more than 20%.
**LIFECYCLE**: the lifecycle of the table, in days. If you execute the **CREATE TABLE LIKE** statement to create a table
based on the schema of the source table, the lifecycle settings of the source table are not replicated.
**CREATE TABLE [IF NOT EXISTS] table_name [AS select_statement | LIKE existing_table_name]** :

| CREATE TABLE…AS select statement… _ |   | statement to create a ta |
|---|---|---|
| the table. However, the | CREATE TABLE…AS select statement… _ |   |

partition attributes of the source table. Partition key columns in the source table become standard columns in the destination table. If you execute the CREATE TABLE…LIKE existing_table_name statement to create a table, the destination table has the same schema as the source table. However, the statement does not replicate data or lifecycle settings from the source table to the destination table. Clauses related to external tables:
**STORED BY StorageHandler**: the storage handler that is specified based on the format of data in the external
table.
**WITH SERDEPROPERTIES (Options)**: the parameters for authorization, compression, and character parsing in
the external table.
**LOCATION OSSLocation**: the Object Storage Service (OSS) directory where the external table is saved.
**TBLPROPERTIE("compressionstrategy"="xxx")**: the attribute of the transactional table. You can specify the
lifecycle and comment attributes in this clause. **compressionstrategy** specifies the compression policy for data storage. The valid values are normal, high, and extreme. The **compressionstrategy** parameter must be in lowercase. However, the value of this parameter is not case-sensitive. This attribute applies only to the internal tables of MaxCompute. The default compression policy is normal for non-archived data and high for archived data. Definitions of the valid values: normal: indicates zstd level 1. high: indicates zstd level 4. extreme: indicates zstd level 9. You can also specify the compression policy for a project. The project owner must use
**odps.storage.compression.strategy** to specify the compression policy in the common attributes for project
management. After this attribute is specified, the configuration applies to all generated non-archived data and does not affect the archive policy.
**TBLPROPERTIES("transactional"="true")**: indicates that the table that you want to create is a transactional
table. You can execute the UPDATE or DELETE statement to update or delete data by row. If you do not specify **IF NOT EXISTS** in a table creation statement and another table with the same name exists, an error is returned. If you specify **IF NOT EXISTS** in a table creation statement, a success message is returned regardless of whether a table with the same name exists. The message is returned even if the schema of the existing table is different from that of the table to create. In addition, the metadata of the existing table remains unchanged.

**Example for creating a partitioned table**

The following example shows how to create a table named sale_detail to store sales records. The table has two partition key columns: **sale_date** and **region**. Syntax:

```
CREATE TABLE IF NOT EXISTS sale_detail
```

`(`

```
shop_name STRING, customer_id STRING, total_price DOUBLE
```

`)`

```
PARTITIONED BY (sale_date STRING,region STRING); -- Create a partitioned table named sale_detail.
```

**Example of CREATE TABLE...AS...**

You can execute the `CREATE TABLE...AS select_statement...` statement to create a table and replicate data from the source table to the table. Example:

```
CREATE TABLE sale_detail_ctas1 AS SELECT * FROM sale_detail;
```

If the sale_detail table contains data, all data in the sale_detail table is replicated to the sale_detail_ctas1 table after you execute the preceding statement. The sale_detail table is a partitioned table. When you execute the `CREATE TABLE...AS select_statement...` statement to create the sale_detail_ctas1 table, partition attributes of the sale_detail table are not replicated to the sale_detail_ctas1 table, and partition key columns in the sale_detail table are considered standard columns in the sale_detail_ctas1 table. sale_detail_ctas1 is a non-partitioned table that has five columns. If the SELECT clause in the `CREATE TABLE...AS select_statement...` statement uses constants as column values, we recommend that you specify the names of columns. Example:

```
CREATE TABLE sale_detail_ctas2
```

`AS`

```
SELECT shop_name, customer_id, total_price, '2013' AS sale_date, 'China' AS region FROM sale_detail;
```

Example without column aliases specified:

```
CREATE TABLE sale_detail_ctas3
```

`AS`

```
SELECT shop_name, customer_id, total_price, '2013', 'China' FROM sale_detail;
```

**Example of CREATE TABLE...LIKE...**

If you want the source and destination tables to have the same schema, you can execute the `CREATE` `TABLE...LIKE...` statement. Example:

```
CREATE TABLE sale_detail_like LIKE sale_detail;
```

The schema of sale_detail_like is exactly the same as that of sale_detail. The two tables have the same attributes, such as column names, column comments, and table comments, aside from the lifecycle. However, data in the sale_detail table is not replicated to the sale_detail_like table.

**Create clustered tables**

The following example shows how to create a hash-clustered table.

```
CREATE TABLE T1 (a STRING, b STRING, c BIGINT) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS; -- Create a ha sh-clustered non-partitioned table. CREATE TABLE T1 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY (c) SORTED by (c) INTO 1 024 BUCKETS; -- Create a hash-clustered partitioned table.
```

The following example shows how to create a range-clustered table.

```
CREATE TABLE T2 (a STRING, b STRING, c BIGINT) RANGE CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS; -- Creat e a range-clustered non-partitioned table. CREATE TABLE T2 (a STRING, b STRING, c BIGINT) PARTITIONED BY (dt STRING) CLUSTERED BY (c) SORTED by (c) ; -- C reate a range-clustered partitioned table. The number of buckets can be empty.
```

**Create transactional tables**

```
-- Create a transactional table. create table txn_table(id bigint) tblproperties("transactional"="true"); -- Create a partitioned transactional table. create table if not exists txn_table_pt(id bigint) partitioned by(ds string) tblproperties ("transactional"="true");
```

**Query information about a table**

MaxCompute allows you to execute the DESC statement to query table information.

```
DESC <table_name>; -- Query table information. DESC EXTENDED <table_name>; -- Query information about an external table. -- You can also check whether the table is a transactional table. If you want to check whether the table is a t ransactional table, you must upgrade the version of the MaxCompute client to V0.35.0.
```

**Query the statements that are used to create tables**

MaxCompute allows you to execute the SHOW CREATE TABLE statement to query the statements that are used to create tables.

```
SHOW CREATE TABLE <table_name>;
```

You can use this statement to generate SQL DDL statements that are used to create tables. These DDL statements can be used to rebuild the table schema.

##### 3.4.1.2 Delete a table

This topic describes how to use a DDL statement to delete a table.

```
DROP TABLE [IF EXISTS] table_name;
```

If you do not specify **IF EXISTS** and the table does not exist, an error is returned. If this option is specified, a success message is returned regardless of whether the table exists.

```
CREATE TABLE sale_detail_drop LIKE sale_detail; DROP TABLE sale_detail_drop; -- If the table exists, a success message is returned. If the table does not exist, an error is returned. DROP TABLE IF EXISTS sale_detail_drop2; -- A success message is returned regardless of whether the sale_detail_drop2 table exists.
```

##### 3.4.1.3 Rename a table

This topic describes how to use a DDL statement to rename a table.

```
ALTER TABLE table_name RENAME TO new_table_name;
```

The **RENAME** operation changes only the name of a table. Data in the table remains unchanged. If a table that has the same name as the table specified by new_table_name exists, an error is returned. If the table specified by **table_name** does not exist, an error is returned.

```
CREATE TABLE sale_detail_rename1 LIKE sale_detail; ALTER TABLE sale_detail_rename1 RENAME TO sale_detail_rename2;
```

##### 3.4.1.4 Change the owner of a table

This topic describes how to use a DDL statement to change the owner of a table. MaxCompute SQL allows you to execute the `CHANGEOWNER` statement to change the owner of a table.

```
ALTER TABLE table_name CHANGEOWNER TO 'ALIYUN$xxx@aliyun.com';
```

##### 3.4.1.5 Modify the comment of a table

This topic describes how to use a DDL statement to modify the comment of a table.

```
ALTER TABLE table_name SET COMMENT 'tbl comment';
```

The table specified by **table_name** must exist. The value of **comment** can be up to 1,024 bytes.

```
ALTER TABLE sale_detail SET COMMENT 'new coments for table sale_detail';
```

You can execute the DESC statement in MaxCompute to view the comment of the table after modification.

##### 3.4.1.6 Modify the lifecycle settings of a table

MaxCompute provides the lifecycle management feature to facilitate storage release and simplify data reclamation. This topic describes how to use a DDL statement to modify the lifecycle settings of a table.

```
ALTER TABLE table_name SET lifecycle days;
```

**days**: the lifecycle duration, which must be a positive integer in days.
**table_name**: the name of the table whose lifecycle settings you want to modify.
You can specify the lifecycle when you create a table. The lifecycle can be specified only for a table rather than a partition. After a lifecycle is specified for a partitioned table, the lifecycle applies to the partitions of the table. If data in a table is modified, the value of **LastDataModifiedTime** is updated. Therefore, MaxCompute determines whether to reclaim this table based on the value of **LastDataModifiedTime** and the lifecycle settings. For a non-partitioned table, if the data remains unchanged for the duration specified by **days** after data is last modified, MaxCompute automatically executes a statement such as DROP TABLE to reclaim the table. For a partitioned table, MaxCompute determines whether to reclaim a partition based on the value of
**LastDataModifiedTime** for the partition. Unlike non-partitioned tables, a partitioned table is not deleted
even if all of the partitions are reclaimed. You can only modify the lifecycle settings instead of disabling the lifecycle for non-partitioned tables. You can disable the lifecycle for a specific partition in a partitioned table.

```
create table test_lifecycle(key string) lifecycle 100; -- Create a table named test_lifecycle with a lifecycle of 100 days. alter table test_lifecycle set lifecycle 50; -- Change the lifecycle of the test_lifecycle table to 50 days.
```

##### 3.4.1.7 Disable or enable the lifecycle feature

In some cases, if you do not want some partitions to be automatically reclaimed based on the lifecycle feature, you can disable the lifecycle feature for these partitions. This topic describes how to use a DDL statement to disable or enable the lifecycle feature.

```
ALTER TABLE table_name partition[partition_spec] ENABLE|DISABLE LIFECYCLE;
```

**DISABLE LIFECYCLE**: disables the lifecycle feature for a table or partition.
It prevents the reclamation of a table and its partitions based on the lifecycle feature. This parameter has a higher priority than partition_spec enable lifecycle. If you use **table disable lifecycle**,
**partition_spec enable lifecycle** is invalid.
After the lifecycle feature of a table is disabled, the table lifecycle settings and the ENABLE and DISABLE tags of partitions in the table are retained. After the lifecycle feature of a table is disabled, you can still modify the lifecycle settings of the table and its partitions.
**ENABLE LIFECYCLE**: enables the lifecycle feature for a table or partition.
A table and its partitions can be reclaimed based on the lifecycle feature again. The lifecycle settings of the current table and its partitions are used by default. Before you enable the lifecycle feature for a table, you can modify the lifecycle settings of the table and its partitions. This prevents data from being mistakenly reclaimed due to the use of previous settings.

```
ALTER TABLE trans DISABLE LIFECYCLE; -- Disable the lifecycle feature for the trans table. ALTER TABLE trans PARTITION(dt='20141111') DISABLE LIFECYCLE; -- Disable the lifecycle feature for the dt='20141111' partition in the trans table. ALTER TABLE trans ENABLE LIFECYCLE; -- Enable the lifecycle feature for the trans table. ALTER TABLE trans PARTITION(dt='20141111') ENABLE LIFECYCLE; -- Enable the lifecycle feature for the dt='20141111' partition in the trans table.
```

##### 3.4.1.8 Modify the value of LastDataModifiedTime for a table

MaxCompute SQL allows you to perform the TOUCH operation to modify the value of **LastDataModifiedTime** for a table. This operation changes the value of **LastDataModifiedTime** for a table to the current time. This topic describes how to use a DDL statement to modify the value of LastDataModifiedTime for a table.

```
ALTER TABLE table_name TOUCH;
```

If the table specified by **table_name** does not exist, an error is returned. This operation modifies the value of **LastDataModifiedTime** for a table. In this case, MaxCompute considers a change to the table data and recalculates the lifecycle.

##### 3.4.1.9 Modify the clustering attributes of a table

This topic describes how to use a DDL statement to modify the clustering attributes of a table. MaxCompute allows you to add or remove the clustering attributes of a partitioned table by using the `ALTER TABLE` statement. The `ALTER TABLE` statement can modify only the clustering attributes of a partitioned table. The clustering attributes of a non-partitioned table cannot be modified after these attributes are added. The `ALTER TABLE` statement is applicable to the tables that already exist. After new clustering attributes are added, new partitions are stored based on the modified clustering attributes. The `ALTER TABLE` statement affects only the new partitions of partitioned tables, including the partitions generated by using the INSERT OVERWRITE statement. New partitions are stored based on the new clustering attributes, while the clustering attributes and storage of existing partitions remain unchanged. After you specify the clustering attributes for a table, you can remove the clustering attributes and add clustering attributes for the table again. You can specify different clustering columns, sort columns, and numbers of buckets for new partitions. The `ALTER TABLE` statement takes effect only on the new partitions of a table. Therefore, you cannot specify a partition in this statement.

**Add hash clustering attributes to a table**

```
ALTER TABLE table_name [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_name [ASC | DESC] ...])] IN TO number_of_buckets BUCKETS]
```

**Remove hash clustering attributes from a table**

```
ALTER TABLE table_name NOT CLUSTERED;
```

**Add range clustering attributes to a table**

If you do not specify the number of buckets, MaxCompute automatically determines the optimal number based on the data volume.

```
ALTER TABLE table_name [RANGE CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_name [ASC | DESC] ... ])] INTO number_of_buckets BUCKETS]
```

**Remove range clustering attributes from a table or partition**

```
ALTER TABLE table_name NOT CLUSTERED; ALTER TABLE table_name partition_spec NOT CLUSTERED;
```

##### 3.4.1.10 Delete data from a non-partitioned table

This topic describes how to use a DDL statement to delete data from a non-partitioned table.

```
TRUNCATE TABLE table_name;
```

This statement is used to delete data from a specific non-partitioned table. To delete data from a partitioned table, execute the `ALTER TABLE table_name DROP PARTITION(partition_spec)` statement.

##### 3.4.1.11 Archive table data

This topic describes how to use a DDL statement to archive the data of a table. If a project does not have enough space and data needs to be compressed or deleted, you can use table archiving of MaxCompute to compress data by about 50%. Table archiving uses a compression algorithm with a high compression ratio. It saves data as redundant array of independent disks (RAID) files. Data is no longer simply stored in three copies. Instead, six copies and three check blocks are maintained to increase the compression ratio from 1:3 to 1:1.5. Table archiving allows data to consume only half of the physical space. However, this feature comes at a price. If a data block or machine is faulty, it requires a long time to restore the data block, and read performance deteriorates. Therefore, this feature is suitable for the compression of cold data. For example, you can use this feature to store a large number of logs that are less used as RAID files for a long time.

```
ALTER TABLE [table_name] <PARTITION(partition_name='partition_value')> ARCHIVE;
```

If the table specified by **table_name** does not exist, an error is returned. If the partition specified by **partition_name** does not exist, an error is returned.

```
alter table my_log partition(ds='20170101') archive;
```

Output:

```
Summary: table name: test0128 /pt=a instance count: 1 run time: 21 before merge, file count: 1 file size: 456 file physical size: 1368 after merge, file count: 1 file size: 512 file physical size: 768
```

|   | Note The output shows the changes in the logical size and physical size after the data is archived. In the archiving process, multiple small files are automatically merged. After the data is archived, you can execute the DESC EXTENDED statement to check whether the data in the partition has been archived and view the usage of physical space: desc extended my log partition(ds='20170101'); _ -- The following result is returned: +------------------------------------------------------------------------------------+ PartitionSize: 512 \| +------------------------------------------------------------------------------------+ CreateTime: 2017-01-28 07:05:20 \| LastDDLTime: 2017-01-28 07:05:20 \| LastModifiedTime: 2017-01-28 07:05:21 \| +------------------------------------------------------------------------------------+ |   |   |
|---|---|---|---|
|   |   | DESC |   |
|   | EXTENDED |   |   |

##### 3.4.1.12 Forcibly delete data from a table or partition

This topic describes how to use a DDL statement to forcibly delete data from a table or partition. If you want to forcibly and irrecoverably delete data from a table or partition to immediately release storage, you can execute a DROP statement with the PURGE option.

```
DROP TABLE tblname PURGE; ALTER TABLE tblname DROP PARTITION(part_spec) PURGE; drop table my_log purge; alter table my_log drop partition (ds='20170618') purge;
```

#### 3.4.2 View-based operation

##### 3.4.2.1 Create a view

This topic describes how to use a DDL statement to create a view.

```
CREATE [OR REPLACE] VIEW [IF NOT EXISTS] view_name [(col_name [COMMENT col_comment], ...)] [COMMENT view_comment] [AS select_statement];
```

To create a view, you must have read permissions on the table referenced by the view. A view can contain only one valid SELECT statement. A view can reference other views but cannot reference itself. Circular references are not supported. You cannot write data to a view. For example, the `INSERT INTO` and `INSERT OVERWRITE` statements do not work on views. If the table referenced by a view changes, you may no longer be able to access the view. For example, a view becomes inaccessible after the table it references is deleted. You must maintain the mappings between referenced tables and views. If the `CREATE VIEW` statement is executed without the **IF NOT EXISTS** option and the view already exists, an exception is returned. In this case, you can execute `CREATE VIEW or REPLACE VIEW` to recreate the view. The permissions on the view remain unchanged after the view is recreated.

```
create view if not exists sale_detail_view (store_name, customer_id, price, sale_date, region) comment 'a view for table sale_detail' as select * from sale_detail; -- Create a view named sale_detail_view.
```

##### 3.4.2.2 Delete a view

This topic describes how to use a DDL statement to delete a view.

```
DROP VIEW [IF EXISTS] view_name;
```

If the partition does not exist and **IF EXISTS** is not specified, an error is returned.

```
DROP VIEW IF EXISTS sale_detail_view;
```

##### 3.4.2.3 Rename a view

This topic describes how to use a DDL statement to rename a view.

```
ALTER VIEW view_name RENAME TO new_view_name;
```

If a view with the same name already exists, an error is returned.

```
alter view sale_detail_view rename to market;
```

#### 3.4.3 Materialized view operations

A materialized view is a database object that stores the pre-calculation results of time-consuming queries, such as JOIN and AGGREGATE. You can directly reuse the pre-calculation results when you want to perform the same queries. This accelerates the speed of queries. A view is a stored query accessible as a virtual table. Each time you query a view, the query statement is converted into the SQL statement that is used to define the view. A materialized view is a special physical table that occupies storage resources to store real data. Materialized views are suitable for the following queries: Queries that are in a fixed mode and are frequently executed Queries that involve time-consuming operations, such as JOIN or AGGREGATE Queries that involve only a small portion of data in a table The following table compares traditional queries and queries based on materialized views.

| Item | Traditional query | Query based on a materialized view |
|---|---|---|

| Query statements | SQL statements are used to query data. SELECT empid, deptname FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2018-01- _ 01'; | Data is queried based on the materialized view that you created. Statements that are used to create a materialized view: CREATE MATERIALIZED VIEW mv AS SELECT empid, deptname, hire date _ FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2016-01-01'; _ Statements that are used to query data based on the materialized view that you created: SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ If the query rewrite feature is enabled for the materialized view, data is directly obtained from the query result that is contained in the materialized view when you execute the first SQL statement in the following code: SELECT empid, deptname FROM emps JOIN depts ON emps.deptno=depts.deptno WHERE hire date >= '2018-01-01'; _ -- The preceding statement is equivalent to the following statement: SELECT empid, deptname FROM mv WHERE hire date >= '2018-01-01'; _ |
|---|---|---|
| Query characteristics | Queries involve table reading, JOIN, and filter (WHERE clause) operations. If the source table contains a large amount of data, the query speed is slow. The query operation is complex, and the query efficiency is low. | Queries involve table reading and filter operations. JOIN operations are not involved. MaxCompute automatically matches the optimal materialized view and reads data from the optimal materialized view. This greatly improves query efficiency. |

| Operation | Description | Authorized user |
|---|---|---|
| Create a materialized view that supports clustering or partitioning | Creates a materialized view based on a query statement. | Users who have the CreateTable permission on a project |
| Update a materialized view | Updates an existing materialized view. | Users who have the Alter permission on tables |
| Change the lifecycle of an existing materialized view | Changes the lifecycle of an existing materialized view. | Users who have the Alter permission on tables |
| Enable or disable the lifecycle feature for an existing materialized view | Enables or disables the lifecycle feature for an existing materialized view. | Users who have the Alter permission on tables |
| Query information about a materialized view | Queries the basic information about a materialized view. | Users who have the Describe permission on the metadata of a table |

| Query the status of a materialized view | Queries the status of a materialized view. | Users who have the Describe permission on the metadata of a table |
|---|---|---|
| List all materialized views within a project | Lists all materialized views in a project or the materialized views that meet specific rules in a project. | Users who have the List permission on objects in a project |
| Drop an existing materialized view | Drops an existing materialized view. | Users who have the Drop permission on tables |
| Drop partitions from an existing materialized view | Drops partitions from an existing materialized view. | Users who have the Drop permission on tables |
| Perform a penetration query on a materialized view | Queries data from the source partitioned table if the partition data that you want to query is not contained in the materialized view. | Users who have the Write and CreateTable permissions on a project |

Window functions, User-defined table-valued functions (UDTFs), and non-deterministic functions, such as user-defined scalar functions (UDFs) and user-defined aggregate functions (UDAFs), are not supported.

|   | Note If you must use non-deterministic functions, run the set |   |   |
|---|---|---|---|
|   |   | set |   |
|   | odps.sql.materialized.view.support.nondeterministic.function=true; |   |   |

**Create a materialized view that supports clustering or partitioning**

You can create a materialized view that supports clustering or partitioning based on the data for materialized view scenarios. The name of the materialized view that you want to create cannot be the same as the name of an existing table, view, or materialized view in the current project. You can run the SHOW TABLES; command to view the names of all tables and materialized views in a project. You cannot create a materialized view based on an existing materialized view. You cannot create a materialized view based on an external table. If the query statement based on which you create a materialized view fails to be executed, you cannot create the materialized view. Partition key columns in a materialized view must be derived from a source table. The sequence and number of the columns in the materialized view must be the same as the sequence and number of the columns in the source table. Column names can be different. You must specify comments for all columns, including partition key columns. If you specify comments only for some columns, an error is returned. You can specify both the partitioning and clustering attributes for a materialized view. In this case, the data in each partition has the specified clustering attribute. If the query statement based on which you create a materialized view contains operators that are not supported by the materialized view, an error is returned. By default, MaxCompute does not allow you to create materialized views by using non-deterministic functions, such as UDFs or UDAFs. If you must use non-deterministic functions, run the `set` odps.sql.materialized.view.support.nondeterministic.function=true; command at the session level. If the source table of a materialized view contains an empty partition, you can refresh the materialized view to generate an empty partition in the materialized view. Command syntax

```
CREATE MATERIALIZED VIEW [IF NOT EXISTS][project_name.]<mv_name> [LIFECYCLE <days>] -- The lifecycle of the materialized view. [BUILD DEFERRED] -- Specifies that only the schema is created and no data is updated when you create the m aterialized view. [(<col_name> [COMMENT <col_comment>],...)] -- The column comments. [DISABLE REWRITE] -- Specifies whether to disable the query rewrite operation that is performed based on the materialized view. [COMMENT 'table comment'] -- The materialized view comments. [PARTITIONED BY (<col_name> [, <col_name>, ...]) -- The partitions in the materialized view. This parameter is required when you create a partitioned materialized view. [CLUSTERED BY|RANGE CLUSTERED BY (<col_name> [, <col_name>, ...]) [SORTED BY (<col_name> [ASC | DESC] [, <col_name> [ASC | DESC] ...])]
    INTO <number_of_buckets> BUCKETS]    -- The shuffle and sort attributes of the materialized view. This pa
rameter is required when you create a clustered materialized view. [REFRESH EVERY <num> MINUTES/HOURS/DAYS] [TBLPROPERTIES("compressionstrategy"="normal/high/extreme", -- The compression policy for data storage of the materialized view.
                "enable_auto_substitute"="true",    -- Specifies whether to query data from the source partiti
oned table if the partition data that you want to query is not contained in the materialized view.
                "enable_auto_refresh"="true",    -- Specifies whether to enable the scheduled update feature.
                "refresh_interval_minutes"="120",    -- The update interval.
                "only_refresh_max_pt"="true"    -- Specifies whether to automatically update the latest partit
ion data in the source table to the materialized view.
```

`)]`

```
AS <select_statement>;
```

Parameters and descriptions

| Parameter | Requir ed | Description |
|---|---|---|
| IF NOT EXISTS | No | If you do not specify IF NOT EXISTS and the materialized view already exists, an error is returned. |
| project name _ | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to create. |
| days | No | The lifecycle of the materialized view that you want to create. Unit: days. Valid values: 1 to 37231. |
| BUILD DEFERRED | No | If this keyword is added, only the schema is created and the data is not updated when you create the materialized view. |
| col name _ | No | The name of a column in the materialized view that you want to create. |
| col comment _ | No | The comment on a column in the materialized view that you want to create. |
| DISABLE REWRITE | No | Specifies whether to disable the query rewrite operation that is performed based on this materialized view. If you do not configure this parameter, the query rewrite operation based on this materialized view is allowed. In this case, you can execute the ALTER MATERIALIZED VIEW [project name.]<mv name> DISABLE REWRITE; statement to _ _ disable the query rewrite operation that is performed based on the materialized view. You can also execute the ALTER MATERIALIZED VIEW [project name.]<mv name> ENABLE _ _ REWRITE; statement to enable the query rewrite operation that is performed based on the materialized view. |
|   |   | REWRITE; |
| PARTITIONED BY | No | The partition key columns in the materialized view that you want to create. If you want to create a partitioned materialized view, you must configure this parameter. |

|   | MATERIALIZED VIEW [project name.]<mv name> DISABLE REWRITE; _ _ |
|---|---|

| ALTER MATERIALIZED VIEW [project name.]<mv name> ENABLE _ _ |   |
|---|---|

| CLUSTERED BY\|RANGE CLUSTERED BY | No | The shuffle attribute of the materialized view that you want to create. If you want to create a clustered materialized view, you must specify the clustered by or range clustered by parameter. |
|---|---|---|
| SORTED BY | No | The sort attribute of the materialized view that you want to create. If you want to create a clustered materialized view, you must configure this parameter. |
| REFRESH EVERY | No | The scheduled update interval for materialized views. Supported units: minutes, hours, days, and days. |
| number of buckets _ _ | No | The number of buckets in the materialized view that you want to create. If you want to create a clustered materialized view, you must configure this parameter. |
| TBLPROPERTIES | No | compressionstrategy specifies the compression policy for data storage of the materialized view that you want to create. Valid values: normal, high, and extreme. enable auto substitute specifies whether to automatically query data from the source _ _ table if the materialized view does not contain the partition from which you want to query data. enable auto refresh: optional. Set this parameter to true if you want the system _ _ to automatically update data. refresh interval minutes: conditionally optional. If enable auto refresh is set to _ _ _ _ true , you need to configure this parameter. Unit: minutes. only refresh max pt: optional. This parameter is valid for partitioned materialized _ _ _ views. If this parameter is set to true , the latest partition data in the source table is updated to the materialized view. |
| select statement _ | Yes | The SELECT statement. For more information about the syntax of the SELECT statement, see SELECT syntax. |

Example 1: Create a materialized view. a. Create tables named `mf_t` and `mf_t1` and insert data into the tables.

```
CREATE TABLE IF NOT EXISTS mf_t(
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t ADD PARTITION (ds='1'); INSERT INTO mf_t PARTITION (ds='1') VALUES (1,10,'kyle'),(2,20,'xia'); SELECT * FROM mf_t WHERE ds ='1'; -- The following result is returned: +------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 2          | 20         | xia        | 1          |
+------------+------------+------------+------------+ CREATE TABLE IF NOT EXISTS mf_t1(
     id     bigint,
     value   bigint,
     name   string)
PARTITIONED BY (ds STRING); ALTER TABLE mf_t1 ADD PARTITION (ds='1'); INSERT INTO mf_t1 PARTITION (ds='1') VALUES (1,10,'kyle'),(3,20,'john'); SELECT * FROM mf_t1 WHERE ds ='1'; -- The following result is returned: +------------+------------+------------+------------+
| id         | value      | name       | ds         |
+------------+------------+------------+------------+
| 1          | 10         | kyle       | 1          |
| 3          | 20         | john       | 1          |
+------------+------------+------------+------------+
```

b. Create a materialized view. Sample 1: Create a materialized view that contains a partition key column named ds.

```
CREATE MATERIALIZED VIEW mf_mv LIFECYCLE 7
```

`(`

```
  key comment 'unique id',
  value comment 'input value',
  ds comment 'partitiion'
```

`)`

```
PARTITIONED BY (ds) AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
     FROM mf_t AS t1 JOIN mf_t1 AS t2
       ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
-- Query data from the created materialized view. SELECT * FROM mf_mv WHERE ds =1; +------------+------------+------------+
| key        | value      | ds         |
+------------+------------+------------+
| 1          | 10         | 1          |
+------------+------------+------------+
```

Sample 2: Create a non-partitioned materialized view that is clustered.

```
CREATE MATERIALIZED VIEW mf_mv2 LIFECYCLE 7 CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

Sample 3: Create a partitioned materialized view that is clustered.

```
CREATE MATERIALIZED VIEW mf_mv3 LIFECYCLE 7 PARTITIONED BY (ds) CLUSTERED BY (key) SORTED BY (value) INTO 1024 buckets AS SELECT t1.id AS key, t1.value AS value, t1.ds AS ds
      FROM mf_t AS t1 JOIN mf_t1 AS t2
        ON t1.id = t2.id AND t1.ds=t2.ds AND t1.ds='1';
```

Example 2: Update a materialized view whose source table contains an empty partition. An empty partition is generated in the materialized view.

```
CREATE TABLE mf_blank_pts(id bigint ,name string) PARTITIONED BY (ds bigint); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 1); ALTER TABLE mf_blank_pts ADD PARTITION (ds = 2); INSERT INTO TABLE mf_blank_pts PARTITION(ds=1) VALUES (1,"aba"),(2,"cbd"); CREATE MATERIALIZED VIEW IF NOT EXISTS mf_mv_blank_pts PARTITIONED BY (ds) AS SELECT id,name,ds FROM mf_blank_pts; ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>0); SHOW PARTITIONS mf_mv_blank_pts; -- The partition ds=2 in the source table does not contain any data. After you execute an ALTER statement t hat contains the expression ds>0, an empty partition is generated in the materialized view. ds=1 ds=2 SELECT * FROM mf_mv_blank_pts WHERE ds>0; -- The returned result shows that only the ds=1 partition has data. +------------+------------+------------+
| id         | name       | ds         |
+------------+------------+------------+
| 1          | aba        | 1          |
| 2          | cbd        | 1          |
+------------+------------+------------+
```

**Update a materialized view**

If you perform operations, such as insert, overwrite, update, and delete operations on the table or partition that corresponds to a materialized view, the materialized view becomes invalid and cannot be used for query rewrite operations. You can check the status of a materialized view. If the materialized view is invalid, you must update the materialized view. Data in a materialized view or a partition in a materialized view is updated only when data in the source table or a partition in the source table changes. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name>
      REBUILD [PARTITION (<ds>=max_pt(<table_name>),<expression1>...)];
```

Parameters and descriptions

| Parameter | Requir ed | Description |
|---|---|---|
| project name _ | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to update. |
| ds | No | The name of the partition field in the materialized view. |
| max pt _ | No | The maximum partition value of the table or materialized view that is specified by table name. _ |
| expression | No | The expression that is used to specify the partitions that you want to update. If you want to update a partitioned materialized view, you must configure this parameter. |

Example 1: Update a non-partitioned materialized view.

```
-- Create a non-partitioned table. CREATE TABLE count_test(a BIGINT, b BIGINT); -- Create a non-partitioned materialized view. CREATE MATERIALIZED VIEW count_mv LIFECYCLE 7 AS SELECT COUNT(*) FROM count_test; -- Update the non-partitioned materialized view. ALTER MATERIALIZED VIEW count_mv rebuild;
```

Example 2: Update a partition of a partitioned materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds='1');
```

Example 3: Update the partitions of a partitioned materialized view. The partitions meet the specified conditions.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts REBUILD PARTITION (ds>='1', ds<='2');
```

Example 4: Update the latest partition data to a partitioned materialized view.

```
-- Create a partitioned table. CREATE TABLE IF NOT EXISTS sale_detail_jt (shop_name STRING , customer_id STRING , total_price DOUBLE ) PARTITIONED BY (sale_date STRING ,region STRING ); ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='china'); INSERT INTO sale_detail_jt PARTITION (sale_date='2013',region='china') VALUES
    ('s1','c1',100.1),
    ('s2','c2',100.2),
    ('s3','c3',100.3);
ALTER TABLE sale_detail_jt ADD PARTITION (sale_date='2013',region='en'); INSERTINTO saledetailjtPARTITION(saledate='2013',region='en')VALUES
```

```
INSERT INTO sale_detail_jt PARTITION (sale_date 2013,region en) VALUES
    ('t1','c5',200.0),
    ('t2','c6',300.0);
-- View partition data. SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='china'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| s1        | c1          | 100.1       | 2013      | china  |
| s2        | c2          | 100.2       | 2013      | china  |
| s5        | c2          | 100.2       | 2013      | china  |
+-----------+-------------+-------------+-----------+--------+ -- View partition data. SELECT * FROM sale_detail_jt WHERE sale_date='2013' AND region='en'; +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+
| t1        | c5          | 200.0       | 2013      | en     |
| t2        | c6          | 300.0       | 2013      | en     |
+-----------+-------------+-------------+-----------+--------+ -- Create a materialized view. CREATE MATERIALIZED VIEW mv_deferred BUILD DEFERRED AS SELECT * FROM sale_detail_jt; -- Query data from the mv_deferred materialized view. SELECT * FROM mv_deferred; -- The following result is returned: +-----------+-------------+-------------+-----------+--------+
| shop_name | customer_id | total_price | sale_date | region |
+-----------+-------------+-------------+-----------+--------+ +-----------+-------------+-------------+-----------+--------+ -- Create a partitioned table. CREATE TABLE mf_part (id bigint,name string) PARTITIONED BY (dt string); -- Insert data into the table. INSERT INTO mf_part PARTITION(dt='2013') VALUES(1,'name1'),(2,'name2'); -- Query data from the table. SELECT * FROM mf_part WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+ -- Create a partitioned materialized view. CREATE MATERIALIZED VIEW mv_rebuild BUILD DEFERRED PARTITIONED BY (dt) AS SELECT * FROM mf_part; -- Query data from the materialized view. SELECT * FROM mv_rebuild WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+ +------------+------+----+ -- Update the latest partition data to the materialized view. ALTER MATERIALIZED VIEW mv_rebuild REBUILD PARTITION(dt=max_pt('mf_part')); -- Query data from the materialized view. SELECT * FROM mv_rebuild WHERE dt='2013'; -- The following result is returned: +------------+------+----+
| id         | name | dt |
+------------+------+----+
| 1          | name1 | 2013 |
| 2          | name2 | 2013 |
+------------+------+----+
```

**Change the lifecycle of an existing materialized view**

You can change the lifecycle of an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> SET LIFECYCLE <days>;
```

Parameters and descriptions

| Parameter | Requi red | Description |
|---|---|---|
| project name _ | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to update. |
| days | Yes | The new lifecycle of the materialized view. Unit: days. |

```
-- Change the lifecycle of an existing materialized view to 10 days. ALTER MATERIALIZED VIEW count_mv SET LIFECYCLE 10;
```

**Enable or disable the lifecycle feature for an existing materialized view**

You can enable or disable the lifecycle feature for an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> [<pt_spec>] enable|disable LIFECYCLE;
```

Parameters and descriptions

| Parameter | Required | Description |   |
|---|---|---|---|
| project nam _ e | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |   |
| mv name _ | Yes | The name of the materialized view for which you want to enable or disable the lifecycle feature. |   |
| pt spec | No | The partition information of the materialized view for which you want to enable or disable the lifecycle feature. Format: (partition col1 = partition col value1, partition col2 = _ _ _ _ |   |
|   |   |   | (partition col1 = partition col value1, partition col2 = _ _ _ _ |
| _ |   | partition col value2, ...) _ _ |   |
| enable\|disa ble | Yes | The enable option specifies that the lifecycle feature is enabled for a materialized view or a partition of a materialized view. The disable option specifies that the lifecycle feature is disabled for a materialized view or a partition of a materialized view. If you disable the lifecycle feature, lifecycle management is not required for the materialized view or partition. |   |

Example 1: Enable the lifecycle feature for a materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') enable LIFECYCLE;
```

Example 2: Disable the lifecycle feature for a materialized view.

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts PARTITION (ds='1') disable LIFECYCLE;
```

**Query information about a materialized view**

You can query the information about a materialized view, including the schema and modification time of the materialized view. Command syntax

```
DESC EXTENDED [<project_name>.]<mv_name>;
```

Parameters and descriptions

| Parameter | Required | Description |
|---|---|---|
| project nam _ e | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to query. |

```
DESC EXTENDED mv;
```

Sample query result: The following sample result can be returned only if the version of the MaxCompute client is V0.43 or later.

```
+------------------------------------------------------------------------------------+
| Owner:                    ALIYUN$$****@***.aliyunid.com                       |
| Project:                  m****                                                |
| TableComment:                                                                      |
+------------------------------------------------------------------------------------+
| CreateTime:               2023-05-30 13:16:07                                      |
| LastDDLTime:              2023-05-30 13:16:07                                      |
| LastModifiedTime:         2023-05-30 13:16:07                                      |
+------------------------------------------------------------------------------------+
| MaterializedView: YES                                                              |
| ViewText: select id,name from mf_refresh                                           |
| Rewrite Enabled: true                                                              |
| AutoRefresh Enabled: true                                                          |
| Refresh Interval Minutes: 10                                                       |
+------------------------------------------------------------------------------------+
| Native Columns:                                                                    |
+------------------------------------------------------------------------------------+
| Field    | Type   | Label | ExtendedLabel | Nullable | DefaultValue | Comment      |
+------------------------------------------------------------------------------------+
| id       | bigint |       |               | true     | NULL         |              |
| name     | string |       |               | true     | NULL         |              |
+------------------------------------------------------------------------------------+
| Extended Info:                                                                     |
+------------------------------------------------------------------------------------+
| IsOutdated:               false                                                    |
| TableID:                  569ec712873e44b3868e79b7a8beabab                         |
| IsArchived:               false                                                    |
| PhysicalSize:             1875                                                     |
| FileNum:                  2                                                        |
| StoredAs:                 CFile                                                    |
| CompressionStrategy:      normal                                                   |
| odps.timemachine.retention.days: 1                                                        |
| ColdStorageStatus:        N/A                                                      |
| encryption_enable:        false                                                    |
+------------------------------------------------------------------------------------+
| AutoRefresh History:                                                               |
+------------------------------------------------------------------------------------+
| InstanceId                | Status     | StartTime           | EndTime             |
+------------------------------------------------------------------------------------+
| 20230619070546735ghwl1****** | TERMINATED | 2023-06-19 15:05:46 | 2023-06-19 15:05:47 |
| 20230619065545586gwllc****** | TERMINATED | 2023-06-19 14:55:45 | 2023-06-19 14:55:46 |
| 20230619064544463gcjgom****** | TERMINATED | 2023-06-19 14:45:44 | 2023-06-19 14:45:45 |
| 20230619063543334gzxs2d****** | TERMINATED | 2023-06-19 14:35:43 | 2023-06-19 14:35:44 |
| 2023061906254257gi21w2****** | TERMINATED | 2023-06-19 14:25:42 | 2023-06-19 14:25:43 |
| 20230619061540813giacg8****** | TERMINATED | 2023-06-19 14:15:41 | 2023-06-19 14:15:41 |
| 20230619060539674gswjq9****** | TERMINATED | 2023-06-19 14:05:39 | 2023-06-19 14:05:40 |
| 20230619055538578gvdjk****** | TERMINATED | 2023-06-19 13:55:38 | 2023-06-19 13:55:40 |
| 20230619054537356glqdne****** | TERMINATED | 2023-06-19 13:45:37 | 2023-06-19 13:45:38 |
| 2023061905353687gcc5pl****** | TERMINATED | 2023-06-19 13:35:36 | 2023-06-19 13:35:37 |
+------------------------------------------------------------------------------------+
```

**Query the status of a materialized view**

You can query the status of a materialized view. This operation allows you to view changes to the source table and determines whether the materialized view is valid. A materialized view can be in one of the following states: Valid When you execute a query statement, MaxCompute queries data from the materialized view instead of querying data from the source table. Invalid When you execute a query statement, MaxCompute cannot directly query data from the materialized view. In this case, MaxCompute queries data from the source table. As a result, the query speed is not accelerated. You can use a function to check whether data in a materialized view is valid. Function syntax

```
boolean materialized_view_is_valid(<mv_name>,<partition_value>);
```

Check whether data in the materialized view mf_mv_refresh4 is consistent with the latest data in the source table. If the data is consistent, `true` is returned. Otherwise, `false` is returned.

```
SELECT materialized_view_is_valid("count_mv"); SELECT materialized_view_is_valid("mf_mv_blank_pts","1");
```

**List all materialized views within a project**

You can use this feature to list all materialized views in a project or the materialized views that meet specific rules in a project. To run the `SHOW MATERIALIZED VIEWS` command on the MaxCompute client (odpscmd), the version of the MaxCompute client must be 0.43.0 or later. Command syntax

```
-- List all materialized views in a project. SHOW MATERIALIZED VIEWS; -- List the materialized views whose names match the condition specified by materialized_view in a project. SHOW MATERIALIZED VIEWS LIKE '<materialized_view>'; -- List the materialized views whose names match the test* keyword in a project. The asterisk (*) indicates a ny character. SHOW MATERIALIZED VIEWS LIKE 'test*';
```

Sample query result:

```
ALIYUN$account_name:test_two_mv ALIYUN$account_name:test_create_one_mv
```

**Drop an existing materialized view**

You can drop an existing materialized view. Command syntax

```
DROP MATERIALIZED VIEW [IF EXISTS] [<project_name>.]<mv_name> [purge];
```

Parameters and descriptions

| Parameter | Require d | Description |
|---|---|---|
| IF EXISTS | No | If you do not specify IF EXISTS and the materialized view does not exist, an error is returned. |
| project nam _ e | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |
| mv name _ | Yes | The name of the materialized view that you want to drop. |
| purge | No | If you specify the purge parameter, data in a materialized view is deleted when you drop the materialized view. |

Drop the `mv` materialized view.

```
DROP MATERIALIZED VIEW count_mv;
```

Drop the `mv` materialized view and delete the data in the materialized view at the same time.

```
DROP MATERIALIZED VIEW count_mv purge;
```

**Drop partitions from an existing materialized view**

You can drop one or more partitions from an existing materialized view. Command syntax

```
ALTER MATERIALIZED VIEW [<project_name>.]<mv_name> DROP [IF EXISTS] PARTITION <pt_spec> [PARTITION <pt_spec>, PARTITION <pt_spec>....];
```

Parameters and descriptions

| Parameter | Require d | Description |   |
|---|---|---|---|
| project nam _ e | No | The name of the MaxCompute project to which the materialized view belongs. If you do not configure this parameter, the current MaxCompute project is used. |   |
| mv name _ | Yes | The name of the partitioned materialized view from which you want to drop one or more partitions. |   |
| IF EXISTS | No | If you do not specify IF EXISTS and the materialized view does not exist, an error is returned. |   |
| pt spec | Yes | You must specify at least one partition. The partitions that you want to drop. You must specify at least one partition. Format: (partition col1 = partition col value1, partition col2 = _ _ _ _ |   |
|   |   |   | (partition col1 = partition col value1, partition col2 = _ _ _ _ |
| _ |   | partition col value2, ...) _ _ |   |

Example 1: Drop a partition from a partitioned materialized view. Sample command:

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds='1');
```

Example 2: Drop the partitions that meet the specific conditions from a partitioned materialized view. Sample command:

```
ALTER MATERIALIZED VIEW mf_mv_blank_pts DROP PARTITION (ds>='1' AND ds<='2');
```

**Perform a penetration query on a materialized view**

A partitioned materialized view does not contain the data of all partitions in a source partitioned table if only the latest partition data is updated to the partitioned materialized view. If the partition data that you want to query does not exist in a partitioned materialized view, the system performs a penetration query to query data from the source partitioned table. The following figure shows how to perform a penetration query. To allow a materialized view to support penetration query, you must configure the following parameters: When you create a materialized view, add `"enable_auto_substitute"="true"` to **tblproperties**. The following example shows how to perform a penetration query based on a materialized view.
1. Create a partitioned materialized view that supports penetration query.

```
-- Create a table named src. CREATE TABLE src(id bigint,name string) PARTITIONED BY (dt string); -- Insert data into the table. INSERT INTO src PARTITION(dt='20210101') VALUES(1,'Alex'); INSERT INTO src PARTITION(dt='20210102') VALUES(2,'Flink'); -- Create a partitioned materialized view that supports penetration query. CREATE MATERIALIZED VIEW IF NOT EXISTS mv LIFECYCLE 7 PARTITIONED BY (dt) tblproperties("enable_auto_substitute"="true") AS SELECT id, name, dt FROM src;
```

2. Query the data of the 20210101 partition in the src table from the mv materialized view.

```
SELECT * FROM mv WHERE dt='20210101';
```

3. Query the data of the 20210102 partition in the src table from the mv materialized view. The mv materialized view
does not contain the partition data. Therefore, a penetration query is performed to query the partition data from the src table.

```
SELECT * FROM mv WHERE dt = '20210102'; -- The preceding statement is equivalent to the following statement because the mv materialized view does not contain the data of the 20210102 partition, and the partition data needs to be queried from the src table. SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20210102') t;
```

4. Query the data of partitions 20201230 to 20210102 from the mv materialized view. The mv materialized view does
not contain all partition data. Therefore, a penetration query is performed to obtain the data that is not contained in the mv materialized view, and a UNION operation is performed on the obtained data and the data that is queried from the mv materialized view to return the final result.

```
SELECT * FROM mv WHERE dt >= '20201230' AND dt<='20210102' AND id='5'; -- The mv materialized view does not contain the data of the 20210102 partition, and a penetration query is p erformed to query the data of the 20210102 partition from the source table. The preceding statement is equiva lent to the following statement: SELECT * FROM (SELECT id, name, dt FROM src WHERE dt='20211231' OR dt='20210102'
 SELECT * FROM mv WHERE dt='20210101'
) t WHERE id = '5';
```

#### 3.4.4 Column and partition operations

##### 3.4.4.1 Add partitions

This topic describes how to use a DDL statement to add partitions.

```
alter table table_name add [if not exists] partition partition_spec; -- Add one partition at a time. alter table table_name add [if not exists] partition partition_spec [PARTITION partition_spec PARTITION partiti on_spec...] ; -- Add multiple partitions at a time.
```

If you do not specify **IF NOT EXISTS** and another partition with the same name exists, an error is returned. A MaxCompute table can contain a maximum of 60,000 partitions. To add a partition to a table that has multi-level partitions, you must specify all partition values.

```
alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou'); -- Add a partition to store the sales records of the China (Hangzhou) region for December 2017. alter table sale_detail add if not exists partition (sale_date='201712', region='shanghai'); -- Add a partition to store the sales records of the China (Shanghai) region for December 2017. alter table sale_detail add if not exists partition(sale_date='20171011'); -- Specify only the sale_date partition. An error is returned. alter table sale_detail add if not exists partition(region='shanghai'); -- Specify only the region partition. An error is returned. alter table sale_detail add if not exists partition (sale_date='201712', region='hangzhou') partition (sale_date='201712', region='shanghai'); -- Add two partitions to store the sales records of the China (Hangzhou) and China (Shanghai) regions for December 2017.
```

##### 3.4.4.2 Delete a partition

This topic describes how to use DDL statements to delete a partition. MaxCompute allows you to delete partitions that meet a specific filter condition. If you want to delete one or more partitions that meet a filter condition at a time, you can use an expression to specify the condition, use the condition to filter partitions, and then delete the partitions. If you do not specify a filter condition, execute the following statements:

```
alter table table_name drop [if exists] PARTITION partition_spec; -- Delete one partition at a time. alter table table_name drop [if exists] PARTITION partition_spec,PARTITION partition_spec,[PARTITION partition_spec....] ; -- Delete multiple partitions at a time.
```

Syntax for **partition_spec**:

```
partition_spec:(partition_col1 = partition_col_value1, partition_col2 = partiton_col_value2, ...)
```

If you specify a filter condition, execute the following statement:

```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION partition_filtercondition; -- Delete a partition based on the specified filter condition.
```

Syntax for **PARTITION partition_filtercondition**:

```
PARTITION partition_filtercondition
    : PARTITION (partition_col relational_operators partition_col_value)
    | PARTITION (scalar(partition_col) relational_operators partition_col_value)
    | PARTITION (partition_filtercondition1 AND|OR partition_filtercondition2)
    | PARTITION (NOT partition_filtercondition)
    | PARTITION (partition_filtercondition1)[,PARTITION (partition_filtercondition2), ...]
```

Parameters:
**table_name**: the name of the partitioned table from which you want to delete a partition.
**IF EXISTS**: If **IF EXISTS** is not specified and the partition does not exist, an error is returned.
**partition_spec**: the name of the partition that you want to delete. The value is not case-sensitive. **partition_col**
indicates the name of the partition key column, and **partition_col_value** indicates the value of the partition key column.
**PARTITION partition_filtercondition**: the partition that you want to delete. The value is not case-sensitive.
**partition_col**: the name of the partition key column.
**relational_operators**: the relational operator.
**partition_col_value**: a value in the partition key column, which is a comparison value or regular expression. The
data type of this value must be the same as that of the partition key column.
**scalar()**: the scalar function. This function generates a scalar based on the input value, processes the value in
**partition_col**, and uses the relational operator specified by **relational_operators** to compare the processed
value with **partition_col_value**. The filter condition that is used to delete partitions supports the following logical operators: NOT, AND, and OR. You can use PARTITION (NOT partition_filtercondition) to obtain the complementary set of the condition. You can use PARTITION (partition_filtercondition1 AND|OR partition_filtercondition2) to obtain the condition that is used to match the partitions you want to delete. Multiple PARTITION partition_filtercondition clauses are supported. If these clauses are separated by commas (,), OR is used for each clause to obtain the condition that is used to match the partitions you want to delete. Limits: Each PARTITION partition_filtercondition clause can be used for only one partition key column. If you use an expression to specify PARTITION partition_filtercondition, only the built-in scalar function can be used for the expression. The filter condition is not specified.

```
-- Delete a partition from the sale_detail table. The partition stores the sales records of the China (Hangzhou ) region in December 2017. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date='201712',region='hangzhou'); -- Delete two partitions from the sale_detail table at a time. The partitions store the sales records of the Ch ina (Hangzhou) and China (Shanghai) regions in December 2017. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date='201712',region='hangzhou'),PARTITION(sale_date='201712',region='shanghai');
```

The filter condition is specified.

```
-- Create a partitioned table. CREATE TABLE IF NOT EXISTS sale_detail( shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING); -- Add partitions. ALTER TABLE sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '201910') PARTITION (sale_date= '201911') PARTITION (sale_date= '201912') PARTITION (sale_date= '202001') PARTITION (sale_date= '202002') PARTITION (sale_date= '202003') PARTITION (sale_date= '202004') PARTITION (sale_date= '202005') PARTITION (sale_date= '202006') PARTITION (sale_date= '202007'); -- Delete multiple partitions from the table at a time. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date >= '202007'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date LIKE '20191%'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date IN ('202002','202004','202006')); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date BETWEEN '202001' AND '202007'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(substr(sale_date, 1, 4) = '2020'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201912' OR sale_date >= '202006'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date > '201912' AND sale_date <= '202004'); ALTER TABLE sale_detail DROP IF EXISTS PARTITION(NOT sale_date > '202004'); -- Delete partitions by using a condition. The condition is specified by expressions that have the OR relationship. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'), PARTITION(sale_date >= '202007'); -- Add partitions in other formats. ALTER TABLE sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '2019-10-05'); PARTITION (sale_date= '2019-10-06') PARTITION (sale_date= '2019-10-07'); -- Delete multiple partitions at a time and use regular expressions to match the partitions you want to delete. ALTER TABLE sale_detail DROP IF EXISTS PARTITION(sale_date RLIKE '2019-\\d+-\\d+'); -- Create a table that has multi-level partitions. CREATE TABLE IF NOT EXISTS region_sale_detail( shop_name STRING, customer_id STRING, total_price DOUBLE) PARTITIONED BY (sale_date STRING , region STRING ); -- Add partitions. ALTER TABLE region_sale_detail ADD IF NOT EXISTS PARTITION (sale_date= '201910',region = 'shanghai') PARTITION (sale_date= '201911',region = 'shanghai') PARTITION (sale_date= '201912',region = 'shanghai') PARTITION (sale_date= '202001',region = 'shanghai') PARTITION (sale_date= '202002',region = 'shanghai') PARTITION (sale_date= '201910',region = 'beijing') PARTITION (sale_date= '201911',region = 'beijing') PARTITION (sale_date= '201912',region = 'beijing') PARTITION (sale_date= '202001',region = 'beijing') PARTITION (sale_date= '202002',region = 'beijing'); -- Delete the partitions that meet the sale_date < '201911' and region = 'beijing' conditions from the table at a time. ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911'),PARTITION(region = 'beijing');
```

If you execute the following statement, the following error is returned: `FAILED: ODPS-0130071:[1,82] Semantic analysis`

```
exception - invalid column reference region, partition expression must have one and only one column reference . -- An error is returned because PARTITION partition_filtercondition can be specified only for one partition key column. ALTER TABLE region_sale_detail DROP IF EXISTS PARTITION(sale_date < '201911' AND region = 'beijing');
```

##### 3.4.4.3 Add columns or comments

This topic describes how to use DDL statements to add columns or comments.

```
ALTER TABLE table_name ADD COLUMNS (col_name1 type1,col_name2 type2...) ; -- Add columns. ALTER TABLE table_name ADD COLUMNS (col_name1 type1 comment 'XXX',col_name2 type2 comment 'XXX'); -- Add both columns and comments. ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING, education BIGINT); -- Add two columns to the sale_detail table. ALTER TABLE sale_detail ADD COLUMNS (customer_name STRING comment 'Customer', education BIGINT comment 'Educati on' ); -- Add two columns and their comments to the sale_detail table.
```

##### 3.4.4.4 Change the name of a column

This topic describes how to use a DDL statement to change the name of a column.

```
ALTER TABLE table_name CHANGE COLUMN old_col_name RENAME TO new_col_name;
```

The column specified by **old_col_name** must exist in the table. The table cannot contain the column specified by **new_col_name**.

```
ALTER TABLE sale_detail CHANGE COLUMN customer_name RENAME TO customer; -- Change the name of a column in the sale_detail table.
```

##### 3.4.4.5 Modify the comment of a column

This topic describes how to use a DDL statement to modify the comment of a column.

```
ALTER TABLE table_name CHANGE COLUMN col_name COMMENT 'comment_string';
```

The value of **comment_string** cannot exceed 1,024 bytes. The data type and position of a column cannot be changed. The column specified by **col_name** must exist.

```
ALTER TABLE sale_detail CHANGE COLUMN customer COMMENT 'customer'; -- Modify the comment of a column in the sale_detail table.
```

##### 3.4.4.6 Modify the name and comment of a column at the same time

**time**

This topic describes how to use a DDL statement to modify the name and comment of a column at the same time.

```
ALTER TABLE table_name CHANGE COLUMN old_col_name new_col_name column_type COMMENT 'column_comment';
```

The column specified by **old_col_name** must exist. The table cannot contain the column specified by **new_col_name**. The data type and position of a column cannot be changed. The value of **column_comment** cannot exceed 1,024 bytes.

```
ALTER TABLE sale_detail CHANGE COLUMN customer customer_name string COMMENT 'Customer'; -- Modify the name and comment of a column in the sale_detail table.
```

**3.4.4.7. Change LastDataModifiedTime of a non-partitioned table**

**or a partition in a partitioned table.**

MaxCompute SQL allows you to execute the TOUCH operation to modify the value of **LastDataModifiedTime** for a non-partitioned table or a partition in a partitioned table. This operation changes the value of **LastDataModifiedTime** to the current time. This topic describes how to use a DDL statement to change the value of LastDataModifiedTime for a non-partitioned table or a partition in a partitioned table.

```
ALTER TABLE table_name TOUCH; -- Change the value of LastDataModifiedTime for a non-partitioned table. ALTER TABLE table_name TOUCH PARTITION(partition_col='partition_col_value', ...); -- Change the value of LastDataModifiedTime for a partition in a partitioned table.
```

If the table specified by **table_name** does not exist, an error is returned. If the partition specified by **partition_col='partition_col_value'** does not exist, an error is returned. This operation changes the value of **LastDataModifiedTime** for a non-partitioned table or a partition in a partitioned table. In this case, MaxCompute considers a change to the table data and recalculates the lifecycle. Sample statements:

```
ALTER TABLE result_table TOUCH; -- Change the value of LastDataModifiedTime for a non-partitioned table. ALTER TABLE sale_detail TOUCH PARTITION(sale_date='201712'); -- Change the value of LastDataModifiedTime for a partition in a partitioned table.
```

##### 3.4.4.8 Modify partition values

This topic describes how to use a DDL statement to modify partition values.

```
ALTER TABLE table_name PARTITION (partition_col1 = 'partition_col_value1', partition_col2 = 'partiton_col_value2', ...) RENAME TO PARTITION (partition_col1 = 'partition_col_newvalue1', partition_col2 = 'partiton_col_newvalue2', ... ) ;
```

This statement can modify only the values rather than the names of partition key columns. To modify the values of one or more partitions in a table that has multi-level partitions, you must specify the partition values at each level. If the table specified by **table_name** does not exist, an error is returned.

```
ALTER TABLE sale_detail PARTITION (sale_date = '201712', region = 'hangzhou') RENAME TO PARTITION (sale_date = '201710', region = 'beijing'); -- Modify the partition values in the sale_detail table.
```

##### 3.4.4.9 Merge partitions

MaxCompute SQL allows you to execute the `MERGE PARTITION` statement to merge multiple partitions of a partitioned table into one partition. This operation deletes the dimension information about the merged partitions and moves data to a specific partition. This topic describes how to use a DDL statement to merge partitions. Syntax

```
ALTER TABLE <tableName> MERGE [IF EXISTS] PARTITION(<predicate>) [, PARTITION(<predicate2>) ...] OVERWRITE PART ITION(<fullPartitionSpec>) [PURGE];
```

If you do not specify **IF EXISTS** and the partition that you want to merge does not exist, an error is returned. If you specify **IF EXISTS** but no partitions meet the merge conditions, no new partitions are generated. If operations such as INSERT, RENAME, and DROP are performed at the same time to modify the source data when you execute the preceding statement, an error is returned even if you specified **IF EXISTS**. If the PURGE attribute is specified, you cannot back up or restore merged partitions by using metadata snapshots. Limits and troubleshooting: Partitions of external tables cannot be merged. After partitions of a clustered table are merged into one partition, the partition does not have the clustering attribute. You can merge a maximum of 4,000 partitions at a time. If an error that indicates the catalog server is busy is returned, you can try again later. If a hard link in Apsara Distributed File System is faulty, you can clear the recycle bin and try again. Sample code:

```
odps@ jet_zwz>SHOW PARTITIONS intpstringstringstring; ds=20181101/hh=00/mm=00 ds=20181101/hh=00/mm=10 ds=20181101/hh=10/mm=00 ds=20181101/hh=10/mm=10
```

`OK`

```
odps@ jet_zwz>DESC intpstringstringstring; +------------+------------+------------+------------+
| value      | ds         | hh         | mm         |
+------------+------------+------------+------------+
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 00         | 10         |
| 1          | 20181101   | 10         | 00         |
| 1          | 20181101   | 10         | 10         |
+------------+------------+------------+------------+ -- Partitions and data of a partitioned table: odps@ jet_zwz>ALTER TABLE intpstringstringstring MERGE PARTITION(hh='00') OVERWRITE PARTITION(ds='20181101', hh ='00', mm='00'); ID = 20190404025755844g80qwa7a
```

`OK`

```
-- Merge all partitions that meet the hh='00' condition into the ds=20181101/hh=00/mm=00 partition. odps@ jet_zwz>SHOW PARTITIONS intpstringstringstring; ds=20181101/hh=00/mm=00 ds=20181101/hh=10/mm=00 ds=20181101/hh=10/mm=10
```

`OK`

```
-- Query the partitions of the table after the merge operation is performed. odps@ jet_zwz>DESC intpstringstringstring; +------------+------------+------------+------------+
| value      | ds         | hh         | mm         |
+------------+------------+------------+------------+
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 00         | 00         |
| 1          | 20181101   | 10         | 00         |
| 1          | 20181101   | 10         | 10         |
+------------+------------+------------+------------+ -- Data in two partitions that meet the specified condition is merged into the specified partition.
```

### 3.5 DML statements

#### 3.5.1 INSERT

##### 3.5.1.1 Update data in a table

This topic describes how to use an INSERT statement to update data in a table. The `INSERT OVERWRITE` and `INSERT INTO` statements are used to write the data processing results of MaxCompute SQL to a destination table. The `INSERT INTO` statement inserts data into a table or partition. The `INSERT INTO` statement cannot be used to insert data into clustered tables. If you want to insert a small amount of test data, you can use this statement with VALUES.

| INSERT OVERWRITE |   | statemen |
|---|---|---|
| ition. The | INSERT OVERWRITE |   |

The `INSERT OVERWRITE` statement clears the original data in a table or partition and inserts data into the table or partition. The `INSERT OVERWRITE` statement cannot be used to insert data into specific columns.

```
INSERT OVERWRITE|INTO TABLE table_name [PARTITION (partcol1=val1, partcol2=val2 ...)] [(col1,col2 ...)] select_statement FROM from_statement [ZORDER BY zcol1 [, zcol2 ...]] ;
```

| Note The INSERT syntax in MaxCompute is different from that in MySQL or Oracle. In MaxCompute, INSERT OVERWRITE or INSERT INTO must be followed by the keyword TABLE, instead of directly followed by the table name parameter. _ To ensure data consistency during concurrent writes, MaxCompute uses the atomicity, consistency, isolation, durability (ACID) properties. The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. If the destination table consists of static partitions and you want to insert data into a static partition, partition key columns cannot be included in the SELECT clause. |   |   |
|---|---|---|
|   | INSERT |   |

Parameters:
**table_name**: the name of the table into which you want to insert data.
**PARTITION (partcol1=val1, partcol2=val2 ...)**: the name of the partition into which you want to insert data. The
value must be a constant. It cannot be an expression, such as a function.
**[(col1,col2 ...)]**: the names of the columns into which you want to insert data. This parameter is not supported in
the `INSERT OVERWRITE` statement.
**select_statement**: the SELECT clause used to query the data that you want to insert from the source table.
**from_statement**: the FROM clause used to indicate the data source. For example, the value can be the name of the
source table.
**[ZORDER BY zcol1 [, zcol2 ...]]**: the columns that are used to sort data. If you write data to a table or partition,
you can use this clause to place rows with similar data records in the columns specified in select_statement in adjacent positions. This improves filtering performance for queries and reduces storage costs. The `ORDER BY x, y` clause sorts data records based on the ordering of x coming before y. The `ZORDER BY x, y` clause places rows that have similar x values in adjacent positions and rows that have similar y values in adjacent positions. If the filter condition of an SQL query statement includes sort columns, the ORDER BY clause filters and sorts data based on x, whereas the ZORDER BY clause filters and sorts data based on x or on both x and y. ZORDER BY increases the column store ratio. The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. If the destination table consists of static partitions and you want to insert data into a partition, partition key columns cannot be included in the SELECT clause. The ZORDER BY clause occupies a large number of resources to write data. As a result, data writes based on ZORDER BY require a longer time than data writes without ordering. If the destination table is a clustered table, ZORDER BY is not supported. ZORDER BY can be used with DISTRIBUTE BY. However, ZORDER BY cannot be used with ORDER BY, CLUSTER BY, or SORT BY. Calculate the sales of different regions listed in the sale_detail table. Then, insert the obtained data into the sale_detail_insert table.

```
-- Create a partitioned table named sale_detail, add partitions, and insert data into the table. You do not nee d to define partition key columns as standard columns in the statement that is used to create the source table. CREATE TABLE IF NOT EXISTS sale_detail
```

`(`

```
shop_name string, customer_id string, total_price double
```

`)`

```
PARTITIONED BY (sale_date STRING,region STRING); -- Add partitions to the source table. ALTER TABLE sale_detail ADD PARTITION (sale_date='2013', region='china'); -- Insert data into the source table. INSERT INTO TABLE table_name can be abbreviated as INSERT INTO table_name. However, INSERT OVERWRITE TABLE table_name has no abbreviation. INSERT INTO sale_detail PARTITION (sale_date='2013', region='china') VALUES ('s1','c1',100.1), ('s2','c2',100.2),('s3','c3',100.3); -- Create a destination table named sale_detail_insert that has the same schema as the source table. CREATE TABLE sale_detail_insert LIKE sale_detail; -- Add partitions to the destination table. ALTER TABLE sale_detail_insert ADD PARTITION (sale_date='2013', region='china'); -- Extract data from the sale_detail table and insert the data into the sale_detail_insert table. -- Fields in the destination table do not need to be declared or rearranged. -- If the destination table consists of static partitions and partition fields have been declared in PARTITION(), you do not need to include these fields in the SELECT clause. You only need to search for the fiel ds based on the sequence of standard columns in the destination table and sequentially map these fields to thos e in the destination table. If the destination table consists of dynamic partitions, partition fields must be i ncluded in the SELECT clause. For more information, see Insert data into dynamic partitions. INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
  shop_name,
  customer_id,
  total_price
  FROM sale_detail
  ZORDER BY customer_id, total_price;
```

Take note of the following points: The mappings between the source and destination tables are based on the column sequence in the SELECT clause. The mappings between the column names of the tables are not considered. Example:

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
    SELECT customer_id, shop_name, total_price FROM sale_detail;
```

In the created sale_detail_insert table, the columns **shop_name STRING**, **customer_id STRING**, and **total_price**
**BIGINT** are listed in sequence. If you insert data from the sale_detail table to the sale_detail_insert table, the data is
inserted from the **customer_id**, **shop_name**, and **total_price** columns in sequence. In this case, data in
**sale_detail.customer_id** is inserted into **sale_detail_insert.shop_name**, and data in **sale_detail.shop_name** is
inserted into **sale_detail_insert.customer_id**. If you insert data into a partition, partition key columns cannot be included in the SELECT clause. If you execute the following statement, an error is returned because **sale_date** and **region** are partition key columns. These columns cannot be included in the INSERT statement that is used to insert table data into a static partition.

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date='2013', region='china')
   SELECT shop_name, customer_id, total_price, sale_date, region FROM sale_detail;
```

The value of **PARTITION** must be a constant and cannot be an expression. The following example shows invalid settings:

```
INSERT OVERWRITE TABLE sale_detail_insert PARTITION (sale_date=datepart('2016-09-18 01:10:00', 'yyyy') , regi on='china')
   SELECT shop_name, customer_id, total_price FROM sale_detail;
```

**Precautions**

If you want to update table data to a dynamic partition, take note of the following points: If you execute the `INSERT INTO PARTITION` statement and the specified partition does not exist, the system automatically creates this partition. If multiple jobs that use the `INSERT INTO PARTITION` statement concurrently run and the specified partitions do not exist, the system attempts to create these partitions. However, only one partition can be created. If you cannot control the concurrency of the jobs that use the `INSERT INTO PARTITION` statement, we recommend that you use the `ALTER TABLE` statement to create partitions in advance.

##### 3.5.1.2 Insert data into multiple objects

This topic describes how to use an INSERT statement to insert data to multiple objects. MaxCompute SQL allows you to insert data into different result tables or partitions by using one SQL statement.

```
FROM from_statement INSERT OVERWRITE | INTO TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...)] select_statement1 [FROM from_statement] [INSERT OVERWRITE | INTO TABLE tablename2 [PARTITION (partcol1=val3, partcol2=val4 ...)] select_statement2 [FROM from_statement]];
```

In most cases, an SQL statement supports up to 256 outputs. If the number of outputs exceeds 256, a syntax error is returned. In a MULTI INSERT statement, non-partitioned tables and destination partitions in a partitioned table must be unique. The `INSERT OVERWRITE` and `INSERT INTO` operations cannot be simultaneously performed on different partitions of a table. If these operations are simultaneously performed on the partitions, an error is returned.
**PARTITION (partcol1=val1, partcol2=val2 ...)**: The parameter values can be only constants rather than
expressions, such as functions.

```
-- Create a destination table named sale_detail_multi. create table sale_detail_multi like sale_detail; -- Insert data from sale_detail into sale_detail_multi. set odps.sql.allow.fullscan=true; -- Enable the full table scan, which is valid only for this session. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price ; -- An error is returned because the same partition appears more than once. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price; -- An error is returned because the INSERT OVERWRITE and INSERT INTO operations are simultaneously performed on different partitions of a partitioned table. from sale_detail insert overwrite table sale_detail_multi partition (sale_date='2010', region='china' ) select shop_name, customer_id, total_price insert into table sale_detail_multi partition (sale_date='2011', region='china' ) select shop_name, customer_id, total_price;
```

##### 3.5.1.3 Insert data into dynamic partitions

This topic describes how to use an INSERT statement to insert data into dynamic partitions. You can use the INSERT OVERWRITE statement to insert data into the following partitions of a partitioned table: Static partitions: You must specify partition values in the INSERT statement to insert data into the specified partitions. Dynamic partitions: You need only to specify the names of partition key columns in the INSERT statement. The values of the partition key columns are provided in the SELECT clause. The system automatically inserts data into the required partitions based on the values.

```
INSERT OVERWRITE|INTO TABLE tablename PARTITION (partcol1, partcol2 ...) select_statement FROM from_statement;
```

A maximum of 10,000 dynamic partitions can be generated by using the INSERT INTO statement. A maximum of 60,000 dynamic partitions can be generated by using the INSERT OVERWRITE statement. An SQL statement that is used to insert data into dynamic partitions in a distributed environment can generate a maximum of 512 dynamic partitions in a single process. If the number of dynamic partitions exceeds this limit, an exception occurs. The dynamically generated partition values cannot be NULL or contain special characters. If a value is NULL or contains special characters, an exception occurs.

```
FAILED: ODPS-0123031:Partition exception - invalid dynamic partition value: province=xxx
```

If the destination table has multi-level partitions, you can specify some partitions as static partitions in an INSERT statement. However, the static partitions must be high-level partitions. If the destination table is a hash-clustered table, dynamic partitions are not supported. If you insert data into dynamic partitions, the mappings between the columns in **select_statement** and dynamic partitions in the destination table are determined by the column sequence, not by the column names. If the sequence of columns in the source table is different from that in the destination table, we recommend that you specify the columns in **select_statement** based on the column sequence in the destination table. Insert data from a source table into a destination table. You can obtain the partitions generated based on the region field only after the required statement is executed.

```
-- Create a destination table named total_revenues. create table total_revenues (revenue bigint) partitioned by (region string); -- Insert the data from sale_detail into total_revenues. insert overwrite table total_revenues partition(region) select total_price as revenue, region from sale_detail;
```

Insert data from a source table into a destination table. If the destination table has multi-level partitions, level-1 partition sale_date must be specified.

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price,region from sale_detail;
```

To insert data into dynamic partitions, the dynamic partition key columns must be specified in the SELECT clause. Otherwise, the execution fails.

```
insert overwrite table sale_detail_dypart partition (sale_date='2013', region) select shop_name,customer_id,total_price from sale_detail;
```

If you specify only low-level subpartitions when you insert data into dynamic partitions, you may fail to insert data into high-level partitions.

```
insert overwrite table sales partition (region='china', sale_date) select shop_name,customer_id,total_price,sale_date from sale_detail;
```

If the data types of values in partition key columns are inconsistent with those in the SELECT clause, an error is returned when data is inserted into dynamic partitions in MaxCompute V1.0. MaxCompute V2.0 supports the implicit conversions of data types.

```
-- Create a destination table named parttable. create table parttable(a int, b double) partitioned by (p string); -- Insert the data from source table src into destination table parttable. insert into parttable partition(p) select key, value, current_timestmap() from src; -- Query data in parttable. select * from parttable;
```

##### 3.5.1.4 VALUES

This topic describes how to use the INSERT...VALUES statement to insert data into a table that contains small amounts of data.

```
INSERT INTO TABLE tablename [PARTITION (partcol1=val1, partcol2=val2,...)][(co1name1,colname2,...)] [VALUES (col1_value,col2_value,...),(col1_value,col2_value,...),...]
```

Parameters:
**tablename**: the name of the table into which you want to insert data. The table must be an existing table.
**[PARTITION (partcol1=val1, partcol2=val2,...)]**: the information about partitions. If you want to insert data into
a partitioned table, you must configure this parameter.
**[(co1name1,colname2,...)]**: the names of the columns in the destination table.
**col_value**: the value in the specified column in the destination table. Separate multiple values with commas (,).
Each value in the column must be a constant. If no values are specified, the default value NULL is used. You can use only the `INSERT INTO` statement rather than the `INSERT OVERWRITE` statement to insert data into specific columns. Functions cannot be used to construct constants for some complex data types, such as ARRAY, in VALUES. However, you can use the following statement to pass the values of the ARRAY type to VALUES:

```
INSERT INTO TABLE srcp (p='abc') SELECT 'a', ARRAY('1', '2', '3');
```

To pass the values of the DATETIME or TIMESTAMP type, you must specify the data type in VALUES.

```
INSERT INTO TABLE srcp (p='abc') VALUES (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789');
```

Example: Insert data into a specific partition.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into the abc partition of the srcp table. INSERT INTO TABLE srcp PARTITION (p='abc') VALUES ('a',1),('b',2),('c',3); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| a          | 1          | abc        |
| b          | 2          | abc        |
| c          | 3          | abc        |
+------------+------------+------------+
```

Insert data into a random partition.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into a partition of the srcp table. INSERT INTO TABLE srcp PARTITION (p)(key,p) VALUES ('d','20170101'),('e','20170101'),('f','20170101'); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='20170101';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| d          | NULL       | 20170101   |
| e          | NULL       | 20170101   |
| f          | NULL       | 20170101   |
+------------+------------+------------+
```

Use complex data types to construct constants and execute an `INSERT` statement to import data.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string,value array<int>) partitioned by (p string); -- Add a partition to the srcp table. alter table srcp add if not exists partition (p='abc'); -- Insert data into the abc partition of the srcp table. insert into table srcp partition (p='abc') select 'a', array(1, 2, 3); -- Query data from the srcp table. select * from srcp where p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| a          | [1,2,3]    | abc        |
+------------+------------+------------+
```

Use the `INSERT...VALUES` statement to write data of the DATETIME or TIMESTAMP type.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string, value timestamp) partitioned by (p string); -- Add a partition to the srcp table. alter table srcp add if not exists partition (p='abc'); -- Insert data into the abc partition of the srcp table. insert into table srcp partition (p='abc') values (datetime'2017-11-11 00:00:00',timestamp'2017-11-11 00:00:00.123456789'); -- Query data from the srcp table. select * from srcp where p='abc';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| 2017-11-11 00:00:00 | 2017-11-11 00:00:00.123456789 | abc        |
+------------+------------+------------+
```

**Features of VALUES TABLE**

When you use INSERT…VALUES, the values after VALUES must be constants. If you want to perform simple computing operations on the inserted data, we recommend that you use VALUES TABLE of MaxCompute.

```xml
values (<col1_value>,<col2_value>,...),(<col1_value>,<col2_value>,...),<table_name> (<col1_name> , <col2_name>,...)...
```

You can use VALUES TABLE in the following scenarios: If no physical tables are available, create a table that contains multiple rows of data and perform computing operations on the table. For example, VALUES (…), (...) t(a, b) defines that a table named t contains the a and b columns. The a column is of the STRING data type and the b column is of the BIGINT data type. The data type of a column must be derived from the VALUES list.

```
-- Delete the srcp table that already exists in the system. DROP TABLE IF EXISTS srcp; -- Create a partitioned table named srcp. CREATE TABLE IF NOT EXISTS srcp (key string,value bigint) PARTITIONED BY (p string); -- Insert data into the srcp table. INSERT INTO TABLE srcp PARTITION (p) SELECT concat(a,b), length(a)+length(b),'20170102' FROM VALUES ('d',4),( 'e',5),('f',6) t(a,b); -- Query data from the srcp table. SELECT * FROM srcp WHERE p='20170102';
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| d4         | 2          | 20170102   |
| e5         | 2          | 20170102   |
| f6         | 2          | 20170102   |
+------------+------------+------------+
```

Use VALUES TABLE rather than the combination of `SELECT * FROM` and `UNION ALL` to create a constant-type table.

```
SELECT 1 c UNION ALL SELECT 2 c; -- The preceding statement is equivalent to the following statement: SELECT * FROM VALUES (1), (2) t(c);
```

The following result is returned:

```
+------------+
| c          |
+------------+
| 1          |
| 2          |
+------------+
```

Use the special forms of VALUES TABLE. If the expressions of the SELECT statement do not contain upstream table data, you can execute the SELECT statement without the FROM clause. In this case, the underlying implementation is to select data from an anonymous VALUES table that contains only one row and no columns. This way, you can test user-defined functions (UDFs) or other functions without the need to manually create DUAL tables.

```
-- Create a partitioned table named srcp. create table if not exists srcp (key string,value bigint) partitioned by (p string); -- Insert data into the srcp table. insert into table srcp partition (p) select abs(-1), length('abc'), getdate(); -- Query data from the srcp table. select * from srcp;
```

The following result is returned:

```
+------------+------------+------------+
| key        | value      | p          |
+------------+------------+------------+
| 1          | 3          | 2020-11-25 18:39:48 |
+------------+------------+------------+
```

**Support for expressions that do not contain constants**

Constant expressions are supported in VALUES expressions. Expressions that do not contain constants are also supported in VALUES expressions. Syntax:

```
select * from values (udf(1)),(to_date('20190101', 'yyyyMMdd')),(getdate()) t(d);
```

#### 3.5.2 SELECT

##### 3.5.2.1 SELECT operations

This topic describes how to use SELECT statements for SELECT operations. Syntax

```
SELECT [ALL | DISTINCT] select_expr, select_expr, ... FROM table_reference [WHERE where_condition] [GROUP BY col_list] [ORDER BY order_condition] [DISTRIBUTE BY distribute_condition [SORT BY sort_condition] ] [LIMIT number];
```

A SELECT statement can return a maximum of 10,000 rows of results. However, no limits are imposed when the SELECT statement is used as a clause. If the SELECT statement is used as a clause, the clause returns all results in response to the query from the upper layer. You are not allowed to perform full table scans on partitioned tables by using SELECT statements. If you want to perform a full table scan on a partitioned table, add set odps.sql.allow.fullscan=true; before the SQL statement that is used for the full table scan. Then, commit and run the added command with the SQL statement. To enable the full table scan for the entire project, run the following command:

```
setproject odps.sql.allow.fullscan=true;
```

**Column expression (select_expr)**

Each select_expr expression indicates a column from which you want to read data. You can use the following select_expr expressions to read data from a table. Specify the names of the columns from which you want to read data.

```
select shop_name from sale_detail;
```

Use an asterisk (*) to represent all columns.

```
select * from sale_detail; -- You can also use a WHERE clause to specify filter conditions. select * from sale_detail where shop_name like 'hang%';
```

**Use a regular expression.**

Use DISTINCT before the name of a column to filter out duplicate values from the column and return only distinct values. If you use ALL before the name of a column, all values including the duplicate values in the column are returned. If DISTINCT is not used, the default value ALL is used.

```
-- Query data from the region column in the sale_detail table and return only distinct values. select distinct region from sale_detail;
```

The following result is returned:

```
+------------+
| region     |
+------------+
| shanghai   |
+------------+ -- If you use DISTINCT in a SELECT statement where multiple columns are specified, DISTINCT applies to all th e columns you specified, instead of a single column. Mappings exist between columns. If you perform deduplication on multiple columns, the mappings may be destroyed. select distinct region, sale_date from sale_detail;
```

The following result is returned:

```
+------------+------------+
| region     | sale_date  |
+------------+------------+
| shanghai   | 20191110   |
+------------+------------+
```

**Information about a queried destination table (table_reference)**

table_reference specifies the table that you want to query. Nested subqueries are also supported in table_reference. Sample code:

```
select * from (select region from sale_detail) t where region = 'shanghai';
```

**WHERE**

The following table describes the operators that are used as filter conditions supported by the WHERE clause.

| Operator | Description |
|---|---|
| >, <, =, ≥, ≤, and <> | The relational operators. |
| LIKE and RLIKE | The source and pattern parameters of LIKE and RLIKE must be of the STRING type. |
| IN and NOT IN | If a subquery is added after the IN or NOT IN operator, the values in only one column can be returned for the subquery and the number of return values cannot exceed 1,000. |
| BETWEEN…AND | The operator that specifies the query range. |

In the WHERE clause of a SELECT statement, you can specify the partitions that you want to scan in a table to avoid a full table scan.

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date >= '2008' AND sale_detail.sale_date <= '2014';
```

User-defined functions (UDFs) support partition pruning. UDFs are run as small jobs and then replaced with the execution results. You can use one of the following methods to implement UDF-based partition pruning: Add an annotation to the UDF class when you write a UDF.

```
@com.aliyun.odps.udf.annotation.UdfProperty(isDeterministic=true)
```

**Important**

**com.aliyun.odps.udf.annotation.UdfProperty** defines that the version of referenced **odps-sdk-udf** must
be 0.30.x or later in odps-sdk-udf.jar. Add the set odps.sql.udf.ppr.deterministic = true; flag before the SQL statement that you want to execute. Then, all UDFs in the SQL statement are considered **deterministic** UDFs.

|   | Note The preceding SET command backfills partitions with the results of jobs. A maximum of 1,000 partitions can be backfilled with the results of jobs. If you add an annotation to a UDF class, an error that indicates more than 1,000 partitions are backfilled may be returned. To ignore this error, you can run the set odps.sql.udf.ppr.to.subquery = false; command. After you run this command, UDF-based partition pruning is no longer in effect. |
|---|---|
|   | odps.sql.udf.ppr.to.subquery = false; |

Precautions When you use a UDF to perform partition pruning, the UDF must be placed in the `WHERE` clause that is used to query a table. UDF-based partition pruning takes effect only when you place the UDF in the WHERE clause. Sample statement of correct usage:

```
-- Place a UDF in the WHERE clause that is used to query the source table. SELECT key, value from srcp where udf(ds) = 'xx';
```

Sample statement of incorrect usage:

```
-- Place a UDF after the ON condition in the JOIN clause. UDF-based partition pruning does not take effect. SELECT A.c1, A.c2 from srcp1 A join srcp2 B on A.c1 = B.c1 and udf(A.ds) ='xx';
```

The WHERE clause in an SQL statement can include the BETWEEN...AND operator. Sample code:

```
SELECT sale_detail.* FROM sale_detail WHERE sale_detail.sale_date BETWEEN '2008' AND '2014';
```

**GROUP BY**

In most cases, the GROUP BY clause is used with aggregate functions. If a SELECT statement contains aggregate functions, you must comply with the following rules: The operation specified by the GROUP BY clause takes precedence over the operation specified by the SELECT statement. Therefore, columns in the GROUP BY clause can be specified by column names of the input table of the SELECT statement or an expression that is formed by columns of the input table of the SELECT statement. The columns in GROUP BY cannot be the aliases of the output columns from SELECT. The value of GROUP BY may be both a column name or an expression composed of input table columns and the alias of an output column from SELECT. In this case, the column name or expression is used as the value of GROUP BY. If set hive.groupby.position.alias=true; is added before an SQL statement, integer constants in the GROUP BY clause are considered column numbers in a SELECT operation.

```
set hive.groupby.position.alias=true; -- Run this command with the next SELECT statement. select region, sum(total_price) from sale_detail group by 1; -- 1 indicates the region column, which is the first column read by the SELECT statement. This statement grou ps the table data based on the values in the region column and returns distinct region values and total sales of each group. -- The statement uses the name of the region column in the input table as the value of the GROUP BY clause and groups the table data based on the values in the region column. select region from sale_detail group by region; -- The statement groups the table data based on the values in the region column and returns the total sales of each group. select sum(total_price) from sale_detail group by region; -- The statement groups the table data based on the values in the region column and returns distinct values and total sales of each group. select region, sum(total_price) from sale_detail group by region; -- An error is returned because the alias of the column in the SELECT operation is used as the value of the GRO UP BY clause. select region as r from sale_detail group by r; -- A complete expression of the column is required. select 2 + total_price as r from sale_detail group by 2 + total_price; -- An error is returned because all the columns that do not use aggregate functions in the SELECT operation mus t be included in the GROUP BY clause. select region, total_price from sale_detail group by region; -- The statement can be successfully executed because all the columns that do not use aggregate functions are i ncluded in the GROUP BY clause. select region, total_price from sale_detail group by region, total_price;
```

**ORDER BY|DISTRIBUTE BY|SORT BY**

ORDER BY: This clause is used to sort all data records based on the specified columns. To sort data records in descending order, use the **desc** keyword. By default, data records are sorted in ascending order. When you use ORDER BY to sort data records, null is considered the smallest value. This rule is consistent with MySQL, but is different from Oracle. The columns in the ORDER BY clause must be the aliases of the columns in the SELECT operation. If you want to query a column but the column alias is not specified in the SELECT statement, the column name is used as the column alias. If set hive.orderby.position.alias=true; is added before an SQL statement, integer constants in the ORDER BY clause are considered column numbers in a SELECT operation.

```
-- Configure the flag. set hive.orderby.position.alias=true; -- Create a table named src. create table src(key BIGINT,value BIGINT); -- Query the src table and sort the records that are returned in ascending order by value. SELECT * FROM src ORDER BY 2 limit 100; The preceding statement is equivalent to the following statement: SELECT * FROM src ORDER BY value limit 100;
```

You can use the OFFSET clause with the ORDER BY LIMIT clause to skip the number of rows specified by OFFSET.

```
-- Sort the rows of the src table in ascending order by key, and return row 11 to row 30. OFFSET 10 indicat es that the first 10 rows are skipped, and LIMIT 20 indicates that a maximum of 20 rows can be returned. SELECT * FROM src ORDER BY key LIMIT 20 OFFSET 10; -- Query the sale_detail table and sort the first 100 records that are returned in ascending order by region. SELECT * FROM sale_detail ORDER BY region LIMIT 100; -- By default, the LIMIT clause is used with the ORDER BY clause. If only the ORDER BY clause is used, an err or is returned. SELECT * FROM sale_detail ORDER BY region; -- ORDER BY is followed by a column alias. SELECT region AS r FROM sale_detail ORDER BY region LIMIT 100; SELECT region AS r FROM sale_detail ORDER BY r LIMIT 100;
```

DISTRIBUTE BY: This clause is used to shard data based on hash values of specific columns. You must specify the alias of an output column from the SELECT operation as the value of the DISTRIBUTE BY clause.

```
-- The statement queries the values of the region column from the sale_detail table and performs hash partiti oning on data based on the values of the region column. SELECT region FROM sale_detail DISTRIBUTE BY region; -- The statement can be executed because the column name is used as the alias. SELECT region AS r FROM sale_detail DISTRIBUTE BY region; The preceding statement is equivalent to the following statement: SELECT region AS r FROM sale_detail DISTRIBUTE BY r;
```

SORT BY: This clause is used to sort specific data records. You can add a keyword, such as ASC or DESC, to sort specific data records. If ASC is used, data records are sorted in ascending order. If DESC is used, data records are sorted in descending order. If SORT BY is not followed by a keyword, data records are sorted in ascending order by default. If the SORT BY clause is preceded by the DISTRIBUTE BY clause, the SORT BY clause sorts specific results of the DISTRIBUTE BY clause. The DISTRIBUTE BY clause determines how to distribute the output values of the map stages to reducers. To prevent duplicate output values from being distributed to different reducers or to process the same group of data together, you can use the DISTRIBUTE BY clause. This ensures that the same group of data is distributed to the same reducer. Then, use SORT BY to sort the group of data. Example

```
-- The statement queries values in the region column of the sale_detail table, shards data based on the has h values of the region column, and then sorts the sharded data. SELECT region FROM sale_detail DISTRIBUTE BY region SORT BY region;
```

If the SORT BY clause is not preceded by the DISTRIBUTE BY clause, the SORT BY clause sorts the data of each reducer. This process sorts specific data records. This ensures that the output values of each reducer are sorted and increases the data compression ratio. If data is filtered during data reading, the amount of data read from disks is reduced, which makes subsequent global sorting more efficient. Example

```
SELECT region FROM sale_detail SORT BY region;
```

The value of ORDER BY, DISTRIBUTE BY, or SORT BY must be the alias of an output column from the SELECT statement. Column aliases can be Chinese. During the parsing of MaxCompute SQL statements, the ORDER BY, DISTRIBUTE BY, or SORT BY clause is executed after the SELECT operation. Therefore, the value of ORDER BY, DISTRIBUTE BY, or SORT BY must be the alias of an output column from the SELECT operation. The ORDER BY clause cannot be used with the DISTRIBUTE BY or SORT BY clause. The GROUP BY clause cannot be used with the DISTRIBUTE BY or SORT BY clause.

**LIMIT**

The **number** in the LIMIT clause is a constant that limits the number of rows to return. Remove the limit on the simultaneous execution of the ORDER BY and LIMIT clauses The ORDER BY clause needs to sort all data of a single node. By default, the ORDER BY clause is used with the LIMIT clause to prevent a single node from processing large amounts of data. You can remove the limit on the simultaneous execution of the ORDER BY and LIMIT clauses for a project or session. To remove the limit for a project, run the setproject odps.sql.validate.orderby.limit=false; command. To remove the limit for a session, run the setproject odps.sql.validate.orderby.limit=false; command with the SQL statement. If a single node has large amounts of data to sort after the limit is removed, more resources and time are required. Limits on the number of rows to return If you use a SELECT statement without the LIMIT clause or the number in the LIMIT clause exceeds the specified upper limit, you can view only the rows within the upper limit. The maximum number of rows that can be displayed varies based on projects. You can use one of the following methods to control the maximum number: If project data protection is disabled by setting **use_instance_tunnel** to true and **instance_tunnel_max_record** is not specified, no limits are imposed on the number of rows to return. For more information about project data protection, see Data protection. For more information about the configurations of **use_instance_tunnel=true** and
**instance_tunnel_max_record**, see Tunnel operations.
If project data protection is enabled, the number of rows to return is limited by **READ_TABLE_MAX_ROW**. The maximum value of this parameter is 10000. You can run the SHOW SecurityConfiguration; command to view the value of **ProjectProtection**. If
**ProjectProtection** is set to true, you can determine whether to disable project data protection. You can run the
set ProjectProtection=false; command to disable project data protection. By default, **ProjectProtection** is disabled. For more information about project data protection, see Data protection.

##### 3.5.2.2 Subquery

This topic describes how to use a SELECT statement to perform subqueries. A common SELECT statement reads data from multiple tables, such as, `select column_1, column_2 ... from` `table_name` . The query object can be another SELECT operation, which is a subquery.

```
select * from (select shop_name from sale_detail) a;
```

**Important**

A subquery must have an alias.

```
create table shop as select * from sale_detail; select a.shop_name, a.customer_id, a.total_price from (select * from shop) a join sale_detail on a.shop_name = sale_detail.shop_name;
```

In a FROM clause, a subquery can be used as a table, which supports a JOIN operation with other tables or subqueries.

##### 3.5.2.3 UNION ALL

This topic describes how to use a SELECT statement to perform UNION ALL operations.

```
select_statement union all select_statement
```

The UNION ALL clause is used to combine two or more datasets returned from a SELECT operation into one dataset. If duplicate rows exist in the results, all rows that meet the condition are returned, with duplicate rows retained. MaxCompute SQL does not support UNION ALL between two top-level query statements. To combine the query results of the two statements, you must rewrite the UNION ALL clause as a subquery. Syntax before rewriting:

```
select * from sale_detail where region = 'hangzhou' select * from sale_detail where region = 'shanghai';
```

Syntax after rewriting:

```
select * from ( select * from sale_detail where region = 'hangzhou' union all select * from sale_detail where region = 'shanghai') t;
```

The syntax that uses a pair of parentheses to specify the priority of UNION ALL is supported.

```
SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3); -- Execute the UNION ALL clause for the src2 and src3 tables. Then, execute the UNION ALL clause for the src ta ble and the result of the first UNION ALL operation.
```

**Important**

For a UNION ALL operation, all subqueries must have the same number of columns, column names, and column types. If the column names are inconsistent, use column aliases. In most cases, MaxCompute allows a UNION ALL operation for a maximum of 256 subqueries. If the limit is exceeded, a syntax error is returned.

##### 3.5.2.4 JOIN

This topic describes how to use SELECT statements to perform JOIN operations. MaxCompute supports multiple JOIN operations in an SQL statement. MaxCompute does not support CROSS JOIN. A CROSS JOIN operation joins two tables without the need to specify conditions in the ON clause.

```
join_table:
        table_reference JOIN table_factor [join_condition]
        | table_reference {LEFT OUTER|RIGHT OUTER|FULL OUTER|INNER|NATURAL} JOIN table_reference join_condition
    table_reference:
        table_factor
        | join_table
    table_factor:
        tbl_name [alias]
        | table_subquery alias
        | ( table_references )
    join_condition:
        ON equality_expression ( AND equality_expression )
```

**equality_expression** indicates an equality expression.
Types of JOIN operations: LEFT OUTER JOIN: shortened as LEFT JOIN. It returns all rows in the left table, including the rows that do not match any rows in the right table.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a LEFT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name; -- Both the shop and sale_detail tables have the shop_name column. You must use aliases to distinguish the co lumns in the SELECT operation.
```

If the values in some rows of the right table are duplicate, we recommend that you do not consecutively use LEFT JOIN. If you consecutively use LEFT JOIN, data bloat may occur and interrupt your jobs. RIGHT OUTER JOIN: shortened as RIGHT JOIN. It returns all rows in the right table, including rows that do not match any rows in the left table.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a RIGHT OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

FULL OUTER JOIN: shortened as FULL JOIN. It returns all rows in both the left and right tables.

```
SELECT a.shop_name AS ashop, b.shop_name AS bshop FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name;
```

INNER JOIN: The INNER keyword can be omitted. INNER JOIN only returns rows in which a match between the two tables exists.

```
SELECT a.shop_name FROM shop a INNER JOIN sale_detail b ON a.shop_name=b.shop_name; SELECT a.shop_name FROM shop a JOIN sale_detail b ON a.shop_name=b.shop_name;
```

NATURAL JOIN: In a NATURAL JOIN operation, the conditions used to join two tables are automatically determined based on the common fields in the two tables. MaxCompute supports OUTER NATURAL JOIN. You can use the USING clause so that the JOIN operation returns common fields only once.

```
SELECT * FROM src NATURAL JOIN src2; -- Both the src and src2 tables include the key1 and key2 fields. In this case, the preceding statement is eq uivalent to the following statement: SELECT src.key1 AS key1, src.key2 AS key2, src.a1, src.a2, src2.b1, src2.b2 FROM src INNER JOIN src2 ON src.k ey1 = src2.key1 AND src.key2 = src2.key2;
```

Implicit JOIN operation: A JOIN operation that is performed without the need to specify the JOIN keyword.

```
SELECT * FROM table1, table2 WHERE table1.id = table2.id; -- The preceding statement is equivalent to the following statement: SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;
```

Join conditions: You must use equi-joins and combine conditions by using AND. You can use non-equi joins or combine multiple conditions by using OR in a MAPJOIN operation.

```
-- MaxCompute supports multiple JOIN operations in an SQL statement. SELECT a. * FROM shop a FULL OUTER JOIN sale_detail b ON a.shop_name=b.shop_name
        FULL OUTER JOIN sale_detail c ON a.shop_name=c.shop_name;
-- MaxCompute does not support non-equi joins and returns an error. SELECT a. * FROM shop a JOIN sale_detail b ON a.shop_name ! = b.shop_name;
```

You can use parentheses () to specify the priority of JOIN operations. The JOIN operation enclosed in parentheses () has a high priority.

```
SELECT * FROM src JOIN (src2 JOIN src3 on xxx) ON yyy; -- In the preceding statement, src2 JOIN src3 is first executed. Then, the JOIN operation is performed for the src table and the result of the first JOIN operation.
```

The test_table_a and test_table_b tables are available. You want to query the two tables for the rows whose values in the **origin** column are equal to those in the **id** column and whose data timestamp is greater than 20180101. If you use LEFT JOIN, all rows in the left table test_table_a are returned.

```
SELECT s.id
    ,s.name
    ,s.origin
    ,d.value
FROM (SELECT * FROM test_table_a WHERE ds > "20180101" ) s LEFT JOIN (SELECT * FROM test_table_b WHERE ds > "20180101") d ON s.origin = d.id;
```

##### 3.5.2.5 MAPJOIN hint

This topic describes how to specify MAPJOIN in a SELECT statement to join a large table with one or more small tables. You can explicitly specify MAPJOIN in a SELECT statement to join a large table with one or more small tables. MAPJOIN speeds up your query. A JOIN operation contains three stages: map, shuffle, and reduce. In most cases, tables are joined in the reduce stage. MAPJOIN joins tables in the map stage instead of the reduce stage. This reduces data transmission time and system resource consumption and optimizes jobs. In the map stage, MAPJOIN loads all data in the specified tables into the memory of the program that executes the JOIN operation. The tables specified for MAPJOIN must be small tables, and the total memory occupied by the table data cannot exceed 512 MB. When a large table is joined with one or more small tables, MAPJOIN loads all data in the specified small tables into the memory of the program that executes the JOIN operation. This way, tables are connected in the map stage to accelerate the execution of the JOIN operation.

**Usage**

To use MAPJOIN, you must specify the hint `/*+ MAPJOIN(table) */` in a SELECT statement. For example, sale_detail is a large table whose alias is b, and shop is a small table whose alias is a. The following statement is used to perform a common JOIN operation:

```
SELECT a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

The following statement is used to perform a JOIN operation with MAPJOIN specified:

```
SELECT /* + MAPJOIN(a) */
        a.shop_name,
        b.customer_id,
        b.total_price
FROM shop a JOIN sale_detail b ON a.shop_name = b.shop_name;
```

When you use MAPJOIN and reference a small table or a subquery, you must reference the alias of the table or subquery. MAPJOIN supports small tables in subqueries. The left table in a LEFT OUTER JOIN operation must be a large table. The right table in a RIGHT OUTER JOIN operation must be a large table. Either the left or right table in an INNER JOIN operation can be a large table. MAPJOIN cannot be used in a FULL OUTER JOIN operation. For MAPJOIN, you can use non-equi joins or combine conditions by using OR. You can leave the ON condition unspecified or use `MAPJOIN ON 1 = 1` , such as `SELECT /* + MAPJOIN(a) */ a.id FROM shop a JOIN table_name b ON` `1=1` , to calculate the Cartesian product. However, this calculation method may increase the data amount. MaxCompute allows you to specify a maximum of 128 small tables for MAPJOIN. If you specify more than 128 small tables, a syntax error is returned. Separate small tables with commas (,), such as `/*+MAPJOIN(a,b,c)*/` . The total memory occupied by small tables cannot exceed 512 MB. MaxCompute compresses your data before storage. As a result, the data amount of small tables sharply increases after they are loaded into the memory. 512 MB indicates the maximum data amount after small tables are loaded into the memory. In a MaxCompute SQL statement, you cannot use complex join conditions, such as non-equi joins or the OR logical operator, in the ON condition for a common JOIN operation. However, you can use them for a JOIN operation with MAPJOIN specified.

```
SELECT /* + MAPJOIN(a) */
        a.total_price,
        b.total_price
FROM shop a JOIN sale_detail b ON a.total_price < b.total_price OR a.total_price + b.total_price < 500;
```

##### 3.5.2.6 SELECT TRANSFORM

###### 3.5.2.6.1 Overview

This topic describes the syntax of the SELECT TRANSFORM statement in MaxCompute. The SELECT TRANSFORM statement allows you to start a specific child process and insert data in the required format into the child process by using standard input. Then, the SELECT TRANSFORM statement parses the standard output of the child process to obtain the output data. The SELECT TRANSFORM statement allows you to run scripts in other programming languages without the need to write user-defined functions (UDFs).

```
SELECT TRANSFORM(arg1, arg2 ...) (ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value)) USING 'unix_command_line' (RESOURCES 'res_name' (',' 'res_name')*) ( AS col1, col2 ...) (ROW FORMAT DELIMITED (FIELDS TERMINATED BY field_delimiter (ESCAPED BY character_escape)) (LINES SEPARATED BY line_separator) (NULL DEFINED AS null_value))
```

Parameters:
**SELECT TRANSFORM**: the keyword, which can be replaced with the **MAP** or **REDUCE** keyword. These keywords
have the same syntax. We recommend that you use **SELECT TRANSFORM** to make the syntax clearer.
**(arg1, arg2 ...)**: the input data. The data format is similar to that of the SELECT statement. In the default format,
the results of expressions for each parameter are implicitly converted into a value of the STRING type. Then, the parameters are combined by **\t** and passed to the specified child process. The format is configurable. For more information, see **ROW FORMAT**.
**USING**: the commands that are used to start a child process. Take note of the following points:
In most MaxCompute SQL statements, the USING clause specifies resources. However, in the SELECT TRANSFORM statement, the USING clause specifies the commands to start a child process. The USING clause is used to ensure compatibility with the Hive syntax. The syntax of the USING clause is similar to that of a shell script. However, instead of running the shell script, the USING clause creates a child process based on the input commands. Therefore, some shell features, such as input and output redirection, pipe, and loop, cannot be used. A shell script can be used as the commands to start a child process if necessary.
**RESOURCES**: the resources that the specified child process can access. You can use one of the following methods to
specify resources: Use the RESOURCES clause. Example: `using 'sh foo.sh bar.txt' resources 'foo.sh','bar.txt'` . Add the set odps.sql.session.resources=foo.sh,bar.txt; flag before SQL statements to specify resources. This is a global configuration. It allows all **SELECT TRANSFORM** statements to access the specified resources. Separate multiple resource files with commas (,).
**ROW FORMAT**: the input and output formats. The syntax includes two ROW FORMAT clauses. The first clause
specifies the format of the input data, and the second clause specifies the format of the output data. By default, **\t** is used as a column delimiter, **\n** is used as a row delimiter, and **\N** is used to represent NULL values. For field_delimiter, character_escape, and line_separator, only one character is accepted. If you specify a string, the first character in the string takes priority over the others. MaxCompute supports syntax in the formats that are specified by Hive, such as **inputRecordReader**,
**outputRecordReader**, and **SerDe**. You must enable the Hive-compatible mode to use the syntax. To
enable the Hive-compatible mode, add set odps.sql.hive.compatible=true; before SQL statements. If you specify the syntax that is supported by Hive, such as **inputRecordReader** and
**outputRecordReader**, the performance of SQL queries may deteriorate.
**AS**: the output columns.
If you do not specify the data types for output columns, the STRING type is used. The output data is obtained after the standard output of the child process is parsed. If the data is not of the STRING type, the system implicitly calls the CAST function to convert the data into the STRING type. Exceptions may occur during the conversion process. You must specify data types for all output columns. If you omit the AS keyword, the field before the first **\t** in the standard output data is the key and all the following parts are values. This is equivalent to **AS(key, value)**.

###### 3.5.2.6.2 SELECT TRANSFORM examples

###### 3.5.2.6.2.1 Call shell scripts

This topic describes how to use SELECT TRANSFORM to call shell scripts and provides examples. Assume that you use a shell script to generate 50 rows of data. The values are from 1 to 50. The following code shows the output of the data field:

```
SELECT TRANSFORM(script) USING 'sh' AS (data) FROM (
            SELECT  'for i in `seq 1 50`; do echo $i; done' AS script
        ) t
```

; You can use shell commands as the input for SELECT TRANSFORM. SELECT TRANSFORM allows you to use the scripts of multiple programming languages, such as AWK, Python, Perl, and shell, as the input to implement simple features. You do not need to compile script files or upload resources, which simplifies development. You can upload a script to implement complex features. For more information, see Call Python scripts.

###### 3.5.2.6.2.2 Call Python scripts

This topic describes how to use SELECT TRANSFORM to call Python scripts and provides examples.
1. Compile a Python script file. In this example, the file name is myplus.py.

```java
#! /usr/bin/env python
import sys line = sys.stdin.readline() while line:
    token = line.split('\t')
    if (token[0] == '\\N') or (token[1] == '\\N'):
        print '\\N'
    else:
        print str(token[0]) +'\t' + str(token[1])
    line = sys.stdin.readline()
```

2. Add the Python script file as a resource to MaxCompute.

```
add py ./myplus.py -f;
```

3. Execute SELECT TRANSFORM to call the resource.

```
-- Create a test table. CREATE TABLE testdata(c1 bigint,c2 bigint); -- Insert test data into the test table. INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); -- Execute the following statement: TRANSFORM (testdata.c1, testdata.c2) USING 'python myplus.py'resources 'myplus.py' AS (result1,result2) FROM testdata; -- The preceding statement is equivalent to the following statement: set odps.sql.session.resources=myplus.py; SELECT TRANSFORM (testdata.c1, testdata.c2) USING 'python myplus.py' AS (result1,result2) FROM testdata;
```

In MaxCompute, you can use Python scripts as the input for SELECT TRANSFORM. For example, you can run Python commands to call shell scripts.

```
SELECT TRANSFORM('for i in xrange(1, 50): print i;') USING 'python' AS (data);
```

The following result is returned:

```
+------------+------------+
| result1    | result2    |
+------------+------------+
| 1          | 4          |
|            | NULL       |
| 2          | 5          |
|            | NULL       |
| 3          | 6          |
|            | NULL       |
+------------+------------+
```

###### 3.5.2.6.2.3 Call Java scripts

This topic describes how to use SELECT TRANSFORM to call Java scripts and provides examples. Java scripts are called in a similar way to Python scripts. In this example, you must prepare a Java script file, export it as a JAR package, and then execute the `ADD FILE` statement to add the JAR package as a resource to MaxCompute. Then, the resource can be called by using SELECT TRANSFORM.
1. Prepare a Java script file and export it as a JAR package. In this example, the name of the JAR package is Sum.jar.
Sample code:

```java
package com.aliyun.odps.test; import java.util.Scanner public class Sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            String s = sc.nextLine();
            String[] tokens = s.split("\t");
            if (tokens.length < 2) {
                throw new RuntimeException("illegal input");
```

`}`

```java
            if (tokens[0].equals("\\N") || tokens[1].equals("\\N")) {
                System.out.println("\\N");
```

`}`

```java
            System.out.println(Long.parseLong(tokens[0]) + Long.parseLong(tokens[1]));
```

`}` `}` `}`
2. Add the JAR package as a resource to MaxCompute.

```
add jar . /Sum.jar -f;
```

3. Execute the SELECT TRANSFORM statement to call the resource.

```
-- Create a test table. CREATE TABLE testdata(c1 bigint,c2 bigint); -- Insert test data into the test table. INSERT INTO TABLE testdata VALUES (1,4),(2,5),(3,6); -- Execute the SELECT TRANSFORM statement. SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' resources 'Sum.jar' FROM testdata; -- The preceding statement is equivalent to the following statement: set odps.sql.session.resources=Sum.jar; SELECT TRANSFORM(testdata.c1, testdata.c2) USING 'java -cp Sum.jar com.aliyun.odps.test.Sum' FROM testdata;
```

The following result is returned:

```
+-----+
| cnt |
+-----+
| 5   |
| 7   |
| 9   |
+-----+
```

You can use the preceding method to run most Java utilities. Although UDTF frameworks are provided for Java and Python, SELECT TRANSFORM makes it easier to compile code. SELECT TRANSFORM is a simpler process because it is not subject to dependencies or format requirements and can be called offline. The paths for Java and Python offline scripts can be obtained from the JAVA_HOME and PYTHON_HOME environment variables.

###### 3.5.2.6.2.4 Call the scripts of other programming languages

This topic describes how to use SELECT TRANSFORM to call the scripts of other programming languages and provides examples. SELECT TRANSFORM supports the programming languages described in the preceding topics. It also supports commonly used UNIX commands and script interpreters, such as AWK and Perl interpreters. Example on how to call an AWK script to display the second column:

```
SELECT TRANSFORM(*) USING "awk '//{print $2}'" as (data) from testdata;
```

Example on how to call a Perl script:

```
SELECT TRANSFORM (testdata.c1, testdata.c2) USING "perl -e 'WHILE($input = <STDIN>){print $input;}'" FROM testdata;
```

PHP and Ruby are not deployed in MaxCompute compute clusters. Therefore, you cannot call PHP or Ruby scripts in MaxCompute.

###### 3.5.2.6.2.5 Call scripts in series

This topic describes how to use SELECT TRANSFORM to call scripts in series and provides examples. SELECT TRANSFORM allows you to call scripts in series. For example, you can use DISTRIBUTE BY and SORT BY to preprocess data.

```
SELECT TRANSFORM(key, value) USING 'cmd2' FROM
```

`(`

```
    SELECT TRANSFORM(*) USINg 'cmd1' FROM
```

`(`

```
        SELECt * FROM data DISTRIBUTE BY col2 SORT BY col1
    ) t DISTRIBUTE BY key SORT BY value
) t2;
```

You can also use the MAP or REDUCE keyword to obtain the same results.

```
@a := select * from data distribute by col2 sort by col1; @b := map * using 'cmd1' distribute by col1 sort by col2 from @a; reduce * using 'cmd2' from @b;
```

###### 3.5.2.6.3 Performance

This topic describes the advantages of SELECT TRANSFORM and user-defined table-valued functions (UDTFs). The performance of SELECT TRANSFORM and UDTFs varies based on specific scenarios. In most cases, SELECT TRANSFORM performs better. However, UDTFs perform better as the data amount increases. SELECT TRANSFORM is more suitable for ad hoc data analytics because the development of SELECT TRANSFORM is easier. The following sections describe the advantages of UDTFs and SELECT TRANSFORM.

**Advantages of UDTFs**

For UDTFs, the input parameters and output results support multiple data types. For SELECT TRANSFORM, the child process transfers data based on the standard input and output and processes all data as the STRING type. Therefore, SELECT TRANSFORM requires one more step of data type conversions than UDTFs. For SELECT TRANSFORM, data transfer depends on the operating system pipe. The pipe has only a 4 KB cache that cannot be specified. If the operating system pipe is empty or fully occupied, SELECT TRANSFORM cannot respond. For UDTFs, the constant parameters do not need to be transferred. However, SELECT TRANSFORM does not support this feature.

**Advantages of SELECT TRANSFORM**

SELECT TRANSFORM supports two processes: parent and child processes. UDTFs support only a single process. If the usage of computing resources is high and the data throughput is low, SELECT TRANSFORM can take advantage of the multi-core feature of the server. SELECT TRANSFORM calls underlying systems to read and write data during data transfer. This allows SELECT TRANSFORM to provide better performance in data transfer than Java programs. SELECT TRANSFORM supports the native code of tools such as AWK. This allows SELECT TRANSFORM to deliver more performance benefits than Java programs.

##### 3.5.2.7 GROUPING SETS

###### 3.5.2.7.1 Overview

This topic describes GROUPING SETS in MaxCompute. In some cases, you must execute the UNION ALL clause multiple times to aggregate and analyze data from multiple dimensions. For example, you want to aggregate Column A, aggregate Column B, and then aggregate Column A and Column B. The GROUPING SETS clause is a better choice in these cases. GROUPING SETS is an extension to the GROUP BY clause in a SELECT statement. GROUPING SETS allows you to group results by using various methods without the need to execute multiple SELECT statements. This allows the MaxCompute engine to generate more efficient execution plans with high performance. Most examples in this topic are demonstrated by using MaxCompute Studio. We recommend that you install MaxCompute Studio before you proceed with subsequent operations. For more information, see MaxCompute Studio.

###### 3.5.2.7.2 Example

This topic provides an example on how to execute the GROUPING SETS statement. Example:
1. Prepare data.

```
create table requests LIFECYCLE 20 as select * from values
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city);
```

2. Execute the GROUPING SETS statement.

```
SELECT os,device, city ,COUNT(*) FROM requests GROUP BY os, device, city GROUPING SETS((os, device), (city), ());
```

The following result is returned:

```
+----+--------+------+------------+
| os | device | city | cnt        |
+----+--------+------+------------+
| NULL | NULL   | NULL | 7          |
| NULL | NULL   | Beijing | 4          |
| NULL | NULL   | Shijiazhuang | 3          |
| ios | Phone  | NULL | 1          |
| linux | PC     | NULL | 1          |
| linux | Phone  | NULL | 1          |
| windows | PC     | NULL | 3          |
| windows | Phone  | NULL | 1          |
+----+--------+------+------------+
```

You can also execute multiple SELECT statements to obtain the same result.

```
SELECT NULL, NULL, NULL, COUNT(*) FROM requests SELECT os, device, NULL, COUNT(*) FROM requests GROUP BY os, device SELECT null, null, city, COUNT(*) FROM requests GROUP BY city;
```

However, the execution of GROUPING SETS is simpler and more efficient. NULL is used as placeholders for the expressions that are not used in GROUPING SETS. This way, you can perform UNION operations on the result sets.

###### 3.5.2.7.3 CUBE and ROLLUP

This topic describes the CUBE and ROLLUP functions for GROUPING SETS. CUBE and ROLLUP are special GROUPING SETS functions. CUBE lists all the possible combinations of specific columns as grouping sets. ROLLUP aggregates data by level to generate grouping sets.

```
GROUP BY CUBE(a, b, c) -- Equivalent to the following statement: GROUPING SETS((a,b,c),(a,b),(a,c),(b,c),(a),(b),(c),()) GROUP BY ROLLUP(a, b, c) -- Equivalent to the following statement: GROUPING SETS((a,b,c),(a,b),(a), ()) GROUP BY CUBE ( (a, b), (c, d) ) -- Equivalent to the following statement: GROUPING SETS (
    ( a, b, c, d ),
    ( a, b       ),
    (       c, d ),
    (            )
```

`)`

```
GROUP BY ROLLUP ( a, (b, c), d ) -- Equivalent to the following statement: GROUPING SETS (
    ( a, b, c, d ),
    ( a, b, c    ),
    ( a          ),
    (            )
```

`)`

```
GROUP BY a, CUBE (b, c), GROUPING SETS ((d), (e)) -- Equivalent to the following statement: GROUP BY GROUPING SETS (
    (a, b, c, d), (a, b, c, e),
    (a, b, d),    (a, b, e),
    (a, c, d),    (a, c, e),
    (a, d),       (a, e)
```

`)`

```
GROUP BY grouping sets((b), (c),rollup(a,b,c)) -- Equivalent to the following statement: GROUP BY GROUPING SETS (
    (b), (c),
    (a,b,c), (a,b), (a), ()
```

`)`

###### 3.5.2.7.4 GROUPING and GROUPING_ID

This topic describes the GROUPING and GROUPING_ID functions in GROUPING SETS. NULL is used as placeholders in the results of GROUPING SETS. As a result, the NULL placeholders cannot be distinguished from the NULL values. To address this issue, MaxCompute provides the GROUPING function. GROUPING allows you to specify the name of a column as a parameter. If specific rows are aggregated based on the column specified in the GROUPING function, 0 is returned, which indicates that NULL is an input value. Otherwise, 1 is returned, which indicates that NULL is a placeholder in GROUPING SETS. GROUPING_ID allows you to specify the names of one or more columns as parameters. The GROUPING results of these columns are formed into integers by using bitmap.

```
SELECT a,b,c ,COUNT(*), GROUPING(a) ga, GROUPING(b) gb, GROUPING(c) gc, GROUPING_ID(a,b,c) groupingid FROM VALUES (1,2,3) as t(a,b,c) GROUP BY CUBE(a,b,c);
```

The following result is returned:

```
+------------+------------+------------+------------+------------+------------+------------+------------+
| a          | b          | c          | _c3        | ga         | gb         | gc         | groupingid |
+------------+------------+------------+------------+------------+------------+------------+------------+
| NULL       | NULL       | NULL       | 1          | 1          | 1          | 1          | 7          |
| NULL       | NULL       | 3          | 1          | 1          | 1          | 0          | 6          |
| NULL       | 2          | NULL       | 1          | 1          | 0          | 1          | 5          |
| NULL       | 2          | 3          | 1          | 1          | 0          | 0          | 4          |
| 1          | NULL       | NULL       | 1          | 0          | 1          | 1          | 3          |
| 1          | NULL       | 3          | 1          | 0          | 1          | 0          | 2          |
| 1          | 2          | NULL       | 1          | 0          | 0          | 1          | 1          |
| 1          | 2          | 3          | 1          | 0          | 0          | 0          | 0          |
+------------+------------+------------+------------+------------+------------+------------+------------+
```

By default, the columns that are not used in the GROUP BY clause are filled with NULL. You can use the GROUPING function to obtain more useful data.

```
-- Prepare table data. create table requests lifecycle 20 as select * from values
    (1, 'windows', 'PC', 'Beijing'),
    (2, 'windows', 'PC', 'Shijiazhuang'),
    (3, 'linux', 'Phone', 'Beijing'),
    (4, 'windows', 'PC', 'Beijing'),
    (5, 'ios', 'Phone', 'Shijiazhuang'),
    (6, 'linux', 'PC', 'Beijing'),
    (7, 'windows', 'Phone', 'Shijiazhuang')
as t(id, os, device, city); -- Sample code
  if(grouping(os) == 0, os, 'ALL') as os,
  if(grouping(device) == 0, device, 'ALL') as device,
  if(grouping(city) == 0, city, 'ALL') as city,
  count(*) as count
from requests group by os, device, city grouping sets((os, device), (city), ());
```

The following result is returned:

```
+------------+------------+------------+------------+
| os         | device     | city       | count      |
+------------+------------+------------+------------+
| ALL        | ALL        | ALL        | 7          |
| ALL        | ALL        | Beijing    | 4          |
| ALL        | ALL        | Shijiazhuang | 3          |
| ios        | Phone      | ALL        | 1          |
| linux      | PC         | ALL        | 1          |
| linux      | Phone      | ALL        | 1          |
| windows    | PC         | ALL        | 3          |
| windows    | Phone      | ALL        | 1          |
+------------+------------+------------+------------+
```

##### 3.5.2.8 UNION, INTERSECT, and EXCEPT

This topic describes the SQL statements that use the UNION, INTERSECT, and EXCEPT set operators, such as UNION, UNION ALL, UNION DISTINCT, INTERSECT, INTERSECT ALL, INTERSECT DISTINCT, EXCEPT, EXCEPT ALL, and EXCEPT DISTINCT.

```
select_statement UNION ALL select_statement; select_statement UNION [DISTINCT] select_statement; select_statement INTERSECT ALL select_statement; select_statement INTERSECT [DISTINCT] select_statement; select_statement EXCEPT ALL select_statement; select_statement EXCEPT [DISTINCT] select_statement; select_statement MINUS ALL select_statement; select_statement MINUS [DISTINCT] select_statement;
```

Parameters: UNION: the union of two datasets. The UNION operation combines two datasets into one dataset. INTERSECT: the intersection of two datasets. The INTERSECT operation returns the records contained in both datasets. EXCEPT: the complement of the second dataset in the first dataset. The EXCEPT operation returns the records that are contained in the first dataset, but not in the second dataset. MINUS: equivalent to EXCEPT. UNION: If UNION ALL is used, all records of the two datasets are returned.

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4) t(a, b) SELECT * FROM VALUES (1, 2), (1, 4) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

If multiple UNION ALL clauses are used, parentheses can be used to prioritize the clauses.

```
SELECT * FROM src UNION ALL (SELECT * FROM src2 UNION ALL SELECT * FROM src3);
```

If UNION is used, duplicate records are not included in the returned records. UNION is equivalent to UNION DISTINCT.

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4) t(a, b) UNION SELECT * FROM VALUES (1, 2), (1, 4) t(a, b); -- The preceding statement is equivalent to the following statement: SELECT DISTINCT * FROM (<Result of UNION ALL>)t;
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 4          |
| 3          | 4          |
+------------+------------+
```

Assume that UNION is followed by a CLUSTER BY, DISTRIBUTE BY, SORT BY, ORDER BY, or LIMIT clause. If `set` odps.sql.type.system.odps2=false; is used, the clause works on the result of the last **select_statement** after the

| odps.sql.type.system.odps2=false; |   |
|---|---|
| UNION operator. If | odps.sql.type.system.odps2=true; |

operations.

```
set odps.sql.type.system.odps2=true; SELECT explode(array(3, 1)) AS (a) UNION ALL SELECT explode(array(0, 4, 2)) AS (a) ORDER BY a LIMIT 3;
```

The following result is returned:

```
+------+
| a    |
+------+
| 0    |
| 1    |
| 2    |
+------+
```

INTERSECT: INTERSECT ALL:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 6) t(a, b) INTERSECT ALL SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

INTERSECT DISTINCT:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 6) t(a, b) INTERSECT DISTINCT SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (5, 7) t(a, b);
```

The following result is returned. The preceding statement is equivalent to the `SELECT DISTINCT * FROM (< Result of` INTERSECT ALL >) t; statement.

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 3          | 4          |
+------------+------------+
```

EXCEPT: EXCEPT ALL:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (3, 4), (5, 6), (7, 8) t(a, b) EXCEPT ALL SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b);
```

The following result is returned:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 1          | 2          |
| 3          | 4          |
| 7          | 8          |
+------------+------------+
```

EXCEPT DISTINCT:

```
SELECT * FROM VALUES (1, 2), (1, 2), (3, 4), (3, 4), (5, 6), (7, 8) t(a, b) EXCEPT SELECT * FROM VALUES (3, 4), (5, 6), (5, 6), (9, 10) t(a, b);
```

The following result is returned. The preceding statement is equivalent to the `SELECT DISTINCT * FROM left_branch` EXCEPT ALL SELECT DISTINCT * FROM right_branch; statement.

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
| 7          | 8          |
+------------+------------+
```

Set operations do not necessarily return sorted results. The two branches for a set operation must have the same number of output columns with consistent data types. If data types are inconsistent, implicit conversion of the data types may be performed. To ensure compatibility for set operations, MaxCompute forbids the implicit conversion between STRING and other data types. MaxCompute supports a maximum of 256 branches for a set operation. If the limit is exceeded, an error is returned.

#### 3.5.3 EXPLAIN

This topic describes the EXPLAIN statement in MaxCompute SQL. This statement shows the structure of the execution plan of a DML statement. An execution plan is a program that executes SQL statements.

```
EXPLAIN <DML query>;
```

The execution results of an EXPLAIN statement include: Dependencies among all the jobs of this DML statement Dependencies among all the tasks of each job Dependencies among all operators in a task

```
SELECT abs(a.key), b.value FROM src a JOIN src1 b ON a.value = b.value;
```

The output of the EXPLAIN statement consists of the following three parts: Job dependencies: `job0 is root job` . This query requires only one **job (job0)**. Therefore, only one row of information is displayed. Task dependencies. Example:

```
In Job job0: root Tasks: M1_Stg1, M2_Stg1 J3_1_2_Stg1 depends on: M1_Stg1, M2_Stg1
```

Job0 contains three tasks, M1_Stg1, M2_Stg1, and J3_1_2_Stg1. J3_1_2_Stg1 is executed after the M1_Stg1 and M2_Stg1 tasks are complete. Naming conventions for a task: MaxCompute provides the task types of map, reduce, join, and local work. The first letter in a task name indicates the type of the task. For example, M2Stg1 is a map task. The number following the first letter indicates the task ID. This ID is unique among all tasks that correspond to the current query. Digits that are combined by underscores (_) indicate the task dependencies. For example, J3_1_2_Stg1 indicates that the current task with the ID of 3 depends on two tasks whose IDs are 1 and 2. Operator structure, where each operator string describes the execution semantics of a task.

```
In Task M1_Stg1:
  Data source: yudi_2.src                       # Data source describes the input of the task.
  TS: alias: a                                  # TableScanOperator
      RS: order: +                              # ReduceSinkOperator
          keys:
               a.value
          values:
               a.key
          partitions:
               a.value
In Task J3_1_2_Stg1:
  JOIN: a INNER JOIN b                          # JoinOperator
      SEL: Abs(UDFToDouble(a._col0)), b._col5   # SelectOperator
          FS: output: None                      # FileSinkOperator
In Task M2_Stg1:
  Data source: yudi_2.src1
  TS: alias: b
      RS: order: +
          keys:
               b.value
          values:
               b.value
          partitions:
               b.value
```

The following table describes the operators.

| Operator | Description |
|---|---|
| TableScanOperator | Describes the logic of FROM statement blocks in a query statement. The alias of the input table is displayed in the EXPLAIN results. |
| SelectOperator | Describes the logic of SELECT statement blocks in a query statement. The columns that are transferred to the next operator are displayed in the EXPLAIN results. Separate multiple columns with commas (,). If columns are referenced, the value is in the < alias >.< column name > _ format. If the result of an expression is transferred, the value is displayed as a function, such as func1(arg1 1, arg1 2, func2(arg2 1, arg2 2)). _ _ _ _ If constants are transferred, the value is immediately displayed. |
| FilterOperator | Describes the logic of WHERE statement blocks in a query statement. The EXPLAIN results include a WHERE clause, with the display rules that are similar to those of SelectOperator. |
| JoinOperator | Describes the logic of JOIN statement blocks in a query statement. The EXPLAIN results show which tables are joined in which way. |
| GroupByOperator | Describes the logic of aggregate operations. This operator is displayed if an aggregate function is used in a query. The content of the aggregate function is displayed in the EXPLAIN results. |
| ReduceSinkOperator | Describes the logic of data distribution between tasks. If the result of the current task is transferred to another task, ReduceSinkOperator must be used to distribute data at the last stage of the current task. The sorting method of output data records, the distributed keys and values, and the columns used to calculate the hash value are displayed in the EXPLAIN results. |
| FileSinkOperator | Describes the logic of storage operations on final data records. If an INSERT statement block exists in a query, the name of the required table is displayed in the EXPLAIN results. |
| LimitOperator | Describes the logic of LIMIT statement blocks in a query statement. The number of records specified by LIMIT is displayed in the EXPLAIN results. |
| MapjoinOperator | Describes JOIN operations on large tables. This operator is similar to JoinOperator. |

If a query statement is complex, the EXPLAIN statement returns excessive results. As a result, API limits are reached and complete results cannot be obtained. In this case, you can split a query and execute the EXPLAIN statement on each subquery to understand the structure of the job. If you specify more than 10,000 partitions in a query, large amounts of source data needs to be read. To circumvent this limit, you can add filter conditions in the query to filter out most partitions.

#### 3.5.4 IF statement

This topic describes the IF statement that MaxCompute SQL supports. MaxCompute SQL supports the IF-ELSE statement. You can use the IF-ELSE statement to execute SQL scripts with specific conditions. A condition in the IF-ELSE statement can be a standard variable or a scalar subquery that returns only one column value from one row. The IF statement allows the system to automatically select the execution logic based on the specified conditions. MaxCompute supports the following IF syntax:

```
IF (condition) BEGIN
  statement 1
  statement 2
  ...
END IF (condition) BEGIN
  statements
END ELSE IF (condition2) BEGIN
  statements
END ELSE BEGIN
  statements
END
```

The BEGIN and END conditional clause can be omitted if it contains only one statement, similar to '{ }' in Java. The IF statement can contain two types of conditions: expressions and scalar subqueries. Both of them are of the BOOLEAN type. Expressions: A BOOLEAN-type expression in the IF-ELSE statement determines which branch is executed at the compiling stage. Example:

```
@date := '20190101'; @row TABLE(id STRING); -- Declare the row variable. The type of the row is Table and schema is STRING. IF ( cast(@date as bigint) % 2 == 0 ) BEGIN @row := SELECT id from src1; END ELSE BEGIN @row := SELECT id from src2; END INSERT OVERWRITE TABLE dest SELECT * FROM @row;
```

Scalar subqueries: A BOOLEAN-type scalar subquery in the IF-ELSE statement determines which branch is executed at the running stage. Therefore, you must submit multiple jobs. Example:

```
@i bigint; @t table(id bigint, value bigint); IF ((SELECT count(*) FROM src WHERE a = '5') > 1) BEGIN @i := 1; @t := select @i, @i*2; END ELSE BEGIN @i := 2; @t := select @i, @i*2; END select id, value from @t;
```

#### 3.5.5 UPDATE and DELETE

This topic describes the UPDATE and DELETE statements in MaxCompute SQL. The UPDATE and DELETE statements are used to manage data of specific rows in tables or partitions. MaxCompute data manipulation language (DML) statements have limits on table operations. MaxCompute allows you to use only the INSERT OVERWRITE and INSERT INTO statements to delete and update some rows in a table. For example, if you use an INSERT statement to modify small amounts of data in a table or partition, you must use a SELECT statement to read all data and modify the data. Then, you can execute the INSERT statement to insert the modified data into the table or partition. This is a low-efficiency process. However, if you use the UPDATE and DELETE statements, the amount of data read or written in a query significantly decreases. History tables were considered the best to perform multiple UPDATE operations at a time. If you use a history table, you must add auxiliary columns, such as **start_date** and **end_date**, in the table. These columns indicate the lifecycle of the data records in a row. To query the current status of a table, you must find the latest status from large amounts of data based on the timestamp. This is a time-consuming process. However, the UPDATE and DELETE statements directly read data from the current table.

**Description**

When you execute a DELETE statement, the system automatically generates a Delta file. **txnid(bigint)** and
**rowid(bigint)** in the Delta file indicate which rows in which transactional table are deleted from the Base file.
The Delta file stores the row numbers that are used to indicate the deleted rows in the Base file. If you execute a DELETE statement again, another Delta file named f2.del is generated. The f2.del file also stores the row numbers based on the Base file. During data reading, all Delta files are queried and data that is not deleted is returned. Similarly, the UPDATE statement is converted into the combination of the DELETE and INSERT INTO statements. If jobs are run in parallel and the tables on which you want to perform operations are the same, conflicts may occur. For more information, see ACID semantics of MaxCompute concurrent write jobs.

**Precautions**

The UPDATE and DELETE operations must be performed based on transactional tables. For more information about how to create a transactional table, see Create a table. When you execute an UPDATE statement, you must add set odps.service.mode=off; before the statement and commit them at the same time. If the ratio of the rows that you want to delete or update to all rows is small, the performance of the data that is read from a table is slightly affected. In this case, we recommend that you use the UPDATE or DELETE statement. If the ratio is less than 5%, we recommend that you use the UPDATE or DELETE statement. The maximum ratio varies based on your business scenarios. If you perform the UPDATE or DELETE operation multiple times to update or delete a small number of rows in a table, we recommend that you execute the COMPACT statement after the UPDATE and DELETE statements. This reduces the storage usage of the table. If you perform less UPDATE or DELETE operations to update or delete a large number of rows in a table and will frequently read data from the table, we recommend that you use the INSERT OVERWRITE and INSERT INTO statements. For example, a total of 10% of the data in a table needs to be updated or deleted ten times a day. In this case, we recommend that you evaluate the sum of the costs of the UPDATE or DELETE statement and the read performance consumption based on the generated Delta file. Then, compare it with that of the INSERT OVERWRITE and INSERT INTO statements to select an efficient method. After you delete data, a Delta file is generated. As a result, the storage resources may not be released. If you want to use the DELETE statement to delete data and release the storage resources, you can use the ALTER TABLE COMPACT statement to merge the Base files with Delta files. If you use the ALTER TABLE COMPACT statement in MaxCompute SQL mode of DataWorks, a compatibility issue occurs. To handle this issue, we recommend that you use the MaxCompute client whose version must be 0.35.0. You can specify the transactional attribute for a table only when you create the table. However, you are not allowed to modify the transactional attribute of an existing table by using the ALTER TABLE COMPACT statement. If you modify the transactional attribute of an existing table, an error is returned.

```
alter table not_txn_tbl set tblproperties("transactional"="true"); -- FAILED is returned. Catalog Service Failed, Error Code: 151, Error Message: Set transactional is not supported.
```

You cannot specify clustered tables or external tables as transactional tables. Existing internal tables or external tables cannot be converted into transactional tables, and transactional tables cannot be converted into standard tables. Tasks from peripheral systems, such as Graph and Machine Learning Platform for AI (PAI), are not supported. If these tasks access a transactional table, an error is returned. CLONE TABLE, MERGE PARTITION, and incremental replication operations cannot be performed on transactional tables. Before you perform the UPDATE, DELETE, or INSERT OVERWRITE operation on data in transactional tables, make sure that you back up the data in advance. You must have the Select and Update permissions on a table to perform the UPDATE and DELETE operations.

**DELETE**

```
delete from <table_name> [WHERE where_condition];
```

Description: This statement is used to delete some rows from a table. The following examples are provided: Example 1: Delete some rows from a table.

```
-- Create a transactional table. create table if not exists acid_delete(id bigint) tblproperties ("transactional"="true"); -- Insert data into the table. insert overwrite table acid_delete values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_delete;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+ -- Delete the row whose id value is 2. You must enter Yes or No to confirm the operation in the MaxCompute clie nt. delete from acid_delete where id = 2; -- Read data from the table. Only the rows whose id values are 1 and 3 are retained in the table. select * from acid_delete;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 3          |
+------------+
```

Example 2: Delete some rows from a partitioned table.

```
-- Create a transactional table. create table if not exists acid_delete_pt(id bigint) partitioned by(ds string) tblproperties ("transactional"="true"); -- Add partitions to the table. alter table acid_delete_pt add if not exists partition (ds= '2019'); -- Insert data into the partitions. insert overwrite table acid_delete_pt partition (ds='2019') values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_delete_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+
```

```
-- Delete data from the partitions. You must enter Yes or No to confirm the operation in the MaxCompute client. delete from acid_delete_pt where ds='2019' and id= 2; -- Read data from the table. Only the rows whose id values are 1 and 3 are retained in the table. select * from acid_delete_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

**UPDATE**

```
update <table_name> set col1 = value1 [, col2 = value2 ...] [WHERE where_condition]; update <table_name> set (col1 [, col2 ...]) = (value1 [, value2 ...]);
```

Description: This statement is used to update some rows in a table. The UPDATE statement is converted into the combination of the DELETE and INSERT INTO statements to update some rows. The following examples are provided: Example 1: Update some rows in a table.

```
-- Create a transactional table. create table if not exists acid_update(id bigint) tblproperties ("transactional"="true"); -- Insert data into the table. insert overwrite table acid_update values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_update;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 1          |
| 2          |
| 3          |
+------------+ -- Update the value 2 in the id column to 4. set odps.service.mode=off; update acid_update set id = 4 where id = 2; -- Query the table to check whether the value 2 is updated to 4 in the id column. select * from acid_update;
```

The following result is returned:

```
+------------+
| id         |
+------------+
| 4          |
| 1          |
| 3          |
+------------+
```

Example 2: Update some rows in a partitioned table.

```
-- Create a transactional table. create table if not exists acid_update_pt(id bigint) partitioned by(ds string) tblproperties ("transactional"="true");-- Add a partition. -- Add partitions to the table. alter table acid_update_pt add if not exists partition (ds= '2019'); -- Insert data into the partitions. insert overwrite table acid_update_pt partition (ds='2019') values(1),(2),(3); -- Query the table to check whether data is inserted. select * from acid_update_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 1     | 2019   |
| 2     | 2019   |
| 3     | 2019   |
+-------+--------+ -- Update the id values of rows in partition 2019 to 4. The rows must have the id values of 2. set odps.service.mode=off; update acid_update_pt set id = 4 where ds = '2019' and id = 2; -- Query the table to check whether the value 2 is updated to 4 in the id column. select * from acid_update_pt where ds = '2019';
```

The following result is returned:

```
+-------+--------+
| id    | ds     |
+-------+--------+
| 4     | 2019   |
| 1     | 2019   |
| 3     | 2019   |
+-------+--------+
```

Example 3: Update several columns and update a destination table by using the data in a source table.

```
-- Create a destination table named acid_update_t and create a table named acid_update_s for joins. create table if not exists acid_update_t(id bigint,value1 bigint,value2 bigint) tblproperties ("transactional"="true"); create table if not exists acid_update_s(id bigint,value1 bigint,value2 bigint); -- Insert data into these tables. insert overwrite table acid_update_t values(2,20,21),(3,30,31),(4,40,41); insert overwrite table acid_update_s values(1,100,101),(2,200,201),(3,300,301); -- Use constants to update the acid_update_t table. set odps.service.mode=off; update acid_update_t set (value1, value2) = (3, 4); -- Use the data in the acid_update_s table to update the acid_update_t table. Left join the acid_update_t table with the acid_update_s table. If you want to update only the intersection of the two tables, you must add a WHE RE clause to the update <table_name> statement. set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s where acid_update_t.id = acid_update_s.id); -- Use the data in the acid_update_s table to update the acid_update_t table. Add filter conditions for the aci d_update_t table to update only the intersection of the two tables. set odps.service.mode=off; update acid_update_t set (value1, value2) = (select value1, value2 from acid_update_s where acid_update_t.id = acid_update_s.id) where acid_update_t.id in (select id from acid_update_s); -- Use the aggregate results of the acid_update_t and acid_update_s tables to update the acid_update_t table. set odps.service.mode=off; update acid_update_t set (id, value1, value2) = (select id, max(value1),max(value2) from acid_update_s where ac id_update_t.id = acid_update_s.id group by acid_update_s.id) where acid_update_t.id in (select id from acid_update_s);
```

**MERGE INTO**

The MERGE INTO statement encapsulates the INSERT, UPDATE, and DELETE operations. You can use this statement to perform multiple operations on a destination table after the table is joined with a source table. MaxCompute DML provides the UPDATE and DELETE statements to enrich its expressions. However, if you want to use several INSERT, UPDATE, and DELETE statements to perform multiple UPDATE operations on a destination table at a time, you must execute several statements. These statements trigger multiple full table scans. The MERGE INTO statement requires only one full table scan for you to complete the operations. The MERGE INTO statement is more efficient than the INSERT, UPDATE, and DELETE statements. If you use the INSERT, UPDATE, and DELETE statements in a job to update a table, the update succeeds only when all the statements are successfully executed. If only some of these statements are successfully executed, the execution cannot be rolled back. However, the MERGE INTO statement is atomic, which can be used to prevent this issue.

```
MERGE INTO <target table> AS T USING <source expression/table> AS S ON <boolean expression1> WHEN MATCHED [AND <boolean expression2>] THEN UPDATE SET <set clause list> WHEN MATCHED [AND <boolean expression3>] THEN DELETE WHEN NOT MATCHED [AND <boolean expression4>] THEN INSERT VALUES <value list>
```

Description: This statement is used to update or insert data from the **source expression or table** into the
**destination table**. This statement is also used to delete data from the source expression or table from the
destination table. Parameters:
**source expression/table**: the source table. The value of this parameter can be a table, view, or subquery.
**target table**: the destination table, which must be an existing physical table.
**ON**: the clause that is used to determine whether the source table is joined with the destination table. **boolean**
**expression** specifies the join condition.
**WHEN MATCHED…THEN**: specifies the action when the **ON** clause determines that the two tables are joined. Data
obtained from multiple **WHEN MATCHED [AND <boolean expression>]** clauses must have no intersections. The MERGE INTO statement has clear objectives. You are not allowed to perform the INSERT or UPDATE operation on the same row in a single MERGE INTO statement. When you execute the MERGE INTO statement, make sure that the data in the source tables that meet the ON joint condition is unique. Otherwise, an error is returned. If a MERGE INTO statement has three WHEN clauses, the UPDATE, DELETE, and INSERT operations can appear at most once in each clause.
**WHEN NOT MATCHED** must be the last WHEN clause and can be used only for an INSERT operation.
If both the UPDATE and DELETE statements are included in a MERGE INTO statement, the statement that appears first must include **[AND <boolean expression>]**. The following example is provided: Prepare the test data.

```
-- Create a destination table. create table if not exists acid_address_book_base1 (id bigint,first_name string,last_name string,phone string) partitioned by(year string, month string, day string, hour string) tblproperties ("transactional"="true"); -- Create a source table. create table if not exists tmp_table1 (id bigint, first_name string, last_name string, phone string, _event_type_ string); -- Insert the test data into the destination table. insert overwrite table acid_address_book_base1 partition(year='2020', month='08', day='20', hour='16') values (4, 'nihaho', 'li', '222'), (5, 'tahao', 'ha', '333'), (7, 'djh', 'hahh', '555'); -- Insert the test data into the source table. insert overwrite table tmp_table1 values (1, 'hh', 'liu', '999', 'I'), (2, 'cc', 'zhang', '888', 'I'), (3, 'cy', 'zhang', '666', 'I'),(4, 'hh', 'liu', '999', 'U'), (5, 'cc', 'zhang', '888', 'U'),(6, 'cy', 'zhang', '666', 'U');
```

If data meets the ON joint condition and is from the source table, you can use the data to perform the MERGE INTO operation on the destination table. If data does not meet the ON joint condition but is of the **I** type specified by
**event_type** in the source table, you can insert the data into the destination table.

```
merge into acid_address_book_base1 as t using tmp_table1 as s on s.id = t.id and t.year='2020' and t.month='08' and t.day='20' and t.hour='16' when matched then update set t.first_name = s.first_name, t.last_name = s.last_name, t.phone = s.phone when not matched and (s._event_type_='I') then insert values(s.id, s.first_name, s.last_name,s.phone,'2020','08','20','16'); -- Query the destination table after the preceding operations are complete. select * from acid_address_book_base1;
```

The following result is returned:

```
+------------+------------+-----------+-------+------+-------+-----+------+
| id         | first_name | last_name | phone | year | month | day | hour |
+------------+------------+-----------+-------+------+-------+-----+------+
| 4          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 5          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 7          | djh        | hahh      | 555   | 2020 | 08    | 20  | 16   |
| 1          | hh         | liu       | 999   | 2020 | 08    | 20  | 16   |
| 2          | cc         | zhang     | 888   | 2020 | 08    | 20  | 16   |
| 3          | cy         | zhang     | 666   | 2020 | 08    | 20  | 16   |
+------------+------------+-----------+-------+------+-------+-----+------+
```

**ALTER TABLE COMPACT**

If you perform DELETE operations on a transactional table, the Base file that you want to delete is not modified. A Delta file is generated every time you perform a DELETE operation. As a result, if you perform multiple DELETE operations, the generated Delta files occupy more storage resources. If you perform several DELETE operations on the same table or partition, a large number of Delta files may be generated based on the amount of the data that you delete. Similarly, if you perform an UPDATE operation which is converted into the combination of the DELETE and INSERT INTO operations, Delta files are also generated. If the system reads data from the table, it must load the generated Delta files to find the deleted rows. A large number of Delta files reduce data reading efficiency. In this case, you can use the ALTER TABLE COMPACT statement to merge the Base files with Delta files to reduce storage usage and improve data reading efficiency.

```
alter table <table_name> [partition (partition_key = 'partition_value' [, ...])] compact [major|minor];
```

Description: This statement is used to merge the Base files with Delta files to reduce storage usage and improve data reading efficiency.
**Minor compaction**: merges all Delta files with their Base files. The Delta files must be generated based on the
same Base file. Delta files that are generated based on different Base files cannot be merged.
**Major compaction**: merges all Delta files generated based on the same Base file with the Base file, deletes the
Delta files, and merges small files in multiple Base files that correspond to tables. If the size of the Base file is less than 32 MB or a Delta file is generated, the INSERT OVERWRITE operation is performed on the table. However, if the size of the Base file is greater than or equal to 32 MB or no Delta files are generated, the INSERT OVERWRITE operation is not performed on the table. Sample statements:

```
alter table acid_delete compact minor; alter table acid_update_pt partition (ds = '2019') compact major;
```

The following result is returned:

```
Summary: table name: acid_update_pt /ds=2019 instance count: 2 run time: 16
  before merge, file count:        8  file size: 2423  file physical size: 7269
   after merge, file count:        2  file size: 642  file physical size: 1926
```

### 3.6 Built-in functions

#### 3.6.1 Mathematical functions

##### 3.6.1.1 ABS

This topic describes the ABS function in mathematical functions and provides examples.

```
double abs(double number) bigint abs(bigint number) decimal abs(decimal number)
```

Description: This function calculates the absolute value of **number**. Parameters: The **number** parameter supports a value of the BIGINT, DOUBLE, or DECIMAL type. If the input value is of the BIGINT, DOUBLE, or DECIMAL type, a value of the same type is returned. If the input value is of the STRING type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: The type of the return value depends on that of the input value, which can be DOUBLE, BIGINT, or DECIMAL. If the input value is NULL, NULL is returned. If the input value is of the BIGINT type and is greater than the maximum value of the BIGINT type, a value of the DOUBLE type is returned. However, the precision may be lost.

```
abs(null)=null abs(-1)=1 abs(-1.2)=1.2 abs("-2")=2.0 abs(122320837456298376592387456923748)=1.2232083745629837e32
```

The following example shows the usage of an ABS function in SQL statements. Other built-in functions, except window functions and aggregate functions, are used in a similar way.

```
select abs(id) from tbl1; -- Calculate the absolute value of the id field in tbl1.
```

##### 3.6.1.2 ACOS

This topic describes the ACOS function in mathematical functions and provides examples.

```
double acos(double number) decimal acos(decimal number)
```

Description: This function calculates the arccosine of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. The value ranges from -1 to 1. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. The value ranges from 0 to π. If the input value is NULL, NULL is returned.

```
acos("0.87") = 0.5155940062460905 acos(0) = 1.5707963267948966
```

##### 3.6.1.3 ASIN

This topic describes the ASIN function in mathematical functions and provides examples.

```
double asin(double number) decimal asin(decimal number)
```

Description: This function calculates the arcsine of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. The value ranges from -1 to 1. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. The value ranges from -π/2 to π/2. If the input value is NULL, NULL is returned.

```
asin(1) = 1.5707963267948966 asin(-1) = -1.5707963267948966
```

##### 3.6.1.4 ATAN

This topic describes the ATAN function in mathematical functions and provides examples.

```
double atan(double number)
```

Description: This function calculates the arctangent of **number**. Parameters: The **number** parameter supports a value of the DOUBLE type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE type is returned. The value ranges from -π/2 to π/2. If the input value is NULL, NULL is returned.

```
atan(1) = 0.7853981633974483; atan(-1) = -0.7853981633974483
```

##### 3.6.1.5 CEIL

This topic describes the CEIL function in mathematical functions and provides examples.

```
bigint ceil(double value) bigint ceil(decimal value)
```

Description: This function rounds up **value** and returns the nearest integer. Parameters: The **value** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the BIGINT type is returned. If the input value is NULL, NULL is returned.

```
ceil(1.1) = 2 ceil(-1.1) = -1
```

##### 3.6.1.6 CONV

This topic describes the CONV function in mathematical functions and provides examples.

```
string conv(string input, bigint from_base, bigint to_base)
```

Description: This function converts a number from one number system to another. Parameters:
**input**: the integer you want to convert, which is of the STRING type. If the input value is of the BIGINT or DOUBLE
type, it is implicitly converted to a value of the STRING type before calculation.
**from_base, to_base**: decimal numbers. The values can be 2, 8, 10, or 16. If the input value is of the STRING or
DOUBLE type, it is implicitly converted to a value of the BIGINT type before calculation. Return value: A value of the STRING type is returned. If an input value is NULL, NULL is returned. The conversion process runs at 64-bit precision. If an overflow occurs, an error is returned. If the input value is a negative value that begins with an en dash (–), an error is returned. If the input value is a decimal, it is converted to an integer before the conversion of number systems. The decimal part is left out.

```
conv('1100', 2, 10) = '12' conv('1100', 2, 16) = 'c' conv('ab', 16, 10) = '171' conv('ab', 16, 16) = 'ab'
```

##### 3.6.1.7 COS

This topic describes the COS function in mathematical functions and provides examples.

```
double cos(double number) decimal cos(decimal number)
```

Description: This function calculates the cosine of **number**, which is a radian value. Parameters: **number**, a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

```
cos(3.1415926/2) = 2.6794896585028633e-8 cos(3.1415926) = -0.9999999999999986
```

##### 3.6.1.8 COSH

This topic describes the COSH function in mathematical functions.

```
double cosh(double number) decimal cosh(decimal number)
```

Description: This function calculates the hyperbolic cosine of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.9 COT

This topic describes the COT function in mathematical functions.

```
double cot(double number) decimal cot(decimal number)
```

Description: This function calculates the cotangent of **number**, which is a radian value. Parameters: **number**, a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.10 EXP

This topic describes the EXP function in mathematical functions.

```
double exp(double number) decimal exp(decimal number)
```

Description: This function calculates the exponential value of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: The exponential value of **number** is returned. The value is of the DOUBLE or DECIMAL type. If the input value is NULL, NULL is returned.

##### 3.6.1.11 FLOOR

This topic describes the FLOOR function in mathematical functions and provides examples.

```
bigint floor(double number) bigint floor(decimal number)
```

Description: This function rounds down **number** and returns the nearest integer that is no greater than the value of number. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the BIGINT type is returned. If the input value is NULL, NULL is returned.

```
floor(1.2) = 1 floor(1.9) = 1 floor(0.1) = 0 floor(-1.2) = -2 floor(-0.1) = -1 floor(0.0) = 0 floor(-0.0) = 0
```

##### 3.6.1.12 LN

This topic describes the LN function in mathematical functions.

```
double ln(double number) decimal ln(decimal number)
```

Description: This function calculates the natural logarithm of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned. If the input value is a negative value or 0, an error is returned.

```
select ln(1000);
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 6.907755278982137 |
+------------+
```

##### 3.6.1.13 LOG

This topic describes the LOG function in mathematical functions.

```
double log(double base, double x) decimal log(decimal base, decimal x)
```

Description: This function calculates the logarithm of **x** whose base number is **base**. Parameters:
**base**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned.
**x**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: The logarithm value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned. If an input value is a negative value or 0, an error is returned. If the value of **base** is 1, an error is returned. The value 1 causes division by zero.

```
select log(10,100);
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 2.0        |
+------------+
```

##### 3.6.1.14 POW

This topic describes the POW function in mathematical functions.

```
double pow(double x, double y) decimal pow(decimal x, decimal y)
```

Description: This function calculates the **y**th power of **x**, namely, **x^y**. Parameters:
**x**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned.
**y**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned.

```
select pow(10,2);
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 100.0      |
+------------+
```

##### 3.6.1.15 RAND

This topic describes the RAND function in mathematical functions and provides examples.

```
double rand(bigint seed)
```

Description: This function returns a random number of the DOUBLE type based on **seed**. The value ranges from 0 to 1. Parameters: The **seed** parameter supports a value of the BIGINT type. It specifies the starting point in generating random numbers. This parameter is optional. Return value: A value of the DOUBLE type is returned.

```
select rand(); select rand(1);
```

##### 3.6.1.16 ROUND

This topic describes the ROUND function in mathematical functions and provides examples.

```
double round(double number, [bigint decimal_places]) decimal round(decimal number, [bigint decimal_places])
```

Description: This function returns a number rounded to the specified decimal place. Parameters:
**number**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned.
**decimal_places**: a constant of the BIGINT type. It specifies the decimal place to which the number is rounded. If the
input value is of another data type, an error is returned. If this parameter is not specified, the number is rounded to the ones place. The default value is 0.
**decimal_places** supports negative values. A negative value indicates counting from the decimal
point to the left, and the decimal part is excluded. If **decimal_places** exceeds the length of the integer part, 0 is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned.

```
round(125.315) = 125.0 round(125.315, 0) = 125.0 round(125.315, 1) = 125.3 round(125.315, 2) = 125.32 round(125.315, 3) = 125.315 round(-125.315, 2) = -125.32 round(123.345, -2) = 100.0 round(null) = null round(123.345, 4) = 123.345 round(123.345, -4) = 0.0
```

##### 3.6.1.17 SIN

This topic describes the SIN function in mathematical functions.

```
double sin(double number) decimal sin(decimal number)
```

Description: This function calculates the sine of **number**, which is a radian value. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.18 SINH

This topic describes the SINH function in mathematical functions.

```
double sinh(double number) decimal sinh(decimal number)
```

Description: This function calculates the hyperbolic sine of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.19 SQRT

This topic describes the SQRT function in mathematical functions.

```
double sqrt(double number) decimal sqrt(decimal number)
```

Description: This function calculates the square root of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. It must be greater than 0. If it is less than 0, an error is returned. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.20 TAN

This topic describes the TAN function in mathematical functions.

```
double tan(double number) decimal tan(decimal number)
```

Description: This function calculates the tangent of **number**, which is a radian value. Parameters: **number**, a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.21 TANH

This topic describes the TANH function in mathematical functions.

```
double tanh(double number) decimal tanh(decimal number)
```

Description: This function calculates the hyperbolic tangent of **number**. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted to a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If the input value is NULL, NULL is returned.

##### 3.6.1.22 TRUNC

This topic describes the TRUNC function in mathematical functions and provides examples.

```
double trunc(double number[, bigint decimal_places]) decimal trunc(decimal number[, bigint decimal_places])
```

Description: This function truncates the input value of **number** to a specified number of decimal places. Parameters:
**number**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into a value of the DOUBLE type before calculation. If the input value is of another data type, an error is returned.
**decimal_places**: the decimal place, which is a constant of the BIGINT type. This parameter indicates the position
where the number is truncated. If it is of another data type, it is implicitly converted into the BIGINT type. If you do not specify this parameter, the number is truncated to the ones place.
**decimal_places** can be a negative value, which indicates that the number is truncated from the
decimal point to the left and the decimal part is left out. If **decimal_places** exceeds the length of the integer part, 0 is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. If an input value is NULL, NULL is returned. If a value of the DOUBLE type is returned, the return value may not be properly displayed. This issue exists in all systems. For more information, see **trunc(125.815,1)** in the following example. The number is filled with zeros from the specified position.

```
trunc(125.815) = 125.0 trunc(125.815, 0) =125.0 trunc(125.815, 1) = 125.80000000000001 trunc(125.815, 2) = 125.81 trunc(125.815, 3) = 125.815 trunc(-125.815, 2) = -125.81 trunc(125.815, -1) = 120.0 trunc(125.815, -2) = 100.0 trunc(125.815, -3) = 0.0 trunc(123.345, 4) = 123.345 trunc(123.345, -4) = 0.0
```

##### 3.6.1.23 Additional mathematical functions

###### 3.6.1.23.1 Usage notes

This topic provides notes for you to use additional mathematical functions. MaxCompute 2.0 provides additional mathematical functions. If you want to call additional mathematical functions, you must add the following SET statement before the SQL statement that contains the additional mathematical functions:

```
set odps.sql.type.system.odps2=true;
```

You must simultaneously submit and execute the SET statement and the SQL statement that contains the additional mathematical functions.

###### 3.6.1.23.2 LOG2

This topic describes the LOG2 function in mathematical functions and provides examples.

```
double log2(double number) double log2(decimal number)
```

Description: This function calculates the logarithm of **number** with the base number of 2. Parameters: **number**, a value of the DOUBLE or DECIMAL type. Return value: A value of the DOUBLE type is returned. If the input value is 0 or NULL, NULL is returned.

```
log2(null) = null log2(0) = null log2(8) = 3.0
```

###### 3.6.1.23.3 LOG10

This topic describes the LOG10 function in mathematical functions and provides examples.

```
double log10(double number) double log10(decimal number)
```

Description: This function calculates the logarithm of **number** with the base number of 10. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. Return value: A value of the DOUBLE type is returned. If the input value is 0 or NULL, NULL is returned.

```
log10(null)=null log10(0)=null log10(8)=0.9030899869919435
```

###### 3.6.1.23.4 BIN

This topic describes the BIN function in mathematical functions and provides examples.

```
string bin(bigint number)
```

Description: This function calculates the binary code of **number**. Parameters: The **number** parameter supports a value of the BIGINT type. Return value: A value of the STRING type is returned. If the input value is 0, 0 is returned. If the input value is NULL, NULL is returned.

```
bin(0) = '0' bin(null) = 'null' bin(12) = '1100'
```

###### 3.6.1.23.5 HEX

This topic describes the HEX function in mathematical functions and provides examples.

```
string hex(bigint number) string hex(string number) string hex(binary number)
```

Description: This function converts an integer or a string into a hexadecimal number. Parameters: If **number** is of the BIGINT type, a hexadecimal number is returned. If **number** is of the STRING type, a string in hexadecimal format is returned. Return value: A value of the STRING type is returned. If the input value is 0, 0 is returned. If the input value is NULL, NULL is returned.

```
hex(0) = '0' hex('abc') = '616263' hex(17) = '11' hex('17') = '3137' hex(null) -- An exception occurs and the execution fails.
```

###### 3.6.1.23.6 UNHEX

This topic describes the UNHEX function in mathematical functions and provides examples.

```
binary unhex(string number)
```

Description: This function converts a hexadecimal string into a string. Parameters: The **number** parameter specifies a hexadecimal string. Return value: A value of the BINARY type is returned. If the input value is 0, an error is returned. If the input value is NULL, NULL is returned.

```
unhex('616263') = 'abc' unhex(616263) = 'abc'
```

###### 3.6.1.23.7 RADIANS

This topic describes the RADIANS function in mathematical functions and provides examples.

```
double radians(double number)
```

Description: This function converts a degree into a radian value. Parameters: **number**, a value of the DOUBLE type. Return value: A value of the DOUBLE type is returned. If the input value is NULL, NULL is returned.

```
radians(90) = 1.5707963267948966 radians(0) = 0.0 radians(null) = null
```

###### 3.6.1.23.8 DEGREES

This topic describes the DEGREES function in mathematical functions and provides examples.

```
double degrees(double number) double degrees(decimal number)
```

Description: This function converts a radian value to a degree. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. Return value: A value of the DOUBLE type is returned. If the input value is NULL, NULL is returned.

```
degrees(1.5707963267948966) = 90.0 degrees(0) = 0.0 degrees(null) = null
```

###### 3.6.1.23.9 SIGN

This topic describes the SIGN function in mathematical functions and provides examples.

```
double sign(double number) double sign(decimal number)
```

Description: This function returns the sign of an input value. Parameters: The **number** parameter supports a value of the DOUBLE or DECIMAL type. Return value: A value of the DOUBLE type is returned. If the input value is a positive value, 1.0 is returned. If the input value is a negative value, -1.0 is returned. If the input value is 0, 0.0 is returned. If the input value is NULL, NULL is returned.

```
sign(-2.5) = -1.0 sign(2.5) = 1.0 sign(0) = 0.0 sign(null) = null
```

###### 3.6.1.23.10 E

This topic describes the E function in mathematical functions and provides examples.

```
double e()
```

Description: This function returns the value of **e**. Return value: A value of the DOUBLE type is returned.

```
e() = 2.718281828459045
```

###### 3.6.1.23.11 PI

This topic describes the PI function in mathematical functions and provides examples.

```
double pi()
```

Description: This function calculates the value of π. Return value: A value of the DOUBLE type is returned.

```
pi() = 3.141592653589793
```

###### 3.6.1.23.12 FACTORIAL

This topic describes the FACTORIAL function in mathematical functions and provides examples.

```
bigint factorial(int number)
```

Description: This function calculates the factorial of **number**. Parameters: **number** indicates a value of the INT type. The value ranges from 0 to 20. Return value: A value of the BIGINT type is returned. If the input value is 0, 1 is returned. If the input value is NULL or a value that does not fall into the range from 0 to 20, NULL is returned.

```
factorial(5) = 120 --5! = 5*4*3*2*1 = 120
```

###### 3.6.1.23.13 CBRT

This topic describes the CBRT function in mathematical functions and provides examples on how to use the function.

```
double cbrt(double number)
```

Description: This function calculates the cube root of **number**. Parameters: **number**: A value of the BIGINT, INT, SMALLINT, TINYINT, DOUBLE, FLOAT, or STRING type. Return value: A value of the DOUBLE type is returned. If **number** is not of the BIGINT, INT, SMALLINT, TINYINT, DOUBLE, FLOAT, or STRING type, an error is returned. If the input value is null, null is returned.

```
-- The return value is 2.0. select cbrt(8); -- The return value is null. select cbrt(null);
```

###### 3.6.1.23.14 SHIFTLEFT

This topic describes the SHIFTLEFT function in mathematical functions and provides examples.

```
int shiftleft(tinyint|smallint|int number1, int number2) bigint shiftleft(bigint number1, int number2)
```

Description: This function shifts a value left by a specific number of places (<<). Parameters:
**number1**: an integer of the TINYINT, SMALLINT, INT, or BIGINT type.
**number2**: an integer of the INT type.
Return value: A value of the INT or BIGINT type is returned.

```
shiftleft(1,2)=4 -- Shift the binary value of 1 two places to the left (1<<2, 0001 shifted to 0100). shiftleft(4,3)=32 -- Shift the binary value of 4 three places to the left (4<<3, 0100 shifted to 100000).
```

###### 3.6.1.23.15 SHIFTRIGHT

This topic describes the SHIFTRIGHT function in mathematical functions and provides examples.

```
int shiftright(tinyint|smallint|int number1, int number2) bigint shiftright(bigint number1, int number2)
```

Description: This function shifts a value right by a specific number of places (>>). Parameters:
**number1**: an integer of the TINYINT, SMALLINT, INT, or BIGINT type.
**number2**: an integer of the INT type.
Return value: A value of the INT or BIGINT type is returned.

```
shiftright(4,2) = 1 -- Shift the binary value of 4 two places to the right (4>>2, 0100 shifted to 0001). shiftright(32,3) = 4 -- Shift the binary value of 32 three places to the right (32>>3, 100000 shifted to 0100).
```

###### 3.6.1.23.16 SHIFTRIGHTUNSIGNED

This topic describes the SHIFTRIGHTUNSIGNED function in mathematical functions and provides examples.

```
int shiftrightunsigned(tinyint|smallint|int number1, int number2) bigint shiftrightunsigned(bigint number1, int number2)
```

Description: This function shifts an unsigned value right by a specific number of places (>>>). Parameters:
**number1**: an integer of the TINYINT, SMALLINT, INT, or BIGINT type.
**number2**: an integer of the INT type.
Return value: A value of the INT or BIGINT type is returned.

```
shiftrightunsigned(8,2) = 2 -- Shift the binary unsigned value of 8 two places to the right (8>>>2,1000 shifted to be 0010). shiftrightunsigned(-14,2) = 1073741820 -- Shift the binary value of -14 two places to the right (-14>>>2, 11111111 11111111 11111111 11110010 shifted to be 00111111 11111111 11111111 11111100).
```

###### 3.6.1.23.17 FORMAT_NUMBER

This topic describes the FORMAT_NUMBER function in mathematical functions and provides examples.

```
string format_number(float|double|decimal expr1, expr2)
```

Description: This function converts a number to a string in the specified format. Parameters:
**expr1**: a numeric expression that you want to format.
**expr2**: the number of decimal places. It can be of the INT type. It can also be expressed in the format of
**#,###,###.##**.
If **expr2** is greater than 0, the value is rounded to the specified place after the decimal point. If **expr2** is equal to 0, the value has no decimal point or fractional part. If **expr2** is less than 0 or greater than 340, an error is returned. Return value: A value of the STRING type is returned.

```
select format_number(5.230134523424545456,3); -- The value 5.230 is returned. select format_number(12332.123456, '#,###,###,###. ###'); -- The value 12,332.123 is returned.
```

###### 3.6.1.23.18 WIDTH_BUCKET

This topic describes the WIDTH_BUCKET function in mathematical functions and provides examples on how to use the function.

```
WIDTH_BUCKET(NUMERIC expr, NUMERIC min_value, NUMERIC max_value, INT num_buckets)
```

Description: This function specifies the number of buckets and the minimum and maximum values of the acceptable range for a bucket. This function allows you to construct equi-width buckets, in which the bucket range is divided into intervals that have an identical size. This function returns the ID of the bucket into which the value of a specific expression falls. This function supports the following data types: DECIMAL(precision,scale) in the MaxCompute V2.0 data type edition, BIGINT, INT, FLOAT, DOUBLE, and DECIMAL. Parameters:
**expr**: The expression for which you want to identify the matching bucket ID.
**min_value**: The minimum value of the acceptable range for the bucket.
**max_value**: The maximum value of the acceptable range for the bucket. The value must be greater than min_value.
**num_buckets**: The number of buckets. The value must be greater than 0.
Return value: A value of the BIGINT type is returned. The value ranges from 0 to num_buckets plus 1. If the value of
**expr** is less than the value of **min_value**, 0 is returned. If the value of **expr** is greater than the value of **max_value**,
the value of num_buckets plus 1 is returned. If the value of expr is NULL, NULL is returned. In other cases, the ID of the bucket into which the value falls is returned. The bucket ID is named based on the following formula: `FLOOR(`

```
num_buckets * (expr - min_value)/(max_value - min_value) + 1) . SELECT key,value,WIDTH_BUCKET(value,100,500,5) as value_group FROM VALUES
    (1,99),
    (2,100),
    (3,199),
    (4,200),
    (5,499),
    (6,500),
    (7,501),
    (8,NULL)
AS t(key,value);
```

The following result is returned:

```
+-------+--------+-------------+
| key   | value  | value_group |
+-------+--------+-------------+
| 1     | 99     | 0           |
| 2     | 100    | 1           |
| 3     | 199    | 2           |
| 4     | 200    | 2           |
| 5     | 499    | 5           |
| 6     | 500    | 6           |
| 7     | 501    | 6           |
| 8     | \N     | \N          |
+-------+--------+-------------+
```

#### 3.6.2 String functions

##### 3.6.2.1 CHAR_MATCHCOUNT

The CHAR_MATCHCOUNT function of MaxCompute calculates the number of characters that are the same between two specified strings. This function calculates the number of characters that belong to **str1** and appear in **str2**. This topic describes the syntax and parameters of the CHAR_MATCHCOUNT function. This topic also provides examples on how to use this function.

**Syntax**

```
bigint char_matchcount(string str1, string str2)
```

**Description**

**str1 and str2**: The values must be valid UTF-8 strings. If invalid characters are found during the comparison of the two
strings, the return value is `0` .

**Return value**

A value of the BIGINT type is returned. If an input value is null, null is returned.

```
-- The return value is 2. The strings a and b that belong to str1 appear in str2. select char_matchcount('abd', 'aabc');
```

##### 3.6.2.2 CHR

This topic describes the CHR function in string functions.

```
string chr(bigint ascii)
```

Description: This function converts specified an **ASCII** code into the required character. Parameters: **ascii** indicates the ASCII code in the BIGINT type. If the input value is of the STRING, DOUBLE, or DECIMAL type, it is implicitly converted into a value of the BIGINT type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. The input value ranges from 0 to 255. If the input value does not fall into this range, an error is returned. If an input value is NULL, NULL is returned.

##### 3.6.2.3 CONCAT

This topic describes the CONCAT function in string functions and provides examples.

```
string concat(string a, string b...)
```

Description: This function concatenates all specified strings. Parameters: **a** and **b**, values of the STRING type. If an input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If an input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the parameters are not specified or an input value is NULL, NULL is returned.

```
concat('ab', 'c') = 'abc' concat() = null concat('a', null, 'b') = null
```

##### 3.6.2.4 INSTR

The INSTR function returns the position of substring **str2** in string **str1**. This topic describes the syntax and parameters of the INSTR function and provides examples of using this function.

**Syntax**

```
bigint instr(string str1, string str2[, bigint start_position[, bigint nth_appearance]])
```

**Description**

**str1**: a value of the STRING type, which indicates the string in which you search for the substring. If the input value
is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of a data type that cannot be converted into a value of the STRING type, an error is returned.
**str2**: a value of the STRING type, which indicates the substring you want to search for. If the input value is of the
BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of a data type that cannot be converted into a value of the STRING type, an error is returned.
**start_position**: a value of the BIGINT type. If the input value is of another data type, an error is returned. This
parameter specifies the position of the character in **str1** from which the search starts. The default start position is the first character, marked as 1. If **start_position** is a negative value, the search starts from the end to the start of the string and the last character is -1.
**nth_appearance**: a value of the BIGINT type. If the value is greater than 0, it indicates the position where the
substring matches the string for the **nth_appearance** time. If the value is of another data type or less than or equal to 0, an error is returned.

**Return value**

A value of the BIGINT type is returned. The return value varies based on the following rules: If **str2** is not found in **str1**, 0 is returned. If **str2** is an empty string, the matching always succeeds and 1 is returned. For example, 1 is returned for `select`

```
instr('abc',''); .
```

If the value of **str1**, **str2**, **start_position**, or **nth_appearance** is null, null is returned. Example 1: Return the position of the substring `e` in the string `Tech on the net` . Sample statement:

```
-- The return value is 2. select instr('Tech on the net', 'e');
```

Example 2: Return the position of substring `on` in the string `Tech on the net` . Sample statement:

```
-- The return value is 6. select instr('Tech on the net', 'on');
```

Example 3: Return the position of the second occurrence in which the substring `e` appears in the string `Tech on` `the net` from the third character. Sample statement:

```
-- The return value is 14. select instr('Tech on the net', 'e', 3, 2);
```

Example 4: An input parameter is set to null. Sample statement:

```
-- The return value is null. select instr('Tech on the net', null);
```

##### 3.6.2.5 IS_ENCODING

This topic describes the IS_ENCODING function in string functions and provides examples.

```
boolean is_encoding(string str, string from_encoding, string to_encoding)
```

Description: This function determines whether the input string **str** can be converted from the character set specified by **from_encoding** to the character set specified by **to_encoding**. It can be used to determine whether the input string is garbled. Generally, **from_encoding** is set to utf-8, and **to_encoding** is set to gbk. Parameters:
**str**: a value of the STRING type. An empty string can belong to any character set.
**from_encoding** and to_encoding: a value of the STRING type. The two parameters specify the source and
destination character sets. If an input value is NULL, NULL is returned. Return value: A value of the BOOLEAN type is returned. If **str** can be converted, true is returned. Otherwise, false is returned.

```
is_encoding('test', 'utf-8', 'gbk') = true is_encoding('test', 'utf-8', 'gb2312') = true
```

##### 3.6.2.6 KEYVALUE

This topic describes the KEYVALUE function in string functions and provides examples on how to use the function.

```
KEYVALUE(STRING srcStr,STRING split1,STRING split2, STRING key) KEYVALUE(STRING srcStr,STRING key) // split1 = ";", split2 = ":"
```

Description: This function splits the source string **srcStr** into key-value pairs by **split1**, separates key-value pairs by
**split2**, and then returns the value of the specified **key**.
Parameters:
**srcStr**: The source string that you want to split.
**key**: A value of the STRING type. After you split the source string by **split1** and **split2**, the value of the specified
**key** is returned.
**split1 and split2**: Values of the STRING type. The delimiters that are used to split strings. You must split the source
string by using the specified delimiters. If you do not configure the parameters, the default value of **split1** is a semicolon (**;**) and the default value of **split2** is a colon (**:**). If multiple key-value pairs are obtained after the source string is split by **split1** and multiple delimiters specified by **split2** are used to split the pairs, the returned result is undefined. Return value: A value of the STRING type is returned. If the value of **split1** or **split2** is null, null is returned. If the value of **srcStr** or **key** is null, or **key** is not matched, null is returned. If multiple key-value pairs match the key, the value that corresponds to the first matched **key** is returned. Example 1

```
-- The return value is 2. select keyvalue('0:1\;1:2', 1);
```

The source string is **"0:1\;1:2"**. **split1** and **split2** use their default values. The default value of **split1** is a semicolon (**;**) and the default value of **split2** is a colon (**:**). After the source string is split by **split1**, the key-value pairs of **0:1\,1:2** are generated. After the key-value pairs are split by **split2**, the key-value pairs change to the following form:

```
0 1/ 1 2 -- The value 2 that corresponds to the key 1 is returned.
```

Example 2

```
-- The return value is 21910. keyvalue("\;decreaseStore:1\;xcard:1\;isB2C:1\;tf:21910\;cart:1\;shipping:2\;pf:0\;market:shoes\;instPayAmount:0\ \;",":","tf");
```

The source string is “\;decreaseStore:1\;xcard:1\;isB2C:1\;tf:21910\;cart:1\;shipping:2\;pf:0\;market:shoes\;instPayAmount:0\;". After the source string is split by **\;** specified by split1, the following key-value pairs are generated:

```
decreaseStore:1, xcard:1, isB2C:1, tf:21910, cart:1, shipping:2, pf:0, market:shoes, instPayAmount:0
```

After the key-value pairs are split by a colon (**:**) specified by split2, the key-value pairs change to the following form:

```
decreaseStore 1 xcard 1 isB2C 1 tf 21910 cart 1 shipping 2 pf 0 market shoes instPayAmount 0 -- The value 21910 that corresponds to the key tf is returned.
```

##### 3.6.2.7 LENGTH

This topic describes the LENGTH function in string functions and provides examples.

```
bigint length(string str)
```

Description: This function returns the length of the string **str**. Parameters: The **str** parameter supports a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the BIGINT type is returned. If the input value is NULL, NULL is returned. If the input value is not encoded in UTF-8, -1 is returned.

```
length('china') = 5
```

##### 3.6.2.8 LENGTHB

This topic describes the LENGTHB function in string functions and provides examples.

```
bigint lengthb(string str)
```

Description: This function calculates the length of **str** in bytes. Parameters: **str**, a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the BIGINT type is returned. If the input value is NULL, NULL is returned.

```
lengthb('hi! China') = 10
```

##### 3.6.2.9 MD5

This topic describes the MD5 function in string functions.

```
string md5(string value)
```

Description: This function calculates the **MD5** value of **value**. Parameters: **value**, a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

##### 3.6.2.10 PARSE_URL

This topic describes the PARSE_URL function in string functions and provides examples.

```
string parse_url(string url, string part[,string key])
```

Description: This function parses **url** and extracts information by **key**. Parameters:
**url**: the URL to parse. If **url** is NULL, NULL is returned. If **url** is an invalid URL, an error is returned.
**part**: a value of the STRING type. Valid values: HOST, PATH, QUERY, REF, PROTOCOL, AUTHORITY, FILE, and
USERINFO. The input value is not case-sensitive. If the input value is invalid, an error is returned.
**key**: If **part** is QUERY, the value of **key** is exacted from the query string in **URL** and is returned. Otherwise, **key** is
omitted. Return value: A value of the STRING type is returned.

```
url = file://username:password@example.com:8042/over/there/index.dtb? type=animal&name=narwhal#nose parse_url('url', 'HOST') = "example.com" parse_url('url', 'PATH') = "/over/there/index.dtb" parse_url('url', 'QUERY') = "type=animal&name=narwhal" parse_url('url', 'QUERY', 'name') = "narwhal" parse_url('url', 'REF') = "nose" parse_url('url', 'PROTOCOL') = "file" parse_url('url', 'AUTHORITY') = "username:password@example.com:8042" parse_url('url', 'FILE') = "/over/there/index.dtb? type=animal&name=narwhal" parse_url('url', 'USERINFO') = "username:password"
```

##### 3.6.2.11 REGEXP_EXTRACT

This topic describes the REGEXP_EXTRACT function in string functions and provides examples.

```
string regexp_extract(string source, string pattern[, bigint occurrence])
```

Description: This function splits **source** based on the regular expression specified by **pattern** and returns the characters in **group** at the nth occurrence, where n is specified by **occurrence**. Parameters:
**source**: a value of the STRING type. This parameter indicates the string that you want to split.
**pattern**: a constant of the STRING type. If **pattern** is an empty string or **group** is not specified in **pattern**, an error
is returned.
**occurrence**: a constant of the BIGINT type, which must be greater than or equal to 0. If the input value is of another
data type or is smaller than 0, an error is returned. If you do not specify this parameter, the default value 1 is used. The value 1 indicates that characters in the first **group** are returned. If you set **occurrence** to 0, all substrings that match the regular expression specified by **pattern** are returned. Data is encoded by using UTF-8. Return value: A value of the STRING type is returned. If an input value is NULL, NULL is returned.

```
regexp_extract('foothebar', 'foo(. *?)( bar)', 1) = the regexp_extract('foothebar', 'foo(. *?)( bar)', 2) = bar regexp_extract('foothebar', 'foo(. *?)( bar)', 0) = foothebar regexp_extract('8d99d8', '8d(\\d+)d8') = 99 -- If the regular expression is submitted on the MaxCompute client, use two backslashes (\\) as the escape char acters. regexp_extract('foothebar', 'foothebar') -- An error is returned because group is not specified in pattern.
```

##### 3.6.2.12 REGEXP_INSTR

This topic describes the REGEXP_INSTR function in string functions and provides examples.

```
bigint regexp_instr(string source, string pattern[,bigint start_position[, bigint nth_occurrence[, bigint retur n_option]]])
```

Description: This function returns the start or end position of the substring that matches **pattern** at the nth occurrence, where n is specified by **nth_occurrence**, in the **source** string from the start position specified by
**start_position**.
Parameters:
**source**: a value of the STRING type. This parameter specifies the string to which the substring you want to search
for belongs.
**pattern**: a constant of the STRING type. If **pattern** is an empty string, an error is returned.
**start_position**: a constant of the BIGINT type. This parameter indicates the start position for the search. If you do
not specify this parameter, the default value 1 is used. If the value is of another data type or less than or equal to 0, an error is returned.
**nth_occurrence**: a constant of the BIGINT type. If you do not specify this parameter, the default value 1 is used.
The default value 1 indicates the position where a substring matches pattern in the search for the first time. If the value is of another data type or less than or equal to 0, an error is returned.
**return_option**: a constant of the BIGINT type. Valid values are 0 and 1. If the value is of another data type or
invalid, an error is returned. The value 0 indicates that the start position of the matched substring is returned. The value 1 indicates that the end position of the matched substring is returned. Return value: A value of the BIGINT type is returned. This parameter indicates the start or end position of the matched substring returned in the **source** string based on the type specified by **return_option**. If an input value is NULL, NULL is returned.

```
-- The return value is 14. select regexp_instr("i love www.taobao.com", "o[[:alpha:]]{1}", 3, 2);
```

##### 3.6.2.13 REGEXP_SUBSTR

This topic describes the REGEXP_SUBSTR function in string functions and provides examples.

```
string regexp_substr(string source, string pattern[, bigint start_position[, bigint nth_occurrence]])
```

Description: This function returns the substring that matches a given **pattern** at the nth occurrence, where n is specified by **nth_occurrence**, in the **source** string from the start position specified by **start_position**. Parameters:
**source**: a value of the STRING type. It specifies the string that contains the substring to return.
**pattern**: a constant of the STRING type. It specifies the pattern used to match the substring. If the **pattern** value is
NULL, an error is returned.
**start_position**: a constant of the BIGINT type. It must be greater than 0. If it is of another data type or is less than or
equal to 0, the function returns an error. If start_position is not specified, the default value 1 is used. In this case, the function starts matching from the first character of the **source** string.
**nth_occurrence**: a constant of the BIGINT type. It must be greater than 0. If it is of another data type or is less than
or equal to 0, an error is returned. If it is not specified, the default value 1 is used. In this case, the function returns the substring that first matches the specified pattern. Return value: A value of the STRING type is returned. If an input value is NULL, NULL is returned. If no substrings match the specified pattern, NULL is returned.

```
regexp_substr ("I love aliyun very much", "a[[:alpha:]]{5}") = "aliyun" regexp_substr('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 1) = " have" regexp_substr('I have 2 apples and 100 bucks!', '[[:blank:]][[:alnum:]]*', 1, 2) = " 2"
```

##### 3.6.2.14 REGEXP_COUNT

This topic describes the REGEXP_COUNT function in string functions and provides examples.

```
bigint regexp_count(string source, string pattern[, bigint start_position])
```

Description: This function returns the number of times a substring matches a given **pattern** in the **source** string from the start position specified by **start_position**. Parameters:
**source**: a value of the STRING type. It specifies the string that contains the substring to match. If the input value is
of another data type, an error is returned.
**pattern**: a constant of the STRING type. It specifies the pattern used to match the substring. If the **pattern** value is
an empty string or is of another data type, an error is returned.
**start_position**: a constant of the BIGINT type. It must be greater than 0. If it is of another data type or is less than or
equal to 0, the function returns an error. If start_position is not specified, the default value 1 is used. In this case, the function starts matching from the first character of the **source** string. Return value: A value of the BIGINT type is returned. If an input value is NULL, NULL is returned. If no substrings match the specified pattern, 0 is returned.

```
regexp_count('abababc', 'a.c') = 1 regexp_count('abcde', '[[:alpha:]]{2}', 3) = 1
```

##### 3.6.2.15 REGEXP_REPLACE

This topic describes the REGEXP_REPLACE function in string functions and provides examples.

```
string regexp_replace(string source, string pattern, string replace_string[, bigint occurrence])
```

Description: This function substitutes the string specified by **replace_string** for the substring that matches a given
**pattern** at the nth occurrence, where n is specified by **occurrence**, in the **source** string, and returns the result.
Parameters:
**source**: a value of the STRING type. It specifies the string that contains the substring to substitute.
**pattern**: a constant of the STRING type. It specifies the pattern used to match the substring. If the value of **pattern**
is NULL, an error is returned.
**replace_string**: a value of the STRING type. It specifies the string to substitute for the substring that matches
**pattern**.
**occurrence**: a constant of the BIGINT type. It specifies the number of times at which the substring matches the
pattern and is substituted with **replace_string**. It must be greater than or equal to 0. If the input value is 0, all matched substrings are substituted. If the input value is less than 0 or is not of the BIGINT type, an error is returned. Default value: 0. The action of referencing a character class that does not exist is undefined. Return value: A value of the STRING type is returned. If the function references a character class that does not exist, substitution is not performed. If **replace_string** is NULL and substrings match **pattern**, NULL is returned. If
**replace_string** is NULL and no substrings match **pattern**, the source string is returned. If an input value is NULL,
NULL is returned.

```
regexp_replace("123.456.7890", "([[:digit:]]{3})\\.([[:digit:]]{3})\\.([[:digit:]]{4})", "(\\1)\\2-\\3", 0) = " (123)456-7890" regexp_replace("abcd", "(.)", "\\1 ", 0) = "a b c d " regexp_replace("abcd", "(.)", "\\1 ", 1) = "a bcd" regexp_replace("abcd", "(.)", "\\2", 1) = "abcd" -- Only one character class is defined in pattern. The second referenced character class does not exist. -- Try to avoid this action. The result of referencing a non-existent group is undefined. regexp_replace("abcd", "(. *)(.)$", "\\2", 0) = "d" regexp_replace("abcd", "a", "\\1", 0) = "bcd" -- No character class is defined in pattern. \1 references a non-existent character class. -- Try to avoid this action. The result of referencing a non-existent group is undefined.
```

##### 3.6.2.16 SPLIT_PART

This topic describes the SPLIT_PART function in string functions and provides examples.

```
string split_part(string str, string separator, bigint start[, bigint end])
```

Description: This function uses a delimiter specified by **separator** to split **str**, and returns a substring that starts from the character specified by **start** and ends with the character specified by **end**. Parameters:
**str**: a value of the STRING type, which indicates the string that you want to split. If the input value is of the BIGINT,
DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned.
**separator**: a constant of the STRING type, which indicates the delimiter used to split a string. It can be a character
or string. If it is of another data type, an error is returned.
**start**: a constant of the BIGINT type, which must be greater than 0. If the value is not a constant or is of another
data type, an error is returned. It indicates the start number of the segment to be returned. The number starts from
1. If **end** is not specified, the segment specified by **start** is returned.
**end**: a constant of the BIGINT type. It must be greater than or equal to the value of **start**. Otherwise, an error is
returned. It indicates the end number of the segment to be returned. If the value is not a constant or is of another data type, an error is returned. If this parameter is not specified, the last segment is returned. Return value: A value of the STRING type is returned. If you set **start** to a value greater than the number of segments, an empty string is returned. If **separator** is absent in **str** and **start** is set to 1, the entire **str** is returned. If **str** is an empty string, an empty string is returned. If **separator** is an empty string, **str** is returned. If you set **end** to a value greater than the number of segments, all segments are returned. If an input value is NULL, NULL is returned.

```
split_part('a,b,c,d', ',', 1) = 'a' split_part('a,b,c,d', ',', 1, 2) = 'a,b' split_part('a,b,c,d', ',', 10) = ''
```

##### 3.6.2.17 SUBSTR

This topic describes the SUBSTR function and provides examples of using this function.

```
string substr(string str, bigint start_position[, bigint length])
```

Description: This function returns a substring that starts from **start_position** in **str** and has a length specified by
**length**.
Parameters:
**str**: a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is
implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned.
**start_position**: a value of the BIGINT type. The search starts from the first character. If **start_position** is 0, null is
returned. If **start_position** is a negative value, the search starts from the end to the start of the string and the last character is -1. If the input value is of another data type, an error is returned.
**length**: a value of the BIGINT type. This parameter specifies the length of the substring. The input value must be
greater than 0. If the input value is of another data type or is less than or equal to 0, an error is returned. Return value: A value of the STRING type is returned. If an input value is null, null is returned. If **length** is not specified, this function returns a substring that starts from **start_position** in **str** to the end of **str**.

```
-- The return value is bc. select substr('abc', 2); -- The return value is b. select substr('abc', 2, 1); -- The return value is bc. select substr('abc',-2 , 2);
```

##### 3.6.2.18 TOLOWER

This topic describes the TOLOWER function in string functions and provides examples.

```
string tolower(string source)
```

Description: This function converts the string **source** to lowercase letters. Parameters: The **source** parameter supports a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

```
tolower("aBcd") = "abcd" tolower("HAHACd") = "hahacd"
```

##### 3.6.2.19 TOUPPER

This topic describes the TOUPPER function in string functions and provides examples.

```
string toupper(string source)
```

Description: This function converts **source** into uppercase letters. Parameters: **source**, a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

```
toupper("aBcd") = "ABCD" toupper("HahaCd") = "HAHACD"
```

##### 3.6.2.20 TO_CHAR

This topic describes the TO_CHAR function in string functions and provides examples on how to use the function.

```
string to_char(boolean value) string to_char(bigint value) string to_char(double value) string to_char(decimal value)
```

Description: This function converts data of the BOOLEAN, BIGINT, DECIMAL, or DOUBLE type into the STRING type. Parameters: **value** is a value of the BOOLEAN, BIGINT, DECIMAL, or DOUBLE type. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is null, null is returned.

```
-- The return value is 123. select to_char(123); -- The return value is TRUE. select to_char(true); -- The return value is 1.23. select to_char(1.23); -- The return value is null. select to_char(null);
```

##### 3.6.2.21 TRIM

This topic describes the TRIM function in string functions.

```
string trim(string str)
```

Description: This function eliminates the spaces on the left and right sides of the string **str**. Parameters: The **str** parameter supports a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, an error is returned.

##### 3.6.2.22 LTRIM

This topic describes the LTRIM function in string functions and provides examples.

```
string ltrim(string str)
```

Description: This function removes the spaces on the left side of **str**. Parameters: **str**, a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

```
select ltrim(' abc '); -- The following result is returned: +-----+
| _c0 |
+-----+
| abc  |
+-----+
```

##### 3.6.2.23 RTRIM

This topic describes the RTRIM function in string functions and provides examples.

```
string rtrim(string str)
```

Description: This function eliminates the spaces on the right side of the string **str**. Parameters: The **str** parameter supports a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

```
select rtrim('a abc '); -- The following result is returned: +-----+
| _c0 |
+-----+
| a abc |
+-----+
```

##### 3.6.2.24 REVERSE

This topic describes the REVERSE function in string functions and provides examples.

```
string reverse(string str)
```

Description: This function returns a string in reverse order. Parameters: The **str** parameter supports a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If the input value is NULL, an error is returned.

```
select reverse('abcedfg'); -- The following result is returned: +-----+
| _c0 |
+-----+
| gfdecba |
+-----+
```

##### 3.6.2.25 SPACE

This topic describes the SPACE function in string functions and provides examples.

```
string space(bigint n)
```

Description: This function returns a string of a length specified by **n**. Parameters: The **n** parameter supports a value of the BIGINT type. The value cannot exceed 2 MB. If this parameter is left empty, an error is returned. Return value: A value of the STRING type is returned.

```
select length(space(10)); -- The value 10 is returned. select space(400000000000); -- An error is returned because the length exceeds 2 MB.
```

##### 3.6.2.26 REPEAT

This topic describes the REPEAT function in string functions and provides examples.

```
string repeat(string str, bigint n)
```

Description: This function returns **n** duplicates of the string **str**. Parameters:
**str**: a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is
implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned.
**n**: a value of the BIGINT type. The returned string cannot exceed 2 MB in length. If this parameter is left empty, an
error is returned. Return value: A value of the STRING type is returned.

```
select repeat('abc',5); -- abcabcabcabcabc is returned.
```

##### 3.6.2.27 ASCII

This topic describes the ASCII function in string functions and provides examples.

```
bigint ascii(string str)
```

Description: This function returns the ASCII code of the first character in the string **str**. Parameters: The **str** parameter supports a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the BIGINT type is returned.

```
select ascii('abcde'); -- The value 97 is returned.
```

##### 3.6.2.28 Additional string functions

###### 3.6.2.28.1 Usage notes

This topic provides notes for you to use additional string functions. MaxCompute V2.0 provides additional string functions. You must add the following flag before the SQL statement that contains the additional string functions:

```
set odps.sql.type.system.odps2=true;
```

You must submit the flag along with the SQL statement that contains the additional string functions for execution.

###### 3.6.2.28.2 CONCAT_WS

This topic describes the CONCAT_WS function in string functions and provides examples.

```
string concat_ws(string SEP, string a, string b...) string concat_ws(string SEP, array)
```

Description: This function concatenates all input strings in an array by using a specified delimiter. Parameters:
**SEP**: the delimiter of the STRING type. If this parameter is not specified, an error is returned.
**a, b...**: a value of the STRING type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is
implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If no input values are specified or an input value is NULL, NULL is returned.

```
concat_ws(':','name','hanmeimei')='name:hanmeimei' concat_ws(':','avg',null,'34')=null
```

###### 3.6.2.28.3 LPAD

This topic describes the LPAD function in string functions and provides examples.

```
string lpad(string a, int len, string b)
```

Description: This function pads the left side of **a** with **b** based on the length specified by **len**. Parameters:
**len**: a value of the INT type.
**a**: a value of the STRING type.
**b**: a value of the STRING type.
A value of the STRING type is returned. The return value varies based on the following rules: If **len** is smaller than the number of characters in **a**, **a** is truncated from the left to obtain a string with the number of characters specified by **len**. If **len** is 0, no value is returned. If no input parameters are available or an input parameter is set to null, null is returned. If the value of **len** is greater than the number of characters in **a** and less than the total number of characters in **a** and **b**, this function left-pads **a** with **b** to the specified **len**.

```
-- The return value is 12abcdefgh. select lpad('abcdefgh', 10, '12'); -- The return value is abcde. select lpad('abcdefgh', 5, '12'); -- The return value is an empty string. select lpad('abcdefgh' ,0, '12'); -- The return value is null. select lpad(null ,0, '12'); -- The return value is 1abcdefgh. select lpad('abcdefgh',9,'12');
```

###### 3.6.2.28.4 RPAD

This topic describes the RPAD function in string functions and provides examples.

```
string rpad(string a, int len, string b)
```

Description: This function pads the right side of String **a** with String **b** until the new padded string has **len** characters. Parameters:
**len**: a value of the INT type.
**a**: a value of the STRING type.
**b**: a value of the STRING type.
A value of the STRING type is returned. The return value varies based on the following rules: If **len** is smaller than the number of characters in **a**, **a** is truncated from the left to obtain a string with the number of characters specified by **len**. If **len** is 0, no value is returned. If no input parameters are available or an input parameter is set to null, null is returned. If **len** is greater than the number of characters in **a** and less than the sum of the number of characters in **a** and **b**, **a** is right paded with **b** from left to right to the specified **len**.

```
-- The return value is abcdefgh12. select rpad('abcdefgh', 10, '12'); -- The return value is abcde. select rpad('abcdefgh', 5, '12'); -- The return value is an empty string. select rpad('abcdefgh' ,0, '12'); -- The return value is null. select rpad(null ,0, '12'); -- The return value is abcdefgh1. select rpad('abcdefgh',9,'12');
```

###### 3.6.2.28.5 REPLACE

This topic describes the REPLACE function in string functions and provides examples.

```
string replace(string a, string OLD, string NEW)
```

Description: This function substitutes the string **NEW** for the part of string **a** that is exactly the same as the string
**OLD**, and returns the string **a**.
Parameters: All the parameters support a value of the STRING type. Return value: A value of the STRING type is returned. If an input value is NULL, NULL is returned.

```
replace('ababab','abab','12')='12ab' replace('ababab','cdf','123')='ababab' replace('123abab456ab',null,'abab')=null
```

###### 3.6.2.28.6 SOUNDEX

This topic describes the SOUNDEX function in string functions and provides examples.

```
string soundex(string a)
```

Description: This function converts a normal string to a string of the **soundex** type. Parameters: The **a** parameter supports a value of the STRING type. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

```
soundex('hello') = 'H400'
```

###### 3.6.2.28.7 SUBSTRING_INDEX

This topic describes the SUBSTRING_INDEX function in string functions and provides examples on how to use this function.

```
string substring_index(string a, string SEP, int count))
```

Description: This function truncates the string **a** to a substring from the first character to the nth delimiter, where n is specified by **count**. If **count** is a positive value, the string is truncated from left to right. Otherwise, the string is truncated from right to left. Parameters:
**a**: required. A value of the STRING type. This parameter specifies the string that you want to truncate.
**SEP**: required. A value of the STRING type. This parameter specifies a delimiter.
**count**: required. A value of the INT type. This parameter specifies the position of the delimiter.
Return value: A value of the STRING type is returned. If an input parameter is set to null, null is returned.

```
-- The return value is https://help.aliyun. select substring_index('https://help.aliyun.com', '.', 2); -- The return value is aliyun.com. select substring_index('https://help.aliyun.com', '.', -2); -- The return value is null. select substring_index('https://help.aliyun.com', null, 2);
```

###### 3.6.2.28.8 TRANSLATE

This topic describes the TRANSLATE function in string functions and provides examples.

```
string translate(string|varchar str1, string|varchar str2, string|varchar str3)
```

Description: This function replaces the common substring of **str1** and **str2** with **str3**. Parameters: The **str** parameter supports a value of the STRING or VARCHAR type. If the input value is of the BIGINT, DECIMAL, DOUBLE, or DATETIME type, it is implicitly converted to a value of the STRING type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the STRING type is returned. If an input value is NULL, NULL is returned.

```
translate('MaxComputer','puter','pute')='MaxCompute' translate('aaa','b','c')='aaa' translate('MaxComputer','puter',null)=null
```

###### 3.6.2.28.9 URL_ENCODE

This topic describes the URL_ENCODE function in string functions and provides examples.

```
string url_encode(string input[, string encoding])
```

Description: This function encodes the input string in the **application/x-www-form-urlencoded MIME** format and returns the encoded string. The encoding format must comply with the following rules: All letters remain unchanged. Periods (.), hyphens (-), asterisks (*), and underscores (_) remain unchanged. Spaces are converted into plus signs (+). Other characters are converted into byte values based on the specified **encoding** format. Each byte value is then represented in the **%xy** format, where **xy** is the hexadecimal representation of the character value. Parameters
**input**: the string that you want to decode.
**encoding**: the specified encoding format. Valid values: GBK and UTF-8. If you do not specify this parameter, the
default value UTF-8 is used. Return value: A value of the STRING type is returned. If the input value is null, null is returned.

```
-- The return value is %CA%BE%EF%BF%BD%EF%BF%BDfor + URL_ENCODE%3A%2F%2F +%28fdsf%29. select URL_ENCODE ('Example for URL_ENCODE:// (fdsf)'); -- The return value is Example + for + URL_ENCODE%3A%2F%2F + dsf%28fasfs%29. select URL_ENCODE('Example for URL_ENCODE:// dsf(fasfs)', 'GBK');
```

###### 3.6.2.28.10 URL_DECODE

This topic describes the URL_DECODE function in string functions and provides examples.

```
string url_decode(string input[, string encoding])
```

Description: This function converts an input string from the **application/x-www-form-urlencoded MIME** format into a normal string. This is the inverse function of **URL_ENCODE**. All letters remain unchanged. Periods (.), hyphens (-), asterisks (*), and underscores (_) remain unchanged. Plus signs (+) are converted into spaces. The function first performs decoding based on the percent sign (%). The sequences that are in the **%xy** format are converted into byte values. Then, the function performs decoding based on the encoding format specified by the second parameter. Consecutive byte values are decoded to the required strings based on the format specified by
**encoding**.
Other characters remain unchanged. The return value of the function is a string encoded in UTF-8. Parameters:
**input**: the string that you want to decode.
**encoding**: the specified encoding format. Valid values include GBK and UTF-8. If you do not specify this parameter,
the default value UTF-8 is used. Return value: A value of the STRING type is returned. If the input value is null, null is returned.

```
-- The return value is Example for url_decode:// (fdsf). select url_decode('%E7%A4%BA%E4%BE%8Bfor+url_decode%3A%2F%2F+%28fdsf%29'); -- The return value is Example for url_decode :// dsf(fasfs). select url_decode('Example+for+url_decode+%3A%2F%2F+dsf%28fasfs%29', 'GBK');
```

###### 3.6.2.28.11 JSON_TUPLE

This topic describes the JSON_TUPLE function in string functions and provides examples.

```
STRING JSON_TUPLE(STRING json,STRING key1,STRING key2,...)
```

Description: This function extracts specific strings from a standard JSON string based on a set of input keys, such as
**key1 and key2**.
Parameters:
**json**: a value of the STRING type. It specifies a standard JSON string.
**key**: a value of the STRING type. It describes the JSON **path**. You can enter multiple keys at a time. A key cannot
start with a dollar sign ($). Return value: A value of the STRING type is returned. If the **JSON** parameter is empty or invalid, NULL is returned. If the **key** parameter is empty or invalid, NULL is returned. If the key value does not exist in the **JSON** string, it is considered invalid. If the **JSON** parameter is valid and the **key** value exists in the JSON string, the required string is returned. This function can parse JSON data that contains Chinese characters. This function can parse nested JSON data. This function can parse JSON data that contains nested arrays. This function parses a JSON string in the same way as the GET_JSON_OBJECT function for which `set` odps.sql.udf.getjsonobj.new=true; is added. To parse a **JSON** string multiple times, you must call the GET_JSON_OBJECT function multiple times. However, the JSON_TUPLE function allows you to enter multiple
**keys** at a time and parse the **JSON** string only once. This improves parsing efficiency.
JSON_TUPLE is a user-defined table-valued function (UDTF). To select other columns, you can use JSON_TUPLE with LATERAL VIEW. Prepare a school table that contains the following data:

```json
Table: school +------------+------------+
| Id         | json       |
+------------+------------+
| 1          | {
                "School name": "Hupan college",
                "Location":"Hangzhou",
                "SchoolRank": "00",
                "Class1":{
                  "Student":[{
                    "studentId":1,
                    "scoreRankIn3Year":[1,2,[3,2,6]]
                  }, {
                    "studentId":2,
                    "scoreRankIn3Year":[2,3,[4,3,1]]
                }]}
               }          |
+------------+------------+
```

Extract JSON objects.

```
select json_tuple(school.json,"SchoolRank","Class1") as (item0,item1) from school; -- The preceding and following statements are equivalent. select get_json_object(school.json,"$.SchoolRank") item0,get_json_object(school.json,"$.Class1") item1 from sch ool;
```

The following result is returned:

```
+-------+-------+
| item0 | item1 |
+-------+-------+
| 00    | {"Student":[{"studentId":1,"scoreRankIn3Year":[1,2,[3,2,6]]},{"studentId":2,"scoreRankIn3Year":[2,3,[
4,3,1]]}]} | +-------+-------+
```

Parse JSON data that contains Chinese characters.

```
select json_tuple(school.json,"School name","Location") as (item0,item1) from school;
```

The following result is returned:

```
+-------+-------+
| item0 | item1 |
+-------+-------+
| Hupan college | Hangzhou |
+-------+-------+
```

Parse nested JSON data.

```
select sc.Id, q.item0, q.item1 from school sc LATERAL VIEW json_tuple(sc.json,"Class1.Student.[ *].studentId","Class1.Student.[0] .scoreRankIn3Year") q as item0,item1;
```

The following result is returned:

```
+------------+-------+-------+
| id         | item0 | item1 |
+------------+-------+-------+
| 1          | [1,2] | [1,2,[3,2,6]] |
+------------+-------+-------+
```

Parse JSON data that contains nested arrays.

```
select sc.Id, q.item0, q.item1 from school sc LATERAL VIEW json_tuple(sc.json,"Class1.Student[0].scoreRankIn3Year[2]","Class1.Student[0].scoreRankIn3Year[2][1]") q as ite m0,item1;
```

The following result is returned:

```
+------------+-------+-------+
| id         | item0 | item1 |
+------------+-------+-------+
| 1          | [3,2,6] | 2     |
+------------+-------+-------+
```

###### 3.6.2.28.12 FROM_JSON

This topic describes the FROM_JSON function in string functions and provides examples.

```
FROM_JSON(jsonStr, schema)
```

Description: This function processes a JSON string and returns a value of the ARRAY, MAP, or STRUCT type with the specified schema. Parameters:
**jsonStr**: a value of the STRING type. This parameter specifies the JSON string to process.
**schema**: the data structure. The syntax of schema is the same as that of table creation statements. Examples:

```
 array<bigint>
 map<string, array<string>>
 struct<a:int, b:double, c:map<string,string>>
```

For the STRUCT type, you can also specify a value in the `'a INT, b DOUBLE'` format, which is equivalent to

```
 struct<a:int, b:double> .
```

The following table describes the mapping relationships between JSON and MaxCompute data types.

| JSON | MaxCompute |
|---|---|
| Object | STRUCT/MAP/STRING |
| Array | ARRAY/STRING |
| Number | TINYINT/SMALLINT/IBT/BIGINT/FLOAT/DOUBLE/DECIMAL/STRING |
| true/false | BOOLEAN/STRING |
| String | STRING |
| null | All types |

For the OBJECT and ARRAY types, this function preferentially parses the data. For the types that are not supported by MaxCompute, this function ignores the data. Return value: A value of the ARRAY, MAP, or STRUCT type is returned. If the **schema** parameter is left empty, an error is returned.

```
SELECT from_json('{"a":1, "b":0.8}', 'a INT, b DOUBLE'); -- {"a":1, "b":0.8} is returned. SELECT from_json('{"time":"26/08/2015"}', 'time string'); -- {"time":"26/08/2015"} is returned. SELECT from_json('{"a":1, "b":0.8}', 'a INT, b DOUBLE, c STRING'); -- {"a":1, "b":0.8, c: NULL} is returned. SELECT from_json('[1, 2, 3, "a"]', 'array<BIGINT>'); -- [1, 2, 3] is returned.
```

###### 3.6.2.28.13 TO_JSON

This topic describes the TO_JSON function in string functions and provides examples.

```
TO_JSON(expr)
```

Description: This function returns a JSON string for a value of a given type. Parameters: The **expr** parameter supports a value of the ARRAY, MAP, or STRUCT type. Return value: A value of the STRING type is returned.

```
SELECT to_json(named_struct('a', 1, 'b', 2)); -- {"a":1,"b":2} is returned. SELECT to_json(named_struct('time', "26/08/2015")); -- {"time":"26/08/2015"} is returned. SELECT to_json(array(named_struct('a', 1, 'b', 2))); -- [{"a":1,"b":2}] is returned. SELECT to_json(map('a', named_struct('b', 1))); -- {"a":{"b":1}} is returned. SELECT to_json(map('a', 1)); -- {"a":1} is returned. SELECT to_json(array((map('a', 1)))); -- [{"a":1}] is returned.
```

#### 3.6.3 Date functions

##### 3.6.3.1 DATEADD

This topic describes the date function DATEADD and provides examples.

```
datetime dateadd(datetime date, bigint delta, string datepart)
```

Description: This function modifies a **date** value based on **datepart** and **delta** that you specified. Parameters:
**date**: a date value of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, it is
implicitly converted into a value of the DATETIME type before the calculation. If the input value is of another data type, an error is returned.
**delta**: a value of the BIGINT type, which indicates the interval to add to the specified part of the date value. If the
input value is of the STRING or DOUBLE type, it is implicitly converted into a value of the BIGINT type before the calculation. If the input value is of another data type, an error is returned. If the value of **delta** is greater than 0, this function adds the interval to the date value. In other cases, this function subtracts the interval from the date value. If you add or subtract the interval specified by **delta** at a date part, a carry or return at more significant date parts may occur. The year, month, hour, minute, and second parts are computed by using different numeral systems. The year part uses the base-10 numeral system. The month part uses the base-12 numeral system. The hour part uses the base-24 numeral system. The minute and second parts use the base-60 numeral system. If the DATEADD function adds an interval specified by **delta** to the month part of a date value of the DATETIME type and this operation does not cause an overflow of **day**, keep **day** unchanged. If the operation causes an overflow of day, set **day** to the last day of the specified month.
**datepart**: the part you want to modify in the date value. The value is a constant of the STRING type. If the value is
in an invalid format or is not a constant of the STRING type, an error is returned. The value of this parameter is specified in compliance with the rules of conversions between the STRING and DATETIME types. The value **yyyy** indicates that the DATEADD function adds an interval to the year part of the date value. The value **mm** indicates that the DATEADD function adds an interval to the month part of the date value. This parameter also supports extended date formats, such as **-year**, **-month**, **-mon**, **-day**, and **-hour**. For more information about the rules of data type conversions, see Conversion between string and datetime types. Return value: A value of the DATETIME type is returned. If an input value is NULL, NULL is returned. Example 1: common usage

```
select dateadd(datetime '2005-02-28 00:00:00', 1, 'dd') ; -- The return value is 2005-03-01 00:00:00. After one day is added, the result is beyond the last day of Febr uary. The actual date value is the first day of March. select dateadd(datetime '2005-02-28 00:00:00', -1, 'dd'); -- The return value is 2005-02-27 00:00:00. One day is subtracted. select dateadd(datetime '2005-02-28 00:00:00', 20, 'mm'); -- The return value is 2006-10-28 00:00:00. After 20 months are added, the month overflows, and the year incr eases by 1. select dateadd(datetime '2005-02-28 00:00:00', 1, 'mm'); -- The return value is 2005-03-28 00:00:00. One month is added. select dateadd(datetime '2005-01-29 00:00:00', 1, 'mm'); -- The return value is 2005-02-28 00:00:00. February in 2005 has only 28 days. Therefore, the last day of Feb ruary is returned. select dateadd(datetime '2005-03-30 00:00:00', -1, 'mm'); -- The return value is 2005-02-28 00:00:00. One month is subtracted. February in 2005 has only 28 days. There fore, the last day of February is returned.
```

Example 2: usage of DATEADD in which a value of the DATETIME type is expressed as a constant

```
select dateadd(2005-03-30 00:00:00, -1, 'mm'); -- In MaxCompute SQL statements, a value of the DATETIME type cannot be directly expressed as a constant. Thi s statement uses an invalid expression for a value of the DATETIME type. select dateadd(cast("2005-03-30 00:00:00" as datetime), -1, 'mm'); -- This statement uses the DATEADD function in which a constant of the STRING type is explicitly converted to a value of the DATETIME type.
```

##### 3.6.3.2 DATEDIFF

This topic describes the date function DATEDIFF and provides examples.

```
bigint datediff(datetime date1, datetime date2, string datepart)
```

Description: This function calculates the difference between **date1** and **date2**. The difference is measured in the time unit specified by **datepart**. Parameters:
**date1** and **date2**: the minuend and subtrahend. The values are of the DATE, DATETIME, or TIMESTAMP type. If an
input value is of the STRING type, it is implicitly converted into a value of the DATETIME type before the calculation. If the input value is of another data type, an error is returned.
**datepart**: the time unit, which is a constant of the STRING type. This parameter supports extended date formats. If
**datepart** is not in the specified format or is of another data type, an error is returned.
Return value: A value of the BIGINT type is returned. If an input value is NULL, NULL is returned. If **date1** is earlier than **date2**, a negative value is returned. If the difference between two dates is more precise than the unit specified by **datepart**, the excessive parts are discarded in the return value. For example, if the unit specified by **datepart** is day, the hour, minute, and second parts are discarded in the return value. This function omits the parts with smaller units based on the unit specified by **datepart** and calculates the result. The parts with smaller units refer to the excessive parts previously described.

```
-- The start time is 2005-12-31 23:59:59 and the end time is 2006-01-01 00:00:00.
    datediff(end, start, 'dd') = 1
    datediff(end, start, 'mm') = 1
    datediff(end, start, 'yyyy') = 1
    datediff(end, start, 'hh') = 1
    datediff(end, start, 'mi') = 1
    datediff(end, start, 'ss') = 1
    datediff(datetime'2013-05-31 13:00:00', '2013-05-31 12:30:00', 'ss') = 1800
    datediff(datetime'2013-05-31 13:00:00', '2013-05-31 12:30:00', 'mi') = 30
-- The start time is 2018-06-04 19:33:23.234 and the end time is 2018-06-04 19:33:23.250. Date values with mill iseconds do not adopt the standard DATETIME type and therefore cannot be implicitly converted into the DATETIME type. In this case, an explicit conversion is required.
    datediff(to_date('2018-06-04 19:33:23.250', 'yyyy-MM-dd hh:mi:ss.ff3'),to_date('2018-06-04 19:33:23.234', '
yyyy-MM-dd hh:mi:ss.ff3') , 'ff3') = 16
```

##### 3.6.3.3 DATEPART

This topic describes the date function DATEPART and provides examples.

```
bigint datepart(datetime date, string datepart)
```

Description: This function returns a specific part of a **date** value. The part is specified by **datepart**. Parameters:
**date**: a date value of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, it is
implicitly converted into a value of the DATETIME type before the calculation. If the input value is of another data type, an error is returned.
**datepart**: a constant of the STRING type. This parameter supports extended date formats. If **datepart** is not in the
specified format or is of another data type, an error is returned. Return value: A value of the BIGINT type is returned. If an input value is NULL, NULL is returned.

```
datepart('2017-06-08 01:10:00', 'yyyy') = 2017 datepart('2017-06-08 01:10:00', 'mm') = 6
```

##### 3.6.3.4 DATETRUNC

This topic describes the date function DATETRUNC and provides examples.

```
datetime datetrunc (datetime date,string datepart)
```

Description: This function truncates a **date** value to the accuracy specified by **datepart** and returns a new date. Parameters:
**date**: a date value of the DATE, DATETIME, or TIMESTAMP type. If the input value is of the STRING type, it is
implicitly converted into a value of the DATETIME type before the calculation. If the input value is of another data type, an error is returned.
**datepart**: a constant of the STRING type. This parameter supports extended date formats. If **datepart** is not in the
specified format or is of another data type, an error is returned. Return value: A value of the DATETIME type is returned. If an input value is NULL, NULL is returned.

```
datetrunc('2017-12-07 16:28:46', 'yyyy') = 2017-01-01 00:00:00 -- The function truncates the date value to the accuracy of the year 2017 and returns the date value that is ac curate to the year. In this example, the date value that is accurate to the year 2017 is returned. datetrunc('2017-12-07 16:28:46', 'month') = 2017-12-01 00:00:00 -- The function truncates the date value to the accuracy of the month December and returns the date value that is accurate to the month. In this example, the date value that is accurate to the month "2017-12" is returned. datetrunc('2017-12-07 16:28:46', 'DD') = 2017-12-07 00:00:00 -- The function truncates the date value to the accuracy of the day 07 and returns the date value that is accur ate to the day. In this example, the date value that is accurate to the day "2017-12-07" is returned.
```

##### 3.6.3.5 GETDATE

This topic describes the GETDATE function in date functions.

```
datetime getdate()
```

Description: This function returns the current system time as a date value. MaxCompute uses UTC+8 as the standard time zone. Return value: A value of the DATETIME type is returned. The value indicates the current date and time. In a MaxCompute SQL task that is executed in distributed mode, the **GETDATE** function always returns a fixed value. The return value is an arbitrary time during the execution of the MaxCompute SQL task. The time is accurate to seconds. In MaxCompute V2.0 that supports more data types, the time is accurate to milliseconds.

##### 3.6.3.6 ISDATE

This topic describes the ISDATE function in date functions.

```
boolean isdate(string date, string format)
```

Description: This function determines whether a date string can be converted into a date value in a specified format. If the date string can be converted into a date value in the specified format, True is returned. Otherwise, False is returned. Parameters:
**date**: a value of the STRING type. If the input value is of the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is
implicitly converted into a value of the STRING type before calculation. If the input value is of another data type, an error is returned.
**format**: a constant of the STRING type. This parameter does not support extended date formats. If the input value is
of another data type, an error is returned. If redundant format strings exist in **format**, this function converts the date string that corresponds to the first format string into a date value. The rest strings are considered delimiters. For example, **isdate("1234-yyyy", "yyyy-yyyy")** returns True. Return value: A value of the BOOLEAN type is returned. If an input value is NULL, NULL is returned.

##### 3.6.3.7 LASTDAY

This topic describes the LASTDAY function in date functions.

```
datetime lastday(datetime date)
```

Description: This function returns the last day of the month in which the **date** value falls. The value is accurate to days. The hour, minute, and second parts are expressed as **00:00:00**. Parameters: The **date** parameter supports a value of the DATETIME type. If the input value is of the STRING type, it is implicitly converted into a value of the DATETIME type before calculation. If the input value is of another data type, an error is returned. Return value: A value of the DATETIME type is returned. If the input value is NULL, NULL is returned.

##### 3.6.3.8 TO_DATE

This topic describes the TO_DATE function and provides examples of using this function.

```
datetime to_date(string date, string format)
```

Description: This function converts a **date** string in a specified **format** into a date value. Parameters:
**date**: a date value of the STRING type, which indicates the date string you want to convert. If the input value is of
the BIGINT, DOUBLE, DECIMAL, or DATETIME type, it is implicitly converted into a value of the STRING type before calculation. If the input value is of another data type or an empty string, an error is returned.
**format**: a constant of the STRING type, which indicates a date format. If the input value is not a constant or is not of
the STRING type, an error is returned. The Extended Date/Time Format (EDTF) is not supported. In this format, the characters are parsed as invalid characters and omitted. The value of this parameter must contain **yyyy**. Otherwise, an error is returned. If redundant format strings are included in the value of this parameter, only the date value that corresponds to the first format string is used, and the date values that correspond to the other format strings are parsed as delimiters. For example, **to_date('1234-2234 ', 'yyyy-yyyy ')** is parsed as **1234-01-01 00:00:00**. Return value: A value of the DATETIME type is returned and the value is in the format of **yyyy-mm-dd hh:mi:ss:ff3**. If the value of any input parameter is NULL, NULL is returned. In the format, yyyy indicates a 4-digit year, mm indicates a 2-digit month, dd indicates a 2-digit day, hh indicates an hour in 24-hour display, mi indicates a 2-digit minute, ss indicates a 2-digit second, and ff3 indicates a 3-digit millisecond.

```
to_date('Alibaba2017-12*03', 'Alibabayyyy-mm*dd') = 2017-12-03 00:00:00 to_date('20170718', 'yyyymmdd') = 2017-07-18 00:00:00 to_date('201707182030','yyyymmddhhmi')=2017-07-18 20:30:00 to_date('2017718', 'yyyymmdd') -- Invalid format. NULL is returned. to_date('Alibaba2017-12*3', 'Alibabayyyy-mm*dd') -- Invalid format. NULL is returned. to_date('2017-24-01', 'yyyy') -- Invalid format. NULL is returned. to_date('20181030 15-13-12.345','yyyymmdd hh-mi-ss.ff3')=2018-10-30 15:13:12
```

##### 3.6.3.9 TO_CHAR

This topic describes the TO_CHAR function and provides examples of using this function.

```
string to_char(datetime date, string format)
```

Description: This function converts a **date** value of the DATETIME type into a string in a specified **format**. Parameters:
**date**: a date value of the DATETIME type, which indicates the date value you want to convert. If the input value is of
the STRING type, it is implicitly converted into the DATETIME type before calculation. If the input value is not of the STRING type, an error is returned.
**format**: a constant of the STRING type. If it is not a constant or is not of the STRING type, an error is returned. In the
**format** parameter, the date format part is replaced by the related data and other characters remain unchanged in
the output. Return value: A value of the STRING type is returned. If the value of an input parameter is NULL, NULL is returned.

```
to_char('2017-12-03 00:00:00', 'Alibaba Cloud Financial Servicesyyyy-mm*dd') = 'Alibaba Cloud Financial Services2017-12*03' to_char('2017-07-18 00:00:00', 'yyyymmdd') = '20170718' to_char('Alibaba2017-12*3', 'Alibabayyyy-mm*dd') -- NULL is returned. to_char('2017-24-01', 'yyyy') -- NULL is returned. to_char('2017718', 'yyyymmdd') -- NULL is returned.
```

##### 3.6.3.10 UNIX_TIMESTAMP

This topic describes the UNIX_TIMESTAMP function and provides examples of using this function.

```
bigint unix_timestamp(datetime date)
```

Description: This function converts a **date** value to a UNIX timestamp that is an integer. Parameters: **date**: a date value of the DATETIME type. If the input value is of the STRING type, it is implicitly converted into a value of the DATETIME type before calculation. If the input value is not of the STRING type, an error is returned. If you enable new data types, the implicit conversion fails. In this case, you must use the CAST function for conversion, for example, **unix_timestamp(cast(... as datetime))**. Return value: A UNIX timestamp of the BIGINT type is returned. If the value of the input parameter is NULL, NULL is returned.

```
select unix_timestamp(datetime'2009-03-20 11:11:00'); -- 1237518660 is returned.
```

##### 3.6.3.11 FROM_UNIXTIME

This topic describes the FROM_UNIXTIME function and provides examples of using this function.

```
datetime from_unixtime(bigint unixtime)
```

Description: This function converts **unixtime** of the BIGINT type to a date value of the DATETIME type. Parameters: **unixtime**: a date value of the BIGINT type in the UNIX format. Its value is accurate to seconds. If the input value is of the STRING, DOUBLE, or DECIMAL type, it is implicitly converted into a value of the BIGINT type before calculation. Return value: A value of the DATETIME type is returned. If an input value is NULL, NULL is returned. In the Hive-compatible mode where set odps.sql.hive.compatible=true; has been run, if the value of the input parameter is of the STRING type, a date value of the STRING type is returned.

```
from_unixtime(123456789) = 1973-11-30 05:33:09;
```

##### 3.6.3.12 WEEKDAY

This topic describes the WEEKDAY function.

```
bigint weekday (datetime date)
```

Description: This function returns the day of the week for a specified **date**. Parameters: **date**: a date value of the DATETIME type. If the input value is of the STRING type, it is implicitly converted into a value of the DATETIME type before calculation. If the input value is not of the STRING type, an error is returned. Return value: A value of the BIGINT type is returned. If the value of the input parameter is NULL, NULL is returned. Monday is treated as the first day of a week and its return value is 0. Days are numbered in ascending order starting from 0. The return value for Sunday is 6.

##### 3.6.3.13 WEEKOFYEAR

This topic describes the WEEKOFYEAR function and provides examples of using this function.

```
bigint weekofyear(datetime date)
```

Description: This function returns the calendar week of the year that the specified date falls in. Monday is treated as the first day of a week. If a week spans two years, whether this week belongs to the previous year or the next year is based on which year contains more than four days. If more days fall in the previous year, the week is considered as the last week of the previous year. If more days fall in the next year, the week is considered as the first week of the next year. Parameters: **date**: a date value of the DATETIME type. If the value of the input parameter is of the STRING type, it is implicitly converted into a value of the DATETIME type before calculation. If the value of the input parameter is not of the STRING type, an error is returned. Return value: A value of the BIGINT type is returned. If the value of the input parameter is NULL, NULL is returned.

```
select weekofyear(to_date("20141229", "yyyymmdd")); -- The following result is returned: +------------+
| _c0        |
+------------+
| 1          |
+------------+ -- 20141229 is in year 2014, but most days of the week fall in year 2015. Therefore, the return value 1 indicates the first week of year 2015. select weekofyear(to_date("20141231", "yyyymmdd")); -- 1 is returned. select weekofyear(to_date("20151229", "yyyymmdd")); -- 53 is returned.
```

##### 3.6.3.14 Additional date functions

###### 3.6.3.14.1 Usage notes

This topic describes the configuration operation that you must perform before you use the date functions that are added to MaxCompute V2.0. MaxCompute V2.0 provides more date functions. You must add the following SET statement before the SQL statements for these new functions:

```
set odps.sql.type.system.odps2=true;
```

You must submit and execute the SET statement and the SQL statements for the new functions at the same time.

###### 3.6.3.14.2 YEAR

This topic describes the YEAR function and provides examples of using this function.

```
INT YEAR(DATETIME/STRING date)
```

Description: This function returns the year in which the specified **date** value falls. Parameters: **date**: a date value of the DATETIME or STRING type. The format of the date value must include **yyyy-mm-**
**dd** and exclude redundant strings. Otherwise, NULL is returned.
Return value: A value of the INT type is returned.

```
SELECT YEAR('1970-01-01 12:30:00'); -- 1970 is returned. SELECT YEAR('1970-01-01'); -- 1970 is returned. SELECT YEAR('70-01-01'); -- 70 is returned. SELECT YEAR('1970-01-01'); -- 1970 is returned. SELECT YEAR('1970/03/09'); -- NULL is returned. SELECT YEAR(null); -- An error is returned.
```

###### 3.6.3.14.3 QUARTER

This topic describes the QUARTER function and provides examples of using this function.

```
INT QUARTER (DATETIME/TIMESTAMP/STRING date)
```

Description: This function returns the quarter of the year for a date value. The quarter is an integer from 1 to 4. Parameters: **date**: a date value of the DATETIME, TIMESTAMP, or STRING type. The format of the date value must include **yyyy-mm-dd**. If the date value is not of the DATETIME, TIMESTAMP, or STRING type, NULL is returned. Return value: A value of the INT type is returned. If the value of an input parameter is NULL, NULL is returned.

```
SELECT QUARTER('1970-11-12 10:00:00'); -- 4 is returned. SELECT QUARTER('1970-11-12'); -- 4 is returned.
```

###### 3.6.3.14.4 MONTH

This topic describes the MONTH function and provides examples of using this function.

```
INT MONTH(DATETIME/STRING date)
```

Description: This function returns the month part of a date value. Parameters: **date**: a value of the DATETIME or STRING type. The date format must include **yyyy-mm-dd**. If it is not of the DATETIME or STRING type, an error is returned. Return value: A value of the INT type is returned.

```
SELECT MONTH('2014-09-01'); -- 9 is returned. SELECT MONTH('20140901'); -- NULL is returned.
```

###### 3.6.3.14.5 DAY

The DAY function returns the day of a specified date value. This topic describes the DAY function and provides examples of using this function.

```
INT DAY(DATETIME/STRING date)
```

Description: This function returns the day of a specified date value. Parameters: **date**: a date value of the DATETIME or STRING type. The format of the date value can be **yyyy-mm-dd** or
**yyyy-mm-dd hh:mi:ss**. If the date value is not of the DATETIME or STRING type, an error is returned.
Return value: A value of the INT type is returned.

```
SELECT DAY('2014-09-01'); -- 1 is returned. SELECT DAY('20140901'); -- NULL is returned.
```

###### 3.6.3.14.6 DAYOFMONTH

This topic describes the DAYOFMONTH function and provides examples on how to use this function. DAYOFMONTH returns the day component of a date value. Syntax

```
int dayofmonth(date)
```

Description: This function returns the day component of a date value. For example, if the date is October 13, 2019, 13 is returned after you run the `int dayofmonth(2019-10-13)` command. Parameters: **date**: a date value of the STRING type. The date format must include **yyyy-mm-dd**. If it is not of the STRING type, an error is returned. Return value: A value of the INT type is returned.

```
dayofmonth('2019-09-01'); -- The return value is 1. dayofmonth('20190901'); -- The return value is null.
```

###### 3.6.3.14.7 HOUR

This topic describes the HOUR function and provides examples of using this function.

```
INT HOUR(DATETIME/STRING date)
```

Description: This function returns the value of the hour part of a date. Parameters: **date**: a value of the DATETIME or STRING type. If the value is not of the DATETIME or STRING type, an error is returned. Return value: A value of the INT type is returned.

```
SELECT HOUR('2014-09-01 12:00:00'); -- 12 is returned. SELECT HOUR('12:00:00'); -- 12 is returned. SELECT HOUR('20140901120000'); -- NULL is returned.
```

###### 3.6.3.14.8 MINUTE

This topic describes the MINUTE function and provides examples of using this function.

```
INT MINUTE(DATETIME/STRING date)
```

Description: This function returns the value of the minute part of a date. Parameters: **date**: a value of the DATETIME or STRING type. If the value is not of the DATETIME or STRING type, an error is returned. Return value: A value of the INT type is returned.

```
SELECT MINUTE('2014-09-01 12:30:00'); -- 30 is returned. SELECT MINUTE('12:30:00'); -- 30 is returned. SELECT MINUTE('20140901120000'); -- NULL is returned.
```

###### 3.6.3.14.9 SECOND

This topic describes the SECOND function and provides examples of using this function.

```
INT SECOND(DATETIME/STRING date)
```

Description: This function returns the value of the second part of a date value. Parameters: **date**: a date value of the DATETIME or STRING type. If it is not of the DATETIME or STRING type, an error is returned. Return value: A value of the INT type is returned.

```
SELECT SECOND('2014-09-01 12:30:45'); -- 45 is returned. SELECT SECOND('12:30:45'); -- 45 is returned. SELECT SECOND('20140901123045'); -- NULL is returned.
```

###### 3.6.3.14.10 FROM_UTC_TIMESTAMP

This topic describes the FROM_UTC_TIMESTAMP function and provides examples of using this function.

```
timestamp from_utc_timestamp({any primitive type}*, string timezone)
```

Description: This function converts a UTC timestamp to a timestamp for a specified time zone. Parameters: {any primitive type}*: the timestamp, which is a value of the TIMESTAMP, DATETIME, TINYINT, SMALLINT, INT, or BIGINT type. If the value is of the TINYINT, SMALLINT, INT, or BIGINT type, the unit is milliseconds.
**timezone**: the time zone to which you want to convert the timestamp, such as Pacific Standard Time (PST).
Return value: A value of the TIMESTAMP type is returned.

```
SELECT from_utc_timestamp(1501557840000, 'PST'); -- The unit of the input value is milliseconds and 2017-08-01 04:24:00 is returned. SELECT from_utc_timestamp('1970-01-30 16:00:00','PST'); -- 1970-01-30 08:00:00.0 is returned. SELECT from_utc_timestamp('1970-01-30','PST'); -- 1970-01-29 16:00:00.0 is returned.
```

###### 3.6.3.14.11 CURRENT_TIMESTAMP

This topic describes the CURRENT_TIMESTAMP function and provides examples of using this function.

```
timestamp current_timestamp()
```

Description: This function returns the current timestamp. The return value is not fixed. Return value: A value of the TIMESTAMP type is returned.

```
select current_timestamp(); -- '2017-08-03 11:50:30.661' is returned.
```

###### 3.6.3.14.12 ADD_MONTHS

This topic describes the ADD_MONTHS function and provides examples of using this function.

```
string add_months(string startdate, int nummonths)
```

Description: This function adds a specified number of months to a date specified by **startdate**. The number of months is specified by **nummonths**. Parameters:
**startdate**: a date value of the STRING type. The date format must contain **yyyy-mm-dd**. Otherwise, NULL is
returned.
**num_months**: a value of the INT type.
Return value: A value of the STRING type is returned and the value is in the format of **yyyy-mm-dd**.

```
add_months('2017-02-14',3) = '2017-05-14' add_months('17-2-14',3) = '0017-05-14' add_months('2017-02-14 21:30:00',3) = '2017-05-14' add_months('20170214',3) = null
```

###### 3.6.3.14.13 LAST_DAY

This topic describes the LAST_DAY function and provides examples of using this function.

```
string last_day(string date)
```

Description: This function returns the last date of the month part of a date value. Parameters: **date**: a date value of the STRING type and in the format of **yyyy-mm-dd hh:mi:ss** or **yyyy-mm-dd**. Return value: A value of the STRING type is returned and the value is in the format of **yyyy-mm-dd**.

```
last_day('2017-03-04') = '2017-03-31' last_day('2017-07-04 11:40:00') = '2017-07-31' last_day('20170304') = null
```

###### 3.6.3.14.14 NEXT_DAY

This topic describes the NEXT_DAY function and provides examples of using this function.

```
string next_day(string startdate, string week)
```

Description: This function returns the date of the first day that is later than **startdate** and matches the **week** value. The return value indicates the date of the specified day in the next week. Parameters:
**startdate**: a date value of the STRING type and in the format of **yyyy-mm-dd hh:mi:ss** or **yyyy-mm-dd**.
**week**: a date value of the STRING type. The full name of a day in a week, or the first two or three letters of the day,
for example, MO, TUE, or FRIDAY. Return value: A value of the STRING type is returned and the value is in the format of **yyyy-mm-dd**.

```
next_day('2017-08-01','TU') = '2017-08-08' next_day('2017-08-01 23:34:00','TU') = '2017-08-08' next_day('20170801','TU') = null
```

###### 3.6.3.14.15 MONTHS_BETWEEN

This topic describes the MONTHS_BETWEEN function and provides examples of using this function.

```
double months_between(datetime/timestamp/string date1, datetime/timestamp/string date2)
```

Description: This function returns the number of months between **date1** and **date2**. Parameters:
**date1**: a value of the DATETIME, TIMESTAMP, or STRING type. The value is in the format of **yyyy-mm-dd hh:mi:ss**
or **yyyy-mm-dd**.
**date2**: a value of the DATETIME, TIMESTAMP, or STRING type. The value is in the format of **yyyy-mm-dd hh:mi:ss**
or **yyyy-mm-dd**. Return value: A value of the DOUBLE type is returned. If **date1** is later than **date2**, a positive value is returned. If **date2** is later than **date1**, a negative value is returned. If both **date1** and **date2** correspond to the last days of two months, the return value is an integer that represents the number of months. Otherwise, the return value is computed by using the following formula: **date1** - **date2**)/31

```
months_between('1997-02-28 10:30:00', '1996-10-30') = 3.9495967741935485 months_between('1996-10-30','1997-02-28 10:30:00' ) = -3.9495967741935485 months_between('1996-09-30','1996-12-31') = -3.0
```

###### 3.6.3.14.16 EXTRACT

This topic describes the EXTRACT function and provides examples of using this function.

```
int extract(<datepart> from <timestamp>)
```

Description: This function extracts the part specified by **datepart** from the time specified by **timestamp**. Parameters:
**datepart**: a value that can be set to YEAR, MONTH, DAY, HOUR, or MINUTE.
**timestamp**: a date value of the TIMESTAMP type.
Return value: A value of the INT type is returned.

```
set odps.sql.type.system.odps2=true; select extract(year from '2019-05-01 11:21:00') year
         ,extract(month from '2019-05-01 11:21:00') month
         ,extract(day from '2019-05-01 11:21:00') day
         ,extract(hour from '2019-05-01 11:21:00') hour
         ,extract(minute from '2019-05-01 11:21:00') minute;
-- The following result is returned: +------+-------+------+------+--------+
| year | month | day  | hour | minute |
+------+-------+------+------+--------+
| 2019 | 5     | 1    | 11   | 21     |
+------+-------+------+------+--------+
```

If the time value specified in the SQL statement is invalid or exceeds the specified range, the return value is the remainder obtained by dividing the specified time value by the maximum value in the time range.

```
set odps.sql.type.system.odps2=true; select extract(hour from '2019-05-01 31:01:01') hour
         ,extract(minute from '2019-05-01 23:61:01') minute;
-- The following result is returned: +------+-------+
| hour | minute|
+------+-------+
| 7    | 1     |
+------+-------+ -- The maximum value of the hour part is 24, and the specified time value is 31. The return value is 7 (31/24). -- The maximum value of the minute part is 60, and the specified time value is 61. The return value is 1 (61/60
```

`).`

#### 3.6.4 Window functions

##### 3.6.4.1 Overview

In MaxCompute SQL, window functions can be used for flexible data analysis and processing. This topic describes the precautions for using window functions and the syntax of window functions.

**Important**

Window functions can only be included in the SELECT clause. A window function cannot contain nested window functions or aggregate functions. Window functions cannot be used with aggregate functions of the same level. A maximum of five window functions can be used in a MaxCompute SQL statement.

```
window_func() over (partition by [col1,col2…] [order by [col1[asc|desc], col2[asc|desc]…]] windowing_clause)
```

Parameters:
**PARTITION BY**: the columns in the window that is used for calculation. Rows with the same values of the partition
key columns are considered in the same window. A window can contain a maximum of 100 million rows of data. We recommend that the number of rows in a window not exceed 5 million. If the number of rows exceeds 5 million, an error is returned.
**ORDER BY**: specifies how to sort data in a window.
**windowing_clause**: You can use **ROWS** to specify how to define the window for the function. Valid values:
**rows between x preceding|following and y preceding|following**: indicates a window that ranges from the
xth row preceding or following the current row to the yth row preceding or following the current row.
**rows x preceding|following**: indicates a window that ranges from the xth row preceding or following the current
row to the current row. x and y must be integer constants greater than or equal to 0. Their values range from 0 to 10000. 0 indicates the current row. You must specify **ORDER BY** before you use **ROWS** to specify a window range. Window functions that allow you to use **rows** to define the window include AVG, COUNT, MAX, MIN, STDDEV, and SUM.

##### 3.6.4.2 COUNT

This topic describes the COUNT function and provides examples of using this function.

```
Bigint count([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function returns the counted values of specified rows. Parameters:
**expr**: a value of any data type. If the value for a row is NULL, this row is not used for calculation. If the **distinct**
keyword is specified, only the distinct values are counted.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the counted value of **expr** in the current
window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the value accumulated from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: A value of the BIGINT type is returned. The test_src table contains the **user_id** column of the BIGINT type.

```
select user_id,count(user_id) over (partition by user_id) as count from test_src; +---------+------------+
| user_id |  count     |
+---------+------------+
| 1       | 3          |
| 1       | 3          |
| 1       | 3          |
| 2       | 1          |
| 3       | 1          |
+---------+------------+ +---------+------------+ -- If ORDER BY is not specified, the counted value of the user_id column in the current window is returned. select user_id,count(user_id) over (partition by user_id order by user_id) as count from test_src; +---------+------------+
| user_id | count      |
+---------+------------+
| 1       | 1          |      -- This row is the starting row of this window.
| 1       | 2          |      -- Two rows are found from the starting row to the current row. 2 is returned.
| 1       | 3          |
| 2       | 1          |
| 3       | 1          |
+---------+------------+ -- If ORDER BY is specified, the counted value from the starting row to the current row in the current window i s returned.
```

If duplicate values are specified for **ORDER BY**, the processing method is based on the compatibility between MaxCompute and Hive. If MaxCompute is not compatible with Hive, the value of COUNT for each row is returned.

```
set odps.sql.hive.compatible=false; select user_id, price, count(price) over
  (partition by user_id order by price) as count from test_src;
+------------+------------+------------+
| user_id    | price      | count      |
+------------+------------+------------+
| 1          | 4.5        | 1          |  -- This row is the starting row of this window.
| 1          | 5.5        | 2          |  -- The value of COUNT for the second row is 2.
| 1          | 5.5        | 3          |  -- The value of COUNT for the third row is 3.
| 1          | 6.5        | 4          |
| 2          | NULL       | 0          |
| 2          | 3.0        | 1          |
| 3          | NULL       | 0          |
| 3          | 4.0        | 1          |
+------------+------------+------------+
```

If MaxCompute is compatible with Hive, the return value is the value of COUNT for the last row of the rows with the same value.

```
set odps.sql.hive.compatible=true; select user_id, price, count(price) over
  (partition by user_id order by price) as count from test_src;
+------------+------------+------------+
| user_id    | price      | count      |
+------------+------------+------------+
| 1          | 4.5        | 1          | -- This row is the starting row of this window.
| 1          | 5.5        | 3          | -- The value of COUNT for the second row is the same as the value of
COUNT for the third row because the prices of the two rows are the same.
| 1          | 5.5        | 3          | -- The value of COUNT for the third row is 3.
| 1          | 6.5        | 4          |
| 2          | NULL       | 0          |
| 2          | 3.0        | 1          |
| 3          | NULL       | 0          |
| 3          | 4.0        | 1          |
+------------+------------+------------+
```

##### 3.6.4.3 AVG

This topic describes the AVG function and provides examples of using this function.

```
avg([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function returns the average value of input values in specified rows. Parameters:
**expr**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. If the input value for a row is NULL, the row is not used for calculation. Values of the BOOLEAN type are not used for calculation. If the **distinct** keyword is specified, the average value of distinct values is calculated.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the average value of all values in the
current window is returned. If **ORDER BY** is specified, the returned results are sorted in a specified order and the accumulated average value of the values from the starting row to the current row is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: A value of the DOUBLE type is returned. If duplicate values are specified for **ORDER BY**, the processing method is based on the compatibility between MaxCompute and Hive. If MaxCompute is not compatible with Hive, the return value is the average value for each row.

```
set odps.sql.hive.compatible=false; select user_id, price, avg(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+-------------------+
| user_id    | price      | _c2               |
+------------+------------+-------------------+
| 1          | 4.5        | 4.5               |    -- This row is the starting row of this window.
| 1          | 5.5        | 5.0               |    -- The return value is the average value of the values for
the first and second rows.
| 1          | 5.5        | 5.166666666666667 |    -- The return value is the average value of the values from
the first row to the third row.
| 1          | 6.5        | 5.5               |
| 2          | NULL       | NULL              |
| 2          | 3.0        | 3.0               |
| 3          | NULL       | NULL              |
| 3          | 4.0        | 4.0               |
+------------+------------+-------------------+
```

If MaxCompute is compatible with Hive, the return value is the average value of values for the last row of the rows with the same value.

```
set odps.sql.hive.compatible=true; select user_id, price, avg(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+-------------------+
| user_id    | price      | _c2               |
+------------+------------+-------------------+
| 1          | 4.5        | 4.5               |  -- This row is the starting row of this window.
| 1          | 5.5        | 5.166666666666667 |  -- The return value is the average value of values from the f
irst row to the third row.
| 1          | 5.5        | 5.166666666666667 |  -- The return value is the average value of values from the f
irst row to the third row.
| 1          | 6.5        | 5.5               |
| 2          | NULL       | NULL              |
| 2          | 3.0        | 3.0               |
| 3          | NULL       | NULL              |
| 3          | 4.0        | 4.0               |
+------------+------------+-------------------+
```

##### 3.6.4.4 MAX

This topic describes the MAX function.

```
max([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function calculates the maximum value of specified rows in the current window. Parameters:
**expr**: a value of any data type except BOOLEAN. If the value for a row is NULL, this row is not used for calculation. If
the **distinct** keyword is specified, the maximum value of distinct values is calculated. The calculation result is not affected regardless of whether the parameter is specified.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the maximum value of all values in the
current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the maximum value of values from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: A value of the same data type as **expr** is returned.

##### 3.6.4.5 MIN

This topic describes the MIN function.

```
min([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function returns the minimum value of values in specified rows. Parameters:
**expr**: a value of any data type except BOOLEAN. If the value for a row is NULL, the row is not used for calculation. If
the **distinct** keyword is specified, the minimum value of distinct values is calculated. The calculation result is not affected regardless of whether the parameter is specified.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the minimum value in the current
window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the minimum value of values from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: A value of the same data type as **expr** is returned.

##### 3.6.4.6 MEDIAN

This topic describes the MEDIAN function.

```
double median(double number1,number2...) over(partition by [col1, col2…]) decimal median(decimal number1,number2...) over(partition by [col1, col2…])
```

Description: This function calculates the median. Parameters:
**number1,number2...**: numbers of the DOUBLE or DECIMAL type. You can enter 1 to 255 numbers. At least one
number is required. If the input value is of the DOUBLE type, it is automatically converted into an array of the DOUBLE type before calculation. If the input value is of the STRING or BIGINT type, it is implicitly converted into the DOUBLE type before calculation. If it is not of the STRING or BIGINT type, an error is returned. If the input value is NULL, NULL is returned.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
Return value: A value of the DOUBLE or DECIMAL type is returned.

##### 3.6.4.7 STDDEV

This topic describes the STDDEV function and provides examples of using this function.

```
Double stddev([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause]) Decimal stddev([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function calculates the population standard deviation of values in specified rows. Parameters:
**expr**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. If the value for a row is NULL, this row is not used for calculation. If the **distinct** keyword is specified, the population standard deviation of distinct values is calculated.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the population standard deviation of
rows in the current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the population standard deviation from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: If the input value is of the DECIMAL type, a value of the DECIMAL type is returned. Otherwise, a value of the DOUBLE type is returned.

```
select window, seq, stddev_pop('1\01') over (partition by window order by seq) from dual;
```

If duplicate values are specified for **ORDER BY**, the processing method is based on the compatibility between MaxCompute and Hive. If MaxCompute is not compatible with Hive, the return value is the value of STDDEV for each row.

```
set odps.sql.hive.compatible=false; select user_id, price, stddev(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+--------------------+
| user_id    | price      | _c2                |
+------------+------------+--------------------+
| 1          | 4.5        | 0.0                |  -- This row is the starting row of this window.
| 1          | 5.5        | 0.5                |  -- The return value is the value of STDDEV for the first and
second rows.
| 1          | 5.5        | 0.4714045207910316 |  -- The return value is the value of STDDEV from the first ro
w to the third row.
| 1          | 6.5        | 0.7071067811865475 |
| 2          | NULL       | NULL               |
| 2          | 3.0        | 0.0                |
| 3          | NULL       | NULL               |
| 3          | 4.0        | 0.0                |
+------------+------------+--------------------+
```

If MaxCompute is compatible with Hive, the return value is the value of STDDEV for the last row of the rows with the same value.

```
set odps.sql.hive.compatible=true; select user_id, price, stddev(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+--------------------+
| user_id    | price      | _c2                |
+------------+------------+--------------------+
| 1          | 4.5        | 0.0                | -- This row is the starting row of this window.
| 1          | 5.5        | 0.4714045207910316 | -- The return value is the value of STDDEV from the first row
to the third row.
| 1          | 5.5        | 0.4714045207910316 | -- The return value is the value of STDDEV from the first row
to the third row.
| 1          | 6.5        | 0.7071067811865475 |
| 2          | NULL       | NULL               |
| 2          | 3.0        | 0.0                |
| 3          | NULL       | NULL               |
| 3          | 4.0        | 0.0                |
+------------+------------+--------------------+
```

##### 3.6.4.8 STDDEV_SAMP

This topic describes the STDDEV_SAMP function.

```
Double stddev_samp([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause]) Decimal stddev_samp([distinct] expr) over((partition by [col1,col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function calculates the sample standard deviation. Parameters:
**expr**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly
converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. If the value for a row is NULL, the row is not used for calculation. If the **distinct** keyword is specified, the sample standard deviation of distinct values is calculated.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the sample standard deviation in the
current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the sample standard deviation from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: If the input value is of the DECIMAL type, a value of the DECIMAL type is returned. Otherwise, a value of the DOUBLE type is returned.

##### 3.6.4.9 SUM

This topic describes the SUM function and provides examples of using this function.

```
sum([distinct] expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function returns the sum of values in specified rows. Parameters:
**expr**: a value of the DOUBLE, DECIMAL, or BIGINT type. If the input value is of the STRING type, it is implicitly
converted to the DOUBLE type before calculation. If it is not of the STRING type, an error is returned. If the value for a row is NULL, the row is not used for calculation. If the **distinct** keyword is specified, the sum of distinct values is calculated.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the sum of the **expr** values in the current
window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the sum of the values from the starting row to the current row in the current window is returned. If the **distinct** keyword is specified, **ORDER BY** cannot be used. Return value: If the input value is of the BIGINT type, a value of the BIGINT type is returned. If the input value is of the DECIMAL type, a value of the DECIMAL type is returned. If the input value is of the DOUBLE or STRING type, a value of the DOUBLE type is returned. If duplicate values are specified for **ORDER BY**, the processing method is based on the compatibility between MaxCompute and Hive. If MaxCompute is not compatible with Hive, the return value is the sum of values for each row.

```
set odps.sql.hive.compatible=false; select user_id, price, sum(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+------------+
| user_id    | price      | _c2        |
+------------+------------+------------+
| 1          | 4.5        | 4.5        |  -- This row is the starting row of this window.
| 1          | 5.5        | 10.0       |  -- The return value is the sum of values for the first and second ro
ws.
| 1          | 5.5        | 15.5       |  -- The return value is the sum of values from the first row to the t
hird row.
| 1          | 6.5        | 22.0       |
| 2          | NULL       | NULL       |
| 2          | 3.0        | 3.0        |
| 3          | NULL       | NULL       |
| 3          | 4.0        | 4.0        |
+------------+------------+------------+
```

If MaxCompute is compatible with Hive, the return value is the sum of values for the last row of the rows with the same value.

```
set odps.sql.hive.compatible=true; select user_id, price, sum(price) over
  (partition by user_id order by price) from test_src;
+------------+------------+------------+
| user_id    | price      | _c2        |
+------------+------------+------------+
| 1          | 4.5        | 4.5        |  -- This row is the starting row of this window.
| 1          | 5.5        | 15.5       |  -- The return value is the sum of values from the first row to the t
hird row.
| 1          | 5.5        | 15.5       |  -- The return value is the sum of values from the first row to the t
hird row.
| 1          | 6.5        | 22.0       |
| 2          | NULL       | NULL       |
| 2          | 3.0        | 3.0        |
| 3          | NULL       | NULL       |
| 3          | 4.0        | 4.0        |
+------------+------------+------------+
```

##### 3.6.4.10 DENSE_RANK

This topic describes the DENSE_RANK function and provides examples of using this function.

```
Bigint dense_rank() over(partition by [col1, col2…] order by [col1[asc|desc], col2[asc|desc]…])
```

Description: This function returns the ranking of values. The data in rows with the same column value in ORDER BY has the same ranking. Parameters:
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: the value on which the ranking values are based.
Return value: A value of the BIGINT type is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Group employees by department, sort the employees in each group in descending order of **sal**, and then obtain the rankings of employees in each group.

```
select deptno
        , ename
        , sal
        , dense_rank() over (partition by deptno order by sal desc) as nums
-- DEPTNO (department) is the column in the window that is used for calculation. Values in the sal column are s orted to generate the ranking of each employee.
    from emp;
-- The following result is returned: +------------+-------+------------+------------+
| deptno     | ename | sal        | nums       |
+------------+-------+------------+------------+
| 10         | JACCKA | 5000.0     | 1          |
| 10         | KING  | 5000.0     | 1          |
| 10         | CLARK | 2450.0     | 2          |
| 10         | WELAN | 2450.0     | 2          |
| 10         | TEBAGE | 1300.0     | 3          |
| 10         | MILLER | 1300.0     | 3          |
| 20         | SCOTT | 3000.0     | 1          |
| 20         | FORD  | 3000.0     | 1          |
| 20         | JONES | 2975.0     | 2          |
| 20         | ADAMS | 1100.0     | 3          |
| 20         | SMITH | 800.0      | 4          |
| 30         | BLAKE | 2850.0     | 1          |
| 30         | ALLEN | 1600.0     | 2          |
| 30         | TURNER | 1500.0     | 3          |
| 30         | MARTIN | 1250.0     | 4          |
| 30         | WARD  | 1250.0     | 4          |
| 30         | JAMES | 950.0      | 5          |
+------------+-------+------------+------------+
```

##### 3.6.4.11 RANK

This topic describes the RANK function and provides examples of using this function.

```
Bigint rank() over(partition by [col1, col2…] order by [col1[asc|desc], col2[asc|desc]…])
```

Description: This function determines the ranking of values in rows with the same column value, after the values are sorted in descending order by using the ORDER BY clause. Parameters:
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: the field based on which values are ranked.
Return value: A value of the BIGINT type is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Group employees by department, sort the employees in each group in descending order of **sal**, and then obtain the ranking values of employees in each group.

```
select deptno
        , ename
        , sal
        , rank() over (pratition by deptno order by sal desc) as nums
-- DEPTNO (department) is the column in the window that is used for calculation. Values in the sal column are s orted to generate the ranking value for each employee.
    from emp;
-- The following result is returned: +------------+-------+------------+------------+
| deptno     | ename | sal        | nums       |
+------------+-------+------------+------------+
| 10         | JACCKA | 5000.0     | 1          |
| 10         | KING  | 5000.0     | 1          |
| 10         | CLARK | 2450.0     | 3          |
| 10         | WELAN | 2450.0     | 3          |
| 10         | TEBAGE | 1300.0     | 5          |
| 10         | MILLER | 1300.0     | 5          |
| 20         | SCOTT | 3000.0     | 1          |
| 20         | FORD  | 3000.0     | 1          |
| 20         | JONES | 2975.0     | 3          |
| 20         | ADAMS | 1100.0     | 4          |
| 20         | SMITH | 800.0      | 5          |
| 30         | BLAKE | 2850.0     | 1          |
| 30         | ALLEN | 1600.0     | 2          |
| 30         | TURNER | 1500.0     | 3          |
| 30         | MARTIN | 1250.0     | 4          |
| 30         | WARD  | 1250.0     | 4          |
| 30         | JAMES | 950.0      | 6          |
+------------+-------+------------+------------+
```

##### 3.6.4.12 LAG

This topic describes the LAG function and provides examples of using this function.

```
lag(expr, Bigint offset, default) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]])
```

Description: This function returns the values for a row at a given offset before the current row. For example, if the current row is **rn**, the values for the **rn - offset**th row are returned. Parameters:
**expr**: a value of any data type.
**offset**: the offset, which is a constant of the BIGINT type. The value of the offset must be greater than 0. If the input
value is of the STRING or DOUBLE type, it is implicitly converted into the BIGINT type before calculation.
**default**: The default value when the **offset** is out of the valid range. The value of this parameter must be a
constant. The default value of this parameter is NULL.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by col1[asc|desc], col2[asc|desc]**: specifies how values in the rows are sorted.
Return value: A value of the same data type as **expr** is returned.

```
select seq, lag(seq+100, 1) over (partition by window order by seq) as r from sliding_window; -- The following result is returned: +------------+------------+
| seq        | r          |
+------------+------------+
| 0          | NULL       |
| 1          | 100        |
| 2          | 101        |
| 3          | 102        |
| 4          | 103        |
| 5          | 104        |
| 6          | 105        |
| 7          | 106        |
| 8          | 107        |
| 9          | 108        |
+------------+------------+
```

##### 3.6.4.13 LEAD

This topic describes the LEAD function and provides examples on how to use this function.

**Syntax**

```
lead(expr,Bigint offset, default) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]])
```

**Description**

Returns the value of expr that corresponds to the Nth row following the current row at a given `offset` . The expression expr can be a column, a column operation, or a function operation.

**Parameters**

**expr**: a value of any data type.
**offset**: the offset, which is a constant of the BIGINT type. The value of the offset must be greater than 0. If the input
value is of the STRING or DOUBLE type, it is implicitly converted into the BIGINT type.
**default**: a constant. The default value when the **offset** is out of the valid range. The default value of this parameter
is NULL.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by col1[asc|desc], col2[asc|desc]**: specifies how values in the rows are sorted.

**Return value**

A value of the same data type as **expr** is returned.

**Sample data**

This section provides sample source data and examples for you to understand how to use the functions. Create a table named emp and insert the sample data into the table. Sample commands:

```
create table if not exists emp
   (empno bigint,
    ename string,
    job string,
    mgr bigint,
    hiredate datetime,
    sal bigint,
    comm bigint,
    deptno bigint);
tunnel upload emp.txt emp; -- Replace emp.txt with the actual path (path and name) to which you upload the data file.
```

The emp.txt file contains the following sample data:

```
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Group all employees based on the deptno column and calculate the value of sal for each employee at a given offset. Sample statements:

```
select deptno, ename, sal, lead(sal, 1) over (partition by deptno order by sal) as sal_new from emp;
```

The following result is returned:

```
+------------+------------+------------+------------+
| deptno     | ename      | sal        | sal_new    |
+------------+------------+------------+------------+
| 10         | TEBAGE     | 1300       | 1300       |
| 10         | MILLER     | 1300       | 2450       |
| 10         | CLARK      | 2450       | 2450       |
| 10         | WELAN      | 2450       | 5000       |
| 10         | KING       | 5000       | 5000       |
| 10         | JACCKA     | 5000       | NULL       |
| 20         | SMITH      | 800        | 1100       |
| 20         | ADAMS      | 1100       | 2975       |
| 20         | JONES      | 2975       | 3000       |
| 20         | SCOTT      | 3000       | 3000       |
| 20         | FORD       | 3000       | NULL       |
| 30         | JAMES      | 950        | 1250       |
| 30         | MARTIN     | 1250       | 1250       |
| 30         | WARD       | 1250       | 1500       |
| 30         | TURNER     | 1500       | 1600       |
| 30         | ALLEN      | 1600       | 2850       |
| 30         | BLAKE      | 2850       | NULL       |
+------------+------------+------------+------------+
```

##### 3.6.4.14 PERCENT_RANK

This topic describes the PERCENT_RANK function.

```
percent_rank() over(partition by [col1, col2…] order by [col1[asc|desc], col2[asc|desc]…])
```

Description: This function returns the relative percent rank of a row in a group of data. Parameters:
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by col1[asc|desc], col2[asc|desc]**: the value that is used to calculate the percent rank.
Return value: A value of the DOUBLE type is returned. Valid values: [0,1]. The relative percent rank is calculated by using the following formula: **(Rank - 1)/(Number of rows - 1)** The number of rows in a single window cannot exceed 10 million.

##### 3.6.4.15 ROW_NUMBER

This topic describes the ROW_NUMBER function and provides examples of using this function.

```
row_number() over(partition by [col1, col2…] order by [col1[asc|desc], col2[asc|desc]…])
```

Description: This function returns the ordinal number of the current row within a group of rows, counting from 1. Parameters:
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: the values that need to be sorted to return the ordinal number of the
current row. Return value: A value of the BIGINT type is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Group employees by department, sort the employees in each group in descending order of **sal**, and then obtain the ordinal numbers of employees in each group.

```
select deptno
        , ename
        , sal
        , row_number() over (partition by deptno order by sal desc) as nums
-- DEPTNO (department) is the column in the window that is used for calculation. Values in the sal column are s orted to return the ordinal number of the current row.
    from emp;
-- The following result is returned: +------------+-------+------------+------------+
| deptno     | ename | sal        | nums       |
+------------+-------+------------+------------+
| 10         | JACCKA | 5000.0     | 1          |
| 10         | KING  | 5000.0     | 2          |
| 10         | CLARK | 2450.0     | 3          |
| 10         | WELAN | 2450.0     | 4          |
| 10         | TEBAGE | 1300.0     | 5          |
| 10         | MILLER | 1300.0     | 6          |
| 20         | SCOTT | 3000.0     | 1          |
| 20         | FORD  | 3000.0     | 2          |
| 20         | JONES | 2975.0     | 3          |
| 20         | ADAMS | 1100.0     | 4          |
| 20         | SMITH | 800.0      | 5          |
| 30         | BLAKE | 2850.0     | 1          |
| 30         | ALLEN | 1600.0     | 2          |
| 30         | TURNER | 1500.0     | 3          |
| 30         | MARTIN | 1250.0     | 4          |
| 30         | WARD  | 1250.0     | 5          |
| 30         | JAMES | 950.0      | 6          |
+------------+-------+------------+------------+
```

##### 3.6.4.16 CLUSTER_SAMPLE

This topic describes the CLUSTER_SAMPLE function and provides examples of using this function.

```
boolean cluster_sample([Bigint x, Bigint y]) over(partition by [col1, col2..])
```

Description: This function performs cluster sampling. Parameters:
**x**: a constant of the BIGINT type. The value of this parameter must be greater than or equal to 1. If **y** is specified, **x**
indicates that a window is divided into **x** portions. Otherwise, **x** indicates that the records of **x** rows in a window are extracted. In this case, True is returned for the **x** rows. If the value of **x** is NULL, NULL is returned.
**y**: a constant of the BIGINT type. The value of y must be greater than or equal to 1 and less than or equal to x. y
indicates that **y** records of the **x** portions in a window are extracted. In this case, True is returned for the **y** records. If the value of **y** is NULL, NULL is returned.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
Return value: A value of the BOOLEAN type is returned. The test_tbl table contains two columns: **key** and **value**. **key** specifies a group, which can be **groupa** or **groupb**.
**value** indicates the value of key. Data in the test_tbl table:

```
+------------+--------------------+
| key        | value              |
+------------+--------------------+
| groupa     | -1.34764165478145  |
| groupa     | 0.740212609046718  |
| groupa     | 0.167537127858695  |
| groupa     | 0.630314566185241  |
| groupa     | 0.0112401388646925 |
| groupa     | 0.199165745875297  |
| groupa     | -0.320543343353587 |
| groupa     | -0.273930924365012 |
| groupa     | 0.386177958942063  |
| groupa     | -1.09209976687047  |
| groupb     | -1.10847690938643  |
| groupb     | -0.725703978381499 |
| groupb     | 1.05064697475759   |
| groupb     | 0.135751224393789  |
| groupb     | 2.13313102040396   |
| groupb     | -1.11828960785008  |
| groupb     | -0.849235511508911 |
| groupb     | 1.27913806620453   |
| groupb     | -0.330817716670401 |
| groupb     | -0.300156896191195 |
| groupb     | 2.4704244205196    |
| groupb     | -1.28051882084434  |
+------------+--------------------+
```

If you want to extract a sample of 10% of the values from each group, execute the following MaxCompute SQL statement:

```
select key, value from (select key, value, cluster_sample(10, 1) over(partition by key) as flag from tbl) sub w here flag = true; -- The following result is returned: +--------+--------------------+
| key    | value              |
+--------+--------------------+
| groupa | -0.273930924365012  |
| groupb | -1.11828960785008 |
+-----+-----------------------
```

##### 3.6.4.17 NTILE

This topic describes the NTILE function and provides examples of using this function.

```
BIGINT ntile(BIGINT n) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause]))
```

Description: This function divides rows into **n** ranking groups of as equal size as possible and returns the ranking group that a given row falls into. If rows are not evenly divided into ranking groups, more rows are included in the first ranking group. Parameters: **n**: a value of the BIGINT type. Return value: A value of the BIGINT type is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Classify all employees into three groups by department, sort employees in each group in descending order of **sal**, and then obtain the ranking groups of employees in each group.

```
select deptno,ename,sal,ntile(3) over(partition by deptno order by sal desc) as nt3 from emp; -- The following result is returned: +------------+-------+------------+------------+
| deptno     | ename | sal        | nt3        |
+------------+-------+------------+------------+
| 10         | JACCKA | 5000.0     | 1          |
| 10         | KING  | 5000.0     | 1          |
| 10         | WELAN | 2450.0     | 2          |
| 10         | CLARK | 2450.0     | 2          |
| 10         | TEBAGE | 1300.0     | 3          |
| 10         | MILLER | 1300.0     | 3          |
| 20         | SCOTT | 3000.0     | 1          |
| 20         | FORD  | 3000.0     | 1          |
| 20         | JONES | 2975.0     | 2          |
| 20         | ADAMS | 1100.0     | 2          |
| 20         | SMITH | 800.0      | 3          |
| 30         | BLAKE | 2850.0     | 1          |
| 30         | ALLEN | 1600.0     | 1          |
| 30         | TURNER | 1500.0     | 2          |
| 30         | MARTIN | 1250.0     | 2          |
| 30         | WARD  | 1250.0     | 3          |
| 30         | JAMES | 950.0      | 3          |
+------------+-------+------------+------------+
```

##### 3.6.4.18 NTH_VALUE

This topic describes the NTH_VALUE function and provides examples of using this function.

```
nth_value(expr, number [, skipNull]) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function calculates the **n**th value in the window. If the value of **n** exceeds the total number of rows in the window, NULL is returned. Parameters:
**expr**: a value of any basic data type.
**number**: an integer that is greater than or equal to 1.
**skipNull**: specifies whether to ignore the rows with NULL values when you calculate the **n**th value. The value of this
parameter is of the BOOLEAN type. The default value is False.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the value of **expr** of the **n**th row in the
current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the value of **expr** of the **n**th row from the starting row to the current row in the current window is returned. Return value: A value of the same data type as **expr** is returned.

```
select user_id, price, nth_value(price, 2) over
  (partition by user_id) as nth_value from test_src;
+------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 5.5        | 4.5        |
| 1          | 4.5        | 4.5        | -- This row is the second row in the current window.
| 1          | 6.5        | 4.5        |
| 1          | 5.5        | 4.5        |
| 2          | NULL       | 3.0        |
| 2          | 3.0        | 3.0        | -- This row is the second row in the current window.
| 3          | 4.0        | NULL       |
| 3          | NULL       | NULL       | -- This row is the second row in the current window.
+------------+------------+------------+ -- If ORDER BY is not specified, rows from the first row to the last row are in the current window. The value o f the second row is returned. select user_id, price, nth_value(price, 3) over
  (partition by user_id) as nth_value from test_src;
+------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 5.5        | 6.5        |
| 1          | 4.5        | 6.5        |
| 1          | 6.5        | 6.5        | -- This row is the third row in the current window.
| 1          | 5.5        | 6.5        |
| 2          | NULL       | NULL       |
| 2          | 3.0        | NULL       |
| 3          | 4.0        | NULL       |
| 3          | NULL       | NULL       |
+------------+------------+------------+ -- If ORDER BY is not specified, rows from the first row to the last row are in the current window. The value o f the third row is returned. -- The second and third windows have only two rows. select user_id, price, nth_value(price, 2) over
  (partition by user_id order by price) as nth_value from test_src;
+------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 4.5        | NULL       | -- The current window has only one row. The second row exceeds the wind
ow length.
| 1          | 5.5        | 5.5        |
| 1          | 5.5        | 5.5        |
| 1          | 6.5        | 5.5        |
| 2          | NULL       | NULL       |
| 2          | 3.0        | 3.0        |
| 3          | NULL       | NULL       |
| 3          | 4.0        | 4.0        |
+------------+------------+------------+ -- If ORDER BY is specified, rows from the first row to the current row belong to the current window. The value of the second row is returned. select user_id, price, nth_value(price, 1, true) over
  (partition by user_id) as nth_value from test_src;
+------------+------------+------------+
| user_id    | price      | nth_value  |
+------------+------------+------------+
| 1          | 5.5        | 5.5        |
| 1          | 4.5        | 5.5        |
| 1          | 6.5        | 5.5        |
| 1          | 5.5        | 5.5        |
| 2          | NULL       | 3.0        | -- The value of the first row is NULL, and therefore this row is skippe
```

|
|
|
|
`,` `pp` `d.`

```
| 2          | 3.0        | 3.0        |
| 3          | 4.0        | 4.0        |
| 3          | NULL       | 4.0        |
+------------+------------+------------+ -- If ORDER BY is not specified, rows from the first row to the last row belong to the current window. -- The value of the first row is returned. skipNull is set to True.
```

##### 3.6.4.19 CUME_DIST

This topic describes the CUME_DIST function and provides examples of using this function.

```
cume_dist() over(partition by [col1, col2…] order by [col1[asc|desc], col2[asc|desc]…]
```

Description: This function calculates the cumulative distribution. The cumulative distribution is the ratio of rows whose values are greater than or equal to the current value to all rows in a group. Parameters: **ORDER BY**: the value used for comparison. Return value: The ratio of the number of rows whose values are greater than or equal to the current value in the group to the total number of rows in the group is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Group all employees by department and obtain the cumulative distribution of **sal** for each group.

```
select deptno , ename , sal , concat(round(cume_dist() over(partition by deptno order by sal desc)*100,2),'%') as cume_dist from emp; -- The following result is returned: +------------+-------+------------+-----------+
| deptno     | ename | sal        | cume_dist |
+------------+-------+------------+-----------+
| 10         | JACCKA | 5000.0     | 33.33%    |
| 10         | KING  | 5000.0     | 33.33%    |
| 10         | CLARK | 2450.0     | 66.67%    |
| 10         | WELAN | 2450.0     | 66.67%    |
| 10         | TEBAGE | 1300.0     | 100.0%    |
| 10         | MILLER | 1300.0     | 100.0%    |
| 20         | SCOTT | 3000.0     | 40.0%     |
| 20         | FORD  | 3000.0     | 40.0%     |
| 20         | JONES | 2975.0     | 60.0%     |
| 20         | ADAMS | 1100.0     | 80.0%     |
| 20         | SMITH | 800.0      | 100.0%    |
| 30         | BLAKE | 2850.0     | 16.67%    |
| 30         | ALLEN | 1600.0     | 33.33%    |
| 30         | TURNER | 1500.0     | 50.0%     |
| 30         | MARTIN | 1250.0     | 83.33%    |
| 30         | WARD  | 1250.0     | 83.33%    |
| 30         | JAMES | 950.0      | 100.0%    |
+------------+-------+------------+-----------+
```

##### 3.6.4.20 FIRST_VALUE

This topic describes the FIRST_VALUE function and provides examples of using this function.

```
first_value(expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause]
```

Description: This function sorts rows and returns the first value in the range from the starting row to the current row. Parameters:
**expr**: a value of any basic data type.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the value of **expr** of the starting row in
the current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the value of **expr** of the starting row in the current window is returned. Return value: A value of the same data type as **expr** is returned.

```
select user_id, price, first_value(price) over
  (partition by user_id) as first_value from test_src;
+------------+------------+-------------+
| user_id    | price      | first_value |
+------------+------------+-------------+
| 1          | 5.5        | 5.5         | -- This row is the starting row of this window.
| 1          | 4.5        | 5.5         |
| 1          | 6.5        | 5.5         |
| 1          | 5.5        | 5.5         |
| 2          | NULL       | NULL        | -- This row is the starting row of this window.
| 2          | 3.0        | NULL        |
| 3          | 4.0        | 4.0         | -- This row is the starting row of this window.
| 3          | NULL       | 4.0         |
+------------+------------+-------------+ -- If ORDER BY is not specified, rows from the first row to the last row belong to the current window. The valu e of the starting row in the current window is returned. select user_id, price, first_value(price) over
  (partition by user_id order by price) as first_value from test_src;
+------------+------------+-------------+
| user_id    | price      | first_value |
+------------+------------+-------------+
| 1          | 4.5        | 4.5         | -- This row is the starting row of this window.
| 1          | 5.5        | 4.5         |
| 1          | 5.5        | 4.5         |
| 1          | 6.5        | 4.5         |
| 2          | NULL       | NULL        | -- This row is the starting row of this window.
| 2          | 3.0        | NULL        |
| 3          | NULL       | NULL        | -- This row is the starting row of this window.
| 3          | 4.0        | NULL        |
+------------+------------+-------------+ -- If ORDER BY is specified, rows from the first row to the current row belong to the current window. The value of the starting row in the current window is returned.
```

##### 3.6.4.21 LAST_VALUE

This topic describes the LAST_VALUE function and provides examples of using this function.

```
last_value(expr) over(partition by [col1, col2…] [order by [col1[asc|desc], col2[asc|desc]…]] [windowing_clause])
```

Description: This function sorts rows and returns the last value in the range from the starting row to the current row. Parameters:
**expr**: a value of any basic data type.
**partition by [col1, col2...]**: the columns in the window that is used for calculation.
**order by [col1[asc|desc], col2[asc|desc]**: If **ORDER BY** is not specified, the value of **expr** of the last row in the
current window is returned. If **ORDER BY** is specified, the returned results are sorted in the specified order and the value of **expr** of the current row in the current window is returned. Return value: A value of the same data type as **expr** is returned.

```
select user_id, price, last_value(price) over
  (partition by user_id) as last_value from test_src;
+------------+------------+------------+
| user_id    | price      | last_value |
+------------+------------+------------+
| 1          | 5.5        | 5.5        |
| 1          | 4.5        | 5.5        |
| 1          | 6.5        | 5.5        |
| 1          | 5.5        | 5.5        | -- This row is the last row in this window.
| 2          | NULL       | 3.0        |
| 2          | 3.0        | 3.0        | -- This row is the last row in this window.
| 3          | 4.0        | NULL       |
| 3          | NULL       | NULL       | -- This row is the last row in this window.
+------------+------------+------------+ -- If ORDER BY is not specified, the rows from the first row to the last row belong to the current window, and the value of the last row in the current window is returned. select user_id, price, last_value(price) over
  (partition by user_id order by price) as last_value from test_src;
+------------+------------+------------+
| user_id    | price      | last_value |
+------------+------------+------------+
| 1          | 4.5        | 4.5        | -- This row is the current row in the current window.
| 1          | 5.5        | 5.5        | -- This row is the current row in the current window.
| 1          | 5.5        | 5.5        | -- This row is the current row in the current window.
| 1          | 6.5        | 6.5        | -- This row is the current row in the current window.
| 2          | NULL       | NULL       | -- This row is the current row in the current window.
| 2          | 3.0        | 3.0        | -- This row is the current row in the current window.
| 3          | NULL       | NULL       | -- This row is the current row in the current window.
| 3          | 4.0        | 4.0        | -- This row is the current row in the current window.
+------------+------------+------------+ -- If ORDER BY is specified, rows from the first row to the current row belong to the current window. The value of the current row in the current window is returned.
```

#### 3.6.5 Aggregate functions

##### 3.6.5.1 Expressions of filter conditions in aggregate functions

This topic describes the expressions of filter conditions in aggregate functions and provides examples. Filter conditions can be added for all aggregate functions. If FILTER is specified, only the rows for which the value of
**where_condition** is TRUE are processed by the required aggregate functions.

```
aggregate_name(expression[,...]) [FILTER (WHERE where_condition)]
      SUM(x),
      SUM(x) FILTER (WHERE y > 1),
      SUM(x) FILTER (WHERE y > 2)
      FROM VALUES(NULL, 1),(1,2),(2,3),(3,NULL) AS t(x,y);
```

The following result is returned:

```
+------------+------------+------------+
| _c0        | _c1        | _c2        |
+------------+------------+------------+
| 6          | 3          | 2          |
+------------+------------+------------+
```

Only built-in aggregate functions support FILTER (WHERE where_condition). User-defined aggregate functions (UDAFs) do not support FILTER (WHERE where_condition). COUNT(*) cannot be used with FILTER (WHERE where_condition). To implement this feature, use the COUNT_IF function.

##### 3.6.5.2 COUNT

This topic describes the COUNT function and provides examples on how to use this function.

```
bigint count([distict|all] value)
```

Description: This function returns the number of records. Parameters
**distinct|all**: specifies whether to deduplicate records during counting. The default value is **all**, which indicates that
all records are counted. If this parameter is set to **distinct**, only records with distinct values are counted.
**value**: a value of any data type. If the input value for a row is null, this row is not used for calculation. You can set
**value** to an asterisk (*). This means that you can run count(*) to count all records.
Return value: A value of the BIGINT type is returned. The tbla table contains the **col1** column of the BIGINT type. Data in the tbla table:

```
+------+
| col1 |
+------+
| 1 |
+------+
| 2 |
+------+
| NULL |
+------+
```

Execute SQL statements.

```
select count(*) from tbla; -- The return value is 3. select count(col1) from tbla; -- The return value is 2.
```

The COUNT function can be used with the GROUP BY clause. For example, the test_src table contains two columns:
**key** and **value**. key is of the STRING type and value is of the DOUBLE type.
Data in the test_src table:

```
+-----+-------+
| key | value |
+-----+-------+
| a   | 2.0   |
+-----+-------+
| a   | 4.0   |
+-----+-------+
| b   | 1.0   |
+-----+-------+
| b   | 3.0   |
+-----+-------+
```

Execute SQL statements.

```
select key, count(value) as count from test_src group by key; -- The following result is returned: +-----+-------+
| key | count |
+-----+-------+
| a   | 2     |
+-----+-------+
| b   | 2     |
+-----+-------+
```

##### 3.6.5.3 COUNT_IF

This topic describes the aggregate function COUNT_IF and provides examples.

```
bigint count_if(BOOLEAN expr)
```

Description: This function calculates the number of records whose value of **expr** is TRUE. Parameters: **expr**, which is of the BOOLEAN type. If the value for a row is FALSE or NULL, the row is not counted. Return value: A value of the BIGINT type is returned.

```
SELECT COUNT_IF(x > 1), COUNT_IF(x <=1) FROM VALUES(NULL),(0),(1),(2) AS t(x);
```

The following result is returned:

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| 1          | 2          |
+------------+------------+
```

##### 3.6.5.4 AVG

This topic describes the AVG function and provides examples of using this function.

```
double avg(double value) decimal avg(decimal value)
```

Description: This function returns the average value of a column. Parameters: **value**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. If the input value for a row is NULL, this row is not used for calculation. Values of the BOOLEAN type cannot be used for calculation. Return value: If the input value is of the DECIMAL type, a value of the DECIMAL type is returned. If the input value is not of the DECIMAL type, a value of the DOUBLE type is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+-------+
| value |
+-------+
| 1     |
| 2     |
| NULL  |
+-------+
```

Execute the following statement:

```
select avg(value) as avg from tbla; -- The average value of the value column is 1.5, which is calculated by using the following formula: (1 + 2)/2 +------+
| avg  |
+------+
| 1.5  |
+------+
```

##### 3.6.5.5 MAX

This topic describes the MAX function and provides examples of using this function.

```
max(value)
```

Description: This function calculates the maximum value of values in a column. Parameters: **value**: a value of any data type. If the value for a row is NULL, this row that corresponds to the column is not used for calculation. Values of the BOOLEAN type are not used for calculation. Return value: A value of the same data type as **value** is returned. The tbla table contains the **col1** column of the BIGINT type. Data in the tbla table:

```
+------+
| col1 |
+------+
| 1    |
+------+
| 2    |
+------+
| NULL |
+------+
```

Execute the following statement:

```
select max(value) from tbla; -- 2 is returned.
```

##### 3.6.5.6 MIN

This topic describes the MIN function and provides examples of using this function.

```
min(value)
```

Description: This function calculates the minimum value of values in a column. Parameters: **value**: a value of any data type. If the value for a row is NULL, this row that corresponds to the column is not used for calculation. Values of the BOOLEAN type are not used for calculation. Return value: A value of the same data type as **value** is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+------+
| value|
+------+
| 1 |
+------+
| 2 |
+------+
| NULL |
+------+
```

Execute the following statement:

```
select min(value) from tbla; -- 1 is returned.
```

##### 3.6.5.7 MEDIAN

This topic describes the MEDIAN function and provides examples of using this function.

```
double median(double number) decimal median(decimal number)
```

Description: This function calculates the median value for a group of values. Parameters: **value**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+------+
| value|
+------+
| 1 |
+------+
| 2 |
+------+
| 3 |
+------+
| 4 |
+------+
| 5 |
+------+
```

Execute the following statement:

```
select median(value) from tbla; -- 3.0 is returned.
```

##### 3.6.5.8 STDDEV

This topic describes the STDDEV function and provides examples of using this function.

```
double stddev(double number) decimal stddev(decimal number)
```

Description: This function calculates the population standard deviation. Parameters: **value**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+------+
| value|
+------+
| 1 |
+------+
| 2 |
+------+
| 3 |
+------+
| 4 |
+------+
| 5 |
+------+
```

Execute the following statement:

```
select stddev(value) from tbla; -- 1.4142135623730951 is returned.
```

##### 3.6.5.9 STDDEV_SAMP

This topic describes the STDDEV_SAMP function and provides examples of using this function.

```
double stddev_samp(double number) decimal stddev_samp(decimal number)
```

Description: This function returns the sample standard deviation of a group of values. Parameters: **value**: a value of the DOUBLE or DECIMAL type. If the input value is of the STRING or BIGINT type, it is implicitly converted into the DOUBLE type before calculation. If the input value is not of the STRING or BIGINT type, an error is returned. Return value: A value of the DOUBLE or DECIMAL type is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+------+
| value|
+------+
| 1 |
+------+
| 2 |
+------+
| 3 |
+------+
| 4 |
+------+
| 5 |
+------+
```

Execute the following statement:

```
select stddev_samp(value) from tbla; -- 1.58113883008418981 is returned.
```

##### 3.6.5.10 SUM

This topic describes the SUM function and provides examples of using this function.

```
sum(value)
```

Description: This function returns the sum of values in specified rows. Parameters: **value**: a value of the DOUBLE, DECIMAL, or BIGINT type. If the input value is of the STRING type, it is implicitly converted into the DOUBLE type before calculation. If the input value for a row is NULL, this row is not used for calculation. Values of the BOOLEAN type are not used for calculation. Return value: If the input value is of the BIGINT type, a value of the BIGINT type is returned. If the input value is of the DOUBLE or STRING type, a value of the DOUBLE type is returned. The tbla table contains the **value** column of the BIGINT type. Data in the tbla table:

```
+------+
| value|
+------+
| 1 |
+------+
| 2 |
+------+
| NULL |
+------+
```

Execute the following statement:

```
select sum(value) from tbla; -- 3 is returned.
```

##### 3.6.5.11 WM_CONCAT

This topic describes the WM_CONCAT function and provides examples of using this function.

```
string wm_concat(string separator, string str)
```

Description: This function returns a string of values that are separated by using a given delimiter. The delimiter is specified by **separator**. Parameters:
**separator**: the delimiter, which is a constant of the STRING type. If it is not of the STRING type or is not a constant,
an error is returned.
**str**: a value of the STRING type. If the input value is of the BIGINT, DOUBLE, or DATETIME type, it is implicitly
converted into the STRING type before calculation. If the input value is not of the BIGINT, DOUBLE, or DATETIME type, an error is returned. Return value: A value of the STRING type is returned. If **test_src** in **select wm_concat(',', name) from test_src;** is an empty set, NULL is returned. Group and sort values in the test table and use a string to list the values in the same group.

```
-- Create the test table. create table test(id int , alphabet string); -- Insert data into the test table. insert into test values (1,'a'),(1,'b'),(1,'c'),(2,'D'),(2,'E'),(2,'F'); -- Group and sort values in the test table based on the id column. Then, use a string to list values in the sam e group. select id,wm_concat('',alphabet) from test group by id order by id limit 100; +------------+------------+
| id         | _c1        |
+------------+------------+
| 1          | abc        |
| 2          | DEF        |
+------------+------------+
```

##### 3.6.5.12 PERCENTILE

This topic describes the PERCENTILE function and provides examples of using this function.

```
double percentile(bigint col, p) array<double> percentile(bigint col, array(p1 [, p2]...))
```

Description: This function returns the **p**th percentile of the specified column. **p** must be between 0 and 1.

**Important**

You can calculate the percentile only for integer values. Parameters:
**col**: the name of the table column of the BIGINT type.
**p**: the percentile that must be between 0 and 1.
The var_test table contains the **c1** column. Data in the var_test table:

```
+------------+
| c1         |
+------------+
| 8          |
| 9          |
| 10         |
| 11         |
+------------+
```

Execute the following statement to calculate the **p**th percentile of the **c1** column.

```
select percentile(c1,0),percentile(c1,0.3),percentile(c1,0.5),percentile(c1,1) from var_test; -- The following result is returned: +------------+------------+------------+------------+
| _c0 | _c1 | _c2 | _c3 |
+------------+------------+------------+------------+
| 8.0 | 8.9 | 9.5 | 11.0 |
+------------+------------+------------+------------+ select percentile(c1,array(0,0.3,0.5,1))from var_test; -- The following result is returned: +------+
| _c0 |
+------+
| [8, 8.9, 9.5, 11] |
+------+
```

##### 3.6.5.13 Additional aggregate functions

###### 3.6.5.13.1 Usage notes

This topic describes the configuration operation that you must perform before you use additional aggregate functions. MaxCompute V2.0 provides more aggregate functions. You must add the following SET statement before the SQL statements for these new functions:

```
set odps.sql.type.system.odps2=true;
```

You must submit and execute the SET statement and the SQL statements for the new functions at the same time.

###### 3.6.5.13.2 COLLECT_LIST

This topic describes the COLLECT_LIST function and provides examples of using this function.

```
ARRAY collect_list(col)
```

Description: This function aggregates the expressions that are specified by **col** in a given group into an array. Parameters: **col**: a column of the table, which is of any data type. Return value: A value of the ARRAY type is returned.

###### 3.6.5.13.3 COLLECT_SET

This topic describes the COLLECT_SET function.

```
array collect_set(col)
```

Description: This function aggregates the expressions that are specified by **col** in a given group into an array without duplicate elements. Parameters: **col**: a table column, which can be of any data type. Return value: A value of the ARRAY type is returned.

###### 3.6.5.13.4 VARIANCE or VAR_POP

This topic describes the VARIANCE or VAR_POP function and provides examples of using this function.

```
DOUBLE variance(col) DOUBLE var_pop(col)
```

Description: This function calculates the variance of a specified column of a numeric data type. Parameters: **col**: the column of a numeric data type. If it is not of a numeric data type, NULL is returned. Return value: A value of the DOUBLE type is returned. The test table contains the**c1** column. Data in the test table:

```
+------------+
| c1         |
+------------+
| 8          |
| 9          |
| 10         |
| 11         |
+------------+
```

Execute the following statement to calculate the variance of the **c1** column:

```
select variance(c1) from test; -- You can also execute the following statement: select var_pop(c1) from test; -- The following result is returned: +------------+
| _c0 |
+------------+
| 1.25 |
+------------+
```

###### 3.6.5.13.5 VAR_SAMP

This topic describes the VAR_SAMP function and provides examples of using this function.

```
DOUBLE var_samp(col)
```

Description: This function calculates the sample variance of a specified column of a numeric data type. Parameters: **col**: a column of a numeric data type. If it is not of a numeric data type, NULL is returned. Return value: A value of the DOUBLE type is returned The test table contains the **c1** column. Data in the test table:

```
+------------+
| c1         |
+------------+
| 8          |
| 9          |
| 10         |
| 11         |
+------------+
```

Execute the following statement to calculate the sample variance of the **c1** column:

```
select var_samp(c1) from test; -- The following result is returned: +------------+
| _c0 |
+------------+
| 1.6666666666666667 |
+------------+
```

###### 3.6.5.13.6 COVAR_POP

This topic describes the COVAR_POP function and provides examples of using this function.

```
DOUBLE covar_pop(col1, col2)
```

Description: This function calculates the population covariance of two columns of a numeric data type. Parameters: **col1 and col2**: the columns of a numeric data type. If they are not of a numeric data type, NULL is returned. Return value: A value of the DOUBLE type is returned. The test table contains the **c1** and **c2** columns. Data in the test table:

```
+------------+------------+
| c1         | c2         |
+------------+------------+
| 3          | 2          |
| 14         | 5          |
| 50         | 14         |
| 26         | 75         |
+------------+------------+
```

Execute the following statement to calculate the population covariance of the **c1** and **c2** columns:

```
select covar_pop(c1,c2) from test; -- The following result is returned: +------------+
| _c0        |
+------------+
| 123.49999999999997|
+------------+
```

###### 3.6.5.13.7 COVAR_SAMP

This topic describes the COVAR_SAMP function and provides examples of using this function.

```
DOUBLE covar_samp(col1, col2)
```

Description: This function calculates the sample covariance of two columns of a numeric data type. Parameters: **col1 and col2**: the columns of a numeric data type. If they are not of a numeric data type, NULL is returned. Return value: A value of the DOUBLE type is returned The test table contains the **c1** and **c2** columns. Data in the test table:

```
+------------+------------+
| c1         | c2         |
+------------+------------+
| 3          | 2          |
| 14         | 5          |
| 50         | 14         |
| 26         | 75         |
+------------+------------+
```

Execute the following statement to calculate the sample covariance of the **c1** and **c2** columns:

```
select covar_samp(c1,c2) from test; -- The following result is returned: +------------+
| _c0        |
+------------+
| 164.66666666666663|
+------------+
```

###### 3.6.5.13.8 ANY_VALUE

This topic describes the ANY_VALUE function and provides examples of using this function.

```
ANY_VALUE(value)
```

Description: This function returns a non-deterministic value from a specific column. Parameters: **value**: a value of any data type. If the input **value** for a row is NULL, this row is not used for calculation. Return value: A value of the same data type as the input value is returned.

```
select key, ANY_VALUE(value) from values (1, 'value1'),(1, 'value2'),(2, 'value3'),(2, NULL),(3, NULL) as t(key, value) group by key; -- The following result is returned: +------------+------------+
| key        | _c1        |
+------------+------------+
| 1          | value1     |
| 2          | value3     |
| 3          | NULL       |
+------------+------------+
```

The value returned by ANY_VALUE is not deterministic and different values may be returned for the same input value.

###### 3.6.5.13.9 NUMERIC_HISTOGRAM

This topic describes the NUMERIC_HISTOGRAM function.

```
map<double, double> numeric_histogram(bigint buckets , double value)
```

Description: This function returns the approximate histogram of a given column. Parameters:
**buckets**: the maximum number of buckets in the column whose approximate histogram is returned. The value must
be of the BIGINT type.
**value**: the column whose approximate histogram you want to obtain. The column must be of the DOUBLE type.
Return value: A value of the MAP<DOUBLE,DOUBLE> type is returned. In the return value, a key indicates an xcoordinate, and its value indicates the height on the approximate histogram of the column.

###### 3.6.5.13.10 PERCENTILE_APPROX

This topic describes the PERCENTILE_APPROX function and provides examples of using this function.

```
double percentile_approx(double col, p [, B])) array<double> percentile_approx(double col, array(p1 [, p2]...) [, B])
```

Description: This function returns the approximate percentile value of the **col** column at the given percentage **p**. Parameters:
**p**: the given percentile value. Valid values: [0.0,1.0]. You can specify one percentage to return an approximate
percentile value or multiple percentages to return an array that consists of percentile values.
**B**: the accuracy of the return value. A higher accuracy indicates a more accurate value. If you do not specify this
parameter, 10000 is used. If the number of values in the **col** column is less than **B**, an exact percentile value is returned. Return value: **percentile_approx(double col, p [, B]))** returns a single approximate percentile value.
**percentile_approx(double col, array(p1 [, p2]…) [, B])** returns an array that consists of multiple percentile values.

```
select percentile_approx(10.0, 0.5, 100); -- 10.0 is returned. select percentile_approx(10.0, array(0.5, 0.4, 0.1), 100); -- [10.0,10.0,10.0] is returned.
```

###### 3.6.5.13.11 APPROX_DISTINCT

This topic describes the APPROX_DISTINCT function and provides examples of using this function.

```
bigint approx_distinct(value)
```

Description: This function returns the approximate number of distinct input values. Parameters: **value**: the input data that is used for deduplication. Return value: A value of the BIGINT type is returned. If all input values are NULL, 0 is returned. This function produces a standard error of 5%.

#### 3.6.6 Other functions

##### 3.6.6.1 ARRAY

This topic describes the ARRAY function and provides examples of using this function.

```
ARRAY array(value1,value2, ...)
```

Description: This function creates an array of a given data type that is specified by **value**. Parameters: **value**: any data type. All the values must be of the same data type. Return value: A value of the ARRAY type is returned.

```
select array(123,456,789); -- The following result is returned: [123, 456, 789]
```

##### 3.6.6.2 ARRAY_CONTAINS

This topic describes the ARRAY_CONTAINS function and provides examples of using this function.

```
boolean array_contains(ARRAY<T> a, value v)
```

Description: This function checks whether array **a** contains value **v**. Parameters:
**a**: a value of the ARRAY type.
**v**: a value of the same data type as other values in the array.
Return value: A value of the BOOLEAN type is returned.

```
select array_contains(array('a','b'), 'a'); -- True is returned. select array_contains(array(456,789),123); -- False is returned.
```

##### 3.6.6.3 CAST

This topic describes the CAST function.

```
cast(expr as <type>)
```

Description: This function converts the result of an expression into another data type. For example, you can use `cast('1' as bigint)` to convert **1** of the STRING type into **1** of the INT type. If the conversion fails, an error is returned. Notes: `cast(double as bigint)` : converts a value of the DOUBLE type into a value of the BIGINT type. `cast(string as bigint)` : converts a value of the STRING type into a value of the BIGINT type. If the string consists of numerals expressed as integers, the string is directly converted into the BIGINT type. If the string consists of numerals expressed in the FLOAT or EXPONENTIAL form, the string is converted into the DOUBLE type and then into the BIGINT type. The date format for `cast(string as datetime)` or `cast(datetime as > string)` is **yyyy-mm-dd hh:mi:ss**.

##### 3.6.6.4 COALESCE

This topic describes the COALESCE function.

```
coalesce(expr1, expr2, ...)
```

Description: This function returns the first non-NULL value in a list. If all values in the list are NULL, NULL is returned. Parameters: **expr**: the values you want to test. All these values must be of the same data type or are all NULL. Otherwise, an error is returned. The list must include at least one parameter. Otherwise, an error is returned. Return value: A value of the same data type as the expr parameter is returned.

##### 3.6.6.5 DECODE

This topic describes the DECODE function and provides examples of using this function.

```
decode(expression, search, result[, search, result]...[, default])
```

Description: This function implements the IF-THEN-ELSE conditional branching feature. Parameters:
**expression**: the expression that you want to compare.
**search**: the search item that you want to compare with **expression**.
**result**: the value returned if the values of **search** and **expression** match.
**default**: the value returned if no search item matches the expression. If **default** is not specified, NULL is returned.
This parameter is optional. Return value: The matched **search** value is returned. If no matched item exists, **default** is returned. If **default** is not specified, NULL is returned. Three or more parameters must be specified. All **results** must be of the same data type or be NULL. Inconsistent data types will cause an error. All values of **search** and **expression** must be of the same data type. Otherwise, an error is returned. If **search** in the **DECODE** function has duplicate values that match the expression, the first mapping result is returned.

```
decode(customer_id, 1, 'Taobao', 2, 'Alipay', 3, 'Aliyun', NULL, 'N/A', 'Others') as result FROM VALUES (1,10),
        (1,10),
        (2,null),
        (3,13),
        (4,0),
        (null,6),
        (5,18)
        as t(customer_id,value);
```

In this example, the **DECODE** function implements the **IF-THEN-ELSE** statement.

```
if customer_id = 1 then result := 'Taobao'; elsif customer_id = 2 then result := 'Alipay'; elsif customer_id = 3 then result := 'Aliyun'; ... else result := 'Others'; end if;
```

In most cases, if "NULL = NULL" appears during data computation, the result returned by the MaxCompute SQL engine is NULL, whereas the **DECODE** function considers that the two NULL values are the same. In this example, if the value of **customer_id** is NULL, the **DECODE** function returns N/A.

##### 3.6.6.6 EXPLODE

This topic describes the EXPLODE function and provides examples of using this function.

```
explode (var)
```

Description: This function is a user-defined table-valued function (UDTF) that transposes one row into multiple rows. If **var** is of the ARRAY <T> type, the data of the ARRAY type stored in a column is converted into multi-row data. If **var** is of the MAP<K, V> type, each key-value pair of the MAP type stored in a column is transposed to a row with two columns. One column is used for storing keys and the other column is used for storing values. Parameters: **var**: a value of the ARRAY<T> or MAP<K, V> type. Return value: transposed rows. Limits on the EXPLODE function: A SELECT statement can specify only the column that is used for this function. Other columns cannot be specified. This function cannot be used with the GROUP BY, CLUSTER BY, DISTRIBUTE BY, or SORT BY clause.

```
select explode(array(null, 'a', 'b', 'c')); -- The following result is returned: +------------+
| col        |
+------------+
| NULL       |
| a          |
| b          |
| c          |
+------------+
```

##### 3.6.6.7 GET_IDCARD_AGE

This topic describes the GET_IDCARD_AGE function.

```
get_idcard_age(idcardno)
```

Description: This function returns the current age based on the ID card number. The current age is the current year minus the birth year in the ID card number. Parameters: **idcardno**: the ID card number of the STRING type. The value is a 15-digit or 18-digit number. During data computation, the validity of the ID card is verified based on the province code and the last check code. If the verification fails, NULL is returned. Return value: A value of the BIGINT type is returned. If the input value is NULL, NULL is returned. If the difference between the current year and the birth year is greater than 100, NULL is returned.

##### 3.6.6.8 GET_IDCARD_BIRTHDAY

This topic describes the GET_IDCARD_BIRTHDAY function.

```
get_idcard_birthday(idcardno)
```

Description: This function returns the date of birth based on the ID card number. Parameters: **idcardno**: the ID card number of the STRING type. The value is a 15-digit or 18-digit number. During data computation, the validity of the ID card is verified based on the province code and the last check code. If the verification fails, NULL is returned. Return value: A value of the DATETIME type is returned. If the input value is NULL, NULL is returned.

##### 3.6.6.9 GET_IDCARD_SEX

This topic describes the GET_IDCARD_SEX function.

```
get_idcard_sex(idcardno)
```

Description: This function returns the gender based on the ID card number. The return value is M or F. M indicates male and F indicates female. Parameters: **idcardno**: the ID card number of the STRING type. The value is a 15-digit or 18-digit number. During data computation, the validity of the ID card is verified based on the province code and the last check code. If the verification fails, NULL is returned. Return value: A value of the STRING type is returned. If the input value is NULL, NULL is returned.

##### 3.6.6.10 GREATEST

This topic describes the GREATEST function.

```
greatest(var1, var2, ...)
```

Description: This function returns the maximum value of the input parameters. Parameters: **var1** and **var2**: values of the BIGINT, DOUBLE, DECIMAL, DATETIME, or STRING type. If all input values are NULL, NULL is returned. Return value: The maximum value in the values of all input parameters. If implicit conversion is not required, the data type of the return value is the same as the data types of input parameters. NULL is interpreted as the minimum value. If a data type conversion is performed among the DOUBLE, BIGINT, and STRING types, a value of the DOUBLE type is returned. If a data type conversion is performed between the STRING and DATETIME types, a value of the DATETIME type is returned. If a data type conversion is performed among the DECIMAL, DOUBLE, BIGINT, and STRING types, a value of the DECIMAL type is returned. Implicit conversions of other data types are not allowed. If `odps.sql.hive.compatible` is set to true and the value of an input parameter is NULL, NULL is returned.

##### 3.6.6.11 INDEX

This topic describes the INDEX function and provides examples of using this function.

```
index(var1[var2])
```

Description: This function returns the **var2**th value if **var1** is of the ARRAY<T> type and returns the value whose key is
**var2** in **var1** if **var1** is of the MAP<K, V> type.
Parameters:
**var**: a value of the ARRAY<T> or MAP<K, V> type.
**var2**: If the value of **var1** is of the ARRAY<T> type, the value of **var2** is of the BIGINT type and greater than or equal
to 0. If the value of **var1** is of the MAP<K, V> type, the value of **var2** is of the K type. Return value: If the value of **var1** is of the ARRAY<T> type, a value of the T type is returned. If the value of **var2** is beyond the range of elements in the value of the ARRAY<T> type, NULL is returned. If the value of **var1** is of the MAP<K, V> type, a value of the V type is returned. If the value whose key is **var2** does not exist in values of the MAP<K, V> type, NULL is returned. If the value of **var1** is an array, execute the following SQL statement:

```
select array('a','b','c')[2] from dual; -- The following result is returned: +-----+
| _c0 |
+-----+
| c   |
+-----+
```

If the value of **var1** is of the MAP<K, V> type, execute the following SQL statement:

```
select str_to_map("test1=1,test2=2")["test1"] from dual; -- The following result is returned: +-----+
| _c0 |
+-----+
| 1   |
+-----+
```

To execute the SQL statement, remove the index, and execute `var1[var2]` directly. Otherwise, a syntax error is returned. If the value of **var1** is NULL, NULL is returned.

##### 3.6.6.12 MAX_PT

This topic describes the MAX_PT function and provides examples of using this function.

```
max_pt(table_full_name)
```

Description: This function returns the maximum value of each first-level partition of a partitioned table in alphabetic order. This function also reads data from the data file in the first-level partitions. Parameters: **table_full_name**: the table name that has a project name, such as prj.src. The value of this parameter is of the STRING type. You must have the permissions to read the table. Return value: The maximum value in each first-level partition is returned. The tbl table is a partitioned table and contains the following partitions:

```
pt ='20120901' pt ='20120902'
```

The return value of the following statement is **'20120902'**. The MaxCompute SQL statement reads data from the
**20120902** partition.

```
select * from tbl where pt=max_pt('myproject.tbl');
```

If a partition is added by using the **ALTER TABLE** statement and the partition contains no data file, the maximum value in this partition is not returned.

##### 3.6.6.13 ORDINAL

This topic describes the ORDINAL function and provides examples of using this function.

```
ordinal(bigint nth, var1, var2, ...)
```

Description: This function sorts the input variables in ascending order, and returns the value in the **nth** bit. Parameters:
**nth**: a value of the BIGINT type. This parameter specifies the position in which the value is to be returned. The value
of this parameter starts from `1` . If the value of this parameter is null, null is returned.
**var**: a value of the BIGINT, DOUBLE, DATETIME, or STRING type.
Return value: The value in the **nth** bit is returned. If no implicit conversion is required, the return value is of the same data type as the input parameter. If a data type conversion is performed among the DOUBLE, BIGINT, and STRING types, a value of the DOUBLE type is returned. If a data type conversion is performed between the STRING and DATETIME types, a value of the DATETIME type is returned. Implicit conversions of other data types are not allowed. The value null is interpreted as the minimum value. Example:

```
-- The return value is 2. select ordinal(3, 1, 3, 2, 5, 2, 4, 6);
```

##### 3.6.6.14 LEAST

This topic describes the LEAST function.

```
least(var1, var2, ...)
```

Description: This function returns the minimum value of the input parameters. Parameters: **var**: a value of the BIGINT, DOUBLE, DECIMAL, DATETIME, or STRING type. If the values of all input parameters are NULL, NULL is returned. Return value: The minimum value of all values of the input parameters is returned. If implicit conversion is not required, the return value must be of the same data type as the input parameters. If a data type conversion is performed among the DOUBLE, BIGINT, and STRING types, a value of the DOUBLE type is returned. If a data type conversion is performed between the STRING and DATETIME types, a value of the DATETIME type is returned. If a data type conversion is performed among the DECIMAL, DOUBLE, BIGINT, and STRING types, a value of the DECIMAL type is returned. Implicit conversions of other data types are not allowed. NULL is interpreted as the minimum value.

##### 3.6.6.15 SIZE

This topic describes the SIZE function and provides examples of using this function.

```
INT size(map) INT size(array)
```

Description: **size(map)** returns the number of key-value pairs in the specified **map** parameter. **size(array)** returns the number of elements in the specified **array** parameter. Parameters:
**map**: a value of the MAP type.
**array**: a value of the ARRAY type.
Return value: A value of the INT type is returned.

```
select size(map('a',123,'b',456)); -- 2 is returned. select size(map('a',123,'b',456,'c',789)); -- 3 is returned. select size(array('a','b')); -- 2 is returned. select size(array(123,456,789)); -- 3 is returned.
```

##### 3.6.6.16 SPLIT

This topic describes the SPLIT function and provides examples of using this function.

```
split(str, pat)
```

Description: This function returns an array after **str** is split with **pat**. Parameters:
**str**: the string that you want to split, which is of the STRING type.
**pat**: a delimiter of the STRING type, which supports regular expressions.
Return value: The result after **str** is split with **pat** is returned. The return value is of the ARRAY<STRING> type.

```
select split("a,b,c",","); -- The following result is returned: +------+
| _c0  |
+------+
| [a, b, c] |
+------+
```

##### 3.6.6.17 STR_TO_MAP

This topic describes the STR_TO_MAP function and provides examples of using this function.

```
str_to_map(text [, delimiter1 [, delimiter2]])
```

Description: This function splits **text** into key-value pairs by using **delimiter1** and then splits the key and value in a key-value pair by using **delimiter2**. Parameters:
**text**: the string that you want to split. The value of this parameter is of the STRING type.
**delimiter1**: the delimiter that splits text into key-value pairs. The value of this parameter is of the STRING type. If
this parameter is not specified, a comma (,) is used by default.
**delimiter2**: the delimiter that separates keys from values. The value of this parameter is of the STRING type. If this
parameter is not specified, an equal sign (=) is used by default. Return value: The result after **text** is split by using **delimiter1** and **delimiter2** is returned. The return value is of the MAP<STRING, STRING> type. Example:

```
select str_to_map("test1=1,test2=2"); -- Returned result: +------+
| _c0  |
+------+
| {test1:1, test2:2} |
+------+
```

##### 3.6.6.18 UUID

This topic describes the UUID function.

```
string uuid()
```

Description: This function returns a random ID, for example, **29347a88-1e57-41ae-bb68-a9edbdd94212**. The return value of this function is a random global ID that has a low probability of duplication.

##### 3.6.6.19 UNIQUE_ID

This topic describes the UNIQUE_ID function.

```
string unique_id()
```

Description: This function returns a unique random ID, for example, **29347a88-1e57-41ae-bb68-a9edbdd94212_1**. This function is more efficient than the UUID function.

##### 3.6.6.20 SAMPLE

This topic describes the SAMPLE function and provides examples of using this function.

```
boolean sample(x, y, column_name1,column_name2,...)
```

Description: This function samples all values that are read from the column specified by **column_name** based on x and y, and filters out the rows that do not meet the sampling condition. Parameters: x and y: integer constants that are greater than 0. The values of the two parameters are of the BIGINT type. These parameters indicate that the values fall into **x** portions by calling the hash function and the **y**th portion is used. If **y** is not specified, the first portion is used, and you must not specify **column_name**. If the value of x or y is not of the BIGINT type or is less than or equal to 0, an error is returned. If the value of y is greater than the value of x, an error is returned. If the value of x or y is NULL, NULL is returned.
**column_name**: the column from which you want to sample values. This parameter is optional. If this parameter is
not specified, random sampling is performed based on the values of x and y. This parameter can be of any data type, and its value can be NULL. No implicit conversion is performed. If the value of **column_name** is a constant, an error is returned. Return value: A value of the BOOLEAN type is returned. To avoid data skew due to NULL values, the system performs uniform hashing on NULL values in the columns specified by **column_name**. This ensures that data evenly falls into **x** portions. If **column_name** is not specified and the amount of data is small, random hashing may be performed. In this case, we recommend that you specify **column_name** for uniform hashing. The tbla table contains the **cola** column.

```
select * from tbla where sample (4, 1 , cola) = true; -- The values in the cola column fall into four portions by calling the hash function, and data in the first po rtion is extracted. select * from tbla where sample (4, 2) = true; -- The values in each row are randomly hashed into four portions, and data in the second portion is extracted.
```

##### 3.6.6.21 CASE WHEN expression

This topic describes the CASE WHEN expression and provides examples of using this function. MaxCompute provides two syntax formats for the CASE WHEN expression.

```
case value when value1 then result1 when value2 then result2 ... else resultn end case when (_condition1) then result1 when (_condition2) then result2 when (_condition3) then result3 ... else resultn end
```

The CASE WHEN expression can return different values based on the calculation result of the **value** expression. The following example shows that different regions are obtained based on the value of **shop_name**.

```
case when shop_name is null then 'default_region' when shop_name like 'hang%' then 'zj_region' end as region from sale_detail;
```

If all **result** values are of the BIGINT or DOUBLE type, the data types are converted into the DOUBLE type before the values are returned. If some **result** values are of the STRING type, the data types of all values are converted into the STRING type before the values are returned. If the conversion cannot be performed, for example, the BOOLEAN type cannot be converted into the STRING type, an error is returned. Conversions between other data types are not allowed.

##### 3.6.6.22 IF

This topic describes the IF function and provides examples of using this function.

```
if(testCondition, valueTrue, valueFalseOrNull)
```

Description: This function determines whether **testCondition** evaluates to true. If testCondition evaluates to true,
**valueTrue** is returned. Otherwise, **valueFalse** or NULL is returned.
Parameters:
**testCondition**: the expression that you want to evaluate. The value of this parameter is of the BOOLEAN type.
**valueTrue**: the value returned if **testCondition** evaluates to true.
**valueFalseOrNull**: the value returned if **testCondition** evaluates to false. It can be set to NULL.
Return value: The data type of the return value is the same as that of **valueTrue** or **valueFalseOrNull**.

```
select if(1=2,100,200); -- The following result is returned: +------------+
| _c0        |
+------------+
| 200        |
+------------+
```

##### 3.6.6.23 Additional functions

###### 3.6.6.23.1 Usage notes

This topic describes the configuration operation that you must perform before you use other functions that are added to MaxCompute V2.0. MaxCompute V2.0 provides more other functions. You must add the following SET statement before the SQL statements for these new functions:

```
set odps.sql.type.system.odps2=true;
```

You must submit and execute the SET statement and the SQL statements for the new functions at the same time.

###### 3.6.6.23.2 MAP

This topic describes the MAP function and provides examples of using this function.

```
map map(K key1, V value1, K key2, V value2, ...)
```

Description: This function creates mappings by using the given key-value pairs. Parameters:
**key**: All **keys** must be of the same data types, such as those after an implicit conversion. The data types must be
basic types.
**value**: All **value** types, such as those after an implicit conversion, must be the same and can be of any data types.
Return value: A value of the MAP type is returned. The t_table table contains the **c1**, **c2**, **c3**, **c4**, and **c5** columns. The c1, c4, and C5 columns are of the BIGINT type, and the c2 and c3 columns are of the STRING type. Data in the t_table table:

```
+------------+----+----+------------+------------+
| c1         | c2 | c3 | c4         | c5         |
+------------+----+----+------------+------------+
| 1000       | k11 | k21 | 86         | 15         |
| 1001       | k12 | k22 | 97         | 2          |
| 1002       | k13 | k23 | 99         | 1          |
+------------+----+----+------------+------------+
```

Execute the following statement:

```
select map(c2,c4,c3,c5) from t_table; -- The following result is returned: +------+
| _c0  |
+------+
| {k11:86, k21:15} |
| {k12:97, k22:2} |
| {k13:99, k23:1} |
+------+
```

###### 3.6.6.23.3 MAP_KEYS

This topic describes the MAP_KEYS function and provides examples of using this function.

```
ARRAY map_keys(map<K, V>)
```

Description: This function returns all keys in the MAP parameter as an array. Parameters: **map**: a value of the MAP type. Return value: A value of the ARRAY type is returned. If the input value is NULL, NULL is returned. The t_table_map table contains two columns: **c1** and **t_map**. c1 is of the BIGINT type and t_map is of the MAP<STRING,BIGINT> type.

```
+------------+-------+
| c1         | t_map |
+------------+-------+
| 1000       | {k11:86, k21:15} |
| 1001       | {k12:97, k22:2} |
| 1002       | {k13:99, k23:1} |
+------------+-------+
```

Execute the following statement:

```
select c1,map_keys(t_map) from t_table_map; -- The following result is returned: +------------+------+
| c1         | _c1  |
+------------+------+
| 1000       | [k11, k21] |
| 1001       | [k12, k22] |
| 1002       | [k13, k23] |
+------------+------+
```

###### 3.6.6.23.4 MAP_VALUES

This topic describes the MAP_VALUES function and provides examples of using this function.

```
ARRAY map_values(map<K, V>)
```

Description: This function returns all values in the map parameter as an array. Parameters: **map**: a value of the MAP type. Return value: A value of the ARRAY type is returned. If the input value is NULL, NULL is returned.

```
select map_values(map('a',123,'b',456)); -- The following result is returned: [123, 456]
```

###### 3.6.6.23.5 SORT_ARRAY

This topic describes the SORT_ARRAY function and provides examples of using this function.

```
ARRAY sort_array(ARRAY<T>)
```

Description: This function sorts data in a given array. Parameters: **ARRAY<T>**: data of the ARRAY type. Data in the array can be of any data type. Return value: A value of the ARRAY type is returned. The t_array table contains three columns: **c1**, **c2**, and **c3**. The c1 and c3 columns are of the ARRAY<STRING> type, and the c2 column is of the ARRAY<INT> type.

```
+------------+---------+--------------+
| c1         | c2      | c3           |
+------------+---------+--------------+
| [a, c, f, b]  | [4, 5, 7, 2, 5, 8]  |  [You, Me, Him] |
+------------+---------+--------------+
```

Execute the following statement:

```
select sort_array(c1),sort_array(c2),sort_array(c3) from t_array; -- The following result is returned: [a, b, c, f] [2, 4, 5, 5, 7, 8] [Him, You, Me]
```

###### 3.6.6.23.6 POSEXPLODE

This topic describes the POSEXPLODE function and provides examples of using this function.

```
posexplode(ARRAY<T>)
```

Description: This function converts a given array into a table that has two columns. The first column lists subscripts of each value in the array, starting from 0. The second column lists array elements. Parameters: **ARRAY<T>**: a value of the ARRAY type. Data in the array can be of any data type. Return value: The generated table is returned.

```
select posexplode(array('a','c','f','b')); -- The following result is returned: +------------+-----+
| pos        | val |
+------------+-----+
| 0          | a   |
| 1          | c   |
| 2          | f   |
| 3          | b   |
+------------+-----+
```

###### 3.6.6.23.7 STRUCT

This topic describes the STRUCT function and provides examples of using this function.

```
STRUCT struct(value1,value2, ...)
```

Description: This function creates a value of the STRUCT type based on the given **value** list. Parameters: **value**: a value of any data type. Return value: A value of the STRUCT type is returned. The fields in returned results are sequentially named as **col1,**
**col2, ...**.

```
select struct('a',123,'ture',56.90); -- The following result is returned: {col1:a, col2:123, col3:ture, col4:56.9}
```

###### 3.6.6.23.8 NAMED_STRUCT

This topic describes the NAMED_STRUCT function and provides examples of using this function.

```
STRUCT named_struct(string name1, T1 value1, string name2, T2 value2, ...)
```

Description: This function creates a value of the STRUCT type based on the given **name/value** list. Parameters:
**value**: a value of any data type.
**name**: the name of the field of the STRING type. This parameter is a constant.
Return value: A value of the STRUCT type is returned. Fields in the return value are sequentially named as **name1,**
**name2, ...**.

```
select named_struct('user_id',10001,'user_name','bob','married','F','weight',63.50); -- The following result is returned: {user_id:10001, user_name:bob, married:F, weight:63.5}
```

###### 3.6.6.23.9 INLINE

This topic describes the INLINE function and provides examples of using this function.

```
inline(array<STRUCT<f1:T1, f2:T2, ... >>)
```

Description: This function expands a given STRUCT array. Each array element is given one row and each STRUCT element corresponds to one column in each row. Parameters: **STRUCT**: the values in the array, which are of any data type. Return value: The function generated by the table is returned. Column information of the t_table table is **t_struct**
**struct<user_id:bigint,user_name:string,married:string,weight:double>**. Data in the t_table table:

```
+----------+
| t_struct |
+----------+
| {user_id:10001, user_name:LiLei, married:N, weight:63.5} |
| {user_id:10002, user_name:HanMeiMei, married:Y, weight:43.5} |
+----------+
```

Execute the following statement:

```
select inline(array(t_struct)) from t_table; -- The following result is returned: +------------+-----------+---------+------------+
| user_id    | user_name | married | weight     |
+------------+-----------+---------+------------+
| 10001      | LiLei     | N       | 63.5       |
| 10002      | HanMeiMei | Y       | 43.5       |
+------------+-----------+---------+------------+
```

###### 3.6.6.23.10 BETWEEN AND expression

This topic describes the BETWEEN AND expression function and provides examples of using this function.

```
A [NOT] BETWEEN B AND C
```

If the value of A, B, or C is NULL, NULL is returned. If the value of A is greater than or equal to the value of B and less than or equal to the value of C, True is returned. Otherwise, False is returned. The emp table contains the following data:

```
| empno | ename | job | mgr | hiredate| sal| comm | deptno |
7369,SMITH,CLERK,7902,1980-12-17 00:00:00,800,,20 7499,ALLEN,SALESMAN,7698,1981-02-20 00:00:00,1600,300,30 7521,WARD,SALESMAN,7698,1981-02-22 00:00:00,1250,500,30 7566,JONES,MANAGER,7839,1981-04-02 00:00:00,2975,,20 7654,MARTIN,SALESMAN,7698,1981-09-28 00:00:00,1250,1400,30 7698,BLAKE,MANAGER,7839,1981-05-01 00:00:00,2850,,30 7782,CLARK,MANAGER,7839,1981-06-09 00:00:00,2450,,10 7788,SCOTT,ANALYST,7566,1987-04-19 00:00:00,3000,,20 7839,KING,PRESIDENT,,1981-11-17 00:00:00,5000,,10 7844,TURNER,SALESMAN,7698,1981-09-08 00:00:00,1500,0,30 7876,ADAMS,CLERK,7788,1987-05-23 00:00:00,1100,,20 7900,JAMES,CLERK,7698,1981-12-03 00:00:00,950,,30 7902,FORD,ANALYST,7566,1981-12-03 00:00:00,3000,,20 7934,MILLER,CLERK,7782,1982-01-23 00:00:00,1300,,10 7948,JACCKA,CLERK,7782,1981-04-12 00:00:00,5000,,10 7956,WELAN,CLERK,7649,1982-07-20 00:00:00,2450,,10 7956,TEBAGE,CLERK,7748,1982-12-30 00:00:00,1300,,10
```

Query the data with sal greater than or equal to 1000 and less than or equal to 1500.

```
select * from emp where sal BETWEEN 1000 and 1500; -- The following result is returned: +-------+-------+-----+------------+------------+------------+------------+------------+
| empno | ename | job | mgr        | hiredate   | sal        | comm       | deptno     |
+-------+-------+-----+------------+------------+------------+------------+------------+
| 7521  | WARD  | SALESMAN | 7698  | 1981-02-22 00:00:00 | 1250.0     | 500.0      | 30  |
| 7654  | MARTIN | SALESMAN | 7698 | 1981-09-28 00:00:00 | 1250.0     | 1400.0     | 30 |
| 7844  | TURNER | SALESMAN | 7698 | 1981-09-08 00:00:00 | 1500.0     | 0.0        | 30 |
| 7876  | ADAMS | CLERK | 7788  | 1987-05-23 00:00:00 | 1100.0     | NULL     | 20   |
| 7934  | MILLER | CLERK | 7782  | 1982-01-23 00:00:00 | 1300.0     | NULL      | 10  |
| 7956  | TEBAGE | CLERK | 7748  | 1982-12-30 00:00:00 | 1300.0     | NULL      | 10  |
+-------+-------+-----+------------+------------+------------+------------+------------+
```

###### 3.6.6.23.11 NVL

MaxCompute allows you to use the NVL function to replace a null value in a query with a specific value. This way, no unexpected null values are included in the returned result during data analysis or report generation. This topic describes how to use the NVL function in MaxCompute.

**Syntax**

```
nvl(T <value>, T <default_value>)
```

**Parameters**

**value**: required. The input parameter. `T` specifies the type of input data. The type can be a data type supported
by MaxCompute.
**default_value**: required. The value that is used to replace null. The data type of default_value must be the same as
the data type of **value**.

**Return value**

If `value` is null, `default_value` is returned. Otherwise, `value` is returned. The value and default_value parameters must be of the same data type.

**Sample data**

This section provides sample source data to demonstrate how to use the NVL function. In this example, a table named nvl_test is created and data is added to the table. Sample statement:

```
CREATE TABLE nvl_test (
  c1 string,
  c2 bigint,
  c3 datetime);
 -- Insert data into the table.
INSERT INTO nvl_test VALUES
 ('aaa',23,'2024-01-11 00:00:00'),
 ('bbb',NULL,'2024-01-12 08:00:00'),
 (NULL,20,'2024-01-13 05:00:00'),
 ('ddd',25,NULL);
```

The nvl_test table contains the following columns: `c1` , `c2` , and `c3` . The NVL function replaces a null value in the c1 column with `00000` , replaces a null value in the c2 column with `0` , and replaces a null value in the c3 column with a `hyphen (-)` . Sample statement:

```
SELECT nvl(c1,'00000'),nvl(c2,0),nvl(c3,'-') FROM nvl_test; -- The following result is returned: +-----+------------+-----+
| _c0 | _c1        | _c2 |
+-----+------------+-----+
| aaa | 23         | 2024-01-11 00:00:00 |
| bbb | 0          | 2024-01-12 08:00:00 |
| 00000 | 20         | 2024-01-13 05:00:00 |
| ddd | 25         | -   |
+-----+------------+-----+
```

###### 3.6.6.23.12 TABLE_EXISTS

This topic describes the TABLE_EXISTS function and provides an example of using this function. Function declaration:

```
boolean table_exists(string table_name)
```

Description: This function checks whether a specific table exists. Parameters:
**table_name**: the table name of the STRING type. The value can include the project name, such as my_proj.my_table. If
no project name is specified, the name of the current project is used. Return value: A value of the BOOLEAN type is returned. If the specified table exists, True is returned. Otherwise, False is returned. Example:

```
-- Use this function in a SELECT statement. select if(table_exists('abd'), col1, col2) from src;
```

###### 3.6.6.23.13 PARTITION_EXISTS

This topic describes the PARTITION_EXISTS function and provides an example of using this function. Function declaration:

```
boolean partition_exists(string table_name, string... partitions)
```

Description: This function checks whether a specific partition exists. Parameters:
**table_name**: the table name of the STRING type. The value can include the project name, such as
my_proj.my_table. If no project name is specified, the name of the current project is used.
**partitions**: the partition names of the STRING type. In this parameter, you must specify the values of partition key
columns in a table based on the sequence of these columns. The number of values must be the same as the number of partition key columns. Return value: A value of the BOOLEAN type is returned. If the specified partitions exist, True is returned. Otherwise, False is returned. Example:

```
create table foo (id bigint) partitioned by (ds string, hr string); -- Create a partitioned table named foo. alter table foo add partition (ds='20190101', hr='1'); -- Add a partition to foo. select partition_exists('foo', '20190101', '1'); -- Check whether partitions with ds='20190101' and hr='1' exist.
```

### 3.7 UDFs

#### 3.7.1 Java UDFs

##### 3.7.1.1 Overview

This topic describes user-defined functions (UDFs) in MaxCompute. MaxCompute offers a variety of built-in functions to meet your computing requirements. You can also create UDFs. UDFs work in a way similar to built-in functions. For the mapping between Java and MaxCompute data types, see Types of parameters and returned values. If a UDF has the same name as a built-in function, MaxCompute executes the UDF by default. To call the built-in function, you must execute the select ::Function name (expression) ; statement. For example, if a UDF in MaxCompute is named CONCAT, MaxCompute calls the UDF rather than the CONCAT built-in function. To call the CONCAT built-in function, execute the select ::concat('ab', 'c') ; statement. The following table describes three types of UDFs supported by MaxCompute.

| UDF type | Description |
|---|---|
| UDF | User-defined scalar function. The input and output of a user-defined scalar function have a one-to-one mapping relationship. Every time a user-defined scalar function reads one row of data, one value is returned. |
| UDTF | User-defined table-valued function. A UDTF is used in scenarios in which multiple rows of data are returned after you call the function. Only this type of function can return multiple fields. A UDTF is not equivalent to a user-defined type (UDT). |
| UDAF | User-defined aggregate function. The input and output of a user-defined aggregate function have a many-to-one mapping relationship. Multiple input records are aggregated to generate one output value. This type of function can be used with the GROUP BY clause of SQL. |

When you use a UDF in an SQL statement, the system may prompt insufficient memory. The reason is that the memory size required for the computing task exceeds the default memory size. In this case, you can execute the set odps.sql.udf.joiner.jvm.memory=xxxx; statement to adjust the memory size. MaxCompute UDFs can be shared by multiple projects. UDFs in one project can be used in another project. SQL statement for cross-project UDF sharing:

```
select other_project:udf_in_other_project(arg0, arg1) as res from table_t;
```

If you use Maven, you can obtain the dependency from the Maven repository.

```xml
<dependency>
    <groupId>com.aliyun.odps</groupId>
    <artifactId>odps-sdk-udf</artifactId>
   <version>0.29.10-public</version>
</dependency>
```

##### 3.7.1.2 Types of parameters and return values

This topic describes the types of parameters and return values of user-defined functions (UDFs) in MaxCompute. Java UDFs in MaxCompute V2.0 support more basic data types in addition to BIGINT, STRING, DOUBLE, and BOOLEAN. These UDFs also support complex data types, such as ARRAY, MAP, and STRUCT, as well as Writable types. To use a new basic data type, UDFs specify their function signatures in the following ways: A user-defined aggregate function (UDAF) or user-defined table-valued function (UDTF) uses the **@Resolve** annotation, for example, `@Resolve("smallint->varchar(10)")` . A user-defined scalar function uses the **evaluate** method. In this case, the built-in function types of MaxCompute and Java function types have a one-to-one mapping relationship.

**Important**

You can use `type,*` to pass any number of parameters, for example, @resolve("string,*- >array<string>"). You must add Subtype after ARRAY. The field name and field type of com.aliyun.odps.data.Struct cannot be reflected. Therefore, you must use the @Resolve annotation to obtain the field name and field type. In other words, to use STRUCT in a UDF, you must add the @Resolve annotation to the UDF class. This annotation affects only the overloads of parameters or return values that contain com.aliyun.odps.data.Struct. Only one @Resolve annotation can be provided for the class. Therefore, only one overload with a STRUCT parameter or return value exists in a UDF. To use a complex data type, UDFs specify their function signatures in the following ways: A UDTF uses the **@Resolve** annotation, for example, `@Resolve("array<string>,struct<a1:bigint,b1:string>,string-`

```
>map<string,bigint>,struct<b1:bigint>") .
```

A user-defined scalar function uses the signature of the **evaluate** method to match input and output types. This involves the following mapping between MaxCompute and Java data types: ARRAY in MaxCompute maps to **java.util.List**. MAP in MaxCompute maps to **java.util.Map**. STRUCT in MaxCompute maps to **com.aliyun.odps.data.Struct**. A UDAF uses the **@Resolve** annotation, for example, `@Resolve("smallint->varchar(10)")` . The following table describes the mapping between MaxCompute and Java data types.

| MaxCompute data type | Java data type |
|---|---|
| TINYINT | java.lang.Byte |
| SMALLINT | java.lang.Short |
| INT | java.lang.Integer |
| BIGINT | java.lang.Long |
| FLOAT | java.lang.Float |
| DOUBLE | java.lang.Double |
| DECIMAL | java.math.BigDecimal |
| BOOLEAN | java.lang.Boolean |
| STRING | java.lang.String |
| VARCHAR | com.aliyun.odps.data.Varchar |
| BINARY | com.aliyun.odps.data.Binary |
| DATETIME | java.util.Date |
| TIMESTAMP | java.sql.Timestamp |
| ARRAY | java.util.List |
| MAP | java.util.Map |
| STRUCT | com.aliyun.odps.data.Struct |

Make sure that the input and output parameters in a UDF are of a Java type. Otherwise, error ODPS-0130071 is returned. Java data types and the data types of return values are objects. Java data types must start with an uppercase letter. The NULL value in SQL statements is represented by a NULL reference in Java. Java Primitive Type cannot have NULL values and must not be used. The ARRAY type in the preceding table maps java.util.List. MaxCompute V2.0 allows you to use Writable types as parameters and return values when you define Java UDFs. The following table describes the mapping between MaxCompute data types and Java Writable types.

| MaxCompute data type | Java Writable type |
|---|---|
| TINYINT | ByteWritable |
| SMALLINT | ShortWritable |
| INT | IntWritable |
| BIGINT | LongWritable |
| FLOAT | FloatWritable |
| DOUBLE | DoubleWritable |
| DECIMAL | BigDecimalWritable |
| BOOLEAN | BooleanWritable |
| STRING | Text |
| VARCHAR | VarcharWritable |
| BINARY | BytesWritable |
| DATETIME | DatetimeWritable |
| TIMESTAMP | TimestampWritable |
| INTERVAL YEAR MONTH _ _ | IntervalYearMonthWritable |
| INTERVAL DAY TIME _ _ | IntervalDayTimeWritable |
| ARRAY | N/A |
| MAP | N/A |
| STRUCT | N/A |

##### 3.7.1.3 UDF

This topic describes user-defined scalar functions (UDFs) and provides examples of using UDFs. UDFs must inherit the class **com.aliyun.odps.udf.UDF** and implement the **evaluate** method of the class. The
**evaluate** method must be a non-static public method, and the types of parameters and return values are used as the
UDF signature in SQL statements. You can implement multiple **evaluate** methods in a UDF. To call a UDF, the framework matches the correct **evaluate** method based on the parameter type called by the UDF. We recommend that you do not use the classes that have the same name but different function logic in different JAR packages. For example, in **UDF(UDAF/UDTF): udf1, udf2**, the JAR package of udf1 is
**udf1.jar** and the JAR package of udf2 is **udf2.jar**. Assume that the two JAR packages contain the
**com.aliyun.UserFunction.class** class. If you use the two UDFs in the same SQL statement, the system
randomly loads the class contained in one of the two JAR packages. This may cause the UDFs to be executed in different ways or even cause a compilation failure. If you execute an SQL statement that has two UDFs, the UDFs are not isolated from each other. This is because the UDFs share the same classpath. If the resources referenced by the UDFs contain the same class, the class that the classloader attempts to load is uncertain. To avoid this issue, make sure that the resources referenced by the two UDFs do not contain the same class. You can use `void setup(ExecutionContext ctx)` to initialize a UDF and use `void close()` to terminate a UDF. The following example shows how to implement a UDF:

```java
package org.alidata.odps.udf.examples;
  import com.aliyun.odps.udf.UDF;
public final class Lower extends UDF {
  public String evaluate(String s) {
    if (s == null) {
        return null;
```

`}`

```
        return s.toLowerCase();
```

`}` `}` The following example shows how to implement Concat by using a Writable type:

```java
package com.aliyun.odps.udf.example; import com.aliyun.odps.io.Text; import com.aliyun.odps.udf.UDF; public class MyConcat extends UDF {
  private Text ret = new Text();
  public Text evaluate(Text a, Text b) {
    if (a == null || b == null) {
      return null;
```

`}`

```
    ret.clear();
    ret.append(a.getBytes(), 0, a.getLength());
    ret.append(b.getBytes(), 0, b.getLength());
    return ret;
```

`}` `}`

##### 3.7.1.4 UDAF

This topic describes user-defined aggregate functions (UDAFs) and provides examples of using UDAFs. UDAFs must inherit the **com.aliyun.odps.udf.Aggregator** class and implement the following methods:

```java
import com.aliyun.odps.udf.ContextFunction; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; public abstract class Aggregator implements ContextFunction {
    @Override
    public void setup(ExecutionContext ctx) throws UDFException {
```

`}`

```java
    @Override
    public void close() throws UDFException {
```

`}`

```
    /**
     * Create an aggregation buffer * @return Writable aggregation buffer
```

`*/`

```
    abstract public Writable newBuffer();
    /**
     * @param buffer: aggregation buffer * @param args: a parameter specified to call a UDAF in SQL. It cannot
be NULL, but the values in args can be NULL, which indicates that the input data is NULL * @throws UDFException.
```

`*/`

```
    abstract public void iterate(Writable buffer, Writable[] args) throws UDFException;
    /**
     * Generate the final result * @param buffer * @return Final result of Object UDAF * @throws UDFException.
```

`*/`

```
    abstract public Writable terminate(Writable buffer) throws UDFException;
    abstract public void merge(Writable buffer, Writable partial) throws UDFException;
```

`}` The most important methods are **iterate**, **merge**, and **terminate** because the main logic of UDAFs relies on these methods. In addition, you must implement the user-defined Writable buffer. The following figure illustrates the implementation logic and procedure to calculate the **avg** value by using a MaxCompute UDAF. In the preceding figure, the input data is sliced based on the specified size. The size of each slice is suitable for a worker to complete the calculation in a specified time. The slice size must be manually configured. The calculation procedure of a UDAF involves two steps: Step 1: Each worker counts the data quantity and total sum in a slice. You can consider the data quantity and total sum in each slice as an intermediate result. Step 2: Each worker gathers the information about each slice generated in Step 1. In the final output, **r.sum/r.count** is the average value of all input data. Sample code for a UDAF that is used to calculate the average value:

```java
import java.io.DataInput; import java.io.DataOutput; import java.io.IOException; import com.aliyun.odps.io.DoubleWritable; import com.aliyun.odps.io.Writable; import com.aliyun.odps.udf.Aggregator; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve("double->double") public class AggrAvg extends Aggregator {
  private static class AvgBuffer implements Writable {
    private double sum = 0;
    private long count = 0;
    @Override
    public void write(DataOutput out) throws IOException {
      out.writeDouble(sum);
      out.writeLong(count);
```

`}`

```java
    @Override
    public void readFields(DataInput in) throws IOException {
      sum = in.readDouble();
      count = in.readLong();
```

`}` `}`

```java
  private DoubleWritable ret = new DoubleWritable();
  @Override
  public Writable newBuffer() {
    return new AvgBuffer();
```

`}`

```java
  @Override
  public void iterate(Writable buffer, Writable[] args) throws UDFException {
    DoubleWritable arg = (DoubleWritable) args[0];
    AvgBuffer buf = (AvgBuffer) buffer;
    if (arg ! = null) {
      buf.count += 1;
      buf.sum += arg.get();
```

`}` `}`

```java
  @Override
  public Writable terminate(Writable buffer) throws UDFException {
    AvgBuffer buf = (AvgBuffer) buffer;
    if (buf.count == 0) {
      ret.set(0);
    } else {
      ret.set(buf.sum / buf.count);
```

`}`

```
    return ret;
```

`}`

```java
  @Override
  public void merge(Writable buffer, Writable partial) throws UDFException {
    AvgBuffer buf = (AvgBuffer) buffer;
    AvgBuffer p = (AvgBuffer) partial;
    buf.sum += p.sum;
    buf.count += p.count;
```

`}` `}` Sample code for implementing Concat by using Writable types:

```java
package com.aliyun.odps.udf.example; import com.aliyun.odps.io.Text; import com.aliyun.odps.udf.UDF; public class MyConcat extends UDF {
  private Text ret = new Text();
  public Text evaluate(Text a, Text b) {
    if (a == null || b == null) {
      return null;
```

`}`

```
    ret.clear();
    ret.append(a.getBytes(), 0, a.getLength());
    ret.append(b.getBytes(), 0, b.getLength());
    return ret;
```

`}` `}`

##### 3.7.1.5 UDTFs

###### 3.7.1.5.1 Overview

This topic describes user-defined table-valued functions (UDTFs) and provides examples of using UDTFs. UDTFs must inherit the **com.aliyun.odps.udf.UDTF** class and implement four methods. The following table describes the methods.

| Method | Description |
|---|---|
| public void setup(ExecutionContext ctx) throws UDFException | The initialization method to call the user-defined initialization behavior before a UDTF processes the input data. setup is called once first for each worker. |
| public void process(Object[] args) throws UDFException | This method is called by the framework. Each SQL record calls process once. The parameters of process are the input parameters of the UDTF specified in the SQL statement. The input parameters are passed in as Object[], and the results are returned by using the forward function. You must call forward in the process function to determine the output data. |
| public void close() throws UDFException | The method for terminating a UDTF. The framework calls this method only once. The method is called after the last record is processed. |
| public void forward(Object ...o) throws UDFException | You can call the forward method to return data. One record is returned each time forward is called. The record corresponds to the column specified by the AS clause in the SQL statement of the UDTF. |

Example:

```java
package org.alidata.odps.udtf.examples; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.UDTFCollector; import com.aliyun.odps.udf.annotation.Resolve; import com.aliyun.odps.udf.UDFException; // TODO define input and output types, e.g., "string,string->string,bigint".
   @Resolve("string,bigint->string,bigint")
   public class MyUDTF extends UDTF {
     @Override
     public void process(Object[] args) throws UDFException {
       String a = (String) args[0];
       Long b = (Long) args[1];
       for (String t: a.split("\\s+")) {
         forward(t, b);
```

`}` `}` `}` Assume that you create a UDTF in MaxCompute with the registered function name of user_udtf. Execute the following statement to use the UDTF:

```
select user_udtf(col0, col1) as (c0, c1) from my_table;
```

The following example shows the values of col0 and col1 in my_table.

```
+------+------+
| col0 | col1 |
+------+------+
| A B  | 1    |
| C D  | 2    |
+------+------+
```

The following example shows the execution result of the SELECT statement.

```
+----+----+
| c0 | c1 |
+----+----+
| A  | 1  |
| B  | 1  |
| C  | 2  |
| D  | 2  |
+----+----+
```

###### 3.7.1.5.2 Examples of using UDTFs

This topic provides examples of using UDTFs.

**Use a UDTF to read resources in MaxCompute**

You can use a UDTF to read resources in MaxCompute. Example:
1. Compile a UDTF program. After the compilation is successful, export the JAR package. In this example, the JAR
package is named udtfexample1.jar.

```java
package com.aliyun.odps.examples.udf; import java.io.BufferedReader; import java.io.IOException; import java.io.InputStream; import java.io.InputStreamReader; import java.util.Iterator; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.annotation.Resolve; /**
 * project: example_project
 * table: wc_in2
 * partitions: p2=1,p1=2
 * columns: colc,colb
```

`*/`

```java
@Resolve("string,string->string,bigint,string") public class UDTFResource extends UDTF {
  ExecutionContext ctx;
  long fileResourceLineCount;
  long tableResource1RecordCount;
  long tableResource2RecordCount;
  @Override
  public void setup(ExecutionContext ctx) throws UDFException {
  this.ctx = ctx;
  try {
   InputStream in = ctx.readResourceFileAsStream("file_resource.txt");
   BufferedReader br = new BufferedReader(new InputStreamReader(in));
   String line;
   fileResourceLineCount = 0;
   while ((line = br.readLine()) ! = null) {
     fileResourceLineCount++;
```

`}`

```
   br.close();
   Iterator<Object[]> iterator = ctx.readResourceTable("table_resource1").iterator();
   tableResource1RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource1RecordCount++;
     iterator.next();
```

`}`

```
   iterator = ctx.readResourceTable("table_resource2").iterator();
   tableResource2RecordCount = 0;
   while (iterator.hasNext()) {
     tableResource2RecordCount++;
     iterator.next();
```

`}`

```
 } catch (IOException e) {
   throw new UDFException(e);
```

`}` `}`

```java
   @Override
   public void process(Object[] args) throws UDFException {
     String a = (String) args[0];
     long b = args[1] == null ? 0 : ((String) args[1]).length();
     forward(a, b, "fileResourceLineCount=" + fileResourceLineCount + "|tableResource1RecordCount="
     + tableResource1RecordCount + "|tableResource2RecordCount=" + tableResource2RecordCount);
```

`}` `}`
2. Add resources to MaxCompute.

```
Add file file_resource.txt; Add jar udtfexample1.jar; Add table table_resource1 as table_resource1; Add table table_resource2 as table_resource2;
```

3. Create the my_udtf UDTF in MaxCompute.

```
create function mp_udtf as com.aliyun.odps.examples.udf.UDTFResource using 'udtfexample1.jar, file_resource.txt, table_resource1, table_resource2';
```

4. Run this UDTF.

```
select mp_udtf("10","20") as (a, b, fileResourceLineCount) from table_resource1;
```

Returned result:

```
+-------+------------+-------+
| a | b      | fileResourceLineCount |
+-------+------------+-------+
| 10    | 2          | fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 |
| 10    | 2          | fileResourceLineCount=3|tableResource1RecordCount=0|tableResource2RecordCount=0 |
+-------+------------+-------+
```

**Use complex data types in a UDF**

The following example defines a UDF with three overloads. The first overload uses the ARRAY type, the second overload uses the MAP type, and the third overload uses the STRUCT type. The third overload uses STRUCT as the data type of parameters or returned values. Therefore, the **@Resolve** annotation must be added to the UDF class to specify the STRUCT type.

```java
import com.aliyun.odps.udf.UDF; import com.aliyun.odps.udf.annotation.Resolve; @Resolve("struct,string->string") public class UdfArray extends UDF {
    public String evaluate(List vals, Long len) {
        return vals.get(len.intValue());
```

`}`

```
    public String evaluate(Map map, String key) {
        return map.get(key);
```

`}`

```
    public String evaluate(Struct struct, String key) {
        return struct.getFieldValue("a") + key;
```

`}` `}` You can pass complex data types into a UDF.

```
create function my_index as 'UdfArray' using 'myjar.jar'; select id, my_index(array('red', 'yellow', 'green'), colorOrdinal) as color_name from co
```

**Use Hive UDFs**

MaxCompute V2.0 supports Hive UDFs. Some Hive UDFs and UDTFs can be directly used in MaxCompute. MaxCompute V2.0 is compatible with Hive 2.1.0 and Hadoop 2.7.2. If you develop a UDF by using other versions of Hive or Hadoop, you may need to recompile the UDF on the compatible Hive or Hadoop version. The following example shows how to use a Hive UDF in MaxCompute:

```java
package com.aliyun.odps.compiler.hive; import org.apache.hadoop.hive.ql.exec.UDFArgumentException; import org.apache.hadoop.hive.ql.metadata.HiveException; import org.apache.hadoop.hive.ql.udf.generic.GenericUDF; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspector; import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspectorFactory; import java.util.ArrayList; import java.util.List; import java.util.Objects; public class Collect extends GenericUDF {
  @Override
  public ObjectInspector initialize(ObjectInspector[] objectInspectors) throws UDFArgumentException {
    if (objectInspectors.length == 0) {
      throw new UDFArgumentException("Collect: input args should >= 1");
```

`}`

```
    for (int i = 1; i < objectInspectors.length; i++) {
      if (objectInspectors[i] ! = objectInspectors[0]) {
        throw new UDFArgumentException("Collect: input oi should be the same for all args");
```

`}` `}`

```
    return ObjectInspectorFactory.getStandardListObjectInspector(objectInspectors[0]);
```

`}`

```java
  @Override
  public Object evaluate(DeferredObject[] deferredObjects) throws HiveException {
    List<Object> objectList = new ArrayList<>(deferredObjects.length);
    for (DeferredObject deferredObject : deferredObjects) {
      objectList.add(deferredObject.get());
```

`}`

```
    return objectList;
```

`}`

```java
  @Override
  public String getDisplayString(String[] strings) {
    return "Collect";
```

`}` `}` The Hive UDF in the example packages any type and number of parameters into arrays. In this example, the output JAR package is named test.jar.

```
-- Add a resource. Add jar test.jar; -- Create a Hive UDF. CREATE FUNCTION hive_collect as 'com.aliyun.odps.compiler.hive.Collect' using 'test.jar'; -- Use the Hive UDF. set odps.sql.hive.compatible=true; select hive_collect(4y,5y,6y) from dual;
```

Returned result:

```
+------+
| _c0  |
+------+
| [4, 5, 6] |
+------+
```

Take note of the following items when you use Hive UDFs that are compatible with MaxCompute: Specify the JAR package when you create a Hive UDF. MaxCompute cannot automatically add all JAR packages to the classpath. The `add jar` command in MaxCompute creates a permanent resource in the project. Insert set odps.sql.hive.compatible=true; before an SQL statement, and commit and execute the SET statement with the SQL statement. Pay attention to the limits imposed by the Java sandbox on MaxCompute.

#### 3.7.2 Python UDFs

##### 3.7.2.1 Before you start

This topic describes the prerequisites for the use of Python user-defined functions (UDFs). Before you use Python UDFs, you must enable the isolation sandbox for a specified project. For more information about how to enable an isolation sandbox, contact technical support.

##### 3.7.2.2 Limits

This topic describes limits on Python user-defined functions (UDFs). MaxCompute uses Python 2.7. User code runs in a sandbox, which is a limited environment. In this environment, the following operations are prohibited: Read and write local files. Start subprocesses. Start threads. Initiate socket-based communication. Call other systems. Due to these limits, the code that you upload must be implemented by standard Python, and C extension modules are not allowed in your code. In addition, the modules that involve the preceding operations are disabled in the Python standard library. The following modules are available in the standard library: The modules that are implemented by standard Python. The following C extension modules: audioop binascii _bisect cmath _codecs_cn _codecs_hk _codecs_iso2022 _codecs_jp _codecs_kr _codecs_tw _collections cStringIO datetime _functools future_builtins _hashlib _heapq itertools _json _locale _lsprof math _md5 _multibytecodec operator _random _sha256 _sha512 _sha _struct strop time unicodedata _weakref cPickle Some modules with limited functionality. For example, the size of data that your code can write into standard output sys.stdout and standard error output sys.stderr in a sandbox is limited to 20 KB. Characters that exceed this limit are ignored.

##### 3.7.2.3 Third-party libraries

This topic describes third-party libraries for Python user-defined functions (UDFs). Common third-party libraries such as NumPy are installed in the runtime environment to supplement the standard library.

**Warning**

The use of third-party libraries is also subject to limits. For example, when you use a third-party library, you are not allowed to access local data and you can use only limited network I/O resources. The related APIs in the third-party libraries are disabled.

##### 3.7.2.4 Types of parameters and return values

This topic describes the types of parameters and return values of Python user-defined functions (UDFs). The types of parameters and return values are specified by using the following method:

```
@odps.udf.annotate(signature)
```

Python UDFs support MaxCompute SQL data types, such as BIGINT, STRING, DOUBLE, BOOLEAN, DATETIME, DECIMAL, complex data types, and nested complex data types. Complex data types include ARRAY, MAP, and STRUCT. Before you execute an SQL statement, the types of parameters and return values of all functions must be determined. Python is a dynamically typed language. You must add decorators to the UDF class to specify the function signature. The function signature is specified by a string. The following syntax is supported:

```
arg_type_list '->' type_list arg_type_list: type_list | '*' | '' | 'char(n)' | 'varchar(n)' type_list: [type_list ','] type type: 'bigint' | 'string' | 'double' | 'boolean' | 'datetime' | 'float' | 'binary' | 'date' | 'decimal' | 'deci mal(precision,scale)'
```

The part to the left of the arrow indicates the types of parameters. The part to the right of the arrow indicates the types of return values. The return value of a UDTF can contain multiple columns, while the return value of a UDF or UDAF contains only one column. An asterisk (*) represents variable-length parameters. If variable-length parameters are used, UDFs, UDTFs, and UDAFs can match input parameters of any type. In a project that uses the MaxCompute V2.0 data type edition, you can set the **decimal** parameter to precision or scale. The return value cannot be of the CHAR or VARCHAR type. The following example shows a valid signature:

```
'bigint,double->string' # Parameters are of the BIGINT and DOUBLE types, and return values are of th e STRING type. 'bigint,boolean->string,datetime' # UDTF parameters are of the BIGINT and BOOLEAN types, and return values are of the STRING and DATETIME types. '*->string' # Input parameters are variable-length parameters and can be of any type, and return values are of the STRING type. '->double' # Parameters are left empty, and return values are of the DOUBLE type. 'array<bigint>->struct<x:string, y:int>' # Parameters are of the ARRAY<BIGINT> type, and return values are of t he STRUCT<x:STRING, y:BIGINT> type. '->map<bigint, string>' # Parameters are left empty, and return values are of the MAP<BIGINT, STRING> type.
```

If an invalid signature is found during query parsing, an error is reported, and the execution of the function is prohibited. During the execution of the function, the UDF parameters of the type specified by the function signature are passed. The return values must be of the same type as those specified by the function signature. Otherwise, an error is reported. The following table describes the mappings between Python data types and MaxCompute SQL data types.

| MaxCompute SQL data type | Python data type |
|---|---|

| BIGINT | INT |
|---|---|
| STRING | STR |
| DOUBLE | FLOAT |
| BOOLEAN | BOOL |
| DATETIME | INT |
| FLOAT | FLOAT |
| CHAR | STR |
| VARCHAR | STR |
| BINARY | BYTEARRAY |
| DATE | INT |
| DECIMAL | DECIMAL.DECIMAL |
| ARRAY | LIST |
| MAP | DICT |
| STRUCT | COLLECTIONS.NAMEDTUPLE |

A value of the DATETIME type is converted to a value of the INT type. The value of the INT type follows the UNIX format, which is the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970. You can process data of the DATETIME type by using the DATETIME module in the Python standard library.
**silent** is added to `odps.udf.int(value,[silent=True])` . If **silent** is set to True and **value** cannot be
converted to the INT type, None is returned, and no error is reported. The NULL value corresponds to None in Python.

##### 3.7.2.5 UDF

This topic describes user-defined scalar functions (UDFs) and provides an example of using UDFs. To implement Python UDFs, you must define a new-style class and implement the **evaluate** method.

```python
from odps.udf import annotate @annotate("bigint,bigint->bigint") class MyPlus(object):
   def evaluate(self, arg0, arg1):
       if None in (arg0, arg1):
           return None
       return arg0 + arg1
```

A Python UDF must have its signature specified by using **annotate**.

##### 3.7.2.6 UDAF

This topic describes user-defined aggregate functions (UDAFs) and provides an example of using UDAFs.
**class odps.udf.BaseUDAF**: is inherited to implement Python UDAFs.
**BaseUDAF.new_buffer()**: returns **buffer** of the intermediate value of a UDAF. **buffer** must be a marshallable
object (such as LIST or DICT), and the **buffer** size cannot increase with the data volume. Under extreme circumstances, the **buffer** size cannot exceed 2 MB after the marshal operation.
**BaseUDAF.iterate(buffer[, args, ...])**: aggregates **args** to **buffer** of the intermediate value.
**BaseUDAF.merge(buffer, pbuffer)**: aggregates **buffer** of two intermediate values. It merges **pbuffer** to **buffer**.
**BaseUDAF.terminate(buffer)**: converts **buffer** of the intermediate value to a value of a basic data type in
MaxCompute SQL. Example of using a UDAF to obtain the average value:

```python
@annotate('double->double') class Average(BaseUDAF):
    def new_buffer(self):
        return [0, 0]
    def iterate(self, buffer, number):
        if number is not None:
            buffer[0] += number
            buffer[1] += 1
    def merge(self, buffer, pbuffer):
        buffer[0] += pbuffer[0]
        buffer[1] += pbuffer[1]
    def terminate(self, buffer):
        if buffer[1] == 0:
            return 0.0
        return buffer[0] / buffer[1]
```

##### 3.7.2.7 UDTF

This topic describes user-defined table-valued functions (UDTFs) and provides an example of using UDTFs.
**class odps.udf.BaseUDTF**: the base class of Python UDTFs. This class can be inherited to implement the **PROCESS**
and **CLOSE** methods.
**BaseUDTF.__init__()**: the initialization method. To implement this method for a derived class, you must call the
**super(BaseUDTF, self).__init__()** initialization method of the base class at the beginning of code execution.
Throughout the lifecycle of a UDTF, the **INIT** method is called only once. It is called only before the first record is processed. If a UDTF needs to save internal states, all states can be initialized by using this method.
**BaseUDTF.process([args, ...])**: is called by the MaxCompute SQL framework. The **PROCESS** method is called for
each record in SQL. The parameters in the **PROCESS** method are the UDTF input parameters that are specified in SQL statements.
**BaseUDTF.forward([args, ...])**: the UDTF output method. This method is called by user code. One record is
generated each time the **FORWARD** method is called. The parameters in the **FORWARD** method are the UDTF output parameters that are specified in SQL statements.
**BaseUDTF.close()**: the UDTF termination method. This method is called only once by the MaxCompute SQL
framework. It is called only after the last record is processed. Example:

```python
#coding:utf-8
# explode.py
from odps.udf import annotate from odps.udf import BaseUDTF @annotate('string -> string') class Explode(BaseUDTF):
   # Use commas (,) to separate the string into multiple records.
   def process(self, arg):
       props = arg.split(',')
       for p in props:
           self.forward(p)
```

The types of parameters and the return value of a Python UDTF can be specified without the need to use **annotate** to specify the UDTF signature. This way, the function can match input parameters of any type in SQL. However, the type of the return value cannot be deduced. All output parameters are considered to be of the STRING type. Therefore, when **FORWARD** is called, all output values must be converted to the STRING type.

##### 3.7.2.8 Resource reference

This topic describes how to reference resources in Python user-defined functions (UDFs) and provides an example for reference. You can reference file and table resources in Python UDFs by using the **odps.distcache** module. The following sample code shows the syntax that is used to reference file resources:

```
odps.distcache.get_cache_file(resource_name) -- Return the content of a specified resource.
```

The **resource_name** parameter is a string that corresponds to the name of an existing file resource in the current project. If the resource name is invalid or the file resource does not exist, an error is returned. The return value is a file-like object. If this object is no longer used, the caller must call the `close` method to release the open file resource. Example:

```python
@annotate('bigint->string') class DistCacheExample(object): def __init__(self):
    cache_file = get_cache_file('test_distcache.txt')
    kv = {}
    for line in cache_file:
        line = line.strip()
        if not line:
            continue
        k, v = line.split()
        kv[int(k)] = v
    cache_file.close()
    self.kv = kv
def evaluate(self, arg):
    return self.kv.get(arg)
```

The following sample code shows the syntax that is used to reference table resources:

```
odps.distcache.get_cache_table(resource_name)
```

The **resource_name** parameter is a string that corresponds to the name of an existing table resource in the current project. If the resource name is invalid or the table resource does not exist, an error is returned. The return value is of the GENERATOR type. The caller traverses the table to obtain the content. A record of the ARRAY type is obtained each time the caller traverses the table. Example:

```python
from odps.udf import annotate from odps.distcache import get_cache_table @annotate('->string') class DistCacheTableExample(object):
    def __init__(self):
        self.records = list(get_cache_table('udf_test'))
        self.counter = 0
        self.ln = len(self.records)
    def evaluate(self):
        if self.counter > self.ln - 1:
            return None
        ret = self.records[self.counter]
        self.counter += 1
        return str(ret)
```

#### 3.7.3 Python 3 UDF

This topic describes the precautions when you use Python 3 user-defined functions (UDFs). Python Software Foundation announces the End of Life (EOL) for Python 2. Due to this reason, MaxCompute supports Python 3 and uses CPython 3.7.3. Python 3 is incompatible with Python 2. You can select Python 2 or Python 3 to execute an SQL statement. However, you cannot use Python 2 code and Python 3 code in a single SQL statement at the same time.

**Enable Python 3**

You can enable Python 3 only for jobs. To enable Python 3 for a job, add the following command before the required SQL statement and execute them together:

```
set odps.sql.python.version=cp37;
```

**Use third-party libraries**

MaxCompute Python UDFs support third-party libraries. The third-party library NumPy is installed in the Python 2 runtime environment to supplement the standard library. NumPy is not installed in the Python 3 runtime environment in MaxCompute. To use a NumPy UDF, you must manually upload a NumPy wheel package. If you download a NumPy wheel package from Python Package Index (PyPI), the package name is in the **numpy-<Version>-cp37-cp37m-manylinux1_x86_64.whl** format.

**Port Python 2 UDFs**

Python Software Foundation announced the EOL for Python 2. Therefore, we recommend that you port Python 2 UDFs. The method used to port Python 2 UDFs varies based on the types of MaxCompute projects. In a new project or an existing project for which you write UDFs in Python for the first time, we recommend that you use Python 3 to write all Python UDFs. In an existing project where a large number of Python 2 UDFs exist, proceed with caution when you enable Python 3. This is because you cannot use Python 2 code and Python 3 code in a single SQL statement at the same time. If you plan to gradually replace Python 2 UDFs with Python 3 UDFs, use the following methods: Use Python 3 to write new UDFs and enable Python 3 for new jobs. Rewrite Python 2 UDFs in a manner in which the UDFs are compatible with Python 2 and Python 3. For more information about how to rewrite UDFs, see Porting Python 2 Code to Python 3. If you write a public UDF that needs to be shared among multiple projects, we recommend that you write the UDF that is compatible with both Python 2 and Python 3.

#### 3.7.4 SQL Function

This topic describes how to use SQL functions. SQL functions allow you to reference SQL user-defined functions (UDFs) in SQL scripts. You can use SQL functions of MaxCompute to resolve the following issues: Generally, a large amount of similar code exists, which is inconvenient to maintain and prone to errors. To use UDFs, you must develop code, compile the code in Java, and then create resources and functions. The process is complicated. In addition, UDFs cannot catch up with built-in functions in terms of performance. Example:

```
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key1')), 'default') AS key1,
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.key2')), 'default') AS key2,
    ...
    NVL(STR_TO_MAP(GET_JSON_OBJECT(col, '$.keyN')), 'default') AS keyN
FROM t;
```

One function can be transferred as a parameter to another only by using code similar to lambda expressions in Java.

**Feature description**

As a type of UDFs, SQL functions allow you to create UDFs in SQL and use function type parameters and anonymous functions. This way, you can define business logic more flexibly. You can use SQL functions to simplify feature implementation and improve code reuse. SQL functions provide the following features: SQL functions allow you to reference and call SQL UDFs in SQL scripts. You can specify built-in functions, UDFs, or SQL functions in function type parameters when you call SQL functions. You can specify anonymous functions in function type parameters when you call SQL functions.

**Create a permanent SQL function**

After you create a permanent SQL function and store it in the metadata system, all query statements can reference this function. To reference SQL functions, you must have function-level permissions. The following example shows the

```
CREATE SQL FUNCTION function_name(@parameter_in1 datatype[, @parameter_in2 datatype...]) [RETURNS @parameter_out datatype] AS [BEGIN] function_expression [END];
```

Parameters:
**function_name**: the name of the SQL function that you want to create. Each function name must be unique and can
be registered only once. The SQL function names cannot be the same as those of built-in functions.
**parameter_in**: the input parameters of the SQL function.
**RETURNS**: the variable to be returned by the SQL function. If you do not specify RETURNS, the value of
function_name is returned.
**parameter_out**: the output parameters of the SQL function.
**function_expression**: the expression of the SQL function.
Example:

```
CREATE SQL FUNCTION MY_ADD(@a BIGINT) AS @a + 1;
```

In the preceding example, **@a + 1** indicates the implementation logic of the SQL function. You can write it as an expression to specify a built-in operator, built-in function, or UDF. If the implementation logic is complex, you can write multiple SQL statements and enclose them with BEGIN and END. RETURNS specifies the variable to be returned by the SQL function. If you do not specify RETURNS, the value of function_name is returned. Example:

```
CREATE SQL FUNCTION MY_SUM(@a BIGINT, @b BIGINT, @c BIGINT) RETURNS @my_sum BIGINT AS BEGIN
    @temp := @a + @b;
    @my_sum := @temp + @c;
END;
```

**Query an SQL function**

You can query an SQL function in the same way as querying a Java or Python UDF. Example:

```
DESC FUNCTION my_add;
```

**Delete an SQL function**

You can delete an SQL function in the same way as deleting a Java or Python UDF. Example:

```
DROP FUNCTION my_add;
```

**Call an SQL function**

You can call an SQL function in the same way as calling an existing built-in function. Example:

```
SELECT my_sum(col1, col2 ,col3) from t;
```

**Use temporary SQL functions**

You can use temporary SQL functions if you no longer need to save SQL functions to the metadata system of MaxCompute. The temporary SQL functions are valid only in the current script. Example:

```
FUNCTION MY_ADD(@a BIGINT) AS @a + 1; SELECT MY_ADD(key), MY_ADD(value) FROM src;
```

**Use function type parameters**

You can specify built-in functions, UDFs, or SQL functions in function type parameters when you call SQL functions. Example:

```
FUNCTION ADD(@a BIGINT) AS @a + 1; FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, ADD), OP(key, ABS) FROM VALUES (1),(2) AS t (key);
```

Returned results:

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| 2          | 1          |
| 3          | 2          |
+------------+------------+
```

In this example, two input parameters are specified for the OP function. The **@a** parameter specifies a value of the BIGINT type. The **@fun** parameter specifies a function whose input and output parameters are both of the BIGINT type. The OP function transfers **@a** to the function that is specified by **@fun** and then to the ADD and ABS functions for processing.

**Use anonymous functions**

You can specify anonymous functions in function type parameters when you call SQL functions. Example:

```
FUNCTION OP(@a BIGINT, @fun FUNCTION (BIGINT) RETURNS BIGINT) AS @fun(@a); SELECT OP(key, FUNCTION (@a) AS @a + 1) FROM VALUES (1),(2) AS t (key);
```

In this example, **FUNCTION (@a) AS @a + 1** is an anonymous function. You do not need to specify a data type for the input parameter **@a**. The compiler will infer the data type of **@a** based on the parameter definition of the OP function.

#### 3.7.5 Embedded UDF

##### 3.7.5.1 Background information

This topic describes the background information of code-embedded user-defined functions (UDFs). The code-embedded UDFs of MaxCompute resolve the following issues in code implementation and maintenance: Complicated code implementation: After you create UDFs and develop code, you must compile the code in Java and create resources and functions. Inconvenient code maintenance: You cannot directly view the implementation logic of the UDFs that are referenced in SQL scripts or obtain the source code of JAR packages. Poor code readability: To implement Java library functions by using user-defined types (UDTs), you must write Java code as expressions in long code lines. In addition, you may fail to write some Java code as expressions. Example:

```
Foo f = new Foo(); f.execute(); f.getResult();
```

##### 3.7.5.2 Feature summary

This topic describes the features of code-embedded user-defined functions (UDFs). Code-embedded UDFs allow you to embed Java or Python code into SQL scripts. When you compile a script, Janinocompiler identifies and extracts the embedded code, compiles the code in Java, and then dynamically generates resources and creates temporary functions. You can place SQL scripts and third-party code lines in the same source code file. This simplifies the usage of userdefined types (UDTs) or UDFs and facilitates routine development and maintenance.

##### 3.7.5.3 Limits

This topic describes the limits on code-embedded user-defined functions (UDFs). You can use only Janino-compiler to compile embedded Java code. The syntax of the embedded Java code must be a subset of the standard JDK syntax. Embedded Java code has the following limits: Lambda expressions are not supported. You cannot specify multiple types of exceptions in a single catch block, for example, **catch(Exception1 |**
**Exception2 e)**.
Generics cannot be automatically inferred, for example, **Map map = new HashMap<>();**. Expressions for type parameter inference are ignored and you must use cast expressions to specify the parameter type, for example, **(String) myMap.get(key)**. Assertions are forcibly enabled, even if the -ea option of the Java Virtual Machine (JVM) is used. Code that is programmed in versions later than Java 8 is not supported.

##### 3.7.5.4 Examples

This topic describes how to use code-embedded user-defined functions (UDFs) and provides examples for reference.

**Reference embedded code in a UDT**

`s,`

```java
  com.mypackage.Foo.extractNumber(s)
FROM VALUES ('abc123def'),('apple') AS t(s);
#CODE ('lang'='JAVA')
package com.mypackage; import java.util.regex.Matcher; import java.util.regex.Pattern; public class Foo {
  final static Pattern compile = Pattern.compile(".*?([0-9]+).*");
  public static String extractNumber(String input) {
    final Matcher m = compile.matcher(input);
    if (m.find()) {
      return m.group(1);
```

`}`

```
    return null;
```

`}` `}`

```
#END CODE;
```

Description:
**#CODE** indicates the beginning of the embedded code block. **#END CODE** indicates the end of the embedded code
block. In this example, the embedded code block is placed at the end of the script and applies to the whole script.
**'lang'='JAVA'** indicates that the embedded code is in Java. JAVA can be replaced with **PYTHON** if you compile code
in Python. You can use UDT syntax in the SQL script to call **Foo.extractNumber**.

**Define and call a Java code-embedded UDF**

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA')
package com.mypackage; import com.aliyun.odps.udf.UDF; public class Reverse extends UDF {
  public String evaluate(String input) {
    if (input == null) return null;
    StringBuilder ret = new StringBuilder();
    for (int i = input.toCharArray().length - 1; i >= 0; i--) {
      ret.append(input.toCharArray()[i]);
```

`}`

```
    return ret.toString();
```

`}` `}`

```
#END CODE;
SELECT foo('abdc');
```

Description: You can place the embedded code block next to **USING** or at the end of the script. If you place it next to **USING**, it

| CREATE TEMPORARY FUNCTION |   | state |
|---|---|---|
| d by | CREATE TEMPORARY FUNCTION |   |

The function created by `CREATE TEMPORARY FUNCTION` is a temporary function. This temporary function takes effect only during the current execution process and is not stored in the MaxCompute metadata system.

**Define and call a Java code-embedded UDTF**

```java
CREATE TEMPORARY FUNCTION foo AS 'com.mypackage.Reverse' USING
#CODE ('lang'='JAVA', 'filename'='embedded.jar')
package com.mypackage; import com.aliyun.odps.udf.UDTF; import com.aliyun.odps.udf.UDFException; import com.aliyun.odps.udf.annotation.Resolve; @Resolve({"string->string,string"}) public class Reverse extends UDTF {
  @Override
  public void process(Object[] objects) throws UDFException {
    String str = (String) objects[0];
    String[] split = str.split(",");
    forward(split[0], split[1]);
```

`}` `}`

```
#END CODE;
SELECT foo('ab,dc') AS (a,b);
```

The return value of **@Resolve** must be of the **string[]** type. However, Janino-compiler cannot identify **"string-**
**>string,string"** in embedded code as **string[]**. To enable Janino-compiler to identify **"string->string,string"** as
string[], "string->string,string" must be enclosed in braces {}. If you create a Java UDTF by using a common method, braces {} are not required.

**Define and call a Python code-embedded UDF**

```python
CREATE TEMPORARY FUNCTION foo AS 'embedded.UDFTest' USING
#CODE ('lang'='PYTHON', 'filename'='embedded')
from odps.udf import annotate @annotate("bigint->bigint") class UDFTest(object):
  def evaluate(self, a):
    return a * a
#END CODE;
SELECT foo(4);
```

Description: The indentation of Python code must comply with the specifications of the Python language. When you create a Python UDF, the class name that follows the **AS** clause must contain the file name of the Python source code. You can use `'filename'='embedded'` to specify a virtual file name.

### 3.8 UDTs

#### 3.8.1 Scenarios and limits

This topic describes the scenarios and limits of user-defined types (UDTs). MaxCompute introduces UDTs based on the new-generation SQL engine. UDTs allow you to reference classes or objects of third-party programming languages in SQL statements to call methods or obtain data. UDTs are suitable for the following scenarios: You want to use some features that are not provided by MaxCompute but can be implemented in other programming languages. For example, to implement some features, you need only to call built-in Java classes once. However, MaxCompute does not provide methods to implement these features. If you use user-defined functions (UDFs) to run these tasks, the procedure is complex. You want to call a third-party library in SQL statements to implement the related features. In this scenario, UDFs allow you to directly use a function provided by a third-party library in a SQL statement, instead of wrapping the function inside a UDF. You want to directly call the source code of a third-party programming language in SQL statements. The SELECT TRANSFORM statement allows you to write scripts to SQL statements. This improves readability and facilitates code maintenance. For some programming languages, such as Java, the source code can be executed only after it is compiled. You can use UDTs to reference objects and classes of these languages in SQL statements. UDTs support only Java. By default, all classes of SDK for Java can be referenced by UDTs. JDK 1.8 is used. A version later than JDK 1.8 may not be supported. All operators use the semantics of MaxCompute SQL instead of UDTs. UDTs cannot be used as shuffle keys in clauses, such as JOIN, GROUP BY, DISTRIBUTE BY, SORT BY, ORDER BY, or CLUSTER BY. DDL statements do not support UDTs. You cannot create tables that contain UDT objects. The final output cannot be UDT types.

#### 3.8.2 Feature summary

This topic describes the features of user-defined types (UDTs) and provides examples for reference. UDTs supported by many SQL engines are similar to the STRUCT type in MaxCompute. UDTs supported by MaxCompute are similar to the CREATE TYPE statement. A UDT contains both fields and methods. You do not need to use data definition language (DDL) statements to define new data types in MaxCompute. Instead, MaxCompute allows you to reference new data types directly in SQL statements. The following examples show how to use UDTs. For example, to call the java.lang package in SQL statements, you can use one of the following methods: Use UDTs to call the java.lang package

```
-- Enable new data types. A new type of INTEGER (INT) is used in this example. set odps.sql.type.system.odps2=true; SELECT java.lang.Integer.MAX_VALUE;
```

Based on Java conventions, you can also omit the java.lang package from the preceding statement and use the following statement:

```
set odps.sql.type.system.odps2=true; SELECT Integer.MAX_VALUE;
```

Returned results:

```
+-----------+
| max_value |
+-----------+
| 2147483647 |
+-----------+
```

Use user-defined functions (UDFs) to call the java.lang package i. Define a UDF class.

```java
package com.aliyun.odps.test; public class IntegerMaxValue extends com.aliyun.odps.udf.UDF {
  public Integer evaluate() {
     return Integer.MAX_VALUE;
```

`}` `}` ii. Compile the UDF into a JAR package, upload the package, and create a function.

```
add jar odps-test.jar; create function integer_max_value as 'com.aliyun.odps.test.IntegerMaxValue' using 'odps-test.jar';
```

iii. Call the function in the SQL statement.

```
select integer_max_value();
```

In this example, UDTs simplify the procedure for you to use other programming languages to extend SQL features.

#### 3.8.3 Implementation principles and feature description

This topic describes the implementation principles of user-defined types (UDTs) and their features.

**Implementation principles**

The following example shows how to run a UDT:

```
-- Sample data. @table1 := select * from values ('100000000000000000000') as t(x); @table2 := select * from values (100L) as t(y); -- Code logic. -- Create an object by using the new method. @a := select new java.math.BigInteger(x) x from @table1; -- Call a static method. @b := select java.math.BigInteger.valueOf(y) y from @table2; -- Call an instance method. select /*+mapjoin(b)*/ x.add(y).toString() from @a a join @b b;
```

Returned results:

```
100000000000000000100
```

The following figure shows the process. This UDT has three stages: M1, R2, and J3. If a **JOIN** operation is used in MapReduce, data must be reshuffled. As a result, data is processed at multiple stages. The processes and physical machines that process data vary at different stages. Only the `new java.math.BigInteger(x)` method is called at the M1 stage. The `java.math.BigInteger.valueOf(y)` and `x.add(y).toString()` methods are separately called at the J3 stage. These methods are called at different stages and executed in different processes and on different physical machines. UDTs encapsulate these stages to achieve an effect similar to all the stages being implemented on the same Java Virtual Machine (JVM). The preceding example shows that the result of a subquery supports UDT columns. The x column retrieved by variable a is of the **java.math.BigInteger** type rather than a built-in type. You can transfer the UDT data to another operator and then call its method. You can also use the UDT data in a data shuffle.

**Feature description**

UDTs support only Java. By default, all classes of SDK for Java can be referenced by UDTs. UDTs also allow you to upload JAR packages and directly reference these packages. Some flags are provided for UDTs.
**set odps.sql.session.resources**: specifies the resource that you want to reference. Separate multiple resources

| with commas (,). For example, you can set this flag to | foo.sh,bar.txt | . |
|---|---|---|
| Note This flag works the same as the flag used to specify resources in the SELECT TRANSFORM statement. Therefore, this flag controls two features. set odps.sql.type.system.odps2=true; set odps.sql.session.resources=odps-test.jar; -- Specify the JAR package that you want to reference. You must upload the package to your project in a dvance. select new com.aliyun.odps.test.IntegerMaxValue().evaluate(); |   |   |

**odps.sql.session.java.imports**: specifies the default Java package. You can specify multiple packages and
separate them with commas (,). This flag is similar to the **IMPORT** statement in Java. You can specify a class path, such as java.math.BigInteger, or use asterisks (*). **static import** is not supported.

```
set odps.sql.type.system.odps2=true; set odps.sql.session.resources=odps-test.jar; set odps.sql.session.java.imports=com.aliyun.odps.test. *; -- Specify the default JAR package. select new IntegerMaxValue().evaluate();
```

UDTs support resource access. In MaxCompute SQL, you can call the static method `com.aliyun.odps.udf.impl.UDTExecutionContext.get()` to obtain the **ExecutionContext** object. Then, you can use this object to access the current **ExecutionContext** class and then access resources, such as files or tables. UDTs support the following operations:

|   | new |
|---|---|
| new |   |

Create objects by using the `new` method. Create arrays by using the `new` method. Initializer lists can be used. Example: `new Integer[] { 1, 2, 3 }` . Call methods, including static methods. The identifiers in UDTs contain the names of packages, classes, methods, and fields. All identifiers are case-sensitive. Anonymous classes and lambda expressions are not supported. UDTs are used in expressions. Functions that do not return values cannot be called in expressions. This issue will be resolved in later versions. UDTs support the following data types: UDTs support SQL type conversions, such as `cast(1 as java.lang.Object)` . UDTs do not support Java type conversions, such as `(Object)1` . The built-in types of UDTs have a one-to-one mapping relationship with specific Java types. You can directly call the method of the Java type to which the built-in type is mapped. Example: `'123'.length()`

```
, 1L.hashCode() .
```

UDTs can be used in built-in functions and UDFs. For example, in `chr(Long.valueOf('100'))` , **Long.valueOf** returns a value of the **java.lang.Long** type. The built-in function CHR supports the built-in BIGINT type. The data of a Java primitive type is automatically converted to the boxing type and the preceding two rules apply. For some new built-in data types, you must use set odps.sql.type.system.odps2=true; to declare these types. Otherwise, an error occurs. The following type conversion rules apply in UDTs: UDT objects can be implicitly converted to the objects of their base classes. UDT objects can be forcibly converted to the objects of their base classes or subclasses. The data type conversion between two objects without inheritance follows the original conversion rules. However, such conversions may result in changes to the data. For example, data of the **java.lang.Long** type can be forcibly converted to the **java.lang.Integer** type. This conversion uses the rules that are used to convert the built-in BIGINT type to the INT type. This process may result in changes to the data and even loss of data precision. UDTs support Java generics. For example, the compiler can determine that the value returned by `java.util.Arrays.asList(new java.math.BigInteger('1'))` is of the **java.util.List<java.math.BigInteger>** type based on the parameter type. You must specify the type parameter in a constructor function or use **java.lang.Object**. This is the same as Java. All operators use the semantics of MaxCompute SQL. Examples: Combination of strings: The result of `String.valueOf(1) + String.valueOf(2)` is 3. The two strings are implicitly converted to DOUBLE-type values and summed. If you use Java string concatenation to combine the strings, the result is 12.
**=** operations: The **=** operator in SQL statements is used as a comparison operator. It is used to compare one
expression with another. You must call the equals method in Java to check whether two objects are equivalent. The **=** operator cannot be used to verify the equivalence of two objects. UDTs do not have a clear definition of object equality. This is caused by data reshuffling. Objects may be transmitted between different processes or physical machines. During object transmission, an object may be referenced as two different objects. For example, an object may be shuffled to two machines and then reshuffled. Therefore, when you use UDTs, you must use the equals method instead of the **=** operator to verify the equivalence of two objects. Objects in the same row or column are correlated in some way. However, a correlation between objects in different rows or columns cannot be ensured. UDTs cannot be used as shuffle keys in clauses, such as JOIN, GROUP BY, DISTRIBUTE BY, SORT BY, ORDER BY, or CLUSTER BY. UDTs can be used at the stages of expressions, but cannot be used as outputs. You can use UDTs to implement the feature provided by the SCALAR function. You can use the built-in functions COLLECT_SET and EXPLODE with UDTs to implement the features provided by aggregate and table-valued functions.

#### 3.8.4 Benefits

This topic describes the benefits of user-defined types (UDTs). UDTs deliver the following benefits: UDTs are easy to use. You do not need to define functions. UDTs support all Java Development Kit (JDK) features. This improves SQL flexibility. UDT code can be stored in the same file as the SQL code. This facilitates code management. You can directly reference the libraries of other programming languages and reuse code that you have written in other languages.

#### 3.8.5 Performance advantages

This topic describes the performance advantages of user-defined types (UDTs). UDTs run in a similar way to UDFs in terms of performance. Therefore, the performance of UDTs is almost the same as that of UDFs. The optimized computing engine improves the performance of UDTs in specific scenarios. If a UDT object is used in different processes, it must be serialized and deserialized. If you use a UDT to perform operations that do not require data reshuffling, such as JOIN or AGGREGATE, the overheads of serialization and deserialization are avoided. The runtime of UDTs is based on Codegen rather than reflection. Therefore, no performance loss occurs. Multiple UDTs can be executed in a single function call. In the following example, it seems that a UDT is called multiple times, but the UDF is actually called only once. Therefore, no additional interface overheads are caused even though the operational units of UDTs are small.

```
values[x].add(values[y]).divide(java.math.BigInteger.valueOf(2))
```

#### 3.8.6 Security advantages

This topic describes the security advantages of user-defined types (UDTs). Similar to UDFs, UDTs are restricted in the Java sandbox model. To perform restricted operations, you must cancel sandbox isolation for the operations or apply to join a sandbox whitelist.

#### 3.8.7 More examples

##### 3.8.7.1 Example of using Java arrays

This topic provides an example of using Java arrays of user-defined types (UDTs). Example:

```
set odps.sql.type.system.odps2=true; set odps.sql.udt.display.tostring=true;
    new Integer[10],    -- Create an array that contains 10 elements.
    new Integer[] {c1, c2, c3},  -- Initialize an ArrayList to create an array that contains three elements.
    new Integer[][] { new Integer[] {c1, c2}, new Integer[] {c3, c4} },  -- Create a multidimensional array.
    new Integer[] {c1, c2, c3} [2], -- Access the elements in the array by using indexes.
    java.util.Arrays.asList(c1, c2, c3);    -- Create a list of the List<Integer> type, which can be used as an
array of the Array<Int> type. This is another way to create a built-in array. FROM VALUES (1,2,3,4) AS t(c1, c2, c3, c4);
```

##### 3.8.7.2 Example of using JSON

This topic provides an example of using JSON for user-defined types (UDTs). The runtime of a UDT carries a JSON dependency (V2.2.4), which can be directly used in JSON. In addition to JSON dependencies, MaxCompute runtime also carries other dependencies, including commons-logging (1.1.1), commons-lang (2.5), commons-io (2.4), and protobuf-java (2.4.1). Example:

```
set odps.sql.type.system.odps2=true; set odps.sql.session.java.imports=java.util.*,java,com.google.gson. *; -- To import multiple packages at a time , separate the packages with commas (,). @a := select new Gson() gson; -- Create a Gson object. gson.toJson(new ArrayList<Integer>(Arrays.asList(1, 2, 3))), -- Convert an object to a JSON string. cast(gson.fromJson('["a","b","c"]', List.class) as List<String>) -- Deserialize the JSON string. Gson forcibly converts the deserialization result from the List<Object> type to the List<String> type. from @a;
```

Returned results:

```
+------------+------------+
| _c0        | _c1        |
+------------+------------+
| [1,2,3]    | 1          |
+------------+------------+
```

Compared with the built-in function GET_JSON_OBJECT, this UDT-based method is simpler. In addition, this method deserializes the content that is extracted from the JSON string to a supported data type. The deserialization improves efficiency.

##### 3.8.7.3 Example of using complex data types

This topic provides an example of using complex data types of user-defined types (UDTs). The built-in data type ARRAY maps the **java.util.List** method, and the built-in data type MAP maps the **java.util.Map** method. Java objects in classes that implement **java.util.List** or **java.util.Map** can be used to process complex-type data in MaxCompute SQL. MaxCompute can directly call java.util.List or java.util.Map to process data of the ARRAY or MAP type. Example:

```
set odps.sql.type.system.odps2=true; set odps.sql.session.java.imports=java.util.*;
    size(new ArrayList<Integer>()),        -- Call the built-in function size() to obtain the size of the
ArrayList.
    array(1,2,3).size(),                   -- Call the built-in function size() of the java.util.List method for
the built-in data type ARRAY.
    sort_array(new ArrayList<Integer>()),  -- Sort the data in the ArrayList.
    al[1],                                 -- java.util.List does not support indexing but can process data of th
e ARRAY type that supports indexing.
    Objects.toString(a),        -- Convert data from the ARRAY type to the STRING type.
    array(1,2,3).subList(1, 2)             -- Obtain a sublist.
from (select new ArrayList<Integer>(array(1,2,3)) as al, array(1,2,3) as a) t;
```

Returned results:

```
+------------+------------+------------+------------+------------+------------+
| _c0        | _c1        | _c2        | _c3        | _c4        | _c5        |
+------------+------------+------------+------------+------------+------------+
| 0          | 3          | []         | 2          | [1, 2, 3]  | [2]        |
+------------+------------+------------+------------+------------+------------+
```

##### 3.8.7.4 Aggregation example

This topic provides an example of using user-defined types (UDTs) to aggregate data. To aggregate data by using a UDT, you must use the built-in function COLLECT_SET or COLLECT_LIST to aggregate data to a list and then call the UDT to calculate the aggregate value. The following example shows how to calculate the median of BigInteger data. You cannot directly call the built-in function MEDIAN because the data is of the java.math.BigInteger type.

```
set odps.sql.session.java.imports=java.math.*; @test_data := select * from values (1),(2),(3),(5) as t(value); @a := select collect_list(new BigInteger(value)) values from @test_data; -- Aggregate the data to a list. @b := select sort_array(values) as values, values.size() cnt from @a; -- Sort the data. @c := select if(cnt % 2 == 1, new BigDecimal(values[cnt div 2]), new BigDecimal(values[cnt div 2 - 1].add(value s[cnt div 2])).divide(new BigDecimal(2))) med from @b; -- Obtain the final output. select med.toString() from @c;
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 2.5        |
+------------+
```

The **COLLECT_LIST** function cannot be used to aggregate partial data because the function can only aggregate all data in a specific group. The COLLECT_LIST function is less efficient than the built-in aggregate functions of MaxCompute or user-defined aggregate functions (UDAFs). We recommend that you use built-in aggregate functions if possible. If all data in a group is aggregated, data skew may occur. The UDT-based method is more efficient than UDAFs or built-in aggregate functions, such as WM_CONCAT, for aggregating all data in a group.

##### 3.8.7.5 Example of using table-valued functions

This topic provides an example of table-valued functions of user-defined types (UDTs). Table-valued functions allow you to specify multiple input rows and columns, and can generate multiple output rows and columns. To implement a table-valued function, perform the following steps: Specify multiple input rows or columns. For more information, see Example of aggregation. Call the java.util.List or java.util.Map method to generate a data collection, and then call the explode function to split the collection into multiple rows. Call different getter methods to obtain data from different fields in a UDT. The obtained data is returned in multiple columns. The following example shows how to expand a JSON string.

```
@a := select '[{"a":"1","b":"2"},{"a":"1","b":"2"}]' str; -- The sample data. @b := select new com.google.gson.Gson().fromJson(str, java.util.List.class) l from @a; -- Deserialize the JSON string. @c := select cast(e as java.util.Map<Object,Object>) m from @b lateral view explode(l) t as e; -- Call the exp lode function to split the string. @d := select m.get('a') as a, m.get('b') as b from @c; -- Return the splitting result in multiple columns. select a.toString() a, b.toString() b from @d; -- The final output. Columns a and b in the variable d are of th e Object type.
```

Returned results:

```
+------------+------------+
| a          | b          |
+------------+------------+
| 1          | 2          |
+------------+------------+
| 1          | 2          |
+------------+------------+
```

### 3.9 UDJ

#### 3.9.1 Background information

This topic describes the background information of user-defined join (UDJ). MaxCompute provides multiple JOIN methods, including INNER JOIN, RIGHT JOIN, OUTER JOIN, LEFT JOIN, FULL JOIN, SEMI JOIN, and ANTI-SEMI JOIN. You can use these built-in JOIN methods in most scenarios. However, these methods are insufficient if you want to perform cross join operations. In most cases, you can use user-defined functions (UDFs) to describe your code framework. However, the current UDF, user-defined table-valued function (UDTF), and user-defined aggregate function (UDAF) frameworks can only handle one table at a time. To perform user-defined operations for multiple tables, you must use built-in JOIN methods, UDFs, UDTFs, and complex SQL statements. In such scenarios, you must use a custom MapReduce framework instead of SQL to complete the required computing tasks. Regardless of the scenario, these operations require technological expertise and may cause the following issues: In scenarios where you use built-in JOIN methods, UDFs, UDTFs, and complex SQL statements: The use of multiple JOIN methods and code in SQL statements results in a logical black box, which makes it difficult to generate an optimal execution plan. In scenarios where you use a custom MapReduce framework: Execution plans are hard to optimize. Most of the MapReduce code is written in Java. During the deep optimization of native runtime code, the execution of the MapReduce code is less efficient than the execution of the MaxCompute code that is generated by the LLVM code generator. MaxCompute introduces UDJ to the UDF framework based on the MaxCompute V2.0 computing engine. You can flexibly join tables by using UDJ to perform more customized operations. This simplifies MapReduce-based underlying operations in the distributed system.

#### 3.9.2 Examples of using UDJ

##### 3.9.2.1 Cross join operation by using UDJ

This topic describes how to use user-defined join (UDJ) to perform cross join operations and provides an example for reference. Assume that two log tables named payment and user_client_log exist. The payment table stores the payment records of users. Each payment record contains the user ID, payment time, and payment content. The following table lists the sample data.

| user id _ | time | pay info _ |
|---|---|---|
| 2656199 | 2018-02-13 22:30:00 | gZhvdySOQb |
| 8881237 | 2018-02-13 08:30:00 | pYvotuLDIT |
| 8881237 | 2018-02-13 10:32:00 | KBuMzRpsko |

The user_client_log table stores the client logs of users. Each log contains the user ID, logging time, and log content. The following table lists the sample data.

| user id _ | time | content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL |

Requirement: For each record in the user_client_log table, find the payment record that has the closest time to this record in the payment table. Then, join the two records and generate results. The following table lists the results.

| user id _ | time | content |
|---|---|---|
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn, pay pYvotuLDIT |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL, pay pYvotuLDIT |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL, pay KBuMzRpsko |

To meet this requirement, use one of the following methods: Use built-in JOIN methods. SQL sample code:

```
  p.user_id,
  p.time,
  merge(p.pay_info, u.content)
FROM
  payment p RIGHT OUTER JOIN user_client_log u
ON p.user_id = u.user_id and abs(p.time - u.time) = min(abs(p.time - u.time))
```

If you join two rows in the tables, you must calculate the minimum difference between the p.time and u.time under the same user_id. However, you cannot call aggregate functions in the join condition. Therefore, you cannot use standard JOIN methods to complete this task. Use the UDJ method. i. Create a UDJ function. a. Configure the SDK of the new version.

```xml
<dependency>
  <groupId>com.aliyun.odps</groupId>
  <artifactId>odps-sdk-udf</artifactId>
  <version>0.30.0</version>
  <scope>provided</scope>
</dependency>
```

b. Write UDJ code and package the code as odps-udj-example.jar.

```java
package com.aliyun.odps.udf.example.udj; import com.aliyun.odps.Column; import com.aliyun.odps.OdpsType; import com.aliyun.odps.Yieldable; import com.aliyun.odps.data.ArrayRecord; import com.aliyun.odps.data.Record; import com.aliyun.odps.udf.DataAttributes; import com.aliyun.odps.udf.ExecutionContext; import com.aliyun.odps.udf.UDJ; import com.aliyun.odps.udf.annotation.Resolve; import java.util.ArrayList; import java.util.Iterator; /** For each record in the table on the right, find the record in the table on the left that has the clos est time to this record.
 * Join the two records.
```

`*/`

```java
@Resolve("->string,bigint,string") public class PayUserLogMergeJoin extends UDJ {
  private Record outputRecord;
  /** Call the preceding code before data is processed. You can use the PayUserLogMergeJoin method for in
itialization.
```

`*/`

```java
@Override
```

```java
  @Override
  public void setup(ExecutionContext executionContext, DataAttributes dataAttributes) {
```

`//`

```
    outputRecord = new ArrayRecord(new Column[]{
      new Column("user_id", OdpsType.STRING),
      new Column("time", OdpsType.BIGINT),
      new Column("content", OdpsType.STRING)
    });
```

`}`

```
  /** Rewrite the PayUserLogMergeJoin method to implement the connection logic.
   * @param key: the current key for joining.
   * @param left: the record group of the current key in the table on the left.
   * @param right: the record group of the current key in the table on the right.
   * @param output: generates the result of UDJ.
```

`*/`

```java
  @Override
  public void join(Record key, Iterator<Record> left, Iterator<Record> right, Yieldable<Record> output) {
    outputRecord.setString(0, key.getString(0));
    if (! right.hasNext()) {
      // The group on the right is empty. Do not perform operations on this group.
      return;
    } else if (! left.hasNext()) {
      // The group on the left is empty. Generate all records from the group on the right but do not join
the records of the two tables.
      while (right.hasNext()) {
        Record logRecord = right.next();
        outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
        outputRecord.setString(2, logRecord.getString(1));
        output.yield(outputRecord);
```

`}`

```
      return;
```

`}`

```
    ArrayList<Record> pays = new ArrayList<>();
    // The records in the group on the left are iterated from the beginning to the end.
    // The iterator cannot reset the records in the group on the right.
    // Save each record of the group on the left to ArrayList.
    left.forEachRemaining(pay -> pays.add(pay.clone()));
    while (right.hasNext()) {
      Record log = right.next();
      long logTime = log.getDatetime(0).getTime();
      long minDelta = Long.MAX_VALUE;
      Record nearestPay = null;
      // Iterate all the records of the group on the left. Then, you can find the minimum time difference
between the records.
      for (Record pay: pays) {
        long delta = Math.abs(logTime - pay.getDatetime(0).getTime());
        if (delta < minDelta) {
          minDelta = delta;
          nearestPay = pay;
```

`}` `}`

```
      // Merge the log records and payment records that are closest in time and then generate results.
      outputRecord.setBigint(1, log.getDatetime(0).getTime());
      outputRecord.setString(2, mergeLog(nearestPay.getString(1), log.getString(1)));
      output.yield(outputRecord);
```

`}` `}`

```
  String mergeLog(String payInfo, String logContent) {
    return logContent + ", pay " + payInfo;
```

`}`

```java
  @Override
  public void close() {
```

`}` `}` c. Add the odps-udj-example.jar package to MaxCompute.

```
add jar odps-udj-example.jar;
```

d. Register the UDJ function pay_user_log_merge_join in MaxCompute.

```
create function pay_user_log_merge_join
  as 'com.aliyun.odps.udf.example.udj.PayUserLogMergeJoin'
  using 'odps-udj-example.jar';
```

ii. Prepare sample data. a. Create the payment table and the user_client_log table.

```
create table payment(user_id string,time datetime,pay_info string); create table user_client_log(user_id string,time datetime,content string);
```

b. Insert data into the sample tables.

```
-- Insert data into the payment table. INSERT OVERWRITE TABLE payment VALUES ('1335656', datetime '2018-02-13 19:54:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 12:21:00', 'pYvotuLDIT'), ('2656199', datetime '2018-02-13 20:50:00', 'PEqMSHyktn'), ('2656199', datetime '2018-02-13 22:30:00', 'gZhvdySOQb'), ('8881237', datetime '2018-02-13 08:30:00', 'pYvotuLDIT'), ('8881237', datetime '2018-02-13 10:32:00', 'KBuMzRpsko'), ('9890100', datetime '2018-02-13 16:01:00', 'gZhvdySOQb'), ('9890100', datetime '2018-02-13 16:26:00', 'MxONdLckwa')
```

;

```
-- Insert data into the user_client_log table. INSERT OVERWRITE TABLE user_client_log VALUES ('1000235', datetime '2018-02-13 00:25:36', 'click FNOXAibRjkIaQPB'), ('1000235', datetime '2018-02-13 22:30:00', 'click GczrYaxvkiPultZ'), ('1335656', datetime '2018-02-13 18:30:00', 'click MxONdLckpAFUHRS'), ('1335656', datetime '2018-02-13 19:54:00', 'click mKRPGOciFDyzTgM'), ('2656199', datetime '2018-02-13 08:30:00', 'click CZwafHsbJOPNitL'), ('2656199', datetime '2018-02-13 09:14:00', 'click nYHJqIpjevkKToy'), ('2656199', datetime '2018-02-13 21:05:00', 'click gbAfPCwrGXvEjpI'), ('2656199', datetime '2018-02-13 21:08:00', 'click dhpZyWMuGjBOTJP'), ('2656199', datetime '2018-02-13 22:29:00', 'click bAsxnUdDhvfqaBr'), ('2656199', datetime '2018-02-13 22:30:00', 'click XIhZdLaOocQRmrY'), ('4356142', datetime '2018-02-13 18:30:00', 'click DYqShmGbIoWKier'), ('4356142', datetime '2018-02-13 19:54:00', 'click DYqShmGbIoWKier'), ('8881237', datetime '2018-02-13 00:30:00', 'click MpkvilgWSmhUuPn'), ('8881237', datetime '2018-02-13 06:14:00', 'click OkTYNUHMqZzlDyL'), ('8881237', datetime '2018-02-13 10:30:00', 'click OkTYNUHMqZzlDyL'), ('9890100', datetime '2018-02-13 16:01:00', 'click vOTQfBFjcgXisYU'), ('9890100', datetime '2018-02-13 16:20:00', 'click WxaLgOCcVEvhiFJ')
```

; iii. Use a UDJ function in SQL.

```
SELECT r.user_id, from_unixtime(time/1000) as time, content FROM ( SELECT user_id, time as time, pay_info FROM payment ) p JOIN ( SELECT user_id, time as time, content FROM user_client_log ) u ON p.user_id = u.user_id USING pay_user_log_merge_join(p.time, p.pay_info, u.time, u.content)
```

`r`

```
AS (user_id, time, content);
```

Parameters in the USING clause:
**pay_user_log_merge_join**: the name of the UDJ function in SQL.
**(p.time, p.pay_info, u.time, u.content)**: the columns in both of the tables used in the UDJ function.
**r**: the alias of the result returned by the UDJ function. You can reference this alias in other SQL statements.
**(user_id, time, content)** are the columns returned by the UDJ function.
Returned results:

```
+---------+------------+---------+
| user_id | time       | content |
+---------+------------+---------+
| 1000235 | 2018-02-13 00:25:36 | click FNOXAibRjkIaQPB |
| 1000235 | 2018-02-13 22:30:00 | click GczrYaxvkiPultZ |
| 1335656 | 2018-02-13 18:30:00 | click MxONdLckpAFUHRS, pay PEqMSHyktn |
| 1335656 | 2018-02-13 19:54:00 | click mKRPGOciFDyzTgM, pay PEqMSHyktn |
| 2656199 | 2018-02-13 08:30:00 | click CZwafHsbJOPNitL, pay pYvotuLDIT |
| 2656199 | 2018-02-13 09:14:00 | click nYHJqIpjevkKToy, pay pYvotuLDIT |
| 2656199 | 2018-02-13 21:05:00 | click gbAfPCwrGXvEjpI, pay PEqMSHyktn |
| 2656199 | 2018-02-13 21:08:00 | click dhpZyWMuGjBOTJP, pay PEqMSHyktn |
| 2656199 | 2018-02-13 22:29:00 | click bAsxnUdDhvfqaBr, pay gZhvdySOQb |
| 2656199 | 2018-02-13 22:30:00 | click XIhZdLaOocQRmrY, pay gZhvdySOQb |
| 4356142 | 2018-02-13 18:30:00 | click DYqShmGbIoWKier |
| 4356142 | 2018-02-13 19:54:00 | click DYqShmGbIoWKier |
| 8881237 | 2018-02-13 00:30:00 | click MpkvilgWSmhUuPn, pay pYvotuLDIT |
| 8881237 | 2018-02-13 06:14:00 | click OkTYNUHMqZzlDyL, pay pYvotuLDIT |
| 8881237 | 2018-02-13 10:30:00 | click OkTYNUHMqZzlDyL, pay KBuMzRpsko |
| 9890100 | 2018-02-13 16:01:00 | click vOTQfBFjcgXisYU, pay gZhvdySOQb |
| 9890100 | 2018-02-13 16:20:00 | click WxaLgOCcVEvhiFJ, pay MxONdLckwa |
+---------+------------+---------+
```

##### 3.9.2.2 Pre-sorting

This topic describes the pre-sorting feature of user-defined join (UDJ) and provides an example for reference. An iterator is used to iterate all records in the payment table and find the payment record that has the closest time to a specific log record in the user_client_log table. To perform this task, you must load all payment records with the same user_id to an ArrayList. This method can be applied when the number of payment records is small. Due to the limits of the memory size, you must find another method to load the data if a large number of payment records have been generated. This topic describes how to address this issue by using the SORT BY clause. If the number of payment records is too large to be stored in the memory and all the data in the table has been sorted by time, you need only to compare the first element in the two lists. This method uses the SORT BY clause to pre-sort the UDJ data. To achieve the same effect by using the previous method, you need only to cache a maximum of three data records during pre-sorting. The following code shows an example:

```java
@Override public void join(Record key, Iterator<Record> left, Iterator<Record> right, Yieldable<Record> output) {
  outputRecord.setString(0, key.getString(0));
  if (! right.hasNext()) {
    return;
  } else if (! left.hasNext()) {
    while (right.hasNext()) {
      Record logRecord = right.next();
      outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
      outputRecord.setString(2, logRecord.getString(1));
      output.yield(outputRecord);
```

`}`

```
    return;
```

`}`

```
  long prevDelta = Long.MAX_VALUE;
  Record logRecord = right.next();
  Record payRecord = left.next();
  Record lastPayRecord = payRecord.clone();
  while (true) {
    long delta = logRecord.getDatetime(0).getTime() - payRecord.getDatetime(0).getTime();
    if (left.hasNext() && delta > 0) {
      // The time delta between the two records decreases and the operation can continue.
      // Explore the group on the left to try to obtain a smaller time delta.
      lastPayRecord = payRecord.clone();
      prevDelta = delta;
      payRecord = left.next();
    } else {
     // The minimum time delta point is reached. Check the final record in the payment table.
     // Generate the merged result and prepare to process the next record.
     // The group on the right.
      Record nearestPay = Math.abs(delta) < prevDelta ? payRecord : lastPayRecord;
      outputRecord.setBigint(1, logRecord.getDatetime(0).getTime());
      String mergedString = mergeLog(nearestPay.getString(1), logRecord.getString(1));
      outputRecord.setString(2, mergedString);
      output.yield(outputRecord);
      if (right.hasNext()) {
        logRecord = right.next();
        prevDelta = Math.abs(
          logRecord.getDatetime(0).getTime() - lastPayRecord.getDatetime(0).getTime()
```

);

```
      } else {
        break;
```

`}` `}` `}` `}`

#### 3.9.3 Performance

This topic describes the performance of user-defined join (UDJ). A real online MapReduce job is used as an example to verify the performance of UDJ. The job runs based on a complex algorithm. In this example, two tables are joined, UDJ is used to rewrite the MapReduce job, and the correctness of the UDJ results is checked. The following figure shows the MapReduce and UDJ performance under the same data concurrency. As shown in the figure, UDJ conveniently describes the complex logic of how to handle multiple tables and greatly improves performance. The code is called only within UDJ. The entire Mapper logic in this example is executed by the native runtime engine of MaxCompute. The data exchange logic between the MaxCompute UDJ runtime engine and Java interfaces is optimized in Java code. The JOIN logic of UDJ is more efficient than that of a reducer.

### 3.10 Parameterized view

This topic describes the parameterized view feature that is supported by the MaxCompute SQL engine. In the traditional views of MaxCompute, complex SQL scripts are encapsulated at the underlying layer. Callers can call views the same way as reading a common table without the need to understand the underlying implementation. Traditional views are widely used because they implement encapsulation and reuse. However, traditional views cannot accept parameters from callers. This reduces code reuse efficiency. For example, a caller cannot filter data in the underlying table that is read by a view nor pass other parameters. The MaxCompute SQL engine supports parameterized views and allows you to import tables or variables to customize views.

**Define a parameterized view**

You can use the following syntax to create a parameterized view:

```
-- view with parameters -- param @a -a table parameter -- param @b -a string parameter -- returns a table with schema (key STRING,value STRING) CREATE VIEW IF NOT EXISTS pv1(@a table (k STRING,v BIGINT), @b STRING)
```

`AS`

```
SELECT srcp.key,srcp.value FROM srcp JOIN @a ON srcp.key=a.k AND srcp.p=@b;
```

Syntax description: To create a parameterized view, you must specify parameters. Therefore, you must use Script Mode SQL to create a parameterized view. The created view pv1 has two parameters: TABLE and STRING. The parameter value can be a table or of a basic data type. The parameter value can also be a subquery, for example, `SELECT * FROM view_name( (SELECT 1 FROM src WHERE a >`

```
0), 1); .
```

When you create a view, you can set ANY for a parameter, which indicates any data type. For example, `CREATE VIEW`

```
paramed_view (@a ANY) AS SELECT * FROM src WHERE CASE WHEN @a IS NULL THEN key1 ELSE key2 END = key3; defines
```

that the first parameter of the view can be a value of any data type. However, the ANY type cannot be used in a specific operation, such as **+** or **AND**, which requires specific data types. A field of the ANY type is often used as a PassThrough column in the TABLE parameter. Example:

```
CREATE VIEW paramed_view (@a TABLE(name STRING, id ANY, age BIGINT)) AS SELECT * FROM @a WHERE name = 'foo' A ND age < 25; -- The call example. SELECT * FROM param_view((SELECT name, id, age FROM students));
```

After you execute the `CREATE VIEW` statement to create a view, you can run the `DESC` command to obtain the description of the view. This description contains the return type of the view. The return type of a view is recalculated when the view is called. It may be different from the return type, such as ANY, that you specify when you create the view. When you create a view, you can use an asterisk (*) in the TABLE parameter to retrieve any columns. The asterisk (*) can represent a specific data type or the ANY type. Example:

```
CREATE VIEW paramed_view (@a TABLE(key STRING, * ANY), @b TABLE(key STRING, * STRING)) AS SELECT a. * FROM @a JOIN @b ON a.key = b.key; -- The call example. SELECT name, address FROM param_view((SELECT school, name, age, address FROM student), school) WHERE age < 20
```

; In this example, the view accepts two TABLE parameters. In the table that is specified by the first TABLE parameter, data in the first column is of the STRING type, and data in other columns can be of the ANY type. In the table that is specified by the second TABLE parameter, data in the first and other columns is all of the STRING type. Take note of the following points: The varied-length part must be placed at the end of the table that is specified by the TABLE parameter. This means that the * column cannot be followed by other columns. Therefore, the table that is specified by the TABLE parameter can contain only one varied-length column. The varied-length part must be placed at the end of the table that is specified by the TABLE parameter. However, the columns of an input table may not be arranged in this sequence. In this case, the columns need to be rearranged. A subquery can be used as a parameter value and must be enclosed in a pair of parentheses (). No name is specified for the varied-length part of the table that is specified by the TABLE parameter. As a result, data in the varied-length part cannot be referenced or used for operation when you define the view. Although you cannot use the varied-length part for operation, you can use the SELECT * statement to transfer data in the varied-length part out of the table. The column of the table that is specified by the TABLE parameter may be different from the fixed-length column that you specify when you define the view. If the names are different, the compiler automatically renames the column of the table that is specified by the TABLE parameter. If the data types are different, the compiler performs an implicit conversion. If the implicit conversion fails, an error occurs.

**Call a parameterized view**

You can execute the following statement to call the pv1 view that you defined:

```
@a := SELECT * FROM src WHERE value >0; --call view with table variable and scalar @b := SELECT * FROM pv1(@a,'20170101'); @another_day := '20170102'; --call view with table name and scalar variable @c := SELECT * FROM pv1(src2, @another_day); @d := SELECT * FROM @c UNION ALL SELECT * FROM @b; WITH t AS(SELECT * FROM src3) SELECT * FROM @c SELECT * FROM @d SELECT* FROM pv1(t,@another_day);
```

You can use different parameters to call the pv1 view. The value of the TABLE parameter can be the name of a physical table, view, or table variable. You can also set the TABLE parameter to a table alias by using common table expressions (CTEs). The values of common parameters can be variables or constants. The script of a parameterized view can contain only data manipulation language (DML) statements. The statements, such as INSERT, CREATE TABLE, or PRINT, cannot be contained. A parameterized view can contain multiple SQL statements.

```
-- view with parameters -- param @a -a table parameter -- param @b -a string parameter -- returns a table with schema (key string,value string) CREATE VIEW IF NOT EXISTS pv2(@a TABLE (k STRING,v BIGINT), @b STRING) AS BEGIN @srcp := SELECT * FROM srcp WHERE p=@b; @pv2 := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k; END;
```

Statements between BEGIN and END are the script of this view. The `@pv2 :=...` statement is similar to the RETURN statement in other programming languages. You can use the @pv2 :=... statement to assign a value to a variable of an implicit table that has the same name as the view. The matching rules for actual and formal view parameters are the same as those specified in a common weaklytyped language. Specifically, if a view parameter can be implicitly converted, it can match the defined parameter. For example, a value of the BIGINT type can match parameters of the DOUBLE type. For table variables, if the schema of table a can be inserted into table b, table a can be used to match the table-type parameters that have the same schema as table b. You can explicitly declare the return type to make the code easier to read.

```
CREATE VIEW IF NOT EXISTS pv3(@a table (k STRING,v BIGINT), @b STRING) RETURNS @ret TABLE (x STRING,y STRING)
```

`AS`

```
BEGIN
    @srcp := SELECT * FROM srcp WHERE p=@b;
    @ret := SELECT srcp.key,srcp.value FROM @srcp JOIN @a ON srcp.key=a.k;
end;
```

**RETURNS @ret TABLE (x STRING,y STRING)** defines the following information:
The return type, which indicates the type returned to the caller. The return type is specified by the **TABLE**
**(x STRING,y STRING)** parameter. You can use this parameter to customize the table schema.
The response parameter. The **@ret** parameter defines the name of the response parameter. Assigning a value to the response parameter is performed in the view script. You can consider the view that contains no **BEGIN/END** or return variables as a simplified parameterized view.

### 3.11 CLONE TABLE

This topic describes how to use the CLONE TABLE statement. The CLONE TABLE statement is used to clone data from one table to another. This statement improves data migration efficiency. The schema of the destination table must be compatible with that of the source table. The CLONE TABLE statement can be executed for partitioned tables and non-partitioned tables. This statement cannot be executed for hash clustering tables. If a destination table is created before the CLONE TABLE statement is executed, data in a maximum of 10,000 partitions can be cloned at a time. If a destination table is not created before the CLONE TABLE statement is executed, the number of partitions from which you can clone data at a time is unlimited. This ensures atomicity. You can execute the CLONE TABLE statement for up to seven times in the same non-partitioned table or in the same partition of a partitioned table. You cannot execute the CLONE TABLE statement for projects across regions.

**Syntax**

```
CLONE TABLE <[src_project_name.]src_table_name> [PARTITION(spec), ...]
 TO <[dest_project_name.]desc_table_name> [IF EXISTS (OVERWRITE | IGNORE)] ;
```

**Description**

The CLONE TABLE statement is used to clone data from the src_table_name table to the desc_table_name table. After you clone data to the desc_table_name table, we recommend that you verify the data accuracy. For example, you can execute the SELECT COUNT statement to view the number of rows in the destination table or execute the DESC statement to view the table size.

**Parameters**

**src_table_name**: the name of the source table.
**src_project_name**: the name of the project to which the source table belongs. If this parameter is not specified, the
name of the current project is used by default.
**desc_table_name**: the name of the destination table.
If a destination table is not created, the table is created by using the CREATE TABLE LIKE statement when you execute the CLONE TABLE statement. If a destination table is created and IF EXISTS OVERWRITE is specified, data in the partitions of the destination table is overwritten when you execute the CLONE TABLE statement. If a destination table is created and IF EXISTS IGNORE is specified, the existing partitions in the table are skipped and the data in these partitions is not overwritten when you execute the CLONE TABLE statement.
**dest_project_name**: the name of the project to which the destination table belongs. If this parameter is not
specified, the current project name is used by default. Assume that the partitioned table srcpart_copy and non-partitioned table src_copy are source tables. The two tables have the following metadata:

```
odps@ multi>READ srcpart_copy; +------------+------------+------------+------------+
| key        | value      | ds         | hr         |
+------------+------------+------------+------------+
| 1          | ok49       | 2008-04-09 | 11         |
| 1          | ok48       | 2008-04-08 | 12         |
+------------+------------+------------+------------+ odps@ multi>READ src_copy; +------------+------------+
| key        | value      |
+------------+------------+
| 1          | ok         |
+------------+------------+
```

Clone all data from the non-partitioned table src_copy to the destination table src_clone.

```
CLONE TABLE src_copy TO src_clone;
```

Returned results:

```
ID = 2019102303024544g2540cdv2
```

`OK` //After the data is cloned, query data in the destination table src_clone and check the data accuracy.

```
SELECT * FROM src_clone;
```

Clone data from a specified partition of the partitioned table srcpart_copy to the destination table srcpart_clone.

```
CLONE TABLE srcpart_copy PARTITION(ds="2008-04-09", hr='11') TO srcpart_clone IF EXISTS OVERWRITE;
```

Returned results:

```
ID = 20191023030534986g4540cdv2
```

`OK` //After the data is cloned, query data in the destination table srcpart_clone and check the data accuracy.

```
SELECT * FROM srcpart_clone;
```

Clone all data from the partitioned table srcpart_copy to the destination table srcpart_clone and skip the data in the existing partitions of the destination table.

```
CLONE TABLE srcpart_copy TO srcpart_clone IF EXISTS IGNORE;
```

Returned results:

```
ID = 20191023030619196g5540cdv2
```

`OK` //After the data is cloned, query data in the destination table srcpart_clone and check the data accuracy.

```
SELECT * FROM srcpart_clone;
```

Clone all data from the partitioned table srcpart_copy to the destination table srcpart_clone2.

```
CLONE TABLE srcpart_copy TO srcpart_clone2;
```

Returned results:

```
ID = 20191023030825186g6540cdv2
```

`OK` //After the data is cloned, query data in the destination table srcpart_clone2 and check the data accuracy.

```
SELECT * FROM srcpart_clone2;
```

### 3.12 Geographic functions

#### 3.12.1 Usage notes

Geographic functions use a set of Java user-defined functions (UDFs) to allow you to perform geometric computing in MaxCompute. Before you use geographic functions, understand the following information:

**What are geographic functions?**

The application of geographic functions requires extensive knowledge in the field. Esri developed a set of open-source Hive UDFs that support simple geometric computing (see spatial-framework-for-hadoop). MaxCompute supports Hive UDFs and conducted secondary development on the functions to develop more features, such as spherical functions, grid functions, and indexing. The names of most functions remain the same as those of PostGIS, which simplifies the learning process. Supported features: Geometry models that comply with OpenGIS standards. You can use the Well-Known Text (WKT) and Well-Known Binary (WKB) formats to input and output spatial geometry objects, such as ST_Point, ST_MultiPoint, ST_LineString, ST_MultiLineString, ST_Polygon, and ST_MultiPolygon. A set of functions based on the preceding geometry models to construct objects, test geometric relationships, obtain geometry object attributes, and calculate plane and sphere measurements, such as areas and distances. A set of indexing functions, such as GeoHash, S2, and RTree, to optimize spatial joins. All algorithms used by the geographic function are based on open source technologies. For example, spatial-sdkodps.jar contains encapsulated open-source resources that are free of charge. MaxCompute cannot control or provide support for external capabilities because they are encapsulated by using open-source algorithms. Therefore, MaxCompute does not provide explanation, maintenance, or technical support for the business, performance, and accuracy of UDFs. In case of issues, you can compare and test functions, fix errors, or replace functions based on open source implementations. Therefore, the geographic functions are suitable only for users who have a deep understanding of open-source geographic functions.

**Register geographic functions with MaxCompute**

Perform the following steps to register the geographic functions with MaxCompute and use them in your project:
1. Download three compiled JAR packages.
Click Spatial JAR to download the Spatial JAR package and rename the package name to `spatial-sdk-hive.jar` . Click esri-geometry-api to download the Esri Geometry JAR package and rename the package to `esri-geometry-`

```
api.jar .
```

Obtain the spatial-sdk-odps.jar package.
2. Use the MaxCompute client (odpscmd) to access the project. Run the following script to upload the JAR package and
register the functions. Then, you can use the functions in the project or authorize other users to use the functions in other projects.

```
ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar; CREATE FUNCTION ST_Aggr_ConvexHull AS 'com.esri.hadoop.hive.ST_Aggr_ConvexHull' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Aggr_Intersection AS 'com.esri.hadoop.hive.ST_Aggr_Intersection' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATEFUNCTIONSTAggrUnion
```

`AS`

```
'comesrihadoophieSTAggrUnion' USING'spatialsdkhiejaresri
```

```
CREATE FUNCTION ST_Aggr_Union AS 'com.esri.hadoop.hive.ST_Aggr_Union' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Area AS 'com.esri.hadoop.hive.ST_Area' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_AsBinary AS 'com.esri.hadoop.hive.ST_AsBinary' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_AsGeoJson AS 'com.esri.hadoop.hive.ST_AsGeoJson' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_AsJson AS 'com.esri.hadoop.hive.ST_AsJson' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_AsShape AS 'com.esri.hadoop.hive.ST_AsShape' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_AsText AS 'com.esri.hadoop.hive.ST_AsText' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Bin AS 'com.esri.hadoop.hive.ST_Bin' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_BinEnvelope AS 'com.esri.hadoop.hive.ST_BinEnvelope' USING 'spatial-sdk-hive.jar,esri-ge ometry-api.jar'; CREATE FUNCTION ST_Boundary AS 'com.esri.hadoop.hive.ST_Boundary' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Buffer AS 'com.esri.hadoop.hive.ST_Buffer' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Centroid AS 'com.esri.hadoop.hive.ST_Centroid' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Contains AS 'com.esri.hadoop.hive.ST_Contains' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_ConvexHull AS 'com.esri.hadoop.hive.ST_ConvexHull' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_CoordDim AS 'com.esri.hadoop.hive.ST_CoordDim' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Crosses AS 'com.esri.hadoop.hive.ST_Crosses' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Difference AS 'com.esri.hadoop.hive.ST_Difference' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Dimension AS 'com.esri.hadoop.hive.ST_Dimension' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Disjoint AS 'com.esri.hadoop.hive.ST_Disjoint' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Distance AS 'com.esri.hadoop.hive.ST_Distance' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_EndPoint AS 'com.esri.hadoop.hive.ST_EndPoint' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Envelope AS 'com.esri.hadoop.hive.ST_Envelope' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_EnvIntersects AS 'com.esri.hadoop.hive.ST_EnvIntersects' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Equals AS 'com.esri.hadoop.hive.ST_Equals' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_ExteriorRing AS 'com.esri.hadoop.hive.ST_ExteriorRing' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeodesicLengthWGS84 AS 'com.esri.hadoop.hive.ST_GeodesicLengthWGS84' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomCollection AS 'com.esri.hadoop.hive.ST_GeomCollection' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Geometry AS 'com.esri.hadoop.hive.ST_Geometry' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_GeometryN AS 'com.esri.hadoop.hive.ST_GeometryN' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_GeometryType AS 'com.esri.hadoop.hive.ST_GeometryType' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromGeoJson AS 'com.esri.hadoop.hive.ST_GeomFromGeoJson' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromJson AS 'com.esri.hadoop.hive.ST_GeomFromJson' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromShape AS 'com.esri.hadoop.hive.ST_GeomFromShape' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromText AS 'com.esri.hadoop.hive.ST_GeomFromText' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeomFromWKB AS 'com.esri.hadoop.hive.ST_GeomFromWKB' USING 'spatial-sdk-hive.jar,esri-ge ometry-api.jar';
```

`y` `p` `j`

```
CREATE FUNCTION ST_InteriorRingN AS 'com.esri.hadoop.hive.ST_InteriorRingN' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersection AS 'com.esri.hadoop.hive.ST_Intersection' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Intersects AS 'com.esri.hadoop.hive.ST_Intersects' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Is3D AS 'com.esri.hadoop.hive.ST_Is3D' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_IsClosed AS 'com.esri.hadoop.hive.ST_IsClosed' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_IsEmpty AS 'com.esri.hadoop.hive.ST_IsEmpty' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_IsMeasured AS 'com.esri.hadoop.hive.ST_IsMeasured' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_IsRing AS 'com.esri.hadoop.hive.ST_IsRing' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_IsSimple AS 'com.esri.hadoop.hive.ST_IsSimple' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Length AS 'com.esri.hadoop.hive.ST_Length' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_LineFromWKB AS 'com.esri.hadoop.hive.ST_LineFromWKB' USING 'spatial-sdk-hive.jar,esri-ge ometry-api.jar'; CREATE FUNCTION ST_LineString AS 'com.esri.hadoop.hive.ST_LineString' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_M AS 'com.esri.hadoop.hive.ST_M' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MaxM AS 'com.esri.hadoop.hive.ST_MaxM' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MaxX AS 'com.esri.hadoop.hive.ST_MaxX' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MaxY AS 'com.esri.hadoop.hive.ST_MaxY' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MaxZ AS 'com.esri.hadoop.hive.ST_MaxZ' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MinM AS 'com.esri.hadoop.hive.ST_MinM' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MinX AS 'com.esri.hadoop.hive.ST_MinX' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MinY AS 'com.esri.hadoop.hive.ST_MinY' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MinZ AS 'com.esri.hadoop.hive.ST_MinZ' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_MLineFromWKB AS 'com.esri.hadoop.hive.ST_MLineFromWKB' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPointFromWKB AS 'com.esri.hadoop.hive.ST_MPointFromWKB' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MPolyFromWKB AS 'com.esri.hadoop.hive.ST_MPolyFromWKB' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiLineString AS 'com.esri.hadoop.hive.ST_MultiLineString' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_MultiPoint AS 'com.esri.hadoop.hive.ST_MultiPoint' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_MultiPolygon AS 'com.esri.hadoop.hive.ST_MultiPolygon' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumGeometries AS 'com.esri.hadoop.hive.ST_NumGeometries' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumInteriorRing AS 'com.esri.hadoop.hive.ST_NumInteriorRing' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_NumPoints AS 'com.esri.hadoop.hive.ST_NumPoints' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Overlaps AS 'com.esri.hadoop.hive.ST_Overlaps' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_Point AS 'com.esri.hadoop.hive.ST_Point' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_PointFromWKB AS 'com.esri.hadoop.hive.ST_PointFromWKB' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_PointN AS 'com.esri.hadoop.hive.ST_PointN' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_PointZ AS 'com.esri.hadoop.hive.ST_PointZ' USING 'spatial-sdk-hive.jar,esri-geometry-a
```

```
pi.jar'; CREATE FUNCTION ST_PolyFromWKB AS 'com.esri.hadoop.hive.ST_PolyFromWKB' USING 'spatial-sdk-hive.jar,esri-ge ometry-api.jar'; CREATE FUNCTION ST_Polygon AS 'com.esri.hadoop.hive.ST_Polygon' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Relate AS 'com.esri.hadoop.hive.ST_Relate' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_SetSRID AS 'com.esri.hadoop.hive.ST_SetSRID' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_SRID AS 'com.esri.hadoop.hive.ST_SRID' USING 'spatial-sdk-hive.jar,esri-geometryapi.jar'; CREATE FUNCTION ST_StartPoint AS 'com.esri.hadoop.hive.ST_StartPoint' USING 'spatial-sdk-hive.jar,esrigeometry-api.jar'; CREATE FUNCTION ST_SymmetricDiff AS 'com.esri.hadoop.hive.ST_SymmetricDiff' USING 'spatial-sdkhive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Touches AS 'com.esri.hadoop.hive.ST_Touches' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Union AS 'com.esri.hadoop.hive.ST_Union' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_Within AS 'com.esri.hadoop.hive.ST_Within' USING 'spatial-sdk-hive.jar,esri-geometry-a pi.jar'; CREATE FUNCTION ST_X AS 'com.esri.hadoop.hive.ST_X' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Y AS 'com.esri.hadoop.hive.ST_Y' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_Z AS 'com.esri.hadoop.hive.ST_Z' USING 'spatial-sdk-hive.jar,esri-geometry-api.jar'; CREATE FUNCTION ST_GeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHash' USING 'spatial-sdkodps.jar'; CREATE FUNCTION ST_PointFromGeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_PointFromGeoHash' USING 'sp atial-sdk-odps.jar'; CREATE FUNCTION ST_GeoHashNeighbours AS 'com.aliyun.odps.geospatial.udf.geohash.ST_GeoHashNeighbours' USING ' spatial-sdk-odps.jar'; CREATE FUNCTION ST_EnvelopeFromGeoHash AS 'com.aliyun.odps.geospatial.udf.geohash.ST_EnvelopeFromGeoHash' USI NG 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_AreaWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_AreaWGS84' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_BufferWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_BufferWGS84' USING 'spatial-sdkodps.jar'; CREATE FUNCTION ST_DistanceWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_DistanceWGS84' USING 'spatialsdk-odps.jar'; CREATE FUNCTION ST_GeodesicDistance AS 'com.aliyun.odps.geospatial.udf.compute.ST_GeodesicDistance' USING 'sp atial-sdk-odps.jar'; CREATE FUNCTION ST_Transform AS 'com.aliyun.odps.geospatial.udf.compute.ST_Transform' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_TransformWGS84 AS 'com.aliyun.odps.geospatial.udf.compute.ST_TransformWGS84' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_IsValid AS 'com.aliyun.odps.geospatial.udf.compute.ST_IsValid' USING 'spatial-sdkodps.jar'; CREATE FUNCTION ST_S2CellCenterPoint AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellCenterPoint' USING 'spa tial-sdk-odps.jar'; CREATE FUNCTION ST_S2CellIdsFromGeom AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromGeom' USING 'spa tial-sdk-odps.jar'; CREATE FUNCTION ST_S2CellIdsFromText AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellIdsFromText' USING 'spa tial-sdk-odps.jar'; CREATE FUNCTION ST_S2CellNeighbours AS 'com.aliyun.odps.geospatial.udf.grid.ST_S2CellNeighbours' USING 'spa tial-sdk-odps.jar'; CREATE FUNCTION ST_Area_Sphere AS 'com.aliyun.odps.geospatial.udf.compute.ST_Area_Sphere' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_Distance_Sphere AS 'com.aliyun.odps.geospatial.udf.compute.ST_Distance_Sphere' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_BuildRTreeIndex AS 'com.aliyun.odps.geospatial.udf.index.ST_BuildRTreeIndex' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_ContainsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_ContainsFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_CrossesFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_CrossesFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_EqualsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_EqualsFromRTree' USING 'spatial-sdk-odps.jar'; CREATEFUNCTIONSTIntersectsFromRTreeAS'comaliyunodpsgeospatialudfindexSTIntersectsFromRTree'USING
```

```
CREATE FUNCTION ST_IntersectsFromRTree AS com.aliyun.odps.geospatial.udf.index.ST_IntersectsFromRTree USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_OverlapsFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_OverlapsFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_TouchesFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_TouchesFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_WithinFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_WithinFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_KNNFromRTree AS 'com.aliyun.odps.geospatial.udf.index.ST_KNNFromRTree' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_Simplify AS 'com.aliyun.odps.geospatial.udf.compute.ST_Simplify' USING 'spatial-sdk-odps .jar'; CREATE FUNCTION ST_SimplifyVW AS 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyVW' USING 'spatial-sdk-od ps.jar'; CREATE FUNCTION ST_SimplifyPreserveTopology AS 'com.aliyun.odps.geospatial.udf.compute.ST_SimplifyPreserveTopology' USING 'spatial-sdk-odps.jar'; CREATE FUNCTION ST_LineLocatePoint AS 'com.aliyun.odps.geospatial.udf.compute.ST_LineLocatePoint' USING 'spatial-sdk-odps.jar';
```

To perform a bug fix or version upgrade, run the following command to rename the JAR package to the name in Step 1 after compilation:

```
DROP resource esri-geometry-api.jar; DROP resource spatial-sdk-hive.jar; DROP resource spatial-sdk-odps.jar; ADD jar esri-geometry-api.jar; ADD jar spatial-sdk-hive.jar; ADD jar spatial-sdk-odps.jar;
```

Before you run SQL statements to call the functions, submit the following flags. The isolation flag provides a secure and isolated environment for running UDFs.

```
SET odps.sql.hive.compatible=true; SET odps.sql.udf.java.retain.legacy=false; SET odps.isolation.session.enable=true;
```

**Test the functions**

Submit SQL statements in the MaxCompute client to test whether a UDF can work as expected. Sample commands:

```
set odps.sql.hive.compatible=true; select ST_AsText(ST_Point(1, 2));
```

The following output indicates that the UDF is registered with MaxCompute.

```
+-----+
| _c0 |
+-----+
| POINT (1 2) |
+-----+
```

For more information about how to use the geographic function, see UDF-Documentation.

#### 3.12.2 Constructors

##### 3.12.2.1 ST_AsBinary

This topic describes the Constructor function ST_AsBinary and provides an example for reference. Function declaration:

```
ST_AsBinary(ST_Geometry)
```

Description: This function returns the well-known binary (WKB) expression of the input geometry. Example:

```
SELECT ST_AsBinary(ST_Point(1, 2)) FROM onerow;
```

Returned results:

```
WKB representation of POINT (1 2)
```

##### 3.12.2.2 ST_AsGeoJson

This topic describes the Constructor function ST_AsGeoJson and provides an example for reference. Function declaration:

```
ST_AsGeoJson(geometry)
```

Description: This function returns the GeoJSON expression of the input geometry. Example:

```
SELECT ST_AsGeoJson(ST_Point(1.0, 2.0)) from onerow;
```

Returned results:

```json
{"type":"Point", "coordinates":[1.0, 2.0]}
```

##### 3.12.2.3 ST_AsJson

This topic describes the Constructor function ST_AsJson and provides examples for reference. Function declaration:

```
ST_AsJSON(ST_Geometry)
```

Description: This function returns the JSON expression of the input geometry.

```
SELECT ST_AsJSON(ST_Point(1.0, 2.0)) from onerow;
```

Returned results:

```json
{"x":1.0,"y":2.0} SELECT ST_AsJSON(ST_SetSRID(ST_Point(1, 1), 4326)) from onerow;
```

Returned results:

```json
{"x":1.0,"y":1.0,"spatialReference":{"wkid":4326}}
```

##### 3.12.2.4 ST_AsShape

This topic describes the Constructor function ST_AsShape and provides an example for reference. Function declaration:

```
ST_AsShape(ST_Geometry)
```

Description: This function returns the ESRI shape expression of the input geometry. Example:

```
SELECT ST_AsShape(ST_Point(1, 2)) FROM onerow;
```

Returned results:

```
Esri shape representation of POINT (1 2)
```

##### 3.12.2.5 ST_AsText

This topic describes the Constructor function ST_AsText and provides an example for reference. Function declaration:

```
ST_AsText(ST_Geometry)
```

Description: This function returns the well-known text (WKT) expression of the input geometry. Example:

```
SELECT ST_AsText(ST_Point(1, 2)) FROM onerow;
```

Returned results:

```
POINT (1 2)
```

##### 3.12.2.6 ST_GeomCollection

This topic describes the ST_GeomCollection function of the Constructors function and provides an example for reference. Function declaration:

```
ST_GeomCollection(wkt)
```

Description: This function constructs a multi-part geometry based on the well-known text (WKT) representation defined by the Open Geospatial Consortium (OGC).

**Important**

The ST_GeomCollection function in MaxCompute supports only the multi-part geometry feature, not the collection feature. Example:

```
SELECT ST_GeomCollection('multipoint ((1 0), (2 3))') FROM src LIMIT 1; -- Construct a multipoint geometry. ST_GeomCollection('POINT(1 1), LINESTRING(2 0,3 0)') -- The collection feature is not supported.
```

##### 3.12.2.7 ST_GeomFromGeoJson

This topic describes the Constructor function ST_GeomFromGeoJson and provides an example for reference. Function declaration:

```
ST_GeomFromGeoJson(json)
```

Description: This function constructs a geometry based on the input GeoJSON expression. Example:

```
SELECT ST_GeomFromGeoJson('{"type":"Point", "coordinates":[1.2, 2.4]}') FROM src LIMIT 1; -- Construct a point. SELECT ST_GeomFromGeoJson('{"type":"LineString", "coordinates":[[1,2], [3,4]]}') FROM src LIMIT 1; -- Construct a linestring.
```

##### 3.12.2.8 ST_GeomFromJSON

This topic describes the Constructor function ST_GeomFromJSON and provides an example for reference. Function declaration:

```
ST_GeomFromJSON(json)
```

Description: This function constructs a geometry based on the input ESRI JSON expression. Example:

```
SELECT ST_GeomFromJSON('{"x":0.0,"y":0.0}') FROM src LIMIT 1; -- Construct a point.
```

##### 3.12.2.9 ST_GeomFromShape

This topic describes the Constructor function ST_GeomFromShape and provides an example for reference. Function declaration:

```
ST_GeomFromShape(shape)
```

Description: This function constructs a geometry based on the input ESRI shape expression. Example:

```
SELECT ST_GeomFromShape(ST_AsShape(ST_Point(1, 2))); -- Construct a point.
```

##### 3.12.2.10 ST_GeomFromText

This topic describes the Constructor function ST_GeomFromText and provides an example for reference. Function declaration:

```
ST_GeomFromText(wkt)
```

Description: This function constructs a geometry based on the input well-known text (WKT) representation defined by the Open Geospatial Consortium (OGC). Example:

```
SELECT ST_GeomFromText('linestring (1 0, 2 3)') FROM src LIMIT 1; -- Construct a linestring. SELECT ST_GeomFromText('multipoint ((1 0), (2 3))') FROM src LIMIT 1; -- Construct a multipoint geometry.
```

##### 3.12.2.11 ST_GeomFromWKB

This topic describes the Constructor function ST_GeomFromWKB and provides an example for reference. Function declaration:

```
ST_GeomFromWKB(wkb)
```

Description: This function constructs a geometry based on the input well-known binary (WKB) expression that complies with the Open Geospatial Consortium (OGC) standards. Example:

```
SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)'))) FROM src LIMIT 1; -- Construct a linestring. SELECT ST_GeomFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))'))) FROM src LIMIT 1; -- Construct a multipoint geometry.
```

##### 3.12.2.12 ST_GeometryType

This topic describes the Constructor function ST_GeometryType and provides examples for reference. Function declaration:

```
ST_GeometryType(geometry)
```

Description: This function returns the type of the input geometry.

```
SELECT ST_GeometryType(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_GeometryType(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_GeometryType(ST_Polygon(2,0, 2,3, 3,0)) FROM src LIMIT 1;
```

Returned results:

##### 3.12.2.13 ST_LineString

This topic describes the Constructor function ST_LineString and provides an example for reference. Function declaration:

```
ST_LineString(x, y, [x, y]*) ST_LineString('linestring( ... )') ST_LineString(array(x+), array(y+)) ST_LineString(array(ST_Point(x,y)+)))
```

Description: This function constructs a two-dimensional line. Example:

```
SELECT ST_LineString(1, 1, 2, 2, 3, 3) from src LIMIT 1; SELECT ST_LineString('linestring(1 1, 2 2, 3 3)') from src LIMIT 1; SELECT ST_LineString(array(1,2,3), array (1,2,3)) from src LIMIT 1; SELECT ST_LineString(array(ST_Point(1, 1), ST_Point(2,2), ST_Point(3,3))) from src LIMIT 1;
```

##### 3.12.2.14 ST_LineFromWKB

This topic describes the Constructor function ST_LineFromWKB and provides an example for reference. Function declaration:

```
ST_LineFromWKB(wkb)
```

Description: This function constructs a two-dimensional line based on the input well-known binary (WKB) representation defined by the Open Geospatial Consortium (OGC). Example:

```
SELECT ST_LineFromWKB(ST_AsBinary(ST_GeomFromText('linestring (1 0, 2 3)'))) FROM src LIMIT 1; -- Construct a two-dimensional line.
```

##### 3.12.2.15 ST_MultiLineString

This topic describes the Constructor function ST_MultiLineString and provides an example for reference. Function declaration:

```
ST_MultiLineString(array(x1, y1, x2, y2, ... ), array(x1, y1, x2, y2, ... ), ... ) ST_MultiLineString('multilinestring( ... )')
```

Description: This function constructs a two-dimensional multilinestring. Example:

```
SELECT ST_MultiLineString(array(1, 1, 2, 2), array(10, 10, 20, 20)) from src LIMIT 1; SELECT ST_MultiLineString('multilinestring ((1 1, 2 2), (10 10, 20 20))', 0) from src LIMIT 1; -- Construct a two-dimensional multilinestring.
```

##### 3.12.2.16 ST_MLineFromWKB

This topic describes the Constructor function ST_MLineFromWKB and provides an example for reference. Function declaration:

```
ST_MLineFromWKB(wkb)
```

Description: This function constructs a two-dimensional multilinestring based on the input well-known binary (WKB) expression that complies with the Open Geospatial Consortium (OGC) standards. Example:

```
SELECT ST_MLineFromWKB(ST_AsBinary(ST_GeomFromText('multilinestring ((1 0, 2 3), (5 7, 7 5))'))) FROM src LIMIT
```

1;

```
-- Construct a two-dimensional multilinestring.
```

##### 3.12.2.17 ST_MultiPoint

This topic describes the Constructor function ST_MultiPoint and provides an example for reference. Function declaration:

```
ST_MultiPoint(x1, y1, x2, y2, x3, y3) ST_MultiPoint('multipoint( ... )')
```

Description: This function constructs a two-dimensional multipoint geometry. Example:

```
SELECT ST_MultiPoint(1, 1, 2, 2, 3, 3) from src LIMIT 1; -- Construct a three-point geometry. SELECT ST_MultiPoint('MULTIPOINT ((10 40), (40 30))') from src LIMIT 1; -- Construct a two-point geometry.
```

##### 3.12.2.18 ST_MPointFromWKB

This topic describes the Constructor function ST_MPointFromWKB and provides an example for reference. Function declaration:

```
ST_MPointFromWKB(wkb)
```

Description: This function constructs a two-dimensional multipoint geometry based on the input well-known binary (WKB) representation defined by the Open Geospatial Consortium (OGC). Example:

```
SELECT ST_MPointFromWKB(ST_AsBinary(ST_GeomFromText('multipoint ((1 0), (2 3))'))) FROM src LIMIT 1; -- Construct a two-dimensional multipoint geometry.
```

##### 3.12.2.19 ST_MultiPolygon

This topic describes the Constructor function ST_MultiPolygon and provides an example for reference. Function declaration:

```
ST_MultiPolygon(array(x1, y1, x2, y2, ... ), array(x1, y1, x2, y2, ... ), ... ) ST_MultiPolygon('multipolygon ( ... )')
```

Description: This function constructs a two-dimensional multipolygon. Example:

```
SELECT ST_MultiPolygon(array(1, 1, 1, 2, 2, 2, 2, 1), array(3, 3, 3, 4, 4, 4, 4, 3)) from src LIMIT 1; SELECT ST_MultiPolygon('multipolygon (((0 0, 0 1, 1 0, 0 0)), ((2 2, 2 3, 3 2, 2 2)))') from src LIMIT 1; -- Construct a two-dimensional multipolygon.
```

##### 3.12.2.20 ST_MPolyFromWKB

This topic describes the Constructor function ST_MPolyFromWKB and provides an example for reference. Function declaration:

```
ST_MPolyFromWKB(wkb)
```

Description: This function constructs a two-dimensional multipolygon based on the input well-known binary (WKB) expression that complies with the Open Geospatial Consortium (OGC) standards. Example:

```
SELECT ST_MPolyFromWKB(ST_AsBinary(ST_GeomFromText('multipolygon (((0 0, 1 0, 0 1, 0 0)), ((2 2, 1 2, 2 1, 2 2) ))'))) FROM src LIMIT 1; -- Construct a two-dimensional multipolygon.
```

##### 3.12.2.21 ST_Point

This topic describes the Constructor function ST_Point and provides an example for reference. Function declaration:

```
ST_Point(x, y) ST_Point('point (x y)')
```

Description: This function constructs a two-dimensional point. Example:

```
SELECT ST_Point(longitude, latitude) from src LIMIT 1; SELECT ST_Point('point (0 0)') from src LIMIT 1; -- Construct a two-dimensional point.
```

##### 3.12.2.22 ST_PointFromWKB

This topic describes the Constructor function ST_PointFromWKB and provides an example for reference. Function declaration:

```
ST_PointFromWKB(wkb)
```

Description: This function constructs a two-dimensional point based on the input well-known binary (WKB) expression that complies with the Open Geospatial Consortium (OGC) standards. Example:

```
SELECT ST_PointFromWKB(ST_AsBinary(ST_GeomFromText('point (1 0))'))) FROM src LIMIT 1; -- Construct a two-dimensional point.
```

##### 3.12.2.23 ST_PointZ

This topic describes the Constructor function ST_PointZ and provides an example for reference. Function declaration:

```
ST_PointZ(x, y, z)
```

Description: This function constructs a three-dimensional point. Example:

```
SELECT ST_PointZ(longitude, latitude, elevation) from src LIMIT 1; -- Construct a three-dimensional point.
```

##### 3.12.2.24 ST_Polygon

This topic describes the Constructor function ST_Polygon and provides an example for reference. Function declaration:

```
ST_Polygon(x, y, [x, y]*) ST_Polygon('polygon( ... )')
```

Description: This function constructs a two-dimensional polygon. Example:

```
SELECT ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1) from src LIMIT 1; -- Construct a square. SELECT ST_Polygon('polygon ((1 1, 4 1, 1 4))') from src LIMIT 1; -- Construct a triangle.
```

##### 3.12.2.25 ST_PolyFromWKB

This topic describes the Constructor function ST_PolyFromWKB and provides an example for reference. Function declaration:

```
ST_PolyFromWKB(wkb)
```

Description: This function constructs a two-dimensional polygon based on the input well-known binary (WKB) representation defined by the Open Geospatial Consortium (OGC). Example:

```
SELECT ST_PolyFromWKB(ST_AsBinary(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))'))) FROM src LIMIT 1; -- Construct a two-dimensional polygon.
```

##### 3.12.2.26 ST_SetSRID

This topic describes the Constructor function ST_SetSRID and provides an example for reference. Function declaration:

```
ST_SetSRID(<ST_Geometry>, SRID)
```

Description: This function sets the spatial reference system identifier (SRID) of the input geometry. Example:

```
SELECT ST_SetSRID(ST_Point(1.5, 2.5), 4326)) FROM src LIMIT 1; -- Construct a point and set its SRID to 4326.
```

#### 3.12.3 Accessors

##### 3.12.3.1 ST_Area

This topic describes the Accessor function ST_Area and provides an example for reference. Function declaration:

```
ST_Area(ST_Polygon)
```

Description: This function returns the areas of one or more polygons. Example:

```
SELECT ST_Area(ST_Polygon(1,1, 1,4, 4,4, 4,1)) FROM src LIMIT 1;
```

Returned results:

```
9.0
```

##### 3.12.3.2 ST_Centroid

This topic describes the Accessor function ST_Centroid and provides examples for reference. Function declaration:

```
ST_Centroid(polygon)
```

Description: This function returns the centroid of the minimum bounding rectangle of the input polygon.

```
SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 3 6, 6 0, 0 0))')) FROM src LIMIT 1;
```

Returned results:

```
POINT(3 3) SELECT ST_Centroid(ST_GeomFromText('polygon ((0 0, 0 8, 8 0, 0 0))')) FROM src LIMIT 1;
```

Returned results:

```
POINT(4 4)
```

##### 3.12.3.3 ST_CoordDim

This topic describes the Accessor function ST_CoordDim and provides examples for reference. Function declaration:

```
ST_CoordDim(geometry)
```

Description: This function returns the coordinate dimension of the input geometry.

```
SELECT ST_CoordDim(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_CoordDim(ST_PointZ(1.5,2.5, 3) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_CoordDim(ST_Point(1.5, 2.5, 3., 4.)) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.4 ST_Dimension

This topic describes the Accessor function ST_Dimension and provides examples for reference. Function declaration:

```
ST_Dimension(geometry)
```

Description: This function returns the spatial dimension of the input geometry.

```
SELECT ST_Dimension(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_Dimension(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_Dimension(ST_Polygon(2,0, 2,3, 3,0)) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.5 ST_Distance

This topic describes the Accessor function ST_Distance and provides an example for reference. Function declaration:

```
ST_Distance(ST_Geometry1, ST_Geometry2)
```

Description: This function returns the distance between two geometries. Example:

```
SELECT ST_Distance(ST_Point(0.0,0.0), ST_Point(3.0,4.0)) FROM src LIMIT 1;
```

Returned results:

```
5.0
```

##### 3.12.3.6 ST_GeodesicLengthWGS84

This topic describes the Accessor function ST_GeodesicLengthWGS84 and provides examples for reference. Function declaration:

```
ST_GeodesicLengthWGS84(line)
```

Description: This function returns the distance in meters on a spheroid based on World Geodetic System 1984 (WGS84). The geometry must be in WGS84. Otherwise, this function returns NULL.

```
SELECT ST_GeodesicLengthWGS84(ST_SetSRID(ST_Linestring(0.0,0.0, 0.3,0.4), 4326)) FROM src LIMIT 1;
```

Returned results:

```
55km SELECT ST_GeodesicLengthWGS84(ST_GeomFromText('MultiLineString((0.0 80.0, 0.3 80.4))', 4326)) FROM src LIMIT 1;
```

Returned results:

```
45km
```

##### 3.12.3.7 ST_GeometryN

This topic describes the Accessor function ST_GeometryN and provides examples for reference. Function declaration:

```
ST_GeometryN(ST_GeometryCollection, n)
```

Description: This function returns the nth geometry in the input geometry collection. n starts from 1.

```
SELECT ST_GeometryN(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 10))'), 3) FROM src LIMIT 1;
```

Returned results:

```
ST_Point(20 20) SELECT ST_GeometryN(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8))'), 2) FROM src LIMIT 1;
```

Returned results:

```
ST_Linestring(20 20, 7 8)
```

##### 3.12.3.8 ST_Is3D

This topic describes the Accessor function ST_Is3D and provides an example for reference. Function declaration:

```
ST_Is3D(geometry)
```

Description: If the input geometry has Z coordinates, this function returns True. Otherwise, this function returns False. Example:

```
SELECT ST_Is3D(ST_Polygon(1,1, 1,4, 4,4, 4,1)) FROM src LIMIT 1; -- False is returned. SELECT ST_Is3D(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1; -- False is returned. SELECT ST_Is3D(ST_Point(3., 4.)) FROM src LIMIT 1; -- False is returned. SELECT ST_Is3D(ST_PointZ(3., 4., 2)) FROM src LIMIT 1; -- True is returned.
```

##### 3.12.3.9 ST_IsClosed

This topic describes the Accessor function ST_IsClosed and provides an example for reference. Function declaration:

```
ST_IsClosed(ST_[Multi]LineString)
```

Description: If the input linestring or linestrings are closed, this function returns True. Otherwise, it returns False. Example:

```
SELECT ST_IsClosed(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1; -- True is returned. SELECT ST_IsClosed(ST_LineString(0.,0., 3.,4.)) FROM src LIMIT 1; -- False is returned.
```

##### 3.12.3.10 ST_IsEmpty

This topic describes the Accessor function ST_IsEmpty and provides an example for reference. Function declaration:

```
ST_IsEmpty(geometry)
```

Description: If the input geometry is empty, this function returns True. Otherwise, it returns False. Example:

```
SELECT ST_IsEmpty(ST_Point(1.5, 2.5)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsEmpty(ST_GeomFromText('point empty')) FROM src LIMIT 1; -- True is returned.
```

##### 3.12.3.11 ST_IsMeasured

This topic describes the Accessor function ST_IsMeasured and provides an example for reference. Function declaration:

```
ST_IsMeasured(geometry)
```

Description: If the input geometry has M coordinates (measures), this function returns True. Otherwise, it returns False. Example:

```
SELECT ST_IsMeasured(ST_Polygon(1,1, 1,4, 4,4, 4,1)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_Point(3., 4.)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsMeasured(ST_PointM(3., 4., 2)) FROM src LIMIT 1; -- True is returned.
```

##### 3.12.3.12 ST_IsSimple

This topic describes the Accessor function ST_IsSimple and provides an example for reference. Function declaration:

```
ST_IsSimple(geometry)
```

Description: If the input geometry is a simple object, this function returns True. Otherwise, it returns False. Example:

```
SELECT ST_IsSimple(ST_Point(1.5, 2.5)) FROM src LIMIT 1; -- True is returned. SELECT ST_IsSimple(ST_LineString(0.,0., 1.,1., 0.,1., 1.,0.)) FROM src LIMIT 1; -- False is returned.
```

##### 3.12.3.13 ST_IsRing

This topic describes the Accessor function ST_IsRing and provides an example for reference. Function declaration:

```
ST_IsRing(ST_LineString)
```

Description: This function specifies whether the input geometry is a closed ring, whose start point and end point are the same. If the input geometry is a closed ring, this function returns True. Otherwise, this function returns False. Example:

```
SELECT ST_IsRing(ST_LineString(0.,0., 3.,4., 0.,4., 0.,0.)) FROM src LIMIT 1; -- True is returned. SELECT ST_IsRing(ST_LineString(0.,0., 1.,1., 1.,2., 2.,1., 1.,1., 0.,0.)) FROM src LIMIT 1; -- False is returned. SELECT ST_IsRing(ST_LineString(0.,0., 3.,4.)) FROM src LIMIT 1; -- False is returned.
```

##### 3.12.3.14 ST_Length

This topic describes the Accessor function ST_Length and provides an example for reference. Function declaration:

```
ST_Length(line)
```

Description: This function returns the length of the input line segment. Example:

```
SELECT ST_Length(ST_Line(0.0,0.0, 3.0,4.0)) FROM src LIMIT 1;
```

Returned results:

```
5.0
```

##### 3.12.3.15 ST_M

This topic describes the Accessor function ST_M and provides an example for reference. Function declaration:

```
ST_M(geometry)
```

Description: This function returns the M coordinate of the input geometry. Example:

```
SELECT ST_M(ST_PointM(3., 4., 2)) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.16 ST_MaxM

This topic describes the Accessor function ST_MaxM and provides examples for reference. Function declaration:

```
ST_MaxM(geometry)
```

Description: This function returns the maximum M coordinate of the input geometry.

```
SELECT ST_MaxM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MaxM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.17 ST_MinM

This topic describes the Accessor function ST_MinM and provides examples for reference. Function declaration:

```
ST_MinM(geometry)
```

Description: This function returns the minimum M coordinate of the input geometry.

```
SELECT ST_MinM(ST_PointM(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MinM(ST_LineString('linestring m (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.18 ST_X

This topic describes the Accessor function ST_X and provides an example for reference. Function declaration:

```
ST_X(point)
```

Description: This function returns the X coordinate of the input point. Example:

```
SELECT ST_X(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
1.5
```

##### 3.12.3.19 ST_Y

This topic describes the Accessor function ST_Y and provides an example for reference. Function declaration:

```
ST_Y(point)
```

Description: This function returns the Y coordinate of the input point. Example:

```
SELECT ST_Y(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
2.5
```

##### 3.12.3.20 ST_Z

This topic describes the Accessor function ST_Z and provides an example for reference. Function declaration:

```
ST_Z(point)
```

Description: This function returns the Z coordinate of the input point. Example:

```
SELECT ST_Z(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
1.5
```

##### 3.12.3.21 ST_MaxX

This topic describes the Accessor function ST_MaxX and provides examples for reference. Function declaration:

```
ST_MaxX(geometry)
```

Description: This function returns the maximum X coordinate of the input geometry.

```
SELECT ST_MaxX(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
1.5 SELECT ST_MaxX(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
3.0
```

##### 3.12.3.22 ST_MaxY

This topic describes the Accessor function ST_MaxX and provides examples for reference. Function declaration:

```
ST_MaxY(geometry)
```

Description: This function returns the maximum Y coordinate of the input geometry.

```
SELECT ST_MaxY(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
2.5 SELECT ST_MaxY(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
2.5
```

##### 3.12.3.23 ST_MaxZ

This topic describes the Accessor function ST_MaxZ and provides examples for reference. Function declaration:

```
ST_MaxZ(geometry)
```

Description: This function returns the maximum Z coordinate of the input geometry.

```
SELECT ST_MaxZ(ST_PointZ(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MaxZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.24 ST_MinX

This topic describes the Accessor function ST_MinX and provides examples for reference. Function declaration:

```
ST_MinX(geometry)
```

Description: This function returns the minimum X coordinate of the input geometry.

```
SELECT ST_MinX(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
1.5 SELECT ST_MinX(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
3.0
```

##### 3.12.3.25 ST_MinY

This topic describes the Accessor function ST_MinY and provides examples for reference. Function declaration:

```
ST_MinY(geometry)
```

Description: This function returns the minimum Y coordinate of the input geometry.

```
SELECT ST_MinY(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
2.5 SELECT ST_MinY(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
2.2
```

##### 3.12.3.26 ST_MinZ

This topic describes the Accessor function ST_MinZ and provides examples for reference. Function declaration:

```
ST_MinZ(geometry)
```

Description: This function returns the minimum Z coordinate of the input geometry.

```
SELECT ST_MinZ(ST_PointZ(1.5, 2.5, 2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_MinZ(ST_LineString('linestring z (1.5 2.5 2, 3.0 2.2 1)')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.27 ST_NumGeometries

This topic describes the Accessor function ST_NumGeometries and provides examples for reference. Function declaration:

```
ST_NumGeometries(ST_GeometryCollection)
```

Description: This function returns the number of geometries in the input geometry collection.

```
SELECT ST_NumGeometries(ST_GeomFromText('multipoint ((10 40), (40 30), (20 20), (30 10))')) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_NumGeometries(ST_GeomFromText('multilinestring ((2 4, 10 10), (20 20, 7 8))')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.28 ST_NumInteriorRing

This topic describes the Accessor function ST_NumInteriorRing and provides examples for reference. Function declaration:

```
ST_NumInteriorRing(ST_Polygon)
```

Description: This function returns the number of interior rings of the input polygon.

```
SELECT ST_NumInteriorRing(ST_Polygon(1,1, 1,4, 4,1)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_NumInteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.29 ST_NumPoints

This topic describes the Accessor function ST_NumPoints and provides examples for reference. Function declaration:

```
ST_NumPoints(geometry)
```

Description: This function returns the number of points in the input geometry.

```
SELECT ST_NumPoints(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_NumPoints(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
SELECT ST_NumPoints(ST_GeomFromText('polygon ((0 0, 10 0, 0 10, 0 0))')) FROM src LIMIT 1;
```

Returned results:

##### 3.12.3.30 ST_PointN

This topic describes the Accessor function ST_PointN and provides an example for reference. Function declaration:

```
ST_PointN(ST_Geometry, n)
```

Description: This function returns the nth point of one or more linestrings. Example:

```
SELECT ST_PointN(ST_LineString(1.5,2.5, 3.0,2.2), 2) FROM src LIMIT 1;
```

Returned results:

```
POINT(3.0 2.2)
```

##### 3.12.3.31 ST_StartPoint

This topic describes the Accessor function ST_StartPoint and provides an example for reference. Function declaration:

```
ST_StartPoint(geometry)
```

Description: This function returns the first point of the input linestring. Example:

```
SELECT ST_StartPoint(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
POINT(1.5 2.5)
```

##### 3.12.3.32 ST_EndPoint

This topic describes the Accessor function ST_EndPoint and provides an example for reference. Function declaration:

```
ST_EndPoint(geometry)
```

Description: This function returns the last point of the input linestring. Example:

```
SELECT ST_EndPoint(ST_LineString(1.5,2.5, 3.0,2.2)) FROM src LIMIT 1;
```

Returned results:

```
POINT(3.0 2.0)
```

##### 3.12.3.33 ST_SRID

This topic describes the Accessor function ST_SRID and provides an example for reference. Function declaration:

```
ST_SRID(ST_Geometry)
```

Description: This function returns the spatial reference system identifier (SRID) of the input geometry. Example:

```
SELECT ST_SRID(ST_Point(1.5, 2.5)) FROM src LIMIT 1;
```

Returned results:

```
returns SRID 0
```

#### 3.12.4 Operations

##### 3.12.4.1 ST_Aggr_ConvexHull

This topic describes the Operation function ST_Aggr_ConvexHull and provides an example for reference. Function declaration:

```
ST_Aggr_ConvexHull(ST_Geometry)
```

Description: This function returns a convex hull for input geometries by using aggregate transformation. Example:

```
SELECT ST_Aggr_ConvexHull(geometry) FROM source; -- Return the convex hull of input geometries from the data source by using aggregate transformation.
```

##### 3.12.4.2 ST_Aggr_Intersection

This topic describes the Operation function ST_Aggr_Intersection and provides an example for reference. Function declaration:

```
ST_Aggr_Intersection(ST_Geometry)
```

Description: This function returns the intersection of input geometries by using aggregate transformation. Example:

```
SELECT ST_Aggr_Intersection(geometry) FROM source; -- Return the intersection of input geometries from the data source by using aggregate transformation.
```

##### 3.12.4.3 ST_Aggr_Union

This topic describes the Operation function ST_Aggr_Union and provides an example for reference. Function declaration:

```
ST_Aggr_Union(ST_Geometry)
```

Description: This function returns a union of input geometries by using aggregate transformation. Example:

```
SELECT ST_Aggr_Union(geometry) FROM source; -- Return the union of input geometries from the data source by using aggregate transformation.
```

##### 3.12.4.4 ST_Bin

This topic describes the Operation function ST_Bin. Function declaration:

```
ST_Bin(placeholder)
```

Description: This function returns the bin ID of the input point.

##### 3.12.4.5 ST_BinEnvelope

This topic describes the Operation function ST_BinEnvelop. Function declaration:

```
ST_BinEnvelope(binsize, point)
```

Description: This function returns the binary envelope for the input point. Function declaration:

```
ST_BinEnvelope(binsize, binid)
```

Description: This function returns the binary envelope for the input bin ID.

##### 3.12.4.6 ST_Boundary

This topic describes the Operation function ST_Boundary and provides examples for reference. Function declaration:

```
ST_Boundary(ST_Geometry)
```

Description: This function returns the boundary of the input geometry ST_Geometry.

```
SELECT ST_Boundary(ST_LineString(0,1, 1,0))) FROM src LIMIT 1;
```

Returned results:

```
MULTIPOINT((1 0),(0 1)) SELECT ST_Boundary(ST_Polygon(1,1, 4,1, 1,4)) FROM src LIMIT 1;
```

Returned results:

```
LINESTRING(1 1, 4 1, 1 4, 1 1)
```

##### 3.12.4.7 ST_Buffer

This topic describes the Operation function ST_Buffer. Function declaration:

```
ST_Buffer(geometry, distance)
```

Description: This function returns a geometry that indicates all points whose distance from this geometry to the input geometry is less than or equal to the value of the distance parameter.

##### 3.12.4.8 ST_ConvexHull

This topic describes the Operation function ST_ConvexHull and provides an example for reference. Function declaration:

```
ST_ConvexHull(ST_Geometry, ST_Geometry, ...)
```

Description: This function returns the geometric object ST_Geometry as the convex hull of the specified geometry. Example:

```
SELECT ST_AsText(ST_ConvexHull(ST_Point(0, 0), ST_Point(0, 1), ST_Point(1, 1))) FROM onerow;
```

Returned results:

```
MULTIPOLYGON (((0 0, 1 1, 0 1, 0 0)))
```

##### 3.12.4.9 ST_Difference

This topic describes the Operation function ST_Difference and provides examples for reference. Function declaration:

```
ST_Difference(ST_Geometry1, ST_Geometry2)
```

Description: This function returns a geometry that indicates the difference between ST_Geometry1 and ST_Geometry2.

```
SELECT ST_AsText(ST_Difference(ST_MultiPoint(1, 1, 1.5, 1.5, 2, 2), ST_Point(1.5, 1.5))) FROM onerow;
```

Returned results:

```
MULTIPOINT (1 1, 2 2)
```

```
SELECT ST_AsText(ST_Difference(ST_Polygon(0, 0, 0, 10, 10, 10, 10, 0), ST_Polygon(0, 0, 0, 5, 5, 5, 5, 0))) fro m onerow;
```

Returned results:

```
MULTIPOLYGON (((10 0, 10 10, 0 10, 0 5, 5 5, 5 0, 10 0)))
```

##### 3.12.4.10 ST_Envelope

This topic describes the Operation function ST_Envelope and provides examples for reference. Function declaration:

```
ST_Envelope(ST_Geometry)
```

Description: This function returns the envelope of the input geometry. If the specified geometry is a point, a horizontal line, or a vertical line, this function returns the common difference or an empty envelope.

```
SELECT ST_Envelope(ST_LineString(0,0, 2,2)) from src LIMIT 1;
```

Returned results:

```
POLYGON ((0 0, 2 0, 2 2, 0 2, 0 0)) SELECT ST_Envelope(ST_Polygon(2,0, 2,3, 3,0)) from src LIMIT 1;
```

Returned results:

```
POLYGON ((2 0, 3 0, 3 3, 2 3, 2 0))
```

##### 3.12.4.11 ST_ExteriorRing

This topic describes the Operation function ST_ExteriorRing and provides examples for reference. Function declaration:

```
ST_ExteriorRing(polygon)
```

Description: This function returns the exterior ring of a polygon as a linestring.

```
SELECT ST_ExteriorRing(ST_Polygon(1,1, 1,4, 4,1)) FROM src LIMIT 1;
```

Returned results:

```
LINESTRING(1 1, 4 1, 1 4, 1 1) SELECT ST_ExteriorRing(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))')) FROM src LIMIT 1;
```

Returned results:

```
LINESTRING (8 0, 0 8, 0 0, 8 0)
```

##### 3.12.4.12 ST_InteriorRingN

This topic describes the Operation function ST_InteriorRingN and provides an example for reference. Function declaration:

```
ST_InteriorRingN(ST_Polygon, n)
```

Description: This function returns the nth interior ring of a polygon as a linestring. Example:

```
SELECT ST_InteriorRingN(ST_Polygon('polygon ((0 0, 8 0, 0 8, 0 0), (1 1, 1 5, 5 1, 1 1))'), 1) FROM src LIMIT 1
```

; Returned results:

```
LINESTRING (1 1, 5 1, 1 5, 1 1)
```

##### 3.12.4.13 ST_Intersection

This topic describes the Operation function ST_Intersection and provides examples for reference. Function declaration:

```
ST_Intersection(ST_Geometry1, ST_Geometry2)
```

Description: This function returns a geometry that indicates the intersection of the input geometries. If the input geometries intersect in a lower dimension, ST_Intersection may drop lower-dimension intersections or return a closed linestring.

```
SELECT ST_AsText(ST_Intersection(ST_Point(1,1), ST_Point(1,1))) FROM onerow;
```

Returned results:

```
POINT (1 1) SELECT ST_AsText(ST_Intersection(ST_GeomFromText('linestring(0 2, 0 0, 2 0)'), ST_GeomFromText('linestring(0 3, 0 1, 1 0, 3 0)'))) FROM onerow;
```

Returned results:

```
MULTILINESTRING ((1 0, 2 0), (0 2, 0 1)) SELECT ST_AsText(ST_Intersection(ST_LineString(0,2, 2,3), ST_Polygon(1,1, 4,1, 4,4, 1,4))) FROM onerow;
```

Returned results:

```
MULTILINESTRING ((1 2.5, 2 3)) SELECT ST_AsText(ST_Intersection(ST_Polygon(2,0, 2,3, 3,0), ST_Polygon(1,1, 4,1, 4,4, 1,4))) FROM onerow;
```

Returned results:

```
MULTIPOLYGON (((2.67 1, 2 3, 2 1, 2.67 1))) SELECT ST_AsText(ST_Intersection(ST_Polygon(2,0, 3,1, 2,1), ST_Polygon(1,1, 4,1, 4,4, 1,4))) FROM onerow;
```

Returned results:

```
MULTIPOLYGON EMPTY or LINESTRING (2 1, 3 1, 2 1)
```

##### 3.12.4.14 ST_SymmetricDiff

This topic describes the ST_SymmetricDiff function and provides examples of using this function. Function declaration:

```
ST_SymmetricDiff(ST_Geometry1, ST_Geometry2)
```

Description: This function returns a geometry that consists of the symmetric differences of the input geometries.

```
SELECT ST_AsText(ST_SymmetricDiff(ST_LineString('linestring(0 2, 2 2)'), ST_LineString('linestring(1 2, 3 2)'))) FROM onerow;
```

Returned result:

```
MULTILINESTRING((0 2, 1 2), (2 2, 3 2)) SELECT ST_AsText(ST_SymmetricDiff(ST_SymmetricDiff(ST_Polygon('polygon((0 0, 2 0, 2 2, 0 2, 0 0))'), ST_Polygon('polygon((1 1, 3 1, 3 3, 1 3, 1 1))'))) from onerow;
```

Returned result:

```
MULTIPOLYGON (((0 0, 2 0, 2 1, 1 1, 1 2, 0 2, 0 0)), ((3 1, 3 3, 1 3, 1 2, 2 2, 2 1, 3 1)))
```

##### 3.12.4.15 ST_Union

This topic describes the ST_Union function and provides an example of using this function. Function declaration:

```
ST_Union(ST_Geometry, ST_Geometry, ...)
```

Description: This function returns a geometry that is the union of the input geometries. Example:

```
SELECT ST_AsText(ST_Union(ST_Polygon(1, 1, 1, 4, 4, 4, 4, 1), ST_Polygon(4, 1, 4, 4, 4, 8, 8, 1))) FROM onerow;
```

Returned result:

```
MULTIPOLYGON (((4 1, 8 1, 4 8, 4 4, 1 4, 1 1, 4 1)))
```

#### 3.12.5 Relationship tests

##### 3.12.5.1 ST_Contains

This topic describes the ST_Contains function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Contains(geometry1, geometry2)
```

Description: If geometry1 contains geometry2, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Contains(st_polygon(1,1, 1,4, 4,4, 4,1), st_point(2, 3) from src LIMIT 1; -- true is returned. SELECT ST_Contains(st_polygon(1,1, 1,4, 4,4, 4,1), st_point(8, 8) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.2 ST_Crosses

This topic describes the ST_Crosses function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Crosses(geometry1, geometry2)
```

Description: If geometry1 crosses geometry2, this function returns true. Otherwise, this function returns false. Crossing indicates that some points in the two geometries are the same. Example:

```
SELECT ST_Crosses(st_linestring(0,0, 1,1), st_linestring(1,0, 0,1)) from src LIMIT 1; -- true is returned. SELECT ST_Crosses(st_linestring(2,0, 2,3), st_polygon(1,1, 1,4, 4,4, 4,1)) from src LIMIT 1; -- true is returned. SELECT ST_Crosses(st_linestring(0,2, 0,1), ST_linestring(2,0, 1,0)) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.3 ST_Disjoint

This topic describes the ST_Disjoint function and provides examples of using this function.

```
BOOLEAN ST_Disjoint(geometry1, geometry2)
```

Description: This function is used to determine whether two geometry objects are disjoint. If two geometry objects do not have any intersection point, line, or plane, this function returns True. Otherwise, this function returns False.

```
SELECT ST_Disjoint(ST_LineString(0,0, 0,1), ST_LineString(1,1, 1,0)) from src LIMIT 1; -- True is returned. SELECT ST_Disjoint(ST_LineString(0,0, 1,1), ST_LineString(1,0, 0,1)) from src LIMIT 1; -- False is returned.
```

##### 3.12.5.4 ST_EnvIntersects

This topic describes the ST_EnvIntersects function and provides examples of using this function.

```
BOOLEAN ST_EnvIntersects(ST_Geometry1, ST_Geometry2)
```

Description: This function is used to determine whether the envelopes of two geometry objects intersect. If the envelopes of two geometry objects intersect, this function returns True. Otherwise, this function returns False.

```
SELECT ST_EnvIntersects(ST_LineString(0,0, 1,1), ST_LineString(1,3, 2,2)) from src LIMIT 1; -- False is returned. SELECT ST_EnvIntersects(ST_LineString(0,0, 2,2), ST_LineString(1,0, 3,2)) from src LIMIT 1; -- True is returned.
```

##### 3.12.5.5 ST_Equals

This topic describes the ST_Equals function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Equals(geometry1, geometry2)
```

Description: If geometry1 equals geometry2, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Equals(st_linestring(0,0, 1,1), st_linestring(1,1, 0,0)) from src LIMIT 1; -- true is returned. SELECT ST_Equals(st_linestring(0,0, 1,1), st_linestring(1,0, 0,1)) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.6 ST_Intersects

This topic describes the ST_Intersects function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Intersects(geometry1, geometry2)
```

Description: If geometry1 and geometry2 intersect, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Intersects(st_linestring(0,0, 1,1), st_linestring(1,1, 0,0)) from src LIMIT 1; -- true is returned. SELECT ST_Intersects(st_linestring(0,0, 1,1), st_linestring(1,0, 0,1)) from src LIMIT 1; -- true is returned. SELECT ST_Intersects(ST_LineString(2,0, 2,3), ST_Polygon(1,1, 4,1, 4,4, 1,4)) from src LIMIT 1; -- true is returned. SELECT ST_Intersects(ST_LineString(8,7, 7,8), ST_Polygon(1,1, 4,1, 4,4, 1,4)) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.7 ST_Overlaps

This topic describes the ST_Overlaps function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Overlaps(geometry1, geometry2)
```

Description: If geometry1 and geometry2 overlap, this function returns true. Otherwise, this function returns false. Overlapping excludes the tangency of the geometries. Example:

```
SELECT ST_Overlaps(st_polygon(2,0, 2,3, 3,0), st_polygon(1,1, 1,4, 4,4, 4,1)) from src LIMIT 1; -- true is returned. SELECT ST_Overlaps(st_polygon(2,0, 2,1, 3,1), ST_Polygon(1,1, 1,4, 4,4, 4,1)) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.8 ST_Relate

This topic describes the ST_Relate function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Relate(geometry1, geometry2)
```

Description: If geometry1 has the specified Dimensionally Extended nine-Intersection Model (DE-9IM) relationship with geometry2, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Relate(st_polygon(2,0, 2,1, 3,1), ST_Polygon(1,1, 1,4, 4,4, 4,1), '****T****') from src LIMIT 1; -- true is returned. SELECT ST_Relate(st_polygon(2,0, 2,1, 3,1), ST_Polygon(1,1, 1,4, 4,4, 4,1), 'T********') from src LIMIT 1; -- false is returned. SELECT ST_Relate(st_linestring(0,0, 3,3), ST_linestring(1,1, 4,4), 'T********') from src LIMIT 1; -- true is returned. SELECT ST_Relate(st_linestring(0,0, 3,3), ST_linestring(1,1, 4,4), '****T****') from src LIMIT 1; -- false is returned.
```

##### 3.12.5.9 ST_Touches

This topic describes the ST_Touches function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Touches(geometry1, geometry2)
```

Description: If geometry1 and geometry2 spatially touch and have no similar interior points, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Touches(st_point(1, 2), st_polygon(1, 1, 1, 4, 4, 4, 4, 1)) from src LIMIT 1; -- true is returned. SELECT ST_Touches(st_point(8, 8), st_polygon(1, 1, 1, 4, 4, 4, 4, 1)) from src LIMIT 1; -- false is returned.
```

##### 3.12.5.10 ST_Within

This topic describes the ST_Within function and provides an example of using this function. Function declaration:

```
BOOLEAN ST_Within(geometry1, geometry2)
```

Description: If geometry1 is within geometry2, this function returns true. Otherwise, this function returns false. Example:

```
SELECT ST_Within(st_point(2, 3), st_polygon(1,1, 1,4, 4,4, 4,1)) from src LIMIT 1; -- true is returned. SELECT ST_Within(st_point(8, 8), st_polygon(1,1, 1,4, 4,4, 4,1)) from src LIMIT 1; -- false is returned.
```

#### 3.12.6 Geohash index functions

##### 3.12.6.1 ST_GeoHash

This topic describes the ST_GeoHash function and provides an example on how to use this function.

```
string ST_GeoHash(st_geometry geometry, integer precision=full_precision) string ST_GeoHash(double longitude, double latitude, integer precision=full_precision)
```

Description: This function returns the unique Geohash string of the specified point. This function uses a function with the ST_ prefix or the specified longitudes and latitudes as input parameters. If the precision is not specified, the maximum precision is used. The precision depends on your business requirements and the characteristics of the data.

```
SELECT ST_GeoHash(ST_Point(-102.849854, 36.451113), 8); SELECT ST_GeoHash(ST_GeomFromText('POINT(-102.849854 36.451113)')); SELECT ST_GeoHash(-102.849854, 36.451113, 10);
```

##### 3.12.6.2 ST_PointFromGeoHash

This topic describes the ST_PointFromGeoHash function and provides an example on how to use this function.

```
st_geometry ST_PointFromGeoHash(string geohash, integer precision=full_precision)
```

Description: This function returns a point based on the input Geohash value. If the precision parameter is not configured, the maximum precision is used. The precision depends on your business requirements and the characteristics of the data.

```
SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq')); SELECT ST_AsText(ST_PointFromGeoHash('9wqz7eep0eyq', 4));
```

##### 3.12.6.3 ST_EnvelopeFromGeoHash

This topic describes the ST_EnvelopeFromGeoHash function and provides an example of using this function.

```
st_geometry ST_EnvelopeFromGeoHash(string geohash, integer precision=full_precision)
```

Description: This function returns the envelope of the specified precision based on the input Geohash value. If the precision parameter is not configured, the maximum precision is used. The precision depends on your business requirements and the characteristics of the data.

```
SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq', 8)); SELECT ST_AsText(ST_EnvelopeFromGeoHash('9wqz7eep0eyq'));
```

##### 3.12.6.4 ST_GeoHashNeighbours

This topic describes the ST_GeoHashNeighbours function and provides an example of using this function. Function declaration:

```
list_of_string ST_GeoHashNeighbours(double longitude, double latitude, integer precision)
```

Description: This function is a user-defined table-valued function (UDTF) that generates nine data records. This function returns nine Geohash strings of the current point and its eight neighboring points based on the input longitude, latitude, and precision. These parameters must be specified. Example:

```
SELECT ST_GeoHashNeighbours(-102.849854, 36.451113, 10);
```

#### 3.12.7 S2 mesh functions

##### 3.12.7.1 ST_S2CellIdsFromGeom

This topic describes the ST_S2CellIdsFromGeom function and provides an example of using this function. Function declaration:

```
list_of_string ST_S2CellIdsFromGeom(st_geometry geometry, integer level)
```

Description: This function overwrites the input geometry by using S2 cells at the specified level. Then, it returns the IDs of all S2 cells. Example:

```
SELECT ST_S2CellIdsFromGeom(ST_Point(-102.849854, 36.451113), 4); SELECT ST_S2CellIdsFromGeom(ST_LineString('LINESTRING(-71.160281 42.258729,-71.160837 42.259113,-71.161144 42.2 5932)'), 17) as cellid;
```

##### 3.12.7.2 ST_S2CellIdsFromText

This topic describes the ST_S2CellIdsFromText function and provides an example of using this function. Function declaration:

```
list_of_string ST_S2CellIdsFromText(string wkt, integer level)
```

Description: This function overwrites the well-known text (WKT) representation of the input geometry by using S2 cells at the specified level. Then, it returns the IDs of all S2 cells. Example:

```
SELECT ST_S2CellIdsFromText(ST_GeomFromText('POINT(-102.849854 36.451113)'), 4); SELECT ST_S2CellIdsFromText('LINESTRING(-71.160281 42.258729,-71.160837 42.259113,-71.161144 42.25932)', 17) as cellid;
```

##### 3.12.7.3 ST_S2CellCenterPoint

This topic describes the ST_S2CellCenterPoint function and provides an example of using this function. Function declaration:

```
st_point ST_S2CellCenterPoint(string cellId)
```

Description: This function calculates the center point of the cell specified by the cellId parameter in the input S2 cell. Example:

```
SELECT ST_S2CellCenterPoint('549015'); SELECT ST_AsText(ST_S2CellCenterPoint('89e37f091'));
```

##### 3.12.7.4 ST_S2CellNeighbours

This topic describes the ST_S2CellNeighbours function and provides an example of using this function. Function declaration:

```
list_of_string ST_S2CellNeighbours(string cellId, integer level)
```

Description: This function calculates the neighboring S2 cells of the cell specified by the cellId parameter at the specified level. Then, it returns the IDs of all neighboring S2 cells. Example:

```
SELECT ST_S2CellNeighbours('549015', 10); SELECT ST_S2CellNeighbours('89e37f091', 16) as neighour;
```

#### 3.12.8 Geodesic functions

##### 3.12.8.1 ST_AreaWGS84

This topic describes the ST_AreaWGS84 function and provides an example of using this function. Function declaration:

```
double ST_AreaWGS84(st_geometry geometry)
```

Description: This function returns the approximate geodesic area of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane area in square meters. Example:

```
SELECT ST_AreaWGS84(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 2967450,743265.625 2967416,743238 2967416))'));
```

##### 3.12.8.2 ST_DistanceWGS84

This topic describes the ST_DistanceWGS84 function and provides an example of using this function. Function declaration:

```
double ST_DistanceWGS84(st_geometry geometry1, st_geometry geometry2)
```

Description: This function returns the approximate geodesic distance of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane distance in meters. Example:

```
SELECT ST_DistanceWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), ST_GeomFromText('LINESTRING(-72.1260 42.45, -72.123 42.1546)'));
```

##### 3.12.8.3 ST_BufferWGS84

This topic describes the ST_BufferWGS84 function and provides an example of using this function. Function declaration:

```
st_geometry ST_BufferWGS84(st_geometry geometry, double radius)
```

Description: This function returns the approximate geodesic buffer of the input geometry based on World Geodetic System 1984 (WGS84). This function converts the coordinates of the input geometry from EPSG:4326 to EPSG:3857. Then, it calculates the plane buffer and converts the coordinates back to EPSG:4326. Example:

```
SELECT ST_AsText(ST_BufferWGS84(ST_GeomFromText('POINT(-72.1235 42.3521)'), 10));
```

##### 3.12.8.4 ST_GeodesicDistance

This topic describes the ST_GeodesicDistance function and provides an example of using this function. Function declaration:

```
double ST_GeodesicDistance(double lon1, double lat1, double lon2, double lat2, string method = VINCENTY) double ST_GeodesicDistance(st_geometry geo1, st_geometry geo2, string method = VINCENTY)
```

Description: This function calculates the geodesic distance between two points by using the specified method. The supported methods are Vincenty, LawOfCosines, and Haversine. The default value of the method parameter is VINCENTY. The return value is in radians. Example:

```
SELECT ST_GeodesicDistance(ST_GeomFromText('POINT(152.352298 -24.875975)'), ST_GeomFromText('POINT(151.960336 - 24.993289)'), 'LawOfCosines');
```

##### 3.12.8.5 ST_Distance_Sphere

This topic describes the ST_Distance_Sphere function and provides an example of using this function.

```
double ST_Distance_Sphere(st_point geo1, st_point2 geo2) double ST_Distance_Sphere(double lng1, double lat1, double lng2, double lat2)
```

Description: This function uses the algorithm provided by AMAP to calculate the approximate geodesic distance between two input points. The distance specified in this function is measured in meters. This function uses ST_Point or the specified longitudes and latitudes as input parameters. Example:

```
SELECT ST_Distance_Sphere(
            ST_GeomFromText('POINT(116.292078 39.919622)'),
            ST_GeomFromText('POINT(116.286676 39.919593)'));
```

Returned result:

```
+------------+
| _c0        |
+------------+
| 460.6965312526471 |
+------------+
```

##### 3.12.8.6 ST_Area_Sphere

This topic describes the ST_Area_Sphere function and provides an example of using this function.

```
double ST_Area_Sphere(st_geometry geo)
```

Description: This function uses the algorithm provided by AMAP to calculate the geodesic area of the input geometry. Unit: square meters. This function uses only ST_Polygon and ST_MultiPolygon as input parameters.

```
SELECT geospatial.ST_Area_Sphere(geospatial.ST_GeomFromText('POLYGON((116.259097 40.202114,116.259024 40.20199,116.258768 40.201662,116.258376 40.201341,116.258031 40.201036,116.257675 40.200734,116.257429 40.200656,116.257357 40.200562,116.257392 40.200051,116.257506 40.199433,116.257569 40.198586,116.257564 40.19756,116.257561 40.197372,116.257552 40.197036,116.257554 40.19675,116.257539 40.196647,116.257502 40.19653,116.257343 40.196389,116.257153 40.196276,116.256733 40.196071,116.25582 40.195646,116.255628 40.195611,116.255468 40.195653,116.255385 40.195742,116.255347 40.195849,116.255258 40.197143,116.255103 40.199576,116.255078 40.200585,116.251227 40.20059,116.251098 40.203978,116.259433 40.204111,116.259247 40.203079,116.259097 40.202114))'));
```

The following result is returned:

```
+------------+
| _c0        |
+------------+
| 353493.765625 |
+------------+
```

#### 3.12.9 R-tree index functions

##### 3.12.9.1 ST_BuildRTreeIndex

This topic describes the ST_BuildRTreeIndex function and provides an example of using this function. Function declaration:

```
RTree ST_BuildRTreeIndex(string uniqueId, string geometryWkt)
```

Description: This function is a user-defined aggregate function (UDAF). It uses the unique ID and well-known text (WKT) string of each geometry as input parameters to create the R-tree index. This function must be used with other R-tree functions. Example:

```
SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index FROM poi_sample;
```

##### 3.12.9.2 ST_ContainsFromRTree

This topic describes the ST_ContainsFromRTree function. Function declaration:

```
ST_ContainsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that are contained by the geometry from the R-tree index. This function is used to accelerate the ST_Contains query.

##### 3.12.9.3 ST_CrossesFromRTree

This topic describes the ST_CrossesFromRTree function. Function declaration:

```
ST_CrossesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that cross the geometry from the R-tree index. This function is used to accelerate the ST_Crosses query.

##### 3.12.9.4 ST_EqualsFromRTree

This topic describes the ST_EqualsFromRTree function. Function declaration:

```
ST_EqualsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that equal the geometry from the R-tree index. This function is used to accelerate the ST_Equals query.

##### 3.12.9.5 ST_IntersectsFromRTree

This topic describes the ST_IntersectsFromRTree function. Function declaration:

```
ST_IntersectsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that intersect with the geometry from the R-tree index. This function is used to accelerate the ST_Intersects query.

##### 3.12.9.6 ST_OverlapsFromRTree

This topic describes the ST_OverlapsFromRTree function. Function declaration:

```
ST_OverlapsFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that overlap with the geometry from the R-tree index. This function is used to accelerate the ST_Overlaps query.

##### 3.12.9.7 ST_TouchesFromRTree

This topic describes the ST_TouchesFromRTree function. Function declaration:

```
ST_TouchesFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that spatially touch the geometry from the R-tree index. This function is used to accelerate the ST_Touches query.

##### 3.12.9.8 ST_WithinFromRTree

This topic describes the ST_WithinFromRTree function and provides an example of using this function. Function declaration:

```
ST_WithinFromRTree(string uniqueId, string geometryWkt, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of objects that include the geometry from the R-tree index. This function is used to accelerate the ST_Within query. Example: Query the intersections of line segments in the A table and polygons in the B table.

```
set odps.sql.allow.cartesian=true; SELECT a.id as link_id, b.id as shape_id FROM link_sample_wkt a, poi_sample_wkt b WHERE geospatial.ST_IsValid(b.shape) AND geospatial.ST_Intersects(
        geospatial.ST_LineString(a.line),
        geospatial.ST_Multipolygon(b.shape));
```

Returned result:

```
Summary: resource cost: cpu 3.28 Core * Min, memory 5.76 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
  meta_dev.link_sample_wkt: 1000 (105940 bytes)
outputs: Job run time: 111.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

After optimization by using the new function:

```
SELECT /*+mapjoin(i)*/
      geospatial.ST_IntersectsFromRTree(id, line, i.index)
      AS (link_id, shape_id)
FROM link_sample_wkt
```

`(`

```
      SELECT geospatial.ST_BuildRTreeIndex(id, shape) AS index
      FROM poi_sample_wkt
      WHERE geospatial.ST_IsValid(shape)
) i;
```

Returned result:

```
Summary: resource cost: cpu 1.03 Core * Min, memory 1.99 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
  meta_dev.link_sample_wkt: 1000 (105940 bytes)
outputs: Job run time: 41.000 +---------+----------+
| link_id | shape_id |
+---------+----------+
| 5121371185457659960 | B000A844XK |
| 5121377123249946651 | B000A85TV4 |
| 5121377166199619654 | B000A844KT |
+---------+----------+
```

##### 3.12.9.9 ST_KNNFromRTree

This topic describes the ST_KNNFromRTree function and provides an example of using this function. Function declaration:

```
ST_KNNFromRTree(string uniqueId, string geometryWkt, int k, RTree rtree)
```

Description: This function is a user-defined table-valued function (UDTF). It uses the unique ID and well-known text (WKT) string of each geometry and the R-tree index that is created by calling ST_BuildRTreeIndex as input parameters. This function returns the IDs of k objects that are near to the geometry from the R-tree index. Example: Create an R-tree for all points in a table and use the KNN function to find the nearest point of each point.

```
SELECT /*+mapjoin(i)*/
    geospatial.ST_KNNFromRTree(id, point, 1, i.index) AS (id1, id2)
FROM poi_sample_wkt
```

`(`

```
    SELECT geospatial.ST_BuildRTreeIndex(id, point) AS index
    FROM poi_sample_wkt
) i;
```

Returned result:

```
Summary: resource cost: cpu 1.17 Core * Min, memory 2.24 GB * Min inputs:
  meta_dev.poi_sample_wkt: 1000 (237592 bytes)
outputs: Job run time: 46.000 +-----+-----+
| id1 | id2 |
+-----+-----+
| B000A01B4E | B000A01B4E |
| B000A01C19 | B000A01C19 |
| B000A023A5 | B000A023A5 |
| B000A02F81 | B000A02F81 |
| B000A07BEE | B000A07BEE |
| B000A07E06 | B000A07E06 |
| B000A08863 | B000A08863 |
... -- The table has 1,000 rows of data. This function returns 1,000 rows of data, which meets your expectations.
```

#### 3.12.10 Other functions

##### 3.12.10.1 ST_IsValid

This topic describes the ST_IsValid function and provides an example of using this function. Function declaration:

```
boolean ST_IsValid(st_geometry geometry) boolean ST_IsValid(string wkt)
```

Description: This function checks whether the input geometry or well-known text (WKT) string meets the requirements. Example:

```
SELECT ST_IsValid('POINT(-102.849854 36.451113)'); SELECT ST_IsValid(ST_Point('POINT(-102.849854 36.451113)'));
```

##### 3.12.10.2 ST_Transform

This topic describes the ST_Transform function and provides an example of using this function. Function declaration:

```
st_geometry ST_TransformWGS84(st_geometry geometry) st_geometry ST_Transform(st_geometry geometry, integer toSRID) st_geometry ST_Transform(st_geometry geometry, integer fromSRID, integer toSRID)
```

Description: This function converts the coordinates of the input geometry from one spatial reference system to another. The ST_TransformWGS84 function converts the coordinates of the geometry from EPSG:4326 to EPSG:3857. The ST_Transform function converts the geometry from fromSRID to toSRID. If the overload function contains only toSRID, you must call the ST_SetSRID function first. Example:

```
SELECT ST_AsText(ST_Transform(ST_GeomFromText('POLYGON((743238 2967416,743238 2967450, 743265 2967450,743265.625 2967416,743238 2967416))', 2249, 4326))); SELECT ST_AsText(ST_TransformWGS84(ST_GeomFromText('POLYGON((-71.1776848522251 42.3902896512902,- 71.1776843766326 42.3903829478009, -71.1775844305465 42.3903826677917,-71.1775825927231 42.3902893647987,- 71.1776848522251 42.3902896512902))')));
```

### 3.13 MaxCompute Hash Clustering

#### 3.13.1 Background information

This topic describes the background of MaxCompute Hash Clustering. JOIN operations are commonly used for queries in MaxCompute. MaxCompute provides the following methods to implement JOIN operations: Broadcast hash join: This method is used when a JOIN operation involves a small table. The small table is broadcasted and transferred to all instances in a join task. Then, the hash join operation is performed to join the small table with a large table. Shuffle hash join: This method is used when a JOIN operation involves large tables that cannot be directly broadcasted. In this case, the hash shuffle operation is performed on two tables based on join keys. The hash results for the same key-value pairs are the same. This ensures that results that have the same key are collected to the same instance of a join task. For each instance, a hash table is created by using a small table, probe operations are performed by using a large table, and then the tables are joined. Sort merge join: This method is used when a JOIN operation involves larger tables and the preceding methods cannot be used because the memory is insufficient to create a hash table. In this case, the hash shuffle operation is performed on two tables based on join keys, the obtained values are sorted by using join keys, and then the sorted values are merged. The following figure shows the process. The sort merge join method is commonly used in MaxCompute because MaxCompute processes large amounts of data in most cases. If you use this method, shuffle and join operations are repeatedly performed. The physical execution plan of Job Scheduler of a JOIN operation requires multiple stages, which consumes excessive amounts of resources. To resolve this issue, MaxCompute allows you to configure the hash shuffle and sort attributes when the data is initially generated in a table. This prevents data from being repeatedly shuffled and sorted in subsequent queries. The number of stages in the physical execution plan of Job Scheduler of a JOIN operation is also reduced. The preceding figure shows that only one stage is required. MaxCompute Hash Clustering allows you to configure the shuffle and sort attributes of a table when you create the table. Then, MaxCompute optimizes the execution plan, improves the efficiency, and saves resources based on the existing storage characteristics.

#### 3.13.2 Descriptions

##### 3.13.2.1 Enable Hash Clustering

This topic describes how to enable the Hash Clustering feature of MaxCompute. The Hash Clustering feature has been launched. By default, this feature is enabled. If you want to use clustered indexes, add the following flag:

```
set odps.sql.cfile2.enable.read.write.index.flag=true;
```

After the flag is set to true, the system automatically creates indexes for the sorted hash buckets to improve query efficiency. To use clustered indexes, you must add this flag during table creation and subsequent queries. If you want to use clustered indexes in your project at all times, contact the MaxCompute team. Clustered indexes improve the efficiency of queries (equivalent values or ranges) based on sort keys. You can experience the superior performance provided by Hash Clustering even if you do not add this flag.

##### 3.13.2.2 Create a hash-clustered table

This topic describes how to create a hash-clustered table. You can use the following statement to create a hash-clustered table. You must specify cluster keys or hash keys and the number of hash buckets. The sort operation is optional. However, we recommend that you use the same parameter values as the cluster keys to achieve optimal performance.

```
CREATE TABLE [IF NOT EXISTS] table_name [(col_name data_type [comment col_comment], ...)] [comment table_comment] [PARTITIONED BY (col_name data_type [comment col_comment], ...)] [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_name [ASC | DESC] ...])] IN TO number_of_buckets BUCKETS] [AS select_statement]
```

You can use the following statement to create a standard table:

```
CREATE TABLE T1 (a string, b string, c bigint) CLUSTERED BY (c) SORTED by (c) INTO 1024 BUCKETS;
```

You can use the following statement to create a partitioned table:

```
CREATE TABLE T1 (a string, b string, c bigint) PARTITIONED BY (dt string) CLUSTERED BY (c) SORTED by (c) INTO 1 024 BUCKETS;
```

The following sections detail the CLUSTERED BY, SORTED BY, and INTO number_of_buckets BUCKETS clauses.

**CLUSTERED BY**

The CLUSTERED BY clause specifies hash keys. MaxCompute performs the hash operation on the specified column and distributes data to buckets based on the hash values. To prevent data skew and hot spots, and to concurrently execute statements, we recommend that you specify a column that has large value ranges and a small number of duplicate key-value pairs in CLUSTERED BY. In addition, to optimize the JOIN operation, we recommend that you select commonly used join or aggregation keys. The join and aggregation keys are similar to the primary keys in conventional databases.

**SORTED BY**

The SORTED BY clause specifies how fields are sorted in a bucket. We recommend that you specify the same column in SORTED BY as that in CLUSTERED BY to improve execution efficiency. After you specify the column in SORTED BY, MaxCompute automatically generates indexes and then executes SQL statements faster when you query data based on these indexes.

**INTO number_of_buckets BUCKETS**

The INTO number_of_buckets BUCKETS clause specifies the number of hash buckets, which is required. The number of hash buckets is determined by the volume of data. More buckets indicate higher concurrency, which shortens the job running time. However, if a large number of buckets exist, excessive small files may be generated. In addition, high concurrency increases CPU time. We recommend that you set the data size of each bucket to a value that ranges from 500 MB to 1 GB. If a large table is used, you can adjust the value to a larger value based on your business requirements. You can remove the shuffle operation only for tables with the same number of buckets in MaxCompute. The maximum number of buckets is 4,096. If the number of buckets exceeds the value, the performance and resource usage may be affected. If you want to remove the shuffle and sort operations during a JOIN operation on two tables, the numbers of hash buckets in the tables must be the same. If the numbers that are calculated based on the aforementioned method are inconsistent, we recommend that you use the larger number for the JOIN operation. This ensures that SQL statements can be concurrently executed in an efficient manner. If the size of the large table is much larger than the size of the small table, you can set the number of buckets for the large table to a value that is several times the number of buckets for the small table. For example, you can set the number of buckets for the large table to 1,024 and set the number of buckets for the small table to 256. If automatic hash bucket split and merging are supported, you can perform the JOIN operation based on the data characteristics of MaxCompute.

##### 3.13.2.3 Modify table attributes

This topic describes how to modify the attributes of a hash-clustered table. For a partitioned table, MaxCompute allows you to execute the ALTER TABLE statement to add the Hash Clustering attribute to a table or remove the Hash Clustering attribute from a table.

```
ALTER TABLE table_name
 [CLUSTERED BY (col_name [, col_name, ...]) [SORTED BY (col_name [ASC | DESC] [, col_name [ASC | DESC] ...])] I
NTO number_of_buckets BUCKETS] ALTER TABLE table_name NOT CLUSTERED;
```

When you use the ALTER TABLE statement, take note of the following points: The ALTER TABLE statement can modify only the Hash Clustering attribute of a partitioned table. The Hash Clustering attribute cannot be modified after it is added to a non-partitioned table. The ALTER TABLE statement takes effect only on the new partitions of a table, which include the partitions generated by using the INSERT OVERWRITE statement. New partitions are stored based on the Hash Clustering attribute. The storage formats of existing partitions remain unchanged. The ALTER TABLE statement takes effect only on the new partitions of a table. Therefore, you cannot specify a partition in this statement. The ALTER TABLE statement is suitable for existing tables. After the Hash Clustering attribute is added, new partitions are stored based on the Hash Clustering attribute.

##### 3.13.2.4 View and verify table attributes

This topic describes how to view and verify attributes of a hash-clustered table. After you create a hash-clustered table, execute the following statement to view table attributes:

```
DESC EXTENDED table_name;
```

The table attributes are displayed in Extended Info. You can also execute the following statement to view partition attributes of a partitioned table:

```
DESC EXTENDED table_name partition(pt_spec);
```

The following figure shows the execution result.

#### 3.13.3 Benefits

##### 3.13.3.1 Bucket pruning and index optimization

This topic describes bucket pruning and index optimization. The following code provides a syntax sample:

```
CREATE TABLE t1 (id bigint, a string, b string) CLUSTERED BY (id) SORTED BY (id) into 1000 BUCKETS; ... SELECT t1.a, t1.b, t1.c FROM t1 WHERE t1.id=12345;
```

This syntax indicates a full scan for a standard table. A full scan for a large table consumes a large number of resources. However, if the hash shuffle operation is performed on all **id** fields and the **id** fields are sorted, the query is greatly simplified. Sample procedure:
1. Find the hash bucket that corresponds to **12345**. This query is performed in only one bucket, not all 1,000 buckets.
This process is called **bucket pruning**.
2. Data in a bucket is stored based on IDs. MaxCompute automatically creates indexes and uses the INDEX LOOKUP
function to locate relevant records. The simplified procedure not only greatly reduces the number of mappers, but also allows mappers to locate the page where the data is stored by using the INDEX function. Therefore, the volume of loaded data is greatly reduced.

##### 3.13.3.2 Aggregation optimization

This topic describes aggregation optimization. The following code provides an example:

```
SELECT department, SUM(salary) FROM employee GROUP BY (department);
```

In most cases, the department column is shuffled and sorted. Then, a stream aggregate operation is performed to collect statistics on the department groups. However, if `CLUSTERED BY (department) SORTED BY (department)` is executed for the table data, the shuffle and sort operations are no longer required.

##### 3.13.3.3 Storage optimization

This topic describes storage optimization. In addition to computation optimization, storage space is greatly saved if tables are shuffled and stored in a sorted manner. MaxCompute uses column store at the underlying layer. Records that have the same or similar key-value pairs are stored together by the sort function, which facilitates encoding and compression. This way, compression efficiency is improved. In some extreme cases, a sorted table can save 50% more storage space than an unsorted table. Therefore, Hash Clustering is suitable for storing tables that have long lifecycles. The following figure shows a sample table with 100 GB of TPC-H line items and multiple data types, such as INT, DOUBLE, and STRING. If Hash Clustering is used, about 10% of the storage space is saved when the volume of data and compression format remain unchanged.

#### 3.13.4 ShuffleRemove

This topic describes the operations that are related to ShuffleRemove. Range-clustered tables support the join and aggregate operations. If a join key or group key is a range-clustered key or its prefix, data redistribution is not required. This mechanism is called ShuffleRemove, which improves execution efficiency. Usage: The `odps.optimizer.enable.range.partial.repartitioning` flag specifies whether to enable this feature. By default, this feature is disabled. If the two hash-clustered tables you want to join have different numbers of buckets but the numbers are multiples of each other, data redistribution is not required. This improves execution efficiency. Usage: The `odps.optimizer.enable.hash.partial.repartitioning` flag specifies whether to enable this feature. By default, this feature is enabled. Correlated Shuffle Remove is supported. If data meets distribution requirements but does not meet the sorting requirements, you can add a sort operator to avoid data redistribution.

#### 3.13.5 Limits

This topic describes limits on MaxCompute Hash Clustering. Limits: The INSERT INTO statement is not supported. You can only execute the INSERT OVERWRITE statement to add data. Small files cannot be merged. Most data is evenly distributed in buckets when it is split. Therefore, the number of small files is not large. If you merge files, the data distribution is affected. However, you can still use the merge and archive commands to change the storage format of a table file and the format of a RAID file. You cannot use Tunnel to upload data to a range-clustered table because the data uploaded by using Tunnel is unsorted.

### 3.14 Common MaxCompute SQL parameter settings

**settings**

#### 3.14.1 Map configurations

This topic describes Map configurations.

```
set odps.sql.mapper.cpu=100;
```

Description: specifies the number of CPUs used by each instance in a Map task. Default value: 100. Valid values: [50,800].

```
set odps.sql.mapper.memory=1024;
```

Description: specifies the memory size of each instance in a Map task. Unit: MB. Default value: 1024. Valid values: [256,12288].

```
set odps.sql.mapper.merge.limit.size=64;
```

Description: specifies the maximum size of control files to be merged. Unit: MB. Default value: 64. Valid values: [0,Integer.MAX_VALUE]. You can configure this variable to control the input of mappers.

```
set odps.sql.mapper.split.size=256;
```

Description: specifies the maximum data input volume for a Map task. Unit: MB. Default value: 256. Valid values: [1,Integer.MAX_VALUE]. You can configure this variable to control the input of mappers.

#### 3.14.2 Join configurations

This topic describes Join configurations.

```
set odps.sql.joiner.instances=-1;
```

Description: specifies the number of instances of a join task. Default value: -1. Valid values: [0,2000].

```
set odps.sql.joiner.cpu=100;
```

Description: specifies the number of CPUs used by each instance of a join task. Default value: 100. Valid values: [50,800].

```
set odps.sql.joiner.memory=1024;
```

Description: specifies the memory size of each instance of a join task. Unit: MB. Default value: 1024. Valid values: [256,12288].

#### 3.14.3 Reduce configurations

This topic describes Reduce configurations.

```
set odps.sql.reducer.instances=-1;
```

Description: specifies the number of instances in a Reduce task. Default value: -1. Valid values: [0,2000].

```
set odps.sql.reducer.cpu=100;
```

Description: specifies the number of CPUs used by each instance in a Reduce task. Default value: 100. Valid values: [50,800].

```
set odps.sql.reducer.memory=1024;
```

Description: specifies the memory size of each instance in a Reduce task. Unit: MB. Default value: 1024. Valid values: [256,12288].

#### 3.14.4 UDF configurations

This topic describes the configurations of user-defined functions (UDFs).

```
set odps.sql.udf.jvm.memory=1024;
```

Description: specifies the maximum memory size used by the UDF JVM heap. Unit: MB. Default value: 1024. Valid values: [256,12288].

```
set odps.sql.udf.timeout=600;
```

Description: specifies the timeout period of a UDF. Unit: seconds. Default value: 600. Valid values: [0,3600].

```
set odps.sql.udf.python.memory=256;
```

Description: specifies the maximum memory size used by the UDF Python API. Unit: MB. Default value: 256. Valid values: [64,3072].

```
set odps.sql.udf.optimize.reuse=true/false;
```

Description: When this parameter is set to true, each UDF function expression can be calculated only once. This improves performance. Default value: true.

```
set odps.sql.udf.strict.mode=false/true;
```

Description: specifies whether functions return NULL or an error if dirty data is found. If the parameter is set to true, an error is returned. Otherwise, NULL is returned.

#### 3.14.5 MapJoin configurations

This topic describes MapJoin configurations.

```
set odps.sql.mapjoin.memory.max=512;
```

Description: specifies the maximum memory size for a small table that is involved in a MapJoin operation. Unit: MB. Default value: 512.

```
set odps.sql.reshuffle.dynamicpt=true/false;
```

Description: Dynamic partitioning is time-consuming in some scenarios. Disabling dynamic partitioning can accelerate SQL. If the number of dynamic partitions is small, disabling dynamic partitioning can prevent data skew.

#### 3.14.6 Configurations of data skew

This topic describes configurations of data skew.

```
set odps.sql.groupby.skewindata=true/false;
```

Description: allows you to enable GROUP BY optimization.

```
set odps.sql.skewjoin=true/false;;
```

Description: allows you to enable JOIN optimization. This is effective only when **odps.sql.skewinfo** is specified.

```
set odps.sql.skewinfo;
```

Description: allows you to configure detailed information for JOIN optimization. Command syntax:

```
set odps.sql.skewinfo=skewed_src:(skewed_key)[("skewed_value")]
```

Example: Configure a single skewed value for a single field.

```
set odps.sql.skewinfo=src_skewjoin1:(key)[("0")]; -- Output result: explain select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src_skewjoin1 b on a.key = b.key;
```

Configure multiple skewed values for a single field.

```
set odps.sql.skewinfo=src_skewjoin1:(key)[("0")("1")]; -- Output result: explain select a.key c1, a.value c2, b.key c3, b.value c4 from src a join src_skewjoin1 b on a.key = b.key;
```

### 3.15 MapReduce-to-SQL conversion for execution

**execution**

#### 3.15.1 Overview

This topic provides an overview of the MapReduce-to-SQL conversion for execution feature. MaxCompute provides a series of Java APIs for MapReduce to process data. MapReduce programs are automatically converted to SQL for execution. After the conversion, you can use the compiler, cost-based optimizer, and vectorized execution engine released with MaxCompute V2.0 to process the MapReduce programs. The new features of the SQL engine can also be used. The features, performance, and stability of the SQL engine are optimized. You do not need to change the original APIs and job logic. Only MapReduce jobs of the OpenMR type, which are written by using MapReduce APIs, can be converted to SQL. This feature can be used only for projects and jobs. This feature supports views as the input. This feature supports external tables as the input. This feature supports TemporaryFile reads and writes. This feature allows you to read data from and write data to hash-clustered tables. This feature supports near-real-time execution of small jobs.

#### 3.15.2 Configure the MaxCompute client

This topic describes how to configure the MaxCompute client when you use the MapReduce-to-SQL conversion feature.
1. Download the latest version of the MaxCompute client package to your on-premises machine and configure the
MaxCompute client. On the download page, you can obtain the MaxCompute client package of the required version in the **Other**
**Resources** section.
2. Configure the execution mode.
You can configure the execution mode based on your business requirements. The default execution mode is lot. In lot mode, jobs are run by MapReduce. The new compiler, optimizer, and execution engine are not used. You can enable the execution mode by setting the **odps.mr.run.mode** parameter. Valid values: **lot**, **sql**, and
**hybrid**.
Method 1: Enable the execution mode at the project level. In this case, the configuration takes effect on all jobs in the project. Therefore, only the project administrator can apply to enable the execution mode. Set the
**odps.mr.run.mode** parameter to **hybrid** or **sql**. If SQL execution fails in **hybrid** mode, the job is run by
MapReduce. If SQL execution fails in **sql** mode, an error is reported. Method 2: Enable the execution mode at the session level. This method applies only to the current job. To enable the execution mode, use one of the following methods: Add a set flag, such as set odps.mr.run.mode=hybrid; before JAR statements. Configure job parameters. Example:

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

MaxCompute O&M personnel can enable the execution mode at the project level at a later point in time.

#### 3.15.3 Configure running settings in DataWorks

This topic describes how to configure running settings in DataWorks. Jobs that run in DataWorks are updated by the O&M personnel of MaxCompute and DataWorks. You do not need to update your client. Enable the conversion for a single job. You can add a set flag before the statement of a MapReduce job or configure job parameters for the set flag. These methods take effect at the session level and apply only to the current job. The following examples show how to use these methods: Add a set flag, such as set odps.mr.run.mode=hybrid; before JAR statements. Configure job parameters. Example:

```
JobConf job = new JobConf(); job.set("odps.mr.run.mode","hybrid")
```

Enable the conversion at the project level by setting **odps.mr.run.mode** for a project.

#### 3.15.4 View details

This topic describes how to view MapReduce-to-SQL conversion results and running details of SQL jobs. You can use Logview and MaxCompute Studio to view MapReduce-to-SQL conversion results and running details of SQL jobs. Logview XML Open Logview and click the LOT node in the center of the page. The SQL jobs that are converted from MapReduce jobs are included in the XML information about the node. Example:

```
create temporary function mr2sql_mapper_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotMapperUDTF' using ; create temporary function mr2sql_reducer_152955927079392291755 as 'com.aliyun.odps.mapred.bridge.LotReducerUDTF' using ;
 @sub_query_mapper :=
k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku_stock,v_sku_code,v_sku_i e,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_image_version,v_currency_code FROM( mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stoc ku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code ) as (k_id,v _gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku_stock,v_sku_code,v_sku_image,v livery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_image_version,v_currency_code) FROM ae_antispam.product_sku_tt_inc WHERE ds = "20180615" AND hh = "21" mr2sql_mapper_152955927079392291755(id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stoc ku_code,sku_image,delivery_time,sku_bulk_order,sku_bulk_discount,sku_image_version,currency_code ) as (k_id,v _gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku_price,v_sku_stock,v_sku_code,v_sku_image,v livery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_image_version,v_currency_code) FROM ae_antispam.product_sku ) open_mr_alias1
 DISTRIBUTE BY k_id SORT BY k_id ASC;
@sub_query_reducer := mr2sql_reducer_152955927079392291755(k_id,v_gmt_create,v_gmt_modified,v_product_id,v_admin_seq,v_sku_attr,v_sku ice,v_sku_stock,v_sku_code,v_sku_image,v_delivery_time,v_sku_bulk_order,v_sku_bulk_discount,v_sku_image_version currency_code) as (id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code,sku_image,delivery_time, _bulk_order,sku_bulk_discount,sku_image_version,currency_code) FROM @sub_query_mapper; FROM @sub_query_reducer INSERT OVERWRITE TABLE ae_antispam.product_sku id,gmt_create,gmt_modified,product_id,admin_seq,sku_attr,sku_price,sku_stock,sku_code,sku_image,delivery_time,s bulk_order,sku_bulk_discount,sku_image_version,currency_code ;
```

Logview details or summary A new execution engine is used to run jobs.

```
Job run mode: fuxi job Job run engine: execution engine
```

Logview details or JSON summary The JSON summary information in MapReduce contains only the input and output information about Map and Reduce. However, the JSON summary information in SQL allows you to view details about each stage of SQL execution, such as all execution parameters, logical execution plans, physical execution plans, and execution details. Example:

```json
 "midlots" :
```

`[`

```
 "LogicalTableSink(table=
[[odps_flighting.flt_20180621104445_step1_ad_quality_tech_qp_algo_antifake_wordbag_filter_bag_change_result_lv2 , auctionid,word,match_word(3) {0, 1, 2}]]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$0], word=[$1], match_word=[$2]) OdpsLogicalProject(auctionid=[$2], word=[$3], match_word=[$4]) OdpsLogicalTableFunctionScan(invocation=[[MR2SQL_MAPPER_152955294118813063732($0, $1)]()], rowType=[RecordTyp e(VARCHAR(2147483647) item_id, VARCHAR(2147483647) text, VARCHAR(2147483647) __tf_0_0, VARCHAR(2147483647) __ tf_0_1, VARCHAR(2147483647) __tf_0_2)]) OdpsLogicalTableScan(table=[[ad_quality_tech.qp_algo_antifake_wordbag_filter_bag_change_lv2_20, item_id,text(2) {0, 1}]])
```

`]`

#### 3.15.5 Perform operations on the distributed file system

This topic describes how to perform operations on the distributed file system.

**Procedure**

1. Specify volume files.
You can use one of the following methods to specify volume files: Use a utility class to specify the input and output files:

```
com.aliyun.odps.mapred.utils.InputUtils.addVolume( new VolumeInfo([project,]inVolume,inPartition, "inLabel "), new JobConf()); com.aliyun.odps.mapred.utils.OutputUtils.addVolume( new VolumeInfo([project,]outVolume, outPartition, "out Label"), new JobConf());
```

In the preceding commands, **project** and **label** are optional, and the current project and default label are used by default. If multiple input and output files are used, labels are used to distinguish the files from each other. Authorization is required before you access the volume files of other projects. Configure parameters to specify the volume and partition of the input and output files. If multiple input or output files are used, separate the parameters with commas (,).

```
set odps.sql.volume.input[/output].desc = [<project>.]<table>.<partition>[:<label>];
```

2. Call the following method by using a **context** object in the map and reduce steps to write data to the distributed file
system or write data stream input and output files:

```
context.getOutputVolumeFileSystem();
```

### 3.16 Analysis of the mapping between SQL input and output fields

**input and output fields**

#### 3.16.1 Overview

This topic describes the feature of analyzing the mapping between fields in input and output tables. Example:

```
select key, sum(value) as total from src group by key;
```

The result that is shown in the following figure is returned. Two columns are returned: **key** and **total**. The **key** column corresponds to the **src.key** column of the input table. The
**total** column corresponds to the **src.value** column of the input table.

#### 3.16.2 Usage notes

This topic provides an example on how to use the feature of analyzing the mapping between fields in input and output tables.

**Output format**

Field mapping analysis supports human-readable and JSON formats. You can use the `set` `odps.sql.select.output.format=HumanReadable/json` flag to specify the output format.

**SDK-based field mapping analysis**

```java
Odps odps = initOdps(); // To perform analysis, use LineageTask. LineageTask task = new LineageTask("task_name", "select * from dual;"); // Optional. Use the preceding flag to specify the output format. Map<String, String> settings = new LinkedHashMap<>(); settings.putIfAbsent("odps.sql.select.output.format", "json"); task.setProperty("settings", JSON.toJSONString(settings)); // Submit code to the server for field mapping analysis. Instance instance = odps.instances().create(task); System.out.println(instance.getId()); String logView = odps.logview().generateLogView(instance, 72); System.out.println(logView); instance.waitForSuccess(); // Obtain the analysis result. System.out.println(instance.getTaskResults().get("task_name"));
```

**odpscmd-based field mapping analysis**

CLI mode: Use the **-X** parameter for field mapping analysis.

```
./bin/odpscmd.bat -X D:\lineage.q
```

Interactive mode: After you enter the interactive mode of odpscmd, you can use the preceding flag to specify the output format. The usage method is similar to that used to submit SQL jobs.

```
lineage_test>set odps.sql.task.mode=LINEAGE; -- OK is returned. Continue to run the following command: odps@ lineage_test>set odps.sql.select.output.format=Humanreadable; -- OK is returned. Continue to run the following command: lineage_test>select * from dual;
```

Returned result:

```
== Column Lineage Column : id Source Columns :
  test2.dual.id
```

### 3.17 Common MaxCompute SQL errors and solutions

**solutions**

#### 3.17.1 Data skew

##### 3.17.1.1 Overview

This topic provides an overview of data skew issues. In most cases, data skew occurs if the min, max, and avg values of the instance time, input records, and output records parameters are unbalanced in an instance on which jobs run. For example, if the max value is significantly larger than the avg value, data skew may occur. You can use Logview to identify data skew issues, as shown in the following figure. The **Long Tails** tab of each task displays the instances on which data skew occurs. The root cause of data skew is that the amount of data processed by a specific instance far exceeds that processed by other instances. As a result, the running time of this instance is also much longer than the average running time of other instances, and the entire job slows down. Different types of data skew issues in SQL are resolved by using different methods. The subsequent topics describe possible causes of data skew issues and provide solutions.

##### 3.17.1.2 GROUP BY data skew

This topic describes possible causes of the GROUP BY data skew and provides a solution. Possible cause: GROUP BY keys are unevenly distributed, which results in data skew on reducers. Solution: Set the anti-skew parameter before you execute SQL statements.

```
set odps.sql.groupby.skewindata=true;
```

If you set this parameter to true, when the Shuffle hash algorithm is used, the system automatically adds a random factor and introduces a new task to prevent data skew.

##### 3.17.1.3 DISTRIBUTE BY data skew

This topic describes possible causes of the DISTRIBUTE BY data skew and provides a solution. Possible cause: Constants are used to execute the DISTRIBUTE BY clause for full sorting of the entire table. This results in data skew on reducers. Solution: The DISTRIBUTE BY clause determines how to distribute the output values of the map stages to reducers. To prevent duplicate output values from being distributed to different reducers or to process the same group of data together, use the DISTRIBUTE BY clause. This ensures that the same group of data is distributed to the same reducer. Specify the alias of an output column of a SELECT statement. If you execute a SELECT statement to query data of a column and the alias of this column is not specified, the column name is used as the alias. Examples:

```
-- Query the values of the region column from the sale_detail table and perform hash partitioning on data based on the values of the region column. SELECT region from sale_detail distribute by region;
```

To prevent data skew and hot spots, you must specify a column that has large value ranges in the DISTRIBUTE BY clause.

##### 3.17.1.4 Data skew caused by JOIN operations

This topic describes the data skew caused by JOIN operations and provides a solution. Possible cause: JOIN ON keys are unevenly distributed. For example, a key has a large number of duplicates in multiple tables that you want to join. This results in a Cartesian explosion of data in the instance on which the JOIN statement is executed and causes data skew. Solution: You can use one of the following methods to resolve the data skew issue based on scenarios: If one of the tables that you want to join is a small table, execute the MAP JOIN statement, instead of the JOIN statement. Use separate logic to handle skewed keys. For example, if data skew occurs because a large number of null key values exist in both tables, you must filter out these null key values or use a CASE WHEN expression to replace the null key values with random values before you perform a JOIN operation. If you do not want to change the SQL statement, configure the following parameters to enable automatic optimization on MaxCompute:

```
set odps.sql.skewinfo=tab1:(col1,col2)[(v1,v2),(v3,v4),...]; set odps.sql.skewjoin=true;
```

##### 3.17.1.5 Data skew caused by multiple DISTINCT operations

This topic describes the data skew caused by multiple DISTINCT operations and provides a solution. Possible cause: Multiple DISTINCT operations aggravate the GROUP BY skew. Solution: Execute two GROUP BY clauses to alleviate the data skew issue. In most cases, do not use multiple DISTINCT operations at the same time.

##### 3.17.1.6 Data skew caused by misuse of dynamic partitions

This topic describes the data skew caused by misuse of dynamic partitions and provides a solution. Possible cause: In scenarios where dynamic partitions are used, if K Map instances and N destination partitions are deployed, K × N small files may be generated. This significantly increases the management workload of the file system. Therefore, the following configuration takes effect by default:

```
set odps.sql.reshuffle.dynamicpt=true;
```

An additional level of Reduce task is introduced. The same or a small number of other Reduce instances are used to write data to the same destination partition. This prevents a large number of small files from being generated. However, dynamic partition shuffle may cause data skew. Solution: If the number of destination partitions is small, only an appropriate number of small files are generated. In this case, you can run the following command to set odps.sql.reshuffle.dynamicpt to false to prevent the data skew caused by dynamic partition shuffle.

```
set odps.sql.reshuffle.dynamicpt=false;
```

If the number of destination partitions is large, we recommend that you do not use dynamic partitions because a large number of small files are generated.

##### 3.17.1.7 Use SKEWJOIN HINT to avoid skewed hot key values

This topic describes how to avoid skewed hot key values by using SKEWJOIN HINT. This topic also provides examples for reference.

**Methods**

Method 1: Specify the name of a table in SKEWJOIN HINT. Note that the name specified in the hint is the alias of the table. Sample statement:

```
select /*+ skewjoin(a) */ * from T0 a join T1 b on a.c0 = b.c0 and a.c1 = b.c1;
```

Method 2: Specify the table name and possibly skewed columns in SKEWJOIN HINT. In the following statement, the
**c0** and **c1** columns of Table a are skewed columns.

```
select /*+ skewjoin(a(c0, c1)) */ * from T0 a join T1 b on a.c0 = b.c0 and a.c1 = b.c1 and a.c2 = b.c2;
```

Method 3: Specify the table name, columns, and skewed hot key values in SKEWJOIN HINT. If the skewed key values are of the STRING type, enclose each value with double quotation marks ("). In the following statement, **(a.c0=1**
**and a.c1="2")** and **(a.c0=3 and a.c1="4")** contain skewed hot key values.

```
select /*+ skewjoin(a(c0, c1)((1, "2"), (3, "4"))) */ * from T0 a join T1 b on a.c0 = b.c0 and a.c1 = b.c1 an d a.c2 = b.c2;
```

Differences Method 3 in which the **skewvalue** parameter is specified is more efficient than Method 1 and Method 2 in which the skewvalue parameter is not specified. If you use Analyze and Freeride to collect TopK skewed hot key values, SKEWJOIN may automatically take effect without requiring you to specify a hint.
1. Identify the JOIN statement that causes data skew.
In the following screenshot captured on LogView, J5_3_4 is the Fuxi task that took the longest time to run. Click the J5_3_4 task and query the instances of this task on the tab that appears. The query results show that the
**J5_3_4#215_0** instance takes the longest time to run and its I/O records and I/O bytes are much more than those of
other instances. This indicates that data skew occurs on the J5_3_4#215_0 instance. However, the JOIN statement that causes the data skew needs to be further determined. You can open the stdout of the skewed instance and the stdout of a nonskewed instance. The stdout of the skewed instance is enclosed in the yellow rectangle in the preceding figure. The Stdout dialog box shown in the following figure appears. In most cases, the web page cannot display all the content of stdout. To view all the content, you can click **Download** in this dialog box. The following figures show that the value of **record count** in StreamLineRead7 of the skewed instance is much greater than that of the non-skewed instance. Therefore, data skew occurs when data in StreamLineWrite7 and SreamLineRead7 is shuffled. Figure 1. Skewed instance Figure 2. Non-skewed instance On the directed acyclic graph (DAG), you can right-click the skewed instance and select **expand all** to find StreamLineWrite7 and StreamLineRead7. The DAG shows that data skew occurs on StreamLineRead7 in MergeJoin2. MergeJoin2 is generated after the
**dim_hm_item** and **dim_tb_itm_brand** tables are joined, and then the generated new table and the **dim_tb_brand**
table are joined.
2. Locate the join based on the names of the related tables in Step 1. The result shows that data skew occurs in **LEFT**
**OUTER JOIN** in the SQL statements and table t1 has data skew. To resolve this data skew issue, add the following
command to the SQL statements:

```
/*+ skewjoin(t1) */
```

**Precautions**

Supported join types: INNER JOIN allows you to specify a hint for either the right or left table of the JOIN operation. LEFT JOIN, SEMI JOIN, and ANTI JOIN allow you to specify a hint only for the left table. RIGHT JOIN allows you to specify a hint only for the right table. FULL JOIN does not support SKEWJOIN HINT. An Aggregate is run after SKEWJOIN HINT is added, which slows down the JOIN operation. Therefore, we recommend that you add SKEWJOIN HINT only to the JOIN statements that cause data skew. The data type of Left Side Join Key must be the same as that of Right Side Join Key for the JOIN statement to which SKEWJOIN HINT is added. If the data types are different, SKEWJOIN HINT becomes ineffective. After a hint is added, the optimizer runs an Aggregate to dynamically obtain the hot key values of the first 20 rows with the most duplicate key values. 20 is a default value. You can add the following flag parameter and specify the number of the rows whose hot key values you want to return.

```
set odps.optimizer.skew.join.topk.num = xx;
```

You can specify a hint only for one of the two tables in the JOIN operation. In the JOIN statement to which SKEWJOIN HINT is added, **left key** = **right key** must be included. SKEWJOIN HINT cannot be added to a CARTESIAN JOIN statement. When you use SKEWJOIN HINT with other hints, note that SKEWJOIN HINT cannot be added to a JOIN statement to which MAPJOIN HINT is added. On the Json Summary tab of LogView, you can search for the **topk_agg** field to check whether SKEWJOIN HINT takes effect. If such a field exists, SKEWJOIN HINT takes effect.

#### 3.17.2 Insufficient computing resources

This topic describes the issue of insufficient computing resources and provides a solution. Computing resources in MaxCompute may be insufficient due to improper planning and misuse of cluster resources. Jobs with insufficient computing resources have the following common characteristics: The job output stops at a stage and the progress remains unchanged. For example, in the following figure, the progress of M1_Stg1 in the job remains at 0%. R2_1_Stg1 depends on M1_Stg1. Therefore, the progress of R2_1_Stg1 remains at 0% before M1_Stg1 is complete. Task instances are in the **Ready** state on Logview, as shown in the following figure. This state indicates that resources are insufficient to run these task instances. After an instance obtains the necessary resources, its state changes to **Running**. If an instance is in the **Waiting** state, the instance waits for the completion of the task on which it depends. Each job is split into multiple tasks based on an execution plan. These tasks form a directed acyclic graph (DAG). Multiple instances are concurrently invoked in each task to complete the computation. In most cases, the resources required to invoke an instance are a single-core CPU and 2 GB memory. To properly allocate resources, a quota group is assigned to each project. The quota group determines the upper limit of resources (CPU and memory) that are available for all jobs in the project. If the resources used by the jobs that concurrently run reach the upper limit of the quota group, the jobs stop running due to insufficient resources. You can use one of the following methods to resolve this issue: Run jobs in off-peak hours. Contact O&M personnel to increase the resource capacity of the quota group for the project.

#### 3.17.3 MaxCompute storage optimization tips

**Partition tables reasonably**

MaxCompute supports the concept of partitioning in a table. A partition refers to the specified partition space in the creation of a table; that is, a few fields in the specified table as the partition columns. In most cases, you can consider a partition as a directory in a file system. MaxCompute divides each value of the partition column into a partition (directory). Users can specify multi-level partitions (use multiple fields of the table as partition columns). Multi-level partitions are like multi-level directories. If you specify the name of the partition that you want to access when using the data, then only the corresponding partition are read, avoiding a full table scan. This improves the processing efficiency and reduces costs.

| ent: | create table src (key string, value bigint) partitioned by (pt |   |
|---|---|---|
| select * from src where |   |   |

string); . In this example, `select * from src where` pt='20160901'; specifies the partitioning format. MaxCompute takes only the data in the "20160901" partition as the input when generating a query plan. Example of a non-partitioning statement: select * from src where key = 'MaxCompute'; scans the entire table. Partitioning is usually based on date or geographical region. You may also set partitions based on your business requirements. Example:

```
create table if not exists sale_detail( shop_name string, customer_id string, total_price double) partitioned by (sale_date string,region string); -- Create a two-level partitioned table, in which sale_date is level-1 partition, and region level-2 partition.
```

**Set table lifecycle reasonably**

Storage space on MaxCompute is precious. You can set the life cycle of a table according to data usage. MaxCompute will delete expired data to save storage space. Example: Run the `create table test3 (key boolean) partitioned by (pt string, ds string) lifecycle` 100; command to create a table with a lifecycle of 100. If the latest modification time of this table or partition was more than 100 days ago, the table or partition will be deleted.

**Important**

The lifecycle takes a partition as the smallest unit, so for a partitioned table, if some partitions reach the lifecycle threshold, they will be deleted directly. Partitions that have not reached the lifecycle threshold are not be affected. Run the alter table table_name set lifecycle days; command to modify the lifecycle of an existing table.

**Archive cold data**

Some data need to be preserved either permanently or for a long period of time, but the frequency of access decreases over time. When the use frequency is very low, you can archive the data. The archive function saves data with RAID. Data is not simply stored as three copies. By using the Cauchy Reed-Solomon algorithm, data is stored as six copies of the original data plus three parity blocks. This improves the effective storage ratio from 1:3 to 1:1.5. In addition, MaxCompute uses the bzip2 algorithm to archive tables with a higher compression ratio than other algorithms. Combining the two algorithms reduces storage usage by more than 70%. Archiving command format is as below:

```
ALTER TABLE table_name [PARTITION(partition_name='partition_value')] ARCHIVE;
```

Example:

```
alter table my_log partition(ds='20140101') archive;
```

**Merge small files**

In the reduce calculation or real-time tunnel data collection, a large number of small files are generated. Too many small files may cause the following problems: Many instances are occupied because a single instance can process only a small number of files. This results in a waste of resources, affecting the overall execution performance. The file system becomes larger, while the use ratio of disk space becomes smaller. Currently, there are two alternative ways to merge small files: ALTER merge mode and SQL merge mode: The ALTER merge mode merges files through 'console' command. The command format is as follows:

| ALTER TABLE tablename [PARTITION] MERGE SMALLFILES; |   |   |
|---|---|---|
| Set control parameters after SQL execution is complete. Run | odps.task.merge.enabled=true; | to determine whether |

it is necessary to merge small files. If so, start FuxiJob to merge these files.

#### 3.17.4 UDF OOM

This topic describes the UDF OOM issue and provides a solution. An OOM error is reported when some jobs are running. Detailed error information:

```
FAILED: ODPS-0123144: Fuxi job failed - WorkerRestart errCode:9,errMsg:SigKill(OOM), usually caused by OOM(out of memory)
```

You can configure UDF runtime parameters to fix the error. Example:

```
odps.sql.mapper.memory=3072; set odps.sql.udf.jvm.memory=2048; set odps.sql.udf.python.memory=1536;
```

### 3.18 Limits of MaxCompute SQL statements

This topic describes all the limits of MaxCompute SQL statements.

| Limit | Maximum value/Limit | Requirement | Description |
|---|---|---|---|
| Table name length | 128 bytes | Size | A table or column name can contain only letters, digits, and underscores ( ). It must _ start with a letter. |
| Comment length | 1,024 bytes | Size | A comment is a valid string that cannot exceed 1,024 bytes in length. |
| Column definitions in a table | 1,200 | Quantity | A table can contain a maximum of 1,200 column definitions. |
| Partitions in a table | 60,000 | Quantity | A table can contain a maximum of 60,000 partitions. |
| Partition levels of a table | 6 | Quantity | A table can contain a maximum of six levels of partitions. |
| Destination INSERT objects | 256 | Quantity | In a MULTI-INSERT operation, you can insert data into a maximum of 256 tables at a time. |
| UNION ALL | 256 | Quantity | A UNION ALL operation can be performed on a maximum of 256 tables. |
| MAPJOIN | 128 | Quantity | A MAPJOIN operation can be performed on a maximum of 128 small tables. |
| MAPJOIN memory | 512 MB | Size | The memory size for all small tables on which a MAPJOIN operation is performed cannot exceed 512 MB. |
| Window functions | 5 | Quantity | A SELECT statement can contain a maximum of five window functions. |
| PT IN SUBQUERY | 1,000 | Quantity | A PT IN SUBQUERY statement can generate a maximum of 1,000 rows. |
| Length of an SQL statement | 2 MB | Size | An SQL statement cannot exceed 2 MB in length. This limit is suitable for the scenarios where you use an SDK to call SQL statements. |
| Conditions of a WHERE clause | 256 | Quantity | A WHERE clause can contain a maximum of 256 conditions. |
| Length of a column record | 8 MB | Size | A column record in a table cannot exceed 8 MB in length. |
| Parameters in an IN clause | 1,024 | Quantity | This item specifies the maximum number of parameters in an IN clause, for example, IN (1,2,3….,1024) . If the number of parameters in an IN clause is too large, the compilation performance is affected. We recommend that you use no more than 1,024 parameters, but this is not a fixed upper limit. |

| jobconf.json | 1 MB | Size |   | The maximum size of the jobconf.json file is 1 MB. If a table contains a large number of partitions, the size of the jobconf.json file may exceed 1 MB. |   |
|---|---|---|---|---|---|
| View | Not writable | Operation |   | A view is not writable and does not support the INSERT operation. |   |
| Data type and position of a column | Unmodifiable | Operation |   | The data type and position of a column cannot be modified. |   |
| Java UDFs | Not allowed to be abstract or static | Operation |   | Java UDFs cannot be abstract or static . |   |
| Partitions that can be queried | 10,000 | Quantity |   | A maximum of 10,000 partitions can be queried. |   |
| SQL execution plans | 1 MB | Size |   | The size of the execution plan generated by MaxCompute SQL cannot exceed 1 MB. Otherwise, FAILED: ODPS- |   |
|   |   |   |   |   | FAILED: ODPS- |
|   |   |   |   | 0010000:System internal error - The |   |
|   |   |   |   | Size of Plan is too large |   |

**Important**

The preceding limits cannot be manually modified.

### 3.19 Appendix

#### 3.19.1 Escape characters

This topic describes the escape characters in MaxCompute SQL. In MaxCompute SQL, the backslash (\) is an escape character that invokes an alternative representation on the special characters in a character string. This escape character may also indicate a literal interpretation of the characters that follow the escape character. If the backslash (\) in a string constant is followed by three valid octal digits in the range from 001 to 177, the system converts the ASCII values to the corresponding characters. The following table describes the mapping between escape characters and represented special characters.

| Escape character | Represented special character |
|---|---|
| \b | Backspace |
| \t | Tab |
| \n | Newline |
| \r | Carriage-return |
| \' | Single quotation mark |
| \" | Double quotation marks |
| \ \ | Backslash |
| \; | Semicolon |
| \Z | Control-Z |
| \0 or \00 | Ending character |

Use an escape character to indicate a literal interpretation of the characters that follow the escape character. String constants in MaxCompute SQL can be expressed in single quotation marks (' ') or double quotation marks ('' ''). You can include double quotation marks ('' '') in a string that is enclosed in single quotation marks (' ') or include single quotation marks (' ') in a string that is enclosed in double quotation marks ('' ''). Examples:

```
"I'm a happy manong." 'I\'m a happy manong.'
```

Use an escape character to represent special characters. Examples:

```
select length('a\tb'); -- 3 is displayed in the returned result. This indicates that the string contains three characters and that \ t is treated as one character. select 'a\ab',length('a\ab'); -- aab, 3 is displayed in the returned result. \a is treated as Letter a.
```

#### 3.19.2 LIKE usage

This topic describes how to use the LIKE operator for character matching. In LIKE character matching, a percent sign (%) is a wildcard character that matches an arbitrary number of characters. An underscore (_) is a wildcard character that matches a single character. To match percent signs (**%**) or underscores (**_**), escape them with double backslashes (\\). Specifically, **\\%** or **\\_** is used for the match.

```
'abcd' like 'ab%' -- True. 'abcd' like 'ab_' -- False. 'ab_cde' like 'ab\\_c%'; -- True.
```

MaxCompute SQL statements support only UTF-8 character sets. If data is encoded in another format, the calculation result may be incorrect.

#### 3.19.3 Regular expressions

This topic describes regular expressions in MaxCompute SQL. Regular expressions in MaxCompute SQL use the Perl Compatible Regular Expressions (PCRE) standards to match strings by character.

**RLIKE**

You can use the RLIKE operator to match regular expressions. The following table lists the supported metacharacters.

| Metacharacter | Description |   |   |
|---|---|---|---|
| ^ | Matches the beginning of a string. |   |   |
| $ | Matches the end of a string. |   |   |
| . | Matches any single character. |   |   |
| * | Matches zero or more instances of the preceding character or character pattern. |   |   |
| + | Matches one or more instances of the preceding character or character pattern. |   |   |
| ? | Matches zero or one instance of the preceding character or character pattern. |   |   |
| ? | Matches a modifier. If this character follows one of other characters ( *, +, ?, {n}, {n,}, or {n,m} ), the match pattern is non-greedy. In the non-greedy algorithm, a character string matches as few characters as possible. In the greedy algorithm, a character string matches as many characters as possible. By default, the greedy algorithm is used. |   |   |
|   |   | ( *, +, ?, {n}, {n,}, or |   |
| A\|B | Matches A or B. |   |   |
| (abc)* | Matches the abc sequence zero or more times. |   |   |

|   | {n,m} |
|---|---|

| {n} or {m,n} | The number of matches. |
|---|---|
| [ab] | Matches any character in the brackets. Fuzzy match is used. |
| [a-d] | Matches one of the following characters: a, b, c, and d. |
| [^ab] | Matches any character except those in the brackets. |
| [::] | For more information, see the following table. |
| \ | The escape character. |
| \n | n is a digit ranging from 1 to 9 and indicates back reference. |
| \d | Matches a digit. |
| \D | Matches a non-digit character. |

**POSIX character groups**

| Character group | Description | Valid value |
|---|---|---|
| [[:alnum:]] | Letters and digits | [a-zA-Z0-9] |
| [[:alpha:]] | Letters | [a-zA-Z] |
| [[:ascii:]] | ASCII characters | [\x00-\x7F] |
| [[:blank:]] | Spaces and tab characters | [ \t] |
| [[:cntrl:]] | Control characters | [\x00-\x1F\x7F] |
| [[:digit:]] | Digits | [0-9] |
| [[:graph:]] | Characters other than whitespace characters | [\x21-\x7E] |
| [[:lower:]] | Lowercase letters | [a-z] |
| [[:print:]] | [:graph:] and whitespace characters | [\x20-\x7E] |
| [[:punct:]] | Punctuations | [][!”#$%&’()*+,./:;<=>? @\^ `{\|}~-] _ |
| [[:space:]] | Whitespace characters | [ \t\r\n\v\f] |
| [[:upper:]] | Uppercase letters | [A-Z] |
| [[:xdigit:]] | Hexadecimal characters | [A-Fa-f0-9] |

The system uses a backslash (\) as the escape character. A backslash (\) in a regular expression indicates a second escape. For example, a regular expression is used to match the `a+b` string. The plus sign ( `+` ) is a special character in the expression and must be escaped. In the regular expression engine, the string is expressed as

| a\\+b |   |
|---|---|
|   | a\\\+b |

a\\+b . The system must perform another escape in the expression. Therefore, the expression that can match the The following example shows how to use escape characters in a regular expression. The test_dual table is used.

```
select 'a+b' rlike 'a\\\+b' from test_dual;
```

The following result is returned:

```
+------+
| _c1  |
+------+
| true |
+------+
```

The \ character is a special character in the regular expression engine. To match this character, it is expressed as **\\** in the engine. Then, the system performs an escape on the expression. As a result, the \ character is expressed as **\\\**.

```
select 'a\\b', 'a\\b' rlike 'a\\\b' from test_dual;
```

The following result is returned:

```
+-----+------+
| _c0 | _c1  |
+-----+------+
| a\b | false |
+-----+------+
```

If a MaxCompute SQL statement contains a\\b , MaxCompute returns a\b because MaxCompute escapes the expression. If a string contains tab characters, MaxCompute stores \t as one character when MaxCompute reads this expression. In this case, \t is a common character in regular expressions.

```
select 'a\tb', 'a\tb' rlike 'a\tb' from test_dual;
```

The following result is returned:

```
+---------+------+
| _c0     | _c1  |
+---------+------+
| a     b | true |
+---------+------+
```

#### 3.19.4 Reserved words and keywords

This topic describes all reserved words and keywords in MaxCompute SQL.

**Important**

When you name a table, a column, or a partition, do not use reserved words or keywords. Otherwise, an error may occur. Reserved words and keywords are not case-sensitive.

```
    %    &    &&    (    )    *    +
    -    .    /    ;    <    <=    <>
    =    >    >=    ?    ADD    AFTER    ALL
    ALTER    ANALYZE    AND    ARCHIVE    ARRAY    AS    ASC
    BEFORE    BETWEEN    BIGINT    BINARY    BLOB    BOOLEAN    BOTH    DECIMAL
    BUCKET    BUCKETS    BY    CASCADE    CASE    CAST    CFILE
    CHANGE    CLUSTER    CLUSTERED    CLUSTERSTATUS    COLLECTION    COLUMN    COLUMNS
    COMMENT    COMPUTE    CONCATENATE    CONTINUE    CREATE    CROSS    CURRENT
    CURSOR    DATA    DATABASE    DATABASES    DATE    DATETIME    DBPROPERTIES
    DEFERRED    DELETE    DELIMITED    DESC    DESCRIBE    DIRECTORY    DISABLE
    DISTINCT    DISTRIBUTE    DOUBLE    DROP    ELSE    ENABLE    END    EXCEPT
    ESCAPED    EXCLUSIVE    EXISTS    EXPLAIN    EXPORT    EXTENDED    EXTERNAL
    FALSE    FETCH    FIELDS    FILEFORMAT    FIRST    FLOAT    FOLLOWING
    FORMAT    FORMATTED    FROM    FULL    FUNCTION    FUNCTIONS    GRANT
    GROUP    HAVING    HOLD_DDLTIME    IDXPROPERTIES    IF    IMPORT    IN
    INDEX    INDEXES    INPATH    INPUTDRIVER    INPUTFORMAT    INSERT    INT
    INTERSECT    INTO    IS    ITEMS    JOIN    KEYS    LATERAL
    LEFT    LIFECYCLE    LIKE    LIMIT    LINES    LOAD    LOCAL
    LOCATION    LOCK    LOCKS    LONG    MAP    MAPJOIN    MATERIALIZED
    MINUS    MSCK    NOT    NO_DROP    NULL    OF    OFFLINE    OFFSET
    ON    OPTION    OR    ORDER    OUT    OUTER    OUTPUTDRIVER
    OUTPUTFORMAT    OVER    OVERWRITE    PARTITION    PARTITIONED    PARTITIONPROPERTIES    PARTITIONS
    PERCENT    PLUS    PRECEDING    PRESERVE    PROCEDURE    PURGE    RANGE
    RCFILE    READ    READONLY    READS    REBUILD    RECORDREADER    RECORDWRITER
    REDUCE    REGEXP    RENAME    REPAIR    REPLACE    RESTRICT    REVOKE
    RIGHT    RLIKE    ROW    ROWS    SCHEMA    SCHEMAS    SELECT
    SEMI    SEQUENCEFILE    SERDE    SERDEPROPERTIES    SET    SHARED    SHOW
    SHOW_DATABASE    SMALLINT    SORT    SORTED    SSL    STATISTICS    STATUS    STORED
    STREAMTABLE    STRING    STRUCT    TABLE    TABLES    TABLESAMPLE    TBLPROPERTIES
    TEMPORARY    TERMINATED    TEXTFILE    THEN    TIMESTAMP    TINYINT    TO
    TOUCH    TRANSFORM    TRIGGER    TRUE    TYPE    UNARCHIVE    UNBOUNDED    UNDO
    UNION    UNIONTYPE    UNIQUEJOIN    UNLOCK    UNSIGNED    UPDATE    USE
    USING    UTC    UTC_TMESTAMP    VIEW    WHEN    WHERE    WHILE    DIV
```

#### 3.19.5 Settings of new data types

This topic describes the precautions for configuring new data types in MaxCompute SQL. If you want to read a table that includes new data types, you are not required to add the setodps.sql.type.system.odps2=true; flag. However, you must take note of the following points: If the flag is not added, the read data is implicitly converted into the original data type for all computations. If the flag is not added for integer constants, the BIGINT type is used, and an error message is reported. If you write data to a table and the data is in passthrough mode, you can choose not to add the new data type flag. However, if you want to calculate the data, an error is reported because the implicit data type conversion is invalid.

#### 3.19.6 ACID semantics of MaxCompute parallel write jobs

This topic describes the atomicity, consistency, isolation, durability (ACID) semantics of MaxCompute parallel write jobs.

**Terms**

Operation: a single job submitted in MaxCompute. Data object: an object that stores data, such as a non-partitioned table or a partition. INTO job: an SQL job that contains the INTO keyword, such as INSERT INTO or DYNAMIC INSERT INTO. OVERWRITE job: an SQL job that contains the OVERWRITE keyword, such as INSERT OVERWRITE or DYNAMIC INSERT OVERWRITE. Data upload by using Tunnel: an INTO or OVERWRITE job.

**Description of ACID semantics**

Atomicity: An operation is completely performed or not performed at all. An operation is not partially performed. Consistency: The integrity of data objects is maintained when an operation is performed. Isolation: An operation is independent of other parallel operations. Durability: After an operation is complete, modified data is permanently valid and not lost even if a system failure occurs.

**Scenarios of ACID semantics for MaxCompute**

Atomicity When multiple jobs conflict with each other, MaxCompute ensures that only one job succeeds. The atomicity of the CREATE, OVERWRITE, and DROP operations on a single table or partition is ensured. The atomicity of cross-table operations, such as MULTI-INSERT, cannot be ensured. In extreme cases, the following operations may not be atomic: A `DYNAMIC INSERT OVERWRITE` operation that is performed on more than 10,000 partitions. An INTO operation. The atomicity of INTO operations cannot be ensured because data cleansing fails during a transaction rollback. However, the data cleansing failure does not cause loss of original data. Consistency The consistency can be ensured for OVERWRITE jobs. If an INTO job fails due to a conflict, data from the failed job may remain. Isolation For non-INTO operations, MaxCompute ensures that read operations are submitted. For INTO operations, some read operations may not be submitted. Durability MaxCompute ensures data durability.

**ACID semantics of transactional tables**

If existing ACID semantics are used, INTO operations ensure that read operations are submitted and no data remains after an operation fails due to a conflict. The atomicity of the UPDATE and DELETE operations on a single non-partitioned table or a partition is ensured. For example, if two update jobs run in parallel to modify the data of a partition, only one job succeeds. The partition is not partially updated by one job. It is also not updated by the two jobs with part of the updated data remained. Conflicts among parallel operations: When two jobs run in parallel and write data to the same destination table, a conflict may occur. In this case, the job that ends earlier will succeed, and the job that ends later will fail due to the conflict. The following table describes the conflicts that may occur when two jobs run in parallel and write data to the same non-partitioned table or partition. The first column lists the job that ends earlier. The other columns list the jobs that end later.

| Before/After | INSERT OVERWRITE | INSERT INTO | UPDATE/DELETE | MERGE SMALLFILES |
|---|---|---|---|---|
| INSERT OVERWRITE | Both jobs succeed. The result data of the INSERT OVERWRITE operation that ends later will overwrite that of the INSERT OVERWRITE operation that ends earlier. | Both jobs succeed. The result data of the INSERT INTO operation is appended to that of the INSERT OVERWRITE operation. | The INSERT OVERWRITE operation modifies the data of the non-partitioned table or partition. An error is reported in the UPDATE operation. | The INSERT OVERWRITE operation modifies the data of the non-partitioned table or partition. An error is reported in the MERGE SMALLFILES operation. |
| INSERT INTO | Both jobs succeed. The result data of the INSERT OVERWRITE operation overwrites that of the INSERT INTO operation. | Both jobs succeed. The result data of the two INSERT INTO operations is merged. | The INSERT INTO operation modifies the data of the non- partitioned table or partition. An error is reported in the UPDATE operation that ends later. | The INSERT INTO operation modifies the data of the non- partitioned table or partition. An error is reported in the MERGE SMALLFILES operation that ends later. |
| UPDATE/DELETE | Both jobs succeed. The result data of the INSERT OVERWRITE operation overwrites that of the UPDATE operation. | Both jobs succeed. The result data of the INSERT INTO operation is appended to that of the UPDATE operation. | The UPDATE operation that ends earlier modifies the data of the non-partitioned table or partition. An error is reported in the UPDATE operation that ends later. | The UPDATE operation modifies the data of the non-partitioned table or partition. An error is reported in the MERGE SMALLFILES operation that ends later. |

| MERGE SMALLFILES | Both jobs succeed. The result data of the INSERT OVERWRITE operation overwrites that of the MERGE SMALLFILES operation. | Both jobs succeed. The result data of the INSERT INTO operation is appended to that of the MERGE SMALLFILES operation. | The MERGE SMALLFILES operation modifies the data of the non-partitioned table or partition. An error is reported in the UPDATE operation that ends later. | The MERGE SMALLFILES operation that ends earlier modifies the data of the non-partitioned table or partition. An error is reported in the MERGE SMALLFILES operation that ends later. |
|---|---|---|---|---|

The following table simplifies the preceding rules and describes only whether an error is reported for an operation after data changes.

| Operation | Error reported upon data changes |
|---|---|
| INSERT OVERWRITE | No |
| INSERT INTO | No |
| UPDATE/DELETE | Yes |
| MERGE SMALLFILES | Yes |

No conflict occurs for INSERT operations in the event of data changes. An error is reported in the UPDATE/DELETE or MERGE SMALLFILES operation if the destination non-partitioned table or partition has data changes. Minor or major compaction is classified as MERGE SMALLFILES operations. In extreme scenarios, if multiple jobs are all in the metadata update phase, an error may be reported due to a conflict among these parallel update operations. atures of MaxCompute

## 4 Open source features of MaxCompute

**MaxCompute**

This topic describes open source features of MaxCompute.

**SDK**

MaxCompute provides APIs for SDK for Java and SDK for Python to create, view, and delete MaxCompute tables. You can use SDKs to edit code and perform required operations on MaxCompute Technical support: View the official documentation or submit a ticket.

**MaxCompute RODPS**

MaxCompute RODPS is an R plug-in for MaxCompute. For more information, see aliyun-odps-r-plugin on GitHub. Technical support: Leave a message or create an issue in aliyun-odps-r-plugin on GitHub.

**MaxCompute JDBC**

MaxCompute JDBC is an official JDBC driver provided by MaxCompute. It provides a set of interfaces to run SQL tasks for Java programs. The project is hosted in aliyun-odps-jdbc on GitHub. Technical support: Leave a message or create an issue in aliyun-odps-jdbc on GitHub.

**Data Collector**

Data Collector is a collection of the major open source data collection tools of MaxCompute, such as the Flume plug-in, OGG plug-in, Sqoop, Kettle plug-in, and Hive Data Transfer UDTF. Flume and OGG plug-ins are implemented based on the DataHub SDK, whereas Sqoop, Kettle plug-in, and Hive Data Transfer UDTF are implemented based on the Tunnel SDK. DataHub is a real-time data transfer channel, and Tunnel is a batch data transfer channel. The Flume and OGG plug-ins are used to transfer data in real time. Sqoop, Kettle plugin, and Hive Data Transfer UDTF are used to transfer data in offline mode. For information about the source code, see aliyun-maxcompute-data-collectors on GitHub. For more information about these tools, see wiki on GitHub. Technical support: Leave a message or create an issue in aliyun-maxcompute-data-collectors on GitHub.
