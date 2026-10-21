---
title: "Alibaba Cloud Apsara Stack V3.18.3 Container Service for Kubernetes Operations and Maintenance Guide 20241213"
product_version: "V3.18.3"
doc_version: "20241213"
pdf_pages: 26
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Container Service for Kubernetes Operations and Maintenance Guide 20241213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1ACK/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Container%20Service%20for%20Kubernetes%20Operations%20and%20Maintenance%20Guide%2020241213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Container Service for Kubernetes Operations and Maintenance Guide 20241213

## Table of Contents

- 1 Before you begin
- 2 Architecture
  - 2.1 System architecture
  - 2.2 Architecture
  - 2.3 Deployment architecture
  - 2.4 Server roles
- 3 Components and features
  - 3.1 Console
  - 3.2 Troopers
  - 3.3 Mirana
- 4 System restart
  - 4.1 Restart a control node
- 5 Manage certificates for control components

## 1 Before you begin

Container Service for Kubernetes (ACK) provides container services. You may encounter service interruptions if you perform improper operations on applications in your ACK clusters. This topic describes the usage notes of ACK clusters and instructions on high-risk operations. This helps you learn the risks that may arise when you use ACK clusters.

**Usage notes**

**Data plane components**

Data plane components are system components that run on your Elastic Compute Service (ECS) instances. Data plane components include CoreDNS, Ingresses, kube-proxy, Terway, and the kubelet. You and the ACK team must collaborate to ensure the stability of data plane components that run on your ECS instances. When you use data plane components, we recommend that you take note of the following items: Modifying the component configuration may cause the component to malfunction. Exercise caution when you modify the component configuration. For more information about how to manage components in the ACK console, choose **User Guide for ACK** > **Components** >
**Manage components**.
Do not use the APIs of Infrastructure as a service (IaaS) services to modify the environment of data plane components. For example, do not use the ECS API to change the status of the ECS instances on which data plane components run, or modify the security groups or network settings of the worker nodes. Do not use the Server Load Balancer (SLB) API to modify the configurations of the SLB instances that are used by your cluster. Improper changes to the IaaS resources may cause the components to malfunction. Several data plane components may have the same bugs or vulnerabilities as the corresponding open source versions. Update your components at the earliest opportunity in case the bugs or vulnerabilities affect your business.

**Cluster updates**

Use the cluster update feature that is provided by ACK to update the Kubernetes version of ACK clusters. If you use other methods to update the Kubernetes version of your ACK clusters, stability or compatibility issues may occur in the ACK clusters. For more information about how to manage components in the ACK console, choose **User Guide for ACK** > **Kubernetes**
**clusters** > **Clusters** > **Update the Kubernetes version of a cluster** .
ACK provides the following features to update clusters: Version updates for ACK clusters. Release notes to describe new Kubernetes versions and compare new versions with earlier versions. Pre-update notifications that inform you of the risks that may arise due to resource changes caused by version updates. We recommend that you follow these suggestions when you use the cluster update feature: Read the release notes of the new Kubernetes versions, confirm the status of the cluster and workloads based on the update risks that are reported by ACK, and evaluate the impacts of the risks. For more information about how to manage components in the ACK console, choose **User Guide for ACK** > **Announcements** and choose **User Guide for**
**ACK** > **Kubernetes clusters** > **Clusters** > **Update the Kubernetes version of a**
**cluster**.
You cannot roll back cluster updates. Before you update a cluster, prepare for the update and make sure that you have a backup plan.

**Kubernetes configurations**

Do not change key Kubernetes configurations. For example, do not change the following directories or modify the paths, links, and content of the files in the directories: /var/lib/kubelet /var/lib/docker /etc/kubernetes /etc/kubeadm /var/lib/containerd Do not use annotations that are reserved by Kubernetes in YAML templates. Otherwise, resource unavailability, application failures, and exceptions may occur. Labels prefixed with

