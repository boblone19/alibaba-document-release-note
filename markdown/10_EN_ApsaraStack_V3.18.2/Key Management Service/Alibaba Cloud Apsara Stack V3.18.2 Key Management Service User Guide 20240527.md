---
title: "Alibaba Cloud Apsara Stack V3.18.2 Key Management Service User Guide 20240527"
product_version: "V3.18.2"
doc_version: "20240527"
pdf_pages: 52
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Key Management Service User Guide 20240527.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1KMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Key%20Management%20Service%20User%20Guide%2020240527.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Key Management Service User Guide 20240527

## Table of Contents

- 1 Manage keys in the KMS console
  - 1.1 Log on to the KMS console
  - 1.2 Create a CMK
  - 1.3 View the details of a CMK
  - 1.4 Enable a CMK
  - 1.5 Disable a CMK
  - 1.6 Schedule a key deletion task
  - 1.7 Configure a rotation policy
  - 1.8 Generate a data key
  - 1.9 Generate a CSR
- 2 Use RAM for access control
- 3 Use aliases
- 4 Overview of CMKs
- 5 Use symmetric keys
  - 5.1 Overview
  - 5.2 EncryptionContext
  - 5.3 Import and delete key material
- 6 Use asymmetric keys
  - 6.1 Overview
  - 6.2 Encrypt and decrypt data by using an asymmetric CMK
  - 6.3 Generate and verify a digital signature by using an asymmetric CMK
- 7 Key rotation
  - 7.1 Overview
  - 7.2 Automatic key rotation
  - 7.3 Manual CMK rotation
- 8 Security Audit
  - 8.1 Overview
  - 8.2 Log on to the Apsara Uni-manager Management Console
  - 8.3 View the summary information about security audit
  - 8.4 Query audit events
  - 8.5 View raw logs
  - 8.6 View the number of logs
  - 8.7 Policy settings
    - 8.7.1 Manage audit rules
    - 8.7.2 Configure alert recipients
    - 8.7.3 Query the archives of audit events and raw logs
    - 8.7.4 Download exported audit events or logs
    - 8.7.5 Modify system settings

MS console

## 1 Manage keys in the KMS console

**console**

### 1.1 Log on to the KMS console

This topic describes how to log on to the Key Management Service (KMS) console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the operations administrator before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击右上角的**浏览**
**器证书安装**，可打开浏览器证书安装指南。
2. Enter your username and password.
Obtain the username and password that are used to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username as prompted. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**You log on to the Apsara Uni-manager Management Console for the first time**

**after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

MS console Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see **Manage MFA** in **Apsara** **Uni-manager Management Console User Guide**.

5. In the top navigation bar, choose **Products > Security > Key Management Service**.

### 1.2 Create a CMK

This topic describes how to create a customer master key (CMK) for subsequent encryption and decryption.

**Procedure**

1. Log on to the Key Management Service (KMS) console.
2. On the Keys page, click **Create Key**.
3. On the **Create key** page, select an organization from the **Organization** drop-down list.
Then, the **Resource set** and **Region** parameters are automatically configured.
4. In the **Basic configuration** section, configure the parameters.

| Parameter | Description |
|---|---|
| Key type | The type of the CMK. Valid values: Symmetric CMKs: Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ |
| Key usage | Valid values: ENCRYPT/DECRYPT SIGN/VERIFY |
| Protection level | Valid values: SOFTWARE: Use a software module to protect the CMK. |
| Alias | The alias of the CMK, which helps identify the CMK. Aliases are optional for CMKs. For more information, see Alias overview. |
| Description | The description of the CMK. |

5. In the **Advanced configuration** section, configure the parameters.
MS console

| Parameter | Description |
|---|---|
| Rotation cycle | Valid values: Do not open: does not enable automatic rotation. Open: enables automatic rotation. You can select a rotation interval or configure a custom rotation interval. Note You can configure this parameter only if you set the Key type parameter to Aliyun AES 256 or Aliyun SM4. _ _ _ If the Key material source parameter is set to External, automatic rotation is not supported. |
| Key material source | Valid values: Alibaba Cloud KMS: KMS generates key material. External: KMS does not generate key material. You must import your own key material to KMS. Note You can set this parameter only if the Key type parameter is set to Aliyun AES 256 or Aliyun SM4. _ _ _ |

6. Click **Submit**.

### 1.3 View the details of a CMK

After you create a CMK, you can view the details of the CMK, such as the key ID, status, purpose, and creation time.

**Procedure**

1. Log on to the KMS console. For more information, see Log on to the KMS console.
2. On the Keys page, find the CMK that you want to view and click its alias or choose
**More**>**Key Details** in the Actions column.
3. In the **Key Details** section, view the details of the CMK, such as the key ID, status,
purpose, and creation time.

### 1.4 Enable a CMK

This topic describes how to enable a CMK that is in the disabled state.

**Procedure**

1. Log on to the KMS console. For more information, see Log on to the KMS console.
2. Find a CMK in the **Disabled** state and click **Enable** in the **Actions** column.
3. In the **Enable Key** message, click **OK**.
After the CMK is enabled, the status of the CMK is changed from **Disabled** to **Enabled**. MS console

### 1.5 Disable a CMK

This topic describes how to disable a CMK.

**Background information**

If a CMK is disabled, the CMK cannot be used for encryption and decryption. The ciphertext encrypted by using this CMK cannot be decrypted until you re-enable the CMK.

**Procedure**

1. Log on to the KMS console. For more information, see Log on to the KMS console.
2. Find a CMK in the **Enabled** state and click **Disable** in the **Actions** column.
3. In the **Disable Key** message, click **OK**.
After the CMK is disabled, the status of the CMK is changed from **Enabled** to **Disabled**.

### 1.6 Schedule a key deletion task

You can schedule the deletion of a key by specifying a waiting period. After the period ends, the key is automatically deleted.

**Background information**

You can specify a waiting period of 7 to 30 days. Take note of the following items when you schedule the deletion of a key: During the waiting period, the key is in the Pending Deletion state. The key cannot be used to encrypt data, decrypt data, or generate data keys. Deleting a key may have a severe impact on data availability. In most cases, we recommend that you disable a key instead of deleting the key. After a key is deleted, the key cannot be recovered. The data encrypted by using this key and the data keys generated by using this key cannot be decrypted. Therefore, KMS only allows you to schedule the deletion of a key. You cannot immediately delete a key. KMS deletes the key within 24 hours after the specified waiting period ends. For example, if you submit a deletion application at 14:00, September 10, 2021 and specify a waiting period of seven days, KMS deletes the key within 24 hours after 14:00, September 17, 2021.

**Procedure**

1. Log on to the KMS console.
2. Find the key for which you want to schedule the deletion and choose **More** > **Schedule**
**Key Deletion** in the **Actions** column.
3. In the **Schedule Key Deletion** dialog box, configure **Delete In (7-30 days)**.
4. Click **OK**.

**Execution result**

The status of the key becomes **Pending Deletion**.

> **Note:** Before the waiting period ends, you can choose **More** > **Cancel Key** **Deletion** to cancel key deletion.

MS console

### 1.7 Configure a rotation policy

This topic describes how to configure a rotation policy of a customer master key (CMK).

**Procedure**

1. Log on to the Key Management Service (KMS) console
2. Find a symmetric key whose **Key Spec** is Aliyun_AES_256. In the **Actions** column, choose
**More** > **Key Details**.
3. In the **Key Version** section, click **Set Rotation Policy**.
4. In the **Set Rotation Policy** dialog box, set the **Rotation Period** parameter.
Disable: Disable automatic rotation for the CMK. 30 Days, 90 Days, 180 Days, and 365 Days: Select an automatic rotation interval. Customize: Allow you to specify a custom rotation interval.
5. Click **OK**.

### 1.8 Generate a data key

Data keys can be used to encrypt and decrypt on-premises data. This topic describes how to generate a data key.

