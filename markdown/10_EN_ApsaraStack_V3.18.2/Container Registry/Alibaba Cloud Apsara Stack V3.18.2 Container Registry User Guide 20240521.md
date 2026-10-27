---
title: "Alibaba Cloud Apsara Stack V3.18.2 Container Registry User Guide 20240521"
product_version: "V3.18.2"
doc_version: "20240521"
pdf_pages: 51
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Container Registry User Guide 20240521.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8FACR/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Container%20Registry%20User%20Guide%2020240521.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.2 Container Registry User Guide 20240521

## Table of Contents

- 1 What is Container Registry?
- 2 Getting Started
  - 2.1 Use Container Registry
  - 2.2 Log on to the Container Registry console
- 3 Container Registry Standard Edition
  - 3.1 Permission management
    - 3.1.1 Create a user and a user group
    - 3.1.2 Create a role and grant permissions to the role
    - 3.1.3 Repository access control
  - 3.2 Create a namespace
  - 3.3 Creates an image repository
  - 3.4 Configure an access credential
  - 3.5 Upload and download images
  - 3.6 Replicate an image
  - 3.7 Configure a trigger
  - 3.8 Sign container images
- 4 Container Registry Advanced Edition
  - 4.1 Permission management
    - 4.1.1 Create a user and a user group
    - 4.1.2 Create a role and grant permissions to the role
    - 4.1.3 Repository access control
  - 4.2 Create a namespace
  - 4.3 Create an image repository
  - 4.4 Configure an access credential
  - 4.5 Upload and download images
  - 4.6 Configure a trigger
  - 4.7 Push and pull Helm charts
    - 4.7.1 Use Helm 2 to push and pull charts
    - 4.7.2 Use Helm 3 to push and pull charts
  - 4.8 Replicate images between instances that belong to the same account
  - 4.9 Replicate images between instances that belong to different accounts
  - 4.10 Configure a repository to be immutable
  - 4.11 Delete image tags
  - 4.12 Use the aliyun-acr-credential-helper component to pull images without a secret

gistry?

## 1 What is Container Registry?

Container Registry is a platform that allows you to manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: image permission management, synchronous image distribution, and content signing. The features allow you to manage the entire lifecycle of container images. Container Registry simplifies the setup and O&M of container registries. Container Registry is integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to help enterprises reduce delivery complexity and create a one-stop solution for cloud-native applications.

**Classification of Container Registry Enterprise Edition**

Container Registry Standard Edition is suitable for small and medium-sized enterprises. It supports secure hosting and efficient distribution of container images. You can use multiple Alibaba Cloud accounts in the Container Registry Standard Edition, create 15 namespaces for each account, and maintain 1,000 public repositories or private repositories in each namespace. Container Registry Standard Edition allows 100 nodes to concurrently pull a container image. Container Registry Advanced Edition is suitable for medium and large-sized enterprises. It provides secure hosting and lifecycle management of OCI artifacts, such as container images, Helm charts, and operators. Container Registry Advanced Edition also supports efficient artifact distribution scenarios, such as multi-region replication and cross-cloud replication. You can create up to 1,000 namespaces and maintain 100,000 repositories on a Container Registry Advanced Edition instance. Container Registry Advanced Edition allows 500 nodes to concurrently pull a container image.

**Features**

| Module | Feature |   | Description | Standard Edition | Advanced Edition |
|---|---|---|---|---|---|
| Artifact management | Container images | Secure hosting | Container images can be securely hosted by namespace. | Supported | Supported |
|   |   | Lifecycle management | You can query container image tags and delete image repositories. | Supported | Supported |
|   |   | Fine-grained permission management | You can manage the permissions on resource sets and departments in the Apsara Uni-manager Management Console. You can manage user permissions. | Supported | Supported |
|   |   | Immutable tags | You can configure image tags of repositories to be immutable. | Not supported | Supported |
|   | OCI artifacts, such as Helm charts and | Secure hosting | OCI artifacts can be securely hosted by namespace. | Not supported | Supported |
|   |   | Lifecycle management | You can query artifact tags and delete artifact repositories. | Not supported | Supported |

|   | charts and operators |   |   |   |   |
|---|---|---|---|---|---|
|   |   | Fine-grained permission management | You can manage the permissions on resource sets and departments in the Apsara Uni-manager Management Console. You can manage user permissions. | Not supported | Supported |
|   |   | Immutable tags | You can configure OCI artifact tags of repositories to be immutable. | Not supported | Supported |
|   | Triggers |   | If a container image is updated, the corresponding event is automatically triggered. | Supported | Supported |
| Efficient image distribution | Manual image replication |   | You can manually trigger the replication of a container image of a specific tag to implement geo-disaster recovery for container images. | Supported | Supported |
|   | Automatic image replication |   | After images are pushed, the images are automatically replicated based on replication rules. | Not supported | Supported |
|   | Cross-account replication |   | Images can be replicated across Alibaba Cloud accounts. | Not supported | Supported |
| Artifact security | Encrypted image distribution |   | You can configure secure HTTPS protocol to distribute container images. | Supported | Supported |
|   | Image signing |   | This feature prevents man-in- the-middle (MITM) attacks and unauthorized image updates or deployments. This ensures image consistency and security from distribution to deployment. | Supported | Supported |
|   | Image scanning (provided after Container Registry is integrated with Apsara Stack Security Center) |   | You can scan container images to identify vulnerabilities. | Not supported | Supported |
| Deployment integration | Image pulls without using a secret |   | You can configure image pulls without a secret in the ACK console. This way, you do not need to specify a secret for each image pull. | Supported | Supported |
|   | Deployment selection |   | You can select image repositories and image tags when you configure a Deployment in the ACK console. | Supported | Supported |

## 2 Getting Started

### 2.1 Use Container Registry

This topic describes how to use Container Registry.

**Standard Edition**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. Create a namespace. For more information, see Create a namespace.
3. Create an image repository. For more information, see Creates an image repository.
4. Upload and download images. For more information, see Upload and download images.

**Advanced Edition**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. Create a namespace. For more information, see Create a namespace.
3. Create an image repository. For more information, see Create an image repository.
4. Upload and download images. For more information, see Upload and download images.

### 2.2 Log on to the Container Registry console

**console**

This topic describes how to log on to the Container Registry console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. The password must be 8 to 20 characters in length and contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations
in the following scenarios: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **"Manage MFA"** section in **Apsara Uni-manager Management** **Console User Guide**.

5. In the top navigation bar, choose **Products > Elastic Computing > Container Registry**.
6. On the **Instances** page, select an instance to perform image-related operations.
Click the card of a Container Registry Advanced Edition instance. On the management page of the instance, you can perform operations on the instance. For example, you can create a namespace and upload and download images on the instance. Click the card of a Container Registry Standard Edition instance. On the management page of the instance, you can perform operations on the instance. For example, you can create a namespace and upload and download images on the instance.

## 3 Container Registry Standard Edition

**Edition**

### 3.1 Permission management

#### 3.1.1 Create a user and a user group

You can create users and assign different roles to the users to meet different requirements for system access control as an administrator. This topic describes how to create a user and a user group.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. A browser is available. We recommend that you use Google Chrome.

**Create an organization**

To create a user or a user group, you must create an organization in advance.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your browser and
press Enter.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. In the top navigation bar, click **Enterprise**.
5. In the left-side navigation pane of the Enterprise page, choose Resources > **Organizations**.
6. In the left-side organization navigation tree, click the name of a parent organization under which you
want to create an organization. Click **Create Organization** in the upper-right corner of the page.
7. In the Add Organization dialog box, enter a name for the organization and click **OK**.
8. **Optional:** If the multi-cloud management feature is enabled for the primary node, the
**Synchronously Create Multi-cloud Organization** check box is displayed after you click **OK**.
Select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

**Create a user group**

A role cannot be directly assigned to a user. You can assign a role to a user group. Then, users in the user group can obtain the permissions of the role. Relationships between user groups and users: A user group can contain zero or more users. A user does not necessarily belong to a user group. A user can be added to multiple user groups. Relationships between user groups and organizations: A user group belongs to only one organization. You can create multiple user groups within an organization. Relationships between user groups and roles: A role can be assigned to multiple user groups. When a role is assigned to a user group, the permissions that the role has are automatically granted to the users within the user group. Relationships between user groups and resource sets: A resource set can be added to zero or more user groups. A user group can be added to multiple resource sets.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users > User Groups**.
3. Click **Create a user group** in the upper-left corner of the page.
4. In the dialog box that appears, configure **User Group Name**, **Organization**, and **Role**
**authorization**.

| Parameter | Description |
|---|---|
| User Group Name | The name of the user group. The name must be 3 to 255 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), and at signs (@). _ |
| Organization | The organization to which the user group belongs. |
| Role authorization | The roles that are assigned to the user group. |