| kubernetes.io/ |   | or | k8s.io/ | are reserved for key comp |
|---|---|---|---|---|
| the annotation |   |   |   |   |

**App catalog**

The application marketplace of ACK provides the app catalog feature to help you install applications that are developed based on open source versions. Open source applications may have potential risks. Proceed with caution.

**High-risk operations**

The following high-risk operations may adversely affect your business when you work with ACK. Read and understand the impacts of the following high-risk operations before you perform these operations:

**High-risk operations on clusters**

| Category | High-risk operation | Impact | How to recover |
|---|---|---|---|
| API Server | Delete the SLB instance that is used to expose the API server. | You cannot manage the cluster. | Unrecoverable. You must create a new cluster. |
| Worker nodes | Modify the security group of nodes. | The nodes may become unavailable. | Add the master nodes to the original security groups again. The security groups are created when you create the cluster. For more information, choose User Guide for ECS > Security groups > Add an instance to a security group. |
|   | Remove nodes. | The nodes become unavailable. | Unrecoverable. |
|   | Reinstall the node OS. | Components are uninstalled from nodes. | Remove the worker nodes and then add the nodes to the cluster again. |
|   | Update component versions. | The nodes may become unavailable. | Roll back to the original component versions. |
|   | Change the IP addresses of nodes. | The nodes become unavailable. | Change the IP addresses of the nodes to the original IP addresses. |

|   | Modify the parameters of key components, such as kubelet, docker, and containerd. | The nodes may become unavailable. | Refer to the ACK official documentation and configure the component parameters. |
|---|---|---|---|
|   | Modify node OS configurations. | The nodes may become unavailable. | Restore the configurations, or remove the worker nodes and then purchase new nodes. |
|   | Modify the security group of master nodes. | The master nodes may become unavailable. | Add the master nodes to the original security groups again. The security groups are created when you create the cluster. For more information, choose User Guide for ECS > Security groups > Add an instance to a security group. |
| Master nodes in ACK dedicated clusters |   |   |   |
|   | Remove master nodes. | The master nodes become unavailable. | Unrecoverable. |
|   | Reinstall the node OS. | Components are uninstalled from master nodes. | Unrecoverable. |
|   | Update master nodes or the etcd component. | The cluster may become unavailable. | Roll back to the original version. |
|   | Delete or format the directories that store business-critical data on nodes, for example, /etc/kubernetes. | The master nodes become unavailable. | Unrecoverable. |
|   | Change the IP addresses of master nodes. | The master nodes become unavailable. | Change the IP addresses of the master nodes to the original IP addresses. |
|   | Modify the parameters of key components, such as etcd, kube-apiser, and docker. | The master nodes may become unavailable. | Refer to the ACK official documentation and configure the component parameters. |
|   | Replace the certificates of master nodes or the etcd. | The cluster may become unavailable. | Unrecoverable. |
|   | Increase or decrease the number of master nodes. | The cluster may become unavailable. | Unrecoverable. |
| Other services | Use Resource Access Management (RAM) to modify permissions. | Resources such as SLB instances may fail to be created. | Restore the permissions. |

**High-risk operations on node pools**

| High-risk operation | Impact | How to recover |
|---|---|---|

