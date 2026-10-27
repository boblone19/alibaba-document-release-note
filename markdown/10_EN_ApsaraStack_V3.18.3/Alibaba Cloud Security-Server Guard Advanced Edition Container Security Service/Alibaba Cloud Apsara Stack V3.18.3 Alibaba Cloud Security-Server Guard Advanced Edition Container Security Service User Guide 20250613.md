---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service User Guide 20250613"
product_version: "V3.18.3"
doc_version: "20250613"
pdf_pages: 37
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service User Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Container%20Security%20Service%20User%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service User Guide 20250613

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Container Protection
  - 3.1 Asset center
    - 3.1.1 Container network topology
    - 3.1.2 Container management
    - 3.1.3 Image management
  - 3.2 CI/CD security
    - 3.2.1 Container image scan
    - 3.2.2 Scanner integration
  - 3.3 Runtime protection
    - 3.3.1 Vulnerability management
    - 3.3.2 Baseline check
    - 3.3.3 Intrusion alert
    - 3.3.4 Container firewall
    - 3.3.5 Container file protection
    - 3.3.6 Proactive defense for containers
  - 3.4 Log retrieval
  - 3.5 Feature settings
- 4 Apsara Stack Security configurations
  - 4.1 Log on to the Apsara Uni-manager Management Console
  - 4.2 Rules
    - 4.2.1 Create and manage IPS rules
    - 4.2.2 Manage Anti-DDoS Service rules
    - 4.2.3 Manage Server Guard rules
    - 4.2.4 Create and manage WAF rules
  - 4.3 Global configuration
    - 4.3.1 Configure the attack blocking feature
  - 4.4 Account management
    - 4.4.1 Manage Apsara Stack tenant accounts
    - 4.4.2 Manage Alibaba Cloud accounts

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

#### 3.1.1 Container network topology

You can use a network topology to view container assets from the Internet and cluster perspectives. This topic describes how to view the network topology of containers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Container Network Topology**.
4. On the **Cluster Overview** page, click the **Internet Perspective** or **Cluster Perspective**
tab.
5. On the **Internet Perspective** or **Cluster Perspective** tab, perform the following
operations: Use the date picker to specify a time range within the last seven days to view the running details of clusters. Click the or icon to enable or disable the network topology for all clusters. Click the icon to refresh the network topology of clusters. Click the icon to export the snapshot for the network topology of clusters. Click a cluster in the network topology to view the cluster information, cluster risks, image information, and protection policies.

#### 3.1.2 Container management

The container management feature allows you to synchronize assets and connect selfmanaged clusters. You can also view and manage namespaces, nodes, applications, pods, and containers in your assets. This topic describes how to manage containers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Container Management**.
4. On the **Container Management** page, synchronize assets or connect self-managed
clusters. Click **Synchronize Assets** to synchronize the assets.

> **Note:** The asset synchronization results take effect once every half an hour. Do not frequently click the button.

Click **On-premises cluster access**. In the **Manage an on-premises cluster cluster** panel, click **On-premises cluster access**. For more information, see the **Add a self-**
**managed Kubernetes cluster** topic.
5. On the **Container Management** page, click the name of a cluster in the **Cluster**
**Information** column or find a cluster and click **View** in the **Actions** column to go to the
details page of the cluster.
6. Click **Namespaces**, **Worker**, **Apply**, **Pod**, **Container**, or **Runtime mirroring**.
You can specify query conditions above the asset list to view assets after you click
**Namespaces**, **Worker**, **Apply**,**Pod**, **Container**, or **Runtime mirroring**.

| Asset | Operation |
|---|---|

