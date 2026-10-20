---
title: "Key Management Service User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 44
source_pdf: "54e6e0b82d0aceaa_Alibaba Cloud Apsara Stack V3.18.6 Key Management Service User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Key%20Management%20Service%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Key Management Service User Guide 20260701

## Table of Contents

- 1 Restrictions
- 2 Quick start
  - 2.1 Log on to the Apsara Uni-manager Management Console
  - 2.2 User roles and permissions
- 3 Manage CMKs
  - 3.1 Create a CMK
  - 3.2 View and adjust the key quota
  - 3.3 View the details of a CMK
  - 3.4 Enable a CMK
  - 3.5 Disable a CMK
  - 3.6 Synchronize keys across regions
  - 3.7 Schedule a CMK deletion task
  - 3.8 Configure a rotation policy
  - 3.9 Generate a data key
  - 3.10 Generate a CSR
- 4 Use RAM for access control
- 5 Use aliases
- 6 Overview of CMKs
- 7 Use symmetric keys
  - 7.1 Overview
  - 7.2 EncryptionContext
  - 7.3 Import and delete key material
- 8 Use asymmetric keys
  - 8.1 Overview
  - 8.2 Encrypt and decrypt data by using an asymmetric CMK
  - 8.3 Generate and verify a digital signature by using an asymmetric CMK
- 9 Key rotation
  - 9.1 Overview
  - 9.2 Automatic key rotation
  - 9.3 Manual CMK rotation

## 1 Restrictions

Before logging on to Apsara Stack Security Center, make sure that your local PC meets the requirements. Table 1. Configuration requirements

| Item | Requirements |
|---|---|
| Browser | Internet Explorer: 11 or later Google Chrome (recommended): 42.0.0 or later Mozilla Firefox: 30 or later Safari: 9.0.2 or later |
| Operating system | Windows XP, Windows 7, or later Mac |

## 2 Quick start

### 2.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. To configure the Cloud Security system, you must log on with a global organization security administrator account. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
> **Forgot password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

### 2.2 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. Custom roles and default roles are supported. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. Table 1. Default roles in Apsara Stack Security

| Role | Description |
|---|---|
| Organization security administrator | This role has the permissions to use Security Operations Center (SOC) to manage the security of hosts, applications, and networks for an organization. This role also has the permissions to manage security services related to Elastic Compute Service (ECS). |
| Global organization security administrator | This role has the permissions to use SOC to conduct security management for Apsara Stack and all tenants and manage security services related to ECS. |

If you do not have an account or a role, contact the administrator to create a user and assign a role to the user. For more information, see **Create a user** in **Apsara Uni-manager**
**Management Console User Guide**.

## 3 Manage CMKs

### 3.1 Create a CMK

This topic describes how to create a customer master key (CMK) for subsequent encryption and decryption.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, click **Create Key**.
4. On the **Create Key Pair** page, select an organization from the **Organization** drop-down
list. Then, the **Resource Set** and **Region** parameters are automatically configured.
5. In the **Basic Configurations** section, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|
| Key Type | The type of the CMK. Valid values: Symmetric CMKs: Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ |
| Key Purpose | The purpose of the CMK. Valid values: ENCRYPT/DECRYPT: The CMK is used to encrypt and decrypt data. SIGN/VERIFY: The CMK is used to generate and verify a digital signature. |
| Protection Level | The protection level of the CMK. Set the value to SOFTWARE. SOFTWARE: A software module is used to protect the CMK. |
| Alias | The alias of the CMK, which is used to identify the CMK. For more information, see Use aliases. |
| Description | The description of the CMK. |

6. In the **Advanced Settings** section, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|

| Rotation Period | Specifies whether to enable automatic rotation. Valid values: Disable: disables automatic rotation. Enable: enables automatic rotation. You can select a rotation interval or configure a custom rotation interval. Note You can configure this parameter only if you set the Key type parameter to Aliyun AES 256. _ _ If the Key Material Source parameter is set to External, automatic rotation is not supported. |
|---|---|
| Key Material Source | The key material source. Valid values: Key Management Service: KMS generates the key material. External: KMS does not generate the key material. You must import the key material to KMS. Note You can configure this parameter only if you set the Key Type parameter to Aliyun AES 256 or Aliyun SM4. _ _ _ |

7. Click **Confirm Order**.

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
4. On the Customer Master Key page, find the CMK that you want to view and click its alias or
choose **More** > **Key Details** in the Actions column.

> **Note:** In the CMK list, you can find a CMK and move the pointer over the value in the **Key ID** column. Then, the description of the CMK appears. This helps you distinguish CMKs.

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

> **Warning:** Make sure that the CMK and replica keys are enabled before you change the primary region.
> During the operation, you cannot perform other operations to manage the CMK or replica keys.

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK whose primary region you want to
change, and click its alias or choose **More > Key Details** in the **Actions** column.
4. On the **Regional** tab of the key details page, click **Change Primary Region**.
5. In the **Change Primary Region** dialog box, select a region and click **OK**.