**Procedure**

1. Log on to the Key Management Service (KMS) console.
2. Find a symmetric key whose key purpose is **Encrypt/Decrypt** and click its alias or choose
**More** > **Key Details**.

> **Note:** The key type for symmetric keys is Aliyun_AES_256.

3. In the **DataKey management** section, click **DataKey management**.
4. On the **Generate data key** tab, configure the parameters and click **Submit**.
i. In the **Generate dataKey parameters** section, configure the **Key Spec** and
**Encryption Context** parameters.
ii. In the **Generate dataKey parameters** section, set the **Export using public key**
**encryption** parameter. Valid values:
**Yes**: Encrypt a data key by using a specific public key and export the data key. In the
**Specify the export publicKey** section, configure the **Publickey Type**, **Public Key**,
and **Key Algorithm** parameters.
**No**: Export a data key without encrypting the data key by using a specific public key.
This way, you can directly generate a data key.

> **Note:** After the data key is generated, you can view the ciphertext of the data key in the **Data key export results** dialog box.

5. Optional. Click the **Data key transfer protection** tab, configure the parameters, and then
click **Submit**. MS console

| Transfer protection scenario | Related operation |
|---|---|
| Use public key to protect | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Encryption Context parameters. ii. In the Specify the export publicKey section, configure the Publickey Type, Public Key, and Key Algorithm parameters. |
| Data key transfer protection in the same region | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target KeyId and Target EncryptionContext parameters. |
| Data key transfer protection across regions | i. In the Parameters to export dataKey section, configure the Data Key Ciphertext and Source EncryptionContext parameters. ii. In the Target key parameters section, configure the Target RegionId, Target Asymmetric KeyID, Target Asymmetric KeyVersionID, Target KeyId, and Target EncryptionContext parameters. |

> **Note:** After transfer protection is configured for the data key, you can view the ciphertext of the data key in the **Data key transfer protection result** dialog box.

### 1.9 Generate a CSR

To generate a certificate, you must submit a certificate signing request (CSR) to a certificate authority (CA). This topic describes how to generate a CSR.

**Procedure**

1. Log on to the Key Management Service (KMS) console.
2. Find an asymmetric key whose key purpose is **Sign/Verify** and click its alias or choose
**More** > **Key Details**.

> **Note:** The key type for asymmetric keys is RSA_2048, EC_P256, or EC_P256K.

3. In the **Key Version** section, click **Generate CSR** in the **Actions** column.
4. In the **Generate CSR** dialog box, configure the parameters.
5. Click **Generate CSR**.
6. Click **Download CSR file** to save the CSR file to your on-premises computer.
ontrol

## 2 Use RAM for access control

Key Management Service (KMS) allows you to use Resource Access Management (RAM) to control access to KMS resources. This topic describes the KMS resource types, actions, and conditions that can be defined in RAM policies. Apsara Stack tenant accounts have full operation permissions on their own resources. RAM users and roles are granted only operation permissions on specified resources.

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

ontrol

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

ontrol

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

You can add conditions in RAM policies to control access to KMS. RAM authentication succeeds only when the added conditions are met. For example, you can add an `acs:CurrentTime` condition to control the period during which a RAM policy is valid. ontrol In addition to global conditions, you can use tags as filters to restrict the use of cryptographic operations such as Encrypt, Decrypt, and GenerateDataKey. Filters must be in the kms:tag/${tag-key} format.

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

`]` `}` `]` `}` A RAM policy that allows users to use keys that contain the following tag to perform cryptographic operations: Tag key: `Project` Tag value: `Apollo` ontrol `{`

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

## 3 Use aliases

Aliases are optional to CMKs. Aliases must be unique in a region for each Apsara Stack tenant account. An Alibaba Stack tenant account can use the same alias in different regions. An alias can be bound to only one CMK in a region, but a CMK can have multiple aliases.

**Overview**

Although each alias is bound to a CMK, aliases are resources independent from the CMKs to which they are bound. Take note of the following points about aliases: You can call the UpdateAlias operation to bind an alias to a different CMK. This operation does not affect the original CMK. If you delete an alias, the CMK to which the alias is bound is not deleted. RAM users must be authorized before they can perform operations on an alias. For more information, see Use RAM for access control. Aliases cannot be modified. To change the alias of a CMK, you must delete the original alias and create another one for the CMK. You can replace the CMK ID in the request parameters of the following API operations with an alias that is bound to the CMK: DescribeKey Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext

> **Note:** For more information about the API operations, see the **API reference** topic of **Developer Guide**.

To specify an alias instead of a CMK ID in the request parameters of the preceding operations, a RAM user must have the relevant permissions on the CMK. The RAM user does not need to have permissions on the alias. When you use an alias, you must make sure that the alias is complete. Example:

```
// A complete alias must have the alias/ prefix. alias/example
```

**Create an alias**

An alias must contain the `alias/` prefix. An alias, excluding the prefix, can contain letters, digits, underscores (_), hyphens (-), and forward slashes (/). An alias, excluding the prefix, must be 1 to 255 characters in length. To allow a RAM user to create an alias, you must create a custom policy to grant the RAM user the permissions on the alias and the CMK to which the alias is bound. The following sample policy allows User 123456 to create an alias named `alias/example` for CMK 08ec3bb9-034f-485b-b1cd-3459baa8****: `{`

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

You can use one of the following methods to create an alias: Create an alias in the KMS console. i. Log on to the KMS console. ii. In the left-side navigation pane, click **Keys**. iii. Find the CMK for which you want to create an alias and click its alias. In the Aliases section, click **Create Alias**. iv. In the **Create Alias** dialog box, set the Alias Name parameter. v. Click **OK**. Create an alias by calling the CreateAlias operation. Create an alias by running the `aliyun kms CreateAlias` command in Apsara Stack CLI.

```
aliyun kms CreateAlias --KeyId 08ec3bb9-034f-485b-b1cd-3459baa8**** --AliasName alias /example
```

**Bind an alias to a different CMK**

You can bind an existing alias to a different CMK. To allow a RAM user to bind an existing alias to a different CMK, you must create a custom policy to grant the RAM user the permissions on the original CMK, new CMK, and alias. The following sample policy allows User 123456 to bind the `alias/example` alias to CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****. The original CMK to which this alias is bound is 08ec3bb9-034f-485b-b1cd-3459baa8****. `{`

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

`]` `}` `]` `}` You can use one of the following methods to bind an alias to a different CMK: Bind an alias to a different CMK by calling the UpdateAlias operation. Bind an alias to a different CMK by running the `aliyun kms UpdateAlias` command in Apsara Stack CLI.

```
aliyun kms UpdateAlias --AliasName alias/example --KeyId 127d2f84-ee5f-4f4d-9d41-dbc1 aca2****
```

**Delete an alias**

You can delete aliases that are not required. If you delete an alias, the CMK to which the alias is bound is not affected. To allow a RAM user to delete an alias, you must create a custom policy to grant the RAM user the permissions on the alias and the CMK to which the alias is bound. The following sample policy allows User 123456 to delete the `alias/example` alias that is bound to CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****: `{`

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

`]` `}` `]` `}` You can use one of the following methods to delete an alias: Delete an alias in the KMS console. i. Log on to the KMS console. ii. In the left-side navigation pane, click **Keys**. iii. Find the CMK for which you want to delete an alias and click its alias. iv. In the **Aliases** section, click **Delete Alias** next to the alias to be deleted. v. In the **Delete Alias** message, click **OK**. Delete an alias by calling the DeleteAlias operation. Delete an alias by running the `aliyun kms DeleteAlias` command in Apsara Stack CLI.

```
aliyun kms DeleteAlias --AliasName alias/example
```

**Query aliases**

You can query all aliases that belong to your Apsara Stack tenant account in the current region. To allow a RAM user to query aliases, you must create a custom policy to grant the RAM user the permissions on aliases. The following sample policy allows User 123456 to query aliases: `{`

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

