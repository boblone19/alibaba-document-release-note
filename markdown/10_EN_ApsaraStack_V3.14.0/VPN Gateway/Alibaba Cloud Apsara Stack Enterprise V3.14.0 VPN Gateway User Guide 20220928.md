---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 VPN Gateway User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 46
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 VPN Gateway User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20VPN%20Gateway%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 VPN Gateway User Guide 20220928

## Table of Contents

- 1 What is VPN Gateway?
- 2 Log on to the VPN Gateway console
- 3 Get started with IPsec-VPN
  - 3.1 Connect a data center to a VPC
- 4 Get started with SSL-VPN
  - 4.1 Connect a Linux client to a VPC
  - 4.2 Connect a Windows client to a VPC
  - 4.3 Connect a macOS client to a VPC
- 5 Manage a VPN Gateway
  - 5.1 Create a VPN gateway
  - 5.2 Modify a VPN gateway
  - 5.3 Configure routes of a VPN Gateway
    - 5.3.1 Route overview
    - 5.3.2 Work with a policy-based route
    - 5.3.3 Manage destination-based routes
  - 5.4 Delete a VPN gateway
  - 5.5 View the monitoring information about a VPN gateway
- 6 Manage a customer gateway
  - 6.1 Create a customer gateway
  - 6.2 Modify a customer gateway
  - 6.3 Delete a customer gateway
- 7 Configure IPsec-VPN connections
  - 7.1 Configuration overview
  - 7.2 Manage an IPsec-VPN connection
    - 7.2.1 Create an IPsec-VPN connection
    - 7.2.2 Modify an IPsec-VPN connection
    - 7.2.3 Download the configuration file of an IPsec-VPN connection
    - 7.2.4 Configure a security group
    - 7.2.5 View IPsec-VPN connection logs
    - 7.2.6 Delete an IPsec-VPN connection
  - 7.3 View the monitoring information about an IPsec-VPN connection
  - 7.4 MTU considerations
- 8 Configure SSL-VPN
  - 8.1 SSL-VPN configuration overview
  - 8.2 Manage an SSL server
    - 8.2.1 Create an SSL server
    - 8.2.2 Modify an SSL server
    - 8.2.3 Configure a security group
    - 8.2.4 Delete an SSL server
  - 8.3 Manage an SSL client certificate
    - 8.3.1 Create an SSL client certificate
    - 8.3.2 Download an SSL client certificate
    - 8.3.3 Delete an SSL client certificate
  - 8.4 Query SSL-VPN connection logs

## 1 What is VPN Gateway?

VPN Gateway is an Internet-based service that allows you to connect enterprise data centers, office networks, or Internet-facing terminals to Alibaba Cloud Virtual Private Cloud (VPC) networks through secure and reliable connections. VPN Gateway supports both IPsec-VPN connections and SSL-VPN connections. The Alibaba Cloud VPN Gateway service complies with the local regulations and policies. VPN Gateway does not provide Internet access services. Features VPN Gateway supports the following features: IPsec-VPN Route-based IPsec-VPN allows you to route network traffic in multiple ways, and also facilitates the configuration and maintenance of VPN policies. You can use IPsec-VPN to connect an on-premises data center to a VPC network or connect two VPC networks. IPsec-VPN supports the IKEv1 and IKEv2 protocols. Any devices that support these two protocols can connect to Alibaba Cloud VPN Gateway, such as devices manufactured by Huawei, H3C, Hillstone, Sangfor, Cisco ASA, Juniper, SonicWall, Nokia, IBM, and Ixia. SSL-VPN SSL-VPN is implemented based on the OpenVPN framework. You can create an SSL-VPN connection to connect a remote client to applications and services deployed in a VPC network. After you deploy your applications or services, you only need to import the certificate to the client to initiate a connection. Benefits VPN Gateway offers the following benefits: High security: You can use the IKE and IPsec protocols to encrypt data for secure and reliable data transmission. High availability: VPN Gateway adopts the hot-standby architecture to achieve failover within a few seconds, session persistence, and zero service downtime. Cost-effectiveness: The encrypted Internet connections provided by VPN Gateway are more costeffective than leased lines. Ease of use: VPN Gateway is a ready-to-use service. VPN gateways start to work immediately after they are deployed. way console

## 2 Log on to the VPN Gateway console

console This topic describes how to log on to the Apsara Uni-manager Management Console. You can manage your VPN gateways in the console. The Google Chrome browser is used as an example. The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top menu bar, choose Product s > Net working > Virt ual Privat e Cloud.
5. In the left-side navigation pane, choose Int erconnect ions > VPN.
PN

## 3 Get started with IPsec-VPN

### 3.1 Connect a data center to a VPC

This topic describes how to connect a data center to a virtual private cloud (VPC) by using an IPsec-VPN connection. Before you start, make sure that the following requirements are met: The gateway device in the data center is checked. VPN Gateway supports the standard IKEv1 and IKEv2 protocols. Gateway devices that support these two protocols can connect to VPN gateways on Alibaba Cloud, such as gateway devices that are manufactured by H3C, 华为、Hillstone, Sangfor, Cisco ASA, Juniper, SonicWall, Nokia, IBM, or Ixia. A static public IP address is assigned to the gateway device in the data center. The CIDR block of the data center does not overlap with that of the VPC. Context An enterprise has created a VPC on Alibaba Cloud. The CIDR block of the VPC is 192.168.0.0/16. The CIDR block of the data center is 172.16.0.0/12. The static public IP address for the gateway device in the data center is 211.XX.XX.68. To meet business requirements, the enterprise needs to connect the data center to the VPC. As shown in the preceding figure, you can establish an IPsec-VPN connection between the data center and the VPC. Step 1: Create a VPN gateway Take the following steps to create a VPN gateway:
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where you want to deploy the VPN gateway. Make sure that the VPN gateway and the VPC are deployed in the same region. PN Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter, and cannot start with `http://` or

```
 https:// .
```

