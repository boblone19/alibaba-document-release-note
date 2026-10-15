---
title: "ApsaraDB for MongoDB User Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 163
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for MongoDB User Guide 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20MongoDB%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20MongoDB%20User%20Guide%2020260630.pdf"
converter: line-classifier (PyMuPDF)
---

# ApsaraDB for MongoDB User Guide 20260630

| Operation | Limits |
|---|---|
| Scale out nodes | When a replica set instance is created, three nodes are added. ApsaraDB for MongoDB provides a primary node, a secondary node, and a hidden node for each replica set instance. The primary and secondary nodes provide services, and the hidden node is invisible to you. You cannot scale out secondary nodes. |
| Restart instances | You must restart an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console or by calling the API operation. |

## Precautions

Before you begin to use ApsaraDB for MongoDB, you must familiarize yourself with the precautions and limits of the service. To ensure the stability and security of ApsaraDB for MongoDB instances, take note of the limits described in ApsaraDB for MongoDB limits. Table 1. ApsaraDB for MongoDB limits

## Log on to the ApsaraDB for

**MongoDB console**

This topic describes how to log on to the ApsaraDB for MongoDB console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

**Note**

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your login scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA code and click **Authentication**. You have enabled and bound MFA: Enter the six-digit MFA code and click **Authentication**.

**Note**

For more information about how to bind and enable MFA, see **Security Center** >
**MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.
5. In the top navigation bar, choose **Products** > **Database Services** > **ApsaraDB for**
**MongoDB**.

| Instance type | Characteristics | Scenario |
|---|---|---|
| Dedicated instance type | A dedicated cluster occupies all allocated compute resources such as CPU cores. The cluster does not share compute resources with other clusters that run on the same server. This improves the reliability and stability of the cluster. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| General- purpose instance type | Idle compute resources such as CPUs are shared among clusters that run on the same server. Resource sharing allows you to deploy a large number of clusters at low costs. | Scenarios in which cost-effectiveness is prioritized. |

| Instance type | Specificati ons | Specification code | Maximum connections | Maximum IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|
|  | 2 cores, 4 GB | dds.mongo.2x.lar ge.c | 3,000 | 8,000 | 10 to 3,000 |
|  | 2 cores, 8 GB | dds.mongo.4x.lar ge.c | 3,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.mongo.2x.xla rge.c | 6,000 | 8,000 |  |
|  | 4 cores, 16 GB | dds.mongo.4x.xla rge.c | 6,000 | 8,000 |  |

## Instance types

### Replica set instance types

This topic describes the available instance types of replica set instances in ApsaraDB for MongoDB.

**Supported specifications (MongoDB 5.0 to 8.0)**

| General- purpose |  |  |  |  |  |
|---|---|---|---|---|---|
|  | 8 cores, 16 GB | dds.mongo.2x.2xl arge.c | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.mongo.4x.2xl arge.c | 16,000 | 14,000 |  |
|  | 16 cores, 32 GB | dds.mongo.2x.4xl arge.c | 16,000 | 14,000 |  |
|  | 16 cores, 64 GB | dds.mongo.4x.4xl arge.c | 32,000 | 16,000 |  |
|  | 32 cores, 64 GB | dds.mongo.2x.8xl arge.c | 32,000 | 16,000 |  |
| Dedicated | 2 cores, 8 GB | dds.mongo.4x.lar ge.d | 5,000 | 8,000 | 250 to 3,000 |
|  | 2 cores, 16 GB | dds.mongo.8x.lar ge.d | 8,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.mongo.2x.xla rge.d | 8,000 | 8,000 | 500 to 3,000 |
|  | 4 cores, 16 GB | dds.mongo.4x.xla rge.d | 8,000 | 8,000 |  |
|  | 4 cores, 32 GB | dds.mongo.8x.xla rge.d | 12,000 | 9,000 |  |
|  | 8 cores, 16 GB | dds.mongo.2x.2xl arge.d | 12,000 | 8,000 | 1,000 to 3,000 |
|  | 8 cores, 32 GB | dds.mongo.4x.2xl arge.d | 16,000 | 9,000 |  |
|  | 8 cores, 64 GB | dds.mongo.8x.2xl arge.d | 16,000 | 18,000 |  |
|  | 16 cores, 32 GB | dds.mongo.2x.4xl arge.d | 16,000 | 9,000 |  |

|  |  |  |  |  | aDB for MongoDB |
|---|---|---|---|---|---|
|  |  |  |  |  | 2,000 to 3,000 |
|  | 16 cores, 64 GB | dds.mongo.4x.4xl arge.d | 32,000 | 18,000 |  |
|  | 16 cores, 128 GB | dds.mongo.8x.4xl arge.d | 32,000 | 36,000 |  |
|  | 32 cores, 64 GB | dds.mongo.2x.8xl arge.d | 32,000 | 18,000 |  |
|  | 32 cores, 128 GB | dds.mongo.4x.8xl arge.d | 96,000 | 36,000 |  |
|  | 32 cores, 256 GB | dds.mongo.8x.8xl arge.d | 96,000 | 72,000 |  |
|  | 64 cores, 128 GB | dds.mongo.2x.16x large.d | 96,000 | 36,000 |  |
|  | 64 cores, 256 GB | dds.mongo.4x.16x large.d | 128,000 | 72,000 |  |
|  | 64 cores, 512 GB | dds.mongo.8x.16x large.d | 128,000 | 144,000 |  |

| Instance type | Specifica tions | Specification code | Maximum connections | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|
| General- purpose | 1 core, 2 GB | dds.mongo.mid | 200 | 800 | 10 to 2,000 |
|  | 2 cores, 4 GB | dds.mongo.standar d | 400 | 1,600 |  |
|  | 4 cores, 8 GB | dds.mongo.large | 1,000 | 3,200 |  |
|  | 8 cores, 16 GB | dds.mongo.xlarge | 2,000 | 6,400 |  |
|  | 8 cores, 32 GB | dds.mongo.2xlarge | 4,000 | 12,800 |  |
| 3 | > Document Ve |  |  |  | rsion: 2026063 |

**Supported specifications (MongoDB 3.0 to 4.2)**

|  | 16 cores, 64 GB | dds.mongo.4xlarge | 8,000 | 12,800 |  |
|---|---|---|---|---|---|
|  | 2 cores, 16 GB | mongo.x8.medium | 2,500 | 4,500 | 250 |
| Dedicated |  |  |  |  |  |
|  | 4 cores, 32 GB | mongo.x8.large | 5,000 | 9,000 | 500 |
|  | 8 cores, 64 GB | mongo.x8.xlarge | 10,000 | 18,000 | 1,000 |
|  | 16 cores, 128 GB | mongo.x8.2xlarge | 20,000 | 36,000 | 2,000 |
|  | 32 cores, 256 GB | mongo.x8.4xlarge | 40,000 | 72,000 | 2,000 |
| Physical machine (dedicated) | 60 cores, 440 GB | dds.mongo.2xmon opolize | 100,000 | 100,000 | 3,000 |

| Instance type | Characteristics | Scenario |
|---|---|---|
| Dedicated instance type | A dedicated cluster occupies all allocated compute resources such as CPU cores. The cluster does not share compute resources with other clusters that run on the same server. This improves the reliability and stability of the cluster. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |

### Sharded cluster instance

**types**

This topic describes the available instance types of sharded cluster instances in ApsaraDB for MongoDB.

| General- purpose instance type | Idle compute resources such as CPUs are shared among clusters that run on the same server. Resource sharing allows you to deploy a large number of clusters at low costs. | Scenarios in which cost-effectiveness is prioritized. |
|---|---|---|

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|---|---|
| General- purpose | 2 cores, 4 GB | dds.mon gos.2x.la rge.c | 2 | 4 | 3,000 | 1,600 |  |
|  | 4 cores, 8 GB | dds.mon gos.2x.xl arge.c | 4 | 8 | 6,000 | 3,200 |  |
|  | 8 cores, 16 GB | dds.mon gos.2x.2x large.c | 8 | 16 | 12,000 | 6,400 |  |
|  | 16 cores, 32 GB | dds.mon gos.2x.4x large.c | 16 | 32 | 16,000 | 12,800 |  |
|  | 32 cores, 64 GB | dds.mon gos.2x.8x large.c | 32 | 64 | 32,000 | 12,800 |  |
|  | 2 cores, 8 GB | dds.mon gos.4x.la rge.d | 2 | 8 | 5,000 | 3,200 |  |
|  | 2 cores, 16 GB | dds.mon gos.8x.la rge.d | 2 | 16 | 8,000 | 6,400 |  |
|  | 4 cores, 8 GB | dds.mon gos.2x.xl arge.d | 4 | 8 | 8,000 | 3,200 |  |

**MongoDB specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

|  | 4 cores, 16 GB | dds.mon gos.4x.xl arge.d | 4 | 16 | 8,000 | 6,400 |  |
|---|---|---|---|---|---|---|---|
| Dedicate d |  |  |  |  |  |  |  |
|  | 4 cores, 32 GB | dds.mon gos.8x.xl arge.d | 4 | 32 | 12,000 | 12,800 |  |
|  | 8 cores, 16 GB | dds.mon gos.2x.2x large.d | 8 | 16 | 12,000 | 6,400 |  |
|  | 8 cores, 32 GB | dds.mon gos.4x.2x large.d | 8 | 32 | 16,000 | 12,800 |  |
|  | 8 cores, 64 GB | dds.mon gos.8x.2x large.d | 8 | 64 | 16,000 | 12,800 |  |
|  | 16 cores, 32 GB | dds.mon gos.2x.4x large.d | 16 | 32 | 16,000 | 12,800 |  |
|  | 16 cores, 64 GB | dds.mon gos.4x.4x large.d | 16 | 64 | 32,000 | 12,800 |  |
|  | 16 cores, 128 GB | dds.mon gos.8x.4x large.d | 16 | 128 | 32,000 | 25,600 |  |
|  | 32 cores, 64 GB | dds.mon gos.2x.8x large.d | 32 | 64 | 32,000 | 12,800 |  |
|  | 32 cores, 128 GB | dds.mon gos.4x.8x large.d | 32 | 128 | 96,000 | 25,600 |  |
|  | 32 cores, 256 GB | dds.mon gos.8x.8x large.d | 32 | 256 | 96000 | 51,200 |  |

**Supported specifications (MongoDB 3.4 to 4.2)**

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|---|---|
| General- purpose | 1 core, 2 GB | dds.mon gos.mid | 1 | 2 | 1,000 | 1,000 | 10 to 2,000 |
|  | 2 cores, 4 GB | dds.mon gos.stand ard | 2 | 4 | 2,000 | 2,000 |  |
|  | 4 cores, 8 GB | dds.mon gos.large | 4 | 8 | 4,000 | 4,000 |  |
|  | 8 cores, 16 GB | dds.mon gos.xlarg e | 8 | 16 | 8,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.mon gos.2xlar ge | 8 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 64 GB | dds.mon gos.4xlar ge | 16 | 64 | 16,000 | 16,000 |  |
|  | 2 cores, 8 GB | dds.mon gos.4x.la rge.d | 2 | 8 | 5,000 | 3,200 |  |
|  | 2 cores, 16 GB | dds.mon gos.8x.la rge.d | 2 | 16 | 8,000 | 6,400 |  |
|  | 4 cores, 8 GB | dds.mon gos.2x.xl arge.d | 4 | 8 | 8,000 | 3,200 |  |
|  | 4 cores, 16 GB | dds.mon gos.4x.xl arge.d | 4 | 16 | 8,000 | 6,400 |  |
|  | 4 cores, 32 GB | dds.mon gos.8x.xl arge.d | 4 | 32 | 12,000 | 12,800 |  |

| Dedicate d |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  | 8 cores, 16 GB | dds.mon gos.2x.2x large.d | 8 | 16 | 12,000 | 6,400 |  |
|  | 8 cores, 32 GB | dds.mon gos.4x.2x large.d | 8 | 32 | 16,000 | 12,800 |  |
|  | 8 cores, 64 GB | dds.mon gos.8x.2x large.d | 8 | 64 | 16,000 | 12,800 |  |
|  | 16 cores, 32 GB | dds.mon gos.2x.4x large.d | 16 | 32 | 16,000 | 12,800 |  |
|  | 16 cores, 64 GB | dds.mon gos.4x.4x large.d | 16 | 64 | 32,000 | 12,800 |  |
|  | 16 cores, 128 GB | dds.mon gos.8x.4x large.d | 16 | 128 | 32,000 | 25,600 |  |
|  | 32 cores, 64 GB | dds.mon gos.2x.8x large.d | 32 | 64 | 32,000 | 12,800 |  |
|  | 32 cores, 128 GB | dds.mon gos.4x.8x large.d | 32 | 128 | 96,000 | 25,600 |  |
|  | 32 cores, 256 GB | dds.mon gos.8x.8x large.d | 32 | 256 | 96,000 | 51,200 |  |

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|---|---|

**Shard specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

| General- purpose | 2 cores, 4 GB | dds.shar d.2x.larg e.c | 2 | 4 | 3,000 | 8,000 |  |
|---|---|---|---|---|---|---|---|
|  | 2 cores, 8 GB | dds.shar d.4x.larg e.c | 2 | 8 | 3,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.shar d.2x.xlar ge.c | 4 | 8 | 6,000 | 8,000 |  |
|  | 4 cores, 16 GB | dds.shar d.4x.xlar ge.c | 4 | 16 | 6,000 | 8,000 |  |
|  | 8 cores, 16 GB | dds.shar d.2x.2xla rge.c | 8 | 16 | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.shar d.4x.2xla rge.c | 8 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 32 GB | dds.shar d.2x.4xla rge.c | 16 | 64 | 16,000 | 14,000 |  |
|  | 16 cores, 64 GB | dds.shar d.4x.4xla rge.c | 16 | 64 | 32,000 | 16,000 |  |
|  | 32 cores, 64 GB | dds.shar d.2x.8xla rge.c | 32 | 64 | 32,000 | 16,000 |  |
|  | 2 cores, 8 GB | dds.shar d.4x.larg e.d | 2 | 8 | 5,000 | 8,000 |  |
|  | 2 cores, 16 GB | dds.shar d.8x.larg e.d | 2 | 16 | 8,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.shar d.2x.xlar ge.d | 4 | 8 | 8,000 | 8,000 |  |

|  |  |  |  |  |  |  | 10 to 3,000 |
|---|---|---|---|---|---|---|---|
|  | 4 cores, 16 GB | dds.shar d.4x.xlar ge.d | 4 | 16 | 8,000 | 8,000 |  |
| Dedicate d |  |  |  |  |  |  |  |
|  | 4 cores, 32 GB | dds.shar d.8x.xlar ge.d | 4 | 32 | 12,000 | 9,000 |  |
|  | 8 cores, 16 GB | dds.shar d.2x.2xla rge.d | 8 | 16 | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.shar d.4x.2xla rge.d | 8 | 32 | 16,000 | 9,000 |  |
|  | 8 cores, 64 GB | dds.shar d.8x.2xla rge.d | 8 | 64 | 16,000 | 18,000 |  |
|  | 16 cores, 32 GB | dds.shar d.2x.4xla rge.d | 16 | 32 | 16,000 | 9,000 |  |
|  | 16 cores, 64 GB | dds.shar d.4x.4xla rge.d | 16 | 64 | 32,000 | 18,000 |  |
|  | 16 cores, 128 GB | dds.shar d.8x.4xla rge.d | 16 | 128 | 32,000 | 36,000 |  |
|  | 32 cores, 64 GB | dds.shar d.2x.8xla rge.d | 32 | 64 | 32,000 | 18,000 |  |
|  | 32 cores, 128 GB | dds.shar d.4x.8xla rge.d | 32 | 128 | 96,000 | 36,000 |  |
|  | 32 cores, 256 GB | dds.shar d.8x.8xla rge.d | 32 | 256 | 96,000 | 72,000 |  |
|  | 64 cores, 128 GB | dds.shar d.2x.16xl arge.d | 64 | 128 | 96,000 | 36,000 |  |

|  | 64 cores, 256 GB | dds.shar d.4x.16xl arge.d | 64 | 256 | 128,000 | 72,000 |  |
|---|---|---|---|---|---|---|---|
|  | 64 cores, 512 GB | dds.shar d.8x.16xl arge.d | 64 | 512 | 128,000 | 144,000 |  |

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|---|---|
| General- purpose | 1 core, 2 GB | dds.shar d.mid | 1 | 2 | 500 | 1,000 | 10 to 2,000 |
|  | 2 cores, 4 GB | dds.shar d.standar d | 2 | 4 | 1,000 | 2,000 |  |
|  | 4 cores, 8 GB | dds.shar d.large | 4 | 8 | 3,000 | 4,000 |  |
|  | 8 cores, 16 GB | dds.shar d.xlarge | 8 | 16 | 5,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.shar d.2xlarge | 8 | 32 | 8,000 | 14,000 |  |
|  | 16 cores, 64 GB | dds.shar d.4xlarge | 16 | 64 | 16,000 | 16,000 |  |
|  | 2 cores, 16 GB | dds.shar d.sn8.xla rge.3 | 2 | 16 | 2,500 | 4,500 | 10 to 250 |
|  | 4 cores, 32 GB | dds.shar d.sn8.2xl arge.3 | 4 | 32 | 5,000 | 9,000 | 10 to 500 |
|  | 8 cores, 64 GB | dds.shar d.sn8.4xl arge.3 | 8 | 64 | 10 | 18,000 | 10 to 1,000 |
| 1 |  |  |  |  |  |  |  |

**Supported specifications (MongoDB 3.4 to 4.2)**

|  | 16 cores, 128 GB | dds.shar d.sn8.8xl arge.3 | 16 | 128 | 20,000 | 36,000 | 10 to 2,000 |
|---|---|---|---|---|---|---|---|
| Dedicate d |  |  |  |  |  |  |  |
|  | 32 cores, 256 GB | dds.shar d.sn8.16x large.3 | 32 | 256 | 40,000 | 72,000 | 10 to 3,000 |
|  | 2 cores, 8 GB | dds.shar d.4x.larg e.d | 2 | 8 | 5,000 | 8,000 |  |
|  | 2 cores, 16 GB | dds.shar d.8x.larg e.d | 2 | 16 | 8,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.shar d.2x.xlar ge.d | 4 | 8 | 8,000 | 8,000 |  |
|  | 4 cores, 16 GB | dds.shar d.4x.xlar ge.d | 4 | 16 | 8,000 | 8,000 |  |
|  | 4 cores, 32 GB | dds.shar d.8x.xlar ge.d | 4 | 32 | 12,000 | 9,000 |  |
|  | 8 cores, 16 GB | dds.shar d.2x.2xla rge.d | 8 | 16 | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.shar d.4x.2xla rge.d | 8 | 32 | 16,000 | 9,000 |  |
|  | 8 cores, 64 GB | dds.shar d.8x.2xla rge.d | 8 | 64 | 16,000 | 18,000 |  |
|  | 16 cores, 32 GB | dds.shar d.2x.4xla rge.d | 16 | 32 | 16,000 | 9,000 |  |
|  | 16 cores, 64 GB | dds.shar d.4x.4xla rge.d | 16 | 64 | 32,000 | 18,000 |  |

|  | 16 cores, 128 GB | dds.shar d.8x.4xla rge.d | 16 | 128 | 32,000 | 36,000 |  |
|---|---|---|---|---|---|---|---|
|  | 32 cores, 64 GB | dds.shar d.2x.8xla rge.d | 32 | 64 | 32,000 | 18,000 |  |
|  | 32 cores, 128 GB | dds.shar d.4x.8xla rge.d | 32 | 128 | 96,000 | 36,000 |  |
|  | 32 cores, 256 GB | dds.shar d.8x.8xla rge.d | 32 | 256 | 96,000 | 72,000 |  |
|  | 64 cores, 128 GB | dds.shar d.2x.16xl arge.d | 64 | 128 | 96,000 | 36,000 |  |
|  | 64 cores, 256 GB | dds.shar d.4x.16xl arge.d | 64 | 256 | 128,000 | 72,000 |  |
|  | 64 cores, 512 GB | dds.shar d.8x.16xl arge.d | 64 | 512 | 128,000 | 144,000 |  |

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | capacity (GB) |
| General- purpose | 2 cores, 4 GB | dds.cs.2x .large.c | 2 | 4 | 3,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.cs.2x .xlarge.c | 4 | 8 | 6,000 | 8,000 |  |
|  | 8 cores, 16 GB | dds.cs.2x .2xlarge. c | 8 | 16 | 12,000 | 8,000 |  |
| 3 |  |  |  |  |  |  |  |

**ConfigServer specifications**

**Supported specifications (MongoDB 5.0 to 8.0)**

