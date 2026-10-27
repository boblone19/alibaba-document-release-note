---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 38
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20VPN%20Gateway%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway User Guide 20220928

## Table of Contents

- 1 What is VPN Gateway?
- 2 Log on to the VPN Gateway console
- 3 Get started with IPsec-VPN
  - 3.1 Connect on-premises data centers to VPC networks
- 4 Get started with SSL-VPN
  - 4.1 Initiate a connection from a Linux client
  - 4.2 Initiate a connection from a Windows client
  - 4.3 Initiate a connection from a macOS client
- 5 Manage a VPN Gateway
  - 5.1 Create a VPN gateway
  - 5.2 Modify a VPN gateway
  - 5.3 Configure routes of a VPN Gateway
    - 5.3.1 VPN Gateway route overview
    - 5.3.2 Add a policy-based route entry
    - 5.3.3 Add a destination-based route entry
  - 5.4 Delete a VPN gateway
- 6 Manage a customer gateway
  - 6.1 Create a customer gateway
  - 6.2 Modify a customer gateway
  - 6.3 Delete a customer gateway
- 7 Configure SSL-VPN
  - 7.1 Configuration overview
  - 7.2 Manage an SSL server
    - 7.2.1 Create an SSL Server
    - 7.2.2 Modify an SSL server
    - 7.2.3 Configure a routing group
    - 7.2.4 Delete an SSL server
  - 7.3 Manage an SSL client certificate
    - 7.3.1 Create an SSL client certificate
    - 7.3.2 Download an SSL client certificate
    - 7.3.3 Delete an SSL client certificate
- 8 Configure IPsec-VPN connections
  - 8.1 Configuration overview
  - 8.2 Manage an IPsec-VPN connection
    - 8.2.1 Create an IPsec-VPN connection
    - 8.2.2 Modify an IPsec-VPN connection
    - 8.2.3 Download the configuration file of an IPsec-VPN connection
    - 8.2.4 Configure a routing group
    - 8.2.5 View IPsec-VPN connection logs
    - 8.2.6 Delete an IPsec-VPN connection
  - 8.3 MTU notes

## 1 What is VPN Gateway?

VPN Gateway is an Internet-based service that allows you to connect enterprise data centers, office networks, or Internet-facing terminals to Alibaba Cloud Virtual Private Cloud (VPC) networks through secure and reliable connections. VPN Gateway supports both IPsec-VPN connections and SSL-VPN connections. Not e The Alibaba Cloud VPN Gateway service complies with the local regulations and policies. VPN Gateway does not provide Internet access services. Features VPN Gateway supports the following features: IPsec-VPN Route-based IPsec-VPN allows you to route network traffic in multiple ways, and also facilitates the configuration and maintenance of VPN policies. You can use IPsec-VPN to connect an on-premises data center to a VPC network or connect two VPC networks. IPsec-VPN supports the IKEv1 and IKEv2 protocols. Any devices that support these two protocols can connect to Alibaba Cloud VPN Gateway, such as devices manufactured by Huawei, H3C, Hillstone, Sangfor, Cisco ASA, Juniper, SonicWall, Nokia, IBM, and Ixia. SSL-VPN SSL-VPN is implemented based on the OpenVPN framework. You can create an SSL-VPN connection to connect a remote client to applications and services deployed in a VPC network. After you deploy your applications or services, you only need to import the certificate to the client to initiate a connection. Benefits VPN Gateway offers the following benefits: High security: You can use the IKE and IPsec protocols to encrypt data for secure and reliable data transmission. High availability: VPN Gateway adopts the hot-standby architecture to achieve failover within a few seconds, session persistence, and zero service downtime. Cost-effectiveness: The encrypted Internet connections provided by VPN Gateway are more costeffective than leased lines. Ease of use: VPN Gateway is a ready-to-use service. VPN gateways start to work immediately after they are deployed. way console

## 2 Log on to the VPN Gateway console

console This topic describes how to use Google Chrome to log on to the VPN Gateway console in Apsara Stack Cloud Management (ASCM). Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net working > VPN Gat eway.
PN

## 3 Get started with IPsec-VPN

### 3.1 Connect on-premises data centers to VPC networks

