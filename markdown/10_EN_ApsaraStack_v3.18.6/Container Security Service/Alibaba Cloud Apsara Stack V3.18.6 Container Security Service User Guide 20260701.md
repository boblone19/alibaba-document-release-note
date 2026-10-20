---
title: "Container Security Service User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 69
source_pdf: "844e6ae3e27d7594_Alibaba Cloud Apsara Stack V3.18.6 Container Security Service User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Security%20Service%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Container Security Service User Guide 20260701

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Container Protection
  - 3.1 Asset center
    - 3.1.1 Manage containers
    - 3.1.2 Container network topology
    - 3.1.3 Manage images
  - 3.2 CI/CD security
    - 3.2.1 Scan container images
    - 3.2.2 Scanner integration
  - 3.3 Runtime protection
    - 3.3.1 Vulnerability management
    - 3.3.2 Check baseline risks
    - 3.3.3 Manage intrusion alerts
    - 3.3.4 Container firewall
      - 3.3.4.1 Create a network object
      - 3.3.4.2 Create a defense rule
      - 3.3.4.3 Manage the defense status and defense rules of a cluster
      - 3.3.4.4 View protection status
    - 3.3.5 Container file protection
    - 3.3.6 Use proactive defense for containers
    - 3.3.7 Create and enable a container signature security policy
  - 3.4 Log retrieval
  - 3.5 Configure protection settings
- 4 Apsara Stack Security configurations
  - 4.1 Log on to the Apsara Uni-manager Management Console
  - 4.2 规则运营
    - 4.2.1 Create and manage IPS rules
    - 4.2.2 Manage Anti-DDoS Service rules
    - 4.2.3 Manage Server Guard rules
    - 4.2.4 Create and manage WAF rules
  - 4.3 Configure alert settings
  - 4.4 全局设置
    - 4.4.1 Configure the attack blocking feature
  - 4.5 账号管理
    - 4.5.1 Manage Apsara Stack tenant accounts
    - 4.5.2 Manage Alibaba Cloud accounts
  - 4.6 Migration to Apsara Uni-manager Operations Console
    - 4.6.1 Log on to Cloud Shield Operations Center
    - 4.6.2 View system monitoring data
    - 4.6.3 Global settings
      - 4.6.3.1 Configure host security rules
      - 4.6.3.2 Configure whitelist settings
    - 4.6.4 Upgrade center
      - 4.6.4.1 Upgrade center overview
      - 4.6.4.2 Feature library or version updates

## 1 Usage notes

Before you log on to Apsara Stack Security Center, make sure that your computer meets the configuration requirements. For more information, see the Configuration requirements table of this topic. Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Quick start

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles in Apsara Stack Security Center are provided by default. You cannot create custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see Default roles in Apsara Stack Security. Table 1. Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| Organization security administrator | Uses SOC to manage the security of hosts, applications, and networks for an organization. This role also manages security products related to Elastic Compute Service (ECS). |
| Global organization security administrator | Uses SOC to conduct security management for Apsara Stack and all tenants, and manages security products related to ECS. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

## 3 Container Protection

### 3.1 Asset center

#### 3.1.1 Manage containers

The container management feature allows you to synchronize assets and connect selfmanaged clusters. It also allows you to view and manage namespaces, nodes, applications, pods, and containers in your assets. This topic describes how to manage containers.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Container Management**.
4. On the **Container Management** page, synchronize assets or connect self-managed
clusters. Click **Synchronize Assets** to synchronize the assets.

> **Note:** The asset synchronization results take effect once every half an hour. Do not frequently click the button.

Click **On-premises cluster access**. In the **Manage a on-premises cluster cluster** panel, click **On-premises cluster access**. Specify the parameters on the **Mirror-**
**hosted cluster access** or **Custom Image Repository Cluster Integration** tab.
5. On the **Container Management** page, find the cluster that you want to manage and click
its name in the **Cluster Information** column or click **View** in the **Actions** column to go to the details page of the cluster. On the page that appears, you can click**Namespaces**, **Worker**, **Apply**, **Pod**, **Container**, or **Runtime mirroring** to go to the details page of specific assets to view asset details or manage assets. The following table describes the assets and related operations.

| Asset | Operation |
|---|---|

| Namespace s | Find the namespace that you want to view and click its name or clickH andle in the Actions column. On the details page of the namespace, view the vulnerabilities, alerts, and pods. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. Find the vulnerability that you want to manage and clickV iew in the Actions column to view the vulnerability details and pending vulnerabilities. Click the CVE ID to view the vulnerability details and fixing suggestions. You cani gnore the vulnerability. You can also fix the vulnerability on an asset and click Verify to check whether the vulnerability is fixed. Find the alert that you want to manage and clickH andle in the Actions column. In the dialog box that appears, select Handled manually, Ignore, or Add to Whitelist. Batch processing is supported. |
|---|---|
| Worker | Find the node that you want to manage and click its name or clickH andle in the Actions column. On the details page of the node, view the vulnerabilities, alerts, and baseline check results. Click the Vulnerabilities, Alerts, and Baseline Risks tabs to handle vulnerabilities and risks. |
| Apply | Find the application that you want to manage and click its name or clickH andle in the Actions column. On the details page of the application, view the vulnerabilities, alerts, and pods. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. |
| Pod | Find the pod that you want to manage and click its name or clickH andle in the Actions column. On the details page of the pod, view the vulnerabilities, alerts, and containers. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. |

| Container | Find the container that you want to manage and click its name or clickH andle in the Actions column. On the details page of the container, you can perform the following operations: On the Vulnerability and Alerts tabs: view and handle vulnerabilities and alerts. On the Asset Investigation tab: View the asset fingerprints of a server: Log in to the Server Guard console. In the left-side navigation pane, choose Asset > Server Fingerprints. In the upper-right corner of the Server Fingerprints page, click Settings to configure the automatic collection cycle. The system periodically displays the collected data on the page based on the configured policy. Manually collect the latest fingerprint data of a single asset: On the details page of an asset, click Collect data now in the upper-right corner to collect the latest fingerprint data of the asset with one click. Note It takes about 1 to 5 minutes to collect data. Please wait. For more information, see Appendix: Supported asset fingerprint objects and collected data. |
|---|---|
| Runtime mirroring | View the runtime image vulnerabilities, including the image system vulnerability, image application vulnerabilities, image baseline check, and malicious image sample list. Find the vulnerability that you want to manage and click View in the Actions column to view and handle the vulnerability. Find the baseline risk or malicious image sample that you want to view, and click Details in the Actions column to view the risk or malicious image sample and the related container. |

**Appendix: Supported asset fingerprint objects and collected**

**data**

Asset fingerprints accurately identify the characteristics of IT resources. This helps you gain a comprehensive understanding of your asset status, quickly locate security vulnerabilities, and block intrusion threats at the earliest opportunity. You can configure the asset fingerprint feature to collect multiple asset fingerprints of your servers, including ports, software, processes, middleware, AI components, databases, web services, and websites. The following table describes the asset fingerprint investigation objects and collected data.

| Asset fingerprint object | Collected data |
|---|---|

| Port | The information about the external port of your server is collected, including the following items: Port Process: the server process that monitors the listener port. PID: the ID of the server process that monitors the listener port. IP: the IP address of the network interface controller (NIC) that is associated with the listener port. Latest Collection Time: the last time when Security Center collected the information about the listener port. |
|---|---|
| Software | The information about the software that is installed on your server is collected, including the following items: Software Name: the name of the software. Version: the version of the software. Software startup path: the path from which the software is started. Software Update Time: the time when the software version is updated. Latest Collection Time: the last time when Security Center collected the information about the software. |
| Process | The information about the process that runs on your server is collected, including the following items: Process name: the name of the process. Process path: the path from which the process is started. Startup parameters: the startup parameters of the process. Start time: the time when the process was started. Running user: the user who started the process. Run permission: the permissions of the user who started the process. PID: the ID of the process. Parent Process Name: the name of the parent process to which the process belongs. SHA256/MD5: the fingerprint of the corresponding executable file of the process. Latest Collection Time: the last time when Security Center collected the process information from the server. |

| Middleware | The information about the middleware that runs on your server is collected. The middleware refers to system components that can independently run, such as MySQL databases and Docker. Docker is a container component. The collected information includes the following items: Middleware: the name of the middleware. Type: the type of the middleware. Version: The version of the middleware that runs on your server. Name: the name of the middleware. Runtime Environment Version: the version of the runtime environment on which the middleware depends. PID: the ID of the process that started the middleware. Installation Path: the directory where the main program of the middleware is installed. Version Verification: the method that is used to obtain the version of the middleware. Parent Process PID: the ID of the parent process that started the middleware. Enable User: the user who started the middleware. Process listening IP: the listener IP address of the started middleware. Listening Port: the listener port of the started middleware. Listener Status: the status of the listener for the middleware. Listening Port Protocol: the network protocol of the listener port for the middleware. Process Initiation Time: the time when the middleware was started. Cmdline: the command that is run when the middleware was started. Configuration Path: the absolute path of the startup configurations for the middleware. Web Directory: the root directory where the middleware that provides external services is located. Latest Collection Time: the last time when Security Center collected the middleware information from the server. |
|---|---|

| AI component | The information about AI components on your server is collected, including the following items: AI components: the name of the AI component. Type: the type of the AI component. Runtime Environment Version: the version of the runtime environment on which the AI component depends. Version: the version of the AI component. PID: the ID of the process that started the AI component. Installation Path: the absolute path of the main program or deployment directory of the AI component. Version Verification: the method that is used to obtain the version of the AI component. Parent Process PID: the ID of the parent process that started the AI component. Running user: the user who started the AI component. Process listening IP: the listener IP address of the started AI component. Listening Port: the listener port of the started AI component. Listener Status: the status of the listener for the AI component. Listening Port Protocol: the network protocol of the listener port for the AI component. start time: the time when the AI component was started. Cmdline: the command that is run when the AI component was started. Configuration Path: the absolute path of the startup configurations for the AI component. Latest Collection Time: the last time when Security Center collected the AI component information from the server. |
|---|---|

