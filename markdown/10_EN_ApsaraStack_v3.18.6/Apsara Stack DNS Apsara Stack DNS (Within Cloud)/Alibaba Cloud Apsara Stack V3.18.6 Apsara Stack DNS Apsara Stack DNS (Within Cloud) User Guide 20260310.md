---
title: "Apsara Stack DNS Apsara Stack DNS (Within Cloud) User Guide 20260310"
product_version: "V3.18.6"
pdf_pages: 66
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack DNS Apsara Stack DNS (Within Cloud) User Guide 20260310.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E8%A7%A3%E6%9E%90DNS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20DNS%20Apsara%20Stack%20DNS%20%28Within%20Cloud%29%20User%20Guide%2020260310.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara Stack DNS Apsara Stack DNS (Within Cloud) User Guide 20260310

DNS?

## What is Apsara Stack DNS?

Apsara Stack DNS is a service that provides Domain Name System (DNS) resolution in an Apsara Stack environment. It lets you set rules and policies to map domain names to IP addresses, which redirects domain name requests from clients to resources such as cloud resources, business systems on a corporate intranet, or service resources from an Internet Service Provider (ISP). Apsara Stack DNS provides basic DNS resolution and scheduling services for Virtual Private Cloud (VPC) environments. You can use Apsara Stack DNS in your VPC to perform the following operations: Access other ECS instances deployed in your VPC. Access cloud service instances provided by Apsara Stack. Access custom enterprise business systems. Access Internet services and businesses. Establish network connections between DNS and user-created DNS over a leased line.

| Role | Permission |
|---|---|
| System administrator | A user of this role has read, write, and execute permissions on all level-1 organization resources, global resources, and system configurations. |
| Level-1 organization administrator | A user of this role has read, write, and execute permissions on level-1 organization resources to which the user belongs, but does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Lower-level organization administrator | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Resource user | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Other roles | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |

## User roles and permissions

## Log on to the Apsara Stack

**DNS console**

This topic describes how to log on to the Apsara Stack DNS console using Google Chrome.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

**Note**

You can select a language from the drop-down list in the upper-right corner of the page. 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

**Forgot password**

If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For information about how to bind and enable MFA, see the **Security Center** >
**Multi-factor Authentication** > **Manage Multi-factor Authentication** section in
the Apsara Uni-manager Management Console User Guide.
5. In the top menu bar, choose **Products > Network > Alibaba Cloud DNS**.

| Parameter | Description |
|---|---|

## DNS within cloud

### Internal DNS resolution

**management**

Internal DNS resolution management allows you to manage global internal domain names, global forwarding configurations, and global recursive resolution configurations that you have created in Apsara Stack.

#### Overview

This feature is designed for multicloud integration scenarios. It syncs configuration information globally across multiple clouds to provide global domain name resolution for all applications.

#### Global internal domain names

##### Add and manage global internal domain

**names**

This topic describes how to add and manage global internal domain names.

**Add a domain name**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Intra-cloud Global Domain Name** page, click the **Global Internal Domain**
**Name** tab.
4. Click the **Add Domain Name** button.
5. In the **Add Global Internal Domain Name** dialog box, configure the domain name based
on the following information.

| Global Internal Domain Name | Enter the global internal domain name. Note i. A domain name cannot exceed 220 characters in length, including the trailing period (.). ii. A domain name consists of segments separated by periods (.). Each segment cannot exceed 63 characters and cannot be empty. This means you cannot use consecutive periods. iii. A domain name can contain only letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores ( ). Other characters are not _ allowed. iv. Domain names are not case-sensitive. v. The domain name must end with a period (.). |
|---|---|
| Current Domain Name Type | Select the type of the current domain name. Primary Domain Name Secondary Domain Name |
| DNS Server Address Of Primary Domain Name | Enter the DNS server address of the primary domain name.T he DNS data is synchronized to the secondary domain name from this address. Enter one address per line. You can enter up to five addresses. Only IP addresses are supported. Both IPv4 and IPv6 addresses are supported. Use the ip:port format. Note This parameter is required only when you set Current Domain Name Type to Secondary Domain Name. |
| Enable TSIG Key Authentication | Select whether to enable TSIG key authentication. Note This parameter is available only when you set Current Domain Name Type to Secondary Domain Name. |

| TSIG Key Name | Enter the TSIG key name. The value must be an integer from 1 to 65535 and specified in a format such as "1/200" or "80/80". The value "-1/-1" represents unrestricted ports and cannot be set as a standalone value. Note This parameter is required if you enable TSIG Key Authentication. |
|---|---|
| TSIG Key Algorithm | Enter the TSIG key algorithm. Note This parameter is required if you enable TSIG Key Authentication. |
| TSIG Key Value | Enter the TSIG key value. Note This parameter is required if you enable TSIG Key Authentication. |

6. Click **OK**.

**More operations**

**View the domain list**

On the **Global Internal Domain Name** page, you can view a list of your added domain names. Use the **Advanced Filter** to perform a fuzzy search by **Domain Name**. Click the icon in the upper-right corner of the list to customize the list. You can show or hide columns and drag columns to change their order.

**Modify a domain name**

**Note**

Only secondary domain names can be modified. Primary domain names cannot be modified.
1. On the **Global Internal Domain Name** page, find the domain name that you want to
modify and click **Modify** in the **Actions** column.
2. In the **Modify Global Internal Domain Name** dialog box, modify the parameters and
click **OK**. For more information about the parameters, see Add a domain name.

**Add remarks to a domain name**

1. On the **Global Internal Domain Name** page, find the domain name to which you want to
add remarks and click **Add Remark** in the **Actions** column.
2. In the **Add Remark For Global Internal Domain Name** dialog box, enter a remark in the
**Remark** field and click **OK**.

**Delete a domain name**

**Note**

When a domain name is deleted, all its DNS records are also deleted. Proceed with caution.
1. (Method 1) On the **Global Internal Domain Name** page, find the domain name that you
want to delete. In the **Actions** column, click the icon and then click **Delete**. (Method 2) On the **Global Internal Domain Name** page, select the checkbox of one or more domain names that you want to delete, and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Global Internal Domain Name** page, click **Operation Logs** in the **Actions** column to view the operation logs for the corresponding domain name. For more information, see View operation logs.

##### Parsing configuration

###### Add and manage DNS records

You can configure parsing settings in the Apsara Uni-manager Management Console.

**Add a DNS record**

**Important**

You can add DNS records only for primary domain names. You cannot add DNS records for secondary domain names. The DNS data for a secondary domain name is synchronized from the DNS server of the primary domain name.
1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Intra-cloud Global Domain Name** page, click the **Global Internal Domain**
**Name** tab.
4. On the **Global Internal Domain Names** tab, find the target global domain name and click
the number in the **Total DNS Record Sets** column or **DNS Settings** in the **Actions** column.
5. On the DNS Settings page, click **Add DNS Record** in the upper-left corner.
6. On the **Add DNS Record** page, configure the DNS record as described below and click **OK**.

| Name | Description |
|---|---|
| Record Name | Enter a host record. The domain name is appended to the host record to form the full record name. Note A record name consists of a host record and a domain name. The host record, except for the single asterisk (*) character used for wildcard DNS, must meet the following format requirements: i. A domain name cannot exceed 254 characters in length, including the trailing period (.). ii. A domain name is divided into labels separated by periods (.). Each label cannot exceed 63 characters and cannot be empty. This means you cannot have consecutive periods. iii. A domain name can contain only uppercase letters (A–Z), lowercase letters (a–z), digits (0–9), hyphens (-), and underscores ( ). Other _ characters are not allowed. iv. A domain name must start with a letter, a digit, or an underscore ( ). It _ must end with a letter, a digit, or a trailing period (.). v. Domain names are not case-sensitive. vi. The trailing period (.) is optional. If you omit it, the system automatically adds it. For example, for the domain name `example.com.`, common DNS records are configured as follows: Website application: Leave the host record empty. The resolved domain name is `example.com.`. Website application: Set the host record to `www`. The resolved domain name is `www.example.com.`. Mail server: Set the host record to `mail`. The resolved domain name is `mail.example.com.`. Wireless application: Set the host record to `m`. The resolved domain name is `m.example.com.`. Mobile application: Set the host record to `webapp`. The resolved domain name is `webapp.example.com.`. Wildcard DNS: Set the host record to `*`. The resolved domain name is `*.example.com.`, which matches all subdomains of `example.com.`. Subdomain: Set the host record to `abc`. The resolved domain name is `abc.example.com.`. |
| Load Balancing Policy | Select a load balancing policy. You can select Polling or Weight. |

