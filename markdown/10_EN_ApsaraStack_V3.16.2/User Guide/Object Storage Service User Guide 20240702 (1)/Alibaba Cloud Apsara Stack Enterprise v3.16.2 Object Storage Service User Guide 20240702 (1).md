---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Object Storage Service User Guide 20240702 (1) User Guide"
product_version: "V3.16.2"
doc_version: "20240702"
pdf_pages: 61
source_pdf: "281790d88d7df8fe_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Object Storage Service User Guide 20240702 (1).pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8OSS/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Object%20Storage%20Service%20User%20Guide%2020240702%20%281%29.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Object Storage Service User Guide 20240702 (1) User Guide

## Table of Contents

- 1 What is OSS?
  - 1.1 Features
    - 1.1.1 Manage buckets
      - 1.1.1.1 Create a bucket
      - 1.1.1.2 ACL
      - 1.1.1.3 Static website hosting
      - 1.1.1.4 Logging
      - 1.1.1.5 Lifecycle rules
    - 1.1.2 Manage objects
      - 1.1.2.1 Upload objects
      - 1.1.2.2 ACL
      - 1.1.2.3 Download objects
      - 1.1.2.4 Search for objects
      - 1.1.2.5 Manage objects by using directories
      - 1.1.2.6 Object tagging
    - 1.1.3 Data security
      - 1.1.3.1 Erasure coding
      - 1.1.3.2 Resource isolation
      - 1.1.3.3 Disaster recovery
      - 1.1.3.4 Access permissions and account authorization
      - 1.1.3.5 Server-side encryption
      - 1.1.3.6 Client-side encryption
    - 1.1.4 Data processing
      - 1.1.4.1 IMG
      - 1.1.4.2 Video snapshots
- 2 Usage notes
- 3 Quick start
  - 3.1 Log on to the OSS console
  - 3.2 Create buckets
  - 3.3 Upload objects
  - 3.4 Obtain object URLs
- 4 Buckets
  - 4.1 View bucket information
  - 4.2 Delete buckets
  - 4.3 Modify bucket ACLs
  - 4.4 Configure static website hosting
  - 4.5 Configure hotlink protection
  - 4.6 Configure CORS
  - 4.7 Configure lifecycle rules
  - 4.8 Configure storage quota
  - 4.9 Configure cluster-disaster recovery
  - 4.10 Bucket tagging
  - 4.11 Configure server-side encryption
  - 4.12 Bind a bucket to a VPC
  - 4.13 Configure CRR rules
  - 4.14 Configure cross-cloud replication
  - 4.15 Log management
    - 4.15.1 Configure logging
    - 4.15.2 Real-time log query
  - 4.16 IMG
    - 4.16.1 Configure image styles
    - 4.16.2 Configure source image protection
- 5 Objects
  - 5.1 Search for objects
  - 5.2 Configure object ACLs
  - 5.3 Create folders
  - 5.4 Configure bucket policies to authorize other users to access OSS resources
  - 5.5 Delete objects
  - 5.6 Manage parts
- 6 Create single tunnels
- 7 Add OSS paths

## 1 What is OSS?

Object Storage Service (OSS) is a secure, cost-effective, and highly reliable cloud storage service provided by Alibaba Cloud.

**Overview**

OSS is an object storage service based on key-value pairs. Files uploaded to OSS are stored as objects in buckets. You can obtain the content of an object based on the object key. Compared with user-created server storage, OSS has outstanding advantages in reliability, security, cost-effectiveness, and data processing capabilities. OSS enables you to store and retrieve a variety of unstructured data objects, such as text, images, audios, and videos over networks anytime. In OSS, you can perform the following operations: Create a bucket and upload objects to the bucket. Obtain an object URL from OSS to share or download the object. Modify the attributes or metadata of a bucket or an object. You can also configure the access control list (ACL) of the bucket or the object. Perform basic and advanced operations in the OSS console. Perform basic and advanced operations by using OSS SDKs or calling RESTful API operations in your application.

**Basic concepts**

**Object**

The basic unit for data operations in OSS. Objects are also known as OSS files. An object is composed of object metadata, object content, and a key. A key can uniquely identify an object in a bucket. Object metadata is a group of key-value pairs that define the properties of an object, such as the last modification time and the object size. You can also assign user metadata to the object. The lifecycle of an object starts when the object is uploaded and ends when it is deleted. During the lifecycle, the object cannot be modified. OSS does not support modifying objects. If you want to modify an object, you must upload a new object with the same name as the existing object to replace it.

**Note**

Unless otherwise stated, objects and files mentioned in OSS documents are collectively called objects.

**Bucket**

A container for OSS objects. Each object in OSS is contained in a bucket. You can configure and modify the attributes of a bucket to manage ACLs and lifecycle rules of the bucket. These attributes apply to all objects in the bucket. Therefore, you can create different buckets to meet different management requirements. OSS does not use a hierarchical structure for objects, but instead uses a flat structure. All elements are stored as objects in buckets. However, OSS supports folders as a concept to group objects and simplify management. You can create multiple buckets. A bucket name must be unique in OSS within an Apsara Stack tenant account. Bucket names cannot be changed after the buckets are created. A bucket can contain an unlimited number of objects.

**Strong consistency**

Object operations in OSS are atomic. Operations can either succeed or fail without intermediate states. To ensure that users can access only complete data, OSS does not return corrupted or partial data. Object-related operations in OSS are highly consistent. For example, when a user receives an upload (PUT) success response, the uploaded object can be read immediately, and copies of the object are written to multiple devices for redundancy. Therefore, there are no situations where data is not obtained when you perform the read-after-write operation. The same is true for delete operations. After a user deletes an object, the object and its copies no longer exist. Similar to traditional storage devices, modifications are immediately visible in OSS and consistency is guaranteed.

**Comparison between OSS and file systems**

OSS is a distributed object storage service that stores objects based on key-value pairs. You can retrieve object content based on unique object keys. For example, the object name test1/test.jpg does not necessarily indicate that the object is stored in a directory named test1. In OSS, test1/test.jpg is only a string. There is nothing essentially different between test1/test.jpg and a.jpg. Therefore, similar amounts of resources are consumed regardless of which object you access. A file system uses a typical tree index structure. To access a file named test1/test.jpg, you must first access the test1 directory and then search for the test.jpg file in this directory. This makes it easy for a file system to support folder operations, such as renaming, deleting, and moving directories because these operations are only performed on directories. However, the performance of a file system depends on the capacity of a single device. The more files and directories that are created in the file system, the more resources and time are consumed. You can simulate similar folder functions of a file system in OSS, but such operations are costly. For example, if you want to rename the test1 directory as test2, OSS must copy all objects whose names start with test1/ to generate objects whose names start with test2. This operation consumes a large amount of resources. Therefore, we recommend that you do not perform such operations in OSS. Objects stored in OSS cannot be modified. A specific operation must be called to append an object. The generated objects are different from the objects uploaded by using other methods. To modify an object, you must upload the entire object again. A file system allows you to modify files. You can modify the content at a specified offset location or truncate the end of a file. These features make file systems suitable for more general scenarios. However, OSS supports a large amount of concurrent access, whereas the performance of a file system is subject to the performance of a single device. We recommend that you do not map operations on OSS objects to file systems because it is inefficient. If you attach OSS as a file system, we recommend that you only add new files, delete files, and read files. You can make full use of OSS advantages, such as the capability to process and store large amounts of unstructured data such as images, videos, and documents.

**Limits**

| Limit | Description |
|---|---|
| Bucket | You can create a maximum of 100 buckets. After a bucket is created, its name and region cannot be modified. |

| Upload objects | Objects larger than 5 GB cannot be uploaded by using the following methods: console upload, simple upload, form upload, or append upload. To upload an object that is larger than 5 GB, you must use multipart upload. The size of an object uploaded by using multipart upload cannot exceed 48.8 TB. If you upload an object that has the same name as an existing object in OSS, the new object overwrites the existing object. |
|---|---|
| Delete objects | Deleted objects cannot be recovered. You can delete up to 100 objects at a time from the console. To delete more than 100 objects at a time, you must call API operations or use an OSS SDK. |
| Lifecycle rules | You can configure up to 1,000 lifecycle rules for each bucket. |

### 1.1 Features

#### 1.1.1 Manage buckets

##### 1.1.1.1 Create a bucket

A bucket is a container that is used to store objects in Object Storage Service (OSS). Every object is contained in a bucket. You can configure a variety of bucket attributes such as the region, access control list (ACL), and storage class. You can create buckets of different storage classes to store data.

**Naming conventions**

After a bucket is created, the name of the bucket cannot be modified. OSS supports the following bucket naming conventions: The name of a bucket must be unique in OSS in an Apsara Stack tenant account. The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or a digit. The name must be 3 to 63 characters in length.

**Examples**

The following examples of bucket names are valid: examplebucket1 test-bucket-2021 aliyun-oss-bucket The following examples show invalid bucket names and the reasons why the names are invalid: Examplebucket1 (Uppercase letters are included.) test_bucket_2021 (Underscores (_) are included.) aliyun-oss-bucket- (The name ends with a hyphen (-).)

##### 1.1.1.2 ACL

You can configure the access control list (ACL) of a bucket when you create the bucket or modify the ACL of a created bucket. Only the owner of a bucket can configure or modify the ACL of the bucket. You can set one of the following three ACLs for a bucket:

| ACL | Description |
|---|---|
| public-read-write | Anyone, including anonymous users, can perform read and write operations on the objects in the bucket. Warning All Internet users can access objects in the bucket and write data to the bucket. This may result in unexpected access to the data in your bucket and out-of- control costs. If a user uploads prohibited data or information, your legitimate interests and rights may be infringed. Therefore, we recommend that you do not set your bucket ACL to public read/write except in special cases. |
| public-read | Only the bucket owner can perform write operations on the objects in the bucket. Other users, including anonymous users can perform only read operations on the objects in the bucket. Warning All Internet users can access objects in the bucket. This may result in unexpected access to the data in your bucket and out-of-control costs. Exercise caution when you set your bucket ACL to Public Read. |
| private | Only the bucket owner can perform read and write operations on the objects in the bucket. Other users have no access to the objects in the bucket. |

##### 1.1.1.3 Static website hosting

Static websites are websites in which all web pages consist only of static content, including scripts such as JavaScript code that is run on the client. You can use the static website hosting feature to host your static website on an Object Storage Service (OSS) bucket and use the endpoint of the bucket to access the website.

**Usage notes**

When you configure static website hosting, you must specify the default homepage and the default 404 page for the website. The default homepage appears when you use a browser to access the static website hosted on an OSS bucket. The default homepage functions in a similar manner to the index.html file of a website. The object that you specify as the default homepage must be an object that is stored in the root directory of the bucket and allows anonymous access. The object must be in the HTML format. The default 404 page is the error page returned by OSS. When you use a browser to access the static website hosted on an OSS bucket and a 404 error occurs, OSS returns the default 404 page. The object that you specify as the default 404 page must be an object that is stored in the root directory of the bucket and allows anonymous access. The object must be in one of the following formats: HTML, JPG, PNG, BMP, and WebP.

**Configurations**

After you host a static website on a bucket, you must upload an object whose name is the same as that of the default homepage, such as index.html, to the bucket. If the bucket contains a directory such as subdir/, you must also upload the object named index.html to subdir/. In addition, you must upload an object whose name is the same as that of the default 404 page, such as error.html, to the bucket. The following structure shows the objects and directories in the sample bucket:

```
Bucket
 ├── index.html
 ├── error.html
 ├── example.txt
 └── subdir/
      └── index.html
```

