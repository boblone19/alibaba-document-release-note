---
title: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response Operations and Maintenance Guide 20241024"
product_version: "V3.18.3"
doc_version: "20241024"
pdf_pages: 17
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response Operations and Maintenance Guide 20241024.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Cloud%20Security%20Network%20Detection%20and%20Response%20Operations%20and%20Maintenance%20Guide%2020241024.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response Operations and Maintenance Guide 20241024

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
- 2 Service status check
  - 2.1 Basic inspection
  - 2.2 Advanced inspection
- 3 Common operations and maintenance
  - 3.1 Restart the beaver_drv process
  - 3.2 Uninstall Network Traffic Monitoring System
  - 3.3 View NDR logs in Log Service
  - 3.4 Access databases
  - 3.5 View the NIC types and status
  - 3.6 Use packet capture tools
  - 3.7 Replay packets
  - 3.8 Query information about a server
  - 3.9 Disable TCP blocking
  - 3.10 Enable TCPDump

cture Management console

## 1 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
cture Management console

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Apsara Infrastructure Management Framework**.

## 2 Service status check

This topic describes how to check the service status of Network Detection Response (NDR).

### 2.1 Basic inspection

The purpose of a basic inspection is to check the service status of Network Detection Response (NDR). This topic describes how to perform a basic inspection.

**Procedure**

## 1 Log on to the Apsara Infrastructure Management console.

2. In the left-side navigation pane, click **Project & Cluster O&M**.
3. On the Project O&M page, enter **BeaverCluster** in the **Project | Cluster** search box.
4. Find the BeaverClusterForTAPSW-A-xx cluster and click **Cluster Details** in the **Actions**
column.
5. On the cluster details page, click the **Services** tab.
6. On the Services tab, enter **yundun-beaver-advance** in the **Service** search box. Then,
check whether the service status is normal.

### 2.2 Advanced inspection

The purpose of an advanced inspection is to check the service status and features of Network Detection Response (NDR). This topic describes how to perform an advanced inspection.

**Procedure**

2. Log on to the two physical servers of Beaver.
i. In the left-side navigation pane, click **Project & Cluster O&M**. ii. On the Project O&M page, enter **BeaverCluster** in the **Project | Cluster** search box. iii. Find the BeaverClusterForTAPSW-A-xx cluster and click **Cluster Details** in the **Actions** column. iv. On the cluster details page, click the **Services** tab. v. On the Services tab, enter **yundun-beaver-advance** in the **Service** search box. Then, click **Details** in the Actions column to go to the service details page. vi. In the **Components** section, click **BeaverAdvance#** to view the detailed information about the component. vii. In the Information of Component BeaverAdvance# section, click the **Instances** tab. On this tab, find the instance whose information you want to view and click **Terminal** in the
**Actions** column.
3. Check the status of Beaver logs.
Run the `sudo tail /var/log/messages` command. If a record is returned, the Beaver logs are normal.
4. Check the status of image traffic.
Run the `sudo cat /dev/shm/beaver_debug_info` command. If the **speed(K)** value in the second-to-last row in the output is not 0, the image traffic is normal.
5. Check the configurations of the protected CIDR block.
Run the `tail -f /dev/shm/banff-<year>-<month>.log` command. Replace <year> with the current year and <month> with the current month. For example, if the current year and month are March 2023, query the banff-2023-03.log file. The CIDR block in the command output is a Server Load Balancer (SLB) or Elastic IP Address (EIP) CIDR block on the classic network. However, if the CIDR block is connected to a customer access switch (CSW), a CIDR block in a virtual private cloud (VPC) is returned.
6. View the status of all NDR processes.
Run the python /opt/beaver/bin/scripts/check_beaver_process.py command. If the client not exist process and server not exist process parameters have no values, all NDR processes are normal.
7. Check configurations of the traffic scrubbing server.
Run the `cat /home/admin/beaver-dj-schedule/conf/dj.conf` command. Check whether the value of the ip parameter in the aliguard_smart field that is not commented out is set to the domain name system (DNS) virtual IP address (VIP) mapped to the aliguard.${global:internet-domain} domain name. Check whether the IP address can be pinged.

## 3 Common operations and maintenance

**maintenance**

### 3.1 Restart the beaver_drv process

**process**

**Background information**