| Delete scaling groups. | Node pool exceptions occur. | Unrecoverable. You must create new node pools. |
|---|---|---|
| Use kubectl to remove nodes from a node pool. | The number of nodes in the node pool that is displayed in the ACK console is different from the actual number. | Remove the nodes by using the ACK console or by calling the ACK API. For more information about how to manage components in the ACK console, choose User Guide for ACK > Kubernetes clusters > Nodes > Remove a node and Node pools. |
| Manually release ECS instances. | Incorrect information may be displayed on the node pool details page. | Unrecoverable. Remove the nodes by using the ACK console or by calling the ACK API. For more information about how to manage components in the ACK console, choose User Guide for ACK > Kubernetes clusters > Nodes > Remove a node and Node pools. |
| Manually scale in or scale out a node pool that has auto scaling enabled. | The auto scaling component automatically adjusts the number of nodes in the node pool after you manually scale in or scale out the node pool. | Unrecoverable. You do not need to manually scale a node pool that has auto scaling enabled. |
| Change the upper or lower limit of instances that a scaling group can contain. | Scaling errors may occur. | For a node pool that has auto scaling disabled, the default upper limit of instances for the scaling group is 2,000, and the default lower limit of instances is 0. For a node pool that has auto scaling enabled, make sure that the upper and lower limits of instances for the scaling group are the same as the upper and lower limits of instances for the node pool. |
| Add existing nodes to a cluster without backing up the data on the nodes. | The data on the nodes is lost after the nodes are added to the cluster. | Unrecoverable. If you want to add existing nodes in Manual mode, you must first back up the data on the nodes. If you want to add existing nodes in Auto mode, you must first back up the data on the system disks because the system disks will be replaced when the nodes are added to the cluster. |

**High-risk operations on networks and load balancing**

| High-risk operation | Impact | How to recover |
|---|---|---|

|   | Specify the following kernel setting: net.ipv4.ip forward=0 . _ |   |   | Network connectivity issues occur. |   |   | Replace the setting with the following content: net.ipv4.ip forward=1 . _ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   | Specify the following kernel parameter settings: net.ipv4.conf.all.rp fil _ ter = 1\|2 |   |   |   |   |   | Replace the settings with the following content: net.ipv4.conf.all.rp fil _ ter = 0 |   |   |   |
|   |   | net.ipv4.conf.all.rp fil _ |   |   |   |   |   |   |   |   |
|   | ter = 1\|2 |   |   |   |   |   |   |   |   |   |
|   |   | net.ipv4.conf. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | net.ipv4.conf.all.rp fil _ |   |   |
|   | [ethX].rp filter = 1\|2 _ |   |   |   |   |   |   |   |   |   |
|   |   |   |   | Network connectivity issues occur. | connectivity issues |   | ter = 0 |   |   |   |
|   |   |   |   |   |   |   |   | net.ipv4.conf. |   |   |
|   | Specify the following kernel setting: net.ipv4.tcp tw reuse = _ _ 1 . |   |   | Pods fail to pass health checks. |   |   | Replace the setting with the following content: net.ipv4.tcp tw reuse = _ _ 0 . |   |   |   |
|   | Specify the following kernel setting: net.ipv4.tcp tw recycle = _ _ 1 . |   |   | Network address translation errors occur. |   |   | Replace the setting with the following content: net.ipv4.tcp tw recycle = _ _ 0 . |   |   |   |
|   | Specify the following kernel setting: net.ipv4.ip local port ran _ _ _ ge . |   |   | Network connectivity issues occasionally occur. |   |   | Replace the setting with the following content: net.ipv4.ip local port ran _ _ _ ge="32768 60999" . |   |   |   |
|   | Install firewall software, for example, Firewalld or ufw. |   |   | The container network become inaccessible. |   |   | Uninstall the firewall software and restart the nodes. |   |   |   |
|   | The security group of a node does not open UDP port 53 for the pod CIDR block. |   |   | DNS resolutions cannot be performed as normal in the cluster. |   |   | Refer to the ECS official documentation and modify the security group configuration to open UDP port 53 for the pod CIDR block. |   |   |   |
|   | Modify or delete the tags that ACK added to SLB instances. |   |   | The SLB instances cannot work as normal. |   |   | Restore the tags. |   |   |   |
|   | Modify the configurations of the SLB instances that are managed by ACK, including the configurations of the instances, listeners, and vServer groups. |   |   | The SLB instances do not work as normal. |   |   | Restore the SLB configurations. |   |   |   |

|   | net.ipv4.tcp tw reuse = _ _ |
|---|---|
| 1 |   |

