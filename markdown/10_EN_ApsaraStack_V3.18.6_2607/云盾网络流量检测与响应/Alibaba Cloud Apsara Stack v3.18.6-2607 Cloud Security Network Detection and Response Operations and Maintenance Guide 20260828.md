---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 19
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Operations and Maintenance Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%B5%81%E9%87%8F%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Security%20Network%20Detection%20and%20Response%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Operations and Maintenance Guide 20260828

cture Management console

## Log on to the Apsara

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. cture Management console You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the correct username and password.
Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Apsara Infrastructure Management Framework**.

## Service status check

This topic describes how to check the service status of Network Detection Response (NDR).

### Basic inspection

The purpose of a basic inspection is to check the service status of Network Detection and Response (NDR). This topic describes how to perform a basic inspection.
1. Log in to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**.
3. In the **Product | Cluster** search box, enter **BeaverCluster**.
4. Find the `BeaverClusterForTAPSW-A-xx` cluster and click **Cluster Details** in the **Actions**
column.
5. On the cluster details page, click the **Services** tab.
6. On the Services tab, enter **yundun-beaver-advance** in the **Service** search box. Then,
check whether the service status is normal.

### Advanced inspection

The purpose of an advanced inspection is to check the service status and features of Network Detection and Response (NDR). This topic describes how to perform an advanced inspection.
1. Log in to the Apsara Infrastructure Management console.
2. Log in to the two physical servers of NDR.
i. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**.
ii. In the **Product | Cluster** search box, enter **BeaverCluster**. iii. Find the `BeaverClusterForTAPSW-A-xx` cluster and click **Cluster Details** in the **Actions** column. iv. On the cluster details page, click the **Services** tab. v. On the Services tab, enter **yundun-beaver-advance** in the **Service** search box. Then, click **Details** in the **Actions** column to open the service details page. vi. In the **Components** section, click **BeaverAdvance#** to view the detailed information about the component. vii. In the Information of Component BeaverAdvance# section, click the **Instances** tab. On this tab, find the instance whose information you want to view and click **Terminal** in the
**Actions** column.
viii. In the left-side navigation pane, click the node to which you want to log in or the icon. In the dialog box that appears, select **Account Type** and **Server Account**, and then click **OK**. For more information about account types and server accounts, see **Platform O&M >**

**Apsara Infrastructure Management > Web clients > Web Client Logon > Server**

**logon** in Apsara Uni-manager Operations Console User Guide.
3. Check the status of NDR logs.
Run the following commands. If results are returned, the NDR logs are normal. Run the following command to view migrated messages logs: `sudo tail`

```
/home/logs/ndr/messages
```

Run the following command to view management logs: `sudo tail`

```
/home/logs/ndr/ndr_manager.log
```

4. Check the status of mirrored traffic.
Run the `sudo cat /dev/shm/beaver_debug_info` command. If the **speed(K)** value in the second-to-last row in the output is not 0, the traffic mirroring is normal.
5. Check the configurations of the protected CIDR block.
Run the `tail -f /dev/shm/banff-<year>-<month>.log` command. Replace <year> with the current year and <month> with the current month. For example, if the year and month are March 2023, query the banff-2023-03.log file. The CIDR block in the command output is a Server Load Balancer (SLB) or Elastic IP Address (EIP) CIDR block on the classic network. However, if the CIDR block is connected to a customer access switch (CSW), a CIDR block in a virtual private cloud (VPC) is returned.
6. View the status of all NDR processes.
Run the python /opt/beaver/bin/scripts/check_beaver_process.py command. If the client not exist process and server not exist process parameters have no values, all NDR processes are normal.

## Common operations and

**maintenance**

### Restart the beaver_drv

**process**

This topic describes how to restart the beaver_drv process.
1. Log in to the two physical servers of Network Detection and Response (NDR).
2. Switch to the root user.
3. Run the following command to restart the NDR process:
Run the `/home/admin/beaver_drv/bin/beaver_drv.sh stop` command five times, and then wait until the process automatically starts.

### View NDR logs in SLS

This topic describes how to log in to Simple Log Service (SLS) to view Network Detection and Response (NDR) logs.

**Log in to the SLS console**