### 3.7 Schedule a CMK deletion task

You can schedule the deletion of a customer master key (CMK) by specifying a waiting period. After the waiting period ends, the key is automatically deleted.

**Background information**

You can specify a waiting period of 7 to 30 days. Take note of the following items when you schedule the deletion of a CMK: During the waiting period, the CMK is in the Pending Deletion state. It cannot be used to encrypt data, decrypt data, or generate data keys. Deleting a CMK may have a severe impact on data availability. Therefore, in most cases, we recommend that you disable a CMK instead of deleting it. After a CMK is deleted, it cannot be recovered. The data encrypted by using this CMK and the ciphertext data keys generated by using this CMK cannot be decrypted. Therefore, KMS only allows you to schedule the deletion of a CMK. You cannot immediately delete a CMK. KMS deletes the CMK within 24 hours after the specified waiting period ends. For example, if you submit a deletion request at 14:00, September 10, 2024 and specify a waiting period of seven days, KMS deletes the CMK within 24 hours after 14:00, September 17, 2024.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find the CMK that you want to delete and choose
**More** > **Schedule Key Deletion** in the **Actions** column.
4. In the **Schedule Key Deletion** dialog box, configure the **Delete In (7-30 days):**
parameter.
5. Then, click **OK**.

**Verify the result**

After you complete the configuration, the status of the CMK becomes **Pending Deletion**.

> **Note:** Before the waiting period ends, you can choose **More** > **Cancel Key Deletion** to cancel the schedule.

### 3.8 Configure a rotation policy

This topic describes how to configure a rotation policy of a customer master key (CMK).

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, select a CMK whose **Key Type** is Aliyun_AES_256,
and choose **More** > **Key Details** in the **Actions** column.
4. On the **Key Version** tab, click **Configure Rotation Policy**.
5. In the **Configure Rotation Policy** dialog box, configure the **Rotation Period** parameter.
Disable: Disable automatic rotation for the CMK. 30 Days, 90 Days, 180 Days, and 365 Days: Select an automatic rotation interval. Customize: Allow you to specify a custom rotation interval.
6. Click **OK**.

### 3.9 Generate a data key

Data keys can be used to encrypt and decrypt on-premises data. This topic describes how to generate a data key.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find a symmetric customer master key (CMK) whose
purpose is **Encrypt/Decrypt** and click its alias or choose **More** > **Key Details**.

> **Note:** The key type for symmetric keys is Aliyun_AES_256.

4. On the **Data Key Usage** tab, click the **Generate Data Key** tab.
5. On the **Generate Data Key** tab, configure the parameters as required and click **Submit**.
i. In the **Parameters to Generate Data Key** section, configure the **Key Type** and
**Encryption Context** parameters.
ii. In the **Parameters to Generate Data Key** section, configure the **Encrypt Data Key**
**by Using Public Key** parameter. Valid values:
**Yes**: Encrypt a data key by using a specific public key and export the data key. In the
**Specify the export publicKey** section, configure the **Publickey Type**, **Public Key**,
and **Key Algorithm** parameters.
**No**: Export a data key without encrypting the data key by using a specific public key.
This way, you can directly generate a data key.

> **Note:** After the data key is generated, you can view the ciphertext of the data key in the **Data key export results** dialog box.

6. Optional. Click the **Data Key Re-encryption** tab, configure the parameters as required,
and then click **Submit**.

| Transfer protection scenario | Related operation |
|---|---|
| Use public key to protect | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Encryption Context parameters. ii. In the Specify the export publicKey section, configure the Publickey Type, Public Key, and Key Algorithm parameters. |
| Data key transfer protection in the same region | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target KeyId and Target EncryptionContext parameters. |
| Data key transfer protection across regions | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target RegionId, Target Asymmetric KeyID, Target Asymmetric KeyVersionID, Target KeyId, and Target EncryptionContext parameters. |

> **Note:** After transfer protection is configured for the data key, you can view the ciphertext of the data key in the **Data key transfer protection result** dialog box.

### 3.10 Generate a CSR

To generate a certificate, you must submit a certificate signing request (CSR) to a certificate authority (CA). This topic describes how to generate a CSR.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, find an asymmetric CMK whose purpose is
**Sign/Verify** and click its alias or choose **More** > **Key Details**.

> **Note:** The key type for asymmetric keys is RSA_2048, EC_P256, or EC_P256K.

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

KMS defines actions used in RAM policies for each API operation that requires access control. Actions must be in the kms:${api-name} format.

> **Note:** The DescribeRegions operation does not require access control. It can be called by Apsara Stack tenant accounts, RAM users, or RAM roles after they pass RAM authentication.

The following tables describe the RAM action and resource type that correspond to each KMS API operation. Key service operations

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

Each alias is associated with a CMK. However, aliases are independent of the CMKs that are associated with them. Aliases have the following characteristics: You can call the UpdateAlias operation to associate an alias with another CMK. This operation does not affect the original CMK. If you delete an alias, the CMK associated with the alias is not deleted. Resource Access Management (RAM) users must be authorized before they can perform operations on an alias. For more information, see Use RAM for access control. Aliases cannot be modified. To change the alias of a CMK, you must delete the original alias and create another one for the CMK. You can replace the ID of a CMK with its alias in the request parameters of the following API operations: DescribeKey Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext

> **Note:** For more information about the API operations, see the **API reference** topic of **Developer Guide**.

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

`]` `}` `]` `}`

> **Note:** A new alias created for a CMK does not affect the existing aliases of the CMK.

You can use one of the following methods to create an alias: Console: i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Security > Key Management Service**. iii. On the **Customer Master Key** page, find the desired CMK, and click its alias or choose
**More** > **Key Details**.
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

`]` `}` `]` `}` You can use one of the following methods to delete an alias: Console: i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Security > Key Management Service**. iii. On the **Customer Master Key** page, find the desired CMK, and click its alias or choose
**More** > **Key Details**.
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

## 6 Overview of CMKs

The key service is a core component of Key Management Service (KMS). It provides fully managed keys and key protection features, with cloud-native API operations for data encryption and digital signature management.

**Algorithms**

| Algorithm class | Algorithm subclass | Encryption and decryption | Signing and verification |
|---|---|---|---|
| Symmetric key | AES | Supported | Not supported |
| Asymmetric key | RSA | Supported | Supported |
| Asymmetric key | ECC | Not supported | Supported |

Symmetric keys are used to encrypt or decrypt data. If you do not specify the KeySpec parameter during key creation, KMS creates a symmetric key. You can call the Encrypt or Decrypt operation to encrypt or decrypt data without the need to obtain the plaintext of a symmetric key. For more information, see Overview of symmetric encryption. Asymmetric keys can be used to encrypt data, decrypt data, sign data, or verify a signature. An asymmetric customer master key (CMK) in Key Management Service (KMS) consists of a public key and a private key, which are cryptographically related to each other. The public key can be sent to all users, but the private key must be protected. To protect the private key, KMS does not provide an API operation for you to export the private key of an asymmetric key. You can use a private key to decrypt data or sign data by calling the related operations. Users with a public key can use the public key to encrypt data or verify the signature that is generated by using the matched private key. For more information, see Overview of asymmetric keys.

> **Note:** Only KMS of the Advanced edition supports Rivest-Shamir-Adleman (RSA) and elliptic-curve cryptography (ECC) keys.

**Key owner**

In most cases, you are the owner of your CMKs in KMS, and their Creator attributes are set to the ID of your Apsara Stack tenant account. Apsara Stack services can be integrated with KMS to implement server-side encryption (SSE). In this scenario, KMS allows a service to automatically manage an encryption key that can be used only by the service to encrypt your data. This makes it easier for you to use the entrylevel data encryption features and reduces your workload in the management of key lifecycles and permissions. These service-managed keys are called service keys. To identify a service key, the Creator attribute of the service key is assigned the code of the associated service. The service key is associated with an alias that is in the `acs/<code of the service>` format. For example, the Creator attribute of the service key managed by Object Storage Service (OSS) is set to OSS and the acs/oss alias is associated with the service key.

## 7 Use symmetric keys

### 7.1 Overview

KMS handles cryptographic operations on your behalf, so your applications never manage key material or implement encryption logic directly. When you create a customer master key (CMK) without specifying the `KeySpec` parameter, KMS creates a symmetric key by default.

> **Note:** For more information about the API operations, see the **API reference** topic of **Developer Guide**.

**Types of symmetric CMKs**

The following table describes the types of symmetric customer master keys (CMKs) that Key Management Service (KMS) supports.

| Algorithm | CMK length | CMK specification | Data encryption mode | Protection level |
|---|---|---|---|---|
| AES | 256 bits | Aliyun AES 256 _ _ | GCM | Software |

**Encryption and decryption features**

To encrypt data, you need to only specify the ID or alias of a CMK. KMS uses the specified CMK for encryption and returns the ciphertext. When you call the Decrypt operation to decrypt data, you need to only specify the ciphertext that you want to decrypt. You do not need to specify the CMK. The Decrypt operation is available for you to decrypt the ciphertext that is generated by calling the Encrypt, GenerateDataKey, or GenerateDataKeyWithoutPlaintext operation.

**AAD**

Symmetric CMKs of KMS use GCM for block ciphers. You can use additional authenticated data (AAD) to provide additional protection to ensure the integrity of encrypted data. KMS encapsulates the AAD input. This way, you can configure and include your own authentication data in an efficient manner. For more information, see EncryptionContext.

**Envelope encryption**

KMS allows you to generate a two-level key hierarchy to accelerate envelope encryption by calling the GenerateDataKey and GenerateDataKeyWithoutPlaintext operations. For more information about envelope encryption, see the **Envelope encryption** topic below
**Features** in **Technical White Paper**.

**Rotation of symmetric keys**

