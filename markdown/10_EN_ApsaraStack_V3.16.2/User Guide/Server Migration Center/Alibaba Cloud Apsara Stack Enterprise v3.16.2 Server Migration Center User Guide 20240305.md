---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center User Guide"
product_version: "V3.16.2"
doc_version: "20240305"
pdf_pages: 37
source_pdf: "4048e1e71bea4567_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center User Guide 20240305.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%81%E7%A7%BB%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Server%20Migration%20Center%20User%20Guide%2020240305.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Migration Center User Guide

## Table of Contents

- 1 What is SMC?
- 2 Getting started
  - 2.1 Migration process
  - 2.2 Log on to the SMC console
  - 2.3 Before you begin
    - 2.3.1 Prepare a source server
    - 2.3.2 Preparations in the Apsara Uni-manager Operations Console
  - 2.4 Step 1: Import the information about a migration source
  - 2.5 Step 2: Create and start a migration job
- 3 Use the Windows GUI version of the SMC client
- 4 Migrate incremental data from a source server
- 5 Migrate a server to an ECS instance

## 1 What is SMC?

Server Migration Center (SMC) is a server migration platform developed by Alibaba Cloud. SMC allows you to migrate one or more source servers to Apsara Stack. The source servers are called migration sources in SMC. The source servers can be servers of a variety of types, such as servers in data centers, VMs, and hosts on other cloud platforms. The core component of SMC is the SMC client. If you want to migrate a source server to Apsara Stack, configure and run the SMC client on the source server. The following figure shows how the SMC client works.

## 2 Getting started

### 2.1 Migration process

Server Migration Center (SMC) allows you to migrate one or more servers at a time to Apsara Stack. Migration sources or source servers can be servers in self-managed data centers, VMs, third-party cloud servers, or servers of other types. This topic describes the migration process of SMC. When you use SMC to migrate a source server to Apsara Stack, you must complete relevant settings on the source server and in the SMC console. You must run the SMC client on the source server to import the information about the source server to the SMC console, and then create and run a migration job in the SMC console. Perform the following steps:
1. Prepare for the migration.
2. Import the information about a migration source.
i. Download and decompress an SMC client package. ii. Run the SMC client to import the information about the migration source.
3. Create and start a migration job.
i. Create a migration job. ii. Start the migration job. iii. View the migration status and perform other operations. Before you use SMC, take note of the following items: Do not perform operations on the intermediate instance. During each migration, SMC creates a temporary intermediate instance named No_Delete_SMC_Transition_Instance in your organization. During the migration, do not stop, restart, or release the intermediate instance. Otherwise, the migration fails. After the migration is complete, SMC automatically releases the intermediate instance. The following information describes the data directories that are migrated: Windows servers: Only the data on the C drive is migrated as a partition of the system disk. Directories that are mounted to the C drive are also included. If you want to migrate data from other partitions such as the D drive, you must select and configure the data disk when you create a migration job. Linux servers: The data in all subdirectories in the root directory, including shared subdirectories in the root directory, is migrated as a partition of the system disk. If you want to migrate the data in other directories such as /disk1, you must select and configure the data disk when you create a migration job.

### 2.2 Log on to the SMC console

This topic describes how to log on to the Server Migration Center SMC console.

**Prerequisites**

You have obtained the endpoint, username, and password of the one-stop cloud migration service center console from the deployment personnel or administrator. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Cloud Migration Center
console and press the Enter key.
2. Enter your username and password.
Obtain the username and password for logging on to the console from the administrator.

> **Note:** When you log on to the one-stop cloud migration service center console for the first time, you need to change the password of the logon username. Follow the instructions to complete the password change. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log on**.
4. In the left-side navigation pane, click **Tool Center > Server Migration Center**.

### 2.3 Before you begin

#### 2.3.1 Prepare a source server

This topic describes the preparations that you must make on a source server before you migrate the source server to Apsara Stack. Before the migration, you must make the following preparations on the source server: Make sure that the system time of the source server is the same as the actual time. Otherwise, the IllegalTimestamp error is reported during the migration. Make sure that the source server can access the endpoint of the Server Migration Center (SMC) service. To obtain the endpoint of SMC, perform the following steps: i. Log on to the SMC console. ii. In the upper-right corner, click **SMC Endpoint Address** to copy the endpoint of SMC.

#### 2.3.2 Preparations in the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to create a Resource Access Management (RAM) role and a RAM user and grant permissions to the RAM role and RAM user, obtain the AccessKey pair of the organization, and create a Virtual Private Cloud (VPC) and a vSwitch before you migrate the source server to Alibaba Cloud Apsara Stack.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console, username, and password that are used to log on to the console are obtained from the deployment personnel or an administrator. A web browser is available. We recommend that you use Google Chrome.

**Step 1: Log on to the Apsara Uni-manager Operations Console**

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters such as the exclamation point (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%).

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **"Manage MFA"** section in **Apsara Uni-manager** **Management Console User Guide**.

**Step 2: Create a RAM role and a RAM user and grant**

**permissions to the RAM role and RAM user**

