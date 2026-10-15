---
title: "Object Storage Service — Product Introduction (English translation)"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
source_pages: 13
source_pdf: "01_产品简介_ascm-enterprise-product-introduction.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/oss/zh/ascm-enterprise-product-introduction.pdf"
translation: "unofficial, translated by QwenWork from the Chinese V3.18.6 manual; not an Alibaba Cloud official English publication"
---

# Object Storage Service — Product Introduction

> **Note on this file.** Alibaba Cloud's international documentation portal has **no English Object
> Storage Service volume for Apsara Stack V3.18.6** (English OSS volumes existed up to V3.16.2). This
> document is an unofficial English translation of the Chinese V3.18.6 manual (product version
> `v3.18.6-SP2607`, document date 2026-07-29), for internal reading only. Repeated running-header
> lines produced by the PDF extractor ("对象存储 OSS", "产品简介·对象存储") have been removed.

Alibaba Cloud Object Storage Service (OSS) is a secure, low-cost and highly reliable cloud storage
service provided by Alibaba Cloud. Compared with traditional self-built server storage, OSS has
outstanding advantages in reliability, security, cost and data processing capability. With OSS, users
can store and retrieve unstructured data files of all kinds — including text, images, audio and
video — over the network at any time.

## Product details

OSS uploads data files as objects into buckets and provides key-value object storage. Users can
retrieve the content of an object by its name (key).

**Bucket management**

A bucket is a container for storing objects; every object must belong to a bucket. Users can create
different types of buckets according to their requirements and manage them by configuring
read/write permission ACLs, lifecycle rules and other attributes.

**Object management**

An object is the basic unit of data stored in OSS, also referred to as an OSS file. OSS provides
multiple ways to upload and download files; users can choose an appropriate method based on file size
and network conditions, and manage objects by configuring ACLs, object tags and other attributes.

**Data security**

| Feature | Description |
|---|---|
| EC storage mode | Erasure Coding (EC) is a data storage mode of OSS. Compared with triple replication, EC achieves higher data reliability with less redundancy. |
| Resource isolation | OSS slices user data and stores the slices discretely in a distributed file system according to certain rules, storing data and data indexes separately. |
| Disaster recovery | Provides multiple data disaster-recovery and backup capabilities to protect data security and improve data continuity. |
| Security control and authorization | By default, OSS resources (buckets and objects) are private and can be accessed only by the resource owner or authorized users. To allow third-party access, specific permissions can be granted through several access-control policies. |
| Server-side encryption | When uploading, OSS encrypts the received file and persists the encrypted file; when downloading, OSS automatically decrypts the file, returns it to the user, and declares in the HTTP response header that the file is server-side encrypted. |
| Client-side encryption | Supports client-side encryption: files can be encrypted locally before being sent to OSS. |

**Data processing**

| Feature | Description |
|---|---|
| Image processing | For image files stored in OSS, users can process images with one or more parameters directly, or package multiple parameters into a style to process images in batches — for example adding watermarks or converting formats. |
| Video snapshot | Video files stored in OSS can be processed to extract video frames. |

## Product advantages

Object Storage OSS is a secure, low-cost, highly reliable cloud storage service; compared with
traditional self-built server storage it has outstanding advantages in reliability, security, cost
and data processing capability.

**OSS vs self-built storage**

| Item | Object Storage OSS | Self-built server storage |
|---|---|---|
| Reliability | Data is automatically backed up with multiple redundancies. Supports disk-level, node-level, rack-level and cluster-level failures; up to two damaged nodes are tolerated while data read/write continues uninterrupted. | Limited by hardware reliability and prone to problems; once a disk has bad sectors, irreversible data loss is likely. Manual recovery is difficult, time-consuming and labour-intensive. |
| Security | Enterprise-grade multi-layer protection; multi-tenant resource isolation with same-city disaster recovery; multiple authentication and authorization mechanisms plus whitelists, anti-leeching, master/sub accounts and STS temporary credentials. | Traffic scrubbing and blackhole devices must be purchased separately; security mechanisms must be implemented separately. |
| Data processing | Provides image processing. | Requires extra procurement and separate deployment. |

**Other advantages**

- *Convenient usage*: standard RESTful API (some APIs are compatible with Amazon S3), rich SDKs,
  clients and a console, so data for websites or mobile apps can be uploaded, downloaded, retrieved
  and managed like files.
