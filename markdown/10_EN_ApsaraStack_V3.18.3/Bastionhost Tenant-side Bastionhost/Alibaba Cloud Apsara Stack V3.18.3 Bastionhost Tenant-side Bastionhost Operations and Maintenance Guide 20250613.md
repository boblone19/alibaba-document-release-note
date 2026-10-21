---
title: "Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost Operations and Maintenance Guide 20250613"
product_version: "V3.18.3"
doc_version: "20250613"
pdf_pages: 26
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost Operations and Maintenance Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A0%A1%E5%9E%92%E6%9C%BA/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Bastionhost%20Tenant-side%C2%A0Bastionhost%20Operations%20and%20Maintenance%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost Operations and Maintenance Guide 20250613

## Table of Contents

- 1 Cloud-native Bastionhost O&M Guide
  - 1.1 Web-based O&M operations
    - 1.1.1 Log on to the O&M audit system
    - 1.1.2 Install Bastionhost Assistant
    - 1.1.3 Specify an O&M tool
    - 1.1.4 Host O&M
      - 1.1.4.1 O&M of hosts that use SSH
      - 1.1.4.2 O&M of hosts that use RDP
    - 1.1.5 Database O&M
      - 1.1.5.2 Tunnel O&M
  - 1.2 C/S O&M operations
    - 1.2.1 Preparations
    - 1.2.2 Host O&M
      - 1.2.2.1 O&M of hosts that use SSH, Telnet, and RLogin
      - 1.2.2.2 O&M of hosts that use RDP
      - 1.2.2.3 O&M of hosts that use SFTP
      - 1.2.2.4 O&M of hosts that use FTP
  - 1.3 O&M of computers that run the macOS operating system
  - 1.4 Host logon O&M
    - 1.4.1 Log on to a host by using menus for a CLI terminal application
    - 1.4.2 Log on to a host by using menus for a remote desktop connection application

## 1 Cloud-native Bastionhost O&M Guide

**O&M Guide**

### 1.1 Web-based O&M operations

After an administrator grants permissions on a host to an O&M engineer, the O&M engineer can log on to the host from the web page of the O&M audit system to perform O&M operations. Only O&M engineers of Windows terminals can use the preceding method to perform O&M operations.

#### 1.1.1 Log on to the O&M audit system

This topic describes how to log on to the O&M audit system.
1. Log on to the O&M audit system by using a browser and enter the username, password,
and verification code.
2. Click **Log On** to enter the system. Change the password if it is the first time you log on to
the O&M audit system.

#### 1.1.2 Install Bastionhost Assistant

This topic describes how to install Bastionhost Assistant.
1. In the upper-right corner of the Control Panel page, move the pointer over the username
and click Tool Download to go the Tool Download page.
2. Download and install Bastionhost Assistant.

> **Note:** Bastionhost Assistant is a logon tool that you need to install if you want to call an on- premises O&M client tool based on a web page. Make sure that you are not blocked by antivirus software.

#### 1.1.3 Specify an O&M tool

This topic provides an example on how to specify Xshell as an O&M tool.
1. Click **SSH**. On the configuration page that appears, set Client Program to Xshell and
configure the Terminal Type and Encoding Format parameters.
2. Click **Save**. In the dialog box that appears, select Xshell from the Select Client drop-down
list and select the related on-premises package. SSO configuration:
3. Click **OK**. A message indicating that the configuration is successful is displayed.
Message for successful configuration:
4. Click **OK**. Xshell is specified as an O&M tool.
After the configuration is complete, close the page.

#### 1.1.4 Host O&M

This topic provides an example on how to perform O&M operations on hosts that use Remote Desktop Protocol (RDP) or SSH.

##### 1.1.4.1 O&M of hosts that use SSH

This topic describes O&M of hosts that use SSH.
1. Choose **O&M** > **Host O&M** and find hosts that use SSH.
2. Open the **on-premises client** to access the desired host on which you want to perform
O&M operations.

##### 1.1.4.2 O&M of hosts that use RDP

This topic describes O&M of hosts that use Remote Desktop Protocol (RDP).
1. Choose **O&M** > **Host O&M** and find hosts that use RDP.
2. Open the **H5 client** to access the desired host on which you want to perform O&M
operations.

#### 1.1.5 Database O&M

##### 1.1.5.1 BS O&M

This topic describes BS O&M of hosts that use MySQL, Oracle, SQL Server, and DB2 protocols.
1. Choose **O&M** > **Host O&M** and find hosts that use the MySQL protocol.
2. Open the **on-premises client** to access the desired host on which you want to perform
O&M operations.

##### 1.1.5.2 Tunnel O&M

This topic describes tunnel O&M of hosts that use MySQL and Oracle protocols.
1. Open the Navicat client and create a MySQL connection. On the General tab of the window
that appears, enter the connection name and information about the host that uses the MySQL protocol. On the SSH tab of the same window, select **Use SSH Channel** and enter information such as the IP address, username, and password of the bastion host.
2. Click OK to save the configurations and double-click the tag for a MySQL connection.

### 1.2 C/S O&M operations

O&M engineers log on to the O&M audit system by using an on-premises client tool and then access the desired host.

#### 1.2.1 Preparations

This topic describes the preparations for C/S O&M.

**Install O&M tools that support SSH on your on-premises machine**

For example, you can install PuTTY, SecureCRT, and Xshell.

**Install O&M tools that support Remote Desktop Protocol (RDP) on your on-**

**premises machine**

For example, you can install a remote desktop connection tool supported by Windows systems.

**Install O&M tools that support Secure File Transfer Protocol (SFTP) on your on-**

**premises machine**

For example, you can install WinSCP and Xftp.

**Install O&M tools that support FTP on your on-premises machine**

For example, you can install Xftp.