5. Click **OK**.

**Create a user**

You can create users based on your business requirements.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users > Users**.
3. Click the **System Users** tab. Click **Create a user**.
4. In the dialog box that appears, configure parameters.

| Parameter | Required | Description |
|---|---|---|
| User name | Yes | The Apsara Stack tenant account name of the user. The name must be 1 to 64 characters in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Display name | Yes | The display name of the user. The name must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). _ |
| Role | Yes | The role to be assigned to the user. Note You can enter role names in the field. Fuzzy match is supported. |
| Organization | Yes | The organization to which the user belongs. |

| Logon policy | Yes | The logon policy that specifies the logon time of the user and the IP address that the user logs on to. If you do not configure this parameter, the default policy is attached to the created user. Note The default policy does not specify the logon time of the user and the IP address that the user logs on to. To specify the logon time and IP address, you can modify the logon policy or create a logon policy. |
|---|---|---|
| Phone | Yes | The mobile phone number of the user. If you want to send text messages about the resource requests and usage to the mobile phone number, make sure that the specified mobile phone number is valid. Note If the mobile phone number of the user changes, update it on the system in a timely manner. |
| Landline | No | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | Yes | The email address of the user. If you want to send emails about the resource requests and usage to the email address, make sure that the specified email address is valid. Note If the email address changes, update it on the system in a timely manner. |
| DingTalk Key | No | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |
| Notify User by Email | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
| Notify User by DingTalk | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

5. Click **Modify**.

#### 3.1.2 Create a role and grant permissions to the role

**role**

You can create custom roles, attach permission policies to the roles, and assign the roles to a user to grant permissions to the user. This topic describes how to create a role, assign the role to a user group, and attach a policy to the role.

**Background information**

A role is a set of access permissions. Each role has a range of permissions. A user can have multiple roles, which means that the user is granted all the permissions defined for the roles. A role can be used to grant the same set of permissions to a group of users. The total number of custom and default roles cannot exceed 20.

**Create a role**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your browser and
press Enter.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters: ! @ # $ %

3. Click **Log On**.
4. In the top navigation bar, click **Enterprise**.
5. In the left-side navigation pane, choose **Permissions > Role Permissions**.
6. In the upper-left corner of the **Role authorization** page, click **Create Custom Role**.
7. On the **Create Custom Role** page, click **Advanced Settings**.
8. In the **Advanced Settings** section, click **Create RAM Role & Attach Policy** .
9. In the Basic Configurations step of the **Create RAM Role & Attach Policy** wizard, configure
parameters. i. Enter a **Role name** and **Description**, and set the **Sharing Scope**. The description is optional. By default, **Global** is selected for **Sharing Scope**, which indicates that the role is visible to and can be assumed by all organizations. Click **Next**. ii. In the Configure Custom Policy step, select an existing policy or create a new policy, and then click
**Next**.

> **Note:** You can select a maximum of five policies for a RAM role.

For information about how to create a policy, see Attach a custom policy to the role. iii. In the Configure Trust Policy step, select values from the **Trust Organization** and **Trust Cloud**
**Service** drop-down lists separately. Click **Next**.

> **Note:** You can select multiple trust organizations and trust cloud services at a time for a RAM role.

iv. In the Preview Policy step, check the content of the selected policies and trust policies, and click
**Create**.
0. **Optional:** Add authorized users to the RAM role.
When you create a RAM role, you can add authorized users to the role. After you add authorized users to the RAM role, the authorized users are granted the permissions of the role. i. In the left-side navigation pane of the Enterprise page, choose Permissions > **Role Permissions**. On the Role authorization page, click the name of the role of which permissions you want to grant to users. ii. On the details page of the role, click the **Authorized Personnel** tab. iii. On the **Authorized Personnel** tab, click **Authorized** in the **Authorize Users** section. iv. In the **Authorized User** dialog box, select the users to which you want to grant the permissions of the role and click **Confirm authorization**. To add authorized users to the RAM role, you must create users in advance. For more information, see Create a user and a user group.

**Attach a custom policy to the role**

When you create a RAM role, in the Configure Custom Policy step you can click **Create Policy** in the upper-right corner of the page to create a policy. In the **Create Policy** dialog box, configure the following parameters and then click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Specify a name for the custom policy. The name can be up to 15 characters in length. Example: MangeNameSpace . |
| Sharing Scope | Select the sharing scope of the role based on your business requirements. Valid values: Global: The role is visible to and can be assumed by all organizations. This is the default option. Current Organization: The role is visible to and can be assumed by the organization to which the user belongs. Subordinate Organization: The role is visible to and can be assumed by the organization to which the user belongs and the subsidiaries of the organization. Note If you use the admin account to log on to the Apsara Uni-manager Management Console, the sharing scope is automatically set to Global and cannot be changed. If you use another account to log on to the Apsara Uni-manager Management Console, the preceding three options are displayed for the Sharing Scope parameter. |
| Description | Enter the description of the policy, such as the capabilities of the policy. |

| Policy Content | The following code provides a sample policy. { "Version": "1", "Statement": [ { "Action": [ "edas:CreateNamespace" ], "Resource": [ "acs:edas:*:*:namespace/*" ], "Effect": "Allow" }, { "Action": [ "edas:ManageNamespace" ], "Resource": [ "acs:edas:*:*:namespace/$namespace" ], "Effect": "Allow" }, { "Action": [ "edas:ReadNamespace", "edas:DeleteNamespace" ], "Resource": [ "acs:edas:*:*:namespace/$namespace" ], "Effect": "Allow" } ] } This policy allows the actions of creating, editing, and deleting a namespace. |
|---|---|

#### 3.1.3 Repository access control

Users can obtain access to a repository if you grant them permissions. This topic describes how to configure access control for repositories in different scenarios.

**Precautions**

When you grant permissions to a user, pay attention to the following instructions to make sure that you do not grant excessive permissions to the user. You can grant a user the AdministratorAccess permission that contains management permissions on all Alibaba Cloud resources. In this case, the user has all permissions on Container Registry, regardless of whether the user is granted permissions before.

**System policy configuration**

AliyunContainerRegistryFullAccess This policy grants a user the same permissions on image resources as those of an Alibaba Cloud account. The user can perform all operations on image resources. `{`

```json
  "Statement": [
```

`{`

```json
      "Action": "cr:*",
      "Effect": "Allow",
      "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}` AliyunContainerRegistryReadOnlyAccess This policy grants a user the read-only permission on all image resources. For example, the user can view the repository list and pull images. `{`

```json
  "Statement": [
```

`{`

```json
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:PullRepository"
```

`],`

```json
      "Effect": "Allow",
      "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}`

**Policy configuration for typical scenarios**

Scenario 1 Scenario: Grant a user the read-only permission on a namespace that is named juzhong. After the user logs on to the Container Registry instance, the user can pull all images in the namespace juzhong. The user can view information about the namespace and all repositories in the namespace by calling API operations. `{`

```json
  "Statement": [
```

`{`

```json
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:PullRepository"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/juzhong/*"
```

`]` `}` `],`

```json
  "Version": "1"
```

`}`

> **Important:** If you want to allow the user to view all the namespaces in the console, add the following authorization configurations. Then, the user can view all the namespaces and repositories. However, the user can pull only images from the repositories in the namespace juzhong.

`{`

```json
  "Statement": [
```

`{`

```json
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:PullRepository"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/juzhong/*"
```

`]` `},` `{`

```json
      "Action": [
        "cr:ListNamespace",
        "cr:ListRepository"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "*"
```

`]` `}` `],`

```json
  "Version": "1"
```

`}` Scenario 2 Scenario: Grant a user all permissions on a repository, such as the repository nginx in the namespace juzhong in the China (Hangzhou) region.

> **Important:** If you want to allow the user to manage repositories in the console, add the relevant configurations by referring to scenario 1.

`{`

```json
  "Statement": [
```

`{`

```json
      "Action": [
        "cr:*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:cn-hangzhou:*:repository/juzhong/nginx"
```

`]` `},` `{`

```json
      "Action": [
        "cr:Get*",
        "cr:List*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/juzhong"
```

`]` `}` `],`

```json
  "Version": "1"
```

`}` Scenario 3 Scenario: Grant a user all permissions on a namespace.

> **Important:** You can implement the scenario only by calling API operations. If you want to allow the user to view all repositories in the console, add the relevant configurations by referring to scenario 1.

`{`

```json
    "Statement": [
```

`{`

```json
            "Action": [
                "cr:*"
```

`],`

```json
            "Effect": "Allow",
            "Resource": [
                "acs:cr:cn-hangzhou:*:repository/juzhong",
                "acs:cr:cn-hangzhou:*:repository/juzhong/*"
```

`]` `}` `],`

