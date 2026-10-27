---
title: "Alibaba Cloud Apsara Stack V3.18.3 cloud gateway Operations and Maintenance Guide 20250121"
product_version: "V3.18.3"
doc_version: "20250121"
pdf_pages: 77
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 cloud gateway Operations and Maintenance Guide 20250121.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20cloud%20gateway%20Operations%20and%20Maintenance%20Guide%2020250121.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 cloud gateway Operations and Maintenance Guide 20250121

## Table of Contents

- 1 Log on to the Apsara Uni-manager Operations Console
- 2 Connect a bare metal instance to a VPC
  - 2.1 Manage cloud access gateways
  - 2.2 View the operation logs
  - 2.3 Network management for bare metal instances
    - 2.3.1 View network information about bare metal instances in a VPC
    - 2.3.2 Create a bare metal instance and add the instance to a VPC
    - 2.3.3 Close the connection between a bare metal instance and a VPC
    - 2.3.4 Manage IP addresses for bare metal instances
  - 2.4 O&M configurations
    - 2.4.1 Apply for a bare metal instance in a VPC
    - 2.4.2 Release a bare metal instance in a VPC
    - 2.4.3 View the bandwidth of the Express Connect circuit
    - 2.4.4 Modify the bandwidth of the Express Connect circuit
- 3 CPN
  - 3.1 CPN diagnosis
  - 3.2 CPN performance analysis
  - 3.3 CPN access gateways
    - 3.3.1 Manage RDMA devices
    - 3.3.2 Manage RDMA device policies
    - 3.3.3 Manage policies for the RDMA device interface
  - 3.4 RDMA NIC O&M
  - 3.5 CPN management
    - 3.5.1 CPN topology
    - 3.5.2 CPN network element
  - 3.6 CPN network monitoring
    - 3.6.1 CPN host monitoring dashboard
    - 3.6.2 CPN switch dashboard
    - 3.6.3 NAK packet analysis tool
- 4 Connection of intelligent computing servers to VPCs
  - 4.1 Manage access gateways
  - 4.2 Manage operation logs
  - 4.3 Manage networks for bare metal instances
  - 4.4 O&M configurations
    - 4.4.1 Apply for a bare metal instance in a VPC
    - 4.4.2 Release a bare metal instance in a VPC
    - 4.4.3 Delete a route table entry
    - 4.4.4 Delete a router interface
    - 4.4.5 Delete a VBR
    - 4.4.6 Delete an Express Connect circuit
    - 4.4.7 Delete all resources
    - 4.4.8 View the bandwidth of the Express Connect circuit
    - 4.4.9 View trunk usage
    - 4.4.10 View BM VPN usage
    - 4.4.11 View BD usage
    - 4.4.12 Check the initialization configuration
    - 4.4.13 Check the route configuration
    - 4.4.14 Display information about bare metal network gateways
- 5 Traffic visualization
  - 5.1 Configure traffic visualization
    - 5.1.1 Manage analysis devices
    - 5.1.2 Manage collection rules
    - 5.1.3 Manage scenarios
  - 5.2 Visualized overview
  - 5.3 Traffic search and scheduling

ager Operations Console

## 1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The URL, username, and password that are required to log on to the Apsara Uni-manager Operations Console are obtained from the deployment personnel or administrators. The URL of the Apsara Uni-manager Operations Console is in the format of regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the URL. Then, press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter your username and password.

> **Note:** To obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console, contact the deployment personnel or administrators.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username as prompted. To enhance security, make sure that the password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length. ager Operations Console
4. Click **Log On**.
e to a VPC

## 2 Connect a bare metal instance to a VPC

**instance to a VPC**

You can connect bare metal instances to a virtual private cloud (VPC) by using Central Gateway (CGW) to manage the instances in a centralized manner. CGW is a dedicated hybrid switch (HSW) device. The system supports operations such as instance management, operation log management, bare metal network management, and O&M configurations to complete the daily O&M operations of CGW.

### 2.1 Manage cloud access gateways

**gateways**

On the Instance Management tab, you can add cloud access gateway devices to the cloud platform for centralized management. You can also view information about cloud access gateways, such as the cloud access gateway name, internal Border Gateway Protocol (iBGP) role, and creation time.

**Procedure**

## 1 Log on to the Apsara Uni-manager Operations Console.

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the **Instance Management** tab, click the **Scan for New Devices** tab.
5. Find the device that you want to manage and click **Manage** in the **Actions** column.
You can also select multiple devices that you want to manage and click **Batch Manage** below the device list.
6. Configure the **IBGP Role** parameter for the device.
The iBGP role specifies the role that the cloud access gateway plays in the environment. Valid values: Client, Deploy Client and RR on A Device, and Deploy RR on a Device.
**Client**: indicates that the cloud access gateway serves as the client of the iBGP peer and
only serves as a server.
**Deploy Client and RR on A Device**: indicates that the cloud access gateway serves as
the RR reflective route of the iBGP peer and serves as a server.
**Deploy RR on a Device**: indicates that the cloud access gateway only serves as the RR
reflective route of the iBGP peer.

> **Important:** The following list describes the networking requirements for the iBGP role:
> Single-data center deployment: The data center is deployed with at least one set of cloud access gateways, and the iBGP roles of the cloud access gateways are RR roles. The iBGP roles of other devices are Client.
> Multi-data center deployment: At least two data centers are separately deployed with a set of cloud access gateways, and the iBGP roles of the cloud access gateways are RR roles. The iBGP roles of other devices are Client.
> The following list describes the recommended RR role settings:

e to a VPC

> By default, the recommended value is Deploy Client and RR on A Device.
> If you have high requirements on network stability, we recommend that you select Deploy RR on a Device.

7. Click **OK**.

**View cloud access gateways**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. On the **Instance Management** tab, click the **Display Devices** tab to view the cloud
access gateway details.

| Parameter | Description |
|---|---|
| Cloud Gateway Name | The name of the cloud access gateway. |
| IBGP Role | The role of the cloud access gateway in the environment. Client: indicates that the cloud access gateway serves as the client of the iBGP peer and only serves as a server. Deploy Client and RR on A Device : indicates that the cloud access gateway serves as the RR reflective route of the iBGP peer and serves as a server. Deploy RR on a Device: indicates that the cloud access gateway only serves as the RR reflective route of the iBGP peer. |
| Manage IP Address | The IP address of the cloud access gateway. |
| Management status | The initialization status of the cloud access gateway. Not Initialized Initializing Initialized |

e to a VPC

| Authorization Status | The authorization status of the cloud access gateway. Unauthorized Authorized Note To use cloud access gateway devices, you must plan the number of cloud access gateway licenses in Apsara Stack Deployment Planner. If the number of cloud access gateway licenses planned in Apsara Stack Deployment Planner is less than the number of cloud access gateway devices, the devices without licenses are in the Unauthorized state. You must apply for licenses for these devices. |
|---|---|
| Created At | The time when the cloud access gateway was created. |

### 2.2 View the operation logs

To meet O&M requirements, you can view the API records and results that are managed by bare metal instances and called by the Apsara Uni-manager Operations Console. The API records and results are provided by the cloud access gateway.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Operation Logs** tab.
5. Optional. In the Start/End Time section, configure the **Start Date** and **End Date**
parameters.
6. View the operation logs.

| Parameter | Description |
|---|---|
| ID | The index of the logs of the current API operation. |
| Created At | The time when the current API operation was called. |

e to a VPC

| API Operation | The category of the API operation. For example, you can apply for or release a bare metal instance in a virtual private cloud (VPC). add indicates that a bare metal instance is applied for in the VPC. del indicates that a bare metal instance is released in the VPC. del pc indicates that a physical connection is deleted. _ del vbr indicates that a Virtual Border Router (VBR) is deleted. _ del router intf indicates that a router interface is deleted. _ _ del route entry indicates that a route table entry is deleted. _ _ |
|---|---|
| Vswitch ID | The ID of the vSwitch when the bare metal instance is applied for or released in the VPC. |
| Cloud Gateway Name | The name of the cloud access gateway that is involved in the current API operation. |
| Port | The port to which the bare metal instance belongs. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in the VPC. |
| Status | The status of the API operation. success indicates that the operation was successful. If the API operation is in progress, the value indicates the real-time status of the API operation. If the API operation is complete but the value is nots uccess, you can view the failure information in this column. Example: create vpc connection fail. |
| Details | Click Details in the Actions column to view the detailed information. For example, you can view the region ID, initiator, and status code. |

### 2.3 Network management for bare metal instances

**metal instances**

#### 2.3.1 View network information about bare metal instances in a VPC

**metal instances in a VPC**

You can view network information about bare metal instances on the Bare Metal Network Management tab. e to a VPC
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
By default, the network information of bare metal instances in the current system is displayed by page.
5. You can specify the start and end time and advanced filter conditions to query information
about the bare metal instances that meet the conditions. Advanced filter conditions include the bare metal instance name, virtual private cloud (VPC) ID, vSwitch ID, virtual border router (VBR) ID, bridge domain ID, and cloud gateway name.
6. View network information about the bare metal instances that meet the filter conditions.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. |
| SN | The serial number of the bare metal instance. |
| VPC ID | The ID of the VPC to which the bare metal instance belongs. |
| Vswitch ID | The ID of the vSwitch to which the bare metal instance belongs. |
| Cloud Gateway Name | The name of the cloud gateway to which the bare metal instance belongs. |
| Port | The port of the cloud gateway to which the bare metal instance belongs. |
| VBR ID | The VBR ID of the Express Connect circuit created on HSW by the VPC to which the bare metal instance belongs. |
| BD ID | The bridge domain of the hardware to which the bare metal instance is added. |
| Created At | The time when the network of the bare metal instance was created. |
| Bare Metal IP Address | Click Manage to assign an IP address to the bare metal instance. For more information, see Manage IP addresses for bare metal instances. |