**Make sure that the port of your terminal can access the port of the O&M audit**

**system**

Default ports of the O&M audit system: Port 60022 is used to access hosts that use SSH, Telnet, and SFTP. Port 63389 is used to access hosts that use RDP. Port 60021 is used to access hosts that use FTP.

#### 1.2.2 Host O&M

##### 1.2.2.1 O&M of hosts that use SSH, Telnet, and RLogin

**RLogin**

This topic provides an example on how to use Xshell to perform O&M operations on hosts that use SSH, Telnet, and RLogin.
1. Open the Xshell tool. In the logon window of the Xshell tool, enter the IP address and port
number 60022 of the O&M audit system.
2. Click **Connect**. In the logon window of the O&M audit system, enter the username and
password of the O&M audit system.
3. Click **OK**. On the asset management page that appears, find hosts by pressing up and down
arrow keys, and the Enter key.
4. After you press the Enter key, an input box is displayed. Enter the username for logging on
to the host.
5. After you press the Enter key, the host logon page is displayed. Enter the password for
logging on to the host.
6. After you press the Enter key, you enter the page on which you can perform O&M
operations on the host.

##### 1.2.2.2 O&M of hosts that use RDP

This topic provides an example on how to use a remote desktop connection tool Microsoft Terminal Server Client (MSTSC) to perform O&M operations on hosts that use Remote Desktop Protocol (RDP).
1. Open the **Start** menu on your Windows computer, enter mstsc in the Run input box, and
then press the Enter key. In the **Remote Desktop Connection** dialog box, enter the `IP`

```
address and port number 63389 of the O&M audit system .
```

2. Click **Connect**. The **Do you trust this remote connection?** dialog box appears.
3. Click **Connect**. The **Cannot verify the identity of the computer that requests the**
**remote connection. Are you sure that you want to continue?** dialog box appears.
4. Click **Yes**. In the login dialog box, enter the username and password for logging on to the
O&M audit system.
5. Click **Login**. On the asset management page that appears, select an authorized asset or
search for the host information in the search box.
6. Double-click the host. The host logon page is displayed. Enter the username and password
for logging on to the host.
7. After you press the Enter key, you can enter the page on which you can perform O&M
operations on the host.

##### 1.2.2.3 O&M of hosts that use SFTP

This topic provides an example on how to use WinSCP to perform O&M operations on hosts that use Secure File Transfer Protocol (SFTP).
1. Open the WinSCP tool. In the logon window of the tool, enter the IP address, port number
60022, username, and password of the O&M audit system.
2. Click **Log On**. In the window that appears, you can view the list of hosts on the right.
3. Find the desired host and double-click the host. You can access the directories of the host
and transfer files.

##### 1.2.2.4 O&M of hosts that use FTP

This topic provides an example on how to use Xftp to perform O&M operations on hosts that use FTP.
1. O&M engineers can go to the web page of a bastion host by using a browser. In the upper-
right corner of the page that appears, move the pointer over the username and click **View**
**Personal Information** to go to the page on which you can view the personal information
about the user.
2. On the **CS Logon Password** tab of the **Personal Information** page, specify a CS logon
password. This password is used to log on to Bastionhost to perform C/S O&M operations on hosts that use FTP.
3. Open the Xftp tool. In the logon window of the tool, enter the IP address, port number
60021, username, CS logon password, and FTP of the O&M audit system.
4. Click **Connect**. In the window that appears, you can view the list of hosts on the right.
5. Find the desired host and double-click the host. You can access the directories of the host
and transfer files.

### 1.3 O&M of computers that run the macOS operating system

**the macOS operating system**

O&M engineers log on to the O&M audit system by using a client tool that is an application running the macOS operating system and then access the desired host.

> **Note:** Bastionhost Assistant is applicable only to the Windows systems. O&M engineers of systems that run the macOS operating system cannot log on to a bastion host to perform web-based O&M operations.

**Install applications that support SSH on your on-premises**

**machine**

For example, you can install applications such as a CLI terminal, SecureCRT, and Xshell.

**Install applications that support Remote Desktop Protocol**

**(RDP) on your on-premises machine**

For example, you can install a remote desktop connection application.

**Make sure that the port of your terminal that runs the macOS**

**operating system can access the port of the O&M audit system.**

Port 60022 is used to access hosts that use SSH. Port 63389 is used to access hosts that use RDP.

**Make sure that the port of the O&M audit system can access**

**the O&M port of the desired host.**

SSH port 22 and RDP port 3389

### 1.4 Host logon O&M

#### 1.4.1 Log on to a host by using menus for a CLI terminal application

**CLI terminal application**

This topic describes how to log on to a host by using menus for a CLI terminal application.
1. Start the CLI terminal application and enter `ssh Username of the O&M audit system@IP`

```
address of the O&M audit system-p60022 .
```

2. Press the Enter key. On the asset management page that appears, find authorized assets
by pressing up and down arrow keys.
3. After you press the Enter key, select the username that you want to use to log on to the
desired host.
4. After you press the Enter key, you enter the page on which you can perform O&M
operations on the host.

#### 1.4.2 Log on to a host by using menus for a remote desktop connection application

**remote desktop connection application**

This topic describes how a remote desktop connection application logs on to a host by using menus.
1. Start the remote desktop connection application and enter the `IP address and port number`

```
63389 of the O&M audit system .
```

2. Click **Connect**. The **Are you sure that you want to continue to connect this**
**computer?** dialog box appears.
3. Click **Connect**. In the logon window of the O&M audit system, enter the username and
password for logging on to the O&M audit system.
4. Click **Login**. On the asset management page that appears, select an authorized asset or
search for the host information in the search box.
5. After you double-click the host, you can enter the page on which you can perform O&M
operations on the host.