| Database | The information about the database that runs on your server is collected, including the following items: Database Name: the name of the database. Type: the type of the database. Version: the version of the database. PID: the ID of the process that started the database. Installation Path: the directory where the main program of the database is installed or the data directory of the database. Version Verification: the method that is used to obtain the version of the database. Parent Process PID: the ID of the parent process that started the database. Running user: the user who started the database. Process listening IP: the listener IP address of the started database. Listening Port: the listener port of the started database. Listener Status: the status of the listener for the database. Listening Port Protocol: the network protocol of the listener port for the database. start time: the time when the database was started. Cmdline: the command that is run when the database was started. Configuration Path: the absolute path of the startup configurations for the database. Latest Collection Time: the last time when Security Center collected the database information from the server. |
|---|---|

| Web service | The information about the web service of your server is collected, including the following items: Web Service Name: the name of the web service. Type: the type of the web service. Runtime Environment Version: the Java Development Kit (JDK) version. JDK is the runtime of the web service. Version: the version of the web service. PID: the ID of the process that started the web service. Installation Path: the path where the web service is installed. Version Verification: the method that is used to obtain the version of the web service. Parent Process PID: the ID of the parent process that started the web service. Running user: the user who started the web service. Process listening IP: the listener IP address of the started web service. Listening Port: the listener port of the started web service. Listener Status: the status of the listener for the web service. Listening Port Protocol: the network protocol of the listener port for the web service. start time: the time when the web service was started. Cmdline: the command that is run when the web service was started. Configuration Path: the absolute path of the startup configurations for the web service. Web Directory: the path of the web configuration page. Latest Collection Time: the last time when Security Center collected the web service information from the server. |
|---|---|
| Website | The information about the website on your server is collected, including the following items: Domain Name: the domain name of the website. Website Type: the type of the software that is used by the website. Port: the listener port of the website. Web Path: the path to the home directory of the website. Web Root Path: the path of the root directory in the web configuration. User: the user who started the website. Directory Permission: the permissions on the web directory. Monitoring Protocol: the listener protocol of the website. PID: the ID of the process. start time: the time when the website was started. Latest Collection Time: the last time when Security Center collected the website information from the server. |

#### 3.1.2 Container network topology

You can use a network topology to view container assets from the Internet and cluster perspectives. This topic describes how to view the network topology of containers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Container Network Topology**.
4. On the **Cluster Overview** page, click the **Internet Perspective** or **Cluster Perspective**
tab.
5. On the **Internet Perspective** or **Cluster Perspective** tab, perform the following
operations: Use the date picker to specify a time range within the last seven days to view the running details of clusters. Click the or icon to enable or disable the network topology for all clusters. Click the icon to refresh the network topology of clusters. Click the icon to export the snapshot for the network topology of clusters. Click a cluster in the network topology to view the cluster information, cluster risks, image information, and protection policies.

#### 3.1.3 Manage images

You can use the image management feature to synchronize assets and connect image repositories. You can also view and manage all images and at-risk images. This topic describes how to manage images.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Image Management**.
4. On the **Image management** page, synchronize assets or connect image repositories.
Click **Synchronize Assets** to synchronize assets.

> **Note:** The asset synchronization results take effect once every half an hour. Do not frequently click the button.

Click **Image warehouse access**. In the **Image warehouse access** panel, configure the parameters. For more information, see **Connect to a third-party image repository**.
5. On the **Image management** page, find the image repository that you want to manage and
click **View** in the **Actions** column. You can view information about an image in the following columns: **Mirror information**,
**Size**, **Latest Detection Time**, **Scan status**, **Scan progress**, and **Risk Status**.
6. Find the image on which risks are detected and click **Handle** in the **Actions** column.
On the page that appears, you can view the information about the image on the following tabs: **Image System Vul**, **Image Application Vul**, **Image Baseline Check**, **Mirror**
**Malicious Sample**, and **Mirror Fingerprint Survey**. You can also find the vulnerability
that you want to view and click its name or click **Details** in the **Operation** column to view the vulnerability details. 7.

### 3.2 CI/CD security

#### 3.2.1 Scan container images

Container Security Service (CSS) allows you to scan image repositories for image vulnerabilities, baseline risks, and malicious samples. This topic describes how to scan container images.

**Background information**

The feature of container image scan can detect and identify high-risk system vulnerabilities, application vulnerabilities, malicious samples, configuration risks, and sensitive data. Vulnerabilities may exist in the basic system software, middleware, web applications, and databases in your images. The vulnerabilities include mining programs and backdoor programs. Containers that run based on vulnerable images pose threats to your assets. The feature allows you to check whether image vulnerabilities and malicious samples exist in your vulnerable assets, and provides suggestions on vulnerability fixing. The feature provides endto-end vulnerability management capabilities and allows you to fix image vulnerabilities with ease.

**Scan images**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **CI/CD security > Image Scan**.

**Immediately scan images**

To immediately scan images, perform the following operations. You can scan only the container assets on which your account has permissions.
1. On the **Image Scan** page, click **Scan now**.
2. Configure settings in the One-Click Scan dialog box. By default, all types of images are
selected in the **One-Click Scan** dialog box. You can clear the types of images that you do not want to scan, configure the **Scan Time Range** parameter, and click **Confirm**.

**Configure a periodic image scan**

1. In the upper-right corner of the **Image Scan** page, click **Scan Settings**. The **Scan**
**Settings** panel appears.
2. On the Scan Configurations tab, configure the **Scan cycle** and **Scan Time Range**
parameters.
3. On the **Image repository** tab, view the list of image repositories that can be scanned. The
list displays image repositories of the **acr** and **defaultAcr** types, and connected private image repositories of the **harbor** and **quay** types. If the private image repositories that you want to scan are not displayed on the Image repository tab, click **Image warehouse access** to connect the private image repositories that you require.
4. On the **Baseline Configuration Management** tab, click **Manage** on the right side of
**Configuration Scope**. In the Baseline check scope panel, select the baselines that you
want to check and click **OK**.
5. Click the close icon in the upper-right corner of the **Scan Settings** panel to close the panel.
After you complete the scan settings, the system scans your images based on the settings.

**View scan results**

1. In the left-side navigation pane, choose **CI/CD security > Image Scan**.
2. On the **Image System Vul** or **Image Application Vul** tab, find the vulnerability that you
want to view and click its name or click **View** in the **Operation** column. You can view the details of the vulnerability and the affected images.
3. On the **Image Baseline Check** tab, find the baseline that you want to view and click
**Details** in the **Operation** column. You can view the information about the baseline in the
**Image/Version** and **Check Details/Total Check Items** columns. You can also click
**Details** in the **Operation** column to view the status of a risk, and click **Whitelist** or
**Remove** to add the risk to or remove the risk from the whitelist.
4. On the **Mirror Malicious Sample** tab, find the malicious sample that you want to view and
click its name or click **Details** in the **Operation** column. In the panel that appears, you can view the details of the malicious sample and the affected images.

#### 3.2.2 Scanner integration

The scanner integration feature can detect image risks in the project building stage and provide solutions to detected image risks. This topic describes how to configure the scan plug-in.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **CI/CD security > Scanner Integration**.
4. On the **Scanner Integration** page, click **Click to view documentation** to view the

**instructions for installing the CI/CD scan plug-in.**

5. Close the **Install CI/CD Plug-in** panel and click **Integration Configuration** to configure
parameters.

### 3.3 Runtime protection

#### 3.3.1 Vulnerability management

The vulnerability management feature of Container Security Service (CSS) is provided by Server Guard to help you handle vulnerabilities in containers in an efficient manner. This topic describes how to scan for and handle vulnerabilities in containers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Vulnerabilities**.
4. In the upper-right corner of the **Vulnerabilities** page, click **Settings** to navigate to the
Server Guard console. In the left-side navigation pane, choose **Security Prevention** >
**Vulnerabilities**. In the upper-right corner, click **Settings**. In the panel that appears,
configure the types of vulnerabilities that you want to detect, and parameters including Vulnerability Scan Level and Vulnerability Whitelist.
5. On the **Vulnerabilities** page, view information including the node vulnerabilities and the
time when a system vulnerability was last detected.
6. Click **Scan Now** to start a vulnerability scan task.

> **Note:** The scan task requires 1 to 5 minutes to complete. Wait until the scan task is complete. You can refresh the page to view the most recent statistics.

After the scan task is complete, you can view and handle the detected vulnerabilities.
7. On the **Vulnerabilities** page, click the **Linux Software**or**Application(Urgent**
**Vulnerability Included)** tab.
i. Click a security bulletin or click **View** in the **Actions** column of a security bulletin. In the panel that appears, perform the following operations: Click **Globally Add to White** in the upper-right corner to add the security bulletin to the whitelist for all affected assets.

> **Note:** After you add the security bulletin to the whitelist, the security bulletin is no longer marked as unhandled. The system no longer notifies you of the security bulletin.
> This operation affects all assets. If you want to manage the applicable scope of the whitelist, go to the Settings panel.
> If you want to remove the security bulletin from the whitelist or change the reason for adding the security bulletin to the whitelist, go to the Settings panel.