Before you migrate the source server, make sure that the service-linked role of Server Migration Center (SMC) is added to your organization and the RAM user that you use to log on to the console is granted the required permissions. To create a RAM role and a RAM user and grant permissions to the RAM role and RAM user, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. Create an organization
i. In the top navigation bar, click **Enterprise**. ii. In the left-side navigation pane, choose **Resources > Organizations**. iii. In the upper-right corner of the **Organizations** page, click **Create Organization**. iv. In the **Add Organization** dialog box, enter an organization name in the Name field. v. Click **OK**.
3. Create a RAM role
i. In the top navigation bar, click **Configurations**. ii. On the **Service-linked Roles** page, click **Create Service-linked Role**. iii. On the Create Service-linked Role page, configure the following parameters. The following part describes the parameters: Organization Name: Select your organization. Service Name: Select **Cloud Migration Center**. iv. Return to the **Service-linked Roles** page. From the **Service Name** drop-down list, select **Cloud Migration Center** and click **Search**. Check whether the service-linked role for SMC is added to your organization.
4. Create a user group.
i. In the top navigation bar, click **Enterprise**. ii. In the left-side navigation pane, choose **Users > User Groups**. iii. On the User Groups page, click **Create a user group**. iv. In the **Create a user group** dialog box, configure the User Group Name, Organization, and Role Permissions parameters. v. Click **OK**.
5. Create a RAM role and grant permissions to the role.
i. In the top navigation bar, click **Enterprise**. ii. In the left-side navigation pane, choose **Permissions > Role Permissions**. iii. Click **Create RAM Role**. iv. On the **Create RAM Role** page, configure the required information. The following part describes the parameters: Role Name: Enter a name for the role. Sharing Range: Select a sharing range based on your business requirements. v. Click **Create RAM Role**. vi. On the **User Groups** tab, click **Add User Group** and select a user group. vii. On the **Permissions** tab, click **Add Policy**.

> **Note:** If an existing SMC policy exists, click **Select Existing Policy** and select a policy.

viii. In the dialog box that appears, set Policy Name and Policy Content. You must create two polices. We recommend that you name the polices AliyunSMCFullAccess and AliyunSMCRolePolicy. AliyunSMCFullAccess Policy `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": "smc:*",
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": "ram:CreateServiceLinkedRole",
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "ram:ServiceName": "smc.aliyuncs.com"
```

`}` `}` `}` `]` `}` AliyunSMCRolePolicy Policy `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "ecs:DescribeAvailableResource",
        "ecs:DescribeZones",
        "ecs:RunInstances",
        "ecs:DescribeInstances",
        "ecs:StopInstance",
        "ecs:DeleteInstance",
        "ecs:AuthorizeSecurityGroup",
        "ecs:DescribeSecurityGroupAttribute",
        "ecs:CreateSecurityGroup",
        "ecs:DeleteSecurityGroup",
        "ecs:DescribeSecurityGroups",
        "ecs:CreateSnapshot",
        "ecs:DeleteSnapshot",
        "ecs:DescribeSnapshots",
        "ecs:CreateImage",
        "ecs:DescribeImages",
        "ecs:DescribeDisks",
        "ecs:DescribeAccountAttributes",
        "ecs:StartInstance",
        "ecs:DeleteImage",
        "ecs:DescribeLaunchTemplates",
        "ecs:DescribeLaunchTemplateVersions",
        "ecs:DescribeKeyPairs",
        "ecs:DetachDisk",
        "ecs:ReplaceSystemDisk",
```

```
        "ecs:AttachDisk",
        "ecs:DeleteDisk",
        "ecs:JoinSecurityGroup",
        "ecs:CreateDisk",
        "ecs:ModifyInstanceAttribute",
        "ecs:LeaveSecurityGroup",
        "ecs:ModifyImageAttribute"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "vpc:CreateVpc",
        "vpc:CreateVSwitch",
        "vpc:DescribeVpcs",
        "vpc:DeleteVSwitch",
        "vpc:DeleteVpc",
        "vpc:DescribeVSwitches"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "ram:GetRole",
        "cr:GetRepository"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": "ram:PassRole",
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "acs:Service": [
            "ecs.aliyuncs.com"
```

`]` `}` `}` `}` `]` `}` ix. Click **OK**.
6. Create a user and add the user to a user group.
i. Create a user. a. In the top navigation bar, click **Enterprise**. b. In the left-side navigation pane, choose **Users > Users**. c. On the **System Users** tab, click **Create a user**. d. In the **Create a user** dialog box, configure the parameters as prompted and click **OK**. e. In the **View AccessKey Pair** dialog box, save the AccessKey pair and click **Close**. f. Find the user whose authorization you want to modify. Click the icon in the **Actions** column and select **Authorize**. g. Select the role for the **Role** parameter based on your business requirements and click
**OK**.
h. Find the user whose initial password you want to view. Click the icon in the **Actions** column and click **View Initial Password**. i. In the **View Initial Password** dialog box, view the initial password. ii. Add a user to a user group. a. Find the user that you want to add to a user group, click the icon in the **Actions** column, and then select **Add to User Group**. b. In the **Add to User Group** dialog box, select a user group from the drop-down list. c. Click **OK**.

**Step 3: Obtain the AccessKey pair of the organization**

The system uses an AccessKey pair to verify the identity of the user who initiates the request. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. To migrate a source server, you must use the AccessKey pair of your organization as an access credential. To obtain the AccessKey pair of the organization, perform the following operations:
1. Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, click
**Enterprise**.
2. In the left-side navigation pane, choose **Resources > Organizations**.
3. In the organization list, click the name of the organization whose AccessKey pair you want
to obtain.
4. In the right-side section, click **Management AccessKey**.
5. In the Management AccessKey dialog box, view the AccessKey pair of the organization.
If no AccessKey pair is created in your organization, click **Create AccessKey**.