centers to VPC networks This topic describes how to create IPsec-VPN connections on VPN gateways to connect an on-premises data center to a Virtual Private Cloud (VPC) network. Prerequisites Before you start, make sure that the following requirements are met: Check the gateway device in the on-premises data center. Alibaba Cloud VPN gateways support the standard IKEv1 and IKEv2 protocols. Any gateway device that supports these two protocols can connect to Alibaba Cloud VPN gateways, such as gateway devices manufactured by H3C,Huawei, Hillstone, Sangfor, Cisco ASA, Juniper, SonicWall, Nokia, IBM, and Ixia. Make sure that you have set a static public IP address for the gateway device in the on-premises data center. The CIDR block of the on-premises data center must not overlap with that of the VPC network. Context For example, a company creates a VPC network on Alibaba Cloud. The CIDR block of the VPC network is 192.168.0.0/16. The CIDR block of the on-premises data center is 172.16.0.0/12. The static public IP address for the gateway device in the on-premises data center is 211.xx.xx.68. To meet business requirements, the company needs to connect the on-premises data center to the VPC network. The preceding figure displays that the on-premises data center is connected to the VPC network through IPsec-VPN. Cloud resources can be shared with on-premises data centers. Step 1: Create a VPN gateway Take the following steps to create a VPN gateway:
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where you want to deploy the VPN gateway. PN Make sure that the VPC network and the VPN gateway associated with the VPC network are deployed in the same region. Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter or Chinese character and cannot start with `http://` or `https://` . VPC: Select the VPC network to be associated with the VPN gateway. Bandwidt h: Specify the maximum bandwidth of the VPN gateway. The bandwidth is provided for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, select Enable. After IPsec-VPN is enabled, you can create IPsec-VPN connections between an on-premises data center and a VPC network, or between two VPC networks. SSL-VPN: Specify whether to enable SSL-VPN. In this example, select Disable. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a customer gateway. SSL Connect ions: Specify the maximum number of concurrent SSL connections that the VPN gateway supports. Not e This parameter is available only after SSL-VPN is enabled.
5. Go to the VPN Gateways page to view the newly created VPN gateway.
The newly created VPN gateway is in the Preparing state. Its status changes to Normal after about two minutes. The Normal state indicates that the VPN gateway is initialized and ready for use. Not e It takes about one to five minutes to create a VPN gateway. Step 2: Create a customer gateway Take the following steps to create a customer gateway.
1. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
2. Select the region where you want to deploy the customer gateway
3. On the Cust omer Gat eways page, click Creat e Cust omer Gat eway.
4. On the Creat e Cust omer Gat eway page, set the following parameters, and click Submit .
Organizat ion: Select the organization to which the customer gateway belongs. Resource Set : Select the resource set to which the customer gateway belongs. Region: Select the region where you want to deploy the customer gateway. Not e Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region. Zone: Select the zone where you want to deploy the customer gateway. PN Name: Enter a name for the customer gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). It must start with a letter or Chinese character and cannot start with `http://` or `https://` . IP Address: Enter the public IP address of the gateway device in the on-premises data center that is to be connected to the VPC network. In this example, enter 211.xx.xx.68. Descript ion: Enter a description for the customer gateway. The description must be 2 to 256 characters in length, and cannot start with `http://` or `htt` `ps://` . Step 3: Create an IPsec-VPN connection Take the following steps to create an IPsec-VPN connection:
1. In the left-side navigation pane, choose VPN > IPsec Connect ions.
2. Select the region where you want to create an IPsec-VPN connection.
3. On the IPsec Connect ions page, click Creat e IPsec Connect ion.
4. On the Creat e IPsec Connect ion page, set the following parameters for the IPsec-VPN
connection, and click Submit . Organizat ion: Select the organization to which the IPsec-VPN connection belongs. Resource Set : Select the resource set to which the IPsec-VPN connection belongs. Region: Select the region where the IPsec-VPN connection is established. Zone: Select the zone where the IPsec-VPN connection is established. Name: Enter a name for the IPsec-VPN connection. VPN Gat eway: Select a VPN gateway. Cust omer Gat eway: Select the customer gateway to be connected through the IPsec-VPN connection. Source CIDR Block: Enter the CIDR block of the VPC network with which the selected VPN gateway is associated. In this example, enter 192.168.0.0/16. Dest inat ion CIDR Block: Enter the CIDR block of the on-premises data center. In this example, enter 172.16.0.0/12. Immediat e Ef f ect : Specify whether to start connection negotiations immediately. Yes: negotiate immediately after the configuration is complete. No: negotiate when traffic is detected in the IPsec-VPN connection. Pre-shared Key: Enter the pre-shared key. The pre-shared key must be the same as that of the gateway device deployed in the on-premises data center. Use the default settings for other parameters. Step 4: Load the configurations of the IPsec-VPN connection to the customer gateway device Take the following steps to load the configurations of the IPsec-VPN connection to the customer gateway device: PN
1. In the left-side navigation pane, choose VPN > IPsec Connect ions.
2. Select the region where the IPsec-VPN connection is established.
3. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
Download Conf igurat ion in the Act ions column.
4. Load the configurations of the IPsec-VPN connection to the customer gateway device by
following the instructions described in . For more information about how to configure customer gateways, consult the manufacturers of the gateway devices. RemotSubnet and LocalSubnet in the downloaded configurations are opposite to RemotSubnet and LocalSubnet that you specify when you create an IPsec-VPN connection. For a VPN gateway, RemotSubnet refers to the CIDR block of the on-premises data center and LocalSubnet refers to the CIDR block of the VPC network. For a customer gateway, LocalSubnet refers to the CIDR block of the on-premises data center and RemoteSubnet refers to the CIDR block of the VPC network. Step 5: Configure routes for the VPN gateway Take the following steps to configure routes for the VPN gateway:
1. In the left-side navigation pane, choose VPN > VPN Gat eways.
2. Select the region where the VPN gateway is deployed.
3. On the VPN Gat eways page, find the target VPN gateway, and then click the instance ID in the
Inst ance ID/Name column.
4. In the Dest inat ion-based rout ing tab, click Add Rout e Ent ry.
5. In the Add Rout e Ent ry dialog box, set the following parameters and click OK.
Dest inat ion CIDR Block: Enter the CIDR block of the on-premises data center. In this example, enter 172.16.0.0/12. Next Hop T ype: Select IPsec Connection. Next Hop: Select an IPsec instance. Publish t o VPC: Specify whether to automatically publish new route entries to the VPC route table. In this example, select Yes. Weight : Select a weight. In this example, select 100. Step 6: Verify the settings Log on to an Elastic Compute Service (ECS) instance that is not assigned a public IP address in the VPC network. Run the ping command to ping the private IP address of a server that resides in the onpremises data center, and test the connectivity. N