In this example, the custom domain name `example.com` is mapped to the bucket, the default homepage of the static website hosted on the bucket is index.html, and the default 404 page of the website is error.html. When you access the static website by using the custom domain name, OSS returns different responses based on your configurations of Static Pages for the bucket that hosts the website.

| When you access | https://example.com/ |
|---|---|
| https://example.com/index.html |   |

When you access `https://example.com/` and `https://example.com/subdir/` , OSS returns

|   | https://example.com/example.txt |
|---|---|
|   | https://example.com/object |
| https://example.com/error.html |   |

##### 1.1.1.4 Logging

When you access Object Storage Service (OSS), large numbers of access logs are generated. After you enable and configure logging for a bucket, OSS generates log objects every hour in accordance with a predefined naming convention and then stores the access logs as objects in a specified bucket. You can use Apsara Stack Log Service or build a Spark cluster to analyze the logs.

**Naming conventions for log objects**

The following naming conventions apply to log objects that are stored in OSS:

```xml
<TargetPrefix><SourceBucket>YYYY-mm-DD-HH-MM-SS-UniqueString
```

| Field | Description |
|---|---|
| TargetPrefix | The prefix of the log object name. |
| SourceBucket | The name of the source bucket for which access logs are generated. |
| YYYY-mm-DD-HH-MM-SS | The time when the log object is created. The items of this field indicate the year, month, day, hour, minute, and second in sequence. |
| UniqueString | The string generated by OSS to uniquely identify the log object. |

**Usage notes**

The source bucket for which access logs are generated and the destination bucket in which the log objects are stored can be the same bucket or different buckets. However, the destination bucket must belong to the same account in the same region as the source bucket. OSS generates bucket access logs on an hourly basis. However, requests in the previous hour may be recorded in the logs generated for the subsequent hour. Before you disable logging, OSS keeps generating access logs. Delete log objects that you no longer need based on lifecycle rules to reduce storage costs. OSS adds more fields to access logs in the future. We recommend that developers consider potential compatibility issues when they develop log processing tools.

##### 1.1.1.5 Lifecycle rules

You can configure lifecycle rules to regularly delete expired objects and parts to save storage costs.

**Scenarios**

You can configure a lifecycle rule to regularly delete objects that are no longer accessed or convert the storage class of non-hot data to Infrequent Access (IA), Archive, or Cold Archive. This makes data management easier and saves storage costs. You can manually delete up to 1,000 objects each time. If a bucket contains more than 1,000 objects, you must delete the objects multiple times. In this case, you can configure a lifecycle rule that is used to delete all objects in the bucket the next day. This way, all objects in the bucket can be deleted the next day.

**Usage notes**

Number of lifecycle rules You can configure up to 100 lifecycle rules for each bucket in the OSS console and up to 1,000 lifecycle rules for each bucket by using OSS SDKs for a variety of programming languages. Effective time After a lifecycle rule is configured, OSS loads the rule within 24 hours. After the lifecycle rule is loaded, OSS runs the rule every day at 08:00:00 (UTC+8) and completes the actions triggered by the rule within 24 hours. The interval between the last modified time of an object and the time when the lifecycle rule is run must be longer than 24 hours. For example, if you configure a lifecycle rule for a bucket to delete objects one day after they are uploaded, objects that are uploaded on July 20, 2020 are deleted on a different date based on the specific time when the objects are uploaded. Objects uploaded before 08:00:00 (UTC+8) are deleted from 08:00:00 (UTC+8) on July 21, 2020 to 08:00:00 (UTC+8) on July 22, 2020. Objects uploaded after 08:00:00 (UTC+8) are deleted from 08:00:00 (UTC+8) on July 22, 2020 to 08:00:00 (UTC+8) on July 23, 2020.

**Important**

When you update a lifecycle rule, tasks performed based on the rule on the current day are suspended. We recommend that you do not frequently update lifecycle rules.

**Component elements**

A lifecycle rule consists of the following elements: Policy: specifies the objects and parts that match the rule. Match by prefix: specifies that the rule matches objects and parts by prefix. You can create multiple rules to match different prefixes. A prefix must be matched to only one lifecycle rule. Match by bucket: indicates that the rule matches all objects and parts stored in the bucket. After you configure a lifecycle rule for a bucket to match all objects and parts in a bucket, other lifecycle rules cannot be configured for the bucket. Object lifecycle policy: specifies the validity period or the expiration date of objects and the operation to perform on expired objects. Validity Period (Days): specifies the number of days to retain objects after they are last modified. The objects are deleted the next day after they expire. Expiration date: specifies a date to delete objects that are last modified before this date. Part lifecycle policy: specifies the validity period or the expiration date of parts and the operation to perform on these expired parts. Validity period: specifies the validity period for parts. Parts that match the lifecycle rule are retained for the validity period and are deleted after the validity period ends. Expiration date: specifies the expiration date of parts. Parts that are last modified before this date expire and are deleted.

#### 1.1.2 Manage objects

##### 1.1.2.1 Upload objects

Objects are the basic unit for data storage in Object Storage Service (OSS). Objects are also known as files. You can choose an upload method based on the size of the object to upload and your network environment. OSS provides the following upload methods: Simple upload includes streaming upload and object upload. You can use this method to upload an object up to 5 GB in size. Form upload: supports the upload of an object up to 5 GB in size. Append upload: supports the upload of an object up to 5 GB in size. Resumable upload: supports concurrent and resumable upload of an object up to 48.8 TB in size. This method is suitable for the upload of large objects. You can use this method to upload an object up to 48.8 TB in size. Multipart upload: supports the upload of an object up to 48.8 TB in size. This method is suitable for the upload of large objects. During object upload, you can configure object metadata and view upload progress in the Upload Tasks panel. After the object is uploaded, you can perform upload callback.

##### 1.1.2.2 ACL

Object Storage Service (OSS) allows you to configure access control lists (ACLs) for objects to control access to the objects. You can configure ACL for an object when or after you upload the object. By default, if you do not specify ACL for an object, the ACL of the object is **Inherited from Bucket**.
**Inherited from Bucket**: The ACL for the object is the same as that for the bucket.
**Private**: Only the bucket owner or authorized users can read from and write to the objects
in the bucket. Other users, including anonymous users, cannot access objects in the bucket.
**Public Read**: Only the bucket owner or authorized users can read from and write to
objects. Other users, including anonymous users, can only read from objects in the bucket.
**Public Read/Write**: All users, including anonymous users, can perform read and write
operations on objects in the bucket. The bucket owner are charged fees incurred by these operations. Therefore, we recommend that you use this ACL policy only when necessary.

##### 1.1.2.3 Download objects

Object Storage Service (OSS) provides a variety of object download methods that you can choose to download objects stored in buckets based on your requirements. OSS provides the following object download methods: Download objects to local disks: You can download objects stored in buckets to your local disks. Streaming download: If you want to download a large object or it takes a long time to download an object at a time, you can use streaming download to download the object incrementally until the entire object is downloaded. Range download: If you need only part of the data in an object, you can use range download to download data within the specified range. Resumable download: You may fail to download a large object if the network is unstable or other exceptions occur. In some cases, you may still fail to download the object even after multiple attempts. To handle this issue, OSS provides the resumable download feature. In resumable download, objects that you want to download are split into multiple parts and downloaded separately. After all parts are downloaded, these parts are combined into a complete object. Conditional download: You can specify one or multiple conditions when you download objects. If the specified conditions are met, the object is downloaded. If the specified conditions are not met, an error is returned and the object is not downloaded.

##### 1.1.2.4 Search for objects

If a large number of objects are stored in your buckets, you can search for an object by specifying the prefix that the object name contains.

**Usage notes**

Search rules You can search for objects by prefix. The string used to search for objects is case-sensitive and cannot contain forward slashes (/). Search results When you specify a prefix to search for an object in the root directory or a specified directory of a bucket, only the objects or subdirectories whose names contain the specified prefix are returned. Objects in subdirectories cannot be returned.

**Examples**

Search for specific objects or directories within the root directory of the bucket Specify a prefix to search for specific objects or directories. Then, objects and directories that match the prefix within the root directory of the bucket are returned. The following example shows the search result when you specify Example as the prefix to search for objects and directories within the root directory of the bucket named TestBucket.

```
Folder structure Specified prefix Search result TestBucket Example Examplesrcfolder1
    └── Examplesrcfolder1                                Exampledestfolder.png
           ├── test.txt
           ├── abc.jpg
    └── Exampledestfolder.png
    └── example.txt
```

Search for specific objects or subdirectories within a directory of the bucket Select the directory and specify a prefix. Then, objects and subdirectories that match the prefix within the directory are returned. The following example shows the search result when you specify Project as the prefix to search for objects and subdirectories within the directory named Examplesrcfolder1.

```
Folder structure Specified prefix Search result Examplesrcfolder1 Project Projectfolder
    └── Projectfolder                                         ProjectA.jpg
          ├── a.txt                                                        ProjectB.doc
          ├── b.txt
    └── ProjectA.jpg
    └── ProjectB.doc
    └── projectC.doc
```

##### 1.1.2.5 Manage objects by using directories

Object Storage Service (OSS) uses a flat structure instead of a hierarchical structure used by traditional file systems to store objects. All data in OSS are stored as objects in buckets. You can create simulated directories in OSS to help you categorize objects and control access to your objects in a simplified manner.

**Structure**

OSS uses objects whose names end with a forward slash (/) to simulate directories. The following example shows the structure of a bucket named examplebucket:

```
examplebucket
    └── log/
       ├── date1.txt
       ├── date2.txt
       ├── date3.txt
    └── destfolder/
       └── 2021/
          ├── photo.jpg
```

In the preceding structure: The following three objects have the log prefix in their names: log/date1.txt, log/date2.txt, and log/date3.txt. In the OSS console, a directory named log is displayed. Three objects named date1.txt, date2.txt, and date3.txt are stored within the directory. The destfolder/2021/photo.jpg object has the destfolder prefix in its name. In the OSS console, a directory named destfolder is displayed, which contains a subdirectory named 2021. An object named photo.jpg is stored in the 2021 subdirectory.

**Access control based on directories**

The following examples show how to grant third-party users different permissions to access the directories and objects in examplebucket described in the preceding section: The following objects within the log directory store the OSS access logs of a user in the last three days: log/date1.txt, log/date2.txt, and log/date3.txt. For support professionals to troubleshoot issues, such as slow access and object upload failures reported by the user, they need to view the logs stored in the three objects. In this case you can configure bucket policies to authorize other users to access your OSS resources An object named destfolder/2021/photo.jpg in examplebucket is a group photo of all your employees, which was taken on a 2021 spring outing. You want all your employees to have access to the object. In this case, you can set the ACL of the object to public read.

**Implementation methods**

You can create a directory in the OSS console. After you create a directory, you can upload objects to the directory. Directories cannot be created or deleted by calling API operations. However, you can use OSS SDKs for various programming languages to create or delete directories by using the following methods: When you upload an object to OSS, you can add a directory name that ends with a forward slash (/) to the object name (key) to create a directory for the object. For example, when you upload a local file named localfile.txt to a bucket named examplebucket, you can set the name of the uploaded object to destfolder/localfile.txt. In this case, a directory named destfolder is created in examplebucket, and the uploaded object named localfile.txt is stored in destfolder. In this example, the destfolder directory is simulated by an object whose name is destfolder/ and whose size is 0. When you delete objects, you can specify a prefix that is contained in the names of all objects you want to delete. In this case, the directory whose name is the specified prefix and all objects within the directory are deleted. For example, if you specify a prefix "log", the directory named log and all objects within the directory are deleted.