| Namespa ce | Click the name of the namespace, or find a namespace and clickH andle in the Actions column. On the details page of the namespace, view information including vulnerabilities, alerts, and pods. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. Find a vulnerability and click View in the Actions column to view the vulnerability details and pending vulnerabilities. Click the CVE ID to view the vulnerability details and suggestions. You can ignore the vulnerability. You can also fix the vulnerability on an asset and click Verify to ensure vulnerability fixing. Find an alert and click Handle in the Actions column. In the dialog box that appears, select Handled Manually, Ignore, or Add to Whitelist. |
|---|---|
| Node | Click a node name or find a node and click Handle in the Actions column. On the details page of the node, view the vulnerabilities, alerts, and baseline check results. Click the Vulnerabilities, Alerts, or Baseline Risks tab to handle vulnerabilities and risks. |
| Applicati on | Click the name of an application, or find an application and clickH andle in the Actions column. On the details page of the application, view vulnerabilities, alerts, and pods. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. |
| Pod | Click the name of a pod, or find a pod and clickH andle in the Actions column. On the details page of the pod, view vulnerabilities, alerts, and pods. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. |
| Containe r | Click the name of a container, or find a container and clickH andle in the Actions column. On the details page of the container, view vulnerabilities and alerts. Click the Vulnerability and Alerts tabs to handle vulnerabilities and alerts. |
| Runtime image | View image system vulnerabilities, image application vulnerabilities, image baseline check results, and malicious image samples. Find a vulnerability and click View in the Actions column to view and handle the vulnerability. Find a baseline risk or malicious image sample and click Details in the Actions column to view and handle the risk or related container. |

#### 3.1.3 Image management

You can use the image management feature to synchronize assets and connect image repositories. You can also view and manage all images and at-risk images. This topic describes how to manage images.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Asset > Image Management**.
4. On the **Image management** page, synchronize assets or connect image repositories.
Click **Synchronize Assets** to synchronize the assets.

> **Note:** The asset synchronization results take effect once every half an hour. Do not frequently click the button.

Click **Image warehouse access**. In the **Image warehouse access** panel, configure the parameters. For more information, see the **Connect to a third-party image**
**repository** topic.
5. On the **Image management** page, find an image repository and click **View** in the **Actions**
column. The image list displays the following information: **Mirror information**, **Size**, **Latest**
**Detection Time**, **Scan status**, **Scan progress**, and **Risk Status**.
6. Find an image on which risks are detected and click **Handle** in the **Actions** column.
On the page that appears, you can view the following information about the image: **Image**
**System Vul**, **Image Application Vul**, **Image Baseline Check**, **Mirror Malicious**
**Sample**, and **Mirror Fingerprint Survey**. You can also click a vulnerability name or find a
vulnerability and click **Details** in the **Operation** column to view the vulnerability details.

### 3.2 CI/CD security

#### 3.2.1 Container image scan

Container Security Service (CSS) allows you to scan image repositories. You can scan for image vulnerabilities, baseline risks, and malicious samples. This topic describes how to scan images.

**Background information**

The container image scan feature can detect and identify high-risk system vulnerabilities, application vulnerabilities, malicious samples, configuration risks, and sensitive data in images. Vulnerabilities may exist in the basic system software, middleware, web applications, and databases that are in your images. The vulnerabilities include mining programs and backdoor programs. Containers that run based on vulnerable images pose threats to your assets. The feature allows you to check whether image vulnerabilities and malicious samples exist in your vulnerable assets, and provides suggestions on vulnerability fixing. The feature provides end-to-end vulnerability management capabilities and allows you to fix image vulnerabilities in a convenient manner.

**Scan images**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **CI/CD security > Image Scan**.

**Immediately scan images**

To immediately scan images, perform the following operations. You can scan only the container assets on which your account has permissions.
1. On the **Image Scan** page, click **Scan now**.
2. By default, all types of images are selected in the **One-Click Scan** dialog box. You can
clear the types of images that you do not want to scan, configure the **Scan Time Range** parameter, and click **OK**.

**Configure a periodic image scan**

