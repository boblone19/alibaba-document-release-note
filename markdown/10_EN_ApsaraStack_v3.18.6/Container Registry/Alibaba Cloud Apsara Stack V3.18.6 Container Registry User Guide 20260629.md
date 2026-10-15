---
title: "Container Registry User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 110
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Container Registry User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E9%95%9C%E5%83%8F%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Registry%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# Container Registry User Guide 20260629

| Primary Feature | Secondary Feature | Description | ACR Standard Edition | ACR Premium Edition | ACR Multi- instance Edition |
|---|---|---|---|---|---|
|  | Create Multiple Instances | Supports creating multiple instances. By default, up to 100 instances are supported. | Not supported | Not supported | Supported |

gistry?

## What is Container Registry?

Container Registry is a platform that allows you to manage and distribute cloud-native artifacts in a secure and efficient manner. Cloud-native artifacts include container images and Helm charts that meet the standards of Open Container Initiative (OCI). Container Registry provides the following features: image permission management, synchronous image distribution, and content signing. The features allow you to manage the entire lifecycle of container images. Container Registry simplifies the setup and O&M of container registries. Container Registry is integrated with Alibaba Cloud services such as Container Service for Kubernetes (ACK) to help enterprises reduce delivery complexity and create a one-stop solution for cloud-native applications.

**Classification of Container Registry Enterprise Edition**

Container Registry Standard Edition is suitable for small and medium-sized enterprises. It supports secure hosting and efficient distribution of container images. You can use multiple Alibaba Cloud accounts in the Container Registry Standard Edition, create 15 namespaces for each account, and maintain 1,000 public repositories or private repositories in each namespace. Container Registry Standard Edition allows 100 nodes to concurrently pull container images. Container Registry Advanced Edition is suitable for medium and large-sized enterprises. It provides secure hosting and lifecycle management of OCI artifacts, such as container images, Helm charts, and operators. Container Registry Advanced Edition also supports efficient artifact distribution scenarios, such as multi-region replication and cross-cloud replication. You can create up to 1,000 namespaces and maintain 100,000 repositories on a Container Registry Advanced Edition instance. Container Registry Advanced Edition allows 500 nodes to concurrently pull container images. Container Registry Multi-instance Edition is suitable for medium and large-sized enterprises. Based on Container Registry Advanced Edition, Container Registry Multi-instance Edition allows you to create multiple independent Container Registry instances within a single region. Each instance has its dedicated resources such as namespaces and image repositories. Container Registry Multi-instance Edition meets the requirements for storage isolation between image repositories and fine-grained permission management.

**Note**

Only the PaaS deployment mode supports Container Registry Multi-instance Edition instances.

**Features**

| Instance Management |  |  |  |  |  |
|---|---|---|---|---|---|
|  | Cross-instance Image Sync | Supports synchronizing image repositories across instances. | Not supported | Not supported | Supported |
|  | Delete Instance | Supports deleting and releasing image instances. | Not supported | Not supported | Supported |
| Artifact Distribution | Manual Sync | Supports manually triggering sync for a specific image version to enable disaster recovery and backup across regions. | Supported | Supported | Supported |
|  | Automatic Sync | Supports automatic synchronization based on sync rules after an image is pushed. | Not supported | Supported | Supported |
|  | Triggers | Supports automatically triggering events when a container image is updated. | Supported | Supported | Supported |
|  | DADI Image Acceleration | Supports DADI image acceleration. | Not supported | Supported | Supported |
|  | Encrypted Image Distribution | Supports distributing container images using the HTTPS encryption protocol. | Supported | Supported | Supported |

gistry?

|  | Image Signing | Supports signing container images to ensure end-to- end consistency from distribution to deployment and prevent man-in-the- middle attacks and unauthorized image updates or execution. | Supported | Supported | Not supported |
|---|---|---|---|---|---|
| Artifact Security |  |  |  |  |  |
|  | Signing Management | Supports GUI- based operations to add signatures at the instance and namespace levels. Note This feature depends on KMS and Container Security products and requires them to be used together. | Supported | Supported | Supported |
| Artifact Management | Container Images | Supports immutable image versions. | Not supported | Supported | Supported |
|  |  | Supports secure hosting of container images organized by namespace. | Not supported | Supported | Supported |
|  |  | Supports querying image versions and deleting image repositories. | Not supported | Supported | Supported |

gistry?

|  |  | Supports permission management for ASCM departments and resource sets, along with RAM user permissions. | Supported | Supported | Supported |
|---|---|---|---|---|---|
|  |  | Supports passwordless pull configuration during deployment on container platforms, eliminating the need to reconfigure Secrets for every deployment. | Supported | Supported | Not supported |
| Deployment Integration | Passwordless Pull |  |  |  |  |
|  | Deployment Selection | Supports visually selecting image repositories and versions from ACR during deployment on container platforms. | Supported | Supported | Supported |

gistry?

| Log in to the Container Registry console |  | Create a Container Registry instance |  | Creates a namespace |  | Creates an image repository |  | Upload and download images |
|---|---|---|---|---|---|---|---|---|

## Getting started

### Work with Container Registry

This topic describes how to use Container Registry. 1.
2. Create a namespace. For more information, see Create a namespace.
3. Create an image repository. For more information, see Create an image repository.
4. Upload and download images. For more information, see Upload and download images.
1.
2. Create a namespace. For more information, see Create a namespace.
3. Create an image repository. For more information, see Create an image repository.
4. Upload and download images. For more information, see Upload and download images.
1.
2. Create a Container Registry Multi-instance Edition instance. For more information, see Create an
instance.
3. Create a namespace. For more information, see Create a namespace.
4. Create an image repository. For more information, see Create an image repository.
5. Upload and download images. For more information, see Upload and download images.

### Log in to the Container Registry

**console**

This topic describes how to log in to the Container Registry console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations
in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management Console after**

**MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as described in Step 2 and click **Log On**. c. Enter the six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the six-digit MFA verification code and click **Authenticate**.

**Note**

For more information about how to bind an MFA device to enable MFA, see **Apsara Uni-**
**manager User Guide > Manage MFA**.
5. In the top navigation bar, choose **Products > Elastic Computing > Container Registry (ACR)**.
6. In the left-side navigation pane, choose an instance management page to perform operations.
On the **Standard Instance Management** page, click **Management**. You can create namespaces and upload or download images. On the **Advanced instance management** page, click **Management**. You can create namespaces and upload or download images. On the **Multi-Instance Edition List** page, click the ID of the instance that you want to manage. You can create namespaces and upload or download images.

**Note**

Only the PaaS deployment mode supports Container Registry Multi-instance Edition instances.
7. Use the floating action button to perform operations.
Click the Shopping Cart icon on the floating action button to go to the shopping cart page. Click the Arrow icon on the floating action button to expand or collapse the floating menu.

**Note**

The floating action button is in the lower-right corner of the page by default, and can be dragged to the desired position.

## Container Registry Standard

**Edition**

### Permission management

#### Create users and user groups

You can create users and assign different roles to the users to meet different requirements for system access control as an administrator. This topic describes how to create a user and a user group.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Create an organization**

To create a user or a user group, you must create an organization in advance.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.
4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Resources > Organizations**.
5. In the left-side organization tree of the **Organizations** page, click **root** and then click **Create**
**Organization** in the upper-right corner of the page.
6. In the **Add Organization** dialog box, specify a name for the organization and then click **OK**.
7. **Optional:** If the organization is created on multiple clouds, the **Synchronously Create Multi-cloud**
**Organization** check box is displayed after you click **OK**.
After you select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

**Create a user group**

A role cannot be directly assigned to a user. You can assign a role to a user group. Then, users in the user group can obtain the permissions of the role.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. In the upper-left corner of the **User Groups** page, click **Create a user group**.
3. In the **Create a user group** dialog box, specify **User Group Name**, select the organization that you
created from the **Organization** drop-down list, and then click **OK**.

| Parameter | Description |
|---|---|
| User name | The Apsara Stack account name of the user. The name must be 3 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). The name must start with a letter or a digit. _ |
| Display name | The display name of the user. The name must be 2 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at _ signs (@). |
| Role | You must select resource user. Otherwise, you will be prompted that you have no permissions when you attempt to log on to the Apsara Uni-manager Management Console. |
| Organization | The organization to which the user belongs. |
| Logon policy | Select Default Policies. |
| Phone | The mobile phone number of the user. If you want to send text messages about the resource requests and usage to the mobile phone number, make sure that the specified mobile phone number is valid. Note If the mobile number of the user changes, update it on the system in a timely manner. |
| Landline | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | The email address of the user. If you want to send emails about the resource requests and usage to the email address, make sure that the specified email address is valid. Note If the email address changes, update it on the system in a timely manner. |
| DingTalk Key | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |

You can create users based on your business requirements.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > Users**.
2. On the **Users** page, click the **System Users** tab, and then click **Create a user**.
3. In the **Create a user** dialog box, configure the basic information of the user and then click **OK**.

| Notify User by Email | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
|---|---|
| Notify User by DingTalk | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

**Add the user to the user group**

After a user is added to a user group, the user has the permissions of the role that is assigned to the user group.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. On the **User Groups** page, find the user group to which you want to add the user and click **Add User**
in the **Actions** column.
3. In the **Add User** dialog box, select the user under the organization, click the
icon, and then click
**OK**.

#### Create a role and assign permissions

Container Registry adopts the authentication system that consists of Alibaba Cloud account and RAM users. You can create a custom role, attach a permission policy to the role, and assign the role to a user to grant the permissions of the role to the user. This topic describes how to create a role, assign the role to a user group, and attach a permission policy to the role.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.
4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Permissions > Role Permissions**.
5. In the upper-left corner of the **Role Permissions** page, click **Create Custom Role**.
6.
7. **Optional:**
i. ii. Create a user group Add a user to a user group
8. i.

|  | Repository access control |
|---|---|

ii.

#### Repository access control

Users can obtain access to a repository if you grant them permissions. This topic describes how to configure access control for repositories in different scenarios.

**Background information**

For the level-1 to level-5 organizations created in the Apsara Uni-manager Management console, the subordinate organizations do not have independent accounts and passwords, but the users within the subordinate organizations have their own accounts and passwords, which are independent of each other. After you run the `docker login` command to log in to an image repository, you can view only the images uploaded and downloaded by your organization. Namespaces are isolated between different organizations (regardless of the levels), and image resources among organizations are invisible to each other. Users can obtain access to an image repository if you grant them permissions.

**Usage notes**

When you grant permissions to a user, pay attention to the following instructions to make sure that you do not grant excessive permissions to the user. You can grant a user the AdministratorAccess permission that contains management permissions on all Alibaba Cloud resources. In this case, the user has all permissions on Container Registry, regardless of whether the user is granted permissions before.

**System policy configuration**

AliyunContainerRegistryFullAccess This policy grants a user the same permissions on image resources as those of an Alibaba Cloud account. The user can perform all operations on image resources.