| Record Type | Select a record type. If you set Load Balancing Policy to Polling, you can select one of the following record types: A - Maps A Domain Name To An IPv4 Address AAAA - Maps A Domain Name To An IPv6 Address CNAME - Maps A Domain Name To Another Domain Name MX - Maps A Domain Name To A Mail Server Address TXT - Specifies A Text Record, Often Used For Sender Policy Framework (SPF) Records To Prevent Spam PTR - Maps An IP Address To A Domain Name For Reverse DNS Lookup SRV - Specifies A Server That Provides A Specific Service NAPTR - Specifies A Name Authority Pointer (NAPTR) Record, Which Is Often Used For E.164 Number Mapping (ENUM) CAA - Specifies Authorization Information For The Certificate Authority (CA) That Can Issue Certificates For A Domain NS - Delegates A Subdomain To A Specified DNS Server For Resolution If you set Load Balancing Policy to Weight, you can select one of the following record types: A - Maps A Domain Name To An IPv4 Address AAAA - Maps A Domain Name To An IPv6 Address CNAME - Maps A Domain Name To Another Domain Name |
|---|---|
| TTL (Seconds) | TTL is the amount of time that the DNS record is cached on a local DNS server. The value must be an integer from 0 to 2147483647. A value of 0 means the record is not cached. The default value is 300. If the endpoint of your service changes frequently, set a smaller TTL value. Otherwise, set a larger TTL value. |
| Resolution Line | Select the global line. You can select multiple lines. |

| Record Value Collection | Add a record value collection. Value: Enter a record value based on the selected Record Type. For information about the required format, see Record value format. Weight: Enter a weight. The value must be an integer from 0 to 999. A larger value indicates a higher proportion of DNS requests that are forwarded to the record value. This parameter is required only when you set Load Balancing Policy to Weight. Note Click Add Entry to add multiple record values. Click the in the Actions column of the target record value to delete the record value. |
|---|---|

| Record type | Record value format requirements |
|---|---|
| A - Maps a domain name to an IPv4 address | Enter one IPv4 address per line. You can enter up to 100 unique record values. Format requirement: A standard IPv4 address. Examples: 192.168.1.1 192.168.1.2 192.168.1.3 |
| AAAA - Maps a domain name to an IPv6 address | Enter one IPv6 address per line. You can enter up to 100 unique record values. Format requirement: A standard IPv6 address. Examples: 2400:3200::6666 2400:3200::6688 2400:3200::8888 |
| CNAME - Maps a domain name to another domain name | Enter only one domain name. Format requirement: A fully qualified domain name (FQDN) that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Example: www.example.com. |

**Record value format**

| MX - Maps a domain name to a mail server address | Enter one mail server entry per line. You can enter up to 100 unique record values. Format requirement: `[Priority] [Mail server hostname]` Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Mail server hostname: An FQDN that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Examples: 10 mailserver1.example.com. 20 mailserver2.example.com. |
|---|---|
| TXT - Specifies a text record, often used for Sender Policy Framework (SPF) records to prevent spam | Enter one text string per line. You can enter up to 100 unique record values. Format requirement: The text string cannot be empty and can contain up to 254 ASCII characters. Example: v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all |
| PTR - Maps an IP address to a domain name for reverse DNS lookup | Enter one domain name per line. You can enter up to 100 unique record values. Format requirement: An FQDN that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Examples: www1.example.com. www2.example.com. www3.example.com. |
| SRV - Specifies a server that provides a specific service | Enter one application service entry per line. You can enter up to 100 unique record values. Format requirement: `[Priority] [Weight] [Port] [Application server hostname]` Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Weight: An integer from 0 to 999. A larger value indicates a higher proportion of traffic. Port: An integer from 0 to 65535. This indicates the TCP or UDP port. Application server hostname: An FQDN that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Examples: 1 10 8080 www1.example.com. 2 20 8081 www2.example.com. |

| NAPTR - Specifies a Name Authority Pointer (NAPTR) record, which is often used for E.164 Number Mapping (ENUM) | Enter one NAPTR record per line. You can enter up to 100 unique record values. Format requirement: `[Order] [Preference] [Flags] [Service] [Regular expression] [Replacement]` Order: An integer from 0 to 999. Records with smaller values are processed first. Preference: An integer from 0 to 999. For records with the same Order value, records with smaller Preference values are processed first. Flags: This field can be empty. It must be a single character from A to Z, a to z, or 0 to 9. The flag is not case-sensitive and must be enclosed in double quotation marks (""). Service: This field can be empty. It can contain up to 32 ASCII characters, must start with a letter, and must be enclosed in double quotation marks (""). Regular expression: This field can be empty. It can contain up to 255 ASCII characters and must be enclosed in double quotation marks (""). Replacement: An FQDN that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Examples: 100 50 "S" "Z3950+I2L+I2C" "" z3950. tcp.example.com. _ _ 100 50 "S" "RCDS+I2C" "" rcds. udp.example.com. _ _ 100 50 "S" "HTTP+I2L+I2C+I2R" "" http. tcp.example.com. _ _ |
|---|---|
| CAA - Specifies authorization information for the certificate authority (CA) that can issue certificates for a domain | Enter one CAA record per line. You can enter up to 100 unique record values. Format requirement: `[Flag] [Tag] [Value]` Flag: An integer from 0 to 255. Tag: The valid values are `issue`, `issuewild`, and `iodef`. Value: This field cannot be empty. It can contain up to 254 ASCII characters and must be enclosed in double quotation marks (""). Examples: 0 issue "caa.example.com" 0 issuewild ";" 0 iodef "mailto:example@example.com" |

| NS - Delegates a subdomain to a specified DNS server for resolution | Enter one DNS server address per line. You can enter up to 100 unique record values. Format requirement: An FQDN that ends with a period (.). The FQDN can contain up to 254 ASCII characters. Wildcard domain names are not allowed. Examples: ns1.example.com. ns2.example.com. |
|---|---|

**More operations**

After you add a DNS record, you can perform the following operations in the list of DNS records. Query DNS records Advanced filtering is supported. You can perform a fuzzy search by entering a value in the
**Record Name** field.
View load balancing policy (weight) Find the target DNS record. In the **Load Balancing Policy** column, click **Weight**. In the dialog box that appears, view the details of the configured load balancing policy. Modify a DNS record In the list of DNS records, find the target DNS record. In the **Actions** column, click **Modify**. Modify the information as described in Add a DNS record, and then click **OK**. Add a description to a DNS record Find the target DNS record, click **Add Description** in the **Actions** column, enter a description in the **Description** field, and then click **OK**. Delete a DNS record Find the target DNS record. In the **Actions** column, click **Delete**, and then click **OK**. Delete multiple DNS records at a time Select the DNS records that you want to delete. In the lower-left corner, click **Batch**
**Delete**, and then click **OK**.

#### Global forwarding configurations

##### Overview

All operations on global forwarding domain names require system administrator permissions. Apsara Stack DNS forwards specific domain names to other DNS servers for resolution. Apsara Stack DNS can forward requests with or without recursion. In the mode of forwarding without recursion, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails. In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used.

##### Global forwarding domain names

| Configuration Parameters | Description |
|---|---|
| Global Forwarding Domain Name | Enter the global forwarding domain name. The domain name must meet the following format requirements: The domain name can be up to 254 characters long, including the period (.) at the end. The domain name can contain multiple segments separated by periods (.). Each segment can be up to 63 characters long and cannot be empty. This means you cannot use consecutive periods (..). The domain name can contain only letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores ( ). Other characters are not allowed. _ The domain name must start with a letter, digit, or underscore ( ). It _ must end with a letter, digit, or a period (.). The domain name is not case-sensitive. The domain name must end with a period (.). |

###### Add and manage forwarding domain

**names**

In the Apsara Uni-manager Management Console, you can add and manage global forwarding domain names. This operation requires administrator permissions.

**Add a domain name**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Global Domain Names** page, go to **Global Forwarding Configuration > Global**
**Forwarding Domain Name List**.
4. On the **Global Forwarding Domain Name List** tab, click **Add Domain Name**.
5. In the **Add Global Forwarding Domain Name** dialog box, configure the domain name
based on the following information, and then click **OK**.

| Forwarding Mode | Select a forwarding mode. Two forwarding modes are supported for both domain-based forwarding and default forwarding. Forward All Mode (Recommended) - All Requests Are Forwarded Only (no Recursion): Forwards DNS queries only to the destination DNS server. If the server cannot resolve the domain name, a failure message is returned to the client. Forward First Mode - Degrades To Internet Recursion On Forwarding Failure: Tries to use the destination DNS server first for domain name resolution. If the query fails, the local DNS server performs a recursive query over the Internet. Important Threat reminder: If the destination IP addresses are all internal IP addresses, degrading to an Internet recursive query may produce unexpected results. For example, a domain name used for an internal service might be resolved to a public IP address. |
|---|---|
| Destination IP Address | Enter the list of destination IP addresses. Format requirements: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv4 or IPv6 address per line. You can enter up to five unique IP addresses. |

**More operations**

**Note**

Global forwarding domain names forwarded to ops cannot be modified or deleted. You can modify, add remarks to, and delete user-defined domain names.

**View the domain name list**

On the Global Forwarding Domain Name List tab, you can view the domain names that you have added. Use the **Advanced Filter** to perform a fuzzy search by **Domain Name**. Click the icon in the upper-right corner of the list to show or hide columns. You can also drag columns to reorder them.

**Note: Domain Names**

