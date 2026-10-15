---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 VPN Gateway User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 56
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 VPN Gateway User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/VPN%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20VPN%20Gateway%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 VPN Gateway User Guide 20260828

nsole

## Log on to the VPC console

This topic describes how to log on to the Apsara Uni-manager Management Console to manage your virtual private clouds (VPCs). In this example, the Google Chrome browser is used.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. nsole

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

**Forgot password**

If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**. For information about how to bind and enable MFA, see the **Security Center** >
**Multi-factor Authentication** > **Manage Multi-factor Authentication** section in
the Apsara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.

## Getting started

### Get started with IPsec-VPN

#### Overview of IPsec-VPN connections

You can connect a data center to a virtual private cloud (VPC) through an IPsec-VPN connection. This topic provides an overview of IPsec-VPN connections.

**Prerequisites**

Before you use IPsec-VPN to connect a data center to a VPC, make sure that the following requirements are met: The gateway device in the data center supports the IKEv1 and IKEv2 protocols. IPsec-VPN supports the IKEv1 and IKEv2 protocols. All gateway devices that support the two protocols can connect to VPN gateways on Apsara Stack. A static public IP address is assigned to the gateway device in the data center. The CIDR block of the data center does not overlap with the CIDR block of the VPC. You have read and understand the security group rules that apply to the Elastic Cloud Service (ECS) instances in VPCs, and the security group rules allow gateway devices in the data center to access cloud resources.

**Procedure**

1. Create a VPN gateway
You need to enable the IPsec-VPN feature for the VPN gateway. Then, you can establish more than one IPsec-VPN connection to the VPN gateway.
2. Create a customer gateway
You need to load the configuration of the gateway device in the data center to the customer gateway on Apsara Stack.
3. Create an IPsec-VPN connection
An IPsec-VPN connection is a VPN tunnel between a VPN gateway and a gateway device in the data center. The data center can communicate with Apsara Stack through an encrypted tunnel only after an IPsec-VPN connection is established.
4. Configure the gateway device in the data center
You must load the configuration of the VPN gateway on Apsara Stack to the gateway device in the data center.
5. Configure routes on a VPN gateway
You need to add routes to the VPN gateway and advertise these routes to the VPC route table. Then, the VPC can communicate with the data center. For more information, see Overview of gateway routes.
6. Test the connectivity
Log on to an ECS instance that is not assigned a public IP address in the VPC. Then, run the
**ping** command to **ping** the private IP address of a server in the data center.

**Use cases**

Connect a data center to a VPC

#### Connect a data center to a VPC

This topic describes how to use IPsec-VPN to connect a data center to a virtual private cloud (VPC). After you establish an IPsec-VPN connection, the data center and the VPC can communicate with each other.

**Prerequisites**

The gateway device in the data center supports the IKEv1 and IKEv2 protocols. All gateway devices that support these protocols can connect to a VPN gateway. A static public IP address is assigned to the gateway device in the data center. The CIDR block of the data center does not overlap with the CIDR block of the VPC. You have read and understand the security group rules that apply to the Elastic Cloud Service (ECS) instances in VPCs, and the security group rules allow gateway devices in the data center to access cloud resources.

**Background information**

The following scenario is used as an example in this topic. An enterprise has created a VPC on Apsara Stack. The CIDR block of the VPC is 192.168.0.0/16. The CIDR block of the data center is 172.16.0.0/16. The static public IP address of the gateway device in the data center is 211.XX.XX.68. To meet business requirements, the enterprise needs to connect the data center to the VPC. You can establish an IPsec-VPN connection between the data center and the VPC, as shown in the following figure. This way, the data center and the VPC can share resources with each other.

**Step 1: Create a VPN gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, click **Create a VPN Gateway**.
5. On the **Create VPN** page, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization | The organization to which the VPN gateway belongs. |
| Resource Set | The resource set to which the VPN gateway belongs. |
| Region | The region where you want to deploy the VPN gateway. You can create IPsec-VPN connections on VPN gateways to connect a data center to a VPC or connect two VPCs. Make sure that the VPC and the VPN gateway associated with the VPC are deployed in the same region. |
| Zone | The zone to which the VPN gateway belongs. |
| Billing configuration |   |
| Billing method | The billing method of the VPN gateway. Use the default valueP ay-as- you-go. Pay-as-you-go: suits scenarios in which the business volume fluctuates and is difficult to predict. |
| Basic Configurations |   |
| Instance Name | The name of the VPN gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
| VPC | The VPC that you want to associate with the VPN gateway. Note You can also click Create VPC to create a VPC. |
| VSwitch | The vSwitch that you want to associate with the VPN gateway. You can only select the vSwitch in the same zone as the VPC. Note You can also click Create vSwitch to create a vSwitch in the VPC. |

| Bandwidth | The maximum bandwidth value of the VPN gateway. Unit: Mbit/s. The bandwidth is used for data transfer over the Internet. |
|---|---|
| Advanced Settings |   |
| IPsec-VPN | Specifies whether to enable IPsec-VPN. In this example, Disable is selected. |
| SSL-VPN | Specifies whether to enable SSL-VPN. In this example, Enable is selected. |
| SSL-VPN Connections | The number of SSL-VPN connections based on the maximum number of clients that can connect at the same time. |

6. Create a VPN gateway.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **VPN Gateway** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **VPN Gateway** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .
7. Return to the VPN Gateways page to view the VPN gateway that you created.
A newly created VPN gateway is in the **Preparing** state and changes to the **Normal** state in about 1 to 5 minutes. After the state of the VPN gateway changes to **Normal**, the VPN gateway is ready for use.

**Step 2: Create a customer gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > Customer Gateway**.
3. In the top navigation bar, select the region in which you want to create the customer
gateway.
4. On the **Customer Gateways** page, click **Create Customer Gateway**.
5. On the **Create Customer Gateway** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resou rce Set | The organization and resource set to which the customer gateway belongs. |

| Region/Zone | The region and zone in which you want to deploy the customer gateway. Note Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region. |
|---|---|
| Basic Configurations |   |
| Name | The name of the customer gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
| IP Address | Enter the static public IP address of the gateway device in the data center. |
| Description | Enter a description for the customer gateway. The description must be 2 to 100 characters in length. The description can contain digits, hyphens (-), underscores ( ), full-width periods (。), full- _ width commas (，), and full-width colons (：). It must start with a letter and cannot start with http:// or https://. |

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
6. Create a customer gateway.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **Customer Gateway** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **Customer Gateway** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**Step 3: Create an IPsec-VPN connection**

1. In the left-side navigation pane, choose **VPN > IPsec-VPN Connection**.
2. In the top navigation bar, select the region in which you want to create an IPsec-VPN
connection.
3. On the **IPsec Connections** page, click **Create IPsec-VPN Connection**.
4. On the **Create IPSec Connection** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization | The organization to which the IPsec-VPN connection belongs. |
| Resource Set | The resource set to which the IPsec-VPN connection belongs. |
| Region | The region to which the IPsec-VPN connection belongs. Note Make sure that the IPsec-VPN connection and the VPN gateway to be connected are deployed in the same region. |
| Zone | The zone to which the IPsec-VPN connection belongs. |
| Basic Configurations |   |
| Name | The name of the IPsec-VPN connection. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
| VPN Gateway | The VPN gateway to which you want to connect through the IPsec-VPN connection. Note You can also click Create VPN Gateway to create a VPN gateway to which you want to connect the IPsec-VPN connection. |
| Customer Gateway | The customer gateway to which you want to connect through the IPsec- VPN connection. Note You can also click Create Customer Gateway to create a customer gateway to which you want to connect the IPsec-VPN connection. |

