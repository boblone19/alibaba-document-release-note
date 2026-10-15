---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Key Management Service Key Management Service User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 51
source_pdf: "ea066775dc9dd523_Alibaba Cloud Apsara Stack v3.18.6-2607 Key Management Service Key Management Service User Guide 202"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Key%20Management%20Service%20Key%20Management%20Service%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Key Management Service Key Management Service User Guide 20260831

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 Log in to the Apsara Uni-manager Management Console
  - 2.2 User roles and permissions
- 3 Manage CMKs
  - 3.1 Create a key
  - 3.2 View and adjust the key quota
  - 3.3 View the details of a CMK
  - 3.4 Enable a CMK
  - 3.5 Disable a CMK
  - 3.6 Synchronize keys across regions
  - 3.7 Schedule key deletion
  - 3.8 Configure a rotation policy
  - 3.9 Generate a data key
  - 3.10 Generate a CSR
- 4 Use RAM for access control
- 5 Use aliases
- 6 Customer master key
- 7 Use symmetric keys
  - 7.1 Symmetric encryption
  - 7.2 EncryptionContext
  - 7.3 Import and delete key material
- 8 Use asymmetric keys
  - 8.1 Asymmetric keys
  - 8.2 Asymmetric data encryption and decryption
  - 8.3 Asymmetric digital signature
- 9 Rotate CMKs
  - 9.1 Overview
  - 9.2 Automatic key rotation
  - 9.3 Manually rotate a master key

## 1 Usage notes

Before you log on to Apsara Stack Security Center, make sure that your computer meets the configuration requirements. For more information, see the Configuration requirements table of this topic. Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Quick start

### 2.1 Log in to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log in to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button. If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.
Obtain the username and password from an operations administrator. The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**. For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in Apsara Uni-manager Management Console User Guide.

**What to do next**

**Forget password**

1. If you forget the login password, click **Forgot Password** below the Password field.
2. On the Forgot Password page, configure the **Account Name** and **Email Address**
parameters, enter the verification code, and then click **Confirm**. Enter the username of your account in the Account Name field and the email address that was used to create the account in the Email Address field. The system sends a link for resetting the password to the email address that you specify.

### 2.2 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. Custom roles and default roles are supported. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. Table 1. Default roles in Apsara Stack Security

| Role | Description |
|---|---|
| Organization security administrator | This role has the permissions to use Security Operations Center (SOC) to manage the security of hosts, applications, and networks for an organization. This role also has the permissions to manage security services related to Elastic Compute Service (ECS). |
| Global organization security administrator | This role has the permissions to use SOC to conduct security management for Apsara Stack and all tenants and manage security services related to ECS. |

If you do not have an account or a role, contact the administrator to create a user and assign a role to the user. For more information, see **Create a user** in **Apsara Uni-manager**
**Management Console User Guide**.

## 3 Manage CMKs

### 3.1 Create a key

This topic describes how to create a customer master key, which you can use for encryption and decryption.

**Procedure**

1. Sign in to the Apsara Uni-manager Operation Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Keys** page, click **Create Key**.
4. On the **Create Key** page, select an **organization**. The system automatically populates the
**resource set** and **region** fields.
5. In the **Basic configurations** section, configure the following parameters.

| Parameter | Description |
|---|---|
| Key type | Valid values: Symmetric key types: Aliyun AES 256 _ _ Asymmetric key types: RSA 2048 _ EC P256 _ EC P256K _ |
| Key usage | Valid values: ENCRYPT/DECRYPT: Encrypt and decrypt data. SIGN/VERIFY: Generate and verify a digital signature. |
| Protection level | Valid values: SOFTWARE: Protects the key with a software module. |
| Alias | An optional identifier for a customer master key. For more information, see Manage aliases. |
| Description | A description of the customer master key. |

6. In the **Advanced configurations** section, configure the following parameters.

| Parameter | Description |
|---|---|

| Rotation period | Valid values: Disable: Disables automatic key rotation. Enable: Enables automatic key rotation. You can select a predefined rotation interval or specify a custom number of days. Note You can set a rotation period only for symmetric keys of type Aliyun AES 256 . _ _ You cannot enable automatic rotation for keys with an external key material origin. |
|---|---|
| Key material origin | Valid values: Aliyun KMS: Key Management Service (KMS) generates the key material. External: KMS does not generate the key material. You must import your own key material into KMS. Note You can import external key material only for symmetric keys of type Aliyun AES 256 . _ _ |

7. Click **Submit**.

### 3.2 View and adjust the key quota

This topic describes how to view and adjust the key quota.

**View the key quota**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, click **Create Key**.
4. In the **Quota** section on the right side of the page, view the key quota and usage.

**Increase or decrease the key quota**

1. In the **Quota** section on the right side of the **Create Key Pair** page, click **Quota**
**Management** to go to the Quotas page.
2. Enter **Key Management Service** in the **cloud service name** search box.
3. Increase or decrease the quota based on on-screen instructions.

**Cancel the key quota limit**

1. In the **Quota** section on the right side of the **Create Key Pair** page, click **Quota**
**Management** to go to the Quotas page.
2. Enter **Key Management Service** in the **cloud service name** search box.
3. Change the quota to Not Configured based on on-screen instructions.
After you modify the quota, the **Quota** section indicates that no quota data is available.

### 3.3 View the details of a CMK

After you create a customer master key (CMK), you can view the details of the CMK, such as the key status, purpose, and creation time.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, search for a CMK by **Protection Level**, **Key Status**,
**Key Usage**, **Key Type**, **Regional**, and **Alias**.
4. Find the CMK that you want to view and click its alias or choose **More > Key Details** in the
Actions column. In the CMK list, you can find a CMK and move the pointer over the value in the **Key ID** column. Then, the description of the CMK appears. This helps you distinguish CMKs.
5. In the **Key Details** section, view the details of the CMK, such as the status, purpose, and
creation time.

### 3.4 Enable a CMK

This topic describes how to enable a customer master key (CMK) that is in the disabled state.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK that is in the **Disabled** state and click
**Enable** in the **Actions** column.
4. In the **Enable Key** message, click **OK**.
After the CMK is enabled, the status of the CMK is changed from **Disabled** to **Enabled**.

### 3.5 Disable a CMK

This topic describes how to disable a customer master key (CMK).

**Background information**

If a CMK is disabled, the CMK cannot be used for encryption or decryption. The ciphertext encrypted by using this CMK cannot be decrypted until you enable the CMK.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK that is in the **Enabled** state and click
**Disable** in the **Actions** column.
4. In the **Disable Key** message, click **OK**.
After the CMK is disabled, the status of the CMK is changed from **Enabled** to **Disabled**.

### 3.6 Synchronize keys across regions

**regions**

This topic describes how to synchronize keys across regions.

**Overview**

Key Management Service (KMS) allows you to create replica keys in different regions. This way, you can encrypt data by using the data key generated based on the customer master key (CMK) in Region A and decrypt the data by using the replica key in Region B. The following key properties are synchronized during key synchronization: key ID, key material, original key material, key description, algorithm, key usage, automatic key rotation, and manual key rotation. If you manually import key material for a CMK, the key material is not automatically synchronized to the corresponding replica keys. You must manually import the key material for each replica key. The following table describes the features supported by CMKs and replica keys.

| Capability | CMK | Replica key | Description |
|---|---|---|---|
| Enable | Supported | Supported | Enabling a CMK does not affect its replica keys. |

| Disable | Supported | Supported | Disabling a CMK does not affect its replica keys. |
|---|---|---|---|
| Delete schedules or cancel schedule deletion | Supported | Supported | A CMK can be deleted only after all its replica keys are deleted. After a replica key is deleted, it can be recreated from the CMK. The new replica key is same as the original one, and services are not affected. |
| Data key | Supported | Supported | Data encrypted by using a data key created from a CMK can be decrypted by using a replica key. |
| Alias | Supported | Supported | You can modify the alias of a CMK, which does not affect its replica keys. |
| Tag | Supported | Supported | You can modify the tags of a CMK, which does not affect its replica keys. |
| Key rotation | Supported | Not supported | Only CMKs can be rotated. The rotation settings of a CMK are synchronized to all its replica keys. When a CMK is rotated, the newly created key material will be synchronized to all its replica keys. During key rotation and synchronization, you cannot encrypt or decrypt data. Asymmetric keys and Bring Your Own Key (BYOK) keys cannot be rotated in this scenario. |