##### 1.1.2.6 Object tagging

Object tags can be used to classify objects. You can configure lifecycle rules and ACLs for objects based on their tags.

**Usage notes**

The object tagging feature uses a key-value pair to identify an object. You can add tags to objects when and after you upload objects. A maximum of 10 tags can be configured for each object. Tags associated with an object must have unique tag keys. A tag key can be up to 128 bytes in length. A tag value can be up to 256 bytes in length. Tag keys and tag values are case-sensitive. The key and the value of a tag can contain letters, digits, spaces, and the following special characters: + - = . _ : / Only the bucket owner and authorized users have read and write permissions on object tags. These permissions are independent of object access control lists (ACLs). In cross-region replication (CRR), object tags are replicated to the destination bucket.

**Configure lifecycle rules for objects with the same tags**

When you configure lifecycle rules, you can configure conditions for lifecycle rules to select subsets of objects to which the rules apply. You can configure conditions based on the object name prefixes, object tags, or both. If you configure conditions based on tags in one lifecycle rule, the rule applies only to objects that meet both the tag key and value conditions. If you configure object name prefixes and multiple object tags in one lifecycle rule, the rule applies only to objects that match the object name prefixes and object tags. Example:

```xml
<LifecycleConfiguration>
  <Rule>
    <ID>r1</ID>
    <Prefix>rule1</Prefix>
    <Tag><Key>xx</Key><Value>1</Value></Tag>
    <Tag><Key>yy</Key><Value>2</Value></Tag>
    <Status>Enabled</Status>
    <Expiration>
       <Days>30</Days>
    </Expiration>
  </Rule>
  <Rule>
    <ID>r2</ID>
    <Prefix>rule2</Prefix>
    <Tag><Key>xx</Key><Value>1</Value></Tag>
    <Status>Enabled</Status>
    <Transition>
      <Days>60</Days>
      <StorageClass>Archive</StorageClass>
   </Transition>
 </Rule>
</LifecycleConfiguration>
```

In the preceding rules: Objects whose names are prefixed with rule1 and whose tagging configurations are xx=1 and yy=2 are deleted after the objects are stored for 30 days. The storage class of objects whose names are prefixed with rule2 and whose tagging configurations are xx=1 is converted to Archive after the objects are stored for 60 days.

**Use RAM policies to manage permissions on objects with**

**specified tags**

You can authorize RAM users to manage object tags. You can also authorize RAM users to manage objects that have specific tags. Authorize RAM users to manage object tags You can authorize RAM users to manage all object tags or manage only specific object tags. If User A is authorized to set object tagging to allow=yes, this user can add the tagging configuration of allow=yes to objects. The following code provides an example on how to configure the corresponding RAM policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": "oss:PutObjectTagging",
      "Effect": "Allow",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "oss:RequestObjectTag/allow": [
            "yes"
```

`]` `}` `}` `}` `]` `}`

**Important**

After the RAM user is authorized to configure a specified tag for objects, the user can configure the tag only for existing objects. However, the user cannot configure the tag for objects when the user uploads the objects. Authorize RAM users to manage objects that have specific tags You can authorize RAM users to manage all objects that have specific tags. For example, you can authorize User A to access all objects that have the tagging configuration of allow=yes. The following code provides an example on how to configure the corresponding RAM policy: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": "oss:GetObject",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "oss:ExistingObjectTag/allow": [
            "yes"
```

`]` `}` `}` `}` `]` `}`

#### 1.1.3 Data security

##### 1.1.3.1 Erasure coding

Erasure Coding (EC) is a data storage mode used by Object Storage Service (OSS). Compared with triplicate storage, EC can provide higher data reliability at lower data redundancy levels.

**EC**

EC involves the following two concepts: Data fragments (m): Data is divided into m data fragments. Parity fragments (n): n parity fragments are computed based on the m data fragments. The m data fragments and n parity fragments located on different servers compose an erasure coding group. If the number of lost data fragments is equal to or less than n, the lost segments can be recovered based on the erasure coding algorithm. We recommend that you configure the value of m and n based on the number of servers. If you have 6 to 13 servers, we recommend that you set the values of both m and n to 2. If you have more than 14 servers, we recommend that you set the value of m to 8 and the value of n to 3.

**Triplicate**

Apsara Stack uses a flat design in which a linear address space is divided into slices called chunks. Each chunk is replicated into three copies stored on different data nodes of the storage cluster to ensure data reliability. Triplicate storage involves three types of key component: the master, chunk server, and client. Chunk servers are data nodes where chunk copies are stored. Each write operation is executed by the client in the following manner:
1. The client receives your write request and determines the chunk that corresponds to the
write operation by computing.
2. The client queries the master to find the chunk servers where the three copies of the chunk
are stored.
3. The client sends write requests to the chunk servers returned from the master.
4. If the write operation succeeds on all three chunk copies, the client returns a success.
Otherwise, the client returns a failure. The master ensures that the copies of each chunk are distributed on different chunk servers across different racks. This prevents data unavailability caused by the failure of a single chunk server or rack. The distribution strategy of the master takes many factors of the storage system into account, such as chunk server disk usage, chunk server distribution across racks, power distribution conditions, and node workloads.

**Comparison between EC and triplicate storage**

Compared with triplicate storage, EC is a better solution in terms of storage usage and data reliability.

| Item | EC | Triplicate storage |
|---|---|---|
| Storage usage | m/(m+n) . For example, the storage usage in EC storage of the 8+3 configuration can be calculated in the following method: 8/(8+3)=72.7% | 1/3=33.3% |
| Reliability | Handles the loss of up to n fragments. Failures on up to n servers can be handled in the worst case. For example, when m is 8 and n is 3, failures on up to three servers can be handled. | Handles the loss of up to two replicas. Failures on up to two servers can be handled in the worst case. |

##### 1.1.3.2 Resource isolation

Object Storage Service (OSS) slices user data and discretely stores the sliced data in a distributed file system based on specific rules. The user data and its indexes are stored separately. OSS uses symmetric AccessKey pairs to authenticate users and verifies the signature in each HTTP request sent by users. If verification is successful, OSS reassembles the distributed data. This way, OSS implements data storage isolation between different tenants.

##### 1.1.3.3 Disaster recovery

Object Storage Service (OSS) provides multiple disaster recovery types to ensure data security and improve availability. To ensure your data security, OSS provides the following disaster recovery types.

| Type | Description |
|---|---|
| Zone-disaster recovery | Zone-disaster recovery allows you to store multiple replicas of your data in multiple zones within the same region. This feature protects your data from being lost and helps you recover your business when a single zone fails. |
| CRR | Cross-region replication (CRR) provides automatic and asynchronous (near real-time) replication of objects across buckets in different OSS regions. Operations such as creating, overwriting, and deleting objects can be synchronized from a source bucket to a destination bucket. |
| Cross-cloud replication | You can use cross-cloud replication to replicate data from a cloud to another cloud. This way, you can back up data in a cloud. When a cloud fails, you can switch over your business to another cloud to ensure business continuity. |
| Three data centers across two regions | If your business has high requirements on data backup, you can use zone-disaster recovery and cross-region replication to build a disaster recovery solution based on three data centers across two regions. |

##### 1.1.3.4 Access permissions and account authorization

**authorization**

By default, the access control list (ACL) of Object Storage Service (OSS) resources, including buckets and objects, is set to private to ensure data security. Only the bucket owner and authorized users can access these resources. OSS allows you to configure a variety of policies to grant third-party users specific permissions to access or use your OSS resources. OSS provides the following access permission policies.

| Policy | Description |
|---|---|
| RAM Policy | Resource Access Management (RAM) is a service provided by Alibaba Cloud to manage access permissions on resources. RAM policies are configured based on users. You can manage users by configuring RAM policies. For users such as employees, systems, or applications, you can control which resources are accessible. For example, you can create a RAM policy to grant users only read permissions on a bucket. |
| Bucket Policy | A bucket policy is a resource-based authorization policy. Compared with RAM policies, bucket policies can be easily configured by using GUI in the console. In addition, the owner of a bucket can configure bucket policies for the bucket without RAM permissions. You can configure bucket policies to grant permissions to the RAM users of other Apsara Stack accounts or anonymous users who access OSS by using the specified IP addresses. |
| Bucket ACL | You can configure the ACL of a bucket when you create the bucket or modify the ACL of a created bucket. Only the owner of a bucket can configure or modify the ACL of the bucket. You can set the ACL of a bucket to one of the following values: Public Read/Write, Public-Read, and Private. |
| Object ACL | You can also configure the ACL of each object stored in OSS. You can configure the ACL of an object when you upload the object or modify the ACL of an uploaded object based on your requirements. You can set the ACL of an object to one of the following values: Inherited from bucket, Public Read/Write, Public-Read, and Private. |
| Hotlink protection | You can configure a Referer whitelist for a bucket to prevent your resources in the bucket from unauthorized access. |
| CORS | Cross-origin resource sharing (CORS) is a standard cross-origin solution provided by HTML5 to allow web application servers to control cross- origin access, which ensures the security of data transmission across origins. |

##### 1.1.3.5 Server-side encryption

Object Storage Service (OSS) supports server-side encryption. When you upload an object to a bucket for which server-side encryption is enabled, OSS encrypts the object and stores the encrypted object. When you download the encrypted object from OSS, OSS automatically decrypts the object and returns the decrypted object to you. In addition, a header is added in the response to indicate that the object is encrypted on the OSS server.

**Encryption methods**

OSS protects static data by using server-side encryption. You can use this method in scenarios in which additional security or compliance is required, such as the storage of deep learning samples and online collaborative documents. You can use SSE-OSS to encrypt all your objects. To improve security, OSS uses master keys that are rotated on a regular basis to encrypt data keys. You can use this method to encrypt and decrypt multiple objects at a time.

**Server-side encryption by using OSS-managed keys**

OSS generates and manages data keys used to encrypt data, and provides strong and multifactor security measures to protect data. OSS server-side encryption uses AES-256, which is one of the advanced encryption standard algorithms, and SM4, which is one of the Chinese cryptographic algorithms. Use the following configuration methods: Configure the default server-side encryption method for a bucket Set the default encryption method to SSE-OSS and specify the encryption algorithm as AES- 256 . This way, all objects uploaded to this bucket are encrypted. Configure an encryption method for a specific object When you upload an object or modify the metadata of an object, include the `x-oss-server-`

| side-encryption |   |   |
|---|---|---|
|   | SM4 | . This way, |

`side-encryption` parameter in the request and set the parameter value to `AES-265` or `SM4` . This way, the object is encrypted by using SSE-OSS.

##### 1.1.3.6 Client-side encryption

Client-side encryption is performed to encrypt objects on the local client before the objects are uploaded to Object Storage Service (OSS).

**Disclaimer**

When you use client-side encryption, you must ensure the integrity and validity of the customer master key (CMK). If the CMK is incorrectly used or lost due to improper key management, you are responsible for all losses and consequences caused by decryption failures. When you copy or migrate encrypted data, you are responsible for the integrity and validity of the object metadata related to client-side encryption. If the encrypted metadata is incorrectly used or lost due to improper maintenance, you are responsible for all losses and consequences caused by decryption failures.

**Encryption**

In client-side encryption, a random data key is generated for each object to perform symmetric encryption on the object. The client uses a CMK to generate a random data encryption key. The encrypted data key is uploaded as a part of the object metadata and stored in the OSS server. When an encrypted object is downloaded, the client uses the CMK to decrypt the random data key and then uses the data key to decrypt the data of the object. The CMK is used only on the client and is not transmitted over the network or stored in the server, which ensures data security.