**Step 4: Create a VPC and a vSwitch**

Before you use SMC to migrate a source server, you must specify a VPC that can be accessed by the source server and a vSwitch. For details about how to create a Virtual Private Cloud and a switch, see **the Virtual Private Cloud User Guide**.

### 2.4 Step 1: Import the information about a migration source

**about a migration source**

Migration sources can be servers of a variety of types, such as servers in data centers, VMware VMs, and hosts on other cloud platforms. Before you migrate a source server, run the source server on the Server Migration Center (SMC) client and import the information about the migration source to Alibaba Cloud Apsara Stack. Then, log on to the SMC console to complete the migration. This topic describes how to import the information about a migration source.

**Prerequisites**

The preparations for the migration of the source server are made. For more information, see the following topics: Preparations on the source server

**Background information**

If you want to migrate only databases, we recommend that you use Data Transmission Service (DTS). For more information, see **Data Transmission Service Server DTS Product**
**Introduction**.

**Procedure**

1. Download and decompress the SMC client package.
i. Log on to the SMC console. ii. In the upper-right corner of the page, click **SMC Client Download URL** to obtain the download URL of the SMC client package. iii. Download the SMC client package. Use one of the following methods to decompress SMC client packages based on the operating system of the source server: Windows: Paste the download URL of the SMC client package in your web browser. Download the SMC client package to your on-premises machine and upload the SMC client package to the source server. Linux: Log on to the Linux server and run the **wget <Download URL of the SMC**
**client package>** command to download the SMC client package to the source server.
iv. Decompress the SMC client package. Use one of the following methods to decompress the SMC client package based on the operating system of the source server: Windows: Use the decompression tool provided by Windows or a decompression tool installed on the source server. Linux: Run the **unzip Alibaba_Cloud_Migration_Tool.zip** command. Make sure that the unzip utility is installed on the source server. For example, the installation command for CentOS 7 is **yum -y install unzip**. SMC provides client versions for different operating systems and architectures. Select a client version based on the operating system and architecture of the migration source. The following figure shows the decompressed client folders for Windows. Table 1. SMC client package description

| Client package | Archite cture | Operat ing system | Numbe r of bits | Supported destination instances after migration |
|---|---|---|---|---|
| go2aliyun client2.5.8 linux arm64.zip _ _ _ | ARM | Linux | 64 | Elastic Compute Service (ECS) image ECS instance |
| go2aliyun client2.5.8 linux i386.zip _ _ _ | x86 | Linux | 32 | ECS image ECS instance |
| go2aliyun client2.5.8 linux x86 64.zi _ _ _ _ p | x86 | Linux | 64 |   |
| go2aliyun client2.5.8 windows i386.zi _ _ _ p | x86 | Window s | 32 | ECS image ECS instance |
| go2aliyun client2.5.8 windows x86 6 _ _ _ _ 4.zip | x86 | Window s | 64 |   |

> **Note:** In the preceding table, 2.5.8 indicates a sample version number of the SMC client. The version number of your downloaded SMC client package prevails.
> SMC allows you to migrate Linux ARM64 servers. The supported instance families are the general-purpose instance family g6r and compute-optimized instance family c6r.

v. Decompress the client package that is compatible with the operating system of the migration source. The following figure shows the decompressed folders and files. Table 2. Description of the main files of the SMC client

| Folder or file | Description |
|---|---|
| go2aliyun client _ .exe | The Windows CLI executable file. |
| go2aliyun gui.e _ xe | The Windows GUI executable file. For more information about the GUI version, see Use the Windows GUI version of an SMC client. |
| go2aliyun client _ | The Linux CLI executable file. |
| user config.json _ | The configuration file of the migration source and destination. |
| Excludes | The folder to which the directories that you want to exclude from the migration are added. |
| client data _ | The migration data file, which stores the information about the intermediate instance and the migration progress. |

2. **(Optional)** Exclude files or directories from the migration.

> **Note:** The block replication feature must be enabled if you migrate a source server that runs on the Windows operating system. In this case, you cannot exclude files or directories from the migration. If you migrate a source server that runs on the Windows operating system, skip this step.

You can add the files or directories that you want to exclude from the migration to the configuration file in the Excludes directory. The following section describes the configuration files of the Linux operating system. The configuration file of the system disk: rsync_excludes_linux.txt. The configuration file of the data disk: the name of the system disk with the index number of the disk as the suffix. Example: rsync_excludes_linux_disk1.txt. The following table describes the examples on how to exclude configuration files from the migration.

| Configuration examples | Configuration file |
|---|---|
| Example 1: Exclude files from the system disk (root directory /) and the directory /var/mydirs/docs/words /var/mydirs/docs/excels/report1.txt | The final configuration file is as follows: /var/mydirs/docs/words/ /var/mydirs/docs/excels/report1.txt |
| Example 2: Exclude files and directories /mnt/disk1/mydirs2/docs2/words2 from the data disk /mnt/disk1/mydirs2/docs2/excels2/report 2.txt | Remove the prefix of a Linux path. In this example, /mnt/disk1 is removed. The final configuration file is as follows: /mydirs2/docs2/words2/ /mydirs2/docs2/excels2/report2.txt |