Regional identifiers of keys: Single-region key: By default, new keys are single-region keys. Multi-region CMK: After you create a replica key, the original single-region key is changed to a multi-region key. Multi-region replica key: The replica key that you created is marked as a multi-region replica key.

**Create a replica key**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK for which you want to create replica
keys, and click its alias or choose **More > Key Details** in the **Actions** column.
4. Click the **Regional** tab on the key details page and click **Create Replica Key**.
5. In the **Create Replica Key** dialog box, specify **Area**, **Alias**, **Description**, and **Tag**, and
then click OK.

**Change the primary region**

You can change the primary region of only CMKs. Replica keys do not support this operation.

**Warning**

Make sure that the CMK and replica keys are enabled before you change the primary region. During the operation, you cannot perform other operations to manage the CMK or replica keys.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK whose primary region you want to
change, and click its alias or choose **More > Key Details** in the **Actions** column.
4. On the **Regional** tab of the key details page, click **Change Primary Region**.
5. In the **Change Primary Region** dialog box, select a region and click **OK**.

### 3.7 Schedule key deletion

This topic describes how to schedule a customer master key for deletion by specifying a pending deletion period.

**Background**

You need to specify a pending deletion period from 7 to 30 days. The following are notes about scheduling a key for deletion: During the pending deletion period, the key is in the pending deletion state and cannot be used for encryption, decryption, or generating data keys. As a best practice, disable the key instead of deleting it. A master key cannot be recovered after deletion, and all data encrypted by it becomes permanently undecipherable. For this reason, Key Management Service (KMS) prevents immediate deletion and requires you to schedule it instead. KMS deletes the key within 24 hours after the pending deletion period ends. For example, if you schedule a master key for deletion on September 10, 2024, at 14:00 with a seven-day pending deletion period, KMS will delete the key within 24 hours after 14:00 on September 17, 2024.

**Procedure**

1. Log in to the Apsara Uni-manager Operation Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Keys** page, find the key you want to delete. In the **Actions**
column, choose **More > Schedule Key Deletion**.
4. In the **Schedule Key Deletion** dialog box, set the **Pending Deletion Period (7-30**
**days)**.
5. Click **OK**.

**Result**

The key status changes to **Pending Deletion**. Before the pending deletion period ends, you can cancel the scheduled deletion by choosing **More > Cancel Key Deletion**.

### 3.8 Configure a rotation policy

This topic describes how to configure a rotation policy of a customer master key (CMK).

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, select a symmetric CMK whose **Key Type** is
Aliyun_AES_256, and choose More > **Key Details** in the **Actions** column.
4. On the **Key Version** tab, click **Configure Rotation Policy**.
5. In the **Configure Rotation Policy** dialog box, configure the **Rotation Period** parameter.
Disable: Disable automatic rotation for the CMK. 30 Days, 90 Days, 180 Days, and 365 Days: Select an automatic rotation interval. Customize: Allow you to specify a custom rotation interval.
6. Click **OK**.

### 3.9 Generate a data key

Data keys can be used to encrypt and decrypt on-premises data. This topic describes how to generate a data key.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find an asymmetric CMK whose Key Usage is
**Encrypt/Decrypt** and click its alias or choose **More > Key Details** in the **Actions**
column. The key type for symmetric keys is Aliyun_AES_256.
4. On the **Data Key Usage** tab, click the **Generate Data Key** tab, configure parameters, and
click **Submit**. i. In the **Parameters to Generate Data Key** section, configure the **Key Type** and
**Encryption Context** parameters.
ii. In the **Parameters to Generate Data Key** section, configure the **Encrypt Data Key**
**by Using Public Key** parameter. Valid values:
**Yes**: Encrypt a data key by using a specific public key and export the data key. In the
**Specify the export publicKey** section, configure the **Publickey Type**, **Public Key**,
and **Key Algorithm** parameters.
**No**: Export a data key without encrypting the data key by using a specific public key.
This way, you can directly generate a data key. After the data key is generated, you can view the ciphertext of the data key in the
**Data key export results** dialog box.
5. Optional. On the **Data Key Usage** tab, click the **Data Key Re-encryption** tab, configure
parameters, and click **Submit**.

| Transfer protection scenario | Related operation |
|---|---|
| Use public key to protect | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Encryption Context parameters. ii. In the Specify the export publicKey section, configure the Publickey Type, Public Key, and Key Algorithm parameters. |

| Data key transfer protection in the same region | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target KeyId and Target EncryptionContext parameters. |
|---|---|
| Data key transfer protection across regions | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target RegionId, Target Asymmetric KeyID, Target Asymmetric KeyVersionID, Target KeyId, and Target EncryptionContext parameters. |

After transfer protection is configured for the data key, you can view the ciphertext of the data key in the **Data key transfer protection result** dialog box.

### 3.10 Generate a CSR

To generate a certificate, you must submit a certificate signing request (CSR) to a certificate authority (CA). This topic describes how to generate a CSR.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find an asymmetric CMK whose Key Usage is
**Sign/Verify** and click its alias or choose More > **Key Details** in the **Actions** column.
The key type for asymmetric keys is RSA_2048, EC_P256, or EC_P256K.
4. On the **Key Version** tab, click **Generate CSR** in the **Actions** column.
5. In the **Generate CSR** dialog box, configure the parameters as required.
6. Click **Generate CSR**.
7. Click **Download CSR File** to save the CSR file to your on-premises machine.

## 4 Use RAM for access control

Key Management Service (KMS) integrates with Resource Access Management (RAM) to let you control who can access your KMS resources and what they can do. RAM users and RAM roles require explicit permission grants — Alibaba Cloud accounts have full access to their own resources by default. Apsara Stack tenant accounts have full operation permissions on their own resources. RAM users and roles are granted only operation permissions on specified resources.

**Resource types in KMS**

The following table describes all resource types and their Alibaba Cloud Resource Names (ARNs) in KMS. The ARNs can be used in the **Resource** parameter of a RAM policy.

| Resource type | ARN |
|---|---|
| Abstract key container | acs:kms:${region}:${account}:key |
| Abstract alias container | acs:kms:${region}:${account}:alias |
| Key | acs:kms:${region}:${account}:key/${key-id} |
| Alias | acs:kms:${region}:${account}:alias/${alias-name} |

**Actions in KMS**

KMS defines actions used in RAM policies for each API operation that requires access control. Actions must be in the kms:${api-name} format. The DescribeRegions operation does not require access control. It can be called by Apsara Stack tenant accounts, RAM users, or RAM roles after they pass RAM authentication. The following tables describe the RAM action and resource type that correspond to each KMS API operation. Key service operations

| Operation | Action | Resource type |
|---|---|---|
| ListKeys | kms:ListKeys | Abstract key container |
| CreateKey | kms:CreateKey | Abstract key container |
| DescribeKey | kms:DescribeKey | Key |

| UpdateKeyDescription | kms:UpdateKeyDescription | Key |
|---|---|---|
| EnableKey | kms:EnableKey | Key |
| DisableKey | kms:DisableKey | Key |
| ScheduleKeyDeletion | kms:ScheduleKeyDeletion | Key |
| CancelKeyDeletion | kms:CancelKeyDeletion | Key |
| GetParametersForImport | kms:GetParametersForImport | Key |
| ImportKeyMaterial | kms:ImportKeyMaterial | Key |
| DeleteKeyMaterial | kms:DeleteKeyMaterial | Key |
| ListAliases | kms:ListAliases | Abstract alias container |
| CreateAlias | kms:CreateAlias | Alias and key |
| UpdateAlias | kms:UpdateAlias | Alias and key |
| DeleteAlias | kms:DeleteAlias | Alias and key |
| ListAliasesByKeyId | kms:ListAliasesByKeyId | Key |
| CreateKeyVersion | kms:CreateKeyVersion | Key |
| DescribeKeyVersion | kms:DescribeKeyVersion | Key |
| ListKeyVersions | kms:ListKeyVersions | Key |
| UpdateRotationPolicy | kms:UpdateRotationPolicy | Key |
| Encrypt | kms:Encrypt | Key |
| Decrypt | kms:Decrypt | Key |