- Supports streaming write and read — well suited to scenarios such as video, where a large file is
  read while being written.
- Supports data lifecycle management, including batch deletion of expired data.
- Very large capacity: storage can be expanded by adding nodes, and a single bucket supports trillions
  of files.
- Powerful and flexible security: STS and URL signing/authorization, whitelists, anti-leeching and
  RAM roles.
- Rich image processing: conversion among JPG, PNG, BMP, GIF, WebP and TIFF, plus thumbnails,
  cropping, watermarks and scaling.

## Scenarios

OSS is suited to massive storage for image, audio and video applications, multi-site disaster
recovery, and offline data archiving.

**Massive storage for image, audio and video applications** — OSS can store huge volumes of files such
as images, audio, video and logs. Various devices, websites and mobile apps can read from or write to
OSS directly; both streaming write and file write are supported.

**Offline data archiving** — thanks to low cost and high availability, enterprise data that must be
archived offline for a long time can be transferred to OSS.

**Multi-site disaster recovery** — stored data can be replicated asynchronously (near real time)
between two clusters or two cloud systems through cross-region replication or cross-cloud replication,
helping users implement a "two sites, three centres" architecture and multi-site data backup so that
businesses keep running even in extreme disasters.

## Features

**Bucket management**

| Feature | Description |
|---|---|
| Create bucket | A bucket is a container for objects and has configuration attributes such as region, access permission and storage class. Users can create buckets as needed. |
| Delete bucket | Empty buckets (with no objects) can be deleted. **Warning**: a deleted bucket cannot be restored; operate with caution. |
| Read/write ACL | ACL can be set when the bucket is created and modified afterwards according to business needs; only the bucket owner can do this. `public-read-write`: anyone (including anonymous visitors) may read and write objects in the bucket — **warning**: any user on the Internet can access and write data into the bucket, which may leak your data and, if illegal content is written maliciously, may infringe your legitimate rights; not recommended except in special scenarios. `public-read`: only the owner may write, anyone (including anonymous visitors) may read — **warning**: any user on the Internet can access objects in the bucket, which may leak your data. `private`: only the owner may read and write; others cannot access the bucket. |
| Static website hosting | A static website can be hosted in a bucket and accessed through the bucket endpoint. The index document is the homepage OSS returns when the website domain is visited in a browser (equivalent to `index.html`); it must be an anonymously readable file in the root directory of the bucket and only HTML format is supported. The error document is the page OSS returns when a request for an object inside the bucket fails with 404; it must be anonymously readable in the bucket root directory, and HTML, JPG, PNG, BMP and WebP formats are supported. |
| Capacity management | When creating a bucket, its capacity limit can be set; the limit can also be modified in the console. |
| Log stashing | Accessing OSS generates large volumes of access logs; with log stashing these logs are written into a specified bucket as hourly log files following a fixed naming rule. Stored logs can be analysed with Simple Log Service or a self-built Spark cluster. |
| Lifecycle management | Lifecycle rules periodically move cold data or delete data that no longer needs to be accessed, improving management efficiency and saving labour and storage cost. For example, a bucket may contain a very large number of files to delete, while manual deletion removes at most 1,000 files per call; in that case a rule matching the whole bucket with "delete after one day" empties it the next day. |
| Bucket tags | Tagging buckets enables classification and management, such as listing buckets with a given tag or setting access permissions for buckets with a given tag. |
| Anti-leeching | A Referer whitelist restricts access to bucket resources to the listed domains. OSS supports anti-leeching based on the `Referer` header field in HTTP and HTTPS requests. Anti-leeching is verified only when an object is accessed through a signed URL or anonymously; requests carrying an `Authorization` header are not verified. |
| Retention policy (WORM) | The OSS retention policy provides WORM (Write Once Read Many) characteristics for storing and using data in a non-deletable and tamper-proof way. If no user (including the resource owner) may modify or delete objects in a bucket within a specified period, configure a retention policy for the bucket: before the retention period of an object expires, only uploading and reading are allowed; after it expires the object may be modified or deleted. |
| Cross-origin resource sharing (CORS) | CORS configuration of the HTML5 protocol enables cross-origin access. When OSS receives a cross-origin request (or an OPTIONS request), it reads the CORS rules of the bucket and performs the corresponding permission checks, evaluating rules one by one and allowing the request with the first matching rule and returning the corresponding headers. If no rule matches, no CORS-related headers are added. |
| Mirroring and redirection | origin-fetch types are mirroring and redirection, covering hot data migration and redirection of specific requests. *Mirroring*: after it is configured, when a GET request targets a non-existent object, OSS requests it from the origin address specified in the rule, returns it to the user once retrieved, and writes it into OSS; mainly used to migrate data to OSS seamlessly when the service runs on your own origin or another cloud product and cannot be stopped. *Redirection*: when a GET request targets a non-existent object, OSS redirects the request to the address specified in the rule to obtain the target file; this jump can be used for redirection-based business logic. |
| Access OSS with a custom domain name | After an object is uploaded to a bucket, OSS generates the object URL, which can be used directly. To access objects with a custom (own) domain name, bind the domain to the bucket that stores the objects. |

