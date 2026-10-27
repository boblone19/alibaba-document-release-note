---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 80
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20for%20MongoDB%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for MongoDB User Guide 20220928

## Table of Contents

- 1 Usage notes
- 2 Log on to the ApsaraDB for MongoDB console
- 3 Quick start
  - 3.1 Use ApsaraDB for MongoDB
  - 3.2 Create an ApsaraDB for MongoDB instance
  - 3.3 Reset the password for an ApsaraDB for MongoDB instance
  - 3.4 Configure a whitelist for an ApsaraDB for MongoDB instance
  - 3.5 Connect to an instance
    - 3.5.1 Use DMS to log on to an ApsaraDB for MongoDB instance
    - 3.5.2 Use the mongo shell to connect to an ApsaraDB for MongoDB instance
    - 3.5.3 Introduction to connection strings and URIs
      - 3.5.3.1 Overview of replica set instance connections
      - 3.5.3.2 Overview of sharded cluster instance connections
- 4 Instances
  - 4.1 Create an ApsaraDB for MongoDB instance
  - 4.2 View the details of an ApsaraDB for MongoDB instance
  - 4.3 Restart an ApsaraDB for MongoDB instance
  - 4.4 Change the specifications of an ApsaraDB for MongoDB instance
  - 4.5 Change the name of an ApsaraDB for MongoDB instance
  - 4.6 Reset the password for an ApsaraDB for MongoDB instance
  - 4.7 Switch node roles
  - 4.8 Migrate an ApsaraDB for MongoDB instance across zones in the same region
  - 4.9 Release an ApsaraDB for MongoDB instance
  - 4.10 Primary/secondary failover
    - 4.10.1 Trigger a primary/secondary failover for a replica set instance
    - 4.10.2 Trigger a primary/secondary failover for a sharded cluster instance
  - 4.11 Monitoring
- 5 Backup and restoration
  - 5.1 Configure automatic backup for an ApsaraDB for MongoDB instance
  - 5.2 Manually back up an ApsaraDB for MongoDB instance
  - 5.3 Download a backup file
  - 5.4 Restore data to the current ApsaraDB for MongoDB instance
- 6 Database connections
  - 6.1 Modify a public or internal endpoint of an ApsaraDB for MongoDB instance
  - 6.2 Use DMS to log on to an ApsaraDB for MongoDB instance
  - 6.3 Use the mongo shell to connect to an ApsaraDB for MongoDB instance
  - 6.4 Apply for a public endpoint for an ApsaraDB for MongoDB instance
  - 6.5 Release a public endpoint
  - 6.6 Overview of replica set instance connections
  - 6.7 Overview of sharded cluster instance connections
- 7 Data security
  - 7.1 Configure a whitelist for an ApsaraDB for MongoDB instance
  - 7.2 Create or delete a whitelist
  - 7.3 Audit logs
  - 7.4 Configure SSL encryption for an ApsaraDB for MongoDB instance
  - 7.5 Configure TDE for an ApsaraDB for MongoDB instance
  - 7.6 Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode
- 8 Zone-disaster recovery
  - 8.1 Create a dual-zone replica set instance
  - 8.2 Create a dual-zone sharded cluster instance
- 9 CloudDBA
  - 9.1 Performance trends
  - 9.2 Real-time performance
  - 9.3 Instance sessions
  - 9.4 Storage analysis
  - 9.5 Slow query logs

## 1 Usage notes

You must get familiar with the precautions and limits of ApsaraDB for MongoDB before you start. To ensure the stability and security of ApsaraDB for MongoDB instances, take note of the limits, see Instance types in ApsaraDB for MongoDB ApsaraDB for MongoDB limits. ApsaraDB for MongoDB limits

| Item | Limit |
|---|---|
| Scale out nodes | You cannot scale out secondary nodes. |
|   | When a replica set instance is created, three nodes are added. ApsaraDB for MongoDB provides a primary node, a secondary node, and a hidden node for each replica set instance. The hidden node is invisible to you. You cannot scale out secondary nodes. |
| Restart an instance | You must restart an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console or by calling the API operation. |

for MongoDB console

## 2 Log on to the ApsaraDB for MongoDB console

MongoDB console This topic describes how to log on to the ApsaraDB for MongoDB console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. In the top navigation bar, choose Product s > Dat abase Services > ApsaraDB f or MongoDB.

## 3 Quick start

### 3.1 Use ApsaraDB for MongoDB

This topic is a quick start guide to basic usage operations for ApsaraDB for MongoDB, such as creating an instance, configuring a whitelist, and connecting to an instance. Flowcharts are used to describe the basic procedures in ApsaraDB for MongoDB, and guide you to create an ApsaraDB for MongoDB instance. An instance is a virtual database server on which you can create and manage multiple databases. After you create an ApsaraDB for MongoDB instance, you need to configure a whitelist for the instance to allow external devices to access the instance. A whitelist can enhance access security for ApsaraDB for MongoDB instances. We recommend that you update the whitelist on a regular basis. The normal services of the instance are not affected if you configure a whitelist. Connect to a replica set instance by using the mongo shell After you create an instance and configure a whitelist, you can use the mongo shell to connect to the instance.

### 3.2 Create an ApsaraDB for MongoDB instance

instance This topic describes how to create an instance in the ApsaraDB for MongoDB console. Prerequisites An account is obtained to log on to the ApsaraDB for MongoDB console. Create a replica set instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. On the Replica Set Inst ances page, click Creat e Inst ance in the upper-left corner. On the
Creat e ApsaraDB f or MongoDB Inst ance page, configure the parameters. The following table describes the required parameters. Parameters for creating a replica set instance

| Section | Parameter | Description |
|---|---|---|
| Basic Set t ings | Organizat ion | Select an organization for the new instance. |
|   | Resource Set | Select a resource set for the new instance. |
| Region | Region | Select a region for the new instance. |
|   | Zone | Select a zone for the new instance |
| Specif icat ions | Dat abase Engine | Select a database engine for the new instance. In this case, you can select only MongoDB. |
|   | Engine Version | Select a database engine version for the new instance. Valid values: 3.0 3.4 4.0 4.2 |
|   | Node T ype | ApsaraDB for MongoDB supports the following options: Three-node Replica Set: uses dedicated memory and I/O resources but shares CPU and storage resources with other general-purpose instances on the same server. Dedicated Instance: uses dedicated CPU, memory, storage, and I/O resources to ensure long-term performance. In this case, an instance is not affected by other instances on the same server. Dedicated Host: exclusively uses all resources of a server. This is the top configuration of exclusive specifications. |
|   | Node Specif icat ions | Select a node specification for the new instance. For more information, see descriptions in the ApsaraDB for MongoDB console. |
|   | St orage Capacit y (GB) | The storage space of the instance, which contains the space for data, system files, log files, and transaction files. For more information, see Ins tance types in ApsaraDB for MongoDB Product Introduction. |

| Section | Parameter | Description |
|---|---|---|
| Net work | Net work T ype | ApsaraDB for MongoDB supports the following options: Classic Net work: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. VPC: Virtual Private Cloud (VPC) is an isolated network environment built in Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Not e If you select the VPC network type, you must configure the VPC and vSwit ch parameters. |
|   | VPC | Select a VPC. Not e When Net work T ype is set to VPC, you must specify this parameter. |
|   | vSwit ch | Select a vSwitch. Not e When Net work T ype is set to VPC, you must specify this parameter. |
| Password Set t ings | Inst ance Name | Set the name of the new instance. The name must be 2 to 256 characters in length, The name must start with a letter, and can contain digits, letters, underscores ( ), and hyphens (-). _ |
|   | Password Set t ing | Determine when to set the password for logging on to databases in the new instance. You can select Set Now to set the logon password immediately, or select Set af t er Purchase to set the logon password after you create the instance. For more information, see Reset the password for an ApsaraDB for MongoDB instance. |
|   | Logon Password | Set a password. The password must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The name can contain special characters. Special characters include ! # $ % ^ & * ( ) + = _ |
|   | Conf irm Password | Enter the password again. The password you enter here must be the same as that in New Password. |

3. Click Submit to create the instance.
Create a sharded cluster instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. Click Creat e Inst ance in the upper-left corner to go to the Creat e MongoDB Inst ance page.
Configure the parameters. The following table describes the required parameters. Parameters for creating a sharded cluster instance

| Section | Parameter | MNS logs |
|---|---|---|
| Basic Set t ings | Organizat ion | Select an organization for the new instance. |
|   | Resource Set | Select a resource set for the new instance. |
| Region | Region | Select a region for the new instance. |
|   | Zone | Select a zone for the new instance |
| Specif icat ions | Dat abase Engine | Select a database engine for the new instance. In this case, you can select only MongoDB. |
|   | Engine Version | Select a database engine version for the new instance. Valid values: 3.4 4.0 4.2 |
| Net work | Net work T ype | ApsaraDB for MongoDB supports the following options: Classic Net work: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. VPC: Virtual Private Cloud (VPC) is an isolated network environment built in Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Not e If you select the VPC network type, you must configure the VPC and vSwit ch parameters. |
|   | VPC | Select a VPC. Not e When Net work T ype is set to VPC, you must specify this parameter. |

