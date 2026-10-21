---
title: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud DNS Alibaba Cloud DNS (Within Cloud) User Guide 20250612"
product_version: "V3.18.2"
doc_version: "20250612"
pdf_pages: 50
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud DNS Alibaba Cloud DNS (Within Cloud) User Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/DNS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Alibaba%20Cloud%20DNS%20Alibaba%20Cloud%20DNS%20%28Within%20Cloud%29%20User%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud DNS Alibaba Cloud DNS (Within Cloud) User Guide 20250612

## Table of Contents

- 1 What is Apsara Stack DNS?
- 2 User roles and permissions
- 3 Log on to the Apsara Stack DNS console
- 4 DNS within cloud
  - 4.1 Internal DNS resolution management
    - 4.1.1 Global internal domain names
      - 4.1.1.1 Overview
      - 4.1.1.2 View an internal domain name
      - 4.1.1.3 Add a domain name
      - 4.1.1.4 Add a description for a domain name
      - 4.1.1.5 Delete a domain name
      - 4.1.1.6 Delete multiple domain names at a time
      - 4.1.1.7 Add a DNS record for a domain name
    - 4.1.2 Global forwarding configurations
      - 4.1.2.1 Global forwarding domain names
        - 4.1.2.1.1 Overview
        - 4.1.2.1.2 View global forwarding domain names
        - 4.1.2.1.3 Add a domain name
        - 4.1.2.1.4 Add a description for a domain name
        - 4.1.2.1.5 Modify the configurations of a domain name
        - 4.1.2.1.6 Delete a domain name
        - 4.1.2.1.7 Delete multiple domain names
      - 4.1.2.2 Global default forwarding configurations
        - 4.1.2.2.1 Enable default forwarding
        - 4.1.2.2.2 Modify default forwarding configurations
        - 4.1.2.2.3 Disable default forwarding
    - 4.1.3 Global recursive resolution
      - 4.1.3.1 Recursive ACL policy
        - 4.1.3.1.1 Overview
        - 4.1.3.1.2 Add an ACL policy
        - 4.1.3.1.3 Modify an ACL policy
        - 4.1.3.1.4 Add a description for an ACL policy
        - 4.1.3.1.5 Delete an ACL policy
        - 4.1.3.1.6 Delete multiple ACL policies at a time
      - 4.1.3.2 Global default recursion
        - 4.1.3.2.1 Enable global recursive resolution
        - 4.1.3.2.2 Disable global recursive resolution
    - 4.1.4 Cache management
      - 4.1.4.1 Query caches
      - 4.1.4.2 Clear caches
  - 4.2 IP Address Line Configuration
    - 4.2.1 View global lines
    - 4.2.2 Add a line
    - 4.2.3 Sort lines
    - 4.2.4 Modify the configurations of a line
    - 4.2.5 Delete a line
    - 4.2.6 Delete multiple global lines at a time
- 5 Private DNS
  - 5.1 PrivateZone (DNS Standard Edition only)
    - 5.1.1 Tenant internal domain name
      - 5.1.1.1 View a domain name
      - 5.1.1.2 Add a domain name
      - 5.1.1.3 Configure DNS records
      - 5.1.1.4 Bind an organization to a VPC
      - 5.1.1.5 Unbind a domain name from a VPC
      - 5.1.1.6 Add a description for a domain name
      - 5.1.1.7 Delete a domain name
      - 5.1.1.8 Delete multiple domain names at a time
      - 5.1.1.9 View a resolution policy
    - 5.1.2 Tenant forwarding configurations
      - 5.1.2.1 Tenant forwarding domain names
        - 5.1.2.1.1 View a tenant forwarding domain name
        - 5.1.2.1.2 Add a tenant forwarding domain name
        - 5.1.2.1.3 Modify the forwarding configurations of a domain name
        - 5.1.2.1.4 Bind an organization to a VPC
        - 5.1.2.1.5 Unbind a domain name from a VPC
        - 5.1.2.1.6 Add a description for a tenant forwarding domain name
        - 5.1.2.1.7 Delete a tenant forwarding domain name
        - 5.1.2.1.8 Delete multiple tenant forwarding domain names
      - 5.1.2.2 Tenant default forwarding configurations
        - 5.1.2.2.1 View default forwarding configurations
        - 5.1.2.2.2 Add a default forwarding configuration
        - 5.1.2.2.3 Bind an organization to a VPC
        - 5.1.2.2.4 Unbind a domain name from a VPC
        - 5.1.2.2.5 Modify a default forwarding configuration
        - 5.1.2.2.6 Add a default forwarding configuration
        - 5.1.2.2.7 Delete a default forwarding configuration
        - 5.1.2.2.8 Delete multiple default forwarding configurations
  - 5.2 Private lines
    - 5.2.1 Query private lines
    - 5.2.2 Create a private line
    - 5.2.3 Change the priority of a private line
    - 5.2.4 Modify a private line
    - 5.2.5 Delete a private line
    - 5.2.6 Delete multiple private lines at a time
- 6 Global scheduling
  - 6.1 Scheduling instances
    - 6.1.1 Search for a scheduling instance
    - 6.1.2 Create a scheduling instance
    - 6.1.3 Modify the configurations of a scheduling instance
    - 6.1.4 Configure a scheduling instance
      - 6.1.4.1 Create an access policy for a scheduling instance
      - 6.1.4.2 Modify the access policy of a scheduling instance
      - 6.1.4.3 Delete the access policy of a scheduling instance
    - 6.1.5 Delete a scheduling instance
  - 6.2 Address pool
    - 6.2.1 Search for address pools
    - 6.2.2 Create an address pool
    - 6.2.3 Modify the configurations of an address pool
    - 6.2.4 Delete an address pool
    - 6.2.5 Create a health check task for an address pool
- 7 System management
  - 7.1 Nodes
    - 7.1.1 View a node
    - 7.1.2 Configure the emergency group feature
    - 7.1.3 Add a description for a node
    - 7.1.4 Set a follower node as the leader node
  - 7.2 Logs
    - 7.2.1 Query alert logs

DNS?

## 1 What is Apsara Stack DNS?

Apsara Stack DNS is a service that runs on Apsara Stack to resolve domain names. You can configure rules to map domain names to IP addresses. Then, Apsara Stack DNS distributes domain name requests from clients to cloud resources, business systems on your internal networks, or the business resources of Internet service providers (ISPs). Apsara Stack DNS provides DNS resolution in virtual private clouds (VPCs). You can perform the following operations in your VPC by using Apsara Stack DNS: Access other ECS instances deployed in your VPC. Access cloud service instances provided by Apsara Stack. Access custom enterprise business systems. Access Internet services and businesses. Establish network connections between DNS and user-created DNS over a leased line. Manage internal domain names. Manage DNS records of internal domain names. Manage forwarding configurations. Manage recursive resolution configurations. sions

## 2 User roles and permissions