|  | 16 cores, 32 GB | dds.cs.2x .4xlarge. c | 16 | 32 | 16,000 | 14,000 |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | 20 to 2,000 |
| Dedicate d | 4 cores, 8 GB | dds.cs.2x .xlarge.d | 4 | 8 | 8,000 | 8,000 |  |
|  | 4 cores, 16 GB | dds.cs.4x .xlarge.d | 4 | 16 | 8,000 | 8,000 |  |
|  | 8 cores, 16 GB | dds.cs.2x .2xlarge. d | 8 | 16 | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB | dds.cs.4x .2xlarge. d | 8 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 32 GB | dds.cs.2x .4xlarge. d | 16 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 64 GB | dds.cs.4x .4xlarge. d | 16 | 64 | 32,000 | 16,000 |  |

| Instance type | Specific ations | Specific ation code | CPU cores | Memory (GB) | Maximu m connecti ons | IOPS | Storage capacity (GB) |
|---|---|---|---|---|---|---|---|
| General- purpose | 1 core, 2 GB | dds.cs.mi d | 1 | 2 | 8,000 | 8,000 |  |
|  | 2 cores, 4 GB | dds.cs.st andard | 2 | 4 | 8,000 | 8,000 |  |
|  | 4 cores, 8 GB | dds.cs.lar ge | 4 | 8 | 8,000 | 8,000 |  |
|  | 8 cores, 16 GB | dds.cs.xl arge | 8 | 16 | 8,000 | 8,000 |  |

**Supported specifications (MongoDB 3.4 to 4.2)**

|  | 8 cores, 32 GB | dds.cs.2x large | 8 | 32 | 16,000 | 14,000 |  |
|---|---|---|---|---|---|---|---|
|  | 16 cores, 64 GB | dds.cs.4x large | 16 | 64 | 32,000 | 16,000 |  |
|  |  |  |  |  |  |  | 20 to 2,000 |
| Dedicate d | 4 cores, 8 GB (dedicate d) | dds.cs.2x .xlarge.d | 4 | 8 | 8,000 | 8,000 |  |
|  | 4 cores, 16 GB (dedicate d) | dds.cs.4x .xlarge.d | 4 | 16 | 8,000 | 8,000 |  |
|  | 8 cores, 16 GB (dedicate d) | dds.cs.2x .2xlarge. d | 8 | 16 | 12,000 | 8,000 |  |
|  | 8 cores, 32 GB (dedicate d) | dds.cs.4x .2xlarge. d | 8 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 32 GB (dedicate d) | dds.cs.2x .4xlarge. d | 16 | 32 | 16,000 | 14,000 |  |
|  | 16 cores, 64 GB (dedicate d) | dds.cs.4x .4xlarge. d | 16 | 64 | 32,000 | 16,000 |  |

## Quick start

### Use ApsaraDB for MongoDB

This topic is a quick start guide to basic usage operations for ApsaraDB for MongoDB, such as creating an instance, configuring a whitelist, and connecting to an instance. Flowcharts are used to describe the basic procedures in ApsaraDB for MongoDB, and guide you to create an ApsaraDB for MongoDB instance. An instance is a virtual database server on which you can create and manage multiple databases. After you create an ApsaraDB for MongoDB instance, you need to configure a whitelist for the instance to allow external devices to access the instance. A whitelist can enhance access security for ApsaraDB for MongoDB instances. We recommend that you update the whitelist on a regular basis. The normal services of the instance are not affected if you configure a whitelist.

#### Use the mongo shell to connect to an ApsaraDB for MongoDB instance

After you create an instance and configure a whitelist, you can use the mongo shell to connect to the instance.

### Create an instance

#### Create a replica set instance

This topic describes how to create a replica set instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set instance List** page, click **+ Create an instance** in the upper-left
corner.

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Organization | The organization where you want to deploy the instance. |
|  | Resource Set | The resource set where you want to deploy the instance. |
| Area | Region | The region where you want to deploy the instance. |
|  | Deployment Method | Single Zone: The primary, secondary, and hidden nodes are deployed in one zone. Dual Availability Zones: The primary, secondary, and hidden nodes are deployed in two zones to meet the requirements of zone- disaster recovery. Three available areas: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone- disaster recovery. |
|  | Primary Availability Zone | Select a primary zone for the instance. Note If you select dual zones, the instance supports zone-disaster recovery across two data centers. |

4. On the **Create a MongoDB instance** page, configure the parameters described in the
following table.

|  | Secondary Availability Zone | The zone in which the secondary instance is deployed. Note This parameter is required only when you select Dual Availability Zones or Three available areas for the Deployment Method parameter. |
|---|---|---|
|  | Third Availability Zone | Select the third availability zone of the instance. Note This parameter is required only when you select Three available areas for the Deployment Method parameter. |
|  | Chip Architecture | The chip architecture of the host where you want to deploy the instance. Note If you do not have permissions to select an option, contact the operations administrator to grant permissions to your account. |
|  | Database Engine | The database engine of the instance. Set the value to MongoDB. |
|  | Database Version | The database engine version of the instance. Valid values: 8.0 7.0 6.0 5.0 4.2 4.0 3.4 3.0 |

| Specification Configuration |  |  |
|---|---|---|
|  | Number of primary and standby nodes | The number of active-standby nodes in the replica set instance. Configure this parameter based on your business requirements. |
|  | Number of read-only nodes | The number of read-only nodes in the replica set instance. Configure this parameter based on your business requirements. |
|  | Specification Type | The instance type of the instance. Valid values: General-Purpose: Instances of this type exclusively use the allocated memory and I/O resources, while CPU and storage resources are shared with other general- purpose instances on the same server. Dedicated: Instances of this type exclusively use CPU, memory, storage, and I/O resources. Performance remains stable over time and is not affected by the behavior of other instances on the same server. Exclusive Physical Machine: Instances of this type are the highest-tier dedicated instances, also referred to as dedicated host instances. All resources of a physical server are exclusively allocated to a single instance. |
|  | Node Specifications | The node specifications of the instance. Select an option based on your actual needs. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |

|  | Storage Space (GB) | The storage space of the instance. This space contains the space for data, system files, log files, and transaction files. For more information, see Replica set instance types in ApsaraDB for MongoDB Product Introduction. |
|---|---|---|
| Network | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. Note If you select the Proprietary Network network type, you must specify the Private network vpc and Switch vswitch parameters. |
|  | Private network vpc | The VPC where you want to deploy the instance. If no VPCs are available, click Create a VPC to the right of the drop- down list. Note If Network Type is set to Proprietary Network, you must specify this parameter. |

|  | Switch vswitch | The vSwitch in the VPC. If no vSwitches are available, click Create a switch to the right of the drop-down list. Note If Network Type is set to Proprietary Network, you must specify this parameter. |
|---|---|---|
|  | Instance Name | The name of the instance. The name must meet the following requirements: It must start with a letter. It can contain digits, letters, underscores ( ), and _ hyphens (-). It must be 2 to 256 characters in length. |
|  | Set Password | The time when you want to set the password. Valid values: Set up now: immediately sets the login password. Set up after creation: sets the login password after instance creation. For more information, see Reset a password. |
| Password Settings |  |  |

|  | Login password | The password used to log in to the instance. The password must meet the following requirements: It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! # $ % ^ & * ( ) + = _ It must be 8 to 32 characters in length. Note If Set Password is set to Set up now, this parameter is required. |
|---|---|---|
|  | Confirm password | Enter the password again. The password that you enter must be the same as that in Login password. Note If Set Password is set to Set up now, this parameter is required. |

| Section | Parameter | Description |
|---|---|---|

5. Click **Submit**.

#### Create a sharded cluster instance

This topic describes how to create a sharded cluster instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **List of sharded cluster instances** page, click **+ Create an instance**.
4. On the **Create a MongoDB instance - Sharding** page, configure the parameters
described in the following table.

| Basic configuration | Organization | The organization where you want to deploy the instance. |
|---|---|---|
|  | Resource Set | The resource set where you want to deploy the instance. |
| Region | Region | The region where you want to deploy the instance. |
|  | Deployment method | Single Availability Zone: The primary, secondary, and hidden nodes are deployed in one zone. Dual Availability Zones: The primary, secondary, and hidden nodes are deployed in two zones to meet the requirements of zone-disaster recovery. Three Availability Zones: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone-disaster recovery. |
|  | Primary Availability Zone | Select a primary zone for the instance. Note If you select dual-zone, the instance supports zone- disaster recovery across two data centers. |
|  | Secondary Availability Zone | The zone in which the secondary instance is deployed. Note This parameter is required only when you select Dual Availability Zones or Three Availability Zones for the Deployment method parameter. |
|  | Third Availability Zone | Select the third availability zone for the instance. Note This parameter is required only when you select Three Availability Zones for the Deployment method parameter. |

| Specification Configuration | Chip architecture | The chip architecture of the host where you want to deploy the instance. Note If you do not have permissions to select a chip architecture, contact the operations administrator to grant permissions to your account. |
|---|---|---|
|  | Database engine | The database engine of the instance. Set the value to MongoDB. |
|  | Database version | The database engine version of the instance. Valid values: 8.0 7.0 6.0 5.0 4.2 4.0 3.4 |
|  | Network type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Virtual Private Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. Note If you select the Virtual Private Network network type, you must specify the Virtual Private Cloud (VPC) and Switch vswitch parameters. |

|  | IP Type | IPv4: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks. Dual-Stack (IPv4/IPv6): assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance. Note To configure this parameter, you must enable IPv6 first. For more information, see the "Enable IPv6 for ApsaraDB for MongoDB" topic in O&M Guide. If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB. |
|---|---|---|
| Network |  |  |
|  | Virtual Private Cloud (VPC) | The VPC where you want to deploy the instance. If no VPCs are available, click Create a VPC to the right of the drop- down list. Note If Network type is set to Virtual Private Network, this parameter is required. |
|  | Switch vswitch | The vSwitch in the VPC. If no vSwitches are available, click Create a switch to the right of the drop-down list. Note If Network type is set to Virtual Private Network, this parameter is required. |
|  | IPv4 Whitelist | Add IPv4 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note We recommend that you use private CIDR blocks defined in RFC 1918 for the VPC, such as 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16. |

|  | IPv6 Whitelist | Add IPv6 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note Take note of the following requirements when you add addresses to the IPv6 whitelist: An IPv6 address consists of eight segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0000:0000:0000:0000:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once. The prefix length must be specified, which is an integer from 0 to 128, following a forward slash (/). Example: 2001:db8::/32. fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address. ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments. fe80::/10 is a link-local address similar to IPv4 addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it. |
|---|---|---|
| Mongos specification configuration | Mongos specification | The specifications of the mongos node. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |
|  | Quantity | The number of mongos nodes. You can select 2 to 32 mongos nodes. |
|  | Custom name for mongos | The custom name of the mongos node. |
| Shard specification configuration | Shard specification | The specifications of the shard. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |
|  | Storage Space (GB) | The storage space of the shard. This space stores data, system files, log files, and transaction files. For more information, see Sharded cluster instance types in ApsaraDB for MongoDB Product Introduction. |
|  | Quantity | The number of shards. You can select 2 to 32 shards. |
| Document Version: 2 | 0260630 3 |  |

|  | Shard custom name | The custom name of the shard. |
|---|---|---|
| Configserver specification configuration | Configserver specification | The specifications of the ConfigServer component. Set the value to 1 vCPU, 2 GB. |
|  | Disk Space (GB) | The storage space of the ConfigServer component. Set the value to 20. |
|  | Custom name for configserver | The custom name of the ConfigServer component. |
| Password Setup | Instance Name | The name of the instance. The name must meet the following requirements: It must start with a letter. It can contain digits, letters, underscores ( ), and _ hyphens (-). It must be 2 to 256 characters in length. |
|  | Set a password | The time when you want to set the password. Valid values: Set up now: immediately sets the login password. Set After Creation: sets the password after the instance is created. For more information, see Reset a password. |
|  | Login password | The password used to log in to the instance. The password must meet the following requirements: It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! # $ % ^ & * ( ) + = _ It must be 8 to 32 characters in length. Note If Set a password is set to Set up now, this parameter is required. |
|  | Confirm password | Enter the password again. The password that you enter must be the same as that in Login password. Note If Set a password is set to Set up now, this parameter is required. |

| Parameter | Description |
|---|---|
| New Password | The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! # $ % ^ & * ( ) + - = _ The password must be 8 to 32 characters in length. You must not use keywords such as Admin or Password. |
| Confirm new password | Enter the password again. The password you enter must be the same as that in New Password. |

5. Click **Submit**.

### Reset a password

This topic describes how to reset the password of an account in the ApsaraDB for MongoDB console. For data security purposes, we recommend that you change the password of your account on a regular basis.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, click **Accounts**.
5. Find the account for which you want to change the password and click **Reset Password** in
the **Operation** column.
6. In the **Reset account password** dialog box, configure the following parameters.
7. Click **OK**.

### Configure a whitelist

This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or CIDR blocks to an instance whitelist to allow access from those addresses. This improves database security and stability. Proper configuration of whitelists can enhance the security of access to ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis.

**Background information**

The system creates a default whitelist for each instance. This whitelist can be modified or cleared but cannot be deleted. After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the **default** whitelist of the instance. The IP address 127.0.0.1 indicates that no IP addresses are allowed to access the instance.

| Parameter | Description |
|---|---|
| Group name | The group name must be 2 to 32 characters in length. It can contain lowercase letters, digits, and underscores ( ) and must start with a _ lowercase letter and end with a lowercase letter or a digit. |
| Type | You can select IPv4 or IPv6. |
| Whitelist within a group | Take note of the following requirements when you add IP addresses to the whitelist: Separate multiple IP addresses with commas (,). A maximum of 1,000 unique IP addresses can be added. You can specify IP addresses in the following formats: IPv4: 10.23.12.24 (specific IPv4 address) or 10.23.12.24/24 (CIDR block with a prefix length ranging from 1 to 32). IPv6: 2001:db8::1 (specific IPv6 address) or 2001:db8::/32 (CIDR block with a prefix length ranging from 1 to 128). Note If you enter a CIDR block whose prefix length is 0, such as 0.0.0.0/0 or ::/0, all IP addresses are allowed to access the instance. This poses a high security risk. Proceed with caution. Examples Allow a single IPv6 address: 2001:db8:85a3::8a2e:370:7334 Allow an IPv6 CIDR block: 240e:390:a100::/44 Allow all IP addresses (high risk): ::/0 or 0.0.0.0/0 |

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
5. Click **Add a whitelist Group** above the list.
6. In the **New name adding list groups (up to 50 groups supported)** panel, configure
parameters.

| Import file (.txt) | You can import IP addresses in batches. |
|---|---|
| Load the private IP addresses of ECS instances | i. Select Import ECS Internal IP Address. ii. Select IP addresses based on your business requirements. Note To find the Elastic Compute Service (ECS) instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |

| Parameter | Description |
|---|---|

7. Click **OK**.

### Connect to an instance

#### Use DMS to log on to an ApsaraDB for

**MongoDB instance**

You can use Data Management (DMS) to log on to an ApsaraDB for MongoDB instance.

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure a whitelist.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the upper-right corner of the page, click **Log On**.

**Note**

For a sharded cluster instance, you must also select a mongos node. Log on to the **DMS** console.
5. In the **Login instance** dialog box, configure the parameters described in the following
table.

| Database Type | The database engine of the instance. By default, this parameter is set to the database engine of the instance that you want to access. |
|---|---|
| Instance Region | The region where the instance is deployed. By default, this parameter is set to the region where the current instance is deployed. |
| Connection string address | The connection string of the instance. By default, this parameter is set to the connection string of the current instance. |
| Database Name | The name of the database. By default, this parameter is set to admin. |
| Database Account | The account used to connect to the database. By default, this parameter is set to root. |
| Database Password | The password of the account used to connect to the database. |

6. Click **Login**.

**Note**

You can select **Remember password** to eliminate the need to manually enter the password again the next time you log on to the database.

#### Use the mongo shell to connect to an

**ApsaraDB for MongoDB instance**

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by MongoDB. You can install MongoDB on your client and use the mongo shell to connect to an ApsaraDB for MongoDB instance.

**Prerequisites**

The version of MongoDB that you install on your client is the same as that of your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about how to install MongoDB, see Install MongoDB.

**Note**

You can select a MongoDB version corresponding to your client version in the upper-left corner of the page. The IP address of your client is added to an IP address whitelist of your ApsaraDB for MongoDB instance. For more information, see Configure a whitelist.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, find the instance
that you want to manage and click the ID of the instance.
4. In the left-side navigation pane, click **Database Connections** to obtain the endpoints.

**Note**

If the instance is a replica set instance, obtain the endpoint or connection string URI of a node. If the instance is a sharded cluster instance, obtain the endpoint or connection string URI of a mongos node. For more information about endpoints, see Overview of replica set instance connections or Overview of sharded cluster instance connections.
5. Connect to a database of the instance from your client on which the mongo shell is
installed. If the instance is a replica set instance, the following methods are available: High-availability (HA) connection (recommended) You can use a connection string URI to connect to both the primary and secondary nodes in the instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched. Command syntax:

```
mongo "<ConnectionStringURI>"
```

**Note**

The connection string URI must be enclosed in a pair of double quotation marks (""). <ConnectionStringURI>: the connection string URI of the instance. You must replace `****` in the connection string URI with the database password. For more information about how to specify a database password, see Reset the password. Example:

```
mongo "mongodb://root:****@dds-
**********.mongodb.rds.intra.env17e.shuguang.com:3717,dds-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
```