You can add remarks to a domain name to specify its purpose, such as its function as a hostname or its use for an internal information system.
1. On the **Global Forwarding Domain Name List** tab, find the target domain name and
click **Remark** in the **Actions** column.
2. In the **Modify Global Forwarding Domain Name** dialog box, change the **Forwarding**
**Mode** or **Destination IP Address**, and then click **OK**.

**Modify a domain name**

1. On the **Global Forwarding Domain Names List** tab, click **Modify** in the **Actions** column
for the target domain name.
2. In the **Modify Global Forwarding Domain Name** dialog box, enter a description in the
**Remarks** field, and click **OK**.

**Delete a domain name**

1. (Method 1) On the **Global Forwarding Domain Name List** tab, find the target domain
name and click
**> Delete** in the **Actions** column.
(Method 2) On the **Global Forwarding Domain Name List** tab, select the checkbox for one or more domain names that you want to delete, and then click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Global Forwarding Domain Name List** tab, click **Operation Logs** in the **Actions** column to view the operation logs for the target domain name. For more information, see View operation logs.

##### Global default forwarding configuration

You can enable or disable default forwarding in the Apsara Uni-manager Management Console. This operation requires administrator permissions.

**Procedure**

**Note**

If you disable default forwarding, DNS requests for external domain names are not sent to the forwarding server.
1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Global Domain Names** page, click the **Global Forwarding Configurations >**
**Global Default Forwarding Configurations**.
4. Configure global default forwarding as follows.

| Parameter | Description |
|---|---|
| Enable Default Forwarding | Specifies whether to enable default forwarding. |
| Default Forwarding Mode | If you enable default forwarding, select a forwarding mode. Two forwarding modes are supported for both domain name-based forwarding and default forwarding. Force Forwarding Mode (Recommended) - Forwards All Requests Without Recursion: Forwards DNS requests only to the destination DNS server for domain name resolution. If the query fails to return a result, a failure message is sent to the client. Forward First Mode - Degrades To Internet Recursion On Failure: Preferentially uses the destination DNS server for domain name resolution. If the query fails to return a result, the local DNS server performs a recursive query over the Internet. Important Warning: If all destination IP addresses are internal IP addresses, degrading to an Internet recursive query may produce unexpected results. For example, a domain name for an internal service might be resolved to a public IP address. |
| Destination IP Address | If you enable default forwarding, enter a list of destination IP addresses. Format requirements: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv4 or IPv6 address per line. You can enter up to five unique IP addresses. |
| Last Modified Time | Displays the time when the global default forwarding configuration was last modified. |

5. Click **Submit**.

#### Global recursive resolution

| Parameter | Description |
|---|---|
| ACL Policy Name | Enter a name for the ACL policy. The name must be globally unique within the recursive ACL list. For more information about naming conventions, see "Basic UI interaction conventions". |
| Request Source | Select one or more request sources. You can only select lines that are configured in the global line settings. Custom lines are mutually exclusive. If a custom line is already in use, you cannot select it. |
| Enable Recursion | Select whether to turn on the Enable Recursion switch. |
| Description | Enter a description. |

##### Overview

Recursive access control list (ACL) policies are used to specify whether to recursively send DNS requests to the Internet.

**Note**

Recursive resolution defined in such ACL policies takes precedence over global recursive resolution.

##### Recursive ACL policy

###### Add and manage ACL policies

You can add and manage access control list (ACL) policies in the Apsara Uni-manager Management Console. This operation requires administrator permission.

**Add an ACL policy**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Global Domain Name Within Cloud** page, choose **Global Recursive**
**Configuration > Recursive ACL Policy**.
4. Click **Add ACL Policy**.
5. In the **Add ACL Policy** dialog box, configure the parameters.
5. Click **OK**.

**More operations**

After you add an ACL policy, you can perform the following operations on the **Recursive ACL**
**Policy** tab.
Query ACL policies Use the **Advanced Filter** and enter an **ACL Policy Name** to perform a fuzzy search. Click the icon in the upper-right corner of the list to show or hide columns, and drag columns to reorder them. Modify an ACL policy Find the target policy and click **Modify** in the **Operation** column. In the dialog box that appears, modify the parameters as described in Add an ACL policy, and then click **OK**. Add a description to an ACL policy Find the target policy and click **Description** in the **Operation** column. In the dialog box that appears, enter a **Description**, and then click **OK**. Delete ACL policies Single deletion: Find the target policy and click **Delete** in the **Operation** column, and then click **OK**. Batch deletion: Select the policies to delete, click **Batch Delete** in the lower-left corner of the page, and then click **OK**. Find the target policy and click **Operation Logs** in the **Operation** column to view its operation logs. For more information, see View operation logs.

##### Global default recursive configuration

**Prerequisites**

Only system administrators have permission to manage the recursion configuration.

**Procedure**

**Note**

Enabling recursive resolution lets you perform recursive queries, such as resolving domain names on the Internet. Disabling recursive resolution blocks recursive queries, such as resolving domain names on the Internet.
1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Global Domain Name Within Cloud** page, choose **Global Recursive**
**Configuration > Global Default Recursion**.
4. Turn the switch next to **Global Recursive Resolution** on or off, and then click **Submit**.

#### Cache management

| Parameter | Description |
|---|---|
| Service Instance | Select a service instance. You can select only learner nodes from node management. The name is displayed in the following format: Resolution Node (Service Instance IP address). |
| Domain Name | Enter a domain name. |
| Domain Name Matching Method | Select a domain name matching method. Suffix Match: Clears the cache for all domain names with the specified suffix. Exact Match: Clears the cache only for the domain name that you entered. |

Domain names queried using global forwarding or recursion are cached. You can view and clear the cache in the Apsara Uni-manager Management Console. This operation requires administrator permissions.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Intra-cloud Domain Name Service > Intra-**
**cloud Global Domain Name**.
3. On the **Global Domain Name Within Cloud** page, click the **Cache Management** tab to
view the cache list. You can filter the cache list by selecting a **Type** or entering a **Domain Name**.
4. You can clear the cache.
Click **Clear Cache**. In the **Clear Cache** dialog box, configure the following parameters, and then click **OK**.

### IP Address Line Configuration

The IP Address Line Configuration tab allows you to define lines based on IP addresses. The lines are used to group request sources to achieve intelligent load balancing.

#### Add and manage global lines

In the Apsara Uni-manager Management Console, you can add global lines.

**Add a line**

1. Log on to the DNS console.
2. In the navigation pane on the left, select **Cloud DNS > Global Lines**.
3. On the **Global Lines** page, click **Add Line**.
4. In the **Add Line** dialog box, configure the global line.

| Parameter | Description |
|---|---|
| Line Name | Enter a name for the line. |
| Sorting Behavior | Select a Sorting Behavior. Insert At The Beginning Insert At The End Insert Before A Selected Line Note The sort number of a line determines its priority. A smaller number indicates a higher priority. |
| Insert Before This Line | Select the line before which you want to insert the new line. Note This parameter is required only when you set Sorting Behavior to Insert Before A Selected Line. |
| IPv4 Address Range | Enter the IPv4 address range. You must specify either an IPv4 Address Range or an IPv6 Address Range. Format: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Note Enter one IPv4 address per line. You can enter up to 1,000 lines. Duplicate addresses are not allowed. |

| IPv6 Address Range | Enter the IPv6 address range. You must specify either an IPv4 Address Range or an IPv6 Address Range. Format: Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv6 address per line. You can enter up to 1,000 lines. Duplicate addresses are not allowed. |
|---|---|

5. Click **OK**.

**Related operations**

After you add a global line, you can perform the following operations on the **Global Lines** page. Query global lines Use the **Advanced Filter** to perform a fuzzy search by **Line Name** or **IP**. Click the icon in the upper-right corner of the list to show or hide columns, or drag columns to reorder them. Modify a global line Find the line that you want to modify and click **Modify** in the **Actions** column. Change the
**Line Name**, **IPv4 Address Range**, or **IPv6 Address Range**, and then click **OK**.

**Note**

You must specify either an **IPv4 Address Range** or an **IPv6 Address Range**. Sorting global lines In the line that you want to reorder, click **Sort** in the **Actions** column. Then, select a
**Sorting Behavior** and click **OK**.
Delete a global line

**Important**

Before you can delete a line, you must dissociate it from all scheduling instances and global line parsing configurations. To delete a single line: Find the line and click **Delete** in the **Actions** column. Then, click
**OK**.
To delete multiple lines in a batch: Select the checkboxes of the lines that you want to delete. Click **Batch Delete** in the lower-left corner of the page. Then, click **OK**. Find the line and click **Operation Logs** in the **Actions** column. For more information, see View operation logs.

## Private DNS

### PrivateZone (DNS Standard

**Edition only)**

The PrivateZone feature allows you to create VPC-specific tenant domain names. You can bind the domain names to VPCs as required to achieve tenant isolation.

#### Tenant internal domain name

##### Add and manage tenant internal domain

**names**