| Role | Permission |
|---|---|
| System administrator | A user of this role has read, write, and execute permissions on all level-1 organization resources, global resources, and system configurations. |
| Level-1 organization administrator | A user of this role has read, write, and execute permissions on level-1 organization resources to which the user belongs, but does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Lower-level organization administrator | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Resource user | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Other roles | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |

Stack DNS console

## 3 Log on to the Apsara Stack DNS console

**DNS console**

This topic describes how to log on to the Apsara Stack DNS console by using Google Chrome.

**Prerequisites**

You need to obtain the endpoint of the Apsara Uni-manager Management Console from the deployment personnel. A browser is available. We recommend using Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter. Stack DNS console

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.

If you need to click Continue to access multiple times or cannot find the entry to the Apsara Uni-manager Management Console because of an expired browser certificate or HTTPS authentication enabled in the environment, you must install a certificate for normal access. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Account Logon**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Networking > DNS within Cloud**.

## 4 DNS within cloud

### 4.1 Internal DNS resolution management

**management**

Internal DNS resolution management allows you to manage global internal domain names, global forwarding configurations, and global recursive resolution configurations that you have created in Apsara Stack.

#### 4.1.1 Global internal domain names

##### 4.1.1.1 Overview

All the operations of this feature require administrator privileges.

##### 4.1.1.2 View an internal domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domains > Global Internal Domains**.
3. In the **Domain Name** search box, enter the domain name that you want to view.
4. Click **Search**.
The search result is displayed.

##### 4.1.1.3 Add a domain name

This topic describes how to add a global internal domain name in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane.
3. On the Global Internet Domain Name tab of the page that appears, click **Add Domain**
**Name**.
4. In the Add Global Internal Domain Name dialog box, enter a domain name in the **Global**
**Internal Domain Name** field.
5. Select an option from the **Current Domain Name Type** drop-down list.
6. Select Primary Domain Name or Secondary Domain Name.
7. If you select Secondary Domain Name, you must specify the **DNS Server Address of**
**Primary Domain Name** parameter. Only IPv4 and IPv6 addresses are supported. Specify
the parameter in the format of IP address:Port number.
8. Turn on **Enable TSIG Key Authentication** based on your business requirements.
9. Click **OK**.

##### 4.1.1.4 Add a description for a domain name

This topic describes how to add a description for a domain name in the Apsara Uni-manager Management Console.

**Background information**

You can add a description for a domain name to help you identify it. For example, you can add a hostname or internal system information to describe a domain name.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Global Internal**
**Domain Name**.
3. Find the domain name for which you want to add a description, click the
icon in the Actions column, and then select **Description**.
4. In the dialog box that appears, enter a description.
5. Click **OK**.

##### 4.1.1.5 Delete a domain name

This topic describes how to delete a domain name in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Global Internal**
**Domain Name**.
3. Find the domain name that you want to delete, click the
icon in the **Actions** column, and then select **Delete**.
4. In the message that appears, click **OK**.

##### 4.1.1.6 Delete multiple domain names at a time

This topic describes how to delete multiple global internal domain names at a time in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane.
3. On the Global Internet Domain Name tab of the page that appears, select one or more
domain names that you want to delete and click **Batch Delete** below the domain names.
4. In the message that appears, click **OK**.

##### 4.1.1.7 Add a DNS record for a domain name

This topic describes how to add a Domain Name System (DNS) record for a global internal domain name in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Stack DNS console. For more information, see Log on to the Apsara
Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane.
3. On the Global Internet Domain Name tab of the page that appears, find the domain name
for which you want to add a DNS record and click **Configure DNS Records** in the Actions column.
4. On the **DNS Settings** page, click **Add DNS Record**.
5. You can only view the DNS records for secondary domain names, because the Configure
DNS Records, Add Description, and Delete options in the Actions column of the secondary domain names are unavailable on the Global Internet Domain Name tab. 6.

#### 4.1.2 Global forwarding configurations

##### 4.1.2.1 Global forwarding domain names

###### 4.1.2.1.1 Overview

All operations on global forwarding domain names require system administrator permissions. Apsara Stack DNS forwards specific domain names to other DNS servers for resolution. Apsara Stack DNS can forward requests with or without recursion. In the mode of forwarding without recursion, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails. In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used.

###### 4.1.2.1.2 View global forwarding domain names

This topic describes how to view global forwarding domain names in the Apsara Uni-manager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Forwarding Domain Names**.
3. In the **Domain Name** search box, enter the domain name that you want to query and click
**Search**.

###### 4.1.2.1.3 Add a domain name

This topic describes how to add a domain name in the Apsara Uni-manager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Forwarding Domain Names**.
3. Click **Add Domain Name**.
4. In the dialog box that appears, configure Global Forwarding Domain, Forwarding Mode, and
Forwarder IP Addresses. Then, click **OK**.

###### 4.1.2.1.4 Add a description for a domain name

This topic describes how to add a description for a domain name in the Apsara Uni-manager Management Console. This operation requires administrator permissions.

**Background information**

You can add a description for a domain name to help you identify it. For example, you can describe a domain name by using a hostname or internal system information.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Forwarding Domain Names**.
3. Select the domain name for which you want to add a description, click
in the Actions column, and then select **Description**.
4. In the dialog box that appears, enter a description and click **OK**.

###### 4.1.2.1.5 Modify the configurations of a domain name

**name**

This topic describes how to modify the configurations of a global forwarding domain name in the Apsara Uni-manager Management Console. This operation requires system administrator permissions.
1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the page that appears, click the **Global Forwarding Configurations** tab and click the Global Forwarding Domain Names subtab.
3. Find the domain name whose configurations you want to modify and click **Modify** in the
Actions column.
4. In the dialog box that appears, modify the Forwarding Mode and Destination IP Address
parameters based on your business requirements and click **OK**.

###### 4.1.2.1.6 Delete a domain name

This topic describes how to delete a domain name in the Apsara Uni-manager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Forwarding Domain Names**.
3. Find the domain name that you want to delete, click the
icon in the Actions column, and then select **Delete**.
4. Click **OK**.

###### 4.1.2.1.7 Delete multiple domain names

This topic describes how to delete multiple domain names at a time in the Apsara Unimanager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Domains > Forwarding**
**Settings > Global Forwarding Domain Names**.
3. Select one or more domain names that you want to delete and click **Delete** in the upper-
right corner.
4. In the message that appears, click **OK**.

##### 4.1.2.2 Global default forwarding configurations

###### 4.1.2.2.1 Enable default forwarding

This topic describes how to enable default forwarding in the Apsara Uni-manager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Default Forwarding**.
3. Click the
icon in the Actions column and select **Enable**.
4. In the dialog box that appears, configure Default Forwarding Mode and Forwarder IP
Addresses. Then, click **OK**. Make sure that **Enable Default Forwarding** is set to **ON**.

###### 4.1.2.2.2 Modify default forwarding configurations

This topic describes how to modify default forwarding configurations in the Apsara Unimanager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Default Forwarding**.
3. Click the
icon in the Actions column and select **Modify**.
4. In the dialog box that appears, configure Forwarding Mode and Forwarder IP Addresses.
Then, click **OK**.