|   |   | net.ipv4.tcp tw reuse = _ _ |
|---|---|---|
|   | 0 |   |

|   | net.ipv4.tcp tw recycle = _ _ |   |
|---|---|---|
| 1 |   |   |

|   |   | net.ipv4.tcp tw recycle = _ _ |   |
|---|---|---|---|
|   | 0 |   |   |

| net.ipv4.ip local port ran _ _ _ | o |
|---|---|

|   |   | net.ipv4.ip local port ran _ _ _ |
|---|---|---|
|   | ge="32768 60999" |   |

| Remove the annotation service.beta.kubernetes.io |   |   | Add the annotation to the Service configuration. Note If a Service is configured to use an existing SLB instance, you cannot modify the configuration to create a new SLB instance for the Service. To use a new SLB instance, you must create a new Service. |   |
|---|---|---|---|---|
|   | service.beta.kubernetes.io |   |   | Note If |
| /alibaba-cloud- |   |   |   |   |
|   |   | The existing SLB ins |   |   |
|   |   | T |   |   |
| loadbalancer-id: |   | is |   |   |
| ${YOUR LB ID} _ _ |   |   |   |   |
| Delete the SLB instances that are created by ACK in the SLB console. |   | Errors may occur in the cluster network. | Delete SLB instances by deleting the Services that are associated with the SLB instances. |   |

|   | Manually delete the nginx- ingress-lb Service in the kube-system namespace of a cluster that has the NGINX Ingress controller installed. | The NGINX Ingress controller does not run as normal or may stop running. | Use the following YAML template to create a Service that has the same name: apiVersion: v1 kind: Service metadata: annotations: labels: app: nginx-ingress- lb name: nginx-ingress-lb namespace: kube-system spec: externalTrafficPolicy: Local ports: - name: http port: 80 protocol: TCP targetPort: 80 - name: https port: 443 protocol: TCP targetPort: 443 selector: app: ingress-nginx type: LoadBalancer |
|---|---|---|---|
|   | ingress-lb |   |   |

| nginx- |   |
|---|---|

**High-risk operations on storage**

| High-risk operation | Impact | How to recover |
|---|---|---|
| Unmount cloud disks that are mounted to pods in the ECS console. | I/O errors occur when you write data to the pods. | Restart the pods and clear residual data on the nodes. |
| Unmount disks from their mount paths on nodes. | Pod data is written to local disks. | Restart the pods. |
| Manage cloud disks on the nodes. | Pod data is written to local disks. | Unrecoverable. |
| Mount a cloud disk to multiple pods. | Pod data is written to local disks or I/O errors occur when you write data to the pods. | Mount the cloud disk only to one pod. |
| Manually delete the NAS directories that are mounted to pods. | I/O errors occur when you write data to the pods. | Restart the pods. |
| Delete the NAS file systems that are mounted to pods or delete the mount targets that are used to mount NAS file systems. | I/O hangs occur when you write data to the pods. | Restart the ECS instances. |

**High-risk operations on logs**

| High-risk operation | Impact | How to recover |
|---|---|---|
| Delete the /tmp/ccs-log- collector/pos directory on a node. | Duplicate logs are collected. | Unrecoverable. The /tmp/ccs- log-collector/pos directory contains information about the path from which logs are collected. |
| Delete the /tmp/ccs-log- collector/buffer directory on a node. | Logs are lost. | Unrecoverable. The /tmp/ccs- log-collector/buffer directory stores cached log files that need to be consumed. |
| Delete the aliyunlogconfig CustomResourceDefinition (CRD) objects. | Logs cannot be collected. | Recreate the aliyunlogconfig CRD objects that are deleted and the related resources. Logs that are generated within the period of time during which the aliyunlogconfig CRD objects do not exist cannot be collected. If you delete the aliyunlogconfig CRD objects, the related log collection tasks are also deleted. After you recreate the aliyunlogconfig CRD objects, you must also relaunch the log collection tasks. |