| ReEncrypt | kms:ReEncryptFrom kms:ReEncryptTo kms:ReEncrypt* | Key |
|---|---|---|
| GenerateDataKey | kms:GenerateDataKey | Key |
| GenerateDataKeyWithoutPlaint ext | kms:GenerateDataKeyWithout Plaintext | Key |
| ExportDataKey | kms:ExportDataKey | Key |
| GenerateAndExportDataKey | kms:GenerateAndExportDataK ey | Key |
| AsymmetricSign | kms:AsymmetricSign | Key |
| AsymmetricVerify | kms:AsymmetricVerify | Key |
| AsymmetricEncrypt | kms:AsymmetricEncrypt | Key |
| AsymmetricDecrypt | kms:AsymmetricDecrypt | Key |
| GetPublicKey | kms:GetPublicKey | Key |

Tag management operations

| Operation | Action | Resource type |
|---|---|---|
| ListResourceTags | kms:ListResourceTags | Key |
| UntagResource | kms:UntagResource | Key |
| TagResource | kms:TagResource | Key |

**Policy conditions in KMS**

In addition to global conditions, you can use tags as filters to restrict the use of cryptographic operations such as Encrypt, Decrypt, and GenerateDataKey. Filters must be in the kms:tag/${tag-key} format.

**RAM policy examples**

A RAM policy that allows users to access all KMS resources `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:*"
```

`],`

```json
      "Resource": [
        "*"
```

`]` `}` `]` `}` A RAM policy that allows users only to query keys, aliases, and permissions to use keys `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:List*", "kms:Describe*",
        "kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey"
```

`],`

```json
      "Resource": [
        "*"
```

`]` `}` `]` `}` A RAM policy that allows users to use keys that contain the following tag to perform cryptographic operations: Tag key: `Project` Tag value: `Apollo` `{`

```json
    "Version": "1",
    "Statement": [
```

`{`

```json
            "Effect": "Allow",
            "Action": [
                "kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey"
```

`],`

```json
            "Resource": [
                "*"
```

`],`

```json
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "kms:tag/Project": [
                        "Apollo"
```

`]` `}` `}` `}` `]` `}`

## 5 Use aliases

Aliases are optional to customer master keys (CMKs). Aliases must be unique within a region for each Apsara Stack tenant account. An Alibaba Stack tenant account can use the same alias across regions. An alias can be associated with only one CMK in a region, but a CMK can be associated with multiple aliases.

**Overview**

Each alias is associated with a CMK. However, aliases are independent of the CMKs that are associated with them. Aliases have the following characteristics: You can call the UpdateAlias operation to associate an alias with another CMK. This operation does not affect the original CMK. If you delete an alias, the CMK associated with the alias is not deleted. Resource Access Management (RAM) users must be authorized before they can perform operations on an alias. For more information, see Use RAM for access control. Aliases cannot be modified. To change the alias of a CMK, you must delete the original alias and create another one for the CMK. You can replace the ID of a CMK with its alias in the request parameters of the following API operations: DescribeKey Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext For more information about the API operations, see the **API reference** topic of
**Developer Guide**.
To specify an alias instead of a CMK ID in the request parameters of the preceding API operations, a RAM user must have the relevant permissions on the CMK. The RAM user does not need to have permissions on the alias. When you use an alias, you must ensure that the alias is complete. Example:

```
// A complete alias must contain the prefix "alias/". alias/example
```

**Creates an alias**

An alias must contain the `alias/` prefix. An alias, excluding the prefix, can contain letters, digits, underscores (_), hyphens (-), and forward slashes (/). An alias, excluding the prefix, must be 1 to 255 characters in length. If you create an alias for a CMK as a RAM user, make sure that a custom policy is created to grant the RAM user the required permissions. The following sample policy allows User 123456 to create an alias named `alias/example` for CMK 08ec3bb9-034f-485b-b1cd-3459baa8****: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:CreateAlias"
```

`],`

```json
      "Resource": [
        "acs:kms:cn-hangzhou:123456:key/08ec3bb9-034f-485b-b1cd-3459baa8****",
        "acs:kms:cn-hangzhou:123456:alias/example"
```

`]` `}` `]` `}` A new alias created for a CMK does not affect the existing aliases of the CMK. You can use one of the following methods to create an alias: Console: i. Log in to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Security > Key Management Service**. iii. On the **Customer Master Key** page, find the desired CMK, and click its alias or choose
**More > Key Details** in the **Actions** column.
iv. On the **Aliases** tab, click **Create Alias**. v. In the **Create Alias** dialog box, configure the Alias parameter. vi. Click **OK**. API: Call the CreateAlias operation. Alibaba Cloud CLI: Run the `aliyun kms CreateAlias` command.

```
aliyun kms CreateAlias --KeyId 08ec3bb9-034f-485b-b1cd-3459baa8**** --AliasName alias /example
```

**Reassociate an alias**

You can reassociate an existing alias with another CMK. To allow a RAM user to reassociate an existing alias with another CMK, you must create a custom policy to grant the RAM user the permissions on the original CMK, new CMK, and alias. The following sample policy allows User 123456 to reassociate an alias named `alias/example` with CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****. The original CMK associated with the alias is 08ec3bb9-034f-485b-b1cd-3459baa8****. `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:UpdateAlias"
```

`],`

```json
      "Resource": [
        "acs:kms:cn-hangzhou:123456:key/08ec3bb9-034f-485b-b1cd-3459baa8****",
        "acs:kms:cn-hangzhou:123456:key/127d2f84-ee5f-4f4d-9d41-dbc1aca2****",
        "acs:kms:cn-hangzhou:123456:alias/example"
```

`]` `}` `]` `}` You can use one of the following methods to reassociate an alias with another CMK: API: Call the UpdateAlias operation. Alibaba Cloud CLI: Run the `aliyun kms UpdateAlias` command.

```
aliyun kms UpdateAlias --AliasName alias/example --KeyId 127d2f84-ee5f-4f4d-9d41-dbc1 aca2****
```

**Delete an alias**

You can delete an alias that is no longer needed. After you delete an alias, the CMK associated with the alias is not deleted. If you use a RAM user to delete an alias, make sure that a custom policy is created to grant the RAM user the required permissions. The following sample policy allows User 123456 to delete an alias named `alias/example` from CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:DeleteAlias"
```

`],`

```json
      "Resource": [
        "acs:kms:cn-hangzhou:123456:key/127d2f84-ee5f-4f4d-9d41-dbc1aca2****",
        "acs:kms:cn-hangzhou:123456:alias/example"
```

`]` `}` `]` `}` You can use one of the following methods to delete an alias: Console: i. Log in to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Security > Key Management Service**. iii. On the **Customer Master Key** page, find the desired CMK, and click its alias or choose
**More > Key Details** in the **Actions** column.
iv. On the **Aliases** tab, click **Delete Alias** in the Actions column of the alias you want to delete. v. In the **Delete Alias** message, click **OK**. API: Call the DeleteAlias operation. Alibaba Cloud CLI: Run the `aliyun kms DeleteAlias` command.

```
aliyun kms DeleteAlias --AliasName alias/example
```

**Query aliases**