|   | DB User Guide·Quick star |   |
|---|---|---|
| Section | Parameter | MNS logs |
|   | vSwit ch | Select a vSwitch. If no vSwitch exists, you can click Creat e vSwit ch to create a vSwitch. Not e When Net work T ype is set to VPC, you must specify this parameter. |
|   | Mongos Specif icat ions | The specifications of the mongos node. For more information, see descriptions in the ApsaraDB for MongoDB console. |
| Mongos Specif icat ions |   |   |
|   | Quant it y | The number of the mongos nodes. You can select 2 to 32 mongos nodes. |
| Shard Specif icat ions | Shard Specif icat ions | The specifications of the shard node. For more information, see descriptions in the ApsaraDB for MongoDB console. |
|   | St orage Capacit y (GB) | The storage space of the instance, which contains the space for data, system files, log files, and transaction files. For more information, see Ins tance types in ApsaraDB for MongoDB Product Introduction. |
|   | Quant it y | The number of the shard nodes. You can select 2 to 32 shard nodes. |
| Conf ig Server Specif icat ions | Conf ig Server Specif icat ions | The specifications of Configserver nodes. It is fixed at 1 vCPU, 2 GiB memory and cannot be customized. |
|   | St orage Capacit y (GB) | The storage space of the Configserver node. It is fixed at 20 GB and cannot be customized. |
| Password Set t ings | Inst ance Name | Set the name of the new instance. The name must be 2 to 256 characters in length, and can contain digits, letters, underscores ( ), and _ hyphens (-). It must start with a letter. |
|   | Password Set t ing | Determine when to set the password for logging on to databases in the new instance. You can select Set Now to set the logon password immediately, or select Set af t er Purchase to set the logon password after you create the instance. For more information, see Reset the password for an ApsaraDB for MongoDB instance. |
|   | Logon Password | Set a password. The password must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The name can contain special characters. Special characters include ! # $ % ^ & * ( ) + = _ |
| ument Version | : 20220928 1 |   |

|   | rt ApsaraDB for MongoD |   |
|---|---|---|
| Section | Parameter | MNS logs |
|   | Conf irm Password | Enter the password again. The password you enter here must be the same as that in New Password. |

4. Click Submit to create the instance.

### 3.3 Reset the password for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to reset your password in the ApsaraDB for MongoDB console. Context

> Not ice We recommend that you change your password on a regular basis to ensure data security.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Account s.
5. Click Reset Password in the Actions column and configure the parameters in the Reset Password
panel. describes the parameters. Parameters for resetting a password

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| New Password | Specify the new password of the account based on the following rules: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !#$%^&*() += _ The password must be 8 to 32 characters in length. |
| Conf irm New Password | Enter the password again. The password you enter here must be the same as that in New Password. |

6. Click OK.

### 3.4 Configure a whitelist for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or Classless Inter-Domain Routing (CIDR) blocks that you use for database access to a whitelist of this instance. This improves database security and stability. Proper configuration of whitelists can enhance access security of ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis. Context The system creates a default whitelist for each instance. This whitelist can be modified or cleared, but it cannot be deleted. After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the def ault whitelist of this instance. The IP address 0.0.0.0/0 indicates that all IP addresses are allowed to access this instance. You must add the IP addresses or CIDR blocks that you allow to access this ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > Whit elist Set t ings.
5. You can manually configure a whitelist or import ECS Internal IP addresses to the whitelist.
Manually modif y a whit elist i. Find the whitelist you want to modify and choose
> Manually Modif y in the Act ions

column. ii. Enter IP addresses or CIDR blocks.

> Not e
> Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits.
> If the IP whitelist is empty or only contains `0.0.0.0/0` , all devices are granted
> access. This is risky for your ApsaraDB for MongoDB instance. We recommend that you add only the IP addresses or CIDR blocks of your own web servers to the whitelist.

iii. Click OK. Load IP addresses of ECS inst ances i. Find the whitelist, and choose
> Import ECS Int ranet IP in the Act ions column.

ii. From the displayed internal IP addresses of ECS instances that belong to the current account, select the IP addresses and click to add them to the whitelist. iii. Click OK.

### 3.5 Connect to an instance

#### 3.5.1 Use DMS to log on to an ApsaraDB for MongoDB instance

MongoDB instance You can use DMS to connect to an ApsaraDB for MongoDB instance. Prerequisites The IP address whitelist is configured. For more information about how to configure the IP address whitelist, see Configure a whitelist for an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. Click Log On in the upper-right corner of the page.

> Not e For a sharded cluster instance, you must also select the Mongos node.

5. In the Login inst ance dialog box of the DMS console, check values of Dat abase t ype, Inst ance
Area, and Connect ion st ring address. If the information is correct, enter Dat abase account and Dat abase password, as shown in the following figure.

| Parameter | Description |
|---|---|
| Dat abase t ype | The engine of the database. By default, the engine of the database to be connected is displayed. |
| Inst ance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connect ion st ring address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Dat abase account | The account of the database to be connected. |
| Dat abase password | The password of the account used to connect to the database. |

6. Click Login.

> Not e If you want your web browser to remember the password, select Remember password before you click Login.

#### 3.5.2 Use the mongo shell to connect to an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by ApsaraDB for MongoDB. You can install it on your client or in an Elastic Compute Service (ECS) instance. Prerequisites The version of the mongo shell is the same as your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about the installation procedure, see Install MongoDB. Choose the version in the upper-left corner of the page based on your client version. The IP address of your client is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.

> Not e
> Replica set instances: View the connection string or connection string URI of a node.
> Sharded cluster instances: View the connection string or connection string URI of a mongos node.

For more information about connection strings, see Overview of replica set instance connections or Overview of sharded cluster instance connections.
5. Connect to the ApsaraDB for MongoDB instance from your client or ECS instance where the mongo
shell is installed. Replica set instances: Connection string of a node During routine tests, you can directly connect to a primary or secondary node. Note that if the primary node fails, the system automatically switches to the secondary node, and the roles of connected nodes change. This affects the read and write operations of your application. Command syntax:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database>
```

> Not e
> <host>: the connection string of the primary or secondary node.
> <username>: the username used to log on to a database of the instance. The initial username is root .
> <database>: the name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.

Example:

```
mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticati onDatabase admin
```

When `Enter password:` is displayed, enter the password of the database user and press the Enter key. If you forget the password of the root user, you can reset it. For more information, see Reset the password for an ApsaraDB for MongoDB instance.

> Not e The password characters are not displayed when you enter the password.

HA connection (recommended): You can use a connection string URI to connect to both the primary and secondary nodes of a replica set instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched. Command syntax:

```
mongo "<ConnectionStringURI>"
```

> Not e
> The connection string URI must be enclosed in a pair of double quotation marks ("").
> <ConnectionStringURI>: the connection string URI of the instance.
> You must replace `****` in the connection string URI with the database password.

For more information about how to set a database password, see Reset the password for an ApsaraDB for MongoDB instance. Example:

```
mongo "mongodb://root:****@dds-**********.mongodb.rds.intra.env17e.shuguang.com:3717, dds-**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
```

`*"` Sharded cluster instances: Connection string of a mongos node Command syntax:

```
mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
```

> Not e
> <mongos_host>: the connection string of a mongos node in the sharded cluster instance.
> <username>: the username used to log on to a database of the instance. The initial username is root .
> <database>: the name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.

Example:

```
mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authentication Database admin
```

HA connection (recommended): You can use a connection string URI to connect to a database. If one mongos node fails, another mongos node takes over business to ensure the high availability of the connection. Command syntax:

```
mongo "<ConnectionStringURI>"
```

> Not e
> The connection string URI must be enclosed in a pair of double quotation marks ("").
> <ConnectionStringURI>: the connect ion st ring URI of the instance.
> You must replace `****` in the connect ion st ring URI with the database

password. For more information about how to set a database password, see Reset the password for an ApsaraDB for MongoDB instance. Example:

```
mongo "mongodb://root:****@s-**********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
```

#### 3.5.3 Introduction to connection strings and URIs

##### 3.5.3.1 Overview of replica set instance connections

ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node, and use a connection string URI to connect to both of them. For high availability, we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections. Prerequisites A whitelist is configured for the instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. View connection strings
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.
Description of connection strings

| Item | Description |
|---|---|
| Connection type | Internal Connections - Classic Network: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. Internal Connections - VPC: A virtual private cloud (VPC) is an isolated network with higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints. |
| Role | Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance. Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance. Connection String URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and high availability. |
| Connection string | The connection string of a primary or secondary node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port used to connect to the instance. |

| Item | Description |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to a database of the replica set instance. You must separate them with a colon (:). hostX:portX: the endpoint and port of a node in the replica set instance. /database: the name of the database corresponding to the username if authentication is enabled. ?options: additional connection options. Not e If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. This way, when a node fails, the read and write operations of your application are not affected as a result of the failover. |

Related information Connect to a replica set instance by using the mongo shell

##### 3.5.3.2 Overview of sharded cluster instance connections

connections ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node, and use a connection string URI to connect to multiple mongos nodes. For high availability, we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections. View connection strings
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.
Description of connection strings