VPC: Select the VPC to be associated with the VPN gateway. vSwit ch: Select the vSwitch to which you want to attach the VPN gateway. Bandwidt h: Select a maximum bandwidth value for the VPN gateway. The bandwidth is used for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, Enable is selected. After IPsec-VPN is enabled, you can create a secure IPsec tunnel to connect a data center to a VPC, or connect two VPCs. SSL-VPN: Specify whether to enable SSL-VPN. In this example, Disable is selected. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without the need to configure a customer gateway. SSL Connect ions: Select the maximum number of concurrent SSL connections that the VPN gateway supports. This parameter is available only after SSL-VPN is enabled.
5. Go to the VPN Gateways page to view the newly created VPN gateway.
The newly created VPN gateway is in the Preparing state. The VPN gateway changes to the Normal state after about 2 minutes. The Normal state indicates that the VPN gateway is initialized and ready for use. It takes about 1 to 5 minutes to create a VPN gateway. Step 2: Create a customer gateway Perform the following operations to create a customer gateway.
1. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
2. Select the region where you want to create the customer gateway.
3. On the Cust omer Gat eways page, click Creat e Cust omer Gat eway.
4. On the Creat e Cust omer Gat eway page, set the following parameters, and click Submit .
Organizat ion: Select the organization to which the customer gateway belongs. Resource Set : Select the resource set to which the customer gateway belongs. Region: Select the region where you want to deploy the customer gateway. Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region. Zone: Select the zone where you want to deploy the customer gateway. Name: Enter a name for the customer gateway. PN The name must be 2 to 128 characters in length, and can contain digits, hyphens (-), and underscores (_). It must start with a letter and cannot start with `http://` or `https://` . IP Address: Enter the public IP address of the gateway device in the data center that you want to connect to the VPC. In this example, 211.XX.XX.68 is entered. Descript ion: Enter a description for the customer gateway. The description must be 2 to 256 characters in length, and can contain digits, hyphens (-), underscores (_), full width periods (。), full width commas (，), and full width colons (：). The description must start with a letter and cannot start with `http://` or `https://` . Step 3: Create an IPsec-VPN connection Perform the following operations to create an IPsec-VPN connection:
1. In the left-side navigation pane, choose VPN > IPsec Connect ions.
2. Select the region where you want to create an IPsec-VPN connection.
3. On the IPsec Connect ions page, click Creat e IPsec Connect ion.
4. On the Creat e IPsec Connect ion page, set the following parameters for the IPsec-VPN
connection, and click Submit . Organizat ion: Select the organization to which the IPsec-VPN connection belongs. Resource Set : Select the resource set to which the IPsec-VPN connection belongs. Region: Select the region to which the IPsec-VPN connection belongs. Zone: Select the zone to which the IPsec-VPN connection belongs. Name: Enter a name for the IPsec-VPN connection. VPN Gat eway: Select the VPN gateway you created. Cust omer Gat eway: Select the customer gateway to be connected through the IPsec-VPN connection. Source CIDR Block: Enter the CIDR block of the VPC with which the selected VPN gateway is associated. In this example, 192.168.0.0/16 is entered. Dest inat ion CIDR Block: Enter the CIDR block of the data center. In this example, 172.16.0.0/12 is entered. Immediat e Ef f ect : Specify whether to start connection negotiations immediately. Yes: immediately starts negotiations after you complete the configuration. No: starts negotiations when traffic is detected. Advanced Conf igurat ion: Use def ault advanced configurations. A pre-shared key is automatically generated by default. Step 4: Load the configurations of the IPsec-VPN connection to the on-premises gateway device Perform the following operations to load the configurations of the IPsec-VPN connection to the onpremises gateway device:
1. In the left-side navigation pane, choose VPN > IPsec Connect ions.
2. Select the region where the IPsec-VPN connection is created.
PN
3. On the IPsec Connect ions page, find the IPsec-VPN connection you want to manage, and then
choose More > Download Conf igurat ion in the Act ions column.
4. Load the configurations of the IPsec-VPN connection to the on-premises gateway device based on
the configuration requirements of the gateway device. For more information, consult the vendor of the gateway device. RemoteSubnet and LocalSubnet in the downloaded configurations are opposite to RemoteSubnet and LocalSubnet that you specify when you create an IPsec-VPN connection. For a VPN gateway, RemotSubnet refers to the CIDR block of the data center and LocalSubnet refers to the CIDR block of the VPC. For a customer gateway, LocalSubnet refers to the CIDR block of the data center and RemoteSubnet refers to the CIDR block of the VPC. Step 5: Configure routes for the VPN gateway Take the following steps to configure routes for the VPN gateway:
1. In the left-side navigation pane, choose VPN > VPN Gat eways.
2. Select the region where the VPN gateway is deployed.
3. On the VPN Gat eways page, find the VPN gateway for which you want to configure routes, and
click its ID in the Inst ance ID/Name column.
4. In the Dest inat ion-based rout ing tab, click Add Rout e Ent ry.
5. In the Add Rout e Ent ry dialog box, set the following parameters, and click OK.
Dest inat ion CIDR Block: Enter the CIDR block of the data center. In this example, 172.16.0.0/12 is entered. Next Hop T ype: Select IPsec Connect ion. Next Hop: Select an IPsec-VPN connection. Publish t o VPC: Specify whether to automatically advertise new route entries to the VPC route table. In this example, Yes is selected. Weight : Select a weight. In this example, 100 is selected. Step 6: Test the connectivity Log on to an Elastic Compute Service (ECS) instance that is not assigned a public IP address in the VPC. Run the ping command to ping the private IP address of a server in the data center to test the connectivity. N

## 4 Get started with SSL-VPN

### 4.1 Connect a Linux client to a VPC

This topic describes how to connect a Linux client to a virtual private cloud (VPC) through SSL-VPN connections. Before you start, make sure that the following requirements are met: A VPC is created. The CIDR block of the VPC must be different from that of the on-premises device. Your client can access the Internet. Step 1: Create a VPN gateway Perform the following operations to create a VPN gateway:
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where you want to deploy the VPN gateway. Make sure that the VPC and the VPN gateway for the VPC are deployed in the same region. Inst ance Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://` . N VPC: Select the VPC network to be associated with the VPN gateway. vSwit ch: Select the vSwitch to which you want to attach the VPN gateway. Bandwidt h: Specify the maximum bandwidth of the VPN gateway. The bandwidth is used for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, Disable is selected. SSL-VPN: Specify whether to enable SSL-VPN for the VPN gateway. In this example, Enable is selected. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a gateway for the client. SSL Connect ions: Specify the maximum number of concurrent SSL connections that the VPN gateway supports.
5. Return to the VPN Gat eways page to view the VPN gateway.
The newly created VPN gateway is in the Preparing state. The VPN gateway changes to the Normal state after about 2 minutes. The Normal state indicates that the VPN gateway is initialized and ready for use. It takes about 1 to 5 minutes to create a VPN gateway. Step 2: Create an SSL server Perform the following steps to create an SSL server:
1. In the left-side navigation pane, choose VPN > SSL Servers.
2. In the top navigation bar, select the region where you want to create the SSL server.
3. On the SSL Servers page, click Creat e SSL Server.
4. On the Creat e SSL Server page, set the following parameters for the SSL server, and then click
Submit . Organizat ion: Select the organization to which the SSL server belongs. Resource Set : Select the resource set to which the SSL server belongs. Region: Select the region where you want to deploy the SSL server. Zone: Select the zone where you want to deploy the SSL server. Name: Enter a name for the SSL server. VPN Gat eway: Select a VPN gateway from the drop-down list. Local Net work: Enter the CIDR block of the network to which you want to connect. Click to add more CIDR blocks. You can add the CIDR block of a VPC, a vSwitch, and an on-premises network. Client Subnet : Enter the client CIDR block that the client uses to connect to the SSL server. Advanced Conf igurat ion: Use def ault advanced configurations. Step 3: Create and download an SSL client certificate
1. In the left-side navigation pane, choose VPN > SSL Client s.
N
2. In the top navigation bar, select the region where the SSL client is deployed.
3. On the SSL Client s page, click Creat e Client Cert if icat e.
4. On the Creat e SSL Client Cert if icat e page, set the following parameters for the SSL client, and
then click Submit . Organizat ion: Select the organization to which the SSL client certificate belongs. Resource Set : Select the resource set to which the SSL client certificate belongs. Region: Select the region where you want to create the SSL client certificate. Zone: Select the zone where you want to create the SSL client certificate. Name: Enter a name for the SSL client certificate. VPN Gat eway: Select the VPN gateway to be associated with the SSL client certificate. SSL Server: Select the SSL server to be associated with the SSL client certificate.
5. On the SSL Client s page, find the SSL client certificate and click Download in the Act ions
column. The SSL client certificate is downloaded to your on-premises device. Step 4: Configure the client Perform the following steps to configure the Linux client:
1. Run the following command to install the OpenVPN client:

```bash
yum install -y openvpn
```

2. Extract the downloaded SSL client certificate and copy it to the /etc/openvpn/conf/ directory.
3. Run the following command to launch OpenVPN:

```
openvpn --config /etc/openvpn/conf/config.ovpn --daemon
```

Step 5: Test the connectivity Run the ping command to test the connectivity between the client and an Elastic Compute Service (ECS) instance in the VPC. Make sure that the security group rules of the ECS instance allow remote access from Linux clients.

### 4.2 Connect a Windows client to a VPC

VPC This topic describes how to connect a Windows client to a virtual private cloud (VPC) through SSL-VPN connections. Context N The following scenario is used as an example. Before you start, make sure that the following requirements are met: A VPC is created. The CIDR block of the VPC must be different from that of the on-premises device. Your client can access the Internet. Step 1: Create a VPN gateway Perform the following operations to create a VPN gateway:
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where you want to deploy the VPN gateway. Make sure that the VPC and the VPN gateway for the VPC are deployed in the same region. Inst ance Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://` . VPC: Select the VPC network to be associated with the VPN gateway. vSwit ch: Select the vSwitch to which you want to attach the VPN gateway. Bandwidt h: Specify the maximum bandwidth of the VPN gateway. The bandwidth is used for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, Disable is selected. SSL-VPN: Specify whether to enable SSL-VPN for the VPN gateway. In this example, Enable is selected. N SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a gateway for the client. SSL Connect ions: Specify the maximum number of concurrent SSL connections that the VPN gateway supports.
5. Return to the VPN Gat eways page to view the VPN gateway.
The newly created VPN gateway is in the Preparing state. The VPN gateway changes to the Normal state after about 2 minutes. The Normal state indicates that the VPN gateway is initialized and ready for use. It takes about 1 to 5 minutes to create a VPN gateway. Step 2: Create an SSL server Perform the following steps to create an SSL server:
1. In the left-side navigation pane, choose VPN > SSL Servers.
2. In the top navigation bar, select the region where you want to create the SSL server.
3. On the SSL Servers page, click Creat e SSL Server.
4. On the Creat e SSL Server page, set the following parameters for the SSL server, and then click
Submit . Organizat ion: Select the organization to which the SSL server belongs. Resource Set : Select the resource set to which the SSL server belongs. Region: Select the region where you want to deploy the SSL server. Zone: Select the zone where you want to deploy the SSL server. Name: Enter a name for the SSL server. VPN Gat eway: Select a VPN gateway from the drop-down list. Local Net work: Enter the CIDR block of the network to which you want to connect. Click to add more CIDR blocks. You can add the CIDR block of a VPC, a vSwitch, and an on-premises network. Client Subnet : Enter the client CIDR block that the client uses to connect to the SSL server. Advanced Conf igurat ion: Use def ault advanced configurations. Step 3: Create and download an SSL client certificate
1. In the left-side navigation pane, choose VPN > SSL Client s.
2. In the top navigation bar, select the region where the SSL client is deployed.
3. On the SSL Client s page, click Creat e Client Cert if icat e.
4. On the Creat e SSL Client Cert if icat e page, set the following parameters for the SSL client, and
then click Submit . Organizat ion: Select the organization to which the SSL client certificate belongs. Resource Set : Select the resource set to which the SSL client certificate belongs. Region: Select the region where you want to create the SSL client certificate. Zone: Select the zone where you want to create the SSL client certificate. N Name: Enter a name for the SSL client certificate. VPN Gat eway: Select the VPN gateway to be associated with the SSL client certificate. SSL Server: Select the SSL server to be associated with the SSL client certificate.
5. On the SSL Client s page, find the SSL client certificate and click Download in the Act ions
column. The SSL client certificate is downloaded to your on-premises device. Step 4: Configure the client Perform the following steps to configure the Windows client: Not ice You must run the client as an administrator.
1. Download and install the OpenVPN client.
Download OpenVPN.
2. Extract the downloaded SSL client certificate and copy it to the OpenVPN\config directory.
In this example, the certificate is copied to the C:\Program Files\OpenVPN\config directory. You must copy the certificate to the directory where the OpenVPN client is installed.
3. Start the OpenVPN client and click Connect to initiate a connection.
Step 5: Test the connectivity Run the ping command to test the connectivity between the client and an Elastic Compute Service (ECS) instance in the VPC. Make sure that the security group rules of the ECS instance allow remote access from Windows clients. N

### 4.3 Connect a macOS client to a VPC

This topic describes how to connect a macOS client to a virtual private cloud (VPC) through SSL-VPN connections. Before you start, make sure that the following requirements are met: A VPC is created. The CIDR block of the VPC must be different from that of the on-premises device. Your client can access the Internet. Step 1: Create a VPN gateway Perform the following operations to create a VPN gateway:
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit . Organizat ion: Select the organization to which the VPN gateway belongs. Resource Set : Select the resource set to which the VPN gateway belongs. Region: Select the region where you want to deploy the VPN gateway. Make sure that the VPC and the VPN gateway for the VPC are deployed in the same region. Inst ance Name: Enter a name for the VPN gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://` . VPC: Select the VPC network to be associated with the VPN gateway. vSwit ch: Select the vSwitch to which you want to attach the VPN gateway. Bandwidt h: Specify the maximum bandwidth of the VPN gateway. The bandwidth is used for data transfer over the Internet. IPsec-VPN: Specify whether to enable IPsec-VPN for the VPN gateway. In this example, Disable is selected. N SSL-VPN: Specify whether to enable SSL-VPN for the VPN gateway. In this example, Enable is selected. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without configuring a gateway for the client. SSL Connect ions: Specify the maximum number of concurrent SSL connections that the VPN gateway supports.
5. Return to the VPN Gat eways page to view the VPN gateway.
The newly created VPN gateway is in the Preparing state. The VPN gateway changes to the Normal state after about 2 minutes. The Normal state indicates that the VPN gateway is initialized and ready for use. It takes about 1 to 5 minutes to create a VPN gateway. Step 2: Create an SSL server Perform the following steps to create an SSL server:
1. In the left-side navigation pane, choose VPN > SSL Servers.
2. In the top navigation bar, select the region where you want to create the SSL server.
3. On the SSL Servers page, click Creat e SSL Server.
4. On the Creat e SSL Server page, set the following parameters for the SSL server, and then click
Submit . Organizat ion: Select the organization to which the SSL server belongs. Resource Set : Select the resource set to which the SSL server belongs. Region: Select the region where you want to deploy the SSL server. Zone: Select the zone where you want to deploy the SSL server. Name: Enter a name for the SSL server. VPN Gat eway: Select a VPN gateway from the drop-down list. Local Net work: Enter the CIDR block of the network to which you want to connect. Click to add more CIDR blocks. You can add the CIDR block of a VPC, a vSwitch, and an on-premises network. Client Subnet : Enter the client CIDR block that the client uses to connect to the SSL server. Advanced Conf igurat ion: Use def ault advanced configurations. Step 3: Create and download an SSL client certificate
1. In the left-side navigation pane, choose VPN > SSL Client s.
2. In the top navigation bar, select the region where the SSL client is deployed.
3. On the SSL Client s page, click Creat e Client Cert if icat e.
4. On the Creat e SSL Client Cert if icat e page, set the following parameters for the SSL client, and
then click Submit . Organizat ion: Select the organization to which the SSL client certificate belongs. Resource Set : Select the resource set to which the SSL client certificate belongs. N Region: Select the region where you want to create the SSL client certificate. Zone: Select the zone where you want to create the SSL client certificate. Name: Enter a name for the SSL client certificate. VPN Gat eway: Select the VPN gateway to be associated with the SSL client certificate. SSL Server: Select the SSL server to be associated with the SSL client certificate.
5. On the SSL Client s page, find the SSL client certificate and click Download in the Act ions
column. The SSL client certificate is downloaded to your on-premises device. Step 4: Configure the client Perform the following steps to configure the macOS client:
1. Run the following command to install the OpenVPN client:

```
brew install openvpn
```

Make sure that homebrew is installed before you install OpenVPN.
2. Extract the certificate that you downloaded in Step 3 and copy it to the directory where the
OpenVPN client is installed. Then, initiate an SSL-VPN connection. i. Back up the default configuration file. ii. Run the following command to delete the default configuration file:

```
rm /usr/local/etc/openvpn/*
```

iii. Run the following command to copy the file to the configuration directory:

```
cp cert_location /usr/local/etc/openvpn/
```

In the preceding command, replace `cert_location` with the directory where the certificate is downloaded in Step 3. For example: /Users/example/Downloads/certs6.zip. iv. Run the following command to decompress the SSL client certificate package:

```
cd /usr/local/etc/openvpn/ unzip /usr/local/etc/openvpn/certs6.zip
```

v. Run the following command to initiate a connection:

```python
sudo /usr/local/opt/openvpn/sbin/openvpn --config /usr/local/etc/openvpn/config.ovp
```

`n` Step 5: Test the connectivity Run the ping command to test the connectivity between the client and an Elastic Compute Service (ECS) instance in the VPC. Make sure that the security group rules of the ECS instance allow remote access from macOS clients.

## 5 Manage a VPN Gateway

### 5.1 Create a VPN gateway

This topic describes how to create a VPN gateway. You must create a VPN gateway before you can use the IPsec-VPN and SSL-VPN features. After you create a VPN gateway, a public IP address is assigned to the VPN gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. On the VPN Gat eways page, click Creat e VPN Gat eway.
4. On the Creat e VPN Gat eway page, set the following parameters for the VPN gateway, and then
click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VPN gateway belongs. |
| Resource Set | Select the resource set to which the VPN gateway belongs. |
| Region | Select the region where you want to create the VPN gateway. You can create IPsec-VPN connections on VPN gateways to connect a data center to a VPC or connect two VPCs. Make sure that the VPC and the VPN gateway associated with the VPC are deployed in the same region. |
| Inst ance Name | Enter a name for the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a letter, _ and cannot start with http:// or https:// . |
| VPC | Select the VPC network to be associated with the VPN gateway. |
| vSwit ch | Select the vSwitch to which you want to attach the VPN gateway. |
| Bandwidt h | Select a maximum bandwidth value for the VPN gateway. The bandwidth is used for data transfer over the Internet. |
| IPsec-VPN | Specify whether to enable IPsec-VPN for the VPN gateway. The default value is Enable IPsec. After IPsec-VPN is enabled, you can create a secure IPsec tunnel to connect a data center to a VPC, or connect two VPCs. |

| Parameter | Description |
|---|---|
| SSL-VPN | Specify whether to enable SSL-VPN for the VPN gateway. The default value is Disable. SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Alibaba Cloud without the need to configure a customer gateway. |
| SSL Connect ions | Select the maximum number of concurrent SSL connections that the VPN gateway supports. Not e You can set this parameter only after SSL-VPN is enabled. |

### 5.2 Modify a VPN gateway

This topic describes how to modify the name and description of a VPN gateway. A VPN gateway is created. For more information, see Create and manage a VPN gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. Select the region where the VPN gateway is deployed.
4. On the VPN Gat eways page, find the target VPN gateway, and click the
icon in the Inst ance ID/Name column. In the dialog box that appears, enter a new name and click OK. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.
5. Click the
icon in the Descript ion column. In the dialog box that appears, enter a new description and click OK. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.

### 5.3 Configure routes of a VPN Gateway

Gateway

#### 5.3.1 Route overview

After you create an IPsec-VPN connection by using a VPN gateway, you must add a route to the VPN gateway. Route-based IPsec-VPN allows you to route network traffic in multiple ways, and facilitates the configuration and maintenance of VPN policies. You can add the following two types of route to a VPN gateway: Policy-based routes. Destination-based routes. Policy-based routes Policy-based routes forward traffic based on source and destination IP addresses. For more information, see Add a policy-based route entry. Policy-based routes take precedence over destination-based routes. Destination-based routes Destination-based routes forward traffic to specified destination IP addresses. For more information, see Create a destination-based route.

#### 5.3.2 Work with a policy-based route

A policy-based route forwards traffic based on source and destination IP addresses. This topic describes how to create, advertise, modify, and delete a policy-based route. An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection. Add a policy-based route After you create an IPsec-VPN connection, you can create a policy-based route for the IPsec-VPN connection.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway you want to manage and click the gateway ID
in the Inst ance ID/Name column.
5. Click the Policy-based Rout ing tab, and then click Add Rout e Ent ry.
6. In the Add Rout e Ent ry panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Dest inat ion CIDR block | The private CIDR block that you want to access. |
| Source CIDR Block | The private CIDR block of the VPC. |
| Next Hop T ype | Select IPsec Connection. |

| Guide·Manage a VPN Gate | way VPN Gatewa |
|---|---|

| Parameter | Description |
|---|---|
| Next Hop | Select the IPsec-VPN connection for which you want to create the policy- based route. |
| Publish t o VPC | Specify whether to advertise the route to the VPC route table. Valid values: Yes: automatically advertises the route to the route table of the VPC. We recommend that you select this value. No: does not advertise the route to the VPC route table. Not e If you select No, you must manually advertise the route to the VPC route table. |
| Weight | Select a weight. Valid values: 100: specifies a high priority for the policy-based route. 0: specifies a low priority for the policy-based route. Not e If two policy-based routes are configured with the same destination CIDR block, you cannot set the weights of the routes to 100. |

Advertise a policy-based route
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway you want to manage and click the gateway ID
in the Inst ance ID/Name column.
5. On the Policy-based Rout ing tab, find the policy-based route that you want to advertise and
click Publish in the Act ions column.
6. In the Publish Rout e Ent ry message, click OK.
If you want to withdraw the policy-based route, click Unpublish. Modify a policy-based route You can change the weight of a policy-based route.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway you want to manage and click the gateway ID
in the Inst ance ID/Name column.
5. On the Policy-based Rout ing tab, find the policy-based route that you want to modify and click
Edit in the Act ions column.
6. In the panel that appears, specify a new weight for the route and click OK.
Delete a policy-based route
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways .
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway you want to manage and click the gateway ID
in the Inst ance ID/Name column.
5. On the Policy-based Rout ing tab, find the policy-based route that you want to delete and click
Delet e in the Act ions column.
6. In the Delet e Rout e Ent ry message, click OK.