`*"` Single-node connection In most cases, you can directly connect to the primary node or a secondary or readonly node. If the primary node fails, the system automatically switches to a secondary node and the secondary node becomes the primary node. This affects the read and write operations of your application. Command syntax:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database>
```

**Note**

<host>: the endpoint of the primary or secondary node. <username>: the username used to log on to a database of the instance. The initial username is **root**. <database>: the name of the database corresponding to the username for which authentication is enabled. If the username is root, enter admin. Example:

```
mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenti cationDatabase admin
```

When the `Enter password:` message is displayed, enter the password of the username and press the Enter key. If you forget the password of the root account, you can reset the password. For more information, see Reset the password.

**Note**

The password characters are masked when you enter the password. If the instance is a sharded cluster instance, the following methods are available: HA connection (recommended) You can use a connection string URI to connect to a database of the instance. If one mongos node fails, the system switches to another mongos node to ensure the HA of the connection. Command syntax:

```
mongo "<ConnectionStringURI>"
```

**Note**

The connection string URI must be enclosed in a pair of double quotation marks (""). <ConnectionStringURI>: the connection string URI of the instance. You must replace `****` in the connection string URI with the database password. For more information about how to specify a database password, see Reset the password. Example:

```
mongo "mongodb://root:****@s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
```

| Item | Description |
|---|---|

Mongos node connection Command syntax:

```
mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
```

**Note**

<mongos_host>: the endpoint of a mongos node in the instance. <username>: the username used to log on to a database of the instance. The initial username is **root**. <database>: the name of the database corresponding to the username for which authentication is enabled. If the username is root, enter admin. Example:

```
mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authentica tionDatabase admin
```

#### Introduction to connection strings and

**URIs**

##### Overview of replica set instance

**connections**

ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node and use a connection string URI to connect to both of them. For high availability (HA), we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections.

**Prerequisites**

A whitelist is configured for the instance. For more information, see Configure a whitelist.

**Obtain connection strings**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set Instances** page, click the ID of an instance.
4. In the left-side navigation pane, click **Database Connections** to obtain connection strings.

**Description of connection strings**

| Connection address type | Classic network endpoint: Classic network connection is a type of internal connection, and classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists. VPC endpoint: Virtual Private Cloud (VPC) connection is a type of internal connection, and VPC endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and higher performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance. Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |
|---|---|
| Role | Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance. Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance. Connection string URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and HA. |
| Connection string | The connection string of a primary or secondary node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port number used to connect to the instance. |
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to a database of the instance. You must separate them with a colon (:). hostX:portX: the endpoint and port number used to connect to the instance. /database: the name of the database corresponding to the username if authentication is enabled. options: the additional options that are used to connect to the instance. Note We recommend that you use the URI to connect to the instance in a production environment. This way, when a node fails, the read and write operations of your application are not affected by the failover. |

**Related topics**

#### Use the mongo shell to connect to an ApsaraDB for MongoDB instance

| Item | Description |
|---|---|
| Connection address type | Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists. VPC endpoint: Virtual Private Cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance. Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |

##### Overview of sharded cluster instance

**connections**

ApsaraDB for MongoDB sharded cluster instances support both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node and use a connection string URI to connect to multiple mongos nodes. For high availability (HA), we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections.

**View connection strings**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of the instance whose connection
strings you want to view.
4. In the left-side navigation pane, click **Database Connections** to view connection strings.

**Description of connection strings**

| Mongos node ID | The connection string of a mongos node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port number used to connect to the instance. Note During routine tests, you can use a connection string to directly connect to a mongos node. |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to the instance. You must separate them with a colon (:). hostX:portX: the endpoint and port number used to connect to the instance. /database: the name of the database corresponding to the username if authentication is enabled. options: the additional options that are used to connect to the instance. Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads. If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Organization | The organization where you want to deploy the instance. |
|  | Resource Set | The resource set where you want to deploy the instance. |
|  | Region | The region where you want to deploy the instance. |
|  | Deployment Method | Single Zone: The primary, secondary, and hidden nodes are deployed in one zone. Dual Availability Zones: The primary, secondary, and hidden nodes are deployed in two zones to meet the requirements of zone- disaster recovery. Three available areas: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone- disaster recovery. |

t

## Instance management

### Create an instance

#### Create a replica set instance

This topic describes how to create a replica set instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set instance List** page, click **+ Create an instance** in the upper-left
corner.
4. On the **Create a MongoDB instance** page, configure the parameters described in the
following table.

| Area |  |  |
|---|---|---|
|  | Primary Availability Zone | Select a primary zone for the instance. Note If you select dual zones, the instance supports zone-disaster recovery across two data centers. |
|  | Secondary Availability Zone | The zone in which the secondary instance is deployed. Note This parameter is required only when you select Dual Availability Zones or Three available areas for the Deployment Method parameter. |
|  | Third Availability Zone | Select the third availability zone of the instance. Note This parameter is required only when you select Three available areas for the Deployment Method parameter. |
|  | Chip Architecture | The chip architecture of the host where you want to deploy the instance. Note If you do not have permissions to select an option, contact the operations administrator to grant permissions to your account. |

t

|  | Database Engine | The database engine of the instance. Set the value to MongoDB. |
|---|---|---|
| Specification Configuration |  |  |
|  | Database Version | The database engine version of the instance. Valid values: 8.0 7.0 6.0 5.0 4.2 4.0 3.4 3.0 |
|  | Number of primary and standby nodes | The number of active-standby nodes in the replica set instance. Configure this parameter based on your business requirements. |
|  | Number of read-only nodes | The number of read-only nodes in the replica set instance. Configure this parameter based on your business requirements. |

t

|  | Specification Type | The instance type of the instance. Valid values: General-Purpose: Instances of this type exclusively use the allocated memory and I/O resources, while CPU and storage resources are shared with other general- purpose instances on the same server. Dedicated: Instances of this type exclusively use CPU, memory, storage, and I/O resources. Performance remains stable over time and is not affected by the behavior of other instances on the same server. Exclusive Physical Machine: Instances of this type are the highest-tier dedicated instances, also referred to as dedicated host instances. All resources of a physical server are exclusively allocated to a single instance. |
|---|---|---|
|  | Node Specifications | The node specifications of the instance. Select an option based on your actual needs. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |
|  | Storage Space (GB) | The storage space of the instance. This space contains the space for data, system files, log files, and transaction files. For more information, see Replica set instance types in ApsaraDB for MongoDB Product Introduction. |

t

|  | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. Note If you select the Proprietary Network network type, you must specify the Private network vpc and Switch vswitch parameters. |
|---|---|---|

t

|  | IP Type | IPv4: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks. IPv4/IPv6 Dual-Stack: assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance. Note To configure this parameter, you must enable IPv6 first. For more information, see the "Enable IPv6 for ApsaraDB for MongoDB" topic in O&M Guide. If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB. |
|---|---|---|

t

| Network |  |  |
|---|---|---|
|  | Private network vpc | The VPC where you want to deploy the instance. If no VPCs are available, click Create a VPC to the right of the drop- down list. Note If Network Type is set to Proprietary Network, you must specify this parameter. |
|  | Switch vswitch | The vSwitch in the VPC. If no vSwitches are available, click Create a switch to the right of the drop-down list. Note If Network Type is set to Proprietary Network, you must specify this parameter. |
|  | IPv4 Whitelist | Add IPv4 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note We recommend that you use private CIDR blocks defined in RFC 1918 for the VPC, such as 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16. |
|  |  | Add IPv6 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note Take note of the following requirements when you add addresses to the IPv6 whitelist: |

t

|  |  |  | An IPv6 address consists of eight |  |
|---|---|---|---|---|
|  | IPv6 Whitelist | segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0 000:0000:0000:00 00:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once. The prefix length must be specified, which is an integer from 0 to 128, following a forward slash (/). Example: 2001:db8::/32. fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address. ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments. fe80::/10 is a link- local address similar to IPv4 addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it. | segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0 000:0000:0000:00 00:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once. The prefix length must be specified, which is an integer from 0 to 128, following a forward slash (/). Example: 2001:db8::/32. fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address. ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments. fe80::/10 is a link- local address similar to IPv4 addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it. |  |

t

| Password Settings | Instance Name | The name of the instance. The name must meet the following requirements: It must start with a letter. It can contain digits, letters, underscores ( ), and _ hyphens (-). It must be 2 to 256 characters in length. |
|---|---|---|
|  | Set Password | The time when you want to set the password. Valid values: Set up now: immediately sets the login password. Set After Creation: sets the password after the instance is created. For more information, see Reset a password. |
|  | Login password | The password used to log in to the instance. The password must meet the following requirements: It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! # $ % ^ & * ( ) + = _ It must be 8 to 32 characters in length. Note If Set Password is set to Set up now, this parameter is required. |
|  | Confirm password | Enter the password again. The password that you enter must be the same as that in Login password. Note If Set Password is set to Set up now, this parameter is required. |

t

| Section | Parameter | Description |
|---|---|---|
| Basic configuration | Organization | The organization where you want to deploy the instance. |
|  | Resource Set | The resource set where you want to deploy the instance. |
| Region | Region | The region where you want to deploy the instance. |
|  | Deployment method | Single Availability Zone: The primary, secondary, and hidden nodes are deployed in one zone. Dual Availability Zones: The primary, secondary, and hidden nodes are deployed in two zones to meet the requirements of zone-disaster recovery. Three Availability Zones: The primary, secondary, and hidden nodes are deployed in three zones to meet the requirements of zone-disaster recovery. |
|  | Primary Availability Zone | Select a primary zone for the instance. Note If you select dual-zone, the instance supports zone- disaster recovery across two data centers. |
|  | Secondary Availability Zone | The zone in which the secondary instance is deployed. Note This parameter is required only when you select Dual Availability Zones or Three Availability Zones for the Deployment method parameter. |

t
5. Click **Submit**.

#### Create a sharded cluster instance

This topic describes how to create a sharded cluster instance in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **List of sharded cluster instances** page, click **+ Create an instance**.
4. On the **Create a MongoDB instance - Sharding** page, configure the parameters
described in the following table.

|  | Third Availability Zone | Select the third availability zone for the instance. Note This parameter is required only when you select Three Availability Zones for the Deployment method parameter. |
|---|---|---|
|  | Chip architecture | The chip architecture of the host where you want to deploy the instance. Note If you do not have permissions to select a chip architecture, contact the operations administrator to grant permissions to your account. |
| Specification Configuration | Database engine | The database engine of the instance. Set the value to MongoDB. |
|  | Database version | The database engine version of the instance. Valid values: 8.0 7.0 6.0 5.0 4.2 4.0 3.4 |
|  | Network type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Virtual Private Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. Note If you select the Virtual Private Network network type, you must specify the Virtual Private Cloud (VPC) and Switch vswitch parameters. |

t

|  | IP Type | IPv4: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks. Dual-Stack (IPv4/IPv6): assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance. Note To configure this parameter, you must enable IPv6 first. For more information, see the "Enable IPv6 for ApsaraDB for MongoDB" topic in O&M Guide. If the system prompts that you are not authorized, see Authorize a tenant organization to access SLB. |
|---|---|---|
| Network |  |  |
|  | Virtual Private Cloud (VPC) | The VPC where you want to deploy the instance. If no VPCs are available, click Create a VPC to the right of the drop- down list. Note If Network type is set to Virtual Private Network, this parameter is required. |
|  | Switch vswitch | The vSwitch in the VPC. If no vSwitches are available, click Create a switch to the right of the drop-down list. Note If Network type is set to Virtual Private Network, this parameter is required. |
|  | IPv4 Whitelist | Add IPv4 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note We recommend that you use private CIDR blocks defined in RFC 1918 for the VPC, such as 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16. |

t

|  | IPv6 Whitelist | Add IPv6 addresses that are allowed to access the ApsaraDB for MongoDB instance. Note Take note of the following requirements when you add addresses to the IPv6 whitelist: An IPv6 address consists of eight segments of hexadecimal numbers separated by colons (:). Each segment consists of four characters. Example: 2001:0db8:0000:0000:0000:0000:0000:0001. Shorthand notation is supported, such as 2001:db8::1. Consecutive zero segments can be replaced by "::" only once. The prefix length must be specified, which is an integer from 0 to 128, following a forward slash (/). Example: 2001:db8::/32. fc00::/7 is a unique local address similar to IPv4 CIDR blocks starting with 192.168. It can be used only for private networks. We recommend that you use this address. ::/0 specifies all IPv6 addresses. We recommend that you do not use it in production environments. fe80::/10 is a link-local address similar to IPv4 addresses starting with 169.254. It is used for automatic configuration and direct communication of devices in LANs. We recommend that you do not use it. |
|---|---|---|
|  | Mongos specification | The specifications of the mongos node. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |

t

| er Guide·Instance m | anagemen ApsaraDB for MongoDB |  |
|---|---|---|
| Mongos specification configuration |  |  |
|  | Quantity | The number of mongos nodes. You can select 2 to 32 mongos nodes. |
|  | Custom name for mongos | The custom name of the mongos node. |
| Shard specification configuration | Shard specification | The specifications of the shard. You can log in to the ApsaraDB for MongoDB console to view the detailed specifications. |
|  | Storage Space (GB) | The storage space of the shard. This space stores data, system files, log files, and transaction files. For more information, see Sharded cluster instance types in ApsaraDB for MongoDB Product Introduction. |
|  | Quantity | The number of shards. You can select 2 to 32 shards. |
|  | Shard custom name | The custom name of the shard. |
| Configserver specification configuration | Configserver specification | The specifications of the ConfigServer component. Set the value to 1 vCPU, 2 GB. |
|  | Disk Space (GB) | The storage space of the ConfigServer component. Set the value to 20. |
|  | Custom name for configserver | The custom name of the ConfigServer component. |
|  | Instance Name | The name of the instance. The name must meet the following requirements: It must start with a letter. It can contain digits, letters, underscores ( ), and _ hyphens (-). It must be 2 to 256 characters in length. |
|  | Set a password | The time when you want to set the password. Valid values: Set up now: immediately sets the login password. Set After Creation: sets the password after the instance is created. For more information, see Reset a password. |

t

| Password Setup |  |  |
|---|---|---|
|  | Login password | The password used to log in to the instance. The password must meet the following requirements: It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! # $ % ^ & * ( ) + = _ It must be 8 to 32 characters in length. Note If Set a password is set to Set up now, this parameter is required. |
|  | Confirm password | Enter the password again. The password that you enter must be the same as that in Login password. Note If Set a password is set to Set up now, this parameter is required. |

t
5. Click **Submit**.

### View the details of an

**ApsaraDB for MongoDB instance**

This topic describes how to view the details of an ApsaraDB for MongoDB instance, such as the basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. Go to the basic information page by using one of the following methods:
Find the instance that you want to view and click its ID to go to the **Basic Information** page. Then, you can view the details of the instance. in the **Actions** column corresponding to the instance that you want to view and select **Manage** to go to the **Basic Information** page. Then, you can view the details of the instance.

### Restart an instance

This topic describes how to restart an instance when instance connections reach the upper limit or your instances have performance issues. This topic describes how to restart an ApsaraDB for MongoDB instance.

**Prerequisites**

t The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. Click **Restart Instance** in the upper-right corner.

**Note**

When an ApsaraDB for MongoDB instance is restarted, all its connections are closed. Plan your operations in advance before you restart an ApsaraDB for MongoDB instance. You can also find the instance that you want to restart, click in the **Actions** column, and then select **Restart**.
5. In the **Restart Instance** message, click **OK**.

### Change the configurations of

**a replica set instance**

This topic describes how to change the configurations of an ApsaraDB for MongoDB instance. You can upgrade or downgrade an ApsaraDB for MongoDB instance to meet your business requirements.

**Prerequisites**

The instance is a replica set instance.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set Instances** page, click the ID of an instance, or click
in the **Actions** column corresponding to the instance and select **Manage**.
4. In the upper-right corner of the Specification Information section of the page that appears,
click **Change Configuration** to go to the **Modify Instance** page. t

**Note**

You can also click in the **Actions** column corresponding to the instance and select **Change Configuration** on the **Replica Set Instances** page to go to the
**Modify Instance** page.
5. On the **Modify Instance** page, change the instance configurations.
You can change the values of the following parameters:

**Node Type**

**Node Specification**

**Storage Capacity (GB)**

6. Click **Submit**.

### Change the configurations of

**a sharded cluster instance**

#### Add a mongos node

This topic describes how to add a mongos node to an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability. When mongos nodes are added, your business keeps running without interruption. Typically, mongos nodes are added within 5 minutes. The time required to add mongos nodes is not dependent on the number of mongos nodes being added.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance, or click
in the
**Actions** column corresponding to the instance and select **Manage**.
4. In the **Mongos List** section of the page that appears, click **Add Mongos**.
5. In the **MongoDB sharded cluster add node** panel, click **Add a new item**, and configure
the **Specifications** and **Quantity** parameters.
6. Click **Submit**.
t

#### Add a shard node

This topic describes how to add a shard node to an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability. When shard nodes are added, no transient connections occur and business keeps running without interruption. Typically, shard nodes are added within 5 minutes. The time required to add shard nodes does not depend on the number of shard nodes that are being added. The specifications of the new shard node must be higher than or equal to the highest specifications among all the shard nodes in the sharded cluster instance. For example, if the largest storage capacity among all the shard nodes in a sharded cluster instance is 10 GB, the storage capacity of the new shard node must be greater than or equal to 10 GB.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance, or click
in the
**Actions** column corresponding to the instance and select **Manage**.
4. In the **Shard List** section, click **Add Shard**.
5. On the **Add Nodes to MongoDB Sharded Cluster** page, configure the **Specifications**,
**Username**, and **Password** parameters. Then, click **Confirm Password**.

**Note**

When you change the value of the **Storage Capacity (GB)** parameter, make sure that the new storage capacity that you specify is greater than or equal to the largest storage capacity among all the shard nodes in the sharded cluster instance. The specifications of the new shard node must be higher than or equal to the highest specifications among all the shard nodes in the sharded cluster instance. For example, if the largest storage capacity among all the shard nodes in the sharded cluster instance is 10 GB, the storage capacity of the new shard node must be greater than or equal to 10 GB.
6. Click **Submit**.

#### Change the configurations of one or

**more mongos nodes**

t This topic describes how to change the configurations of one or more mongos nodes in an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

During a configuration change, one or two transient connections may occur. Each transient connection lasts about 30 seconds. To prevent a configuration change from interrupting your workloads, we recommend that you change configurations at a time that has minimal impact on your business. The amount of time required to perform a configuration change depends on factors such as the network conditions, task queue status, and data size. We recommend that you change the configurations of a sharded cluster instance during off-peak hours and make sure that your application can automatically reconnect to the instance. If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance, or click
in the
**Actions** column corresponding to the instance and select **Manage**.
4. In the **Mongos List** section of the page that appears, change the configurations of one or
more mongos nodes based on your business requirements. Change the configurations of a mongos node Find the mongos node that you want to manage and click the icon in the
**Actions** column. Then, select **Change Configuration**.
Change the configurations of multiple mongos nodes a. In the **Mongos List** section of the page that appears, select the mongos nodes that you want to manage. b. In the upper-left corner of the **Mongos List** section, click **Batch Reconfigure**.
5. In the **MongoDB sharded cluster configuration node** panel, configure the
**Specification configuration** parameter.
6. Click **Submit**.

#### Change the configurations of one or

**more shard nodes**

This topic describes how to change the configurations such as specifications and storage capacity of one or more shard nodes in an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

t During a configuration change, one or two transient connections may occur. Each transient connection lasts about 30 seconds. To prevent a configuration change from interrupting your workloads, we recommend that you change configurations at a time that has minimal impact on your business.

**Warning**

If you change only the storage capacity of an instance, the system performs the corresponding operation based on whether your host has sufficient storage resources. If your host has sufficient storage resources, the system scales out the storage space on your host without the need for cross-host migrations or failovers. Transient connections do not occur during the scale-out process. The scale-out task is immediately executed to completion. You do not need to wait for the maintenance window. If your host does not have sufficient storage resources, cross-host migrations and failovers are required. Transient connections may occur during the scale-out process. The scale-out task is executed during the specified maintenance window. The amount of time required to perform a configuration change depends on factors such as the network conditions, task queue status, and data size. We recommend that you change the configurations of a sharded cluster instance during off-peak hours and make sure that your application can automatically reconnect to the instance. If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability. The storage capacity that you specify must be greater than or equal to the used storage capacity on the shard node.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance, or click
in the
**Actions** column corresponding to the instance and select **Manage**.
4. In the **Shard List** section of the page that appears, change the configurations of one or
more shard nodes based on your business requirements. Change the configurations of a shard node Find the shard node that you want to manage and click the icon in the
**Actions** column. Then, select **Change Configuration**.
Change the configurations of multiple shard nodes a. In the **Shard List** section of the page that appears, select the shard nodes that you want to manage. b. In the upper-left corner of the **Shard List** section, click **Batch Reconfigure**.
5. In the **MongoDB sharded cluster configuration node** panel, configure the
**Specifications** and **Storage space** parameters.
6. Click **Submit**.
t

#### Change the configurations of a

**Configserver node**

This topic describes how to change the configurations of a Configserver node in an ApsaraDB for MongoDB sharded cluster instance.

**Usage notes**

During a configuration change, one or two transient connections may occur. Each transient connection lasts about 30 seconds. To prevent a configuration change from interrupting your workloads, we recommend that you change configurations at a time that has minimal impact on your business. The amount of time required to perform a configuration change depends on factors such as the network conditions, task queue status, and data size. We recommend that you change the configurations of a sharded cluster instance during off-peak hours and make sure that your application can automatically reconnect to the instance. If the minor version of a sharded cluster instance expires or is not maintained, ApsaraDB for MongoDB automatically updates the minor version of the instance to the latest version during a configuration change. This ensures that the sharded cluster instance can provide higher performance and higher stability.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance, or click
in the
**Actions** column corresponding to the instance and select **Manage**.
4. In the **ConfigServer List** section of the page that appears, find the Configserver node that
you want to manage and click the icon in the **Actions** column. Then, select
**Change Configuration**.
5. In the **MongoDB sharded cluster configuration node** panel, configure the
**ConfigServer specification** and **Disk space (GB)** parameters.
6. Click **Submit**.

### Change the name of an

**instance**

This topic describes how to change the name of an ApsaraDB for MongoDB instance to facilitate management.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
t instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. Click **Edit** to the right of **Instance Name**.

**Note**

The name must start with a letter. The name cannot start with http:// or https://. The name can contain letters, underscores (_), hyphens (-), and digits. The name must be 2 to 128 characters in length.
5. Click **OK**.

### Manage accounts

ApsaraDB for MongoDB supports the account management feature. You can create accounts and customize account permissions.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the
instance that you want to manage.
4. In the left-side navigation pane, click **Accounts**.
5. Click **Create Account**.
6. In the **Create Account** panel, enter an account and a password as prompted and grant
permissions to the account.
7. Click **OK**.

| Parameter | Description |
|---|---|
| New Password | The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! # $ % ^ & * ( ) + - = _ The password must be 8 to 32 characters in length. You must not use keywords such as Admin or Password. |
| Confirm new password | Enter the password again. The password you enter must be the same as that in New Password. |

t

**Note**

After you create the account, you can reset the password, modify the account permissions, and delete the account.

### Reset the password

This topic describes how to reset the password of an account in the ApsaraDB for MongoDB console. For data security purposes, we recommend that you change the password of your account on a regular basis.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, click **Accounts**.
5. Find the account for which you want to change the password and click **Reset Password** in
the **Operation** column.
6. In the **Reset account password** dialog box, configure the following parameters.
7. Click **OK**.

### Upgrade the MongoDB version

**of an instance**

ApsaraDB for MongoDB allows you to upgrade the MongoDB version of your instance. This topic describes how to upgrade the MongoDB version of your instance.

**Usage notes**

Nodes in an instance are upgraded in turn. An instance is automatically restarted two or three times during an upgrade. We recommend that you perform the upgrade during off-

| Instance architecture | MongoDB version before upgrade | MongoDB version after upgrade |
|---|---|---|
| Replica set instances | MongoDB 4.2 | N/A |
|  | MongoDB 4.0 | MongoDB 4.2 |
|  | MongoDB 3.4 | MongoDB 4.0 or MongoDB 4.2 |
|  | MongoDB 3.0 | MongoDB 3.4, MongoDB 4.0, or MongoDB 4.2 |
| Sharded cluster instances | MongoDB 4.2 | N/A |
|  | MongoDB 4.0 | MongoDB 4.2 |
|  | MongoDB 3.4 | MongoDB 4.0 or MongoDB 4.2 |

t peak hours or make sure that your application can automatically reconnect to the instance. The balancer of a sharded cluster instance is disabled during an upgrade and is enabled after the upgrade. The amount of time required to upgrade the MongoDB version of an instance is related to the data volume of databases in the instance. We recommend that you schedule your upgrade task during off-peak hours. You cannot downgrade the MongoDB version of an instance after you upgrade it.

**MongoDB versions available for upgrades**

The following table lists the MongoDB versions to which ApsaraDB for MongoDB instances of different architectures and versions can be upgraded.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. Find the instance that you want to manage and click the ID of the instance.
4. In the upper-right corner of the **Specification Information** section of the page that
appears, click **Upgrade Database** and select the version to which you want to upgrade the instance.
5. In the **Upgrade Database** message, click **OK**.

### Switch node roles

You can switch the node roles of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console based on your business deployment.

**Typical scenario**

When an Elastic Compute Service (ECS) instance and an ApsaraDB for MongoDB instance are connected in the same zone over an internal network, the latency is minimal. If they are connected across different zones, the latency increases and the performance of the ApsaraDB for MongoDB instance and your business is affected. t In this example, the ECS instance to which the application belongs is in Zone 2. If the primary node of the ApsaraDB for MongoDB instance is in Zone 1, the ECS instance needs to connect to the primary node across zones. To optimize the business deployment architecture, you can switch roles between the primary and secondary nodes. In this example, you can change the role of the node in Zone 2 to primary and the role of the node in Zone 1 to secondary. The ECS and ApsaraDB for MongoDB instances can be connected in the same zone. Each time you switch node roles, the instance may experience a transient connection of up to 30 seconds. Perform this operation during off-peak hours or make sure that your application can automatically re-establish a connection. Each time you switch node roles, only the node roles are changed and the zones and role IDs of nodes remain unchanged.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, click **Service Availability**.
5. On the **Service Availability** page, perform the subsequent operations based on the
corresponding instance architecture. Replica set instances a. Click **Switch Role** in the upper-right corner of the page. t b. In the **Switch Role** panel, select the node for which you want to switch the role. c. Click **OK**. Sharded cluster instances

**Note**

For sharded cluster instances, you can manage only the zone distribution of shard and Configserver nodes. a. In the upper-right corner of the **Zone Distribution for Shards** or **Zone Distribution**
**for Configservers** section, click **Switch Role**.
t b. In the **Switch Role** panel, select the node for which you want to switch the role. c. Click **OK**.

### Migrate an instance across

**multiple zones**

This topic describes how to migrate an ApsaraDB for MongoDB instance to a different zone within the same region. After an ApsaraDB for MongoDB instance is migrated to a different zone, the attributes, specifications, and connection addresses of the instance remain unchanged.

**Prerequisites**

The ApsaraDB for MongoDB instance is a replica set instance or sharded cluster instance that runs MongoDB 4.2 or earlier. Transparent data encryption (TDE) is disabled for the ApsaraDB for MongoDB instance. The source zone and the destination zone belong to the same region. If the instance is deployed in a virtual private cloud (VPC), make sure that a vSwitch is created in the destination zone before you start migration. For more information, see
**Create a VPC** and **Create a vSwitch** in **VPC User Guide**.
The ApsaraDB for MongoDB instance does not have a public endpoint. If you have applied for a public endpoint, you must release the public endpoint before you migrate the t ApsaraDB for MongoDB instance to a different zone. For more information about how to release a public endpoint, see Release a public endpoint. If the ApsaraDB for MongoDB instance resides in a VPC, the destination zone must also belong to the same VPC. The amount of time that is required for the migration varies based on factors such as the network conditions, task queue state, and data volume. We recommend that you migrate the instance during off-peak hours. During the migration, you may experience transient connections that last about 30 seconds. Make sure that your application is configured to automatically reconnect to the ApsaraDB for MongoDB instance. After the migration, the virtual IP addresses (VIPs) of the ApsaraDB for MongoDB instance change. A sample VIP is 172.16.88.60. If your application is connected to the ApsaraDB for MongoDB instance by using an original VIP after the migration, the application disconnects from the instance.

**Note**

We recommend that you connect your application to the ApsaraDB for MongoDB instance by using a connection string URI of the instance to ensure high availability. For more information, see Overview of replica set instance connections and Overview of sharded cluster instance connections.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the **Basic Information** section, click **Change Zone**.
5. In the **Migrate Instance to Other Zone** panel, configure the parameters based on the
network type of the instance. Migrate an ApsaraDB for MongoDB instance in a VPC to a different zone

| Parameter | Description |
|---|---|
| Migrate To | Select the destination zone. |
| Select a vSwitch | Select the destination vSwitch. |
| Migration Time | Select the time when you want to start the migration. Valid values: Switch Immediately after Migration: The migration immediately starts after you configure the parameters. Switch within Maintenance Window: The migration starts during the specified period. You can click Edit to the right of Switch within Maintenance Window to change the period. |

t Migrate an ApsaraDB for MongoDB instance in the classic network to a different zone

| Parameter | Description |
|---|---|
| Migrate To | Select the destination zone. |
| Migration Time | Select the time when you want to start the migration. Valid values: Switch Immediately after Migration: The migration immediately starts after you configure the parameters. Switch within Maintenance Window: The migration starts during the specified period. You can click Edit to the right of Switch within Maintenance Window to change the period. |

t
6. Read the prompt and select the check box.
7. Click **Submit**.

### Release an ApsaraDB for

**MongoDB instance**

This topic describes how to manually release an ApsaraDB for MongoDB instance to meet your business needs.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. On the page that appears, click **Release** in the lower-right corner of the **Basic**
**Information** section.

**Note**

You can also click in the **Actions** column corresponding to the instance and select **Release**.
5. In the **Release Instance** message, click **OK**.

**Warning**

After you release an ApsaraDB for MongoDB instance, data in the instance can no longer be recovered. Proceed with caution.

### Primary/secondary failover

#### Configure a primary/secondary

**switchover for a replica set instance**

t By default, an ApsaraDB for MongoDB replica set instance consists of three nodes. ApsaraDB for MongoDB provides connection strings for you to connect to the primary node and a secondary node. The other secondary node is hidden as a backup to ensure high availability (HA). If a node fails, the HA system of ApsaraDB for MongoDB automatically triggers a primary/secondary switchover to ensure the availability of the instance. You can also manually trigger a primary/secondary switchover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills.

**Prerequisites**

The instance is in the **Running** state.

**Background information**

After a primary/secondary switchover is triggered for a replica set instance, the system switches roles between the primary and secondary nodes in the instance. Each time you trigger a primary/secondary switchover for an instance, the instance may experience a transient connection of up to 30 seconds. Make sure that your applications can automatically re-establish a connection.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set Instances** page, click the ID of an instance, or click
in the **Actions** column corresponding to the instance and select **Manage**.
3. In the **Node List** section, click **Failover**.
4. In the **Failover** message, click **OK**.
5. The instance state changes to **Switching Role**. When the instance state changes to
**Running**, the switchover is successful.

**Note**

The switchover operation is complete in about 1 minute. After the switchover operation, you must use the connection string of the new primary node to connect to the instance if your original connection uses the connection string of the original primary node. This is because the original primary node becomes a secondary node that has no write permissions after the switchover. For more information, see Overview of replica set instance connections.

#### Configure a primary/secondary

**failover for a sharded cluster instance**

t By default, each shard or Configserver node of a sharded cluster instance consists of three nodes. If a node fails, the high availability system of ApsaraDB for MongoDB automatically triggers a primary/secondary failover to ensure the availability of the shard or Configserver node. You can also manually trigger a primary/secondary failover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills.

**Prerequisites**

The instance is in the **Running** state.

**Background information**

After a primary/secondary failover is triggered, the system switches roles between the primary and secondary nodes in a shard node. Each time you trigger a primary/secondary failover for an instance, the instance may experience a transient connection of up to 30 seconds. We recommend that you perform this operation during off-peak hours and ensure that your applications can automatically reestablish a connection.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the **Shard List** or **ConfigServer List** section, click
in the **Actions** column corresponding to the node for which you want to perform failover and select **Failover**.

**Note**

You can separately trigger a primary/secondary failover for each shard node. The failover operation takes effect only for the current shard node and does not affect other shard nodes of the same sharded cluster instance.
5. In the **Failover** message, click **OK**.

**Note**

The failover operation is complete in about one minute.

### View monitoring data

This topic describes the performance metrics provided by ApsaraDB for MongoDB to check the status of ApsaraDB for MongoDB instances. You can view instance monitoring data in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.

| Metric | Description |
|---|---|
| CPU utilization | cpu usage: the CPU utilization of the instance. _ |
| Memory usage | mem usage: the memory usage of the instance. _ |
| IOPS usage | The IOPS of the instance. The following items are included: data iops: the IOPS of the data disk. _ log iops: the IOPS of the disk that stores logs. _ |
| IOPS usage percentage | iops usage: the ratio of the IOPS used by the instance to the maximum _ IOPS allowed. |
| Disk usage | The total disk space used by the instance. The following items are included: ins size: the total space used. _ data size: the disk space used by data files. _ log size: the disk space used by log files. _ |
| Disk usage percentage | disk usage: the ratio of the total disk space used by the instance to the _ maximum disk space that can be used. |
| QPS | The queries per second (QPS) of the instance. The following items are included: The number of insert operations. The number of query operations. The number of delete operations. The number of update operations. The number of getMore operations. The number of command operations. |
| Connections | current conn: the number of current connections to the instance. _ |
| Cursors | The number of cursors used by the instance. The following items are included: total open: the number of cursors that are opened. _ timed out: the number of cursors that timed out. _ |
| Network traffic | The network traffic of the instance. The following items are included: bytes in: the inbound network traffic. _ bytes out: the outbound network traffic. _ num requests: the number of requests that are processed. _ |

t
4. In the left-side navigation pane, click **Monitoring Data**.
5. On the page that appears, specify a time range to view the monitoring data.
Instance monitoring data is collected every 300 seconds.

| Read/write queues | The length of the queues that are waiting for global locks for the instance. The following items are included: gl cq total: the length of the queue that is waiting for both global read _ _ and write locks. gl cq readers: the length of the queue that is waiting for global read _ _ locks. gl cq writers: the length of the queue that is waiting for global write _ _ locks. |
|---|---|
| WiredTiger | The cache metrics of the WiredTiger engine used by the instance. The following items are included: bytes read into cache: the amount of data that is read into the cache. _ _ _ bytes written from cache: the amount of data that is written from the _ _ _ cache to the disk. maximum bytes configured: the size of the maximum available disk _ _ space that is configured. |
| Primary/secondary replication latency | repl lag: the latency in data synchronization between the primary and _ secondary nodes of the instance. |

t

### Recycle bin

The recycle bin of ApsaraDB for MongoDB is used to retain released ApsaraDB for MongoDB instances. You can rebuild or destroy instances in the **recycle bin**. After an ApsaraDB for MongoDB instance is released, it is retained in the recycle bin for seven days before the instance is released from the recycle bin. After the instance is released from the recycle bin, the instance data cannot be restored. Proceed with caution.

**Rebuild an instance**

**Note**

Only **released** ApsaraDB for MongoDB instances can be **rebuilt**.
2. In the left-side navigation pane, click **Recycle Bin**.
3. Find the instance that you want to rebuild and click **Reconstruction Recovery** in the
**Operation** column.
4. On the **MongoDB Clone Instance** page, configure the **Availability Zone**, **Specification**
**Type**, **Node Specifications**, and **Storage space** parameters and the parameters in the
**Network**, and **Password Settings** sections.
5. Click **Submit**.

**Destroy an instance**

**Warning**

After an ApsaraDB for MongoDB instance is destroyed, the instance data is cleared and cannot be restored. t
2. In the left-side navigation pane, click **Recycle Bin**.
3. Find the instance that you want to destroy and click **Destroy immediately** in the
**Operation** column.
4. In the message that appears, click **OK**.

| Parameter name | Default value | Recomm ended value | Confirm restart? | Value range | Parameter description | Applicable versions and notes |
|---|---|---|---|---|---|---|

on

## Parameter configuration

### Set instance parameters

You can view and modify the values of certain parameters and query the parameter modification history in the ApsaraDB for MongoDB console. When you modify a parameter value, refer to the **Modifiable Parameter Values** column on the parameter list page. Some parameters require you to restart the instance after they are modified. For more information, see the **Restart Required** column on the **Parameter List** page in the console. Perform this operation during off-peak hours and ensure that your application has a reconnection mechanism.

**Modify parameter values**

1. Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the
target instance.
4. In the navigation pane on the left, choose **Parameter Settings > Parameter List**.
5. Click **Batch Modify**. On the **Modify Parameters** page, select the target parameter and
modify its value.
6. Click **OK**.

**View parameter modification history**

1. Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the
target instance.
4. In the navigation pane on the left, choose **Parameter Settings > Modification History**.
5. On the modification history page, select a time range and click **OK**.

**Parameter descriptions**

**Replica set parameter descriptions**

| auditLog.au thSuccess | true |  | true |  | A restart is not required. |  | true\|false |  |  |  | Specifies whether to audit successful authenticatio n operations for CRUD operations and commands. |  | 3.0+ (3.4, 3.6, 4.0, 4.2) |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auditLog.op Filter | admin,sl ow |  | admin,slo w |  | No restart is |  |  |  |  |  | An audit log filter option. You can specify the operation types to audit. It supports any combination of auth,admin |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | auth,admin |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ,slow,insert |  |  |  |
|  |  |  |  |  |  |  |  | .* |  |  |  |  | All 3.0+ |  |
|  |  |  |  |  |  |  |  |  |  |  | ,update,dele |  | versions |  |
|  |  |  |  |  | required. | quired. |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | te,command,q |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | uery,pbwm |  |  |  |
| auditLog.vip Only | true |  | true |  | A restart is not required. |  | true\|false |  |  |  | Specifies whether to audit only the CRUD operations and commands that are connected through a virtual IP address (VIP). |  | 3.0+ (3.4 to 4.2) |  |

|  | all |
|---|---|
| off |  |

on

| net.compre ssion.compr essors | snappy,z std,zlib | snappy,zst d,zlib | A restart is required. | snappy\|zlib\| zstd\|snappy ,zstd,zlib\|dis abled | Sets the network compression algorithm for mongod or mongos. |  | 5.0 to 7.0 Earlier versions (3.4 to 4.2) support only `snappy \| disabled` or `snappy \| zlib`. |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| net.listenBa cklog | 511 | 511 | A restart is required. | [511-1023] | The length of the TCP backlog queue. |  | 3.4 to 7.0 (Renamed from net.tcpBa cklog to net.liste nBacklog ) |  |  |  |
|  |  |  |  |  |  |  |  | net.tcpBa |  |  |
|  |  |  |  |  |  | log e. | cklog |  |  |  |
|  |  |  |  |  |  |  |  |  | to |  |
|  |  |  |  |  |  |  | nBacklog |  |  |  |
| net.serviceE xecutor | synchro nous | synchrono us | A restart is required. | synchronou s\|adaptive | Determines the threading and execution model used by mongod or mongos. |  | 4.0 to 4.2 (This parameter is not available in version 3.4.) |  |  |  |
| net.tls.mod e | disabled | disabled | A restart is required. | disabled\|all owTLS\|pref erTLS\|requir eTLS | The TLS mode for network connections. |  | 5.0 to 7.0 (Replaces net.ssl.m ode ) |  |  |  |
| net.ssl.mod e | disabled | disabled | Requires a restart | disabled\|all owSSL | SSL/TLS mode setting (old name). |  | 3.4 to 4.2 (Replaced by net.tls.m ode ) |  |  |  |

|  |  | net.ssl.m |  |
|---|---|---|---|
| ections. | ode |  |  |

|  |  | net.tls.m |  |
|---|---|---|---|
|  | ode |  |  |

on

| operationPr ofiling.mode | off | off | A restart is not required. | off\|slowOp\| all | The database performance profiling level: off : disabled. slowOp : records slow operations. all : records all operations. | All 3.0+ versions |
|---|---|---|---|---|---|---|
| operationPr ofiling.slow OpThreshol dMs | 100 | 100 | A restart is not required. | [0-65536] | The threshold in milliseconds for a query to be considered "slow" by the database. The default value is 100 ms. | All 3.0+ versions |
| replication.e nableMajorit yReadConc ern | true | true | You need to restart. | true\|false | Specifies whether to enable support for majority read concern. | 4.0 to 4.2 (Enabled by default and cannot be disabled in versions 5.0 and later.) |
| replication.o plogGlobalI d | false | A number, such as 4617 | You need to restart. | .* (any string or number) | The global ID (GID). The default value is the replSetName. This parameter is used for two- way synchronizati on scenarios. | 3.0+ (3.4 to 7.0) |
| replication.o plogGlobalI dEnabled | false | false | A restart is required. | true\|false | When enabled, GID is used to support two- way synchronizati on. | 3.0+ (3.4 to 7.0) |

on

| replication.o plogSizeMB | 1024 | Modifiable | No restart is required. | [1024- 107374182 4] | The maximum size of the oplog table in MB. | All 3.0+ versions |
|---|---|---|---|---|---|---|
| rsconf.write ConcernMaj orityJournal Default | true | true | No restart is required. | true\|false | Specifies whether to require that the journal is persisted when the write concern is `majority`. | 5.0 to 7.0 (Dynamic setting is not supported in 4.x versions.) |
| security.aut horization | enabled | enabled | A restart is required. | enabled\|dis abled | Specifies whether to enable role- based access control (RBAC). | All 3.0+ versions |
| security.jav ascriptEnabl ed | true | true | A restart is required. | true\|false | Specifies whether to allow the execution of JavaScript scripts, such as $where and `mapReduce` . | All 3.0+ versions |
| setParamet er.cursorTi meoutMillis | 600000 | 600000 | No restart is required. | [1- 214748364 7] | The timeout period for idle cursors in milliseconds. The default value is 10 minutes. Cursors that are idle for longer than this period are automatically purged by MongoDB. | All 3.0+ versions |

on

| setParamet er.enableFlo wControl | true | true | A restart is not required. |  |  | true\|false |  | Specifies whether to enable the flow control mechanism for replica sets. This prevents secondary nodes from lagging too far behind. |  | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| setParamet er.flowContr olTargetLag Seconds | 10 | 10 | No restart is required. |  |  | [1-600] |  | The target maximum majority commit lag in seconds when flow control is enabled. |  | 5.0 to 7.0 |  |  |
| setParamet er.internalQ ueryMaxBlo ckingSortMe moryUsage Bytes | 3355443 2 | 33554432 | A restart is not required. |  |  | [33554432- 268435456] |  | The maximum amount of memory in bytes that can be used |  | 5.0 to 7.0 (Equivalent to internalQ |  |  |
|  |  |  |  |  |  |  |  |  |  |  | internalQ |  |
|  |  |  |  |  |  |  |  |  | e used | ueryExecMa |  |  |
|  |  |  |  |  |  |  |  | for the sorting stage | e |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xBlockingS |  |  |
|  |  |  |  |  |  |  |  | of a query. |  | ortBytes |  |  |
|  |  |  |  |  |  |  |  | The default value is 32 MB. |  |  |  |  |
| setParamet er.internalQ ueryExecMa xBlockingSo rtBytes | 3355443 2 | 33554432 | A restart is not required. |  |  |  |  | The maximum amount of memory in bytes that |  | 3.4 to 4.2 (Renamed to internalQ |  |  |
|  |  |  |  |  |  |  |  |  |  |  | internalQ |  |
|  |  |  |  |  |  |  |  |  | that | ueryMaxBlo |  |  |
|  |  |  |  |  |  |  |  | can be used |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | ckingSortM |  |  |
|  |  |  |  |  |  |  |  | for the |  | emoryUsage |  |  |
|  |  |  |  | A restart |  |  |  | sorting stage |  |  |  |  |
|  |  |  |  |  |  |  |  | of a query. |  | Bytes |  |  |
|  |  |  |  |  |  | [33554432- 268435456] |  | The default value is 32 MB. |  |  |  |  |

on

| setParamet er.logicalSe ssionRefres hMillis | 300000 | 300000 | A restart is required. | [60000- 1800000] | The interval in milliseconds at which the logical session cache refreshes the primary session store. The default value is 5 minutes. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |
|---|---|---|---|---|---|---|
| setParamet er.maxInde xBuildMemo ryUsageMeg abytes | 200 | 200 | A restart is not required. | [50-200] | The maximum total memory in MB that can be consumed by all index creation processes on a single collection. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |
| setParamet er.maxNum ActiveUserI ndexBuilds | 3 | 3 | A restart is not required. | [1-5] | The maximum number of concurrent user-initiated index builds on the primary node. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |
| setParamet er.maxSessi ons | 1000000 | 1000000 | A restart is required. | [1000- 1000000] | The maximum number of sessions that can be cached. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |
| setParamet er.maxTran sactionLock RequestTim eoutMillis | 5 | 5 | A restart is not required. | [0-60] | The timeout in milliseconds for a transaction to acquire a lock. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |

on

| setParamet er.mirrorRe ads | { samplin gRate: 0.01, maxTim eMS: 5000 } | { samplingR ate: 0.01, maxTime MS: 5000 } | A restart is not required. | .* (object format) | Specifies whether to enable Mirrored Reads and sets the sample rate and maximum running time. | 5.0 to 7.0 |
|---|---|---|---|---|---|---|
| setParamet er.oplogFetc herUsesExh aust | true | true | A restart is required. | true\|false | Specifies whether to enable stream replication, which uses exhaust sockets to continuously pull the oplog. | 5.0 to 7.0 (Improves replication efficiency) |
| setParamet er.replWrite rThreadCou nt | 16 | 16 | A restart is required. | [1-256] | The number of write threads for applying the oplog in parallel. This affects replication throughput. | 5.0 to 7.0 |
| setParamet er.tcmalloc Aggressive MemoryDec ommit | 0 | 0 | No restart is required. | 0\|1 | Specifies whether to enable aggressive memory reclamation for tcmalloc, which releases unused memory back to the operating system. | 5.0 to 7.0 |
| setParamet er.tcmalloc ReleaseRat e | 1 | 1 | No restart is required. | [1-10] | Controls the rate at which tcmalloc releases memory to the operating system. A higher value indicates a faster rate. | 5.0 to 7.0 |

on

| setParamet er.transacti onLifetimeLi mitSeconds | 60 | 60 | A restart is not required. | [1-300] | The total lifecycle timeout for a transaction in seconds. This prevents transactions from being suspended for a long time. | 5.0 to 7.0 |
|---|---|---|---|---|---|---|
| setParamet er.vpcAuth Mode | false | false | A restart is not required. | true\|false | The switch for VPC authenticatio n mode. This is used in specific cloud environments . | 4.0 to 4.2 (Specific to earlier versions) |
| storage.oplo gMinRetenti onHours | 0 | 0 | A restart is not required. | [0.00- 720.00] | The minimum retention period for the oplog in hours. This ensures that delayed secondary nodes can still sync. | 5.0 to 7.0 (This parameter is not available in 4.x versions.) |
| storage.wire dTiger.colle ctionConfig. blockCompr essor | snappy | snappy | A restart is required. | snappy\|zlib\| zstd\|none | The block compression algorithm for the WiredTiger storage engine. This takes effect only for new collections. | 5.0 to 7.0 (4.x versions support `snappy`/`z lib`.) |
| systemLog.l ogRotateSiz eMB | 100 | 100 | No restart is required. | [1- 214748364 7] | The minimum size in MB for rotating system logs (`mongod.log `/`mongos.lo g`). | 3.4+ (3.0 to 4.2) |

on

| Parameter name | Default value |  | Recomme nded value |  | Restart |  | Value range | Parameter description and versions |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| auditLog.authS uccess | true |  | true |  | A restart is required. |  | true\|false | Specifies whether the audit log records successful authentication events. Versions: 3.4+ (4.0, 4.2, 5.0, 6.0, 7.0) |  |  |
| auditLog.opFilt er | admin,slow |  | admin,slow |  | No restart is |  | .* (such | Filters the operation types for the audit log. You can use any combination of auth,admin,slow, |  |  |
|  |  |  |  |  |  |  |  |  | auth,admin,slow, |  |
|  |  |  |  |  |  |  | as auth,admin,s | insert,update,dele |  |  |
|  |  |  |  |  | required. |  |  |  |  |  |
|  |  |  |  |  |  |  | low,... or | te,command,query,p |  |  |
|  |  |  |  |  |  |  | all/off) | bwm |  |  |
| auditLog.vipOn ly | true |  | true |  | A restart is required. |  | true\|false | Specifies whether to allow only virtual IP address (VIP) access to the audit log feature. Versions: 3.4+ (4.0, 4.2, 5.0, 6.0, 7.0) |  |  |
| net.compressi on.compressor s | snappy |  | snappy,zst d,zlib |  | A restart is required. |  | snappy\|zlib\|z std\|snappy,zs td,zlib\|disabl ed | Sets the network communication compression algorithm for mongod/mongos. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0). Versions 4.2 and earlier support only `snappy\|zlib\|disable d`. |  |  |
| net.listenBackl og | 511 |  | 511 |  | Restart required |  | [511-1023] | The length of the TCP connection queue (backlog). This is used for the size of the accept queue. Versions: 3.4+ (Universal) |  |  |

on

**Sharded cluster parameter descriptions**

| net.serviceExe cutor | synchrono us | adaptive (Recomme nded for high concurrenc y) | A restart is required. | synchronous\| adaptive | Specifies the threading model used by mongod/mongos: synchronous (synchronous), adaptive (adaptive, dynamic threads). Versions: 4.0+ (4.0, 4.2). Deprecated in versions 5.0 and later. |
|---|---|---|---|---|---|
| net.ssl.mode | disabled | requireSSL (Recomme nded for production) | You must restart. | disabled\|allo wSSL | The SSL connection mode. Allows or disables SSL only. Versions: 3.4+ (3.4, 4.0, 4.2). Replaced by TLS-related parameters starting from version 5.0. |
| net.tls.mode | disabled | requireTLS (Recomme nded for production) | A restart is required. | disabled\|allo wTLS\|preferT LS\|requireTL S | The TLS encrypted connection mode. Replaces SSL. requireTLS forces the use of TLS. Versions: 5.0+ (5.0, 6.0, 7.0) |
| security.forbid AdminDB | true | true | No restart is required. | true\|false | Specifies whether to prohibit users from writing to the admin database of a sharded cluster. This prevents accidental operations on the admin database. Versions: 3.4+ (Universal) |
| operationProfili ng.slowOpThre sholdMs | 100 | 100 to 500 (as needed) | A restart is not required. | [0-65536] | The threshold for slow queries in milliseconds. The profiler considers queries that exceed this time as slow queries. A value of 0 records all queries. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |

on

| setParameter. cursorTimeout Millis | 600000 | 300000 to 600000 | No restart is required. | [1- 2147483647] | The timeout period for idle cursors in milliseconds. MongoDB automatically purges idle cursors that time out. The default is 10 minutes. Versions: 3.4+ (Universal) |
|---|---|---|---|---|---|
| setParameter.l ogicalSessionR efreshMillis | 300000 | 300000 | A restart is required. | [60000- 1800000] | The refresh interval for the logical session cache in milliseconds. This controls the frequency of session cleanup. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter. maxSessions | 1000000 | 500000 to 1000000 | A restart is required. | [1000- 1000000] | The maximum number of cachable sessions (logical sessions). This affects memory usage. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.r eadHedgingMo de | on | on (Recomme nded for high availability) | A restart is not required. | on\|off | Specifies whether to enable Hedged Reads. When reading from a replica set, requests are sent to multiple nodes in parallel, and the fastest response is used. This improves read availability. Versions: 5.0+ (5.0, 6.0, 7.0) |
| setParameter. ShardingTaskE xecutorPoolHo stTimeoutMS | 300000 | 300000 | A restart is not required. | [60000- 3600000] | The timeout in milliseconds before mongos gives up on the connection pool for a shard host. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |

on

| setParameter. ShardingTaskE xecutorPoolMa xConnecting | 2 | 2 to 8 (depending on the network) | No restart is required. | [1-32] | The maximum number of concurrent connections during the initialization of a shard connection pool. This controls the speed of connection establishment. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
|---|---|---|---|---|---|
| setParameter. ShardingTaskE xecutorPoolMa xSize | 32767 | 1000 to 5000 (commonly used in practice) | A restart is not required. | [1-32767] | The maximum number of connections in each shard connection pool. This prevents resource exhaustion. Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter. ShardingTaskE xecutorPoolMi nSize | 1 | 1 to 10 | No restart is required. | [1-256] | The minimum number of connections in each shard connection pool (keepalive connections). Versions: 4.2+ (4.2, 5.0, 6.0, 7.0) |
| setParameter.t cmallocAggres siveMemoryDe commit | 0 | 0 (disabled by default) | A restart is not required. | [0-1] | Specifies whether to enable aggressive memory reclamation for tcmalloc, which releases unused memory to the OS. Enabling this may reduce memory usage but can affect performance. Versions: 5.0+ (5.0, 6.0, 7.0) |
| setParameter.t cmallocReleas eRate | 1 | 2 to 5 (balanced) | No restart is required. | [1-10] | The rate at which tcmalloc releases memory to the operating system. A higher value indicates a faster rate. A value that is too high may cause frequent allocation and release. Versions: 5.0+ (5.0, 6.0, 7.0) |

on

| setParameter. vpcAuthMode | false | false | A restart is not required. | true\|false | Specifies whether to enable VPC internal network authentication mode. This is used in specific cloud environments. Versions: 4.0+ (4.0, 4.2). Not mentioned in later versions. It may have been integrated into other features. |
|---|---|---|---|---|---|

| Parameter | Description |
|---|---|
| Template name | Enter a name for the parameter template. The name must meet the following requirements: The name must start with a letter, can contain digits and underscores ( ), and _ cannot contain Chinese characters. It must be 8 to 64 characters in length. |
| Organizati on | Select an organization. |
| Resource Set | Select a resource set. |
| Instance Type | Select the type of the destination instance. |
| Database engine | Set the value to MongoDB. |
| Database version | Select a database engine version. |

on

### Use parameter templates

When you configure multiple clusters that contain one or more parameters with the same settings, you can use parameter templates to manage and quickly apply parameters to clusters. This improves the efficiency of parameter management and cluster configuration.

**Create a parameter template**

1. Log in to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Parameter Template**. On the page that appears,
click **Create a parameter Template** and configure parameters. The following table describes the parameters.

| Descriptio n | Enter a description for the parameter template to facilitate management. The description can be 0 to 200 characters in length. |
|---|---|
| Add configurati on | After you click Add configuration, the system adds a parameter line to the list. You can specify Parameter Name and configure Configuration Value based on Description and Modifiable parameter values. You can also view the information about whether a cluster restart is required and the default parameter value on the page. Note To add another parameter, click Add configuration again. To delete a parameter, you can click Delete on the right of the parameter. |

on
3. Click **OK**.

**Apply a parameter template**

**Important**

If a restart is required, we recommend that you apply the parameter template during offpeak hours and make sure that your application is configured to automatically reconnect to the cluster.
1. Log in to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Parameter Template**. On the page that appears,
find the parameter template that you want to apply and click **Apply to an instance** in the
**Operation** column.
3. In the **Apply to an instance** panel, select the clusters to which you want to apply the
parameter template and click the icon to move them to the right list. You can view the differences between the parameter values in the template and the parameter values in the clusters in the **Parameter comparison** section.

**Note**

When you apply a parameter template to multiple clusters, take note of the following items: Check whether the parameters are applicable to these clusters. Proceed with caution. A parameter template can be applied to up to 10 clusters at a time. To apply a parameter template to more than 10 clusters, you can apply it in batches.
4. Click **OK**.

**Copy a parameter template**

1. Log in to the ApsaraDB for MongoDB console.

| Parameter | Description |
|---|---|
| Template name | The name of the parameter template. By default, the name is in the original template name clone format. You can rename the template. The name must _ meet the following requirements: The name must start with a letter, can contain digits and underscores ( ), and _ cannot contain Chinese characters. It must be 8 to 64 characters in length. |
| Description | Enter a description for the parameter template to facilitate management. The description can be 0 to 200 characters in length. |
| Add configuration | By default, the parameters are the same as those in the original template. You can modify the parameters based on your business requirements. Note To add a parameter, click Add configuration. To modify the value of a parameter, enter the value in the Configuration value field on the right of the parameter. To delete a parameter, you can click Delete on the right of the parameter. |

on
2. In the left-side navigation pane, click **Parameter Template**. On the page that appears,
find the parameter template that you want to copy and click **Clone** in the **Operation** column. In the Clone panel, configure the parameters. The following table describes the parameters. 3.
4. Click **OK**.

**Delete a parameter template**

1. Log in to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Parameter Template**. On the page that appears,
find the parameter template that you want to delete and click **Delete** in the **Operation** column.
3. Click **OK**.

| Parameter | Description |
|---|---|
| Retention Period (Days) | The retention period from 7 to 730 days. If the data volume is large, change the retention period from 30 days to 7 days. This way, storage space can be released promptly to efficiently reduce the storage usage and costs of Object Storage Service (OSS). |
| Backed Up At | The period of time during which you want to back up data. We recommend that you back up data during off-peak hours. |
| Day of Week | The days of a week on which you want to back up data. You can select multiple days. |

on

## Backup and restoration

### Data backup

#### Configure automatic backup

This topic describes how to configure automatic backup for an ApsaraDB for MongoDB instance. ApsaraDB for MongoDB can automatically back up data based on the default backup policy or the backup policy that you specify.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. In the upper-left corner of the page, click **Backup Settings**.
6. In the **Backup Settings** panel, configure the following parameters.
7. Click **OK**.

#### Manually back up an ApsaraDB for

**MongoDB instance**

This topic describes how to manually back up an ApsaraDB for MongoDB instance. ApsaraDB for MongoDB supports both automatic backup and manual backup. You can configure a backup policy for the system to automatically back up your ApsaraDB for MongoDB instance based on the backup cycle you specify.

**Backup methods**

Physical backup: This method backs up physical database files of an ApsaraDB for on MongoDB instance. Compared with logical backup, physical backup provides faster data backup and restoration. Logical backup: The mongodump tool is used to store operation records of databases in a logical backup file. Logical backup restores data in the form of playback commands during restoration.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the upper-right corner of the page, click **Back up Instance**.
5. In the **Back up Instance** panel, select a backup method from the **Backup Method** drop-
down list and then click **OK**.

### Download a backup file

ApsaraDB for MongoDB allows you to download backup files that can be used to restore databases. This topic describes how to download a backup file in the ApsaraDB for MongoDB console.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. On the page that appears, click
in the **Actions** column corresponding to a backup file and select **Download**.
6. In the **Download Backup** dialog box, click **Copy** next to the download URL and then click
**OK**.
7. Select an appropriate method to download the backup file based on your business
environment. You can run the **wget** command, or paste the copied download URL into the address bar of your browser and press the Enter key to download the backup file.

### Data restoration

on

#### Restore backup data to a new

**ApsaraDB for MongoDB instance by point in**

**time**

ApsaraDB for MongoDB allows you to create an instance at a point in time when the current instance is running and restore the backup data at that point in time to the new instance. This method is suitable for data restoration and verification.

**Limits**

Only points in time from the last seven days can be selected. Individual databases can be restored only from physical backups. If your instance runs a MongoDB version earlier than 4.0 and the total number of collections and indexes in your instance exceeds 10,000, physical backups may fail. The amount of time required to restore data of individual databases varies based on factors such as the data volume, task queue state, and network conditions. When the state of the new instance changes to **Running**, the restoration is complete.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the left-side navigation pane, click **Backup and Recovery**.
5. Select the databases that you want to restore.
i. On the **Backup and Recovery** page, click **Create Instance By Time Point**.

| Parameter | Description |
|---|---|
| Select recovery time point | Selects a point in time from which you want to restore data. Points in time from the last seven days can be selected. Note The point in time you select must be earlier than the current time and later than the time when the source instance was created. |
| Select databases to recover | All Databases: All databases in the source instance are restored. Select Databases: Only selected databases are restored. You can directly select the databases that you want to restore or click Enter Databases to enter the names of the databases that you want to restore. Note If you enter the names of the databases, separate the names with commas (,). By default, all databases are restored for sharded cluster instances. You can skip this step if the instance is a sharded cluster instance. If the instance is a sharded cluster instance, do not select the latest point in time (usually the latest hour). Otherwise, the restoration will fail. |

on ii. In the **Create Instance By Time Point** panel, specify the following parameters. iii. Click **OK**.
6. On the **Clone ApsaraDB for MongoDB instance** page, configure the parameters of the
new instance. For more information, see Create a replica set instance or Create a sharded cluster instance.

**Note**

If the instance is a replica set instance, the storage capacity of the new instance must be greater than or equal to that of the source instance. If the instance is a sharded cluster instance, the following requirements must be met: The number of shard nodes in the new instance must be equal to that in the source instance. The storage capacity of each shard node in the new instance must be greater than or equal to that in the source instance.
7. Click **Submit**.

#### Restore backup data to a new

**ApsaraDB for MongoDB instance by backup**

**point**

on ApsaraDB for MongoDB allows you to restore data to a new ApsaraDB for MongoDB instance by backup point. This method is suitable for data restoration and verification.

**Prerequisites**

The instance is a replica set instance.

**Limits**

Only backup points from the last seven days can be selected.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set Instances** page, click the ID of an instance, or click
in the **Actions** column corresponding to the instance and select **Manage**.
4. In the left-side navigation pane, click **Backup and Recovery**.
5. Select the databases that you want to restore.
i. Find the backup file that you want to use for data restoration. Choose
> **Create**
**Instance from Backup Point** in the **Actions** column.
ii. In the **Create Instance from Backup Point** panel, select the databases that you want to restore.
**All Databases**: All databases in the source instance are restored.
**Select Databases**: Only selected databases are restored.
You can directly select the databases that you want to restore or click **Enter**
**Databases** to enter the names of the databases that you want to restore.

**Note**

If you enter the names of the databases, separate the names with commas (,). iii. Click **OK**.
6. On the **Clone ApsaraDB for MongoDB instance** page, configure the parameters of the
new instance. For more information, see Create a replica set instance or Create a sharded cluster instance.

**Note**

The storage capacity of the new instance must be greater than or equal to that of the source instance.
7. Click **Submit**.

#### Restore data to the current ApsaraDB

**for MongoDB instance**

Data restoration minimizes the data loss caused by accidental changes. This topic describes how to restore data to the current ApsaraDB for MongoDB instance.

**Prerequisites**

on The instance is a replica set instance with three nodes.

**Background information**

The time required to restore database data varies based on factors such as the data volume, task queue status, and network conditions. When the state of the instance changes to **Running**, the restoration is complete. If you restore data to your current instance, all existing data is overwritten and cannot be restored. Proceed with caution.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set Instances** page, click the ID of an instance, or click
in the **Actions** column corresponding to the instance and select **Manage**.
3. In the left-side navigation pane, click **Backup and Recovery**.
4. On the **Backup and Recovery** page, find the backup set that you want to manage and
click the icon. Then, select Data Rollback.

**Note**

If the MongoDB version has been upgraded, the backup files of the original instance that runs an earlier version cannot be used to restore data to the new instance.
5. In the **Data Restoration** message, click **OK**.

**Note**

The instance state becomes **Restoring from Backup** after you click **OK**. You can click **Refresh** in the upper-right corner of the **Backup and Recovery** page to update the instance state. The restoration is complete when the instance state changes to **Running**.

| Task | Procedure |
|---|---|
| View alert history | In the Alert History list, view the Product Name, Affected Instance, Time, Rule Name, Status, Level, and Notification Recipient. Click the rule name to view the details of the alert rule. Note By default, you can query alert history data from the last 2 days. |

## Cloud Monitor

### View performance metrics

PolarDB for MySQL V2.0 provides rich performance metrics and second-level monitoring frequency, which allow you to easily track the status of clusters and address operational challenges.

**View the dashboard**

1. Log in to the PolarDB for MySQL V2.0 console.
2. On the **Instances Using Local Disks** page, find the cluster that you want to manage and
click its ID.
3. In the left-side navigation pane, click **CloudMonitor**.
4. You can view metrics related to **computing resources**, **disks**, **networks**, **deadlocks**,
and **read-only instances**. View performance metrics

**View monitoring information**

1. Log in to the PolarDB for MySQL V2.0 console.
2. In the left-side navigation pane, click **CloudMonitor**.
3. In the **time granularity** drop-down list, select **1 Minute** or **1 Hour** (default value) as the
data collection interval.

### Alert history

After an alert is triggered, you can view its history. You can also export and download the alert history for local data analytics.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **Cloud Monitor** and choose **Alert Service** > **Alert**
**History**.
4. (Optional) On the **Alert History** page, filter the alert history by **Rule ID**, **Rule Name**, **Alert**
**Level**, and time.
5. On the Alert History page, you can perform the following tasks.

| Export alert history | i. On the Alert History page, click in the upper-right corner. ii. In the Export Task dialog box, set Time Range and Task Name. Then, click OK. |
|---|---|

| Parameter | Description |
|---|---|
| Cloud Service Selection | This is set by default and does not need to be selected. |
| Resource Scope | The scope of resources associated with the alert rule. The following types are supported. The available scope types may vary by cloud service. Instance: Select one or more target instances from the resource set of the current organization. Resource Set: Select a target resource set in the current organization and region. Application Group: Select an application group in the current organization and region. All Resources: This option is not supported by default. |

### Alert rules

#### Create an alert rule

Create an alert rule that triggers alerts for a cloud service based on specified metric thresholds and promptly notifies relevant users.

**Background information**

During its effective period, an alert rule checks at a default detection frequency if a metric exceeds the specified threshold. If a metric exceeds the threshold and becomes abnormal, an alert is sent to the specified alert contacts or other alert processing platforms.

**Note**

The minimum alert detection frequency is once per minute.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **CloudMonitor**, and then choose **Alert Service** >
**Alert Rules**.
4. Above the list, click **Create Alert Rule**.
5. In the **Create Alert Rule** panel, set the parameters as needed.

| Resource Selection | Based on the selected Resource Scope, select a specific resource instance, resource set, or application group. |
|---|---|
| Alert Rule Description | The main body of the alert rule. The rule is triggered when monitoring data meets the alert conditions. To set the rule description: i. Click Create Alert Rule. ii. In the Create Alert Rule panel, set the Rule Name, Metric Dimension, Monitoring Metric, Threshold, AndAlert Level. Note The Metric Dimension parameter is displayed only when Resource Scope is set to Instance. iii. Click Confirm. |
| Mute For | The interval at which to resend an alert notification if the alert is not resolved. Valid values: 5 Minutes, 15 Minutes, 30 Minutes, 1 Hour, 3 Hours, 6 Hours, 12 Hours, and 24 Hours. When a metric exceeds the alert threshold, an alert is triggered. If the metric continues to exceed the threshold during the mute period, no more alert notifications are sent. If the metric has not recovered after the mute period, CloudMonitor sends another alert notification. For example, if Mute For is set to 12 Hours, CloudMonitor sends another alert notification if the metric that exceeded the threshold has not recovered 12 hours after the first alert was triggered. |
| Effective Period | The period during which the alert rule is active. The rule only checks if monitoring data exceeds the alert threshold during this period. |
| Alert Callback | A webhook address that receives alert messages pushed by CloudMonitor through POST requests. Note The webhook address must be a domain name accessible to CloudMonitor. Only the HTTP protocol is supported. You cannot enter an IP address. |
| No Data Handling Method | The method for handling alerts when there is no monitoring data. Do Nothing Send No-data Alert |
| Alert Contact | Select the user group or user to whom alert messages are sent. The default alert contact group for an Alibaba Cloud account is an empty group. You can use it to test the validity of an alert rule. |

6. Click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the alert rule. |
| Monitoring Metric | From all the metrics available for the selected cloud service, select the target metric. For more information about the metrics for each cloud service, see the relevant monitoring documentation. |
| Metric Dimension | Refers to dimensions other than the instance ID. This parameter is displayed only when Resource Scope is set to Instance. |
| Threshold And Alert Level (unit: %) | The alert levels are Critical, Warning, and Info. The aggregation method for monitoring data can be Average, Minimum, or Maximum. You can set the monitoring data epoch to 1 Consecutive Epoch, 5 Consecutive Epochs, 10 Consecutive Epochs, 15 Consecutive Epochs, 30 Consecutive Epochs, or 60 Consecutive Epochs. The comparison operator between the actual monitoring data and the alert threshold. Supported operators include “>”, “ >=”, “<”, “<= ”, “=”, “!=”, “Day-on-day Increase”, “Day-on-day Decrease”, “Period-on-period Increase”, “period-on-period Decrease”, “increase From Last Period”, and “decrease From Last Period”. You can also set a threshold and the number of times it must be met to trigger an alert. |

**Rule description parameters**

**Example configuration**

This example creates an alert rule named "example" for an Elastic Compute Service (ECS) instance to monitor its CPU utilization. The rule triggers a Critical alert if the maximum CPU utilization is greater than or equal to 70% for three occurrences within five detection periods. The following figure shows the rule description configuration for this scenario.

| Task | Procedure |
|---|---|
| View alert rule details | In the Operation column of the target alert rule, click Details to view the rule details on the Alert Rule/Alert History/Faulty Resources panel. |

#### Manage alert rules

From the list of alert rules, you can modify, enable, disable, and delete rules.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **Cloud Monitor** and then choose **Alert Service**>
**Alert Rules**.
4. Find the desired alert rule and perform the required operation.

| Check rule validity | In the Validity column of the target alert rule, click Click To Inspect. The inspection result is displayed in the Validity column. Note If the inspection result is abnormal, click Detection Result. In the panel that appears, view the results for Alert Rule Execution Anomaly Detection, Alert Rule Load Detection, Invalid Alert Rule Detection, and Alert Rule Callback Detection. Click Re-detect to check the rule validity again. |
|---|---|
| View rule execution records | In the Rule Execution Record column of the target alert rule, click View Rule Execution Record. On the Alert Rule Execution Record panel, filter the execution records by time range. |
| Modify an alert rule | i. In the Operation column of the target alert rule, click Edit. ii. On the Modify Alert Rule panel, modify the alert rule. For more information about the configuration parameters, see Create an alert rule. iii. After you finish the modification, click OK. |
| Disable an alert rule | Disable alert rules when you manually stop a cloud product for maintenance or an upgrade. This prevents unnecessary alert notifications. Note Before disabling an alert rule, make sure that its Status is Normal. Disable a single rule a. In the Operation column of the target alert rule, click the icon, and then click Disable. b. In the Disable Alert Rule dialog box, click OK. Disable rules in a batch a. Select the check boxes next to the target alert rules, and then click Disable in the lower-left corner of the list. b. In the Disable Alert Rule dialog box, click OK. |

| Enable an alert rule | After you finish the maintenance or upgrade of a cloud product, re-enable the disabled alert rules. Note Before enabling an alert rule, make sure that its Status is Disabled. Enable a single rule a. In the Operation column of the target alert rule, click Enable. b. In the Enable Alert Rule dialog box, click OK. Enable rules in a batch a. Select the check boxes next to the target alert rules, and then click Enable in the lower-left corner of the list. b. In the Enable Alert Rule dialog box, click OK. |
|---|---|
| Delete an alert rule | Delete a single rule a. In the Operation column of the target alert rule, click the icon, and then click Delete. b. In the Delete Alert Rule dialog box, click OK. Delete rules in a batch a. Select the check boxes next to the target alert rules, and then click Delete in the lower-left corner of the list. b. In the Delete Alert Rule dialog box, click OK. |

| Architecture | Limits |
|---|---|
| Replica set instance | You can modify only the public and internal endpoints of primary and secondary nodes. |
| Sharded cluster instance | You can modify only the public and internal endpoints of mongos nodes. |

s

## Database connections

### Modify a public or internal

**endpoint of an ApsaraDB for**

**MongoDB instance**

This topic describes how to modify a public or internal endpoint of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console.

**Limits**

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of the
instance whose endpoint you want to modify.
4. In the left-side navigation pane, click **Database Connection**.
5. In the **Internal Connections** or **Public Connections** section, click **Update Connection**
**String**.
6. In the **Update Connection String** panel, specify a new endpoint.

**Note**

Only the prefix of the endpoint can be modified. You must comply with the following rules when you modify the prefix: The prefix must start with a lowercase letter. The prefix must start or end with a lowercase letter or digit. The prefix must be 8 to 64 characters in length and can contain lowercase letters, digits, and hyphens (-).
7. Click **OK**.

**What to do next**

After you modify the public or internal endpoint, you must connect a client or an application to your ApsaraDB for MongoDB instance by using the new endpoint.

| Parameter | Description |
|---|---|
| Database Type | The database engine of the instance. By default, this parameter is set to the database engine of the instance that you want to access. |
| Instance Region | The region where the instance is deployed. By default, this parameter is set to the region where the current instance is deployed. |
| Connection string address | The connection string of the instance. By default, this parameter is set to the connection string of the current instance. |
| Database Name | The name of the database. By default, this parameter is set to admin. |
| Database Account | The account used to connect to the database. By default, this parameter is set to root. |
| Database Password | The password of the account used to connect to the database. |

s

### Use DMS to log on to an

**ApsaraDB for MongoDB instance**

You can use Data Management (DMS) to log on to an ApsaraDB for MongoDB instance.

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure a whitelist.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the upper-right corner of the page, click **Log On**.

**Note**

For a sharded cluster instance, you must also select a mongos node. Log on to the **DMS** console.
5. In the **Login instance** dialog box, configure the parameters described in the following
table.
6. Click **Login**.

**Note**

You can select **Remember password** to eliminate the need to manually enter the password again the next time you log on to the database. s

### Use the mongo shell to

**connect to an ApsaraDB for**

**MongoDB instance**

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by ApsaraDB for MongoDB. You can install it on your client or in an Elastic Compute Service (ECS) instance.

**Prerequisites**

The version of the mongo shell is the same as that of your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about the installation procedure, see Install MongoDB.

**Note**

You can select a MongoDB version corresponding to your client version in the upper-left corner of the page. The IP address of your client is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, click **Database Connections** to view connection strings.

**Note**

Replica set instances: View the connection string or connection string URI of a node. Sharded cluster instances: View the connection string or connection string URI of a mongos node. For more information about connection strings, see Overview of replica set instance connections or Overview of sharded cluster instance connections.
5. Connect to a database of the instance from your client or ECS instance where the mongo
shell is installed. Replica set instances s High-availability connection (recommended) You can use a connection string URI to connect to both the primary and secondary nodes of the instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched. Command syntax:

```
mongo "<ConnectionStringURI>"
```

**Note**

The connection string URI must be enclosed in a pair of double quotation marks (""). <ConnectionStringURI>: the **connection string URI** of the instance. You must replace `****` in the **connection string URI** with the database password. For more information about how to set a database password, see Reset a password. Example:

```
mongo "mongodb://root:****@dds-
**********.mongodb.rds.intra.env17e.shuguang.com:3717,dds-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
```

`*"` s Single-node connection In most cases, you can directly connect to the primary, secondary, or read-only node. When the primary node fails, the system automatically switches to the secondary node and the secondary node becomes the primary node. This affects the read and write operations of your application. Command syntax:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database>
```

**Note**

<host>: the endpoint used to log on to the primary or secondary node. <username>: the username used to log on to a database of the instance. The initial username is **root**. <database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin as the database name. Example:

```
mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenti cationDatabase admin
```

When `Enter password:` is displayed, enter the password of the username and press the Enter key. If you forget the password of the root username, you can reset the password. For more information, see Reset a password.

**Note**

The password characters are not displayed when you enter the password. Sharded cluster instances s High-availability connection (recommended) You can use a connection string URI to connect to a database of the instance. If one mongos node fails, another mongos node takes over business to ensure the high availability of the connection. Command syntax:

```
mongo "<ConnectionStringURI>"
```

**Note**

The connection string URI must be enclosed in a pair of double quotation marks (""). <ConnectionStringURI>: the **connection string URI** of the instance. You must replace `****` in the **connection string URI** with the database password. For more information about how to set a database password, see Reset a password. Example:

```
mongo "mongodb://root:****@s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
```

Mongos node connection Command syntax:

```
mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
```

**Note**

<mongos_host>: the endpoint used to log on to a mongos node. <username>: the username used to log on to a database of the instance. The initial username is **root**. <database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin as the database name. Example:

```
mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authentica tionDatabase admin
```

### Apply for a public endpoint

This topic describes how to apply for a public endpoint for an ApsaraDB for MongoDB instance when you want to connect to the instance over the Internet.

**Background information**

ApsaraDB for MongoDB instances support Virtual Private Cloud (VPC), classic network, and public endpoints. The following table describes these endpoints.

| Endpoint | Description |
|---|---|
| VPC endpoint | A VPC is an isolated network that provides higher security and performance than the classic network. By default, an ApsaraDB for MongoDB comes with a VPC endpoint. You can connect to the VPC endpoint for higher security and performance. |
| Classic network endpoint | Cloud services deployed in the classic network are not isolated from each other. Unauthorized access can be blocked only by using security groups or whitelists. |
| Public endpoint | Your ApsaraDB for MongoDB instance is at risk when you connect to it over the Internet. For this reason, ApsaraDB for MongoDB does not provide public endpoints by default. If you want to connect to an ApsaraDB for MongoDB instance from a device outside Alibaba Cloud, such as an on-premise device, you must apply for a public endpoint. |

s

**Apply for a public endpoint for a replica set instance**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set instance List** page, find the instance that you want to manage and
click the ID of the instance.
3. In the left-side navigation pane, click **Database Connections**.
4. In the **Public Connections** section, apply for an IPv4 address or apply for an IPv4 address
and an IPv6 address.
5. In the message that appears, click **OK**.

**Note**

Apply for an IPv4 address: This option is suitable for IPv4 networks. Apply for an IPv4 address and an IPv6 address: This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you want to connect to a replica set instance by using a public endpoint, you must add the public IP address of your client to the whitelist of the instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. s After you submit the application, the replica set instance generates public endpoints for both the primary and secondary nodes and a connection string URI for establishing highavailability connections. For more information, see Overview of replica set instance connections.

**Apply for a public endpoint for a sharded cluster instance**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **List of sharded cluster instances** page, click the ID of the instance that you want
to manage.
4. In the left-side navigation pane, click **Database Connections**.
5. In the **Public Connections** section, click **Apply for Public Connection String**.
6. In the **Apply for Public Connection String** pane, specify **Node Type**, **Node ID**, and
**Apply for IP type** and click **OK**.
7. **Optional:** If you want to apply for multiple public endpoints for the nodes in the sharded
cluster instance, repeat the preceding steps.

**Note**

To apply for public endpoints for multiple nodes in the instance consecutively, you must wait until the state of the instance changes to **Running**.

**References**

To ensure data security, we recommend that you release public endpoints if you no longer need them. For more information, see Release a public endpoint. Before you connect to a database over the Internet, we recommend that you enable SSL encryption. For more information, see Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode.

### Release a public endpoint

To ensure data security, you can release public endpoints that are no longer needed in the ApsaraDB for MongoDB console. You can release one or more public endpoints of the mongos nodes for a sharded cluster instance. After a public endpoint is released for an instance or node, you cannot connect to the instance or node by using the public endpoint. After the public endpoint is released, we recommend that you delete the corresponding public IP address from the whitelist to ensure data security. For more information, see s Configure a whitelist.

**Release a public endpoint for a replica set instance**

**Note**

After the public endpoint of a replica set instance is released, the public endpoints of the primary and secondary nodes are released.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set Instances** page, click the ID of an instance.
3. In the left-side navigation pane, click **Database Connections**.
4. In the **Public Connections** section, click **Release Public Connection String**.
5. In the **Release Public Connection String** message, click **OK**.

**Release a public endpoint for a sharded cluster instance**

**Note**

You can release one or more public endpoints of the mongos, shard, and Configserver nodes for a sharded cluster instance. After the public endpoint of a shard or Configserver node is released, the public endpoints of the primary and secondary nodes are released.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of an instance.
4. In the left-side navigation pane, click **Database Connections**.
5. In the **Public Connections** section, find the mongos node for which you want to release
the public endpoint.
6. Click **Release** in the **Actions** column.

**Note**

You can repeat this step to release the public endpoints of other nodes as needed. To release the public endpoint of another node in the instance, you must wait until the public endpoint of the current node is released or the state of the current instance becomes **Running**.
7. In the **Release Public Connection String** message, click **OK**.
8. **Optional:**You can repeat this step to release the public endpoints of multiple nodes in a
sharded cluster instance.

| Parameter | Description |
|---|---|
| Node Type | Shard: shard node CS: ConfigServer node |

s

**Note**

To release the public endpoint of another node in the instance, you must wait until the state of the instance becomes **Running**.

### Apply for an endpoint for a

**shard or ConfigServer node**

A sharded cluster instance consists of mongos, shard, and Configserver nodes. Typically, you need only to connect to a mongos node to read and write data. If you want to read oplog data from a shard node or read configuration information from a Configserver node when you perform specific operations such as data synchronization between clusters, you must apply for an endpoint for the corresponding node first.

**Prerequisites**

A sharded cluster instance is created.

**Usage notes**

After you submit an application, two endpoints are allocated to each node, one for the primary node and the other for the secondary node. The network type of an endpoint for which you want to apply must be the same as that of the current mongos node. You cannot modify the endpoint that is allocated to a shard or ConfigServer node. The endpoint allocated can only be used to access the node over the internal network. If you want to access the node over the Internet, you can apply for a public endpoint. For more information, see Apply for a public endpoint.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the left-side navigation pane, click **Database Connections**.
5. Click **Apply for Shard\Configserver Endpoint**.
6. In the dialog box that appears, apply for an endpoint for the shard or Configserver node.

| Apply for IP type | IPv4: Apply for an IPv4 address. This option is suitable for IPv4 networks. IPv4v6: Apply for an IPv4 address and an IPv6 address. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. |
|---|---|
| Select Node ID | Select a check box corresponding to the ID of the node for which you want to apply for an endpoint. |
| Account Name | The account name must be 4 to 16 characters in length, and can contain lowercase letters, digits, and underscores ( ). It must start with a lowercase _ letter. Note You must set the account and password only when you apply for an endpoint for a shard or Configserver node for the first time. The account and password are required for all shard and Configserver nodes. The account has only permissions to read data. |
| Account Password | The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. The following special characters are supported: !@#$%^&*() += _ The password must be 8 to 32 characters in length. Note If you forget your password, you can reset the password. For more information, see Reset the password. |
| Confirm Password | Enter the account password again. |

| Node type | Description |
|---|---|

s
7. Click **OK**.
8. Wait until the instance state changes from **Creating Connection** to **Running**.

**Node types**

After you **apply for an endpoint for a shard or Configserver node**, you can view the endpoint on the **Database Connections** page. The following table describes node types.

| DB | A shard node. |
|---|---|
| CS | A ConfigServer node. |
| Mongos | A mongos node. |

s

**References**

If you no longer need the endpoints of shard or ConfigServer nodes, you can release the endpoints. For more information about how to release an endpoint, see Release the connection string of a shard or Configserver node.

### Release the connection string

**of a shard or Configserver node**

When you no longer need to connect to a shard or Configserver node, you can release its connection string. This operation applies to sharded cluster instances only. The connection string of a mongos node cannot be released. After the connection string of a shard or Configserver node is released, the connection strings of the primary and secondary nodes are released and you cannot use this connection string to connect to the released node. Proceed with caution. This operation releases the internal connection string of the node. If the node also has a public connection string and the connection string is no longer needed, you can Release a public endpoint.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the left-side navigation pane, click **Database Connection**.
5. Find the node and click **Release** in the **Actions** column.

**Note**

**db** indicates a shard node. **cs** indicates a Configserver node.
6. In the dialog box that appears, click **OK**.
7. Wait until the instance status changes from **Releasing Network Connection** to **Running**.

| Item | Description |
|---|---|
| Connection address type | Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Apsara Stack services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists. VPC endpoint: Virtual private cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and higher performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance. |
| Role | Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance. Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance. Connection String URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and high availability. |

s

### Overview of replica set

**instance connections**

ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node, and use a connection string URI to connect to both of them. For high availability, we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections.

**Prerequisites**

A whitelist is configured for the replica set instance. For more information, see Configure a whitelist.

**View connection strings**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set Instances** page, click the ID of an instance.
4. In the left-side navigation pane, click **Database Connections** to view connection strings.

**Description of connection strings**

| Connection string | The connection string of a primary or secondary node is in the following format: <host>:<port> <host>: the endpoint used to connect to the replica set instance. <port>: the port number used to connect to the replica set instance. |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of the connection string URI. username:password@: the username and password used to log on to the replica set instance. You must separate them with a colon (:). hostX:portX: the endpoint and port number used to connect to the replica set instance. /database: the name of the database corresponding to the username if authentication is enabled. ?options: the additional options that are used to connect to the replica set instance. Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. This way, when a node fails, the read and write operations of your application are not affected as a result of the failover. |

s

**Related topics**

#### Use the mongo shell to connect to an ApsaraDB for MongoDB instance

### Overview of sharded cluster

**instance connections**

ApsaraDB for MongoDB sharded cluster instances support both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node and use a connection string URI to connect to multiple mongos nodes. For high availability (HA), we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections.

**View connection strings**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click the ID of the instance whose connection
strings you want to view.
4. In the left-side navigation pane, click **Database Connections** to view connection strings.

| Item | Description |
|---|---|
| Connection address type | Classic network endpoint: Classic network endpoints are used for communication over the classic network. In the classic network, Alibaba Cloud services are not isolated. To block unauthorized traffic, you must configure security groups or IP address whitelists. VPC endpoint: Virtual Private Cloud (VPC) endpoints are used for communication over VPCs. A VPC is an isolated network that provides higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints for ApsaraDB for MongoDB instances to ensure high security and high performance. Public endpoint: Public endpoints are used for communication over the Internet. If you connect to an ApsaraDB for MongoDB instance over the Internet, the instance may be exposed to security risks. By default, ApsaraDB for MongoDB does not provide public endpoints for ApsaraDB for MongoDB instances. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Apsara Stack (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint. |
| Mongos node ID | The connection string of a mongos node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port number used to connect to the instance. Note During routine tests, you can use a connection string to directly connect to a mongos node. |

s

**Description of connection strings**

| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to the instance. You must separate them with a colon (:). hostX:portX: the endpoint and port number used to connect to the instance. /database: the name of the database corresponding to the username if authentication is enabled. options: the additional options that are used to connect to the instance. Note If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads. If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |
|---|---|

s

## Data security

### Configure a whitelist for an

**ApsaraDB for MongoDB instance**

This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or CIDR blocks that you use for database access to a whitelist of this instance. This improves database security and stability. Proper configuration of whitelists can enhance access security of ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis.

**Background information**

The system creates a default whitelist for each instance. This whitelist can be modified or cleared but cannot be deleted. After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the **default** whitelist of this instance. The IP address 127.0.0.1 indicates that no IP addresses are allowed to access this instance.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
5. On the page that appears, use one of the following methods to add IP addresses to a
whitelist: Manually modify a whitelist a. Click in the **Actions** column corresponding to a whitelist and select **Manually**
**Modify**.
b. In the Manually Modify panel, enter IP addresses or CIDR blocks in the **IP White List** field.

**Note**

Separate multiple IP addresses with commas (,). A maximum of 1,000 different IP addresses can be added. Supported formats are 0.0.0.0/0, IP addresses such as 10.23.12.24, or CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits. If the IP address whitelist is empty or contains only `0.0.0.0/0` , all devices are granted access. This poses risks to your ApsaraDB for MongoDB instance. We recommend that you add only the IP addresses or CIDR blocks of your own web servers to the whitelist. c. Click **OK**. Load internal IP addresses of ECS instances

| Parameter | Description |
|---|---|
| Group Name | You can customize the group name based on the following rules. Start with a lowercase letter. End with a letter or a digit. Contain only lowercase letters, digits, and underscores ( ). _ Be 2 to 32 characters in length. |

a. Click in the **Actions** column corresponding to a whitelist and select **Import ECS**
**Intranet IP**.
b. In the **Import ECS Intranet IP** panel, select the IP addresses that you want to add to the IP address whitelist and click to add these IP addresses to the whitelist. c. Click **OK**.

### Create or delete a whitelist

This topic describes how to create or delete a whitelist. Whitelists consist of the IP addresses allowed to access specific databases.

**Background information**

If your business involves multiple applications and you need to create a whitelist for each of them, you can sort the IP addresses of the applications into different whitelists.

**Create a whitelist**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the navigation pane on the left, choose **Data Security > Whitelist Settings**.
5. Click **Create Whitelist**.
6. In the **Create Whitelist** panel, specify **Group Name** and **IP Whitelist** and click **OK**.

| IP Whitelist | Enter the IP addresses or CIDR blocks to add. Both IPv4 and IPv6 whitelists are supported. Note Separate multiple IP addresses with a comma (,). You can add up to 1,000 unique IP addresses. A whitelist can include IP addresses such as 0.0.0.0/0 and 10.23.12.24 or CIDR blocks such as 10.23.12.24/24. /24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32. Setting the whitelist to 0.0.0.0/0 removes all IP address restrictions. This creates a high security risk for your database. We recommend that you grant access only to the public IP addresses or CIDR blocks of your web servers. You can import and export IP lists in text format. |
|---|---|

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the navigation pane on the left, choose **Data Security > Whitelist Settings**.
5. For the target whitelist group, click **Delete Whitelist Group** in the **Actions** column.

**Note**

You cannot delete the **default** group.
6. In the **Delete Whitelist Group** message, click **OK**.

### Enable the audit log feature

You can view the statement execution logs, operational logs, and error logs of an instance in the ApsaraDB for MongoDB console. This helps you locate and analyze faults.

**Usage notes**

Audit logs are retained for seven days. Expired logs are deleted. If you disable the audit log feature for an instance, saved logs are deleted. If you enable the audit log feature for an instance for the first time, the **admin** and **slow** operation types are selected by default. If you disable the audit log feature for an operation type, the system stops collecting logs related to this operation type. However, the collected logs are still retained.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.

| Instance type | Audit type | Operation type |
|---|---|---|
| Replica set instance | db | admin: O&M operations slow: slow queries query:: queries insert: insert operations update: update operations delete: delete operations command: all commands |
| Sharded cluster instance | db | admin: O&M operations slow: slow queries query:: queries insert: insert operations update: update operations delete: delete operations command: all commands |

2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set instance List** or **List of sharded cluster instances** page, click the
ID of the instance that you want to manage.
4. In the left-side navigation pane, choose **Data Security > Audit Logs**.
5. In the upper-left corner of the page, click **Enable Audit Log**.
6. In the **Enable Audit Log** message, click **OK**.
After the audit log feature is enabled, you can query audit logs by **time range**, **keyword**, and **database name**. In addition, you can perform the following operations:

**Sort SQL statements in descending order of duration (recommended)**

Feature description: The system intelligently aggregates and sorts SQL statements that occupy the most resources in descending order of duration. Benefits: This feature helps O&M engineers quickly locate slow SQL statements, optimize indexes, and fine-tune SQL statements. It ensures the stability of your system in high-concurrency scenarios. How to perform: On the Audit Logs page, select the **Sort by Top SQL time-**
**consuming** check box and click Search to view the SQL statements.
**Create an export task**: You can export audit log files.
**View the list of exported files**: You can view audit log files in a list.
**Disable audit logs**: After you disable this feature, the system stops collecting database
operation information and deletes all saved audit logs.
**Audit log filter setting**: You can modify the types of operations to be audited. The
following table describes the operation types available in different architectures.

|  | mongos | admin: O&M operations slow: slow queries insert: insert operations update: update operations delete: delete operations |
|---|---|---|

### Configure SSL encryption

This topic describes how to enable Secure Sockets Layer (SSL) encryption for an instance to enhance connection security. After you enable SSL encryption, you must install SSL certificates that are issued by certificate authorities (CAs) on your application. SSL encryption can encrypt connections at the transport layer to improve data security and ensure data integrity. This topic describes the operations related to SSL encryption.

**Prerequisites**

A replica set instance is created.

**Impacts**

When you enable or disable SSL encryption or renew SSL certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your applications can automatically reconnect to the instance.

**Note**

When an instance is restarted, all its nodes are restarted in turn and each node experiences a temporary disconnection of approximately 30 seconds. If the instance houses more than 10,000 collections, the temporary disconnection lasts even longer.

**Usage notes**

You can download SSL certificate files only from the ApsaraDB for MongoDB console. After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary. For example, you can enable SSL encryption when you connect to an ApsaraDB for MongoDB instance over the Internet.

**Note**

In most cases, connections that are established to the internal endpoint of your instance are secure and do not require SSL encryption. After you enable SSL encryption for an instance, both SSL and non-SSL connections are supported.

**Method 1**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set instance List** page, find the instance that you want to manage and
click the ID of the instance.

| Operation | Prerequisites | Procedure |
|---|---|---|
| Enable SSL encryption | SSL encryption is in the Disabled state. | i. Turn on SSL Status. ii. In the Restart Instance message, click OK. |
| Renew an SSL certificate | SSL encryption is in the Enabled state. | i. Click Update Certificate. ii. In the Restart Instance message, click OK. |
| Download an SSL certificate | SSL encryption is in the Enabled state. | Click Download Certificate to download the SSL certificate to your on-premises machine. |
| Disable SSL encryption | SSL encryption is in the Enabled state. | i. Turn off SSL Status. ii. In the Restart Instance message, click OK. |

| Parameter | Description |
|---|---|

4. In the left-side navigation pane, choose **Data Security > SSL**.
5. Perform operations described in the following table based on your business requirements.

**Note**

When you enable or disable SSL encryption or renew SSL certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your applications can automatically reconnect to the instance.

**Method 2**

**Note**

The following procedure applies only to ApsaraDB for MongoDB V8.0 and V7.0.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set instance List** page, find the instance that you want to manage and
click the ID of the instance.
4. In the left-side navigation pane, choose **Data Security > SSL**.
5. On the right side of the page, configure the parameters.

| Select Configuration Mode | Simple Mode: You do not need to configure a client certificate. This mode is suitable for basic SSL encryption scenarios. Complete Mode: You need to configure access control lists (ACLs) and certificates. This mode is suitable for scenarios that require higher security. |
|---|---|
| Select Certificate Type | Select the source of the SSL certificate. We recommend that you use a certificate hosted in the cloud for better security and convenience. |
| Select Connection String to Protect | Select a database endpoint that requires SSL encryption. You can select an internal endpoint. |

6. Click **Enable SSL Encryption**.

**Note**

The result of the operation is displayed after a short period of time. You can also click **Modify Expiry** or **Download CA Certificate** to perform the corresponding operation.

### Configure TDE for an

**ApsaraDB for MongoDB instance**

You can use transparent data encryption (TDE) to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to the disk and is decrypted when it is read from the disk to the memory. TDE does not increase the sizes of data files. You do not need to modify your application to use TDE. To improve data security, you can enable TDE for an instance in the ApsaraDB for MongoDB console to encrypt instance data.

**Prerequisites**

The MongoDB version of the instance is 4.0.

**Note**

Before you enable TDE, you can create an instance that runs MongoDB 4.0 to test the compatibility between your application and the database version. You can release the instance after the test is complete.

**Impacts**

When you enable the TDE feature, your instance is restarted and a transient connection occurs. We recommend that you enable the TDE feature during off-peak hours and make sure that your application can automatically reconnect to the instance. TDE increases the CPU utilization of your instance.

**Usage notes**

You cannot disable TDE after it is enabled. You can enable TDE for an instance and disable encryption for a collection.

**Note**

If you have specific requirements, you can disable encryption for a collection when you create the collection. For more information, see the Disable encryption for a specified collection section of this topic. After you enable TDE, only new collections are encrypted. Existing collections are not encrypted. Key Management Service (KMS) generates and manages the keys used by TDE. ApsaraDB for MongoDB does not provide keys or certificates required for encryption.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set Instances** page, find the instance that you want to manage.
3. Click the ID of the instance. You can also click the
icon in the **Actions** column corresponding to the instance and then select **Manage** to go to the **Basic Information** page.
4. In the left-side navigation pane, choose **Data Security > TDE**.
5. Turn on TDE Status to enable TDE.
6. In the **Restart Instance** message, select **Use Automatically Generated Key** or **Use**
**Custom Key**.
7. In the message that appears, click **OK**.
The instance state changes to **Modifying TDE**. After the state changes to **Running**, TDE is enabled.

**Disable encryption for a specified collection**

After you enable TDE, all new collections are encrypted. When you create a collection, you can perform the following steps to disable encryption for the collection:
1. Use the mongo shell to connect to an ApsaraDB for MongoDB database. For more
information, see Use the mongo shell to connect to an ApsaraDB for MongoDB instance.
2. Run the following command to create a collection and disable encryption for the collection:

```
db.createCollection("<collection_name>",{ storageEngine: { wiredTiger: { configString: "encryption=(name=none)" } } })
```

**Note**

<collection_name>: the name of the collection. Examples

```
db.createCollection("customer",{ storageEngine: { wiredTiger: { configString: "encryp tion=(name=none)" } } })
```

### Use the mongo shell to

**connect to an ApsaraDB for**

**MongoDB database in SSL**

**encryption mode**

This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB database in Secure Sockets Layer (SSL) encryption mode. SSL encryption can encrypt network connections at the transport layer to improve data security and ensure data integrity.

**Prerequisites**

The instance is a replica set instance that runs MongoDB 4.0 or 4.2. The mongo shell of the required version is installed on the on-premises server or Elastic Compute Service (ECS) instance from which you want to connect to the database. For more information about how to install the mongo shell, see Install MongoDB. SSL encryption is enabled for the instance. For more information, see Configure SSL encryption for an ApsaraDB for MongoDB instance. The IP address of the on-premises server or ECS instance is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist.

**Usage notes**

After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary.

**Procedure**

An on-premises server with a Linux operating system is used in the following example.
1. Download the SSL CA certificate. For more information, see Configure SSL encryption for an
ApsaraDB for MongoDB instance.
2. Decompress the package and upload the certificate files to the on-premises server or the
ECS instance on which the mongo shell is installed.

| the Enter key. |  |  |
|---|---|---|
| Note The password characters are masked when you enter the password. If you forget the password of the root user, you can reset the password. For more information, see Reset the password for an ApsaraDB for MongoDB instance. |  |  |

**Note**

In this example, the .pem file is uploaded to the /root/sslcafile/ directory of the on-premises server.
3. On the on-premises server or the ECS instance, run the following command to connect to a
database of the ApsaraDB for MongoDB instance:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database> --ssl --sslC AFile <sslCAFile_path> --sslAllowInvalidHostnames
```

