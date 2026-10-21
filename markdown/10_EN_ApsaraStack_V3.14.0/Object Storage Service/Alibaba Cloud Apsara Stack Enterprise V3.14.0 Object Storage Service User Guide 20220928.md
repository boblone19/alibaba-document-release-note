---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Object Storage Service User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 38
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Object Storage Service User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Object%20Storage%20Service%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Object Storage Service User Guide 20220928

## Table of Contents

- 1 What is OSS?
- 2 Usage notes
- 3 Quick start
  - 3.1 Log on to the OSS console
  - 3.2 Create buckets
  - 3.3 Upload objects
  - 3.4 Obtain object URLs
- 4 Buckets
  - 4.1 View bucket information
  - 4.2 Delete a bucket
  - 4.3 Modify bucket ACLs
  - 4.4 Configure static website hosting
  - 4.5 Configure hotlink protection
  - 4.6 Configure logging
  - 4.7 Configure CORS
  - 4.8 Configure lifecycle rules
  - 4.9 Configure storage quota
  - 4.10 Configure back-to-origin rules
  - 4.11 Configure server-side encryption
  - 4.12 Bind a bucket to a VPC network
  - 4.13 Configure CRR
- 5 Objects
  - 5.1 Search for objects
  - 5.2 Configure object ACLs
  - 5.3 Create folders
  - 5.4 Delete objects
  - 5.5 Manage parts
  - 5.6 Configure object tagging
- 6 Create single tunnels
- 7 Add OSS paths

## 1 What is OSS?

Object Storage Service (OSS) is a secure, cost-effective, and highly reliable cloud storage service provided by Alibaba Cloud. It enables you to store a large amount of data in the cloud. Compared with user-created server storage, OSS has outstanding advantages in reliability, security, cost-effectiveness, and data processing capabilities. OSS enables you to store and retrieve a variety of unstructured data objects, such as text, images, audios, and videos over the network at any time. OSS is an object storage service based on key-value pairs. Files uploaded to OSS are stored as objects in buckets. You can obtain the content of an object based on the object key. In OSS, you can perform the following operations: Create a bucket and upload objects to the bucket. Obtain an object URL from OSS to share or download the object. Modify the attributes or metadata of a bucket or an object. You can also configure the ACL of the bucket or the object. Perform basic and advanced operations in the OSS console. Perform basic and advanced operations by using OSS SDKs or calling RESTful API operations in your application.

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

This topic describes how to log on to the OSS console. Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. In the address bar, enter the URL used to access the Apsara Uni-manager Management Console.
Press Enter.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Login to go to the Apsara Uni-manager Management Console.
4. In the top navigation bar, choose Product s > Object St orage Service.

### 3.2 Create buckets

Objects uploaded to OSS are stored in a bucket. You must create a bucket before you upload objects to OSS.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click Creat e Bucket .
3. On the Creat e OSS Bucket page, configure parameters.
The following table describes the parameters that you can configure.

| Parameter | Description |
|---|---|
| Organizat ion | Select an organization from the drop-down list for the bucket. |

| Parameter | Description |
|---|---|

| Resource Set | Select a resource set from the drop-down list for the bucket. |
|---|---|
| Region | Select a region from the drop-down list for the bucket. Not e The region of a bucket cannot be changed after the bucket is created. If you want to access OSS from your ECS instance through the internal network, select the same region where your ECS instance is deployed. |
| Clust er | Select a cluster for the bucket. |
| Bucket Name | Enter the name of the bucket. Not e The bucket name must comply with the naming conventions. The bucket name must be globally unique among all existing buckets in OSS. The bucket name cannot be changed after the bucket is created. |
| St orage Class | Set the value to St andard. Only Standard is supported. |
| Bucket Capacit y | Specify the capacity of the bucket. Valid values: 0 to 2000000. Unit: TB or GB. |
| Access Cont rol List (ACL) | Set the ACL of the bucket. You can select the following options: Privat e: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access objects in the bucket without authorization. Public Read: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users can only read objects in the bucket. Public Read/Writ e: All users, including anonymous users can read and write objects in the bucket. Fees incurred by such operations are paid by the owner of the bucket. Exercise caution when you configure this option. Not e You can modify the ACL of a bucket after the bucket is created. For more information, see Modify bucket ACLs. |

| Parameter | Description |
|---|---|
| Server-Side Encrypt ion | Configure server-side encryption for the bucket. You can select the following options: None: Server-side encryption is not performed. AES256: AES256 is used to encrypt each object in the bucket using different data keys. Customer master keys (CMKs) used to encrypt the data keys are rotated regularly. KMS: CMKs managed by KMS are sued to encrypt objects in the bucket. |
| Encrypt ion Algorit hm | You can configure this parameter when you select KMS for Server-Side Encrypt ion. |
| Key ID | You can configure this parameter when you select KMS for Server-Side encrypt ion. OSS uses the specified CMK to encrypt objects in the bucket. Not e To select a CMK ID for server-side encryption, you must create the CMK in the KMS console. |

4. Click Submit .

### 3.3 Upload objects