Click the **Detail** tab and click a CVE ID to view the details of the vulnerability. Click the **Pending vulnerability** tab and click **Verify** in the **Actions** column of a vulnerability. You can also select multiple vulnerabilities and click **Verify** below the vulnerability list to verify the vulnerabilities at a time. Click the **Pending vulnerability** tab and click **Ignore** in the **Actions** column of a vulnerability. You can also select multiple vulnerabilities and click **Ignore** below the vulnerability list to ignore the vulnerabilities at a time. ii. Return to the Vulnerabilities page. Select multiple vulnerabilities and click **Add to**
**Whitelist** to add the vulnerabilities to the whitelist at a time.
iii. In the upper-right corner of the vulnerability list, click the icon to download vulnerabilities as a file.

#### 3.3.2 Check baseline risks

The baseline check feature can help you identify baseline risks in an efficient manner. This topic describes how to check and handle baseline risks.

**Configure a baseline check policy**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Baseline Check**.
4. In the upper-right corner of the **Baseline Check** page, click **Manage Policies**. In the
Manage Policies panel, click **Add standard policy** or click **Edit** in the **Actions** column of an existing standard policy. In the panel that appears, configure the parameters and click
**OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. After a policy is created, you cannot modify the name of the policy. |
| Schedule | The check interval. Valid values: Every Day, Every 3 Days, Every 7 Days, and Every 30 Days. |
| Detection time | The check period. Valid values: 0:00 - 6:00, 6:00 - 12:00, 12:00 - 18:00, and 18:00 - 24:00. |
| Check Items | The name of the baseline. Valid values include but are not limited to: Kubernetes (ACK) Master Internationally Agreed Best Practices for Security Kubernetes (ACK) Node Internationally Agreed Best Practices for Security Alibaba Cloud Standard - Kubernetes-Master security baseline check Alibaba Cloud Standard - Kubernetes-Node security baseline check |
| Effective Cluster | The clusters to which you want to apply the baseline check policy. |

5. Go back to the **Baseline Check** page, select a created policy from the **Select Policy** drop-
down list and click **Check Now**. After the baseline check is complete, you can view and verify baseline risks in the baseline list.
6. Find the baseline that you want to manage and click its name. In the panel that appears,
perform the following operations: Move the pointer over an asset name to view the details of the affected asset. You can select one or multiple baseline issues for verification.

**View and manage risks**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Baseline Check**.
4. On the Baseline Check page, click the **Risk situation** tab to view the risks of baseline
checks. You can search for risks by risk level, status, baseline type, and check item.
5. Find the risk item that you want to view and click **Details** in the **Actions** column to view
the **Details** and **Process** sections. The Details section lists the Description, Suggestion, and Related Baseline information. You can handle the risk by clicking **Whitelist**, **Verify**, or
**Cancel White**.
6. To add a risk item to the whitelist, find the risk item and click **Whitelist** in the **Operate**
column. To add multiple risk items to the whitelist at a time, select the risk items that you want to manage and click **Whitelist** below the risk list.

#### 3.3.3 Manage intrusion alerts

Container Security Service (CSS) allows you to monitor nodes and containers in clusters. You can monitor and block risks such as trojans, intrusions, supply chain attacks, and container escapes that are caused by privilege escalation. This topic describes how to configure the intrusion alert feature.

**Background information**

The intrusion alert feature is developed based on the big data alerting model that is provided by Alibaba Cloud. The threat detection module of Server Guard provides comprehensive intrusion detection capabilities that can inform you of risks in Container Service for Kubernetes (ACK) and block external risks in an efficient manner.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Intrusion Alerts**.
4. On the **Intrusion Alerts** page, view the numbers of at-risk nodes, at-risk containers, all
risk items, and high-risk items. You can specify filter conditions to view information about an alert such as the severity, event, and affected assets. You can move the pointer over the name of an affected asset to view the details of the affected asset.
5. Click **Handle** in the **Actions** column of the alert that you want to manage.
You can perform the following operations on the alert: **Add to Whitelist**, **Ignore**, **Handled**
**manually**, **Stop container**, and **Batch handled**.
6. On the **Intrusion Alerts** page, click the name of an alert or click **Details** in the **Actions**
column of the alert. You can view the details of the alert and its associated exceptions.
7. Click the
icon to export and view all information about the alerts in a list.

#### 3.3.4 Container firewall

The container firewall feature helps you protect container assets from attacks. This topic describes how to configure the container firewall feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. Click the **Protection status** tab to view the number of risks in the last 24 hours, the
number of risks in the last 30 days, the number of risks in the last 180 days, the numbers of unprotected clusters and total clusters, and the total number of rules. You can view the alerts generated by the container firewall feature in the alert list. Find an alert and click **Details** in the **Operation** column to view the details of the alert.
5. Click the **Protection management** tab, find an unprotected cluster and create a
protection rule, and then enable the rule. Configure a protection rule a. Click **Rule management** in the **Actions** column. In the Defense rules panel, click
**Create defense rules**.
b. In the **Create rules** panel, configure parameters. In the **Source configuration** step, configure the **Rule name** and **Network object** parameters. In the **Purpose configuration** step, configure the **Network object**, **Port**, **Action**,
**Rule status**, and **Priority** parameters.
c. In the Defense rules panel, find a rule and click the icon in the **Enabled status** column, or select multiple rules and click **Batch open** below the rule list. Enable protection In the cluster list, find a cluster and click the icon in the **Defensive status** column, or select multiple clusters and click **Batch open** below the cluster list. Restore the interceptable status to normal In the cluster list, find a cluster and click **Recovery** in the **Interceptible status** column.
6. On the **Network object** tab, click **Add Network Object**. In the **Add Object** panel,
configure the **Object name**, **Object type**, **Namespaces**, and **Image** parameters, and click **OK**. Valid values of Object type are Container, IP, and Domain Name.

> **Note:** Fuzzy match by suffix is supported for **Namespaces** and **Image**. Example: abc*.

After you create a network object, you can add the network object to a protection rule.

##### 3.3.4.1 Create a network object

To use the container firewall feature of Container Security Service (CSS), you must create a source network object and a destination network object and then create defense rules. This topic describes how to create a network object.

**Prerequisites**

The malicious behavior defense feature is enabled for your assets.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. On the **Container Firewall** page, click the **Network object** tab.
5. On the **Network object** tab, click **Add Network Object**.
6. In the **Add Object** panel, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Object name | The name of the network object. |
| Object type | The type of the network object. Valid values: Container IP Domain Name |
| Namespace | The namespace to which the network object belongs. Note You can enter the namespace of a cluster. Fuzzy match by suffix is supported. Example: a*. |
| Application name | The name of the application to which the network object belongs. Note You can enter the tag value of a pod whose tag key is app. Fuzzy match by suffix is supported. Example: abc*. |
| Image | The image of the network object. Note You can enter the image of a cluster. Fuzzy match by suffix is supported. Example: a*. |
| Tag | The tag of the pod. You can select one or more tags. A tag is the business attribute that is attached to the containers in a Kubernetes cluster after the containers are started. You can add custom tags to identify pods. Tags are the basic match conditions in defense rules. Note You can enter the tag of a cluster. Fuzzy match by suffix is supported. Example: a*. |

7. Click OK.
The created network object is displayed on the Network object tab. You can click **Edit** or **Delete** in the **Actions** column of the network object to modify or delete it. You can also select multiple network objects and click **Batch delete** below the network object list to delete the network objects at a time.

> **Note:** You can delete a network object only if the network object is not added to a defense rule.

**What to do next**

After you create a source network object and a destination network object, you can create a defense rule to allow, block, or generate alerts for unusual traffic from the source network object to the destination network object.

##### 3.3.4.2 Create a defense rule

You can create a defense rule to control traffic from a source network object to a destination network object. This topic describes how to create a defense rule.

**Prerequisites**

A source network object and a destination network object are created. For more information, see Create a network object.

**Background information**

A defense rule that is created in the container firewall module is used to implement network isolation. A defense rule consists of a source network object, a destination network object, one or more port ranges, an action, and a priority.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. On the **Container Firewall** page, click the **Protection management** tab.
5. In the cluster list of the **Protection management** tab, find the cluster for which you want
to create a defense rule and click **Rule Management** in the **Actions** column.
6. In the **Defense rules** panel, click **Create defense rules**.
7. In the **Create rules** panel, create a defense rule for the cluster.
i. **Source configuration** You need to configure the following parameters:
**Rule name**: the name of the defense rule.
**Network object**: the source network object.
ii. Click **Next**. iii. **Destination configuration** You need to configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Network object | The destination network object. |
| Port | The destination port range of traffic. Note You can specify at most eight port ranges. Each port range must be unique. Separate multiple port ranges with commas (,). Example: 20/30,80/90. |
| Action | The action on traffic. Valid values: Intercept: blocks traffic. Alert: allows traffic and generates alerts. Release: allows traffic and does not generate alerts. |
| Rule status | The status of the defense rule. Valid values: Open: The rule is enabled after it is created. Close: The rule is disabled after it is created. |
| Priority | The priority of the defense rule. Valid values: 1 to 1000. A smaller value indicates a higher priority. |

8. Click **Determine**.
The defense rules that you create are displayed in the defense rule list in descending order based on priority. By default, a newly created defense rule is disabled. You must enable the defense rule to allow the rule to take effect. For more information about how to enable a defense rule, see Manage the defense status and defense rules of a cluster. After you enable the defense rules of a cluster, the rules are applied in sequence based on the priorities that you specify.

> **Important:** If traffic from the source network object does not hit the first defense rule, the subsequent rules are used. When a rule is hit, the rule processes the traffic based on the action that you specify in the rule. If no defense rules are hit, the container firewall feature allows the traffic.

##### 3.3.4.3 Manage the defense status and defense rules of a cluster

**rules of a cluster**

After you create defense rules for a cluster, you can enable or disable defense for the cluster. You can also enable, disable, and modify the defense rules of the cluster. If you no longer need a defense rule, you can delete it. This topic describes how to enable, disable, modify, and delete a defense rule.

**Prerequisites**

