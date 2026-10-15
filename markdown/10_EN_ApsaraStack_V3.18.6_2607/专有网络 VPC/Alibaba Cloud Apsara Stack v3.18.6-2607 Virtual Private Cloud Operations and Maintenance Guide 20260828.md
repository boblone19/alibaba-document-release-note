---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 126
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Operations and Maintenance Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Virtual%20Private%20Cloud%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Operations and Maintenance Guide 20260828

ager Operations Console

## Log on to the Apsara Uni-

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the username and password.
ager Operations Console

**Note**

Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

## Dashboard

### Overview

The Overview page displays the key metrics of network services to help users keep track of the status of services and devices at the earliest opportunity.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Dashboard** > **Overview**.
4. On the **Overview** page, view the following information.

**Alert Dashboard**

| Section | Description |
|---|---|
| Alert Overview | Alert Distribution: displays the total number of alerts triggered by network devices and the distribution of resources that have triggered alerts. Alerts: displays information about alerts of the P1 and P2 levels in the network event center. The alert information includes Event Name/Code, Description, Associated Alert Object, Source Type, Alert Source, Alert Type, Alert Level, Alerts, Clear or Not, Triggered At, Cleared At, Auto-clearing Cycle, and Auto-cleared At. In the upper-right corner, click View Details. In the Alerts dialog box, you can view the list of alerts. Advanced Filter: You can search for alerts by Name, Associated Alert Object, Alert Level, Source Type, Alert Source, Associated Event Code, or their combinations. Find the alert that you want to view and clickD etails in the Details column. In the Event Details dialog box, you can view the details of the alert. |

| Port Overview | Port Usage: displays the port usage of network devices. In the upper-right corner, click View Details. In the Port Usage Details dialog box, you can view the port usage details. The port usage details are displayed in the following columns: Device Role, Device Name, IP Address, Usage (%), Device Status, Total Ports, and Used Ports. Health Distribution of Optical Modules: displays the distribution of optical transceiver modules on the current day. Abnormal Optical Modules: displays information about optical transceiver modules in the Exception state by default. The displayed information includes Hostname, Interface name, Ownership Type, Manufacturer, Model, Status, Failure probability, Expected residual life, and Intelligent analysis results. Click View Details in the upper-right corner. Then, you can view information about abnormal optical transceiver modules in the Abnormal Optical Modules dialog box. Advanced Filter: You can search for optical transceiver modules by Optical module model, Optical module manufacturer, Optical module status, Hostname, Interface name, Device type, or their combinations. Find the optical transceiver module that you want to view and click Details in the Actions column. Then, you are redirected to Intelligent Diagnostics > Optical Module Diagnostics. On the Optical Module Prediction Details page, you can view the details of the optical transceiver module. For more information, see Optical transceiver module diagnostics. |
|---|---|
| Traffic Dashboard | By default, the information about SLB Cluster Usage Overview and XGW Cluster Usage Overview within the last 1 Hour is displayed. For more information about the metrics, see the "Usage metrics on the traffic dashboard" section in the Overview topic. You can click Last 1 Hour, 6 Hours, 12 Hours, or 24 Hours to quickly query the historical usage trend charts of SLB and XGW clusters within a specific time range. In the upper-right corner, select the cluster whose usage trend charts you want to view to display and view the usage trend charts. |

**Usage metrics on the traffic dashboard**

|   | Metric | Description |
|---|---|---|
| SLB cluster | InBitsPS | The number of inbound bits per second. |
|   | OutBitsPS | The number of outbound bits per second. |
| XGW cluster | InByteRate | The inbound bandwidth. Unit: bit/s. |
|   | OutByteRate | The outbound bandwidth. Unit: bit/s. |

**TOPN**: Metrics are sorted based on their **Values**, and the top five metrics are displayed
by default. You can filter and display metrics in each region by specifying filter conditions such as Top N, Start Time, End Time, vSwitch, and Port.

| Section | Metric |
|---|---|
| Physical Network | vSwitch CPUs vSwitch Memory vSwitch Ports phy switch port bps (inbound and outbound) _ _ _ phy switch port pps (inbound and outbound) _ _ _ phy switch port error pps (inbound and outbound CRC error _ _ _ _ packets) phy switch port drop pps (inbound and outbound) _ _ _ _ |

| Network Elements | XGW xgw cpu usage _ _ xgw huge mem usage _ _ _ xgw port bps (inbound and outbound) _ _ xgw port pps (inbound and outbound) _ _ xgw port drop pps (inbound and outbound) _ _ _ LVS lvs connsPS _ lvs dropConnPS _ lvs failConnPS _ lvs connections _ lvs BitsPS (inbound and outbound) _ lvs PktsPS (inbound and outbound) _ lvs DropPktsPS (inbound and outbound) _ SLB PROXY _ proxy requests _ PROXY qps proxy rt _ proxy cps _ proxy handle ps _ _ proxy conn active _ _ AVS avs cpu _ avs phyif in drop pps _ _ _ _ avs phyif in buffer missed errors pps _ _ _ _ _ _ avs vport tcp connecting flows cps _ _ _ _ _ avs vport tcp established flows _ _ _ _ avs phyif bps (inbound and outbound) _ _ avs phyif pps (inbound and outbound) _ _ avs phyif error pps (inbound and outbound) _ _ _ |
|---|---|

| Network Resources | EIP xgw eip bps (inbound and outbound) _ _ xgw eip pps (inbound and outbound) _ _ Reverse Access xgw ecs maping bps (inbound and outbound) _ _ _ xgw ecs mapping pps (inbound and outbound) _ _ _ xgw ecs mapping ratelimit drop pps (inbound and outbound) _ _ _ _ _ xgw ecs mapping drop pps (inbound and outbound) _ _ _ _ NATGW xgw snat session count _ _ _ xgw snat session drop cps _ _ _ _ xgw snat session ratelimit drop cps _ _ _ _ _ vlink xgw vlink bps (inbound and outbound) _ _ xgw vlink pps (inbound and outbound) _ _ Layer 4 VIP lvs listener connsPS/lvs realserver connsPS _ _ _ _ lvs listener dropConnPS/lvs realserver dropConnPS _ _ _ _ lvs listener connections 1m/lvs realserver connections 1m _ _ _ _ _ _ lvs listener PktsPS (inbound and _ _ outbound)/lvs realserver PktsPS (inbound and outbound) _ _ lvs listener BitsPS (inbound and _ _ outbound)/lvs realserver BitsPS (inbound and outbound) _ _ lvs listener DropPktsPS (inbound and _ _ outbound)/lvs realserver DropBitsPS (inbound and outbound) _ _ Layer 7 VIP proxy listener cps _ _ proxy listener qps _ _ proxy listener rt _ _ proxy listener conn concurrent _ _ _ vport avs vport tcp connecting flows num sum 1m _ _ _ _ _ _ _ avs vport tcp established flows num sum 1m _ _ _ _ _ _ _ avs vport pkts 1m (inbound and outbound) _ _ _ avs vport bytes 1m (inbound and outbound) _ _ _ avs vport drop pkts 1m (inbound and outbound) _ _ _ _ |
|---|---|

### Network topology

On the Network Topology page, you can view the physical network topology.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Dashboard** > **Network Topology**.
4. Select a data center from the **Data Center** drop-down list and view the physical network
topology of the selected data center. Click **Baseline topology** or **Dynamic Topology** to view the network topology of the corresponding type. If the **dynamic topology** or the **base topology** has data discrepancies, you can click
**Update topology** to update the topology.
Network devices displayed in different colors are in different states. Blue: A device is in a normal state. Orange: A device is in an abnormal state. If you choose to display the **baseline topology**, the **Real-time alert refresh** feature is available. If you do not enable this feature, the states of devices and links in the topology are not updated when an alert is generated. If you choose to display the **dynamic topology**, the **Real-time alert refresh** feature is not available.
5. View the network device information and interconnection link statuses.
Click a network device icon. In the Network Device Information panel, view the device information in the **Basic device information** and **Alert List** sections. Click a connection between two network devices. In the Interconnection link status panel, view the link status details in the **Link information List** and **Alert List** sections.

### Custom views

The Apsara Uni-manager Operations Console allows you to create a custom view. After the view is created, you can configure the content and rules of the view to summarize and demonstrate the monitoring data and graph information based on your business requirements.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.

**Create a view**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Dashboard** > **Custom Views**.
4. On the Custom Views page, click **Create View**.
5. In the Create View dialog box, configure the **View Name** and **View Description**
parameters, and then click **OK**. After the view is created, the page of the view automatically appears.

**Note**

The view name must be unique. If the **Data Already Existing** message appears, you must change the view name, and then click **OK** when no name conflict occurs.
6. Create a subview.
i. Click the icon in the view section. ii. In the Create Subview panel, configure the following parameters and click **OK**. After the subview is created, the page of the view automatically appears, on which the subview is displayed.

| Parameter | Description |
|---|---|
| Device | The device to be monitored. |
| Monitoring Type | The type of the monitoring metric. Valid values: interface: the switch interface, including the water level, packet error, and packet loss of the interface. hardware: the switch hardware, including the memory usage and CPU usage. capacity: others. This option is not supported. |
| Metric | The monitoring metric. |
| Submetric | The monitoring submetric. |

iii. You can create more subviews by repeating Step 6.

**Query a view**

1. In the upper part of the Custom Views page, select a view name from the drop-down list,
specify a time range, and then click **Search**.
2. The Custom Views page displays the monitoring charts of all the corresponding subviews.

**Delete a view**

**Delete a subview**

1. Search for the view that you want to manage.
2. Find the subview that you want to delete and click the
icon in the upper-right corner of the subview section.
3. In the message that appears, click **OK**.

**Delete a view**

**Important**

If you delete a view, all subviews of the view are also deleted. Proceed with caution.
1. Search for the view that you want to delete.
2. In the upper-right corner of the view section, click **Delete View**.
3. In the message that appears, click **OK**.

## Basic network

### Network element

**management**

Network elements are network devices such as vSwitches and routers. The Network Element Management module displays the basic information and status of physical network devices. The module also supports configuration management operations on physical network devices, including device management, password management, and configuration consistency comparison. For more information about the features of the Network Operations Console that are applicable to device manufacturers, see vSwitch Monitoring Capabilities Supported by Network Operations Console.

**Manage devices**

On the Device Management tab, you can view the monitoring information about physical network devices and configure collection settings for them.

**Manage network monitoring data**

**Background information**

On the **Network Monitoring** tab, you can view the basic information, status, and traffic monitoring information of physical network devices in Apsara Stack to stay updated with their health status.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the **Network Monitoring** tab of the **Device Management** tab, specify the **IDC**
parameter to view the physical network devices in Apsara Stack. You can view information about the physical network devices in the columns, including
**Device Name**, **Management IP address**, **SN**, **Business Domain**, **Vendor**, **Model**, **Role**,
**Online Time**, **Ping status**, **Snmp status**, and **Last Updated**.

**Note**

You can click **Export** in the upper-right corner of the Network Monitoring tab to export the information about the physical network devices to your computer. If the ping or Simple Network Management Protocol (SNMP) is abnormal, Unreachable in red is displayed in the **Ping status** or **Snmp status** column. In the upper-right corner of the Network Monitoring tab, you can enter a device name or an IP address in the search box to search for the physical network device, and then view its information. The **Management IP address**, **Ping status**, and **Snmp status** columns can be used to sort the physical network devices. The **Role** column can be used to filter the physical network devices.
5. Find the physical network device that you want to view and click its name or click **Details**
in the **Details** column to view the details of the physical network device. The following table describes the details of the physical network device.

| Section or tab | Description |
|---|---|
| Basic information | View the information about the device from the parameters, including Device Name, IP, SN, Vendor, Model, Role, Online time, Ping status, Snmp status, Last Updated, Release, and Software version. |

| Port | View the information about the ports of the device in the columns, including Port Name, Port rate, Port description, Management status, Operation Status, Peer Device, Peer interface, Peer description, and Last Updated. Note The Management status and Operation Status columns can be used to sort the ports of a device. If exceptions occur, Down in red is displayed in the Management status or Operation Status column. View the details of a port. a. Find the port that you want to view and click its name or clickS ee in the Details column to view the details of the port. b. View the basic information and usage data of the port. In the Water level data section, you can select a time range in the Quick query section or specify a custom time range in the upper-right corner to query traffic data within the specified time range. |
|---|---|

| CPU usage | View the CPU utilization of the device. |
|---|---|
| Memory usage | View the memory usage of the device. |

| Aggregation Port Management | View the information about all aggregation ports of the device. On the Aggregation Port Management tab, find the aggregation port that you want to view and click See in the Operation column to view the usage data of the aggregation port. |
|---|---|

| Alert information | View the alert information about the device. Note During routine O&M, you need to view the alert information about a device at the earliest opportunity. If no data is displayed on the Alert information tab, the device is running as expected. If alert events occur, the system displays the alert events that are not handled on the Alert information tab. You need to handle the alert events at the earliest opportunity. |
|---|---|

6. Optional. Delete the monitoring information of the network device.
i. Click **Delete** in the **Details** column of the device. ii. In the message that appears, click **Delete**.

**Configure collection settings**

**Feature description**

On the Collection settings tab, you can set the collection interval of physical network devices and manage out-of-band (OOB) CIDR blocks. Before you collect network device information, you must configure a collection interval. In the OOB CIDR block management section, you can configure the management scope of a physical network device. In most cases, operations engineers must add the loopback CIDR block in which the network device to be managed resides.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**Background information**

If you use the network element management feature of the Network Operations Console for the first time, you must add the loopback CIDR block planned by the current network device in Apsara Stack. In most cases, the loopback CIDR block is the CIDR block specified by the netdev.loopback field in the planned IP address list. To expand the network and the loopback CIDR block, you must add the CIDR block involved in the expansion to the management scope. The procedure to add an expanded CIDR block is the same as that used to add the loopback CIDR block for the first time. Then, you can search for the CIDR block of the managed device on the Collection settings tab.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the **Device Management** tab, click the **Collection settings** tab.

| Section | Description |
|---|---|
| Collection cycle settings | i. In the Collection cycle settings section, configure the Automatic scan cycle (minutes), Device scan cycle (minutes), Port scan cycle (minutes), and Link scan cycle (minutes) parameters. Note If you have no special requirements, we recommend that you use the default values. ii. Click Submitted. Then, the system collects the device information based on your configurations. |
| OOB CIDR block management | Add a CIDR block. a. Click Add CIDR block. b. In the Add CIDR block dialog box, configure the following parameters. Then, click OK. Manage CIDR blocks: Enter an IP address and its subnet mask in CIDR notation. Example: 10.0.0.0/8. Computer room: Select a data center from the drop-down list. Business Domain: Select In-band or Out-of-band from the drop- down list. View CIDR blocks. |

|   | a. In the search box above the CIDR clock list, enter an ID, a management CIDR block, or the name of a data center and click the icon to search for the CIDR block, and then view information about the CIDR block. b. View information about the CIDR blocks in the columns, includingI D, Management CIDR blocks, Computer room, Business Domain, Created, and Last modification. Modify a CIDR block. a. Find the CIDR block that you want to modify and clickE diting in the Operation column. b. In the Modify CIDR block dialog box, modify the parameter settings, and click OK. Delete a CIDR block. a. Find the CIDR block that you want to delete and clickD elete in the Operation column. b. In the message that appears, click OK. |
|---|---|