###### 4.1.2.2.3 Disable default forwarding

This topic describes how to disable default forwarding in the Apsara Uni-manager Management Console. This operation requires administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Internal Domain Names > Forwarding**
**Settings > Global Default Forwarding**.
3. Click the
icon in the Actions column and select **Disable**.
4. In the message that appears, click **OK**.

#### 4.1.3 Global recursive resolution

##### 4.1.3.1 Recursive ACL policy

###### 4.1.3.1.1 Overview

Recursive access control list (ACL) policies are used to specify whether to recursively send DNS requests to the Internet.

> **Note:** Recursion for ACL policies takes precedence over global resolution.

###### 4.1.3.1.2 Add an ACL policy

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Global Recursive Resolution tab.
3. On the Recursive ACL Policy subtab, click **Add Access Control Policy**.
4. In the dialog box that appears, enter a name in the **ACL Policy Name** field.
5. Select an option from the **Request Source** drop-down list.
6. Turn off **Enable Recursion** based on your business requirements.
7. Enter a **description**. This parameter is optional.

**Important**

| Parameter | Description |
|---|---|
| ACL Policy Name | Required. The name is globally unique in recursive access control list (ACL) policies. For more information about the naming conventions, see Basic conventions for user interfaces. |
| Request Source | Required. You can select multiple global lines. A custom line cannot be selected together with another custom line. If a custom line is selected for another ACL policy, it cannot be selected. |
| Enable Recursion | Required. |

###### 4.1.3.1.3 Modify an ACL policy

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Global Recursive Resolution tab.
3. On the Recursive ACL Policy subtab, find the recursive access control list (ACL) policy that
you want to modify and click **Modify** in the Actions column.
4. In the dialog box that appears, modify the value of the **Policy Name** parameter.
5. Select an option from the **Request Source** drop-down list.
6. Turn off **Enable Recursion** based on your business requirements.

###### 4.1.3.1.4 Add a description for an ACL policy

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Global Recursive Resolution tab.
3. On the Recursive ACL Policy subtab, find the recursive access control list (ACL) policy for
which you want to add a description and click **Description** in the Actions column.
4. In the dialog box that appears, enter a description.

###### 4.1.3.1.5 Delete an ACL policy

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Global Recursive Resolution tab.
3. On the Recursive ACL Policy subtab, find the recursive access control list (ACL) policy that
you want to delete and click **Delete** in the Actions column.
4. In the message that appears, click **OK**.

###### 4.1.3.1.6 Delete multiple ACL policies at a time

You can delete multiple access control list (ACL) policies at a time in the Apsara Stack Domain Name System (DNS) console. This operation requires system administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, click **Global Domain Name within Cloud**. On the **Global**
**Domain Names** page, click the **Global Recursive Resolution** tab, and then click the
**Recursive ACL Policy** subtab.
3. Select one or more ACL policies and click **Batch Delete** in the lower-left corner of the
page.
4. In the message that appears, click **OK**.

##### 4.1.3.2 Global default recursion

###### 4.1.3.2.1 Enable global recursive resolution

**Prerequisites**

You have administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. Choose **Internal Domains > Global Recursive Resolution**.
3. Click the
icon in the Actions column and select **Enable**.
4. In the dialog box that appears, click **OK**.

###### 4.1.3.2.2 Disable global recursive resolution

**Prerequisites**

You have administrator permissions.
1. Log on to the Apsara Stack DNS console.
2. Choose **Internal Domains > Global Recursive Resolution**.
3. Click the
icon in the Actions column and select **Disable**.
4. In the dialog box that appears, click **OK**.

#### 4.1.4 Cache management

Domain names that are queried by using global forwarding or recursion are cached.

##### 4.1.4.1 Query caches

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Cache Management tab.
3. Select an option from the **Type** drop-down list next to Clear Cache and enter the **domain**
**name**.
4. The cached domain name is displayed.

##### 4.1.4.2 Clear caches

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **DNS within Cloud > Global Domain Name within Cloud** in the left-side
navigation pane. On the Global Domain Names page, click the Cache Management tab.
3. Click **Clear Cache**.
4. In the dialog box that appears, specify the **Service Instance and Domain Name**
parameters.
5. Select an option from the **Domain Name Matching Method** drop-down list.

**Important**

| Parameter | Description |
|---|---|
| Service Instance | You can select multiple options. Only the learner nodes on the Nodes page can be selected. The name is displayed in the format of Resolution Node (Service instance IP address). |
| Domain Name | Enter a domain name. |
| Domain Name Matching Method | You can select Suffix Match or Exact Match. Suffix Match is selected by default. If you select Suffix Match, all domain names with the same suffix as the domain name that you entered are cleared. If you select Exact Match, the domain names that are the same as the domain name that you entered are cleared. |

### 4.2 IP Address Line Configuration

The IP Address Line Configuration tab allows you to define lines based on IP addresses. The lines are used to group request sources to achieve intelligent load balancing.

#### 4.2.1 View global lines

You can view the list of global lines in the Apsara Stack Domain Name System (DNS) console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, click **Global Line**.
3. On the Global Line page, select **Line Name** or **IP** from the drop-down list, enter the
corresponding keyword in the search box, and then click the Search icon.

#### 4.2.2 Add a line

1. In the left-side navigation pane, choose **Internal Global Traffic Manager** > **Scheduling**
**Line Management** > IP Address Line Configuration.
2. Click **Add Line** in the upper-right corner of the line list.
3. In the dialog box that appears, configure the parameters as prompted and click **OK**.

#### 4.2.3 Sort lines

1. In the left-side navigation pane, choose **Internal Global Traffic Manager** > **Scheduling**
**Line Management** > IP Address Line Configuration.
2. Find the line whose sequence you want to change and click **Sort** in the Actions column.
3. Specify Sort Behavior as prompted and click **OK**.

#### 4.2.4 Modify the configurations of a line

1. In the left-side navigation pane, choose **Internal Global Traffic Manager** > **Scheduling**
**Line Management** > IP Address Line Configuration.
2. Find the line whose configurations you want to modify and click **Modify** in the Actions
column.
3. Modify the configurations as prompted and click **OK**.

#### 4.2.5 Delete a line

1. In the left-side navigation pane, choose **Internal Global Traffic Manager** > **Scheduling**
**Line Management > IP Address Line Configuration**.
2. Find the line that you want to delete and click **Delete** in the Actions column.
3. In the message that appears, click **OK**.

#### 4.2.6 Delete multiple global lines at a time

You can delete multiple global lines in the Apsara Stack Domain Name System (DNS) console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, click **Global Line**
3. On the Global Line page, select one or more lines and click **Batch Delete** below the line
list.
4. In the message that appears, click **OK**.

## 5 Private DNS

### 5.1 PrivateZone (DNS Standard Edition only)

**Edition only)**