| Local CIDR Block | The CIDR block of the VPC in which the VPN gateway is deployed. In this example, 192.168.0.0/16 is used. |
|---|---|
| Peer CIDR Block | The CIDR block of the data center. In this example, 172.16.0.0/16 is used. |
| Effective Immediately | Specifies whether to immediately start negotiations for the connection. Valid values: Yes: starts negotiations after the configuration takes effect. When negotiations are reinitiated, transient connections may occur. No (default): starts negotiations when inbound traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| Group |   |
| Advanced Settings | The type of advanced settings. Select Default. By default, a pre-shared key is automatically generated. Valid values: Default: Use the default advanced settings. Configure: Use custom settings. |

**Step 4: Load the configuration of the IPsec-VPN connections to**

**the gateway devices in the data center**

1. In the left-side navigation pane, choose **VPN > IPsec-VPN Connection**.
2. In the top navigation bar, select the region in which you want to create an IPsec-VPN
connection.
3. On the **IPsec Connections** page, find the IPsec-VPN connection that you want to manage
and click **Download Peer Configuration** in the **Actions** column.
4. In the **IPsec Connection Configuration** dialog box, copy and save the configuration
information. The values of RemoteSubnet and LocalSubnet in the downloaded configuration file are opposite to the values that you specified when you create the IPsec-VPN connection. For a VPN gateway, RemoteSubnet refers to the CIDR block of the data center, whereas LocalSubnet refers to the CIDR block of the VPC. For a gateway device, LocalSubnet refers to the CIDR block of the data center, whereas RemoteSubnet refers to the CIDR block of the VPC.
5. Load the configuration of the IPsec-VPN connection to the gateway device in the data
center. For more information, consult the vendor of your gateway device.

**Step 5: Configure routes for the VPN gateway**

1. In the left-side navigation pane, choose **VPN > VPN Gateway**.
2. In the top navigation bar, select the region in which the VPN gateway resides.
3. On the **VPN Gateways** page, find the VPN gateway and click the gateway ID in the **VPN**
**Gateway ID/Name** column.
4. On the **VPN Gateway Details** tab, click the **Destination-based Route Table** tab.
5. Click **Add Route Entry**. In the **Add Route Entry** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination CIDR Block | The private CIDR block of the data center. In this example, 172.16.0.0/16 is used. |
| Next Hop Type | Select IPsec Connection. |
| Next Hop | The IPsec-VPN connection for which you want to create a destination- based route. |
| Publish to VPC | Specify whether to publish the route to VPC route table. In this example, Yes is selected. |
| Weight | The weight. In this example, 100 is selected. Valid values: 100: specifies a high priority for the destination-based route. 0: specifies a low priority for the destination-based route. Note If two routes are configured with the same destination CIDR block, you cannot set the weights of both routes to 100. |

**Step 6: Test the connectivity**

1. Log on to an ECS instance that is not assigned a public IP address in the VPC.
2. Run the **ping** command to ping a server in the data center to test the network connectivity.

### Get started with SSL-VPN

#### Overview of SSL-VPN

SSL-VPN allows remote clients to connect to a virtual private cloud (VPC) and access the applications or services that are deployed in the VPC securely. This topic describes how to use SSL-VPN.

**Prerequisites**

Before you use SSL-VPN to connect a client to a VPC, make sure that the following requirements are met: The private CIDR block of the client does not overlap with the private CIDR block of the VPC. Otherwise, the client and the VPC cannot communicate with each other. The client can access the Internet. You have read and understand the security group rules that apply to the Elastic Cloud Service (ECS) instances in VPCs, and the security group rules allow gateway devices in the data center to access cloud resources.

**Procedure**

| Step | Description |
|---|---|
| 1 | Create a VPN gateway and enable the SSL-VPN feature. |
| 2 | On the SSL server, specify the private CIDR block that the client needs to access and the CIDR block that is used by the client. |
| 3 | Create and download a client certificate based on the SSL server configuration. |
| 4 | Download and install VPN software on the client, load the SSL client certificate, and then initiate an SSL-VPN connection. |
| 5 | Open the CLI on the client, and run thep ing command to ping an Elastic Compute Service (ECS) instance in the VPC. |

**Use cases**

Connect a client to a VPC.

#### Connect a client to a VPC

This topic describes how to connect a client to a virtual private cloud (VPC) by using SSL-VPN.

**Prerequisites**

The private CIDR block of the client does not overlap with the private CIDR block of the VPC. Otherwise, the client and the VPC cannot communicate with each other. The client can access the Internet. You have read and understand the security group rules that apply to the Elastic Cloud Service (ECS) instances in VPCs, and the security group rules allow gateway devices in the data center to access cloud resources.

**Background information**

The scenario in the following figure is used as an example to describe how to connect Linux, Windows, and Mac clients to a VPC by using SSL-VPN.

**Step 1: Create a VPN gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, click **Create a VPN Gateway**.
5. On the **Create VPN** page, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization | The organization to which the VPN gateway belongs. |
| Resource Set | The resource set to which the VPN gateway belongs. |
| Region | The region where you want to deploy the VPN gateway. You can create IPsec-VPN connections on VPN gateways to connect a data center to a VPC or connect two VPCs. Make sure that the VPC and the VPN gateway associated with the VPC are deployed in the same region. |
| Zone | The zone to which the VPN gateway belongs. |

| Billing configuration |   |
|---|---|
| Billing method | The billing method of the VPN gateway. Use the default valueP ay-as- you-go. Pay-as-you-go: suits scenarios in which the business volume fluctuates and is difficult to predict. |
| Basic Configurations |   |
| Instance Name | The name of the VPN gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
| VPC | The VPC that you want to associate with the VPN gateway. Note You can also click Create VPC to create a VPC. |
| VSwitch | The vSwitch that you want to associate with the VPN gateway. You can only select the vSwitch in the same zone as the VPC. Note You can also click Create vSwitch to create a vSwitch in the VPC. |
| Bandwidth | The maximum bandwidth value of the VPN gateway. Unit: Mbit/s. The bandwidth is used for data transfer over the Internet. |
| Advanced Settings |   |
| IPsec-VPN | Specifies whether to enable IPsec-VPN. In this example, Disable is selected. |
| SSL-VPN | Specifies whether to enable SSL-VPN. In this example, Enable is selected. |
| SSL-VPN Connections | The number of SSL-VPN connections based on the maximum number of clients that can connect at the same time. |

6. Create a VPN gateway.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **VPN Gateway** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **VPN Gateway** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .
7. Return to the VPN Gateways page to view the VPN gateway that you created.
A newly created VPN gateway is in the **Preparing** state and changes to the **Normal** state in about 1 to 5 minutes. After the state of the VPN gateway changes to **Normal**, the VPN gateway is ready for use.

**Step 2: Create an SSL server**

1. In the left-side navigation pane, choose **VPN > SSL Server**.
2. In the top navigation bar, select the region in which you want to create an SSL server.
Make sure that the SSL server and the VPN gateway that you created reside in the same region.
3. On the **SSL Servers** page, click **Create SSL Server**.
4. On the **Create SSL Server** page, configure the parameters. The following table describes
the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization | The organization to which the SSL server belongs. |
| Resource Set | The resource set to which the SSL server belongs. |
| Region | The region in which you want to deploy the SSL server. |
| Zone | The zone in which you want to deploy the SSL server. |
| Basic Settings |   |
| Name | The name of the SSL server. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |

| VPN Gateway | The VPN gateway that you want to associate with the SSL server. Note You can also click Create VPN Gateway to create a VPN gateway. |
|---|---|
| Local CIDR Block | The local CIDR block that your client needs to access by using the SSL-VPN connection. It can be the CIDR block of a VPC, a vSwitch, a data center connected to a VPC through an Express Connect circuit, or a cloud service such as ApsaraDB RDS or Object Storage Service (OSS). You can enter multiple local CIDR blocks. Separate local CIDR blocks with commas (,). Note The subnet mask of the specified CIDR block must be 16 to 29 bits in length. |
| Client CIDR Block | The CIDR block from which an IP address is allocated to the virtual network interface controller (NIC) of the client. Do not enter the private CIDR block of the client. When the client accesses the destination network by using an SSL-VPN connection, the associated VPN gateway allocates an IP address from the client CIDR block to the client. Note Make sure that the local CIDR block and the client CIDR block do not overlap with each other. |
| Advanced Settings |   |
| Advanced Settings | The type of advanced settings. Select Default. |

**Step 3: Create and download an SSL client certificate**

1. In the left-side navigation pane, choose **VPN > SSL Client**.
2. In the top navigation bar, select the region in which you want to create an SSL client.
3. On the **SSL Clients** page, click **Create SSL Client**.
4. On the **Create SSL Client Certificate** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resource Set | Select the organization and resource set to which the SSL client belongs. |

| Region/Zone | Select the region and zone to which the SSL client belongs. |
|---|---|
| Basic Configurations |   |
| Name | Enter a name for the SSL client certificate. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a _ letter and cannot start with http:// or https://. |
| VPN Gateway | The VPN gateway that you want to associate with the SSL client. Note You can also click Create VPN Gateway to create a VPN gateway. |
| SSL Server | Select the SSL server that you want to associate with the SSL client. Note You can also click Create SSL Server to create an SSL server to be associated. |

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
5. On the **SSL Clients** page, find the desired SSL client and click **Download** in the **Actions**
column.
6. View the downloaded SSL client certificate on your on-premises machine.

**Step 4: Configure the client**

The following section describes how to configure clients that run Linux, Mac, and Windows. Configure a client that runs Linux i. Run the following command to install the OpenVPN client:

```bash
yum install -y openvpn
```

ii. Decompress the SSL client certificate package that you downloaded and copy the SSL client certificate to the /etc/openvpn/conf/ directory. iii. Go to the /etc/openvpn/conf/ directory and run the following command to start OpenVPN:

```
openvpn --config /etc/openvpn/conf/config.ovpn --daemon
```

Configure a client that runs Windows i. Download and install OpenVPN. Download OpenVPN. ii. Decompress the downloaded SSL client certificate package and copy the SSL client certificate to the OpenVPN\config directory. In this example, the certificate is copied to C:\Program Files\OpenVPN\config. You need to copy the certificate to the directory in which OpenVPN is installed. iii. Start OpenVPN and click **Connect** to initiate a connection. Configure a client that runs macOS i. Run the following command to install the OpenVPN client:

```
brew install openvpn
```

Make sure that homebrew is installed before you install OpenVPN. ii. Copy the SSL client certificate package that you downloaded in Step 3 to the configuration directory of OpenVPN and decompress the package. Then, initiate an SSL- VPN connection. a. Back up all configuration files in the /usr/local/etc/openvpn folder. b. Run the following command to delete the configuration files of OpenVPN:

```
rm /usr/local/etc/openvpn/*
```

c. Run the following command to copy the downloaded SSL client certificate package to the configuration directory of OpenVPN:

```
cp cert_location /usr/local/etc/openvpn/
```

`cert_location` is the path of the SSL client certificate downloaded in Step 3. Example: /Users/example/Downloads/certs6.zip. d. Run the following command to decompress the SSL client certificate package:

```
cd /usr/local/etc/openvpn/ unzip /usr/local/etc/openvpn/certs6.zip
```

e. Run the following command to initiate a connection:

```python
sudo /usr/local/opt/openvpn/sbin/openvpn --config /usr/local/etc/openvpn/config.ovpn
```

**Step 5: Test the network connectivity**

1. Open the CLI of the client.
2. Run the **ping** command to ping an ECS instance in the VPC.

### Overview of gateway routes

After you create an IPsec-VPN connection by using a VPN gateway, you must add a route to the VPN gateway. Route-based IPsec-VPN allows you to route network traffic in multiple ways and facilitates the configuration and maintenance of VPN policies. You can add the following two types of route to a VPN gateway: Policy-based routes Destination-based routes Policy-based routes take precedence over destination-based routes.

**Policy-based routes**

Policy-based routes forward traffic based on source and destination IP addresses. For more information, see Manage policy-based routes.

**Destination-based routes**

Destination-based routes forward traffic to specified destination IP addresses. For more information, see Manage destination-based routes.

## VPN gateways

### Create and manage a VPN

**gateway**

This topic describes how to create a VPN gateway. You must create a VPN gateway before you can use the IPsec-VPN and SSL-VPN features. After you create a VPN gateway, a public IP address is assigned to the VPN gateway.

**Create a VPN gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, click **Create a VPN Gateway**.
5. On the **Create VPN** page, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Billing configuration |   |
| Billing method | The billing method of the VPN gateway. Use the default valueP ay-as- you-go. Pay-as-you-go: Fees are generated based on the actual amount of consumed resources. This method is suitable for scenarios in which business usage frequently fluctuates, which allows users to flexibly utilize resources based on actual needs and avoid waste. Note This parameter is available only if the administrator has configured billing rules in the operations center. For more information about the billing rules, see the Management billing configurations topic in Apsara Uni-manager Operations Console User Guide. |
| Region |   |
| Organization/Resou rce Set | The organization and resource set to which the VPN gateway belongs. |

| Region/Zone | The region and zone where you want to deploy the VPN gateway. You can create IPsec-VPN connections on VPN gateways to connect a data center to a virtual private cloud (VPC) or connect two VPCs. Make sure that the VPC and the VPN gateway associated with the VPC are deployed in the same region. |
|---|---|
| Basic Configuration |   |
| Instance Name | The name of the VPN gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It must start with a _ letter and cannot start with http:// or https://. |
| VPC | The VPC to be associated with the VPN gateway. Note You can also click Create VPC to create a VPC. |
| VSwitch | The vSwitch to be associated with the VPN gateway. You can select only the vSwitch in the same zone with the VPC. Note You can also click Create vSwitch to create a vSwitch in the VPC. |
| Bandwidth Specification | The maximum bandwidth of the VPN gateway. Unit: Mbps. The bandwidth is used for data transfer over the Internet. |
| Advanced Configuration |   |
| IPsec-VPN | Specifies whether to enable IPsec-VPN. The default value is Enable. Valid values: Enable: After IPsec-VPN is enabled, you can create IPsec-VPN connections between a data center and a VPC, or between two VPCs. Disable |
| SSL-VPN | Specifies whether to enable SSL-VPN. The default value is Disable. Valid values: Enable: SSL-VPN connections are point-to-site connections. SSL-VPN allows you to connect a client to Apsara Stack without the need to configure a customer gateway. Disable |

| SSL Connections | The number of SSL-VPN connections based on the maximum number of clients that can connect at the same time. Note This parameter is required only if you set SSL-VPN to Enable. |
|---|---|

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements. You can click **Quota Management** (the organization/resource set does not have quotas) or click **Quota Management** (the organization/resource set has quotas) in the **Quota** section to manage quotas for cloud services. For more information about quota management, see the **Quota management** topic in **Apsara Uni-manager Management Console User Guide** .
6. Create a VPN gateway.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **VPN Gateway** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **VPN Gateway** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**What to do next**