**Manage passwords**

You can modify the password of a physical network device.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the Network Element Management page, click the Password management tab. On the
**Password management** tab, query current network devices.

**Note**

You can enter a device name in the search box to perform an exact search.
5. Select one or more devices whose passwords you want to modify and click **Add to**
**implementation**. Then, the devices whose passwords you want to modify are displayed in
the **Implementation equipment** section on the right.

**Note**

To remove a device from the **Implementation equipment** section, you can click
**Management** in the **Operation** column of the device, and then select **Delete**. You
can also click **Empty** in the upper-right corner to remove all devices from the Implementation equipment section.
6. In the lower-right corner of the Password management tab, enter values in the **User name**
and **Old password** fields, and click **Verification**. The system verifies the old password before you can modify the passwords.

**Note**

If multiple devices are added to the Implementation equipment section and the old passwords of the devices are different, you need to separately verify the old passwords. After the verification is passed, **Verified** is displayed in the Verification status column.
7. After the verification is passed, modify the passwords for one or more devices.
Modify the password of a device. a. In the Implementation equipment section, find the device whose password you want to modify, click **Management** in the **Operation** column, and then select **Set account**
**password**.
b. In the Set account password dialog box, configure the **User name** and **Password** parameters, and click **OK**. Modify the passwords of all added devices. a. In the lower part of the **Implementation equipment** section, click **Modify**. b. In the dialog box that appears, configure the **User name** and **Password** parameters, and click **OK**.

**Compare configuration consistency for devices**

You can compare the current configurations of a device with its configurations on startup and check whether the configurations are consistent.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and has reached the desired state.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. On the Network Element Management page, click the **Configuration consistency**
**comparison** tab. On the Configuration consistency comparison tab, view the information
about the network devices in the columns, including **Device Name**, **Device**
**Manufacturer**, **Device logon IP address**, and **Result**.

**Note**

You can enter a device name in the search box to perform an exact search.
5. Select one or more devices whose configurations you want to compare and click
**Consistency comparison**.
Click **Refresh status** to update the comparison status. Click **Export result** to export the comparison results to your computer for viewing.

### Syslog

The Syslog module records and stores the logs generated by network hardware devices in the system based on dimensions such as time, log level, and module to facilitate subsequent analysis and management. This helps you identify and solve issues to improve the availability and stability of devices.

**View logs**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** >**Syslog**.
4. On the Syslog page, click **Advanced Filter**. Then, configure the **Data Center**, **Source**
**Device**, **Recorded At**, **Log Content**, **Parsing Status**, **Log Level**, **Manufacturer**, and
**Alert Module** parameters to filter logs.
5. View the information about the logs that meet the filter conditions in the columns that are
described in the following table.

| Column | Description |
|---|---|
| Recorded At | The time when the log entry was recorded. You can sort log entries based on the column. |
| Log Content | The parsed log data, which is the content of the raw log. |

| erations and Maintena Basic network | nce Gui Virtual Private Cloud |
|---|---|

| Source Device | The source device from which the log data was collected. |
|---|---|
| Parsing Status | The parsing status of log data. Valid values: Parsed and Parsing Failed. Note Logs may fail to be parsed due to the following reasons: The log format does not meet the RFC 3164 specification. The network device from which the log data was collected is not produced by an asset-heavy manufacturer that is supported by Apsara Stack. |
| Log Level | The level of the log data. Valid values: Emergency, Alert, Serious, Error, Warning, Notification, Information, and Debugging. |
| Module | The module to which the log data belongs. |
| Raw Logs | The raw log data that is not parsed. |
| Manufacturer | The manufacturer of the network device. |

6. Find the log entry that you want to view and click **Details** in the Operation column. In the
Syslog Details panel, view more detailed information about the log, such as the alert matching results, module details, and location.

**What to do next**

**Export logs**

On the Syslog page, click **Export Logs** in the upper-left corner to export the logs to your computer for viewing.

**Note**

By default, all logs are exported.

**Test the log parsing feature**

1. On the Syslog page, click **Test Analysis** in the upper-left corner.
2. In the Test Analysis dialog box, enter content in the **Original Text** field and click **Submit**.

**Note**

If you click **Reset**, the content in the Original Text field is cleared.
3. In the Parsing Results section, view the parsed information, such as the description,
hostname, and log level.

## Networking services

### XGW O&M

#### XGW cluster management

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **XGW Cluster**
**Management**.
4. On the XGW Cluster Management page, select a region ID from the **Region** drop-down list
and click **Synchronize data** to obtain the latest data of the XGW cluster list.
5. Find the cluster that you want to manage, click **Quick Settings** in the **Operation** column,
and then select **Set backup zone**.

**Note**

The cluster that you select as the secondary zone must have the same architecture and reside in the same region as the current cluster. Click **Set backup zone**. Then, the system checks the data. After the data is checked, you can configure a secondary zone.
6. Select a secondary zone from the Select backup zone drop-down list and click **OK**.

#### XGW management

The XGW Management module allows you to manage VPC gateways and view the water level information of device nodes and service instances.

#### NAT gateway monitoring

In scenarios such as multi-cloud geo-disaster recovery and hybrid cloud, you can query the monitoring data of a NAT gateway by tunnel ID.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **NAT**
**Gateway Monitoring**.
4. On the NAT Gateway Monitoring page, select a cluster, specify a time range, enter the
tunnel ID, and then click **Query** to view the trend chart of the NAT gateway.

**Note**

You can move the pointer over a point in time in the chart to view the corresponding monitoring data. The following table describes the metrics displayed in the chart.

| Metric | Description |
|---|---|
| CurrNum | The number of connected instances. |
| EstablishRate | The number of connections that are established per second. |
| RatelimitDrop | The number of packets dropped due to throttling. |
| CapacityDropInc | The number of packets dropped due to the Inc capacity limit. |
| CapacityDrop | The number of packets dropped due to the capacity limit. |

| IninNum | The number of initialized instances. |
|---|---|
| RatelimitDropInc | The number of packets dropped due to the Inc throttling. |

#### Router interface instances

This topic describes how to view the instances of a router interface and the O&M information about the instances.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Products** > **XGW O&M** > **RI Instances**.
4. On the RI Instances page, click Advanced Filter. In the **Search Condition** section, select
**VPC ID** or **UID** from the drop-down list and enter the corresponding value in the field.
5. Optional. Specify the **Connection Type**, **RI ID**, **Router Type**, **Router ID**, **Instance State**,
**Instance Name**, **Peer RI ID**, **Peer Router ID**, **Peer Router Type**, and **Peer Region ID**
parameters to filter router interface instances.
6. Click **Search**. The router interface instances that match the UID are displayed on the RI
Instances page.

**Note**

If you select **VPC ID** from the drop-down list in the **Search Condition** section, all router interface instances that belong to the virtual private cloud (VPC) are automatically queried.
7. Find the router interface instance that you want to manage and click **Details** in the
**Operation** column. On the details page, view the detailed O&M information about the
router interface instance. If usage data exists, the usage data is also displayed on the page.

### AVS O&M

#### AVS management

The Apsara virtual switch (AVS) management feature allows you to view the basic information and usage dashboard of AVSes.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Products** > **AVS O&M** > **AVS**
**Management**.
4. On the AVS management page, you can view the ASV information in the following columns:
**Hostname**, **NC IP**, **Kernel version**, **pync version**, **rpm version**, **Version mvssSDK**, and
**vtools version**.
5. Find the AVS that you want to manage and click **Details** in the **Operation** column. On the
page that appears, view the monitoring data in the **netdev traffic**, **CPU usage**, **Total**
**vport traffic**, **vxlanVport total traffic**, and **Physical Nic traffic** sections.
The following table describes the metrics.

| Category |   | Metric | Description |
|---|---|---|---|
| netdev traffic | Flow | if ipackets sum _ _ | The number of packets that the network interface controller (NIC) receives per second. |
|   |   | if opackets sum _ _ | The number of packets that the NIC sends per second. |
|   |   | if idrop sum _ _ | The number of NIC inbound packets that are dropped per second. |
|   |   | if odrop sum _ _ | The number of NIC outbound packets that are dropped per second. |
|   | BandWidth | if ibytes sum _ _ | The number of bytes that the NIC receives per second. |
|   |   | if obytes sum _ _ | The number of bytes that the NIC sends per second. |
| CPU usage |   | usage avg _ | The average CPU utilization. |
|   |   | usage min _ | The minimum CPU utilization. |
| Document Version: 20260828 |   | 3 |   |

| erations and Maintenance Gui Networking services |   |   |   |
|---|---|---|---|
|   |   | usage max _ | The maximum CPU utilization. |
|   | Flow | rx packets sum _ _ | The number of inbound packets per second. |
|   |   | rx dropped sum _ _ | The number of inbound packets that are dropped per second. |
|   |   | tx packets sum _ _ | The number of outbound packets per second. |
|   |   | tx dropped sum _ _ | The number of outbound packets that are dropped per second. |
|   |   | slb tx packets sum _ _ _ | The number of packets that Server Load Balancer (SLB) sends per second. |
|   |   | slb tx dropped sum _ _ _ | The number of SLB outbound packets that are dropped per second. |
|   |   | slb rx packets sum _ _ _ | The number of packets that SLB receives per second. |
|   |   | slb rx dropped sum _ _ _ | The number of SLB inbound packets that are dropped per second. |
|   |   | rx pps limit error sum _ _ _ _ | The number of inbound packets that are dropped due to throttling per second. |
|   |   | tx pps limit error sum _ _ _ _ | The number of outbound packets that are dropped due to throttling per second. |
|   |   | rx acl error sum _ _ _ | The number of inbound packets that are dropped from the security group per second. |

|   |   | tx acl error sum _ _ _ | The number of outbound packets that are dropped from the security group per second. |
|---|---|---|---|
|   |   | ipv6 tx packets sum _ _ _ | The number of packets that IPv6 clients send per second. |
|   |   | ipv6 tx acl error sum _ _ _ _ | The number of IPv6 outbound packets that are dropped from the security group per second. |
|   |   | ipv6 rx packets sum _ _ _ | The number of packets that IPv6 clients receive per second. |
|   |   | ipv6 rx acl error sum _ _ _ _ | The number of IPv6 inbound packets that are dropped from the security group per second. |
|   |   | rx bytes sum _ _ | The number of bytes that are received per second. |
|   |   | rx dropped bytes sum _ _ _ | The number of bytes of inbound packets that are dropped per second. |
|   |   | tx bytes sum _ _ | The number of bytes that are sent per second. |
|   |   | tx dropped bytes sum _ _ _ | The number of bytes of outbound packets that are dropped per second. |
|   | BandWidth |   |   |
|   |   | slb tx bytes sum _ _ _ | The number of bytes that SLB sends per second. |
|   |   | slb tx dropped bytes sum _ _ _ _ | The number of bytes of SLB outbound packets that are dropped per second. |
|   |   | slb rx bytes sum _ _ _ | The number of bytes that SLB receives per second. |

| Total vport traffic |   |   |   |
|---|---|---|---|
|   |   | slb rx dropped bytes sum _ _ _ _ | The number of bytes of SLB inbound packets that are dropped per second. |
|   |   | ipv6 tx bytes sum _ _ _ | The number of bytes that IPv6 clients send per second. |
|   |   | ipv6 rx bytes sum _ _ _ | The number of bytes that IPv6 clients receive per second. |
|   |   | tx igw packets avg _ _ _ | The number of packets that are sent per second in the north-south traffic. |
|   |   | rx igw packets avg _ _ _ | The number of packets that are received per second in the north-south traffic. |
|   | NorthSouthFlow |   |   |
|   |   | ipv6 tx igw packets avg _ _ _ _ | The number of packets that IPv6 clients send per second in the north-south traffic. |
|   |   | ipv6 rx igw packets avg _ _ _ _ | The number of packets that IPv6 clients receive per second in the north-south traffic. |
|   | NorthSouthBandWi dth | tx igw bytes avg _ _ _ | The number of bytes that are sent per second in the north- south traffic. |
|   |   | rx igw bytes avg _ _ _ | The number of bytes that are received per second in the north-south traffic. |
|   |   | ipv6 tx igw bytes avg _ _ _ _ | The number of bytes that IPv6 clients send per second in the north-south traffic. |
|   |   | ipv6 rx igw bytes avg _ _ _ _ | The number of bytes that IPv6 clients receive per second in the north-south traffic. |
|   |   | session count sum _ _ | The total number of fast forwarding connections. |

|   | d |   |   |
|---|---|---|---|
|   | Connect |   |   |
|   |   | slb session count sum _ _ _ | The number of SLB connections. |
|   |   | noconn flows num sum _ _ _ | The number of User Datagram Protocol (UDP) and Internet Control Message Protocol (ICMP) connections. |
|   |   | tcp connecting flows num _ _ _ sum _ | The number of new connections. |
|   |   | tcp established flows num _ _ _ sum _ | The number of concurrent connections. |
|   |   | tcp closing flows num su _ _ _ _ m | The number of connections that are being closed. |
|   |   | tcp closed flows num sum _ _ _ _ | The number of closed connections. |
|   |   | rx session new fail sum _ _ _ _ | The number of inbound connections that fail to be created. |
|   |   | rx session update fail sum _ _ _ _ | The number of inbound connections that fail to be updated. |
|   |   | tx session new fail sum _ _ _ _ | The number of outbound connections that fail to be created. |
|   |   | tx session update fail sum _ _ _ _ | The number of outbound connections that fail to be updated. |
|   |   | tx retrans avg _ _ | The ratio of the number of re-sent outbound packets to the total number of outbound packets. |
|   |   | rx retrans avg _ _ | The ratio of the number of re-sent inbound packets to the total number of inbound packets. |

|   |   | tx igw retrans avg _ _ _ | The ratio of the number of re-sent outbound packets to the total number of outbound packets in the north-south traffic. |
|---|---|---|---|
|   | RetransmissionRat e |   |   |
|   |   | rx igw retrans avg _ _ _ | The ratio of the number of re-sent inbound packets to the total number of inbound packets in the north-south traffic. |
|   |   | ipv6 rx retrans avg _ _ _ | The ratio of the number of re-sent IPv6 outbound packets to the total number of IPv6 outbound packets. |
|   |   | ipv6 tx retrans avg _ _ _ | The ratio of the number of re-sent IPv6 inbound packets to the total number of IPv6 inbound packets. |
|   |   | ipv6 tx igw retrans avg _ _ _ _ | The ratio of the number of re-sent IPv6 outbound packets to the total number of IPv6 outbound packets in the north-south traffic. |
|   |   | ipv6 rx igw retrans avg _ _ _ _ | The ratio of the number of re-sent IPv6 inbound packets to the total number of IPv6 inbound packets in the north- south traffic. |
|   |   | rx packets avg _ _ | The number of inbound packets per second. |
|   |   | tx packets avg _ _ | The number of outbound packets per second. |
|   |   | rx dropped avg _ _ | The number of inbound packets that are dropped per second. |
|   |   | tx dropped avg _ _ | The number of outbound packets that are dropped per second. |

