---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack DNS Apsara Stack DNS (Multicloud Integration) User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 19
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack DNS Apsara Stack DNS (Multicloud Integration) User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E4%BA%91DNS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Stack%20DNS%20Apsara%20Stack%20DNS%20%28Multicloud%20Integration%29%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack DNS Apsara Stack DNS (Multicloud Integration) User Guide 20260828

S (Multicloud Integration)?

## What is DNS (Multicloud

**Integration)?**

DNS (Multicloud Integration) is a domain name resolution product designed for Apsara Stack environments. It provides shared domain name resolution across multiple Apsara Stack environments. DNS (Multicloud Integration) uses rules and policies to map domain names to IP addresses. This process redirects client requests to resources such as cloud resources, business systems on a corporate intranet, and service resources from an Internet Service Provider. nd permissions

## User roles and permissions

| User role | Permission |
|---|---|
| System administrator | A user of this role has read, write, and execute permissions on all level-1 organization resources, global resources, and system configurations. |
| Level-1 organization administrator | A user of this role has read, write, and execute permissions on level-1 organization resources to which the user belongs, but does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Lower-level organization administrator | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Resource user | A user of this role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |
| Other roles | A user of such role does not have permissions on Apsara Stack DNS. The user does not have permissions on level-1 organization resources to which the user belongs, and does not have permissions on level-1 organization resources, global resources, or system configurations to which other users belong. |

e DNS (Multicloud Integration) co nsole

## Log on to the DNS

**(Multicloud Integration)**

**console**

This topic describes how to log on to the DNS (Multicloud Integration) console using Google Chrome.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. You can select a language from the drop-down list in the upper-right corner of the page. 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。 e DNS (Multicloud Integration) co nsole
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

**Forgot password**

If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**. For information about how to bind and enable MFA, see the **Security Center** >
**Multi-factor Authentication** > **Manage Multi-factor Authentication** section in
the Apsara Uni-manager Management Console User Guide.
5. In the top menu bar, choose **Products > Network > Cross-cloud DNS**.

## Cross-cloud shared domain

**names**

### Overview

Suitable for multicloud integration scenarios. The configuration information is globally synchronized among multiple clouds to provide global domain name resolution for all applications after multicloud integration.

### Add and manage domain

**names**

You can add and manage domain names in the Apsara Uni-manager Management Console.

**Add a domain name**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Cross-cloud Domain Name Service > Cross-**
**cloud Shared Domain Names**.
3. On the **Multicloud Domain Names** page, click **Add Domain Name**.
4. In the **Create Scheduling Domain** dialog box, enter a **Scheduling Domain Name** and
click **OK**. i. A domain name cannot exceed 220 characters, including the trailing period (.). ii. A domain name is divided into segments by periods (.). Each segment cannot exceed 63 characters and cannot be empty. This means you cannot have consecutive periods. iii. A domain name can contain only letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores (_). iv. Domain names are case-insensitive. v. A domain name must end with a period (.).

**What to do next**

**View domain names**

On the **Multicloud Domain Names** page, you can view the added domain names in a list. The list includes **Domain Name/ID**, **Record Sets**, **Description**, **Created At**, and **Last**
**Modified At**.
You can enter a domain name to search for it. Click the icon in the upper-right corner of the list to show or hide columns. You can also drag the columns to reorder them.

**Add a note to a domain name**

You can add a note to a domain name to mark it with information, such as a hostname or internal system info.
1. On the **Multicloud Domain Names** page, find the domain name that you want to add a
note to, and click **Description** in the **Actions** column.
2. In the **Add Description** dialog box, enter the **Description** and click **OK**.

**Delete a domain name**

When you delete a scheduling domain, all its scheduling instances are also deleted. This action cannot be undone. Proceed with caution.
1. (Method 1) On the **Multicloud Domain Names** page, find the domain name that you want
to delete and click **Delete** in the **Actions** column. (Method 2) On the **Multicloud Domain Names** page, select the check boxes for one or more domain names that you want to delete and click **Batch Delete** in the lower-left corner.
2. In the confirmation dialog box, click **OK**.

### Parsing settings