e to a VPC

| Details | Click Connect to VPC to connect the bare metal instance to a VPC. Note This option is displayed only when the bare metal instance is not connected to a VPC. Click Close the Connection to VPC to remove the bare metal instance from the VPC. Note The option is displayed only after the bare metal instance is connected to a VPC. Click Delete Instance to remove the bare metal instance from the VPC and delete the bare metal instance. Note The Delete Instance option is displayed only for bare metal instances created on the Bare Metal Network Management page. Click Details to view the details of the bare metal instance, such as the Express Connect circuit ID, VPC router interface, and VBR router interface. |
|---|---|

#### 2.3.2 Create a bare metal instance and add the instance to a VPC

**the instance to a VPC**

You can create a bare metal instance and connect the instance to a virtual private cloud (VPC) based on O&M requirements. After the bare metal instance is connected to the VPC, you can access the bare metal instance over the VPC.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
5. Click **Create Bare Metal Instance**. In the dialog box that appears, set **Bare Metal**
**Name**, **SN**, and **Description**.
6. Find the bare metal instance that you created and click **Connect to VPC**.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. You do not need to configure this parameter. |

e to a VPC

| Bare Metal SN | The serial number of the bare metal instance. You do not need to configure this parameter. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage AccessKey pairs in Apsara Uni-manager Operations Console User Guide. |
| Region ID | The name of the region in the current environment. |
| Vswitch ID | The private vSwitch to which the bare metal instance belongs. |
| Cloud Gateway Name | The physical gateway to which the bare metal instance belongs. |
| Port | The port of the physical gateway to which the bare metal instance belongs. |
| Bare Metal Description | The description of the bare metal instance. |

7. Click **OK**.

#### 2.3.3 Close the connection between a bare metal instance and a VPC

**metal instance and a VPC**

After you close the connection between a bare metal instance and a virtual private cloud (VPC), you cannot access the bare metal instance over the VPC.

**Prerequisites**

A bare metal instance is added to a VPC.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
5. Find the bare metal instance and click **Close the Connection to VPC** or **Delete Instance**.
Click **Close the Connection to VPC** to close the connection to the VPC. Click **Delete Instance** to close the connection to the VPC and delete the bare metal instance. e to a VPC

> **Note:** The Delete Instance option is displayed only for bare metal instances created on the Bare Metal Network Management page.

#### 2.3.4 Manage IP addresses for bare metal instances

**instances**

> On the Bare Metal Network Management tab, you can manage IP addresses for bare metal instances.

**Background information**

Cloud access gateways work together with bare metal instance management. Bare metal instance management is used for bare metal installation, IP address allocation, and network configuration. Cloud access gateways are used to connect bare metal instances to virtual private clouds (VPCs). In some cases, you cannot use bare metal instance management to complete bare metal installation or network configuration but you must use cloud access gateways to connect bare metal instances to VPCs. As a result, the IP addresses of bare metal instances cannot be allocated, and you can only manually maintain the IP address allocation results. The manual operation causes IP address conflicts and poor usability. On the O&M page of cloud access gateways, you can go to the Bare Metal Network Management tab and configure the management feature for IP addresses of bare metal instances.

**Prerequisites**

A bare metal instance is added to a VPC.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
5. Find the bare metal instance whose **IP address** you want to manage and click **Manage** in
the Actions column.
6. In the **Bare Metal IP management** panel, click **Apply for Bare Metal IP Address** .
7. In the **Apply for Bare Metal IP Address** panel, configure the **Bare Metal NIC**, **IP**
**address, and IP address description** parameters and click**OK.**

> **Note:** If you do not configure the IP address parameter, the system automatically generates an IP address.

8. After you apply for an IP address for the bare metal instance, view the IP address on the
**Bare Metal IP management** tab.
You can click **Edit** to modify the IP address. You can click **Release** to release the IP address. e to a VPC

### 2.4 O&M configurations

#### 2.4.1 Apply for a bare metal instance in a VPC

**VPC**

In O&M emergency scenarios, you can use the feature to add the physical port of the access gateway associated with a bare metal instance to a virtual private cloud (VPC).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.
> The feature can only be used to connect the bare metal instance to the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to apply for a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to enable the network of the bare metal instance.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **O&M Settings** tab.
5. In the left-side drop-down list, select **Apply for Bare Metal in VPC** .
6. Configure the following parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |

e to a VPC

| Cloud Gateway Name | The name of the cloud access gateway to which the bare metal instance is connected. |
|---|---|
| Vswitch ID | The ID of the vSwitch to which you want to add the bare metal instance. You can obtain the vSwitch ID from the VPC page in the Apsara Uni-manager Management Console. |
| Port | The port of the cloud access gateway to which the bare metal instance is connected. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage AccessKey pairs in Apsara Uni-manager Operations Console User Guide. |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The names of bare metal instances must be unique. |

> **Note:** If the specified values are incorrect, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Confirm the parameter settings. If the settings are correct, click **Confirm**.
After the configurations are delivered, the **Success** message appears. You can search for the bare metal instance by instance name on the **Bare Metal Network Management** tab. If the bare metal instance is displayed, the bare metal instance is added to the VPC.

#### 2.4.2 Release a bare metal instance in a VPC

In O&M emergency scenarios, you can use the feature to disconnect the physical port of a bare metal instance from a virtual private cloud (VPC).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.
> The feature can only be used to connect the bare metal instance to the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to release a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to delete the network of the bare metal instance.

e to a VPC
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **O&M Settings** tab.
5. In the left-side drop-down list, select **Release Bare Metal in VPC** .
6. Configure the following parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| Bare Metal Name | The name of the bare metal instance that you want to release. You can search for the bare metal instance on theB are Metal Network Management tab by instance name. |

> **Note:** If the specified values are incorrect, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Confirm the parameter settings. If the settings are correct, click **Confirm**.
After the configurations are delivered, the **Success** message appears. In this case, you can search for the bare metal instance by instance name on the **Bare Metal Network**
**Management** tab. If the bare metal instance is not displayed, the instance is released.

#### 2.4.3 View the bandwidth of the Express Connect circuit

**Connect circuit**

You can view the bandwidth of the Express Connect circuit when the access gateway is connected to a VPC in the system based on your O&M requirements. e to a VPC
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **O&M Settings** tab.
5. In the left-side drop-down list, select **View Express Connect Circuit Bandwidth**.
6. Configure the search conditions and click **Query**. The information about the bandwidth of
the Express Connect circuit that meets the search conditions is displayed. The bandwidth information includes the specifications of the Express Connect circuit on the HSW of the current VPC. Then, you can check the table on the left and obtain the bandwidth (bit/s) based on the specification.

**Search conditions**

| Parameter | Description |
|---|---|
| The region ID. | The ID of the region in the current environment. |
| Router Interface ID | The ID of the virtual border router (VBR) interface. On theB are Metal Network Management tab, specify the ID of the virtual private cloud (VPC) and the name of the cloud access gateway. Then, click Details in the Actions column. |
| AK and SK | The AccessKey ID and AccessKey secret. You can obtain the values on the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage AccessKey pairs in Apsara Uni- manager Operations Console User Guide. |

**Bandwidth comparison table**

| Specification string | Bandwidth (unit: bit/s) |
|---|---|
| Large.1 | 1 GB |
| Large.2 | 2 GB |
| Large.5 | 5 GB |
| Xlarge.1 | 10 GB |
| Xlarge.2 | 20 GB |

e to a VPC

| Xlarge.4 | 40 GB |
|---|---|
| Xlarge.5 | 50 GB |
| Xlarge.8 | 80 GB |
| Xlarge.10 | 100 GB |
| Xlarge.16 | 160 GB |
| Xlarge.20 | 200 GB |

#### 2.4.4 Modify the bandwidth of the Express Connect circuit

**Connect circuit**

In O&M emergency scenarios, you can use the feature to modify the bandwidth of the Express Connect circuit.

**Warning**

The modification may affect your workloads. Unauthorized operations are prohibited. In addition, the modification must be performed under the guidance of technical support.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **O&M Settings** tab.
5. In the left-side drop-down list, select **Change Express Connect Circuit Bandwidth**.
6. Configure the following parameters and click **Next**.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| Router Interface ID | The ID of the virtual border router (VBR) interface. On theB are Metal Network Management tab, specify the ID of the virtual private cloud (VPC) and the name of the cloud access gateway. Then, click Details in the Actions column. |

e to a VPC

| Router Interface Specifications | The new specification of the bandwidth of the Express Connect circuit. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret. You can obtain the values on the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage AccessKey pairs in Apsara Uni- manager Operations Console User Guide. |

7. Check whether all the parameters are valid.
If the parameters are valid, click **Confirm**. After the configurations are delivered, check whether the configurations have been modified. For more information, see View the bandwidth of the Express Connect circuit. If the parameters are invalid, click **Back to Modify** and specify the parameters again.

## 3 CPN

### 3.1 CPN diagnosis

The Computing Platform Network (CPN) diagnosis feature checks the nodes in CPN and displays the diagnostic items, diagnostic details, and diagnostic results to help administrators better understand and manage network performance and troubleshoot issues.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Diagnosis**.
4. Click **Create a diagnosis**, select a **cluster** and a **test node**, and then click **OK**.

> **Note:** You can select multiple nodes.

5. In the dialog box that appears, confirm that the selected parameters are correct and click
**OK**. The diagnostic task starts running immediately.
6. View diagnostic results.
i. Click **Details** in the **Actions** column of the diagnostic task.