|   |   | rx pps limit error avg _ _ _ _ | The number of inbound packets that are dropped due to packets per second (PPS) throttling per second. |
|---|---|---|---|
|   |   | rx fastpath error avg _ _ _ | The number of inbound packets that are dropped due to fast forwarding per second. |
| vxlanVport total traffic | Flow |   |   |
|   |   | tx pps limit error avg _ _ _ _ | The number of outbound packets that are dropped due to PPS throttling per second. |
|   |   | tx fastpath error avg _ _ _ | The number of outbound packets that are dropped due to fast forwarding per second. |
|   |   | rx cpu limit error avg _ _ _ _ | The number of inbound packets that are dropped due to CPU throttling per second. |
|   |   | tx cpu limit error avg _ _ _ _ | The number of outbound packets that are dropped due to CPU throttling per second. |
|   |   | relay packet err avg _ _ _ | The number of packets that encounter relay errors. |
|   |   | relay packet avg _ _ | The number of packets that are relayed. |
|   |   | rx loc route error avg _ _ _ _ | The number of inbound location table match errors per second. |
|   |   | ipv6 rx loc error avg _ _ _ _ | The number of inbound IPv6 location table match errors per second. |
|   |   | rx bps limit error avg _ _ _ _ | The number of inbound packets that are dropped due to bytes per second (BPS) throttling per second. |

|   | ntenance Gui ices |   |   |
|---|---|---|---|
|   | BandWidth |   |   |
|   |   | tx bps limit error avg _ _ _ _ | The number of outbound packets that are dropped due to BPS throttling per second. |
|   |   | rx bytes avg _ _ | The number of bytes that are received per second. |
|   |   | rx dropped bytes avg _ _ _ | The number of bytes of inbound packets that are dropped per second. |
|   |   | tx bytes avg _ _ | The number of bytes that are sent per second. |
|   |   | tx dropped bytes avg _ _ _ | The number of bytes of outbound packets that are dropped per second. |
| Physical Nic traffic | Flow | rx drop packets avg _ _ _ | The number of inbound packets that are dropped per second. |
|   |   | rx error packets avg _ _ _ | The number of error inbound packets per second. |
|   |   | rx missed errors avg _ _ _ | The number of inbound packets that are dropped in the buffer per second. |
|   |   | rx packets avg _ _ | The number of inbound packets per second. |
|   |   | tx error packets avg _ _ _ | The number of error outbound packets per second. |
|   |   | tx packets avg _ _ | The number of outbound packets per second. |
|   | BandWidth | rx bytes avg _ _ | The number of bytes that are received per second. |
|   |   | tx bytes avg _ _ | The number of bytes that are sent per second. |

### VPC O&M

#### Tiangong VPC

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the navigation pane on the left, choose **Network Products** > **VPC O&M** > **VPC-On-**
**ECS**.
4. On the VPC-On-ECS page, click **Advanced Filter** and then specify the **VPC ID**, **Status**, and
**Created At** parameters to filter virtual private clouds (VPCs).
5. Find a VPC that you want to manage and click its name or **Details** in the **Operation**
column. On the details page of the VPC, you can view the VPC details in the **VPC Instance**
**Information**, **VRouter Information**, and **vSwitches** sections.
6. In the **vSwitches** section, perform the following operations:
Create a vSwitch: Click **Create vSwitch**. In the dialog box that appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| AZone | The ID of the zone to which the vSwitch belongs. |
| CIDR | The IPv4 CIDR block of the vSwitch. |

| Usage | The purpose of the vSwitch. Valid values: Alibaba Cloud Service Container Network |
|---|---|
| Description | The description of the vSwitch. |

Search for vSwitches: Click **Advanced Filter** and then specify the **Instance ID**, **Owner**,
**AZone**, and **Created At** parameters to filter vSwitches.
Delete a vSwitch: Find a vSwitch that you want to delete and click **Delete** in the
**Operation** column. In the dialog box that appears, click **OK**.

**Important**

After you delete a vSwitch, the vSwitch cannot be restored. Proceed with caution.

#### VPC workflows

You can view and manage workflows in the VPC Business Foundation System.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Product O&M** > **Network O&M** > **Network O&M Console**.
3. In the navigation pane on the left, choose **Network Products** > **VPC O&M** > **VPC**
**Workflow**.
4. On the **VPC Workflow** page, configure the parameters to query process tasks, and then
click **OK**.

| Parameter | Description |
|---|---|
| Workflow Name | Enter a custom workflow name. |
| Execution Status | Select the execution status of the task. ALL: All statuses. SCHEDULABLE: Schedulable. RUNNING: Running. PAUSED: Paused. HUMAN PROCESSING: Manual intervention required. _ COMPLETED: Completed. FAILED: Failed. TIMEOUT: Timed out. |
| Request ID | Enter the request ID of the task. |
| AliUid | Enter the ID of your Alibaba Cloud account. |
| InstanceId | Enter the ID of the instance that the current workflow operates on. |

The process tasks that match the filter criteria are displayed in the **List** area.
5. In the **Workflow List** area, find the target process task and click **Details** in the **Actions**
column. On the **Workflow Details** page, you can view information about the process task, such as its activity name, method, and failure reason.
6. (Optional) In the **Workflow List** area, find the target process task. In the **Actions** column,
click **Stop** to end a running workflow or **Retry** to run the workflow again. ng

## Network monitoring and

**alerting**

### Network event center

This topic describes how to query all events in the network event center, including INSPECT, SYSLOG, and NOEPING events.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Event Center**.
4. On the **Network Event Center** page, you can view the events and event content,
including **Event Name/Code**, **Description**, **Associated Object**, **Event Source Type**,
**Associated Task**, **Type**, **Level**, **Converted Alert**, **Occurrences, Occurred At**, and **Last**
**Reported At**.
Click **Advanced Filter** to search for events based on a combination of **Time**, **Name**,
**Associated Object**, **Level**, **Event Source Type**, **Event Type**, and **Event Code**.
5. Find the event that you want to view and click **Details** in the **Actions** column to view the
**event details**. Details of RECOVER events are unavailable.
The event details include **Event Information** and **Event content**. Content of VALUE events is not displayed. The event details vary based on the event type. The displayed information prevails. ng

### Network event configurations

This topic describes how to modify and manage event generation rules in the network event configuration center of Apsara Stack. You can create, import, clone, modify, and delete event generation rules.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Monitoring & Alerting** > **Network**
**Event Configuration**.
4. You can view information about event generation rules on the **Network Event**
**Configurations** page, including **Event Name**, **Description**, **Event Level**, **Type**, **Event**
**Source, Event Code**, **Event Dimension**, **Status**, **Converted Alert**, **Automatic**
**Recovery Time, and Event Group**.
Click **Advanced Filter** to search for event generation rules based on a combination of
**Name**, **Event Level**, **Event Source**, **Event Code**, **Status**, and **Converted Alert**.
You can select the following event sources from the **Event Source** drop-down list:
**INSPECT**: the NOE inspection platform.
**SYSLOG**: the vSwitch syslog.
**NOEPING**: NOEPING-based connectivity check.
**EVENT_CENTER**: the NOE event center, where the same events are generated.
ng
**NOE_TSDB**: the NOE time series database.
**NOE_GRPC**: NOE gRPC.
5. You can also perform the following operations on the **Network Event Configurations**
page:

**Create an event generation rule**

In the upper-left corner of the Network Event Configurations page, click **Create Rule** above the list. On the **Create Event** page, configure the following parameters and click
**Create**.

| Parameter | Description |
|---|---|
| Basic Settings |   |
| Event Code | Enter the unique identifier of the event. |
| Event Name | Enter the default display name of the event. You can enter a regular expression. |
| Enable | Specify whether to enable the event generation rule. By default, the rule is enabled. |
| Description | Describe the static information related to the event. |

ng

| Associated Dimension | The dimensions of the objects associated with the event. The dimensions can be used to aggregate and locate events based on the order in which they are selected. Dimensions are the only information associated with the event. You can select one or more dimensions. PRODUCT: product name. CLUSTER: cluster name. SERVICE: service name. SERVER ROLE: service role name. _ HOST: hostname. HOST PORT: host port. _ INSTANCE ID: instance name. _ DOMAIN NAME: domain name. _ IP: IP address. PAIR: source and destination address pair, which is dedicated to NOEPING. IDC: data center. NETWORK DEVICE: network device. _ NETWORK DEVICE COMPONENT: network device component. _ _ NETWORK DEVICE PORT: network device port. _ _ |
|---|---|
| Event Level | The level of the event. Valid values: P1, P2, P3, P4, P5, P6, and P7. |
| Alert Settings |   |
| Associated Alert | Specify whether to convert the event to an alert. By default, this feature is enabled. |
| Automatic Recovery Time | Specify the auto recovery time. If the event is not reported again after the specified time period ends, the platform clears the corresponding alert. The default value is 1 hour. If you set the parameter to 0, the default value is used. |
| Push Recovery Events | Specify whether the data source pushes recovery events. By default, this feature is disabled. When this feature is enabled, after the platform receives a recovery event, it clears the alert related to the most recent exception event. When this feature is disabled, the platform handles alerts based on the recovery time specified in Automatic Recovery Time. |
| Event Aggregation Period | The event aggregation period. This setting aggregates events to reduce the frequency of alerts. Events reported from the same event source and associated with the same object are aggregated within the event aggregation period. The default value is 600 seconds. |

ng

| Event Group | An event group is used to clear the alerts of multiple exception events based on one recovery event. It is a collection of correlated events. Each event can be added to multiple event groups. |
|---|---|
| Rule Settings |   |
| Event Source | The source of events. Different event sources have different event dimensions and different types of alert reporting logic. For custom events, you can select the SYSLOG or NOE TSDB event _ source. SYSLOG events are used to monitor the status of vSwitches, and NOE TSDB events are used to monitor network metrics. Valid values: _ SYSLOG: the vSwitch syslog. NOE TSDB: the NOE time series database. _ |
| Event Type | The type of the event. Valid values: VALUE: events indicating that the values of metrics fall out of the expected range. CONFIG: events indicating that the configurations of underlying machines do not comply with the expected configurations. NORMAL: events whose details are described with strings. RECOVER: recovery events indicating that exceptions have disappeared. A recovery event is used to clear the alert related to the most recent exception event. |
|   | Specify whether downstream alert rules exist. If you turn on the switch, configure the following parameters based on the event source: |

ng

| Downstream alert rules exist | SYSLOG Matching Rule Note This parameter is required when Event Source is set to SYSLOG. Device Manufacturer: Select a network element manufacturer. Valid values: H3C, Huawei, and Ruijie. Alert Association: Enter the associated objects, which are eventually reported to the event center. The objects correspond to the selected event dimensions. Regex Template: Enter a regular expression that corresponds to the syslog. Regex Keyword: Enter the fields that are extracted from the regular expression. |
|---|---|
|   | Log Level: Enter a log level. Click Automatic Recognition. In the Recognize dialog box, specify Original Text and click Submit to view the parsing result. You can click Fill to paste the parsing result to the Log Level parameter. Log Module: Enter a module. Typically, the module is defined by the manufacturer. Mnemonic Words: Enter an alert mnemonic. Typically, the mnemonic is defined by the manufacturer. Metric Anomaly Detection Rule Note This parameter is required when Event Source is set to NOE TSDB. _ PromQL Statement: Enter a PromQL statement. Click Test to test the PromQL statement that you entered. Click Retrieve Supported Metrics and select a TSDB metric |

from the **Metric** drop-down list to search for the metric in fuzzy

**Clone an event generation rule**

match mode and display the tags of the metric. a. Click **Clone** in the **Actions** column of the event generation rule that you want to clone.
**Alert Association**: Enter the associated objects, which are
In the **Copy Alert Rule** dialog box, specify **New Event Name** and **New Event Code**, eventually reported to the event center. The objects correspond to the selected event dimensions. and click **OK**.
**Alert Description**: Enter the description of the alert.
**Detection Cycle**: Set the detection cycle. The default value is 60s.
**Custom Tag**: Enter custom tags in key-value pairs, which are used
in the alert description. b. After the rule is cloned, you are redirected to the **event details** page. On the details page, you can modify the event generation rule.

**Modify an event generation rule**

ng Click **Details** in the **Actions** column of the event generation rule that you want to modify. On the **Event Details** page, modify the parameters and click **Update**.

**Delete event generation rules**

Select the event generation rules that you want to delete and click **Delete** below the list. In the message that appears, click **OK**.

**Import an event generation rule**

On the Network Event Configurations page, click **Import Configurations** above the list. In the dialog box that appears, select a configuration file and click **Open** to import the file.

## Intelligent diagnostics

### Network inspection

This feature schedules recurring network inspection tasks and converts the results into inspection events or alarms.

**Procedure**

1. Log on to the Apsara Uni-manager O&M Console.
2. In the top navigation bar, choose **Product O&M** > **Network O&M** > **Network O&M**
**Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnosis** > **Network Inspection**.
4. On the **Network Inspection** page, view the list of inspection configurations.
Each inspection configuration includes the following properties: **Name**, **Description**,
**execution interval**, **Status**, **Executions**, **Product**, **Service**, and **Role**.
Click **Advanced Filter** to find a specific inspection configuration by using the **Name**,
**Product**, **Service**, **Role**, and **Status** fields.

**Note**

Click the icon in the **Executions** column to sort the list in ascending or descending order.
5. In the list of inspection configurations, find the specific configuration and click **View**
**Details** in the **Actions** column. The panel that appears shows the details of the inspection
item. On the **Execution information** tab, view the **Basic information**, **Execution**
**information**, and the list of execution tasks.
**Basic information**: includes **Inspection item ID**, **Name**, **Code**, **Description**, **Type**,
**Product**, **Service**, **Service role**, **Convert to alarm**, and **Alarm level**.
**Execution information**: includes **Execution location**, **Execution content**, **Interval**,
and **Running status**. View the list of execution tasks. Task information includes **Task ID**, **Start time**, and
**Execution status**.
Find a specific execution task by using the **Task ID**, **Status**, and **Execution time** fields. Hover over a task's status in the **Execution status** column to view its execution results.

**Note**

Execution statuses:
**WAITING**: The inspection task is waiting to be triggered.
**RUNNING**: The inspection task is running.
**SUCCESS**: The inspection task was successfully executed.
**FAILED**: The inspection task failed to execute.
**TIMEOUT**: The inspection task timed out.
**CLEANED**: The platform clears residual tasks from previous runs during
initialization. Hover over **Execution Parameters** in a task's **Actions** column to view its parameters. Hover over **Additional Information** in a task's **Actions** column to view its additional information. On the **Related events** tab, view the list of events. Event information includes **Event name**, **Event description**, **Associated object**,
**Event source type**, **Event source**, **Exception type**, **Event timeout**, **Event level**,
**Associated alarm ID**, and **Occurrence time**.
Click **Advanced Filter** to find a specific event by using the **Time**, **Event name**,
**Associated object**, **Alarm level**, **Event source type**, and **Event exception type**
fields. Find the specific event and click **Details** in the **Actions** column to view its details in the dialog box that appears. The details primarily include **Event information** and **Event content**. The specific details vary by event type. For more information, see the content displayed in the console.