After you create a bucket, you can upload objects to it. A bucket is created. For more information about how to create a bucket, see Create buckets. You can upload an object of any format to a bucket. You can use the OSS console to upload an object up to 5 GB in size. To upload an object larger than 5 GB, use OSS SDKs or call an API operation.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
to which you want to upload objects.
3. On the bucket details page, click the Files tab.
4. Click Upload.
5. In the Upload panel, set the parameters described in the following table.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Upload T o | Set the folder to which objects are uploaded. Current : Objects are uploaded to the current folder. Specif ied: Objects are uploaded to the specified folder. You must enter a folder name. If the specified folder does not exist, OSS automatically creates the specified folder and uploads the object to the folder. |
| File ACL | Set the ACL of the object to upload. Default value: Inherit ed f rom Bucket . Inherit ed f rom Bucket : The ACL of uploaded objects is the same as that of the bucket. Privat e: Only the owner or authorized users can read and write objects in the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization. Public Read: Only the bucket owner can perform write operations on objects in the bucket. Other users, including anonymous users, can perform only read operations on objects in the bucket. Public Read/Writ e: All users, including anonymous users, can read and write objects in the bucket. |
| Upload | Drag one or more objects to upload to this section, or click Upload to select one or more objects to upload. Not ice When the uploaded object has the same name as an existing object in the bucket, the existing object is overwritten. If you upload a folder, only the files in the folder are uploaded and stored in the same folder in the bucket. The name of an uploaded object must comply with the following conventions: The name can contain only UTF-8 characters. The name is case-sensitive. The name must be 1 to 1,023 bytes in length. The name cannot start with a forward slash (/) or backslash (\). |

6. In the Upload T asks panel, wait until the upload task is complete.
Do not refresh or close the Upload T asks panel when objects are being uploaded. Otherwise, the upload tasks are interrupted.

### 3.4 Obtain object URLs

You can obtain the URL of an uploaded object and share the URL with other users to preview or download the object. q An object is uploaded to the bucket. For more information, see Upload objects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which the object whose URL you want to obtain is stored.
3. Click the Files tab.
4. Click the name of the object whose URL you want to obtain. In the View Det ails panel, click Copy
File URL.

## 4 Buckets

### 4.1 View bucket information

You can view the detailed information about the created buckets in the OSS console. A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
that you want to view.
3. On the Overview tab, you can view the information about the bucket, including the organization,
resource set, endpoints, and basic settings.

### 4.2 Delete a bucket

You can delete a bucket in the OSS console. All objects and parts in the bucket are deleted. For more information, see Delete objects and Manage parts.

> **Warning:** Deleted objects, parts, and buckets cannot be recovered. Exercise caution when you delete objects, parts, and buckets.

1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
that you want to delete.
3. On the bucket details page that appears, click Delet e Bucket in the upper right corner. In the
message that appears, click OK.

### 4.3 Modify bucket ACLs

OSS provides access control list (ACL) to control access to buckets. By default, the ACL of bucket is private. You can modify the ACL of the bucket after it is created. A bucket is created. For more information about how to create a bucket, see Create buckets. You can set the ACL of a bucket to one of the following values: Private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization. Public Read: Only the owner or authorized users of this bucket can write objects in the bucket. Other users, including anonymous users can only read objects in the bucket. Public Read/Write: Any users, including anonymous users can read and write objects in the bucket.

> **Warning:** If you set the ACL of a bucket to Public Read or Public Read/Write, other users can read the data in the bucket without authentication, which results in security risks. To ensure the security of your data, we recommend that you configure the ACL of your bucket to private.

1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to modify the ACL.
3. Click the Basic Set t ings tab. Find the Access Cont rol List (ACL) section.
4. Click Conf igure. Modify the bucket ACL.
5. Click Save.

### 4.4 Configure static website hosting

You can configure static website hosting for a bucket in the OSS console so that users can access the website by using the domain name of the bucket. A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure static website hosting.
3. Click the Basic Set t ings tab. Find the St at ic Pages section.
4. Click Conf igure and then set the parameters described in the following table.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Def ault Homepage | Specify an index page that functions similar to index.html. Only HTML objects can be set to the index page. Static website hosting is disabled if you do not specify this parameter. If Subfolder Homepage is disabled, you must make sure that the index object exists in the root folder and is readable. If Subfolder Homepage is enabled, you must make sure that the index object exists in both the root folder and the subfolder and the index object is readable. Not e You can specify only one index object for Default Homepage. If you enable Subfolder Homepage, the index object for the subfolder homepage must have the same name as that for the root folder homepage. However, the content of the index objects can be different. |
| Def ault 404 Page | Set the default 404 page that is displayed when the requested resource does not exist. Only the HTML, JPG, PNG, BMP, or WebP object in the root folder can be set to the default 404 page. Default 404 Page is disabled if you do not specify this parameter. |
| Subf older Homepage | Specify whether to enable the subfolder homepage feature. Disable: disables Subfolder Homepage. The default homepage of the root folder is displayed if you access the root domain name of a static website or any URL that ends with a forward slash (/) under this domain name. Enable: enables Subfolder Homepage. When you access the root domain name of a static website, the default homepage of the root folder is displayed. When you access a URL ending with a forward slash (/), the default homepage of the corresponding folder is displayed. For example, when you access the URL test.oss-cn- hangzhou.aliyuncs.com/subdir/, the default homepage of the subfolder is displayed if the index object exists in the subdir/ folder. |

| Parameter | Description |   |   |
|---|---|---|---|
| Subf older 404 Rule | This parameter is available if you enable Subfolder Homepage. You can configure this parameter to specify the result to return when you access an object whose name does not end with a forward slash (/) and the object does not exist. For example, if subdir does not exist when you access test.oss-cn-hangzhou.aliyuncs.com/subdir, the following rules apply: Redirect : the default rule that checks whether subdir/index object exists. If the index object exists, HTTP status code 302 is returned with the Location header that specifies test.oss-cn-hangzhou.aliyuncs .com/subdir/ . If the index object does not exist, the default 404 page is returned. If the default 404 page does not exist, HTTP status code 404 is returned. NoSuckKey: returns the default 404 page. If the default 404 page does not exist, HTTP status code 404 is returned. Index: the rule that checks whether subdir/index document exists. If the index document exists, the content of the index document is directly returned. If the index document does not exist, the default 404 page is returned. If the default 404 page does not exist, HTTP status code 404 is returned. |   |   |
|   |   | test.oss-cn-hangzhou.aliyuncs |   |

|   | .com/subdir/ |
|---|---|

5. Click Save.

### 4.5 Configure hotlink protection