| Diagnostic Analysis results | Description |
|---|---|
| Overview view | Displays the clusters, nodes, the total number of users, the number of normal users, and the number of abnormal users. |
| Details view | You can query diagnostic details by node or diagnostic item. |

ii. On the **Diagnostic Analysis results** page, click **Details view**. iii. Select **Node** or **Diagnostic Item** from the drop-down list, enter the node IP address or diagnostic item name in the search box, and then click .

> **Note:** Click **Advanced Filter** to query nodes and diagnostic items.

iv. On the Details view tab, you can view diagnostic results, diagnostic details, and error messages.

**What to do next**

On the **CPN one-click diagnosis** page, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Filter diagnostic tasks | Basic filter i. Select Start and end time or Status from the drop-down list. ii. Select a time range or status to filter diagnostic tasks that meet the condition. Advanced filter i. Click Advanced Filter. ii. Set Start and end time and Status and click Search. |
| Retry | 1. Click Retry in the Actions column of the diagnostic task. 2. In the message that appears, click OK. |
| Delete | 1. Click Delete in the Actions column of the diagnostic task. 2. In the message that appears, click OK. |

### 3.2 CPN performance analysis

You can perform a CPN performance analysis task to test the performance of machines under stress conditions. The task analyzes the maximum load and pressure resistance of the existing software and hardware. This helps identify the pressure limits of the machines and provides sufficient data for the O&M team to improve network performance.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Performance Analysis**.
4. Click **Create a test** to create an analysis task.
The following table describes the parameter combinations for an analysis task in which Protocol Type is set to RDMA.

| Test cluster | Protoc ol type | Test type | Required parameter | Value of Traffic model | Node |
|---|---|---|---|---|---|
| Arbitrary | RDMA | Traffic test | Number of QPS tested Node Port Test duration (s) GDR | MtoN | Server Client |
|   |   |   |   | FullMesh | Server |
|   |   |   |   | Ring | Server |
|   |   | Latency Test | Node Port Test duration (s) | N/A | Server |

The following table describes the parameters you must configure to create an analysis task in which Protocol Type is set to RDMA.

| Parameter | Description |
|---|---|

| Number of QPS tested | The number of test processes. This parameter determines the test bandwidth. If the number of queue pairs (QPs) is insufficient, the related queues are blocked, which affects the efficiency and stability of data transmission. If the number of QPs is excessively large, the system overheads, complexity, and failure rate are increased. Note QP is a key concept in RDMA networks and is used to describe a queue between a pair of endpoints. |
|---|---|
| Node Port | The port number used for the test. |
| Test duration (s) | The duration of the test. Unit: seconds. |
| GDR | Specifies whether to enable GDR. If you turn on the switch, the system associates the eRDMA interface (ERI) with a GPU for traffic testing. Before you turn on the switch, check whether your machine supports the feature. If your machine does not support the feature, do not turn on the switch. |
| MtoN | Many to Many (MtoN) specifies a many-to-many relational model. This option allows you to test the one-way connectivity from Client nodes to Server nodes, including the one-way connectivity from a single Client node and a single Server node and from multiple Client nodes to multiple Server nodes. |
| FullMesh | All nodes in the network topology are connected to each other. This option allows you to test the two-way connectivity between all destination nodes. |
| Ring | Multiple nodes in the network topology form a closed loop. Data packets are sent from one node to the next node in sequence and finally returned to the original node. This option allows you to test the actual available network bandwidth. |
| Client | The sender of the test traffic. |
| Server | The receiver of the test traffic. |

The following table describes the parameters you must configure to create an analysis task in which Protocol Type is set to Communication Library.

| Test clust er | Protocol type | Test type | Communicati on library | Required parameter |
|---|---|---|---|---|

| Arbitr ary | Commun ication Library | Communi cation library test | NCCL CPN-CCL RCCL PCCL |   |   | Algorithm: the algorithm of the task. The algorithm bandwidth, bus bandwidth, and execution time of a task vary based on the algorithm. Communication primitive: the data transmission and processing methods vary based on the communication primitive. Select a value from the drop- down list. Timeout period (s): If the execution time of performance analysis test is greater than the specified timeout period plus 1 minute, the test task fails. Data type: the data type of the performance analysis test. Select a value from the drop-down list. Number of iterations: the number of times the current task is executed. Start bytes: the minimum amount of data to start the task. Number of cut-off bytes: the maximum amount of data to stop the task. Step factor: Specify an integer greater than 1. If you set the parameter to 2, the data specification increases by two times. The first row corresponds to the value of the Start bytes parameter and the last row corresponds to the value of the Number of cut-off bytes parameter. Host List: Click Add entry to add hosts. mpirun custom parameters: Specify custom parameters in the --mca ... - -mca ... format. Example: --mca |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | --mca ... - |   |   |
|   |   |   |   |   |   | -mca ... |   |   |   |
|   |   |   |   |   |   |   |   | --mca |   |
|   |   |   |   |   |   | tcp,self --mca btl tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --mca oob tcp if include _ _ _ |   |   |   |
|   |   |   |   |   |   | bond0 --bind-to none |   |   |   |

5. Click **Submit**.

**Related operations**

The following table describes the operations that you can perform on the **CPN performance**
**analysis** page.

| Operation | Procedure |
|---|---|

| Query a test task | Basic filter After you specify the start time and end time, the system automatically filters test tasks. Advanced filter i. Click Advanced Filter. ii. Configure the Start and end time, Test type, Protocol Type, and Status parameters. iii. Click Search. |
|---|---|
| View performance analysis details | 1. Find the required test task and click Details in the Actions column. 2. View the basic information, analysis results, and device information of the task. |
| Retry a test task | 1. Find the required test task and click Retry in the Actions column. 2. In the dialog box that appears, click OK. The value in the Task Status column changes to In progress. |
| Delete a test task | 1. Find the required test task and click Delete in the Actions column. 2. In the message that appears, click OK. |
| Terminate a test task | 1. Find the required test task and click Terminate in the Actions column. 2. In the dialog box that appears, click OK. The value in the Task Status column changes to Terminating. If the value in the Task Status column changes to Terminated, the task is terminated. |

### 3.3 CPN access gateways

#### 3.3.1 Manage RDMA devices

This topic describes how to manage Remote Direct Memory Access (RDMA) devices, including how to scan for and delete RDMA devices.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Select the **RDMA Device Management** tab.
5. Manage RDMA devices.
Scan for new devices Click **Scan New Devices** to add new RDMA devices to the system. Query new devices Basic filter a. Select **Device Name**, **Equipment manufacturer**, **Equipment model**, **Device**
**role**, **Device Management IP**, **Serial Number**, or **Device status** from the drop-
down list. b. In the search box, enter the device name or manufacturer, or select the status of the device, and click . Advanced filter a. Click **Advanced Filter**. b. Enter the device name, device manufacturer, device model, device role, device management IP address, and serial number, and select the device status. c. Click **Search**. Delete a new device a. Click **Delete** in the **Actions** column. b. In the message that appears, click **OK**.

#### 3.3.2 Manage RDMA device policies

This topic describes how to configure policies for Remote Direct Memory Access (RDMA) devices to manage RDMA devices in a centralized manner.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Click the **RDMA device policy management** tab.
5. Click **Create an RDMA device policy** and set the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Policy name | Enter a custom name for the policy. |
| Description | Enter the description of the policy. This parameter is optional. |
| Equipment manufacturer | Select a device vendor from the drop-down list. The system automatically displays the device vendors on the RDMA Device Management tab. |

| Device role | Select the role of the device to which the policy applies from the drop-down list. Valid values: RASW: the access vSwitch of the data exchange module in RDMA networking scenarios. RDSW: the core vSwitch of the data exchange module in RDMA networking scenarios. The core vSwitch is used to connect different access vSwitches. EHSW: the vSwitch that is used to connect to the custodian network in RDMA networking scenarios. |
|---|---|
| Equipment model | Select the model of the device to which the policy applies from the drop-down list. The system automatically displays the device models on the RDMA Device Management tab. |
| Device List | Select the device to which the policy applies from the drop-down list. The system automatically displays the devices of a specific device model on the RDMA Device Management tab. |
| Headroom | The size of the RDMA over Converged Ethernet (RoCE) queue buffer, and the maximum number of available cell resources in the headroom. Enter the size of the global buffer. |

6. Click **OK**.

**What to do next**

On the **RDMA device policy management** tab, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Query the policy for an RDMA device | 1. Select Device Name, Equipment manufacturer, Equipment model, Device role, Device Management IP, Serial Number, or Device status from the drop-down list. 2. Enter the device name, device vendor, device model, device role, device management IP address, serial number, or device status in the search box and click . |
| View the details of the policy of an RDMA device | 1. Click Details in the Actions column. 2. Click OK or Cancel. |
| Retry the policy of an RDMA device | 1. Click Retry in the Actions column. 2. In the message that appears, click OK. |

#### 3.3.3 Manage policies for the RDMA device interface

**interface**

This topic describes how to manage interface policies, such as policy configuration, query, and retry.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Access Gateway**.
4. Click the **RDMA device interface policy management** tab.
5. Click **Create an RDMA device interface policy** and configure the following parameters.

| Parameter | Description |
|---|---|
| Policy Name | Enter a custom name for the policy. |
| Description | Enter the description of the policy. This parameter is optional. |
| Device Vendor | Select a device vendor from the drop-down list. The system automatically displays the device vendors on the RDMA Device Management tab. |
| Device Role | Select the role of the device to which the policy applies from the drop-down list. Valid values: RASW: the access vSwitch of the data exchange module in Remote Direct Memory Access (RDMA) networking scenarios. RDSW: the core vSwitch of the data exchange module in RDMA networking scenarios. The core vSwitch is used to connect different access vSwitches. EHSW: the vSwitch that is used to connect to the custodian network in RDMA networking scenarios. |
| Device Model | Select the model of the device to which the policy applies from the drop-down list. The system automatically displays the device models on the RDMA Device Management tab. |
| Device List | Select the device to which the policy applies from the drop-down list. The system automatically displays the devices of a specific device model on the RDMA Device Management tab. |