You can query all aliases that belong to your Apsara Stack tenant account in the current region. To allow a RAM user to query aliases, you must create a custom policy to grant the RAM user the permissions on aliases. The following sample policy allows User 123456 to query all aliases in a region: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:ListeAliases"
```

`],`

```json
      "Resource": [
        "acs:kms:cn-hangzhou:123456:alias"
```

`]` `}` `]` `}` You can use one of the following methods to query aliases: API: Call the ListAliases operation. Alibaba Cloud CLI: Run the `aliyun kms ListAliases` command.

```
aliyun kms ListAliases
```

**Query the aliases of a CMK**

If you query the aliases of a CMK, only the related aliases are returned. To allow a RAM user to query the aliases of a CMK, you must create a custom policy to grant the RAM user the permissions on the CMK. The following sample policy allows User 123456 to query the aliases of CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****: `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "kms:ListAliasesByKeyId"
```

`],`

```json
      "Resource": [
        "acs:kms:cn-hangzhou:123456:key/127d2f84-ee5f-4f4d-9d41-dbc1aca2****"
```

`]` `}` `]` `}` You can use one of the following methods to query the aliases of a CMK: API: Call the ListAliasesByKeyId operation. Alibaba Cloud CLI: Run the `aliyun kms ListAliasesByKeyId` command.

```
aliyun kms ListAliasesByKeyId --KeyId 127d2f84-ee5f-4f4d-9d41-dbc1aca2****
```

## 6 Customer master key

Key Management Service (KMS) is a core service that provides fully managed keys and protection capabilities. It lets you encrypt data and create digital signatures by using simple, cloud-native APIs.

**Key algorithms**

The following table lists the cryptographic algorithms KMS supports.

| Algorithm family | Algorithm type | Encryption and decryption | Signing and verification |
|---|---|---|---|
| Symmetric key | AES | Supported | Not supported |
| Asymmetric key | RSA | Supported | Supported |
| Asymmetric key | ECC | Not supported | Supported |

Symmetric keys are primarily used for data encryption. If you do not specify a KeySpec, KMS creates a symmetric key by default. You can use KMS APIs for encryption and decryption without exposing the plaintext key material. For more information, see **Use symmetric keys**
**>** **Symmetric encryption**.
Asymmetric keys can be used for data encryption and digital signatures. An asymmetric customer master key (CMK) created in KMS consists of a public and private key pair. The public key can be distributed to anyone, while the private key must be kept secure. KMS protects the private key and provides no API to export it. You can use the private key through KMS APIs to decrypt data or create digital signatures. Anyone with the public key can encrypt data or verify signatures created with the private key. For more information, see **Use**
**asymmetric keys >** **Asymmetric keys**.

**Key owners**

Typically, you are the owner of a customer master key in KMS. In this case, the Creator attribute of the key is your Alibaba Cloud account ID. When a cloud service integrates with KMS for server-side encryption, KMS allows the service to automatically manage an encryption key on your behalf. This simplifies data encryption and reduces the overhead of managing the key lifecycle and permissions. A key managed by a cloud service is called a service key. To help you identify them, the Creator attribute of a service key is set to the cloud service's code, and the key is assigned a special alias in the format `acs/<product_code>` . For example, a service key for Object Storage Service (OSS) has OSS as its Creator attribute and is assigned the alias acs/oss.

## 7 Use symmetric keys

### 7.1 Symmetric encryption

Symmetric encryption is the most common method for data protection. Key Management Service (KMS) provides easy-to-use API operations to encrypt and decrypt data in the cloud. For details about API operations, see the **API Reference** chapter in the **Developer**
**Guide**.
If you do not specify a key specification (KeySpec), KMS creates a symmetric key by default. Alibaba Cloud supports mainstream symmetric key algorithms and provides robust security.

**Types of symmetric keys**

KMS supports the following types of symmetric key algorithms:

| Algorithm | Key length | Key specification | Data encryption mode | Protection level |
|---|---|---|---|---|
| AES | 256-bit | Aliyun AES 256 _ _ | GCM | Software |

**Encryption and decryption features**

When you encrypt data, you only need to specify the identifier or alias of the master key. KMS uses the specified master key to encrypt the data and returns the ciphertext. When you call the `Decrypt` operation, you only need to provide the ciphertext; the master key identifier is not required. This applies to ciphertext generated by the `Encrypt` , `GenerateDataKey` , and `GenerateDataKeyWithoutPlaintext` operations.

**Using additional authenticated data**

Symmetric keys in KMS use Galois/Counter Mode (GCM), which supports providing additional authenticated data (AAD) for enhanced integrity protection. KMS encapsulates this process, simplifying the use of custom authenticated data. For more information, see EncryptionContext.

**Envelope encryption**

KMS provides the `GenerateDataKey` and `GenerateDataKeyWithoutPlaintext` API operations. These operations generate a two-level key hierarchy in a single call, which helps you implement envelope encryption more quickly. For details about envelope encryption, see the **Product White Paper**, specifically the
**Product Features** chapter's section on **Envelope Encryption Service**.

**Rotating symmetric keys**

Symmetric customer master keys (CMKs) in KMS support multiple key versions and automatic key rotation. You can set a custom key rotation policy. When a CMK has multiple versions, encryption operations, such as `Encrypt` , `GenerateDataKey` , and `GenerateDataKeyWithoutPlaintext` , use the latest key version of the specified CMK to encrypt data. For decryption, you do not need to provide the CMK identifier or the key version identifier. KMS automatically detects the correct CMK and key version from the ciphertext, then uses that version's key material for decryption. Automatic key rotation works by creating a new key version. After rotation, ciphertext generated by KMS API calls automatically uses the latest version. Ciphertext generated before the rotation can still be decrypted using the older key versions. For more information, see Automatic key rotation.

**Bring your own key (BYOK)**

To meet stricter security and compliance requirements, KMS supports bring your own key (BYOK). This feature lets you import your own keys to protect your data in the cloud.

### 7.2 EncryptionContext

EncryptionContext is a JSON string that may be used in KMS API operations, such as Encrypt, GenerateDataKey, and Decrypt.

**Roles of EncryptionContext**

EncryptionContext is a JSON string, and it must be in the string:string format. EncryptionContext is used to ensure data integrity. If this parameter is specified during encryption, you must specify an equivalent EncryptionContext value for decryption. You can call the Encrypt or GenerateDataKey operation for encryption and call the Decrypt operation for decryption. EncryptionContext is related to decryption, but EncryptionContext is not included in ciphertext that is specified by the CipherBlob parameter.

**Valid values of EncryptionContext**

A valid value of EncryptionContext is a JSON string of up to 8,192 characters in the string:string format. When you specify EncryptionContext for an API operation, take note of the escape characters. Sample valid EncryptionContext:

```json
{"ValidKey":"ValidValue"} {"Key1":"Value1","Key2":"Value2"}
```

Sample invalid EncryptionContext:

```json
[{"Key":"Value"}] // JSON array {"Key":12345} //String-int {"Key":["value1","value2"]} // String:Array
```

**Equivalent EncryptionContext**

EncryptionContext is a map or hash table in the string:string format. When EncryptionContext is used as a parameter, two values of the EncryptionContext parameter are considered to be equivalent if their key-value pairs are consistent. If EncryptionContext is specified during encryption, you can specify an equivalent EncryptionContext value to decrypt the ciphertext. The sequences of the key-value pairs of two EncryptionContext values can be different. Sample equivalent EncryptionContext values:

```json
{"Key1":"Value1","Key2":"Value2"} is equivalent to {"Key2":"Value2","Key1":"Value1"}.
```

### 7.3 Import and delete key material

**material**

This topic describes how to import and delete external key material.

**Background information**

A customer master key (CMK) is a fundamental resource in Key Management Service (KMS). A CMK consists of a key ID, basic metadata such as the key status, and the key material used to encrypt and decrypt data. By default, KMS generates the key material when you call the CreateKey operation to create a CMK. You can also create a key and specify its key material source as external. In this case, KMS does not generate key material for the CMK. You can import your own key material into the CMK. You can call the DescribeKey operation to check the key material source. For more information about API operations, see the **API Reference** and the **Developer**
**Guide**.
Keys are classified as ordinary keys or external keys based on the key material source: When the **Origin** parameter of KeyMetadata is set to Aliyun_KMS, it means that the key material is generated by KMS and the key is called an **ordinary key**. When **Origin** is EXTERNAL, it indicates that the key material is imported from an external source, and the key is known as an **external key**. When using imported key material, note the following: Generate your key material from a random source that meets your security requirements. You are responsible for the durability of your key material. KMS ensures the high availability of imported key material, but cannot guarantee the same durability as KMS-generated key material. You can immediately delete imported key material by calling the DeleteKeyMaterial operation. You can also set an expiration time for the key material to delete it automatically (the CMK is not deleted). In contrast, key material generated by KMS cannot be deleted directly. You can only delete it along with its CMK after a 7- to 30-day waiting period by calling the ScheduleKeyDeletion operation. After imported key material is deleted, you can re-import the same key material to reactivate the CMK. Therefore, you are responsible for maintaining a secure copy of your key material. A CMK can be associated with only one specific key material. When you import key material into a CMK, the CMK is permanently bound to that key material. You cannot import different key material into the CMK, even if the original key material expires or is deleted. If you need to rotate a CMK that uses external key material, you must create a new CMK and import the new key material. CMKs are independent. For example, data encrypted by one CMK cannot be decrypted by another CMK, even if both CMKs use the same key material. You can import only a 256-bit symmetric key as key material.

**Import key material**

1. Create an external key.
You can create an external key in one of the following two ways: Method 1: In the console, expand the Advanced Options section and set Key Material Source to External when you create a key. Method 2: Call the CreateKey API operation and set the **Origin** parameter to EXTERNAL.

```
./aliyun --skip-secure-verify --region ${please-replace-your-region} --endpoint $ {please-replace-your-endpoint} --access-key-id ${please-replace-your-access-key-id} --access-key-secret ${please-replace-your-access-key-secret} kms CreateKey --Origi n EXTERNAL --Description "External key"
```

2. Get the import parameters.
The import parameters include a public key for encrypting your key material and an import token. You can get the import parameters in one of the following two ways: Method 1: Get the import parameters in the console. Method 2: Call the GetParametersForImport operation to get the import parameters.

```
./aliyun --skip-secure-verify --region ${please-replace-your-region} --endpoint $ {please-replace-your-endpoint} --access-key-id ${please-replace-your-access-key-id} --access-key-secret ${please-replace-your-access-key-secret} kms GetParametersForImport --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --WrappingAlgor ithm RSAES_OAEP_SHA_1 --WrappingKeySpec RSA_2048
```

3. Import the key material.
You can import key material into a new external key, or re-import key material that has expired or been deleted. You can also use this operation to reset the expiration time of the key material. An import token can only be used for the CMK it was generated for. The import token is valid for 24 hours. You can use it multiple times within this period. After it expires, you must request a new import token and public key. i. Encrypt your key material by using the public key. The public key is a 2048-bit RSA key. The encryption algorithm you use must match the one specified when you requested the import parameters. The API returns the public key in Base64-encoded format, so you must decode it before use. KMS currently supports the `RSAES_OAEP_SHA_256` , `RSAES_OAEP_SHA_1` , and `RSAES_PKCS1_V1_5` encryption algorithms. ii. Base64-encode the encrypted key material. iii. Call the ImportKeyMaterial operation with the Base64-encoded key material and the import token.

```
./aliyun --skip-secure-verify --region ${please-replace-your-region} --endpoint $ {please-replace-your-endpoint} --access-key-id ${please-replace-your-access-key-id} --access-key-secret ${please-replace-your-access-key-secret} kms ImportKeyMaterial --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --EncryptedKeyMaterial xxx --ImportTok en xxxx
```

**Delete key material**

After you import key material, you can use an external key in the same way you use an ordinary key. Unlike ordinary keys, the key material of an external key can expire or be deleted directly. If the key material expires or is deleted, the key becomes unusable, and you cannot decrypt ciphertext that was encrypted by the key unless you re-import the same key material. If a key is in the pending deletion state when its key material expires or is deleted, the key status remains unchanged. Otherwise, the key status changes to pending import. You can delete key material in one of the following two ways: Method 1: Delete the key material in the console. Method 2: Call the DeleteKeyMaterial operation to delete the key material.

```
./aliyun --skip-secure-verify --region ${please-replace-your-region} --endpoint ${p lease-replace-your-endpoint} --access-key-id ${please-replace-your-access-key-id} --a ccess-key-secret ${please-replace-your-access-key-secret} kms DeleteKeyMaterial --Key Id 1339cb7d-54d3-47e0-b595-c7d3dba8****
```

**Encrypt and import key material using OpenSSL**

1. Create an external key.
2. Create the key material.
The key material must be a 256-bit symmetric key. This example uses OpenSSL to generate a 32-byte random value for demonstration.

```
openssl rand -out KeyMaterial.bin 32
```

3. Get the import parameters.
4. Encrypt the key material.
i. Base64-decode the public key. ii. Encrypt the key material by using the specified encryption algorithm. This example uses

```
 RSAES_OAEP_SHA_1 .