## 4 Get started with SSL-VPN

### 4.1 Initiate a connection from a Linux client

client This topic describes how to use SSL-VPN to connect a Linux client to a Virtual Private Cloud (VPC) network. Prerequisites Before you start, make sure that the following requirements are met: The CIDR block of the VPC network must not overlap with that of the client. Otherwise, the client cannot communicate with the VPC network. The client must be able to access the Internet. Context The following scenario is used as an example. Step 1: Create a VPN gateway Take the following steps to create a VPN gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, specify the following parameters for the VPN gateway, and
then click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where the VPN gateway is deployed. Make sure that the VPC network and the VPN gateway associated with the VPC network are deployed in the same region. N Inst ance Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter or Chinese character, and cannot start with `http://` or `https://` . VPC: Select the VPC network to be associated with the VPN gateway. Bandwidt h: Specify the maximum bandwidth of the VPN gateway. The bandwidth is provided for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, select Disable. SSL-VPN: Specify whether to enable SSL-VPN for the VPN gateway. In this example, select Enable. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a gateway for the client. SSL Connect ions: Specify the maximum number of concurrent SSL connections that the VPN gateway supports.
5. Go to the VPN Gateways page to view the newly created VPN gateway.
The newly created VPN gateway is in the Preparing state. Its status changes to Normal after about two minutes. The Normal status indicates that the VPN gateway is initialized and ready for use. Not e It takes about one to five minutes to create a VPN gateway. Step 2: Create an SSL server Take the following steps to create an SSL server.
1. In the left-side navigation pane, choose VPN > SSL Servers.
2. Select the region where you want to create the SSL server.
3. On the SSL Servers page, click Creat e SSL Server.
4. On the Creat e SSL Server page, set the following parameters for the SSL server, and then click
Submit . Organizat ion: Select the organization to which the SSL server belongs. Resource Set : Select the resource set to which the SSL server belongs. Region: Select the region where you want to deploy the SSL server. Zone: Select the zone where you want to deploy the SSL server. Name: Enter a name for the SSL server. VPN Gat eway: Select a VPN gateway from the drop-down list. Source CIDR Block: Enter the CIDR block of the VPC network. Click +Add Local Net work to add more CIDR blocks. You can add the CIDR block of a VPC network, a VSwitch, and a local network. Client CIDR Block: Enter the CIDR block of the client. The client connects to the SSL server from the specified CIDR block. Advanced Set t ings: Specify whether to customize the advanced settings. In this topic, the default settings are used. N Step 3: Create and download an SSL client certificate Take the following steps to create and download an SSL client certificate.
1. In the left-side navigation pane, choose VPN > SSL Client s.
2. Select the region where the client is created.
3. On the SSL Client s page, click Creat e Client Cert if icat e.
4. On the Creat e SSL Client Cert if icat e page, set the following parameters for the SSL client, and
then click Submit . Organizat ion: Select the organization to which the SSL client certificate belongs. Resource Set : Select the resource set to which the SSL client certificate belongs. Region: Select the region where you want to create the SSL client certificate. Zone: Select the zone where you want to create the SSL client certificate. Name: Enter a name for the SSL client certificate. VPN Gat eway: Select the VPN gateway to be associated with the SSL client certificate. SSL Server: Select the SSL server to which you want to import the SSL client certificate.
5. On the SSL Client s page, find the target SSL client certificate, and then click Download in the
Act ions column. Step 4: Configure the client Take the following steps to configure the Linux client:
1. Run the following command to install the OpenVPN:

```bash
yum install -y openvpn
```

2. Decompress the client certificate package that you downloaded in Step 3 and copy the client
certificate file to the /etc/openvpn/conf/ folder where OpenVPN is installed.
3. Run the following command to launch OpenVPN:

```
openvpn --config /etc/openvpn/conf/config.ovpn --daemon
```

Step 5: Test the connectivity To test the connectivity, run the ping command to ping the connected ECS instance in the VPC network. Not e Make sure that the security group rules of the ECS instance allow remote access from Linux clients.

### 4.2 Initiate a connection from a Windows client

Windows client This topic describes how to use SSL-VPN to connect a Windows client to a Virtual Private Cloud (VPC) network. N Context The following scenario is used as an example. Step 4: Configure the client Take the following steps to configure the Windows client: Not ice You must run the client as an administrator.
1. Download and install OpenVPN.
2. Decompress the client certificate package that you downloaded in Step 3 and copy the client
certificate file to the config folder where OpenVPN is installed.
3. Click Connect to initiate a connection.

### 4.3 Initiate a connection from a macOS client

macOS client N This topic describes how to use SSL-VPN to connect a macOS client to a Virtual Private Cloud (VPC) network. Context The following scenario is used as an example. Step 4: Configure the client Take the following steps to configure the macOS client:
1. Run the following command to install OpenVPN:

```
brew install openvpn
```

Not e If Homebrew is not installed, install Homebrew first.
2. Decompress the client certificate package that you downloaded in Step 3, copy the client
certificate file to the folder where OpenVPN is installed, and initiate a connection. i. Back up the default configuration file. ii. Run the following command to delete the default configuration file:

```
rm /usr/local/etc/openvpn/*
```

iii. Run the following command to copy the file to the configuration directory:

```
cp cert_location /usr/local/etc/openvpn/
```

In the preceding command, `cert_location` represents the path that stores the certificate downloaded in Step 3, for example, /Users/example/Downloads/certs6.zip. iv. Run the following command to decompress the client certificate package:

```
cd /usr/local/certificates unzip /usr/local/etc/openvpn/certs6.zip
```

v. Run the following command to initiate a connection:

```python
sudo /usr/local/opt/openvpn/sbin/openvpn --config /usr/local/etc/openvpn/config.ovp
```

`n`

## 5 Manage a VPN Gateway

### 5.1 Create a VPN gateway

This topic describes how to create a VPN gateway. You must create a VPN gateway before you can use the IPsec-VPN and SSL-VPN services. After the VPN gateway is created, a public IP address is assigned to the VPN gateway. Procedure
1. Log on to the VPN Gateway console.
2.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN page, specify the following parameters for the VPN gateway, and then click
Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VPN gateway belongs. |
| Resource Set | Select the resource set to which the VPN gateway belongs. |
| Region | Select the region where the VPN gateway is deployed. You can use IPsec-VPN to connect an on-premises data center to a VPC network or connect two VPC networks. Make sure that the VPC network and the VPN gateway associated with the VPC network are deployed in the same region. |
| Inst ance Name | Enter a name for the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a letter _ or Chinese character and cannot start with http:// or https:// . |
| VPC | Select the VPC network to be associated with the VPN gateway. |
| Bandwidt h | Specify the maximum bandwidth of the VPN gateway. The bandwidth is provided for data transfer over the Internet. |
| IPsec-VPN | Specify whether to enable IPsec-VPN for the VPN gateway. After IPsec-VPN is enabled, you can create IPsec-VPN connections between an on-premises data center and a VPC network, or between two VPC networks. |
| SSL-VPN | Specify whether to enable SSL-VPN for the VPN gateway. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a customer gateway. |

| Parameter | Description |
|---|---|
| SSL Connect ions | Specify the maximum number of concurrent SSL connections that the VPN gateway supports. Not e This parameter is available only after SSL-VPN is enabled. |

### 5.2 Modify a VPN gateway

This topic describes how to modify the name and description of a VPN gateway. Prerequisites A VPN gateway is created. For more information, see Create and manage a VPN gateway. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. Select the region where the VPN gateway is deployed.
4. On the VPN Gat eways page, find the target VPN gateway, and click the
icon in the Inst ance ID/Name column. In the dialog box that appears, enter a new name and click OK. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.
5. Click the
icon in the Descript ion column. In the dialog box that appears, enter a new description and click OK. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.

### 5.3 Configure routes of a VPN Gateway

Gateway

#### 5.3.1 VPN Gateway route overview

After you create an IPsec-VPN connection, you must manually add a VPN Gateway route. The route-based IPsec-VPN enables you to easily configure and maintain VPN policies, and provides flexible ways for routing traffic. You can add the following two types of routes for a VPN Gateway: Policy-based routes. Destination-based routes. Policy-based route If a policy-based route is used, traffic is forwarded based on both the source IP address and the destination IP address. For more information, see Add a policy-based route entry. Not e Policy-based routes take precedence over destination-based routes. Destination-based route If a destination-based route is used, traffic is forwarded based only on the destination IP address. For more information, see Add a destination-based route entry.

#### 5.3.2 Add a policy-based route entry

This topic describes how to add a policy-based route entry after an IPsec-VPN connection is created. Policy-based routing (PBR) is a technique that routes packets based on source and destination IP addresses. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the VPN Gat eways page, find the target VPN gateway and click the instance ID in the
Inst ance ID/Name column.
5. Click the Policy-based Rout ing tab, and then click Add Rout e Ent ry.
6. In the Add Rout e Ent ry dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Dest inat ion CIDR Block | The CIDR block that you want to access. |
| Source CIDR Block | The CIDR block of the VPC network. |
| Next Hop T ype | Select IPsec Connection. |
| Next Hop | Select an IPsec instance to create an IPsec-VPN connection. |
| Publish t o VPC | Specify whether to automatically publish new route entries to the VPC route table. Yes (Recommended): automatically publishes new route entries to the VPC route table. No: does not automatically publish new route entries to the VPC route table. Not e If you select No, you must manually publish new route entries to the VPC route table. |

| Parameter | Description |
|---|---|
| Weight | Select a weight. Valid values: 100: indicates that the priority of the route entry is high. 0: indicates that the priority of the route entry is low. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |

#### 5.3.3 Add a destination-based route entry

This topic describes how to manually add a destination-based route entry after an IPsec-VPN connection is created. Destination-based routing is a technique that routes packets to specified destination IP addresses. Procedure
1. Log on to the VPN Gateway console.
2. 3. 4.
5. In the Dest inat ion-based rout ing tab, click Add Rout e Ent ry.
6. In the Add Rout e Ent ry dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Dest inat ion CIDR Block | The CIDR block that you want to access. |
| Next Hop T ype | Select IPsec Connection. |
| Next Hop | Select an IPsec instance to create an IPsec-VPN connection. |
| Publish t o VPC | Specify whether to automatically publish new route entries to the VPC route table. Yes (Recommended): automatically publishes new route entries to the VPC route table. No: does not automatically publish new route entries to the VPC route table. Not e If you select No, you must manually publish new route entries to the VPC route table. |

| Parameter | Description |
|---|---|
| Weight | Select a weight. Valid values: 100: indicates that the priority of the route entry is high. 0: indicates that the priority of the route entry is low. Not e If two destination-based route entries are configure with the same destination CIDR block, you cannot set the weights of both route entries to 100. |