3. Run the SMC client to import the information about the migration source.
i. Open the SMC client folder and run the SMC client. Windows: Use one of the following methods to run the SMC client: To run the Windows GUI version, double-click the go2aliyun_gui.exe file. To run the Windows CLI version, double-click the go2aliyun_client.exe file.

> **Note:** When you run the program, you must click **OK** to confirm that you have the administrator privilege.

Linux: Run one of the following commands in the directory in which the go2aliyun_client file resides based on the root and sudo permissions. In this example, the go2aliyun_client file resides in the go2aliyun_client2.5.8_linux_x86_64 directory. Run the following commands in sequence if the Linux operating system supports the root permissions.

```
cd go2aliyun_client2.5.8_linux_x86_64 chmod +x go2aliyun_client ./go2aliyun_client
```

Run the following commands in sequence if the Linux operating system supports the sudo permissions.

```python
cd go2aliyun_client2.5.8_linux_x86_64 sudo chmod +x ./go2aliyun_client sudo ./go2aliyun_client
```

ii. Enter the endpoint of SMC and the AccessKey pair of your Alibaba Cloud Apsara Stack account. Obtain the endpoint of SMC in advance. For more information, see Preparations on the source server. Obtain an AccessKey pair of your Alibaba Cloud Apsara Stack account in advance. For more information, see the "Step 3: Obtain the AccessKey pair of the organization" section of the Preparations in the Apsara Uni-manager Operations Console topic.

> If the AccessKey pair that you enter is invalid, open the user_config.json file, delete the values of the **access_id** and **secret_key** parameters, and then run the client again.

Windows servers To run the Windows GUI version, enter the `endpoint of SMC` in the **SMC ********** field. Enter the `AccessKey ID` in the **Account AK** field. Enter the `AccessKey secret` in the
**Account SK**field. Then, click **Run**. For more information, see Use the Windows GUI
version of the SMC client.

```
endpoint of SMC,
```

`AccessKey ID`, and To run the Windows CLI version, enter the `AccessKey secret` and click `Enter` . Linux servers

```
endpoint of SMC,
```

`AccessKey ID`, and Enter the `AccessKey secret` and click `Enter` . The following messages may appear: If no snapshot dependency is installed on your source server, a message appears. The following figure shows the details of the message. You can install a snapshot dependency based on whether you need to enable the block replication feature. If you need to enable the block replication feature when you create a migration job and the source server can access the Internet, enter `yes` to automatically install a snapshot dependency. If you do not enable the block replication feature when you create a migration job `no`. or the source server cannot access the Internet, enter

> **Note:** If the snapshot dependency fails to be installed, do not enable the block replication feature when you create a migration job. Otherwise, the migration may fail.

By default, the rsync tool is installed on most mainstream migration sources. If the rsync tool is not installed on your source server, the message in the following figure is returned. Enter `yes` to automatically install the rsync tool. Enter `no` if you want to manually install the rsync tool. If SELinux is enabled on the migration source, a message that prompts you to disable SELinux appears. Enter `yes` to disable SELinux. The following figure shows how to disable SELinux.

> **Important:** Do not close the client until the migration is complete. Otherwise, the migration source is disconnected from the SMC console and the migration fails.

4. View import results of the information about the migration source.
If the Import Source Server [s-bxxxxxxxxxxxx] Successfully! message is returned, the information about the migration source is imported to the SMC console.

> **Important:** Do not close the client. Otherwise, the migration fails.

If you import the information about the migration source for the first time, a record is automatically generated in the SMC console and the source migration is in the Online state. The default name of the source migration is in the <host name of the migration source + IP address of the migration source> format. The following figure shows an example. When you import the information about a migration source, SMC collects information about the source server, including the CPU, memory, CPU utilization, memory usage, and internal IP address. Click the ID of the migration source to view the information. The following figure shows the information. After the migration job is complete, you can create an ECS instance by using the information about the source server. After the information about the migration source is imported, create and start a migration job in the SMC console to migrate the source server. For more information, see Step 2: Create and start a migration task. If the message Error or Goto Aliyun Not Finished! appears, the information about the migration source failed to be imported. The following figure shows the error message. We recommend that you troubleshoot the issue, and run the client again.

### 2.5 Step 2: Create and start a migration job

**migration job**

After you import the information about a migration source, Server Migration Center (SMC) automatically generates a record for the migration source. You must create and start a migration job for the migration source in the SMC console. This topic describes how to create and start a migration job.

**Prerequisites**

The information about the migration source is imported to the SMC console. For more information, see Step 1: Import the information about a migration source. The migration source is in the Active state.

**Background information**

SMC can obtain the partitioning scheme of a source disk used by the migration source and generate the same partitioning scheme for the destination disk. This accelerates data transmission during the migration.

**Procedure**

1. Log on to the SMC console.
2. Create a migration job.
i. In the left-side pane, click **Migration Sources**. ii. On the Migration Sources page, find the migration source that you want to manage and click **Create Migration Job** in the **Actions** column. You can obtain the migration source ID from the CLI or GUI of the SMC client and find the migration source that you want to manage based on the migration source ID. The following figure provides an example. iii. In the **Create Migration Job** panel, read the instructions and configure the parameters for the migration job.

**Basic Settings**