#### 5.3.3 Manage destination-based routes

Destination-based routing is a technique that routes network traffic to specified destination IP addresses. This topic describes how to create, advertise, modify, and delete a destination-based route. An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection. Create a destination-based route After you create an IPsec-VPN connection, you can create a destination-based route for the IPsec-VPN connection.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway and click its ID.
5. On the Dest inat ion-based rout ing tab, click Add Rout e Ent ry.
6. In the Add Rout e Ent ry dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Dest inat ion CIDR block | Enter the CIDR block that you want to access. |
| Next Hop T ype | Select IPsec Connection. |
| Next Hop | Select the IPsec-VPN connection for which you want to create a destination- based route. |

| Parameter | Description |
|---|---|
| Publish t o VPC | Specify whether to advertise the destination-based route to the virtual private cloud (VPC) route table. Yes: automatically advertises the route to the route table of the VPC. We recommend that you select this value. No: does not advertise the destination-based route to the VPC route table. Not e If you select No, you must manually advertise the destination-based route to the VPC route table. |
| Weight | Select a weight. Valid values: 100: specifies a high priority for the destination-based route. 0: specifies a low priority for the destination-based route. Not e If two destination-based routes are configured with the same destination CIDR block, you cannot set the weights of the routes to 100. |

Advertise the destination-based route
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway and click its ID.
5. On the Dest inat ion-based Rout ing tab, find the destination-based route that you want to
manage and click Publish in the Act ions column.
6. In the Publish Rout e Ent ry message, click OK.
If you want to withdraw the destination-based route, click Unpublish. Modify the destination-based route You can change the weight of the destination-based route.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway and click its ID.
5. On the Dest inat ion-based Rout ing tab, find the destination-based route that you want to
manage and click Edit in the Act ions column.
6. In the panel that appears, specify the weight of the destination-based route and click OK.
Delete the destination-based route
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. In the top navigation bar, select the region of the VPN gateway.
4. On the VPN Gat eways page, find the VPN gateway and click its ID.
5. On the Dest inat ion-based Rout ing tab, find the destination-based route that you want to
manage and click Delet e in the Act ions column.
6. In the Delet e Rout e Ent ry message, click OK.

### 5.4 Delete a VPN gateway

This topic describes how to delete a VPN gateway. After you delete a VPN gateway, you can no longer use the VPN gateway to establish IPsec-VPN or SSL-VPN connections. Context Before you delete a VPN gateway, make sure that the following conditions are met: The IPsec-VPN connections on the VPN gateway are deleted. For more information, see Delete an IPsec-VPN connection. The SSL server associated with the VPN gateway is deleted. For more information, see Delete an SSL server.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > VPN Gat eways.
3. Select the region where the VPN gateway is deployed.
4. On the VPN Gat eways page, find the VPN gateway that you want to delete, and then click
Delet e in the Act ions column.
5. In the Delet e VPN Gat eway message, click OK.

### 5.5 View the monitoring information about a VPN gateway

about a VPN gateway This topic describes how to view the monitoring information about a VPN gateway. Before you start, make sure that the following requirements are met: Log Service is activated. CloudMonitor is activated.
1. Log on to the VPN Gateway console.
2. In the top navigation bar, select the region of the VPN gateway.
3. On the VPN Gat eway page, find the VPN gateway you want to manage and click the gateway ID.
4. On the details page of the VPN gateway, click the Monit or tab.
5. On the Monit or tab, view the monitoring information.
By default, the system displays the monitoring information within the last hour. You can also view the monitoring information within the last 3, 6, or 12 hours. In addition, you can view the monitoring information in a specified time period. VPN Gateway provides the following monitoring information:

| Metric | Description |
|---|---|
| Vpn rxPkgs | The rate at which packets are received by the VPN gateway. Unit: packet/s. This is the default unit. You can also select kilopacket/s or megapacket/s from the drop- down list next to the monitored item. |
| Vpn t xPkgs | The rate at which packets are sent by the VPN gateway. Unit: packet/s. This is the default unit. You can also select kilopacket/s or megapacket/s from the drop- down list next to the monitored item. |
| Vpn net rat e | The rate of inbound traffic. Unit: bit/s. This is the default unit. You can also select Kbit/s, Mbit/s, or Gbit/s from the drop-down list next to the monitored item. |
| Vpn net rat e | The rate of outbound traffic. Unit: bit/s. This is the default unit. You can also select Kbit/s, Mbit/s, or Gbit/s from the drop-down list next to the monitored item. |
| ssl connect count (count ) | The number of clients that are connected to Alibaba Cloud by using the SSL-VPN connection. |

eway

## 6 Manage a customer gateway

### 6.1 Create a customer gateway

This topic describes how to create a customer gateway. You can use a customer gateway to establish an IPsec-VPN connection between a virtual private cloud (VPC) and a data center or between two VPCs. After you create a customer gateway, you can update the information about a gateway device in the data center to Alibaba Cloud. Then, you can connect the customer gateway to a VPN gateway. A customer gateway can connect to multiple VPN gateways.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
3. Select the region where you want to deploy the customer gateway.
Make sure that the customer gateway and the VPN gateway to be connected belong to the same region.
4. On the Cust omer Gat eways page, click Creat e Cust omer Gat eway.
5. On the Creat e Cust omer Gat eway page, set the following parameters and click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Organizat ion | Select the organization to which the customer gateway belongs. |   |   |
| Resource Set | Select the resource set to which the customer gateway belongs. |   |   |
| Region | Select the region where you want to deploy the customer gateway. Not e Make sure that the customer gateway and the VPN gateway to be connected belong to the same region. |   |   |
| Zone | Select the zone where you want to deploy the customer gateway. |   |   |
| Name | Enter a name for the customer gateway. The name must be 2 to 128 characters in length and can contain digits, hyphens (-), and underscores ( ). The name must start with a letter and _ cannot start with http:// or https:// . |   |   |
| IP Address | Enter the static public IP address of the gateway device in the data center. |   |   |
| Descript ion | Enter a description for the customer gateway. The description must be 2 to 256 characters in length and can contain digits, hyphens (-), underscores ( ), periods (.), commas (,), and colons (:). The _ description must start with a letter and cannot start with http:// or h ttps:// . |   |   |
|   |   | h |   |

|   | ttps:// |
|---|---|

eway

### 6.2 Modify a customer gateway

This topic describes how to modify the name and description of a customer gateway. A customer gateway is created. For more information, see Create a customer gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
3. Select the region where the customer gateway is deployed.
4. On the Cust omer Gat eways page, find the target customer gateway, click the
icon in the Inst ance ID column. In the dialog box that appears, enter a name and click OK. The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.
5. Click the
icon in the Descript ion column. In the dialog box that appears, enter a new description and click OK. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.

### 6.3 Delete a customer gateway