### 5.4 Delete a VPN gateway

This topic describes how to delete a VPN gateway. After you delete a VPN gateway, you can no longer use the VPN gateway to establish IPsec-VPN or SSL-VPN connections. Context Before you delete a VPN gateway, make sure that the following conditions are met: The IPsec-VPN connections on the VPN gateway are deleted. For more information, see and Delete an IPsec-VPN connection. The SSL server associated with the VPN gateway is deleted. For more information, see and Delete an SSL server. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. Select the region where the VPN gateway is deployed.
4. On the VPN Gat eways page, find the target VPN gateway, and then click Delet e in the Act ions
column.
5. In the Delet e VPN Gat eway dialog box, click OK.
eway

## 6 Manage a customer gateway

### 6.1 Create a customer gateway

This topic describes how to create a customer gateway when you use IPsec-VPN to connect a Virtual Private Cloud (VPC) network to an on-premises data center or connect two VPC networks. You can register and update the information of an on-premises gateway to Alibaba Cloud by creating a customer gateway, and then connect the customer gateway to the VPN gateway. A customer gateway can be connected to multiple VPN gateways. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, click VPN > Cust omer Gat eways.
3. Select the region where you want to deploy the customer gateway.
Not e Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region.
4. On the Cust omer Gat eways page, click Creat e Cust omer Gat eway.
5. On the Creat e Cust omer Gat eway page, set the following parameters, and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the customer gateway belongs. |
| Resource Set | Select the resource set to which the customer gateway belongs. |
| Region | Select the region where you want to deploy the customer gateway. Not e Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region. |
| Zone | Select the zone where you want to deploy the customer gateway |
| Name | Enter a name for the customer gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). It must start with a letter or Chinese _ character and cannot start with http:// or https:// . |
| IP Address | Enter the static public IP address of the gateway device that is deployed in the on-premises data center. |
| Descript ion | Enter a description for the customer gateway. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . |

eway

### 6.2 Modify a customer gateway

This topic describes how to modify the name and description of a customer gateway. Prerequisites A customer gateway is created. For more information, see Create a customer gateway. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
3. Select the region where the customer gateway is deployed.
4. On the Cust omer Gat eways page, find the target customer gateway, click the
icon in the Inst ance ID column. In the dialog box that appears, enter a name and click OK. The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.
5. Click the
icon in the Descript ion column. In the dialog box that appears, enter a new description and click OK. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.

### 6.3 Delete a customer gateway

This topic describes how to delete a customer gateway. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the Cust omer Gat eways page, find the target customer gateway, and then click Delet e in
the Act ions column.
5. In the message that appears, click OK.

## 7 Configure SSL-VPN

### 7.1 Configuration overview

This topic describes how to use the SSL-VPN function to connect a remote client to a VPC. Environment requirements Before you use SSL-VPN to establish a connection between a client and a VPC, make sure that the following requirements are met: The private CIDR block of the client does not overlap with the private CIDR block of the VPC. Otherwise, the client and the VPC cannot communicate with each other. The client can access the Internet. You have read and understand the security group rules that apply to the Elastic Compute Service (ECS) instances in the VPC, and make sure that the security rules allow the client to access the ECS instances. Procedure
1. Create a VPN gateway.
Create a VPN gateway and enable the SSL-VPN feature.
2. Create an SSL server.
On the SSL server, specify the private CIDR block that the client needs to access and the CIDR block that is used by the client.
3. Create an SSL client certificate.
Create and download a client certificate based on the SSL server configuration.
4. Configure the client.
Download and install VPN software on the client, load the SSL client certificate, and then initiate an SSL-VPN connection.
5. Verify the connectivity.
Open the CLI on the client, and run the ping command to ping an ECS instance in the VPC.

### 7.2 Manage an SSL server

#### 7.2.1 Create an SSL Server

This topic describes how to create an SSL server. Before you use SSL-VPN to establish point-to-site connections, you must create an SSL server. A VPN gateway is created and SSL-VPN is enabled. For more information, see Create a VPN gateway. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. In the top navigation bar, select the region where you want to create the SSL server.
4. On the SSL Servers page, click Creat e SSL Server.
5. On the Creat e SSL Server page, configure the SSL server based on the following information, and
then click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the SSL server belongs. |
| Resource Set | Select the resource set to which the SSL server belongs. |
| Region | Select the region where the SSL server is to be deployed. |
| Zone | Select the zone where the SSL server is to be deployed. |
| Name | Enter a name for the SSL server. The name must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). It must start with a letter or Chinese _ character and cannot start with http:// or https:// . |
| VPN Gat eway | Select the VPN gateway to be associated with the SSL server. Make sure that SSL-VPN is enabled for the VPN gateway. |
| Source CIDR Block | Enter the CIDR block that the client needs to access through the SSL-VPN connection. It can be the CIDR block of a VPC network, a VSwitch, an on- premises data center connected to a VPC through a leased line, or a cloud service such as ApsaraDB for RDS or Object Storage Service (OSS). Click + to add more CIDR blocks. Not e The subnet mask of the specified server CIDR block must be 16 to 29 bits in length. |