**Destination Region**: required. The ID of the Apsara Stack region to which you want to
migrate the source server.
**Migration Job Name**: the name of the migration job.

> **Note:** The job name must be unique within an Apsara Stack region.

**Job Description**: the description of the migration job.
**Destination Disk Size (GiB)**: the disk configurations of the destination Elastic
Compute Service (ECS) instance. The following table describes the parameters.

| Parameter | Req uire d | Description |
|---|---|---|
| Enable Block Replication | No | If you select Enable Block Replication, stable data transmission is ensured. The block-level replication feature also ensures that the source and destination disks use the same partitioning scheme. You cannot modify the size of each partition on the destination disk. After you select Enable Block Replication, the Enable Block Replication switch appears next to Partition <N>. If you clear Enable Block Replication, SMC uses the default method to migrate the source server at the file level. You can modify the size of each partition on the destination disk. Note If your source server runs Windows, block-level replication is enabled by default. Do not disable this feature. If your source server runs Linux and no snapshot dependency is installed or a snapshot dependency fails to be installed on your source server, you must disable block-level replication. Otherwise, the migration fails. |

| System Disk | Yes | System Disk: the size of the system disk of the destination ECS instance. Unit: GiB. Valid values: 20 to 2048. The size of the destination system disk must be larger than the amount of data stored on the source system disk. For example, if the total size of the source system disk is 400 GiB but the amount of data stored on this disk is only 100 GiB, you must set this parameter to a value greater than 100. Note By default, the size of the destination system disk equals that of the source system disk. We recommend that you retain the default value or specify a greater value. Partition <N>: the size of the partition. SMC generates a partitioning scheme for the destination disk based on the partitioning scheme of the source disk. Unit: GiB. Valid values: 1 to 2047. <N> indicates the serial number of the partition. For example, if the system disk of the migration source has only one partition, Partition 0 is generated. Enable Block Replication: This switch is displayed only if you select Enable Block Replication. SMC allows or disallows you to turn on the switch based on whether the migration source supports block-level replication for partitions. If the migration source does not support block-level replication for partitions, you cannot turn on the switch. If the migration source supports block-level replication for partitions, you can turn on the switch to migrate disk data at the partition level. |
|---|---|---|

| Data Disk <N> | No | Data Disk <N>: the size of the data disk of the destination ECS instance. Unit: GiB. Valid values: 20 to 32768. If you select Data Disk <N>, a destination data disk is generated. <N> indicates the serial number of the data disk. The size of the destination data disk must be larger than the amount of data stored on the source data disk. For example, if the total size of the source data disk is 500 GiB but the amount of data stored on this disk is only 100 GiB, you must set this parameter to a value greater than 100. Partition <N>: the size of the partition. SMC generates a partitioning scheme for the destination disk based on the partitioning scheme of the source disk. Unit: GiB. Valid values: 0 to 141. <N> indicates the serial number of the partition. For example, if a data disk of the migration source has only one partition, Partition 0 is generated. Enable Block Replication: This switch is displayed only if you select Enable Block Replication. SMC allows or disallows you to turn on the switch based on whether the migration source supports block-level replication for partitions. If the migration source does not support block-level replication for partitions, you cannot turn on the switch. If the migration source supports block-level replication for partitions, you can turn on the switch to migrate disk data at the partition level. Note Data Disk <N> is displayed only if the migration source has a data disk. |
|---|---|---|

**Destination Type**: the type of the destination on Apsara Stack to which you want to
migrate the source server. If you select **ECS Image**, you can configure the parameters that are described in the following table.

| Parameter | Req uire d | Description |
|---|---|---|
| Image Name | No | The name of the destination ECS image generated by SMC for the migration source. Note The image name must be unique within an Apsara Stack region. |
| Automatic Incremental Synchroniza tion | No | Specifies whether SMC automatically synchronizes incremental data from the migration source to Apsara Stack. To enable this feature, you must configure the following parameters: Synchronization Interval: the interval at which SMC automatically synchronizes incremental data to Apsara Stack. Upperlimit of Reserved Images: the maximum number of images that can be retained during incremental migration. SMC automatically synchronizes incremental data to Apsara Stack at the specified interval. For more information, see Migrate incremental data from a source server. If you disable this feature, incremental data is not synchronized. |

If you select **ECS Instance**, you can configure the parameters that are described in the following table. The storage system and operating system of the source server must be compatible with those of the destination ECS instance. For more information, see Migrate a server to an ECS instance.

| Parameter | Req uire d | Description |
|---|---|---|
| Destination Instance | Yes | The destination ECS instance. |
| Automatic Incremental Synchroniza tion | No | Specifies whether SMC automatically synchronizes incremental data from the migration source to Apsara Stack. To enable this feature, you must configure the following parameters: Synchronization Interval: the interval at which SMC automatically synchronizes incremental data to Apsara Stack. Upperlimit of Reserved Images: the maximum number of images that can be retained during incremental migration. SMC automatically synchronizes incremental data to Apsara Stack at the specified interval. For more information, see Migrate incremental data from a source server. If you disable this feature, incremental data is not synchronized. |

**Execution Method**: the mode in which the migration job is run. Valid values:
**Run Now**: The migration job starts immediately after it is created.
**Run Later**: The migration job automatically starts at the specified time after it is
created.