**View the VPN gateway list**

On the **VPN Gateways** page, you can view the details of VPN gateways. You can use a keyword or a specific filter condition to filter VPN gateways. Click the icon next to a column to sort VPN gateways. Click the icon in the upper-right corner to show or hide items in the VPN gateway list. You can also drag and drop the items to adjust their order. Click the icon next to the **Status** column to filter VPN gateways by status. Click the VPC ID in the **VPC ID/Name** column to view the basic information about the VPC to which the VPN gateway belongs. In the **Monitoring** column, click the icon to view the monitoring information about the VPN gateway. Click the icon next to the VPN gateway name in the **VPN Gateway ID/Name** column to modify the name of a VPN gateway. Click the icon next to the username in the **Creator** column to modify the creator of the VPN gateway.

**Manage tags**

On the **VPN Gateways** page, you can add tags to VPN gateways for management. For more information, see Manage tags.

**Delete a VPN gateway**

You can delete VPN gateways that you no longer need. After you delete a VPN gateway, you can no longer establish IPsec-VPN or SSL-VPN connections to the VPN gateway. Before you delete a VPN gateway, make sure that the following conditions are met: The IPsec-VPN connections established to the VPN gateway are deleted. For more information, see the Delete an IPsec-VPN connection section of the Create and manage IPsec-VPN connections topic. The SSL server associated with the VPN gateway is deleted. For more information, see the Delete an SSL server section of the Create and manage an SSL server topic.
1. On the **VPN Gateways** page, find the VPN gateway that you want to delete, and then click
**Delete** in the **Actions** column.
2. In the **Delete** dialog box, click **Release**.
3. In the **Release Resource** message, click **OK**.
4. In the message that appears, click **OK**.

**Manage a VPN gateway**

1. On the **VPN Gateways** page, find the VPN gateway and click the gateway ID in the **VPN**
**Gateway ID/Name** column.
2. On the **VPN Gateway Details** page, you can manage the VPN gateway.
Click the **Basic Information** tab to view and manage the basic information about the VPN gateway. In the **Basic Information** section, click the VPC ID next to the **VPC ID** parameter to view the basic information about the VPC to which the VPN gateway belongs. In the **Basic Information** section, click the icon next to the **VPN Gateway Name** parameter to modify the name of the VPN gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter and cannot start with http:// or https://. In the **Basic Information** section, click the icon next to the **Description** parameter to modify the description of the VPN gateway. The description must be 2 to 100 characters in length. It must start with a letter and cannot start with http:// or https://. Click the **Destination-based Route Table** tab to manage the destination-based routes of the VPN gateway. For more information, see Manage destination-based routes. Click the **Policy-based Route Table** tab to manage the policy-based routes of the VPN gateway. For more information, see Manage a policy-based route. Click the **Monitoring** tab to view the monitoring information about the VPN gateway. For more information, see View monitoring data. On the **Operation Log** tab, you can view all operation logs of the VPN gateway. For more information, see View operation logs.

### Configure routes of a VPN

**Gateway**

#### Manage destination-based routes

Destination-based routes forward traffic to specified destination IP addresses. This topic describes how to create, publish, modify, and delete a destination-based route.

**Prerequisites**

An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection.

**Create a destination-based route**

After you create an IPsec-VPN connection, you can create a destination-based route for the IPsec-VPN connection.
1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, find the VPN gateway and click the gateway ID in the **VPN**
**Gateway ID/Name** column.
5. On the **VPN Gateway Details** tab, click the **Destination-based Route Table** tab.
6. Click **Add Route Entry**. In the **Add Route Entry** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination CIDR Block | The private CIDR block that you want to access. |
| Next Hop Type | The type of the next hop. Select IPsec connection. |
| Next Hop | Select the IPsec-VPN connection for which you want to create a destination-based route. |

| Publish to VPC | Specify whether to publish the route to virtual private cloud (VPC) route table. Yes (default): publishes the route to the VPC route table. No: does not publish the route to the VPC route table. Note If you select No, you must manually publish the route to the VPC route table. |
|---|---|
| Weight | The weight. Valid values: 100: specifies a high priority for the destination-based route. 0: specifies a low priority for the destination-based route. Note If a route table contains multiple destination-based routes that have the same destination CIDR block and weight, a destination-based route is randomly selected to forward traffic. |

**Modify a destination-based route**

You can change the weight of a destination-based route.
1. On the **VPN Gateway Details** tab, click the **Destination-based Route Table** tab.
2. In the route list, find the route that you want to modify and click **Edit** in the **Actions**
column.
3. In the **Edit route entry** dialog box, select a new **weight** and click **OK**.

**Publish/Unpublish destination-based routes**

You can publish destination-based routes you create or unpublish destination-based routes based on your business requirements.
1. On the **VPN Gateway Details** tab, click the **Destination-based Route Table** tab.
2. In the route list, find the route that you want to manage and click **Advertise** or **Withdraw**
in the **Actions** column.
3. In the message that appears, click **OK**.

**Delete a destination-based route**

1. On the **VPN Gateway Details** tab, click the **Destination-based Route Table** tab.
2. In the route list, find the route that you want to delete and click **Delete** or **Withdraw** in the
**Actions** column.
3. In the **Delete Route Entry** message, click **OK**.

#### Manage a policy-based route

A policy-based route forwards traffic based on source and destination IP addresses. This topic describes how to create, advertise, modify, and delete a policy-based route.

**Prerequisites**

An IPsec-VPN connection is created. For more information, see Create an IPsec-VPN connection.

**Create a policy-based route**

After you create an IPsec-VPN connection, you can create a policy-based route for the IPsec- VPN connection.
1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, find the VPN gateway and click the gateway ID in the **VPN**
**Gateway ID/Name** column.
5. On the **VPN Gateway Details** page, click the **Policy-based Route Table** tab.
6. Click **Add Route Entry**. In the **Add Route Entry** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Destination CIDR Block | Enter the private CIDR block that you want to access. |
| Source CIDR Block | Enter the private CIDR block of the virtual private cloud (VPC). |
| Next Hop Type | Select IPsec Connection. |
| Next Hop | Select the IPsec-VPN connection for which you want to create a policy- based route. |
| Publish to VPC | Specify whether to advertise the route to VPC route table. Yes (default): advertises the route to the VPC route table. No: does not advertise the route to the VPC route table. Note If you select No, you must manually advertise the route to the VPC route table. |

| Weight | Select a weight for the route. 100 (default): a high priority for the route. 0: a low priority for the route. Note If a route table contains multiple policy-based routes that have the same source CIDR block, destination CIDR block, and weight, a policy- based route is randomly selected to forward traffic. |
|---|---|

**Modify a policy-based route**

You can change the weight of a policy-based route.
1. On the **VPN Gateway Details** page, click the **Policy-based Route Table** tab.
2. In the route list, find the route that you want to manage and click **Edit** or **Withdraw** in the
**Actions** column.
3. In the **Edit Route Entry** dialog box, select a new **weight** and click **OK**.

**Publish or withdraw a policy-based route**

You can advertise or withdraw policy-based routes based on your business requirements.
1. On the **VPN Gateway Details** page, click the **Policy-based Route Table** tab.
2. In the route list, find the route that you want to manage and click **Advertise** or **Withdraw**
in the **Actions** column.
3. In the **Advertise Route** message, click **OK**.

**Delete a policy-based route**