`]` `}` `]` `}` You can use one of the following methods to query aliases: Query aliases by calling the ListAliases operation. Query aliases by running the `aliyun kms ListAliases` command in Apsara Stack CLI.

```
aliyun kms ListAliases
```

**Query aliases bound to a specified CMK**

If you query the aliases bound to a specified CMK, only the related aliases are returned. To allow a RAM user to query the aliases bound to a specified CMK, you must create a custom policy to grant the RAM user the permissions on the CMK. The following sample policy allows User 123456 to query the aliases bound to CMK 127d2f84-ee5f-4f4d-9d41-dbc1aca2****: `{`

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

`]` `}` `]` `}` You can use one of the following methods to query aliases bound to a specified CMK: Query aliases bound to a specified CMK by calling the ListAliasesByKeyId operation. Query aliases bound to a specified CMK by running the `aliyun kms ListAliasesByKeyId` command in Apsara Stack CLI.

```
aliyun kms ListAliasesByKeyId --KeyId 127d2f84-ee5f-4f4d-9d41-dbc1aca2****
```

## 4 Overview of CMKs

The key service is a core component of Key Management Service (KMS). The key service provides fully managed keys and key protection features. The key service supports simple data encryption and digital signature management based on cloud-native API operations.

**Algorithms**

The following table describes the encryption algorithms supported by KMS.

| Algorithm class | Algorithm subclass | Encryption and decryption | Signing and verification |
|---|---|---|---|
| Symmetric key | AES | Supported | Not supported |
| Asymmetric key | RSA | Supported | Supported |
| Asymmetric key | ECC | Not supported | Supported |

Symmetric keys are used to encrypt or decrypt data. If you do not specify the KeySpec parameter during key creation, KMS creates a symmetric key. You can call the Encrypt or Decrypt operation to encrypt or decrypt data without the need to obtain the plaintext of a symmetric key. For more information, see Overview of symmetric encryption. Asymmetric keys can be used to encrypt data, decrypt data, sign data, or verify a signature. An asymmetric customer master key (CMK) in Key Management Service (KMS) consists of a public key and a private key, which are cryptographically related to each other. The public key can be sent to all users, but the private key must be protected. To protect the private key, KMS does not provide an API operation for you to export the private key of an asymmetric key. You can use a private key to decrypt data or sign data by calling the related operations. Users with a public key can use the public key to encrypt data or verify the signature that is generated by using the matched private key. For more information, see Overview of asymmetric keys.

> **Note:** Only KMS of the Advanced edition supports Rivest-Shamir-Adleman (RSA) and elliptic-curve cryptography (ECC) keys.

**Key owner**

In most cases, you are the owner of your CMKs in KMS, and their Creator attributes are set to the ID of your Apsara Stack tenant account. Apsara Stack services can be integrated with KMS to implement server-side encryption (SSE). In this scenario, KMS allows a service to automatically manage an encryption key that can be used only by the service to encrypt your data. This makes it easier for you to use the entrylevel data encryption features and reduces your workload in the management of key lifecycles and permissions. These service-managed keys are called service keys. To identify a service key, the Creator attribute of the service key is assigned the code of the associated service. The service key is associated with an alias that is in the `acs/<code of the service>` format. For example, the Creator attribute of the service key managed by Object Storage Service (OSS) is set to OSS and the acs/oss alias is associated with the service key.

## 5 Use symmetric keys

### 5.1 Overview

This topic describes symmetric encryption, which is the most commonly used data encryption method. KMS provides easy-to-use API operations that allow you to encrypt and decrypt data on the cloud.

> **Note:** For more information about the API operations, see the **API reference** topic of Developer Guide.

If you do not specify the KeySpec parameter during key creation, KMS creates a symmetric key. KMS supports popular symmetric key algorithms and provides high-level data security by using strong cryptography.

**Types of symmetric keys**

The following table describes the types of symmetric keys that Key Management Service (KMS) supports.

| Algorithm | Key length | Key specification | Data encryption mode | Protection level |
|---|---|---|---|---|
| AES | 256 bits | Aliyun AES 256 _ _ | GCM | Software |

**Encryption and decryption features**

To encrypt data, you need to only specify the ID or alias of a customer master key (CMK). KMS uses the specified CMK for encryption and returns the ciphertext. When you call the Decrypt operation to decrypt data, you need to only specify the ciphertext that you want to decrypt. You do not need to specify the CMK. The Decrypt operation is available for you to decrypt the ciphertext that is generated by calling the Encrypt, GenerateDataKey, or GenerateDataKeyWithoutPlaintext operation.

**AAD**

Symmetric keys of KMS use Galois/Counter Mode (GCM) for block ciphers. You can use additional authenticated data (AAD) to provide supplemental protection for the integrity of encrypted data. KMS encapsulates the AAD input. This way, you can configure and include your own authentication data in an efficient manner. For more information, see EncryptionContext.

**Envelope encryption**

KMS allows you to generate a two-level key hierarchy to accelerate envelope encryption by calling the GenerateDataKey and GenerateDataKeyWithoutPlaintext operations. For more information about envelope encryption, see the Envelope encryption in the
**Features** topic of Technical White Paper.

**Rotation of symmetric keys**

Each symmetric CMK that is generated in KMS supports multiple key versions. KMS automatically rotates CMKs by generating new key versions. You can customize the key rotation policy. If a CMK has multiple versions, the latest version of the CMK is used in the Encrypt, GenerateDataKey, and GenerateDataKeyWithoutPlaintext operations to encrypt data. To decrypt the data, you do not need to specify the ID or the CMK or key version. KMS automatically identifies the CMK and its key version with which the data is encrypted. Then, KMS uses the key material of the identified key version to decrypt the ciphertext. KMS rotates a CMK by generating a new version of the CMK. After a rotation is complete, KMS automatically uses the new key version to encrypt data. However, the earlier key version is still available for decrypting the ciphertext generated before the rotation. For more information, see Automatic key rotation.

**BYOK feature**

KMS allows you to encrypt your data in the cloud by using the Bring Your Own Key (BYOK) feature. This feature helps you meet stringent security and compliance requirements. We recommend that you use a managed hardware security module (HSM) to protect your keys by importing key material into CMKs with HSM-grade security. The keys imported into the managed HSM can only be destroyed, and their plaintext cannot be exported.

### 5.2 EncryptionContext

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

### 5.3 Import and delete key material

**material**

This topic describes how to import and delete external key material for a CMK.

**Background information**

CMKs are basic resources of KMS. A CMK is composed of a key ID, basic metadata such as key status, and key material that is used to encrypt and decrypt data. By default, KMS generates key material when you call the CreateKey operation to create a CMK. You can select an external key as the material source. In this case, KMS does not create key material. You must import external key material to the CMK. You can call the DescribeKey operation to check the key material source of an existing CMK.

> **Note:** For more information about the API operations, see the **API reference** topic of **Developer Guide**.

Keys can be divided into normal keys and external keys based on the source of key material. If the value of the **Origin** parameter in KeyMetadata is Aliyun_KMS, the key material is generated by KMS. In this case, the CMK is considered a **regular CMK**. If the value of the **Origin** parameter is EXTERNAL, the key material is imported from an external source. In this case, the CMK is considered an **external CMK**. Before you import external key material, take note of the following points: Make sure that the source of randomness from which the key material is generated meets security requirements. Make sure that the key material is reliable. KMS ensures the high availability of imported key material. However, KMS cannot ensure that the imported key material has the same reliability as the key material generated by KMS. You can call the DeleteKeyMaterial operation to delete the key material that you have imported. You can also set a validity period to enable KMS to automatically delete the key material after the validity period ends. The CMK is not deleted. To delete key material generated by KMS, you can only call the ScheduleKeyDeletion operation to specify a waiting period of 7 to 30 days for deleting the CMK. The key material is deleted with the relevant CMK after the waiting period ends. After you delete the imported key material, you can re-import the same key material to make the relevant CMK available again. Therefore, we recommend that you save a copy of the key material. A CMK can have only one piece of key material. After you import key material into a CMK, the CMK is bound to the key material. Even after the key material is expired or deleted, you cannot import a different piece of key material into that CMK. If you need to rotate a CMK that uses external key material, you must create a CMK and then import new key material. CMKs are independent. You cannot use a CMK to decrypt data that is encrypted by using another CMK, even if the two CMKs use the same key material. The key material to be imported must be a 256-bit symmetric key.