```json
{
  "Statement": [
    {
      "Action": "cr:*",
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

AliyunContainerRegistryReadOnlyAccess This policy grants a user the read-only permission on all image resources. For example, the user can view the repository list and pull images.

```json
{
  "Statement": [
    {
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:PullRepository"
```

`],`

```json
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

**Policy configuration for typical scenarios**

Scenario 1 Scenario: Grant a user the read-only permission on a namespace that is named juzhong. After the user logs on to the Container Registry instance, the user can pull all images in the namespace juzhong. The user can view information about the namespace and all repositories in the namespace by calling API operations.

```json
{
  "Statement": [
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}
```

**Important**

If you want to allow the user to view all the namespaces in the console, add the following authorization configurations. Then, the user can view all the namespaces and repositories. However, the user can pull only images from the repositories in the namespace juzhong.

```json
{
  "Statement": [
    {
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

]

```json
    },
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}
```

Scenario 2 Scenario: Grant a user all permissions on a repository, such as the repository nginx in the namespace juzhong in the China (Hangzhou) region.

**Important**

If you want to allow the user to manage repositories in the console, add the relevant configurations by referring to scenario 1.

```json
{
  "Statement": [
    {
      "Action": [
        "cr:*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": [
        "acs:cr:cn-hangzhou:*:repository/juzhong/nginx"
```

]

```json
    },
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}
```

Scenario 3 Scenario: Grant a user all permissions on a namespace.

**Important**

You can implement the scenario only by calling API operations. If you want to allow the user to view all repositories in the console, add the relevant configurations by referring to scenario 1.

```json
{
    "Statement": [
        {
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

]

```
        }
```

`],`

```json
    "Version": "1"
}
```

**Authentication rules of Container Registry**

ARN format

| Resource type | ARN format in an authorization policy |
|---|---|
| repository | acs:cr:$regionid:$accountid:repository/$namespacena me/$repositoryname |

| Parameter | Description |
|---|---|
| $regionid | The region ID, which can be replaced by an asterisk (*). |
| $accountid | The ID of the Alibaba Cloud account, which can be replaced by an asterisk (*). |
| $namespacename | The name of the namespace. |
| $repositoryname | The name of the image repository. |

| API operation | Action | Resource |
|---|---|---|
| Creates a namespace | cr:CreateNamespace | * |
| Deletes a namespace | cr:DeleteNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Updates a namespace | cr:UpdateNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Queries a namespace | cr:GetNamespace | acs:cr:$regionid:$accountid:reposit ory/$namespacename |
| Queries namespaces | cr:ListNamespace | * |
| Creates a repository | cr:CreateRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename |

The following table describes the Alibaba Cloud Resource Name (ARN) format in an authorization policy when you grant a user access to the resources. The following table describes the parameters in the ARN format. Authentication rules When you access the Container Registry API as a user or by using Security Token Service (STS), Container Registry checks whether you have obtained the required permissions. The permissions that Container Registry checks vary based on the resources that are requested by the API operation and the syntax of the API operation. The following table describes the authentication rules for different API operations.

| Deletes a repository | cr:DeleteRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
|---|---|---|
| Updates a repository | cr:UpdateRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries a repository | cr:GetRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries repositories | cr:ListRepository | * |
| Queries repositories in a namespace | cr:ListRepository | * |
| Queries the tag information about a repository | cr:ListRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Deletes an image tag | cr:DeleteRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries the manifest information about an image | cr:GetRepositoryManifest | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries the information about image layers | cr:GetRepositoryLayers | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Queries a temporary authorization token | cr:GetAuthorizationToken | * |
| Pulls images | cr:PullRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |
| Pushes images | cr:PushRepository | acs:cr:$regionid:$accountid:reposit ory/$namespacename/$repository name |

### Quota management

#### Configure quotas

This topic describes how to allocate resource quotas for a Container Registry Standard Edition instance in an organization or resource set.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Resource Pool Configuration**.
4. In the upper-left corner of the Resource Pool Configuration page, select a cloud platform, region ID,
and zone.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments. If you select All Zones, you can manage quotas in the region. If you select a zone, you can manage quotas in the zone, and the console displays only cloud services in the current zone.
5. Click **Container Registry Standard Edition** to go to the **Resource Pool Details** panel, and view
the details of Container Registry Standard Edition, such as **Resource Item**, **Logical Inventory**,
**Physical Inventory**, and **Total Activated Resources**.
6. In the **Resource Pool Details** panel, click **Configure Quota** in the lower part.
7. In the **Configure Quota** dialog box, add or remove quota items. For more information about quotas,
see Quota overview.

**Note**

After you select a zone on the Resource Pool Configuration page, the **Synchronously Modify**
**Quotas in Other Zones** option appears in the Configure Quota dialog box. You can select this
option to synchronize the quota item configurations in this zone to other zones.
**Add quota items**: In the **Available Quotas** list, select the quota items that you want to add and
click the icon to add the quota items to the **Selected Quota Items** list.
**Remove quota items**: In the **Selected Quota Items** list, select the quota items that you want to
remove and click the icon to remove the quota items.
8. Click **OK**.
9. In the **Resource Pool Details** panel, click **Create Inventory** in the lower part of the page, set a
quota for the resource, and then click **Save**.

**Step 2: Allocate quotas**

1. Log in to the Apsara Uni-manager Management Console as an operations administrator or an
organization administrator.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quotas**.
4. In the upper-left corner of the **Quotas** page, select a cloud platform from the Cloud Platform drop-
down list.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments.
5. On the right side of the product, set Region, Region, and Zone.
6. In the left-side organizational structure of the Quotas page, select the organization or resource set
whose resources you want to manage.
7. Click **Container Registry Standard Edition** to go to the Quota Details panel, and view the quota
details of Container Registry Standard Edition in the organization or resource set.

| Parameter |  | Parameter |
|---|---|---|
| Alert Rule Information | Cloud Platform | The cloud platform on which the quota alert rule takes effect. Note The Cloud Platform parameter is displayed only in multi-cloud environments. |
|  | Organization/ Resource Set | The organization or resource set for which the quota alert rule takes effect. |
|  | Include Child Organization | Specifies whether to apply the quota alert rule to the subordinate organizations and resource sets of the current organization. If you turn on Include Child Organization, the quota alert rule is applied to the current organization and its subordinate organizations and the resource sets of the current organization. This parameter is displayed only if you select an organization from the Organization/Resource Set drop-down list. : turns on Include Child Organization. : turns off Include Child Organization. |
|  | > Document Version: 20260629 |  |

8. In the **Quota Details** panel, click **Set Quota**, configure the parameters, and then click **Save**.

#### Create an alert rule for a quota

This topic describes how to create an alert rule for a quota of Container Registry Standard Edition in an organization and resource set. When the quota of an organization or a resource set reaches the preset threshold, the system notifies the administrator of the organization or resource set once a day. The system sends a notification when the quota alert is triggered for the first time every day.

**Prerequisites**

A quota is configured. For more information, see Configure a quota. You are assigned the operations administrator or organization administrator role. If you are assigned a custom role, the custom role must be granted the permissions to manage quotas and access the
**Quotas > Quotas** menu.

**Limits**

If a quota alert rule other than the preset one is enabled for a cloud service in an organization or a resource set, no more quota alert rules can be created for the cloud service in the organization or resource set. A quota alert rule automatically takes effect after it is created. Then, the preset quota alert rule applied to the organizations or resource sets to which the new quota alert rule applies is disabled.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. On the **Quota Alerts** page, click **Create Alert Rule**.
5. In the **Create Alert Rule** dialog box, configure the parameters that are described in the following
table.

|  | Region | The region in which the quota alert rule takes effect. |
|---|---|---|
|  | Cloud Service | Select Container Registry Standard Edition. |
|  | Alert Rule Name | The name of the quota alert rule. |
|  | Alert Type | The criteria based on which an alert is generated. Valid values:U sed Amount: An alert is generated when the used quota exceeds the configured alert threshold. Remaining Available Quota: An alert is generated when the available quota is less than the configured alert threshold. |
| Alert Information |  |  |
|  | Alert Threshold | Resource Type: the resource item of the cloud service specified in the Alert Rule Information section by default. Used Amount/Quota: the used amount and the quota configured for the cloud service in the organization or resource set by default. Threshold: Valid values: No, Percentage, and Number. Alert Threshold: the threshold based on which the alert rule is triggered. If the used quota exceeds the alert threshold or the available quota is less than the alert threshold, an alert is generated. If you set the Threshold parameter to No, the Alert Threshold parameter is set to No Alerts by default. |

| Quota item | Description |
|---|---|
| Image Repository Quota (Units) | The number of image repositories that can be created for Container Registry Standard Edition. |
| Image Namespace Quota (Units) | The number of image namespaces that can be created for Container Registry Standard Edition. |

6. Click **OK**.

#### Quota description

This topic describes the quotas that you can configure for Container Registry Standard Edition, calculation methods of quota usage, and inventory source.

**Quota items**

**Calculation methods of quota usage**

Usage of Image Repository Quota (Units) = Number of image repositories that are created for Usage of Image Namespace Quota (Units) = Number of image namespaces that are created for

**Note**

The quota usage is calculated based on the number of resource instances.

**Inventory source**

| Parameter | Description |
|---|---|
| Organization | The organization to which the namespace belongs. |
| Resource Set | The resource set to which the namespace belongs. |
| Region | The region in which the namespace resides. |
| Sharing Scope | Valid values: Current Resource Set Current Organization and Subordinate Organizations Current Organization |
| Namespace | The value must be 2 to 30 characters in length, and can contain lowercase letters, digits, underscores ( ), _ and hyphens (-). It cannot start or end with an underscore ( ) or a hyphen (-). _ |

Not applicable. By default, the inventory is unlimited.

### Create a namespace

This topic describes how to create a namespace in the Container Registry console.

**Background information**

A namespace is a collection of repositories. We recommend that you place the repositories of a company or an organization in the same namespace. Sample namespaces that are named after a company: aliyun and alibaba. Sample namespace that is named after a team or an organization: team.

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, click **Create Namespace**.
6. On the **Create Namespace** page, configure the **Organization**, **Resource Set**, **Region**, **Sharing**
**Scope**, and **Namespace** parameters, and then click **Confirm Order**. The following table describes
the parameters.

**Note**

You can also click **Add Configuration Quotation** to place the order later.

**What to do next**

You can create image repositories in the namespace.

### Delete a namespace

This topic describes how to delete a namespace from a Container Registry Standard Edition instance.

| Parameter | Description |
|---|---|
| Organization | The organization to which the repository belongs. |
| Resource Set | The resource set to which the repository belongs. |
| Region | The region in which the repository resides. |
| Sharing scope | Valid values: Current Resource Set Current Organization and Subordinate Organizations Current Organization |
| Namespace | The namespace to which the image repository belongs. |
| Repository Name | The name of the image repository. The name must be 1 to 64 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It _ cannot start or end with a hyphen (-) or an underscore ( ). _ |
| Digest | The digest of the repository. |

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, find the namespace that you want to delete and click **Delete** in the
**Actions** column.
6. In the dialog box that appears, select **Confirm to Delete** and click **OK**.

### Create an image repository

This topic describes how to create an image repository in the Container Registry console.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, click **Create Image Repository**.
6. On the **Create Repository** page, configure the parameters and then click **Confirm Order**.

**Note**

You can also click **Add Configuration Quotation** for later purchase.

| Details | The description of the repository. The description can be up to 2,000 characters in length. |
|---|---|
| Repository Type | The type of the image repository. Valid values: Public and Private. |

| Parameter | Description |
|---|---|
| Repository Type | By default, users must log in to the corresponding Container Registry instance if they want to pull a public image. If you want public images to be pulled by anonymous users, turn on Allow Anonymous Users to Pull Public Artifacts for the instance. To pull a private image, users must obtain the pull operation permission and log in to the corresponding Container Registry instance. |
| Digest | The summary of the image repository. |
| Description | The description of the image repository. |

**What to do next**

After the repository is created, you can click **Manage** in the **Actions** column that corresponds to the repository to go to the **Basic Information** page and learn how to manage the repository.

### Manage image repositories

This topic describes how to manage image repositories of Container Registry Standard Edition instances.

**Modify an image repository**

1. 2. 3. 4.
5. Optional. On the **Image Repository** page, select a namespace and enter a repository name keyword
to perform a fuzzy search.
6. On the **Image Repository** page, find the repository that you want to manage and click **Management**
in the **Operation** column.
7. On the **Basic Information** page, you can view the information on the following tabs:
**User Guide**: provides the information about how to log in to the instance, pull and push images, add
a tag to an image, and select an image repository.
**Image Description**: provides the description of the image.
8. On the **Basic Information** page, click **Edit**.
9. In the **Modify Basic Information** dialog box, configure the **Repository Type**, **Digest**, and
**Description** parameters. Then, click **OK**.
For more information, see Configure a trigger.

**Image Version**

1. In the left-side navigation pane of the **Basic Information** page, click **Image Version**.
You can view the following information about the images in the image repository: **Edition**, **Image ID**,
**Image Tag Status**, **Digest**, **Image Size**, and **Last Update At**.
2. Perform the following operations in the **Actions** column of an image tag:
Click **Delete**. In the dialog box that appears, select **Confirm to Delete Image of This Tag** and click **OK**. Click **Layer information** and view the layer information, including the size and metadata for each layer of the image. Click **Image Replication**. In the **Select Destination Repository for Replication** dialog box, configure the **Image Tag to be Copied** and **Destination Repository** parameters. Then, click **OK**.

**Image Synchronization**

For more information, see Replicate an image.

### Delete an image repository

This topic describes how to delete an image repository from a Container Registry Standard Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, find the repository that you want to delete and click **Delete** in the
**Actions** column.
6. In the dialog box that appears, select **Confirm to Delete** and click **OK**.

### Configure an access credential

Access credentials can be used to control and secure the upload and download of container images. This topic describes how to configure an access credential.

**Prerequisites**

Only operations administrators, resource set administrators, and organization administrators can set fixed passwords. For other users, you must create a custom role, select **Reset the passwords of**
**Standard Edition instances**, and assign the custom role to the user before the user can set a fixed
password. For more information, see Create a role and assign permissions.

**Procedure**

1. 2. 3. 4.
5. On the **Access Credential** page, click **Set a fixed password**.
6. In the **Set a fixed password** dialog box, configure the **Password** and **Confirm password**
parameters. Then, click **OK**.
7. **Optional.** For more information about how to set a temporary token, see **GetAuthorizationToken** of
**API Reference for Standard Edition** in the **Container Registry Developer Guide**.

**What to do next**

You can use the password or temporary token that you set to log in to the Container Registry instance.
1. On the Access Credential page, check the logon command.
2. Run the login command and enter the logon password as prompted in the command output.

### Upload and download images

This topic describes how to upload and download images.

**Procedure**

1. View the username.
i. ii. iii. iv. v. On the **Access Credential** page, view and record the username and the domain name of the repository.
2. Run the following command to log on to the image repository:

```bash
sudo docker login --username=<Username> <Domain name of the repository>
```

As prompted in the command output, enter the password that you set when you activated Container Registry. If you forget your password, you can reset it. For information about how to reset a password, see Configure an access credential.
3. Upload and download an image.
Upload an image a. Run the following command to add a tag to the image:

```bash
sudo docker tag <ID of the image> <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

b. Run the following command to upload the image:

```bash
sudo docker push <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

| Parameter | Description |
|---|---|
| Image Tag to be Copied | Select the version of the repository to be replicated. |
| Destination Repository | Select the region, namespace, and name of the destination repository and enter the version of the destination repository. |

Download an image Run the following command to download an image:

```bash
sudo docker pull <Domain name of the repository>/<Name of the namespace>/<Name of the repository>:<Image version number>
```

4. **Optional:** Modify the image name.
i. Run the following command to query the ID of the image:

```bash
sudo docker images
```

ii. Run the following command to modify the name of the image:

```bash
sudo docker tag <ID of the image> registryDomain/<Name of the namespace>/<Name of the repository>:<Image version number>
```

### Replicate an image

Container Registry allows you to replicate images across data centers. This way, you can obtain the expected image from the nearest data center when you deploy workloads.

**Prerequisites**

A namespace is created. For more information, see Create a namespace. An image repository is created in the namespace. For more information, see Create an image repository.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repositories** page, find the target repository and click **Manage** in the **Actions**
column.
6. In the left-side navigation pane of the details page of the repository, click **Image Synchronization**.
7. On the Image Replication page, click **Create Copy Task**.
8. In the **Select Destination Repository for Replication** dialog box, configure parameters and then
click **OK**.

**Execution result**

On the **Image Replication** page, you can view the status of the replication task. You can click **Details** in the Actions column of the task to check the replication status of image layers.

### Configure a trigger

| Parameter | Description |
|---|---|
| Name | Enter a name for the trigger. |
| Trigger URL | Enter the URL of the trigger that is created in Container Service for Kubernetes (ACK). |

Container Registry provides the trigger feature for image repositories. If you create a trigger for an image repository, a notification is pushed to you when an image is built. This facilitates the redeployment of images for applications. This topic describes how to configure a trigger.

**Security rules on trigger usage**

HTTP services: Port 80 is used by default. If you want to use another port, append the port number to the end of the trigger URL. You can use only the following port numbers: 80, 21, 443, 70, 210, 280, 488, 591, 777, and from 1025 to 65535. HTTPS services: Port 443 is used by default. Only port 443 is supported. If you want to use another port, use HTTP.

**Create a trigger**

**Note**

A trigger of a repository can subscribe to events generated by a new image. When a new image is generated, you can view the access records of the trigger, including the request time, request parameters, and request results. The request parameters provide information about the current repository. Before you configure a Container Service trigger, bind a repository trigger. For more information, see **Kubernetes clusters > Application management > Use application triggers** in the **Alibaba Cloud Container Service for Kubernetes User Guide**. 1. 2. 3. 4.
5. On the **Image Repositories** page, find the target repository and click **Manage** in the **Actions**
column.
6. On the details page of the image repository, click **Trigger** in the left-side navigation pane.
7. On the **Trigger** page, click **Create**.
8. In the **Create Trigger** dialog box, set the parameters and click **OK**.

| Trigger Mode | Valid values: Trigger All, Expression-based Trigger, and Tag-based Trigger. Trigger All: Each time an image is built, an image pull is triggered. Expression-based Trigger: Tags are filtered based on a regular expression. An image pull is triggered only when a tag matches the regular expression. You can enter a simple regular expression. For example, if you enter release-v.* , an image pull is triggered only after an image with a tag that starts with release-v is built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. Tag-based Trigger: An image pull is triggered based on the specified tags. You can specify a maximum of 10 tags based on which an image pull needs to be triggered. Then, an image pull is triggered only when images with the specified tags are built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. |
|---|---|

**What to do next**

**View access records**

1. On the **Trigger** page, find the trigger that you want to manage and click **Access Log** in the **Actions**
column.
2. In the **Access Log** dialog box, you can view information such as **Access Status Code** and **Accessed**
**At**. Find the access log that you want to view and click **Details** in the **Actions** column. You can view
the details of the access log, including the request time, request parameters, and request results.

**Modify a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Modify** in the **Actions**
column.
2. In the **Modify Trigger** dialog box, modify the configuration of the trigger and click **OK**.

**Delete a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Delete** in the **Actions**
column.
2. In the **Are you sure you want to delete the repository** message, click **OK**.

### Sign container images

When you manage container images, you can use content trust to verify both the integrity and the publisher of images. Image publishers can encrypt images by using digital signatures that are stored in Container Registry.

**Install and configure signature tools**

1. Install Alibaba Cloud Command Line Interface (CLI). For more information, see Install Alibaba Cloud
CLI.
2. Run the following command to configure Alibaba Cloud CLI:

```
./aliyun configure set \ --profile akProfile \ --mode AK \ --region cn-qingdao-env17-d01 \ -access-key-id yourAK \ --access-key-secret yourAK
```

3. After you install and configure the GPG tool, run the following command to export the public key:

```bash
# Query pubKeyIdgpg --fingerprint# Export public key gpg --armor --output public-key.txt --
export yourUser.
```

**Note**

For Apsara Stack instances, instanceId is set to default.

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

**Note**

The user in the following example is `abcdef@example.com` .

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

| Parameter | Description |
|---|---|
| Instance ID | The ID of the instance. Example: cri-priv**. |
| Instance Name | The name of the instance, which is easy to identify and manage. |
| Region | The region ID of the instance. Example: cn-qingdao-env***. |
| Running status | The current status of the instance. |
| Instance Specification | Apsara Stack Advanced Specification is displayed. |
| Creation Time | The time when the instance was created. |
| Update Time | The last time when the instance status or configuration was updated. |

| Parameter | Description |
|---|---|
| Warehouse | The number of repositories that you have created and the quota. Example: 100/100000. |
| Namespace | The number of namespaces that you have created and the quota. Example: 15/1000. |
| OSS Bucket | - |
| OSS Bucket storage usage | - |

## Container Registry Advanced

**Edition**

### Instance overview

This topic describes how to view the information about a Container Registry Advanced Edition instance.

**Procedure**

1. 2.
3. On the **Advanced instance management** page, you can view the following information:

**Instance information**

**Warehouse information**

**Basic functions**

| Parameter | Description |
|---|---|
| Global synchronous acceleration | Cross-region automatic synchronization is supported. Synchronization rules can be configured for namespaces or repositories. |
| Trusted content | You can sign OCI artifacts such as container images and Helm charts. |
| Helm Chart | You can manage the full lifecycle of multi-version cloud-native artifacts such as Helm charts. |

| Parameter | Description |
|---|---|
| Access credentials | Configure access credentials. For more information, see Configure an access credential. |
| Namespace | Create namespaces. For more information, see Create a namespace. |
| Image Repository | Create image repositories. For more information, see Create an image repository. |

**Novice Guide**

The **Instance settings** module is not available in the current version.

### Permission management

#### Create a user and a user group

You can create users and assign different roles to the users to meet different requirements for system access control as an administrator. This topic describes how to create a user and a user group.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Create an organization**

To create a user or a user group, you must create an organization in advance.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

| Parameter | Description |
|---|---|
| User name | The Apsara Stack account name of the user. The name must be 3 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). The name must start with a letter or a digit. _ |
| Display name | The display name of the user. The name must be 2 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at _ signs (@). |
| Role | You must select resource user. Otherwise, you will be prompted that you have no permissions when you attempt to log on to the Apsara Uni-manager Management Console. |
| Organization | The organization to which the user belongs. |

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.
4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Resources > Organizations**.
5. In the left-side organization tree of the **Organizations** page, click **root** and then click **Create**
**Organization** in the upper-right corner of the page.
6. In the **Add Organization** dialog box, specify a name for the organization and then click **OK**.
7. **Optional:** If the organization is created on multiple clouds, the **Synchronously Create Multi-cloud**
**Organization** check box is displayed after you click **OK**.
After you select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

**Create a user group**

A role cannot be directly assigned to a user. You can assign a role to a user group. Then, users in the user group can obtain the permissions of the role.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. In the upper-left corner of the **User Groups** page, click **Create a user group**.
3. In the **Create a user group** dialog box, specify **User Group Name**, select the organization that you
created from the **Organization** drop-down list, and then click **OK**. You can create users based on your business requirements.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > Users**.
2. On the **Users** page, click the **System Users** tab, and then click **Create a user**.
3. In the **Create a user** dialog box, configure the basic information of the user and then click **OK**.

| Logon policy | Select Default Policies. |
|---|---|
| Phone | The mobile phone number of the user. If you want to send text messages about the resource requests and usage to the mobile phone number, make sure that the specified mobile phone number is valid. Note If the mobile number of the user changes, update it on the system in a timely manner. |
| Landline | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
| Email | The email address of the user. If you want to send emails about the resource requests and usage to the email address, make sure that the specified email address is valid. Note If the email address changes, update it on the system in a timely manner. |
| DingTalk Key | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |
| Notify User by Email | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
| Notify User by DingTalk | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

**Add the user to the user group**

After a user is added to a user group, the user has the permissions of the role that is assigned to the user group.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. On the **User Groups** page, find the user group to which you want to add the user and click **Add User**
in the **Actions** column.
3. In the **Add User** dialog box, select the user under the organization, click the
icon, and then click
**OK**.

#### Create a role and grant permissions to the

**role**

Container Registry adopts the authentication system that consists of Alibaba Cloud account and RAM users. You can create a custom role, attach a permission policy to the role, and assign the role to a user to grant the permissions of the role to the user. This topic describes how to create a role, assign the role to a user group, and attach a permission policy to the role.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.
4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Permissions > Role Permissions**.
5. In the upper-left corner of the **Role Permissions** page, click **Create Custom Role**.
6.

|  | Repository access control |
|---|---|

7. **Optional:**
i. ii. Create a user group Add a user to a user group
8. i.
ii.

#### Enable access control for a repository

You can create users and grant different permissions to the users. This way, you can control the access permissions of the users on Container Registry resources. This topic describes how to configure access control for repositories in different scenarios.

**Background information**

For the level-1 to level-5 organizations created in the Apsara Uni-manager Management console, the subordinate organizations do not have independent accounts and passwords, but the users within the subordinate organizations have their own accounts and passwords, which are independent of each other. After you run the `docker login` command to log in to an image repository, you can view only the images uploaded and downloaded by your organization. Namespaces are isolated between different organizations (regardless of the levels), and image resources among organizations are invisible to each other. Users can obtain access to an image repository if you grant them permissions.

**Usage notes**

When you authorize a user, pay attention to the following instructions to make sure that you do not grant excessive permissions to the user. You can grant a user the AdministratorAccess permission that contains management permissions on all Apsara Stack resources. In this case, the user has all permissions on Container Registry, regardless of whether the user is granted permissions before.

**System policies**

AliyunContainerRegistryFullAccess This policy grants a user the same permissions on image resources as those of an Apsara Stack account. The user can perform all operations on image resources.

```json
{
  "Statement": [
    {
      "Action": "cr:*",
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

AliyunContainerRegistryReadOnlyAccess This policy grants a user the read-only permission on all image resources. For example, the user can view the repository list and pull images.

```json
{
  "Statement": [
    {
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:Pull*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

**Policies for typical scenarios**

Grant the user the read and write permissions on a namespace of a Container Registry Advanced Edition instance.

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
```

```
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
    },
    {
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

]

```json
    },
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
    },
    {
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

]

```json
    },
    {
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

]

```
    }
```

`],`

| Resource type | ARN format |
|---|---|
| * | acs:cr:$regionid:$accountid:* |
| instance | acs:cr:$regionid:$accountid:instance/$instanceid |
| repository | acs:cr:$regionid:$accountid:repository/$instanceid/* acs:cr:$regionid:$accountid:repository/$instanceid acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/* acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/$repositoryname acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename |

| Parameter | Description |
|---|---|
| regionid | The region ID, which can be replaced by an asterisk (*). |
| accountid | The ID of the Apsara Stack account, which can be replaced by an asterisk (*). |
| instanceid | The ID of the Container Registry Advanced Edition instance. |
| namespacename | The namespace name. |
| repositoryname | The name of the image repository. |

```json
  "Version": "1"
}
```

**Authentication rules of Container Registry**

ARN format The following table describes the Alibaba Cloud Resource Name (ARN) format in an authorization policy when you use RAM to authorize access to the resources. The following table describes the parameters in the ARN format. Authentication rules When you access the Container Registry API as a RAM user or by using Security Token Service (STS), Container Registry checks whether you have obtained the required permissions. The permissions that Container Registry checks vary based on the resources that are requested by the API operation and the syntax of the API operation. The following table describes the authentication rules of different API operations.

**Note**

The asterisk (*) is used as a wildcard.

| API | Action | Resource |
|---|---|---|
| Queries a pair of temporary username and password that is used to log in to a Container Registry instance | cr:GetAuthorizationToken | * |
| Queries a namespace | cr:GetNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Creates a namespace | cr:CreateNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Queries namespaces | cr:ListNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/* |
| Deletes a namespace | cr:DeleteNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Updates a namespace | cr:UpdateNamespace | acs:cr:$regionid:$accountid:chart/$ instanceid/$chartnamespacename |
| Queries a repository | cr:GetRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image repositories | cr:ListRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ * |
| Deletes an image repository | cr:DeleteRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Updates an image repository | cr:UpdateRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image tags in an image repository | cr:ListRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Deletes an image from an image repository | cr:DeleteRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries the information about image layers of an image tag | cr:GetRepositoryLayers | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |

| Queries the manifest information of an image tag | cr:GetRepositoryManifest | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
|---|---|---|
| Updates a trigger for an image repository | cr:UpdateWebHook | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |

### Quota management

#### Configure quotas

This topic describes how to allocate resource quotas for a Container Registry Advanced Edition instance in an organization or resource set.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Resource Pool Configuration**.
4. In the upper-left corner of the Resource Pool Configuration page, select a cloud platform, region ID,
and zone.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments. If you select All Zones, you can manage quotas in the region. If you select a zone, you can manage quotas in the zone, and the console displays only cloud services in the current zone.
5. Click **Container Registry Advanced Edition**. In the **Resource Pool Details** panel, you can view the
details of the Container Registry Advanced Edition instance, including **Resource Items**, **Logical**
**Inventory**, **Physical Inventory**, and **Total Activated Resources**.
6. In the **Resource Pool Details** panel, click **Configure Quota** in the lower part.
7. In the **Configure Quota** dialog box, add or remove quota items. For more information about quotas,
see Quota overview.

**Note**

After you select a zone on the Resource Pool Configuration page, the **Synchronously Modify**
**Quotas in Other Zones** option appears in the Configure Quota dialog box. You can select this
option to synchronize the quota item configurations in this zone to other zones.
**Add quota items**: In the **Available Quotas** list, select the quota items that you want to add and
click the icon to add the quota items to the **Selected Quota Items** list.
**Remove quota items**: In the **Selected Quota Items** list, select the quota items that you want to
remove and click the icon to remove the quota items.
8. Click **OK**.
9. In the **Resource Pool Details** panel, click **Create Inventory** in the lower part of the page, set a
quota for the resource, and then click **Save**.

| Parameter | Description |
|---|---|

**Step 2: Allocate quotas**

1. Log in to the Apsara Uni-manager Management Console as an operations administrator or an
organization administrator.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quotas**.
4. In the upper-left corner of the **Quotas** page, select a cloud platform from the Cloud Platform drop-
down list.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments.
5. On the right side of the product, set Region, Region, and Zone.
6. In the left-side organizational structure of the Quotas page, select the organization or resource set
whose resources you want to manage.
7. Click **Container Registry Advanced Edition** to go to the **Quota Details** panel and view the quota
details in the organization or resource set.
8. In the **Quota Details** panel, click **Set Quota**, configure the parameters, and then click **Save**.

#### Create an alert rule for a quota

This topic describes how to create an alert rule for a quota of Container Registry Advanced Edition in an organization or resource set. When the quota of an organization or a resource set reaches the preset threshold, the system notifies the administrator of the organization or resource set once a day. The system sends a notification when the quota alert is triggered for the first time every day.

**Prerequisites**

A quota is configured. For more information, see Configure a quota. You are assigned the operations administrator or organization administrator role. If you are assigned a custom role, the custom role must be granted the permissions to manage quotas and access the
**Quotas > Quotas** menu.

**Limits**

If a quota alert rule other than the preset one is enabled for a cloud service in an organization or a resource set, no more quota alert rules can be created for the cloud service in the organization or resource set. A quota alert rule automatically takes effect after it is created. Then, the preset quota alert rule applied to the organizations or resource sets to which the new quota alert rule applies is disabled.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. On the **Quota Alerts** page, click **Create Alert Rule**.
5. In the **Create Alert Rule** dialog box, configure the parameters that are described in the following
table.

| Alert Rule Information | Cloud Platform | The cloud platform on which the alert rule takes effect. Note The Cloud Platform parameter is displayed only in multi-cloud scenarios. |
|---|---|---|
|  | Organization/ Resource Set | The organization or resource set for which the alert rule takes effect. |
|  | Include Child Organization | Specifies whether to apply the alert rule to the subordinate organizations and resource sets of the current organization. If you turn on Include Child Organization, the alert rule is applied to the current organization and all the subordinate organizations and resource sets of the current organization. This parameter is displayed only if you select an organization from the Organization/Resource Set drop-down list. : turns on Include Child Organization. : turns off Include Child Organization. |
|  | Region | The region in which the alert rule takes effect. |
|  | Cloud Service | Select Container Registry Advanced Edition. |
| Alert Information | Alert Rule Name | The name of the alert rule. |
|  | Alert Type | The criteria based on which an alert is generated. Valid values:U sed Amount: An alert is generated when the used quota exceeds the configured alert threshold. Remaining Available Quota: An alert is generated when the available quota is less than the configured alert threshold. |
|  | Alert Threshold | Resource Type: the resource item of the cloud service specified in the Alert Rule Information section by default. Used Amount/Quota: the used amount and the quota configured for the cloud service in the organization or resource set by default. Threshold: Valid values: No, Percentage, and Number. Alert Threshold: the threshold based on which the alert rule is triggered. If the amount of used resources exceeds the alert threshold or the amount of remaining available resources is less than the alert threshold, an alert is generated. If you set the Threshold parameter to No, the Alert Threshold parameter is set toN o Alerts by default. |

6. Click **OK**.

#### Quota overview

| Quota | Description |
|---|---|
| Apsara Stack Advanced Edition Namespace Quota (Units) | The number of namespaces that can be created for Container Registry Advanced Edition. |
| Apsara Stack Advanced Edition Image Repository Quota (Units) | The number of image repositories that can be created for Container Registry Advanced Edition. |

| Parameter | Description |
|---|---|

This topic describes the quotas that you can configure for Container Registry Advanced Edition, calculation methods of quota usage, and inventory source.

**Calculation methods of quota usage**

Usage of Apsara Stack Advanced Edition Namespace Quota (Units) = Number of namespaces that are created for Container Registry Advanced Edition Usage of Apsara Stack Advanced Edition Image Repository Quota (Units) = Number of image repositories that are created for Container Registry Advanced Edition

**Note**

The quota usage is calculated based on the number of resource instances.

**Inventory source**

No inventory is involved. By default, the inventory is unlimited.

### Create a namespace

This topic describes how to create a namespace on a Container Registry Advanced Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, click **Create Namespace**.
6. On the **Create Namespace** page, configure the Namespace, Auto Create, and Default Repository
Type parameters, and then click **Confirm Order**. The following table describes the parameters.

**Note**

You can also click **Add Configuration Quotation** for later purchase. By default, if you push an image to a repository that does not exist in a namespace, Container Registry automatically creates the repository based on the repository name that you specify. To disable this feature, turn off Auto Create for the namespace. By default, a repository that is automatically created upon image push is private. To allow the automatically created repositories to be public, you can set the Default Repository Type parameter to Public.

| Organization | The organization to which the namespace belongs. |
|---|---|
| Resource Set | The resource set to which the namespace belongs. |
| Region | The region in which the namespace resides. |
| Sharing Scope | Valid values: Current Resource Set Current Organization and Subordinate Organizations Current Organization |
| Instance Name | The name of the instance is automatically populated. |
| Namespace | The name of the namespace. The name must be 2 to 120 characters in length and can contain lowercase letters, digits, underscores ( ), hyphens (-), and _ periods (.). It cannot start or end with an underscore ( ), hyphen (-), or period (.). _ |
| Auto Create | Specifies whether the system automatically creates a repository. |
| Default Repository Type | The type of the image repository. Valid values: Public and Private. |

### Modify image accessibility

The system allows you to modify the types of existing images and new images. This topic describes how to change the types of all images in the same namespace.

**Procedure**

1. 2. 3. 4.
5. In the namespace list, click **Public** or **Private** in the **Default Repository Type** column.

**Note**

If the **Automatically Create Repository** feature is disabled, you must enable the **Automatically**
**Create Repository** feature before you can set the **Default Repository Type** parameter.
6. In the dialog box that appears, select **Inventory and new images are modified** or **Add only**
**Image modifications** based on your business requirements, and then click **OK**.

### Delete a namespace

This topic describes how to delete a namespace in an Advanced Edition instance of Container Registry Enterprise Edition.

| Parameter | Description |
|---|---|
| Namespace name | The name of the namespace. The name must be 2 to 120 characters in length, and can contain lowercase letters, digits, underscores ( ), hyphens (-), and _ periods (.). It cannot start or end with an underscore ( ), hyphen (-), or period (.). _ |

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, find the namespace that you want to delete and click **Delete** in the
**Actions** column.
6. In the message that appears, click **OK**.

### Helm chart management

#### Overview of Helm charts

This topic introduces Helm charts.

**Context**

Kubernetes provides a unified API that you can call to define Kubernetes resources in YAML files. Kubernetes has defined a variety of resource types, such as Deployments, StatefulSets, and ConfigMaps. As the YAML-based software delivery system is constantly improved, the Cloud Native Computing Foundation (CNCF) community has developed charts and its implementation tool Helm to manage resources at a higher level. A chart is a collection of files that describe a related collection of Kubernetes resources. For example, a chart can be a collection of files that describe WordPress and MySQL resources or a collection of resource description files for an etcd cluster. Helm is a CLI tool used to manage charts and their releases.

#### Create a namespace

This topic describes how to create a namespace on a Container Registry Advanced Edition instance.

**Procedure**

1. 2. 3.
4. In the navigation pane, click **Helm Chart**.
5. On the **Namespace** tab, click **Create a namespace**.
6. On the **Create a namespace** page, configure parameters and click **Submit**.
By default, if you push an image to a repository that does not exist in a namespace, Container Registry automatically creates the repository based on the repository name that you specified. To disable this feature, turn off **Automatically create a repository** for the namespace. By default, a repository that is automatically created upon image push is **private**. You can set **Default repository type** to **Public** for a namespace to change the default repository type.

| Default repository type | Valid values: Public and Private. |
|---|---|
| Automatically create a repository | Specifies whether to automatically create a repository. |

| Parameter | Description |
|---|---|
| Warehouse name | The name of the chart repository. It must be 2 to 64 characters in length, and can contain lowercase letters, digits, underscores ( ), hyphens (-), periods (.), and forward slashes (/). It _ cannot start or end with an underscore ( ), hyphen (-), period (.), or forward slash (/). _ |

**What to do next**

You can click **Delete** in the **Operation** column of a namespace to delete the namespace.

**Important**

After a **namespace** is deleted, you can no longer access repositories in the namespace. Proceed with caution.

#### Delete a namespace

This topic describes how to delete a namespace on a Container Registry Advanced Edition instance.

**Usage notes**

After a namespace is deleted, you can no longer access the repositories in the namespace. Proceed with caution.

**Procedure**

1. 2. 3.
4. In the navigation pane, click **Helm Chart**.
5. On the **Namespace** tab, click **Delete** in the **Operation** column of the namespace you want to delete.
6. Confirm the information in the **Confirm** message and click **OK**.

#### Create a chart repository

This topic describes how to create a chart repository on a Container Registry Advanced Edition instance.

**Prerequisites**

A namespace is created. For more information, see Create a namespace.

**Procedure**

1. 2. 3.
4. In the navigation pane, click **Helm Chart**.
5. On the **Chart Warehouse** page, click the **chart warehouse** tab.
6. On the **chart warehouse** tab, click **Create a Chart repository**.
7. On the **Create a Chart repository** page, configure the following parameters and click **OK**.

| Namespace | The namespace to which the chart repository belongs. |
|---|---|
| Warehouse type | Valid values: Public and Private. |
| Description | The description of the chart repository. The description can be up to 2,000 characters in length. |

#### Manage chart repositories

This topic describes how to manage chart repositories on a Container Registry Advanced Edition instance.

**Query chart repositories**

1. 2. 3.
4. In the navigation pane, click **Helm Chart**.
5. On the **Chart Warehouse** page, click the **chart warehouse** tab.
6. On the **chart warehouse** tab, you can filter chart repositories by **namespace** or **repository name**.
7. The chart repository list displays the information of each chart repository, including **Warehouse**
**name/ID**, **Namespace**, **Warehouse type**, **Creation time**, and **Description**.

**Modify a chart repository**

**Note**

You cannot change the namespace of a chart repository.
1. On the **chart warehouse** tab, click **Editor** in the **Operation** column of a chart repository.
2. On the **Edit the Chart repository** page, modify **Warehouse name**, **Warehouse type**, and
**Description** and click **OK**.

**Delete a chart repository**

1. On the **chart warehouse** tab, click **Delete** in the **Operation** column of a chart repository.
2. Click **OK**.

**Manage a chart repository**

1. On the **chart warehouse** tab, click **Management** in the **Operation** column of a chart repository.
2. On the **Basic Information** tab, you can view the basic information and **Operating Instructions** of
the chart repository. The basic information includes **Mirror Name**, **Region**, **Description**, **Warehouse type**, and
**Warehouse URL**.
**Operating Instructions**: You can configure local repository mappings, push charts, and pull charts.
3. Click the **Chart Management** tab to upload, download, and delete charts.

**Upload a chart file:**

a. On the **Chart Management** tab, click **Upload**. b. On the **Upload Chart Repository** page, click the icon, select a local chart file, click **Open**, and then click **OK**.
**View the historical versions of a chart file** :
a. On the **Chart Management** tab, click **Version** in the Operation column of a chart. b. In the **Version** panel, you can view the historical version of the chart, including **Version**, **Size**, and **Update Time**. To download a chart version, click **Download** in the **Operation** column of the version and click
**OK**.
To delete a chart version, click **Delete** in the **Operation** column of the version and click **OK**.
**Delete a chart file**:

**Important**

After you delete a chart file, all versions of the chart file are deleted. Proceed with caution. a. On the **Chart Management** tab, click **Delete** in the Operation column of a chart. b. Click **OK**.

### Create an image repository

This topic describes how to create an image repository on a Container Registry Advanced Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, click **Create Image Repository**.
6. On the **Create Image Repository** page, configure the following parameters and click **Confirm**
**Order**.

| Parameter | Description |
|---|---|
| Organizatio n | The organization to which the namespace belongs. |
| Resource Set | The resource set to which the namespace belongs. |
| Region | The region in which the namespace resides. |
| Sharing Scope | The scope for which to share the image repository. Valid values:C urrent Resource Set, Current Organization and Subordinate Organizations, and Current Organization. |
| Namespace | The namespace to which the image repository belongs. |
| Repository Name | The name of the image repository. It must be 2 to 64 characters in length and can contain lowercase letters, digits, underscores ( ), hyphens (-), periods (.), and forward slashes (/). It _ cannot start or end with an underscore ( ), hyphen (-), period (.), or forward slash (/). _ |
| Repository Type | The type of the image repository. Valid values: Public and Private. |
| Image Version | Specifies whether to enable the image tag. If you turn on this switch, image tags other than the latest tag in the repository cannot be overwritten. This ensures the consistency of container image tags. |
| Digest | The digest of the repository. |
| Description | The description of the repository. The description can be up to 2,000 characters in length. |

**Note**

You can also click **Add Configuration Quotation** for later purchase.

### Manage image repositories

This topic describes how to manage image repositories in a Container Registry Advanced Edition instance.

**Modify the information of an image repository**

1. 2. 3. 4.
5. Optional. On the **Image Repository** page, select a namespace and enter a repository name keyword
to perform a fuzzy search.
6. On the **Image Repository** page, find the image repository that you want to manage and perform the
following operations in the **Operation** column:

| Parameter | Description |
|---|---|
| Repository Type | By default, users must log in to the corresponding Container Registry instance if they want to pull a public image. If you want public images to be pulled by anonymous users, turn on Allow Anonymous Users to Pull Public Artifacts for the instance. To pull a private image, you must obtain the pull operation permission and log in to the corresponding Container Registry instance. |
| Image Tag | If you select this check box, image tags other than the latest tag in the repository cannot be overwritten. This ensures the consistency of container image tags. |
| Accelerated Images | Image acceleration aims to enable on-demand loading of image data. It allows you to download and decompress only the data required for launching the container instead of pulling the entire image, which greatly accelerates application deployment and enhances elasticity. After you select this check box, each image that is pushed to the repository is automatically converted to an accelerated image. The time required to convert an image to an accelerated image depends on the size of the image. The conversion does not affect the base image. |
| Digest | The summary of the image repository. |
| Description | The description of the image repository. |

Click **Private** (available only for public repositories). In the message that appears, click **OK** to set the current repository as private. Click **Management**. On the **Basic Information** page, you can view the information on the following tabs:
**Image Instructions**: provides the information about how to log in to the instance, pull and push
images, add a tag to an image, and select an image repository.
**Chart Instructions**: provides the information about how to use a Helm 3 client to configure
environment variables, log in to an instance, save image tags, push and pull image tags, and export an image tag to a local directory.
**Instructions on OCI Artifacts**: provides the information about how to log in to an instance and
push and pull OCI artifacts.
**Image Description**: provides the description of the image.
On the **Basic Information** page, click **Edit**. In the **Modify Basic Information** dialog box, configure the following parameters and click **OK**. For more information, see Configure a trigger.

**Image Version**

1. In the left-side navigation pane of the **Basic Information** page, click **Image Version**.
You can view the following information about the images in the image repository: **Edition**, **Total**
**Image Size**, **Image Tag Status**, **Last Updated At**, **Digest**, **Image Size**, **Type**, and
**OS/Architecture**.
2. You can perform the following operations in the **Actions** column of an image tag:
Click **Image Replication**. In the **Select Destination Repository for Replication** dialog box, configure the **Synchronization Scenario**, **Destination Repository**, and **Overwrite Image** parameters. Then, click **OK**. For more information, see Replicate images between instances that belong to the same account. In this example, you can select a destination repository only in a Container Registry Advanced Edition instance across regions. Click the icon and click **Synchronization Records** to view the detailed replication records of the current image tag. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact Size**,
**Size of Replicated Image Layer**, and **Replication Status**. The layer details include **Layer**
**Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You can check
whether the tag has been replicated and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task. Click the icon and click **Delete**. In the dialog box that appears, select **Confirm to Delete Image**
**of This Tag** and click **OK**.
Click **Layer Information** and view the layer information, including the size and metadata for each layer of the image. Click **Upload Image** or **Download** to upload and download images. For more information, see Upload and download images.

**Image Synchronization**

1. In the left-side navigation pane of the **Basic Information** page, click **Image Synchronization**.
2. On the **Image Synchronization** page, you can perform the following operations:
Click **Create Copy Task**. In the **Select Destination Repository for Replication** dialog box, configure the **Image Tag to be Copied**, **Destination Repository**, and **Overwrite Image** parameters. Then, click **OK**. For more information, see Replicate images between instances that belong to the same account. Find the replication task that you want to view and click **Details** in the **Actions** column. You can view the path from the source to the destination and the replication status of the involved artifacts and layers, such as **Image Layer Digest**, **Image Size**, and **Replication Status**.

### Delete an image repository

This topic describes how to delete an image repository from a Container Registry Advanced Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, find the repository that you want to delete and click **Delete** in the
**Operation** column.
6. In the message that appears, click **OK**.

### Export image information

This topic describes how to export the summary information about the images in a Container Registry Advanced Edition instance.

**Limits**

Custom export fields are not supported. Only the images on which the permissions are granted to the current account can be exported.

**Procedure**

1. 2. 3.
4. On the **Image Repository** page, click the
icon in the upper-right corner of the image list.
5. In the **New Download Task** dialog box, confirm the download path and file name, and then click
**Download** to export the data as an Excel file.

**Note**

After the download is complete, you can view the exported file on your on-premises machine.

### Configure an access credential

You can configure an access credential to set a password that you use to log in to a Container Registry Advanced Edition instance. This method ensures that you can control the upload and download of container images. This topic describes how to configure an access credential.

**Prerequisites**

Only operations administrators, resource set administrators, and organization administrators can set fixed passwords. For other users, you must create a custom role, select **Reset the passwords of**
**Advanced Edition instances**, and assign the custom role to the user before the user can set a fixed
password. For more information, see Create a role and assign permissions.

**Background information**

Access credentials are independent of Apsara Stack accounts and passwords. Access credentials are available in two types: Password: A password is valid permanently. Keep it safe. If you forget your password, you can reset it. Temporary token: A temporary token is valid for one hour. If the temporary token is obtained by using Security Token Service (STS), the temporary token is valid so long as the STS token is valid.

**Procedure**

1. 2. 3. 4.
5. On the **Access Credential** page, click **Set a fixed password**.

**Note**

On the right side of **Fixed password**, you can view whether a password has been set. Password: A password is valid permanently. Keep it safe. If the password is lost, you can reset it.
6. In the **Set a fixed password** dialog box, configure the **Password** and **Confirm password**
parameters. Then, click **OK**.
7. **Optional.** For more information about how to set a temporary token, see **GetAuthorizationToken** of
**API Reference for Advanced Edition** in the **Container Registry Developer Guide**.

### Upload and download images

This topic describes how to upload an image to and download an image from a Container Registry Advanced Edition instance.

**Procedure**

**Method 1: Upload and download images by using the CLI**

1. Obtain the address of the image repository.
i. ii. iii. iv. v. On the **Image Repository** page, click the name of the image repository that you want to manage. On the **Basic Information** page, obtain the address of the image repository.
2. Run the following command to log in to the Container Registry Advanced Edition instance:

```bash
docker login --username=<Your Apsara Stack tenant account> <Address of the image repository>
```

As prompted in the command output, enter the password that you set when you activated Container Registry. If you forget your password, you can reset it. For information about how to reset a password, see Configure an access credential.
3. Upload and download an image.
Upload an image a. Run the following command to add a tag to the image:

```bash
docker tag <ID of the image> <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

b. Run the following command to upload the image to the image repository:

```bash
docker push <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

Download an image Run the following command to download an image from the image repository:

```bash
docker pull <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

**Method 2: Upload and download images by using the console**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. In the left-side navigation pane, click **Image Version**.
7. Upload and download an image.
Upload an image a. On the **Image Details** page, click **Upload Image**. b. In the **Upload Image** dialog box, specify **Tag**, click the icon, select the desired image file, click
**Open**, and then click **OK**.
Download an image a. On the **Image Details** page, click **Download** in the **Actions** column of the desired image.

| Parameter | Description |
|---|---|
| Name | Enter a name for the trigger. |
| Trigger URL | Enter the URL of the trigger that is created in Container Service for Kubernetes (ACK). |

b. In the **Confirm Download** message, read the information and click **OK**.

**Important**

Use this download feature only when you cannot use the standard Docker API to download images. This feature is not suitable for large-sized images. Do not use this feature to pull all images. Use the standard Docker API if possible. The download task is executed in the background. The validity period of the generated package is 24 hours. c. After the image package is generated, click **Download** in the **Download Info** column to download the package to your on-premises machine. d. In the **New Download Task** dialog box, click **Download**. After the package is downloaded, you can view it on the on-premises machine.

### Configure a trigger

Container Registry provides the trigger feature for image repositories. If you create a trigger for an image repository, a notification is pushed to you when an image is built. This facilitates the redeployment of images for applications. This topic describes how to configure a trigger.

**Security rules on trigger usage**

HTTP services: Port 80 is used by default. If you want to use another port, append the port number to the end of the trigger URL. You can use only the following port numbers: 80, 21, 443, 70, 210, 280, 488, 591, 777, and from 1025 to 65535. HTTPS services: Port 443 is used by default. Only port 443 is supported. If you want to use another port, use HTTP.

**Create a trigger**

**Note**

A trigger of a repository can subscribe to events generated by a new image. When a new image is generated, you can view the access records of the trigger, including the request time, request parameters, and request results. The request parameters provide information about the current repository. Before configuring a Container Service trigger, bind a repository trigger. For more information, see **Kubernetes clusters > Application management > Use application triggers** in **Alibaba Cloud Container Service for Kubernetes User Guide**. 1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. On the details page of the image repository, click **Trigger** in the left-side navigation pane.
7. On the **Trigger** page, click **Create**.
8. In the **Create Trigger** dialog box, set the parameters and click **OK**.

| Trigger Mode | Valid values: Trigger All, Expression-based Trigger, and Tag-based Trigger. Trigger All: Each time an image is built, an image pull is triggered. Expression-based Trigger: Tags are filtered based on a regular expression. An image pull is triggered only when a tag matches the regular expression. You can enter a simple regular expression. For example, if you enter release-v.* , an image pull is triggered only after an image with a tag that starts with release-v is built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. Tag-based Trigger: An image pull is triggered based on the specified tags. You can specify a maximum of 10 tags based on which an image pull needs to be triggered. Then, an image pull is triggered only when images with the specified tags are built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. |
|---|---|

**What to do next**

**View access records**

1. On the **Trigger** page, find the trigger that you want to manage and click **Access Log** in the **Actions**
column.
2. In the **Access Log** dialog box, you can view information such as **Access Status Code** and **Accessed**
**At**. Find the access log that you want to view and click **Details** in the **Actions** column. You can view
the details of the access log, including the request time, request parameters, and request results.

**Modify a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Modify** in the **Actions**
column.
2. In the **Modify Trigger** dialog box, modify the configuration of the trigger and click **OK**.

**Delete a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Delete** in the **Actions**
column.
2. In the **Are you sure you want to delete the repository** message, click **OK**.

### Replicate images between

**instances that belong to the same**

**account**

This topic describes how to manually and automatically replicate an image across regions between instances that belong to the same account.

**Automatically replicate images within the same account**

You can configure a replication rule to automate image replication between two instances that belong to the same account. After you upload an image to the source instance that resides in one region, the system automatically replicates the image to the destination instance that resides in the other region. 1. 2. 3. 4.
5. On the **Instance Synchronization** page, click **Create Rule**.

| Parameter | Description |
|---|---|
| Rule Name | The name of the custom rule. The name must be 1 to 128 characters in length. |
| Synchronization Scenario | You can select only Same Account. |
| Destination Instance | Select a region, an instance type, and an instance. |
| Synchronization Level | Valid values: Namespace: Images in all repositories in the specified namespace are synchronized. Repository: Only images in the specified repository are synchronized. |
| Source Namespace | Select an existing namespace. |
| Source Repository | Note This parameter is displayed only when Synchronization Level is set to Repository. Specify the name of the repository in which the images will be synchronized. |
| Tag Filter | Enter a regular expression to filter the tags of images in the repository. By default, all image tags are selected. |

6. In the **Create Rule** dialog box, configure the following parameters and click **Create**
**Synchronization Rule**.

**Important**

The destination instance must have a namespace same as that of the source namespace. If you set Synchronization Level to Repository, a repository with the same name must also exist. Otherwise, the rule fails to be created. Select a source instance and click **Detect** to check whether the destination instance meets the requirement. If the destination instance does not have the same namespace or repository, create them first. For more information, see Create a namespace and Create an image repository. When you upload an image to the source instance, the image is automatically replicated to the destination instance. In the left-side navigation pane of the management page of the Container Registry Advanced Edition instance, click **Synchronization Records**. If the status of the replication task on the
**Synchronization Records** page is Completed and the image exists in the destination instance, the
image is automatically replicated between the instances that belong to the same account. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact Size**,
**Size of Replicated Image Layer**, and **Replication Status**. The layer details include **Layer**
**Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You can check
whether the tag has been replicated and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task.

**Manually replicate images within the same account**

You can configure a replication rule to manually replicate an image from a source instance to a destination instance across regions.

**Method 1: On the Image Version page**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. On the details page of the image repository, click **Image Version** in the left-side navigation pane.
7. On the **Image Tag** page, find the image that you want to manage and click **Image Replication** in the
**Actions** column of the image.
8. In the **Select Destination Repository for Replication** dialog box, select **Same Account** for the
**Synchronization Scenario** parameter, specify the region, destination instance name, namespace,
image repository, and repository version, specify **Overwrite Image**, and then click **OK**. After you manually create the replication rule, image replication between the instances is immediately triggered. On the **Image Version** page, you can click the icon in the Actions column of the desired image and click **Synchronization Records**. On the **Synchronization Records** page, if the status of the replication task is **Replicated** and the image can be found in the destination instance, the image is manually replicated between the instances that belong to the same account. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact Size**,
**Size of Replicated Image Layer**, and **Replication Status**. The layer details include **Layer**
**Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You can check
whether the tag has been replicated and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task.

**Method 2: On the Image Synchronization page**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. On the details page of the image repository, click **Image Synchronization** in the left-side navigation
pane.
7. On the **Image Replication** page, click **Create Copy Task**.
8. In the **Select Destination Repository for Replication** dialog box, select a value for **Image Tag to**
**be Copied**, specify the region, product type, destination instance name, namespace, image
repository, and repository version, specify **Overwrite Image**, and then click **OK**. You can select a cross-region Advanced Edition instance. You can also select an instance in the same region but a different namespace. After you manually create the replication rule, image replication between the instances is immediately triggered. If the status of the replication task on the **Image Replication** page is **Replicated** and the image exists in the destination instance, the image is manually replicated between the instances that belong to the same account. Find the replication task that you want to view and click **Details** in the **Actions** column. You can view the path from the source to the destination and the replication status of the involved artifacts and layers, such as **Image Layer Digest**, **Image Size**, and **Replication Status**.

### Configure a repository to be

**immutable**

Container Registry allows you to configure a repository to be immutable to prevent image tags from being overwritten due to unintended operations. After you configure a repository to be immutable, the existing and newly added image tags in the repository cannot be overwritten except for the tags of the latest. After you push an image with a tag other than latest to the repository, you cannot push another image with the same tag to the repository. This ensures that the images in the repository are consistent with the images that have been deployed in containers. This topic describes how to configure a repository to be immutable.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, find the repository that you want to manage and click **Management**
in the **Operation** column.
6. On the Basic Information page, click **Edit**.
7. In the **Modify Basic Information** dialog box, select **Immutable** for **Image Tag** and click **OK**.

**Note**

To configure a repository to be mutable, clear **Immutable**.

**Verify the results**

1. Run the `docker push` command to push an image whose tag is not latest to a repository.

```bash
docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:v1
```

2. Push another image whose tag is the same as the tag of the image you pushed in Step 1.
The push request is denied. The following error is returned, which indicates that the image tag cannot be overwritten:

```
The requested tag already exists and cannot be overwritten.
```

3. Run the `docker push` command to push an image whose tag is latest to the repository.

```bash
docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:latest
```

4. Push another image whose tag is also latest. The tag is the same as the tag of the image that you
pushed in Step 3. The push is successful. The image overwrites the image that you pushed in Step 3.
5. Configure the repository to be mutable. For specific operations, see the preceding section.
6. Push another image whose tag is the same as the tag of the image you pushed in Step 1.
The push is successful. The image overwrites the image that is pushed in Step 1.

### Delete image tags

Container Registry allows you to delete multiple image tags of a Container Registry instance at a time. This topic describes how to delete multiple image tags at a time by configuring a tag retention policy.

| Parameter | Description |
|---|---|
| Cleaning range | Namespace: After you select a namespace, the retention policy applies to all image repositories in the namespace. Note You can enter a namespace keyword to search for namespaces. Warehouse: After you select a namespace and an image repository, the retention policy applies to the specified image repository in the namespace. Note You can enter a namespace keyword and a repository keyword to perform a quick search. |
| Execution method | Only Manual is supported. |
| Number of reserved images (Optional) | The number of recently pushed image tags that are retained. The number of retained images must be greater than 0 and less than or equal to the total number of current image tags. |
| Retain image version (optional) | In addition to the number of recently pushed images that you want to retain, you can specify the image tags that you want to retain. Note The default value of this parameter is an asterisk (*), which indicates that all image tags are retained in addition to the specified number of recently pushed images. |
| Last Pull Retention Days (optional) | The images that are recently pulled within the number of days specified by this parameter are retained. |
| Recent push retention days (optional) | The images that are recently pushed within the number of days specified by this parameter are retained. |

**Configure a tag retention policy**

After you configure a tag retention policy, the image tags that do not match the policy are deleted. 1. 2. 3. 4.
5. On the **Version Management** page, click **Create a retention policy**.
6. In the **Create a retention policy** dialog box, configure the following parameters and click **OK**.

**Manually trigger a tag deletion task**

1. On the **Version Management** page, find the retention policy that you want to apply and click
**Execute now** in the **Operation** column.
2. In the message that appears, click **OK**.

**View the task list**

1. In the **Task list** section of the **Version Management** page, view image tag deletion tasks and the
status of the tasks.
2. Find the task that you want to view and click **View** in the **Operation** column. In the panel that
appears, view the details of the task.

**Manage retention policies**

On the **Version Management** page, you can perform the following operations on a retention policy: Modify a retention policy: Find the retention policy that you want to modify, click **Modify** in the
**Operation** column, modify the settings of the retention policy, and then click **OK**.
Delete a retention policy: Find the retention policy that you want to delete and click **Delete** in the
**Operation** column. In the message that appears, click **OK**.

### Use the aliyun-acr-credential-

**helper component to pull images**

**without a secret**

You can use the aliyun-acr-credential-helper component to pull private images without using a secret from instances of Container Registry Standard Edition, Advanced Edition, and Multi-instance Edition. This component is automatically installed in Container Service for Kubernetes (ACK) clusters. This topic describes how to use the aliyun-acr-credential-helper component to pull a private image without using a secret in different scenarios.

**Prerequisites**

An ACK cluster is created. For more information, see **Create a Kubernetes cluster** in **Container**
**Service for Kubernetes User Guide**.
A kubectl client is connected to your cluster. For more information, see **Use kubectl to connect to a**
**Kubernetes cluster** in **Container Service for Kubernetes User Guide**.

**Usage notes**

If you want to use the aliyun-acr-credential-helper component, do not specify the imagePullSecret parameter. If the imagePullSecret parameter is specified in the template of a Kubernetes resource, such as a Deployment, the component becomes invalid. If a Kubernetes resource, such as a Deployment, uses a custom service account, you must modify the service-account parameter in the configuration file of the aliyun-acr-credential-helper component. This way, the component is authorized to pull images by using the custom service account. Check whether the private image that you want to pull resides in the same region as your ACK cluster. By default, you can pull private images only from Container Registry instances that reside in the same region as your ACK cluster. If you want to pull images from Container Registry instances that reside in different regions from your ACK cluster, see Scenario 2 in this topic. After you create a service account in a cluster, it takes some time for the aliyun-acr-credential-helper component to renew the token of the service account. The new token for pulling private images is generated based on the default permissions of your ACK cluster. Applications with the service account can use the token to pull images only after the token is renewed. If you create an application immediately after you create a service account, the application will fail to pull images because it is unauthorized. By default, the configuration of the aliyun-acr-credential-helper component overwrites the
**imagePullSecret** parameter of default service accounts in all namespaces. These service accounts
are automatically modified when the **service-account** parameter of the **acr-configuration** ConfigMap in the kube-system namespace is changed. When you modify the **acr-configuration** ConfigMap in the kube-system namespace, make sure that you use the same indentation as the example that is provided in this topic. We recommend that you paste the YAML code provided in this topic to the editor, replace the corresponding values, and apply the configuration. This ensures that the format of the ConfigMap is valid.

| Name of the acr- configuration ConfigMap | Description of the name | Value |
|---|---|---|
| service-account | The service accounts that are used by the aliyun-acr-credential-helper component to pull images. | Default value: default. Note Separate multiple service accounts with commas (,). Enter an asterisk (*) to specify all service accounts in all namespaces. |
| acr-registry-info | The information about Container Registry instances. Each instance can be specified by three fields of the String type in a YAML file. Note Configure the three fields based on the following descriptions: instanceId: the ID of the Container Registry instance. This field is required for Container Registry Enterprise Edition and Multi-instance Edition instances. domains: the domain names of the Container Registry instance. This parameter is optional. By default, all domain names of the instance are specified. You can specify one or more domain names. Separate multiple domain names with commas (,). | The value is empty by default. This means that images are pulled from the default repository of the Container Registry instance that resides in the same region as your ACK cluster. Sample configurations for a Container Registry Advanced Edition or Multi- instance Edition instance: - instanceId: "cri-xxx" domains: "xxx.com,yyy.com" Sample configurations for a Container Registry Standard Edition instance: - instanceId:"" domains: "xxx.com,yyy.com" |

**Update and configure the aliyun-acr-credential-helper component**

Before you use aliyun-acr-credential-helper to pull images, you may need to update and configure the component. To do so, perform the following steps: Configure the acr-configuration ConfigMap.

**Method 1: Configure the acr-configuration ConfigMap in the ACK console**

1. Log in to the ACK console. For more information, see **Log in to the ACK console** in the **Container**
**Service for Kubernetes User Guide**.
2. In the left-side navigation pane, click **Cluster**.
3. On the **Cluster List** page, click the name of the cluster that you want to view.
4. In the left-side navigation pane of the **Cluster Information** page, choose **Configuration**
**Management > Config Maps**.
5. In the upper part of the **ConfigMap** page, select **kube-system** from the Namespace drop-down list
and find the **acr-configuration** ConfigMap. Then, modify the acr-configuration ConfigMap by using one of the following methods: Method 1: Click **Edit** in the Actions column and modify the names and values of the **ConfigMap**. Method 2: Click **Edit YAML** in the Actions column and modify the names and values of the
**ConfigMap**.
The following table describes the names and values of the acr-configuration ConfigMap.

| watch-namespace | The namespaces from which images can be pulled without secrets. | Default value: default. Note If the value is set to all, images can be pulled from all namespaces without a secret. Separate multiple namespaces with commas (,). |
|---|---|---|
| expiring-threshold | The duration after which the cache token expires. | Default value: 15m. We recommend that you use the default value. |

**Method 2: Configure the acr-configuration ConfigMap by using kubectl**

1. Run the following command to open the editing page of the acr-configuration ConfigMap:

```bash
kubectl edit cm acr-configuration -n kube-system
```

2. Configure the parameters of the acr-configuration ConfigMap based on your requirements.
Sample configurations for Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition: Advanced Edition and Multi-instance Edition

```
apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"cri-xxx" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration
  namespace:kube-system
selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration namespace:kube-system selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration
```

**Scenario 1: Pull private images from Container Registry Advanced**

**Edition, Multi-instance Edition, and Standard Edition instances**

ACK allows you to pull private images from Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition instances at the same time, only from Container Registry Advanced Edition and Multi-instance Edition instances, or only from Container Registry Standard Edition instances. Modify the
**acr-configuration****ConfigMap** based on your business requirements. For more information, see Update
and configure the aliyun-acr-credential-helper component. Sample configurations: Pull private images from Container Registry Advanced Edition and Multi-instance Edition instances.

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

Pull private images from Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition instances.

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

### Sign container images

To prevent man-in-the-middle ((MITM)) attacks and the update and running of invalid images, Container Registry automatically signs images in specified namespaces. After an image is pushed to Container Registry, Container Registry automatically signs the image based on the matched signing rules. This ensures that your container images are trusted.

**Create asymmetric keys**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, click **Create Key**.
4. On the **Create Key Pair** page, select an organization from the **Organization** drop-down list. Then,
the **Resource Set** and **Region** parameters are automatically configured.
5. In the **Basic Configurations** section, configure the parameters that are described in the following
table.

| Paramete rs | Description | Example |
|---|---|---|
| Key Type | Symmetric CMKs: Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ | Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ |
| Key Purpose | ENCRYPT/DECRYPT: The CMK is used to encrypt and decrypt data. SIGN/VERIFY: The CMK is used to generate and verify a digital signature. | SIGN/VERIFY |

**Note**

The image signing feature is implemented based on asymmetric key algorithms. When you create the KMS key, select an EC or RSA key type and set the Purpose parameter to SIGN/VERIFY. Other parameters are configured based on your business.
6. Click **Confirm Order**.

**Authorize Container Registry to access KMS keys**

To allow Container Registry to read asymmetric keys within your account, configure a policy in Resource Access Management (RAM).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise > Permissions > Role Permissions**.
3. Click **Create Custom Role** page, click **Advanced Settings > Create RAM Role & Attach Policy** .
4. On the RAM Roles page, create a RAM role named AliyunContainerRegistryKMSRole.
i. **Basic Configurations**
**Role Name**: AliyunContainerRegistryKMSRole.
**Description**: custom.
**Sharing Scope**: global sharing.
Click **Next**. ii. **Custom policy configurations.** a. Click **Create Policy**. On the **Create Policy** page, set the following parameters:
**Policy Name** :AliyunContainerRegistryKMSRolePolicy
**Policy Content**:

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kms:*"
```

`],`

```json
      "Resource": "acs:kms:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "yundun-css:*"
```

`],`

```json
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

click **OK**. b. On the **Role Authorization** page, enter **AliyunContainerRegistryKMSRolePolicy** in the **Select**
**Policy** field.
c. Select the policy content and click **Next**. iii. **Trust Policy Configuration**
**Cloud services**: Select the **cr.aliyuncs.com** and click **Next**.
iv. **Policy preview** Click **Create** to create and authorize the AliyunContainerRegistryKMSRole role. If multiple organizations need to use image signature, repeat the following steps to create a RAM role for the target organizations.
1. In the top navigation bar, choose **Enterprise > Permissions > Role Authorization**.
2. On the **Role Authorization** page, enter AliyunContainerRegistryKMSRole in the search box, and then
click the name of the role.
3. On the **Role Name: AliyunContainerRegistryKMSRole** page, click **RAM Role**.
4. On the **RAM Roles** tab, click **+ Create**. In the search box, select the organization that you want to
create and click **OK**.

**Configure a witness and a signature verification policy**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Host Security > Container Security**.
3. In the left-side navigation pane, choose **run time Protection> Container Signature**. On the
Container Signature page, create a certifier and associate it with a KMS key for container image signing.

**Configure a signature rule for automatic image signing**

1. 2. 3.
4. On the instance management page, click **Image Signing** in the left-side navigation pane, and then
click **Create a signature rule**.
5. In the **Key Configuration** step, select the witness that you created in the Security Center console and
associate the witness with the KMS key. Then, click **Next**.
6. In the **Signature Configurations** step, configure parameters and click **Create Signing Rule**.

**Note**

A signature rule applies only to new images that are pushed to the specified namespace. Existing images are not signed based on the signature rule.
**Signing Algorithm**: **RSA_PSS_SHA_256** or **RSA_PKCS1_SHA_256** of the two available signing
algorithms.
**Signing Range**: Select the namespace that you want to automatically sign.
**Signature Type**:
**Default**: Image digests and tags are signed. The default mode is suitable for the signing of images
in the current instance.
**Simple**: Only image digests are signed. Image tags are not signed. The simple mode is suitable
for cross-instance image replication scenarios. The signatures of corresponding images are verified when image tags change.
**Trigger Type**: the mode in which image signing is triggered. The default value is Automatic Trigger,
indicating that image signing is automatically triggered for each image that is pushed to Container Registry.

**Image signature verification**

For more information about image signature verification, see **kritis-validation-hook** of **Kubernetes**
**Clusters > Components > Component overview** in the **ACK User Guide**.

**Usage note**

You can use kritis-validation-hook to automatically verify image signatures in ACK clusters. You can set a policy to block image deployment if image signatures fail the verification. We recommend that you use this method. You can also verify image signatures in Container Registry by using the signature verification feature of **KMS**.

| Parameter | Description |
|---|---|
| Organization | The organization to which the Multi-instance Edition instance belongs. |
| Resource Set | The resource set to which the Multi-instance Edition instance belongs. |
| Region | The region to which the Multi-instance Edition instance belongs. |
| Instance Name | The name of the Multi-instance Edition instance. The name must be 1 to 64 characters in length, and can contain lowercase letters, digits, underscores ( ), _ hyphens (-), and periods (.). It cannot start or end with an underscore ( ), a hyphen (-), or a period (.). _ |

## Container Registry Multi-

**instance Edition**

### Create an instance

Before you use Container Registry Multi-instance Edition, you must create a Container Registry Multiinstance Edition instance to manage and distribute your cloud-native assets.

**Prerequisites**

Container Registry Multi-instance Edition is assigned permissions on your Object Storage Service (OSS) bucket. For more information, see Use RAM to enable access to OSS buckets. 1. 2.
3. On the **Multi-instance Specification List** page, click **Create Instances**.
4. On the **Create Instance** page, set the following parameters and click **Submit**.
5. In the **Operation succeeded** message, click **OK**.

**Note**

You can follow the preceding steps to create multiple Multi-instance Edition instances in the same region based on your business requirements.

**View instances**

1. 2. 3.
4. On the instance overview page, view the following information.

**Instance information**

| Parameter | Description |
|---|---|
| Instance ID | The ID of the instance. Example: cri-priv**. |
| Billing Method | - |
| Instance Specification | Multi-instance Edition |
| Region | The region ID of the instance. Example: cn-qingdao-env***. |
| Expiration Date | - |
| Support for Concurrent Pulls | 500 nodes. |

| Parameter | Description |
|---|---|
| Warehouse | The number of repositories that you have created and the quota. Example: -/100000. |
| Namespace | The number of namespaces that you have created and the quota. Example: 0/1000. |
| OSS Bucket | - |
| OSS Bucket storage usage | - |

| Parameter | Description |
|---|---|
| Global synchronous acceleration | Cross-region automatic synchronization is supported. Synchronization rules can be configured for namespaces or repositories. |
| Trusted content | You can sign OCI artifacts such as container images and Helm charts. |
| Helm Chart | You can manage the full lifecycle of multi-version cloud-native artifacts such as Helm charts. |

| Parameter | Description |
|---|---|

**Warehouse information**

**Basic functions**

**Novice Guide**

| Access credentials | Configure access credentials. For more information, see Configure an access credential. |
|---|---|
| Namespace | Create namespaces. For more information, see Create a namespace. |
| Image Repository | Create image repositories. For more information, see Create an image repository. |

The **Instance settings** and **Component settings** modules are not available for the current version.

### Delete an instance

This topic describes how to delete a Container Registry Multi-instance Edition instance.

**Prerequisites**

All namespaces under the instance are deleted. For more information, see Delete a namespace.

**Procedure**

1. 2.
3. On the **Multi-instance Specification List** page, find the instance that you want to delete and click
**Delete** in the **Operation** column.
4. In the message that appears, click **OK**.

### Permission management

#### Create a user and a user group

You can create users and assign different roles to the users to meet different requirements for system access control as an administrator. This topic describes how to create a user and a user group.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Create an organization**

To create a user or a user group, you must create an organization in advance.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.

| Parameter | Description |
|---|---|
| User name | The Apsara Stack account name of the user. The name must be 3 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at signs (@). The name must start with a letter or a digit. _ |
| Display name | The display name of the user. The name must be 2 to 30 characters in length and can contain letters, digits, hyphens (-), underscores ( ), periods (.), and at _ signs (@). |
| Role | You must select resource user. Otherwise, you will be prompted that you have no permissions when you attempt to log on to the Apsara Uni-manager Management Console. |
| Organization | The organization to which the user belongs. |
| Logon policy | Select Default Policies. |
| Phone | The mobile phone number of the user. If you want to send text messages about the resource requests and usage to the mobile phone number, make sure that the specified mobile phone number is valid. Note If the mobile number of the user changes, update it on the system in a timely manner. |

4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Resources > Organizations**.
5. In the left-side organization tree of the **Organizations** page, click **root** and then click **Create**
**Organization** in the upper-right corner of the page.
6. In the **Add Organization** dialog box, specify a name for the organization and then click **OK**.
7. **Optional:** If the organization is created on multiple clouds, the **Synchronously Create Multi-cloud**
**Organization** check box is displayed after you click **OK**.
After you select **Synchronously Create Multi-cloud Organization**, select clouds on which the organization is synchronously created, and then click **OK**.

**Create a user group**

A role cannot be directly assigned to a user. You can assign a role to a user group. Then, users in the user group can obtain the permissions of the role.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. In the upper-left corner of the **User Groups** page, click **Create a user group**.
3. In the **Create a user group** dialog box, specify **User Group Name**, select the organization that you
created from the **Organization** drop-down list, and then click **OK**. You can create users based on your business requirements.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > Users**.
2. On the **Users** page, click the **System Users** tab, and then click **Create a user**.
3. In the **Create a user** dialog box, configure the basic information of the user and then click **OK**.

| Landline | The landline number of the user. The landline number must be 4 to 20 characters in length and can contain only digits and hyphens (-). |
|---|---|
| Email | The email address of the user. If you want to send emails about the resource requests and usage to the email address, make sure that the specified email address is valid. Note If the email address changes, update it on the system in a timely manner. |
| DingTalk Key | The key of the chatbot for the DingTalk group to which the user belongs. For more information about how to configure the key, see DingTalk development documentation. |
| Notify User by Email | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by email whenever an alert is generated. Note You must configure an email server to receive emails. For more information, contact on-site O&M engineers. |
| Notify User by DingTalk | After this option is selected, the Apsara Uni-manager Management Console informs the user configured as the alert contact by DingTalk whenever an alert is generated. |

**Add the user to the user group**

After a user is added to a user group, the user has the permissions of the role that is assigned to the user group.
1. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Users > User Groups**.
2. On the **User Groups** page, find the user group to which you want to add the user and click **Add User**
in the **Actions** column.
3. In the **Add User** dialog box, select the user under the organization, click the
icon, and then click
**OK**.

#### Create a role and grant permissions to the

**role**

Container Registry adopts the authentication system that consists of Alibaba Cloud account and RAM users. You can create a custom role, attach a permission policy to the role, and assign the role to a user to grant the permissions of the role to the user. This topic describes how to create a role, assign the role to a user group, and attach a permission policy to the role.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Log on to the Apsara Uni-manager Management Console by using an Alibaba Cloud account.
Obtain the username and password that you can use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log In**.
4. In the top navigation bar, click Enterprise. In the left-side navigation pane of the Enterprise page,
choose **Permissions > Role Permissions**.
5. In the upper-left corner of the **Role Permissions** page, click **Create Custom Role**.
6.
7. **Optional:**
i. ii. Create a user group Add a user to a user group
8. i.

|  | Repository access control |
|---|---|

ii.

#### Enable access control for a repository

You can create users and grant different permissions to the users. This way, you can control the access of the users to Container Registry resources. This topic describes how to configure access control for repositories in different scenarios.

**Background information**

For the level-1 to level-5 organizations created in the Apsara Uni-manager Management console, the subordinate organizations do not have independent accounts and passwords, but the users within the subordinate organizations have their own accounts and passwords, which are independent of each other. After you run the `docker login` command to log in to an image repository, you can view only the images uploaded and downloaded by your organization. Namespaces are isolated between different organizations (regardless of the levels), and image resources among organizations are invisible to each other. Users can obtain access to an image repository if you grant them permissions.

**Usage notes**

When you authorize a user, pay attention to the following instructions to make sure that you do not grant excessive permissions to the user. You can grant a user the AdministratorAccess permission that contains management permissions on all Apsara Stack resources. In this case, the user has all permissions on Container Registry, regardless of whether the user is granted permissions before.

**System policies**

AliyunContainerRegistryFullAccess This policy grants a user the same permissions on image resources as those of an Apsara Stack account. The user can perform all operations on image resources.

```json
{
  "Statement": [
    {
      "Action": "cr:*",
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

AliyunContainerRegistryReadOnlyAccess This policy grants a user the read-only permission on all image resources. For example, the user can view the repository list and pull images.

```json
{
  "Statement": [
    {
      "Action": [
        "cr:Get*",
        "cr:List*",
        "cr:Pull*"
```

`],`

```json
      "Effect": "Allow",
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

**Policies for typical scenarios**

Grant the user the read and write permissions on a namespace of a Container Registry Multi-instance Edition instance.

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
    },
    {
      "Action": [
        "cr:*"
```

`],`

```json
      "Effect": "Allow",
```

```json
      "Resource": [
        "acs:cr:*:*:repository/$instanceid/$namespace/*",
        "acs:cr:*:*:repository/$instanceid/$namespace"
```

]

```json
    },
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cr:ListInstance*",
        "cr:GetInstance*",
        "cr:ListSignature*"
```

`],`

```json
      "Resource": "*"
    },
    {
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

]

```json
    },
    {
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

]

```
    }
```

`],`

```json
  "Version": "1"
}
```

**Authentication rules of Container Registry**

ARN format The following table describes the Alibaba Cloud Resource Name (ARN) format in an authorization policy when you use RAM to authorize access to the resources.

| Resource type | ARN format |
|---|---|
| * | acs:cr:$regionid:$accountid:* |
| instance | acs:cr:$regionid:$accountid:instance/$instanceid |
| repository | acs:cr:$regionid:$accountid:repository/$instanceid/* acs:cr:$regionid:$accountid:repository/$instanceid acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/* acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename/$repositoryname acs:cr:$regionid:$accountid:repository/$instanceid/$na mespacename |

| Parameter | Description |
|---|---|
| regionid | The region ID, which can be replaced by an asterisk (*). |
| accountid | The ID of the Apsara Stack account, which can be replaced by an asterisk (*). |
| instanceid | The ID of the Container Registry Multi-instance Edition instance. |
| namespacename | The namespace name. |
| repositoryname | The name of the image repository. |

| API | Action | Resource |
|---|---|---|
| Queries a pair of temporary username and password that is used to log on to a Container Registry instance | cr:GetAuthorizationToken | * |

The following table describes the parameters in the ARN format. Authentication rules When you access the Container Registry API as a RAM user or by using Security Token Service (STS), Container Registry checks whether you have obtained the required permissions. The permissions that Container Registry checks vary based on the resources that are requested by the API operation and the syntax of the API operation. The following table describes the authentication rules of different API operations.

**Note**

The asterisk (*) is used as a wildcard.

| Queries a namespace | cr:GetNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
|---|---|---|
| Create a namespace | cr:CreateNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Queries namespaces | cr:ListNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/* |
| Deletes a namespace | cr:DeleteNamespace | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename |
| Updates a namespace | cr:UpdateNamespace | acs:cr:$regionid:$accountid:chart/$ instanceid/$chartnamespacename |
| Queries a repository | cr:GetRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image repositories | cr:ListRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ * |
| Deletes an image repository | cr:DeleteRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Updates an image repository | cr:UpdateRepository | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries image tags in an image repository | cr:ListRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Deletes an image from an image repository | cr:DeleteRepositoryTag | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries the information about image layers of an image tag | cr:GetRepositoryLayers | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Queries the manifest information of an image tag | cr:GetRepositoryManifest | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |
| Updates a trigger for an image repository | cr:UpdateWebHook | acs:cr:$regionid:$accountid:reposit ory/$instanceid/$namespacename/ $repositoryname |

| Parameter | Description |
|---|---|
| Service Name | Select Container Registry. After you select a service, the permissions of the service-linked role are displayed. |
| Authorizing Organization Name | Select the organizations that you want to authorize. You can select one or more organizations. |

| Policy | Description |
|---|---|
| AliyunContainerRegistryDefaultRole | Aliyun Container Registry Default Role |

#### Use RAM to enable access to OSS buckets

Container Registry Multi-instance Edition hosts container images in Object Storage Service (OSS) buckets. You need to authorize Container Registry Multi-instance Edition to access OSS buckets.

**Create a service-linked role**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the **Service-linked Roles** page, click **Create Service-linked Role**, configure the parameters,
and then click **OK**. The following table describes the parameters. Permissions of the service role:

**View the details of a service-linked role**

1. On the **Service-linked Roles** page, set the **Role Name** parameter to
`AliyunContainerRegistryDefaultRole` , configure the **Organization Name**, and then the **Service**
**Name** parameters.
2. Find the RAM role that you want to manage and click **View Details** in the **Actions** column to go to the
details page of the RAM role.
3. On the **Service-linked Role Details** page, view the details and policy of the RAM role.
Click the **Role Details** tab to view the name, creation time, description, and trust policy of the RAM role. Click the **Role Policy** tab to view the policy information, including the policy name, policy type, default version, description, and time when the policy is attached to the RAM role. You can click **View Details** in the **Actions** column to view the policy details.

**Trust policies**

Trust policies allow Container Registry to access OSS buckets by assuming this service-linked role.

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "cr.aliyuncs.com"
```

]

```
      }
    }
```

]

```
}
```

**RAM policies**

The policy of the RAM role grants Container Registry Multi-instance Edition management permissions on the specified OSS bucket.

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": [
        "oss:GetObject",
        "oss:PutObject",
        "oss:DeleteObject",
        "oss:ListParts",
        "oss:AbortMultipartUpload",
        "oss:InitiateMultipartUpload",
        "oss:CompleteMultipartUpload",
        "oss:DeleteMultipleObjects",
        "oss:ListMultipartUploads",
        "oss:ListObjects",
        "oss:DeleteObjectVersion",
        "oss:GetObjectVersion",
        "oss:ListObjectVersions"
```

`],`

```json
      "Resource": [
        "acs:oss:*:*:cri-*",
        "acs:oss:*:*:cri-*/*"
```

`],`

```json
      "Effect": "Allow",
      "Condition": {}
    },
    {
      "Action": [
        "oss:PutBucket",
        "oss:GetBucket",
        "oss:ListBuckets",
        "oss:GetBucketLocation",
        "oss:PutBucketEncryption",
        "oss:GetBucketEncryption",
        "oss:PutBucketAcl",
        "oss:GetBucketAcl",
        "oss:PutBucketLogging",
        "oss:GetBucketLogging",
        "oss:PutBucketReferer",
        "oss:GetBucketReferer",
```

```
        "oss:PutBucketVersioning",
        "oss:GetBucketVersioning",
        "oss:PutBucketLifecycle",
        "oss:GetBucketLifecycle",
        "oss:DeleteBucketLifecycle",
        "oss:GetBucketTransferAcceleration"
```

`],`

```json
      "Resource": [
        "acs:oss:*:*:cri-*"
```

`],`

```json
      "Effect": "Allow",
      "Condition": {}
    },
    {
      "Action": [
        "vpc:DescribeVpcs"
```

`],`

```json
      "Resource": "acs:vpc:*:*:vpc/*",
      "Effect": "Allow",
      "Condition": {}
    },
    {
      "Action": [
        "cms:QueryMetricLast",
        "cms:QueryMetricList"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow",
      "Condition": {}
    }
```

]

```
}
```

### Quota management

#### Configure quotas

This topic describes how to allocate resource quotas for a Container Registry Multi-instance Edition instance in an organization or resource set.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console as a platform administrator.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Resource Pool Configuration**.
4. In the upper-left corner of the Resource Pool Configuration page, select a cloud platform, region ID,
and zone.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments. If you select All Zones, you can manage quotas in the region. If you select a zone, you can manage quotas in the zone, and the console displays only cloud services in the current zone.
5. Click **Container Registry Advanced Edition**. In the **Resource Pool Details** panel, you can view the
details of the Container Registry Advanced Edition instance, including **Resource Items**, **Logical**
**Inventory**, **Physical Inventory**, and **Total Activated Resources**.
6. In the **Resource Pool Details** panel, click **Configure Quota** in the lower part.
7. In the **Configure Quota** dialog box, add or remove quota items. For more information about quotas,
see Quota description.

**Note**

After you select a zone on the Resource Pool Configuration page, the **Synchronously Modify**
**Quotas in Other Zones** option appears in the Configure Quota dialog box. You can select this
option to synchronize the quota item configurations in this zone to other zones.
**Add quota items**: In the **Available Quotas** list, select the quota items that you want to add and
click the icon to add the quota items to the **Selected Quota Items** list.
**Remove quota items**: In the **Selected Quota Items** list, select the quota items that you want to
remove and click the icon to remove the quota items.
8. Click **OK**.
9. In the **Resource Pool Details** panel, click **Create Inventory** in the lower part of the page, set a
quota for the resource, and then click **Save**.

**Step 2: Allocate quotas**

1. Log in to the Apsara Uni-manager Management Console as an operations administrator or an
organization administrator.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quotas**.
4. In the upper-left corner of the **Quotas** page, select a cloud platform from the Cloud Platform drop-
down list.

**Note**

The Cloud Platform drop-down list is displayed only in multi-cloud environments.
5. On the right side of the product, set Region, Region, and Zone.
6. In the left-side organizational structure of the Quotas page, select the organization or resource set
whose resources you want to manage.
7. Click **Container Registry Advanced Edition** to go to the **Quota Details** panel and view the quota
details in the organization or resource set.
8. In the **Quota Details** panel, click **Set Quota**, configure the parameters, and then click **Save**.

#### Create a quota alert rule

This topic describes how to create an alert rule for a quota of Container Registry Multi-instance Edition in an organization or resource set. When the quota of an organization or a resource set reaches the preset threshold, the system notifies the administrator of the organization or resource set once per day. The system sends a notification when the quota alert is triggered for the first time every day.

**Prerequisites**

A quota is configured. For more information, see Configure a quota. You are assigned the operations administrator or organization administrator role. If you are assigned a custom role, the custom role must be granted the permissions to manage quotas and access the
**Quotas > Quotas** menu.

**Limits**

| Parameter |  | Description |
|---|---|---|
| Alert Rule Information | Cloud Platform | The cloud platform on which the alert rule takes effect. Note The Cloud Platform parameter is displayed only in multi-cloud scenarios. |
|  | Organization/ Resource Set | The organization or resource set for which the alert rule takes effect. |
|  | Include Child Organization | Specifies whether to apply the alert rule to the subordinate organizations and resource sets of the current organization. If you turn on Include Child Organization, the alert rule is applied to the current organization and all the subordinate organizations and resource sets of the current organization. This parameter is displayed only if you select an organization from the Organization/Resource Set drop-down list. : turns on Include Child Organization. : turns off Include Child Organization. |
|  | Region | The region in which the alert rule takes effect. |
|  | Cloud Service | Select Container Registry Advanced Edition. |
| Alert Information | Alert Rule Name | The name of the alert rule. |
|  | Alert Type | The criteria based on which an alert is generated. Valid values:U sed Amount: An alert is generated when the used quota exceeds the configured alert threshold. Remaining Available Quota: An alert is generated when the available quota is less than the configured alert threshold. |

If a quota alert rule other than the preset one is enabled for a cloud service in an organization or a resource set, no more quota alert rules can be created for the cloud service in the organization or resource set. A quota alert rule automatically takes effect after it is created. Then, the preset quota alert rule applied to the organizations or resource sets to which the new quota alert rule applies is disabled.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Operations** > **Resource Operations**.
3. In the left-side navigation pane, choose **Quotas** > **Quota Alerts**.
4. On the **Quota Alerts** page, click **Create Alert Rule**.
5. In the **Create Alert Rule** dialog box, configure the parameters that are described in the following
table.

|  | Alert Threshold | Resource Type: the resource item of the cloud service specified in the Alert Rule Information section by default. Used Amount/Quota: the used amount and the quota configured for the cloud service in the organization or resource set by default. Threshold: Valid values: No, Percentage, and Number. Alert Threshold: the threshold based on which the alert rule is triggered. If the amount of used resources exceeds the alert threshold or the amount of remaining available resources is less than the alert threshold, an alert is generated. If you set the Threshold parameter to No, the Alert Threshold parameter is set toN o Alerts by default. |
|---|---|---|

| Quota | Description |
|---|---|
| Apsara Stack Multi-instance Quota (Units) | The number of Container Registry Multi-instance Edition instances that can be created. |

6. Click **OK**.

#### Quota overview

This topic describes the quotas that you can configure for Container Registry Multi-instance Edition, calculation methods of quota usage, and inventory source.

**Calculation methods of quota usage**

Usage of Apsara Stack Multi-instance Edition instance quota (units) = Number of Container Registry Multi-instance Edition instances that have been used

**Note**

The quota usage is calculated based on the number of resource instances.

**Inventory source**

No inventory is involved. By default, the inventory is unlimited.

### Create a namespace

This topic describes how to create a namespace on a Container Registry Multi-instance Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, click **Create Namespace**.
6. On the **Create Namespace** page, configure the Namespace, Auto Create, and Default Repository
Type parameters, and then click **Confirm Order**. The following table describes the parameters.

**Note**

You can also click **Add Configuration Quotation** to place the order later.

| Parameter | Description |
|---|---|
| Organization | The organization to which the namespace belongs. |
| Resource Set | The resource set to which the namespace belongs. |
| Region | The region in which the namespace resides. |
| Instance Name | The name of the instance is automatically populated. |
| Namespace | The name of the namespace. The name must be 2 to 120 characters in length, and can contain lowercase letters, digits, underscores ( ), hyphens (-), and _ periods (.). It cannot start or end with an underscore ( ), a hyphen (-), or a period (.). _ |
| Auto Create | Specifies whether the system automatically creates a repository. |
| Default Repository Type | The type of the image repository. Valid values: Public and Private. |

By default, if you push an image to a repository that does not exist in a namespace, Container Registry automatically creates the repository based on the repository name that you specify. To disable this feature, turn off Auto Create for the namespace. By default, a repository that is automatically created upon image push is private. To allow the automatically created repositories to be public, set the Default Repository Type parameter to Public.

### Batch modify the accessibility of

**images**

The system allows you to modify the types of existing images and new images. This topic describes how to change the types of all images in the same namespace.

**Procedure**

1. 2. 3. 4.
5. In the namespace list, click **Public** or **Private** in the **Default Repository Type** column.

**Note**

If the **Automatically Create Repository** feature is disabled, you must enable the **Automatically**
**Create Repository** feature before you can set the **Default Repository Type** parameter.
6. In the dialog box that appears, select **Inventory and new images are modified** or **Add only**
**Image modifications** based on your business requirements, and then click **OK**.

| Parameter | Description |
|---|---|
| Organizatio n | The organization to which the image repository belongs. |
| Resource Set | The resource set to which the image repository belongs. |
| Region | The region in which the image repository resides. |
| Namespace | The namespace to which the image repository belongs. |
| Repository Name | The name of the image repository. It must be 2 to 64 characters in length and can contain lowercase letters, digits, underscores ( ), hyphens (-), periods (.), and forward slashes (/). It _ cannot start or end with an underscore ( ), hyphen (-), period (.), or forward slash (/). _ |
| Repository Type | The type of the image repository. Valid values: Public and Private. |

### Delete a namespace

This topic describes how to delete a namespace from a Container Registry Multi-instance Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Namespace** page, find the namespace that you want to delete and click **Delete** in the
**Actions** column.
6. In the message that appears, click **OK**.

### Create an image repository

This topic describes how to create an image repository in a Container Registry Multi-instance Edition instance.

**Procedure**

1. 2. 3. 4.
5. On the **Create Image Repository** page, configure the following parameters and then click **Confirm**
**Order**.

**Note**

You can also click **Add Configuration Quotation** for later purchase.

| Image Version | Specifies whether to enable the image tag. If you turn on this switch, image tags other than the latest tag in the repository cannot be overwritten. This ensures the consistency of container image tags. |
|---|---|
| Digest | The digest of the image repository. |
| Description | The description of the image repository. The description can be up to 2,000 characters in length. |

| Parameter | Description |
|---|---|
| Repository Type | By default, users must log in to the corresponding Container Registry instance if they want to pull a public image. If you want public images to be pulled by anonymous users, turn on Allow Anonymous Users to Pull Public Artifacts for the instance. To pull a private image, you must obtain the pull operation permission and log in to the corresponding Container Registry instance. |
| Image Tag | If you select this check box, image tags other than the latest tag in the repository cannot be overwritten. This ensures the consistency of container image tags. |

### Manage image repositories

This topic describes how to manage image repositories in a Container Registry Multi-instance Edition instance.

**Modify the information of an image repository**

1. 2. 3. 4.
5. Optional. On the **Image Repository** page, select a namespace and enter a repository name keyword
to perform a fuzzy search.
6. On the **Image Repository** page, find the image repository that you want to manage and perform the
following operations in the **Operation** column: Click **Private** (available only for public repositories). In the message that appears, click **OK** to set the current repository as private. Click **Management**. On the **Basic Information** page, you can view the information on the following tabs:
**Image Instructions**: provides the information about how to log in to the instance, pull and push
images, add a tag to an image, and select an image repository.
**Chart Instructions**: provides the information about how to use a Helm 3 client to configure
environment variables, log in to an instance, save image tags, push and pull image tags, and export an image tag to a local directory.
**Instructions on OCI Artifacts**: provides the information about how to log in to an instance and
push and pull OCI artifacts.
**Image Description**: provides the description of the image.
On the **Basic Information** page, click **Edit**. In the **Modify Basic Information** dialog box, configure the following parameters and click **OK**.

| Accelerated Images | Image acceleration aims to enable on-demand loading of image data. It allows you to download and decompress only the data required for launching the container instead of pulling the entire image, which greatly accelerates application deployment and enhances elasticity. After you select this check box, each image that is pushed to the repository is automatically converted to an accelerated image. The time required to convert an image to an accelerated image depends on the size of the image. The conversion does not affect the base image. |
|---|---|
| Digest | The summary of the image repository. |
| Description | The description of the image repository. |

For more information, see Configure a trigger.

**Image Version**

1. In the left-side navigation pane of the **Basic Information** page, click **Image Version**.
You can view the following information about the images in the image repository: **Edition**, **Total**
**Image Size**, **Image Tag Status**, **Last Updated At**, **Digest**, **Image Size**, **Type**, and
**OS/Architecture**.
2. You can perform the following operations in the **Actions** column of an image tag:
Click **Image Replication**. In the **Select Destination Repository for Replication** dialog box, configure the **Synchronization Scenario**, **Destination Repository**, and **Overwrite Image** parameters. Then, click **OK**. For more information, see Replicate images between instances that belong to the same account. Click the icon and click **Synchronization Records** to view the detailed replication records of the current image tag. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact Size**,
**Size of Replicated Image Layer**, and **Replication Status**. The layer details include **Layer**
**Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You can check
whether the tag has been synchronized and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task. Click the icon and click **Delete**. In the dialog box that appears, select **Confirm to Delete Image**
**of This Tag** and click **OK**.
Click **Layer Information** and view the layer information, including the size and metadata for each layer of the image. Click **Upload Image** or **Download** to upload and download images. For more information, see Upload and download images.

**Image Synchronization**

1. In the left-side navigation pane of the **Basic Information** page, click **Image Synchronization**.
2. On the **Image Synchronization** page, you can perform the following operations:
Click **Create Copy Task**. In the **Select Destination Repository for Replication** dialog box, configure the **Image Tag to be Copied**, **Destination Repository**, and **Overwrite Image** parameters. Then, click **OK**. For more information, see Replicate images between instances that belong to the same account. Find the replication task that you want to view and click **Details** in the **Actions** column. You can view the path from the source to the destination and the replication status of the involved artifacts and layers, such as **Image Layer Digest**, **Image Size**, and **Replication Status**.

### Export image information

This topic describes how to export the summary information about images in an instance of Container Registry Multi-instance Edition.

**Limits**

Custom export fields are not supported. Only the images on which the permissions are granted to the current account can be exported.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, click the
icon in the upper-right corner of the image list.
6. In the **New Download Task** dialog box, confirm the download path and file name, and then click
**Download** to export the data as an Excel file.

**Note**

After the download is complete, you can view the exported file on your on-premises machine.

### Configure an access credential

You can configure an access credential to set a password that you use to log in to a Container Registry Multi-instance Edition instance. This method ensures that you securely control the upload and download of container images. This topic describes how to configure an access credential.

**Prerequisites**

Only operations administrators, resource set administrators, and organization administrators can set fixed passwords. For other users, you must create a custom role, select **Reset the passwords of**
**Advanced Edition instances**, and assign the custom role to the user before the user can set a fixed
password. For more information, see Create a role and assign permissions.

**Background information**

Access credentials are independent of Apsara Stack accounts and passwords. Access credentials are available in two types: Password: A password is valid permanently. Keep it safe. If you forget your password, you can reset it. Temporary token: A temporary token is valid for one hour. If the temporary token is obtained by using Security Token Service (STS), the temporary token is valid so long as the STS token is valid.

**Procedure**

1. 2. 3. 4.
5. On the **Access Credential** page, click **Set a fixed password**.

**Note**

On the right side of **Fixed password**, you can view whether a password has been set. Password: A password is valid permanently. Keep it safe. If the password is lost, you can reset it.
6. In the **Set a fixed password** dialog box, configure the **Password** and **Confirm password**
parameters. Then, click **OK**.
7. **Optional.** For more information about how to set a temporary token, see **GetAuthorizationToken** of
**API Reference for Advanced Edition** in the **Container Registry Developer Guide**.

### Configure access control policies

You can configure access control policies to enable access to Container Registry domain names over the Internet. By configuring a public IP address whitelist, you can restrict only specified clients to access your image repositories over the Internet. This improves security. This topic describes how to configure access control policies.

**Prerequisites**

An instance is created. For more information, see Create an instance.

**Procedure**

1. 2. 3. 4.
5. On the **Access control** page, turn on **Access Entrance**.

**Note**

If **Access Entrance** is turned off, Internet access is disabled.
6. In the message that appears, click **OK**.

**Note**

After access control is enabled, a whitelist is added by default. Only the IP addresses in the whitelist can access Container Registry domain names.
7. Click **Add public whitelist**. In the dialog box that appears, enter the CIDR block that is allowed to
access Container Registry domain names and the remarks, and then click **OK**.

**Note**

You can click **Delete** in the Operation column to remove the public IP address whitelist.

**Verify the result**

1. On the **Access control** page, obtain the domain name address.
2.
3. On the **Image Repository** page, find the image repository that you want to manage and click
**Management** in the Operation column.
4. Refer to the step descriptions on the **Image Instructions** tab of the **Basic Information** page. Log in
to a public IP address in the public IP address whitelist. Then, upload and download an image. For more information, see Upload and download images. A successful image upload or download indicates that the public IP address whitelist is successfully configured.

**Note**

Replace <Repository address> in the command with the domain name obtained in Step 1.

### Upload and download images

This topic describes how to upload an image to and download an image from a Container Registry Multiinstance Edition instance.

**Procedure**

**Method 1: Upload and download images by using the CLI**

1. Obtain the address of the image repository.
i. ii. iii. iv. v. On the **Image Repository** page, click the name of the image repository that you want to manage. On the **Basic Information** page, obtain the address of the image repository.
2. Run the following command to log in to the Container Registry Multi-instance Edition instance:

```bash
docker login --username=<Your Apsara Stack tenant account> <Address of the image repository>
```

As prompted in the command output, enter the password that you set when you activated Container Registry. If you forget your password, you can reset it. For information about how to reset a password, see Configure an access credential.
3. Upload and download an image.
Upload an image a. Run the following command to add a tag to the image:

```bash
docker tag <ID of the image> <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

b. Run the following command to upload the image to the image repository:

```bash
docker push <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

Download an image Run the following command to download an image from the image repository:

```bash
docker pull <Address of the image repository>/<Name of the namespace>/<Name of the image repository>:<Version number of the image>
```

**Method 2: Upload and download images by using the console**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. In the left-side navigation pane, click **Image Version**.
7. Upload and download an image.
Upload an image a. On the **Image Details** page, click **Upload Image**.

| Parameter | Description |
|---|---|

b. In the **Upload Image** dialog box, specify **Tag**, click the icon, select the desired image file, click
**Open**, and then click **OK**.
Download an image a. On the **Image Details** page, click **Download** in the **Actions** column of the desired image. b. In the **Confirm Download** message, read the information and click **OK**.

**Important**

Use this download feature only when you cannot use the standard Docker API to download images. This feature is not suitable for large-sized images. Do not use this feature to pull all images. Use the standard Docker API if possible. The download task is executed in the background. The validity period of the generated package is 24 hours. c. After the image package is generated, click **Download** in the **Download Info** column to download the package to your on-premises machine. d. In the **New Download Task** dialog box, click **Download**. After the package is downloaded, you can view it on the on-premises machine.

### Configure a trigger

Container Registry provides the trigger feature for image repositories. If you create a trigger for an image repository, a notification is pushed to you when an image is built. This facilitates the redeployment of images for applications. This topic describes how to configure a trigger.

**Security rules on trigger usage**

HTTP services: Port 80 is used by default. If you want to use another port, append the port number to the end of the trigger URL. You can use only the following port numbers: 80, 21, 443, 70, 210, 280, 488, 591, 777, and from 1025 to 65535. HTTPS services: Port 443 is used by default. Only port 443 is supported. If you want to use another port, use HTTP.

**Create a trigger**

**Note**

A trigger of a repository can subscribe to events generated by a new image. When a new image is generated, you can view the access records of the trigger, including the request time, request parameters, and request results. The request parameters provide information about the current repository. Before you create a trigger in Container Service for Kubernetes (ACK), bind a repository trigger. For more information, see **Kubernetes clusters > Application management > Use**
**application triggers** in **Alibaba Cloud Container Service for Kubernetes User Guide**.
1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to view.
6. On the details page of the image repository, click **Trigger** in the left-side navigation pane.
7. On the **Trigger** page, click **Create**.
8. In the **Create Trigger** dialog box, configure the parameters and click **OK**.

| Name | The name of the trigger. |
|---|---|
| Trigger URL | The URL of the trigger that is created in ACK. |
| Trigger Mode | Valid values: Trigger All, Expression-based Trigger, and Tag-based Trigger. Trigger All: Each time an image is built, an image pull is triggered. Expression-based Trigger: Tags are filtered based on a regular expression. An image pull is triggered only when a tag matches the regular expression. You can enter a simple regular expression. For example, if you enter release-v.* , an image pull is triggered only after an image with a tag that starts with release-v is built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. Tag-based Trigger: An image pull is triggered based on the specified tags. You can specify a maximum of 10 tags based on which an image pull needs to be triggered. Then, an image pull is triggered only when images with the specified tags are built. Otherwise, no image pull is triggered and the access status code in the access log is Untriggered. |

**Related operations**

**View access records**

1. On the **Trigger** page, find the trigger that you want to manage and click **Access Log** in the **Actions**
column.
2. In the **Access Log** dialog box, you can view information such as **Access Status Code** and **Accessed**
**At**. Find the access log that you want to view and click **Details** in the **Actions** column. You can view
the details of the access log, including the request time, request parameters, and request results.

**Modify a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Modify** in the **Actions**
column.
2. In the **Modify Trigger** dialog box, modify the configuration of the trigger and click **OK**.

**Delete a trigger**

1. On the **Trigger** page, find the trigger that you want to manage and click **Delete** in the **Actions**
column.
2. In the **Confirm Deletion** message, click **OK**.

### Replicate images between

**instances that belong to the same**

**account**

This topic describes how to manually and automatically replicate images from a Container Registry Multi-instance Edition instance to a Container Registry Multi-instance Edition or Advanced Edition instance that is in the same region or across regions within the same account.

**Automatic image replication between instances that belong to the**

| Parameter | Description |
|---|---|
| Rule Name | The name of the custom rule. The name must be 1 to 128 characters in length. |
| Synchronization Scenario | You can select only Same Account. |
| Destination Instance | Select a region, an instance type, and an instance. |
| Synchronization Level | Valid values: Namespace: Images in all repositories in the specified namespace are synchronized. Repository: Only images in the specified repository are synchronized. |
| Source Namespace | Select an existing namespace. |
| Source Repository | Note This parameter is displayed only when Synchronization Level is set to Repository. Specify the name of the repository in which the images will be synchronized. |
| Tag Filter | Enter a regular expression to filter the tags of images in the repository. By default, all image tags are selected. |

You can configure a replication rule to automate image replication between two instances that belong to the same account. After you upload an image to the source instance, the system automatically replicates the image to the destination instance. 1. 2. 3.
4. On the management page of your Container Registry Multi-instance Edition instance, click **Instance**
**Synchronization** in the left-side navigation pane. Then, click **Create Rule** on the right side of the
page.
5. In the **Create Rule** dialog box, configure the following parameters and click **Create**
**Synchronization Rule**.

**Important**

The destination instance must have a namespace same as that of the source namespace. If you set Synchronization Level to Repository, a repository with the same name must also exist. Otherwise, the rule fails to be created. Select a source instance and click **Detect** to check whether the destination instance meets the requirement. If the destination instance does not have the same namespace or repository, create them first. For more information, see Create a namespace and Create an image repository.

**Note**

You can select a Container Registry Multi-instance Edition or a Container Registry Advanced Edition instance in the same region or across regions to replicate images. When you upload an image to the source instance, the image is automatically replicated to the destination instance. In the left-side navigation pane of the management page of the Container Registry Multi-instance Edition instance, click **Synchronization Records**. If the status of the replication task on the
**Synchronization Records** page is **Completed** and the image exists in the destination instance,
the image is automatically replicated between the instances that belong to the same account. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact Size**,
**Size of Replicated Image Layer**, and **Replication Status**. The layer details include **Layer**
**Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You can check
whether the tag has been replicated and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task.

**Manual image replication between instances that belong to the same**

You can configure a replication rule to manually replicate an image from a source instance to a destination instance.

**Method 1: Perform the following operations on the Image Version**

**page**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. On the details page of the image repository, click **Image Version** in the left-side navigation pane.
7. On the **Image Tag** page, find the image that you want to manage and click **Image Replication** in the
**Actions** column of the image.
8. In the **Select Destination Repository for Replication** dialog box, select **Same Account** for the
**Synchronization Scenario** parameter, specify the region, product type, destination instance name,
namespace, image repository, and repository version, specify **Overwrite Image**, and then click **OK**. You can select a Container Registry Multi-instance Edition or Advanced Edition instance in the same region or across regions to replicate data. If the source and destination instances are the same, you can replicate images only between different namespaces. After you manually create the replication rule, image replication between the instances is immediately triggered. On the **Image Version** page, you can click the icon in the **Actions** column of the desired image and click **Synchronization Records**. On the **Synchronization Records** page, if the status of the replication task is **Replicated** and the image can be found in the destination instance, the image is manually replicated between the instances that belong to the same account. You can perform the following operations in the **Actions** column of a replication task: Click **Details** to view the path from the source to the destination, artifact information, and layer details. The artifact information includes **Artifact Digest**, **Type**, **OS/Architecture**, **Artifact**
**Size**, **Size of Replicated Image Layer**, and **Replication Status**. The layer details include
**Layer Digest**, **Layer Size**, **Size of Replicated Image Layer**, and **Replication Status**. You
can check whether the tag has been synchronized and view the transmission status of a specific layer. Click **Re-trigger**. In the message that appears, click **OK** to retry the replication task.

**Method 2: Perform the following operations on the Image**

**Synchronization page**

1. 2. 3. 4.
5. On the **Image Repository** page, click the name of the image repository that you want to manage.
6. On the details page of the image repository, click **Image Synchronization** in the left-side navigation
pane.
7. On the **Image Replication** page, click **Create Copy Task**.
8. In the **Select Destination Repository for Replication** dialog box, select a value for **Image Tag to**
**be Copied**, specify the region, product type, destination instance name, namespace, image
repository, and repository version, specify **Overwrite Image**, and then click **OK**. You can select a Container Registry Multi-instance Edition or Advanced Edition instance in the same region or across regions to replicate data. If the source and destination instances are the same, you can replicate images only between different namespaces. After you manually create the replication rule, image replication between the instances is immediately triggered. If the status of the replication task on the **Image Replication** page is **Replicated** and the image exists in the destination instance, the image is manually replicated between the instances that belong to the same account. Find the replication task that you want to view and click **Details** in the **Actions** column. You can view the path from the source to the destination and the replication status of the involved artifacts and layers, such as **Image Layer Digest**, **Image Size**, and **Replication Status**.

### Configure a repository to be

**immutable**

Container Registry allows you to configure a repository to be immutable to prevent image tags from being overwritten due to unintended operations. After you configure a repository to be immutable, the existing and newly added image tags in the repository cannot be overwritten except for the tags of the latest. After you push an image with a tag other than latest to the repository, you cannot push another image with the same tag to the repository. This ensures that the images in the repository are consistent with the images that have been deployed in containers. This topic describes how to configure a repository to be immutable.

**Procedure**

1. 2. 3. 4.
5. On the **Image Repository** page, find the repository that you want to manage and click **Management**
in the **Operation** column.

| Parameter | Description |
|---|---|

6. On the Basic Information page, click **Edit**.
7. In the **Modify Basic Information** dialog box, select **Immutable** for **Image Tag** and click **OK**.

**Note**

To configure a repository to be mutable, clear **Immutable**.

**Verify the results**

1. Run the `docker push` command to push an image whose tag is not latest to the repository.

```bash
docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:v1
```

2. Push another image whose tag is the same as the tag of the image you pushed in Step 1.
The push request is denied. The following error is returned, which indicates that the image tag cannot be overwritten:

```
The requested tag already exists and cannot be overwritten.
```

3. Run the `docker push` command to push an image whose tag is latest to the repository.

```bash
docker push <Address of the repository>/<Name of the namespace>/<Name of the repository>:latest
```

4. Push another image whose tag is also latest. The tag is the same tag of the image that you pushed in
Step 3. The push is successful. The image overwrites the image that you pushed in Step 3.
5. Configure the repository to be mutable. For specific operations, see the preceding section.
6. Push another image whose tag is the same as the tag of the image you pushed in Step 1.
The push is successful. The image overwrites the image that is pushed in Step 1.

### Delete image tags

Container Registry allows you to delete multiple image tags of a Container Registry instance at a time. This topic describes how to delete multiple image tags at a time by configuring a tag retention policy.

**Configure a tag retention policy**

After you configure a tag retention policy, the image tags that do not match the policy are deleted. 1. 2. 3. 4.
5. On the **Version Management** page, click **Create a retention policy**.
6. In the **Create a retention policy** dialog box, configure the following parameters and click **OK**.

| Cleaning range | Namespace: After you select a namespace, the retention policy applies to all image repositories in the namespace. Note You can enter a namespace keyword to search for namespaces. Warehouse: After you select a namespace and an image repository, the retention policy applies to the specified image repository in the namespace. Note You can enter a namespace keyword and a repository keyword to perform a quick search. |
|---|---|
| Execution method | Only Manual is supported. |
| Number of reserved images (Optional) | The number of recently pushed image tags that are retained. The number of retained images must be greater than 0 and less than or equal to the total number of current image tags. |
| Retain image version (optional) | In addition to the number of recently pushed images that you want to retain, you can specify the image tags that you want to retain. Note The default value of this parameter is an asterisk (*), which indicates that all image tags are retained in addition to the specified number of recently pushed images. |
| Last Pull Retention Days (optional) | The images that are recently pulled within the number of days specified by this parameter are retained. |
| Recent push retention days (optional) | The images that are recently pushed within the number of days specified by this parameter are retained. |

**Manually trigger a tag deletion task**

1. On the **Version Management** page, find the retention policy that you want to apply and click
**Execute now** in the **Operation** column.
2. In the message that appears, click **OK**.

**View the task list**

1. In the **Task list** section of the **Version Management** page, view image tag deletion tasks and the
status of the tasks.
2. Find the task that you want to view and click **View** in the **Operation** column. In the panel that
appears, view the details of the task.

**Manage retention policies**

On the **Version Management** page, you can perform the following operations on a retention policy: Modify a retention policy: Find the retention policy that you want to modify, click **Modify** in the
**Operation** column, modify the settings of the retention policy, and then click **OK**.
Delete a retention policy: Find the retention policy that you want to delete and click **Delete** in the
**Operation** column. In the message that appears, click **OK**.

### Use the aliyun-acr-credential-

**helper component to pull images**

**without using a secret**

You can use the aliyun-acr-credential-helper component to pull private images without using a secret from instances of Container Registry Standard Edition, Advanced Edition, and Multi-instance Edition. This component is automatically installed in Container Service for Kubernetes (ACK) clusters. This topic describes how to use the aliyun-acr-credential-helper component to pull a private image without using a secret in different scenarios.

**Prerequisites**

An ACK cluster is created. For more information, see **Create a Kubernetes cluster** in **Container**
**Service for Kubernetes User Guide**.
A kubectl client is connected to your cluster. For more information, see **Use kubectl to connect to a**
**Kubernetes cluster** in **Container Service for Kubernetes User Guide**.

**Usage notes**

If you want to use the aliyun-acr-credential-helper component, do not specify the imagePullSecret parameter. If the imagePullSecret parameter is specified in the template of a Kubernetes resource, such as a Deployment, the component becomes invalid. If a Kubernetes resource, such as a Deployment, uses a custom service account, you must modify the service-account parameter in the configuration file of the aliyun-acr-credential-helper component. This way, the component is authorized to pull images by using the custom service account. Check whether the private image that you want to pull resides in the same region as your ACK cluster. By default, you can pull private images only from Container Registry instances that reside in the same region as your ACK cluster. If you want to pull images from Container Registry instances that reside in different regions from your ACK cluster, see Scenario 2 in this topic. After you create a service account in a cluster, it takes some time for the aliyun-acr-credential-helper component to renew the token of the service account. The new token for pulling private images is generated based on the default permissions of your ACK cluster. Applications with the service account can use the token to pull images only after the token is renewed. If you create an application immediately after you create a service account, the application will fail to pull images because it is unauthorized. By default, the configuration of the aliyun-acr-credential-helper component overwrites the
**imagePullSecret** parameter of default service accounts in all namespaces. These service accounts
are automatically modified when the **service-account** parameter of the **acr-configuration** ConfigMap in the kube-system namespace is changed. When you modify the **acr-configuration** ConfigMap in the kube-system namespace, make sure that you use the same indentation as the example that is provided in this topic. We recommend that you paste the YAML code provided in this topic to the editor, replace the corresponding values, and apply the configuration. This ensures that the format of the ConfigMap is valid.

**Update and configure the aliyun-acr-credential-helper component**

Before you use aliyun-acr-credential-helper to pull images, you may need to update and configure the component. To do so, perform the following steps: Configure the acr-configuration ConfigMap.

**Method 1: Configure the acr-configuration ConfigMap in the ACK console**

1. Log in to the ACK console. For more information, see **Log in to the ACK console** in the **Container**
**Service for Kubernetes User Guide**.
2. In the left-side navigation pane, click **Cluster**.
3. On the **Cluster List** page, click the name of the cluster that you want to view.
4. In the left-side navigation pane of the **Cluster Information** page, choose **Configuration**
**Management > Config Maps**.

| Name of the acr- configuration ConfigMap | Description of the name | Value |
|---|---|---|
| service-account | The service accounts that are used by the aliyun-acr-credential-helper component to pull images. | Default value: default. Note Separate multiple service accounts with commas (,). Enter an asterisk (*) to specify all service accounts in all namespaces. |
| acr-registry-info | The information about Container Registry instances. Each instance can be specified by three fields of the String type in a YAML file. Note Configure the three fields based on the following descriptions: instanceId: the ID of the Container Registry instance. This field is required for Container Registry Enterprise Edition and Multi-instance Edition instances. domains: the domain names of the Container Registry instance. This parameter is optional. By default, all domain names of the instance are specified. You can specify one or more domain names. Separate multiple domain names with commas (,). | The value is empty by default. This means that images are pulled from the default repository of the Container Registry instance that resides in the same region as your ACK cluster. Sample configurations for a Container Registry Advanced Edition or Multi- instance Edition instance: - instanceId: "cri-xxx" domains: "xxx.com,yyy.com" Sample configurations for a Container Registry Standard Edition instance: - instanceId:"" domains: "xxx.com,yyy.com" |
| watch-namespace | The namespaces from which images can be pulled without secrets. | Default value: default. Note If the value is set to all, images can be pulled from all namespaces without a secret. Separate multiple namespaces with commas (,). |
| expiring-threshold | The duration after which the cache token expires. | Default value: 15m. We recommend that you use the default value. |

5. In the upper part of the **ConfigMap** page, select **kube-system** from the Namespace drop-down list
and find the **acr-configuration** ConfigMap. Then, modify the acr-configuration ConfigMap by using one of the following methods: Method 1: Click **Edit** in the Actions column and modify the names and values of the **ConfigMap**. Method 2: Click **Edit YAML** in the Actions column and modify the names and values of the
**ConfigMap**.
The following table describes the names and values of the acr-configuration ConfigMap.

**Method 2: Configure the acr-configuration ConfigMap by using kubectl**

1. Run the following command to open the editing page of the acr-configuration ConfigMap:

```bash
kubectl edit cm acr-configuration -n kube-system
```

2. Configure the parameters of the acr-configuration ConfigMap based on your requirements.
Sample configurations for Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition: Advanced Edition and Multi-instance Edition

```
apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"cri-xxx" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration
  namespace:kube-system
selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration apiVersion:v1 data: acr-api-version:"2018-12-01" acr-registry-info:|- -instanceId:"" expiring-threshold:15m service-account:default watch-namespace:all kind:ConfigMap metadata: name:acr-configuration namespace:kube-system selfLink:/api/v1/namespaces/kube-system/configmaps/acr-configuration
```

**Scenario 1: Pull private images from Container Registry Advanced**

**Edition, Multi-instance Edition, and Standard Edition instances**

ACK allows you to pull private images from Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition instances at the same time, only from Container Registry Advanced Edition and Multi-instance Edition instances, or only from Container Registry Standard Edition instances. Modify the
**acr-configuration****ConfigMap** based on your business requirements. For more information, see Update
and configure the aliyun-acr-credential-helper component. Sample configurations: Pull private images from Container Registry Advanced Edition and Multi-instance Edition instances.

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

| Paramete r | Description | Example |
|---|---|---|
| Key Type | Symmetric CMKs: Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ | Asymmetric customer master keys (CMKs): RSA 2048 _ EC P256 _ EC P256K _ |

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

Pull private images from Container Registry Advanced Edition, Multi-instance Edition, and Standard Edition instances.

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

### Sign container images

To prevent man-in-the-middle (MITM) attacks and the update and running of invalid images, Container Registry automatically signs images in specified namespaces. After an image is pushed to Container Registry, Container Registry automatically signs the image based on the matched signing rules. This ensures that your container images are trusted.

**Create asymmetric keys**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Security > Key Management Service**.
3. On the **Customer Master Key** page, click **Create Key**.
4. On the **Create Key Pair** page, select an organization from the **Organization** drop-down list. Then,
the **Resource Set** and **Region** parameters are automatically configured.
5. In the **Basic Configurations** section, configure the parameters that are described in the following
table.

**Note**

The image signing feature is implemented based on asymmetric key algorithms. When you create the KMS key, select an EC or RSA key type and set the Purpose parameter to SIGN/VERIFY. Other parameters are configured based on your business.

| Key Purpose | ENCRYPT/DECRYPT: The CMK is used to encrypt and decrypt data. SIGN/VERIFY: The CMK is used to generate and verify a digital signature. | SIGN/VERIFY |
|---|---|---|

6. Click **Confirm Order**.

**Authorize Container Registry to access KMS keys**

To allow Container Registry to read asymmetric keys within your account, configure a policy in Resource Access Management (RAM).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise > Permissions > Role Permissions**.
3. Click **Create Custom Role** page, click **Advanced Settings** -> **Create RAM Role & Attach Policy** .
4. On the RAM Roles page, create a RAM role named AliyunContainerRegistryKMSRole.
i. **Basic Configurations**
**Role Name**: AliyunContainerRegistryKMSRole.
**Description**: custom.
**Sharing Scope**: global sharing.
Click **Next**. ii. **Custom policy configurations.** a. Click **Create Policy**. On the **Create Policy** page, set the following parameters:
**Policy Name**: AliyunContainerRegistryKMSRolePolicy
**Policy Content**:

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kms:*"
```

`],`

```json
      "Resource": "acs:kms:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "yundun-css:*"
```

`],`

```json
      "Resource": "*"
    }
```

`],`

```json
  "Version": "1"
}
```

Then, click **OK**. b. On the **Role Authorization** page, enter **AliyunContainerRegistryKMSRolePolicy** in the **Select**
**Policy** field.
c. Select the policy content and click **Next**. iii. **Trust Policy Configuration**
**Cloud services**: Select the **cr.aliyuncs.com** and click **Next**.
iv. **Policy preview** Click **Create** to create and authorize the AliyunContainerRegistryKMSRole role. If multiple organizations need to use image signature, repeat the following steps to create a RAM role for the target organizations.
1. In the top navigation bar, choose **Enterprise > Permissions > Role Authorization**.
2. On the **Role Authorization** page, enter AliyunContainerRegistryKMSRole in the search box, and then
click the name of the role.
3. On the **Role Name: AliyunContainerRegistryKMSRole** page, click **RAM Role**.
4. On the **RAM Roles** tab, click **+ Create**. In the search box, select the organization that you want to
create and click **OK**.

**Configure a witness and a signature verification policy**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Server Security > Container Security Service**
**(CSS)**.
3. In the left-side navigation pane, choose **Runtime Detection > Container Signature**. On the
Container Signature page, create a witness and associate it with the KMS key for container image signing.

**Configure a signature rule for automatic image signing**

1. 2. 3.
4. On the instance management page, click **Image Signing** in the left-side navigation pane, and then
click **Create a signature rule**.
5. In the **Key Configuration** step, select the witness that you created in the Security Center console and
associate the witness with the KMS key. Then, click **Next**.
6. In the **Signature Configurations** step, configure the parameters and click **Create Signing Rule**.

**Note**

A signature rule applies only to new images that are pushed to the specified namespace. Existing images are not signed based on the signature rule.
**Algorithms**: You can select **RSA_PSS_SHA_256** or **RSA_PKCS1_SHA_256**.
**Scope**: Select the instance or namespace that you want to automatically sign.
**Signature Type**:
**Default**: Image digests and tags are signed. The default mode is suitable for the signing of images
in the current instance.
**Simple**: Only image digests are signed. Image tags are not signed. The simple mode is suitable
for cross-instance image replication scenarios. The signatures of corresponding images are verified when image tags change.
**Trigger Type**: the mode in which image signing is triggered. The default value is Automatic Trigger,
indicating that image signing is automatically triggered for each image that is pushed to Container Registry.

**Image signature verification**

For more information about image signature verification, see **Use kritis-validation-hook to automate**
**image signature verification** of **Kubernetes Clusters > Application management** in the **ACK**
**User Guide**.

**Note**

You can use kritis-validation-hook to automatically verify image signatures in Container Service for Kubernetes (ACK) clusters. You can set a policy to block image deployment if image signatures fail the verification. We recommend that you use this method. You can also verify image signatures in Container Registry by using the signature verification feature of **KMS**.