**Add a domain name**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **VPC Private Domain Names** page, click the **Tenant Internal Domain Names**
tab.
4. Click the **Add Domain Name** button.
5. In the **Add Tenant Internal Domain Name** dialog box, configure the following
parameters and click **OK**.
**Organization**: Select an organization.
**Resource Set**: Select a resource set.
**Tenant Internal Domain Name**: Enter a tenant internal domain name, such as
example.com.

**More operations**

**View the list of domain names**

On the **Tenant Internal Domain Names** page, you can view the domain names that you have added. Enter filter conditions in the advanced search box to find a specific domain name. Click the icon in the upper-right corner of the list to show or hide columns, and drag the columns to change their order.

**Add a remark to a domain name**

1. On the **Tenant Internal Domain Names** page, find the target domain name and click
**Add Remark** in the **Actions** column.
2. In the **Add Remark** dialog box, enter a remark in the **Remark** field and click **OK**.

**Delete a domain name**

| Name | Description |
|---|---|

1. (Method 1) On the **Tenant Internal Endpoints** page, find the target domain name, and
click
**> Delete** in the **Actions** column.
(Method 2) On the **Tenant Internal Domain Names** page, select one or more domain names that you want to delete, and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Tenant Internal Domain Names** page, click **Operation Logs** in the **Actions** column to view the operation logs of the target domain name. For more information, see View operation logs. On the **Tenant Internal Domain Names** tab, you can use tags to mark and group domain names. For more information, see Manage tags.

**View monitoring data**

1. On the **Tenant Internal Domain Names** tab, find the target domain name and click the
icon in the **Monitoring** column.
2. On the **Monitoring** panel, you can view the CloudMonitor data of the target domain name,
such as **Response Time (ms)**, **Successful Resolutions (count)**, **Total Resolutions**
**(count)**, **Client IP Count (count)** , **Domain Name Resolution Success Rate (%)** ,
**Response Time (qname)**, **Successful Resolutions (qname)**, and **Total Resolutions**
**(qname)**.
You can query data by time or metric.

##### Parsing configuration

###### Add and manage DNS records

**Add a DNS record**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **VPC Private Domain Names** page, click the **Tenant Internal Domain Names**
tab.
4. On the **Tenant Internal Same-region Endpoint** tab, find the private domain name that
you want to manage and click the number in the **Total DNS Record Sets** column or **DNS**
**Settings** in the **Operation** column.
5. In the upper-left corner of the **DNS Settings** page, click **Add DNS Record**.
6. On the **Add DNS Record** page, configure the parameters for the DNS record and click **OK**.

| Record Name | Enter the host record. The domain name is automatically appended to the host record. Note A host record consists of a prefix and the domain name. The prefix must meet the following format requirements. You can also use a single asterisk (*) for wildcard DNS. i. A domain name cannot exceed 254 characters, including the trailing period (.). ii. A domain name is divided into labels separated by periods (.). Each label cannot exceed 63 characters and cannot be empty. This means you cannot have consecutive periods. iii. Domain names can contain only letters (a-z, A-Z), digits (0-9), hyphens (- ), and underscores ( ). _ iv. A domain name must start with a letter, digit, or underscore ( ). It must _ end with a letter, digit, or a trailing period (.). v. Domain names are not case-sensitive. vi. The trailing period (.) is optional. The system automatically adds it if it is omitted. For example, for the domain name `example.com.`, common DNS records are as follows: Website: Leave the host record empty to resolve `example.com.`. Website: Enter `www` as the host record to resolve `www.example.com.`. Mail server: Enter `mail` as the host record to resolve `mail.example.com.`. Wireless application: Enter `m` as the host record to resolve `m.example.com.`. Mobile application: Enter `webapp` as the host record to resolve `webapp.example.com.`. Wildcard DNS: Enter `*` as the host record to resolve `*.example.com.`. This matches all subdomains of `example.com.`. Subdomain: Enter `abc` as the host record to resolve `abc.example.com.`. |
|---|---|
| Load Balancing Policy | Select a load balancing policy. The supported policies are Polling and Weight. |

| Record Type | Select a record type. If you set Load Balancing Policy to Polling, you can select one of the following record types: A - Maps A Domain Name To An IPv4 Address AAAA - Maps A Domain Name To An IPv6 Address CNAME - Maps A Domain Name To Another Domain Name MX - Maps A Domain Name To A Mail Server Address TXT - Text String With A Length Limit Of 255 Characters. Typically Used For SPF Records (anti-spam). PTR - Records The Domain Name For Reverse DNS Lookup Of An IP Address SRV - Records The Server That Provides A Specific Service NAPTR - Records A Name Authority Pointer (NAPTR) For A Domain Name. Typically Used For ENUM. CAA - Sets The Certificate Authority Authorization (CAA) Information For A Domain Name NS - Points A Subdomain To A Specified DNS Server For Resolution If you set Load Balancing Policy to Weight, you can select one of the following record types: A - Maps A Domain Name To An IPv4 Address AAAA - Maps A Domain Name To An IPv6 Address CNAME - Maps A Domain Name To Another Domain Name |
|---|---|
| TTL (seconds) | TTL specifies how long a DNS record is cached by a local DNS server. The value must be an integer from 0 to 2147483647. A value of 0 indicates that the record is not cached. The default value is 300. If your endpoint changes frequently, set a smaller TTL value. If the endpoint is static, set a larger TTL value. |
| Line | Select one or more lines. |
| Record Value Collection | Add a record value collection. Value: Enter a record value based on the selected Record Type. For more information about the format, see Record value format. Weight: Enter an integer from 0 to 999. A larger value indicates a higher weight. This parameter is required only if you set Load Balancing Policy to Weight. Note Click Add Item to add multiple record values. Click the icon in the Actions column for the target record value to delete it. |

| Record type | Record value format requirements |
|---|---|
| A - Maps a domain name to an IPv4 address | Enter one IPv4 address per line. You can enter up to 100 unique record values. Format: Standard IPv4 address format. Example: 192.168.1.1 192.168.1.2 192.168.1.3 |
| AAAA - Maps a domain name to an IPv6 address | Enter one IPv6 address per line. You can enter up to 100 unique record values. Format: Standard IPv6 address format. Example: 2400:3200::6666 2400:3200::6688 2400:3200::8888 |
| CNAME - Maps a domain name to another domain name | Enter a single domain name. Format: A fully qualified domain name (FQDN) that ends with a period (.). The maximum length is 254 ASCII characters. Example: www.example.com. |
| MX - Maps a domain name to a mail server address | Enter one mail server record per line. You can enter up to 100 unique record values. Format: `[Priority] [Mail server hostname]` Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Mail server hostname: An FQDN that ends with a period (.). The maximum length is 254 ASCII characters. Example: 10 mailserver1.example.com. 20 mailserver2.example.com. |
| TXT - A text string with a length limit of 255 characters. This record type is typically used for Sender Policy Framework (SPF) records for anti-spam purposes. | Enter one text string per line. You can enter up to 100 unique record values. Format: A non-empty text string. The maximum length is 254 ASCII characters per string. Example: v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all |

**Record value format**

| PTR - Records the domain name for reverse DNS lookup of an IP address | Enter one domain name per line. You can enter up to 100 unique record values. Format: An FQDN that ends with a period (.). The maximum length is 254 ASCII characters. Example: www1.example.com. www2.example.com. www3.example.com. |
|---|---|
| SRV - Records the server that provides a specific service | Enter one application service record per line. You can enter up to 100 unique record values. Format: `[Priority] [Weight] [Port] [Application server hostname]` Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Weight: An integer from 0 to 999. A larger value indicates a higher weight. Port: An integer from 0 to 65535 that specifies the TCP or UDP port number. Application server hostname: An FQDN that ends with a period (.). The maximum length is 254 ASCII characters. Example: 1 10 8080 www1.example.com. 2 20 8081 www2.example.com. |

| NAPTR - Records a Name Authority Pointer (NAPTR) for a domain name. This record type is typically used for E.164 Number Mapping (ENUM). | Enter one NAPTR record per line. You can enter up to 100 unique record values. Format: `[Order] [Preference] [Flags] [Service] [Regexp] [Replacement]` Order: An integer from 0 to 999. A smaller value is processed first. Preference: An integer from 0 to 999. For records with the same order number, a smaller preference value is processed first. Flags: A single, case-insensitive character from [A-Z, a-z, 0-9] enclosed in double quotation marks (""). This field can be empty. Service: A string of up to 32 ASCII characters that starts with a letter and is enclosed in double quotation marks (""). This field can be empty. Regexp: A regular expression of up to 255 ASCII characters enclosed in double quotation marks (""). This field can be empty. Replacement: An FQDN that ends with a period (.). The maximum length is 254 ASCII characters. Example: 100 50 "S" "Z3950+I2L+I2C" "" z3950. tcp.example.com. _ _ 100 50 "S" "RCDS+I2C" "" rcds. udp.example.com. _ _ 100 50 "S" "HTTP+I2L+I2C+I2R" "" http. tcp.example.com. _ _ |
|---|---|
| CAA - Sets the Certificate Authority Authorization (CAA) information for a domain name | Enter one CAA record per line. You can enter up to 100 unique record values. Format: `[Flag] [Tag] [Value]` Flag: An integer from 0 to 255. Tag: The supported values for the tag are `issue`, `issuewild`, and `iodef`. Value: A non-empty string of up to 254 ASCII characters enclosed in double quotation marks (""). Example: 0 issue "caa.example.com" 0 issuewild ";" 0 iodef "mailto:example@example.com" |