1. Log in to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Registration Variable**
**Dashboard**.
3. On the **Service Registration Variable Dashboard** page, enter **sls** in the search box, find
the **sls-common** service, click the icon in the **Service Registration** column, and then click the information.
4. In the **Registration Variables** dialog box, obtain the information in the
`sls_portal.endpoint` field, and populate the obtained `sls_portal.endpoint` value into the URL address bar of your browser.
5. Use the AccessKey ID and AccessKey secret to log in to the SLS console.
You can create and obtain the AccessKey ID and AccessKey secret from the **AccessKey**
**Management** page in the **Platform Credential Management (PCM)** console. For more
information, see **Security management > Account security > PCM > AccessKey pair**
**management** in **Apsara Uni-manager Operations Console User Guide** .

**SLS projects and logstores for NDR**

| Project | Logstore | Description |
|---|---|---|
| tjm-yundun-beaver- common | beavercommon | Stores the monitoring logs of the beavercommon service. |

| tjm-yundun-beaver- advance | beaveradvance | Stores the monitoring logs of the beaveradvance service. |
|---|---|---|
| ali-beaver-behavior-log | ndr attack behavior dga _ _ _ | Stores the domain generation algorithm (DGA) attack logs of the behavior analysis feature. |
|   | ndr attack behavior login brute cra _ _ _ _ _ ck | Stores the brute-force attack logs of the behavior analysis feature. |
|   | ndr attack behavior monitor log _ _ _ _ | Stores the process monitoring logs of the behavior analysis feature. |
|   | ndr attack behavior ssl _ _ _ | Stores the SSL logs of the behavior analysis feature. |
|   | ndr attack behavior weak pwd _ _ _ _ | Stores the weak password logs of the behavior analysis feature. |
|   | ndr behavior access stats _ _ _ | Stores the communication status logs of the behavior analysis feature. |
|   | ndr behavior dns whitelist _ _ _ | Stores the DNS whitelist of the behavior analysis feature. |
|   | ndr behavior encrypt whitelist _ _ _ | Stores the encryption whitelist of the behavior analysis feature. |
|   | ndr behavior log _ _ | Stores the raw logs of the behavior analysis feature. |

|   | ndr monitor task detail log _ _ _ _ | Stores the task monitoring detail logs of the behavior analysis feature. |
|---|---|---|
|   | ndr web attack check _ _ _ | Stores the attack confirmation logs of the behavior analysis feature. |
|   | ndr log 5tuple _ _ | Stores 5-tuple logs. |
|   | ndr log dns _ _ | Stores DNS logs. |
|   | ndr log http _ _ | Stores HTTP logs. |
|   | ndr log protocol _ _ | Stores protocol logs. |
|   | ndr log ssh _ _ | Stores SSH logs. |
|   | ndr log ssl _ _ | Stores SSL logs. |
|   | ndr pcap index _ _ | Stores packet capture (PCAP) logs. |
|   | odl beaver log dns _ _ _ | Stores DNS logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
| ali-beaver-net-log | odl beaver log http request _ _ _ _ | Stores HTTP request logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
|   | odl beaver log http response _ _ _ _ | Stores HTTP response logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |

|   | odl beaver log mysql _ _ _ | Stores MySQL logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
|---|---|---|
|   | odl beaver log sla _ _ _ | Stores SLA logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
|   | odl beaver log tcp session _ _ _ _ | Stores TCP logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
|   | odl beaver log udp session _ _ _ _ | Stores UDP logs. This Logstore is used in Apsara Stack V3.17 and has been discontinued. |
|   | beaver cc detail _ _ | Stores Layer-4 threat detection logs. This Logstore is used in Apsara Stack V3.16 and has been discontinued. |
|   | beaver rtds scan _ _ | Stores Layer-7 threat detection logs. This Logstore is used in Apsara Stack V3.16 and has been discontinued. |
| ali-beaver-rt-display |   |   |
|   | ndr attack alert _ _ | Stores the alert logs of the threat detection feature. |
|   | ndr attack log _ _ | Stores the record logs of the threat detection feature. |

|   | slb https access log _ _ _ | Stores HTTPS-based Server Load Balancer (SLB) access logs. This Logstore is used in Apsara Stack V3.16 and has been discontinued. |
|---|---|---|
| ali-beaver-reset-log | ndr reset log _ _ | Stores the blocking logs at Layer 4 and Layer 7. |

### Access databases

This topic describes how to access the three databases on which a Network Detection and Response (NDR) server depends from the NDR server.
1. Log in to the two physical servers of NDR.
2. Run the following command to access the NDR database:

```
/opt/beaver/bin/tools/mysql_jifei_ctl
```

### View the NIC types and status