**Import key material**

1. Create an external key.
You can use one of the following methods to create an external key: Method 1: Log on to the KMS console and click Create Key. On the Create Key page, set the Key Material Source parameter to External in the Advanced Settings section. For more information, see Create a CMK. Method 2: Call the CreateKey operation. Set the **Origin** parameter to EXTERNAL.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms CreateKey --Origin EXTERNAL --Description "External key"
```

2. Obtain the parameters that are used to import key material.
The parameters include a public key and an import token. The public key is used to encrypt the key material. You can use one of the following methods to obtain the parameters: Method 1: Obtain the parameters in the KMS console. Method 2: Obtain the parameters by calling the GetParametersForImport operation.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms GetParame tersForImport --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --WrappingAlgorithm RSAE S_OAEP_SHA_1 --WrappingKeySpec RSA_2048
```

3. Import key material.

> **Note:** You can import key material into an external key that does not have key material. You can also reset the expiration time of key material or re-import key material that has expired or been deleted.
> Each import token is bound to a public key that is used to encrypt key material. A CMK is specified when an import token is generated. The import token can only be used to import key material into the specified CMK.
> The lifecycle of an import token is 24 hours. It can be used repeatedly within this period. After it expires, you must obtain a new import token and a new public key.

i. Use the public key to encrypt the key material. The public key is a 2,048-bit Rivest-Shamir-Adleman (RSA) public key. The encryption algorithm must be the same as that specified when you obtain the parameters that are used to import the key material. The public key returned when you call the GetParametersForImport operation is Base64-encoded. You must first decode the public key. KMS supports the following encryption algorithms: RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256, and RSAES_PKCS1_V1_5. ii. Encode the encrypted key material in the Base64 format. iii. Call the ImportKeyMaterial operation to import the encoded key material and the import token to KMS.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${please-repleace-your-endpoint} --access-key-id ${please-repleace-your-accesskey-id} --access-key-secret ${please-repleace-your-access-key-secret} kms ImportKey Material --KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8**** --EncryptedKeyMaterial xxx -- ImportToken xxxx
```

**Delete key material**

After you import key material into an external key, you can use the external key in the same way as a normal key. The only difference lies in that the key material of an external key may expire and can be independently deleted. After the key material of an external key expires or is deleted, the external key can no longer be used, and the ciphertext encrypted by using this external key cannot be decrypted. To use the external key and decrypt the related ciphertext again, you must re-import the same key material. If an external key is in the PendingDeletion state when its key material expires or is deleted, the key status does not change after the key material expires or is deleted. Otherwise, the key status becomes PendingImport after the key material expires or is deleted. You can use one of the following methods to delete key material: Method 1: Delete the key material in the KMS console. Method 2: Delete the key material by calling the DeleteKeyMaterial operation.

```
./aliyun --skip-secure-verify --region ${please-repleace-your-region} --endpoint ${ please-repleace-your-endpoint} --access-key-id ${please-repleace-your-access-key-id} --access-key-secret ${please-repleace-your-access-key-secret} kms DeleteKeyMaterial - -KeyId 1339cb7d-54d3-47e0-b595-c7d3dba8****
```

**Use OpenSSL to encrypt and upload key material**

1. Create an external key.
2. Create key material.
The key material must be a 256-bit symmetric key. In this example, OpenSSL is used to generate a 32-byte random number.

```
openssl rand -out KeyMaterial.bin 32
```

3. Obtain parameters that are used to import the key material.
4. Encrypt the key material.
i. Decode the public key that is used to encrypt the key material in the Base64 format. ii. Use an encryption algorithm such as RSAES_OAEP_SHA_1 to encrypt the key material. iii. Encode the encrypted key material in the Base64 format and save it to a text file.

```
openssl rand -out KeyMaterial.bin 32 openssl enc -d -base64 -A -in PublicKey_base64.txt -out PublicKey.bin openssl rsautl -encrypt -in KeyMaterial.bin -oaep -inkey PublicKey.bin -keyform DE R -pubin -out EncryptedKeyMaterial.bin openssl enc -e -base64 -A -in EncryptedKeyMaterial.bin -out EncryptedKeyMaterial_base64.txt
```

iv. Upload the encrypted key material and import token.

**Example**

Use SDK for Java to encrypt and upload key material

```java
// Use the latest KMS SDK for Java. //KmsClient.java import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.kms.model.v20160120.*; import com.aliyuncs.profile.DefaultProfile; // Encapsulate KMS API operations public class KmsClient {
    DefaultAcsClient client;
    public KmsClient(String regionId, String ak, String secret) {
        DefaultProfile profile = DefaultProfile.getProfile(regionId, ak, secret);
        this.client = new DefaultAcsClient(profile);
```

`}`

```
    // Specify a custom endpoint. In most cases, a VPC endpoint is specified. You can a
lso specify a custom endpoint when you cannot obtain the IP address in the Apsara Stack environment based on the regionId parameter.
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
returnthisclientgetAcsResponse(request);
```

```
        return this.client.getAcsResponse(request);
```

`}`

```
    //... Omitted. The remaining operations are encapsulated in the same way as the pre
ceding operations.
```

`}`

```java
//example.java import com.aliyuncs.kms.model.v20160120.*; import javax.crypto.Cipher; import javax.crypto.spec.OAEPParameterSpec; import javax.crypto.spec.PSource.PSpecified; import javax.xml.bind.DatatypeConverter; import java.security.KeyFactory; import java.security.PublicKey; import java.security.spec.MGF1ParameterSpec; import java.security.spec.X509EncodedKeySpec; import java.util.Random; public class CreateAndImportExample {
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
            // Generate a 32-byte random number.
            byte[] keyMaterial = new byte[32];
            new Random().nextBytes(keyMaterial);
            // Obtain the parameters that are used to import key material.
            GetParametersForImportResponse paramResponse =
kmsclient.getParametersForImport(keyId, "RSA_2048", "RSAES_OAEP_SHA_256");
            String importToken = paramResponse.getImportToken();
            String encryptPublicKey = paramResponse.getPublicKey();
            // Decode the public key in the Base64 format.
            byte[] publicKeyDer =