1. In the upper-right corner of the **Image Scan**page, click **Scan Settings**.
2. On the Scan Configurations tab, configure the **Scan cycle** and **Scan Time Range**
parameters.
3. On the **Image repository** tab, view the list of image repositories that can be scanned. The
list displays image repositories that are of the **acr** and **defaultAcr** types, and connected third-party image repositories that are of the **harbor** and **quay** types. If the third-party image repositories that you want to scan are not displayed on the Image repository tab, click **Image warehouse access** to connect the desired third-party image repositories.
4. On the **Baseline Configuration Management**tab, click**Manage** on the right side of
**Configuration Scope**. Then, select the baselines that you want to check and click **OK**.
5. Click the close icon in the upper-right corner of the **Scan Settings** panel to close the panel.
After the configuration is complete, the system scans your images based on the configurations.

**View scan results**

1. In the left-side navigation pane, choose **CI/CD security > Image Scan**.
2. On the **Image System Vul** or **Image Application Vul** tab, click the name of a
vulnerability or find a **vulnerability** and click **View** in the **Operation** column. You can view the details of the vulnerability and the affected images.
3. On the **Image Baseline Check** tab, click **Details** in the **Operation** column of a baseline.
You can view **Image/Version** and **Check Details/Total Check Items** of the baseline. You can also click **Details** in the **Operation** column to view the status of a risk, and click
**Whitelist** or **Remove** to add the risk to the whitelist or remove the risk from the whitelist.
4. On the **Mirror Malicious Sample** tab, click the name of a malicious sample or click
**Details** in the **Operation** column of the **malicious sample**.
You can view the details of the malicious sample and the affected images.

#### 3.2.2 Scanner integration

The scanner integration feature can detect image risks in the project building stage and provide solutions to detected image risks. This topic describes how to configure the scan plug-in.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

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
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

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

#### 3.3.2 Baseline check

The baseline check feature can help you identify baseline risks in an efficient manner. This topic describes how to detect and handle baseline risks.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Baseline Check**.
4. In the upper-right corner of the **Baseline Check** page, click **Manage Policies**. In the panel
that appears, click **Add standard policy** or click **Edit** in the **Actions** column of an existing standard policy. In the panel that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a policy name. You cannot change the name of an existing policy. |
| Schedule | Select a check interval for the policy. Valid values: Every Day, Every 3 Days, Every 7 Days, and Every 30 Days. |
| Detection time | Select a check period for the policy. Valid values: 0:00 - 6:00, 6:00 - 12:00, 12:00 - 18:00, and 18:00 - 24:00. |
| Check Items | Select baseline types. Valid values include: Kubernetes (ACK) Master Internationally Agreed Best Practices for Security Kubernetes (ACK) Node Internationally Agreed Best Practices for Security Alibaba Cloud Standard - Kubernetes-Master security baseline check Alibaba Cloud Standard - Kubernetes-Node security baseline check |
| Effective Cluster | Select clusters on which you want the baseline check to take effect. |

5. Go back to the **Baseline Check** page, select a created policy from the **Select Policy** drop-
down list and click **Check Now**. After the baseline check is complete, you can view and verify baseline risks in the baseline list.
6. Click the name of a baseline. In the panel that appears, perform the following operations:
Move the pointer over an asset name to view the details of the affected asset. Click **Verify** in the **Actions** column of an affected asset. You can also select multiple vulnerabilities and click **Verify** below the asset list to verify the risk at a time.

#### 3.3.3 Intrusion alert

Container Security allows you to monitor nodes and containers in clusters. You can monitor and block risks such as trojans, intrusions, supply chain attacks, and container escapes that are caused by privilege escalation. This topic describes how to configure the intrusion alert feature.

**Background information**