A defense rule is created for your cluster. For more information, see Create a defense rule.

**Background information**

The defense rule that is created for the cluster can take effect only when the interceptable status of the cluster is normal. If the interceptable status is abnormal, you must troubleshoot the issue at the earliest opportunity.

**Manage defense status**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. On the **Container Firewall** page, click the Protection management tab.
5. In the cluster list of the **Protection management** tab, find the cluster for which you want
to manage the defense status. Click the or icon in the **Defensive status** column to enable or disable defense for the cluster. You can also select multiple clusters and click **Batch open** or **Batch**
**shutdown** below the cluster list to manage the defense status for multiple clusters at a
time.

> **Important:** You can enable defense rules for a cluster only when **Normal** is displayed in the **Interceptable status** column of the cluster. If **Exception** or **Normal to Be** **Confirmed** is displayed in the **Interceptable status** column, you cannot enable defense rules for the cluster.

**Manage defense rules**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. On the **Container Firewall** page, click the Protection management tab.
5. In the cluster list of the **Protection management** tab, find the cluster for which you want
to manage defense rules. i. Click **Rule management** in the **Actions** column to go to the **Defense rules** panel. ii. In the defense rule list of the **Defense rules** panel, you can perform the following operations on the defense rules: Enable or disable one or more defense rules Click the or icon in the **Enabled status** column of a defense rule to enable or disable the defense rule. You can also select multiple defense rules and click **Batch open** or **Batch shutdown** below the rule list to enable or disable the defense rules at a time. View the details of a defense rule Find the rule that you want to view and click **Details** in the **Operation** column to go to the **Details** panel. In the Details panel, view the configurations of the source network object and destination network object, and other details of the defense rule. Modify a defense rule Find the rule that you want to modify and click **Edit** in the **Operation** column to go to the **Edit rules** panel. In the Edit rules panel, modify the defense rule.

> **Note:** The modifications to the defense rule take effect within 1 minute.

Delete one or more defense rules Find the rule that you want to delete and click **Delete** in the **Operation** column. In the message that appears, click OK to delete the rule. You can also select multiple defense rules and click **Batch delete** below the rule list to delete the defense rules at a time.

> **Note:** The delete operation takes effect within 1 minute.

##### 3.3.4.4 View protection status

After you create and enable a defense rule for a cluster, the defense rule allows, blocks, or generates alerts for the traffic destined for the cluster. You can view the alerts that are generated by the defense rule on the Protection status tab of the Container Firewall page. This topic describes how to view protection details on the Protection status tab.

**Background information**

The Protection status tab displays only the alerts generated by defense rules whose action is set to Intercept or Alert. If the action of a defense rule is set to Release, the defense rule does not generate alerts.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Firewall**.
4. On the **Container Firewall** page, click the **Protection status** tab.
5. On the **Protection status** tab, view the protection status of the container firewall.
The Protection status tab displays defense statistics and the alert list. Defense statistics You can view the defense statistics in the following sections: **Number of risks in the**
**last 24 hours**, **Number of risks in the last 30 days** , **Number of risks in the last**
**180 days**, **Unprotected clusters/total clusters**, and **Total number of rules**.
Alert list You can view the alerts that are sorted by generation time in reverse chronological order. All the alerts are generated by the defense rules whose action is set to Alert or Intercept. If alerts are generated for the same source pod, destination pod, port number, and cluster on the same calendar day, the number of alerts is calculated as 1, and the number of times of access attempts is displayed in the **Number of attempts** column. You can click **Edit Rule** in the Actions column of an alert to modify the defense rule that generated the alert. You can also click the icon next to **Edit Rule** to modify the action of the defense rule that generated the alert.

> **Note:** The modifications to the defense rule take effect within 1 minute.

#### 3.3.5 Container file protection

The container file protection feature can monitor directories and files in containers in real time, and generate alerts or intercept tampering operations when the directories or files are tampered with. This prevents your applications from being inserted with illegal information or malicious code and ensures the security of the container environment.

**Create a rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container File**
**Protection**.
4. On the **Container File Protection** page, click **New rule**.
5. In the **New rule** panel, configure the parameters and click **Next**.

| Parameter |   | Description | Example |
|---|---|---|---|
| Rule Name |   | Enter a name for the rule. The name must be 6 to 50 characters in length and can contain letters, digits, underscores ( ), _ and hyphens (-). It must start with a letter. | Cluster01 |
|   | Protected File Directory | Enter the directory that you want to protect. When you configure this parameter, take note of the following items: The directory must start with a forward slash (/). You can enter only one directory. The length of a directory must be less than 500 characters. You can enter only one directory each time. To protect multiple directories, click Add in the Actions column. You can specify up to 10 directories in a rule. | /home/app/label |

| Rule Configur ation |   |   |   |
|---|---|---|---|
|   | Whitelist | Enter the processes that are allowed to modify the protected directory. If a process is added to the whitelist, no alert is generated and the process is not blocked when the process modifies files. When you configure this parameter, take note of the following items: You can enter only the processes that run in your container. The length of a process cannot exceed 50 characters. You must separate multiple processes with semicolons (;). You can add up to 10 processes to the whitelist of a directory. | /bin/cp;/usr/bin/mv;/bi n/vi |
|   | Action | Select the action that you want the system to perform when a tampering operation is detected. Valid values: Alert: When the system detects tampering operations on files in the directory, the system only generates alerts. Block: When the system detects tampering operations on files in the directory, the system generates alerts and blocks the tampering processes. Note We recommend that you set the Action parameter to Alert. After you confirm that no false alerts are generated, change the Action parameter to Block. This prevents normal processes from being blocked. If a blocked process is required in your workloads, you can add the process to the whitelist. | Alert |

6. Select the cluster on which you want the rule to take effect in the Cluster Name column,
select a pod label in the Pod Tag column, and then click **Determine**. We recommend that you select a pod label that starts with `app` . In Kubernetes, labels are key-value pairs and are used to label and classify Kubernetes resources, such as pods, Deployments, and services. You can add custom labels to Kubernetes resources based on scenarios, features, or purposes to better manage the resources. Labels that start with `app` are used to organize resources by application. If no labels are displayed in the drop-down list, you must enter a label. If you want the rule to take effect on multiple clusters or multiple pod labels in a cluster, you can click **Add** in the Actions column to specify multiple clusters or pod labels.

**Manage the rule**

After you create a rule, you can perform the following operations on the **Container File**
**Protection** page:
Copy the rule Click **Copy** in the **Actions** column to copy the rule. Enable or disable the rule Click the switch in the **Enable** column to enable or disable the rue. Edit the rule Click **Edit** in the **Actions** column to modify the name, configurations, and scope of the rule. Delete the rule

> **Important:** The deleted rule cannot be restored. Before you delete a rule, make sure that you no longer require the rule.

Click **Delete** in the **Actions** column. In the message that appears, click **OK** to delete the rule.

#### 3.3.6 Use proactive defense for containers

The feature of proactive defense for containers proactively detects risks when your containers start or run from the following dimensions: image security, runtime security, and running environment security. You can configure rules to block the running of at-risk images, stop untrusted processes, and block container escapes. This helps improve the runtime security of your containers. This topic describes how to configure rules of the at-risk image blocking, drift prevention, and container escape prevention types.

**Rule description**

The following table describes the rule types that you can select based on your business requirements.

| Rule type | Rule description |
|---|---|
| At-risk Image Blocking | After you create a rule of the At-risk Image Blocking type, Container Security Service (CSS) detects risks on images based on the rule when you use the images to create resources in the clusters that are specified in the rule. If an image hits the rule, CSS performs the action that is specified in the rule on the image, and generates an alert for the risk detection result. The action can be Block or Alert. This ensures that only images that meet your security requirements can be started in your clusters. |
| Drift Prevention | After you create a rule of the Drift Prevention type, CSS detects and blocks the startup of programs that are not included in the images of specified clusters in the rule. This helps defend against malicious software intrusion and known and unknown attacks. |
| Container Escape Prevention | After you create a rule of the Container Escape Prevention type, CSS detects risky operations from multiple dimensions, such as processes, files, and system calls, and establishes protection barriers between containers and hosts. This helps block escape behaviors and ensure the runtime security of containers in an efficient manner. You can also use this type of rule to block attacks that are launched by exploiting container vulnerabilities to take control over hosts. This helps improve the security of server systems. |

**Use a rule of the At-risk Image Blocking type**

**Manage system rules**

After you create a rule of the At-risk Image Blocking type for a cluster, a request is sent to CSS to detect image risks when you use an image specified in the rule to create resources such as pods in the cluster. CSS checks whether the image contains risks that you select in the rule. If the image hits the rule,CSS performs the action that is specified in the rule on the image, and generates a security event for the risk detection result. The action can be Alert or Block. If multiple rules are created for a cluster, all rules take effect. If an image hits multiple rules, CSS handles the image based on the actions that are specified in the rules, and generates multiple alerts. If multiple policies are configured in a rule and a policy is hit, CSS immediately handles the risks based on the action that is specified in the rule. CSS no longer matches the image against other policies. The matching sequence of policies in the rule is: whitelist > blacklist > others (to be more specific, malicious samples > unscanned images > baselines > vulnerabilities).

**Create a custom rule**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers**. On the page that appears, select **At-risk Image Blocking** from the Rule type
section and click **New rule**.

> **Note:** If you created a rule for a cluster, find the rule and click **Copy** in the **Operation** column. In the **Copy Rule** panel, you can modify the parameters of the rule based on your business requirements and click **OK**.

4. In the New rule panel, configure the parameters in the Add rule step and click **Next**. The
following table describes the parameters.

| Paramet er | Description |
|---|---|