**More operations**

| Actions | Description |
|---|---|
| Import inspection configuration | 1. On the Network Inspection page, click Import Inspection Configuration. 2. Select the inspection configuration file to import and clickO pen. |

| Enable inspection configuration | Note You can enable an inspection configuration only when its Status is Stopped. 1. In the list of inspection configurations, find the target configuration and click Enable in the Actions column. 2. In the dialog box that appears, click OK. |
|---|---|
| Stop inspection configuration | Note You can stop an inspection configuration only when its Status is Running. 1. In the list of inspection configurations, find the target configuration and click Stop in the Actions column. 2. In the dialog box that appears, click OK. |

**Common inspection items**

| Product | Name | Description |
|---|---|---|
| SLB | SLB resource usage watermark check | Checks the resource usage watermark for SLB. |
|   | SLB LVS and proxy local address check | Checks the local addresses of SLB LVS and proxies. |
|   | SLB HTTP rule configuration sync check | Checks the configuration sync of SLB HTTP rules. |
|   | SLB LVS and proxy plug status check | Checks the plug status of SLB LVS and proxies. |
|   | SLB consistency inspection | Checks for SLB consistency. |
|   | SLB abnormal workflow inspection | Checks for abnormal SLB workflows. |
|   | SLB xdss configuration check | Checks the configuration sync of SLB xdss. |
|   | SLB-Yaochi duplicate resource inspection | Checks for duplicate resources between SLB and Yaochi, including duplicate real servers _ and VIPs. |
|   | SLB API and master site reconciliation check | Performs a reconciliation check between the SLB API and the master site. |

|   | SLB database structure check | Checks the SLB database structure. |
|---|---|---|
|   | SLB API and master LB status reconciliation check | Performs a status reconciliation check for load balancers between the SLB API and master. |
|   | SLB LVS multi-AZ route redundancy inspection | Inspects route redundancy for LVS in multi-AZ deployments. Applicable to dual- and triple-AZ scenarios, but not to single-AZ deployments. |
|   | switch lldp check _ _ | Checks whether LLDP is enabled on the switch. |
|   | switch link aggregation check _ _ _ | Checks whether the status of link aggregation member ports on the switch is normal. |
|   | switch reboot time check _ _ _ | Checks for recent unexpected switch reboots. |
|   | switch resource monitor resource ro _ _ _ _ ute check _ | Checks whether the watermark for route table entries on the switch is too high. |
|   | switch stp check _ _ | Checks whether Spanning Tree Protocol (STP) is enabled on the switch. |
|   | switch transceiver diagnosis check _ _ _ | Checks whether the optical attenuation of the switch transceiver is within the normal range. |
|   | switch mad check _ _ | Checks whether Multi-Active Detection (MAD) is enabled for the switch stack. |
|   | switch igmp group check _ _ _ | Checks whether the IGMP multicast groups on the switch are non-empty. |
|   | switch interface status check _ _ _ | Checks whether the switch interface status is normal. |
|   | switch packet drop check _ _ _ | Checks for buffer-related packet drops on switch ports. |
|   | switch interfaces counters errors ch _ _ _ _ eck | Checks for an increase in CRC or error counts on switch interfaces. |
|   | switch current bgp configuration ch _ _ _ _ eck | Checks if switch routes use Equal-Cost Multi- Path (ECMP). |

| baseServi ceAll |   |   |
|---|---|---|
|   | switch power check _ _ | Checks whether the switch power supply status is normal. |
|   | switch info center check _ _ _ | Checks whether the switch information center and logging functions are enabled. |
|   | switch monitor link group check _ _ _ _ | Checks whether the switch CPU monitor-link status is normal. |
|   | switch load- _ balance configuration check _ _ | Checks if the switch hash algorithm configuration is correct. |
|   | switch temperature check _ _ | Checks whether the switch hardware operating temperature is too high. |
|   | switch cpu check _ _ | Checks whether the switch CPU utilization is too high. |
|   | switch save time check _ _ _ | Checks whether the switch configuration is saved. |
|   | switch routing table age check _ _ _ _ | Checks for route flapping on the switch. |
|   | switch pim routing-table check _ _ _ | Checks whether the switch PIM multicast routing information is non-empty. |
|   | switch lacp counters check _ _ _ | Checks if the load is balanced across the switch's LACP member ports. |
|   | switch fan check _ _ | Checks whether the switch fan status is normal. |
|   | switch memory check _ _ | Checks whether the switch memory utilization is too high. |
|   | switch bgp peer check _ _ _ | Checks the stability and status of the switch's BGP peers. |
|   | switch save check _ _ | Checks whether the switch flash memory is writable. |
|   | switch snmp status check _ _ _ | Checks whether the switch SNMP status is abnormal. |

|   | switch device check _ _ | Checks whether the switch hardware card status is normal. |
|---|---|---|
|   | switch interface check _ _ | Checks whether the switch interface status is normal. |
|   | switch eth trunk check _ _ _ | In non-stacking scenarios, checks whether aggregated ports have dual uplinks. |
|   | switch irf check _ _ | Checks whether the switch stacking status is normal. |
|   | switch transceiver alarm check _ _ _ | Checks for alarms on the switch transceiver. |
| VPN Gateway | VPN Gateway image check | Checks the VPN Gateway image. |
|   | VPN Gateway Yaochi workflow status check | Checks the workflow status for VPN Gateway in Yaochi. |
|   | VPN Gateway control plane workflow status check | Checks the workflow status of the VPN Gateway control plane. |
|   | VPN Gateway control plane and VPC Yaochi Havip inspection | Performs a Havip check between the VPN Gateway control plane and VPC in Yaochi. |
|   | VPN Gateway and VPC reconciliation check | Performs a reconciliation check between VPN Gateway and VPC. |
|   | VPN Gateway and ECS reconciliation check | Performs a reconciliation check between VPN Gateway and ECS. |
|   | VPN Gateway DB check | Checks the VPN Gateway database. |
|   | VPN Gateway instance transient state check | Checks for VPN Gateway instances that are stuck in a transient state. |
|   | VPN Gateway Yaochi and VPN Gateway control plane reconciliation check | Performs a reconciliation check between VPN Gateway on Yaochi and the VPN Gateway control plane. |
|   | VPN Gateway control plane and VPC Yaochi NatPublicIp inspection | Performs a NatPublicIp check between the VPN Gateway control plane and VPC in Yaochi. |

| ALB | Check rspool data consistency | Checks the data consistency of rspool. |
|---|---|---|
|   | Check for proxy devices that are online but fail health checks | Checks for online proxy devices that are failing health checks. |
|   | Check proxy plug status | Checks if the management status and traffic steering status of a proxy device match. |
|   | ALB control plane and keyserver data consistency check | Checks for data consistency between the ALB control plane and keyserver. |
|   | ALB and SLB ACL reconciliation | Performs an ACL resource reconciliation between ALB and the SLB control plane. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | ALB parameter memory and DB consistency check | Checks for consistency between ALB parameters in memory and in the database. |
|   | ALB and SLB rspool reconciliation | Performs an rspool resource reconciliation between ALB and the SLB control plane. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | Check consistency of data for running VIPs | Checks data consistency for running VIPs. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | ALB four history tables row count check | Checks the row counts of the four ALB history tables. |
|   | ALB Yaochi | Checks for resources in ALB on Yaochi that are not in a stable state. |
|   | ALB and VPC Yaochi reconciliation | Performs a resource reconciliation between ALB and VPC on Yaochi. |
|   | Check consistency of data for active LBs | Checks the data consistency for active load balancers. |
|   | ALB Yaochi and ALB control plane reconciliation check | Performs a reconciliation check between ALB on Yaochi and the ALB control plane. |

| ECS | AVS steady-state issue inspection | Checks for steady-state issues in the AVS environment. |
|---|---|---|
|   | Inspect for abnormal network sync status | Inspects for abnormal network sync status under high CPU utilization. |
|   | Checks for AVS terminations caused by out-of-memory errors | Checks for AVS terminations caused by out-of- memory errors. |
|   | AVS DHCP service Unix domain socket inspection | Checks if the Unix domain socket connection for the AVS DHCP service is established. |
| nfv | nfv-controller-thirdNet workflow status check | Checks the workflow status of nfv-controller- thirdNet. |
|   | nfv-platform-controller workflow status check | Checks the workflow status of nfv-platform- controller. |
|   | nfv-controller-tr workflow status check | Checks the workflow status of nfv-controller-tr. |
|   | nfv-controller-alb workflow status check | Checks the workflow status of nfv-controller- alb. |
|   | vpc env check _ _ | Performs the vpc env check. _ _ |
|   | VPC service CIDR validity inspection | Checks the validity of the VPC service CIDR block. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | VPC duplicate global tunnel id _ _ inspection | Checks for duplicate global tunnel id in VPC. _ _ Applicable to single-, dual-, and triple-AZ scenarios. |
|   | VPC region resource watermark inspection | Inspects the resource watermark for VPC. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | VPC multi-AZ XGW route redundancy inspection | Inspects route redundancy for XGW in multi-AZ VPC deployments. Applicable to dual- and triple-AZ scenarios, but not to single-AZ deployments. |

| VPC |   |   |
|---|---|---|
|   | VPC CGW multi-AZ route redundancy inspection | Inspects route redundancy for CGW in multi-AZ deployments. Applicable to dual- and triple-AZ scenarios, but not to single-AZ deployments. |
|   | VPC asynchronous task inspection | Checks VPC asynchronous tasks. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | Duplicate app server ip inspection _ _ | Checks for duplicate app server ip. Applicable _ _ to single-, dual-, and triple-AZ scenarios. |
|   | VPC sequential task backlog inspection | Checks for backlogged VPC sequential tasks. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | VPC-AVS reconciliation inspection | Performs a reconciliation check between VPC and AVS. |
|   | vpc gw oplog global version large _ _ _ _ table inspection | Checks the large vpc gw oplog global version _ _ _ _ table. |
|   | VPC tenant resource watermark inspection | Inspects the watermark for VPC tenant-level resources. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | vpc nc oplog large table inspection _ _ | Checks the large vpc nc oplog table. _ _ |
|   | VPC-XGW reconciliation inspection | Performs a reconciliation check between VPC and XGW. |
| CEN | Inspection for stuck BRPOP asynchronous events | Checks for stuck BRPOP asynchronous events. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | Watermark inspection for RI count within a region | Inspects the watermark for the number of router interfaces (RIs) within a region. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | CEN Yaochi inspection for stuck asynchronous events | Checks for stuck asynchronous events in CEN on Yaochi. Applicable to single-, dual-, and triple-AZ scenarios. |
|   | Watermark inspection for the number of leased lines with health checks in a region | Inspects the watermark for the number of leased lines with health checks in a region. Applicable to single-, dual-, and triple-AZ scenarios. |

|   | Inspection for stuck RRC asynchronous operations | Checks for stuck RRC asynchronous operations. Applicable to single-, dual-, and triple-AZ scenarios. |
|---|---|---|
|   | CEN NullPointerException file log inspection | Checks the CEN file log for NullPointerExceptions. |
|   | tr-gobgp check | Performs a TR-GOBGP check. |
|   | Inspection for stuck CENC workflows | Checks for stuck CENC workflows. Applicable to single-, dual-, and triple-AZ scenarios. |

### Intelligent path analysis

#### Intelligent path analysis

The intelligent path analysis and forwarding feature provides path diagnostics capabilities. You can use this feature to implement end-to-end path analysis by quickly establishing IP paths. This facilitates fault analysis and shortens the fault analysis time.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Intelligent Path**
**Analysis**.
4. On the Intelligent Path Analysis page, click **Create Path Analysis**. On the page that
appears, configure the following parameters and click **Analysis**.

| Parameter | Description | Example |
|---|---|---|

| Scenario | The scenario of path analysis. Valid values: Mutual access between ECS instances: access between Elastic Compute Service (ECS) instances in a virtual private cloud (VPC). ECS access server load balancer: access from an ECS instance in a VPC to a Server Load Balancer (SLB) instance. ECS access AnyTunnel: access from an ECS instance in a VPC to an AnyTunnel virtual IP address (VIP). ECS access SingleTunnel: access from an ECS instance in a VPC to a SingleTunnel VIP. ECS access IDC: access between an ECS instance in a VPC and a data center. ECS access to the Internet: access from an ECS instance in a VPC to the Internet. Exchange of space-based containers: access between Docker containers in a cloud platform. Apsara infrastructure management framework container access load balancing: access from a Docker container to an SLB instance in a cloud platform. Apsara infrastructure management framework container access NC: access from a Docker container to a physical machine in a cloud platform. NC Mutual visits: access between physical machines in a cloud platform. NC access Apsara infrastructure management framework container: access from a physical machine to a Docker container in a cloud platform. NC access load balancing: access from a physical machine to an SLB instance in a cloud platform. | Mutual access between ECS instances |
|---|---|---|
| Physical link analysis | Specify whether to enable or disable the physical link analysis feature. If you enable this feature, you must deliver the configuration to vSwitches. In this case, the analysis time is extended. If you disable this feature, the analysis time is shortened. However, the packet capture data of the physical devices is not contained. | N/A |
| Source IP address | The IP address of the source node. IPv4 and IPv6 addresses are supported. | 192.168.1.1 and FE80::/10 |
| Destination IP address | The IP address of the destination node. IPv4 and IPv6 addresses are supported. | 192.168.1.1 and FE80::/10 |

| Detection Protocol | The protocol type of probe packets for the path analysis. Valid values: TCP UDP ICMP | TCP |
|---|---|---|
| SOURCE Port | The port of the source node. If you leave this parameter empty, all ports are used. | 80 |
| Destination Port | The port of the destination node. If you leave this parameter empty, all ports are used. | 8080 |
| Number of probe packets | The total number of probe packets for path analysis. | 10 |
| SOURCE VpcId | The ID of the VPC in which the source node resides. | vpc- **fczvaczv |
| Destination VpcId | The ID of the VPC in which the destination node resides. | vpc- **fczvaczv |
| Timeout period | The timeout period of the packet capture in the analysis task. If this period is exceeded, the packet capture stops. Unit: minutes. | 5 |

5. In the **Path analysis** section, the status timeline of the analysis task is displayed, and the
estimated time required for each phase is displayed. The topology of the path is displayed at the bottom of the timeline. After the analysis is complete, the analysis result is displayed.

**Note**

For path nodes of the ECS type or physical machine type, you can click the hyperlink in the topology to go to the details page. After you select the topology, you can drag the topology and change the location of the topology.
6. In the **Diagnosis details** section, the details of the task are displayed.
7. In the **Analyze one by one** section, the analysis details of the packets captured by the
task are displayed if the analysis task is successful. You can view the analysis details of packets one by one.

**What to do next**