The intrusion alert feature is developed based on the big data alerting model that is provided by Alibaba Cloud. The threat detection module of Server Guard provides comprehensive intrusion detection capabilities that can inform you of risks in Container Security for Kubernetes (ACK) and block external risks in an efficient manner.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Intrusion Alerts**.
4. On the **Intrusion Alerts** page, view the numbers of at-risk nodes, at-risk containers, all
risks, and high-level risks. You can specify filter conditions to view information about an alert such as the alert level, alert name, and affected assets. You can move the pointer over the name of an **affected**
**asset** to view the details of the affected asset.
5. Click **Handle** in the **Actions** column of the alert that you want to manage.
You can select **Add To Whitelist**, **Ignore**, **Handled manually**, or **Batch unhandled**
**(combine the alert triggered by the same rule or type)** for the intrusion for which the
alert is generated.
6. On the **Intrusion Alerts** page, click the name of an alert or click **Details** in the **Actions**
column of the alert. You can view the details of the alert and associated exceptions of the alert.

#### 3.3.4 Container firewall

The container firewall feature helps you protect container assets from attacks. This topic describes how to configure the container firewall feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

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

#### 3.3.5 Container file protection

The container file protection feature can monitor directories and files in containers in real time, and generate alerts or intercept tampering operations when the directories or files are tampered with. This prevents your applications from being inserted with illegal information or malicious code and ensures the security of the container environment.

**Create a rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Container File**
**Protection**.
4. On the **Container File Protection** page, click **New rule**.
5. In the **New rule** panel, configure the parameters and click **Next**.

| Parameter | Description | Example |
|---|---|---|
| Rule Name | Enter a name for the rule. The name must be 6 to 50 characters in length and can contain letters, digits, underscores ( ), _ and hyphens (-). It must start with a letter. | Cluster01 |

| Rule Configur ation | Protected File Directory | Enter the directory that you want to protect. When you configure this parameter, take note of the following items: The directory must start with a forward slash (/). You can enter only one directory. The length of a directory must be less than 500 characters. You can enter only one directory each time. To protect multiple directories, click Add in the Actions column. You can specify up to 10 directories in a rule. | /home/app/label |
|---|---|---|---|
|   | Whitelist | Enter the processes that are allowed to modify the protected directory. If a process is added to the whitelist, no alert is generated and the process is not blocked when the process modifies files. When you configure this parameter, take note of the following items: You can enter only the processes that run in your container. The length of a process cannot exceed 50 characters. You must separate multiple processes with semicolons (;). You can add up to 10 processes to the whitelist of a directory. | /bin/cp;/usr/bin/mv;/bi n/vi |

|   | Action | Select the action that you want the system to perform when a tampering operation is detected. Valid values: Alert: When the system detects tampering operations on files in the directory, the system only generates alerts. Block: When the system detects tampering operations on files in the directory, the system generates alerts and blocks the tampering processes. Note We recommend that you set the Action parameter to Alert. After you confirm that no false alerts are generated, change the Action parameter to Block. This prevents normal processes from being blocked. If a blocked process is required in your workloads, you can add the process to the whitelist. | Alert |
|---|---|---|---|

6. Select the cluster on which you want the rule to take effect in the Cluster Name column,
select a pod label in the Pod Tag column, and then click **Determine**. We recommend that you select a pod label that starts with app. In Kubernetes, labels are key-value pairs and are used to label and classify Kubernetes resources, such as pods, Deployments, and services. You can add custom labels to Kubernetes resources based on scenarios, features, or purposes to better manage the resources. Labels that start with app are used to organize resources by application. If no labels are displayed in the drop-down list, you must enter a label. If you want the rule to take effect on multiple clusters or multiple pod labels in a cluster, you can click **Add** in the Actions column to specify multiple clusters or pod labels.

**Manage the rule**

After you create a rule, you can perform the following operations on the **Container File**
**Protection** page:
Copy the rule Click **Copy** in the **Actions** column to copy the rule. Enable or disable the rule Click the switch in the **Enable** column to enable or disable the rue. Edit the rule Click **Edit** in the **Actions** column to modify the name, configurations, and scope of the rule. Delete the rule