|   | Rule Name | Select a rule template from the drop-down list and enter a name for the rule. You can select Blank template to create a rule based on your business requirements. You can also select an existing template with preconfigured risk detection settings. |   |   |
|---|---|---|---|---|
|   | Rule descripti on | Enter a description for the rule. |   |   |
|   | Rule Configur ation | Select the types of risks that CSS detects on an image. If you select the check box next to a type of risks, CSS detects the risks. If you clear the check box, CSS does not detect the risks. The following list describes five supported types of risks: Unscanned Image: If you do not scan images, risks can occur after the images are released in a cluster. We recommend that you scan images for risks. Important If you select this type of risk, we recommend that you set Action to Alert. If you have high requirements for security management, you can change the action to Block. Before you change the action, we recommend that you observe the alert events that are generated based on the existing settings for a period of time and check whether your business is affected. If your business is not affected, you can change the action of the rule. Baseline: If you select this type of risk, CSS checks the container images against the predefined standard security configurations and best practices. Vulnerability: If you select this type of risk, CSS detects the vulnerabilities that may cause security risks to container environments, and detects the application- related vulnerabilities in images. Malicious Sample: If you select this type of risk, CSS detects the malicious files, code, and behaviors that may exist in container images and container runtime. Custom Blacklist Mirror: If you select this type of risk, you can specify up to 20 images to be added to the blacklist. Fuzzy match is supported by using keywords. For example, if you want to add the image whose address is yundun-example-registry.cn- hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords for fuzzy match: yun-repo , test , yun-repo:test , and repo:test . |   |   |
|   |   |   | yundun-example-registry.cn- |   |
|   |   | hangzhou.aliyuncs.com/yundun-example/yun-repo:test |   |   |
|   | Action | Specify the action to be performed for an enabled rule. You can configure the action as Alert or Block. Alert: If an image is started and hits the rule, an alert event whose Action is Alert is generated. Block: If an image is being started and hits the rule, the image is blocked, and an alert event whose Action is Block is generated. |   |   |

|   |   | Click Create Rule and enter the tag of the image that you want to add to the whitelist. You can specify up to 20 images to be added to the whitelist. After you add an image to the whitelist, CSS no longer detects risks on the image when the image is started. Fuzzy match is supported by using keywords. For example, if you want to add the image whose address is yundun-example-registry.cn- hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords for fuzzy match: yun-repo , test , yun- repo:test , and repo:test . |   |   |
|---|---|---|---|---|
|   |   |   | yundun-example-registry.cn- |   |
|   | Add to Whitelist | hangzhou.aliyuncs.com/yundun-example/yun-repo:test |   |   |

| yun- |   |
|---|---|

|   | repo:test |
|---|---|

5. Configure the protection scope and click **OK**.
Click the **Cluster**, **Image**, or **Tag** tab to select the assets that you want to protect.

**View generated alerts**

After you create and enable a rule of the At-risk Image Blocking type, you can perform the following operations to view the alerts that are generated based on the rule: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose Security > Container Security Service. In the left-side navigation pane, choose Runtime Detection > Intrusion Alerts. On the **Intrusion Alerts**page, select**Risk Image Blocking** from the Alert Type drop-down list. The alerts that are generated based on the at-risk image blocking feature are divided into the following types based on the value of the Defense Action parameter in the rule: If the Defense Action parameter is set to **Alert** in the rule, an alert in the **Pending** state is generated when the rule is triggered. We recommend that you handle the alert at the earliest opportunity. For more information, see Manage intrusion alerts. If the Defense Action parameter is set to **Block** in the rule, an alert in the **Target process**
**does not exist** or **End process successful** state is generated when the rule is triggered.
CSS automatically handles the alerts of this type, and you can view them in the handled alert list. The following list describes the Target process does not exist state and the End process successful state:
**Target process does not exist** : The process is complete. You do not need to handle
the alert in this state.
**End process successful**: CSS blocks the process. You do not need to handle the alert in
this state.

**Use a rule of the Drift Prevention type**

**Manage system rules**

By default, CSS provides the system rule for non-image program defense. The system rule is automatically enabled for users who do not configure custom rules for non-image program defense. The system rule generates alerts for the startups of non-image programs in all clusters that are connected to CSS. You can perform the following operations to view the system rule for non-image program defense: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose Security > Container Security Service. In the leftside navigation pane, choose Runtime Detection > **Proactive Defense for Containers**. On the Proactive Defense for Containers page, select **Drift Prevention** in the Rule type section and view the system rule on the **System Rule** tab. The action that is specified in the system rule is Alert. When the startup of a non-image program is detected, the system generates an alert and does not block the startup of the non-image program. You can enable or disable a system rule and modify the clusters to which the system rule applies. If the clusters are changed or new clusters are added, the system automatically adds the new clusters to the protection scope. If you use the non-image program defense feature for the first time, we recommend that you check whether false positive alerts are generated by the system rule. You cannot configure whitelists in the system rules or block the risky behaviors detected by the system rules. If you want to configure a whitelist or block a risky behavior, you can create a custom rule. After you create a custom rule, the system rule is automatically disabled and cannot be re-enabled. If you want to enable the system rule, you must delete all custom rules.

**Create a custom rule**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers**.
4. In the **Rule type** section of the Proactive Defense for Containers page, click **Drift**
**Prevention**.
5. Click the Custom Rule tab. On the **Custom Rule** tab, click **New rule**.
6. In the **New rule** panel, configure the parameters in the Add rule step and click **Next**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the rule. |
| Rule description | Enter a description for the rule. |
| Status | Turn on or turn off the switch for the rule. Valid values: On: If you turn on the switch, the rule is enabled after it is created and is automatically applied to protect the clusters within the protection scope. Off: If you turn off the switch, the rule is disabled and does not take effect after it is created. |

| Defense Action | Specify the action that is performed after the rule is triggered. Valid values: Alert: If an untrusted process is detected, the system generates an alert. Intercept: If an untrusted process is detected, the system generates an alert and blocks the process. Note We recommend that you first set the Defense Action parameter to Alert. If no executable programs that are not included in container images are installed and started during the running of your container, change the value of the Defense Action parameter to Intercept. This helps prevent false positives. |
|---|---|
| Create File Directory Whitelist | Click Create Rule and enter the file directory that you want to add to the whitelist. Separate multiple directories with line breaks. Example: /user/name1 . |
| Create Image Whitelist | Click Create Rule and enter the image that you want to add to the whitelist. For example, if you want to add the image whose address is yundun-example- registry.cn-hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords: yun-repo test yun-repo:test repo:test |

7. In the Specify Protection Scope step, select the clusters to which you want to apply the rule
and click **Determine**. You can configure only one rule for a cluster. If a rule is already configured for a cluster, you cannot select the cluster in this step.

**View generated alerts**

After you create and enable a rule of the Drift Prevention type, you can perform the following operations to view the alerts that are generated based on the rule: Log in to the Apsara Unimanager Management Console. In the top navigation bar, choose Security > Container Security Service. In the left-side navigation pane, choose Runtime Detection > Intrusion Alerts. On the **Intrusion Alerts**page, select **Container Active Defense** from the Alert Type drop-down list. The alerts that are generated based on the rule of the Drift Prevention type are displayed. The alerts that are generated based on the non-image program defense feature are divided into the following types based on the value of the Defense Action parameter in the rule: If the Defense Action parameter is set to **Alert** in the rule, an alert in the **Pending** state is generated when the rule is triggered. We recommend that you handle the alert at the earliest opportunity. For more information, see Manage intrusion alerts. If the Defense Action parameter is set to **Intercept** in the rule, an alert in the **Target**
**process does not exist** or **End process successful** state is generated when the rule is
triggered. CSS automatically handles the alerts of this type, and you can view them in the handled alert list. The following list describes the Target process does not exist state and the End process successful state:
**Target process does not exist** : The process is complete. You do not need to handle
the alert in this state.
**End process successful**: CSS blocks the process. You do not need to handle the alert in
this state.

**Use a rule of the Container Escape Prevention type**

**Manage system rules**

CSS provides various rules of the container escape prevention type. By default, the rules are enabled for all clusters that are connected to CSS. The rules are referred to as system rules. You can perform the following operations to view the details of system rules for container escape prevention: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose Security > Container Security Service. In the left-side navigation pane, choose Runtime Detection > Proactive Defense for Containers. On the**Proactive Defense**
**for Containers**page, select **Container Escape Prevention** in the Rule type section. On
the System Rule tab, view information about system rules. The action that is specified in a system rule is Alert. When an escape behavior is detected, the system generates an alert and does not block the behavior. You can enable or disable a system rule and modify the clusters to which the system rule applies. If the clusters are changed or new clusters are added, the system automatically adds the new clusters to the protection scope. If you use the container escape prevention feature for the first time, we recommend that you check whether false positive alerts are generated by the system rules. If no false positive alert is generated, you can change the rule action that is specified in the rules to Block. You cannot configure whitelists in the system rules or block the risky behaviors detected by the system rules. If you want to configure a whitelist or block a risky behavior, you can create a custom rule. After you create a custom rule of a specific type, the system rule of the same type is automatically disabled.

**Create a custom rule**