You can configure hotlink protection for a bucket in the OSS console to prevent data in your bucket from being accessed by unauthorized domain names. A bucket is created. For more information about how to create a bucket, see Create buckets. The hotlink protection feature allows you to configure a Referer whitelist for a bucket. This way, only requests from domain names included in the Referer whitelist can access data in the bucket. OSS allows you to configure Referer whitelists based on the Referer header field in HTTP and HTTPS requests. After hotlink protection is configured for a bucket, OSS verifies requests to objects in the bucket only when the requests are initiated from signed URLs or anonymous users. Requests that contain the Authorization field in the header are not verified.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure hotlink protection.
3. Click the Basic Set t ings tab. Find the Hot link Prot ect ion section.
4. Click Conf igure. Configure the parameters.
Enter domain names or IP addresses in the Ref erer Whit elist field. Separate multiple Referers by using line feed. You can use asterisks (*) and question marks (?) as wildcards. Example: If you add www.example.com to the Referer whitelist, requests sent from URLs that start with www.example.com, such as www.example.com/123 and www.example.com.cn are allowed. If you add *www.example.com/ to the Referer whitelist, requests sent from http://www.exa mple.com/ and https://www.example.com/ are allowed. An asterisk (*) can be used as a wildcard to indicate zero or more characters. For example, if you add *.example.com to the Referer whitelist, requests sent from URLs such as help.example. com and www.example.com are allowed. A question mark (?) can be used as a wildcard to indicate a single character. For example, if you add example?.com to the Referer whitelist, requests sent from URLs such as examplea.com and exampleb.com are allowed. You can add domain names or IP addresses that include a port number, such as www.example. com:8080 and 10.10.10.10:8080, to the Referer whitelist. Select whether to turn on Allow Empt y Ref erer to allow requests in which the Referer field is empty. An HTTP or HTTPS request that contains an empty Referer indicates that the request does not contain the Referer field or the value of the Referer field is empty. If you do not allow empty Referers fields, only HTTP or HTTPS requests which include an allowed Referer field can access the objects in the bucket.

> Not e By default, if you use the bucket endpoint to preview an MP4 object, the browser sends a request that contains the Referer field and a request that does not contain the Referer field at the same time. Therefore, you must not only add the bucket endpoint to the Referer whitelist but also allow empty Referer fields. To use the bucket endpoint to preview an object of other formats, you need only to allow empty Referer fields.

5. Click Save.

### 4.6 Configure logging

When you access OSS, a large number of access logs are generated. You can use the logging feature to store OSS access logs in a specified bucket. A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure logging.
3. Click the Basic Set t ings tab. Find the Logging section.
4. Click Conf igure. Turn on the Logging switch. Select Dest inat ion Bucket and set Log Pref ix.
Dest inat ion Bucket : Select the name of the bucket used to store access logs from the dropdown list. You must be the owner of the selected bucket, and the bucket must be in the same region as the bucket for which logging is enabled. Log Pref ix: Enter the prefix and folder where the access logs are stored. If you specify log/<Tar getPrefix> as the prefix, access logs are stored in the log/ directory.
5. Click Save.

### 4.7 Configure CORS

You can configure cross-origin resource sharing (CORS) in the OSS console to enable cross-origin access. A bucket is created. For more information about how to create a bucket, see Create buckets. OSS provides CORS over HTML5 to implement cross-origin access. When OSS receives a cross-origin request (or an OPTIONS request) for a bucket, OSS reads the CORS rules of the bucket and checks the relevant permissions. OSS matches the request with the rules one by one. When OSS finds the first match, OSS returns a corresponding header in the response. If no match is found, OSS does not include any CORS header in the response.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure CORS.
3. Click the Basic Set t ings tab. In the Cross-Origin Resource Sharing (CORS) section, click
Conf igure.
4. Click Creat e Rule. In the Creat e Rule panel, configure the parameters described in the following
table.

| Parameter | Required | Description |
|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| Sources | Yes | Specifies the sources from which you want to allow cross-origin requests. Note the following rules when you configure the sources: You can configure multiple rules for sources. Separate multiple rules with line feeds. The domain names must include the protocol name, such as HTTP or HTTPS. Asterisks (*) are supported as wildcards. Each rule can contain up to one asterisk (*). A domain name must contain the port number if the domain name does not use the default port. Example: https://www.example.com:8080. The following examples show how to configure domain names: To match a specified domain name, enter the full domain name. Example: https://www.example.com:8080. Use an asterisk (*) as a wildcard in the domain name to match second-level domains. Example: https://*.example.com. Enter only an asterisk (*) as the wildcard to match all domain names. |
| Allowed Met hods | Yes | Specifies the cross-origin request methods that are allowed. |
| Allowed Headers | No | Specifies the response headers for the allowed cross-origin requests. Take note of the following rules when you configure the allowed headers: This parameter is in the key:value format and case-insensitive. Example: content- type:text/plain. You can configure multiple rules for allowed headers. Separate multiple rules with new lines. Each rule can contain up to one asterisk (*) as the wildcard. Set this parameter to an asterisk (*) if you do not have special requirements. |
| Exposed Headers | No | Specifies the response headers for allowed access requests from applications, such as an XMLHttpRequest object in JavaScript. Exposed headers cannot contain asterisks (*). |

| Parameter | Required | Description |
|---|---|---|
| Cache T imeout (Seconds) | No | Specifies the time the browser can cache the response to a preflight (OPTIONS) request to a specific resource. |

> Not e You can configure up to 10 rules for each bucket.

5. Click OK.

### 4.8 Configure lifecycle rules