If a CMK has multiple versions, the latest version of the CMK is used in the Encrypt, GenerateDataKey, and GenerateDataKeyWithoutPlaintext operations to encrypt data. To decrypt the data, you do not need to specify the ID or the CMK or key version. KMS automatically identifies the CMK and its key version with which the data is encrypted. Then, KMS uses the key material of the identified key version to decrypt the ciphertext. KMS rotates a CMK by generating a new version of the CMK. After a rotation is complete, KMS automatically uses the new CMK to encrypt data. However, the earlier CMK is still available for decrypting the ciphertext generated before the rotation. For more information, see Automatic key rotation.

**BYOK feature**

KMS allows you to encrypt your data in the cloud by using the Bring Your Own Key (BYOK) feature. This feature helps you meet stringent security and compliance requirements. We recommend that you use a managed hardware security module (HSM) to protect your keys by importing key material into CMKs with HSM-grade security. The keys imported into the managed HSM can only be destroyed, and their plaintext cannot be exported.

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

This topic describes how to import and delete external key material for a customer master key (CMK).

**Background information**

CMKs are basic resources of Key Management Service (KMS). A CMK consists of a key ID, basic metadata such as the key status, and key material that is used to encrypt and decrypt data. By default, KMS generates key material when you call the CreateKey operation to create a CMK. You can select an external CMK as the key material source. In this case, KMS does not create key material. You must import external key material to the CMK. You can call the DescribeKey operation to check the key material source of an existing CMK.

> **Note:** For more information about the API operations, see the **API reference** topic of **Developer Guide**.

CMKs can be classified into regular CMKs and external CMKs based on the source of key material. Before you import external key material, take note of the following points: Make sure that the key material is reliable. KMS ensures the high availability of the imported key material. However, KMS cannot ensure that the imported key material is as reliable as the key material generated by KMS. You can call the DeleteKeyMaterial operation to delete the key material that you have imported. You can also set a validity period to enable KMS to automatically delete the key material after the validity period ends. The CMK is not deleted. To delete key material generated by KMS, you can only call the ScheduleKeyDeletion operation to specify a waiting period of 7 to 30 days for deleting the CMK. The key material is deleted with the relevant CMK after the waiting period ends. After you delete the imported key material, you can re-import the same key material to make the relevant CMK available again. Therefore, we recommend that you save a copy of the key material. The key material to be imported must be a 256-bit symmetric key.

**Import key material**

1. Create an external CMK.
You can use one of the following methods to create an external CMK: Method 1: Log on to the KMS console and click Create Key. On the Create Key page, set the Key Material Source parameter to External in the Advanced Settings section. For more information, see Create a CMK. Method 2: Call the CreateKey operation. Set the **Origin** parameter to EXTERNAL.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms CreateKey --Origin EXTERNAL --Description "External key"
```

2. Obtain the parameters that are used to import key material.
The parameters include a public key and an import token. The public key is used to encrypt key material. You can use one of the following methods to obtain the parameters used to import key material: Method 1: Obtain the parameters in the KMS console. Method 2: Obtain the parameters by calling the GetParametersForImport operation.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms GetParame tersForImport --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --WrappingAlgorithm RSAE S_OAEP_SHA_1 --WrappingKeySpec RSA_2048
```

3. Import the key material.

> **Note:** You can import key material into an external CMK that does not have key material. You can also reset the expiration time of key material or re-import key material that has expired or been removed.
> Each import token is bound to a public key that is used to encrypt key material. A CMK is specified when an import token is generated. The import token can be used to import key material only into the specified CMK.
> The validity period of an import token is 24 hours. It can be repeatedly used within the validity period. After it expires, you must obtain a new import token and a new public key.

i. Use the public key to encrypt key material. The public key is a 2,048-bit Rivest-Shamir-Adleman (RSA) public key. The encryption algorithm must be the same as that specified when you obtain the parameters that are used to import the key material. The public key returned by the GetParametersForImport operation is encoded in Base64. You must first decode the public key. Currently, KMS supports the RSAES_OAEP_SHA_256 and RSAES_PKCS1_V1_5 encryption algorithms. ii. Encode the encrypted key material in Base64. iii. Call the ImportKeyMaterial operation to import the encoded key material and the import token to KMS.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms ImportKey Material --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --EncryptedKeyMaterial xxx -- ImportToken xxxx
```

**Delete key material**

After you import key material into an external CMK, you can use the external CMK in the same way as a regular CMK. The only difference is that the key material of an external CMK may expire and can be removed separately. After the key material of an external CMK expires or is removed, the external CMK can no longer be used, and the ciphertext encrypted by using the external CMK cannot be decrypted. To use the external CMK and decrypt the related ciphertext again, you must re-import the same key material. If an external CMK is in the PendingDeletion state when its key material expires or is removed, the CMK status does not change after the key material expires or is removed. Otherwise, the status of the CMK becomes PendingImport after the key material expires or is removed. You can use one of the following methods to delete key material: Method 1: Delete the key material in the KMS console. Method 2: Delete the key material by calling the DeleteKeyMaterial operation.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${ please-repleace-your-endpoint} --access-key-id ${please-repleace-your-access-key-id} --access-key-secret ${please-repleace-your-access-key-secret} kms DeleteKeyMaterial - -KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8****
```