| Uninstall logging components. | Logs cannot be collected. | Reinstall the logging component and manually create the aliyunlogconfig CRD objects. Logs that are generated within the period of time during which the logging component and the aliyunlogconfig CRD objects do not exist cannot be collected. If you delete the logging component, the aliyunlogconfig CRD objects and Logtail are also deleted. Logs that are generated within the period of time during which the logging component does not exist cannot be collected. |
|---|---|---|

## 2 Architecture

### 2.1 System architecture

This topic describes the system architecture of Container Service for Kubernetes (ACK). Container Service is adapted and enhanced based on native Kubernetes. This service simplifies cluster creation and scaling, and is integrated with Apsara Stack virtualization, storage, network, and security capabilities. This service provides the optimal environment to run Kubernetes-based containerized applications in the cloud.

| Feature | Description |
|---|---|
| Dedicated Kubernetes mode | Integrated with Apsara Stack virtualization technologies, the service allows you to create dedicated Kubernetes clusters. You can use Elastic Compute Service (ECS), Elastic GPU Service (EGS), and ECS Bare Metal instances as cluster nodes. You can deploy a wide range of plug-ins and configure various specifications for the instances. |
| Cluster management and control | The service provides powerful network, storage, cluster management, scaling, and application extension features. |
| Kubernetes management | The service supports secure images and is integrated with Apsara Stack Resource Access Management (RAM), Key Management Service (KMS), and logging and monitoring services to provide a secure and compliant Kubernetes solution. |

| Convenient and efficient use | ACK provides services through the web console, APIs, and SDK. |
|---|---|

### 2.2 Architecture

This topic describes the component architecture of Container Service for Kubernetes (ACK).

| Category | Component | Description |
|---|---|---|
| Apsara Stack Container Service console | CosConsoleAliyunCom | The console that is used to manage clusters, nodes, and applications. |
|   | Backend | Dashboard. |
| Apsara Stack Container Service controller | Troopers | Controller backend. |
|   | RC | Component installation service. |
|   | CloudAccessVpc | Reverse tunneling. |
|   | Cert | Static file service. |
|   | CertControl | Component certificate signing. |
|   | Registry | Image service. |
| > Document Version: 20241213 | 1 |   |

|   | Mirana | API server traffic forwarding. |
|---|---|---|
|   | Certificate | Certificate update. |
| ACK tools | ControlInit | Data initialization and API registration. |
|   | ServiceTest | Self-check service. |
|   | DiagnosticTool | Quick diagnostic tool. |

### 2.3 Deployment architecture

This topic describes the deployment architecture of Container Service for Kubernetes (ACK).

| Component | Deployment method |
|---|---|
| Apsara Stack Container Service console | Containerized deployment |
| Apsara Stack Container Service controller | Containerized deployment |
| Container Service tools | Containerized deployment |

### 2.4 Server roles

This topic describes the server roles of Container Service for Kubernetes (ACK).

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|

| acs | AcsControlCluste r | acs-acs control _ | ControlInit | Data initialization and API registration. |
|---|---|---|---|---|
|   |   |   | Troopers | Controller backend. |
|   |   |   | CloudAccessVpc | Reverse tunneling. |
|   |   |   | Cert | Static file service. |
|   |   |   | CertControl | Component certificate signing. |
|   |   |   | Registry | Image service. |
|   |   |   | Mirana | API server traffic forwarding. |
|   |   |   | Backend | Dashboard. |
|   |   |   | CosConsoleAliyun Com | Console. |
|   |   |   | Certificate | Certificate updates. |
|   |   |   | ServiceTest | Self-check service. |
|   |   |   | DiagnosticTool | Quick diagnostic tool. |

## 3 Components and features

### 3.1 Console