You can configure lifecycle rules for a bucket and manage the rules in the OSS console. A bucket is created. For more information, see Create buckets. Take note of the following items when you configure lifecycle rules for a bucket: After a lifecycle rule is configured, it is loaded within 24 hours and takes effect within 24 hours after it is loaded. Check the configurations of a rule before you save the rule. Objects that are deleted based on lifecycle rules cannot be recovered. Configure lifecycle rules based on your requirements. You can configure up to 100 lifecycle rules in the OSS console. To configure more than 100 rules, use ossutil or OSS SDKs.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure lifecycle rules.
3. Click the Basic Set t ings tab. Find the Lif ecycle section. Click Conf igure.
4. Click Creat e Rule. In the Creat e Rule panel, configure the parameters described in the following
table.

| Parameter | Description |
|---|---|
| Basic Set t ings |   |
| St at us | Specify the status of the lifecycle rule. Valid values: Enabled and Disabled. |

| Parameter | Description |
|---|---|
| Applied T o | Select policies used to match objects with the rule. You can select Files wit h Specif ied Pref ix or Whole Bucket . Files with Specified Prefix indicates that this rule applies to objects whose names contain a specified prefix. Whole Bucket indicates that this rule applies to all objects in the bucket. Not e If you select Files wit h Specif ied Pref ix, you can configure multiple lifecycle rules for objects whose names contain different prefixes. If you select Whole Bucket , only one lifecycle rule can be configured for the bucket. |
| Pref ix | If you set Applied T o to Files wit h Specif ied Pref ix, you must specify the prefix of the objects to which the rule applies. For example, if you want the rule applies to objects whose names start with img, enter img. |
| Clear Policy |   |
| File Lif ecycle | Configure rules for objects to specify when objects expire. You can set File Lifecycle to Validit y Period (Days), Expirat ion Dat e, or Disabled. If you select Disabled, the configurations of File Lifecycle do not take effect. |
| Delet e | Specify when objects expire based on Validit y Period (Days) or Expirat ion Dat e that you set for File Lif ecycle. Expired objects are deleted. Validit y Period (Days): Specify the number of days to retain objects after they are last modified. The objects are deleted the next day after they expire. For example, if you set Validity Period (Days) to 30, objects that are last modified on January 1, 2019 are deleted on February 1, 2019. Expirat ion Dat e: Specify the expiration date. Objects that are last modified before this date expire and are deleted. For example, if you set Expiration Date to 2019-1-1, objects that are last modified before January 1, 2019 are deleted. |
| Delet e Part s |   |
| Part Lif ecycle | Specify the operations to perform on expired parts. You can set Part Lifecycle to Validit y Period (Days), Expirat ion Dat a, or Disabled. If you select Disabled, the configurations of Part Lifecycle do not take effect. Not ice You must configure at least one of File Lif ecycle and Part Lif ecycle. |
| Delet e | Specify when parts expire based on Validit y Period (Days) or Expirat ion Dat a that you set for Part Lif ecycle. Expired parts are deleted. You can configure this parameter in the same way as you configure the Delete parameter in Clear Policy. |

5. Click OK.

### 4.9 Configure storage quota

If the capacity of a bucket reaches the specified storage quota, write operations such as PutObject, MultipartUpload, CopyObject, PostObject, and AppendObject cannot be performed on the bucket. This topic describes how to configure the storage quota of a created bucket. A bucket is created. For more information, see Create buckets. Take note of the following items when you configure the storage quota of a bucket: Before you configure the storage quota of a bucket, make sure that the quota does not limit your business because write operations cannot be performed if the bucket capacity reaches the quota. In general, it takes about an hour for OSS to determine whether the bucket capacity exceeds the storage quota. In some cases, it can take longer.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure storage quota.
3. Click the Basic Set t ings tab, find the St orage Quot a section.
4. Click Conf igure. Turn on St orage Quot a and set St orage Quot a.
Units: TB or GB. Valid values: -1 to 2000000 The default value is -1, which indicates that the bucket capacity is not limited.
5. Click Save.

### 4.10 Configure back-to-origin rules

If you access data in a bucket that has no back-to-origin rules configured and the data does not exist, 404 Not Found is returned. However, if you configure back-to-origin rules that contain the correct origin URL, you can obtain the data based on the back-to-origin rules. Back-to-origin supports the mirroring and redirection modes. You can configure back-to-origin rules for hot migration and specific request redirection. Mirroring-based back-to-origin After mirroring-based back-to-origin rules are configured for a bucket, you can obtain an object in the bucket based on the rules when the requested object is not found. For example, when you perform the GetObject operation on an object and the object is not found, OSS retrieves the object based on the origin URL, returns the object, and then writes the object to OSS. Mirroring-based backto-origin rules are used to seamlessly migrate data to OSS. This feature allows you to migrate a service that already runs on a user-created origin or in another cloud service to OSS without interrupting services. Redirection-based back-to-origin After redirection-based back-to-origin rules are configured for a bucket, you can obtain an object in the bucket based on the rules when the requested object is not found. For example, when you perform the GetObject operation on an object and the object is not found, OSS redirects the request to the origin URL, and then a browser or client returns the content from the origin. You can use this feature to redirect requests for objects and develop various services based on redirection. You can configure up to 20 back-to-origin rules, which are run in a sequence that they are configured.

> Not ice Back-to-origin rules and versioning cannot be configured for a bucket at the same time.

Configure a mirroring-based back-to-origin rule
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure the mirroring-based back-to-origin rule.
3. Click the Basic Set t ings tab. In the Back-t o-Origin section, click Conf igure.
4. Click Creat e Rule. In the Creat e Rule panel, set the parameters described in the following table
to create a mirroring-based back-to-origin rule.

| Parameter | Required | Description |
|---|---|---|
| Mode | Yes | Select Mirroring. In this mode, when a requested object cannot be found in OSS, OSS automatically retrieves the object from the origin, stores the object in OSS, and then returns the content to the requester. |