| RoCE queue PFCs configuration (RDMA over Converged Ethernet) | Headroom cache threshold: the size of the RDMA over Converged Ethernet (RoCE) queue buffer, and the maximum number of available cell resources in the headroom. Back pressure frame trigger threshold: the analysis model of network traffic. The model ensures that the sum of the back pressure frame triggering thresholds for all ingresses is less than or equal to the tail-drops threshold for the egress. Offset between back pressure frame stop threshold and trigger threshold: When the number of cell resources used by packets with a 802.1p priority decreases by the value of this parameter after PFC is triggered, PFC stops sending PFC pause frames. PFCs reserved threshold: the number of cell resources reserved for packets with a 802.1p priority in the guaranteed storage capacity. PFCs: If you use PFC and congestion occurs in a specific type of traffic, the routing of other types of traffic is not affected. This ensures that different types of packets on the same link do not affect each other. Deadlock monitoring function: If a link or device failure occurs, temporary loops may occur during the route reconvergence period. In this case, PFC frames are repeatedly sent and received between devices, packets cannot be forwarded, cell resources in the interface buffer are occupied and cannot be released, and the device enters the PFC deadlock state. |
|---|---|
| RoCE queue WRED configuration | ECN function: Explicit Congestion Notification (ECN) uses the DiffServ field in the IP header to mark the congestion status along the packet transmission path. An ECN-capable terminal can determine whether congestion occurs on the transmission path based on the packet content. If congestion occurs, the terminal adjusts the method to send packets to prevent congestion from being aggravated. Lower limit of average queue length: the lower limit of the length of the queue that the packets of the forwarding device enter in the egress. The lower limit is also called ECN threshold. Upper limit of average queue length: When the device assigns packets to a queue in the outbound direction, the queue size reaches the upper threshold (ECN threshold). Discarding probability: the marking probability if ECN is used. A larger value indicates that more packets are marked between the upper and lower limits. |

| Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. When the device assigns packets to a queue in the outbound direction, if the average queue size exceeds the upper threshold, take note of the following items: If the ECN field is 00, the packets are sent out of an ECN- incapable terminal, the device drops the packets. . Click OK. If the value of the ECN field in the packet received by the device is 01 or 10, it indicates that the packet sender What to do next supports the ECN function. After the ECN field of the inbound packet is changed to 11, the packet continues to On the RDMA device interface policbye fmorawnaradgede,m anedn atl l tianbbo, uynodu p caacnke ptse arfroer nmot t dhiesc faordlleodw.ing operations: If the ECN field is 11 in a packet, the packet on the original |   | Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original |   |   |
|---|---|---|---|---|
|   |   |   | Note If the length of the queue that the packets of the forwarding device enter in the egress is smaller than the lower limit, the forwarding device directly forwards the packets from the egress without processing the packets. When the device assigns packets to a queue in the outbound direction, if the average queue size is between the lower threshold and the upper threshold, take note of the following items: If the value of the ECN field in the received packets is 00, the packets are sent out of an ECN-incapable terminal. In this case, the forwarding device determines whether to drop the packets based on the drop probability. If the value of the ECN field in the received packets is 01 or 10, the packets are sent out of an ECN-capable terminal. In this case, the forwarding devices change the value of the ECN field for some of these packets based on the drop probability and forward these packets. All incoming packets are not dropped. If the ECN field is 11 in a packet, the packet on the original |   |
|   |   |   | device has experienced congestion along the transmission path. In this case, the device does not process the packet and directly forwards the packet out of the outgoing interface. When the device assigns packets to a queue in the outbound direction, if the average queue size exceeds the upper threshold, take note of the following items: If the ECN field is 00, the packets are sent out of an ECN- incapable terminal, the device drops the packets. |   |
|   |   |   | If the value of the ECN field in the packet received by the device is 01 or 10, it indicates that the packet sender t supports the ECN function. After the ECN field of the inbound packet is changed to 11, the packet continues to interface policbye fmorawnaradgede,m anedn atl l tianbbo, uynodu p caacnke ptse arfroer nmot t dhiesc faordlleodw.ing If the ECN field is 11 in a packet, the packet on the original |   |
| Operation |   |   | device has experienced congestion along the transmission path. In this case, the device does not process the packet Procedure and directly forwards the packet out of the outgoing interface. |   |
| Query the policy for an RDMA device interface |   | 1. Configure the Policy Name, Device Vendor, Device Model, Device Role, or Device Management IP parameter. 2. Enter the policy name, device vendor, device model, device role, or device management IP address in the search box and click the icon. | 1. Configure the Policy Name, Device Vendor, Device Model, Device Role, |   |
| View the details of a policy of an RDMA device interface |   | 1. Click Details in the Actions column. 2. Click OK or Cancel. |   |   |
| Retry the policy for an RDMA device interface |   | 1. Click Retry in the Actions column. 2. In the message that appears, click OK. |   |   |

### 3.4 RDMA NIC O&M

To perform O&M on Remote Direct Memory Access (RDMA) network interface cards (NICs), you must check the performance metrics of RDMA NICs. RDMA NIC O&M allows you to identify and troubleshoot issues and ensure network stability and reliability.

**Terms**

**RDMA**: RDMA is a high-speed network technology developed to reduce the delay of server-
side data processing in network transmission. RDMA transfers data directly into the memory of a computer over the RDMA network and enables direct memory access between hosts without affecting the operating system. This increases the data transfer speed and reduces the CPU load.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > RDMA**
**Card O&M**.
4. In the upper-right corner of the page, select **Data Source** and **Cluster**. You can set Data
Source only to CPN.
5. On the **Cluster** tab, view the monitoring information about the cluster.

| Section | Description |
|---|---|
| Average QP | The average number of queue pairs (QPs) in the RDMA network. If you select PAI for Data Source, this parameter is unavailable. If the number of QPs is insufficient, the queue is blocked, which affects the efficiency and stability of data transmission. If the number of QPs is excessively large, the system overheads, complexity, and failure rate increase. Note A QP is a key concept in RDMA networks and is used to describe the queue between a pair of endpoints. |
| Abnormal Networks | The number of times that network device exceptions or traffic exceptions occur in the RDMA network. |
| Average Throughput Sent by RDMA (Mbit/s) | The average amount of data sent by all nodes in the RDMA network per second. |
| Average Throughput Received by RDMA (Mbit/s) | The average amount of data received by all nodes in the RDMA network per second. |
|   | i. Select the start time and the end time on the right side of the monitoring chart to view the monitoring data within the time range. ii. In the Throughput Dashboard section, view the RDMA TX BYTES and _ _ RDMA RX BYTES metrics. _ _ RDMA TX BYTES is the number of bytes sent in the RDMA network. _ _ RDMA RX BYTES is the number of bytes received in the RDMA _ _ network. |

|   | iii. In the Basic Data of RDMA Network section, view the following data in the specified time range: RDMA IGNORE CNP AVG: the average number of ignored _ _ _ Congestion Notification Packets (CNPs) in the RDMA network. Note CNPs are packets used for network congestion control. When network congestion occurs, CNPs are sent to notify the sender to reduce the sending rate to avoid network congestion and packet loss. RDMA TX PFC PAUSE AVG: the average number of Priority-based _ _ _ _ Flow Control (PFC) packets when data is sent in the RDMA network. |
|---|---|
| Monitoring Chart | RDMA RX PFC PAUSE AVG: the average number of PFC packets _ _ _ _ when data is received in the RDMA network. RDMA OOB AVG: the average amount of out-of-band (OOB) data _ _ processed in the RDMA network. Note OOB data is a special type of data transmitted in an RDMA network. RDMA OOS AVG: the average amount of out-of-order (OOS) data _ _ processed in the RDMA network. Note OOS data is a special type of data transmitted in an RDMA network. OOS data is generated when packet loss or latency occurs during transmission. RDMA SENT CNP AVG: the average number of CNPs sent in the _ _ _ RDMA network. RDMA MARKED ECN AVG: the average number of marked Explicit _ _ _ Congestion Notification (ECN) packets in the RDMA network. RDMA HANDLE CNP AVG: the average number of CNPs processed _ _ _ in the RDMA network. RDMA TX PFC TRANS AVG: the average number of PFC packets _ _ _ _ that are enabled in the RDMA network. RDMA QP CNT AVG: the average number of QPs in the RDMA _ _ _ network. RDMA TX BYTES AVG: the average number of bytes of data sent in _ _ _ the RDMA network. RDMA RX BYTES AVG: the average number of bytes of data _ _ _ received in the RDMA network. |

| RDMA Network Overview | View the metrics of the nodes in the RDMA network, includingN odes, Outbound Throughput, Inbound Throughput, Network QP, CNP Processed by Network, Out-of-order Data Packets, and Network Buffer Overflow. |
|---|---|

6. On the **Node** tab, view the monitoring information of each node.

| Parameter | Description |
|---|---|
| QP in RDMA Network | Displays the monitoring data of a node. For more information, see the descriptions of the cluster metrics. |
| Abnormal Networks |   |
| Throughput Sent by RDMA Network (Mbit/s) |   |
| Throughput Received by RDMA Network (Mbit/s) |   |
| Monitoring Chart |   |

### 3.5 CPN management

#### 3.5.1 CPN topology