The Container Service for Kubernetes (ACK) console provides a graphical user interface (GUI) that serves as a portal for all operations on ACK. The ACK console uses the deployment mode that applies to standard Java applications on Apsara Stack. The ACK console consists of a Tengine server and a Jetty container.

**Procedure**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Base/Platforms > Apsara Infrastructure Management**.
2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
3. On the **Project O&M** page, enter
`acs` in the **Project | Cluster** search box. Find the acs
4. On the cluster details page, click the **Services** tab and then click **acs-acs_control**.
5. On the **Serviceacs-acs_control** page, click **CosConsoleAliyunCom#** in the left-side
**Components** list. Click the **Instances** tab to view the machines on which the service role
(component) is deployed.
6. Click **Terminal** in the **Actions** column of the target machine. On the **TerminalService**
page, run the `docker ps` command to query the ID of the cos-console-aliyun-com container.
7. Run the `sudo docker exec -it container_id bin/bash` command to log on to the
container.
8. Enter the directory to find Tengine and Jetty.

**O&M commands**

Restart Tengine: `/etc/rc.d/init.d/tengine restart` Restart Jetty: `/etc/init.d/jetty restart`

**Directory structure**

The root directory of web applications: `/alidata/www/` The WAR directory of applications: /alidata/www/wwwroot/cos-console-aliyun-com

### 3.2 Troopers

The Troopers component is used to create clusters and machines. You can also use Troopers to manage clusters and machines in Container Service. Troopers is programmed in Go. Each container runs only the Troopers daemon and does not run any other daemons. This topic describes how to use the Troopers component.

**Procedure**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Base/Platforms > Apsara Infrastructure Management**.
2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
3. On the **Projects** page, enter
`acs` into the **Product | Cluster** search box. Find the acs
4. On the cluster details page, click the **Services** tab and then click **acs-acs_control**.
5. On the **Serviceacs-acs_control** page, click **Troopers#** in the left-side **Components** list.
Click the **Instances** tab, and then click **Terminal** in the **Actions** column to go to the
**TerminalService** page.
6. In the left-side navigation pane, enter the hostname in the Machine search box. Move the
pointer over the More icon next to the hostname and choose Terminal from the shortcut menu. This allows you to log on to the machine by using a terminal session. On the command line, enter `docker ps` to query the ID of the Troopers container.
7. Run the `sudo docker exec -it container_id bin/bash` command to log on to the
container.

**Container directory structure**

/usr/aliyun/acs/troopers: the root directory of the application. troopers: the main program of Troopers. troopers.json: the configuration file of Troopers. troopers.ym: the configurations of certificate encryption. start.sh: the entry script used to start Troopers. If the Troopers daemon already exists, do not run the start.sh script. /opt/aliyun/install/check_health.sh: the script that is used to run health checks. /usr/aliyun/acs/certs/control: the directory that stores a certificate. Troopers uses the certificate to access the Region Controller (RC). You can use OpenSSL to validate the certificate.

### 3.3 Mirana

This topic describes the deployment modes and features of Mirana.

**Procedure**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Base/Platforms > Apsara Infrastructure Management**.
2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
3. On the **Projects** page, enter
`acs` into the **Product | Cluster** search box. Find the acs
4. On the cluster details page, click the **Services** tab and then click **acs-acs_control**.
5. On the **Serviceacs-acs_control** page, click **Mirana#** in the left-side **Components** list.
Click the **Instances** tab to view the machines on which the service role (component) is deployed.

**Deployment modes**

Mirana containers are deployed on control machines and use HTTPS to provide services. Mirana requires the Kubernetes API certificate that is provided by Troopers.

**Features**

Allows you to deploy applications to Kubernetes by using Kompose. Allows you to use the Helm client to manage orchestration templates. Allows you to call API operations to perform blue-green deployments. Serves as the proxy for Kubernetes-native API operations.

## 4 System restart

### 4.1 Restart a control node

Control nodes run as Docker containers where services such as CosConsoleAliyunCom, Troopers, and the etcd are deployed. This topic describes how to restart a control node.