| Parameter |   |   | Required | Description |
|---|---|---|---|---|
| Prerequisit e |   |   |   | Configure the conditions that trigger the back-to-origin rule. A rule is triggered only when all conditions are met. HT T P St at us Code: The back-to-origin rule is triggered when the specified HTTP status code is returned. The default HTTP status code is 404, which indicates that the rule is triggered when the requested object is not found in OSS and HTTP status code 404 is returned. By default, this option is selected when you select the Mirroring mode. File Name Pref ix: The back-to-origin rule is triggered when the name of the requested object contains the specified prefix. For example, when this parameter is set to abc/, the back-to-origin rule is triggered when you access https://bucketname.endpoint/abc/image.j pg . File Name Suf f ix: The back-to-origin rule is triggered when the name of the requested object contains the specified suffix. For example, when this parameter is set to .jpg, the back-to-origin rule is triggered when you access https://bucketname.endpoint/image.jpg . Not e File Name Prefix and File Name Suffix are optional when you configure only one back-to-origin rule. When you configure multiple back-to-origin rules, you must differentiate the rules by specifying a different prefix or suffix for each of the rules. |
|   | Prerequisit e |   | Yes | pg |
| Replace or Delet e File Pref ix |   |   | No | You can configure this parameter after you select and configure File Name Pref ix. When OSS sends a request to the origin, the content of File Name Pref ix is replaced with that of Replace or Delet e File Pref ix. Example: You want to store the object obtained from the origin in the mirror folder under the root folder of the bucket. If the name of the requested object is path/test/p hoto.jpg, set File Name Pref ix to mirror/, Replace or Delet e File Pref ix to test/, and the third column of Origin URL to path. In this case, when you access https ://bucketname.endpoint/mirror/photo.jpg , if photo.j pg does not exist, OSS sends the https://origin URL/ path/test/photo.jpg request to obtain this object. If the object is obtained from the origin, OSS stores this object in the mirror/ folder and returns the object to you. |
|   |   |   |   | path/test/photo.jpg |

| https://bucketname.endpoint/abc/image.j |   |
|---|---|

|   | ://bucketname.endpoint/mirror/photo.jpg |   |
|---|---|---|

| Parameter |   |   | Required | Description |
|---|---|---|---|---|
| Origin URL |   |   | Yes | Configure the information about the origin URL. First column: Select HTTP or HTTPS based on the protocol used by the origin. Not e If SNI is enabled on the origin, HTTPS that you select does not take effect. Second column: Enter the domain name or IP address of the origin. Internal endpoints and IP addresses are not supported. If you enter an IP address, ensure that the origin corresponding to the IP address can be accessed by using the IP address. Third column: Enter the folder where the requested object is stored. Separate subfolders in a folder with forward slashes (/). Example: abc/123 . |
| MD5 Verif icat ion |   |   | No | If this option is selected, the MD5 hash of the object obtained from the origin is checked. When the response contains the Content-MD5 header value, OSS checks whether the MD5 hash of the object matches the Content- MD5 header value. If the MD5 hash of the object matches the Content-MD5 header value, the client obtains the object, and OSS saves the object by using mirroring-based back-to- origin. If the MD5 hash of the object does not match the Content-MD5 header value, OSS calculates the Content- MD5 header value of the object based on the data integrity and does not save the object. However, the client can obtain the object because the object is returned to the client. |
| Keep Forward Slash in Origin URL |   |   | No | OSS does not support object names that start with a forward slash (/). Therefore, when the name of the requested object starts with a forward slash (/), you must select this option to obtain the requested object based on the back-to-origin rules. For example, the origin is https://www.example.com , the name of the requested object is /object.txt, and the name of the bucket is examplebucket. If this option is selected, the default public endpoint to access the requested object is https://examplebucket.endpoint/ /object.txt , and the origin URL is https://www.exam ple.com//object.txt . The object is obtained from OSS, returned to the client, and then saved in the bucket as obje ct.txt. |
|   |   |   |   | /object.txt |

| https://examplebucket.endpoint/ |   |   |
|---|---|---|
|   | https://www.exam |   |

| Parameter | Required | Description |
|---|---|---|
| Ot her Paramet er | No | If this option is selected, the query string included in the request to OSS is transferred to the origin. |
| 3xx Response | No | If this option is selected, OSS follows the origin to direct the request to obtain the resource and stores the resource in buckets. If this option is not selected, OSS passes the 3xx response without obtaining the resource. |
| Set T ransmission Rule of HT T P Header | No | You can configure the transmission rule for HTTP headers to customize transmission actions such as passthrough, filtering, or modification. For more information, see the following examples of transmission rule configurations for HTTP headers. |

The following figure provides a sample transmission rule for HTTP headers. You send a request that contains the following HTTP headers to OSS.

```
GET /object host : bucket.oss-cn-hangzhou.aliyuncs.com aaa-header : aaa bbb-header : bbb ccc-header : 111
```

After the mirroring-based back-to-origin rule is triggered, OSS sends the following request to the origin:

```
GET /object host : source.com aaa-header : aaa ccc-header : ccc
```

Transmission rules do not support the following HTTP headers: Headers that contain the following prefixes: x-ossossx-drs- All standard HTTP headers. Examples: content-length authorization2 authorization range date Configure a redirection-based back-to-origin rule
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure a redirection-based back-to-origin rule.
3. Click the Basic Set t ings tab. In the Back-t o-Origin section, click Conf igure.
4. Click Creat e Rule. In the Creat e Rule panel, configure the parameters described in the following
table to create a redirection-based back-to-origin rule.