#### Add and manage DNS records

You can configure parsing settings in the Apsara Uni-manager Management Console.

**Add a DNS record**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Cross-cloud Domain Name Service > Cross-**
**cloud Shared Domain Names**.
3. On the **Multicloud Domain Names**page, find the target domain name and click the value
in the **Record Sets** column, or click **Actions** in the **Configure DNS Records** column.
4. On the **DNS Settings** page, click **Add DNS Record** in the upper-left corner.
5. On the **Add DNS Record** page, configure the DNS record as described below and click **OK**.

| Name | Description |
|---|---|

| Record Name | Enter a record name. The domain name is automatically appended to the record name. Note The record name consists of a host record and a domain name suffix. The host record can be a single asterisk (*) for wildcard DNS, but must otherwise meet the following format requirements: i. A domain name cannot exceed 254 characters in length, including the trailing period (.). ii. A domain name is divided into labels separated by periods (.). Each label cannot exceed 63 characters and cannot be empty. This means you cannot have consecutive periods. iii. Domain names can contain only uppercase or lowercase letters (a-z, A- Z), digits (0-9), hyphens (-), and underscores ( ). Other characters are _ not allowed. iv. A domain name must start with a letter, digit, or underscore ( ) and end _ with a letter, digit, or a trailing period (.). Other characters are not allowed at the start or end. v. Domain names are not case-sensitive. vi. The trailing period (.) is optional. If you omit it, the system automatically adds it. For example, for the domain name suffix example.com., common DNS records are configured as follows: Website application: Leave the host record empty. The resolved domain name is example.com. Website application: Set the host record to www. The resolved domain name is www.example.com. Mail server: Set the host record to mail. The resolved domain name is mail.example.com. Wireless application: Set the host record to m. The resolved domain name is m.example.com. Mobile application: Set the host record to webapp. The resolved domain name is webapp.example.com. Wildcard DNS: Set the host record to *. The resolved domain name is *.example.com., which matches all subdomains of example.com. Subdomain: Set the host record to abc. The resolved domain name is abc.example.com. |
|---|---|
| Load Balancing Policy | Select a load balancing policy. Polling: For DNS queries from any source, all addresses in the IPAM pool are returned. The addresses are rotated for each query. Weight: Allows you to set a different weight for each address. DNS queries are then returned based on the weight ratio. |

| Record Type | Select a record type. If you set Load Balancing Policy to Polling, you can select one of the following types: A - Points a domain name to an IPv4 address AAAA - Points a domain name to an IPv6 address CNAME - Points one domain name to another MX - Points a domain name to an email server address TXT - Serves as a Sender Policy Framework (SPF) record to protect against spam (Maximum length: 255 characters) PTR - Points an IP address to a domain name SRV - Specifies the servers that host specific services NAPTR - Records the Naming Authority Pointer (NAPTR) and is usually used in ENUM CAA - Specifies which certificate authorities (CAs) are allowed to issue certificates for a domain name NS - Points a subdomain to other DNS servers If you set Load Balancing Policy to Weight, you can select one of the following types: A - Points a domain name to an IPv4 address AAAA - Points a domain name to an IPv6 address CNAME - Points one domain name to another |
|---|---|
| TTL (Seconds) | TTL indicates the cache time (in seconds) of record values on a local DNS server. The value ranges from 0 to 2147483647. The value 0 indicates that the record values are not cached. If your IP addresses frequently change, specify a small TTL value. If your IP address do not frequently change, specify a large TTL value. |
| Resolution Line | Select one or more lines. |
| Record Values | Add a record value collection. Value: Enter a record value based on the selected Record Type. For more information about how to enter the value, see Record value format. Weight: Enter a weight. The value must be an integer from 0 to 999. A larger value indicates a greater weight. This parameter is required only if you set Load Balancing Policy to Weight. Note Click Add Entry to add multiple record values. Click in the Actions column of the target record value to delete the record value. |

**Record value format**