This topic describes how to delete a customer gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > Cust omer Gat eways.
3. In the top navigation bar, select the region of the customer gateway.
4. On the Cust omer Gat eways page, find the customer gateway that you want to delete, and then
click Delet e in the Act ions column.
5. In the Delet e Cust omer Gat eway message, click OK.
nections

## 7 Configure IPsec-VPN connections

connections

### 7.1 Configuration overview

This topic describes how to connect a VPC to an on-premises data center through IPsec-VPN. Before creating a site-to-site VPN connection, make sure the following conditions are met: The protocols IKEv1 and IKEv2 are supported by the gateway device of the on-premises data center. IPsec-VPN supports IKEv1 and IKEv2 protocols. Devices that support these two protocols can connect to Alibaba Cloud VPN Gateway, including devices of Huawei, H3C, Hillstone, SANGFOR, Cisco ASA, Juniper, SonicWall, Nokia, IBM, and Ixia. A static public IP address is configured for the local gateway. The IP address ranges of the VPC and on-premises data center to be connected do not conflict with each other. The following figure shows the procedure of connecting a VPC to an on-premises data center through IPsec-VPN. Enable the IPsec-VPN function. Up to 10 IPsec-VPN connections can be established in a VPN Gateway. By creating a customer gateway, you can register the local gateway to Alibaba Cloud and connect the customer gateway to the VPN Gateway. A customer gateway can be connected to multiple VPN Gateways.
3. Create an IPsec connection
An IPsec connection is a VPN channel established between a VPN Gateway and a customer gateway. The encrypted communication between the VPN Gateway and the on-premises data center can be achieved only after the IPsec connection is established.
4. Configure the local gateway
You need to load the VPN Gateway configurations to the local gateway device. nections
5. Configure the VPN Gateway route
You need to configure a route in the VPN Gateway and publish it to the VPC route table.
6. Test the connection
Log on to an ECS instance (without a public IP address) in the connected VPC. ping the private IP address of a server in the on-premises data center to check whether the connection is established.

### 7.2 Manage an IPsec-VPN connection

#### 7.2.1 Create an IPsec-VPN connection

This topic describes how to create an IPsec-VPN connection. After you create a VPN gateway and a customer gateway, you can create an IPsec-VPN connection between the two gateways for encrypted data transmission.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where you want to create the IPsec-VPN connection.
4. On the IPsec Connect ions page, click Creat e IPsec Connect ion.
5. On the Creat e IPsec Connect ion page, configure the IPsec-VPN connection based on the
following information and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the IPsec-VPN connection belongs. |
| Resource Set | Select the resource set to which the IPsec-VPN connection belongs. |
| Region: | Select the region where the IPsec-VPN connection is created. |
| Zone | Select the zone where the IPsec-VPN connection is created. |
| Name | Enter a for the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain digits, hyphens (-), and underscores ( ). It must start with a letter and cannot start _ with http:// or https:// . |
| VPN Gat eway | Select the VPN gateway to be connected through the IPsec-VPN connection. |
| Cust omer Gat eway | Select the customer gateway to be connected through the IPsec-VPN connection. |
| Local Net work | Enter the CIDR block of the VPC to be connected to the data center. The CIDR block is used in Phase 2 negotiations. You can add multiple CIDR blocks of the VPC only if IKEv2 is used. |

nections

| Parameter | Description |
|---|---|
| Remot e Net work | Enter the CIDR block of the data center to be connected to the VPC. This CIDR block is used in Phase 2 negotiations. You can add multiple CIDR blocks of the data center only if IKEv2 is used. |
| Ef f ect ive Immediat ely | Specify whether to start connection negotiations immediately. Yes: immediately starts negotiations after you complete the configuration. No: starts negotiations when traffic is detected. |
| Advanced Conf igurat ions | Select the type of advanced configurations. Def ault : Use default settings. Conf igure: Use custom settings. |
| Advanced conf igurat ion: IKE conf igurat ion |   |
| Pre-Shared Key | Enter the pre-shared key used for authentication between the VPN gateway and the customer gateway. You can specify a key, or use the default key that is randomly generated by the system. |
| Version | Select an IKE version. ikev1 ikev2 IKEv1 and IKEv2 are supported. Compared with IKEv1, IKEv2 simplifies the Security Association (SA) negotiation process and provides better support for scenarios where multiple CIDR blocks are used. We recommend that you select IKEv2. |
| Negot iat ion Mode | Select the negotiation mode of IKEv1. main: This mode offers higher security during negotiations. aggressive: This mode is faster and has a higher success rate. Connections negotiated in both modes ensure the same security level of data transmission. |
| Encrypt ion Algorit hm | Select the encryption algorithm to be used in Phase 1 negotiations. Supported algorithms are aes, aes192, aes256, des, and 3des. |
| Aut hent icat ion Algorit hm | Select the authentication algorithm to be used in Phase 1 negotiations. Supported algorithms are sha1 and md5. |
| DH Group | Select the Diffie-Hellman key exchange algorithm to be used in Phase 1 negotiations. |
| SA Lif e Cycle (seconds) | Specify the lifecycle of the SA after Phase 1 negotiations succeed. Default value: 86400. Unit: seconds. |

| Guide·Configure IPsec-VPN | con |
|---|---|

nections

| Parameter | Description |
|---|---|
| LocalId | Specify the ID of the VPN gateway. The ID is used in Phase 1 negotiations. The default value is the public IP address of the VPN gateway. If you set LocalId to a FQDN, we recommend that you set Negotiation Mode to Aggressive. |
| Remot eId | Specify the ID of the customer gateway. The ID is used in Phase 1 negotiations. The default value is the public IP address of the customer gateway. If you set RemoteId to a FQDN, we recommend that you select set Negotiation Mode to Aggressive. |
| Advanced conf igurat ion: IPSec conf igurat ion |   |
| Encrypt ion Algorit hm | Select the encryption algorithm to be used in Phase 2 negotiations. Supported algorithms are aes, aes192, aes256, des, and 3des. |
| Aut hent icat ion Algorit hm | Select the authentication algorithm to be used in Phase 2 negotiations. Supported algorithms are sha1 and md5. |
| DH Group | Select the Diffie-Hellman key exchange algorithm to be used in Phase 2 negotiations. If you select a value other than disabled, the PFS feature is enabled by default, which necessitates key update for every renegotiation. Therefore, you must also enable PFS for the client. For clients that do not support PFS, select disabled. |
| SA Lif e Cycle (seconds) | Specify the lifecycle of the SA after Phase 2 negotiations succeed. Default value: 86400. Unit: seconds. |

#### 7.2.2 Modify an IPsec-VPN connection

This topic describes how to modify the name, advanced settings, and health check for an IPsec-VPN connection. An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection and then click Edit in the
Act ions column.
5. In the Modif y IPsec Connect ions dialog box, modify the name, advanced settings, and health
check, and click Submit . nections

#### 7.2.3 Download the configuration file of an IPsec-VPN connection