| Item | Description |
|---|---|
| Connection type | Internal Connections - Classic Network: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. Internal Connections - VPC: A virtual private cloud (VPC) is an isolated network with higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints. Public Connections: Security risks may arise if you connect to a sharded cluster instance over the Internet. Therefore, ApsaraDB for MongoDB does not provide public endpoints. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Alibaba Cloud (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint for an ApsaraDB for MongoDB instance. |
| Mongos ID | The connection string of a mongos node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port used to connect to the instance. Not e During routine tests, you can use a connection string to directly connect to a mongos node. |

| Item | Description |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to a database of the sharded cluster instance. You must separate them with a colon (:). hostX:portX: the endpoint and port of a mongos node in the sharded cluster instance. /database: the name of the database corresponding to the username if authentication is enabled. ?options: additional connection options. Not e If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads. If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |

Log on to a database of an ApsaraDB for MongoDB instance
1. Obtain the connection string and the following information:
The username used to log on to the database. The initial username is root. The password of the database user. If you forget the password of the root user, you can reset it. For more information, see Reset the password for an ApsaraDB for MongoDB instance. The name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.
2. Log on to the database.
Use DMS to log on to a replica set instance of ApsaraDB for MongoDB Connect to a replica set instance by using the mongo shell

## 4 Instances

### 4.1 Create an ApsaraDB for MongoDB instance

instance This topic describes how to create an instance in the ApsaraDB for MongoDB console. Prerequisites An account is obtained to log on to the ApsaraDB for MongoDB console. Create a replica set instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click Creat e Inst ance in the upper-left corner. On the
Creat e ApsaraDB f or MongoDB Inst ance page, configure the parameters. The following table describes the required parameters. Parameters for creating a replica set instance

| Section | Parameter | Description |
|---|---|---|
| Basic Set t ings | Organizat ion | Select an organization for the new instance. |
|   | Resource Set | Select a resource set for the new instance. |
| Region | Region | Select a region for the new instance. |
|   | Zone | Select a zone for the new instance |
|   | Dat abase Engine | Select a database engine for the new instance. In this case, you can select only MongoDB. |
|   | Engine Version | Select a database engine version for the new instance. Valid values: 3.0 3.4 4.0 4.2 |

| Specif icat Section ions | Parameter | Description |
|---|---|---|
|   | Node T ype | ApsaraDB for MongoDB supports the following options: Three-node Replica Set: uses dedicated memory and I/O resources but shares CPU and storage resources with other general-purpose instances on the same server. Dedicated Instance: uses dedicated CPU, memory, storage, and I/O resources to ensure long-term performance. In this case, an instance is not affected by other instances on the same server. Dedicated Host: exclusively uses all resources of a server. This is the top configuration of exclusive specifications. |
|   | Node Specif icat ions | Select a node specification for the new instance. For more information, see descriptions in the ApsaraDB for MongoDB console. |
|   | St orage Capacit y (GB) | The storage space of the instance, which contains the space for data, system files, log files, and transaction files. For more information, see Ins tance types in ApsaraDB for MongoDB Product Introduction. |
| Net work | Net work T ype | ApsaraDB for MongoDB supports the following options: Classic Net work: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. VPC: Virtual Private Cloud (VPC) is an isolated network environment built in Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Not e If you select the VPC network type, you must configure the VPC and vSwit ch parameters. |
|   | VPC | Select a VPC. Not e When Net work T ype is set to VPC, you must specify this parameter. |
|   | vSwit ch | Select a vSwitch. Not e When Net work T ype is set to VPC, you must specify this parameter. |
|   | Inst ance Name | Set the name of the new instance. The name must be 2 to 256 characters in length, The name must start with a letter, and can contain digits, letters, underscores ( ), and hyphens (-). _ |

| raDB for Mongo |   |   |
|---|---|---|
|   | DB User Guide·Instance |   |
| Section | Parameter | Description |
| Password Set t ings | Password Set t ing | Determine when to set the password for logging on to databases in the new instance. You can select Set Now to set the logon password immediately, or select Set af t er Purchase to set the logon password after you create the instance. For more information, see Reset the password for an ApsaraDB for MongoDB instance. |
|   | Logon Password | Set a password. The password must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The name can contain special characters. Special characters include ! # $ % ^ & * ( ) + = _ |
|   | Conf irm Password | Enter the password again. The password you enter here must be the same as that in New Password. |

3. Click Submit to create the instance.
Create a sharded cluster instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. Click Creat e Inst ance in the upper-left corner to go to the Creat e MongoDB Inst ance page.
Configure the parameters. The following table describes the required parameters. Parameters for creating a sharded cluster instance

| Section | Parameter | MNS logs |
|---|---|---|
| Basic Set t ings | Organizat ion | Select an organization for the new instance. |
|   | Resource Set | Select a resource set for the new instance. |
| Region | Region | Select a region for the new instance. |
|   | Zone | Select a zone for the new instance |
| Specif icat ions | Dat abase Engine | Select a database engine for the new instance. In this case, you can select only MongoDB. |
|   | Engine Version | Select a database engine version for the new instance. Valid values: 3.4 4.0 4.2 |

| Guide·Instance |   |   |
|---|---|---|
| Section | Parameter | MNS logs |
| Net work | Net work T ype | ApsaraDB for MongoDB supports the following options: Classic Net work: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. VPC: Virtual Private Cloud (VPC) is an isolated network environment built in Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Not e If you select the VPC network type, you must configure the VPC and vSwit ch parameters. |
|   | VPC | Select a VPC. Not e When Net work T ype is set to VPC, you must specify this parameter. |
|   | vSwit ch | Select a vSwitch. If no vSwitch exists, you can click Creat e vSwit ch to create a vSwitch. Not e When Net work T ype is set to VPC, you must specify this parameter. |
| Mongos Specif icat ions | Mongos Specif icat ions | The specifications of the mongos node. For more information, see descriptions in the ApsaraDB for MongoDB console. |
|   | Quant it y | The number of the mongos nodes. You can select 2 to 32 mongos nodes. |
| Shard Specif icat ions | Shard Specif icat ions | The specifications of the shard node. For more information, see descriptions in the ApsaraDB for MongoDB console. |
|   | St orage Capacit y (GB) | The storage space of the instance, which contains the space for data, system files, log files, and transaction files. For more information, see Ins tance types in ApsaraDB for MongoDB Product Introduction. |
|   | Quant it y | The number of the shard nodes. You can select 2 to 32 shard nodes. |
| Conf ig Server S if i t | Conf ig Server Specif icat ions | The specifications of Configserver nodes. It is fixed at 1 vCPU, 2 GiB memory and cannot be customized. |
|   | > Document Version: 2022092 |   |

| raDB for Mongo |   |   |
|---|---|---|
| Specif icat iSoencstion | Parameter | MNS logs |
|   | St orage Capacit y (GB) | The storage space of the Configserver node. It is fixed at 20 GB and cannot be customized. |
| Password Set t ings | Inst ance Name | Set the name of the new instance. The name must be 2 to 256 characters in length, and can contain digits, letters, underscores ( ), and _ hyphens (-). It must start with a letter. |
|   | Password Set t ing | Determine when to set the password for logging on to databases in the new instance. You can select Set Now to set the logon password immediately, or select Set af t er Purchase to set the logon password after you create the instance. For more information, see Reset the password for an ApsaraDB for MongoDB instance. |
|   | Logon Password | Set a password. The password must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The name can contain special characters. Special characters include ! # $ % ^ & * ( ) + = _ |
|   | Conf irm Password | Enter the password again. The password you enter here must be the same as that in New Password. |

4. Click Submit to create the instance.

### 4.2 View the details of an ApsaraDB for MongoDB instance

for MongoDB instance This topic describes how to view the details of an ApsaraDB for MongoDB instance, such as the basic information, internal network connection information, status, and configurations. This topic describes how to view the details of an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. Go to the instance details page. Either of the following methods can be used:
Find the instance and click its ID to go to the Basic Inf ormat ion page, where you can view the details of the instance. In the Operations column corresponding to the instance, choose
> Manage to go to the Basic

Inf ormat ion page, where you can view the details of the instance.

### 4.3 Restart an ApsaraDB for MongoDB instance

MongoDB instance You can manually restart an instance when the number of connections exceeds the threshold or any performance issue occurs on the instance. This topic describes how to restart an ApsaraDB for MongoDB instance. Prerequisites The instance is in the Running state. Context

> Not e When an ApsaraDB for MongoDB instance is restarted, all its connections are terminated. Plan your operations in advance before you restart an ApsaraDB for MongoDB instance. Proceed with caution.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the upper-right corner of the page, click Rest art Inst ance.

> Not e You can also choose
> > Rest art in the Act ions column corresponding to the
> instance.

5. In the Rest art Inst ance message, click OK.

### 4.4 Change the specifications of an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to change the specifications of an ApsaraDB for MongoDB instance. You can upgrade or downgrade an ApsaraDB for MongoDB instance to meet your business needs. Prerequisites The instance must be an ApsaraDB for MongoDB replica set instance.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. Click Change Conf igurat ion in the upper right corner of the Specification Information section to
go to the Modif y Inst ance page.

> Not e To go to the Modif y Inst ance page, you can also choose
> > Change
> Conf igurat ion in the Act ions column corresponding to the instance on the Replica Set Inst ances page.

4. On the Modif y Inst ance page, change the instance specifications.
You can change values of the following parameters: Node T ype Node Specif icat ions St orage Capacit y
5. Click Submit .

### 4.5 Change the name of an ApsaraDB for MongoDB instance

for MongoDB instance This topic describes how to change the name of an ApsaraDB for MongoDB instance for better management. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. Click Edit next to Inst ance Name.

> Not e
> The instance name must start with an English letter. It cannot start with http:// or https://.
> The instance name can contain letters, underscores (_), hyphens (-), and digits.
> The instance name must be 2 to 128 characters in length.

5. Click OK.

### 4.6 Reset the password for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to reset your password in the ApsaraDB for MongoDB console. Context

> Not ice We recommend that you change your password on a regular basis to ensure data security.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Account s.
5. Click Reset Password in the Actions column and configure the parameters in the Reset Password
panel. describes the parameters. Parameters for resetting a password

| Parameter | Description |
|---|---|
| New Password | Specify the new password of the account based on the following rules: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include !#$%^&*() += _ The password must be 8 to 32 characters in length. |
| Conf irm New Password | Enter the password again. The password you enter here must be the same as that in New Password. |

6. Click OK.

### 4.7 Switch node roles

You can switch the node roles of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console based on your business deployment. Typical scenario When an ECS instance and an ApsaraDB for MongoDB instance are in the same zone and connected over the internal network, the latency is minimal. If they are connected across different zones, the latency increases and the performance of ApsaraDB for MongoDB instances and your business will be affected. In this example, the ECS instance to which the application belongs is in Zone 2. If the primary node of the ApsaraDB for MongoDB instance is in Zone 1, the ECS instance needs to connect to the primary node across zones. To optimize the business deployment architecture, you can switch the roles of the primary and secondary nodes. In this example, you can change the role of the node in Zone 2 to primary and the role of the node in Zone 1 to secondary. Note that only the node roles are changed. ECS and ApsaraDB for MongoDB instances can be connected in the same zone without changing the actual zones and role IDs. Precautions Switching node roles will cause a transient disconnection of up to 30 seconds. Perform this operation during off-peak hours or ensure that your application has a reconnection mechanism. Switching node roles only changes the roles of nodes, but not the zones and role IDs of nodes. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Service Availabilit y.
5. Subsequent steps on the Service Availabilit y page vary depending on instance types.
Replica set instance a. Click Swit ch Role in the upper-right corner of the page. b. In the Swit ch Role dialog box that appears, select the nodes. c. Click OK. Sharded cluster instance

> Not e For sharded cluster instances, you can only manage the zone distribution of shard and Configserver nodes.

a. In the upper-right corner of the Zone Dist ribut ion f or Shards or Zone Dist ribut ion f or Conf igservers section, click Swit ch Role. b. In the Swit ch Role dialog box that appears, select the nodes. Click OK.

### 4.8 Migrate an ApsaraDB for MongoDB instance across zones in the same region

MongoDB instance across zones in the same region This topic describes how to migrate an ApsaraDB for MongoDB instance across zones in the same region. After instances are migrated to other zones, the attributes, specifications, and connection strings of the instances remain unchanged. Prerequisites The ApsaraDB for MongoDB instance is a replica set instance or sharded cluster instance that runs MongoDB 4.2 or later. Transparent data encryption (TDE) is not enabled for the ApsaraDB for MongoDB instance. The destination zone must be in the same region as the current zone of the instance. If the instance is in a VPC, make sure that a vSwitch is created in the destination zone before you start migration. For more information, see Create a VPC and Create a vSwitch in VPC User Guide. The instance does not have a public endpoint. If you have applied for a public endpoint, you must release it before migration. For more information, see Release a public connection string. Precautions If the instance is in a VPC, you cannot change the VPC when the instance is in the migration process. The time required varies based on factors such as the network conditions, task queue status, and data volume. We recommend that you migrate the instance across zones during off-peak hours. During the migration, a transient connection of 30 seconds occurs. Make sure that your application is configured to reconnect to the instance after it is disconnected. The virtual IP addresses (VIPs) of the instance, such as 172.16.88.60, are changed when the instance is migrated across zones. If your application uses the original VIP, the application cannot connect to the instance after the migration. Not e We recommend that you use a connection string URI to connect to the instance, which ensures high availability. For more information, see Overview of replica set instance connections or Overview of sharded cluster instance connections. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the Basic Inf ormat ion section, click Change Zone.
5. In the Migrat e Inst ance t o Ot her Zone panel, configure parameters based on the network type
of the instance. VPC

| Parameter | Description |
|---|---|
| Migrat e T o | Select the destination zone. |
| Select a VSwit ch | Select the destination vSwitch. |
| Migrat ion T ime | Select the time when you want to start the migration. Swit ch Immediat ely af t er Migrat ion: The migration immediately starts. When the instance status changes to Running, the migration is complete. Swit ch wit hin Maint enance Window: The migration starts during the specified period. You can click Edit next to Swit ch wit hin Maint enance Window to change the period. |

Classic network

| Parameter | Description |
|---|---|
| Migrat e T o | Select the destination zone. |
| Migrat ion T ime | Select the time when you want to start the migration. Swit ch Immediat ely af t er Migrat ion: The migration immediately starts. When the instance status changes to Running, the migration is complete. Swit ch wit hin Maint enance Window: The migration starts during the specified period. You can click Edit next to Swit ch wit hin Maint enance Window to change the period. |

6. Read the message that is displayed and select the check box next to the message.
7. Click OK.

### 4.9 Release an ApsaraDB for MongoDB instance

MongoDB instance This topic describes how to manually release an ApsaraDB for MongoDB instance to meet your business needs. This topic describes how to manually release an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the lower-right corner of the Basic Inf ormat ion section, click Release.

> Not e You can also go to the Replica Set Instances page, find the instance, click the
> icon in the Act ions column, and then choose Release.

5. In the Release Inst ance message, click OK.

> **Warning:** After you release an ApsaraDB for MongoDB instance, data in the instance can no longer be recovered. Proceed with caution.

### 4.10 Primary/secondary failover

#### 4.10.1 Trigger a primary/secondary failover for a replica set instance

replica set instance An ApsaraDB for MongoDB replica set instance consists of three nodes by default. ApsaraDB for MongoDB provides connection strings for you to connect to the primary node and a secondary node. The other secondary node is hidden as a backup to ensure high availability. If a node is faulty, the high availability system of ApsaraDB for MongoDB automatically triggers a primary/secondary failover to ensue the availability of the instance. You also can manually trigger a primary/secondary failover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills. Context After you log on to the ApsaraDB for MongoDB console or call the SwitchDBInstanceHA operation to trigger a primary/secondary failover for a replica set instance, ApsaraDB for MongoDB interchanges the roles of the primary and secondary nodes.

> Not e
> You can trigger a primary/secondary failover only for replica set and sharded cluster instances, but not for standalone instances due to their single-node architecture.
> Each time you trigger a primary/secondary failover for an instance, the instance may have a transient connection error of about 30 seconds. Ensure that your applications can automatically re-establish a connection.
> You can trigger a primary/secondary failover only for instances in the running state.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the Node List section, click Failover, as shown in the following figure.
4. In the dialog box that appears, click OK.
5. The instance status changes to HA Swit ching.The failover is successful when the instance status
changes back to Running. The failover operation is complete in about one minute. Then the instance returns to normal.

> Not e If you have connected to the connection string of the primary node for an instance, you are connecting to a secondary node after a failover and you have no write permissions on the instance. In this case, you must connect to the connection string of the new primary node and obtain read and write permissions. For more information, see Overview of replica set instance connections.

#### 4.10.2 Trigger a primary/secondary failover for a sharded cluster instance

sharded cluster instance Each shard or Configserver of a sharded cluster instance consists of three nodes by default. If a node is faulty, the high availability system of ApsaraDB for MongoDB automatically triggers a primary/secondary failover to ensure the availability of the shard. You can also manually trigger a primary/secondary failover for an ApsaraDB for MongoDB instance in scenarios such as routine disaster recovery drills. Precautions ApsaraDB for MongoDB provides connection strings for you to connect to the primary and secondary nodes. The hidden node is invisible to you and only used to ensure high availability. After you log on to the ApsaraDB for MongoDB console or call the SwitchDBInstanceHA operation to trigger a primary/secondary failover for a shard of a sharded cluster instance, ApsaraDB for MongoDB switches the roles of the primary and secondary nodes.

> Not e
> You can trigger a primary/secondary failover only for the shard or Configserve node in the running state.
> Each time you trigger a primary/secondary failover for an instance, the instance may have a transient connection error of about 30 seconds. We recommend that you perform this operation during off-peak hours and ensure that your applications can automatically re- establish a connection.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
in the Act ions column corresponding to the instance and select Manage.
4. In the Shard List or Conf igServer List section, find the node and choose
> Failover in the

Actions column.

> Not e You can trigger a primary/secondary failover separately for each shard node. The failover operation takes effect only for the current shard node and does not affect other shard nodes of the same sharded cluster instance.

5. In the Failover message, click OK.

> Not e The failover operation is complete in about one minute.

### 4.11 Monitoring

This topic describes the performance metrics provided by ApsaraDB for MongoDB to check the status of ApsaraDB for MongoDB instances. You can view these performance metrics in the ApsaraDB for MongoDB console. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Monit oring Inf o.
You can select a time range to query historical performance metrics. The following table describes metric details. Performance metrics

| Performance metric | Description | Monitoring frequency |
|---|---|---|
| CPU Utilization Percentage | cpu usage: the CPU utilization _ of the instance | Every 300 seconds |
| Memory Usage Percentage | mem usage: the memory _ usage of the instance | Every 300 seconds |

| Performance metric | Description | Monitoring frequency |
|---|---|---|
| IOPS Usage | The input/output operations per second (IOPS) of the instance. The following items are included: data iops: the IOPS of the _ data disk. log iops: the IOPS of the log _ disk. | Every 300 seconds |
| IOPS Usage Percentage | iops usage: the ratio of the _ IOPS used by the instance to the maximum IOPS allowed | Every 300 seconds |
| Disk Usage | The total disk space used by the instance. The following items are included: ins size: the total space _ used. data size: the space used on _ the data disk. log size: the space used on _ the log disk. | Every 300 seconds |
| Disk Usage Percentage | disk usage: the ratio of the _ total disk space used by the instance to the maximum disk space that can be used | Every 300 seconds |
| Operation QPS | The queries per second (QPS) of the instance. The following items are included: The number of insert operations. The number of query operations. The number of delete operations. The number of update operations. The number of getmore operations. The number of command operations. | Every 300 seconds |
| Connections | current conn: the number of _ current connections to the instance | Every 300 seconds |

| Guide·Instances |   | ApsaraDB for MongoD |
|---|---|---|
| Performance metric | Description | Monitoring frequency |
| Cursors | The number of cursors used by the instance. The following items are included: total open: the number of _ cursors that are opened. timed out: the number of _ cursors that timed out. | Every 300 seconds |
| Network Traffic | The network traffic of the instance. The following items are included: bytes in: the inbound _ network traffic. bytes out: the outbound _ network traffic. num requests: the number _ of requests that are processed. | Every 300 seconds |
| Global Lock Waiting Queues | The length of the queues that are waiting for global locks for the instance. The following items are included: gl cq total: the length of _ _ the queue that is waiting for both global read and write locks. gl cq readers: the length of _ _ the queue that is waiting for global read locks. gl cq writers: the length of _ _ the queue that is waiting for global write locks. | Every 300 seconds |

| Performance metric | Description | Monitoring frequency |
|---|---|---|
| WiredTiger | The cache metrics of the WiredTiger engine used by the instance. The following items are included: bytes read into cache: the _ _ _ amount of data that is read into the cache. bytes written from cache: _ _ _ the amount of data that is written from the cache to the disk. maximum bytes configured: _ _ the size of the maximum available disk space that is configured. | Every 300 seconds |
| Primary/Secondary Replication Latency | repl lag: the latency in data _ synchronization between the primary and secondary nodes of the instance | Every 300 seconds |

## 5 Backup and restoration

### 5.1 Configure automatic backup for an ApsaraDB for MongoDB instance

an ApsaraDB for MongoDB instance This topic describes how to configure automatic backup for an ApsaraDB for MongoDB instance. ApsaraDB for MongoDB automatically backs up data based on the backup policy you specify. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Backup and Recovery.
5. In the upper-left corner of the page, click Backup Set t ings. Configure the parameters in the
Backup Settings panel. The following table describes the parameters. Backup policy parameters

| Parameter | Description |
|---|---|
| Ret ent ion Days | The number of days for which you want to retain backup files. It can only be seven days. |
| Backup T ime | The hour at which you want to perform the backup task. |
| Day of Week | The backup cycle. You can select one or more days in a week. |

6. Click OK.

### 5.2 Manually back up an ApsaraDB for MongoDB instance

for MongoDB instance This topic describes how to manually back up an ApsaraDB for MongoDB instance. Backup methods Physical backup: This method backs up physical database files of an ApsaraDB for MongoDB instance. Compared with logical backup, physical backup provides faster data backup and recovery. Logical backup: The mongodump tool is used to store operation records of databases to a logical backup file. Then, data can be restore data by using the mongorestore tool.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the upper-right corner of the page, click Backup Inst ance.
5. In the dialog box that appears, set Backup Met hod and click OK.

### 5.3 Download a backup file

ApsaraDB for MongoDB allows you to download backup files that can be used to restore databases. This topic describes how to download a backup file in the ApsaraDB for MongoDB console. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Backup and Recovery.
5. On the page that appears, click
in the Act ions column corresponding to a backup file and select Download.
6. In the Download Backup dialog box, click Copy next to the download URL and then click OK.
7. Select an appropriate method to download the backup file based on your business environment.
You can run the wget command, or paste the copied download URL into the address bar of your browser and press the Enter key to download the backup file.

### 5.4 Restore data to the current ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to restore data to the current ApsaraDB for MongoDB instance. This helps minimize the data loss caused by incorrect operations. Prerequisites The instance is a replica set instance with three nodes. Background information The time required to restore data to your current instance varies depending on factors such as the data volume, task queue status, and network conditions. When the status of the instance changes to Running, the restoration is complete. If you restore data to your current instance, all existing data is overwritten and cannot be restored. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the left-side navigation pane, click Backup and Recovery.
4. On the Backup and Recovery page that appears, find the backup set and choose
> Dat a

Recovery in the Actions column.

> Not e If you have upgraded the database version, you cannot use the backup files of the earlier database version to restore data.

5. In the Roll Back Inst ance message, click OK.

> Not e The instance status becomes Rest oring f rom Backup after you click OK. You can click Ref resh in the upper-right corner of the Backup and Recovery page to update the instance status. The restoration is complete when the instance status changes to Running.

## 6 Database connections

### 6.1 Modify a public or internal endpoint of an ApsaraDB for MongoDB instance

endpoint of an ApsaraDB for MongoDB instance This topic describes how to modify a public or internal endpoint of an ApsaraDB for MongoDB instance in the ApsaraDB for MongoDB console. Limits

| Architecture | Limit |
|---|---|
| Replica set instance | You can modify the public and internal endpoints of both primary and secondary nodes. |
| Sharded cluster instance | You can modify only the public and internal endpoints of mongos nodes. |

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions.
5. In the upper-right corner of the Int ernal Connect ions or Public Connect ions section, click
Updat e Connect ion St ring.
6. In the panel that appears, enter a new endpoint.
Replica set instance Sharded cluster instance

> Not e
> You can modify only the prefix of the endpoint.
> The endpoint must start with a lowercase letter and end with a lowercase letter or a digit. It must be 8 to 64 characters in length and can contain lowercase letters, digits, and hyphens (-).

7. Click Submit .
What's next After you modify the public or internal endpoint, you must connect a client or an application to your ApsaraDB for MongoDB instance by using the new endpoint.

### 6.2 Use DMS to log on to an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance You can use DMS to connect to an ApsaraDB for MongoDB instance. Prerequisites The IP address whitelist is configured. For more information about how to configure the IP address whitelist, see Configure a whitelist for an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. Click Log On in the upper-right corner of the page.

> Not e For a sharded cluster instance, you must also select the Mongos node.

5. In the Login inst ance dialog box of the DMS console, check values of Dat abase t ype, Inst ance
Area, and Connect ion st ring address. If the information is correct, enter Dat abase account and Dat abase password, as shown in the following figure.

| Parameter | Description |
|---|---|
| Dat abase t ype | The engine of the database. By default, the engine of the database to be connected is displayed. |
| Inst ance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connect ion st ring address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Dat abase account | The account of the database to be connected. |
| Dat abase password | The password of the account used to connect to the database. |

6. Click Login.

> Not e If you want your web browser to remember the password, select Remember password before you click Login.

### 6.3 Use the mongo shell to connect to an ApsaraDB for MongoDB instance

to an ApsaraDB for MongoDB instance This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB instance. The mongo shell is a database management tool provided by ApsaraDB for MongoDB. You can install it on your client or in an Elastic Compute Service (ECS) instance. Prerequisites The version of the mongo shell is the same as your ApsaraDB for MongoDB instance. This ensures successful authentication. For more information about the installation procedure, see Install MongoDB. Choose the version in the upper-left corner of the page based on your client version. The IP address of your client is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.

> Not e
> Replica set instances: View the connection string or connection string URI of a node.
> Sharded cluster instances: View the connection string or connection string URI of a mongos node.

For more information about connection strings, see Overview of replica set instance connections or Overview of sharded cluster instance connections.
5. Connect to the ApsaraDB for MongoDB instance from your client or ECS instance where the mongo
shell is installed. Replica set instances: Connection string of a node During routine tests, you can directly connect to a primary or secondary node. Note that if the primary node fails, the system automatically switches to the secondary node, and the roles of connected nodes change. This affects the read and write operations of your application. Command syntax:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database>
```

> Not e
> <host>: the connection string of the primary or secondary node.
> <username>: the username used to log on to a database of the instance. The initial username is root .
> <database>: the name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.

Example:

```
mongo --host dds-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticati onDatabase admin
```

When `Enter password:` is displayed, enter the password of the database user and press the Enter key. If you forget the password of the root user, you can reset it. For more information, see Reset the password for an ApsaraDB for MongoDB instance.

> Not e The password characters are not displayed when you enter the password.

HA connection (recommended): You can use a connection string URI to connect to both the primary and secondary nodes of a replica set instance. This ensures that your application is always connected to the primary node and the read and write operations of your application are not affected even if the roles of the primary and secondary nodes are switched. Command syntax:

```
mongo "<ConnectionStringURI>"
```

> Not e
> The connection string URI must be enclosed in a pair of double quotation marks ("").
> <ConnectionStringURI>: the connection string URI of the instance.
> You must replace `****` in the connection string URI with the database password.

For more information about how to set a database password, see Reset the password for an ApsaraDB for MongoDB instance. Example:

```
mongo "mongodb://root:****@dds-**********.mongodb.rds.intra.env17e.shuguang.com:3717, dds-**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin?replicaSet=mgset-****
```

`*"` Sharded cluster instances: Connection string of a mongos node Command syntax:

```
mongo --host <mongos_host> -u <username> -p --authenticationDatabase <database>
```

> Not e
> <mongos_host>: the connection string of a mongos node in the sharded cluster instance.
> <username>: the username used to log on to a database of the instance. The initial username is root .
> <database>: the name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.

Example:

```
mongo --host s-bp**********.mongodb.rds.aliyuncs.com:3717 -u root -p --authentication Database admin
```

HA connection (recommended): You can use a connection string URI to connect to a database. If one mongos node fails, another mongos node takes over business to ensure the high availability of the connection. Command syntax:

```
mongo "<ConnectionStringURI>"
```

> Not e
> The connection string URI must be enclosed in a pair of double quotation marks ("").
> <ConnectionStringURI>: the connect ion st ring URI of the instance.
> You must replace `****` in the connect ion st ring URI with the database

password. For more information about how to set a database password, see Reset the password for an ApsaraDB for MongoDB instance. Example:

```
mongo "mongodb://root:****@s-**********.mongodb.rds.intra.env17e.shuguang.com:3717,s-
**********.mongodb.rds.intra.env17e.shuguang.com:3717/admin"
```

### 6.4 Apply for a public endpoint for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to apply for a public endpoint for an ApsaraDB for MongoDB instance when you want to connect to this instance over the Internet. Context The following table describes the Virtual Private Cloud (VPC) and classic network endpoints supported by ApsaraDB for MongoDB.

| Type | Description |
|---|---|
| VPC endpoint | A VPC is an isolated network with higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides endpoints on a VPC. |
| Classic network endpoint | Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by using security groups or whitelists. |
| Public endpoint | Security risks may arise if you connect to an ApsaraDB for MongoDB instance over the Internet. Therefore, ApsaraDB for MongoDB does not provide public endpoints. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Alibaba Cloud (such as an on-premises device), you must apply for a public endpoint. |

Apply for a public endpoint for a replica set instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the left-side navigation pane, click Dat abase Connect ions.
4. In the upper-right corner of the Public Connect ions section, click Apply f or Public Connect ion
St ring.
5. In the Apply f or Public Connect ion St ring message, click OK.

> Not e If you want to connect to an ApsaraDB for MongoDB instance by using a public endpoint, you must add the public IP address of your client to a whitelist of this instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance.

After the application is complete, the replica set instance generates new endpoints for both the primary and secondary nodes and the corresponding connection string URI. For more information, see Overview of replica set instance connections. Apply for a public endpoint for a sharded cluster instance
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions.
5. In the upper-right corner of the Public Connect ions section, click Apply f or Public Connect ion
St ring.
6. In the panel that appears, specify Node T ype and Node ID, and click OK.

| Paramet er | Value | Description |
|---|---|---|
| Node T ype | Mongos | The mongos node. You can apply for public endpoints only for mongos nodes. Your applications are connected to mongos nodes in most cases. |
| Node ID | The ID of the component for which you want to apply for a public endpoint. | None |

> Not e You can repeat this step to apply for public endpoints for other mongos nodes as your needs change. You can apply for a new public endpoint only after the current one is created.

References To ensure data security, we recommend that you release a public endpoint if you no longer need it. For more information, see Release a public connection string. Before you connect to a replica set instance over the Internet, we recommend that you enable SSL encryption. For more information, see Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode.

### 6.5 Release a public endpoint

To ensure data security, you can release a public endpoint that is no longer needed in the console. Precautions You can release one or more public endpoints of the mongos nodes for a sharded cluster instance. After the public endpoint is released for an instance or node, you cannot connect to the instance or node by using the original public endpoint. After the public endpoint is released, we recommend that you delete the corresponding public IP address from the whitelist to ensure data security. For more information, see Configure a whitelist. Release a public endpoint for a replica set instance

> Not e After the public endpoint of a replica set instance is released, the public endpoints of the primary and secondary nodes are released.

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the left-side navigation pane, click Dat abase Connect ions.
4. In the upper-right corner of the Public Connect ions section, click Release Public Connect ion
St ring.
5. In the message that appears, click OK.
Release a public endpoint for a sharded cluster instance You can release one or more public endpoints of the mongos, shard, and Configserver nodes for a sharded cluster instance.

> Not e After the public endpoint of a shard or Configserver node is released, the public endpoints of the primary and secondary nodes are released.

1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions.
5. In the Public Connect ions section, find the mongos, shard, or Configserver node for which you
want to release the public endpoint.
6. In the Act ions column corresponding to the node, click Release.

> Not e You can repeat this step to release the public endpoints of other nodes as your needs change. To release the public endpoint of the next node, you must wait until the public endpoint of the current node is released or the status of the current node becomes Running.

7. In the message that appears, click OK.

### 6.6 Overview of replica set instance connections

connections ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to the primary or secondary node, and use a connection string URI to connect to both of them. For high availability, we recommend that you use connection string URIs to connect your application to both primary and secondary nodes. This topic provides an overview of replica set instance connections. Prerequisites A whitelist is configured for the instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. View connection strings
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. On the Replica Set Inst ances page, click the ID of an instance, or click
in the Act ions column corresponding to the instance and select Manage.
3. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.
Description of connection strings

| Item | Description |
|---|---|
| Connection type | Internal Connections - Classic Network: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. Internal Connections - VPC: A virtual private cloud (VPC) is an isolated network with higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints. |
| Role | Primary: the primary node in the replica set instance. If you connect to this node, you can perform read and write operations on the databases of the replica set instance. Secondary: the secondary node in the replica set instance. If you connect to this node, you can perform only read operations on the databases of the replica set instance. Connection String URI: ApsaraDB for MongoDB allows you to use a connection string URI to connect to a replica set instance to achieve load balancing and high availability. |
| Connection string | The connection string of a primary or secondary node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port used to connect to the instance. |

| Item | Description |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to a database of the replica set instance. You must separate them with a colon (:). hostX:portX: the endpoint and port of a node in the replica set instance. /database: the name of the database corresponding to the username if authentication is enabled. ?options: additional connection options. Not e If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. This way, when a node fails, the read and write operations of your application are not affected as a result of the failover. |

Related information Connect to a replica set instance by using the mongo shell

### 6.7 Overview of sharded cluster instance connections

instance connections ApsaraDB for MongoDB supports both connection strings and connection string URIs. You can use a connection string to connect to a single mongos node, and use a connection string URI to connect to multiple mongos nodes. For high availability, we recommend that you use connection string URIs to connect your application to multiple mongos nodes. This topic provides an overview of sharded cluster instance connections. View connection strings
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, click Dat abase Connect ions to view connection strings.
Description of connection strings

| Item | Description |
|---|---|
| Connection type | Internal Connections - Classic Network: Cloud services on the classic network are not isolated. Unauthorized access can be blocked only by security groups or whitelists. Internal Connections - VPC: A virtual private cloud (VPC) is an isolated network with higher security and performance than the classic network. By default, ApsaraDB for MongoDB provides VPC endpoints. Public Connections: Security risks may arise if you connect to a sharded cluster instance over the Internet. Therefore, ApsaraDB for MongoDB does not provide public endpoints. If you want to connect to an ApsaraDB for MongoDB instance from a device outside of Alibaba Cloud (such as an on-premises device), you must apply for a public endpoint. For more information, see Apply for a public endpoint for an ApsaraDB for MongoDB instance. |
| Mongos ID | The connection string of a mongos node is in the following format: <host>:<port> <host>: the endpoint used to connect to the instance. <port>: the port used to connect to the instance. Not e During routine tests, you can use a connection string to directly connect to a mongos node. |

| Item | Description |
|---|---|
| Connection string URI | A connection string URI is in the following format: mongodb://[username:password@]host1[:port1][,host2[:port2],... [,hostN[:portN]]][/[database][?options]] mongodb://: the prefix of a connection string URI. username:password@: the username and password used to log on to a database of the sharded cluster instance. You must separate them with a colon (:). hostX:portX: the endpoint and port of a mongos node in the sharded cluster instance. /database: the name of the database corresponding to the username if authentication is enabled. ?options: additional connection options. Not e If your application is in a production environment, we recommend that you use a connection string URI to connect to the instance. Then, your client can automatically distribute your requests to multiple mongos nodes to balance loads. If a mongos node fails, your client automatically redirects requests to other mongos nodes in the normal state. |

Log on to a database of an ApsaraDB for MongoDB instance
1. Obtain the connection string and the following information:
The username used to log on to the database. The initial username is root. The password of the database user. If you forget the password of the root user, you can reset it. For more information, see Reset the password for an ApsaraDB for MongoDB instance. The name of the database corresponding to the username if authentication is enabled. If the database username is root, enter admin as the database name.
2. Log on to the database.
Use DMS to log on to a replica set instance of ApsaraDB for MongoDB Connect to a replica set instance by using the mongo shell

## 7 Data security

### 7.1 Configure a whitelist for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to configure a whitelist for an ApsaraDB for MongoDB instance. Before you use an ApsaraDB for MongoDB instance, you must add the IP addresses or Classless Inter-Domain Routing (CIDR) blocks that you use for database access to a whitelist of this instance. This improves database security and stability. Proper configuration of whitelists can enhance access security of ApsaraDB for MongoDB. We recommend that you maintain the whitelists on a regular basis. Context The system creates a default whitelist for each instance. This whitelist can be modified or cleared, but it cannot be deleted. After an ApsaraDB for MongoDB instance is created, the system automatically adds the IP address 127.0.0.1 to the def ault whitelist of this instance. The IP address 0.0.0.0/0 indicates that all IP addresses are allowed to access this instance. You must add the IP addresses or CIDR blocks that you allow to access this ApsaraDB for MongoDB instance. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > Whit elist Set t ings.
5. You can manually configure a whitelist or import ECS Internal IP addresses to the whitelist.
Manually modif y a whit elist i. Find the whitelist you want to modify and choose
> Manually Modif y in the Act ions

column. ii. Enter IP addresses or CIDR blocks.

> Not e
> Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. Supported formats are IP addresses such as 0.0.0.0/0 and 10.23.12.24, or CIDR blocks such as 10.23.12.24/24. /24 indicates the length of the IP address prefix in the CIDR block. An IP address prefix can contain 1 to 32 bits.
> If the IP whitelist is empty or only contains `0.0.0.0/0` , all devices are granted
> access. This is risky for your ApsaraDB for MongoDB instance. We recommend that you add only the IP addresses or CIDR blocks of your own web servers to the whitelist.

iii. Click OK. Load IP addresses of ECS inst ances i. Find the whitelist, and choose
> Import ECS Int ranet IP in the Act ions column.

ii. From the displayed internal IP addresses of ECS instances that belong to the current account, select the IP addresses and click to add them to the whitelist. iii. Click OK.

### 7.2 Create or delete a whitelist

This topic describes how to create or delete whitelists that consist of the IP addresses allowed to access specific databases. Context If your business involves multiple applications and you need to add a whitelist for each of them, you can sort the IP addresses into different whitelists. Create a whitelist
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > Whit elist Set t ings.
5. Click Creat e Whit elist in the upper-left corner of the page.
6. In the panel that appears, set Group Name and IP Whit e List and click OK.

> Not e
> Group Name: The name must be 2 to 32 characters in length and can contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter and end with a lowercase letter or digit.
> IP Whit e List :
> Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to a whitelist. A whitelist can include IP addresses such as 0.0.0.0/0 and 10.23.12.24, or CIDR blocks such as 10.23.12.24/24. /24 indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
> If the whitelist is empty or contains only 0.0.0.0/0, all devices are granted access. This poses risks to your ApsaraDB for MongoDB instance. We recommend that you add only the IP addresses or CIDR blocks of your own web servers to the whitelist.

Delete a whitelist
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > Whit elist Set t ings.
5. Find the whitelist that you want to delete and choose
> Delet e Whit elist Group in the

Act ions column.

> Not e You cannot delete the def ault whitelist.

6. In the Delete Whitelist Group message, click OK.

### 7.3 Audit logs

This topic describes audit logs provided in the ApsaraDB for MongoDB console. You can query the statement execution logs, operations logs, and error logs of an ApsaraDB for MongoDB instance to locate and analyze faults. Context The audit log feature records all operations that a client performs on a connected database. This feature provides references for you to perform fault analysis, behavior analysis, and security auditing because you can obtain the operation execution details from the audit logs. Audit logs are essential in the regulatory operations of Finance Cloud and other core business scenarios.

> Not e Audit logs are stored for seven days, after which they are deleted.

Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > Audit Logs.
5. Click Enable Audit Log in the upper-left corner. In the Enable Audit message, click OK.
Result On the Audit Log page, specify the time range, database name, database user, and keyword to query audit logs. You can also perform the following operations: Export File: exports an audit log file. File List : displays a list of audit logs. Disable Audit Log: stops the collection of information on database operations and deletes the saved audit logs.

### 7.4 Configure SSL encryption for an ApsaraDB for MongoDB instance

ApsaraDB for MongoDB instance This topic describes how to enhance link security by enabling Secure Sockets Layer (SSL) encryption and installing SSL CA certificates on your application services. The SSL encryption feature encrypts network connections at the transport layer to improve data security and ensure data integrity during communication. Prerequisites The instance is a replica set instance. The MongoDB version of the instance is 3.4, 4.0, or 4.2. Notes When you enable or disable SSL encryption or update SSL CA certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your application is configured to reconnect to the instance after it is disconnected.

> Not e When an instance is restarted, all its nodes are restarted in turn and each node has a transient connection error of about 30 seconds. If the instance contains more than 10,000 collections, the transient connection error last longer.

Precautions You can download SSL CA certificate files only from the ApsaraDB for MongoDB console. After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary. For example, you can enable SSL encryption when you connect to an ApsaraDB for MongoDB instance over the Internet.

> Not e Internal network connections are more secure than Internet connections and do not need SSL encryption.

After you enable SSL encryption for an instance, both SSL and non-SSL connections are supported. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > SSL.
5. Perform one of the following operations.

> Not e When you enable or disable SSL encryption or update SSL CA certificates for an instance, the instance is restarted. Plan your operations in advance and make sure that your applications can automatically re-establish a connection.

| Operation | Prerequisite | Procedure |
|---|---|---|
| Enable SSL encryption | The SSL encryption status is Disabled. | Turn on SSL St at us. In the message that appears, click OK. |
| Update an SSL CA certificate | The SSL encryption status is Enabled. | Click Updat e Cert if icat e. In the message that appears, click OK. |
| Download an SSL CA certificate file | The SSL encryption status is Enabled. | Click Download Cert if icat e to download an SSL CA certificate file to your computer. |
| Disable SSL encryption | The SSL encryption status is Enabled. | Turn off SSL St at us. In the message that appears, click OK. |

### 7.5 Configure TDE for an ApsaraDB for MongoDB instance

for MongoDB instance This topic describes how to configure Transparent Data Encryption (TDE) for an ApsaraDB for MongoDB instance. Before data files are written to disks, TDE encrypts the data files. When data files are loaded from disks to the memory, TDE decrypts the data files. TDE does not increase the sizes of data files. When you use TDE, you do not need to modify your application that uses the ApsaraDB for MongoDB instance. To enhance data security, you can enable the TDE feature for an instance in the ApsaraDB for MongoDB console. Prerequisites The MongoDB version of the instance is 4.0 or 4.2.

> Not e Before you enable TDE, you can create a MongoDB 4.0 or 4.2 instance to test the compatibility between your application and the database version. You can release the instance after the test is complete.

Notes When you enable TDE, your instance is restarted, and your application is disconnected from the instance. We recommend that you enable TDE during off-peak hours and make sure that your application can reconnect to the instance after it is disconnected. TDE increases the CPU utilization of your instance. Precautions You cannot disable TDE after it is enabled. You can enable TDE for an instance and disable encryption for a collection.

> Not e In special business scenarios, you can choose not to encrypt a collection when you create it. For more information, see Disable encryption for a specified collection.

After you enable TDE, only new collections are encrypted. Existing collections are not encrypted. Key Management Service (KMS) generates and manages the keys used by TDE. ApsaraDB for MongoDB does not provide keys or certificates required for encryption. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose Dat a Securit y > T DE.
5. Turn on T DE St at us to enable TDE.
6. In the Rest art Inst ance dialog box, click OK.
The instance status changes to Modif ying T DE. After the status changes to Running, TDE is enabled. Disable encryption for a specified collection After you enable TDE, all new collections are encrypted. When you create a collection, you can perform the following steps to disable encryption for the collection:
1. Connect to a replica set instance by using the mongo shell. For more information, see Connect to a
replica set instance by using the mongo shell.
2. Run the following command to create a collection and disable the encryption feature:

```
db.createCollection("<collection_name>",{ storageEngine: { wiredTiger: { configString: "encryption=(name=none)" } } })
```

> Not e <collection_name>: the name of the collection.

Example:

```
db.createCollection("customer",{ storageEngine: { wiredTiger: { configString: "encrypti on=(name=none)" } } })
```

### 7.6 Use the mongo shell to connect to an ApsaraDB for MongoDB database in SSL encryption mode

to an ApsaraDB for MongoDB database in SSL encryption mode This topic describes how to use the mongo shell to connect to an ApsaraDB for MongoDB database in Secure Sockets Layer (SSL) encryption mode. SSL encryption can encrypt network connections at the transport layer to improve data security and ensure data integrity. Prerequisites The instance is a replica set instance, and the database version of the instance is 3.4, 4.0, or 4.2. The mongo shell of the required version is installed on the local server or ECS instance from which you want to connect to the database. For more information about the installation procedure, visit MongoDB official documentation. SSL encryption is enabled for the instance. For more information, see Configure SSL encryption. The IP address of the local server or the ECS instance is added to a whitelist of the ApsaraDB for MongoDB instance. For more information, see Configure a whitelist for an ApsaraDB for MongoDB instance. Precautions After you enable SSL encryption for an instance, the CPU utilization of the instance is significantly increased. We recommend that you enable SSL encryption only when necessary. Procedure A local server with a Linux operating system is used in the following example.
1. Download an SSL CA certificate package. For more information, see Configure SSL encryption.
2. Decompress the package and upload the certificate files to the local server or the ECS instance
where the mongo shell is installed.

> Not e In this example, the .pem file is uploaded to the /root/sslcafile/ directory of the local server.

3. On the local server or the ECS instance, run the following command to connect to a database of
the ApsaraDB for MongoDB instance:

```
mongo --host <host> -u <username> -p --authenticationDatabase <database> --ssl --sslCAF ile <sslCAFile_path> --sslAllowInvalidHostnames
```

> Not e
> <host>: the connection string of the primary or secondary node for a replica set instance or of mongos node for a sharded cluster instance. For more information, see Overview of replica set instance connections or Overview of sharded cluster instance connections. If you want to connect to a database of the ApsaraDB for MongoDB instance over an internal network, make sure that the ApsaraDB for MongoDB instance has the same network type as the ECS instance. If the network type is VPC, make sure that the two instances are in the same VPC.
> <username>: the username you use to log on to a database of the ApsaraDB for MongoDB instance. The default username is root.
> <database>: the name of database corresponding to the username if authentication is enabled. If the database username is root, enter admin.
> <sslCAFile_path>: the path of the SSL CA certificate files.

Example:

```
mongo --host dds-bpxxxxxxxx-pub.mongodb.rds.aliyuncs.com:3717 -u root -p --authenticati onDatabase admin --ssl --sslCAFile /root/sslcafile/ApsaraDB-CA-Chain.pem --sslAllowInv alidHostnames
```

4. When `Enter password:` is displayed, enter the password of the database user and press Enter.

> Not e
> The password characters are not displayed when you enter the password.

If you forget the password of the root user, you can reset it. For more information, see Reset the password for an ApsaraDB for MongoDB instance.

## 8 Zone-disaster recovery

### 8.1 Create a dual-zone replica set instance

instance This topic describes how to create a dual-zone replica set instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the reliability and availability of your replica set instance. This solution deploys the three nodes of a replica set instance across two different zones within one region. The components in these zones exchange data over an internal network. When one of the two zones becomes unavailable due to unexpected events such as a power or network failure, the high-availability (HA) system switches services over to another zone. Deployment policies The primary, secondary, and hidden nodes of a replica set instance are deployed in two different zones within one region. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances.
3. On the Replica Set Inst ances page, click Creat e Inst ance.
4. On the Creat e ApsaraDB f or MongoDB Inst ance page, configure parameters.

> Not e
> For the Zone parameter, you must select dual zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region.

For more information, see Create a replica set instance.
5. Click Submit .

### 8.2 Create a dual-zone sharded cluster instance

cluster instance This topic describes how to create a dual-zone sharded cluster instance. ApsaraDB for MongoDB provides a zone-disaster recovery solution to ensure the reliability and availability of your sharded cluster instance. This solution deploys the components of a sharded cluster instance across two different zones within one region. The components in these zones exchange data over an internal network. When one zone becomes unavailable due to unexpected events such as a power or network failure, the high availability (HA) system automatically switches business over to the other zone. Deployment policies The components of a sharded cluster instance are deployed across two different zones within one region. Mongos nodes are evenly deployed across all data centers. At least two mongos nodes are deployed at a time, with each in one zone. Each new mongos node added later is deployed to one of the zones in turn. The primary, secondary, and hidden nodes in each shard node are not deployed to the two zones in sequence. The deployment of these nodes may change when manual switchover or HA failover between primary and secondary nodes is triggered. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Sharded Clust er Inst ances.
3. On the Sharded Clust er Inst ances page, click Creat e Inst ance.
4. On the Creat e ApsaraDB f or MongoDB Sharded Clust er Inst ance page, configure parameters.

> Not e
> For the Zone parameter, you must select dual zones, such as the amtest17001-a and amtest17001-b zones of the cn-qingdao-env11e-MAZ1 region.

For more information, see Create a sharded cluster instance.
5. Click Submit .

## 9 CloudDBA

### 9.1 Performance trends

This topic describes how to view performance trends in specific ranges, compare performance trends, and customize charts to view performance trends on your ApsaraDB for MongoDB instances. Go to the Performance page
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose CloudDBA > Perf ormance T rends.

> Not e For more information about performance trends, see relevant topics in Database Autonomy Service (DAS) User Guide.

### 9.2 Real-time performance

This topic describes how to view real-time monitoring statistics of your ApsaraDB for MongoDB instances, such as read/write latency, queries per second (QPS), operations, connections, and network traffic. Prerequisites Database Autonomy Service (DAS) is authorized to manage ApsaraDB for MongoDB instances. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose CloudDBA > Real-t ime Perf ormance.
Overview of the Real-time Monitoring page On the Real-time Monitoring page, you can click the Real-time Charts or Mongostat tab to view monitoring statistics. When you refresh the Real-t ime Monit oring page, the information on the Realtime Charts and Mongostat tabs is refreshed, and Available Ref reshes is reset in the upper-right corner. Real-time charts By default, content on the Real-t ime Chart s tab is displayed when you go to the Real-time Monitoring page. Line charts on the tab are refreshed every 5 seconds.

> Not e For more information about performance metrics, click the
> icon above each chart.

mongostat Click the Mongost at tab. On the tab, you can view Mongostat command outputs. A new line of monitoring data is added every 5 seconds. The tab can contain up to 999 lines of information. Not e For more information about Mongostat command outputs, see MongoDB official documentation.

### 9.3 Instance sessions

This topic describes how to view real-time monitoring statistics of your ApsaraDB for MongoDB instances, such as read/write latency, queries per second (QPS), operations, connections, and network traffic. Prerequisites Database Autonomy Service (DAS) is authorized to manage your ApsaraDB for MongoDB instances. View instance sessions
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose CloudDBA > Sessions.

> Not e
> If you turn on Aut o Ref resh, the system updates session data on the page every 5 seconds.
> By default, the system displays only active sessions. You can turn on Display All to view both active and inactive sessions.
> In the Session St at ist ics section, you can view information about sessions in the Overview, St at ist ics by Client , and St at ist ics by Namespace charts.

Terminate instance sessions

> **Warning:** To avoid unexpected results, we recommend that you do not terminate system- level sessions.

1. In the Inst ance Sessions section, select the sessions that you want to terminate and click Kill
Select ed.
2. In the message that appears, click OK.

### 9.4 Storage analysis

This topic describes how to view information about the storage analysis feature, including St orage, Except ions, St orage t rend, T ablespaces, and Dat a space. The information helps you identify and resolve exceptions in the database storage to ensure database stability. Prerequisites Database Autonomy Service (DAS) is authorized to manage ApsaraDB for MongoDB instances.
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
click in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose CloudDBA > St orage analysis.
5. In the upper-right corner, click Re-analyze. Then, wait until the analysis is complete.
6. On the St orage Overview or Dat a Space tab, view the analysis results.
For more information about Storage Overview, see Storage Overview. For more information about Data Space, see Data Space. Storage Overview On the Storage Overview tab, you can view information in the St orage, Except ions, St orage T rend, and T ablespaces sections. St orage

| Item | Description |
|---|---|
| Except ion | The number of detected storage exceptions. ApsaraDB for MongoDB can detect the following types of exceptions: Over 90% of the storage capacity is used. The total physical storage can become unavailable in seven days. The number of indexes in a collection exceeds 10. |

| Item | Description |
|---|---|
| Avg Daily Increase in Last Week | The average daily increase of storage usage over the last seven days. Formula: (Storage usage at the time of collection - Storage usage seven days ago)/7. Not e The increase speed is the average value during the seven days before the collection time. This parameter is used only as a reference for scenarios in which the traffic remains stable. Abrupt storage changes caused by batch imports, deletion of historical data, instance migration, or instance re-creation affect the accuracy of the data. |
| Available Days of St orage | The estimated number of days during which storage space is available. Formula: Size of available storage space/Average daily increase over the last week. Not e 90+ indicates that the storage space is sufficient for more than 90 days of usage. This parameter is used only as a reference for scenarios in which the traffic remains stable. Abrupt storage changes caused by batch imports, deletion of historical data, instance migration, or instance re-creation affect the accuracy of the data. |
| Used St orage | The size of used storage space in contrast to the total size of storage space. |

Except ions Information about detected storage exceptions. You can resolve the exceptions based on the information in this section. St orage T rend Changes in storage usage over the last week, such as changes in the used st orage, dat a space, and log space. T ablespaces Information about all tables, such as the database name, storage engine, and collection storage.

> Not e You can click the name of a collection to view its indexes.

Data Space The Data Space tab shows the total storage capacity and tablespace information of each database.

> Not e
> You can click the name of a data space to view its tablespace information.
> You can click the name of a collection to view its indexes.

### 9.5 Slow query logs

This topic describes how to view slow query logs of ApsaraDB for MongoDB instances. You can identify, analyze, diagnose, and track slow query logs to create indexes. This improves the utilization of the instance resources. Procedure
1. Log on to the ApsaraDB for MongoDB console. For more information about how to log on to the
console, see Log on to the ApsaraDB for MongoDB console.
2. In the left-side navigation pane, click Replica Set Inst ances or Sharded Clust er Inst ances.
3. On the Replica Set Inst ances or Sharded Clust er Inst ances page, click the ID of an instance, or
in the Act ions column corresponding to the instance and select Manage.
4. In the left-side navigation pane, choose CloudDBA > Slow Query Logs.

> Not e By default, slow query logs generated in the past 15 minutes are displayed in the trend chart. You can specify the time range and click Search to view slow query logs in specific periods of time. The maximum time range is one day.

5. View details of slow query logs by using one of the following methods:
Method 1: i. Click the Slow Log Det ails tab in the lower part of the page. ii. On the Slow Log Det ails tab, select the database that you want to query.

> Not e If the request content of the database is hidden, you can move the pointer over the corresponding content in the Request Cont ent column and view the complete content.

Method 2: i. In the Slow Log Trend chart, click a point in time. Then, you can view the statistics of the slow query logs generated at the point in time on the Slow Log St at ist ics tab. ii. On the Slow Log St at ist ics tab, click Sample in the Act ions column corresponding to a slow query log. In the Slow Log Sample dialog box, you can view details of the slow query log.

> Not e If the request content of the database is hidden, you can move the pointer over the corresponding content in the Request Cont ent column and view the complete content.

Export slow query logs You can click Export Slow Log on the Slow Log St at ist ics tab to save the slow query log information to your computer.