> **Note:** The earliest time that you can specify to run a migration job is 10 minutes after the job is created.

**Create Only**: After the migration job is created, you must manually start the
migration job. Default value: **Run Now**.

**Tags and Network (Optional)**

**Network Type**: the type of the network that is used to migrate data to the intermediate
instance. During the migration, SMC creates an intermediate instance that connects to a vSwitch in a virtual private cloud (VPC). If you select Public Network, a public IP address is assigned to the intermediate instance. The following table describes the valid values.

| Valid value | Description |
|---|---|
| Public Network | SMC migrates data to the intermediate instance over the Internet. If you select Public Network, make sure that the source server can access the Internet. You can determine whether to specify a VPC and a vSwitch based on your business requirements. If you specify a VPC and a vSwitch, SMC creates an intermediate instance that connects to the specified VPC and vSwitch. If you migrate multiple migration sources at a time, you can specify the same VPC and vSwitch for migration jobs. This improves the usage of VPC resources. In this case, you can migrate up to 100 migration sources at a time. If you do not specify a VPC or a vSwitch, SMC automatically creates a VPC and a vSwitch, and creates an intermediate instance that connects to the created VPC and vSwitch. If you do not specify a VPC or a vSwitch before you migrate multiple migration sources at a time, SMC creates a VPC for each intermediate instance. Note Each Apsara Stack tenant account can have up to 10 VPCs in a region, including the VPCs that are manually created and the VPCs that are automatically created by SMC. Therefore, you can migrate up to 10 migration sources at a time if you do not specify a VPC or a vSwitch. |
| VPC | SMC migrates data to the intermediate instance over a VPC. If you select VPC, you must specify a VPC and a vSwitch and make sure that the source server can connect to the VPC. Note If your server in a self-managed data center, your VM, or your third-party cloud server can connect to a VPC, we recommend that you select this network type to migrate data. Compared with migration over the Internet, migration over a VPC is more efficient and stable. You can use VPN Gateway, Express Connect, and Cloud Gateway to connect a migration source to a VPC. |

**Advanced Settings (Optional)**

**Checksum Verification**: specifies whether to verify data integrity by using a
checksum. If you enable this feature, data integrity is ensured, but transmission speed may be reduced. By default, this feature is disabled.
**Transmission Speed Limit**: the maximum bandwidth for data transmission during
the migration. Unit: Mbit/s.
**Compression Ratio**: the compression ratio of the data to be migrated. Set the
compression ratio based on your business requirements. If the bandwidth is limited, a high compression ratio improves the transmission efficiency. If a high bandwidth is available, we recommend that you do not compress data. Data compression consumes the CPU resources of the migration source. Valid values: 0 to 10. Default value: 7. A value of 0 specifies that data is not compressed.
**Intermediate Instance Type**: the instance type of the intermediate instance. Select
an instance type based on your business requirements. This parameter is displayed only if the **Destination Type** parameter is set to **ECS Image**. If you specify an instance type, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, the migration job fails to be created. If you do not specify an instance type, SMC automatically selects an instance type to create an intermediate instance. iv. After you configure the preceding parameters, click **OK**.
3. Start the migration job.

> **Note:** If the Execution Method parameter is set to **Run Now**, skip this step. If the Execution Method parameter is set to **Create Only** or **Run Later**, you can perform the following steps to start the migration job.

i. In the left-side pane, click **Migration Jobs**. ii. Find the migration job and click **Run** in the Actions column. To pause a migration job in the **Synchronizing** state, click **Pause** in the **Actions** column.

**What to do next**

On the **Migration Jobs** page, wait until the migration job is complete. You can view the migration speed and remaining synchronization duration. If the state of the migration job changes to **Completed**, the migration succeeds. If you set the Destination Type parameter to **ECS Instance**, you can find the migration job and click View Destination Instance in the Actions column to view the details of the destination ECS instance. If you set the Destination Type parameter to **ECS Image**, you can perform the following steps to view the destination ECS image: a. Log on to the Apsara Uni-manager Management Console. For more information, see Step 1: Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Elastic Computing > Elastic**
**Compute Service**.
c. In the left-side navigation pane, choose **Instances & Images > Images**. d. On the **Custom Image** tab, find and view the destination ECS image. If the state of the migration job changes to **InError**, the migration fails. In this case, you can perform the following steps: i. Find the migration job and click **View Logs** in the **Actions** column to view logs and fix errors. ii. After errors are fixed, click **Retry Migration Job** in the **Actions** column. The migration job resumes from the point at which it was stopped. version of the SMC client

## 3 Use the Windows GUI version of the SMC client

**version of the SMC client**

You can use the Windows GUI version of the Server Migration Center (SMC) client to migrate Windows servers to Apsara Stack. The settings for the SMC client on the GUI are the same as those on the CLI. The Windows GUI version is compatible with the CLI version.

**Daemon mode**

In daemon mode, you can import the information about a migration source by using the SMC client. Then, you can log on to the SMC console to complete the migration. You must configure the **SMC Endpoint**, **Access Id**, and **Secret Key** parameters. For more information about how to migrate servers in the SMC console, see Migration process. The following figure shows the Windows GUI of the SMC client in daemon mode.

**GUI elements**

version of the SMC client The following figure shows the elements on the Windows GUI of the SMC client. The following table describes the GUI elements.

