---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 32
source_pdf: "8d4642f5a6f325cb_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Operat"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Physical machine-based WAF O&M in Apsara Infrastructure Management
  - 1.1 Log in to the Apsara Infrastructure Management console
  - 1.2 Check the service status
    - 1.2.1 Basic inspection
    - 1.2.2 Advanced inspection
- 2 Physical machine-based WAF O&M in Cloud Shield Operations Center
  - 2.1 Log on to Cloud Shield Operations Center
  - 2.2 Global system settings
  - 2.3 Configure global custom rules
  - 2.4 Metrics
    - 2.4.1 Introduction to WAF metrics
    - 2.4.2 View metrics

O&M in Apsara Infrastructure Ma nagement

## 1 Physical machine-based WAF O&M in Apsara Infrastructure Management

**WAF O&M in Apsara**

**Infrastructure Management**

### 1.1 Log in to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log in to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. O&M in Apsara Infrastructure Ma nagement

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter the correct username and password.
O&M in Apsara Infrastructure Ma nagement

**Note**

Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Apsara Infrastructure Management**.

### 1.2 Check the service status

#### 1.2.1 Basic inspection

The basic inspection of Web Application Firewall (WAF) checks whether a service runs as expected.

**Procedure**

1. Log in to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**.
3. In the **Product | Cluster** search box, enter **SemaWafCluster**.
4. Find the `SemaWafCluster-A-xx` cluster and click **Cluster Details** in the **Actions** column.
5. On the **Services** tab, enter **yundun-semawaf** in the **Service** search box to check whether
the service status is normal.

#### 1.2.2 Advanced inspection

The advanced inspection of Web Application Firewall (WAF) checks the system status and service status.

**Procedure**

1. Log on to the two physical machines of WAF.
i. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**.
O&M in Apsara Infrastructure Ma nagement ii. In the **Product | Cluster** search box, enter **SemaWafCluster**. iii. Find the `SemaWafCluster-A-xx` cluster and click **Cluster Details** in the **Actions** column. iv. On the **Services** tab, enter **yundun-semawaf** in the **Service** search box and click
**Details** in the Actions column. The service details page appears.
v. In the **Components** section, click **YundunSemawafApp#**. vi. In the Information of Component YundunSemawafApp# section, click the **Instances** tab. On this tab, find the instance whose information you want to view and click **Terminal** in the **Actions** column to log in to the WAF physical machine. vii. In the left-side navigation pane, click the node to which you want to log in or the icon. In the dialog box that appears, select **Account Type** and **Server Account**, and then click **OK**. For more information about account types and server accounts, see **Platform O&M >**

**Apsara Infrastructure Management > Web clients > Web Client Logon > Server**

**logon** in **Apsara Uni-manager Operations Console User Guide** .
2. Check the system status.
i. View system logs. Run the dmesg -T |tail -30 command to check for exception logs. ii. Check the system loads. Run the `free -h` command to check whether the memory usage is normal. Run the `df -h` command to check whether the disk usage is normal. Run the `uptime` command to check whether the average system load is normal. Run the `top` command to check whether the CPU usage is normal.
3. Check the service status.

**Note**

In the WAF installation directory /home/safeline, perform the following operations. i. Run the `cd /home/safeline` command to open the installation directory. ii. Check the minion service. a. Run the `systemctl status minion` command to check the execution time and the status of the minion service. b. Run the `tail -100 logs/minion/minion.log` command to check for exception logs. O&M in Apsara Infrastructure Ma nagement iii. Check the mgt-api service. a. Run the `docker logs --tail 50 mgt-api` command to check for exception logs. b. Run the `docker exec -it mgt-api supervisorctl status` command to check whether the service runs as expected and whether **uptime** is normal. c. Run the `tail -50 logs/management/gunicorn.log` command to check for exception logs. d. Run the `tail -50 logs/management/daphne.log` command to check for exception logs. e. Run the `tail -50 logs/management/scheduler.log` command to check for exception logs. f. Run the `tail -50 logs/management/dramatiq.log` command to check for exception logs. iv. Check the redis service. Run the `docker logs --tail 50 mgt-redis` command to check for exception logs. v. Check the detector service. a. Run the `docker logs --tail 50 detector-srv` command to check for exception logs. b. Run the `tail -50 logs/detector/snserver.log` command to check for exception logs. c. Run the curl 127.0.0.1:8001/stat | grep num command to check whether the service responds and whether the status of the real-time request processing data is normal. For example, check whether the value of the **req_num_total** parameter is normal. The req_num_total parameter indicates the number of requests that are processed within the previous 5 seconds. vi. Check the tengine service. a. Run the `docker logs --tail 50 tengine` command to check for exception logs. b. Run the `tail -50 logs/nginx/error.log` command to check for exception logs. vii. Check the mario service. a. Run the `docker logs --tail 50 mario` command to check for exception logs. b. Run the `tail -50 logs/mario/mario.log` command to check for exception logs. c. Run the `curl 127.0.0.1:3335/api/v1/state` command to check whether the service responds and whether the status of the real-time request processing data is normal. For example, check whether the **num_pending** parameter remains at a high value of nearly 10,000 or whether the value of the **num_processed_last_10s** parameter is normal. The num_processed_last_10s parameter indicates the number of requests that are processed within the previous 10 seconds.