| Parameter |   | Required | Description |   |   |
|---|---|---|---|---|---|
| Mode |   | Yes | Select Redirect ion. In this mode, OSS redirects requests that meet the prerequisites to the origin URL over HTTP, and then a browser or client returns the content from the origin to the requester. |   |   |
| Prerequisit e |   |   | Configure the conditions that trigger the back-to-origin rule. A rule is triggered only when all conditions are met. HT T P St at us Code: The back-to-origin rule is triggered when the specified HTTP status code is returned. The default HTTP status code is 404, which indicates that the rule is triggered when the requested object is not found in OSS and HTTP status code 404 is returned. File Name Pref ix: The back-to-origin rule is triggered when the name of the requested object contains the specified prefix. For example, when this parameter is set to abc/, the back-to-origin rule is triggered when you access https://bucketname.endpoint/abc/image.j pg . File Name Suf f ix: The back-to-origin rule is triggered when the name of the requested object contains the specified suffix. For example, when this parameter is set to .jpg, the back-to-origin rule is triggered when you access https://bucketname.endpoint/image.jpg . Not e File Name Prefix and File Name Suffix are optional when you configure only one back-to-origin rule. When you configure multiple back-to-origin rules, you must differentiate the rules by specifying a different prefix or suffix for each of the rules. |   |   |
|   |   |   |   | https://bucketname.endpoint/abc/image.j |   |
|   | Prerequisit e | Yes | pg |   |   |

|   | Parameter |   |   | Required |   | Description |   |
|---|---|---|---|---|---|---|---|
|   | Replace or Delet e File Pref ix |   |   | No |   | You can configure this parameter after you select and configure File Name Pref ix. When OSS sends a request to the origin, the content of File Name Pref ix is replaced with that of Replace File Name Pref ix. Not e If you select this option, you can only set Replace File Name Pref ix for Origin URL. |   |
|   | Origin URL |   |   |   |   | Configure the information about the origin URL. You must configure the back-to-origin rule based on the origin URL. Configuring the origin URL in accordance with the following rules: First column: Select HTTP or HTTPS based on the protocol used by the origin. Second column: Enter the domain name or IP address of the origin. Not e You can enter IP addresses only when the origin can be directly accessed by using IP addresses. Third column: Configure the redirection-based back-to- origin rule based on the prefix and suffix configurations. Add Pref ix or Suf f ix: Add a prefix or suffix to the redirected URL. The prefix is configured in the third column. The suffix is configured in the fourth column. You can select this option to configure information for the redirected URL when the URL of the requested data excludes a prefix or suffix. For example, the prefix is set to 123/, and the suffix is set to .jpg. When you access https://bucketname.endpoint/ image , the request is redirected to https://Orig in URL/123/image.jpg . Redirect t o Fixed URL: Access to the requested object is redirected to a specified object. The object address is specified in the third column. Example: a bc/myphoto.jpg . Not e You can also set the value of this parameter to the URL of a website. For example, if you set the URL to https://www.aliyun.com /index.html , access to the bucket is redirected to the Alibaba Cloud homepage. |   |
|   |   |   |   |   |   | image |   |
|   |   |   |   | Yes |   |   |   |
|   |   |   |   |   |   |   | /index.html |

| https://bucketname.endpoint/ |   |   |
|---|---|---|
|   | https://Orig |   |

| a |   |
|---|---|

| https://www.aliyun.com |   |   |
|---|---|---|

| Parameter | Required | Replace File Name Pref ix: If you set this parameter Description and File Name Pref ix for Prerequisite, the prefix in |
|---|---|---|
|   |   | the name of the object to which the access is redirected is replaced with that of the third column. If you set this parameter without setting File Name Pref ix for Prerequisite, the specified prefix is added to the name of the object to which the access is redirected. Separate subfolders in a folder with forward slashes (/). The folder name must end with a forward slash (/). The folder name cannot contain asterisks (*). |
| Ot her Paramet er | No | If this option is selected, the query string included in the request to OSS is transferred to the origin. |
| Redirect ion Code | Yes | You can select the redirection code from the drop-down list. Select Source f rom Alibaba Cloud CDN if the redirect request is from Alibaba Cloud CDN. |

5. Click OK.

### 4.11 Configure server-side encryption

OSS supports server-side encryption. When you upload an object to a bucket for which server-side encryption is enabled, OSS encrypts the object and stores the encrypted object. When you download the encrypted object from OSS, OSS automatically decrypts the object and returns the decrypted object to you. A header is added in the response to indicate that the object is encrypted on the OSS server. OSS supports the following encryption methods: Server-side encryption by using KMS (SSE-KMS) OSS uses the default customer master key (CMK) managed by KMS or a specified CMK to encrypt objects. The CMK is managed by KMS to ensure confidentiality, integrity, and availability at minimal costs. Server-side encryption by using OSS-managed keys (SSE-OSS) OSS uses data keys to encrypt objects and manages the data keys. In addition, OSS uses master keys that are regularly rotated to encrypt data keys. You can enable server-side encryption in the OSS console by using one of the following methods: Method 1: Enable server-side encryption when you create a bucket Method 2: Enable server-side encryption on the Basic Settings tab Method 1: Enable server-side encryption when you create a bucket
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click Creat e Bucket .
3. On the Creat e OSS Bucket page, set parameters.
You can set the following parameters to configure server-side encryption for the bucket. Server-Side Encrypt ion: Specify the encryption methods. None: Server-side encryption is not performed. AES256: AES256 is used to encrypt each object in the bucket by using different data keys. The CMKs used to encrypt the data keys are rotated regularly. KMS: CMKs managed by KMS are used to encrypt objects in the bucket. Encrypt ion Algorit hm: This parameter can be configured when you select KMS for Server- Side Encrypt ion. Key ID: This parameter can be configured when you select KMS for Server-Side Encrypt ion. OSS uses the specified CMK to encrypt objects in the bucket.

> Not e
> To select a CMK ID for server-side encryption, you must create the CMK in the KMS console.

4. Click Submit .
Method 2: Enable server-side encryption on the Basic Settings tab
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
for which you want to configure server-side encryption.
3. Click the Basic Set t ings tab. Find the Server-side Encrypt ion section.
4. Click Conf igure and set the following parameters:
Encrypt ion Met hod: Specify the encryption method. None: Server-side encryption is not performed. OSS-Managed: Keys managed by OSS are used to encrypt your data. KMS: CMKs managed by KMS are used to encrypt objects in the bucket. CMK: This parameter can be configured when you select KMS for Encrypt ion Met hod. OSS uses the specified CMK to encrypt objects in the bucket.