| Operation | Procedure |
|---|---|
| View the details of an analysis task | 1. On the Intelligent Path Analysis page, select a time range to view the information about the intelligent path analysis tasks within the specified time range. 2. Find the analysis task that you want to view and clickD etails in the Operation column. You can view the analysis results, including the path analysis, diagnostic details, and analysis details of each packet. |
| Terminate an analysis task | On the Intelligent Path Analysis page, find the analysis task that you want to terminate and click Terminate in the Operation column. Note You cannot terminate an analysis task that is in theC ompleted state. |

#### Topology analysis

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and in the desired state.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Intelligent Path**
**Analysis** > **Topology Analysis**.
4. On the **Topology Analysis** page, set the following parameters.

| Parameter | Description |
|---|---|
| Scenario | Select a scenario for path analysis. Physical Path Topology ECS to ECS: access between Elastic Compute Service (ECS) instances in a virtual private cloud (VPC). ECS to AnyTunnel: access from an ECS instance in a VPC to an AnyTunnel virtual IP address (VIP). ECS to SingleTunnel: access from an ECS instance in a VPC to a SingleTunnel VIP. ECS to SLB: access from an ECS instance in a VPC to a Server Load Balancer (SLB) instance. ECS to IDC: access between an ECS instance in a VPC and a data center. ECS to the Internet: access from an ECS instance in a VPC to the Internet. Docker to Docker: access between Docker containers on a cloud platform. Docker to SLB: access from a Docker container to an SLB instance on a cloud platform. Docker to NC: access from a Docker container to a physical machine on a cloud platform. NC to NC: access between physical machines on a cloud platform. NC to Docker: access from a physical machine to a Docker container on a cloud platform. NC to SLB: access from a physical machine to an SLB instance in a cloud platform. Forwarding Path Topology > Common Forward Path Analysis |
| Source IP address | The IP address of the source node. IPv4 and IPv6 addresses are supported. |

| Destination IP address | The IP address of the destination node. IPv4 and IPv6 addresses are supported. |
|---|---|
| Detection Protocol | The protocol type of probe packets for the path analysis. Valid values: TCP UDP ICMP |
| SOURCE Port | The port of the source node. If you leave this parameter empty, all ports are used. |
| Destination Port | The port of the destination node. If you leave this parameter empty, all ports are used. |
| Source VpcId | The ID of the VPC in which the source node resides. |
| Destination VpcId | The ID of the VPC in which the destination node resides. |

5. Click **Analysis**. In the **Topology Analysis** section, view and manage the logical topology.

**Note**

Click any topology icon to view related content in the panel that appears. For a path node of the ECS type, you can go to the ECS console to view the instance details. For a path node of the NC type, you can click the **blue link** in the topology to view details. You can also go to the machine details page of the Apsara Infrastructure Management console to view details.

### Network instance diagnostics

The network instance diagnostics feature allows you to analyze the status of network instances with a few clicks.

**Scenarios**

The network instance diagnostics feature helps you quickly analyze a network instance to identify whether it has an unexpected state. This feature provides visualized and automated diagnostics capabilities and can improve the O&M efficiency of network O&M engineers, reduce O&M risks, and improve the quality of virtual private cloud (VPC) O&M.

**Limits**

The NetworkBaseServiceCluster cluster for BaseServiceAll has been deployed and has reached the desired state. After a diagnostic task is started, it does not stop until the diagnosis is complete. You cannot pause or terminate the task.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Instance**
**Diagnosis**.
4. In the **One-click analysis of the running status of network instances** section, select
the service whose instance you want to diagnose, enter the ID of the instance, and then click **Diagnose now**. You can select one of the following values: SLB DNS Elastic IP Address Virtual Board Router Physical Connection NAT Gateway DCI Connection External Connection
5. The Network instance diagnosis results page appears. On this page, view the information in
the **Instance details**, **Instance topology**, and **Diagnosis details** sections.

**Note**

The **Instance details** section is displayed only when you select SLB in the previous step. In the field at the top of the Network instance diagnosis results page, the ID of the diagnosed instance is displayed by default. You can also enter the ID of another instance and click **Diagnose now** to perform diagnostics. In this example, an Server Load Balancer (SLB) instance is diagnosed and its diagnostic results are described. Instance details: Instance topology: In the topology example shown in the preceding figure, the leftmost column displays the SLB instance, the middle column displays the listeners of the SLB instance, and the rightmost column displays the backend servers that correspond to the listeners. If a backend server is of the ECS type or the machine type of Apsara Infrastructure Management, click realServer in the topology. A panel appears to show the server details. After you select the topology, you can drag the topology to change the location of the topology. Diagnosis details: This section displays the information about diagnostic items in the following columns: **Diagnostic item name**, **Description**, **Diagnostic results**, and
**Diagnosis details**.
6. You can also perform the following operations in the **Task list** section on the Network
Instance Diagnosis page to view historical diagnostic results of an instance: Specify a time range, find the diagnostic task that you want to view, and then click **Details** in the **Operation** column to go to the Network instance diagnosis results page. On this page, view the diagnostic results in the **Instance details**, **Instance topology**, and
**Diagnosis details** sections.

### Container network diagnostics

This topic describes the automated intelligent diagnostics capabilities for container networks based on mutual accessibility.

**Scenarios**

The container network diagnostics feature helps you quickly analyze container networks to determine whether the container networks have unexpected states. Visualized and automated diagnostics capabilities are provided. This feature can improve the O&M efficiency of network O&M engineers, reduce O&M risks, and improve the O&M quality of virtual private clouds (VPCs).

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Diagnose Container**
**Network**.
4. On the Container Network Diagnostics page, click **Create Diagnosis Task**. On the page
that appears, configure the parameters that are described in the following table and click
**Submit**.

| Parameter | Description |
|---|---|
| Source IP Address | The source IP address. |
| Destination Node Information | The information about the destination node. Select Destination IP Address or Destination Domain and enter the corresponding information. |
| Destination Port | The number of the destination port. |
| Protocol | The type of the protocol. Valid values: tcp udp |
| Enable Global Check | Specifies whether to enable the global check. After you turn on Enable Global Check, no topology information is displayed. |

5. After the diagnostic task is complete, view the path analysis topology and diagnostic report
in the lower part of the page.

**What to do next**

| Operation | Procedure |
|---|---|
| View the details of a diagnostic task | 1. On the Container Network Diagnostics page, find the diagnostic task that you want to view and click Details in the Operation column. 2. On the Diagnose Container Network page, view the details of the diagnostic task, including the path analysis topology and diagnostic report. |
| Terminate a diagnostic task | You can terminate a diagnostic task only when it is in the Running state. 1. On the Container Network Diagnostics page, find the diagnostic task that you want to terminate and click Terminate in the Operation column. 2. In the message that appears, click OK. |

### Network health assessment

The Network Health Assessment module evaluates and diagnoses the health status of each layer of the network based on the dimensions such as performance, capacity, function, and status. This module provides an overview of the network health status and detects issues and risks at all layers of the network in real time to ensure that the network runs as expected.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Health**
**Assessment**.
4. On the Network Health Assessment page, view the health assessment status of different
network layers in the Health overview list.

| Evaluation layer | Description | Dimension |
|---|---|---|
| Network service instance | The Network Health Assessment module detects the access and configuration issues of a network service instance at the earliest opportunity by checking the features and configurations of the network service instance. | Function health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Overlay network layer | The Network Health Assessment module comprehensively evaluates the health status of services such as eXtreme Global Workspace (XGW), Apsara Virtual Switch (AVS), Content Switched Network (CSW), Converged Gateway (CGW), Smart Network Appliance (SNA), and Hybrid Switch (HSW) by checking the monitoring results of the physical servers, network element nodes, and packet loss of the services. | Status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Network service controller | The Network Health Assessment module checks the alerts on the control planes of services such as Virtual Private Cloud (VPC), Server Load Balancer (SLB), DNS, and NSP and identifies issues at the earliest opportunity by checking the monitoring data of the services. | Status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
| Physical device layer | The Network Health Assessment module evaluates the health status of devices by monitoring the core metrics of the devices. | Performance health assessment score, capacity health assessment score, status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage. |
| Protocol layer | The Network Health Assessment module checks the status of routing protocols, such as Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP). | Capacity health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |

| Network layer | The Network Health Assessment module comprehensively evaluates the health status of the network layer by checking the monitoring data of interconnection status of devices, physical interface of the network, intelligent prediction of the optical module, and network interface controllers (NICs). | Performance health assessment score, status health assessment score, numbers of normal diagnostics items and total diagnostics items, and overall score of this layer in percentage |
|---|---|---|

5. In the Health overview list, find an evaluation layer whose details you want to view and
click **Details** in the Operation column to go to the **Health Details** page. i. In the **KPI details** section, click Advanced Filter. Then, configure the KPI name, Status, and Network evaluation hierarchy type parameters to filter key performance indicators (KPIs). The following table describes the information about KPIs in the list.

| Parameter | Description |
|---|---|
| KPI name | The name of the KPI at the evaluation layer. KPIs are different at different evaluation layers. |
| Hierarchy type | The dimensions based on which the layer is evaluated. The dimensions vary with different evaluation layers. Network service instance: Only the function dimension is supported. Overlay network layer: Only the status dimension is supported. Network service controller: Only the status dimension is supported. Physical device layer: Only the performance, capacity, and status dimensions are supported. Protocol layer: Only the capacity dimension is supported. Network layer: Only the performance and status dimensions are supported. |
| Status | The KPI status. Valid values: critical, abnormal, sub-health, and healthy. |
| Total number of diagnostic items | The total number of KPI items that are diagnosed. |

| Number of diagnostics items passed | The number of the KPI items that passed the diagnostics. |
|---|---|
| Number of diagnostic exceptions | The number of abnormal KPI items. You can click the number in the Number of diagnostic exceptions column to filter the abnormal events by the current KPI in the Abnormal Event section. |
| Health Assessment Score (percentile system) | The health evaluation score of the KPI. The score is calculated based on the following formula: Health evaluation score of a KPI = Number of items that passed the diagnostics/Total number of diagnostics items. |
| Update Time | The time when the KPI was last diagnosed. |

ii. In the **Abnormal Event** section, click Advanced Filter and configure the KPI name, Start time, Clear Time, Show cleared issues, Grade, Associated instance, and Event type parameters to filter abnormal events. The following table describes the information about abnormal events in the list.

| Parameter | Description |
|---|---|
| Name | The name of the abnormal event. |
| KPI name | The name of the alert event to which the abnormal event belongs. |
| Problem Description | The description of the abnormal event. |
| Associated instance | The information about the instance associated with the abnormal event. |
| Critical grade | The severity level of the abnormal event. The severity levels are listed in descending order: P1, P2, P3, P4, P5, P6, and P7. |
| Type | The type of the abnormal event. Valid values: status, function, capacity, and performance. |
| Clear Tags | Indicates whether the abnormal event is cleared. By default, No is displayed in the Clear Tags column of an abnormal event. After you click Clear in the Operation column, Yes is displayed in the Clear Tags column of the abnormal event. |
| Confirmation mark | Indicates whether the abnormal event is confirmed. By default, No is displayed in the Confirmation mark column of an abnormal event. After you click Confirm in the Operation column, Yes is displayed in the Confirmation mark column of the abnormal event. |

| Start time | The time when the abnormal event was detected. |
|---|---|
| Clear Time | The time when the abnormal event was cleared. |

a. Find the abnormal event that you want to view and click **Details** in the Operation column. In the Exception event details panel, view the details of the abnormal event. b. Click **Confirm** in the Operation column to mark the event as an abnormal event. c. Handle the abnormal event based on its name, issue description, severity level, and associated instance, and then click **Clear** in the Operation column.

**Note**

**Clear** is displayed in the Operation column of an abnormal event only after you
click **Confirm** in the Operation column of the abnormal event.

### Optical transceiver module

**diagnostics**

The Optical Module Diagnostics module analyzes and predicts the status of optical transceiver modules based on AI algorithms and assists O&M personnel in troubleshooting issues.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Optical Module**
**Diagnostics**.
4. In the upper part of the Optical Module Diagnostics page, view the status distribution of
optical transceiver modules on the current day and the status distribution of optical transceiver modules within a specific period of time.

**Note**

The status of an optical transceiver module can be health, sub-health, exception, or unknown. The line chart shows the trend in the proportion of optical transceiver modules in the health state.
5. In the lower part of the Optical Module Diagnostics page, view the basic information and
analysis results of optical transceiver modules. You can click **Advanced Filter** and then filter optical transceiver modules by **optical transceiver module model**, **optical**
**transceiver module manufacturer**, **optical transceiver module status**, **hostname**,
**interface name**, and **device type**.

| Parameter | Description |
|---|---|
| Hostname | The name of the device to which the optical transceiver module belongs. |
| Interface name | The interface name of the device to which the optical transceiver module belongs. |
| Ownership Type | The type of the device to which the optical transceiver module belongs. Valid values: NETWORK SWITCH and NC. _ |
| Manufacturer | The manufacturer of the optical transceiver module. |
| Model | The model of the optical transceiver module. |
| Status | The status of the optical transceiver module. |
| Failure probability | The failure probability of the optical transceiver module. The failure probability is predicted based on the transmit power, received power, and bias current variation. |
| Expected residual life | The expected residual life of the optical transceiver module. Note The residual life is calculated based on the monitoring data and threshold of the bias current. If the bias current threshold or the real- time bias current value cannot be detected, unknown is displayed in the Expected residual life column. |
| Intelligent analysis results | The intelligent analysis result of the optical transceiver module. The analysis is performed based on the predicted failure probability and expected residual life. The following exception analysis results may be returned: The failure probability of the optical transceiver module is high. The residual life of the optical transceiver module is insufficient. The connection of the optical transceiver module is poor. |

6. Find the optical transceiver module that you want to view and click **Details** in the
Operation column. The **Optical Module Prediction Details** page appears. i. In the upper part of the page, view the basic information and prediction of the optical transceiver module. ii. In the lower part of the page, select a time range and view the metrics of the optical transceiver module, including **temperature**, **bias current**, **voltage**, **transmit power**, and **received power**.

| Metric | Description |
|---|---|
| Temperature | The temperature of an optical transceiver module affects the performance and life of the optical transceiver module. If the temperature is excessively high or low, the performance of the optical transceiver module may be damaged and the life of the optical transceiver module may be shortened. Excessively high temperature may affect the transmission distance and rate of the optical transceiver module. In addition, the performance of the light emitter and the detector may be compromised, which results in a failure of the optical transceiver module. Excessively low temperature affects the performance and life of the optical transceiver module. |
| Bias current | The bias current of an optical transceiver module is used to stimulate the laser to emit optical signals and affects the output power of the laser and the transmission distance of the optical transceiver module. Excessively large bias current may cause aging and damage of the laser and shorten the life of the optical transceiver module. Excessively small bias current may lower the output power of the laser and shorten the transmission distance. |
| Voltage | The voltage of an optical transceiver module refers to the voltage that is used to stimulate the laser to emit optical signals and the receiver to receive optical signals. If the voltage is unstable or deviates from the specified range, the optical transceiver module may fail or its performance may degrade. If the voltage is lower than expected, the transmit power of the optical transceiver module may be decreased. If the voltage is higher than expected, the optical transceiver module may fail. |
| Transmit power | The transmit power of an optical transceiver module refers to the power of the laser to emit optical signals. The transmit power of the optical transceiver module affects the transmission distance and rate of the optical transceiver module. Excessively high transmit power may damage the optical transceiver module. Excessively low transmit power may shorten the transmission distance. |