**Note**

If you want to connect to a database of the ApsaraDB for MongoDB instance over an internal network, make sure that the ApsaraDB for MongoDB instance has the same network type as the ECS instance. If the network type is Virtual Private Cloud (VPC), make sure that the two instances are in the same VPC. <host>: the endpoint of the primary node or a secondary node in a replica set instance or a mongos node in a sharded cluster instance. For more information, see Overview of replica set instance connections or Overview of sharded cluster instance connections. <username>: the database account of the ApsaraDB for MongoDB instance. The initial account is root. <database>: the name of the database corresponding to the username if authentication is enabled. If the username is root, enter admin. <sslCAFile_path>: the path of the SSL CA certificate files. Example:

```
mongo --host dds-bpxxxxxxxx-pub.mongodb.rds.aliyuncs.com:3717 -u root -p --authentica tionDatabase admin --ssl --sslCAFile /root/sslcafile/ApsaraDB-CA-Chain.pem --sslAllo wInvalidHostnames
```

## Tag management

### Add or create tags

You can add tags to one or more instances and filter the instances by tag.

**Prerequisites**

An ApsaraDB for MongoDB instance is created.

**Limits**

A maximum of 20 tags can be added to an instance.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. Find the instance to which you want to add tags, move the pointer over the tag column, and
then click the icon.
4. In the **Edit Tags** dialog box, click **Add**.
5. Enter a tag key and a tag value in the fields below **Tag Key** and **Tag Value**.
If you want to add an existing tag, click the corresponding field and select an existing tag key and tag value from the drop-down list.
6. Click **OK**.