> Not e
> To select a CMK ID for server-side encryption, you must create the CMK in the KMS console.

5. Click Save.

> Not ice
> The configurations of the default encryption method for a bucket do not affect the encryption configurations of existing objects within the bucket.

### 4.12 Bind a bucket to a VPC network

You can bind your bucket to a specified virtual private cloud (VPC) network to allow only requests from IP addresses within the VPC network to access your bucket. A VPC network is created. For more information, see the "Create a VPC" chapter of VPC User Guide.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
that you want to bind to the VPC network.
3. Click the Overview tab. Click Bind VPC in the VPC Inf o section.
4. On the Bind VPC page, select the VPC network that you create.
You can also click Creat e VPC to create a new VPC network.
5. Click Submit .

### 4.13 Configure CRR

Cross-region replication (CRR) enables the automatic and asynchronous (near real-time) replication of objects across buckets in different OSS regions. Operations such as the creation, overwriting, and deletion of objects can be synchronized from the source bucket to the destination bucket. The steps described in Create buckets are performed or a bucket is created in the region. This feature meets the requirements of geo-disaster recovery or data replication. Objects in the destination bucket are extra replicas of objects in the source bucket. They have the same object names, object content, and object metadata such as the creation time, owner, user metadata, and object ACL.
1. Log on to the OSS console.
2. In the left-side navigation pane, click the name of a bucket for which you want to configure CRR to
go to the bucket details page.
3. On the bucket details page, click the Basic Set t ings tab. Find the Cross-Region Replicat ion
section.
4. Click Enable. In the Cross-Region Replicat ion dialog box that appears, configure the parameters
described in the following table.

| Parameter | Description |
|---|---|
| Source Region | The region where the current bucket is located. |
| Source Bucket | The name of the current bucket. |

| t Storage Service | User Guide·Bucket |
|---|---|

| Parameter | Description |
|---|---|
| Dest inat ion Region | Select the region where the destination bucket is located. The source and destination buckets for CRR must be located in different regions. Data cannot be synchronized between buckets located within the same region. |
| Dest inat ion Bucket | Select the destination bucket. The two buckets with CRR enabled cannot synchronize data with other buckets. If you synchronize data from Bucket A to Bucket B, neither Bucket A nor Bucket B can synchronize data with other buckets. |
| Applied T o | Select the source data to synchronize. All Files in Source Bucket : synchronizes all objects from the source bucket to the destination bucket. Files wit h Specif ied Pref ix: synchronizes the objects whose names contain the specified prefix from the source bucket to the destination bucket. For example, if you have a folder named management/ in the root folder of a bucket and a subfolder named abc/ in management/, when you want to synchronize objects in the abc/ subfolder, enter management/abc/ as the prefix. You can specify up to five prefixes. |
| Operat ions | Select the synchronization policy. Add/Change: synchronizes only added or changed data from the source bucket to the destination bucket. Add/Delet e/Change: synchronizes all data changes such as the creation, overwriting, and deletion of objects from the source bucket to the destination bucket. |
| Replicat e Hist orical Dat a | Specify whether to synchronize historical data before you enable CRR. Yes: synchronizes historical data to the destination bucket. Not ice When historical data is synchronized, objects in the source bucket may overwrite objects in the destination bucket if these objects have the same name. Before you select this option, ensure that the data is consistent. No: synchronizes only objects that you want to upload or update after CRR is enabled to the destination bucket. |

5. Click OK.

> Not e
> After the configuration is complete, it may take three to five minutes for CRR to take effect. Synchronization information is displayed after the source bucket is synchronized.
> In CRR, data is asynchronously (near real-time) replicated. It takes several minutes to several hours for the data to be replicated to the destination bucket based on the amount of data.

## 5 Objects

### 5.1 Search for objects

You can search for objects whose names contain specific prefixes in buckets or folders in the OSS console. Object are uploaded to the bucket. For more information, see Upload objects. When you search for objects based on a prefix, search strings are case-sensitive and cannot contain forward slashes (/). You can search for objects only in the root folder of the current bucket or in the current folder. Subfolders and objects stored in subfolders cannot be searched.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which the objects that you want to search for are stored.
3. Click the Files tab.
4. Search for objects.
Search for objects or folders within the root folder of the bucket In the upper-right corner, enter the prefix to search in the search box and press Enter or click the icon to search for related objects. Objects and subfolders whose names contain the specified prefix within the root folder of the bucket are displayed. Search for objects or subfolders within a specified folder Click the folder in which the objects or subfolders that you want to search for are stored. In the upper-right corner, enter the prefix to search in the search box and press Enter or click the icon to search for related objects. Objects and subfolders whose names contain the specified prefix within the current folder are displayed.

### 5.2 Configure object ACLs

You can configure the ACL of an object in the OSS console to control access to the object. An object is uploaded to the bucket. For more information, see Upload objects.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket
that contains the object whose ACL you want to configure.
3. In the left-side navigation pane, click Files.
4. Click the name of the object whose ACL you want to configure. In the View Det ails panel, click Set
ACL on the right side of File ACL. You can also choose More > Set ACL in the Actions column corresponding to the object whose ACL you want to configure.
5. In the Set ACL panel, configure the ACL of the object.
You can set the ACL of the object to one of the following values: Inherit ed f rom Bucket : The ACL of the object is the same as that of the bucket. Privat e: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization. Public Read: Only the owner or authorized users of this bucket can write objects in the bucket. Other users, including anonymous users can only read objects in the bucket. Public Read/Writ e: All users, including anonymous users can read and write objects in the bucket. Fees incurred by such operations are charged to the owner of the bucket. Exercise caution when you set the object ACL to this value.
6. Click OK.