| Parameter | Description |
|---|---|
| Client CIDR Block | Enter the CIDR block to be allocated to the virtual network interface of the client. Do not enter the CIDR block where the client resides. When the client accesses the server through an SSL-VPN connection, the VPN gateway selects an IP address from the specified CIDR block and assigns it to the client. Not e Make sure the server CIDR block and the client CIDR block do not overlap. |
| Advanced Set t ings | Specify whether to customize the advanced settings. Def ault : Use the default settings. Conf igure: Use custom settings. You can customize the following settings: Prot ocol: Select the protocol over which the SSL-VPN connection is established. Supported protocols are UDP and TCP. Port : Specify the port to which the SSL-VPN connection is established. The following ports are not supported: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. Encrypt ion Algorit hm: Select the encryption algorithm used by the SSL connection. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, and none. Compress: Specify whether to enable data compression. |

#### 7.2.2 Modify an SSL server

This topic describes how to modify the name, server CIDR block, client CIDR block, and advanced settings of an SSL server. Prerequisites An SSL server is created. For more information, see Create an SSL server. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the SSL Servers page, find the target SSL server, and then click Edit in the Act ions column.
5. On the Edit SSL Server page, modify the name, server CIDR block, client CIDR block, and advanced
settings of the SSL server, and then click OK.

#### 7.2.3 Configure a routing group

This topic describes how to configure a routing group to control the inbound and outbound traffic of an Elastic Compute Service (ECS) instance after you create an IPsec-VPN connection.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. Select the region where the SSL server is deployed.
4. On the SSL Servers page, find the target SSL server, and then click Conf igure Rout ing Group in
the Act ions column.
5. In the Conf igure Rout ing Group panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Securit y Group | Select the security group to which you want to add the security group rule. |
| Rule Direct ion | Select the direction of data transfer that the rule controls. Out bound: controls data transfer from the ECS instances in the security group to the Internet or other ECS instances. Inbound: controls data transfer from the Internet or other ECS instances to the ECS instances in the security group. |
| Act ion | Specify the action to be performed on the matching requests. Allow: accepts requests. Deny: drops requests without returning messages. If two security group rules use the same settings except for different actions, the Deny rule prevails over the Allow rule. |
| Prot ocol T ype | The protocol of the security group rule. |
| Port Range | Enter a port range for the security group rule. Valid values: -1 and 1 to 65535. You cannot enter only -1. Examples: 1/200 specifies ports 1 to 200. 80/80 specifies port 80. -1/-1 specifies all ports. |
| Priorit y | Set the priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Aut horizat ion Mode | Specify the type of addresses that the security group rule permits or blocks. You can select only Address, which indicates CIDR blocks. |
| ENI T ype | Specify the type of data transfer that the security group rule controls. Int ernal: controls data transfer within Alibaba Cloud. Ext ernal: controls data transfer over the Internet. |

| Guide·Configure SSL- | VPN VPN Gatewa |
|---|---|

| Parameter | Description |   |   |
|---|---|---|---|
| Aut horizat ion IP Addresses | Specify the CIDR blocks that you want the security group rule to accept or block. You can specify at most 10 CIDR blocks. |   |   |
| Enable Aut omat ically Conf igure Rout ers | Specify whether to automatically propagate routes. The feature is enabled by default. |   |   |
| Descript ion | Enter a description for the security group rule. The description must be 2 to 256 characters in length, and cannot start with htt p:// or https:// . You can leave this parameter empty. |   |   |
|   |   | htt |   |

|   | p:// |
|---|---|

#### 7.2.4 Delete an SSL server

This topic describes how to delete an SSL server. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the SSL Servers page, find the target SSL server, and then click Delet e in the Act ions column.
5. In the message that appears, click OK.

### 7.3 Manage an SSL client certificate

#### 7.3.1 Create an SSL client certificate

After you create an SSL server, you must create an SSL client certificate based on the configuration of the SSL server before you can establish an SSL-VPN connection. Prerequisites An SSL server is created. For more information, see Create an SSL server. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Client s page, click Creat e Client Cert if icat e.
5. On the Creat e SSL Client Cert if icat e page, configure the client certificate based on the
following information, and then click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the SSL client belongs. |
| Resource Set | Select the resource set to which the SSL client belongs. |
| Region | Select the region where the SSL client is deployed. |
| Zone | Select the zone where the SSL client is deployed. |
| Name | Enter a name for the SSL client certificate. The name must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). It must start with a letter or Chinese _ character and cannot start with http:// or https:// . |
| VPN Gat eway | Select the VPN gateway that is used to establish the SSL-VPN connection. |
| SSL Server | Select the SSL server to be associated with the SSL client. |

#### 7.3.2 Download an SSL client certificate

This topic describes how to download an SSL client certificate. Before you use an SSL client to initiate an SSL-VPN connection, you must import the SSL client certificate to the SSL client. Prerequisites An SSL client certificate is created. For information, see Create an SSL client certificate. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Client s page, find the target SSL client certificate, and then click Download in the
Act ions column.

#### 7.3.3 Delete an SSL client certificate

This topic describes how to delete an SSL client certificate. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the SSL Client s page, find the target SSL client certificate, and then click Delet e in the
Act ions column.
5. In the message that appears, click OK.
nections

## 8 Configure IPsec-VPN connections

connections

### 8.1 Configuration overview