This topic describes how to query the topology information about clusters and nodes.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Management > CPN Topology**.
4. In the upper-left corner of the page, select **Cluster** and **Nodes**.
5. Click **Query** to query the topology information.

**What to do next**

After the topology is displayed, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Zoom in or zoom out the topology | Click or in the upper-right corner of the topology to zoom in or zoom out the topology. |
| Reset the topology canvas | Click in the upper-right corner of the topology to reset the canvas. |

| Display the topology in full screen | 1. Click in the upper right corner of the topology to display the topology in full screen. 2. Click in the upper-right corner to exit the full screen. |
|---|---|

#### 3.5.2 CPN network element

> This topic describes how to view network devices and monitoring and O&M information in the cloud platform.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Management > CPN Network Element**.
4. Select a data center from the drop-down list and enter a network element name in the
**Network element name** search box.
5. Click the name of a network element or click **Details** in the **Actions** column to go to the
details page of the network element.

| Tab | Description |
|---|---|
| Port | Displays the port information of the network element device. Click the port name or click View in the Actions column to view the usage data of the port. |
| CPU Utilization | Displays the CPU usage of the network element device. |
| Memory Utilization | Displays the memory utilization of the network element device. |

| Aggregation Port Management | Displays the aggregated port information of the network element device. Click View in the Actions column to view the traffic of the port. |
|---|---|
| Alert | Displays the alert information of the network element device. |

**What to do next**

On the **CPN network element** page, you can also perform the following operations:

| Operation | Procedure |
|---|---|
| Delete a CPN network element | 1. Click Delete in the Actions column. 2. In the message that appears, click OK. |

### 3.6 CPN network monitoring

#### 3.6.1 CPN host monitoring dashboard

You can use this feature to monitor the key metrics of remote direct memory access (RDMA) networks on the server side of the intelligent computing network. The metrics include bandwidth, packet loss rate, and traffic control.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > CPN Host Monitoring**.
4. In the upper-right corner of the CPN host monitoring dashboard page, click **Variable**
**Filtering**. In the Variable Filtering dialog box, configure the **Custer** and **Host** parameters,
and click **OK**.
5. On the **CPN host monitoring dashboard** page, view information about the following
metrics: **Network Overview**, **End-side congestion packet loss**, **Network card RDMA**
**packet loss**, **Network card RDMA communication QP quantity & network card**
**status**, **Network congestion metrics**, **Network physical throughput**, and **Nic queue**
**throughput**.You can also click the
icon to the left of each metric to view details.

#### 3.6.2 CPN switch dashboard

You can use this feature to monitor the running status metrics of vSwitches. The metrics include bandwidth, packet loss, and traffic control.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > CPN Switcher**.
4. In the upper-right corner of the CPN switch dashboard page, click **Variable Filtering**. In
the Variable Filtering dialog box, configure the **idc** and **host** parameters, and click **OK**.
5. On the CPN switch dashboard page, view information about the following metrics: **Network**
**Overview**, **Ruijie exception indicator top 50**, **Top 50 abnormal indicators**, **Queue**
**metrics**, **Port metrics**, **Alarm status**, and **Logs**. You can also click the
icon to the left of each metric to view details.

#### 3.6.3 NAK packet analysis tool

You can use this tool to collect NAK packets in real time. After the packets are aggregated and analyzed, a matrix diagram is generated to help you quickly identify abnormal nodes.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > CPN Management > CPN**
**Network Monitoring > NAK Message Analysis Tool**.
4. In the upper-right corner of the NAK message Analysis Tool page, click **Variable Filtering**.
In the Variable Filtering dialog box, configure the **Network cluster**, **SOURCE device**
**Group**, and **Destination device Group** parameters, and click **OK**.
5. On the **NAK message Analysis Tool** page, view information about the following metrics:
**Network cluster-level NAK dashboard** and **Device Group-level NAK dashboard.** You
can also click the icon to the left of each metric to view details. puting servers to VPCs

## 4 Connection of intelligent computing servers to VPCs

**computing servers to VPCs**

You can use access gateways such as dedicated computing host switches (CHSWs) on the computing power platform to connect intelligent computing servers to virtual private clouds (VPCs). This helps implement the centralized management of intelligent computing servers. The system supports operations such as instance management, operation log management, bare metal network management, and O&M configurations to complete the daily O&M operations of access gateways on the computing power platform.

### 4.1 Manage access gateways

On the Instance Management tab, you can view information about access gateways on the computing power platform, such as the access gateway name, internal Border Gateway Protocol (IBGP) role, and creation time.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > Cloud Gateways**.
4. Click the **Instance Management** tab. Then, click the **Scan for New Devices** tab.
i. Find the device that you want to manage and click **Manage** in the **Actions** column. Select the devices that you want to manage and click **Batch Manage** below the device list. puting servers to VPCs ii. Configure the **IBGP Role** parameter for the device. The IBGP role specifies the role of the access gateway on the computing power platform in the environment. Valid values: Client, Deploy Client and RR on A Device, and Deploy RR on a Device.
**Client**: The access gateway on the computing power platform serves as the client of
the IBGP peer and is used only for server access.
**Deploy Client and RR on A Device**: The access gateway on the computing power
platform serves as the RR reflective route of the IBGP peer and is used for server access.
**Deploy RR on a Device**: The access gateway on the computing power platform only
serves as the RR reflective route of the IBGP peer and cannot be used for server access.

> **Important:** The following list describes the networking requirements for the IBGP role:
> Single-data center deployment: At least one set of access gateways on the computing power platform is deployed, and the IBGP roles of the access gateways are RR roles. The IBGP roles of other devices are Client.
> Multi-data center deployment: A set of access gateways on the computing power platform are deployed in at least two data centers, and the IBGP roles of the access gateways are RR roles. The IBGP roles of other devices are Client.
> You can select an RR role based on the following description:
> By default, the recommended value is Deploy Client and RR on A Device.
> If you have high requirements on network stability, we recommend that you select Deploy RR on a Device.

iii. Click **OK**.

**View access gateways on the computing power platform**

On the **Instance Management** tab, click the **Display Devices** tab to view the instance details.

| Parameter | Description |
|---|---|
| Cloud Gateway Name | The name of the access gateway on the computing power platform. |
| IBGP role | The role of the access gateway on the computing power platform in the environment. Client: indicates that the access gateway on the computing power platform serves as the client of the IBGP peer and only serves as a server. Deploy Client and RR on A Device : indicates that the access gateway on the computing power platform serves as the RR reflective route of the IBGP peer and serves as a server. Deploy RR on a Device: indicates that the access gateway on the computing power platform only serves as the RR reflective route of the IBGP peer. |

puting servers to VPCs

| Manage IP Address | The IP address of the access gateway on the computing power platform. |
|---|---|
| Management status | The initialization status of the access gateway on the computing power platform. Uninitialized Initializing Initialized |
| Created At | The creation time of the access gateway on the computing power platform. |

### 4.2 Manage operation logs

To meet O&M requirements, you can view the records and results of API operations that are managed by bare metal instances and called by the Apsara Uni-manager Operations Console. The API records and results are provided by the access gateway of the computing power platform.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Operation Logs** tab.
5. Optional. In the Start/End Time section, configure the **Start Date** and **End Date**
parameters.
6. View the operation logs.

| Parameter | Description |
|---|---|
| ID | The index of the operation log. |
| Created At | The time when the operation was performed. |
| Bare Metal Name | The name of the bare metal instance that was applied for or released in the VPC. |

puting servers to VPCs

| API Operation | The category of the API operation. For example, you can apply for or release a bare metal instance in a VPC. add: A bare metal instance is applied for in the VPC. del: A bare metal instance is released in the VPC. del pc: A physical connection is deleted. _ del vbr: A Virtual Border Router (VBR) is deleted. _ del router intf: A router interface is deleted. _ _ del route entry: A route table entry is deleted. _ _ |
|---|---|
| Vswitch ID | The ID of the vSwitch when the bare metal instance is applied for or released in the VPC. |
| Cloud Gateway Name | The name of the access gateway of the computing power platform that is involved in the current API operation. |
| Port | The port to which the bare metal instance belongs. |
| Status | The status of the API operation. success indicates that the operation was successful. If the API operation is in progress, the value indicates the real-time status of the API operation. If the API operation is complete but the value is nots uccess, you can view the failure information in this column. Example: create vpc connection fail. |
| Actions | Click Details in the Actions column to view more details. For example, you can view the region ID, initiator, and status code. |

### 4.3 Manage networks for bare metal instances

**metal instances**

On the Bare Metal Network Management tab, view information about the bare metal instance that is connected to a virtual private cloud (VPC) by using the access gateway on the computing power platform.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Cloud Gateways**.
4. Click the **Bare Metal Network Management** tab.
5. Create a bare metal instance and add it to a VPC.
i. Click **Create Bare Metal Instance**, configure the **Bare Metal Name**, **SN**, and
**Description** parameters, and then click **OK**.
puting servers to VPCs ii. Find the bare metal instance that you create, and click **Connect to VPC**.

| Parameter | Description |
|---|---|
| Bare Metal Name | The name of the bare metal instance. You do not need to configure this parameter. |
| Bare Metal SN | The serial number of the bare metal instance. You do not need to configure this parameter. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni- manager Management Console based on the organization to which the VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
| Region ID | The name of the region in the current environment. |
| Vswitch ID | The private vSwitch to which the bare metal instance belongs. |
| Cloud Gateway Name | The physical gateway to which the bare metal instance belongs. |
| Port | The port of the physical gateway to which the bare metal instance belongs. |
| Bare Metal Description | The description of the bare metal instance. |

iii. Click **OK**.

**What to do next**