| Received power | The received power of an optical transceiver module refers to the power of the receiver to receive optical signals. The received power of the optical transceiver module affects the receiver sensitivity and transmission performance of the optical transceiver module. If the received power exceeds the specified range, issues such as signal transmission interruption, error increase, and transmission distance decrease may occur. In this case, you can monitor the received power to identify and resolve issues at the earliest opportunity. If the received power is higher than expected, you can decrease the transmit power or check the length of the jointed fiber. If the received power is lower than expected, you can increase the transmit power or check the quality of the jointed fiber. |
|---|---|

### NOE ping

NOE ping provides full-path probing for physical networks to help diagnose global network failures on the cloud platform. You can use it to troubleshoot packet loss within a single data center, monitor the quality of Data Center Interconnect (DCI) leased lines, and check network quality in edge availability zones (AZs) and across regions.

**Deploy the NOE ping agent**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Product O&M** > **Network O&M** > **Network O&M Console**.
3. In the navigation pane on the left, choose **Intelligent Diagnosis** > **NOE ping**.
4. On the **Agent Information** tab, click **Deploy**.
5. In the dialog box that appears, enter the **Physical Server IP** for the agent deployment,
and then click **OK**.

**Related operations**

| Operation | Procedure |
|---|---|
| Start probing | On the Agent Information tab, find the agent and click Start in the Actions column. |
| Stop probing | On the Agent Information tab, find the agent and click Stop in the Actions column. |
| Take an NOE ping agent offline | On the Agent Information tab, find the agent and click Take Offline in the Actions column to take the agent offline. |

| Set a blacklist | On the Agent Information tab, click Blacklist. In the dialog box that appears, add IPs to the Blocked IP List. Note Probing failures for blocked IPs do not trigger alerts. |
|---|---|
| Set parameters | On the Agent Information tab, click Parameter Settings. On the page that appears, set the probing metric parameters. Note For probing between AZs and across regions, UDP messages are used. NOE ping agents enable the UDP service to probe each other. For probing within an AZ, TCP messages are used. Each NOE ping agent probes different IPs under a group of Access Switches (ASWs). |

**View intra-AZ probing results**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Product O&M** > **Network O&M** > **Network O&M Console**.
3. In the navigation pane on the left, choose **Intelligent Diagnosis** > **NOE ping**.
4. On the **Intra-AZ Probing Results** tab, view the probing results.

**Related operations**

| Operation | Instructions |
|---|---|
| Initiate Probing | In the Actions column for the target item, click Initiate Probing. In the dialog box that appears, select a Probing Protocol, and click Confirm to start probing. |
| Probing Details | In the Actions column for the target item, click Probing Details to view the details. |

**View inter-AZ probing results**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Product O&M** > **Network O&M** > **Network O&M Console**.
3. In the navigation pane on the left, choose **Intelligent Diagnosis** > **NOE ping**.
4. On the **Inter-AZ Probing Results** tab, view the probing results.

### Network toolbox

#### Tools

The Tools page displays a list of tools that are available in the network toolbox.

**View the tool list**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Toolbox** >
**ToolList**.
4. On the **Tools** page, view the tools available in the network toolbox. The tool list includes
the following columns: **Tool Name**, **Risk Level**, **Affected Product**, **Number of**
**Executions**, and **Description**.
To import tools, click **Import Tool** above the list and upload a local file. To filter tools, click **Advanced Filter** and configure the **Tool Name**, **Risk Level**, and
**Affected Product** parameters.
To view the execution history of a tool, click the number in the **Number of Executions** column of the tool to go to the **Tool Executions** page. For more information, see the "Search for an execution" section of the Tool execution history topic.

**Preset tools**

| Tool name | Risk level | Description |
|---|---|---|
| logic topo | Low risk | Used to analyze the network connection paths between nodes in the cloud platform. For more information, see the parameter description in Topology analysis. |

**View the details of a tool**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Toolbox** >
**ToolList**.
4. On the **Tools** page, find the tool that you want to view and click **Details** in the **Actions**
column.
5. On the **Tool Details** page, view the details of the tool.
**Basic Information**: displays **Tool Code**, **Name**, **Risk Level**, **Affected Product**,
**Version**, **Description of Applicable Conditions**, and **Scenario Description**.
**Tool Flowchart**: displays the execution process of the tool, including the **Parameter**
**Check** step and subsequent steps.
The steps after Parameter Check vary based on the tool. Click the icon of a step to view the details of the step, including **step information** and
**execution information**.

**Execute a tool**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Toolbox** >
**ToolList**.
4. On the **Tools** page, find the tool that you want to execute and click **Initiate Execution** in
the **Actions** column.

**Note**

You can also click **Initiate Execution** in the upper-right corner of the **Tool Details** page to create a tool execution workflow.
5. In the **Initiate Execution** dialog box, configure the parameters and click **OK**.
The parameters to be configured vary based on the tool.
6. After the tool execution workflow is created, you are redirected to the **Tool Execution**
**Details** page. You can view the execution status of the workflow. For more information, see
the "View the details of an execution" section of the Tool execution history topic.

#### Tool execution history

The Tool Executions page displays the tool execution history.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Intelligent Diagnostics** > **Network Toolbox** >
**toolExecutionHistory**.
4. On the **Tool Executions** page, view the execution details of tools in the following columns:
**Workflow ID**, **Tool Name**, **Description**, **Execution Time**, **Execution Result**, **Executed**
**By**, and **Execution Parameters**.

**Search for an execution**

To filter executions, click **Advanced Filter** and configure the **Tool Name**, **Execution**
**Result**, **Execution Time**, **Submitted By**, **Workflow ID**, and **Execution Parameters**
parameters.

**Note**

For more information about the meaning of **execution results**, see the Execution result explanation section of this topic.

**View the details of an execution**

Find the execution that you want to view and click **View Details** in the **Actions** column. On the **Tool Execution Details** page, view the details of the execution.

**Note**

The execution details vary based on the tool.
**Basic Information**: displays **Tool Name**, **Tool Code**, **Workflow ID**, **Execution Time**,
**Execution Status**, **Submitted By**, **Affected Product**, **Risk Level**, **Workflow Is**
**Rolled Back or Not**, **Description of Applicable Conditions**, and **Scenario**
**Description**.
If **Execution Status** is W_Running, wait until the status changes to ParamVerifying. If **Execution Status** is ParamVerifying, the workflow is paused until the executor confirms the parameter check results. If **Execution Status** displays an abnormal state, such as Failed or W_MaxRetries, suspend the execution, troubleshoot issues based on the execution log, and then continue the execution or re-execute the tool. If **Execution Status** is W_MaxRetries, you can retry the workflow. When **Execution Status** changes to End, the workflow is complete.
**Execution Progress**: displays the status of each step in the workflow. The steps are
the same as those in the tool flowchart. Click **Proceed**, **Suspend**, or **Terminate** to resume, pause, or stop the workflow. Click **View Details** below a step to view the **step details**.
**Basic Information**: displays the basic information about the step.
**Execution Information**: displays **Last Execution Information**, **Last Execution**
**Environment Variable**, and **Execution History**.
In the **Execution History** section, find the execution that you want to view and move the pointer over **Details** in the **Actions** column to view the execution details.
**Parameter Information**: displays **Input Parameters** and **Output Parameters**.
The name, type, and description of each parameter are displayed. Click **Confirm Parameters** in the **Parameter Check** section to view the parameter check results of the check items of the workflow and determine whether the check results are normal. Click **Approved** to continue to run the workflow. Click **Terminate Workflow** to terminate the workflow. Click **Retry** below a step to re-execute the step.

**Execution Information**

**Execution Result**: displays the tool execution results.
**Event Records**: displays the reported events.
**Parameter Information**: displays the **parameter check** results and **input**
**parameters**.
**Execution Logs**: displays the latest 1,000 lines of the execution log.
Click the icon in the upper-right corner to download the execution log to your computer.

**Execution result explanation**

| Execution result | Description | Running status |
|---|---|---|
| Pending | The tool is waiting for execution. | Launching |

| Preparing | The environment is being prepared. | Launching |
|---|---|---|
| ParamParsing | The parameters are being preprocessed. | Launching |
| TransformBuilding | The workflow is being configured and orchestrated. | Launching |
| ContextBuilding | The workflow context is generated. | Launching |
| WardenLaunching | The workflow engine is started. | Launching |
| TaskRunning | The workflow is running. | Running |
| ParamVerifying | The parameters are waiting for verification. | Interrupted |
| End | The workflow is complete. | Closed |
| W Init _ | The workflow is initialized. | Running |
| W New _ | The workflow is created. | Running |
| W Adopting _ | The workflow is distributed. | Running |
| W Start _ | The workflow is started. | Running |
| W Running _ | The workflow is running. | Running |
| W Done _ | The workflow is being closed. | Interrupted |
| W Closed _ | The workflow is closed. | Closed |
| W Cancelled _ | The workflow is canceled. | Closed |
| W StepError _ | The steps of the workflow are abnormal. | Closed |

| W MaxRetries _ | The maximum number of retries for the workflow is reached. | Closed |
|---|---|---|
| W Paused _ | The workflow is paused. | Interrupted |
| W Rollback _ | The workflow is rolled back. | Running |
| W Misfired _ | The workflow is stopped due to a timeout. | Closed |
| W Escaping _ | The workflow is escaping. | Running |
| W EscapeFail _ | The workflow failed to escape. | Closed |
| W EscapeSuccess _ | The workflow successfully escaped. | Closed |
| W QuotaReached _ | The upper limit for the workflow is reached. | Closed |
| Cleaned | The workflow is deleted as residual data. | Closed |
| Failed | An exception occurred during the workflow execution. | Closed |

## Network resources

### Network asset management

The Network Asset Management page displays network assets in virtual private clouds (VPCs). You can query a network asset by using a property such as Asset Type, IP Address, or Instance ID.

**Prerequisites**

The NetworkBaseServiceCluster cluster for BaseServiceAll is deployed and at desired state.

**Background information**

Only some instances in VPCs are displayed on the Network Asset Management page. You can query specific instances by instance IP address or ID. Filter properties include Asset Type, IP Address, IP Address Version, Network Type, Instance ID, Zone, Product, ClusterName, Service, ServerRole, IP Address Pool ID, Base Resource, Inband Resource, and vpcId. When you query a network asset, you must specify the Product and ClusterName parameters before you specify the Service parameter. When you query a network asset, you must specify the Product, ClusterName, and Service parameters before you specify the ServiceRole parameter.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Resources** > **Network Asset**
**Management**.
4. On the Network Asset Management page, click **Advanced Filter** and search for a network
asset in a VPC by **Asset Type**, **IP Address**, **IP Address Version**, **Network Type**,
**Instance ID**, **Zone**, **Product**, **ClusterName**, **Service**, **ServerRole**, **IP Address Pool ID**,
**Base Resource**, **In-band Resource**, and **vpcId**.
5. Click **Overloaded IP Data** to refresh the IP address data.
6. Find the network asset that you want to view and click **View Details** in the **Operation**
column to view the details of the network asset.

### IP address pool management

#### IP address pool

This feature provides a centralized view of all CIDR blocks declared by cloud services on the platform. You can perform standard O&M tasks, such as adding, expanding, querying, or deleting CIDR blocks to meet your operational requirements. The conflict check feature detects address conflicts when you expand CIDR blocks. It simultaneously checks if a CIDR block contains, or is contained by, another.

**Background**

This feature is suitable for scenarios such as multi-cloud geo-disaster recovery and hybrid cloud. A single instance often hosts multiple cloud services. During O&M tasks like network changes or security audits, you may need to view the CIDR blocks declared by a specific cloud service to analyze the scope of changes or define security policies. This feature shows the CIDR blocks requested by each cloud service within an instance. You can also manually add custom CIDR blocks.

**Procedure**

1. Log on to the Apsara Uni-manager O&M console.
2. In the top navigation bar, choose **Product O&M** > **Network O&M** > **Network O&M**
**Console**.
3. In the left-side navigation pane, choose **Network Resources** > **IP Address Pool**
**Management** > **IP Address Pool**.
4. On the **CIDR Block Management** page, use the following operations to view and manage
CIDR blocks. You can view statistics for **CIDR Block Category**, **Protocol Distribution**, **IPv4 Prefix**
**Distribution**, and **IPv6 Prefix Distribution**.
Add a CIDR block: Click **Manual Entry**. In the panel that opens, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| CIDR Block Name | Enter a name for the CIDR block. |
| CIDR Block Information | Enter the CIDR block information. |
| Protocol Type | Select the protocol type for the CIDR block. IPv4 IPv6 |
| CIDR Block Owner | Select the owner of the CIDR block. Network Device Cloud Service Other |
| Network Type | Select the network type for the CIDR block. Platform Network Tenant Network |
| Region | Select the region to which the CIDR block belongs. |
| Availability Zone | After you select a Region, select an availability zone. |
| CIDR Block Category | Select the category of the CIDR block. Private CIDR Block Public CIDR Block Public IP address for private use Other |

| Product Name | Select the product name to which the CIDR block belongs. |
|---|---|
| Cluster Name | After you select a Product Name, select the cluster name for the CIDR block. |
| Service Name | After you select a Cluster Name, select the service name for the CIDR block. |
| Service Role | After you select a Service Name, select the service role for the CIDR block. |
| IDC | Select the IDC for the CIDR block. |
| Associated Network Device | After you select an IDC, select the source network device for the CIDR block. |
| Associated Network Interface | After you select an IDC, select the associated network interface for the CIDR block. |
| Remarks | Enter remarks for the CIDR block. |
| Enable | Specify whether to enable the CIDR block. |
| Expiration Time | Set an expiration time for the CIDR block. |

CIDR block conflict verification a. Click **Conflict Verification**. In the dialog box that appears, under **CIDR Block**
**Information**, enter the target CIDR block.
b. Click **Detect**. The system displays the conflict check result. Query CIDR blocks a. Click **Advanced Search** and set filter conditions by using a combination of **ID**,
**IPResourceName**, **CIDR Block Information**, **Protocol**, **Product**, **Cluster Name**,
**Service Name**, **Service Role**, **Enablement Status**, and **CIDR Block Category**.
b. Click **Search** to find the target CIDR blocks. View the CIDR block list: The list includes information such as **ID**, **CIDR Block**
**Information**, **IPResourceName**, **Protocol**, **CIDR Block Category**, **Network Type**,
**Enablement Status**, **Region**, **Availability Zone**, **Product**, **Service Name**, **Server**
**Role**, **Source Device**, **Associated Port**, and **Last Update**.
View CIDR block details: In the **Actions** column of a target CIDR block, click **Details**. In the panel that appears, view the detailed information about the CIDR block. Delete a CIDR block To delete a CIDR block, click **Delete** in its **Actions** column. In the confirmation dialog box, click **OK**.

#### Collection settings

On the Collection Settings page, you can view the collection settings of the IP address pools of cloud services across the platform. You can also trigger a data update for a single IP address pool on this page.