**Use OpenSSL to encrypt and upload key material**

1. Create an external CMK.
2. Create key material.
The key material must be a 256-bit symmetric key. In this example, OpenSSL is used to generate a 32-byte random number.

```
openssl rand -out KeyMaterial.bin 32
```

3. Obtain the parameters that are used to import key material.
4. Encrypt the key material.
i. Decode the Base64-encoded public key. ii. Use the specified encryption algorithm, such as RSAES_OAEP_SHA_1, to encrypt the key material. iii. Encode the encrypted key material in Base64 and save the key material to a text file.

```
openssl rand -out KeyMaterial.bin 32 openssl enc -d -base64 -A -in PublicKey_base64.txt -out PublicKey.bin openssl rsautl -encrypt -in KeyMaterial.bin -oaep -inkey PublicKey.bin -keyform DE R -pubin -out EncryptedKeyMaterial.bin openssl enc -e -base64 -A -in EncryptedKeyMaterial.bin -out EncryptedKeyMaterial_base64.txt
```

iv. Upload the encrypted key material and import token.

**Example**

Use SDK for Java to encrypt and upload key material.

```java
//Use the latest version of KMS SDK for Java. //KmsClient.java import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; importcomaliyuncshttpFormatType;
```

```java
import com.aliyuncs.http.FormatType; import com.aliyuncs.kms.model.v20160120.*; import com.aliyuncs.profile.DefaultProfile; // Encapsulate the KMS API. public class KmsClient {
    DefaultAcsClient client;
    public KmsClient(String regionId, String ak, String secret) {
        DefaultProfile profile = DefaultProfile.getProfile(regionId, ak, secret);
        this.client = new DefaultAcsClient(profile);
```

`}`

```
    //Specify a custom endpoint. In most cases, a Virtual Private Cloud (VPC) endpoint
is specified. You can also specify a custom endpoint if you cannot obtain the IP addres s in the Apsara Stack environment based on the regionId parameter.
    public KmsClient(String regionId, String ak, String secret, String endpoint) {
        DefaultProfile.addEndpoint(regionId, "kms", endpoint);
        DefaultProfile profile = DefaultProfile.getProfile(regionId, ak, secret);
        this.client = new DefaultAcsClient(profile);
```

`}`

```
    public CreateKeyResponse createKey() throws Exception {
        CreateKeyRequest request = new CreateKeyRequest();
        request.setOrigin("EXTERNAL"); //Create an external CMK.
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
    //Same as other API operations. Details are not shown.
```

`}`

```java
//example.java import com.aliyuncs.kms.model.v20160120.*;
```

`p` `y` ;

```java
import javax.crypto.Cipher; import javax.crypto.spec.OAEPParameterSpec; import javax.crypto.spec.PSource.PSpecified; import javax.xml.bind.DatatypeConverter; import java.security.KeyFactory; import java.security.PublicKey; import java.security.spec.MGF1ParameterSpec; import java.security.spec.X509EncodedKeySpec; import java.util.Random; public class CreateAndImportExample {
    public static void main(String[] args) {
        String regionId = "cn-hangzhou";
        String accessKeyId = "*** Provide your AccessKeyId ***";
        String accessKeySecret = "*** Provide your AccessKeySecret ***";
        KmsClient kmsclient = new KmsClient(regionId, accessKeyId, accessKeySecret);
        //String endpoint = "*** VPC Endpoint ***";
        //KmsClient kmsclient = new KmsClient(regionId, accessKeyId, accessKeySecret, e
ndpoint);
        //Create External Key
        try {
            CreateKeyResponse keyResponse = kmsclient.createKey();
            String keyId = keyResponse.getKeyMetadata().getKeyId();
            //Generate a 32-byte random number.
            byte[] keyMaterial = new byte[32];
            new Random().nextBytes(keyMaterial);
            //Obtain the parameters that are used to import key material.
            GetParametersForImportResponse paramResponse =
kmsclient.getParametersForImport(keyId, "RSA_2048", "RSAES_OAEP_SHA_256");
            String importToken = paramResponse.getImportToken();
            String encryptPublicKey = paramResponse.getPublicKey();
            //Decode the public key in Base64.
            byte[] publicKeyDer =
DatatypeConverter.parseBase64Binary(encryptPublicKey);
            //Generate an RSA public key.
            KeyFactory keyFact = KeyFactory.getInstance("RSA");
            X509EncodedKeySpec spec = new X509EncodedKeySpec(publicKeyDer);
            PublicKey publicKey = keyFact.generatePublic(spec);
            //Encrypt the key material.
            Cipher oaepFromAlgo = Cipher.getInstance("RSA/ECB/OAEPWithSHA-
1AndMGF1Padding");
            String hashFunc = "SHA-256";
            OAEPParameterSpec oaepParams = new OAEPParameterSpec(hashFunc, "MGF1", new
MGF1ParameterSpec(hashFunc), PSpecified.DEFAULT);
            oaepFromAlgo.init(Cipher.ENCRYPT_MODE, publicKey, oaepParams);
            byte[] cipherDer = oaepFromAlgo.doFinal(keyMaterial);
            //Encode the encrypted key material in Base64.
            String encryptedKeyMaterial =
DatatypeConverter.printBase64Binary(cipherDer);
            //Import the key material.
            Long expireTimestamp = 1546272000L; //The UNIX timestamp. The timestamp is
accurate to seconds. A value of 0 indicates that the key material never expires.
            kmsclient.importKeyMaterial(keyId, importToken, encryptedKeyMaterial,
```