CSS provides the same types of custom rules and system rules. You can configure whitelists and set Defense Action to Block for custom rules.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers**.
4. In the **Rule type** section of the Proactive Defense for Containers page, click **Container**
**Escape Prevention**.
5. Click the Custom Rule tab. On the **Custom Rule** tab, click **New rule**.
6. In the **New rule** panel, configure the parameters in the Add rule step and click **Next**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the rule. |
| Rule type | The type of the risk that you want the rule to prevent. Select a type from the drop-down list based on your business requirements. After you select a type, all check items that are supported for the type are selected. If you do not require specific check items, you can clear the check items. Valid values: Modify Host User Profile: This risk occurs when a container is mounted with system configuration files, such as /etc/passwd, or SSH service configuration directories at startup. This allows an attacker to modify the files within the container, thereby gaining user permissions on the host node. Escape to Host by Exploiting Vulnerabilities or Improper Configuration: This risk occurs when a container is started with escalated privileges or mounted with pseudo file systems. This allows an attacker to exploit system mechanisms such as core pattern and cgroup within the container to escape. _ High Risk System Call: This risk occurs when attackers exploit kernel vulnerabilities to escalate privileges or perform escape actions. Attackers use critical system calls to achieve these objectives. Escape to Host by Writing to Important Host File: This risk occurs when a container is started with scheduled start task directories mounted such as etc/crontab, init script directories such as /etc/init.d, trigger-based script directories such as /etc/profile, and Kubernetes static pod configuration directories. Attackers can write malicious code into these directories that can be automatically executed on the host, thereby gaining permissions. Run Container Escape Tool: Escape tools are running within a container. In most cases, after an attacker intrudes into a container, the attacker uses escape tools to break out of the container and bypass the isolation between the container and the host node, thereby gaining control over the host. |

| Defense Action | The action that is performed after the rule is triggered. Valid values: Alert: The system only generates alerts when it detects risks specified in the rule. Block: The system generates alerts and blocks the related processes or operations when it detects risks specified in the rule. Note A rule may be triggered in some normal business scenarios. When you configure a rule, we recommend that you set the Defense Action parameter to Alert and check whether false positive alerts are generated within a period of time. If no false positive alerts are generated, change the value of the Defense Action parameter to Block. |
|---|---|
| Add to Whitelist | Click Create Rule and enter the name of the image that you want to add to the whitelist. You can add up to 20 images to the whitelist. Fuzzy match is supported by using keywords. For example, if you want to add the image whose address is yundun-example-registry.cn- hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords: yun-repo test yun-repo:test repo:test Note After you add an image to the whitelist, the system does not detect escape behaviors on the image. Proceed with caution. |

After you complete this step, the rule is displayed in the rule list.
7. In the Specify Protection Scope step, select the clusters that you want to protect and click
**Determine**.

**View generated alerts**

After you create and enable a rule of the Container Escape Prevention type, you can perform the following operations to view the alerts that are generated based on the rule: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose Security > Container Security Service. In the left-side navigation pane, choose Runtime Detection > Intrusion Alerts. On the**Intrusion Alerts**page, select **Container Escape Prevention** from the Alert Type drop-down list. The alerts that are generated based on the rule of the container escape prevention type are displayed. The alerts that are generated based on the container escape prevention feature are divided into the following types based on the value of the Defense Action parameter in the rule: If the Defense Action parameter is set to **Alert** in a rule, an alert in the **Pending** state is generated when the rule is triggered. We recommend that you handle the alert at the earliest opportunity. For more information, see Manage intrusion alerts. If the Defense Action parameter is set to **Block** in a rule, an alert in the **Successful**
**Interception** state is generated when the rule is triggered. This indicates that CSS has
blocked container escapes. You do not need to handle the alerts.

#### 3.3.7 Create and enable a container signature security policy

**signature security policy**

The container signature feature signs trusted container images and verifies the signatures to ensure that only trusted images are deployed. This prevents unauthorized container images from being started and improves asset security.

**Prerequisites**

A key is created based on an **asymmetric encryption algorithm in Key Management**
**Service (KMS)**.

> **Important:** Only **asymmetric key algorithms** support the container signature feature. When you create a KMS key, set the **Key Specifications** parameter to RSA_2048 and the **Key** **Usage** parameter to SIGN/VERIFY.

A Container Service for Kubernetes (ACK) cluster is created and the `kritis-validation-` `hook` component is installed in the cluster.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container Signature**.
4. On the Container Signature page, click the **Witness** tab. On the Witness tab, click **Create a**
**witness**. In the Create a witness panel, configure the parameters and click **OK**.

> **Note:** If a witness already exists, you can skip this step and go to the next step to configure the policy.

| Parameter | Description |
|---|---|

| Witness | Enter an informative name for the witness, which allows you to quickly select the witness when you configure a security policy subsequently. |
|---|---|
| Select a certificate | Select the KMS key that you created from the certificate list. |
| Description | Enter a description for the witness. |

5. On the **Security Policy** tab, click **Add Policy**. In the Add Policy panel, configure the
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a name for the security policy. When you configure a security policy, you must select a witness to enable the container signature feature for the required cluster. We recommend that you enter an informative name. |
| Witness | Select the witness that you created from the witness list. |
| Application Cluster | Select the cluster group for which you want to enable the container signature feature. Then, select the required cluster namespace. |
| Policy Enabled | Turn on the switch. The policy is automatically enabled after it is created. Note By default, the policy is disabled. If the policy is disabled, it does not take effect. |
| Remarks | Enter a description for the security policy. |

After you create and enable a container signature security policy for a container image, you can view the container image labeled as a **trusted image** in the Container Registry console.

### 3.4 Log retrieval

The log retrieval feature allows you to query the logs of process snapshots, network connections, and process startups of containers. Prefix-based fuzzy match is supported. This topic describes how to search for logs.

**Background information**

The intrusion alert feature is developed based on the big data alerting model that is provided by Alibaba Cloud. The threat detection module of Server Guard provides comprehensive intrusion detection capabilities that can inform you of risks in Container Security for Kubernetes (ACK) and block external risks in an efficient manner.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Log Retrieval**.
4. On the **Log Retrieval** page, specify the **log source**, **log field**, **query condition**, and
**keyword**, and click **Search**.
You can select **Within 24 Hours** or **Within 7 Days** for the Duration parameter. You can also select **Custom** to specify a time range based on your business requirements. The
**custom time range** cannot exceed 30 calendar days.

### 3.5 Configure protection settings

This topic describes the core protection features of Container Security Service (CSS) and how to configure them. This helps you configure security policies in your business scenarios and improve the overall protection capabilities of the Container Service for Kubernetes (ACK) environment.

**Feature overview**

| Feature | Description |
|---|---|
| Container Network Topology | Displays the communication relationship between services in container clusters to assist in security analysis and exception troubleshooting. |
| Malicious Behavior Prevention | Blocks known malicious network behaviors to prevent containers from being exploited for attacks such as command and control communication and mining. |
| Container Escape Prevention | Protects against the unauthorized privilege escalation from containers to hosts by alerting or blocking. |
| Authorization management | Manages the container clusters that are integrated with the container security protection capability and their resource quotas (number of CPU cores). |

**Enable the container network topology feature**

After you enable this feature, the system automatically collects network communication data between containers and generates a visualized network topology. You can navigate to **Asset**
**> Container Network Topology** page to view the network topology. If you enable the
container network topology feature, a small amount of additional CPU resources is consumed.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose Runtime Detection > Feature Settings. On the
**Feature Settings** page, turn on the **Container Network topology collection** switch.

**Enable the malicious behavior prevention feature**

After you enable this feature, CSS blocks the abnormal network behaviors between your servers and disclosed malicious access sources. This reinforces the security of your servers.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose Runtime Detection > Feature Settings. On the
**Feature Settings** page, turn on the **Installation Status** switch.
You can click **Manage** to customize the management scope of the plug-in.

**Enable the container escape prevention feature**

The container escape prevention feature detects risky operations from multiple dimensions, such as processes, files, and system calls, and establishes protection barriers between containers and hosts. This helps block escape behaviors and ensure the runtime security of containers in an efficient manner. This feature defends against known and unknown attacks and blocks attacks that are launched by exploiting container vulnerabilities to take control over the hosts.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose Runtime Detection > Feature Settings. On the
**Feature Settings** page, turn on the **Threat Detection** switch.
4. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers > Container Escape Prevention** in the Rule type section to customize
protection rules. After you turn on the Threat Detection switch for the container escape prevention feature, you must configure a rule of the container escape prevention type to protect the container. For more information, see the `Proactive defense for containers` section of the Runtime detection chapter.

**Enable the authorization management feature**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose Runtime Detection > Feature Settings. On the
**Feature Settings** page, click **Manage** under the Authorization management feature to
customize the protection scope of your cluster.

> **Note:** After you bind the authorization to a cluster and container protection is enabled for the cluster, you cannot unbind the authorization from the cluster or bind the authorization to another cluster within 30 days.
> After the container cluster is released or scaled in, the system automatically revokes the authorization bound to the cluster.
> After you scale out a container cluster that is integrated with the container security protection capability, even if the number of CPU cores in the cluster exceeds the authorization quota, the container protection feature still protects all CPU cores in the cluster. However, the authorization cannot be bound to another cluster whose number of CPU cores exceeds the maximum authorization quota.

igurations

## 4 Apsara Stack Security configurations

**configurations**

### 4.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

### 4.2 规则运营

igurations

#### 4.2.1 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Cloud Firewall IPS Rules** tab, click **Create Rule**. In the Create Rule panel,
configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Name | The name of the IPS rule. We recommend that you enter an informative name to facilitate management. |
| Rules Engine | The rules engine that you want to use. Valid values:B asic Policies and Virtual Patches. |
| Attack Type | The type of attacks that you want to detect by using the IPS rule |
| Severity | The severity level. Valid values: Low, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability that you want to list in the IPS rule. Note CVE provides a list of public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Application | The name of the attacked application. |
| Rule Mode | The mode of the IPS rule. Valid values: Packet and Traffic. |
| Direction | The direction of traffic that you want to monitor by using the IPS rule. Valid values: Inbound and Outbound, Inbound, and Outbound. |

igurations

| Rule Content | The content of the IPS rule. You must specify the content by using the Snort syntax. Note To prevent negative impact on your business, make sure that you enter valid content for the rule. |
|---|---|
| Rule Description | The description of the IPS rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Remarks | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule to facilitate management. |