## 2 Physical machine-based WAF O&M in Cloud Shield Operations Center

**WAF O&M in Cloud Shield**

**Operations Center**

### 2.1 Log on to Cloud Shield Operations Center

**Operations Center**

Cloud Shield Operations Center is an operations platform for Apsara Stack Security services. The platform monitors the status and workloads of Apsara Stack Security services in real time and sends alert notifications to users. This topic describes how to log on to Cloud Shield Operations Center.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, choose **Product Operation > Security O&M > Cloud Shield**
**Operations Center**.

**View execution results**

You can view information on the pages of **Cloud Shield Operations Center**.

### 2.2 Global system settings

You can configure global system settings to enable or disable the Web Application Firewall (WAF) global protection engine, specify an internal-facing Server Load Balancer (SLB) instance as the downstream service, and configure shared virtual IP addresses. This topic describes how to configure global system settings.

**Procedure**

1. Log in to the Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > WAF Management > Global**
**Config**.
3. On the **Global system settings** page, configure the following parameters.

| Parameter | Description | Supported operation |
|---|---|---|
| WAF global protection engine | Specify whether to enable the global protection engine. The engine determines the status of intrusion prevention configurations on the platform management side and the service group management side. If you disable the engine, WAF allows all traffic and does not perform intrusion detection or traffic processing. | Turn on or off the switch. |

| Intelligence Switch | After you turn off the switch, the existing WAF rules no longer take effect. | Turn on or off the switch. |
|---|---|---|
| Private SLB as site downstream | Specify whether to associate an elastic IP address (EIP) with an SLB instance to add the EIP to WAF. | Turn on or off the switch. |
| Shared IP | Specify whether to enable shared IP addresses. | Turn on or off the switch. |
| Create external shared virtual IP | Create a shared public virtual IP address. | Click Click to create to the right of the parameter. Important If you click Click to create, five shared public virtual IP addresses are created. Proceed with caution. |
| Nginx log delivery to OSS | Specify whether to deliver NGINX logs to Object Storage Service (OSS). | Click the icon to the right of the parameter. In the Edit nginx log delivery to OSS dialog box, turn on the switch, specify Endpoint, AccessKeyId, AccessKeySecret, and Preset OSS path, and then click OK. |
| Show Alibaba Cloud Logo when exporting reports | Specify whether to display the Alibaba Cloud logo in the security report. | Turn on or off the switch. |
| Log download quota | Specify the maximum number of logs that can be downloaded. | Click the icon to the right of this parameter. Then, set the maximum number of logs that can be downloaded and click Confirm. |
| Anti-tampering | Specify whether to enable web page protection. When a locked page receives a request, a cached version of the page is returned. This helps prevent web page tampering. | Turn on or off the switch. |
| EIP | Specify whether EIPs can be added to WAF. | Turn on or off the switch. |

| Specify response status code for unmatched domains | Specify the status code to return when no domain name is matched. | Click the icon to the right of this parameter to specify the HTTP status code to return. |
|---|---|---|
| Maximum number of listening ports | Specify the maximum number of listening ports. | Click the icon to the right of this parameter to specify the maximum number of listening ports. |

### 2.3 Configure global custom rules

You can create global custom rules in Web Application Firewall (WAF) based on your business requirements and network environment to monitor the status of WAF. This topic describes how to create and manage global custom rules.

**Procedure**

**Important**

The global custom rules that you add take effect on all tenants. Proceed with caution.
1. Log in to the Cloud Shield Operations Center.
2. In the left-side navigation pane, choose **Cloud Services > WAF Management > Global**
**Rules**.
3. On the **Rule management** page, click **Create Rule**, configure the following parameters,
and then click **OK**.