```

iii. Base64-encode the encrypted key material and save it to a text file.

```
openssl rand -out KeyMaterial.bin 32 openssl enc -d -base64 -A -in PublicKey_base64.txt -out PublicKey.bin openssl rsautl -encrypt -in KeyMaterial.bin -oaep -inkey PublicKey.bin -keyform DE R -pubin -out EncryptedKeyMaterial.bin openssl enc -e -base64 -A -in EncryptedKeyMaterial.bin -out EncryptedKeyMaterial_base64.txt
```

iv. Import the encrypted key material and the import token.

**Usage example**

Encrypt and import key material using the Java SDK.

```java
// Use the latest KMS Java SDK. // KmsClient.java import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; importcomaliyuncskmsmodelv20160120*;
```

```java
import com.aliyuncs.kms.model.v20160120.*; import com.aliyuncs.profile.DefaultProfile; // KMS API wrapper. public class KmsClient {
    DefaultAcsClient client;
    public KmsClient(String regionId, String ak, String secret) {
        DefaultProfile profile = DefaultProfile.getProfile(regionId, ak, secret);
        this.client = new DefaultAcsClient(profile);
```

`}`

```
    // Use a custom endpoint. This is typically required when you access a VPC endpoint
or in a private cloud where the region ID cannot be resolved to an endpoint address.
    public KmsClient(String regionId, String ak, String secret, String endpoint) {
        DefaultProfile.addEndpoint(regionId, "kms", endpoint);
        DefaultProfile profile = DefaultProfile.getProfile(regionId, ak, secret);
        this.client = new DefaultAcsClient(profile);
```

`}`

```
    public CreateKeyResponse createKey() throws Exception {
        CreateKeyRequest request = new CreateKeyRequest();
        request.setOrigin("EXTERNAL"); // Create an external key.
        return this.client.getAcsResponse(request);
```

`}`

```
    public GetParametersForImportResponse getParametersForImport(String keyId, String w
rappingKeySpec, String wrappingAlgorithm) throws ClientException {
        GetParametersForImportRequest request = new GetParametersForImportRequest();
        request.setAcceptFormat(FormatType.JSON);
        request.setKeyId(keyId);
        request.setWrappingKeySpec(wrappingKeySpec);
        request.setWrappingAlgorithm(wrappingAlgorithm);
        return this.client.getAcsResponse(request);
```

`}`

```java
    public ImportKeyMaterialResponse importKeyMaterial(String keyId, String
importToken, String encryptedKeyMaterial, Long expireTimestamp) throws ClientException
```

`{`

```
        ImportKeyMaterialRequest request = new ImportKeyMaterialRequest();
        request.setAcceptFormat(FormatType.JSON);
        request.setKeyId(keyId);
        request.setImportToken(importToken);
        request.setEncryptedKeyMaterial(encryptedKeyMaterial);
        request.setKeyMaterialExpireUnix(expireTimestamp);
        return this.client.getAcsResponse(request);
```

`}`

```
    // ... Omitted. Other API operations are similar.