| NS - Points a subdomain to a specified DNS server for resolution | Enter one DNS server address per line. You can enter up to 100 unique record values. Format: An FQDN that ends with a period (.). The maximum length is 254 ASCII characters. Wildcard domain names are not allowed. Example: ns1.example.com. ns2.example.com. |
|---|---|

**More operations**

After you add a DNS record, you can perform the following operations on the DNS records in the list. Query DNS records You can use the **Advanced Filter** feature to perform a fuzzy search by **Record Name**. View the load balancing policy (weight) Find the DNS record that you want to view. In the Load Balancing Policy column, click
**Weight**. In the dialog box that appears, you can view the details of the configured load
balancing policy. Modify a DNS record Find the target DNS record and click **Modify** in the **Operation** column. In the dialog box that appears, modify the information as described in Add a DNS record and then click **OK**. Add a remark to a DNS record Find the DNS record to which you want to add a remark. In the **Actions** column, click
**Remark**. Enter the content for the **Remark** and then click **OK**.
Delete a DNS record Find the DNS record that you want to delete. In the **Operation** column, click **Delete**, and then click **OK**. Batch delete DNS records Select the DNS records that you want to delete. In the lower-left corner of the page, click
**Batch Delete**, and then click **OK**.

##### Associate VPC

Tenant isolation is based on Virtual Private Clouds (VPCs). By default, domain name resolution for a private domain name is inactive. You must associate the private domain name with a VPC for the resolution to take effect within that VPC environment.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **VPC Private Domain Names** page, click the **Tenant Internal Domain Names**
tab.
4. On the **Tenant Internal Domain Name** tab, find the target private domain name and click
**Associate VPC** in the **Actions** column.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |

5. In the **Associate VPC** dialog box, select a **Region**, select a VPC from the **Associate VPC**
list, and then click **OK**. The **Associate VPC** list supports multiple selections.

##### Dissociate a VPC

You can dissociate a VPC from a private domain name.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **VPC Private Domain Names** page, click the **Tenant Internal Domain Names**
tab.
4. On the **Tenant Internal Domain Name** tab, find the target private domain name and click
the number in the **Associated VPCs** column.
5. (Method 1) On the **VPC List** page, find the VPC that you want to detach and click **Detach** in
the **Operation** column. (Method 2) On the **VPC List** page, select one or more VPCs that you want to detach and click **Batch Detach** in the lower-left corner of the page.
6. In the dialog box that appears, click **Confirm**.
The detached VPC is no longer listed on the VPC List page.

#### Tenant forwarding configurations

##### Tenant forwarding domain names

###### Add and manage tenant forwarding

**domain names**

**Add a domain name**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names for VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Forwarding Domain Names**.
4. On the **Tenant Forwarding Domain Names** tab, click **Add Domain Name**.
5. In the **Add Tenant Forwarding Domain Name** dialog box, configure the parameters as
described in the following table and click **OK**.

| Tenant Forwarding Domain Name | Enter the tenant forwarding domain name. The domain name must follow these format rules: The domain name can be up to 254 characters long, including the trailing period (.). The domain name consists of segments separated by periods (.). Each segment can be up to 63 characters long. The domain name cannot contain consecutive periods. The domain name can contain only letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores ( ). _ The domain name must start with a letter, digit, or underscore ( ). It _ must end with a letter, digit, or a period (.). The domain name is not case-sensitive. The domain name must end with a period (.). |
|---|---|
| Forwarding Mode | Select a forwarding mode. Two forwarding modes are supported for both domain-based forwarding and default forwarding. Forward All Mode (Recommended) - Forwards All Requests Without Recursion: Forwards DNS requests only to the destination DNS server. If the server cannot resolve the domain name, a failure message is returned to the client. Forward First Mode - Falls Back To Internet Recursion On Failure: Preferentially uses the destination DNS server for domain name resolution. If the server cannot resolve the domain name, the local DNS server performs a recursive query on the Internet. Important Risk warning: If all destination IP addresses are internal, falling back to Internet recursion may produce unexpected results. For example, a domain name for an internal service might be resolved to a public IP address. |

| Destination IP Addresses | Enter the list of destination IP addresses. Format requirements: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv4 or IPv6 address per line. You can enter up to five unique IP addresses. |
|---|---|

**More operations**

**View the domain name list**

On the **Tenant Forwarding Domain Names** page, you can view the domain names that you have added. You can use the advanced search feature to enter filter conditions and find specific domain names. Click the icon in the upper-right corner of the list to customize the columns. You can show or hide columns and drag them to change their order. Click the icon next to a column name to sort the list by that column.

**Modify a domain name**

1. On the **Tenant Forwarding Domain Names** page, find the target domain name and click
**Modify** in the **Actions** column.
2. In the **Modify Tenant Forwarding Domain Name** dialog box, modify the **Forwarding**
**Mode** and **Destination IP Addresses**, and click **OK**.
For more information about the parameters, see Add a domain name.

**Add remarks to a domain name**

1. On the **Tenant Forwarding Domain Names** page, find the target domain name and click
**Add Remarks** in the **Actions** column.
2. In the **Add Remarks to Domain Name** dialog box, enter the remarks in the **Remarks**
field and click **OK**.

**Delete a domain name**

1. (Method 1) On the **Tenant Forwarding Domain Names** page, find the target domain
name, and in the **Actions** column, click the
**> Delete**.
(Method 2) On the **Tenant Forwarding Domain Names** page, select the checkboxes of one or more domain names and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Tenant Forwarding Domain Names** page, find the target domain name and click
**Operation Logs** in the **Actions** column to view the operation logs. For more information,
see View operation logs.

**Tag management**

On the **Tenant Forwarding Domain Names** tab, you can use tags to mark and group domain names. For more information, see Manage tags.

###### Associate a VPC

Tenant isolation is based on Virtual Private Clouds (VPCs). By default, domain name resolution settings do not take effect. To apply the settings within a specific VPC, you must associate the domain name with that VPC.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names for VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Forwarding Domain Names**.
4. In the list of tenant forwarding domain names, find the domain name that you want to
associate and click **Associate VPC** in the **Actions** column.
5. In the **Associate VPC** dialog box, set the **Region** and **Associate VPC** parameters, and
then click **OK**. The **Associate VPC** parameter supports multiple selections.

###### Dissociate a VPC

You can dissociate a VPC.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names for VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Forwarding Domain Names**.
4. In the tenant forwarding domain name list, find the target domain name and click the
number in the **Associated VPCs** column.
5. (Method 1) On the **VPC List** page, find the VPC that you want to detach, and click **Detach**
in the **Actions** column. (Method 2) On the **VPC List** page, select one or more VPCs that you want to detach, and click **Batch Detach** in the lower-left corner of the page.
6. In the dialog box that appears, click **OK**.
The detached VPC is no longer displayed on the VPC List page.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Forwarding Mode | Select a forwarding mode. Two forwarding modes are supported for both domain name- based forwarding and default forwarding. Forward All Mode (Recommended) - Forwards All Requests Without Recursion: Uses only the destination DNS server to resolve domain names. If a result is not found, a failure message is returned to the client. Forward First Mode - Degrades To Internet Recursion On Failure: Preferentially uses the destination DNS server to resolve domain names. If a result is not found, the local DNS server is then used for recursive queries on the Internet. Important Risk warning: When all destination IP addresses are internal IP addresses, degrading to Internet recursion might produce unexpected results. For example, a domain name for an internal service might be resolved to a public IP address. |

##### Tenant default forwarding configurations

###### Add and manage default forwarding

**configurations**

**Limits**

This feature is available only to system administrators and level-1 organization administrators.

**Add a configuration**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names For VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Default Forwarding Configurations**.
4. On the **Tenant Default Forwarding Configurations** tab, click **Add Configuration**.
5. In the **Add Tenant Default Forwarding** dialog box, set the following parameters and
click **OK**.

| Destination IP Address | Enter the destination IP addresses. Format requirements: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv4 or IPv6 address per line. You can enter up to five unique IP addresses. |
|---|---|

**More operations**

**List of Domain Names**

On the **Tenant Default Forwarding Configurations** page, you can view the added configurations in a list. Use the advanced search feature to find a specific configuration by entering filter criteria. Click the icon in the upper-right corner of the list to customize columns. You can show or hide columns and drag them to change their order. Click the icon next to a column header to sort the list by that column.

**Modify domain name**

1. On the **Tenant Default Forwarding Configurations** page, find the target configuration
and click **Modify** in the **Actions** column.
2. In the **Modify Tenant Default Forwarding** dialog box, change the **Forwarding Mode**
and **Destination IP Address**, and then click **OK**. For more information about the parameters, see Add a configuration.

**Notes on Domain Names**