**Use customer-managed CMK**

To use this method for client-side encryption, you must generate and manage CMKs by yourself. When you implement client-side encryption on an object to upload, you must upload a symmetric or asymmetric CMK to the client. The following figure shows the specific encryption process. Encrypt and upload an object i. You must provide the client with a symmetric or asymmetric CMK. ii. The client uses the CMK to generate a one-time symmetric data key that is used only to encrypt the current object to upload. The client generates a random and unique data key for each object to upload. iii. The client uses the data key to encrypt the object to upload and uses the CMK to encrypt the data key. iv. The encrypted data key is included in the metadata of the uploaded object in OSS. Download and decrypt an object i. The client downloads an encrypted object. The encrypted data key is included in the metadata of the object. ii. The client uses the object metadata information to determine the CMK used to generate the data key and uses this CMK to decrypt the encrypted data key. Then, the client uses the decrypted data key to decrypt the object.

**Important**

CMKs and unencrypted data are not sent to OSS. Therefore, keep your CMKs secure. If a CMK is lost, objects encrypted by using the data keys generated by this CMK cannot be decrypted. Data keys are randomly generated by the client.

**Usage notes**

To perform client-side encryption on objects that are larger than 5 GB in size before you upload the objects, you must use multipart upload. When you use multipart upload to upload an object, you must specify the total size of the object and the size of each part. The size of each part except for the last part must be the same and be a multiple of 16 bytes. After you upload objects encrypted on the client, object metadata related to client-side encryption is protected. In this case, CopyObject cannot be called to modify object metadata.

#### 1.1.4 Data processing

##### 1.1.4.1 IMG

You can add Image Processing (IMG) parameters to GetObject requests to process image objects stored in Object Storage Service (OSS). For example, you can add image watermarks to images or convert image formats. OSS allows you to use one or more parameters to process images, or encapsulate multiple IMG parameters in a style to process images. When multiple IMG parameters are included in a request, OSS processes the image in the order of the parameters. You can use object URLs, API operations, and OSS SDKs to process images. The following table describes the IMG operations supported by OSS.

| IMG operation | Parameter | Description |
|---|---|---|
| Resize images | resize | Resizes images to a specified size. |
| Incircle | circle | Crops images based on the center point of images to rounds of a specified size. |
| Custom crop | crop | Crops images to rectangles of a specified size. |
| Indexed cut | indexcrop | Cuts images along a specified horizontal or vertical axis and selects one of the cut images. |
| Rounded rectangle | rounded- corners | Crops images to rounded rectangles based on the specified rounded corner size. |
| Automatic rotation | auto-orient | Auto-rotates images for which the auto-orient parameter is configured. |
| Rotate | rotate | Rotates images clockwise at a specified angle. |
| Blur | blur | Blurs images. |
| Adjust brightness | bright | Adjusts the brightness of images. |
| Sharpen | sharpen | Sharpens images. |
| Adjust contrast | contrast | Adjusts the contrast of images. |
| Gradual display | interlace | Configures gradual display for the JPG images. |
| Adjust image quality | quality | Adjusts the quality of JPG and WebP images. |
| Convert format | format | Converts image formats. |
| Add watermarks | watermark | Adds image or text watermarks to images. |
| Query average tone | average-hue | Queries the average tone of images. |
| Query image information | info | Queries image information, including basic information and Exchangeable Image File Format (EXIF) information. |

##### 1.1.4.2 Video snapshots

This topic describes the parameters that you can configure to capture video snapshots and provides examples.

**Usage notes**

When you capture video snapshots, you are charged based on the number of captured images. Object Storage Service (OSS) can capture images from video objects only in the H.264 and H.265 formats. By default, OSS does not automatically store captured images. You must manually download the captured images to your local storage devices.

**Parameters**

Operation type: `video` Operation name: **snapshot**

| Para met er | Description | Valid value |
|---|---|---|
| t | Specifies the time when the image is to be captured. | [0, video duration] Unit: ms |
| w | Specifies the width based on which to capture the image. If this parameter is set to 0, the width of the image to capture is automatically calculated. | [0, video width] Unit: px |
| h | Specifies the height based on which to capture the image. If this parameter is set to 0, the height of the image to capture is automatically calculated. If both w and h are set to 0, the width and height of the source image are used as those of image to capture. | [0, video height] Unit: px |
| m | Specifies the mode used to capture the image. If this parameter is not specified, the image is captured in the default mode. In other words, the image at the specified point of time in the video is captured. If this parameter is set to fast, the most recent key frame before the specified time is captured. | fast |
| f | Specifies the format of the captured image. | jpg and png |
| ar | Specifies whether to automatically rotate the image based on the video information. If this parameter is set to auto, the system automatically rotates the image based on the video information. | auto |

**Examples**

Use the fast mode to capture the image at the seventh second of the video. Export the captured image as a JPG image with the width of 800 px and height of 600 px. The URL of the processed image is in the following format: <Source video URL>?x-oss-

```
process=video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
```

Use the default mode to capture the image at the fiftieth second of the video accurately. Export it as a JPG image with the width of 800 px and height of 600 px. The URL of the processed image is in the following format: <Source video URL>?x-oss-

```
process=video/snapshot,t_50000,f_jpg,w_800,h_600
```

## 2 Usage notes

Before you use OSS, you must understand the following content: To allow other users to use all or part of OSS features, you must create RAM users and grant permissions to the users by configuring RAM policies. Before you use OSS, you must also understand the following limits.

| Item | Limit |
|---|---|
| Bucket | You can create up to 100 buckets. After a bucket is created, its name and region cannot be modified. |
| Upload objects | Objects larger than 5 GB cannot be uploaded by using the following modes: console upload, simple upload, form upload, or append upload. To upload an object that is larger than 5 GB, you must use multipart upload. The size of an object uploaded by using multipart upload cannot exceed 48.8 TB. If you upload an object that has the same name of an existing object in OSS, the new object will overwrite the existing object. |
| Delete objects | Deleted objects cannot be recovered. You can delete up to 100 objects at a time in the OSS console. To delete more than 100 objects at a time, you must call an API operation or use an SDK. |
| Lifecycle | You can configure up to 1,000 lifecycle rules for each bucket. |

## 3 Quick start

### 3.1 Log on to the OSS console

This topic describes how to log on to the Object Storage Service (OSS) console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

**Note**

You can click the current language in the upper-right corner to switch to another language. 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击右上角的**浏览**
**器证书安装**，可打开浏览器证书安装指南。
2. Enter your username and password.
Obtain the username and password from an operations administrator.

**Note**

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forget password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**You log on to the Apsara Uni-manager Management Console for the first time**

**after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For information about how to bind and enable MFA, see **Manage MFA** in **Apsara**
**Uni-manager Management Console User Guide**.
5. In the top navigation pane, choose **Products > Object Storage Service**.

### 3.2 Create buckets

Objects uploaded to OSS are stored in a bucket. You must create a bucket before you upload objects to OSS.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click **Create Bucket**.
3. On the **Create OSS Bucket** page, configure parameters.
The following table describes the parameters that you can configure.

| Parameter | Description |
|---|---|
| Organization | Select an organization from the drop-down list for the bucket. |
| Resource Set | Select a resource set from the drop-down list for the bucket. |
| Region | Select a region from the drop-down list for the bucket. Note The region of a bucket cannot be changed after the bucket is created. If you want to access OSS from your ECS instance through the internal network, select the same region where your ECS instance is deployed. |
| Cluster | Select a cluster for the bucket. |
| Bucket Name | Enter the name of the bucket. Note The bucket name must comply with the naming conventions. The bucket name must be globally unique among all existing buckets in OSS. The bucket name cannot be changed after the bucket is created. |
| Storage Class | Set the value to Standard. Only Standard is supported. |
| Bucket Capacity | Specify the capacity of the bucket. Valid values: 0 to 2000000. Unit: TB or GB. |

| Access Control List (ACL) | Set the ACL of the bucket. You can select the following options: Private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access objects in the bucket without authorization. Public Read: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users can only read objects in the bucket. Public Read/Write: All users, including anonymous users can read and write objects in the bucket. Fees incurred by such operations are paid by the owner of the bucket. Exercise caution when you configure this option. Note You can modify the ACL of a bucket after the bucket is created. For more information, see Modify bucket ACLs. |
|---|---|
| Server-Side Encryption | Configure server-side encryption for the bucket. You can select the following options: None: Server-side encryption is not performed. AES256: AES256 is used to encrypt each object in the bucket using different data keys. Customer master keys (CMKs) used to encrypt the data keys are rotated regularly. |

4. Click **Submit**.

### 3.3 Upload objects

After you create a bucket, you can upload objects to it.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

You can upload an object of any format to a bucket. You can use the OSS console to upload an object up to 5 GB in size. To upload an object larger than 5 GB, use OSS SDKs or call an API operation.
1. Log on to the OSS console.
2. Click Buckets. On the Buckets page that appears, click the name of the bucket to which you
want to upload objects.
3. On the bucket details page that appears, click **Files**.
4. Click **Upload**.
5. In the **Upload** panel, set the parameters described in the following table.

| Parameter | Description |
|---|---|

| Upload To | Set the directory to which you want to upload objects. Current: Objects are uploaded to the current directory. Specified: Objects are uploaded to the specified directory. You must enter the directory name. If the specified directory does not exist, OSS automatically creates the specified directory and uploads the object to the directory. |
|---|---|
| File ACL | Set the access control list (ACL) of the object to upload. Default value: Inherited from Bucket. Inherited from Bucket: The ACL of uploaded objects is the same as that of the bucket. Private: Only the owner or authorized users can read and write objects in the bucket. Other users, which includes anonymous users, cannot access the objects in the bucket without authorization. Public Read: Only the bucket owner can perform write operations on objects in the bucket. Other users, which includes anonymous users, can perform only read operations on objects in the bucket. Public Read/Write: All users, which includes anonymous users, can read and write objects in the bucket. |
| Upload | Drag one or more files to upload to this section, or click Upload to select one or more files to upload. Important When the object to upload has the same name as an existing object in the bucket, the existing object is overwritten. If you upload a directory, only the files in the directory are uploaded, and the files are stored in the same directory in the bucket. The name of an uploaded object must comply with the following conventions: The name must be encoded in UTF-8. The name is case-sensitive. The name must be 1 to 1,023 bytes in length. The name cannot start with a forward slash (/) or backslash (\). |

6. In the **Upload Tasks** panel, wait until the upload task is completed.
During the upload process, you can click **Cancel All** to cancel the task. After the task is completed, click **Removed** to remove the task.

**Important**

Do not refresh or close the **Upload Tasks** panel when objects are being uploaded. Otherwise, the upload tasks are interrupted.

### 3.4 Obtain object URLs

You can obtain the URL of an uploaded object in Object Storage Service (OSS) and share the URL with other users to preview or download the object.

**Prerequisites**

An object is uploaded to the bucket. For more information, see Upload objects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Files** tab.
4. Obtain object URLs.
Obtain the URL of a single object. Click the name of the object whose URL you want to obtain, or click **View Details** in the Actions column that corresponds to the object. In the **View Details** panel, click **Copy**
**File URL**.
Batch export URL lists. Select the objects that you want to share. Choose **Batch Operation > Export URL List**.

## 4 Buckets

### 4.1 View bucket information

You can view the detailed information about created buckets in the Object Storage Service (OSS) console.

**Prerequisites**

A bucket is created. For more information, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. On the **Overview** tab, you can view the information about the bucket, which includes
Organization and Resource Set, Domain Names, and Basic Settings.

### 4.2 Delete buckets