| No. | Section | Description |
|---|---|---|
| 1 | Top navigation bar | Consists of the Config, Logs, View, Help, and Language menus. Config: Click Sync. In the dialog box that appears, specify the maximum bandwidth for data transmission. Unit: KB/s. Click Save User Config to save the current settings. Click Clear Client Data to initialize the client configuration file. Logs: Click Open Log File to open the migration log file. Click Open Logs Dir to find the path of the migration log file. View: Click Hide Progress Log to hide or show the Progress Logs section. Help: Obtain online documentation or the version information of the SMC client. Language: Select the display language of the GUI. |

version of the SMC client

| 2 | Custom configuration section | Allows you to configure parameters to specify the endpoint of SMC and your AccessKey pair. SMC Endpoint: the endpoint of SMC. Access Id: your AccessKey ID. Secret Key: your AccessKey secret. Note Obtain the endpoint of SMC in advance. For more information, see Prepare a source server. Obtain an AccessKey pair in advance. For more information, see Step 3: Obtain the AccessKey pair of the organization. The settings that you configure are written to the user config.json file of the SMC client. _ |
|---|---|---|
| 3 | Job progress and logs section | Allows you to view the job progress or troubleshoot issues after you run the SMC client. |

data from a source server

## 4 Migrate incremental data from a source server

**from a source server**

Server Migration Center (SMC) allows you to migrate incremental data from source servers to Apsara Stack. You can specify the time interval between two consecutive incremental migrations. Incremental migration reduces the service downtime and the total migration duration. This topic describes how to migrate incremental data from a source server.

**Prerequisites**

The information about the source server is imported to the SMC console. For more information, see Step 1: Import the information about a migration source.

**Background information**

Make sure that the SMC client is running during the migration. If data transmission is interrupted, you can restart the SMC client and the migration job to resume the migration. The intermediate instance is released only when the incremental migration job is in the
**Expired** state or when the job is deleted.

**Step 1: (Optional) Exclude dynamic data directories**

To ensure stable migration, we recommend that you exclude dynamic data directories, such as the data directories of large databases, before you start an incremental migration job. Later, you can stop the services on the source server and migrate the excluded data directories. Skip this step if you do not need to exclude dynamic data directories from migration. To exclude dynamic data directories, perform the following steps. You do not need to stop the services that are running on the source server.
1. Log on to the source server.
2. **(Optional)** Exclude files or directories from the migration.

> **Note:** The block replication feature must be enabled if you migrate a source server that runs on the Windows operating system. In this case, you cannot exclude files or directories from the migration. If you migrate a source server that runs on the Windows operating system, skip this step.

You can add the files or directories that you want to exclude from the migration to the configuration file in the Excludes directory. The following section describes the configuration files of the Linux operating system. The configuration file of the system disk: rsync_excludes_linux.txt. The configuration file of the data disk: the name of the system disk with the index number of the disk as the suffix. Example: rsync_excludes_linux_disk1.txt. The following table describes the examples on how to exclude configuration files from the migration.

| Configuration examples | Configuration file |
|---|---|

data from a source server

| Example 1: Exclude files from the system disk (root directory /) and the directory /var/mydirs/docs/words /var/mydirs/docs/excels/report1.txt | The final configuration file is as follows: /var/mydirs/docs/words/ /var/mydirs/docs/excels/report1.txt |
|---|---|
| Example 2: Exclude files and directories /mnt/disk1/mydirs2/docs2/words2 from the data disk /mnt/disk1/mydirs2/docs2/excels2/report 2.txt | Remove the prefix of a Linux path. In this example, /mnt/disk1 is removed. The final configuration file is as follows: /mydirs2/docs2/words2/ /mydirs2/docs2/excels2/report2.txt |

**Step 2: Create and start an incremental migration job**

You can perform the following steps to create and start an incremental migration job in the SMC console. You do not need to stop the services that are running on the source server.
1. Log on to the SMC console. For more information, see Log on to the SMC console.
2. In the left-side pane, click **Migration Sources**.
3. On the Migration Sources page, find the source server from which you want to migrate data
and click **Create Migration Job** in the **Actions** column.
4. In the **Create Migration Job** panel, turn on **Automatic Incremental Synchronization**
and configure the **Synchronization Interval** and **Upperlimit of Reserved Images** parameters. Configure other parameters based on your business requirements and click
**OK**.
The following list describes some parameters. For more information about other parameters, see Step 2: Create and start a migration job.
**Synchronization Interval**: the time interval between two consecutive incremental
migrations. You can specify a time interval in the range of one hour to seven days.
**Upperlimit of Reserved Images**: the maximum number of images that can be retained
during incremental migration. Valid values: 1 to 10. An image is generated for each incremental migration. If the total number of images exceeds the upper limit, the earliest unused image is deleted.
**Execution Method**: the mode in which the migration job is run. In this example, **Run**
**Now** is selected.
The incremental migration job immediately starts after it is created. Data is migrated in the following way: data from a source server i. During the first incremental migration, SMC migrates all data except the excluded directories and files, and generates a full image. You can use this image to create an Elastic Compute Service (ECS) instance for verification. ii. After the first incremental migration is complete, SMC automatically migrates incremental data and generates images at specific points in time based on the time interval that you specify.

> **Note:** The image generated for each incremental migration is a full image of the source server at a specific point in time. The image contains the incremental data at the point in time of migration and all earlier migrated data.

