---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Developer Guide 20251107"
product_version: "V3.18.3"
doc_version: "20251107"
pdf_pages: 528
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Developer Guide 20251107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Uni-manager%20Operations%20Console%20Developer%20Guide%2020251107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Developer Guide 20251107

## Table of Contents

- 1 Usage notes on development documentation
- 2 Release notes for Apsara Uni-manager Operations Console SDK
- 3 Unrecommended and unavailable APIs
- 4 Preparations
  - 4.1 Log on to the Apsara Uni-manager Operations Console
  - 4.2 Obtain a region ID
  - 4.3 Obtain the permissions required to call API operations
  - 4.4 Obtain an AccessKey pair
  - 4.5 Obtain the service domain name
  - 4.6 Test network connectivity
  - 4.7 Obtain the ASO Console SDKs
- 5 Call Examples for SDK for Java
  - 5.1 Getting started
  - 5.2 Use the SDK
    - 5.2.1 Install Apsara Uni-manager Operations Console SDK for Java
    - 5.2.2 Initiate an API request
- 6 Use Apsara Uni-manager Operations Console SDK for Python to call API operations
  - 6.1 Getting started
  - 6.2 Use the SDK
    - 6.2.1 Install Apsara Uni-manager Operations Console SDK for Python
    - 6.2.2 Initiate an API request
- 7 API Reference
  - 7.1 Apsara Uni-manager Operations Console
    - 7.1.1 Monitoring and alerting
      - 7.1.1.1 GetIncidentAlertList
        - 7.1.1.1.1 Supplementary details on GetIncidentAlertList
      - 7.1.1.2 GetMetricData
        - 7.1.1.2.1 Supplementary details on GetMetricData
      - 7.1.1.3 ListAlertByUpdateTime
      - 7.1.1.4 GetAlertList
      - 7.1.1.5 GetCpuMetrics
      - 7.1.1.6 GetDiskMetrics
      - 7.1.1.7 GetIoMetrics
      - 7.1.1.8 GetLoadMetrics
      - 7.1.1.9 GetMemMetrics
      - 7.1.1.10 GetTrafficMetrics
    - 7.1.2 Inventory management
      - 7.1.2.1 GetOverview
      - 7.1.2.2 GetSlbInventoryInfo
      - 7.1.2.3 GetEcsInventoryByCurrent
      - 7.1.2.4 GetEcsInventoryList
      - 7.1.2.5 GetEcsInventoryByZoneId
      - 7.1.2.6 GetVms
      - 7.1.2.7 GetEbsClusterTypeInfo
      - 7.1.2.8 GetNasInventoryInfo
      - 7.1.2.9 GetOssInventoryInfo
      - 7.1.2.10 GetOtsInnerInventoryInfo
      - 7.1.2.11 GetRdsInventoryInfo
      - 7.1.2.12 GetSlsInnerInfo
      - 7.1.2.13 GetPanguInventoryByClusterName
      - 7.1.2.14 GetInventoryStat
      - 7.1.2.15 GetIntegratedProductInventory
        - 7.1.2.15.1 Supplementary details on GetIntegratedProductInventory
    - 7.1.3 Inspections
      - 7.1.3.1 InspectionGetTaskList
      - 7.1.3.2 InspectionGetTaskExecution
      - 7.1.3.3 InspectionGetReport
    - 7.1.4 Platform products
      - 7.1.4.1 GetProductListDetail
      - 7.1.4.2 GetProductList
      - 7.1.4.3 GetProductVersion
      - 7.1.4.4 DescribeProductStatus
      - 7.1.4.5 GetClusterListByProductDetail
      - 7.1.4.6 GetClusterListByProduct
      - 7.1.4.7 GetClusters
      - 7.1.4.8 GetServiceInstanceDetail
      - 7.1.4.9 GetServerRoleList
      - 7.1.4.10 GetServerroleVersion
      - 7.1.4.11 GetServiceRole
      - 7.1.4.12 GetServerRoleMachinesDetail
    - 7.1.5 Equipment assets
      - 7.1.5.1 GetMachineByIp
      - 7.1.5.2 GetMachineByName
      - 7.1.5.3 GetMachineListDetail
      - 7.1.5.4 GetMachineList
      - 7.1.5.5 GetNetworkMachineByIp
      - 7.1.5.6 GetNetworkMachineByName
    - 7.1.6 Platform data
      - 7.1.6.1 GetCurrentUserStats
      - 7.1.6.2 ListUsers
  - 7.2 Network Operations Console
    - 7.2.1 Network element management
      - 7.2.1.1 GetSwitchInfo
      - 7.2.1.2 GetTopoInfo
      - 7.2.1.3 ListPorts
      - 7.2.1.4 ListSwTotal
      - 7.2.1.5 GetPortInfo
      - 7.2.1.6 GetXnetFlow
      - 7.2.1.7 GetHardwareUtilization
      - 7.2.1.8 GetPortTransPowerByName
    - 7.2.2 Networking services
      - 7.2.2.1 AllSlbClusters
      - 7.2.2.2 GetNodeList
      - 7.2.2.3 GetSlbLvsNodeStats
      - 7.2.2.4 GetSlbLvsClusterStats
      - 7.2.2.5 GetLbStats
      - 7.2.2.6 GetSlbProxyClusterStats
      - 7.2.2.7 GetSlbProxyNodeStats
      - 7.2.2.8 GetXgwClusterList
      - 7.2.2.9 GetXgwClusterAll
      - 7.2.2.10 GetXgwMachineList
  - 7.3 Storage Operations Console
    - 7.3.1 Apsara Distributed File System O&M
      - 7.3.1.1 GetPanguStorageCapacity
    - 7.3.2 CDS O&M
      - 7.3.2.1 DescribeOssCluster
      - 7.3.2.2 DescribeClusterCapacity
      - 7.3.2.3 DescribeHosts
      - 7.3.2.4 DescribeMetrics
      - 7.3.2.5 DescribeStorageClusters
      - 7.3.2.6 DescribeBlockClusters
  - 7.4 ApsaraDB Operations and Maintenance System
    - 7.4.1 RDS O&M
      - 7.4.1.1 DescribeHostInfoByDbType
      - 7.4.1.2 DescribeCustInsSlaveInfo
      - 7.4.1.3 DescribeResourceInventory
      - 7.4.1.4 DescribeComboInventory
  - 7.5 Apsara Uni-manager Management Console
    - 7.5.1 Platform data
      - 7.5.1.1 GetCurrentUserStats
- 8 References
  - 8.1 QPS of API operations
  - 8.2 Troubleshooting based on logs when an API operation call is abnormal

development documentation

## 1 Usage notes on development documentation

**development documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Procedure**

You can follow the procedure described in the following figure to view the desired development documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.
or Apsara Uni-manager Operation s Console SDK

## 2 Release notes for Apsara Uni-manager Operations Console SDK

**Uni-manager Operations**

**Console SDK**

This topic describes the release notes for Apsara Uni-manager Operations Console SDK of Apsara Stack V3.18.3.

**SDK version history**

| Version | Release date | Description |
|---|---|---|
| 3.18.3-0 | 2024.09 | Released the Apsara Uni-manager Operations Console SDK from which external API operations of Apsara Stack V3.18.3 can be called. |

**API release, modification, and issue records**

**Apsara Uni-manager Operations Console**

| Module | API operation | V3.18.3 or later |
|---|---|---|
| Monitoring and alerting | GetIncidentAlertList | v3.18.3 ASO RELEASE |
|   | GetMetricData | v3.18.3 ASO RELEASE |
|   | ListAlertByUpdateTime | v3.18.3 ASO RELEASE |
|   | GetAlertList | v3.18.3 ASO RELEASE |
|   | GetCpuMetrics | v3.18.3 ASO RELEASE |
|   | GetDiskMetrics | v3.18.3 ASO RELEASE |
|   | GetIoMetrics | v3.18.3 ASO RELEASE |
|   | GetLoadMetrics | v3.18.3 ASO RELEASE |
|   | GetMemMetrics | v3.18.3 ASO RELEASE |
| 0 | > Document Version: 2025110 |   |

or Apsara Uni-manager Operation s Console SDK

|   | GetTrafficMetrics | v3.18.3 ASO RELEASE |
|---|---|---|
|   | GetOverview | v3.18.3 ASO RELEASE |
|   | GetSlbInventoryInfo | v3.18.3 ASO RELEASE |
|   | GetEcsInventoryByCurrent | v3.18.3 ASO RELEASE |
|   | GetEcsInventoryList | v3.18.3 ASO RELEASE |
|   | GetEcsInventoryByZoneId | v3.18.3 ASO RELEASE |
| Inventory management |   |   |
|   | GetVms | v3.18.3 ASO RELEASE |
|   | GetEbsClusterTypeInfo | v3.18.3 ASO RELEASE |
|   | GetNasInventoryInfo | v3.18.3 ASO RELEASE |
|   | GetOssInventoryInfo | v3.18.3 ASO RELEASE |
|   | GetOtsInnerInventoryInfo | v3.18.3 ASO RELEASE |
|   | GetRdsInventoryInfo | v3.18.3 ASO RELEASE |
|   | GetSlsInnerInfo | v3.18.3 ASO RELEASE |
|   | GetPanguInventoryByClusterName | v3.18.3 ASO RELEASE |
|   | GetInventoryStat | v3.18.3 ASO RELEASE |
|   | GetIntegratedProductInventory | v3.18.3 ASO RELEASE |
| Inspections | InspectionGetReport | v3.18.3 ASO RELEASE |
|   | InspectionGetTaskExecution | v3.18.3 ASO RELEASE |
|   | InspectionGetTaskList | v3.18.3 ASO RELEASE |

or Apsara Uni-manager Operation s Console SDK

| Platform products | GetProductListDetail | v3.18.3 ASO RELEASE |
|---|---|---|
|   | GetProductList | v3.18.3 ASO RELEASE |
|   | GetProductVersion | v3.18.3 ASO RELEASE |
|   | DescribeProductStatus | v3.18.3 ASO RELEASE |
|   | GetClusterListByProductDetail | v3.18.3 ASO RELEASE |
|   | GetClusterListByProduct | v3.18.3 ASO RELEASE |
|   | GetClusters | v3.18.3 ASO RELEASE |
|   | GetServiceInstanceDetail | v3.18.3 ASO RELEASE |
|   | GetServerRoleList | v3.18.3 ASO RELEASE |
|   | GetServerroleVersion | v3.18.3 ASO RELEASE |
|   | GetServiceRole | v3.18.3 ASO RELEASE |
|   | GetServerRoleMachinesDetail | v3.18.3 ASO RELEASE |
| Equipment assets | GetMachineByIp | v3.18.3 ASO RELEASE |
|   | GetMachineByName | v3.18.3 ASO RELEASE |
|   | GetMachineListDetail | v3.18.3 ASO RELEASE |
|   | GetMachineList | v3.18.3 ASO RELEASE |
|   | GetNetworkMachineByIp | v3.18.3 ASO RELEASE |
|   | GetNetworkMachineByName | v3.18.3 ASO RELEASE |
| Platform data | GetCurrentUserStats | v3.18.3 ASO RELEASE |
| 2 | > Document Version: 2025110 |   |

| psara Uni-mana Console | Developer Guide·Release notes ger Operations or Apsara Uni-manager Operatio s Console SD |   |
|---|---|---|
|   | ListUsers | v3.18.3 ASO RELEASE |

**Network Operations Console**

| Module | API operation | V3.18.3 or later |
|---|---|---|
| Network element management | GetSwitchInfo | v3.18.3 baseServiceAll RELEASE |
|   | GetTopoInfo | v3.18.3 baseServiceAll RELEASE |
|   | ListPorts | v3.18.3 baseServiceAll RELEASE |
|   | ListSwTotal | v3.18.3 baseServiceAll RELEASE |
|   | GetPortInfo | v3.18.3 baseServiceAll RELEASE |
|   | GetXnetFlow | v3.18.3 baseServiceAll RELEASE |
|   | GetHardwareUtilization | v3.18.3 baseServiceAll RELEASE |
|   | GetPortTransPowerByName | v3.18.3 baseServiceAll RELEASE |
| Networking services | AllSlbClusters | v3.18.3 baseServiceAll RELEASE |
|   | GetNodeList | v3.18.3 baseServiceAll RELEASE |
|   | GetSlbLvsNodeStats | v3.18.3 baseServiceAll RELEASE |
|   | GetSlbLvsClusterStats | v3.18.3 baseServiceAll RELEASE |
|   | GetLbStats | v3.18.3 baseServiceAll RELEASE |
|   | GetSlbProxyClusterStats | v3.18.3 baseServiceAll RELEASE |
|   | GetSlbProxyNodeStats | v3.18.3 baseServiceAll RELEASE |
|   | GetXgwClusterList | v3.18.3 baseServiceAll RELEASE |
| > Document Ver | sion: 20251107 1 |   |

or Apsara Uni-manager Operation s Console SDK

|   | GetXgwClusterAll | v3.18.3 baseServiceAll RELEASE |
|---|---|---|
|   | GetXgwMachineList | v3.18.3 baseServiceAll RELEASE |

**Storage Operations Console**

| Module | API operation | V3.18.3 or later |
|---|---|---|
|   | GetPanguStorageCapacity | v3.18.3 ASO RELEASE |
| Apsara Distributed File System O&M |   |   |
| CDS O&M | DescribeClusterCapacity | v3.18.3 CDS-Management RELEASE |
|   | DescribeMetrics | v3.18.3 CDS-Management RELEASE |
|   | DescribeStorageClusters | v3.18.3 CDS-Management RELEASE |
|   | DescribeOssCluster | v3.18.3 CDS-Management RELEASE |
|   | DescribeBlockClusters | v3.18.3 CDS-Management RELEASE |
|   | DescribeHosts | v3.18.3 CDS-Management RELEASE |

**ApsaraDB Operations and Maintenance System**

| Module | API operation | V3.18.3 or later |
|---|---|---|
| RDS O&M | DescribeComboInventory | v3.18.3 RDS RELEASE |
|   | DescribeCustInsSlaveInfo | v3.18.3 RDS RELEASE |
|   | DescribeHostInfoByDbType | v3.18.3 RDS RELEASE |
|   | DescribeResourceInventory | v3.18.3 RDS RELEASE |

**Apsara Uni-manager Management Console**

| Module | API operation | V3.18.3 or later |
|---|---|---|

or Apsara Uni-manager Operation s Console SDK

| Platform data | GetCurrentUserStats | v3.18.3 ASCM RELEASE |
|---|---|---|

d and unavailable APIs

## 3 Unrecommended and unavailable APIs

**unavailable APIs**

Some APIs provided by the Apsara Uni-manager Operations Console of versions earlier than 3.18.1 are not supported or not recommended for use. This topic describes the APIs that are not supported or not recommended for use.

> **Note:** **Unrecommended** APIs are still described in the API reference, and alternative APIs are provided. In general, unrecommended APIs will no longer be supported in later versions of the Apsara Uni-manager Operations Console.
> Most **unsupported** APIs do not have alternative APIs and are not described in the API reference. Only a small number of unsupported APIs have alternative APIs with similar functions.

| API | Availability | Alternative API |
|---|---|---|
| GetAlertList | Not recommended | GetIncidentAlertList |
| GetCpuMetrics | Not recommended | GetMetricData |
| GetDiskMetrics | Not recommended | GetMetricData |
| GetIoMetrics | Not recommended | GetMetricData |
| GetLoadMetrics | Not recommended | GetMetricData |
| GetMemMetrics | Not recommended | GetMetricData |
| GetTrafficMetrics | Not recommended | GetMetricData |
| GetProductList | Not recommended | GetProductListDetail |
| GetClusterListByProduct | Not recommended | GetClusterListByProductDetail |
| GetMachineList | Not recommended | GetMachineListDetail |
| GetOverview | Not recommended | GetIntegratedProductInventory |
| GetSlbInventoryInfo | Not recommended | GetIntegratedProductInventory |

d and unavailable APIs

| GetEcsInventoryByCurrent | Not recommended | GetIntegratedProductInventory |
|---|---|---|
| GetEcsInventoryList | Not recommended | GetIntegratedProductInventory |
| GetEcsInventoryByZoneId | Not recommended | GetIntegratedProductInventory |
| GetEbsClusterTypeInfo | Not recommended | GetIntegratedProductInventory |
| GetNasInventoryInfo | Not recommended | GetIntegratedProductInventory |
| GetOssInventoryInfo | Not recommended | GetIntegratedProductInventory |
| GetOtsInnerInventoryInfo | Not recommended | GetIntegratedProductInventory |
| GetRdsInventoryInfo | Not recommended | GetIntegratedProductInventory |
| GetSlsInnerInfo | Not recommended | GetIntegratedProductInventory |
| GetPanguInventoryByClusterName | Not recommended | GetIntegratedProductInventory |
| GetInventoryStat | Not recommended | GetIntegratedProductInventory |
| GetHistoryAlert | No longer supported | GetIncidentAlertList |
| PushToASO | No longer supported | N/A |
| GetScriptInfo | No longer supported | N/A |
| GetScriptList | No longer supported | N/A |
| GetTaskExecuteHistory | No longer supported | N/A |
| GetTaskOutput | No longer supported | N/A |
| GetTaskInfo | No longer supported | N/A |
| GetTaskList | No longer supported | N/A |

## 4 Preparations

### 4.1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and Traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.

### 4.2 Obtain a region ID

This topic describes how to obtain a region ID.

**Background information**

You must obtain a region ID before you call API operations of the Apsara Uni-manager Operations Console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. On the left side of the top navigation bar, you can view the region ID.

### 4.3 Obtain the permissions required to call API operations

**required to call API operations**

When you use the Apsara Uni-manager Operations Console SDK to call API operations, you must provide an account for authentication. This topic describes how to determine whether your account has the required permissions to call API operations. The Apsara Uni-manager Operations Console SDK for Java supports AccessKey pair authentication. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair.

**However, not all Apsara Uni-manager Operations Console users have the**

**permissions to call API operations. Only users who are granted certain roles can**

**use their AccessKey pairs to call specific API operations. Users who are assigned**

**the OAM super administrator role can call all API operations. For more information**

**about how to create a custom role and how to view the preset roles, see the Roles**

**section of User Permissions** in **Apsara Uni-manager Operations Console User Guide** .

**Apsara Uni-manager Operations Console**

| Module | API operation | Supported role |
|---|---|---|
|   | GetIncidentAlertList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Alert events Read-only and Alert events Read/write _ _ |
|   | GetMetricData | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Alert events Read-only and Alert events Read/write _ _ |

| Monitori ng and alerting | ListAlertByUpdateTime | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Alert events Read-only and Alert events Read/write _ _ |
|---|---|---|
|   | GetAlertList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Alert events Read-only and Alert events Read/write _ _ |
|   | GetCpuMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetDiskMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetIoMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetLoadMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetMemMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |

|   | GetTrafficMetrics | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|---|---|---|
| Capacity manage ment | GetOverview | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetSlbInventoryInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetEcsInventoryByCurrent | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetEcsInventoryList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetEcsInventoryByZoneId | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetVms | Preset roles: System Administrator and System Viewer |
|   | GetEbsClusterTypeInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetNasInventoryInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |

|   | GetOssInventoryInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|---|---|---|
|   | GetOtsInnerInventoryInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetRdsInventoryInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetSlsInnerInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetPanguInventoryByClusterNam e | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetInventoryStat | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | GetIntegratedProductInventory | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
| Inspecti ons | InspectionGetTaskList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Inspections Read-only and Inspections Read/write _ _ |
|   | InspectionGetTaskExecution | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Inspections Read-only and Inspections Read/write _ _ |
| > Document | Version: 20251107 2 |   |

|   | InspectionGetReport | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Inspections Read-only and Inspections Read/write _ _ |
|---|---|---|
| Platform products | GetProductListDetail | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetProductList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetProductVersion | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | DescribeProductStatus | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetClusterListByProductDetail | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetClusterListByProduct | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |

|   | GetClusters | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|---|---|---|
|   | GetServiceInstanceDetail | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetServerRoleList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetServerroleVersion | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetServiceRole | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetServerRoleMachinesDetail | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetMachineByIp | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |

| Developer G |   |   |
|---|---|---|
| Equipme nt assets |   |   |
|   | GetMachineByName | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetMachineListDetail | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetMachineList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetNetworkMachineByIp | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
|   | GetNetworkMachineByName | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Infrastructure Management basics Read-only _ and Apsara Infrastructure Management basics Read/write _ |
| Platform data | GetCurrentUserStats | Preset roles: System Administrator and System Viewer |
|   | ListUsers | Preset roles: System Administrator and System Viewer |

**Network Operations Console**

| Module | API operation | Supported role |
|---|---|---|

| Network element manage ment | GetSwitchInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|---|---|---|
|   | GetTopoInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | ListPorts | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | ListSwTotal | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetPortInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetXnetFlow | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetHardwareUtilization | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetPortTransPowerByName | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |

| Network ing services | AllSlbClusters | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|---|---|---|
|   | GetNodeList | System administrator, product DevOps personnel, network administrator, and network monitor of the Apsara Uni-manager Operations Console |
|   | GetSlbLvsNodeStats | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetSlbLvsClusterStats | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetLbStats | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetSlbProxyClusterStats | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetSlbProxyNodeStats | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|   | GetXgwClusterList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |

|   | GetXgwClusterAll | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |
|---|---|---|
|   | GetXgwMachineList | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Network Operations Console Read-only and _ Network Operations Console Read/write _ |

**Storage Operations Console**

| Module | API operation | Supported role |
|---|---|---|
| Apsara Distribu ted File System O&M | GetPanguStorageCapacity | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Apsara Distributed File System Read-only and _ Apsara Distributed File System Read/write _ |
| CDS O&M | DescribeClusterCapacity | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |
|   | DescribeMetrics | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |
|   | DescribeStorageClusters | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |
|   | DescribeOssCluster | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |
|   | DescribeBlockClusters | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |
|   | DescribeHosts | Preset roles: System Administrator Custom roles with the CDS Read-only _ permissions |

**ApsaraDB Operations and Maintenance System**

| Module | API operation | Supported role |
|---|---|---|
| RDS O&M | DescribeComboInventory | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | DescribeCustInsSlaveInfo | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | DescribeHostInfoByDbType | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |
|   | DescribeResourceInventory | Preset roles: System Administrator and System Viewer Custom roles with one or more permissions of Capacity Read-only and Capacity Read/write _ _ |

**Apsara Uni-manager Management Console**

| Module | API operation | Supported role |
|---|---|---|
| Platfor m data | GetCurrentUserStats | Preset roles: System Administrator and System Viewer |

### 4.4 Obtain an AccessKey pair

This topic describes how to obtain an AccessKey ID and AccessKey secret.

**Background information**

You must obtain an AccessKey pair before you call API operations of the Apsara Uni-manager Operations Console. An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user and the AccessKey secret is a string that is used to encrypt the signature.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. On the right side of the top navigation bar, click the profile image.
3. Select **Personal information** from the drop-down list.
4. In the *************section, you can view the AccessKey ID and AccessKey secret of the RAM
user.

> **Note:** The AccessKey secret of **an Apsara Stack tenant account** cannot be displayed or used. Only the AccessKey secret of **a RAM user** can be displayed and used.

Only users who are assigned specific roles can use their AccessKey pairs to call specific API operations. For more information about the roles authorized to call specific API operations, see Obtain the permissions required to call API operations.
5. If no AccessKey pairs of RAM users are available, click **Create Accesskey** to obtain an
AccessKey pair.

> **Note:** You can create up to two AccessKey pairs for RAM users per account. The Create Accesskey button is automatically disabled after two AccessKey pairs are already created.

### 4.5 Obtain the service domain name

**name**

This topic describes how to obtain the service domain name of the Apsara Uni-manager Operations Console.

**Background information**

You must obtain the intranet and Internet domain names before you call API operations of the Apsara Uni-manager Operation Console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. On the right side of the top navigation bar, click the profile image.
3. Select **Personal information** from the drop-down list.
4. You can view the intranet and Internet domain names in the **Apsara Stack API calls**
section.

### 4.6 Test network connectivity

This topic describes how to test the network connectivity of machines on which you want to call API operations.

**Prerequisites**

The Central Region ID and Local Region ID are obtained. The Internet domain name and intranet domain name are obtained.

**Test methods**

**Apsara Uni-manager Operations Console**

```bash
# The domain name of the cloud service in the Central Region.
aso-mgr-pop-ops.${internetDomain}
# The domain name of the cloud service in the Local Region.
aso-mgr-pop-ops.${region}.${internetDomain}
```

**Examples**

Run the ping or curl command to test the network connectivity of a cloud service that you want to access by calling an API.

```bash
curl http://aso-mgr-pop-ops.inter.demo.aliyun.com curl http://aso-mgr-pop-ops.cn-region02-d02.inter.demo.aliyun.com
```

**Network Operations Console**

```bash
# The domain name of the cloud service in the Central Region.
full-link-pop.${intranetDomain}
# The domain name of the cloud service in the Local Region.
full-link-pop.${region}.${intranetDomain}
```

**Examples**

Run the ping or curl command to test the network connectivity of a cloud service that you want to access by calling an API.

```bash
curl http://full-link-pop.intra.demo.aliyun.com curl http://full-link-pop.cn-region02-d02.intra.demo.aliyun.com
```

**Storage Operations Console**

```bash
# The domain name of CDS in the Central Region and the Local Region. CDS has the same d
omain name in the two regions. cds-management-ops-pop.${region}.${internetDomain}
# The domain name of pgmon in the Central Region.
slalink-pgmon-pop.${intranetDomain}
# The domain name of pgmon in the Local Region.
slalink-pgmon-pop.${Local Region}.${intranetDomain}
```

**Examples**

Run the ping or curl command to test the network connectivity of a cloud service that you want to access by calling an API.

```bash
#cds
curl http://cds-management-ops-pop.cn-region01-d01.inter.demo.aliyun.com curl http://cds-management-ops-pop.cn-region02-d02.inter.demo.aliyun.com
#pgmon
curl http://slalink-pgmon-pop.intra.demo.aliyun.com curl http://slalink-pgmon-pop.cn-region02-d02.intra.demo.aliyun.com
```

**Apsara Uni-manager Management Console**

```bash
# The domain name of the cloud service in the Central Region.
ascm-ops.${internetDomain}
# The domain name of the cloud service in the Local Region.
ascm-ops.${Local Region}.${internetDomain}
```

**Examples**

Run the ping or curl command to test the network connectivity of a cloud service that you want to access by calling an API.

```bash
curl http://ascm-ops.inter.demo.aliyun.com curl http://ascm-ops.cn-region02-d02.inter.demo.aliyun.com
```

**Test results**

Determine whether the network connection is normal based on the returned result. If the returned result contains "InvalidAction.NotFound" or "Specified api is not found. please check your url and method", it indicates that the network connection of the domain name is normal. If the returned result contains "Connection refused", it indicates that the network connection of the domain name failed. You must create an anyTunnel-type tunnel and set the port number to 80 or 443. The "Could not resolve host" or "nodename nor servname provided, or not known" error message in the returned result indicates that the domain name resolution failed. You must check the DNS configuration of your machine.

### 4.7 Obtain the ASO Console SDKs

When you call API operations of a cloud service in Apsara Stack by using the POP gateway, you must use an SDK. This topic describes how to obtain the ASO Console SDKs. The ASO Console SDKs contain sample code and examples. The SDK for Java is provided. For more information, see Alibaba Cloud SDKs. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack. or SDK for Java

## 5 Call Examples for SDK for Java

**Java**

### 5.1 Getting started

This topic describes how to obtain and use Apsara Uni-manager Operations Console SDK for Java.

**Prepare the environment**

Create an Apsara Uni-manager Operations Console account with the required permissions and obtain an AccessKey pair. For more information, see Obtain an AccessKey pair. Obtain the endpoints of the Apsara Uni-manager Operations Console. For more information, see Obtain the service domain name. Install Java Development Kit (JDK) 1.8 or later.

**Install Apsara Uni-manager Operations Console SDK for Java**

If you use Apache Maven to manage Java projects, you only need to copy the content of the JAR file to the pom.xml file of the project. To use Apsara Uni-manager Operations Console SDK for Java, you must install the SDK for Java core library, Gson, and Apsara Uni-manager Operations Console SDK for Java. We recommend that you use the SDK for Java core library 4.6.0 or later, Gson 2.9.1 or later, and the latest version of Apsara Uni-manager Operations Console SDK for Java. For more information, see Release notes for Apsara Uni-manager Operations Console SDK. The following sample code provides an example on how to configure the pom.xml file:

```xml
<dependencies>
    <!--Required dependencies-->
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-uni-sdk</artifactId>
        <version >${version number of the latest SDK}</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/aliyun-java-uni-sdk-${version number of the
latest SDK}.jar</systemPath>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
    <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.9.1</version>
    </dependency>
</dependencies>
```

**Use Apsara Uni-manager Operations Console SDK for Java**

or SDK for Java To use Apsara Uni-manager Operations Console SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initiate it.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.
The following sample code provides an example on how to call the GetMachineListDetail operation:

```java
import com.aliyun.apsarabase.unisdk.SdkManager; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.asoops.model.v20220118.GetMachineListDetailRequest; import com.aliyuncs.asoops.model.v20220118.GetMachineListDetailResponse; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.profile.DefaultProfile; public class Example {
    public static void main(String[] args) {
        // Set the common parameters required to call the API operation.
        String region = "<your region>"; // Enter your region ID.
        String ak = "<your ak>"; // Enter the AccessKey ID of your account.
        String sk = "<your sk>"; // Enter the AccessKey secret of your account.
        String internetDomain = "<yourInternetDomain>";  // Enter your Internet domai
n name.
        String intranetDomain = "<yourIntranetDomain>";  // Enter your intranet domai
n name.
        boolean isCenterRegion = true;        // Specify whether your region is the Ce
ntral Region.
                                                            // If your application is d
ployed in only one region, set this parameter to true.
                                                            // If your application is d
ployed in multiple regions and the current region is the Central Region, set this par ameter to true.
                                                            // If your application is d
ployed in multiple regions and the current region is a Local Region, set this paramet er to false.
        String proxy = "<your proxy>"; // Specify the proxy information. This
parameter is optional.
        // Initialize the client.
        DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
        // ======== Proxy information (Optional) ========
        HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
        httpClientConfig.setHttpProxy(proxy);
        profile.setHttpClientConfig(httpClientConfig);
        // ====== End of proxy information ========
        IAcsClient client = new DefaultAcsClient(profile);
        SdkManager sdkManager = new SdkManager(internetDomain, intranetDomain,
region, isCenterRegion);
        System.out.println("Start GetMachineListDetail Request");
        try {
```

or SDK for Java

```java
            GetMachineListDetailRequest getMachineListDetailRequest =
sdkManager.getModel(GetMachineListDetailRequest.class);
            // Configure the timeout period. Unit: milliseconds. Default value:
10000.
            Integer readTimeoutMillis = 30000;
            getMachineListDetailRequest.setSysReadTimeout(readTimeoutMillis);
            // Add the request ID for debugging and print it to the logs to
facilitate troubleshooting.
            String uuid = UUID.randomUUID().toString();
            getMachineListDetailRequest.putHeaderParameter("test-request-id", uuid);
            System.out.println("request uuid" + uuid);
            // ======== Configure operation-specific parameters. Some parameters are
optional and others are required. ========
            getMachineListDetailRequest.setPageNum(1);
            getMachineListDetailRequest.setPageSize(10);
            // ======== End of parameter information ========
            GetMachineListDetailResponse getMachineListDetailResponse =
client.getAcsResponse(getMachineListDetailRequest);
            // For Apsara Stack V3.18.0 and later, we recommend that you use
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess()) to determine whether t he API operation is called successfully.
            // For Apsara Stack of earlier versions, you can use
"success".equalsIgnoreCase(getMachineListDetailResponse.getResult()) to determine whe ther the API operation is called successfully if the success field is not contained i n the response parameters.
            if (getMachineListDetailResponse != null &&
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess())) {
                // Specify the response if the API operation is called successfully.
System.out.println(getMachineListDetailResponse.getData().get(0).getHostName());
            } else {
                // Print the error message if an error occurs on the backend servers.
                System.out.println("GetMachineListDetail Request failed");
                if (getMachineListDetailResponse != null) {
                    System.out.println("Error response is: " +
JSONObject.toJSONString(getMachineListDetailResponse));
                } else {
                    System.out.println("Error getting GetMachineListDetail Response, r
esponse is null");
```

`}` `}`

```java
        } catch (Exception e) {
            // Print the error message if an error occurs on the client, gateways, or
backend servers.
            System.out.println("GetMachineListDetail Request failed");
            e.printStackTrace();
```

`}` `}` `}` or SDK for Java

### 5.2 Use the SDK

#### 5.2.1 Install Apsara Uni-manager Operations Console SDK for Java

**Console SDK for Java**

This topic describes how to install and use the Apsara Uni-manager Operations Console SDK for Java. Java Development Kit (JDK) 1.8 or later is installed. To use Apsara Uni-manager Operations Console SDK for Java, you must install the SDK for Java core library and the Apsara Unimanager Operations Console SDK for Java.
1. We recommend that you use the SDK for Java core library (aliyun-java-sdk-core) 4.6.0 or
later. You can install the core library by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs.
2. You can download Apsara Uni-manager Operations Console SDK for Java (aliyun-java-uni-
sdk) in the lower part of the Apsara Stack Help Center page.
3. We recommend that you use Gson 2.9.1 or later.

```xml
<dependencies>
    <!--Required dependencies-->
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-uni-sdk</artifactId>
        <version >${version number of the latest SDK}</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/aliyun-java-uni-sdk-${version number of the
latest SDK}.jar</systemPath>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
      <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.9.1</version>
    </dependency>
</dependencies>
```

#### 5.2.2 Initiate an API request

This topic describes how to use Apsara Uni-manager Operations Console SDK for Java to initiate an API request.

**Procedure**

1. Configure the pom.xml file.
For more information about how to configure the pom.xml file, see Install Apsara Unimanager Operations Console SDK for Java. or SDK for Java
2. Initialize Apsara Uni-manager Operations Console SDK for Java by specifying the region and
AccessKey pair of your account. Each account has a unique AccessKey pair that consists of an AccessKey ID and an AccessKey secret. Make sure that the account has the permissions to call the API operation. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. For more information about the required role permissions, see Permissions required to call API operations.

```
String region = "<yourRegionID>"; // Enter your region ID. String ak = "<yourAccessKeyId>"; // Enter the AccessKey ID of your account. String sk = "<yourAccessKeySecret>"; // Enter the AccessKey secret of your account. DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
```

3. (Optional) Configure connectivity settings, including the proxy.
If you want to use a proxy server, you must configure the proxy. Assume that the IP address of the proxy is 10.0.0.0 and the port number is 54321. The following sample code provides an example on how to configure the proxy:

```
HttpClientConfig httpClientConfig = HttpClientConfig.getDefault(); httpClientConfig.setHttpProxy("http://10.0.0.0:54321"); profile.setHttpClientConfig(httpClientConfig);
```

4. Initialize IAcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

5. Initialize SDKManager.
SDKManager is an Ingress gateway that receives all API requests sent from the Apsara Unimanager Operations Console. The following parameters are required to initialize SDKManager: **internetDomain**, **intranetDomain**, **region**, and **isCenterRegion**. For more information about the first three parameters, see Obtain a region ID and Obtain the service domain name. Configure **isCenterRegion** based on your environment. If you set **region** to the central region, set **isCenterRegion** to true. Otherwise, set isCenterRegion to false.

```
String internetDomain = "<yourInternetDomain>"; // Enter your Internet domain. String intranetDomain = "<yourIntranetDomain>"; // Enter your intranet domain. boolean isCenterRegion = true; // Specify whether your region is the Central R egion.
                                                 // If your application is deployed in
only one region, set this parameter to true.
                                                 // If your application is deployed in
multiple regions and the current region is the Central Region, set this parameter to true.
                                                 // If your application is deployed in
multiple regions and the current region is a Local Region, set this parameter to fals
```

`e.`

```
SdkManager sdkManager = new SdkManager(internetDomain, intranetDomain, region, isCent erRegion);
```

6. Create an API request by using SDKManager.
The request name must be in the ${apiName}Request format. Replace ${apiName} with the name of the API operation. Example: GetMachineListDetailRequest. or SDK for Java If Apsara Uni-manager Operations Console SDK for Java includes API operations that belong to multiple services, the API requests may have identical class names. We recommend that you differentiate the identical requests based on package names.

```
GetMachineListDetailRequest getMachineListDetailRequest = sdkManager.getModel(GetMachineListDetailRequest.class); // ======== Configure operation-specific parameters. Some parameters are optional and others are required. ======== getMachineListDetailRequest.setPageNum(1); getMachineListDetailRequest.setPageSize(10); // ======== End of parameter information ========
```

7. Initiate a request and handle exceptions.
If a request fails, Apsara Uni-manager Operations Console SDK for Java or backend servers will return an error message. All the errors need to be handled manually. Apsara Uni-manager Operations Console SDK for Java may return the following types of error messages: ServerException and ClientException. ServerException indicates a server error, and ClientException indicates a client error. For example, if the following error message is returned, it indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified ac cess key is not found.
```

To handle the errors that are returned by the backend servers, you must parse the responses. For Apsara Uni-manager Operations Console 3.18.0 or later, the exception information is specified by the success, errorCode, and errorMessage parameters in the response. success is a Boolean expression that indicates whether the request succeeded or failed. errorCode and errorMessage are both strings that indicate the error code and error message, respectively. The following sample code shows how to handle exceptions returned by the GetMachineListDetail operation: or SDK for Java

```java
try {
    GetMachineListDetailRequest getMachineListDetailRequest =
sdkManager.getModel(GetMachineListDetailRequest.class);
    // Configure the timeout period. Unit: milliseconds. Default value: 10000.
    Integer readTimeoutMillis = 30000;
    getMachineListDetailRequest.setSysReadTimeout(readTimeoutMillis);
    // Add the request ID for debugging and print it to the logs to facilitate trou
bleshooting.
    String uuid = UUID.randomUUID().toString();
    getMachineListDetailRequest.putHeaderParameter("test-request-id", uuid);
    System.out.println("request uuid" + uuid);
    // ======== Configure operation-specific parameters. Some parameters are option
al and others are required. ========
    getMachineListDetailRequest.setPageNum(1);
    getMachineListDetailRequest.setPageSize(10);
    // ======== End of parameter information ========
    GetMachineListDetailResponse getMachineListDetailResponse =
client.getAcsResponse(getMachineListDetailRequest);
    // For Apsara Stack V3.18.0 and later, we recommend that you use
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess()) to determine whether the API operation is called successfully.
    // For Apsara Stack of earlier versions, you can use
"success".equalsIgnoreCase(getMachineListDetailResponse.getResult()) to determine w hether the API operation is called successfully if the success field is not contain ed in the response parameters.
    if (getMachineListDetailResponse != null &&
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess())) {
        // Specify the response if the API operation is called successfully.
System.out.println(getMachineListDetailResponse.getData().get(0).getHostName());
    } else {
        // Print the error message if an error occurs on the backend servers.
        System.out.println("GetMachineListDetail Request failed");
        if (getMachineListDetailResponse != null) {
            System.out.println("Error response is: " +
JSONObject.toJSONString(getMachineListDetailResponse));
        } else {
            System.out.println("Error getting GetMachineListDetail Response,
response is null");
```

`}` `}`

```java
} catch (Exception e) {
    // Print the error message if an error occurs on the client, gateways, or backe
nd servers.
    System.out.println("GetMachineListDetail Request failed");
    e.printStackTrace();
```

`}`

```java
import com.aliyun.apsarabase.unisdk.SdkManager; import com.aliyuncs.DefaultAcsClient;
```

or SDK for Java

```java
potco.a yucs.eautcsC et; import com.aliyuncs.IAcsClient; import com.aliyuncs.asoops.model.v20220118.GetMachineListDetailRequest; import com.aliyuncs.asoops.model.v20220118.GetMachineListDetailResponse; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.profile.DefaultProfile; public class Example {
    public static void main(String[] args) {
        // Set the common parameters required to call the API operation.
        String region = "<your region>"; // Enter your region ID.
        String ak = "<your ak>"; // Enter the AccessKey ID of your account.
        String sk = "<your sk>"; // Enter the AccessKey secret of your account.
        String internetDomain = "<yourInternetDomain>";  // Enter your Internet domain
name.
        String intranetDomain = "<yourIntranetDomain>";  // Enter your intranet domain
name.
        boolean isCenterRegion = true;        // Specify whether your region is the Cent
ral Region.
                                                            // If your application is dep
oyed in only one region, set this parameter to true.
                                                            // If your application is dep
oyed in multiple regions and the current region is the Central Region, set this paramet er to true.
                                                            // If your application is dep
oyed in multiple regions and the current region is a Local Region, set this parameter t o false.
        String proxy = "<your proxy>"; // Specify the proxy information. This parameter
is optional.
        // Initialize the client.
        DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
        // ======== Proxy information (Optional) ========
        HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
        httpClientConfig.setHttpProxy(proxy);
        profile.setHttpClientConfig(httpClientConfig);
        // ====== End of proxy information ========
        IAcsClient client = new DefaultAcsClient(profile);
        SdkManager sdkManager = new SdkManager(internetDomain, intranetDomain, region,
isCenterRegion);
        System.out.println("Start GetMachineListDetail Request");
        try {
            GetMachineListDetailRequest getMachineListDetailRequest =
sdkManager.getModel(GetMachineListDetailRequest.class);
            // Configure the timeout period. Unit: milliseconds. Default value: 10000.
            Integer readTimeoutMillis = 30000;
            getMachineListDetailRequest.setSysReadTimeout(readTimeoutMillis);
            // Add the request ID for debugging and print it to the logs to facilitate
troubleshooting.
            String uuid = UUID.randomUUID().toString();
            getMachineListDetailRequest.putHeaderParameter("test-request-id", uuid);
```

or SDK for Java

```java
            System.out.println("request uuid" + uuid);
            // ======== Configure operation-specific parameters. Some parameters are
optional and others are required. ========
            getMachineListDetailRequest.setPageNum(1);
            getMachineListDetailRequest.setPageSize(10);
            // ======== End of parameter information ========
            GetMachineListDetailResponse getMachineListDetailResponse =
client.getAcsResponse(getMachineListDetailRequest);
            // For Apsara Stack V3.18.0 and later, we recommend that you use
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess()) to determine whether the API operation is called successfully.
            // For Apsara Stack of earlier versions, you can use
"success".equalsIgnoreCase(getMachineListDetailResponse.getResult()) to determine wheth er the API operation is called successfully if the success field is not contained in th e response parameters.
            if (getMachineListDetailResponse != null &&
Boolean.TRUE.equals(getMachineListDetailResponse.getSuccess())) {
                // Specify the response if the API operation is called successfully.
System.out.println(getMachineListDetailResponse.getData().get(0).getHostName());
            } else {
                // Print the error message if an error occurs on the backend servers.
                System.out.println("GetMachineListDetail Request failed");
                if (getMachineListDetailResponse != null) {
                    System.out.println("Error response is: " +
JSONObject.toJSONString(getMachineListDetailResponse));
                } else {
                    System.out.println("Error getting GetMachineListDetail Response, res
ponse is null");
```

`}` `}`

```java
        } catch (Exception e) {
            // Print the error message if an error occurs on the client, gateways, or ba
ckend servers.
            System.out.println("GetMachineListDetail Request failed");
            e.printStackTrace();
```

`}` `}` `}` manager Operations Console SD K for Python to call API operation s

## 6 Use Apsara Uni-manager Operations Console SDK for Python to call API operations

**Operations Console SDK for**

**Python to call API operations**

### 6.1 Getting started

This topic describes how to obtain and use Apsara Uni-manager Operations Console SDK for Python.

**Prepare the environment**

Create an Apsara Uni-manager Operations Console account with the required permissions and obtain an AccessKey pair. For more information, see Obtain an AccessKey pair. Obtain the endpoints of the Apsara Uni-manager Operations Console. For more information, see Obtain the service domain name.

**Install Apsara Uni-manager Operations Console SDK for Python**

To call the API operations of Apsara Uni-manager, you must install the SDK for Python core library and Apsara Uni-manager Operations Console SDK for Python. We recommend that you use the SDK for Python core library 2.11.5 or later, and use the latest version of Apsara Unimanager Operations Console SDK for Python. For more information about the latest version, see Release notes for Apsara Uni-manager Operations Console SDK. For more information about how to install the SDK for Python, see Install Apsara Uni-manager Operations Console SDK for Python.

**Use Apsara Uni-manager Operations Console SDK for Python**

To use Apsara Uni-manager Operations Console SDK for Python, perform the following steps:
1. Create and initialize an AcsClient instance.
2. Create an API request and set the required parameters.
3. Initiate the request and handle the response or exceptions.
The following sample code provides an example on how to call the DescribeProductStatusRequest operation:

```python
from aliyuncs.sdk_manager import UniSdk from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException from aliyunsdkcore.client import AcsClient from aliyuncs.aliyunsdkasoops.request.v20220118.DescribeProductStatusRequest import D escribeProductStatusRequest def testUniSDK():
  interDomain="<yourInternetDomain>"
  intraDomain="<yourIntranetDomain>"
  region="<yourRegion>"
  isCenterRegion=True # Set this parameter based on the value of region.
  ak = "<yourAccessKeyId>"
  sk = "<yourAccessKeySecret>"
  client = AcsClient(ak=ak, secret=sk, region_id=region)
  sdkManager = UniSdk(interDomain=interDomain, intraDomain=intraDomain,
region=region, isCenterRegion=isCenterRegion)
```

manager Operations Console SD K for Python to call API operation s

```python
  print("Start GetMachineListDetail Request")
  try:
        describeProductStatusInstance =
sdkManager.get_class(DescribeProductStatusRequest)
        # Configure the timeout period. Unit: milliseconds. Default value: 10000.
        readTimeoutMillis = 30000
        describeProductStatusInstance.set_read_timeout(readTimeoutMillis)
        # Add the request ID for debugging and print it to the logs to facilitate tro
ubleshooting.
        uuidstr = str(uuid.uuid4())
        describeProductStatusInstance.add_header("test-request-id", uuidstr)
        print(uuidstr)
        # ======== Configure operation-specific parameters. Some parameters are optio
nal and others are required. ========
        describeProductStatusInstance.set_project("aso")
        describeProductStatusResponse =
client.do_action_with_exception(describeProductStatusInstance)
        strDescribeProductStatusResponse = str(describeProductStatusResponse,
encoding="utf-8")
        describeProductStatusJsonResponse =
json.loads(strDescribeProductStatusResponse)
        # For earlier versions, you need to use
describeProductStatusJsonResponse["message"] == "success" to determine whether the AP I operation is called successfully if the success field is not contained in the respo nse parameters.
        if (
            describeProductStatusJsonResponse != None
            and describeProductStatusJsonResponse["success"]
```

`)`

```python
            print(strDescribeProductStatusResponse)
        else:
            // Print the error message if an error occurs on the backend server.
            print("GetMachineListDetail request failed:")
            if describeProductStatusJsonResponse is not None:
                print(f"Error response is: {strDescribeProductStatusResponse}")
            else:
                print("An error occurred while obtaining the response of GetMachineLis
tDetail. The response is None.")
  except ServerException as e:
    print(str(e, encoding="utf-8")) # Specify the operation that you want to perform
when an error occurs. Example: print error messages.
  except ClientException as e:
    print(str(e, encoding="utf-8")) # Specify the operation that you want to perform
when an error occurs. Example: print error messages. if __name__ == "__main__":
  testUniSDK()
```

### 6.2 Use the SDK

manager Operations Console SD K for Python to call API operation s

#### 6.2.1 Install Apsara Uni-manager Operations Console SDK for Python

**Console SDK for Python**

This topic describes how to install and use Apsara Uni-manager Operations Console SDK for Python. Before you Install Apsara Uni-manager Operations Console SDK for Python, you must install Python 2.7 or later. To call the API operations of Apsara Uni-manager, you must install the SDK for Python core library and Apsara Uni-manager Operations Console SDK for Python.
1. We recommend that you use the SDK for Python core library (aliyun-python-sdk-core)
2.11.5 or later. You can install the core library by downloading the SDK on the Alibaba Cloud SDKs page or by running the following command:

```
pip install aliyun-python-sdk-core
```

2. To install aliyun-python-uni-sdk, download the **Apsara Stack Enterprise Edition v3.18.1**
**ASO SDK package** in the lower part of the Apsara Stack Help Center page. If you installed
pip, you can run the following command to install aliyun-python-uni-sdk.

```
pip install aliyun-python-uni-sdk-3.18.1.0.tar.gz
```

If you did not install pip, you can decompress the tar package and run a setup.py task​ by running the following commands:

```
tar -zxvf aliyun-python-uni-sdk-3.18.1.0.tar.gz cd aliyun-python-uni-sdk-3.18.1.0 python setup.py install
```

#### 6.2.2 Initiate an API request

This topic describes how to use Apsara Uni-manager Operations Console SDK for Python to initiate an API request.

**Procedure**

1. Install the SDK for Python on your computer. For more information, see Install Apsara Uni-
manager Operations Console SDK for Python.
2. Initialize Apsara Uni-manager Operations Console SDK for Python by specifying the region
and AccessKey pair of your account. Each account has a unique AccessKey pair that consists of an AccessKey ID and an AccessKey secret. Make sure that the account has the permissions to call the API operation. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. For more information about the required role permissions, see Permissions required to call API operations.

```
region = "<yourRegion>" # Replace the value with the region ID. ak = "<yourAccessKeyId>" # Enter the AccessKey ID of your account. sk = "<yourAccessKeySecret>" # Enter the AccessKey secret of your account.
```

3. (Optional) Configure connectivity settings, including the proxy.
If you want to use a proxy server, you must configure the proxy. Assume that the IP address of the proxy is 10.0.0.0 and the port number is 54321. The following sample code provides an example on how to configure the proxy: manager Operations Console SD K for Python to call API operation s

```
proxy = "http://10.0.0.0:54321" client = AcsClient(ak=ak, secret=sk, region_id=region, proxy={"http": proxy})
```

4. Create and initialize an AcsClient instance.
If you already completed Step 3 and used the proxy information to initialize the client, skip this step.

```
client = AcsClient(ak=ak, secret=sk, region_id=region)
```

5. Initialize SDKManager.
SDKManager is an Ingress gateway that receives all API requests sent from the Apsara Unimanager Operations Console. The following parameters are required to initialize the SDKManager: **internetDomain**, **intranetDomain**, **region**, and **isCenterRegion**. For more information about the first three parameters, see Obtain a region ID and Obtain the service domain name. Configure **isCenterRegion** based on your environment. If you set **region** to the central region, set isCenterRegion to **true**. Otherwise, set isCenterRegion to false.

```bash
interDomain="<yourInternetDomain>" # Enter your Internet domain. intraDomain="<yourIntranetDomain>" # Enter your intranet domain. isCenterRegion=True # Specify whether your region is the Central Region.
                  # If your application is deployed in only one region, set this param
eter to true.
                                    # If your application is deployed in multiple
regions and the current region is the Central Region, set this parameter to true.
                                    # If your application is deployed in multiple
regions and the current region is a Local Region, set this parameter to false. sdk_manager = UniSdk(interDomain=interDomain, intraDomain=intraDomain, region=region, isCenterRegion=isCenterRegion)
```

6. Create an API request by using SDKManager.
The request name must be in the ${apiName}Request format. Replace ${apiName} with the name of the API operation. Example: DescribeProductStatusRequest.

```
from aliyuncs.aliyunsdkasoops.request.v20220118.DescribeProductStatusRequest import D escribeProductStatusRequest describeProductStatusRequest = sdkmanager.get_class(DescribeProductStatusRequest)
```

If Apsara Uni-manager Operations Console SDK for Python includes API operations that belong to multiple services, the API requests may have identical names. We recommend that you differentiate the identical request names by adding as to your code to generate new request names. Example of a new name: GetCurrentUserStatsAscmRequest.

```
from aliyuncs.aliyunsdkascmops.request.v20220531.GetCurrentUserStatsRequest import Ge tCurrentUserStatsRequest as GetCurrentUserStatsAscmRequest getCurrentUserStatsAscmRequest = sdkmanager.get_class(GetCurrentUserStatsAscmRequest)
```

7. Initiate a request and handle exceptions.
If a request fails, Apsara Uni-manager Operations Console SDK for Python or backend servers will return an error message. All the errors need to be handled manually. Apsara Uni-manager Operations Console SDK for Python may return the following types of error messages: ServerException and ClientException. ServerException indicates a server error, and ClientException indicates a client error. manager Operations Console SD K for Python to call API operation s For example, if the following error message is returned, it indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
aliyunsdkcore.acs_exception.exceptions.ServerException: HTTP Status: 404 Error:Inva lidAccessKeyId.NotFound Specified access key is not found.
```

To handle the errors that are returned by the backend servers, you must parse the responses. For Apsara Uni-manager Operations Console 3.18.0 or later, the exception information is specified by the success, errorCode, and errorMessage parameters in the response. success is a Boolean expression that indicates whether the request succeeded or failed. errorCode and errorMessage are both strings that indicate the error code and error message, respectively.

```python
# Initiate a request and view the result.
describeProductStatusResponse = client.do_action_with_exception(describeProductStatusInstance)
# Configure the required parameters.
describeProductStatusRequest.set_project("ASO") print(str(describeProductStatusResponse, encoding="utf-8")) from aliyuncs.sdk_manager import UniSdk from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException from aliyunsdkcore.client import AcsClient from aliyuncs.aliyunsdkasoops.request.v20220118.DescribeProductStatusRequest import Des cribeProductStatusRequest def testUniSDK():
  interDomain="<yourInternetDomain>"
  intraDomain="<yourIntranetDomain>"
  region="<yourRegion>"
  isCenterRegion=True # Set this parameter based on the value of region.
  ak = "<yourAccessKeyId>"
  sk = "<yourAccessKeySecret>"
  client = AcsClient(ak=ak, secret=sk, region_id=region)
  sdkManager = UniSdk(interDomain=interDomain, intraDomain=intraDomain, region=region,
isCenterRegion=isCenterRegion)
  print("Start GetMachineListDetail Request")
  try:
        describeProductStatusInstance =
sdkManager.get_class(DescribeProductStatusRequest)
        # Configure the timeout period. Unit: milliseconds. Default value: 10000.
        readTimeoutMillis = 30000
        describeProductStatusInstance.set_read_timeout(readTimeoutMillis)
        # Add the request ID for debugging and print it to the logs to facilitate troub
leshooting.
        uuidstr = str(uuid.uuid4())
        describeProductStatusInstance.add_header("test-request-id", uuidstr)
        print(uuidstr)
#========Configureoperation-specificparameters
Someparametersare
```

manager Operations Console SD K for Python to call API operation s

```bash
        # ======== Configure operation-specific parameters. Some parameters are
optional and others are required. ========
        describeProductStatusInstance.set_project("aso")
        describeProductStatusResponse =
client.do_action_with_exception(describeProductStatusInstance)
        strDescribeProductStatusResponse = str(describeProductStatusResponse,
encoding="utf-8")
        describeProductStatusJsonResponse =
json.loads(strDescribeProductStatusResponse)
        # For earlier versions, you need to use
describeProductStatusJsonResponse["message"] == "success" to determine whether the API operation is called successfully if the success field is not contained in the response parameters.
        if (
            describeProductStatusJsonResponse != None
            and describeProductStatusJsonResponse["success"]
```

`)`

```python
            print(strDescribeProductStatusResponse)
        else:
            // Print the error message if an error occurs on the backend server.
            print("GetMachineListDetail request failed:")
            if describeProductStatusJsonResponse is not None:
                print(f"Error response is: {strDescribeProductStatusResponse}")
            else:
                print("An error occurred while obtaining the response of GetMachineListD
etail. The response is None.")
  except ServerException as e:
    print(str(e, encoding="utf-8")) # Specify the operation that you want to perform wh
en an error occurs. Example: print error messages.
  except ClientException as e:
    print(str(e, encoding="utf-8")) # Specify the operation that you want to perform wh
en an error occurs. Example: print error messages. if __name__ == "__main__":
  testUniSDK()
```

## 7 API Reference

### 7.1 Apsara Uni-manager Operations Console

**Operations Console**

#### 7.1.1 Monitoring and alerting

##### 7.1.1.1 GetIncidentAlertList

Queries a list of alerts.
1. The result of this operation is similar to that of the Alerts page on the Apsara Uni-manager
Operations Console. You can refer to the Alerts page for the function of this operation.
2. For more information about how to understand the alert ID and alert information, see Alarm
Reference in the Maintenance ASO section on the Help and Open Platform page. You can go to this page by clicking the Help documentation icon in the upper-right corner of the Apsara Uni-manager Operations Console.
3. Call this operation instead of the `GetAlertList` operation to query alerts.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/incident/api/alert/list HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| page | Integ er | Quer y | No | 1 | The page number. |
| pageSize | Integ er | Quer y | No | 20 | The number of entries per page. |
| keywords | Strin g | Quer y | No | ecs | The alert keyword that is used for fuzzy search. |
| code | Strin g | Quer y | No | CPUHigh | The alert code. |
| statusList | JSON ARR AY | Quer y | No | 0 | The alert status. Valid values: 0: not handled. 1: processing. 2: closed. |
| level | Integ er | Quer y | No | 1 | The severity level of the alert. Valid values: 1: P1. 2: P2. 3: P3. 4: P4. |
| startTime Min | Integ er | Quer y | No | 1920001300 | The beginning of the time range to query alerts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: seconds. |
| startTime Max | Integ er | Quer y | No | 1920001300 | The end of the time range to query alerts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: seconds. |

| source | Strin g | Quer y | No | tianjimon | The data source. |
|---|---|---|---|---|---|
| product | Strin g | Quer y | No | aso | The product that triggered the alert. |
| orderBySta rtTimeAsc | Bool ean | Quer y | No | true | Specifies whether to sort the alerts in ascending order based on the time when they are triggered. |

The following items describe how to obtain specific alerts about physical servers:

| : Set code to hardware monitor new . In th _ _ lertName is hardware monitor new alarm _ _ _ SasRaidMonitor . |   | hardware monitor new _ _ |   | . In th |
|---|---|---|---|---|
|   | hardware monitor new alarm _ _ _ |   |   |   |
| SasRaidMonitor |   |   |   |   |
|   |   |   | . |   |

```
 DiskBackplaneMonitor  or  SasRaidMonitor .
```

| to | hardware monitor new _ _ |
|---|---|

whose alertName is `hardware_monitor_new_alarm` and monitor is `FanMonitor` .

| hardware monitor new . _ _ | In the |
|---|---|
| hardware monitor new alarm _ _ _ |   |

| to | hardware monitor new _ _ |
|---|---|

whose alertName is `hardware_monitor_new_alarm` and monitor is `CPUMonitor` .

| o | hardware monitor new _ _ | . In t |
|---|---|---|
| hardware monitor new alarm _ _ _ |   |   |

| o hardware monitor new . In t _ _ hardware monitor new alarm _ _ _ | hardware monitor new _ _ | . In t |
|---|---|---|

```
 BoardMonitor .
```

| to | hardware monitor new . _ _ |
|---|---|

whose alertName is `hardware_monitor_new_alarm` and monitor is `PcieFlashMonitor` .

| to | ntp cluster host _ _ | . In th |
|---|---|---|
| host ntp sync state alarm _ _ _ _ |   |   |

| to | check pangu disk error _ _ _ |   |
|---|---|---|
| check pangu disk error _ _ _ |   |   |
|   |   | . |

Apsara Distributed File System damaged disk: Set code to `check_pangu_disk_error` . In the returned result, find the data entry whose alertName is `check_pangu_disk_error` .

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | "" | The error message. |

| psara Uni-manag Console | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|
| data | Map | {"pageSize":"1","to tal":"42589","page ":"1","totalPage":"4 2589","objectList": [{"shield":"false","c luster":"","checkInt erval":"0","metricN ame":"base base _ _ meta project chec _ _ ker","code":"base _ base meta project _ _ checker","source" _ :"bcc","type":"defa ult","duration":"18 3463223","alarmC ount":"3052","host name":"docker010 212012134","start Time":"2022-11- 12T00:01:16.000+ 0000","id":"31360", "product":"","handl eUserName":"","lev el":"2","updateTim e":"2022-11- 14T02:58:38.000+ 0000","alarmName ":"base base meta _ _ project checker"," _ _ message":"base - base base meta p _ _ _ roject checker - _ warning - The Job: [mc export ] state _ is Failed!","lastAlarm Time":"2022-11- 14T02:58:38.000+ 0000","serverRole" :"","alarmRule":""," createTime":"2022 -11- 12T00:01:16.000+ 0000","service":""," endTime":"1970- 01- 01T00:00:00.000+ 0000","region":"cn- XX-XX- XX","currentValue" :"","dimensions": [{"standard":"true" ,"value":"docker01 23456789","key":" hostname"}, {"standard":"false" ,"value":"tcheck","k ey":"source"}],"sta tus":"0"}]} | The response. |

| cost | Long | 30 | The time spent on querying alerts. Unit: milliseconds. |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| success | Boolean | true | Indicates whether the call was successful. Valid values: true. false. |
| eagleEyeTrace Id | String | 0acd10a61654599 3190765214d002a | The EagleEye ID. |
| msg | String | "" | The error message. |
| errorStack | String | "" | The stack where the error occurred. |
| version | String | v1 | The version of the API on Apsara Uni- manager Operations Console. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
|---|---|---|---|
| message | String | "" | The error message. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso- emergency.Inciden t# | The service role. |
| path | String | /aso/incident/api/al ert/list | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

The data parameter includes the following fields: totalPage: the total number of returned pages. pageSize: the number of entries per page. total: the total number of returned alerts. page: the page number. objectList: the returned alerts. id: the alert ID. startTime: the time when the alert was triggered. endTime: the time when the alert was closed. duration: the duration of the alert. message: the alert message. code: the alert code. metricName: the metric name. metricProject: the monitoring project. alarmName: the alert name. alarmRule: the rule that describes how the alert is triggered. currentValue: the current value of the metric. source: the alert source. type: the type of the alert. dimensions: the metric dimensions. key: the dimension key. value: the dimension value. standard: indicates whether the dimension is a standard dimension. level: the severity level of the alert. The values 1 to 4 indicate P1 to P4. status: the status of the alert. Valid values: 0, 1, and 2. 0 indicates that the alert is not handled, 1 indicates that the alert is being processed, and 2 indicates that the alert is closed. alarmCount: the number of alerts. handleUserName: the user who handled the alert. shield: indicates whether the alert is blocked. region: the region ID. product: the product that triggered the alert. cluster: the cluster that triggered the alert. service: the service that triggered the alert. hostname: the hostname. checkInterval: the time interval at which the system checks for alerts. lastAlarmTime: the last time when an alert was triggered. updateTime: the time when the alert information was updated. description: the description of the alert.

**Examples**

Sample requests

```
GET /openapi/popResource/aso/incident/api/alert/list HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "msg":"\"\"",
 "eagleEyeTraceId":"0acd10a616545993190765214d002a",
 "cost":30,
 "code":"200",
 "data":{
```

```json
  "total":"42589",
  "totalPage":"42589",
  "pageSize":"1",
  "page":"1",
  "objectList":[
```

`{`

```json
    "shield":"false",
    "cluster":"",
    "checkInterval":"0",
    "metricName":"base_base_meta_project_checker",
    "code":"base_base_meta_project_checker",
    "source":"bcc",
    "type":"default",
    "duration":"183463223",
    "alarmCount":"3052",
    "hostname":"docker010212012134",
    "startTime":"2022-11-12T00:01:16.000+0000",
    "id":"31360",
    "product":"",
    "handleUserName":"",
    "level":"2",
    "updateTime":"2022-11-14T02:58:38.000+0000",
    "alarmName":"base_base_meta_project_checker",
    "message":"base - base_base_meta_project_checker - warning - The Job: [mc_export ]
state is Failed!",
    "lastAlarmTime":"2022-11-14T02:58:38.000+0000",
    "serverRole":"",
    "alarmRule":"",
    "createTime":"2022-11-12T00:01:16.000+0000",
    "service":"",
    "endTime":"1970-01-01T00:00:00.000+0000",
    "region":"cn-XX-XX-XX",
    "currentValue":"",
    "dimensions":[
```

`{`

```json
      "standard":"true",
      "value":"docker0123456789",
      "key":"hostname"
```

`},` `{`

```json
      "standard":"false",
      "value":"tcheck",
      "key":"source"
```

`}` `],`

```json
    "status":"0"
```

`}` `]` `},`

```json
 "errorMessage":"\"\"",
 "errorCode":"\"\"",
 "message":"\"\"",
 "version":"v1",
 "successResponse":true,
```

`"`

```
Rl""
```

`id`

```
t#"
```

```json
 "serverRole":"aso-emergency.Incident#",
 "path":"/aso/incident/api/alert/list",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "errorStack":"\"\""
```

`}` ASO 2022-01-18

###### 7.1.1.1.1 Supplementary details on GetIncidentAlertList

##### GetIncidentAlertList

This topic provides supplementary details on the request and response parameters of the `GetIncidentAlertList` operation.

> **Note:** Multiple key-value pairs may be returned for $.data.objectList[*].dimensions[*]. The following table describes the key-value pair that matches each alert item. N/A indicates any key-value pair.
> For more information about the alert ID and alert information, see Alarm Reference in the Maintenance ASO section on the Help and Open Platform page. You can find the page by clicking the Help documentation icon in the upper-right corner of the Apsara Uni-manager Operations Console.

| Alert item | Code parameter value | Value of $.data.objectList[*].di mensions[*].key | Value of $. data.objectList[*].dime nsions[*].value |
|---|---|---|---|
| High CPU temperature |   |   | CPUMonitor |
| Abnormal motherboard voltage |   |   | BoardMonitor |
| Memory ECC error |   |   | MemoryMonitor |
| Number of hard disk media exceptions ≥ 100 |   |   | DiskError |

|   | hardware monitor ne _ _ | monitor |   |
|---|---|---|---|
| Input packet receiving error rate of the network interface controller (NIC) > 1/100000 |   |   | NetworkCableMonitor |
|   | w alarm _ |   |   |
| NIC flapping |   |   | NetworkCableMonitor |
| Power outage |   |   | PowerMonitor |
| RAID controller failure |   |   | RaidCard |
| Hard disk media exception |   |   | DiskError |
| High NVMe SSD temperature |   |   | PcieFlashMonitor |
| RAID controller restart or exception |   |   | SasRaidMonitor |
| Fan speed < 1,000 RPM |   |   | FanMonitor |
| NTP offset | host ntp sync state al _ _ _ _ arm | N/A | N/A |
| Damaged disk of Apsara Distributed File System | check pangu disk err _ _ _ or | N/A | N/A |

##### 7.1.1.2 GetMetricData

Queries monitoring data. GetMetricData can be used for on-demand display of monitoring dashboards, but is not suitable for directly connecting to three-party monitoring and alerting systems (scheduled collection). If you need to connect to three-party monitoring and alerting systems, we recommend that you use the GetIncidentAlertList operation.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |
|---|---|---|---|---|---|
| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/incident/api/metric/getMetricData HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| metricProj ect | Strin g | Quer y | Yes | tjm tianji _ | The monitoring project. |
| metricNam e | Strin g | Quer y | Yes | cpu host _ | The metric name. |
| startTime | Long | Quer y | Yes | 1654582166000 | The beginning of the time range to query. Unit: milliseconds. |

| endTime | Long | Quer y | Yes | 1654582166000 | The end of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|---|
| period | Integ er | Quer y | Yes | 600 | The monitoring period for which data is queried. Unit: seconds. |
| dimension s | Strin g | Quer y | Yes | {"host": "d22XXXX.XXX.XXX.XXX" } | Dimensions of the metric in the JSON format. |

The following code block shows an example of how to specify the key-value pairs of dimensions:

```
Map<String, String> dimensionsMap = new HashMap<>(); dimensionsMap.put("cluster", "ECS-IO8XXX-X-XXXX"); dimensionsMap.put("host", "d22XXX.cloud.XXX.amtestXXX"); String dimensions = JSON.toJSONString(dimensionsMap); getMetricDataRequest.setDimensions(dimensions); ...
```

For more information about the key-value pairs that can be set in `dimensionsMap` , see the Supplementary details on GetMetricData topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO INCIDENT SYS _ _ TEM ERROR _ | The error code. |
| errorMessage | String | Response error caused by: query tianjimon error, code=400 | The error message. |

| data | Map | {"size":"1","datapo ints": [{"util max":"1.1"," _ hirq avg":"0.0","sy _ s avg":"0.4333333 _ 333333333","sirq _ avg":"0.0","wait av _ g":"0.0999999999 9999999","util avg _ ":"0.86666666666 66667","user max" _ :"0.5","hirq max":" _ 0.0","host":"d22i0X X.XXX.XXX.XXX","s irq max":"0.0","sys _ max":"0.6","user _ _ avg":"0.422222222 2222222","wait m _ ax":"0.1","timesta mp":"1654582200 000"}],"total":"1"} | The response. |
|---|---|---|---|
| cost | Long | 30 | The response time. Unit: milliseconds. |
| errCode | String | failed | The error code. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| eagleEyeTrace Id | String | 0acd18e31654599 3193995236d0029 | The EagleEye ID. |
| errMessage | String | "" | The error message. An empty string is returned if the request is successful. |
| errTitle | String | "" | The title of the error message. |
| requestURI | String | /aso/incident | The request path. |
| responseVersi on | String | v1 | The version of the response format. |

| serviceRole | String | "" | The service role. |
|---|---|---|---|
| code | String | 500 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso- emergency.Inciden t# | The server role. |
| path | String | /aso/incident/api/m etric/getMetricData | The URL of the API. |
| errorTitle | String | Response error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/incident/api/metric/getMetricData HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0acd18e316545993193995236d0029",
 "cost":30,
 "code":"500",
 "data":{
  "datapoints":[
```

`{`

```json
    "util_max":"1.1",
    "hirq_avg":"0.0",
    "sys_avg":"0.4333333333333333",
    "sirq_avg":"0.0",
    "wait_avg":"0.09999999999999999",
    "util_avg":"0.8666666666666667",
    "user_max":"0.5",
    "hirq_max":"0.0",
    "host":"d22i0XX.XXX.XXX.XXX",
    "sirq_max":"0.0",
    "sys_max":"0.6",
    "user_avg":"0.4222222222222222",
    "wait_max":"0.1",
    "timestamp":"1654582200000"
```

`}` `],`

```json
  "total":"1",
  "size":"1"
```

`},`

```json
 "errTitle":"\"\"",
 "serviceRole":"\"\"",
 "errorMessage":"Response error caused by: query tianjimon error, code=400",
 "errorCode":"ASO_INCIDENT_SYSTEM_ERROR",
 "requestURI":"/aso/incident ",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-emergency.Incident#",
 "path":"/aso/incident/api/metric/getMetricData",
 "responseVersion":"v1",
 "errCode":"failed",
 "success":true,
 "errorTitle":"Response error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "errMessage":"\"\""
```

`}` ASO 2022-01-18

###### 7.1.1.2.1 Supplementary details on GetMetricData

This topic provides supplementary details on the request and response parameters of the `GetMetricData` operation.
1. In this topic, `metricProject` is set to tjm_tianji.
2. The following table describes the settings of other parameters.

| Metric | metricNam e | Key of dimensions (in the JSON format) | Minimum value of period | Key of the field in the $.data.data points array | Description | Unit |
|---|---|---|---|---|---|---|
| Status of processes on the host | check task _ host _ | cluster host | 60 | state | Indicates whether the query request was successful. Valid values: 0 and 1. 0 indicates that the query request was successful. 1 indicates that the query request failed. fail |   |
|   |   |   |   | thread usa _ ge | The thread utilization of the host. | % |

|   |   |   |   | z count _ | The number of zombie processes. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | d count _ | The number of defunc processes. | N/A |
|   |   |   |   | pid usage _ | The PID utilization of the host. | % |
|   |   |   |   | state | Indicates whether the query request was successful. Valid values: 0 and 1. 0 indicates that the query request was successful. 1 indicates that the query request failed. fail |   |
| DNS status of the host | check dns _ _ host | cluster host | 60 |   |   |   |
|   |   |   |   | dns state _ | The DNS status. |   |

| Disk mounting status | check mou _ nt host _ | cluster host | 60 | state | Indicates whether the query request was successful. Valid values: 0 and 1. 0 indicates that the query request was successful. 1 indicates that the query request failed. fail |   |
|---|---|---|---|---|---|---|
|   |   |   |   | mount stat _ e | The disk mounting status. |   |
|   |   |   |   | mount poi _ nt state _ | Indicates whether the mount point is read-only. |   |
|   | check kern _ el host _ | cluster host | 60 | cluster | The cluster name. |   |
|   |   |   |   | host | The physical host name. |   |

| Kernel out- of-memory (OOM) error check status |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | state | Indicates whether the query request was successful. Valid values: 0 and 1. 0 indicates that the query request was successful. 1 indicates that the query request failed. fail |   |
|   |   |   |   | kernel stat _ e | The kernel status. |   |
| Network connection status of the host | check net _ work host _ | cluster host | 60 | state | Indicates whether the query request was successful. Valid values: 0 and 1. 0 indicates that the query request was successful. 1 indicates that the query request failed. fail |   |
|   |   |   |   | close wait _ _ count | The number of Transmissi on Control Protocol (TCP) connection s in the CLOSE WAI _ T state. | N/A |

| System load of the host | load host _ | cluster host | 60 | host | The physical host name. |   |
|---|---|---|---|---|---|---|
|   |   |   |   | load1 avg _ | The average system load over the previous minute. | % |
|   |   |   |   | load1 max _ | The maximum system load over the previous minute. | % |
|   |   |   |   | load5 avg _ | The average system load over the previous 5 minutes. | % |
|   |   |   |   | load5 max _ | The maximum system load over the previous 5 minutes. | % |
|   |   |   |   | load15 avg _ | The average system load over the previous 15 minutes. | % |

|   |   |   |   | load15 ma _ x | The maximum system load over the previous 15 minutes. | % |
|---|---|---|---|---|---|---|
| CPU utilization |   | cluster |   | host | The physical host name. |   |
|   |   |   |   | user avg _ | The average amount of time that the CPU ran in the user state. | 0 |
|   |   |   |   | sys avg _ | The average amount of time that the CPU ran in the kernel state. | 0 |
|   |   |   |   | wait avg _ | The average amount of time spent on an I/O wait. | 0 |
|   |   |   |   | hirq avg _ | The average amount of time that the CPU spent processing hardware interrupt requests. | 0 |
| of the host | cpu host _ | host | 60 |   |   |   |

|   |   |   |   | sirq avg _ | The average amount of time that the CPU spent processing software interrupt requests. | 0 |
|---|---|---|---|---|---|---|
|   |   |   |   | util avg _ | The average CPU utilization. | 0 |
|   |   |   |   | util max _ | The maximum CPU utilization. | 0 |
|   |   |   |   | host | The physical host name. |   |
|   |   |   |   | used avg _ | The average used memory. | KiB |
|   |   |   |   | used max _ | The maximum used memory. | KiB |
|   |   |   |   | buff avg _ | The average buffer memory. | KiB |
|   |   |   |   | buff max _ | The maximum buffer memory. | KiB |
|   |   |   |   | cach avg _ | The average cache memory. | KiB |

|   |   |   |   | cach max _ | The maximum cache memory. | KiB |
|---|---|---|---|---|---|---|
|   |   |   |   | total avg _ | The average memory. | KiB |
|   |   |   |   | total max _ | The maximum memory. | KiB |
|   |   |   |   | util avg _ | The average memory utilization. Memory utilization is calculated based on the following formula: Memory utilization = (Total memory - Free memory - Buffer memory - Cache memory) / Total memory × 100%. | 0 |
| Memory utilization of the host | memo hos _ t | cluster host | 60 |   |   |   |

|   |   |   |   | util max _ | The maximum CPU utilization. Memory usage is calculated based on the following formula: Memory utilization = (Total memory - Free memory - Buffer memory - Cache memory) / Total memory × 100%. | 0 |
|---|---|---|---|---|---|---|
|   |   |   |   | host | The physical host name. |   |
|   |   |   |   | partition | The partition name. |   |

|   |   |   |   | free avg _ | The average size of idle partitions in the disk. | Bytes |
|---|---|---|---|---|---|---|
| Disk utilization of the host | disk host _ | cluster host partition | 60 |   |   |   |
|   |   |   |   | free max _ | The maximum size of idle partitions in the disk. | Bytes |
|   |   |   |   | used avg _ | The average size of occupied partitions in the disk. | Bytes |
|   |   |   |   | used max _ | The maximum size of occupied partitions in the disk. | Bytes |
|   |   |   |   | totl avg _ | The average size of partitions in the disk. | Bytes |
|   |   |   |   | totl max _ | The maximum size of partitions in the disk. | Bytes |
|   |   |   |   | util avg _ | The average space utilization of partitions in the disk. | 0 |

|   |   |   |   | util max _ | The maximum space utilization of partitions in the disk. | 0 |
|---|---|---|---|---|---|---|
|   |   |   |   | ifree avg _ | The average number of idle inodes. | N/A |
|   |   |   |   | ifree max _ | The maximum number of idle inodes. | N/A |
|   |   |   |   | itotl avg _ | The average number of inodes. | N/A |
|   |   |   |   | itotl max _ | The maximum number of inodes. | N/A |
|   |   |   |   | iused avg _ | The average number of used inodes. | N/A |
|   |   |   |   | iused max _ | The maximum number of used inodes. | N/A |
|   |   |   |   | iutil avg _ | The average inode usage. | % |
|   |   |   |   | iutil max _ | The maximum inode usage. | % |

| Network traffic of the host | traffic host _ | cluster host | 60 | host | The physical host name. |   |
|---|---|---|---|---|---|---|
|   |   |   |   | ifin avg _ | The average inbound network interface controller (NIC) traffic. | Byte/s |
|   |   |   |   | ifin max _ | The maximum inbound NIC traffic. | Byte/s |
|   |   |   |   | ifout avg _ | The average outbound NIC traffic. | Byte/s |
|   |   |   |   | ifout max _ | The maximum outbound NIC traffic. | Byte/s |
|   |   |   |   | pktin | The packet reception rate of NICs. | pps |
|   |   |   |   | pktout | The packet transmissio n rate of NICs. | pps |
|   |   |   |   | pkterr avg _ | The average packet error rate of NICs. | pps |
|   |   |   |   | pkterr max _ | The maximum packet error rate of NICs. | pps |

|   |   |   |   | pktdrp avg _ | The average packet loss rate of NICs. | pps |
|---|---|---|---|---|---|---|
|   |   |   |   | pktdrp ma _ x | The maximum packet loss rate of NICs. | pps |
|   |   |   |   | host | The physical host name. |   |
|   |   |   |   | TCP _ | The number of TCP connection s. | N/A |
|   |   |   |   | TCP avg _ _ | The average number of TCP connection s. | N/A |
|   |   |   |   | TCP max _ _ | The maximum number of TCP connection s. | N/A |
|   |   |   |   | estab _ | The number of TCP connection s that are established . | N/A |
|   |   |   |   | estab ma _ _ x | The maximum number of TCP connection s that are established . | N/A |

|   |   |   |   | estab su _ _ m | The total number of TCP connection s that are established on all hosts. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | estab avg _ _ | The average number of TCP connection s that are established . | N/A |
|   |   |   |   | synrecv _ | The number of TCP connection s that are in the SYNCRECEI VE state. | N/A |
|   |   |   |   | synrecv a _ _ vg | The average number of TCP connection s that are in the SYNCRECEI VE state. | N/A |
| TCP connection s of the host | tcp conns _ _ host | cluster host | 60 |   |   |   |
|   |   |   |   | closed _ | The number of closed TCP connection s. | N/A |
|   |   |   |   | closed ma _ _ x | The maximum number of closed TCP connection s. | N/A |

|   |   |   |   | closed su _ _ m | The total number of closed TCP connection s of all hosts. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | closed av _ _ g | The average number of closed TCP connection s. | N/A |
|   |   |   |   | timewait _ | The number of TCP connection s in the TIME WAIT _ state. | N/A |
|   |   |   |   | timewait _ _ max | The maximum number of TCP connection s in the TIME WAIT _ state. | N/A |
|   |   |   |   | timewait _ _ sum | The total number of TCP connection s in the TIME WAIT _ state of all hosts. | N/A |
|   |   |   |   | timewait _ _ avg | The average number of TCP connection s in the TIME WAIT _ state. | N/A |
|   |   |   |   | ports _ | The number of ports. | N/A |

|   |   |   |   | ports avg _ _ | The average number of ports. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | ports max _ _ | The maximum number of ports. | N/A |
| TCP traffic status of the host | tcp host _ | cluster host | 60 | host | The physical host name. |   |
|   |   |   |   | active avg _ | The average number of actively opened TCP connection s. | N/A |
|   |   |   |   | pasive avg _ | The average number of passively opened TCP connection s. | N/A |
|   |   |   |   | EstReset a _ vg | The average number of TCP resets. | N/A |
|   |   |   |   | retran avg _ | The average TCP retransmis sion rate. | % |
|   |   |   |   | host | The physical host name. |   |

| psara Uni-ma Console | nager Operatio | ns |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | disk | The disk name. Examples: sda, sdg, and sdb. |   |
|   |   |   |   | util avg _ | The average percentage of the CPU time that is taken to make I/O requests to the device to the total CPU time (bandwidth utilization of the device). | % |
|   |   |   |   | util max _ | The maximum percentage of the CPU time that is taken to make I/O requests to the device to the total CPU time (bandwidth utilization of the device). | % |
|   |   |   |   | rrqms avg _ | The average number of merged read requests sent to the device per second. | N/A |
|   |   |   |   | rrqms max _ | The maximum number of merged read requests sent to the device per second. | N/A |

| Disk I/O usage of | io host _ | cluster host disk | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | wrqms avg _ | The average number of merged write requests sent to the device per second. | N/A |
|   |   |   |   | wrqms ma _ x | The maximum number of merged write requests sent to the device per second. | N/A |
|   |   |   |   | rs avg _ | The average number of read requests sent to the device per second. | N/A |
|   |   |   |   | rs max _ | The maximum number of read requests sent to the device per second. | N/A |
|   |   |   |   | ws avg _ | The average number of write requests sent to the device per second. | N/A |
| the host |   |   |   |   |   |   |

|   |   |   |   | ws max _ | The maximum number of write requests sent to the device per second. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | rsecs avg _ | The average number of sectors read from the device per second. | N/A |
|   |   |   |   | rsecs max _ | The maximum number of sectors read from the device per second. | N/A |
|   |   |   |   | wsecs avg _ | The average number of sectors written to the device per second. | N/A |
|   |   |   |   | wsecs max _ | The maximum number of sectors written to the device per second. | N/A |
|   |   |   |   | rqsize avg _ | The average size of requests sent to the device. | KB |

|   |   |   |   | rqsize max _ | The maximum size of requests sent to the device. | KB |
|---|---|---|---|---|---|---|
|   |   |   |   | qusize avg _ | The average queue length of requests sent to the device. | N/A |
|   |   |   |   | qusize ma _ x | The maximum queue length of requests sent to the device. | N/A |
|   |   |   |   | await avg _ | The average latency per device I/O operation. | ms |
|   |   |   |   | await max _ | The maximum latency per device I/O operation. | ms |
|   |   |   |   | svctm avg _ | The average service time to make I/O requests to the device. | ms |
|   |   |   |   | svctm max _ | The maximum service time per device I/O operation. | ms |

| Network Time Protocol (NTP) time synchroniz ation status | ntp host _ | cluster host | 60 | host | The physical host name. |   |
|---|---|---|---|---|---|---|
|   |   |   |   | sync _ | Indicates whether to synchroniz e time with the NTP server. Valid values: 0 and 1. 0 indicates that time synchroniz ation is disabled. 1 indicates that time synchroniz ation is enabled. |   |
|   |   |   |   | offset[The _ offset depends on the value of sync. If _ the value of sync is _ 1, the offset will only be 0.] | The offset between the time of the host and the time of the NTP server. | ms |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | load1 avg _ | The average system load over the previous minute. | 0 |
|   |   |   |   | load1 max _ | The average system load over the previous minute. | 0 |

| System load of the cluster | load cluste _ r | cluster | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | load5 avg _ | The average system load over the previous 5 minutes. | 0 |
|   |   |   |   | load5 max _ | The maximum system load over the previous 5 minutes. | 0 |
|   |   |   |   | load15 avg _ | The average system load over the previous 15 minutes. | 0 |
|   |   |   |   | load15 ma _ x | The maximum system load over the previous 15 minutes. | 0 |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | user avg _ | The average amount of time that the CPU ran in the user state. | 0 |
|   |   |   |   | sys avg _ | The average amount of time that the CPU ran in the kernel state. | 0 |

| CPU utilization of the | cpu cluster _ | cluster | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | wait avg _ | The average amount of time spent on an I/O wait. | 0 |
|   |   |   |   | hirq avg _ | The average amount of time that the CPU spent processing hardware interrupt requests. | 0 |
| cluster |   |   |   |   |   |   |
|   |   |   |   | sirq avg _ | The average amount of time that the CPU spent processing software interrupt requests. | 0 |
|   |   |   |   | util avg _ | The average CPU utilization. | 0 |
|   |   |   |   | util max _ | The maximum CPU utilization. | 0 |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | used avg _ | The average used memory. | KiB |
|   |   |   |   | used max _ | The maximum used memory. | KiB |

|   |   |   |   | buff avg _ | The average buffer memory. | KiB |
|---|---|---|---|---|---|---|
| Memory utilization of the cluster | memo clus _ ter | cluster | 60 |   |   |   |
|   |   |   |   | buff max _ | The maximum buffer memory. | KiB |
|   |   |   |   | cach avg _ | The average cache memory. | KiB |
|   |   |   |   | cach max _ | The maximum cache memory. | KiB |
|   |   |   |   | total avg _ | The average memory. | KiB |
|   |   |   |   | total max _ | The maximum memory. | KiB |
|   |   |   |   | util avg _ | The average memory utilization. Memory utilization is calculated based on the following formula: Memory utilization = (Total memory - Free memory - Buffer memory - Cache memory) / Total memory × 100%. | % |

|   |   |   |   | util max _ | The maximum CPU utilization. Memory usage is calculated based on the following formula: Memory utilization = (Total memory - Free memory - Buffer memory - Cache memory) / Total memory × 100%. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | partition | The partition name. |   |
|   |   |   |   | free avg _ | The average size of idle partitions in the disk. | Bytes |
|   |   |   |   | free max _ | The maximum size of idle partitions in the disk. | Bytes |
|   |   |   |   | used avg _ | The average size of occupied partitions in the disk. | Bytes |

|   |   |   |   | used max _ | The maximum size of occupied partitions in the disk. | Bytes |
|---|---|---|---|---|---|---|
|   |   |   |   | totl avg _ | The average size of partitions in the disk. | Bytes |
|   |   |   |   | totl max _ | The maximum size of partitions in the disk. | Bytes |
|   |   |   |   | util avg _ | The average space utilization of partitions in the disk. | % |
| Disk usage of the cluster | disk cluste _ r | cluster partition | 60 |   |   |   |
|   |   |   |   | util max _ | The maximum space utilization of partitions in the disk. | % |
|   |   |   |   | ifree avg _ | The average number of idle inodes. | N/A |
|   |   |   |   | ifree max _ | The maximum number of idle inodes. | N/A |
|   |   |   |   | itotl avg _ | The average number of inodes. | N/A |

|   |   |   |   | itotl max _ | The maximum number of inodes. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | iused avg _ | The average number of used inodes. | N/A |
|   |   |   |   | iused max _ | The maximum number of used inodes. | N/A |
|   |   |   |   | iutil avg _ | The average inode utilization. | % |
|   |   |   |   | iutil max _ | The maximum inode utilization. | % |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | ifin avg _ | The average inbound NIC traffic. | Byte/s |
|   |   |   |   | ifin max _ | The maximum inbound NIC traffic. | Byte/s |
|   |   |   |   | ifout avg _ | The average outbound NIC traffic. | Byte/s |
|   |   |   |   | ifout max _ | The maximum outbound NIC traffic. | Byte/s |

| Network traffic of the cluster | traffic clust _ er | cluster | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | pktin | The packet reception rate of NICs. | pps |
|   |   |   |   | pktout | The packet transmissio n rate of NICs. | pps |
|   |   |   |   | pkterr avg _ | The average packet error rate of NICs. | pps |
|   |   |   |   | pkterr max _ | The maximum packet error rate of NICs. | pps |
|   |   |   |   | pktdrp avg _ | The average packet loss rate of NICs. | pps |
|   |   |   |   | pktdrp ma _ x | The maximum packet loss rate of NICs. | pps |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | TCP _ | The number of TCP connection s. | N/A |
|   |   |   |   | TCP avg _ _ | The average number of TCP connection s. | N/A |

|   |   |   |   | TCP max _ _ | The maximum number of TCP connection s. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | estab _ | The number of TCP connection s that are established . | N/A |
|   |   |   |   | estab ma _ _ x | The maximum number of TCP connection s that are established . | N/A |
|   |   |   |   | estab su _ _ m | The total number of TCP connection s that are established . | N/A |
|   |   |   |   | estab avg _ _ | The average number of TCP connection s that are established . | N/A |
|   |   |   |   | synrecv _ | The number of TCP connection s that are in the SYNCRECEI VE state. | N/A |

| TCP connection s of the cluster | tcp conns _ _ cluster | cluster | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | synrecv a _ _ vg | The average number of TCP connection s that are in the SYNCRECEI VE state. | N/A |
|   |   |   |   | closed _ | The number of closed TCP connection s. | N/A |
|   |   |   |   | closed ma _ _ x | The maximum number of closed TCP connection s. | N/A |
|   |   |   |   | closed su _ _ m | The total number of closed TCP connection s. | N/A |
|   |   |   |   | closed av _ _ g | The average number of closed TCP connection s. | N/A |
|   |   |   |   | timewait _ | The number of TCP connection s in the TIME WAIT _ state. | N/A |
|   |   |   |   | timewait _ _ max | The maximum number of TCP connection s in the TIME WAIT _ state. | N/A |

|   |   |   |   | timewait _ _ sum | The total number of TCP connection s in the TIME WAIT _ state. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | timewait _ _ avg | The average number of TCP connection s in the TIME WAIT _ state. | N/A |
|   |   |   |   | ports _ | The number of ports. | N/A |
|   |   |   |   | ports avg _ _ | The average number of ports. | N/A |
|   |   |   |   | ports max _ _ | The maximum number of ports. | N/A |
| TCP traffic status of the cluster | tcp cluster _ | cluster | 60 | cluster | The cluster name. |   |
|   |   |   |   | active avg _ | The average number of actively opened TCP connection s. | N/A |
|   |   |   |   | pasive avg _ | The average number of passively opened TCP connection s. | N/A |

|   |   |   |   | EstReset a _ vg | The average number of TCP resets. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | retran avg _ | The average TCP retransmis sion rate. | % |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | disk | The disk name. Examples: sda, sdg, and sdb. |   |
|   |   |   |   | util avg _ | The average percentage of the CPU time that is taken to make I/O requests to the device to the total CPU time (bandwidth utilization of the device). | % |
|   |   |   |   | util max _ | The maximum percentage of the CPU time that is taken to make I/O requests to the device to the total CPU time (bandwidth utilization of the device). | % |

|   |   |   |   | rrqms avg _ | The average number of merged read requests sent to the device per second. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | rrqms max _ | The maximum number of merged read requests sent to the device per second. | N/A |
|   |   |   |   | wrqms avg _ | The average number of merged write requests sent to the device per second. | N/A |
|   |   |   |   | wrqms ma _ x | The maximum number of merged write requests sent to the device per second. | N/A |

| Disk I/O usage of the cluster | io cluster _ | cluster disk | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | rs avg _ | The average number of read requests sent to the device per second. | N/A |
|   |   |   |   | rs max _ | The maximum number of read requests sent to the device per second. | N/A |
|   |   |   |   | ws avg _ | The average number of write requests sent to the device per second. | N/A |
|   |   |   |   | ws max _ | The maximum number of write requests sent to the device per second. | N/A |
|   |   |   |   | rsecs avg _ | The average number of sectors read from the device per second. | N/A |
|   |   |   |   | rsecs max _ | The maximum number of sectors read from the device per second. | N/A |

|   |   |   |   | wsecs avg _ | The average number of sectors written to the device per second. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | wsecs max _ | The maximum number of sectors written to the device per second. | N/A |
|   |   |   |   | rqsize avg _ | The average size of requests sent to the device. | KB |
|   |   |   |   | rqsize max _ | The maximum size of requests sent to the device. | KB |
|   |   |   |   | qusize avg _ | The average queue length of requests sent to the device. | N/A |
|   |   |   |   | qusize ma _ x | The maximum queue length of requests sent to the device. | N/A |

|   |   |   |   | await avg _ | The average latency per device I/O operation. | ms |
|---|---|---|---|---|---|---|
|   |   |   |   | await max _ | The maximum latency per device I/O operation. | ms |
|   |   |   |   | svctm avg _ | The average service time to make I/O requests to the device. | ms |
|   |   |   |   | svctm max _ | The maximum service time per device I/O operation. | ms |
| CPU utilization of the Docker instance | docker cpu _ usage _ | cluster hostname serverRole app dockerNam e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |

|   |   |   |   | cpu usage _ min _ | The minimum CPU utilization. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | cpu usage _ max _ | The maximum CPU utilization. | % |
|   |   |   |   | cpu usage _ avg _ | The average CPU utilization. | % |
|   |   |   |   | cpu util av _ _ g | The CPU utilization. | % |
| System- mode CPU utilization of the Docker instance | docker cpu _ system _ | cluster hostname serverRole app dockerNam e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | cpu syste _ m min _ | The minimum system- mode CPU utilization. | % |

|   |   |   |   | cpu syste _ m max _ | The maximum system- mode CPU utilization. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | cpu syste _ m avg _ | The average system- mode CPU utilization. | % |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
| User-mode CPU utilization of the Docker instance | docker cpu _ user _ | cluster hostname serverRole app dockerNam e | 60 |   |   |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | cpu user _ _ min | The minimum user-mode CPU utilization. | % |
|   |   |   |   | cpu user _ _ max | The maximum user-mode CPU utilization. | % |
| 02 |   |   |   | > Document Version: 2025110 |   |   |

|   |   |   |   | cpu user a _ _ vg | The average user-mode CPU utilization. | % |
|---|---|---|---|---|---|---|
| Memory usage of the Docker instance | docker me _ mory max _ | cluster hostname serverRole app dockerNam e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | memory m _ ax min _ | The lowest maximum memory usage. | Bytes |
|   |   |   |   | memory m _ ax max _ | The highest maximum memory usage. | Bytes |
|   |   |   |   | memory m _ ax avg _ | The average maximum memory usage. | Bytes |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |

| Developer Guid | e·API Referen | ce |   |   |   |   |
|---|---|---|---|---|---|---|
| Memory usage of the Docker instance | docker me _ mory used _ | cluster hostname serverRole app dockerNam e | 60 |   |   |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | memory u _ sed min _ | The minimum memory usage. | Bytes |
|   |   |   |   | memory u _ sed max _ | The maximum memory usage. | Bytes |
|   |   |   |   | memory u _ sed avg _ | The average memory usage. | Bytes |
| Memory limit of the Docker instance | docker me _ mory limit _ |   | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |

|   |   | cluster hostname serverRole app dockerNam e |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | memory li _ mit min _ | The minimum memory limit. | Bytes |
|   |   |   |   | memory li _ mit max _ | The maximum memory limit. | Bytes |
|   |   |   |   | memory li _ mit avg _ | The average memory limit. | Bytes |
| Memory utilization of the Docker instance | docker me _ mory util _ | cluster hostname serverRole app dockerNam e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | memory ut _ il min _ | The minimum memory utilization. | % |
|   |   |   |   | memory ut _ il max _ | The maximum memory utilization. | % |
| > Document V | ersion: 202511 | 07 |   | 10 |   |   |

|   |   |   |   | memory ut _ il avg _ | The average memory utilization. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
| Number of memory errors on the Docker instance | docker me _ mory failcn _ t | cluster hostname serverRole app dockerNam e | 60 |   |   |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | memory fa _ ilcnt min _ | The minimum number of memory errors. | N/A |
|   |   |   |   | memory fa _ ilcnt max _ | The maximum number of memory errors. | N/A |
|   |   |   |   | memory fa _ ilcnt avg _ | The average number of memory errors. | N/A |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |

| psara Uni-ma onsole | nager Operatio | ns |   |   |   |   |
|---|---|---|---|---|---|---|
| tianji Disk I/O read rate of the Docker instance | docker io r _ _ ead speed _ | cluster hostname serverRole app dockerNam e | 60 |   |   |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | io read sp _ _ eed min _ | The minimum I/O read rate. | Byte/s |
|   |   |   |   | io read sp _ _ eed max _ | The maximum I/O read rate. | Byte/s |
|   |   |   |   | io read sp _ _ eed avg _ | The average I/O read rate. | Byte/s |
| Disk I/O write rate of the Docker instance | docker io _ _ write spee _ d |   | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |

|   |   | cluster hostname serverRole app dockerNam e |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | io write sp _ _ eed min _ | The minimum I/O write rate. | Byte/s |
|   |   |   |   | io write sp _ _ eed max _ | The maximum I/O write rate. | Byte/s |
|   |   |   |   | io write sp _ _ eed avg _ | The average I/O write rate. | Byte/s |
| Data receive rate of the Docker instance | docker net _ work recei _ ve speed _ | cluster hostname serverRole app dockerNam e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | network re _ ceive spee _ d min _ | The minimum data receive rate. | Byte/s |
|   |   |   |   | network re _ ceive spee _ d max _ | The maximum data receive rate. | Byte/s |
| 08 |   |   |   | > Document Version: 2025110 |   |   |

|   |   |   |   | network re _ ceive spee _ d avg _ | The average data receive rate. | Byte/s |
|---|---|---|---|---|---|---|
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
| Data send rate of the Docker instance | docker net _ work trans _ mit speed _ | cluster hostname serverRole app dockerNam e | 60 |   |   |   |
|   |   |   |   | dockerNam e | The Docker name. |   |
|   |   |   |   | network tr _ ansmit spe _ ed min _ | The minimum data send rate. | Byte/s |
|   |   |   |   | network tr _ ansmit spe _ ed max _ | The maximum data send rate. | Byte/s |
|   |   |   |   | network tr _ ansmit spe _ ed avg _ | The average data send rate. | Byte/s |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |

| Developer Guid | e·API Referen | ce |   |   |   |   |
|---|---|---|---|---|---|---|
| CPU utilization of the service request process | process cp _ u usage _ | cluster hostname serverRole app processTyp e | 60 |   |   |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | cpu usage _ min _ | The minimum CPU utilization. | % |
|   |   |   |   | cpu usage _ max _ | The maximum CPU utilization. | % |
|   |   |   |   | cpu usage _ avg _ | The average CPU utilization. | % |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |

| Memory utilization of the service request process | process m _ em usage _ | cluster hostname serverRole app processTyp e | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | mem usag _ e min _ | The minimum memory utilization. | % |
|   |   |   |   | mem usag _ e max _ | The maximum memory utilization. | % |
|   |   |   |   | mem usag _ e avg _ | The memory utilization. | % |
| Number of file handles of the service request process | process op _ en fd _ | cluster hostname serverRole app processTyp e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | processTyp e | The Docker name. |   |

|   |   |   |   | open fd mi _ _ n | The minimum number of file handles. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | open fd m _ _ ax | The maximum number of file handles. | N/A |
|   |   |   |   | open fd av _ _ g | The average number of file handles. | N/A |
| Number of threads of the service request process | process thr _ ead num _ | cluster hostname serverRole app processTyp e | 60 | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | thread nu _ m min _ | The minimum number of threads. | N/A |
|   |   |   |   | thread nu _ m max _ | The maximum number of threads. | N/A |

|   |   |   |   | thread nu _ m avg _ | The average number of threads of the ontianji process. | N/A |
|---|---|---|---|---|---|---|
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
| Resident set size (RSS) of the service request process | process rss _ | cluster hostname serverRole app processTyp e | 60 |   |   |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | rss min _ | The minimum RSS. | KB |
|   |   |   |   | rss max _ | The maximum RSS. | KB |
|   |   |   |   | rss avg _ | The average RSS. | KB |

| Disk I/O read rate of the service request process | process re _ ad bytes _ | cluster hostname serverRole app processTyp e | 60 | cluster | The cluster name. |   |
|---|---|---|---|---|---|---|
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |
|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | read bytes _ min _ | The minimum I/O read rate. | Byte/s |
|   |   |   |   | read bytes _ max _ | The maximum I/O read rate. | Byte/s |
|   |   |   |   | read bytes _ avg _ | The average I/O read rate. | Byte/s |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | hostname | The hostname. |   |
|   |   |   |   | serverRole | The service role. |   |

|   |   |   |   | app | The application name. A service role may be assumed by multiple application s. |   |
|---|---|---|---|---|---|---|
| Disk I/O write rate of the service request process | process wr _ ite bytes _ | cluster hostname serverRole app processTyp e | 60 |   |   |   |
|   |   |   |   | processTyp e | The Docker name. |   |
|   |   |   |   | write bytes _ min _ | The minimum I/O write rate. | Byte/s |
|   |   |   |   | write bytes _ max _ | The maximum I/O write rate. | Byte/s |
|   |   |   |   | write bytes _ avg _ | The average I/O write rate. | Byte/s |
|   |   | cluster serverrole host | 60 | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | count avg _ | The average number of threads. | N/A |
|   |   |   |   | count max _ | The maximum number of threads. | N/A |

| Thread deadlock status of the Java virtual machine (JVM) instance | jvm.thread. deadlock c _ luster serv _ errole |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | deamon co _ unt avg _ | The average number of daemon threads. | N/A |
|   |   |   |   | deamon co _ unt max _ | The maximum number of daemon threads. | N/A |
|   |   |   |   | deadlock c _ ount avg _ | The average number of deadlocked threads. | N/A |
|   |   |   |   | deadlock c _ ount max _ | The maximum number of deadlocked threads. | N/A |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | blocked av _ g | The average number of blocked threads. | N/A |
|   |   |   |   | blocked m _ ax | The maximum number of blocked threads. | N/A |
|   |   |   |   | new avg _ | The average number of new threads. | N/A |

| Thread status of the JVM instance | jvm.thread. state clust _ er serverro _ le | cluster serverrole host | 60 |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   | new max _ | The maximum number of new threads. | N/A |
|   |   |   |   | runnable a _ vg | The average number of runnable threads. | N/A |
|   |   |   |   | runnable _ max | The maximum number of runnable threads. | N/A |
|   |   |   |   | terminated avg _ | The average number of terminated threads. | N/A |
|   |   |   |   | terminated max _ | The maximum number of terminated threads. | N/A |
|   |   |   |   | timed waiti _ ng avg _ | The average number of threads in the TIME WAIT _ state. | N/A |
|   |   |   |   | timed waiti _ ng max _ | The maximum number of threads in the TIME WAIT _ state. | N/A |
|   |   |   |   | waiting av _ g | The average number of threads in the waiting state. | N/A |

|   |   |   |   | waiting ma _ x | The maximum number of threads in the waiting state. | N/A |
|---|---|---|---|---|---|---|
| Garbage collection status of the JVM instance | jvm.gc clus _ ter serverr _ ole | cluster serverrole host name | 60 | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | count avg _ | The average number of garbage collections during the current data collection period. | N/A |
|   |   |   |   | count max _ | The maximum number of garbage collections during the current data collection period. | N/A |

|   |   |   |   | time avg _ | The average amount of time spent on garbage collection during the current data collection period. | ms |
|---|---|---|---|---|---|---|
|   |   |   |   | time max _ | The maximum amount of time spent on garbage collection during the current data collection period. | ms |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | name | The memory pool name. |   |
|   |   |   |   | init avg _ | The average initial memory during polling. | Bytes |
|   |   |   |   | init max _ | The maximum initial memory during polling. | Bytes |

|   |   |   |   | committed avg _ | The average committed memory during polling. | Bytes |
|---|---|---|---|---|---|---|
|   |   |   |   | committed max _ | The maximum committed memory during polling. | Bytes |
|   |   |   |   | used avg _ | The average used memory during polling. | Bytes |
| Memory usage of the JVM instance during polling | jvm.mem.p oll cluster _ _ serverrole | cluster serverrole host name | 60 |   |   |   |
|   |   |   |   | used max _ | The maximum used memory during polling. | Bytes |
|   |   |   |   | max avg _ | The average maximum available memory during polling. | Bytes |
|   |   |   |   | max max _ | The highest maximum available memory during polling. | Bytes |

|   |   |   |   | usage avg _ | The average memory utilization during polling. Memory utilization is calculated based on the following formula: Memory utilization = Used memory/To tal memory * 100%. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | usage max _ | The maximum memory utilization during polling. Memory utilization is calculated based on the following formula: Memory utilization = Used memory/To tal memory * 100%. | % |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |

| Developer Guid | e·API Referen | ce |   |   |   |   |
|---|---|---|---|---|---|---|
| Memory usage of the JVM instance | jvm.mem.t otal cluster _ serverrole _ | cluster serverrole host | 60 |   |   |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | init avg _ | The average initial memory. | Bytes |
|   |   |   |   | init max _ | The maximum initial memory. | Bytes |
|   |   |   |   | max avg _ | The average used memory. | Bytes |
|   |   |   |   | max max _ | The maximum used memory. | Bytes |
|   |   |   |   | used avg _ | The average maximum available memory. | Bytes |
|   |   |   |   | used max _ | The highest maximum available memory. | Bytes |
|   |   |   |   | cluster | The cluster name. |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | init avg _ | The average initial heap memory. | Bytes |

|   |   |   |   | init max _ | The maximum initial heap memory. | Bytes |
|---|---|---|---|---|---|---|
| Heap memory usage of the JVM instance | jvm.mem.h eap cluster _ serverrole _ | cluster serverrole host | 60 | committed avg _ | The average committed heap memory. | Bytes |
|   |   |   |   | committed max _ | The maximum committed heap memory. | Bytes |
|   |   |   |   | used avg _ | The average used heap memory. | Bytes |
|   |   |   |   | used max _ | The maximum used heap memory. | Bytes |
|   |   |   |   | max avg _ | The average maximum available heap memory. | Bytes |
|   |   |   |   | max max _ | The highest maximum available heap memory. | Bytes |

|   |   |   |   | usage avg _ | The average heap memory utilization. Heap memory utilization is calculated based on the following formula: Heap memory utilization = Used heap memory/To tal heap memory * 100%. | % |
|---|---|---|---|---|---|---|
|   |   |   |   | usage max _ | The maximum heap memory utilization. Heap memory utilization is calculated based on the following formula: Heap memory utilization = Used heap memory/To tal heap memory * 100%. | % |
|   |   |   |   | cluster | The cluster name. |   |
| 24 |   |   |   |   |   |   |

| psara Uni-ma Console | nager Operatio | ns |   |   |   |   |
|---|---|---|---|---|---|---|
| Class loading of the JVM instance | jvm.classlo ader cluste _ r serverrol _ e | cluster serverrole host | 60 |   |   |   |
|   |   |   |   | serverrole | The service role. |   |
|   |   |   |   | host | The hostname. |   |
|   |   |   |   | loaded avg _ | The average number of loaded classes. | N/A |
|   |   |   |   | loaded ma _ x | The maximum number of loaded classes. | N/A |
|   |   |   |   | unloaded a _ vg | The average number of unloaded classes. | N/A |
|   |   |   |   | unloaded _ max | The maximum number of unloaded classes. | N/A |

##### 7.1.1.3 ListAlertByUpdateTime

Traverses alerts by update time.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |
|---|---|---|---|---|---|

**Request syntax**

```
GET /openapi/popResource/aso/incident/api/alert/listByUpdateTime HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| page | Integ er | Quer y | Yes | 1 | The page number. |
| minUpdate Time | Long | Quer y | Yes | 1920001300000 | The minimum value of the time at which the system traverses alerts. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: seconds. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| totalPage | Integer | 262 | The total number of returned pages. |
| pageSize | Integer | 100 | The number of entries per page. |

| total | Integer | 26166 | The total number of entries returned. |
|---|---|---|---|
| page | Integer | 1 | The page number. |
| objectList | Array of objectItem |   | The returned alerts. |
| id | Long | 844934 | The alert ID. |
| startTime | String | 2022-02- 24T08:33:29.000+ 0000 | The time when the alert was triggered. |
| endTime | String | 1970-01- 01T00:00:00.000+ 0000 | The time when the alert was closed. |
| duration | Long | 37197 | The duration of the alert. |
| message | String | Tianji SR Postcheckfailed Alarm01.100.2000. 00002 | The alert message. |
| code | String | tj client proxy ma _ _ _ chine sr monitor s _ _ _ tate | The alert code. |
| metricName | String | tj client proxy ma _ _ _ chine sr monitor s _ _ _ tate | The metric name. |
| alarmName | String | private.C ECS- _ CPUXXXXX tianji p _ _ ostheck monitor al _ _ arm tianji sub- __ _ tianjiclient | The alert name. |

| alarmRule | String | $level==\"error\"\|\| $level==\"ERROR\" \|\|$level==\"FATAL\ "\|\|$level==\"fatal\" | The rule that describes how the alert is triggered. |
|---|---|---|---|
| currentValue | String | {\"level\":\"error\"} | The current value of the metric. |
| source | String | "" | The alert source. |
| type | String | metric | The type of the alert. |
| dimensions | Array of dimension |   | The metric dimensions. |
| key | String | cluste | The dimension key. |
| value | String | ECS-CPU-X-XXXX | The dimension value. |
| standard | Boolean | true | Indicates whether the dimension is a standard dimension. |
| level | Integer | 1 | The severity level of the alert. The values 1 to 4 indicate P1 to P4. |
| status | Integer | 0 | The status of the alert. Valid values: 0: The alert is not handled. 1: The alert is being processed. 2: The alert is closed. |
| alarmCount | Integer | 1 | The number of alerts. |
| handleUserNa me | String | "" | The user who handled the alert. |
| shield | Boolean | false | Indicates whether the alert is blocked. |
| region | String | cn-XX-XX-XX | The region ID. |
| product | String | ecs | The product that triggered the alert. |
| cluster | String | ECS-CPU-X-XXXX | The cluster that triggered the alert. |

| service | String | tianji | The service that triggered the alert. |
|---|---|---|---|
| serverRole | String | "" | The service role. |
| hostname | String | "" | The hostname. |
| checkInterval | Integer | 0 | The time interval at which the system checks for alerts. |
| lastAlarmTime | String | 2022-02- 24T08:33:29.000+ 0000 | The last time when an alert was triggered. |
| updateTime | String | 2022-11- 14T02:58:38.000+ 0000 | The time when the alert information was updated. |
| description | String | test description _ | The description of the alert. By default, the alert is described in Chinese. You can obtain multilingual results by setting request headers aliyun lang and _ aliyun territory . _ |
| cost | Long | 30 | The period of time required to process the request. Unit: milliseconds. |
| errorCode | String | ASO INCIDENT SYS _ _ TEM ERROR _ | The error code. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| eagleEyeTrace Id | String | 0acd0d041659596 1080397999d0027 | The EagleEye ID. |
| msg | String | "" | The error message. |
| errorStack | String | "" | The stack where the error occurred. |

|   | aliyun lang _ |
|---|---|
| aliyun territory _ |   |

| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
|---|---|---|---|
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true. false. |
| serverRole | String | "" | The service role. |
| path | String | /aso/incident/api/al ert/listByUpdateTi me | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListAlertByUpdateTime &page=1 &minUpdateTime=1920001300000 &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "msg":"\"\"",
 "eagleEyeTraceId":"0acd0d0416595961080397999d0027",
 "cost":30,
 "code":"200",
 "data":{
"ttl"26166
```

```json
  "total":26166,
  "totalPage":262,
  "pageSize":100,
  "page":1,
  "objectList":{
   "shield":false,
   "cluster":"ECS-CPU-X-XXXX",
   "checkInterval":0,
   "code":"tj_client_proxy_machine_sr_monitor_state",
   "metricName":"tj_client_proxy_machine_sr_monitor_state",
   "description":"test_description",
   "source":"\"\"",
   "type":"metric",
   "duration":37197,
   "alarmCount":1,
   "hostname":"\"\"",
   "startTime":"2022-02-24T08:33:29.000+0000",
   "id":844934,
   "product":"ecs",
   "level":1,
   "handleUserName":"\"\"",
   "alarmName":"private.C_ECS-CPUXXXXX_tianji_postheck_monitor_alarm__tianji_sub-tianji
client",
   "updateTime":"2022-11-14T02:58:38.000+0000",
   "message":"Tianji SR Postcheckfailed Alarm01.100.2000.00002",
   "lastAlarmTime":"2022-02-24T08:33:29.000+0000",
   "serverRole":"\"\"",
"alarmRule":"$level==\\\"error\\\"||$level==\\\"ERROR\\\"||$level==\\\"FATAL\\\"||$level= \\"fatal\\\"",
   "service":"tianji",
   "endTime":"1970-01-01T00:00:00.000+0000",
   "region":"cn-XX-XX-XX",
   "currentValue":"{\\\"level\\\":\\\"error\\\"}",
   "dimensions":{
    "standard":true,
    "value":"ECS-CPU-X-XXXX ",
    "key":"cluste"
```

`},`

```json
   "status":0
```

`}` `},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_INCIDENT_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"\"\"",
 "path":"/aso/incident/api/alert/listByUpdateTime",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "errorStack":"\"\""
```

`}` ASO 2022-01-18

##### 7.1.1.4 GetAlertList

Queries a list of alerts.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be used when aliyun lang is set to _ zh). US (can be used when aliyun lang is set to _ en). TW (can be used when aliyun lang is set to _ zh). |

**Request syntax**

```
GET /openapi/popResource/aso/fullview/popapi/getAlertList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| type | Strin g | Quer y | No | metric | The alert type. Valid values: metric. event. |
| cluster | Strin g | Quer y | No | OssHybridCluster-X-XX- XX | The cluster to which the alert belongs. |

| alertName | Strin g | Quer y | No | alert a _ | The alert name. |
|---|---|---|---|---|---|
| metricNam e | Strin g | Quer y | No | aso a _ | The monitoring metric. |
| level | Integ er | Quer y | No | 1 | The severity level of the alert. Valid values: 0 to 5. |
| alertProdu ct | Strin g | Quer y | No | oss | The product to which the alert belongs. |
| service | Strin g | Quer y | No | tianji | The service to which the alert belongs. |
| startTime | Strin g | Quer y | Yes | 2021-12-01 00:00:00 | The beginning of the time range to query alerts. Specify the time in the ISO 8601 standard in the yyyy-MM-dd HH:mm:ss format. |
| endTime | Strin g | Quer y | Yes | 2021-12-01 00:00:00 | The end of the time range to query alerts. Specify the time in the ISO 8601 standard in the yyyy-MM- dd HH:mm:ss format. |
| page | Integ er | Quer y | Yes | 1 | The page number. |
| pageSize | Integ er | Quer y | Yes | 15 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO MONITOR SYS _ _ TEM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| result | Array of result |   | The alerts. |
|---|---|---|---|
| id | Integer | 46082 | The alert event ID. |
| hashCode | String | 295452124 | The hash code of the alert. |
| alertName | String | alert name _ | The alert name. |
| metricName | String | oss service- _ cluster error code _ _ _ from chiji _ | The monitoring metric. |
| dimensions | String | {\"cluster\":\"Oss2L 54Cluster-X-XX- XX\",\"serverrole\": \"oss- service.OssCluster Monitor#\",\"host\" :\"vm010017XXXX\ "} | The alert information. |
| alarmId | String | 02.305.0101.0000 5 | The alert ID. |
| message | String | The read and write latency of requests at the frontend of an OSS cluster exceeds the1,000 ms threshold. | The error message. |
| region | String | "" | The region name. |
| product | String | "" | The product to which the alert belongs. |
| cluster | String | OssXX-XX-XX | The cluster to which the alert belongs. |
| service | String | oss-service | The service to which the alert belongs. |
| alertCount | Integer | 1 | The number of historical alerts. |

| eventLevel | String | P3 | The severity level of the alert. |
|---|---|---|---|
| eventStatus | String | Done | The status of the alert. |
| startTime | Long | 1590393226471 | The time when the alert was triggered. |
| lastTime | Long | 1295964673 | The duration of the alert. Unit: milliseconds. |
| processTime | Long | 1590393226471 | The time when the alert was handled. |
| updateTime | Long | 1590393226471 | The time when the alert information was updated. |
| changeRecord | String | [{\"key\":\"Start\",\" time\":1590393226 471,\"value\":\"SER IOUS\"}, {\"key\":\"Recover\ ",\"time\":1590402 946453,\"value\":\" RECOVER\"}] | The record of modifications. |
| notifyFlag | Boolean | true | Indicates whether the notification flag was enabled. |
| dataSource | String | tianjimon | The data source. |
| type | String | test | The type of the monitoring metric. |
| metricProject | String | tjm oss service _ _ | The monitored project. |
| eventType | Integer | 1 | The type of the monitoring object. |
| metricType | String | METRIC | The metric type. |
| eventSource | Map | "" | The event source. |
| contacts | Array of contacts |   | Details about the contacts to which the alert was sent. |
| id | Integer | 1 | The primary key ID. |

| username | String | admin | The alert contact name. |
|---|---|---|---|
| telephone | String | "" | The contact phone number. |
| email | String | "" | The contact email address. |
| dingding | String | 1234567 | The DingTalk account of the contact. |
| product | String | "" | The product whose alerts the contact wants to receive. |
| role | String | "" | The contact role. |
| dutyStartTime | Long | 1592358292430 | The start time of the contact work shift. |
| dutyEndTime | Long | 1592358292430 | The end time of the contact work shift. |
| department | String | dept1 | The department of the contact. |
| region | String | "" | The region name. |
| telephoneNotif icationOn | Boolean | true | The phone notification status. |
| emailNotificati onOn | Boolean | true | The email notification status. |
| dingdingNotifi cationOn | Boolean | true | The DingTalk notification status. |
| products | List | "" | The products whose alerts the contact wants to receive. |
| levels | List | "" | The error level. |
| combinationTy pe | Integer | 1 | The alert combination type for notification. |
| productsJson | String | "" | The products list in the JSON format. |

| levelsJson | String | "" | The alert severity level in the JSON format. |
|---|---|---|---|
| total | Integer | 200 | The total number of entries returned. |
| pageSize | Integer | 15 | The number of entries per page. |
| currentPage | Integer | 1 | The page number. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | fccbab1d-a496- 4ae6-88e8- 83557f883a85 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | SYSTEM ERROR _ | The keyword of the error. |
| level | String | 1 | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso- monitor.Monitor# | The server role of the request. |
| path | String | /aso/fullview/popap i/getAlertList | The URL of the API. |

| responseVersi on | String | v1 | The version of the response format. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/fullview/popapi/getAlertList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "result":{
   "lastTime":1295964673,
   "cluster":"OssXX-XX-XX",
   "metricName":"oss_service-cluster_error_code_from_chiji",
   "eventSource":"",
   "type":"test",
   "processTime":1590393226471,
   "changeRecord":"
[{\\\"key\\\":\\\"Start\\\",\\\"time\\\":1590393226471,\\\"value\\\":\\\"SERIOUS\\\"},{ \\\"key\\\":\\\"Recover\\\",\\\"time\\\":1590402946453,\\\"value\\\":\\\"RECOVER\\\"}]",
   "metricType":"METRIC",
   "eventLevel":"P3 ",
   "alertName":"alert_name ",
   "hashCode":"295452124",
   "alarmId":"02.305.0101.00005",
   "startTime":1590393226471,
   "id": "46082",
   "notifyFlag":true,
   "product":"\"\"",
   "updateTime":1590393226471,
   "eventType":1,
   "message": "The read and write latency of requests at the frontend of an OSS cluster
exceeds the threshold. The threshold is 1,000 ms.", "metricProject":"tjmossservice",
```

```json
   metricProject:tjm_oss_service,
   "alertCount":1,
   "service":"oss-service",
   "eventStatus":"Done",
   "region":"\"\"",
   "dataSource":"tianjimon",
   "contacts":{
    "product":"",
    "role":"\"\"",
    "dutyStartTime":1592358292430,
    "levelsJson":"\"\"",
    "telephone":"\"\"",
    "dingding":"1234567",
    "products":"\"\"",
    "dutyEndTime":1592358292430,
    "productsJson":"\"\"",
    "dingdingNotificationOn":true,
    "combinationType":1,
    "telephoneNotificationOn":true,
    "id":"1",
    "department":"dept1",
    "region":"",
    "emailNotificationOn":true,
    "email":"\"\"",
    "levels":"\"\"",
    "username":"admin"
```

`},`

```json
   "dimensions":"{\\\"cluster\\\":\\\"Oss2L54Cluster-X-XX-
XX\\\",\\\"serverrole\\\":\\\"ossservice.OssClusterMonitor#\\\",\\\"host\\\":\\\"vm010017XXXX\\\"}"
```

`},`

```json
  "total":200,
  "pageSize":15,
  "currentPage":1
```

`},`

```json
 "level":"1",
 "errorMessage":"System error",
 "errorCode":"ASO_MONITOR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-monitor.Monitor#",
 "path":"/aso/fullview/popapi/getAlertList",
 "responseVersion":"v1",
 "requestId":"fccbab1d-a496-4ae6-88e8-83557f883a85",
 "success":true,
 "errorTitle":"Service error",
 "key":"SYSTEM_ERROR"
```

`}` ASO 2022-01-18

##### 7.1.1.5 GetCpuMetrics

Queries CPU utilization.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/cpu HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | m54a01212.cloud.a04.a mtest11 | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries CPU utilization. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | The end of the time range to query. |

| psara Uni-ma onsole | nager O | perations |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| action | Strin g | Query | Yes | util avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [0.4,0.3,0.4,0.3,0.4] ,"name":"util avg" _ }],"categories": [1638352080000,1 638352140000,16 38352200000,163 8352260000,1638 352320000]},"type ":"CPU"} | The response. |
| cost | Long | 54 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | 201a065d-d03a- 4d33-b9ac- 2d9fba9ec6b9 | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/psm/metrics/c pu | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/cpu HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":54,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
      0.4,
      0.3,
      0.4,
      0.3,
      0.4
```

`],`

```json
     "name":"util_avg"
```

`}` `],`

```json
   "categories":[
    1638352080000,
    1638352140000,
    1638352200000,
    1638352260000,
    1638352320000
```

`]` `},`

```json
  "type":"CPU"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/cpu",
 "responseVersion":"v1",
 "requestId":"201a065d-d03a-4d33-b9ac-2d9fba9ec6b9",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

##### 7.1.1.6 GetDiskMetrics

Queries disk utilization.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/disk HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | m5XXX.cloud.aXX.amXX X | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries disk utilization. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | The end of the time range to query. |
| action | Strin g | Query | Yes | util avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [7.8,7.8,7.8,7.8,7.8] ,"name":"util avg" _ }],"categories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"DISK"} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | c1310a2c-56e0- 4ca4-8de0- 87b842a47a9e | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/psm/metrics/d isk | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|
| Parameter | Type | Example | Description |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/disk HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
      7.8,
      7.8,
      7.8,
      7.8,
      7.8
```

`],`

```json
     "name":"util_avg"
```

`}` `],`

```json
   "categories":[
    1638348780000,
    1638348840000,
    1638348900000,
    1638348960000,
    1638349020000
```

`]` `},`

```json
  "type":"DISK"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/disk",
 "responseVersion":"v1",
 "requestId":"c1310a2c-56e0-4ca4-8de0-87b842a47a9e",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

##### 7.1.1.7 GetIoMetrics

Queries disk I/O loads.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/io HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | m5XXX.cloud.aXX.amXX X | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries disk I/O loads. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | The end of the time range to query. |
| action | Strin g | Query | Yes | util avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [0,0,0,0,0],"name": "util avg"}],"categ _ ories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000,16383 49080000]},"type" :"IO"} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | db6ab7b0-f435- 4d2a-80f7- 529750fabf98 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/psm/metrics/i o | The URL of the API. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/io HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
```

`0,` `0,` `0,` `0,` `],`

```json
     "name":"util_avg"
```

`}` `],`

```json
   "categories":[
    1638348780000,
    1638348840000,
    1638348900000,
    1638348960000,
    1638349020000,
    1638349080000
```

`]` `},`

```json
  "type":"IO"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/io",
 "responseVersion":"v1",
 "requestId":"db6ab7b0-f435-4d2a-80f7-529750fabf98",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

##### 7.1.1.8 GetLoadMetrics

Queries system loads.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/load HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | mXXXX.cloud.aXX.amXX | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries system loads. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | The end of the time range to query. |
| action | Strin g | Query | Yes | load1 avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [1.1,1.1,1,1.2,1.4]," name":"load1 avg" _ }],"categories": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"LOAD"} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | e15eef8f-69e4- 47fc-ade7- 8274622447d2 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/psm/metrics/l oad | The URL of the API. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/load HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
      1.1,
      1.1,
```

`1,`

```
      1.2,
      1.4
```

`],`

```json
     "name":"load1_avg"
```

`}` `],`

```json
   "categories":[
    1638348780000,
    1638348840000,
    1638348900000,
    1638348960000,
    1638349020000
```

`]` `},`

```json
  "type":"LOAD"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/load",
 "responseVersion":"v1",
 "requestId":"e15eef8f-69e4-47fc-ade7-8274622447d2",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

##### 7.1.1.9 GetMemMetrics

Queries memory utilization.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/mem HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | mXXX.cloud.aXX.amXX | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries memory utilization. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | The end of the time range to query. |
| action | Strin g | Query | Yes | util avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [10.7,10.7,10.7,10. 7,10.7],"name":"uti l avg"}],"categorie _ s": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"MEM"} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | 48b17b90-621a- 460c-92b4- f2fdd376b287 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d0 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/psm/metrics/ mem | The URL of the API. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/mem HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d0",
 "cost":30,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
      10.7,
      10.7,
      10.7,
      10.7,
      10.7
```

`],`

```json
     "name":"util_avg"
```

`}` `],`

```json
   "categories":[
    1638348780000,
    1638348840000,
    1638348900000,
    1638348960000,
    1638349020000
```

`]` `},`

```json
  "type":"MEM"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/mem",
 "responseVersion":"v1",
 "requestId":"48b17b90-621a-460c-92b4-f2fdd376b287",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

##### 7.1.1.10 GetTrafficMetrics

Queries the traffic of a host.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/psm/metrics/traffic HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| hostname | Strin g | Query | Yes | m54a01212.cloud.a04.a mtest11 | The hostname. |
| interval | Strin g | Query | No | 60 | The time interval at which the system queries the traffic of the host. Unit: seconds. Default value: 60. |
| startTime | Strin g | Query | Yes | 1638348739166 | The beginning of the time range to query. |
| endTime | Strin g | Query | Yes | 1638352339166 | 1638352339166 |
| action | Strin g | Query | Yes | ifin avg _ | The metric dimension that you want to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"data":{"series": [{"data": [2.77,3.08,2.96,2.9 6,2.63],"name":"ifi n avg"}],"categori _ es": [1638348780000,1 638348840000,16 38348900000,163 8348960000,1638 349020000]},"type ":"TRAFFIC"} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestId | String | 0067966f-d480- 4628-b8c5- a467ea7ffdbf | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | null | The keyword of the error. |
| level | String | null | The error level. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| path | String | /aso/psm/metrics/tr affic | The URL of the API. |
| serverRole | String | aso-mgr.asmgr# | The request ID. |
| responseVersi on | String | v1 | The version of the response format. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/psm/metrics/traffic HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "data":{
   "series":[
```

`{`

```json
     "data":[
      2.77,
      3.08,
      2.96,
      2.96,
      2.63
```

`],`

```json
     "name":"ifin_avg"
```

`}` `],`

```json
   "categories":[
    1638348780000,
    1638348840000,
    1638348900000,
    1638348960000,
    1638349020000
```

`]` `},`

```json
  "type":"TRAFFIC"
```

`},`

```json
 "level":"null",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/psm/metrics/traffic",
 "responseVersion":"v1",
 "requestId":"0067966f-d480-4628-b8c5-a467ea7ffdbf",
 "success":true,
 "errorTitle":"Service error",
 "key":"null"
```

`}`

#### 7.1.2 Inventory management

##### 7.1.2.1 GetOverview

Queries the inventory overview.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request headers.

**Syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOverview HTTP/1.1
```

**Request parameters**

None

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned code. 200 indicates that the call was successful. |
| cost | Long | 30 | The time spent on querying the inventory information. Unit: milliseconds. |
| data | Struct |   | The returned data. |
| ecs | Array of ecs |   | The Elastic Compute Service (ECS) inventory information. |
| flavors | Array of JSONArray |   | The list of ECS instance specifications. |
| flavor | String | ecs.sn1ne.8xlarge | The ECS instance specification. |
| soldAmount | Integer | 3 | The number of sold resources. |
| totalAmount | Integer | 8 | The number of total resources. |
| vendibleAmou nt | Integer | 5 | The number of available resources. |
| zoneId | Integer | 132 | The ID of the region. |
| zoneName | String | ECS-XX-XX-XX-X | The name of the region. |
| nas | Struct |   | The Apsara File Storage NAS (NAS) inventory information. |

| clusters | Map | {"StandardNasClus ter-XX-XX-XX": {"disk usage":"9.3 _ 00003","disk used" _ :"13250.83","disk t _ otal":"142482.0","d isk remain":"1292 _ 31.17"}} | The information about the cluster. |
|---|---|---|---|
| oss | Struct |   | The Object Storage Service (OSS) inventory information. |
| overview | Struct |   | The inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 945318.56 | The free space of the disk. |
| disk total _ | Float | 1064488 | The total capacity of the disk. |
| disk usage _ | Float | 11.195 | The usage of the disk in percentage. |
| disk used _ | Float | 119169.43 | The used space of the disk. |
| ots | Struct |   | The Tablestore inventory information. |
| overview | Struct |   | The inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 347621.84 | The free space of the disk. |
| disk total _ | Float | 389886 | The total capacity of the disk. |
| disk usage _ | Float | 10.840136 | The usage of the disk in percentage. |
| disk used _ | Float | 42264.17 | The used space of the disk. |
| rds | Struct |   | The ApsaraDB RDS inventory information. |

| engines | Map | {"hawq": {"mem used":"0.0 _ ","cpu used":"0.0", _ "mem usage":"0.0 _ ","disk total":"0.0", _ "disk used":"0.0"," _ disk remain":"0.0", _ "cpu remain":"0.0" _ ,"disk usage":"0.0", _ "mem remain":"0. _ 0","cpu total":"0.0" _ ,"cpu usage":"0.0", _ "mem total":"0.0"} _ } | The information about ApsaraDB RDS inventory on each engine. |
|---|---|---|---|
| overview | Struct |   | The information about the total ApsaraDB RDS inventory. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 55302 | The free space of the disk. |
| disk total _ | Float | 82826 | The total capacity of the disk. |
| disk usage _ | Float | 33.23232 | The usage of the disk in percentage. |
| disk used _ | Float | 27525 | The used space of the disk. |
| slb | Map | {"INTERNET": {"ip usage":"8.984 _ 375","ip used":"23 _ ","ip remain":"233" _ ,"ip total":"256","ty _ pe":"INTERNET"},"I NTRANET": {"ip usage":"14.33 _ 59375","ip used":" _ 367","ip remain":" _ 2193","ip total":"2 _ 560","type":"INTRA NET"}} | The Server Load Balancer (SLB) inventory information. |
| sls | Struct |   | The Log Service inventory information. |
| overview | Struct |   | The inventory information. |
| cluster | String | "" | The information about the cluster. |
| disk remain _ | Float | 245040.0 | The free space of the disk. |

| disk total _ | Float | 266122.0 | The total capacity of the disk. |
|---|---|---|---|
| disk usage _ | Float | 7.9219303 | The usage of the disk in percentage. |
| disk used _ | Float | 21082.0 | The used space of the disk. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| message | String | success | The error message. |
| requestId | String | c6cb0637-40a1- 4ac0-abe7- ad45efc848ac | The ID of the request. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOverview HTTP/1.1 OpsProduct: ASOOps
```

Sample success responses `JSON` format `{`

```json
    "successResponse": "true",
    "code": "200",
    "cost": "30",
    "data": {
        "slb": "{\"INTERNET\":
{\"ip_usage\":\"8.984375\",\"ip_used\":\"23\",\"ip_remain\":\"233\",\"ip_total\":\"256\", type\":\"INTERNET\"},\"INTRANET\": {\"ip_usage\":\"14.3359375\",\"ip_used\":\"367\",\"ip_remain\":\"2193\",\"ip_total\":\"25 \",\"type\":\"INTRANET\"}}",
        "ecs": [
```

`{`

```json
                "zoneId": "132",
                "zoneName": "ECS-XX-XX-XX-X",
                "flavors": [
```

`{`

```json
                        "flavor": "ecs.sn1ne.8xlarge",
"ttlA
```

`t"`

```
"8"
```

```json
                        "totalAmount": "8",
                        "vendibleAmount": "5",
                        "soldAmount": "3"
```

`}` `]` `}` `],`

```json
        "rds": {
            "engines": "{\"hawq\":
{\"mem_used\":\"0.0\",\"cpu_used\":\"0.0\",\"mem_usage\":\"0.0\",\"disk_total\":\"0.0\",\ isk_used\":\"0.0\",\"disk_remain\":\"0.0\",\"cpu_remain\":\"0.0\",\"disk_usage\":\"0.0\", mem_remain\":\"0.0\",\"cpu_total\":\"0.0\",\"cpu_usage\":\"0.0\",\"mem_total\":\"0.0\"}}"
            "overview": {
                "cluster": "\"\"",
                "disk_used": "27525",
                "disk_total": "82826",
                "disk_remain": "55302",
                "disk_usage": "33.23232"
```

`}` `},`

```json
        "sls": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "21082.0",
                "disk_total": "266122.0",
                "disk_remain": "245040.0",
                "disk_usage": "7.9219303"
```

`}` `},`

```json
        "ots": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "42264.17",
                "disk_total": "389886",
                "disk_remain": "347621.84",
                "disk_usage": "10.840136"
```

`}` `},`

```json
        "nas": {
            "clusters": "{\"StandardNasCluster-XX-XX-XX\":
{\"disk_usage\":\"9.300003\",\"disk_used\":\"13250.83\",\"disk_total\":\"142482.0\",\"dis remain\":\"129231.17\"}}"
```

`},`

```json
        "oss": {
            "overview": {
                "cluster": "\"\"",
                "disk_used": "119169.43",
                "disk_total": "1064488",
                "disk_remain": "945318.56",
                "disk_usage": "11.195"
```

`}` `}` `},`

```json
"level":"\"\""
```

```
    level: \\
```

`,`

```json
    "requestId": "c6cb0637-40a1-4ac0-abe7-ad45efc848ac",
    "message": "success",
    "key": "\"\""
```

`}`

##### 7.1.2.2 GetSlbInventoryInfo

Query the inventory information of Server Load Balancer (SLB).

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getSlbInventoryInfo HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
|---|---|---|---|
| errorMessage | String | System error | The error message. |
| data | Map | {"INTERNET": {"ip usage":"5.078 _ 125","ip used":"26 _ ","ip remain":"486" _ ,"ip total":"512","ty _ pe":"INTERNET"},"I NTRANET": {"ip usage":"22.97 _ 3633","ip used":"9 _ 41","ip remain":"3 _ 155","ip total":"40 _ 96","type":"INTRAN ET"}} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | 56bb6208-89f0- 4b62-a2e6- 5204db52fcf5 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |

| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
|---|---|---|---|
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getSlbInvento ryInfo | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getSlbInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "INTERNET":{
   "ip_usage":"5.078125",
   "ip_total":"512",
   "ip_used":"26",
   "ip_remain":"486",
   "type":"INTERNET"
```

`},`

```json
  "INTRANET":{
   "ip_usage":"22.973633",
   "ip_total":"4096",
   "ip_used":"941",
   "ip_remain":"3155",
   "type":"INTRANET"
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getSlbInventoryInfo",
 "responseVersion":"v1",
 "requestId":"56bb6208-89f0-4b62-a2e6-5204db52fcf5",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}` ASO 2022-01-18

##### 7.1.2.3 GetEcsInventoryByCurrent

Queries the current CPU and memory information of an Elastic Compute Service (ECS) instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryByCurrent HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"ECS-XXXX-X- XXXX-X": {"mem used":"0.0 _ ","cpu used":"0.0", _ "mem usage":"0.0 _ ","cpu remain":"56 _ 0.0","mem remain _ ":"2240.0","cpu tot _ al":"560.0","cpu us _ age":"0.0","mem t _ otal":"2240.0"},"EC S-XXX-X-XXXX-X": {"mem used":"656 _ .0","cpu used":"29 _ 2.0","mem usage": _ "47.67","cpu remai _ n":"52.0","mem re _ main":"720.0","cpu total":"344.0","cp _ u usage":"84.88"," _ mem total":"1376. _ 0"},"ECS-XXX-X- XXXX-X": {"mem used":"384 _ .0","cpu used":"96. _ 0","mem usage":" _ 25.0","cpu remain" _ :"288.0","mem re _ main":"1152.0","cp u total":"384.0","c _ pu usage":"25.0"," _ mem total":"1536. _ 0"}} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | 04a9613b-8e04- 475a-b028- ac66019edc91 | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| path | String | /aso/inventory/ope napi/getEcsInvento ryByCurrent | The URL of the API. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryByCurrent HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "ECS-XXX-X-XXXX-X":{
   "mem_used":"384.0",
   "cpu_used":"96.0",
   "mem_usage":"25.0",
   "cpu_remain":"288.0",
   "mem_remain":"1152.0",
   "cpu_total":"384.0",
   "cpu_usage":"25.0",
   "mem_total":"1536.0"
```

`},`

```json
  "ECS-XXXX-X-XXXX-X":{
   "mem_used":"0.0",
   "cpu_used":"0.0",
   "mem_usage":"0.0",
   "cpu_remain":"560.0",
   "mem_remain":"2240.0",
   "cpu_total":"560.0",
   "cpu_usage":"0.0",
   "mem_total":"2240.0"
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getEcsInventoryByCurrent",
 "responseVersion":"v1",
 "requestId":"04a9613b-8e04-475a-b028-ac66019edc91",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.4 GetEcsInventoryList

Queries the inventory information of Elastic Compute Service (ECS).

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryList HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Array of JSONArray |   | The response. |
| zoneId | Integer | 131 | The zone ID. |
| zoneName | String | ECS-XX-XX-XX | The zone name. |
| flavors | Array of JSONArray |   | The list of ECS instance types. |
| flavor | String | ecs.mn4v2.2xlarge | The type of the ECS instance. |
| totalAmount | Integer | 48 | The total number of ECS instances. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| soldAmount | Integer | 4 | The number of sold ECS instances. |
| vendibleAmou nt | Integer | 44 | The number of available ECS instances. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | 8d526115-1347- 4fba-8d48- 6fe267701983 | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getEcsInvento ryList | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "flavors":{
   "flavor":"ecs.mn4v2.2xlarge",
   "totalAmount":48,
   "vendibleAmount":44,
   "soldAmount":4
```

`},`

```json
  "zoneId":131,
  "zoneName":"ECS-XX-XX-XX "
```

`},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getEcsInventoryList",
 "responseVersion":"v1",
 "requestId":"8d526115-1347-4fba-8d48-6fe267701983",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.5 GetEcsInventoryByZoneId

Queries the inventory information of Elastic Compute Service (ECS) based on zone IDs.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryByZoneId HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| zoneId | Strin g | Query | Yes | 133 | The zone ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | Service error | The title of the error message. |
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| requestId | String | fa07ab18-06cf- 470f-9417- c6ae644bbe2c | The request ID. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| path | String | /aso/inventory/ope napi/getEcsInvento ryByZoneId | The URL of the API. |
| key | String | "" | The keyword of the error. |
| data | Array of data |   | The response. |
| zoneId | String | 133 | The zone ID. |
| zoneName | String | ECS-XXX-X-XXXX-X | The zone name. |
| flavors | Array of flavors |   | The list of ECS instance types. |
| flavor | String | ecs.XXX.XXX | The type of the ECS instance. |
| totalAmount | Integer | 1 | The total number of ECS instances. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| soldAmount | Integer | 0 | The number of sold ECS instances. |
| vendibleAmou nt | Integer | 1 | The number of available ECS instances. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getEcsInventoryByZoneId HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":30,
 "data":{
  "flavors":{
   "flavor":"ecs.XXX.XXX ",
   "totalAmount":1,
   "vendibleAmount":1,
   "soldAmount":0
```

`},`

```json
  "zoneId":"133",
  "zoneName":"ECS-XXX-X-XXXX-X"
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "serverRole":"aso-mgr.asmgr#",
 "successResponse":true,
 "path":"/aso/inventory/openapi/getEcsInventoryByZoneId",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"fa07ab18-06cf-470f-9417-c6ae644bbe2c",
 "key":"\"\""
```

`}`

##### 7.1.2.6 GetVms

Queries the information about Elastic Compute Service (ECS) instances. You can call this operation once per second.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/api-adapter/ecs/getVms HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| region | Strin g | Query | Yes | cn-env-XXX-XXX | The region ID. |
| instanceId s | Strin g | Query | No | i- 3ar015df5d2dagqh****,i -3ar00ogdk61lnsgl**** | The IDs of the ECS instances. You can enter multiple IDs and separate them with commas (,). |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| status | Strin g | Query | No | Running | The status of the instance. Valid values: Running: The instance is running. Shutted: The instance is stopped. Pending: The instance is to be started. Starting: The instance is being started. Shutting: The instance is being stopped. Resetting: The instance is being reset. StartFailure: The startup failed. ShutFailure: The stop failed. ResetFailure: The reset failed. |
| pageNum ber | Integ er | Query | No | 1 | The page number. Default value: 1. |
| pageSize | Integ er | Query | No | 10 | The number of entries per page. Default value: 10. Maximum value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| items | Array of items |   | The ECS instance information. |
| regionId | String | cn-env-XXX-XXX | The region ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| zoneId | String | cn-env-XXX-XXX- XXX | The zone ID. |
| clusterId | String | ECS-XXX-XXX-XXX- XXX | The cluster ID. |
| instanceId | String | i- 3ar015df5d2dagqh **** | The instance ID. |
| instanceName | String | test name _ | The instance name. |
| status | String | Running | The status of the instance. Valid values: Running: The instance is running. Shutted: The instance is stopped. Pending: The instance is to be started. Starting: The instance is being started. Shutting: The instance is being stopped. Resetting: The instance is being reset. StartFailure: The startup failed. ShutFailure: The stop failed. ResetFailure: The reset failed. |
| requestId | String | A701B38D-DD64- 4D84-8E39- 1E035664C87E | The request ID. |
| pageNumber | Integer | 1 | The page number. |
| pageSize | Integer | 10 | The number of entries per page. |
| totalCount | Integer | 1 | The total number of entries returned. |
| cost | Long | 1200 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 6878ff2c-93c7- 4356-8a8c- c6296a3d5ef9 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/api- adapter/ecs/opena pi/getVms | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/api-adapter/ecs/getVms HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":1200,
 "code":"200",
 "data":{
  "pageNumber":1,
  "requestId":"A701B38D-DD64-4D84-8E39-1E035664C87E",
  "pageSize":10,
  "totalCount":1,
  "items":{
   "instanceId":"i-3ar015df5d2dagqh****",
   "regionId":"cn-env-XXX-XXX",
   "instanceName":"test_name",
   "zoneId":"cn-env-XXX-XXX-XXX",
   "clusterId":"ECS-XXX-XXX-XXX-XXX",
   "status":"Running"
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/api-adapter/ecs/openapi/getVms",
 "responseVersion":"v1",
 "requestId":"6878ff2c-93c7-4356-8a8c-c6296a3d5ef9",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.7 GetEbsClusterTypeInfo

Queries the inventory information of Elastic Block Storage (EBS).

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/pgmon/queryEbsClusterTypeInventory HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Map | {"EbsBlockSsdClus ter": [{"cluster":"ECS- XX-XX- XX","freeSize":"283 45.57","totalSize":" 28391.00","modify Date":"165021078 0000","project":"ec s","id":"23233","re gion":"cn-XX-XX- XX","userdSize":"4 5.43","usedSpaceP ercent":"0.16"}]} | The response. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | b2f7e0c7-ea6f- 4282-bf87- 9ad4aa4d9760 | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/pgm on/openapi/queryE bsClusterTypeInve ntory | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/pgmon/queryEbsClusterTypeInventory HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "EbsBlockSsdCluster":[
```

`{`

```json
    "cluster":"ECS-XX-XX-XX",
    "freeSize":"28345.57",
    "totalSize":"28391.00",
    "modifyDate":"1650210780000",
    "project":"ecs",
    "id":"23233",
    "region":"cn-XX-XX-XX",
    "userdSize":"45.43",
    "usedSpacePercent":"0.16"
```

`}` `]` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/pgmon/openapi/queryEbsClusterTypeInventory",
 "responseVersion":"v1",
 "requestId":"b2f7e0c7-ea6f-4282-bf87-9ad4aa4d9760",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.8 GetNasInventoryInfo

Queries the inventory information of Apsara File Storage NAS.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getNasInventoryInfo HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| clusters | Map | {"StandardNasClus te r-XX-XX-XX": {"disk usage":"9.3 _ 00 003","disk used":" _ 1 3250.83","disk tota _ l ":"142482.0","disk _ r emain":"129231.17 "} } | The cluster information. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | adb1a2e2-ccea- 4701-ac0b- cb1fe6034c17 | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getNasInvento ryInfo | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getNasInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "clusters":{
   "StandardNasCluster-XX-XX-XX":{
    "disk_used":"13250.83",
    "disk_remain":"129231.17",
    "disk_usage":"9.300003",
    "disk_total":"142482.0"
```

`}` `}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getNasInventoryInfo",
 "responseVersion":"v1",
 "requestId":"adb1a2e2-ccea-4701-ac0b-cb1fe6034c17",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.9 GetOssInventoryInfo

Queries the inventory information of Object Storage Service (OSS).

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOssInventoryInfo HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| overview | Struct |   | The OSS inventory information. |
| disk total _ | Float | 119169.43 | The total capacity of the disk. |
| disk used _ | Float | 119169.43 | The used space of the disk. |
| disk remain _ | Float | 945318.56 | The free space of the disk. |
| disk usage _ | Float | 945318.56 | The disk utilization. |
| cluster | String | "" | The cluster information. |
| cost | Long | 30 | The response time. Unit: milliseconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the call was successful. Valid values: true. false. |
| requestId | String | 9ac36287-3ba4- 4f94-a7de- ac14e91d0c1c | The request ID. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getOssInvento ryInfo | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the call was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOssInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "overview":{
   "cluster":"\"\"",
   "disk_total":119169.43,
   "disk_used":119169.43,
   "disk_remain":945318.56,
   "disk_usage":945318.56
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getOssInventoryInfo",
 "responseVersion":"v1",
 "requestId":"9ac36287-3ba4-4f94-a7deac14e91d0c1c",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.10 GetOtsInnerInventoryInfo

Queries the inventory information of Tablestore.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getOtsInnerInventoryInfo HTTP/1.
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| overview | Struct |   | The Tablestore inventory information. |
| disk total _ | Float | 389886 | The total capacity of the disk. |
| disk used _ | Float | 347621.84 | The used space of the disk. |
| disk remain _ | Float | 347621.84 | The free space of the disk. |
| disk usage _ | Float | 10.840136 | The disk utilization. |
| cluster | String | "" | The cluster information. |
| cost | Long | 30 | The response time. Unit: milliseconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | 466f9e0f-d0a8- 4290-860b- dda9f792e438 | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getOtsInnerIn ventoryInfo | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getOtsInnerInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "overview":{
   "cluster":"\"\"",
   "disk_total":389886.0,
   "disk_used":347621.84,
   "disk_remain":347621.84,
   "disk_usage":10.840136
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getOtsInnerInventoryInfo",
 "responseVersion":"v1",
 "requestId":"466f9e0f-d0a8-4290-860b-dda9f792e438",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.11 GetRdsInventoryInfo

Queries the inventory information of ApsaraDB RDS.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getRdsInventoryInfo HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| overview | Struct |   | The information about the ApsaraDB RDS inventory. |
| cpu total _ | Float | 1.0 | The total CPU capacity. |
| cpu used _ | Float | 0 | The used CPU capacity. |
| cpu remain _ | Float | 1.0 | The available CPU capacity. |
| cpu usage _ | Float | 0 | The CPU utilization. |
| mem total _ | Float | 200.0 | The total amount of memory. |
| mem used _ | Float | 100.0 | The amount of used memory. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| mem remain _ | Float | 100.0 | The amount of available memory. |
| mem usage _ | Float | 50.0 | The memory utilization. |
| disk total _ | Float | 82826 | The total capacity of the disk. |
| disk used _ | Float | 27525 | The used space of the disk. |
| disk remain _ | Float | 55302 | The free space of the disk. |
| disk usage _ | Float | 33.23232 | The disk utilization. |
| engines | Map | {"hawq": {"mem used":"0.0 _ ","cpu used":"0.0", _ "mem usage":"0.0 _ ","disk total":"0.0", _ "disk used":"0.0"," _ disk remain":"0.0", _ "cpu remain":"0.0" _ ,"disk usage":"0.0", _ "mem remain":"0. _ 0","cpu total":"0.0" _ ,"cpu usage":"0.0", _ "mem total":"0.0"} _ } | The details of the ApsaraDB RDS inventory. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | c6cb0637-40a1- 4ac0-abe7- ad45efc848ac | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getRdsInvento ryInfo | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getRdsInventoryInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "overview":{
   "mem_used":100.0,
   "cpu_used":0.0,
   "mem_usage":50.0,
   "disk_total":82826.0,
   "disk_used":27525.0,
   "disk_remain":55302.0,
   "cpu_remain":1.0,
   "mem_remain":100.0,
   "disk_usage":33.23232,
   "cpu_total":1.0,
   "cpu_usage":0.0,
   "mem_total":200.0
```

`},`

```json
  "engines":{
   "hawq":{
    "mem_used":"0.0",
    "cpu_used":"0.0",
    "mem_usage":"0.0",
    "disk_total":"0.0",
    "disk_used":"0.0",
    "disk_remain":"0.0",
    "cpu_remain":"0.0",
    "disk_usage":"0.0",
    "mem_remain":"0.0",
    "cpu_total":"0.0",
    "cpu_usage":"0.0",
    "mem_total":"0.0"
```

`}` `}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getRdsInventoryInfo",
 "responseVersion":"v1",
 "requestId":"c6cb0637-40a1-4ac0-abe7-ad45efc848ac",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.12 GetSlsInnerInfo

Queries the inventory information of Log Service.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getSlsInnerInfo HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| overview | Struct |   | The information overview. |
| disk total _ | Float | 266122 | The total capacity of the disk. |
| disk used _ | Float | 21082 | The used space of the disk. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| disk remain _ | Float | 245040 | The free space of the disk. |
| disk usage _ | Float | 7.9219303 | The disk utilization. |
| cluster | String | "" | The cluster information. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | aae56eb7-74db- 423b-b563- 18ffd8f249ed | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | so-mgr.asmgr# | The service role. |
| path | String | /aso/inventory/ope napi/getSlsInnerInf o | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getSlsInnerInfo HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "overview":{
   "cluster":"\"\"",
   "disk_total":266122.0,
   "disk_used":21082.0,
   "disk_remain":245040.0,
   "disk_usage":7.9219303
```

`}` `},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"so-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getSlsInnerInfo",
 "responseVersion":"v1",
 "requestId":"aae56eb7-74db-423b-b563-18ffd8f249ed",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.13 GetPanguInventoryByClusterName

Queries the inventory information of Apsara Distributed File System based on cluster names.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/openapi/getPanguInventoryByClusterName HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| clusterNa me | Strin g | Query | Yes | ECS-XXX-X-XXXX | The cluster name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| requestId | String | 2740eec5-a674- 4651-b959- 9f24e71ab2ba | The request ID. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|
| Parameter | Type | Example | Description |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| path | String | /aso/inventory/ope napi/getPanguInve ntoryByClusterNam e | The URL of the API. |
| data | Array of data |   | The response. |
| modifyDate | Long | 1657295602000 | The latest modification time of the inventory information. |
| regionId | String | "" | The region ID. |
| id | Long | 91 | The record ID. You can ignore this parameter. |
| project | String | aso | The product name. |
| cluster | String | ECS-XXX-X-XXXX | The cluster name. |
| region | String | cn-XXXX-XXXX-XX | The region ID. |
| totalSize | String | 249478 | The total capacity of the disk. |
| usedSpacePer cent | String | 0.0000 | The disk utilization. |
| userdSize | String | 0.0000 | The used space of the disk. |
| freeSize | String | 249478.0000 | The free space of the disk. |
| key | String | "" | The keyword of the error. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/openapi/getPanguInventoryByClusterName HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":30,
 "data":{
  "cluster":"ECS-XXX-X-XXXX",
  "totalSize":"249478",
  "freeSize":"249478.0000",
  "modifyDate":1657295602000,
  "regionId":"\"\"",
  "project":"aso",
  "id":91,
  "region":"cn-XXXX-XXXX-XX ",
  "userdSize":"0.0000",
  "usedSpacePercent":"0.0000"
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/openapi/getPanguInventoryByClusterName",
 "responseVersion":"v1",
 "requestId":"2740eec5-a674-4651-b959-9f24e71ab2ba",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.14 GetInventoryStat

Queries the inventory information of Server Load Balancer (SLB).

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/inventory/slb/stat HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| label | Strin g | Query | No | default | The tag of the SLB cluster. |
| clusterNa me | Strin g | Query | No | slbCluster-XXXXX-XXXX | The cluster name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| requestId | String | 82ecd983-62d8- 4be4-8d87- 1957cd09b796 | The request ID. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| path | String | /aso/inventory/slb/ openapi/stat | The URL of the API. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| data | Array of data |   | The response. |
| modifyDate | Long | 1660780800000 | The last modification time of the inventory information. |
| regionId | String | cn-XXXX-XXXX-XX | The region ID. |
| id | Integer | 84 | The primary key ID. |
| type | String | INTRANET | The network type. |
| assignedCount | Integer | 628 | The number of assigned SLB instances. |
| frozenCount | Integer | 3468 | The number of frozen SLB instances. |
| releasedCount | Integer | 0 | The number of released SLB instances. |
| protectedCoun t | Integer | 0 | The number of protected SLB instances. |
| label | String | default | The tag of the SLB cluster. |
| suName | String | su 0 _ | The SU name. |
| ppoName | String | proxy XXX XXX 1 _ _ _ | The PPO name. |
| zoneId | String | cn-XXXX-XXXX- amtest1XXXX-X | The zone ID. |
| key | String | "" | The keyword of the error. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/slb/stat HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":30,
 "data":{
  "protectedCount":0,
  "frozenCount":3468,
  "ppoName":"proxy_XXX_XXX_1",
  "modifyDate":1660780800000,
  "regionId":"cn-XXXX-XXXX-XX",
  "releasedCount":0,
  "assignedCount":628,
  "zoneId":"cn-XXXX-XXXX-amtest1XXXX-X",
  "id":84,
  "label":"default",
  "type":"INTRANET",
  "suName":"su_0"
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/slb/openapi/stat",
 "responseVersion":"v1",
 "requestId":"82ecd983-62d8-4be4-8d87-1957cd09b796",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.2.15 GetIntegratedProductInventory

Queries the capacity information of a cloud service.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| region | Strin g | Quer y | No | cn-XX-XX-XX | The region. |

| paged | Bool ean | Quer y | No | true | Specifies whether to paginate the responses of this operation. Default value: true. |
|---|---|---|---|---|---|
| pageSize | Integ er | Quer y | No | 20 | The number of entries per page. |
| product | Strin g | Quer y | Yes | oss | The code of the cloud service. ecs ebs oss nas ots sls slb rds |
| dimension | Strin g | Quer y | No | sale | The query dimension. Only the sale dimension is supported. |
| cluster | Strin g | Quer y | No | OssHybridCluster-A-XX- XX | The logical cluster of the cloud service. |
| pageIndex | Integ er | Quer y | No | 1 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. Valid values: true false |
| cost | Long | 22 | The response time. Unit: milliseconds. |
| path | String | /aso/inventory/inte grate/presentDetail | The request path. |

| serverRole | String | aso-mgr.asmgr# | The server role. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The title of the error message. |
| errorMessage | String | "" | The error message. |
| requestId | String | 0ab408921688116 7637553107d0045 | The request ID. |
| eagleEyeTrace Id | String | 0ab408921688116 7637553107d0045 | The EagleEye ID. |
| data | Struct |   | The response data. |
| -list | Array |   | The returned data. |
| --regionId | String | cn-XX-XX-XX | The region. |
| --cluster | String | OssHybridCluster- A-XX-XX | The cluster name. |
| --dimension | String | sale | The dimension. For more information, see the Supplementary details on GetIntegratedProductInventory. |
| -- dimensionValu e | String | flavor | The sub-dimension. For more information, see the Supplementary details on GetIntegratedProductInventory. |
| --metric | String | disk type _ | The metric. |
| --metricValue | String | default | The value of the metric. |
| --unit | String | GB | The unit of the metric. |
| --total | Integer | 128778 | The total capacity. |

| --used | Integer | 58142 | The used capacity. |
|---|---|---|---|
| --free | Integer | 70635 | The remaining capacity. |
| --usage | Integer | 45 | The usage. For example, a value of 45 indicates that the utilization is 45%. |
| -pageInfo | Struct |   | The pagination information. |
| --currentPage | Integer | 1 | The page number. |
| --pageSize | Integer | 20 | The number of entries per page. |
| --total | Long | 30 | The total number of entries returned. |
| --totalPage | Long | 2 | The total number of pages returned. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inventory/integrate/presentDetail HTTP/1.1 &product=oss &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/inventory/integrate/presentDetail",
 "eagleEyeTraceId":"0ab4089216881167637553107d0045",
 "cost":22,
 "responseVersion":"v1",
 "data":{
  "pageInfo":{
   "total":30,
   "totalPage":2,
   "pageSize":20,
   "currentPage":1
```

`},`

```json
  "list":{
   "cluster":"OssHybridCluster-A-XX-XX",
   "unit":"GB",
   "total":128778,
   "dimensionValue":"flavor",
   "regionId":"cn-XX-XX-XX",
   "metric":"disk_type",
   "usage":45,
   "metricValue":"default",
   "used":58142,
   "free":70635,
   "dimension":"sale"
```

`}` `},`

```json
 "success":true,
 "errorTitle":"\"\"",
 "requestId":"0ab4089216881167637553107d0045",
 "errorMessage":"\"\"",
 "errorCode":"\"\""
```

`}`

###### 7.1.2.15.1 Supplementary details on GetIntegratedProductInventory

##### GetIntegratedProductInventory

This topic provides supplementary details on the request and response parameters of the `GetIntegratedProductInventory` operation.

| Request parameters | Response parameters |   |   |   |   |
|---|---|---|---|---|---|
| Service code | Dimension | Dimension value | Unit | Metric | Metric value |

| ecs | sale - service logical capacity | flavor - capacity | Core | cpu type _ | share: shared ECS instance. exclude: dedicated ECS instance. bareMetal: ECS bare metal instance. default: unknown. |
|---|---|---|---|---|---|
|   | sale - service logical capacity | flavor - capacity | GB | mem type _ | default: the default value, which is of a non-enumeration type. |
| ebs | sale - service logical capacity | flavor - capacity | GB | disk type _ | The valid values are the specifications supported by Elastic Block Storage (EBS). Examples: IO7, IO8, IO15, and IO16. |
| oss | sale - service logical capacity | flavor - capacity | GB | disk type _ | HYBRID: hybrid flash storage. SSD: all-flash storage. |
| nas | sale - service logical capacity | flavor - capacity | GB | disk type _ | HYBRID: hybrid flash storage. SSD: all-flash storage. |
| ots | sale - service logical capacity | flavor - capacity | GB | disk type _ | HYBRID: hybrid flash storage. SSD: all-flash storage. |

| sls | sale - service logical capacity | flavor - capacity | GB | disk type _ | HYBRID: hybrid flash storage. SSD: all-flash storage. |
|---|---|---|---|---|---|
| slb | sale - service logical capacity | flavor - capacity | N/A | internet | default: the default value, which is of a non-enumeration type. |
|   |   |   | N/A | intranet | default: the default value, which is of a non-enumeration type. |
| rds | sale - service logical capacity | The instance engine. Valid values: redis pgsql mongodb mysql gpdb ppassql hbase mssql | Core | cpu type _ | blank: empty host. share: shared ECS instance. exclude: dedicated ECS instance. |
|   |   |   | GB | mem type _ |   |
|   |   |   | GB | disk type _ |   |

#### 7.1.3 Inspections

##### 7.1.3.1 InspectionGetTaskList

Queries inspection scenarios.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Hea der | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| aliyun terr _ itory | Strin g | Hea der | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |
|---|---|---|---|---|---|

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Quer y | No | 15 | The number of entries per page. |
| page | Integ er | Quer y | No | 1 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. true false |
| cost | Long | 74 | The response time. Unit: milliseconds. |
| path | String | /aso/inspection/so mepath | The request path. |
| serverRole | String | inspection# | The server role. |
| responseVersi on | String | v1 | The version of the response. |
| errorCode | String | "" | The error code. |

| errorTitle | String | "" | The title of the error message. |
|---|---|---|---|
| errorMessage | String | "" | The error message. |
| requestId | String | 8ae2a476-52b1- 4bac-98c4- 4ca17671482a | The request ID. |
| eagleEyeTrace Id | String | "" | The EagleEye ID. |
| data | Struct |   | The response data. |
| -objectList | Array |   | The queried inspection scenarios. |
| -- inspectionItem s | Array |   | The inspection items. |
| ---id | Long | 10001 | The inspection item ID. |
| --- inspectionCate goryId | Long | 10001 | The ID of the inspection item category. |
| ---name | String | Network inspection | The name of the inspection item. |
| ---description | String | Network inspection | The description of the inspection item. |
| ---preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ---capabilityId | Long | 1 | The ID of the atomic capability. |
| --- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |

| ---active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
|---|---|---|---|
| --- atomCapabilit y | Struct |   | The information about the atomic capability. |
| ----id | Long | 1 | The ID of the atomic capability. |
| ----name | String | Network inspection | The name of the atomic capability. |
| ----description | String | Network inspection | The description of the atomic capability. |
| ----preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ---- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ---- capabilityType Name | String | Script | The name of the atomic capability category. |
| ----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ----content | Map | {"":""} | The parameters of the atomic capability. |
| --- executionResu lt | Struct |   | The execution result of the inspection item. |
| ---- dimensionTitle s | String | "" | The dimensions of the inspection item. |

| ---- checkResults | Array |   | The details of the inspection result. |
|---|---|---|---|
| -----dimensions | String | "" | The returned values of the dimensions. |
| -----id | Long | 1 | The ID of the dimension entry. |
| ----- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ----- checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| -----description | String | Inspection succeeded | The description of the inspection result. |
| -----detail | String | Inspection succeeded | The details of the inspection result. |
| ----id | Long | 1 | The ID of the execution result. |
| ----capabilityId | Long | 1 | The ID of the atomic capability. |
| ----param | Map | {"":""} | The parameters of the atomic capability. |
| ----status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ----message | String | Inspection succeeded | The message that indicates the inspection result. |
| ----extraInfo | String | Inspection succeeded | The details of the inspection result. |

| ---- checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
|---|---|---|---|
| ----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ---- executionType | Integer | 0 | The execution type. |
| ---- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| ----configId | Long | 1 | The configuration ID. |
| ----capability | Struct |   | The information about the atomic capability. |
| -----id | Long | 1 | The ID of the atomic capability. |
| -----name | String | Network inspection | The name of the atomic capability. |
| -----description | String | Network inspection | The description of the atomic capability. |
| -----preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ----- capabilityType | Integer | 1 | The ID of the atomic capability category. |

| ----- capabilityType Name | String | Script | The name of the atomic capability category. |
|---|---|---|---|
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -----content | Map | {"":""} | The parameters of the atomic capability. |
| ----statistics | Struct |   | The statistics of inspection items. |
| ----- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ----- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ----- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ----- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ----- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were executed successfully. |
| ----- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ----- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ----- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |

| ----- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
|---|---|---|---|
| ----- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ----- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ----- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ----- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ----- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| --schedules | Array |   | The configuration for scheduled inspection items. |
| ---weekDays | Integer | 1 | The day of the week to execute the inspection item. |
| ---timeStr | String | 12:01:26 | The time to execute the inspection item. |
| -- inspectionCate gories | Array |   | The information about the inspection category. |
| --- subCategories | Array |   | The information about the inspection sub- category. |
| ---- inspectionItem s | Array |   | The inspection items. |
| -----id | Long | 1 | The inspection item ID. |

| ----- inspectionCate goryId | Long | 1 | The ID of the inspection item category. |
|---|---|---|---|
| -----name | String | Network inspection | The name of the inspection item. |
| -----description | String | Network inspection | The description of the inspection item. |
| -----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| ----- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ----- atomCapabilit y | Struct |   | The information about the atomic capability. |
| ------id | Long | 1 | The ID of the atomic capability. |
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |

| ------ capabilityType Name | String | Script | The name of the atomic capability category. |
|---|---|---|---|
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| ----- executionResu lt | Struct |   | The execution result of the inspection item. |
| ------ dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ------ checkResults | Array |   | The details of the inspection result. |
| ------- dimensions | String | "" | The returned values of the dimensions. |
| -------id | Long | 1 | The ID of the dimension entry. |
| ------- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------- checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| ------- description | String | Inspection succeeded | The description of the inspection result. |
| -------detail | String | Inspection succeeded | The details of the inspection result. |
| ------id | Long | 1 | The ID of the execution result. |

| ------ capabilityId | Long | 1 | The ID of the atomic capability. |
|---|---|---|---|
| ------param | Map | {"":""} | The parameters of the atomic capability. |
| ------status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ------message | String | Inspection succeeded | The message that indicates the inspection result. |
| ------extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ------ checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| ------startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ------endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ------ updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ------ executionType | Integer | 1 | The execution type. |
| ------ taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| ------configId | Long | 1 | The configuration ID. |

| ------capability | Struct |   | The information about the atomic capability. |
|---|---|---|---|
| -------id | Long | 1 | The ID of the atomic capability. |
| -------name | String | Network inspection | The name of the atomic capability. |
| ------- description | String | Network inspection | The description of the atomic capability. |
| -------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------- capabilityType Name | String | Script | The name of the atomic capability category. |
| -------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -------content | Map | {"":""} | The parameters of the atomic capability. |
| ------statistics | Struct |   | The statistics of inspection items. |
| ------- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ------- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |

| ------- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
|---|---|---|---|
| ------- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were executed successfully. |
| ------- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ----id | Long | 1 | The ID of the inspection item category. |
| ----name | String | Basic inspection | The name of the inspection category. |

| ----code | String | network | The code of the inspection category. |
|---|---|---|---|
| ----parentId | Long | 0 | The ID of the inspection item category. |
| ----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ---- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ---- checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| ----order | Integer | 0 | The order of inspection items. |
| ---- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ----- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ----- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ----- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |

| ----- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
|---|---|---|---|
| ----- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were executed successfully. |
| ----- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ----- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ----- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ----- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ----- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ----- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ----- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ----- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ----- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| --- inspectionItem s | Array |   | The inspection items. |

| ----id | Long | 10001 | The inspection item ID. |
|---|---|---|---|
| ---- inspectionCate goryId | Long | 10001 | The ID of the inspection item category. |
| ----name | String | Network inspection | The name of the inspection item. |
| ----description | String | Network inspection | The description of the inspection item. |
| ----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----capabilityId | Long | 1 | The ID of the atomic capability. |
| ---- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| ----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ---- atomCapabilit y | Struct |   | The information about the atomic capability. |
| -----id | Long | 1 | The ID of the atomic capability. |
| -----name | String | Network inspection | The name of the atomic capability. |
| -----description | String | Network inspection | The description of the atomic capability. |
| -----preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |

| ----- capabilityType | Integer | 1 | The ID of the atomic capability category. |
|---|---|---|---|
| ----- capabilityType Name | String | Script | The name of the atomic capability category. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -----content | Map | {"":""} | The parameters of the atomic capability. |
| ---- executionResu lt | Struct |   | The execution result of the inspection item. |
| ----- dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ----- checkResults | Array |   | The details of the inspection result. |
| ------ dimensions | String | "" | The returned values of the dimensions. |
| ------id | Long | 1 | The ID of the dimension entry. |
| ------ atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------ checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| ------ description | String | Inspection succeeded | The description of the inspection result. |
| ------detail | String | Inspection succeeded | The details of the inspection result. |

| -----id | Long | 1 | The ID of the execution result. |
|---|---|---|---|
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| -----param | Map | {"":""} | The parameters of the atomic capability. |
| -----status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| -----message | String | Inspection succeeded | The message that indicates the inspection result. |
| -----extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ----- checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| -----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----- updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ----- executionType | Integer | 0 | The execution type. |
| ----- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |

| -----configId | Long | 1 | The configuration ID. |
|---|---|---|---|
| -----capability | Struct |   | The information about the atomic capability. |
| ------id | Long | 1 | The ID of the atomic capability. |
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------ capabilityType Name | String | Script | The name of the atomic capability category. |
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| -----statistics | Struct |   | The statistics of inspection items. |
| ------ totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------ executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |

| ------ executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
|---|---|---|---|
| ------ executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------ executionSucc essItemsCount | Integer | 10 | The number of inspection items that were executed successfully. |
| ------ executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------ errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------ warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------ normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------ errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------ warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------ normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------ cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |

| ------ totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
|---|---|---|---|
| ---id | Long | 1 | The ID of the inspection item category. |
| ---name | String | Network inspection | The name of the inspection category. |
| ---code | String | network | The code of the inspection category. |
| ---parentId | Long | 0 | The ID of the inspection item category. |
| ---startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ---endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| --- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ---checkStatus | Integer | 0 | The inspection result. Valid values: 0: normal. 1: alerting. 2: error. |
| ---order | Integer | 0 | The order of inspection items. |
| --- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ---- totalItemsCou nt | Integer | 10 | The total number of inspection items. |

| ---- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
|---|---|---|---|
| ---- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ---- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ---- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were executed successfully. |
| ---- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ---- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ---- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ---- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ---- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ---- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ---- normalDetailC ount | Integer | 10 | The number of normal check items. |

| ---- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
|---|---|---|---|
| ---- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| -- inspectionItem sCount | Integer | 100 | The total number of inspection items. |
| --id | Long | 1 | The ID of the scenario. |
| --name | String | Network inspection | The name of the scenario. |
| --description | String | Network inspection | The description of the scenario. |
| --preinstall | Boolean | true | Indicates whether the scenario is preset. Valid values: true false |
| --active | Boolean | true | Indicates whether the scenario is activated. Valid values: true false |
| --createTime | String | 2023-07- 25T12:01:26.000+ 0000 | The time when the automatic snapshot policy was created. |
| -- createUserNa me | String | opsadmin | The username. |
| -- executionCoun t | Integer | 10 | The number of times an execution is performed. |
| --orders | Integer | 0 | The order of inspection scenarios. |
| -totalPage | Integer | 2 | The total number of pages returned. |

| -pageSize | Integer | 15 | The number of entries per page. |
|---|---|---|---|
| -total | Integer | 20 | The total number of entries. |
| -page | Integer | 1 | The page number. |

Sample requests

```
GET /openapi/popResource/aso/inspection/api/inspection/getTaskList HTTP/1.1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "serverRole":"inspection#",
 "path":"/aso/inspection/somepath",
 "eagleEyeTraceId":"\"\"",
 "cost":74,
 "responseVersion":"v1",
 "data":{
  "total":20,
  "totalPage":2,
  "pageSize":15,
  "page":1,
  "-objectList":{
   "preinstall":true,
   "description":"Network inspection",
   "active":true,
   "createUserName":"opsadmin",
   "inspectionCategories":{
    "checkStatus":0,
    "code":"network",
    "executionStatus":0,
    "name":"Network inspection",
    "inspectionItemStatistics":{
     "totalItemsCount":10,
     "totalDetailCount":10,
     "executionSkippedItemsCount":1,
     "executionInitCount":1,
     "errorItemsCount":0,
     "normalItemsCount":10,
     "errorDetailCount":0,
     "executionSuccessItemsCount":10,
     "warningItemsCount":0,
     "warningDetailCount":0,
     "normalDetailCount":10,
     "cancelDetailCount":0,
     "executionFailedItemsCount":0,
```

```json
     "executingItemsCount":1
```

`},`

```json
    "inspectionItems":{
     "executionResult":{
      "capabilityId":1,
      "dimensionTitles":"\"\"",
      "executionType":0,
      "capability":{
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
      "updateTime":"2023-08-25T12:01:26.000+0000",
      "message":"Inspection succeeded",
      "statistics":{
       "totalItemsCount":10,
       "totalDetailCount":10,
       "executionSkippedItemsCount":1,
       "executionInitCount":1,
       "errorItemsCount":0,
       "normalItemsCount":10,
       "errorDetailCount":0,
       "executionSuccessItemsCount":10,
       "warningItemsCount":0,
       "warningDetailCount":0,
       "normalDetailCount":10,
       "cancelDetailCount":0,
       "executionFailedItemsCount":0,
       "executingItemsCount":1
```

`},`

```json
      "checkStatus":0,
      "taskExecutionId":1,
      "param":{
       "":""
```

`},`

```json
      "configId":1,
      "checkResults":{
       "checkStatus":0,
       "description":"Inspection succeeded",
       "id":1,
       "detail":"Inspection succeeded",
       "dimensions":"\"\"",
       "atomCapabilityExecutionId":1
```

`},`

```json
      "startTime":"2023-07-25T12:01:26.000+0000",
      "id":1,
      "endTime":"2023-09-25T12:01:26.000+0000",
```

```json
      "status":0,
      "extraInfo":"Inspection succeeded"
```

`},`

```json
     "inspectionCategoryId":10001,
     "capabilityId":1,
     "preinstall":true,
     "name":"Network inspection",
     "atomCapability":{
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "capabilityTypeName":"Script",
      "id":1,
      "capabilityType":1,
      "content":{
       "":""
```

`}` `},`

```json
     "description":"Network inspection",
     "active":true,
     "id":10001,
     "capabilityParam":{
      "":""
```

`}` `},`

```json
    "startTime":"2023-07-25T12:01:26.000+0000",
    "subCategories":{
     "checkStatus":0,
     "code":"network",
     "inspectionItemStatistics":{
      "totalItemsCount":10,
      "totalDetailCount":10,
      "executionSkippedItemsCount":1,
      "executionInitCount":1,
      "errorItemsCount":0,
      "normalItemsCount":10,
      "errorDetailCount":0,
      "executionSuccessItemsCount":10,
      "warningItemsCount":0,
      "warningDetailCount":0,
      "normalDetailCount":10,
      "cancelDetailCount":0,
      "executionFailedItemsCount":0,
      "executingItemsCount":1
```

`},`

```json
     "inspectionItems":{
      "atomCapability":{
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
```

```json
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
      "inspectionCategoryId":1,
      "capabilityId":1,
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "id":1,
      "capabilityParam":{
       "":""
```

`},`

```json
      "executionResult":{
       "checkResults":{
        "checkStatus":0,
        "description":"Inspection succeeded",
        "id":1,
        "detail":"Inspection succeeded",
        "dimensions":"\"\"",
        "atomCapabilityExecutionId":1
```

`},`

```json
       "capabilityId":1,
       "dimensionTitles":"\"\"",
       "executionType":1,
       "statistics":{
        "totalItemsCount":10,
        "totalDetailCount":10,
        "executionSkippedItemsCount":1,
        "executionInitCount":1,
        "errorItemsCount":0,
        "normalItemsCount":10,
        "errorDetailCount":0,
        "executionSuccessItemsCount":10,
        "warningItemsCount":0,
        "warningDetailCount":0,
        "normalDetailCount":10,
        "cancelDetailCount":0,
        "executionFailedItemsCount":0,
        "executingItemsCount":1
```

`},`

```json
       "capability":{
        "preinstall":true,
        "name":"Network inspection",
        "description":"Network inspection",
        "active":true,
        "capabilityTypeName":"Script",
        "id":1,
        "capabilityType":1,
        "content":{
         "":""
```

`}` `}` `},`

```json
       "updateTime":"2023-08-25T12:01:26.000+0000",
       "message":"Inspection succeeded",
       "checkStatus":0,
       "taskExecutionId":1,
       "param":{
        "":""
```

`},`

```json
       "configId":1,
       "startTime":"2023-07-25T12:01:26.000+0000",
       "id":1,
       "endTime":"2023-09-25T12:01:26.000+0000",
       "status":0,
       "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
     "executionStatus":0,
     "name":"Basic inspection",
     "startTime":"2023-07-25T12:01:26.000+0000",
     "id":1,
     "endTime":"2023-09-25T12:01:26.000+0000",
     "parentId":0,
     "order":0
```

`},`

```json
    "id":1,
    "endTime":"2023-09-25T12:01:26.000+0000",
    "parentId":0,
    "order":0
```

`},`

```json
   "inspectionItems":{
    "inspectionCategoryId":10001,
    "capabilityId":1,
    "preinstall":true,
    "name":"Network inspection",
    "description":"Network inspection",
    "active":true,
    "executionResult":{
     "capability":{
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "capabilityTypeName":"Script",
      "id":1,
      "capabilityType":1,
      "content":{
       "":""
```

`}` `},`

```json
     "capabilityId":1,
     "dimensionTitles":"\"\"",
     "executionType":0,
     "checkResults":{
      "checkStatus":0,
"description":"Inspectionsucceeded",
```

```json
      description:Inspection succeeded,
      "id":1,
      "detail":"Inspection succeeded",
      "dimensions":"\"\"",
      "atomCapabilityExecutionId":1
```

`},`

```json
     "updateTime":"2023-08-25T12:01:26.000+0000",
     "message":"Inspection succeeded",
     "statistics":{
      "totalItemsCount":10,
      "totalDetailCount":10,
      "executionSkippedItemsCount":1,
      "executionInitCount":1,
      "errorItemsCount":0,
      "normalItemsCount":10,
      "errorDetailCount":0,
      "executionSuccessItemsCount":10,
      "warningItemsCount":0,
      "warningDetailCount":0,
      "normalDetailCount":10,
      "cancelDetailCount":0,
      "executionFailedItemsCount":0,
      "executingItemsCount":1
```

`},`

```json
     "checkStatus":0,
     "taskExecutionId":1,
     "param":{
      "":""
```

`},`

```json
     "configId":1,
     "startTime":"2023-07-25T12:01:26.000+0000",
     "id":1,
     "endTime":"2023-09-25T12:01:26.000+0000",
     "status":0,
     "extraInfo":"Inspection succeeded"
```

`},`

```json
    "atomCapability":{
     "preinstall":true,
     "name":"Network inspection",
     "description":"Network inspection",
     "active":true,
     "capabilityTypeName":"Script",
     "id":1,
     "capabilityType":1,
     "content":{
      "":""
```

`}` `},`

```json
    "id":10001,
    "capabilityParam":{
     "":""
```

`}` `},`

```json
   "inspectionItemsCount":100,
   "schedules":{
```

```json
    "weekDays":1,
    "timeStr":"12:01:26"
```

`},`

```json
   "createTime":"2023-07-25T12:01:26.000+0000",
   "name":"Network inspection",
   "executionCount":10,
   "orders":0,
   "id":1
```

`}` `},`

```json
 "success":true,
 "errorTitle":"\"\"",
 "requestId":"8ae2a476-52b1-4bac-98c4-4ca17671482a",
 "errorMessage":"\"\"",
 "errorCode":"\"\""
```

`}`

##### 7.1.3.2 InspectionGetTaskExecution

Queries inspection records.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |

|   | Developer Gui | de·API R | eference |   | Apsa | ra Uni-manager Operations Consol | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| page | Integ er | Query | No | 1 | The page number. |
| taskId | Long | Query | No | 1 | The ID of the inspection scenario. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. true false |
| cost | Long | 74 | The response time. Unit: milliseconds. |
| path | String | /aso/inspection/so mepath | The request path. |
| serverRole | String | "" | The server role. |
| responseVersi on | String | v1 | The version of the response. |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The title of the error message. |
| errorMessage | String | "" | The error message. |
| requestId | String | 8ae2a476-52b1- 4bac-98c4- 4ca17671482a | The request ID. |
| eagleEyeTrace Id | String | "" | The EagleEye ID. |
| data | Struct |   | The response data. |
| -objectList | Array |   | The queried inspection records. |
| --id | Long | 1 | The ID of the inspection task. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| --createTime | String | 2023-07- 25T12:01:26.000+ 0000 | The time when the automatic snapshot policy was created. |
| --startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| --endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| -- executorUserN ame | String | opsadmin | The user who executed the inspection item. |
| --message | String | Inspection succeeded | The message that indicates the inspection result. |
| --extraInfo | String | Inspection succeeded | The details of the inspection result. |
| -- inspectionTask | Struct |   | The information about the inspection scenario. |
| --- inspectionItem s | Array |   | The inspection items. |
| ----id | Long | 10001 | The inspection item ID. |
| ---- inspectionCate goryId | Long | 10001 | The ID of the inspection category. |
| ----name | String | Network inspection | The name of the inspection item. |
| ----description | String | Network inspection | The description of the inspection item. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----capabilityId | Long | 1 | The ID of the atomic capability. |
| ---- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| ----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ---- atomCapabilit y | Struct |   | The information about the atomic capability. |
| -----id | Long | 1 | The ID of the atomic capability. |
| -----name | String | Network inspection | The name of the atomic capability. |
| -----description | String | Network inspection | The description of the atomic capability. |
| -----preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ----- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ----- capabilityType Name | String | Script | The name of the atomic capability category. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -----content | Map | {"":""} | The parameters of the atomic capability. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---- executionResu lt | Struct |   | The execution result of the inspection item. |
| ----- dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ----- checkResults | Array |   | The details of the inspection result. |
| ------ dimensions | String | "" | The returned values of the dimensions. |
| ------id | Long | 1 | The ID of the dimension entry. |
| ------ atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------ checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ------ description | String | Inspection succeeded | The description of the inspection result. |
| ------detail | String | Inspection succeeded | The details of the inspection result. |
| -----id | Long | 1 | The ID of the execution result. |
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| -----param | Map | {"":""} | The parameters of the atomic capability. |
| -----status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| -----message | String | Inspection succeeded | The message that indicates the inspection result. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -----extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ----- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----- updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ----- executionType | Integer | 0 | The execution type. |
| ----- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| -----configId | Long | 1 | The configuration ID. |
| -----capability | Struct |   | The information about the atomic capability. |
| ------id | Long | 1 | The ID of the atomic capability. |
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------ capabilityType Name | String | Script | The name of the atomic capability category. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| -----statistics | Struct |   | The statistics of inspection items. |
| ------ totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------ executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ------ executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------ executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------ executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ------ executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------ errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------ warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------ normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------ errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------ warningDetail Count | Integer | 0 | The number of returned inspection alerts. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------ cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------ totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ---schedules | Array |   | The configuration for scheduled inspection items. |
| ----weekDays | Integer | 1 | The day of the week to execute the inspection item. |
| ----timeStr | String | 12:01:26 | The time to execute the inspection item. |
| --- inspectionCate gories | Array |   | The information about the inspection category. |
| ---- subCategories | Array |   | The information about the inspection sub- category. |
| ----- inspectionItem s | Array |   | The inspection items. |
| ------id | Long | 1 | The inspection item ID. |
| ------ inspectionCate goryId | Long | 1 | The ID of the inspection category. |
| ------name | String | Network inspection | The name of the inspection item. |
| ------ description | String | Network inspection | The description of the inspection item. |
| ------preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ------ capabilityId | Long | 1 | The ID of the atomic capability. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------ atomCapabilit y | Struct |   | The information about the atomic capability. |
| -------id | Long | 1 | The ID of the atomic capability. |
| -------name | String | Network inspection | The name of the atomic capability. |
| ------- description | String | Network inspection | The description of the atomic capability. |
| -------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------- capabilityType Name | String | Script | The name of the atomic capability category. |
| -------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -------content | Map | {"":""} | The parameters of the atomic capability. |
| ------ executionResu lt | Struct |   | The execution result of the inspection item. |
| ------- dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ------- checkResults | Array |   | The details of the inspection result. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------- dimensions | String | "" | The returned values of the dimensions. |
| --------id | Long | 1 | The ID of the dimension entry. |
| -------- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| -------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -------- description | String | Inspection succeeded | The description of the inspection result. |
| --------detail | String | Inspection succeeded | The result of the check item. |
| -------id | Long | 1 | The ID of the execution result. |
| ------- capabilityId | Long | 1 | The ID of the atomic capability. |
| -------param | Map | {"":""} | The parameters of the atomic capability. |
| -------status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| -------message | String | Inspection succeeded | The message that indicates the inspection result. |
| -------extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -------endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ------- updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ------- executionType | Integer | 1 | The execution type. |
| ------- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| -------configId | Long | 1 | The configuration ID. |
| -------capability | Struct |   | The information about the atomic capability. |
| --------id | Long | 1 | The ID of the atomic capability. |
| --------name | String | Network inspection | The name of the atomic capability. |
| -------- description | String | Network inspection | The description of the atomic capability. |
| --------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| -------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| -------- capabilityType Name | String | Script | The name of the atomic capability category. |
| --------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| --------content | Map | {"":""} | The parameters of the atomic capability. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------statistics | Struct |   | The statistics of inspection items. |
| -------- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| -------- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| -------- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| -------- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| -------- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| -------- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| -------- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| -------- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| -------- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| -------- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| -------- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| -------- normalDetailC ount | Integer | 10 | The number of normal check items. |
| -------- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| -----id | Long | 1 | The ID of the inspection category. |
| -----name | String | Basic inspection | The name of the inspection category. |
| -----code | String | network | The code of the inspection category. |
| -----parentId | Long | 0 | The ID of the inspection category. |
| -----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ----- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -----order | Integer | 0 | The order of inspection items. |
| ----- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ------ totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------ executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------ executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------ executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ------ executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------ errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------ warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------ normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------ errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------ warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------ normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------ cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------ totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ---- inspectionItem s | Array |   | The inspection items. |
| -----id | Long | 10001 | The inspection item ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----- inspectionCate goryId | Long | 10001 | The ID of the inspection category. |
| -----name | String | Network inspection | The name of the inspection item. |
| -----description | String | Network inspection | The description of the inspection item. |
| -----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| ----- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ----- atomCapabilit y | Struct |   | The information about the atomic capability. |
| ------id | Long | 1 | The ID of the atomic capability. |
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------ capabilityType Name | String | Script | The name of the atomic capability category. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| ----- executionResu lt | Struct |   | The execution result of the inspection item. |
| ------ dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ------ checkResults | Array |   | The details of the inspection result. |
| ------- dimensions | String | "" | The returned values of the dimensions. |
| -------id | Long | 1 | The ID of the dimension entry. |
| ------- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ------- description | String | Inspection succeeded | The description of the inspection result. |
| -------detail | String | Inspection succeeded | The result of the check item. |
| ------id | Long | 1 | The ID of the execution result. |
| ------ capabilityId | Long | 1 | The ID of the atomic capability. |
| ------param | Map | {"":""} | The parameters of the atomic capability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ------message | String | Inspection succeeded | The message that indicates the inspection result. |
| ------extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ------ checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ------startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ------endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ------ updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection result. |
| ------ executionType | Integer | 0 | The execution type. |
| ------ taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| ------configId | Long | 1 | The configuration ID. |
| ------capability | Struct |   | The information about the atomic capability. |
| -------id | Long | 1 | The ID of the atomic capability. |
| -------name | String | Network inspection | The name of the atomic capability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------- description | String | Network inspection | The description of the atomic capability. |
| -------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------- capabilityType Name | String | Script | The name of the atomic capability category. |
| -------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -------content | Map | {"":""} | The parameters of the atomic capability. |
| ------statistics | Struct |   | The statistics of inspection items. |
| ------- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ------- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ------- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ----id | Long | 1 | The ID of the inspection category. |
| ----name | String | Network inspection | The name of the inspection category. |
| ----code | String | network | The code of the inspection category. |
| ----parentId | Long | 0 | The ID of the inspection category. |
| ----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ---- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ----order | Integer | 0 | The order of inspection items. |
| ---- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ----- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ----- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ----- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ----- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ----- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ----- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ----- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ----- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ----- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ----- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ----- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ----- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ----- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| --- inspectionItem sCount | Integer | 100 | The total number of inspection items. |
| ---id | Long | 1 | The ID of the scenario. |
| ---name | String | Network inspection | The name of the scenario. |
| ---description | String | Network inspection | The description of the scenario. |
| ---preinstall | Boolean | true | Indicates whether the scenario is preset. Valid values: true false |
| ---active | Boolean | true | Indicates whether the scenario is activated. Valid values: true false |
| ---createTime | String | 2023-09- 25T12:01:26.000+ 0000 | The time when the automatic snapshot policy was created. |
| --- createUserNa me | String | opsadmin | The user who created the inspection item. |
| --- executionCoun t | Integer | 10 | The number of times the inspection item was executed. |
| ---orders | Integer | 0 | The order of inspection scenarios. |
| -- inspectionItem Statistics | Struct |   | The statistics of inspection items. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| --- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| --- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| --- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| --- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| --- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| --- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| --- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| --- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| --- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| --- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| --- normalDetailC ount | Integer | 10 | The number of normal check items. |
| --- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| --- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -totalPage | Integer | 2 | The total number of pages returned. |
| -pageSize | Integer | 15 | The number of entries per page. |
| -total | Integer | 20 | The total number of entries. |
| -page | Integer | 1 | The page number. |

**Examples**

`JSON` format `{`

```json
 "serverRole":"\"\"",
 "path":"/aso/inspection/somepath",
 "eagleEyeTraceId":"\"\"",
 "cost":74,
 "responseVersion":"v1",
 "data":{
  "total":20,
  "totalPage":2,
  "pageSize":15,
  "page":1,
  "objectList":{
   "executorUserName":"opsadmin",
   "createTime":"2023-07-25T12:01:26.000+0000",
   "inspectionTask":{
    "preinstall":true,
    "inspectionCategories":{
     "checkStatus":0,
     "code":"network",
     "inspectionItemStatistics":{
      "totalItemsCount":10,
      "totalDetailCount":10,
      "executionSkippedItemsCount":1,
      "executionInitCount":1,
      "errorItemsCount":0,
      "normalItemsCount":10,
      "errorDetailCount":0,
      "executionSuccessItemsCount":10,
      "warningItemsCount":0,
      "warningDetailCount":0,
      "normalDetailCount":10,
      "cancelDetailCount":0,
      "executionFailedItemsCount":0,
      "executingItemsCount":1
```

`},`

```json
     "inspectionItems":{
      "atomCapability":{
```

```json
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
      "inspectionCategoryId":10001,
      "capabilityId":1,
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "id":10001,
      "capabilityParam":{
       "":""
```

`},`

```json
      "executionResult":{
       "checkResults":{
        "checkStatus":0,
        "description":"Inspection succeeded",
        "id":1,
        "detail":"Inspection succeeded",
        "dimensions":"\"\"",
        "atomCapabilityExecutionId":1
```

`},`

```json
       "capabilityId":1,
       "dimensionTitles":"\"\"",
       "executionType":0,
       "statistics":{
        "totalItemsCount":10,
        "totalDetailCount":10,
        "executionSkippedItemsCount":1,
        "executionInitCount":1,
        "errorItemsCount":0,
        "normalItemsCount":10,
        "errorDetailCount":0,
        "executionSuccessItemsCount":10,
        "warningItemsCount":0,
        "warningDetailCount":0,
        "normalDetailCount":10,
        "cancelDetailCount":0,
        "executionFailedItemsCount":0,
        "executingItemsCount":1
```

`},`

```json
       "capability":{
        "preinstall":true,
        "name":"Network inspection",
        "description":"Network inspection",
        "active":true,
```

```json
        "capabilityTypeName":"Script",
        "id":1,
        "capabilityType":1,
        "content":{
         "":""
```

`}` `},`

```json
       "updateTime":"2023-08-25T12:01:26.000+0000",
       "message":"Inspection succeeded",
       "checkStatus":0,
       "taskExecutionId":1,
       "param":{
        "":""
```

`},`

```json
       "configId":1,
       "startTime":"2023-07-25T12:01:26.000+0000",
       "id":1,
       "endTime":"2023-09-25T12:01:26.000+0000",
       "status":0,
       "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
     "executionStatus":0,
     "name":"Network inspection",
     "startTime":"2023-07-25T12:01:26.000+0000",
     "id":1,
     "endTime":"2023-09-25T12:01:26.000+0000",
     "subCategories":{
      "checkStatus":0,
      "inspectionItems":{
       "inspectionCategoryId":1,
       "capabilityId":1,
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "id":1,
       "capabilityParam":{
        "":""
```

`},`

```json
       "atomCapability":{
        "preinstall":true,
        "name":"Network inspection",
        "description":"Network inspection",
        "active":true,
        "capabilityTypeName":"Script",
        "id":1,
        "capabilityType":1,
        "content":{
         "":""
```

`}` `},`

```json
       "executionResult":{
        "checkResults":{
```

```json
         "checkStatus":0,
         "description":"Inspection succeeded",
         "id":1,
         "detail":"Inspection succeeded",
         "dimensions":"\"\"",
         "atomCapabilityExecutionId":1
```

`},`

```json
        "capabilityId":1,
        "dimensionTitles":"\"\"",
        "executionType":1,
        "capability":{
         "preinstall":true,
         "name":"Network inspection",
         "description":"Network inspection",
         "active":true,
         "capabilityTypeName":"Script",
         "id":1,
         "capabilityType":1,
         "content":{
          "":""
```

`}` `},`

```json
        "updateTime":"2023-08-25T12:01:26.000+0000",
        "message":"Inspection succeeded",
        "statistics":{
         "totalItemsCount":10,
         "totalDetailCount":10,
         "executionSkippedItemsCount":1,
         "executionInitCount":1,
         "errorItemsCount":0,
         "normalItemsCount":10,
         "errorDetailCount":0,
         "executionSuccessItemsCount":10,
         "warningItemsCount":0,
         "warningDetailCount":0,
         "normalDetailCount":10,
         "cancelDetailCount":0,
         "executionFailedItemsCount":0,
         "executingItemsCount":1
```

`},`

```json
        "checkStatus":0,
        "taskExecutionId":1,
        "param":{
         "":""
```

`},`

```json
        "configId":1,
        "startTime":"2023-07-25T12:01:26.000+0000",
        "id":1,
        "endTime":"2023-09-25T12:01:26.000+0000",
        "status":0,
        "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
      "code":"network",
"executionStatus":0
```

```json
      "executionStatus":0,
      "name":"Basic inspection",
      "startTime":"2023-07-25T12:01:26.000+0000",
      "id":1,
      "endTime":"2023-09-25T12:01:26.000+0000",
      "parentId":0,
      "inspectionItemStatistics":{
       "totalItemsCount":10,
       "totalDetailCount":10,
       "executionSkippedItemsCount":1,
       "executionInitCount":1,
       "errorItemsCount":0,
       "normalItemsCount":10,
       "errorDetailCount":0,
       "executionSuccessItemsCount":10,
       "warningItemsCount":0,
       "warningDetailCount":0,
       "normalDetailCount":10,
       "cancelDetailCount":0,
       "executionFailedItemsCount":0,
       "executingItemsCount":1
```

`},`

```json
      "order":0
```

`},`

```json
     "parentId":0,
     "order":0
```

`},`

```json
    "description":"Network inspection",
    "active":true,
    "createUserName":"opsadmin",
    "schedules":{
     "weekDays":1,
     "timeStr":"12:01:26"
```

`},`

```json
    "inspectionItemsCount":100,
    "createTime":"2023-09-25T12:01:26.000+0000",
    "name":"Network inspection",
    "inspectionItems":{
     "executionResult":{
      "capabilityId":1,
      "dimensionTitles":"\"\"",
      "executionType":0,
      "capability":{
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
"updateTime":"2023-08-25T12:01:26.000+0000",
```

```json
      updateTime:20230825T12:01:26.000+0000,
      "message":"Inspection succeeded",
      "statistics":{
       "totalItemsCount":10,
       "totalDetailCount":10,
       "executionSkippedItemsCount":1,
       "executionInitCount":1,
       "errorItemsCount":0,
       "normalItemsCount":10,
       "errorDetailCount":0,
       "executionSuccessItemsCount":10,
       "warningItemsCount":0,
       "warningDetailCount":0,
       "normalDetailCount":10,
       "cancelDetailCount":0,
       "executionFailedItemsCount":0,
       "executingItemsCount":1
```

`},`

```json
      "checkStatus":0,
      "taskExecutionId":1,
      "param":{
       "":""
```

`},`

```json
      "configId":1,
      "checkResults":{
       "checkStatus":0,
       "description":"Inspection succeeded",
       "id":1,
       "detail":"Inspection succeeded",
       "dimensions":"\"\"",
       "atomCapabilityExecutionId":1
```

`},`

```json
      "startTime":"2023-07-25T12:01:26.000+0000",
      "id":1,
      "endTime":"2023-09-25T12:01:26.000+0000",
      "status":0,
      "extraInfo":"Inspection succeeded"
```

`},`

```json
     "inspectionCategoryId":10001,
     "capabilityId":1,
     "preinstall":true,
     "name":"Network inspection",
     "atomCapability":{
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "capabilityTypeName":"Script",
      "id":1,
      "capabilityType":1,
      "content":{
       "":""
```

`}` `},`

```json
     "description":"Network inspection",
```

```json
     "active":true,
     "id":10001,
     "capabilityParam":{
      "":""
```

`}` `},`

```json
    "executionCount":10,
    "orders":0,
    "id":1
```

`},`

```json
   "inspectionItemStatistics":{
    "totalItemsCount":10,
    "totalDetailCount":10,
    "executionSkippedItemsCount":1,
    "executionInitCount":1,
    "errorItemsCount":0,
    "normalItemsCount":10,
    "errorDetailCount":0,
    "executionSuccessItemsCount":10,
    "warningItemsCount":0,
    "warningDetailCount":0,
    "normalDetailCount":10,
    "cancelDetailCount":0,
    "executionFailedItemsCount":0,
    "executingItemsCount":1
```

`},`

```json
   "executionStatus":0,
   "startTime":"2023-07-25T12:01:26.000+0000",
   "id":1,
   "endTime":"2023-09-25T12:01:26.000+0000",
   "message":"Inspection succeeded",
   "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
 "success":true,
 "errorTitle":"\"\"",
 "requestId":"8ae2a476-52b1-4bac-98c4-4ca17671482a",
 "errorMessage":"\"\"",
 "errorCode":"\"\""
```

`}`

##### 7.1.3.3 InspectionGetReport

Queries inspection reports.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| executionI d | Long | Query | Yes | 1 | The ID of the inspection task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. true false. |
| cost | Long | 74 | The response time. Unit: milliseconds. |
| path | String | /aso/inspection/so mepath | The request path. |
| serverRole | String | "" | The server role. |
| responseVersi on | String | v1 | The version of the response. |
| errorCode | String | "" | The error code. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | "" | The title of the error message. |
| errorMessage | String | "" | The error message. |
| requestId | String | 8ae2a476-52b1- 4bac-98c4- 4ca17671482a | The request ID. |
| eagleEyeTrace Id | String | "" | The EagleEye ID. |
| data | Struct |   | The response data. |
| -suggestion | String | Inspection succeeded | The suggestion. |
| - inspectionTask Execution | Struct |   | The information of the inspection task. |
| --id | Long | 1 | The ID of the inspection task. |
| -- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| --createTime | String | 2023-07- 25T12:01:26.000+ 0000 | The time when the inspection task was created. |
| --startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| --endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| -- executorUserN ame | String | opsadmin | The user who executed the inspection task. |
| --message | String | Inspection succeeded | The message that indicates the inspection result. |
| --extraInfo | String | Inspection succeeded | The details of the inspection result. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- inspectionTask | Struct |   | The information about the inspection scenario. |
| --- inspectionItem s | Array |   | The inspection items. |
| ----id | Long | 10001 | The inspection item ID. |
| ---- inspectionCate goryId | Long | 10001 | The ID of the inspection category. |
| ----name | String | Network inspection | The name of the inspection item. |
| ----description | String | Network inspection | The description of the inspection item. |
| ----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----capabilityId | Long | 1 | The ID of the atomic capability. |
| ---- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| ----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ---- atomCapabilit y | Struct |   | The information about the atomic capability. |
| -----id | Long | 1 | The ID of the atomic capability. |
| -----name | String | Network inspection | The name of the atomic capability. |
| -----description | String | Network inspection | The description of the atomic capability. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -----preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ----- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ----- capabilityType Name | String | Script | The name of the atomic capability category. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -----content | Map | {"":""} | The parameters of the atomic capability. |
| ---- executionResu lt | Struct |   | The execution result of the inspection item. |
| ----- dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ----- checkResults | Array |   | The details of the inspection result. |
| ------ dimensions | String | "" | The returned values of the dimensions. |
| ------id | Long | 1 | The ID of the dimension entry. |
| ------ atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------ checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ------ description | String | Inspection succeeded | The description of the inspection result. |
| ------detail | String | Inspection succeeded | The result of the check item. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -----id | Long | 1 | The ID of the execution result. |
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| -----param | Map | {"":""} | The parameters of the atomic capability. |
| -----status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| -----message | String | Inspection succeeded | The message that indicates the inspection result. |
| -----extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ----- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----- updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection. |
| ----- executionType | Integer | 0 | The execution type. |
| ----- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| -----configId | Long | 1 | The configuration ID. |
| -----capability | Struct |   | The information about the atomic capability. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------id | Long | 1 | The ID of the atomic capability. |
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------ capabilityType Name | String | Script | The name of the atomic capability category. |
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| -----statistics | Struct |   | The statistics of inspection items. |
| ------ totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------ executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ------ executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------ executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------ executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------ errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------ warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------ normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------ errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------ warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------ normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------ cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------ totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ---schedules | Array |   | The configuration for scheduled inspection items. |
| ----weekDays | Integer | 1 | The day of the week to execute the inspection item. |
| ----timeStr | String | 12:01:26 | The time to execute the inspection item. |
| --- inspectionCate gories | Array |   | The information about the inspection category. |
| ---- subCategories | Array |   | The information about the inspection sub- category. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----- inspectionItem s | Array |   | The inspection items. |
| ------id | Long | 1 | The inspection item ID. |
| ------ inspectionCate goryId | Long | 1 | The ID of the inspection category. |
| ------name | String | Network inspection | The name of the inspection item. |
| ------ description | String | Network inspection | The description of the inspection item. |
| ------preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ------ capabilityId | Long | 1 | The ID of the atomic capability. |
| ------ capabilityPara m | Map |   | The parameters of the atomic capability. |
| ------active | Boolean |   | Indicates whether the inspection item is activated. Valid values: true false |
| ------ atomCapabilit y | Struct |   | The information about the atomic capability. |
| -------id | Long | 1 | The ID of the atomic capability. |
| -------name | String | Network inspection | The name of the atomic capability. |
| ------- description | String | Network inspection | The description of the atomic capability. |
| -------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------- capabilityType Name | String | Script | The name of the atomic capability category. |
| -------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -------content | Map | {"":""} | The parameters of the atomic capability. |
| ------ executionResu lt | Struct |   | The execution result of the inspection item. |
| ------- dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ------- checkResults | Array |   | The details of the inspection result. |
| -------- dimensions | String | "" | The returned values of the dimensions. |
| --------id | Long | 1 | The ID of the dimension entry. |
| -------- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| -------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -------- description | String | Inspection succeeded | The description of the inspection result. |
| --------detail | String | Inspection succeeded | The result of the check item. |
| -------id | Long | 1 | The ID of the execution result. |
| ------- capabilityId | Long | 1 | The ID of the atomic capability. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------param | Map | {"":""} | The parameters of the atomic capability. |
| -------status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| -------message | String | Inspection succeeded | The message that indicates the inspection result. |
| -------extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -------startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -------endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ------- updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection. |
| ------- executionType | Integer | 1 | The execution type. |
| ------- taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| -------configId | Long | 1 | The configuration ID. |
| -------capability | Struct |   | The information about the atomic capability. |
| --------id | Long | 1 | The ID of the atomic capability. |
| --------name | String | Network inspection | The name of the atomic capability. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------- description | String | Network inspection | The description of the atomic capability. |
| --------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| -------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| -------- capabilityType Name | String | Script | The name of the atomic capability category. |
| --------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| --------content | Map | {"":""} | The parameters of the atomic capability. |
| -------statistics | Struct |   | The statistics of inspection items. |
| -------- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| -------- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| -------- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| -------- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| -------- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| -------- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| -------- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -------- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| -------- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| -------- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| -------- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| -------- normalDetailC ount | Integer | 10 | The number of normal check items. |
| -------- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| -------- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| -----id | Long | 1 | The ID of the inspection category. |
| -----name | String | Basic inspection | The name of the inspection category. |
| -----code | String | network | The code of the inspection category. |
| -----parentId | Long | 0 | The ID of the inspection category. |
| -----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| -----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ----- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| -----order | Integer | 0 | The order of inspection items. |
| ----- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ------ totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------ executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ------ executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------ executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------ executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ------ executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------ errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------ warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------ normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------ errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------ warningDetail Count | Integer | 0 | The number of returned inspection alerts. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------ cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------ totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ---- inspectionItem s | Array |   | The inspection items. |
| -----id | Long | 10001 | The inspection item ID. |
| ----- inspectionCate goryId | Long | 10001 | The ID of the inspection category. |
| -----name | String | Network inspection | The name of the inspection item. |
| -----description | String | Network inspection | The description of the inspection item. |
| -----preinstall | Boolean | true | Indicates whether the inspection item is preset. Valid values: true false |
| ----- capabilityId | Long | 1 | The ID of the atomic capability. |
| ----- capabilityPara m | Map | {"":""} | The parameters of the atomic capability. |
| -----active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ----- atomCapabilit y | Struct |   | The information about the atomic capability. |
| ------id | Long | 1 | The ID of the atomic capability. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------name | String | Network inspection | The name of the atomic capability. |
| ------ description | String | Network inspection | The description of the atomic capability. |
| ------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------ capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------ capabilityType Name | String | Script | The name of the atomic capability category. |
| ------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| ------content | Map | {"":""} | The parameters of the atomic capability. |
| ----- executionResu lt | Struct |   | The execution result of the inspection item. |
| ------ dimensionTitle s | String | "" | The dimensions of the inspection item. |
| ------ checkResults | Array |   | The details of the inspection result. |
| ------- dimensions | String | "" | The returned values of the dimensions. |
| -------id | Long | 1 | The ID of the dimension entry. |
| ------- atomCapabilit yExecutionId | Long | 1 | The ID of the atomic capability task. |
| ------- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| ------- description | String | Inspection succeeded | The description of the inspection result. |
|---|---|---|---|
| -------detail | String | Inspection succeeded | The result of the check item. |
| ------id | Long | 1 | The ID of the execution result. |
| ------ capabilityId | Long | 1 | The ID of the atomic capability. |
| ------param | Map | {"":""} | The parameters of the atomic capability. |
| ------status | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ------message | String | Inspection succeeded | The message that indicates the inspection result. |
| ------extraInfo | String | Inspection succeeded | The details of the inspection result. |
| ------ checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ------startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ------endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ------ updateTime | String | 2023-08- 25T12:01:26.000+ 0000 | The update time of the inspection. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------ executionType | Integer | 0 | The execution type. |
| ------ taskExecutionI d | Long | 1 | The ID of the scenario-specific inspection task. |
| ------configId | Long | 1 | The configuration ID. |
| ------capability | Struct |   | The information about the atomic capability. |
| -------id | Long | 1 | The ID of the atomic capability. |
| -------name | String | Network inspection | The name of the atomic capability. |
| ------- description | String | Network inspection | The description of the atomic capability. |
| -------preinstall | Boolean | true | Indicates whether the atomic capability is preset. Valid values: true false |
| ------- capabilityType | Integer | 1 | The ID of the atomic capability category. |
| ------- capabilityType Name | String | Script | The name of the atomic capability category. |
| -------active | Boolean | true | Indicates whether the inspection item is activated. Valid values: true false |
| -------content | Map | {"":""} | The parameters of the atomic capability. |
| ------statistics | Struct |   | The statistics of inspection items. |
| ------- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ------- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ------- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ------- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ------- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| ------- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ------- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ------- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ------- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ------- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ------- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ------- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ------- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ------- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| ----id | Long | 1 | The ID of the inspection category. |
| ----name | String | Network inspection | The name of the inspection category. |
| ----code | String | network | The code of the inspection category. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----parentId | Long | 0 | The ID of the inspection category. |
| ----startTime | String | 2023-07- 25T12:01:26.000+ 0000 | The start time of the inspection. |
| ----endTime | String | 2023-09- 25T12:01:26.000+ 0000 | The end time of the inspection. |
| ---- executionStat us | Integer | 0 | The state of the task. Valid values: 0: The task is being initialized. 1: The task is being executed. 2: The task is successful. 3: The task failed. 4: The task was skipped. |
| ---- checkStatus | Integer | 0 | The state of the task. Valid values: 0: normal. 1: alerting. 2: error. |
| ----order | Integer | 0 | The order of inspection items. |
| ---- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| ----- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| ----- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| ----- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| ----- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| ----- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| ----- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| ----- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| ----- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| ----- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| ----- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| ----- normalDetailC ount | Integer | 10 | The number of normal check items. |
| ----- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| ----- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| --- inspectionItem sCount | Integer | 10 | The total number of inspection items. |
| ---id | Long | 1 | The ID of the scenario-specific inspection task. |
| ---name | String | Network inspection | The name of the scenario-specific inspection task. |
| ---description | String | Network inspection | The description of the scenario-specific inspection task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---preinstall | Boolean | true | Indicates whether the scenario is preset. Valid values: true false |
| ---active | Boolean | true | Indicates whether the scenario-specific inspection task is activated. Valid values: true false |
| ---createTime | String | 2023-09- 25T12:01:26.000+ 0000 | The time when the inspection task was created. |
| --- createUserNa me | String | opsadmin | The user who created the inspection item. |
| --- executionCoun t | Integer | 10 | The number of times the inspection item was executed. |
| ---orders | Integer | 0 | The order of inspection scenarios. |
| -- inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| --- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| --- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| --- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| --- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| --- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |
| --- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| --- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| --- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| --- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| --- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| --- normalDetailC ount | Integer | 10 | The number of normal check items. |
| --- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| --- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |
| - inspectionItem Statistics | Struct |   | The statistics of inspection items. |
| -- totalItemsCou nt | Integer | 10 | The total number of inspection items. |
| -- executionSkip pedItemsCoun t | Integer | 1 | The number of inspection items that were skipped. |
| -- executionInitC ount | Integer | 1 | The number of inspection items that are being initialized. |
| -- executingItem sCount | Integer | 1 | The number of inspection items that are being executed. |
| -- executionSucc essItemsCount | Integer | 10 | The number of inspection items that were successful. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- executionFaile dItemsCount | Integer | 0 | The number of failed inspection items. |
| -- errorItemsCou nt | Integer | 0 | The number of inspection items on which an error occurred. |
| -- warningItemsC ount | Integer | 0 | The number of inspection items that triggered an alert. |
| -- normalItemsC ount | Integer | 10 | The number of normal inspection items. |
| -- errorDetailCou nt | Integer | 0 | The number of returned inspection errors. |
| -- warningDetail Count | Integer | 0 | The number of returned inspection alerts. |
| -- normalDetailC ount | Integer | 10 | The number of normal check items. |
| -- cancelDetailCo unt | Integer | 0 | The number of cancelled check items. |
| -- totalDetailCou nt | Integer | 10 | The total number of inspection errors, alerts, normal check items, and cancelled check items. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/inspection/api/inspection/getReport HTTP/1.1 &executionId=1 &<Common request parameters>
```

Sample success responses `JSON` format `{`

```json
 "serverRole":"\"\"",
 "path":"/aso/inspection/somepath",
 "eagleEyeTraceId":"\"\"",
 "cost":74,
 "responseVersion":"v1",
 "data":{
```

```json
  "suggestion":"Inspection succeeded",
  "inspectionItemStatistics":{
   "totalItemsCount":10,
   "totalDetailCount":10,
   "executionSkippedItemsCount":1,
   "executionInitCount":1,
   "errorItemsCount":0,
   "normalItemsCount":10,
   "errorDetailCount":0,
   "executionSuccessItemsCount":10,
   "warningItemsCount":0,
   "warningDetailCount":0,
   "normalDetailCount":10,
   "cancelDetailCount":0,
   "executionFailedItemsCount":0,
   "executingItemsCount":1
```

`},`

```json
  "inspectionTaskExecution":{
   "executorUserName":"opsadmin",
   "createTime":"2023-07-25T12:01:26.000+0000",
   "inspectionTask":{
    "preinstall":true,
    "inspectionCategories":{
     "checkStatus":0,
     "code":"network",
     "inspectionItemStatistics":{
      "totalItemsCount":10,
      "totalDetailCount":10,
      "executionSkippedItemsCount":1,
      "executionInitCount":1,
      "errorItemsCount":0,
      "normalItemsCount":10,
      "errorDetailCount":0,
      "executionSuccessItemsCount":10,
      "warningItemsCount":0,
      "warningDetailCount":0,
      "normalDetailCount":10,
      "cancelDetailCount":0,
      "executionFailedItemsCount":0,
      "executingItemsCount":1
```

`},`

```json
     "inspectionItems":{
      "atomCapability":{
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
      "inspectionCategoryId":10001,
      "capabilityId":1,
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "id":10001,
      "capabilityParam":{
       "":""
```

`},`

```json
      "executionResult":{
       "checkResults":{
        "checkStatus":0,
        "description":"Inspection succeeded",
        "id":1,
        "detail":"Inspection succeeded",
        "dimensions":"\"\"",
        "atomCapabilityExecutionId":1
```

`},`

```json
       "capabilityId":1,
       "dimensionTitles":"\"\"",
       "executionType":0,
       "statistics":{
        "totalItemsCount":10,
        "totalDetailCount":10,
        "executionSkippedItemsCount":1,
        "executionInitCount":1,
        "errorItemsCount":0,
        "normalItemsCount":10,
        "errorDetailCount":0,
        "executionSuccessItemsCount":10,
        "warningItemsCount":0,
        "warningDetailCount":0,
        "normalDetailCount":10,
        "cancelDetailCount":0,
        "executionFailedItemsCount":0,
        "executingItemsCount":1
```

`},`

```json
       "capability":{
        "preinstall":true,
        "name":"Network inspection",
        "description":"Network inspection",
        "active":true,
        "capabilityTypeName":"Script",
        "id":1,
        "capabilityType":1,
        "content":{
         "":""
```

`}` `},`

```json
       "updateTime":"2023-08-25T12:01:26.000+0000",
       "message":"Inspection succeeded",
       "checkStatus":0,
       "taskExecutionId":1,
```

`"` `"``{`

```json
       "param":{
        "":""
```

`},`

```json
       "configId":1,
       "startTime":"2023-07-25T12:01:26.000+0000",
       "id":1,
       "endTime":"2023-09-25T12:01:26.000+0000",
       "status":0,
       "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
     "executionStatus":0,
     "name":"Network inspection",
     "startTime":"2023-07-25T12:01:26.000+0000",
     "id":1,
     "endTime":"2023-09-25T12:01:26.000+0000",
     "subCategories":{
      "checkStatus":0,
      "inspectionItems":{
       "inspectionCategoryId":1,
       "capabilityId":1,
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":"",
       "id":1,
       "capabilityParam":"",
       "atomCapability":{
        "preinstall":true,
        "name":"Network inspection",
        "description":"Network inspection",
        "active":true,
        "capabilityTypeName":"Script",
        "id":1,
        "capabilityType":1,
        "content":{
         "":""
```

`}` `},`

```json
       "executionResult":{
        "checkResults":{
         "checkStatus":0,
         "description":"Inspection succeeded",
         "id":1,
         "detail":"Inspection succeeded",
         "dimensions":"\"\"",
         "atomCapabilityExecutionId":1
```

`},`

```json
        "capabilityId":1,
        "dimensionTitles":"\"\"",
        "executionType":1,
        "capability":{
         "preinstall":true,
         "name":"Network inspection",
"description":"Networkinspection"
```

```json
         description:Network inspection,
         "active":true,
         "capabilityTypeName":"Script",
         "id":1,
         "capabilityType":1,
         "content":{
          "":""
```

`}` `},`

```json
        "updateTime":"2023-08-25T12:01:26.000+0000",
        "message":"Inspection succeeded",
        "statistics":{
         "totalItemsCount":10,
         "totalDetailCount":10,
         "executionSkippedItemsCount":1,
         "executionInitCount":1,
         "errorItemsCount":0,
         "normalItemsCount":10,
         "errorDetailCount":0,
         "executionSuccessItemsCount":10,
         "warningItemsCount":0,
         "warningDetailCount":0,
         "normalDetailCount":10,
         "cancelDetailCount":0,
         "executionFailedItemsCount":0,
         "executingItemsCount":1
```

`},`

```json
        "checkStatus":0,
        "taskExecutionId":1,
        "param":{
         "":""
```

`},`

```json
        "configId":1,
        "startTime":"2023-07-25T12:01:26.000+0000",
        "id":1,
        "endTime":"2023-09-25T12:01:26.000+0000",
        "status":0,
        "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
      "code":"network",
      "executionStatus":0,
      "name":"Basic inspection",
      "startTime":"2023-07-25T12:01:26.000+0000",
      "id":1,
      "endTime":"2023-09-25T12:01:26.000+0000",
      "parentId":0,
      "inspectionItemStatistics":{
       "totalItemsCount":10,
       "totalDetailCount":10,
       "executionSkippedItemsCount":1,
       "executionInitCount":1,
       "errorItemsCount":0,
       "normalItemsCount":10,
"errorDetailCount":0,
```

```json
       errorDetailCount:0,
       "executionSuccessItemsCount":10,
       "warningItemsCount":0,
       "warningDetailCount":0,
       "normalDetailCount":10,
       "cancelDetailCount":0,
       "executionFailedItemsCount":0,
       "executingItemsCount":1
```

`},`

```json
      "order":0
```

`},`

```json
     "parentId":0,
     "order":0
```

`},`

```json
    "description":"Network inspection",
    "active":true,
    "createUserName":"opsadmin",
    "schedules":{
     "weekDays":1,
     "timeStr":"12:01:26"
```

`},`

```json
    "inspectionItemsCount":10,
    "createTime":"2023-09-25T12:01:26.000+0000",
    "name":"Network inspection",
    "inspectionItems":{
     "executionResult":{
      "capabilityId":1,
      "dimensionTitles":"\"\"",
      "executionType":0,
      "capability":{
       "preinstall":true,
       "name":"Network inspection",
       "description":"Network inspection",
       "active":true,
       "capabilityTypeName":"Script",
       "id":1,
       "capabilityType":1,
       "content":{
        "":""
```

`}` `},`

```json
      "updateTime":"2023-08-25T12:01:26.000+0000",
      "message":"Inspection succeeded",
      "statistics":{
       "totalItemsCount":10,
       "totalDetailCount":10,
       "executionSkippedItemsCount":1,
       "executionInitCount":1,
       "errorItemsCount":0,
       "normalItemsCount":10,
       "errorDetailCount":0,
       "executionSuccessItemsCount":10,
       "warningItemsCount":0,
       "warningDetailCount":0,
       "normalDetailCount":10,
```

```json
       "cancelDetailCount":0,
       "executionFailedItemsCount":0,
       "executingItemsCount":1
```

`},`

```json
      "checkStatus":0,
      "taskExecutionId":1,
      "param":{
       "":""
```

`},`

```json
      "configId":1,
      "checkResults":{
       "checkStatus":0,
       "description":"Inspection succeeded",
       "id":1,
       "detail":"Inspection succeeded",
       "dimensions":"\"\"",
       "atomCapabilityExecutionId":1
```

`},`

```json
      "startTime":"2023-07-25T12:01:26.000+0000",
      "id":1,
      "endTime":"2023-09-25T12:01:26.000+0000",
      "status":0,
      "extraInfo":"Inspection succeeded"
```

`},`

```json
     "inspectionCategoryId":10001,
     "capabilityId":1,
     "preinstall":true,
     "name":"Network inspection",
     "atomCapability":{
      "preinstall":true,
      "name":"Network inspection",
      "description":"Network inspection",
      "active":true,
      "capabilityTypeName":"Script",
      "id":1,
      "capabilityType":1,
      "content":{
       "":""
```

`}` `},`

```json
     "description":"Network inspection",
     "active":true,
     "id":10001,
     "capabilityParam":{
      "":""
```

`}` `},`

```json
    "executionCount":10,
    "orders":0,
    "id":1
```

`},`

```json
   "inspectionItemStatistics":{
    "totalItemsCount":10,
    "totalDetailCount":10,
```

```json
    "executionSkippedItemsCount":1,
    "executionInitCount":1,
    "errorItemsCount":0,
    "normalItemsCount":10,
    "errorDetailCount":0,
    "executionSuccessItemsCount":10,
    "warningItemsCount":0,
    "warningDetailCount":0,
    "normalDetailCount":10,
    "cancelDetailCount":0,
    "executionFailedItemsCount":0,
    "executingItemsCount":1
```

`},`

```json
   "executionStatus":0,
   "startTime":"2023-07-25T12:01:26.000+0000",
   "id":1,
   "endTime":"2023-09-25T12:01:26.000+0000",
   "message":"Inspection succeeded",
   "extraInfo":"Inspection succeeded"
```

`}` `},`

```json
 "success":true,
 "errorTitle":"\"\"",
 "requestId":"8ae2a476-52b1-4bac-98c4-4ca17671482a",
 "errorMessage":"\"\"",
 "errorCode":"\"\""
```

`}`

#### 7.1.4 Platform products

##### 7.1.4.1 GetProductListDetail

Queries the information about all products. We recommend that you use this API rather than `GetProductList` .

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 1000 | The number of entries per page. Default value: 20. |
| pageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | List | ["acr","acs","ads"," aliware- taokeeper","ans"," apigateway","appst reaming"] | The response. |
| pageSize | Integer | 10 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 37 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"[\"acr\",\"acs\",\"ads\",\"aliware-
taokeeper\",\"ans\",\"apigateway\",\"appstreaming\"]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":10,
 "totalRows":37,
 "message":"success",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.2 GetProductList

Queries the information about all products. We recommend that you use `GetProductListDetail` rather than this API.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | String | [\"ans\",\"asa\",\"as cm\",\"asd\",\"aso\" ,\"astc\",\"baseServ iceAll\",\"buffer\",\" cms\",\"config- assist\",\"ecs\"] | The response. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| pageSize | Integer | 10 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 13 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|
| Parameter | Type | Example | Description |

| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getProductList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"
[\\\"ans\\\",\\\"asa\\\",\\\"ascm\\\",\\\"asd\\\",\\\"aso\\\",\\\"astc\\\",\\\"baseServic ll\\\",\\\"buffer\\\",\\\"cms\\\",\\\"config-assist\\\",\\\"ecs\\\"]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":10,
 "totalRows":13,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.3 GetProductVersion

Queries the version of a product.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getProductVersion HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| project | Strin g | Query | No | aso | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error subcode message. An empty string is returned if the request is successful. |
| errorDetail | String |   | The error subcode details. An empty string is returned if the request is successful. |
| data | String | [{\"product\":\"aso\ ",\"product version _ \":\"ccec1cf3-91ec- 4c89-9e9e- fa65ccfc33ae\",\"id c\":\"A\"}] | The response. |
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. |
| cost | Long | 67 | The response time. Unit: milliseconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr#a | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getProductVersion HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"[{\\\"product\\\":\\\"aso\\\",\\\"product_version\\\":\\\"ccec1cf3-91ec-4c89-9
e9e-fa65ccfc33ae\\\",\\\"idc\\\":\\\"A\\\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"success",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#a",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":""
```

`}`

##### 7.1.4.4 DescribeProductStatus

Queries the desired states of clusters and services of a product based on the product name.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/getComponentStatus HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| project | Strin g | Query | Yes | aso | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |
| data | Struct |   | The response. |
| product | Map | {"aso":"notfinal"} | The name and desired state of the product. |
| cluster | Map | {"asoCluster- XXXXXXXXX":"notfi nal"} | The name and desired state of the cluster. |
| service | Map | {"aso- scm":"final","aso- ecsops":"final","as o- tools":"final","aso- doc":"final","os":"fi nal","aso- mgr":"notfinal","tia nji":"final","aso- systemMgr":"final", "aso- inventoryMgr":"fina l","aso- opr":"final","aso- physicalOps":"final ","tianji- dockerdaemon":"fi nal","aso- cplatformOps":"fin al","staragent- client":"final","aso- standalone":"final", "aso- slalink":"final","aso - console":"final","tia nji-sshtunnel- client":"final","aso- emergency":"final", "aso- monitor":"final"} | The name and desired state of the service. |
| cost | Long | 63 | The response time. Unit: milliseconds. |
| path | String | /aso/cmdb/openapi /getComponentStat us | The URL of the API. |
| key | String | ASO-GW-1- INTERNAL SERVER _ ERROR _ | The keyword of the error. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |

| psara Uni-manag Console | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | resource not found | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/getComponentStatus HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":63,
 "data":{
  "cluster":{
   "asoCluster-X\u0002XXXX\u0002XXXX":"notfinal"
```

`},`

```json
  "product":{
   "aso":"notfinal"
```

`},`

```json
  "service":{
   "aso-scm":"final",
   "aso-ecsops":"final",
   "aso-tools":"final",
   "aso-doc":"final",
   "os":"final",
   "aso-mgr":"notfinal",
   "tianji":"final",
   "aso-systemMgr":"final",
   "aso-inventoryMgr":"final",
   "aso-opr":"final",
   "aso-physicalOps":"final",
   "tianji-dockerdaemon":"final",
   "aso-cplatformOps":"final",
   "staragent-client":"final",
   "aso-standalone":"final",
   "aso-slalink":"final",
   "aso-console":"final",
   "tianji-sshtunnel-client":"final",
   "aso-emergency":"final",
   "aso-monitor":"final"
```

`}` `},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"failed",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/cmdb/openapi/getComponentStatus",
 "responseVersion":"v1",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "success":true,
 "errorTitle":"resource not found",
 "key":"ASO-GW-1-INTERNAL_SERVER_ERROR"
```

`}`

##### 7.1.4.5 GetClusterListByProductDetail

Queries a list of clusters of a product. We recommend that you use this API rather than `GetClusterListByProduct` .

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProductDetail HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 10 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| project | Strin g | Query | No | aso | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | Map | {"asa": ["asaCluster-XX- XX- XX"],"appstreamin g": ["ManageCluster- XX-XX-XX"],"acs": ["AcsControlCluster -XX-XX- XX"],"apigateway": ["classicCluster-XX- XX-XX"],"ads": ["ads-XX-XX- XX"],"ascm": ["ascm-XX-XX- XX","UniManagerB ase-XX-XX- XX","unimanagerBi lling-XX-XX-XX"]} | The mapping between a product and its clusters. |
| pageSize | Integer | 10 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 29 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. |

| A C | psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | fccbab1d-a496- 4ae6-88e8- 83557f883a85 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProductDetail HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":{
  "acs":[
   "AcsControlCluster-XX-XX-XX"
```

`],`

```json
  "apigateway":[
   "classicCluster-XX-XX-XX"
```

`],`

```json
  "ads":[
   "ads-XX-XX-XX"
```

`],`

```json
  "ascm":[
   "ascm-XX-XX-XX",
   "UniManagerBase-XX-XX-XX",
   "unimanagerBilling-XX-XX-XX"
```

`],`

```json
  "asa":[
   "asaCluster-XX-XX-XX"
```

`],`

```json
  "appstreaming":[
   "ManageCluster-XX-XX-XX"
```

`]` `},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":10,
 "totalRows":29,
 "message":"success",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"fccbab1d-a496-4ae6-88e8-83557f883a85",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.6 GetClusterListByProduct

Queries the information about clusters of a product. We recommend that you use `GetClusterListByProductDetail` rather than this API.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProduct HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 10 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| project | Strin g | Query | No | aso | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO MANAGE SYS _ _ TEM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates that whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | String | "{\"astoolbox\": [\"Basic-ASTB- Cluster-XX-XX- XX\"],\"asrdr\": [\"StandardCloudCl uster-XX-XX- XX\"]}" | The response. |
| pageSize | Integer | 10 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 29 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode message. An empty string is returned if the request is successful. |
| return subMsg _ | String | "" | The error subcode details. An empty string is returned if the request is successful. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | Service error | The title of the error message. |
| code | String | 200 | The response code. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| requestId | String | fccbab1d-a496- 4ae6-88e8- 83557f883a85 | The request ID. |
| cost | Long | 67 | The response time. |
| path | String | "" | The URL of the API. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| responseVersi on | String | v1 | The version of the response format. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getClusterListByProduct HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"\"{\\\"astoolbox\\\":[\\\"Basic-ASTB-Cluster-XX-XX-XX\\\"],\\\"asrdr\\\":[\\\"
StandardCloudCluster-XX-XX-XX\\\"]}\"",
 "errorMessage":"System error",
 "errorCode":"ASO_MANAGE_SYSTEM_ERROR",
 "pageSize":10,
 "totalRows":29,
 "message":"success",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"fccbab1d-a496-4ae6-88e8-83557f883a85",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.7 GetClusters

Queries a list of clusters and their status. We recommend that you use this API rather than `GetClusterListByProduct` .

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/clusters HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| productNa me | Strin g | Query | No | aso | The product name. |
| clusterNa me | Strin g | Query | No | asoCluster-XXXX-XX | The cluster name. |
| clusterSta tus | Strin g | Query | No | final | The status of the cluster. Valid values: final: desired state. notfinal: not reach the desired state. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| pageSize | Integ er | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The response. |
| result | Array of result |   | The returned result set. |
| region | String | cn-XX-XX-XX | The region ID. |
| projectName | String | aso | The product name. |
| name | String | asoCluster-XX-XX- XX | The cluster name. |
| status | String | notfinal | The status of the cluster. Valid values: final: desired state. notfinal: not reach the desired state. |
| serverCount | Integer | 5 | The number of machines. |
| serviceRoleCo unt | Integer | 25 | The number of server roles. |
| total | Integer | 100 | The total number of entries returned. |
| totalPage | Integer | 4 | The total number of pages returned. |
| pageSize | Integer | 10 | The number of entries per page. |
| currentPage | Integer | 1 | The page number. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | 32b53c70-97a8- 4e89-837f- d129f746688b | The request ID. |
| message | String | "" | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/clusters HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "result":{
   "serverCount":5,
   "serviceRoleCount":25,
   "name":"asoCluster-XX-XX-XX",
   "region":"cn-XX-XX-XX",
   "projectName":"aso",
   "status":"notfinal"
```

`},`

```json
  "total":100,
  "totalPage":4,
  "pageSize":10,
  "currentPage":1
```

`},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "requestId":"32b53c70-97a8-4e89-837f-d129f746688b",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.4.8 GetServiceInstanceDetail

Queries service instance information.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getServiceInstanceDetail HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 20 | The number of entries per page. Default value: 20. |
| pageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |
| project | Strin g | Query | Yes | aso | The product name. |
| cluster | Strin g | Query | Yes | asoCluster-XX-XX-XX | The cluster name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseCode | String | 200 | The response code. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | Array of data |   | The response. |
| name | String | aso-console | The service name. |
| state | String | good | The status of the service. Valid values: good: normal. probation: observation window. error: abnormal. |
| expectedServe rRoleCount | Integer | 1 | The number of expected server roles. |
| deletingServer RoleCount | Integer | 0 | The number of server roles that are being deleted. |
| goodExpected ServerRoleCou nt | Integer | 1 | The number of server roles that are expected in the normal state. |
| pageSize | Integer | 10 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 100 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 63 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getServiceInstanceDetail HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":63,
 "data":{
  "expectedServerRoleCount":1,
  "goodExpectedServerRoleCount":1,
  "name":"aso-console",
  "deletingServerRoleCount":0,
  "state":"good"
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":10,
 "totalRows":100,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.9 GetServerRoleList

Queries a list of server roles.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getServerRoleList HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| project | Strin g | Query | No | aso | The product name. |
| cluster | Strin g | Query | No | asoCluster-X-XXXX-XXXX | The cluster name. |
| server | Strin g | Query | No | aso-monitor | The service name. |
| idc | Strin g | Query | No | A | The data center. |
| type | Strin g | Query | No | vm | The type of the machine. |
| machineIp | Strin g | Query | No | 10.66.XX.XX | The IP address of the machine. |
| machine | Strin g | Query | No | vm01006600XXXX | The machine name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | String | [{\"cluster\":\"asoC luster-X-XXXX- XXXX\",\"dockerIp\" :\"\",\"id\":3044,\"id c\":\"A\",\"machine\ ":\"vm01006600XX XX\",\"machineIp\": \"10.66.XX.XX\",\" modifyTime\":1660 837174000,\"produ ct\":\"aso\",\"server \":\"aso- monitor\",\"serverr ole\":\"Tpcmon#\",\ "type\":\"vm\"}] | The response. |
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getServerRoleList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"[{\\\"cluster\\\":\\\"asoCluster-X-XXXX-
XXXX\\\",\\\"dockerIp\\\":\\\"\\\",\\\"id\\\":3044,\\\"idc\\\":\\\"A\\\",\\\"machine\\\": \"vm01006600XXXX\\\",\\\"machineIp\\\":\\\"10.66.XX.XX\\\",\\\"modifyTime\\\":16608371740 ,\\\"product\\\":\\\"aso\\\",\\\"server\\\":\\\"asomonitor\\\",\\\"serverrole\\\":\\\"Tpcmon#\\\",\\\"type\\\":\\\"vm\\\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.10 GetServerroleVersion

Queries the version information of a server role.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getServerroleVersion HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| serverrole | Strin g | Query | No | ApiInit# | The service role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | String | [{\"cluster\":\"asoC luster-X-XXXX- XXXX\",\"serverrole \":\"ApiInit#\",\"ser verrole version\":\" _ 3474896 aso- _ ecsops ApiInit f7b _ _ eb90b\",\"product\" :\"aso\",\"service\": \"aso- ecsops\",\"idc\":\"A\ "}, {\"cluster\":\"ECS- controller-X- XXXX\",\"serverrole \":\"ApiInit#\",\"ser verrole version\":\" _ 3533672 ecs- _ YaochiInit ApiInit 6 _ _ 4216aeb\",\"produc t\":\"ecs\",\"service \":\"ecs- YaochiInit\",\"idc\":\ "A\"}, {\"cluster\":\"opsap iCluster-X-XXXX- XXXX\",\"serverrole \":\"ApiInit#\",\"ser verrole version\":\" _ 3535084 opsapi A _ _ piInit c7620cd2\",\ _ "product\":\"opsapi \",\"service\":\"opsa pi\",\"idc\":\"A\"}] | The response. |
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of entries returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | fa07ab18-06cf- 470f-9417- c6ae644bbe2c | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getServerroleVersion HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":30,
 "data":"[{\\\"cluster\\\":\\\"asoCluster-X-XXXX-
XXXX\\\",\\\"serverrole\\\":\\\"ApiInit#\\\",\\\"serverrole_version\\\":\\\"3474896_asoecsops_ApiInit_f7beb90b\\\",\\\"product\\\":\\\"aso\\\",\\\"service\\\":\\\"aso-ecsops\ \\",\\\"idc\\\":\\\"A\\\"},{\\\"cluster\\\":\\\"ECS-controller-X- XXXX\\\",\\\"serverrole\\\":\\\"ApiInit#\\\",\\\"serverrole_version\\\":\\\"3533672_ecs- YaochiInit_ApiInit_64216aeb\\\",\\\"product\\\":\\\"ecs\\\",\\\"service\\\":\\\"ecs-Yao chiInit\\\",\\\"idc\\\":\\\"A\\\"},{\\\"cluster\\\":\\\"opsapiCluster-X-XXXX-XXXX\\\",\ \\"serverrole\\\":\\\"ApiInit#\\\",\\\"serverrole_version\\\":\\\"3535084_opsapi_ApiInit_ 620cd2\\\",\\\"product\\\":\\\"opsapi\\\",\\\"service\\\":\\\"opsapi\\\",\\\"idc\\\":\\\" \\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"fa07ab18-06cf-470f-9417-c6ae644bbe2c",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.4.11 GetServiceRole

Queries a list of server roles and their status.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/serviceRole HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| productNa me | Strin g | Query | No | aso | The product name. |
| clusterNa me | Strin g | Query | No | asoCluster-XX-XX-XX | The cluster name. |
| serviceNa me | Strin g | Query | No | aso-mgr | The service name. |
| serviceRol eName | Strin g | Query | No | asmgr# | The service role. |
| status | Strin g | Query | No | good | The status of the service role. Valid values: GOOD: normal. PROBATION: observation window. ERROR: abnormal. |
| pageNum | Integ er | Query | No | 1 | The page number. |

| Developer Gui | de·API R | eference |   | Apsa | ra Uni-manager Operations |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Struct |   | The response. |
| result | Array of result |   | An array of returned data. |
| region | String | cn-XX-XX-XX | The region name. |
| product | String | aso | The product name. |
| clusterName | String | asoCluster-XX-XX- XX | The cluster name. |
| serviceName | String | aso-mgr | The service name. |
| name | String | asmgr# | The service role. |
| status | String | GOOD | The status of the service role. Valid values: GOOD: normal. PROBATION: observation window. ERROR: abnormal. |
| machinesCoun t | Integer | 2 | The number of machines. |
| errorMachines Count | Integer | 0 | The number of abnormal machines. |
| normalMachin esCount | Integer | 2 | The number of normal machines. |
| alarmCount | Integer | 0 | The number of machine alerts. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| machineInfoLi st | Array of machineInfoLi st |   | The machines. |
| machine | String | test vm _ | The machine name. |
| machine ip _ | String | 10.25.XX.X | The IP address of the machine. |
| status | String | GOOD | The status of the machine. Valid values: GOOD: normal. OS ERROR: OS exception. _ PROBATION: observation window. ERROR: abnormal. OS PROBATION: OS observation _ window. |
| sn | String | test vm _ | The serial number of the machine. |
| total | Integer | 1 | The total number of entries returned. |
| totalPage | Integer | 1 | The total number of pages returned. |
| pageSize | Integer | 10 | The number of entries per page. |
| currentPage | Integer | 1 | The page number. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | b91429a7-0762- 4b21-882d- 35eb5a80ff2d | The request ID. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/cmdb/openapi /serviceRole | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/serviceRole HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "result":{
   "alarmCount":0,
   "product":"aso",
   "errorMachinesCount":0,
   "clusterName":"asoCluster-XX-XX-XX",
   "name":"asmgr#",
   "machinesCount":2,
   "normalMachinesCount":2,
   "machineInfoList":{
    "machine":"test_vm",
    "machine_ip":"10.25.XX.X",
    "sn":"test_vm",
    "status":"GOOD"
```

`},`

```json
   "region":"cn-XX-XX-XX",
   "serviceName":"aso-mgr",
   "status":"GOOD"
```

`},`

```json
  "total":1,
  "totalPage":1,
  "pageSize":10,
  "currentPage":1
```

`},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"\"\"",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/cmdb/openapi/serviceRole",
 "responseVersion":"v1",
 "requestId":"b91429a7-0762-4b21-882d-35eb5a80ff2d",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.4.12 GetServerRoleMachinesDetail

Queries the association information between server roles and machines.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getServerRoleMachinesDetail HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 20 | The number of entries per page. Default value: 20. |
| pageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |
| project | Strin g | Query | Yes | aso | The product name. |
| cluster | Strin g | Query | Yes | asoCluster-XX-XX-XX | The cluster name. |
| service | Strin g | Query | Yes | aso-mgr | The service name. |
| serverrole | Strin g | Query | Yes | asmgr# | The service role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | Array of data |   | The response. |
| sn | String | test vm _ | The serial number of the machine. |
| state | String | good | The status of the service role. Valid values: good: normal. probation: observation window. error: abnormal. |
| cluster | String | asoCluster-XX-XX- XX | The cluster name. |
| idc | String | test idc _ | The data center. |
| ip | String | 10.205.XX.XX | The IP address of the machine. |
| machineState | String | good | The status of the machine. |
| pageSize | Integer | 20 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| totalRows | Long | 100 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 500 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 63 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getServerRoleMachinesDetail HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"500",
 "cost":63,
 "data":{
  "cluster":"asoCluster-XX-XX-XX",
  "machineState":"good",
  "ip":"10.205.XX.XX",
  "idc":"test_idc",
  "sn":"test_vm",
  "state":"good"
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":20,
 "totalRows":100,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

#### 7.1.5 Equipment assets

##### 7.1.5.1 GetMachineByIp

Queries the information about physical machines based on IP addresses.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getMachineByIp HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| ip | Strin g | Query | No | 10.66.XX.XX | The IP address of the machine. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates whether the request was successful. success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error subcode message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error subcode details. An empty string is returned if the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [{"machine type fr _ _ om manufacturer": _ "","cluster":"Standa rdAsrbrCluster-X- XXXX- XXXX","project":"a srbr","max docker _ _ number":"0","sm n _ ame":"VM","spec":" {}","TianjiCluster": "StandardAsrbrClus ter-X-XXXX- XXXX","guarantee _ brandname":"vm d _ ocker","is vm":"tru _ e","hostname":"vm 01006602XXXX","s tate description":" _ PROBATION slice wind end since 1657164399113.ti meout = 30000ms[default]." ,"hw mem":"18636 _ ","state":"GOOD","a zone":"cn-XXXX- XXXX-amtestXXXX- a","machine type _ _ with nic type":"VM _ _ ","npod":"ASW.XXX X- 1","big container n _ _ umber":"0","ip":"10 .66.XX.XXX","idc":" amtestXXXX","part ":"ALdefault","use _ vm number":"0","h _ w cpu":"2","host ty _ _ pe":"vm","cpu arc _ h":"x86 64","srg q _ _ uota":" {"cpu":8.9,"diskSiz e":64,"memory":18 .2,"gpu":0}","hw h _ arddisk":"65536"," use big container _ _ _ number":"0","powe r":"0","sn":"vm010 06602XXXX","expe cted os":" _ {"os":"AliOS7U2- x86- 64","part":"ALdefa ult","app name":"d _ ockervm"}","curre nt os":" _ {"os":"AliOS7U2- x86- 64","part":"ALdefa ult","app name":"d _ ockervm"}","use d _ ocker number":"0" _ }] | The response. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| code | String | 200 | The response code. |
| message | String | "" | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| path | String | "" | The URL of the API. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| serverRole | String | aso-mgr.asmgr# | The service role of the machine. |
| responseVersi on | String | v1 | The version of the response format. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getMachineByIp HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"[{\"machine_type_from_manufacturer\":\"\",\"cluster\":\"StandardAsrbrCluster-X
-XXXX- XXXX\",\"project\":\"asrbr\",\"max_docker_number\":\"0\",\"sm_name\":\"VM\",\"spec\":\" {}\",\"TianjiCluster\":\"StandardAsrbrCluster-X-XXXX- XXXX\",\"guarantee_brandname\":\"vm_docker\",\"is_vm\":\"true\",\"hostname\":\"vm01006602 XX\",\"state_description\":\"PROBATION slice wind end since 1657164399113.timeout = 300 00ms[default].\",\"hw_mem\":\"18636\",\"state\":\"GOOD\",\"azone\":\"cn-XXXX-XXXX-amtes tXXXX-a\",\"machine_type_with_nic_type\":\"VM\",\"npod\":\"ASW.XXXX- 1\",\"big_container_number\":\"0\",\"ip\":\"10.66.XX.XXX\",\"idc\":\"amtestXXXX\",\"part\ \"ALdefault\",\"use_vm_number\":\"0\",\"hw_cpu\":\"2\",\"host_type\":\"vm\",\"cpu_arch\": x86_64\",\"srg_quota\":\" {\"cpu\":8.9,\"diskSize\":64,\"memory\":18.2,\"gpu\":0}\",\"hw_harddisk\":\"65536\",\"use ig_container_number\":\"0\",\"power\":\"0\",\"sn\":\"vm01006602XXXX\",\"expected_os\":\" {\"os\":\"AliOS7U2-x86- 64\",\"part\":\"ALdefault\",\"app_name\":\"dockervm\"}\",\"current_os\":\" {\"os\":\"AliOS7U2-x86- 64\",\"part\":\"ALdefault\",\"app_name\":\"dockervm\"}\",\"use_docker_number\":\"0\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"\"\"",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.5.2 GetMachineByName

Queries the information about physical machines based on machine names.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getMachineByName HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| name | Strin g | Query | No | vm01006602XXXX | The machine name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [{"machine type fr _ _ om manufacturer": _ "","cluster":"Standa rdAsrbrCluster-X- 2022XXXX- XXXX","project":"a srbr","max docker _ _ number":"0","sm n _ ame":"VM","spec":" {}","TianjiCluster": "StandardAsrbrClus ter-X-XXXX- XXXX","guarantee _ brandname":"vm d _ ocker","is vm":"tru _ e","hostname":"vm 01006602XXXX","h w mem":"18636"," _ security domain":" _ ","state":"GOOD","a zone":"cn-XXXX- XXXX- amtest1XXXX- a","machine type _ _ with nic type":"VM _ _ ","npod":"ASW.XXX X- 1","big container n _ _ umber":"0","ip":"10 .66.XX.XX","idc":"a mtestXX","bucket": "default","is ops wi _ _ th vm":"N/A","expe _ cted link":" _ []","part":"ALdefaul t","use vm numbe _ _ r":"0","hw cpu":"2", _ "host type":"vm","c _ pu arch":"x86 64", _ _ "srg quota":" _ {"cpu":8.9,"diskSiz e":64,"memory":18 .2,"gpu":0}","hw h _ arddisk":"65536"," use big container _ _ _ number":"0","powe r":"0","sn":"vm010 06602XXXX","expe cted os":" _ {"os":"AliOS7U2- x86- 64","part":"ALdefa ult","app name":"d _ ockervm"}","curre nt os":" _ {"os":"AliOS7U2- x86- 64","part":"ALdefa ult","app name":"d _ ockervm"}","use d _ ocker number":"0" _ }] | The response. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getMachineByName HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"[{\"machine_type_from_manufacturer\":\"\",\"cluster\":\"StandardAsrbrCluster-X
-2022XXXX- XXXX\",\"project\":\"asrbr\",\"max_docker_number\":\"0\",\"sm_name\":\"VM\",\"spec\":\" {}\",\"TianjiCluster\":\"StandardAsrbrCluster-X-XXXX- XXXX\",\"guarantee_brandname\":\"vm_docker\",\"is_vm\":\"true\",\"hostname\":\"vm01006602 XX\",\"hw_mem\":\"18636\",\"security_domain\":\"\",\"state\":\"GOOD\",\"azone\":\"cn-XX XX-XXXX-amtest1XXXX-a\",\"machine_type_with_nic_type\":\"VM\",\"npod\":\"ASW.XXXX-1\",\ "big_container_number\":\"0\",\"ip\":\"10.66.XX.XX\",\"idc\":\"amtestXX\",\"bucket\":\"de ult\",\"is_ops_with_vm\":\"N/A\",\"expected_link\":\" []\",\"part\":\"ALdefault\",\"use_vm_number\":\"0\",\"hw_cpu\":\"2\",\"host_type\":\"vm\" "cpu_arch\":\"x86_64\",\"srg_quota\":\" {\"cpu\":8.9,\"diskSize\":64,\"memory\":18.2,\"gpu\":0}\",\"hw_harddisk\":\"65536\",\"use ig_container_number\":\"0\",\"power\":\"0\",\"sn\":\"vm01006602XXXX\",\"expected_os\":\" {\"os\":\"AliOS7U2-x86- 64\",\"part\":\"ALdefault\",\"app_name\":\"dockervm\"}\",\"current_os\":\" {\"os\":\"AliOS7U2-x86- 64\",\"part\":\"ALdefault\",\"app_name\":\"dockervm\"}\",\"use_docker_number\":\"0\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"\"\"",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.5.3 GetMachineListDetail

Queries the information about machines. We recommend that you use this API rather than `GetProductList` .

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getMachineListDetail HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 20 | The number of entries per page. Default value: 20. |
| pageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |
| project | Strin g | Query | No | aso | The product name. |
| cluster | Strin g | Query | No | asoCluster-XX-XX-XX | The cluster name. |
| idc | Strin g | Query | No | amtestxxx | The data center. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | Array of data |   | The response. |
| sn | String | test vm _ | The serial number of the machine. |
| hostName | String | test vm _ | The hostname. |
| ip | String | 10.205.XX.XX | The IP address of the host. |
| model | String | docker | The machine type. Valid values: physical: physical machine. docker: virtual machine. |
| isVm | Integer | 1 | Indicates whether it is a virtual machine. Valid values: 0: no. 1: yes. |
| machineType WithNicType | String | VM | The machine model and network interface controller (NIC) model. |
| idc | String | test idc _ | The data center. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| room | String | "" | The server room name. |
| rack | String | "" | The rack name. |
| cpu | Integer | 2 | The number of CPU cores. |
| memory | Integer | 17817 | The memory capacity of the machine. Unit: MB. |
| disk | Integer | 144384 | The disk space of the machine. Unit: MB. |
| azone | String | cn-XX-XX-XX-X | The zone ID. |
| cpuArch | String | x86 64 _ | The CPU architecture. |
| smName | String | VM | The machine model. |
| rackUnitId | String | "" | The rack ID. |
| rackGroup | String | ASW.XX-X | The rack group. |
| devFunction | String | Controller | The role of the machine. Valid values: Controller. Worker. VmHost. |
| clusterName | String | asoCluster-XX-XX- XX | The cluster name. |
| status | String | GOOD | The status of the machine. Valid values: GOOD: normal. OS ERROR: OS exception. _ PROBATION: observation window. ERROR: abnormal. OS PROBATION: OS observation _ window. |
| project | String | aso | The product name. |
| cpuAvg | Integer | 57 | The CPU utilization of the machine. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| loadAvg | Integer | 1 | The CPU load of the machine. |
| diskAvg | Integer | 13 | The disk utilization of the machine. |
| memAvg | Integer | 3 | The memory utilization of the machine. |
| trafficAvg | Integer | 21776 | The data transfer volume of the machine. Unit: bytes. |
| ioAvg | Integer | 14 | The I/O load of the machine. |
| targetHost | String | test host _ | The host. |
| pageSize | Integer | 20 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 100 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string is returned if the request is successful. |
| return subMsg _ | String | "" | The error subcode message. An empty string is returned if the request is successful. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| message | String | failed | The returned message. If the request was successful, a success message is returned. If the request failed, a failed message is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getMachineListDetail HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":30,
 "data":{
  "hostName":"test_vm",
  "memory":17817,
  "trafficAvg":21776,
  "devFunction":"Controller",
  "project":"aso",
  "machineTypeWithNicType":"VM",
  "rackUnitId":"\"\"",
  "clusterName":"asoCluster-XX-XX-XX",
```

```json
  "diskAvg":13,
  "model":"docker",
  "cpuAvg":57,
  "sn":"test_vm",
  "loadAvg":1,
  "azone":"cn-XX-XX-XX-X",
  "rackGroup":"ASW.XX-X",
  "rack":"\"\"",
  "targetHost":"test_host ",
  "ip":"10.205.XX.XX ",
  "smName":"VM",
  "idc":"test_idc",
  "cpu":2,
  "cpuArch":"x86_64 ",
  "room":"\"\"",
  "isVm":1,
  "disk":144384,
  "ioAvg":14,
  "status":"GOOD",
  "memAvg":3
```

`},`

```json
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":20,
 "totalRows":100,
 "message":"failed",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.5.4 GetMachineList

Queries a list of physical machines. We recommend that you use `GetProductListDetail` rather than this API.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getMachineList HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| dataVersi on | Strin g | Query | No | v3 | The version of the data. Default value: v3. |
| pageSize | Integ er | Query | No | 10 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| project | Strin g | Query | No | oss | The product name. |
| cluster | Strin g | Query | No | OssHybridCluster-XX-XX- XX | The cluster name. |
| idc | Strin g | Query | No | test idc _ | The data center. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |
| data | String | [{"machine type fr _ _ om manufacturer": _ "","node group":"", _ "cluster":"ansClust er-XX-XX- XX","project":"ans" ,"max docker num _ _ ber":"0","sm name _ ":"VM","action par _ ams":"","nic info":" _ ","rack unit id":""," _ _ spec":" {}","TianjiCluster": "ansCluster-XX-XX- XX","ecs region":"" _ ,"guarantee brand _ name":"vm docker _ ","is vm":"true","ho _ stname":"test vm", _ "hw mem":"1331", _ "date purchase":"" _ ,"uniform type":""," _ action name":""," _ model":"","security domain":"","state" _ :"GOOD","ip config _ ":"","machine type _ with nic type":"V _ _ _ M","npod":"ASW.X X- XX","vm host tag": _ _ "","big container n _ _ umber":"0","idc":"t est idc"}] _ | The response. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| pageSize | Integer | 20 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 100 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getMachineList HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"
[{\"machine_type_from_manufacturer\":\"\",\"node_group\":\"\",\"cluster\":\"ansCluster- XX-XX- XX\",\"project\":\"ans\",\"max_docker_number\":\"0\",\"sm_name\":\"VM\",\"action_params\" "\",\"nic_info\":\"\",\"rack_unit_id\":\"\",\"spec\":\" {}\",\"TianjiCluster\":\"ansCluster-XX-XX- XX\",\"ecs_region\":\"\",\"guarantee_brandname\":\"vm_docker\",\"is_vm\":\"true\",\"hostn e\":\"test_vm\",\"hw_mem\":\"1331\",\"date_purchase\":\"\",\"uniform_type\":\"\",\"action ame\":\"\",\"model\":\"\",\"security_domain\":\"\",\"state\":\"GOOD\",\"ip_config\":\"\", machine_type_with_nic_type\":\"VM\",\"npod\":\"ASW.XX- XX\",\"vm_host_tag\":\"\",\"big_container_number\":\"0\",\"idc\":\"test_idc\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":20,
 "totalRows":100,
 "message":"\"\"",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.5.5 GetNetworkMachineByIp

Queries network device information based on IP addresses.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getNetworkMachineByIp HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| ip | Strin g | Query | No | 10.66.XX.X | The IP address of the network device. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [{\"stack\":\"false\" ,\"role\":\"ASW.10G E\",\"expected link\ _ ":\"- startport:\ name: EthernetXXXX\ speed: \\\"40000\\\"\ endport:\ name: FortyGigE0/XXXX\ speed: \\\"40000\\\"\ enddevice: DSW- VM-XX-X- X.AMTEXXXX\- startport:\ name: EthernetXXXX\ speed: \\\"40000\\\"\ endport:\ name: EthernetXXXX\ speed: \\\"40000\\\"\ enddevice: ASW- XX-X- XX.AMTEXXXX- X.AMTEXXXX\\",\"d evice type\":\"netw _ ork device\",\"host _ type\":\"network _ _ device\",\"TianjiClu ster\":\"amteXXXX\ ",\"manufacturer\": \"Cisco\",\"hostnam e\":\"ASW-XX-X- DXX.AMTEXXXX- 1.AMTEXXXX\",\"np od id\":\"ASW.XXX _ X- X\",\"model\":\"N9K -C921XXXX- X\",\"power\":\"0\",\ "sn\":\"FDO2351XX XX\",\"location in r _ _ ack\":\"52\",\"rack\" :\"D13\",\"device id _ \":\"ASW.XXXX- X.X\",\"ip\":\"10.66. XXX.XX\",\"idc\":\"A MTEXXXX\",\"index \":\"2\",\"weight\":\" 0\",\"pair\":\"true\", \"room\":\"A3- 4\",\"is ops with v _ _ _ m\":\"N/A\",\"pod i _ d\":\"ASW.XXXX- X\"}] | The response. |
| pageSize | Integer | 15 | The number of entries per page. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| pageNum | Integer | 1 | The page number. |
| totalRows | Long | 1 | The total number of rows. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. |
| cost | Long | 67 | The response time. Unit: milliseconds. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getNetworkMachineByIp HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":67,
 "data":"
[{\\\"stack\\\":\\\"false\\\",\\\"role\\\":\\\"ASW.10GE\\\",\\\"expected_link\\\":\\\"startport:\\ name: EthernetXXXX\\ speed: \\\\\\\"40000\\\\\\\"\\ endport:\\ name: Forty GigE0/XXXX\\ speed: \\\\\\\"40000\\\\\\\"\\ enddevice: DSW-VM-XX-X-X.AMTEXXXX\\- startp ort:\\ name: EthernetXXXX\\ speed: \\\\\\\"40000\\\\\\\"\\ endport:\\ name: EthernetXXXX\\ speed: \\\\\\\"40000\\\\\\\"\\ enddevice: ASW-XX-X-XX.AMTEXXXX-X.AMTEXXX X\\\\\",\\\"device_type\\\":\\\"network_device\\\",\\\"host_type\\\":\\\"network_device\\ ,\\\"TianjiCluster\\\":\\\"amteXXXX\\\",\\\"manufacturer\\\":\\\"Cisco\\\",\\\"hostname\\ :\\\"ASW-XX-X-DXX.AMTEXXXX-1.AMTEXXXX\\\",\\\"npod_id\\\":\\\"ASW.XXXX- X\\\",\\\"model\\\":\\\"N9K-C921XXXX- X\\\",\\\"power\\\":\\\"0\\\",\\\"sn\\\":\\\"FDO2351XXXX\\\",\\\"location_in_rack\\\":\\\ 2\\\",\\\"rack\\\":\\\"D13\\\",\\\"device_id\\\":\\\"ASW.XXXX- X.X\\\",\\\"ip\\\":\\\"10.66.XXX.XX\\\",\\\"idc\\\":\\\"AMTEXXXX\\\",\\\"index\\\":\\\"2\ ",\\\"weight\\\":\\\"0\\\",\\\"pair\\\":\\\"true\\\",\\\"room\\\":\\\"A3- 4\\\",\\\"is_ops_with_vm\\\":\\\"N/A\\\",\\\"pod_id\\\":\\\"ASW.XXXX-X\\\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"\"\"",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

##### 7.1.5.6 GetNetworkMachineByName

Queries network device information based on device names.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/cmdb/machines/getNetworkMachineByName HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | No | 15 | The number of entries per page. |
| pageNum | Integ er | Query | No | 1 | The page number. |
| name | Strin g | Query | No | OSW-XX-4-XX-S- 1.AMTESTXXXX | The device name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | System error | The error message. |
| result | String | success | Indicates whether the request was successful. Valid values: success. failed. |
| responseCode | String | 200 | The response code. The status code 200 indicates that the request was successful. The status code 500 indicates that the request failed. |
| errorMsg | String | "" | The error message. An empty string is returned if the request is successful. |
| errorDetail | String | "" | The error details. An empty string is returned if the request is successful. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | String | [{\"stack\":\"false\" ,\"role\":\"OSWS\",\ "expected link\":\"- _ startport:\ name: GigabitEtherneXXX X\ speed: \\\"1000\\\"\ endport:\ name: GigabitEthernXXXX \ speed: \\\"1000\\\"\ enddevice: OMR- XX-X-E11- 1.AMTEXXXX\- startport:\ name: GigabitEtherneXXX X\ speed: \\\"1000\\\"\ endport:\ name: GigabitEtherneXXX X\ speed: \\\"1000\\\"\ enddevice: OMR- XX-4-EXX- 2.AMTEXXXX\\",\"d evice type\":\"netw _ ork device\",\"dock _ er config\":\"\",\"do _ cker version\":\"\",\ _ "rack unit id\":\"\", _ _ \"host type\":\"net _ work device\",\"Tia _ njiCluster\":\"amte XXXX\",\"manufact urer\":\"Cisco\",\"ho stname\":\"OSW- XX-4-EXX-S- 1.AMTEXXXX\",\"np od id\":\"\",\"model _ \":\"WS-C2960XR- 48TS- I\",\"power\":\"0\",\" sn\":\"FDO2351F0G B\",\"location in ra _ _ ck\":\"40\",\"rack\": \"E12\",\"device id\ _ ":\"OSWS- 1\",\"ip\":\"10.66.X X.XX\",\"idc\":\"AM TEXXXX\",\"index\": \"1\",\"weight\":\"0\ ",\"pair\":\"false\",\" room\":\"A3- 4\",\"is ops with v _ _ _ m\":\"N/A\",\"pod i _ d\":\"\"}] | The response. |
| pageSize | Integer | 15 | The number of entries per page. |
| pageNum | Integer | 1 | The page number. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| totalRows | Long | 1 | The total number of entries returned. |
| return subCod _ e | String | "" | The error subcode. An empty string indicates that the request was successful. The subcode 500 indicates that the request failed. |
| return subMsg _ | String | "" | The error subcode message. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| cost | Long | 63 | The response time. Unit: milliseconds. |
| message | String | "" | The error message. An empty string is returned if the request is successful. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | "" | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |
| requestId | String | ab05b875-165f- 43c1-ba0a- 83b973201800 | The request ID. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/cmdb/machines/getNetworkMachineByName HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "return_subCode":"\"\"",
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "code":"200",
 "cost":63,
 "data":"
[{\\\"stack\\\":\\\"false\\\",\\\"role\\\":\\\"OSWS\\\",\\\"expected_link\\\":\\\"- sta rtport:\\ name: GigabitEtherneXXXX\\ speed: \\\\\\\"1000\\\\\\\"\\ endport:\\ name: Gig abitEthernXXXX\\ speed: \\\\\\\"1000\\\\\\\"\\ enddevice: OMR-XX-X-E11-1.AMTEXXXX\\- st artport:\\ name: GigabitEtherneXXXX\\ speed: \\\\\\\"1000\\\\\\\"\\ endport:\\ name: Gi gabitEtherneXXXX\\ speed: \\\\\\\"1000\\\\\\\"\\ enddevice: OMR-XX-4-EXX- 2.AMTEXXXX\\\\\",\\\"device_type\\\":\\\"network_device\\\",\\\"docker_config\\\":\\\"\\\ \\\"docker_version\\\":\\\"\\\",\\\"rack_unit_id\\\":\\\"\\\",\\\"host_type\\\":\\\"netwo _device\\\",\\\"TianjiCluster\\\":\\\"amteXXXX\\\",\\\"manufacturer\\\":\\\"Cisco\\\",\\\ ostname\\\":\\\"OSW-XX-4-EXX-S- 1.AMTEXXXX\\\",\\\"npod_id\\\":\\\"\\\",\\\"model\\\":\\\"WS-C2960XR-48TS- I\\\",\\\"power\\\":\\\"0\\\",\\\"sn\\\":\\\"FDO2351F0GB\\\",\\\"location_in_rack\\\":\\\ 0\\\",\\\"rack\\\":\\\"E12\\\",\\\"device_id\\\":\\\"OSWS- 1\\\",\\\"ip\\\":\\\"10.66.XX.XX\\\",\\\"idc\\\":\\\"AMTEXXXX\\\",\\\"index\\\":\\\"1\\\" \\"weight\\\":\\\"0\\\",\\\"pair\\\":\\\"false\\\",\\\"room\\\":\\\"A3- 4\\\",\\\"is_ops_with_vm\\\":\\\"N/A\\\",\\\"pod_id\\\":\\\"\\\"}]",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "pageSize":15,
 "totalRows":1,
 "message":"\"\"",
 "pageNum":1,
 "responseCode":"200",
 "errorMsg":"\"\"",
 "result":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"\"\"",
 "responseVersion":"v1",
 "success":true,
 "errorTitle":"Service error",
 "requestId":"ab05b875-165f-43c1-ba0a-83b973201800",
 "return_subMsg":"\"\"",
 "errorDetail":"\"\""
```

`}`

#### 7.1.6 Platform data

##### 7.1.6.1 GetCurrentUserStats

Queries the login user statistics of Apsara Uni-manager Operations Console.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| aliyun lan _ g | Strin g | Header | No | zh | The language code. Valid values: zh: Chinese. en: English. |
| aliyun ter _ ritory | Strin g | Header | No | CN | The country and region code. Valid values: CN (can be specified only when aliyun lang _ is set to zh). US (can be specified only when aliyun lang _ is set to en). TW (can be specified only when aliyun lang _ is set to zh). |

**Request syntax**

```
GET /openapi/popResource/aso/auth/user/getCurrentUserStats HTTP/1.1
```

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | ASO ASMGR SYST _ _ EM ERROR _ | The error code. |
| errorMessage | String | System error | The error message. |
| data | Array of AsoUserStat |   | The response. |
| username | String | admin | The username. |
| loginName | String | admin | The logon name. |

| psara Uni-manag | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| lastLoginTime | Long | 1654596285000 | The last logon time. |
| sessionInfoList | Array of SessionInfo |   | The information about users who are in the valid logon state. |
| loginTime | Long | 1654589231158 | The time when the user logged on. |
| cost | Long | 30 | The response time. Unit: milliseconds. |
| code | String | 200 | The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| successRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| requestId | String | 37d50d06-2089- 48d6-ad02- f3cb6009a2af | The request ID. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| key | String | "" | The keyword of the error. |
| level | String | "" | The error level. |
| eagleEyeTrace Id | String | 0ab408f41680511 2341264295d00c9 | The EagleEye ID. |
| serverRole | String | aso-mgr.asmgr# | The service role. |
| path | String | /aso/auth/user/ope napi/getCurrentUse rStats | The URL of the API. |
| responseVersi on | String | v1 | The version of the response format. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. Valid values: true. false. |
| errorTitle | String | Service error | The title of the error message. |

**Examples**

Sample requests

```
GET /openapi/popResource/aso/auth/user/getCurrentUserStats HTTP/1.1
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0ab408f416805112341264295d00c9",
 "cost":30,
 "code":"200",
 "data":{
  "lastLoginTime":1654596285000,
  "loginName":"admin",
  "sessionInfoList":{
   "loginTime":1654589231158
```

`},`

```json
  "username":"admin"
```

`},`

```json
 "level":"\"\"",
 "errorMessage":"System error",
 "errorCode":"ASO_ASMGR_SYSTEM_ERROR",
 "message":"success",
 "successResponse":true,
 "serverRole":"aso-mgr.asmgr#",
 "path":"/aso/auth/user/openapi/getCurrentUserStats",
 "responseVersion":"v1",
 "requestId":"37d50d06-2089-48d6-ad02-f3cb6009a2af",
 "success":true,
 "errorTitle":"Service error",
 "key":"\"\""
```

`}`

##### 7.1.6.2 ListUsers

Queries a list of users.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| name | Strin g | Query | No | test | The username, which can be used for fuzzy search. |
| pageSize | Integ er | Query | Yes | 15 | The number of entries per page. |
| lock | Boole an | Query | Yes | false | Specifies whether to move the user to the recycle bin. |
| currentPa ge | Integ er | Query | Yes | 1 | The page number. |
| role | Strin g | Query | No | Product DevOps personnel | The name of the role. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| deptName | Strin g | Query | No | root-dept | The organization name. If you leave this parameter and the name parameter empty, all users in your department are returned. If you set this parameter to root-dept and leave the name parameter empty, all users are returned. If you set this parameter to a specific department but leave the name parameter empty, all users in the specified department are returned. If you specify both this parameter and the name parameter, users who meet the fuzzy search conditions are returned. If you leave this parameter empty but specify the name parameter, users who meet the fuzzy search conditions in your department are returned. If you set this parameter to root-dept and specify the name parameter, users who meet the fuzzy search conditions in all departments are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. Valid values: |
| data | Struct |   | The response data. |
| items | Array of user |   | The users. |
| roles | Array of role |   | The roles. |
| roleName | String | Product DevOps personnel | The name of the role. |
| aliuid | String | 165238201113541 2 | The account ID. |
| parentAliuid | String | 140688221715314 3 | The ID of the Alibaba Cloud account. If the current account is an Alibaba Cloud account, this parameter is empty. If the current account is a RAM user, the value is the ID of the Alibaba Cloud account to which the RAM user belongs. |
| name | String | opsadmin | The username. |
| fullName | String | fullname 1682303 _ 525103 | The display name. |
| departmentId | Integer | 1 | The ID of the department. |
| deptName | String | root-dept | The name of the department. |
| telephone | String | 19500000000 | The phone number. |
| email | String | asotest@alibaba- inc.com | The email address. |
| loginTime | String | 1682319987000 | The time when the user logged on. |
| status | String | ACTIVE | The state of the user. |
| ruleName | String | default rule _ | The logon policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| userExternalId | String | "" | The foreign key ID of the user, which is used for Identity-as-a-Service (IDaaS) scenarios. |
| deptExternalId | String | "" | The foreign key ID of the department, which is used for IDaaS scenarios. |
| createTime | String | 2023-04-21 01:18:55 | The time when the user was created. |
| page | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number. |
| pageSize | Integer | 15 | The number of entries per page. |
| total | Long | 20 | The total number of entries returned. |
| totalPage | Long | 2 | The total number of pages returned. |
| cost | Long | 74 | The response time. Unit: milliseconds. |
| path | String | /aso/auth/user/ope napi/listUsers | The request path. |
| serverRole | String | "" | The name of the service that was accessed. |
| responseVersi on | String | v1 | The version of the response. |
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The title of the error message. |
| errorMessage | String | "" | The error message. |
| requestId | String | 8ae2a476-52b1- 4bac-98c4- 4ca17671482a | The request ID. |
| eagleEyeTrace Id | String | "" | The EagleEye ID, which is used as a trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &pageSize=20 &lock=false &currentPage=1 &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "serverRole":"\"\"",
 "path":"/aso/auth/user/openapi/listUsers",
 "eagleEyeTraceId":"\"\"",
 "cost":74,
 "responseVersion":"v1",
 "data":{
  "page":{
   "total":20,
   "totalPage":2,
   "pageSize":15,
   "currentPage":1
```

`},`

```json
  "items":{
   "deptName":"root-dept",
   "deptExternalId":"\"\"",
   "roles":{
    "roleName":"Product DevOps personnel"
```

`},`

```json
   "departmentId":1,
   "fullName":"fullname_1682303525103",
   "parentAliuid":"1406882217153143",
   "telephone":"19500000000",
   "loginTime":"1682319987000",
   "createTime":"2023-04-21 01:18:55",
   "name":"opsadmin",
   "ruleName":"default_rule",
   "userExternalId":"\"\"",
   "aliuid":"1652382011135412",
   "email":"a***@alibaba-inc.com",
   "status":"ACTIVE"
```

`}` `},`

```json
 "success":true,
 "errorTitle":"\"\"",
 "requestId":"8ae2a476-52b1-4bac-98c4-4ca17671482a",
 "errorMessage":"\"\"",
 "errorCode":"\"\""
```

`}`

### 7.2 Network Operations Console

#### 7.2.1 Network element management

##### 7.2.1.1 GetSwitchInfo

Queries switch information.

**Request parameters**

**q**

**p**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetSwitchInfo | The operation that you want to perform. Set the value to GetSwitchInfo. |
| ip | String | Yes | 10.205.XX.XX | The IP address of the switch. |
| OpsProduct | String | No | NrmOps | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array of JSONArray |   | The details of the switch. |
| GmtCreate | Long | 1654593453 | The timestamp that specifies when the entry was created. |
| HostName | String | ASW-XX-XX-XXXX | The SYSNAME of the switch. |
| IDC | String | amtestXXX | The data center. |
| IP | String | 10.205.XX.XX | The IP address of the switch. |
| LastUpdate | Long | 1654593453 | The timestamp that specifies when the entry was last updated. |
| Manufacturer | String | Huawei | The switch manufacturer. |
| Model | String | CEXX-XX-XXXX | The switch model. |
| PingConn | Integer | 1 | The ping connectivity. Valid values: 1: The network connectivity is normal. -1: The network connectivity is abnormal. |
| Role | String | ASW | The service role of the switch. |
| SN | String | 210XXXXXXXXX | The serial number (SN) of the switch. The SNs of two switches are returned in case of a switch stack. |

| SnmpConn | Integer | 1 | The SNMP connectivity. Valid values: 1: The network connectivity is normal. -1: The network connectivity is abnormal. |
|---|---|---|---|
| SoftwareRelea se | String | V10XXXXXXXXXX | The software release number of the switch. |
| SoftwareVersi on | String | 8.1XXX | The software version number of the switch. |
| UpTime | String | 2693524135 | The startup time of the main processing unit of the switch. |
| message | String | success | The message that indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSwitchInfo &ip=10.205.XX.XX &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Data>
    <LastUpdate>1654593453</LastUpdate>
    <IP>10.205.XX.XX</IP>
    <IDC>amtestXXX</IDC>
    <SoftwareRelease>V10XXXXXXXXXX</SoftwareRelease>
    <Role>ASW</Role>
    <PingConn>1</PingConn>
    <GmtCreate>1654593453</GmtCreate>
    <SoftwareVersion>8.1XXX</SoftwareVersion>
    <SnmpConn>1</SnmpConn>
    <UpTime>2693524135</UpTime>
    <Model>CEXX-XX-XXXX</Model>
    <Manufacturer>Huawei</Manufacturer>
    <SN>210XXXXXXXXX</SN>
    <HostName>ASW-XX-XX-XXXX</HostName>
</Data> <message>success</message>
```

`JSON` format `{`

```json
    "Data": {
        "LastUpdate": 1654593453,
        "IP": "10.205.XX.XX",
        "IDC": "amtestXXX",
        "SoftwareRelease": "V10XXXXXXXXXX",
        "Role": "ASW",
        "PingConn": 1,
        "GmtCreate": 1654593453,
        "SoftwareVersion": "8.1XXX",
        "SnmpConn": 1,
        "UpTime": 2693524135,
        "Model": "CEXX-XX-XXXX",
        "Manufacturer": "Huawei",
        "SN": "210XXXXXXXXX",
        "HostName": "ASW-XX-XX-XXXX"
```

`},`

```json
    "message": "success"
```

`}`

##### 7.2.1.2 GetTopoInfo

Queries network topology information.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTopoInfo | The operation that you want to perform. Set the value to GetTopoInfo. |
| idc | String | Yes | amtestXXX | The data center. |
| query type _ | String | No | base | The topology type. Valid values: base (default): reference topology. dynamic: real-time topology. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. |
| Data | Struct |   | The network topology information. |

| Edges | Array of JSONArray |   | The information about network topology edges. |
|---|---|---|---|
| Color | String | #ccc | The color of the network topology edge. |
| EdgeFrom | String | 10.205.XX.XX | The source device of the topology edge. |
| EdgeTo | String | 10.202.XX.XX | The destination device of the topology edge. |
| EndPort | String | FortyGigXXXXX | The port of the destination device of the topology edge. |
| ID | String | 256XXXXXXXXXXX | The hash value of the edge ID. |
| IDC | String | amtestXXX | The data center. |
| NodePair | String | 54XXXXXXXXXXXX | The hash value of the edge. Edges that have the same hash value are represented by a line. |
| StartPort | String | 40GE X/X/X | The port of the source device of the topology edge. |
| Groups | Struct |   | The node groups. |
| ASW | Struct |   | The ASW device group. |
| Image | String | /assets/bdm/ASW.p ng | The icon of the group. |
| Shape | String | image | The icon type. |
| CSW | Struct |   | The CSW device group. |
| Image | String | /assets/bdm/CSW.p ng | The icon of the group. |
| Shape | String | image | The icon type. |
| DSW | Struct |   | The DSW device group. |

| Image | String | /assets/bdm/DSW.p ng | The icon of the group. |
|---|---|---|---|
| Shape | String | image | The icon type. |
| HSW | Struct |   | The HSW device group. |
| Image | String | /assets/bdm/HSW.p ng | The icon of the group. |
| Shape | String | image | The icon type. |
| ISW | Struct |   | The ISW device group. |
| Image | String | /assets/bdm/ISW.p ng | The icon of the group. |
| Shape | String | image | The icon type. |
| LSW | Struct |   | The LSW device group. |
| Image | String | /assets/bdm/LSW.p ng | The icon of the group. |
| Shape | String | image | The icon type. |
| Nodes | Array of JSONArray |   | The topology nodes. |
| ID | String | 10.205.XX.XX | The element ID. |
| IDC | String | amtestXXX | The data center. |
| Label | String | ASW-XX-XX-XXXX | The element tag. |
| Name | String | ASW-XX-XX-XXXX | The element name. |
| NodeGroup | String | ASW | The group to which the node device belongs. The value depends on the icon that is used by the node device. |
| Pid | String | ["10.XX.XX. 01","10.XX.XX. 02" ] | The logical parent node ID of the device. This parameter takes effect only for DSW. |

| SubIDs | String | ["10.XX.XX. 03","10.XX.XX. 04" ] | The logical child node ID of the device. This parameter takes effect only for DSW. |
|---|---|---|---|
| X | String | -200 | The x-coordinate of the node. |
| Y | String | 500 | The y-coordinate of the node. |
| ErrMsg | String | ok | The message that indicates whether the request was successful. |
| ErrNo | String | 0 | The error code. |
| RequestId | String | 256XXXXXXXXXXX XXXXXXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| successRespo nse | String | true | Indicates whether the request was successful. Valid values: true and false. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetTopoInfo &idc=amtestXXX &<Common request parameters>
```

Sample success responses `XML` format

```xml
<successResponse>true</successResponse> <RequestId>256XXXXXXXXXXXXXXXXXXX</RequestId> <ErrMsg>ok</ErrMsg> <ErrNo>0</ErrNo> <Data>
    <Edges>
        <EdgeFrom>10.205.XX.XX</EdgeFrom>
        <NodePair>54XXXXXXXXXXXX</NodePair>
        <StartPort>40GE X/X/X</StartPort>
        <EndPort>FortyGigXXXXX</EndPort>
        <EdgeTo>10.202.XX.XX</EdgeTo>
        <Color>#ccc</Color>
        <IDC>amtestXXX</IDC>
        <ID>256XXXXXXXXXXX</ID>
    </Edges>
    <Nodes>
        <X>-200</X>
```

```xml
        <SubIDs>[ "10.XX.XX. 03","10.XX.XX. 04" ]</SubIDs>
        <Label>ASW-XX-XX-XXXX</Label>
        <Y>500</Y>
        <IDC>amtestXXX</IDC>
        <Pid>[ "10.XX.XX. 01","10.XX.XX. 02" ]</Pid>
        <ID>10.205.XX.XX</ID>
        <NodeGroup>ASW</NodeGroup>
        <Name>ASW-XX-XX-XXXX</Name>
    </Nodes>
    <Groups>
        <ASW>
            <Shape>image</Shape>
            <Image>/assets/bdm/ASW.png</Image>
        </ASW>
        <CSW>
            <Shape>image</Shape>
            <Image>/assets/bdm/CSW.png</Image>
        </CSW>
        <DSW>
            <Shape>image</Shape>
            <Image>/assets/bdm/DSW.png</Image>
        </DSW>
        <ISW>
            <Shape>image</Shape>
            <Image>/assets/bdm/ISW.png</Image>
        </ISW>
        <HSW>
            <Shape>image</Shape>
            <Image>/assets/bdm/HSW.png</Image>
        </HSW>
        <LSW>
            <Shape>image</Shape>
            <Image>/assets/bdm/LSW.png</Image>
        </LSW>
    </Groups>
</Data> <Code>200</Code> <Success>true</Success>
```

`JSON` format `{`

```json
    "successResponse": true,
    "RequestId": "256XXXXXXXXXXXXXXXXXXX",
    "ErrMsg": "ok",
    "ErrNo": 0,
    "Data": {
        "Edges": {
            "EdgeFrom": "10.205.XX.XX",
            "NodePair": "54XXXXXXXXXXXX",
            "StartPort": "40GE X/X/X",
            "EndPort": "FortyGigXXXXX",
            "EdgeTo": "10.202.XX.XX",
"Color":"#ccc"
```

```json
            Color: #ccc,
            "IDC": "amtestXXX",
            "ID": "256XXXXXXXXXXX"
```

`},`

```json
        "Nodes": {
            "X": -200,
            "SubIDs": "[ \"10.XX.XX.03\",\"10.XX.XX.04\" ]",
            "Label": "ASW-XX-XX-XXXX",
            "Y": 500,
            "IDC": "amtestXXX",
            "Pid": "[ \"10.XX.XX.01\",\"10.XX.XX.02\" ]",
            "ID": "10.205.XX.XX",
            "NodeGroup": "ASW",
            "Name": "ASW-XX-XX-XXXX"
```

`},`

```json
        "Groups": {
            "ASW": {
                "Shape": "image",
                "Image": "/assets/bdm/ASW.png"
```

`},`

```json
            "CSW": {
                "Shape": "image",
                "Image": "/assets/bdm/CSW.png"
```

`},`

```json
            "DSW": {
                "Shape": "image",
                "Image": "/assets/bdm/DSW.png"
```

`},`

```json
            "ISW": {
                "Shape": "image",
                "Image": "/assets/bdm/ISW.png"
```

`},`

```json
            "HSW": {
                "Shape": "image",
                "Image": "/assets/bdm/HSW.png"
```

`},`

```json
            "LSW": {
                "Shape": "image",
                "Image": "/assets/bdm/LSW.png"
```

`}` `}` `},`

```json
    "Code": 200,
    "Success": true
```

`}`

##### 7.2.1.3 ListPorts

Queries a list of device ports.

**Request parameters**

| 04 |   |   |   | > Document Version: 2025110 |
|---|---|---|---|---|

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListPorts | The operation that you want to perform. Set the value to ListPorts. |
| ip | String | Yes | 10.205.XX.XX | The IP address of the device. |
| OpsProduct | String | No | NrmOps | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array of JSONArray |   | The ports of the device. |
| EndDevice | String | d22i0XX.XXX.XX | The name of the peer device. |
| EndPort | String | ethX | The name of the peer port. |
| EndPortIfAlias | String | Link XXXXX-X _ | The description of the peer port. |
| GmtCreate | Long | 1654491059 | The timestamp that specifies when the entry was created. |
| IP | String | 10.205.XX.XX | The IP address of the network device to which the port belongs. |
| IfAdminStatus | String | 1 | The admin status of the port. Valid values: 1: UP. 2: DOWN. |
| IfAlias | String | Link XXXX-XX _ | The description of the port. |
| IfIndex | String | 10 | The interface index that was assigned to the port. |
| IfOperStatus | String | 1 | The operational status of the port. Valid values: 1: UP. 2: DOWN. |

| IfSpeed | String | 10000 | The data transfer rate on the port. |
|---|---|---|---|
| LastUpdate | Long | 1654593824 | The timestamp that specifies when the entry was last updated. |
| ifName | String | 10GEX/X/X | The port name. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListPorts &ip=10.205.XX.XX &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Data>
    <IfSpeed>10000</IfSpeed>
    <IfAdminStatus>1</IfAdminStatus>
    <EndPortIfAlias>Link_XXXXX-X</EndPortIfAlias>
    <GmtCreate>1654491059</GmtCreate>
    <EndDevice>d22i0XX.XXX.XX</EndDevice>
    <LastUpdate>1654593824</LastUpdate>
    <EndPort>ethX</EndPort>
    <IP>10.205.XX.XX</IP>
    <ifName>10GEX/X/X</ifName>
    <IfIndex>10</IfIndex>
    <IfAlias>Link_XXXX-XX</IfAlias>
    <IfOperStatus>1</IfOperStatus>
</Data> <message>success</message>
```

`JSON` format `{`

```json
    "Data": {
        "IfSpeed": 10000,
        "IfAdminStatus": 1,
        "EndPortIfAlias": "Link_XXXXX-X",
        "GmtCreate": 1654491059,
        "EndDevice": "d22i0XX.XXX.XX",
        "LastUpdate": 1654593824,
        "EndPort": "ethX",
        "IP": "10.205.XX.XX",
        "ifName": "10GEX/X/X",
        "IfIndex": 10,
        "IfAlias": "Link_XXXX-XX",
        "IfOperStatus": 1
```

`},`

```json
    "message": "success"
```

`}`

##### 7.2.1.4 ListSwTotal

Queries a list of switches.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSwTotal | The operation that you want to perform. Set the value to ListSwTotal. |
| idc | String | No | amtestXXX | The data center. Default value: None. You can select "all" or a specific data center. |
| OpsProduct | String | No | NrmOps | The product name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array of JSONArray |   | The list of switches. |
| GmtCreate | Long | 1653585092 | The timestamp that specifies when the entry was created. |
| HostName | String | ASW-XX-XX-XXXX | The SYSNAME of the switch. |

| IDC | String | amtestXXX | The data center. |
|---|---|---|---|
| IP | String | 10.205.XX,XX | The IP address of the switch. |
| LastUpdate | Long | 1654593453 | The timestamp that specifies when the entry was last updated. |
| Manufacturer | String | Huawei | The switch manufacturer. |
| Model | String | CEXX-XX-XXX | The switch model. |
| PingConn | Integer | 1 | The ping connectivity. Valid values: 1: The network connectivity is normal. -1: The network connectivity is abnormal. |
| Role | String | ASW | The service role of the switch. |
| SN | String | 210XXXXXXXXXXX XX | The serial number (SN) of the switch. The SNs of two switches are returned in case of a switch stack. |
| ScanSource | String | null | This parameter is no longer in use. |
| SnmpConn | Integer | 1 | The SNMP connectivity. Valid values: 1: The network connectivity is normal. -1: The network connectivity is abnormal. |
| SoftwareRelea se | String | V100XXXXXXXXXX XX | The software release number of the switch. |
| SoftwareVersi on | String | 8.XXXX | The software version number of the switch. |
| UpTime | String | 2693524135 | The startup time of the main processing unit of the switch. |
| message | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListSwTotal &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Data>
    <ScanSource>null</ScanSource>
    <LastUpdate>1654593453</LastUpdate>
    <IP>10.205.XX,XX</IP>
    <IDC>amtestXXX</IDC>
    <SoftwareRelease>V100XXXXXXXXXXXX</SoftwareRelease>
    <Role>ASW</Role>
    <PingConn>1</PingConn>
    <GmtCreate>1653585092</GmtCreate>
    <SoftwareVersion>8.XXXX</SoftwareVersion>
    <SnmpConn>1</SnmpConn>
    <UpTime>2693524135</UpTime>
    <Model>CEXX-XX-XXX</Model>
    <Manufacturer>Huawei</Manufacturer>
    <SN>210XXXXXXXXXXXXX</SN>
    <HostName>ASW-XX-XX-XXXX</HostName>
</Data> <message>success</message>
```

`JSON` format `{`

```json
    "Data": {
        "ScanSource": "null",
        "LastUpdate": 1654593453,
        "IP": "10.205.XX,XX",
        "IDC": "amtestXXX",
        "SoftwareRelease": "V100XXXXXXXXXXXX",
        "Role": "ASW",
        "PingConn": 1,
        "GmtCreate": 1653585092,
        "SoftwareVersion": "8.XXXX",
        "SnmpConn": 1,
        "UpTime": 2693524135,
        "Model": "CEXX-XX-XXX",
        "Manufacturer": "Huawei",
        "SN": "210XXXXXXXXXXXXX",
        "HostName": "ASW-XX-XX-XXXX"
```

`},`

```json
    "message": "success"
```

`}`

##### 7.2.1.5 GetPortInfo

Queries the port information of a network device.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetPortInfo | The operation that you want to perform. Set the value to GetPortInfo. |
| ip | String | Yes | 10.205.XX.XX | The IP address of the network device. |
| port | String | Yes | Ten- GigabitEthernet 1/0/1 | The port name of the network device. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The information about the network device port. |
| EndDevice | String | d22i0XX.XXX.X | The name of the peer device. |
| EndPort | String | ethX | The name of the peer port. |
| EndPortIfAlias | String | Link XXXXX-X _ | The description of the peer port. |
| GmtCreate | Long | 1654491059 | The timestamp that specifies when the entry was created. |
| IP | String | 10.205.XX.XX | The IP address of the network device to which the port belongs. |
| IfAdminStatus | String | 1 | The admin status of the port. Valid values: 1: UP. 2: DOWN. |
| IfAlias | String | Link XXXX-XX _ | The description of the port. |
| IfIndex | String | 100 | The interface index that was assigned to the port. |

| IfOperStatus | String | 1 | The operational status of the port. Valid values: 1: UP. 2: DOWN. |
|---|---|---|---|
| IfSpeed | String | 1000 | The data transfer rate on the port. |
| LastUpdate | Long | 1654593824 | The timestamp that specifies when the entry was last updated. |
| ifName | String | 10GEX/X/X | The port name. |
| Message | String | ok | The message that indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPortInfo &ip=10.205.XX,XX &port=Ten-GigabitEthernet1/0/1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>ok</Message> <Data>
    <IfSpeed>1000</IfSpeed>
    <IfAdminStatus>1</IfAdminStatus>
    <EndPortIfAlias>Link_XXXXX-X</EndPortIfAlias>
    <GmtCreate>1654491059</GmtCreate>
    <EndDevice>d22i0XX.XXX.X</EndDevice>
    <LastUpdate>1654593824</LastUpdate>
    <EndPort>ethX</EndPort>
    <IP>10.205.XX.XX</IP>
    <ifName>10GEX/X/X</ifName>
    <IfIndex>100</IfIndex>
    <IfAlias>Link_XXXX-XX</IfAlias>
    <IfOperStatus>1</IfOperStatus>
</Data>
```

`JSON` format `{`

```json
    "Message": "ok",
    "Data": {
        "IfSpeed": 1000,
        "IfAdminStatus": 1,
        "EndPortIfAlias": "Link_XXXXX-X",
        "GmtCreate": 1654491059,
        "EndDevice": "d22i0XX.XXX.X",
        "LastUpdate": 1654593824,
        "EndPort": "ethX",
        "IP": "10.205.XX.XX",
        "ifName": "10GEX/X/X",
        "IfIndex": 100,
        "IfAlias": "Link_XXXX-XX",
        "IfOperStatus": 1
```

`}` `}`

##### 7.2.1.6 GetXnetFlow

Queries the data transfer volume of a network device port.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetXnetFlow | The operation that you want to perform. Set the value to GetXnetFlow. |
| end time _ | Long | Yes | 1655894604 | The timestamp that specifies the end of the time range to query. |
| hostname | String | Yes | ASW-C4-3-AXXX | The SYSNAME of the network device. |
| info type _ | String | Yes | interface | The type of the data to query. The value is specified as interface. |
| item | String | Yes | 10GE1/0/6 | The port name of the network device. |
| start time _ | Long | Yes | 1655891004 | The timestamp that specifies the beginning of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Data | Array of JSONArray |   | The information about the network device port. |
|---|---|---|---|
| Array | Array of JSONArray |   | Details of the data transfer volume of the network device port. |
| TimeStamp | Long | 1655894040 | The timestamp that specifies the time when the data was returned. |
| Value | Long | 21808258 | The data transfer volume of the network device port. |
| Calc | Boolean | true | Indicates whether the returned data needs to be converted to rate. |
| Item | String | in discard _ | The metric of the data transfer volume. Valid values: in discard, in pps, in bps, _ _ _ in error, out discard, out pps, out bps, _ _ _ _ and out error. _ |
| Message | String | success | The message that indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetXnetFlow &end_time=1655894604 &hostname=ASW-C4-3-AXXX &info_type=interface &item=10GE1/0/6 &start_time=1655891004 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>success</Message> <Data>
    <Item>in_discard</Item>
    <Calc>true</Calc>
    <Array>
        <Value>21808258</Value>
        <TimeStamp>1655894040</TimeStamp>
    </Array>
</Data>
```

`JSON` format `{`

```json
    "Message": "success",
    "Data": {
        "Item": "in_discard",
        "Calc": true,
        "Array": {
            "Value": 21808258,
            "TimeStamp": 1655894040
```

`}` `}` `}`

##### 7.2.1.7 GetHardwareUtilization

Queries the CPU or memory utilization of a network device.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetHardwareUtil ization | The operation that you want to perform. Set the value to GetHardwareUtilization. |
| hardware | String | Yes | mem | The type of the hardware. Valid values: cpu: CPU. mem: memory. |
| hostname | String | Yes | ASW-XX-XX- XXXX | The SYSNAME of the network device. |
| ip | String | Yes | 10.205.XX.XX | The IP address of the network device. |
| start time _ | Long | No | 1654593453 | The timestamp that specifies the beginning of the time range to query. |
| end time _ | Long | No | 1654598453 | The timestamp that specifies the end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |

| Data | Array of JSONArray |   | The information about the hardware utilization. |
|---|---|---|---|
| Item | String | CPU CE6XXX- _ 48S6Q-HI.X | The hardware model. |
| Utiliz | String | 28 | The hardware utilization. |
| Message | String | success | The message that indicates whether the request was successful. |
| SuccessRespo nse | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetHardwareUtilization &hardware=mem &hostname=ASW-XX-XX-XXXX &ip=10.205.XX.XX &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SuccessResponse>true</SuccessResponse> <Message>success</Message> <Data>
    <Item>CPU_CE6XXX-48S6Q-HI.X</Item>
    <Utiliz>28</Utiliz>
</Data> <Code>200</Code>
```

`JSON` format `{`

```json
    "SuccessResponse": true,
    "Message": "success",
    "Data": {
        "Item": "CPU_CE6XXX-48S6Q-HI.X",
        "Utiliz": 28
```

`},`

```json
    "Code": 200
```

`}`

##### 7.2.1.8 GetPortTransPowerByName

Queries the optical RX/TX power of a network device port.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetPortTransPo werByName | The operation that you want to perform. Set the value to GetPortTransPowerByName. |
| IP | String | Yes | 10.205.XX.XX | The IP address of the network device. |
| Port | String | Yes | 10GEI/X/X | The port name of the network device. |
| StartTime | Long | No | 1655604751 | The timestamp that specifies the beginning of the time range to query. |
| EndTime | Long | No | 1655608351 | The timestamp that specifies the end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The information about the optical RX/TX power of the network device port. |
| IP | String | 10.205.XX.XX | The IP address of the network device. |
| IfIndex | String | 16850178 | The interface index that was assigned to the port. |
| Port | String | 10GEI/X/X | The port name of the network device. |
| Timestamps | List | ["1655607000","16 55607060","16556 07060"] | The timestamps. |
| TransceiverCu rRXPower | List | ["-220","-220","- 223"] | The optical RX power data. |
| TransceiverCu rTXPower | List | ["-261","-259","- 259"] | The optical TX power data. |
| Message | String | ok | The message that indicates whether the request was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPortTransPowerByName &IP=10.205.XX.XX &Port=10GEI/X/X &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Message>ok</Message> <Data>
    <Port>10GEI/X/X</Port>
    <IP>10.205.XX.XX</IP>
    <IfIndex>16850178</IfIndex>
    <TransceiverCurRXPower>["-220","-220","-223"]</TransceiverCurRXPower>
    <TransceiverCurTXPower>["-261","-259","-259"]</TransceiverCurTXPower>
    <Timestamps>["1655607000","1655607060","1655607060"]</Timestamps>
</Data>
```

`JSON` format `{`

```json
    "Message": "ok",
    "Data": {
        "Port": "10GEI/X/X",
        "IP": "10.205.XX.XX",
        "IfIndex": 16850178,
        "TransceiverCurRXPower": "[\"-220\",\"-220\",\"-223\"]",
        "TransceiverCurTXPower": "[\"-261\",\"-259\",\"-259\"]",
        "Timestamps": "[\"1655607000\",\"1655607060\",\"1655607060\"]"
```

`}` `}`

#### 7.2.2 Networking services

##### 7.2.2.1 AllSlbClusters

Queries a list of Server Load Balancer (SLB) clusters or SLB proxy clusters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Service | Strin g | Query | No | slb-lvs | The service name. Valid values: slb-lvs: SLB cluster. slb-proxy: SLB proxy cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Map | {"slbCluster-A- XXXXXXX- XXXX":"slbCluster- B-XXXXXXX- XXXX"} | The clusters. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |

| psara Uni-manag Console | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AllSlbClusters &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists. ",
 "ErrNo":"0",
 "Data":{
  "slbCluster-A-XXXXXXX-XXXX":"slbCluster-B-XXXXXXX-XXXX"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.2 GetNodeList

Queries a node list of a Server Load Balancer (SLB) cluster or an SLB proxy cluster.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | Yes | slbCluster-A-XXXXXXX | The name of the SLB cluster or SLB proxy cluster. Set this parameter to the value returned by the AllSlbClusters operation. |
| Service | Strin g | Query | No | slb-lvs | The service name. Valid values: slb-lvs: SLB cluster. slb-proxy: SLB proxy cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The custom response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Array of TestListModel |   | The nodes. |
| enabled | Integer | 1 | The status of the node. Valid values: 1: enabled. 0: disabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| gmt create _ | Long | 1681179099000 | The timestamp that indicates when the node was created. |
| gmt modify _ | Long | 1681179205000 | The timestamp that indicates when the information about the node was updated. |
| id | Integer | 12 | The node ID. |
| instance id _ | String | lvsNode-XXXXXX | The instance ID. |
| ip addr _ | String | 10.XX.XX.X | The host IP address of the node. |
| laddr | String | 10.XX.XX.XX/25 | The CIDR block of the node. |
| service enable _ d | String | disabled | The service status of the node. |
| status | String | online | The status of the node. |
| Ip | String | 10.XX.XX.X | The service IP address of the node. |
| MachineState | String | good | The status of the host. |
| Hostname | String | c27b0XXXX.XXX | The hostname. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetNodeList &ClusterName=slbCluster-A-XXXXXXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "gmt_create":1681179099000,
  "laddr":"10.XX.XX.XX/25",
  "instance_id":"lvsNode-XXXXXX",
  "Ip":"10.XX.XX.X",
  "gmt_modify":1681179205000,
  "service_enabled":"disabled",
  "Hostname":"c27b0XXXX.XXX",
  "id":12,
  "ip_addr":"10.XX.XX.X",
  "enabled":1,
  "MachineState":"good",
  "status":"online"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.3 GetSlbLvsNodeStats

Queries the usage data of a Server Load Balancer (SLB) node.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterNa me | Strin g | Quer y | Yes | slbCluster-A-XXXXXXX | The SLB cluster name. Set this parameter to the value returned by the AllSlbClusters operation. |
|---|---|---|---|---|---|
| NodeIP | Strin g | Quer y | Yes | 1.XX.XX.X | The IP address of the node. The value is the value of the IPAddr parameter that is returned by the GetNodeList operation. |
| StartTime | Strin g | Quer y | No | 1681446655 | The timestamp that specifies the beginning of the time range to query. Default value: the timestamp 1 hour before the current time. |
| EndTime | Strin g | Quer y | No | 1685082869 | The timestamp that specifies the end of the time range to query. Default value: the timestamp of the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Struct |   | The usage data. |
| actConnsPS | List | [0,0,0,0,0] | The number of active connections. Unit: connections per seconds (CPS). |

| connsPS | List | [1,2,2,3,4] | The number of new connections. Unit: CPS. |
|---|---|---|---|
| dropConnPS | List | [0,0,0,0,0] | The number of dropped connections per second. Unit: CPS. |
| failConnPS | List | [1,2,2,3,4] | The number of failed connections per second. Unit: CPS. |
| inActConnPS | List | [1,2,2,3,4] | The number of inactive connections. Unit: CPS. |
| inBitsPS | List | [0,0,0,0,0] | The number of inbound bits per second. |
| inDBitesPS | List | [0,0,0,0,0] | The number of dropped inbound bits per second. |
| inDPktsPS | List | [0,0,0,0,0] | The number of dropped inbound packets per second. |
| inPktsPS | List | [0,0,0,0,0] | The number of inbound packets per second. |
| maxConnsPs | List | [0,0,0,0,0] | The total number of connections. Unit: CPS. |
| outBitsPS | List | [1,2,2,3,4] | The number of outbound bits per second. |
| outDBitesPS | List | [1,2,2,3,4] | The number of dropped outbound bits per second. |
| outDPktsPS | List | [0,0,0,0,0] | The number of dropped outbound packets per second. |
| outPktsPS | List | [0,0,0,0,0] | The number of outbound packets per second. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| Code | String | 200 | The response code. |

| Message | String | ok | The response message. |
|---|---|---|---|
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSlbLvsNodeStats &ClusterName=slbCluster-A-XXXXXXX &NodeIP=1.XX.XX.X &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "inDPktsPS":"[0,0,0,0,0]",
  "inPktsPS":"[0,0,0,0,0]",
  "inBitsPS":"[0,0,0,0,0]",
  "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
  "maxConnsPs":"[0,0,0,0,0]",
  "outPktsPS":"[0,0,0,0,0]",
  "inDBitesPS":"[0,0,0,0,0]",
  "outDBitesPS":"[1,2,2,3,4]",
  "outBitsPS":"[1,2,2,3,4]",
  "dropConnPS":"[0,0,0,0,0]",
  "actConnsPS":"[0,0,0,0,0]",
  "inActConnPS":"[1,2,2,3,4]",
  "connsPS":"[1,2,2,3,4]",
  "failConnPS":"[1,2,2,3,4]",
  "outDPktsPS":"[0,0,0,0,0]"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}` Nrm 2022-04-25

##### 7.2.2.4 GetSlbLvsClusterStats

Queries the usage data of a Server Load Balancer (SLB) cluster.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | Yes | slbCluster-A-XXXXXXX | The SLB cluster name. Set this parameter to the value returned by the AllSlbClusters operation. |
| StartTime | Strin g | Query | No | 1681446655 | The timestamp that specifies the beginning of the time range to query. Default value: the timestamp 1 hour before the current time. |
| EndTime | Strin g | Query | No | 1681446655 | The timestamp that specifies the end of the time range to query. Default value: the timestamp of the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Struct |   | The usage data. |
| aclDBitsPS | List | [1,2,2,3,4] | The number of bits that were blocked by access control lists (ACLs) per second. |
| aclDPktsPS | List | [1,2,2,3,4] | The number of packets blocked by ACLs per second. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| actConnsPS | List | [0,0,0,0,0] | The number of active connections. Unit: connections per seconds (CPS). |
| connsPS | List | [1,2,2,3,4] | The number of new connections. Unit: CPS. |
| dropConnPS | List | [0,0,0,0,0] | The number of dropped connections per second. Unit: CPS. |
| failConnPS | List | [1,2,2,3,4] | The number of failed connections per second. Unit: CPS. |
| inActConnPS | List | [1,2,2,3,4] | The number of inactive connections. Unit: CPS. |
| inBitsPS | List | [0,0,0,0,0] | The number of inbound bits per second. |
| inDBitesPS | List | [0,0,0,0,0] | The number of dropped inbound bits per second. |
| inDPktsPS | List | [0,0,0,0,0] | The number of dropped inbound packets per second. |
| inPktsPS | List | [0,0,0,0,0] | The number of inbound packets per second. |
| maxConnsPs | List | [0,0,0,0,0] | The total number of connections. Unit: CPS. |
| outBitsPS | List | [1,2,2,3,4] | The number of outbound bits per second. |
| outDBitesPS | List | [1,2,2,3,4] | The number of dropped outbound bits per second. |
| outDPktsPS | List | [0,0,0,0,0] | The number of dropped outbound packets per second. |
| outPktsPS | List | [0,0,0,0,0] | The number of outbound packets per second. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSlbLvsClusterStats &ClusterName=slbCluster-A-XXXXXXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "inDPktsPS":"[0,0,0,0,0]",
  "inPktsPS":"[0,0,0,0,0]",
  "inBitsPS":"[0,0,0,0,0]",
  "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
  "maxConnsPs":"[0,0,0,0,0]",
  "aclDBitsPS":"[1,2,2,3,4]",
  "outPktsPS":"[0,0,0,0,0]",
  "inDBitesPS":"[0,0,0,0,0]",
  "outDBitesPS":"[1,2,2,3,4]",
  "outBitsPS":"[1,2,2,3,4]",
  "dropConnPS":"[0,0,0,0,0]",
  "aclDPktsPS":"[1,2,2,3,4]",
  "actConnsPS":"[0,0,0,0,0]",
  "inActConnPS":"[1,2,2,3,4]",
  "connsPS":"[1,2,2,3,4]",
  "failConnPS":"[1,2,2,3,4]",
  "outDPktsPS":"[0,0,0,0,0]"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.5 GetLbStats

Queries the usage data of a Server Load Balancer (SLB) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | Yes | slbCluster-A-XXXXXXX | The SLB cluster name. Set this parameter to the value returned by the AllSlbClusters operation. |
| LbIndex | Strin g | Query | Yes | 1.XX.XX.X | The ID or virtual IP address of the instance. |
| StartTime | Long | Query | No | 1681446655 | The timestamp that specifies the beginning of the time range to query. Default value: the timestamp 1 hour before the current time. |
| EndTime | Long | Query | No | 1681446655 | The timestamp that specifies the end of the time range to query. Default value: the timestamp of the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Array of TestListModel |   | The usage data. |
| Array | Struct |   | The usage data. |
| actConnsPS | List | [0,0,0,0,0] | The number of active connections. Unit: connections per seconds (CPS). |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| connsPS | List | [1,2,2,3,4] | The number of new connections. Unit: CPS. |
| dropConnPS | List | [0,0,0,0,0] | The number of dropped connections per second. Unit: CPS. |
| failConnPS | List | [1,2,2,3,4] | The number of failed connections per second. Unit: CPS. |
| inActConnPS | List | [1,2,2,3,4] | The number of inactive connections. Unit: CPS. |
| inBitsPS | List | [0,0,0,0,0] | The number of inbound bits per second. |
| inDBitesPS | List | [0,0,0,0,0] | The number of dropped inbound bits per second. |
| inDPktsPS | List | [0,0,0,0,0] | The number of dropped inbound packets per second. |
| inPktsPS | List | [0,0,0,0,0] | The number of inbound packets per second. |
| maxConnsPs | List | [0,0,0,0,0] | The total number of connections. Unit: CPS. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| outBitsPS | List | [1,2,2,3,4] | The number of outbound bits per second. |
| outDBitesPS | List | [1,2,2,3,4] | The number of dropped outbound bits per second. |
| outDPktsPS | List | [0,0,0,0,0] | The number of dropped outbound packets per second. |
| outPktsPS | List | [0,0,0,0,0] | The number of outbound packets per second. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Protocol | String | tcp | The protocol. |
| Port | String | 80 | The port number. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The EagleEye ID. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetLbStats &ClusterName=slbCluster-A-XXXXXXX &LbIndex=1.XX.XX.X &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "Array":{
   "inDPktsPS":"[0,0,0,0,0]",
   "inPktsPS":"[0,0,0,0,0]",
   "inBitsPS":"[0,0,0,0,0]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "maxConnsPs":"[0,0,0,0,0]",
   "outPktsPS":"[0,0,0,0,0]",
   "inDBitesPS":"[0,0,0,0,0]",
   "outDBitesPS":"[1,2,2,3,4]",
   "outBitsPS":"[1,2,2,3,4]",
   "dropConnPS":"[0,0,0,0,0]",
   "actConnsPS":"[0,0,0,0,0]",
   "inActConnPS":"[1,2,2,3,4]",
   "connsPS":"[1,2,2,3,4]",
   "failConnPS":"[1,2,2,3,4]",
   "outDPktsPS":"[0,0,0,0,0]"
```

`},`

```json
  "Port":"80",
  "Protocol":"tcp"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.6 GetSlbProxyClusterStats

Queries the usage data of a Server Load Balancer (SLB) proxy cluster.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | Yes | slbCluster-A-XXXXXXX | The SLB cluster name. Set this parameter to the value returned by the AllSlbClusters operation. |
| StartTime | Strin g | Query | No | 1681446655 | The timestamp that specifies the beginning of the time range to query. Default value: the timestamp 1 hour before the current time. |
| EndTime | Strin g | Query | No | 1681446655 | The timestamp that specifies the end of the time range to query. Default value: the timestamp of the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Struct |   | The usage data. |
| ClusterName | String | slbCluster-A- XXXXXXX | The cluster name. |
| Info | Struct |   | The usage data. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| handleps | List | [0,0,0,0,0] | The average number of processed connections. |
| httpqps | List | [2.3,2.4,2.4] | The number of HTTP requests processed per second. |
| qps | List | [0,0,0,0,0] | The number of requests processed per second. |
| read | List | [0,0,0,0,0] | The number of connections created for read requests. |
| reqs | List | [0,0,0,0,0] | The total number of generated requests. |
| rt | List | [0,0,0,0,0] | The average response time. Unit: ms. The value is calculated based on the following formula: (request time[x] - _ request time[x-1])/(requests[x] - _ requests[x-1]). |
| spdyps | List | [1,2,2,3,4] | The number of SPDY requests processed per second. |
| sslf | List | [0,0,0,0,0] | The number of failed SSL connections. |
| sslhst | List | [2.3,2.4,2.4] | The average SSL handshake time. Unit: ms. |
| sslqps | List | [0,0,0,0,0] | The number of SSL requests processed per second. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| sslv3f | List | [2.3,2.4,2.4] | The number of failed SSLv3 connections. |
| wait | List | [1,2,2,3,4] | The number of queued persistent connections. |
| write | List | [2.0,2.0,2.0] | The number of connections that wrote response data to users. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| accept | List | [1,2,2,3,4] | The total number of new connections received. |
| active | List | [0,0,0,0,0] | The number of times that connections were initiated per second. |
| cps | List | [0,0,0,0,0] | The average number of connections received per second. |
| count | List | [1,2,2,3,4] | The total number of connections. |
| h2qps | List | [2.3,2.4,2.4] | The number of HTTP2 requests processed per second. |
| handle | List | [1,2,2,3,4] | The total number of processed connections. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSlbProxyClusterStats &ClusterName=slbCluster-A-XXXXXXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "ClusterName":"slbCluster-A-XXXXXXX",
  "Info":{
   "reqs":"[0,0,0,0,0]",
   "rt":"[0,0,0,0,0]",
   "wait":"[1,2,2,3,4]",
   "read":"[0,0,0,0,0]",
   "spdyps":"[1,2,2,3,4]",
   "cps":"[0,0,0,0,0]",
   "count":"[1,2,2,3,4]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "active":"[0,0,0,0,0]",
   "handle":"[1,2,2,3,4]",
   "sslf":"[0,0,0,0,0]",
   "sslqps":"[0,0,0,0,0]",
   "accept":"[1,2,2,3,4]",
   "handleps":"[0,0,0,0,0]",
   "qps":"[0,0,0,0,0]",
   "sslhst":"[2.3,2.4,2.4]",
   "sslv3f":"[2.3,2.4,2.4]",
   "h2qps":"[2.3,2.4,2.4]",
   "httpqps":"[2.3,2.4,2.4]",
   "write":"[2.0,2.0,2.0]"
```

`}` `},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.7 GetSlbProxyNodeStats

Queries the usage data of a Server Load Balancer (SLB) proxy node.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Quer y | Yes | slbCluster-A-XXXXXXX | The SLB cluster name. |
| Hostname | Strin g | Quer y | Yes | c27b0XXXXXXXX | The hostname of the node. The value is the value of the Hostname field that is returned by the GetNodeList operation. |
| StartTime | Strin g | Quer y | No. | 1681446655 | The timestamp that specifies the beginning of the time range to query. Default value: the timestamp 1 hour before the current time. |
| EndTime | Strin g | Quer y | No. | 1681446655 | The timestamp that specifies the end of the time range to query. Default value: the timestamp of the current time. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The custom response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |

| Data | Struct |   | The usage data. |
|---|---|---|---|
| slb proxy cpu _ _ | Struct |   | The CPU usage data. |
| hirq | List | [2.3,2.4,2.4] | The percentage of the time that the CPU spent processing hardware interrupt requests. |
| sirq | List | [2.3,2.4,2.4] | The percentage of time that the CPU spent processing software interrupt requests. |
| sys | List | [1.1,1.2] | The percentage of time during which the CPU ran in kernel mode. A high value indicates that bottlenecks existed in the system. A low value indicates high CPU performance. |
| user | List | [1.1,1.2] | The percentage of time that the CPU spent executing user processes. A high value indicates high CPU performance. |
| util | List | [2.0,2.0,2.0] | The memory utilization. |
| wait | List | [2.3,2.4,2.4] | The number of queued persistent connections. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| slb proxy disk _ _ io | Struct |   | The disk usage data. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| await | List | [2.0,2.0,2.0] | The average amount of time that was consumed to send I/O requests to the serving device. Unit: milliseconds. The value is the sum of the time that was consumed to handle the requests in the queue and the time that was consumed to serve them. |

| qusize | List | [1.1,1.2] | The average queue length of requests sent to the device. |
|---|---|---|---|
| rqsize | List | [2.0,2.0,2.0] | The average size of requests sent to the device. Unit: sectors. |
| rrqms | List | [2.0,2.0,2.0] | The number of concurrent read requests sent to the device per second. |
| rs | List | [2.0,2.0,2.0] | The number of read requests sent to the device per second. |
| rsecs | List | [1.1,1.2] | The number of sectors read from the device per second. |
| svctm | List | [1.1,1.2] | The average amount of time that was consumed to serve I/O requests sent to the device. Unit: milliseconds. |
| util | List | [2.0,2.0,2.0] | The percentage of time that the CPU spent sending I/O requests to the device. This value shows the bandwidth utilization of the device. If the value is 100%, it indicates that the device is saturated. |
| wrqms | List | [2.0,2.0,2.0] | The number of concurrent write requests sent to the device per second. |
| ws | List | [2.0,2.0,2.0] | The number of write requests sent to the device per second. |
| wsecs | List | [1.1,1.2] | The number of sectors written to the device per second. |
| slb proxy load _ _ | Struct |   | The load usage data. |
| load1 | List | [1.1,1.2] | The average system loads over the previous minute. |
| load15 | List | [1.1,1.2] | The average system loads over the previous 15 minutes. |
| load5 | List | [1.1,1.2] | The average system loads over the previous 5 minutes. |

| plit | List | [1.1,1.2] | The number of active tasks in the system when the data point was collected. Completed tasks are not included. |
|---|---|---|---|
| runq | List | [1.1,1.2] | The number of tasks in the queue when the data point was collected. The value is the same as the value of the procs running field in /proc/stat. _ |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| slb proxy me _ _ m | Struct |   | The memory usage data. |
| Dirty | List | [1.1,1.2] | The size of data waiting to be written back to the disk. |
| SReclaimable | List | [1.1,1.2] | The slab memory that can be reclaimed. |
| Shmem | List | [1.1,1.2] | The size of shared memory that has been allocated. |
| Slab | List | [1.1,1.2] | The cache size of the kernel data structure. |
| Writeback | List | [1.1,1.2] | The size of data being written back. |
| buff | List | [1.1,1.2] | The size of memory consumed by buffers. |
| cach | List | [1.1,1.2] | The size of memory consumed by caches. The operating system stores frequently accessed data in caches for quick access. |
| free | List | [1.1,1.2] | The size of the idle physical memory. |
| total | List | [1.1,1.2] | The total memory size. |
| used | List | [1.1,1.2] | The size of consumed memory. |
| util | List | [1.1,1.2] | The memory utilization. |

| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|
| slb proxy qps _ _ | Struct |   | The QPS usage data. |
| accept | List | [1.1,1.2] | The total number of new connections received. |
| active | List | [1.1,1.2] | The number of active connections, including read, write, and waiting requests. |
| cps | List | [1.1,1.2] | The average number of connections received per second. |
| h2qps | List | [1.1,1.2] | The number of HTTP2 requests processed per second. |
| handle | List | [1.1,1.2] | The total number of processed connections. |
| handleps | List | [1.1,1.2] | The average number of processed connections. |
| httpqps | List | [1.1,1.2] | The number of HTTP requests processed per second. |
| qps | List | [1.1,1.2] | The number of requests processed per second. |
| read | List | [1.1,1.2] | The number of connections created for read requests. |
| reqs | List | [1.1,1.2] | The total number of generated requests. |
| rt | List | [1.1,1.2] | The average response time. Unit: ms. |
| spdyps | List | [1.1,1.2] | The number of SPDY requests processed per second. |
| sslf | List | [1.1,1.2] | The number of failed connections. |

| sslhst | List | [1.1,1.2] | The average SSL handshake time. Unit: ms. |
|---|---|---|---|
| sslqps | List | [1.1,1.2] | The number of SSL requests processed per second. |
| sslv3f | List | [1.1,1.2] | The number of failed SSLv3 connections. |
| wait | List | [1.1,1.2] | The number of queued persistent connections. |
| write | List | [1.1,1.2] | The number of connections that wrote response data to users. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| slb proxy tcp _ _ | Struct |   | The TCP connection data. |
| AtmpFa | List | [1.1,1.2] | The number of times that a connection failed to be initiated per second. For example, syn packets are discarded due to a full semi-connection queue. |
| CurrEs | List | [1.1,1.2] | The number of current TCP connections. |
| EstRes | List | [1.1,1.2] | The number of times that connections were reset per second. |
| active | List | [1.1,1.2] | The number of times that connections were initiated per second. |
| iseg | List | [1.1,1.2] | The number of inbound TCP segments per second. |
| lisove | List | [1.1,1.2] | The number of connections that were discarded due to a full listen accept queue. |
| outseg | List | [1.1,1.2] | The number of outbound TCP segments per second. |

| pasive | List | [1.1,1.2] | The number of times that connections were passively generated per second. |
|---|---|---|---|
| retran | List | [1.1,1.2] | The retransmission percentage, which is the total number of retransmitted TCP segments divided by the total number of sent TCP segments. |
| msTimestamp | List | ["1681446655000" ,"1681446713000", "1681446771000", "1681446829000", "1681446887000"] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSlbProxyNodeStats &ClusterName=slbCluster-A-XXXXXXX &Hostname=c27b0XXXXXXXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "slb_proxy_diskio":{
   "rs":"[2.0,2.0,2.0]",
   "svctm":"[1.1,1.2]",
   "util":"[2.0,2.0,2.0]",
   "rqsize":"[2.0,2.0,2.0]",
   "await":"[2.0,2.0,2.0]",
   "rsecs":"[1.1,1.2]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "wsecs":"[1.1,1.2]",
   "rrqms":"[2.0,2.0,2.0]",
   "ws":"[2.0,2.0,2.0]",
   "wrqms":"[2.0,2.0,2.0]",
   "qusize":"[1.1,1.2]"
```

`},`

```json
  "slb_proxy_cpu":{
   "hirq":"[2.3,2.4,2.4]",
   "sirq":"[2.3,2.4,2.4]",
   "wait":"[2.3,2.4,2.4]",
   "util":"[2.0,2.0,2.0]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "sys":"[1.1,1.2]",
   "user":"[1.1,1.2]"
```

`},`

```json
  "slb_proxy_load":{
   "plit":"[1.1,1.2]",
   "runq":"[1.1,1.2]",
```

```json
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "load5":"[1.1,1.2]",
   "load1":"[1.1,1.2]",
   "load15":"[1.1,1.2]"
```

`},`

```json
  "slb_proxy_tcp":{
   "lisove":"[1.1,1.2]",
   "retran":"[1.1,1.2]",
   "AtmpFa":"[1.1,1.2]",
   "EstRes":"[1.1,1.2]",
   "outseg":"[1.1,1.2]",
   "active":"[1.1,1.2]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "CurrEs":"[1.1,1.2]",
   "iseg":"[1.1,1.2]",
   "pasive":"[1.1,1.2]"
```

`},`

```json
  "slb_proxy_qps":{
   "reqs":"[1.1,1.2]",
   "rt":"[1.1,1.2]",
   "wait":"[1.1,1.2]",
   "read":"[1.1,1.2]",
   "spdyps":"[1.1,1.2]",
   "cps":"[1.1,1.2]",
   "active":"[1.1,1.2]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "handle":"[1.1,1.2]",
   "sslf":"[1.1,1.2]",
   "sslqps":"[1.1,1.2]",
   "accept":"[1.1,1.2]",
   "handleps":"[1.1,1.2]",
   "qps":"[1.1,1.2]",
   "sslhst":"[1.1,1.2]",
   "sslv3f":"[1.1,1.2]",
   "h2qps":"[1.1,1.2]",
   "httpqps":"[1.1,1.2]",
   "write":"[1.1,1.2]"
```

`},`

```json
  "slb_proxy_mem":{
   "SReclaimable":"[1.1,1.2]",
   "Shmem":"[1.1,1.2]",
   "total":"[1.1,1.2]",
   "Writeback":"[1.1,1.2]",
   "util":"[1.1,1.2]",
   "msTimestamp":"
[\"1681446655000\",\"1681446713000\",\"1681446771000\",\"1681446829000\",\"1681446887000\
```

`",`

```json
   "used":"[1.1,1.2]",
```

```json
   "free":"[1.1,1.2]",
   "Dirty":"[1.1,1.2]",
   "Slab":"[1.1,1.2]",
   "buff":"[1.1,1.2]",
   "cach":"[1.1,1.2]"
```

`}` `},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}` Nrm 2022-04-25

##### 7.2.2.8 GetXgwClusterList

Queries a list of extendable gateways.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ProductNa me | Strin g | Query | Yes | vpc | The service name. Set the value to vpc. |
| ClusterTy pe | Strin g | Query | No | xgw | The type of the cluster. Default value: xgw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Map | {"vpcAzoneCluster -A-XXXXXXX- XXXX":"vpcAzoneCl uster-B-XXXXXXX- XXXX"} | The clusters. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetXgwClusterList &ProductName=vpc &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "vpcAzoneCluster-A-XXXXXXX-XXXX":"vpcAzoneCluster-B-XXXXXXX-XXXX"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.9 GetXgwClusterAll

Queries the usage data of extendable gateways and their nodes.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Host | Strin g | Query | No | c27b02007.cloudXXXXX XXXXXX | The hostname of the node. You must specify this parameter when you query the usage data of the node. The value is the value of the Hostname parameter that is returned by the GetXgwMachineList operation. |
| ClusterTy pe | Strin g | Query | No | xgw | The type of the cluster. Default value: xgw. |
| StartTime | Long | Query | No. | 1681446655 | The timestamp that specifies the beginning of the time range to query. |
| EndTime | Long | Query | No. | 1681446655 | The timestamp that specifies the end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The custom response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Struct |   | The usage data. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TimeStamp | List | [1681446660000,1 681446720000,16 81446780000] | The time when the monitoring data was collected. The value is a UNIX timestamp. Unit: milliseconds. |
| PacketLossRat eIn | List | ["0","0","0"] | The number of dropped inbound packets per second. |
| PacketLossRat eOut | List | ["0","0","0"] | The number of dropped outbound packets per second. |
| PacketRateIn | List | ["51","68","70"] | The number of inbound packets per second. |
| PacketRateOut | List | ["46","58","61"] | The number of outbound packets per second. |
| OutByteRate | List | ["43416","51792"," 54904"] | The outbound bandwidth. Unit: bit/s. |
| InByteRate | List | ["49560","66968"," 64744"] | The inbound bandwidth. Unit: bit/s. |
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetXgwClusterAll &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "PacketLossRateIn":"[\"0\",\"0\",\"0\"]",
  "PacketLossRateOut":"[\"0\",\"0\",\"0\"]",
  "PacketRateOut":"[\"46\",\"58\",\"61\"]",
  "OutByteRate":"[\"43416\",\"51792\",\"54904\"]",
  "PacketRateIn":"[\"51\",\"68\",\"70\"]",
  "InByteRate":"[\"49560\",\"66968\",\"64744\"]",
  "TimeStamp":"[1681446660000,1681446720000,1681446780000]"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

##### 7.2.2.10 GetXgwMachineList

Queries a list of the nodes of extendable gateways.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | Strin g | Query | Yes | vpcAzoneCluster- AXXXXXXX | The name of the cluster. Set the value to the value returned by the GetXgwClusterList operation. |
| ClusterTy pe | Strin g | Query | No | xgw | The type of the cluster. Default value: xgw. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ErrMsg | String | success | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| ErrNo | String | 0 | The response code. |
| RequestId | String | 0ED8XXXX-XXXX- XXXX-XXXX | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| Data | Array of TestListModel |   | The clusters. |
| HostName | String | c27b0XXXXXXXXX XX | The hostname of the node. |
| IDC | String | amXXXX | The data center where the node is deployed. |
| IP | String | 10.XX.XX.X | The IP address of the node. |
| State | String | good | The status of the node. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. |
| Message | String | ok | The response message. |
| eagleEyeTrace Id | String | 0a421xxxxxxxxxxx xxxxxxxxxxxx | The EagleEye ID. |
| cost | Integer | 905 | The response time. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true and false. |
| requestURI | String | /slalink/fulllink/clas sic/XXXXXX | The URL of the request. |
| serviceRole | String | baseXXXXX.baseX XXXXXX.XXXX# | The service role. |
| responseVersi on | String | v1 | The version of the response. |
| errCode | String | ASO NETWORK EX _ _ ISTING | The error code. |
| errTitle | String | The data already exists. | The title of the error message. |
| errMessage | String | The data already exists. Check the parameter value. | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetXgwMachineList &ClusterName=vpcAzoneCluster-AXXXXXXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "eagleEyeTraceId":"0a421xxxxxxxxxxxxxxxxxxxxxxx",
 "cost":905,
 "RequestId":"0ED8XXXX-XXXX-XXXX-XXXX",
 "Message":"ok",
 "ErrMsg":"success",
 "serviceRole":"baseXXXXX.baseXXXXXXX.XXXX#",
 "errTitle":"The data already exists.",
 "ErrNo":"0",
 "Data":{
  "State":"good",
  "IP":"10.XX.XX.X",
  "IDC":"amXXXX",
  "HostName":"c27b0XXXXXXXXXXX"
```

`},`

```json
 "requestURI":"/slalink/fulllink/classic/XXXXXX",
 "Code":"200",
 "Success":true,
 "responseVersion":"v1",
 "success":true,
 "errCode":"ASO_NETWORK_EXISTING",
 "errMessage":"The data already exists. Check the parameter value."
```

`}`

### 7.3 Storage Operations Console

#### 7.3.1 Apsara Distributed File System O&M

##### 7.3.1.1 GetPanguStorageCapacity

Queries the capacity of a product in Apsara Distributed File System.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| productCo de | Strin g | Query | Yes | hologres | The product name. Examples: oss, nas, cds, hologres, ecs, tianji, and odps. |

To query the values that you can specify for productCode, log on to the **ApsaraUni-manager**

**Operations Console**

, click **Products** , and select **Apsara Distributed File System** from the drop-down list. Then, click **Dashboard** in the left-side navigation pane.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The response code. Valid values: 200: The request is successful. 500: An unknown exception occurred. You must troubleshoot the backend service port. |
| data | Array of PanguStorage Capacity |   | The information about the capacity of the product in Apsara Distributed File System. |
| totalSize | String | 88542 | The total capacity of the product. Unit: GB. |
| totalFreeSize | String | 83801 | The remaining capacity of the product. Unit: GB. |
| usedSpacePer cent | String | 5.3500 | The proportion of the used capacity. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPanguStorageCapacity &productCode=hologres &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "code":"200",
 "data":[{
  "totalSize":"88542",
  "totalFreeSize":"83801",
  "usedSpacePercent":"5.3500"
```

`}]` `}`

#### 7.3.2 CDS O&M

##### 7.3.2.1 DescribeOssCluster

Queries the information about an Object Storage Service (OSS) cluster based on the cluster ID.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OpsProduc t | Strin g | Hea der | No |   |   |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| storageClu sterId | Strin g | Body | No | sc- 0000266w2des2hk08oj6 | The storage cluster ID. You can call the DescribeStorageClusters operation to query storage clusters and obtain their IDs. |
| ossClusterI d | Strin g | Body | No | oc- 0000266w2des2hk08oj6 | The OSS cluster ID. You must specify this parameter or the storageClusterId parameter. If you specify both parameters, the value of storageClusterId prevails. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request is successful. Valid values: true and false. |
| requestId | String | 2b88c1d1-dbcd- 4204-b0ea- ed768a7ef863 | The request ID. |
| code | String | 200 | The returned HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |

| message | String | successful | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
|---|---|---|---|
| storageCluster Id | String | sc- 0000263bm0ssvce 7ika2 | The storage cluster ID. |
| ossClusterId | String | oc- 0000263bm0ssvce 9qsp4 | The OSS cluster ID. |
| slaDay | Float | 100.0 | The percentage of Standard buckets in the cluster. Unit: %. |
| totalRequest | Long | 14590646 | The total number of requests that the cluster handled. |
| totalReadRequ est | Long | 14493831 | The number of read requests that the cluster handled. |
| totalWriteReq uest | Long | 80184 | The number of write requests that the cluster handled. |
| trafficIn | Float | 148674670 | The cluster inbound traffic of the current day. Unit: Bytes. |
| trafficOut | Float | 63725396 | The cluster outbound traffic of the current day. Unit: Bytes. |
| bucketCount | Long | 82 | The number of buckets in the cluster. |
| bucketCountT odayInc | Long | 0 | The number of buckets created on the current day. |
| totalObjectCou nt | Long | 516829340 | The number of objects in the cluster. |
| totalObjectCou ntTodayInc | Long | 15333291 | The number of objects created on the current day. |
| storage | Long | 41647257681920 | The logical storage capacity of the cluster. |

| storageInc | Long | 0 | The logical incremental storage capacity of the cluster on the current day. |
|---|---|---|---|
| overdue | Boolean | false | Indicates whether the cluster is expired. Valid values: true and false. |
| updatedTime | Long | 0 | The time when the cluster information was last updated. |
| ossUsed | Long | 0 | This parameter has been deprecated. |
| ossUsedRate | Float | 38.81 | The capacity utilization. Unit: %. |
| ossTotalSizeT | Float | 432 | The total capacity. Unit: TiB. |
| ossUsedT | Float | 3.41 | The used capacity. Unit: TiB. |

**Examples**

Sample requests `{`

```json
    "storageClusterId":"sc-0000266w2des2hk08oj6"
```

`}` Sample success responses `JSON` format `{`

```json
 "updatedTime": 0,
 "ossUsed": 0,
 "totalObjectCount": 516829340,
 "code": "200",
 "trafficIn": 148674670,
 "trafficOut": 63725396,
 "ossUsedT": 141.71,
 "slaDay": 100,
 "storageClusterId": "sc-0000263bm0ssvce7ika2",
 "storageInc": 0,
 "storage": 41647257681920,
 "message": "successful",
 "ossTotalSizeT": 365.14,
 "totalReadRequest": 14493831,
 "totalObjectCountTodayInc": -15333291,
 "totalRequest": 14590646,
 "bucketCountTodayInc": 0,
 "overdue": false,
 "success": true,
 "requestId": "2b88c1d1-dbcd-4204-b0ea-ed768a7ef863",
 "ossClusterId": "oc-0000263bm0ssvce9qsp4",
 "bucketCount": 82,
 "ossUsedRate": 38.81,
 "totalWriteRequest": 80184
```

`}`

##### 7.3.2.2 DescribeClusterCapacity

Queries the capacity statistics about storage clusters.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OpsProduc t | Strin g | Hea der | No |   |   |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| clusterNa me | Strin g | Body | No | CdsOtsSearchSsdCluster- A-20230910-004c | The name of the storage cluster. Separate multiple names with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -clusterName | String | CdsEbsHybridClust er-A-20230910- 0048 | The cluster name. |
| - clusterAliasNa me | String | CdsEbsHybridClust er-A-20230910- 0048 | The cluster alias. |
| -ioType | String | io8,io16 | The I/O type of a block cluster. This parameter takes effect only when the queried cluster is a block storage cluster. |
| -media | String | hybrid | The storage medium type. Valid values: hybrid and ssd. hybird indicates hybrid flash storage and ssd indicates all-flash storage. |
| -storageType | String | EBS | The storage service type. Valid values: -EBS -EBS -OSS -OSS |
| -factoryBytes | Long | 864009981001728 | The rated physical storage capacity. Unit: bytes. |
| -plannedBytes | Long | 544326237028352 | The storage capacity displayed on Deployment Planner. Unit: bytes. |
| - consumedByte s | Long | 515396075520 | The used logical space of the storage service. Unit: bytes. The value is calculated based on the formula of the corresponding service. |
| - provisionedByt es | Long | 726580450151103 | The total logical space of the storage service. Unit: bytes. The value is calculated based on the formula of the corresponding service. |

| - allocatedBytes | Long | 8761529272893 | The used physical space displayed on Apsara Distributed File System, excluding the physical space used by cache disks. Unit: bytes. The value may be different from the data queried by calling the relevant operations of the storage service. Therefore, the data queried by calling the relevant operations of the storage service prevail. |
|---|---|---|---|
| - guaranteedByt es | Long | 854800529589534 | The total physical space displayed on Apsara Distributed File System, excluding the physical space of cache disks. Unit: bytes. The value may be different from the data queried by calling the relevant operations of the storage service. Therefore, the data queried by calling the relevant operations of the storage service prevail. |
| success | Boolean | true | Indicates whether the request is successful. Valid values: true and false. |
| requestId | String | 7ac0e3b8-1f9e- 4793-aa0c- 850fba0394c0 | The request ID. |
| code | String | 200 | The response code. |
| message | String | successful | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

**Examples**

Sample requests `{`

```json
    "clusterName": "CdsEbsHybridCluster-A-20230910-0048,CdsOssHybridCluster-A-20230830-
004e"
```

`}` Sample success responses `JSON` format `{`

```json
 "code": "200",
 "data": [{
   "allocatedBytes": 8761529272893,
   "clusterAliasName": "CdsEbsHybridCluster-A-20230910-0048",
   "clusterName": "CdsEbsHybridCluster-A-20230910-0048",
   "consumedBytes": 515396075520,
   "factoryBytes": 864009981001728,
   "guaranteedBytes": 854800529589534,
   "ioType": "io8,io16",
   "media": "hybrid",
   "plannedBytes": 544326237028352,
   "provisionedBytes": 726580450151103,
   "storageType": "EBS"
```

`},` `{`

```json
   "allocatedBytes": 81972049518,
   "clusterAliasName": "CdsOssHybridCluster-A-20230830-004e",
   "clusterName": "CdsOssHybridCluster-A-20230830-004e",
   "consumedBytes": 0,
   "factoryBytes": 864009981001728,
   "guaranteedBytes": 814263822100000,
   "plannedBytes": 330483808337920,
   "provisionedBytes": 244256501399552,
   "media": "hybrid",
   "storageType": "OSS"
```

`}` `],`

```json
 "message": "successful",
 "requestId": "7ac0e3b8-1f9e-4793-aa0c-850fba0394c0",
 "success": true
```

`}`

##### 7.3.2.3 DescribeHosts

Queries a list of hosts.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OpsProduc t | Strin g | Hea der | No |   |   |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| storageClu sterId | Strin g | Body | No | sc- 0009x1sadxxl4s399d40 | The storage cluster ID. |
|---|---|---|---|---|---|
| sortBy | Strin g | Body | No | hostName | The field by which the returned data is sorted. If this parameter is left empty, the returned data is sorted by creation time. |
| orderBy | Strin g | Body | No | DESC | The type of sorting. Valid values: ASC: ascending order. DESC (default): descending order. |
| page | Integ er | Body | No | 1 | The page number. Default value: 1. |
| size | Integ er | Body | No | 10 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| hosts | Array |   | The hosts. |
| - storageCluster Id | String | sc- 000ekx55q5mf27z d5a3p | The storage cluster ID. |
| -hostId | String | hs- 000ekx55q5mf27z g1z2m | The host ID. |
| -hostName | String | 21e03018.cloud.e0 3.amtest212 | The hostname. |
| -clusterName | String | CdsOssHybridClust er-A-20230820- 013c | The cluster name. |

| - clusterAliasNa me | String | CdsOssHybridClust er-A-20230820- 013c | The cluster alias. |
|---|---|---|---|
| -ipAddress | String | 10.212.1.8 | The IP address. |
| -cpu | Integer | 64 | The number of CPU cores. |
| -memory | Long | 274877906944 | The memory size. Unit: bytes. |
| -state | String | GOOD | Indicates whether the host is available. GOOD indicates that the host is available. Otherwise, the host is unavailable. |
| -status | String | NORMAL | The status of the host. Valid values: NORMAL: The host is normal. PINGERROR: A PING failure occurred. OPS: The host is under O&M. NOHEARTBEAT: No heartbeat is detected. STATUSERROR: The host status is invalid. SCALEIN: The host is being scaled in. SCALEOUT: The host is being scaled out. |
| -machineType | String | PN68P2M1S1.22 | The type of the host. |
| -os | String | AliOS7U2-x86-64 | The operating system. |
| -sn | String | 221266574 | The serial number. |
| -azone | String | cn-wulan-env212- amtest212001-a | The zone ID. |
| -idc | String | amtest212 | IDC |
| -room | String | C2-1 | The data center. |
| -rack | String | E03 | The rack ID. |
| -rackUnitId | Integer | 18 | The rack unit ID. |

| success | Boolean | true | Indicates whether the request is successful. Valid values: true and false. |
|---|---|---|---|
| requestId | String | 80eb5f0b-11d9- 4992-95df- 2a15be050a25 | The request ID. |
| code | String | 200 | The returned HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | successful | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| totalElements | Long | 6 | The total number of entries returned. |
| totalPages | Long | 1 | The total number of pages returned. |
| numberOfElem ents | Long | 6 | The number of returned objects. |
| sorted | Boolean | true | Indicates whether sorting was enabled. Valid values: true and false. |
| paged | Boolean | true | Indicates whether pagination was enabled. Valid values: true and false. |
| firstPage | Boolean | true | Indicates whether the current page is the first page. Valid values: true and false. |
| lastPage | Boolean | true | Indicates whether the current page is the last page. Valid values: true and false. |
| page | Integer | 1 | The page number. |
| size | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests `{`

```json
 "storageClusterId": "sc-0009x1sadxxl4s399d40",
 "page": 1,
 "size": 10
```

`}` Sample success responses `JSON` format `{`

```json
    "paged": true,
    "code": "200",
    "lastPage": true,
    "hosts": [
```

`{`

```json
            "hostName": "c21e03018.cloud.e03.amtest212",
            "rack": "E03",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.1.8",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zg1z2m",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 18,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221266574",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
            "status": "NORMAL"
```

`},` `{`

```json
            "hostName": "c21e03117.cloud.e04.amtest212",
            "rack": "E04",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.1.9",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zkqyop",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 17,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221268367",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
            "status": "NORMAL"
```

`},` `{`

```json
            "hostName": "c21e05016.cloud.e05.amtest212",
            "rack": "E05",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.2.8",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zjhkjr",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 16,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221268368",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
            "status": "NORMAL"
```

`},` `{`

```json
            "hostName": "c21e05114.cloud.e06.amtest212",
            "rack": "E06",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.2.9",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zlhlgz",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 14,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221268369",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
            "status": "NORMAL"
```

`},` `{`

```json
            "hostName": "c21e07017.cloud.e07.amtest212",
            "rack": "E07",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.3.6",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zfyylr",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 17,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221268372",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
```

```json
            "status": "NORMAL"
```

`},` `{`

```json
            "hostName": "c21e07102.cloud.e08.amtest212",
            "rack": "E08",
            "memory": 274877906944,
            "os": "AliOS7U2-x86-64",
            "ipAddress": "10.212.3.7",
            "cpu": 64,
            "hostId": "hs-000ekx55q5mf27zc0vxj",
            "idc": "amtest212",
            "storageClusterId": "sc-000ekx55q5mf27zd5a3p",
            "rackUnitId": 2,
            "room": "C2-1",
            "clusterName": "CdsOssHybridCluster-A-20230820-013c",
            "sn": "221268375",
            "state": "GOOD",
            "azone": "cn-wulan-env212-amtest212001-a",
            "machineType": "PN68P2M1S1.22",
            "status": "NORMAL"
```

`}` `],`

```json
    "message": "successful",
    "totalElements": 6,
    "sorted": true,
    "firstPage": true,
    "numberOfElements": 6,
    "size": 9,
    "requestId": "80eb5f0b-11d9-4992-95df-2a15be050a25",
    "success": true,
    "totalPages": 1,
    "page": 1
```

`}`

##### 7.3.2.4 DescribeMetrics

Queries metric data. Metric types STORAGE_CLUSTER STORAGE_CLUSTER: metrics related to storage clusters. To query the metric data of a storage cluster, you must obtain the cluster ID, specify the ID as the value of entityId, and then call the DescribeMetrics operation. You can call the DescribeStorageClusters operation to obtain the ID of the storage cluster. BLOCK_CLUSTER BLOCK_CLUSTER: metrics related to block storage clusters. To query the metric data of a block storage cluster, you must obtain the cluster ID, specify the ID as the value of entityId, and then call the DescribeMetrics operation. You can call the DescribeBlockClusters operation to obtain the ID of the block storage cluster. OSS_CLUSTER OSS_CLUSTER: metrics related to Object Storage Service (OSS) clusters. To query the metric data of an OSS cluster, you must obtain the cluster ID, specify the ID as the value of entityId, and then call the DescribeMetrics operation. You can call the DescribeOssCluster operation to obtain the ID of the OSS cluster. HOST HOST: metrics related to hosts. To query the metric data of a host, you must obtain the host ID, specify the ID as the value of entityId, and then call the DescribeMetrics operation. You can call the DescribeHosts operation to obtain the ID of the host. OSS_BUCKET OSS_BUCKET: metrics related to OSS buckets. To query the metric data of an OSS bucket, you can call the DescribeMetrics operation and set the entityId parameter to oss_bucket and the Tags parameter to the name of the bucket. You can call the ListBucket operation to obtain the name of the bucket. You want to obtain the data points of the qps1 and qps2 metrics of an OSS cluster. You can perform the following steps to obtain the metric data points: Step 1: Obtain the storage cluster ID Call the DescribeStorageClusters operation to obtain the value of storageClusterId. Step 2: Obtain the OSS cluster ID Specify the value of storageClusterId obtained in Step 1 as the value of ossClusterId and call the DescribeOssCluster operation to obtain the corresponding OSS cluster ID. Step 3: Obtain the data points of metrics Specify the value of ossClusterId obtained in Step 2 as the value of entiryId and set the metrics parameter to qps1 and qps2. Then, call the DescribeMetrics operation to obtain the data points of qps1 and qps2 metrics.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OpsProduc t | Strin g | Hea der | No |   |   |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| entityId | Strin g | Body | No | oc- 0000266w2des2hjxvno4 | The ID of the entity whose metric information you want to query. Supported entity types: STORAGE CLUSTER: _ storage cluster. BLOCK CLUSTER: block _ storage cluster. OSS CLUSTER: OSS _ cluster. HOST: host. To query the metric information of an OSS bucket, set this parameter to oss bucket _ and specify the bucket name in the Tags parameter. |
|---|---|---|---|---|---|
| startTs | Long | Body | No | 1693185016323 | The start time of metric collection. Unit: ms. |
| endTs | Long | Body | No | 1693188616323 | The end time of metric collection. Unit: ms. |
| resolution | Integ er | Body | No | 400 | The number of times that data points for the metric are collected between the start time and end time of metric collection. Valid values: 1–960. Recommended value: 400. The system calculates the number of times that data points for the metric are collected based on the value of this parameter and the values of the startTs and endTs parameters. |

| metrics | Strin g | Body | No | sync in intranet recv,syn _ _ _ c in intranet send _ _ _ | The name of the metric whose data you want to obtain. You can specify multiple metrics at the same time. Separate multiple metrics with commas (,). The metric type must be the same as the type of the entity that you specified in entityId. Metrics are classified into the following types based on the entity types: 1. STORAGE CLUSTER _ 2. BLOCK CLUSTER _ 3. OSS CLUSTER _ 4. HOST 5. OSS BUCKET _ The metrics of each type will be described in detail in the following section. |
|---|---|---|---|---|---|
| tags | List | Body | No | [{"key":"bucket","value":" aes202308281511"}] | The tag key-value pair of the bucket whose metric information you want to query. You need to specify this parameter only for metrics of the OSS BUCKET type. _ Example: {"key":"bucket","value":" aes202308281511"}. This example indicates that you want to query the metric information of the bucket whose tag value is aes202308281511. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call was successful. Valid values: true and false. |

| requestId | String | 2b88c1d1-dbcd- 4204-b0ea- ed768a7ef863 | The request ID. |
|---|---|---|---|
| code | String | 200 | The returned HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | successful | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |
| body | String | [{\"columns\": [\"time\", \"value\"],\"name\": \"sync in intranet _ _ _ recv\",\"values\": [[1692938670000, 0.0], [1692938680000, 0.0], [1692938690000, 0.0], [1692938700000, 0.0]] }, {\"columns\": [\"time\", \"value\"],\"name\": \"sync in intranet _ _ _ send\", \"values\": [[1692938670000, 0.0], [1692938680000, 0.0], [1692938690000, 0.0], [1692938700000, 0.0], [1692938710000, 0.0]]}] | The metric information. The value is a JSON string that contains the following fields: name, columns, and values. name The metric name. columns The returned metric data. - time: the time when the data point was collected. -value: the data point of the metric. values The array of the values field corresponds to the array of the columns field. For example, the [1692938670000, 0.0] array can be converted to the {"time": 1692938670,000, "value": 0.0} object. |

**Examples**

Sample requests `{`

```json
 "_tag": "default",
 "entityId": "oc-0000266w2des2hjxvno4",
 "startTs": 1693185016323,
 "endTs": 1693188616323,
 "metrics": "sync_in_intranet_recv,sync_in_intranet_send",
 "tags": [],
 "resolution": 400
```

`}` Sample success responses `JSON` format `{`

```json
    "code": "200",
    "success": true,
    "requestId": "a3ff0f3d-bff6-4b29-8e27-d05aae23f069",
    "message": "successful",
    "body": "[{\"columns\": [\"time\", \"value\"],\"name\":
\"sync_in_intranet_recv\",\"values\": [[1692938670000, 0.0],[1692938680000, 0.0],[16929 38690000, 0.0],[1692938700000, 0.0]] }, {\"columns\": [\"time\", \"value\"],\"name\":\"sync_in_intranet_send\", \"values\": [[1692938670000, 0.0],[16929 38680000, 0.0],[1692938690000, 0.0], [1692938700000, 0.0],[1692938710000, 0.0]]}]"
```

`}`

**Metrics**

Metrics are classified into the following types: STORAGE_CLUSTER, BLOCK_CLUSTER, BLOCK_CLUSTER, HOST, and OSS_BUCKET.

**HOST**

| Description | Metric |
|---|---|
| CPU | host cpu _ |
| Memory | host mem _ |
| Average loads over the previous minute | host load1 avg _ _ |
| Average loads over the previous 5 minutes | host load5 avg _ _ |
| Average loads over the previous 15 minutes | host load15 avg _ _ |

| iops | host iops _ |
|---|---|
| Outbound traffic | host traffic out _ _ |
| Inbound traffic | host traffic in _ _ |
| iops | host iops _ |
| Offset between the time of the host and the time of the NTP server. Unit: ms. | host ntp offset _ _ |
| NTP server synchronization status. 0 indicates normal. | host ntp sync _ _ |

**STORAGE_CLUSTER**

| Description | Metric |
|---|---|
| CPU | cluster cpu _ |
| Memory size | cluster mem _ |
| Average loads over the previous minute | cluster load1 avg _ _ |
| Average loads over the previous 5 minutes | cluster load5 avg _ _ |
| Average loads over the previous 15 minutes | cluster load15 avg _ _ |
| Disk IOPS | cluster disk iops _ _ |

**OSS_CLUSTER**

**OSS cluster QPS**

| Description | Metric |
|---|---|
| QPSI(PUT/POST/DELETE) | qps1 |
| QPSII(GET/Head) | qps2 |

**OSS cluster bandwidth**

| Description | Metric |
|---|---|
| Inbound traffic over the internal network | private net in traffic _ _ _ |
| Outbound traffic over the internal network | private net out traffic _ _ _ |

**OSS management bandwidth**

| Description | Metric |
|---|---|
| Inbound traffic over the Internet | public net in traffic _ _ _ |
| Inbound traffic over the internal network | private net in traffic _ _ _ |
| Inbound CDN traffic | cdn in _ |
| Inbound VPC traffic | vpc in _ |
| Inbound traffic of synchronization requests over the Internet | sync in _ |
| Inbound traffic of synchronization requests over the internal network | sync in intranet recv _ _ _ |
| Inbound QoS | qos bw in _ _ |
| Outbound traffic over the Internet | public net out traffic _ _ _ |
| Outbound traffic over the internal network | private net out traffic _ _ _ |
| Outbound CDN traffic | cdn out _ |
| Outbound VPC traffic | vpc out _ |
| Outbound traffic of synchronization requests over the Internet | sync out _ |

| Outbound traffic of synchronization requests over the internal network | sync in intranet send _ _ _ |
|---|---|
| Outbound QoS | qos bw out _ _ |

**QPS**

| Description | Metric |
|---|---|
| Total number of requests | total request _ |
| QPS throttling | qos qps _ |
| QPSI(PUT/POST/DELETE) | qps1 |
| QPSII(GET/Head) | qps2 |
| Synchronous writes | sync in qpsi count _ _ _ |
| Synchronous reads | sync in qpsii count _ _ _ |
| copy object | copy object count _ _ |
| upload part copy | upload part copy count _ _ _ |
| get object(0~100KB) _ | small2 get object count _ _ _ |
| get object(100~200KB) _ | small1 get object count _ _ _ |
| get object(200~1MB) _ | small get object count _ _ _ |
| get object(1MB~) _ | big get object count _ _ _ |
| put object(0~100KB) _ | small2 put object count _ _ _ |
| put object(100~200KB) _ | small1 put object count _ _ _ |
| put object(200~1MB) _ | small put object count _ _ _ |

| put object(1MB~) _ | big put object count _ _ _ |
|---|---|
| upload part(0~100KB) _ | small2 upload part count _ _ _ |
| upload part(100~200KB) _ | small1 upload part count _ _ _ |
| upload part(200~1MB) _ | small upload part count _ _ _ |
| upload part(1MB~) _ | big upload part count _ _ _ |
| post object(0~100KB) _ | small2 post object count _ _ _ |
| post object(100~200KB) _ | small1 post object count _ _ _ |
| post object(200~1MB) _ | small post object count _ _ _ |
| post object(1MB~) _ | big post object count _ _ _ |
| append object(0~100KB) _ | small2 append object count _ _ _ |
| append object(100~200KB) _ | small1 append object count _ _ _ |
| append object(200~1MB) _ | small append object count _ _ _ |
| append object(1MB~) _ | big append object count _ _ _ |
| head object | head object count _ _ |
| get object info | get object info count _ _ _ |
| img process(0~100KB) _ | small2 img process count _ _ _ |
| img process(100~200KB) _ | small1 img process count _ _ _ |
| img process(200~1MB) _ | small img process count _ _ _ |
| img process(1MB~) _ | big img process count _ _ _ |

**Storage capacity**

| Description | Metric |
|---|---|
| Archive storage capacity | ar real storage _ _ |
| Archive storage capacity increment | ar real storage inc _ _ _ |
| Volume of written data | delta add _ |
| Volume of deleted data | delta del _ |
| Infrequent Access (IA) storage capacity | ia real storage _ _ |
| IA storage capacity increment | ia real storage inc _ _ _ |
| Standard storage capacity | std storage _ |
| Standard storage capacity increment | std storage inc _ _ |
| Total storage capacity | storage quota _ |
| Storage capacity increment | storage quota inc _ _ |

**Latency**

| Description | Metric |
|---|---|
| avg sl put(0~100KB) _ _ | small2 put object sl _ _ _ |
| avg sl put(100~200KB) _ _ | small1 put object sl _ _ _ |
| avg sl put(200~1MB) _ _ | small put object sl _ _ _ |
| avg sl put(1MB~) _ _ | big put object sl _ _ _ |
| max sl put(0~100KB) _ _ | max small2 put object sl _ _ _ _ |
| max sl put(100~200KB) _ _ | max small1 put object sl _ _ _ _ |

| max sl put(200~1MB) _ _ | max small put object sl _ _ _ _ |
|---|---|
| max sl put(1MB~) _ _ | max big put object sl _ _ _ _ |
| avg rl put(0~100KB) _ _ | small2 put object rl _ _ _ |
| avg rl put(100~200KB) _ _ | small1 put object rl _ _ _ |
| avg rl put(200~1MB) _ _ | small put object rl _ _ _ |
| avg rl put(1MB~) _ _ | big put object rl _ _ _ |
| max rl put(0~100KB) _ _ | max small2 put object rl _ _ _ _ |
| max rl put(100~200KB) _ _ | max small1 put object rl _ _ _ _ |
| max rl put(200~1MB) _ _ | max small put object rl _ _ _ _ |
| max rl put(1MB~) _ _ | max big put object rl _ _ _ _ |
| avg sl get(0~100KB) _ _ | small2 get object sl _ _ _ |
| avg sl get(100~200KB) _ _ | small1 get object sl _ _ _ |
| avg sl get(200~1MB) _ _ | small get object sl _ _ _ |
| avg sl get(1MB~) _ _ | big get object sl _ _ _ |
| max sl get(0~100KB) _ _ | max small2 get object sl _ _ _ _ |
| max sl get(100~200KB) _ _ | max small1 get object sl _ _ _ _ |
| max sl get(200~1MB) _ _ | max small get object sl _ _ _ _ |
| max sl get(1MB~) _ _ | max big get object sl _ _ _ _ |
| avg rl get(0~100KB) _ _ | small2 get object rl _ _ _ |

| avg rl get(100~200KB) _ _ | small1 get object rl _ _ _ |
|---|---|
| avg rl get(200~1MB) _ _ | small get object rl _ _ _ |
| avg rl get(1MB~) _ _ | big get object rl _ _ _ |
| max rl get(0~100KB) _ _ | max small2 get object rl _ _ _ _ |
| max rl get(100~200KB) _ _ | max small1 get object rl _ _ _ _ |
| max rl get(200~1MB) _ _ | max small get object rl _ _ _ _ |
| max rl get(1MB~) _ _ | max big get object rl _ _ _ _ |
| avg sl upload part(0~100KB) _ _ _ | small2 upload part sl _ _ _ |
| avg sl upload part(100~200KB) _ _ _ | small1 upload part sl _ _ _ |
| avg sl upload part(200~1MB) _ _ _ | small upload part sl _ _ _ |
| avg sl upload part(1MB~) _ _ _ | big upload part sl _ _ _ |
| max sl upload part(0~100KB) _ _ _ | max small2 upload part sl _ _ _ _ |
| max sl upload part(100~200KB) _ _ _ | max small1 upload part sl _ _ _ _ |
| max sl upload part(200~1MB) _ _ _ | max small upload part sl _ _ _ _ |
| max sl upload part(1MB~) _ _ _ | max big upload part sl _ _ _ _ |
| avg rl upload part(0~100KB) _ _ _ | small2 upload part rl _ _ _ |
| avg rl upload part(100~200KB) _ _ _ | small1 upload part rl _ _ _ |
| avg rl upload part(200~1MB) _ _ _ | small upload part rl _ _ _ |
| avg rl upload part(1MB~) _ _ _ | big upload part rl _ _ _ |

| max rl upload part(0~100KB) _ _ _ | max small2 upload part rl _ _ _ _ |
|---|---|
| max rl upload part(100~200KB) _ _ _ | max small1 upload part rl _ _ _ _ |
| max rl upload part(200~1MB) _ _ _ | max small upload part rl _ _ _ _ |
| max rl upload part(1MB~) _ _ _ | max big upload part rl _ _ _ _ |
| avg sl post(0~100KB) _ _ | small2 post object sl _ _ _ |
| avg sl post(100~200KB) _ _ | small1 post object sl _ _ _ |
| avg sl post(200~1MB) _ _ | small post object sl _ _ _ |
| avg sl post(1MB~) _ _ | big post object sl _ _ _ |
| max sl post(0~100KB) _ _ | max small2 post object sl _ _ _ _ |
| max sl post(100~200KB) _ _ | max small1 post object sl _ _ _ _ |
| max sl post(200~1MB) _ _ | max small post object sl _ _ _ _ |
| max sl post(1MB~) _ _ | max big post object sl _ _ _ _ |
| avg rl post(0~100KB) _ _ | small2 post object rl _ _ _ |
| avg rl post(100~200KB) _ _ | small1 post object rl _ _ _ |
| avg rl post(200~1MB) _ _ | small post object rl _ _ _ |
| avg rl post(1MB~) _ _ | big post object rl _ _ _ |
| max rl post(0~100KB) _ _ | max small2 post object rl _ _ _ _ |
| max rl post(100~200KB) _ _ | max small1 post object rl _ _ _ _ |
| max rl post(200~1MB) _ _ | max small post object rl _ _ _ _ |

| max rl post(1MB~) _ _ | max big post object rl _ _ _ _ |
|---|---|
| avg sl append(0~100KB) _ _ | small2 append object sl _ _ _ |
| avg sl append(100~200KB) _ _ | small1 append object sl _ _ _ |
| avg sl append(200~1MB) _ _ | small append object sl _ _ _ |
| avg sl append(1MB~) _ _ | big append object sl _ _ _ |
| max sl append(0~100KB) _ _ | max small2 append object sl _ _ _ _ |
| max sl append(100~200KB) _ _ | max small1 append object sl _ _ _ _ |
| max sl append(200~1MB) _ _ | max small append object sl _ _ _ _ |
| max sl append(1MB~) _ _ | max big append object sl _ _ _ _ |
| avg rl append(0~100KB) _ _ | small2 append object rl _ _ _ |
| avg rl append(100~200KB) _ _ | small1 append object rl _ _ _ |
| avg rl append(200~1MB) _ _ | small append object rl _ _ _ |
| avg rl append(1MB~) _ _ | big append object rl _ _ _ |
| max rl append(0~100KB) _ _ | max small2 append object rl _ _ _ _ |
| max rl append(100~200KB) _ _ | max small1 append object rl _ _ _ _ |
| max rl append(200~1MB) _ _ | max small append object rl _ _ _ _ |
| max rl append(1MB~) _ _ | max big append object rl _ _ _ _ |
| avg sl copy _ _ | copy object sl _ _ |
| max sl copy _ _ | max copy object sl _ _ _ |

| avg rl copy _ _ | copy object rl _ _ |
|---|---|
| max rl copy _ _ | max copy object rl _ _ _ |
| avg sl upload part copy _ _ _ _ | upload part copy sl _ _ _ |
| max sl upload part copy _ _ _ _ | max upload part copy sl _ _ _ _ |
| avg rl upload part copy _ _ _ _ | upload part copy rl _ _ _ |
| max rl upload part copy _ _ _ _ | max upload part copy rl _ _ _ _ |
| avg sl head _ _ | head object sl _ _ |
| max sl head _ _ | max head object sl _ _ _ |
| avg rl head _ _ | head object rl _ _ |
| max rl head _ _ | max head object rl _ _ _ |
| avg sl get object info _ _ _ _ | get object info sl _ _ _ |
| max sl get object info _ _ _ _ | max get object info sl _ _ _ _ |
| avg rl get object info _ _ _ _ | get object info rl _ _ _ |
| max rl get object info _ _ _ _ | max get object info rl _ _ _ _ |
| avg sl img(0~100KB) _ _ | small2 img process server latency _ _ _ _ |
| avg sl img(100~200KB) _ _ | small1 img process server latency _ _ _ _ |
| avg sl img(200~1MB) _ _ | small img process server latency _ _ _ _ |
| avg sl img(1MB~) _ _ | big img process server latency _ _ _ _ |
| max sl img(0~100KB) _ _ | max small2 img process server latency _ _ _ _ _ |

| max sl img(100~200KB) _ _ | max small1 img process server latency _ _ _ _ _ |
|---|---|
| max sl img(200~1MB) _ _ | max small img process server latency _ _ _ _ _ |
| max sl img(1MB~) _ _ | max big img process server latency _ _ _ _ _ |
| avg rl img(0~100KB) _ _ | small2 img process request latency _ _ _ _ |
| avg rl img(100~200KB) _ _ | small1 img process request latency _ _ _ _ |
| avg rl img(200~1MB) _ _ | small img process request latency _ _ _ _ |
| avg rl img(1MB~) _ _ | big img process request latency _ _ _ _ |
| max rl img(0~100KB) _ _ | max small2 img process request latency _ _ _ _ _ |
| max rl img(100~200KB) _ _ | max small1 img process request latency _ _ _ _ _ |
| max rl img(200~1MB) _ _ | max small img process request latency _ _ _ _ _ |
| max rl img(1MB~) _ _ | max big img process request latency _ _ _ _ _ |

**SLA**

| Description | Metric |
|---|---|
| Standard storage SLA | sla |

**HTTP status codes**

| Description | Metric |
|---|---|
| error 5xx _ | error 5xx _ |
| error 503 _ | error 503 _ |
| error 403 _ | error 403 _ |

| error 404 _ | error 404 _ |
|---|---|
| error 499 _ | error 499 _ |
| error 4xx other _ _ | error 4xx other _ _ |
| success 2xx _ | success 2xx _ |
| success 3xx _ | success 3xx _ |
| sync in5xx count _ _ | sync in5xx count _ _ |

**BLOCK_CLUSTER**

**Capacity**

| Description | Metric |
|---|---|
| Used logical space | cluster total sale _ _ |
| Used physical space | cluster total pangu usage _ _ _ |
| Total physical space | cluster total _ |

**Disks and snapshots**

| Description | Metric |
|---|---|
| Number of disks | device total _ |
| Number of snapshots | snapshot total _ |

**Total IOPS of block storage clusters**

| Description | Metric |
|---|---|
| Read IOPS | read sum iops _ _ |
| Write IOPS | write sum iops _ _ |

**Total throughput of block storage clusters**

| Description | Metric |
|---|---|
| Read throughput | read sum bps _ _ |
| Write throughput | write sum bps _ _ |

**Cluster monitoring**

| Description | Metric |
|---|---|
| cpu | cluster cpu _ |
| Memory size | cluster mem _ |
| Average loads over the previous minute | cluster load1 avg _ _ |
| Average loads over the previous 5 minutes | cluster load5 avg _ _ |
| Average loads over the previous 15 minutes | cluster load15 avg _ _ |
| Disk IOPS | cluster disk iops _ _ |

**Average latency**

| Description | Metric |
|---|---|
| Read latency | read latency _ |
| Write latency | write latency _ |

**Average latency of Netcat commands**

| Description | Metric |
|---|---|
| Read latency of Netcat commands | nc read latency _ _ |
| Write latency of Netcat commands | nc write latency _ _ |

**Read/write IOPS of Netcat commands**

| Description | Metric |
|---|---|
| Read IOPS of Netcat commands | nc read iops _ _ |
| Write IOPS of Netcat commands | nc write iops _ _ |

**Throughput of Netcat commands**

| Description | Metric |
|---|---|
| Read throughput of Netcat commands | nc read bps _ _ |
| Write throughput of Netcat commands | nc write bps _ _ |

**Average disk latency**

| Description | Metric |
|---|---|
| Disk read latency | device read latency _ _ |
| Disk write latency | device write latency _ _ |

**Disk read/write IOPS**

| Description | Metric |
|---|---|
| Disk read IOPS | device read iops _ _ |
| Disk write IOPS | device write iops _ _ |

**Disk throughput**

| Description | Metric |
|---|---|
| Disk read throughput | device read bps _ _ |
| Disk write throughput | device write bps _ _ |

**OSS_BUCKET**

| Description | Metric |
|---|---|
| SLA of an OSS bucket of the Standard class | bucket sla _ |
| Inbound traffic over the Internet | bucket public net in traffic _ _ _ _ |
| Outbound traffic over the Internet | bucket public net out traffic _ _ _ _ |
| Inbound traffic over the internal network | bucket private net in traffic _ _ _ _ |
| Outbound traffic over the internal network | bucket private net out traffic _ _ _ _ |
| Inbound CDN traffic | bucket cdn in _ _ |
| Outbound CDN traffic | bucket cdn out _ _ |
| Inbound VPC traffic | bucket vpc in _ _ |
| Outbound VPC traffic | bucket vpc out _ _ |
| Inbound traffic of synchronization requests over the Internet | bucket sync in _ _ |
| Outbound traffic of synchronization requests over the Internet | bucket sync out _ _ |
| Inbound traffic of synchronization requests over the internal network | bucket sync in intranet recv _ _ _ _ |
| Outbound traffic of synchronization requests over the internal network | bucket sync in intranet send _ _ _ _ |
| Inbound QoS | bucket qos bw in _ _ _ |
| Outbound QoS | bucket qos bw out _ _ _ |
| Total number of requests | bucket total request _ _ |

| QPS throttling | bucket qos qps _ _ |
|---|---|
| QPS of paid PUT, POST, and DELETE requests | bucket qps1 _ |
| QPS of paid GET and HEAD requests | bucket qps2 _ |
| Synchronous writes | bucket sync in qpsi count _ _ _ _ |
| Synchronous reads | bucket sync in qpsii count _ _ _ _ |
| copy object | bucket copy object count _ _ _ |
| upload copy part | bucket upload part copy count _ _ _ _ |
| get object (0 ~ 100KB) | bucket small2 get object count _ _ _ _ |
| get object (100 ~ 200KB) | bucket small1 get object count _ _ _ _ |
| get object (200KB ~ 1MB) | bucket small get object count _ _ _ _ |
| get object (>= 1MB) | bucket big get object count _ _ _ _ |
| put object (0 ~ 100KB) | bucket small2 put object count _ _ _ _ |
| put object (100KB ~ 200KB) | bucket small1 put object count _ _ _ _ |
| put object (200KB ~ 1MB) | bucket small put object count _ _ _ _ |
| put object (>= 1MB) | bucket big put object count _ _ _ _ |
| upload part (0 ~ 100KB) | bucket small2 upload part count _ _ _ _ |
| upload part (100KB ~ 200KB) | bucket small1 upload part count _ _ _ _ |
| upload part (200KB ~ 1MB) | bucket small upload part count _ _ _ _ |
| upload part (>= 1MB) | bucket big upload part count _ _ _ _ |

| post object (0 ~ 100KB) | bucket small2 post object count _ _ _ _ |
|---|---|
| post object (100KB ~ 200KB) | bucket small1 post object count _ _ _ _ |
| post object (200KB ~ 1MB) | bucket small post object count _ _ _ _ |
| post object (>=1MB) | bucket big post object count _ _ _ _ |
| append object (0 ~ 100KB) | bucket small2 append object count _ _ _ _ |
| append object (100KB ~ 200KB) | bucket small1 append object count _ _ _ _ |
| append object (200KB ~ 1MB) | bucket small append object count _ _ _ _ |
| append object (>= 1MB) | bucket big append object count _ _ _ _ |
| head object | bucket head object count _ _ _ |
| get object info | bucket get object info count _ _ _ _ |
| image process (0 ~ 100KB) | bucket small2 img process count _ _ _ _ |
| image process (100KB ~ 200KB) | bucket small1 img process count _ _ _ _ |
| image process (200KB ~ 1MB) | bucket small img process count _ _ _ _ |
| image process (>= 1MB) | bucket big img process count _ _ _ _ |
| average put object server latency (0 ~ 100KB) | bucket small2 put object sl _ _ _ _ |
| average put object server latency (100KB ~ 200KB) | bucket small1 put object sl _ _ _ _ |
| average put object server latency (200KB ~ 1MB) | bucket small put object sl _ _ _ _ |
| average put object server latency (>= 1MB) | bucket big put object sl _ _ _ _ |
| max put object server latency (0 ~ 100KB) | bucket max small2 put object sl _ _ _ _ _ |

| max put object server latency (100KB ~ 200KB) | bucket max small1 put object sl _ _ _ _ _ |
|---|---|
| max put object server latency (200KB ~ 1MB) | bucket max small put object sl _ _ _ _ _ |
| max put object server latency (>= 1MB) | bucket max big put object sl _ _ _ _ _ |
| average put object request latency (0 ~ 100KB) | bucket small2 put object rl _ _ _ _ |
| average put object request latency (100KB ~ 200KB) | bucket small1 put object rl _ _ _ _ |
| average put object request latency (200KB ~ 1MB) | bucket small put object rl _ _ _ _ |
| average put object request latency (>= 1MB) | bucket big put object rl _ _ _ _ |
| max put object request latency (0 ~ 100KB) | bucket max small2 put object rl _ _ _ _ _ |
| max put object request latency (100KB ~ 200KB) | bucket max small1 put object rl _ _ _ _ _ |
| max put object request latency (200KB ~ 1MB) | bucket max small put object rl _ _ _ _ _ |
| max put object request latency (>= 1MB) | bucket max big put object rl _ _ _ _ _ |
| average get object server latency (0 ~ 100KB) | bucket small2 get object sl _ _ _ _ |
| average get object server latency (100KB ~ 200KB) | bucket small1 get object sl _ _ _ _ |
| average get object server latency (200KB ~ 1MB) | bucket small get object sl _ _ _ _ |
| average get object server latency (>= 1MB) | bucket big get object sl _ _ _ _ |
| max get object server latency (0 ~ 100KB) | bucket max small2 get object sl _ _ _ _ _ |
| max get object server latency (100KB ~ 200KB) | bucket max small1 get object sl _ _ _ _ _ |
| max get object server latency (200KB ~ 1MB) | bucket max small get object sl _ _ _ _ _ |

| max get object server latency (>= 1MB) | bucket max big get object sl _ _ _ _ _ |
|---|---|
| average get object request latency (0 ~ 100KB) | bucket small2 get object rl _ _ _ _ |
| average get object request latency (100KB ~ 200KB) | bucket small1 get object rl _ _ _ _ |
| average get object request latency (200KB ~ 1MB) | bucket small get object rl _ _ _ _ |
| average get object request latency (>= 1MB) | bucket big get object rl _ _ _ _ |
| max get object request latency (0 ~ 100KB) | bucket max small2 get object rl _ _ _ _ _ |
| max get object request latency (100KB ~ 200KB) | bucket max small1 get object rl _ _ _ _ _ |
| max get object request latency (200KB ~ 1MB) | bucket max small get object rl _ _ _ _ _ |
| max get object request latency (>= 1MB) | bucket max big get object rl _ _ _ _ _ |
| average upload part server latency (0 ~ 100KB) | bucket small2 upload part sl _ _ _ _ |
| average upload part server latency (100KB ~ 200KB) | bucket small1 upload part sl _ _ _ _ |
| average upload part server latency (200KB ~ 1MB) | bucket small upload part sl _ _ _ _ |
| average upload part server latency (>= 1MB) | bucket big upload part sl _ _ _ _ |
| max upload part server latency (0 ~ 100KB) | bucket max small2 upload part sl _ _ _ _ _ |
| max upload part server latency (100KB ~ 200KB) | bucket max small1 upload part sl _ _ _ _ _ |
| max upload part server latency (200KB ~ 1MB) | bucket max small upload part sl _ _ _ _ _ |
| max upload part server latency (>= 1MB) | bucket max big upload part sl _ _ _ _ _ |
| average upload part request latency (0 ~ 100KB) | bucket small2 upload part rl _ _ _ _ |

| average upload part request latency (100KB ~ 200KB) | bucket small1 upload part rl _ _ _ _ |
|---|---|
| average upload part request latency (200KB ~ 1MB) | bucket small upload part rl _ _ _ _ |
| average upload part request latency (>= 1MB) | bucket big upload part rl _ _ _ _ |
| max upload part request latency (0 ~ 100KB) | bucket max small2 upload part rl _ _ _ _ _ |
| max upload part request latency (100KB ~ 200KB) | bucket max small1 upload part rl _ _ _ _ _ |
| max upload part request latency (200KB ~ 1MB) | bucket max small upload part rl _ _ _ _ _ |
| max upload part request latency (>= 1MB) | bucket max big upload part rl _ _ _ _ _ |
| average post object server latency (0 ~ 100KB) | bucket small2 post object sl _ _ _ _ |
| average post object server latency (100KB ~ 200KB) | bucket small1 post object sl _ _ _ _ |
| average post object server latency (200KB ~ 1MB) | bucket small post object sl _ _ _ _ |
| average post object server latency (>= 1MB) | bucket big post object sl _ _ _ _ |
| max post object server latency (0 ~ 100KB) | bucket max small2 post object sl _ _ _ _ _ |
| max post object server latency (100KB ~ 200KB) | bucket max small1 post object sl _ _ _ _ _ |
| max post object server latency (200KB ~ 1MB) | bucket max small post object sl _ _ _ _ _ |
| max post object server latency (>= 1MB) | bucket max big post object sl _ _ _ _ _ |
| average post object request latency (0 ~ 100KB) | bucket small2 post object rl _ _ _ _ |
| average post object request latency (100KB ~ 200KB) | bucket small1 post object rl _ _ _ _ |

| average post object request latency (200KB ~ 1MB) | bucket small post object rl _ _ _ _ |
|---|---|
| average post object request latency (>= 1MB) | bucket big post object rl _ _ _ _ |
| max post object request latency (0 ~ 100KB) | bucket max small2 post object rl _ _ _ _ _ |
| max post object request latency (100KB ~ 200KB) | bucket max small1 post object rl _ _ _ _ _ |
| max post object request latency (200KB ~ 1MB) | bucket max small post object rl _ _ _ _ _ |
| max post object request latency (>= 1MB) | bucket max big post object rl _ _ _ _ _ |
| average append object server latency (0 ~ 100KB) | bucket small2 append object sl _ _ _ _ |
| average append object server latency (100KB ~ 200KB) | bucket small1 append object sl _ _ _ _ |
| average append object server latency (200KB ~ 1MB) | bucket small append object sl _ _ _ _ |
| average append object server latency (>= 1MB) | bucket big append object sl _ _ _ _ |
| max append object server latency (0 ~ 100KB) | bucket max small2 append object sl _ _ _ _ _ |
| max append object server latency (100KB ~ 200KB) | bucket max small1 append object sl _ _ _ _ _ |
| max append object server latency (200KB ~ 1MB) | bucket max small append object sl _ _ _ _ _ |
| max append object server latency (>= 1MB) | bucket max big append object sl _ _ _ _ _ |
| average append object request latency (0 ~ 100KB) | bucket small2 append object rl _ _ _ _ |
| average append object request latency (100KB ~ 200KB) | bucket small1 append object rl _ _ _ _ |

| average append object request latency (200KB ~ 1MB) | bucket small append object rl _ _ _ _ |
|---|---|
| average append object request latency (>= 1MB) | bucket big append object rl _ _ _ _ |
| max append object request latency (0 ~ 100KB) | bucket max small2 append object rl _ _ _ _ _ |
| max append object request latency (100KB ~ 200KB) | bucket max small1 append object rl _ _ _ _ _ |
| max append object request latency (200KB ~ 1MB) | bucket max small append object rl _ _ _ _ _ |
| max append object request latency (>= 1MB) | bucket max big append object rl _ _ _ _ _ |
| average copy object server latency | bucket copy object sl _ _ _ |
| max copy object server latency | bucket max copy object sl _ _ _ _ |
| average copy object request latency | bucket copy object rl _ _ _ |
| max copy object request latency | bucket max copy object rl _ _ _ _ |
| average upload part copy server latency | bucket upload part copy sl _ _ _ _ |
| max upload part copy server latency | bucket max upload part copy sl _ _ _ _ _ |
| average upload part copy request latency | bucket upload part copy rl _ _ _ _ |
| max upload part copy request latency | bucket max upload part copy rl _ _ _ _ _ |
| average head object server latency | bucket head object sl _ _ _ |
| max head object server latency | bucket max head object sl _ _ _ _ |
| average head object request latency | bucket head object rl _ _ _ |
| max head object request latency | bucket max head object rl _ _ _ _ |

| average get object info server latency | bucket get object info sl _ _ _ _ |
|---|---|
| max get object info server latency | bucket max get object info sl _ _ _ _ _ |
| average get object info request latency | bucket get object info rl _ _ _ _ |
| max get object info request latency | bucket max get object info rl _ _ _ _ _ |
| average image process server latency (0 ~ 100KB) | bucket small2 img process server latency _ _ _ _ _ |
| average image process server latency (100KB ~ 200KB) | bucket small1 img process server latency _ _ _ _ _ |
| average image process server latency (200KB ~ 1MB) | bucket small img process server latency _ _ _ _ _ |
| average image process server latency (>= 1MB) | bucket big img process server latency _ _ _ _ _ |
| max image process server latency (0 ~ 100KB) | bucket max small2 img process server latency _ _ _ _ _ _ |
| max image process server latency (100KB ~ 200KB) | bucket max small1 img process server latency _ _ _ _ _ _ |
| max image process server latency (200KB ~ 1MB) | bucket max small img process server latency _ _ _ _ _ _ |
| max image process server latency (>= 1MB) | bucket max big img process server latency _ _ _ _ _ _ |
| average image process request latency (0 ~ 100KB) | bucket small2 img process request latency _ _ _ _ _ |
| average image process request latency (100KB ~ 200KB) | bucket small1 img process request latency _ _ _ _ _ |
| average image process request latency (200KB ~ 1MB) | bucket small img process request latency _ _ _ _ _ |
| average image process request latency (>= 1MB) | bucket big img process request latency _ _ _ _ _ |

| max image process request latency (0 ~ 100KB) | bucket max small2 img process request latenc _ _ _ _ _ _ y |
|---|---|
| max image process request latency (100KB ~ 200KB) | bucket max small1 img process request latenc _ _ _ _ _ _ y |
| max image process request latency (200KB ~ 1MB) | bucket max small img process request latency _ _ _ _ _ _ |
| max image process request latency (>= 1MB) | bucket max big img process request latency _ _ _ _ _ _ |
| 5xx | bucket error 5xx _ _ |
| 503 | bucket error 503 _ _ |
| 403 | bucket error 403 _ _ |
| 404 | bucket error 404 _ _ |
| 499 | bucket error 499 _ _ |
| other 4xx | bucket error 4xx other _ _ _ |
| success 2xx | bucket success 2xx _ _ |
| success 3xx | bucket success 3xx _ _ |
| sync 5xx | bucket sync in5xx count _ _ _ |
| Storage usage | bucket storage quota _ _ |
| Storage capacity increment | bucket storage quota inc _ _ _ |
| Standard storage capacity | bucket std storage _ _ |
| Standard storage capacity increment | bucket std storage inc _ _ _ |
| IA storage capacity | bucket ia real storage _ _ _ |

| IA storage capacity increment | bucket ia real storage inc _ _ _ _ |
|---|---|
| Archive storage capacity | bucket ar real storage _ _ _ |
| Archive storage capacity increment | bucket ar real storage inc _ _ _ _ |
| Volume of written data | bucket delta add _ _ |
| Volume of deleted data | bucket delta del _ _ |

##### 7.3.2.5 DescribeStorageClusters

Queries a list of storage clusters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| storageCluster s | Array |   | The storage clusters. |
| - storageService s | Array |   | The service information of the storage cluster. |
| --tags | Array |   | The information about the tag. |
| ---id | Long | 29 | The tag ID. |
| ---tagName | String | io16 | The tag name. |
| ---tagJsonInfo | String | {\"closeable\":false ,\"color\":\"purple\", \"tagKey\":\"ioType \"} | The tag configurations. closeable: indicates whether a tag was used. color: the color of the tag. tagKey: the tag key, which is globally unique. |
| ---gmtCreate | Long | 1691395655 | The time when the tag was created. |

| psara Uni-manag onsole | er Operations |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---gmtModify | Long | 1691395655 | The time when the tag was last modified. |
| --service | String |   | The name of the service. |
| -- isPluginServic e | Boolean | false | Indicates whether the storage cluster can be scaled. |
| --isManaged | Boolean | true | Indicates whether the storage cluster is a primary cluster. |
| - storageCluster Id | String | sc- 0000266w2des2fk qw7r5 | The storage cluster ID. |
| -name | String | CdsEbsHybridClust er-A-20220927- 0f22 | The storage cluster name. |
| - totalMetaServ erNumber | Integer | 3 | The total number of meta servers. |
| - abnormalMeta ServerNumber | Integer | 0 | The number of abnormal meta servers. |
| - totalChunkSer verNumber | Integer | 6 | The total number of chunk servers. |
| - abnormalChun kServerNumbe r | Integer | 0 | The number of abnormal chunk servers. |
| - totalDiskNumb er | Integer | 84 | The total number of disks. |
| - abnormalDisk Number | Integer | 0 | The number of abnormal disks. |
| -totalSize | Long | 571492643373056 | The total capacity. Unit: bytes. |
| -totalFreeSize | Long | 564899868573696 | The used capacity. Unit: bytes. |
| - totalChunkNu mber | Long | 10 | The total number of snapshots. |

|   |   |   | Apsara Uni-manager Operations |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - totalHostNum ber | Integer | 6 | The total number of hosts. |
| - abnormalHost Number | Integer | 0 | The number of abnormal hosts. |
| -refreshErrors | String | [{\\\"entityType\\\": \\\"STORAGE CLUS _ TER\\\",\\\"failureM OCount\\\":1,\\\"sa mpleEntityId\\\":\\\" sc- 0000iyzeojfcberqw 4g9\\\",\\\"sampleE rrorMessage\\\":\\\"j ava.lang.IllegalStat eException: Duplicate key HostEntity(hostNa me=c25a04106.clo ud.a05.amtest38, clusterName=CdsC pfsCluster-A- 20230704-0599, ipAddress=10.38.4 .22, cpu=64, memory=2748779 06944, state=GOOD, machineType=PL7 2P1M2.0JRA, os=AnolisOS-8.4- 4.19-x86 64, _ sn=210235A2UBH 225000340, azone=cn-wulan- env38- amtest38001-a, idc=amtest38, room=C2-5, rack=A05, rackUnitId=6, status=NORMAL)\\\ "}]\ | The error message. |
| -media | String | hybrid | The type of the block storage. Valid values: hybrid and ssd. hybrid indicates hybrid flash storage, and ssd indicates all- flash storage. |
| -products | String | CDS:3.16 | The service category. The value is in the following format: "CDS:version information". Examples: CDS:3.16~ and CDS:~3.15. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -updatedTime | Long | 1693190066 | The time when the cluster information was last updated. |
| -overdue | Boolean | false | Indicates whether the storage cluster is expired. Valid values: true and false. |
| -zoneInfo | String | {\"isMasterZone\":\ "true\",\"myCluster Name\":\"CdsEbsH ybridCluster-A- 20220927- 0f22\",\"oppositeCl uster\":\"\",\"zone\" :\"cn-wulan- env174- amtest174001-a\"} | The information about the storage set. |
| success | Boolean | true | Indicates whether the request is successful. Valid values: true and false. |
| requestId | String | eaf53a13-141f- 49c1-86db- 5c741de5dd01 | The request ID, which is required to search for logs. |
| code | String | 200 | The returned HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | successful | The returned message. |

**Examples**

`JSON` format `{`

```json
    "code": "200",
    "message": "successful",
    "requestId": "75dcfee2-57f2-4f9a-8d2a-57480f244823",
    "storageClusters": [
```

`{`

```json
            "abnormalChunkServerNumber": 0,
            "abnormalDiskNumber": 0,
            "abnormalHostNumber": 0,
            "abnormalMetaServerNumber": 0,
            "alias": "CdsCpfsCluster-A-20230704-0598",
            "hasPanshi": false,
            "media": "hybrid",
            "name": "CdsCpfsCluster-A-20230704-0598",
            "overdue": false,
            "panguBased": false,
"products":"CDS:316~",
```

```
            products: CDS:3.16
```

`,`

```json
            "refreshErrors": "[]",
            "storageClusterId": "sc-0009itmtcei3le3zs43z",
            "storageServices": [
```

`{`

```json
                    "isManaged": true,
                    "isPluginService": true,
                    "service": "cpfs"
```

`}` `],`

```json
            "totalChunkNumber": 0,
            "totalChunkServerNumber": 0,
            "totalDiskNumber": 90,
            "totalFreeSize": 2225751910776832,
            "totalHostNumber": 6,
            "totalMetaServerNumber": 0,
            "totalSize": 2364290375876608,
            "totalUsedSize": 138538465099776,
            "updatedTime": 1695188782,
            "zoneInfo": "
{\"isMasterZone\":\"true\",\"oppositeCluster\":\"\",\"zone\":\"cn-wulan-env38-amtest380 01-a\"}"
```

`},` `{`

```json
            "abnormalChunkServerNumber": 0,
            "abnormalDiskNumber": 0,
            "abnormalHostNumber": 0,
            "abnormalMetaServerNumber": 0,
            "alias": "CdsCpfsCluster-A-20230704-0599",
            "hasPanshi": false,
            "media": "ssd",
            "name": "CdsCpfsCluster-A-20230704-0599",
            "overdue": false,
            "panguBased": false,
            "products": "CDS:3.16~",
            "refreshErrors": "[]",
            "storageClusterId": "sc-0009itmtcei3le45xoie",
            "storageServices": [
```

`{`

```json
                    "isManaged": true,
                    "isPluginService": true,
                    "service": "cpfs"
```

`}` `],`

```json
            "totalChunkNumber": 0,
            "totalChunkServerNumber": 0,
            "totalDiskNumber": 273,
            "totalFreeSize": 342356138131456,
            "totalHostNumber": 11,
            "totalMetaServerNumber": 0,
            "totalSize": 353351254409216,
            "totalUsedSize": 10995116277760,
            "updatedTime": 1695188861,
            "zoneInfo": "
{\"isMasterZone\":\"true\",\"oppositeCluster\":\"\",\"zone\":\"cn-wulan-env38-amtest380
```

`,` `pp` `,`

```
01-a\"}"
```

`},` `{`

```json
            "abnormalChunkServerNumber": 0,
            "abnormalDiskNumber": 0,
            "abnormalHostNumber": 0,
            "abnormalMetaServerNumber": 0,
            "alias": "CdsCpfsCluster-A-20230816-088a",
            "hasPanshi": false,
            "name": "CdsCpfsCluster-A-20230816-088a",
            "overdue": false,
            "panguBased": false,
            "products": "CDS:3.16~",
            "refreshErrors": "[]",
            "storageClusterId": "sc-0009itmtcei3le42sqol",
            "storageServices": [
```

`{`

```json
                    "isManaged": true,
                    "isPluginService": true,
                    "service": "cpfs"
```

`}` `],`

```json
            "totalChunkNumber": 0,
            "totalChunkServerNumber": 0,
            "totalDiskNumber": 64,
            "totalFreeSize": 0,
            "totalHostNumber": 6,
            "totalMetaServerNumber": 0,
            "totalSize": 0,
            "totalUsedSize": 0,
            "updatedTime": 1695188800,
            "zoneInfo": "
{\"isMasterZone\":\"true\",\"oppositeCluster\":\"\",\"zone\":\"cn-wulan-env38-amtest380 01-a\"}"
```

`},` `{`

```json
            "abnormalChunkServerNumber": 0,
            "abnormalDiskNumber": 0,
            "abnormalHostNumber": 0,
            "abnormalMetaServerNumber": 0,
            "alias": "CdsEbsOssHybridCluster-A-20221210-0068",
            "hasPanshi": true,
            "media": "hybrid",
            "name": "CdsEbsOssHybridCluster-A-20221210-0068",
            "overdue": false,
            "panguBased": true,
            "products": "CDS:3.16",
            "refreshErrors": "[]",
            "storageClusterId": "sc-0009itmtcei3le46tifx",
            "storageServices": [
```

`{`

```json
                    "isManaged": true,
                    "isPluginService": false,
                    "service": "ebs",
```

```json
                    "tags": [
```

`{`

```json
                            "gmtCreate": 1693816339,
                            "gmtModify": 1693816339,
                            "id": 5,
                            "tagJsonInfo": "
{\"closeable\":false,\"color\":\"purple\",\"tagKey\":\"ioType\"}",
                            "tagName": "io16"
```

`}` `]` `},` `{`

```json
                    "isManaged": true,
                    "isPluginService": false,
                    "service": "oss",
                    "tags": []
```

`}` `],`

```json
            "totalChunkNumber": 22116432,
            "totalChunkServerNumber": 6,
            "totalDiskNumber": 84,
            "totalFreeSize": 508645460672512,
            "totalHostNumber": 6,
            "totalMetaServerNumber": 3,
            "totalSize": 814263522295808,
            "totalUsedSize": 305618061623296,
            "updatedTime": 1695188801,
            "zoneInfo": "
{\"isMasterZone\":\"true\",\"myClusterName\":\"CdsEbsOssHybridCluster-A-20221210-0068\" ,\"oppositeCluster\":\"\",\"zone\":\"cn-wulan-env38-amtest38001-a\"}"
```

`}` `],`

```json
    "success": true
```

`}` `XML` format

```xml
<code>200</code> <message>successful</message> <requestId>75dcfee2-57f2-4f9a-8d2a-57480f244823</requestId> <storageClusters>
 <abnormalChunkServerNumber>0</abnormalChunkServerNumber>
 <abnormalDiskNumber>0</abnormalDiskNumber>
 <abnormalHostNumber>0</abnormalHostNumber>
 <abnormalMetaServerNumber>0</abnormalMetaServerNumber>
 <alias>CdsCpfsCluster-A-20230704-0598</alias>
 <hasPanshi>false</hasPanshi>
 <media>hybrid</media>
 <name>CdsCpfsCluster-A-20230704-0598</name>
 <overdue>false</overdue>
 <panguBased>false</panguBased>
 <products>CDS:3.16~</products>
 <refreshErrors>[]</refreshErrors>
 <storageClusterId>sc-0009itmtcei3le3zs43z</storageClusterId>
```

```
stoageCuste dsc0009ttce3e3s3 /stoageCuste
```

`d`

```xml
 <storageServices>
  <isManaged>true</isManaged>
  <isPluginService>true</isPluginService>
  <service>cpfs</service>
 </storageServices>
 <totalChunkNumber>0</totalChunkNumber>
 <totalChunkServerNumber>0</totalChunkServerNumber>
 <totalDiskNumber>90</totalDiskNumber>
 <totalFreeSize>2225751910776832</totalFreeSize>
 <totalHostNumber>6</totalHostNumber>
 <totalMetaServerNumber>0</totalMetaServerNumber>
 <totalSize>2364290375876608</totalSize>
 <totalUsedSize>138538465099776</totalUsedSize>
 <updatedTime>1695188782</updatedTime>
 <zoneInfo>
{&quot;isMasterZone&quot;:&quot;true&quot;,&quot;oppositeCluster&quot;:&quot;&quot;,&quot one&quot;:&quot;cn-wulan-env38-amtest38001-a&quot;}</zoneInfo> </storageClusters> <storageClusters>
 <abnormalChunkServerNumber>0</abnormalChunkServerNumber>
 <abnormalDiskNumber>0</abnormalDiskNumber>
 <abnormalHostNumber>0</abnormalHostNumber>
 <abnormalMetaServerNumber>0</abnormalMetaServerNumber>
 <alias>CdsCpfsCluster-A-20230704-0599</alias>
 <hasPanshi>false</hasPanshi>
 <media>ssd</media>
 <name>CdsCpfsCluster-A-20230704-0599</name>
 <overdue>false</overdue>
 <panguBased>false</panguBased>
 <products>CDS:3.16~</products>
 <refreshErrors>[]</refreshErrors>
 <storageClusterId>sc-0009itmtcei3le45xoie</storageClusterId>
 <storageServices>
  <isManaged>true</isManaged>
  <isPluginService>true</isPluginService>
  <service>cpfs</service>
 </storageServices>
 <totalChunkNumber>0</totalChunkNumber>
 <totalChunkServerNumber>0</totalChunkServerNumber>
 <totalDiskNumber>273</totalDiskNumber>
 <totalFreeSize>342356138131456</totalFreeSize>
 <totalHostNumber>11</totalHostNumber>
 <totalMetaServerNumber>0</totalMetaServerNumber>
 <totalSize>353351254409216</totalSize>
 <totalUsedSize>10995116277760</totalUsedSize>
 <updatedTime>1695188861</updatedTime>
 <zoneInfo>
{&quot;isMasterZone&quot;:&quot;true&quot;,&quot;oppositeCluster&quot;:&quot;&quot;,&quot one&quot;:&quot;cn-wulan-env38-amtest38001-a&quot;}</zoneInfo> </storageClusters> <storageClusters>
 <abnormalChunkServerNumber>0</abnormalChunkServerNumber>
 <abnormalDiskNumber>0</abnormalDiskNumber>
 <abnormalHostNumber>0</abnormalHostNumber>
```

```xml
 <abnormalMetaServerNumber>0</abnormalMetaServerNumber>
 <alias>CdsCpfsCluster-A-20230816-088a</alias>
 <hasPanshi>false</hasPanshi>
 <name>CdsCpfsCluster-A-20230816-088a</name>
 <overdue>false</overdue>
 <panguBased>false</panguBased>
 <products>CDS:3.16~</products>
 <refreshErrors>[]</refreshErrors>
 <storageClusterId>sc-0009itmtcei3le42sqol</storageClusterId>
 <storageServices>
  <isManaged>true</isManaged>
  <isPluginService>true</isPluginService>
  <service>cpfs</service>
 </storageServices>
 <totalChunkNumber>0</totalChunkNumber>
 <totalChunkServerNumber>0</totalChunkServerNumber>
 <totalDiskNumber>64</totalDiskNumber>
 <totalFreeSize>0</totalFreeSize>
 <totalHostNumber>6</totalHostNumber>
 <totalMetaServerNumber>0</totalMetaServerNumber>
 <totalSize>0</totalSize>
 <totalUsedSize>0</totalUsedSize>
 <updatedTime>1695188800</updatedTime>
 <zoneInfo>
{&quot;isMasterZone&quot;:&quot;true&quot;,&quot;oppositeCluster&quot;:&quot;&quot;,&quot one&quot;:&quot;cn-wulan-env38-amtest38001-a&quot;}</zoneInfo> </storageClusters> <storageClusters>
 <abnormalChunkServerNumber>0</abnormalChunkServerNumber>
 <abnormalDiskNumber>0</abnormalDiskNumber>
 <abnormalHostNumber>0</abnormalHostNumber>
 <abnormalMetaServerNumber>0</abnormalMetaServerNumber>
 <alias>CdsEbsOssHybridCluster-A-20221210-0068</alias>
 <hasPanshi>true</hasPanshi>
 <media>hybrid</media>
 <name>CdsEbsOssHybridCluster-A-20221210-0068</name>
 <overdue>false</overdue>
 <panguBased>true</panguBased>
 <products>CDS:3.16</products>
 <refreshErrors>[]</refreshErrors>
 <storageClusterId>sc-0009itmtcei3le46tifx</storageClusterId>
 <storageServices>
  <isManaged>true</isManaged>
  <isPluginService>false</isPluginService>
  <service>ebs</service>
  <tags>
   <gmtCreate>1693816339</gmtCreate>
   <gmtModify>1693816339</gmtModify>
   <id>5</id>
   <tagJsonInfo>
{&quot;closeable&quot;:false,&quot;color&quot;:&quot;purple&quot;,&quot;tagKey&quot;:&quo ioType&quot;}</tagJsonInfo>
   <tagName>io16</tagName>
  </tags>
```

```xml
 </storageServices>
 <storageServices>
  <isManaged>true</isManaged>
  <isPluginService>false</isPluginService>
  <service>oss</service>
  <tags  />
 </storageServices>
 <totalChunkNumber>22116432</totalChunkNumber>
 <totalChunkServerNumber>6</totalChunkServerNumber>
 <totalDiskNumber>84</totalDiskNumber>
 <totalFreeSize>508645460672512</totalFreeSize>
 <totalHostNumber>6</totalHostNumber>
 <totalMetaServerNumber>3</totalMetaServerNumber>
 <totalSize>814263522295808</totalSize>
 <totalUsedSize>305618061623296</totalUsedSize>
 <updatedTime>1695188801</updatedTime>
 <zoneInfo>
{&quot;isMasterZone&quot;:&quot;true&quot;,&quot;myClusterName&quot;:&quot;CdsEbsOssHybri luster-A-20221210- 0068&quot;,&quot;oppositeCluster&quot;:&quot;&quot;,&quot;zone&quot;:&quot;cn-wulan-env 38-amtest38001-a&quot;}</zoneInfo> </storageClusters> <success>true</success>
```

##### 7.3.2.6 DescribeBlockClusters

Queries the information about a block storage cluster based on the cluster ID.

**Request headers**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OpsProduc t | Strin g | Hea der | No |   |   |

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| storageClu sterId | Strin g | Body | No | sc- 000ekx55q5me4udn21jp | The block storage cluster ID. |

**Response parameters**

| > Document Versi | on: 20251107 |   | 51 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| blockClusters | Array |   |   |
| -blockClusterId | String | bc- 000021owan7tk5o sxnf0 | The block storage cluster ID. |
| -clusterName | String | ECS-IO7-A-00a4 | The block storage cluster name. |
| - clusterAliasNa me | String | ECS-IO7-A-00a4 | The block storage cluster alias. |
| -totalSale | Long | 16580721246208 | The used logical space. Unit: bytes. |
| -totalUsedSize | Long | 14547054231552 | The used physical space. Unit: bytes. |
| - totalBlockMast erNumber | Long | 3 | The number of normal block masters of the primary server. |
| - abnormalBlock MasterNumber | Long | 0 | The number of abnormal block masters of the primary server. |
| - totalBlockServ erNumber | Long | 4 | The number of normal block masters of the storage server. |
| - abnormalBlock ServerNumber | Long | 0 | The number of abnormal block masters of the storage server. |
| - totalBlockDevi ceNumber | Long | 150 | The number of normal disks. |
| - abnormalBlock DeviceNumber | Long | 0 | The number of abnormal disks. |
| - totalSnapshot Number | Long | 25 | The number of normal snapshots. |

| - abnormalSnap shotNumber | Long | 0 | The number of abnormal snapshots. |
|---|---|---|---|
| -storageType | String | io7 | The I/O type. |
| -products | String | EBS-1.0:~ | CDS:~: cds. OSS:~: oss. EBS-1.0:~: ecs. EBS-2.0:~3.14: ecs. EBS-2.0:3.15~: cds. PanguStack:~: tianji. |
| -zoneInfo | String | {\"isMasterZone\":\ "true\",\"oppositeCl uster\":\"\",\"zone\" :\"cn-wulan- env212- amtest212001-a\"} | The service information of the cluster storage set. |
| success | Boolean | true | Indicates whether the request is successful. Valid values: true and false. |
| requestId | String | f893bad3-66f3- 4b84-9411- 85375d3429b0 | The request ID. |
| code | String | 200 | The returned HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. |
| message | String | successful | The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned. |

**Examples**

Sample requests `{`

```json
    "storageClusterId":"sc-0000266w2des2hk08oj6"
```

`}` Sample success responses `JSON` format `{`

```json
 "code": "200",
 "data": {
  "blockClusters": [{
   "blockClusterId": "bc-000021owan7tk5osxnf0",
   "abnormalSnapshotNumber": 0,
   "totalSnapshotNumber": 25,
   "totalUsedSize": 14547054231552,
   "abnormalBlockDeviceNumber": 0,
   "abnormalBlockServerNumber": 0,
   "products": "EBS-1.0:~",
   "totalBlockDeviceNumber": 150,
   "zoneInfo": "{\"isMasterZone\":\"true\",\"oppositeCluster\":\"\",\"zone\":\"cn-wulan
-env212-amtest212001-a\"}",
   "abnormalBlockMasterNumber": 0,
   "clusterName": "ECS-IO7-A-00a4",
   "totalBlockMasterNumber": 3,
   "storageType": "io7",
   "totalSale": 16580721246208,
   "totalBlockServerNumber": 4
  }],
  "eagleEyeTraceId": "0ad414c416932924601235587e0033",
  "asapiSuccess": true,
  "code": "200",
  "asapiRequestId": "f893bad3-66f3-4b84-9411-85375d3429b0",
  "success": true,
  "requestId": "f893bad3-66f3-4b84-9411-85375d3429b0",
  "message": "successful"
```

`},`

```json
 "cost": 27,
 "apiCost": 25,
 "eagleEyeTraceId": "0ad414c416932924601235587e0033",
 "successResponse": true
```

`}`

### 7.4 ApsaraDB Operations and Maintenance System

**Maintenance System**

#### 7.4.1 RDS O&M

##### 7.4.1.1 DescribeHostInfoByDbType

Queries host information based on the specified database engine.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Engine | Strin g | Query | Yes | mysql | The database engine of the instance. |
| CpuLabel | Strin g | Query | No | intel | The chip type. |
| IsolateHos t | Strin g | Query | No | 0 | The isolation level. |
| RequestId | Strin g | Query | Yes | 0ab4107a1t3wq6a6aaq 73561d0a106144 | The request ID. |
| Action | Strin g | Query | No | DescribeHostInfoByDbTy pe | The operation that you want to perform. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The returned HTTP status code. |
| Message | String | successful | The returned message that indicates whether the request is successful. |
| Data | Struct |   | The response data. |
| Items | Array of Items |   | The returned data. |
| dbType | String | "" | The database engine of the instance. |
| hostIp | String | 10.10.1.1 | The IP address of the host. |
| hostName | String | a36b04135.cloud.b 05.amtest17 | The name of the host. |
| subDomain | String | cn-XXX-XXX-XXX | The subdomain name. |
| siteName | String | amtest17 | The name of data center. |
| cabinet | String | a36b041 | The name of the cabinet. |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| dbVersion | String | 5.6 | The version of the database engine. |
| ecsHost | Boolean | false | Indicates whether the instance is an ECS instance. |
| label | String | intel\|x86\|mix | The chip of the host. |
| isolateHost | Integer | 0 | The isolation level. 0: shared 1: dedicated host 2: dedicated 3: idle |
| memSizeForSa le | Integer | 174785 | The memory size available for sale. |
| memSizeUsed Scale | Integer | 174785 | The memory size available for use. |
| memSizeSold | Integer | 110592 | The memory size that is sold. |
| memSizeUsed | Integer | 64097 | The used memory size. |
| diskSizeForSal e | Integer | 4875422 | The disk size available for sale. |
| diskSizeUsedS cale | Integer | 3412795 | The disk size available for use. |
| diskSizeSold | Integer | 4817920 | The disk size that is sold. |
| dataSpaceUse d | Integer | 38427 | The used disk size. |
| cpuCores | Integer | 40 | The number of CPU cores. |
| cpuCoresForSa le | Integer | 360000 | The number of CPU cores available for sale. |
| cpuCoresSold | Integer | 52 | The number of CPU cores that are sold. |
| insCount | Integer | 27 | The number of existing instances. |

| psara Uni-manag | er Operations |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| status | Integer | 1 | The state of the host. Valid values: 1: normal 2: faulty 3: ready for deactivation. |
| serviceStatus | Integer | 1 | The health state. 1: normal 2: abnormal |
| isAvail | Boolean | true | Indicates whether the host is available. |
| avail | Integer | 1 | Indicates whether the host is disabled for allocation. |
| comment | String | Available now. | The current state phrase of the host. |
| summary | String | "" | The summary. |
| exceptionStac k | Boolean | "" | The error stack. |
| requestId | String | "" | The request ID. |
| traceId | String | "" | The trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ops.api.rds.DescribeHostInfoByDbType.2023-08-17 &Engine=mysql &RequestId=0ab4107a1t3wq6a6aaq73561d0a106144 &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "summary":"""",
 "traceId":"""",
 "exceptionStack":false,
 "Message":"successful",
 "requestId":"""",
 "Data":{
  "Items":{
   "memSizeUsed":64097,
   "hostName":"a36b04135.cloud.b05.amtest17",
   "subDomain":"cn-XXX-XXX-XXX",
   "siteName":"amtest17",
   "memSizeForSale":174785,
   "dataSpaceUsed":38427,
   "isAvail":true,
   "serviceStatus":1,
   "cpuCoresSold":52,
   "diskSizeForSale":4875422,
   "ecsHost":false,
   "avail":1,
   "hostIp":"10.10.1.1",
   "isolateHost":0,
   "dbVersion":"5.6",
   "dbType":"""",
   "label":"intel|x86|mix",
   "insCount":27,
   "diskSizeSold":4817920,
   "memSizeUsedScale":174785,
   "diskSizeUsedScale":3412795,
   "cpuCores":40,
   "cpuCoresForSale":360000,
   "memSizeSold":110592,
   "comment":"Available now.",
   "cabinet":"a36b041",
   "status":1
```

`}` `},`

```json
 "Code":"200"
```

`}`

##### 7.4.1.2 DescribeCustInsSlaveInfo

Queries the connection information about the secondary database based on the specified instance name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

**q**

**p**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| instanceN ame | Strin g | Query | Yes | dds- 3jl17fbba9336e74.2023 0816145326 | The name of the instance. |
| RequestId | Strin g | Query | Yes | 0ab4107a1t3wq6a6aaq 73561d0a106145 | The request ID. |
| Action | Strin g | Query | No | DescribeCustInsSlaveInf o | The operation that you want to perform. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The returned HTTP status code. |
| Message | String | successful | The returned message that indicates whether the request is successful. |
| Data | Struct |   | The response data. |
| describeCustIn sSlaveInfo | Array of describeCustIn sSlaveInfo |   | The returned data. |
| hostId | String | 21 | The ID of the secondary database. |
| ip | String | 10.10.1.1 | The IP address of the secondary database. |
| port | String | 3005 | The port of the secondary database. |
| summary | String | "" | The summary. |
| exceptionStac k | Boolean | "" | The error stack. |
| requestId | String | "" | The request ID. |
| traceId | String | "" | The trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ops.api.rds.DescribeCustInsSlaveInfo.2023-08-17 &instanceName=dds-3jl17fbba9336e74.20230816145326 &RequestId=0ab4107a1t3wq6a6aaq73561d0a106145 &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "summary":"""",
 "traceId":"""",
 "exceptionStack":false,
 "Message":"successful",
 "requestId":"""",
 "Data":{
  "describeCustInsSlaveInfo":{
   "port":"3005",
   "ip":"10.10.1.1",
   "hostId":"21"
```

`}` `},`

```json
 "Code":"200"
```

`}`

##### 7.4.1.3 DescribeResourceInventory

Obtains the resource information of the specified subdomain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Engine | Strin g | Query | No | mysql | The database engine of the instance. |
| RequestId | Strin g | Query | Yes | 0ab4107a1t3wq6a6aaq 73561d0a106146 | The request ID. |
| SubDomai n | Strin g | Query | Yes | cn-XXX-XXX-XXX | The subdomain name. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Query | No | DescribeResourceInvent ory | The operation that you want to perform. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The returned HTTP status code. |
| Message | String | successful | The returned message that indicates whether the request is successful. |
| Data | Struct |   | The response data. |
| SubDomain | String | cn-XXX-XXX-XXX | The subdomain name. |
| Items | Array of Items |   | The returned data. |
| Engine | String | Redis | The database engine of the instance. |
| HostType | String | 0 | The type of the host. 0: SSD 1: SATA 3: HyBird |
| ResourceType | String | cpu | The type of the resource. Valid values: memory, disk, and cpu. |
| ResourceUnit | String | core | The unit of the resource type. |
| ResourceTotal | String | 160 | The total number of resources. |
| ResourceUsed | String | 10 | The number of used resources. |
| ResourceSold | String | 870 | The number of resources that are sold. |
| ResourceSoldC eiling | String | 144 | The maximum number of resources that can be sold. |

|   | Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| summary | String | "" | The summary. |
| exceptionStac k | Boolean | "" | The error stack. |
| requestId | String | "" | The request ID. |
| traceId | String | "" | The trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ops.api.rds.DescribeResourceInventory.2023-08-17 &RequestId= &SubDomain= &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "summary":"""",
 "traceId":"""",
 "exceptionStack":false,
 "Message":"successful",
 "requestId":"""",
 "Data":{
  "SubDomain":"cn-XXX-XXX-XXX",
  "Items":{
   "ResourceUnit":"core",
   "HostType":"0",
   "ResourceTotal":"160",
   "ResourceSold":"870",
   "ResourceUsed":"10",
   "ResourceType":"cpu",
   "Engine":"Redis",
   "ResourceSoldCeiling":"144"
```

`}` `},`

```json
 "Code":"200"
```

`}`

##### 7.4.1.4 DescribeComboInventory

Queries the inventory of a resource combination.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Engine | Strin g | Query | No | mysql | The database engine of the instance. |
| RequestId | Strin g | Query | Yes | 0ab4107a1t3wq6a6aaq 73561d0a106147 | The request ID. |
| SubDomai n | Strin g | Query | Yes | cn-XXX-XXX-XXX | The subdomain name. |
| Action | Strin g | Query | No | DescribeComboInventor y | The operation that you want to perform. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The returned HTTP status code. |
| Message | String | successful | The returned message that indicates whether the request is successful. |
| Data | Struct |   | The response data. |
| SubDomain | String | cn-XXX-XXX-XXX | The subdomain name. |
| Items | Array of Items |   | The returned data. |
| Engine | String | redis | The database engine of the instance. |
| EngineVersion | String | 2.8 | The version of the database engine. |
| HostType | String | 0 | The type of the host. 0: SSD 1: SATA 3: HyBird |

| Developer Guide·A | PI Reference |   | Apsara Uni-manager Operations Consol |
|---|---|---|---|
| Parameter | Type | Example | Description |
| MemSize | Integer | 1024 | The memory size. |
| DiskSize | Integer | 20480 | The disk size. |
| CpuCores | Integer | 3 | The number of CPU cores. |
| ClassCode | String | redis.master.small. special1x | The code of the instance type. |
| IsolateLevel | String | 0 | The isolation level. 0: shared 1: dedicated 2: dedicated host |
| AvailableCoun t | Integer | 0 | The number of instances that can be created. |
| summary | String | "" | The summary. |
| exceptionStac k | Boolean | "" | The error stack. |
| requestId | String | "" | The request ID. |
| traceId | String | "" | The trace ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ops.api.rds.DescribeComboInventory.2023-08-17 &RequestId=0ab4107a1t3wq6a6aaq73561d0a106147 &SubDomain=cn-XXX-XXX-XXX &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "summary":"""",
 "traceId":"""",
 "exceptionStack":false,
 "Message":"successful",
 "requestId":"""",
 "Data":{
  "SubDomain":"cn-XXX-XXX-XXX",
  "Items":{
   "IsolateLevel":"0",
   "HostType":"0",
   "EngineVersion":"2.8",
   "ClassCode":"redis.master.small.special1x",
   "MemSize":1024,
   "DiskSize":20480,
   "CpuCores":3,
   "AvailableCount":0,
   "Engine":"redis"
```

`}` `},`

```json
 "Code":"200"
```

`}`

### 7.5 Apsara Uni-manager Management Console

**Management Console**

#### 7.5.1 Platform data

##### 7.5.1.1 GetCurrentUserStats

Queries the user statistics of Apsara Uni-manager Management Console.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /openapi/popResource/ascm/auth/stat/user HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| currentPage | Integer | Body | No | 1 | The page number. |
|---|---|---|---|---|---|
| pageSize | Integer | Body | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The response code. |
| cost | Integer | 17 | The time spent on querying the user statistics. Unit: milliseconds. |
| data | Array of JSONArray |   | The returned data. |
| loginName | String | test login name _ _ | The account name used to log on to Apsara Uni-manager Management Console. |
| sessionInfoList | Array of JSONArray |   | The login information of the user. |
| loginTime | Long | 1655045432302 | The time when the user logged on. |
| username | String | test user _ | The user name. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number. |
| pageSize | Integer | 10 | The number of entries per page. |
| total | Integer | 27 | The total number of entries returned. |
| totalPage | Integer | 24 | The total number of pages returned. |
| message | String | Parameter error | The error message. |
| success | Boolean | true | Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed. |

**Examples**

Sample requests

```
POST /openapi/popResource/ascm/auth/stat/user HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
    "cost": "17",
    "code": "200",
    "data": [
```

`{`

```json
            "loginName": "test_login_name",
            "username": "test_user",
            "sessionInfoList": [
```

`{`

```json
                    "loginTime": "1655045432302"
```

`}` `]` `}` `],`

```json
    "success": "true",
    "pageInfo": {
        "total": "27",
        "totalPage": "24",
        "pageSize": "10",
        "currentPage": "1"
```

`},`

```json
    "message": "Parameter error"
```

`}`

## 8 References

### 8.1 QPS of API operations

To ensure the stability of the Apsara Uni-manager Operations Console, the queries per second (QPS) of API operations is limited to 10 by default, which indicates that a maximum of 10 requests are allowed per second. Generally, the return data of an API operation is real-time data at the minute level. Therefore, the QPS of 10 can meet business requirements.

### 8.2 Troubleshooting based on logs when an API operation call is abnormal

**when an API operation call is**

**abnormal**

If an API operation call is abnormal, provide the following information for troubleshooting. Java SDK i. Request ID

```java
// Add the request ID for debugging and print it to the logs to facilitate troubles hooting. String uuid = UUID.randomUUID().toString(); getMachineListDetailRequest.putHeaderParameter("test-request-id", uuid); System.out.println("request uuid" + uuid);
```

ii. Return value printing

```java
System.out.println("Error response is: " + JSONObject.toJSONString(getMachineListDetailResponse));
```

Python SDK i. Request ID

```python
# Add the request ID for debugging and print it to the logs to facilitate troublesh
ooting. uuidstr = str(uuid.uuid4()) describeProductStatusInstance.add_header("test-request-id", uuidstr) print(uuidstr)
```

ii. Return value printing

```python
strDescribeProductStatusResponse = str(describeProductStatusResponse, encoding="utf -8") describeProductStatusJsonResponse = json.loads(strDescribeProductStatusResponse) if describeProductStatusJsonResponse != None and describeProductStatusJsonResponse.message == "success":
    print(strDescribeProductStatusResponse)
```