This topic describes how to view the network interface controller (NIC) types, check whether a business NIC is enabled, and view the link status of NICs on a server of Network Detection and Response (NDR).
1. Log in to the two physical servers of Network Detection and Response (NDR).
2. Run the following command to view the network interface controller (NIC) types and status.

**View the NIC types**

```
lspci | grep net
```

NICs used by NDR servers consist of management NICs and business NICs. A management NIC is a local NIC of a server. A management NIC is usually a GE NIC, such as the I350 NIC shown in the preceding figure. A business NIC is a NIC that receives mirrored traffic. A business NIC is usually a 10GE NIC, such as the 82599ES NIC shown in the preceding figure. NDR servers use NICs of specific types as business NICs. The following NIC types are supported:

```json
["RP2000","RP1000","MT28800","MT27800", "MT27700", "MT27710", "X710", "XL710" , "X520", "82599ES", "82599EB", "82599"]
```

**Check whether a business NIC is enabled**

```
/home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/ether_ctl --dump
```

Check the values in the `link` column. If a value in the link column is `down` , you need to troubleshoot the cable connection or optical module.

**View the link status**

```
/home/admin/beaver_drv/beaver_lib/bvpp_sdk/scripts/bvpp_lldp_info.py
```

You can use the preceding script to view the information about the peer device and port that are connected to the NDR server.

### Use packet capture tools

This topic describes the built-in packet capture tools of Network Detection and Response (NDR) that are used for troubleshooting.
1. Log in to the two physical servers of NDR.
2. Troubleshoot the issue based on the following descriptions of packet capture tools.

**DPDK**

```
/home/admin/beaver_drv/bin/example_no_dpdk pkt_desc 1 -1 <IP address>
```

The following logs are generated: `is_v6` : indicates whether IPv6 is used. Valid values: 0 and 1. A value of `0` indicates that IPv6 is not used. A value of `1` indicates that IPv6 is used. `sip` : the source IP address. `dip` : the destination IP address. `sport` : the source port. `dport` : the destination port. `dscp_cxp_id` : the hexadecimal value of the VLAN ID. This can be used to determine whether the traffic is on a specific VLAN. `aliuid` : the tenant UID. This can be used to distinguish the traffic of different tenants. A value of 0 indicates the non-tenant resources, an error in the synchronization of NDR resources, or an error in mirrored traffic.

**CapTool**

```
#/home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/captool
CapTool git info: 691f6a7, compile at 2022-02-23 19:32:40 must specific the action param, dump to screen or dump to file Usage: /home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/captool --time [0-3600], 0 means infinite, default 0
         --count [0-10000], 0 means infinite, default 0
         --intf [0-63]
         --vlan [0-4095]
         --core [0-63]
         --ether [0xXXXX]]
         --tunnel-id [xxxxx]
         --proto [0-255]]
         --src-ip [src ipaddr]
         --dst-ip [dst ipaddr]
         --ip [dst or src ipaddr]
         --port [0-65535]
         --inner-proto [0-255]]
         --inner-src-ip [inner src ipaddr]
         --inner-dst-ip [inner dst ipaddr]
         --inner-ip [inner dst or src ipaddr]
         --inner-port [0-65535]
         --direction
rx|tx|drop|kernel|pre_routing|local_in|post_routing|pre_routing6|local_in6|post_routing6
         --file     file path to write in cap format
         --screen   dump to screen
         --unix    capture on which master, default main
         --stop
         --help
         --version
```

The results of CapTool can be displayed on the screen or stored to packet capture (PCAP) files. However, you cannot distinguish traffic among tenants.

### Replay packets

This topic describes how to use DPDK to replay packets. This way, you can test the performance of Network Detection and Response (NDR) features.
1. Log in to the two physical servers of NDR.
2. Run the following command to replay packets.

**Replay commands**

```
#/home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/pkt_replay <cap file> <speed> <r
eplay_loops> <Interval> Userage ./pkt_repaly <cap file> <speed(Kpps)> <time(Second), 0 means nolimit> <replay_l oops, 0:replay persist, other replay n times> <Interval time(us) for frame,0 means noli mit>
```

### Query information about a

**server**

This topic describes how to query information about a server.
1. Log in to the two physical servers of Network Detection and Response (NDR).
2. Run the following commands to query information about a server.

**Obtain the serial number of a server**

```bash
dmidecode |grep "Serial Number"
# The value of Serial Number in the command output is the serial number of the server.
```

**Query the information about a server**

```bash
curl "localhost:7070/api/v3/column/m.*?m.sn=Serial number of the server"
```