| Parameter | Description |
|---|---|
| Mode | The action and status of the rule. You can set the action to Block, Allow, Monitor, or Detection Module Control. You can set the status to Enable or Disable. |
| Description | The description of the rule. |
| Severity | The severity level of the rule. Valid values: No Threat, Low, Moderate, and Important. |
| Match Condition | The match conditions of the rule. Each match condition consists of thef ield to be matched, logical operator, and value of the field. |

| Logging | Specify whether to enable logging. Valid values: Perform Logging When Match Condition Is Met Do not Perform Logging When Match Condition Is Met |
|---|---|
| Attack Type | The type of attacks that you want the rule to detect. You can select only one type. |
| Blocking Status Code | The status code that is returned. You can select only one status code. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After the global custom rule is added, you can perform the following operations on the rule in the rule list. Specify **Mode**, **Severity**, and **Status** above the list to filter global custom rules. Find the rule that you want to manage and click **Edit** in the **Actions** column of the rule to modify the rule. Select multiple rules, click **More operations** above the list, and then select Enable Rule, Disable Rule, or Delete Rule to enable, disable, or delete the rules at a time.

### 2.4 Metrics

#### 2.4.1 Introduction to WAF metrics

This topic describes the common metrics for Web Application Firewall (WAF).

**Business metrics**

**Note**

The hyphen (-) in the following table indicates that the metric is unavailable in Cloud Shield Operations Center.

| Metr ic | Metric definiti on | Data type | Uni t | Data dime nsio n | Coll ecti on inte rval | Script | Remarks | Wh eth er ava ilab le in Clo ud Sec urit y Op era tio ns Cen ter | Wh eth er an ale rt is trig ger ed |
|---|---|---|---|---|---|---|---|---|---|
|   | acl temp _ late: Access control list (ACL) template configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the access control list (ACL) template configuratio n used by mario is of the latest version. | Yes | Yes |
|   | acl whit _ elist: ACL whitelist configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the ACL whitelist configuratio n used by mario is of the latest version. | Yes | Yes |
|   | acl data _ config: _ ACL data configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the ACL data configuratio n used by mario is of the latest version. | Yes | Yes |

| tjmon yun _ dun- sema waf- mario versi _ on |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | summar y config: _ summar y configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the summary configuratio n used by mario is of the latest version. | Yes | Yes |
|   | log aggr _ egate co _ nfig: log aggr _ egate configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the log aggrega _ te configuratio n used by mario is of the latest version. | Yes | Yes |
|   | desensiti zation: Data masking configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the data masking configuratio n used by mario is of the latest version. | Yes | Yes |
|   | policy co _ nfig vers _ ion: Custom rule configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the custom rule configuratio n used by detector is of the latest version. | Yes | Yes |

| tjmon yun _ dun- sema waf- detec tor v _ ersio |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | cc confi _ g versio _ n: HTTP flood protectio n configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the HTTP flood protection configuratio n used by detector is of the latest version. | Yes | Yes |
| n |   |   |   |   |   |   |   |   |   |
| tjmon yun _ dun- sema waf- tengi ne ve _ rsion | website _ config v _ ersion: Site configur ation version | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to determine whether the site configuratio n generated by minion is of the latest version. | Yes | Yes |
| - | req dete _ ct count _ time: _ Average detectio n time | Real- time data | ms | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the efficiency of the detection engine. | No | Yes |
| - | req han _ dler tim _ e: Average detectio n latency | Real- time data | ms | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the efficiency of the detection engine. | No | Yes |
| - | detect q _ ps: Detectio n queries per second (QPS) | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | None | No | No |
| - | syn recv _ count: _ Stacked semi- connecti ons | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the efficiency of WAF. | No | Yes |

| - | tcp retra _ n: TCP packet retransm ission | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the efficiency of WAF. | No | No |
|---|---|---|---|---|---|---|---|---|---|
| - | tengine i _ nfo: tengine status | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the status of tengine. | No | No |
| - | tengine _ status: Tengine synchron ization status | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | The metric is used to verify the status of tengine. | No | Yes |
| - | mgt- redis- stat: ApsaraD B for Redis master- replica status | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | This metric is used to determine whether the ApsaraDB for Redis instance does not have a master node. | No | Yes |
| - | redis-db- no- master: ApsaraD B for Redis split- brain | Real- time data | Non e | Host | 1 min ute | None. WAF (minion) writes the metric value to the log file. | This metric is used to determine whether the ApsaraDB for Redis instance encounters a split-brain issue. | No | Yes |