You can delete a bucket in the Object Storage Service (OSS) console.

**Prerequisites**

All objects and parts in the bucket are deleted. For more information, see Delete objects and Manage parts.

**Warning**

Deleted objects, parts, and buckets cannot be recovered. Exercise caution when you delete objects, parts, and buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. In the upper-right corner, click **Delete Bucket**.
4. In the message that appears, click **OK**.

### 4.3 Modify bucket ACLs

Object Storage Service (OSS) provides access control list (ACL) to control access to buckets. By default, the ACL of a bucket is private. You can modify the ACL of a bucket after the bucket is created.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

You can set the ACL of a bucket to one of the following values: Private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users, cannot access the objects in the bucket without authorization. Public Read: Only the owner or authorized users of this bucket can write objects in the bucket. Other users, including anonymous users, can only read the objects in the bucket. Public Read/Write: Any users, including anonymous users, can read and write the objects in the bucket.

**Warning**

If you set the ACL of a bucket to Public Read or Public Read/Write, other users can read the data in the bucket without authentication, which may result in security risks. To ensure the security of your data, we recommend that you set the ACL of your bucket to private.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Basic Settings** tab. Find the **Access Control List (ACL)** section.
4. Click **Configure**. Modify the bucket ACL.
5. Click **Save**.

### 4.4 Configure static website hosting

**hosting**

You can configure static website hosting for a bucket in the Object Storage Service (OSS) console so that users can access the website by using the domain name of the bucket.

**Prerequisites**

A bucket is created. For more information, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Basic Settings** tab. Find the **Static Pages** section.
4. Click **Configure** and then set the parameters described in the following table.

| Parameter | Description |
|---|---|
| Default Homepage | Specify an index page that functions similar to index.html. Only HTML objects can be specified as the index page. If you do not specify this parameter, static website hosting is disabled. |
| Default 404 Page | Set the default 404 page that is displayed when the requested resource does not exist. Only HTML, JPG, PNG, BMP, or WebP objects in the root directory of the bucket can be set to the default 404 page. If you do not specify this parameter, Default 404 Page is disabled. |

5. Click **Save**.

### 4.5 Configure hotlink protection

You can configure hotlink protection for a bucket in the Object Storage Service (OSS) console to prevent data in your bucket from being accessed by unauthorized domain names.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

The hotlink protection feature allows you to configure a Referer whitelist for a bucket. This way, only requests from domain names included in the Referer whitelist can access your data in the bucket. OSS allows you to configure Referer whitelists based on the Referer header field in HTTP or HTTPS requests. After hotlink protection is configured for a bucket, OSS verifies requests to objects in the bucket only when the requests are initiated by using signed URLs or from anonymous users. Requests that contain the Authorization field in the header are not verified.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Basic Settings** tab. Find the **Hotlink Protection** section.
4. Click **Configure** and configure the following parameters:
Enter domain names or IP addresses in the **Referer Whitelist** field. Separate multiple Referers by using line feed. You can use asterisks (*) and question marks (?) as wildcards. Examples: If you add www.example.com to the Referer whitelist, requests sent from URLs that start with www.example.com, such as www.example.com/123 and www.example.com.cn are allowed. If you add *www.example.com/ to the Referer whitelist, requests sent from http://www.example.com/ and https://www.example.com/ are allowed. An asterisk (*) can be used as a wildcard to indicate zero or more characters. For example, if you add *.example.com to the Referer whitelist, requests sent from URLs such as help.example.com and www.example.com are allowed. A question mark (?) can be used as a wildcard to indicate a single character. For example, if you add example?.com to the Referer whitelist, requests sent from URLs such as examplea.com and exampleb.com are allowed. You can add domain names or IP addresses that include a port number, such as www.example.com:8080 and 10.10.10.10:8080, to the Referer whitelist. Select whether to turn on **Allow Empty Referer** to allow requests in which the Referer field is empty. An HTTP or HTTPS request with an empty Referer field indicates that the request does not contain the Referer field or the value of the Referer field is empty. If you do not allow empty Referers fields, only HTTP or HTTPS requests which include an allowed Referer field can access the objects in the bucket.

**Note**

By default, if you use the bucket endpoint to preview an MP4 object, the browser sends a request that contains the Referer field and a request that does not contain the Referer field at the same time. Therefore, to allow access to the MP4 objects in your bucket, you must not only add the bucket endpoint to the Referer whitelist but also allow empty Referer fields. To preview a non-MP4 object by using the bucket domain name, you need only to allow empty Referer fields.
5. Click **Save**.

### 4.6 Configure CORS

You can configure cross-origin resource sharing (CORS) in the Object Storage Service (OSS) console to enable cross-origin access.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

OSS provides CORS over HTML5 to implement cross-origin access. When OSS receives a cross-origin request (or an OPTIONS request) for a bucket, OSS reads the CORS rules of the bucket and checks the relevant permissions of the request. OSS matches the request with the rules one by one. When OSS finds the first match, OSS returns a corresponding header in the response. If no match is found, OSS does not include any CORS header in the response.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Basic Settings** tab. In the **Cross-Origin Resource Sharing (CORS)** section,
click **Configure**.
4. On the page that appears, click **Create Rule**. Then, in the **Create Rule** panel, configure
the parameters in the following table.

| Parameter | Required | Description |
|---|---|---|
| Sources | Yes | Specify the sources from which you want to allow cross-origin requests. Take note of the following items when you configure the sources: You can configure multiple rules for sources. Separate multiple rules with line feeds. The domain names must include the protocol name, such as HTTP or HTTPS. Asterisks (*) are supported as wildcards. Each rule can contain up to one asterisk (*). A domain name must include the port number if the domain name does not use the default port. Example: https://www.example.com:8080. The following examples show how to configure domain names: To match a specified domain name, enter the full domain name. Example: https://www.example.com. Use an asterisk (*) as a wildcard in the domain name to match second-level domains. Example: https://*.example.com. Enter only an asterisk (*) as the wildcard to match all domain names. |

| Allowed Methods | Yes | Select the cross-origin request methods that are allowed. |
|---|---|---|
| Allowed Headers | No | Specify the response headers for the allowed cross-origin requests. Take note of the following rules when you configure the allowed response headers: This parameter is in the key:value format and case-insensitive. Example: content- type:text/plain. You can configure multiple rules for allowed headers. Separate multiple rules with new lines. Each rule can contain up to one asterisk (*) as the wildcard. We recommend that you set this parameter to an asterisk (*) if you do not have special requirements. |
| Exposed Headers | No | Specify the response headers for allowed access requests from applications, such as an XMLHttpRequest object in JavaScript. Exposed headers cannot include asterisks (*). |
| Cache Timeout (Seconds) | No | Specify the period of time within which the browser can cache the response for an OPTIONS preflight request to a specific resource. Unit: seconds. |

**Note**

You can configure up to 10 CORS rules for each bucket.
5. Click **OK**.

### 4.7 Configure lifecycle rules

You can configure a lifecycle rule for a bucket to regularly delete expired objects and parts to save storage costs.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

Take note of the following items when you configure lifecycle rules for a bucket: After a lifecycle rule is configured, it is loaded within 24 hours and takes effect within 24 hours after it is loaded. Check the configurations of a rule before you save the rule. Objects that are deleted based on lifecycle rules cannot be recovered. Configure lifecycle rules based on your requirements. You can configure up to 100 lifecycle rules for each bucket in the Object Storage Service (OSS) console and up to 1,000 lifecycle rules for each bucket by using ossutil.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure lifecycle rules.
3. Click the **Basic Settings** tab. Find the **Lifecycle** section. Click **Configure**.
4. Click **Create Rule**. In the **Create Rule** panel that appears, configure the parameters
described in the following table.

| Parameter | Description |
|---|---|
| Status | Specify the status of the lifecycle rule. Valid values: Enabled and Disabled. |
| Applied To | Select objects to which the rule applies. You can selectF iles with Specified Prefix or Whole Bucket. Files with Specified Prefix indicates that this rule applies to objects whose names contain a specified prefix. Whole Bucket indicates that this rule applies to all objects in the bucket. Note If you select Files with Specified Prefix, you can configure different lifecycle rules for objects whose names contain different prefixes. If you select Whole Bucket, only one lifecycle rule can be configured for the bucket. |
| Prefix | If you set Applied To to Files with Specified Prefix, you must specify the prefix of the objects to which the rule applies. For example, if you want that the rule applies to objects whose names start with img, enter img . |
| File Lifecycle | Configure rules for objects to specify when objects expire. You can set File Lifecycle to Validity Period (Days), Expiration Date, or Disabled. If you select Disabled, the configurations of File Lifecycle do not take effect. |
| Delete | Specify when objects expire based on Validity Period (Days) or Expiration Date that you set for File Lifecycle. After objects expire, the objects are deleted. Validity Period (Days): Specify the number of days to retain objects after they are last modified. Select the check box next to Delete and specify a number such as N. The objects expire N days after they are last modified. Then, the objects are deleted the next day after they expire. For example, if you specify the number as 30, objects that are last modified on January 1,2019 are deleted on February 1, 2019. Expiration Date: Specify the expiration date. Select the check box next to Delete and set an expiration date. The objects that are last modified before this date expire and are deleted. For example, if you set Expiration Date to January 1, 2019, objects that are last modified before January 1, 2019 are deleted. |
| Part Lifecycle | Specify the operations to perform on expired parts. You can set Part Lifecycle to Validity Period (Days), Expiration Date, or Disabled. If you select Disabled, the configurations of Part Lifecycle do not take effect. Important You must configure at least one of File Lifecycle and Part Lifecycle. |
| Delete Parts | Specify when parts that match the rule expire based onV alidity Period (Days) or Expiration Data that you set for Part Lifecycle. Expired parts are deleted. You can configure this parameter in the same way as you configure the Delete parameter in Clear Policy. |

5. Click **OK**.

### 4.8 Configure storage quota

If the capacity of a bucket reaches the specified storage quota, write operations such as PutObject, MultipartUpload, CopyObject, PostObject, and AppendObject cannot be performed on the bucket. This topic describes how to configure the storage quota of a bucket in Object Storage Service (OSS).

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

Take note of the following items when you configure the storage quota of a bucket: Before you configure the storage quota of a bucket, make sure that the quota does not limit your business because write operations cannot be performed if the bucket capacity reaches the specified quota. In general, it takes about an hour for OSS to determine whether the bucket capacity exceeds the storage quota. In some cases, it can take longer than one hour.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure storage quota.
3. Click the **Basic Settings** tab and find the **Storage Quota** section.
4. Click **Configure**.
5. On the **Modify OSS Bucket** page, modify the storage quota of the bucket.
Units: TB or GB. Valid values: -1 to 2000000 The default value is -1, which indicates that the bucket capacity is not limited.
6. Click **Submit**.
After you submitted, you can click **Back to Console** in the pop-up dialog box to go back to the **Overview** page.

### 4.9 Configure cluster-disaster recovery

**recovery**

In cluster-disaster recovery mode, buckets with the same name are replicated. Cluster-based disaster recovery is automatically enabled based on configurations made when the cluster is created. In other words, after a primary bucket is created, a secondary bucket with the same name is automatically created. Information stored in the primary bucket is automatically synchronized to the secondary bucket. By default, Cluster-disaster Recovery is turned on for buckets that are created by using the Object Storage Service (OSS) console.

**Prerequisites**

A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Buckets. On the Buckets page, click the name of the
bucket to go to the bucket details page.
3. On the bucket details page, click the **Basic Settings** tab. Find the **Cluster-disaster**
**Recovery** section.
4. Click **Configure**. Turn on or turn off **Cluster-disaster Recovery**.
5. Click **Save**.