```

`}`

```java
// example.java import com.aliyuncs.kms.model.v20160120.*; importjavax.crypto.Cipher;
```

```java
import javax.crypto.Cipher; import javax.crypto.spec.OAEPParameterSpec; import javax.crypto.spec.PSource.PSpecified; import javax.xml.bind.DatatypeConverter; import java.security.KeyFactory; import java.security.PublicKey; import java.security.spec.MGF1ParameterSpec; import java.security.spec.X509EncodedKeySpec; import java.util.Random; public class CreateAndImportExample {
    public static void main(String[] args) {
        String regionId = "cn-hangzhou"; // China (Hangzhou)
        String accessKeyId = "*** Provide your AccessKeyId ***";
        String accessKeySecret = "*** Provide your AccessKeySecret ***";
        KmsClient kmsclient = new KmsClient(regionId, accessKeyId, accessKeySecret);
        //String endpoint = "*** VPC Endpoint ***";
        //KmsClient kmsclient = new KmsClient(regionId, accessKeyId, accessKeySecret, e
ndpoint);
        // Create an external key.
        try {
            CreateKeyResponse keyResponse = kmsclient.createKey();
            String keyId = keyResponse.getKeyMetadata().getKeyId();
            // Generate a 32-byte random value.
            byte[] keyMaterial = new byte[32];
            new Random().nextBytes(keyMaterial);
            // Get the parameters for importing key material.
            GetParametersForImportResponse paramResponse =
kmsclient.getParametersForImport(keyId, "RSA_2048", "RSAES_OAEP_SHA_256");
            String importToken = paramResponse.getImportToken();
            String encryptPublicKey = paramResponse.getPublicKey();
            // Base64-decode the public key.
            byte[] publicKeyDer =
DatatypeConverter.parseBase64Binary(encryptPublicKey);
            // Parse it into an RSA public key.
            KeyFactory keyFact = KeyFactory.getInstance("RSA");
            X509EncodedKeySpec spec = new X509EncodedKeySpec(publicKeyDer);
            PublicKey publicKey = keyFact.generatePublic(spec);
            // Encrypt the key material.
            Cipher oaepFromAlgo = Cipher.getInstance("RSA/ECB/OAEPWithSHA-
1AndMGF1Padding");
            String hashFunc = "SHA-256";
            OAEPParameterSpec oaepParams = new OAEPParameterSpec(hashFunc, "MGF1", new
MGF1ParameterSpec(hashFunc), PSpecified.DEFAULT);
            oaepFromAlgo.init(Cipher.ENCRYPT_MODE, publicKey, oaepParams);
            byte[] cipherDer = oaepFromAlgo.doFinal(keyMaterial);
            // Base64-encode the encrypted key material.
            String encryptedKeyMaterial =
DatatypeConverter.printBase64Binary(cipherDer);
            // Import the key material.
            Long expireTimestamp = 1546272000L; // Unix timestamp, accurate to the
second. A value of 0 means the key material never expires.
            kmsclient.importKeyMaterial(keyId, importToken, encryptedKeyMaterial,
expireTimestamp);
        } catch (Exception e) {
```

```
            // ... Omitted.
```

`}` `}` `}`

## 8 Use asymmetric keys

### 8.1 Asymmetric keys

Compared to symmetric encryption, asymmetric keys are typically used between systems with different trust levels to generate and verify digital signatures or to encrypt and transmit sensitive information. You can create an asymmetric customer master key in KMS. An asymmetric key consists of a mathematically related public key and private key pair. The public key can be distributed to anyone, but the private key must be protected and restricted to trusted parties. KMS supports mainstream asymmetric key algorithms and provides robust security for data encryption and digital signatures.

**Types of asymmetric keys**

KMS supports the following types of asymmetric key algorithms:

| Algorithm | Key spec | Description | Purpose |
|---|---|---|---|
| RSA | RSA 2048 _ | RSA asymmetric cryptography | Data encryption and decryption Digital signatures |
| ECC | EC P256: The P-256 curve _ recommended by NIST EC P256K: The secp256k1 _ curve from SECG | Elliptic Curve Cryptography | Digital signatures |

**Data encryption**

When used for data encryption, asymmetric keys are ideal for transmitting sensitive information. A typical scenario includes the following steps:
1. The recipient distributes the public key to the sender.
2. The sender uses the public key to encrypt the sensitive information.
3. The sender transmits the ciphertext to the recipient.
4. The recipient uses the private key to decrypt the ciphertext.
Because only the recipient possesses the private key for decryption, this process prevents the plaintext from being intercepted by malicious actors during transmission. This method of transmitting sensitive information is widely used in various key exchange scenarios, such as exchanging a session key in TLS or importing and exporting encrypted keys between different hardware security modules. For more information, see Asymmetric data encryption and decryption.

**Digital signatures**

A more common use for asymmetric keys is creating a digital signature, which involves using a private key to sign a message or information. Because the private key is strictly protected and only available to the trusted holder, verifying the signature with the public key achieves the following:
**integrity**: A mismatch between the data and the signature indicates that the data may
have been tampered with.
**authenticity**: If the signature is invalid for the message, the sender is not the legitimate
holder of the private key.
**non-repudiation**: If the data and signature match, the signer cannot deny having signed
the message. A typical signature and verification scenario is as follows:
1. The signer distributes the public key for verification to the message recipient.
2. The signer uses the private key to generate a signature for the data.
3. The signer sends the data and the signature to the recipient.
4. After receiving the data and signature, the recipient uses the public key to verify the
signature for the data. Digital signatures are widely used in applications such as data tamper-proofing and identity authentication. For more information, see Asymmetric digital signatures.

**Key versions**

Due to the specific use cases of public-private key pairs, KMS does not support automatic rotation for asymmetric customer master keys. You can call the CreateKeyVersion API operation to create a new key version for a specified customer master key. This operation generates a new public and private key pair. If you use the new version for digital signatures or data encryption, you must redistribute the new public key. Additionally, unlike symmetric customer master keys, asymmetric customer master keys do not have the concept of a primary version (PrimaryKeyVersion). Therefore, when you call an API for an asymmetric cryptographic operation, you must specify both the identifier (or alias) of the customer master key and the key version.

**Public key operations**

In most cases involving public key encryption and signature verification, you can call the GetPublicKey API operation to retrieve the public key and then distribute it to its users. The users can then perform computations locally within their applications by using common cryptographic libraries such as OpenSSL or Java JCE. KMS also provides the AsymmetricEncrypt and AsymmetricVerify API operations for public key operations. Compared to performing local computations with the public key in your application, calling the KMS API operations allows you to easily log all calls and use Resource Access Management (RAM) to control the public key's usage. This helps you meet specific compliance or security requirements.

**Private key operations**

You can use a private key for data decryption or digital signatures only by calling the AsymmetricDecrypt and AsymmetricSign API operations provided by KMS.

### 8.2 Asymmetric data encryption and decryption

**and decryption**

This topic explains how to use the CLI to encrypt and decrypt data with an asymmetric CMK. An asymmetric encryption and decryption workflow typically involves these steps:
1. The recipient distributes the public key to the sender.
2. The sender uses the public key to encrypt sensitive information.
3. The sender transmits the ciphertext to the recipient.
4. The recipient uses the private key to decrypt the ciphertext.

**Before you begin**

Call the CreateKey operation to create an asymmetric key of an appropriate type in Key Management Service (KMS). Specify the key type by using the KeySpec parameter and set the KeyUsage parameter to `ENCRYPT/DECRYPT` . Create an RSA encryption key:

```
aliyun kms CreateKey --KeySpec=RSA_2048 --KeyUsage=ENCRYPT/DECRYPT -- ProtectionLevel=HSM
```

**Get the public key**

1. Call the GetPublicKey operation to get the public key.

```
aliyun kms GetPublicKey --KeyId=**** --KeyVersionId=****
```

The following response is returned: `{`

```json
        "RequestId": "82c383eb-c377-4mf6-bxx8-81hkc1g5g7ab",
        "KeyId": "****",
        "KeyVersionId": "****",
        "PublicKey": "PublicKey-DataBlob"
```

`}`
2. Save the public key to a file named rsa_publickey.pub. In the following command, replace
the PublicKey-DataBlob placeholder with the PublicKey value from the response.

```
echo PublicKey-DataBlob > rsa_publickey.pub
```

**Encrypt data with the public key**

1. Create a sample plaintext file named plaintext-file.txt that contains "this is plaintext":

```
echo "this is plaintext" > plaintext-file.txt
```

2. Use OpenSSL to encrypt the file and save the binary ciphertext to plaintext-file.enc:

```
openssl pkeyutl -encrypt -in plaintext-file.txt \
  -inkey rsa_publickey.pub -pubin \
  -pkeyopt rsa_padding_mode:oaep \
  -pkeyopt rsa_oaep_md:sha256 \
  -pkeyopt rsa_mgf1_md:sha256 \
  -out plaintext-file.enc
```

**Call KMS to decrypt data**

Call the AsymmetricDecrypt operation to decrypt the data. KMS uses the corresponding private key for the decryption.
1. Before you transmit the ciphertext over a network, you must Base64-encode it.

```
openssl base64 -in plaintext-file.enc
```

Expected output:

```
5kdCB06HHeAwgfH9ARY4/9Nv5vlpQ94GXZcmaC9FE59Aw8v8RYdozT6ggSbyZbi+ 8STKVq9402MEfmUDmwJLuu0qgAZsCe5wU4JWHh1y84Qn6HT068j0qOy5X2HIlrjs fCdetgtMtVorSgb3bbERk2RV67nHWrDkecNbUaz+6ik4AlZxv2uWrV62eQ9yUBYm Jb956LbqnfWdCFxUSHH/qB5QCnLpijzvPmfNlZr653H4nF08gpZjnmlF4FjTu3i2 mGLzK4J3Rh/l7PQHiVMdc4hSnXosg68QmMVdZBGLK9/cD9SYngPDiirU7z0q7Git dIeloyCAUDFyuQC6a+SqzA==
```

2. Pass the Base64-encoded ciphertext to KMS to decrypt the data.

```
aliyun kms AsymmetricDecrypt \
  --KeyId 5c438b18-05be-40ad-b6c2-3be6752c**** \
  --KeyVersionId 2ab1a983-7072-4bbc-a582-584b5bd8**** \
  --Algorithm RSAES_OAEP_SHA_256 \
  --CiphertextBlob