1. On the **VPN Gateway Details** page, click the **Policy-based Route Table** tab.
2. In the route list, find the route that you want to delete and click **Delete** or **Withdraw** in the
**Actions** column.
3. In the **Delete Route Entry** message, click **OK**.

## Customer gateways

### Create and manage a

**customer gateway**

This topic describes how to create a customer gateway. You can use a customer gateway to establish an IPsec-VPN connection between a virtual private cloud (VPC) and a data center or between two VPCs. After you create a customer gateway, you can update the information about a gateway device in the data center to Alibaba Cloud. Then, you can connect the customer gateway to a VPN gateway. A customer gateway can connect to multiple VPN gateways.

**Create a customer gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > Customer Gateway**.
3. In the top navigation bar, select the region in which you want to create the customer
gateway.
4. On the **Customer Gateways** page, click **Create Customer Gateway**.
5. On the **Create Customer Gateway** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resou rce Set | The organization and resource set to which the customer gateway belongs. |
| Region/Zone | The region and zone in which you want to deploy the customer gateway. Note Make sure that the customer gateway and the VPN gateway to be connected are deployed in the same region. |
| Basic Configurations |   |
| Name | The name of the customer gateway. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
| IP Address | Enter the static public IP address of the gateway device in the data center. |

| Description | Enter a description for the customer gateway. The description must be 2 to 100 characters in length. The description can contain digits, hyphens (-), underscores ( ), full-width periods (。), full- _ width commas (，), and full-width colons (：). It must start with a letter and cannot start with http:// or https://. |
|---|---|

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
6. Create a customer gateway.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **Customer Gateway** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **Customer Gateway** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**What to do next**

**View the customer gateway List**

On the **Customer Gateways** page, you can view the details of the created gateways in the list. You can use a keyword or a specific filter condition to filter gateways. Click the icon next to a column to sort gateways. Click the icon in the upper-right corner to show or hide items in the gateway list. You can also drag and drop the items to adjust their order. Click the icon next to the customer gateway name in the **Customer Gateway ID/Name** column to modify the name of a customer gateway. Click the icon next to the description in the **Description** column to modify the description of the customer gateway. Click the icon next to the username in the **Creator** column to change the creator of the customer gateway.

**Manage tags**

On the Customer Gateways page, you can add tags to customer gateways for management. For more information, see Manage tags.

**Delete a customer gateway**

You can delete a customer gateway you no longer need. Before you delete a customer gateway, make sure that the IPsec-VPN connection that is associated with the customer gateway is deleted. For more information, see the Delete an IPsec-VPN connection section of the Create and manage IPsec-VPN connections topic.
1. On the **Customer Gateways** page, find the customer gateway that you want to delete,
and then click **Delete** in the **Actions** column.
2. In the **Delete** dialog box, click **Release**.
3. In the **Release Resource** message, click **OK**.
4. In the message that appears, click **OK**.
connections

## Configure IPsec-VPN

**connections**

### Create and manage IPsec-VPN

**connections**

This topic describes how to create an IPsec-VPN connection. After you create a VPN gateway and a customer gateway, you can create an IPsec-VPN connection between the two gateways to encrypt data transmission.

**Prerequisites**

A VPN gateway is created, and the IPsec-VPN feature is enabled. For more information, see Create a VPN gateway. A customer gateway is created. For more information, see Create a customer gateway.

**Create an IPsec-VPN connection**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > IPsec-VPN Connection**.
3. In the top navigation bar, select the region in which you want to create an IPsec-VPN
connection.
4. On the **IPsec Connections** page, click **Create IPsec-VPN Connection**.
5. On the **Create IPSec Connection** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resou rce Set | Select the organization and resource set to which the IPsec-VPN connection belongs. |
| Region/Zone | Select the organization and zone to which the IPsec-VPN connection belongs. Note Make sure that the IPsec-VPN connection and the VPN gateway to be connected are deployed in the same region. |
| Basic Configurations |   |

connections

| Name | The name of the IPsec-VPN connection. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |
|---|---|
| VPN Gateway | Select the VPN gateway to be connected through the IPsec-VPN connection. Note You can also click Create VPN Gateway to create a VPN gateway to which you want to connect through the IPsec-VPN connection. |
| Customer Gateway | Select the customer gateway to be connected through the IPsec-VPN connection. Note You can also click Create Customer Gateway to create a customer gateway to which you want to connect through the IPsec-VPN connection. |
| Local CIDR Block | Enter the CIDR block on the virtual private cloud (VPC) side. The CIDR block is used in Phase 2 negotiations. You can specify multiple local CIDR blocks. Separate CIDR blocks with commas (,). |
| Peer CIDR Block | Enter the CIDR block on the data center side. This CIDR block is used in Phase 2 negotiations. You can specify multiple peer CIDR blocks. Separate CIDR blocks with commas (,). |
| Effective Immediately | Specifies whether to immediately start negotiations for the connection. Valid values: Yes: starts negotiations after the configuration takes effect. When negotiations are reinitiated, transient connections may occur. No (default): starts negotiations when inbound traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| Group |   |
| Advanced Settings | Select the type of advanced settings. Valid values: Default: Use the default advanced settings. Configure: Use custom settings. |
| IKE Settings (Custom advanced settings) |   |

connections

| Pre-shared Key | The pre-shared key used for authentication between the VPN gateway and the customer gateway. You can specify a key, or use the key that is randomly generated by the system. By default, the system generates a 16-character string. To establish the IPsec-VPN connection, you must use the same key for the local side and the peer side. |
|---|---|
| Version | The IKE version. Valid values: ikev1 (default) ikev2 IKEv1 and IKEv2 are supported. Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for scenarios in which multiple CIDR blocks are used. We recommend that you select IKEv2. |
| Negotiation Mode | The negotiation mode. Default value: main. Valid values: main (default): This mode offers higher security during negotiations. aggressive: This mode is faster and has a higher success rate. If the NAT crossing feature is enabled, we recommend that you select the aggressive mode. Connections negotiated in both modes ensure the same level of security for data transmission. |
| Encryption Algorithm | The encryption algorithm that is used in Phase 1 negotiations. Supported algorithms are aes (default), aes192, aes256, des, and 3des. |
| Authentication Algorithm | The authentication algorithm that is used in Phase 1 negotiations. Valid values: sha1 (default) and md5. |
| DH Group | The Diffie-Hellman (DH) key exchange algorithm that is used in Phase 1 negotiations. Default value: group2. Valid values: group1: DH group 1. group2: DH group 2. group5: DH group 5. group14: DH group 14. |
| SA Life Cycle (Seconds) | The SA lifecycle after Phase 1 negotiations succeed. Valid values: 0 to 86400. Default value: 86400. |
| LocalId | The identifier of the VPN gateway. The identifier is used in Phase 1 negotiations. The default value is the public IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. If you set LocalId to a value in the FQDN format, we recommend that you set Negotiation Mode to aggressive. |

connections