### 4.10 Bucket tagging

Object Storage Service (OSS) allows you to configure bucket tagging to classify and manage buckets. For example, you can use this feature to list buckets that have specific tags and configure access control lists (ACLs) for buckets that have specific tags.

**Background information**

The bucket tagging feature uses a key-value pair to identify a bucket. You can add tags to buckets that are used for different purposes and manage the buckets by tags. Only the bucket owner or authorized Resource Access Management (RAM) users can configure tagging for the bucket. Otherwise, 403 Forbidden is returned with the AccessDenied error code. You can configure up to 20 tags for a bucket. The tag key is required. The tag key can be up to 64 Bytes in length and cannot start with `http://` , `https://` , or `Aliyun` . The tag value is optional. The tag value can be up to 128 bytes in length. You can leave the parameter empty. The key and value of a tag must be encoded in UTF-8.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure tagging.
3. Choose **Basic Settings > Bucket Tagging**.
4. Click **Configure**.
5. Add tags to the bucket based on the naming conventions. You can click the **+** icon to add
multiple tags to a bucket.
6. Click **Save**.

### 4.11 Configure server-side encryption

**encryption**

OSS supports server-side encryption. When you upload an object to a bucket for which server-side encryption is enabled, OSS encrypts the object and stores the encrypted object. When you download the encrypted object from OSS, OSS automatically decrypts the object and returns the decrypted object to you. A header is added in the response to indicate that the object is encrypted on the OSS server.

**Context**

OSS supports the following encryption methods:

**Context**

Server-side encryption by using KMS (SSE-KMS) OSS uses the default customer master key (CMK) managed by KMS or a specified CMK to encrypt objects. The CMK is managed by KMS to ensure confidentiality, integrity, and availability at minimal costs. Server-side encryption by using OSS-managed keys (SSE-OSS) OSS uses data keys to encrypt objects and manages the data keys. In addition, OSS uses master keys that are regularly rotated to encrypt data keys. You can enable server-side encryption in the OSS console by using one of the following methods: Method 1: Enable server-side encryption when you create a bucket Method 2: Enable server-side encryption on the Basic Settings tab

**Method 1: Enable server-side encryption when you create a**

**bucket**

1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click **Create Bucket**.
3. On the **Create OSS Bucket** page, set parameters.
You can set the following parameters to configure server-side encryption for the bucket.
**Server-Side Encryption**: Specify the encryption methods.
**None**: Server-side encryption is not performed.
**AES256**: AES256 is used to encrypt each object in the bucket by using different data
keys. The CMKs used to encrypt the data keys are rotated regularly.
**KMS**: CMKs managed by KMS are used to encrypt objects in the bucket.
**Encryption Algorithm**: This parameter can be configured when you select **KMS** for
**Server-Side Encryption**.
**Key ID**: This parameter can be configured when you select **KMS** for **Server-Side**
**Encryption**. OSS uses the specified CMK to encrypt objects in the bucket.

**Note**

To select a CMK ID for server-side encryption, you must create the CMK in the KMS console.
4. Click **Submit**.

**Method 2: Enable server-side encryption on the Basic Settings**

**tab**

1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure server-side encryption.
3. Click the **Basic Settings** tab. Find the **Server-side Encryption** section.
4. Click **Configure** and set the following parameters:
**Encryption Method**: Specify the encryption method.
**None**: Server-side encryption is not performed.
**OSS-Managed**: Keys managed by OSS are used to encrypt your data.
**KMS**: CMKs managed by KMS are used to encrypt objects in the bucket.
**CMK**: This parameter can be configured when you select **KMS** for **Encryption Method**.
OSS uses the specified CMK to encrypt objects in the bucket.

**Note**

To select a CMK ID for server-side encryption, you must create the CMK in the KMS console.
5. Click **Save**.

**Important**

The configurations of the default encryption method for a bucket do not affect the encryption configurations of existing objects within the bucket.

### 4.12 Bind a bucket to a VPC

You can bind your bucket to a specified virtual private cloud (VPC) to allow only requests from IP addresses within the VPC to access your bucket.

**Prerequisites**

A VPC is created. For more information, see the "Create a VPC" chapter of VPC User Guide.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket that you want to bind to the VPC network.
3. Click the Overview tab. Click **Bind VPC** in the **VPC Info** section.
4. On the Bind VPC page, select the VPC that you create.
You can also click **Create VPC** to create a new VPC.
5. Click **Submit**.

### 4.13 Configure CRR rules

Cross-region replication (CRR) allows you to automatically and asynchronously (in near realtime) replicate Object Storage Service (OSS) objects from a bucket in a region to another bucket in another region. CRR also allows you to replicate operations, such as the creation, overwriting, and deletion of objects, from a source bucket to a destination bucket.

**Prerequisites**

The source bucket and destination bucket are created. For more information, see Create a bucket.

**Background information**

CRR can help you meet compliance requirements for cross-region disaster recovery or data replication. Objects in the destination bucket are exact replicas of objects in the source bucket. The objects have the same object names, object content, and object metadata, such as the creation time, owner, user metadata, and access control lists (ACLs).
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure a CRR rule.
3. On the bucket details page, click the **Basic Settings** tab. Find the **Cross-Region**
**Replication** section.
4. Click **Enable**. In the **Cross-Region Replication** panel, configure the parameters described
in the following table.

| Parameter | Description |
|---|---|
| Source Region | The region in which the current bucket is located. |
| Source Bucket | The name of the current bucket. |
| Destination region | The region in which the destination bucket is located. The source and destination buckets for CRR must be located in different regions. You cannot configure a CRR rule to replicate data between buckets that are located in the same region. |
| Destination Bucket | The destination bucket to which you want to replicate data. The source and destination buckets specified in a CRR rule are not allowed to be specified in other CRR rules. For example, if you configure a CRR rule to replicate data from Bucket A to Bucket B, Bucket A and Bucket B are not allowed to be configured in other CRR rules. |
| Applied To | The objects that you want to replicate to the destination bucket. Valid values: All Files in Source Bucket: All objects in the source bucket are replicated to the destination bucket. Files with Specified Prefix: Only objects whose names contain one of the specified prefixes are replicated to the destination bucket. For example, if you have a subdirectory named management/ in the root directory of the source bucket and want to replicate objects in a subdirectory named abc/ in management/, you can set the prefix to management/abc/ . You can specify up to 10 prefixes. |
| Operations | The operations that you want to replicate. Valid values: Add/Change: OSS replicates only object creation and update operations from the source bucket to the destination bucket. Add/Delete/Change: OSS replicates object creation, update, and deletion operations from the source bucket to the destination bucket. |

| Replicate Historical Data | Specifies whether to replicate historical data (data that exists in the source bucket before you enable CRR) to the destination bucket. Yes: OSS does not replicate historical data to the destination bucket. Important When historical data is replicated, objects that are replicated from the source bucket may overwrite objects that have the same names in the destination bucket. To prevent data loss, we recommend that you enable versioning for the source and destination buckets. No: OSS replicates only objects that are uploaded or updated after the CRR rule takes effect to the destination bucket. |
|---|---|

5. Click **Confirm**.

**Note**

After you configure a CRR rule, the replication task starts in 3 to 5 minutes. Then, you can view the replication progress. In CRR, data is asynchronously replicated in near real time. The period of time that is required to replicate data from the source bucket to the destination bucket may range from a few minutes to a few hours, depending on the data size. If you want to replicate an object encrypted based on KMS from the source bucket to the destination bucket, KMS must be configured for the destination bucket. Otherwise, data replication fails.

### 4.14 Configure cross-cloud replication

**replication**

You can use the cross-cloud replication feature to synchronize Object Storage Service (OSS) data between two clouds. This topic describes how to configure cross-cloud replication.

**Step 1: Obtain the parameters of the destination cloud.**

Before you configure cross-cloud replication, you must obtain the required parameters of the destination cloud.
1. Log on to the Apsara Uni-manager Operations Console of the destination cloud.
For more information about how to log on to the Apsara Uni-manager Operations console, see **Log on to the Apsara Uni-manager Operations console** in **Operations and**
**Maintenance Guide**.
2. In the left-side navigation pane, choose **Product Management > Products**.
3. Click **OSS O&M**.
4. In the left-side navigation pane, choose **Service O&M - OSS > Synchronization**
**Management > Cross-Cloud Synchronization**.
5. In the upper-right corner, select the destination cluster from the **Cluster** drop-down list,
and then click **View Parameters of the Current Cloud** . Record the information displayed in the **Parameters of the Current Cloud** dialog box.

**Step 2: Configure cross-cloud synchronization for the source**

**cloud.**

After you obtain the required parameters of the destination cloud, you must configure crosscloud synchronization for the source cloud in the Apsara Uni-manage Operations Console.
1. Log on to the Apsara Uni-manager Operations Console of the source cloud.
2. In the left-side navigation pane, choose **Product Management > Products**.
3. Click **OSS O&M**.
4. In the left-side navigation pane, choose **Service O&M - OSS > Synchronization**
**Management > Cross-Cloud Synchronization**.
5. In the upper-right corner, click **Create**. In the **Create Cross-Cloud Synchronization**
**Task** dialog box, add the obtained parameters of the destination cloud.
6. Click **Submit**.
Wait a few minutes until the cross-synchronization configurations take effect.

**Step 3: Configure cross-cloud replication in the Apsara Uni-**

**manager Management Console of the source cloud.**

After the cross-cloud synchronization configurations take effect, you must configure crosscloud replication in the Apsara Uni-manager Management Console.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure cross-cloud replication.
3. On the bucket details page, click the **Basic Settings** tab. In the **Cross-Cloud Replication**
section, click **Enable**.
4. In the **Cross-Cloud Replication** panel, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Source Region | The region in which the source bucket is located. |
| Source Bucket | The name of the source bucket. |
| Destination Cloud | Enter the name of the destination cloud obtained in Step 1. |
| Destination Cloud Address | Enter the value of Location of the destination cloud obtained in Step 1. |
| Destination Bucket | Enter the name of the destination bucket. |
| Applied To | Select the objects that you want to synchronize. All Files in Source Bucket: All objects within the source bucket are synchronized to the destination bucket. Files with Specified Prefix: Only objects whose names contain one of the specified prefixes are synchronized to the destination bucket. Click Add. You can add up to 10 prefixes. |

| Operations | Select a synchronization policy. Add/Change: Only newly added and changed data is synchronized from the source bucket to the destination bucket. Add/Delete/Change: All changes to data including creation, modification, and deletion of objects are synchronized from the source bucket to the destination bucket. |
|---|---|
| Replicate Historical Data | Specify whether to synchronize historical data that is generated before you enable cross-cloud replication. Yes: Historical data is synchronized to the destination bucket. No: Only objects that are uploaded or updated after cross-cloud replication is enabled are synchronized to the destination bucket. |

5. Click **OK** to save your settings.

### 4.15 Log management

#### 4.15.1 Configure logging

When you access Object Storage Service (OSS), a large number of access logs are generated. You can use the logging feature to store OSS access logs in a specified bucket.

**Prerequisites**

A bucket is created. For more information, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click the **Basic Settings** tab. Find the **Logging** section.
4. Click **Configure**. Turn on the **Logging** switch. Select **Destination Bucket** and set **Log**
**Prefix**.
**Destination Bucket**: Select the bucket in which you want to store access logs from the
drop-down list. You must be the owner of the selected bucket, and the selected bucket must be in the same region as the bucket for which logging is enabled.
**Log Prefix**: Enter the prefix and directory where the access logs are stored. If you
specify `log/<TargetPrefix>` as the prefix, access logs are stored in the log/ directory.
5. Click **Save**.