**Object management**

| Feature | Description |
|---|---|
| Upload objects | An object is the basic unit of data stored in OSS (also called an OSS file); choose the upload method according to file size and network environment. Methods: *simple upload* (streaming upload and file upload), up to **5 GiB**; *form upload*, up to **5 GiB**; *append upload*, up to **5 GiB**; *resumable upload* — supports concurrency, resumable transfer and custom part size, recommended for large files, up to **48.8 TiB**; *multipart upload* for large files, up to **48.8 TiB**. During upload, object metadata can be set and progress can be monitored with a progress bar; upload callbacks are supported after completion. |
| Delete objects | Objects can be deleted via the console, automatically by lifecycle rules, via SDKs and API operations, or with tools such as ossutil. **Warning**: deleted objects cannot be restored; operate with caution. |
| Read/write ACL | Object-level ACLs control access to objects. ACL can be set when uploading or modified afterwards; if not set, the default is *inherit from bucket*. *Inherit from bucket*: the object's permissions follow those of its bucket. *Private*: only the owner may read and write; others cannot access. *Public read*: only the owner may write, anyone (including anonymous visitors) may read. *Public read/write*: anyone (including anonymous visitors) may read and write — use with caution. |
| Download objects | OSS provides several download methods: *download to a local file*; *streaming download* — when the file is too large or a single download takes too long, part of the content is processed at a time until the download completes; *range download* — download data within a specified range only; *resumable download* — when downloading large files over an unstable network or after abnormal program exit, downloads may fail even after several retries, so OSS splits the file into parts downloaded separately and merged into a complete file once all parts finish; *conditional download* — one or more conditions can be specified; the object is returned when conditions are met, otherwise an error is returned and nothing is downloaded. |
| Manage objects | Objects can be located quickly by specifying a file name prefix; directories can be created to store files in a specified location. |
| Object tags | Tags are key-value pairs that mark objects; they can be added when uploading or to existing objects, allowing lifecycle rules to be set for objects with the same tag and permissions for tagged objects to be managed with RAM policies. |

**Data security**