| yund unse maw afapp ngin _ x wor _ ker s _ huttin g do _ wn c _ ount _ mach ine h _ ost | ng work _ er count _ : Whether the number of NGINX workers is close to 1,024 | Real- time data | Non e | Host | 1 min ute | check ng w _ _ orker count _ | This metric is used to verify the status of NGINX. | Yes | Yes |
|---|---|---|---|---|---|---|---|---|---|

**Business alerts**

After you log in to Apsara Uni-manager Operations Console, choose **Monitor&Alert > Alert**
**Management > Alert List** in the top navigation bar. In the alert list, enter **yundun-**
**semawaf** into the **Resource Owner** filter condition to view alerts triggered by WAF.

| Metric | Alert description | Alert thres hold | Nu mb er of tim es the thr esh old is con sec uti vel y exc eed ed to trig ger the aler t | Sev erit y lev el | Impact | Wheth er the faulty host can be locate d based on the alert | Action to perform after the alert is triggered |
|---|---|---|---|---|---|---|---|

| acl temp _ late | The alert is triggered when the backend configuration differs from the frontend configuration . | $acl t _ empl ate st _ atus! =0 | 5 | P3 | Newly added HTTP flood protectio n rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
|---|---|---|---|---|---|---|---|
| acl whit _ elist | The alert is triggered when the backend configuration differs from the frontend configuration . | $acl _ whitel ist st _ atus! =0 | 5 | P3 | Newly added HTTP flood protectio n rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
| acl data _ config _ | The alert is triggered when the backend configuration differs from the frontend configuration . | $acl _ data _ confi g stat _ us!=0 | 5 | P3 | Newly added HTTP flood protectio n rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
| summar y config _ | The alert is triggered when the backend configuration differs from the frontend configuration . | $sum mary confi _ g stat _ us!=0 | 5 | P4 | Newly added custom rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
| log aggr _ egate co _ nfig | The alert is triggered when the backend configuration differs from the frontend configuration . | $log _ aggre gate _ confi g stat _ us!=0 | 5 | P4 | Newly added custom rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |

| desensiti zation | The alert is triggered when the backend configuration differs from the frontend configuration . | $dese nsitiz ation _ status !=0 | 5 | P3 | Newly added data masking rules do not take effect on the mario side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
|---|---|---|---|---|---|---|---|
| policy co _ nfig vers _ ion | The alert is triggered when the backend configuration differs from the frontend configuration . | $polic y con _ fig ve _ rsion _ status !=0 | 5 | P3 | Newly added custom rules do not take effect on the detector side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |
| cc confi _ g versio _ n | The alert is triggered when the backend configuration differs from the frontend configuration . | $cc c _ onfig _ versio n stat _ us!=0 | 5 | P3 | Newly added HTTP flood protectio n rules do not take effect on the detector side. | Yes | The system automatically fixes the issue. If the issue persists after 30 minutes, contact the development team. |

| website _ config v _ ersion | The alert is triggered when the backend configuration differs from the frontend configuration . | $web site c _ onfig _ versio n stat _ us!=0 | 5 | P2 |   | Newly added HTTP flood protectio n rules |   | Common solutions: 1. Check the latest site configuration for any invalid HTTP header. 2. Check the latest site configuration for any invalid SSL protocol. 3. If the number of sites exceeds 3,000, run the time docker |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | time docker |   |
|   |   |   |   |   |   |   | Yes | exec -it nginx - |   |   |
|   |   |   |   |   |   | do not take |   |   |   |   |
|   |   |   |   |   |   |   |   | t |   |   |
|   |   |   |   |   |   | effect on the tengine side. |   |   |   |   |