#### 4.15.2 Real-time log query

A large number of logs are generated when Object Storage Service (OSS) resources are accessed. OSS uses Log Service to help you query and collect statistics for OSS access logs and audit access to OSS in the OSS console, track exception events, and troubleshoot problems. This helps you improve work efficiency and make informed decisions.

**Benefits**

Pushes logs to Log Service within three minutes and allows you to view real-time logs in the OSS console. Provides log analysis and common analysis reports so that you can easily query data. Allows you to query and analyze raw logs in real time and filter logs by bucket name, object name, API operation, or time.

**Prerequisites**

Log Service is activated and is authorized to access OSS.

**Enable real-time log query**

**Important**

After you enable real-time log query for a bucket for the first time, you must wait for about one minute and then refresh the page to use this feature. When you enable real-time log query, the system creates Log Service projects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click Logging and then click **Real-time Log Query**. On the Real-time Log Query tab, click
**Activate Now**.

**Specify the retention period of logs**

By default, logs are retained for seven days. You can modify the retention period based on your business requirements.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click Logging and then click **Real-time Log Query**. On the Real-time Log Query tab, click
**Config Log Retention Time**.
4. In the **Config Log Retention Time** dialog box, modify the retention time. Then, click **OK**.
Data can be retained for 7 to 3,000 days.

**Query real-time logs**

OSS uses Log Service to help you query and collect statistics for OSS access logs and audit access to OSS in the OSS console, track exception events, and troubleshoot problems. This helps you improve work efficiency and make informed decisions. Method 1: Query real-time logs on the **Original Log** tab i. Log on to the OSS console. ii. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the bucket that you want to manage. iii. Click Logging and then click **Real-time Log Query**. On the Real-time Log Query tab, click the **Original Log** tab and enter the query condition. A query condition consists of a query statement and an analytic statement in the `query`

| statement \| analytic statement |   |
|---|---|
|   | . The query stat |

statement | analytic statement format. Example: * | SELECT status, count(*) AS PV `GROUP BY status` . The query statement and the analytic statement are separated by a vertical bar (|). The query statement uses proprietary syntax of Log Service. A query statement can be individually executed. However, an analytic statement must be executed together with a query statement. In other words, analysis is performed based on the query results or the complete data. For more information, see the "Search and Analysis section of the Log Service" section in **CDS User Guide**.

| Statement | Description |
|---|---|
| Query statement | A query statement specifies one or more query conditions, and then returns the logs that meet the specified conditions. A query statement can be a keyword, a numeric value, a numeric value range, a space character, or an asterisk (*). If you specify a space character or an asterisk (*) as the query statement, no conditions are specified and all logs are returned. |
| Analytic statement | An analytic statement is used to aggregate or analyze all log data or the log data that meets the specified query conditions in a Logstore. |

iv. Click **15 Minutes(Relative)** to specify the time range for the query statement. You can select a relative time, a time frame, or a custom time range. However, the time range that you can specify is only accurate to the minute at most. If you want to use a time range that is accurate to the second, you must specify the time range in the analytic statement. Example: * | SELECT * FROM log WHERE __time__>1558013658 AND __time__<

```
1558013660 .
```

v. Click **Search & Analyze**. Query results contain query and analysis results in a log distribution histogram, on the Raw Logs tab, and on the Graph tab. You can also perform operations on the results. For example, you can configure alerts and create saved searches. Log distribution histogram The log distribution histogram shows the distribution of returned logs in different periods of time. Alert You can click **Save as Alert** to configure alerts for query and analysis results. Saved search You can click **Save Search** to save a query statement as a saved search. Raw log You can click the Table or Raw Data option on the **Raw Logs** tab to analyze the distribution of a field over a period of time, view the context of the specified log in the raw file, monitor the log content in real time, and extract key log information. Graph On the **Graph** tab, you can view the visual query and analysis results, add charts to the dashboard, download logs, and configure interactive behaviors. LogReduce On the **LogReduce** tab, you can click **Enable LogReduce** to cluster similar logs during log collection. Method 2: Query real-time logs on the **Dashboard** tab i. Log on to the OSS console. ii. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the bucket that you want to manage. iii. Click the **Dashboard** tab to analyze logs. Dashboard allows you to view four reports that are immediately available.
**Access Center**: displays the overall operating status including the PV, UV, traffic, and
distribution of access over the Internet.
**Audit Center**: displays statistics of object operations including read, write, and delete
operations.
**Operation Center**: displays statistics of access logs including the number of requests
and distribution of failed operations.
**Performance Center**: displays statistics of performance including the performance of
downloads and uploads over the Internet, the performance of transmission over different networks or with different object sizes, and the list of differences between stored and downloaded objects.

**Disable real-time log query**

**Important**

If you disable real-time log query, the system does not delete Log Service projects. Delete these projects before you disable real-time log query.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name to
which you want to upload objects.
3. Click Logging and then click **Real-time Log Query**. On the Real-time Log Query tab, click
**Disable Real-time Log Query**.

### 4.16 IMG

#### 4.16.1 Configure image styles

You can encapsulate multiple Image Processing (IMG) parameters in a style and perform complex IMG operations by using the style.

**Background information**

Up to 50 styles can be created for a bucket. These styles can be used only for image objects in the bucket.

**Create a style**

1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to create styles.
3. Click the **Image Processing (IMG)** tab. On the page that appears, click **Create Rule**.
4. In the **Create Rule** panel, configure the style.
You can use **Basic Edit** or **Advanced Edit** to create a style:
**Basic Edit**: You can use the IMG features by using the graphical user interface (GUI). For
example, resize an image, add a watermark, and modify the image format.
**Advanced Edit**: You can use the API code to edit the IMG features that you want to use
to process an image. The format is:

```
 image/action1,parame_value1/action2,parame_value2/... .
```

Example: `image/resize,p_63/quality,q_90` indicates that the image is scaled down to 63% of the source image, and then the relative quality of the image is set to 90%.

**Note**

If you want to add image and text watermarks to images at the same time by using a style, use **Advanced Edit** to create the style.
5. Click **OK**.
After you create a style, you can click **Export** to export the style to a specified local path.

**Apply styles**

You can perform the following steps to use a created style to process an image object in the current bucket:
1. On the Overview page, click the **Files** tab.
2. Click the name of the image that you want to process.
3. In the **View Details** panel, select an image style from the **Image Style** drop-down list.
You can view the processed image in the **View Details** panel. Right-click the image and click **Save As** to save the image to your local disk.

**Simplify IMG URLs that include style parameters**

IMG URLs that include style parameters generally include the access URL of the image to process, the style parameter and the name of the style. Example: `https://image-demo.oss-` cn-qd-ase-d01-a.mytest-inc.com/example.jpg?x-oss-process=style/small . You can replace ? `x-oss-process=style/` with customized delimiters to simplify the IMG URL. For example, if you specify the delimiter as an exclamation point (!), the IMG URL can be simplified to

```
 https://image-demo.oss-cn-qd-ase-d01-a.mytest-inc.com/example.jpg!small .
```

1. In the Buckets page, click the **Image Processing (IMG)** tab.
2. Click **Access Settings**.
3. On the **Access Settings** panel, select one of the **Delimiters**.
Only hyphens (-), underscores (_), forward slashes (/), and exclamation points (?) can be used as delimiters.
4. Click **OK**.

#### 4.16.2 Configure source image protection

Object Storage Service (OSS) provides the source image protection feature to protect your images from being used by unauthorized anonymous requesters. After you enable source image protection for your bucket, anonymous requesters can access original images in the bucket only by adding style parameters in the requests or by using signed URLs.

**Background information**

You can use the following methods to access the protected original images: Use URLs that contain style parameters in the following format:

| https://BucketName.Endpoint/ObjectName?x-oss-process=style/StyleName |   | . |
|---|---|---|
|   | https://BucketName.Endpoint/ObjectName? |   |

```
Signature .
```

1. Log on to the OSS console.
2. Click the **Image Processing (IMG)** tab. On the page that appears, click **Access Settings**.
3. In the **Access Settings** panel, turn on **Protect Source Image File** and configure the
parameters described in the following table.

| Parameter | Description |
|---|---|

| Protected File Extensions | Select a file suffix from the Protected File Extensions drop-down list. All objects in the bucket that match the specified suffix are protected. |
|---|---|
| Delimiters | After you select a custom delimiter, you can use the delimiter to replace ?x-oss-process=style/ to simplify the IMG URL. OSS supports the following delimiters: hyphens (-), underscores ( ), _ forward slashes (/), and exclamation points (!). Click the check box before the delimiter that you want to select. For example, if you set the delimiter to an exclamation point (!), the IMG URL can be simplified to the following format: http(s)//:BucketName.Endpoint/ObjcetName!StyleName . |

4. Click **OK**.

## 5 Objects

### 5.1 Search for objects

You can search for objects whose names contain specific prefixes in buckets or folders in the OSS console.

**Prerequisites**

Object are uploaded to the bucket. For more information, see Upload objects.

**Background information**

When you search for objects based on a prefix, search strings are case-sensitive and cannot contain forward slashes (/). You can search for objects only in the root folder of the current bucket or in the current folder. Subfolders and objects stored in subfolders cannot be searched.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket in which the objects that you want to search for are stored.
3. Click the **Files** tab.
4. Search for objects.
Search for objects or folders within the root folder of the bucket In the upper-right corner, enter the prefix to search in the search box and press Enter or click the icon to search for related objects. Objects and subfolders whose names contain the specified prefix within the root folder of the bucket are displayed. Search for objects or subfolders within a specified folder Click the folder in which the objects or subfolders that you want to search for are stored. In the upper-right corner, enter the prefix to search in the search box and press Enter or click the icon to search for related objects. Objects and subfolders whose names contain the specified prefix within the current folder are displayed.

### 5.2 Configure object ACLs

You can configure the ACL of an object in the OSS console to control access to the object.

**Prerequisites**

An object is uploaded to the bucket. For more information, see Upload objects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket that contains the object whose ACL you want to configure.
3. In the left-side navigation pane, click **Files**.
4. Click the name of the object whose ACL you want to configure. In the **View Details** panel,
click **Set ACL** on the right side of **File ACL**. You can also choose **More > Set ACL** in the Actions column corresponding to the object whose ACL you want to configure.
5. In the **Set ACL** panel, configure the ACL of the object.
You can set the ACL of the object to one of the following values:
**Inherited from Bucket**: The ACL of the object is the same as that of the bucket.
**Private**: Only the owner or authorized users of this bucket can read and write objects in
the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization.
**Public Read**: Only the owner or authorized users of this bucket can write objects in the
bucket. Other users, including anonymous users can only read objects in the bucket.
**Public Read/Write**: All users, including anonymous users can read and write objects in
the bucket. Fees incurred by such operations are charged to the owner of the bucket. Exercise caution when you set the object ACL to this value.
6. Click **OK**.

### 5.3 Create folders

You can use the OSS console to create and simulate basic features of folders in Windows. This topic describes how to create a folder by using the OSS console.

**Prerequisites**

A bucket is created. For more information, see Create buckets.

**Background information**

OSS does not use a hierarchical structure for objects, but instead uses a flat structure. All elements are stored in buckets as objects. To facilitate object grouping and to simplify management, the OSS console displays objects whose names end with a forward slash (/) as folders. These objects can be uploaded and downloaded. You can use OSS folders in the OSS console in the same manner as you use folders in Windows.

**Note**