> **Important:** The deleted rule cannot be restored. Before you delete a rule, make sure that you no longer require the rule.

Click **Delete** in the **Actions** column. In the message that appears, click **OK** to delete the rule.

#### 3.3.6 Proactive defense for containers

The feature of proactive defense for containers detects risks when your containers start or run from the following dimensions: image security, runtime security, and running environment security. You can configure rules to block the running of at-risk images, stop untrusted processes, and block container escapes. This helps improve the runtime security of your containers.

**Rule description**

The following table describes the rule types that you can select based on your business requirements.

| Type | Description |
|---|---|
| Non-image Program Defense | After you create a rule of the Non-image Program Defense type, the system detects and blocks the startup of programs that are not included in the images of specified clusters in the rule. This helps defend against malicious software intrusion and known and unknown attacks. |
| Container Escape Prevention | After you create a rule of the Container Escape Prevention type, the system detects risky operations from multiple dimensions, such as processes, files, and system calls, and establishes protection barriers between containers and hosts. This helps block escape behaviors and ensure the runtime security of containers in an efficient manner. You can also use this type of rule to block attacks that are launched by exploiting container vulnerabilities to take control over hosts. This helps improve the security of operating systems. |

**Manage system rules**

By default, Container Security Service (CSS) provides the system rule for non-image program defense. The system rule is automatically enabled for users who do not configure custom rules for non-image program defense. The system rule generates alerts for the startups of non-image programs in all clusters that are connected to CSS. You can perform the following operations to view the system rule for non-image program defense: Log on to the CSS console. In the left-side navigation pane, choose Runtime Detection > **Proactive Defense**
**for Containers**. Then, select **Non-image Program Defense** for Rule type and view the
system rule on the **System Rule** tab. The action that is specified in the system rule is Alert. When the startup of a non-image program is detected, the system generates an alert and does not block the startup of the non-image program. You can enable or disable a system rule, and modify the clusters on which the system rule takes effect. If the clusters are changed or new clusters are added, the system automatically adds the new clusters to the protection scope. The first time you use the non-image program defense feature, we recommend that you check whether false positive alerts are generated by the system rule. You cannot configure whitelists in the system rules or block the risky behavior detected by the system rules. If you want to configure a whitelist or block a risky behavior, you can create a custom rule. After you create a custom rule, the system rule is automatically disabled and cannot be re-enabled. If you want to enable the system rule, you must delete all custom rules.

**Create a custom rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers**.
4. In the **Rule Type** section, click **Non-image Program Defense**.
5. On the **Custom Rule** tab, click **New rule**.
6. In the **New rule** panel, configure the parameters to create a rule and click **Next**. In the
message that appears, click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the rule. |
| Rule description | Enter a description for the rule. |
| Status | Turn on or turn off the switch for the rule. Valid values: On: If you turn on the switch, the rule is enabled after it is created and is automatically applied to protect the clusters within the protection scope. Off: If you turn off the switch, the rule is disabled and does not take effect after it is created. |

| Defense Action | Specify the action that is performed after the rule is triggered. Valid values: Alert: If an untrusted process is detected, the system generates an alert. Intercept: If an untrusted process is detected, the system generates an alert and blocks the process. Note We recommend that you first set the Defense Action parameter to Alert. If no executable programs that are not included in container images are installed and started during the running of your container, change the value of the Defense Action parameter to Intercept. This helps prevent false positives. |
|---|---|
| Create File Directory Whitelist | Click Create Rule and enter the file directory that you want to add to the whitelist. Separate multiple directories with line breaks. Example: /user/name1 . |
| Create Image Whitelist | Click Create Rule and enter the image that you want to add to the whitelist. For example, if you want to add the image whose address is yundun-example- registry.cn-hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords: yun-repo test yun-repo:test repo:test |

7. Select the clusters to which you want to apply the rule and click **OK**.
You can configure only one rule for a cluster. If a rule is already configured for a cluster, you cannot select the cluster in this step.