```json
    "Version": "1"
```

`}`

**Authentication rules of Container Registry**

ARN format The following table describes the Alibaba Cloud Resource Name (ARN) format in an authorization policy when you grant a user access to the resources.

| Resource type | ARN format in an authorization policy |
|---|---|
| repository | acs:cr:$regionid:$accountid:repository/$namespacena me/$repositoryname |

The following table describes the parameters in the ARN format.

| Parameter | Description |
|---|---|
| $regionid | The region ID, which can be replaced by an asterisk (*). |
| $accountid | The ID of the Alibaba Cloud account, which can be replaced by an asterisk (*). |
| $namespacename | The name of the namespace. |
| $repositoryname | The name of the repository. |

Authorization rules When you access the Container Registry API as a user or by using Security Token Service (STS), Container Registry checks whether you have obtained the required permissions. The permissions that Container Registry checks vary based on the resources that are requested by the API operation and the syntax of the API operation. The following table describes the authentication rules for different API operations.

| API | Action | Resource |
|---|---|---|
| Creates a namespace. | cr:CreateNamespace | * |
| Deletes a namespace. | cr:DeleteNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Updates a namespace. | cr:UpdateNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Queries a namespace. | cr:GetNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Queries namespaces. | cr:ListNamespace | * |
| Creates a repository. | cr:CreateRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Deletes a repository. | cr:DeleteRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Updates a repository. | cr:UpdateRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries a repository. | cr:GetRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries repositories. | cr:ListRepository | * |
| Queries repositories in a namespace. | cr:ListRepository | * |
| Queries the tag information about a repository. | cr:ListRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Deletes an image tag. | cr:DeleteRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries the manifest information about an image. | cr:GetRepositoryManifest | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |

| Queries the information about image layers. | cr:GetRepositoryLayers | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
|---|---|---|
| Queries a temporary authorization token. | cr:GetAuthorizationToken | * |
| Pulls images. | cr:PullRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Pushes images | cr:PushRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |

### 3.2 Create a namespace

This topic describes how to create a namespace in the Container Registry console.

**Background information**

A namespace is a collection of repositories. We recommend that you place the repositories of a company or an organization in the same namespace. Sample namespaces that are named after a company: aliyun and alibaba Sample namespace that is named after a team or an organization: team

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Standard Edition Instance.
3. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Namespace**.
4. On the **Namespace** page, click **Create Namespace**.
5. On the **Create Namespace** page, configure **Organization**, **Resource Set**, **Region**, and Namespace
Name, and then click **Submit**.

**What to do next**

You can create image repositories in the namespace.

### 3.3 Creates an image repository

This topic describes how to create an image repository in the Container Registry console.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Standard Edition Instance.
3. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Repository**.
4. On the **Repository** page, click **Create Repository**.
5. On the **Create Repository** page, configure parameters and then click **Submit**.

| Parameter | Description |
|---|---|
| Organization | The organization to which the repository belongs. |
| Resource Set | The resource set to which the repository belongs. |
| Region | The region in which the repository resides. |

| Namespace | The namespace to which the repository belongs. |
|---|---|
| Repository Name | The name of the repository. The name must be 1 to 64 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). The name _ cannot start with a hyphen (-) or an underscore ( ). _ |
| Digest | The digest of the repository. |
| Description | The description of the repository. The description can be up to 2,000 characters in length. |
| Repository Type | Public repositories and private repositories are supported. |

**What to do next**

After the repository is created, you can click **Manage** in the **Actions** column of the repository to go to the **Details** page and learn how to manage the repository.

### 3.4 Configure an access credential

Access credentials ensure the secure upload and download of container images. This topic describes how to configure an access credential.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Standard Edition Instance.
3. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Access Credential**.
4. On the **Access Credential** page, click **Set Password**.
5. In the **Set Password** dialog box, enter the password and confirm the password. Then, click **Confirm**.
6. **Optional:**For information about how to set a temporary token, see **GetAuthorizationToken** of **API**
**Operations for Standard Edition** in the **Container Registry Developer Guide**.

**Other operations**

You can use the password or temporary token that you set to log on to the Container Registry instance.
1. On the Access Credential page, check the logon command.
2. Run the logon command and enter the logon password as prompted in the command output.

### 3.5 Upload and download images

This topic describes how to upload and download images.

**Procedure**

1. Obtain the username.
i. Log on to the Container Registry console. For more information, see Log on to the Container Registry console. ii. On the **Instances** page, click the card of a Standard Edition Instance. iii. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Access Credential**.
On the **Access Credential** page, view and record the username and the domain name of the repository.
2. Run the following command to log on to the image repository:

```python
sudo docker login --username=<Username> <Domain name of the repository>
```

As prompted in the command output, enter the password that you set when you activated Container Registry. If you forget your password, you can reset it. For more information, see Configure an access credential.
3. Upload and download an image.
Upload an image a. Run the following command to add a tag to the image:

```python
sudo docker tag <ID of the image> <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

b. Run the following command to upload the image:

```python
sudo docker push <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

Download an image Run the following command to download an image:

```python
sudo docker pull <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

4. **Optional:** Modify the name of an image.
i. Run the following command to query the ID of the image:

```python
sudo docker images
```

ii. Run the following command to modify the name of the image:

```python
sudo docker tag <ID of the image> registryDomain/<Name of the namespace>/<Name of the repository>:<Image version number>
```

### 3.6 Replicate an image

Container Registry allows you to replicate images across data centers. This way, you can obtain the expected image from the nearest data center when you deploy workloads.

**Prerequisites**

A namespace is created. For more information, see Create a namespace. An image repository is created in the namespace. For more information, see Creates an image repository.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Standard Edition Instance.
3. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Repository**.
4. On the **Repository** page, find the repository that you want to manage and click **Manage** in the
Actions column.
5. In the left-side navigation pane of the details page of the repository, click **Image Replication**.
6. On the Image Replication page, click **Create Replication Task**.
7. In the **Select Destination Repository** dialog box, configure parameters and then click **OK**.

| Parameter | Description |
|---|---|
| Version to be Replicated | Select the version of the repository to be replicated. |
| Destination Repository | Select the region, namespace, and name of the destination repository and enter the version of the destination repository. |

**Result**

On the **Image Replication** page, you can view the status of the replication task. You can click **Details** in the Actions column of the task to check the replication status of image layers.

### 3.7 Configure a trigger

Container Registry provides the trigger feature for image repositories. If you create a trigger for an image repository, a notification is pushed to you when an image is built. This facilitates the redeployment of images for applications. If you create a trigger for a container service, the applications on the container service automatically pull and redeploy the new images that are built on the container service. This topic describes how to configure a trigger.

**Security rules on trigger usage**

HTTP: Port 80 is used by default. If you want to use another port, append the port number to the end of the trigger URL. You can use only the following port numbers: 80, 21, 443, 70, 210, 280, 488, 591, 777, and from 1025 to 65535. HTTPS: Port 443 is used by default. Only port 443 is supported. If you want to use another port, use HTTP.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Standard Edition Instance.
3. In the left-side navigation pane of the management page of the Standard Edition instance, click
**Repository**.
4. On the **Repository** page, find the repository that you want to manage and click **Manage** in the
**Actions** column.
5. In the left-side navigation pane of the details page of the repository, click **Trigger**.
6. On the **Trigger** page, click **Create**.
7. In the **Create Trigger** dialog box, configure parameters and click **Confirm**.

| Parameter | Description |
|---|---|
| Name | The name of the trigger. |
| Trigger URL | Enter the URL of the trigger that is created in Container Service for Kubernetes (ACK). |
| Trigger | You can select Every time, Expression trigger, or Tag triggers. Every time: Each time an image is built, an image pull is triggered. Expression trigger: Tags are filtered based on a regular expression. An image pull is triggered only when a tag matches the regular expression. You can enter a simple regular expression, such as release-v.* . An image pull is triggered only after an image with a tag that starts with release-v is built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. Tag triggers: An image pull is triggered based on the specified tags. You can specify a maximum of 10 tags based on which an image pull needs to be triggered. Then, an image pull is triggered only when images with the specified tags are built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. |

### 3.8 Sign container images

When you manage container images, you can use content trust to verify both the integrity and the publisher of images. Image publishers can encrypt images by using digital signatures that are stored in Container Registry.

**Install and configure signature tools**

1. Install Alibaba Cloud Command Line Interface (CLI). For more information, see Install Alibaba Cloud
CLIInstall Alibaba Cloud CLI.
2. Run the following command to configure Alibaba Cloud CLI:

```
./aliyun configure set \ --profile akProfile \ --mode AK \ --region cn-qingdao-env17-d01 \ -access-key-id yourAK \ --access-key-secret yourAK
```

3. After you install and configure the GPG tool, run the following command to export the public key:

```bash
# Query pubKeyIdgpg --fingerprint# Export public key gpg --armor --output public-key.txt --
export yourUser.
```

> **Note:** For Apsara Stack instances, instanceId is set to default.

**Sign images**

1. Run the following command to obtain the image tag URL:

```
echo image://region/instanceId/namespace/repo@digest | tee imageURL.txt#e.g.#echo image://cn-qi ngdao-env17-d01/default/kritistest/busybox2@sha256:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bfff3dca > imageURL.txt
```

2. Run the following command to use GPG to sign the unique URL of the image. By default,
imageURL.txt.asc is generated.

```
gpg --armor --sign imageURL.txt
```

The imageURL.txt.asc file includes the following content:

```
-----BEGIN PGP MESSAGE----owGbwMvMwMEo63vGqaX74wXGNXVJ3CmpaYmlOSV6JRUlcZy7vmfmJqanWunr****.......=O2TP-----END PGP MESSAGE -----
```

3. Run the following command to create a metadata namespace:

```
./aliyun cr CreateMetadataNamespace --force --version 2018-12-01 --endpoint cr.inter.env17e.shuguang.com --NamespaceName kritis-test-2 --Description "for test"
```

4. Run the following command to create a signature note:

```
cat <<EOF > note.json| jq{ "name": "/namespaces/kritis-test-2/notes/image-sign", "LongDescriptio n": "long", "ShortDescription": "short", "ExpirationTime": "2021-01-01T00:00:00Z", "Kind": "ATTE STATION", "Attestation": { "Hint": { "HumanReadableName": "ACR" } }}EOF
```

5. Run the following command to create an occurrence for the image signature and save the occurrence
to the metadata service:

```json
cat <<EOF > occurrence.json | jq{ "Name": "/namespaces/kritis-test-2/occurrences/randomId1", "NoteName": "/namespaces/kritis-test-2/notes/image-sign", "ResourceUri": "image://cn-qingdao-env 17-d01/default/kritistest/busybox2@sha256:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bff****", "Kind": "ATTESTATION", "Attestation": { "Signatures": [ { "Signature": $(cat imageURL.txt.asc|jq -R --sl urp), "PublicKeyId": "E5B5FF2AFC3A1D70FE3CE57C1D4DCC42848****" } ] }}EOF ./aliyun cr CreateMetadataOccurrence --force --version 2018-12-01 --endpoint cr.inter.env17e.shuguang.com --NamespaceName kritis-test-2 --OccurrenceName randomId1 --Occurren ce "$(cat occurrence.json)"
```

6. Run the following command to query the image signature:

```bash
# Obtain a list of occurrences for a specified note: ./aliyun cr ListMetadataOccurrences --
force --version 2018-12-01 --endpoint cr.inter.env17e.shuguang.com --NamespaceName kritis-test-2 --NoteName image-sign --PageNo 1 --PageSize 5# Obtain a list of occurrences for a specified note that occurs on a resource: ./aliyun cr ListMetadataOccurrences --force --version 2018-12- 01 --endpoint cr.inter.env17e.shuguang.com --NamespaceName kritis-test-2 --NoteName image-sign - -PageNo 1 --PageSize 5 --ResourceURIs '["image://cn-qingdao-env17-d01/default/kritis-test/busybo x2@sha256:2f122941b5850006dbb7adda78d2ea5b382841ca6569fd174bd24c14bfff****"]'
```

**Appendix 1: Use GPG commands to generate publicKeyData**

1. Run the following command to find the local GPG key user that you want to use:

> **Note:** The user in the following example is `abcdef@example.com` .

```
gpg --list-keyspub rsa2048 2020-01-08 [SC] [Valid until: 2022-01-07] 7726310BC6E11E9B57B9CC08E2932E4363F3***uid [absolute] abcdef <abcdef@example.com>sub rsa2048 202 0-01-08 [E] [Valid until: 2022-01-07]
```

2. Export the public key of this user and encode the content of the public key in the Base64 format to
generate publicKeyData.

```bash
$ gpg --armor --export <user> |base64 | tr -d '\n'# For example, the user in the preceding example is abcdef@example.com, so the command is: gpg --armor --export abcdef@example.com
|base64 | tr -d '\n'# export publicKeyData=$(gpg --armor --export abcdef@example.com |base64 | t
r -d '\n')
```

**Appendix 2: Obtain an image digest value**

You can use the following method to find an image digest value. In this example, the image URL is registry.acs.example.com/kritis-test/alpine:3.11.

```bash
$ docker pull registry.acs.example.com/kritis-test/alpine:3.11$ docker images --digests | grep registry.acs.example.com/kritis-test/alpineregistry.acs.example.com/kritis-test/alpine 3.11 sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45 e7d92cdc71fe 2 months ago 5.59MB
```

The output shows that the image digest value is
**sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45**. When you
create resources, the following image ID must be used: **registry.acs.example.com/kritis-**
**test/alpine:sha256:ddba4d27a7ffc3f86dd6c2f92041af252a1f23a8e742c90e6e1297bfa1bc0c45**.

## 4 Container Registry Advanced Edition

**Edition**

### 4.1 Permission management

#### 4.1.1 Create a user and a user group

You can create users and assign different roles to the users to meet different requirements for system access control as an administrator. This topic describes how to create a user and a user group.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Create an organization**

To create a user or a user group, you must create an organization in advance.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. In the top navigation bar, click **Enterprise**.
5. In the left-side navigation pane of the Enterprise page, choose Resources > **Organizations**.
6. In the left-side organization navigation tree, click the name of a parent organization under which you
want to create an organization. Click **Create Organization** in the upper-right corner of the page.
7. In the Add Organization dialog box, enter a name for the organization and click **OK**.
8. **Optional:** If the multi-cloud management feature is enabled for the primary node, the
**Synchronously Create Multi-cloud Organization** check box is displayed after you click **OK**.
Select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

**Create a user group**

A role cannot be directly assigned to a user. You can assign a role to a user group. Then, users in the user group can obtain the permissions of the role. Relationships between user groups and users: A user group can contain zero or more users. A user does not necessarily belong to a user group. A user can be added to multiple user groups. Relationships between user groups and organizations: A user group belongs to only one organization. You can create multiple user groups within an organization. Relationships between user groups and roles: A role can be assigned to multiple user groups. When a role is assigned to a user group, the permissions that the role has are automatically granted to the users within the user group. Relationships between user groups and resource sets: A resource set can be added to zero or more user groups. A user group can be added to multiple resource sets.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users > User Groups**.
3. Click **Create a user group** in the upper-left corner of the page.
4. In the dialog box that appears, configure **User Group Name**, **Organization**, and **Role**
**authorization**.

| Parameter | Description |
|---|---|
| User Group Name | The name of the user group. The name must be 3 to 255 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), and at signs (@). _ |
| Organization | The organization to which the user group belongs. |
| Role authorization | The roles that are assigned to the user group. |

5. Click **OK**.

**Create a user**

You can create users based on your business requirements.
1. In the top navigation bar, click **Enterprise**.
2. In the left-side navigation pane, choose **Users > Users**.
3. Click the **System Users** tab. Click **Create a user**.
4. In the dialog box that appears, configure parameters.

| Parameter | Required | Description |
|---|---|---|
| User name | Yes | The Apsara Stack tenant account name of the user. The name must be 1 to 64 characters in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Display name | Yes | The display name of the user. The name must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). _ |
| Role | Yes | The role to be assigned to the user. Note You can enter role names in the field. Fuzzy match is supported. |
| Organization | Yes | The organization to which the user belongs. |

| Logon policy | Yes | The logon policy that specifies the logon time of the user and the IP address that the user logs on to. If you do not configure this parameter, the default policy is attached to the created user. Note The default policy does not specify the logon time of the user and the IP address that the user logs on to. To specify the logon time and IP address, you can modify the logon policy or create a logon policy. |
|---|---|---|
| Phone | Yes | The mobile phone number of the user. If you want to send text messages about the resource requests and usage to the mobile phone number, make sure that the specified mobile phone number is valid. Note If the mobile phone number of the user changes, update it on the system in a timely manner. |
| Landline | No | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | Yes | The email address of the user. If you want to send emails about the resource requests and usage to the email address, make sure that the specified email address is valid. Note If the email address changes, update it on the system in a timely manner. |
| DingTalk Key | No | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |
| Notify User by Email | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
| Notify User by DingTalk | No | If this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

5. Click **OK**.

#### 4.1.2 Create a role and grant permissions to the role

**role**

You can create custom roles, attach permission policies to the roles, and assign the roles to a user to grant permissions to the user. This topic describes how to create a role, assign the role to a user group, and attach a policy to the role.

**Background information**

A role is a set of access permissions. Each role has a range of permissions. A user can have multiple roles, which means that the user is granted all of the permissions defined for each role. A role can be used to grant the same set of permissions to a group of users. The total number of custom and default roles cannot exceed 20.

**Create a role**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. In the top navigation bar, click **Enterprise**.
5. In the left-side navigation pane, choose **Permissions > Role Permissions**.
6. In the upper-left corner of the **Role authorization** page, click **Create Custom Role**.
7. On the **Create Custom Role** page, click **Advanced Settings**.
8. In the **Advanced Settings** section, click **Create RAM Role & Attach Policy** .
9. In the Basic Configurations step of **Create RAM Role & Attach Policy** wizard, configure parameters.
i. Enter a value for **Role name** and **Description** separately. Select **Sharing Scope**. By default,
**Global** is select for **Sharing Scope**, which indicates that the role is visible to and used by all
organizations. Click **Next**. ii. In the Configure Custom Policy step, select an existing policy or create a new policy, and then click
**Next**.

> **Note:** You can select a maximum of five policies for a RAM role.

iii. In the Configure Trust Policy step, select values from the **Trust Organization** and **Trust Cloud**
**Service** drop-down lists separately. Click **Next**.

> **Note:** You can select multiple trust organizations and trust cloud services at a time for a RAM role.

iv. In the Preview Policy step, check the content of selected policies and trust policies, and click **Create**.
0. **Optional:**Add authorized users to the RAM role.
When you create a RAM role, you can add authorized users to the role. After you add authorized users to the RAM role, the users are granted the permissions of the role. i. **>** ii. Create a user and a user group
1. i.
ii. iii.

|   | Note |
|---|---|
|   | { "Version": "1", "Statement": [ { "Action": [ "edas:CreateNamespace" ], "Resource": [ "acs:edas:*:*:namespace/*" ], "Effect": "Allow" }, { "Action": [ "edas:ManageNamespace" ], "Resource": [ "acs:edas:*:*:namespace/$namespace" ], "Effect": "Allow" }, { "Action": [ "edas:ReadNamespace", "edas:DeleteNamespace" ], "Resource": [ "acs:edas:*:*:namespace/$namespace" ], "Effect": "Allow" } ] } |

iv.

#### 4.1.3 Repository access control

You can create users and grant different permissions to the users. This way, you can control the access of the users to Container Registry resources. This topic describes how to configure access control for repositories in different scenarios.

**Precautions**

When you authorize a user, pay attention to the following instructions to make sure that you do not grant excessive permissions to the user. You can grant a user the AdministratorAccess permission that contains management permissions on all Alibaba Cloud resources. In this case, the user has all permissions on Container Registry, regardless of whether the user is granted permissions before.

**System policy configuration**

AliyunContainerRegistryFullAccess This policy grants a user the same permissions on image resources as those of an Alibaba Cloud account. The user can perform all operations on image resources. `{`

```json
  "Statement": [
```

`{`

```json
      "Action": "cr:*",
      "Effect": "Allow",
      "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}` AliyunContainerRegistryReadOnlyAccess This policy grants a user the read-only permission on all image resources. For example, the user can view the repository list and pull images. `{`

```json
  "Statement": [
```

`{`

```json
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:Pull*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": "*"
```

`}` `],`

```json
  "Version": "1"
```

`}`

**Policy configuration for typical scenarios**

Grant the user the read and write permissions on a namespace of a Container Registry Advanced Edition instance. `{`

```json
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
```

`},` `{`

```json
"Action":[
```

```
      Action: [
        "cr:*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/$instanceid/$namespace/*",
        "acs:cr:*:*:repository/$instanceid/$namespace"
```

`]` `},` `{`

```json
      "Action": [
        "cr:List*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/$instanceid/*",
        "acs:cr:*:*:repository/$instanceid/*/*"
```

`]` `}` `],`

```json
  "Version": "1"
```

`}{`

```json
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": [
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
```

`},` `{`

```json
      "Action": [
        "cr:*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/$instanceid/$namespace/*",
        "acs:cr:*:*:repository/$instanceid/$namespace"
```

`]` `},` `{`

```json
      "Action": [
        "cr:List*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:*:*:repository/$instanceid/*",
        "acs:cr:*:*:repository/$instanceid/*/*"
```

`]` `}` `],`

```json
  "Version": "1"
```

`}`

**Authentication rules of Container Registry**

ARN format The following table describes the Alibaba Cloud Resource Name (ARN) format in an authorization policy when you use RAM to authorize access to the resources.

| Resource type | ARN format in an authorization policy |
|---|---|
| * | acs:cr:$regionid:$accountid:* |
| instance | acs:cr:$regionid:$accountid:instance/$instanceid |
| repository | acs:cr:$regionid:$accountid:repository/$instanceid/* acs:cr:$regionid:$accountid:repository/$instanceid acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/* acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/$repositoryname acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename |

The following table describes the parameters in the ARN format.

| Parameter | Description |
|---|---|
| regionid | The region ID, which can be replaced by an asterisk (*). |
| accountid | The ID of the Alibaba Cloud account, which can be replaced by an asterisk (*). |
| instanceid | The ID of the Container Registry Enterprise Edition instance. |
| namespacename | The name of the namespace. |
| repositoryname | The name of the repository. |

Authorization rules When you access the Container Registry API as a RAM user or by using Security Token Service (STS), Container Registry checks whether you have obtained the required permissions. The permissions that Container Registry checks vary based on the resources that are requested by the API operation and the syntax of the API operation. The following table describes the authentication rules for different API operations.

> **Note:** The asterisk (*) is used as a wildcard.

| API | Action | Resource |
|---|---|---|
| Queries a pair of temporary username and password that you use to log on to a Container Registry instance. | cr:GetAuthorizationToken | * |
| Queries a namespace. | cr:GetNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Creates a namespace. | cr:CreateNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Queries namespaces. | cr:ListNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/* |
| Deletes a namespace. | cr:DeleteNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |

| Updates a namespace. | cr:UpdateNamespace | acs:cr:$regionid:$accountid:chart/$ instanceid/$chartnamespacename |
|---|---|---|
| Queries a repository. | cr:GetRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image repositories. | cr:ListRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ * |
| Deletes an image repository. | cr:DeleteRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Updates an image repository. | cr:UpdateRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image tags in an image repository. | cr:ListRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Deletes an image from an image repository. | cr:DeleteRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries the information about image layers of an image tag. | cr:GetRepositoryLayers | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries the manifest information of an image tag. | cr:GetRepositoryManifest | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Updates a trigger for an image repository. | cr:UpdateWebHook | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |

### 4.2 Create a namespace

This topic describes how to create a namespace on a Container Registry Advanced Edition instance.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Advanced Edition instance, choose
**Repository > Namespace**.
4. On the **Namespace** page, click **Create Namespace**.
5. On the **Create Namespace** page, configure the Namespace and Default Repository Type parameters,
set whether to automatically create repositories, and then click **Submit**. By default, if you push an image to a repository that does not exist in a namespace, Container Registry automatically creates the repository based on the repository name that you specify. To disable this feature, turn off Auto Create for the namespace. By default, a repository that is automatically created upon image push is private. You can set Default Repository Type to Public for a namespace to change the default repository type.

### 4.3 Create an image repository

This topic describes how to create an image repository on a Container Registry Advanced Edition instance.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Repositories**.
4. On the **Repositories** page, click **Create Repository**.
5. On the Create Image Repository page, configure the **Organization**, **Resource Set**, **Region**,
**Namespace**, **Repository Name**, **Repository Type**, **Image Version**, **Digest**, and **Description**
parameters, and then click **Submit**.

### 4.4 Configure an access credential

You can configure an access credential to set a password that you use to log on to a Container Registry Advanced Edition instance. This method can ensure that you securely control the upload and download of container images. This topic describes how to configure an access credential.

**Background information**

Access credentials are independent of Alibaba Cloud accounts and passwords. Access credentials are available in two types: Password: A password is valid permanently. Keep it safe. If the password is lost, you can reset it. Temporary token: A temporary token is valid for one hour. If the temporary token is obtained by using Security Token Service (STS), the temporary token is valid so long as the STS token is valid.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Access Credential**.
4. On the **Access Credential** page, click **Set Password**.
5. In the **Set Password** dialog box, enter the password and confirm the password. Then, click **Confirm**.
6. **Optional:** For information about how to set a temporary token, see **GetAuthorizationToken** of **API**
**Management for Advanced Edition** in the **Container Registry Developer Guide**.

### 4.5 Upload and download images

This topic describes how to upload an image to and download an image from a Container Registry Advanced Edition instance.

**Procedure**

1. Obtain the address of the repository.
i. Log on to the Container Registry console. For more information, see Log on to the Container Registry console. ii. On the **Instances** page, click the card of a Container Registry Advanced Edition instance. iii. In the left-side navigation pane of the management page of the Container Registry Advanced Edition instance, choose **Repository > Repositories**. iv. On the **Repositories** page, click the name of the repository. On the **Details** page, obtain the address of the repository.
2. Run the following command to log on to the Advanced Edition instance.

```bash
docker login --username=<Your Alibaba Cloud account> <Address of the repository>
```

As prompted in the command output, enter the password that you set when you activated Container Registry. If you forget your password, you can reset it. For information about how to reset a password, see Configure an access credential.
3. Upload and download an image.
Upload an image a. Run the following command to add a tag to the image:

```bash
docker tag <ID of the image> <Address of the repository>/<Name of the namespace>/<Name of t he repository>:<Version number of the image>
```

b. Run the following command to upload the image to the repository:

```bash
 docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:<
Version number of the image>
```

Download an image Run the following command to download an image from the image repository:

```bash
docker pull <Address of the repository>/<Name of the namespace>/<Name of the repository>: <Version number of the image>
```

### 4.6 Configure a trigger

Container Registry provides the trigger feature for image repositories. If you create a trigger for an image repository, a notification is pushed to you when an image is built. This facilitates the redeployment of images for applications. If you create a trigger for a container service, the applications on the container service automatically pull and redeploy the new images that are built on the container service. This topic describes how to configure a trigger.

**Security rules on trigger usage**

HTTP: Port 80 is used by default. If you want to use another port, append the port number to the end of the trigger URL. You can use only the following port numbers: 80, 21, 443, 70, 210, 280, 488, 591, 777, and from 1025 to 65535. HTTPS: Port 443 is used by default. Only port 443 is supported. If you want to use another port, use HTTP.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Repositories**.
4. On the **Repositories** page, click the name of the repository.
5. In the left-side navigation pane of the details page of the repository, click **Trigger**.
6. On the **Trigger** page, click **Create**.
7. In the **Create Trigger** dialog box, configure parameters and click **Confirm**.

| Parameter | Description |
|---|---|
| Name | The name of the trigger. |
| Trigger URL | Enter the URL of the trigger that is created in Container Service for Kubernetes (ACK). |
| Trigger | You can select Every time, Expression trigger, or Tag triggers. Every time: Each time an image is built, an image pull is triggered. Expression trigger: Tags are filtered based on a regular expression. An image pull is triggered only when a tag matches the regular expression. You can enter a simple regular expression, such as release-v.* . An image pull is triggered only after an image with a tag that starts with release-v is built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. Tag triggers: An image pull is triggered based on the specified tags. You can specify a maximum of 10 tags based on which an image pull needs to be triggered. Then, an image pull is triggered only when images with the specified tags are built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. |

### 4.7 Push and pull Helm charts

After you install and configure a Helm client, you can use the Helm chart feature provided by Container Registry to push an pull charts and manage and distribute resources in Kubernetes clusters in an efficient manner.

**Background**

Kubernetes provides a unified API which you can use to define Kubernetes resources in YAML files. Kubernetes has a variety of resource types, such as Deployments, StatefulSets, and ConfigMaps. As the YAML-based software delivery system is constantly improved, the Cloud Native Computing Foundation (CNCF) community has developed charts and its implementation tool Helm to manage resources at a higher level. A chart is a collection of files that describe a related set of Kubernetes resources. For example, a chart can be a collection of files that describe WordPress and MySQL resources or a collection of resource description files for an etcd cluster. Helm is a command-line interface (CLI) tool used to manage charts and their releases.

**Usage notes**

Container Registry instances support Helm 2 and Helm 3 clients. The clients can help you manage cloudnative assets on the cloud. Helm clients of different versions provide different methods to manage Helm charts: If you use a Helm 3 client, you can manage Helm charts in image repositories. If you use a Helm 2 client, you must turn on Component Settings on the **Overview** page of the instance. After the status of the component changes to Running, you can use the client to manage chart repositories.

| Client version | Plug-in | Feature |
|---|---|---|
| Helm 2 | Helm-acr | Manage charts in chart repositories. For more information, seeUse Helm 2 to push and pull charts. |

| Helm 3 | Helm-push | Manage charts in chart repositories. Helm 3 clients support open source components. For more information, seeUse Helm 3 to push and pull charts. |
|---|---|---|

#### 4.7.1 Use Helm 2 to push and pull charts

Helm is a package manager for Kubernetes. Helm uses a packaging format called charts. After you create or update a chart, you can push the chart to a chart repository. This way, others can pull the chart from the chart repository for use.

**View chart repositories**

1. Log on to the Container Registry console.
2. On the top navigation bar of the **Apsara Uni-manager Management Console** , choose **Products >**
**Container Registry**.
3. On the **Container Registry** page, click the Container Registry instance on which you want to view
chart repositories. In the left-side navigation pane, choose **Helm Charts > Chart Repositories**. On the Chart Repositories page, you can view the information of existing chart repositories, such as Repository Name, **Namespace**, **Repository Type**, and **Created At**.
4. On the **Chart Repositories** page, click the name of a repository to go to the details page of the
repository. You can view the basic information of the repository and the user guide on how to push and pull charts by using a Helm client.

**Install and configure a Helm client**

1. Download Helm of the required version from the official website.

> **Note:** Make sure that the version of the client is v2.X. You can run the `helm version -c` command to check the versions of helm clients. In this example, the version of the client is v2.14.2.

2. Run the following commands to decompress the installation package of Helm and store the extracted
files in the specified directory:

```bash
# Decompress the installation package.
tar -zxvf helm-v2.14.2-linux-amd64.tgz
# Store the extracted files in the specified directory.
mv linux-amd64/helm /usr/local/bin/helm
```

3. Install the Helm-acr plug-in provided by Alibaba Cloud.

> **Note:** Before you install the Helm-acr plug-in, you must install Git.

```
helm plugin install https://github.com/AliyunContainerService/helm-acr
```

4. Initialize Helm.
If the current node is a Container Service for Kubernetes (ACK) cluster, a Tiller server is initialized in the cluster by default. You only need to initialize the client. If you also do not want to access Google charts, run the following command to initialize Helm:

```
helm init --client-only --skip-refresh
```

If the current node is a self-managed Kubernetes cluster and you do not want to access Google charts, run the following command to initialize Helm:

```
helm init --skip-refresh
```

**Push and pull charts**

1. Run the following commands to configure mapping for an on-premises repository.
You must specify the name of an on-premises repository and map the on-premises repository to a chart repository in a namespace of the Container Registry instance.

```
export HELM_REPO_USERNAME='<Username in the access credential of the Container Registry instance>'; export HELM_REPO_PASSWORD='<Password in the access credential of the Container Registry instance>'; helm repo add <Name of the on-premises repository> acr://<Instance name>-chart.<Region ID>.cr.aliyuncs.com/<Namespace name>/<Chart repository> --username ${HELM_REPO_USERNAME} -password ${HELM_REPO_PASSWORD}
```

2. Run the following commands to push a chart.

```bash
# Create an on-premises chart.
helm create <Chart name>
# Push the chart directory.
helm push <Chart name> <Name of the on-premises repository>
# Or push the compressed chart package.
helm cm-push <Chart name>-<Chart version>.tgz <Name of the on-premises repository>
```

On the **Chart Repositories** page, click the name of the chart repository. On the page that appears, click **Versions** in the left-side navigation pane. On the **Versions** page, you can view the new chart that you pushed.
3. Run the following commands to pull a chart.

```bash
# Update the on-premises chart index from the chart repository in Container Registry.
helm repo update
# Pull a chart.
helm fetch <Name of the on-premises repository>/<Chart name> --version <Chart version>
# Or directly install the chart.
helm install -f values.yaml <Name of the on-premises repository>/<Chart name> --version <Chart version>
```

4. Run the following commands to push a chart.

```bash
# Create an on-premises chart.
helm create <Chart name>
# Push the chart directory.
helm push <Chart name> <Name of the on-premises repository>
# Or push the compressed chart package.
helm cm-push <Chart name>-<Chart version>.tgz <Name of the on-premises repository>
```

On the **Chart Repositories** page, click the name of the chart repository. On the page that appears, click **Versions** in the left-side navigation pane. On the **Versions** page, you can view the new chart that you pushed.
5. Run the following commands to pull a chart.

```bash
# Update the on-premises chart index from the chart repository in Container Registry.
helm repo update
# Pull a chart.
helm fetch <Name of the on-premises repository>/<Chart name> --version <Chart version>
# Or directly install the chart.
helm install -f values.yaml <Name of the on-premises repository>/<Chart name> --version <Chart version>
```

#### 4.7.2 Use Helm 3 to push and pull charts

You can use a Helm cm-push plug-in to push and pull charts. Helm uses a packaging format called charts. A chart is a collection of files that describe a related set of Kubernetes resources. Before you use a Helm cm-push plug-in to push charts to a chart repository in Container Registry, you must run the `helm plugin install` command to install the Helm cm-push plug-in on your on-premises device. Then, you can run the `helm push` command to push charts.

**View chart repositories**

1. Log on to the Container Registry console.
2. On the top navigation bar of the **Apsara Uni-manager Management Console** , choose **Products >**
**Container Registry**.
3. On the **Container Registry** page, click the Container Registry instance on which you want to view
chart repositories. In the left-side navigation pane, choose **Helm Charts > Chart Repositories**. On the Chart Repositories page, you can view the information of existing chart repositories, such as
**Repository Name**, **Namespace**, **Repository Type**, and **Created At**.
4. On the **Chart Repositories** page, click the name of a repository to go to the details page of the
repository. You can view the basic information of the repository and the user guide on how to push and pull charts by using a Helm client.

**Install and configure a Helm client**

1. Download Helm.

> **Note:** The image push and pull operations described in this topic are applicable to Helm 3.7 or later. You can run the `helm version -c` command to check the versions of helm clients. In this example, Helm 3.10.0 is downloaded to push and pull charts.

2. Run the following commands to decompress the installation package of Helm and store the extracted
files in the specified directory:

```bash
# Decompress the installation package.
tar -zxvf helm-v3.10.0-rc.1-linux-amd64.tar.gz
# Store the extracted files in the specified directory.
mv linux-amd64/helm /usr/local/bin/helm
```

3. Run the following command to install the Helm cm-push plug-in:

> **Note:** Before you install the Helm cm-push plug-in, you must run the `yum install git` command to install Git.

```
helm plugin install https://github.com/chartmuseum/helm-push
```

**Push and pull charts**

1. Run the following command. In the command, specify the name of an on-premises repository and map
the on-premises repository to a chart repository in a namespace of the Container Registry instance.

```
helm repo add <Name of the on-premises repository> https://test9-7-chart****.cnhangzhou.cr.aliyuncs.com/ns1/repo1 --username <username> --password <password>
```

2. Run the following commands to push a chart.

```bash
# Create an on-premises chart.
helm create <Chart name>
# Push the chart directory.
helm cm-push <Chart name> <Name of the on-premises repository>
```

On the Chart Repositories page, click the name of the chart repository. In the left-side navigation pane of the page that appears, click **Versions**. On the **Versions** page, you can view the new chart that you pushed.
3. Run the following commands to pull or install a chart.

```bash
# Update the on-premises chart index from the chart repository in Container Registry.
helm repo update
# Pull a chart.
helm fetch <Name of the on-premises repository>/<Chart name> --version <Chart version>
# Or directly install the chart.
helm install -f values.yaml <Name of the on-premises repository>/<Chart name> --version <Chart version>
```

### 4.8 Replicate images between instances that belong to the same account

**instances that belong to the same**

**account**

This topic describes how to manually and automatically replicate an image across regions between instances that belong to the same account.

**Automate image replication across regions between instances that**

**belong to the same account**

You can configure a replication rule to automate image replication between two instances that belong to the same account. After you upload an image to the source instance that resides in one region, the system automatically replicates the image to the destination instance that resides in the other region.
1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Distribution > Instance Replication**. On the page that appears, click **Create**
**Rule**.
4. In the **Instance Information** step of the Create Rule wizard, set the Rule Name parameter, select
**Same Account** for the **Synchronization Scenario** parameter, select the region and name of the
target instance, and then click **Next**. A cloud department is an organization on the cloud platform. A cloud department is a collection of multiple persons and can represent a group company, a group branch, or a department in a company.
5. In the **Replication Information** step, set **Replication Level** to **Namespace** or **Repository**, select a
namespace or repository, and enter a regular expression to filter repository versions. Then, click
**Create Rule**.
When you upload an image to the source instance, the image is automatically replicated to the destination instance. In the left-side navigation pane of the management page of the Container Registry Advanced Edition instance, choose **Distribution > Replication Record**. If the status of the replication task on the **Replication Record** page is Completed and the image exists in the destination instance, the image is automatically replicated between the instances that belong to the same account.

**Manually replicate an image across regions between instances that**

**belong to the same account**

You can configure a replication rule to manually replicate an image from a source instance to a destination instance across regions.
1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Repositories**.
4. On the **Repositories** page, click the name of the repository.
5. In the left-side navigation pane of the management page of the repository, click **Tags**.
6. On the **Tags** page, click **Replicate** in the **Actions** column of the image.
7. In the **Select Destination Repository** dialog box, select **Same Account** for the **Synchronization**
**Scenario** parameter and select the region and name of the destination instance. Select a namespace
and a repository, enter a regular expression to filter repository versions, set **Overwrite existing**
**images that have the same name**, and then click **OK**.
After you manually create the replication rule, image replication between the instances is immediately triggered. On the Tags page, you can click Image Sync Records in the Actions column of the image. If the status of the replication task on the **Replication Record** page is Completed and the image exists in the destination instance, the image is manually replicated between the instances that belong to the same account.

### 4.9 Replicate images between instances that belong to different accounts

**instances that belong to different**

**accounts**

This topic describes how to manually and automatically replicate an image between instances that belong to different accounts.

**Prerequisites**

You have obtained the permissions on the multi-cloud management platform. For more information, see
**Multi-Cloud management platform** in **Apsara Uni-manager Management Console User Guide** .

**Automate image replication between instances that belong to**

**different accounts**

You can configure a replication rule to automate image replication between two instances that belong to different accounts. After you upload an image to the source instance in one account, the system automatically replicates the image to the destination instance that belong to the other account.
1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Distribution > Instance Replication**. On the page that appears, click **Create**
**Rule**.
4. In the **Instance Information** step of the Create Rule wizard, set the Rule Name parameter and select
Across Account for the Synchronization Scenario parameter. Select a destination cloud platform and a cloud department, select the name and ID of the target instance, and then click **Next**. A cloud department is an organization on the cloud platform. A cloud department is a collection of multiple persons and can represent a group company, a group branch, or a department in a company.
5. In the **Replication Information** step, set Replication Level to **Namespace** or **Repository**, select a
namespace or repository, and enter a regular expression to filter repository versions. Then, click
**Create Rule**.
When you upload an image to the source instance, the image is automatically replicated to the destination instance. In the left-side navigation pane of the management page of the Container Registry Advanced Edition instance, choose **Distribution > Replication Record**. If the status of the replication task on the **Replication Record** page is Completed and the image exists in the destination instance, the image is automatically replicated between the instances that belong to different accounts.

**Manually replicate an image between instances that belong to**

**different accounts**

You can configure a replication rule to manually replicate an image from a source instance to a destination instance across accounts.
1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Repositories**.
4. On the **Repositories** page, click the name of the repository.
5. In the left-side navigation pane of the management page of the repository, click **Tags**.
6. On the **Tags** page, click **Replicate** in the **Actions** column of the image.
7. In the Select Destination Repository dialog box, select Across Account for the Synchronization
Scenario parameter and select a destination cloud platform and a cloud department. Select the name and ID of the target instance, select a namespace and a repository, and enter a regular expression to filter repository versions. Set whether to overwrite existing images that have the same name and then click **OK**. After you manually create the replication rule, image replication between the instances across accounts is immediately triggered. On the Tags page, you can click Image Sync Records in the Actions column of the image. If the status of the replication task on the **Replication Record** page is Completed and the image exists in the destination instance, the image is manually replicated between the instances that belong to different accounts.

### 4.10 Configure a repository to be immutable

**immutable**

Container Registry allows you to configure a repository to be immutable to prevent image tags from being overwritten due to unintended operations. After you configure a repository to be immutable, the existing and newly added image tags in the repository cannot be overwritten except for the tags of the latest. After you push an image with a tag other than latest to the repository, you cannot push another image with the same tag to the repository. This ensures that the images in the repository are consistent with the images that have been deployed in containers. This topic describes how to configure a repository to be immutable.

**Procedure**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Repositories**.
4. On the Repositories page, find the repository that you want to configure and click **Manage** in the
**Actions** column.
5. On the page that appears, click **Edit** in the Details section.
6. In the **Modify Settings** dialog box, select **Immutable** and click **Confirm**.

> **Note:** To configure a repository to be mutable, clear **Immutable**.

**Verification**

| Run the | docker push | command to push an image whose tag is not latest to the repository. |
|---|---|---|
| docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:v1 |   |   |

2. Push another image whose tag is the same as the tag of the image that you pushed in Step 1.
The push request is denied. The following error is returned, which indicates that the image tag cannot be overwritten:

```
The requested tag already exists and cannot be overwritten.
```

| Run the | docker push | command to push an image whose tag is latest to the repository. |
|---|---|---|
| docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:latest |   |   |

4. Push another image whose tag is the same as the tag of the image that you pushed in Step 3.
The push request is allowed. The image that you pushed in Step 3 is overwritten by the image that you pushed in this step.
5. Configure the repository to be mutable by following the preceding procedure.
6. Push another image whose tag is the same as the tag of the image that you pushed in Step 1.
The push request is allowed. The image that you pushed in Step 1 is overwritten by the image that you pushed in this step.

### 4.11 Delete image tags

Container Registry allows you to delete multiple image tags of a Container Registry Enterprise Edition instance at a time. This topic describes how to delete multiple image tags at a time by configuring a tag retention policy.

**Configure a tag retention policy**

After you configure a tag retention policy, the image tags that do not match the policy are deleted.
1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Tags**.
4. On the **Tags** page, click **Create Retention Policy**.
5. In the **Create Retention Policy** dialog box, configure parameters in the **Set Deletion Scope** step
and then click **Next**. The retention policy can be applied to a namespace or an image repository.
**Namespace**: The retention policy is applied to all image repositories in the specified namespace.
**Repository**: If you select Repository and then select namespaces and repositories in the
namespaces, the retention policy is applied to the specified repositories in the namespaces.
6. In the **Configure Retention Policy** step, configure parameters and then click **Save**.

| Parameter | Description |
|---|---|
| Retain the Latest Images (required) | Set the number of the latest images that you want to retain. |
| Retain Image Tags (optional) | In addition to the number of the latest images that you want to retain, you can specify the image tags that you want to retain. Note The default value of this parameter is an asterisk (*), which indicates that all image tags are retained in addition to the specified number of the latest images. |

**Manually trigger a tag deletion task**

1. Log on to the Container Registry console. For more information, see Log on to the Container Registry
console.
2. On the **Instances** page, click the card of a Container Registry Advanced Edition instance.
3. In the left-side navigation pane of the management page of the Container Registry Advanced Edition
instance, choose **Repository > Tags**.
4. On the **Tags** page, find the retention policy that you want to apply and click **Execute** in the **Actions**
column.
5. In the **Tips** message, click **OK**.

### 4.12 Use the aliyun-acr-credential-helper component to pull images without a secret

**helper component to pull images**

**without a secret**

You can use the aliyun-acr-credential-helper component to pull private images without a secret from instances of Container Registry Standard Edition and Advanced Edition. This component is automatically installed in Container Service for Kubernetes (ACK) clusters. This topic describes how to use the aliyunacr-credential-helper component to pull a private image without a secret in different scenarios.

**Prerequisites**

An ACK cluster is created. For more information, see **Create a Kubernetes cluster** in **Container**
**Service for Kubernetes User Guide**.
A kubectl client is connected to your cluster. For more information, see **Use kubectl to connect to a**
**Kubernetes cluster** in **User Guide for Container Service for Kubernetes**.

**Precautions**

If you want to use the aliyun-acr-credential-helper component, do not specify the imagePullSecret parameter. If the imagePullSecret parameter is specified in the template of a Kubernetes resource, such as a Deployment, the component becomes invalid. If a Kubernetes resource, such as a Deployment, uses custom service accounts, you must modify the service-account parameter in the configuration file of the aliyun-acr-credential-helper component. This way, the component is authorized to pull images by using the custom service accounts. Check whether the private image that you want to pull resides in the same region as your ACK cluster. By default, you can pull private images only from Container Registry instances that reside in the same region as your ACK cluster. If you want to pull images from Container Registry instances that reside in different regions from your ACK cluster, see Scenario 2 in this topic. After you create a service account in a cluster, it takes some time for the aliyun-acr-credential-helper component to renew the token of the service account. The new token for pulling private images is generated based on the default permissions of your ACK cluster. Applications with the service account can use the token to pull images only after the token is renewed. If you create an application immediately after you create a service account, the application will fail to pull images because it is unauthorized. By default, the configuration of the aliyun-acr-credential-helper component overwrites the
**imagePullSecret** parameter of default service accounts in all namespaces. These service accounts
are automatically modified when the **service-account** parameter of the **acr-configuration** ConfigMap in the kube-system namespace is changed. When you modify the **acr-configuration** ConfigMap in the kube-system namespace, make sure that you use the same indentation as the example in this topic. We recommend that you paste the YAML code provided in this topic to the editor, replace the corresponding values, and apply the configuration. This ensures that the format of the ConfigMap is valid.

**Upgrade and configure the aliyun-acr-credential-helper component**

Before you use the aliyun-acr-credential-helper component to pull images, you must update and configure the component by performing the following steps: Configure the acr-configuration ConfigMap.

**Configure the acr-configuration ConfigMap in the ACK console**

1. Log on to the ACK console. For more information, see **Log on to the ACK console** in the **User Guide**
**for Container Service for Kubernetes**.
2. In the left-side navigation pane, click **Clusters**.
3. On the **Clusters** page, click the name of the cluster for which you want to configure the acr-
configuration ConfigMap.
4. In the left-side navigation pane of the **Cluster Information** page, choose **Configurations >**
**ConfigMap**.
5. In the upper part of the **ConfigMap** page, select **kube-system** from the Namespace drop-down list
and find the **acr-configuration** ConfigMap. Then, modify the ConfigMap by using one of the following methods: Method 1: Click **Edit** in the Actions column and edit the names and values of the **ConfigMap**. Method 2: Click **Edit YAML** in the Actions column and edit the names and values of the **ConfigMap**. The following table describes the names and values of the acr-configuration ConfigMap.

| Name of the acr- configuration ConfigMap | Description of the name | Value |
|---|---|---|
| service-account | The service accounts that are used by the aliyun-acr-credential-helper component to pull images. | Default value: default. Note Separate multiple service accounts with commas (,). Enter an asterisk (*) to specify all service accounts in all namespaces. |
| acr-registry-info | The information about Container Registry instances. Each instance can be specified by three fields of the String type in a YAML file. Note Set the three fields based on the following descriptions: instanceId: the ID of the Container Registry instance. This field is required for Container Registry Enterprise Edition instances. domains: the domain names of the Container Registry instance. This field is optional. By default, all domain names of the instance are specified. You can specify one or more domain names. Separate multiple domain names with commas (,). | The value is empty by default. This means that images are pulled from the default repository of the Container Registry instance that resides in the same region as your ACK cluster. Sample configurations for a Container Registry Advanced Edition instance: - instanceId: "cri-xxx" domains: "xxx.com,yyy.com" Sample configurations for a Container Registry Standard Edition instance: - instanceId:"" domains: "xxx.com,yyy.com" |
| watch-namespace | The namespaces from which images can be pulled without a secret. | Default value: default. Note If the value is set to all, images can be pulled from all namespaces without a secret. Separate multiple namespaces with commas (,). |
| expiring-threshold | The duration after which the cache token expires. | Default value: 15m. We recommend that you use the default value. |

**Configure the acr-configuration ConfigMap by using kubectl**

1. Run the following command to go to the editing page of the acr-configuration ConfigMap:

```bash
kubectl edit cm acr-configuration -n kube-system
```

2. Configure the parameters of the acr-configuration ConfigMap based on your requirements.
Sample configurations for Container Registry Advanced Edition and Standard Edition: Advanced Edition

```
apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"cri-xxx" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration
  namespace:kube-system
selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration
```

Standard Edition

```
apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration namespace:kube-system selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration
```

**Scenario 1: Pull private images from Container Registry Advanced**

**Edition and Container Registry Standard Edition instances**

ACK allows you to pull private images from both Container Registry Advanced Edition and Standard Edition instances, only from Container Registry Advanced Edition instances, or only from Container Registry Standard Edition instances. Modify the **acr-configuration****ConfigMap** based on your business requirements. For more information, see Update and configure the aliyun-acr-credential-helper component. Sample configurations: Pull private images from Container Registry Advanced Edition instances.

```
data:
    service-account: "default"
    watch-namespace: "all"
    expiring-threshold: "15m"
    notify-email: "c***@aliyuncs.com"
    acr-registry-info: |
      - instanceId: "cri-xxx"
        domains: "xxx.com,yyy.com"
```

Pull private images from Container Registry Standard Edition instances.

```
data:
    service-account: "default"
    watch-namespace: "all"
    expiring-threshold: "15m"
    notify-email: "c***@aliyuncs.com"
    acr-registry-info: |
      - instanceId: ""
        domains: "xxx.com,yyy.com"
```

Pull private images from both Container Registry Advanced Edition and Standard Edition instances.

```
data:
    service-account: "default"
    watch-namespace: "all"
    expiring-threshold: "15m"
    notify-email: "c***@aliyuncs.com"
    acr-registry-info: |
      - instanceId: ""
      - instanceId: "cri-xxxx"
```