**Procedure**

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Infrastructure Management**.
2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Product & Cluster O&M**.
3. On the **Projects** page, enter
`acs` into the **Product | Cluster** search box. Find the acs
4. On the cluster details page, click the **Services** tab and then click **acs-acs_control**.
5. In the left-side **Components** list, click the component that you want to manage. Click the
**Instances** tab, and then click **Terminal** in the **Actions** column of the instance that you
want to manage to go to the TerminalService page.
6. Log on to the terminal of the machine and run the docker ps|grep [app] command to
query the container ID. `[app]` specifies the name of the application that is deployed in the container. You can query the container ID by using the application name.
7. Run the `docker restart container_id` command to restart the container.
l components

## 5 Manage certificates for control components

**control components**

If you do not renew expired certificates for control components, you cannot use the control components. You must renew a certificate within one week after the certificate expires. This topic describes how to query the certificate expiration time and renew a certificate for a control component.

**Prerequisites**

The permissions to access control components are granted.

**Query the certificate expiration time**

**Method 1: Query the component creation time to determine**

**the certificate expiration time**

Log on to the control component and query the creation time of the component. The certificate of the control component expires four years after the control component is created. In the following steps, the Troopers component is used as an example.
1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Base/Platforms > Apsara Infrastructure Management**.
2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
3. On the **Project O&M** page, enter **acs** in the **Project | Cluster** search box. Find the acs
4. On the cluster details page, click the service that you want to manage on the **Services** tab.
5. In the **Components** list, click the Troopers component (service role). On the **Instances**
tab, click **Terminal** in the **Actions** column to go to the **TerminalService** page.
6. On the left of the **TerminalService** page, click a machine and run the following command
in the CLI on the right of the page to query the time when the container was started. The start time of the container is the same as the creation time of the control component.

```bash
docker ps | grep troopers
```

The certificate of the control component expires four years after the control component is created.

**Method 2: Log on to the component container to query the**

**certificate expiration time**

l components

> **Note:** We recommend that you use this method to query the certificate expiration time because this method produces more accurate results.

1. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
> **Base/Platforms** > **Apsara Infrastructure Management**.

2. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
3. On the **Project O&M** page, enter **acs** in the **Project | Cluster** search box. Find the acs
4. On the cluster details page, click the service that you want to manage on the **Services** tab.
5. In the **Components** list, click the Troopers component (service role). On the **Instances**
tab, click **Terminal** in the **Actions** column to go to the **TerminalService** page.
6. On the left of the **TerminalService** page, click a machine and run the following command
in the CLI on the right of the page to enter the certificate directory.

```
cd /usr/aliyun/acs/certs/control
```

7. Copy the cert.pem file in the certificate directory to your on-premises Linux environment.

> **Note:** You must install OpenSSL in your on-premises Linux environment before you copy the file.

8. Run the following command to query the certificate expiration time:

```
openssl x509 -in cert.pem -noout -text
```

Expected output:

```
Validity
            Not Before: Dec 23 16:02:00 2020 GMT
            Not After : Dec 22 16:07:40 2024 GMT
```

The time that follows `Not After` in the `Validity` field is the expiration time of the certificate.

**Renew the certificate for a control component**

1. Log on to the control database and delete all data entries about signed certificates for
components such as Console, Mirana, and Troopers. These data entries start with the string

```
 manager .
```

i. In the top navigation bar of the Apsara Uni-manager Operations Console, choose
**Products** > **Base/Platforms** > **Apsara Infrastructure Management**.
ii. In the left-side navigation pane of the **Apsara Infrastructure Management** page, click
**Project & Cluster O&M**.
iii. On the **Project O&M** page, enter **acs** in the **Project | Cluster** search box. Find the acs iv. On the cluster details page, click the **Resource Details** tab and enter the name of the resource that you want to manage in the **Resource Name** field. l components v. In the **Resource Application Result** column, click the icon and then click the hyperlink that is displayed. In the **Resource Application Result** dialog box, you can view information about how to log on to the database. vi. Log on to an OPS machine or a VM in the cluster. vii. Run the following command to log on to the database: Replace the parameters in the following command with the information that you obtained in Step e.