After you create custom IPS rules, you can perform the following operations on the rules: View the details of a rule You can filter rules by specifying filter conditions above the rule list. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable an IPS rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the state of the rule from **Disable** to **Enable**. Disable an IPS rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the state of the rule from **Enable** to **Disable**.

#### 4.2.2 Manage Anti-DDoS Service rules

On the Anti-DDoS Service Rules page, you can modify threshold settings for traffic scrubbing and redirection based on your business requirements. This topic describes how to modify threshold settings for traffic scrubbing and redirection.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Anti-DDoS Service Rules** tab, click **Scrubbing Policy**. Then, specify a custom
threshold for traffic scrubbing. i. Find the traffic scrubbing rule whose threshold you want to modify and click **Modify**
**Threshold** in the **Solution** column.
ii. In the **Modify Threshold** dialog box, specify a threshold and click **OK**. igurations
5. On the **Anti-DDoS Service Rules** tab, click **Reroute Threshold**. Then, specify custom
thresholds for traffic redirection. i. Find the rule whose thresholds you want to modify and click **Modify Threshold** in the
**Solution** column.
ii. In the **Modify Threshold** dialog box, specify custom thresholds and click **OK**. iii. **Optional.** Click **Automatic DDoS Traffic Redirection and Scrubbing**. In the **Enable**
**Automatic Redirection** message, click **OK**.

> **Note:** By default, **Automatic DDoS Traffic Redirection and Scrubbing** is turned off.

If you turn on Automatic DDoS Traffic Redirection and Scrubbing, traffic scrubbing events are triggered based on the thresholds that you specify. The traffic of attacked IP addresses is automatically forwarded to an Anti-DDoS cluster for scrubbing. If you turn off Automatic DDoS Traffic Redirection and Scrubbing, alert events are triggered based on the thresholds that you specify. You can start or end traffic scrubbing in the Anti-DDoS Service console based on your business requirements.

#### 4.2.3 Manage Server Guard rules

You can view vulnerabilities, baselines, and server exceptions on the Server Guard Rules tab. This topic describes how to view the information about Server Guard rules.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Server Guard Rules** tab, view the operations of Server Guard rules.

| Section or tab | Description |
|---|---|
| Overview (marked with ① in the preceding figure) | In this section, you can view the following information: Total Vulnerability Detection Rules, Total Baseline Check Items, Total Host Exception Detection Rules, and Engines. |

igurations