### Filter instances by tag

After you add tags to ApsaraDB for MongoDB instances, you can filter the instances by tag in the instance list to quickly find the instances of a specified category.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Instance List** page, click **Advanced Filter**.
4. On the right side of **Filter by Tag**, select a **tag key** and a **tag value** from the drop-down
list.
5. Click **Search**.

### Remove or delete a tag

When a tag is no longer required in an ApsaraDB for MongoDB instance, you can remove the tag from the instance. If the tag is not added to other instances, the tag is deleted.

**Usage notes**

You can remove up to 20 tags at a time. If you remove a tag from all instances to which the tag is added, the tag is automatically deleted. Removing a tag does not affect the normal operation of the instance. After all tags of the instance are removed, the instance cannot be filtered by tag.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. Find the instance to which you want to add tags, move the pointer over the tag column, and
then click the icon.
4. In the **Edit Tags** dialog box, click the
icon next to the tag that you want to delete.
5. Click **OK**.
ry

## Zone-disaster recovery

### Create a dual-zone replica

**set instance**

This topic describes how to create a dual-zone replica set instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the reliability and availability of your replica set instance. This solution deploys the three nodes of a replica set instance across two different zones within one region. The components in these zones exchange data over an internal network. When one of the two zones becomes unavailable due to unexpected events such as a power or network failure, the high-availability (HA) system switches services over to another zone.