This topic describes how to connect a VPC to an on-premises data center through IPsec-VPN. Prerequisites Before creating a site-to-site VPN connection, make sure the following conditions are met: The protocols IKEv1 and IKEv2 are supported by the gateway device of the on-premises data center. IPsec-VPN supports IKEv1 and IKEv2 protocols. Devices that support these two protocols can connect to Alibaba Cloud VPN Gateway, including devices of Huawei, H3C, Hillstone, SANGFOR, Cisco ASA, Juniper, SonicWall, Nokia, IBM, and Ixia. A static public IP address is configured for the local gateway. The IP address ranges of the VPC and on-premises data center to be connected do not conflict with each other. Procedure The following figure shows the procedure of connecting a VPC to an on-premises data center through IPsec-VPN. Enable the IPsec-VPN function. Up to 10 IPsec-VPN connections can be established in a VPN Gateway. By creating a customer gateway, you can register the local gateway to Alibaba Cloud and connect the customer gateway to the VPN Gateway. A customer gateway can be connected to multiple VPN Gateways.
3. Create an IPsec connection
An IPsec connection is a VPN channel established between a VPN Gateway and a customer gateway. The encrypted communication between the VPN Gateway and the on-premises data center can be achieved only after the IPsec connection is established.
4. Configure the local gateway
You need to load the VPN Gateway configurations to the local gateway device. nections
5. Configure the VPN Gateway route
You need to configure a route in the VPN Gateway and publish it to the VPC route table.
6. Test the connection
Log on to an ECS instance (without a public IP address) in the connected VPC. ping the private IP address of a server in the on-premises data center to check whether the connection is established.

### 8.2 Manage an IPsec-VPN connection

#### 8.2.1 Create an IPsec-VPN connection

This topic describes how to create an IPsec-VPN connection. After you create a VPN gateway and a customer gateway, you can create an IPsec-VPN connection between the two gateways for encrypted data transmission. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. Select the region where you want to create the IPsec-VPN connection.
4. On the IPsec Connect ions page, click Creat e IPsec Connect ion.
5. On the Creat e IPsec Connect ion page, configure the IPsec-VPN connection based on the
following information and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the IPsec-VPN connection belongs. |
| Resource Set | Select the resource set to which the IPsec-VPN connection belongs. |
| Region | Select the region where the IPsec-VPN connection is established. |
| Zone | Select the zone where the IPsec-VPN connection is established. |
| Name | Enter a name for the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). It must start with a letter or Chinese _ character and cannot start with http:// or https:// . |
| VPN Gat eway | Select the VPN gateway to be connected through the IPsec-VPN connection. |
| Cust omer Gat eway | Select the customer gateway to be connected through the IPsec-VPN connection. |
| Source CIDR Block | Enter the CIDR block of the VPC network to be connected to the on-premises data center. The CIDR block is used during phase 2 negotiation. You can add more than one CIDR blocks only if IKEv2 is used. |

nections

| Parameter | Description |
|---|---|
| Dest inat ion CIDR Block | Enter the CIDR block of the on-premises data center to be connected to the VPC network. This CIDR block is used during phase 2 negotiation. You can add more than one CIDR blocks only if IKEv2 is used. |
| Immediat e Ef f ect | Specify whether to start connection negotiations immediately. Yes: Negotiate immediately after the configuration is complete. No: Negotiate when traffic is detected in the IPsec-VPN tunnel. |
| Advanced Set t ings | Specify whether to customize the advanced settings. Def ault : Use default settings. Conf igure: Use custom settings. |
| Advanced conf igurat ion: IKE conf igurat ion |   |
| Pre-shared Key | Enter the pre-shared key used for authentication between the VPN gateway and customer gateway. You can specify a key, or use the default key that is randomly generated by the system. |
| Version | The version of the IKE protocol. Select an IKE version. Compared with IKEv1, IKEv2 simplifies the process of Security Association (SA) negotiation and provides better support for scenarios where an SSL-VPN connection is established with multiple subnets. We recommend that you select IKEv2. |
| Negot iat ion Mode | The negotiation mode of IKEv1. Main: This mode offers higher security. Aggressive: This mode is faster than the main mode. Negotiations are more likely to succeed in this mode. Connections negotiated in both modes ensure the same security level of data transmission. |
| Encrypt ion Algorit hm | Select the encryption algorithm used during phase 1 negotiation. Supported algorithms are aes, aes192, aes256, des, and 3des. |
| Aut hent icat ion Algorit hm | Select the authentication algorithm used during phase 1 negotiation. Supported algorithms are sha1, and md5. |
| DH Group | Select the Diffie-Hellman key exchange algorithm used during phase 1 negotiation. |
| SA Lif e Cycle (Seconds) | Specify the lifecycle of the SA after phase 1 negotiation succeeds. Default value: 86,400. |
| LocalId | The ID of the VPN gateway used during phase 1 negotiation. The default value is the public IP address of the VPN gateway. If you set LocalId to a FQDN, we recommend that you set Negotiation Mode to Aggressive. |

| ateway | User Guide·Configure IPsec-VPN co |
|---|---|

| Parameter | Description |
|---|---|
| Remot eId | The ID of the customer gateway used during phase 1 negotiation. The default value is the public IP address of the customer gateway. If you set RemoteId to a FQDN, we recommend that you select set Negotiation Mode to Aggressive. |
| Advanced conf igurat ion: IPSec conf igurat ion |   |
| Encrypt ion Algorit hm | Select the encryption algorithm used during phase 2 negotiation. Supported algorithms are aes, aes192, aes256, des, and 3des. |
| Aut hent icat ion Algorit hm | Select the authentication algorithm used during phase 2 negotiation. Supported algorithms are sha1, and md5. |
| DH Group | Select the Diffie-Hellman key exchange algorithm for phase 2 negotiations. If you select a Diffie-Hellman group, the perfect forward secrecy (PFS) feature is enabled and each negotiation requires a new key. Therefore, you must also enable PFS for the client. For clients that do not support PFS, select disabled. |
| SA Lif e Cycle (Seconds) | Specify the lifecycle of the SA after phase 2 negotiation succeeds. Default value: 86,400. |