| req dete _ ct count _ time _ |   | The alert is triggered when the detection threshold is exceeded. |   | >10 |   |   |   |   |   | This alert is triggered |   |   |   | 1. Capture packets received on port 8000 ( tcpdump - |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | tcpdump - |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | i safeline -vnn |   |   |   |
|   |   |   |   |   |   |   |   |   |   | when the |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | -s0 port 8000 -w |   |   |   |
|   |   |   |   |   |   |   |   |   |   | average |   |   |   | /tmp/8000.pcap |   |   |   |
|   |   |   |   |   |   | 5 |   | P2 |   | detection time of the WAF detection engine is abnormal . When the alert is triggered, WAF needs more time to check certain requests. |   | Yes |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | select * |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | from |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | aliyun policy pol _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | This issue may be |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | icyrule order by |   |   |   |
|   |   |   |   |   |   |   |   |   |   | caused |   |   |   | last update time _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | by |   |   |   | desc limit 50; |   |   |   |
|   |   |   |   |   |   |   |   |   |   | improper custom rules. |   |   |   |   |   |   |   |
| req han _ dler tim _ e |   | The alert is triggered when the request processing time is exceeded. |   | >50 |   | 5 |   | P2 |   | Same as above. |   | Yes |   | Same as above. |   |   |   |

|   |   |   |   |   |   |   |   |   |   |   | This alert indicates that the number of semi- connectio ns on a WAF physical machine exceeds the normal level. When |   |   |   | Check the distribution of peering IP addresses when semi-connections are stacked: ss -nt state |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ss -nt state |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | syn-recv \| awk |   |   |
|   |   |   |   |   |   |   |   |   |   |   | this alert |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | {'print $4}' \| awk |   |   |
|   |   |   |   |   |   |   |   |   |   |   | is |   |   |   | -F: '{print $1}' \| |   |   |
|   |   |   |   |   |   |   |   |   |   |   | triggered, |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | sort \| uniq -c \| |   |   |
|   |   |   |   |   |   |   |   |   |   |   | you must |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | pay close |   |   |   | sort -nr \| head -n |   |   |
|   |   |   |   |   |   |   |   |   |   |   | attention |   |   |   | 30 |   |   |
|   |   | check sy _ n recv c _ _ ount |   | The alert is triggered when the detection threshold is exceeded. |   |   | >100 0 | 10 |   | P3 | to the number of semi- connectio ns. This issue may occur when the Linux |   | Yes |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | select |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | count(distinct |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Virtual |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port) from |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Server |   |   |   | aliyun website vipp _ _ |   |   |
|   |   |   |   |   |   |   |   |   |   |   | (LVS) |   |   |   | ortwafportbinding; |   |   |
|   |   |   |   |   |   |   |   |   |   |   | traffic |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | throttling |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | threshold needs to be adjusted because there are excessive sites. |   |   |   |   |   |   |

| tengine _ version | tengine version. | 0 | 5 | P2 | This alert indicates that the latest WAF site configura tion does not take immediat ely due to a synchroni zation failure. | Yes | In most cases, the site encryption algorithm manually specified by the tenant is incorrect. For example, the algorithm contains additional space characters or line breaks. Consequently, the setting fails to pass the syntax check and the latest configuration is not applied. You need to collect the node minion log from the WAF physical machine for detailed information of the error and modify the configuration accordingly. tail -n 100000 /home/safeline/l ogs/minion/minio n.log > minion latest 1w _ _ .log tail -n 100000 /home/safeline/l ogs/management/n ode.log > node latest 1w.l _ _ og |
|---|---|---|---|---|---|---|---|

| detector version _ | Check whether the detector version is the same as that in the database. Valid values: 0: no 1: yes | >0 | 5 | P2 | This alert indicates that the latest WAF rules do not take effect immediat ely due to a synchroni zation failure. | Yes | The detector configuration has multiple versions. In this case, check the details of the alert to confirm the inconsistent versions. Then, check how long does this issue last. Typically, the system will automatically synchronize detector to the latest configuration. If the issue persists, collect the MySQL load and minion logs to troubleshoot. |
|---|---|---|---|---|---|---|---|

| mgt- redis sta _ t | ApsaraDB for Redis master- replica switchover | >1 | 5 | P3 | This alert indicates that ApsaraDB for Redis triggers a master- replica switchov er. If the alert is triggered, MiniRDS resources may be insufficie nt or the loads may be heavy. You need to pay close attention. | Yes | 1. Collect the minion log. Modify the log collection parameters to collect logs generated during the master-replica switchover. You can extend the time range of log collection. tail -n 100000 /home/safeline/l ogs/minion/minio n.log > minion latest 1w _ _ .log journalctl -u minion --no- pager --since '20 minutes ago' 2. Check the disk usage, CPU and memory loads, and locks of MySQL. If MySQL is overloaded or runs out of disk space, ApsaraDB for Redis may trigger a master-replica switchover. 3. Record the environment version, run the inspection script, and collect node status information. 4. Observe the master-replica switchover frequency. Report the preceding information to the technical support. |
|---|---|---|---|---|---|---|---|

|   | redis db _ no mas _ _ ter |   | ApsaraDB for Redis encounters split-brain issue. Consequentl y, no master node is elected. |   | >0 | 3 | P2 | This alert indicates that ApsaraDB for Redis triggers a master- replica switchov er but fails to elect the master node. If this alert is triggered, MiniRDS resources may be insufficie nt or the loads may be heavy. You need to pay close attention. |   | Yes |   | Same as the master- replica switchover alert, you need to observe how long does the issue last. After you collect the relevant information, run the systemctl restart minion command on the WAF physical machine to restore the master and replica nodes. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   | systemctl |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | restart minion |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 1. Log in to the physical machine of the yundun- semawaf.YundunS emawafApp# component. 2. Run the nproc command to view the number of vCPUs. 3. Run the ps -aux |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | ps -aux |   |
|   |   |   |   |   |   |   |   |   |   |   |   | I grep 'nginx: |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | worker' \|grep |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | '203'\| grep -v |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 'shutting down'I |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | grep -v 'grep'\| |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | wc -l command to view the number of workers in the normal state. |   |   |   |
|   |   |   |   |   | >800 | 1 | P1 |   |   | Yes |   |   |   |   |   |

|   |   |   |   |   |   |   | This alert is triggered because sites are frequentl y created, modified, and deleted. |   |   |   |   |   | If the number of normal workers equals half of the number of vCPUs, no action is needed. Do not modify sites frequently within a short period of time in case this issue occurs |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | ng work _ er count _ alarm _ | Determine whether the number of NGINX workers is close to 1,024. |   |   |   |   | As a result, an excessive number of workers of the WAF forwardin g engine remain in the shutting |   |   |   |   |   | again. If the number of workers in the normal state is less than half of the number of cpu cores, the number of workers in the shutting down state is too large when starting a new worker. As a result, the new worker cannot be created. In this case, you need to perform subsequent operations. 4. Run the ps -aux |   |   |   |
|   |   |   |   |   |   |   | down state. This causes traffic forwardin g error. If this alert is triggered, stop the operation |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | ps -aux |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | \| grep |   |   |   |
|   |   |   |   |   |   |   |   |   | n |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | 'nginx:worker'\| |   |   |   |
|   |   |   |   |   |   |   | s |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | grep 'shutting |   |   |   |
|   |   |   |   |   |   |   | performe d on sites |   |   |   |   |   | down'\| wc -l |   |   |   |
|   |   |   | >cpu core _ s * 4 | 3 | P3 |   | immediat ely and perform the correspo nding troublesh ooting action. |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | sudo |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | docker exec |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | tengine kill- |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | stale-worker |   |   |   |
|   |   |   |   |   |   |   |   |   |   | Yes |   |   |   |   |   |   |

|   |   |   |   |   |   |   |   |   |   |   | This alert is triggered because sites are |   |   |   |   |   | 6. Wait 1 minute and run the sudo |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | sudo |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | docker exec |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | se are |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | tengine nginx -s |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | frequentl |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | reload |   | and | ps |   |
|   |   |   |   |   |   |   |   |   |   |   | y created, |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 'nginx: worker' |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | modified, |   | , |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | \|grep '203'\| |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | and |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | deleted. |   |   |   |   |   | grep -v |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | As a |   |   |   |   |   | 'shutting down' |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | result, an |   |   |   |   |   | \| grep -v |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | excessive |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | number |   |   |   |   |   | 'grep'\| wc -l |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | of workers of the WAF forwardin g engine remain in the shutting down state. This |   |   |   |   |   |   |   |   |   |   |

causes traffic

#### 2.4.2 View metrics

forwardin g error. To avoid This topic describes how to view the metrics of Web Application Firewall (WAF). this issue, do

**System metrics**

not modify
1. Log in to the Cloud Shield Operations Center.
sites frequentl
2. In the left-side navigation pane, choose **Monitoring and Alerting > System Monitoring**.
y within a short Monitoring overview: On the **Monitoring Overview** tab, you can view the metrics of period of services provided by Apsara Stack Security, including the service name, description, time. number of metrics, number of abnormal metrics, and service status. WAF system monitoring overview: On the **Application Security > Web Application**
**Firewall** tab, you can view the system metrics, including the CPU utilization, memory
usage, loads, number of TCP connections, and process data. WAF instance system monitoring: Click the **YundunSemawafApp** card to go to the
**Basic Monitoring** tab to view system monitoring details.
On this tab, you can view changes in the CPU utilization, memory usage, loads, number of TCP connections, and process data in **Cluster View** or **Single-server View**. You can select or specify a time range, click the Refresh icon to manually update the monitoring data, or enable Automatic Refresh to allow the system to automatically update the monitoring data.