The PrivateZone feature allows you to create VPC-specific tenant domain names. You can bind the domain names to VPCs as required to achieve tenant isolation.

#### 5.1.1 Tenant internal domain name

##### 5.1.1.1 View a domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. In the **Domain Name** search box, enter the domain name that you want to view.
4. Click Search.
The search result is displayed.

##### 5.1.1.2 Add a domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Click **Add Domain Name**.
4. In the dialog box that appears, set Tenant Internal Domain Name.
5. Click **OK**.

##### 5.1.1.3 Configure DNS records

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Configure DNS Records**.
4. In the upper-right corner of the **Configure DNS Records** page, click **Add DNS Record**.
5. In the **Add DNS Record** dialog box, configure Host, Type, TTL, Resolution Policy, and
Record Set. Then, click **OK**. The following tables describe the types of DNS records. A record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter up to 100 unique IPv4 addresses, each in a separate row. Make sure that the IPv4 addresses are valid. Example: 192.168.1.1 192.168.1.2 192.168.1.3 |
| Weight | You can enter up to 100 unique IPv4 addresses, each in a separate row. Format: [IPv4 address] [Weight] (The IPv4 address and weight are separated with a space.) Make sure that the IPv4 addresses are valid. The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight. Example: 192.168.1.1 20 192.168.1.1 30 192.168.1.1 50 |

AAAA record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter up to 100 unique IPv6 addresses, each in a separate row. Make sure that the IPv6 addresses are valid. Example: 2400:3200::6666 2400:3200::6688 2400:3200::8888 |
| Weight | You can enter up to 100 unique IPv6 addresses, each in a separate row. Format: [IPv6 address] [Weight] (The IPv6 address and weight are separated with a space.) Make sure that the IPv6 addresses are valid. The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight. Example: 2400:3200::6666 20 2400:3200::6688 20 2400:3200::8888 60 |

CNAME record

| Resolution policy | Formatting rule |
|---|---|

| None | You can enter only one domain name. The domain name must be a fully qualified domain name (FQDN) that ends with a dot (.). It must be 1 to 255 characters in length. Example: www.example.com. |
|---|---|
| Weight | You can enter up to 100 unique domain names, each in a separate row. Format: [Domain name] [Weight] (The domain name and weight are separated with a space.) The domain name must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight. Example: www1.example.com. 20 www2.example.com. 20 www3.example.com. 60 |

MX record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter 100 unique email server hostnames, each in a separate row. Format: [Priority] [Email server hostname] (The priority and hostname are separated with a space.) The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority. The email server hostname must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Example: 10 mailserver1.example.com. 20 mailserver2.example.com. |

TXT record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter up to 100 unique character strings, each in a separate row. A string must be 1 to 255 characters in length. No row can be left blank. Example: "v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all" |

PTR record

| Resolution policy | Formatting rule |
|---|---|

| None | You can enter up to 100 unique domain names, each in a separate row. The DNS server address must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Example: www1.example.com. www2.example.com. www3.example.com. |
|---|---|

SRV record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter up to 100 unique application server hostnames, each in a separate row. Format: [Priority] [Weight] [Port number] [Application server hostname] (Every two items are separated with a space.) The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority. The weight value is an integer ranging from 0 to 999. A larger value indicates a greater weight. The port number is an integer ranging from 0 to 65535. It indicates the TCP or UDP port used for network communications. The application server hostname must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Example: 1 10 8080 www1.example.com. 2 20 8081 www2.example.com. |

NAPTR record

| Resolution policy | Formatting rule |
|---|---|

| None | You can enter up to 100 unique NAPTR record values, each in a separate row. Format: [Serial number] [Priority] [Flag] [Service information] [Regular expression] [Substitute domain name] (Every two items are separated with a space.) The serial number is an integer ranging from 0 to 999. A smaller value indicates a higher priority. The priority value is an integer ranging from 0 to 999. A smaller value indicates a higher priority. If two records have the same serial number, the one with a higher priority takes effect first. The flag value can be left blank or be a character from A to Z, a to z, or 0 to 9. It is not case-sensitive and must be enclosed in double quotation marks (""). The service information can be left blank or be a string of 1 to 32 characters. It must start with a letter and be enclosed in double quotation marks (""). The regular expression can be left blank or be a string of 1 to 255 characters enclosed in double quotation marks (""). The substitute domain name must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Example: 100 50 "S" "Z3950+I2L+I2C" "" z3950. tcp.example.com. _ _ 100 50 "S" "RCDS+I2C" "" rcds. udp.example.com. _ _ 100 50 "S" "HTTP+I2L+I2C+I2R" "" http. tcp.example.com. _ _ |
|---|---|

CAA record

| Resolution policy | Formatting rule |
|---|---|
| None | You can enter up to 100 unique CAA records, each in a separate row. Format: [Certificate authority flag] [Certificate property tag] [Authorization information] (Every two items are separated with a space.) The certification authority flag is an integer ranging from 0 to 255. The certificate property tag can be issue, issuewild, or iodef. The authorization information must be 1 to 255 characters in length and enclosed in double quotation marks (""). Example: 0 issue "caa.example.com" 0 issuewild ";" 0 iodef "mailto:example@example.com" |

NS record

| Resolution policy | Formatting rule |
|---|---|

| None | You can enter up to 100 unique DNS server addresses, each in a separate row. The DNS server address must be an FQDN that ends with a period (.). It must be 1 to 255 characters in length. Wildcard domain names are not allowed. Example: ns1.example.com. ns2.example.com. |
|---|---|

6. After you add DNS records, perform the following operations as required:
Add a description for a DNS record. Find the target DNS record, click the icon in the Actions column, and then select
**Description**. In the dialog box that appears, enter a description and click **OK**.
Delete a DNS record. Find the target DNS record, click the icon in the Actions column, and then select
**Delete**. In the message that appears, click **OK**.
Modify a DNS record. Find the target DNS record, click the icon in the Actions column, and then select
**Modify**. In the dialog box that appears, modify the required parameters and click **OK**.
Delete multiple DNS records. Select the DNS records that you want to modify and click **Delete** in the upper-right corner. In the message that appears, click **OK**.

##### 5.1.1.4 Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. To ensure that the DNS forwarding configurations take effect, you must bind the organization of domain names to a VPC.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name, click the
icon in the Actions column, and select
**Associate VPCs**.
4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to
the list of VPCs Selected, and then click **OK**.

##### 5.1.1.5 Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name and click the number in the **VPCs Associated** column.
4. On the **VPCs Associated** page, find the target VPC, click the
icon in the **Actions** column, and then select **Disassociate**. Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

##### 5.1.1.6 Add a description for a domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Description**.
4. In the dialog box that appears, enter a description.
5. Click **OK**.

##### 5.1.1.7 Delete a domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Delete**.
4. In the message that appears, click **OK**.

##### 5.1.1.8 Delete multiple domain names at a time

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **Private DNS > Private Domain Name for VPC** in the left-side navigation pane.
3. On the Tenant Internal Domain Name tab of the page that appears, select one or more
tenant internal domain names that you want to delete and click **Batch Delete** below the domain names.
4. In the message that appears, click **OK**.

