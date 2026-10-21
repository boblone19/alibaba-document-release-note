---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Express%20Connect%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect User Guide 20220928

## Table of Contents

- 1 What is Express Connect?
- 2 Log on to the Express Connect console
- 3 Connect two VPCs
- 4 Delete a peering connection

?

## 1 What is Express Connect?

This topic provides an overview of Express Connect. Express Connect allows you to establish private connections to enable fast, stable, and secure communication between different networking environments. You can use Express Connect to ensure network stability and prevent data breaches. Features You can use a leased line provided by an Internet Service Provider (ISP) to establish a physical connection between your data center and an Alibaba Cloud access point. After the physical connection is established, you can create a virtual border router (VBR) to connect your data center with Alibaba Cloud to build a hybrid cloud. The physical connections of Express Connect do not traverse the Internet, and therefore feature faster speeds, lower latency, greater security, and higher reliability compared with Internet connections. Express Connect enables you to create a peering connection between two Virtual Private Clouds (VPCs) as a channel for private communication. Benefits Express Connect provides the following benefits: High-speed interconnections Powered by the network virtualization technology of Alibaba Cloud, Express Connect allows networks to connect and exchange traffic at high speeds within internal networks without carrying traffic across the Internet. The impact of distance on network performance is minimized to ensure low-latency and high-bandwidth communication. Stability and reliability Built on the state-of-the-art infrastructure of Alibaba Cloud, Express Connect guarantees stable and reliable communication between networks. Security Express Connect implements cross-network communication at the network virtualization layer, where data is transmitted over separate and private channels within the infrastructure of Alibaba Cloud, mitigating the risks of data breaches. Buy-as-you-need service Express Connect delivers connectivity with a wide range of bandwidth options. You can choose based on the needs of your business to get the best value for your purchase. nnect console

## 2 Log on to the Express Connect console

console This topic provides an example of how to log on to the Apsara Stack Cloud Management (ASCM) console and then access Express Connect by using Google Chrome . Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net working > Express Connect .

## 3 Connect two VPCs

This topic describes how to create a peering connection to connect two VPCs. Procedure
1. Log on to the Express Connect console.
2. In the left-side navigation pane, choose VPC Peering Connect ions > VPC-t o-VPC.
3. On the VPC Peering Connect ionspage, click Creat e Peering Connect ion.
4. Specify the following information to configure the peering connection.

| Parameter | Description |
|---|---|
| Scenario | Select VPC-t o-VPC to create a peering connection between two VPCs. |
| Source Conf igurat ions |   |
| Organizat ion | Select the organization to which the source VPC belongs. |
| Resource Set | Select the resource set to which the source VPC belongs. |
| Region | Select the region where the source VPC resides. |
| Rout er T ype | Use the default VRout er setting. |
| Source VPC ID | Select the ID of the source VPC (initiator or acceptor of this peering connection). |
| Source Rout er | Select the router of the source VPC (initiator or acceptor of this peering connection). |
| Destination Configurations |   |

| User | Guide·Connect two VPCs Express Connec | t |
|---|---|---|

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the destination VPC belongs. |
| Resource Set | Select the resource set to which the destination VPC belongs. |
| Dest inat ion Region | Select the region where the destination VPC resides. |
| Dest inat ion Rout er T ype | Use the default VRout er setting. |
| Dest inat ion VPC ID | Select the ID of the destination VPC (initiator or acceptor of this peering connection). |
| Dest inat ion Rout er | Select the router of the destination VPC (initiator or acceptor of this peering connection). |
| Basic Settings |   |
| Bandwidt h | Select a bandwidth for the peering connection. |

5. Click Submit .
tion

## 4 Delete a peering connection

This topic describes how to delete a peering connection. Procedure
1. Log on to the Express Connect console.
2. In the left-side navigation pane, choose VPC Peering Connect ions > VPC-t o-VPC.
3. Find the target peering connection and choose
> Suspend Init iat or in the Act ions column.

4. Find the target peering connection and choose
> Suspend Accept or in the Act ions column.

5. Find the target peering connection and choose
> Delet e in the Act ions column.

6. In the Delet e Peering Connect ion dialog box, click Conf irm.