1. On the **Tenant Default Forwarding Configurations** page, find the target configuration
and click **Remarks** in the **Actions** column.
2. In the **Remark** dialog box, enter the **Remark** text, and then click **OK**.

**Delete domain name**

1. (Method 1) On the **Tenant Default Forwarding Configurations** page, find the target
configuration and click
**> Delete** in the **Actions** column.
(Method 2) On the **Tenant Default Forwarding Configurations** page, select one or more configurations and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Tenant Default Forwarding Configurations** page, find the target configuration and click **Operation Logs** in the **Actions** column to view its logs. For more information, see View operation logs. On the **Tenant Default Forwarding Configurations** tab, you can use tags to mark and group configurations. For more information, see Manage tags.

###### Associate a VPC

Tenant isolation is based on Virtual Private Clouds (VPCs). By default, domain name resolution configurations are not active. To activate a configuration in a specific VPC, you must associate it with that VPC.

**Limits**

Only system administrators and level-1 organization administrators can perform these operations.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names For VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Default Forwarding Configurations**.
4. In the list of tenant default forwarding configurations, find the target configuration, and
click **Associate VPC** in the **Actions** column.
5. In the **Associate VPC** dialog box, set parameters such as **Region** and **Associate VPC**,
and then click **OK**. You can select multiple VPCs for the **Associate VPC** parameter.

###### Detach a VPC

You can detach an associated VPC.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private DNS > VPC Private Domain Names**.
3. On the **Private Domain Names For VPC** page, choose **Tenant Forwarding**
**Configurations > Tenant Default Forwarding Configurations**.
4. In the list of tenant default forwarding configurations, find the target configuration and click
the number in the **Number Of Associated VPCs** column.
5. (Method 1) On the **VPC List** page, find the VPC that you want to detach, and click **Detach**
in the **Actions** column. (Method 2) On the **VPC List** page, select one or more VPCs to detach, and click **Batch**
**Detach** in the lower-left corner of the page.
6. In the dialog box, click **OK**.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Line Name | Enter a name for the line. |
| Sorting Behavior | Select a sorting behavior. Insert To Top Insert To Bottom Insert Before Selected Line Note The sort number of a line determines its priority. A smaller sort number indicates a higher priority. |
| Insert Before This Line | Select the line before which you want to insert the new line. Note This parameter is required when you set Sorting Behavior to Insert Before Selected Line. |

The detached VPC is no longer displayed on the VPC List page.

### Private lines

Apsara Stack DNS allows you to define lines based on IP addresses on the Private Line page. The lines are used to group request sources to achieve intelligent load balancing. The lines can be referenced by private domain names for VPCs.

#### Add and manage private lines

Private lines are address pools that identify the source of requests. This topic describes how to add and manage private lines.

**Add a line**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Private Domain Name Service > Private**
**Line**.
3. On the **Private Line** page, click **Add Line**.
4. In the **Add Line** dialog box, configure the private line and click **OK**.

| IPv4 Address Range | Enter the IPv4 address range. You must specify either IPv4 Address Range or IPv6 Address Range. Format: Standard IPv4 address format Examples: 192.168.1.1 192.168.1.2 Note Enter one IPv4 address per line. You can enter up to 1,000 lines. |
|---|---|
| IPv6 Address Range | Enter the IPv6 address range. You must specify either IPv4 Address Range or IPv6 Address Range. Format: Standard IPv6 address format Examples: 2400:3200::6666 2400:3200::6688 Note Enter one IPv6 address per line. You can enter up to 1,000 lines. |

**More operations**

**Query lines**

On the **Private Line** page, you can view the details of the private lines in the list. You can search for a private line by entering a keyword or by specifying filter conditions in the **Advanced Search** section. Click the icon in the upper-right corner of the list to customize the columns. You can show or hide columns and drag columns to reorder them. Click the icon next to a column name to sort the list by that column.

**Modify a line**

1. On the **Private Line** page, find the line that you want to modify and click **Modify** in the
**Actions** column.
2. In the dialog box that appears, modify **Line Name**, **IPv4 Address Range**, and **IPv6**
**Address Range**, and click **OK**.

**Note**

You must specify either **IPv4 Address Range** or **IPv6 Address Range**.

**Sort lines**

1. On the **Private Line** page, find the line that you want to reorder and click **Sort** in the
**Actions** column.
2. In the dialog box that appears, select **Sorting Behavior** and click **OK**.

**Delete a line**

**Note**

Before you delete a line, you must dissociate it from all scheduling instances.
1. (Method 1) On the **Private Lines** page, find the target line, and click **Delete** in the
**Actions** column.
(Method 2) On the **Private Lines** page, select the target lines, and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
On the **Private Lines** page, click **Operation Logs** in the **Actions** column for the target line to view its operation logs. For more information, see View operation logs. On the **Private Line** tab, you can use tags to mark and group lines. For more information, see Manage tags.

| Parameter | Description |
|---|---|
| Scheduling Instance Name | Enter a name for the scheduling instance. |
| Scheduling Domain Name | Enter the domain name for the scheduling instance. |
| Organization | Select an organization. The current system organization is selected by default. This parameter is used to filter VPC private domain names for the scheduling domain. The scheduling instance itself does not belong to an organization. |
| Region | Select a region. This parameter is used to filter VPC private domain names for the scheduling domain. The scheduling instance itself does not belong to a region. |
| Scheduling Domain | Select a created global domain name instance in the cloud or a VPC private domain name instance. This parameter cannot be modified after it is set. |

## Global scheduling

### Scheduling instances

The Scheduling Instance page displays all existing scheduling instances. You can create, delete, modify, and configure scheduling instances on this page. You must associate an address pool and a scheduling domain with the instance.

#### Create and manage scheduling

**instances**

A scheduling instance is the basic unit of scheduling in Global Traffic Manager. You can use a scheduling instance to reroute traffic for a specified domain name. This topic describes how to create and manage scheduling instances.

**Create a scheduling instance**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Global Scheduling > Scheduling Instance**.
3. On the **Scheduling Instances** page, click **Create Scheduling Instance**.
4. In the dialog box that appears, configure the settings as described below and click **OK**.

| Global TTL | Enter the cache duration. TTL specifies the duration for which a DNS record is cached on a local DNS server. The value must be an integer from 0 to 2,147,483,647. The unit is seconds. A value of 0 indicates that the record is not cached. If your endpoint changes frequently, set a smaller TTL value. Otherwise, set a larger TTL value. |
|---|---|

**More operations**

After you create a scheduling instance, you can perform the following operations on the
**Scheduling Instance** page.
You can use the **Advanced Filter** to perform a fuzzy search by entering a **Scheduling**
**Instance Name**.
Click the icon in the upper-right corner of the list to show or hide columns, or drag columns to reorder them. Modify a scheduling instance Find the target scheduling instance and click **Modify** in the **Actions** column. In the dialog box that appears, modify the instance information as described in Create a scheduling instance, and then click **OK**. Delete a scheduling instance

**Important**

After a scheduling instance is deleted, domain name resolution for the business domain names that use the instance will fail. Proceed with caution. To delete a single instance: Find the target scheduling instance, click **Delete** in the
**Actions** column, and then click **OK**.
To delete multiple instances: Select the scheduling instances that you want to delete, click **Batch Delete** in the lower-left corner of the page, and then click **OK**. Find the target scheduling instance. In the **Actions** column, click **Operation Logs** to view the operation logs. For more information, see View operation logs.

#### Configure a scheduling instance

You can create, delete, modify, and query access policies for scheduling instances.

**Execution policy for automatic switchover (access policy**

**processing logic)**

| Primary address pool status | Secondar y address pool status | Sub-condition (comparison of healthy address counts) | Active address pool (list of available addresses) |
|---|---|---|---|
| Available | Available | - | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Available | Unavailabl e | - | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Unavailabl e | Available | - | Secondary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Unavailabl e | Unavailabl e | Primary to Standby | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |

**Note**

Whether an address pool is available is determined based on the number of normal addresses in the address pool and the minimum number of available addresses in the address pool that you specify when you configure the access policy. If the number of normal addresses in the address pool is less than the specified minimum number of available addresses in the address pool, the address pool is considered unavailable. You can perform a health check to obtain the number of normal addresses in the address pool. Healthy addresses include intelligently returned healthy addresses and all alwaysonline addresses, regardless of their health check status. Healthy addresses do not include intelligently returned abnormal addresses or any always-offline addresses, regardless of their health check status.

| Unavailabl e | Unavailabl e | Primary < Secondary | Secondary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
|---|---|---|---|
| Unavailabl e | Unavailabl e | Number of normal addresses in the primary address pool = Number of normal addresses in the secondary address pool > 0 | Primary address pool (The available addresses include the normal addresses that are intelligently returned and the addresses that are always online. Abnormal addresses that are intelligently returned are deleted, or their weight values are set to 0.) |
| Unavailabl e | Unavailabl e | Both Primary and Secondary are 0. | If the DNS request source is a custom line, the system clears the DNS configurations of the line instead of selecting an address pool. This means that the configurations of the custom line are deleted. If the DNS request source is the global default line, the system selects the primary address pool. This means that the system returns all the configured addresses without considering their return modes. |