##### 5.1.1.9 View a resolution policy

This topic describes how to view the details of a resolution policy.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant Internal**
**Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select Configure DNS Records.
4. View the resolution policy in the DNS Records list.

#### 5.1.2 Tenant forwarding configurations

##### 5.1.2.1 Tenant forwarding domain names

###### 5.1.2.1.1 View a tenant forwarding domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. In the **Domain Name** search box, enter the domain name that you want to view.
4. Click **Search**.
The search result is displayed.

###### 5.1.2.1.2 Add a tenant forwarding domain name

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Click **Add Domain Name**.
4. In the dialog box that appears, configure parameters such as Domain Name, Forwarding
Mode, and Forwarder IP Addresses.

| Parameter | Description |
|---|---|

| Domain Name | The domain name, which must meet the following formatting rules: The domain name must be 1 to 255 characters in length. This includes the period (.) at the end of the domain name. The domain name can contain multiple domain name segments that are separated with periods (.). A domain name segment must be 1 to 63 characters in length. It cannot contain consecutive periods (.) or be left blank. The domain name can only contain letters (a to z, A to Z), digits (0 to 9), hyphens (-), and underscores ( ). _ The domain name must start with a letter, digit, or underscore ( ) and _ end with a letter, digit, or period (.). The domain name is not case-sensitive. The system saves the domain name in lowercase letters. The period (.) at the end of the domain name is optional. The system adds a period (.) to the end of the domain name. |
|---|---|
| Forwarding Mode | For both domain name-based forwarding and default forwarding, the following two forwarding modes are supported: Forward All Requests without Recursion: forwards DNS requests to the target DNS server. If the target DNS server cannot resolve the domain names, a message is returned to the DNS client indicating that the query failed. Forward All Requests with Recursion: A specified DNS server is preferentially used to resolve domain names. If the specified DNS server cannot resolve the domain names, the local DNS is used instead. If you enter internal IP addresses in the Forwarder IP Addresses field, unexpected results may occur during recursive resolution. For example, a domain name used for internal network services may be resolved to a public IP address. |
| Forwarder IP Addresses | A list of destination IP addresses. Note Multiple IP addresses are separated with semicolons (;). |

5. Click **OK**.

###### 5.1.2.1.3 Modify the forwarding configurations of a domain name

**a domain name**

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Modify**.
4. In the dialog box that appears, change the value of **Forwarding Mode** or **Forwarder IP**
**Addresses**.
5. Click **OK**.

###### 5.1.2.1.4 Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. You must bind the organization of domain names to a VPC before the DNS forwarding configurations can take effect.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Associate VPCs**.
4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to
the list of VPCs Selected, and then click **OK**.

###### 5.1.2.1.5 Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Find the target domain name and click the number in the **VPCs Associated** column.
4. On the VPCs Associated page, find the target VPC, click the
icon in the Actions column, and then select **Disassociate**. Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

###### 5.1.2.1.6 Add a description for a tenant forwarding domain name

**forwarding domain name**

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Find the target domain name, click the
icon in the Actions column, and then select
**Description**.
4. In the dialog box that appears, enter a description.
5. Click **OK**.

###### 5.1.2.1.7 Delete a tenant forwarding domain name

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. Choose **Private DNS > Private Domain Name for VPC** in the left-side navigation pane.
On the page that appears, click the Tenant Forwarding Configurations tab and click the
**Tenant Forwarding Domain Names** subtab.
3. Find the tenant forwarding domain name that you want to delete and click **Delete** in the
Actions column.
4. In the message that appears, click **OK**.

###### 5.1.2.1.8 Delete multiple tenant forwarding domain names

**domain names**

1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Forwarding Domains**.
3. Select one or more domain names that you want to delete and click **Delete** in the upper-
right corner.
4. In the message that appears, click **OK**.

##### 5.1.2.2 Tenant default forwarding configurations

###### 5.1.2.2.1 View default forwarding configurations

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.

###### 5.1.2.2.2 Add a default forwarding configuration

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Click **Add Settings**.
4. In the dialog box that appears, configure parameters such as Forwarding Mode and
Forwarder IP Addresses.

| Parameter | Description |
|---|---|
| Forwarding Mode | For both domain name-based forwarding and default forwarding, the following two forwarding modes are available: Forward All Requests without Recursion: Only a specified DNS server is used to resolve domain names. If the specified DNS server cannot resolve the domain names, a message is returned to the DNS client to indicate that the query failed. Forward All Requests with Recursion: A specified DNS server is preferentially used to resolve domain names. If the specified DNS server cannot resolve the domain names, a local DNS server is used instead. If you enter internal IP addresses in the Forwarder IP Addresses field, unexpected results may occur during recursive resolution. For example, a domain name used for internal network services may be resolved to a public IP address. |
| Forwarder IP Addresses | A list of destination IP addresses. Note Multiple IP addresses are separated with semicolons (;). |

5. Click **OK**.

###### 5.1.2.2.3 Bind an organization to a VPC

Tenant domain names are isolated based on VPCs. You must bind the organization of domain names to a VPC before the DNS forwarding configurations can take effect.

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Find the target organization, click the
icon in the Actions column, and then select
**Associate VPCs**.
4. Select one or more VPCs from the list of VPCs to Select, click the right arrow to add them to
the list of VPCs Selected, and then click **OK**.

###### 5.1.2.2.4 Unbind a domain name from a VPC

This topic describes how to unbind a domain name from a VPC.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Find the target domain name and click the number in the **VPCs Associated** column.
4. On the VPCs Associated page, find the target VPC, click the
icon in the Actions column, and then select **Disassociate**. Make sure that the unbound VPC is no longer displayed on the VPCs Associated page.

###### 5.1.2.2.5 Modify a default forwarding configuration

**configuration**

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Find the target organization, click the
icon in the Actions column, and then select
**Modify**.
4. In the dialog box that appears, change the value of **Forwarding Mode** or **Forwarder IP**
**Addresses**.
5. Click **OK**.

###### 5.1.2.2.6 Add a default forwarding configuration

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Find the target organization, click the
icon in the Actions column, and then select
**Description**.
4. In the dialog box that appears, enter **Description**.
5. Click **OK**.

###### 5.1.2.2.7 Delete a default forwarding configuration

**configuration**

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Find the target organization, click the
icon in the Actions column, and then select
**Delete**.
4. In the dialog box that appears, click **OK**.

###### 5.1.2.2.8 Delete multiple default forwarding configurations

**configurations**

**Prerequisites**

You have the permissions of a system administrator or level-1 organization administrator.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Forwarding Configurations > Tenant**
**Forwarding Settings > Tenant Default Forwarding**.
3. Select one or more domain names that you want to delete and click **Delete** in the upper-
right corner.
4. In the message that appears, click **OK**.

### 5.2 Private lines