### 5.3 Create folders

You can use the OSS console to create and simulate basic features of folders in Windows. This topic describes how to create a folder by using the OSS console. A bucket is created. For more information, see Create buckets. OSS does not use a hierarchical structure for objects, but instead uses a flat structure. All elements are stored in buckets as objects. To facilitate object grouping and to simplify management, the OSS console displays objects whose names end with a forward slash (/) as folders. These objects can be uploaded and downloaded. You can use OSS folders in the OSS console in the same manner as you use folders in Windows.

> Not e The OSS console displays objects whose names end with a forward slash (/) as folders, regardless of whether these objects contain data. The objects can only be downloaded by calling an API operation or by using OSS SDKs.

1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which you want to create folders.
3. Click the Files tab. On the page that appears, click Creat e Folder.
4. In the Creat e Folder panel, enter the folder name.
The folder name must comply with the following conventions: The name can contain only UTF-8 characters and cannot contain emojis. The name cannot start with a forward slash (/) or backslash (\). The name cannot contain consecutive forward slashes (/). You can use forward slashes (/) in a folder name to quickly create a subfolder. For example, when you create a folder named example/test/, the folder named example/ is created in the root folder of the bucket and the subfolder named test/ is created in the example/ folder. The name cannot be two consecutive periods ( `..` ). The folder name must be 1 to 254 characters in length.
5. Click OK.

### 5.4 Delete objects

You can delete uploaded objects in the OSS console when they are no longer needed. You can delete a single object or batch delete multiple objects. You can batch delete up to 100 objects. To delete specific objects or batch delete more than 100 objects, we recommend that you use API operations or OSS SDKs.

> Not ice Deleted objects cannot be recovered. Exercise caution when you delete objects.

1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which the objects you want to delete are stored.
3. In the left-side navigation pane, click Files.
4. Select one or more objects that you want to delete in the object list, and then choose Bat ch
Operat ion > Delet e. You can also choose More > Complet ely Delet e in the Actions column corresponding to the object you want to delete.
5. In the dialog box that appears, click OK.

### 5.5 Manage parts

When you use multipart upload to upload an object, the object is split into several parts. After all of the parts are uploaded to the OSS server, you can call CompleteMultipartUpload to combine the parts into a complete object. You can also configure lifecycle rules to clear parts that are not needed on a regular basis. For more information, see Manage lifecycle rules.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which the parts you want to delete are stored.
3. Click the Files tab. On the page that appears, click Part s.
4. In the Part s panel, delete the parts.
To delete all parts in the bucket, select all parts and then click Delet e All. To delete specific parts in the bucket, select these parts and then click Delet e.
5. In the dialog box that appears, click OK.

### 5.6 Configure object tagging

You can configure object tagging to classify objects. Object tagging uses key-value pairs to identify objects. You can perform operations on multiple objects that have the same tag. For example, you can configure lifecycle rules for objects that have the same tag. Object tagging uses key-value pairs to identify objects. You can manage multiple objects that have the same tag. For example, you can configure lifecycle rules for objects that have the same tag or authorize Resource Access Management (RAM) users to access objects that have the same tag. When you configure object tagging, take note of the following items: You can add up to 10 tags to an object. The tags added to an object must have unique tag keys. A tag key can be up to 128 bytes in length. A tag value can be up to 256 bytes in length. Tag keys and tag values are case-sensitive. The key and value of a tag can contain letters, digits, spaces, and the following special characters: + - = ._:/ Only the bucket owner and authorized users have read and write permissions on object tags. These permissions are independent of object access control lists (ACLs). In cross-region replication (CRR), object tags are also replicated to the destination bucket.
1. Log on to the OSS console.
2. In the left-side navigation pane, click Bucket s. On the Buckets page, click the name of the bucket in
which the object that you want to configure tagging is stored.
3. On the bucket details page, click the Files tab.
4. Choose More > T agging in the Actions column corresponding to the object to which you want to
add tags.
5. In the T agging panel, configure the Key and Value of the tag.
You can click Add to add up to more 10 tags to the object.
6. Click OK.

## 6 Create single tunnels

You can create single tunnels between OSS and a virtual private cloud (VPC) to access OSS resources from the VPC. A VPC and a vSwitch are created. For more information, see the Create a VPC and Create a vSwitch topics in VPC User Guide.
1. Log on to the OSS console.
2. In the left-side navigation panel, click Creat e Single T unnel.
3. Click Creat e.
4. On the Creat e Single T unnel page, configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Organizat ion | Yes | Select the organization of the VPC from which you want to access OSS resources. |
| Resource Set | Yes | After you select an organization, the resource set is automatically selected based on the organization. |
| Region | Yes | After you select an organization, a region is automatically selected based on the organization. |
| Descript ion | No | Enter the description of the single tunnel you want to create. The description cannot exceed 180 characters in length. |
| VPC | Yes | Select the VPC that you created. You can also click Creat e VPC to create a VPC. |
| vSwit ch | Yes | Select the vSwitch that you created. You can also click Creat e vSwit ch to create a vSwitch. |

5. Click Submit .

## 7 Add OSS paths

You can add the paths of OSS resources in the console for quicker access. A bucket is created. For more information about how to create a bucket, see Create buckets.
1. Log on to the OSS console.
2. Click the + icon on the right side of My OSS Pat hs.
3. In the Add Aut horized OSS Pat h panel, add a path.
You can configure the following parameters to add a path. Region: Select the region of the bucket in the path that you want to add. File Pat h: Add the path of the resource that you want to access. The path is in the `bucket/ob` `ject-prefix` format. For example, if the OSS resource that you want to access is the root folder of a bucket named example, set File Path to example. If the OSS resource that you want to access is the test folder in the root folder of the bucket named example, set File Path to exa mple/test/.