After you create the bare metal instance, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Query the bare metal instance. | 1. Select the start and end time, bare metal instance name, VPC ID, vSwitch ID, Virtual Border Router (VBR) ID, BD ID, or name of the access gateway of the computing power platform. 2. Specify search conditions. The system automatically displays the instances that meet the search conditions. |
| View the details of the bare metal instance. | 1. Click Details in the Actions column to view the ID of the Express Connect circuit, VBR ID, and logical name. 2. Click OK. |

puting servers to VPCs

| Close the connection to the VPC. | 1. Click Close the Connection to VPC in the Actions column of the bare metal instance. 2. In the message that appears, click Exit. |
|---|---|
| Delete the bare metal instance. | 1. Click Delete Instance in the Actions column. 2. In the message that appears, click Exit. |

### 4.4 O&M configurations

#### 4.4.1 Apply for a bare metal instance in a VPC

**VPC**

In O&M emergency scenarios, you can use the feature to add the physical port of the access gateway associated with a bare metal instance to a virtual private cloud (VPC). The access gateway must be deployed on a computing power platform.

**Prerequisites**

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.
> The feature can only be used to connect the bare metal instance to the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to apply for a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to enable the network of the bare metal instance.

**Procedure**

i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
iii. In the left-side navigation pane, choose **Basic Network** > **Computing Access**
**Gateway**.
iv. Click the **O & M configuration** tab. puting servers to VPCs v. Select **Apply for Bare Metal in VPC** from the drop-down list in the upper-left corner of the tab. vi. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Computing power platform access gateway name | The name of the access gateway to which the bare metal instance is connected. |
| Vswitch ID | The ID of the vSwitch to which you want to add the bare metal instance. You can obtain the vSwitch ID from the VPC page in the Apsara Uni-manager Management Console. |
| Port | The port of the access gateway to which the bare metal instance is connected. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
| Bare Metal Name | The name of the bare metal instance that you want to apply for. The names of bare metal instances must be unique. |

vii. Click **Next**. viii. Check the information. If the information is correct, click **Confirm**. After the configurations are delivered, the **Success** message appears. You can search for the bare metal instance by instance name on the **Bare Metal network management** tab. If the bare metal instance is displayed, the bare metal instance is added to the VPC. puting servers to VPCs

#### 4.4.2 Release a bare metal instance in a VPC

In O&M emergency scenarios, you can use the feature to disconnect the physical port of the access gateway associated with a bare metal instance from a virtual private cloud (VPC). The access gateway must be deployed on a computing power platform.

**Context**

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.
> The feature can only be used to disconnect the bare metal instance from the access gateway port. You cannot use the feature to perform operations on the bare metal instance. To configure the network port, IP address, and routing information of the bare metal instance, contact the product team.
> In most cases, you cannot use the feature to release a bare metal instance in a VPC. You can use the bare metal controller to call an API operation to delete the network of the bare metal instance.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Release Bare Metal in VPC** from the drop-down list in the upper-left corner of the
tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |

puting servers to VPCs

| Bare Metal Name | The name of the bare metal instance that you want to release. You can search for the bare metal instance on theB are Metal network management tab by instance name. |
|---|---|

> **Note:** If the specified values are incorrect, click **Re-enter** in the lower part of the tab and configure the parameters again.

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.
After the configurations are delivered, the **Success** message appears. In this case, you can search for the bare metal instance by instance name on the **Bare Metal network**
**management** tab. If the bare metal instance is not displayed, the instance is released.

#### 4.4.3 Delete a route table entry

In O&M emergency scenarios, you can use the feature to delete route table entries that point to the subnet of a bare metal instance in a virtual private cloud (VPC) and the default route table entries of a virtual border router (VBR).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.

In most scenarios, you cannot use this feature to delete a VPC route table entry. This operation is only used for emergency scenarios. You can perform this operation to delete only one route table entry at a time. To delete multiple route table entries, you must perform this operation multiple times.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
puting servers to VPCs
5. Select **Delete Route Table Entry** from the drop-down list in the upper-left corner of the
tab.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Route Table ID | To obtain the ID of the VPC route table or VBR route table, click theB are Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Router Interface ID | To obtain the router interface of the VPC or VBR, click theB are Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Routing Destination CIDR | The destination CIDR block of the subnet of the bare metal instance. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

6. Click Next.
7. Check the parameters. If the settings are correct, click**Confirm**. After the configurations
are delivered, the **Success** message appears.

#### 4.4.4 Delete a router interface

In emergency O&M scenarios, you can use this feature to delete the router interface of a virtual private cloud (VPC) or virtual border router (VBR). puting servers to VPCs

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support personnel. Otherwise, normal business operations will be affected.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete Router Interface** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Router Interface ID | To obtain the router interface of the VPC or VBR, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click Next.
8. Check the parameters. If the settings are correct, click**Confirm**. After the configurations
are delivered, the **Success** message appears.

#### 4.4.5 Delete a VBR

In O&M emergency scenarios, you can use this feature to delete a virtual border router (VBR).

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
puting servers to VPCs
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete VBR** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| VBR ID | The ID of the VBR to be deleted. To obtain the VBR ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VBR belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

#### 4.4.6 Delete an Express Connect circuit

In O&M emergency scenarios, you can use this feature to delete an Express Connect circuit.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete Express Connect Circuit** from the drop-down list in the upper-left corner of
the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |

puting servers to VPCs

| Express Connect Circuit ID | The ID of the Express Connect circuit to be deleted. To obtain the Express Connect circuit ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VPC belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

#### 4.4.7 Delete all resources

In O&M emergency scenarios, you can use this feature to delete all resources. The resources include virtual private cloud (VPC) route table entries, virtual border router (VBR) route table entries, VPC router interfaces, VBR router interfaces, VBRs, and Express Connect circuits.

> **Warning:** This operation is only for emergency scenarios and must be performed under the guidance of technical support. Otherwise, normal business operations will be affected.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. Select **Delete ALL Resources** from the drop-down list in the upper-left corner of the tab.
6. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Computing power platform access gateway name | The name of the access gateway to which the bare metal instance is connected. |

puting servers to VPCs

| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the VPC belongs, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |
|---|---|
| VPC Router Interface ID | The ID of the VPC router interface. To obtain the VPC router interface ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC Route Table ID | The ID of the VPC route table. To obtain the VPC route table ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR Route Table ID | The VBR route table ID. To obtain the VBR route table ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC CIDR1 | A destination CIDR block that points to the subnet of the bare metal instance in the VPC. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VPC CIDR2 | Another destination CIDR block that points to the subnet of the bare metal instance in the VPC. To obtain the destination CIDR block, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR Router Interface ID | The VBR router interface ID. To obtain the VBR router interface ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| VBR ID | The ID of the VBR to be deleted. To obtain the VBR ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |
| Express Connect Circuit ID | The ID of the Express Connect circuit to be deleted. To obtain the Express Connect circuit ID, click the Bare Metal network management tab, search for the bare metal instance, and view the details of the bare metal instance. |

puting servers to VPCs

| Trunk ID | Obtain the value of the Port parameter from the Bare Metal network management tab and specify the last integer of the value as a trunk ID. For example, if the port number is 10GE1/0/40, set Trunk ID to 40. You can also leave the parameter empty. |
|---|---|

7. Click **Next**.
8. Check the information. If the information is correct, click **Confirm**.

#### 4.4.8 View the bandwidth of the Express Connect circuit

**Connect circuit**

You can view the bandwidth of the Express Connect circuit when the access gateway is connected to a virtual private cloud (VPC) based on your O&M requirements.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View Express Connect Circuit Bandwidth**.
6. Configure the filter conditions and click **Query**. The information about the bandwidth of the
Express Connect circuit that meets the search conditions is displayed. The bandwidth information includes the specifications of the Express Connect circuit on the PHSW of the current VPC. Then, you can check the table on the left and obtain the bandwidth (bit/s) based on the specification.

**Search conditions**

| Parameter | Description |
|---|---|
| Region ID | The name of the region in the current environment. |
| Router Interface ID | The ID of the virtual border router (VBR) interface. On the Bare Metal network management tab, specify the ID of the VPC and the name of the access gateway. Then, click Details in the Actions column. |
| AK and SK | The AccessKey ID and AccessKey secret. You can obtain the values on the Organizations page of the Apsara Uni-manager Management Console based on the organization to which the VBR belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

**Bandwidth comparison table**

puting servers to VPCs

| Specification string | Bandwidth (bit/s) |
|---|---|
| Large.1 | 1G |
| Large.2 | 2G |
| Large.5 | 5G |
| Xlarge.1 | 10G |
| Xlarge.2 | 20G |
| Xlarge.4 | 40G |
| Xlarge.5 | 50G |
| Xlarge.8 | 80G |
| Xlarge.10 | 100G |
| Xlarge.16 | 160G |
| Xlarge.20 | 200G |

#### 4.4.9 View trunk usage

You can view trunk usage to obtain the latest information about the usage of hardware ports at the earliest opportunity.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View Trunk Usage**.
6. Specify a trunk ID and a computing access gateway name, select a trunk state, and then
click **Search**. The trunk state can be Idle, Used, Creating, or Deleting. puting servers to VPCs

> **Note:** You can obtain the value of the **Port** parameter from the **Bare Metal network** **management** tab and specify the last integer of the value as a trunk ID. For example, if the port number is 10GE1/0/40, specify 40 as the trunk ID.

7. View results that meet the filter conditions in a list.

#### 4.4.10 View BM VPN usage

You can view information about the BM VPN that is assigned to a computing access gateway.

**Procedure**