| Feature | Description |
|---|---|
| Three replicas | Each chunk is replicated into three identical copies stored on different nodes of the cluster according to a policy, so data can be recovered from other nodes if one node fails. |
| Erasure coding (EC) | Raw data is split into data blocks and parity blocks are computed; the data and parity blocks form an EC group distributed across storage nodes, so lost blocks can be recovered from the remaining ones. EC comprises data blocks (n) — the data is split into n slices — and parity blocks (m) — m parity blocks computed from the n data blocks. The n+m blocks of an EC group reside on different servers, and any loss of up to m blocks can be recovered by the EC algorithm. `n+m` is configurable; **the recommended Apsara Stack configuration is 8+3**, depending on the number of nodes in the deployed cluster. |
| Resource isolation | OSS user authentication uses Access Key symmetric-key authentication, verifying the signature of every HTTP request. After authentication passes, the discretely stored user data is reassembled, which achieves storage isolation between multi-tenant users. |
| Same-city disaster recovery | OSS supports dual-datacentre same-city disaster recovery. For a bucket with this feature enabled, data in the primary datacentre is synchronised to the backup bucket in the OSS cluster of the secondary datacentre, so that data remains accessible when the primary datacentre fails as a whole (power outage, fire, and the like). |
| Cross-region replication | Cross-Region Replication automatically and asynchronously (near real time) replicates objects between buckets in different OSS datacentres (regions), copying create, update and delete operations from the source bucket to the destination bucket in another region. |
| Cross-cloud replication | Replicates data from one cloud system into another, giving users data backup across cloud systems: when one cloud system fails, the business can be switched directly to the other, ensuring business continuity. |
| RAM policies | Resource Access Management (RAM) is the Alibaba Cloud resource access control service. A RAM policy is a user-based authorization policy: users (employees, systems or applications) can be managed centrally and their permissions over resources of the cloud account controlled — for example, granting another user read-only access to a specific bucket. |
| Bucket policies | A bucket policy is a resource-based authorization policy. Compared with RAM policies it is simpler to operate, can be configured graphically in the console, and can be granted by the bucket owner without RAM permissions. Bucket policies can grant access to RAM users of other accounts and to anonymous users with specific IP conditions. *Bucket ACL*: set when creating a bucket and modifiable at any time by the owner — `public-read-write`, `public-read`, `private`. *Anti-leeching*: whitelisting access sources so OSS resources cannot be misused by others. |
| Object policy | Besides bucket-level ACLs, OSS also provides object-level ACLs, set when uploading or modified at any time afterwards according to business needs: inherit from bucket, `public-read-write`, `public-read`, `private`. |
| Server-side encryption | Provides data-at-rest protection through server-side encryption, suited to scenarios with high security or compliance requirements for object storage, such as storing deep-learning sample files or online collaborative document data. |
| Client-side encryption | With client-side encryption, a random data encryption key is generated for each object and used in plaintext to symmetrically encrypt the object's data. The master key is used to generate the random data encryption key, and the encrypted key is stored on the server side as part of the object's metadata. To decrypt, the master key first decrypts the random data encryption key, which then decrypts the object's data. The master key is used only in local client-side computation — it is never transmitted over the network or stored on the server side, which protects the master key. **Warning**: when using client-side encryption you are responsible for the integrity and correctness of the master key; any loss or consequence caused by an incorrect or lost master key due to improper maintenance is borne by you. When copying or migrating encrypted data you are responsible for the integrity and correctness of the encryption metadata, and any loss or consequence caused by erroneous or lost encryption metadata is borne by you. |
| Transport Layer Security (TLS) | Communication between client applications and OSS is encrypted with TLS, a standard cryptographic protocol ensuring privacy and data integrity between clients and servers communicating over the Internet. After the TLS version is configured on the OSS server side, clients can send and receive data only with the specified TLS version, meeting link security requirements. |
| Versioning | Versioning is a bucket-level data protection feature. Once enabled, overwrite and delete operations are saved as historical versions, so objects in the bucket can be restored to any historical version after an accidental overwrite or deletion. |

**Data processing**

| Feature | Description |
|---|---|
| Original image protection | When enabled, direct access to the original OSS file and access that passes image parameters to change the image style are denied. |
| Image processing rules | Multiple style processing rules can be configured. |
| Image effects | Set brightness, contrast, sharpness, blur and rotation in a graphical interface. |
| Image styles | One style can contain multiple image processing parameters to perform complex processing quickly. |
| Image scaling | Choose no thumbnail, proportional downscaling, proportional upscaling, or scaling to a specified width and height. |
| Progressive display | Enables a blurry-then-clear presentation; effective only for images in `jpg` format. |
| Auto-orientation | Rotates the image according to its EXIF orientation information before scaling. |
| Format conversion | Converts images to the original format, JPG, JPEG, PNG, BMP, GIF, WebP or TIFF. |
| Image quality | Choose relative quality, absolute quality, or no compression. |
| Image watermark | Choose no watermark, image watermark or text watermark. |
| Video snapshot | Extracts video frames and converts them to the required image format through the SDK or by adding snapshot parameters to the URL. |

**Tools and compatibility**

| Type | Item | Supported version |
|---|---|---|
| Tools | ossbrowser graphical management tool | ossbrowser 2.0 |
| | ossfs, which maps objects to a file system (NFS and CIFS) | ossfs 1.91.4 |
| | ossftp, which maps objects to FTP | ossftp 1.2.0 |
| | ossutil command-line tool | ossutil 2.0 |
| SDK support | Java | up to 3.17.4 |
| | Python | up to 2.18.3 |
| | PHP | up to 2.0.0 |
| | C | up to 3.11.2 |
| | Go | up to 3.0.2 |