| RemoteId | The identifier of the customer gateway. The identifier is used in Phase 1 negotiations. FQDN and IP formats are supported. The default value is the IP address of the customer gateway. If you set RemoteId to a value in the FQDN format, we recommend that you set Negotiation Mode to aggressive. |
|---|---|
| IPsec Settings (Custom advanced settings) |   |
| Encryption Algorithm | The encryption algorithm that is used in Phase 2 negotiations. Valid values: aes (default), aes192, aes256, des, and 3des. |
| Authentication Algorithm | The authentication algorithm that is used in Phase 2 negotiations. Valid values: sha1 and md5 (default). |
| DH Group | The DH key exchange algorithm that is used in Phase 2 negotiations. Default value: group2. Valid values: disabled: does not use a DH key exchange algorithm. For clients that do not support perfect forward secrecy (PFS), select disabled. If you select a value other than disabled, the PFS feature is enabled by default, which requires a key update for every renegotiation. Therefore, you must also enable PFS for the client. group1: DH group 1. group2: DH group 2. group5: DH group 5. group14: DH group 14. |
| SA Life Cycle (Seconds) | The SA lifecycle after Phase 2 negotiations succeed. Valid values: 0 to 86400. Default value: 86400. |
| DPD Configuration | Specifies whether to enable the dead peer detection (DPD) feature. Default value: Enabled. After you enable DPD, the initiator of the IPsec-VPN connection sends DPD packets to check the existence and availability of the peer. If no response is received from the peer within the specified period of time, the connection fails. Then, the Internet Security Association and Key Management Protocol (ISAKMP) SA, IPsec SA, and IPsec tunnel are deleted. |
| NAT Traversal | Specifies whether to enable the NAT traversal feature. Default value: Enabled. After you enable NAT traversal, the initiator does not check UDP ports during Internet Key Exchange (IKE) negotiations and can automatically discover NAT gateway devices along the IPsec tunnel. |

connections Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
6. Create an IPsec-VPN connection.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **IPsec Connection** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **IPsec Connection** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**What to do next**

**View the IPsec-VPN connection list**

On the IPsec Connections page, you can view the details of the created IPsec-VPN connection. Use a keyword or a specific filter condition to filter IPsec-VPN connections. Click the icon next to a column to sort IPsec-VPN connections. Click the icon in the upper-right corner to show or hide items in the IPsec-VPN connection list. You can also drag and drop the items to adjust their order. Click the icon next to the **Status** column to filter IPsec-VPN connections by status. Click the VPN gateway ID in the **VPN Gateway ID/Name** column to view the basic information of the VPN gateway to be connected through the IPsec-VPN connection. Click the customer gateway ID in the **Customer Gateway ID/Name** column to view the basic information of the customer gateway to be connected through the IPsec-VPN connection. Click the icon next to the name in the **IPsec Connection ID/Name** column to modify the name of the IPsec-VPN connection. Click the icon next to the username in the **Creator** column to change the name of the user who created the IPsec-VPN connection.

**Manage tags**

On the **IPsec Connections** page, you can add tags to IPsec-VPN connections for management. For more information, see Manage tags.

**Modify an IPsec-VPN connection**

After you create an IPsec-VPN connection, you can modify its configurations.
1. On the **IPsec Connections** page, find the IPsec-VPN connection that you want to modify
and click **Edit** in the **Actions** column. connections
2. In the **Edit IPsec Connection** dialog box, modify the name, advanced settings, and CIDR
block of the IPsec-VPN connection, and then click **OK**.

**Download the configurations of an IPsec-VPN connection**

After you create an IPsec-VPN connection, you can download its configuration.
1. On the **IPsec Connections** page, find the IPsec-VPN connection that you want to manage
and click **Download Peer Configuration** in the **Actions** column.
2. In the **IPsec Connection Configuration** dialog box, copy and save the configuration
information. The values of RemoteSubnet and LocalSubnet in the downloaded configuration file are opposite to the values that you specified when you create the IPsec-VPN connection. For a VPN gateway, RemoteSubnet refers to the CIDR block of the data center, whereas LocalSubnet refers to the CIDR block of the VPC. For a gateway device, LocalSubnet refers to the CIDR block of the data center, whereas RemoteSubnet refers to the CIDR block of the VPC.

**Delete an IPsec-VPN connection**

You can delete an IPsec-VPN connection you no longer need.
1. On the **IPsec Connections** page, find the IPsec-VPN connection that you want to delete
and click **Delete** in the **Actions** column.
2. In the **Delete** dialog box, confirm the IPsec-VPN connection information and click **Release**.
3. In the **Release Resource** message, click **OK**.

### Configure a security group

This topic describes how to configure a security group to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances in the security group.

**Procedure**

**Important**

You can modify or delete security group rules in the ECS console.
1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > IPsec-VPN Connection**.
3. In the top navigation bar, select the region in which you want to create an IPsec-VPN
connection.
4. On the **IPsec Connections** page, find the IPsec-VPN connection that you want to manage
and click **Configure Routing Security Groups** in the **Actions** column.
5. In the **Configure Routing Security Groups** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|

connections

| VPC | Select the VPC to which the security group belongs. You can enter a keyword or specify advanced filter conditions to search for a specific VPC. |
|---|---|
| Security Group | Select a security group for which you want to configure rules based on the selected VPC. You can use a keyword or a specific filter condition to filter security groups. |
| Rule Direction | The direction to which the security group rule applies. Outbound: controls data transfer from the ECS instances in the security group to the Internet or other ECS instances. Inbound Direction: controls data transfer from the Internet or other ECS instances to the ECS instances in the security group. |
| Authorization Policy | The action to be performed on the requests that match the rule. Allow: accepts requests. Rejection: rejects requests without returning a response. If two security group rules use the same settings except for the action, the Rejection action prevails over the Allow action. |
| Protocol Type | Select a protocol for the security group rule. Valid values: ALL, TCP, UDP, ICMP, and GRE. |
| Port Range | The port range for the security group rule. Valid values: 1 to 65535. A value of - 1/-1 specifies all ports. Do not specify this value. Examples: 1/200: specifies port 1 to port 200. 80/80: specifies port 80. |
| Priority | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Authorization Type | The type of addresses that the security group rule allows or denies. Only Address Segment Access is supported. |
| NIC Type | The type of data transfer that the security group rule controls. You can set the parameter only to Intranet, which indicates that the security group rule applies only to the internal network. |
| Authorization Object | The CIDR blocks that you want the security group rule to allow or deny. You can specify at most 10 groups of authorization objects. |

connections

| Automatic Routing | Specify whether to automatically advertise routes. By default, this feature is disabled. |
|---|---|
| Description | The description for the security group rule. This parameter is optional. If you enter a description, the description must be 2 to 256 characters in length, and cannot start with http:// or https:// . |

## Configure SSL-VPN

### Create and manage an SSL

**server**

This topic describes how to create an SSL server. Before you can create an SSL-VPN connection, you must create an SSL server.

**Prerequisites**

A VPN gateway is created, and SSL-VPN is enabled for the VPN gateway. For more information, see Create a VPN gateway.

**Create an SSL server**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > SSL Server**.
3. In the top navigation bar, select the region in which you want to create an SSL server.
Make sure that the SSL server and the VPN gateway that you created reside in the same region.
4. On the **SSL Servers** page, click **Create SSL Server**.
5. On the **Create SSL Server** page, configure the parameters. The following table describes
the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resou rce Set | Select the organization and resource set to which the SSL server belongs. |
| Region/Availability Zone | Select the region and zone to which the SSL server belongs. |
| Basic Configuration |   |
| Name | The name of the SSL server. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https://. |