| Record type | Record value format requirements |
|---|---|
| A - Points a domain name to an IPv4 address | Enter an IPv4 address in each row. You can enter a maximum of 100 unique record values in multiple rows. Format: Standard IPv4 address format. Examples: 192.168.1.1 192.168.1.2 192.168.1.3 |
| AAAA - Points a domain name to an IPv6 address | Enter an IPv6 address in each row. You can enter a maximum of 100 unique IP addresses in multiple rows. Format: Standard IPv6 address format. Examples: 2400:3200::6666 2400:3200::6688 2400:3200::8888 |
| CNAME - Points one domain name to another | Enter a domain name in each row. You can enter a maximum of 100 unique domain names in multiple rows. Format: A fully qualified domain name (FQDN) that ends with a period (.) and is up to 254 ASCII characters in length. Example: www.example.com. |
| MX - Points a domain name to an email server address | Enter one mail server record per line. You can enter up to 100 unique records. Format: [Priority] [Mail server hostname] Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Mail server hostname: An FQDN that ends with a period (.) and is up to 254 ASCII characters in length. Examples: 10 mailserver1.example.com. 20 mailserver2.example.com. |
| TXT - Serves as a Sender Policy Framework (SPF) record to protect against spam (Maximum length: 255 characters) | Enter one text string per line. You can enter up to 100 unique text strings. Format: Each text string cannot be empty and can be up to 254 ASCII characters in length. Example: v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all |

| PTR - Points an IP address to a domain name | Enter one domain name per line. You can enter up to 100 unique domain names. Format: An FQDN that ends with a period (.) and is up to 254 ASCII characters in length. Examples: www1.example.com. www2.example.com. www3.example.com. |
|---|---|
| SRV - Specifies the servers that host specific services | Enter one application service record per line. You can enter up to 100 unique records. Format: [Priority] [Weight] [Port] [Application server hostname] Priority: An integer from 0 to 999. A smaller value indicates a higher priority. Weight: An integer from 0 to 999. A larger value indicates a greater weight. Port: An integer from 0 to 65535, which indicates the TCP or UDP port number. Application server hostname: An FQDN that ends with a period (.) and is up to 254 ASCII characters in length. Examples: 1 10 8080 www1.example.com. 2 20 8081 www2.example.com. |

| NAPTR - Records the Naming Authority Pointer (NAPTR) and is usually used in ENUM | Enter one NAPTR record per line. You can enter up to 100 unique records. Format: [Ordinal number] [Priority] [Flag] [Service information] [Regular expression] [Replacement domain name] Ordinal number: An integer from 0 to 999. A smaller value is processed first. Priority: An integer from 0 to 999. For records with the same ordinal number, the one with the smaller priority value is processed first. Flag: This can be empty or a single character from A-Z, a- z, or 0-9. The value is case-insensitive and must be enclosed in double quotation marks (""). Service information: This can be empty or a string of up to 32 ASCII characters. It must start with a letter and be enclosed in double quotation marks (""). Regular expression: This can be empty or a string of up to 255 ASCII characters. It must be enclosed in double quotation marks (""). Replacement domain name: An FQDN that ends with a period (.) and is up to 254 ASCII characters in length. Examples: 100 50 "S" "Z3950+I2L+I2C" "" z3950. tcp.example.com. _ _ 100 50 "S" "RCDS+I2C" "" rcds. udp.example.com. _ _ 100 50 "S" "HTTP+I2L+I2C+I2R" "" http. tcp.example.com. _ _ |
|---|---|
| CAA - Specifies which certificate authorities (CAs) are allowed to issue certificates for a domain name | Enter one CAA record per line. You can enter up to 100 unique records. Format: [Flag] [Tag] [Value] Flag: An integer from 0 to 255. Tag: Supported values are issue, issuewild, and iodef. Value: This cannot be empty. It can be up to 254 ASCII characters in length and must be enclosed in double quotation marks (""). Examples: 0 issue "caa.example.com" 0 issuewild ";" 0 iodef "mailto:example@example.com" |

| NS - Points a subdomain to other DNS servers | Enter one DNS server address per line. You can enter up to 100 unique addresses. Format: An FQDN that ends with a period (.) and is up to 254 ASCII characters in length. Wildcard domain names are not allowed. Examples: ns1.example.com. ns2.example.com. |
|---|---|