This topic describes how to restart the beaver_drv process.

**Procedure**

1. Log on to a physical server of Beaver.
2. Switch to the root user.
3. Restart the beaver_drv process.
Run the `/home/admin/beaver_drv/bin/beaver_drv.sh stop` command for five times, and then wait until the process automatically starts.

### 3.2 Uninstall Network Traffic Monitoring System

**Monitoring System**

**Background information**

To uninstall Network Traffic Monitoring System, follow the following steps:

**Procedure**

1. Log on to a physical machine of Network Traffic Monitoring System.
2. Switch to the root account.
3. Run the following command to uninstall Network Traffic Monitoring System:

```
 bash /opt/beaver/bin/uninstall.sh
```

### 3.3 View NDR logs in Log Service

This topic describes how to log on to Log Service to view Network Detection Response (NDR) logs.

**Log on to Log Service**

1. Obtain the information that is used to log on to Log Service.

```
cat /beaver.def | grep sls sls_account_accessid=xxxx sls_account_accesskey=xxxxxxx sls_domain_dataendpoint=data.xxxx
```

2. Replace data in the value of the sls_domain_dataendpoint parameter with portal, and then
visit the modified endpoint in a browser.
3. On the logon page, enter the values of the sls_account_accessid and sls_account_accesskey
parameters to log on to Log Service.

**Log Service projects and logstores for NDR**

| Project | Logstore | Description |
|---|---|---|
| tjm-yundun- beaver-common | beavercommon | Stores the monitoring logs of the beavercommon service. |
| tjm-yundun- beaver-advance | beaveradvance | Stores the monitoring logs of the beaveradvance service. |
| ali-beaver- behavior-log | ndr attack behavior _ _ _ dga | Stores the domain generation algorithm (DGA) attack logs of the behavior analysis feature. |
|   | ndr attack behavior l _ _ _ ogin brute crack _ _ | Stores the brute-force attack logs of the behavior analysis feature. |
|   | ndr attack behavior _ _ _ monitor log _ | Stores the process monitoring logs of the behavior analysis feature. |
|   | ndr attack behavior _ _ _ ssl | Stores the SSL logs of the behavior analysis feature. |
|   | ndr attack behavior _ _ _ weak pwd _ | Stores the weak password logs of the behavior analysis feature. |
|   | ndr behavior access _ _ _ stats | Stores the communication status logs of the behavior analysis feature. |
|   | ndr behavior dns whi _ _ _ telist | Stores the DNS whitelist of the behavior analysis feature. |
|   | ndr behavior encrypt _ _ whitelist _ | Stores the encryption whitelist of the behavior analysis feature. |
|   | ndr behavior log _ _ | Stores the raw logs of the behavior analysis feature. |
|   | ndr monitor task det _ _ _ ail log _ | Stores the task monitoring detail logs of the behavior analysis feature. |
|   | ndr web attack check _ _ _ | Stores the attack confirmation logs of the behavior analysis feature. |

| ali-beaver-net- log | ndr log 5tuple _ _ | Stores 5-tuple logs. |
|---|---|---|
|   | ndr log dns _ _ | Stores DNS logs. |
|   | ndr log http _ _ | Stores HTTP logs. |
|   | ndr log protocol _ _ | Stores protocol logs. |
|   | ndr log ssh _ _ | Stores SSH logs. |
|   | ndr log ssl _ _ | Stores SSL logs. |
|   | ndr pcap index _ _ | Stores packet capture (PCAP) logs. |
| ali-beaver-rt- display | ndr attack alert _ _ | Stores the alert logs of the threat detection feature. |
|   | ndr attack log _ _ | Stores the record logs of the threat detection feature. |
|   | ndr reset log _ _ | Stores the blocking logs at layer 4 and layer 7. |

### 3.4 Access databases

This topic describes how to access the three databases on which a Network Detection Response (NDR) server depends from the server.

**NDR database**

```
/opt/beaver/bin/tools/mysql_jifei_ctl
```

**SecureConsole database**

```
/opt/beaver/bin/tools/mysql_secureconsole_ctl
```

**SOC database**

```
/opt/beaver/bin/tools/mysql_yundunsoc_ctl
```

### 3.5 View the NIC types and status

This topic describes how to view the network interface controller (NIC) types, check whether a business NIC is enabled, and view the link status of NICs on a server of Network Detection Response (NDR).