| VPN Gateway | The VPN gateway that you want to associate with the SSL server. Note You can also click Create VPN Gateway to create a VPN Gateway to be associated with. |
|---|---|
| Local CIDR Block | The local CIDR block that your client needs to access by using the SSL-VPN connection. It can be the CIDR block of a virtual private cloud (VPC), a vSwitch, a data center connected to a VPC through an Express Connect circuit, or a cloud service such as ApsaraDB RDS or Object Storage Service (OSS). You can enter multiple local CIDR blocks. Separate local CIDR blocks with commas (,). Note The subnet mask of the specified CIDR block must be 16 to 29 bits in length. |
| Client CIDR Block | The CIDR block from which an IP address is allocated to the virtual network interface controller (NIC) of the client. Do not enter the private CIDR block of the client. When the client accesses the destination network by using an SSL-VPN connection, the associated VPN gateway allocates an IP address from the client CIDR block to the client. Note Make sure that the local CIDR block and the client CIDR block do not overlap with each other. |
| Advanced Configuration |   |
| Advanced Configuration | Select the type of advanced settings. Valid values: Default: Use the default settings. Configuration: Use custom settings. You can set the following parameters: Protocol: Select a protocol for the SSL-VPN connection. Valid values: UDP (default) and TCP. Port: Specify the port used by the SSL-VPN connection. You cannot use the following port numbers: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. Encryption Algorithm: Select the encryption algorithm for the SSL- VPN connection. Valid values: AES-128-CBC (default), AES-192-CBC, AES-256-CBC, and none. Compression Enabled: specifies whether to compress the data that is transmitted over an SSL-VPN connection. Default value: No. |

| Two-factor Authentication | Specifies whether to enable two-factor authentication for an SSL-VPN connection. By default, two-factor authentication is disabled. |
|---|---|
| IDaaS Instance | Select the Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) instance used for authentication. Note This parameter is required when you enable two-factor authentication. |
| IDaaS Application | Select the ID of the IDaaS application used for authentication. Note This parameter is required when you enable two-factor authentication. |

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
6. Create an SSL server.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **SSL Server** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **SSL Server** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**What to do next**

**View the SSL server list**

On the **SSL Servers** page, you can view the details of the created instance in the list. Use a keyword or a specific filter condition to filter SSL servers. Click the icon next to a column to sort SSL servers. Click the icon in the upper-right corner to show or hide items in the SSL server list. You can also drag and drop the items to adjust their order. Click the instance ID in the **VPN Gateway ID/Name** column to view the basic information of the VPN gateway associated with the SSL server. Click the icon next to the instance name in the **SSL Server ID/Name** column to modify the name of the SSL server. Click the icon next to the username in the **Creator** column to modify the creator of the SSL server.

**Manage tags**

On the **SSL Servers** page, you can add tags to instances for management. For more information, see Manage tags.

**Modify an SSL server**

After you create an SSL server, you can modify its configurations.
1. On the **SSL Servers** page, find the SSL server you want to modify and click **Edit** in the
**Actions** column.
2. In the **Edit SSL Server** dialog box, modify the **name**, **local CIDR block**, **client CIDR**
**block**, and **advanced settings** of the SSL server, and then click **OK**.

**View details of an SSL server**

1. On the **SSL Servers** page, find the SSL server that you want to manage and click **Details**
in the **Actions** column.
2. On the **Details** page, view the configuration of the SSL server.

**Delete an SSL server**

You can delete an SSL server that you no longer require.
1. On the **SSL Servers** page, find the target SSL server and click **Delete** in the **Actions**
column.
2. In the **Delete** dialog box, confirm the SSL server information and click **Release**.
3. In the **Release Resource** message, click **OK**.

### Configure a security group

This topic describes how to configure a security group to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances in the security group after an IPsec-VPN connection is created.

**Procedure**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > SSL Server**.
3. In the top navigation bar, select the region in which you want to create an SSL server.
Make sure that the SSL server and the VPN gateway that you created reside in the same region.
4. On the **SSL Servers** page, find the SSL server that you want to manage and click
**Configure Routing Security Groups** in the **Actions** column.
5. In the **Configure Routing Security Groups** dialog box, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Security Group | The security group to which you want to add the security group rule. |
| Regular Direction | The direction to which the security group rule applies. Valid values: Outbound: controls data transfer from the ECS instances in the security group to the Internet or other ECS instances. Inbound: controls data transfer from the Internet or other ECS instances to the ECS instances in the security group. |
| Authorization Policy | The action to be performed on the requests that match the rule. Valid values: Allow: accepts requests. Rejection: rejects requests without returning a response. If two security group rules use the same settings except for the action, the Rejection action prevails over the Allow action. |
| Protocol Type | The protocol for the security group rule. |
| Port Range | The port range for the security group rule. Valid values: -1 and 1 to 65535. You cannot enter only -1. Examples: 1/200 specifies ports 1 to 200. 80/80 specifies port 80. -1/-1 specifies all ports. |
| Priority | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Authorization Type | The type of addresses that the security group rule allows or denies. Only Address Segment Access is supported. |
| NIC Type | The type of data transfer that the security group rule controls. Valid values: Intranet: controls data transfer within Apsara Stack. Public Network: controls data transfer over the Internet. |
| Authorization Object | The CIDR blocks that you want the security group rule to allow or deny. You can specify at most 10 CIDR blocks. |
| Description | The description for the security group rule. This parameter is optional. If you enter a description, the description must be 2 to 256 characters in length, and cannot start with http:// or https:// . |

### Create and manage an SSL

**client certificate**

After you create an SSL server, you must create an SSL client certificate based on the configuration of the SSL server.

**Prerequisites**

An SSL server is created. For more information, see the "Create an SSL server" section of the Create and manage an SSL server topic.

**Create an SSL client**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > SSL Client**.
3. In the top navigation bar, select the region in which you want to create an SSL client.
4. On the **SSL Clients** page, click **Create SSL Client**.
5. On the **Create SSL Client Certificate** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Region |   |
| Organization/Resource Set | Select the organization and resource set to which the SSL client belongs. |
| Region/Zone | Select the region and zone to which the SSL client belongs. |
| Basic Configurations |   |
| Name | Enter a name for the SSL client certificate. The name must be 2 to 100 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a _ letter and cannot start with http:// or https://. |
| VPN Gateway | The VPN gateway that you want to associate with the SSL client. Note You can also click Create VPN Gateway to create a VPN gateway. |

| SSL Server | Select the SSL server that you want to associate with the SSL client. Note You can also click Create SSL Server to create an SSL server to be associated. |
|---|---|

Before you click Submit to create the instance, you can view and check the configurations of the instance in the right-side **Configuration overview** section. You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
6. Create an SSL client.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **SSL Client** is displayed in the **Cloud resources** column of the service. If no service whose **Cloud resources** value is **SSL Client** exists on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Operations Console User Guide** .

**What to do next**

**View the SSL client list**

On the **SSL Clients** page, you can view the details about the created instances. You can use a keyword or a specific filter condition to filter instances. Click the icon next to a column to sort instances. Click the icon in the upper-right corner to show or hide items in the list. You can also drag and drop the items to adjust their order. Click the icon next to the **Status** column to filter instances by status. Click the instance ID in the **SSL Server ID/Name** column to view the basic information of the SSL server associated with the SSL client. Click the icon next to the name in the **SSL Client ID/Name** column to modify the name of the SSL client certificate. Click the icon next to the username in the **Creator** column to modify the creator of the SSL server.

**Manage tags**

On the **SSL Clients** page, you can add tags to instances for management. For more information, see Manage tags.

**Download an SSL client certificate**

To connect an SSL client to SSL-VPN, load an SSL client certificate. You can download an SSL client certificate in the VPN Gateway console.
1. On the **SSL Clients** page, find the desired SSL client and click **Download** in the **Actions**
column.
2. View the downloaded SSL client certificate on your on-premises machine.

**Delete an SSL client certificate**

You can delete an SSL client certificate that you no longer need.
1. On the **SSL Clients** page, find the desired SSL client and click **Delete** in the **Actions**
column.
2. In the **Delete** dialog box, confirm the instance information and click **Release**.
3. In the **Release Resource** message, click **OK**.