5kdCB06HHeAwgfH9ARY4/9Nv5vlpQ94GXZcmaC9FE59Aw8v8RYdozT6ggSbyZbi+8STKVq9402MEfmUDmwJLuu0 AZsCe5wU4JWHh1y84Qn6HT068j0qOy5X2HIlrjsfCdetgtMtVorSgb3bbERk2RV67nHWrDkecNbUaz+6ik4AlZx uWrV62eQ9yUBYmJb956LbqnfWdCFxUSHH/qB5QCnLpijzvPmfNlZr653H4nF08gpZjnmlF4FjTu3i2mGLzK4J3R l7PQHiVMdc4hSnXosg68QmMVdZBGLK9/cD9SYngPDiirU7z0q7GitdIeloyCAUDFyuQC6a+SqzA==
```

Expected output: `{`

```json
        "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
        "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
        "Plaintext": "dGhpcyBpcyBwbGFpbnRleHQgDQo=",
        "RequestId": "6be7a8e4-35b9-4549-ad05-c5b1b535a22c"
```

`}`
3. The Plaintext value in the response is Base64-encoded. Base64-decode it to retrieve the
original plaintext.

```
echo dGhpcyBpcyBwbGFpbnRleHQgDQo= | openssl base64 -d
```

The command returns the original plaintext:

```
this is plaintext
```

### 8.3 Asymmetric digital signature

This topic demonstrates how to use the ALIYUN CLI with an asymmetric CMK to generate and verify a digital signature. You can also perform these operations by using the KMS SDK. An asymmetric signing scenario typically includes the following steps:
1. The signer distributes the public key to the message receiver.
2. The signer uses the private key to generate a signature for the data.
3. The signer sends the data and the signature to the message receiver.
4. The message receiver uses the public key to verify the signature against the data.

**Before you begin**

Call the CreateKey operation to create an asymmetric key of the appropriate type in KMS. You must set the KeySpec parameter and specify `SIGN/VERIFY` for the KeyUsage parameter. To create an RSA signing key:

```
aliyun kms CreateKey --KeySpec=RSA_2048 --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

To create a NIST P-256 signing key:

```
aliyun kms CreateKey --KeySpec=EC_P256 --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

To create a secp256k1 signing key:

```
aliyun kms CreateKey --KeySpec=EC_P256K --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

**Calculate the message digest**

For both RSA and ECC signing, you must first calculate a digest of the message. The signing operation is then performed on this digest. The algorithm used to generate the digest must match the signing algorithm specified when you call KMS. For example, the ECDSA_SHA_256 signing algorithm requires a SHA- 256 digest. If you use the SHA-384 algorithm to create the digest, it will be incompatible with ECDSA_SHA_256. The examples in this topic use the SHA-256 digest algorithm.
1. Save the message to be signed, "this is message", in the message-file.txt file:

```
echo "this is message" > message-file.txt
```

2. Calculate the SHA-256 digest of the message, and save the binary digest to the file
message-sha256.bin:

```
openssl dgst -sha256 -binary -out message-sha256.bin message-file.txt
```

**Call KMS to generate the signature**

Call the KMS API to use the private key and generate a signature for the message digest.
1. Base64-encode the message digest before sending it over the network:

```
openssl base64 -in message-sha256.bin
```

The Base64-encoded digest is as follows:

```
uCx5YpLfBrqoYMP8Hf9H7j9/1zT+PPxq1qJRW6uQbos=
```

2. Pass the Base64-encoded digest to KMS to generate the signature.
The required parameters and resulting signature depend on the key and signing algorithm. In the following examples, each generated signature is saved to a separate file.

**RSASSA-PSS**

To sign with an RSA key using the RSASSA-PSS algorithm and a SHA-256 digest, run the following ALIYUN CLI command:

```
aliyun kms AsymmetricSign --KeyId=**** --KeyVersionId=**** \
    --Algorithm=RSA_PSS_SHA_256 --Digest=hRP2cu...
```

`{`

```json
        "KeyId": "****",
        "KeyVersionId": "****",
        "Value": "J7xmdnZ...",
        "RequestId": "70f78da9-c1b6-4119-9635-0ce4427cd424"
```

`}` Base64-decode the signature result Value and output the binary signature to the file rsa_pss_signature.bin:

```
echo J7xmdnZ... | openssl base64 -d -out rsa_pss_signature.bin
```

**RSASSA_PKCS1_V1_5**

To sign with an RSA key using the RSASSA_PKCS1_V1_5 algorithm and a SHA-256 digest, run the following ALIYUN CLI command:

```
aliyun kms AsymmetricSign --KeyId=**** --KeyVersionId=**** \
    --Algorithm=RSA_PKCS1_SHA_256 --Digest=hRP2cu...
```

`{`

```json
        "KeyId": "****",
        "KeyVersionId": "****",
        "Value": "qreBkH/u...",
        "RequestId": "4be57288-f477-4ecd-b7be-ad8688390fbc"
```

`}`

| e64-decode the | Value | of |
|---|---|---|
| rsa pkcs1 signature.bin _ _ |   |   |

Base64-decode the `Value` of the signature result and output the binary signature to

```
echo qreBkH/u... | openssl base64 -d -out rsa_pkcs1_signature.bin
```

**NIST P-256**

To sign with a NIST P-256 key using the ECDSA algorithm and a SHA-256 digest, run the following ALIYUN CLI command:

```
aliyun kms AsymmetricSign --KeyId=**** --KeyVersionId=**** \
    --Algorithm=ECDSA_SHA_256 --Digest=hRP2cu...
```

`{`

```json
        "KeyId": "****",
        "KeyVersionId": "****",
        "Value": "MEYCIQD33Y98...",
        "RequestId": "472d789c-d4be-4271-96bb-367f7f0f8ec3"
```

`}` Base64-decode the signature result Value and output the binary signature to the ec_p256_signature.bin file:

```
echo MEYCIQD33Y98... | openssl base64 -d -out ec_p256_signature.bin
```

**secp256k1**

To sign with a secp256k1 key, run the following ALIYUN CLI command:

```
aliyun kms AsymmetricSign --KeyId=**** --KeyVersionId=**** \
    --Algorithm=ECDSA_SHA_256 --Digest=hRP2cu...
```

`{`

```json
        "KeyId": "****",
        "KeyVersionId": "****",
        "Value": "MEYCIQDWuuI...",
        "RequestId": "fe41abed-91e7-4069-9f6b-0048f5bf4de5"
```

`}`

| Base64-decode the | Value |   |
|---|---|---|
| ec p256k signature.bin _ _ |   |   |
|   |   | fi |

Base64-decode the `Value` of the signature result and save the binary signature to the

```
echo MEYCIQDWuuI... | openssl base64 -d -out ec_p256k_signature.bin
```

**Get the public key**

Retrieve the public key for your asymmetric key from KMS. The following examples assume the public keys are saved to the files listed below:

**Verify the signature**

Use the following commands to verify the signature for each key type and algorithm:

**RSASSA-PSS**

```
openssl dgst \
    -verify rsa_publickey.pub \
    -sha256 \
    -sigopt rsa_padding_mode:pss \
    -sigopt rsa_pss_saltlen:-1 \
    -signature rsa_pss_signature.bin \
    message-file.txt
```

**RSASSA_PKCS1_V1_5**

```
openssl dgst \
    -verify rsa_publickey.pub \
    -sha256 \
    -signature rsa_pkcs1_signature.bin \
    message-file.txt
```

**NIST P-256**

```
openssl dgst \
    -verify ec_p256_publickey.pub \
    -sha256 \
    -signature ec_p256_signature.bin \
    message-file.txt
```

**secp256k1**

```
openssl dgst \
    -verify ec_p256k_publickey.pub \
    -sha256 \
    -signature ec_p256k_signature.bin \
    message-file.txt
```

A successful verification returns the following output:

```
Verified OK
```

## 9 Rotate CMKs

### 9.1 Overview

Keys are used to protect specific data. Therefore, the security of the data depends on the security of its keys. You can regularly rotate keys between key versions to improve key security and implement security policies and best practices for data protection.

**Achieve security goals**

You can regularly rotate keys to achieve the following goals: Reduce the amount of data encrypted based on each key The security of a key is inversely proportional to the amount of data encrypted based on the key. This amount is usually defined by the total bytes of data or the total number of messages that are encrypted based on the same key. For example, National Institute of Standards and Technology (NIST) defines the secure lifecycle of a key in Galois/Counter Mode (GCM) as the total number of messages encrypted based on the key. Regular key rotation allows each key to remain secure and minimizes vulnerability to cryptanalytic attacks. Respond in advance to security events In the early days of system design, key rotation was introduced as a routine operations and maintenance (O&M) method. This provides the system with a method to handle security events when they occur, and complies with the fail early, fail often principle of software engineering. If key rotation is not executed in the system until an emergency event has already occurred, the probability of system failure increases exponentially. Provide logical isolation of data Data encrypted before a key rotation is isolated from data encrypted after the key rotation. The impact of key-related security events can be identified and preventive measures can be taken. Reduce the window of time to crack keys Regular rotation of encryption keys ensures that you can control and reduce the window of time during which the key and its encrypted data are vulnerable to being cracked. The interval between rotation tasks during which attackers are able to crack the key is limited. This practice greatly increases the security of your data against cryptanalytic attacks.