**Background information**

The collection settings feature is applicable to scenarios such as multi-cloud geo-disaster recovery and hybrid clouds. This feature allows you to perform the following operations: View the collection rules of IP address pools of all cloud services across the cloud platform. Trigger a data update for a single IP address pool.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Resources** > **IP Address Pool**
**Management** > **Collection Settings**.
4. On the Collection Settings page, find the IP address pool that you want to manage by the IP
address pool name and view the CIDR block collection settings of the IP address pool.
5. Click **Details** in the **Operation** column. In the Details panel, view the details of the IP
address pool.
6. Click **Single trigger** in the **Operation** column. In the message that appears, click **OK**.
Then, the system displays the trigger result.

### Reverse access

The reverse access feature implements active access from base cloud services to virtual private clouds (VPCs) by establishing NAT mappings.

**Create a reverse access instance**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Resources** > **Reverse Access**.
4. On the Cloud Service Reverse Access page, click **Create Reverse Access Instance**. In the
dialog box that appears, configure the following parameters and click **Create Application**. After the instance is created, an application ID that is automatically assigned by the system for the instance is displayed on the Cloud Service Reverse Access page.

| Parameter | Description |
|---|---|
| Application Name | The name of the application. |
| Application Description | The description of the application. |
| uid | The user ID that is used for resource management. This parameter is required. |

5. In the **Server Address Pool Settings** section, configure the following parameters and
click **Create**.

| Parameter | Description |
|---|---|
| Address Pool ID | The ID of the address pool of the application server. If you leave this parameter empty, a new address pool ID is created. |
| Address Pool Name | The name of the address pool. |
| Address Pool Description | The description of the address pool. |

| Creation Mode | The creation type of the application server. Valid values: Within VPC Outside VPC Note If you select application servers in a VPC, you can add multiple application servers in the same VPC at a time. Separate the server IDs or IP addresses with commas (,). |
|---|---|
| vpcId | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The ID of the VPC in which the application server resides. |
| serverIds | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The IDs of the application servers to be added. You can add multiple application servers at a time. Separate the server IDs with commas (,). |
| vswitchId | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The ID of the vSwitch to which the application server belongs. |
| mappingIp | This parameter takes effect only if you set the Creation Mode parameter to Within VPC. The mapping IP address that is created for the specified vSwitch. The IP address is used to map the IP address of the application server. Note If the existing mapping IP addresses in the vSwitch are not used up, the mapping IP address created in this step may not be used. If no mapping IP addresses exist in the vSwitch and you do not create a mapping IP address in this step, an error may be reported later. |
| serverIps | This parameter takes effect only if you set the Creation Mode parameter to Outside VPC. The classic network IP addresses of the application servers to be added. |

6. Configure the following parameters and click **Create ECS Authorization**.

| Parameter | Description |
|---|---|
| VPC ID | The ID of the VPC in which the Elastic Compute Service (ECS) instance that you want to authorize the reverse access instance to access resides. |
| Creation Mode | The creation type of the ECS authorization. Valid values: Instance ID Instance IP Address |
| instanceId | This parameter takes effect only if you set the Creation Mode parameter to Instance ID. The ID of the ECS instance to be accessed. |
| instanceIp | This parameter takes effect only if you set the Creation Mode parameter to Instance IP Address. The private IP address of the ECS instance to be accessed. |
| instancePort | The port of the ECS instance to be accessed. |

7. View the details of a reverse access instance.
i. Find the reverse access instance that you want to view and click **Details** in the
**Operation** column.
ii. On the **Reverse Access Instance Details** page, view the instance details in the **Basic**
**Information** section and on the **Server Address Pool** and **ECS Reverse**
**Authorization** tabs.
iii. On the **Server Address Pool** tab, perform the following operations.

| Operation | Procedure |
|---|---|
| Create an address pool | a. Click Create Address Pool. b. In the dialog box that appears, configure the parameters as described in Step 5 and click Create. |

| View the server details of an address pool | a. Find the address pool that you want to view and clickS erver Details in the Operation column. In the Server Details panel, view the server details of the address pool. b. The server details are displayed in the following columns: VPC ID, Server ID, Server IP, Server Mapping IP, Server Type, and Status. Note To add an application server, click Add Application Server To delete an application server, find the application server that you want to delete and click Delete in the Operation column. |
|---|---|
| Modify an address pool | a. Find the address pool that you want to modify and clickM odify in the Operation column. b. In the dialog box that appears, modify the parameters and clickM odify. Note You can modify only the Name and Description parameters. |
| Delete an address pool | a. Find the address pool that you want to delete and clickD elete in the Operation column. b. In the message that appears, click Delete. Note Before you delete an address pool, you must delete all application servers that are associated with the address pool. Otherwise, the address pool cannot be deleted. The address pool is deleted immediately after you click Delete. Proceed with caution. |

iv. On the **ECS Reverse Authorization** tab, perform the following operations.

| Operation | Procedure |
|---|---|
| Create an authorization | a. Click Authorize. b. In the dialog box that appears, configure the parameters as described in Step 6 and click Create ECS Authorization. |
| Delete an authorization | a. Find the authorization that you want to delete and clickD elete in the Operation column. b. In the message that appears, click Delete. Note The authorization is deleted immediately after you click Delete. Proceed with caution. |

**What to do next**

**Modify a reverse access instance**

1. Find the reverse access instance that you want to modify and click **Modify** in the
**Operation** column.
2. In the dialog box that appears, modify the parameters and click **Modify**.

**Note**

You can modify only the **Instance ID/Name** and **Description** parameters.

**Delete a reverse access instance**

1. Find the reverse access instance that you want to delete and click **Details** in the
**Operation** column.
2. On the **Reverse Access Instance Details** page, click **Delete Instance** in the upper-right
corner.
3. In the message that appears, click **Delete**.

**Note**

Before you delete a reverse access instance, you must delete all application servers and address pools that are associated with the instance. Otherwise, the instance cannot be deleted.

### Cloud instance management

This topic describes how to manage the lifecycle of cloud instances, including creating instances, deleting instances, and querying instance status.

**Create a cloud instance**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Resources** > **Cloud Instance**
**Management**.
4. On the **Cloud Instance Management** page, choose **Create Instance** > **Create**
**Instance**.
5. On the **Create Instance** page, perform the following steps to create an instance.

**Step 1: Create a VPC**

In the **Create VPC** step, configure the following parameters and click **Create**.

| Parameter | Description |
|---|---|
| RegionID | The ID of the region in which the virtual private cloud (VPC) resides. |
| Cloud Service Instance ID | The ID of the VPC. |
| Tunnel Type | SingleTunnel: specifies a SingleTunnel virtual IP address (VIP) that allows a single Elastic Compute Service (ECS) instance in the VPC to access external cloud services. AnyTunnel: specifies an AnyTunnel VIP that allows all ECS instances in the VPC to access the specified cloud service. |
| IpVersion | The protocol. The default value is Ipv4. Valid values: Ipv4 Ipv6 |
| CloudInstance IP | The VIP that you want to assign to the VPC. If you do not specify a VIP, the system automatically assigns one. |
| Vswitch ID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The ID of any vSwitch in the VPC to which the ECS instance that needs to access external cloud services belongs. |
| UID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The UID of the user that creates the vSwitch. This parameter is required if the user is not the API caller. |

| BID | This parameter is available only when the Tunnel Type parameter is set to SingleTunnel. The BID of the user that creates the vSwitch. This parameter is required if the user is not the API caller. |
|---|---|
| CIDR Type | This parameter is available only when the Tunnel Type parameter is set to AnyTunnel. Link local (Regular Cloud Services): The AnyTunnel VIP assigned to _ Application Load Balancer (ALB) is allocated from a subnet that does not belong to 100.100.100.0/24. Special Inner (ECS META Server) Service: The AnyTunnel VIP assigned to ALB is allocated from a subnet that belongs to 100.100.100.0/24. |

**Step 2: Add backend servers to an SLB instance**

In the **Add RS to SLB Instance** step, configure the following parameters and click **Create**.

| Parameter | Description |
|---|---|
| VPC ID | The ID of the VPC in which the ECS instances that you want to add are deployed. This parameter is required if you want to add ECS instances deployed in a VPC. |
| RS List | The backend servers (ECS instances) that you want to add to the Server Load Balancer (SLB) instance. IP: the IP address of the backend server. weight: The weight of the backend server. Valid values: 0 to 1000. If you leave the parameter empty, the default value 100 is used. Note Click Add RS to add multiple backend servers. Click Delete in the Actions column of a backend server to remove the backend server. |

**Step 3: Create listeners**

In the **Create Listener** step, configure the following parameters and click **Create**.

| Parameter | Description |
|---|---|
| Protocol | The listener protocol. Valid values: Tcp Udp |
| Frontend Port | The frontend port of the VIP. |
| Backend Port | The service port on the backend server. |
| Configurations | Click Configurations to specify Scheduling Policy, Session Persistence (Seconds), and Health Check Method. |

**Note**

You can click **Add Listener** to add multiple listeners. Click **Delete** in the Delete column of a listener to delete the listener.
6. Optional. After the cloud instance is created, it enters the **Working** state. You can go to the
**Cloud Instance Management** page and view the instance in the instance list.

**Apply for a Direct AnyTunnel VIP**

1. On the **Cloud Instance Management** page, choose Create Instance > **Create Direct**
**Any Tunnel**.
2. On the **Create Direct Any Tunnel VIP** page, configure the following parameters and click
**Create**.

| Parameter | Description |
|---|---|
| RegionID | Displays the region ID of the cloud instance. |
| Cloud Service Instance ID | The ID of the cloud instance. By default, the ID of a random cloud instance is displayed. |
| Tunnel Type | You can select only Direct Any Tunnel. After a Direct AnyTunnel VIP is obtained, all ECS instances in the VPC can use the VIP to access the specified cloud service. |
| CloudInstance IP | Enter the IP address of the cloud instance. If you do not specify a VIP, the system automatically assigns one. |
| CIDR Type | Link local (Regular Cloud Services): The Direct AnyTunnel VIP is _ allocated from a subnet that does not belong to 100.100.100.0/24. Special Inner (ECS META Server) Service: The Direct AnyTunnel VIP is allocated from a subnet that belongs to 100.100.100.0/24. |

3. Optional. After the Direct AnyTunnel is created, it enters the **Working** state. You can go
back to the **Cloud Instance Management** page and view it in the instance list.

**Manage existing resources**

**Prerequisites**

The existing resource management operation is not performed.

**Procedure**

**Important**

The existing resource management operation attempts to manage **SingleTunnel**,
**AnyTunnel**, and **Direct AnyTunnel** resources created in Apsara Network
Intelligence. You cannot repeat this operation after all resources are successfully managed. After you perform this operation, if instances whose **Tunnel Type** is
**InvalidResource** are displayed, the instances are abnormal resources in Apsara
Network Intelligence. The creation of the instances may be terminated or the instances may be invalid. The status of these instances displays **Invalid**. You can only view and delete these instances. You cannot modify the backend servers or listeners of these instances. To do this, you need to delete the existing instances and recreate them.
1. On the **Cloud Instance Management** page, click **Existing Resource Management**
above the list.
2. In the message that appears, confirm the information and click **OK**. Then, resource
management starts.
3. Refresh the **Cloud Instance Management** page. If an instance ID that does not start with
noe appears, existing resource management is performed. If all resources are managed, the **Existing Resource Management** feature is dimmed. If some resources fail to be managed, **Failed to manage some resources.** is displayed. You can retry to manage the failed resources. a. Click **Failed to manage some resources** above the list. b. In the message that appears, click **OK** to try again.

**What to do next**

| Operation | Description |
|---|---|
| Modify backend servers | Note You cannot modify the backend servers of instances whose Tunnel Type is DirectAnyTunnel. You cannot modify the backend servers of instances whose status is Create Failed or Invalid. 1. Click Edit RS in the Operation column of a cloud instance. 2. In the dialog box that appears, modify the backend server parameters and click OK. For more information, see the Step 2: Add backend servers to an SLB instance section of this topic. 3. Optional. If you failed to modify the backend servers and the cloud instance is in the Update Failed state, click Edit RS to update the backend server list again. |
| Modify listeners | Note You cannot modify the listeners of instances whose Tunnel Type is DirectAnyTunnel. You cannot modify the listeners of instances whose status is Create Failed or Invalid. 1. Click Modify Listener in the Operation column of a cloud instance. 2. In the dialog box that appears, modify the listener parameters and click OK. For more information, see the Step 3: Create listeners section of this topic. 3. Optional. If you failed to modify the listeners and the instance is in the Update Failed state, click Edit RS to update the listener list again. |
| Delete a cloud instance | 1. Click Delete in the Operation column of a cloud instance to delete the cloud instance. 2. In the message that appears, click OK. |

## Network changes

The network change feature simplifies the process of configuring switches in mainstream scenarios, such as expanding the RAMA CIDR blocks, expanding the CIDR blocks of kernelbased virtual machines (KVMs), expanding the virtual IP address (VIP) range of Server Load Balancer (SLB) instances, and expanding the access switch (ASW) CIDR blocks.

### Change plans

#### Change plan list

The change plan list module displays all available change plans.

**Prerequisites**

Incremental planning is complete on Apsara Stack Deployment Planner, and the desired state file is obtained. Switches are installed, deployed, and connected based on incremental planning. Switches are powered on, and the latest patches are installed. The association with distribution switches (DSWs) is completed.

**View the change plan list**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Changes** > **Change Plan** > **Change**
**Plan List**.
4. On the **Change Plans** page, you can view information about built-in change plans,
including **Solution Name**, **Risk Level**, **Affected Product**, **Number of Executions**, and
**Description**. For more information about built-in change plans, see the Built-in change
plans section of this topic. To import change plans, click **Import** above the list and upload a local file. To filter change plans, click **Advanced Filter** and configure the **Solution Name**, **Risk**
**Level**, and **Affected Product** parameters.
To view the execution history of a change plan, click the number in the **Number of**
**Executions** column of the change plan to go to the **Execution History** page. For more
information, see the Search for an execution section in the Execution history topic.

**Built-in change plans**

| N o. | Change plan | Risk level | Description |
|---|---|---|---|
| 1 | Switch Account Password Update | High risk | This change plan applies to scenarios where you want to change the password of a switch based on your business requirements or password strategy. You must save the new password. |
| 2 | ACL Rule Configuration | High risk | This change plan applies to scenarios where you want to create access control list (ACL) rules for switches. You can use the change plan to create multiple ACL rules at a time. Ports whose configurations are changed at a time use the same ACL rules. You cannot add rules to an existing ACL. Otherwise, when you roll back this change plan, the ACL is deleted. |
| 3 | Incremental Deployment of ASW for Apsara Stack Enterprise Cloud Platform | Low risk | This change plan applies to scenarios where you want to perform incremental deployment for Access Switches (ASWs) on Apsara Stack. |
| 4 | CGW 3AZ Disaster Recovery Configuration | High risk | This change plan applies only to scenarios where you deploy a single Cloud Gateway (CGW) cluster across three zones. |