#### 8.2.2 Modify an IPsec-VPN connection

This topic describes how to modify the name, advanced settings, and health check for an IPsec-VPN connection. Prerequisites An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection and then click Edit in the
Act ions column.
5. In the Modif y IPsec Connect ions dialog box, modify the name, advanced settings, and health
check, and click Submit .

#### 8.2.3 Download the configuration file of an IPsec-VPN connection

IPsec-VPN connection This topic describes how to download the configurations of an IPsec-VPN connection, and load the configurations to the customer gateway device after an IPsec-VPN connection is configured. nections An IPsec-VPN connection is created. For more information, see Create and manage IPsec-VPN connections. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
Download Conf igurat ion in the Act ions column. Not e RemoteSubnet and LocalSubnet in the downloaded configurations are opposite to RemoteSubnet and LocalSubnet that you specify when you create an IPsec-VPN connection. For a VPN gateway, RemotSubnet refers to the CIDR block of the on-premises data center and LocalSubnet refers to the CIDR block of the VPC network. For a customer gateway, LocalSubnet refers to the CIDR block of the on-premises data center and RemoteSubnet refers to the CIDR block of the VPC network.

#### 8.2.4 Configure a routing group

This topic describes how to configure routing groups to control the inbound and outbound traffic of ECS instances in a routing group after an IPsec-VPN connection is created. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
Conf igure Rout ing Group in the Act ions column.
5. In the Conf igure Rout ing Group dialog box, set the following parameters, and then click Submit .

| Parameter | Description |
|---|---|
| Rout ing Group | Select the routing group to which you want to add the routing group rule. |
| Rule Direct ion | Select the direction in which the rule is applied. Out bound: from the ECS instances in the current routing group to other ECS instances on Alibaba Cloud or resources on the Internet. Inbound: from other ECS instances on Alibaba Cloud or resources on the Internet to the ECS instances in the current routing group. |

nections

| Parameter | Description |
|---|---|
| Aut horizat ion Policy | Select an authorization policy. Allow: accept requests received on the specified ports. Deny: discard requests received on the specified ports without returning messages. If you specify different authorization policies for two routing group rules but the other settings are the same, the Deny rule prevails over the Allow rule. |
| Prot ocol T ype | Select a protocol type. |
| Port Range | Select a port range for the routing group rule. The port range depends on the protocol type: When you set Protocol to All, this parameter displays -1/-1, which indicates all ports. You cannot specify a port range if you select this protocol type. When you set Protocol to T CP, you can specify a port range in the <start port number>/<end port number> format. Valid port numbers: 1 to 65535. To specify a single port, set the start and end port numbers to the same value. For example, use 22/22 to indicate port 22. When Protocol is set to UDP, specify a port range in the <start port number>/<end port number> format. Valid port numbers: 1 to 65535. To specify a single port, set the start and end port numbers to the same value. For example, use 3389/3389 to indicate port 3389. When Protocol is set to ICMP, this parameter displays -1/-1, which indicates all ports. You cannot set a port range if you select this protocol type. When Protocol is set to GRE, this parameter displays -1/-1, which indicates all ports. You cannot set a port range if you select this protocol type. |
| Priorit y | Set the priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Aut horizat ion T ype | Select the authorization type of the routing group rule. You can select only Address. |
| NIC t ype | Select a NIC type. Int ernal: Control inbound and outbound traffic within Alibaba Cloud. Ext ernal: Control inbound and outbound traffic over the Internet. |
| Aut horized IP Addresses | Select the CIDR blocks to be authorized. You can specify up to 10 CIDR blocks at a time. |
| Aut omat ically Conf igure Rout ers | Specify whether to automatically configure routers. |

nections

| Parameter | Description |   |   |
|---|---|---|---|
| Descript ion | The description of the routing group rule. The description must be 2 to 256 characters in length, and cannot start with htt p:// or https:// . You can left this parameter empty. |   |   |
|   |   | htt |   |

|   | p:// |
|---|---|

#### 8.2.5 View IPsec-VPN connection logs

This topic describes how to view IPsec-VPN connection logs that are generated within the last 30 days to troubleshoot connection errors. You can query log data generated within 10 minutes. Procedure
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
View Logs in the Act ions column.
5. In the IPsec Connect ion Logs dialog box, set the time range and query the logs.

#### 8.2.6 Delete an IPsec-VPN connection

This topic describes how to delete an IPsec-VPN connection. Procedure
1. Log on to the VPN Gateway console.
2. 3.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then click Delet e in
the Act ions column.
5. In the message that appears, click OK.

### 8.3 MTU notes

The maximum transmission unit (MTU) is the size (in bytes) of the largest packet supported by the network layer protocol (such as TCP), with headers and data included. Network packets sent over IPsec tunnels are encrypted and then encapsulated in external packets for routing. Because an encapsulated internal packet itself must fit the MTU of the corresponding external packet, the MTU of the internal packet must be smaller. Gateway MTU and system MTU You must configure the MTU limit of the local VPN Gateway to not more than 1,400 bytes. We recommend that you set the MTU to 1,400 bytes. nections For TCP traffic, the maximum length of data that can be carried by each packet segment can be negotiated by the sender and receiver when they communicate based on the maximum segment size (MSS).