**Deployment policies**

The primary, secondary, and hidden nodes of a replica set instance are deployed in two different zones within one region.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances**.
3. On the **Replica Set Instances** page, click **Create Instance**.
4. On the **Create ApsaraDB for MongoDB Instance** page, configure parameters.

**Note**

For the **Zone** parameter, you must select dual zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region. For more information, see Procedure.
5. Click **Submit**.

### Create a dual-zone sharded

**cluster instance**

This topic describes how to create a dual-zone sharded cluster instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the high availability (HA) of your sharded cluster instances. This solution deploys the components of a sharded cluster instance across two different zones within the same region. The components in these zones exchange data over an internal network. If one zone becomes unavailable due to uncontrollable circumstances, the HA system automatically switches business over to the other zone to ensure service continuity of the sharded cluster instance.

**Deployment policies**

The components of a sharded cluster instance are deployed across two different zones within one region. Mongos nodes are evenly deployed across all data centers. At least two mongos nodes are deployed at a time, with each in one zone. Each new mongos node added later is deployed to one of the zones in turn. ry The primary, secondary, and hidden nodes in each shard node are not deployed to the two zones in sequence. The deployment of these nodes may change when manual switchover or HA failover between primary and secondary nodes is triggered.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Sharded Cluster Instances**.
3. On the **Sharded Cluster Instances** page, click **Create Instance**.
4. On the **Create ApsaraDB for MongoDB Sharded Cluster Instance** page, configure the
required parameters.