IPsec-VPN connection This topic describes how to download the configurations of an IPsec-VPN connection, and load the configurations to the customer gateway device after an IPsec-VPN connection is configured. An IPsec-VPN connection is created. For more information, see Create and manage IPsec-VPN connections.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
Download Conf igurat ion in the Act ions column. RemoteSubnet and LocalSubnet in the downloaded configurations are opposite to RemoteSubnet and LocalSubnet that you specify when you create an IPsec-VPN connection. For a VPN gateway, RemotSubnet refers to the CIDR block of the on-premises data center and LocalSubnet refers to the CIDR block of the VPC network. For a customer gateway, LocalSubnet refers to the CIDR block of the on-premises data center and RemoteSubnet refers to the CIDR block of the VPC network.

#### 7.2.4 Configure a security group

This topic describes how to configure a security group to control the inbound and outbound traffic of ECS instances in the security group after an IPsec-VPN connection is created.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the IPsec-VPN connection you want to manage, and then
choose More > Conf igure Rout ing Group in the Act ions column.
5. In the Conf igure Rout ing Group panel, set the following parameters, and then click Submit .

| Parameter | Description |
|---|---|
| Securit y Group | Select the security group to which you want to add the security group rule. |

nections

| Parameter | Description |   |   |
|---|---|---|---|
| Rule Direct ion | Select the direction in which the rule applies. Out bound: from the ECS instances in the current security group to other ECS instances on Alibaba Cloud or resources on the Internet. Inbound: from other ECS instances on Alibaba Cloud or resources on the Internet to the ECS instances in the current security group. |   |   |
| Policy | Select an authorization policy. Allow: allows access requests on the specified ports. Deny: discards requests on the specified ports without returning messages. If you specify different authorization policies for two security group rules but the other settings are the same, the Deny rule prevails over the Allow rule. |   |   |
| Prot ocol T ype | Select a protocol type. |   |   |
| Port Range | Select a port range for the security group rule. Specify the port range in the format of 1/200 or 80/80. 1/200 specifies a port range from 1 to 200. 80/80 specifies port 80. Valid values: -1 and 1 to 65535. A value of -1/-1 specifies all ports. |   |   |
| Priorit y | Set a priority for the rule. Valid values: 1 to 100. The default value is 1, which specifies the highest priority. |   |   |
| Aut horizat ion T ype | Select the authorization type of the security group rule. You can select only Address. |   |   |
| Net work T ype | Select a network interface controller (NIC) type. Int ernal: controls inbound and outbound traffic within Alibaba Cloud. Ext ernal: controls inbound and outbound traffic over the Internet. |   |   |
| Aut horizat ion Object | Select the CIDR blocks to be authorized by the security group rule. You can specify up to 10 CIDR blocks at a time. |   |   |
| Enable Aut omat ically Conf igure Rout ers | Specify whether to automatically configure routers. The feature is enabled by default. |   |   |
| Descript ion | Enter a description for the security group rule. The description must be 2 to 256 characters in length, and cannot start with htt p:// or https:// . You can leave this parameter empty. |   |   |
|   |   | htt |   |

|   | p:// |
|---|---|

nections

#### 7.2.5 View IPsec-VPN connection logs

This topic describes how to view IPsec-VPN connection logs that are generated within the last 30 days to troubleshoot connection errors. You can query log data generated within 10 minutes.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where the IPsec-VPN connection is created.
4. On the IPsec Connect ions page, find the target IPsec-VPN connection, and then choose More >
View Logs in the Act ions column.
5. In the IPsec Connect ion Logs dialog box, set the time range and query the logs.

#### 7.2.6 Delete an IPsec-VPN connection

This topic describes how to delete an IPsec-VPN connection.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where you want to delete the IPsec-VPN connection.
4. On the IPsec Connect ions page, find the IPsec-VPN connection that you want to delete, and click
Delet e in the Act ions column.
5. In the message that appears, click OK.

### 7.3 View the monitoring information about an IPsec-VPN connection

about an IPsec-VPN connection This topic describes how to view the monitoring information about an IPsec-VPN connection. Before you start, make sure that the following requirements are met: Log Service is activated. CloudMonitor is activated.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > IPsec Connect ions.
3. In the top navigation bar, select the region where you want to delete the IPsec-VPN connection.
4. On the IPsec Connect ions page, find the IPsec-VPN connection that you want to manage and
click its ID.
5. On the Monit or tab of the IPsec-VPN connection, view the monitoring information about the
nections connection. By default, the system displays monitoring information within the last hour. You can also view monitoring information within the last 3, 6, or 12 hours. In addition, you can view monitoring information within a specified time period. VPN Gateway provides the following monitoring information:

| Metric | Description |
|---|---|
| Ipsec receive pkg Count er | The rate at which packets are received by the IPsec-VPN connection. Unit: packet/s. This is the default unit. You can also select kilopacket/s or megapacket/s from the drop- down list next to the monitored item. |
| Ipsec t ransf orm pkg Count er | The rate at which packets are sent by the IPsec-VPN connection. Unit: packet/s. This is the default unit. You can also select kilopacket/s or megapacket/s from the drop- down list next to the monitored item. |
| Ipsec receive rat e | The rate of inbound traffic. Unit: bit/s. This is the default unit. You can also select Kbit/s, Mbit/s, or Gbit/s from the drop-down list next to the monitored item. |
| Ipsec t ransf orm rat e | The rate of outbound traffic. Unit: bit/s. This is the default unit. You can also select Kbit/s, Mbit/s, or Gbit/s from the drop-down list next to the monitored item. |

### 7.4 MTU considerations

The maximum transmission unit (MTU) is the size of the largest packet that can be transmitted over a network layer protocol, such as TCP. Packets are measured in bytes. The MTU takes both the sizes of headers and data into account. Segments transmitted over an IPsec tunnel are encrypted and then encapsulated into packets for routing purpose. The size of a segment must fit the MTU of the packet that carries the segment. Therefore, the MTU of the segment must be smaller than the MTU of the packet. Gateway MTU You must set the MTU of the local VPN gateway to a value no greater than 1,360 bytes. We recommend that you set the MTU to 1,360 bytes. The TCP protocol negotiates the maximum segment length (MSS) of each packet segment between the sender and the receiver. We recommend that you set the TCP MSS of the on-premises VPN gateway to 1,359 bytes to facilitate the encapsulation and transfer of TCP packets.

## 8 Configure SSL-VPN

### 8.1 SSL-VPN configuration overview

This topic describes how to remotely access a VPC through SSL-VPN. The following conditions must be met before you deploy a VPN Gateway: The client and the VPC are not using the same private CIDR block. The client is able to access the Internet. The following figure describes the process for configuring remote access to a VPC through SSL-VPN. Create a VPN gateway and enable the SSL-VPN function. Specify the range of IP addresses to be accessed and the range of IP addresses to be allocated to the client for making connections.
3. Create a client certificate
Create a client certificate according to the SSL server configuration, and then download the client certificate and the configuration file.
4. Configure the client
Download and install the VPN client, and then import the client certificate and the configuration file.
5. Configure the security group
Make sure that the rules in the security group of the ECS instance allow remote access from clients.

### 8.2 Manage an SSL server

#### 8.2.1 Create an SSL server