```
expireTimestamp);
        } catch (Exception e) {
            //Details are not shown.
```

`}` `}` `}`

## 8 Use asymmetric keys

### 8.1 Overview

Asymmetric keys in KMS use a mathematically linked key pair — a public key and a private key — to encrypt data or generate digital signatures between systems with different trust levels. The public key is available for all to use, but the private key must be kept secure and used only by trusted users. You can create asymmetric customer master keys (CMKs) in Key Management Service (KMS). An asymmetric key pair consists of a public key and a private key, which are cryptographically related to each other. The public key is available for all users, but the private key must be protected and used only by trusted users. KMS supports popular asymmetric key algorithms and provides sufficient security strength to ensure the security of encrypted data and digital signatures.

**Types of asymmetric keys**

The following table describes the types of asymmetric keys that KMS supports.

| Algorithm | Key specification | Description | Usage |
|---|---|---|---|
| RSA | RSA 2048 _ | Rivest-Shamir- Adleman (RSA) | Encrypt or decrypt data. Sign data. |
| ECC | EC P256: National _ Institute of Standards and Technology (NIST)- recommended elliptic curve P-256 EC P256K: _ Standards for Efficient Cryptography Group (SECG) elliptic curve secp256k1 | Elliptic-curve cryptography (ECC) | Sign data. |

**Encrypt data**

Asymmetric keys are used to encrypt and transmit sensitive information. The following steps describe a typical scenario: For more information, see Encrypt and decrypt data by using an asymmetric CMK.

**Sign data.**

For more information, see Asymmetric signature.

**Key versions**

KMS does not support automatic rotation of asymmetric CMKs due to the limits of public and private keys. You can call the CreateKeyVersion operation to create another key version in a specific CMK and generate a new pair of public and private keys. If you use a new key version to generate a digital signature or encrypt data, you must also distribute the new version of the public key. In contrast to symmetric CMKs, asymmetric CMKs do not have a primary key version. Therefore, when you call operations related to asymmetric CMKs in KMS, you must specify the CMK ID or CMK alias, and a key version.

**Public key operations**

In most cases, you can call the GetPublicKey operation to obtain a public key and distribute the public key to users for encryption or verification. Then, the users can use cryptographic libraries such as OpenSSL and Java Cryptography Extension (JCE) to perform calculation in their business systems. You can also call the AsymmetricEncrypt or AsymmetricVerify operation to perform public key operations. KMS records the logs of the calls and provides the capability to restrict the usage of public keys using Resource Access Management (RAM). Compared with calculation in business systems, KMS offers flexible features that better suit your needs.

**Private key operations**

You can only call the AsymmetricDecrypt or AsymmetricSign operation to decrypt data or sign data by using a private key.

### 8.2 Encrypt and decrypt data by using an asymmetric CMK

**using an asymmetric CMK**

This topic shows you how to encrypt data with a public key locally and decrypt it with KMS using an RSA_2048 asymmetric customer master key (CMK) and Alibaba Cloud CLI.

**Before you begin**

Call the CreateKey operation to create an asymmetric CMK in Key Management Service (KMS). Set the KeySpec parameter to a required asymmetric CMK type and the KeyUsage parameter to `ENCRYPT/DECRYPT` . The following sample code provides an example on how to create an asymmetric CMK of the RSA_2048 type:

```
aliyun kms CreateKey --KeySpec=RSA_2048 --KeyUsage=ENCRYPT/DECRYPT -- ProtectionLevel=HSM
```

**Obtain the public key**

1. Call the GetPublicKey operation to obtain the public key of the asymmetric CMK.

```
aliyun kms GetPublicKey --KeyId=**** --KeyVersionId=****
```

Sample success response: `{`

```json
        "RequestId": "82c383eb-c377-4mf6-bxx8-81hkc1g5g7ab",
        "KeyId": "****",
        "KeyVersionId": "****",
        "PublicKey": "PublicKey-DataBlob"
```

`}`
2. Save the public key to the rsa_publickey.pub file. PublicKey-DataBlob is a placeholder.
Replace it with the obtained public key.

```
echo PublicKey-DataBlob > rsa_publickey.pub
```

**Use the public key to encrypt data**

1. Create a sample plaintext file named plaintext-file.txt that contains "this is plaintext."

```
echo "this is plaintext" > plaintext-file.txt
```