**Note**

For the **Zone** parameter, you must select two zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region. For more information, see Create a replica set instance.
5. Click **OK**.

| Source instance version |  | Destination instance version |  |
|---|---|---|---|
| 3.0 | 3.0 | 8.0 | 8.0 |
| 3.4 |  | 8.0 |  |
| 4.0 | 4.0 | 8.0 |  |
| 4.2 |  | 8.0 |  |
| 5.0 | 5.0 | 8.0 |  |
| 6.0 | 6.0 | 8.0 |  |
| 7.0 | 7.0 | 8.0 |  |
| 8.0 | 8.0 | 8.0 |  |
| 3.0 | 3.0 | 7.0 | 7.0 |
| 3.4 |  | 7.0 |  |
| 4.0 | 4.0 | 7.0 |  |
| 4.2 |  | 7.0 |  |
| > Document Version: 20260630 |  |  | 14 |

## AI capability

### One-click migration

#### Migrate data between MongoDB

**databases**

After you create an ApsaraDB for MongoDB instance, you can use Data Transmission Service (DTS) to migrate data to the ApsaraDB for MongoDB instance. You only need to change the service address after the migration.

**Supported source and destination databases**

| 5.0 | 5.0 | 7.0 |  |
|---|---|---|---|
| 6.0 | 6.0 | 7.0 |  |
| 3.0 | 3.0 | 6.0 | 6.0 |
| 3.4 |  | 6.0 |  |
| 4.0 | 4.0 | 6.0 |  |
| 4.2 |  | 6.0 |  |
| 5.0 | 5.0 | 6.0 |  |
| 3.0 | 3.0 | 5.0 | 5.0 |
| 3.4 |  | 5.0 |  |
| 4.0 | 4.0 | 5.0 |  |
| 4.2 |  | 5.0 |  |
| 3.0 | 3.0 | 4.2 | 4.0 |
| 3.4 |  | 4.2 |  |
| 4.0 | 4.0 | 4.2 |  |
| 3.0 | 3.0 | 4.0 |  |
| 3.4 |  | 4.0 |  |

**Prerequisites**