The OSS console displays objects whose names end with a forward slash (/) as folders, regardless of whether these objects contain data. The objects can only be downloaded by calling an API operation or by using OSS SDKs.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket in which you want to create folders.
3. Click the **Files** tab. On the page that appears, click **Create Folder**.
4. In the **Create Folder** panel, enter the folder name.
The folder name must comply with the following conventions: The name can contain only UTF-8 characters and cannot contain emojis. The name cannot start with a forward slash (/) or backslash (\). The name cannot contain consecutive forward slashes (/). You can use forward slashes (/) in a folder name to quickly create a subfolder. For example, when you create a folder named example/test/, the folder named example/ is created in the root folder of the bucket and the subfolder named test/ is created in the example/ folder. The name cannot be two consecutive periods ( `..` ). The folder name must be 1 to 254 characters in length.
5. Click **OK**.

### 5.4 Configure bucket policies to authorize other users to access OSS resources

**authorize other users to access**

**OSS resources**

You can configure bucket policies to authorize other users to access specified Object Storage Service (OSS) resources.

**Background information**

You can configure multiple bucket policies for a bucket. However, the total size of the policies cannot exceed 16 KB.

**Method 1: Configure bucket policies by using the GUI**

1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure bucket policies.
3. On the bucket details page that appears, click **Files**. On the page that appears, click
**Authorize**.
4. On the **GUI** tab, click **Authorize**.
5. In the **Authorize** panel, configure the parameters and then click **OK**. The following table
describes the parameters that you can configure.

| Parameter | Description |
|---|---|
| Applied To | Select the resources that you want to authorize other users to access. Whole Bucket: The authorization policy applies to all resources in the whole bucket. Specified Resource: The authorization policy applies only to specified resources in the bucket. You can configure multiple bucket policies for specific resources in a bucket. Configure a bucket policy for a directory To configure a bucket policy to authorize users to access all subdirectories and objects within a directory, add an asterisk (*) at the end of the directory name. For example, to authorize users to access all subdirectories and objects within a directory named abc, enter abc/* . Configure a bucket policy for a specific object To configure a bucket policy to authorize users to access a specific object, enter the full path of the object that excludes the bucket name. For example, to authorize users to access an object named myphoto.png in the abc directory, enter abc/myphoto.png . |

|   |   |   | Select the type of accounts that you want to authorize. Anonymous Accounts (*): Select this option if you want to authorize all users to access the specified resources. Other Accounts: Select this option if you want to authorize other Apsara Stack tenant accounts, Resource Access Management (RAM) users, or users that use a temporary token generated by Security Token Service (STS) to access the specified resources. To authorize other Apsara Stack tenant accounts or RAM users to access the specified resources, enter the UIDs of the accounts or RAM users. To authorize users that use a temporary token generated by STS to access the specified resources, enter the user and role information in the following format: arn:sts::{RoleOwnerUid}:assumed- role/{RoleName}/{RoleSessionName} . For example, the role used to generate a user that uses a temporary token generated by STS is testrole, the UID of the Apsara Stack tenant account that owns the role is 12345, and the RoleSessionName that is specified when the temporary user is generated is testsession. In this case, enter arn:sts::12345:assumed- role/testrole/testsession . To authorize all users that use a temporary token generated by STS to access the specified resources, use asterisks (*) as wildcards. For example, enter arn:sts::*:*/*/* . Important If an authorized user is a user that uses a temporary token generated by STS, the user cannot access the specified resources on the OSS console. |   |   |
|---|---|---|---|---|---|
|   |   |   |   | arn:sts::{RoleOwnerUid}:assumed- |   |
|   |   | Accounts | role/{RoleName}/{RoleSessionName} |   |   |
|   |   |   | role/testrole/testsession |   |   |

| Authorized Operation | You can use the following methods to specify authorized operations: Basic Settings and Advanced Settings. Basic Settings If you select this method, you can configure the following permissions based on your requirements. You can move the pointer over the icon on the right side of each permission to view the actions that correspond to the permission option. Read Only: Authorized users can view, list, and download the specified resources. Read/Write: Authorized users can read data from and write data to the specified resources. Any Operation: Authorized users can perform all operations on the specified resources. None: Authorized users cannot perform operations on the specified resources. Important If multiple bucket policies are configured for a user, the user has all the permissions defined in these policies. However, a policy in which Authorized Operation is set to None takes precedence over other policies. For example, if you configure a policy to grant the Read Only permission to a user, and then configure another policy to grant the Read/Write permission to the same user, the permission of the user is Read/Write. If you configure a third policy to grant the None permission to the user, the permission of the user is None. Advanced Settings If you select this method, you must configure the following parameters: Effect: Select Allow or Deny. Action: Specify the operation that you want to allow or deny. You can specify any action that is supported by OSS. |
|---|---|
| Conditions | Optional. You can configure this parameter in both Basic Settings and Advanced Settings to specify the conditions that users must meet to access the specified OSS resources. Access Method: Select HTTPS or HTTP. IP =: Specify the IP addresses or Classless Inter-Domain Routing (CIDR) blocks that can be used to access the specified OSS resources. Separate multiple IP addresses with commas (,). IP ≠: Specify IP addresses or CIDR blocks that cannot be used to access OSS resources. Separate multiple IP addresses with commas (,). |

6. Click **OK**.

**Method 2: Configure bucket policies by specifying policy syntax**

1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket for which you want to configure bucket policies.
3. On the bucket details page that appears, click **Files**. On the page that appears, click
**Authorize**.
4. On the **Syntax** tab, click **Edit**.
You can specify policy syntax based on your requirements to manage fine-grained permissions. The following examples describe the bucket policies configured by the resource owner whose UID is `174649585760xxxx` in different scenarios: Example 1: Allow anonymous users to list all objects in a bucket named examplebucket. `{`

```json
    "Statement": [
```

`{`

```json
            "Action": [
                "oss:ListObjects",
                "oss:ListObjectVersions"
```

`],`

```json
            "Effect": "Allow",
            "Principal": [
                "*"
```

`],`

```json
            "Resource": [
                "acs:oss:*:174649585760xxxx:examplebucket"
```

`]` `},` `],`

```json
    "Version": "1"
```

`}` Example 2: Forbid anonymous users whose IP addresses are not in the CIDR block `192.168.0.0/16` from performing operations on a bucket named examplebucket. `{`

```json
    "Version": "1",
    "Statement": [
```

`{`

```json
            "Effect": "Deny",
            "Action": "oss:*",
            "Principal": [
                "*"
```

`],`

```json
            "Resource": [
                "acs:oss:*:174649585760xxxx:examplebucket"
```

`],`

```json
            "Condition":{
                "NotIpAddress": {
                    "acs:SourceIp": ["192.168.0.0/16"]
```

`}` `}` `}` `]` `}` Example 3: Allow a RAM user whose UID is `20214760404935xxxx` only to read the

| hangzhou/2020 | and | hangzhou/2015 | directories in a bucket named examplebucket. |
|---|---|---|---|
| { "Statement": [ { "Action": [ "oss:GetObject", "oss:GetObjectAcl", "oss:GetObjectVersion", "oss:GetObjectVersionAcl" ], "Effect": "Allow", "Principal": [ "20214760404935xxxx" ], "Resource": [ "acs:oss:*:174649585760xxxx:examplebucket/hanghzou/2020/*", "acs:oss:*:174649585760xxxx:examplebucket/hangzhou/2015/*" ] }, { "Action": [ "oss:ListObjects", "oss:ListObjectVersions" ], "Condition": { "StringLike": { "oss:Prefix": [ "hanghzou/2020/*", "hangzhou/2015/*" ] } }, "Effect": "Allow", "Principal": [ "20214760404935xxxx" ], "Resource": [ "acs:oss:*:174649585760xxxx:examplebucket" ] } ], "Version": "1" } |   |   |   |

5. Click **Save**.

**Access authorized OSS resources**

After you configure a bucket policy for a bucket, you can use the following methods to access the resources specified in the policy: Object URL (only for authorized anonymous users) Anonymous users can enter the URL of an object specified in the policy in a browser to access the object. The URL of the object consists of the default domain name of the bucket

| http://mybucket.oss-cn- |   |
|---|---|
|   | . |

and the path of the object. Example: `http://mybucket.oss-cn-`

```
beijing.aliyuncs.com/file/myphoto.png .
```

OSS console Log on to the OSS console. In the left-side navigation pane, click the + icon next to **My OSS**
**Paths**. In the Add Path panel, add the region in which the bucket is located and object path
specified in the bucket policy. For more information, see Add OSS paths.

### 5.5 Delete objects

You can delete uploaded objects in the OSS console when they are no longer needed.

**Background information**

You can delete a single object or batch delete multiple objects. You can batch delete up to 100 objects. To delete specific objects or batch delete more than 100 objects, we recommend that you use API operations or OSS SDKs.

**Important**

Deleted objects cannot be recovered. Exercise caution when you delete objects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket in which the objects you want to delete are stored.
3. In the left-side navigation pane, click **Files**.
4. Select one or more objects that you want to delete in the object list, and then choose
**Batch Operation > Delete**.
You can also choose **More > Completely Delete** in the Actions column corresponding to the object you want to delete.
5. In the dialog box that appears, click **OK**.

### 5.6 Manage parts

When you use multipart upload to upload an object, the object is split into several parts. After all of the parts are uploaded to the OSS server, you can call CompleteMultipartUpload to combine the parts into a complete object.

**Background information**

You can also configure lifecycle rules to clear parts that are not needed on a regular basis. For more information, see Manage lifecycle rules.
1. Log on to the OSS console.
2. In the left-side navigation pane, click **Buckets**. On the Buckets page, click the name of the
bucket in which the parts you want to delete are stored.
3. Click the **Files** tab. On the page that appears, click **Parts**.
4. In the **Parts** panel, delete the parts.
To delete all parts in the bucket, select all parts and then click **Delete All**. To delete specific parts in the bucket, select these parts and then click **Delete**.
5. In the dialog box that appears, click **OK**.

## 6 Create single tunnels

You can create single tunnels between OSS and a virtual private cloud (VPC) to access OSS resources from the VPC.

**Prerequisites**

A VPC and a vSwitch are created. For more information, see the **Create a VPC** and **Create a vSwitch** topics in **VPC User**
**Guide**.
1. Log on to the OSS console.
2. In the left-side navigation panel, click **Create Single Tunnel**.
3. Click **Create**.
4. On the **Create Single Tunnel** page, configure the parameters described in the following
table.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization of the VPC from which you want to access OSS resources. |
| Resource Set | Yes | After you select an organization, the resource set is automatically selected based on the organization. |
| Region | Yes | After you select an organization, a region is automatically selected based on the organization. |
| Description | No | Enter the description of the single tunnel you want to create. The description cannot exceed 180 characters in length. |
| VPC | Yes | Select the VPC that you created. You can also click Create VPC to create a VPC. |
| vSwitch | Yes | Select the vSwitch that you created. You can also click Create vSwitch to create a vSwitch. |

5. Click **Submit**.

## 7 Add OSS paths

You can add the paths of OSS resources in the console for quicker access.

**Prerequisites**

A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. Click the + icon on the right side of **My OSS Paths**.
3. In the **Add Authorized OSS Path** panel, add a path.
You can configure the following parameters to add a path.
**Region**: Select the region of the bucket in the path that you want to add.
**File Path**: Add the path of the resource that you want to access. The path is in the
`bucket/object-prefix` format. For example, if the OSS resource that you want to access `example`. If the OSS resource is the root folder of a bucket named example, set File Path to that you want to access is the test folder in the root folder of the bucket named example,

```
example/test/.
```

set File Path to