Apsara Stack DNS allows you to define lines based on IP addresses on the Private Line page. The lines are used to group request sources to achieve intelligent load balancing. The lines can be referenced by private domain names for VPCs.

#### 5.2.1 Query private lines

You can query the list of private lines in the Apsara Stack Domain Name System (DNS) console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, click **Private Line**.
3. On the Private Line page, select **Line Name** or **IP** from the drop-down list, enter the
corresponding keyword in the search box, and then click the Search icon.

#### 5.2.2 Create a private line

1. Click **Query Source (Private Zone)** in the left-side navigation pane.
2. Click **Add Line** in the upper-left corner of the Private Line page.
3. In the Add Line dialog box, set the required parameters and click **OK**.

#### 5.2.3 Change the priority of a private line

1. Click **Query Source (Private Zone)** in the left-side navigation pane.
2. On the Private Line page, find the line whose priority you want to change and click **Sort** in
the Actions column.
3. In the Sort Line dialog box, specify a sorting method and click **OK**.

#### 5.2.4 Modify a private line

1. Click **Query Source (Private Zone)** in the left-side navigation pane.
2. On the Private Line page, find the line that you want to modify and click **Modify** in the
Actions column.
3. In the Modify Line dialog box, modify the parameters based on your business requirements
and click **OK**.

#### 5.2.5 Delete a private line

1. Click **Query Source (Private Zone)** in the left-side navigation pane.
2. On the Private Line page, find the line that you want to delete and click **Delete** in the
Actions column.
3. In the message that appears, click **Delete**.

#### 5.2.6 Delete multiple private lines at a time

You can delete multiple private lines at a time in the Apsara Stack Domain Name System (DNS) console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, click **Private Line**
3. On the Private Line page, select one or more private lines and click **Batch Delete** in the
lower-left corner of the page.
4. In the message that appears, click **OK**.

## 6 Global scheduling

### 6.1 Scheduling instances

The Scheduling Instance page displays all existing scheduling instances. You can create, delete, modify, and configure scheduling instances on this page. You must associate an address pool and a scheduling domain with the instance.

#### 6.1.1 Search for a scheduling instance

You can search for a scheduling instance in the Apsara Stack Domain Name System (DNS) console.
1. Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Global Scheduling > Scheduling Instance**.
3. On the **Scheduling Instance** page, enter the keyword of the desired scheduling instance
name. The desired scheduling instance is displayed.

#### 6.1.2 Create a scheduling instance

You must associate a scheduling instance with a scheduling domain and an address pool.
1. Log on to the Apsara Stack Domain Name System (DNS) console. In the left-side navigation
pane, choose **Global Scheduling > Scheduling Instance.**
2. On the page that appears, click **Create Scheduling Instance**.
3. In the Create Scheduling Instance dialog box, specify the parameters such as Scheduling
Instance Name, Scheduling Domain Name, Scheduling Domain, and Global TTL, and click **OK**.

#### 6.1.3 Modify the configurations of a scheduling instance

**scheduling instance**

1. Log on to the Apsara Stack Domain Name System (DNS) console. In the left-side navigation
pane, choose **Global Scheduling > Scheduling Instance.**
2. Find the instance whose configurations you want to modify and click **Modify** in the Actions
column.
3. In the dialog box that appears, modify the configurations of the scheduling instance as
instructed based on your business requirements and click **OK**.

#### 6.1.4 Configure a scheduling instance

You can create, delete, modify, and query access policies for scheduling instances.
1. Log on to the Apsara Stack Domain Name System (DNS) console. In the left-side navigation
pane, choose **Global Scheduling** > **Scheduling Instance**.
2. Find the instance that you want to configure and click **Edit** in the **Actions** column.
3. The Access Policy page displays the information about the access policies that you have
created for the scheduling instance in the **Name**, **DNS Query Sources**, **Address Pool in**
**Use, Switchover Policy, and Address Pool** columns.
4. Click the **+** icon before an access policy to view its details, including information about the
**primary and secondary address pools**.
5. Click Edit in the Actions column of the address policy that you want to modify. On the Edit
Access Policy dialog box, specify the **Address Pool Switchover Policy** parameter. The default value is **Automatic**. You can change the value to **Manual**. If you set the Address Pool Switchover Policy parameter to **Automatic**, the system automatically selects an available address pool. If you set the Address Pool Switchover Policy parameter to **Manual**, you must specify whether to use the **primary address pool** or **secondary address pool**.

> **Note:** Whether an address pool is available is determined based on the number of normal addresses in the address pool and the minimum number of available addresses in the address pool that you specify when you configure the access policy. If the number of normal addresses in the address pool is less than the specified minimum number of available addresses in the address pool, the address pool is considered unavailable. You can perform a health check to obtain the number of normal addresses in the address pool.

Processing logic for automatic switchover

| State of the primary address pool | State of the secondary address pool | Compariso n between the numbers of normal addresses in the primary and secondary address pools | Effective address pool (list of available addresses) |
|---|---|---|---|
| Available | Available | - | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Available | Unavailabl e | - | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Unavailabl e | Available | - | Secondary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |

| Unavailabl e | Unavailabl e | Number of normal addresses in the primary address pool > Number of normal addresses in the secondary address pool | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
|---|---|---|---|
| Unavailabl e | Unavailabl e | Number of normal addresses in the primary address pool < Number of normal addresses in the secondary address pool | Secondary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Unavailabl e | Unavailabl e | Number of normal addresses in the primary address pool = Number of normal addresses in the secondary address pool > 0 | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |

| Unavailabl e | Unavailabl e | Number of normal addresses in the primary address pool = Number of normal addresses in the secondary address pool = 0 | If the DNS request source is a custom line, the system clears the DNS configurations of the line instead of selecting an address pool. This means that the configurations of the custom line are deleted. If the DNS request source is the global default line, the system selects the primary address pool. This means that the system returns all the configured addresses without considering their return modes. |
|---|---|---|---|

When the system compares the numbers of normal addresses between the primary and secondary address pools, normal addresses include the normal addresses that are intelligently returned and all addresses that are always online (with the health status ignored). The abnormal addresses that are intelligently returned and all addresses that are always offline (with the health status ignored) are excluded. The following table describes the processing logic for address types if a line is selected in two access policies.

| Scenarios | Address type for the effective address pool in two access policies |   | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv6 | IPv4 and IPv6 addresses take effect at the same time. |
| Same DNS request source: Scenario 2 | IPv4 | Domain Name | Addresses of the domain name type take effect. |
| Same DNS request source: Scenario 3 | IPv6 | Domain Name | Addresses of the domain name type take effect. |

##### 6.1.4.1 Create an access policy for a scheduling instance

**instance**