**Use container escape prevention**

**Manage system rules**

CSS provides various rules of the container escape prevention type. By default, the rules are enabled for all clusters that are connected to CSS. The rules are referred to as system rules. You can perform the following operations to view the system rule for non-image program defense: Log on to the CSS console. In the left-side navigation pane, choose Runtime Detection > **Proactive Defense for Containers**. Then, select **Container Escape**
**Prevention** for Rule type and view information about system rules on the **System Rule** tab.
The action that is specified in a system rule is Alert. When an escape behavior is detected, the system generates an alert and does not block the behavior. You can enable or disable a system rule, and modify the clusters on which the system rule takes effect. If the clusters are changed or new clusters are added, the system automatically adds the new clusters to the protection scope. The first time you use the container escape prevention feature, we recommend that you check whether false positive alerts are generated by the system rules. If no false positive alert is generated, you can change the rule action that is specified in the rules to Block. You cannot configure whitelists in the system rules or block the risky behavior detected by the system rules. If you want to configure a whitelist or block a risky behavior, you can create a custom rule. After you create a custom rule of a specific type, the system rule of the same type is automatically disabled.

**Create a custom rule**

CSS provides the same types of custom rules and system rules. You can configure whitelists and set Defense Action to Block for custom rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Runtime Detection > Proactive Defense for**
**Containers**.
4. In the **Rule type** section, click **Container Escape Prevention**.
5. On the **Custom Rule** tab, click **New rule**.
6. In the **New rule** panel, configure the parameters to create a rule and click **Next**. In the
message that appears, click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the rule. |

| Rule type | Select a rule type based on your business requirements. After you select a type, all check items that are supported for the type are selected. If you do not require specific check items, you can clear the check items. Valid values: modify host profile: This occurs when system configuration files, such as /etc/passwd, or SSH service configuration directories are mounted into a container at startup. This can allow an attacker to modify the files within the container, thereby gaining user permissions on the host node. escape to host by exploiting vulnerabilities or improper configuration: This occurs when a container is started with escalated privileges or when pseudo file systems are mounted. This can allow an attacker to exploit system mechanisms such as core pattern and cgroup within the container to escape. _ high risk system call: This occurs when attackers exploit kernel vulnerabilities to escalate privileges or perform escape actions. Attackers use critical system calls to achieve these objectives. escape to host by writing to important host file: This occurs when a container is started with high-risk directories mounted such as etc/crontab, init script directories such as /etc/init.d, trigger- based script directories such as /etc/profile, and Kubernetes static pod configuration directories. Attackers can write malicious code into these directories that can be automatically executed on the host, thereby granting the attacker permissions. run container escape tool: This checks the running of escape tools within a container. In most cases, after an attacker intrudes into a container, the attacker uses these tools to break out of the container and bypass the isolation between the container and the host node, thereby gaining control over the host. |
|---|---|
| Defense Action | Select a defense action. Valid values: Alert: The system only generates alerts when it detects risks specified in the rule. Block: The system generates alerts and blocks the related processes or operations when it detects risks specified in the rule. Note A rule may be triggered in some normal business scenarios. When you configure a rule, we recommend that you set the Defense Action parameter to Alert and check whether false positive alerts are generated within a period of time. If no false positive alerts are generated, change the value of the Defense Action parameter to Block. |

| Add to Whitelist | Click Create Rule and enter the tag name of the image that you want to add to the whitelist. You can add up to 20 images to the whitelist. Fuzzy match is supported by using keywords. If you want to add the image whose address is yundun-example-registry.cn- hangzhou.aliyuncs.com/yundun-example/yun-repo:test to the whitelist, you can enter one of the following keywords: yun-repo test yun-repo:test repo:test Note After you add an image to the whitelist, the system does not detect escape behaviors on the image. Proceed with caution. |
|---|---|