| 5 | Classic Network and IDC Networking | High risk | This change plan applies to scenarios where you want to connect a data center to the classic network by using inter- connection switches (ISWs) or customer switches (CSWs). This change plan allows you to configure the network quality analysis (NQA) instance and static routes for switches by using physical interfaces or subinterfaces. The change plan supports switches that are deployed in the single-zone, active/standby, or active-active mode. Separate input parameters with commas (,). |
|---|---|---|---|
| 6 | EIP IP Pool Expansion | Low risk | This change plan applies to scenarios where you want to expand the elastic IP address (EIP) CIDR block when EIPs are insufficient on Apsara Stack V3. |
| 7 | Keyserver Node Offline | High risk | This change plan applies to scenarios where you want to undeploy keyservers. This operation includes the removing traffic from Server Load Balancer (SLB), verifying traffic draining, and terminating the service process steps. |
| 8 | Keyserver Node Online | High risk | This change plan applies to scenarios where you want to deploy keyservers. This operation includes the launching the service process, verifying process status, and distributing traffic to SLB steps. |
| 9 | KVM Docker IP Segment Addition | Low risk | This change plan applies to scenarios where you want to add a CIDR block for kvm docker. _ |
| 1 0 | KVM Docker IP Segment Expansion | Low risk | This change plan applies to scenarios where you want to expand the CIDR block of kvm docker. _ |
| 1 1 | LVS Node Offline | High risk | This change plan applies to scenarios where you want to undeploy Linux Virtual Server (LVS) nodes. This operation includes the disabling traffic throttling, removing traffic from nodes, stopping configuration updates, and terminating the SLB forwarding process steps. |
| 1 2 | LVS Node Online | High risk | This change plan applies to scenarios where you want to deploy LVS nodes. This operation includes the launching the SLB forwarding process, enabling prechecks, enabling configurations, performing a deployment precheck, distributing traffic to nodes, and enabling traffic throttling steps. |
| 1 3 | Pre-check for Physical Connection Addition and Reuse in VPC IDC Networking Scenario | Low risk | This change plan applies to scenarios where you want to precheck the environment before you add or reuse an Express Connect circuit to connect a virtual private cloud (VPC) and a data center. |
| 1 4 | Add Rama IP Segment | Low risk | This change plan applies to scenarios where you want to add a CIDR block for RAMA. |

| 1 5 | Rama IP Segment Expansion | Low risk | This change plan applies to scenarios where you want to expand the RAMA CIDR block. |
|---|---|---|---|
| 1 6 | XGW/CGW Cluster Active-Standby Configuration | High risk | This change plan applies to scenarios where you want to configure the replication relationship for Extendable Gateway (XGW) or CGW clusters. |
| 1 7 | SLB VIP Address Pool Expansion | Low risk | This change plan applies to scenarios where you want to expand the virtual IP (VIP) range when the IP addresses in the VIP resource pool are insufficient or the reserved CIDR blocks are insufficient. |
| 1 8 | SNMP Configuration | High risk | This change plan applies to scenarios where you want to set the SNMP configuration for a network device when you configure network monitoring for it. |
| 1 9 | VPC anytunnel cidr _ Network Segment Expansion | Low risk | This change plan applies to scenarios where the CIDR block of the classic network is expanded and the new CIDR block must be added to anytunnel cidr to enable _ communication between the services in the new CIDR block and VPCs. |
| 2 0 | Add VPC CIDR for Public IP Private Use | High risk | The private CIDR blocks of a VPC are specified by the private cidr table in the key value config info _ _ _ _ configuration of the VPC in Apsara Stack. After you associate an EIP with an Elastic Compute Service (ECS) instance deployed in the VPC, the ECS instance routes data based on the private network configuration specified by the private cidr table. If you want to use public IP _ addresses or pseudo-public IP addresses as private IP addresses, you can assign these public IP addresses to an application virtual switch (AVS) as private CIDR blocks. To do this, modify the vpc default private cidr parameter in _ _ _ the key value config info configuration. You can also _ _ _ modify the User cidr table of the VPC to use the custom _ private network configuration. |
| 2 1 | VPC mapping server _ Address Pool Expansion | Low risk | Apsara Stack provides the reverse access feature that allows one-way access from the classic network to VPCs. A certain number of IP addresses are reserved for reverse access during the delivery. The reserved IP addresses may be exhausted. In this case, you can execute this change plan to expand the IP addresses for reverse access. |
| 2 2 | XGW Node Traffic Diversion Operation | High risk | This change plan applies to scenarios where you want to perform XGW node traffic redirection, including configuration distribution, status update, and post- verification. |
| 2 3 | GW Node Online/Offline Operation Pre-check | Low risk | This change plan applies to scenarios where you want to perform an environment precheck before XGW node deployment or undeployment to ensure the security of the operation. |

| 2 4 | XGW Node Offline Operation | High risk | This change plan applies to scenarios where you want to undeploy an XGW node. This operation includes the precheck, node undeployment, and post-verification steps. |
|---|---|---|---|
| 2 5 | XGW Node Online Operation | High risk | This change plan applies to scenarios where you want to deploy an XGW node. This operation includes the precheck, node deployment, and post-verification steps. |

**View the details of a change plan**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Changes > Change Plan** > **Change**
**Plan List**.
4. On the **Change Plans** page, find the change plan that you want to view and click **Details**
in the **Actions** column.
5. On the **Change Plan Details** page, view the details of the change plan.
**Basic Information**: displays **Solution Code**, **Name**, **Risk Level**, **Affected Product**,
**Version**, **Description of Applicable Conditions**, and **Scenario Description**.
**Flowchart**: displays the execution process of the change plan, including the **Parameter**
**Check** step and subsequent steps.
The steps after Parameter Check vary based on the change plan. Click the icon of a step to view the details of the step, including **Step Information** and
**Execution Information**.

**Create a change workflow**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Changes > Change Plan** > **Change**
**Plan List**.
4. On the **Change Plans** page, find the change plan that you want to execute and click
**Initiate Execution** in the **Actions** column.

**Note**

You can also click **Initiate Execution** in the upper-right corner of the **Change Plan**
**Details** page to create a change workflow.
5. In the **Initiate Execution** dialog box, configure the parameters and click **OK**.
The parameters vary based on the change plan.
6. After the change workflow is created, you are redirected to the **Execution Details** page.
You can view the execution status of the workflow. For more information, see the View the details of an execution section in the Execution history topic.

#### Plan execution history

This topic describes how to view the execution history of change plans on the Execution History page.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Network Changes** > **Chang Plan** > **Execution**
**History**.
4. On the **Execution History** page, view the execution details of change plans in the
following columns: **Workflow ID**, **Plan Name**, **Description**, **Execution Time**, **Execution**
**Result**, **Executed By**, and **Execution Parameters**.

**Search for an execution**

To filter executions, click **Advanced Filter** and configure the **Plan Name**, **Execution**
**Result**, **Execution Time**, **Submitted By**, **Workflow ID**, and **Execution Parameters**
parameters.

**Note**

For more information about the definitions of execution results, see the Definitions of execution results section of this topic.

**View the details of an execution**

Find the execution that you want to view and click **View Details** in the **Actions** column. On the **Execution Details** page, view the details of the execution.

**Note**

The execution details vary based on the change plan.
**Basic Information**: displays **Solution Name**, **Solution Code**, **Workflow ID**,
**Execution Time**, **Execution Status**, **Submitted By**, **Affected Product**, **Risk Level**,
**Workflow Is Rolled Back or Not**, **Description of Applicable Conditions**, and
**Scenario Description**.
If **Execution Status** is W_Running, wait until the status changes to ParamVerifying. If **Execution Status** is ParamVerifying, the workflow is paused until the executor confirms the parameter check results. If **Execution Status** displays an abnormal state, such as Failed or W_MaxRetries, suspend the execution, troubleshoot issues based on the execution log, and then continue the execution or re-execute the change plan. If **Execution Status** is W_MaxRetries, you can retry the workflow. When **Execution Status** changes to End, the workflow is complete.
**Execution Progress**: displays the status of each step in the workflow. The steps are
the same as those in the change plan flowchart. Click **Proceed**, **Suspend**, or **Terminate** to resume, pause, or stop the workflow. Click **View Details** below a step to view the step details.
**Basic Information**: displays the basic information about the step.
**Execution Information**: displays **Last Execution Information**, **Last Execution**
**Environment Variable**, and **Execution History**.
In the **Execution History** section, find the execution that you want to view and move the pointer over **Details** in the **Actions** column to view the execution details.
**Parameter Information**: displays **Input Parameters** and **Output Parameters**.
The name, type, and description of each parameter are displayed. Click **Confirm Parameters** in the **Parameter Check** section to view the parameter check results of the check items of the workflow and determine whether the check results are normal. Click **Approved** to continue to run the workflow. Click **Terminate Workflow** to terminate the workflow. Click **Retry** below a step to re-execute the step.

**Execution Information**

**Event Records**: displays the reported events.
**Parameter Information**: displays parameter check results in the **Parameter**
**Check** section and input parameters in the **Input Parameters** section.
**Execution Logs**: displays the latest 1,000 execution log entries. You can turn on
**Automatic Refresh**.
You can also click the icon in the upper-right corner to download the execution log to your computer.

**Definitions of execution results**

| Execution result | Description | Status |
|---|---|---|
| Pending | The change plan is waiting for execution. | Launching |
| Preparing | The environment is being prepared. | Launching |
| ParamParsing | The parameters are being preprocessed. | Launching |

| TransformBuilding | The workflow is being configured and orchestrated. | Launching |
|---|---|---|
| ContextBuilding | The workflow context is generated. | Launching |
| WardenLaunching | The workflow engine is started. | Launching |
| TaskRunning | The workflow is running. | Running |
| ParamVerifying | The parameters are waiting for verification. | Interrupted |
| End | The workflow is complete. | Closed |
| W Init _ | The workflow is initialized. | Running |
| W New _ | The workflow is created. | Running |
| W Adopting _ | The workflow is distributed. | Running |
| W Start _ | The workflow is started. | Running |
| W Running _ | The workflow is running. | Running |
| W Done _ | The workflow is being closed. | Interrupted |
| W Closed _ | The workflow is closed. | Closed |
| W Cancelled _ | The workflow is canceled. | Closed |
| W StepError _ | The steps of the workflow are abnormal. | Closed |
| W MaxRetries _ | The maximum number of retries for the workflow is reached. | Closed |
| W Paused _ | The workflow is paused. | Interrupted |
| W Rollback _ | The workflow is rolled back. | Running |

| W Misfired _ | The workflow is stopped due to a timeout. | Closed |
|---|---|---|
| W Escaping _ | The workflow is escaping. | Running |
| W EscapeFail _ | The workflow failed to escape. | Closed |
| W EscapeSuccess _ | The workflow successfully escaped. | Closed |
| W QuotaReached _ | The workflow engine has reached the workflow upper limit. | Closed |
| Cleaned | The workflow is deleted as residual data. | Closed |
| Failed | An exception occurred during the workflow execution. | Closed |

### Feature orchestration

#### IPv6 dashboard

This topic describes how to view the IPv6 service capability and IPv6 status for cloud services on the Apsara Stack platform that use a baseline to request VIP resources.

**Procedure**

1. Log on to the Apsara Uni-manager O&M console.
2. In the top navigation bar, choose **product O&M** > **network O&M** > **network O&M**
**console**.
3. In the left-side navigation pane, choose **network change** > **feature orchestration** >
**IPv6 dashboard**.
4. The **IPv6 Status of Cloud Services** page lists the cloud services on the Apsara Stack
platform that support IPv6. This list includes columns such as **product**, **cluster**, **data**
**center**, **IPv6 service capability**, **IPv6 status**, **IPv6 enabled time**, and **last**
**synchronized time**.
Click **advanced filter** to filter the cloud services by a combination of **data center**,
**product**, **cluster**, and **IPv6 enabled** status.
In the **Actions** column for a target cluster, click **refresh cluster status** to update the cluster's status. In the **Actions** column for a target cluster, click **IPv6 service dependencies**. A dialog box opens, displaying the service dependencies of the cluster and the IPv6 status of each service. In the **Actions** column for a target cluster, click **enable IPv6**. a. In the dialog box that appears, review and confirm the IPv6 status of the dependent services, and then click **OK**.

**Note**

Before you enable IPv6, check for any service dependencies. You must enable IPv6 for these dependencies first. b. In the dialog box that appears, verify that IPv6 is enabled for all dependent services, and then click **OK**. c. You are redirected to the details page of the service orchestration execution record, which shows the progress of enabling IPv6 for the cluster. For more information, see the **Execution Record** chapter in the **O&M Services** section of the **Apsara Stack O&M Platform User Guide**.

## Platform management

### Log management

#### Query logs

This topic describes the log query feature. This feature allows you to query the logs of products and server roles by EagleEye ID. This helps you quickly troubleshoot issues.

**Prerequisites**

The read and write permissions on Log Center are obtained.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Platform Management > Log Management >**
**Log Query**.
4. On the **Platform Logs** tab, filter logs by **Products**, **Log Type**, **Log Name**, **Time Range**,
and **Query Conditions**.

**Note**

You can select multiple values for **Products**, **Log Type**, and **Log Name**. When you specify **Query Conditions**, you can enter a keyword to query data. You can specify a query condition that contains the and, or, and not operators. Example: (44 or http) and error not fatal.
5. View the query results displayed in the lower part of the page.

| Section | Description |
|---|---|
| Log directory | Enter a log name or server role to search for a log. Click the log and then view its details displayed on the right side. |
| Basic information | View the following information: Product Name, Service Name, Service Role, Log Name, Logs, and Error Logs. |

| Log list | You can click Export List to export the logs to your on-premises machine. You can enter a keyword to search for the desired log. You can select Show exception logs only to view only exception logs. You can click List or Aggregation to switch between the list and aggregation modes. Note In List mode, you can click Details in the Operation column of a log to view the log content. |
|---|---|

6. On the **Local Logs** tab, filter logs by **Products**, **Service**, **Component**, and **Log Path**.
7. In the lower part of the page, click the desired machine on the left side, and then view its
logs displayed on the right side.

**Note**

You can filter logs by **Time Range** and **Keyword**. You can click **Export Logs** to export the logs to your on-premises machine.

### Metric management

#### TSDB clusters

This topic describes how to query time series database (TSDB) clusters and view the details of stored time series metrics.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Platform Management > Indicator**
**Management > TSDB Cluster**.
4. On the **TSDB Multi-cluster Management Page**, view the information in the **Zone List**
section. The cluster information includes Cluster ID, Zone, **Cluster Name**, **Cluster Type**, **Access**
**Point Information**, **Service Nodes**, and **Configurations**.
Click **Advanced Filter** and filter clusters by **Cluster ID**, **Zone**, **Cluster Name**, **Cluster**
**Type**, or any combination of them.
Find the cluster that you want to view, and click **Details** in the **Access Point**
**Information** column. In the dialog box that appears, view the endpoint information
about the cluster. Find the cluster that you want to view, and click **Details** in the **Service Nodes** column. In the dialog box that appears, view the service nodes of the cluster. Find the cluster that you want to view, and click **Details** in the **Configurations** column. In the dialog box that appears, view the configurations of the cluster.