Replica-to-replica migration: A source ApsaraDB for MongoDB replica set instance and a destination ApsaraDB for MongoDB replica set instance are created. A whitelist is created for the source instance and destination instance. The IP address 0.0.0.0/0 is added to the whitelist.

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The collections to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select collections as the objects to be migrated and you need to edit collections in the destination database, such as renaming collections, up to 1,000 collections can be migrated in a single data migration task. If you run a task to migrate more than 1,000 collections, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the collections or configure a task to migrate the entire database. The size of a single data entry in the source database cannot exceed 16 MB. Otherwise, the data migration task fails. |

The data migration information, including the business database, account, and password, is prepared. Whether the ports of the source and destination instances are the same is determined if you want to change the database connection address. The connection address cannot be changed if the source database and destination database are on the same instance. The available storage space of the destination ApsaraDB for MongoDB instance is 10% larger than the total size of the data in the source ApsaraDB for MongoDB instance. Shard--to-shard migration (conditional support): A source ApsaraDB for MongoDB replica set instance and a destination ApsaraDB for MongoDB sharded cluster instance are created. A whitelist is created for the source instance and destination instance. The IP address 0.0.0.0/0 is added to the whitelist. The data migration information, including the business database, account, and password, is prepared. Shard connection between the source and destination instances is enabled. The source and destination clusters have the same number of mongos nodes. Only the mongos addresses are changed. The connection addresses between the shards and configserver node remain unchanged. Whether the ports of the source and destination instances are the same is determined if you want to change the database connection address. The connection address cannot be changed if the source database and destination database are on the same instance.

**Usage notes**

| Other limits | DTS cannot migrate data from the admin or local database. If a primary or unique key conflict occurs when DTS writes data to the destination collection, DTS skips the corresponding data write statement and retains the existing data in the destination collection. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that DTS uses to access the destination database. Otherwise, the data in the source database overwrites the data in the destination instance after the failed data migration task is resumed. You must use the db.$table name.aggregate([{ $count:"myCount"}]) _ syntax to query the return value of a count operation on the destination ApsaraDB for MongoDB database. |
|---|---|

| Version | Description |
|---|---|
| MongoDB 8.0 | We recommend that you do not use the tcmallocAggressiveMemoryDecommit parameter. The tcmallocReleaseRate parameter specifies the memory release rate. By default, ApsaraDB for MongoDB uses a value of 10 MB/s. If null is used as a query condition, MongoDB does not match undefined values. We recommend that you do not use index filters. We recommend that you do not use timeField as the shard key for time series sets. We recommend that you do not use the cleanupOrphaned command. The compact command cannot be executed concurrently in the same set. Before you upgrade to MongoDB 8.0, you must rename or delete any non- time-series set named system.buckets , if such a set exists. |

**Compatibility changes of MongoDB major versions**

The following table describes the compatibility changes of MongoDB major versions.

| MongoDB 7.0 | When you upgrade the major version of an instance to MongoDB 7.0, no compatibility issues exist. If you want to downgrade an instance from MongoDB 7.0 to an earlier major version, you must remove the features supported by MongoDB 7.0, such as the following items: Remove all columnar indexes . Unregister the cluster parameters specified by the setClusterParameter command. Remove all collections that are created with the encryptedFields option. Remove all compound wildcard indexes . |  |
|---|---|---|
| MongoDB 6.0 | If the memory used by an aggregation pipeline exceeds 100 MB, data is written to temporary files on disk by default. If you use a version earlier than MongoDB 6.0, you must use the { allowDiskUse: true } syntax to write data to temporary files on disk. If you specify * in the dropIndexes command, you can drop all indexes except id and the shard key index. _ The mongo shell is deprecated. Use mongosh instead. Operators, such as $explain , $hint , $max , and $maxTimeMS , are deprecated. If the expireAfterSeconds parameter of a time-to-live (TTL) index is set to NaN , it is treated as 0 , which may immediately remove expired documents. The SCRAM-SHA-1 mechanism is deprecated. The reIndex command and the corresponding reIndex() method are deprecated. |  |
| MongoDB 5.0 | The read concern level of secondary nodes is changed from available to local . The default write concern level is changed from 1 to majority . The db.collection.ensureIndex() method is deprecated. You can use the db.collection.createIndex() method instead. The parameters of the saslStart and saslContinue commands are strictly validated and not supported by the MongoDB driver for Go ( mgo ). The saslContinue command contains only the conversationId and payload parameters, whereas mgo has an additional mechanism parameter. The geoSearch command is deprecated. |  |

|  | expireAfterSeconds |
|---|---|
| NaN |  |

| MongoDB 4.4 | The force option is no longer supported by the compact command. The geoSearch command is deprecated. You can create indexes on both the primary and secondary databases to reduce the latency caused by index creation. This way, when an index is being created, the secondary database can still access the latest data. |
|---|---|
| MongoDB 4.2 | The geoNear command is deprecated. Use the $geoNear (aggregation) command instead. The repairDatabase command is deprecated. The cloneCollection command is deprecated. Use the mongoexport and mongoimport tools instead. The afterClusterTime read concern option is deprecated. Drivers that are compatible with MongoDB 4.2 or later enable retryable writes by default. The group , copydb , and clone commands are deprecated. |
| MongoDB 4.0 | The reIndex command obtains a global exclusive (W) lock and blocks other operations until an index is rebuilt. The copydb and clone commands are deprecated. |
| MongoDB 3.6 | The use of the aggregate command without the cursor option to return a single document is deprecated. Unless you include the explain option, you must specify the cursor option. You can use the cursor option to specify a batch size. In MongoDB 3.6 and later versions, the query for $type: "array" returns documents where the field itself is an array. In versions earlier than MongoDB 3.6, the query for $type: "array" returns documents where the field itself is an array that contains at least one element of the array type. The following changes to array ordering are added: The optional sort option is added to the find command to provide the ordering of results. $sort in the $sort(aggregation) stage has a memory limit of 100 MB. If an update operation involves multiple fields, the fields are added in lexicographical order. The snapshot query option is deprecated. |

| MongoDB 3.4 | The group command is deprecated. Use the db.collection.aggregate() or db.collection.mapReduce() method instead. The $in expression is used in an update operation with the upsert option set to true to determine whether matching documents exist. Example: db.c.drop() db.c.update({a:{$in:[1]}},{$addToSet:{a:2}},{upsert:true}) // A document cannot be inserted in MongoDB 3.4, but can be inserted in MongoDB major versions earlier than 3.4. db.c.update({a:{$elemMatch:{$in:[2]}}},{$addToSet:{a:2}}, {upsert:true}) // A document can be successfully inserted in MongoDB 3.4. |
|---|---|

| Database | Database and schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source instance | Read permissions on the database to be migrated and the config database. |  | Read permission on the source database, the admin database, and the local database |
| Destination instance | The dbAdminAnyDatabase permission, the read and write permissions on the destination database, and the read permissions on the local database. |  |  |

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the migration task. DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |

**Required account permissions**

**Use DTS to migrate data**

**Procedure**

1. Log in to the **ApsaraDB for MongoDB console**.
2. In the left-side navigation pane, choose **AI Capabilities > Intelligent Migration**. On the
Data Migration page, click **To migrate** and configure the source and destination databases.

| Source Database | Instance Region | The region in which the source ApsaraDB for MongoDB instance resides. The region is the source region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|---|---|---|
|  | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. Select No. |
|  | Architecture | Select Replica Set or Sharded Cluster. Note If you select Sharded Cluster, you must apply for shards for both the source and destination instances. |
|  | Instance ID | The ID of the source instance. |
|  | Authenticati on Database | The name of the authentication database in which the database account is created. Note If you want to use the root account, enter admin in the Database Name field. |
|  | Database Account | The account of the source database. The account must have the read permissions on the source database, admin database, and local database. |
|  | Database Password | The password of the database account. |
|  | Instance Region | The region in which the destination ApsaraDB for MongoDB instance resides. The region is the destination region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|  | Architecture | Select Replica Set or Sharded Cluster. |
|  | Instance ID | The ID of the destination ApsaraDB for MongoDB instance. |

|  | Authenticati on Database | The name of the authentication database in which the database account is created. Note If you want to use the root account, enter admin in the Database Name field. |
|---|---|---|
|  | Database Account | The account of the destination database. The account must have the read permissions on the destination database, admin database, and local database. |
|  | Database Password | The password that is used to access the database. |

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database. If the source and destination databases have different table schemas, only specific columns are migrated, or the data migration task fails. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Source Objects | Select one or more objects in the Available section and add the objects to the Selected section. Note You can use the navigation tree to search for one or more objects. You can select tables or databases as the objects to be migrated. |
|---|---|
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. Note To select the SQL operations performed on a specific database or table, right-click the object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Select Yes or No based on your business requirements. |

5. Click **Next: Advanced Settings** to configure advanced settings. The following table
describes the parameters.
6. In the lower part of the page, click **Next: Precheck and Start Task**.

| Method | Use case | Details |
|---|---|---|
| ApsaraCopilot- Managed Mode (Recommended for beginners) | Ideal for users who want to quickly test AI and database integration scenarios without deployment or development. | 1. Log on to the ApsaraCopilot platform. 2. On the home page, select the MCP Service entry. 3. The system automatically loads available MCP agents and services. 4. Select the required functional module. |

**Important**

Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.
7. Wait until **Success Rate** displays 100% and then click **Back**.

**Note**

If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

**Switch to the endpoint of the destination database**

Select a successful record from the migration result list and click **Migrate Endpoint** to switch to the endpoint of the destination database. After you update the DNS record, clients may still be connected to the source database due to the caching mechanism. You need to close the connections to the source database.

### AI-native MCP service

The MongoDB AI-native MCP (Model Context Protocol) service provides a standard, secure, and efficient protocol for large models to access your database. By using MCP, AI applications can directly query data, execute SQL, or manage database instances without complex coding, accelerating the development of AI-native use cases such as Retrieval-Augmented Generation (RAG), intelligent operations, and data-driven Q&A. On the **MongoDB console > AI Capability > AI-native MCP service** page, you can explore and use various MCP integration methods to efficiently connect your AI applications to your databases.

**Integration methods**

The MCP service offers three flexible integration methods to meet different needs, from quick trials to production-ready integrations.

| AI Gateway- managed mode (Recommended for production integration) | Ideal for enterprise-level AI application integration. Alibaba Cloud hosts the backend services, which you can use immediately after activation. | 1. Log on to the AI Gateway console. 2. Navigate to Service Management > MCP Service. 3. The system automatically loads available MCP agents and services. 4. Activate the required MCP services, such as the Mongo MCP Server and Mongo Management MCP services. |
|---|---|---|
| Self-deployment (For on-premises or custom scenarios) | Designed for users who require on-premises deployment, custom logic, or integration with their own agent or RPA systems. | 1. Download the MCP service package. 2. Deploy the package on an ECS instance, a container, or a non-cloud server. 3. Embed the MCP service as a backend service in your AI application, agent, or RPA workflow. 4. Call MCP functions through a RESTful API or SDK. |

**Supported MCP services**

You can access supported MCP services from the console.

**Mongo MCP Server**

Overview: The Mongo MCP Server provides AI-native data management capabilities for MongoDB. This service offers a suite of tools for manipulating and querying data in MongoDB, enabling external applications, such as AI model agents, to access the database. Core functions: `list_collections` : Lists all collections. `find_tool` : Executes a query to find documents.

**Mongo Management MCP**

Overview: The Mongo Management MCP provides native interfaces for ApsaraCopilot. It allows you to open the MCP service within ApsaraCopilot to enhance instance operations and management. Core functions: `sql_query` : Runs SQL queries. `execute_sql` : Executes SQL statements.

## CloudDBA

### Quick diagnostics

ApsaraDB for MongoDB supports the quick diagnostics feature. This feature performs diagnostics on instance status within a specified period of time to help you evaluate the health status of the instance from multiple aspects, such as slow query logs, tablespaces, and performance trends and quickly identify instance anomalies.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the left-side navigation pane, choose **CloudDBA > One-click diagnosis**.
5. Click **Create Reports**.
6. In the **Create Reports** dialog box, specify a time range for which you want the system to
perform diagnostics and then click **Confirmation**.

**Note**

The time range cannot exceed one day. If you specify a shorter time range for diagnostics, more detailed statistics are collected in the diagnostic report.
7. Refresh the Diagnostic Report page to view the progress of the diagnostics task. After the
diagnostic report is created, click **View Report** in the **Actions** column.

**Automatically generate diagnostic reports**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance, or click in the **Actions** column corresponding to the instance and select
**Manage**.
4. In the left-side navigation pane, choose **CloudDBA > One-click diagnosis**.
5. Click **Auto generating Report Settings**.
6. In the **Auto-generating Diagnostic Report Settings** dialog box, specify a time at which
you want the system to automatically generate diagnostic reports.

**Note**

Only **Scheduled Trigger** is supported.

| Module | Description |
|---|---|
| Score | The instance's health score. If the score is not full, you can click Deduction Details to view specific deduction information. |
| Basic Instance Information | Displays the instance ID, specifications, database type, analysis node, region, and the name of the database being analyzed. |
| Summary | Displays key performance metrics: CPU utilization, memory usage, connections, disk usage, and IOPS usage. |
| Slow SQL Query | Displays the 10 statements with the longest execution time. |
| Tablespace | Displays the five tables that occupy the most space. |
| Performance Trend | Displays performance trends for CPU utilization, connections, memory usage, disk usage, and IOPS usage. |
| Download | Click Download in the navigation pane on the left to download the diagnostic report. |

7. Click **OK**.

**Diagnostic report details**

### Performance trends

This topic describes how to view performance trends in specific ranges, compare performance trends, and customize charts to view performance trends on an ApsaraDB for MongoDB instance.

**Go to the Performance page**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, choose **CloudDBA > Performance Trends**.

**Note**

For more information about performance trends, see **Performance trends** in **Database Autonomy Service User Guide**.

### Real-time performance

This topic describes how to view real-time performance data of an ApsaraDB for MongoDB instance, such as read/write latency, queries per second (QPS), operations, connections, and network traffic.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, find the instance
that you want to manage and click the ID of instance.
4. In the left-side navigation pane, choose **CloudDBA > Real-time Performance**.

**Page overview**

On the Real-time Performance page, you can click the Real-time Charts or Mongostat tab to view performance data. When you refresh the **Real-time Performance** page, the data on the Real-time Charts and Mongostat tabs is refreshed and **Available Refreshes** is reset in the upper-right corner. Real-time Charts tab By default, content on the **Real-time Charts** tab is displayed when you go to the Real-time Performance page. Line charts on the tab are refreshed every 5 seconds to provide up-todate performance trends.

**Note**

You can move the pointer over next to a performance metric to view the details of the metric. Mongostat Click the **Mongostat** tab to view Mongostat command outputs. A new line of real-time performance data is added every 5 seconds. The tab can contain up to 999 lines of data.

**Note**

For more information about Mongostat command outputs, see mongostat.

### Session management

The instance sessions feature allows you to view the statistics for sessions between an ApsaraDB for MongoDB instance and clients in real time. These statistics include clients, commands that were run, and connection duration. You can also close abnormal sessions based on your business requirements.

**View instance sessions**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, choose **CloudDBA > Sessions**.
If you turn on **Auto Refresh**, the system updates session data on the page every 5 seconds. By default, the system displays only active sessions. You can turn on **Display All** to view all sessions. In the **Session Statistics** section, you can view information about sessions in the
**Overview**, **Statistics by Client**, and **Statistics by Namespace** charts.

**Terminate instance sessions**

**Warning**

To prevent unexpected results, we recommend that you do not terminate system-level sessions.
1. In the **Instance Sessions** section, select the session that you want to terminate.
2. Click **Kill Selected**.
3. In the message that appears, click **OK**.

### Storage analysis

This topic describes how to view storage analysis information, such as the information in the
**Storage Overview**, **Exceptions**, **Storage Trend**, **Tablespaces**, and **Data Space** sections.
The information helps you identify and resolve exceptions in the database storage to ensure database stability.

**Prerequisites**

The database version of the ApsaraDB for MongoDB instance is 4.0 or 4.2.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to
the console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click **Replica Set Instances** or **Sharded Cluster**
**Instances**.
3. On the **Replica Set Instances** or **Sharded Cluster Instances** page, click the ID of an
instance.
4. In the left-side navigation pane, choose **CloudDBA > Storage Analysis**.
5. In the upper-right corner, click **Re-analyze**. Then, wait until the analysis is complete.
6. Click the **Storage Overview** or **Data Space** tab to view analysis results.
For more information about the Storage Overview tab, see Storage Overview tab. For more information about the Data Space tab, see Data Space tab.

**Storage Overview tab**

This tab contains four sections: **Storage**, **Exceptions**, **Storage Trend**, and **Tablespaces**.
**Storage** section

| Item | Description |
|---|---|
| Exception | The number of storage exceptions that are identified in the instance. ApsaraDB for MongoDB can identify the following types of exceptions: More than 90% of the storage capacity is used. The available physical storage space may be exhausted within seven days. A single collection contains more than 10 indexes. |
| Avg Daily Increase in Last Week | The average daily increase of storage usage in the instance over the last seven days. Formula: (Size of available storage space at the time of collection - Size of available storage space seven days ago)/7. Note This increase indicates the average daily increase over the last seven days at the time of collection. This parameter is suitable for scenarios in which the traffic volume remains stable. The value of this parameter is inaccurate in the event of abrupt storage changes that are caused by operations such as batch import, deletion of historical data, instance migration, or instance recreation. |
| Available Days of Storage | The number of days during which storage space is available in the instance. Formula: Size of available storage space/Average daily increase over the last seven days. Note 90+ indicates that the storage space is sufficient for more than 90 days of usage. This parameter is suitable for scenarios in which the traffic volume remains stable. The value of this parameter is inaccurate in the event of abrupt storage changes that are caused by operations such as batch import, deletion of historical data, instance migration, or instance recreation. |
| Used Storage | The amount of storage space that is used in the instance to the total storage space. |

**Exceptions** section
Information about detected storage exceptions. You can resolve the exceptions based on the information in this section.
**Storage Trend** section
Changes in storage usage over the last week, such as changes in **used storage**, **data**
**space**, and **log space**.
**Tablespaces** section
Information about all tables, such as the database name, storage engine, and collection storage.

**Note**

You can click the name of a collection to view its indexes.

**Data Space tab**

The Data Space tab shows the total storage space and tablespace information of each database.

**Note**

You can click the name of a data space to view its tablespace information. You can click the name of a collection to view its indexes.

### Slow query logs

ApsaraDB for MongoDB allows you to identify, analyze, and track slow query logs and perform a diagnostics on the logs so that you can create indexes to make better use of instance resources.

**Procedure**

1. Log on to the ApsaraDB for MongoDB console.
2. On the **Replica Set Instances** page, find the instance that you want to manage.
3. Click the ID of the instance. You can also click the
icon in the **Actions** column corresponding to the instance and then select **Manage** to go to the **Basic Information** page.
4. In the left-side navigation pane, choose **CloudDBA > Slow Query Logs**.

**Note**

By default, slow query logs generated in the last 15 minutes are displayed in the trend chart. You can also specify a time range and click **Search** to view the corresponding slow query logs. The maximum time range that you can specify is one day.
5. View details of slow query logs by using one of the following methods:
Method 1: i. Click the **Slow Log Details** tab in the lower part of the page. ii. On the **Slow Log Details** tab, select the database that you want to query.

**Note**

If the request content of the database is hidden, you can move the pointer over the corresponding **Request Content** column and view the complete content. Method 2: i. In the Slow Log Trend chart, click a point in time. Then, you can view the statistics of the slow query logs generated at the point in time on the **Slow Log Statistics** tab. ii. On the **Slow Log Statistics** tab, click **Sample** in the **Actions** column. In the **Slow Log Sample** dialog box, you can view details of the slow query log.

**Note**

If the request content of the database is hidden, you can move the pointer over the corresponding **Request Content** column and view the complete content. You can click **Export Slow Log** on the **Slow Log Statistics** tab to save the log data to your computer.

## Appendix

### Authorize a tenant

**organization to access SLB**

This topic describes how to grant a tenant organization the permissions to access Server Load Balancer (SLB) and helps you efficiently resolve related issues.

**Important**

If you need to create and use IPv6 addresses for your business, you must ensure that the current tenant organization has explicitly granted database services the permissions to access SLB. If such permissions are not granted, IPv6 addresses cannot be created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the Service-linked Roles page, click **Create Service-linked Role** in the upper-left
corner. Select **Server Load Balancer** for the **Service Name** parameter, and select the organization to which you want to grant permissions for the **Authorized Organization**
**Name** parameter.
5. Click **OK**.