In the image names that are generated during incremental migration, `CYCLE_X` indicates that the image is generated by the Xth incremental migration. For example, if an image name contains CYCLE_2, the image is generated by the second incremental migration, as shown in the following figure.

**Step 3: Stop the services on the source server and run the**

**incremental migration job again**

Select an appropriate point in time to stop the services on the source server, and perform the following steps to include the excluded data directories and run the incremental migration job again:
1. Log on to the source server. Stop the services on the source server and include the
excluded data directories.
2. In the SMC console, manually run the incremental migration job or wait for the job to
automatically run. To manually run the incremental migration job, perform the following steps: i. On the **Migration Jobs** page, find the incremental migration job. ii. In the **Actions** column, click **Manual Incremental Synchronization**. iii. In the **Start Migration Job** dialog box, click **OK**.

**View the result**

On the **Migration Jobs** page, wait until the incremental migration job is complete. If the incremental migration job is in the **Pending** state, the migration is successful. You can obtain the image that is generated for the last migration. The image contains all the data migrated by the first full migration and each subsequent incremental migration. If the incremental migration job is in the **InError** state, the migration fails. You can click
**View Logs** in the **Actions** column to view logs and fix errors. After errors are fixed, restart
the migration job.

**What to do next**

After you obtain the image generated for the last migration, you can perform the following operations: Create an ECS instance to verify the image. i. On the **Migration Jobs** page, find the migration job and view the ID of the image generated for the last migration in the **Migration Result** column. data from a source server ii. Go to the **Create Instance** page in the ECS console and select the image generated for the last migration as **Custom Image**. Configure other parameters based on your business requirements and purchase an ECS instance. For more information, see the "Create an instance" topic in **Elastic Compute Service User Guide**. iii. Connect to the ECS instance and check the migrated system. Pause an incremental migration job.

> **Note:** You can stop an incremental migration job only if the job is in the **Synchronizing** or **Pending** state.

i. On the **Migration Jobs** page, find the migration job and click the icon in the **Actions** column. ii. Select **Pause**. iii. In the **Pause Migration Job** dialog box, click **OK**. Delete an incremental migration job. i. On the **Migration Jobs** page, find the migration job and click the icon in the **Actions** column. ii. Select **Delete**. iii. In the **Delete Migration Job** dialog box, click **OK**. n ECS instance

## 5 Migrate a server to an ECS instance

**instance**

Server Migration Center (SMC) can be used to migrate servers to Elastic Compute Service (ECS) instances. After you purchase an ECS instance, you can migrate your server to the ECS instance. This topic describes how to migrate a server to an ECS instance.

**Prerequisites**

The preparations for the migration are complete. For more information, see Prepare a source server. An ECS instance is created as the destination ECS instance. Make sure that the instance has no data or the data of the instance is backed up by using images, snapshots, or other resources.

> **Warning:** After a migration job is created, all original data is deleted from the destination ECS instance. If the destination ECS instance contains important data, we recommend that you do not directly migrate the source server to the destination instance. In this case, we recommend that you set the Destination Type parameter to ECS Image to migrate the source server to an ECS image and then create an ECS instance by using the image.
> If you migrate data from an ECS instance, make sure that the source ECS instance and the destination ECS instance are different. Otherwise, the migration may fail and data on the cloud disks of the source instance may be lost.

The information about the source server is imported to the SMC console. For more information, see Step 1: Import the information about a migration source.

> **Note:** Make sure that the SMC client is running during the migration. If data transmission is interrupted, you can restart the SMC client and the migration job to resume the migration.

The operating system of the destination ECS instance is the same as that of the source server. The number of data disks attached to the destination ECS instance is greater than or equal to that of data disks attached to the source server. Otherwise, the disk data of the source server cannot be migrated to the destination ECS instance. In this case, you must attach more data disks to the ECS instance. For more information, see the "Attach a data disk" topic in **Elastic Compute Service User Guide**. The capacity of the system disks and data disks attached to the destination ECS instance is larger than or equal to that of the system disks and data disks attached to the source server. Otherwise, the data of the source server cannot be fully migrated to the destination ECS instance. In this case, you must extend the data disks and system disks attached to the ECS instance. For more information, see the "Expand a disk" topic in **Elastic Compute**
**Service User Guide**.

**Procedure**

1. Log on to the SMC console.
n ECS instance
2. In the left-side pane, click **Migration Sources**.
3. On the Migration Sources page, find the source server from which you want to migrate data
and click **Create Migration Job** in the **Actions** column.
4. In the **Create Migration Job** panel, configure the parameters.
This topic describes how to configure the parameters for the destination ECS instance. For more information about other parameters, see Step 2: Create and start a migration job. Parameters for the destination ECS instance:
**Destination Type**: Select **ECS Instance**.
**Destination Instance**: Select an ECS instance based on your business requirements.
After you select an ECS instance, the disk information of the instance is displayed.
**Network Type**: optional. By default, VPC is selected as **Network Type** and the virtual
private cloud (VPC) and vSwitch in which the destination ECS instance resides are selected. The migration job immediately starts after it is created. Then, the migration job enters the Completed or InError state. If the migration job is in the **Completed** state, the job is complete and you can view the details of the destination ECS instance. If the migration job is in the **InError** state, the job fails. You can view logs and fix errors. After errors are fixed, restart the migration job.