2. In the top navigation bar, choose **Product Operation** **>** **Networking** **>** **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View BM VPN Usage**.
6. Specify a **computing access gateway name**, a **VXLAN ID**, and a **BM VPN name**, select
a trunk state, and then click **Search**. The trunk state can be Succeeded or Creating.
7. The results that meet the filter conditions are displayed in the list.

#### 4.4.11 View BD usage

You can view the BD usage to learn about the BD configuration distribution at the earliest opportunity.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **View BD Usage**.
6. Specify a computing access gateway name, a BD ID, and a vSwitch ID, select a trunk state,
and then click **Search**. The Status options contain Succeeded, Creating, and Deleting.
7. The results that meet the filter conditions are displayed in the list.

#### 4.4.12 Check the initialization configuration

You can use this feature to check whether the initialization configuration of vSwitches for computing access gateways is complete. puting servers to VPCs

> **Note:** The feature only checks the initialization status and whether the initialization configuration is successful. The feature does not perform operations on bare metal instances.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Check the Initialization Configuration**.
6. Configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| HSW Name | The name of the vSwitch that you want to check. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the initialization configuration of
the specified vSwitch.

#### 4.4.13 Check the route configuration

You can use this feature to identify abnormal operations and scan the vSwitches of computing access gateways to check whether the route configuration of bare metal instances is valid.

> **Note:** The feature only checks whether the route configuration of a bare metal instance is valid. The feature does not perform operations on the instance.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Check the Route Configuration**.
6. Configure the parameters. The following table describes the parameters.
puting servers to VPCs

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |
| Bare Metal Name | The name of the bare metal instance whose routing configuration you want to check. You can obtain the name of the bare metal instance on theB are Metal network management tab. |
| AK and SK | The AccessKey ID and AccessKey secret of the organization to which the bare metal instance belongs. You can obtain the AccessKey pair of the organization on the Organizations page of the Apsara Uni-manager Management Console. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the route configuration.

#### 4.4.14 Display information about bare metal network gateways

**network gateways**

You can use this feature to check the gateways of vSwitches in scenarios where bare metal networks are unavailable and O&M emergency is performed.

**Note**

The feature only checks the gateway information of vSwitches. The feature does not perform operations on bare metal instances.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Computing Access Gateway**.
4. Click the **O & M configuration** tab.
5. In the left-side drop-down list, select **Display the Information of Bare Metal Network**
**Gateways**.
6. Configure the parameters. The following table describe the parameters.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region in the current environment. |

puting servers to VPCs

| Vswitch ID | The vSwitch ID of the bare metal instance that you want to manage. You can obtain the vSwitch ID from the Virtual Private Cloud (VPC) console. |
|---|---|
| AK and SK | The AccessKey ID and AccessKey secret of the organization, which can be obtained from the Organizations page of the Apsara Uni-manager Management Console based on the organization to which your VPC belongs. For more information, see Manage organizations in Apsara Uni-manager Operations Console User Guide. |

7. Click **Next**.
8. Confirm the parameter settings and click **Check** to check the information about bare metal
network gateways.

## 5 Traffic visualization

Traffic visualization can monitor physical and virtual networks on the cloud platform and analyze real-time and historical network traffic. Traffic visualization can also analyze traffic by virtual private cloud (VPC), Internet access, and boundary physical network type and generate visualized charts. You can troubleshoot issues based on traffic data or traffic metrics.

### 5.1 Configure traffic visualization

Before you use traffic visualization, you must configure items such as analyzers, collection rules, and scenarios to collect, process, and analyze traffic based on your business requirements.

**Procedure**

The following procedure shows how to initialize traffic visualization.
1. For more information about how to add an analyzer and an analysis port, see Manage
analyzers.
2. For more information about how to add a collection rule, see Manage collection rules.
3. For more information about how to add an scenario, see Manage scenarios.

#### 5.1.1 Manage analysis devices

You can use analysis devices, which consist of analyzers and analysis ports, to collect and analyze traffic. Before you collect and analyze traffic, you must create an analysis device.
**An analyzer**, also known as a network performance monitoring (NPM) device, refers to a
device that performs traffic analysis. The following types of analyzers are supported: NPM physical machines and NPM central control machines.
**An analysis port**refers to the traffic collection port of an NPM device. Traffic is received
on the port for collection and analysis.

**Manage analyzers**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Analyze Device Management** tab.

| Operation | Procedure |
|---|---|

| Create an analyzer | i. In the Analyzer management section, click Add analyzer above the analyzer list. ii. In the Add analyzer panel, configure the following parameters: Zone: the zone where the analyzer resides. Analyzer name: the name of the analyzer. Analyzer role: the role that the NPM device assumes. Valid values: NPM physical machines: collects and processes traffic. NPM central control machine: displays traffic analysis results. Galaxy Security Gateway: If you select this option, traffic is preferentially redirected to Galaxy Security Gateway when you configure a VPC traffic mirroring rule. Manage IP addresses: the IP address of the NPM device. Username: the username of the NPM device. Password: the password of the NPM device. Serial Number: the serial number of the NPM device. Portal: the web page address of the NPM central control device. You can perform daily O&M and management on the NPM device at the address. The system automatically generates a value. You can view the value in the analyzer list after the analyzer is created. Analyzer description: the description of the analyzer. iii. Click OK. |
|---|---|
| Modify an analyzer | You can modify the name and description of an analyzer. You cannot modify the role and management IP address of an analyzer. i. In the Analyzer management section, find the analyzer that you want to manage and click Edit in the Operation column. ii. In the Edit analyzer panel, modify the Analyzer name and Analyzer description parameters. iii. Click OK. |
| Delete an analyzer | You can delete an analyzer that you no longer require. Important You cannot delete an analyzer that is associated with a collection rule. i. In the Analyzer management section, find the analyzer that you want to manage and click Delete in the Operation column. ii. Click OK. |

| View information about an analyzer | i. In the Analyzer management section, view information about an analyzer in the analyzer list. You can view the following information: Device ID, Analyzer name, Zone, Manage IP addresses, Authorization Status, Running status, Role, Description, Serial Number, Portal, Creation date, and Modified At. ii. Find the analyzer that you want to manage and clickD etails in the Operation column. iii. In the Details panel, view the information about the analyzer. |
|---|---|

**Manage analysis ports**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Analyze Device Management** tab.

| Operation | Procedure |
|---|---|
| Create an analysis port | i. In the Analysis Port Management section, click Add an analysis Port above the analysis port list. ii. In the Add an analysis Port panel, configure the following parameters: Analysis port name: the name of the analysis port. Analyzer name: the name of the analyzer that you want to use. Analyzer physical interface name: the physical interface of the analyzer. Analysis Port Type: the type of the analysis port. Analysis Port IP: the IP address of the analysis port. Description: the description of the analysis port. iii. Click OK. |
| Modify an analysis port | You can modify the name, IP address, and description of an analysis port. i. In the Analysis Port Management section, find the analysis port that you want to manage and click Edit in the Operation column. ii. In the Edit analysis Port panel, modify the Analysis port name, Analysis port IP, and Description parameters. iii. Click OK. |

| Delete an analysis port | You can delete an analysis port that you no longer require. Important You cannot delete an analysis port that is associated with a collection rule. i. In the Analysis Port Management section, find the analysis port that you want to manage and click Delete in the Operation column. ii. Click OK. |
|---|---|
| View information about an analysis port | i. In the Analysis Port Management section, find the analysis port that you want to manage and click Details in the Operation column. ii. In the Details panel, view information about the analysis port. |

#### 5.1.2 Manage collection rules

A collection rule defines a data source and a traffic analysis mode. Analysis devices collect and analyze traffic based on the configured collection rules.

**Prerequisites**

Before you create a collection rule, make sure that an analyzer and an analysis port are created. For more information, see Manage analysis devices.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visual Settings**.
4. Click the **Collection rule management** tab.

| Operation | Procedure |
|---|---|
| Create a collection rule | i. Click Add collection rules above the collection rule list. ii. In the Add collection rules panel, configure the parameters. For more information about the parameters, see Manage collection rules. iii. Click OK. |
| Modify a collection rule | i. Find the collection rule that you want to modify and clickE dit in the Operation column. ii. In the Edit collection rules panel, modify the Rule name and Description parameters. iii. Click OK. |

| Delete a collection rule | Important You cannot delete a collection rule that is associated with an analysis scenario. i. Find the collection rule that you want to delete and clickD elete in the Operation column. ii. Click OK. |
|---|---|

**Parameters of a collection rule**

| Parameter | Description |
|---|---|
| Zone | Select a zone for the collection rule. |
| Rule name | Enter a name for the collection rule. |
| Data source type | The type of the data source. Valid values: Elastic network card: If you select this option, traffic is collected from a specific elastic network interface (ENI). Physical switch: If you select this option, traffic is collected from a physical switch. ACK container: If you select this option, traffic is collected from a specific Container Service for Kubernetes (ACK) container. |
| Traffic analysis mode | The traffic analysis mode. This parameter is available only if you set Data source type to Elastic network card or Physical switch. The value is fixed as Traffic Image, which specifies that all traffic is copied to the analysis port. |
| AliUid | Enter the Alibaba Cloud account ID of the level-1 organization for Cloud Gateway (CGW) for authorization. You can obtain the ID in the Apsara Uni-manager Operations Console. This parameter is available only if you set Data source type toE lastic network card or ACK container. Note After authorization is complete, the system creates a virtual private cloud (VPC) image, creates a Server Load Balancer (SLB) instance, and then attaches a Node Package Manager (NPM) server or traffic gateway to the backend servers of the SLB instance for tenants in the level-1 organization. |
| ACK Cluster ID | Select the ID of an ACK cluster. This parameter is available only if you set Data source type to ACK container. |