DatatypeConverter.parseBase64Binary(encryptPublicKey);
            // Use RSA to parse the public key.
            KeyFactory keyFact = KeyFactory.getInstance("RSA");
            X509EncodedKeySpec spec = new X509EncodedKeySpec(publicKeyDer);
            PublicKey publicKey = keyFact.generatePublic(spec);
            // Encrypt the key material.
            Cipher oaepFromAlgo = Cipher.getInstance("RSA/ECB/OAEPWithSHA-
1AndMGF1Padding");
            String hashFunc = "SHA-256";
            OAEPParameterSpec oaepParams = new OAEPParameterSpec(hashFunc, "MGF1", new
MGF1ParameterSpec(hashFunc), PSpecified.DEFAULT); oaepFromAlgo.init(Cipher.ENCRYPTMODE,publicKey,oaepParams);
```

```
            oaepFromAlgo.init(Cipher.ENCRYPT_MODE, publicKey, oaepParams);
            byte[] cipherDer = oaepFromAlgo.doFinal(keyMaterial);
            // Encode the encrypted key material in the Base64 format.
            String encryptedKeyMaterial =
DatatypeConverter.printBase64Binary(cipherDer);
            // Import the key material.
            Long expireTimestamp = 1546272000L; // The UNIX timestamp, which is precise
to the second. The value 0 indicates that the key material does not expire.
            kmsclient.importKeyMaterial(keyId, importToken, encryptedKeyMaterial,
expireTimestamp);
        } catch (Exception e) {
            //... Omitted.
```

`}` `}` `}`

## 6 Use asymmetric keys

### 6.1 Overview

Unlike symmetric keys, asymmetric keys are used to verify digital signatures or encrypt sensitive information between systems with different trust levels. You can create asymmetric customer master keys (CMKs) in Key Management Service (KMS). An asymmetric key pair consists of a public key and a private key, which are cryptographically related to each other. The public key is available for all users, but the private key must be protected and used only by trusted users. KMS supports popular asymmetric key algorithms and provides sufficient security strength to ensure the security of encrypted data and digital signatures.

**Types of asymmetric keys**

The following table describes the types of asymmetric keys that KMS supports.

| Algorithm | Key specification | Description | Usage |
|---|---|---|---|
| RSA | RSA 2048 _ | Rivest-Shamir- Adleman (RSA) | Encrypt or decrypt data. Sign data. |
| ECC | EC P256: National _ Institute of Standards and Technology (NIST)- recommended elliptic curve P-256 EC P256K: _ Standards for Efficient Cryptography Group (SECG) elliptic curve secp256k1 | Elliptic-curve cryptography (ECC) | Sign data. |

**Encrypt data**

Asymmetric keys are used to encrypt and transmit sensitive information. The following steps describe a typical scenario:
1. An information receiver distributes a public key to a transmitter.
2. The transmitter uses the public key to encrypt sensitive information.
3. The transmitter sends the ciphertext generated from the sensitive information to the
information receiver.
4. The information receiver uses the private key to decrypt the ciphertext.
The private key can be used only by the information receiver. This ensures that the plaintext of sensitive information cannot be intercepted and decrypted by unauthorized parties during transmission. This encryption method is widely used to exchange keys. For example, session keys are exchanged in Transport Layer Security (TLS) handshakes, and encryption keys are exported and imported between different hardware security modules (HSMs). For more information, see Encrypt and decrypt data by using an asymmetric CMK.

**Sign data.**

Asymmetric keys are also used to generate digital signatures. Private keys can be used to sign messages or information. Private keys are strictly protected and can be used only by trusted users to generate signatures. After a signature is generated, you can use the corresponding public key to verify the signature to achieve the following purposes: Verify data integrity. If the data does not match its signature, the data may be tampered with. Verify message authenticity. If a message does not match its signature, the message transmitter does not hold the private key. Provide non-repudiation for signatures. If the data matches its signature, the signer cannot deny this signature. The following operations describe a typical signature verification scenario:
1. A signer sends a public key to a receiver.
2. The signer uses the private key that matches the public key to sign data.
3. The signer sends the data and signature to the message receiver.
4. After the data and signature are received, the receiver uses the public key to verify the
signature. Digital signatures are widely used to defend against data tampering and authenticate identities. For more information, see Asymmetric signature.

**Key versions**

KMS does not support automatic rotation of asymmetric CMKs due to the limits of public and private keys. You can call the CreateKeyVersion operation to create another key version in a specific CMK and generate a new pair of public and private keys. If you use a new key version to generate a digital signature or encrypt data, you must also distribute the new version of the public key. In contrast to symmetric CMKs, asymmetric CMKs do not have a primary key version. Therefore, when you call operations related to asymmetric CMKs in KMS, you must specify the CMK ID or CMK alias, and a key version.

**Public key operations**

In most cases, you can call the GetPublicKey operation to obtain a public key and distribute the public key to users for encryption or verification. Then, the users can use cryptographic libraries such as OpenSSL and Java Cryptography Extension (JCE) to perform calculation in their business systems. You can also call the AsymmetricEncrypt or AsymmetricVerify operation to perform public key operations. KMS records the logs of the calls and provides the capability to restrict the usage of public keys using Resource Access Management (RAM). Compared with calculation in business systems, KMS offers flexible features that better suit your needs.

**Private key operations**

You can only call the AsymmetricDecrypt or AsymmetricSign operation to decrypt data or sign data by using a private key.

### 6.2 Encrypt and decrypt data by using an asymmetric CMK

**using an asymmetric CMK**

This topic describes how to use an asymmetric customer master key (CMK) to encrypt and decrypt data in Alibaba Cloud CLI. Asymmetric encryption and decryption generally include the following steps:
1. An information receiver distributes a public key to an information transmitter.
2. The information transmitter uses the public key to encrypt sensitive information.
3. The information transmitter sends the ciphertext that is generated from the sensitive
information to the information receiver.
4. The information receiver uses the private key to decrypt the ciphertext.

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

**Call the KMS API operation to decrypt data**

You must call the KMS API operation and use the private key to decrypt data.
1. Before you transmit the ciphertext over the network, encode it in Base64.

```
openssl base64 -in plaintext-file.enc
```

Expected output:

```
5kdCB06HHeAwgfH9ARY4/9Nv5vlpQ94GXZcmaC9FE59Aw8v8RYdozT6ggSbyZbi+ 8STKVq9402MEfmUDmwJLuu0qgAZsCe5wU4JWHh1y84Qn6HT068j0qOy5X2HIlrjs fCdetgtMtVorSgb3bbERk2RV67nHWrDkecNbUaz+6ik4AlZxv2uWrV62eQ9yUBYm Jb956LbqnfWdCFxUSHH/qB5QCnLpijzvPmfNlZr653H4nF08gpZjnmlF4FjTu3i2 mGLzK4J3Rh/l7PQHiVMdc4hSnXosg68QmMVdZBGLK9/cD9SYngPDiirU7z0q7Git dIeloyCAUDFyuQC6a+SqzA==
```

2. Pass the Base64-encoded ciphertext to KMS to decrypt data.

```
aliyun kms AsymmetricDecrypt \
  --KeyId 5c438b18-05be-40ad-b6c2-3be6752c**** \
  --KeyVersionId 2ab1a983-7072-4bbc-a582-584b5bd8**** \
  --Algorithm RSAES_OAEP_SHA_256 \
  --CiphertextBlob
5kdCB06HHeAwgfH9ARY4/9Nv5vlpQ94GXZcmaC9FE59Aw8v8RYdozT6ggSbyZbi+8STKVq9402MEfmUDmwJLuu0qg sCe5wU4JWHh1y84Qn6HT068j0qOy5X2HIlrjsfCdetgtMtVorSgb3bbERk2RV67nHWrDkecNbUaz+6ik4AlZxv2uW 62eQ9yUBYmJb956LbqnfWdCFxUSHH/qB5QCnLpijzvPmfNlZr653H4nF08gpZjnmlF4FjTu3i2mGLzK4J3Rh/l7PQ VMdc4hSnXosg68QmMVdZBGLK9/cD9SYngPDiirU7z0q7GitdIeloyCAUDFyuQC6a+SqzA==
```

Expected output: `{`

```json
        "KeyId": "5c438b18-05be-40ad-b6c2-3be6752c****",
        "KeyVersionId": "2ab1a983-7072-4bbc-a582-584b5bd8****",
        "Plaintext": "dGhpcyBpcyBwbGFpbnRleHQgDQo=",
        "RequestId": "6be7a8e4-35b9-4549-ad05-c5b1b535a22c"
```

`}`
3. Decode the returned Base64-encoded plaintext in Base64.

```
echo dGhpcyBpcyBwbGFpbnRleHQgDQo= | openssl base64 -d
```

The following plaintext after decryption is returned:

```
this is plaintext
```

### 6.3 Generate and verify a digital signature by using an asymmetric CMK

**signature by using an asymmetric**

**CMK**

This topic describes how to use an asymmetric customer master key (CMK) to generate and verify a digital signature. In this topic, Alibaba Cloud CLI is used. You can also use KMS SDKs. Asymmetric encryption includes the following steps:
1. A signer sends a public key to a receiver.
2. The signer uses the private key to sign data.
3. The signer sends the data and signature to the receiver.
4. After the receiver receives the data and signature, the receiver uses the public key to verify
the signature.

**Before you start**

Call the CreateKey operation to create an asymmetric CMK in KMS. Set the KeySpec parameter to a desired key type and the KeyUsage parameter to `SIGN/VERIFY` . Create an RSA signature key:

```
aliyun kms CreateKey --KeySpec=RSA_2048 --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