| Vulnerabilities (marked with ② in the preceding figure) | On the Vulnerabilities tab, you can view all detected vulnerabilities and the total number of detected vulnerabilities. To search for a vulnerability, you can select a vulnerability type from the Vulnerability Type drop-down list and enter a Common Vulnerabilities and Exposures (CVE) ID or an OS name in the search box. In the vulnerability list, you can view the information about a detected vulnerability in the following columns: Vulnerability Detection Rule Name, CVE ID, Operating System, Release Version, Updated At, Online At, and Status. |
|---|---|
| Baselines (marked with ② in the preceding figure) | On the Baselines tab, you can view the baseline types and the check items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and then enter a check item category or name in the search box. In the baseline list, you can view the information about a baseline in the following columns: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |
| Server Exceptions (marked with ② in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the information about an exception in the following columns: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |

#### 4.2.4 Create and manage WAF rules

You can create custom Web Application Firewall (WAF) rules based on your business requirements and network environment to monitor the operations of WAF. This topic describes how to create and manage WAF rules.

**Procedure**

> **Important:** WAF rules are global custom rules that take effect on all tenants. Proceed with caution.

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **WAF Rules** tab, click **Create Rule**. In the Create Rule panel, configure the
parameters and click **OK**. The following table describes the parameters. igurations

| Parameter | Description |
|---|---|
| Mode | The handling action and status of the rule. You can set the handling action to Block, Allow, Monitor, or Detection Module Control. You can set the status to Enable or Disable. |
| Description | The description of the rule. |
| Severity | The level of the severity. Valid values: No Threat, Low, Moderate, and Important. |
| Match Condition | The match condition of the rule. Each match condition consists of am atch field, a logical operator, and a match value. |
| Logging | Specifies whether to record logs. Valid values: Perform Logging When Match Condition Is Met Do not Perform Logging When Match Condition Is Met |
| Attack Type | The type of attacks that you want the rule to detect. You can select only one option. |
| Blocking Status Code | The status code that is returned. You can select only one option. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After you create rules, you can perform the following operations on the rules: Filter WAF rules by specifying filter conditions above the rule list. Find the rule that you want to manage and click **Modify** in the **Actions** column to modify the rule.

### 4.3 Configure alert settings

On the Alert Settings page, you can configure alert contacts and alert rules. When monitoring data triggers alert rules, the system automatically sends alerts to specified alert contacts by using DingTalk messages or emails. This topic describes how to configure alert contacts and alert rules.

**Configure alert contacts**

1. Log in to the Apsara Uni-manager Management Console.
igurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the Alert Settings tab, click **Create Contact**. In the Create Contact dialog box, enter the
contact name, DingTalk chatbot token, email address, and organization, and click
**Determine**.
You can view the added contact in the contact list. You can **modify** a contact or **delete** multiple contacts at a time.

**Configure alert rules**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the Alert Settings page, click the **AEGIS** tab. On the AEGIS tab, configure the alert rules
that you want to use and click **Save**.

| Alert type | Alert subtype | Alert level | Notificati on method | Frequency |
|---|---|---|---|---|
| Vulnerability | Linux software vulnerability Windows system vulnerability Web-CMS vulnerability Application vulnerability Urgent vulnerability | Low Medium High |   | 5 minutes |
| Baseline risk | High-risk exploit Classified protection compliance Best security practices Weak password | Low Medium High |   |   |
| Asset exposure | Vulnerability Non-vulnerability | All levels |   |   |

igurations

|   |   |   | Email DingTal k | 10 minutes 30 minutes 1 hour 1 day 1 week |
|---|---|---|---|---|
| Intrusion alert | Suspicious process Webshell Unusual login Anomalous activity Threat intelligence Malicious process (cloud threat detection) Unusual network connection Abnormal account Application intrusion event Cloud threat detection Precision defense Malicious script Persistent webshell Application threat detection | Low Medium High |   |   |
| Application whitelist event | Unauthorized process start | All levels |   |   |
| Tamper- proofing event | Unusual file modification Unusual file addition Unusual file deletion | All levels |   |   |

### 4.4 全局设置

#### 4.4.1 Configure the attack blocking feature

The attack blocking feature protects your servers from web attacks and brute-force attacks. This topic describes how to configure the attack blocking feature.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. igurations After you disable the attack blocking feature, Apsara Stack Security generates alerts for web attacks and brute-force attacks but does not block them.

### 4.5 账号管理

#### 4.5.1 Manage Apsara Stack tenant accounts

This topic describes how to view and modify the information about your Apsara Stack tenant account.

> **Important:** All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. Proceed with caution when you modify the account information.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find the Apsara Stack tenant account that you want to modify and click **Revised** in the
**Actions** column.
ii. In the **Change Account** dialog box, modify the Apsara Stack Account, Access Key, and Access Secret parameters, and click **OK**. After the modification, you can click Details in the **Actions** column to view the details of the Apsara Stack tenant account.

#### 4.5.2 Manage Alibaba Cloud accounts

After you add an Alibaba Cloud account to Apsara Stack Security, you can manage the Anti- DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security. This way, you can use features in a hybrid cloud. This topic describes how to add an Alibaba Cloud account to Apsara Stack Security.

**Procedure**

To use features in a hybrid cloud, you can add an Alibaba Cloud account to Apsara Stack Security.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Alibaba Cloud Account** tab, click **Add**.
igurations In the **Add Account** dialog box, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Access Key | The AccessKey ID of the Alibaba Cloud account that you want to add. |
| Access Secret | The AccessKey secret of the Alibaba Cloud account. |
| Alibaba Cloud Service | The Alibaba Cloud services that you want to use. Valid values:A nti- DDoS Pro and Anti-DDoS Premium IP and Web Application Protection. You can select one value or both. |

After the Alibaba Cloud account is added, you can view the account in the account list. You can **modify** or **remove** the account.

### 4.6 Migration to Apsara Uni-manager Operations Console

**manager Operations Console**

#### 4.6.1 Log on to Cloud Shield Operations Center

**Center**

Cloud Shield Operations Center is an operations platform for Apsara Stack Security services. The platform monitors the status and workloads of Apsara Stack Security services in real time and sends alert notifications to users. This topic describes how to log on to Cloud Shield Operations Center.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. igurations

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.
igurations

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, choose **Product Operation > Security O&M > Cloud Shield**
**Operations Center**.

**View execution results**

You can view information on the pages of **Cloud Shield Operations Center**.

#### 4.6.2 View system monitoring data

You can use the system monitoring feature to monitor integrated cloud services and identify exceptions in the cloud services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the system monitoring data.

**Procedure**

1. Log in to Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Monitoring and Alerting** > **System Monitoring**.
3. On the System Monitoring page, view the monitoring overview and monitoring data of cloud
services. On the **Monitoring Overview** tab, view the following information: Monitoring overview: You can view the total numbers of monitored services, abnormal services, metrics, and exceptions. Monitoring data of cloud services: You can view the information about each monitored cloud service, such as the service name, number of metrics, number of exceptions, and service status. You can view the monitoring data of each cloud service on the corresponding cloud service tab. Cloud services that can be integrated include: Server Guard, Security Operations Center (SOC), Network Traffic Detection and Response (NDR), Privileged Access Management (PAM), Tenant-side Bastionhost, Cloud Security Scanner, Container Security Service (CSS), and Key Management Service (KMS). igurations Monitoring scope: Click a cloud service tab to view all sub-services of the cloud service in the section marked with ② in the preceding figure. On a cloud service tab, use the search box marked with ① in the preceding figure to search for the required sub-service by service status and name. In a sub-service card marked with ③ in the preceding figure, view the information such as the CPU utilization, memory usage, workloads, number of TCP connections, and number of processes. igurations Click a sub-service card marked with ③ in the preceding figure. On the page that appears, view the monitoring details of the cloud service.

| Tab | Description |
|---|---|
| Basic Monitorin g | You can specify the monitoring time range and monitoring view to view the details of basic monitoring and middleware monitoring. Valid values for the time range: 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually update the monitoring data. You can also turn on Automatic Refresh to automatically update the monitoring data. The monitoring view supports Cluster View and Single-server View. You can view the following monitoring data: CPU utilization (%), memory usage (%), workloads, number of TCP connections, number of processes, and disk usage. |
| Middlewar e | You can specify the monitoring time range and monitoring view to view the details of basic monitoring and middleware monitoring. Valid values for the time range: 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually update the monitoring data. You can also turn on Automatic Refresh to automatically update the monitoring data. The monitoring view supports Cluster View and Single-server View. You can view the following monitoring data: the QPS of MetaQ, the number of garbage collections (GCs) in the JVM, the amount of time consumed to monitor GCs in the JVM, the amount of JVM memory, the number of loaded classes in the JVM, the numbers of JVM threads in different states, the number of JVM threads, the QPS of HSF, the response time of HSF and database usage. |
| Health Check | You can check the health status of all hosts in an application based on check methods such as TCP- and HTTP-based health checks. |

#### 4.6.3 Global settings

##### 4.6.3.1 Configure host security rules

1. Log in to the Cloud Shield Operations Center console.
2. In the left-side navigation pane, choose **Cloud Services > Server Guard O&M > Global**
**Settings**.
3. On the **Host Security Rule Settings** tab, configure the global brute-force attack
detection rule and silence threshold for high-risk command audit and click **Save and**
**Apply**. The following table describes the parameters.

**Important**

igurations

> If you modify the global brute-force attack detection rule, the detection rules for brute- force attacks on all host assets, such as tenant-side hosts and platform-side physical servers, are affected. The attack analysis result of Server Guard is also affected. Proceed with caution.

| Parameter | Description |
|---|---|
| Host Brute- force Attack | The time range within which you want to detect brute-force attacks and the maximum number of login failures that are allowed. If the number of login failures exceeds the specified upper limit within the specified time range, the system determines that a point-to-point brute-force attack is initiated from the source IP address. |
| Batch Unusual Logon | The time range within which you want to detect unusual logins and the maximum number of servers that can be logged in to by using a fixed account. If the number of servers that can be logged in to by using a fixed account exceeds the specified upper limit within the specified time range, the system determines that batch unusual logins are initiated from the source IP address. |
| Suspicious Account Logon | If a remote login account is included in the list of suspicious accounts, an alert is generated for logins that use the account. Click Manage Suspicious Accounts. In the Suspicious Account Management panel, enter suspicious accounts or upload a list of suspicious accounts by using a template. Make sure that the file to be uploaded does not exceed 5 KB in size. To ensure compatibility with the Windows system mechanism, use lowercase letters when you enter Windows accounts. |
| Audit of High- risk Commands | You can configure the silence threshold for high-risk command audit. After you configure the threshold, when the number of alerts generated by the rule reaches the threshold, the rule enters the silent mode and does not generate alerts until it resumes in the next cycle. Default threshold: 100 alerts within 5 minutes. For more information, see Configure host security rules in Apsara Stack Security User Guide for security administrators. |

##### 4.6.3.2 Configure whitelist settings

1. Log in to the Cloud Shield Operations Center console.
2. In the left-side navigation pane, choose **Cloud Services > Server Guard O&M > Global**
**Settings**.
3. On the Global Settings page, click the **Whitelist Settings** tab. On the Whitelist Settings
tab, click **Add**. In the **Create Whitelist** dialog box, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|

igurations

| Type | Global Logon Whitelist: Server Guard does not generate alerts for unusual logins from the IP addresses that are included in this whitelist. Whitelist for Brute-force Attacks: Server Guard does not generate alerts for brute-force attacks from the IP addresses that are included in this whitelist. |
|---|---|
| Source IP Address | The source IP address or CIDR block. |
| Destination IP | The destination IP address or CIDR block. If you set the Type parameter to Whitelist for Brute-force Attacks, you must configure the Destination IP parameter. |

You can **delete** a whitelist that is no longer required.

#### 4.6.4 Upgrade center

##### 4.6.4.1 Upgrade center overview

The upgrade center allows you to manually or automatically update the feature library and the version of Apsara Stack Security to ensure up-to-date protection. You can perform the following steps for an update:
1. Configure the import mode of your update package.
The upgrade center supports**automatic import** and **manual import**. If Apsara Stack can be accessed over the Internet, select **Online Automatic Import**. If Apsara Stack cannot be accessed over the Internet, select **Offline Manual Import**. If you select this option, you must download the update package. For more information, see Download update packages.
2. Update the feature library and the version of Apsara Stack Security. For more information,
see Update the feature library or the version of Apsara Stack Security.

##### 4.6.4.2 Feature library or version updates

The upgrade center supports automatic import and manual import of update packages. You can use the update packages to update the feature libraries or versions of Apsara Stack Security services. This topic describes how to update the feature libraries or versions of Apsara Stack Security services.

**Procedure**

1. Log in to Cloud Shield Operations Center.
2. In the left-side navigation pane, click **Upgrade Center**.
3. On the Upgrade Center page, click the **Upgrade configuration** tab. On the Upgrade
configuration tab, configure the Upgrade Package Import parameter.

**Offline Manual Import**

If your Apsara Stack environment is inaccessible over the Internet, you can manually import update packages to update the feature libraries or versions of Apsara Stack Security services. igurations a. Set the Upgrade Package Import parameter to **Offline Manual Import** and click
**Generate Upgrade Identifier**. Then, use the generated upgrade identifier to obtain
and download update packages. b. Click Import Upgrade Package. In the Manually Import offline upgrade packages dialog box, drag the downloaded update packages to the dotted box. Alternatively, click the icon to upload the update packages.

> **Note:** Before you upload the update packages, click the link in the **Manually Import** **offline upgrade packages** dialog box and trust the certificate.

After you import the update packages, you can view the update packages on the Feature Library Upgrade and Version Upgrade tabs and perform updates.

**Online Automatic Import**

If the Apsara Stack environment can connect to the Internet, you can select the automatic import method to import update packages and update the feature libraries or versions of Apsara Stack Security services. If you select online automatic import, take note of the following items:
1. Apsara Stack Security products and services must be able to access the Internet. 2.
You must apply for an Alibaba Cloud account or use an existing account. The account is used as the identity to automatically obtain the update package online. We recommend that you do not use your personal account. 3. After you complete the configuration, the system automatically obtains and imports the latest update package of Apsara Stack Security and related rule libraries. After the update package is imported, you can view the update package on the Feature Library Upgrade and Version Upgrade tabs and perform the update. igurations a. Set the Upgrade Package Import parameter to **Online Automatic Import** and configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Alibaba Cloud account ID | The ID of your Alibaba Cloud account. |
| Access Key | The AccessKey ID of the account. |
| Access Secret | The AccessKey secret of the account. |
| Automatic upgrade time period | The period within which automatic updates are performed. Valid values: 0-6 when 0-8 when 0-24 when 22-6 when |
| SLB IP | The IP address of the Server Load Balancer (SLB) instance that can connect to the Internet. |

b. Click **Connectivity test**. c. Turn on **Automatic update** if the connectivity test is successful. After **Automatic update** is turned on, the system automatically downloads update packages at a regular interval.
4. Update the feature libraries or versions of Apsara Stack Security services.

**Update feature libraries**

Update feature libraries of all services: On the **Feature Library Upgrade** tab, click
**One-click upgrade**.
Update feature libraries of a specific service: On the **Feature Library Upgrade** tab, find the service that you want to manage and click **Upgrade now** in the **Actions** column. After the update is complete, the state of the service changes to **Upgrade successful**. You can perform the following operations: If the update fails, click **Upgrade Records** in the **Actions** column. In the Feature Library Upgrade Records panel, find the feature library version that failed to be updated and click **Retry** in the Actions column. igurations If the update is successful, you can perform the following operations: On the **Feature Library Upgrade** tab, find the service that you want to manage and click **Version Details** in the **Actions** column. In the Feature Library Version Details panel, view the versions of the updated rule libraries. You can click **Restart**
**Upgrade** to update a rule library in a feature library.
On the **Feature Library Upgrade** tab, find the service that you want to manage and click **Upgrade Records** in the **Actions** column. In the Feature Library Upgrade Records panel, view the versions of the updated feature libraries. In the **Feature Library Upgrade Records**panel, find the feature library that you want to view and click **Details** in the **Actions** column. In the Feature Library Upgrade Package Details panel, view the details of the feature library update package. Find the rule library that you want to manage and click **Restart Upgrade** in the **Actions** column to update the rule library.

**Update versions**

Update versions of all services: On the **Version Upgrade** tab, click **One-click**
**upgrade**.
Update the version of a specific service: Find the service that you want to update on the **Version Upgrade** tab and click **Upgrade now** in the **Actions** column. After the update is complete, the state of the service is **Upgrade successful**. If the update fails, click **Upgrade Records** in the **Actions** column. In the panel that appears, find the feature library version that failed to be updated and click **Retry** in the Actions column. If the update is successful, you can perform the following operations: Click **Upgrade Records** in the **Actions** column to view the versions of the updated feature libraries. You can also click **Restart Upgrade** or **Rollback**.