| Select VPC | Select the VPC to which your ENI or ACK cluster belongs. This parameter is available only if you set Data source type to Elastic network card or ACK container. |
|---|---|
| Select a VSwitch | Select a vSwitch. This parameter is available only if you set Data source type to ACK container. |
| Select ENI | Select an ENI. This parameter is available only if you set Data source type to Elastic network card. |
| Display VPC Image Filtering Rules | Select Show or Hide. This parameter is available only if you set Data source type to Elastic network card. |
| Collection Policy for Inbound Rules | Select Collect Network Traffic or Network Traffic Is Not Collected. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Source CIDR Block of Inbound Traffic | Specify the source CIDR block of inbound traffic. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Source Port Range of Inbound Traffic | Specify the source port range of inbound traffic. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, you do not need to configure this parameter. Ports are not limited. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Protocol Type Used by Inbound Traffic to Be Mirrored | Valid values: ALL, ICMP, TCP, and UDP. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Destination CIDR Block of Inbound Traffic | Specify the destination CIDR block of inbound traffic. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Destination Port Range of Inbound Traffic | Specify the destination port range of inbound traffic. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Collection Policy for Outbound Rules | Select Collect Network Traffic or Network Traffic Is Not Collected. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |

| Source CIDR Block of Outbound Traffic | Specify the source CIDR block of outbound traffic. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
|---|---|
| Source Port Range of Outbound Traffic | Specify the source port range of outbound traffic. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Protocol Type Used by Outbound Traffic to Be Mirrored | Valid values: ALL, ICMP, TCP, and UDP. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Destination CIDR Block of Outbound Traffic | Specify the destination CIDR block of outbound traffic. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| Destination Port Range of Outbound Traffic | Specify the destination port range of outbound traffic. Valid values: 1 to 65535. Separate the first port and the last port with a forward slash (/). Examples: 1/200 and 80/80. If you set the protocol type to ALL or ICMP, all ports are available. In this case, you do not need to configure this parameter. This parameter is available only if you set Display VPC Image Filtering Rules to Show. |
| SLB Type | If you set the Data source type parameter to Elastic network card, you can set the SLB Type parameter to Use Existing SLB Instance or Create SLB Instance. If you set the Data source type parameter to ACK container, you can set the SLB Type parameter to Data Channel or Signaling Channel. This parameter is available only if you set the Data source type parameter to Elastic network card or ACK container. Note If you select Create SLB Instance, the system automatically creates an SLB instance. |
| SLB Instance | Select an existing SLB instance. This parameter is available only if you set the Data source type parameter to Elastic network card and set SLB Type to Use Existing SLB Instance. |
| SLB Backend Device Name | Specify an analyzer for SLB backend collection. This parameter is available only if you set the Data source type parameter to Elastic network card or ACK container. |
| Analysis Port Name of SLB Backend Device | Specify an analysis port for SLB backend collection. This parameter is available only if you set the Data source type parameter to Elastic network card or ACK container. |

| Data source host device | Select the host device of the physical switch. This parameter is available only if you set the Data source type parameter to Physical switch. |
|---|---|
| Port name of the data source host device | Select the port number of the host device. This parameter is available only if you set the Data source type parameter to Physical switch. |
| Data Source Port ID | The system automatically specifies a value based on the values that you specify for the Data source host device and Port name of the data source host device parameters. This parameter is available only if you set the Data source type parameter to Physical switch. |
| Analyzer Name | Specify an analyzer for collection. This parameter is available only if you set the Data source type parameter to Physical switch. |
| Analysis Port Name | Specify an analysis port for collection. This parameter is available only if you set the Data source type parameter to Physical switch. |
| Analysis Port VLAN ID | Enter the VLAN ID of the analysis port. This parameter is available only if you set the Data source type parameter to Physical switch. |
| Description | Enter a description for the collection rule. |

#### 5.1.3 Manage scenarios

You can associate different collection rules with different scenarios based on your business requirements.

**Prerequisites**

Before you create an analysis scenario, make sure that collection rules are added. For more information about how to add a collection rule, see Manage collection rules.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Traffic Visualization** > **Visualization Settings**.
4. Click the **Scenario Management** tab.

| Operation | Procedure |
|---|---|

| Add an analysis scenario | i. Click Create Analysis Scenario. ii. In the Add Scenario panel, enter the information. Zone: Select the zone to which the scenario belongs. Scene Name: Enter a name for the scenario. Network Type: Select a network type for the analysis scenario. VPC: virtual network. BORDER: border physical network. Collection Rule: Select the collection rule to be associated with the analysis scenario. You can select multiple collection rules. Description: The description of the custom scenario. iii. Click OK. |
|---|---|
| Modify an analysis scenario | You can modify analysis scenarios. i. Click Edit in the Actions column of the scenario. ii. In the Edit scene panel, modify the information. iii. Click OK. |
| Delete an analysis scenario | You can delete an analysis scenario that is no longer needed. i. Click Delete in the Actions column of the scenario. ii. Click OK. |

### 5.2 Visualized overview

The visualized overview displays the traffic of virtual networks and boundary physical networks in trend charts and pie charts. The visualized overview allows you to view historical and real-time traffic and perform statistical analysis based on business scenarios.

**Prerequisites**

The initial configuration of traffic visualization is completed. For more information, see Configure traffic visualization.

**Procedure**

2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Traffic Visualization** > **Overview**.
4. In the upper-right corner of the page, select the start time and end time to view the traffic
within the specified time range.

| Item | Description | What to do next |
|---|---|---|

| Network Streams | Displays the number of traffic flows in all scenarios of the virtual network or border physical network type within the specified time range. | Click a number to go to the Streams Search and Scheduling page. |
|---|---|---|
| Resource Statistics | Displays the numbers of VPCs, EIPs and ECS instances within the specified time range. | None. |
| Virtual Network | Displays the traffic trends, distribution, and rankings of different metrics of virtual networks within a specified period of time. | Click View Details to go to the Details dialog box. In the Details dialog box, set Network Type, Scenario, and Start and End Time. Then, select a metric to view the traffic trends, distribution, and rankings in different scenarios. Click Select Metrics and select the metrics that you want to view. |
| Physical Network | Displays the traffic trends, distribution, and rankings of different metrics of border physical networks within a specified period of time. |   |

### 5.3 Traffic search and scheduling

Traffic search and scheduling allows you to view more detailed traffic data and schedule traffic to balance the workload and efficiently utilize system resources.
2. In the top navigation bar, choose **Product Operation** > **Networking** > **Network**
3. In the left-side navigation pane, choose **Traffic Visualization** > **Streams Search and**
**Scheduling**.
4. Click **2-tuples** or **5-tuples**, expand **Advanced Filter**, set filter conditions, and then click
**Search**.

| Type | Advanced filter conditions |
|---|---|

| 2- tuples | You can use a 2-tuple, which consists of the source IP address and the destination IP address to identify network traffic. Start Time and End Time: Select the start time and end time. Network Type: Select VPC or BORDER. Scenario: Select the scenario that you want to query. Source VPC ID: This parameter is available only when Network Type is set toV PC. Destination VPC ID: This parameter is available only when Network Type is set to VPC. Source vSwitch ID: This parameter is available only when Network Type is set to VPC. Destination vSwitch ID: This parameter is available only when Network Type is set to VPC. Source Cloud Service: You can select this option only if Network Type is set to BORDER. Destination Cloud Service: This option is available only when Network Type is set to BORDER. Source IP Address: the source IP address. You can also search by CIDR block. Destination IP Address: the destination IP address. You can also search by CIDR block. Core Metrics: You can select multiple metrics. Sort by Indicator: Select a metric to sort by. Sorting Rule: Select Ascend or Descend. |
|---|---|
|   | You can use a 5-tuple, which consists of the source IP address, source port, destination IP address, destination port, and protocol to identify network traffic. Start Time and End Time: Select the start time and end time. Network Type: Select VPC or BORDER. Scenario: Select the scenario that you want to query. Source VPC ID: This parameter is available only when Network Type is set toV PC. Destination VPC ID: This parameter is available only when Network Type is set to VPC. |

| : | This option is available only when Network Type is set |
|---|---|

| ud gateway | Operations and Maintenance Gu de·Traffic visualizatio |
|---|---|
| 5- tuples | Source vSwitch ID: This parameter is available only when Network Type is set to VPC. Destination vSwitch ID: This parameter is available only when Network Type is set to VPC. Source Cloud Service: You can select this option only if Network Type is set to BORDER. Destination Cloud Service: This option is available only when Network Type is set to BORDER. Protocol Type: Select Only TCP traffic is displayed, Only UDP traffic is displayed, or Other Traffic Types. Source IP Address: the source IP address. You can also search by CIDR block. Destination IP Address: the destination IP address. You can also search by CIDR block. Source Port: the source port number. Destination Port: the destination port number. Core Metrics: You can select multiple metrics. Sort by Indicator: Select a metric to sort by. Sorting Rule: Select Ascend or Descend. |

| : | This option is available only when Network Type is set |
|---|---|

5. View the traffic information that meets the filter conditions.

**View traffic flows identified by 2-tuples**

a. Find the traffic flow that you want to manage and click **Details** in the **Actions** column. b. In the **Traffic Details** panel, view **Cloud Network Association Information** and
**Traffic Trend**.
c. Optional. Click **5-tuples Expansion** in the **Actions** column of a traffic flow identified by a 2-tuple.

**View traffic flows identified by 5-tuples**

You can view more detailed information about a traffic flow that is identified by the protocol type, source IP address, destination IP address, source port, and destination port. a. Find the traffic flow that you want to manage and click **Details** in the **Actions** column. b. In the **Traffic Details** panel, view **Cloud Network Association Information** and
**Traffic Trend**.