After you complete this step, the rule is displayed in the rule list.
7. Select the clusters that you want to protect and click **OK**.

### 3.4 Log retrieval

The log retrieval feature allows you to query the logs of process snapshots, network connections, and process startups of containers. Prefix-based fuzzy match is supported. This topic describes how to search for logs.

**Background information**

The intrusion alert feature is developed based on the big data alerting model that is provided by Alibaba Cloud. The threat detection module of Server Guard provides comprehensive intrusion detection capabilities that can inform you of risks in Container Security for Kubernetes (ACK) and block external risks in an efficient manner.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Log Retrieval**.
4. On the **Log Retrieval** page, specify the **log source**, **log field**, **query condition**, and
**keyword**, and click **Search**.
You can select **Within 24 Hours** or **Within 7 Days** for the Duration parameter. You can also select **Custom** to specify a time range based on your business requirements. The
**custom time range** cannot exceed 30 calendar days.

### 3.5 Feature settings

This topic describes how to manage protection capabilities and protection modes for each container to improve the efficiency and security of containers.

**Management protection modes**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Container Security Service (CSS)**. On the **Container**
**Security Service (CSS)** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Feature Settings**.
4. Find the **Malicious Behavior Prevention** section, and turn on the switch for **Installation**
**Status**, or find the **Container Escape Prevention** section and turn on the switch for
**Threat Detection**.
5. In the **Malicious Behavior Prevention** section, click **Manage** next to **Management**
**Scope**. In the dialog box that appears, select the assets that you want to protect and click
**OK**.
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

### 4.2 Rules

igurations

#### 4.2.1 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Cloud Firewall IPS Rules** tab, click **Create Rule**. In the panel that appears,
configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | The name of the IPS rule. We recommend that you enter an informative name for easy management. |
| Rules Engine | The rules engine that you want to use. Valid values:B asic Policies and Virtual Patches. |
| Attack Type | The type of attacks that you want to detect by using the IPS rule |
| Severity | The level of the severity. Valid values: Low, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability that you want to list in the IPS rule. Note CVE provides a list of public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Application | The name of the attacked application. |
| Rule Mode | The mode of the IPS rule. Valid values: Packet and Traffic. |
| Direction | The direction of traffic that you want to monitor by using the IPS rule. Valid values: Inbound and Outbound, Inbound, and Outbound. |

igurations

| Rule Content | The content of the IPS rule. You must specify the content by using the Snort syntax. Note To prevent negative impact on your business, make sure that you enter valid content for the rule. |
|---|---|
| Rule Description | The description of the IPS rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Description | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |

After you create a custom IPS rule, you can perform the following operations on the rule: View the details of the rule You can filter rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable the rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the status of the rule from **Disable** to **Enable**. Disable the rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the status of the rule from **Enable** to **Disable**.

#### 4.2.2 Manage Anti-DDoS Service rules

On the Anti-DDoS Service rules page, you can modify threshold settings for traffic scrubbing and redirection based on your business requirements. This topic describes how to modify threshold settings for traffic scrubbing and redirection.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
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

If you turn on Automatic DDoS Traffic Redirection and Scrubbing, traffic scrubbing events are triggered based on custom thresholds. The traffic of attacked IP addresses is automatically forwarded to an Anti-DDoS cluster for scrubbing. If you turn off Automatic DDoS Traffic Redirection and Scrubbing, alert events are triggered based on custom thresholds. You can start or end traffic scrubbing in the Anti-DDoS Service console based on your business requirements.

#### 4.2.3 Manage Server Guard rules

You can view vulnerabilities, baselines, and server exceptions on the Server Guard Rules tab. This topic describes how to view the information about Server Guard rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Server Guard Rules** tab, view the information about Server Guard rules.

| Item | Description |
|---|---|
| Overview (marked 1 in the preceding figure) | You can view the following information: Total Vulnerability Detection Rules, Total Baseline Check Items, Total Host Exception Detection Rules, and Engines. |