**More operations**

After you add DNS records, you can perform the following operations in the DNS record list. View DNS records You can view the added DNS records, including **Record Name/ID**, **Record Type**,
**Record Values**, **TTL (Seconds)**, **Description**, **Load Balancing Policy**, and **Last**
**Modified At**.
You can use **Advanced Search** to search by **Record name**. Click the icon in the upper-right corner of the list to show or hide columns, and drag the columns to reorder them. View load balancing policy (Weight) Find the target DNS record and click **Weight** in the **Load Balancing Policy** column. In the dialog box that opens, you can view the details of the configured load balancing policy. Modify a DNS record Find the target DNS record and click **Modify** in the **Actions** column. In the **Modify DNS**
**Record** dialog box, modify the settings and then click **OK**. For more information about the
settings, see Add a DNS record. Add a description for a DNS record Find the target DNS record and click **Description** in the **Actions** column. In the **Add**
**Description** dialog box, enter a description in the **Description** field, and then click **OK**.
Delete a DNS record Find the desired DNS record, click **Delete** in the **Actions** column, and then click **OK**. Delete multiple DNS records at a time Select the DNS records that you want to delete. Click **Batch Delete** in the lower-left corner of the page, and then click **OK**. ines

## Resolution lines

A resolution line is an address library that identifies the source of a Domain Name System (DNS) request. Resolution lines can be referenced by cross-cloud shared domain names.

### Add and manage lines

**Add a line**

1. Log on to the DNS console.
2. In the navigation pane on the left, choose **Cross-cloud Domain Name Service > DNS**
**Lines**.
3. On the **Resolution Line** page, click **Add Line**.
4. In the **Add Line** dialog box, set the following parameters.

| Parameter | Description |
|---|---|
| Line Name | Enter a line name. |
| Sorting Method | Select a sorting behavior. Insert at the Beginning Insert at the End Insert Before Selected Line Note The line sorting number determines the priority of the line. A smaller number indicates a higher priority. |
| Insert Before Current Line | Select the line to insert the new line before. Note This parameter is required if you set Sorting Method to Insert Before Selected Line. |

ines

| IPv4 Address Range | Enter the IPv4 address range. You must specify either an IPv4 Address Range or an IPv6 Address Range. Format: Standard IPv4 address format Example: 192.168.1.1 192.168.1.2 Note Enter an IPv4 address in one row. You can enter up to 1,000 IPv4 addresses in multiple rows.. |
|---|---|
| IPv6 Address Range | Enter the IPv6 address range. You must specify either an IPv4 Address Range or an IPv6 Address Range. Format: Standard IPv6 address format Example: 2400:3200::6666 2400:3200::6688 Note Enter one IPv6 address per line. You can enter a maximum of 1,000 lines. Duplicate entries are not allowed. |

5. Click **OK**.

**More operations**

**Query lines**

On the **Resolution Line** page, you can view the added lines in the list. The list includes **Line**
**Name/ID**, **Line SN**, **IPv4 Address**, **IPv6 Address**, **Created At**, and **Last Modified At**.
Click **Advanced Filter** and enter filter conditions to find a specific line. Click the icon in the upper-right corner of the list to show or hide list items, or drag items to reorder them.

**Modify a line**

1. On the **Resolution Line** page, find the target line and click **Modify** in the **Actions** column.
2. In the **Modify Line** dialog box, modify the **Line Name**, **IPv4 Address Range**, or **IPv6**
**Address Range**, and then click **OK**.
You must specify either an **IPv4 Address Range** or an **IPv6 Address Range**. ines

**Sort lines**

1. On the **Resolution Line** page, find the target line and click **Sort** in the **Actions** column.
2. In the **Sort Line** dialog box, set the **Sorting Method** and click **OK**.

**Delete a line**

To delete a line, you must first dissociate it from all scheduling instances.
1. (Method 1) On the **Resolution Line** page, find the target line and click **Delete** in the
**Actions** column.
(Method 2) On the **Resolution Line** page, select one or more target lines, and then click
**Batch Delete** in the lower-left corner.
2. In the dialog box that appears, click **OK**.