**Meet the requirements of regulatory compliance**

Regular key rotation facilitates compliance with various regulations, which include but are not limited to the following regulations: Payment Card Industry Data Security Standard (PCI DSS) Cryptography-related industrial standards issued by State Cryptography Administration, such as GM/T 0051-2016 Cryptography-related standards issued by NIST, such as NIST Publication 800-38D

### 9.2 Automatic key rotation

This topic describes how to enable automatic rotation for a customer master key (CMK) in Key Management Service (KMS).

**Key versions**

A CMK in KMS supports multiple key versions. Each key version is generated independently, and different versions of the same CMK are not cryptographically related. KMS performs automatic rotation by creating a new key version. A CMK has two types of key versions: Primary key version A primary key version is the active encryption key of a CMK. At any point in time, each CMK has exactly one primary key version. When you call an encryption API, such as GenerateDataKey or Encrypt, KMS uses the primary key version of the specified CMK to encrypt the plaintext. You can view the **PrimaryKeyVersion** property in the response returned by DescribeKey. Non-primary key version A non-primary key version is an inactive encryption key of a CMK. A CMK can have zero or more non-primary key versions. A non-primary key version is a previous primary key version. When key rotation creates a new primary key version, KMS does not delete or disable the previous versions. These non-primary key versions are required to decrypt data that was previously encrypted. Encryption APIs use the primary key version of the specified CMK. Decryption APIs use the specific key version that corresponds to the provided ciphertext. There are two ways to generate a new key version: Create a CMK Call CreateKey to create a CMK. If you set the **Origin** parameter to Aliyun_KMS, KMS generates the initial key version and sets it as the primary key version. For more information about the CreateKey operation, see **API Reference > Key**
**management > CreateKey** in the Key Management Service developer guide.
Automatic rotation You can configure an automatic rotation policy for a CMK. KMS executes this policy at specified intervals to create new key versions.

**Automatic rotation**

**Configure rotation policy**

You can specify an automatic rotation policy when creating a CMK with the CreateKey operation or change an existing policy by calling UpdateRotationPolicy. When you call these operations, you must configure the following parameters:
**EnableAutomaticRotation**: Specifies whether to enable automatic rotation.
**RotationInterval**: The automatic rotation period.
You can call the DescribeKey operation to query the configured rotation policy. The response includes the following parameters:
**AutomaticRotation**: The status of automatic rotation. Disabled indicates that automatic
rotation is not enabled. Enabled indicates that automatic rotation is enabled. Suspended indicates that automatic rotation is enabled but is suspended by KMS.
**RotationInterval**: The automatic rotation period.

**How KMS executes the policy**

If you enable automatic rotation, KMS calculates the next rotation time as follows:

```xml
<NextRotationTime> = <LastRotationTime> + <RotationInterval>
```

The parameters are described as follows:

| LastRotationTime |   | : The time whe |
|---|---|---|
| value from the |   |   |

`LastRotationTime` : The time when the last key version was generated. You can query this value from the `LastRotationDate` field returned by the DescribeKey operation. `NextRotationTime` : The time for the next scheduled rotation. KMS creates a new key version after this time is reached. You can query this value from the `NextRotationDate` field returned by the DescribeKey operation.

**Important**

Updating the rotation period might cause the next scheduled rotation time to be in the past. This does not change the rotation behavior. If the scheduled time is in the past, KMS immediately rotates the key.

**How key state affects rotation**

Only a CMK with a **KeyState** of Enabled can be rotated. Do not call UpdateRotationPolicy to change the rotation policy for a CMK in the Disabled or PendingDeletion state. If a CMK enters the Disabled or PendingDeletion state after you enable automatic rotation, KMS pauses automatic rotation. In this case, the rotation status (**AutomaticRotation**) returned by DescribeKey is Suspended. When the CMK returns to the Enabled state, the previously configured rotation policy resumes.

**Limitations**

The following key types do not support multiple versions: Service-managed keys: Keys that other cloud services create and manage in KMS on your behalf. They provide a basic layer of encryption for your data in those services. Bring your own key (BYOK): Keys that you import into KMS. For this type of CMK, the **Origin** property is External. KMS does not generate key material for you and cannot automatically initiate rotation. Therefore, these two key types do not support version-based rotation, either automatic or manual. For BYOK keys, this is because managing them is already complex. You are responsible for the key lifecycle, which requires an on-premises key management system, keeping information synchronized with KMS, and understanding that deleting key material in the cloud has no buffer period. Adding multiple versions would greatly increase this complexity and the risk of misconfigurations that could put your data at risk. Additionally, since each version could become unavailable at a different time, it would be difficult to guarantee the availability of both the CMK and the data it protects. For keys that do not support version-based rotation, see **Manually rotate CMKs** for an alternative solution.

### 9.3 Manually rotate a master key

If your key type does not support automatic rotation based on key versions, you can manually rotate a Customer Master Key (CMK) as needed. This method works for any CMK, regardless of its support for automatic rotation, and serves as a practical alternative in specific scenarios.

**Custom encryption for applications**

Applications, whether on-premises or in the cloud, can call Key Management Service (KMS) APIs to encrypt their data. For example: Encrypting sensitive information such as ID numbers, credit card numbers, or home addresses before writing it to a database. Performing client-side encryption before uploading data to Object Storage Service (OSS). Encrypting service configuration files that contain sensitive information, such as application configuration files or SSL private key certificates. You can use the key alias feature in KMS to rotate the encryption keys that your applications use. The KMS Decrypt API does not require you to provide a key ID or an alias. Encryption module Encryption module Uses new key: CMK-B alias/MyAppKey alias/MyAppKey

**×**

CMK-A CMK-A CMK- This rotation process involves the following steps:
1. Initial setup
i. An administrator creates a CMK. Assume its ID is CMK-A. ii. The administrator binds the alias alias/MyAppKey to CMK-A. iii. When the application's encryption module calls the Encrypt API, it passes the alias alias/MyAppKey in the **KeyId** parameter. KMS detects that alias/MyAppKey is bound to the master key with the ID CMK-A and uses CMK-A for encryption. iv. When the application's decryption module calls the Decrypt API, it does not need to pass the **KeyId** parameter. KMS identifies the CMK from the ciphertext and uses it to decrypt the data.
2. Manual key rotation
i. The administrator creates a new CMK. Assume its ID is CMK-B. ii. The administrator calls UpdateAlias to bind the alias alias/MyAppKey to CMK-B. iii. When the application's encryption module calls the Encrypt API, it passes the alias alias/MyAppKey in the **KeyId** parameter. KMS now detects that alias/MyAppKey is bound to the master key with the ID CMK-B and uses CMK-B for encryption. iv. When the application's decryption module calls the Decrypt API, it does not need to pass the **KeyId** parameter. KMS identifies the CMK from the ciphertext and uses it to decrypt the data.

**Server-side encryption for cloud products**

Cloud products can integrate with KMS APIs to apply server-side encryption to the data they manage. For key rotation, server-side encryption with cloud products involves two main scenarios: Automatic rotation affects server-side encryption This scenario occurs when a cloud product is configured to use a specific CMK and continuously calls the GenerateDataKey API to generate new data keys. When KMS creates a new primary version of the master key, the cloud product uses this new version to encrypt newly generated data keys. Object Storage Service (OSS) is an example of such a product. In this case, you cannot use automatic rotation with a service-managed default key or an imported external key (bring your own key), as these key types do not support it. Automatic rotation does not affect server-side encryption This scenario occurs when a cloud product calls a KMS encryption API only once for a specific resource. Consequently, the cloud product will not use a new key version even if KMS rotates the CMK. For example, when Elastic Compute Service (ECS) encrypts a cloud disk, it calls the GenerateDataKey API only once to generate a data key for volume encryption. This key is then used for the lifetime of the disk and is not updated. If you used a bring your own key (BYOK) or want to rotate the data key as well in the first scenario, or if your application scenario is the second one, you can achieve key rotation by methods such as changing configurations and copying data.