igurations

| Vulnerabilities (marked 2 in the preceding figure) | On the Vulnerabilities tab, you can view all detected vulnerabilities and the total number of detected vulnerabilities. To search for a vulnerability, you can select a vulnerability type from the Vulnerability Type drop-down list and enter a Common Vulnerabilities and Exposures (CVE) ID or operating system (OS) name in the search box. In the vulnerability list, you can view the following information about a detected vulnerability: Vulnerability Name, CVE ID, Vulnerability Type, OS, Updated At, and Status. |
|---|---|
| Baselines (marked 2 in the preceding figure) | On the Baselines tab, you can view the baseline types and check the items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and enter a check item category or name in the search box. In the baseline list, you can view the following information about a baseline: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |
| Server Exceptions (marked 2 in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the following information: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |

#### 4.2.4 Create and manage WAF rules

You can create custom Web Application Firewall (WAF) rules based on your business requirements and network environment to monitor the operations of WAF. This topic describes how to create and manage WAF rules.

**Procedure**

> **Important:** WAF rules are global custom rules that take effect on all tenants. Proceed with caution.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **WAF Rules** tab, click **Create Rule**. Configure the parameters and click **OK**.

| Parameter | Description |
|---|---|

igurations

| Mode | The handling action and status of the rule. You can set the handling action to Block, Allow, Monitor, or Detection Module Control. You can set the status to Enable or Disable. |
|---|---|
| Description | The description of the rule. |
| Severity | The level of the severity. Valid values: No Threat, Low, Moderate, and Important. |
| Match Condition | The match condition of the rule. Each match condition consists of am atch field, a logical operator, and a match value. |
| Logging | Specifies whether to record logs. Valid values: Perform Logging When Match Condition Is Met and Do not Perform Logging When Match Condition Is Met. |
| Attack Type | The type of attacks that you want the rule to detect. You can select only one value. |
| Blocking Status Code | The status code that is returned. You can select only one value. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After you create a rule, you can perform the following operations on the rule: Filter the WAF rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details.

### 4.3 Global configuration

#### 4.3.1 Configure the attack blocking feature

The attack blocking feature protects your servers from web attacks. This topic describes how to configure the attack blocking feature.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
igurations
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. After you disable the attack blocking feature, Server Guard generates alerts for web attacks but does not block them.

### 4.4 Account management

#### 4.4.1 Manage Apsara Stack tenant accounts

This topic describes how to view and modify the information about your Apsara Stack tenant account.

> **Important:** All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. You can modify the account information. Proceed with caution.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find your Apsara Stack tenant account and click **Revised** in the **Operation** column. ii. In the **Change Account** dialog box, modify Apsara Stack Account, Access Key, and Access Secret, and click **OK**. After the modification, you can click Details in the **Operation** column to view the details of the Apsara Stack tenant account.

#### 4.4.2 Manage Alibaba Cloud accounts

After you add an Alibaba Cloud account to Apsara Stack Security Center, you can manage the Anti-DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security Center. This way, you can use features in a hybrid cloud. This topic describes how to add an Alibaba Cloud account to Apsara Stack Security Center.

**Procedure**

To use features in a hybrid cloud, you can add an Alibaba Cloud account to Apsara Stack Security Center.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
igurations
4. On the **Alibaba Cloud Account** tab, click **Add**.
i.

| Parameter | Description |
|---|---|
| Access Key | The AccessKey ID of the Alibaba Cloud account that you want to add. |
| Access Secret | The AccessKey secret of the Alibaba Cloud account. |
| Alibaba Cloud Service | The Alibaba Cloud services that you want to use. Valid values:A nti- DDoS Pro and Anti-DDoS Premium IP and Web Application Protection. You can select one value or both. |

After the Alibaba Cloud account is added, you can view the account in the account list. You can **modify** or **remove** the account.