| Scenario | Address type: Active address pool in two access policies |  | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv6 | IPv4 and IPv6 addresses take effect at the same time. |
| Same DNS request source: Scenario 2 | IPv4 | Domain Name | Domain name takes effect |
| Same DNS request source: Scenario 3 | IPv6 | Domain Name | Domain name takes effect |

| Scenario | Primary address pool (Access policy 1) | Secondary address pool (Access policy 2) | Processing logic |
|---|---|---|---|

**Handling record type conflicts after a switchover**

**For the same DNS request source,** this section describes how to handle record type
conflicts after a switchover. A conflict occurs when the same line is included in more than one access policy. The following logic applies to the specific line that is in conflict. Conflict restrictions for primary and secondary address pool types

| Same DNS request source: Scenario 1 | IPv4 | IPv4 | Addition allowed |
|---|---|---|---|
| Same DNS request source: Scenario 2 | IPv4 | IPv6 | Addition not allowed |
| Same DNS request source: Scenario 3 | IPv4 | Domain Name | Addition allowed |
| Same DNS request source: Scenario 4 | IPv6 | IPv4 | Addition not allowed |
| Same DNS request source: Scenario 5 | IPv6 | IPv6 | Addition allowed |
| Same DNS request source: Scenario 6 | IPv6 | Domain Name | Addition allowed |
| Same DNS request source: Scenario 7 | Domain Name | IPv6 | Addition allowed |
| Same DNS request source: Scenario 8 | Domain Name | IPv4 | Addition allowed |
| Same DNS request source: Scenario 9 | Domain Name | Domain Name | Addition allowed |

| Scenario | Primary address pool (Access policy 1) | Primary address pool (Access policy 2) | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv6 | Addition and coexistence allowed |
| Same DNS request source: Scenario 2 | IPv4 | IPv4 | Addition and coexistence not allowed |
| Same DNS request source: Scenario 3 | IPv4 | Domain Name | Addition and coexistence not allowed |
| Same DNS request source: Scenario 4 | IPv6 | IPv6 | Addition and coexistence not allowed |

Conflict restrictions for multiple address types

| Same DNS request source: Scenario 5 | Domain Name | IPv6 | Addition and coexistence not allowed |
|---|---|---|---|
| Same DNS request source: Scenario 6 | Domain Name | Domain Name | Addition and coexistence are allowed if the following conditions are met: i. The two primary address pools must be the same address pool. ii. One secondary address pool must be IPv4, and the other must be IPv6. |

| Scenario | Secondary address pool (Access policy 1) | Secondary address pool (Access policy 2) | Processing logic |
|---|---|---|---|
| Same DNS request source: Scenario 1 | IPv4 | IPv6 | Addition and coexistence allowed |
| Same DNS request source: Scenario 2 | IPv4 | IPv4 | Addition and coexistence not allowed |
| Same DNS request source: Scenario 3 | IPv4 | Domain Name | Addition and coexistence not allowed |
| Same DNS request source: Scenario 4 | IPv6 | IPv6 | Addition and coexistence not allowed |
| Same DNS request source: Scenario 5 | Domain Name | IPv6 | Addition and coexistence not allowed |
| Same DNS request source: Scenario 6 | Domain Name | Domain Name | Addition and coexistence are allowed if the following conditions are met: i. The two secondary address pools must be the same address pool. ii. One primary address pool must be IPv4, and the other must be IPv6. |

##### Create and manage access policies for a

**scheduling instance**

| Parameter | Description |
|---|---|
| Policy Name | Required. Enter a name for the access policy. |
| Check for Global Default Request Source | Turn the Global Default Source switch on or off. By default, the switch is Off. If you turn on this switch, this access policy applies to all users that access the application service. Configure the global default line separately. Do not select it in combination with other lines. |
| Parse Request Source | Select a configured Global Line or Private Line. The DNS request source enables intelligent DNS resolution. You can select multiple sources. Note This parameter is required only when Global Default Source is set to Off. |
| Primary Address Pool | Select an available primary address pool. The primary address pool is the default address pool that users access. If the primary address pool becomes unavailable, the system automatically switches between the primary and secondary address pools based on the Active Address Pool Switchover Policy. |
| Primary Address Pool Type | Displays the type of the selected primary address pool. The type can be IPv4, IPv6, or Domain Name. |

An access policy contains information such as intelligent DNS resolution, primary and secondary address pools, and the active address pool switchover policy. For each instance, you can create multiple access policies to configure different response address pools for users from different networks or regions. This provides nearest-point access for users and implements automatic failover.

**Create an access policy**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Global Scheduling > Scheduling Instance**.
3. On the **Scheduling Instance** page, find the target scheduling instance and click
**Configure** in the **Actions** column.
4. On the **Access Policy** page, click **Create Access Policy** in the upper-left corner.
5. On the **Create Access Policy** page, configure the parameters as described in the following
table, and then click **OK**.

| Minimum Number Of Available Addresses In The Primary Address Pool | Required. Set the minimum number of available addresses. The value must be an integer from 1 to 100. If the number of healthy addresses in the address pool is less than this value, the address pool is considered unavailable. |
|---|---|
| Secondary Address Pool | Select an available secondary address pool. |
| Secondary Address Pool Type | Displays the type of the selected secondary address pool. The type can be IPv4, IPv6, or Domain Name. |
| Minimum Number Of Available Addresses In The Secondary Address Pool | The minimum number of available addresses in the secondary address pool. If the number of healthy addresses in the address pool is less than the minimum number of available addresses in the address pool, the address pool is deemed unavailable. This parameter is optional. The value of this parameter must be an integer ranging from 1 to 100. |
| Active Address Pool Switchover Policy | Set the active address pool switchover policy. Default: Automatic. Automatic: The system automatically switches between the primary and secondary address pools based on their availability. The primary address pool is used when both are available. Manual: You must manually specify the active address pool. |
| Specify Address Pool | Specify the active address pool. Select Primary Address Pool or Secondary Address Pool. Note This parameter is required only when Active Address Pool Switchover Policy is set to Manual. |

**More operations**

Query access policies Use **Advanced Filter** and enter a **Policy Name** to perform a fuzzy search. Click the + icon to the left of an access policy to view its **primary/secondary address**
**pool** information.
Click an address pool name to view the details of the **primary/secondary address pool**. Edit an access policy

**Important**

You can modify an access policy to return different address pools based on the DNS request source. When you edit an access policy, no primary/secondary failover is triggered if you do not change the associated primary or secondary address pools. If you re-associate either the primary or secondary address pool, the following rules apply:

| Parameter | Description |
|---|---|
| Address Pool Name | Enter a name for the address pool. The name can contain up to 20 Chinese and English characters. |
| Address Type | Select a type for the address pool. You can select IPv4, IPv6, or Domain Name. After you select a type, you cannot change it. |
| Load Balancing Policy (between Addresses) | Select a load balancing policy for the addresses. After you select a policy, you cannot change it. Polling: For any resolution request, all addresses in the address pool are returned. The addresses are rotated for each request. Weight: You can set a different weight for each address. Resolution requests are then routed to addresses based on their weight ratio. |

i. In manual switchover mode, if the secondary address pool is deleted, the system forces a switchover to the primary address pool. If the secondary address pool is not deleted, the currently active address pool remains unchanged. ii. In automatic switchover mode, the system reselects the active address pool based on the availability of the modified address pools. Proceed with caution. Find the target access policy, click **Edit** in the **Actions** column, modify the parameters in the dialog box that appears as described in Create an access policy, and then click **OK**. Delete an access policy Find the target access policy, click **Delete** in the **Actions** column, and then click **OK**.

### Address pool

#### Create and manage address pools

Address pools are associated with scheduling instances. This topic describes how to create and manage address pools. You can create an address pool by defining a list of addresses. You can then associate the address pool with access policies for scheduling instances.
1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Global Traffic Manager > Address Pools**.
3. On the **Address Pools** page, click **Create Address Pool** in the upper-left corner.
4. On the **Create Address Pool** page, configure the parameters for the address pool and
click **OK**.

| Address List | Add a list of addresses. Address Value: Enter an address based on the selected Address Type. For more information about the format, see Address value format. Mode: Select an address mode. Smart Return: The system determines whether the address is available based on health check results. Always Online: The system ignores health check results and considers the address always available. The health check task continues to run. Always Offline: The system ignores health check results and considers the address always unavailable. The health check task continues to run. Weight: Enter a weight. The value must be an integer from 0 to 999. A larger value indicates a greater weight. This parameter is required only when you set Load Balancing Policy (between Addresses) to Weight. Note Click Add to add more addresses. Click Delete in the Actions column of a target address to remove it. |
|---|---|

| Address type | Format requirements for the address value |
|---|---|
| IPv4 | Enter one IPv4 address per line. You can enter up to 100 unique records. Format requirement: Standard IPv4 address format. Examples: 192.168.1.1 192.168.1.2 192.168.1.3 |
| IPv6 | Enter one IPv6 address per line. You can enter up to 100 unique records. Format requirement: Standard IPv6 address format. Examples: 2400:3200::6666 2400:3200::6688 2400:3200::8888 |