2. Use OpenSSL to encrypt the file and write the obtained binary ciphertext into the plaintext-
file.enc file.

```
openssl pkeyutl -encrypt -in plaintext-file.txt \
  -inkey rsa_publickey.pub -pubin \
  -pkeyopt rsa_padding_mode:oaep \
  -pkeyopt rsa_oaep_md:sha256 \
  -pkeyopt rsa_mgf1_md:sha256 \
  -out plaintext-file.enc
```

### 8.3 Generate and verify a digital signature by using an asymmetric CMK

**signature by using an asymmetric**

**CMK**

Generate and verify digital signatures using asymmetric customer master keys (CMKs) in KMS. This guide walks through a complete signing workflow: creating a key, computing a message digest, calling KMS to sign, retrieving the public key, and verifying the signature locally using OpenSSL.

**Before you start**

Call the CreateKey operation to create an asymmetric CMK in KMS. Set the KeySpec parameter to a desired key type and the KeyUsage parameter to `SIGN/VERIFY` .

**Obtain the public key**

Obtain the public key of the created asymmetric key pair from the KMS. The preceding example assumes that:

## 9 Key rotation

### 9.1 Overview

Keys are used to protect specific data. Therefore, the security of the data depends on the security of its keys. You can regularly rotate keys between key versions to improve key security and implement security policies and best practices for data protection.

**Achieve security goals**

You can regularly rotate keys to achieve the following goals: Reduce the amount of data encrypted based on each key The security of a key is inversely proportional to the amount of data encrypted based on the key. This amount is usually defined by the total bytes of data or the total number of messages that are encrypted based on the same key. For example, National Institute of Standards and Technology (NIST) defines the secure lifecycle of a key in Galois/Counter Mode (GCM) as the total number of messages encrypted based on the key. Regular key rotation allows each key to remain secure and minimizes vulnerability to cryptanalytic attacks. Respond in advance to security events In the early days of system design, key rotation was introduced as a routine operations and maintenance (O&M) method. This provides the system with a method to handle security events when they occur, and complies with the fail early, fail often principle of software engineering. If key rotation is not executed in the system until an emergency event has already occurred, the probability of system failure increases exponentially. Provide logical isolation of data Data encrypted before a key rotation is isolated from data encrypted after the key rotation. The impact of key-related security events can be identified and preventive measures can be taken. Reduce the window of time to crack keys Regular rotation of encryption keys ensures that you can control and reduce the window of time during which the key and its encrypted data are vulnerable to being cracked. The interval between rotation tasks during which attackers are able to crack the key is limited. This practice greatly increases the security of your data against cryptanalytic attacks.

**Meet the requirements of regulatory compliance**

Regular key rotation facilitates compliance with various regulations, which include but are not limited to the following regulations: Payment Card Industry Data Security Standard (PCI DSS) Cryptography-related industrial standards issued by State Cryptography Administration, such as GM/T 0051-2016 Cryptography-related standards issued by NIST, such as NIST Publication 800-38D

### 9.2 Automatic key rotation

This topic shows you how to configure automatic rotation of CMKs in KMS.

**Key versions**

A CMK may have multiple key versions. Each key version represents an independently generated key. Key versions of the same CMK do not have a cryptographic relation to each other. KMS automatically rotates CMKs by generating new key versions. Key versions are divided into the following types: Primary key versions The primary key version of a CMK is an active encryption key. Each CMK has only one primary key version at a point in time. When you call an encryption operation such as GenerateDataKey or Encrypt, KMS uses the primary key version of a specified CMK to encrypt plaintext. You can call the DescribeKey operation to query the **PrimaryKeyVersion** attribute. Non-primary key versions The non-primary key version of a CMK is an inactive encryption key. Each CMK can have zero to multiple non-primary key versions. Each non-primary key version was a primary key version and acted as the active encryption key in the past. When a new primary key version is created, KMS does not delete or disable non-primary key versions, which are needed to decrypt data.

> **Note:** When you call an encryption operation, the primary key version of a specified CMK is used. When you call a decryption operation, the key version that was used for encryption is used.

You can generate a key version in one of the following ways: Create a CMK. You can call the CreateKey operation to create a CMK. If you set the **Origin** parameter to Aliyun_KMS, KMS generates an initial key version and sets it as the primary key version. Execute an automatic rotation policy. After you configure an automatic rotation policy for a CMK, KMS executes the policy on a regular basis to generate key versions.

**Automatic rotation**

Configure a key rotation policy. You can call the DescribeKey operation to view the configured automatic rotation policy. The following parameters are returned:
**AutomaticRotation**: indicates whether automatic rotation is enabled. The value Disabled
indicates that automatic rotation is disabled. The value Enabled indicates that automatic rotation is enabled. The value Suspended indicates that KMS suspends the execution of automatic rotation although automatic rotation is enabled.
**RotationInterval**: indicates the interval for automatic rotation.
Execute an automatic rotation policy.

**CMK status and rotation behavior**

Rotation only runs on CMKs in the `Enabled` state ( `KeyState = Enabled` ).