You can create multiple access policies to resolve different address pools based on different DNS request sources.
1. Log on to the Apsara Stack DNS console. In the left-side navigation pane, click Internal
Global Traffic Manager. On the Scheduling Instances tab of the Global Traffic Management on the Internal Network page, find the scheduling instance for which you want to create an access policy and click Configure in the Actions column. On the page that appears, click
**Create Access Policy**.
2. In the Create Access Policy dialog box, specify **Access Policy Name**, select items in the
**DNS Request Source** section, and then configure parameters in the **Primary/Secondary**
**Address Pool Configuration** section. In the DNS Request Source section, if you select
Global default, you cannot select other items. The parameters on the Primary Address Pool tab must be configured, and the parameters on the Secondary Address Pool tab can be left empty.
3. In the **Primary/Secondary Address Pool Configuration** section, you can set **Address**
**Type** to IPv4, IPv6, or Domain Name to select different types of address pools. You can also
set **Min. Number of Available Addresses**. If the number of healthy addresses in an address pool is less than the value of this parameter, the address pool is determined to be unavailable. The value of Min. Number of Available Addresses must be an integer ranging from 1 to 100.
4. Click **OK**.
The following table describes the limits on address type conflicts between the primary and secondary address pools for two access policies that have the same DNS request source.

| Scenario | Address type of the primary address pool (access policy 1) | Address type of the secondary address pool (access policy 2) | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv4 | The address pools are allowed to be added. |
| Same DNS request source: Scenario 2 | IPv4 | IPv6 | The address pools are not allowed to be added. |
| Same DNS request source: Scenario 3 | IPv4 | Domain name | The address pools are allowed to be added. |
| Same DNS request source: Scenario 4 | IPv6 | IPv4 | The address pools are not allowed to be added. |
| Same DNS request source: Scenario 5 | IPv6 | IPv6 | The address pools are allowed to be added. |
| Same DNS request source: Scenario 6 | IPv6 | Domain name | The address pools are allowed to be added. |
| Same DNS request source: Scenario 7 | Domain name | IPv6 | The address pools are allowed to be added. |
| Same DNS request source: Scenario 8 | Domain name | IPv4 | The address pools are allowed to be added. |
| Same DNS request source: Scenario 9 | Domain name | Domain name | The address pools are allowed to be added. |

The following tables describe the limits on address type conflicts between the primary address pools and those between the secondary address pools for two access policies that have the same DNS request source.

| Scenario | Address type of the primary address pool (access policy 1) | Address type of the primary address pool (access policy 2) | Processing logic |
|---|---|---|---|

| Same DNS request source: Scenario 1 | IPv4 | IPv6 | The address pools are allowed to be added and they can coexist. |
|---|---|---|---|
| Same DNS request source: Scenario 2 | IPv4 | IPv4 | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 3 | IPv4 | Domain name | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 4 | IPv6 | IPv6 | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 5 | Domain name | IPv6 | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 6 | Domain name | Domain name | The address pools are allowed to be added and they can coexist. However, the following conditions must be met: (1) The two primary address pools are the same. (2) Both of the secondary address pools exist. In addition, one secondary address pool is of the IPv4 type and the other is of the IPv6 type. |

| Scenario | Address type of the secondary address pool (access policy 1) | Address type of the secondary address pool (access policy 2) | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv6 | The address pools are allowed to be added and they can coexist. |
| Same DNS request source: Scenario 2 | IPv4 | IPv4 | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 3 | IPv4 | Domain name | The address pools are not allowed to be added and they cannot coexist. |
| Same DNS request source: Scenario 4 | IPv6 | IPv6 | The address pools are not allowed to be added and they cannot coexist. |

| Same DNS request source: Scenario 5 | Domain name | IPv6 | The address pools are not allowed to be added and they cannot coexist. |
|---|---|---|---|
| Same DNS request source: Scenario 6 | Domain name | Domain name | The address pools are allowed to be added and they can coexist. However, the following conditions must be met: (1) The two secondary address pools are the same. (2) Both of the two primary address pools exist. In addition, one primary address pool is of the IPv4 type and the other is of the IPv6 type. |

##### 6.1.4.2 Modify the access policy of a scheduling instance

**instance**

> **Important:** If you do not change the primary or secondary address pool when you modify an access policy, no primary/secondary switchover is triggered. If you change one of the address pools, the system complies with the following processing rules:

1. Manual switchover mode: If the secondary address pool is deleted, the system forcibly
switches services to the primary address pool. If the secondary address pool is not deleted, the effective address pool does not change.
2. Automatic switchover mode: The system determines the address pool that takes effect
based on the status of the newly selected address pools. Exercise caution when you change the address pools.
1. On the Access Policy Configuration page, find the access policy that you want to modify and
click **Modify** in the Actions column.
2. In the Modify Access Policy dialog box, modify **Access Policy Name**, select items in the
**DNS Request Source** section, and then configure parameters in the **Primary/Secondary**
**Address Pool Configuration** section. In the DNS Request Source section, if you select
Global default, you cannot select other items. The parameters on the Primary Address Pool tab must be configured, and the parameters on the Secondary Address Pool tab can be left empty.
3. In the Primary/Secondary Address Pool Configuration section, you can set **Address Type** to
IPv4, IPv6, or Domain Name to select address pools of different types. You can also set Min. Number of Available Addresses. If the number of healthy addresses in an address pool is less than the value of this parameter, the address pool is determined to be unavailable. The value of this parameter must be an integer ranging from 1 to 100.
4. Click **OK**.

##### 6.1.4.3 Delete the access policy of a scheduling instance

**instance**

1. On the Access Policy Configuration page, find the target access policy and click Delete in
the Actions column.
2. In the dialog box that appears, click OK after you verify that the displayed information is
correct.

#### 6.1.5 Delete a scheduling instance

1. Log on to the Apsara Stack Domain Name System (DNS) console. In the left-side navigation
pane, choose **Global Scheduling > Scheduling Instance**.
2. Find the instance that you want to delete and click **Delete** in the Actions column.
3. In the message that appears, click **OK**.
> **Note:** After you delete the instance, its configuration data is also deleted.


### 6.2 Address pool

You can manage address pools on the Address Pool page. For example, you can associate address pools with the access policies of scheduling instances. Address pools are categorized into the following three types: IPv4, IPv6, and domain name. The Load Balancing Policy (Among Addresses) of an address pool can be set to Round-robin Scheduling or Weight.
1. Log on to the Apsara Stack DNS console. For more information, see Log on to the Apsara
Stack DNS console.
2. In the left-side navigation pane, choose **Global Scheduling** > **Address Pool**.
3. The Address Pool page displays information about the created address pools in the Address
Pool Name/ID, Address Type, Load Balancing Policy, Addresses, Created At, and Last Modified At columns. You can also click the options in the Actions column to perform specific operations on an address pool.
4. Click the plus icon (+) before an address pool. In the section that appears, you can view the
addresses in the address pool as well as the return modes and health status of the addresses.

#### 6.2.1 Search for address pools

This topic describes how to search for address pools.
1. Log on to the Apsara Stack Domain Name System (DNS) console.
2. In the left-side navigation pane, choose **Global Scheduling > Address Pool**.
3. On the **Address Pool** page, select **Address Pool Name** or **Include IP Addresses** from
the drop-down list, and then enter a keyword for search. Alternatively, click **Advanced**
**Filter**, specify **Address Pool Name** or **Include IP Addresses**, and then click Search.