This topic describes how to create an SSL server. Before you can create an SSL-VPN connection, you must create an SSL server. A VPN gateway is created and SSL-VPN is enabled for the VPN gateway. For more information, see Create and manage a VPN gateway.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. In the top navigation bar, select the region where you want to create the SSL server.
4. On the SSL Servers page, click Creat e SSL Server.
5. On the Creat e SSL Server page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the SSL server belongs. |
| Resource Set | Select the resource set to which the SSL server belongs. |
| Region | Select the region where you want to deploy the SSL server. |
| Zone | Select the zone where you want to deploy the SSL server. |
| Name | Enter a name for the SSL server. The name must be 2 to 128 characters in length, and can contain digits, hyphens (-), and underscores ( ). It must start with a letter and cannot start _ with http:// or https:// . |
| VPN Gat eway | Select the VPN gateway that you want to associate with the SSL server. Make sure that SSL-VPN is enabled for the VPN gateway. |
| Local Net work | Enter the CIDR block that the client needs to access through the SSL-VPN connection. It can be the CIDR block of a VPC, a vSwitch, a data center connected to a VPC through an Express Connect circuit, or a cloud service such as ApsaraDB RDS or Object Storage Service (OSS). Click + to add more CIDR blocks. Not e The subnet mask of the specified CIDR block must be 16 to 29 bits in length. |
| Client CIDR Block | Enter the CIDR block from which an IP address is allocated to the virtual NIC of the client. Do not enter the private CIDR block of the client. When the client accesses the destination network through an SSL-VPN connection, the VPN gateway allocates an IP address from the client CIDR block to the client. |

| Parameter | Description |
|---|---|
| Advanced Conf igurat ions | Select the type of advanced configurations. Def ault : Use the default advanced configurations. Cust om: Use custom configurations. You can set the following parameters: Prot ocol: Select the protocol used by the SSL-VPN connection. Valid values: UDP and TCP. Port : Specify the port used by the SSL-VPN connection. Invalid values: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. Encrypt ion Algorit hm: Select the encryption algorithm used by the SSL connection. Valid values: AES-128-CBC, AES-192-CBC, AES-256-CBC, and none. Enable Compression: Specify whether to compress the data that is transmitted over the SSL-VPN connection. |

#### 8.2.2 Modify an SSL server

This topic describes how to modify the name, server CIDR block, client CIDR block, and advanced settings of an SSL server. An SSL server is created. For more information, see Create an SSL server.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. In the top navigation bar, select the region where the SSL server is created.
4. On the SSL Servers page, find the SSL server, and then click Edit in the Act ions column.
5. On the Edit SSL Server page, modify the name, server CIDR block, client CIDR block, and advanced
settings of the SSL server, and then click OK.

#### 8.2.3 Configure a security group

This topic describes how to configure a security group to control the inbound and outbound traffic of ECS instances in the security group after an IPsec-VPN connection is created.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. Select the region where the SSL server is deployed.
4. On the SSL Servers page, find the SSL server you want to manage, and then click Conf igure
Rout ing Group in the Act ions column.
5. In the Conf igure Rout ing Group panel, set the following parameters, and then click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Securit y Group | Select the security group to which you want to add the security group rule. |   |   |
| Rule Direct ion | Select the direction in which the rule applies. Out bound: from the ECS instances in the current security group to other ECS instances on Alibaba Cloud or resources on the Internet. Inbound: from other ECS instances on Alibaba Cloud or resources on the Internet to the ECS instances in the security group. |   |   |
| Policy | Select an authorization policy. Allow: allows access requests on the specified ports. Deny: discards requests received on the specified ports without returning messages. If you specify different authorization policies for two security group rules but the other settings are the same, the Deny rule prevails over the Allow rule. |   |   |
| Prot ocol T ype | Select a protocol type. |   |   |
| Port Range | Specify a port range for the security group rule. Specify the port range in the format of 1/200 or 80/80. 1/200 specifies a port range from 1 to 200. 80/80 specifies port 80. Valid values: -1 and 1 to 65535. A value of -1/-1 specifies all ports. |   |   |
| Priorit y | Set a priority for the rule. Valid values: 1 to 100. The default value is 1, which specifies the highest priority. |   |   |
| Aut horizat ion T ype | Select the authorization type of the security group rule. You can select only Address. |   |   |
| Net work T ype | Select the network interface controller (NIC) type. Int ernal: controls inbound and outbound traffic within Alibaba Cloud. Ext ernal: controls inbound and outbound traffic over the Internet. |   |   |
| Aut horizat ion Object | Select the CIDR blocks to be authorized by the security group rule. You can specify up to 10 CIDR blocks at a time. |   |   |
| Descript ion | The description of the security group rule. The description must be 2 to 256 characters in length, and cannot start with htt p:// or https:// . You can leave this parameter empty. |   |   |
|   |   | htt |   |

|   | p:// |
|---|---|

#### 8.2.4 Delete an SSL server

This topic describes how to delete an SSL server.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Servers.
3. In the top navigation bar, select the region where you want to delete the SSL server.
4. On the SSL Servers page, find the SSL server that you want to delete, and click Delet e in the
Act ions column.
5. In the message that appears, click OK.

### 8.3 Manage an SSL client certificate

#### 8.3.1 Create an SSL client certificate

After you create an SSL server, you must create an SSL client certificate based on the configuration of the SSL server. An SSL server is created. For more information, see Create an SSL server.
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
| Region: | Select the region where the SSL client is deployed. |
| Zone | Select the zone where the SSL client is deployed. |
| Name | Enter a name for the SSL client certificate. The name must be 2 to 128 characters in length, and can contain digits, hyphens (-), and underscores ( ). It must start with a letter and cannot start _ with http:// or https:// . |

| Parameter | Description |
|---|---|
| VPN Gat eway | Select the VPN gateway that you want to associate with the SSL client certificate. |
| SSL Server | Select the SSL server that you want to associate with the SSL client certificate. |

#### 8.3.2 Download an SSL client certificate

This topic describes how to download an SSL client certificate. Before you use an SSL client to initiate an SSL-VPN connection, you must import the SSL client certificate to the SSL client. An SSL client certificate is created. For information, see Create an SSL client certificate.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Client s page, find the target SSL client certificate, and then click Download in the
Act ions column.

#### 8.3.3 Delete an SSL client certificate

This topic describes how to delete an SSL client certificate.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Client s page, find the SSL client certificate that you want to delete, and click Delet e
in the Act ions column.
5. In the message that appears, click OK.

### 8.4 Query SSL-VPN connection logs

This topic describes how to query the logs of an SSL server and an SSL client. To troubleshoot the issues in an SSL-VPN connection, you can query the logs of the SSL server and the SSL client to which the connection is established. Context You can query logs that are created within the most recent month. The time range that you can specify for a query cannot exceed 10 minutes. Query the logs of an SSL server.
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Servers page, find the SSL server that you want to manage and click View Logs in the
Act ions column.
5. On the SSL VPN Connect ion Logs page, specify a time range. The system queries logs that are
created during the specified time period. Query the logs of an SSL client
1. Log on to the VPN Gateway console.
2. In the left-side navigation pane, choose VPN > SSL Client s.
3. Select the region where the SSL client is deployed.
4. On the SSL Client s page, find the SSL client certificate that you want to manage and click View
Logs in the Act ions column.
5. On the SSL-VPN Client Logs page, specify a time range. The system queries logs that are created
during the specified time period.