## Manage tags

VPN Gateway allows you to use tags to mark and classify related resources. This facilitates resource search and aggregation. This topic describes how to add tags to VPN gateways and manage the tags. You can use tags to manage other VPN gateway resources by performing similar operations.

**Overview**

As the number of VPN gateways increases, management of VPN gateways becomes more complex. To facilitate instance search and filtering, you can use tags to group VPN gateways. Tags are used to mark instances. Each tag consists of a key and a value. Before you use tags, take note of the following limits: You can manage tags for VPN gateways, customer gateways, IPsec connections, SSL servers, and SSL clients. Each tag key that is added to an instance must be unique. You can modify the key and value of a tag or remove a tag from a resource. If you delete a resource, all tags added to the resource are removed. This operation does not affect the tags added to other resources. You can add up to 20 tags to an instance. This quota cannot be increased.

**Add tags to a VPN gateway**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, add tags to a VPN gateway.
Add tags to a single VPN gateway. a. On the **VPN Gateways** page, find the VPN gateway whose tags you want to manage, move the pointer over the icon in the **Tag** column, and then click **Edit**. b. In the **Edit Tags** dialog box, configure the following parameters, click **Add** to add multiple tags, and then click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | The key of the tag. You can select or enter a tag key. The tag key can be up to 64 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |
| Tag Value | The value of the tag. You can select or enter a tag value. The tag value can be up to 128 characters in length, and cannot contain http:// or https:// . It cannot start with aliyun or acs: . |

c. In the **Configure Tags successfully** dialog box, confirm the tag information and click
**Close**.
Add tags to multiple VPN gateways at a time. a. On the **VPN Gateways** page, select the VPN gateways to which you want to add tags. In the lower-left corner of the page, click **Batch Add Tags**. b. In the **Batch Add Tags** dialog box, click **Add**, configure the **Tag Key** and **Tag Value** parameters, and then click **OK**. c. In the **Configure Tags successfully** dialog box, confirm the tag information and click
**Close**.

**Filter VPN gateways by tag**

After you add tags to VPN gateways, you can efficiently filter VPN gateways by tag.
1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, select **Tag** from the drop-down list next to **Create a VPN**
**Gateway**.
5. In the dialog box that appears, select a **tag key** and a **tag value**, and click **Search**. The
VPN gateways with the specified tag key and tag value are displayed.

**Remove tags from VPN gateways**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, perform the following operations to remove tags from VPN
gateway: Remove tags from a single VPN gateway a. On the **VPN Gateways** page, find the VPN gateway whose tags you want to manage, move the pointer over the icon in the **Tag** column, and then click **Edit**. b. In the **Edit Tags** dialog box, click the icon next to the tag that you want to remove and click **OK**. c. In the **Configure Tags successfully** dialog box, confirm the tag information and click
**Close**.
Remove tags from multiple VPN gateways at a time a. On the **VPN Gateways** page, select the VPN gateways from which you want to remove tags. In the lower-left corner of the page, click **Batch Remove Tags**. b. In the **Batch Remove Tags** dialog box, select the tags that you want to remove in the
**Tags to Remove** section and click **OK**.
c. In the **Configure Tags successfully** dialog box, confirm the tag information and click
**Close**.
enance

## Monitoring and

**maintenance**

### View monitoring data

This topic describes how to monitor a VPN gateway by using CloudMonitor. You can also set threshold-triggered alert rules and monitor the traffic of a VPN gateway. When a threshold is reached, a notification is sent to you.

**Prerequisites**

Before you start, make sure that the following requirements are met: Simple Log Service is activated. CloudMonitor is activated.

**View monitoring data**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. You can use the following methods to view the monitoring data of a VPN gateway.
View the monitoring data on the VPN Gateways page. a. On the **VPN Gateways** page, click in the **Monitor** column of the desired VPN gateway. b. The **Monitor** panel appears. You can view the monitoring information on this page. View the monitoring data on the details page. a. On the **VPN Gateways** page, find the desired VPN gateway and click its ID. b. On the page that appears, click the **Monitor** tab. By default, the system displays the monitoring data within the last hour. You can also choose 3 hours, 6 hours, or 12 hours or specify a **custom** time period. VPN Gateway provides the following monitoring information:

| Metric | Description |
|---|---|
| Inbound Packet Rate of VPN Gateway | The rate at which packets are received by the VPN gateway. |
| Outbound Packet Rate of VPN Gateway | The rate at which packets are sent by the VPN gateway. |

enance

| Inbound Traffic Rate of VPN Gateway | The rate of inbound traffic. |
|---|---|
| Outbound Traffic Rate of VPN Gateway | The rate of outbound traffic. |
| Number of SSL Clients | The number of clients that are connected to Alibaba Cloud by using the SSL-VPN connection. |

**What to do next**

**Create threshold-triggered alert rules**

In the **Monitor** panel, you can create threshold-triggered alert rules. When the value of a metric exceeds the threshold, a notification is sent to you.
1. On the **Monitor** page, click
next to a metric.
2. In the **Create Alert Rule** dialog box, configure parameters and click **OK**.
The following table describes only the parameters that are related to this topic. For other parameters, see **Alert rules** > **Create an alert rule** in **Alerting service** of
**CloudMonitor CMS User Guide**.

| Parameter | Description |
|---|---|
| Alert Rule | The name of the threshold-triggered alert rule. |
| Metric | The metric of the cloud service that you want to monitor. By default, the current metric is selected. |
| Metric Dimensions | The metric dimensions, excluding the instance ID dimension. This parameter is displayed only if you set the Resource Range parameter to Instance. |

enance

| Threshold and Alert Level | Valid values of the alert level: Critical, Warning, and Info. Valid values of the aggregate value type: Average, Minimum, and Maximum. Valid values of the monitoring period: continuous, 5 consecutive cycles, 10 consecutive cycles, 15 consecutive cycles, 30 consecutive cycles, and 60 consecutive cycles. Valid values of the comparison relationship between the monitoring data and alert threshold: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, Year-on-year decline at the same time yesterday, Increase compared with the last monitoring cycle, Decline compared with the last monitoring cycle, Increase compared with the last week, and Decline compared with the last week. You also need to set an alert threshold and a trigger count. An alert is generated if the monitoring data reaches the specified threshold for the specified number of times at a specific interval. |
|---|---|

### View operation logs

This topic describes how to view operation logs on a VPN gateway. This helps analyze and track operations.

**Procedure**

1. Log in to the VPC console.
2. In the left-side navigation pane, choose **VPN > VPN Gateway**.
3. In the top navigation bar, select the region in which the VPN gateway resides.
4. On the **VPN Gateways** page, find the VPN gateway that you want to manage and click its
ID.
5. On the VPN gateway details page, click the **Operation Records** tab.
6. On the **Operation Records** tab, you can view the operation records.
Operation records are retained for seven days. To adjust the retention period, modify the logging configuration as an administrator. If you extend the retention period by modifying the logging configuration, the previous log data is not recorded. You can filter operation records by **Operation Name** and **Operator**. The following table describes the supported filter conditions.

| Filtering condition | Description |
|---|---|
| Performed by | Type the name of the operator. |
| Operation Name | Select the API operation performed on the VPC gateway. |
| Execution status | The execution status. Valid values: Success and Failed. |

enance

| Operation Source IP | Type the source IP address of the operation. |
|---|---|
| Operation Time | Specify the time range that you want to query. |

7. **Optional**: Find the event that you want to view and click **Operation Details** in the
**Operation** column to view details.