**Scenario: CMK enters Disabled or Pending Deletion state**

KMS suspends automatic rotation. `DescribeKey` returns `AutomaticRotation = Suspended` . The rotation policy configuration is preserved and no new key versions are created.

**Scenario: CMK returns to Enabled state**

The automatic rotation policy becomes active again. KMS calculates the next rotation based on `LastRotationDate + RotationInterval` and resumes the schedule.

**Scenario: Updating the rotation policy on a non-Enabled CMK**

Do not call `UpdateRotationPolicy` on a CMK in the `Disabled` or `Pending Deletion` state.

**Limits**

The following keys do not support multiple key versions: Service-managed keys: the default keys managed by KMS for specific cloud services. These keys belong to the users of cloud services and are used to provide basic encryption protection for user data. BYOK-based keys: the keys that you imported to KMS. For more information, see Import and delete key material. The **Origin** attribute of these keys is EXTERNAL. KMS does not generate key material or initiate rotation tasks for these keys. These two types of keys do not support version-based manual or automatic key rotation. A BYOK-based key does not have multiple versions in KMS. Users have strong control over the persistence and lifecycle of BYOK-based keys. This makes management of the keys difficult and error-prone. For example, you must have on-premises key management facilities, data must be synchronized between on-premises facilities and the cloud, and no grace period is provided for key material deletion on the cloud. The complexity of maintaining multiple versions of BYOK-based keys makes key management much more risky. In addition, both primary and non-primary key versions may become unavailable at different points in time. For example, if key versions are deleted by KMS or imported again when they expire, CMKs may not be synchronized and encrypted data may fail to be decrypted due to the use of an invalid CMK. This affects system integrity.

> **Note:** For information about alternative solutions in the cases where version-based key rotation is not supported, see Manual CMK rotation.

### 9.3 Manual CMK rotation

If your CMKs do not support version-based automatic rotation, you can manually rotate the CMKs based on your scenario. This is an alternative solution that can be used regardless of whether automatic CMK rotation is supported.

**Scenario of custom data encryption**

On-premises or cloud applications can call KMS API operations to implement custom data encryption. Examples: Encrypt sensitive data such as ID card numbers, credit card numbers, and home addresses before you write it to databases. Encrypt data on a client before you upload the data to Object Storage Service (OSS). Encrypt application configuration files that contain sensitive data and service configuration files such as SSL certificates and private keys. You can use the key alias feature of KMS to rotate encryption keys within applications. The ID and alias of CMKs are not required when you call the Decrypt operation. In this scenario, the rotation process consists of the following steps:
1. Initial configuration
i. The administrator creates a CMK, whose ID is CMK-A. ii. The administrator binds the alias/MyAppKey alias to CMK-A. iii. When the application encryption module calls the Encrypt operation, the application encryption module sets the value of the **KeyId** parameter to alias/MyAppKey. KMS finds that the alias/MyAppKey alias is bound to CMK-A and then uses CMK-A to encrypt data. iv. When the application decryption module calls the Decrypt operation, the application decryption module does not set the **KeyId** parameter. KMS uses the CMK that is used to encrypt the data to decrypt the data. i. The administrator creates a CMK, whose ID is CMK-B. ii. The administrator calls the UpdateAlias operation to bind the alias/MyAppKey alias to CMK-B. iii. When the application decryption module calls the Encrypt operation, the application decryption module sets the value of the **KeyId** parameter to alias/MyAppKey. KMS finds that the alias/MyAppKey alias is bound to CMK-B and uses CMK-B to encrypt data. iv. When the application decryption module calls the Decrypt operation, the application decryption module does not set the **KeyId** parameter. KMS uses the CMK that is used to encrypt the data to decrypt the data.

**Scenario of server-side encryption by cloud services**

Cloud services can implement server-side encryption by calling KMS API operations. In this scenario, the following situations may occur from the perspective of key rotation: Automatic rotation policies configured in KMS affect the server-side encryption of cloud services. Cause: After encryption based on the specified CMK is configured for cloud services, these services call the GenerateDataKey operation of KMS to generate new data keys. When KMS generates a new primary key version, cloud services use the new version to encrypt the newly generated data keys. A typical example of such cloud services is OSS. In this case, if you want to enable automatic key rotation, you must not use service-managed keys or BYOK-based keys imported to KMS because these keys do not support automatic rotation. Automatic rotation policies configured in KMS do not affect server-side encryption of cloud services. Cause: After encryption based on the specified CMK is configured for cloud services, the services call the GenerateDataKey operation of KMS only once to generate keys to encrypt specific resources. When KMS generates a new primary key version, cloud services do not use this version. For example, Elastic Compute Service (ECS) calls the GenerateDataKey operation of KMS once to generate a volume encryption key. This key is not updated after it is created. If automatic rotation policies configured in KMS do not affect server-side encryption of cloud services or you want to rotate data keys when BYOK-based keys are used, you can modify configurations and copy data to achieve the same effect as key rotation. These methods depend on the features of different cloud services. For more information, see the documents of related cloud services.