**View the NIC types**

```
lspci | grep net
```

> **Note:** NICs used by NDR servers consist of management NICs and business NICs.
> A management NIC is a local NIC of a server. A management NIC is usually a GE NIC such as the I350 NIC shown in the preceding figure.
> A business NIC is a NIC that receives mirrored traffic. A business NIC is usually a 10GE NIC, such as the 82599ES NIC shown in the preceding figure.

> **Important:** NDR servers use NICs of specific types as business NICs.
> The following NIC types are supported:

```json
["RP2000","RP1000","MT28800","MT27800", "MT27700", "MT27710", "X710", "XL710", "X52 0", "82599ES", "82599EB", "82599"]
```

**Check whether a business NIC is enabled**

```
/home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/ether_ctl --dump
```

> **Note:** Check the values in the link column. If a value in the link column is down, you need to troubleshoot the cable connection or optical module.

**View the link status**

```
/home/admin/beaver_drv/beaver_lib/bvpp_sdk/scripts/bvpp_lldp_info.py
```

> **Note:** You can use the preceding script to view the information about the peer device and port that are connected to the NDR server.

### 3.6 Use packet capture tools

This topic describes the built-in packet capture tools of Network Detection Response (NDR) that are used for troubleshooting.

**DPDK**

```
/home/admin/beaver_drv/bin/example_no_dpdk pkt_desc 1 -1 <IP address>
```

The following logs are generated:

> **Note:** is_v6: indicates whether IPv6 is used. Valid values: 0 and 1. A value of 0 indicates that IPv6 is not used. A value of 1 indicates that IPv6 is used.
> sip: the source IP address.
> dip: the destination IP address.
> sport: the source port.
> dport: the destination port.
> dscp_cxp_id: the hexadecimal value of the VLAN ID. This can be used to determine whether the traffic is on a specific VLAN.
> aliuid: the tenant UID. This can be used to distinguish traffic of different tenants.
> A value of 0 indicates the non-tenant resources, an error in the synchronization of NDR resources, or an error in mirrored traffic.

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

> **Note:** The results of CapTool can be displayed on the screen or stored to packet capture (PCAP) files. However, you cannot distinguish traffic among tenants.

### 3.7 Replay packets

This topic describes how to use DPDK to replay packets. This way, you can test the performance of Network Detection Response (NDR) features.

**Replay command**

```
#/home/admin/beaver_drv/beaver_lib/bvpp_sdk/bvpp/tools/pkt_replay <cap file> <speed> <r
eplay_loops> <Interval> Userage ./pkt_repaly <cap file> <speed(Kpps)> <time(Second), 0 means nolimit> <replay_l oops, 0:replay persist, other replay n times> <Interval time(us) for frame,0 means noli mit>
```

### 3.8 Query information about a server

**server**

This topic describes how to query information about a server.

**Obtain the serial number of a server**

```bash
dmidecode |grep "Serial Number"
# The value of Serial Number in the command ouput is the serial number of the server
```

.

**Query the information about a server**

```bash
curl "localhost:7070/api/v3/column/m.*?m.sn=Serial number of the server"
```

### 3.9 Disable TCP blocking

**This topic is applicable only to Apsara Stack V3.13 or earlier.**

**Background information**

This topic describes how to disable TCP blocking for Beaver.

**Procedure**

1. Log on to a physical server of Beaver.
2. Switch to the root user.
3. Open the /beaver_client.sh file on each server of Beaver, and add a number sign ( `#` ) to
the start of the `./tcp_reset` line to comment out the line.
4. Run the following command on each server of Beaver to disable TCP blocking:

```
 killall tcpreset
```

`p_`

### 3.10 Enable TCPDump

**Background information**

To enable TCPDump for Network Traffic Monitoring System, follow the following steps:

**Procedure**

1. Log on to a physical machine of Network Traffic Monitoring System.
2. Switch to the root account.
3. Run the following command to enable TCPDump:

```
 echo 1 > /proc/ixgbe_debug_dispatch
```

> **Note:** When TCPDump is enabled, the performance of Network Traffic Monitoring System may be affected. We recommend that you run the following command to disable TCPDump after packet capture is complete.

```
 echo 0 > /proc/ixgbe_debug_dispatch
```