**Address value format**

| Domain Name | Enter one domain name. Only one domain name is allowed. Format requirement: A fully qualified domain name (FQDN) that ends with a period (.). The domain name can be up to 254 ASCII characters in length. Example: www.example.com. |
|---|---|

**More operations**

On the **Address Pools** page, you can view a list of the address pools that you created. You can use the advanced search feature to enter filter conditions and find a specific address pool. You can click the icon in the upper-right corner of the list to customize the displayed columns. You can show or hide columns and drag them to change their order. You can click the or icon to the left of an address pool to expand or collapse its details, such as the address list and health check status.

**Important**

After you modify an address pool for which health checks are enabled, the health check status of all addresses is reset to Normal. If the address pool is associated with an access policy that uses automatic switchover, a primary/secondary failover may be triggered. Proceed with caution.
1. On the **Address Pools** page, find the address pool that you want to modify and click
**Modify** in the **Actions** column.
2. On the **Modify Address Pool** page, change the **Address Pool Name** and **Address List**,
and then click **OK**. For more information about the parameters, see Create an address pool.

**Important**

Before you can delete an address pool, you must dissociate it from all scheduling instances.
1. (Method 1) On the **Address Pools** page, find the address pool that you want to delete and
click **Delete** in the **Actions** column. (Method 2) On the **Address Pools** page, select one or more address pools that you want to delete and click **Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.

| Configuration parameter | Description |
|---|---|
| Health Check Switch | Turn the health check switch on or off. |
| Protocol | Select a protocol. HTTPS HTTP TCP UDP ICMP |
| Port | Enter the network port number used for health checks on the target address. Default value: 80. The value must be an integer from 1 to 65535. This parameter is required. Note This parameter is required when you set Protocol to HTTPS, HTTP, TCP, or UDP. |

On the **Address Pools** page, click **Operation Logs** in the **Actions** column to view the operation logs for an address pool. For more information, see View operation logs.

#### Health check

Only addresses with a normal health check status are returned. This topic describes how to create a health check for an address pool.
1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Global Traffic Manager > Address Pools**.
3. On the **Address Pool** page, find the desired address pool and click **Health Check** in the
**Actions** column.
4. On the **Health Check** page, click **Create Health Check**.
5. On the **Create Health Check** page, set the parameters and click **OK**.

| Host Settings | Enter the HOST configuration for the health check probe. Example: www.example.com If you leave this parameter empty, the primary domain name is used. Note This parameter is required when you set Protocol to HTTPS or HTTP. |
|---|---|
| URL Path | The path used to confirm if the HTTP/HTTPS service of the target address is normal. The service is considered normal if the path returns an HTTP status code of 2xx or 3xx. The path can be empty. The system automatically adds a leading forward slash (/). The default value is /. The total length cannot exceed 255 characters. Note This parameter is required when you set Protocol to HTTPS or HTTP. |
| Return Code Greater Than | The value that the HTTP return code must be greater than for the health check to be considered abnormal. Default value: 400. Note This parameter is required when you set Protocol to HTTPS or HTTP. |
| Health Check Interval (s) | Enter the time interval for health check probes on the target address. Default value: 15. |
| Timeout (s) | Enter the timeout period to wait for a response when an exception occurs during a health check probe. Default value: 3. |
| Number Of Retries | Enter the number of retries when an exception occurs during a health check probe. Default value: 1. |
| Probe Nodes | Select VPC network nodes. You must select at least two nodes. |

**More operations**

On the **Health Check** page, you can view the list of health checks that you have created. Click the icon in the upper-right corner of the list to show or hide items. You can also drag items to change their order.
1. On the **Health Check** page, find the desired health check and click **Edit** in the **Actions**
column.
2. In the dialog box that appears, modify the health check parameters and click **OK**.
For more information about the parameters, see Create a health check.
1. On the **Health Check** page, find the desired health check and click **Delete** in the **Actions**
column.
2. In the dialog box that appears, click **OK**.

## System management

### Log Management

This topic describes how to view alert information for a DNS cluster.

**Procedure**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **System Administration > Log Management**.
3. On the **Log Management** page, you can view the alert information for the DNS cluster.
The information includes **Time**, **Object**, **Behavior**, and **Content**. You can click the icon in the upper-right corner of the alert list to show or hide columns, and drag columns to reorder them. You can click the drop-down list in the upper-left corner of the alert list to filter alerts by behavior. The options include **All**, **Prepare For Address Pool Switchover**, **Address Pool**
**Unavailable**, **Address Pool Restored To Available**, **Address Unavailable**, and
**Address Restored To Available**.
You can enter a **Keyword** to filter the alerts. You can specify a time range to filter the alerts.

| Parameter | Description |
|---|---|
| Tag Key | The key of the tag. You can select an existing tag key or enter a new one. A tag key can be up to 64 characters in length. It cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Tag Value | The value of the tag. You can select an existing tag value or enter a new one. A tag value can be up to 128 characters in length. It cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

## Manage tags

Alibaba Cloud DNS supports tags. You can use tags to mark and classify instances, such as tenant internal domain names, tenant forwarding domain name lists, tenant default forwarding configurations, and private lines. This helps you search for and group resources. This topic describes how to manage and use tags. Managing many instances can be difficult. You can use tags to group your instances. This makes searching and filtering easier. A tag is a mark assigned to an instance. Each tag consists of a key-value pair. Note the following about tags: You can manage tags for the following instances: tenant internal domain names, tenant forwarding domain name lists, tenant default forwarding configurations, and private lines. The tag key for each tag on a single instance must be unique. You can modify or delete the key and value of a tag at any time. If an instance is deleted, all tags attached to it are also deleted. This operation does not affect tags attached to other instances. You can attach a maximum of 20 tags to an instance. This quota cannot be increased.

**Attach tags**

1. Log on to the DNS console.
2. In the navigation bar, select the instance type.
3. Attach tags to instances.
Add a tag to a single instance a. On the page for the corresponding instance type, find the target instance, hover over the icon in the **Tag** column, and click **Edit** in the pop-up box. b. In the **Edit Tags** dialog box, configure the tag based on the following information. Click
**Add** to attach multiple tags. Then, click **OK**.
c. In the **Tags Edited** dialog box, confirm the result and then click **Close**. Add tags to multiple instances a. On the page for the instance type, select the check boxes of the target instances. Then, click **Batch Add Tags** in the lower-left corner. b. In the **Batch Add Tags** dialog box, add a **Tag Key** and a **Tag Value**. Then, click **OK**. c. In the **Tags Edited** dialog box, confirm the result and then click **Close**.

**Detach tags**

1. Log on to the DNS console.
2. In the navigation bar, select the instance type.
3. Detach tags from instances.
Detaching a tag from a single instance a. On the page for the corresponding instance type, find the target instance, hover over the icon in the **Tags** column, and click **Edit** in the pop-up menu. b. In the **Edit Tags** dialog box, click the icon to the right of the target tag. Then, click
**OK**.
c. In the **Tags Edited** dialog box, click **Close**. Detach tags from multiple instances a. On the instance page, select the check boxes for the target instances from which you want to detach tags. Then, click **Batch Detach Tags** in the lower-left corner. b. In the **Batch Detach Tags** dialog box, select the tags that you want to detach from the **Tags To Detach** list. Then, click **OK**. c. In the **Tags Edited** dialog box, confirm the result, and then click **Close**.

**Search for instances by tag**

After you attach tags to instances, you can use the tags to quickly find them.
1. Log on to the DNS console.
2. In the navigation bar, select the instance type.
3. On the page for the instance type, choose **Advanced Search > Filter By Tag**.
4. In the dialog box that appears, select a **Tag Key** and a **Tag Value**. Then, click **Search**. The
system filters the instances based on the selected tag key and tag value.

| Filter condition | Description |
|---|---|
| Operator | Enter the operator who performed the change operation. |
| Action | Select the name of the change operation for the target instance. This is the API name. |
| Execution Status | Select an execution status of Successful or Failed. |
| Source IP | Enter the source IP address. |
| Time | Select the time range you want to view. |

## View operation logs

You can view the operation logs for your Alibaba Cloud DNS instances. These logs provide information such as the instance status, the source and time of an operation, and API call details. This information helps you analyze and trace historical operations.

**Procedure**

1. Log on to the DNS console.
2. In the navigation bar, select a specific instance type.
3. On the instance list page, find the target instance and click **Operation Log** in the **Actions**
column.
4. On the **Operation Log** page, view the operation logs.

**Note**

The default log retention period is 720 days. To change this period, an administrator must adjust the settings in Configuration > Log Storage Configuration. If you extend the log retention period, historical log data is not backfilled.
5. **Optional:** Filter the operation records using filter conditions such as **Action** and **Operator**.
The supported filter conditions are listed in the following table.
6. **Optional:** For a target management event, click **Operation Details** in the **Actions**
column. In the **Operation Details** panel that appears, view the **Basic Details** and **API**
**Call Details**.