```
mysql -h${db_host} -P${db_port} -u${db_user} -D${dbName} -p
```

Enter the database password in the output. viii. Run the following command to delete the certificates of control components:

```
delete from cert_info where path like "manager/%";
```

ix. Run the following command to check whether the certificates are deleted:

```
select path, created_at from cert_info where path like "manager/%" \G;
```

The output is empty, which indicates that the certificates are deleted.
2. Restart the CertControl component.
Chest is used to sign the certificates for the control components used in ACK clusters that are deployed in Apsara Stack. Chest is deployed as an HTTP server and provides interfaces that are used to sign certificates for the control components. i. In the top navigation bar of the Apsara Uni-manager Operations Console, choose
**Products > Base/Platforms > Apsara Infrastructure Management** .
ii. In the left-side navigation pane of the **Apsara Infrastructure Management** console, click **Project & Cluster O&M**. iii. On the **Project O&M** page, enter **acs** in the **Project | Cluster** search box. Find the acs iv. On the cluster details page, click the service that you want to manage on the **Services** tab. v. In the **Components** list, click the CertControl component (service role). On the
**Instances** tab, choose **Actions** > **Restart** in the **Actions** column.
vi. In the **Confirmation** dialog box, enter **RESTART** and click **OK**.
3. Check whether data entries about component certificates are regenerated in the cert_info
table. These data entries start with the string `manager/` . i. Run the following command to log on to the database: Replace the parameters in the following command with the logon information that you obtained in Step 1.

```
mysql -h${db_host} -P${db_port} -u${db_user} -D${dbName} -p
```

Enter the database password in the output. ii. Run the following command to query the certificate:

```
select path, created_at from cert_info where path like "manager/%" \G;
```

The result indicates that the certificates are regenerated. l components
4. Restart control components.
Restart the following control components: Certificate, Console, Mirana, Static, and Troopers. The startup script of each component image sends a request to the download-cert interface provided by Chest to download a new certificate. The new certificate is valid for four years. The steps to restart a control component are similar to the steps to restart the CertControl component. For more information, see Restart the CertControl component.
5. Check whether the components are restarted.
In the following steps, the Troopers component is used as an example. i. In the top navigation bar of the Apsara Uni-manager Operations Console, choose
**Products** > **Base/Platforms** > **Apsara Infrastructure Management**.
ii. In the left-side navigation pane of the **Apsara Infrastructure Management** console, click **Project & Cluster O&M**. iii. On the **Project O&M** page, enter acs in the **Project | Cluster** search box. Find the acs iv. On the cluster details page, click the service that you want to manage on the **Services** tab. v. In the **Components** list, click the Troopers component (service role). On the **Instances** tab, click **Terminal** in the **Actions** column to log on to the machine. vi. Check whether the certificate exists. a. Run the following command to query the container ID:

```bash
docker ps | grep troopers
```

b. Run the following command to log on to the container:

```bash
docker exec -it <certificate ID> bash
```

c. Run the following command to go to the directory of the certificate:

```
cd /usr/aliyun/ace/certs/control
```

d. Run the following command to query the certificate: `ls` vii. Check whether the certificate expiration time is renewed. a. Copy the cert.pem file in the certificate directory to your on-premises Linux environment. b. Run the following command to query the certificate expiration time:

```
openssl x509 -in cert.pem -noout -text
```

The time that follows `Not After` in the `Validity` field is the expiration time of the certificate.

```
Validity
            Not Before: Dec 23 16:02:00 2020 GMT
            Not After : Dec 22 16:07:40 2024 GMT
```