#### 6.2.2 Create an address pool

You can define a list of addresses that form an address pool, which can be associated with the access policies of scheduling instances when you configure the access policies.
1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Global Scheduling > Address Pool.**
3. On the Address Pool page, click **Create Address Pool**.
4. In the Create Address Pool dialog box, specify the **Address Pool Name**, **Address Type**,
and **Load Balancing Policy (Among Addresses)** parameters, add addresses one by one in the **Addresses** section, and then click **OK**. The following table describes some of the required parameters.

| Parameter | Description |
|---|---|
| Address Pool Name | The name of the address pool. The name can be up to 20 characters in length. |
| Address Type | The address type of the address pool. You can select IPv4, IPv6, or Domain Name from the drop-down list. You cannot modify this parameter after you create the address pool. |
| Load Balancing Policy (Among Addresses) | The load balancing policy of the address pool. You can select Round-robin Scheduling or Weight from the drop-down list. You cannot modify this parameter after you create the address pool. |
| Mode | The mode of the added address. Valid values: Automatically Returned: The system determines whether the address is available based on the health check result of the address. Always Online: The system ignores the health check result of the address and sets the address to be always available. The health check task is still running. Always Offline: The system ignores the health check result of the address and sets the address to be always unavailable. The health check task is still running. |

#### 6.2.3 Modify the configurations of an address pool

### address pool

> **Important:** After you modify the configurations of an address pool, the health check results of all addresses in the address pool are reset to normal if the health check feature is enabled. If the address pool has been associated with specific access policies and automatic switchover is enabled, a primary/secondary switchover may be triggered. Proceed with caution when you modify the configurations of an address pool.

1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Global Scheduling** > **Address Pool**.
3. On the Address Pool page, find the address pool that you want to modify and click **Modify**
in the Actions column.
4. In the Modify Address Pool dialog box, modify the parameters. Only the **Address Pool**
**Name** parameter and the addresses specified in the **Addresses** section can be modified.
5. Click **OK**.

#### 6.2.4 Delete an address pool

1. Log on to the Apsara Stack Domain Name System (DNS) console. In the left-side navigation
pane, choose **Global Scheduling** > **Address Pool**.
2. On the Address Pool page, find the address pool that you want to delete and click **Delete** in
the Actions column.
3. In the message that appears, click **OK**.

#### 6.2.5 Create a health check task for an address pool

### address pool

You can perform health checks on the addresses in an address pool. Only the addresses whose health check result is normal can be returned.
1. Log on to the Apsara Stack Domain Name System (DNS) console. For more information, see
Log on to the Apsara Stack DNS console.
2. In the left-side navigation pane, choose **Global Scheduling** > **Address Pool**.
3. Find the address pool for which you want to create a health check task and click **Health**
**Check** in the Actions column.
4. On the Health Check page, click **Create Health Check Task**. In the Create Health Check
Task dialog box, turn on **Health Check** based on your business requirements, set the remaining parameters, and then click **OK**. The following table describes the parameters.

| Item | Parameter | Description | Supported protocols |
|---|---|---|---|
|   | Port | The port number that is used for health checks on the address pool. The value must be an integer in the range of 1 to 65535. This parameter cannot be empty. | HTTP, HTTPS, TCP, and UDP |
|   | URL | The HTTP or HTTPS path that is used for health checks on the address pool. This path is used to check whether the HTTP or HTTPS service of an address in the address pool is normal. If the HTTP status code returned from this path is 2xx or 3xx, the HTTP or HTTPS service is normal. The system automatically adds a forward slash (/) before the path. The path can be empty. The default value is /. The path can be up to 255 characters in length. | HTTP and HTTPS |

| Protocol Settings |   |   |   |
|---|---|---|---|
|   | Host Settings | The host configuration that is used for health checks. If you do not specify this parameter, the primary domain name is used. | HTTP and HTTPS |
|   | Returned Code Greater Than | The minimum value of the HTTP status code when the health check result is abnormal. The system determines that the result of a health check is abnormal if the HTTP status code returned is greater than or equal to the value of this parameter. | HTTP and HTTPS |
|   | ICMP Packages Sent | The number of Internet Control Message Protocol (ICMP) packets sent each time an ICMP health check is performed. | ICMP |
|   | Packet Loss Rate | The threshold of the packet loss rate. The threshold is used to determine whether the result of an ICMP health check is abnormal. | ICMP |
| Health check settings | Interval | The time interval at which health checks are performed on the address pool. |   |
|   | Timeout Period | The timeout period for which the system waits after an exception occurs. |   |
|   | Number of Retries | The minimum number of consecutive health check retries before the status of an address is considered abnormal. |   |
| Node Settings | Physical Network | The nodes that initiate health checks on the address pool. |   |
|   | VPC |   |   |

## 7 System management

### 7.1 Nodes

The Nodes page displays the DNS servers that serve as nodes. On this page, you can monitor the role and status of each node and check data consistency after synchronization.

#### 7.1.1 View a node

1. Click **Nodes** in the left-side navigation pane.
2. On the Nodes page, find the node that you want to view and check the information
displayed in the **Service Instance IP Address**, **Service Instance Role**, **Working Mode**,
**Working Status**, **Latest Synchronization Log ID**, **Service Address**, and **Description**
columns. You can also view the operations that you can perform on the node in the **Actions** column.

#### 7.1.2 Configure the emergency group feature

1. Click **Nodes** in the left-side navigation pane.
2. Click **Create Emergency Group** in the upper-left corner of the Nodes page.
3. In the Create Emergency Group dialog box, turn on or off **Emergency Group** based on
your business requirements. If you turn on the switch, you need to set the Service Instance parameter.

#### 7.1.3 Add a description for a node

1. Click **Nodes** in the left-side navigation pane.
2. Find the node for which you want to add a description based on IP addresses and click **Add**
**Description** in the Actions column. In the Add Description dialog box, enter a description in
the Add Description field and click OK.

#### 7.1.4 Set a follower node as the leader node

1. Click **Nodes** in the left-side navigation pane.
2. Find the follower node that you want to set as the leader node based on IP addresses and
click **Switch Primary Node** in the Actions column. In the message that appears, click **OK**. Then, the system sets the selected node as the new leader of the cluster for data synchronization.

### 7.2 Logs

The Logs page displays the alert information about the DNS server cluster.

#### 7.2.1 Query alert logs

1. Click **Logs** in the left-side navigation pane.
2. On the Logs page, select the type of alert log that you want to query from the drop-down
list in the upper-left corner. You can select **All, Primary/Secondary Address Pool**

**Switchover, Address Pool Unavailable, The address pool becomes available,**

**Address Unavailable, or Address Restored to Available**. Then, enter a keyword in the
search box, specify the start and end time for the query, and then click **Search**.
3. Check the information displayed in the **Time**, **Object**, **Behavior**, and **Content** columns.