Create a NIST P-256 signature key:

```
aliyun kms CreateKey --KeySpec=EC_P256 --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

Create a secp256k1 signature key:

```
aliyun kms CreateKey --KeySpec=EC_P256K --KeyUsage=SIGN/VERIFY --ProtectionLevel=HSM
```

**Preprocessing before signing: Compute a message digest**

Both RSA and ECC signature operations involve first computing the digest of an unsigned message and then signing the digest.

> **Note:** The algorithm that is used to compute a message digest must match the algorithm that is specified when you call the KMS API operations to generate a signature. For example, the ECDSA_SHA_256 signature algorithm must be used in conjunction with the SHA-256 digest algorithm. The ECDSA_SHA_256 signature algorithm does not match the SHA-384 digest algorithm.

In the following examples, the SHA-256 digest algorithm is used.
1. Save the "this is message" message that needs to be signed to the message-file.txt file:

```
echo "this is message" > message-file.txt
```

2. Compute the SHA-256 digest of the message and save the binary digest to the message-
sha256.bin file:

```
openssl dgst -sha256 -binary -out message-sha256.bin message-file.txt
```

**Call the KMS API operations to generate the signature**

You must call the KMS API operations to generate the signature of a message by using the private key.
1. Before you transmit the message digest over the network, encode the message digest in
Base64.

```
openssl base64 -in message-sha256.bin
```

The following Base64 encoded digest is returned:

```
uCx5YpLfBrqoYMP8Hf9H7j9/1zT+PPxq1qJRW6uQbos=
```

2. Pass the Base64 encoded digest to KMS to generate a signature.

> **Note:** The parameters passed and the results returned vary based on key types and signature algorithms. Each signature result returned in the example is stored in a different file.

**RSASSA-PSS**

For RSA keys, you can use the RSASSA-PSS signature algorithm and the SHA-256 digest algorithm to generate a signature. Run the following command:

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

`}` Decode the signature value in Base64 and generate a binary signature. This signature is saved in the file rsa_pss_signature.bin:

```
echo J7xmdnZ... | openssl base64 -d -out rsa_pss_signature.bin
```

**RSASSA_PKCS1_V1_5**

For RSA keys, you can use the RSASSA_PKCS1_V1_5 signature algorithm and the SHA-256 digest algorithm to generate a signature. Run the following command:

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

`}` Decode the signature value in Base64 and generate a binary signature. This signature is saved in the file rsa_pkcs1_signature.bin:

```
echo qreBkH/u... | openssl base64 -d -out rsa_pkcs1_signature.bin
```

**NIST P-256**

For NIST curve P-256, you can use the ECDSA signature algorithm and the SHA-256 digest signature to generate a signature. Run the following command:

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

`}` Decode the signature value in Base64 and generate a binary signature. This signature is saved in the file ec_p256_signature.bin:

```
echo MEYCIQD33Y98... | openssl base64 -d -out ec_p256_signature.bin
```

**secp256k1**

Run the following command:

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

`}` Decode the signature Value in Base64 and generate a binary signature. This signature is saved in the file ec_p256k_signature.bin:

```
echo MEYCIQDWuuI... | openssl base64 -d -out ec_p256k_signature.bin
```

**Obtain the public key**

Obtain the public key of the created asymmetric key pair from the KMS. The preceding example assumes that: The public key of the RSA CMK is saved to the file rsa_publickey.pub. The public key of the NIST P-256 CMK is saved to the file ec_p256_publickey.pub. The public key of the secp256k1 CMK is saved to the file ec_p256k_publickey.pub.

**Use the public key to verify the signature**

Run the following commands to verify the signature. The commands vary based on the key type and signature algorithm that are used.

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

If the signature passes verification, the system returns the following message:

```
Verified OK
```

## 7 Key rotation

### 7.1 Overview

Keys are used to protect specific data. Therefore, the security of the data depends on the security of its keys. You can regularly rotate keys between key versions to improve key security and implement security policies and best practices for data protection.

**Achieve security goals**

You can regularly rotate keys to achieve the following goals: Reduce the amount of data encrypted based on each key The security of a key is inversely proportional to the amount of data encrypted based on the key. This amount is usually defined by the total bytes of data or the total number of messages that are encrypted based on the same key. For example, National Institute of Standards and Technology (NIST) defines the secure lifecycle of a key in Galois/Counter Mode (GCM) as the total number of messages encrypted based on the key. Regular key rotation allows each key to remain secure and minimizes vulnerability to cryptanalytic attacks. Respond in advance to security events In the early days of system design, key rotation was introduced as a routine operations and maintenance (O&M) method. This provides the system with a method to handle security events when they occur, and complies with the fail early, fail often principle of software engineering. If key rotation is not executed in the system until an emergency event has already occurred, the probability of system failure increases exponentially. Provide logical isolation of data Data encrypted before a key rotation is isolated from data encrypted after the key rotation. The impact of key-related security events can be identified and preventive measures can be taken. Reduce the window of time to crack keys Regular rotation of encryption keys ensures that you can control and reduce the window of time during which the key and its encrypted data are vulnerable to being cracked. The interval between rotation tasks during which attackers are able to crack the key is limited. This practice greatly increases the security of your data against cryptanalytic attacks.

**Meet the requirements of regulatory compliance**

Regular key rotation facilitates compliance with various regulations, which include but are not limited to the following regulations: Payment Card Industry Data Security Standard (PCI DSS) Cryptography-related industrial standards issued by State Cryptography Administration, such as GM/T 0051-2016 Cryptography-related standards issued by NIST, such as NIST Publication 800-38D

### 7.2 Automatic key rotation

This topic shows you how to configure automatic rotation of CMKs in KMS.

**Key versions**

A CMK may have multiple key versions. Each key version represents an independently generated key. Key versions of the same CMK do not have a cryptographic relation to each other. KMS automatically rotates CMKs by generating new key versions. Key versions are divided into the following types: Primary key versions The primary key version of a CMK is an active encryption key. Each CMK has only one primary key version at a point in time. When you call an encryption operation such as GenerateDataKey or Encrypt, KMS uses the primary key version of a specified CMK to encrypt plaintext. You can call the DescribeKey operation to query the **PrimaryKeyVersion** attribute. Non-primary key versions The non-primary key version of a CMK is an inactive encryption key. Each CMK can have zero to multiple non-primary key versions. Each non-primary key version was a primary key version and acted as the active encryption key in the past. When a new primary key version is created, KMS does not delete or disable non-primary key versions, which are needed to decrypt data.

> **Note:** When you call an encryption operation, the primary key version of a specified CMK is used. When you call a decryption operation, the key version that was used for encryption is used.

You can generate a key version in one of the following ways: Create a CMK. You can call the CreateKey operation to create a CMK. If you set the **Origin** parameter to Aliyun_KMS, KMS generates an initial key version and sets it as the primary key version. Execute an automatic rotation policy. After you configure an automatic rotation policy for a CMK, KMS executes the policy on a regular basis to generate key versions.

**Automatic rotation**

Configure a key rotation policy. When you call the CreateKey operation to create a CMK, you can specify an automatic rotation policy for the CMK. You can call the UpdateRotationPolicy operation to update the current automatic rotation policy. When you call the operations, you must configure the following parameters:
**EnableAutomaticRotation**: specifies whether to enable automatic rotation.
**RotationInterval**: the interval for automatic rotation.
You can call the DescribeKey operation to view the configured automatic rotation policy. The following parameters are returned:
**AutomaticRotation**: indicates whether automatic rotation is enabled. The value Disabled
indicates that automatic rotation is disabled. The value Enabled indicates that automatic rotation is enabled. The value Suspended indicates that KMS suspends the execution of automatic rotation although automatic rotation is enabled.
**RotationInterval**: indicates the interval for automatic rotation.
Execute an automatic rotation policy. When automatic rotation is enabled, KMS calculates the time of the next rotation by using the following formula:

```xml
<NextRotationTime> = <LastRotationTime> + <RotationInterval>
```

where: `LastRotationTime` : the time when the last key version was created. You can call the DescribeKey operation and check the `LastRotationDate` parameter to obtain the time. `NextRotationTime` : the time when KMS performs the next rotation task to create a key version. You can call the DescribeKey operation and check the `NextRotationDate` parameter to obtain the time.

> **Important:** When you update the RotationInterval parameter of an automatic rotation policy, the value of NextRotationTime may be a point in time in the past. This does not affect the execution of the automatic rotation policy. A new key version is generated on a regular basis. If this situation occurs, KMS immediately executes the automatic rotation policy.

**Impacts of CMK status on automatic rotation**

A new key version can be created only for an enabled CMK. To enable a CMK, set the
**KeyState** parameter to Enabled. Take note of the following items:
If a CMK is in the Disabled or Pending Deletion state, do not call the UpdateRotationPolicy operation to update its automatic rotation policy. If a CMK enters the Disabled or Pending Deletion state after you enable automatic rotation for the CMK, KMS suspends the execution of automatic rotation. In this case, if you call the DescribeKey operation, the returned value of the **AutomaticRotation** parameter is Suspended. When the CMK enters the Enabled state again, its automatic rotation policy becomes active.

**Limits**

The following keys do not support multiple key versions: Service-managed keys: the default keys managed by KMS for specific cloud services. These keys belong to the users of cloud services and are used to provide basic encryption protection for user data. BYOK-based keys: the keys that you imported to KMS. For more information, see Import and delete key material. The **Origin** attribute of these keys is EXTERNAL. KMS does not generate key material or initiate rotation tasks for these keys. These two types of keys do not support version-based manual or automatic key rotation. A BYOK-based key does not have multiple versions in KMS. Users have strong control over the persistence and lifecycle of BYOK-based keys. This makes management of the keys difficult and error-prone. For example, you must have on-premises key management facilities, data must be synchronized between on-premises facilities and the cloud, and no grace period is provided for key material deletion on the cloud. The complexity of maintaining multiple versions of BYOK-based keys makes key management much more risky. In addition, both primary and non-primary key versions may become unavailable at different points in time. For example, if key versions are deleted by KMS or imported again when they expire, CMKs may not be synchronized and encrypted data may fail to be decrypted due to the use of an invalid CMK. This affects system integrity.

> **Note:** For information about alternative solutions in the cases where version-based key rotation is not supported, see Manual CMK rotation.

### 7.3 Manual CMK rotation

If your CMKs do not support version-based automatic rotation, you can manually rotate the CMKs based on your scenario. This is an alternative solution that can be used regardless of whether automatic CMK rotation is supported.

**Scenario of custom data encryption**

On-premises or cloud applications can call KMS API operations to implement custom data encryption. Examples: Encrypt sensitive data such as ID card numbers, credit card numbers, and home addresses before you write it to databases. Encrypt data on a client before you upload the data to Object Storage Service (OSS). Encrypt application configuration files that contain sensitive data and service configuration files such as SSL certificates and private keys. You can use the key alias feature of KMS to rotate encryption keys within applications. The ID and alias of CMKs are not required when you call the Decrypt operation. In this scenario, the rotation process consists of the following steps:
1. Initial configuration
i. The administrator creates a CMK, whose ID is CMK-A. ii. The administrator binds the alias/MyAppKey alias to CMK-A. iii. When the application encryption module calls the Encrypt operation, the application encryption module sets the value of the **KeyId** parameter to alias/MyAppKey. KMS finds that the alias/MyAppKey alias is bound to CMK-A and then uses CMK-A to encrypt data. iv. When the application decryption module calls the Decrypt operation, the application decryption module does not set the **KeyId** parameter. KMS uses the CMK that is used to encrypt the data to decrypt the data. i. The administrator creates a CMK, whose ID is CMK-B. ii. The administrator calls the UpdateAlias operation to bind the alias/MyAppKey alias to CMK-B. iii. When the application decryption module calls the Encrypt operation, the application decryption module sets the value of the **KeyId** parameter to alias/MyAppKey. KMS finds that the alias/MyAppKey alias is bound to CMK-B and uses CMK-B to encrypt data. iv. When the application decryption module calls the Decrypt operation, the application decryption module does not set the **KeyId** parameter. KMS uses the CMK that is used to encrypt the data to decrypt the data.

**Scenario of server-side encryption by cloud services**

Cloud services can implement server-side encryption by calling KMS API operations. In this scenario, the following situations may occur from the perspective of key rotation: Automatic rotation policies configured in KMS affect the server-side encryption of cloud services. Cause: After encryption based on the specified CMK is configured for cloud services, these services call the GenerateDataKey operation of KMS to generate new data keys. When KMS generates a new primary key version, cloud services use the new version to encrypt the newly generated data keys. A typical example of such cloud services is OSS. In this case, if you want to enable automatic key rotation, you must not use service-managed keys or BYOK-based keys imported to KMS because these keys do not support automatic rotation. Automatic rotation policies configured in KMS do not affect server-side encryption of cloud services. Cause: After encryption based on the specified CMK is configured for cloud services, the services call the GenerateDataKey operation of KMS only once to generate keys to encrypt specific resources. When KMS generates a new primary key version, cloud services do not use this version. For example, Elastic Compute Service (ECS) calls the GenerateDataKey operation of KMS once to generate a volume encryption key. This key is not updated after it is created. If automatic rotation policies configured in KMS do not affect server-side encryption of cloud services or you want to rotate data keys when BYOK-based keys are used, you can modify configurations and copy data to achieve the same effect as key rotation. These methods depend on the features of different cloud services. For more information, see the documents of related cloud services.

## 8 Security Audit

### 8.1 Overview

A security audit refers to the systemic and independent inspection and verification of activities and behavior in the computer network environment. Delegated by property owners and authorized by management authorities, professional auditors give their assessments according to relevant laws and regulations. When the administrator needs to backtrack system operations, the administrator can perform a security audit. Security audits are long-term security management activities throughout the lifecycle of cloud services. The security audit feature of Apsara Stack Security can collect system security data, analyze weaknesses in system operations, report audit events, and classify audit events into important, moderate, and low risk levels. The security administrator views and analyzes audit events to continuously improve the system and ensure the security and reliability of cloud services.

### 8.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You must obtain the username and password from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform corresponding
operations in the following scenarios: It is the first time that you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password that you entered in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

### 8.3 View the summary information about security audit

**information about security audit**

This topic describes how to view the summary information about security audit.

**Background information**

The **Overview** tab provides reports on the raw log trend, audit event trend, audit risk distribution, and security event distribution. The reports are displayed in run charts or pie charts to help security administrators analyze the trend of risks in your cloud services. On the **Overview** tab, security administrators can check the number of logs and the storage usage in a specific time range.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Overview** tab.
4. On the **Overview** tab, view the audit summary for the last seven days.
Trends of Raw Log This chart displays the trend of logs that are generated by **Platform Database**, **Server**,
**Network Device**, **ECS**, **Cloud Products**, or **Platform Database(new)** in the last seven
days. Security administrators can analyze the trend to check whether the number of logs is at a normal level. Audit Events This chart displays the trend of audit events that are generated by **Platform Database**,
**Server**, **Network Device**, **ECS**, **Cloud Products**, or **Platform Database(new)** in the
last seven days. Security administrators can analyze the trend to check whether the number of audit events is at a normal level. Security administrators can analyze the trend to check whether the number of audit events is at a normal level. Audit Risk Distribution This chart displays the percentage distribution of audit events at different risk levels in the last seven days. Risk levels are important, moderate, and low. Security administrators can analyze the trend to check whether the audit events are at acceptable risk levels. Security Issue Distribution This chart displays the percentage distribution of different event types in the last seven days. Security administrators can analyze this chart to check for the most frequent audit events and identify high-risk events to improve security protection. Log Size This chart displays the volume of online logs and offline logs. If the logs consume a large number of storage resources, we recommend that you back up the required audit logs and delete unnecessary logs. Audit Log Size This chart displays the size of logs for each audit type.
5. View the audit summary in a specific time range.
i. Specify **End Time** as the end of the time range to query. ii. In the **Audit Type** section, select the audit types that you want to query. iii. Click **View** to query the audit summary in the last seven days before the specified end time.

### 8.4 Query audit events

This topic describes how to query audit events.

**Background information**

On the **Audit Query** tab, you can view the details of audit events, including the log creation time, audit type, audit object, action type, risk level, and log content. The system matches the logs that are collected by a security audit module against audit rules. If the log content matches the regular expression in an audit rule, an audit event is reported.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the Security Audit page, click the **Audit Query** tab.
4. On the **Audit Query** tab, configure query conditions to view audit events within the
specified time range. Basic query a. Configure the following parameters: **Audit Type**, **Audit Target**, **Action Type**, **Action**,
**Risk Level**, and **Notify**.
b. Specify a time range to query. c. In the **Full-Text Search** search box, enter a keyword. d. Click **Query**. Advanced query In addition to the basic query conditions, you can configure advanced query conditions. a. Configure basic query conditions. b. Click **Advanced Search**. c. In the **Filter Condition** section, configure **Filter Name**, **User**, **Target**, **Action**,
**Result**, and **Cause**.
d. Click **Save**.
5. Click Export to export the audit events.
Download the exported file for analysis. For more information, see Download exported audit events or logs.

### 8.5 View raw logs

On the Raw Logs tab, you can view the raw logs that are generated by a running audit object. Raw logs contain information that is required for debugging. Security administrators can use these raw logs to troubleshoot system failures. This topic describes how to view raw audit logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Raw Logs** tab of the **Security Audit** page, configure query conditions to view the
log summary chart and raw logs within a specific time range. i. Specify **Audit Type** or **Audit Target**. ii. Specify a time range to query. iii. Enter a keyword. iv. Click **Search**. In the raw log list, you can view the **Source**, **Audit Target**, and **Log Content** of a log.
4. Click **Export** to export the audit events.
Download the exported file for analysis. For more information, see Download exported audit events or logs.

### 8.6 View the number of logs

This topic describes how to view and manage log sources.

**Background information**

You can view the number of logs and specify whether to show logs by log type or log source. The Log Types tab provides the number of all logs for a specific audit object of a specific device instance. The Log Sources tab provides the number of logs for all audit objects of a specific device instance.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Log Sources** tab, click the **Log Types** tab to view the number of logs by audit
object. You can view the number of logs that are recorded on the current day and the number of logs that are recorded during the last 30 days for each audit object. If you do not want to display the logs for an audit object, perform the following steps: i. Find the audit object and click **Hide** in the **Actions** column. ii. In the Note message, click **Confirm**.

> **Note:** The process that is used to display the logs for an audit object is similar to the process that is used to hide the logs.

4. Click the Log Sources tab and view the number of logs for each device instance.
You can view the number of logs that are recorded on the current day and the number of logs that are recorded during the last 30 days for each device instance. If you do not want to display the logs for an audit object from a specific device instance, perform the following steps: i. Find the device instance and click **Hide** in the **Actions** column. ii. In the message that appears, click **OK**.

> **Note:** The process that is used to display the logs for an audit object is similar to the process that is used to hide the logs.

### 8.7 Policy settings

#### 8.7.1 Manage audit rules

This topic describes how to create, modify, or delete an audit rule.

**Background information**

If a log matches an audit rule, an audit event is reported. You can specify regular expressions in an audit rule to match logs. A regular expression defines a matching pattern for character strings and can be used to check whether a string contains a specific substring. The following table provides examples about the pattern.

| Regular expression | Description |
|---|---|
| ^\d{5,12}$ | Matches the consecutive numbers from the fifth number to the twelfth number. |
| load file\( _ | Matches the "load file(" string. _ |

The security audit module defines the default audit rule based on the string that is generated in the log. This applies when an audit event is reported. A security administrator can also customize audit rules based on the string that is generated in the log. This applies when the system encounters an attack.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Audit Rules** tab.
5. Create an audit rule.
i. Click **New**. ii. In the **Add Policy** dialog box, configure the parameters. iii. Click **Add**. The system sends an alert email to the specified alert recipient after you create an audit rule. This applies if one string in an audit log of the specified audit type, audit object, or risk level matches the regular expression of the audit rule.
6. Manage audit rules.
You can create, query, disable, enable, and delete audit rules. Query audit rules Specify **Audit Type** and **Audit Target**. Enter a keyword in the search box and click
**Search**.
Disable an audit rule Find the audit rule that you want to disable and click **Disable** in the **Actions** column. Enable an audit rule Find the audit rule that has been disabled and click **Enable** in the **Actions** column. Delete an audit rule Find the audit rule that you want to delete and click **Delete** in the **Actions** column.

> **Note:** You can delete only custom rules.

#### 8.7.2 Configure alert recipients

This topic describes how to configure the recipients of alerts on audit events.

**Background information**

After you specify an alert recipient, the system sends a report to the email address of the alert recipient when an audit event occurs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Alert Settings** tab.
5. Create an alert recipient.
i. Click **New**. ii. In the **Add Alert Recipient** dialog box, configure the following parameters. iii. Click **OK**.
6. Manage alert recipients.
Search for an alert recipient Specify **Audit Type**, **Audit Target**, and **Risk Level**, enter the keyword of the email address, and then click **Search**. Delete an alert recipient Find the email address that you want to delete and click **Delete** in the Actions column.

#### 8.7.3 Query the archives of audit events and raw logs

**raw logs**

This topic describes how to query and download the archives of audit events and raw logs.

**Background information**

You can download the archives of events and logs to analyze audit events. This ensures the security of the Apsara Stack environment.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **Archiving** tab.
5. Query the archives of events and logs.
i. Configure **Audit Type** and **Archiving Type**. ii. Specify a time range to query. iii. Click **Search**. Find the file where the archive information is stored and click **Download** in the **Actions** column to save the archive file to your computer.

#### 8.7.4 Download exported audit events or logs

**logs**

This topic describes how to download exported audit events or logs.

**Background information**

You can export audit events or logs on the **Audit Query** or **Raw Log** tab of the Security Audit page. After you export audit events or logs, you can manage the export tasks on the Exporting tab.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click **Exporting**.
5. View the created export tasks.
6. Click **Download** to download audit events or logs to your on-premises server.
To delete an export task, click **Delete**.

#### 8.7.5 Modify system settings

This topic describes how to configure system parameters for security audit.

**Background information**

You can configure system parameters to specify the maximum number of system alerts per day and the maximum number of audits per day for raw logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security Management** and choose **Security Audit >**
**Apsara Stack Security - Security Audit** .
3. On the **Security Audit** page, click the **Policy Settings** tab.
4. On the **Policy Settings** tab, click the **System Settings** tab.
5. Find the system parameter that you want to modify and click **Edit** in the **Actions** column.
6. Enter a required value and click **OK**.
